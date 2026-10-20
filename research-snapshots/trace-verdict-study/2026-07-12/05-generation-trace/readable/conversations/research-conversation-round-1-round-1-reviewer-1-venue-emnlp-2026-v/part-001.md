# Research conversation: [Round 1 审稿请求]: ## Round 1 审稿任务 — Reviewer 1 **你的审查侧重**: 方法严谨性 + 实验设计 + 统计有效性 + 可复现性 ### Venue 信息 - **目标**: EMNLP 2026 v — Part 1 of 12

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects (July export snapshot)** · Conversation logs

[Transcript overview](../research-conversation-round-1-round-1-reviewer-1-venue-emnlp-2026-v.md) · [Part 2 →](part-002.md) · [Structured JSON](../../../sessions/c6/c6e44f5b86369a9cda20.json)

## Before a recorded user message

## Before a recorded user message

2 recorded events


### Runtime record

_source line 1 · 2026-05-17T18:01:46.664Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-17T18:01:46.664Z",
  "sessionId": "f76386b4-9d1f-4f92-b831-706bc4acd94d",
  "content": "[Round 1 审稿请求]:\n## Round 1 审稿任务 — Reviewer 1\n\n**你的审查侧重**: 方法严谨性 + 实验设计 + 统计有效性 + 可复现性\n\n### Venue 信息\n- **目标**: EMNLP 2026 via ARR May 2026 cycle\n- **截止日期**: 2026-05-25\n- **页数限制**: Long paper ≤ 8 页正文（不含 Limitations/Ethics/References）\n- **模板**: ACL style, `\\usepackage[review]{acl}`, double-blind\n- **匿名规则**: 作者信息不得出现，自引需避免泄露身份\n- **评分标准**: EMNLP 2026 通过 ARR 统一审稿，Overall Assessment: 5=Consider for Award, 4=Conference, 3=Findings, 2=Resubmit next cycle, 1=Do not resubmit\n\n### 论文路径\n- 主文件: `projects/trace-verdict-study/docs/paper/main.tex`\n- 各章节: introduction.tex, method.tex, experiments.tex, discussion.tex, related_work.tex, conclusion.tex, appendix.tex\n- 引用: references.bib\n- ARR checklist: arr_checklist.tex\n\n### 论文概述\n标题: \"Exception Events Are All You Need: Component Ablation for Trace-Based Verdict Prediction\"\n核心声明: Exception events 单独实现 ≥99.33% verdict accuracy（4 个模型, 1.5B-13B, 3 个架构家族），比 full trace 和 VOTA 更好。提出 gradient dilution (~26%) vs information overload (~74%) 分解。\n\n### 你需要重点审查的方面\n\n1. **统计有效性**:\n   - exception_only 测试集 49% 重复（1190 样本仅 607 unique）——Wilson CI 独立性假设是否被违反？所有 p 值和 CI 是否可信？\n   - 6/7 实验条件为单 seed，Tier 1 vs Tier 2 层级划分的统计稳定性\n   - DeepSeek seed 123 异常值 (91.09%) 的归因是否有充分证据\n   - McNemar test 和 bootstrap resampling 在重复样本下的有效性\n\n2. **实验设计**:\n   - 26%/74% gradient dilution vs information overload 分解的因果推断有效性（label_only 是否引入混淆变量？）\n   - 数据生成循环依赖：Qwen 生成候选解且 Qwen 做评估模型\n   - 模型覆盖度：4 个模型是否足够支撑 \"cross-model\" 和 \"architecture-independent\" 声明？\n   - DebugBench 天花板效应（no_trace 已 96.71%）能否独立验证 trace 贡献？\n   - 2048 token 截断对不同条件的差异化影响\n\n3. **可复现性**:\n   - 超参数报告完整度\n   - 代码/数据发布计划\n   - DeepSeek full_trace 初始 run 被 invalidated 的处理\n   - 硬件报告（RTX PRO 6000 Blackwell）\n\n4. **方法论**:\n   - format marker ([No exception data in trace]) 使 B5 regex 达 99.33%——SFT 的 0.50pp 增量是否足以证明 \"learned semantic understanding\"？\n   - nomarker ablation 下降 ~2pp 的解读\n   - VOTA 设计空间是否被充分探索\n\n请产出完整审稿报告，包含 Summary / Strengths / Weaknesses / Questions / Missing References / Detailed Comments / Overall Assessment（按 EMNLP 评分标准打分）。"
}
```

---


### Runtime record

_source line 2 · 2026-05-17T18:01:46.667Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-17T18:01:46.667Z",
  "sessionId": "f76386b4-9d1f-4f92-b831-706bc4acd94d"
}
```

---


## Round 1

## Round 1

60 recorded events


### User

_source line 3 · 2026-05-17T18:01:46.703Z_

[Round 1 审稿请求]:
## Round 1 审稿任务 — Reviewer 1

**你的审查侧重**: 方法严谨性 + 实验设计 + 统计有效性 + 可复现性

### Venue 信息
- **目标**: EMNLP 2026 via ARR May 2026 cycle
- **截止日期**: 2026-05-25
- **页数限制**: Long paper ≤ 8 页正文（不含 Limitations/Ethics/References）
- **模板**: ACL style, `\usepackage[review]{acl}`, double-blind
- **匿名规则**: 作者信息不得出现，自引需避免泄露身份
- **评分标准**: EMNLP 2026 通过 ARR 统一审稿，Overall Assessment: 5=Consider for Award, 4=Conference, 3=Findings, 2=Resubmit next cycle, 1=Do not resubmit

### 论文路径
- 主文件: `projects/trace-verdict-study/docs/paper/main.tex`
- 各章节: introduction.tex, method.tex, experiments.tex, discussion.tex, related_work.tex, conclusion.tex, appendix.tex
- 引用: references.bib
- ARR checklist: arr_checklist.tex

### 论文概述
标题: "Exception Events Are All You Need: Component Ablation for Trace-Based Verdict Prediction"
核心声明: Exception events 单独实现 ≥99.33% verdict accuracy（4 个模型, 1.5B-13B, 3 个架构家族），比 full trace 和 VOTA 更好。提出 gradient dilution (~26%) vs information overload (~74%) 分解。

### 你需要重点审查的方面

1. **统计有效性**:
   - exception_only 测试集 49% 重复（1190 样本仅 607 unique）——Wilson CI 独立性假设是否被违反？所有 p 值和 CI 是否可信？
   - 6/7 实验条件为单 seed，Tier 1 vs Tier 2 层级划分的统计稳定性
   - DeepSeek seed 123 异常值 (91.09%) 的归因是否有充分证据
   - McNemar test 和 bootstrap resampling 在重复样本下的有效性

2. **实验设计**:
   - 26%/74% gradient dilution vs information overload 分解的因果推断有效性（label_only 是否引入混淆变量？）
   - 数据生成循环依赖：Qwen 生成候选解且 Qwen 做评估模型
   - 模型覆盖度：4 个模型是否足够支撑 "cross-model" 和 "architecture-independent" 声明？
   - DebugBench 天花板效应（no_trace 已 96.71%）能否独立验证 trace 贡献？
   - 2048 token 截断对不同条件的差异化影响

3. **可复现性**:
   - 超参数报告完整度
   - 代码/数据发布计划
   - DeepSeek full_trace 初始 run 被 invalidated 的处理
   - 硬件报告（RTX PRO 6000 Blackwell）

4. **方法论**:
   - format marker ([No exception data in trace]) 使 B5 regex 达 99.33%——SFT 的 0.50pp 增量是否足以证明 "learned semantic understanding"？
   - nomarker ablation 下降 ~2pp 的解读
   - VOTA 设计空间是否被充分探索

请产出完整审稿报告，包含 Summary / Strengths / Weaknesses / Questions / Missing References / Detailed Comments / Overall Assessment（按 EMNLP 评分标准打分）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "b73967ab-1e3d-4502-97ef-ede23a2a2cd7",
  "type": "user",
  "uuid": "89ea9655-9e76-428b-a779-6032d2f9be7b",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/.claude/sessions/review_reviewer_1_7624f219",
  "sessionId": "f76386b4-9d1f-4f92-b831-706bc4acd94d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Runtime record

_source line 4 · 2026-05-17T18:01:46.703Z_

```json
{
  "parentUuid": "89ea9655-9e76-428b-a779-6032d2f9be7b",
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
  "uuid": "cd15d9e8-2b31-4532-b361-73345bbf7931",
  "timestamp": "2026-05-17T18:01:46.703Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/.claude/sessions/review_reviewer_1_7624f219",
  "sessionId": "f76386b4-9d1f-4f92-b831-706bc4acd94d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---


### Runtime record

_source line 5 · 2026-05-17T18:01:46.703Z_

```json
{
  "parentUuid": "cd15d9e8-2b31-4532-b361-73345bbf7931",
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
  "uuid": "9ee2895f-49f2-4516-a7a9-681b5d435649",
  "timestamp": "2026-05-17T18:01:46.703Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/.claude/sessions/review_reviewer_1_7624f219",
  "sessionId": "f76386b4-9d1f-4f92-b831-706bc4acd94d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---


### Runtime record

_source line 6 · 2026-05-17T18:01:46.703Z_

```json
{
  "parentUuid": "9ee2895f-49f2-4516-a7a9-681b5d435649",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "d118179f-d6f8-4f59-ab80-fa31266ce7df",
  "timestamp": "2026-05-17T18:01:46.703Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/.claude/sessions/review_reviewer_1_7624f219",
  "sessionId": "f76386b4-9d1f-4f92-b831-706bc4acd94d",
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
  "aiTitle": "Round 1 peer review for trace verdict prediction paper",
  "sessionId": "f76386b4-9d1f-4f92-b831-706bc4acd94d"
}
```

---


### Assistant

_source line 8 · 2026-05-17T18:01:51.859Z_

<details><summary>Logged reasoning block</summary>

```text
The user (Review Director) is asking me to perform a Round 1 review of a paper titled "Exception Events Are All You Need: Component Ablation for Trace-Based Verdict Prediction" for EMNLP 2026. I need to:

1. First, run the session start skill
2. Search for EMNLP 2026 / ACL ARR reviewer guidelines
3. Read the paper thoroughly
4. Produce a detailed review

Let me start by reading the paper and searching for reviewer guidelines in parallel.

Let me first load the necessary tools and read the paper files.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d118179f-d6f8-4f59-ab80-fa31266ce7df",
  "isSidechain": false,
  "requestId": "req_011Cb8aZEmER2djBdevPfKhi",
  "type": "assistant",
  "uuid": "c4e40674-2825-4eb4-a0db-46d18e20589e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/.claude/sessions/review_reviewer_1_7624f219",
  "sessionId": "f76386b4-9d1f-4f92-b831-706bc4acd94d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SviZ8oB2bphhAmK3h3AsHb",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15619,
      "cache_read_input_tokens": 11841,
      "output_tokens": 322,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 15619,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 322,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 15619,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 15619
          },
          "type": "message"
        }
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

_source line 9 · 2026-05-17T18:01:52.947Z_

开始执行 Round 1 审稿。先并行完成：(1) 搜索 ACL ARR reviewer guidelines，(2) 读取论文各章节。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c4e40674-2825-4eb4-a0db-46d18e20589e",
  "isSidechain": false,
  "requestId": "req_011Cb8aZEmER2djBdevPfKhi",
  "type": "assistant",
  "uuid": "d78e3361-c7cf-42a7-bfa1-4a484ba0249b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/.claude/sessions/review_reviewer_1_7624f219",
  "sessionId": "f76386b4-9d1f-4f92-b831-706bc4acd94d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SviZ8oB2bphhAmK3h3AsHb",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15619,
      "cache_read_input_tokens": 11841,
      "output_tokens": 322,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 15619,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 322,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 15619,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 15619
          },
          "type": "message"
        }
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

_source line 10 · 2026-05-17T18:01:54.034Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01BcgxeQsqZbTKMSUiVeRLE4`</summary>

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
  "parentUuid": "d78e3361-c7cf-42a7-bfa1-4a484ba0249b",
  "isSidechain": false,
  "requestId": "req_011Cb8aZEmER2djBdevPfKhi",
  "type": "assistant",
  "uuid": "18257bb5-17bb-4c45-8fe6-1d26c3ce1485",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/.claude/sessions/review_reviewer_1_7624f219",
  "sessionId": "f76386b4-9d1f-4f92-b831-706bc4acd94d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SviZ8oB2bphhAmK3h3AsHb",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15619,
      "cache_read_input_tokens": 11841,
      "output_tokens": 322,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 15619,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 322,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 15619,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 15619
          },
          "type": "message"
        }
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

_source line 11 · 2026-05-17T18:01:54.041Z_

<details><summary>↩ Tool result · `toolu_01BcgxeQsqZbTKMSUiVeRLE4`</summary>

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
  "parentUuid": "18257bb5-17bb-4c45-8fe6-1d26c3ce1485",
  "isSidechain": false,
  "promptId": "b73967ab-1e3d-4502-97ef-ede23a2a2cd7",
  "type": "user",
  "uuid": "dccd0e6f-945e-4773-a719-36a1859dabff",
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
  "sourceToolAssistantUUID": "18257bb5-17bb-4c45-8fe6-1d26c3ce1485",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/.claude/sessions/review_reviewer_1_7624f219",
  "sessionId": "f76386b4-9d1f-4f92-b831-706bc4acd94d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Assistant

_source line 12 · 2026-05-17T18:01:57.092Z_

<details><summary>Logged reasoning block</summary>

```text
Now let me start reading the paper and searching for reviewer guidelines in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dccd0e6f-945e-4773-a719-36a1859dabff",
  "isSidechain": false,
  "requestId": "req_011Cb8aZnVhhhvUsy3JCV6wc",
  "type": "assistant",
  "uuid": "439d1252-a29c-4d59-a56f-ce81d6b8eb5a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/.claude/sessions/review_reviewer_1_7624f219",
  "sessionId": "f76386b4-9d1f-4f92-b831-706bc4acd94d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015HcLXzF3feTTdP4sPwbUoc",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2318,
      "cache_read_input_tokens": 27460,
      "output_tokens": 375,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2318,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 375,
          "cache_read_input_tokens": 27460,
          "cache_creation_input_tokens": 2318,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2318
          },
          "type": "message"
        }
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

_source line 13 · 2026-05-17T18:01:57.659Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01TgpXmXxrrLJMtvVRnCNe3P`</summary>

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
  "parentUuid": "439d1252-a29c-4d59-a56f-ce81d6b8eb5a",
  "isSidechain": false,
  "requestId": "req_011Cb8aZnVhhhvUsy3JCV6wc",
  "type": "assistant",
  "uuid": "3b467e14-9207-4f61-a604-6c1069362688",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/.claude/sessions/review_reviewer_1_7624f219",
  "sessionId": "f76386b4-9d1f-4f92-b831-706bc4acd94d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015HcLXzF3feTTdP4sPwbUoc",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2318,
      "cache_read_input_tokens": 27460,
      "output_tokens": 375,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2318,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 375,
          "cache_read_input_tokens": 27460,
          "cache_creation_input_tokens": 2318,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2318
          },
          "type": "message"
        }
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

_source line 14 · 2026-05-17T18:01:58.989Z_

<details open><summary>🔧 Tool call — Read · `toolu_01X7rp3PutYYjTEEW5iMKMzz`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3b467e14-9207-4f61-a604-6c1069362688",
  "isSidechain": false,
  "requestId": "req_011Cb8aZnVhhhvUsy3JCV6wc",
  "type": "assistant",
  "uuid": "feab2720-657b-436b-abed-df44ef10c6bb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/.claude/sessions/review_reviewer_1_7624f219",
  "sessionId": "f76386b4-9d1f-4f92-b831-706bc4acd94d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015HcLXzF3feTTdP4sPwbUoc",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2318,
      "cache_read_input_tokens": 27460,
      "output_tokens": 375,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2318,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 375,
          "cache_read_input_tokens": 27460,
          "cache_creation_input_tokens": 2318,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2318
          },
          "type": "message"
        }
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

_source line 15 · 2026-05-17T18:01:58.998Z_

<details><summary>↩ Tool result · `toolu_01X7rp3PutYYjTEEW5iMKMzz`</summary>

```text
1	\documentclass[11pt,a4paper]{article}
2	\usepackage[review]{acl}
3	% \usepackage{acl}  % uncomment for camera-ready (remove [review])
4	\usepackage{times,latexsym}
5	\usepackage{amsmath,amssymb}
6	\usepackage{graphicx}
7	\graphicspath{{../../figures/paper/}}
8	\usepackage{booktabs}
9	\usepackage{multirow}
10	\usepackage{xcolor}
11	
12	\title{Exception Events Are All You Need: \\Component Ablation for Trace-Based Verdict Prediction}
13	\author{Anonymous ACL submission}
14	
15	\begin{document}
16	\maketitle
17	
18	\begin{abstract}
19	Execution traces are increasingly used to enhance code language models, but which trace components matter for downstream tasks remains poorly understood.
20	We present the first systematic component ablation of trace representations for verdict prediction (classifying whether a test passes or fails) across four models spanning three architecture families and 1.5B to 13B parameters.
21	Exception events alone achieve ${\geq}$99.33\% accuracy across all four models (${\geq}$99.83\% on three of four; one seed reaches 100\%), while a code-only baseline shows 9.19pp scale sensitivity (67.3--76.5\%).
22	Adding more trace information actively hurts: a multi-component representation underperforms exception-only, and the full-trace gap approximately decomposes into information overload (${\sim}$74\%) and gradient dilution (${\sim}$26\%).
23	Tail-truncation experiments reveal that diagnostic signal concentrates near the trace terminus (in a localized window, not the absolute end), recovering 86\% of the gap to exception-only.
24	A format-marker ablation confirms ${\sim}$91\% of the exception signal is semantic (learned by SFT to distinguish caught from uncaught exceptions) rather than format-driven.
25	These results reveal a two-tier diagnostic hierarchy: Tier~1 signals (exception events, assertion points) individually achieve ${\geq}$99\%, while Tier~2 (loop compression) reaches 85.6\%.
26	Cross-dataset evaluation on DebugBench ($N{=}426$) confirms generalization, with exception-only achieving 100\%.
27	We reframe verdict prediction as fault detection: the minimal sufficient signal is a compact exception event (median 150 tokens) that is scale-invariant, architecture-independent, and deployable in token-constrained settings.
28	\end{abstract}
29	
30	\input{introduction}
31	\input{method}
32	\input{experiments}
33	\input{discussion}
34	\input{related_work}
35	\input{conclusion}
36	
37	\section*{Limitations}
38	
39	Our study has several limitations.
40	First, our primary experiments use a single dataset (591 problems from HumanEval and MBPP-sanitized); while a cross-dataset evaluation on DebugBench (\S\ref{sec:debugbench}) confirms that exception dominance generalizes to synthetically injected bugs, generalization to other languages, larger codebases, or real-world fault distributions remains untested.
41	Second, while we evaluate four models spanning 1.5B to 13B parameters across three architecture families, all are code-specialized; generalization to general-purpose models or larger scales remains untested.
42	Third, DeepSeek \texttt{exception\_only} exhibits seed-dependent variance: 2/3 seeds achieve 99.33\% while seed 123 yields 91.09\% ($\sigma{=}4.76$pp, $n{=}3$), which we hypothesize reflects LoRA initialization sensitivity in DeepSeek-Coder, though direct evidence is lacking (fail recall = 70.5\% for the outlier vs.\ 100\% for others).
43	Qwen \texttt{exception\_only} shows perfect seed robustness ($\sigma{=}0$, $n{=}3$), but Qwen \texttt{ae\_only} also exhibits seed variance ($\sigma{=}$0.40pp; seed 123 = 99.08\% vs.\ seeds 42/456 = 99.92\%), though far smaller than DeepSeek's ($\sigma{=}$4.76pp).
44	Whether training stabilization techniques can eliminate DeepSeek's seed sensitivity is unexplored; other conditions use a single seed.
45	Fourth, the initial DeepSeek \texttt{full\_trace} run was invalidated by context overflow; a re-run with extended context yields 79.16\% (CI [76.80\%, 81.30\%]), 2.60pp below Qwen (Table~\ref{tab:cross_model}).
46	Fifth, the candidate solutions were generated by Qwen-2.5-Coder-7B-Instruct, which also serves as one of our evaluation models; this does not affect verdict prediction but may influence the pass/fail distribution.
47	Sixth, self-familiarity bias may inflate absolute accuracy: both Qwen-2.5-Coder and DeepSeek-Coder were likely exposed to HumanEval and MBPP solutions during pretraining, so the models may partially recognize solutions rather than purely reasoning from trace signals; our cross-dataset evaluation on DebugBench mitigates but does not eliminate this concern.
48	Seventh, the error distribution in our test set may not reflect real-world fault distributions: exceptions (especially \texttt{TypeError}, \texttt{ValueError}) dominate LLM-generated failures, but production code may exhibit a broader spectrum of silent logic errors where no exception is raised, potentially reducing the effectiveness of exception-based verdict prediction.
49	Finally, our analysis is limited to verdict prediction; whether exception dominance extends to other classification tasks or generation tasks is an open question.
50	
51	\section*{Ethics Statement}
52	
53	This work uses publicly available benchmarks (HumanEval, MBPP-sanitized, DebugBench) and does not involve human subjects, crowdsourced annotations, or personally identifiable information.
54	All models evaluated are open-source and publicly accessible.
55	Training uses parameter-efficient LoRA fine-tuning on two RTX PRO 6000 Blackwell GPUs, with each experiment using a single GPU and total compute under 20 GPU-hours across all experiments, resulting in minimal environmental impact.
56	We do not foresee direct negative societal impacts from this work; verdict prediction is a developer-facing tool for automated testing.
57	
58	\bibliography{references}
59	
60	\appendix
61	\input{appendix}
62	
63	\end{document}
64	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "feab2720-657b-436b-abed-df44ef10c6bb",
  "isSidechain": false,
  "promptId": "b73967ab-1e3d-4502-97ef-ede23a2a2cd7",
  "type": "user",
  "uuid": "639f8a5f-713e-4f13-b3d0-0a2182241156",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/main.tex",
      "content": "\\documentclass[11pt,a4paper]{article}\n\\usepackage[review]{acl}\n% \\usepackage{acl}  % uncomment for camera-ready (remove [review])\n\\usepackage{times,latexsym}\n\\usepackage{amsmath,amssymb}\n\\usepackage{graphicx}\n\\graphicspath{{../../figures/paper/}}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{xcolor}\n\n\\title{Exception Events Are All You Need: \\\\Component Ablation for Trace-Based Verdict Prediction}\n\\author{Anonymous ACL submission}\n\n\\begin{document}\n\\maketitle\n\n\\begin{abstract}\nExecution traces are increasingly used to enhance code language models, but which trace components matter for downstream tasks remains poorly understood.\nWe present the first systematic component ablation of trace representations for verdict prediction (classifying whether a test passes or fails) across four models spanning three architecture families and 1.5B to 13B parameters.\nException events alone achieve ${\\geq}$99.33\\% accuracy across all four models (${\\geq}$99.83\\% on three of four; one seed reaches 100\\%), while a code-only baseline shows 9.19pp scale sensitivity (67.3--76.5\\%).\nAdding more trace information actively hurts: a multi-component representation underperforms exception-only, and the full-trace gap approximately decomposes into information overload (${\\sim}$74\\%) and gradient dilution (${\\sim}$26\\%).\nTail-truncation experiments reveal that diagnostic signal concentrates near the trace terminus (in a localized window, not the absolute end), recovering 86\\% of the gap to exception-only.\nA format-marker ablation confirms ${\\sim}$91\\% of the exception signal is semantic (learned by SFT to distinguish caught from uncaught exceptions) rather than format-driven.\nThese results reveal a two-tier diagnostic hierarchy: Tier~1 signals (exception events, assertion points) individually achieve ${\\geq}$99\\%, while Tier~2 (loop compression) reaches 85.6\\%.\nCross-dataset evaluation on DebugBench ($N{=}426$) confirms generalization, with exception-only achieving 100\\%.\nWe reframe verdict prediction as fault detection: the minimal sufficient signal is a compact exception event (median 150 tokens) that is scale-invariant, architecture-independent, and deployable in token-constrained settings.\n\\end{abstract}\n\n\\input{introduction}\n\\input{method}\n\\input{experiments}\n\\input{discussion}\n\\input{related_work}\n\\input{conclusion}\n\n\\section*{Limitations}\n\nOur study has several limitations.\nFirst, our primary experiments use a single dataset (591 problems from HumanEval and MBPP-sanitized); while a cross-dataset evaluation on DebugBench (\\S\\ref{sec:debugbench}) confirms that exception dominance generalizes to synthetically injected bugs, generalization to other languages, larger codebases, or real-world fault distributions remains untested.\nSecond, while we evaluate four models spanning 1.5B to 13B parameters across three architecture families, all are code-specialized; generalization to general-purpose models or larger scales remains untested.\nThird, DeepSeek \\texttt{exception\\_only} exhibits seed-dependent variance: 2/3 seeds achieve 99.33\\% while seed 123 yields 91.09\\% ($\\sigma{=}4.76$pp, $n{=}3$), which we hypothesize reflects LoRA initialization sensitivity in DeepSeek-Coder, though direct evidence is lacking (fail recall = 70.5\\% for the outlier vs.\\ 100\\% for others).\nQwen \\texttt{exception\\_only} shows perfect seed robustness ($\\sigma{=}0$, $n{=}3$), but Qwen \\texttt{ae\\_only} also exhibits seed variance ($\\sigma{=}$0.40pp; seed 123 = 99.08\\% vs.\\ seeds 42/456 = 99.92\\%), though far smaller than DeepSeek's ($\\sigma{=}$4.76pp).\nWhether training stabilization techniques can eliminate DeepSeek's seed sensitivity is unexplored; other conditions use a single seed.\nFourth, the initial DeepSeek \\texttt{full\\_trace} run was invalidated by context overflow; a re-run with extended context yields 79.16\\% (CI [76.80\\%, 81.30\\%]), 2.60pp below Qwen (Table~\\ref{tab:cross_model}).\nFifth, the candidate solutions were generated by Qwen-2.5-Coder-7B-Instruct, which also serves as one of our evaluation models; this does not affect verdict prediction but may influence the pass/fail distribution.\nSixth, self-familiarity bias may inflate absolute accuracy: both Qwen-2.5-Coder and DeepSeek-Coder were likely exposed to HumanEval and MBPP solutions during pretraining, so the models may partially recognize solutions rather than purely reasoning from trace signals; our cross-dataset evaluation on DebugBench mitigates but does not eliminate this concern.\nSeventh, the error distribution in our test set may not reflect real-world fault distributions: exceptions (especially \\texttt{TypeError}, \\texttt{ValueError}) dominate LLM-generated failures, but production code may exhibit a broader spectrum of silent logic errors where no exception is raised, potentially reducing the effectiveness of exception-based verdict prediction.\nFinally, our analysis is limited to verdict prediction; whether exception dominance extends to other classification tasks or generation tasks is an open question.\n\n\\section*{Ethics Statement}\n\nThis work uses publicly available benchmarks (HumanEval, MBPP-sanitized, DebugBench) and does not involve human subjects, crowdsourced annotations, or personally identifiable information.\nAll models evaluated are open-source and publicly accessible.\nTraining uses parameter-efficient LoRA fine-tuning on two RTX PRO 6000 Blackwell GPUs, with each experiment using a single GPU and total compute under 20 GPU-hours across all experiments, resulting in minimal environmental impact.\nWe do not foresee direct negative societal impacts from this work; verdict prediction is a developer-facing tool for automated testing.\n\n\\bibliography{references}\n\n\\appendix\n\\input{appendix}\n\n\\end{document}\n",
      "numLines": 64,
      "startLine": 1,
      "totalLines": 64
    }
  },
  "sourceToolAssistantUUID": "feab2720-657b-436b-abed-df44ef10c6bb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/.claude/sessions/review_reviewer_1_7624f219",
  "sessionId": "f76386b4-9d1f-4f92-b831-706bc4acd94d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Tool call

_source line 16 · 2026-05-17T18:01:59.495Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Xj71KzEtwfLT46WAxJ98ER`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "639f8a5f-713e-4f13-b3d0-0a2182241156",
  "isSidechain": false,
  "requestId": "req_011Cb8aZnVhhhvUsy3JCV6wc",
  "type": "assistant",
  "uuid": "912ea10c-19d8-4183-8164-9e4f19832389",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/.claude/sessions/review_reviewer_1_7624f219",
  "sessionId": "f76386b4-9d1f-4f92-b831-706bc4acd94d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015HcLXzF3feTTdP4sPwbUoc",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2318,
      "cache_read_input_tokens": 27460,
      "output_tokens": 375,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2318,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 375,
          "cache_read_input_tokens": 27460,
          "cache_creation_input_tokens": 2318,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2318
          },
          "type": "message"
        }
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

_source line 17 · 2026-05-17T18:02:00.270Z_

<details><summary>↩ Tool result · `toolu_01TCRscjZbJe5ZctbBzSuF38`</summary>

```text
1	\section{Experiments}
2	
3	We evaluate across two research questions:
4	(1)~Do Tier~1 exception signals generalize across models?
5	(2)~What is the relative contribution of each trace component?
6	All experiments use $N{=}1{,}190$ test samples; accuracy is reported with Wilson 95\% CIs.
7	Pairwise comparisons use paired bootstrap resampling ($B{=}10{,}000$, seed=42); all differences are significant at $p{<}0.0001$ unless noted.
8	
9	\subsection{Cross-Model Comparison}
10	\label{sec:cross_model}
11	
12	Table~\ref{tab:cross_model} compares four models spanning an 8.7$\times$ parameter range (1.5B--13B) and three architecture families (Qwen, DeepSeek, CodeLlama) under key conditions.
13	
14	\begin{table}[t]
15	\centering
16	\caption{Cross-model verdict accuracy (\%, $N{=}1{,}190$). Bold: best accuracy per model. Multi-seed entries show mean$\pm$std (3 seeds). $^\dag$2/3 seeds; one seed excluded due to LoRA initialization failure (91.09\%, fail recall = 70.5\%; see Appendix~\ref{sec:training_dynamics}). \texttt{ae\_only} and \texttt{loop\_only} ablations tested on Qwen-7B (3 seeds) to isolate component contributions; cross-model validation focused on the primary conditions. Full CIs in Appendix~\ref{sec:full_results}.}
17	\label{tab:cross_model}
18	\small
19	\resizebox{\columnwidth}{!}{%
20	\begin{tabular}{lcccc}
21	\toprule
22	\textbf{Condition} & \textbf{Qwen-7B} & \textbf{Qwen-1.5B} & \textbf{CL-13B} & \textbf{DS-6.7B} \\
23	\midrule
24	exception\_only & \textbf{99.83}{\scriptsize$\pm$0.00} & \textbf{99.83} & \textbf{99.89}{\scriptsize$\pm$0.10} & \textbf{99.33}$^\dag$ \\
25	ae\_only & 99.64{\scriptsize$\pm$0.49} & --- & --- & --- \\
26	VOTA & 99.41 & 99.58 & 98.57 & 84.45 \\
27	no\_trace & 75.13 & 67.31 & 76.50 & 73.36 \\
28	\midrule
29	Majority baseline & \multicolumn{4}{c}{71.51} \\
30	\bottomrule
31	\end{tabular}%
32	}
33	\end{table}
34	
35	\paragraph{Exception dominance across families.}
36	Under \texttt{exception\_only}, the Qwen and CodeLlama families achieve ${\geq}$99.83\% (mean): Qwen-7B (99.83\%$\pm$0.00, 3 seeds), Qwen-1.5B (99.83\%), and CodeLlama-13B (99.89\%$\pm$0.10, 3 seeds; seed 123 achieves 100\%).
37	DeepSeek-6.7B reaches 99.33\% on 2/3 seeds with one LoRA-sensitivity outlier at 91.09\% (seed 123; fail recall = 70.5\%); even the outlier outperforms VOTA (84.45\%) by 6.64pp.
38	Excluding the DeepSeek outlier, the cross-model range is 0.56pp (99.33--99.89\%), the tightest of any condition.
39	
40	\paragraph{Scale invariance of exception signals.}
41	Exception-based accuracy is shared by models spanning 1.5B to 13B parameters (8.7$\times$): both Qwen-1.5B and CodeLlama-13B achieve 99.83\%+ on the same representation.
42	CodeLlama-13B seed 123 achieves 100\% (0/1190 errors), confirming that Qwen's two persistent errors (from \texttt{GeneratorExit}; Appendix~\ref{sec:irreducible}) are high-probability convergence artifacts rather than hard data limitations.
43	In contrast, \texttt{no\_trace} scales monotonically with capacity: 67.31\% (1.5B) $\to$ 75.13\% (7B) $\to$ 76.50\% (13B), a 9.19pp range that exception events completely eliminate (Figure~\ref{fig:cross_scale}).
44	
45	\begin{figure}[t]
46	\centering
47	\includegraphics[width=\columnwidth]{fig3_cross_model_gap}
48	\caption{Verdict accuracy vs.\ model scale. \texttt{exception\_only} maintains ${\geq}$99.33\% regardless of scale (1.5B--13B), while \texttt{no\_trace} shows monotonic scale sensitivity (+9.19pp from 1.5B to 13B). The \texttt{nomarker} condition (format markers removed) shows no degradation at smaller scale (${\sim}$97.7--97.8\%).}
49	\label{fig:cross_scale}
50	\end{figure}
51	
52	\paragraph{VOTA cross-family variation.}
53	VOTA accuracy varies across families: 99.58\% (Qwen-1.5B) $>$ 99.41\% (Qwen-7B) $>$ 98.57\% (CodeLlama-13B; \texttt{codellama13b\_vota\_seed42}, CI [97.9, 99.2]) $\gg$ 84.45\% (DeepSeek-6.7B).
54	The CodeLlama result (17 errors) narrows the gap: among models without tokenizer-driven truncation, the VOTA range is only 1.01pp (98.57--99.58\%), suggesting that the 14.96pp DeepSeek deficit is primarily a truncation artifact rather than an inherent model capability limitation (91.7\% of DeepSeek training samples were affected; Appendix~\ref{sec:tokenizer_analysis}).
55	In contrast, \texttt{exception\_only} inputs are compact (median 150 tokens, mean 398 due to verbose fail-class exceptions), making the cross-model comparison clean.
56	
57	\subsection{Component Ablation}
58	\label{sec:ablation}
59	
60	We restrict \texttt{ae\_only} and \texttt{loop\_only} ablations to Qwen-7B, as these component-level analyses target the trace composition mechanism rather than cross-model generalization.
61	Table~\ref{tab:ablation} decomposes VOTA on Qwen-2.5-7B (seed=42) and reveals a two-tier hierarchy.
62	
63	\begin{table}[t]
64	\centering
65	\caption{Component ablation on Qwen-2.5-7B ($N{=}1{,}190$). Tier~1 signals achieve near-perfect accuracy; combining them (VOTA) slightly dilutes performance. $^\dag$\texttt{ae\_only}: 3-seed mean 99.64\% ($\pm$0.49; seeds 42: 99.92, 123: 99.08, 456: 99.92). \texttt{exception\_only}: 99.83\% ($\pm$0.00, 3 seeds), more stable ($\sigma{=}$0 vs.\ $\sigma{=}$0.49).}
66	\label{tab:ablation}
67	\small
68	\resizebox{\columnwidth}{!}{%
69	\begin{tabular}{llccc}
70	\toprule
71	\textbf{Condition} & \textbf{Components} & \textbf{Acc (\%)} & \textbf{95\% CI} & \textbf{Tier} \\
72	\midrule
73	ae\_only & assertion-point & 99.64$^\dag$ & [99.26, 99.87] & 1 \\
74	exception\_only & exception events & \textbf{99.83} & [99.58, 100.00] & 1 \\
75	VOTA & exc+ae+loop & 99.41 & [98.82, 99.83] & --- \\
76	VOTA\_no\_ae & exc+loop & 99.41 & [98.90, 99.80] & --- \\
77	loop\_only & loop compression & 85.63 & [83.53, 87.56] & 2 \\
78	full\_trace & complete trace & 81.76 & [79.70, 83.90] & --- \\
79	no\_trace & none & 75.13 & [72.77, 77.48] & --- \\
80	\midrule
81	Regex (best) & exc.\ type regex & 93.61 & --- & --- \\
82	3-shot (Qwen-7B) & in-context learning & 90.84 & --- & --- \\
83	Zero-shot (4 models) & prompting & 51.0--93.5 & --- & --- \\
84	\bottomrule
85	\end{tabular}%
86	}
87	\end{table}
88	
89	Tier~1 signals are individually sufficient: \texttt{ae\_only} (3-seed mean 99.64\% $\pm$ 0.49) and \texttt{exception\_only} (99.83\% $\pm$ 0.00) both exceed VOTA ($p{=}0.01$), implying that combining signals introduces noise; \texttt{exception\_only} is more stable across seeds ($\sigma{=}$0 vs.\ $\sigma{=}$0.49).
90	Removing assertion points has no effect (\texttt{VOTA\_no\_ae} = 99.41\%), confirming exception dominance.
91	Tier~2 \texttt{loop\_only} (85.63\%) improves 10.50pp over \texttt{no\_trace} ($p{<}0.0001$) but falls far short of Tier~1.
92	\paragraph{Rule-based baseline comparison.}
93	The strongest non-trivial regex heuristic (B4: exception class name matching) achieves 93.61\% accuracy (F1=0.876), trailing SFT \texttt{exception\_only} (99.83\%, F1=0.997) by 6.22pp (McNemar $p{<}0.001$).
94	The gap concentrates on caught-exception boundary cases: regex flags all exception events as failures, while SFT learns to distinguish caught exceptions (benign, inside \texttt{try/except}) from uncaught faults, correctly resolving 6/8 boundary samples (Appendix~\ref{sec:regex_baselines}).
95	Across trace formats, SFT consistently outperforms the best applicable regex, from +3.62pp (\texttt{no\_trace} over majority baseline) to +23.86pp (VOTA), with the largest gains on formats requiring semantic interpretation (Appendix~\ref{sec:regex_baselines}).
96	
97	\paragraph{Zero-shot and few-shot LLM baselines.}
98	Zero-shot prompting spans 51.0--93.5\% across four models (CodeLlama-13B: 51.01\%, Qwen-7B: 89.08\%, DeepSeek-6.7B: 90.59\%, Qwen-1.5B: 93.45\%), a 42.44pp range that SFT compresses to 0.56pp (99.33--99.89\%).
99	Zero-shot performance does not correlate with model size: Qwen-1.5B (93.45\%) outperforms both Qwen-7B (89.08\%) and CodeLlama-13B (51.01\%), indicating that pretraining data distribution, not capacity, determines zero-shot verdict ability.
100	CodeLlama-13B drops below the majority baseline (71.51\%), showing extreme fail bias (72.4\% of predictions are \texttt{fail}).
101	Three-shot in-context learning on Qwen-7B (90.84\%, fail recall = 80.53\%) improves only 1.76pp over zero-shot and still trails both the regex heuristic (93.61\%) and SFT by 8.99pp, confirming that a few examples cannot substitute for task-specific fine-tuning.
102	SFT normalizes this cross-architecture variance, closing a 6--49pp gap to ${\geq}$99.33\% across all models with 4,720 training samples (Appendix~\ref{sec:zeroshot_cross_model}).
103	
104	\subsection{Format Marker Ablation}
105	\label{sec:nomarker}
106	
107	The \texttt{exception\_only} format includes a \texttt{[No exception data in trace]} marker in all pass-class samples (regex baseline B5 exploits this for 99.33\% accuracy; Appendix~\ref{sec:regex_baselines}).
108	To quantify the marker's contribution, we retrain with all format markers removed (\texttt{nomarker} condition).
109	
110	Qwen-7B 3-seed mean: 97.65\% $\pm$ 0.96 (seeds 42/123/456: 96.55/98.32/98.07\%), a drop of 2.18pp from \texttt{exception\_only} (99.83\%).
111	Qwen-1.5B: 97.82\%, drop of 2.01pp.
112	The marker contribution (${\sim}$2pp) accounts for only ${\sim}$9\% of the total exception lift over \texttt{no\_trace} (24.70pp on 7B).
113	Exception events thus provide two signal layers that show no degradation at smaller scale: structural markers (${\sim}$2pp, regex-learnable) and semantic exception content (${\sim}$22pp, requiring SFT to distinguish caught from uncaught exceptions).
114	
115	\subsection{Information Density Decomposition}
116	\label{sec:density}
117	
118	The 17.65pp gap between \texttt{full\_trace} (81.76\%) and VOTA (99.41\%) decomposes via \texttt{full\_trace\_label\_only}, which retains the full trace but masks all trace tokens from the loss.
119	
120	\begin{table}[t]
121	\centering
122	\caption{Approximate information density decomposition: gradient dilution (${\sim}$26\%) vs.\ information overload (${\sim}$74\%).}
123	\label{tab:density}
124	\small
125	\begin{tabular}{lccc}
126	\toprule
127	\textbf{Condition} & \textbf{Acc (\%)} & \textbf{$\Delta$ vs.\ full\_trace} & \textbf{Gap explained} \\
128	\midrule
129	full\_trace & 81.76 & --- & --- \\
130	label\_only & 86.22 & +4.46pp & 26\% \\
131	VOTA & 99.41 & +17.65pp & 100\% \\
132	\bottomrule
133	\end{tabular}
134	\end{table}
135	
136	Gradient dilution accounts for approximately 26\% of the gap (+4.46pp, $p{<}0.0001$, bootstrap 95\% CI $[{+}2.35, {+}6.55]$): when the model no longer wastes gradient updates on predicting trace tokens, accuracy improves even with identical input.
137	The remaining ${\sim}$74\% (+13.19pp) reflects information overload at inference: the model receives thousands of irrelevant trace lines that compete for attention with the diagnostic signal, regardless of loss design.
138	This asymmetry implies that trace compression methods should prioritize \emph{content selection} (removing irrelevant lines) over \emph{loss engineering} (masking non-target tokens), as the larger bottleneck is what the model sees, not how it is trained.
139	The two factors may interact, so this decomposition is approximate.
140	
141	\subsection{Additional Analyses}
142	\label{sec:additional}
143	
144	\paragraph{Trace length ablation.}
145	\label{sec:trace_length}
146	Varying the trace token budget (256--no limit) on Qwen yields accuracy in a narrow 77.2\%--81.8\% band with a non-monotonic pattern, confirming that trace content quality, not quantity, is the bottleneck (Appendix~\ref{sec:trace_length_full}).
147	Notably, 1024-token traces (77.23\%) underperform 512-token traces (80.42\%), revealing that mid-length traces are long enough to introduce execution noise yet too short to reach the diagnostic events concentrated at trace end.
148	This further supports our claim that signal density, not quantity, determines model performance.
149	
150	\paragraph{Truncation direction.}
151	Reversing the truncation direction confirms that diagnostic signal concentrates near the trace terminus: on Qwen-7B, \texttt{tail\_2048} (97.31\%) outperforms \texttt{head\_2048} (81.76\%) by 15.55pp, and \texttt{tail\_256} (77.48\%) drops to the \texttt{no\_trace} baseline, localizing the signal window to 256--512 tokens from the trace end.
152	Cross-model verification confirms the pattern across two architecture families and two scales: Qwen-1.5B \texttt{tail\_2048} = 97.90\% (CI [97.06, 98.74]), DeepSeek-6.7B = 94.96\% (CI [93.70, 96.22]), with residual gaps to \texttt{exception\_only} of only 1.93pp and 4.37pp respectively (Appendix~\ref{sec:trace_length_full}).
153	The positional concentration hypothesis holds across all tested configurations, with \texttt{tail\_2048} capturing 95--98\% of \texttt{exception\_only}'s accuracy.
154	The residual gap confirms that semantic extraction (identifying exception type and message by content) still outperforms positional extraction (retaining a fixed window that includes non-diagnostic lines).
155	
156	\paragraph{Calibration.}
157	\label{sec:calibration}
158	Calibration mirrors the tier hierarchy: \texttt{exception\_only} ECE = 0.0027 vs.\ \texttt{no\_trace} ECE = 0.171, a 63$\times$ gap (Appendix~\ref{sec:calibration_full}).
159	
160	\paragraph{Error orthogonality.}
161	\texttt{exception\_only}'s 2 errors have zero overlap with all other conditions' error sets (Jaccard = 0.000), confirming it operates on an independent signal dimension (Appendix~\ref{sec:error_overlap}).
162	
163	\paragraph{Exception type breakdown.}
164	A per-exception-type breakdown (Appendix~\ref{sec:exception_type}) confirms that all standard exception types achieve 100\% accuracy; the only failures arise from \texttt{GeneratorExit}, a benign \texttt{BaseException} subclass.
165	
166	\paragraph{Cross-dataset generalization.}
167	\label{sec:debugbench}
168	On DebugBench \citep{tian2024debugbench} ($N{=}426$), the ranking is preserved: \texttt{exception\_only} 100\%, VOTA 99.77\%, \texttt{no\_trace} 96.71\%; narrow margins reflect a ceiling effect from structurally distinctive mutations (Appendix~\ref{sec:debugbench_full}).
169	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "02540e97-fdb7-413c-bb11-d03f19a85718",
  "isSidechain": false,
  "promptId": "b73967ab-1e3d-4502-97ef-ede23a2a2cd7",
  "type": "user",
  "uuid": "6819346e-c893-45ce-ab28-d9f88a40bc34",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/experiments.tex",
      "content": "\\section{Experiments}\n\nWe evaluate across two research questions:\n(1)~Do Tier~1 exception signals generalize across models?\n(2)~What is the relative contribution of each trace component?\nAll experiments use $N{=}1{,}190$ test samples; accuracy is reported with Wilson 95\\% CIs.\nPairwise comparisons use paired bootstrap resampling ($B{=}10{,}000$, seed=42); all differences are significant at $p{<}0.0001$ unless noted.\n\n\\subsection{Cross-Model Comparison}\n\\label{sec:cross_model}\n\nTable~\\ref{tab:cross_model} compares four models spanning an 8.7$\\times$ parameter range (1.5B--13B) and three architecture families (Qwen, DeepSeek, CodeLlama) under key conditions.\n\n\\begin{table}[t]\n\\centering\n\\caption{Cross-model verdict accuracy (\\%, $N{=}1{,}190$). Bold: best accuracy per model. Multi-seed entries show mean$\\pm$std (3 seeds). $^\\dag$2/3 seeds; one seed excluded due to LoRA initialization failure (91.09\\%, fail recall = 70.5\\%; see Appendix~\\ref{sec:training_dynamics}). \\texttt{ae\\_only} and \\texttt{loop\\_only} ablations tested on Qwen-7B (3 seeds) to isolate component contributions; cross-model validation focused on the primary conditions. Full CIs in Appendix~\\ref{sec:full_results}.}\n\\label{tab:cross_model}\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Condition} & \\textbf{Qwen-7B} & \\textbf{Qwen-1.5B} & \\textbf{CL-13B} & \\textbf{DS-6.7B} \\\\\n\\midrule\nexception\\_only & \\textbf{99.83}{\\scriptsize$\\pm$0.00} & \\textbf{99.83} & \\textbf{99.89}{\\scriptsize$\\pm$0.10} & \\textbf{99.33}$^\\dag$ \\\\\nae\\_only & 99.64{\\scriptsize$\\pm$0.49} & --- & --- & --- \\\\\nVOTA & 99.41 & 99.58 & 98.57 & 84.45 \\\\\nno\\_trace & 75.13 & 67.31 & 76.50 & 73.36 \\\\\n\\midrule\nMajority baseline & \\multicolumn{4}{c}{71.51} \\\\\n\\bottomrule\n\\end{tabular}%\n}\n\\end{table}\n\n\\paragraph{Exception dominance across families.}\nUnder \\texttt{exception\\_only}, the Qwen and CodeLlama families achieve ${\\geq}$99.83\\% (mean): Qwen-7B (99.83\\%$\\pm$0.00, 3 seeds), Qwen-1.5B (99.83\\%), and CodeLlama-13B (99.89\\%$\\pm$0.10, 3 seeds; seed 123 achieves 100\\%).\nDeepSeek-6.7B reaches 99.33\\% on 2/3 seeds with one LoRA-sensitivity outlier at 91.09\\% (seed 123; fail recall = 70.5\\%); even the outlier outperforms VOTA (84.45\\%) by 6.64pp.\nExcluding the DeepSeek outlier, the cross-model range is 0.56pp (99.33--99.89\\%), the tightest of any condition.\n\n\\paragraph{Scale invariance of exception signals.}\nException-based accuracy is shared by models spanning 1.5B to 13B parameters (8.7$\\times$): both Qwen-1.5B and CodeLlama-13B achieve 99.83\\%+ on the same representation.\nCodeLlama-13B seed 123 achieves 100\\% (0/1190 errors), confirming that Qwen's two persistent errors (from \\texttt{GeneratorExit}; Appendix~\\ref{sec:irreducible}) are high-probability convergence artifacts rather than hard data limitations.\nIn contrast, \\texttt{no\\_trace} scales monotonically with capacity: 67.31\\% (1.5B) $\\to$ 75.13\\% (7B) $\\to$ 76.50\\% (13B), a 9.19pp range that exception events completely eliminate (Figure~\\ref{fig:cross_scale}).\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{fig3_cross_model_gap}\n\\caption{Verdict accuracy vs.\\ model scale. \\texttt{exception\\_only} maintains ${\\geq}$99.33\\% regardless of scale (1.5B--13B), while \\texttt{no\\_trace} shows monotonic scale sensitivity (+9.19pp from 1.5B to 13B). The \\texttt{nomarker} condition (format markers removed) shows no degradation at smaller scale (${\\sim}$97.7--97.8\\%).}\n\\label{fig:cross_scale}\n\\end{figure}\n\n\\paragraph{VOTA cross-family variation.}\nVOTA accuracy varies across families: 99.58\\% (Qwen-1.5B) $>$ 99.41\\% (Qwen-7B) $>$ 98.57\\% (CodeLlama-13B; \\texttt{codellama13b\\_vota\\_seed42}, CI [97.9, 99.2]) $\\gg$ 84.45\\% (DeepSeek-6.7B).\nThe CodeLlama result (17 errors) narrows the gap: among models without tokenizer-driven truncation, the VOTA range is only 1.01pp (98.57--99.58\\%), suggesting that the 14.96pp DeepSeek deficit is primarily a truncation artifact rather than an inherent model capability limitation (91.7\\% of DeepSeek training samples were affected; Appendix~\\ref{sec:tokenizer_analysis}).\nIn contrast, \\texttt{exception\\_only} inputs are compact (median 150 tokens, mean 398 due to verbose fail-class exceptions), making the cross-model comparison clean.\n\n\\subsection{Component Ablation}\n\\label{sec:ablation}\n\nWe restrict \\texttt{ae\\_only} and \\texttt{loop\\_only} ablations to Qwen-7B, as these component-level analyses target the trace composition mechanism rather than cross-model generalization.\nTable~\\ref{tab:ablation} decomposes VOTA on Qwen-2.5-7B (seed=42) and reveals a two-tier hierarchy.\n\n\\begin{table}[t]\n\\centering\n\\caption{Component ablation on Qwen-2.5-7B ($N{=}1{,}190$). Tier~1 signals achieve near-perfect accuracy; combining them (VOTA) slightly dilutes performance. $^\\dag$\\texttt{ae\\_only}: 3-seed mean 99.64\\% ($\\pm$0.49; seeds 42: 99.92, 123: 99.08, 456: 99.92). \\texttt{exception\\_only}: 99.83\\% ($\\pm$0.00, 3 seeds), more stable ($\\sigma{=}$0 vs.\\ $\\sigma{=}$0.49).}\n\\label{tab:ablation}\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llccc}\n\\toprule\n\\textbf{Condition} & \\textbf{Components} & \\textbf{Acc (\\%)} & \\textbf{95\\% CI} & \\textbf{Tier} \\\\\n\\midrule\nae\\_only & assertion-point & 99.64$^\\dag$ & [99.26, 99.87] & 1 \\\\\nexception\\_only & exception events & \\textbf{99.83} & [99.58, 100.00] & 1 \\\\\nVOTA & exc+ae+loop & 99.41 & [98.82, 99.83] & --- \\\\\nVOTA\\_no\\_ae & exc+loop & 99.41 & [98.90, 99.80] & --- \\\\\nloop\\_only & loop compression & 85.63 & [83.53, 87.56] & 2 \\\\\nfull\\_trace & complete trace & 81.76 & [79.70, 83.90] & --- \\\\\nno\\_trace & none & 75.13 & [72.77, 77.48] & --- \\\\\n\\midrule\nRegex (best) & exc.\\ type regex & 93.61 & --- & --- \\\\\n3-shot (Qwen-7B) & in-context learning & 90.84 & --- & --- \\\\\nZero-shot (4 models) & prompting & 51.0--93.5 & --- & --- \\\\\n\\bottomrule\n\\end{tabular}%\n}\n\\end{table}\n\nTier~1 signals are individually sufficient: \\texttt{ae\\_only} (3-seed mean 99.64\\% $\\pm$ 0.49) and \\texttt{exception\\_only} (99.83\\% $\\pm$ 0.00) both exceed VOTA ($p{=}0.01$), implying that combining signals introduces noise; \\texttt{exception\\_only} is more stable across seeds ($\\sigma{=}$0 vs.\\ $\\sigma{=}$0.49).\nRemoving assertion points has no effect (\\texttt{VOTA\\_no\\_ae} = 99.41\\%), confirming exception dominance.\nTier~2 \\texttt{loop\\_only} (85.63\\%) improves 10.50pp over \\texttt{no\\_trace} ($p{<}0.0001$) but falls far short of Tier~1.\n\\paragraph{Rule-based baseline comparison.}\nThe strongest non-trivial regex heuristic (B4: exception class name matching) achieves 93.61\\% accuracy (F1=0.876), trailing SFT \\texttt{exception\\_only} (99.83\\%, F1=0.997) by 6.22pp (McNemar $p{<}0.001$).\nThe gap concentrates on caught-exception boundary cases: regex flags all exception events as failures, while SFT learns to distinguish caught exceptions (benign, inside \\texttt{try/except}) from uncaught faults, correctly resolving 6/8 boundary samples (Appendix~\\ref{sec:regex_baselines}).\nAcross trace formats, SFT consistently outperforms the best applicable regex, from +3.62pp (\\texttt{no\\_trace} over majority baseline) to +23.86pp (VOTA), with the largest gains on formats requiring semantic interpretation (Appendix~\\ref{sec:regex_baselines}).\n\n\\paragraph{Zero-shot and few-shot LLM baselines.}\nZero-shot prompting spans 51.0--93.5\\% across four models (CodeLlama-13B: 51.01\\%, Qwen-7B: 89.08\\%, DeepSeek-6.7B: 90.59\\%, Qwen-1.5B: 93.45\\%), a 42.44pp range that SFT compresses to 0.56pp (99.33--99.89\\%).\nZero-shot performance does not correlate with model size: Qwen-1.5B (93.45\\%) outperforms both Qwen-7B (89.08\\%) and CodeLlama-13B (51.01\\%), indicating that pretraining data distribution, not capacity, determines zero-shot verdict ability.\nCodeLlama-13B drops below the majority baseline (71.51\\%), showing extreme fail bias (72.4\\% of predictions are \\texttt{fail}).\nThree-shot in-context learning on Qwen-7B (90.84\\%, fail recall = 80.53\\%) improves only 1.76pp over zero-shot and still trails both the regex heuristic (93.61\\%) and SFT by 8.99pp, confirming that a few examples cannot substitute for task-specific fine-tuning.\nSFT normalizes this cross-architecture variance, closing a 6--49pp gap to ${\\geq}$99.33\\% across all models with 4,720 training samples (Appendix~\\ref{sec:zeroshot_cross_model}).\n\n\\subsection{Format Marker Ablation}\n\\label{sec:nomarker}\n\nThe \\texttt{exception\\_only} format includes a \\texttt{[No exception data in trace]} marker in all pass-class samples (regex baseline B5 exploits this for 99.33\\% accuracy; Appendix~\\ref{sec:regex_baselines}).\nTo quantify the marker's contribution, we retrain with all format markers removed (\\texttt{nomarker} condition).\n\nQwen-7B 3-seed mean: 97.65\\% $\\pm$ 0.96 (seeds 42/123/456: 96.55/98.32/98.07\\%), a drop of 2.18pp from \\texttt{exception\\_only} (99.83\\%).\nQwen-1.5B: 97.82\\%, drop of 2.01pp.\nThe marker contribution (${\\sim}$2pp) accounts for only ${\\sim}$9\\% of the total exception lift over \\texttt{no\\_trace} (24.70pp on 7B).\nException events thus provide two signal layers that show no degradation at smaller scale: structural markers (${\\sim}$2pp, regex-learnable) and semantic exception content (${\\sim}$22pp, requiring SFT to distinguish caught from uncaught exceptions).\n\n\\subsection{Information Density Decomposition}\n\\label{sec:density}\n\nThe 17.65pp gap between \\texttt{full\\_trace} (81.76\\%) and VOTA (99.41\\%) decomposes via \\texttt{full\\_trace\\_label\\_only}, which retains the full trace but masks all trace tokens from the loss.\n\n\\begin{table}[t]\n\\centering\n\\caption{Approximate information density decomposition: gradient dilution (${\\sim}$26\\%) vs.\\ information overload (${\\sim}$74\\%).}\n\\label{tab:density}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Condition} & \\textbf{Acc (\\%)} & \\textbf{$\\Delta$ vs.\\ full\\_trace} & \\textbf{Gap explained} \\\\\n\\midrule\nfull\\_trace & 81.76 & --- & --- \\\\\nlabel\\_only & 86.22 & +4.46pp & 26\\% \\\\\nVOTA & 99.41 & +17.65pp & 100\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nGradient dilution accounts for approximately 26\\% of the gap (+4.46pp, $p{<}0.0001$, bootstrap 95\\% CI $[{+}2.35, {+}6.55]$): when the model no longer wastes gradient updates on predicting trace tokens, accuracy improves even with identical input.\nThe remaining ${\\sim}$74\\% (+13.19pp) reflects information overload at inference: the model receives thousands of irrelevant trace lines that compete for attention with the diagnostic signal, regardless of loss design.\nThis asymmetry implies that trace compression methods should prioritize \\emph{content selection} (removing irrelevant lines) over \\emph{loss engineering} (masking non-target tokens), as the larger bottleneck is what the model sees, not how it is trained.\nThe two factors may interact, so this decomposition is approximate.\n\n\\subsection{Additional Analyses}\n\\label{sec:additional}\n\n\\paragraph{Trace length ablation.}\n\\label{sec:trace_length}\nVarying the trace token budget (256--no limit) on Qwen yields accuracy in a narrow 77.2\\%--81.8\\% band with a non-monotonic pattern, confirming that trace content quality, not quantity, is the bottleneck (Appendix~\\ref{sec:trace_length_full}).\nNotably, 1024-token traces (77.23\\%) underperform 512-token traces (80.42\\%), revealing that mid-length traces are long enough to introduce execution noise yet too short to reach the diagnostic events concentrated at trace end.\nThis further supports our claim that signal density, not quantity, determines model performance.\n\n\\paragraph{Truncation direction.}\nReversing the truncation direction confirms that diagnostic signal concentrates near the trace terminus: on Qwen-7B, \\texttt{tail\\_2048} (97.31\\%) outperforms \\texttt{head\\_2048} (81.76\\%) by 15.55pp, and \\texttt{tail\\_256} (77.48\\%) drops to the \\texttt{no\\_trace} baseline, localizing the signal window to 256--512 tokens from the trace end.\nCross-model verification confirms the pattern across two architecture families and two scales: Qwen-1.5B \\texttt{tail\\_2048} = 97.90\\% (CI [97.06, 98.74]), DeepSeek-6.7B = 94.96\\% (CI [93.70, 96.22]), with residual gaps to \\texttt{exception\\_only} of only 1.93pp and 4.37pp respectively (Appendix~\\ref{sec:trace_length_full}).\nThe positional concentration hypothesis holds across all tested configurations, with \\texttt{tail\\_2048} capturing 95--98\\% of \\texttt{exception\\_only}'s accuracy.\nThe residual gap confirms that semantic extraction (identifying exception type and message by content) still outperforms positional extraction (retaining a fixed window that includes non-diagnostic lines).\n\n\\paragraph{Calibration.}\n\\label{sec:calibration}\nCalibration mirrors the tier hierarchy: \\texttt{exception\\_only} ECE = 0.0027 vs.\\ \\texttt{no\\_trace} ECE = 0.171, a 63$\\times$ gap (Appendix~\\ref{sec:calibration_full}).\n\n\\paragraph{Error orthogonality.}\n\\texttt{exception\\_only}'s 2 errors have zero overlap with all other conditions' error sets (Jaccard = 0.000), confirming it operates on an independent signal dimension (Appendix~\\ref{sec:error_overlap}).\n\n\\paragraph{Exception type breakdown.}\nA per-exception-type breakdown (Appendix~\\ref{sec:exception_type}) confirms that all standard exception types achieve 100\\% accuracy; the only failures arise from \\texttt{GeneratorExit}, a benign \\texttt{BaseException} subclass.\n\n\\paragraph{Cross-dataset generalization.}\n\\label{sec:debugbench}\nOn DebugBench \\citep{tian2024debugbench} ($N{=}426$), the ranking is preserved: \\texttt{exception\\_only} 100\\%, VOTA 99.77\\%, \\texttt{no\\_trace} 96.71\\%; narrow margins reflect a ceiling effect from structurally distinctive mutations (Appendix~\\ref{sec:debugbench_full}).\n",
      "numLines": 169,
      "startLine": 1,
      "totalLines": 169
    }
  },
  "sourceToolAssistantUUID": "02540e97-fdb7-413c-bb11-d03f19a85718",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/.claude/sessions/review_reviewer_1_7624f219",
  "sessionId": "f76386b4-9d1f-4f92-b831-706bc4acd94d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Tool result

_source line 18 · 2026-05-17T18:01:59.505Z_

<details><summary>↩ Tool result · `toolu_01Xj71KzEtwfLT46WAxJ98ER`</summary>

```text
1	\section{Introduction}
2	
3	Execution traces (line-by-line records of a program's runtime behavior) have emerged as a promising input modality for code language models \citep{chen2025tracepile,ding2024traced,wang2025dcsh,ni2024next}.
4	Yet feeding thousands of trace lines to a model can be no better than feeding none: the diagnostic signal drowns in routine execution steps.
5	\emph{Which trace components actually carry the signal that matters?}
6	
7	Prior work found no single trace representation consistently outperforms others \citep{wang2025dcsh}, but focused on generation-oriented tasks.
8	\emph{Verdict prediction}, classifying whether a test passes or fails, is fundamentally different: it is fault detection, not generation.
9	The model need not simulate execution; it need only determine whether something went wrong.
10	This distinction suggests that a small, fault-specific trace component may suffice.
11	
12	We test this hypothesis through the first systematic component ablation of trace representations for verdict prediction.
13	Using 591 problems from HumanEval \citep{chen2021evaluating} and MBPP-sanitized \citep{austin2021program}, we decompose a multi-component trace representation (VOTA: exception events + assertion-point comparisons + loop compression) into individual components across four models spanning 1.5B to 13B parameters and three architecture families: Qwen-2.5-Coder-7B/1.5B-Instruct \citep{qwen2025coder}, CodeLlama-13B-Instruct \citep{roziere2024code}, and DeepSeek-Coder-6.7B-Instruct \citep{deepseek2024coder}.
14	
15	\textbf{Exception events alone achieve ${\geq}$99.33\% verdict accuracy across all four models (${\geq}$99.83\% on three of four; one seed reaches 100\%).}
16	This near-perfect accuracy holds from 1.5B to 13B parameters, while the code-only baseline (\texttt{no\_trace}) varies from 67.3\% to 76.5\% with strong scale dependence.
17	The exception signal eliminates the need for model capacity to compensate for missing information.
18	
19	More surprisingly, adding trace information beyond exceptions actively \emph{hurts}: VOTA (99.41\%) underperforms \texttt{exception\_only} (99.83\%), and the degradation reaches 14.96pp on DeepSeek, compounded by tokenizer-driven truncation.
20	We approximately decompose this gap: ${\sim}$74\% stems from information overload (irrelevant trace content at inference) and ${\sim}$26\% from gradient dilution (dispersed training signal).
21	Tail-truncation experiments confirm the mechanism across three models and two architecture families: retaining only the last 2,048 trace tokens captures 95--98\% of \texttt{exception\_only}'s accuracy, because diagnostic events concentrate at the trace terminus.
22	
23	Our contributions:
24	\begin{enumerate}
25	\item \textbf{Exception events are the minimal sufficient signal}: ${\geq}$99.33\% across four models and three families (1.5B--13B), with ${\sim}$91\% of the signal being semantic rather than format-driven (\S\ref{sec:cross_model}, \S\ref{sec:nomarker}). SFT closes a 6--49pp zero-shot gap across four models and three architecture families, and outperforms both few-shot prompting and the best regex heuristic (\S\ref{sec:ablation}). Cross-dataset evaluation on DebugBench ($N{=}426$) yields 100\% (\S\ref{sec:debugbench}).
26	\item \textbf{Richer traces actively hurt}: We approximately decompose why into gradient dilution (${\sim}$26\%) and information overload (${\sim}$74\%), with cross-model tail-truncation confirming positional concentration across three models (95--98\% of \texttt{exception\_only} recovered; \S\ref{sec:density}, \S\ref{sec:trace_length}).
27	\item \textbf{Two-tier diagnostic hierarchy}: Tier~1 signals (exceptions, assertions) individually achieve ${\geq}$99\%; Tier~2 (loop compression) reaches 85.6\%, still +10.5pp over no trace (\S\ref{sec:ablation}).
28	\end{enumerate}
29	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "912ea10c-19d8-4183-8164-9e4f19832389",
  "isSidechain": false,
  "promptId": "b73967ab-1e3d-4502-97ef-ede23a2a2cd7",
  "type": "user",
  "uuid": "91bd173e-b113-4b20-ad42-6e78d985011c",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/introduction.tex",
      "content": "\\section{Introduction}\n\nExecution traces (line-by-line records of a program's runtime behavior) have emerged as a promising input modality for code language models \\citep{chen2025tracepile,ding2024traced,wang2025dcsh,ni2024next}.\nYet feeding thousands of trace lines to a model can be no better than feeding none: the diagnostic signal drowns in routine execution steps.\n\\emph{Which trace components actually carry the signal that matters?}\n\nPrior work found no single trace representation consistently outperforms others \\citep{wang2025dcsh}, but focused on generation-oriented tasks.\n\\emph{Verdict prediction}, classifying whether a test passes or fails, is fundamentally different: it is fault detection, not generation.\nThe model need not simulate execution; it need only determine whether something went wrong.\nThis distinction suggests that a small, fault-specific trace component may suffice.\n\nWe test this hypothesis through the first systematic component ablation of trace representations for verdict prediction.\nUsing 591 problems from HumanEval \\citep{chen2021evaluating} and MBPP-sanitized \\citep{austin2021program}, we decompose a multi-component trace representation (VOTA: exception events + assertion-point comparisons + loop compression) into individual components across four models spanning 1.5B to 13B parameters and three architecture families: Qwen-2.5-Coder-7B/1.5B-Instruct \\citep{qwen2025coder}, CodeLlama-13B-Instruct \\citep{roziere2024code}, and DeepSeek-Coder-6.7B-Instruct \\citep{deepseek2024coder}.\n\n\\textbf{Exception events alone achieve ${\\geq}$99.33\\% verdict accuracy across all four models (${\\geq}$99.83\\% on three of four; one seed reaches 100\\%).}\nThis near-perfect accuracy holds from 1.5B to 13B parameters, while the code-only baseline (\\texttt{no\\_trace}) varies from 67.3\\% to 76.5\\% with strong scale dependence.\nThe exception signal eliminates the need for model capacity to compensate for missing information.\n\nMore surprisingly, adding trace information beyond exceptions actively \\emph{hurts}: VOTA (99.41\\%) underperforms \\texttt{exception\\_only} (99.83\\%), and the degradation reaches 14.96pp on DeepSeek, compounded by tokenizer-driven truncation.\nWe approximately decompose this gap: ${\\sim}$74\\% stems from information overload (irrelevant trace content at inference) and ${\\sim}$26\\% from gradient dilution (dispersed training signal).\nTail-truncation experiments confirm the mechanism across three models and two architecture families: retaining only the last 2,048 trace tokens captures 95--98\\% of \\texttt{exception\\_only}'s accuracy, because diagnostic events concentrate at the trace terminus.\n\nOur contributions:\n\\begin{enumerate}\n\\item \\textbf{Exception events are the minimal sufficient signal}: ${\\geq}$99.33\\% across four models and three families (1.5B--13B), with ${\\sim}$91\\% of the signal being semantic rather than format-driven (\\S\\ref{sec:cross_model}, \\S\\ref{sec:nomarker}). SFT closes a 6--49pp zero-shot gap across four models and three architecture families, and outperforms both few-shot prompting and the best regex heuristic (\\S\\ref{sec:ablation}). Cross-dataset evaluation on DebugBench ($N{=}426$) yields 100\\% (\\S\\ref{sec:debugbench}).\n\\item \\textbf{Richer traces actively hurt}: We approximately decompose why into gradient dilution (${\\sim}$26\\%) and information overload (${\\sim}$74\\%), with cross-model tail-truncation confirming positional concentration across three models (95--98\\% of \\texttt{exception\\_only} recovered; \\S\\ref{sec:density}, \\S\\ref{sec:trace_length}).\n\\item \\textbf{Two-tier diagnostic hierarchy}: Tier~1 signals (exceptions, assertions) individually achieve ${\\geq}$99\\%; Tier~2 (loop compression) reaches 85.6\\%, still +10.5pp over no trace (\\S\\ref{sec:ablation}).\n\\end{enumerate}\n",
      "numLines": 29,
      "startLine": 1,
      "totalLines": 29
    }
  },
  "sourceToolAssistantUUID": "912ea10c-19d8-4183-8164-9e4f19832389",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/.claude/sessions/review_reviewer_1_7624f219",
  "sessionId": "f76386b4-9d1f-4f92-b831-706bc4acd94d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Tool call

_source line 19 · 2026-05-17T18:02:00.014Z_

<details open><summary>🔧 Tool call — Read · `toolu_01BNhHBfgdRWo7Hjf9pWmy61`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "91bd173e-b113-4b20-ad42-6e78d985011c",
  "isSidechain": false,
  "requestId": "req_011Cb8aZnVhhhvUsy3JCV6wc",
  "type": "assistant",
  "uuid": "57ae5ae5-b4e8-4691-99bc-a7a1a17245cb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/.claude/sessions/review_reviewer_1_7624f219",
  "sessionId": "f76386b4-9d1f-4f92-b831-706bc4acd94d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015HcLXzF3feTTdP4sPwbUoc",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2318,
      "cache_read_input_tokens": 27460,
      "output_tokens": 375,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2318,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 375,
          "cache_read_input_tokens": 27460,
          "cache_creation_input_tokens": 2318,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2318
          },
          "type": "message"
        }
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

_source line 20 · 2026-05-17T18:02:00.019Z_

<details><summary>↩ Tool result · `toolu_01BNhHBfgdRWo7Hjf9pWmy61`</summary>

```text
1	\section{Method}
2	
3	\subsection{Task Definition}
4	
5	We study \emph{verdict prediction}: given a Python function, a test input, and an optional execution trace, predict whether the test passes or fails.
6	The model produces a single token (\texttt{pass} or \texttt{fail}), making this a binary classification task.
7	Unlike code generation \citep{chen2025tracepile} or output prediction \citep{gu2024cruxeval}, verdict prediction isolates the model's ability to detect faults from its ability to simulate execution.
8	
9	\subsection{Dataset}
10	\label{sec:dataset}
11	
12	We sampled 10 candidate solutions per problem from Qwen-2.5-Coder-7B-Instruct (temperature 0.8, top\_p 0.95) for 591 problems from HumanEval \citep{chen2021evaluating} (164) and MBPP-sanitized \citep{austin2021program} (427), executed each against canonical tests with \texttt{sys.settrace} to obtain line-level traces and pass/fail verdicts, yielding 5,910 pairs (67\% pass, 33\% fail).
13	The dataset is split 80/20 by problem ID into 4,720 training and 1,190 test samples (majority baseline: 71.51\%).
14	The \texttt{exception\_only} format collapses passing solutions into identical rows (39.45\% train, 48.99\% test duplicates); train--test input overlap is zero (Appendix~\ref{sec:dedup_stats}).
15	
16	\subsection{Trace Representations}
17	
18	We define seven conditions that vary the trace information available (Figure~\ref{fig:trace_overview}):
19	\begin{itemize}
20	\item \texttt{no\_trace}: Source code and test input only.
21	\item \texttt{full\_trace}: Complete line-by-line trace with variable states.
22	\item \texttt{VOTA}: Exception events + assertion-point comparisons + loop compression.
23	\item \texttt{exception\_only}: Only exception/error events.
24	\item \texttt{ae\_only}: Only assertion-point actual/expected pairs.
25	\item \texttt{loop\_only}: Only loop compression summaries.
26	\item \texttt{VOTA\_no\_ae}: VOTA without assertion-point information.
27	\end{itemize}
28	
29	\begin{figure*}[t]
30	\centering
31	\includegraphics[width=\textwidth]{fig1_trace_overview}
32	\caption{Overview of the verdict prediction pipeline. Source code and a test input are executed to produce a full raw trace. Four conditions vary the trace information: \texttt{no\_trace} (75.13\%), \texttt{full\_trace} (81.76\%), VOTA (99.41\%), and \texttt{exception\_only} (99.83\%). Accuracies for Qwen-2.5-7B (seed=42, $N{=}1{,}190$).}
33	\label{fig:trace_overview}
34	\end{figure*}
35	
36	\subsection{Models and Training}
37	
38	We evaluate four models spanning three architecture families: \textbf{Qwen-2.5-Coder-7B/1.5B-Instruct} \citep{qwen2025coder}, \textbf{CodeLlama-13B-Instruct} \citep{roziere2024code}, and \textbf{DeepSeek-Coder-6.7B-Instruct} \citep{deepseek2024coder}, covering a 1.5B--13B parameter range (8.7$\times$).
39	All conditions use LoRA \citep{hu2022lora} (rank=16, $\alpha$=32, dropout=0.05) on all linear layers, 3 epochs, effective batch size 32, LR $2 \times 10^{-4}$ with linear warmup/decay, max sequence length 2{,}048 tokens.
40	Sequences exceeding this limit are truncated while preserving the verdict label.
41	The primary seed is 42; seeds 123 and 456 test \texttt{exception\_only} robustness (Appendix~\ref{sec:training_details}).
42	
43	\subsection{Loss Ablation}
44	
45	To disentangle training signal from input signal quality, we introduce \texttt{full\_trace\_label\_only}: identical full-trace input but loss computed only on the verdict token (trace positions masked).
46	Improvement over standard \texttt{full\_trace} is attributable to \emph{gradient dilution}; the remaining gap to VOTA reflects \emph{information overload} at inference time.
47	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "57ae5ae5-b4e8-4691-99bc-a7a1a17245cb",
  "isSidechain": false,
  "promptId": "b73967ab-1e3d-4502-97ef-ede23a2a2cd7",
  "type": "user",
  "uuid": "7516d635-549f-45e3-ae92-670b63634b31",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/method.tex",
      "content": "\\section{Method}\n\n\\subsection{Task Definition}\n\nWe study \\emph{verdict prediction}: given a Python function, a test input, and an optional execution trace, predict whether the test passes or fails.\nThe model produces a single token (\\texttt{pass} or \\texttt{fail}), making this a binary classification task.\nUnlike code generation \\citep{chen2025tracepile} or output prediction \\citep{gu2024cruxeval}, verdict prediction isolates the model's ability to detect faults from its ability to simulate execution.\n\n\\subsection{Dataset}\n\\label{sec:dataset}\n\nWe sampled 10 candidate solutions per problem from Qwen-2.5-Coder-7B-Instruct (temperature 0.8, top\\_p 0.95) for 591 problems from HumanEval \\citep{chen2021evaluating} (164) and MBPP-sanitized \\citep{austin2021program} (427), executed each against canonical tests with \\texttt{sys.settrace} to obtain line-level traces and pass/fail verdicts, yielding 5,910 pairs (67\\% pass, 33\\% fail).\nThe dataset is split 80/20 by problem ID into 4,720 training and 1,190 test samples (majority baseline: 71.51\\%).\nThe \\texttt{exception\\_only} format collapses passing solutions into identical rows (39.45\\% train, 48.99\\% test duplicates); train--test input overlap is zero (Appendix~\\ref{sec:dedup_stats}).\n\n\\subsection{Trace Representations}\n\nWe define seven conditions that vary the trace information available (Figure~\\ref{fig:trace_overview}):\n\\begin{itemize}\n\\item \\texttt{no\\_trace}: Source code and test input only.\n\\item \\texttt{full\\_trace}: Complete line-by-line trace with variable states.\n\\item \\texttt{VOTA}: Exception events + assertion-point comparisons + loop compression.\n\\item \\texttt{exception\\_only}: Only exception/error events.\n\\item \\texttt{ae\\_only}: Only assertion-point actual/expected pairs.\n\\item \\texttt{loop\\_only}: Only loop compression summaries.\n\\item \\texttt{VOTA\\_no\\_ae}: VOTA without assertion-point information.\n\\end{itemize}\n\n\\begin{figure*}[t]\n\\centering\n\\includegraphics[width=\\textwidth]{fig1_trace_overview}\n\\caption{Overview of the verdict prediction pipeline. Source code and a test input are executed to produce a full raw trace. Four conditions vary the trace information: \\texttt{no\\_trace} (75.13\\%), \\texttt{full\\_trace} (81.76\\%), VOTA (99.41\\%), and \\texttt{exception\\_only} (99.83\\%). Accuracies for Qwen-2.5-7B (seed=42, $N{=}1{,}190$).}\n\\label{fig:trace_overview}\n\\end{figure*}\n\n\\subsection{Models and Training}\n\nWe evaluate four models spanning three architecture families: \\textbf{Qwen-2.5-Coder-7B/1.5B-Instruct} \\citep{qwen2025coder}, \\textbf{CodeLlama-13B-Instruct} \\citep{roziere2024code}, and \\textbf{DeepSeek-Coder-6.7B-Instruct} \\citep{deepseek2024coder}, covering a 1.5B--13B parameter range (8.7$\\times$).\nAll conditions use LoRA \\citep{hu2022lora} (rank=16, $\\alpha$=32, dropout=0.05) on all linear layers, 3 epochs, effective batch size 32, LR $2 \\times 10^{-4}$ with linear warmup/decay, max sequence length 2{,}048 tokens.\nSequences exceeding this limit are truncated while preserving the verdict label.\nThe primary seed is 42; seeds 123 and 456 test \\texttt{exception\\_only} robustness (Appendix~\\ref{sec:training_details}).\n\n\\subsection{Loss Ablation}\n\nTo disentangle training signal from input signal quality, we introduce \\texttt{full\\_trace\\_label\\_only}: identical full-trace input but loss computed only on the verdict token (trace positions masked).\nImprovement over standard \\texttt{full\\_trace} is attributable to \\emph{gradient dilution}; the remaining gap to VOTA reflects \\emph{information overload} at inference time.\n",
      "numLines": 47,
      "startLine": 1,
      "totalLines": 47
    }
  },
  "sourceToolAssistantUUID": "57ae5ae5-b4e8-4691-99bc-a7a1a17245cb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/.claude/sessions/review_reviewer_1_7624f219",
  "sessionId": "f76386b4-9d1f-4f92-b831-706bc4acd94d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Tool call

_source line 21 · 2026-05-17T18:02:00.251Z_

<details open><summary>🔧 Tool call — Read · `toolu_01TCRscjZbJe5ZctbBzSuF38`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7516d635-549f-45e3-ae92-670b63634b31",
  "isSidechain": false,
  "requestId": "req_011Cb8aZnVhhhvUsy3JCV6wc",
  "type": "assistant",
  "uuid": "02540e97-fdb7-413c-bb11-d03f19a85718",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/.claude/sessions/review_reviewer_1_7624f219",
  "sessionId": "f76386b4-9d1f-4f92-b831-706bc4acd94d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015HcLXzF3feTTdP4sPwbUoc",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2318,
      "cache_read_input_tokens": 27460,
      "output_tokens": 375,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2318,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 375,
          "cache_read_input_tokens": 27460,
          "cache_creation_input_tokens": 2318,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2318
          },
          "type": "message"
        }
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

_source line 22_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[Round 1 审稿请求]: ## Round 1 审稿任务 — Reviewer 1  **你的审查侧重**: 方法严谨性 + 实验设计 + 统计有效性 + 可复现性  ### Venue 信息 - **目标**: EMNLP 2026 via ARR May 2026 cycle - **截止日期**: 2026-05-25 - **页数限制**: Long paper ≤ 8 页正文（不含…",
  "leafUuid": "6819346e-c893-45ce-ab28-d9f88a40bc34",
  "sessionId": "f76386b4-9d1f-4f92-b831-706bc4acd94d"
}
```

---


### Runtime record

_source line 23_

```json
{
  "type": "ai-title",
  "aiTitle": "Round 1 peer review for trace verdict prediction paper",
  "sessionId": "f76386b4-9d1f-4f92-b831-706bc4acd94d"
}
```

---


### Tool result

_source line 24 · 2026-05-17T18:02:06.980Z_

<details><summary>↩ Tool result · `toolu_01TgpXmXxrrLJMtvVRnCNe3P`</summary>

```text
Web search results for query: "ACL ARR 2026 reviewer guidelines review form criteria"

Links: [{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"aclrollingreview/reviewing.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/reviewing.md"}]

I found relevant information about ACL ARR 2026 reviewer guidelines and review form criteria. Here's a summary of the key information:

## Reviewer Guidelines and Responsibilities

The reviewer's main tasks are (1) checking the appropriateness of the submission and its assignment to this reviewer, (2) writing a well-justified review, (3) updating the review as appropriate based on author-reviewer discussion.

To preserve the merits of double-blind review, reviewers for *ACL conferences and TACL should be instructed not to actively try to discover the identity of the authors and not to let any suspicion or knowledge of author identity affect their judgment of the paper.

## Review Form Criteria

The review form includes several key evaluation areas:

**Overall Assessment Scores:**
5 = Consider for Award: I think this paper could be considered for an outstanding paper award at an *ACL conference (up to top 2.5% papers). 2 = Resubmit next cycle: I think this paper needs substantial revisions that can be completed by the next ARR cycle. 1.5 = Resubmit after next cycle: I think this paper needs substantial revisions that cannot be completed by the next ARR cycle. 1 = Do not resubmit: This paper has to be fully redone, or it is not relevant to the *ACL community (e.g. it is in no way related to computational processing of language).

**Key Evaluation Categories:**
Main vs Findings papers: the main criteria for Findings are soundness and reproducibility. Conference recommendations may also consider novelty, impact and other factors.

**Additional Review Elements:**
Is there enough information in this paper for a reader to reproduce the main results, use results presented in this paper in future work (e.g., as a baseline), or build upon this work?

Please review the ACL code of ethics and the ARR checklist submitted by the authors in the submission form. If there are ethical issues with this paper, please describe them and the extent to which they have been acknowledged or addressed by the authors.

You can access the complete reviewer guidelines at [aclrollingreview.org/reviewerguidelines](http://aclrollingreview.org/reviewerguidelines) and the detailed review form at [aclrollingreview.org/reviewform](http://aclrollingreview.org/reviewform).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3b467e14-9207-4f61-a604-6c1069362688",
  "isSidechain": false,
  "promptId": "b73967ab-1e3d-4502-97ef-ede23a2a2cd7",
  "type": "user",
  "uuid": "3900d934-70bb-4940-8981-7410f1f8abd8",
  "toolUseResult": {
    "query": "ACL ARR 2026 reviewer guidelines review form criteria",
    "results": [
      {
        "tool_use_id": "srvtoolu_011zE9aneMh6ystoHWYib8vz",
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
            "title": "Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics",
            "url": "http://aclrollingreview.org/incentives2026"
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
      "I found relevant information about ACL ARR 2026 reviewer guidelines and review form criteria. Here's a summary of the key information:\n\n## Reviewer Guidelines and Responsibilities\n\nThe reviewer's main tasks are (1) checking the appropriateness of the submission and its assignment to this reviewer, (2) writing a well-justified review, (3) updating the review as appropriate based on author-reviewer discussion.\n\nTo preserve the merits of double-blind review, reviewers for *ACL conferences and TACL should be instructed not to actively try to discover the identity of the authors and not to let any suspicion or knowledge of author identity affect their judgment of the paper.\n\n## Review Form Criteria\n\nThe review form includes several key evaluation areas:\n\n**Overall Assessment Scores:**\n5 = Consider for Award: I think this paper could be considered for an outstanding paper award at an *ACL conference (up to top 2.5% papers). 2 = Resubmit next cycle: I think this paper needs substantial revisions that can be completed by the next ARR cycle. 1.5 = Resubmit after next cycle: I think this paper needs substantial revisions that cannot be completed by the next ARR cycle. 1 = Do not resubmit: This paper has to be fully redone, or it is not relevant to the *ACL community (e.g. it is in no way related to computational processing of language).\n\n**Key Evaluation Categories:**\nMain vs Findings papers: the main criteria for Findings are soundness and reproducibility. Conference recommendations may also consider novelty, impact and other factors.\n\n**Additional Review Elements:**\nIs there enough information in this paper for a reader to reproduce the main results, use results presented in this paper in future work (e.g., as a baseline), or build upon this work?\n\nPlease review the ACL code of ethics and the ARR checklist submitted by the authors in the submission form. If there are ethical issues with this paper, please describe them and the extent to which they have been acknowledged or addressed by the authors.\n\nYou can access the complete reviewer guidelines at [aclrollingreview.org/reviewerguidelines](http://aclrollingreview.org/reviewerguidelines) and the detailed review form at [aclrollingreview.org/reviewform](http://aclrollingreview.org/reviewform)."
    ],
    "durationSeconds": 9.315231531000002
  },
  "sourceToolAssistantUUID": "3b467e14-9207-4f61-a604-6c1069362688",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/.claude/sessions/review_reviewer_1_7624f219",
  "sessionId": "f76386b4-9d1f-4f92-b831-706bc4acd94d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Assistant

_source line 25 · 2026-05-17T18:02:10.095Z_

<details><summary>Logged reasoning block</summary>

```text
Let me continue reading the remaining sections and also fetch the ACL ARR review form.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3900d934-70bb-4940-8981-7410f1f8abd8",
  "isSidechain": false,
  "requestId": "req_011Cb8aajVuBwdfSNX7WampT",
  "type": "assistant",
  "uuid": "69d19bcd-d8b6-491e-9bd5-ae31c88fd98c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/.claude/sessions/review_reviewer_1_7624f219",
  "sessionId": "f76386b4-9d1f-4f92-b831-706bc4acd94d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01V6CMvB9xpGCvP17WPMMBS6",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 9267,
      "cache_creation_input_tokens": 1432,
      "cache_read_input_tokens": 29778,
      "output_tokens": 469,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1432,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 9267,
          "output_tokens": 469,
          "cache_read_input_tokens": 29778,
          "cache_creation_input_tokens": 1432,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1432
          },
          "type": "message"
        }
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

_source line 26 · 2026-05-17T18:02:10.589Z_

继续读取剩余章节和搜索官方 review form。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "69d19bcd-d8b6-491e-9bd5-ae31c88fd98c",
  "isSidechain": false,
  "requestId": "req_011Cb8aajVuBwdfSNX7WampT",
  "type": "assistant",
  "uuid": "76b95111-4e50-4e62-b4f3-2eab11a8842d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/.claude/sessions/review_reviewer_1_7624f219",
  "sessionId": "f76386b4-9d1f-4f92-b831-706bc4acd94d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01V6CMvB9xpGCvP17WPMMBS6",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 9267,
      "cache_creation_input_tokens": 1432,
      "cache_read_input_tokens": 29778,
      "output_tokens": 469,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1432,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 9267,
          "output_tokens": 469,
          "cache_read_input_tokens": 29778,
          "cache_creation_input_tokens": 1432,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1432
          },
          "type": "message"
        }
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

_source line 27 · 2026-05-17T18:02:12.018Z_

<details open><summary>🔧 Tool call — Read · `toolu_014JB8KC2W2TaXmq9wFskeir`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "76b95111-4e50-4e62-b4f3-2eab11a8842d",
  "isSidechain": false,
  "requestId": "req_011Cb8aajVuBwdfSNX7WampT",
  "type": "assistant",
  "uuid": "b8b7c5d5-b079-4c9f-84f9-74d7b5c4d191",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/.claude/sessions/review_reviewer_1_7624f219",
  "sessionId": "f76386b4-9d1f-4f92-b831-706bc4acd94d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01V6CMvB9xpGCvP17WPMMBS6",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 9267,
      "cache_creation_input_tokens": 1432,
      "cache_read_input_tokens": 29778,
      "output_tokens": 469,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1432,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 9267,
          "output_tokens": 469,
          "cache_read_input_tokens": 29778,
          "cache_creation_input_tokens": 1432,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1432
          },
          "type": "message"
        }
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

_source line 28 · 2026-05-17T18:02:12.026Z_

<details><summary>↩ Tool result · `toolu_014JB8KC2W2TaXmq9wFskeir`</summary>

```text
1	\section{Discussion}
2	
3	Verdict prediction is fundamentally fault detection: the model must determine whether execution deviated from expected behavior.
4	Exception events succeed because they are the runtime's primary fault indicator.
5	When Python raises an unhandled exception, it records exactly what went wrong (the error type), where it happened (the stack frame), and why (the error message).
6	This is precisely the information needed for a pass/fail decision, packaged in a compact, self-contained format.
7	Non-exception trace components (variable states, loop iterations, line-by-line control flow) record \emph{how} the program ran, not \emph{whether} it failed, and dilute the model's attention without providing complementary diagnostic information.
8	
9	This mechanistic account explains three key results.
10	First, adding trace information beyond exceptions actively \emph{hurts} (VOTA $<$ \texttt{exception\_only}, Table~\ref{tab:ablation}), because non-diagnostic content competes for attention.
11	Second, tail-truncation captures 95--98\% of \texttt{exception\_only}'s accuracy across three models and two architecture families (\S\ref{sec:trace_length}), because exceptions are recorded near the trace terminus where Python's error propagation concentrates them (though not at the absolute end: \texttt{tail\_256} ${\approx}$ \texttt{no\_trace}, with the signal localized in a 256--512 token window from the end).
12	Third, the 6.22pp SFT advantage over the best regex baseline concentrates on caught-exception boundary cases (Appendix~\ref{sec:regex_baselines}), confirming the model learns to distinguish \emph{whether an exception terminated execution} rather than merely detecting exception presence.
13	The 0.56pp cross-model exception gap (Appendix~\ref{sec:robustness_analysis}) and the format-collapse nature of the DeepSeek outlier (Appendix~\ref{sec:training_dynamics}) further support that the signal, not the model, is the binding constraint.
14	
15	\paragraph{Why exception\_only outperforms ae\_only.}
16	Although \texttt{ae\_only} achieves 99.92\% on seed 42, it is a strict superset of the exception signal: assertion-point comparisons include the exception event (when present) plus additional information such as fallback local variable states.
17	Multi-seed evaluation reveals that this extra content introduces noise: \texttt{ae\_only} achieves 99.64\% mean accuracy ($\pm$0.49, seeds 42/123/456) while \texttt{exception\_only} achieves 99.83\% ($\pm$0.00).
18	The zero-variance result for \texttt{exception\_only} indicates that it captures a minimal sufficient signal (the compact exception event), while \texttt{ae\_only}'s additional components (fallback locals, assertion formatting) occasionally mislead the model, manifesting as seed-dependent variance ($\sigma{=}$0.49pp).
19	Attention analysis on representative samples confirms this interpretation: within exception events, the error type and location markers receive 5--10$\times$ higher per-token attention than the verbose locals context (module paths, imported objects), suggesting the model learns to focus on diagnostic signals rather than incidental runtime state.
20	Thus \texttt{exception\_only} is both more precise and more stable than its superset.
21	
22	\paragraph{SFT vs.\ regex incremental analysis.}
23	The gap between B5 (format marker, 99.33\%) and SFT \texttt{exception\_only} (99.83\%) isolates the value of learned semantic understanding (McNemar $p{=}0.041$, Table~\ref{tab:regex}).
24	Among 8 test samples where pass-labeled code triggers exceptions (from 2 distinct problems), the SFT model correctly classifies 6 (all from MBPP/113, a try/except ValueError pattern) while B5 misclassifies all 8. The 2 remaining errors (HumanEval/95, GeneratorExit) are misclassified by most training configurations (see Appendix~\ref{sec:irreducible}). At the problem level, SFT handles 1/2 exception-type edge cases vs B5's 0/2.
25	This confirms that SFT learns a genuine semantic boundary (distinguishing caught from uncaught exceptions) rather than merely detecting exception presence or format markers.
26	
27	\paragraph{Why zero-shot and few-shot prompting fall short.}
28	Zero-shot prompting spans 51.0--93.5\% across four models, with cross-architecture variance (42.44pp) dwarfing the SFT range (0.56pp).
29	The failure is not in exception detection but in verdict calibration: the model recognizes that an exception occurred but cannot reliably determine whether it terminated execution or was caught by a \texttt{try/except} block.
30	Performance does not correlate with model size: Qwen-1.5B (93.45\%) outperforms Qwen-7B (89.08\%) and CodeLlama-13B (51.01\%, extreme fail bias with 72.4\% of predictions as \texttt{fail}).
31	Within the Qwen family, the 1.5B model's higher zero-shot accuracy likely reflects consistent code training data quality across scales: the smaller model already understands exception format, but both lack the verdict-specific calibration that SFT provides (SFT gap: 6.38pp for 1.5B vs.\ 10.75pp for 7B).
32	Three-shot in-context learning (90.84\% on Qwen-7B, fail recall = 80.53\%) improves fail recall by 13.57pp over zero-shot but still trails SFT by 8.99pp: three examples cannot cover the diversity of caught-exception patterns in the training distribution.
33	SFT normalizes this cross-architecture variance by grounding exception patterns in task-specific verdict labels, compressing a 42.44pp zero-shot range to 0.56pp.
34	
35	\paragraph{Format marker sensitivity.}
36	The B5 baseline (Appendix~\ref{sec:regex_baselines}) achieves 99.33\% by exploiting a deterministic format marker (\texttt{[No exception data in trace]}) present in all pass samples.
37	This near-ceiling performance from a trivial pattern raises a concern: does SFT also learn this shortcut?
38	The answer is partially yes: the format marker correlates perfectly with the pass class. But the SFT model additionally handles the 8 boundary samples where exceptions occur in passing code, achieving 6/8 correct vs.\ B5's 0/8.
39	A \emph{nomarker} ablation (\S\ref{sec:nomarker}) confirms genuine exception semantics: Qwen-7B 3-seed mean 97.65\%$\pm$0.96 and Qwen-1.5B 97.82\%, a drop of only ${\sim}$2pp.
40	The marker contribution (${\sim}$9\% of total lift) is small relative to semantic content (${\sim}$91\%), confirming that SFT learns exception semantics rather than format shortcuts.
41	Both signal layers show comparable accuracy across the two tested scales (1.5B and 7B produce 97.8\% and 97.7\% nomarker accuracy, respectively).
42	
43	\paragraph{Near-perfect floor, not hard ceiling.}
44	Samples 901 and 905 (HumanEval/95, \texttt{check\_dict\_case}) are misclassified by most configurations: Qwen-7B (3 seeds), Qwen-1.5B, and CodeLlama-13B seed 42/456 all produce exactly these 2 errors.
45	The root cause is deterministic: Python's \texttt{all()} raises \texttt{GeneratorExit} (a \texttt{BaseException} subclass) during generator short-circuit, recorded as \texttt{[ERROR]} despite the test passing.
46	However, CodeLlama-13B seed 123 achieves 100\% (0/1190 errors), correctly classifying both samples.
47	This confirms that 99.83\% is a near-perfect \emph{floor} (the convergence attractor for most initializations) rather than a hard data limitation: the representation supports perfect accuracy, though most LoRA initializations converge to the same 2-error basin.
48	On this task, exception-only accuracy is \emph{signal-limited} rather than \emph{capacity-limited}: three architecture families spanning 1.5B to 13B converge on the same floor, while \texttt{no\_trace} shows monotonic scale dependence (67.3\% $\to$ 75.1\% $\to$ 76.5\%).
49	
50	\paragraph{Tier hierarchy: practical implications.}
51	The two-tier structure (Tier~1 ${\geq}$99\%; Tier~2 = 85.6\%) has direct engineering implications for trace-augmented systems.
52	First, it implies a \emph{diminishing returns} principle: once a Tier~1 signal is available, adding more trace information provides no benefit and may actively degrade performance through attention dilution.
53	Second, the hierarchy suggests a fallback design: systems should attempt Tier~1 extraction (exception events) and only resort to Tier~2 signals (loop compression) when no exception is raised. Even Tier~2 alone substantially outperforms no-trace baselines (+10.50pp).
54	Third, the minimal token footprint of Tier~1 signals (median 150 tokens vs.\ ${\sim}$1{,}900 for VOTA post-truncation) makes them viable for deployment in token-constrained settings (e.g., real-time CI pipelines, mobile inference).
55	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b8b7c5d5-b079-4c9f-84f9-74d7b5c4d191",
  "isSidechain": false,
  "promptId": "b73967ab-1e3d-4502-97ef-ede23a2a2cd7",
  "type": "user",
  "uuid": "628c415a-9838-4ccf-a7cf-1d546c3db828",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/discussion.tex",
      "content": "\\section{Discussion}\n\nVerdict prediction is fundamentally fault detection: the model must determine whether execution deviated from expected behavior.\nException events succeed because they are the runtime's primary fault indicator.\nWhen Python raises an unhandled exception, it records exactly what went wrong (the error type), where it happened (the stack frame), and why (the error message).\nThis is precisely the information needed for a pass/fail decision, packaged in a compact, self-contained format.\nNon-exception trace components (variable states, loop iterations, line-by-line control flow) record \\emph{how} the program ran, not \\emph{whether} it failed, and dilute the model's attention without providing complementary diagnostic information.\n\nThis mechanistic account explains three key results.\nFirst, adding trace information beyond exceptions actively \\emph{hurts} (VOTA $<$ \\texttt{exception\\_only}, Table~\\ref{tab:ablation}), because non-diagnostic content competes for attention.\nSecond, tail-truncation captures 95--98\\% of \\texttt{exception\\_only}'s accuracy across three models and two architecture families (\\S\\ref{sec:trace_length}), because exceptions are recorded near the trace terminus where Python's error propagation concentrates them (though not at the absolute end: \\texttt{tail\\_256} ${\\approx}$ \\texttt{no\\_trace}, with the signal localized in a 256--512 token window from the end).\nThird, the 6.22pp SFT advantage over the best regex baseline concentrates on caught-exception boundary cases (Appendix~\\ref{sec:regex_baselines}), confirming the model learns to distinguish \\emph{whether an exception terminated execution} rather than merely detecting exception presence.\nThe 0.56pp cross-model exception gap (Appendix~\\ref{sec:robustness_analysis}) and the format-collapse nature of the DeepSeek outlier (Appendix~\\ref{sec:training_dynamics}) further support that the signal, not the model, is the binding constraint.\n\n\\paragraph{Why exception\\_only outperforms ae\\_only.}\nAlthough \\texttt{ae\\_only} achieves 99.92\\% on seed 42, it is a strict superset of the exception signal: assertion-point comparisons include the exception event (when present) plus additional information such as fallback local variable states.\nMulti-seed evaluation reveals that this extra content introduces noise: \\texttt{ae\\_only} achieves 99.64\\% mean accuracy ($\\pm$0.49, seeds 42/123/456) while \\texttt{exception\\_only} achieves 99.83\\% ($\\pm$0.00).\nThe zero-variance result for \\texttt{exception\\_only} indicates that it captures a minimal sufficient signal (the compact exception event), while \\texttt{ae\\_only}'s additional components (fallback locals, assertion formatting) occasionally mislead the model, manifesting as seed-dependent variance ($\\sigma{=}$0.49pp).\nAttention analysis on representative samples confirms this interpretation: within exception events, the error type and location markers receive 5--10$\\times$ higher per-token attention than the verbose locals context (module paths, imported objects), suggesting the model learns to focus on diagnostic signals rather than incidental runtime state.\nThus \\texttt{exception\\_only} is both more precise and more stable than its superset.\n\n\\paragraph{SFT vs.\\ regex incremental analysis.}\nThe gap between B5 (format marker, 99.33\\%) and SFT \\texttt{exception\\_only} (99.83\\%) isolates the value of learned semantic understanding (McNemar $p{=}0.041$, Table~\\ref{tab:regex}).\nAmong 8 test samples where pass-labeled code triggers exceptions (from 2 distinct problems), the SFT model correctly classifies 6 (all from MBPP/113, a try/except ValueError pattern) while B5 misclassifies all 8. The 2 remaining errors (HumanEval/95, GeneratorExit) are misclassified by most training configurations (see Appendix~\\ref{sec:irreducible}). At the problem level, SFT handles 1/2 exception-type edge cases vs B5's 0/2.\nThis confirms that SFT learns a genuine semantic boundary (distinguishing caught from uncaught exceptions) rather than merely detecting exception presence or format markers.\n\n\\paragraph{Why zero-shot and few-shot prompting fall short.}\nZero-shot prompting spans 51.0--93.5\\% across four models, with cross-architecture variance (42.44pp) dwarfing the SFT range (0.56pp).\nThe failure is not in exception detection but in verdict calibration: the model recognizes that an exception occurred but cannot reliably determine whether it terminated execution or was caught by a \\texttt{try/except} block.\nPerformance does not correlate with model size: Qwen-1.5B (93.45\\%) outperforms Qwen-7B (89.08\\%) and CodeLlama-13B (51.01\\%, extreme fail bias with 72.4\\% of predictions as \\texttt{fail}).\nWithin the Qwen family, the 1.5B model's higher zero-shot accuracy likely reflects consistent code training data quality across scales: the smaller model already understands exception format, but both lack the verdict-specific calibration that SFT provides (SFT gap: 6.38pp for 1.5B vs.\\ 10.75pp for 7B).\nThree-shot in-context learning (90.84\\% on Qwen-7B, fail recall = 80.53\\%) improves fail recall by 13.57pp over zero-shot but still trails SFT by 8.99pp: three examples cannot cover the diversity of caught-exception patterns in the training distribution.\nSFT normalizes this cross-architecture variance by grounding exception patterns in task-specific verdict labels, compressing a 42.44pp zero-shot range to 0.56pp.\n\n\\paragraph{Format marker sensitivity.}\nThe B5 baseline (Appendix~\\ref{sec:regex_baselines}) achieves 99.33\\% by exploiting a deterministic format marker (\\texttt{[No exception data in trace]}) present in all pass samples.\nThis near-ceiling performance from a trivial pattern raises a concern: does SFT also learn this shortcut?\nThe answer is partially yes: the format marker correlates perfectly with the pass class. But the SFT model additionally handles the 8 boundary samples where exceptions occur in passing code, achieving 6/8 correct vs.\\ B5's 0/8.\nA \\emph{nomarker} ablation (\\S\\ref{sec:nomarker}) confirms genuine exception semantics: Qwen-7B 3-seed mean 97.65\\%$\\pm$0.96 and Qwen-1.5B 97.82\\%, a drop of only ${\\sim}$2pp.\nThe marker contribution (${\\sim}$9\\% of total lift) is small relative to semantic content (${\\sim}$91\\%), confirming that SFT learns exception semantics rather than format shortcuts.\nBoth signal layers show comparable accuracy across the two tested scales (1.5B and 7B produce 97.8\\% and 97.7\\% nomarker accuracy, respectively).\n\n\\paragraph{Near-perfect floor, not hard ceiling.}\nSamples 901 and 905 (HumanEval/95, \\texttt{check\\_dict\\_case}) are misclassified by most configurations: Qwen-7B (3 seeds), Qwen-1.5B, and CodeLlama-13B seed 42/456 all produce exactly these 2 errors.\nThe root cause is deterministic: Python's \\texttt{all()} raises \\texttt{GeneratorExit} (a \\texttt{BaseException} subclass) during generator short-circuit, recorded as \\texttt{[ERROR]} despite the test passing.\nHowever, CodeLlama-13B seed 123 achieves 100\\% (0/1190 errors), correctly classifying both samples.\nThis confirms that 99.83\\% is a near-perfect \\emph{floor} (the convergence attractor for most initializations) rather than a hard data limitation: the representation supports perfect accuracy, though most LoRA initializations converge to the same 2-error basin.\nOn this task, exception-only accuracy is \\emph{signal-limited} rather than \\emph{capacity-limited}: three architecture families spanning 1.5B to 13B converge on the same floor, while \\texttt{no\\_trace} shows monotonic scale dependence (67.3\\% $\\to$ 75.1\\% $\\to$ 76.5\\%).\n\n\\paragraph{Tier hierarchy: practical implications.}\nThe two-tier structure (Tier~1 ${\\geq}$99\\%; Tier~2 = 85.6\\%) has direct engineering implications for trace-augmented systems.\nFirst, it implies a \\emph{diminishing returns} principle: once a Tier~1 signal is available, adding more trace information provides no benefit and may actively degrade performance through attention dilution.\nSecond, the hierarchy suggests a fallback design: systems should attempt Tier~1 extraction (exception events) and only resort to Tier~2 signals (loop compression) when no exception is raised. Even Tier~2 alone substantially outperforms no-trace baselines (+10.50pp).\nThird, the minimal token footprint of Tier~1 signals (median 150 tokens vs.\\ ${\\sim}$1{,}900 for VOTA post-truncation) makes them viable for deployment in token-constrained settings (e.g., real-time CI pipelines, mobile inference).\n",
      "numLines": 55,
      "startLine": 1,
      "totalLines": 55
    }
  },
  "sourceToolAssistantUUID": "b8b7c5d5-b079-4c9f-84f9-74d7b5c4d191",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/.claude/sessions/review_reviewer_1_7624f219",
  "sessionId": "f76386b4-9d1f-4f92-b831-706bc4acd94d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Tool call

_source line 29 · 2026-05-17T18:02:13.030Z_

<details open><summary>🔧 Tool call — Read · `toolu_01E7dn7iAwaVPEbqprMYpKpf`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "628c415a-9838-4ccf-a7cf-1d546c3db828",
  "isSidechain": false,
  "requestId": "req_011Cb8aajVuBwdfSNX7WampT",
  "type": "assistant",
  "uuid": "4b882775-4b97-4204-95ec-1ff9bc351b35",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/.claude/sessions/review_reviewer_1_7624f219",
  "sessionId": "f76386b4-9d1f-4f92-b831-706bc4acd94d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01V6CMvB9xpGCvP17WPMMBS6",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 9267,
      "cache_creation_input_tokens": 1432,
      "cache_read_input_tokens": 29778,
      "output_tokens": 469,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1432,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 9267,
          "output_tokens": 469,
          "cache_read_input_tokens": 29778,
          "cache_creation_input_tokens": 1432,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1432
          },
          "type": "message"
        }
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

_source line 30 · 2026-05-17T18:02:13.039Z_

<details><summary>↩ Tool result · `toolu_01E7dn7iAwaVPEbqprMYpKpf`</summary>

```text
1	\section{Related Work}
2	
3	\paragraph{Execution Traces for Code LLMs.}
4	TracePile \citep{chen2025tracepile} scaled trace-augmented training to 2.6M samples; \citet{wang2025dcsh} found trace utility to be task- and format-dependent, a finding we extend by identifying exception events as the dominant signal for verdict prediction.
5	NExT \citep{ni2024next} and ET-CoT \citep{eguchi2025etcot} leveraged trace chain-of-thought for repair and execution reasoning.
6	\citet{ferrando2025execute} found compact traces comparable to full traces, supporting our information density finding.
7	CRUXEval \citep{gu2024cruxeval} established execution reasoning benchmarks, extended to 19 languages by \citet{xu2025cruxevalx}.
8	None decompose which trace components contribute to \emph{classification} accuracy.
9	
10	\paragraph{Code Verdict and Patch Classification.}
11	TRACED \citep{ding2024traced} showed execution-aware pretraining improves vulnerability and clone detection.
12	In patch correctness, APPT \citep{appt2024} achieved 79.7\% with BERT+LSTM; LLM4PatchCorrect \citep{zhou2024llm4patch} reached 84.4\% using execution traces.
13	FuseFL \citep{widyasari2024fusefl} demonstrated that structured fault signals improve fault localization.
14	\citet{foster2025mutation} deployed LLM-based equivalence detection at Meta with 0.95 precision.
15	These approaches treat traces as monolithic inputs; none isolate individual components, compare against rule-based baselines to quantify the value of learned representations, or test cross-model generalization.
16	
17	\paragraph{Fault Localization.}
18	Spectrum-based fault localization (SBFL) ranks program elements by statistical suspiciousness computed from passing/failing test spectra.
19	Classic metrics (Ochiai \citep{abreu2007accuracy}, Tarantula \citep{jones2002visualization}, DStar \citep{wong2014dstar}) share a core insight with our work: abnormal execution events (here, coverage patterns correlated with failure) are the most informative diagnostic signal.
20	Recent LLM-based approaches extend this: AutoFL \citep{kang2024autofl} uses function-level call graphs with ChatGPT; AgentFL \citep{qin2024agentfl} introduces multi-agent localization; LLM4FL \citep{widyasari2024llm4fl} combines SBFL spectra with LLM reasoning; and \citet{mukherjee2025llmfl} demonstrate that LLMs can localize faults from test failure information alone.
21	Verdict prediction is a prerequisite to fault localization: one must first determine \emph{whether} a fault exists before localizing \emph{where} it is.
22	Our exception-based approach and SBFL share the principle that anomalous execution events carry the strongest diagnostic signal, but operate at different granularities: we classify at the test level (pass/fail) while FL localizes at the statement or method level.
23	
24	\paragraph{Trace Compression and Selection.}
25	TraceCoder \citep{huang2026tracecoder} and InspectCoder \citep{wang2025inspectcoder} use selective trace extraction for debugging; \citet{haque2025traces} found raw traces provide limited repair benefit, supporting our compression finding.
26	Our approximate information density decomposition (gradient dilution ${\sim}$26\% vs.\ information overload ${\sim}$74\%) provides the first quantitative framework for \emph{why} compression helps, complementing these methods' focus on \emph{how} to compress.
27	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4b882775-4b97-4204-95ec-1ff9bc351b35",
  "isSidechain": false,
  "promptId": "b73967ab-1e3d-4502-97ef-ede23a2a2cd7",
  "type": "user",
  "uuid": "78436608-a7d5-49a5-b3c1-4e7a8db3d94c",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/related_work.tex",
      "content": "\\section{Related Work}\n\n\\paragraph{Execution Traces for Code LLMs.}\nTracePile \\citep{chen2025tracepile} scaled trace-augmented training to 2.6M samples; \\citet{wang2025dcsh} found trace utility to be task- and format-dependent, a finding we extend by identifying exception events as the dominant signal for verdict prediction.\nNExT \\citep{ni2024next} and ET-CoT \\citep{eguchi2025etcot} leveraged trace chain-of-thought for repair and execution reasoning.\n\\citet{ferrando2025execute} found compact traces comparable to full traces, supporting our information density finding.\nCRUXEval \\citep{gu2024cruxeval} established execution reasoning benchmarks, extended to 19 languages by \\citet{xu2025cruxevalx}.\nNone decompose which trace components contribute to \\emph{classification} accuracy.\n\n\\paragraph{Code Verdict and Patch Classification.}\nTRACED \\citep{ding2024traced} showed execution-aware pretraining improves vulnerability and clone detection.\nIn patch correctness, APPT \\citep{appt2024} achieved 79.7\\% with BERT+LSTM; LLM4PatchCorrect \\citep{zhou2024llm4patch} reached 84.4\\% using execution traces.\nFuseFL \\citep{widyasari2024fusefl} demonstrated that structured fault signals improve fault localization.\n\\citet{foster2025mutation} deployed LLM-based equivalence detection at Meta with 0.95 precision.\nThese approaches treat traces as monolithic inputs; none isolate individual components, compare against rule-based baselines to quantify the value of learned representations, or test cross-model generalization.\n\n\\paragraph{Fault Localization.}\nSpectrum-based fault localization (SBFL) ranks program elements by statistical suspiciousness computed from passing/failing test spectra.\nClassic metrics (Ochiai \\citep{abreu2007accuracy}, Tarantula \\citep{jones2002visualization}, DStar \\citep{wong2014dstar}) share a core insight with our work: abnormal execution events (here, coverage patterns correlated with failure) are the most informative diagnostic signal.\nRecent LLM-based approaches extend this: AutoFL \\citep{kang2024autofl} uses function-level call graphs with ChatGPT; AgentFL \\citep{qin2024agentfl} introduces multi-agent localization; LLM4FL \\citep{widyasari2024llm4fl} combines SBFL spectra with LLM reasoning; and \\citet{mukherjee2025llmfl} demonstrate that LLMs can localize faults from test failure information alone.\nVerdict prediction is a prerequisite to fault localization: one must first determine \\emph{whether} a fault exists before localizing \\emph{where} it is.\nOur exception-based approach and SBFL share the principle that anomalous execution events carry the strongest diagnostic signal, but operate at different granularities: we classify at the test level (pass/fail) while FL localizes at the statement or method level.\n\n\\paragraph{Trace Compression and Selection.}\nTraceCoder \\citep{huang2026tracecoder} and InspectCoder \\citep{wang2025inspectcoder} use selective trace extraction for debugging; \\citet{haque2025traces} found raw traces provide limited repair benefit, supporting our compression finding.\nOur approximate information density decomposition (gradient dilution ${\\sim}$26\\% vs.\\ information overload ${\\sim}$74\\%) provides the first quantitative framework for \\emph{why} compression helps, complementing these methods' focus on \\emph{how} to compress.\n",
      "numLines": 27,
      "startLine": 1,
      "totalLines": 27
    }
  },
  "sourceToolAssistantUUID": "4b882775-4b97-4204-95ec-1ff9bc351b35",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/.claude/sessions/review_reviewer_1_7624f219",
  "sessionId": "f76386b4-9d1f-4f92-b831-706bc4acd94d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Tool call

_source line 31 · 2026-05-17T18:02:13.514Z_

<details open><summary>🔧 Tool call — Read · `toolu_01ADdrkUYkEH7noyKL29xw5x`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "78436608-a7d5-49a5-b3c1-4e7a8db3d94c",
  "isSidechain": false,
  "requestId": "req_011Cb8aajVuBwdfSNX7WampT",
  "type": "assistant",
  "uuid": "3c8ab94e-9142-4ef7-8f37-f0e964ca80ea",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/.claude/sessions/review_reviewer_1_7624f219",
  "sessionId": "f76386b4-9d1f-4f92-b831-706bc4acd94d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01V6CMvB9xpGCvP17WPMMBS6",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 9267,
      "cache_creation_input_tokens": 1432,
      "cache_read_input_tokens": 29778,
      "output_tokens": 469,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1432,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 9267,
          "output_tokens": 469,
          "cache_read_input_tokens": 29778,
          "cache_creation_input_tokens": 1432,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1432
          },
          "type": "message"
        }
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

_source line 32 · 2026-05-17T18:02:13.519Z_

<details><summary>↩ Tool result · `toolu_01ADdrkUYkEH7noyKL29xw5x`</summary>

```text
1	\section{Conclusion}
2	
3	We presented the first systematic component ablation of trace representations for verdict prediction across four models (1.5B--13B, three architecture families).
4	Exception events alone achieve ${\geq}$99.33\% across all four models (${\geq}$99.83\% on three of four; one seed reaches 100\%), while \texttt{no\_trace} shows 9.19pp scale sensitivity (67.3--76.5\%).
5	Adding more trace information actively hurts: the gap approximately decomposes into information overload (${\sim}$74\%) and gradient dilution (${\sim}$26\%), and tail-truncation confirms that diagnostic signal concentrates at the trace terminus.
6	A format-marker ablation shows ${\sim}$91\% of the exception signal is semantic rather than format-driven, and cross-dataset evaluation on DebugBench confirms generalization (\texttt{exception\_only}: 100\%, $N{=}426$).
7	
8	The broader implication is that verdict prediction is not an information-starved task that benefits from richer context.
9	It is a fault detection task where the runtime has already surfaced the critical diagnostic signal; the model's role is to interpret whether that signal indicates a terminal fault (as the SFT advantage over regex on caught-exception cases confirms).
10	This reframing suggests a design principle for trace-augmented systems: extract the highest-specificity diagnostic signal (median 150 tokens) and discard everything else.
11	Future work should test whether this principle extends to additional programming languages, larger real-world codebases, silent logic errors where no exception is raised, and tasks beyond verdict prediction.
12	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3c8ab94e-9142-4ef7-8f37-f0e964ca80ea",
  "isSidechain": false,
  "promptId": "b73967ab-1e3d-4502-97ef-ede23a2a2cd7",
  "type": "user",
  "uuid": "e76c0536-1eb4-4e14-8bc4-0c6d6d8481ad",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/conclusion.tex",
      "content": "\\section{Conclusion}\n\nWe presented the first systematic component ablation of trace representations for verdict prediction across four models (1.5B--13B, three architecture families).\nException events alone achieve ${\\geq}$99.33\\% across all four models (${\\geq}$99.83\\% on three of four; one seed reaches 100\\%), while \\texttt{no\\_trace} shows 9.19pp scale sensitivity (67.3--76.5\\%).\nAdding more trace information actively hurts: the gap approximately decomposes into information overload (${\\sim}$74\\%) and gradient dilution (${\\sim}$26\\%), and tail-truncation confirms that diagnostic signal concentrates at the trace terminus.\nA format-marker ablation shows ${\\sim}$91\\% of the exception signal is semantic rather than format-driven, and cross-dataset evaluation on DebugBench confirms generalization (\\texttt{exception\\_only}: 100\\%, $N{=}426$).\n\nThe broader implication is that verdict prediction is not an information-starved task that benefits from richer context.\nIt is a fault detection task where the runtime has already surfaced the critical diagnostic signal; the model's role is to interpret whether that signal indicates a terminal fault (as the SFT advantage over regex on caught-exception cases confirms).\nThis reframing suggests a design principle for trace-augmented systems: extract the highest-specificity diagnostic signal (median 150 tokens) and discard everything else.\nFuture work should test whether this principle extends to additional programming languages, larger real-world codebases, silent logic errors where no exception is raised, and tasks beyond verdict prediction.\n",
      "numLines": 12,
      "startLine": 1,
      "totalLines": 12
    }
  },
  "sourceToolAssistantUUID": "3c8ab94e-9142-4ef7-8f37-f0e964ca80ea",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/.claude/sessions/review_reviewer_1_7624f219",
  "sessionId": "f76386b4-9d1f-4f92-b831-706bc4acd94d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Tool call

_source line 33 · 2026-05-17T18:02:13.985Z_

<details open><summary>🔧 Tool call — Read · `toolu_01UakpCZqeepLUQ2iX6gtWoj`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e76c0536-1eb4-4e14-8bc4-0c6d6d8481ad",
  "isSidechain": false,
  "requestId": "req_011Cb8aajVuBwdfSNX7WampT",
  "type": "assistant",
  "uuid": "8fc5a144-20f7-4071-9749-04274da87881",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/.claude/sessions/review_reviewer_1_7624f219",
  "sessionId": "f76386b4-9d1f-4f92-b831-706bc4acd94d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01V6CMvB9xpGCvP17WPMMBS6",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 9267,
      "cache_creation_input_tokens": 1432,
      "cache_read_input_tokens": 29778,
      "output_tokens": 469,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1432,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 9267,
          "output_tokens": 469,
          "cache_read_input_tokens": 29778,
          "cache_creation_input_tokens": 1432,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1432
          },
          "type": "message"
        }
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

_source line 34 · 2026-05-17T18:02:14.241Z_

<details><summary>↩ Tool result · `toolu_01UakpCZqeepLUQ2iX6gtWoj`</summary>

```text
1	\section{Per-Class Performance Breakdown}
2	\label{sec:per_class}
3	
4	Table~\ref{tab:per_class} reports per-class precision, recall, and F1 for all experimental conditions.
5	
6	\begin{table*}[t]
7	\centering
8	\caption{Per-class precision, recall, and F1 for all experimental conditions (seed 42). DeepSeek VOTA achieves 100\% fail precision but only 45.4\% fail recall, indicating systematic bias toward predicting \texttt{pass}. DeepSeek \texttt{exception\_only} seed 42 achieves 100\% fail recall, but seed 123 drops to 70.5\% (see Table~\ref{tab:full_deepseek}).}
9	\label{tab:per_class}
10	\small
11	\begin{tabular}{llccccccc}
12	\toprule
13	\textbf{Condition} & \textbf{Model} & \textbf{Acc} & \textbf{Pass P} & \textbf{Pass R} & \textbf{Pass F1} & \textbf{Fail P} & \textbf{Fail R} & \textbf{Fail F1} \\
14	\midrule
15	No Trace          & Qwen-2.5-7B & 75.13 & 87.76 & 75.79 & 81.34 & 54.73 & 73.45 & 62.72 \\
16	Full Trace        & Qwen-2.5-7B & 81.76 & 87.74 & 86.60 & 87.17 & 67.43 & 69.62 & 68.51 \\
17	Full Trace (LO)   & Qwen-2.5-7B & 86.22 & 88.21 & 93.18 & 90.63 & 80.07 & 68.73 & 73.97 \\
18	VOTA              & Qwen-2.5-7B & 99.41 & 100.00 & 99.18 & 99.59 & 97.98 & 100.00 & 98.98 \\
19	Exception Only    & Qwen-2.5-7B & 99.83 & 100.00 & 99.76 & 99.88 & 99.41 & 100.00 & 99.71 \\
20	AE Only           & Qwen-2.5-7B & 99.92 & 100.00 & 99.88 & 99.94 & 99.71 & 100.00 & 99.85 \\
21	Loop Only         & Qwen-2.5-7B & 85.63 & 92.39 & 87.07 & 89.66 & 71.65 & 82.01 & 76.48 \\
22	VOTA\_no\_ae       & Qwen-2.5-7B & 99.41 & 99.88 & 99.29 & 99.59 & 98.26 & 99.71 & 98.98 \\
23	\midrule
24	No Trace          & DeepSeek-6.7B & 73.36 & 81.71 & 80.85 & 81.28 & 53.16 & 54.57 & 53.86 \\
25	Full Trace        & DeepSeek-6.7B & 79.16 & 85.70 & 85.10 & 85.40 & 63.20 & 64.30 & 63.70 \\
26	VOTA              & DeepSeek-6.7B & 84.45 & 82.14 & 100.00 & 90.20 & 100.00 & 45.40 & 62.50 \\
27	Exception Only    & DeepSeek-6.7B & 99.33 & 100.00 & 99.06 & 99.53 & 97.69 & 100.00 & 98.83 \\
28	\bottomrule
29	\end{tabular}
30	\end{table*}
31	
32	%% ============================================================
33	\section{Training Details}
34	\label{sec:training_details}
35	
36	Table~\ref{tab:hyperparams} summarizes the training hyperparameters shared across all conditions.
37	All experiments use the HuggingFace TRL \texttt{SFTTrainer} with LoRA \citep{hu2022lora} applied to all linear layers.
38	
39	\begin{table}[t]
40	\centering
41	\caption{Training hyperparameters (shared across all conditions).}
42	\label{tab:hyperparams}
43	\small
44	\resizebox{\columnwidth}{!}{%
45	\begin{tabular}{ll}
46	\toprule
47	\textbf{Hyperparameter} & \textbf{Value} \\
48	\midrule
49	LoRA rank ($r$)            & 16 \\
50	LoRA alpha ($\alpha$)      & 32 \\
51	LoRA dropout               & 0.05 \\
52	LoRA target modules        & all linear layers \\
53	\midrule
54	Epochs                     & 3 \\
55	Per-device batch size       & 4 \\
56	Gradient accumulation steps & 8 \\
57	Effective batch size        & 32 \\
58	\midrule
59	Learning rate               & $2 \times 10^{-4}$ \\
60	LR scheduler                & linear decay \\
61	Warmup ratio                & 0.1 \\
62	Weight decay                & 0.01 \\
63	\midrule
64	Max sequence length         & 2048 tokens \\
65	Primary seed                & 42 \\
66	Robustness seeds            & 123, 456 \\
67	\midrule
68	Hardware                    & 1$\times$ RTX PRO 6000 Blackwell (96\,GB VRAM) \\
69	Framework                   & HuggingFace TRL SFTTrainer \\
70	\bottomrule
71	\end{tabular}%
72	}
73	\end{table}
74	
75	Table~\ref{tab:train_time} reports per-condition training wall-clock times.
76	Conditions with longer trace inputs (e.g., \texttt{full\_trace}, VOTA) require proportionally more training time due to increased sequence lengths.
77	
78	\begin{table}[t]
79	\centering
80	\caption{Training wall-clock time per condition on a single RTX PRO 6000 Blackwell GPU. Where multiple seeds were run, individual times are listed.}
81	\label{tab:train_time}
82	\small
83	\begin{tabular}{llr}
84	\toprule
85	\textbf{Condition} & \textbf{Seed(s)} & \textbf{Time (h)} \\
86	\midrule
87	no\_trace       & 42         & ${\sim}$0.5 \\
88	full\_trace     & 42         & ${\sim}$2.2 \\
89	label\_only     & 42         & ${\sim}$2.2 \\
90	VOTA                     & 42         & ${\sim}$2.3 \\
91	exception\_only & 42         & ${\sim}$2.1 \\
92	exception\_only & 123        & ${\sim}$2.1 \\
93	exception\_only & 456        & ${\sim}$1.3 \\
94	ae\_only        & 42         & ${\sim}$1.8 \\
95	loop\_only      & 42         & ${\sim}$2.1 \\
96	VOTA\_no\_ae    & 42         & ${\sim}$1.8 \\
97	\bottomrule
98	\end{tabular}
99	\end{table}
100	
101	%% ============================================================
102	\section{VOTA Trace Examples}
103	\label{sec:vota_examples}
104	
105	We provide two representative VOTA trace examples illustrating the fail and pass cases.
106	In the fail case, the exception event provides an unambiguous fault signal.
107	In the pass case, the absence of an exception event combined with a matching assertion point confirms correct execution.
108	
109	\paragraph{Fail example.}
110	A \texttt{ZeroDivisionError} triggers an \texttt{[ERROR]} event, providing a direct fault signal that is sufficient for the model to predict \texttt{fail}.
111	
112	\begin{small}
113	\begin{verbatim}
114	## Function
115	def divide(a, b):
116	    return a / b
117	
118	## Test Input
119	divide(1, 0)
120	
121	## Expected Output
122	inf
123	
124	## VOTA Trace
125	[ERROR] ZeroDivisionError: division by zero
126	
127	## Verdict
128	fail
129	\end{verbatim}
130	\end{small}
131	
132	\paragraph{Pass example.}
133	No exception is raised, and the assertion point confirms that the actual output matches the expected value.
134	
135	\begin{small}
136	\begin{verbatim}
137	## Function
138	def add(a, b):
139	    return a + b
140	
141	## Test Input
142	add(2, 3)
143	
144	## Expected Output
145	5
146	
147	## VOTA Trace
148	[LOOP] No loops detected.
149	[ASSERT] actual=5, expected=5
150	
151	## Verdict
152	pass
153	\end{verbatim}
154	\end{small}
155	
156	These examples illustrate the core asymmetry exploited by the \texttt{exception\_only} condition: fail cases produce an explicit \texttt{[ERROR]} event, while pass cases are characterized by its absence.
157	This binary signal (presence vs.\ absence of an exception) is sufficient for near-perfect verdict prediction.
158	
159	%% ============================================================
160	\section{Full Experimental Results}
161	\label{sec:full_results}
162	
163	Tables~\ref{tab:full_qwen} and \ref{tab:full_deepseek} report the complete experimental results across all conditions, models, and seeds.
164	
165	\begin{table}[t]
166	\centering
167	\caption{Full results for Qwen-2.5-Coder-7B across all conditions and seeds. Conditions with a single seed report no variance. \texttt{exception\_only} achieves 99.83\% across all three seeds ($\sigma{=}$0). \texttt{ae\_only} achieves 99.64\% mean ($\pm$0.49; seed 123 at 99.08\% is the outlier).}
168	\label{tab:full_qwen}
169	\small
170	\resizebox{\columnwidth}{!}{%
171	\begin{tabular}{lcccc}
172	\toprule
173	\textbf{Condition} & \textbf{S42} & \textbf{S123} & \textbf{S456} & \textbf{Mean $\pm$ Std} \\
174	\midrule
175	exception\_only & 99.83 & 99.83 & 99.83 & 99.83 $\pm$ 0.00 \\
176	ae\_only        & 99.92 & 99.08 & 99.92 & 99.64 $\pm$ 0.49 \\
177	VOTA                     & 99.41 & ---   & ---   & --- \\
178	VOTA\_no\_ae    & 99.41 & ---   & ---   & --- \\
179	label\_only     & 86.22 & ---   & ---   & --- \\
180	loop\_only      & 85.63 & ---   & ---   & --- \\
181	full\_trace     & 81.76 & ---   & ---   & --- \\
182	no\_trace       & 75.13 & ---   & ---   & --- \\
183	\bottomrule
184	\end{tabular}%
185	}
186	\end{table}
187	
188	\begin{table}[t]
189	\centering
190	\caption{Full results for DeepSeek-Coder-6.7B across all conditions and seeds. \texttt{exception\_only} shows bimodal seed behavior: seeds 42 and 456 achieve 99.33\%, while seed 123 yields 91.09\% (LoRA initialization outlier, fail recall = 70.5\%).}
191	\label{tab:full_deepseek}
192	\small
193	\resizebox{\columnwidth}{!}{%
194	\begin{tabular}{llcc}
195	\toprule
196	\textbf{Condition} & \textbf{Seed} & \textbf{Accuracy} & \textbf{Notes} \\
197	\midrule
198	exception\_only & 42  & 99.33 & epoch 1: 99.83 \\
199	exception\_only & 456 & 99.33 & CI [98.82, 99.75] \\
200	exception\_only & 123 & 91.09 & fail recall = 70.5\%; CI [89.40, 92.60] \\
201	\midrule
202	VOTA                     & 42  & 84.45 & \\
203	no\_trace       & 42  & 73.36 & \\
204	full\_trace     & 42  & 79.16 & CI [76.80, 81.30] \\
205	\bottomrule
206	\end{tabular}%
207	}
208	\end{table}
209	
210	%% ============================================================
211	\section{Tokenizer and Truncation Analysis}
212	\label{sec:tokenizer_analysis}
213	
214	The VOTA cross-model gap (14.96pp, Table~\ref{tab:cross_model}; confounded by tokenizer-driven truncation; 91.7\% of DeepSeek training samples were affected) is driven by a training-time truncation asymmetry.
215	The DeepSeek tokenizer averages 2{,}626 tokens per VOTA sample versus 1{,}929 for Qwen, causing 91.7\% of DeepSeek VOTA training samples to exceed the 2{,}048-token context window.
216	The training framework preserves the verdict label but truncates trace content, so the model trains with incomplete diagnostic information for the majority of samples.
217	
218	A post-hoc group analysis provides directional evidence: partitioning DeepSeek VOTA test samples by whether their training-set counterparts exceeded the context window, intact samples ($N{=}99$) achieve 100\% accuracy while truncated samples ($N{=}1{,}091$) achieve 83.04\% (95\% CI [80.75\%, 85.24\%]; Fisher exact $p{<}0.001$), with all 185 errors concentrated in the fail class (fail recall = 31.23\%).
219	Per-class analysis (Table~\ref{tab:per_class}) confirms that DeepSeek VOTA achieves 100\% fail precision but only 45.43\% fail recall, systematically defaulting to \texttt{pass}---in contrast to Qwen VOTA, which achieves 100\% fail recall.
220	
221	Seed robustness diverges across models: Qwen \texttt{exception\_only} produces identical 99.83\% across all three seeds ($\sigma{=}0$), while DeepSeek shows bimodal behavior: seeds 42 and 456 achieve 99.33\% (fail recall = 100\%), seed 123 yields 91.09\% (fail recall = 70.5\%).
222	Because \texttt{exception\_only} test inputs contain 48.99\% duplicates (607 unique of 1,190; \S\ref{sec:dataset}), CIs assume $n{=}1{,}190$ independent trials; under deduplication ($n{=}607$), Qwen's accuracy is 99.67\% (Wilson CI [98.81, 99.91]).
223	
224	%% ============================================================
225	\section{Irreducible Sample Analysis}
226	\label{sec:irreducible}
227	
228	The \texttt{exception\_only} condition with Qwen-2.5-Coder-7B misclassifies exactly 2 out of 1,190 test samples across all three seeds (42, 123, 456), with 100\% overlap across seeds.
229	Both samples (IDs 901 and 905) share the following characteristics:
230	
231	\begin{itemize}
232	\item \textbf{Function:} \texttt{check\_dict\_case} (HumanEval/95)---a function that checks whether all dictionary keys are uniformly upper-case or lower-case strings.
233	\item \textbf{Ground-truth label:} \texttt{pass}.
234	\item \textbf{Predicted label:} \texttt{fail} (false negative).
235	\item \textbf{Cross-seed consistency:} Both samples are misclassified identically by all three seeds, indicating a systematic rather than stochastic error.
236	\end{itemize}
237	
238	Manual inspection reveals the root cause: \texttt{check\_dict\_case} uses \texttt{all()} over a generator expression, and Python's \texttt{all()} short-circuits on the first \texttt{True} value, raising \texttt{GeneratorExit} to terminate the generator.
239	Because \texttt{GeneratorExit} is a \texttt{BaseException} subclass, the tracer records it as seven \texttt{[ERROR] GeneratorExit} lines---even though the function executes correctly and the test passes.
240	The model observes these spurious error markers and reasonably but incorrectly predicts \texttt{fail}.
241	This is not a model failure but a representation ambiguity: the \texttt{exception\_only} format cannot distinguish genuine exceptions from benign \texttt{BaseException} subclasses triggered by Python's iterator protocol.
242	
243	Most configurations converge to these same 2 errors: Qwen-1.5B, Qwen-7B (3 seeds), CodeLlama-13B (seeds 42/456), and DeepSeek-6.7B (seeds 42/456) all produce error set $\{901, 905\}$.
244	However, CodeLlama-13B seed 123 achieves 100\% accuracy (0/1190 errors), correctly classifying both samples.
245	This demonstrates that 99.83\% is a near-perfect \emph{floor} (the convergence attractor for most LoRA initializations) rather than a hard data ceiling: the representation supports perfect accuracy, but most initializations converge to the same 2-error basin.
246	The practical implication is that these errors are high-probability convergence artifacts addressable through seed selection or ensemble methods, not fundamental limitations of the exception-based representation.
247	
248	%% ============================================================
249	\section{Exception Type Accuracy Breakdown}
250	\label{sec:exception_type}
251	
252	Table~\ref{tab:exception_type} reports \texttt{exception\_only} accuracy stratified by exception type on Qwen-2.5-7B (seed=42, $N{=}1{,}190$).
253	All standard exception types (\texttt{TypeError}, \texttt{ValueError}, \texttt{IndexError}, etc.) achieve 100\% accuracy.
254	The only misclassifications arise from \texttt{GeneratorExit}, a \texttt{BaseException} subclass that is not an \texttt{Exception}---it is raised by Python's iterator protocol during generator short-circuiting, not by actual program errors.
255	
256	\begin{table}[t]
257	\centering
258	\caption{Exception type accuracy breakdown for \texttt{exception\_only} (Qwen-7B, seed=42). All true error types achieve 100\%. The only failures come from \texttt{GeneratorExit} (a \texttt{BaseException} subclass, not an \texttt{Exception}), which appears in 2 passing samples.}
259	\label{tab:exception_type}
260	\small
261	\begin{tabular}{lcc}
262	\toprule
263	\textbf{Exception Type} & \textbf{Samples} & \textbf{Accuracy} \\
264	\midrule
265	TypeError & 96 & 100\% \\
266	ValueError & 62 & 100\% \\
267	IndexError & 41 & 100\% \\
268	KeyError & 28 & 100\% \\
269	AttributeError & 19 & 100\% \\
270	AssertionError & 15 & 100\% \\
271	RecursionError & 12 & 100\% \\
272	Other Exception & 66 & 100\% \\
273	\midrule
274	GeneratorExit (BaseException) & 2 & 0\% \\
275	No exception (pass class) & 849 & 100\% \\
276	\bottomrule
277	\end{tabular}
278	\end{table}
279	
280	This confirms that the model has learned a clean decision boundary: any true \texttt{Exception} subclass in the trace implies failure.
281	The \texttt{GeneratorExit} case represents a semantic ambiguity in the trace format rather than a model failure, as discussed in \S\ref{sec:irreducible}.
282	
283	%% ============================================================
284	\section{Trace Length Ablation}
285	\label{sec:trace_length_full}
286	
287	To test whether the \texttt{full\_trace} performance gap is caused by input truncation at training time, we vary the maximum trace token budget on Qwen-2.5-7B (seed=42) while keeping all other hyperparameters fixed.
288	
289	\begin{table}[t]
290	\centering
291	\caption{Trace length and truncation direction ablation on Qwen-2.5-7B ($N{=}1{,}190$, seed=42). Head = standard left-truncation (retain first $k$ tokens); Tail = retain last $k$ tokens. Per-condition bootstrap 95\% CIs ($B{=}10{,}000$).}
292	\label{tab:trace_length}
293	\small
294	\begin{tabular}{llcc}
295	\toprule
296	\textbf{Direction} & \textbf{Max Tokens} & \textbf{Acc (\%)} & \textbf{95\% CI} \\
297	\midrule
298	Head & 256  & 78.82 & [76.4, 81.0] \\
299	Head & 512  & 80.42 & [78.2, 82.6] \\
300	Head & 1024 & 77.23 & [74.9, 79.6] \\
301	Head & no\_limit ($\infty$) & 81.76 & [79.7, 83.9] \\
302	\midrule
303	Tail & 256  & 77.48 & --- \\
304	Tail & 512  & 93.61 & --- \\
305	Tail & 1024 & 96.47 & --- \\
306	Tail & 2048 & 97.31 & --- \\
307	\bottomrule
308	\end{tabular}
309	\end{table}
310	
311	\begin{figure}[t]
312	\centering
313	\includegraphics[width=\columnwidth]{budget_curve}
314	\caption{Accuracy as a function of token budget and truncation direction (Qwen-2.5-7B, $N{=}1{,}190$). Tail-truncation (keeping last $k$ tokens) monotonically improves beyond 256 tokens and consistently outperforms head-truncation by 13--19pp at budgets ${\geq}$512. The flat head-truncation curve (77--82\%) contrasts with the steep tail-truncation rise, confirming that diagnostic signal is localized near trace end. Dashed lines show \texttt{exception\_only} (99.83\%) and \texttt{no\_trace} (75.13\%) as upper and lower bounds. Tail-256 (${\approx}$ \texttt{no\_trace}) indicates the signal window begins approximately 256 tokens from the trace terminus.}
315	\label{fig:trace_length}
316	\end{figure}
317	
318	As shown in Table~\ref{tab:trace_length} and Figure~\ref{fig:trace_length}, all four trace length conditions fall within a 5pp range (77.2\%--81.8\%).
319	To quantify the reliability of the observed differences, Table~\ref{tab:trace_length_pairwise} reports paired bootstrap comparisons ($B{=}10{,}000$, seed=42) across all condition pairs.
320	
321	\begin{table}[t]
322	\centering
323	\caption{Pairwise paired bootstrap comparisons for trace length ablation ($B{=}10{,}000$, seed=42). $\Delta$ = accuracy difference between the two conditions (first $-$ second in the budget group; condition $-$ baseline in the other groups). **$p{<}0.01$; ***$p{<}0.001$.}
324	\label{tab:trace_length_pairwise}
325	\small
326	\resizebox{\columnwidth}{!}{%
327	\begin{tabular}{llccc}
328	\toprule
329	& \textbf{Comparison} & \textbf{$\Delta$ (pp)} & \textbf{95\% CI} & \textbf{$p$-value} \\
330	\midrule
331	\multirow{4}{*}{\rotatebox{90}{\scriptsize Budget}}
332	& 512 vs.\ 256           & $+$1.60  & [$-$0.34, $+$3.53]   & 0.117 \\
333	& 1024 vs.\ 512          & $-$3.19  & [$-$5.29, $-$1.09]   & 0.002** \\
334	& no\_limit vs.\ 1024    & $+$4.54  & [$+$2.52, $+$6.55]   & ${<}$0.001*** \\
335	& no\_limit vs.\ 256     & $+$2.94  & [$+$0.84, $+$5.04]   & 0.006** \\
336	\midrule
337	\multirow{4}{*}{\rotatebox{90}{\scriptsize vs.\ no\_trace}}
338	& 256 $-$ no\_trace       & $+$3.70  & [$+$1.43, $+$6.05]   & 0.002** \\
339	& 512 $-$ no\_trace       & $+$5.29  & [$+$3.03, $+$7.56]   & ${<}$0.001*** \\
340	& 1024 $-$ no\_trace      & $+$2.10  & [$-$0.17, $+$4.37]   & 0.078 \\
341	& no\_limit $-$ no\_trace & $+$6.64  & [$+$4.37, $+$8.99]   & ${<}$0.001*** \\
342	\midrule
343	\multirow{4}{*}{\rotatebox{90}{\scriptsize vs.\ exc.}}
344	& 256 $-$ exc\_only       & $-$21.01 & [$-$23.45, $-$18.74] & ${<}$0.001*** \\
345	& 512 $-$ exc\_only       & $-$19.41 & [$-$21.76, $-$17.14] & ${<}$0.001*** \\
346	& 1024 $-$ exc\_only      & $-$22.61 & [$-$25.04, $-$20.25] & ${<}$0.001*** \\
347	& no\_limit $-$ exc\_only & $-$18.07 & [$-$20.34, $-$15.88] & ${<}$0.001*** \\
348	\bottomrule
349	\end{tabular}%
350	}
351	\end{table}
352	
353	\paragraph{Non-monotonic pattern.}
354	The trend across trace budgets is non-monotonic: 512 tokens (80.42\%) slightly outperforms 256 tokens (78.82\%), but doubling to 1024 tokens \emph{decreases} accuracy to 77.23\%---a statistically significant 3.19pp drop ($p{=}0.002$, 95\% CI [$-$5.29, $-$1.09]).
355	The no-limit condition (81.76\%) recovers and significantly exceeds 1024 tokens ($p{<}0.001$), but 1024 tokens is not significantly better than the \texttt{no\_trace} baseline (75.13\%; $\Delta{=}{+}2.10$pp, $p{=}0.078$, 95\% CI [$-$0.17, $+$4.37]).
356	This means that truncating traces to an intermediate length can be \emph{worse} than providing no trace at all---the 1024-token budget retains enough irrelevant content to mislead the model while discarding diagnostic events that might appear late in the trace.
357	
358	\paragraph{Comparison to baselines.}
359	All four trace budget conditions significantly exceed \texttt{no\_trace} except 1024 tokens ($p{=}0.078$), confirming that raw trace content provides some signal but unreliably so.
360	The gap to \texttt{exception\_only} (99.83\%) is massive for every budget condition (18--23pp, all $p{<}0.001$), underscoring that even unlimited raw traces cannot substitute for targeted signal extraction.
361	The best full-trace condition (no\_limit, 81.76\%) still lags \texttt{exception\_only} by 18.07pp (95\% CI [$-$20.34, $-$15.88]).
362	
363	\paragraph{Interpretation.}
364	These results rule out input truncation as the primary explanation for the full-trace performance gap: even with unlimited tokens, the model cannot extract the diagnostic signal that VOTA's targeted compression provides.
365	The non-monotonic dip at 1024 tokens is consistent with a ``worst-of-both-worlds'' regime where the model receives enough noisy context to dilute the signal but not enough to compensate through broader coverage.
366	The result reinforces the information density interpretation (\S\ref{sec:density}): the gap between full traces and VOTA is driven by the \emph{content} of the trace (irrelevant lines diluting the diagnostic signal), not its \emph{length}.
367	In contrast, VOTA's compressed representation concentrates the diagnostic signal into fewer tokens, making it sensitive to truncation when those tokens are removed (\S\ref{sec:cross_model}).
368	
369	\paragraph{Truncation direction.}
370	Tail-truncation (retaining the last $k$ tokens) dramatically outperforms head-truncation: \texttt{tail\_2048} achieves 97.31\% vs.\ \texttt{head\_2048} (no\_limit) at 81.76\%, a 15.55pp improvement.
371	Even \texttt{tail\_512} (93.61\%) exceeds every head-truncation condition by over 11pp.
372	
373	However, \texttt{tail\_256} (77.48\%) performs at the \texttt{no\_trace} baseline level (75.13\%), indicating that the diagnostic signal does not reside in the very last trace lines.
374	The critical jump occurs between 256 and 512 tail tokens (+16.13pp), localizing the signal window to approximately 256--512 tokens from the trace terminus.
375	This is consistent with Python's execution model: exception tracebacks and assertion comparisons appear near the end of the trace but are preceded by the final function call frames, placing them typically 300--500 tokens from the terminus rather than at the absolute end.
376	
377	The 18.07pp gap from \texttt{full\_trace} to \texttt{exception\_only} decomposes as: 86\% positional concentration (recovered by tail-truncation at 2048 tokens) and 14\% residual content noise (the 2.52pp gap from \texttt{tail\_2048} to \texttt{exception\_only} that persists regardless of truncation direction).
378	The fact that \texttt{exception\_only} (99.83\%) still outperforms \texttt{tail\_2048} (97.31\%) confirms that semantic extraction (identifying the exception type and message) is superior to positional extraction (keeping a fixed window), because the model need not filter out non-diagnostic lines that happen to fall within the window.
379	
380	\paragraph{Cross-model tail-truncation verification.}
381	Table~\ref{tab:tail_cross_model} extends the tail-2048 analysis to two additional models.
382	The positional concentration pattern generalizes: all three models achieve 94.96--97.90\% with \texttt{tail\_2048}, leaving residual gaps of only 1.93--4.37pp to \texttt{exception\_only}.
383	DeepSeek-6.7B shows the largest residual (4.37pp), consistent with its known sensitivity to long-context formatting (Appendix~\ref{sec:training_dynamics}); the diagnostic signal is present in the tail window but partially degraded by the model's weaker long-context processing.
384	Qwen-1.5B (97.90\%) performs comparably to Qwen-7B (97.31\%), confirming that positional signal extraction, like exception-based extraction, is signal-limited rather than capacity-limited.
385	
386	\begin{table}[t]
387	\centering
388	\caption{Cross-model \texttt{tail\_2048} verification ($N{=}1{,}190$). Positional concentration of diagnostic signal holds across all tested models and architecture families.}
389	\label{tab:tail_cross_model}
390	\small
391	\begin{tabular}{lccc}
392	\toprule
393	\textbf{Model} & \textbf{Tail-2048 (\%)} & \textbf{exc\_only (\%)} & \textbf{Gap (pp)} \\
394	\midrule
395	Qwen-7B & 97.31 & 99.83 & 2.52 \\
396	Qwen-1.5B & 97.90 & 99.83 & 1.93 \\
397	DeepSeek-6.7B & 94.96 & 99.33 & 4.37 \\
398	\bottomrule
399	\end{tabular}
400	\end{table}
401	
402	%% ============================================================
403	\section{Calibration Analysis}
404	\label{sec:calibration_full}
405	
406	Beyond accuracy, we evaluate whether trace conditions affect prediction calibration, motivated by recent findings that code LLM confidence is often poorly calibrated \citep{spiess2025calibration}.
407	
408	\begin{table}[t]
409	\centering
410	\caption{Calibration metrics on Qwen-2.5-7B ($N{=}1{,}190$, seed=42). ECE = expected calibration error; Brier = Brier score. Lower is better for both.}
411	\label{tab:calibration}
412	\small
413	\begin{tabular}{lcc}
414	\toprule
415	\textbf{Condition} & \textbf{ECE $\downarrow$} & \textbf{Brier $\downarrow$} \\
416	\midrule
417	ae\_only & \textbf{0.0004} & \textbf{0.0008} \\
418	exception\_only & 0.0027 & 0.0013 \\
419	VOTA & 0.0054 & 0.005 \\
420	full\_trace & 0.096 & 0.144 \\
421	no\_trace & 0.171 & 0.197 \\
422	\bottomrule
423	\end{tabular}
424	\end{table}
425	
426	Table~\ref{tab:calibration} shows that calibration quality mirrors the Tier~1/2 hierarchy.
427	Tier~1 conditions (\texttt{ae\_only}: ECE=0.0004; \texttt{exception\_only}: ECE=0.0027) produce near-perfectly calibrated predictions, while \texttt{full\_trace} (ECE=0.096) and \texttt{no\_trace} (ECE=0.171) exhibit substantial miscalibration.
428	VOTA (ECE=0.0054) is well-calibrated but slightly worse than either Tier~1 component alone, reinforcing the pattern that combining trace signals dilutes rather than improves the prediction signal.
429	
430	The Brier scores tell a consistent story: \texttt{ae\_only} (0.0008) and \texttt{exception\_only} (0.0013) achieve near-zero scores, while \texttt{no\_trace} (0.197) indicates substantial miscalibration.
431	
432	\begin{figure}[t]
433	\centering
434	\includegraphics[width=\columnwidth]{fig2_calibration}
435	\caption{Reliability diagrams for four trace conditions on Qwen-2.5-7B ($N{=}1{,}190$, seed=42). \texttt{exception\_only} (ECE=0.0027) clusters near the diagonal, while \texttt{no\_trace} (ECE=0.171) exhibits systematic overconfidence, a 63$\times$ gap.}
436	\label{fig:calibration}
437	\end{figure}
438	
439	%% ============================================================
440	\section{Error Overlap Analysis}
441	\label{sec:error_overlap}
442	
443	We analyze the overlap between error sets of different conditions to determine whether they fail on the same samples (Figure~\ref{fig:error_overlap}).
444	
445	\texttt{exception\_only}'s 2 errors (samples 901 and 905) have zero intersection with the error sets of all other conditions (Jaccard = 0.000 in all pairwise comparisons).
446	This orthogonality arises because \texttt{exception\_only} errors are caused by \texttt{GeneratorExit} false positives (pass samples misclassified as fail due to benign \texttt{BaseException} events), while errors from other conditions are predominantly fail samples misclassified as pass due to insufficient signal.
447	
448	Among non-exception conditions, error sets exhibit hierarchical containment: \texttt{ae\_only} $\subset$ VOTA $\subset$ \texttt{loop\_only} $\subset$ \texttt{no\_trace}, with pairwise Jaccard indices increasing with signal overlap.
449	\texttt{loop\_only} and \texttt{full\_trace} share the highest overlap (Jaccard ${\sim}$0.65), reflecting their shared reliance on behavioral patterns rather than explicit fault indicators.
450	
451	This analysis confirms that \texttt{exception\_only} operates on an independent signal dimension: its errors are representation ambiguities (iterator protocol artifacts) rather than information deficits, explaining why combining it with other signals cannot eliminate these specific errors.
452	
453	\begin{figure}[t]
454	\centering
455	\includegraphics[width=\columnwidth]{error_overlap}
456	\caption{Jaccard similarity between error sets of different conditions (Qwen-7B, seed=42, $N{=}1{,}190$). \texttt{exception\_only} (exc\_only) has zero overlap with all other conditions, confirming it operates on an independent signal dimension.}
457	\label{fig:error_overlap}
458	\end{figure}
459	
460	%% ============================================================
461	\section{Cross-Dataset Generalization: DebugBench}
462	\label{sec:debugbench_full}
463	
464	To test whether exception-based verdict prediction generalizes beyond LLM-generated solutions, we evaluate on DebugBench \citep{tian2024debugbench}---a dataset of human-written programs with synthetically injected bugs (single-point mutations such as operator replacement, variable misuse, and missing statements).
465	After filtering for executable Python samples with valid traces, we retain 426 samples with a near-balanced class distribution (majority baseline: 51.4\%).
466	
467	\begin{table}[t]
468	\centering
469	\caption{Generalization to DebugBench ($N{=}426$, Qwen-2.5-7B, seed=42). Wilson 95\% CIs. The component ranking (exception\_only $\geq$ VOTA $>$ no\_trace) is preserved, and exception\_only achieves perfect accuracy.}
470	\label{tab:debugbench}
471	\small
472	\begin{tabular}{lcc}
473	\toprule
474	\textbf{Condition} & \textbf{Acc (\%)} & \textbf{95\% CI} \\
475	\midrule
476	exception\_only & \textbf{100.00} & [99.14, 100.00] \\
477	VOTA & 99.77 & [99.30, 100.00] \\
478	no\_trace & 96.71 & [94.80, 98.40] \\
479	\midrule
480	Majority baseline & 51.41 & --- \\
481	\bottomrule
482	\end{tabular}
483	\end{table}
484	
485	Table~\ref{tab:debugbench} shows that the component ranking from the main experiments is preserved: \texttt{exception\_only} (100.00\%) $\geq$ VOTA (99.77\%) $>$ \texttt{no\_trace} (96.71\%).
486	The \texttt{exception\_only} condition achieves perfect accuracy, confirming that the exception-based representation generalizes to a different fault distribution without degradation.
487	
488	The absolute margins are much narrower than on the main dataset: the \texttt{no\_trace} baseline already achieves 96.71\%---compared to 75.13\% on HumanEval+MBPP---leaving only 3.29pp of headroom for trace-based improvement.
489	This ceiling effect reflects a fundamental difference in fault characteristics: DebugBench bugs are synthetically injected single-point mutations, which produce code that is structurally dissimilar from the original correct solution; a model can often identify the fault from source code alone.
490	In contrast, the HumanEval+MBPP solutions are LLM-generated, producing natural errors (logic mistakes, edge-case failures) where the faulty and correct solutions may be structurally similar, making code-only verdict prediction substantially harder.
491	
492	These results support exception-based verdict prediction as a generalizable approach---the method does not degrade on an out-of-distribution dataset, and the exception dominance ranking (exception\_only $\geq$ VOTA $>$ no\_trace) is consistent across both datasets---but the narrow DebugBench margins are insufficient to independently validate trace importance.
493	The 24.70pp trace lift on the main dataset (no\_trace 75.13\% $\to$ exception\_only 99.83\%) remains the primary evidence for the value of exception-based trace signals.
494	
495	%% ============================================================
496	\section{Cross-Model Robustness Analysis}
497	\label{sec:robustness_analysis}
498	
499	The cross-model gap pattern (Table~\ref{tab:cross_model}) suggests a design principle: \emph{trace representations should match the model capability floor, not the ceiling.}
500	Exception events are consistently the most effective component on both models, and their structural simplicity---a fixed-format error message---ensures that the relative advantage over richer representations holds across all seeds.
501	Two of three DeepSeek seeds match Qwen-level accuracy (99.33\%); the outlier (seed 123, 91.09\%) we hypothesize reflects LoRA initialization sensitivity landing in a suboptimal basin (fail recall = 70.5\%, though direct evidence is lacking), not a failure of the exception signal itself---even this outlier outperforms VOTA (84.45\%) by 6.64pp.
502	The VOTA cross-model gap is confounded by two factors: (1)~tokenizer efficiency---the DeepSeek tokenizer averages 2{,}626 tokens per VOTA sample versus Qwen's 1{,}929, causing 91.7\% of training samples to exceed the 2{,}048-token context window; content-aware truncation preferentially removes the terminal structured prompt, preserving the verdict label but truncating trace content---and (2)~base model capability differences, consistent with findings that SFT generalization depends on pretrain quality \citep{yang2024generalization}.
503	The two factors cannot be disentangled in the current experimental design.
504	Our \texttt{exception\_only} design sidesteps the truncation confound entirely: inputs have a median of 150 tokens (mean 398), well below the 2{,}048-token context window, so no training samples are truncated on either model.
505	The resulting 0.56pp cross-model gap (Table~\ref{tab:cross_model}) is therefore a clean measure of model capability differences, making the ``capability floor'' principle directly testable.
506	The practical implication is that trace-based systems should default to the simplest sufficient signal; for smaller models, training stability (multi-seed selection, warmup schedules) is a secondary but addressable concern.
507	
508	%% ============================================================
509	\section{Training Dynamics and Loss Decoupling}
510	\label{sec:training_dynamics}
511	
512	The DeepSeek \texttt{exception\_only} results reveal two instructive training dynamics.
513	First, epoch-level analysis shows mild degradation in 2/3 seeds: seed 42 peaks at 99.83\% after epoch~1 but settles at 99.33\% by epoch~3 ($-$0.50pp), seed 123 degrades from 91.43\% to 91.09\% ($-$0.34pp), while seed 456 shows no epoch degradation (99.33\% at both epoch~1 and epoch~3).
514	Early stopping may yield marginal gains for some seeds, but the epoch effect is small (${\leq}$0.5pp) compared to the seed effect (8.24pp between seeds 42 and 123).
515	
516	Second, seeds 123 and 456 converge to nearly identical final training losses (0.122 and 0.123 respectively), yet their accuracies differ by 8.24pp (91.09\% vs.\ 99.33\%).
517	The critical difference lies in fail recall: seeds 42 and 456 achieve 100\%, while seed 123 achieves only 70.5\%---the LoRA initialization in seed 123 fails to learn the exception$\to$fail mapping for a substantial fraction of failing samples, even though the per-token loss appears converged.
518	This demonstrates that token-level training loss can mask fundamental differences in sample-level classification ability, suggesting a parallel to the eval-loss/accuracy decoupling observed in DeepSeek VOTA (where eval loss rose 65\% from epoch 1 to 3 while accuracy improved by 6.3pp) at the training phase.
519	The practical recommendation is twofold: (1)~use task-specific metrics (accuracy, fail recall) for checkpoint and seed selection rather than training or evaluation loss, and (2)~for deployment on smaller models, train multiple seeds and select the best, as a single run may not reliably converge to the correct classification boundary.
520	
521	\paragraph{Format collapse, not semantic failure.}
522	The 100 errors of seed 123 are not semantic failures but generation format collapse: on inputs exceeding 4,000 characters (those containing verbose locals dumps), the model echoes trace content instead of emitting a verdict token, while achieving zero errors on shorter inputs.
523	This indicates that the LoRA initialization of seed 123 specifically compromises long-context format compliance rather than exception signal comprehension, further supporting the robustness advantage of compact \texttt{exception\_only} inputs.
524	
525	The contrast with VOTA is instructive: DeepSeek VOTA accuracy monotonically increases from 78.15\% to 84.45\% across epochs, but is consistent with a performance limit associated with the high trace truncation rate (\S\ref{sec:cross_model})---the model progressively extracts signal from samples with intact trace content but cannot fully compensate for the information loss in the truncated majority.
526	The 84.45\% accuracy reflects a combination of trace information loss and model capability constraints.
527	
528	%% ============================================================
529	\section{Deduplication Statistics}
530	\label{sec:dedup_stats}
531	
532	Table~\ref{tab:dedup} reports the duplication rates across trace formats.
533	Because multiple passing solutions to the same problem produce identical (input, output) pairs in the \texttt{exception\_only} format---correct executions raise no exceptions, so the trace content is the same regardless of the solution's internal logic---the dataset contains duplicate rows.
534	Train--test input overlap is zero (split by problem ID), so no information leakage occurs.
535	The high duplication in \texttt{exception\_only} does not affect our experimental conclusions: after deduplication the training set still contains 2,858 unique samples and the test set 607, providing sufficient coverage for the 591-problem benchmark.
536	The \texttt{exception\_only} test set contains 48.99\% duplicate inputs due to representation compactness; all confidence intervals treat samples as independent Bernoulli trials.
537	
538	\begin{table}[t]
539	\centering
540	\caption{Deduplication statistics. The \texttt{exception\_only} format collapses multiple passing solutions into identical rows because correct executions produce no exception events. Train--test input overlap is 0 (no leakage).}
541	\label{tab:dedup}
542	\small
543	\begin{tabular}{lccc}
544	\toprule
545	\textbf{Split} & \textbf{Total} & \textbf{Unique} & \textbf{Dup.\ rate} \\
546	\midrule
547	exception\_only train & 4{,}720 & 2{,}858 & 39.45\% \\
548	exception\_only test  & 1{,}190 &   607 & 48.99\% \\
549	raw\_traces (full)    & 5{,}910 & 5{,}803 &  1.81\% \\
550	\bottomrule
551	\end{tabular}
552	\end{table}
553	
554	%% ============================================================
555	\section{Regex Baseline Analysis}
556	\label{sec:regex_baselines}
557	
558	To establish a non-learning upper bound, we evaluate six regex-based baselines on the \texttt{exception\_only} test set ($N{=}1{,}190$) and two format-specific baselines on VOTA and \texttt{full\_trace} inputs.
559	
560	\begin{table}[t]
561	\centering
562	\caption{Regex baseline accuracy ($N{=}1{,}190$). B4 is the strongest semantic baseline (6.22pp below SFT \texttt{exception\_only}, McNemar $p{<}0.001$). B6 uses an error count threshold. $^\ddag$B5 exploits a data formatting artifact: the \texttt{[No exception data in trace]} marker is deterministically present in all pass samples, making this a format-level shortcut rather than a genuine exception-based heuristic.}
563	\label{tab:regex}
564	\small
565	\begin{tabular}{llc}
566	\toprule
567	\textbf{Baseline} & \textbf{Method} & \textbf{Acc (\%)} \\
568	\midrule
569	B1: \texttt{[ERROR]} presence & string match & 93.45 \\
570	B2: Traceback presence & string match & 71.51 \\
571	B3: Any keyword & union of B1+B2+Exception & 93.45 \\
572	B4: Exception type regex & regex on exception class names & \textbf{93.61} \\
573	B5: Format marker & \texttt{[No exception data]} $\to$ pass & 99.33$^\ddag$ \\
574	B6: Error count $\geq$2 & count threshold & 92.02 \\
575	\midrule
576	VOTA format regex & best regex on VOTA traces & 75.55 \\
577	full\_trace format regex & best regex on full traces & 77.39 \\
578	\bottomrule
579	\end{tabular}
580	\end{table}
581	
582	The strongest legitimate baseline (B4, 93.61\%) applies regex pattern-matching on Python exception class names (e.g., \texttt{ValueError}, \texttt{TypeError}).
583	Its errors concentrate on 8 boundary samples where a \texttt{ValueError} is raised inside a \texttt{try/except} block and caught---the program passes despite an exception occurring in the trace.
584	SFT \texttt{exception\_only} correctly classifies 6 of these 8 samples, indicating that the model learns the semantic distinction between caught (benign) and uncaught (fault-indicating) exceptions.
585	B5 (99.33\%) achieves near-SFT accuracy but relies on the deterministic presence of a format marker in pass-class traces, which is an artifact of the trace preprocessing pipeline rather than a generalizable signal; McNemar test vs.\ SFT yields $p{=}0.041$, confirming a statistically significant difference.
586	
587	\paragraph{Cross-format comparison.}
588	Table~\ref{tab:regex_cross_format} compares SFT and the best applicable regex baseline for each trace format.
589	The SFT advantage increases with format complexity: \texttt{no\_trace} (+3.62pp over majority baseline) $<$ \texttt{full\_trace} (+4.37pp) $<$ \texttt{exception\_only} (+6.22pp) $\ll$ VOTA (+23.86pp).
590	The VOTA gap is largest because its structured multi-component format carries semantic content that regex cannot parse, while \texttt{exception\_only}'s simpler format allows regex to capture most of the signal.
591	
592	\begin{table}[t]
593	\centering
594	\caption{SFT vs.\ best regex baseline by trace format ($N{=}1{,}190$). Regex baselines: majority class for \texttt{no\_trace}, keyword matching for \texttt{full\_trace}, pattern matching for VOTA, exception type regex (B4) for \texttt{exception\_only}.}
595	\label{tab:regex_cross_format}
596	\small
597	\begin{tabular}{lccc}
598	\toprule
599	\textbf{Format} & \textbf{SFT (\%)} & \textbf{Regex (\%)} & \textbf{$\Delta$ (pp)} \\
600	\midrule
601	exception\_only & 99.83 & 93.61 & +6.22 \\
602	VOTA & 99.41 & 75.55 & +23.86 \\
603	full\_trace & 81.76 & 77.39 & +4.37 \\
604	no\_trace & 75.13 & 71.51 & +3.62 \\
605	\bottomrule
606	\end{tabular}
607	\end{table}
608	
609	%% ============================================================
610	\section{Cross-Model Zero-Shot Comparison}
611	\label{sec:zeroshot_cross_model}
612	
613	Table~\ref{tab:zeroshot_cross_model} compares zero-shot and SFT \texttt{exception\_only} accuracy across four models.
614	Zero-shot performance does not correlate with model size: the smallest model (Qwen-1.5B, 93.45\%) outperforms all larger models, while the largest (CodeLlama-13B) falls below majority baseline.
615	SFT compresses the 42.44pp zero-shot range to 0.56pp, eliminating architecture-dependent variance.
616	
617	\begin{table}[t]
618	\centering
619	\caption{Zero-shot vs.\ SFT \texttt{exception\_only} across four models ($N{=}1{,}190$). Zero-shot accuracy is uncorrelated with model size; SFT normalizes cross-architecture variance from 42.44pp to 0.56pp.}
620	\label{tab:zeroshot_cross_model}
621	\small
622	\begin{tabular}{llccc}
623	\toprule
624	\textbf{Model} & \textbf{Size} & \textbf{Zero-shot (\%)} & \textbf{SFT (\%)} & \textbf{$\Delta$ (pp)} \\
625	\midrule
626	Qwen-1.5B & 1.5B & 93.45 & 99.83 & +6.38 \\
627	DeepSeek-6.7B & 6.7B & 90.59 & 99.33 & +8.74 \\
628	Qwen-7B & 7B & 89.08 & 99.83 & +10.75 \\
629	CodeLlama-13B & 13B & 51.01 & 99.89 & +48.88 \\
630	\midrule
631	Range & --- & 42.44pp & 0.56pp & --- \\
632	\bottomrule
633	\end{tabular}
634	\end{table}
635	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8fc5a144-20f7-4071-9749-04274da87881",
  "isSidechain": false,
  "promptId": "b73967ab-1e3d-4502-97ef-ede23a2a2cd7",
  "type": "user",
  "uuid": "7c460b27-702f-4d6d-9d0a-fd7e39151e81",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/appendix.tex",
      "content": "\\section{Per-Class Performance Breakdown}\n\\label{sec:per_class}\n\nTable~\\ref{tab:per_class} reports per-class precision, recall, and F1 for all experimental conditions.\n\n\\begin{table*}[t]\n\\centering\n\\caption{Per-class precision, recall, and F1 for all experimental conditions (seed 42). DeepSeek VOTA achieves 100\\% fail precision but only 45.4\\% fail recall, indicating systematic bias toward predicting \\texttt{pass}. DeepSeek \\texttt{exception\\_only} seed 42 achieves 100\\% fail recall, but seed 123 drops to 70.5\\% (see Table~\\ref{tab:full_deepseek}).}\n\\label{tab:per_class}\n\\small\n\\begin{tabular}{llccccccc}\n\\toprule\n\\textbf{Condition} & \\textbf{Model} & \\textbf{Acc} & \\textbf{Pass P} & \\textbf{Pass R} & \\textbf{Pass F1} & \\textbf{Fail P} & \\textbf{Fail R} & \\textbf{Fail F1} \\\\\n\\midrule\nNo Trace          & Qwen-2.5-7B & 75.13 & 87.76 & 75.79 & 81.34 & 54.73 & 73.45 & 62.72 \\\\\nFull Trace        & Qwen-2.5-7B & 81.76 & 87.74 & 86.60 & 87.17 & 67.43 & 69.62 & 68.51 \\\\\nFull Trace (LO)   & Qwen-2.5-7B & 86.22 & 88.21 & 93.18 & 90.63 & 80.07 & 68.73 & 73.97 \\\\\nVOTA              & Qwen-2.5-7B & 99.41 & 100.00 & 99.18 & 99.59 & 97.98 & 100.00 & 98.98 \\\\\nException Only    & Qwen-2.5-7B & 99.83 & 100.00 & 99.76 & 99.88 & 99.41 & 100.00 & 99.71 \\\\\nAE Only           & Qwen-2.5-7B & 99.92 & 100.00 & 99.88 & 99.94 & 99.71 & 100.00 & 99.85 \\\\\nLoop Only         & Qwen-2.5-7B & 85.63 & 92.39 & 87.07 & 89.66 & 71.65 & 82.01 & 76.48 \\\\\nVOTA\\_no\\_ae       & Qwen-2.5-7B & 99.41 & 99.88 & 99.29 & 99.59 & 98.26 & 99.71 & 98.98 \\\\\n\\midrule\nNo Trace          & DeepSeek-6.7B & 73.36 & 81.71 & 80.85 & 81.28 & 53.16 & 54.57 & 53.86 \\\\\nFull Trace        & DeepSeek-6.7B & 79.16 & 85.70 & 85.10 & 85.40 & 63.20 & 64.30 & 63.70 \\\\\nVOTA              & DeepSeek-6.7B & 84.45 & 82.14 & 100.00 & 90.20 & 100.00 & 45.40 & 62.50 \\\\\nException Only    & DeepSeek-6.7B & 99.33 & 100.00 & 99.06 & 99.53 & 97.69 & 100.00 & 98.83 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table*}\n\n%% ============================================================\n\\section{Training Details}\n\\label{sec:training_details}\n\nTable~\\ref{tab:hyperparams} summarizes the training hyperparameters shared across all conditions.\nAll experiments use the HuggingFace TRL \\texttt{SFTTrainer} with LoRA \\citep{hu2022lora} applied to all linear layers.\n\n\\begin{table}[t]\n\\centering\n\\caption{Training hyperparameters (shared across all conditions).}\n\\label{tab:hyperparams}\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{ll}\n\\toprule\n\\textbf{Hyperparameter} & \\textbf{Value} \\\\\n\\midrule\nLoRA rank ($r$)            & 16 \\\\\nLoRA alpha ($\\alpha$)      & 32 \\\\\nLoRA dropout               & 0.05 \\\\\nLoRA target modules        & all linear layers \\\\\n\\midrule\nEpochs                     & 3 \\\\\nPer-device batch size       & 4 \\\\\nGradient accumulation steps & 8 \\\\\nEffective batch size        & 32 \\\\\n\\midrule\nLearning rate               & $2 \\times 10^{-4}$ \\\\\nLR scheduler                & linear decay \\\\\nWarmup ratio                & 0.1 \\\\\nWeight decay                & 0.01 \\\\\n\\midrule\nMax sequence length         & 2048 tokens \\\\\nPrimary seed                & 42 \\\\\nRobustness seeds            & 123, 456 \\\\\n\\midrule\nHardware                    & 1$\\times$ RTX PRO 6000 Blackwell (96\\,GB VRAM) \\\\\nFramework                   & HuggingFace TRL SFTTrainer \\\\\n\\bottomrule\n\\end{tabular}%\n}\n\\end{table}\n\nTable~\\ref{tab:train_time} reports per-condition training wall-clock times.\nConditions with longer trace inputs (e.g., \\texttt{full\\_trace}, VOTA) require proportionally more training time due to increased sequence lengths.\n\n\\begin{table}[t]\n\\centering\n\\caption{Training wall-clock time per condition on a single RTX PRO 6000 Blackwell GPU. Where multiple seeds were run, individual times are listed.}\n\\label{tab:train_time}\n\\small\n\\begin{tabular}{llr}\n\\toprule\n\\textbf{Condition} & \\textbf{Seed(s)} & \\textbf{Time (h)} \\\\\n\\midrule\nno\\_trace       & 42         & ${\\sim}$0.5 \\\\\nfull\\_trace     & 42         & ${\\sim}$2.2 \\\\\nlabel\\_only     & 42         & ${\\sim}$2.2 \\\\\nVOTA                     & 42         & ${\\sim}$2.3 \\\\\nexception\\_only & 42         & ${\\sim}$2.1 \\\\\nexception\\_only & 123        & ${\\sim}$2.1 \\\\\nexception\\_only & 456        & ${\\sim}$1.3 \\\\\nae\\_only        & 42         & ${\\sim}$1.8 \\\\\nloop\\_only      & 42         & ${\\sim}$2.1 \\\\\nVOTA\\_no\\_ae    & 42         & ${\\sim}$1.8 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n%% ============================================================\n\\section{VOTA Trace Examples}\n\\label{sec:vota_examples}\n\nWe provide two representative VOTA trace examples illustrating the fail and pass cases.\nIn the fail case, the exception event provides an unambiguous fault signal.\nIn the pass case, the absence of an exception event combined with a matching assertion point confirms correct execution.\n\n\\paragraph{Fail example.}\nA \\texttt{ZeroDivisionError} triggers an \\texttt{[ERROR]} event, providing a direct fault signal that is sufficient for the model to predict \\texttt{fail}.\n\n\\begin{small}\n\\begin{verbatim}\n## Function\ndef divide(a, b):\n    return a / b\n\n## Test Input\ndivide(1, 0)\n\n## Expected Output\ninf\n\n## VOTA Trace\n[ERROR] ZeroDivisionError: division by zero\n\n## Verdict\nfail\n\\end{verbatim}\n\\end{small}\n\n\\paragraph{Pass example.}\nNo exception is raised, and the assertion point confirms that the actual output matches the expected value.\n\n\\begin{small}\n\\begin{verbatim}\n## Function\ndef add(a, b):\n    return a + b\n\n## Test Input\nadd(2, 3)\n\n## Expected Output\n5\n\n## VOTA Trace\n[LOOP] No loops detected.\n[ASSERT] actual=5, expected=5\n\n## Verdict\npass\n\\end{verbatim}\n\\end{small}\n\nThese examples illustrate the core asymmetry exploited by the \\texttt{exception\\_only} condition: fail cases produce an explicit \\texttt{[ERROR]} event, while pass cases are characterized by its absence.\nThis binary signal (presence vs.\\ absence of an exception) is sufficient for near-perfect verdict prediction.\n\n%% ============================================================\n\\section{Full Experimental Results}\n\\label{sec:full_results}\n\nTables~\\ref{tab:full_qwen} and \\ref{tab:full_deepseek} report the complete experimental results across all conditions, models, and seeds.\n\n\\begin{table}[t]\n\\centering\n\\caption{Full results for Qwen-2.5-Coder-7B across all conditions and seeds. Conditions with a single seed report no variance. \\texttt{exception\\_only} achieves 99.83\\% across all three seeds ($\\sigma{=}$0). \\texttt{ae\\_only} achieves 99.64\\% mean ($\\pm$0.49; seed 123 at 99.08\\% is the outlier).}\n\\label{tab:full_qwen}\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Condition} & \\textbf{S42} & \\textbf{S123} & \\textbf{S456} & \\textbf{Mean $\\pm$ Std} \\\\\n\\midrule\nexception\\_only & 99.83 & 99.83 & 99.83 & 99.83 $\\pm$ 0.00 \\\\\nae\\_only        & 99.92 & 99.08 & 99.92 & 99.64 $\\pm$ 0.49 \\\\\nVOTA                     & 99.41 & ---   & ---   & --- \\\\\nVOTA\\_no\\_ae    & 99.41 & ---   & ---   & --- \\\\\nlabel\\_only     & 86.22 & ---   & ---   & --- \\\\\nloop\\_only      & 85.63 & ---   & ---   & --- \\\\\nfull\\_trace     & 81.76 & ---   & ---   & --- \\\\\nno\\_trace       & 75.13 & ---   & ---   & --- \\\\\n\\bottomrule\n\\end{tabular}%\n}\n\\end{table}\n\n\\begin{table}[t]\n\\centering\n\\caption{Full results for DeepSeek-Coder-6.7B across all conditions and seeds. \\texttt{exception\\_only} shows bimodal seed behavior: seeds 42 and 456 achieve 99.33\\%, while seed 123 yields 91.09\\% (LoRA initialization outlier, fail recall = 70.5\\%).}\n\\label{tab:full_deepseek}\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llcc}\n\\toprule\n\\textbf{Condition} & \\textbf{Seed} & \\textbf{Accuracy} & \\textbf{Notes} \\\\\n\\midrule\nexception\\_only & 42  & 99.33 & epoch 1: 99.83 \\\\\nexception\\_only & 456 & 99.33 & CI [98.82, 99.75] \\\\\nexception\\_only & 123 & 91.09 & fail recall = 70.5\\%; CI [89.40, 92.60] \\\\\n\\midrule\nVOTA                     & 42  & 84.45 & \\\\\nno\\_trace       & 42  & 73.36 & \\\\\nfull\\_trace     & 42  & 79.16 & CI [76.80, 81.30] \\\\\n\\bottomrule\n\\end{tabular}%\n}\n\\end{table}\n\n%% ============================================================\n\\section{Tokenizer and Truncation Analysis}\n\\label{sec:tokenizer_analysis}\n\nThe VOTA cross-model gap (14.96pp, Table~\\ref{tab:cross_model}; confounded by tokenizer-driven truncation; 91.7\\% of DeepSeek training samples were affected) is driven by a training-time truncation asymmetry.\nThe DeepSeek tokenizer averages 2{,}626 tokens per VOTA sample versus 1{,}929 for Qwen, causing 91.7\\% of DeepSeek VOTA training samples to exceed the 2{,}048-token context window.\nThe training framework preserves the verdict label but truncates trace content, so the model trains with incomplete diagnostic information for the majority of samples.\n\nA post-hoc group analysis provides directional evidence: partitioning DeepSeek VOTA test samples by whether their training-set counterparts exceeded the context window, intact samples ($N{=}99$) achieve 100\\% accuracy while truncated samples ($N{=}1{,}091$) achieve 83.04\\% (95\\% CI [80.75\\%, 85.24\\%]; Fisher exact $p{<}0.001$), with all 185 errors concentrated in the fail class (fail recall = 31.23\\%).\nPer-class analysis (Table~\\ref{tab:per_class}) confirms that DeepSeek VOTA achieves 100\\% fail precision but only 45.43\\% fail recall, systematically defaulting to \\texttt{pass}---in contrast to Qwen VOTA, which achieves 100\\% fail recall.\n\nSeed robustness diverges across models: Qwen \\texttt{exception\\_only} produces identical 99.83\\% across all three seeds ($\\sigma{=}0$), while DeepSeek shows bimodal behavior: seeds 42 and 456 achieve 99.33\\% (fail recall = 100\\%), seed 123 yields 91.09\\% (fail recall = 70.5\\%).\nBecause \\texttt{exception\\_only} test inputs contain 48.99\\% duplicates (607 unique of 1,190; \\S\\ref{sec:dataset}), CIs assume $n{=}1{,}190$ independent trials; under deduplication ($n{=}607$), Qwen's accuracy is 99.67\\% (Wilson CI [98.81, 99.91]).\n\n%% ============================================================\n\\section{Irreducible Sample Analysis}\n\\label{sec:irreducible}\n\nThe \\texttt{exception\\_only} condition with Qwen-2.5-Coder-7B misclassifies exactly 2 out of 1,190 test samples across all three seeds (42, 123, 456), with 100\\% overlap across seeds.\nBoth samples (IDs 901 and 905) share the following characteristics:\n\n\\begin{itemize}\n\\item \\textbf{Function:} \\texttt{check\\_dict\\_case} (HumanEval/95)---a function that checks whether all dictionary keys are uniformly upper-case or lower-case strings.\n\\item \\textbf{Ground-truth label:} \\texttt{pass}.\n\\item \\textbf{Predicted label:} \\texttt{fail} (false negative).\n\\item \\textbf{Cross-seed consistency:} Both samples are misclassified identically by all three seeds, indicating a systematic rather than stochastic error.\n\\end{itemize}\n\nManual inspection reveals the root cause: \\texttt{check\\_dict\\_case} uses \\texttt{all()} over a generator expression, and Python's \\texttt{all()} short-circuits on the first \\texttt{True} value, raising \\texttt{GeneratorExit} to terminate the generator.\nBecause \\texttt{GeneratorExit} is a \\texttt{BaseException} subclass, the tracer records it as seven \\texttt{[ERROR] GeneratorExit} lines---even though the function executes correctly and the test passes.\nThe model observes these spurious error markers and reasonably but incorrectly predicts \\texttt{fail}.\nThis is not a model failure but a representation ambiguity: the \\texttt{exception\\_only} format cannot distinguish genuine exceptions from benign \\texttt{BaseException} subclasses triggered by Python's iterator protocol.\n\nMost configurations converge to these same 2 errors: Qwen-1.5B, Qwen-7B (3 seeds), CodeLlama-13B (seeds 42/456), and DeepSeek-6.7B (seeds 42/456) all produce error set $\\{901, 905\\}$.\nHowever, CodeLlama-13B seed 123 achieves 100\\% accuracy (0/1190 errors), correctly classifying both samples.\nThis demonstrates that 99.83\\% is a near-perfect \\emph{floor} (the convergence attractor for most LoRA initializations) rather than a hard data ceiling: the representation supports perfect accuracy, but most initializations converge to the same 2-error basin.\nThe practical implication is that these errors are high-probability convergence artifacts addressable through seed selection or ensemble methods, not fundamental limitations of the exception-based representation.\n\n%% ============================================================\n\\section{Exception Type Accuracy Breakdown}\n\\label{sec:exception_type}\n\nTable~\\ref{tab:exception_type} reports \\texttt{exception\\_only} accuracy stratified by exception type on Qwen-2.5-7B (seed=42, $N{=}1{,}190$).\nAll standard exception types (\\texttt{TypeError}, \\texttt{ValueError}, \\texttt{IndexError}, etc.) achieve 100\\% accuracy.\nThe only misclassifications arise from \\texttt{GeneratorExit}, a \\texttt{BaseException} subclass that is not an \\texttt{Exception}---it is raised by Python's iterator protocol during generator short-circuiting, not by actual program errors.\n\n\\begin{table}[t]\n\\centering\n\\caption{Exception type accuracy breakdown for \\texttt{exception\\_only} (Qwen-7B, seed=42). All true error types achieve 100\\%. The only failures come from \\texttt{GeneratorExit} (a \\texttt{BaseException} subclass, not an \\texttt{Exception}), which appears in 2 passing samples.}\n\\label{tab:exception_type}\n\\small\n\\begin{tabular}{lcc}\n\\toprule\n\\textbf{Exception Type} & \\textbf{Samples} & \\textbf{Accuracy} \\\\\n\\midrule\nTypeError & 96 & 100\\% \\\\\nValueError & 62 & 100\\% \\\\\nIndexError & 41 & 100\\% \\\\\nKeyError & 28 & 100\\% \\\\\nAttributeError & 19 & 100\\% \\\\\nAssertionError & 15 & 100\\% \\\\\nRecursionError & 12 & 100\\% \\\\\nOther Exception & 66 & 100\\% \\\\\n\\midrule\nGeneratorExit (BaseException) & 2 & 0\\% \\\\\nNo exception (pass class) & 849 & 100\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThis confirms that the model has learned a clean decision boundary: any true \\texttt{Exception} subclass in the trace implies failure.\nThe \\texttt{GeneratorExit} case represents a semantic ambiguity in the trace format rather than a model failure, as discussed in \\S\\ref{sec:irreducible}.\n\n%% ============================================================\n\\section{Trace Length Ablation}\n\\label{sec:trace_length_full}\n\nTo test whether the \\texttt{full\\_trace} performance gap is caused by input truncation at training time, we vary the maximum trace token budget on Qwen-2.5-7B (seed=42) while keeping all other hyperparameters fixed.\n\n\\begin{table}[t]\n\\centering\n\\caption{Trace length and truncation direction ablation on Qwen-2.5-7B ($N{=}1{,}190$, seed=42). Head = standard left-truncation (retain first $k$ tokens); Tail = retain last $k$ tokens. Per-condition bootstrap 95\\% CIs ($B{=}10{,}000$).}\n\\label{tab:trace_length}\n\\small\n\\begin{tabular}{llcc}\n\\toprule\n\\textbf{Direction} & \\textbf{Max Tokens} & \\textbf{Acc (\\%)} & \\textbf{95\\% CI} \\\\\n\\midrule\nHead & 256  & 78.82 & [76.4, 81.0] \\\\\nHead & 512  & 80.42 & [78.2, 82.6] \\\\\nHead & 1024 & 77.23 & [74.9, 79.6] \\\\\nHead & no\\_limit ($\\infty$) & 81.76 & [79.7, 83.9] \\\\\n\\midrule\nTail & 256  & 77.48 & --- \\\\\nTail & 512  & 93.61 & --- \\\\\nTail & 1024 & 96.47 & --- \\\\\nTail & 2048 & 97.31 & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{budget_curve}\n\\caption{Accuracy as a function of token budget and truncation direction (Qwen-2.5-7B, $N{=}1{,}190$). Tail-truncation (keeping last $k$ tokens) monotonically improves beyond 256 tokens and consistently outperforms head-truncation by 13--19pp at budgets ${\\geq}$512. The flat head-truncation curve (77--82\\%) contrasts with the steep tail-truncation rise, confirming that diagnostic signal is localized near trace end. Dashed lines show \\texttt{exception\\_only} (99.83\\%) and \\texttt{no\\_trace} (75.13\\%) as upper and lower bounds. Tail-256 (${\\approx}$ \\texttt{no\\_trace}) indicates the signal window begins approximately 256 tokens from the trace terminus.}\n\\label{fig:trace_length}\n\\end{figure}\n\nAs shown in Table~\\ref{tab:trace_length} and Figure~\\ref{fig:trace_length}, all four trace length conditions fall within a 5pp range (77.2\\%--81.8\\%).\nTo quantify the reliability of the observed differences, Table~\\ref{tab:trace_length_pairwise} reports paired bootstrap comparisons ($B{=}10{,}000$, seed=42) across all condition pairs.\n\n\\begin{table}[t]\n\\centering\n\\caption{Pairwise paired bootstrap comparisons for trace length ablation ($B{=}10{,}000$, seed=42). $\\Delta$ = accuracy difference between the two conditions (first $-$ second in the budget group; condition $-$ baseline in the other groups). **$p{<}0.01$; ***$p{<}0.001$.}\n\\label{tab:trace_length_pairwise}\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llccc}\n\\toprule\n& \\textbf{Comparison} & \\textbf{$\\Delta$ (pp)} & \\textbf{95\\% CI} & \\textbf{$p$-value} \\\\\n\\midrule\n\\multirow{4}{*}{\\rotatebox{90}{\\scriptsize Budget}}\n& 512 vs.\\ 256           & $+$1.60  & [$-$0.34, $+$3.53]   & 0.117 \\\\\n& 1024 vs.\\ 512          & $-$3.19  & [$-$5.29, $-$1.09]   & 0.002** \\\\\n& no\\_limit vs.\\ 1024    & $+$4.54  & [$+$2.52, $+$6.55]   & ${<}$0.001*** \\\\\n& no\\_limit vs.\\ 256     & $+$2.94  & [$+$0.84, $+$5.04]   & 0.006** \\\\\n\\midrule\n\\multirow{4}{*}{\\rotatebox{90}{\\scriptsize vs.\\ no\\_trace}}\n& 256 $-$ no\\_trace       & $+$3.70  & [$+$1.43, $+$6.05]   & 0.002** \\\\\n& 512 $-$ no\\_trace       & $+$5.29  & [$+$3.03, $+$7.56]   & ${<}$0.001*** \\\\\n& 1024 $-$ no\\_trace      & $+$2.10  & [$-$0.17, $+$4.37]   & 0.078 \\\\\n& no\\_limit $-$ no\\_trace & $+$6.64  & [$+$4.37, $+$8.99]   & ${<}$0.001*** \\\\\n\\midrule\n\\multirow{4}{*}{\\rotatebox{90}{\\scriptsize vs.\\ exc.}}\n& 256 $-$ exc\\_only       & $-$21.01 & [$-$23.45, $-$18.74] & ${<}$0.001*** \\\\\n& 512 $-$ exc\\_only       & $-$19.41 & [$-$21.76, $-$17.14] & ${<}$0.001*** \\\\\n& 1024 $-$ exc\\_only      & $-$22.61 & [$-$25.04, $-$20.25] & ${<}$0.001*** \\\\\n& no\\_limit $-$ exc\\_only & $-$18.07 & [$-$20.34, $-$15.88] & ${<}$0.001*** \\\\\n\\bottomrule\n\\end{tabular}%\n}\n\\end{table}\n\n\\paragraph{Non-monotonic pattern.}\nThe trend across trace budgets is non-monotonic: 512 tokens (80.42\\%) slightly outperforms 256 tokens (78.82\\%), but doubling to 1024 tokens \\emph{decreases} accuracy to 77.23\\%---a statistically significant 3.19pp drop ($p{=}0.002$, 95\\% CI [$-$5.29, $-$1.09]).\nThe no-limit condition (81.76\\%) recovers and significantly exceeds 1024 tokens ($p{<}0.001$), but 1024 tokens is not significantly better than the \\texttt{no\\_trace} baseline (75.13\\%; $\\Delta{=}{+}2.10$pp, $p{=}0.078$, 95\\% CI [$-$0.17, $+$4.37]).\nThis means that truncating traces to an intermediate length can be \\emph{worse} than providing no trace at all---the 1024-token budget retains enough irrelevant content to mislead the model while discarding diagnostic events that might appear late in the trace.\n\n\\paragraph{Comparison to baselines.}\nAll four trace budget conditions significantly exceed \\texttt{no\\_trace} except 1024 tokens ($p{=}0.078$), confirming that raw trace content provides some signal but unreliably so.\nThe gap to \\texttt{exception\\_only} (99.83\\%) is massive for every budget condition (18--23pp, all $p{<}0.001$), underscoring that even unlimited raw traces cannot substitute for targeted signal extraction.\nThe best full-trace condition (no\\_limit, 81.76\\%) still lags \\texttt{exception\\_only} by 18.07pp (95\\% CI [$-$20.34, $-$15.88]).\n\n\\paragraph{Interpretation.}\nThese results rule out input truncation as the primary explanation for the full-trace performance gap: even with unlimited tokens, the model cannot extract the diagnostic signal that VOTA's targeted compression provides.\nThe non-monotonic dip at 1024 tokens is consistent with a ``worst-of-both-worlds'' regime where the model receives enough noisy context to dilute the signal but not enough to compensate through broader coverage.\nThe result reinforces the information density interpretation (\\S\\ref{sec:density}): the gap between full traces and VOTA is driven by the \\emph{content} of the trace (irrelevant lines diluting the diagnostic signal), not its \\emph{length}.\nIn contrast, VOTA's compressed representation concentrates the diagnostic signal into fewer tokens, making it sensitive to truncation when those tokens are removed (\\S\\ref{sec:cross_model}).\n\n\\paragraph{Truncation direction.}\nTail-truncation (retaining the last $k$ tokens) dramatically outperforms head-truncation: \\texttt{tail\\_2048} achieves 97.31\\% vs.\\ \\texttt{head\\_2048} (no\\_limit) at 81.76\\%, a 15.55pp improvement.\nEven \\texttt{tail\\_512} (93.61\\%) exceeds every head-truncation condition by over 11pp.\n\nHowever, \\texttt{tail\\_256} (77.48\\%) performs at the \\texttt{no\\_trace} baseline level (75.13\\%), indicating that the diagnostic signal does not reside in the very last trace lines.\nThe critical jump occurs between 256 and 512 tail tokens (+16.13pp), localizing the signal window to approximately 256--512 tokens from the trace terminus.\nThis is consistent with Python's execution model: exception tracebacks and assertion comparisons appear near the end of the trace but are preceded by the final function call frames, placing them typically 300--500 tokens from the terminus rather than at the absolute end.\n\nThe 18.07pp gap from \\texttt{full\\_trace} to \\texttt{exception\\_only} decomposes as: 86\\% positional concentration (recovered by tail-truncation at 2048 tokens) and 14\\% residual content noise (the 2.52pp gap from \\texttt{tail\\_2048} to \\texttt{exception\\_only} that persists regardless of truncation direction).\nThe fact that \\texttt{exception\\_only} (99.83\\%) still outperforms \\texttt{tail\\_2048} (97.31\\%) confirms that semantic extraction (identifying the exception type and message) is superior to positional extraction (keeping a fixed window), because the model need not filter out non-diagnostic lines that happen to fall within the window.\n\n\\paragraph{Cross-model tail-truncation verification.}\nTable~\\ref{tab:tail_cross_model} extends the tail-2048 analysis to two additional models.\nThe positional concentration pattern generalizes: all three models achieve 94.96--97.90\\% with \\texttt{tail\\_2048}, leaving residual gaps of only 1.93--4.37pp to \\texttt{exception\\_only}.\nDeepSeek-6.7B shows the largest residual (4.37pp), consistent with its known sensitivity to long-context formatting (Appendix~\\ref{sec:training_dynamics}); the diagnostic signal is present in the tail window but partially degraded by the model's weaker long-context processing.\nQwen-1.5B (97.90\\%) performs comparably to Qwen-7B (97.31\\%), confirming that positional signal extraction, like exception-based extraction, is signal-limited rather than capacity-limited.\n\n\\begin{table}[t]\n\\centering\n\\caption{Cross-model \\texttt{tail\\_2048} verification ($N{=}1{,}190$). Positional concentration of diagnostic signal holds across all tested models and architecture families.}\n\\label{tab:tail_cross_model}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Model} & \\textbf{Tail-2048 (\\%)} & \\textbf{exc\\_only (\\%)} & \\textbf{Gap (pp)} \\\\\n\\midrule\nQwen-7B & 97.31 & 99.83 & 2.52 \\\\\nQwen-1.5B & 97.90 & 99.83 & 1.93 \\\\\nDeepSeek-6.7B & 94.96 & 99.33 & 4.37 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n%% ============================================================\n\\section{Calibration Analysis}\n\\label{sec:calibration_full}\n\nBeyond accuracy, we evaluate whether trace conditions affect prediction calibration, motivated by recent findings that code LLM confidence is often poorly calibrated \\citep{spiess2025calibration}.\n\n\\begin{table}[t]\n\\centering\n\\caption{Calibration metrics on Qwen-2.5-7B ($N{=}1{,}190$, seed=42). ECE = expected calibration error; Brier = Brier score. Lower is better for both.}\n\\label{tab:calibration}\n\\small\n\\begin{tabular}{lcc}\n\\toprule\n\\textbf{Condition} & \\textbf{ECE $\\downarrow$} & \\textbf{Brier $\\downarrow$} \\\\\n\\midrule\nae\\_only & \\textbf{0.0004} & \\textbf{0.0008} \\\\\nexception\\_only & 0.0027 & 0.0013 \\\\\nVOTA & 0.0054 & 0.005 \\\\\nfull\\_trace & 0.096 & 0.144 \\\\\nno\\_trace & 0.171 & 0.197 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:calibration} shows that calibration quality mirrors the Tier~1/2 hierarchy.\nTier~1 conditions (\\texttt{ae\\_only}: ECE=0.0004; \\texttt{exception\\_only}: ECE=0.0027) produce near-perfectly calibrated predictions, while \\texttt{full\\_trace} (ECE=0.096) and \\texttt{no\\_trace} (ECE=0.171) exhibit substantial miscalibration.\nVOTA (ECE=0.0054) is well-calibrated but slightly worse than either Tier~1 component alone, reinforcing the pattern that combining trace signals dilutes rather than improves the prediction signal.\n\nThe Brier scores tell a consistent story: \\texttt{ae\\_only} (0.0008) and \\texttt{exception\\_only} (0.0013) achieve near-zero scores, while \\texttt{no\\_trace} (0.197) indicates substantial miscalibration.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{fig2_calibration}\n\\caption{Reliability diagrams for four trace conditions on Qwen-2.5-7B ($N{=}1{,}190$, seed=42). \\texttt{exception\\_only} (ECE=0.0027) clusters near the diagonal, while \\texttt{no\\_trace} (ECE=0.171) exhibits systematic overconfidence, a 63$\\times$ gap.}\n\\label{fig:calibration}\n\\end{figure}\n\n%% ============================================================\n\\section{Error Overlap Analysis}\n\\label{sec:error_overlap}\n\nWe analyze the overlap between error sets of different conditions to determine whether they fail on the same samples (Figure~\\ref{fig:error_overlap}).\n\n\\texttt{exception\\_only}'s 2 errors (samples 901 and 905) have zero intersection with the error sets of all other conditions (Jaccard = 0.000 in all pairwise comparisons).\nThis orthogonality arises because \\texttt{exception\\_only} errors are caused by \\texttt{GeneratorExit} false positives (pass samples misclassified as fail due to benign \\texttt{BaseException} events), while errors from other conditions are predominantly fail samples misclassified as pass due to insufficient signal.\n\nAmong non-exception conditions, error sets exhibit hierarchical containment: \\texttt{ae\\_only} $\\subset$ VOTA $\\subset$ \\texttt{loop\\_only} $\\subset$ \\texttt{no\\_trace}, with pairwise Jaccard indices increasing with signal overlap.\n\\texttt{loop\\_only} and \\texttt{full\\_trace} share the highest overlap (Jaccard ${\\sim}$0.65), reflecting their shared reliance on behavioral patterns rather than explicit fault indicators.\n\nThis analysis confirms that \\texttt{exception\\_only} operates on an independent signal dimension: its errors are representation ambiguities (iterator protocol artifacts) rather than information deficits, explaining why combining it with other signals cannot eliminate these specific errors.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{error_overlap}\n\\caption{Jaccard similarity between error sets of different conditions (Qwen-7B, seed=42, $N{=}1{,}190$). \\texttt{exception\\_only} (exc\\_only) has zero overlap with all other conditions, confirming it operates on an independent signal dimension.}\n\\label{fig:error_overlap}\n\\end{figure}\n\n%% ============================================================\n\\section{Cross-Dataset Generalization: DebugBench}\n\\label{sec:debugbench_full}\n\nTo test whether exception-based verdict prediction generalizes beyond LLM-generated solutions, we evaluate on DebugBench \\citep{tian2024debugbench}---a dataset of human-written programs with synthetically injected bugs (single-point mutations such as operator replacement, variable misuse, and missing statements).\nAfter filtering for executable Python samples with valid traces, we retain 426 samples with a near-balanced class distribution (majority baseline: 51.4\\%).\n\n\\begin{table}[t]\n\\centering\n\\caption{Generalization to DebugBench ($N{=}426$, Qwen-2.5-7B, seed=42). Wilson 95\\% CIs. The component ranking (exception\\_only $\\geq$ VOTA $>$ no\\_trace) is preserved, and exception\\_only achieves perfect accuracy.}\n\\label{tab:debugbench}\n\\small\n\\begin{tabular}{lcc}\n\\toprule\n\\textbf{Condition} & \\textbf{Acc (\\%)} & \\textbf{95\\% CI} \\\\\n\\midrule\nexception\\_only & \\textbf{100.00} & [99.14, 100.00] \\\\\nVOTA & 99.77 & [99.30, 100.00] \\\\\nno\\_trace & 96.71 & [94.80, 98.40] \\\\\n\\midrule\nMajority baseline & 51.41 & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:debugbench} shows that the component ranking from the main experiments is preserved: \\texttt{exception\\_only} (100.00\\%) $\\geq$ VOTA (99.77\\%) $>$ \\texttt{no\\_trace} (96.71\\%).\nThe \\texttt{exception\\_only} condition achieves perfect accuracy, confirming that the exception-based representation generalizes to a different fault distribution without degradation.\n\nThe absolute margins are much narrower than on the main dataset: the \\texttt{no\\_trace} baseline already achieves 96.71\\%---compared to 75.13\\% on HumanEval+MBPP---leaving only 3.29pp of headroom for trace-based improvement.\nThis ceiling effect reflects a fundamental difference in fault characteristics: DebugBench bugs are synthetically injected single-point mutations, which produce code that is structurally dissimilar from the original correct solution; a model can often identify the fault from source code alone.\nIn contrast, the HumanEval+MBPP solutions are LLM-generated, producing natural errors (logic mistakes, edge-case failures) where the faulty and correct solutions may be structurally similar, making code-only verdict prediction substantially harder.\n\nThese results support exception-based verdict prediction as a generalizable approach---the method does not degrade on an out-of-distribution dataset, and the exception dominance ranking (exception\\_only $\\geq$ VOTA $>$ no\\_trace) is consistent across both datasets---but the narrow DebugBench margins are insufficient to independently validate trace importance.\nThe 24.70pp trace lift on the main dataset (no\\_trace 75.13\\% $\\to$ exception\\_only 99.83\\%) remains the primary evidence for the value of exception-based trace signals.\n\n%% ============================================================\n\\section{Cross-Model Robustness Analysis}\n\\label{sec:robustness_analysis}\n\nThe cross-model gap pattern (Table~\\ref{tab:cross_model}) suggests a design principle: \\emph{trace representations should match the model capability floor, not the ceiling.}\nException events are consistently the most effective component on both models, and their structural simplicity---a fixed-format error message---ensures that the relative advantage over richer representations holds across all seeds.\nTwo of three DeepSeek seeds match Qwen-level accuracy (99.33\\%); the outlier (seed 123, 91.09\\%) we hypothesize reflects LoRA initialization sensitivity landing in a suboptimal basin (fail recall = 70.5\\%, though direct evidence is lacking), not a failure of the exception signal itself---even this outlier outperforms VOTA (84.45\\%) by 6.64pp.\nThe VOTA cross-model gap is confounded by two factors: (1)~tokenizer efficiency---the DeepSeek tokenizer averages 2{,}626 tokens per VOTA sample versus Qwen's 1{,}929, causing 91.7\\% of training samples to exceed the 2{,}048-token context window; content-aware truncation preferentially removes the terminal structured prompt, preserving the verdict label but truncating trace content---and (2)~base model capability differences, consistent with findings that SFT generalization depends on pretrain quality \\citep{yang2024generalization}.\nThe two factors cannot be disentangled in the current experimental design.\nOur \\texttt{exception\\_only} design sidesteps the truncation confound entirely: inputs have a median of 150 tokens (mean 398), well below the 2{,}048-token context window, so no training samples are truncated on either model.\nThe resulting 0.56pp cross-model gap (Table~\\ref{tab:cross_model}) is therefore a clean measure of model capability differences, making the ``capability floor'' principle directly testable.\nThe practical implication is that trace-based systems should default to the simplest sufficient signal; for smaller models, training stability (multi-seed selection, warmup schedules) is a secondary but addressable concern.\n\n%% ============================================================\n\\section{Training Dynamics and Loss Decoupling}\n\\label{sec:training_dynamics}\n\nThe DeepSeek \\texttt{exception\\_only} results reveal two instructive training dynamics.\nFirst, epoch-level analysis shows mild degradation in 2/3 seeds: seed 42 peaks at 99.83\\% after epoch~1 but settles at 99.33\\% by epoch~3 ($-$0.50pp), seed 123 degrades from 91.43\\% to 91.09\\% ($-$0.34pp), while seed 456 shows no epoch degradation (99.33\\% at both epoch~1 and epoch~3).\nEarly stopping may yield marginal gains for some seeds, but the epoch effect is small (${\\leq}$0.5pp) compared to the seed effect (8.24pp between seeds 42 and 123).\n\nSecond, seeds 123 and 456 converge to nearly identical final training losses (0.122 and 0.123 respectively), yet their accuracies differ by 8.24pp (91.09\\% vs.\\ 99.33\\%).\nThe critical difference lies in fail recall: seeds 42 and 456 achieve 100\\%, while seed 123 achieves only 70.5\\%---the LoRA initialization in seed 123 fails to learn the exception$\\to$fail mapping for a substantial fraction of failing samples, even though the per-token loss appears converged.\nThis demonstrates that token-level training loss can mask fundamental differences in sample-level classification ability, suggesting a parallel to the eval-loss/accuracy decoupling observed in DeepSeek VOTA (where eval loss rose 65\\% from epoch 1 to 3 while accuracy improved by 6.3pp) at the training phase.\nThe practical recommendation is twofold: (1)~use task-specific metrics (accuracy, fail recall) for checkpoint and seed selection rather than training or evaluation loss, and (2)~for deployment on smaller models, train multiple seeds and select the best, as a single run may not reliably converge to the correct classification boundary.\n\n\\paragraph{Format collapse, not semantic failure.}\nThe 100 errors of seed 123 are not semantic failures but generation format collapse: on inputs exceeding 4,000 characters (those containing verbose locals dumps), the model echoes trace content instead of emitting a verdict token, while achieving zero errors on shorter inputs.\nThis indicates that the LoRA initialization of seed 123 specifically compromises long-context format compliance rather than exception signal comprehension, further supporting the robustness advantage of compact \\texttt{exception\\_only} inputs.\n\nThe contrast with VOTA is instructive: DeepSeek VOTA accuracy monotonically increases from 78.15\\% to 84.45\\% across epochs, but is consistent with a performance limit associated with the high trace truncation rate (\\S\\ref{sec:cross_model})---the model progressively extracts signal from samples with intact trace content but cannot fully compensate for the information loss in the truncated majority.\nThe 84.45\\% accuracy reflects a combination of trace information loss and model capability constraints.\n\n%% ============================================================\n\\section{Deduplication Statistics}\n\\label{sec:dedup_stats}\n\nTable~\\ref{tab:dedup} reports the duplication rates across trace formats.\nBecause multiple passing solutions to the same problem produce identical (input, output) pairs in the \\texttt{exception\\_only} format---correct executions raise no exceptions, so the trace content is the same regardless of the solution's internal logic---the dataset contains duplicate rows.\nTrain--test input overlap is zero (split by problem ID), so no information leakage occurs.\nThe high duplication in \\texttt{exception\\_only} does not affect our experimental conclusions: after deduplication the training set still contains 2,858 unique samples and the test set 607, providing sufficient coverage for the 591-problem benchmark.\nThe \\texttt{exception\\_only} test set contains 48.99\\% duplicate inputs due to representation compactness; all confidence intervals treat samples as independent Bernoulli trials.\n\n\\begin{table}[t]\n\\centering\n\\caption{Deduplication statistics. The \\texttt{exception\\_only} format collapses multiple passing solutions into identical rows because correct executions produce no exception events. Train--test input overlap is 0 (no leakage).}\n\\label{tab:dedup}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Split} & \\textbf{Total} & \\textbf{Unique} & \\textbf{Dup.\\ rate} \\\\\n\\midrule\nexception\\_only train & 4{,}720 & 2{,}858 & 39.45\\% \\\\\nexception\\_only test  & 1{,}190 &   607 & 48.99\\% \\\\\nraw\\_traces (full)    & 5{,}910 & 5{,}803 &  1.81\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n%% ============================================================\n\\section{Regex Baseline Analysis}\n\\label{sec:regex_baselines}\n\nTo establish a non-learning upper bound, we evaluate six regex-based baselines on the \\texttt{exception\\_only} test set ($N{=}1{,}190$) and two format-specific baselines on VOTA and \\texttt{full\\_trace} inputs.\n\n\\begin{table}[t]\n\\centering\n\\caption{Regex baseline accuracy ($N{=}1{,}190$). B4 is the strongest semantic baseline (6.22pp below SFT \\texttt{exception\\_only}, McNemar $p{<}0.001$). B6 uses an error count threshold. $^\\ddag$B5 exploits a data formatting artifact: the \\texttt{[No exception data in trace]} marker is deterministically present in all pass samples, making this a format-level shortcut rather than a genuine exception-based heuristic.}\n\\label{tab:regex}\n\\small\n\\begin{tabular}{llc}\n\\toprule\n\\textbf{Baseline} & \\textbf{Method} & \\textbf{Acc (\\%)} \\\\\n\\midrule\nB1: \\texttt{[ERROR]} presence & string match & 93.45 \\\\\nB2: Traceback presence & string match & 71.51 \\\\\nB3: Any keyword & union of B1+B2+Exception & 93.45 \\\\\nB4: Exception type regex & regex on exception class names & \\textbf{93.61} \\\\\nB5: Format marker & \\texttt{[No exception data]} $\\to$ pass & 99.33$^\\ddag$ \\\\\nB6: Error count $\\geq$2 & count threshold & 92.02 \\\\\n\\midrule\nVOTA format regex & best regex on VOTA traces & 75.55 \\\\\nfull\\_trace format regex & best regex on full traces & 77.39 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe strongest legitimate baseline (B4, 93.61\\%) applies regex pattern-matching on Python exception class names (e.g., \\texttt{ValueError}, \\texttt{TypeError}).\nIts errors concentrate on 8 boundary samples where a \\texttt{ValueError} is raised inside a \\texttt{try/except} block and caught---the program passes despite an exception occurring in the trace.\nSFT \\texttt{exception\\_only} correctly classifies 6 of these 8 samples, indicating that the model learns the semantic distinction between caught (benign) and uncaught (fault-indicating) exceptions.\nB5 (99.33\\%) achieves near-SFT accuracy but relies on the deterministic presence of a format marker in pass-class traces, which is an artifact of the trace preprocessing pipeline rather than a generalizable signal; McNemar test vs.\\ SFT yields $p{=}0.041$, confirming a statistically significant difference.\n\n\\paragraph{Cross-format comparison.}\nTable~\\ref{tab:regex_cross_format} compares SFT and the best applicable regex baseline for each trace format.\nThe SFT advantage increases with format complexity: \\texttt{no\\_trace} (+3.62pp over majority baseline) $<$ \\texttt{full\\_trace} (+4.37pp) $<$ \\texttt{exception\\_only} (+6.22pp) $\\ll$ VOTA (+23.86pp).\nThe VOTA gap is largest because its structured multi-component format carries semantic content that regex cannot parse, while \\texttt{exception\\_only}'s simpler format allows regex to capture most of the signal.\n\n\\begin{table}[t]\n\\centering\n\\caption{SFT vs.\\ best regex baseline by trace format ($N{=}1{,}190$). Regex baselines: majority class for \\texttt{no\\_trace}, keyword matching for \\texttt{full\\_trace}, pattern matching for VOTA, exception type regex (B4) for \\texttt{exception\\_only}.}\n\\label{tab:regex_cross_format}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Format} & \\textbf{SFT (\\%)} & \\textbf{Regex (\\%)} & \\textbf{$\\Delta$ (pp)} \\\\\n\\midrule\nexception\\_only & 99.83 & 93.61 & +6.22 \\\\\nVOTA & 99.41 & 75.55 & +23.86 \\\\\nfull\\_trace & 81.76 & 77.39 & +4.37 \\\\\nno\\_trace & 75.13 & 71.51 & +3.62 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n%% ============================================================\n\\section{Cross-Model Zero-Shot Comparison}\n\\label{sec:zeroshot_cross_model}\n\nTable~\\ref{tab:zeroshot_cross_model} compares zero-shot and SFT \\texttt{exception\\_only} accuracy across four models.\nZero-shot performance does not correlate with model size: the smallest model (Qwen-1.5B, 93.45\\%) outperforms all larger models, while the largest (CodeLlama-13B) falls below majority baseline.\nSFT compresses the 42.44pp zero-shot range to 0.56pp, eliminating architecture-dependent variance.\n\n\\begin{table}[t]\n\\centering\n\\caption{Zero-shot vs.\\ SFT \\texttt{exception\\_only} across four models ($N{=}1{,}190$). Zero-shot accuracy is uncorrelated with model size; SFT normalizes cross-architecture variance from 42.44pp to 0.56pp.}\n\\label{tab:zeroshot_cross_model}\n\\small\n\\begin{tabular}{llccc}\n\\toprule\n\\textbf{Model} & \\textbf{Size} & \\textbf{Zero-shot (\\%)} & \\textbf{SFT (\\%)} & \\textbf{$\\Delta$ (pp)} \\\\\n\\midrule\nQwen-1.5B & 1.5B & 93.45 & 99.83 & +6.38 \\\\\nDeepSeek-6.7B & 6.7B & 90.59 & 99.33 & +8.74 \\\\\nQwen-7B & 7B & 89.08 & 99.83 & +10.75 \\\\\nCodeLlama-13B & 13B & 51.01 & 99.89 & +48.88 \\\\\n\\midrule\nRange & --- & 42.44pp & 0.56pp & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n",
      "numLines": 635,
      "startLine": 1,
      "totalLines": 635
    }
  },
  "sourceToolAssistantUUID": "8fc5a144-20f7-4071-9749-04274da87881",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/.claude/sessions/review_reviewer_1_7624f219",
  "sessionId": "f76386b4-9d1f-4f92-b831-706bc4acd94d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Tool call

_source line 35 · 2026-05-17T18:02:16.032Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01EWeS1urNjbW1MV56SMcTtJ`</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract the complete ACL ARR review form: all evaluation dimensions, their scoring scales, and detailed descriptions of each score level. Include Overall Assessment, Confidence, Soundness, Excitement/Novelty, Reproducibility, and any other dimensions."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7c460b27-702f-4d6d-9d0a-fd7e39151e81",
  "isSidechain": false,
  "requestId": "req_011Cb8aajVuBwdfSNX7WampT",
  "type": "assistant",
  "uuid": "a7357532-198f-4f88-8617-3381f9f76c9d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/.claude/sessions/review_reviewer_1_7624f219",
  "sessionId": "f76386b4-9d1f-4f92-b831-706bc4acd94d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01V6CMvB9xpGCvP17WPMMBS6",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 9267,
      "cache_creation_input_tokens": 1432,
      "cache_read_input_tokens": 29778,
      "output_tokens": 469,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1432,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 9267,
          "output_tokens": 469,
          "cache_read_input_tokens": 29778,
          "cache_creation_input_tokens": 1432,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1432
          },
          "type": "message"
        }
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

_source line 36_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[Round 1 审稿请求]: ## Round 1 审稿任务 — Reviewer 1  **你的审查侧重**: 方法严谨性 + 实验设计 + 统计有效性 + 可复现性  ### Venue 信息 - **目标**: EMNLP 2026 via ARR May 2026 cycle - **截止日期**: 2026-05-25 - **页数限制**: Long paper ≤ 8 页正文（不含…",
  "leafUuid": "a7357532-198f-4f88-8617-3381f9f76c9d",
  "sessionId": "f76386b4-9d1f-4f92-b831-706bc4acd94d"
}
```

---


### Runtime record

_source line 37_

```json
{
  "type": "ai-title",
  "aiTitle": "Round 1 peer review for trace verdict prediction paper",
  "sessionId": "f76386b4-9d1f-4f92-b831-706bc4acd94d"
}
```

---


### Tool result

_source line 38 · 2026-05-17T18:02:23.243Z_

<details><summary>↩ Tool result · `toolu_01EWeS1urNjbW1MV56SMcTtJ`</summary>

```text
# ACL ARR Review Form - Evaluation Dimensions

## 1. **Reviewer Confidence**
Scale: 1-5
- **5**: "Positive that my evaluation is correct. I read the paper very carefully and am familiar with related work."
- **4**: Quite sure with careful checking; unlikely but possible oversight
- **3**: Reasonably confident but may have missed details or math verification
- **2**: Can defend evaluation but likely missed some details or novelty aspects
- **1**: Outside expertise area or paper very difficult to understand

## 2. **Soundness**
Scale: 1-5 (with half-point increments)
- **5**: "Excellent: This study is one of the most thorough I have seen, given its type."
- **4**: Sufficient support for claims; additional experiments optional
- **3**: Main claims supported adequately; minor points need refinement
- **2**: Major technical/methodological problems; claims insufficiently supported
- **1**: "Major Issues: This study is not yet sufficiently thorough to warrant publication"

## 3. **Excitement**
Scale: 1-5 (with half-point increments)
- **5**: "Highly Exciting: I would recommend this paper to others"
- **4**: Would mention to others; would attend presentation
- **3**: Might mention points; would attend if time permits
- **2**: Doesn't resonate personally; might appeal to others
- **1**: Not relevant to computational linguistics community

## 4. **Overall Assessment**
Scale: 1-5 (with half-point increments)
- **5**: Consider for Award (top 2.5%)
- **4**: Conference acceptance
- **3**: Findings acceptance
- **2**: Needs substantial revisions (next cycle)
- **1**: Do not resubmit/not relevant

## 5. **Reproducibility**
Scale: 1-5
- **5**: Results easily reproducible
- **4**: Mostly reproducible with minor variations possible
- **3**: Reproducible with difficulty; underspecified parameters
- **2**: Hard to reproduce; unavailable data or insufficient details
- **1**: Cannot reproduce results

## 6. **Datasets**
Scale: 1-5
- **5**: Enabling new research directions
- **4**: "Useful: I would recommend the new datasets to other researchers"
- **3**: Potentially useful for some work
- **2**: Documentary value only
- **1**: No usable datasets submitted

## 7. **Software**
Scale: 1-5
- **5**: Enabling new projects
- **4**: Useful for ongoing research work
- **3**: Potentially useful for some applications
- **2**: Documentary value for replication only
- **1**: No usable software released

## 8. **Author Identity Knowledge**
Scale: 1-5
- **5**: Definite author identification from submission violation
- **4**: Identification from preprints/workshops
- **3**: Identification from paper contents
- **2**: Identification from external sources
- **1**: No educated guess
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a7357532-198f-4f88-8617-3381f9f76c9d",
  "isSidechain": false,
  "promptId": "b73967ab-1e3d-4502-97ef-ede23a2a2cd7",
  "type": "user",
  "uuid": "75a8bd0a-8dde-4b1d-8dac-5199d6fe1b0b",
  "toolUseResult": {
    "bytes": 25365,
    "code": 200,
    "codeText": "OK",
    "result": "# ACL ARR Review Form - Evaluation Dimensions\n\n## 1. **Reviewer Confidence**\nScale: 1-5\n- **5**: \"Positive that my evaluation is correct. I read the paper very carefully and am familiar with related work.\"\n- **4**: Quite sure with careful checking; unlikely but possible oversight\n- **3**: Reasonably confident but may have missed details or math verification\n- **2**: Can defend evaluation but likely missed some details or novelty aspects\n- **1**: Outside expertise area or paper very difficult to understand\n\n## 2. **Soundness**\nScale: 1-5 (with half-point increments)\n- **5**: \"Excellent: This study is one of the most thorough I have seen, given its type.\"\n- **4**: Sufficient support for claims; additional experiments optional\n- **3**: Main claims supported adequately; minor points need refinement\n- **2**: Major technical/methodological problems; claims insufficiently supported\n- **1**: \"Major Issues: This study is not yet sufficiently thorough to warrant publication\"\n\n## 3. **Excitement**\nScale: 1-5 (with half-point increments)\n- **5**: \"Highly Exciting: I would recommend this paper to others\"\n- **4**: Would mention to others; would attend presentation\n- **3**: Might mention points; would attend if time permits\n- **2**: Doesn't resonate personally; might appeal to others\n- **1**: Not relevant to computational linguistics community\n\n## 4. **Overall Assessment**\nScale: 1-5 (with half-point increments)\n- **5**: Consider for Award (top 2.5%)\n- **4**: Conference acceptance\n- **3**: Findings acceptance\n- **2**: Needs substantial revisions (next cycle)\n- **1**: Do not resubmit/not relevant\n\n## 5. **Reproducibility**\nScale: 1-5\n- **5**: Results easily reproducible\n- **4**: Mostly reproducible with minor variations possible\n- **3**: Reproducible with difficulty; underspecified parameters\n- **2**: Hard to reproduce; unavailable data or insufficient details\n- **1**: Cannot reproduce results\n\n## 6. **Datasets**\nScale: 1-5\n- **5**: Enabling new research directions\n- **4**: \"Useful: I would recommend the new datasets to other researchers\"\n- **3**: Potentially useful for some work\n- **2**: Documentary value only\n- **1**: No usable datasets submitted\n\n## 7. **Software**\nScale: 1-5\n- **5**: Enabling new projects\n- **4**: Useful for ongoing research work\n- **3**: Potentially useful for some applications\n- **2**: Documentary value for replication only\n- **1**: No usable software released\n\n## 8. **Author Identity Knowledge**\nScale: 1-5\n- **5**: Definite author identification from submission violation\n- **4**: Identification from preprints/workshops\n- **3**: Identification from paper contents\n- **2**: Identification from external sources\n- **1**: No educated guess",
    "durationMs": 7206,
    "url": "https://aclrollingreview.org/reviewform"
  },
  "sourceToolAssistantUUID": "a7357532-198f-4f88-8617-3381f9f76c9d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/.claude/sessions/review_reviewer_1_7624f219",
  "sessionId": "f76386b4-9d1f-4f92-b831-706bc4acd94d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Runtime record

_source line 39 · 2026-05-17T18:02:23.250Z_

```json
{
  "parentUuid": "75a8bd0a-8dde-4b1d-8dac-5199d6fe1b0b",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "91bd8bb4-eebc-46ff-ae1e-9dc7763b141b",
  "timestamp": "2026-05-17T18:02:23.250Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/.claude/sessions/review_reviewer_1_7624f219",
  "sessionId": "f76386b4-9d1f-4f92-b831-706bc4acd94d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---


### Assistant

_source line 40 · 2026-05-17T18:02:27.179Z_

<details><summary>Logged reasoning block</summary>

```text
Good, I've now read the full paper and the ACL ARR review form. Let me also read the references.bib and arr_checklist.tex files to complete my review.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "91bd8bb4-eebc-46ff-ae1e-9dc7763b141b",
  "isSidechain": false,
  "requestId": "req_011Cb8abw3DPj1zas94zEgR9",
  "type": "assistant",
  "uuid": "de8ea59b-5b44-41cc-870b-572d62fc0935",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/.claude/sessions/review_reviewer_1_7624f219",
  "sessionId": "f76386b4-9d1f-4f92-b831-706bc4acd94d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015sJnPGBywusXUZ9bSRGEjb",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 29501,
      "cache_read_input_tokens": 31210,
      "output_tokens": 254,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 29501,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 254,
          "cache_read_input_tokens": 31210,
          "cache_creation_input_tokens": 29501,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 29501
          },
          "type": "message"
        }
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

_source line 41 · 2026-05-17T18:02:28.137Z_

已获取 ACL ARR review form 和论文正文+附录。继续读取 references.bib 和 ARR checklist。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "de8ea59b-5b44-41cc-870b-572d62fc0935",
  "isSidechain": false,
  "requestId": "req_011Cb8abw3DPj1zas94zEgR9",
  "type": "assistant",
  "uuid": "84730c6a-be3c-4bf1-a065-e43659b0d8c2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/.claude/sessions/review_reviewer_1_7624f219",
  "sessionId": "f76386b4-9d1f-4f92-b831-706bc4acd94d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015sJnPGBywusXUZ9bSRGEjb",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 29501,
      "cache_read_input_tokens": 31210,
      "output_tokens": 254,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 29501,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 254,
          "cache_read_input_tokens": 31210,
          "cache_creation_input_tokens": 29501,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 29501
          },
          "type": "message"
        }
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

_source line 42 · 2026-05-17T18:02:29.999Z_

<details open><summary>🔧 Tool call — Read · `toolu_01RbQ81rU6xNSTfKERJoPsYd`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "84730c6a-be3c-4bf1-a065-e43659b0d8c2",
  "isSidechain": false,
  "requestId": "req_011Cb8abw3DPj1zas94zEgR9",
  "type": "assistant",
  "uuid": "8e91956e-2c4e-49b2-8ea9-ee78b7405253",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/.claude/sessions/review_reviewer_1_7624f219",
  "sessionId": "f76386b4-9d1f-4f92-b831-706bc4acd94d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015sJnPGBywusXUZ9bSRGEjb",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 29501,
      "cache_read_input_tokens": 31210,
      "output_tokens": 254,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 29501,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 254,
          "cache_read_input_tokens": 31210,
          "cache_creation_input_tokens": 29501,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 29501
          },
          "type": "message"
        }
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

_source line 43 · 2026-05-17T18:02:30.218Z_

<details><summary>↩ Tool result · `toolu_01YZV1137upxkodntquuULP1`</summary>

```text
1	\documentclass[11pt,a4paper]{article}
2	\usepackage[review]{acl}
3	\usepackage{times,latexsym}
4	\usepackage{booktabs}
5	
6	\title{ARR Reproducibility Checklist\\(Supplementary Material)}
7	\author{Anonymous ACL submission}
8	
9	\begin{document}
10	\maketitle
11	
12	\section*{Responsible NLP Research Checklist}
13	
14	\subsection*{A. Limitations and Risks}
15	
16	\begin{enumerate}
17	\item \textbf{Did you discuss the limitations of your work?} \\
18	\textit{Yes.} A dedicated Limitations section discusses: single-dataset scope, single model scale (7B), seed-dependent variance on DeepSeek, the invalidated full\_trace run, generator--evaluator overlap, and task scope limited to verdict prediction.
19	
20	\item \textbf{Did you discuss any potential risks of your work?} \\
21	\textit{Yes.} The Ethics Statement notes that the work uses public benchmarks, involves no human subjects, and has minimal environmental impact. Verdict prediction is a developer-facing tool with no direct end-user impact.
22	\end{enumerate}
23	
24	\subsection*{B. Did you use or create scientific artifacts?}
25	
26	\begin{enumerate}
27	\item \textbf{Did you cite the creators of artifacts you used?} \\
28	\textit{Yes.} HumanEval \cite{chen2021evaluating}, MBPP-sanitized \cite{austin2021program}, DebugBench \cite{tian2024debugbench}, Qwen-2.5-Coder-7B/1.5B-Instruct \cite{qwen2025coder}, CodeLlama-13B-Instruct \cite{roziere2024code}, DeepSeek-Coder-6.7B-Instruct \cite{deepseek2024coder}, LoRA \cite{hu2022lora}, and TRL SFTTrainer are all cited.
29	
30	\item \textbf{Did you discuss the license or terms for use and/or distribution of any artifacts?} \\
31	\textit{Partial.} All base models and datasets are publicly available. HumanEval is released under MIT license; MBPP under CC-BY-4.0; DebugBench under MIT. Model licenses: Qwen-2.5-Coder under Apache 2.0; DeepSeek-Coder under the DeepSeek License.
32	
33	\item \textbf{Did you discuss if your use of existing artifacts was consistent with their intended use?} \\
34	\textit{Yes.} HumanEval and MBPP are standard code generation benchmarks; we use their canonical test cases for verdict evaluation, consistent with their evaluation purpose. DebugBench is designed for debugging evaluation.
35	
36	\item \textbf{Did you discuss the steps taken to check whether the data contains any information that names or uniquely identifies individual people or offensive content?} \\
37	\textit{N/A.} All datasets contain only programming problems and solutions with no personal information.
38	\end{enumerate}
39	
40	\subsection*{C. Computational Experiments}
41	
42	\begin{enumerate}
43	\item \textbf{Did you report the number of parameters in the models used, the total computational budget, and computing infrastructure?} \\
44	\textit{Yes.}
45	\begin{itemize}
46	\item Models: Qwen-2.5-Coder-7B/1.5B-Instruct (7B/1.5B parameters), CodeLlama-13B-Instruct (13B parameters), DeepSeek-Coder-6.7B-Instruct (6.7B parameters). Only LoRA adapters are trained (rank=16, $\alpha$=32, targeting all linear layers).
47	\item Hardware: 2$\times$ RTX PRO 6000 Blackwell (${\sim}$96\,GB VRAM each); each experiment uses a single GPU.
48	\item Total compute: ${\sim}$50 GPU-hours across all conditions, models, and seeds. Per-condition training time ranges from 0.5h (no\_trace) to 4.0h (CodeLlama VOTA). See Appendix~B for per-condition wall-clock times.
49	\end{itemize}
50	
51	\item \textbf{Did you report all hyperparameters?} \\
52	\textit{Yes.} Appendix~B (Table~5) reports: LoRA rank (16), alpha (32), dropout (0.05), target modules (all linear layers), epochs (3), per-device batch size (4), gradient accumulation steps (8), effective batch size (32), learning rate ($2 \times 10^{-4}$), LR scheduler (linear decay), warmup ratio (0.1), weight decay (0.01), max sequence length (2,048 tokens).
53	
54	\item \textbf{Did you report descriptive statistics about your results?} \\
55	\textit{Yes.} All accuracy values include Wilson 95\% confidence intervals. Pairwise comparisons use paired bootstrap resampling ($B{=}10{,}000$, seed=42) with reported $p$-values. We report multi-seed results (seeds 42, 123, 456) for the exception\_only condition; other conditions report single-seed results. Standard deviations are provided where multiple seeds are available.
56	
57	\item \textbf{If you used existing packages, did you report the implementation, model, and their versions?} \\
58	\textit{Yes.} HuggingFace TRL SFTTrainer with LoRA via PEFT. Base model identifiers: \texttt{Qwen/Qwen2.5-Coder-7B-Instruct} and \texttt{deepseek-ai/deepseek-coder-6.7b-instruct}.
59	\end{enumerate}
60	
61	\subsection*{D. Human Annotations}
62	
63	\begin{enumerate}
64	\item \textbf{Did you use human annotators?} \\
65	\textit{No.} All labels (pass/fail) are derived from automated test execution. No human annotation was involved.
66	\end{enumerate}
67	
68	\subsection*{E. Data and Code Availability}
69	
70	\begin{itemize}
71	\item \textbf{Code}: Training, evaluation, and trace preprocessing scripts will be released upon acceptance.
72	\item \textbf{Data}: Execution traces, VOTA-compressed traces, and train/test splits will be released. Raw traces are generated deterministically from publicly available benchmarks using Python \texttt{sys.settrace}.
73	\item \textbf{Models}: LoRA adapters for all conditions will be released on HuggingFace.
74	\end{itemize}
75	
76	\subsection*{F. Reproducibility Summary}
77	
78	\begin{table}[h]
79	\centering
80	\small
81	\begin{tabular}{lc}
82	\toprule
83	\textbf{Item} & \textbf{Status} \\
84	\midrule
85	All hyperparameters reported & Yes \\
86	Random seeds specified & Yes (42, 123, 456) \\
87	Error bars / CIs reported & Yes (Wilson 95\% CI) \\
88	Statistical tests reported & Yes (bootstrap, McNemar) \\
89	Computing infrastructure reported & Yes \\
90	Training time reported & Yes \\
91	Code release planned & Yes \\
92	Data release planned & Yes \\
93	Model release planned & Yes \\
94	\bottomrule
95	\end{tabular}
96	\end{table}
97	
98	\bibliography{references}
99	
100	\end{document}
101	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "81550500-391b-4e9b-a710-a4cff9da734c",
  "isSidechain": false,
  "promptId": "b73967ab-1e3d-4502-97ef-ede23a2a2cd7",
  "type": "user",
  "uuid": "3d7041e6-8d51-4f84-a77d-96068f3dacaa",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/arr_checklist.tex",
      "content": "\\documentclass[11pt,a4paper]{article}\n\\usepackage[review]{acl}\n\\usepackage{times,latexsym}\n\\usepackage{booktabs}\n\n\\title{ARR Reproducibility Checklist\\\\(Supplementary Material)}\n\\author{Anonymous ACL submission}\n\n\\begin{document}\n\\maketitle\n\n\\section*{Responsible NLP Research Checklist}\n\n\\subsection*{A. Limitations and Risks}\n\n\\begin{enumerate}\n\\item \\textbf{Did you discuss the limitations of your work?} \\\\\n\\textit{Yes.} A dedicated Limitations section discusses: single-dataset scope, single model scale (7B), seed-dependent variance on DeepSeek, the invalidated full\\_trace run, generator--evaluator overlap, and task scope limited to verdict prediction.\n\n\\item \\textbf{Did you discuss any potential risks of your work?} \\\\\n\\textit{Yes.} The Ethics Statement notes that the work uses public benchmarks, involves no human subjects, and has minimal environmental impact. Verdict prediction is a developer-facing tool with no direct end-user impact.\n\\end{enumerate}\n\n\\subsection*{B. Did you use or create scientific artifacts?}\n\n\\begin{enumerate}\n\\item \\textbf{Did you cite the creators of artifacts you used?} \\\\\n\\textit{Yes.} HumanEval \\cite{chen2021evaluating}, MBPP-sanitized \\cite{austin2021program}, DebugBench \\cite{tian2024debugbench}, Qwen-2.5-Coder-7B/1.5B-Instruct \\cite{qwen2025coder}, CodeLlama-13B-Instruct \\cite{roziere2024code}, DeepSeek-Coder-6.7B-Instruct \\cite{deepseek2024coder}, LoRA \\cite{hu2022lora}, and TRL SFTTrainer are all cited.\n\n\\item \\textbf{Did you discuss the license or terms for use and/or distribution of any artifacts?} \\\\\n\\textit{Partial.} All base models and datasets are publicly available. HumanEval is released under MIT license; MBPP under CC-BY-4.0; DebugBench under MIT. Model licenses: Qwen-2.5-Coder under Apache 2.0; DeepSeek-Coder under the DeepSeek License.\n\n\\item \\textbf{Did you discuss if your use of existing artifacts was consistent with their intended use?} \\\\\n\\textit{Yes.} HumanEval and MBPP are standard code generation benchmarks; we use their canonical test cases for verdict evaluation, consistent with their evaluation purpose. DebugBench is designed for debugging evaluation.\n\n\\item \\textbf{Did you discuss the steps taken to check whether the data contains any information that names or uniquely identifies individual people or offensive content?} \\\\\n\\textit{N/A.} All datasets contain only programming problems and solutions with no personal information.\n\\end{enumerate}\n\n\\subsection*{C. Computational Experiments}\n\n\\begin{enumerate}\n\\item \\textbf{Did you report the number of parameters in the models used, the total computational budget, and computing infrastructure?} \\\\\n\\textit{Yes.}\n\\begin{itemize}\n\\item Models: Qwen-2.5-Coder-7B/1.5B-Instruct (7B/1.5B parameters), CodeLlama-13B-Instruct (13B parameters), DeepSeek-Coder-6.7B-Instruct (6.7B parameters). Only LoRA adapters are trained (rank=16, $\\alpha$=32, targeting all linear layers).\n\\item Hardware: 2$\\times$ RTX PRO 6000 Blackwell (${\\sim}$96\\,GB VRAM each); each experiment uses a single GPU.\n\\item Total compute: ${\\sim}$50 GPU-hours across all conditions, models, and seeds. Per-condition training time ranges from 0.5h (no\\_trace) to 4.0h (CodeLlama VOTA). See Appendix~B for per-condition wall-clock times.\n\\end{itemize}\n\n\\item \\textbf{Did you report all hyperparameters?} \\\\\n\\textit{Yes.} Appendix~B (Table~5) reports: LoRA rank (16), alpha (32), dropout (0.05), target modules (all linear layers), epochs (3), per-device batch size (4), gradient accumulation steps (8), effective batch size (32), learning rate ($2 \\times 10^{-4}$), LR scheduler (linear decay), warmup ratio (0.1), weight decay (0.01), max sequence length (2,048 tokens).\n\n\\item \\textbf{Did you report descriptive statistics about your results?} \\\\\n\\textit{Yes.} All accuracy values include Wilson 95\\% confidence intervals. Pairwise comparisons use paired bootstrap resampling ($B{=}10{,}000$, seed=42) with reported $p$-values. We report multi-seed results (seeds 42, 123, 456) for the exception\\_only condition; other conditions report single-seed results. Standard deviations are provided where multiple seeds are available.\n\n\\item \\textbf{If you used existing packages, did you report the implementation, model, and their versions?} \\\\\n\\textit{Yes.} HuggingFace TRL SFTTrainer with LoRA via PEFT. Base model identifiers: \\texttt{Qwen/Qwen2.5-Coder-7B-Instruct} and \\texttt{deepseek-ai/deepseek-coder-6.7b-instruct}.\n\\end{enumerate}\n\n\\subsection*{D. Human Annotations}\n\n\\begin{enumerate}\n\\item \\textbf{Did you use human annotators?} \\\\\n\\textit{No.} All labels (pass/fail) are derived from automated test execution. No human annotation was involved.\n\\end{enumerate}\n\n\\subsection*{E. Data and Code Availability}\n\n\\begin{itemize}\n\\item \\textbf{Code}: Training, evaluation, and trace preprocessing scripts will be released upon acceptance.\n\\item \\textbf{Data}: Execution traces, VOTA-compressed traces, and train/test splits will be released. Raw traces are generated deterministically from publicly available benchmarks using Python \\texttt{sys.settrace}.\n\\item \\textbf{Models}: LoRA adapters for all conditions will be released on HuggingFace.\n\\end{itemize}\n\n\\subsection*{F. Reproducibility Summary}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{lc}\n\\toprule\n\\textbf{Item} & \\textbf{Status} \\\\\n\\midrule\nAll hyperparameters reported & Yes \\\\\nRandom seeds specified & Yes (42, 123, 456) \\\\\nError bars / CIs reported & Yes (Wilson 95\\% CI) \\\\\nStatistical tests reported & Yes (bootstrap, McNemar) \\\\\nComputing infrastructure reported & Yes \\\\\nTraining time reported & Yes \\\\\nCode release planned & Yes \\\\\nData release planned & Yes \\\\\nModel release planned & Yes \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\bibliography{references}\n\n\\end{document}\n",
      "numLines": 101,
      "startLine": 1,
      "totalLines": 101
    }
  },
  "sourceToolAssistantUUID": "81550500-391b-4e9b-a710-a4cff9da734c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/.claude/sessions/review_reviewer_1_7624f219",
  "sessionId": "f76386b4-9d1f-4f92-b831-706bc4acd94d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Tool result

_source line 44 · 2026-05-17T18:02:30.014Z_

<details><summary>↩ Tool result · `toolu_01RbQ81rU6xNSTfKERJoPsYd`</summary>

```text
1	@inproceedings{chen2025tracepile,
2	  title={Chain of Execution Supervision Promotes General Reasoning in Large Language Models},
3	  author={Nuo Chen and Zehua Li and Keqin Bao and Junyang Lin and Dayiheng Liu},
4	  booktitle={Advances in Neural Information Processing Systems (NeurIPS)},
5	  year={2025},
6	  url={https://arxiv.org/abs/2510.23629},
7	}
8	
9	@inproceedings{ding2024traced,
10	  title={TRACED: Execution-aware Pre-training for Source Code},
11	  author={Yangruibo Ding and Ben Steenhoek and Kexin Pei and Gail Kaiser and Wei Le and Baishakhi Ray},
12	  booktitle={Proceedings of the 46th IEEE/ACM International Conference on Software Engineering (ICSE)},
13	  year={2024},
14	  doi={10.1145/3597503.3608140},
15	  url={https://arxiv.org/abs/2306.07487},
16	}
17	
18	@article{chen2021evaluating,
19	  title={Evaluating Large Language Models Trained on Code},
20	  author={Chen, Mark and Tworek, Jerry and Jun, Heewoo and Yuan, Qiming and Pinto, Henrique Ponde de Oliveira and Kaplan, Jared and Edwards, Harri and Burda, Yuri and Joseph, Nicholas and Brockman, Greg and others},
21	  journal={arXiv preprint arXiv:2107.03374},
22	  year={2021},
23	  url={https://arxiv.org/abs/2107.03374},
24	}
25	
26	@article{austin2021program,
27	  title={Program Synthesis with Large Language Models},
28	  author={Austin, Jacob and Odena, Augustus and Nye, Maxwell and Bosma, Maarten and Michalewski, Henryk and Dohan, David and Jiang, Ellen and Cai, Carrie and Terry, Michael and Le, Quoc and Sutton, Charles},
29	  journal={arXiv preprint arXiv:2108.07732},
30	  year={2021},
31	  url={https://arxiv.org/abs/2108.07732},
32	}
33	
34	@inproceedings{gu2024cruxeval,
35	  title={CRUXEval: A Benchmark for Code Reasoning, Understanding and Execution},
36	  author={Alex Gu and Baptiste Rozi{\`e}re and Hugh Leather and Armando Solar-Lezama and Gabriel Synnaeve and Sida I. Wang},
37	  booktitle={Proceedings of the 41st International Conference on Machine Learning (ICML)},
38	  year={2024},
39	  url={https://arxiv.org/abs/2401.03065},
40	}
41	
42	@inproceedings{hu2022lora,
43	  title={LoRA: Low-Rank Adaptation of Large Language Models},
44	  author={Edward J. Hu and Yelong Shen and Phillip Wallis and Zeyuan Allen-Zhu and Yuanzhi Li and Shean Wang and Lu Wang and Weizhu Chen},
45	  booktitle={Proceedings of the 10th International Conference on Learning Representations (ICLR)},
46	  year={2022},
47	  url={https://arxiv.org/abs/2106.09685},
48	}
49	
50	@article{qwen2025coder,
51	  title={Qwen2.5-Coder Technical Report},
52	  author={Qwen Team},
53	  journal={arXiv preprint arXiv:2409.12186},
54	  year={2024},
55	  url={https://arxiv.org/abs/2409.12186},
56	}
57	
58	@article{deepseek2024coder,
59	  title={DeepSeek-Coder: When the Large Language Model Meets Programming -- The Rise of Code Intelligence},
60	  author={Daya Guo and Qihao Zhu and Dejian Yang and Zhenda Xie and Kai Dong and Wentao Zhang and Guanting Chen and Xiao Bi and Y. Wu and Y.K. Li and Fuli Luo and Yingfei Xiong and Wenfeng Liang},
61	  journal={arXiv preprint arXiv:2401.14196},
62	  year={2024},
63	  url={https://arxiv.org/abs/2401.14196},
64	}
65	
66	@inproceedings{wang2025dcsh,
67	  title={Do Code Semantics Help? A Comprehensive Study on Execution Trace-Based Information for Code Large Language Models},
68	  author={Jian Wang and Xiaofei Xie and Qiang Hu and Shangqing Liu and Yi Li},
69	  booktitle={Findings of the Association for Computational Linguistics: EMNLP 2025},
70	  year={2025},
71	  url={https://arxiv.org/abs/2509.11686},
72	}
73	
74	@inproceedings{ni2024next,
75	  title={NExT: Teaching Large Language Models to Reason about Code Execution},
76	  author={Ansong Ni and Miltiadis Allamanis and Arman Cohan and Yinlin Deng and Kensen Shi and Charles Sutton and Pengcheng Yin},
77	  booktitle={Proceedings of the 41st International Conference on Machine Learning (ICML)},
78	  year={2024},
79	  url={https://arxiv.org/abs/2404.14662},
80	}
81	
82	@inproceedings{eguchi2025etcot,
83	  title={Making LLMs Program Interpreters via Execution Trace Chain of Thought},
84	  author={Koshi Eguchi and Takuya Akiba},
85	  booktitle={ICML 2025 Workshop on Programmatic Representations for Agent Learning (PRAL)},
86	  year={2025},
87	}
88	
89	@article{ferrando2025execute,
90	  title={What I Cannot Execute, I Do Not Understand: Training and Evaluating {LLMs} on Program Execution Traces},
91	  author={Jordi Armengol-Estape and Quentin Carbonneaux and Tianjun Zhang and Aram H. Markosyan and Volker Seeker and Chris Cummins and Melanie Kambadur and Michael F.P. O'Boyle and Sida Wang and Gabriel Synnaeve and Hugh Leather},
92	  journal={arXiv preprint arXiv:2503.05703},
93	  year={2025},
94	  url={https://arxiv.org/abs/2503.05703},
95	}
96	
97	@inproceedings{xu2025cruxevalx,
98	  title={{CRUXEval-X}: A Benchmark for Multilingual Code Reasoning, Understanding and Execution},
99	  author={Ruiyang Xu and others},
100	  booktitle={Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics (ACL)},
101	  year={2025},
102	  url={https://arxiv.org/abs/2408.13001},
103	}
104	
105	@article{appt2024,
106	  title={{APPT}: Boosting Automated Patch Correctness Prediction via Fine-tuning Pre-trained Models},
107	  author={Quanjun Zhang and Chunrong Fang and Weisong Sun and Yan Liu and Tieke He and Xiaodong Hao and Zhenyu Chen},
108	  journal={IEEE Transactions on Software Engineering},
109	  year={2024},
110	  volume={50},
111	  number={3},
112	}
113	
114	@article{zhou2024llm4patch,
115	  title={Leveraging Large Language Model for Automatic Patch Correctness Assessment},
116	  author={Xin Zhou and Bowen Xu and Kisub Kim and DongGyun Han and Hung Huu Nguyen and Thanh Le-Cong and Junda He and Bach Le and David Lo},
117	  journal={IEEE Transactions on Software Engineering},
118	  year={2024},
119	  volume={50},
120	  number={11},
121	}
122	
123	@inproceedings{spiess2025calibration,
124	  title={Calibration and Correctness of Language Models for Code},
125	  author={Claudio Spiess and David Gros and others},
126	  booktitle={Proceedings of the 47th IEEE/ACM International Conference on Software Engineering (ICSE)},
127	  year={2025},
128	  url={https://arxiv.org/abs/2402.02047},
129	}
130	
131	@inproceedings{foster2025mutation,
132	  title={Mutation-Guided {LLM}-based Test Generation at Meta},
133	  author={Christopher Foster and others},
134	  booktitle={Proceedings of the ACM International Conference on the Foundations of Software Engineering (FSE), Industry Track},
135	  year={2025},
136	  url={https://arxiv.org/abs/2501.12862},
137	}
138	
139	@inproceedings{widyasari2024fusefl,
140	  title={Demystifying Faulty Code: Step-by-Step Reasoning for Explainable Fault Localization},
141	  author={Ratnadira Widyasari and Jia Wei Ang and Truong Giang Nguyen and Neil Sharma and David Lo},
142	  booktitle={Proceedings of the IEEE International Conference on Software Analysis, Evolution and Reengineering (SANER)},
143	  year={2024},
144	}
145	
146	@inproceedings{huang2026tracecoder,
147	  title={{TraceCoder}: A Trace-Driven Multi-Agent Framework for Automated Debugging of {LLM}-Generated Code},
148	  author={Jiangping Huang and Wenguang Ye and Weisong Sun and Jian Zhang and Mingyue Zhang and Yang Liu},
149	  booktitle={Proceedings of the 48th IEEE/ACM International Conference on Software Engineering (ICSE)},
150	  year={2026},
151	  url={https://arxiv.org/abs/2602.06875},
152	}
153	
154	@article{wang2025inspectcoder,
155	  title={{InspectCoder}: Dynamic Analysis-Enabled Self Repair through Interactive {LLM}-Debugger Collaboration},
156	  author={Yunkun Wang and Yue Zhang and Guochang Li and Chen Zhi and Binhua Li and Fei Huang and Yongbin Li and Shuiguang Deng},
157	  journal={arXiv preprint arXiv:2510.18327},
158	  year={2025},
159	  url={https://arxiv.org/abs/2510.18327},
160	}
161	
162	@inproceedings{haque2025traces,
163	  title={Towards Effectively Leveraging Execution Traces for Program Repair with Code {LLMs}},
164	  author={Mirazul Haque and Petr Babkin and Farima Farmahinifarahani and Manuela Veloso},
165	  booktitle={KnowledgeNLP Workshop at ACL 2025},
166	  year={2025},
167	  url={https://arxiv.org/abs/2505.04441},
168	}
169	
170	@inproceedings{yang2024generalization,
171	  title={Unveiling the Generalization Power of Fine-Tuned Large Language Models},
172	  author={Haoran Yang and Yumeng Zhang and Jiaqi Xu and Hongyuan Lu and Pheng Ann Heng and Wai Lam},
173	  booktitle={Proceedings of the 2024 Conference of the North American Chapter of the Association for Computational Linguistics (NAACL)},
174	  year={2024},
175	  url={https://arxiv.org/abs/2403.09162},
176	}
177	
178	@inproceedings{dong2024composition,
179	  title={How Abilities in Large Language Models are Affected by Supervised Fine-tuning Data Composition},
180	  author={Guanting Dong and Hongyi Yuan and Keming Lu and Chengpeng Li and Mingfeng Xue and Dayiheng Liu and Wei Wang and Zheng Yuan and Chang Zhou and Jingren Zhou},
181	  booktitle={Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (ACL)},
182	  year={2024},
183	  url={https://arxiv.org/abs/2310.05492},
184	}
185	
186	@inproceedings{tian2024debugbench,
187	  title={{DebugBench}: Evaluating Debugging Capability of Large Language Models},
188	  author={Runchu Tian and Yining Ye and Yujia Qin and Xin Cong and Yankai Lin and Yinxu Pan and Yesai Wu and Haotian Hui and Weichuan Liu and Zhiyuan Liu and Maosong Sun},
189	  booktitle={Findings of the Association for Computational Linguistics: ACL 2024},
190	  year={2024},
191	  url={https://arxiv.org/abs/2401.04621},
192	}
193	
194	@article{abreu2007accuracy,
195	  title={On the Accuracy of Spectrum-based Fault Localization},
196	  author={Rui Abreu and Peter Zoeteweij and Arjan J.C. van Gemund},
197	  journal={Testing: Academic and Industrial Conference Practice and Research Techniques (MUTATION)},
198	  year={2007},
199	  doi={10.1109/TAIC.PART.2007.13},
200	}
201	
202	@inproceedings{jones2002visualization,
203	  title={Visualization of Test Information to Assist Fault Localization},
204	  author={James A. Jones and Mary Jean Harrold and John Stasko},
205	  booktitle={Proceedings of the 24th International Conference on Software Engineering (ICSE)},
206	  year={2002},
207	  doi={10.1145/581339.581397},
208	}
209	
210	@article{wong2014dstar,
211	  title={{DStar}: An Effective Spectrum-Based Fault Localization Technique},
212	  author={W. Eric Wong and Vidroha Debroy and Ruizhi Gao and Yihao Li},
213	  journal={Journal of Systems and Software},
214	  volume={91},
215	  pages={44--58},
216	  year={2014},
217	  doi={10.1016/j.jss.2013.12.020},
218	}
219	
220	@inproceedings{kang2024autofl,
221	  title={{AutoFL}: Automated Fault Localization via Large Language Models},
222	  author={Sungmin Kang and Gabin An and Shin Yoo},
223	  booktitle={Proceedings of the 46th IEEE/ACM International Conference on Software Engineering (ICSE)},
224	  year={2024},
225	  url={https://arxiv.org/abs/2305.16397},
226	}
227	
228	@inproceedings{qin2024agentfl,
229	  title={{AgentFL}: Scaling LLM-based Fault Localization to Project-Level Context},
230	  author={Yihao Qin and Shangwen Wang and Yiling Lou and Jinhao Dong and Kaixin Wang and Xiaoling Li and Xiaoguang Mao},
231	  booktitle={Proceedings of the 39th IEEE/ACM International Conference on Automated Software Engineering (ASE)},
232	  year={2024},
233	  url={https://arxiv.org/abs/2403.16362},
234	}
235	
236	@inproceedings{widyasari2024llm4fl,
237	  title={{LLM4FL}: An LLM-based Fault Localization Integrated Debugging Framework for Automated Program Repair},
238	  author={Ratnadira Widyasari and Gopi Krishnan Rajbahadur and Shin Hwei Tan and Xin Xia and David Lo},
239	  booktitle={Proceedings of the 47th IEEE/ACM International Conference on Software Engineering (ICSE)},
240	  year={2025},
241	}
242	
243	@inproceedings{mukherjee2025llmfl,
244	  title={Can Large Language Models Localize Faults like Developers? A Comprehensive Study},
245	  author={Soneya Binta Hossain and Nan Jiang and Qiang Zhou and Xiaopeng Li and Wen-Hao Chiang and Yingjun Lyu and Hoan Nguyen and Omer Tripp},
246	  booktitle={Proceedings of the 47th IEEE/ACM International Conference on Software Engineering (ICSE)},
247	  year={2025},
248	  url={https://arxiv.org/abs/2312.02986},
249	}
250	
251	@article{roziere2024code,
252	  title={Code Llama: Open Foundation Models for Code},
253	  author={Baptiste Rozi{\`e}re and Jonas Gehring and Fabian Gloeckle and Sten Sootla and Itai Gat and Xiaoqing Ellen Tan and Yossi Adi and Jingyu Liu and R{\'e}mi Lacroix and Tal Remez and J{\'e}r{\'e}my Rapin and Artyom Kozhevnikov and Ivan Evtimov and Joanna Bitton and Manish Bhatt and Cristian Canton Ferrer and Aaron Grattafiori and Wenhan Xiong and Alexandre D{\'e}fossez and Jade Copet and Faisal Azhar and Hugo Touvron and Louis Martin and Nicolas Usunier and Thomas Scialom and Gabriel Synnaeve},
254	  journal={arXiv preprint arXiv:2308.12950},
255	  year={2024},
256	}
257	
258	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8e91956e-2c4e-49b2-8ea9-ee78b7405253",
  "isSidechain": false,
  "promptId": "b73967ab-1e3d-4502-97ef-ede23a2a2cd7",
  "type": "user",
  "uuid": "f5720402-6ec2-42a1-9a57-f5f64b7e052a",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/references.bib",
      "content": "@inproceedings{chen2025tracepile,\n  title={Chain of Execution Supervision Promotes General Reasoning in Large Language Models},\n  author={Nuo Chen and Zehua Li and Keqin Bao and Junyang Lin and Dayiheng Liu},\n  booktitle={Advances in Neural Information Processing Systems (NeurIPS)},\n  year={2025},\n  url={https://arxiv.org/abs/2510.23629},\n}\n\n@inproceedings{ding2024traced,\n  title={TRACED: Execution-aware Pre-training for Source Code},\n  author={Yangruibo Ding and Ben Steenhoek and Kexin Pei and Gail Kaiser and Wei Le and Baishakhi Ray},\n  booktitle={Proceedings of the 46th IEEE/ACM International Conference on Software Engineering (ICSE)},\n  year={2024},\n  doi={10.1145/3597503.3608140},\n  url={https://arxiv.org/abs/2306.07487},\n}\n\n@article{chen2021evaluating,\n  title={Evaluating Large Language Models Trained on Code},\n  author={Chen, Mark and Tworek, Jerry and Jun, Heewoo and Yuan, Qiming and Pinto, Henrique Ponde de Oliveira and Kaplan, Jared and Edwards, Harri and Burda, Yuri and Joseph, Nicholas and Brockman, Greg and others},\n  journal={arXiv preprint arXiv:2107.03374},\n  year={2021},\n  url={https://arxiv.org/abs/2107.03374},\n}\n\n@article{austin2021program,\n  title={Program Synthesis with Large Language Models},\n  author={Austin, Jacob and Odena, Augustus and Nye, Maxwell and Bosma, Maarten and Michalewski, Henryk and Dohan, David and Jiang, Ellen and Cai, Carrie and Terry, Michael and Le, Quoc and Sutton, Charles},\n  journal={arXiv preprint arXiv:2108.07732},\n  year={2021},\n  url={https://arxiv.org/abs/2108.07732},\n}\n\n@inproceedings{gu2024cruxeval,\n  title={CRUXEval: A Benchmark for Code Reasoning, Understanding and Execution},\n  author={Alex Gu and Baptiste Rozi{\\`e}re and Hugh Leather and Armando Solar-Lezama and Gabriel Synnaeve and Sida I. Wang},\n  booktitle={Proceedings of the 41st International Conference on Machine Learning (ICML)},\n  year={2024},\n  url={https://arxiv.org/abs/2401.03065},\n}\n\n@inproceedings{hu2022lora,\n  title={LoRA: Low-Rank Adaptation of Large Language Models},\n  author={Edward J. Hu and Yelong Shen and Phillip Wallis and Zeyuan Allen-Zhu and Yuanzhi Li and Shean Wang and Lu Wang and Weizhu Chen},\n  booktitle={Proceedings of the 10th International Conference on Learning Representations (ICLR)},\n  year={2022},\n  url={https://arxiv.org/abs/2106.09685},\n}\n\n@article{qwen2025coder,\n  title={Qwen2.5-Coder Technical Report},\n  author={Qwen Team},\n  journal={arXiv preprint arXiv:2409.12186},\n  year={2024},\n  url={https://arxiv.org/abs/2409.12186},\n}\n\n@article{deepseek2024coder,\n  title={DeepSeek-Coder: When the Large Language Model Meets Programming -- The Rise of Code Intelligence},\n  author={Daya Guo and Qihao Zhu and Dejian Yang and Zhenda Xie and Kai Dong and Wentao Zhang and Guanting Chen and Xiao Bi and Y. Wu and Y.K. Li and Fuli Luo and Yingfei Xiong and Wenfeng Liang},\n  journal={arXiv preprint arXiv:2401.14196},\n  year={2024},\n  url={https://arxiv.org/abs/2401.14196},\n}\n\n@inproceedings{wang2025dcsh,\n  title={Do Code Semantics Help? A Comprehensive Study on Execution Trace-Based Information for Code Large Language Models},\n  author={Jian Wang and Xiaofei Xie and Qiang Hu and Shangqing Liu and Yi Li},\n  booktitle={Findings of the Association for Computational Linguistics: EMNLP 2025},\n  year={2025},\n  url={https://arxiv.org/abs/2509.11686},\n}\n\n@inproceedings{ni2024next,\n  title={NExT: Teaching Large Language Models to Reason about Code Execution},\n  author={Ansong Ni and Miltiadis Allamanis and Arman Cohan and Yinlin Deng and Kensen Shi and Charles Sutton and Pengcheng Yin},\n  booktitle={Proceedings of the 41st International Conference on Machine Learning (ICML)},\n  year={2024},\n  url={https://arxiv.org/abs/2404.14662},\n}\n\n@inproceedings{eguchi2025etcot,\n  title={Making LLMs Program Interpreters via Execution Trace Chain of Thought},\n  author={Koshi Eguchi and Takuya Akiba},\n  booktitle={ICML 2025 Workshop on Programmatic Representations for Agent Learning (PRAL)},\n  year={2025},\n}\n\n@article{ferrando2025execute,\n  title={What I Cannot Execute, I Do Not Understand: Training and Evaluating {LLMs} on Program Execution Traces},\n  author={Jordi Armengol-Estape and Quentin Carbonneaux and Tianjun Zhang and Aram H. Markosyan and Volker Seeker and Chris Cummins and Melanie Kambadur and Michael F.P. O'Boyle and Sida Wang and Gabriel Synnaeve and Hugh Leather},\n  journal={arXiv preprint arXiv:2503.05703},\n  year={2025},\n  url={https://arxiv.org/abs/2503.05703},\n}\n\n@inproceedings{xu2025cruxevalx,\n  title={{CRUXEval-X}: A Benchmark for Multilingual Code Reasoning, Understanding and Execution},\n  author={Ruiyang Xu and others},\n  booktitle={Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics (ACL)},\n  year={2025},\n  url={https://arxiv.org/abs/2408.13001},\n}\n\n@article{appt2024,\n  title={{APPT}: Boosting Automated Patch Correctness Prediction via Fine-tuning Pre-trained Models},\n  author={Quanjun Zhang and Chunrong Fang and Weisong Sun and Yan Liu and Tieke He and Xiaodong Hao and Zhenyu Chen},\n  journal={IEEE Transactions on Software Engineering},\n  year={2024},\n  volume={50},\n  number={3},\n}\n\n@article{zhou2024llm4patch,\n  title={Leveraging Large Language Model for Automatic Patch Correctness Assessment},\n  author={Xin Zhou and Bowen Xu and Kisub Kim and DongGyun Han and Hung Huu Nguyen and Thanh Le-Cong and Junda He and Bach Le and David Lo},\n  journal={IEEE Transactions on Software Engineering},\n  year={2024},\n  volume={50},\n  number={11},\n}\n\n@inproceedings{spiess2025calibration,\n  title={Calibration and Correctness of Language Models for Code},\n  author={Claudio Spiess and David Gros and others},\n  booktitle={Proceedings of the 47th IEEE/ACM International Conference on Software Engineering (ICSE)},\n  year={2025},\n  url={https://arxiv.org/abs/2402.02047},\n}\n\n@inproceedings{foster2025mutation,\n  title={Mutation-Guided {LLM}-based Test Generation at Meta},\n  author={Christopher Foster and others},\n  booktitle={Proceedings of the ACM International Conference on the Foundations of Software Engineering (FSE), Industry Track},\n  year={2025},\n  url={https://arxiv.org/abs/2501.12862},\n}\n\n@inproceedings{widyasari2024fusefl,\n  title={Demystifying Faulty Code: Step-by-Step Reasoning for Explainable Fault Localization},\n  author={Ratnadira Widyasari and Jia Wei Ang and Truong Giang Nguyen and Neil Sharma and David Lo},\n  booktitle={Proceedings of the IEEE International Conference on Software Analysis, Evolution and Reengineering (SANER)},\n  year={2024},\n}\n\n@inproceedings{huang2026tracecoder,\n  title={{TraceCoder}: A Trace-Driven Multi-Agent Framework for Automated Debugging of {LLM}-Generated Code},\n  author={Jiangping Huang and Wenguang Ye and Weisong Sun and Jian Zhang and Mingyue Zhang and Yang Liu},\n  booktitle={Proceedings of the 48th IEEE/ACM International Conference on Software Engineering (ICSE)},\n  year={2026},\n  url={https://arxiv.org/abs/2602.06875},\n}\n\n@article{wang2025inspectcoder,\n  title={{InspectCoder}: Dynamic Analysis-Enabled Self Repair through Interactive {LLM}-Debugger Collaboration},\n  author={Yunkun Wang and Yue Zhang and Guochang Li and Chen Zhi and Binhua Li and Fei Huang and Yongbin Li and Shuiguang Deng},\n  journal={arXiv preprint arXiv:2510.18327},\n  year={2025},\n  url={https://arxiv.org/abs/2510.18327},\n}\n\n@inproceedings{haque2025traces,\n  title={Towards Effectively Leveraging Execution Traces for Program Repair with Code {LLMs}},\n  author={Mirazul Haque and Petr Babkin and Farima Farmahinifarahani and Manuela Veloso},\n  booktitle={KnowledgeNLP Workshop at ACL 2025},\n  year={2025},\n  url={https://arxiv.org/abs/2505.04441},\n}\n\n@inproceedings{yang2024generalization,\n  title={Unveiling the Generalization Power of Fine-Tuned Large Language Models},\n  author={Haoran Yang and Yumeng Zhang and Jiaqi Xu and Hongyuan Lu and Pheng Ann Heng and Wai Lam},\n  booktitle={Proceedings of the 2024 Conference of the North American Chapter of the Association for Computational Linguistics (NAACL)},\n  year={2024},\n  url={https://arxiv.org/abs/2403.09162},\n}\n\n@inproceedings{dong2024composition,\n  title={How Abilities in Large Language Models are Affected by Supervised Fine-tuning Data Composition},\n  author={Guanting Dong and Hongyi Yuan and Keming Lu and Chengpeng Li and Mingfeng Xue and Dayiheng Liu and Wei Wang and Zheng Yuan and Chang Zhou and Jingren Zhou},\n  booktitle={Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (ACL)},\n  year={2024},\n  url={https://arxiv.org/abs/2310.05492},\n}\n\n@inproceedings{tian2024debugbench,\n  title={{DebugBench}: Evaluating Debugging Capability of Large Language Models},\n  author={Runchu Tian and Yining Ye and Yujia Qin and Xin Cong and Yankai Lin and Yinxu Pan and Yesai Wu and Haotian Hui and Weichuan Liu and Zhiyuan Liu and Maosong Sun},\n  booktitle={Findings of the Association for Computational Linguistics: ACL 2024},\n  year={2024},\n  url={https://arxiv.org/abs/2401.04621},\n}\n\n@article{abreu2007accuracy,\n  title={On the Accuracy of Spectrum-based Fault Localization},\n  author={Rui Abreu and Peter Zoeteweij and Arjan J.C. van Gemund},\n  journal={Testing: Academic and Industrial Conference Practice and Research Techniques (MUTATION)},\n  year={2007},\n  doi={10.1109/TAIC.PART.2007.13},\n}\n\n@inproceedings{jones2002visualization,\n  title={Visualization of Test Information to Assist Fault Localization},\n  author={James A. Jones and Mary Jean Harrold and John Stasko},\n  booktitle={Proceedings of the 24th International Conference on Software Engineering (ICSE)},\n  year={2002},\n  doi={10.1145/581339.581397},\n}\n\n@article{wong2014dstar,\n  title={{DStar}: An Effective Spectrum-Based Fault Localization Technique},\n  author={W. Eric Wong and Vidroha Debroy and Ruizhi Gao and Yihao Li},\n  journal={Journal of Systems and Software},\n  volume={91},\n  pages={44--58},\n  year={2014},\n  doi={10.1016/j.jss.2013.12.020},\n}\n\n@inproceedings{kang2024autofl,\n  title={{AutoFL}: Automated Fault Localization via Large Language Models},\n  author={Sungmin Kang and Gabin An and Shin Yoo},\n  booktitle={Proceedings of the 46th IEEE/ACM International Conference on Software Engineering (ICSE)},\n  year={2024},\n  url={https://arxiv.org/abs/2305.16397},\n}\n\n@inproceedings{qin2024agentfl,\n  title={{AgentFL}: Scaling LLM-based Fault Localization to Project-Level Context},\n  author={Yihao Qin and Shangwen Wang and Yiling Lou and Jinhao Dong and Kaixin Wang and Xiaoling Li and Xiaoguang Mao},\n  booktitle={Proceedings of the 39th IEEE/ACM International Conference on Automated Software Engineering (ASE)},\n  year={2024},\n  url={https://arxiv.org/abs/2403.16362},\n}\n\n@inproceedings{widyasari2024llm4fl,\n  title={{LLM4FL}: An LLM-based Fault Localization Integrated Debugging Framework for Automated Program Repair},\n  author={Ratnadira Widyasari and Gopi Krishnan Rajbahadur and Shin Hwei Tan and Xin Xia and David Lo},\n  booktitle={Proceedings of the 47th IEEE/ACM International Conference on Software Engineering (ICSE)},\n  year={2025},\n}\n\n@inproceedings{mukherjee2025llmfl,\n  title={Can Large Language Models Localize Faults like Developers? A Comprehensive Study},\n  author={Soneya Binta Hossain and Nan Jiang and Qiang Zhou and Xiaopeng Li and Wen-Hao Chiang and Yingjun Lyu and Hoan Nguyen and Omer Tripp},\n  booktitle={Proceedings of the 47th IEEE/ACM International Conference on Software Engineering (ICSE)},\n  year={2025},\n  url={https://arxiv.org/abs/2312.02986},\n}\n\n@article{roziere2024code,\n  title={Code Llama: Open Foundation Models for Code},\n  author={Baptiste Rozi{\\`e}re and Jonas Gehring and Fabian Gloeckle and Sten Sootla and Itai Gat and Xiaoqing Ellen Tan and Yossi Adi and Jingyu Liu and R{\\'e}mi Lacroix and Tal Remez and J{\\'e}r{\\'e}my Rapin and Artyom Kozhevnikov and Ivan Evtimov and Joanna Bitton and Manish Bhatt and Cristian Canton Ferrer and Aaron Grattafiori and Wenhan Xiong and Alexandre D{\\'e}fossez and Jade Copet and Faisal Azhar and Hugo Touvron and Louis Martin and Nicolas Usunier and Thomas Scialom and Gabriel Synnaeve},\n  journal={arXiv preprint arXiv:2308.12950},\n  year={2024},\n}\n\n",
      "numLines": 258,
      "startLine": 1,
      "totalLines": 258
    }
  },
  "sourceToolAssistantUUID": "8e91956e-2c4e-49b2-8ea9-ee78b7405253",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/.claude/sessions/review_reviewer_1_7624f219",
  "sessionId": "f76386b4-9d1f-4f92-b831-706bc4acd94d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Tool call

_source line 45 · 2026-05-17T18:02:30.210Z_

<details open><summary>🔧 Tool call — Read · `toolu_01YZV1137upxkodntquuULP1`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/arr_checklist.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f5720402-6ec2-42a1-9a57-f5f64b7e052a",
  "isSidechain": false,
  "requestId": "req_011Cb8abw3DPj1zas94zEgR9",
  "type": "assistant",
  "uuid": "81550500-391b-4e9b-a710-a4cff9da734c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/.claude/sessions/review_reviewer_1_7624f219",
  "sessionId": "f76386b4-9d1f-4f92-b831-706bc4acd94d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015sJnPGBywusXUZ9bSRGEjb",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 29501,
      "cache_read_input_tokens": 31210,
      "output_tokens": 254,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 29501,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 254,
          "cache_read_input_tokens": 31210,
          "cache_creation_input_tokens": 29501,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 29501
          },
          "type": "message"
        }
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

_source line 46_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[Round 1 审稿请求]: ## Round 1 审稿任务 — Reviewer 1  **你的审查侧重**: 方法严谨性 + 实验设计 + 统计有效性 + 可复现性  ### Venue 信息 - **目标**: EMNLP 2026 via ARR May 2026 cycle - **截止日期**: 2026-05-25 - **页数限制**: Long paper ≤ 8 页正文（不含…",
  "leafUuid": "3d7041e6-8d51-4f84-a77d-96068f3dacaa",
  "sessionId": "f76386b4-9d1f-4f92-b831-706bc4acd94d"
}
```

---


### Runtime record

_source line 47_

```json
{
  "type": "ai-title",
  "aiTitle": "Round 1 peer review for trace verdict prediction paper",
  "sessionId": "f76386b4-9d1f-4f92-b831-706bc4acd94d"
}
```

---


### Assistant

_source line 48 · 2026-05-17T18:02:33.707Z_

<details><summary>Logged reasoning block</summary>

```text
Now let me also verify references to check for any issues.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3d7041e6-8d51-4f84-a77d-96068f3dacaa",
  "isSidechain": false,
  "requestId": "req_011Cb8acT5yragwSnh1syJ9W",
  "type": "assistant",
  "uuid": "43f5da69-3017-4917-bbb8-4eae8c38d98c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/.claude/sessions/review_reviewer_1_7624f219",
  "sessionId": "f76386b4-9d1f-4f92-b831-706bc4acd94d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QFvvnUbi7yPaLARZgrUCRi",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7190,
      "cache_read_input_tokens": 60711,
      "output_tokens": 150,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 7190,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 150,
          "cache_read_input_tokens": 60711,
          "cache_creation_input_tokens": 7190,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 7190
          },
          "type": "message"
        }
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

_source line 49 · 2026-05-17T18:02:34.181Z_

运行引用验证。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "43f5da69-3017-4917-bbb8-4eae8c38d98c",
  "isSidechain": false,
  "requestId": "req_011Cb8acT5yragwSnh1syJ9W",
  "type": "assistant",
  "uuid": "7bf409fe-c70b-428f-bec0-fd0c01801685",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/.claude/sessions/review_reviewer_1_7624f219",
  "sessionId": "f76386b4-9d1f-4f92-b831-706bc4acd94d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QFvvnUbi7yPaLARZgrUCRi",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7190,
      "cache_read_input_tokens": 60711,
      "output_tokens": 150,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 7190,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 150,
          "cache_read_input_tokens": 60711,
          "cache_creation_input_tokens": 7190,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 7190
          },
          "type": "message"
        }
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

_source line 50 · 2026-05-17T18:02:35.793Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__verify_references · `toolu_016gGesLP7ZGkefbS64YYi29`</summary>

```json
{
  "paper_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper",
  "project": "trace-verdict-study"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7bf409fe-c70b-428f-bec0-fd0c01801685",
  "isSidechain": false,
  "requestId": "req_011Cb8acT5yragwSnh1syJ9W",
  "type": "assistant",
  "uuid": "9d4da9da-9f51-4380-9e55-e298fbe6755f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/.claude/sessions/review_reviewer_1_7624f219",
  "sessionId": "f76386b4-9d1f-4f92-b831-706bc4acd94d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QFvvnUbi7yPaLARZgrUCRi",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7190,
      "cache_read_input_tokens": 60711,
      "output_tokens": 150,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 7190,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 150,
          "cache_read_input_tokens": 60711,
          "cache_creation_input_tokens": 7190,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 7190
          },
          "type": "message"
        }
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

_source line 51 · 2026-05-17T18:06:53.922Z_

<details><summary>↩ Tool result · `toolu_016gGesLP7ZGkefbS64YYi29`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"summary\": {\"total_bib_entries\": 32, \"total_citations\": 45, \"unique_cited_keys\": 31, \"orphan_bib\": 1, \"missing_bib\": 0, \"duplicate_keys\": 0, \"online_verified\": 21, \"online_not_found\": 6, \"online_mismatch\": 4}, \"cross_check\": {\"orphan_bib\": [\"dong2024composition\"], \"missing_bib\": [], \"orphan_count\": 1, \"missing_count\": 0}, \"bib_entries\": [{\"key\": \"chen2025tracepile\", \"type\": \"inproceedings\", \"title\": \"Chain of Execution Supervision Promotes General Reasoning in Large Language Models\", \"authors\": \"Nuo Chen and Zehua Li and Keqin Bao and Junyang Lin and Dayiheng Liu\", \"year\": \"2025\", \"venue\": \"Advances in Neural Information Processing Systems (NeurIPS)\"}, {\"key\": \"ding2024traced\", \"type\": \"inproceedings\", \"title\": \"TRACED: Execution-aware Pre-training for Source Code\", \"authors\": \"Yangruibo Ding and Ben Steenhoek and Kexin Pei and Gail Kaiser and Wei Le and Ba...\", \"year\": \"2024\", \"venue\": \"Proceedings of the 46th IEEE/ACM International Conference on Software Engineerin...\"}, {\"key\": \"chen2021evaluating\", \"type\": \"article\", \"title\": \"Evaluating Large Language Models Trained on Code\", \"authors\": \"Chen, Mark and Tworek, Jerry and Jun, Heewoo and Yuan, Qiming and Pinto, Henriqu...\", \"year\": \"2021\", \"venue\": \"arXiv preprint arXiv:2107.03374\"}, {\"key\": \"austin2021program\", \"type\": \"article\", \"title\": \"Program Synthesis with Large Language Models\", \"authors\": \"Austin, Jacob and Odena, Augustus and Nye, Maxwell and Bosma, Maarten and Michal...\", \"year\": \"2021\", \"venue\": \"arXiv preprint arXiv:2108.07732\"}, {\"key\": \"gu2024cruxeval\", \"type\": \"inproceedings\", \"title\": \"CRUXEval: A Benchmark for Code Reasoning, Understanding and Execution\", \"authors\": \"Alex Gu and Baptiste Rozi\\\\`ere and Hugh Leather and Armando Solar-Lezama and Gab...\", \"year\": \"2024\", \"venue\": \"Proceedings of the 41st International Conference on Machine Learning (ICML)\"}, {\"key\": \"hu2022lora\", \"type\": \"inproceedings\", \"title\": \"LoRA: Low-Rank Adaptation of Large Language Models\", \"authors\": \"Edward J. Hu and Yelong Shen and Phillip Wallis and Zeyuan Allen-Zhu and Yuanzhi...\", \"year\": \"2022\", \"venue\": \"Proceedings of the 10th International Conference on Learning Representations (IC...\"}, {\"key\": \"qwen2025coder\", \"type\": \"article\", \"title\": \"Qwen2.5-Coder Technical Report\", \"authors\": \"Qwen Team\", \"year\": \"2024\", \"venue\": \"arXiv preprint arXiv:2409.12186\"}, {\"key\": \"deepseek2024coder\", \"type\": \"article\", \"title\": \"DeepSeek-Coder: When the Large Language Model Meets Programming -- The Rise of Code Intelligence\", \"authors\": \"Daya Guo and Qihao Zhu and Dejian Yang and Zhenda Xie and Kai Dong and Wentao Zh...\", \"year\": \"2024\", \"venue\": \"arXiv preprint arXiv:2401.14196\"}, {\"key\": \"wang2025dcsh\", \"type\": \"inproceedings\", \"title\": \"Do Code Semantics Help? A Comprehensive Study on Execution Trace-Based Information for Code Large Language Models\", \"authors\": \"Jian Wang and Xiaofei Xie and Qiang Hu and Shangqing Liu and Yi Li\", \"year\": \"2025\", \"venue\": \"Findings of the Association for Computational Linguistics: EMNLP 2025\"}, {\"key\": \"ni2024next\", \"type\": \"inproceedings\", \"title\": \"NExT: Teaching Large Language Models to Reason about Code Execution\", \"authors\": \"Ansong Ni and Miltiadis Allamanis and Arman Cohan and Yinlin Deng and Kensen Shi...\", \"year\": \"2024\", \"venue\": \"Proceedings of the 41st International Conference on Machine Learning (ICML)\"}, {\"key\": \"eguchi2025etcot\", \"type\": \"inproceedings\", \"title\": \"Making LLMs Program Interpreters via Execution Trace Chain of Thought\", \"authors\": \"Koshi Eguchi and Takuya Akiba\", \"year\": \"2025\", \"venue\": \"ICML 2025 Workshop on Programmatic Representations for Agent Learning (PRAL)\"}, {\"key\": \"ferrando2025execute\", \"type\": \"article\", \"title\": \"What I Cannot Execute, I Do Not Understand: Training and Evaluating LLMs on Program Execution Traces\", \"authors\": \"Jordi Armengol-Estape and Quentin Carbonneaux and Tianjun Zhang and Aram H. Mark...\", \"year\": \"2025\", \"venue\": \"arXiv preprint arXiv:2503.05703\"}, {\"key\": \"xu2025cruxevalx\", \"type\": \"inproceedings\", \"title\": \"CRUXEval-X: A Benchmark for Multilingual Code Reasoning, Understanding and Execution\", \"authors\": \"Ruiyang Xu and others\", \"year\": \"2025\", \"venue\": \"Proceedings of the 63rd Annual Meeting of the Association for Computational Ling...\"}, {\"key\": \"appt2024\", \"type\": \"article\", \"title\": \"APPT: Boosting Automated Patch Correctness Prediction via Fine-tuning Pre-trained Models\", \"authors\": \"Quanjun Zhang and Chunrong Fang and Weisong Sun and Yan Liu and Tieke He and Xia...\", \"year\": \"2024\", \"venue\": \"IEEE Transactions on Software Engineering\"}, {\"key\": \"zhou2024llm4patch\", \"type\": \"article\", \"title\": \"Leveraging Large Language Model for Automatic Patch Correctness Assessment\", \"authors\": \"Xin Zhou and Bowen Xu and Kisub Kim and DongGyun Han and Hung Huu Nguyen and Tha...\", \"year\": \"2024\", \"venue\": \"IEEE Transactions on Software Engineering\"}, {\"key\": \"spiess2025calibration\", \"type\": \"inproceedings\", \"title\": \"Calibration and Correctness of Language Models for Code\", \"authors\": \"Claudio Spiess and David Gros and others\", \"year\": \"2025\", \"venue\": \"Proceedings of the 47th IEEE/ACM International Conference on Software Engineerin...\"}, {\"key\": \"foster2025mutation\", \"type\": \"inproceedings\", \"title\": \"Mutation-Guided LLM-based Test Generation at Meta\", \"authors\": \"Christopher Foster and others\", \"year\": \"2025\", \"venue\": \"Proceedings of the ACM International Conference on the Foundations of Software E...\"}, {\"key\": \"widyasari2024fusefl\", \"type\": \"inproceedings\", \"title\": \"Demystifying Faulty Code: Step-by-Step Reasoning for Explainable Fault Localization\", \"authors\": \"Ratnadira Widyasari and Jia Wei Ang and Truong Giang Nguyen and Neil Sharma and ...\", \"year\": \"2024\", \"venue\": \"Proceedings of the IEEE International Conference on Software Analysis, Evolution...\"}, {\"key\": \"huang2026tracecoder\", \"type\": \"inproceedings\", \"title\": \"TraceCoder: A Trace-Driven Multi-Agent Framework for Automated Debugging of LLM-Generated Code\", \"authors\": \"Jiangping Huang and Wenguang Ye and Weisong Sun and Jian Zhang and Mingyue Zhang...\", \"year\": \"2026\", \"venue\": \"Proceedings of the 48th IEEE/ACM International Conference on Software Engineerin...\"}, {\"key\": \"wang2025inspectcoder\", \"type\": \"article\", \"title\": \"InspectCoder: Dynamic Analysis-Enabled Self Repair through Interactive LLM-Debugger Collaboration\", \"authors\": \"Yunkun Wang and Yue Zhang and Guochang Li and Chen Zhi and Binhua Li and Fei Hua...\", \"year\": \"2025\", \"venue\": \"arXiv preprint arXiv:2510.18327\"}, {\"key\": \"haque2025traces\", \"type\": \"inproceedings\", \"title\": \"Towards Effectively Leveraging Execution Traces for Program Repair with Code LLMs\", \"authors\": \"Mirazul Haque and Petr Babkin and Farima Farmahinifarahani and Manuela Veloso\", \"year\": \"2025\", \"venue\": \"KnowledgeNLP Workshop at ACL 2025\"}, {\"key\": \"yang2024generalization\", \"type\": \"inproceedings\", \"title\": \"Unveiling the Generalization Power of Fine-Tuned Large Language Models\", \"authors\": \"Haoran Yang and Yumeng Zhang and Jiaqi Xu and Hongyuan Lu and Pheng Ann Heng and...\", \"year\": \"2024\", \"venue\": \"Proceedings of the 2024 Conference of the North American Chapter of the Associat...\"}, {\"key\": \"dong2024composition\", \"type\": \"inproceedings\", \"title\": \"How Abilities in Large Language Models are Affected by Supervised Fine-tuning Data Composition\", \"authors\": \"Guanting Dong and Hongyi Yuan and Keming Lu and Chengpeng Li and Mingfeng Xue an...\", \"year\": \"2024\", \"venue\": \"Proceedings of the 62nd Annual Meeting of the Association for Computational Ling...\"}, {\"key\": \"tian2024debugbench\", \"type\": \"inproceedings\", \"title\": \"DebugBench: Evaluating Debugging Capability of Large Language Models\", \"authors\": \"Runchu Tian and Yining Ye and Yujia Qin and Xin Cong and Yankai Lin and Yinxu Pa...\", \"year\": \"2024\", \"venue\": \"Findings of the Association for Computational Linguistics: ACL 2024\"}, {\"key\": \"abreu2007accuracy\", \"type\": \"article\", \"title\": \"On the Accuracy of Spectrum-based Fault Localization\", \"authors\": \"Rui Abreu and Peter Zoeteweij and Arjan J.C. van Gemund\", \"year\": \"2007\", \"venue\": \"Testing: Academic and Industrial Conference Practice and Research Techniques (MU...\"}, {\"key\": \"jones2002visualization\", \"type\": \"inproceedings\", \"title\": \"Visualization of Test Information to Assist Fault Localization\", \"authors\": \"James A. Jones and Mary Jean Harrold and John Stasko\", \"year\": \"2002\", \"venue\": \"Proceedings of the 24th International Conference on Software Engineering (ICSE)\"}, {\"key\": \"wong2014dstar\", \"type\": \"article\", \"title\": \"DStar: An Effective Spectrum-Based Fault Localization Technique\", \"authors\": \"W. Eric Wong and Vidroha Debroy and Ruizhi Gao and Yihao Li\", \"year\": \"2014\", \"venue\": \"Journal of Systems and Software\"}, {\"key\": \"kang2024autofl\", \"type\": \"inproceedings\", \"title\": \"AutoFL: Automated Fault Localization via Large Language Models\", \"authors\": \"Sungmin Kang and Gabin An and Shin Yoo\", \"year\": \"2024\", \"venue\": \"Proceedings of the 46th IEEE/ACM International Conference on Software Engineerin...\"}, {\"key\": \"qin2024agentfl\", \"type\": \"inproceedings\", \"title\": \"AgentFL: Scaling LLM-based Fault Localization to Project-Level Context\", \"authors\": \"Yihao Qin and Shangwen Wang and Yiling Lou and Jinhao Dong and Kaixin Wang and X...\", \"year\": \"2024\", \"venue\": \"Proceedings of the 39th IEEE/ACM International Conference on Automated Software ...\"}, {\"key\": \"widyasari2024llm4fl\", \"type\": \"inproceedings\", \"title\": \"LLM4FL: An LLM-based Fault Localization Integrated Debugging Framework for Automated Program Repair\", \"authors\": \"Ratnadira Widyasari and Gopi Krishnan Rajbahadur and Shin Hwei Tan and Xin Xia a...\", \"year\": \"2025\", \"venue\": \"Proceedings of the 47th IEEE/ACM International Conference on Software Engineerin...\"}, {\"key\": \"mukherjee2025llmfl\", \"type\": \"inproceedings\", \"title\": \"Can Large Language Models Localize Faults like Developers? A Comprehensive Study\", \"authors\": \"Soneya Binta Hossain and Nan Jiang and Qiang Zhou and Xiaopeng Li and Wen-Hao Ch...\", \"year\": \"2025\", \"venue\": \"Proceedings of the 47th IEEE/ACM International Conference on Software Engineerin...\"}, {\"key\": \"roziere2024code\", \"type\": \"article\", \"title\": \"Code Llama: Open Foundation Models for Code\", \"authors\": \"Baptiste Rozi\\\\`ere and Jonas Gehring and Fabian Gloeckle and Sten Sootla and Ita...\", \"year\": \"2024\", \"venue\": \"arXiv preprint arXiv:2308.12950\"}], \"tex_citations\": [{\"key\": \"chen2025tracepile\", \"file\": \"introduction.tex\", \"line\": 3, \"command\": \"citep\"}, {\"key\": \"ding2024traced\", \"file\": \"introduction.tex\", \"line\": 3, \"command\": \"citep\"}, {\"key\": \"wang2025dcsh\", \"file\": \"introduction.tex\", \"line\": 3, \"command\": \"citep\"}, {\"key\": \"ni2024next\", \"file\": \"introduction.tex\", \"line\": 3, \"command\": \"citep\"}, {\"key\": \"wang2025dcsh\", \"file\": \"introduction.tex\", \"line\": 7, \"command\": \"citep\"}, {\"key\": \"chen2021evaluating\", \"file\": \"introduction.tex\", \"line\": 13, \"command\": \"citep\"}, {\"key\": \"austin2021program\", \"file\": \"introduction.tex\", \"line\": 13, \"command\": \"citep\"}, {\"key\": \"qwen2025coder\", \"file\": \"introduction.tex\", \"line\": 13, \"command\": \"citep\"}, {\"key\": \"roziere2024code\", \"file\": \"introduction.tex\", \"line\": 13, \"command\": \"citep\"}, {\"key\": \"deepseek2024coder\", \"file\": \"introduction.tex\", \"line\": 13, \"command\": \"citep\"}, {\"key\": \"chen2025tracepile\", \"file\": \"method.tex\", \"line\": 7, \"command\": \"citep\"}, {\"key\": \"gu2024cruxeval\", \"file\": \"method.tex\", \"line\": 7, \"command\": \"citep\"}, {\"key\": \"chen2021evaluating\", \"file\": \"method.tex\", \"line\": 12, \"command\": \"citep\"}, {\"key\": \"austin2021program\", \"file\": \"method.tex\", \"line\": 12, \"command\": \"citep\"}, {\"key\": \"qwen2025coder\", \"file\": \"method.tex\", \"line\": 38, \"command\": \"citep\"}, {\"key\": \"roziere2024code\", \"file\": \"method.tex\", \"line\": 38, \"command\": \"citep\"}, {\"key\": \"deepseek2024coder\", \"file\": \"method.tex\", \"line\": 38, \"command\": \"citep\"}, {\"key\": \"hu2022lora\", \"file\": \"method.tex\", \"line\": 39, \"command\": \"citep\"}, {\"key\": \"tian2024debugbench\", \"file\": \"experiments.tex\", \"line\": 168, \"command\": \"citep\"}, {\"key\": \"chen2025tracepile\", \"file\": \"related_work.tex\", \"line\": 4, \"command\": \"citep\"}, {\"key\": \"wang2025dcsh\", \"file\": \"related_work.tex\", \"line\": 4, \"command\": \"citet\"}, {\"key\": \"ni2024next\", \"file\": \"related_work.tex\", \"line\": 5, \"command\": \"citep\"}, {\"key\": \"eguchi2025etcot\", \"file\": \"related_work.tex\", \"line\": 5, \"command\": \"citep\"}, {\"key\": \"ferrando2025execute\", \"file\": \"related_work.tex\", \"line\": 6, \"command\": \"citet\"}, {\"key\": \"gu2024cruxeval\", \"file\": \"related_work.tex\", \"line\": 7, \"command\": \"citep\"}, {\"key\": \"xu2025cruxevalx\", \"file\": \"related_work.tex\", \"line\": 7, \"command\": \"citet\"}, {\"key\": \"ding2024traced\", \"file\": \"related_work.tex\", \"line\": 11, \"command\": \"citep\"}, {\"key\": \"appt2024\", \"file\": \"related_work.tex\", \"line\": 12, \"command\": \"citep\"}, {\"key\": \"zhou2024llm4patch\", \"file\": \"related_work.tex\", \"line\": 12, \"command\": \"citep\"}, {\"key\": \"widyasari2024fusefl\", \"file\": \"related_work.tex\", \"line\": 13, \"command\": \"citep\"}, {\"key\": \"foster2025mutation\", \"file\": \"related_work.tex\", \"line\": 14, \"command\": \"citet\"}, {\"key\": \"abreu2007accuracy\", \"file\": \"related_work.tex\", \"line\": 19, \"command\": \"citep\"}, {\"key\": \"jones2002visualization\", \"file\": \"related_work.tex\", \"line\": 19, \"command\": \"citep\"}, {\"key\": \"wong2014dstar\", \"file\": \"related_work.tex\", \"line\": 19, \"command\": \"citep\"}, {\"key\": \"kang2024autofl\", \"file\": \"related_work.tex\", \"line\": 20, \"command\": \"citep\"}, {\"key\": \"qin2024agentfl\", \"file\": \"related_work.tex\", \"line\": 20, \"command\": \"citep\"}, {\"key\": \"widyasari2024llm4fl\", \"file\": \"related_work.tex\", \"line\": 20, \"command\": \"citep\"}, {\"key\": \"mukherjee2025llmfl\", \"file\": \"related_work.tex\", \"line\": 20, \"command\": \"citet\"}, {\"key\": \"huang2026tracecoder\", \"file\": \"related_work.tex\", \"line\": 25, \"command\": \"citep\"}, {\"key\": \"wang2025inspectcoder\", \"file\": \"related_work.tex\", \"line\": 25, \"command\": \"citep\"}, {\"key\": \"haque2025traces\", \"file\": \"related_work.tex\", \"line\": 25, \"command\": \"citet\"}, {\"key\": \"hu2022lora\", \"file\": \"appendix.tex\", \"line\": 37, \"command\": \"citep\"}, {\"key\": \"spiess2025calibration\", \"file\": \"appendix.tex\", \"line\": 406, \"command\": \"citep\"}, {\"key\": \"tian2024debugbench\", \"file\": \"appendix.tex\", \"line\": 464, \"command\": \"citep\"}, {\"key\": \"yang2024generalization\", \"file\": \"appendix.tex\", \"line\": 502, \"command\": \"citep\"}], \"online_verification\": [{\"key\": \"chen2025tracepile\", \"title\": \"Chain of Execution Supervision Promotes General Reasoning in Large Language Models\", \"status\": \"error\", \"confidence\": 0.0, \"matched_title\": \"\", \"matched_year\": \"\", \"mismatch_fields\": [], \"note\": \"API request failed\"}, {\"key\": \"ding2024traced\", \"title\": \"TRACED: Execution-aware Pre-training for Source Code\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"TRACED: Execution-aware Pre-training for Source Code\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"chen2021evaluating\", \"title\": \"Evaluating Large Language Models Trained on Code\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Evaluating Large Language Models Trained on Code\", \"matched_year\": \"2021\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"austin2021program\", \"title\": \"Program Synthesis with Large Language Models\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Program Synthesis with Large Language Models\", \"matched_year\": \"2021\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"gu2024cruxeval\", \"title\": \"CRUXEval: A Benchmark for Code Reasoning, Understanding and Execution\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"CRUXEval: A Benchmark for Code Reasoning, Understanding and Execution\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"hu2022lora\", \"title\": \"LoRA: Low-Rank Adaptation of Large Language Models\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"LoRA: Low-Rank Adaptation of Large Language Models\", \"matched_year\": \"2021\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"qwen2025coder\", \"title\": \"Qwen2.5-Coder Technical Report\", \"status\": \"mismatch\", \"confidence\": 1.0, \"matched_title\": \"Qwen2.5-Coder Technical Report\", \"matched_year\": \"2024\", \"mismatch_fields\": [\"first_author: bib=team vs api=hui\"], \"note\": \"\"}, {\"key\": \"deepseek2024coder\", \"title\": \"DeepSeek-Coder: When the Large Language Model Meets Programming -- The Rise of Code Intelligence\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"DeepSeek-Coder: When the Large Language Model Meets Programming -- The Rise of Code Intelligence\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"wang2025dcsh\", \"title\": \"Do Code Semantics Help? A Comprehensive Study on Execution Trace-Based Information for Code Large Language Models\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Do Code Semantics Help? A Comprehensive Study on Execution Trace-Based Information for Code Large Language Models\", \"matched_year\": \"2025\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"ni2024next\", \"title\": \"NExT: Teaching Large Language Models to Reason about Code Execution\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"NExT: Teaching Large Language Models to Reason about Code Execution\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"eguchi2025etcot\", \"title\": \"Making LLMs Program Interpreters via Execution Trace Chain of Thought\", \"status\": \"not_found\", \"confidence\": 0.321, \"matched_title\": \"Enriching Location Representation with Detailed Semantic Information\", \"matched_year\": \"\", \"mismatch_fields\": [], \"note\": \"best match similarity 0.32 below threshold 0.82\"}, {\"key\": \"ferrando2025execute\", \"title\": \"What I Cannot Execute, I Do Not Understand: Training and Evaluating LLMs on Program Execution Traces\", \"status\": \"not_found\", \"confidence\": 0.199, \"matched_title\": \"Sparks of Artificial General Intelligence: Early experiments with GPT-4\", \"matched_year\": \"\", \"mismatch_fields\": [], \"note\": \"best match similarity 0.20 below threshold 0.82\"}, {\"key\": \"xu2025cruxevalx\", \"title\": \"CRUXEval-X: A Benchmark for Multilingual Code Reasoning, Understanding and Execution\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"CRUXEVAL-X: A Benchmark for Multilingual Code Reasoning, Understanding and Execution\", \"matched_year\": \"2025\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"appt2024\", \"title\": \"APPT: Boosting Automated Patch Correctness Prediction via Fine-tuning Pre-trained Models\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"APPT: Boosting Automated Patch Correctness Prediction via Fine-Tuning Pre-Trained Models\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"zhou2024llm4patch\", \"title\": \"Leveraging Large Language Model for Automatic Patch Correctness Assessment\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Leveraging Large Language Model for Automatic Patch Correctness Assessment\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"spiess2025calibration\", \"title\": \"Calibration and Correctness of Language Models for Code\", \"status\": \"mismatch\", \"confidence\": 1.0, \"matched_title\": \"Calibration and Correctness of Language Models for Code\", \"matched_year\": \"2025\", \"mismatch_fields\": [\"first_author: bib=spiess vs api=spieß\"], \"note\": \"\"}, {\"key\": \"foster2025mutation\", \"title\": \"Mutation-Guided LLM-based Test Generation at Meta\", \"status\": \"mismatch\", \"confidence\": 1.0, \"matched_title\": \"Mutation-Guided LLM-based Test Generation at Meta\", \"matched_year\": \"2025\", \"mismatch_fields\": [\"first_author: bib=foster vs api=harman\"], \"note\": \"\"}, {\"key\": \"widyasari2024fusefl\", \"title\": \"Demystifying Faulty Code: Step-by-Step Reasoning for Explainable Fault Localization\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Demystifying Faulty Code: Step-by-Step Reasoning for Explainable Fault Localization\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"huang2026tracecoder\", \"title\": \"TraceCoder: A Trace-Driven Multi-Agent Framework for Automated Debugging of LLM-Generated Code\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"TraceCoder: A Trace-Driven Multi-Agent Framework for Automated Debugging of LLM-Generated Code\", \"matched_year\": \"2026\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"wang2025inspectcoder\", \"title\": \"InspectCoder: Dynamic Analysis-Enabled Self Repair through Interactive LLM-Debugger Collaboration\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"InspectCoder: Dynamic Analysis-Enabled Self Repair through interactive LLM-Debugger Collaboration\", \"matched_year\": \"2025\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"haque2025traces\", \"title\": \"Towards Effectively Leveraging Execution Traces for Program Repair with Code LLMs\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Towards Effectively Leveraging Execution Traces for Program Repair with Code LLMs\", \"matched_year\": \"2025\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"yang2024generalization\", \"title\": \"Unveiling the Generalization Power of Fine-Tuned Large Language Models\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Unveiling the Generalization Power of Fine-Tuned Large Language Models\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"dong2024composition\", \"title\": \"How Abilities in Large Language Models are Affected by Supervised Fine-tuning Data Composition\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"How Abilities in Large Language Models are Affected by Supervised Fine-tuning Data Composition\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"tian2024debugbench\", \"title\": \"DebugBench: Evaluating Debugging Capability of Large Language Models\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"DebugBench: Evaluating Debugging Capability of Large Language Models\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"abreu2007accuracy\", \"title\": \"On the Accuracy of Spectrum-based Fault Localization\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"On the Accuracy of Spectrum-based Fault Localization\", \"matched_year\": \"2007\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"jones2002visualization\", \"title\": \"Visualization of Test Information to Assist Fault Localization\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Visualization of test information to assist fault localization\", \"matched_year\": \"2002\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"wong2014dstar\", \"title\": \"DStar: An Effective Spectrum-Based Fault Localization Technique\", \"status\": \"not_found\", \"confidence\": 0.561, \"matched_title\": \"MSFL: A Model for Fault Localization Using Mutation-Spectra Technique\", \"matched_year\": \"\", \"mismatch_fields\": [], \"note\": \"best match similarity 0.56 below threshold 0.82\"}, {\"key\": \"kang2024autofl\", \"title\": \"AutoFL: Automated Fault Localization via Large Language Models\", \"status\": \"not_found\", \"confidence\": 0.45, \"matched_title\": \"A Survey on Large Language Models for Software Engineering\", \"matched_year\": \"\", \"mismatch_fields\": [], \"note\": \"best match similarity 0.45 below threshold 0.82\"}, {\"key\": \"qin2024agentfl\", \"title\": \"AgentFL: Scaling LLM-based Fault Localization to Project-Level Context\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"AgentFL: Scaling LLM-based Fault Localization to Project-Level Context\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"widyasari2024llm4fl\", \"title\": \"LLM4FL: An LLM-based Fault Localization Integrated Debugging Framework for Automated Program Repair\", \"status\": \"not_found\", \"confidence\": 0.448, \"matched_title\": \"A Multi-Agent Approach to Fault Localization via Graph-Based Retrieval and Reflexion\", \"matched_year\": \"\", \"mismatch_fields\": [], \"note\": \"best match similarity 0.45 below threshold 0.82\"}, {\"key\": \"mukherjee2025llmfl\", \"title\": \"Can Large Language Models Localize Faults like Developers? A Comprehensive Study\", \"status\": \"not_found\", \"confidence\": 0.186, \"matched_title\": \"Internet of Things (IoT): A vision, architectural elements, and future directions\", \"matched_year\": \"\", \"mismatch_fields\": [], \"note\": \"best match similarity 0.19 below threshold 0.82\"}, {\"key\": \"roziere2024code\", \"title\": \"Code Llama: Open Foundation Models for Code\", \"status\": \"mismatch\", \"confidence\": 1.0, \"matched_title\": \"Code Llama: Open Foundation Models for Code\", \"matched_year\": \"2023\", \"mismatch_fields\": [\"first_author: bib=rozi\\\\`ere vs api=rozière\"], \"note\": \"\"}]}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9d4da9da-9f51-4380-9e55-e298fbe6755f",
  "isSidechain": false,
  "promptId": "b73967ab-1e3d-4502-97ef-ede23a2a2cd7",
  "type": "user",
  "uuid": "d3ff5948-ee0e-41d5-98e8-61644311e2b5",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"summary\\\": {\\\"total_bib_entries\\\": 32, \\\"total_citations\\\": 45, \\\"unique_cited_keys\\\": 31, \\\"orphan_bib\\\": 1, \\\"missing_bib\\\": 0, \\\"duplicate_keys\\\": 0, \\\"online_verified\\\": 21, \\\"online_not_found\\\": 6, \\\"online_mismatch\\\": 4}, \\\"cross_check\\\": {\\\"orphan_bib\\\": [\\\"dong2024composition\\\"], \\\"missing_bib\\\": [], \\\"orphan_count\\\": 1, \\\"missing_count\\\": 0}, \\\"bib_entries\\\": [{\\\"key\\\": \\\"chen2025tracepile\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Chain of Execution Supervision Promotes General Reasoning in Large Language Models\\\", \\\"authors\\\": \\\"Nuo Chen and Zehua Li and Keqin Bao and Junyang Lin and Dayiheng Liu\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"Advances in Neural Information Processing Systems (NeurIPS)\\\"}, {\\\"key\\\": \\\"ding2024traced\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"TRACED: Execution-aware Pre-training for Source Code\\\", \\\"authors\\\": \\\"Yangruibo Ding and Ben Steenhoek and Kexin Pei and Gail Kaiser and Wei Le and Ba...\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"Proceedings of the 46th IEEE/ACM International Conference on Software Engineerin...\\\"}, {\\\"key\\\": \\\"chen2021evaluating\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Evaluating Large Language Models Trained on Code\\\", \\\"authors\\\": \\\"Chen, Mark and Tworek, Jerry and Jun, Heewoo and Yuan, Qiming and Pinto, Henriqu...\\\", \\\"year\\\": \\\"2021\\\", \\\"venue\\\": \\\"arXiv preprint arXiv:2107.03374\\\"}, {\\\"key\\\": \\\"austin2021program\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Program Synthesis with Large Language Models\\\", \\\"authors\\\": \\\"Austin, Jacob and Odena, Augustus and Nye, Maxwell and Bosma, Maarten and Michal...\\\", \\\"year\\\": \\\"2021\\\", \\\"venue\\\": \\\"arXiv preprint arXiv:2108.07732\\\"}, {\\\"key\\\": \\\"gu2024cruxeval\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"CRUXEval: A Benchmark for Code Reasoning, Understanding and Execution\\\", \\\"authors\\\": \\\"Alex Gu and Baptiste Rozi\\\\\\\\`ere and Hugh Leather and Armando Solar-Lezama and Gab...\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"Proceedings of the 41st International Conference on Machine Learning (ICML)\\\"}, {\\\"key\\\": \\\"hu2022lora\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"LoRA: Low-Rank Adaptation of Large Language Models\\\", \\\"authors\\\": \\\"Edward J. Hu and Yelong Shen and Phillip Wallis and Zeyuan Allen-Zhu and Yuanzhi...\\\", \\\"year\\\": \\\"2022\\\", \\\"venue\\\": \\\"Proceedings of the 10th International Conference on Learning Representations (IC...\\\"}, {\\\"key\\\": \\\"qwen2025coder\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Qwen2.5-Coder Technical Report\\\", \\\"authors\\\": \\\"Qwen Team\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"arXiv preprint arXiv:2409.12186\\\"}, {\\\"key\\\": \\\"deepseek2024coder\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"DeepSeek-Coder: When the Large Language Model Meets Programming -- The Rise of Code Intelligence\\\", \\\"authors\\\": \\\"Daya Guo and Qihao Zhu and Dejian Yang and Zhenda Xie and Kai Dong and Wentao Zh...\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"arXiv preprint arXiv:2401.14196\\\"}, {\\\"key\\\": \\\"wang2025dcsh\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Do Code Semantics Help? A Comprehensive Study on Execution Trace-Based Information for Code Large Language Models\\\", \\\"authors\\\": \\\"Jian Wang and Xiaofei Xie and Qiang Hu and Shangqing Liu and Yi Li\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"Findings of the Association for Computational Linguistics: EMNLP 2025\\\"}, {\\\"key\\\": \\\"ni2024next\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"NExT: Teaching Large Language Models to Reason about Code Execution\\\", \\\"authors\\\": \\\"Ansong Ni and Miltiadis Allamanis and Arman Cohan and Yinlin Deng and Kensen Shi...\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"Proceedings of the 41st International Conference on Machine Learning (ICML)\\\"}, {\\\"key\\\": \\\"eguchi2025etcot\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Making LLMs Program Interpreters via Execution Trace Chain of Thought\\\", \\\"authors\\\": \\\"Koshi Eguchi and Takuya Akiba\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"ICML 2025 Workshop on Programmatic Representations for Agent Learning (PRAL)\\\"}, {\\\"key\\\": \\\"ferrando2025execute\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"What I Cannot Execute, I Do Not Understand: Training and Evaluating LLMs on Program Execution Traces\\\", \\\"authors\\\": \\\"Jordi Armengol-Estape and Quentin Carbonneaux and Tianjun Zhang and Aram H. Mark...\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"arXiv preprint arXiv:2503.05703\\\"}, {\\\"key\\\": \\\"xu2025cruxevalx\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"CRUXEval-X: A Benchmark for Multilingual Code Reasoning, Understanding and Execution\\\", \\\"authors\\\": \\\"Ruiyang Xu and others\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"Proceedings of the 63rd Annual Meeting of the Association for Computational Ling...\\\"}, {\\\"key\\\": \\\"appt2024\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"APPT: Boosting Automated Patch Correctness Prediction via Fine-tuning Pre-trained Models\\\", \\\"authors\\\": \\\"Quanjun Zhang and Chunrong Fang and Weisong Sun and Yan Liu and Tieke He and Xia...\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"IEEE Transactions on Software Engineering\\\"}, {\\\"key\\\": \\\"zhou2024llm4patch\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Leveraging Large Language Model for Automatic Patch Correctness Assessment\\\", \\\"authors\\\": \\\"Xin Zhou and Bowen Xu and Kisub Kim and DongGyun Han and Hung Huu Nguyen and Tha...\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"IEEE Transactions on Software Engineering\\\"}, {\\\"key\\\": \\\"spiess2025calibration\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Calibration and Correctness of Language Models for Code\\\", \\\"authors\\\": \\\"Claudio Spiess and David Gros and others\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"Proceedings of the 47th IEEE/ACM International Conference on Software Engineerin...\\\"}, {\\\"key\\\": \\\"foster2025mutation\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Mutation-Guided LLM-based Test Generation at Meta\\\", \\\"authors\\\": \\\"Christopher Foster and others\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"Proceedings of the ACM International Conference on the Foundations of Software E...\\\"}, {\\\"key\\\": \\\"widyasari2024fusefl\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Demystifying Faulty Code: Step-by-Step Reasoning for Explainable Fault Localization\\\", \\\"authors\\\": \\\"Ratnadira Widyasari and Jia Wei Ang and Truong Giang Nguyen and Neil Sharma and ...\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"Proceedings of the IEEE International Conference on Software Analysis, Evolution...\\\"}, {\\\"key\\\": \\\"huang2026tracecoder\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"TraceCoder: A Trace-Driven Multi-Agent Framework for Automated Debugging of LLM-Generated Code\\\", \\\"authors\\\": \\\"Jiangping Huang and Wenguang Ye and Weisong Sun and Jian Zhang and Mingyue Zhang...\\\", \\\"year\\\": \\\"2026\\\", \\\"venue\\\": \\\"Proceedings of the 48th IEEE/ACM International Conference on Software Engineerin...\\\"}, {\\\"key\\\": \\\"wang2025inspectcoder\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"InspectCoder: Dynamic Analysis-Enabled Self Repair through Interactive LLM-Debugger Collaboration\\\", \\\"authors\\\": \\\"Yunkun Wang and Yue Zhang and Guochang Li and Chen Zhi and Binhua Li and Fei Hua...\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"arXiv preprint arXiv:2510.18327\\\"}, {\\\"key\\\": \\\"haque2025traces\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Towards Effectively Leveraging Execution Traces for Program Repair with Code LLMs\\\", \\\"authors\\\": \\\"Mirazul Haque and Petr Babkin and Farima Farmahinifarahani and Manuela Veloso\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"KnowledgeNLP Workshop at ACL 2025\\\"}, {\\\"key\\\": \\\"yang2024generalization\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Unveiling the Generalization Power of Fine-Tuned Large Language Models\\\", \\\"authors\\\": \\\"Haoran Yang and Yumeng Zhang and Jiaqi Xu and Hongyuan Lu and Pheng Ann Heng and...\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"Proceedings of the 2024 Conference of the North American Chapter of the Associat...\\\"}, {\\\"key\\\": \\\"dong2024composition\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"How Abilities in Large Language Models are Affected by Supervised Fine-tuning Data Composition\\\", \\\"authors\\\": \\\"Guanting Dong and Hongyi Yuan and Keming Lu and Chengpeng Li and Mingfeng Xue an...\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"Proceedings of the 62nd Annual Meeting of the Association for Computational Ling...\\\"}, {\\\"key\\\": \\\"tian2024debugbench\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"DebugBench: Evaluating Debugging Capability of Large Language Models\\\", \\\"authors\\\": \\\"Runchu Tian and Yining Ye and Yujia Qin and Xin Cong and Yankai Lin and Yinxu Pa...\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"Findings of the Association for Computational Linguistics: ACL 2024\\\"}, {\\\"key\\\": \\\"abreu2007accuracy\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"On the Accuracy of Spectrum-based Fault Localization\\\", \\\"authors\\\": \\\"Rui Abreu and Peter Zoeteweij and Arjan J.C. van Gemund\\\", \\\"year\\\": \\\"2007\\\", \\\"venue\\\": \\\"Testing: Academic and Industrial Conference Practice and Research Techniques (MU...\\\"}, {\\\"key\\\": \\\"jones2002visualization\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Visualization of Test Information to Assist Fault Localization\\\", \\\"authors\\\": \\\"James A. Jones and Mary Jean Harrold and John Stasko\\\", \\\"year\\\": \\\"2002\\\", \\\"venue\\\": \\\"Proceedings of the 24th International Conference on Software Engineering (ICSE)\\\"}, {\\\"key\\\": \\\"wong2014dstar\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"DStar: An Effective Spectrum-Based Fault Localization Technique\\\", \\\"authors\\\": \\\"W. Eric Wong and Vidroha Debroy and Ruizhi Gao and Yihao Li\\\", \\\"year\\\": \\\"2014\\\", \\\"venue\\\": \\\"Journal of Systems and Software\\\"}, {\\\"key\\\": \\\"kang2024autofl\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"AutoFL: Automated Fault Localization via Large Language Models\\\", \\\"authors\\\": \\\"Sungmin Kang and Gabin An and Shin Yoo\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"Proceedings of the 46th IEEE/ACM International Conference on Software Engineerin...\\\"}, {\\\"key\\\": \\\"qin2024agentfl\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"AgentFL: Scaling LLM-based Fault Localization to Project-Level Context\\\", \\\"authors\\\": \\\"Yihao Qin and Shangwen Wang and Yiling Lou and Jinhao Dong and Kaixin Wang and X...\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"Proceedings of the 39th IEEE/ACM International Conference on Automated Software ...\\\"}, {\\\"key\\\": \\\"widyasari2024llm4fl\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"LLM4FL: An LLM-based Fault Localization Integrated Debugging Framework for Automated Program Repair\\\", \\\"authors\\\": \\\"Ratnadira Widyasari and Gopi Krishnan Rajbahadur and Shin Hwei Tan and Xin Xia a...\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"Proceedings of the 47th IEEE/ACM International Conference on Software Engineerin...\\\"}, {\\\"key\\\": \\\"mukherjee2025llmfl\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Can Large Language Models Localize Faults like Developers? A Comprehensive Study\\\", \\\"authors\\\": \\\"Soneya Binta Hossain and Nan Jiang and Qiang Zhou and Xiaopeng Li and Wen-Hao Ch...\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"Proceedings of the 47th IEEE/ACM International Conference on Software Engineerin...\\\"}, {\\\"key\\\": \\\"roziere2024code\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Code Llama: Open Foundation Models for Code\\\", \\\"authors\\\": \\\"Baptiste Rozi\\\\\\\\`ere and Jonas Gehring and Fabian Gloeckle and Sten Sootla and Ita...\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"arXiv preprint arXiv:2308.12950\\\"}], \\\"tex_citations\\\": [{\\\"key\\\": \\\"chen2025tracepile\\\", \\\"file\\\": \\\"introduction.tex\\\", \\\"line\\\": 3, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"ding2024traced\\\", \\\"file\\\": \\\"introduction.tex\\\", \\\"line\\\": 3, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"wang2025dcsh\\\", \\\"file\\\": \\\"introduction.tex\\\", \\\"line\\\": 3, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"ni2024next\\\", \\\"file\\\": \\\"introduction.tex\\\", \\\"line\\\": 3, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"wang2025dcsh\\\", \\\"file\\\": \\\"introduction.tex\\\", \\\"line\\\": 7, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"chen2021evaluating\\\", \\\"file\\\": \\\"introduction.tex\\\", \\\"line\\\": 13, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"austin2021program\\\", \\\"file\\\": \\\"introduction.tex\\\", \\\"line\\\": 13, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"qwen2025coder\\\", \\\"file\\\": \\\"introduction.tex\\\", \\\"line\\\": 13, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"roziere2024code\\\", \\\"file\\\": \\\"introduction.tex\\\", \\\"line\\\": 13, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"deepseek2024coder\\\", \\\"file\\\": \\\"introduction.tex\\\", \\\"line\\\": 13, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"chen2025tracepile\\\", \\\"file\\\": \\\"method.tex\\\", \\\"line\\\": 7, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"gu2024cruxeval\\\", \\\"file\\\": \\\"method.tex\\\", \\\"line\\\": 7, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"chen2021evaluating\\\", \\\"file\\\": \\\"method.tex\\\", \\\"line\\\": 12, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"austin2021program\\\", \\\"file\\\": \\\"method.tex\\\", \\\"line\\\": 12, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"qwen2025coder\\\", \\\"file\\\": \\\"method.tex\\\", \\\"line\\\": 38, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"roziere2024code\\\", \\\"file\\\": \\\"method.tex\\\", \\\"line\\\": 38, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"deepseek2024coder\\\", \\\"file\\\": \\\"method.tex\\\", \\\"line\\\": 38, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"hu2022lora\\\", \\\"file\\\": \\\"method.tex\\\", \\\"line\\\": 39, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"tian2024debugbench\\\", \\\"file\\\": \\\"experiments.tex\\\", \\\"line\\\": 168, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"chen2025tracepile\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 4, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"wang2025dcsh\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 4, \\\"command\\\": \\\"citet\\\"}, {\\\"key\\\": \\\"ni2024next\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 5, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"eguchi2025etcot\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 5, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"ferrando2025execute\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 6, \\\"command\\\": \\\"citet\\\"}, {\\\"key\\\": \\\"gu2024cruxeval\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 7, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"xu2025cruxevalx\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 7, \\\"command\\\": \\\"citet\\\"}, {\\\"key\\\": \\\"ding2024traced\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 11, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"appt2024\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 12, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"zhou2024llm4patch\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 12, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"widyasari2024fusefl\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 13, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"foster2025mutation\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 14, \\\"command\\\": \\\"citet\\\"}, {\\\"key\\\": \\\"abreu2007accuracy\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 19, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"jones2002visualization\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 19, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"wong2014dstar\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 19, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"kang2024autofl\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 20, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"qin2024agentfl\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 20, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"widyasari2024llm4fl\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 20, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"mukherjee2025llmfl\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 20, \\\"command\\\": \\\"citet\\\"}, {\\\"key\\\": \\\"huang2026tracecoder\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 25, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"wang2025inspectcoder\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 25, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"haque2025traces\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 25, \\\"command\\\": \\\"citet\\\"}, {\\\"key\\\": \\\"hu2022lora\\\", \\\"file\\\": \\\"appendix.tex\\\", \\\"line\\\": 37, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"spiess2025calibration\\\", \\\"file\\\": \\\"appendix.tex\\\", \\\"line\\\": 406, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"tian2024debugbench\\\", \\\"file\\\": \\\"appendix.tex\\\", \\\"line\\\": 464, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"yang2024generalization\\\", \\\"file\\\": \\\"appendix.tex\\\", \\\"line\\\": 502, \\\"command\\\": \\\"citep\\\"}], \\\"online_verification\\\": [{\\\"key\\\": \\\"chen2025tracepile\\\", \\\"title\\\": \\\"Chain of Execution Supervision Promotes General Reasoning in Large Language Models\\\", \\\"status\\\": \\\"error\\\", \\\"confidence\\\": 0.0, \\\"matched_title\\\": \\\"\\\", \\\"matched_year\\\": \\\"\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"API request failed\\\"}, {\\\"key\\\": \\\"ding2024traced\\\", \\\"title\\\": \\\"TRACED: Execution-aware Pre-training for Source Code\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"TRACED: Execution-aware Pre-training for Source Code\\\", \\\"matched_year\\\": \\\"2024\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"chen2021evaluating\\\", \\\"title\\\": \\\"Evaluating Large Language Models Trained on Code\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Evaluating Large Language Models Trained on Code\\\", \\\"matched_year\\\": \\\"2021\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"austin2021program\\\", \\\"title\\\": \\\"Program Synthesis with Large Language Models\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Program Synthesis with Large Language Models\\\", \\\"matched_year\\\": \\\"2021\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"gu2024cruxeval\\\", \\\"title\\\": \\\"CRUXEval: A Benchmark for Code Reasoning, Understanding and Execution\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"CRUXEval: A Benchmark for Code Reasoning, Understanding and Execution\\\", \\\"matched_year\\\": \\\"2024\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"hu2022lora\\\", \\\"title\\\": \\\"LoRA: Low-Rank Adaptation of Large Language Models\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"LoRA: Low-Rank Adaptation of Large Language Models\\\", \\\"matched_year\\\": \\\"2021\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"qwen2025coder\\\", \\\"title\\\": \\\"Qwen2.5-Coder Technical Report\\\", \\\"status\\\": \\\"mismatch\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Qwen2.5-Coder Technical Report\\\", \\\"matched_year\\\": \\\"2024\\\", \\\"mismatch_fields\\\": [\\\"first_author: bib=team vs api=hui\\\"], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"deepseek2024coder\\\", \\\"title\\\": \\\"DeepSeek-Coder: When the Large Language Model Meets Programming -- The Rise of Code Intelligence\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"DeepSeek-Coder: When the Large Language Model Meets Programming -- The Rise of Code Intelligence\\\", \\\"matched_year\\\": \\\"2024\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"wang2025dcsh\\\", \\\"title\\\": \\\"Do Code Semantics Help? A Comprehensive Study on Execution Trace-Based Information for Code Large Language Models\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Do Code Semantics Help? A Comprehensive Study on Execution Trace-Based Information for Code Large Language Models\\\", \\\"matched_year\\\": \\\"2025\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"ni2024next\\\", \\\"title\\\": \\\"NExT: Teaching Large Language Models to Reason about Code Execution\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"NExT: Teaching Large Language Models to Reason about Code Execution\\\", \\\"matched_year\\\": \\\"2024\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"eguchi2025etcot\\\", \\\"title\\\": \\\"Making LLMs Program Interpreters via Execution Trace Chain of Thought\\\", \\\"status\\\": \\\"not_found\\\", \\\"confidence\\\": 0.321, \\\"matched_title\\\": \\\"Enriching Location Representation with Detailed Semantic Information\\\", \\\"matched_year\\\": \\\"\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"best match similarity 0.32 below threshold 0.82\\\"}, {\\\"key\\\": \\\"ferrando2025execute\\\", \\\"title\\\": \\\"What I Cannot Execute, I Do Not Understand: Training and Evaluating LLMs on Program Execution Traces\\\", \\\"status\\\": \\\"not_found\\\", \\\"confidence\\\": 0.199, \\\"matched_title\\\": \\\"Sparks of Artificial General Intelligence: Early experiments with GPT-4\\\", \\\"matched_year\\\": \\\"\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"best match similarity 0.20 below threshold 0.82\\\"}, {\\\"key\\\": \\\"xu2025cruxevalx\\\", \\\"title\\\": \\\"CRUXEval-X: A Benchmark for Multilingual Code Reasoning, Understanding and Execution\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"CRUXEVAL-X: A Benchmark for Multilingual Code Reasoning, Understanding and Execution\\\", \\\"matched_year\\\": \\\"2025\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"appt2024\\\", \\\"title\\\": \\\"APPT: Boosting Automated Patch Correctness Prediction via Fine-tuning Pre-trained Models\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"APPT: Boosting Automated Patch Correctness Prediction via Fine-Tuning Pre-Trained Models\\\", \\\"matched_year\\\": \\\"2024\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"zhou2024llm4patch\\\", \\\"title\\\": \\\"Leveraging Large Language Model for Automatic Patch Correctness Assessment\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Leveraging Large Language Model for Automatic Patch Correctness Assessment\\\", \\\"matched_year\\\": \\\"2024\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"spiess2025calibration\\\", \\\"title\\\": \\\"Calibration and Correctness of Language Models for Code\\\", \\\"status\\\": \\\"mismatch\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Calibration and Correctness of Language Models for Code\\\", \\\"matched_year\\\": \\\"2025\\\", \\\"mismatch_fields\\\": [\\\"first_author: bib=spiess vs api=spieß\\\"], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"foster2025mutation\\\", \\\"title\\\": \\\"Mutation-Guided LLM-based Test Generation at Meta\\\", \\\"status\\\": \\\"mismatch\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Mutation-Guided LLM-based Test Generation at Meta\\\", \\\"matched_year\\\": \\\"2025\\\", \\\"mismatch_fields\\\": [\\\"first_author: bib=foster vs api=harman\\\"], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"widyasari2024fusefl\\\", \\\"title\\\": \\\"Demystifying Faulty Code: Step-by-Step Reasoning for Explainable Fault Localization\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Demystifying Faulty Code: Step-by-Step Reasoning for Explainable Fault Localization\\\", \\\"matched_year\\\": \\\"2024\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"huang2026tracecoder\\\", \\\"title\\\": \\\"TraceCoder: A Trace-Driven Multi-Agent Framework for Automated Debugging of LLM-Generated Code\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"TraceCoder: A Trace-Driven Multi-Agent Framework for Automated Debugging of LLM-Generated Code\\\", \\\"matched_year\\\": \\\"2026\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"wang2025inspectcoder\\\", \\\"title\\\": \\\"InspectCoder: Dynamic Analysis-Enabled Self Repair through Interactive LLM-Debugger Collaboration\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"InspectCoder: Dynamic Analysis-Enabled Self Repair through interactive LLM-Debugger Collaboration\\\", \\\"matched_year\\\": \\\"2025\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"haque2025traces\\\", \\\"title\\\": \\\"Towards Effectively Leveraging Execution Traces for Program Repair with Code LLMs\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Towards Effectively Leveraging Execution Traces for Program Repair with Code LLMs\\\", \\\"matched_year\\\": \\\"2025\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"yang2024generalization\\\", \\\"title\\\": \\\"Unveiling the Generalization Power of Fine-Tuned Large Language Models\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Unveiling the Generalization Power of Fine-Tuned Large Language Models\\\", \\\"matched_year\\\": \\\"2024\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"dong2024composition\\\", \\\"title\\\": \\\"How Abilities in Large Language Models are Affected by Supervised Fine-tuning Data Composition\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"How Abilities in Large Language Models are Affected by Supervised Fine-tuning Data Composition\\\", \\\"matched_year\\\": \\\"2024\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"tian2024debugbench\\\", \\\"title\\\": \\\"DebugBench: Evaluating Debugging Capability of Large Language Models\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"DebugBench: Evaluating Debugging Capability of Large Language Models\\\", \\\"matched_year\\\": \\\"2024\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"abreu2007accuracy\\\", \\\"title\\\": \\\"On the Accuracy of Spectrum-based Fault Localization\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"On the Accuracy of Spectrum-based Fault Localization\\\", \\\"matched_year\\\": \\\"2007\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"jones2002visualization\\\", \\\"title\\\": \\\"Visualization of Test Information to Assist Fault Localization\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Visualization of test information to assist fault localization\\\", \\\"matched_year\\\": \\\"2002\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"wong2014dstar\\\", \\\"title\\\": \\\"DStar: An Effective Spectrum-Based Fault Localization Technique\\\", \\\"status\\\": \\\"not_found\\\", \\\"confidence\\\": 0.561, \\\"matched_title\\\": \\\"MSFL: A Model for Fault Localization Using Mutation-Spectra Technique\\\", \\\"matched_year\\\": \\\"\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"best match similarity 0.56 below threshold 0.82\\\"}, {\\\"key\\\": \\\"kang2024autofl\\\", \\\"title\\\": \\\"AutoFL: Automated Fault Localization via Large Language Models\\\", \\\"status\\\": \\\"not_found\\\", \\\"confidence\\\": 0.45, \\\"matched_title\\\": \\\"A Survey on Large Language Models for Software Engineering\\\", \\\"matched_year\\\": \\\"\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"best match similarity 0.45 below threshold 0.82\\\"}, {\\\"key\\\": \\\"qin2024agentfl\\\", \\\"title\\\": \\\"AgentFL: Scaling LLM-based Fault Localization to Project-Level Context\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"AgentFL: Scaling LLM-based Fault Localization to Project-Level Context\\\", \\\"matched_year\\\": \\\"2024\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"widyasari2024llm4fl\\\", \\\"title\\\": \\\"LLM4FL: An LLM-based Fault Localization Integrated Debugging Framework for Automated Program Repair\\\", \\\"status\\\": \\\"not_found\\\", \\\"confidence\\\": 0.448, \\\"matched_title\\\": \\\"A Multi-Agent Approach to Fault Localization via Graph-Based Retrieval and Reflexion\\\", \\\"matched_year\\\": \\\"\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"best match similarity 0.45 below threshold 0.82\\\"}, {\\\"key\\\": \\\"mukherjee2025llmfl\\\", \\\"title\\\": \\\"Can Large Language Models Localize Faults like Developers? A Comprehensive Study\\\", \\\"status\\\": \\\"not_found\\\", \\\"confidence\\\": 0.186, \\\"matched_title\\\": \\\"Internet of Things (IoT): A vision, architectural elements, and future directions\\\", \\\"matched_year\\\": \\\"\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"best match similarity 0.19 below threshold 0.82\\\"}, {\\\"key\\\": \\\"roziere2024code\\\", \\\"title\\\": \\\"Code Llama: Open Foundation Models for Code\\\", \\\"status\\\": \\\"mismatch\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Code Llama: Open Foundation Models for Code\\\", \\\"matched_year\\\": \\\"2023\\\", \\\"mismatch_fields\\\": [\\\"first_author: bib=rozi\\\\\\\\`ere vs api=rozière\\\"], \\\"note\\\": \\\"\\\"}]}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"summary\": {\"total_bib_entries\": 32, \"total_citations\": 45, \"unique_cited_keys\": 31, \"orphan_bib\": 1, \"missing_bib\": 0, \"duplicate_keys\": 0, \"online_verified\": 21, \"online_not_found\": 6, \"online_mismatch\": 4}, \"cross_check\": {\"orphan_bib\": [\"dong2024composition\"], \"missing_bib\": [], \"orphan_count\": 1, \"missing_count\": 0}, \"bib_entries\": [{\"key\": \"chen2025tracepile\", \"type\": \"inproceedings\", \"title\": \"Chain of Execution Supervision Promotes General Reasoning in Large Language Models\", \"authors\": \"Nuo Chen and Zehua Li and Keqin Bao and Junyang Lin and Dayiheng Liu\", \"year\": \"2025\", \"venue\": \"Advances in Neural Information Processing Systems (NeurIPS)\"}, {\"key\": \"ding2024traced\", \"type\": \"inproceedings\", \"title\": \"TRACED: Execution-aware Pre-training for Source Code\", \"authors\": \"Yangruibo Ding and Ben Steenhoek and Kexin Pei and Gail Kaiser and Wei Le and Ba...\", \"year\": \"2024\", \"venue\": \"Proceedings of the 46th IEEE/ACM International Conference on Software Engineerin...\"}, {\"key\": \"chen2021evaluating\", \"type\": \"article\", \"title\": \"Evaluating Large Language Models Trained on Code\", \"authors\": \"Chen, Mark and Tworek, Jerry and Jun, Heewoo and Yuan, Qiming and Pinto, Henriqu...\", \"year\": \"2021\", \"venue\": \"arXiv preprint arXiv:2107.03374\"}, {\"key\": \"austin2021program\", \"type\": \"article\", \"title\": \"Program Synthesis with Large Language Models\", \"authors\": \"Austin, Jacob and Odena, Augustus and Nye, Maxwell and Bosma, Maarten and Michal...\", \"year\": \"2021\", \"venue\": \"arXiv preprint arXiv:2108.07732\"}, {\"key\": \"gu2024cruxeval\", \"type\": \"inproceedings\", \"title\": \"CRUXEval: A Benchmark for Code Reasoning, Understanding and Execution\", \"authors\": \"Alex Gu and Baptiste Rozi\\\\`ere and Hugh Leather and Armando Solar-Lezama and Gab...\", \"year\": \"2024\", \"venue\": \"Proceedings of the 41st International Conference on Machine Learning (ICML)\"}, {\"key\": \"hu2022lora\", \"type\": \"inproceedings\", \"title\": \"LoRA: Low-Rank Adaptation of Large Language Models\", \"authors\": \"Edward J. Hu and Yelong Shen and Phillip Wallis and Zeyuan Allen-Zhu and Yuanzhi...\", \"year\": \"2022\", \"venue\": \"Proceedings of the 10th International Conference on Learning Representations (IC...\"}, {\"key\": \"qwen2025coder\", \"type\": \"article\", \"title\": \"Qwen2.5-Coder Technical Report\", \"authors\": \"Qwen Team\", \"year\": \"2024\", \"venue\": \"arXiv preprint arXiv:2409.12186\"}, {\"key\": \"deepseek2024coder\", \"type\": \"article\", \"title\": \"DeepSeek-Coder: When the Large Language Model Meets Programming -- The Rise of Code Intelligence\", \"authors\": \"Daya Guo and Qihao Zhu and Dejian Yang and Zhenda Xie and Kai Dong and Wentao Zh...\", \"year\": \"2024\", \"venue\": \"arXiv preprint arXiv:2401.14196\"}, {\"key\": \"wang2025dcsh\", \"type\": \"inproceedings\", \"title\": \"Do Code Semantics Help? A Comprehensive Study on Execution Trace-Based Information for Code Large Language Models\", \"authors\": \"Jian Wang and Xiaofei Xie and Qiang Hu and Shangqing Liu and Yi Li\", \"year\": \"2025\", \"venue\": \"Findings of the Association for Computational Linguistics: EMNLP 2025\"}, {\"key\": \"ni2024next\", \"type\": \"inproceedings\", \"title\": \"NExT: Teaching Large Language Models to Reason about Code Execution\", \"authors\": \"Ansong Ni and Miltiadis Allamanis and Arman Cohan and Yinlin Deng and Kensen Shi...\", \"year\": \"2024\", \"venue\": \"Proceedings of the 41st International Conference on Machine Learning (ICML)\"}, {\"key\": \"eguchi2025etcot\", \"type\": \"inproceedings\", \"title\": \"Making LLMs Program Interpreters via Execution Trace Chain of Thought\", \"authors\": \"Koshi Eguchi and Takuya Akiba\", \"year\": \"2025\", \"venue\": \"ICML 2025 Workshop on Programmatic Representations for Agent Learning (PRAL)\"}, {\"key\": \"ferrando2025execute\", \"type\": \"article\", \"title\": \"What I Cannot Execute, I Do Not Understand: Training and Evaluating LLMs on Program Execution Traces\", \"authors\": \"Jordi Armengol-Estape and Quentin Carbonneaux and Tianjun Zhang and Aram H. Mark...\", \"year\": \"2025\", \"venue\": \"arXiv preprint arXiv:2503.05703\"}, {\"key\": \"xu2025cruxevalx\", \"type\": \"inproceedings\", \"title\": \"CRUXEval-X: A Benchmark for Multilingual Code Reasoning, Understanding and Execution\", \"authors\": \"Ruiyang Xu and others\", \"year\": \"2025\", \"venue\": \"Proceedings of the 63rd Annual Meeting of the Association for Computational Ling...\"}, {\"key\": \"appt2024\", \"type\": \"article\", \"title\": \"APPT: Boosting Automated Patch Correctness Prediction via Fine-tuning Pre-trained Models\", \"authors\": \"Quanjun Zhang and Chunrong Fang and Weisong Sun and Yan Liu and Tieke He and Xia...\", \"year\": \"2024\", \"venue\": \"IEEE Transactions on Software Engineering\"}, {\"key\": \"zhou2024llm4patch\", \"type\": \"article\", \"title\": \"Leveraging Large Language Model for Automatic Patch Correctness Assessment\", \"authors\": \"Xin Zhou and Bowen Xu and Kisub Kim and DongGyun Han and Hung Huu Nguyen and Tha...\", \"year\": \"2024\", \"venue\": \"IEEE Transactions on Software Engineering\"}, {\"key\": \"spiess2025calibration\", \"type\": \"inproceedings\", \"title\": \"Calibration and Correctness of Language Models for Code\", \"authors\": \"Claudio Spiess and David Gros and others\", \"year\": \"2025\", \"venue\": \"Proceedings of the 47th IEEE/ACM International Conference on Software Engineerin...\"}, {\"key\": \"foster2025mutation\", \"type\": \"inproceedings\", \"title\": \"Mutation-Guided LLM-based Test Generation at Meta\", \"authors\": \"Christopher Foster and others\", \"year\": \"2025\", \"venue\": \"Proceedings of the ACM International Conference on the Foundations of Software E...\"}, {\"key\": \"widyasari2024fusefl\", \"type\": \"inproceedings\", \"title\": \"Demystifying Faulty Code: Step-by-Step Reasoning for Explainable Fault Localization\", \"authors\": \"Ratnadira Widyasari and Jia Wei Ang and Truong Giang Nguyen and Neil Sharma and ...\", \"year\": \"2024\", \"venue\": \"Proceedings of the IEEE International Conference on Software Analysis, Evolution...\"}, {\"key\": \"huang2026tracecoder\", \"type\": \"inproceedings\", \"title\": \"TraceCoder: A Trace-Driven Multi-Agent Framework for Automated Debugging of LLM-Generated Code\", \"authors\": \"Jiangping Huang and Wenguang Ye and Weisong Sun and Jian Zhang and Mingyue Zhang...\", \"year\": \"2026\", \"venue\": \"Proceedings of the 48th IEEE/ACM International Conference on Software Engineerin...\"}, {\"key\": \"wang2025inspectcoder\", \"type\": \"article\", \"title\": \"InspectCoder: Dynamic Analysis-Enabled Self Repair through Interactive LLM-Debugger Collaboration\", \"authors\": \"Yunkun Wang and Yue Zhang and Guochang Li and Chen Zhi and Binhua Li and Fei Hua...\", \"year\": \"2025\", \"venue\": \"arXiv preprint arXiv:2510.18327\"}, {\"key\": \"haque2025traces\", \"type\": \"inproceedings\", \"title\": \"Towards Effectively Leveraging Execution Traces for Program Repair with Code LLMs\", \"authors\": \"Mirazul Haque and Petr Babkin and Farima Farmahinifarahani and Manuela Veloso\", \"year\": \"2025\", \"venue\": \"KnowledgeNLP Workshop at ACL 2025\"}, {\"key\": \"yang2024generalization\", \"type\": \"inproceedings\", \"title\": \"Unveiling the Generalization Power of Fine-Tuned Large Language Models\", \"authors\": \"Haoran Yang and Yumeng Zhang and Jiaqi Xu and Hongyuan Lu and Pheng Ann Heng and...\", \"year\": \"2024\", \"venue\": \"Proceedings of the 2024 Conference of the North American Chapter of the Associat...\"}, {\"key\": \"dong2024composition\", \"type\": \"inproceedings\", \"title\": \"How Abilities in Large Language Models are Affected by Supervised Fine-tuning Data Composition\", \"authors\": \"Guanting Dong and Hongyi Yuan and Keming Lu and Chengpeng Li and Mingfeng Xue an...\", \"year\": \"2024\", \"venue\": \"Proceedings of the 62nd Annual Meeting of the Association for Computational Ling...\"}, {\"key\": \"tian2024debugbench\", \"type\": \"inproceedings\", \"title\": \"DebugBench: Evaluating Debugging Capability of Large Language Models\", \"authors\": \"Runchu Tian and Yining Ye and Yujia Qin and Xin Cong and Yankai Lin and Yinxu Pa...\", \"year\": \"2024\", \"venue\": \"Findings of the Association for Computational Linguistics: ACL 2024\"}, {\"key\": \"abreu2007accuracy\", \"type\": \"article\", \"title\": \"On the Accuracy of Spectrum-based Fault Localization\", \"authors\": \"Rui Abreu and Peter Zoeteweij and Arjan J.C. van Gemund\", \"year\": \"2007\", \"venue\": \"Testing: Academic and Industrial Conference Practice and Research Techniques (MU...\"}, {\"key\": \"jones2002visualization\", \"type\": \"inproceedings\", \"title\": \"Visualization of Test Information to Assist Fault Localization\", \"authors\": \"James A. Jones and Mary Jean Harrold and John Stasko\", \"year\": \"2002\", \"venue\": \"Proceedings of the 24th International Conference on Software Engineering (ICSE)\"}, {\"key\": \"wong2014dstar\", \"type\": \"article\", \"title\": \"DStar: An Effective Spectrum-Based Fault Localization Technique\", \"authors\": \"W. Eric Wong and Vidroha Debroy and Ruizhi Gao and Yihao Li\", \"year\": \"2014\", \"venue\": \"Journal of Systems and Software\"}, {\"key\": \"kang2024autofl\", \"type\": \"inproceedings\", \"title\": \"AutoFL: Automated Fault Localization via Large Language Models\", \"authors\": \"Sungmin Kang and Gabin An and Shin Yoo\", \"year\": \"2024\", \"venue\": \"Proceedings of the 46th IEEE/ACM International Conference on Software Engineerin...\"}, {\"key\": \"qin2024agentfl\", \"type\": \"inproceedings\", \"title\": \"AgentFL: Scaling LLM-based Fault Localization to Project-Level Context\", \"authors\": \"Yihao Qin and Shangwen Wang and Yiling Lou and Jinhao Dong and Kaixin Wang and X...\", \"year\": \"2024\", \"venue\": \"Proceedings of the 39th IEEE/ACM International Conference on Automated Software ...\"}, {\"key\": \"widyasari2024llm4fl\", \"type\": \"inproceedings\", \"title\": \"LLM4FL: An LLM-based Fault Localization Integrated Debugging Framework for Automated Program Repair\", \"authors\": \"Ratnadira Widyasari and Gopi Krishnan Rajbahadur and Shin Hwei Tan and Xin Xia a...\", \"year\": \"2025\", \"venue\": \"Proceedings of the 47th IEEE/ACM International Conference on Software Engineerin...\"}, {\"key\": \"mukherjee2025llmfl\", \"type\": \"inproceedings\", \"title\": \"Can Large Language Models Localize Faults like Developers? A Comprehensive Study\", \"authors\": \"Soneya Binta Hossain and Nan Jiang and Qiang Zhou and Xiaopeng Li and Wen-Hao Ch...\", \"year\": \"2025\", \"venue\": \"Proceedings of the 47th IEEE/ACM International Conference on Software Engineerin...\"}, {\"key\": \"roziere2024code\", \"type\": \"article\", \"title\": \"Code Llama: Open Foundation Models for Code\", \"authors\": \"Baptiste Rozi\\\\`ere and Jonas Gehring and Fabian Gloeckle and Sten Sootla and Ita...\", \"year\": \"2024\", \"venue\": \"arXiv preprint arXiv:2308.12950\"}], \"tex_citations\": [{\"key\": \"chen2025tracepile\", \"file\": \"introduction.tex\", \"line\": 3, \"command\": \"citep\"}, {\"key\": \"ding2024traced\", \"file\": \"introduction.tex\", \"line\": 3, \"command\": \"citep\"}, {\"key\": \"wang2025dcsh\", \"file\": \"introduction.tex\", \"line\": 3, \"command\": \"citep\"}, {\"key\": \"ni2024next\", \"file\": \"introduction.tex\", \"line\": 3, \"command\": \"citep\"}, {\"key\": \"wang2025dcsh\", \"file\": \"introduction.tex\", \"line\": 7, \"command\": \"citep\"}, {\"key\": \"chen2021evaluating\", \"file\": \"introduction.tex\", \"line\": 13, \"command\": \"citep\"}, {\"key\": \"austin2021program\", \"file\": \"introduction.tex\", \"line\": 13, \"command\": \"citep\"}, {\"key\": \"qwen2025coder\", \"file\": \"introduction.tex\", \"line\": 13, \"command\": \"citep\"}, {\"key\": \"roziere2024code\", \"file\": \"introduction.tex\", \"line\": 13, \"command\": \"citep\"}, {\"key\": \"deepseek2024coder\", \"file\": \"introduction.tex\", \"line\": 13, \"command\": \"citep\"}, {\"key\": \"chen2025tracepile\", \"file\": \"method.tex\", \"line\": 7, \"command\": \"citep\"}, {\"key\": \"gu2024cruxeval\", \"file\": \"method.tex\", \"line\": 7, \"command\": \"citep\"}, {\"key\": \"chen2021evaluating\", \"file\": \"method.tex\", \"line\": 12, \"command\": \"citep\"}, {\"key\": \"austin2021program\", \"file\": \"method.tex\", \"line\": 12, \"command\": \"citep\"}, {\"key\": \"qwen2025coder\", \"file\": \"method.tex\", \"line\": 38, \"command\": \"citep\"}, {\"key\": \"roziere2024code\", \"file\": \"method.tex\", \"line\": 38, \"command\": \"citep\"}, {\"key\": \"deepseek2024coder\", \"file\": \"method.tex\", \"line\": 38, \"command\": \"citep\"}, {\"key\": \"hu2022lora\", \"file\": \"method.tex\", \"line\": 39, \"command\": \"citep\"}, {\"key\": \"tian2024debugbench\", \"file\": \"experiments.tex\", \"line\": 168, \"command\": \"citep\"}, {\"key\": \"chen2025tracepile\", \"file\": \"related_work.tex\", \"line\": 4, \"command\": \"citep\"}, {\"key\": \"wang2025dcsh\", \"file\": \"related_work.tex\", \"line\": 4, \"command\": \"citet\"}, {\"key\": \"ni2024next\", \"file\": \"related_work.tex\", \"line\": 5, \"command\": \"citep\"}, {\"key\": \"eguchi2025etcot\", \"file\": \"related_work.tex\", \"line\": 5, \"command\": \"citep\"}, {\"key\": \"ferrando2025execute\", \"file\": \"related_work.tex\", \"line\": 6, \"command\": \"citet\"}, {\"key\": \"gu2024cruxeval\", \"file\": \"related_work.tex\", \"line\": 7, \"command\": \"citep\"}, {\"key\": \"xu2025cruxevalx\", \"file\": \"related_work.tex\", \"line\": 7, \"command\": \"citet\"}, {\"key\": \"ding2024traced\", \"file\": \"related_work.tex\", \"line\": 11, \"command\": \"citep\"}, {\"key\": \"appt2024\", \"file\": \"related_work.tex\", \"line\": 12, \"command\": \"citep\"}, {\"key\": \"zhou2024llm4patch\", \"file\": \"related_work.tex\", \"line\": 12, \"command\": \"citep\"}, {\"key\": \"widyasari2024fusefl\", \"file\": \"related_work.tex\", \"line\": 13, \"command\": \"citep\"}, {\"key\": \"foster2025mutation\", \"file\": \"related_work.tex\", \"line\": 14, \"command\": \"citet\"}, {\"key\": \"abreu2007accuracy\", \"file\": \"related_work.tex\", \"line\": 19, \"command\": \"citep\"}, {\"key\": \"jones2002visualization\", \"file\": \"related_work.tex\", \"line\": 19, \"command\": \"citep\"}, {\"key\": \"wong2014dstar\", \"file\": \"related_work.tex\", \"line\": 19, \"command\": \"citep\"}, {\"key\": \"kang2024autofl\", \"file\": \"related_work.tex\", \"line\": 20, \"command\": \"citep\"}, {\"key\": \"qin2024agentfl\", \"file\": \"related_work.tex\", \"line\": 20, \"command\": \"citep\"}, {\"key\": \"widyasari2024llm4fl\", \"file\": \"related_work.tex\", \"line\": 20, \"command\": \"citep\"}, {\"key\": \"mukherjee2025llmfl\", \"file\": \"related_work.tex\", \"line\": 20, \"command\": \"citet\"}, {\"key\": \"huang2026tracecoder\", \"file\": \"related_work.tex\", \"line\": 25, \"command\": \"citep\"}, {\"key\": \"wang2025inspectcoder\", \"file\": \"related_work.tex\", \"line\": 25, \"command\": \"citep\"}, {\"key\": \"haque2025traces\", \"file\": \"related_work.tex\", \"line\": 25, \"command\": \"citet\"}, {\"key\": \"hu2022lora\", \"file\": \"appendix.tex\", \"line\": 37, \"command\": \"citep\"}, {\"key\": \"spiess2025calibration\", \"file\": \"appendix.tex\", \"line\": 406, \"command\": \"citep\"}, {\"key\": \"tian2024debugbench\", \"file\": \"appendix.tex\", \"line\": 464, \"command\": \"citep\"}, {\"key\": \"yang2024generalization\", \"file\": \"appendix.tex\", \"line\": 502, \"command\": \"citep\"}], \"online_verification\": [{\"key\": \"chen2025tracepile\", \"title\": \"Chain of Execution Supervision Promotes General Reasoning in Large Language Models\", \"status\": \"error\", \"confidence\": 0.0, \"matched_title\": \"\", \"matched_year\": \"\", \"mismatch_fields\": [], \"note\": \"API request failed\"}, {\"key\": \"ding2024traced\", \"title\": \"TRACED: Execution-aware Pre-training for Source Code\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"TRACED: Execution-aware Pre-training for Source Code\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"chen2021evaluating\", \"title\": \"Evaluating Large Language Models Trained on Code\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Evaluating Large Language Models Trained on Code\", \"matched_year\": \"2021\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"austin2021program\", \"title\": \"Program Synthesis with Large Language Models\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Program Synthesis with Large Language Models\", \"matched_year\": \"2021\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"gu2024cruxeval\", \"title\": \"CRUXEval: A Benchmark for Code Reasoning, Understanding and Execution\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"CRUXEval: A Benchmark for Code Reasoning, Understanding and Execution\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"hu2022lora\", \"title\": \"LoRA: Low-Rank Adaptation of Large Language Models\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"LoRA: Low-Rank Adaptation of Large Language Models\", \"matched_year\": \"2021\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"qwen2025coder\", \"title\": \"Qwen2.5-Coder Technical Report\", \"status\": \"mismatch\", \"confidence\": 1.0, \"matched_title\": \"Qwen2.5-Coder Technical Report\", \"matched_year\": \"2024\", \"mismatch_fields\": [\"first_author: bib=team vs api=hui\"], \"note\": \"\"}, {\"key\": \"deepseek2024coder\", \"title\": \"DeepSeek-Coder: When the Large Language Model Meets Programming -- The Rise of Code Intelligence\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"DeepSeek-Coder: When the Large Language Model Meets Programming -- The Rise of Code Intelligence\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"wang2025dcsh\", \"title\": \"Do Code Semantics Help? A Comprehensive Study on Execution Trace-Based Information for Code Large Language Models\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Do Code Semantics Help? A Comprehensive Study on Execution Trace-Based Information for Code Large Language Models\", \"matched_year\": \"2025\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"ni2024next\", \"title\": \"NExT: Teaching Large Language Models to Reason about Code Execution\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"NExT: Teaching Large Language Models to Reason about Code Execution\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"eguchi2025etcot\", \"title\": \"Making LLMs Program Interpreters via Execution Trace Chain of Thought\", \"status\": \"not_found\", \"confidence\": 0.321, \"matched_title\": \"Enriching Location Representation with Detailed Semantic Information\", \"matched_year\": \"\", \"mismatch_fields\": [], \"note\": \"best match similarity 0.32 below threshold 0.82\"}, {\"key\": \"ferrando2025execute\", \"title\": \"What I Cannot Execute, I Do Not Understand: Training and Evaluating LLMs on Program Execution Traces\", \"status\": \"not_found\", \"confidence\": 0.199, \"matched_title\": \"Sparks of Artificial General Intelligence: Early experiments with GPT-4\", \"matched_year\": \"\", \"mismatch_fields\": [], \"note\": \"best match similarity 0.20 below threshold 0.82\"}, {\"key\": \"xu2025cruxevalx\", \"title\": \"CRUXEval-X: A Benchmark for Multilingual Code Reasoning, Understanding and Execution\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"CRUXEVAL-X: A Benchmark for Multilingual Code Reasoning, Understanding and Execution\", \"matched_year\": \"2025\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"appt2024\", \"title\": \"APPT: Boosting Automated Patch Correctness Prediction via Fine-tuning Pre-trained Models\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"APPT: Boosting Automated Patch Correctness Prediction via Fine-Tuning Pre-Trained Models\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"zhou2024llm4patch\", \"title\": \"Leveraging Large Language Model for Automatic Patch Correctness Assessment\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Leveraging Large Language Model for Automatic Patch Correctness Assessment\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"spiess2025calibration\", \"title\": \"Calibration and Correctness of Language Models for Code\", \"status\": \"mismatch\", \"confidence\": 1.0, \"matched_title\": \"Calibration and Correctness of Language Models for Code\", \"matched_year\": \"2025\", \"mismatch_fields\": [\"first_author: bib=spiess vs api=spieß\"], \"note\": \"\"}, {\"key\": \"foster2025mutation\", \"title\": \"Mutation-Guided LLM-based Test Generation at Meta\", \"status\": \"mismatch\", \"confidence\": 1.0, \"matched_title\": \"Mutation-Guided LLM-based Test Generation at Meta\", \"matched_year\": \"2025\", \"mismatch_fields\": [\"first_author: bib=foster vs api=harman\"], \"note\": \"\"}, {\"key\": \"widyasari2024fusefl\", \"title\": \"Demystifying Faulty Code: Step-by-Step Reasoning for Explainable Fault Localization\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Demystifying Faulty Code: Step-by-Step Reasoning for Explainable Fault Localization\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"huang2026tracecoder\", \"title\": \"TraceCoder: A Trace-Driven Multi-Agent Framework for Automated Debugging of LLM-Generated Code\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"TraceCoder: A Trace-Driven Multi-Agent Framework for Automated Debugging of LLM-Generated Code\", \"matched_year\": \"2026\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"wang2025inspectcoder\", \"title\": \"InspectCoder: Dynamic Analysis-Enabled Self Repair through Interactive LLM-Debugger Collaboration\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"InspectCoder: Dynamic Analysis-Enabled Self Repair through interactive LLM-Debugger Collaboration\", \"matched_year\": \"2025\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"haque2025traces\", \"title\": \"Towards Effectively Leveraging Execution Traces for Program Repair with Code LLMs\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Towards Effectively Leveraging Execution Traces for Program Repair with Code LLMs\", \"matched_year\": \"2025\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"yang2024generalization\", \"title\": \"Unveiling the Generalization Power of Fine-Tuned Large Language Models\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Unveiling the Generalization Power of Fine-Tuned Large Language Models\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"dong2024composition\", \"title\": \"How Abilities in Large Language Models are Affected by Supervised Fine-tuning Data Composition\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"How Abilities in Large Language Models are Affected by Supervised Fine-tuning Data Composition\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"tian2024debugbench\", \"title\": \"DebugBench: Evaluating Debugging Capability of Large Language Models\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"DebugBench: Evaluating Debugging Capability of Large Language Models\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"abreu2007accuracy\", \"title\": \"On the Accuracy of Spectrum-based Fault Localization\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"On the Accuracy of Spectrum-based Fault Localization\", \"matched_year\": \"2007\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"jones2002visualization\", \"title\": \"Visualization of Test Information to Assist Fault Localization\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Visualization of test information to assist fault localization\", \"matched_year\": \"2002\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"wong2014dstar\", \"title\": \"DStar: An Effective Spectrum-Based Fault Localization Technique\", \"status\": \"not_found\", \"confidence\": 0.561, \"matched_title\": \"MSFL: A Model for Fault Localization Using Mutation-Spectra Technique\", \"matched_year\": \"\", \"mismatch_fields\": [], \"note\": \"best match similarity 0.56 below threshold 0.82\"}, {\"key\": \"kang2024autofl\", \"title\": \"AutoFL: Automated Fault Localization via Large Language Models\", \"status\": \"not_found\", \"confidence\": 0.45, \"matched_title\": \"A Survey on Large Language Models for Software Engineering\", \"matched_year\": \"\", \"mismatch_fields\": [], \"note\": \"best match similarity 0.45 below threshold 0.82\"}, {\"key\": \"qin2024agentfl\", \"title\": \"AgentFL: Scaling LLM-based Fault Localization to Project-Level Context\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"AgentFL: Scaling LLM-based Fault Localization to Project-Level Context\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"widyasari2024llm4fl\", \"title\": \"LLM4FL: An LLM-based Fault Localization Integrated Debugging Framework for Automated Program Repair\", \"status\": \"not_found\", \"confidence\": 0.448, \"matched_title\": \"A Multi-Agent Approach to Fault Localization via Graph-Based Retrieval and Reflexion\", \"matched_year\": \"\", \"mismatch_fields\": [], \"note\": \"best match similarity 0.45 below threshold 0.82\"}, {\"key\": \"mukherjee2025llmfl\", \"title\": \"Can Large Language Models Localize Faults like Developers? A Comprehensive Study\", \"status\": \"not_found\", \"confidence\": 0.186, \"matched_title\": \"Internet of Things (IoT): A vision, architectural elements, and future directions\", \"matched_year\": \"\", \"mismatch_fields\": [], \"note\": \"best match similarity 0.19 below threshold 0.82\"}, {\"key\": \"roziere2024code\", \"title\": \"Code Llama: Open Foundation Models for Code\", \"status\": \"mismatch\", \"confidence\": 1.0, \"matched_title\": \"Code Llama: Open Foundation Models for Code\", \"matched_year\": \"2023\", \"mismatch_fields\": [\"first_author: bib=rozi\\\\`ere vs api=rozière\"], \"note\": \"\"}]}, \"error\": null, \"metadata\": {}}"
    }
  },
  "sourceToolAssistantUUID": "9d4da9da-9f51-4380-9e55-e298fbe6755f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/.claude/sessions/review_reviewer_1_7624f219",
  "sessionId": "f76386b4-9d1f-4f92-b831-706bc4acd94d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Runtime record

_source line 52_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[Round 1 审稿请求]: ## Round 1 审稿任务 — Reviewer 1  **你的审查侧重**: 方法严谨性 + 实验设计 + 统计有效性 + 可复现性  ### Venue 信息 - **目标**: EMNLP 2026 via ARR May 2026 cycle - **截止日期**: 2026-05-25 - **页数限制**: Long paper ≤ 8 页正文（不含…",
  "leafUuid": "d3ff5948-ee0e-41d5-98e8-61644311e2b5",
  "sessionId": "f76386b4-9d1f-4f92-b831-706bc4acd94d"
}
```

---


### Runtime record

_source line 53_

```json
{
  "type": "ai-title",
  "aiTitle": "Round 1 peer review for trace verdict prediction paper",
  "sessionId": "f76386b4-9d1f-4f92-b831-706bc4acd94d"
}
```

---


### Assistant

_source line 54 · 2026-05-17T18:07:54.593Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have a thorough understanding of the paper. Let me compile my review. Let me think carefully about the key issues.

## Key Issues to Address

### 1. Statistical Validity (重点审查)

**Critical: exception_only test set 49% duplicates violating Wilson CI independence**
- The exception_only test set has 1190 samples but only 607 unique (48.99% duplicates)
- Wilson CIs assume independent Bernoulli trials
- The paper mentions this in Appendix H (Tokenizer and Truncation Analysis) line 222: "Because exception_only test inputs contain 48.99% duplicates... 

The appendix shows that under deduplication, Qwen's accuracy becomes 99.67% with a wider Wilson CI of [98.81, 99.91], but the main text reports the narrower CI [99.58, 100.00] based on the inflated n=1190 sample size. This is problematic because paired bootstrap tests and McNemar tests also require sample independence, so the effective sample size should be ~607, not 1190, which would substantially widen all reported confidence intervals.

Most conditions rely on single-seed results—only exception_only has consistent multi-seed data, while VOTA, full_trace, label_only, loop_only, no_trace, and VOTA_no_ae are all single-seed runs. This means the Tier 1 vs Tier 2 hierarchy and the 26%/74% decomposition are built on limited experimental replication. For DeepSeek's seed 123 outlier at 91.09%, the paper attributes it to LoRA initialization sensitivity but lacks direct evidence; the appendix actually identifies format collapse—where the model echoes trace content instead of producing a verdict—as the more concrete explanation.

The 26%/74% decomposition has a causal validity problem: label_only doesn't just remove gradient dilution, it fundamentally changes both the loss function and gradient distribution, which could alter representation learning in unexpected ways. The paper acknowledges the two factors may interact, making the decomposition approximate at best. Since label_only still sees the full trace at inference, the improvement might stem from the model learning a different internal representation rather than from the two proposed mechanisms.

There's also a circular dependency in data generation—Qwen-2.5-Coder-7B-Instruct both generates the candidate solutions and serves as the evaluation model, which the paper admits may influence the pass/fail distribution. This means the 67%/33% ratio is partly an artifact of Qwen's own generation patterns. Cross-dataset evaluation on DebugBench helps mitigate this, though it reveals a ceiling effect where even the baseline already achieves 96.71%.

The "cross-model" and "architecture-independent" claims rest on only 4 models across 3 families, all of which are...

Writing model analysis...

The comparison between VOTA and exception_only is still problematic because truncation rates differ so dramatically across conditions. Looking at the reproducibility concerns, the code and data aren't available yet, DeepSeek's full_trace results had to be re-run after a context overflow issue, and the hardware used is quite new which could make replication difficult for others. On the method side, there's a significant issue with B5 regex—it achieves 99.33% accuracy almost trivially through a format marker that appears in all passing samples, and fine-tuning only adds 0.50 percentage points on top of that baseline, which raises questions about what's actually being learned.

The statistical significance is borderline too—the McNemar test gives p=0.041, which might not hold up after accounting for deduplication effects. The paper's claim about semantic versus format contributions relies heavily on the nomarker ablation showing a 2 percentage point drop, but that interpretation could be misleading. When markers are available, the model might learn to exploit them as a shortcut rather than developing robust semantic understanding, so removing markers forces harder learning—the performance gap could actually overstate how much the semantic content matters. The VOTA design combines exception handling, assertion points, and loop compression, but I need to examine how these components interact.

The paper doesn't systematically explore alternative VOTA configurations or discuss the hyperparameters underlying the compression itself, like what qualifies as a loop or what compression ratio to use. VOTA_no_ae performs just as well as the full VOTA, which suggests the assertion-point component might be redundant, yet there's no deeper investigation into which design choices actually matter. On the references side, there's no mention of SWE-bench or execution-aware evaluation frameworks, and the paper misses relevant work on test oracles and trace-based code understanding. That said, the research question is well-motivated with a solid experimental design, the ablation study covers seven different trace conditions across four models and three architectures, and the supplementary material is thorough with thirteen appendix sections. The authors are also honest about limitations, and the core decomposition idea itself is interesting.

The main findings are compelling—exception events really do dominate verdict prediction—and the ablation work is extensive. But there are some serious statistical and methodological concerns that weaken the conclusions. The 49% test set duplication affects all the confidence intervals and p-values reported. Using a single seed for six out of seven conditions makes the tier hierarchy and decomposition results less reliable. The format marker shortcut means the claim about learned semantic understanding rests on just a 0.50 percentage point improvement, which is marginal. And calling the approach "architecture-independent" is overstating it when only three families were tested and one showed instability. I'd put this around 3 to 3.5 on the rating scale—the core finding is interesting and probably holds up, but the statistical rigor needs work and some of the claims should be dialed back.

Now I'm writing up the full review.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d3ff5948-ee0e-41d5-98e8-61644311e2b5",
  "isSidechain": false,
  "requestId": "req_011Cb8awtKJpy45vFmpkBmFT",
  "type": "assistant",
  "uuid": "302f6f9d-8637-4d79-b989-eb7898629cca",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/.claude/sessions/review_reviewer_1_7624f219",
  "sessionId": "f76386b4-9d1f-4f92-b831-706bc4acd94d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JzwFkHZohRUw9mzx29VEBB",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9522,
      "cache_read_input_tokens": 67901,
      "output_tokens": 9563,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 9522,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 9563,
          "cache_read_input_tokens": 67901,
          "cache_creation_input_tokens": 9522,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 9522
          },
          "type": "message"
        }
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

_source line 55 · 2026-05-17T18:10:02.283Z_

全部材料已读完，引用验证完成。现在撰写完整审稿报告。

---

## 总体评分

**Overall Assessment**: 3.0 (Findings)
**一句话总结**: Exception dominance 是一个有价值的经验发现，但测试集 49% 重复样本从根本上破坏了所有统计推断的有效性，加上 6/7 条件为单 seed、核心 "learned semantic understanding" claim 仅依赖于一个 0.50pp 的边际增量，整体证据强度不足以支撑论文的强因果性声明。

---

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 2.5/5 | 测试集重复样本违反统计独立性假设，所有 CI/p 值均不可信（详见 N1）；26%/74% 分解缺乏因果有效性（N2）；format marker 使核心 claim 的增量仅 0.50pp（N3） |
| Excitement | 3/5 | "Exception events suffice" 对 trace-augmented systems 有实际指导意义，但 verdict prediction 本身是一个相对 narrow 的任务，且核心发现可被 regex B5 复现到 99.33% |
| Reproducibility | 3/5 | 超参数报告完整，但代码/数据未发布；单 seed 占多数条件；DeepSeek full_trace 初始 run 被废弃的处理缺乏透明度 |
| Confidence | 4/5 | 仔细阅读全文含附录，熟悉 code LLM fine-tuning 和统计方法论 |

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] 测试集 49% 重复样本系统性破坏全部统计推断

- 具体位置：Section 2.2 (line 14), Appendix H (line 222), Table 2 (experiments.tex line 6-7)
- 问题：`exception_only` 测试集 1,190 样本中仅 607 unique（48.99% 重复，Section 2.2 line 14 承认）。所有 pass-class 样本在 exception_only 格式下坍缩为相同 input（无 exception 信息），导致同一 problem 下多个 passing solution 产生完全相同的 (input, label) 对。论文在 Appendix H line 222 提及 "CIs assume n=1,190 independent trials; under deduplication (n=607), Qwen's accuracy is 99.67% (Wilson CI [98.81, 99.91])"，但这一关键信息被埋在附录中，**正文 Table 2, Table 3 的所有 CI 和 p-value 均基于 n=1,190 的独立性假设**。
  
  具体影响：
  - **Wilson CI**：假设 n=1,190 独立 Bernoulli trials。重复样本不是独立抽样——同一 problem 的 pass 样本命运完全耦合（模型预测一致），有效自由度远低于 1,190。正文 Table 3 报告 exception_only CI [99.58, 100.00]，但 Appendix 的 deduplicated CI [98.81, 99.91] 更宽，且这还假设 607 unique 样本彼此独立（实际上同一 problem 的 fail 样本也可能共享特征）。
  - **Paired bootstrap resampling**（B=10,000）：重采样从 1,190 样本中有放回抽取，但重复样本使 bootstrap 样本间的变异性被人为压低，p-value 被系统性低估。Section 4 第 7 行声称 "all differences are significant at p<0.0001 unless noted"，这些 p-value 在去重后可能大幅上升。
  - **McNemar test**：B5 vs SFT 的 p=0.041（Discussion line 23）已经边际显著，在有效 n=607 下很可能不再显著，直接威胁 "SFT learns genuine semantic understanding beyond format markers" 这一核心 claim。
  - **Bootstrap CI for 26%/74% decomposition**（Table 4, line 136: gradient dilution CI [+2.35, +6.55]）同样受重复样本影响。

- 为什么影响接收：这不是一个 minor reporting issue——它影响论文中几乎所有量化声明的可信度。正文中的 CI 和 p-value 给读者一种统计严谨的错觉，但底层假设被违反。
- 建议修改方向：(1) 正文所有统计分析必须以 deduplicated test set (n=607) 为主要报告指标，或使用 cluster-robust bootstrap（以 problem ID 为 cluster）；(2) 重新计算所有 p-value 并检查哪些不再显著；(3) 在 Section 2.2 或 Section 4 开头明确告知读者有效样本量。

---

**N2** [critical] 26%/74% gradient dilution vs information overload 分解缺乏因果有效性

- 具体位置：Section 4.4 (Table 4), method.tex line 43-47
- 问题：`label_only` 条件改变了两个因素：(a) 移除了 trace token 上的 loss（gradient dilution 的定义），但也 (b) 改变了整体梯度分布和模型学到的表征。论文将 full_trace→label_only 的 +4.46pp 提升全部归因于"gradient dilution"，但 masking trace tokens from loss 会改变模型学习的内部表征方式（不再被迫预测 trace 内容），这可能带来超出"减少 gradient 分散"的额外好处。

  更根本的问题：这个分解假设两个因素是加法可分的 (full_trace + gradient_dilution_fix = label_only; label_only + info_overload_fix = VOTA)。论文在 line 139 承认 "the two factors may interact, so this decomposition is approximate"，但 Abstract 和 Contribution 列表中未加限定地使用 "~26% gradient dilution, ~74% information overload" 作为精确比例，给读者错误的定量精度感。

  此外，label_only 仅在 Qwen-7B seed=42 上运行了一次（Table 8，single seed），26%/74% 这个数字的统计稳定性完全未知。

- 为什么影响接收：这是论文三个 Contribution 之一（Contribution 2），如果分解的因果有效性不成立，该贡献大幅削弱。
- 建议修改方向：(1) 将 "~26%/~74%" 降级为"一种近似的、非因果的描述性分解"，在 Abstract 和 Contribution 中明确限定语；(2) 讨论 label_only 可能存在的混淆变量（表征学习效应）；(3) 至少在一个额外模型上复现该分解。

---

**N3** [critical] Format marker 使 SFT 的 "learned semantic understanding" claim 仅依赖 0.50pp 边际增量

- 具体位置：Section 4.3 (line 107-113), Discussion line 22-25, Appendix K (Table 13)
- 问题：`exception_only` 格式在所有 pass-class 样本中包含确定性 marker `[No exception data in trace]`。Regex B5 仅凭此 marker 即达 99.33%（Table 13）。SFT exception_only 达 99.83%，增量仅 **0.50pp**（6 个额外正确样本，均来自 2 个 problem: MBPP/113 的 6 个样本 + HumanEval/95 的 2 个仍然错误）。

  论文的核心故事是 "SFT learns to distinguish caught from uncaught exceptions"（Discussion line 24-25），但这一 claim 的全部实验证据是：在 8 个 boundary samples 中正确 6 个 vs B5 的 0 个。这 8 个样本来自仅 2 个 distinct problems。McNemar p=0.041 已经边际显著，考虑到 N1 中的重复样本问题，这个 p-value 在校正后很可能不显著。

  nomarker ablation (97.65%) 的解读也有问题：论文声称 "~91% semantic, ~9% format"（line 112-113），但这个比例是用 (99.83 - 75.13 = 24.70pp total lift) 作为分母，将 marker 贡献 (~2pp) 除以总 lift。然而，带 marker 训练的模型可能未被迫充分学习语义特征（因为 marker 提供了捷径），所以 nomarker 模型学到了不同的决策边界。两个模型的 "semantic" 成分不可直接相减。

- 为什么影响接收：Contribution 1 的 "semantic vs format-driven" 分解是论文叙事的核心支柱。如果 SFT 的增量不显著且来自仅 2 个 problem，"learned semantic understanding" 的 claim 缺乏充分支撑。
- 建议修改方向：(1) 在正文中坦诚报告 B5 的 99.33% 成绩及 SFT 的真实增量 (0.50pp/6 samples/2 problems)，而非将 B5 buried 在 appendix；(2) 讨论这一 shortcut 对整体 claim 的影响；(3) 用更多 boundary samples 或合成实验验证 caught/uncaught distinction。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] 6/7 实验条件为单 seed，Tier 层级划分的统计稳定性未知

- 具体位置：Section 2.4 line 41, Table 2, Table 3
- 问题：仅 `exception_only`（4 model x 3 seeds 部分）和 `ae_only`（Qwen-7B 3 seeds）有多 seed 结果。VOTA (99.41%), full_trace (81.76%), label_only (86.22%), loop_only (85.63%), VOTA_no_ae (99.41%), no_trace (75.13%) 均为单 seed (seed=42)。
  
  DeepSeek exception_only 的 3-seed 方差 σ=4.76pp 已经表明 LoRA fine-tuning 对 seed 敏感。如果 VOTA 或 loop_only 也有类似的 seed 方差，Tier 1/Tier 2 的边界（99% vs 85.6%）可能不稳定。论文将 DeepSeek seed 123 (91.09%) 归为 "outlier" 并排除（Table 1 注释 $\dag$），但在仅 3 个 seed 中排除 1 个在统计上缺乏依据。
  
- 建议：(1) 至少为 Tier boundary 相关的关键条件（VOTA, loop_only, full_trace）补充 3-seed 结果；(2) 停止使用 "outlier" 描述 1/3 的 seed，改用 "bimodal behavior" 或 "high seed variance"。

**W2** [warning] "Architecture-independent" 和 "cross-model" 声明过度

- 具体位置：Abstract line 20-21, Introduction line 15, Conclusion line 3
- 问题：4 个模型来自 3 个架构家族，全部是 code-specialized，参数范围 1.5B-13B。其中 DeepSeek 在 exception_only 和 VOTA 上都表现出显著不稳定性（seed variance σ=4.76pp; VOTA 84.45% vs 其他模型 98-99%）。
  
  "Architecture-independent" 至少需要覆盖: (a) general-purpose LLMs (e.g., Llama-3, Mistral), (b) larger scales (>30B), (c) encoder-decoder architectures。当前的模型覆盖度不支撑该 claim。
  
  Abstract 中 "≥99.33% across all four models" 的表述在 DeepSeek 排除了 1/3 seed 后才成立（若含 seed 123，3-seed mean = 96.58%）。

- 建议：将 "architecture-independent" 降级为 "consistent across three tested code-specialized architecture families"；明确报告 DeepSeek 含全部 seed 的均值。

**W3** [warning] DebugBench 天花板效应使其无法独立验证 trace 贡献

- 具体位置：Section 4.6 line 167-168, Appendix I Table 11
- 问题：DebugBench no_trace 已达 96.71%，仅剩 3.29pp headroom。exception_only 100% (N=426) 的 CI 下界为 99.14%，与 VOTA 99.77% (CI [99.30, 100.00]) 高度重叠。这三个条件在统计上不可区分。
  
  论文在 Abstract line 26 和 Conclusion line 6 中引用 DebugBench 100% 作为 "generalization" 证据，但 Appendix I line 488-489 自己承认 "narrow margins are insufficient to independently validate trace importance"。这种在正文高调引用、在附录低调限定的模式对读者不公平。

- 建议：在 Abstract/Conclusion 中引用 DebugBench 时加限定语（"ranking preserved despite ceiling effect"），或在正文主体中讨论天花板效应。

**W4** [warning] 2,048 token 截断对不同条件的差异化影响构成混淆变量

- 具体位置：Section 2.4 line 40, Appendix H line 215-216
- 问题：exception_only（median 150 tokens）基本不受截断影响，而 VOTA 在 DeepSeek 上 91.7% 样本被截断（mean 2,626 tokens）。full_trace 也严重受截断影响。当论文比较 exception_only vs VOTA vs full_trace 时，实际上在比较 "未截断条件 vs 严重截断条件"，而非纯粹的 "trace content 差异"。
  
  虽然 Qwen 的 VOTA 截断率低得多（mean 1,929 tokens）且仍然 <exception_only，但 DeepSeek 的 14.96pp VOTA 差距中截断贡献多大、内容贡献多大，无法分离。

- 建议：(1) 报告各条件各模型的截断率；(2) 在 Qwen（截断率低）上重点做 VOTA vs exception_only 比较；(3) 讨论截断作为混淆变量的影响。

**W5** [warning] Qwen 既生成数据又做评估模型

- 具体位置：Section 2.2 line 12, Limitations line 46
- 问题：Qwen-2.5-Coder-7B-Instruct 以 temperature=0.8 生成 10 个候选解/problem，同时作为 4 个评估模型之一。虽然论文辩称 "does not affect verdict prediction but may influence the pass/fail distribution"，但更深层的问题是：Qwen 生成的代码风格、典型错误模式和 exception 类型可能与 Qwen 自身的 pretraining 分布高度一致，使得 Qwen 在识别 "自己写的代码" 的错误时具有不公平优势。这可能部分解释了 Qwen exception_only σ=0 的完美稳定性。

- 建议：讨论 self-familiarity bias 对各模型相对性能的潜在影响，而非仅在 Limitations 中一笔带过。

---

## 小问题（不影响接收）

- **orphan bib entry**: `dong2024composition` 在 .bib 中存在但未在论文中引用。
- **引用验证**: `eguchi2025etcot`, `ferrando2025execute` 在 OpenAlex 中未找到匹配（可能是较新论文/workshop paper 尚未收录），建议确认这些引用的真实性。
- **RTX PRO 6000 Blackwell**: Ethics Statement 说 "20 GPU-hours"（line 55），ARR checklist 说 "~50 GPU-hours"（line 48），数字不一致。
- **CodeLlama-13B** 在 Table 1 exception_only 报告的是 3-seed mean 99.89±0.10，但论文正文（experiments.tex line 36）说 "mean"。需要确认 CodeLlama 是否真的跑了 3 seeds（checklist 中没有明确提及 CodeLlama multi-seed）。
- **Figure 1 caption** (method.tex line 32): 列出的 accuracy 数字 (no_trace 75.13%, full_trace 81.76%, VOTA 99.41%, exception_only 99.83%) 是 Qwen-7B seed=42 的结果，但图示的 pipeline 是通用的，可能误导读者以为这些是 cross-model 数字。

---

## 缺失引用

- **SWE-bench** (Jimenez et al., 2024): 最相关的真实世界代码评估 benchmark，论文讨论 "real-world codebase" generalization 时应引用。
- **Test oracle literature**: verdict prediction 本质上是 test oracle 问题，缺少对 SE 领域 test oracle 工作的引用 (e.g., Barr et al. 2015 "The Oracle Problem in Software Testing")。
- **AlphaCode / AlphaCode2**: 大规模代码生成 + execution 验证的相关工作。
- **Pass@k / execution-based evaluation**: 论文使用 execution 作为 label source，应讨论与 Chen et al. 2021 中 pass@k 方法的关系。

---

## 主要优势

1. **研究问题清晰且有实际价值**：哪些 trace 成分对 verdict prediction 有用，这个问题对 trace-augmented code LLM 系统的设计有直接指导意义。
2. **消融设计系统化**：7 个 trace conditions 形成了一个结构良好的消融空间（full → VOTA → individual components → none），逻辑清晰。
3. **Limitations section 异常诚实**：坦诚讨论了 DeepSeek seed 问题、数据生成循环、self-familiarity bias、GeneratorExit ambiguity 等，很多审稿人会发现的问题作者自己都提到了。
4. **附录详实**：13 个附录 section 提供了充分的补充实验、per-class breakdown、error analysis，展示了 thorough 的实验工作。
5. **Tail-truncation 实验**（Section 4.6, Appendix G Table 9-10）设计巧妙，positional concentration 的发现（256-512 token window from terminus）有独立价值。
6. **Information density decomposition 的思路**（即使执行上有 N2 的问题）作为概念框架有启发性。

---

## Questions to Authors

1. 请提供全部主要实验（Table 1-4）在 deduplicated test set (n=607) 上的 CI 和 p-value。McNemar test B5 vs SFT 在 n=607 下是否仍然显著？
2. DeepSeek exception_only 3-seed mean（含 seed 123）为 96.58%，而非排除后的 99.33%。你们如何为排除 1/3 seed 作为 "outlier" 辩护？
3. label_only 是否在其他模型或 seed 上复现过？26%/74% 数字的跨模型稳定性如何？
4. 论文声称 "~91% semantic"，但如果以 SFT vs B5 的 0.50pp 增量来衡量，SFT 学到的 "beyond format" 的语义理解仅覆盖 2 个 problem。如何回应 "B5 几乎已经解决了这个任务" 的批评？
5. CodeLlama-13B exception_only 是否真的跑了 3 seeds？如果是，为什么 Appendix D (Table 8, 9) 中没有 CodeLlama multi-seed 的完整结果表？

---

向 Director 提交报告。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "302f6f9d-8637-4d79-b989-eb7898629cca",
  "isSidechain": false,
  "requestId": "req_011Cb8awtKJpy45vFmpkBmFT",
  "type": "assistant",
  "uuid": "b84bccdc-979d-42de-aedc-354be7da73fb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/.claude/sessions/review_reviewer_1_7624f219",
  "sessionId": "f76386b4-9d1f-4f92-b831-706bc4acd94d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JzwFkHZohRUw9mzx29VEBB",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9522,
      "cache_read_input_tokens": 67901,
      "output_tokens": 9563,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 9522,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 9563,
          "cache_read_input_tokens": 67901,
          "cache_creation_input_tokens": 9522,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 9522
          },
          "type": "message"
        }
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

_source line 56 · 2026-05-17T18:10:25.432Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director · `toolu_01NYibm3PsxpEawutyxv2R9d`</summary>

```json
{
  "text": "## Reviewer 1 — Round 1 审稿报告\n\n**审查侧重**: 方法严谨性 + 实验设计 + 统计有效性 + 可复现性\n\n---\n\n### 总体评分\n\n**Overall Assessment**: 3.0 (Findings)\n**一句话总结**: Exception dominance 是一个有价值的经验发现，但测试集 49% 重复样本从根本上破坏了所有统计推断的有效性，加上 6/7 条件为单 seed、核心 \"learned semantic understanding\" claim 仅依赖于一个 0.50pp 的边际增量，整体证据强度不足以支撑论文的强因果性声明。\n\n---\n\n### 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 2.5/5 | 测试集重复样本违反统计独立性假设，所有 CI/p 值均不可信；26%/74% 分解缺乏因果有效性；format marker 使核心 claim 的增量仅 0.50pp |\n| Excitement | 3/5 | \"Exception events suffice\" 对 trace-augmented systems 有实际指导意义，但 verdict prediction 本身是 narrow task，且核心发现可被 regex B5 复现到 99.33% |\n| Reproducibility | 3/5 | 超参数报告完整，但代码/数据未发布；单 seed 占多数条件；DeepSeek full_trace 初始 run 被废弃的处理缺乏透明度 |\n| Confidence | 4/5 | 仔细阅读全文含附录，熟悉 code LLM fine-tuning 和统计方法论 |\n\n---\n\n### Must-Fix 问题（3 个 critical）\n\n**N1** [critical] 测试集 49% 重复样本系统性破坏全部统计推断\n- exception_only 测试集 1,190 样本仅 607 unique (Section 2.2)\n- 正文所有 CI、p-value 基于 n=1,190 独立性假设，Appendix H 承认 deduplicated CI 更宽但仅一笔带过\n- Wilson CI、paired bootstrap、McNemar test 均受影响\n- B5 vs SFT McNemar p=0.041 在有效 n=607 下很可能不再显著\n- 建议：以 deduplicated n=607 或 cluster-robust bootstrap 为主要统计指标\n\n**N2** [critical] 26%/74% gradient dilution vs information overload 分解缺乏因果有效性\n- label_only 改变了 loss function 和梯度分布，不仅是\"减少 gradient dilution\"\n- 加法分解假设未经验证，且仅基于 Qwen-7B 单 seed\n- Abstract/Contribution 中使用 \"~26%/~74%\" 给读者错误的定量精度感\n- 建议：降级为\"近似描述性分解\"，讨论混淆变量\n\n**N3** [critical] Format marker 使 SFT 的 \"learned semantic understanding\" claim 仅依赖 0.50pp\n- B5 regex 凭 [No exception data in trace] marker 达 99.33%，SFT 仅多 0.50pp\n- 全部增量来自 2 个 distinct problems 的 6 个样本\n- McNemar p=0.041 边际显著，考虑 N1 去重后很可能不显著\n- \"91% semantic\" 的计算方式有争议（shortcut learning 效应）\n\n### Should-Fix 问题（5 个 warning）\n\n**W1** 6/7 条件单 seed，Tier 层级稳定性未知\n**W2** \"Architecture-independent\" 声明过度（3 个 code-specialized 家族，其中 1 个不稳定）\n**W3** DebugBench 天花板效应（no_trace 已 96.71%）使其无法独立验证 trace 贡献\n**W4** 2,048 token 截断率在条件间差异巨大（0% vs 91.7%），构成混淆变量\n**W5** Qwen 既生成数据又做评估模型，self-familiarity bias 讨论不足\n\n### 小问题\n- orphan bib: dong2024composition 未被引用\n- GPU-hours 不一致：Ethics 20h vs checklist 50h\n- CodeLlama multi-seed 完整结果缺失\n- 2 个引用 (eguchi2025etcot, ferrando2025execute) OpenAlex 未验证\n\n### 主要优势\n1. 研究问题清晰有实际价值\n2. 7 条件消融设计系统化\n3. Limitations section 异常诚实\n4. 附录详实（13 sections）\n5. Tail-truncation positional concentration 发现有独立价值\n\n### 缺失引用\n- SWE-bench, test oracle literature (Barr et al. 2015), AlphaCode\n\n### Questions to Authors\n1. deduplicated test set 上所有 CI 和 p-value？\n2. 排除 DeepSeek 1/3 seed 的统计依据？\n3. label_only 在其他模型上的复现结果？\n4. 如何回应\"B5 几乎已经解决了这个任务\"的批评？\n5. CodeLlama multi-seed 完整结果？",
  "reviewer_id": "1",
  "project": "trace-verdict-study"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b84bccdc-979d-42de-aedc-354be7da73fb",
  "isSidechain": false,
  "requestId": "req_011Cb8awtKJpy45vFmpkBmFT",
  "type": "assistant",
  "uuid": "76c46e03-0cb0-49a7-afaf-17d6107b98b8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/.claude/sessions/review_reviewer_1_7624f219",
  "sessionId": "f76386b4-9d1f-4f92-b831-706bc4acd94d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JzwFkHZohRUw9mzx29VEBB",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9522,
      "cache_read_input_tokens": 67901,
      "output_tokens": 9563,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 9522,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 9563,
          "cache_read_input_tokens": 67901,
          "cache_creation_input_tokens": 9522,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 9522
          },
          "type": "message"
        }
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

_source line 57_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[Round 1 审稿请求]: ## Round 1 审稿任务 — Reviewer 1  **你的审查侧重**: 方法严谨性 + 实验设计 + 统计有效性 + 可复现性  ### Venue 信息 - **目标**: EMNLP 2026 via ARR May 2026 cycle - **截止日期**: 2026-05-25 - **页数限制**: Long paper ≤ 8 页正文（不含…",
  "leafUuid": "76c46e03-0cb0-49a7-afaf-17d6107b98b8",
  "sessionId": "f76386b4-9d1f-4f92-b831-706bc4acd94d"
}
```

---


### Runtime record

_source line 58_

```json
{
  "type": "ai-title",
  "aiTitle": "Round 1 peer review for trace verdict prediction paper",
  "sessionId": "f76386b4-9d1f-4f92-b831-706bc4acd94d"
}
```

---


### Tool result

_source line 59 · 2026-05-17T18:10:29.128Z_

<details><summary>↩ Tool result · `toolu_01NYibm3PsxpEawutyxv2R9d`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_47a2f37b5c77af2e2351362f8def77a1:director\"}, \"error\": \"\"}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "76c46e03-0cb0-49a7-afaf-17d6107b98b8",
  "isSidechain": false,
  "promptId": "b73967ab-1e3d-4502-97ef-ede23a2a2cd7",
  "type": "user",
  "uuid": "be1d4379-f052-4372-a175-d881703da1fa",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"review_director_key\\\": \\\"feishu:group:oc_47a2f37b5c77af2e2351362f8def77a1:director\\\"}, \\\"error\\\": \\\"\\\"}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_47a2f37b5c77af2e2351362f8def77a1:director\"}, \"error\": \"\"}"
    }
  },
  "sourceToolAssistantUUID": "76c46e03-0cb0-49a7-afaf-17d6107b98b8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/.claude/sessions/review_reviewer_1_7624f219",
  "sessionId": "f76386b4-9d1f-4f92-b831-706bc4acd94d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Runtime record

_source line 60_

```json
{
  "type": "ai-title",
  "aiTitle": "Round 1 peer review for trace verdict prediction paper",
  "sessionId": "f76386b4-9d1f-4f92-b831-706bc4acd94d"
}
```

---


### Runtime record

_source line 61 · 2026-05-18T12:29:46.196Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-18T12:29:46.196Z",
  "sessionId": "f76386b4-9d1f-4f92-b831-706bc4acd94d",
  "content": "[Round 1 审稿请求]:\n[Dream 审稿任务 — Reviewer 1：方法 + 实验]\n\n论文标题：Exception Events Are All You Need: Fault Detection Signals for Verdict Prediction in Execution Traces\n\nPDF 路径：/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/artifacts/dream_reports/dream_20260518T113804/median/review_input_e90a5c14.pdf\n\n实验设计参考（含完整 planned experiments 列表）：/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/artifacts/dream_reports/dream_20260518T113804/median/review_context.yaml\n\n按 top ML venue 通用标准审稿（接受率 ~25%，6 分制：1=Strong Reject … 6=Strong Accept）。\n\n你的审查侧重：\n- **方法描述**：是否完整、claim 是否被实验数据支撑、关键超参 / 训练流程是否清晰\n- **实验设计**：是否覆盖关键 baseline / ablation / 跨数据集 / scale 维度\n- **数据呈现**：表格 / 图是否能让审稿人复现结论、误差棒 / 统计显著性是否充分\n\n请基于论文内容独立评判，不要假设论文结果的质量高低。\n\n**不要评判**：新颖性 / 相关工作（那是 Reviewer 2 的范围）、格式 / 排版。\n\n**Dream 审稿边界提醒**：\n- 不需要评审：Reproducibility checklist、代码/数据可用性、具体数值精确性（数字是想象的，关注实验设计而非数值）、伦理/IRB、匿名性\n- 需要评审但标注为 \"presentation 层面\"：Reference 真实性、论文完整度、Related Work 引用数量\n- 必须评审（idea 层面）：实验设计是否足以支撑 claims（假设数据为真）、叙事逻辑是否自洽、Claim 的 generality 是否被实验范围支撑\n- 每条 weakness 必须标注属于 **idea 层面** 还是 **presentation 层面**\n\n评分校准规则：\n- 3+ Major issues → 不高于 Borderline Reject\n- 2 Major issues → 不高于 Weak Accept\n- 1 Major issue → 不高于 Accept\n- 0 Major issues → 可给 Strong Accept\n- Major issue 定义：实验范围不足以支撑 claim generality、Related Work 缺失导致 novelty 不可验证、核心实验不可复现（缺关键细节）、统计不显著的结果被作为 contribution\n\n请通过 `review_reviewer_post_to_director(text, reviewer_id=\"1\", project=\"trace-verdict-study\", dream_id=\"20260518T113804\")` 汇报。"
}
```

---


### Runtime record

_source line 62 · 2026-05-18T12:29:46.197Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-18T12:29:46.197Z",
  "sessionId": "f76386b4-9d1f-4f92-b831-706bc4acd94d"
}
```

---


## Round 2

## Round 2

2 recorded events


### User

_source line 63 · 2026-05-18T12:29:46.186Z_

Continue from where you left off.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "be1d4379-f052-4372-a175-d881703da1fa",
  "isSidechain": false,
  "promptId": "b72b12af-1fe0-4898-8183-7d12f8920502",
  "type": "user",
  "isMeta": true,
  "uuid": "937cfcf0-8358-4f10-b4e0-1f4c395b473c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/.claude/sessions/review_reviewer_1_7624f219",
  "sessionId": "f76386b4-9d1f-4f92-b831-706bc4acd94d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Assistant

_source line 64 · 2026-05-18T12:29:46.187Z_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "937cfcf0-8358-4f10-b4e0-1f4c395b473c",
  "isSidechain": false,
  "type": "assistant",
  "uuid": "23665448-1b70-4b2e-b4d5-b806a44668f9",
  "isApiErrorMessage": false,
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/.claude/sessions/review_reviewer_1_7624f219",
  "sessionId": "f76386b4-9d1f-4f92-b831-706bc4acd94d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "id": "dde9f83f-d72d-401e-97b6-6403c3e66b6f",
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

87 recorded events


### User

_source line 65 · 2026-05-18T12:29:46.279Z_

[Round 1 审稿请求]:
[Dream 审稿任务 — Reviewer 1：方法 + 实验]

论文标题：Exception Events Are All You Need: Fault Detection Signals for Verdict Prediction in Execution Traces

PDF 路径：/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/artifacts/dream_reports/dream_20260518T113804/median/review_input_e90a5c14.pdf

实验设计参考（含完整 planned experiments 列表）：/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/artifacts/dream_reports/dream_20260518T113804/median/review_context.yaml

按 top ML venue 通用标准审稿（接受率 ~25%，6 分制：1=Strong Reject … 6=Strong Accept）。

你的审查侧重：
- **方法描述**：是否完整、claim 是否被实验数据支撑、关键超参 / 训练流程是否清晰
- **实验设计**：是否覆盖关键 baseline / ablation / 跨数据集 / scale 维度
- **数据呈现**：表格 / 图是否能让审稿人复现结论、误差棒 / 统计显著性是否充分

请基于论文内容独立评判，不要假设论文结果的质量高低。

**不要评判**：新颖性 / 相关工作（那是 Reviewer 2 的范围）、格式 / 排版。

**Dream 审稿边界提醒**：
- 不需要评审：Reproducibility checklist、代码/数据可用性、具体数值精确性（数字是想象的，关注实验设计而非数值）、伦理/IRB、匿名性
- 需要评审但标注为 "presentation 层面"：Reference 真实性、论文完整度、Related Work 引用数量
- 必须评审（idea 层面）：实验设计是否足以支撑 claims（假设数据为真）、叙事逻辑是否自洽、Claim 的 generality 是否被实验范围支撑
- 每条 weakness 必须标注属于 **idea 层面** 还是 **presentation 层面**

评分校准规则：
- 3+ Major issues → 不高于 Borderline Reject
- 2 Major issues → 不高于 Weak Accept
- 1 Major issue → 不高于 Accept
- 0 Major issues → 可给 Strong Accept
- Major issue 定义：实验范围不足以支撑 claim generality、Related Work 缺失导致 novelty 不可验证、核心实验不可复现（缺关键细节）、统计不显著的结果被作为 contribution

请通过 `review_reviewer_post_to_director(text, reviewer_id="1", project="trace-verdict-study", dream_id="20260518T113804")` 汇报。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "23665448-1b70-4b2e-b4d5-b806a44668f9",
  "isSidechain": false,
  "promptId": "b72b12af-1fe0-4898-8183-7d12f8920502",
  "type": "user",
  "uuid": "094a9fff-8a35-4535-bad4-ff6939ceffdc",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/.claude/sessions/review_reviewer_1_7624f219",
  "sessionId": "f76386b4-9d1f-4f92-b831-706bc4acd94d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Assistant

_source line 66 · 2026-05-18T12:30:01.422Z_

<details><summary>Logged reasoning block</summary>

```text
The user is asking me to review a "dream" paper - this is a different paper/PDF from the one I reviewed before. Let me read the PDF and the review context YAML file first, then produce a review.

Let me start by reading both files.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "094a9fff-8a35-4535-bad4-ff6939ceffdc",
  "isSidechain": false,
  "requestId": "req_011CbA33je7ooLDeN7cdJbrY",
  "type": "assistant",
  "uuid": "c6d05e67-05a0-44c7-8f10-fb36993904af",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/.claude/sessions/review_reviewer_1_7624f219",
  "sessionId": "f76386b4-9d1f-4f92-b831-706bc4acd94d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018aL8zbqzZejDEkEiANxdtD",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 76065,
      "cache_read_input_tokens": 11841,
      "output_tokens": 343,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 76065,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 343,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 76065,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 76065
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


### Assistant

_source line 67 · 2026-05-18T12:30:02.595Z_

开始 Dream 审稿。先并行读取 PDF 和实验设计参考文件。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c6d05e67-05a0-44c7-8f10-fb36993904af",
  "isSidechain": false,
  "requestId": "req_011CbA33je7ooLDeN7cdJbrY",
  "type": "assistant",
  "uuid": "a84cecb5-63f3-417e-a944-3df644f3aaa1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/.claude/sessions/review_reviewer_1_7624f219",
  "sessionId": "f76386b4-9d1f-4f92-b831-706bc4acd94d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018aL8zbqzZejDEkEiANxdtD",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 76065,
      "cache_read_input_tokens": 11841,
      "output_tokens": 343,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 76065,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 343,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 76065,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 76065
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

_source line 68 · 2026-05-18T12:30:03.621Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images · `toolu_01AMHgCSLAKRfQvxCHZgX6mK`</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/artifacts/dream_reports/dream_20260518T113804/median/review_input_e90a5c14.pdf",
  "pages": "1-10",
  "dpi": 200
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a84cecb5-63f3-417e-a944-3df644f3aaa1",
  "isSidechain": false,
  "requestId": "req_011CbA33je7ooLDeN7cdJbrY",
  "type": "assistant",
  "uuid": "4fdc5a50-f091-4749-8ee0-639b1b651918",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/.claude/sessions/review_reviewer_1_7624f219",
  "sessionId": "f76386b4-9d1f-4f92-b831-706bc4acd94d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018aL8zbqzZejDEkEiANxdtD",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 76065,
      "cache_read_input_tokens": 11841,
      "output_tokens": 343,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 76065,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 343,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 76065,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 76065
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

_source line 69 · 2026-05-18T12:30:03.818Z_

<details><summary>↩ Tool result · `toolu_01AMHgCSLAKRfQvxCHZgX6mK`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"页码超出范围 (共 9 页): 1-10\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4fdc5a50-f091-4749-8ee0-639b1b651918",
  "isSidechain": false,
  "promptId": "b72b12af-1fe0-4898-8183-7d12f8920502",
  "type": "user",
  "uuid": "0e4b7683-a285-435d-b5be-34ca49722c89",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {}, \\\"error\\\": \\\"页码超出范围 (共 9 页): 1-10\\\", \\\"metadata\\\": {}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {}, \"error\": \"页码超出范围 (共 9 页): 1-10\", \"metadata\": {}}"
    }
  },
  "sourceToolAssistantUUID": "4fdc5a50-f091-4749-8ee0-639b1b651918",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/.claude/sessions/review_reviewer_1_7624f219",
  "sessionId": "f76386b4-9d1f-4f92-b831-706bc4acd94d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Tool call

_source line 70 · 2026-05-18T12:30:04.191Z_

<details open><summary>🔧 Tool call — Read · `toolu_015tvvh4dQcdepA2BeGQnTar`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/artifacts/dream_reports/dream_20260518T113804/median/review_context.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0e4b7683-a285-435d-b5be-34ca49722c89",
  "isSidechain": false,
  "requestId": "req_011CbA33je7ooLDeN7cdJbrY",
  "type": "assistant",
  "uuid": "cb0eef11-4964-4f98-9320-76b06ff93624",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/.claude/sessions/review_reviewer_1_7624f219",
  "sessionId": "f76386b4-9d1f-4f92-b831-706bc4acd94d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018aL8zbqzZejDEkEiANxdtD",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 76065,
      "cache_read_input_tokens": 11841,
      "output_tokens": 343,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 76065,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 343,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 76065,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 76065
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

_source line 71 · 2026-05-18T12:30:04.576Z_

<details><summary>↩ Tool result · `toolu_015tvvh4dQcdepA2BeGQnTar`</summary>

```text
1	narrative_guidance: 'Median 档结果总结：7 个 planned 实验全部符合 ''pattern exists but model-dependent''
2	  预期。 plan_016 (tail-384) 确认 phase transition 存在但 sharpness 分化为两组——强模型 (Qwen-7B, CodeLlama-13B)
3	  gradual，弱模型 (DeepSeek, Qwen-1.5B) sharp——''universal sharp phase transition'' 降级为
4	  ''consistent trend with model-dependent transition characteristics''。plan_017 (cross-seed)
5	  std 范围 0.4-3.5pp 证明 budget curve reproducible 但 variance 与模型强度相关。plan_019 确认 exception_only
6	  near-perfect calibration 跨 4 模型通用（非离群 ECE ≤ 0.01）。plan_020 确认 SFT 优于 frontier model
7	  few-shot 3-5pp，支持 SFT practical recommendation 但非压倒性优势。 plan_018 和 plan_022 提供 supporting
8	  evidence 但不升级任何 claim。plan_021 是最大风险——跨语言 泛化可能大幅降级。总体：Claim 1 + Claim 3 核心证据不受影响，budget
9	  curve 保留为 supporting evidence， EMNLP main 有竞争力 (P≈0.35-0.45) 但 scope concern + model-dependent
10	  phase transition 需 strong rebuttal。
11	
12	  '
13	imagined_experiments:
14	- name: fine_grained_phase_transition_tail384
15	  plan_id: plan_016
16	  description: tail-384 × 4 模型，精确定位 256→512 phase transition 是 sharp 还是 gradual
17	  expected_results:
18	    qwen7b_tail384_accuracy: 0.855
19	    qwen7b_tail384_ci:
20	    - 0.832
21	    - 0.877
22	    qwen7b_delta_vs_tail256_pp: 6.6
23	    qwen7b_delta_vs_tail512_pp: -8.1
24	    qwen7b_transition_type: gradual
25	    deepseek_tail384_accuracy: 0.805
26	    deepseek_tail384_ci:
27	    - 0.781
28	    - 0.829
29	    deepseek_delta_vs_tail256_pp: 4.1
30	    deepseek_delta_vs_tail512_pp: -13.4
31	    deepseek_transition_type: sharp
32	    qwen15b_tail384_accuracy: 0.79
33	    qwen15b_tail384_ci:
34	    - 0.765
35	    - 0.815
36	    qwen15b_delta_vs_tail256_pp: 6.4
37	    qwen15b_delta_vs_tail512_pp: -16.6
38	    qwen15b_transition_type: sharp
39	    codellama13b_tail384_accuracy: 0.875
40	    codellama13b_tail384_ci:
41	    - 0.854
42	    - 0.896
43	    codellama13b_delta_vs_tail256_pp: 9.6
44	    codellama13b_delta_vs_tail512_pp: -10.0
45	    codellama13b_transition_type: gradual
46	    four_model_mean: 0.831
47	    sharp_models_mean: 0.798
48	    gradual_models_mean: 0.865
49	    max_diff_vs_tail256_pp: 9.6
50	  result_rationale: 'tail-384 处于 256→512 相变区间中段。信号来源：exception events 集中在 trace 末尾，tail-384
51	    能捕获约 50-65% 的 exception 信息（vs tail-256 ~30%, tail-512 ~90%）。模型分化原因： (1) 强模型（Qwen-7B
52	    CRUXEval-I 56.5%, CodeLlama-13B 13B参数）能从 partial exception 信息中推理出 verdict，因此 384
53	    tokens 已显著提升——呈 gradual transition； (2) 弱模型（DeepSeek CRUXEval-I 39%, Qwen-1.5B
54	    仅 1.5B 参数）需要 near-complete exception 信号才能有效利用，384 tokens 提升有限，大部分增益集中在 384→512
55	    区间——呈 sharp transition。CodeLlama 虽然 tokenizer 不同（LLaMA BPE），但其 13B 参数量补偿了 tokenizer
56	    差异，在 384 tokens 处已能有效提取 diagnostic signal。DeepSeek 受限于 base model 的 trace reasoning
57	    能力（CRUXEval-I 39%），需要更完整的 exception 上下文。Qwen-1.5B 因模型容量极小， loss landscape 更陡峭，384
58	    tokens 的 noisy partial signal 难以稳定学习。
59	
60	    '
61	  tables:
62	  - title: 'Budget Curve: tail Truncation × 4 Models (含 tail-384 新数据点)'
63	    headers:
64	    - Model
65	    - tail-256 (%)
66	    - tail-384 (%)
67	    - tail-512 (%)
68	    - tail-1024 (%)
69	    - tail-2048 (%)
70	    - Δ(256→384)
71	    - Δ(384→512)
72	    - Transition
73	    rows:
74	    - - Qwen-7B
75	      - 78.9
76	      - 85.5
77	      - 93.6
78	      - 96.5
79	      - 97.3
80	      - +6.6pp
81	      - +8.1pp
82	      - Gradual
83	    - - DeepSeek-6.7B
84	      - 76.4
85	      - 80.5
86	      - 93.9
87	      - 96.5
88	      - 95.0
89	      - +4.1pp
90	      - +13.4pp
91	      - Sharp
92	    - - Qwen-1.5B
93	      - 72.6
94	      - 79.0
95	      - 95.6
96	      - 96.6
97	      - 97.9
98	      - +6.4pp
99	      - +16.6pp
100	      - Sharp
101	    - - CodeLlama-13B
102	      - 77.9
103	      - 87.5
104	      - 97.5
105	      - 98.2
106	      - collapse
107	      - +9.6pp
108	      - +10.0pp
109	      - Gradual
110	  figures_description:
111	  - 'Budget curve figure (4-panel or overlay): x-axis = tail token budget [256, 384,
112	    512, 1024, 2048], y-axis = accuracy (%)。4 条模型曲线，384 处标注 transition type。Gradual
113	    模型（Qwen-7B, CodeLlama）曲线在 256→512 段近似线性上升；Sharp 模型（DeepSeek, Qwen-1.5B）曲线在 256→384
114	    段平缓、384→512 段陡升，呈 S 型。水平虚线标注 exception_only ceiling (99.83%)。'
115	  - 'Transition sharpness scatter: x-axis = model capability proxy (CRUXEval-I 或 param
116	    count), y-axis = Δ(384-256)/Δ(512-256) ratio (越高越 gradual)。4 点+回归线，展示 capability→gradualness
117	    正相关。'
118	  analysis: 'tail-384 结果确认 phase transition 存在但 sharpness 是 model-dependent property。
119	    两组分化模式清晰：强模型 gradual（Δ256→384 ≈ Δ384→512），弱模型 sharp（Δ384→512 >> Δ256→384）。 这直接影响论文
120	    claim：不能说 ''universal sharp phase transition at ~512 tokens''，需降级为 ''consistent
121	    accuracy improvement trend with model-dependent transition characteristics: stronger
122	    models show gradual onset while weaker models exhibit sharper thresholds''。 积极面：4-model
123	    mean (83.1%) 显著高于 tail-256 mean (76.5%)，证明 384 tokens 确实包含 有用信号；且所有模型在 tail-512
124	    均达 93%+，证明 transition 终点 universal。Phase transition figure 保留价值，但 discussion 必须新增
125	    model-dependency caveat 和 transition sharpness 与 model capability 的相关性分析。
126	
127	    '
128	- name: cross_seed_budget_curve_tail512
129	  plan_id: plan_017
130	  description: tail-512 × 4 models × 3 seeds，验证 phase transition 后 convergence band
131	    robustness
132	  expected_results:
133	    qwen7b_seed42: 0.936
134	    qwen7b_seed123: 0.924
135	    qwen7b_seed456: 0.943
136	    qwen7b_mean: 0.934
137	    qwen7b_std_pp: 1.0
138	    deepseek_seed42: 0.939
139	    deepseek_seed123: 0.885
140	    deepseek_seed456: 0.942
141	    deepseek_mean: 0.922
142	    deepseek_std_pp: 3.2
143	    qwen15b_seed42: 0.956
144	    qwen15b_seed123: 0.9
145	    qwen15b_seed456: 0.938
146	    qwen15b_mean: 0.931
147	    qwen15b_std_pp: 2.9
148	    codellama13b_seed42: 0.975
149	    codellama13b_seed123: 0.968
150	    codellama13b_seed456: 0.978
151	    codellama13b_mean: 0.974
152	    codellama13b_std_pp: 0.5
153	    max_std_across_models_pp: 3.2
154	    strong_model_avg_std_pp: 0.75
155	    weak_model_avg_std_pp: 3.05
156	  result_rationale: 'Cross-seed variance 反映 LoRA 初始化对 tail-512 budget 条件下的 trace learning
157	    稳定性。 逻辑链：tail-512 包含足够的 exception 信息但也包含 non-diagnostic noise（loop 片段、变量 赋值）。强模型（Qwen-7B,
158	    CodeLlama-13B）的 LoRA landscape 较平滑，不同初始化均收敛到 类似的 trace→verdict 映射，std < 1pp。弱模型（DeepSeek,
159	    Qwen-1.5B）的 LoRA landscape 更 rugged：(1) DeepSeek 在 exception_only 上已显示 seed sensitivity
160	    (seed123=91.09% vs seed42/456=99.33%)，tail-512 的更复杂 input 放大这一效应——某些 seed 未学到有效的
161	    noise filtering，被 non-exception tokens 干扰；(2) Qwen-1.5B 参数量仅 1.5B，LoRA rank 相对于
162	    total params 的比例更高，初始化影响更大。DeepSeek seed123 (88.5%) 呼应其 exception_only seed123
163	    (91.09%) 的 pattern——同一 LoRA 初始化弱点在更复杂 input 下进一步暴露。 CodeLlama-13B std 最小 (0.5pp)
164	    因其 13B 参数量提供最大 learning capacity，tail-512 的 signal 对其而言接近 trivial。
165	
166	    '
167	  tables:
168	  - title: Cross-seed tail-512 Robustness (3 seeds × 4 models)
169	    headers:
170	    - Model
171	    - Seed42
172	    - Seed123
173	    - Seed456
174	    - Mean
175	    - Std
176	    - Band Width
177	    rows:
178	    - - Qwen-7B
179	      - 93.6%
180	      - 92.4%
181	      - 94.3%
182	      - 93.4%
183	      - 1.0pp
184	      - 1.9pp
185	    - - DeepSeek-6.7B
186	      - 93.9%
187	      - 88.5%
188	      - 94.2%
189	      - 92.2%
190	      - 3.2pp
191	      - 5.7pp
192	    - - Qwen-1.5B
193	      - 95.6%
194	      - 90.0%
195	      - 93.8%
196	      - 93.1%
197	      - 2.9pp
198	      - 5.6pp
199	    - - CodeLlama-13B
200	      - 97.5%
201	      - 96.8%
202	      - 97.8%
203	      - 97.4%
204	      - 0.5pp
205	      - 1.0pp
206	  - title: Strong vs Weak Model Seed Stability 对比
207	    headers:
208	    - Group
209	    - Models
210	    - Avg Std
211	    - Avg Band Width
212	    - Interpretation
213	    rows:
214	    - - Strong
215	      - Qwen-7B + CodeLlama-13B
216	      - 0.75pp
217	      - 1.5pp
218	      - 'Near-deterministic: LoRA landscape smooth'
219	    - - Weak
220	      - DeepSeek + Qwen-1.5B
221	      - 3.05pp
222	      - 5.7pp
223	      - 'Seed-sensitive: LoRA landscape rugged'
224	  figures_description:
225	  - 'Band plot: x-axis = tail token budget, y-axis = accuracy。每个模型一条中线 (mean) + shaded
226	    band (min-max across 3 seeds)。强模型 band 窄，弱模型 band 宽。在 tail-512 处用 error bar 标注
227	    3-seed CI。'
228	  - 'Seed variance vs model capability scatter: x-axis = CRUXEval-I (或 param count
229	    log scale), y-axis = tail-512 3-seed std (pp)。4 点 + power fit，展示 capability↑ →
230	    variance↓ 趋势。'
231	  analysis: 'Cross-seed 结果确认 budget curve pattern reproducible——所有模型 3-seed mean 均在
232	    92-97% 区间，transition 后 convergence 一致。但 variance 的 model-dependency 加强了论文必须 使用的
233	    hedged language：不能说 ''tail-512 reliably achieves >93%''，需改为 ''tail-512 mean accuracy
234	    ≥ 92% across models, with tighter convergence on stronger models (std < 1pp) and
235	    wider bands on weaker models (std 2-3pp)''。审稿人问 ''single-seed robustness'' 时可展示此数据回应。实际价值：证明
236	    budget curve 的 rank ordering (tail-2048 > tail-1024 > tail-512 > tail-384 > tail-256)
237	    在所有 seeds 上保持，trend 本身 robust； absolute performance 的 seed sensitivity 是 LoRA
238	    training 问题而非 signal 问题——与 exception_only 的 seed pattern 一致 (D9)。
239	
240	    '
241	- name: error_analysis_failure_modes
242	  plan_id: plan_018
243	  description: 分析 exception_only/vota/full_trace/no_trace 的 failure modes，重点 Tier
244	    1 vs Tier 2 差异
245	  expected_results:
246	    qwen_exception_only_errors: 2
247	    qwen_exception_only_error_ids:
248	    - 901
249	    - 905
250	    qwen_exception_only_root_cause: 100% GeneratorExit (irreducible)
251	    qwen_exception_only_error_direction: 100% pass→fail false alarm
252	    qwen_vota_errors: 7
253	    qwen_vota_overlap_with_exception: 2
254	    qwen_vota_loop_artifact_errors: 3
255	    qwen_vota_attention_dilution_errors: 2
256	    qwen_vota_fail_to_pass_ratio: 0.57
257	    qwen_full_trace_errors: 217
258	    qwen_full_trace_long_trace_error_rate: 0.35
259	    qwen_full_trace_short_trace_error_rate: 0.08
260	    qwen_full_trace_fail_to_pass_fraction: 0.65
261	    qwen_full_trace_length_correlation_r: 0.42
262	    qwen_no_trace_errors: 296
263	    qwen_no_trace_fail_to_pass_fraction: 0.63
264	    qwen_no_trace_pass_to_fail_fraction: 0.37
265	    deepseek_seed123_errors: 106
266	    deepseek_seed123_fail_to_pass_fraction: 0.72
267	    deepseek_seed123_overlap_with_qwen_irreducible: 2
268	    exception_only_cross_model_jaccard: 0.85
269	    full_trace_cross_model_jaccard: 0.15
270	    no_trace_cross_model_jaccard: 0.25
271	  result_rationale: 'Error analysis 揭示不同 trace 条件的 qualitatively different failure
272	    modes： (1) Exception_only 的 2 个错误完全由 representation 决定（GeneratorExit 是 tracer
273	    设计 缺陷，非模型不足），跨模型高度重叠（Jaccard ≈ 0.85）——说明 irreducible errors 是 data/ representation
274	    property 而非 model property。 (2) VOTA 的额外 5 个错误来自 Tier 2 组件引入的 noise：loop compression
275	    有时产生误导性 摘要（3 例），Tier 2 tokens 稀释对 Tier 1 exception signal 的 attention（2 例）。这直接
276	    支持 Claim 3 的 ''combining tiers introduces noise'' 论点。 (3) Full_trace 错误与 trace
277	    长度强相关（r≈0.42）：>1500 tokens 的 trace 错误率 ~35% vs <500 tokens ~8%，information overload
278	    pattern 明确。错误以 fail→pass 为主（65%）， 说明模型在长 context 中找不到 fault signal，默认预测 majority
279	    class。 (4) No_trace 错误反映纯 majority class bias，无 systematic pattern。 (5) DeepSeek
280	    seed123 的 106 个错误集中在 fail→pass（72%），与 fail_recall=0.705 一致—— LoRA 初始化未学到 exception→fail
281	    映射的关键部分，尤其对 uncommon exception types。
282	
283	    '
284	  tables:
285	  - title: Error Mode Distribution by Condition (Qwen-7B)
286	    headers:
287	    - Condition
288	    - Total Errors
289	    - fail→pass (%)
290	    - pass→fail (%)
291	    - Dominant Pattern
292	    rows:
293	    - - exception_only
294	      - 2
295	      - 0%
296	      - 100%
297	      - GeneratorExit irreducible
298	    - - VOTA
299	      - 7
300	      - 57%
301	      - 43%
302	      - Tier 2 noise (loop artifacts + attention dilution)
303	    - - full_trace
304	      - 217
305	      - 65%
306	      - 35%
307	      - Information overload (length-correlated)
308	    - - no_trace
309	      - 296
310	      - 63%
311	      - 37%
312	      - Majority class bias
313	  - title: Error Rate by Trace Length (full_trace, Qwen-7B)
314	    headers:
315	    - Length Bucket
316	    - N Samples
317	    - Errors
318	    - Error Rate
319	    - Interpretation
320	    rows:
321	    - - <500 tokens
322	      - ~180
323	      - ~14
324	      - ~8%
325	      - 'Short traces: fault signal accessible'
326	    - - 500-1000 tokens
327	      - ~350
328	      - ~56
329	      - ~16%
330	      - 'Medium: partial signal loss'
331	    - - 1000-1500 tokens
332	      - ~380
333	      - ~76
334	      - ~20%
335	      - 'Long: significant overload'
336	    - - '>1500 tokens'
337	      - ~280
338	      - ~98
339	      - ~35%
340	      - 'Very long: severe information overload'
341	  - title: Cross-Model Error Overlap (Jaccard Index, exception_only non-outlier seeds)
342	    headers:
343	    - Model Pair
344	    - Jaccard
345	    - Shared Errors
346	    - Interpretation
347	    rows:
348	    - - Qwen-7B vs Qwen-1.5B
349	      - 0.9
350	      - 2/2 (both GeneratorExit)
351	      - Same representation → same irreducible errors
352	    - - Qwen-7B vs CodeLlama-13B
353	      - 0.8
354	      - 2/~2.5 avg
355	      - Different tokenizer but same root cause
356	    - - Qwen-7B vs DeepSeek (seed42)
357	      - 0.22
358	      - 2/~10
359	      - DeepSeek has 8 errors vs Qwen 2
360	  figures_description:
361	  - 'Confusion matrix grid (2×4): 4 conditions × Qwen-7B，展示 error direction 差异。exception_only
362	    和 VOTA 几乎完美（极少 off-diagonal），full_trace 和 no_trace 显示 fail→pass 偏移。'
363	  - 'Error rate vs trace length scatter (full_trace only): x-axis = input token count,
364	    y-axis = binary correct/incorrect，加 binned error rate 趋势线。展示 information overload
365	    的 dose-response 关系。'
366	  - 'Venn diagram: exception_only vs VOTA 错误重叠（Qwen-7B），展示 VOTA 额外错误全来自 Tier 2 noise。'
367	  analysis: 'Error analysis 为论文提供 3 个具体贡献：(1) 定量确认 exception_only 的 irreducible error
368	    来自 representation 而非模型（跨模型 Jaccard ≈ 0.85，跨 seed variance = 0）， 强化 ''99.83% =
369	    ceiling'' 论点；(2) VOTA 的 5 个额外错误全部可归因于 Tier 2 components， 直接 quantify 了 ''combining
370	    tiers introduces noise'' (Claim 3)；(3) full_trace 错误 与长度的正相关（r≈0.42）是 Claim 2
371	    information overload 假说的 direct evidence。 不足：error analysis 不能作为独立 contribution（审稿人视之为
372	    expected follow-up）， 但作为 Claim 1-3 的 supporting analysis 强化证据链。建议放在 Supplementary
373	    或 Appendix，正文引用关键数字。
374	
375	    '
376	- name: cross_model_calibration_exception_only
377	  plan_id: plan_019
378	  description: 4 models × exception_only ECE/Brier 对比，验证 calibration quality 跨模型通用
379	  expected_results:
380	    qwen7b_ece: 0.0027
381	    qwen7b_brier: 0.0013
382	    qwen7b_accuracy: 0.9983
383	    qwen15b_ece: 0.003
384	    qwen15b_brier: 0.0015
385	    qwen15b_accuracy: 0.9983
386	    codellama13b_ece: 0.002
387	    codellama13b_brier: 0.001
388	    codellama13b_accuracy: 0.9983
389	    deepseek_seed42_ece: 0.008
390	    deepseek_seed42_brier: 0.005
391	    deepseek_seed42_accuracy: 0.9933
392	    deepseek_seed123_ece: 0.085
393	    deepseek_seed123_brier: 0.075
394	    deepseek_seed123_accuracy: 0.9109
395	    four_model_nonoutlier_ece_max: 0.008
396	    four_model_nonoutlier_brier_max: 0.005
397	    ece_ratio_vs_no_trace_min: 21.0
398	    ece_ratio_vs_no_trace_max: 85.5
399	  result_rationale: 'Calibration quality 直接跟随 accuracy：exception_only 在 3 个模型上达 99.83%（仅
400	    2 个 相同错误），这些模型的 ECE/Brier 预期 near-identical——模型对 correct predictions 的 logit confidence
401	    接近 1.0，仅 2 个 misclassified samples 贡献微量 miscalibration。Qwen-7B 和 Qwen-1.5B 使用同系列
402	    tokenizer，exception signal 的 token 表示相同，因此 calibration 差异极小。CodeLlama-13B 因 13B
403	    参数量可能产生更 sharp 的 logit distribution，ECE 略低。 DeepSeek seed42 (99.33%, 8 errors)
404	    的 ECE 较高（~0.008）因为 4× 更多 errors 意味着 更多 bins 有非零 gap between confidence and accuracy。DeepSeek
405	    seed123 (91.09%) 是 outlier——fail_recall 仅 0.705 意味着模型对大量 actual-fail 样本输出 high-confidence
406	    pass 预测，造成严重 miscalibration (ECE ~0.085)。排除 seed123 outlier，4 模型 ECE 均 ≤ 0.008，与
407	    no_trace ECE (0.171) 相比至少 21×-85× 改善——确认 exception signal 不仅提升 accuracy 还 fundamentally
408	    improves model confidence calibration 跨模型通用。
409	
410	    '
411	  tables:
412	  - title: 'Cross-model Calibration: exception_only'
413	    headers:
414	    - Model
415	    - Accuracy
416	    - ECE
417	    - Brier
418	    - ECE ratio vs no_trace (0.171)
419	    - Notes
420	    rows:
421	    - - Qwen-7B
422	      - 99.83%
423	      - 0.0027
424	      - 0.0013
425	      - 63×
426	      - 3-seed confirmed; existing data
427	    - - Qwen-1.5B
428	      - 99.83%
429	      - 0.003
430	      - 0.0015
431	      - 57×
432	      - Same errors as 7B (id=901,905)
433	    - - CodeLlama-13B
434	      - 99.83%
435	      - 0.002
436	      - 0.001
437	      - 86×
438	      - Largest model → sharpest calibration
439	    - - DeepSeek (seed42/456)
440	      - 99.33%
441	      - 0.008
442	      - 0.005
443	      - 21×
444	      - 8 errors; still excellent
445	    - - DeepSeek (seed123) ⚠️
446	      - 91.09%
447	      - 0.085
448	      - 0.075
449	      - 2×
450	      - LoRA outlier; severely miscalibrated
451	  figures_description:
452	  - 'Reliability diagram (4-panel): 每个模型一个 calibration curve (predicted prob vs actual
453	    frequency)。3 个非离群模型的曲线几乎与 perfect calibration 对角线重合；DeepSeek seed123 curve 偏离对角线（overconfident
454	    on pass predictions for actual-fail samples）。'
455	  - 'ECE bar chart: 4 models × exception_only + Qwen-7B no_trace/full_trace/VOTA 作对照。exception_only
456	    的 bar 在所有模型上极短（≤0.008），no_trace bar (0.171) 显著突出。'
457	  analysis: 'Cross-model calibration 确认 exception signal 的 calibration 优势是 universal
458	    property 而非 Qwen-specific artifact。论文可 claim：''exception_only achieves near-perfect
459	    calibration (ECE ≤ 0.008) across 4 architecturally distinct models, a 21-86× improvement
460	    over no-trace baselines''。DeepSeek seed123 outlier 是 LoRA initialization problem
461	    而非 calibration 本身的 issue——将其纳入 D9 (LoRA sensitivity) 讨论即可。关键论文价值： calibration
462	    是独立于 accuracy 的 evidence dimension，审稿人难以 dismiss——即使觉得 99.83% 可能 saturated，ECE/Brier
463	    提供模型 ''knows what it knows'' 的定量证据。建议作为 Table 2 或 Figure 3 纳入正文（非 appendix），与
464	    accuracy table 并列。
465	
466	    '
467	- name: few_shot_frontier_baseline
468	  plan_id: plan_020
469	  description: GPT-4o/Claude 0-shot + 3-shot verdict prediction，作为 non-SFT upper bound
470	  expected_results:
471	    gpt4o_0shot_exception_only: 0.945
472	    gpt4o_0shot_exception_only_ci:
473	    - 0.93
474	    - 0.96
475	    gpt4o_3shot_exception_only: 0.965
476	    gpt4o_3shot_exception_only_ci:
477	    - 0.95
478	    - 0.98
479	    claude_0shot_exception_only: 0.935
480	    claude_0shot_exception_only_ci:
481	    - 0.92
482	    - 0.95
483	    claude_3shot_exception_only: 0.96
484	    claude_3shot_exception_only_ci:
485	    - 0.945
486	    - 0.975
487	    gpt4o_3shot_no_trace: 0.835
488	    claude_3shot_no_trace: 0.82
489	    sft_qwen7b_exception_only: 0.9983
490	    sft_advantage_vs_best_fewshot_pp: 3.3
491	    sft_qwen15b_exception_only: 0.9983
492	    sft_1_5b_vs_gpt4o_3shot_pp: 3.3
493	    gpt4o_api_cost_usd: 2.5
494	    sft_inference_cost_usd: 0.01
495	    cost_ratio: 250
496	  result_rationale: 'GPT-4o 和 Claude 是 frontier models，zero-shot code reasoning 能力极强。给定
497	    exception_only traces，task 简化为 ''if [ERROR] tags present → likely fail; if no
498	    errors → likely pass''。 Frontier models 0-shot 能处理大部分 cases (94-95%)，剩余 5-6% 错误来自：
499	    (1) GeneratorExit 等 non-fatal exceptions（frontier models 也会被 [ERROR] tag 误导， 与
500	    SFT 相同）；(2) 边界情况如 partial exceptions、多个 exception types 混合； (3) 对 no_exception
501	    format marker 的不一致解读（有时将空 trace 误判为 incomplete information 而非 no-fault signal）。
502	    3-shot 提升 ~2pp（GPT-4o: 94.5→96.5%, Claude: 93.5→96%），exemplars 帮助建立 consistent
503	    decision boundary，但无法达到 SFT 水平——SFT 通过 4720 训练样本学到了 dataset-specific patterns（哪些
504	    exception types always fatal, 哪些 benign），few-shot 的 3 个 exemplars 无法覆盖这些 long-tail
505	    patterns。 关键发现：SFT Qwen-1.5B (1.5B params, 99.83%) 以 3.3pp 优势超越 GPT-4o 3-shot
506	    (>175B params, 96.5%)——task-specific SFT 在 verdict prediction 上的参数效率是 generic
507	    reasoning 的 >100×。但 3.3pp gap 在审稿人眼中可能是 ''modest''——需要强调 error count 差异（2 vs ~42
508	    errors, ~21× difference）和 cost 差异（250×）。 GPT-4o 3-shot no_trace (83.5%) vs SFT
509	    no_trace (75.1%) 的对比说明 frontier model 的代码理解能力可以部分替代 trace 信息——但远不如 SFT + exception_only
510	    (99.83%)。
511	
512	    '
513	  tables:
514	  - title: SFT vs Frontier Few-shot Comparison
515	    headers:
516	    - Method
517	    - Model
518	    - Input
519	    - Accuracy
520	    - Errors/1190
521	    - Cost ($)
522	    - Latency
523	    rows:
524	    - - SFT
525	      - Qwen-7B
526	      - exception_only
527	      - 99.83%
528	      - 2
529	      - ~$0.01
530	      - ~2s batch
531	    - - SFT
532	      - Qwen-1.5B
533	      - exception_only
534	      - 99.83%
535	      - 2
536	      - ~$0.005
537	      - ~1s batch
538	    - - 3-shot
539	      - GPT-4o
540	      - exception_only
541	      - 96.5%
542	      - ~42
543	      - ~$2.50
544	      - ~15min serial
545	    - - 3-shot
546	      - Claude
547	      - exception_only
548	      - 96.0%
549	      - ~48
550	      - ~$3.00
551	      - ~18min serial
552	    - - 0-shot
553	      - GPT-4o
554	      - exception_only
555	      - 94.5%
556	      - ~65
557	      - ~$1.80
558	      - ~12min serial
559	    - - 0-shot
560	      - Claude
561	      - exception_only
562	      - 93.5%
563	      - ~77
564	      - ~$2.20
565	      - ~14min serial
566	    - - 3-shot
567	      - GPT-4o
568	      - no_trace
569	      - 83.5%
570	      - ~196
571	      - ~$1.20
572	      - ~10min serial
573	  - title: Base Model Zero-shot vs Frontier Few-shot (contextualization)
574	    headers:
575	    - Model
576	    - Params
577	    - 0-shot
578	    - 3-shot
579	    - SFT
580	    - SFT Δ vs 3-shot
581	    rows:
582	    - - Qwen-1.5B
583	      - 1.5B
584	      - 93.45%
585	      - —
586	      - 99.83%
587	      - +6.4pp
588	    - - Qwen-7B
589	      - 7B
590	      - 89.08%
591	      - 90.84%
592	      - 99.83%
593	      - +9.0pp
594	    - - DeepSeek-7B
595	      - 6.7B
596	      - 90.59%
597	      - —
598	      - 99.33%
599	      - +8.7pp
600	    - - GPT-4o
601	      - '>175B'
602	      - 94.5%
603	      - 96.5%
604	      - —
605	      - —
606	    - - Claude
607	      - '>175B'
608	      - 93.5%
609	      - 96.0%
610	      - —
611	      - —
612	  figures_description:
613	  - 'Bar chart: accuracy by method (SFT exception_only × 4 models, 0-shot × 5 models,
614	    3-shot × 2 frontier models)。SFT bars 在 99%+ 区域，few-shot bars 在 90-97% 区域，清晰展示
615	    SFT advantage。'
616	  - 'Cost-accuracy Pareto plot: x-axis = log(cost per 1190 samples), y-axis = accuracy。SFT
617	    在左上角 (low cost, high accuracy), frontier few-shot 在右下 (high cost, lower accuracy)。'
618	  analysis: 'Few-shot baseline 确认两个论文论点：(1) SFT exception_only 在 verdict task 上超越
619	    frontier model few-shot 3-5pp，证明 task-specific fine-tuning 的价值——尤其 1.5B SFT model
620	    超越 >175B GPT-4o 的 result 有很强 narrative appeal；(2) 即使 frontier model 也从 exception
621	    traces 获益 (no_trace 83.5% → exception_only 96.5%, +13pp)，independent confirm Claim
622	    2 的 information density 论点。但 median 档下 gap 仅 3.3pp，审稿人可能 argue ''the gap is not
623	    practically significant given the cost of SFT''。Rebuttal： (a) error count 差异是
624	    21×（2 vs 42），在 safety-critical 场景下差异巨大； (b) SFT inference cost 是 few-shot 的 1/250；(c)
625	    SFT model 可 offline deploy 无需 API access。建议作为 Section 5 的 comparison table 纳入正文，定位为
626	    ''SFT as practical deployment recommendation'' 而非 ''SFT is fundamentally superior''。
627	
628	    '
629	- name: ood_generalization_cross_language
630	  plan_id: plan_021
631	  description: 不同编程语言/项目的 trace 上测试 exception_only 泛化性
632	  expected_results:
633	    python_ood_exception_only_accuracy: 0.965
634	    python_ood_exception_only_ci:
635	    - 0.945
636	    - 0.98
637	    python_ood_degradation_vs_id_pp: 3.3
638	    java_exception_only_accuracy: 0.92
639	    java_exception_only_ci:
640	    - 0.895
641	    - 0.945
642	    java_degradation_vs_id_pp: 7.8
643	    javascript_exception_only_accuracy: 0.905
644	    javascript_exception_only_ci:
645	    - 0.875
646	    - 0.93
647	    javascript_degradation_vs_id_pp: 9.3
648	    cross_language_mean_accuracy: 0.93
649	    cross_language_mean_degradation_pp: 6.8
650	    python_ood_no_trace_accuracy: 0.72
651	    java_no_trace_accuracy: 0.68
652	    javascript_no_trace_accuracy: 0.67
653	    exception_only_lift_over_no_trace_ood_mean_pp: 24.3
654	  result_rationale: 'Exception_only 的 OOD generalization 依赖于 exception signal 的 cross-language
655	    structural similarity。核心假设：[ERROR] type: ... message: ... 格式是 tracer output 的
656	    design choice，不是 language-inherent property——但不同语言的 exception type naming 和 error
657	    message conventions 不同，导致 distribution shift。 Python OOD (96.5%)：同语言不同项目，exception
658	    types（TypeError, ValueError, IndexError） 与训练集分布相似，仅 project-specific custom exceptions
659	    造成少量降级。3.3pp degradation 主要来自 (1) 训练集未见过的 custom exception classes, (2) 不同项目的
660	    test structure 差异（多文件、fixtures）。 Java (92.0%)：exception structure 类似（try-catch,
661	    stack traces）但 exception type names 不同（NullPointerException, ArrayIndexOutOfBoundsException
662	    等 Java-specific names 训练集中未出现）。模型仍能利用 [ERROR] tag 的 binary signal，但对 exception
663	    type 的 fine-grained 理解降级。7.8pp degradation。 JavaScript (90.5%)：最大降级。JS 的 error
664	    handling 差异更大（Promise rejection, TypeError in async context），且 error message format
665	    与 Python 差异最大。但 [ERROR] tag 的 presence/absence signal 仍 partially transferable。9.3pp
666	    degradation。 所有语言上 exception_only 仍大幅优于 no_trace（mean lift 24.3pp），证明 exception
667	    signal 的 fault detection value 跨语言 robust，即使 absolute accuracy 降级。
668	
669	    '
670	  tables:
671	  - title: 'OOD Generalization: exception_only across Languages'
672	    headers:
673	    - Language
674	    - Setting
675	    - exception_only
676	    - no_trace
677	    - Lift
678	    - Degradation vs in-domain
679	    rows:
680	    - - Python
681	      - In-domain (HumanEval+MBPP)
682	      - 99.83%
683	      - 75.1%
684	      - +24.7pp
685	      - baseline
686	    - - Python
687	      - OOD (new projects)
688	      - 96.5%
689	      - 72.0%
690	      - +24.5pp
691	      - -3.3pp
692	    - - Java
693	      - OOD
694	      - 92.0%
695	      - 68.0%
696	      - +24.0pp
697	      - -7.8pp
698	    - - JavaScript
699	      - OOD
700	      - 90.5%
701	      - 67.0%
702	      - +23.5pp
703	      - -9.3pp
704	  figures_description:
705	  - 'Grouped bar chart: languages × conditions (exception_only vs no_trace)。每种语言两个
706	    bar，展示 exception_only 的 lift 在 OOD 上保持稳定 (~24pp)，即使 absolute accuracy 降级。'
707	  - 'Degradation waterfall: in-domain → Python OOD → Java → JavaScript，展示 progressive
708	    degradation 但 floor 仍 >90%。'
709	  analysis: 'OOD 结果是 median 档最大风险实验。Python OOD 降级温和 (3.3pp) 支持 generalization claim。Java/JavaScript
710	    降级更大 (8-9pp) 但 (1) 仍优于所有 baseline conditions， (2) lift over no_trace 保持稳定 (~24pp)——说明
711	    exception signal 的 fault detection value 跨语言 transferable，但 absolute accuracy
712	    受 token-level distribution shift 影响。论文 framing：''exception_only generalizes within-language
713	    with minimal degradation (3pp) and cross-language with moderate degradation (8-9pp);
714	    the diagnostic signal advantage is preserved (24pp lift) regardless of language''。审稿人可能
715	    argue ''Java/JS 降 8-9pp 说明 signal 不是 truly language-agnostic''——rebuttal：降级来自
716	    exception type vocabulary shift 而非 signal mechanism change；用 language-mixed training
717	    可恢复。此实验的最大价值：如果完成，将 single-task concern 从 1 task → 1 task 多语言，部分回应 scope criticism。风险：如果
718	    Java/JS 降到 <85%，narrative 受损。
719	
720	    '
721	- name: training_dynamics_learning_curves
722	  plan_id: plan_022
723	  description: exception_only vs full_trace 每 50 steps eval，分析收敛速度差异
724	  expected_results:
725	    exception_only_steps_to_90pct: 30
726	    exception_only_steps_to_95pct: 50
727	    exception_only_steps_to_99pct: 120
728	    exception_only_final_accuracy: 0.9983
729	    exception_only_curve_shape: monotonic_rapid_saturation
730	    vota_steps_to_90pct: 60
731	    vota_steps_to_95pct: 100
732	    vota_steps_to_99pct: 180
733	    vota_final_accuracy: 0.9941
734	    vota_curve_shape: monotonic_moderate_saturation
735	    full_trace_steps_to_80pct: 150
736	    full_trace_peak_accuracy: 0.83
737	    full_trace_peak_step: 200
738	    full_trace_final_accuracy: 0.8176
739	    full_trace_curve_shape: non_monotonic_with_dip
740	    no_trace_steps_to_73pct: 80
741	    no_trace_plateau_accuracy: 0.751
742	    no_trace_curve_shape: rapid_plateau_low_ceiling
743	    speed_ratio_exception_vs_vota_to_95pct: 2.0
744	    speed_ratio_exception_vs_full_trace_to_80pct: 5.0
745	    exception_only_samples_per_pp_gain: 8.5
746	    full_trace_samples_per_pp_gain: 72.0
747	    efficiency_ratio: 8.5
748	  result_rationale: 'Training dynamics 直接测量 information density 对 learning efficiency
749	    的影响。 Exception_only 收敛最快（~50 steps to 95%）因为：(1) input 极短（平均 <100 tokens）， gradient
750	    完全集中在 verdict-relevant signal 上；(2) 有效 unique 样本仅 2858，但 signal 的 binary structure（有
751	    exception → fail，无 exception → pass）极其 learnable，少量 样本即可学会；(3) 无 noise tokens
752	    干扰，每一步训练都是 effective update。 Full_trace 收敛最慢且 non-monotonic：(1) 长 input（mean ~2000
753	    tokens）导致 gradient dilution——大部分 gradient 流向 trace token 预测而非 verdict signal；(2)
754	    epoch1 peak (83.0%) 后 epoch2 下降 (76.3%) 说明模型 overfits to trace patterns 而非 verdict
755	    signal；(3) epoch3 partial recovery (81.76%) 可能是 overfitting 的 random fluctuation
756	    而非 systematic learning。 VOTA 介于两者之间：input 长度中等，包含 Tier 1 + Tier 2 信号，前者快速学习，后者需要
757	    更多 steps 但不会严重干扰。 No_trace 快速饱和在低水平（~75%），因为无 trace 信号可学习，模型只能学习 code→verdict
758	    的弱统计相关性。 Convergence efficiency ratio (~8.5×) 是 information density 假说的 direct
759	    quantification： exception_only 每 pp gain 需要 ~8.5 training samples，full_trace 需要
760	    ~72——验证 ''denser signal → faster learning'' 的因果链。
761	
762	    '
763	  tables:
764	  - title: Convergence Milestones (steps to reach accuracy threshold)
765	    headers:
766	    - Condition
767	    - To 80%
768	    - To 90%
769	    - To 95%
770	    - To 99%
771	    - Final
772	    - Shape
773	    rows:
774	    - - exception_only
775	      - ~20
776	      - ~30
777	      - ~50
778	      - ~120
779	      - 99.83%
780	      - Rapid saturation
781	    - - VOTA
782	      - ~30
783	      - ~60
784	      - ~100
785	      - ~180
786	      - 99.41%
787	      - Moderate saturation
788	    - - full_trace
789	      - ~150
790	      - never
791	      - never
792	      - never
793	      - 81.76%
794	      - Non-monotonic
795	    - - no_trace
796	      - never
797	      - never
798	      - never
799	      - never
800	      - 75.13%
801	      - Low-ceiling plateau
802	  - title: Learning Efficiency Comparison
803	    headers:
804	    - Condition
805	    - Effective unique samples
806	    - Final lift (pp)
807	    - Samples per pp
808	    - Efficiency
809	    rows:
810	    - - exception_only
811	      - 2858
812	      - 24.7
813	      - 8.5
814	      - 1.0× (reference)
815	    - - VOTA
816	      - ~5800
817	      - 24.3
818	      - 17.5
819	      - 0.49×
820	    - - full_trace
821	      - ~5800
822	      - 6.6
823	      - 71.8
824	      - 0.12×
825	    - - no_trace
826	      - ~5800
827	      - 3.6
828	      - 131.7
829	      - 0.06×
830	  figures_description:
831	  - 'Learning curve plot (main figure): x-axis = training steps, y-axis = eval accuracy
832	    (%)。4 条 curves 用不同颜色/线型。exception_only 陡升后 flat（红色实线），VOTA 次之（蓝色实线），full_trace
833	    non-monotonic（绿色虚线），no_trace 低 plateau（灰色点线）。水平虚线标注 majority baseline (71.5%)。每
834	    50 steps 一个评估点。'
835	  - 'Convergence speed bar chart: 4 conditions × steps to reach 90% (或 condition-specific
836	    ceiling 的 90%)，直观对比 learning speed。exception_only bar 最短。'
837	  analysis: Training dynamics 为 Claim 2 (information density) 提供 process-level evidence，补充
838	    已有的 outcome-level evidence (accuracy comparison)。Key narrative：exception_only
839	    不仅最终 accuracy 最高，learning efficiency 也最高——8.5× faster per-pp-gain than full_trace，直接量化了
840	    information density 的 learning advantage。full_trace 的 non-monotonic curve（epoch2
841	    dip）进一步说明 information overload 不仅限制 ceiling， 还 destabilize training——与 D1 (eval_loss
842	    vs accuracy decoupling) 呼应。 论文价值：作为 Figure 4 或 Supplementary Figure，与 budget curve
843	    (plan_016) 形成 互补——budget curve 展示 'how much trace to include'，training dynamics
844	    展示 'how efficiently different signals are learned'。不作独立 contribution，但作为 Claim
845	    2 的 converging evidence 有价值。审稿人可能问 'is this just because exception_only has shorter
846	    sequences?'——answer：shorter sequences + diagnostic signal concentration， 两者 confounded
847	    但都支持 information density narrative。
848	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cb0eef11-4964-4f98-9320-76b06ff93624",
  "isSidechain": false,
  "promptId": "b72b12af-1fe0-4898-8183-7d12f8920502",
  "type": "user",
  "uuid": "17c53004-6592-4852-91bd-905013f59f67",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/artifacts/dream_reports/dream_20260518T113804/median/review_context.yaml",
      "content": "narrative_guidance: 'Median 档结果总结：7 个 planned 实验全部符合 ''pattern exists but model-dependent''\n  预期。 plan_016 (tail-384) 确认 phase transition 存在但 sharpness 分化为两组——强模型 (Qwen-7B, CodeLlama-13B)\n  gradual，弱模型 (DeepSeek, Qwen-1.5B) sharp——''universal sharp phase transition'' 降级为\n  ''consistent trend with model-dependent transition characteristics''。plan_017 (cross-seed)\n  std 范围 0.4-3.5pp 证明 budget curve reproducible 但 variance 与模型强度相关。plan_019 确认 exception_only\n  near-perfect calibration 跨 4 模型通用（非离群 ECE ≤ 0.01）。plan_020 确认 SFT 优于 frontier model\n  few-shot 3-5pp，支持 SFT practical recommendation 但非压倒性优势。 plan_018 和 plan_022 提供 supporting\n  evidence 但不升级任何 claim。plan_021 是最大风险——跨语言 泛化可能大幅降级。总体：Claim 1 + Claim 3 核心证据不受影响，budget\n  curve 保留为 supporting evidence， EMNLP main 有竞争力 (P≈0.35-0.45) 但 scope concern + model-dependent\n  phase transition 需 strong rebuttal。\n\n  '\nimagined_experiments:\n- name: fine_grained_phase_transition_tail384\n  plan_id: plan_016\n  description: tail-384 × 4 模型，精确定位 256→512 phase transition 是 sharp 还是 gradual\n  expected_results:\n    qwen7b_tail384_accuracy: 0.855\n    qwen7b_tail384_ci:\n    - 0.832\n    - 0.877\n    qwen7b_delta_vs_tail256_pp: 6.6\n    qwen7b_delta_vs_tail512_pp: -8.1\n    qwen7b_transition_type: gradual\n    deepseek_tail384_accuracy: 0.805\n    deepseek_tail384_ci:\n    - 0.781\n    - 0.829\n    deepseek_delta_vs_tail256_pp: 4.1\n    deepseek_delta_vs_tail512_pp: -13.4\n    deepseek_transition_type: sharp\n    qwen15b_tail384_accuracy: 0.79\n    qwen15b_tail384_ci:\n    - 0.765\n    - 0.815\n    qwen15b_delta_vs_tail256_pp: 6.4\n    qwen15b_delta_vs_tail512_pp: -16.6\n    qwen15b_transition_type: sharp\n    codellama13b_tail384_accuracy: 0.875\n    codellama13b_tail384_ci:\n    - 0.854\n    - 0.896\n    codellama13b_delta_vs_tail256_pp: 9.6\n    codellama13b_delta_vs_tail512_pp: -10.0\n    codellama13b_transition_type: gradual\n    four_model_mean: 0.831\n    sharp_models_mean: 0.798\n    gradual_models_mean: 0.865\n    max_diff_vs_tail256_pp: 9.6\n  result_rationale: 'tail-384 处于 256→512 相变区间中段。信号来源：exception events 集中在 trace 末尾，tail-384\n    能捕获约 50-65% 的 exception 信息（vs tail-256 ~30%, tail-512 ~90%）。模型分化原因： (1) 强模型（Qwen-7B\n    CRUXEval-I 56.5%, CodeLlama-13B 13B参数）能从 partial exception 信息中推理出 verdict，因此 384\n    tokens 已显著提升——呈 gradual transition； (2) 弱模型（DeepSeek CRUXEval-I 39%, Qwen-1.5B\n    仅 1.5B 参数）需要 near-complete exception 信号才能有效利用，384 tokens 提升有限，大部分增益集中在 384→512\n    区间——呈 sharp transition。CodeLlama 虽然 tokenizer 不同（LLaMA BPE），但其 13B 参数量补偿了 tokenizer\n    差异，在 384 tokens 处已能有效提取 diagnostic signal。DeepSeek 受限于 base model 的 trace reasoning\n    能力（CRUXEval-I 39%），需要更完整的 exception 上下文。Qwen-1.5B 因模型容量极小， loss landscape 更陡峭，384\n    tokens 的 noisy partial signal 难以稳定学习。\n\n    '\n  tables:\n  - title: 'Budget Curve: tail Truncation × 4 Models (含 tail-384 新数据点)'\n    headers:\n    - Model\n    - tail-256 (%)\n    - tail-384 (%)\n    - tail-512 (%)\n    - tail-1024 (%)\n    - tail-2048 (%)\n    - Δ(256→384)\n    - Δ(384→512)\n    - Transition\n    rows:\n    - - Qwen-7B\n      - 78.9\n      - 85.5\n      - 93.6\n      - 96.5\n      - 97.3\n      - +6.6pp\n      - +8.1pp\n      - Gradual\n    - - DeepSeek-6.7B\n      - 76.4\n      - 80.5\n      - 93.9\n      - 96.5\n      - 95.0\n      - +4.1pp\n      - +13.4pp\n      - Sharp\n    - - Qwen-1.5B\n      - 72.6\n      - 79.0\n      - 95.6\n      - 96.6\n      - 97.9\n      - +6.4pp\n      - +16.6pp\n      - Sharp\n    - - CodeLlama-13B\n      - 77.9\n      - 87.5\n      - 97.5\n      - 98.2\n      - collapse\n      - +9.6pp\n      - +10.0pp\n      - Gradual\n  figures_description:\n  - 'Budget curve figure (4-panel or overlay): x-axis = tail token budget [256, 384,\n    512, 1024, 2048], y-axis = accuracy (%)。4 条模型曲线，384 处标注 transition type。Gradual\n    模型（Qwen-7B, CodeLlama）曲线在 256→512 段近似线性上升；Sharp 模型（DeepSeek, Qwen-1.5B）曲线在 256→384\n    段平缓、384→512 段陡升，呈 S 型。水平虚线标注 exception_only ceiling (99.83%)。'\n  - 'Transition sharpness scatter: x-axis = model capability proxy (CRUXEval-I 或 param\n    count), y-axis = Δ(384-256)/Δ(512-256) ratio (越高越 gradual)。4 点+回归线，展示 capability→gradualness\n    正相关。'\n  analysis: 'tail-384 结果确认 phase transition 存在但 sharpness 是 model-dependent property。\n    两组分化模式清晰：强模型 gradual（Δ256→384 ≈ Δ384→512），弱模型 sharp（Δ384→512 >> Δ256→384）。 这直接影响论文\n    claim：不能说 ''universal sharp phase transition at ~512 tokens''，需降级为 ''consistent\n    accuracy improvement trend with model-dependent transition characteristics: stronger\n    models show gradual onset while weaker models exhibit sharper thresholds''。 积极面：4-model\n    mean (83.1%) 显著高于 tail-256 mean (76.5%)，证明 384 tokens 确实包含 有用信号；且所有模型在 tail-512\n    均达 93%+，证明 transition 终点 universal。Phase transition figure 保留价值，但 discussion 必须新增\n    model-dependency caveat 和 transition sharpness 与 model capability 的相关性分析。\n\n    '\n- name: cross_seed_budget_curve_tail512\n  plan_id: plan_017\n  description: tail-512 × 4 models × 3 seeds，验证 phase transition 后 convergence band\n    robustness\n  expected_results:\n    qwen7b_seed42: 0.936\n    qwen7b_seed123: 0.924\n    qwen7b_seed456: 0.943\n    qwen7b_mean: 0.934\n    qwen7b_std_pp: 1.0\n    deepseek_seed42: 0.939\n    deepseek_seed123: 0.885\n    deepseek_seed456: 0.942\n    deepseek_mean: 0.922\n    deepseek_std_pp: 3.2\n    qwen15b_seed42: 0.956\n    qwen15b_seed123: 0.9\n    qwen15b_seed456: 0.938\n    qwen15b_mean: 0.931\n    qwen15b_std_pp: 2.9\n    codellama13b_seed42: 0.975\n    codellama13b_seed123: 0.968\n    codellama13b_seed456: 0.978\n    codellama13b_mean: 0.974\n    codellama13b_std_pp: 0.5\n    max_std_across_models_pp: 3.2\n    strong_model_avg_std_pp: 0.75\n    weak_model_avg_std_pp: 3.05\n  result_rationale: 'Cross-seed variance 反映 LoRA 初始化对 tail-512 budget 条件下的 trace learning\n    稳定性。 逻辑链：tail-512 包含足够的 exception 信息但也包含 non-diagnostic noise（loop 片段、变量 赋值）。强模型（Qwen-7B,\n    CodeLlama-13B）的 LoRA landscape 较平滑，不同初始化均收敛到 类似的 trace→verdict 映射，std < 1pp。弱模型（DeepSeek,\n    Qwen-1.5B）的 LoRA landscape 更 rugged：(1) DeepSeek 在 exception_only 上已显示 seed sensitivity\n    (seed123=91.09% vs seed42/456=99.33%)，tail-512 的更复杂 input 放大这一效应——某些 seed 未学到有效的\n    noise filtering，被 non-exception tokens 干扰；(2) Qwen-1.5B 参数量仅 1.5B，LoRA rank 相对于\n    total params 的比例更高，初始化影响更大。DeepSeek seed123 (88.5%) 呼应其 exception_only seed123\n    (91.09%) 的 pattern——同一 LoRA 初始化弱点在更复杂 input 下进一步暴露。 CodeLlama-13B std 最小 (0.5pp)\n    因其 13B 参数量提供最大 learning capacity，tail-512 的 signal 对其而言接近 trivial。\n\n    '\n  tables:\n  - title: Cross-seed tail-512 Robustness (3 seeds × 4 models)\n    headers:\n    - Model\n    - Seed42\n    - Seed123\n    - Seed456\n    - Mean\n    - Std\n    - Band Width\n    rows:\n    - - Qwen-7B\n      - 93.6%\n      - 92.4%\n      - 94.3%\n      - 93.4%\n      - 1.0pp\n      - 1.9pp\n    - - DeepSeek-6.7B\n      - 93.9%\n      - 88.5%\n      - 94.2%\n      - 92.2%\n      - 3.2pp\n      - 5.7pp\n    - - Qwen-1.5B\n      - 95.6%\n      - 90.0%\n      - 93.8%\n      - 93.1%\n      - 2.9pp\n      - 5.6pp\n    - - CodeLlama-13B\n      - 97.5%\n      - 96.8%\n      - 97.8%\n      - 97.4%\n      - 0.5pp\n      - 1.0pp\n  - title: Strong vs Weak Model Seed Stability 对比\n    headers:\n    - Group\n    - Models\n    - Avg Std\n    - Avg Band Width\n    - Interpretation\n    rows:\n    - - Strong\n      - Qwen-7B + CodeLlama-13B\n      - 0.75pp\n      - 1.5pp\n      - 'Near-deterministic: LoRA landscape smooth'\n    - - Weak\n      - DeepSeek + Qwen-1.5B\n      - 3.05pp\n      - 5.7pp\n      - 'Seed-sensitive: LoRA landscape rugged'\n  figures_description:\n  - 'Band plot: x-axis = tail token budget, y-axis = accuracy。每个模型一条中线 (mean) + shaded\n    band (min-max across 3 seeds)。强模型 band 窄，弱模型 band 宽。在 tail-512 处用 error bar 标注\n    3-seed CI。'\n  - 'Seed variance vs model capability scatter: x-axis = CRUXEval-I (或 param count\n    log scale), y-axis = tail-512 3-seed std (pp)。4 点 + power fit，展示 capability↑ →\n    variance↓ 趋势。'\n  analysis: 'Cross-seed 结果确认 budget curve pattern reproducible——所有模型 3-seed mean 均在\n    92-97% 区间，transition 后 convergence 一致。但 variance 的 model-dependency 加强了论文必须 使用的\n    hedged language：不能说 ''tail-512 reliably achieves >93%''，需改为 ''tail-512 mean accuracy\n    ≥ 92% across models, with tighter convergence on stronger models (std < 1pp) and\n    wider bands on weaker models (std 2-3pp)''。审稿人问 ''single-seed robustness'' 时可展示此数据回应。实际价值：证明\n    budget curve 的 rank ordering (tail-2048 > tail-1024 > tail-512 > tail-384 > tail-256)\n    在所有 seeds 上保持，trend 本身 robust； absolute performance 的 seed sensitivity 是 LoRA\n    training 问题而非 signal 问题——与 exception_only 的 seed pattern 一致 (D9)。\n\n    '\n- name: error_analysis_failure_modes\n  plan_id: plan_018\n  description: 分析 exception_only/vota/full_trace/no_trace 的 failure modes，重点 Tier\n    1 vs Tier 2 差异\n  expected_results:\n    qwen_exception_only_errors: 2\n    qwen_exception_only_error_ids:\n    - 901\n    - 905\n    qwen_exception_only_root_cause: 100% GeneratorExit (irreducible)\n    qwen_exception_only_error_direction: 100% pass→fail false alarm\n    qwen_vota_errors: 7\n    qwen_vota_overlap_with_exception: 2\n    qwen_vota_loop_artifact_errors: 3\n    qwen_vota_attention_dilution_errors: 2\n    qwen_vota_fail_to_pass_ratio: 0.57\n    qwen_full_trace_errors: 217\n    qwen_full_trace_long_trace_error_rate: 0.35\n    qwen_full_trace_short_trace_error_rate: 0.08\n    qwen_full_trace_fail_to_pass_fraction: 0.65\n    qwen_full_trace_length_correlation_r: 0.42\n    qwen_no_trace_errors: 296\n    qwen_no_trace_fail_to_pass_fraction: 0.63\n    qwen_no_trace_pass_to_fail_fraction: 0.37\n    deepseek_seed123_errors: 106\n    deepseek_seed123_fail_to_pass_fraction: 0.72\n    deepseek_seed123_overlap_with_qwen_irreducible: 2\n    exception_only_cross_model_jaccard: 0.85\n    full_trace_cross_model_jaccard: 0.15\n    no_trace_cross_model_jaccard: 0.25\n  result_rationale: 'Error analysis 揭示不同 trace 条件的 qualitatively different failure\n    modes： (1) Exception_only 的 2 个错误完全由 representation 决定（GeneratorExit 是 tracer\n    设计 缺陷，非模型不足），跨模型高度重叠（Jaccard ≈ 0.85）——说明 irreducible errors 是 data/ representation\n    property 而非 model property。 (2) VOTA 的额外 5 个错误来自 Tier 2 组件引入的 noise：loop compression\n    有时产生误导性 摘要（3 例），Tier 2 tokens 稀释对 Tier 1 exception signal 的 attention（2 例）。这直接\n    支持 Claim 3 的 ''combining tiers introduces noise'' 论点。 (3) Full_trace 错误与 trace\n    长度强相关（r≈0.42）：>1500 tokens 的 trace 错误率 ~35% vs <500 tokens ~8%，information overload\n    pattern 明确。错误以 fail→pass 为主（65%）， 说明模型在长 context 中找不到 fault signal，默认预测 majority\n    class。 (4) No_trace 错误反映纯 majority class bias，无 systematic pattern。 (5) DeepSeek\n    seed123 的 106 个错误集中在 fail→pass（72%），与 fail_recall=0.705 一致—— LoRA 初始化未学到 exception→fail\n    映射的关键部分，尤其对 uncommon exception types。\n\n    '\n  tables:\n  - title: Error Mode Distribution by Condition (Qwen-7B)\n    headers:\n    - Condition\n    - Total Errors\n    - fail→pass (%)\n    - pass→fail (%)\n    - Dominant Pattern\n    rows:\n    - - exception_only\n      - 2\n      - 0%\n      - 100%\n      - GeneratorExit irreducible\n    - - VOTA\n      - 7\n      - 57%\n      - 43%\n      - Tier 2 noise (loop artifacts + attention dilution)\n    - - full_trace\n      - 217\n      - 65%\n      - 35%\n      - Information overload (length-correlated)\n    - - no_trace\n      - 296\n      - 63%\n      - 37%\n      - Majority class bias\n  - title: Error Rate by Trace Length (full_trace, Qwen-7B)\n    headers:\n    - Length Bucket\n    - N Samples\n    - Errors\n    - Error Rate\n    - Interpretation\n    rows:\n    - - <500 tokens\n      - ~180\n      - ~14\n      - ~8%\n      - 'Short traces: fault signal accessible'\n    - - 500-1000 tokens\n      - ~350\n      - ~56\n      - ~16%\n      - 'Medium: partial signal loss'\n    - - 1000-1500 tokens\n      - ~380\n      - ~76\n      - ~20%\n      - 'Long: significant overload'\n    - - '>1500 tokens'\n      - ~280\n      - ~98\n      - ~35%\n      - 'Very long: severe information overload'\n  - title: Cross-Model Error Overlap (Jaccard Index, exception_only non-outlier seeds)\n    headers:\n    - Model Pair\n    - Jaccard\n    - Shared Errors\n    - Interpretation\n    rows:\n    - - Qwen-7B vs Qwen-1.5B\n      - 0.9\n      - 2/2 (both GeneratorExit)\n      - Same representation → same irreducible errors\n    - - Qwen-7B vs CodeLlama-13B\n      - 0.8\n      - 2/~2.5 avg\n      - Different tokenizer but same root cause\n    - - Qwen-7B vs DeepSeek (seed42)\n      - 0.22\n      - 2/~10\n      - DeepSeek has 8 errors vs Qwen 2\n  figures_description:\n  - 'Confusion matrix grid (2×4): 4 conditions × Qwen-7B，展示 error direction 差异。exception_only\n    和 VOTA 几乎完美（极少 off-diagonal），full_trace 和 no_trace 显示 fail→pass 偏移。'\n  - 'Error rate vs trace length scatter (full_trace only): x-axis = input token count,\n    y-axis = binary correct/incorrect，加 binned error rate 趋势线。展示 information overload\n    的 dose-response 关系。'\n  - 'Venn diagram: exception_only vs VOTA 错误重叠（Qwen-7B），展示 VOTA 额外错误全来自 Tier 2 noise。'\n  analysis: 'Error analysis 为论文提供 3 个具体贡献：(1) 定量确认 exception_only 的 irreducible error\n    来自 representation 而非模型（跨模型 Jaccard ≈ 0.85，跨 seed variance = 0）， 强化 ''99.83% =\n    ceiling'' 论点；(2) VOTA 的 5 个额外错误全部可归因于 Tier 2 components， 直接 quantify 了 ''combining\n    tiers introduces noise'' (Claim 3)；(3) full_trace 错误 与长度的正相关（r≈0.42）是 Claim 2\n    information overload 假说的 direct evidence。 不足：error analysis 不能作为独立 contribution（审稿人视之为\n    expected follow-up）， 但作为 Claim 1-3 的 supporting analysis 强化证据链。建议放在 Supplementary\n    或 Appendix，正文引用关键数字。\n\n    '\n- name: cross_model_calibration_exception_only\n  plan_id: plan_019\n  description: 4 models × exception_only ECE/Brier 对比，验证 calibration quality 跨模型通用\n  expected_results:\n    qwen7b_ece: 0.0027\n    qwen7b_brier: 0.0013\n    qwen7b_accuracy: 0.9983\n    qwen15b_ece: 0.003\n    qwen15b_brier: 0.0015\n    qwen15b_accuracy: 0.9983\n    codellama13b_ece: 0.002\n    codellama13b_brier: 0.001\n    codellama13b_accuracy: 0.9983\n    deepseek_seed42_ece: 0.008\n    deepseek_seed42_brier: 0.005\n    deepseek_seed42_accuracy: 0.9933\n    deepseek_seed123_ece: 0.085\n    deepseek_seed123_brier: 0.075\n    deepseek_seed123_accuracy: 0.9109\n    four_model_nonoutlier_ece_max: 0.008\n    four_model_nonoutlier_brier_max: 0.005\n    ece_ratio_vs_no_trace_min: 21.0\n    ece_ratio_vs_no_trace_max: 85.5\n  result_rationale: 'Calibration quality 直接跟随 accuracy：exception_only 在 3 个模型上达 99.83%（仅\n    2 个 相同错误），这些模型的 ECE/Brier 预期 near-identical——模型对 correct predictions 的 logit confidence\n    接近 1.0，仅 2 个 misclassified samples 贡献微量 miscalibration。Qwen-7B 和 Qwen-1.5B 使用同系列\n    tokenizer，exception signal 的 token 表示相同，因此 calibration 差异极小。CodeLlama-13B 因 13B\n    参数量可能产生更 sharp 的 logit distribution，ECE 略低。 DeepSeek seed42 (99.33%, 8 errors)\n    的 ECE 较高（~0.008）因为 4× 更多 errors 意味着 更多 bins 有非零 gap between confidence and accuracy。DeepSeek\n    seed123 (91.09%) 是 outlier——fail_recall 仅 0.705 意味着模型对大量 actual-fail 样本输出 high-confidence\n    pass 预测，造成严重 miscalibration (ECE ~0.085)。排除 seed123 outlier，4 模型 ECE 均 ≤ 0.008，与\n    no_trace ECE (0.171) 相比至少 21×-85× 改善——确认 exception signal 不仅提升 accuracy 还 fundamentally\n    improves model confidence calibration 跨模型通用。\n\n    '\n  tables:\n  - title: 'Cross-model Calibration: exception_only'\n    headers:\n    - Model\n    - Accuracy\n    - ECE\n    - Brier\n    - ECE ratio vs no_trace (0.171)\n    - Notes\n    rows:\n    - - Qwen-7B\n      - 99.83%\n      - 0.0027\n      - 0.0013\n      - 63×\n      - 3-seed confirmed; existing data\n    - - Qwen-1.5B\n      - 99.83%\n      - 0.003\n      - 0.0015\n      - 57×\n      - Same errors as 7B (id=901,905)\n    - - CodeLlama-13B\n      - 99.83%\n      - 0.002\n      - 0.001\n      - 86×\n      - Largest model → sharpest calibration\n    - - DeepSeek (seed42/456)\n      - 99.33%\n      - 0.008\n      - 0.005\n      - 21×\n      - 8 errors; still excellent\n    - - DeepSeek (seed123) ⚠️\n      - 91.09%\n      - 0.085\n      - 0.075\n      - 2×\n      - LoRA outlier; severely miscalibrated\n  figures_description:\n  - 'Reliability diagram (4-panel): 每个模型一个 calibration curve (predicted prob vs actual\n    frequency)。3 个非离群模型的曲线几乎与 perfect calibration 对角线重合；DeepSeek seed123 curve 偏离对角线（overconfident\n    on pass predictions for actual-fail samples）。'\n  - 'ECE bar chart: 4 models × exception_only + Qwen-7B no_trace/full_trace/VOTA 作对照。exception_only\n    的 bar 在所有模型上极短（≤0.008），no_trace bar (0.171) 显著突出。'\n  analysis: 'Cross-model calibration 确认 exception signal 的 calibration 优势是 universal\n    property 而非 Qwen-specific artifact。论文可 claim：''exception_only achieves near-perfect\n    calibration (ECE ≤ 0.008) across 4 architecturally distinct models, a 21-86× improvement\n    over no-trace baselines''。DeepSeek seed123 outlier 是 LoRA initialization problem\n    而非 calibration 本身的 issue——将其纳入 D9 (LoRA sensitivity) 讨论即可。关键论文价值： calibration\n    是独立于 accuracy 的 evidence dimension，审稿人难以 dismiss——即使觉得 99.83% 可能 saturated，ECE/Brier\n    提供模型 ''knows what it knows'' 的定量证据。建议作为 Table 2 或 Figure 3 纳入正文（非 appendix），与\n    accuracy table 并列。\n\n    '\n- name: few_shot_frontier_baseline\n  plan_id: plan_020\n  description: GPT-4o/Claude 0-shot + 3-shot verdict prediction，作为 non-SFT upper bound\n  expected_results:\n    gpt4o_0shot_exception_only: 0.945\n    gpt4o_0shot_exception_only_ci:\n    - 0.93\n    - 0.96\n    gpt4o_3shot_exception_only: 0.965\n    gpt4o_3shot_exception_only_ci:\n    - 0.95\n    - 0.98\n    claude_0shot_exception_only: 0.935\n    claude_0shot_exception_only_ci:\n    - 0.92\n    - 0.95\n    claude_3shot_exception_only: 0.96\n    claude_3shot_exception_only_ci:\n    - 0.945\n    - 0.975\n    gpt4o_3shot_no_trace: 0.835\n    claude_3shot_no_trace: 0.82\n    sft_qwen7b_exception_only: 0.9983\n    sft_advantage_vs_best_fewshot_pp: 3.3\n    sft_qwen15b_exception_only: 0.9983\n    sft_1_5b_vs_gpt4o_3shot_pp: 3.3\n    gpt4o_api_cost_usd: 2.5\n    sft_inference_cost_usd: 0.01\n    cost_ratio: 250\n  result_rationale: 'GPT-4o 和 Claude 是 frontier models，zero-shot code reasoning 能力极强。给定\n    exception_only traces，task 简化为 ''if [ERROR] tags present → likely fail; if no\n    errors → likely pass''。 Frontier models 0-shot 能处理大部分 cases (94-95%)，剩余 5-6% 错误来自：\n    (1) GeneratorExit 等 non-fatal exceptions（frontier models 也会被 [ERROR] tag 误导， 与\n    SFT 相同）；(2) 边界情况如 partial exceptions、多个 exception types 混合； (3) 对 no_exception\n    format marker 的不一致解读（有时将空 trace 误判为 incomplete information 而非 no-fault signal）。\n    3-shot 提升 ~2pp（GPT-4o: 94.5→96.5%, Claude: 93.5→96%），exemplars 帮助建立 consistent\n    decision boundary，但无法达到 SFT 水平——SFT 通过 4720 训练样本学到了 dataset-specific patterns（哪些\n    exception types always fatal, 哪些 benign），few-shot 的 3 个 exemplars 无法覆盖这些 long-tail\n    patterns。 关键发现：SFT Qwen-1.5B (1.5B params, 99.83%) 以 3.3pp 优势超越 GPT-4o 3-shot\n    (>175B params, 96.5%)——task-specific SFT 在 verdict prediction 上的参数效率是 generic\n    reasoning 的 >100×。但 3.3pp gap 在审稿人眼中可能是 ''modest''——需要强调 error count 差异（2 vs ~42\n    errors, ~21× difference）和 cost 差异（250×）。 GPT-4o 3-shot no_trace (83.5%) vs SFT\n    no_trace (75.1%) 的对比说明 frontier model 的代码理解能力可以部分替代 trace 信息——但远不如 SFT + exception_only\n    (99.83%)。\n\n    '\n  tables:\n  - title: SFT vs Frontier Few-shot Comparison\n    headers:\n    - Method\n    - Model\n    - Input\n    - Accuracy\n    - Errors/1190\n    - Cost ($)\n    - Latency\n    rows:\n    - - SFT\n      - Qwen-7B\n      - exception_only\n      - 99.83%\n      - 2\n      - ~$0.01\n      - ~2s batch\n    - - SFT\n      - Qwen-1.5B\n      - exception_only\n      - 99.83%\n      - 2\n      - ~$0.005\n      - ~1s batch\n    - - 3-shot\n      - GPT-4o\n      - exception_only\n      - 96.5%\n      - ~42\n      - ~$2.50\n      - ~15min serial\n    - - 3-shot\n      - Claude\n      - exception_only\n      - 96.0%\n      - ~48\n      - ~$3.00\n      - ~18min serial\n    - - 0-shot\n      - GPT-4o\n      - exception_only\n      - 94.5%\n      - ~65\n      - ~$1.80\n      - ~12min serial\n    - - 0-shot\n      - Claude\n      - exception_only\n      - 93.5%\n      - ~77\n      - ~$2.20\n      - ~14min serial\n    - - 3-shot\n      - GPT-4o\n      - no_trace\n      - 83.5%\n      - ~196\n      - ~$1.20\n      - ~10min serial\n  - title: Base Model Zero-shot vs Frontier Few-shot (contextualization)\n    headers:\n    - Model\n    - Params\n    - 0-shot\n    - 3-shot\n    - SFT\n    - SFT Δ vs 3-shot\n    rows:\n    - - Qwen-1.5B\n      - 1.5B\n      - 93.45%\n      - —\n      - 99.83%\n      - +6.4pp\n    - - Qwen-7B\n      - 7B\n      - 89.08%\n      - 90.84%\n      - 99.83%\n      - +9.0pp\n    - - DeepSeek-7B\n      - 6.7B\n      - 90.59%\n      - —\n      - 99.33%\n      - +8.7pp\n    - - GPT-4o\n      - '>175B'\n      - 94.5%\n      - 96.5%\n      - —\n      - —\n    - - Claude\n      - '>175B'\n      - 93.5%\n      - 96.0%\n      - —\n      - —\n  figures_description:\n  - 'Bar chart: accuracy by method (SFT exception_only × 4 models, 0-shot × 5 models,\n    3-shot × 2 frontier models)。SFT bars 在 99%+ 区域，few-shot bars 在 90-97% 区域，清晰展示\n    SFT advantage。'\n  - 'Cost-accuracy Pareto plot: x-axis = log(cost per 1190 samples), y-axis = accuracy。SFT\n    在左上角 (low cost, high accuracy), frontier few-shot 在右下 (high cost, lower accuracy)。'\n  analysis: 'Few-shot baseline 确认两个论文论点：(1) SFT exception_only 在 verdict task 上超越\n    frontier model few-shot 3-5pp，证明 task-specific fine-tuning 的价值——尤其 1.5B SFT model\n    超越 >175B GPT-4o 的 result 有很强 narrative appeal；(2) 即使 frontier model 也从 exception\n    traces 获益 (no_trace 83.5% → exception_only 96.5%, +13pp)，independent confirm Claim\n    2 的 information density 论点。但 median 档下 gap 仅 3.3pp，审稿人可能 argue ''the gap is not\n    practically significant given the cost of SFT''。Rebuttal： (a) error count 差异是\n    21×（2 vs 42），在 safety-critical 场景下差异巨大； (b) SFT inference cost 是 few-shot 的 1/250；(c)\n    SFT model 可 offline deploy 无需 API access。建议作为 Section 5 的 comparison table 纳入正文，定位为\n    ''SFT as practical deployment recommendation'' 而非 ''SFT is fundamentally superior''。\n\n    '\n- name: ood_generalization_cross_language\n  plan_id: plan_021\n  description: 不同编程语言/项目的 trace 上测试 exception_only 泛化性\n  expected_results:\n    python_ood_exception_only_accuracy: 0.965\n    python_ood_exception_only_ci:\n    - 0.945\n    - 0.98\n    python_ood_degradation_vs_id_pp: 3.3\n    java_exception_only_accuracy: 0.92\n    java_exception_only_ci:\n    - 0.895\n    - 0.945\n    java_degradation_vs_id_pp: 7.8\n    javascript_exception_only_accuracy: 0.905\n    javascript_exception_only_ci:\n    - 0.875\n    - 0.93\n    javascript_degradation_vs_id_pp: 9.3\n    cross_language_mean_accuracy: 0.93\n    cross_language_mean_degradation_pp: 6.8\n    python_ood_no_trace_accuracy: 0.72\n    java_no_trace_accuracy: 0.68\n    javascript_no_trace_accuracy: 0.67\n    exception_only_lift_over_no_trace_ood_mean_pp: 24.3\n  result_rationale: 'Exception_only 的 OOD generalization 依赖于 exception signal 的 cross-language\n    structural similarity。核心假设：[ERROR] type: ... message: ... 格式是 tracer output 的\n    design choice，不是 language-inherent property——但不同语言的 exception type naming 和 error\n    message conventions 不同，导致 distribution shift。 Python OOD (96.5%)：同语言不同项目，exception\n    types（TypeError, ValueError, IndexError） 与训练集分布相似，仅 project-specific custom exceptions\n    造成少量降级。3.3pp degradation 主要来自 (1) 训练集未见过的 custom exception classes, (2) 不同项目的\n    test structure 差异（多文件、fixtures）。 Java (92.0%)：exception structure 类似（try-catch,\n    stack traces）但 exception type names 不同（NullPointerException, ArrayIndexOutOfBoundsException\n    等 Java-specific names 训练集中未出现）。模型仍能利用 [ERROR] tag 的 binary signal，但对 exception\n    type 的 fine-grained 理解降级。7.8pp degradation。 JavaScript (90.5%)：最大降级。JS 的 error\n    handling 差异更大（Promise rejection, TypeError in async context），且 error message format\n    与 Python 差异最大。但 [ERROR] tag 的 presence/absence signal 仍 partially transferable。9.3pp\n    degradation。 所有语言上 exception_only 仍大幅优于 no_trace（mean lift 24.3pp），证明 exception\n    signal 的 fault detection value 跨语言 robust，即使 absolute accuracy 降级。\n\n    '\n  tables:\n  - title: 'OOD Generalization: exception_only across Languages'\n    headers:\n    - Language\n    - Setting\n    - exception_only\n    - no_trace\n    - Lift\n    - Degradation vs in-domain\n    rows:\n    - - Python\n      - In-domain (HumanEval+MBPP)\n      - 99.83%\n      - 75.1%\n      - +24.7pp\n      - baseline\n    - - Python\n      - OOD (new projects)\n      - 96.5%\n      - 72.0%\n      - +24.5pp\n      - -3.3pp\n    - - Java\n      - OOD\n      - 92.0%\n      - 68.0%\n      - +24.0pp\n      - -7.8pp\n    - - JavaScript\n      - OOD\n      - 90.5%\n      - 67.0%\n      - +23.5pp\n      - -9.3pp\n  figures_description:\n  - 'Grouped bar chart: languages × conditions (exception_only vs no_trace)。每种语言两个\n    bar，展示 exception_only 的 lift 在 OOD 上保持稳定 (~24pp)，即使 absolute accuracy 降级。'\n  - 'Degradation waterfall: in-domain → Python OOD → Java → JavaScript，展示 progressive\n    degradation 但 floor 仍 >90%。'\n  analysis: 'OOD 结果是 median 档最大风险实验。Python OOD 降级温和 (3.3pp) 支持 generalization claim。Java/JavaScript\n    降级更大 (8-9pp) 但 (1) 仍优于所有 baseline conditions， (2) lift over no_trace 保持稳定 (~24pp)——说明\n    exception signal 的 fault detection value 跨语言 transferable，但 absolute accuracy\n    受 token-level distribution shift 影响。论文 framing：''exception_only generalizes within-language\n    with minimal degradation (3pp) and cross-language with moderate degradation (8-9pp);\n    the diagnostic signal advantage is preserved (24pp lift) regardless of language''。审稿人可能\n    argue ''Java/JS 降 8-9pp 说明 signal 不是 truly language-agnostic''——rebuttal：降级来自\n    exception type vocabulary shift 而非 signal mechanism change；用 language-mixed training\n    可恢复。此实验的最大价值：如果完成，将 single-task concern 从 1 task → 1 task 多语言，部分回应 scope criticism。风险：如果\n    Java/JS 降到 <85%，narrative 受损。\n\n    '\n- name: training_dynamics_learning_curves\n  plan_id: plan_022\n  description: exception_only vs full_trace 每 50 steps eval，分析收敛速度差异\n  expected_results:\n    exception_only_steps_to_90pct: 30\n    exception_only_steps_to_95pct: 50\n    exception_only_steps_to_99pct: 120\n    exception_only_final_accuracy: 0.9983\n    exception_only_curve_shape: monotonic_rapid_saturation\n    vota_steps_to_90pct: 60\n    vota_steps_to_95pct: 100\n    vota_steps_to_99pct: 180\n    vota_final_accuracy: 0.9941\n    vota_curve_shape: monotonic_moderate_saturation\n    full_trace_steps_to_80pct: 150\n    full_trace_peak_accuracy: 0.83\n    full_trace_peak_step: 200\n    full_trace_final_accuracy: 0.8176\n    full_trace_curve_shape: non_monotonic_with_dip\n    no_trace_steps_to_73pct: 80\n    no_trace_plateau_accuracy: 0.751\n    no_trace_curve_shape: rapid_plateau_low_ceiling\n    speed_ratio_exception_vs_vota_to_95pct: 2.0\n    speed_ratio_exception_vs_full_trace_to_80pct: 5.0\n    exception_only_samples_per_pp_gain: 8.5\n    full_trace_samples_per_pp_gain: 72.0\n    efficiency_ratio: 8.5\n  result_rationale: 'Training dynamics 直接测量 information density 对 learning efficiency\n    的影响。 Exception_only 收敛最快（~50 steps to 95%）因为：(1) input 极短（平均 <100 tokens）， gradient\n    完全集中在 verdict-relevant signal 上；(2) 有效 unique 样本仅 2858，但 signal 的 binary structure（有\n    exception → fail，无 exception → pass）极其 learnable，少量 样本即可学会；(3) 无 noise tokens\n    干扰，每一步训练都是 effective update。 Full_trace 收敛最慢且 non-monotonic：(1) 长 input（mean ~2000\n    tokens）导致 gradient dilution——大部分 gradient 流向 trace token 预测而非 verdict signal；(2)\n    epoch1 peak (83.0%) 后 epoch2 下降 (76.3%) 说明模型 overfits to trace patterns 而非 verdict\n    signal；(3) epoch3 partial recovery (81.76%) 可能是 overfitting 的 random fluctuation\n    而非 systematic learning。 VOTA 介于两者之间：input 长度中等，包含 Tier 1 + Tier 2 信号，前者快速学习，后者需要\n    更多 steps 但不会严重干扰。 No_trace 快速饱和在低水平（~75%），因为无 trace 信号可学习，模型只能学习 code→verdict\n    的弱统计相关性。 Convergence efficiency ratio (~8.5×) 是 information density 假说的 direct\n    quantification： exception_only 每 pp gain 需要 ~8.5 training samples，full_trace 需要\n    ~72——验证 ''denser signal → faster learning'' 的因果链。\n\n    '\n  tables:\n  - title: Convergence Milestones (steps to reach accuracy threshold)\n    headers:\n    - Condition\n    - To 80%\n    - To 90%\n    - To 95%\n    - To 99%\n    - Final\n    - Shape\n    rows:\n    - - exception_only\n      - ~20\n      - ~30\n      - ~50\n      - ~120\n      - 99.83%\n      - Rapid saturation\n    - - VOTA\n      - ~30\n      - ~60\n      - ~100\n      - ~180\n      - 99.41%\n      - Moderate saturation\n    - - full_trace\n      - ~150\n      - never\n      - never\n      - never\n      - 81.76%\n      - Non-monotonic\n    - - no_trace\n      - never\n      - never\n      - never\n      - never\n      - 75.13%\n      - Low-ceiling plateau\n  - title: Learning Efficiency Comparison\n    headers:\n    - Condition\n    - Effective unique samples\n    - Final lift (pp)\n    - Samples per pp\n    - Efficiency\n    rows:\n    - - exception_only\n      - 2858\n      - 24.7\n      - 8.5\n      - 1.0× (reference)\n    - - VOTA\n      - ~5800\n      - 24.3\n      - 17.5\n      - 0.49×\n    - - full_trace\n      - ~5800\n      - 6.6\n      - 71.8\n      - 0.12×\n    - - no_trace\n      - ~5800\n      - 3.6\n      - 131.7\n      - 0.06×\n  figures_description:\n  - 'Learning curve plot (main figure): x-axis = training steps, y-axis = eval accuracy\n    (%)。4 条 curves 用不同颜色/线型。exception_only 陡升后 flat（红色实线），VOTA 次之（蓝色实线），full_trace\n    non-monotonic（绿色虚线），no_trace 低 plateau（灰色点线）。水平虚线标注 majority baseline (71.5%)。每\n    50 steps 一个评估点。'\n  - 'Convergence speed bar chart: 4 conditions × steps to reach 90% (或 condition-specific\n    ceiling 的 90%)，直观对比 learning speed。exception_only bar 最短。'\n  analysis: Training dynamics 为 Claim 2 (information density) 提供 process-level evidence，补充\n    已有的 outcome-level evidence (accuracy comparison)。Key narrative：exception_only\n    不仅最终 accuracy 最高，learning efficiency 也最高——8.5× faster per-pp-gain than full_trace，直接量化了\n    information density 的 learning advantage。full_trace 的 non-monotonic curve（epoch2\n    dip）进一步说明 information overload 不仅限制 ceiling， 还 destabilize training——与 D1 (eval_loss\n    vs accuracy decoupling) 呼应。 论文价值：作为 Figure 4 或 Supplementary Figure，与 budget curve\n    (plan_016) 形成 互补——budget curve 展示 'how much trace to include'，training dynamics\n    展示 'how efficiently different signals are learned'。不作独立 contribution，但作为 Claim\n    2 的 converging evidence 有价值。审稿人可能问 'is this just because exception_only has shorter\n    sequences?'——answer：shorter sequences + diagnostic signal concentration， 两者 confounded\n    但都支持 information density narrative。\n",
      "numLines": 848,
      "startLine": 1,
      "totalLines": 848
    }
  },
  "sourceToolAssistantUUID": "cb0eef11-4964-4f98-9320-76b06ff93624",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/.claude/sessions/review_reviewer_1_7624f219",
  "sessionId": "f76386b4-9d1f-4f92-b831-706bc4acd94d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Runtime record

_source line 72 · 2026-05-18T12:30:04.582Z_

```json
{
  "parentUuid": "17c53004-6592-4852-91bd-905013f59f67",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "6ab8a121-a630-40b9-b632-73d8a08332c1",
  "timestamp": "2026-05-18T12:30:04.582Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/.claude/sessions/review_reviewer_1_7624f219",
  "sessionId": "f76386b4-9d1f-4f92-b831-706bc4acd94d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---


### Runtime record

_source line 73_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[Round 1 审稿请求]: [Dream 审稿任务 — Reviewer 1：方法 + 实验]  论文标题：Exception Events Are All You Need: Fault Detection Signals for Verdict Prediction in Execution Traces  PDF 路径：/home/ubuntu/.agent-ml-research-id…",
  "leafUuid": "6ab8a121-a630-40b9-b632-73d8a08332c1",
  "sessionId": "f76386b4-9d1f-4f92-b831-706bc4acd94d"
}
```

---


### Runtime record

_source line 74_

```json
{
  "type": "ai-title",
  "aiTitle": "Round 1 peer review for trace verdict prediction paper",
  "sessionId": "f76386b4-9d1f-4f92-b831-706bc4acd94d"
}
```

---


### Assistant

_source line 75 · 2026-05-18T12:30:11.220Z_

<details><summary>Logged reasoning block</summary>

```text
Let me read the PDF now with the correct page range.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6ab8a121-a630-40b9-b632-73d8a08332c1",
  "isSidechain": false,
  "requestId": "req_011CbA355sZgxsU3A17E9DK5",
  "type": "assistant",
  "uuid": "b178b73d-e4c3-4318-b7ea-f40a7fc44607",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/.claude/sessions/review_reviewer_1_7624f219",
  "sessionId": "f76386b4-9d1f-4f92-b831-706bc4acd94d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01F6b7etxCzJ6xGBgz4rzbNm",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 15560,
      "cache_read_input_tokens": 87906,
      "output_tokens": 201,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 15560,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 201,
          "cache_read_input_tokens": 87906,
          "cache_creation_input_tokens": 15560,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 15560
          },
          "type": "message"
        }
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

_source line 76 · 2026-05-18T12:30:11.656Z_

PDF 共 9 页，重新渲染。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b178b73d-e4c3-4318-b7ea-f40a7fc44607",
  "isSidechain": false,
  "requestId": "req_011CbA355sZgxsU3A17E9DK5",
  "type": "assistant",
  "uuid": "5f3ae575-27e5-4229-a486-f7a8f329a025",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/.claude/sessions/review_reviewer_1_7624f219",
  "sessionId": "f76386b4-9d1f-4f92-b831-706bc4acd94d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01F6b7etxCzJ6xGBgz4rzbNm",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 15560,
      "cache_read_input_tokens": 87906,
      "output_tokens": 201,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 15560,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 201,
          "cache_read_input_tokens": 87906,
          "cache_creation_input_tokens": 15560,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 15560
          },
          "type": "message"
        }
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

_source line 77 · 2026-05-18T12:30:14.710Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images · `toolu_01MgDgbS2zdFyP9UAih2hxxA`</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/artifacts/dream_reports/dream_20260518T113804/median/review_input_e90a5c14.pdf",
  "pages": "1-9",
  "dpi": 200
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5f3ae575-27e5-4229-a486-f7a8f329a025",
  "isSidechain": false,
  "requestId": "req_011CbA355sZgxsU3A17E9DK5",
  "type": "assistant",
  "uuid": "bd5ac32a-2770-4d02-8436-db4efd365787",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/.claude/sessions/review_reviewer_1_7624f219",
  "sessionId": "f76386b4-9d1f-4f92-b831-706bc4acd94d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01F6b7etxCzJ6xGBgz4rzbNm",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 15560,
      "cache_read_input_tokens": 87906,
      "output_tokens": 201,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 15560,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 201,
          "cache_read_input_tokens": 87906,
          "cache_creation_input_tokens": 15560,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 15560
          },
          "type": "message"
        }
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

_source line 78 · 2026-05-18T12:30:17.744Z_

<details><summary>↩ Tool result · `toolu_01MgDgbS2zdFyP9UAih2hxxA`</summary>

```text
Error: result (4,659,683 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-4-projects-trace-verdict-study--claude-sessions-review-reviewer-1-7624f219/f76386b4-9d1f-4f92-b831-706bc4acd94d/tool-results/mcp-agent-ml-research-pdf_to_images-1779107417732.txt.
Format: JSON with schema: {result: string}
Use offset and limit parameters to read specific portions of the file, search within it for specific content, and jq to make structured queries.
REQUIREMENTS FOR SUMMARIZATION/ANALYSIS/REVIEW:
- You MUST read the content from the file at /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-4-projects-trace-verdict-study--claude-sessions-review-reviewer-1-7624f219/f76386b4-9d1f-4f92-b831-706bc4acd94d/tool-results/mcp-agent-ml-research-pdf_to_images-1779107417732.txt in sequential chunks until 100% of the content has been read.
- If you receive truncation warnings when reading the file, reduce the chunk size until you have read 100% of the content without truncation.
- Before producing ANY summary or analysis, you MUST explicitly describe what portion of the content you have read. ***If you did not read the entire content, you MUST explicitly state this.***

```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bd5ac32a-2770-4d02-8436-db4efd365787",
  "isSidechain": false,
  "promptId": "b72b12af-1fe0-4898-8183-7d12f8920502",
  "type": "user",
  "uuid": "8c4906ac-37e3-4fa5-91d2-3369a67dce83",
  "toolUseResult": "Error: result (4,659,683 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-4-projects-trace-verdict-study--claude-sessions-review-reviewer-1-7624f219/f76386b4-9d1f-4f92-b831-706bc4acd94d/tool-results/mcp-agent-ml-research-pdf_to_images-1779107417732.txt.\nFormat: JSON with schema: {result: string}\nUse offset and limit parameters to read specific portions of the file, search within it for specific content, and jq to make structured queries.\nREQUIREMENTS FOR SUMMARIZATION/ANALYSIS/REVIEW:\n- You MUST read the content from the file at /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-4-projects-trace-verdict-study--claude-sessions-review-reviewer-1-7624f219/f76386b4-9d1f-4f92-b831-706bc4acd94d/tool-results/mcp-agent-ml-research-pdf_to_images-1779107417732.txt in sequential chunks until 100% of the content has been read.\n- If you receive truncation warnings when reading the file, reduce the chunk size until you have read 100% of the content without truncation.\n- Before producing ANY summary or analysis, you MUST explicitly describe what portion of the content you have read. ***If you did not read the entire content, you MUST explicitly state this.***\n",
  "mcpMeta": {
    "storage": "sanitized-trace-archive",
    "source_line": 78,
    "serialized_bytes": 4659720,
    "serialized_sha256": "d276f52f3a33f992e1269dabc991875a21f2f002daeef8c311f67e3e6b92a844",
    "note": "Complete sanitized source is retained in trace-files.tar.gz."
  },
  "sourceToolAssistantUUID": "bd5ac32a-2770-4d02-8436-db4efd365787",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/.claude/sessions/review_reviewer_1_7624f219",
  "sessionId": "f76386b4-9d1f-4f92-b831-706bc4acd94d",
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
  "lastPrompt": "[Round 1 审稿请求]: [Dream 审稿任务 — Reviewer 1：方法 + 实验]  论文标题：Exception Events Are All You Need: Fault Detection Signals for Verdict Prediction in Execution Traces  PDF 路径：/home/ubuntu/.agent-ml-research-id…",
  "leafUuid": "8c4906ac-37e3-4fa5-91d2-3369a67dce83",
  "sessionId": "f76386b4-9d1f-4f92-b831-706bc4acd94d"
}
```

---


### Runtime record

_source line 80_

```json
{
  "type": "ai-title",
  "aiTitle": "Round 1 peer review for trace verdict prediction paper",
  "sessionId": "f76386b4-9d1f-4f92-b831-706bc4acd94d"
}
```

---


### Assistant

_source line 81 · 2026-05-18T12:30:20.687Z_

<details><summary>Logged reasoning block</summary>

```text
The PDF images are too large. Let me try rendering fewer pages at a time to view them.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8c4906ac-37e3-4fa5-91d2-3369a67dce83",
  "isSidechain": false,
  "requestId": "req_011CbA364FcEZqhGBdjSdCCF",
  "type": "assistant",
  "uuid": "eee19b4d-517c-40e0-b35c-4384f64d5f25",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/.claude/sessions/review_reviewer_1_7624f219",
  "sessionId": "f76386b4-9d1f-4f92-b831-706bc4acd94d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01H3HQhRcfciUHCYK3zpCenK",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 605,
      "cache_read_input_tokens": 103466,
      "output_tokens": 490,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 605,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 490,
          "cache_read_input_tokens": 103466,
          "cache_creation_input_tokens": 605,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 605
          },
          "type": "message"
        }
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

_source line 82 · 2026-05-18T12:30:21.184Z_

PDF 太大，分批渲染。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "eee19b4d-517c-40e0-b35c-4384f64d5f25",
  "isSidechain": false,
  "requestId": "req_011CbA364FcEZqhGBdjSdCCF",
  "type": "assistant",
  "uuid": "42d815fc-c940-47c0-bb9b-e9e718e5de86",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/.claude/sessions/review_reviewer_1_7624f219",
  "sessionId": "f76386b4-9d1f-4f92-b831-706bc4acd94d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01H3HQhRcfciUHCYK3zpCenK",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 605,
      "cache_read_input_tokens": 103466,
      "output_tokens": 490,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 605,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 490,
          "cache_read_input_tokens": 103466,
          "cache_creation_input_tokens": 605,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 605
          },
          "type": "message"
        }
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

_source line 83 · 2026-05-18T12:30:22.615Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images · `toolu_01TpVepFEGmkzrax6xtRjpyj`</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/artifacts/dream_reports/dream_20260518T113804/median/review_input_e90a5c14.pdf",
  "pages": "1-3",
  "dpi": 150
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "42d815fc-c940-47c0-bb9b-e9e718e5de86",
  "isSidechain": false,
  "requestId": "req_011CbA364FcEZqhGBdjSdCCF",
  "type": "assistant",
  "uuid": "ba5a522e-088a-4455-8c59-721551dc3ea8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/.claude/sessions/review_reviewer_1_7624f219",
  "sessionId": "f76386b4-9d1f-4f92-b831-706bc4acd94d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01H3HQhRcfciUHCYK3zpCenK",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 605,
      "cache_read_input_tokens": 103466,
      "output_tokens": 490,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 605,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 490,
          "cache_read_input_tokens": 103466,
          "cache_creation_input_tokens": 605,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 605
          },
          "type": "message"
        }
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

_source line 84 · 2026-05-18T12:30:23.306Z_

&lt;details>&lt;summary>↩ Tool result · `toolu_01TpVepFEGmkzrax6xtRjpyj`&lt;/summary>

```text
Error: result (1,299,987 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-4-projects-trace-verdict-study--claude-sessions-review-reviewer-1-7624f219/f76386b4-9d1f-4f92-b831-706bc4acd94d/tool-results/mcp-agent-ml-research-pdf_to_images-1779107423303.txt.
Format: JSON with schema: {result: string}
Use offset and limit parameters to read specific portions of the file, search within it for specific content, and jq to make structured queries.
REQUIREMENTS FOR SUMMARIZATION/ANALYSIS/REVIEW:
- You MUST read the content from the file at /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-4-projects-trace-verdict-study--claude-sessions-review-reviewer-1-7624f219/f76386b4-9d1f-4f92-b831-706bc4acd94d/tool-results/mcp-agent-ml-research-pdf_to_images-1779107423303.txt in sequential chunks until 100% of the content has been read.
- If you receive truncation warnings when reading the file, reduce the chunk size until you have read 100% of the content without truncation.
- Before producing ANY summary or analysis, you MUST explicitly describe what portion of the content you have read. ***If you did not read the entire content, you MUST explicitly state this.***

```

&lt;/details>

&lt;details>&lt;summary>Recorded metadata&lt;/summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ba5a522e-088a-4455-8c59-721551dc3ea8",
  "isSidechain": false,
  "promptId": "b72b12af-1fe0-4898-8183-7d12f8920502",
  "type": "user",
  "uuid": "3ce72edb-8eca-4f89-a9cb-6fcd02a7eddc",
  "toolUseResult": "Error: result (1,299,987 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-4-projects-trace-verdict-study--claude-sessions-review-reviewer-1-7624f219/f76386b4-9d1f-4f92-b831-706bc4acd94d/tool-results/mcp-agent-ml-research-pdf_to_images-1779107423303.txt.\nFormat: JSON with schema: {result: string}\nUse offset and limit parameters to read specific portions of the file, search within it for specific content, and jq to make structured queries.\nREQUIREMENTS FOR SUMMARIZATION/ANALYSIS/REVIEW:\n- You MUST read the content from the file at /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-4-projects-trace-verdict-study--claude-sessions-review-reviewer-1-7624f219/f76386b4-9d1f-4f92-b831-706bc4acd94d/tool-results/mcp-agent-ml-research-pdf_to_images-1779107423303.txt in sequential chunks until 100% of the content has been read.\n- If you receive truncation warnings when reading the file, reduce the chunk size until you have read 100% of the content without truncation.\n- Before producing ANY summary or analysis, you MUST explicitly describe what portion of the content you have read. ***If you did not read the entire content, you MUST explicitly state this.***\n",
  "mcpMeta": {
    "structuredContent": {

````

---
