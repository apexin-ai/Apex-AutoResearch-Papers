# Research conversation: [Round 1 审稿请求]: ## Round 1 审稿任务 — Reviewer 2（新颖性 + Related Work 完整性 + 写作质量 + 格式合规） ### Venue 信息 - **目标会议**: EMNLP 2026（通 — Part 1 of 4

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction? (July export snapshot)** · Conversation logs

[Transcript overview](../research-conversation-round-1-round-1-reviewer-2-related-work-venue-emnlp-2026.md) · [Part 2 →](part-002.md) · [Structured JSON](../../../sessions/e3/e3ac6b77731a3b922ca5.json)

## Before a recorded user message

## Before a recorded user message

2 recorded events


### Runtime record

_source line 1 · 2026-05-19T04:30:38.269Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-19T04:30:38.269Z",
  "sessionId": "0ff1fe81-4731-4c76-91b4-02652701ddff",
  "content": "[Round 1 审稿请求]:\n## Round 1 审稿任务 — Reviewer 2（新颖性 + Related Work 完整性 + 写作质量 + 格式合规）\n\n### Venue 信息\n- **目标会议**: EMNLP 2026（通过 ARR May 2026 cycle 提交）\n- **截止日期**: 2026-05-25\n- **页数限制**: Long paper, 正文 ≤ 8 页 + 无限参考文献页 + appendix 不计页数\n- **模板**: ACL official style, `\\usepackage[review]{acl}`\n- **匿名规则**: Double-blind\n- **Limitations section**: 必须有，不计入页数\n- **Checklist**: Responsible NLP Research Checklist 必须认真填写\n- **评分标准**: EMNLP 2026 通过 ARR 统一审稿，Overall Assessment: 5=Consider for Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1=Do not resubmit\n\n### 论文路径\n- 主文件: `projects/schema-dag-extraction/docs/paper/main.tex`\n- 各章节: `abstract.tex`, `introduction.tex`, `related_work.tex`, `experimental_setup.tex`, `results.tex`, `sdgd_negative.tex`, `discussion.tex`, `checklist.tex`, `prompt_appendix.tex`\n- 参考文献: `references.bib`\n\n### 你的审查侧重\n\n**新颖性 + Related Work 完整性 + 写作质量 + 格式合规**。具体关注：\n\n1. **新颖性评估**：\n   - SCS 的形式定义（pairwise cosine similarity of type name embeddings）与 LLM-PEE (2025) 的 partitioning criterion 相同。论文声称贡献在于 \"controlled experimental framework\" 而非 metric innovation — 这是否构成足够的新颖性增量？\n   - \"First controlled study isolating count and confusability\" 的 claim 是否成立？是否有遗漏的先前工作？\n   - Negative result (SDGD failure) 的贡献价值如何？\n   - 核心发现（type count dominates, confusability is RE-specific at batch level）对 community 的 actionable insight 有多大？\n\n2. **Related Work 完整性**：\n   - 是否覆盖了所有直接相关方法？特别关注：\n     - Schema decomposition for LLM IE 的最新工作（2025-2026）\n     - CrossAgentIE (ACL 2025 Findings) 的 cross-type debate 是否充分对比？\n     - Label confusion / inter-class similarity 在传统 ML 中的先前工作是否遗漏？\n     - Constrained decoding 对 error pattern 的影响是否有先前分析？\n   - 引用密度是否达到 EMNLP 标准？\n   - 是否有重要遗漏的 references？\n\n3. **写作质量**：\n   - Abstract 是否在 30 秒内传达核心价值？\n   - Introduction 叙事是否连贯（问题 → 洞察 → 方法 → 验证）？\n   - 全文主线是否统一（Abstract/Intro/Method/Results/Discussion/Conclusion 是否讲同一个故事）？\n   - 是否存在 AI 写作风格标志（em-dash, -ing phrases, 过度分段, 用词黑名单）？\n   - 专有名词是否首次出现时有定义？\n   - 图表信息密度是否足够？Caption 是否自包含？\n\n4. **格式合规**：\n   - 正文是否 ≤ 8 页？\n   - `\\usepackage[review]{acl}` 是否正确使用？\n   - 匿名化是否完整（无作者姓名泄露、无自引泄露）？\n   - Limitations section 位置是否正确（在 Conclusion 之后、References 之前）？\n   - Responsible NLP Research Checklist 填写质量如何？\n   - 引用格式是否一致？\n\n5. **论文定位与 framing**：\n   - 论文将自己定位为 \"analytical/empirical study\" 而非 \"new method\" — 对于 EMNLP 2026 是否合适？\n   - Title 中 \"Predict\" 是否准确反映论文内容（correlational evidence, not causal）？\n   - \"Two-dimensional\" framework 在 NER batch-level null 的情况下是否 oversell？\n\n请按 ARR 审稿标准输出完整审稿报告，包含：Summary, Strengths, Weaknesses (逐条编号, 标注 severity: Must-Fix / Should-Fix / Minor), Questions, Missing References, Overall Assessment (评分 + 置信度), Detailed Comments。"
}
```

---


### Runtime record

_source line 2 · 2026-05-19T04:30:38.274Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-19T04:30:38.274Z",
  "sessionId": "0ff1fe81-4731-4c76-91b4-02652701ddff"
}
```

---


## Round 1

## Round 1

100 recorded events


### User

_source line 3 · 2026-05-19T04:30:38.326Z_

[Round 1 审稿请求]:
## Round 1 审稿任务 — Reviewer 2（新颖性 + Related Work 完整性 + 写作质量 + 格式合规）

### Venue 信息
- **目标会议**: EMNLP 2026（通过 ARR May 2026 cycle 提交）
- **截止日期**: 2026-05-25
- **页数限制**: Long paper, 正文 ≤ 8 页 + 无限参考文献页 + appendix 不计页数
- **模板**: ACL official style, `\usepackage[review]{acl}`
- **匿名规则**: Double-blind
- **Limitations section**: 必须有，不计入页数
- **Checklist**: Responsible NLP Research Checklist 必须认真填写
- **评分标准**: EMNLP 2026 通过 ARR 统一审稿，Overall Assessment: 5=Consider for Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1=Do not resubmit

### 论文路径
- 主文件: `projects/schema-dag-extraction/docs/paper/main.tex`
- 各章节: `abstract.tex`, `introduction.tex`, `related_work.tex`, `experimental_setup.tex`, `results.tex`, `sdgd_negative.tex`, `discussion.tex`, `checklist.tex`, `prompt_appendix.tex`
- 参考文献: `references.bib`

### 你的审查侧重

**新颖性 + Related Work 完整性 + 写作质量 + 格式合规**。具体关注：

1. **新颖性评估**：
   - SCS 的形式定义（pairwise cosine similarity of type name embeddings）与 LLM-PEE (2025) 的 partitioning criterion 相同。论文声称贡献在于 "controlled experimental framework" 而非 metric innovation — 这是否构成足够的新颖性增量？
   - "First controlled study isolating count and confusability" 的 claim 是否成立？是否有遗漏的先前工作？
   - Negative result (SDGD failure) 的贡献价值如何？
   - 核心发现（type count dominates, confusability is RE-specific at batch level）对 community 的 actionable insight 有多大？

2. **Related Work 完整性**：
   - 是否覆盖了所有直接相关方法？特别关注：
     - Schema decomposition for LLM IE 的最新工作（2025-2026）
     - CrossAgentIE (ACL 2025 Findings) 的 cross-type debate 是否充分对比？
     - Label confusion / inter-class similarity 在传统 ML 中的先前工作是否遗漏？
     - Constrained decoding 对 error pattern 的影响是否有先前分析？
   - 引用密度是否达到 EMNLP 标准？
   - 是否有重要遗漏的 references？

3. **写作质量**：
   - Abstract 是否在 30 秒内传达核心价值？
   - Introduction 叙事是否连贯（问题 → 洞察 → 方法 → 验证）？
   - 全文主线是否统一（Abstract/Intro/Method/Results/Discussion/Conclusion 是否讲同一个故事）？
   - 是否存在 AI 写作风格标志（em-dash, -ing phrases, 过度分段, 用词黑名单）？
   - 专有名词是否首次出现时有定义？
   - 图表信息密度是否足够？Caption 是否自包含？

4. **格式合规**：
   - 正文是否 ≤ 8 页？
   - `\usepackage[review]{acl}` 是否正确使用？
   - 匿名化是否完整（无作者姓名泄露、无自引泄露）？
   - Limitations section 位置是否正确（在 Conclusion 之后、References 之前）？
   - Responsible NLP Research Checklist 填写质量如何？
   - 引用格式是否一致？

5. **论文定位与 framing**：
   - 论文将自己定位为 "analytical/empirical study" 而非 "new method" — 对于 EMNLP 2026 是否合适？
   - Title 中 "Predict" 是否准确反映论文内容（correlational evidence, not causal）？
   - "Two-dimensional" framework 在 NER batch-level null 的情况下是否 oversell？

请按 ARR 审稿标准输出完整审稿报告，包含：Summary, Strengths, Weaknesses (逐条编号, 标注 severity: Must-Fix / Should-Fix / Minor), Questions, Missing References, Overall Assessment (评分 + 置信度), Detailed Comments。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "8257bd0e-08b4-4530-aa87-1e185ea40a51",
  "type": "user",
  "uuid": "2a27a73e-c511-4feb-84ec-4d0408b184c7",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_reviewer_2_302b64f9",
  "sessionId": "0ff1fe81-4731-4c76-91b4-02652701ddff",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Runtime record

_source line 4 · 2026-05-19T04:30:38.325Z_

```json
{
  "parentUuid": "2a27a73e-c511-4feb-84ec-4d0408b184c7",
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
  "uuid": "f6381b41-bb59-46bf-8769-cde3ee1fdb5a",
  "timestamp": "2026-05-19T04:30:38.325Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_reviewer_2_302b64f9",
  "sessionId": "0ff1fe81-4731-4c76-91b4-02652701ddff",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---


### Runtime record

_source line 5 · 2026-05-19T04:30:38.325Z_

```json
{
  "parentUuid": "f6381b41-bb59-46bf-8769-cde3ee1fdb5a",
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
  "uuid": "38cac7b1-7d78-418c-bb4f-00d38024d424",
  "timestamp": "2026-05-19T04:30:38.325Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_reviewer_2_302b64f9",
  "sessionId": "0ff1fe81-4731-4c76-91b4-02652701ddff",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---


### Runtime record

_source line 6 · 2026-05-19T04:30:38.325Z_

```json
{
  "parentUuid": "38cac7b1-7d78-418c-bb4f-00d38024d424",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "66e7dd49-acb8-4d2d-9491-9aebaef36faa",
  "timestamp": "2026-05-19T04:30:38.325Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_reviewer_2_302b64f9",
  "sessionId": "0ff1fe81-4731-4c76-91b4-02652701ddff",
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
  "aiTitle": "Review Round 1 schema-dag-extraction paper for EMNLP 2026",
  "sessionId": "0ff1fe81-4731-4c76-91b4-02652701ddff"
}
```

---


### Assistant

_source line 8 · 2026-05-19T04:30:42.371Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to perform a detailed review of a paper as Reviewer 2 for EMNLP 2026. Let me start by following the session start skill and then reading the paper materials.

First, I need to:
1. Search for ARR/EMNLP 2026 reviewer guidelines
2. Read the paper (main.tex and all section files)
3. Check format compliance

Let me begin by reading the paper files and searching for reviewer guidelines simultaneously.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "66e7dd49-acb8-4d2d-9491-9aebaef36faa",
  "isSidechain": false,
  "requestId": "req_011CbBJKWt6uKDWRV7pubg4q",
  "type": "assistant",
  "uuid": "af0bdb47-b268-4998-a078-c22d0580eafc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_reviewer_2_302b64f9",
  "sessionId": "0ff1fe81-4731-4c76-91b4-02652701ddff",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01J5VXgxE5CTUo1xG725Em78",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 16229,
      "cache_read_input_tokens": 11841,
      "output_tokens": 282,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 16229,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 282,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 16229,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 16229
          },
          "type": "message"
        }
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

_source line 9 · 2026-05-19T04:30:43.421Z_

开始审稿。先并行读取论文各章节和搜索 ARR 官方审稿标准。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "af0bdb47-b268-4998-a078-c22d0580eafc",
  "isSidechain": false,
  "requestId": "req_011CbBJKWt6uKDWRV7pubg4q",
  "type": "assistant",
  "uuid": "b07d275d-e577-482f-aa5e-50591007a6ce",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_reviewer_2_302b64f9",
  "sessionId": "0ff1fe81-4731-4c76-91b4-02652701ddff",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01J5VXgxE5CTUo1xG725Em78",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 16229,
      "cache_read_input_tokens": 11841,
      "output_tokens": 282,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 16229,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 282,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 16229,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 16229
          },
          "type": "message"
        }
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

_source line 10 · 2026-05-19T04:30:45.192Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01DuvGm2PCCeUHcfaHecfbEL`</summary>

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
  "parentUuid": "b07d275d-e577-482f-aa5e-50591007a6ce",
  "isSidechain": false,
  "requestId": "req_011CbBJKWt6uKDWRV7pubg4q",
  "type": "assistant",
  "uuid": "e480813d-cda5-4dc4-9e30-b0195e7c299f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_reviewer_2_302b64f9",
  "sessionId": "0ff1fe81-4731-4c76-91b4-02652701ddff",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01J5VXgxE5CTUo1xG725Em78",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 16229,
      "cache_read_input_tokens": 11841,
      "output_tokens": 282,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 16229,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 282,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 16229,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 16229
          },
          "type": "message"
        }
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

_source line 11 · 2026-05-19T04:30:45.203Z_

<details><summary>↩ Tool result · `toolu_01DuvGm2PCCeUHcfaHecfbEL`</summary>

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
  "parentUuid": "e480813d-cda5-4dc4-9e30-b0195e7c299f",
  "isSidechain": false,
  "promptId": "8257bd0e-08b4-4530-aa87-1e185ea40a51",
  "type": "user",
  "uuid": "97ce6333-25f8-4350-9c8c-4113203e55fc",
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
  "sourceToolAssistantUUID": "e480813d-cda5-4dc4-9e30-b0195e7c299f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_reviewer_2_302b64f9",
  "sessionId": "0ff1fe81-4731-4c76-91b4-02652701ddff",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Tool call

_source line 12 · 2026-05-19T04:30:51.598Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Rinx95MaPb4ffB8FByTCgp`</summary>

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
  "parentUuid": "97ce6333-25f8-4350-9c8c-4113203e55fc",
  "isSidechain": false,
  "requestId": "req_011CbBJL3Mfp6QVPxgqBTm4o",
  "type": "assistant",
  "uuid": "da49144f-ceab-4df6-b939-2b30013b573e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_reviewer_2_302b64f9",
  "sessionId": "0ff1fe81-4731-4c76-91b4-02652701ddff",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PMdzHtBXazYPW4S8Z616zu",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2278,
      "cache_read_input_tokens": 28070,
      "output_tokens": 849,
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
          "output_tokens": 849,
          "cache_read_input_tokens": 28070,
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

_source line 13 · 2026-05-19T04:30:51.812Z_

<details open><summary>🔧 Tool call — Read · `toolu_01KrDxZWjXBKqFFF8WAFSf3H`</summary>

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
  "parentUuid": "da49144f-ceab-4df6-b939-2b30013b573e",
  "isSidechain": false,
  "requestId": "req_011CbBJL3Mfp6QVPxgqBTm4o",
  "type": "assistant",
  "uuid": "ce8e5d71-3160-4841-a4e0-52e94fa0e0d5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_reviewer_2_302b64f9",
  "sessionId": "0ff1fe81-4731-4c76-91b4-02652701ddff",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PMdzHtBXazYPW4S8Z616zu",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2278,
      "cache_read_input_tokens": 28070,
      "output_tokens": 849,
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
          "output_tokens": 849,
          "cache_read_input_tokens": 28070,
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

_source line 14 · 2026-05-19T04:30:51.832Z_

<details><summary>↩ Tool result · `toolu_01KrDxZWjXBKqFFF8WAFSf3H`</summary>

```text
1	\begin{abstract}
2	Training-free LLM information extraction degrades as schema complexity grows, yet prior work conflates two factors: type count and type confusability. We present what is, to our knowledge, the first controlled study isolating these factors across NER, RE, and event detection on four datasets. We quantify confusability via the Schema Confusability Score (SCS) and its batch-level aggregation, the Batch Confusability Score (BCS). Degradation operates along two largely additive dimensions: count-related recall decline (up to $-$49\,pp for document-level RE) dominates confusability-related type substitution, though typical batches yield modest ${\sim}$2\,pp gaps. BCS explains 22--53\% of cross-batch RE accuracy variance under RE's forced-choice format but shows no batch-level signal for NER, where errors scatter across missed entities and boundary failures. Few-shot demonstrations widen the confusability gap (+4.3\,pp under 5-shot). Schema decomposition fails due to merge amplification (NER) and routing failure (RE). Pairwise confusability is a schema-structural property: effects replicate across model scales and families, and persist under varied prompt designs.
3	\end{abstract}
4	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ce8e5d71-3160-4841-a4e0-52e94fa0e0d5",
  "isSidechain": false,
  "promptId": "8257bd0e-08b4-4530-aa87-1e185ea40a51",
  "type": "user",
  "uuid": "732ac315-f0eb-406a-b88f-7b919ccbe90a",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/abstract.tex",
      "content": "\\begin{abstract}\nTraining-free LLM information extraction degrades as schema complexity grows, yet prior work conflates two factors: type count and type confusability. We present what is, to our knowledge, the first controlled study isolating these factors across NER, RE, and event detection on four datasets. We quantify confusability via the Schema Confusability Score (SCS) and its batch-level aggregation, the Batch Confusability Score (BCS). Degradation operates along two largely additive dimensions: count-related recall decline (up to $-$49\\,pp for document-level RE) dominates confusability-related type substitution, though typical batches yield modest ${\\sim}$2\\,pp gaps. BCS explains 22--53\\% of cross-batch RE accuracy variance under RE's forced-choice format but shows no batch-level signal for NER, where errors scatter across missed entities and boundary failures. Few-shot demonstrations widen the confusability gap (+4.3\\,pp under 5-shot). Schema decomposition fails due to merge amplification (NER) and routing failure (RE). Pairwise confusability is a schema-structural property: effects replicate across model scales and families, and persist under varied prompt designs.\n\\end{abstract}\n",
      "numLines": 4,
      "startLine": 1,
      "totalLines": 4
    }
  },
  "sourceToolAssistantUUID": "ce8e5d71-3160-4841-a4e0-52e94fa0e0d5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_reviewer_2_302b64f9",
  "sessionId": "0ff1fe81-4731-4c76-91b4-02652701ddff",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Tool result

_source line 15 · 2026-05-19T04:30:51.867Z_

<details><summary>↩ Tool result · `toolu_01Rinx95MaPb4ffB8FByTCgp`</summary>

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
40	\item \textbf{Model coverage.} Primary experiments use Qwen3-32B with cross-model validation on Llama-3.1-8B, 70B-Instruct (FP8), and Gemini 2.5 Flash (API). Dimension~1 has been validated across all four models including a proprietary one; Dimension~2 has been verified only on open-weight models and was not robustly detectable on NER at 8B scale, likely due to floor effects.
41	
42	\item \textbf{Effect size and statistical design.} Pairwise SCS explains 1.3--1.7\% of type confusion variance; entity frequency, prompt position, and mention ambiguity likely account for the remainder. The count $\times$ BCS interaction is bounded under the linear specification (TOST $p = 0.003$ at $\pm 3$\,pp on FewRel; DocRED inconclusive, Appendix~\ref{sec:appendix_factorial}) but inconclusive on the logit scale ($p = 0.209$). BCS-controlled experiments use a single seed with greedy decoding; the residual SD of 0.88\,pp (Appendix~\ref{app:variance-decomposition}) supports robustness but precise magnitudes may vary.
43	
44	\item \textbf{Task format dependency.} BCS batch-level prediction is demonstrated only under RE's forced-choice classification format. An unconstrained decoding ablation ($n = 25$) confirms this: removing the enum constraint eliminates the BCS--accuracy correlation ($\rho = -0.14$, $p = 0.49$), establishing that the batch-level signal is specific to forced-choice RE. NER exact-match evaluation conflates boundary and type errors, and relaxed matching may yield different confusability effect sizes.
45	
46	\item \textbf{Causal mechanism.} The study establishes correlational evidence with controlled stratification; mechanistic analysis at the attention or logit level is needed to confirm the causal pathway. A post-hoc renaming experiment (Appendix~\ref{app:renaming}) confirms this concern: replacing high-SCS labels with semantically distinct paraphrases reduced pairwise embedding similarity but decreased accuracy by 3--9\,pp, as label unfamiliarity introduced errors that outweighed any confusability reduction.
47	
48	\item \textbf{Data contamination.} FewRel (2018) may appear in pretraining corpora, but train-origin relations show numerically lower accuracy than val-origin ($-8.8$\,pp, n.s.), opposite to the contamination hypothesis. DocRED (2019) provides a lower-contamination-risk replication with consistent slopes ($R^2 = 0.53$; Appendix~\ref{app:split-origin}).
49	\end{enumerate}
50	
51	\paragraph{Multiple comparisons.} Cross-dataset comparisons serve as independent replications and do not require family-wise correction \citep{rothman-1990}. Within-dataset secondary analyses involve multiple looks; we report individual $p$-values and note that core claims rest on $p < 0.001$ \citep{dror-2018-significance,card-2020-power}.
52	
53	\input{checklist}
54	
55	\bibliography{references}
56	
57	\appendix
58	
59	\section{Additional Figures}
60	\label{sec:appendix_figures}
61	
62	\begin{table}[h]
63	\centering
64	\small
65	\begin{tabular}{lrr}
66	\toprule
67	\textbf{Count} & \textbf{Llama-3.1-8B} & \textbf{Qwen3-32B} \\
68	\midrule
69	1 & 0.702 & 0.640 \\
70	64 & 0.273 & 0.304 \\
71	\midrule
72	Decline & $-$43\,pp & $-$34\,pp \\
73	\bottomrule
74	\end{tabular}
75	\caption{Cross-model count-curve replication on Few-NERD (text-match recall). Both models show a general declining trend in recall with schema size. Per-batch correlation $r = 0.725$. Qwen3-32B values use the v2 prompt (\S\ref{sec:model}) for fair cross-model comparison; the count-curve results in \S\ref{sec:count_curves} use the v1 prompt, yielding higher absolute recall (0.72 vs.\ 0.64 at count${}\,=\,1$) due to over-prediction under v1.}
76	\label{tab:cross_model}
77	\end{table}
78	
79	\begin{table}[h]
80	\centering
81	\small
82	\resizebox{\columnwidth}{!}{%
83	\begin{tabular}{crrrrrr}
84	\toprule
85	& \multicolumn{3}{c}{\textbf{Llama-3.1-8B}} & \multicolumn{3}{c}{\textbf{Qwen3-32B}} \\
86	\cmidrule(lr){2-4} \cmidrule(lr){5-7}
87	\textbf{Count} & \textbf{Low} & \textbf{High} & \textbf{$\Delta$} & \textbf{Low} & \textbf{High} & \textbf{$\Delta$} \\
88	\midrule
89	8 & 78.1\% & 51.0\% & $-$27.1 & 82.3\% & 51.0\% & $-$31.2 \\
90	16 & 75.5\% & 51.6\% & $-$23.9 & 82.8\% & 51.6\% & $-$31.2 \\
91	\bottomrule
92	\end{tabular}}
93	\caption{Cross-model BCS-controlled FewRel accuracy.  High-BCS accuracy converges to $\approx$51\% regardless of model, while low-BCS accuracy reflects model capacity differences.  The confusability gap ($\Delta$, in pp) is 77--87\% as large on Llama-3.1-8B as on Qwen3-32B.}
94	\label{tab:cross_model_bcs}
95	\end{table}
96	
97	\begin{table}[h]
98	\centering
99	\small
100	\resizebox{\columnwidth}{!}{%
101	\begin{tabular}{llrrrrrrr}
102	\toprule
103	 & & \multicolumn{5}{c}{\textbf{BCS Bin}} & & \\
104	\cmidrule(lr){3-7}
105	\textbf{Task} & \textbf{Error} & \textbf{Solo} & \textbf{Low} & \textbf{Mid} & \textbf{High} & \textbf{V.High} & \textbf{$\rho$} & \textbf{$p$} \\
106	\midrule
107	NER & IntraSub & 0\% & 1.6\% & 10.6\% & 49.4\% & --- & 1.000 & ${<}0.001$ \\
108	RE  & IntraSub & 0\% & 4.2\% & 13.0\% & 20.3\% & 32.3\% & 0.954 & ${<}\,0.001$ \\
109	\midrule
110	NER & Missed & --- & 42.8\% & 64.8\% & 49.9\% & --- & --- & --- \\
111	RE  & Missed & --- & 10.4\% & 11.3\% & 13.1\% & 15.7\% & --- & --- \\
112	\bottomrule
113	\end{tabular}}
114	\caption{Intra-batch substitution (IntraSub) and missed-entity rates by BCS bin, with Spearman $\rho$ computed over $n=154$ individual batches (RE) and $n=148$ batches (NER). NER has 4 BCS bins; RE has 5.}
115	\label{tab:error_taxonomy}
116	\end{table}
117	
118	\section{SDGD Full Protocol and Results}
119	\label{sec:appendix_sdgd}
120	
121	We construct a thresholded confusability graph $G = (V, E)$ where each type is a vertex and an edge connects types $t_i, t_j$ whenever $\text{SCS}(t_i, t_j) > \tau$. Greedy graph coloring (\textsc{largest\_first}) assigns each type to a color such that no two adjacent (i.e., highly confusable) types share a color. Each color class forms one extraction batch, and predictions are merged via set union. We compare four modes: (i)~\textbf{single\_pass}, the undecomposed baseline; (ii)~\textbf{sdgd\_zero}, SCS-guided partitioning; (iii)~\textbf{random\_batch}, random partitioning with matched batch sizes; and (iv)~\textbf{per\_type}, the extreme case where each type is extracted in isolation.
122	
123	Single-pass extraction achieves F1\,=\,0.445 (P\,=\,0.563, R\,=\,0.368). SDGD obtains F1\,=\,0.251 (P\,=\,0.210, R\,=\,0.314), a 44\% relative drop. Random batching reaches F1\,=\,0.320 (P\,=\,0.249, R\,=\,0.446), and per-type extraction yields F1\,=\,0.292 (P\,=\,0.194, R\,=\,0.586). Every decomposition mode falls below the single-pass baseline (Table~\ref{tab:sdgd_results}).
124	
125	\begin{table}[h]
126	\centering
127	\small
128	\resizebox{\columnwidth}{!}{%
129	\begin{tabular}{lrccc}
130	\toprule
131	\textbf{Mode} & \textbf{\# Batches} & \textbf{Precision} & \textbf{Recall} & \textbf{F1} \\
132	\midrule
133	single\_pass & 1 & 0.563 & 0.368 & 0.445 \\
134	\midrule
135	sdgd\_zero (v1) & 8 & 0.210 & 0.314 & 0.251 \\
136	random\_batch (v1) & 8 & 0.249 & 0.446 & 0.320 \\
137	per\_type & 66 & 0.194 & 0.586 & 0.292 \\
138	\midrule
139	sdgd\_zero (v2) & 4 & 0.324 & 0.191 & 0.241 \\
140	random\_batch (v2) & 8 & 0.331 & 0.276 & 0.301 \\
141	\bottomrule
142	\end{tabular}}
143	\caption{Few-NERD extraction under decomposition modes. V1 uses union merge; v2 uses confidence-gated merge with \texttt{min\_batch\_size=8} (reducing 8$\to$4 batches for sdgd\_zero). All decomposition modes produce lower F1 than the single-pass baseline. All modes use the v1 prompt.}
144	\label{tab:sdgd_results}
145	\end{table}
146	
147	Decomposition boosts recall (per-type recall reaches 0.586 versus single-pass 0.368) but devastates precision (0.194 versus 0.563). When the same text is presented to the model $k$ times with different type subsets, each pass independently generates entity predictions. Because LLM outputs are not calibrated across passes, the union merge step accumulates overlapping and contradictory predictions and inflates false positives.
148	
149	Our v2 merge ranks competing predictions by the LLM's self-reported confidence and retains only the highest-scoring candidate for each span. Confidence gating improves precision (sdgd\_zero: 0.210$\to$0.324; random\_batch: 0.249$\to$0.331), but at the cost of disproportionate recall loss (0.314$\to$0.191; 0.446$\to$0.276), and both modes produce lower F1 (sdgd\_zero: 0.251$\to$0.241; random\_batch: 0.320$\to$0.301).
150	
151	\subsection{Practical Routing Strategies on RE}
152	\label{sec:appendix_routing}
153	
154	We evaluate five non-oracle routing strategies on FewRel 80-relation RE using graph-coloring sub-schema decomposition (same grouping as Table~\ref{tab:batch_composition}). Each strategy selects a single sub-schema for each test instance and returns that sub-schema's prediction.
155	
156	\begin{table}[h]
157	\centering
158	\small
159	\resizebox{\columnwidth}{!}{\begin{tabular}{@{}lrr@{}}
160	\toprule
161	\textbf{Strategy} & \textbf{Accuracy} & \textbf{$\Delta$ vs.\ Single-Pass} \\
162	\midrule
163	Oracle (gold label) & 72.4\% & +22.0\,pp \\
164	\midrule
165	Max-conf (positive only) & 36.5\% & $-$14.0\,pp \\
166	None-aware & 36.5\% & $-$14.0\,pp \\
167	Margin (positive only) & 35.9\% & $-$14.5\,pp \\
168	Max-conf (all) & 27.7\% & $-$22.7\,pp \\
169	Random & 14.7\% & $-$35.7\,pp \\
170	\midrule
171	Single-pass (no decomposition) & 50.4\% & --- \\
172	\bottomrule
173	\end{tabular}}
174	\caption{Routing strategy comparison on FewRel 80-relation RE with graph-coloring sub-schema decomposition. Oracle requires gold labels. All practical (non-oracle) strategies perform below the single-pass baseline. The failure stems from constrained decoding (enum constraint), which forces confident predictions in every sub-schema: 73.4\% of instances receive positive predictions from 3--5 sub-schemas simultaneously, with per-sub-schema none-rates of only 20--40\%.}
175	\label{tab:routing_strategies}
176	\end{table}
177	
178	\section{Factorial Analysis and Separability Test}
179	\label{sec:appendix_factorial}
180	
181	To formally test whether count and confusability effects are additive, we fit a multiple regression (accuracy $\sim$ $\log_2$\,count $+$ BCS $+$ count$\times$BCS) across 69 batches from FewRel spanning five count levels ($k \in \{4, 8, 16, 32, 40\}$). Both main effects are significant (count: $p = 0.008$; BCS: $p = 0.0002$; $R^2 = 0.52$), but the interaction term is negligible (0.47\,pp). A TOST equivalence test with a $\pm 3$\,pp margin confirms that the interaction is bounded well below practical significance ($p_{\text{TOST}} = 0.003$); this supports bounded interaction between count and confusability effects.
182	
183	A $2 \times 2$ factorial sensitivity check on FewRel (count $\in \{8, 16\}$, BCS low/high; $n = 54$) was inconclusive ($p_{\text{TOST}} = 0.56$) due to limited power; this does not contradict the primary finding but limits generalization beyond the regression framework. The Few-NERD factorial (\S\ref{sec:multi_channel}) similarly did not reach significance ($p = 0.50$). The regression approach provides the stronger test by leveraging the full count range.
184	
185	\paragraph{Equivalence margin justification.}
186	We set the $\pm 3$\,pp margin based on three converging anchors. \emph{Empirical}: typical random-batch confusability variation produces 2--5\,pp accuracy differences (batch SD $\approx 4.6$\,pp at count 32). \emph{Practical}: a ${<}3$\,pp accuracy difference falls below deployment-relevant thresholds. \emph{Statistical}: 3\,pp $\approx 0.5 \times$ batch SD, equivalent to Cohen's $d \approx 0.5$ (medium effect threshold; \citealt{lakens-2017-equivalence}). A 3\,pp interaction atop the 2.2\,pp confusability main effect would represent ${>}130\%$ amplification, fundamentally changing whether confusability warrants mitigation. At $\pm 2$\,pp (marginally equivalent, $p = 0.047$), interaction remains bounded below the main effect itself.
187	
188	\begin{table}[h]
189	\centering
190	\small
191	\begin{tabular}{crrl}
192	\toprule
193	\textbf{Margin (pp)} & \textbf{$t_{\text{upper}}$} & \textbf{$p_{\text{TOST}}$} & \textbf{Conclusion} \\
194	\midrule
195	$\pm 1$ & $-0.59$ & $0.278$ & Inconclusive \\
196	$\pm 2$ & $-1.70$ & $0.047$ & Equivalent \\
197	$\pm 3$ & $-2.81$ & $0.003$ & Equivalent \\
198	$\pm 5$ & $-5.02$ & ${<}\,0.001$ & Equivalent \\
199	\bottomrule
200	\end{tabular}
201	\caption{TOST sensitivity analysis across equivalence margins. The interaction effect (0.47\,pp, 90\% CI [$-$1.0, 2.0]\,pp) is bounded below 2\,pp at marginal significance ($p = 0.047$); the $\pm 3$\,pp choice does not drive the equivalence conclusion. At $\pm 1$\,pp, equivalence is inconclusive ($p = 0.278$), meaning interaction could reach approximately half the main effect magnitude.}
202	\label{tab:tost_sensitivity}
203	\end{table}
204	
205	\paragraph{Logit-scale sensitivity.}
206	Because accuracy near 50\% compresses interaction effects on the linear scale, we refit the regression on logit-transformed accuracy. The logit-scale interaction (0.111 logit units, $p = 0.047$, 90\% CI [0.019, 0.203]) is marginally significant, and TOST at the equivalent $\pm 3$\,pp margin ($\pm 0.156$ logit at median accuracy) is inconclusive ($p_{\text{TOST}} = 0.209$). However, back-transforming the interaction to the probability scale at the observed floor ($p = 0.51$) yields 2.78\,pp, still within the $\pm 3$\,pp margin; at the median baseline ($p = 0.65$), the back-transformed effect is 2.53\,pp. The logit TOST is inconclusive due to limited power ($n = 69$, wide CI) rather than a large effect size: the point estimate remains below the equivalence bound at all observed baselines. We retain the linear-scale TOST as the primary test and report this logit analysis as a sensitivity check.
207	
208	\paragraph{DocRED factorial.}
209	A $2 \times 2$ factorial on DocRED (count $\in \{16, 32\}$, BCS median split at 0.55; $n = 70$) yields a larger interaction estimate (+5.7\,pp, 95\% CI [$-$1.6, 13.0]): the BCS effect is $-$10.6\,pp at count 16 but only $-$4.9\,pp at count 32. TOST at $\pm 3$\,pp is not established ($p = 0.77$). The asymmetry likely reflects baseline compression: at count 32, accuracy approaches chance ($\sim$49\%), leaving less room for confusability to further reduce performance. We therefore restrict the bounded-interaction conclusion to sentence-level RE.
210	
211	\section{Within-Pool CI Details}
212	\label{sec:appendix_within_pool}
213	
214	The quartile $\Delta$ for 80-pool 16-relation subsets ($-$3.92\,pp, 95\% CI [$-$8.17, $+$0.38]) crosses zero, reflecting the compressed BCS range within that pool (0.46--0.68 vs.\ 0.48--0.71 for the independent pool). Within this narrow band, the quartile contrast lacks statistical power to detect the effect that the regression identifies. The full 80-relation condition ($n = 25$) is underpowered for both the slope (CI: [$-$1.303, $+$1.695]) and quartile analyses; we include it in Table~\ref{tab:within_pool} for completeness but do not draw inferential conclusions from it.
215	
216	\section{Controlling for Centrality Confounds in MAVEN Per-Type Analysis}
217	\label{sec:appendix_residualized_bcs}
218	
219	Section~\ref{sec:centrality_confound} identifies a centrality confound in MAVEN's per-type BCS--F1 correlation: both embeddings show a \emph{positive} raw correlation, opposite to the expected direction. Here we formalize this analysis by identifying specific confounders for each embedding and testing whether the BCS--F1 relationship survives partial correlation controlling for these confounders.
220	
221	\paragraph{Confound identification.}
222	For each embedding, we computed the correlation between mean BCS and candidate confounders (type frequency, degree centrality at threshold 0.7) across MAVEN's 149 active event types. The dominant confound differs by embedding:
223	\begin{itemize}[itemsep=2pt,leftmargin=*]
224	\item \textbf{MiniLM}: BCS correlates with log type frequency ($r = 0.201$). Frequent types have more training signal and are extracted more reliably, which produces the positive BCS--F1 association.
225	\item \textbf{Qwen3}: BCS correlates strongly with degree centrality ($r = 0.854$). In the Qwen3 embedding space, high-BCS types are those with many semantic neighbors, central, well-represented types that the model extracts well.
226	\end{itemize}
227	
228	\paragraph{Partial correlation results.}
229	Table~\ref{tab:residualized_bcs} reports raw Spearman $\rho$ and partial Pearson $r$ after controlling for the identified confounders. Under single-variable control, both correlations weaken to non-significance. Under joint control (log frequency $+$ degree centrality simultaneously), neither embedding retains a significant BCS--F1 association.
230	
231	\begin{table}[h]
232	\centering
233	\small
234	\resizebox{\columnwidth}{!}{%
235	\begin{tabular}{llcccc}
236	\toprule
237	\textbf{Embedding} & \textbf{Control} & \textbf{Raw $\rho$} & \textbf{Raw $p$} & \textbf{Partial $r$} & \textbf{Partial $p$} \\
238	\midrule
239	MiniLM & --- & $+$0.208 & $0.011$ & --- & --- \\
240	MiniLM & log freq & --- & --- & $+$0.133 & $0.11$ \\
241	MiniLM & log freq $+$ degree & --- & --- & --- & $0.23$ \\
242	\midrule
243	Qwen3 & --- & $+$0.184 & $0.025$ & --- & --- \\
244	Qwen3 & degree centrality & --- & --- & $+$0.063 & $0.44$ \\
245	Qwen3 & log freq $+$ degree & --- & --- & --- & $0.44$ \\
246	\bottomrule
247	\end{tabular}}
248	\caption{MAVEN per-type BCS--F1 correlation before and after controlling for centrality confounders. Raw correlations are Spearman $\rho$; partial correlations are Pearson $r$ from residualized regression. Degree centrality is computed on the SCS graph at threshold 0.7. All values from experiment \texttt{exp\_maven\_residualized\_bcs}.}
249	\label{tab:residualized_bcs}
250	\end{table}
251	
252	\paragraph{Interpretation.}
253	The two embeddings encode different aspects of the same underlying confound. MiniLM, a smaller sentence encoder, produces a tighter embedding cluster for MAVEN's FrameNet-derived types; here, type frequency is the primary confounder because frequent types accumulate higher mean similarity to the dense cluster. Qwen3, with a larger representation space, differentiates types enough that frequency is not the dominant factor, but degree centrality (the count of strong semantic neighbors) becomes the confound instead. In both cases, the positive raw correlation reflects a centrality artifact: types that are semantically central are both high-BCS and easy to extract.
254	
255	Under joint control, both embeddings yield $p > 0.2$; the raw positive BCS--F1 correlation on MAVEN is thus fully attributable to centrality-related confounders. This does not invalidate the confusability hypothesis; the pairwise SCS--confusion correlation on MAVEN remains significant (MiniLM $r = 0.129$, $p < 0.001$; Table~\ref{tab:pairwise}). Rather, it demonstrates that per-type aggregation (mean BCS) conflates confusability with centrality in semantically homogeneous schemas, and that pairwise analysis or explicit confound adjustment is required in such settings.
256	
257	\section{Batch Composition Results}
258	\label{sec:appendix_batch_composition}
259	
260	\begin{table}[h]
261	\centering
262	\small
263	\resizebox{\columnwidth}{!}{%
264	\begin{tabular}{@{}lcc@{}}
265	\toprule
266	\textbf{Condition} & \textbf{Accuracy} & \textbf{Mean BCS} \\
267	\midrule
268	Single-pass (80 types) & 0.504 & 0.557 \\
269	Random batching (15 seeds)$^\dagger$ & 0.788\,$\pm$\,0.018 & 0.559 \\
270	Confus.-aware (graph coloring) & \textbf{0.802} & 0.552 \\
271	\bottomrule
272	\end{tabular}}
273	\caption{Batch composition on FewRel 80-relation RE with oracle routing. $^\dagger$Mean $\pm$ SD across 15 random seeds.}
274	\label{tab:batch_composition}
275	\end{table}
276	
277	See the accompanying discussion in \S\ref{sec:sdgd}.
278	
279	\input{prompt_appendix}
280	
281	\section{Prompt Version Sensitivity Analysis}
282	\label{sec:appendix_prompt_sensitivity}
283	
284	We assess whether the confusability effects reported in \S\ref{sec:bcs_controlled}--\ref{sec:multi_channel} are robust to prompt design by replicating key experiments under the v2 prompt (\S\ref{sec:model}; full templates in Appendix~\ref{sec:appendix_prompts}).
285	
286	\paragraph{RE (FewRel).}
287	Under the v1 prompt, the extreme-batch BCS gap (Table~\ref{tab:bcs_controlled}) is substantial. Under v2, with $n{=}25$ batches per group and wider BCS contrast (low-BCS range [0.356, 0.367]; high-BCS range [0.791, 0.811]), the gap is $-$25.5\,pp (low-BCS 85.2\% vs.\ high-BCS 59.7\%; 95\% CI: [22.4, 28.6]; $p < 0.001$; Pearson $r = -0.919$). The effect is significant, directionally consistent with v1, and only modestly attenuated in magnitude ($-$5.7\,pp reduction). An earlier $n{=}5$ evaluation with narrower BCS contrast (0.21) yielded a smaller gap of $-$7.9\,pp (CI: [$-$5.2, $+$21.5]), illustrating how limited statistical power and restricted BCS range can obscure the underlying signal, a cautionary note for small-sample prompt sensitivity studies.
288	
289	\paragraph{NER (Few-NERD).}
290	The batch-level BCS--F1 correlation is null under both prompt versions. Pooling across three seeds and all count levels ($n = 450$), the correlation is $r = 0.004$ ($p = 0.94$). An earlier small-sample analysis ($n = 27$, single seed) had reported positive correlations ($r = +0.50$/$+0.58$), but these were driven by an accidental BCS--type-frequency confound: those 27 batches exhibited $r(\text{BCS}, \text{freq}) = 0.53$, creating a spurious path through frequency to F1. After controlling for type frequency, the partial correlation is non-significant in both the small ($r = 0.28$, $p = 0.16$) and large ($r = -0.12$, $p = 0.29$) samples. The pairwise SCS--confusion analysis (\S\ref{sec:pairwise}), which is immune to this batch-level aggregation artifact, remains the primary evidence for the NER confusability dimension.
291	
292	\paragraph{Interpretation.}
293	The $n{=}25$ v2 result confirms that the confusability effect is directionally consistent across prompt designs, with attenuated magnitude: the gap narrows ($-$5.7\,pp) but remains highly significant ($p < 0.001$, $r = -0.919$). The earlier $n{=}5$ non-significance reflected insufficient power and narrow BCS contrast, not absence of the effect. V2's stricter format constraints raise the baseline accuracy (low-BCS 85.2\% vs.\ 82.3\%), but type confusion under high confusability persists (59.7\% vs.\ 51.0\%). Prompt design modulates the practical magnitude of the confusability effect but does not eliminate it, ruling out prompt-specific confounding as the primary source. The underlying confusability signal (pairwise SCS--confusion correlation and the directional BCS--accuracy relationship) persists across both prompt versions.
294	
295	\subsection{Cross-Prompt-Variant BCS Correlation}
296	\label{sec:appendix_prompt_variants}
297	
298	To verify that the BCS--accuracy relationship is not an artifact of a specific prompt template, we evaluate four structurally distinct prompt variants on FewRel 80-relation RE at two count levels (8 and 32), with 10 random batches per condition.
299	
300	\begin{table}[h]
301	\centering
302	\small
303	\resizebox{\columnwidth}{!}{\begin{tabular}{llrrrr}
304	\toprule
305	\textbf{Variant} & \textbf{Count} & \textbf{Mean Acc} & \textbf{$r$} & \textbf{$p$} \\
306	\midrule
307	V2 (definition-first) & 8 & 0.769 & $-$0.333 & 0.348 \\
308	V2 (definition-first) & 32 & 0.564 & $-$0.648 & 0.043 \\
309	Instruction-rewrite & 8 & 0.847 & $-$0.223 & 0.536 \\
310	Instruction-rewrite & 32 & 0.662 & $-$0.469 & 0.171 \\
311	Chain-of-thought & 8 & 0.749 & $+$0.254 & 0.478 \\
312	Chain-of-thought & 32 & 0.617 & $-$0.566 & 0.088 \\
313	Minimal & 8 & 0.852 & $-$0.170 & 0.638 \\
314	Minimal & 32 & 0.615 & $-$0.771 & 0.009 \\
315	\bottomrule
316	\end{tabular}}
317	\caption{BCS--accuracy Pearson correlation across four prompt variants. At count 32, all four variants show negative BCS--accuracy correlations ($r \leq -0.47$), with two reaching $p < 0.05$. At count 8, the narrower BCS range reduces statistical power.}
318	\label{tab:prompt_variants}
319	\end{table}
320	
321	At count 32, all four variants produce negative BCS--accuracy correlations ($r$ ranges from $-$0.47 to $-$0.77), with V2 ($p = 0.043$) and Minimal ($p = 0.009$) reaching significance and Chain-of-thought approaching it ($p = 0.088$). At count 8, correlations are weaker and nonsignificant across all variants, consistent with the narrower BCS range at lower schema complexity reducing the detectable effect size. Rather than applying Bonferroni correction, which assumes independent hypotheses inappropriate for correlated prompt variants testing the same underlying signal, we note directional consistency: 7 of 8 conditions show negative BCS--accuracy slopes, consistent with the primary finding \citep{rothman-1990}. These results confirm that the confusability effect arises from schema composition, not prompt-specific phrasing.
322	
323	\section{BCS Aggregation Sensitivity}
324	\label{sec:appendix_bcs_sensitivity}
325	
326	We define Batch Confusability Score (BCS) as the \emph{mean} pairwise SCS across all type pairs in a batch (\S\ref{sec:bcs_controlled}). An alternative definition takes the \emph{maximum} pairwise SCS within each batch to capture the single most confusable pair. Here we compare both aggregation methods to verify that core conclusions are robust to this choice.
327	
328	\begin{table}[h]
329	\centering
330	\small
331	\resizebox{\columnwidth}{!}{%
332	\begin{tabular}{llcccc}
333	\toprule
334	\textbf{Aggregation} & \textbf{Condition} & \textbf{Slope} & \textbf{95\% CI} & \textbf{$r$} & \textbf{$p$} \\
335	\midrule
336	MEAN (primary) & 16-rel & $-$0.509 & [$-$0.686, $-$0.336] & $-$0.467 & ${<}\,0.001$ \\
337	MEAN & 80-pool 16-sub & $-$0.401 & [$-$0.701, $-$0.069] & $-$0.221 & 0.027 \\
338	\midrule
339	MAX & 16-rel & $-$0.449 & [$-$0.552, $-$0.346] & $-$0.637 & ${<}\,0.001$ \\
340	MAX & 80-pool 16-sub & $-$0.401 & [$-$0.701, $-$0.069] & $-$0.221 & 0.027 \\
341	\bottomrule
342	\end{tabular}}
343	\caption{BCS--accuracy regression under mean vs.\ max pairwise SCS aggregation (FewRel, 16-relation batches). Permutation test for slope equivalence across pools: MEAN $p \approx 0.60$; MAX $p \approx 0.44$. The 80-pool row is identical under both definitions because these batches were collected using mean-aggregated BCS; the MAX column reflects the same data for completeness.}
344	\label{tab:bcs_aggregation}
345	\end{table}
346	
347	MAX aggregation yields stronger correlations ($r = -0.637$ vs.\ $-0.467$ for 16-rel), consistent with the hypothesis that the single most confusable pair in a batch predicts substitution errors. Both definitions produce significant negative slopes across all conditions, and the permutation tests confirm no significant difference between independent and sampled pools under either definition. We adopt MEAN as the primary definition because it better represents average pairwise difficulty across all schema combinations, while MAX may overweight a single outlier pair. The choice does not affect any paper conclusion.
348	
349	\section{BCS-Controlled Detailed Results}
350	\label{app:bcs-controlled-table}
351	
352	\begin{table}[h]
353	\centering
354	\small
355	\resizebox{\columnwidth}{!}{%
356	\begin{tabular}{lcrrrr}
357	\toprule
358	\textbf{Schema} & \textbf{Count} & \textbf{Low-BCS} & \textbf{High-BCS} & \textbf{$\Delta$ (pp)} & \textbf{95\% CI} \\
359	\midrule
360	16-rel & 8 & 88.9\% & 79.8\% & $-$9.1 & --- \\
361	80-rel & 8 & 82.3\% & 51.0\% & $-$31.2 & {[}17.7, 42.7{]} \\
362	80-rel & 16 & 82.8\% & 51.6\% & $-$31.2 & {[}22.9, 39.6{]} \\
363	\bottomrule
364	\end{tabular}}
365	\caption{BCS-controlled FewRel accuracy. Low-BCS batches contain maximally dissimilar types; high-BCS batches contain maximally similar types. The 80-relation extreme-batch gap reflects the wider BCS range; regression slopes are consistent across pools ($p = 0.60$; Table~\ref{tab:within_pool}; see \S\ref{sec:practical_magnitude} for typical-batch magnitudes). The 16-relation condition used a single extreme batch per BCS level; bootstrap CIs require multiple batches.}
366	\label{tab:bcs_controlled}
367	\end{table}
368	
369	\paragraph{Adjusted $R^2$ and confidence intervals.}
370	DocRED regressions (\S\ref{sec:bcs_controlled}) use OLS on $n = 35$ batches (5 high-BCS + 5 low-BCS + 25 random) with one predictor. At count 16, adjusted $R^2 = 0.511$ (unadjusted: 0.525; 95\% CI via Fisher $z$-transformation: [0.27, 0.73]); at count 32, adjusted $R^2 = 0.426$ (unadjusted: 0.443; CI: [0.18, 0.67]). The small shrinkage ($\Delta R^2 \leq 0.02$) indicates the unadjusted values are not inflated by the predictor-to-sample ratio.
371	
372	\section{Within-Pool Analysis Methodology}
373	\label{app:within-pool-method}
374	
375	A potential confound in the cross-scale comparison is that the 16-relation and 80-relation pools contain different types, so the observed gap could reflect pool composition rather than confusability. To control for this, we draw 100 random 16-relation subsets from the 80-relation pool and evaluate under the same BCS-controlled protocol.
376	
377	\begin{table}[h]
378	\centering
379	\small
380	\resizebox{\columnwidth}{!}{%
381	\begin{tabular}{lrrrrrrr}
382	\toprule
383	& \multicolumn{4}{c}{\textbf{Regression (BCS $\to$ Accuracy)}} & \multicolumn{2}{c}{\textbf{Quartile $\Delta$}} \\
384	\cmidrule(lr){2-5} \cmidrule(lr){6-7}
385	\textbf{Setting} & \textbf{Slope} & \textbf{95\% CI} & \textbf{$r$} & \textbf{$p$} & \textbf{$\Delta$ (pp)} & \textbf{95\% CI} \\
386	\midrule
387	Independent 16-rel ($n{=}100$) & $-$0.509 & [$-$0.686, $-$0.336] & $-$0.467 & ${<}\,0.001$ & $-$5.31 & [$-$7.44, $-$3.19] \\
388	80-pool $\to$ 16-sub ($n{=}100$) & $-$0.401 & [$-$0.701, $-$0.069] & $-$0.221 & $0.027$ & $-$3.92 & [$-$8.17, $+$0.38] \\
389	Full 80-rel ($n{=}25$)$^\dagger$ & $+$0.221 & [$-$1.303, $+$1.695] & $+$0.064 & $0.76$ & $-$1.04 & [$-$10.12, $+$8.04] \\
390	\midrule
391	\multicolumn{7}{l}{\footnotesize Permutation test (16-rel vs.\ 80-pool slopes): $p \approx 0.60$ (5{,}000 permutations)} \\
392	\multicolumn{7}{l}{\footnotesize $^\dagger$BCS range (IQR\,=\,0.033) insufficient for regression; slope not interpretable.} \\
393	\bottomrule
394	\end{tabular}}
395	\caption{Three-way BCS--accuracy analysis on FewRel. Slope: OLS of batch accuracy on BCS (bootstrap CIs, $B{=}10{,}000$). $\Delta$: accuracy gap between top- and bottom-quartile BCS batches. See Appendix~\ref{sec:appendix_within_pool} for CI interpretation.}
396	\label{tab:within_pool}
397	\end{table}
398	
399	The within-pool slope ($-$0.401, CI excludes zero) is statistically indistinguishable from the independent 16-relation pool ($-$0.509; permutation $p \approx 0.60$). The smaller quartile gap ($-$3.92\,pp vs.\ $-$5.31\,pp) reflects the narrower BCS range within the 80-relation pool (Appendix~\ref{sec:appendix_within_pool}).
400	
401	In the full 80-relation condition, natural BCS variation is insufficient (IQR${}=0.033$) to yield a detectable effect ($n=25$, slope${}=+0.221$, $p \approx 0.76$). This does not invalidate the confusability effect; the within-pool slope is significant ($p=0.027$) when BCS is deliberately varied, but establishes that natural schema sampling at this scale does not produce sufficient BCS contrast for detection.
402	
403	\section{SCS Embedding Ablation: Name-Only vs. Name+Definition}
404	\label{app:scs-ablation}
405	
406	Table~\ref{tab:scs-ablation} compares predictive accuracy of name-only SCS against name+definition SCS across three datasets.
407	
408	\begin{table}[h]
409	\centering
410	\small
411	\resizebox{\columnwidth}{!}{\begin{tabular}{lcccc}
412	\toprule
413	Dataset & SCS$_\text{name}$ $r$ & SCS$_\text{def}$ $r$ & $\Delta r$ & Matrix corr. \\
414	\midrule
415	Few-NERD & 0.172 & 0.149 & $-$0.023 & 0.894 \\
416	MAVEN & 0.129 & 0.164 & +0.035 & 0.656 \\
417	FewRel & 0.178 & 0.193 & +0.015 & 0.848 \\
418	\bottomrule
419	\end{tabular}}
420	\caption{Pearson correlation between SCS and empirical confusion rate. ``Def'' concatenates type name with definition before embedding. All correlations significant ($p < 0.001$). The inconsistent direction of $\Delta r$ indicates that definitions provide no systematic benefit.}
421	\label{tab:scs-ablation}
422	\end{table}
423	
424	Few-NERD is the only dataset whose prompts include type definitions; for MAVEN and FewRel, prompts use type names alone, so name-only SCS directly matches model input. The high matrix correlation (0.66--0.89) confirms that type names capture the dominant semantic structure.
425	
426	\paragraph{Held-out validation.}
427	\label{app:scs-heldout-validation}
428	From the 80-type confusion matrix, we extract the $\binom{16}{2} = 120$ pairs among the 16 validation-origin types (fully disjoint from the 64 training-pool types). The SCS--confusion Spearman correlation remains positive and significant ($\rho = 0.216$, $p = 0.018$), nearly identical to the full 80-type pool ($\rho = 0.218$, $p < 10^{-34}$, $n = 3{,}160$ pairs), ruling out training-set contamination as the driver of the observed relationship.
429	
430	\section{Pair-to-Batch Aggregation Simulation}
431	\label{app:aggregation-sim}
432	
433	The following simulation provides an illustrative explanatory model for how pair-level effects aggregate to batch-level variance. It is not the evidence base for our claims; the observed batch-level $R^2 = 0.218$ (\S\ref{sec:practical_magnitude}) is a direct empirical measurement independent of this simulation.
434	
435	\paragraph{Setup.} We examine whether the pair-level $R^2 \approx 7\%$ (computed over non-zero confusion pairs) can aggregate to the observed batch-level $R^2 \approx 22\%$ via a Monte Carlo simulation. From the FewRel 16-relation experiment, we estimate the inter-pair SCS correlation for pairs sharing a common type ($\rho_\text{SCS} = 0.35$). For batches of $k=8$ types ($\binom{8}{2}=28$ pairs), we simulate 10{,}000 iterations: (1) generate 28 correlated pair-level effects with individual $R^2 = 0.074$; (2) average to obtain batch-level signals; (3) compute batch-level $R^2$.
436	
437	\paragraph{Results.} Simulated batch $R^2 = 0.219$ [95\% CI: 0.092--0.361], matching the observed value of 0.218. The effective amplification factor is $\sim$3$\times$, explained by signal correlation within batches preserving variance while independent noise averages out (effective degrees of freedom $\approx 3.4$, not 28).
438	
439	\paragraph{Unconditional baseline.}
440	When the simulation uses the unconditional pairwise $r^2 = 0.013$ (computed over all type pairs including zero-confusion pairs; Table~\ref{tab:pairwise}), the simulated batch-level $R^2$ drops to $0.044$ [95\% CI: 0.001--0.151], well below the observed $R^2 = 0.218$. The analytical formula confirms: $\text{SNR} \times \text{EF} / (\text{SNR} \times \text{EF} + 1) = 0.042$ with the same effective factor $\text{EF} = 3.35$. This ${\sim}5\times$ gap reflects the dilution from zero-confusion pairs: approximately 89\% of type pairs never exhibit mutual confusion, contributing only noise to the unconditional correlation. The conditional model ($R^2 = 0.074 \to 0.219$) matches the observed value because it isolates the minority of semantically proximate pairs that actually compete during type resolution; BCS predicts batch accuracy through the density of \emph{active} confusable pairs, not uniform contributions from all pairs.
441	
442	\paragraph{Sensitivity to $\rho$.}
443	The inter-pair SCS correlation $\rho = 0.35$ is estimated from pairs sharing a common type. At $\rho = 0.20$ (halved correlation), a parallel simulation yields batch $R^2 \approx 0.22$, still matching the observed value; at $\rho = 0.50$, the correlation structure approaches the positive-definiteness boundary; $\rho = 0.35$ thus sits in a stable regime. The simulation is illustrative; the observed batch $R^2 = 0.218$ is the primary evidence.
444	
445	\section{BCS Independence from Type Composition}
446	\label{app:bcs-composition}
447	
448	FewRel's balanced design (700 instances per type) makes type frequency invariant across batches, ruling out frequency-driven confounding. To test whether BCS captures information beyond type composition effects, we decompose the explained variance in a joint model (accuracy $\sim$ BCS $+$ mean type difficulty), where type difficulty is the per-type solo-baseline accuracy averaged across batch members. On 100 random 8-type batches from the 16-relation pool, the joint model explains $R^2 = 0.704$. Variance decomposition yields: BCS unique $R^2 = 0.259$ (36.8\% of explained variance), composition unique $R^2 = 0.298$ (42.3\%), and shared $R^2 = 0.147$ (20.9\%). The near-orthogonality of predictors (VIF${}\,=\,1.06$, $r(\text{BCS}, \text{difficulty}) = -0.21$) confirms that BCS captures confusability-specific signal rather than a proxy for type difficulty.
449	
450	\section{SCS vs.\ Simple Baselines}
451	\label{app:scs-baselines}
452	
453	\begin{table}[h]
454	\centering
455	\small
456	\resizebox{\columnwidth}{!}{%
457	\begin{tabular}{llrr}
458	\toprule
459	\textbf{Dataset} & \textbf{Metric} & \textbf{Spearman $\rho$} & \textbf{$p$} \\
460	\midrule
461	FewRel & SCS (embedding) & \textbf{0.218} & $2.2 \times 10^{-35}$ \\
462	(3{,}160 pairs) & Same-parent (WordNet) & 0.097 & $5.4 \times 10^{-8}$ \\
463	& WordNet Wu-Palmer & 0.073 & $4.3 \times 10^{-5}$ \\
464	& Levenshtein & 0.016 & 0.363 (n.s.) \\
465	\midrule
466	Few-NERD & SCS (embedding) & \textbf{0.166} & $1.5 \times 10^{-13}$ \\
467	(1{,}953 pairs) & Levenshtein & 0.152 & $1.4 \times 10^{-11}$ \\
468	& Same-parent (prefix) & 0.146 & $7.8 \times 10^{-11}$ \\
469	& WordNet Wu-Palmer & 0.054 & 0.070 (n.s.)$^\dagger$ \\
470	\bottomrule
471	\end{tabular}}
472	\caption{Pairwise confusion prediction: SCS vs.\ simple baselines. Spearman $\rho$ between each metric and the empirical confusion rate. SCS outperforms all baselines on FewRel; the margin is smaller on Few-NERD, where hierarchical naming conventions provide partial signal to string-based metrics. $^\dagger$42\% of pairs lack WordNet coverage.}
473	\label{tab:scs_baselines}
474	\end{table}
475	
476	\section{Split-Origin Covariate Analysis}
477	\label{app:split-origin}
478	
479	FewRel combines 64 train-split and 16 val-split relation types into a single 80-type pool.  Train-origin types show numerically lower accuracy ($-8.8$\,pp, $p = 0.06$; see Limitations), raising the question of whether differential pre-training exposure confounds the BCS--accuracy relationship.  We test this by adding a per-batch \emph{train-origin ratio} (fraction of relation types drawn from the train split) as a covariate in the BCS--accuracy regression.
480	
481	\paragraph{Method.}  Across 213 multi-type batches ($k \geq 2$) from the batch-composition experiment (\S\ref{sec:sdgd}) and the factorial design (\S\ref{sec:bcs_controlled}), we compute $\texttt{train\_origin\_ratio} = n_{\text{train}} / k$ for each batch.  The ratio ranges from 0.40 to 1.00 (mean 0.80, consistent with the 64/80 base rate).  We fit:
482	{\small\begin{equation*}
483	\text{acc} = \beta_0 + \beta_{\text{BCS}} \!\cdot\! \text{BCS} + \beta_{\text{orig}} \!\cdot\! \text{train\_origin\_ratio} + \varepsilon
484	\end{equation*}}
485	
486	\paragraph{Results.}  The BCS partial effect is unchanged after controlling for split-origin: $\beta_{\text{BCS}} = -0.416$, $p < 10^{-16}$ (vs.\ $\beta = -0.412$, $p < 10^{-16}$ without the covariate).  Train-origin ratio is not independently significant ($\beta_{\text{origin}} = -0.057$, $p = 0.245$), and $\Delta R^2 = 0.005$.  The BCS--accuracy relationship is therefore not confounded by differential pre-training exposure at the batch level.
487	
488	Pairwise SCS distributions do not differ significantly between train-origin (64 types, mean\,=\,0.880) and val-origin (16 types, mean\,=\,0.874) subsets (Mann-Whitney $p = 0.754$, Cohen's $d = 0.081$); the train/val split does not introduce systematic confusability bias.
489	
490	\section{Cross-Seed Variance Decomposition}
491	\label{app:variance-decomposition}
492	
493	\begin{table}[h]
494	\centering
495	\small
496	\begin{tabular}{rrrr}
497	\toprule
498	\textbf{Count} & \textbf{Batch SD} & \textbf{Seed SD} & \textbf{Ratio} \\
499	\midrule
500	4 & 0.0889 & 0.0122 & 53.5 \\
501	8 & 0.0820 & 0.0098 & 70.0 \\
502	16 & 0.0626 & 0.0270 & 5.4 \\
503	32 & 0.0462 & 0.0091 & 26.0 \\
504	40 & 0.0421 & 0.0019 & 474.4 \\
505	64 & 0.0245 & 0.0022 & 119.8 \\
506	80 & 0.0001 & 0.0088 & $<$0.1 \\
507	\bottomrule
508	\end{tabular}
509	\caption{Variance decomposition on FewRel (3 seeds $\times$ 25 batches per count level). Batch SD: root-mean intra-seed variance averaged over seeds. Seed SD: standard deviation of per-seed means. Ratio = batch variance / seed variance. At count 80, only one batch composition exists, so batch variance vanishes by construction.}
510	\label{tab:variance_decomposition}
511	\end{table}
512	
513	Intra-batch variance dominates inter-seed variance by 5--474$\times$ across count levels 4--64 (mean 125$\times$); random batch composition is the primary source of performance variability. Under greedy decoding (temperature${}\,=\,0$), model inference is nearly deterministic; the inter-seed variance reflects differences in which random batch compositions each seed generates, not inference stochasticity. At count 80, the full schema admits only one composition, leaving residual model-level noise as the sole variance source (seed SD = 0.88\,pp, likely attributable to FP8 quantization non-determinism).
514	
515	\section{Cross-Domain Connections}
516	\label{app:cross-domain}
517	
518	The schema-associated degradation documented here is not unique to information extraction. Schema-Guided Dialogue systems (SGD/SGD-X; \citealt{rastogi2020towards}) face an analogous challenge: as the number of intent and slot types grows, dialogue state tracking accuracy declines. \citet{li2023evaluating} observed count-dependent degradation in ChatGPT-based IE, attributing it to prompt overload. Our two-dimensional decomposition offers a more refined explanation: schema size per se is not the sole predictor; rather, larger schemas increase the probability of including high-SCS pairs, which contribute disproportionately to confusion. This distinction has practical implications: a schema of 80 types with low mutual confusability may outperform a 40-type schema with clustered semantics, and suggests that confusability-aware design principles may generalize to any task where an LLM must discriminate among a prompt-specified label inventory.
519	
520	\section{Cross-Model Validation with LLaMA-3.1-70B-Instruct (FP8)}
521	\label{sec:appendix_cross_model_70b}
522	
523	To test whether the two-dimensional degradation pattern generalizes across model families, we replicate the count-curve and BCS-controlled experiments on Meta-LLaMA-3.1-70B-Instruct (FP8 quantization). All batch compositions, type pools, and test samples are identical to those used for Qwen3-32B (\S\ref{sec:count_curves}, \S\ref{sec:bcs_controlled}).
524	
525	\begin{table}[h]
526	\centering
527	\small
528	\begin{tabular}{lrr}
529	\toprule
530	\textbf{Count} & \textbf{LLaMA-70B} & \textbf{Qwen3-32B} \\
531	\midrule
532	\multicolumn{3}{l}{\textit{RE (FewRel, Classification Accuracy)}} \\
533	8  & 0.757 & 0.805 \\
534	16 & 0.685 & 0.719 \\
535	32 & 0.601 & 0.652 \\
536	64 & 0.504 & 0.539 \\
537	80 & 0.450 & 0.504 \\
538	\midrule
539	\multicolumn{3}{l}{\textit{NER (Few-NERD, Text+Type Match Recall)}} \\
540	2  & 0.323 & 0.515 \\
541	6  & 0.300 & 0.399 \\
542	12 & 0.278 & 0.318 \\
543	22 & 0.252 & 0.279 \\
544	44 & 0.297 & 0.309 \\
545	66 & 0.273 & 0.407 \\
546	\bottomrule
547	\end{tabular}
548	\caption{Cross-model count curves for LLaMA-3.1-70B-Instruct (FP8) and Qwen3-32B. RE decline (count 8$\to$80): $-$30.7\,pp (70B) vs.\ $-$30.1\,pp (32B). NER decline (count 2$\to$22): $-$7.1\,pp (70B) vs.\ $-$23.6\,pp (32B); both models exhibit a U-shaped rebound at higher counts. 25 batches per count level, same samples and batch compositions across models (seed 42). All metrics are micro-averaged across batches.}
549	\label{tab:cross_model_70b}
550	\end{table}
551	
552	Table~\ref{tab:cross_model_70b} shows that RE degradation slopes are near-identical: $-$30.7\,pp (70B) versus $-$30.1\,pp (32B) from count 8 to count 80, with the 70B model approximately 4\,pp lower in absolute accuracy at each count level. This quantitative match provides strong evidence that Dimension~1 (count-related decline) is directionally consistent across architectures for RE.
553	
554	On NER, the count-related decline direction is consistent across models: both 70B and Qwen3 show a recall decline from count 2 to count 22 (70B: 0.323$\to$0.252, $-$7.1\,pp; Qwen3: 0.515$\to$0.279, $-$23.6\,pp). Both models also exhibit a U-shaped rebound at higher counts (70B: 0.252 at count 22 $\to$ 0.297 at count 44; Qwen3: 0.279 at count 22 $\to$ 0.407 at count 66), which cross-validates the U-shape phenomenon. The magnitude difference reflects a precision-recall tradeoff: 70B operates more conservatively (higher precision, lower recall), while Qwen3 over-predicts (higher recall, lower precision, especially at low counts).
555	
556	For the confusability dimension (Dimension 2), at count 16 on FewRel, LLaMA-70B achieves low-BCS accuracy of 0.708 versus high-BCS accuracy of 0.599 ($\Delta = +10.9$\,pp, 95\% CI: [$+$3.0, $+$20.1]). The confidence interval excludes zero; the confusability effect is thus confirmed at the 70B scale.
557	
558	In summary, FewRel RE provides a quantitative match across models (near-identical slopes for Dimension~1 and a significant Dimension~2 effect). NER provides directional consistency: the count-related decline direction is preserved and the U-shaped rebound replicates, though magnitudes vary with each model's precision-recall operating point. Together, these results indicate that the degradation pattern is directionally consistent across architectures.
559	
560	\section{Cross-Model Validation with Gemini 2.5 Flash (API)}
561	\label{sec:appendix_cross_model_gemini}
562	
563	We further validate Dimension~1 on a proprietary model, Gemini 2.5 Flash \citep{gemini-2025}, accessed via API. This extends the cross-model evidence from open-weight families (Qwen, LLaMA) to a proprietary architecture with unknown training details. We replicate the FewRel count-curve experiment using the same 960 balanced samples, batch compositions, and evaluation protocol as Qwen3-32B.
564	
565	\begin{table}[h]
566	\centering
567	\small
568	\begin{tabular}{lrr}
569	\toprule
570	\textbf{Count} & \textbf{Gemini Flash} & \textbf{Qwen3-32B} \\
571	\midrule
572	1  & 0.827 & --- \\
573	4  & 0.873 & 0.870 \\
574	8  & 0.820 & 0.805 \\
575	16 & 0.787 & 0.719 \\
576	32 & 0.739 & 0.652 \\
577	64$^\dagger$ & 0.637 & 0.539 \\
578	\bottomrule
579	\end{tabular}
580	\caption{Cross-model count curves for Gemini 2.5 Flash (API) and Qwen3-32B on FewRel RE (classification accuracy). 25 batches per count level, same samples and batch compositions (seed 42). Gemini's count-1 result is included for completeness; Qwen3 count-1 was not collected. Both models show monotonic decline from count 4 onward ($\rho = -1.0$ for both on counts 4--32). $^\dagger$Count 64: Gemini based on 11/25 batches (partial).}
581	\label{tab:cross_model_gemini}
582	\end{table}
583	
584	Table~\ref{tab:cross_model_gemini} confirms that the count-related accuracy decline replicates on Gemini 2.5 Flash. From count 4 to count 32, both models show perfectly monotonic decline (Spearman $\rho = -1.0$). Including count 1, the Gemini count curve yields $\rho = -0.900$ ($p = 0.037$); including partial count-64 data (11/25 batches), $\rho = -0.943$ ($p = 0.005$). The decline magnitude is smaller for Gemini ($-$13.3\,pp from count 4 to 32) than for Qwen3 ($-$21.8\,pp), consistent with Gemini's higher absolute accuracy providing more headroom before degradation saturates. At each count level, Gemini matches or exceeds Qwen3, with the gap widening at higher counts (0.3\,pp at count 4 vs.\ 8.7\,pp at count 32, 9.8\,pp at partial count 64); Gemini appears more robust to schema scaling but not immune. Dimension~2 (BCS-controlled confusability) has not been tested on proprietary models; cross-architecture Dimension~2 validation remains for future work.
585	
586	\section{Few-Shot Prompting and Confusability}
587	\label{sec:appendix_fewshot_bcs}
588	
589	To test whether in-context demonstrations mitigate the BCS-associated confusability effect, we evaluate 0-shot, 1-shot, and 5-shot prompting on FewRel 80-relation RE at count 8 using the same extreme-BCS batch design as \S\ref{sec:bcs_controlled}. Each condition uses 50 batches (25 low-BCS, mean $\approx 0.36$; 25 high-BCS, mean $\approx 0.80$), drawn from the pre-constructed batch pool of \S\ref{sec:bcs_controlled}. Few-shot examples are sampled from the FewRel training split for each target type.
590	
591	\begin{table}[h]
592	\centering
593	\small
594	\resizebox{\columnwidth}{!}{\begin{tabular}{lrrrl}
595	\toprule
596	\textbf{Condition} & \textbf{Low-BCS} & \textbf{High-BCS} & \textbf{$\Delta$ (pp)} & \textbf{95\% CI} \\
597	\midrule
598	0-shot & 0.682 & 0.498 & +18.5 & {[}+14.3, +22.7{]} \\
599	1-shot & 0.754 & 0.554 & +20.0 & {[}+16.3, +23.5{]} \\
600	5-shot & 0.715 & 0.488 & +22.8 & {[}+18.9, +26.8{]} \\
601	\bottomrule
602	\end{tabular}}
603	\caption{BCS gap under few-shot prompting (FewRel, count 8). Demonstrations improve absolute accuracy on low-BCS batches (+3.3--7.2\,pp over 0-shot) but provide inconsistent benefit on high-BCS batches (+5.6\,pp at 1-shot, $-$1.0\,pp at 5-shot). The confusability gap widens from +18.5\,pp (0-shot) to +22.8\,pp (5-shot). All metrics are micro-averaged across batches.}
604	\label{tab:fewshot_bcs}
605	\end{table}
606	
607	Demonstrations improve absolute accuracy primarily on low-BCS (easy) batches, where type boundaries are already distinct and examples reinforce correct mappings. On high-BCS batches, where types are semantically confusable, demonstrations provide inconsistent benefit (+5.6\,pp at 1-shot, $-$1.0\,pp at 5-shot): the model still substitutes similar types at comparable rates. The net effect is that the confusability gap widens under few-shot prompting (+4.3\,pp from 0-shot to 5-shot, bootstrap $p = 0.014$), with all three confidence intervals excluding zero. This indicates that BCS-associated type confusion is a structural property of the schema composition rather than a deficit addressable through prompt engineering. The non-monotonic low-BCS pattern (0.754 at 1-shot vs.\ 0.715 at 5-shot) may reflect lost-in-middle effects from increased prompt length \cite{lost-in-middle-2024}.
608	
609	The 0-shot gap (+18.5\,pp) is smaller than the extreme-batch gap reported in \S\ref{sec:bcs_controlled} (+25.5\,pp) because the two experiments use different test splits and batch sampling seeds; direct magnitude comparison across experiments is not appropriate.
610	
611	\section{Qualitative Error Analysis}
612	\label{app:error-analysis}
613	
614	Tables~\ref{tab:top10_re} and~\ref{tab:top10_ner} list the ten most frequently confused type pairs on FewRel 80-relation RE and Few-NERD NER. Confusion counts are aggregated bidirectionally across three random seeds (72{,}000 predictions per seed for RE; single-seed 66-type extraction for NER).
615	
616	\begin{table}[h]
617	\centering
618	\footnotesize
619	\begin{tabular}{clllr}
620	\toprule
621	\textbf{\#} & \textbf{Type A} & \textbf{Type B} & \textbf{SCS} & \textbf{$N$} \\
622	\midrule
623	1 & instance of & taxon rank & 0.53 & 875 \\
624	2 & child & father & 0.84 & 700 \\
625	3 & participant of & participating team & 0.75 & 675 \\
626	4 & mountain range & part of & 0.57 & 575 \\
627	5 & mouth of watercourse & tributary & 0.65 & 549 \\
628	6 & child & mother & 0.84 & 500 \\
629	7 & league & member of & 0.66 & 450 \\
630	8 & country of citizenship & country of origin & 0.76 & 400 \\
631	9 & followed by & follows & 0.90 & 400 \\
632	10 & occupation & voice type & 0.57 & 400 \\
633	\bottomrule
634	\end{tabular}
635	\caption{Top-10 confused relation pairs on FewRel 80-relation RE. $N$: bidirectional confusion count aggregated over 3 seeds $\times$ 25 batches. SCS: pairwise Schema Confusability Score (Qwen3 embedding cosine similarity). High-SCS pairs (e.g., \textit{followed by}/\textit{follows}, SCS\,=\,0.90) and family-relation pairs (\textit{child}/\textit{father}, \textit{child}/\textit{mother}) dominate. Some low-SCS pairs (\textit{instance of}/\textit{taxon rank}, SCS\,=\,0.53) reflect domain-specific co-occurrence rather than semantic similarity.}
636	\label{tab:top10_re}
637	\end{table}
638	
639	\begin{table}[h]
640	\centering
641	\footnotesize
642	\begin{tabular}{clllr}
643	\toprule
644	\textbf{\#} & \textbf{Type A} & \textbf{Type B} & \textbf{SCS} & \textbf{$N$} \\
645	\midrule
646	1 & person-other & person-politician & 0.93 & 121 \\
647	2 & location-GPE & organization-other & 0.83 & 81 \\
648	3 & art-film & location-GPE & 0.69 & 57 \\
649	4 & building-other & location-GPE & 0.85 & 56 \\
650	5 & building-other & person-other & 0.90 & 43 \\
651	6 & location-GPE & product-other & 0.69 & 39 \\
652	7 & org-gov/agency & person-other & 0.85 & 34 \\
653	8 & person-actor & person-other & 0.90 & 34 \\
654	9 & building-other & location-road/transit & 0.76 & 32 \\
655	10 & location-GPE & org-sportsleague & 0.81 & 30 \\
656	\bottomrule
657	\end{tabular}
658	\caption{Top-10 confused entity type pairs on Few-NERD NER. $N$: bidirectional confusion count from 66-type full-schema extraction. SCS: pairwise Schema Confusability Score (Qwen3 embedding cosine similarity). Intra-category confusions (e.g., \textit{person-other}/\textit{person-politician}, SCS\,=\,0.93) and cross-category pairs sharing referent overlap (\textit{building-other}/\textit{location-GPE}, SCS\,=\,0.85) are most frequent. The ``other'' subtypes absorb diverse entities and confuse with more specific siblings.}
659	\label{tab:top10_ner}
660	\end{table}
661	
662	\paragraph{Illustrative error instances.}
663	Table~\ref{tab:error_examples} shows three FewRel instances where the model predicted a semantically adjacent relation. All gold-predicted pairs have SCS\,$>$\,0.90.
664	
665	\begin{table}[h]
666	\centering
667	\footnotesize
668	\resizebox{\columnwidth}{!}{%
669	\begin{tabular}{p{5.8cm}llc}
670	\toprule
671	\textbf{Sentence (abridged)} & \textbf{Gold} & \textbf{Predicted} & \textbf{SCS} \\
672	\midrule
673	Over five EuroLeague games he played for \textbf{Valencia}, he averaged 8 points \ldots\  [\textbf{EuroLeague}, \textbf{Valencia}] & participant & participant of & 0.97 \\
674	\addlinespace
675	\textbf{Pilões} is a municipality in the state of \textbf{Rio Grande do Norte} in the Northeast region of Brazil. & contains admin.\ terr.\ entity & located in admin.\ terr.\ entity & 0.92 \\
676	\addlinespace
677	In May 1997 Davies was appointed \ldots\ to the \textbf{Cabinet} as \textbf{Secretary of State for Wales}. & part of & member of & 0.90 \\
678	\bottomrule
679	\end{tabular}}
680	\caption{Representative confusion instances from FewRel 80-relation RE (Qwen3-32B, count\,=\,80). Head and tail entities are bolded. In each case, the gold and predicted relations are semantically close (SCS\,$>$\,0.90): \textit{participant} vs.\ \textit{participant of} reverses argument directionality; \textit{contains} vs.\ \textit{located in} inverts the containment relation; \textit{part of} vs.\ \textit{member of} conflates meronymy with membership. These confusions are consistent with the pairwise SCS--confusion correlation reported in \S\ref{sec:pairwise}.}
681	\label{tab:error_examples}
682	\end{table}
683	
684	\section{Schema Label Renaming Experiment}
685	\label{app:renaming}
686	
687	To test whether reducing pairwise SCS through label renaming improves accuracy, we conducted a controlled intervention on FewRel 80-relation RE (count 8, Qwen3-32B). We identified 14 high-SCS relation pairs (covering 12 unique relation types, as two types each appear in multiple pairs; mean SCS = 0.87) and replaced one label in each pair with a semantically distinct paraphrase chosen to minimize embedding cosine similarity (all-MiniLM-L6-v2). Examples: \textit{participant of} $\to$ \textit{event involvement} (SCS: 0.97 $\to$ 0.72), \textit{follows} $\to$ \textit{prior entry} (0.90 $\to$ 0.69), \textit{part of} $\to$ \textit{integral segment of} (0.90 $\to$ 0.64). The renaming reduced mean pairwise SCS from 0.87 to 0.67 ($\Delta = -0.20$). We ran the same 50 BCS-controlled batches (25 low-BCS, 25 high-BCS; 96 samples each) under both original (control) and renamed (treatment) label sets.
688	
689	\begin{table}[h]
690	\centering
691	\small
692	\begin{tabular}{lccc}
693	\toprule
694	& \textbf{Control} & \textbf{Treatment} & \textbf{$\Delta$\,(pp)} \\
695	\midrule
696	Low-BCS ($n=25$)  & 90.1 & 87.1 & $-$3.0 \\
697	High-BCS ($n=25$) & 69.3 & 60.5 & $-$8.8 \\
698	\bottomrule
699	\end{tabular}
700	\caption{Accuracy (\%) under original vs.\ renamed labels on FewRel count-8 batches. Renaming reduced embedding similarity but decreased accuracy in both groups, with a larger drop on high-BCS batches (Cohen's $d = -2.92$) than low-BCS ($d = -1.09$). Interaction: $\Delta_{\text{high}} - \Delta_{\text{low}} = -5.9$\,pp ($t = -7.23$, $p < 0.001$).}
701	\label{tab:renaming}
702	\end{table}
703	
704	Renaming hurt accuracy uniformly: both groups showed significant declines (paired $t$-test, both $p < 0.001$). The number of renamed types per batch correlated negatively with accuracy change ($r = -0.625$, $p < 0.001$). A solo sanity check confirmed that 11 of 12 renamed labels were individually recognizable (accuracy $\geq$ original $-5$\,pp). The results indicate that replacing familiar Wikidata labels with unfamiliar paraphrases disrupts the model's type semantics; this label unfamiliarity effect outweighs any benefit from reduced confusability.
705	
706	\end{document}
707	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "da49144f-ceab-4df6-b939-2b30013b573e",
  "isSidechain": false,
  "promptId": "8257bd0e-08b4-4530-aa87-1e185ea40a51",
  "type": "user",
  "uuid": "49ad9356-8430-42cc-b714-b59903efd3e1",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex",
      "content": "\\documentclass[11pt]{article}\n\n\\usepackage[review]{acl}\n\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage[T1]{fontenc}\n\\usepackage[utf8]{inputenc}\n\\usepackage{microtype}\n\\usepackage{graphicx}\n\\usepackage{booktabs}\n\\usepackage{amsmath}\n\\usepackage{enumitem}\n\\usepackage[normalem]{ulem}\n\\usepackage{listings}\n\n\\title{How Does Schema Complexity Predict Performance\\\\in Training-Free LLM Information Extraction?}\n\n\\author{Anonymous}\n\n\\begin{document}\n\\maketitle\n\n\\input{abstract}\n\n\\input{introduction}\n\n\\input{related_work}\n\n\\input{experimental_setup}\n\n\\input{results}\n\n\\input{sdgd_negative}\n\n\\input{discussion}\n\n\\section*{Limitations}\n\\begin{enumerate}[leftmargin=*,itemsep=2pt]\n\\item \\textbf{Model coverage.} Primary experiments use Qwen3-32B with cross-model validation on Llama-3.1-8B, 70B-Instruct (FP8), and Gemini 2.5 Flash (API). Dimension~1 has been validated across all four models including a proprietary one; Dimension~2 has been verified only on open-weight models and was not robustly detectable on NER at 8B scale, likely due to floor effects.\n\n\\item \\textbf{Effect size and statistical design.} Pairwise SCS explains 1.3--1.7\\% of type confusion variance; entity frequency, prompt position, and mention ambiguity likely account for the remainder. The count $\\times$ BCS interaction is bounded under the linear specification (TOST $p = 0.003$ at $\\pm 3$\\,pp on FewRel; DocRED inconclusive, Appendix~\\ref{sec:appendix_factorial}) but inconclusive on the logit scale ($p = 0.209$). BCS-controlled experiments use a single seed with greedy decoding; the residual SD of 0.88\\,pp (Appendix~\\ref{app:variance-decomposition}) supports robustness but precise magnitudes may vary.\n\n\\item \\textbf{Task format dependency.} BCS batch-level prediction is demonstrated only under RE's forced-choice classification format. An unconstrained decoding ablation ($n = 25$) confirms this: removing the enum constraint eliminates the BCS--accuracy correlation ($\\rho = -0.14$, $p = 0.49$), establishing that the batch-level signal is specific to forced-choice RE. NER exact-match evaluation conflates boundary and type errors, and relaxed matching may yield different confusability effect sizes.\n\n\\item \\textbf{Causal mechanism.} The study establishes correlational evidence with controlled stratification; mechanistic analysis at the attention or logit level is needed to confirm the causal pathway. A post-hoc renaming experiment (Appendix~\\ref{app:renaming}) confirms this concern: replacing high-SCS labels with semantically distinct paraphrases reduced pairwise embedding similarity but decreased accuracy by 3--9\\,pp, as label unfamiliarity introduced errors that outweighed any confusability reduction.\n\n\\item \\textbf{Data contamination.} FewRel (2018) may appear in pretraining corpora, but train-origin relations show numerically lower accuracy than val-origin ($-8.8$\\,pp, n.s.), opposite to the contamination hypothesis. DocRED (2019) provides a lower-contamination-risk replication with consistent slopes ($R^2 = 0.53$; Appendix~\\ref{app:split-origin}).\n\\end{enumerate}\n\n\\paragraph{Multiple comparisons.} Cross-dataset comparisons serve as independent replications and do not require family-wise correction \\citep{rothman-1990}. Within-dataset secondary analyses involve multiple looks; we report individual $p$-values and note that core claims rest on $p < 0.001$ \\citep{dror-2018-significance,card-2020-power}.\n\n\\input{checklist}\n\n\\bibliography{references}\n\n\\appendix\n\n\\section{Additional Figures}\n\\label{sec:appendix_figures}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{lrr}\n\\toprule\n\\textbf{Count} & \\textbf{Llama-3.1-8B} & \\textbf{Qwen3-32B} \\\\\n\\midrule\n1 & 0.702 & 0.640 \\\\\n64 & 0.273 & 0.304 \\\\\n\\midrule\nDecline & $-$43\\,pp & $-$34\\,pp \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Cross-model count-curve replication on Few-NERD (text-match recall). Both models show a general declining trend in recall with schema size. Per-batch correlation $r = 0.725$. Qwen3-32B values use the v2 prompt (\\S\\ref{sec:model}) for fair cross-model comparison; the count-curve results in \\S\\ref{sec:count_curves} use the v1 prompt, yielding higher absolute recall (0.72 vs.\\ 0.64 at count${}\\,=\\,1$) due to over-prediction under v1.}\n\\label{tab:cross_model}\n\\end{table}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{crrrrrr}\n\\toprule\n& \\multicolumn{3}{c}{\\textbf{Llama-3.1-8B}} & \\multicolumn{3}{c}{\\textbf{Qwen3-32B}} \\\\\n\\cmidrule(lr){2-4} \\cmidrule(lr){5-7}\n\\textbf{Count} & \\textbf{Low} & \\textbf{High} & \\textbf{$\\Delta$} & \\textbf{Low} & \\textbf{High} & \\textbf{$\\Delta$} \\\\\n\\midrule\n8 & 78.1\\% & 51.0\\% & $-$27.1 & 82.3\\% & 51.0\\% & $-$31.2 \\\\\n16 & 75.5\\% & 51.6\\% & $-$23.9 & 82.8\\% & 51.6\\% & $-$31.2 \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Cross-model BCS-controlled FewRel accuracy.  High-BCS accuracy converges to $\\approx$51\\% regardless of model, while low-BCS accuracy reflects model capacity differences.  The confusability gap ($\\Delta$, in pp) is 77--87\\% as large on Llama-3.1-8B as on Qwen3-32B.}\n\\label{tab:cross_model_bcs}\n\\end{table}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llrrrrrrr}\n\\toprule\n & & \\multicolumn{5}{c}{\\textbf{BCS Bin}} & & \\\\\n\\cmidrule(lr){3-7}\n\\textbf{Task} & \\textbf{Error} & \\textbf{Solo} & \\textbf{Low} & \\textbf{Mid} & \\textbf{High} & \\textbf{V.High} & \\textbf{$\\rho$} & \\textbf{$p$} \\\\\n\\midrule\nNER & IntraSub & 0\\% & 1.6\\% & 10.6\\% & 49.4\\% & --- & 1.000 & ${<}0.001$ \\\\\nRE  & IntraSub & 0\\% & 4.2\\% & 13.0\\% & 20.3\\% & 32.3\\% & 0.954 & ${<}\\,0.001$ \\\\\n\\midrule\nNER & Missed & --- & 42.8\\% & 64.8\\% & 49.9\\% & --- & --- & --- \\\\\nRE  & Missed & --- & 10.4\\% & 11.3\\% & 13.1\\% & 15.7\\% & --- & --- \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Intra-batch substitution (IntraSub) and missed-entity rates by BCS bin, with Spearman $\\rho$ computed over $n=154$ individual batches (RE) and $n=148$ batches (NER). NER has 4 BCS bins; RE has 5.}\n\\label{tab:error_taxonomy}\n\\end{table}\n\n\\section{SDGD Full Protocol and Results}\n\\label{sec:appendix_sdgd}\n\nWe construct a thresholded confusability graph $G = (V, E)$ where each type is a vertex and an edge connects types $t_i, t_j$ whenever $\\text{SCS}(t_i, t_j) > \\tau$. Greedy graph coloring (\\textsc{largest\\_first}) assigns each type to a color such that no two adjacent (i.e., highly confusable) types share a color. Each color class forms one extraction batch, and predictions are merged via set union. We compare four modes: (i)~\\textbf{single\\_pass}, the undecomposed baseline; (ii)~\\textbf{sdgd\\_zero}, SCS-guided partitioning; (iii)~\\textbf{random\\_batch}, random partitioning with matched batch sizes; and (iv)~\\textbf{per\\_type}, the extreme case where each type is extracted in isolation.\n\nSingle-pass extraction achieves F1\\,=\\,0.445 (P\\,=\\,0.563, R\\,=\\,0.368). SDGD obtains F1\\,=\\,0.251 (P\\,=\\,0.210, R\\,=\\,0.314), a 44\\% relative drop. Random batching reaches F1\\,=\\,0.320 (P\\,=\\,0.249, R\\,=\\,0.446), and per-type extraction yields F1\\,=\\,0.292 (P\\,=\\,0.194, R\\,=\\,0.586). Every decomposition mode falls below the single-pass baseline (Table~\\ref{tab:sdgd_results}).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lrccc}\n\\toprule\n\\textbf{Mode} & \\textbf{\\# Batches} & \\textbf{Precision} & \\textbf{Recall} & \\textbf{F1} \\\\\n\\midrule\nsingle\\_pass & 1 & 0.563 & 0.368 & 0.445 \\\\\n\\midrule\nsdgd\\_zero (v1) & 8 & 0.210 & 0.314 & 0.251 \\\\\nrandom\\_batch (v1) & 8 & 0.249 & 0.446 & 0.320 \\\\\nper\\_type & 66 & 0.194 & 0.586 & 0.292 \\\\\n\\midrule\nsdgd\\_zero (v2) & 4 & 0.324 & 0.191 & 0.241 \\\\\nrandom\\_batch (v2) & 8 & 0.331 & 0.276 & 0.301 \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Few-NERD extraction under decomposition modes. V1 uses union merge; v2 uses confidence-gated merge with \\texttt{min\\_batch\\_size=8} (reducing 8$\\to$4 batches for sdgd\\_zero). All decomposition modes produce lower F1 than the single-pass baseline. All modes use the v1 prompt.}\n\\label{tab:sdgd_results}\n\\end{table}\n\nDecomposition boosts recall (per-type recall reaches 0.586 versus single-pass 0.368) but devastates precision (0.194 versus 0.563). When the same text is presented to the model $k$ times with different type subsets, each pass independently generates entity predictions. Because LLM outputs are not calibrated across passes, the union merge step accumulates overlapping and contradictory predictions and inflates false positives.\n\nOur v2 merge ranks competing predictions by the LLM's self-reported confidence and retains only the highest-scoring candidate for each span. Confidence gating improves precision (sdgd\\_zero: 0.210$\\to$0.324; random\\_batch: 0.249$\\to$0.331), but at the cost of disproportionate recall loss (0.314$\\to$0.191; 0.446$\\to$0.276), and both modes produce lower F1 (sdgd\\_zero: 0.251$\\to$0.241; random\\_batch: 0.320$\\to$0.301).\n\n\\subsection{Practical Routing Strategies on RE}\n\\label{sec:appendix_routing}\n\nWe evaluate five non-oracle routing strategies on FewRel 80-relation RE using graph-coloring sub-schema decomposition (same grouping as Table~\\ref{tab:batch_composition}). Each strategy selects a single sub-schema for each test instance and returns that sub-schema's prediction.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{\\begin{tabular}{@{}lrr@{}}\n\\toprule\n\\textbf{Strategy} & \\textbf{Accuracy} & \\textbf{$\\Delta$ vs.\\ Single-Pass} \\\\\n\\midrule\nOracle (gold label) & 72.4\\% & +22.0\\,pp \\\\\n\\midrule\nMax-conf (positive only) & 36.5\\% & $-$14.0\\,pp \\\\\nNone-aware & 36.5\\% & $-$14.0\\,pp \\\\\nMargin (positive only) & 35.9\\% & $-$14.5\\,pp \\\\\nMax-conf (all) & 27.7\\% & $-$22.7\\,pp \\\\\nRandom & 14.7\\% & $-$35.7\\,pp \\\\\n\\midrule\nSingle-pass (no decomposition) & 50.4\\% & --- \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Routing strategy comparison on FewRel 80-relation RE with graph-coloring sub-schema decomposition. Oracle requires gold labels. All practical (non-oracle) strategies perform below the single-pass baseline. The failure stems from constrained decoding (enum constraint), which forces confident predictions in every sub-schema: 73.4\\% of instances receive positive predictions from 3--5 sub-schemas simultaneously, with per-sub-schema none-rates of only 20--40\\%.}\n\\label{tab:routing_strategies}\n\\end{table}\n\n\\section{Factorial Analysis and Separability Test}\n\\label{sec:appendix_factorial}\n\nTo formally test whether count and confusability effects are additive, we fit a multiple regression (accuracy $\\sim$ $\\log_2$\\,count $+$ BCS $+$ count$\\times$BCS) across 69 batches from FewRel spanning five count levels ($k \\in \\{4, 8, 16, 32, 40\\}$). Both main effects are significant (count: $p = 0.008$; BCS: $p = 0.0002$; $R^2 = 0.52$), but the interaction term is negligible (0.47\\,pp). A TOST equivalence test with a $\\pm 3$\\,pp margin confirms that the interaction is bounded well below practical significance ($p_{\\text{TOST}} = 0.003$); this supports bounded interaction between count and confusability effects.\n\nA $2 \\times 2$ factorial sensitivity check on FewRel (count $\\in \\{8, 16\\}$, BCS low/high; $n = 54$) was inconclusive ($p_{\\text{TOST}} = 0.56$) due to limited power; this does not contradict the primary finding but limits generalization beyond the regression framework. The Few-NERD factorial (\\S\\ref{sec:multi_channel}) similarly did not reach significance ($p = 0.50$). The regression approach provides the stronger test by leveraging the full count range.\n\n\\paragraph{Equivalence margin justification.}\nWe set the $\\pm 3$\\,pp margin based on three converging anchors. \\emph{Empirical}: typical random-batch confusability variation produces 2--5\\,pp accuracy differences (batch SD $\\approx 4.6$\\,pp at count 32). \\emph{Practical}: a ${<}3$\\,pp accuracy difference falls below deployment-relevant thresholds. \\emph{Statistical}: 3\\,pp $\\approx 0.5 \\times$ batch SD, equivalent to Cohen's $d \\approx 0.5$ (medium effect threshold; \\citealt{lakens-2017-equivalence}). A 3\\,pp interaction atop the 2.2\\,pp confusability main effect would represent ${>}130\\%$ amplification, fundamentally changing whether confusability warrants mitigation. At $\\pm 2$\\,pp (marginally equivalent, $p = 0.047$), interaction remains bounded below the main effect itself.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{crrl}\n\\toprule\n\\textbf{Margin (pp)} & \\textbf{$t_{\\text{upper}}$} & \\textbf{$p_{\\text{TOST}}$} & \\textbf{Conclusion} \\\\\n\\midrule\n$\\pm 1$ & $-0.59$ & $0.278$ & Inconclusive \\\\\n$\\pm 2$ & $-1.70$ & $0.047$ & Equivalent \\\\\n$\\pm 3$ & $-2.81$ & $0.003$ & Equivalent \\\\\n$\\pm 5$ & $-5.02$ & ${<}\\,0.001$ & Equivalent \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{TOST sensitivity analysis across equivalence margins. The interaction effect (0.47\\,pp, 90\\% CI [$-$1.0, 2.0]\\,pp) is bounded below 2\\,pp at marginal significance ($p = 0.047$); the $\\pm 3$\\,pp choice does not drive the equivalence conclusion. At $\\pm 1$\\,pp, equivalence is inconclusive ($p = 0.278$), meaning interaction could reach approximately half the main effect magnitude.}\n\\label{tab:tost_sensitivity}\n\\end{table}\n\n\\paragraph{Logit-scale sensitivity.}\nBecause accuracy near 50\\% compresses interaction effects on the linear scale, we refit the regression on logit-transformed accuracy. The logit-scale interaction (0.111 logit units, $p = 0.047$, 90\\% CI [0.019, 0.203]) is marginally significant, and TOST at the equivalent $\\pm 3$\\,pp margin ($\\pm 0.156$ logit at median accuracy) is inconclusive ($p_{\\text{TOST}} = 0.209$). However, back-transforming the interaction to the probability scale at the observed floor ($p = 0.51$) yields 2.78\\,pp, still within the $\\pm 3$\\,pp margin; at the median baseline ($p = 0.65$), the back-transformed effect is 2.53\\,pp. The logit TOST is inconclusive due to limited power ($n = 69$, wide CI) rather than a large effect size: the point estimate remains below the equivalence bound at all observed baselines. We retain the linear-scale TOST as the primary test and report this logit analysis as a sensitivity check.\n\n\\paragraph{DocRED factorial.}\nA $2 \\times 2$ factorial on DocRED (count $\\in \\{16, 32\\}$, BCS median split at 0.55; $n = 70$) yields a larger interaction estimate (+5.7\\,pp, 95\\% CI [$-$1.6, 13.0]): the BCS effect is $-$10.6\\,pp at count 16 but only $-$4.9\\,pp at count 32. TOST at $\\pm 3$\\,pp is not established ($p = 0.77$). The asymmetry likely reflects baseline compression: at count 32, accuracy approaches chance ($\\sim$49\\%), leaving less room for confusability to further reduce performance. We therefore restrict the bounded-interaction conclusion to sentence-level RE.\n\n\\section{Within-Pool CI Details}\n\\label{sec:appendix_within_pool}\n\nThe quartile $\\Delta$ for 80-pool 16-relation subsets ($-$3.92\\,pp, 95\\% CI [$-$8.17, $+$0.38]) crosses zero, reflecting the compressed BCS range within that pool (0.46--0.68 vs.\\ 0.48--0.71 for the independent pool). Within this narrow band, the quartile contrast lacks statistical power to detect the effect that the regression identifies. The full 80-relation condition ($n = 25$) is underpowered for both the slope (CI: [$-$1.303, $+$1.695]) and quartile analyses; we include it in Table~\\ref{tab:within_pool} for completeness but do not draw inferential conclusions from it.\n\n\\section{Controlling for Centrality Confounds in MAVEN Per-Type Analysis}\n\\label{sec:appendix_residualized_bcs}\n\nSection~\\ref{sec:centrality_confound} identifies a centrality confound in MAVEN's per-type BCS--F1 correlation: both embeddings show a \\emph{positive} raw correlation, opposite to the expected direction. Here we formalize this analysis by identifying specific confounders for each embedding and testing whether the BCS--F1 relationship survives partial correlation controlling for these confounders.\n\n\\paragraph{Confound identification.}\nFor each embedding, we computed the correlation between mean BCS and candidate confounders (type frequency, degree centrality at threshold 0.7) across MAVEN's 149 active event types. The dominant confound differs by embedding:\n\\begin{itemize}[itemsep=2pt,leftmargin=*]\n\\item \\textbf{MiniLM}: BCS correlates with log type frequency ($r = 0.201$). Frequent types have more training signal and are extracted more reliably, which produces the positive BCS--F1 association.\n\\item \\textbf{Qwen3}: BCS correlates strongly with degree centrality ($r = 0.854$). In the Qwen3 embedding space, high-BCS types are those with many semantic neighbors, central, well-represented types that the model extracts well.\n\\end{itemize}\n\n\\paragraph{Partial correlation results.}\nTable~\\ref{tab:residualized_bcs} reports raw Spearman $\\rho$ and partial Pearson $r$ after controlling for the identified confounders. Under single-variable control, both correlations weaken to non-significance. Under joint control (log frequency $+$ degree centrality simultaneously), neither embedding retains a significant BCS--F1 association.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llcccc}\n\\toprule\n\\textbf{Embedding} & \\textbf{Control} & \\textbf{Raw $\\rho$} & \\textbf{Raw $p$} & \\textbf{Partial $r$} & \\textbf{Partial $p$} \\\\\n\\midrule\nMiniLM & --- & $+$0.208 & $0.011$ & --- & --- \\\\\nMiniLM & log freq & --- & --- & $+$0.133 & $0.11$ \\\\\nMiniLM & log freq $+$ degree & --- & --- & --- & $0.23$ \\\\\n\\midrule\nQwen3 & --- & $+$0.184 & $0.025$ & --- & --- \\\\\nQwen3 & degree centrality & --- & --- & $+$0.063 & $0.44$ \\\\\nQwen3 & log freq $+$ degree & --- & --- & --- & $0.44$ \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{MAVEN per-type BCS--F1 correlation before and after controlling for centrality confounders. Raw correlations are Spearman $\\rho$; partial correlations are Pearson $r$ from residualized regression. Degree centrality is computed on the SCS graph at threshold 0.7. All values from experiment \\texttt{exp\\_maven\\_residualized\\_bcs}.}\n\\label{tab:residualized_bcs}\n\\end{table}\n\n\\paragraph{Interpretation.}\nThe two embeddings encode different aspects of the same underlying confound. MiniLM, a smaller sentence encoder, produces a tighter embedding cluster for MAVEN's FrameNet-derived types; here, type frequency is the primary confounder because frequent types accumulate higher mean similarity to the dense cluster. Qwen3, with a larger representation space, differentiates types enough that frequency is not the dominant factor, but degree centrality (the count of strong semantic neighbors) becomes the confound instead. In both cases, the positive raw correlation reflects a centrality artifact: types that are semantically central are both high-BCS and easy to extract.\n\nUnder joint control, both embeddings yield $p > 0.2$; the raw positive BCS--F1 correlation on MAVEN is thus fully attributable to centrality-related confounders. This does not invalidate the confusability hypothesis; the pairwise SCS--confusion correlation on MAVEN remains significant (MiniLM $r = 0.129$, $p < 0.001$; Table~\\ref{tab:pairwise}). Rather, it demonstrates that per-type aggregation (mean BCS) conflates confusability with centrality in semantically homogeneous schemas, and that pairwise analysis or explicit confound adjustment is required in such settings.\n\n\\section{Batch Composition Results}\n\\label{sec:appendix_batch_composition}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{@{}lcc@{}}\n\\toprule\n\\textbf{Condition} & \\textbf{Accuracy} & \\textbf{Mean BCS} \\\\\n\\midrule\nSingle-pass (80 types) & 0.504 & 0.557 \\\\\nRandom batching (15 seeds)$^\\dagger$ & 0.788\\,$\\pm$\\,0.018 & 0.559 \\\\\nConfus.-aware (graph coloring) & \\textbf{0.802} & 0.552 \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Batch composition on FewRel 80-relation RE with oracle routing. $^\\dagger$Mean $\\pm$ SD across 15 random seeds.}\n\\label{tab:batch_composition}\n\\end{table}\n\nSee the accompanying discussion in \\S\\ref{sec:sdgd}.\n\n\\input{prompt_appendix}\n\n\\section{Prompt Version Sensitivity Analysis}\n\\label{sec:appendix_prompt_sensitivity}\n\nWe assess whether the confusability effects reported in \\S\\ref{sec:bcs_controlled}--\\ref{sec:multi_channel} are robust to prompt design by replicating key experiments under the v2 prompt (\\S\\ref{sec:model}; full templates in Appendix~\\ref{sec:appendix_prompts}).\n\n\\paragraph{RE (FewRel).}\nUnder the v1 prompt, the extreme-batch BCS gap (Table~\\ref{tab:bcs_controlled}) is substantial. Under v2, with $n{=}25$ batches per group and wider BCS contrast (low-BCS range [0.356, 0.367]; high-BCS range [0.791, 0.811]), the gap is $-$25.5\\,pp (low-BCS 85.2\\% vs.\\ high-BCS 59.7\\%; 95\\% CI: [22.4, 28.6]; $p < 0.001$; Pearson $r = -0.919$). The effect is significant, directionally consistent with v1, and only modestly attenuated in magnitude ($-$5.7\\,pp reduction). An earlier $n{=}5$ evaluation with narrower BCS contrast (0.21) yielded a smaller gap of $-$7.9\\,pp (CI: [$-$5.2, $+$21.5]), illustrating how limited statistical power and restricted BCS range can obscure the underlying signal, a cautionary note for small-sample prompt sensitivity studies.\n\n\\paragraph{NER (Few-NERD).}\nThe batch-level BCS--F1 correlation is null under both prompt versions. Pooling across three seeds and all count levels ($n = 450$), the correlation is $r = 0.004$ ($p = 0.94$). An earlier small-sample analysis ($n = 27$, single seed) had reported positive correlations ($r = +0.50$/$+0.58$), but these were driven by an accidental BCS--type-frequency confound: those 27 batches exhibited $r(\\text{BCS}, \\text{freq}) = 0.53$, creating a spurious path through frequency to F1. After controlling for type frequency, the partial correlation is non-significant in both the small ($r = 0.28$, $p = 0.16$) and large ($r = -0.12$, $p = 0.29$) samples. The pairwise SCS--confusion analysis (\\S\\ref{sec:pairwise}), which is immune to this batch-level aggregation artifact, remains the primary evidence for the NER confusability dimension.\n\n\\paragraph{Interpretation.}\nThe $n{=}25$ v2 result confirms that the confusability effect is directionally consistent across prompt designs, with attenuated magnitude: the gap narrows ($-$5.7\\,pp) but remains highly significant ($p < 0.001$, $r = -0.919$). The earlier $n{=}5$ non-significance reflected insufficient power and narrow BCS contrast, not absence of the effect. V2's stricter format constraints raise the baseline accuracy (low-BCS 85.2\\% vs.\\ 82.3\\%), but type confusion under high confusability persists (59.7\\% vs.\\ 51.0\\%). Prompt design modulates the practical magnitude of the confusability effect but does not eliminate it, ruling out prompt-specific confounding as the primary source. The underlying confusability signal (pairwise SCS--confusion correlation and the directional BCS--accuracy relationship) persists across both prompt versions.\n\n\\subsection{Cross-Prompt-Variant BCS Correlation}\n\\label{sec:appendix_prompt_variants}\n\nTo verify that the BCS--accuracy relationship is not an artifact of a specific prompt template, we evaluate four structurally distinct prompt variants on FewRel 80-relation RE at two count levels (8 and 32), with 10 random batches per condition.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{\\begin{tabular}{llrrrr}\n\\toprule\n\\textbf{Variant} & \\textbf{Count} & \\textbf{Mean Acc} & \\textbf{$r$} & \\textbf{$p$} \\\\\n\\midrule\nV2 (definition-first) & 8 & 0.769 & $-$0.333 & 0.348 \\\\\nV2 (definition-first) & 32 & 0.564 & $-$0.648 & 0.043 \\\\\nInstruction-rewrite & 8 & 0.847 & $-$0.223 & 0.536 \\\\\nInstruction-rewrite & 32 & 0.662 & $-$0.469 & 0.171 \\\\\nChain-of-thought & 8 & 0.749 & $+$0.254 & 0.478 \\\\\nChain-of-thought & 32 & 0.617 & $-$0.566 & 0.088 \\\\\nMinimal & 8 & 0.852 & $-$0.170 & 0.638 \\\\\nMinimal & 32 & 0.615 & $-$0.771 & 0.009 \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{BCS--accuracy Pearson correlation across four prompt variants. At count 32, all four variants show negative BCS--accuracy correlations ($r \\leq -0.47$), with two reaching $p < 0.05$. At count 8, the narrower BCS range reduces statistical power.}\n\\label{tab:prompt_variants}\n\\end{table}\n\nAt count 32, all four variants produce negative BCS--accuracy correlations ($r$ ranges from $-$0.47 to $-$0.77), with V2 ($p = 0.043$) and Minimal ($p = 0.009$) reaching significance and Chain-of-thought approaching it ($p = 0.088$). At count 8, correlations are weaker and nonsignificant across all variants, consistent with the narrower BCS range at lower schema complexity reducing the detectable effect size. Rather than applying Bonferroni correction, which assumes independent hypotheses inappropriate for correlated prompt variants testing the same underlying signal, we note directional consistency: 7 of 8 conditions show negative BCS--accuracy slopes, consistent with the primary finding \\citep{rothman-1990}. These results confirm that the confusability effect arises from schema composition, not prompt-specific phrasing.\n\n\\section{BCS Aggregation Sensitivity}\n\\label{sec:appendix_bcs_sensitivity}\n\nWe define Batch Confusability Score (BCS) as the \\emph{mean} pairwise SCS across all type pairs in a batch (\\S\\ref{sec:bcs_controlled}). An alternative definition takes the \\emph{maximum} pairwise SCS within each batch to capture the single most confusable pair. Here we compare both aggregation methods to verify that core conclusions are robust to this choice.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llcccc}\n\\toprule\n\\textbf{Aggregation} & \\textbf{Condition} & \\textbf{Slope} & \\textbf{95\\% CI} & \\textbf{$r$} & \\textbf{$p$} \\\\\n\\midrule\nMEAN (primary) & 16-rel & $-$0.509 & [$-$0.686, $-$0.336] & $-$0.467 & ${<}\\,0.001$ \\\\\nMEAN & 80-pool 16-sub & $-$0.401 & [$-$0.701, $-$0.069] & $-$0.221 & 0.027 \\\\\n\\midrule\nMAX & 16-rel & $-$0.449 & [$-$0.552, $-$0.346] & $-$0.637 & ${<}\\,0.001$ \\\\\nMAX & 80-pool 16-sub & $-$0.401 & [$-$0.701, $-$0.069] & $-$0.221 & 0.027 \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{BCS--accuracy regression under mean vs.\\ max pairwise SCS aggregation (FewRel, 16-relation batches). Permutation test for slope equivalence across pools: MEAN $p \\approx 0.60$; MAX $p \\approx 0.44$. The 80-pool row is identical under both definitions because these batches were collected using mean-aggregated BCS; the MAX column reflects the same data for completeness.}\n\\label{tab:bcs_aggregation}\n\\end{table}\n\nMAX aggregation yields stronger correlations ($r = -0.637$ vs.\\ $-0.467$ for 16-rel), consistent with the hypothesis that the single most confusable pair in a batch predicts substitution errors. Both definitions produce significant negative slopes across all conditions, and the permutation tests confirm no significant difference between independent and sampled pools under either definition. We adopt MEAN as the primary definition because it better represents average pairwise difficulty across all schema combinations, while MAX may overweight a single outlier pair. The choice does not affect any paper conclusion.\n\n\\section{BCS-Controlled Detailed Results}\n\\label{app:bcs-controlled-table}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lcrrrr}\n\\toprule\n\\textbf{Schema} & \\textbf{Count} & \\textbf{Low-BCS} & \\textbf{High-BCS} & \\textbf{$\\Delta$ (pp)} & \\textbf{95\\% CI} \\\\\n\\midrule\n16-rel & 8 & 88.9\\% & 79.8\\% & $-$9.1 & --- \\\\\n80-rel & 8 & 82.3\\% & 51.0\\% & $-$31.2 & {[}17.7, 42.7{]} \\\\\n80-rel & 16 & 82.8\\% & 51.6\\% & $-$31.2 & {[}22.9, 39.6{]} \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{BCS-controlled FewRel accuracy. Low-BCS batches contain maximally dissimilar types; high-BCS batches contain maximally similar types. The 80-relation extreme-batch gap reflects the wider BCS range; regression slopes are consistent across pools ($p = 0.60$; Table~\\ref{tab:within_pool}; see \\S\\ref{sec:practical_magnitude} for typical-batch magnitudes). The 16-relation condition used a single extreme batch per BCS level; bootstrap CIs require multiple batches.}\n\\label{tab:bcs_controlled}\n\\end{table}\n\n\\paragraph{Adjusted $R^2$ and confidence intervals.}\nDocRED regressions (\\S\\ref{sec:bcs_controlled}) use OLS on $n = 35$ batches (5 high-BCS + 5 low-BCS + 25 random) with one predictor. At count 16, adjusted $R^2 = 0.511$ (unadjusted: 0.525; 95\\% CI via Fisher $z$-transformation: [0.27, 0.73]); at count 32, adjusted $R^2 = 0.426$ (unadjusted: 0.443; CI: [0.18, 0.67]). The small shrinkage ($\\Delta R^2 \\leq 0.02$) indicates the unadjusted values are not inflated by the predictor-to-sample ratio.\n\n\\section{Within-Pool Analysis Methodology}\n\\label{app:within-pool-method}\n\nA potential confound in the cross-scale comparison is that the 16-relation and 80-relation pools contain different types, so the observed gap could reflect pool composition rather than confusability. To control for this, we draw 100 random 16-relation subsets from the 80-relation pool and evaluate under the same BCS-controlled protocol.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lrrrrrrr}\n\\toprule\n& \\multicolumn{4}{c}{\\textbf{Regression (BCS $\\to$ Accuracy)}} & \\multicolumn{2}{c}{\\textbf{Quartile $\\Delta$}} \\\\\n\\cmidrule(lr){2-5} \\cmidrule(lr){6-7}\n\\textbf{Setting} & \\textbf{Slope} & \\textbf{95\\% CI} & \\textbf{$r$} & \\textbf{$p$} & \\textbf{$\\Delta$ (pp)} & \\textbf{95\\% CI} \\\\\n\\midrule\nIndependent 16-rel ($n{=}100$) & $-$0.509 & [$-$0.686, $-$0.336] & $-$0.467 & ${<}\\,0.001$ & $-$5.31 & [$-$7.44, $-$3.19] \\\\\n80-pool $\\to$ 16-sub ($n{=}100$) & $-$0.401 & [$-$0.701, $-$0.069] & $-$0.221 & $0.027$ & $-$3.92 & [$-$8.17, $+$0.38] \\\\\nFull 80-rel ($n{=}25$)$^\\dagger$ & $+$0.221 & [$-$1.303, $+$1.695] & $+$0.064 & $0.76$ & $-$1.04 & [$-$10.12, $+$8.04] \\\\\n\\midrule\n\\multicolumn{7}{l}{\\footnotesize Permutation test (16-rel vs.\\ 80-pool slopes): $p \\approx 0.60$ (5{,}000 permutations)} \\\\\n\\multicolumn{7}{l}{\\footnotesize $^\\dagger$BCS range (IQR\\,=\\,0.033) insufficient for regression; slope not interpretable.} \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Three-way BCS--accuracy analysis on FewRel. Slope: OLS of batch accuracy on BCS (bootstrap CIs, $B{=}10{,}000$). $\\Delta$: accuracy gap between top- and bottom-quartile BCS batches. See Appendix~\\ref{sec:appendix_within_pool} for CI interpretation.}\n\\label{tab:within_pool}\n\\end{table}\n\nThe within-pool slope ($-$0.401, CI excludes zero) is statistically indistinguishable from the independent 16-relation pool ($-$0.509; permutation $p \\approx 0.60$). The smaller quartile gap ($-$3.92\\,pp vs.\\ $-$5.31\\,pp) reflects the narrower BCS range within the 80-relation pool (Appendix~\\ref{sec:appendix_within_pool}).\n\nIn the full 80-relation condition, natural BCS variation is insufficient (IQR${}=0.033$) to yield a detectable effect ($n=25$, slope${}=+0.221$, $p \\approx 0.76$). This does not invalidate the confusability effect; the within-pool slope is significant ($p=0.027$) when BCS is deliberately varied, but establishes that natural schema sampling at this scale does not produce sufficient BCS contrast for detection.\n\n\\section{SCS Embedding Ablation: Name-Only vs. Name+Definition}\n\\label{app:scs-ablation}\n\nTable~\\ref{tab:scs-ablation} compares predictive accuracy of name-only SCS against name+definition SCS across three datasets.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{\\begin{tabular}{lcccc}\n\\toprule\nDataset & SCS$_\\text{name}$ $r$ & SCS$_\\text{def}$ $r$ & $\\Delta r$ & Matrix corr. \\\\\n\\midrule\nFew-NERD & 0.172 & 0.149 & $-$0.023 & 0.894 \\\\\nMAVEN & 0.129 & 0.164 & +0.035 & 0.656 \\\\\nFewRel & 0.178 & 0.193 & +0.015 & 0.848 \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Pearson correlation between SCS and empirical confusion rate. ``Def'' concatenates type name with definition before embedding. All correlations significant ($p < 0.001$). The inconsistent direction of $\\Delta r$ indicates that definitions provide no systematic benefit.}\n\\label{tab:scs-ablation}\n\\end{table}\n\nFew-NERD is the only dataset whose prompts include type definitions; for MAVEN and FewRel, prompts use type names alone, so name-only SCS directly matches model input. The high matrix correlation (0.66--0.89) confirms that type names capture the dominant semantic structure.\n\n\\paragraph{Held-out validation.}\n\\label{app:scs-heldout-validation}\nFrom the 80-type confusion matrix, we extract the $\\binom{16}{2} = 120$ pairs among the 16 validation-origin types (fully disjoint from the 64 training-pool types). The SCS--confusion Spearman correlation remains positive and significant ($\\rho = 0.216$, $p = 0.018$), nearly identical to the full 80-type pool ($\\rho = 0.218$, $p < 10^{-34}$, $n = 3{,}160$ pairs), ruling out training-set contamination as the driver of the observed relationship.\n\n\\section{Pair-to-Batch Aggregation Simulation}\n\\label{app:aggregation-sim}\n\nThe following simulation provides an illustrative explanatory model for how pair-level effects aggregate to batch-level variance. It is not the evidence base for our claims; the observed batch-level $R^2 = 0.218$ (\\S\\ref{sec:practical_magnitude}) is a direct empirical measurement independent of this simulation.\n\n\\paragraph{Setup.} We examine whether the pair-level $R^2 \\approx 7\\%$ (computed over non-zero confusion pairs) can aggregate to the observed batch-level $R^2 \\approx 22\\%$ via a Monte Carlo simulation. From the FewRel 16-relation experiment, we estimate the inter-pair SCS correlation for pairs sharing a common type ($\\rho_\\text{SCS} = 0.35$). For batches of $k=8$ types ($\\binom{8}{2}=28$ pairs), we simulate 10{,}000 iterations: (1) generate 28 correlated pair-level effects with individual $R^2 = 0.074$; (2) average to obtain batch-level signals; (3) compute batch-level $R^2$.\n\n\\paragraph{Results.} Simulated batch $R^2 = 0.219$ [95\\% CI: 0.092--0.361], matching the observed value of 0.218. The effective amplification factor is $\\sim$3$\\times$, explained by signal correlation within batches preserving variance while independent noise averages out (effective degrees of freedom $\\approx 3.4$, not 28).\n\n\\paragraph{Unconditional baseline.}\nWhen the simulation uses the unconditional pairwise $r^2 = 0.013$ (computed over all type pairs including zero-confusion pairs; Table~\\ref{tab:pairwise}), the simulated batch-level $R^2$ drops to $0.044$ [95\\% CI: 0.001--0.151], well below the observed $R^2 = 0.218$. The analytical formula confirms: $\\text{SNR} \\times \\text{EF} / (\\text{SNR} \\times \\text{EF} + 1) = 0.042$ with the same effective factor $\\text{EF} = 3.35$. This ${\\sim}5\\times$ gap reflects the dilution from zero-confusion pairs: approximately 89\\% of type pairs never exhibit mutual confusion, contributing only noise to the unconditional correlation. The conditional model ($R^2 = 0.074 \\to 0.219$) matches the observed value because it isolates the minority of semantically proximate pairs that actually compete during type resolution; BCS predicts batch accuracy through the density of \\emph{active} confusable pairs, not uniform contributions from all pairs.\n\n\\paragraph{Sensitivity to $\\rho$.}\nThe inter-pair SCS correlation $\\rho = 0.35$ is estimated from pairs sharing a common type. At $\\rho = 0.20$ (halved correlation), a parallel simulation yields batch $R^2 \\approx 0.22$, still matching the observed value; at $\\rho = 0.50$, the correlation structure approaches the positive-definiteness boundary; $\\rho = 0.35$ thus sits in a stable regime. The simulation is illustrative; the observed batch $R^2 = 0.218$ is the primary evidence.\n\n\\section{BCS Independence from Type Composition}\n\\label{app:bcs-composition}\n\nFewRel's balanced design (700 instances per type) makes type frequency invariant across batches, ruling out frequency-driven confounding. To test whether BCS captures information beyond type composition effects, we decompose the explained variance in a joint model (accuracy $\\sim$ BCS $+$ mean type difficulty), where type difficulty is the per-type solo-baseline accuracy averaged across batch members. On 100 random 8-type batches from the 16-relation pool, the joint model explains $R^2 = 0.704$. Variance decomposition yields: BCS unique $R^2 = 0.259$ (36.8\\% of explained variance), composition unique $R^2 = 0.298$ (42.3\\%), and shared $R^2 = 0.147$ (20.9\\%). The near-orthogonality of predictors (VIF${}\\,=\\,1.06$, $r(\\text{BCS}, \\text{difficulty}) = -0.21$) confirms that BCS captures confusability-specific signal rather than a proxy for type difficulty.\n\n\\section{SCS vs.\\ Simple Baselines}\n\\label{app:scs-baselines}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llrr}\n\\toprule\n\\textbf{Dataset} & \\textbf{Metric} & \\textbf{Spearman $\\rho$} & \\textbf{$p$} \\\\\n\\midrule\nFewRel & SCS (embedding) & \\textbf{0.218} & $2.2 \\times 10^{-35}$ \\\\\n(3{,}160 pairs) & Same-parent (WordNet) & 0.097 & $5.4 \\times 10^{-8}$ \\\\\n& WordNet Wu-Palmer & 0.073 & $4.3 \\times 10^{-5}$ \\\\\n& Levenshtein & 0.016 & 0.363 (n.s.) \\\\\n\\midrule\nFew-NERD & SCS (embedding) & \\textbf{0.166} & $1.5 \\times 10^{-13}$ \\\\\n(1{,}953 pairs) & Levenshtein & 0.152 & $1.4 \\times 10^{-11}$ \\\\\n& Same-parent (prefix) & 0.146 & $7.8 \\times 10^{-11}$ \\\\\n& WordNet Wu-Palmer & 0.054 & 0.070 (n.s.)$^\\dagger$ \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Pairwise confusion prediction: SCS vs.\\ simple baselines. Spearman $\\rho$ between each metric and the empirical confusion rate. SCS outperforms all baselines on FewRel; the margin is smaller on Few-NERD, where hierarchical naming conventions provide partial signal to string-based metrics. $^\\dagger$42\\% of pairs lack WordNet coverage.}\n\\label{tab:scs_baselines}\n\\end{table}\n\n\\section{Split-Origin Covariate Analysis}\n\\label{app:split-origin}\n\nFewRel combines 64 train-split and 16 val-split relation types into a single 80-type pool.  Train-origin types show numerically lower accuracy ($-8.8$\\,pp, $p = 0.06$; see Limitations), raising the question of whether differential pre-training exposure confounds the BCS--accuracy relationship.  We test this by adding a per-batch \\emph{train-origin ratio} (fraction of relation types drawn from the train split) as a covariate in the BCS--accuracy regression.\n\n\\paragraph{Method.}  Across 213 multi-type batches ($k \\geq 2$) from the batch-composition experiment (\\S\\ref{sec:sdgd}) and the factorial design (\\S\\ref{sec:bcs_controlled}), we compute $\\texttt{train\\_origin\\_ratio} = n_{\\text{train}} / k$ for each batch.  The ratio ranges from 0.40 to 1.00 (mean 0.80, consistent with the 64/80 base rate).  We fit:\n{\\small\\begin{equation*}\n\\text{acc} = \\beta_0 + \\beta_{\\text{BCS}} \\!\\cdot\\! \\text{BCS} + \\beta_{\\text{orig}} \\!\\cdot\\! \\text{train\\_origin\\_ratio} + \\varepsilon\n\\end{equation*}}\n\n\\paragraph{Results.}  The BCS partial effect is unchanged after controlling for split-origin: $\\beta_{\\text{BCS}} = -0.416$, $p < 10^{-16}$ (vs.\\ $\\beta = -0.412$, $p < 10^{-16}$ without the covariate).  Train-origin ratio is not independently significant ($\\beta_{\\text{origin}} = -0.057$, $p = 0.245$), and $\\Delta R^2 = 0.005$.  The BCS--accuracy relationship is therefore not confounded by differential pre-training exposure at the batch level.\n\nPairwise SCS distributions do not differ significantly between train-origin (64 types, mean\\,=\\,0.880) and val-origin (16 types, mean\\,=\\,0.874) subsets (Mann-Whitney $p = 0.754$, Cohen's $d = 0.081$); the train/val split does not introduce systematic confusability bias.\n\n\\section{Cross-Seed Variance Decomposition}\n\\label{app:variance-decomposition}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{rrrr}\n\\toprule\n\\textbf{Count} & \\textbf{Batch SD} & \\textbf{Seed SD} & \\textbf{Ratio} \\\\\n\\midrule\n4 & 0.0889 & 0.0122 & 53.5 \\\\\n8 & 0.0820 & 0.0098 & 70.0 \\\\\n16 & 0.0626 & 0.0270 & 5.4 \\\\\n32 & 0.0462 & 0.0091 & 26.0 \\\\\n40 & 0.0421 & 0.0019 & 474.4 \\\\\n64 & 0.0245 & 0.0022 & 119.8 \\\\\n80 & 0.0001 & 0.0088 & $<$0.1 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Variance decomposition on FewRel (3 seeds $\\times$ 25 batches per count level). Batch SD: root-mean intra-seed variance averaged over seeds. Seed SD: standard deviation of per-seed means. Ratio = batch variance / seed variance. At count 80, only one batch composition exists, so batch variance vanishes by construction.}\n\\label{tab:variance_decomposition}\n\\end{table}\n\nIntra-batch variance dominates inter-seed variance by 5--474$\\times$ across count levels 4--64 (mean 125$\\times$); random batch composition is the primary source of performance variability. Under greedy decoding (temperature${}\\,=\\,0$), model inference is nearly deterministic; the inter-seed variance reflects differences in which random batch compositions each seed generates, not inference stochasticity. At count 80, the full schema admits only one composition, leaving residual model-level noise as the sole variance source (seed SD = 0.88\\,pp, likely attributable to FP8 quantization non-determinism).\n\n\\section{Cross-Domain Connections}\n\\label{app:cross-domain}\n\nThe schema-associated degradation documented here is not unique to information extraction. Schema-Guided Dialogue systems (SGD/SGD-X; \\citealt{rastogi2020towards}) face an analogous challenge: as the number of intent and slot types grows, dialogue state tracking accuracy declines. \\citet{li2023evaluating} observed count-dependent degradation in ChatGPT-based IE, attributing it to prompt overload. Our two-dimensional decomposition offers a more refined explanation: schema size per se is not the sole predictor; rather, larger schemas increase the probability of including high-SCS pairs, which contribute disproportionately to confusion. This distinction has practical implications: a schema of 80 types with low mutual confusability may outperform a 40-type schema with clustered semantics, and suggests that confusability-aware design principles may generalize to any task where an LLM must discriminate among a prompt-specified label inventory.\n\n\\section{Cross-Model Validation with LLaMA-3.1-70B-Instruct (FP8)}\n\\label{sec:appendix_cross_model_70b}\n\nTo test whether the two-dimensional degradation pattern generalizes across model families, we replicate the count-curve and BCS-controlled experiments on Meta-LLaMA-3.1-70B-Instruct (FP8 quantization). All batch compositions, type pools, and test samples are identical to those used for Qwen3-32B (\\S\\ref{sec:count_curves}, \\S\\ref{sec:bcs_controlled}).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{lrr}\n\\toprule\n\\textbf{Count} & \\textbf{LLaMA-70B} & \\textbf{Qwen3-32B} \\\\\n\\midrule\n\\multicolumn{3}{l}{\\textit{RE (FewRel, Classification Accuracy)}} \\\\\n8  & 0.757 & 0.805 \\\\\n16 & 0.685 & 0.719 \\\\\n32 & 0.601 & 0.652 \\\\\n64 & 0.504 & 0.539 \\\\\n80 & 0.450 & 0.504 \\\\\n\\midrule\n\\multicolumn{3}{l}{\\textit{NER (Few-NERD, Text+Type Match Recall)}} \\\\\n2  & 0.323 & 0.515 \\\\\n6  & 0.300 & 0.399 \\\\\n12 & 0.278 & 0.318 \\\\\n22 & 0.252 & 0.279 \\\\\n44 & 0.297 & 0.309 \\\\\n66 & 0.273 & 0.407 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Cross-model count curves for LLaMA-3.1-70B-Instruct (FP8) and Qwen3-32B. RE decline (count 8$\\to$80): $-$30.7\\,pp (70B) vs.\\ $-$30.1\\,pp (32B). NER decline (count 2$\\to$22): $-$7.1\\,pp (70B) vs.\\ $-$23.6\\,pp (32B); both models exhibit a U-shaped rebound at higher counts. 25 batches per count level, same samples and batch compositions across models (seed 42). All metrics are micro-averaged across batches.}\n\\label{tab:cross_model_70b}\n\\end{table}\n\nTable~\\ref{tab:cross_model_70b} shows that RE degradation slopes are near-identical: $-$30.7\\,pp (70B) versus $-$30.1\\,pp (32B) from count 8 to count 80, with the 70B model approximately 4\\,pp lower in absolute accuracy at each count level. This quantitative match provides strong evidence that Dimension~1 (count-related decline) is directionally consistent across architectures for RE.\n\nOn NER, the count-related decline direction is consistent across models: both 70B and Qwen3 show a recall decline from count 2 to count 22 (70B: 0.323$\\to$0.252, $-$7.1\\,pp; Qwen3: 0.515$\\to$0.279, $-$23.6\\,pp). Both models also exhibit a U-shaped rebound at higher counts (70B: 0.252 at count 22 $\\to$ 0.297 at count 44; Qwen3: 0.279 at count 22 $\\to$ 0.407 at count 66), which cross-validates the U-shape phenomenon. The magnitude difference reflects a precision-recall tradeoff: 70B operates more conservatively (higher precision, lower recall), while Qwen3 over-predicts (higher recall, lower precision, especially at low counts).\n\nFor the confusability dimension (Dimension 2), at count 16 on FewRel, LLaMA-70B achieves low-BCS accuracy of 0.708 versus high-BCS accuracy of 0.599 ($\\Delta = +10.9$\\,pp, 95\\% CI: [$+$3.0, $+$20.1]). The confidence interval excludes zero; the confusability effect is thus confirmed at the 70B scale.\n\nIn summary, FewRel RE provides a quantitative match across models (near-identical slopes for Dimension~1 and a significant Dimension~2 effect). NER provides directional consistency: the count-related decline direction is preserved and the U-shaped rebound replicates, though magnitudes vary with each model's precision-recall operating point. Together, these results indicate that the degradation pattern is directionally consistent across architectures.\n\n\\section{Cross-Model Validation with Gemini 2.5 Flash (API)}\n\\label{sec:appendix_cross_model_gemini}\n\nWe further validate Dimension~1 on a proprietary model, Gemini 2.5 Flash \\citep{gemini-2025}, accessed via API. This extends the cross-model evidence from open-weight families (Qwen, LLaMA) to a proprietary architecture with unknown training details. We replicate the FewRel count-curve experiment using the same 960 balanced samples, batch compositions, and evaluation protocol as Qwen3-32B.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{lrr}\n\\toprule\n\\textbf{Count} & \\textbf{Gemini Flash} & \\textbf{Qwen3-32B} \\\\\n\\midrule\n1  & 0.827 & --- \\\\\n4  & 0.873 & 0.870 \\\\\n8  & 0.820 & 0.805 \\\\\n16 & 0.787 & 0.719 \\\\\n32 & 0.739 & 0.652 \\\\\n64$^\\dagger$ & 0.637 & 0.539 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Cross-model count curves for Gemini 2.5 Flash (API) and Qwen3-32B on FewRel RE (classification accuracy). 25 batches per count level, same samples and batch compositions (seed 42). Gemini's count-1 result is included for completeness; Qwen3 count-1 was not collected. Both models show monotonic decline from count 4 onward ($\\rho = -1.0$ for both on counts 4--32). $^\\dagger$Count 64: Gemini based on 11/25 batches (partial).}\n\\label{tab:cross_model_gemini}\n\\end{table}\n\nTable~\\ref{tab:cross_model_gemini} confirms that the count-related accuracy decline replicates on Gemini 2.5 Flash. From count 4 to count 32, both models show perfectly monotonic decline (Spearman $\\rho = -1.0$). Including count 1, the Gemini count curve yields $\\rho = -0.900$ ($p = 0.037$); including partial count-64 data (11/25 batches), $\\rho = -0.943$ ($p = 0.005$). The decline magnitude is smaller for Gemini ($-$13.3\\,pp from count 4 to 32) than for Qwen3 ($-$21.8\\,pp), consistent with Gemini's higher absolute accuracy providing more headroom before degradation saturates. At each count level, Gemini matches or exceeds Qwen3, with the gap widening at higher counts (0.3\\,pp at count 4 vs.\\ 8.7\\,pp at count 32, 9.8\\,pp at partial count 64); Gemini appears more robust to schema scaling but not immune. Dimension~2 (BCS-controlled confusability) has not been tested on proprietary models; cross-architecture Dimension~2 validation remains for future work.\n\n\\section{Few-Shot Prompting and Confusability}\n\\label{sec:appendix_fewshot_bcs}\n\nTo test whether in-context demonstrations mitigate the BCS-associated confusability effect, we evaluate 0-shot, 1-shot, and 5-shot prompting on FewRel 80-relation RE at count 8 using the same extreme-BCS batch design as \\S\\ref{sec:bcs_controlled}. Each condition uses 50 batches (25 low-BCS, mean $\\approx 0.36$; 25 high-BCS, mean $\\approx 0.80$), drawn from the pre-constructed batch pool of \\S\\ref{sec:bcs_controlled}. Few-shot examples are sampled from the FewRel training split for each target type.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{\\begin{tabular}{lrrrl}\n\\toprule\n\\textbf{Condition} & \\textbf{Low-BCS} & \\textbf{High-BCS} & \\textbf{$\\Delta$ (pp)} & \\textbf{95\\% CI} \\\\\n\\midrule\n0-shot & 0.682 & 0.498 & +18.5 & {[}+14.3, +22.7{]} \\\\\n1-shot & 0.754 & 0.554 & +20.0 & {[}+16.3, +23.5{]} \\\\\n5-shot & 0.715 & 0.488 & +22.8 & {[}+18.9, +26.8{]} \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{BCS gap under few-shot prompting (FewRel, count 8). Demonstrations improve absolute accuracy on low-BCS batches (+3.3--7.2\\,pp over 0-shot) but provide inconsistent benefit on high-BCS batches (+5.6\\,pp at 1-shot, $-$1.0\\,pp at 5-shot). The confusability gap widens from +18.5\\,pp (0-shot) to +22.8\\,pp (5-shot). All metrics are micro-averaged across batches.}\n\\label{tab:fewshot_bcs}\n\\end{table}\n\nDemonstrations improve absolute accuracy primarily on low-BCS (easy) batches, where type boundaries are already distinct and examples reinforce correct mappings. On high-BCS batches, where types are semantically confusable, demonstrations provide inconsistent benefit (+5.6\\,pp at 1-shot, $-$1.0\\,pp at 5-shot): the model still substitutes similar types at comparable rates. The net effect is that the confusability gap widens under few-shot prompting (+4.3\\,pp from 0-shot to 5-shot, bootstrap $p = 0.014$), with all three confidence intervals excluding zero. This indicates that BCS-associated type confusion is a structural property of the schema composition rather than a deficit addressable through prompt engineering. The non-monotonic low-BCS pattern (0.754 at 1-shot vs.\\ 0.715 at 5-shot) may reflect lost-in-middle effects from increased prompt length \\cite{lost-in-middle-2024}.\n\nThe 0-shot gap (+18.5\\,pp) is smaller than the extreme-batch gap reported in \\S\\ref{sec:bcs_controlled} (+25.5\\,pp) because the two experiments use different test splits and batch sampling seeds; direct magnitude comparison across experiments is not appropriate.\n\n\\section{Qualitative Error Analysis}\n\\label{app:error-analysis}\n\nTables~\\ref{tab:top10_re} and~\\ref{tab:top10_ner} list the ten most frequently confused type pairs on FewRel 80-relation RE and Few-NERD NER. Confusion counts are aggregated bidirectionally across three random seeds (72{,}000 predictions per seed for RE; single-seed 66-type extraction for NER).\n\n\\begin{table}[h]\n\\centering\n\\footnotesize\n\\begin{tabular}{clllr}\n\\toprule\n\\textbf{\\#} & \\textbf{Type A} & \\textbf{Type B} & \\textbf{SCS} & \\textbf{$N$} \\\\\n\\midrule\n1 & instance of & taxon rank & 0.53 & 875 \\\\\n2 & child & father & 0.84 & 700 \\\\\n3 & participant of & participating team & 0.75 & 675 \\\\\n4 & mountain range & part of & 0.57 & 575 \\\\\n5 & mouth of watercourse & tributary & 0.65 & 549 \\\\\n6 & child & mother & 0.84 & 500 \\\\\n7 & league & member of & 0.66 & 450 \\\\\n8 & country of citizenship & country of origin & 0.76 & 400 \\\\\n9 & followed by & follows & 0.90 & 400 \\\\\n10 & occupation & voice type & 0.57 & 400 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Top-10 confused relation pairs on FewRel 80-relation RE. $N$: bidirectional confusion count aggregated over 3 seeds $\\times$ 25 batches. SCS: pairwise Schema Confusability Score (Qwen3 embedding cosine similarity). High-SCS pairs (e.g., \\textit{followed by}/\\textit{follows}, SCS\\,=\\,0.90) and family-relation pairs (\\textit{child}/\\textit{father}, \\textit{child}/\\textit{mother}) dominate. Some low-SCS pairs (\\textit{instance of}/\\textit{taxon rank}, SCS\\,=\\,0.53) reflect domain-specific co-occurrence rather than semantic similarity.}\n\\label{tab:top10_re}\n\\end{table}\n\n\\begin{table}[h]\n\\centering\n\\footnotesize\n\\begin{tabular}{clllr}\n\\toprule\n\\textbf{\\#} & \\textbf{Type A} & \\textbf{Type B} & \\textbf{SCS} & \\textbf{$N$} \\\\\n\\midrule\n1 & person-other & person-politician & 0.93 & 121 \\\\\n2 & location-GPE & organization-other & 0.83 & 81 \\\\\n3 & art-film & location-GPE & 0.69 & 57 \\\\\n4 & building-other & location-GPE & 0.85 & 56 \\\\\n5 & building-other & person-other & 0.90 & 43 \\\\\n6 & location-GPE & product-other & 0.69 & 39 \\\\\n7 & org-gov/agency & person-other & 0.85 & 34 \\\\\n8 & person-actor & person-other & 0.90 & 34 \\\\\n9 & building-other & location-road/transit & 0.76 & 32 \\\\\n10 & location-GPE & org-sportsleague & 0.81 & 30 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Top-10 confused entity type pairs on Few-NERD NER. $N$: bidirectional confusion count from 66-type full-schema extraction. SCS: pairwise Schema Confusability Score (Qwen3 embedding cosine similarity). Intra-category confusions (e.g., \\textit{person-other}/\\textit{person-politician}, SCS\\,=\\,0.93) and cross-category pairs sharing referent overlap (\\textit{building-other}/\\textit{location-GPE}, SCS\\,=\\,0.85) are most frequent. The ``other'' subtypes absorb diverse entities and confuse with more specific siblings.}\n\\label{tab:top10_ner}\n\\end{table}\n\n\\paragraph{Illustrative error instances.}\nTable~\\ref{tab:error_examples} shows three FewRel instances where the model predicted a semantically adjacent relation. All gold-predicted pairs have SCS\\,$>$\\,0.90.\n\n\\begin{table}[h]\n\\centering\n\\footnotesize\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{p{5.8cm}llc}\n\\toprule\n\\textbf{Sentence (abridged)} & \\textbf{Gold} & \\textbf{Predicted} & \\textbf{SCS} \\\\\n\\midrule\nOver five EuroLeague games he played for \\textbf{Valencia}, he averaged 8 points \\ldots\\  [\\textbf{EuroLeague}, \\textbf{Valencia}] & participant & participant of & 0.97 \\\\\n\\addlinespace\n\\textbf{Pilões} is a municipality in the state of \\textbf{Rio Grande do Norte} in the Northeast region of Brazil. & contains admin.\\ terr.\\ entity & located in admin.\\ terr.\\ entity & 0.92 \\\\\n\\addlinespace\nIn May 1997 Davies was appointed \\ldots\\ to the \\textbf{Cabinet} as \\textbf{Secretary of State for Wales}. & part of & member of & 0.90 \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Representative confusion instances from FewRel 80-relation RE (Qwen3-32B, count\\,=\\,80). Head and tail entities are bolded. In each case, the gold and predicted relations are semantically close (SCS\\,$>$\\,0.90): \\textit{participant} vs.\\ \\textit{participant of} reverses argument directionality; \\textit{contains} vs.\\ \\textit{located in} inverts the containment relation; \\textit{part of} vs.\\ \\textit{member of} conflates meronymy with membership. These confusions are consistent with the pairwise SCS--confusion correlation reported in \\S\\ref{sec:pairwise}.}\n\\label{tab:error_examples}\n\\end{table}\n\n\\section{Schema Label Renaming Experiment}\n\\label{app:renaming}\n\nTo test whether reducing pairwise SCS through label renaming improves accuracy, we conducted a controlled intervention on FewRel 80-relation RE (count 8, Qwen3-32B). We identified 14 high-SCS relation pairs (covering 12 unique relation types, as two types each appear in multiple pairs; mean SCS = 0.87) and replaced one label in each pair with a semantically distinct paraphrase chosen to minimize embedding cosine similarity (all-MiniLM-L6-v2). Examples: \\textit{participant of} $\\to$ \\textit{event involvement} (SCS: 0.97 $\\to$ 0.72), \\textit{follows} $\\to$ \\textit{prior entry} (0.90 $\\to$ 0.69), \\textit{part of} $\\to$ \\textit{integral segment of} (0.90 $\\to$ 0.64). The renaming reduced mean pairwise SCS from 0.87 to 0.67 ($\\Delta = -0.20$). We ran the same 50 BCS-controlled batches (25 low-BCS, 25 high-BCS; 96 samples each) under both original (control) and renamed (treatment) label sets.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n& \\textbf{Control} & \\textbf{Treatment} & \\textbf{$\\Delta$\\,(pp)} \\\\\n\\midrule\nLow-BCS ($n=25$)  & 90.1 & 87.1 & $-$3.0 \\\\\nHigh-BCS ($n=25$) & 69.3 & 60.5 & $-$8.8 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Accuracy (\\%) under original vs.\\ renamed labels on FewRel count-8 batches. Renaming reduced embedding similarity but decreased accuracy in both groups, with a larger drop on high-BCS batches (Cohen's $d = -2.92$) than low-BCS ($d = -1.09$). Interaction: $\\Delta_{\\text{high}} - \\Delta_{\\text{low}} = -5.9$\\,pp ($t = -7.23$, $p < 0.001$).}\n\\label{tab:renaming}\n\\end{table}\n\nRenaming hurt accuracy uniformly: both groups showed significant declines (paired $t$-test, both $p < 0.001$). The number of renamed types per batch correlated negatively with accuracy change ($r = -0.625$, $p < 0.001$). A solo sanity check confirmed that 11 of 12 renamed labels were individually recognizable (accuracy $\\geq$ original $-5$\\,pp). The results indicate that replacing familiar Wikidata labels with unfamiliar paraphrases disrupts the model's type semantics; this label unfamiliarity effect outweighs any benefit from reduced confusability.\n\n\\end{document}\n",
      "numLines": 707,
      "startLine": 1,
      "totalLines": 707
    }
  },
  "sourceToolAssistantUUID": "da49144f-ceab-4df6-b939-2b30013b573e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_reviewer_2_302b64f9",
  "sessionId": "0ff1fe81-4731-4c76-91b4-02652701ddff",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Tool call

_source line 16 · 2026-05-19T04:30:51.949Z_

<details open><summary>🔧 Tool call — Read · `toolu_01REGqMkvoaHpFzUdNrKrQrx`</summary>

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
  "parentUuid": "49ad9356-8430-42cc-b714-b59903efd3e1",
  "isSidechain": false,
  "requestId": "req_011CbBJL3Mfp6QVPxgqBTm4o",
  "type": "assistant",
  "uuid": "ee5efe11-9cf4-4b3a-99e5-b8a07deceeda",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_reviewer_2_302b64f9",
  "sessionId": "0ff1fe81-4731-4c76-91b4-02652701ddff",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PMdzHtBXazYPW4S8Z616zu",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2278,
      "cache_read_input_tokens": 28070,
      "output_tokens": 849,
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
          "output_tokens": 849,
          "cache_read_input_tokens": 28070,
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

_source line 17 · 2026-05-19T04:30:51.954Z_

<details><summary>↩ Tool result · `toolu_01REGqMkvoaHpFzUdNrKrQrx`</summary>

```text
1	\section{Introduction}
2	\label{sec:introduction}
3	
4	Training-free\footnote{We use ``training-free'' and ``zero-shot'' interchangeably to denote prompting without parameter updates.}\footnote{Code and data will be released upon acceptance. Anonymous review materials: \url{https://anonymous.4open.science/r/schema-dag-extraction}} LLM information extraction (prompting a large language model with a target schema and asking it to extract structured information without any task-specific fine-tuning) enables rapid deployment across new domains and ontologies. This zero-shot paradigm eliminates the need for labeled data, and is attractive for applications where annotation is expensive or schemas evolve frequently \cite{llm4ie-survey-2024}. Yet the paradigm carries a critical limitation: performance degrades sharply as the number of candidate types in the prompt schema grows. On named entity recognition, recall drops from 0.72 with a single candidate type to a plateau of ${\sim}$0.27 across intermediate schema sizes (22--44 types) before partial recovery at full-schema. On relation extraction, accuracy falls from 85.7\% with one relation to 49.5\% with 80 relations (sentence-level) and from 88.0\% to 38.7\% with 96 relations (document-level), near-halving or worse. This degradation is not academic: real-world ontologies routinely define 50--200+ types, which places them squarely in the regime where training-free extraction becomes unreliable.
5	
6	What explains this degradation? Prior decomposition strategies \cite{uniner-2024,llm-pee-2025,parse-2025} conflate two factors: having more types to discriminate among (count) and having semantically similar types to confuse (confusability) (hereafter Dimension~1 and Dimension~2). None isolates which factor predicts the gains (\S\ref{sec:related_work}).
7	
8	This study combines correlational analyses with quasi-experimental manipulation (BCS-controlled batches) to characterize how schema properties predict extraction accuracy.
9	
10	We ask three questions. \textbf{RQ1}: Does type confusability independently predict extraction degradation beyond the effect of type count? \textbf{RQ2}: Through what modes do count and confusability each degrade performance? \textbf{RQ3}: Can confusability-aware schema decomposition improve extraction quality?
11	
12	To our knowledge, we present the first controlled study isolating type confusability from type count via stratified design in zero-shot LLM IE, spanning NER, RE, and event detection (ED). We quantify confusability using pairwise embedding similarity, the \emph{Schema Confusability Score} (SCS), and its batch-level aggregation, the \emph{Batch Confusability Score} (BCS). We evaluate on Few-NERD \cite{fewnerd-2021}, FewRel \cite{fewrel-2018}, DocRED \cite{docred-2019}, and MAVEN \cite{maven-2020} using Qwen3-32B (\S\ref{sec:experimental_setup}).
13	
14	Our experiments yield four findings:
15	(1)~Degradation operates along two largely additive dimensions: count-related recall decline (up to $-$49\,pp for document-level RE) and confusability-related type substitution (modest in typical batches), with count as the dominant factor (\S\ref{sec:count_curves}, \S\ref{sec:multi_channel}). The two dimensions show bounded interaction under a $\pm 3$\,pp margin in sentence-level RE (marginally at $\pm 2$\,pp; logit-scale inconclusive) but not in document-level RE or NER.
16	(2)~Pairwise SCS predicts type confusion across NER, RE, and ED (\S\ref{sec:pairwise}); at batch level, BCS predicts accuracy under RE's forced-choice format (\S\ref{sec:bcs_controlled}) but not in NER; per-type aggregation is confounded by centrality on homogeneous schemas (\S\ref{sec:centrality_confound}).
17	(3)~Effects are consistent across schema sizes, prompt designs, and model families (\S\ref{sec:bcs_controlled}).
18	(4)~Schema decomposition fails due to merge amplification in NER; RE confusability-aware grouping yields no significant improvement over random despite oracle routing that recovers substantial accuracy (\S\ref{sec:sdgd}).
19	
20	Our contributions are:
21	\begin{enumerate}[leftmargin=*,itemsep=2pt,topsep=2pt]
22	    \item We present what is, to our knowledge, the first controlled study that isolates count and confusability effects in training-free LLM extraction. Building on the embedding-similarity criterion from prior schema-partitioning work \cite{llm-pee-2025}, we design stratified experiments that quantify confusability's predictive relationship with extraction degradation across NER, RE, and event detection (\S\ref{sec:count_curves}, \S\ref{sec:pairwise}, \S\ref{sec:bcs_controlled}).
23	    \item We document a task asymmetry: under forced-choice classification, BCS explains 22--53\% of RE accuracy variance through type substitution, yet shows no batch-level signal in NER despite significant pairwise effects (\S\ref{sec:bcs_controlled}, \S\ref{sec:multi_channel}).
24	    \item We report a negative result: schema decomposition fails due to merge amplification in NER and routing failure in RE, and we diagnose structural barriers to confusability-aware extraction (\S\ref{sec:sdgd}).
25	\end{enumerate}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ee5efe11-9cf4-4b3a-99e5-b8a07deceeda",
  "isSidechain": false,
  "promptId": "8257bd0e-08b4-4530-aa87-1e185ea40a51",
  "type": "user",
  "uuid": "0b2efc0e-d92a-4ee6-bb04-2b736dcb13fe",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/introduction.tex",
      "content": "\\section{Introduction}\n\\label{sec:introduction}\n\nTraining-free\\footnote{We use ``training-free'' and ``zero-shot'' interchangeably to denote prompting without parameter updates.}\\footnote{Code and data will be released upon acceptance. Anonymous review materials: \\url{https://anonymous.4open.science/r/schema-dag-extraction}} LLM information extraction (prompting a large language model with a target schema and asking it to extract structured information without any task-specific fine-tuning) enables rapid deployment across new domains and ontologies. This zero-shot paradigm eliminates the need for labeled data, and is attractive for applications where annotation is expensive or schemas evolve frequently \\cite{llm4ie-survey-2024}. Yet the paradigm carries a critical limitation: performance degrades sharply as the number of candidate types in the prompt schema grows. On named entity recognition, recall drops from 0.72 with a single candidate type to a plateau of ${\\sim}$0.27 across intermediate schema sizes (22--44 types) before partial recovery at full-schema. On relation extraction, accuracy falls from 85.7\\% with one relation to 49.5\\% with 80 relations (sentence-level) and from 88.0\\% to 38.7\\% with 96 relations (document-level), near-halving or worse. This degradation is not academic: real-world ontologies routinely define 50--200+ types, which places them squarely in the regime where training-free extraction becomes unreliable.\n\nWhat explains this degradation? Prior decomposition strategies \\cite{uniner-2024,llm-pee-2025,parse-2025} conflate two factors: having more types to discriminate among (count) and having semantically similar types to confuse (confusability) (hereafter Dimension~1 and Dimension~2). None isolates which factor predicts the gains (\\S\\ref{sec:related_work}).\n\nThis study combines correlational analyses with quasi-experimental manipulation (BCS-controlled batches) to characterize how schema properties predict extraction accuracy.\n\nWe ask three questions. \\textbf{RQ1}: Does type confusability independently predict extraction degradation beyond the effect of type count? \\textbf{RQ2}: Through what modes do count and confusability each degrade performance? \\textbf{RQ3}: Can confusability-aware schema decomposition improve extraction quality?\n\nTo our knowledge, we present the first controlled study isolating type confusability from type count via stratified design in zero-shot LLM IE, spanning NER, RE, and event detection (ED). We quantify confusability using pairwise embedding similarity, the \\emph{Schema Confusability Score} (SCS), and its batch-level aggregation, the \\emph{Batch Confusability Score} (BCS). We evaluate on Few-NERD \\cite{fewnerd-2021}, FewRel \\cite{fewrel-2018}, DocRED \\cite{docred-2019}, and MAVEN \\cite{maven-2020} using Qwen3-32B (\\S\\ref{sec:experimental_setup}).\n\nOur experiments yield four findings:\n(1)~Degradation operates along two largely additive dimensions: count-related recall decline (up to $-$49\\,pp for document-level RE) and confusability-related type substitution (modest in typical batches), with count as the dominant factor (\\S\\ref{sec:count_curves}, \\S\\ref{sec:multi_channel}). The two dimensions show bounded interaction under a $\\pm 3$\\,pp margin in sentence-level RE (marginally at $\\pm 2$\\,pp; logit-scale inconclusive) but not in document-level RE or NER.\n(2)~Pairwise SCS predicts type confusion across NER, RE, and ED (\\S\\ref{sec:pairwise}); at batch level, BCS predicts accuracy under RE's forced-choice format (\\S\\ref{sec:bcs_controlled}) but not in NER; per-type aggregation is confounded by centrality on homogeneous schemas (\\S\\ref{sec:centrality_confound}).\n(3)~Effects are consistent across schema sizes, prompt designs, and model families (\\S\\ref{sec:bcs_controlled}).\n(4)~Schema decomposition fails due to merge amplification in NER; RE confusability-aware grouping yields no significant improvement over random despite oracle routing that recovers substantial accuracy (\\S\\ref{sec:sdgd}).\n\nOur contributions are:\n\\begin{enumerate}[leftmargin=*,itemsep=2pt,topsep=2pt]\n    \\item We present what is, to our knowledge, the first controlled study that isolates count and confusability effects in training-free LLM extraction. Building on the embedding-similarity criterion from prior schema-partitioning work \\cite{llm-pee-2025}, we design stratified experiments that quantify confusability's predictive relationship with extraction degradation across NER, RE, and event detection (\\S\\ref{sec:count_curves}, \\S\\ref{sec:pairwise}, \\S\\ref{sec:bcs_controlled}).\n    \\item We document a task asymmetry: under forced-choice classification, BCS explains 22--53\\% of RE accuracy variance through type substitution, yet shows no batch-level signal in NER despite significant pairwise effects (\\S\\ref{sec:bcs_controlled}, \\S\\ref{sec:multi_channel}).\n    \\item We report a negative result: schema decomposition fails due to merge amplification in NER and routing failure in RE, and we diagnose structural barriers to confusability-aware extraction (\\S\\ref{sec:sdgd}).\n\\end{enumerate}",
      "numLines": 25,
      "startLine": 1,
      "totalLines": 25
    }
  },
  "sourceToolAssistantUUID": "ee5efe11-9cf4-4b3a-99e5-b8a07deceeda",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_reviewer_2_302b64f9",
  "sessionId": "0ff1fe81-4731-4c76-91b4-02652701ddff",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Tool call

_source line 18 · 2026-05-19T04:30:52.010Z_

<details open><summary>🔧 Tool call — Read · `toolu_01E76eDBfFc8rES9gV4ptU84`</summary>

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
  "parentUuid": "0b2efc0e-d92a-4ee6-bb04-2b736dcb13fe",
  "isSidechain": false,
  "requestId": "req_011CbBJL3Mfp6QVPxgqBTm4o",
  "type": "assistant",
  "uuid": "01931e94-4607-451b-912c-dc1178145411",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_reviewer_2_302b64f9",
  "sessionId": "0ff1fe81-4731-4c76-91b4-02652701ddff",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PMdzHtBXazYPW4S8Z616zu",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2278,
      "cache_read_input_tokens": 28070,
      "output_tokens": 849,
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
          "output_tokens": 849,
          "cache_read_input_tokens": 28070,
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

_source line 19 · 2026-05-19T04:30:52.016Z_

<details><summary>↩ Tool result · `toolu_01E76eDBfFc8rES9gV4ptU84`</summary>

```text
1	\section{Related Work}
2	\label{sec:related_work}
3	
4	\paragraph{Training-free LLM IE.}
5	Training-free LLM IE spans instruction tuning \cite{instructuie-2023}, code-style schema encoding \cite{knowcoder-2024,codeie-2023}, annotation-guided extraction \cite{gollie-2024,adelie-2024}, schema-driven decoding \cite{slot-2025,oneke-2025}, and constrained JSON decoding \cite{json-schema-bench-2025,willard2023efficient}. For NER, methods include zero-shot decomposition \cite{xie-zeroshot-ner-2023,promptner-2023}, distillation \cite{uniner-2024}, bidirectional encoders \cite{gliner-2024,gliner2-2025}, and fine-grained entity typing \cite{gillick-2014-entity-typing}. For RE, recent work examines zero-shot relation triplet extraction via prompting \cite{relationprompt-2022} and revisits relation extraction in the LLM era \cite{wadhwa-re-llm-2023}. These methods perform well with moderate schemas (4--20 types) but none investigates how performance degrades as schema complexity scales, nor proposes quantitative metrics for inter-type confusability. \citet{wei-2023-chatie} reformulate zero-shot IE as multi-turn QA with ChatGPT but do not analyze schema-size effects.
6	
7	\paragraph{Schema complexity in IE.}
8	The most directly related work is LLM-PEE \cite{llm-pee-2025}, which partitions large event schemas by type embedding similarity. Our work differs in three ways: (1)~we conduct controlled analysis to understand \emph{why} extraction degrades rather than developing an engineering solution; (2)~our BCS-controlled experiments isolate count from confusability, which LLM-PEE conflates; (3)~our SDGD experiments reveal that merge amplification (not partitioning quality) is the bottleneck in decompose-then-merge pipelines. LLM-PEE's union merge suffers the same precision collapse (0.56$\to$0.21 in NER) that our \S\ref{sec:sdgd} analysis identifies as the fundamental bottleneck. Other approaches address schema complexity via hard negative mining \cite{iepile-2024}, schema definition optimization \cite{parse-2025}, multi-agent debate \cite{crossagentie-2025,cmas-ner-2025}, schema-aware decomposition for event extraction \cite{dee-2024}, and active prompting \cite{reflect-learn-2026}; all treat it as an engineering problem rather than isolating the underlying degradation factors. Concurrently, \citet{chen-2026-multi-instance} show that instance count degrades LLM multi-instance processing more than context length, consistent with our count-dominant finding. Concurrently, \citet{haystack-to-needle-2025} reduces label spaces via iterative LLM filtering, \citet{dlisc-2025} caches schemas for on-device extraction, and \citet{spt-2025} treats schemas as parameterized tools. Our framework explains \emph{why} such reduction works: it implicitly lowers batch confusability.
9	
10	\paragraph{Schema complexity in dialogue and IE.} The Schema-Guided Dialogue dataset~\cite{rastogi2020towards} and SGD-X~\cite{lee2022sgd} document performance degradation with schema linguistic variation. \citet{li2023evaluating} observe count-dependent degradation in ChatGPT IE. Prompt order sensitivity \cite{lu2022fantastically} and label ordering effects are well documented; our prompt-variant experiments (\S\ref{sec:appendix_prompt_variants}) control for such artifacts. \citet{volkanovska2025ner} categorize LLM NER errors including type confusion. The relationship between label similarity and classification confusion has precedent in traditional ML: hierarchical classification suffers sibling confusion proportional to inter-class proximity \citep{deng-2010-imagenet}, label confusion matrices improve text classification \citep{guo-2021-label-confusion}, classification confusion captures semantic similarity \citep{zhou-2025-rethinking}, label smoothing exploits inter-class similarity structure \citep{muller2019when}, and human label uncertainty mirrors model confusion patterns \citep{peterson2019human}. Hierarchical label sets \citep{novack-2023-chils}, enriched type descriptions \citep{cocchieri-2025-zeroner}, and universal entity taxonomies \citep{yang2025beyond} address related problems but are orthogonal to confusability-aware batching.
11	
12	\paragraph{SCS novelty.} SCS shares its formal definition (pairwise cosine similarity of type name embeddings) with the partitioning criterion in LLM-PEE~\cite{llm-pee-2025}. The use of embedding distance for type discrimination has parallels in metric learning \citep{snell2017prototypical} and zero-shot classification \citep{yin-2019-zero-shot-bench}. Our contribution is the controlled experimental framework that isolates confusability's predictive relationship with extraction degradation. The modest pairwise $r^2$ (1.3--1.7\%) is consistent with individual-difference predictors in behavioral research \citep{cohen-1988-power,lakens-2013-effect-size} and compounds at the aggregate level. Our centrality confound (\S\ref{sec:centrality_confound}) connects to representation degeneration \cite{gao-repr-degen-2019,ethayarajh-contextual-2019}: local clusters can be isotropic \cite{cai-isotropy-clusters-2021}, explaining why MAVEN's single-ontology types conflate confusability with centrality.
13	
14	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "01931e94-4607-451b-912c-dc1178145411",
  "isSidechain": false,
  "promptId": "8257bd0e-08b4-4530-aa87-1e185ea40a51",
  "type": "user",
  "uuid": "25fa10b6-75d3-452a-a2af-23e189272c27",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/related_work.tex",
      "content": "\\section{Related Work}\n\\label{sec:related_work}\n\n\\paragraph{Training-free LLM IE.}\nTraining-free LLM IE spans instruction tuning \\cite{instructuie-2023}, code-style schema encoding \\cite{knowcoder-2024,codeie-2023}, annotation-guided extraction \\cite{gollie-2024,adelie-2024}, schema-driven decoding \\cite{slot-2025,oneke-2025}, and constrained JSON decoding \\cite{json-schema-bench-2025,willard2023efficient}. For NER, methods include zero-shot decomposition \\cite{xie-zeroshot-ner-2023,promptner-2023}, distillation \\cite{uniner-2024}, bidirectional encoders \\cite{gliner-2024,gliner2-2025}, and fine-grained entity typing \\cite{gillick-2014-entity-typing}. For RE, recent work examines zero-shot relation triplet extraction via prompting \\cite{relationprompt-2022} and revisits relation extraction in the LLM era \\cite{wadhwa-re-llm-2023}. These methods perform well with moderate schemas (4--20 types) but none investigates how performance degrades as schema complexity scales, nor proposes quantitative metrics for inter-type confusability. \\citet{wei-2023-chatie} reformulate zero-shot IE as multi-turn QA with ChatGPT but do not analyze schema-size effects.\n\n\\paragraph{Schema complexity in IE.}\nThe most directly related work is LLM-PEE \\cite{llm-pee-2025}, which partitions large event schemas by type embedding similarity. Our work differs in three ways: (1)~we conduct controlled analysis to understand \\emph{why} extraction degrades rather than developing an engineering solution; (2)~our BCS-controlled experiments isolate count from confusability, which LLM-PEE conflates; (3)~our SDGD experiments reveal that merge amplification (not partitioning quality) is the bottleneck in decompose-then-merge pipelines. LLM-PEE's union merge suffers the same precision collapse (0.56$\\to$0.21 in NER) that our \\S\\ref{sec:sdgd} analysis identifies as the fundamental bottleneck. Other approaches address schema complexity via hard negative mining \\cite{iepile-2024}, schema definition optimization \\cite{parse-2025}, multi-agent debate \\cite{crossagentie-2025,cmas-ner-2025}, schema-aware decomposition for event extraction \\cite{dee-2024}, and active prompting \\cite{reflect-learn-2026}; all treat it as an engineering problem rather than isolating the underlying degradation factors. Concurrently, \\citet{chen-2026-multi-instance} show that instance count degrades LLM multi-instance processing more than context length, consistent with our count-dominant finding. Concurrently, \\citet{haystack-to-needle-2025} reduces label spaces via iterative LLM filtering, \\citet{dlisc-2025} caches schemas for on-device extraction, and \\citet{spt-2025} treats schemas as parameterized tools. Our framework explains \\emph{why} such reduction works: it implicitly lowers batch confusability.\n\n\\paragraph{Schema complexity in dialogue and IE.} The Schema-Guided Dialogue dataset~\\cite{rastogi2020towards} and SGD-X~\\cite{lee2022sgd} document performance degradation with schema linguistic variation. \\citet{li2023evaluating} observe count-dependent degradation in ChatGPT IE. Prompt order sensitivity \\cite{lu2022fantastically} and label ordering effects are well documented; our prompt-variant experiments (\\S\\ref{sec:appendix_prompt_variants}) control for such artifacts. \\citet{volkanovska2025ner} categorize LLM NER errors including type confusion. The relationship between label similarity and classification confusion has precedent in traditional ML: hierarchical classification suffers sibling confusion proportional to inter-class proximity \\citep{deng-2010-imagenet}, label confusion matrices improve text classification \\citep{guo-2021-label-confusion}, classification confusion captures semantic similarity \\citep{zhou-2025-rethinking}, label smoothing exploits inter-class similarity structure \\citep{muller2019when}, and human label uncertainty mirrors model confusion patterns \\citep{peterson2019human}. Hierarchical label sets \\citep{novack-2023-chils}, enriched type descriptions \\citep{cocchieri-2025-zeroner}, and universal entity taxonomies \\citep{yang2025beyond} address related problems but are orthogonal to confusability-aware batching.\n\n\\paragraph{SCS novelty.} SCS shares its formal definition (pairwise cosine similarity of type name embeddings) with the partitioning criterion in LLM-PEE~\\cite{llm-pee-2025}. The use of embedding distance for type discrimination has parallels in metric learning \\citep{snell2017prototypical} and zero-shot classification \\citep{yin-2019-zero-shot-bench}. Our contribution is the controlled experimental framework that isolates confusability's predictive relationship with extraction degradation. The modest pairwise $r^2$ (1.3--1.7\\%) is consistent with individual-difference predictors in behavioral research \\citep{cohen-1988-power,lakens-2013-effect-size} and compounds at the aggregate level. Our centrality confound (\\S\\ref{sec:centrality_confound}) connects to representation degeneration \\cite{gao-repr-degen-2019,ethayarajh-contextual-2019}: local clusters can be isotropic \\cite{cai-isotropy-clusters-2021}, explaining why MAVEN's single-ontology types conflate confusability with centrality.\n\n",
      "numLines": 14,
      "startLine": 1,
      "totalLines": 14
    }
  },
  "sourceToolAssistantUUID": "01931e94-4607-451b-912c-dc1178145411",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_reviewer_2_302b64f9",
  "sessionId": "0ff1fe81-4731-4c76-91b4-02652701ddff",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Tool call

_source line 20 · 2026-05-19T04:30:52.076Z_

<details open><summary>🔧 Tool call — Read · `toolu_01VcLC3H7MmEz6rkSFgw1ZPq`</summary>

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
  "parentUuid": "25fa10b6-75d3-452a-a2af-23e189272c27",
  "isSidechain": false,
  "requestId": "req_011CbBJL3Mfp6QVPxgqBTm4o",
  "type": "assistant",
  "uuid": "513998b6-cb6b-44db-ad18-7249e53974ef",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_reviewer_2_302b64f9",
  "sessionId": "0ff1fe81-4731-4c76-91b4-02652701ddff",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PMdzHtBXazYPW4S8Z616zu",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2278,
      "cache_read_input_tokens": 28070,
      "output_tokens": 849,
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
          "output_tokens": 849,
          "cache_read_input_tokens": 28070,
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

_source line 21 · 2026-05-19T04:30:52.084Z_

<details><summary>↩ Tool result · `toolu_01VcLC3H7MmEz6rkSFgw1ZPq`</summary>

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
10	Few-NERD \cite{fewnerd-2021} provides 66 fine-grained entity types organized into 8 coarse categories (person, location, organization, building, art, product, event, other). The dataset spans diverse domains and is suitable for cross-domain evaluation. We sample 1{,}000 test instances uniformly across test instances; type frequency follows the natural long-tail distribution of Few-NERD. Evaluation uses token-level text matching. Pairwise analysis covers 1{,}953 type pairs with non-zero co-occurrence out of $\binom{66}{2}=2{,}145$ possible pairs.
11	
12	\paragraph{FewRel (RE).}
13	FewRel \cite{fewrel-2018} contains 80 relation types sourced from Wikidata. Since the validation split covers only 16 relations, we combine the training and validation splits to obtain the full 80-relation pool required for schema-scale experiments, and sample 1{,}000 balanced instances (12--13 per relation type, stratified to ensure equal representation). Each instance provides a sentence with marked head and tail entities; the task is to classify the relation. FewRel's balanced design (700 instances per relation type) eliminates type frequency as a potential confound; this balance makes it the primary dataset for BCS analysis.
14	
15	\paragraph{DocRED (Document-level RE).}
16	DocRED \cite{docred-2019} contains 96 relation types sourced from Wikidata, evaluated at the document level where entity pairs may span multiple sentences. We sample 1{,}000 instances balanced across 96 relation types ($\sim$10 per type) from the DocRED development set and formulate the task identically to FewRel: given a document with marked head and tail entities, classify the relation. DocRED extends the RE evaluation to a larger schema (96 vs.\ 80 types) and document-level context, testing whether confusability effects persist under longer input contexts and cross-sentence reasoning.
17	
18	\paragraph{MAVEN (ED).}
19	MAVEN \cite{maven-2020} defines 168 event types derived from the FrameNet ontology; all types belong to a single ontology (FrameNet), so this is a same-domain schema. We use the validation set (8{,}042 sentences containing 18{,}904 event mentions) for evaluation, as test set labels are not publicly available. The task requires both trigger identification and event type classification. MAVEN serves a supplementary role because its same-domain schema produces centrality confounds at the batch level (\S\ref{sec:centrality_confound}).
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
37	\caption{Dataset statistics. BCS Range: min--max over count-curve batches. Embedding: model used for SCS/BCS; ranges are not comparable across embedding models. $^\dagger$Trigger mentions across 8{,}042 sentences.}
38	\label{tab:datasets}
39	\end{table}
40	
41	\subsection{Schema Confusability Score (SCS)}
42	\label{sec:scs}
43	
44	We define the Schema Confusability Score (SCS) to quantify semantic overlap between types in a schema. Given a type $t$ with name string $\text{name}(t)$, an embedding function $\text{embed}(\cdot)$ maps the type name to a vector representation. The \textbf{pairwise SCS} between types $t_i$ and $t_j$ is:
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
60	SCS is a pre-hoc proxy computable without running extraction. Pairwise SCS correlates with observed type confusion (Few-NERD $r = 0.112$, FewRel $r = 0.187$, both $p < 0.001$; Table~\ref{tab:pairwise}), though context, frequency, and definition quality also contribute (\S\ref{sec:pairwise}).
61	
62	\subsection{Experimental Design}
63	\label{sec:exp_design}
64	
65	We conduct two complementary experimental paradigms.
66	
67	\paragraph{Experiment 1: Count Curves.}
68	We vary the number of types presented in the prompt schema to measure performance as a function of schema size. For each count level, we sample 25 random type batches for Few-NERD and FewRel (5 for DocRED and MAVEN)\footnote{DocRED and MAVEN use fewer batches due to higher per-batch evaluation cost (document-level RE and 8{,}042 sentences, respectively).} and evaluate the same 1{,}000 test samples across all batches. At count${}=1$, every type is evaluated individually as a solo baseline. The remaining count levels follow natural partition points in each schema's type hierarchy rather than uniform spacing: \{2, 6, 12, 22, 44, 66\} for Few-NERD, \{4, 8, 16, 32, 40, 64, 80\} for FewRel, \{4, 8, 16, 32, 64, 96\} for DocRED, and \{6, 12, 22, 44, 64\} for MAVEN.
69	
70	\paragraph{Experiment 2: BCS-Controlled.}
71	We fix type count and vary BCS to isolate confusability from schema size. For each count level, we construct one low-BCS batch, one high-BCS batch, and 25 random batches (27 total). We evaluate on Few-NERD (count$\,\in\{6, 12\}$), FewRel (count$\,\in\{8, 16\}$, both 16-relation (pilot) and 80-relation pools), and DocRED (count$\,\in\{16, 32\}$). Within-pool 16-relation subsets from the 80-relation pool isolate confusability from pool composition. MAVEN results are reported separately due to a centrality confound (\S\ref{sec:centrality_confound}).
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
82	We use Qwen3-32B-FP8 \cite{qwen3-2025} served via vLLM v0.20.2 \cite{vllm-2023} on a single NVIDIA RTX PRO 6000 GPU (96\,GB) with greedy decoding (temperature${}\,=\,0$, seed 42). Two NER/ED prompt versions are evaluated: v1 requests character offsets (evaluated via text matching); v2 adds format constraints that double precision with minimal recall loss. RE uses a single prompt version throughout. Both versions produce consistent degradation patterns; we report both where applicable to quantify formatting sensitivity \cite{sclar-sensitivity-2024} (templates in Appendix~\ref{sec:appendix_prompts}). Cross-model validation uses Meta-Llama-3.1-70B-Instruct (FP8) and Meta-Llama-3.1-8B-Instruct \cite{llama3-2024}. All experiments use single-seed evaluation with greedy decoding, which substantially reduces model-level randomness (residual SD = 0.88\,pp at count 80 under greedy decoding, likely attributable to FP8 quantization non-determinism); bootstrap CIs capture the remaining sampling variance from batch composition. Pair-level CIs use percentile bootstrap ($B{=}10{,}000$); batch-level CIs use $B{=}1{,}000$.
83	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "513998b6-cb6b-44db-ad18-7249e53974ef",
  "isSidechain": false,
  "promptId": "8257bd0e-08b4-4530-aa87-1e185ea40a51",
  "type": "user",
  "uuid": "08d6c7c6-915a-47f0-8789-3867e221bb84",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/experimental_setup.tex",
      "content": "\\section{Experimental Setup}\n\\label{sec:experimental_setup}\n\nWe evaluate how prompt schema size and inter-type confusability affect zero-shot LLM extraction across three information extraction tasks and four datasets: named entity recognition (NER), sentence-level relation extraction (RE), document-level RE, and event detection (ED).\n\n\\subsection{Tasks and Datasets}\n\\label{sec:datasets}\n\n\\paragraph{Few-NERD (NER).}\nFew-NERD \\cite{fewnerd-2021} provides 66 fine-grained entity types organized into 8 coarse categories (person, location, organization, building, art, product, event, other). The dataset spans diverse domains and is suitable for cross-domain evaluation. We sample 1{,}000 test instances uniformly across test instances; type frequency follows the natural long-tail distribution of Few-NERD. Evaluation uses token-level text matching. Pairwise analysis covers 1{,}953 type pairs with non-zero co-occurrence out of $\\binom{66}{2}=2{,}145$ possible pairs.\n\n\\paragraph{FewRel (RE).}\nFewRel \\cite{fewrel-2018} contains 80 relation types sourced from Wikidata. Since the validation split covers only 16 relations, we combine the training and validation splits to obtain the full 80-relation pool required for schema-scale experiments, and sample 1{,}000 balanced instances (12--13 per relation type, stratified to ensure equal representation). Each instance provides a sentence with marked head and tail entities; the task is to classify the relation. FewRel's balanced design (700 instances per relation type) eliminates type frequency as a potential confound; this balance makes it the primary dataset for BCS analysis.\n\n\\paragraph{DocRED (Document-level RE).}\nDocRED \\cite{docred-2019} contains 96 relation types sourced from Wikidata, evaluated at the document level where entity pairs may span multiple sentences. We sample 1{,}000 instances balanced across 96 relation types ($\\sim$10 per type) from the DocRED development set and formulate the task identically to FewRel: given a document with marked head and tail entities, classify the relation. DocRED extends the RE evaluation to a larger schema (96 vs.\\ 80 types) and document-level context, testing whether confusability effects persist under longer input contexts and cross-sentence reasoning.\n\n\\paragraph{MAVEN (ED).}\nMAVEN \\cite{maven-2020} defines 168 event types derived from the FrameNet ontology; all types belong to a single ontology (FrameNet), so this is a same-domain schema. We use the validation set (8{,}042 sentences containing 18{,}904 event mentions) for evaluation, as test set labels are not publicly available. The task requires both trigger identification and event type classification. MAVEN serves a supplementary role because its same-domain schema produces centrality confounds at the batch level (\\S\\ref{sec:centrality_confound}).\n\nTable~\\ref{tab:datasets} summarizes the dataset statistics, including the Schema Confusability Score (SCS) ranges defined in \\S\\ref{sec:scs}.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llrrlll}\n\\toprule\n\\textbf{Dataset} & \\textbf{Task} & \\textbf{\\# Types} & \\textbf{\\# Eval Units} & \\textbf{Domain} & \\textbf{BCS Range} & \\textbf{Embedding} \\\\\n\\midrule\nFew-NERD & NER & 66 & 1{,}000 & Cross & 0.77--0.93 & Qwen3-32B \\\\\nFewRel & RE (sent.) & 80 & 1{,}000 & Cross & 0.42--0.97 & MiniLM \\\\\nDocRED & RE (doc.) & 96 & 1{,}000 & Cross & 0.53--0.73 & MiniLM \\\\\nMAVEN & ED & 168 & 18{,}904\\rlap{$^\\dagger$} & Same & 0.87--0.97 & MiniLM \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Dataset statistics. BCS Range: min--max over count-curve batches. Embedding: model used for SCS/BCS; ranges are not comparable across embedding models. $^\\dagger$Trigger mentions across 8{,}042 sentences.}\n\\label{tab:datasets}\n\\end{table}\n\n\\subsection{Schema Confusability Score (SCS)}\n\\label{sec:scs}\n\nWe define the Schema Confusability Score (SCS) to quantify semantic overlap between types in a schema. Given a type $t$ with name string $\\text{name}(t)$, an embedding function $\\text{embed}(\\cdot)$ maps the type name to a vector representation. The \\textbf{pairwise SCS} between types $t_i$ and $t_j$ is:\n{\\small\n\\[\n\\text{SCS}(t_i, t_j) = \\cos\\bigl(\\text{embed}(\\text{name}(t_i)),\\; \\text{embed}(\\text{name}(t_j))\\bigr)\n\\]\n}\n\nFor a batch of types $B = \\{t_1, \\ldots, t_k\\}$, the \\textbf{Batch Confusability Score (BCS)} aggregates all pairwise similarities:\n\\[\n\\text{BCS}(B) = \\frac{1}{\\binom{k}{2}} \\sum_{i < j,\\; t_i, t_j \\in B} \\text{SCS}(t_i, t_j)\n\\]\n\nWe compute SCS with two embedding models: (1)~Qwen3-32B \\cite{qwen3-2025} hidden-state representations (5{,}120-d), which capture the extraction model's own type representations, and (2)~all-MiniLM-L6-v2 \\cite{minilm-2020,sentence-bert-2019}, a 384-dimensional general-purpose sentence encoder. Few-NERD uses Qwen3 embeddings because its 66 fine-grained types include same-category pairs (e.g., ``person-artist'' vs.\\ ``person-actor'') that MiniLM's 384-d space does not separate well; a cross-embedding check confirms directional consistency (MiniLM $r = 0.172$, Qwen3 $r = 0.138$; Appendix~\\ref{sec:appendix_bcs_sensitivity}). SCS uses name-only embeddings as a practical simplification. We validate this choice empirically: name+definition SCS yields equivalent predictive accuracy ($\\Delta r$: $-0.023$ to $+0.035$; Appendix~\\ref{app:scs-ablation}), and for MAVEN/FewRel prompts that use type names without definitions, name-only SCS directly matches prompt content. We use MiniLM as the primary embedding for BCS computation because sentence-transformers are specifically trained for semantic similarity \\cite{sentence-bert-2019}; a cross-embedding sensitivity check using Qwen3-32B causal-LM hidden states confirms directional consistency but with compressed BCS range (std${}\\,=\\,0.034$ vs.\\ MiniLM std${}\\,=\\,0.081$), consistent with known autoregressive anisotropy \\cite{ethayarajh-contextual-2019}.\n\n\\paragraph{SCS as a lightweight proxy.}\n\\label{sec:scs-validation}\nSCS is a pre-hoc proxy computable without running extraction. Pairwise SCS correlates with observed type confusion (Few-NERD $r = 0.112$, FewRel $r = 0.187$, both $p < 0.001$; Table~\\ref{tab:pairwise}), though context, frequency, and definition quality also contribute (\\S\\ref{sec:pairwise}).\n\n\\subsection{Experimental Design}\n\\label{sec:exp_design}\n\nWe conduct two complementary experimental paradigms.\n\n\\paragraph{Experiment 1: Count Curves.}\nWe vary the number of types presented in the prompt schema to measure performance as a function of schema size. For each count level, we sample 25 random type batches for Few-NERD and FewRel (5 for DocRED and MAVEN)\\footnote{DocRED and MAVEN use fewer batches due to higher per-batch evaluation cost (document-level RE and 8{,}042 sentences, respectively).} and evaluate the same 1{,}000 test samples across all batches. At count${}=1$, every type is evaluated individually as a solo baseline. The remaining count levels follow natural partition points in each schema's type hierarchy rather than uniform spacing: \\{2, 6, 12, 22, 44, 66\\} for Few-NERD, \\{4, 8, 16, 32, 40, 64, 80\\} for FewRel, \\{4, 8, 16, 32, 64, 96\\} for DocRED, and \\{6, 12, 22, 44, 64\\} for MAVEN.\n\n\\paragraph{Experiment 2: BCS-Controlled.}\nWe fix type count and vary BCS to isolate confusability from schema size. For each count level, we construct one low-BCS batch, one high-BCS batch, and 25 random batches (27 total). We evaluate on Few-NERD (count$\\,\\in\\{6, 12\\}$), FewRel (count$\\,\\in\\{8, 16\\}$, both 16-relation (pilot) and 80-relation pools), and DocRED (count$\\,\\in\\{16, 32\\}$). Within-pool 16-relation subsets from the 80-relation pool isolate confusability from pool composition. MAVEN results are reported separately due to a centrality confound (\\S\\ref{sec:centrality_confound}).\n\n\\subsection{Evaluation Metrics}\n\\label{sec:metrics}\n\n\\textbf{NER}: text-match F1, where a prediction is correct if the exact text string matches after lowercasing and whitespace normalization, \\emph{and} the type matches; partial spans count as incorrect. \\textbf{RE}: accuracy (exact match of predicted relation label to gold). \\textbf{ED}: relaxed F1, where any token overlap between predicted and gold trigger spans, with correct event type.\n\n\n\\subsection{Model and Inference}\n\\label{sec:model}\n\nWe use Qwen3-32B-FP8 \\cite{qwen3-2025} served via vLLM v0.20.2 \\cite{vllm-2023} on a single NVIDIA RTX PRO 6000 GPU (96\\,GB) with greedy decoding (temperature${}\\,=\\,0$, seed 42). Two NER/ED prompt versions are evaluated: v1 requests character offsets (evaluated via text matching); v2 adds format constraints that double precision with minimal recall loss. RE uses a single prompt version throughout. Both versions produce consistent degradation patterns; we report both where applicable to quantify formatting sensitivity \\cite{sclar-sensitivity-2024} (templates in Appendix~\\ref{sec:appendix_prompts}). Cross-model validation uses Meta-Llama-3.1-70B-Instruct (FP8) and Meta-Llama-3.1-8B-Instruct \\cite{llama3-2024}. All experiments use single-seed evaluation with greedy decoding, which substantially reduces model-level randomness (residual SD = 0.88\\,pp at count 80 under greedy decoding, likely attributable to FP8 quantization non-determinism); bootstrap CIs capture the remaining sampling variance from batch composition. Pair-level CIs use percentile bootstrap ($B{=}10{,}000$); batch-level CIs use $B{=}1{,}000$.\n",
      "numLines": 83,
      "startLine": 1,
      "totalLines": 83
    }
  },
  "sourceToolAssistantUUID": "513998b6-cb6b-44db-ad18-7249e53974ef",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_reviewer_2_302b64f9",
  "sessionId": "0ff1fe81-4731-4c76-91b4-02652701ddff",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Tool call

_source line 22 · 2026-05-19T04:30:52.199Z_

<details open><summary>🔧 Tool call — Read · `toolu_01JitX2XEtt71obqsVBdpnED`</summary>

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
  "parentUuid": "08d6c7c6-915a-47f0-8789-3867e221bb84",
  "isSidechain": false,
  "requestId": "req_011CbBJL3Mfp6QVPxgqBTm4o",
  "type": "assistant",
  "uuid": "8877d4a2-5151-464d-ad8a-a49bd498e02a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_reviewer_2_302b64f9",
  "sessionId": "0ff1fe81-4731-4c76-91b4-02652701ddff",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PMdzHtBXazYPW4S8Z616zu",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2278,
      "cache_read_input_tokens": 28070,
      "output_tokens": 849,
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
          "output_tokens": 849,
          "cache_read_input_tokens": 28070,
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

_source line 23 · 2026-05-19T04:30:52.205Z_

<details><summary>↩ Tool result · `toolu_01JitX2XEtt71obqsVBdpnED`</summary>

```text
1	\section{Results}
2	\label{sec:results}
3	
4	Unless otherwise noted, all experiments in this section use the v1 prompt (\S\ref{sec:model}; full templates in Appendix~\ref{sec:appendix_prompts}).
5	
6	\subsection{Count-Degradation Curves}
7	\label{sec:count_curves}
8	
9	\begin{figure*}[t]
10	\centering
11	\begin{minipage}[t]{0.48\textwidth}
12	\centering
13	\includegraphics[width=\linewidth]{../../figures/paper/fig_count_curves.pdf}
14	\end{minipage}
15	\hfill
16	\begin{minipage}[t]{0.48\textwidth}
17	\centering
18	\includegraphics[width=\linewidth]{../../figures/paper/fig_bcs_scaling.pdf}
19	\end{minipage}
20	\caption{\textbf{(a)} Count-degradation curves. Error bars: $\pm 1$\,SD across 3 seeds $\times$ 25 batches. RE declines monotonically; NER shows a U-shape. Hollow markers: full-schema (no sampling variance). \textbf{(b)} BCS-controlled FewRel accuracy. Slopes are consistent across the independent and within-pool 16-relation conditions ($p = 0.60$); wider BCS range at 80 relations produces larger gaps.}
21	\label{fig:main_results}
22	\end{figure*}
23	
24	Figure~\ref{fig:main_results}a shows RE accuracy declines monotonically with schema size (0.86$\to$0.50 for FewRel). NER recall declines through intermediate counts (0.51$\to$0.27, plateauing across counts 22--44) before partial recovery at full-schema (0.41), where the elimination of type-filtering overhead restores extraction performance. DocRED replicates the monotonic RE pattern (88.0\%$\to$38.7\%, $-$56\%; Appendix). MAVEN exhibits a reversed trend attributable to centrality confounding (\S\ref{sec:centrality_confound}). The effect replicates on Llama-3.1-8B-Instruct ($-$43\,pp on Few-NERD; per-batch $r = 0.725$; Table~\ref{tab:cross_model}). The pattern is stable across three seeds (max $\Delta = 10.7$\,pp, within 1\,SD; intra-batch variance exceeds inter-seed variance by ${>}$5$\times$; Appendix~\ref{app:variance-decomposition}). Formal trend analysis confirms monotonic RE decline (Jonckheere-Terpstra $J = 109{,}707$, $p < 0.001$). Count curves establish trend direction; magnitude estimation relies on the higher-powered BCS-controlled experiments (\S\ref{sec:bcs_controlled}).
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
43	\caption{Pairwise SCS--confusion correlation. Confusion rate is bidirectional $C(t_i{\to}t_j) + C(t_j{\to}t_i)$ divided by gold frequency sum; CIs are percentile bootstrap ($B{=}10{,}000$). FewRel ($r = 0.187$; \S\ref{sec:scs-validation}) excluded (per-instance RE format). Type-level cluster bootstrap CIs exclude zero (Few-NERD [0.069, 0.219]; MAVEN [0.081, 0.185]).}
44	\label{tab:pairwise}
45	\end{table}
46	
47	The correlations are statistically significant but modest: $r^2 \approx 1.3\text{--}1.7\%$. Type-level cluster bootstrap yields wider but still significant CIs (Few-NERD: [0.069, 0.219]; MAVEN: [0.081, 0.185]; $B = 10{,}000$). Spearman correlations corroborate: $\rho = 0.144\text{--}0.227$ across all pairs, strengthening to $\rho = 0.27\text{--}0.31$ among pairs with nonzero confusion (though conditioning on the dependent variable may inflate this).
48	
49	The remaining variance likely reflects entity frequency, prompt position \cite{lost-in-middle-2024}, mention ambiguity, and definition quality. Although pairwise $r^2$ is modest, the signal compounds at the batch level into quartile gaps of 3.9--5.3\,pp under typical batching (\S\ref{sec:practical_magnitude}). The independent MiniLM embedding yields a \emph{stronger} SCS--confusion correlation on Few-NERD ($r = 0.172$ vs.\ Qwen3 $r = 0.138$; Appendix), indicating that shared-representation bias is conservative rather than inflationary. SCS also outperforms simpler baselines (Levenshtein, WordNet Wu-Palmer, same-parent) on pairwise confusion prediction (Appendix~\ref{app:scs-baselines}). Appendix~\ref{app:error-analysis} lists the most confusable type pairs and provides concrete confusion examples.
50	
51	\subsection{BCS-Controlled Experiments}
52	\label{sec:bcs_controlled}
53	
54	We fix type count and vary BCS. FewRel's balanced design (700 instances per type) eliminates type frequency as a confound; the within-pool analysis (\S\ref{sec:within_pool}) controls for pool composition.
55	
56	In BCS-controlled FewRel subsets, the high-BCS quartile shows $\Delta=-5.3$\,pp lower accuracy than low-BCS (quartile comparison on 100 random batches; based on a single extreme batch per BCS level at 16-rel scale; full data in Appendix~\ref{app:bcs-controlled-table}). At 80 relations, extreme-batch construction amplifies this to $-$31.2\,pp (CI: [17.7, 42.7]), stable across count levels. An intermediate count${}\,=\,40$ evaluation (40-relation subsets sampled from the 80-relation pool) yields consistent gaps ($-$33.3\,pp at count 8, $-$31.8\,pp at count 16) and confirms monotonic decline.
57	
58	\paragraph{Document-level RE (DocRED).}
59	The effect replicates on DocRED's 96-relation schema: BCS gap $-$23.3\,pp at count 16 (slope $= -0.713$, $\rho = -0.661$, $p < 0.001$) and $-$17.6\,pp at count 32 (slope $= -0.690$, $\rho = -0.509$, $p = 0.002$). BCS explains 44--53\% of cross-batch variance ($R^2 = 0.525$ at count 16, $n = 35$; 95\% CI [0.27, 0.73]), substantially higher than FewRel ($R^2 = 0.218$), possibly reflecting a wider confusability range in the DocRED schema, though document-level context may also provide richer cues for type confusion. Across all RE settings, BCS slopes range from $-$0.40 to $-$0.71, significant in all conditions with sufficient BCS range.
60	
61	\paragraph{Within-pool controlled comparison.}
62	\label{sec:within_pool}
63	Within-pool analysis confirms slope consistency across pools (permutation $p \approx 0.60$; Appendix~\ref{app:within-pool-method}). The 80-relation extreme-batch gap (\S\ref{sec:bcs_controlled}) reflects wider BCS range, not stronger per-unit sensitivity.
64	
65	\paragraph{Practical magnitude.}
66	\label{sec:practical_magnitude}
67	Direct regression on 100 random 16-type batches from the 80-relation pool shows BCS explains 22\% of cross-batch accuracy variance ($R^2 = 0.218$, $p < 0.001$), scaling to 53\% at DocRED 96-rel. The typical BCS span (IQR = 0.054) yields an expected accuracy gap of 2.2\,pp (95\% CI: [0.4, 4.0]). Quartile comparison confirms: bottom-quartile BCS batches average 82.8\% vs.\ 78.9\% for top-quartile ($\Delta = 3.9$\,pp). A post-hoc Monte Carlo simulation confirms the ${\sim}3\times$ pair-to-batch amplification (Appendix~\ref{app:aggregation-sim}).
68	
69	\paragraph{Cross-model validation.}
70	The effect replicates on Meta-Llama-3.1-8B-Instruct: BCS gaps of $-$27.1\,pp (count 8) and $-$23.9\,pp (count 16), reaching 77--87\% of Qwen3-32B's gap. Both models converge to $\approx$51\% under high confusability, suggesting a task-inherent difficulty floor (Table~\ref{tab:cross_model_bcs}). Dimension~1 replicates fully on Llama-3.1-8B (\S\ref{sec:count_curves}); Dimension~2 replicates on RE but shows floor effects on 8B NER (Limitations, item~1). Llama-3.1-70B-Instruct (FP8) and Gemini 2.5 Flash (API) confirm directional consistency across scales and families (Appendix~\ref{sec:appendix_cross_model_70b}, \ref{sec:appendix_cross_model_gemini}).
71	
72	\paragraph{Prompt sensitivity.}
73	Under the v2 prompt, the extreme-batch BCS gap is $-$25.5\,pp ($r = -0.919$, $p < 0.001$; $n{=}25$), modestly attenuated from v1 but highly significant. NER shows no batch-level BCS--F1 correlation under either prompt ($r \approx 0$, $n = 450$; \S\ref{sec:multi_channel}). The effect holds across four structurally distinct prompt variants at count 32 (all $r \leq -0.47$; Appendix~\ref{sec:appendix_prompt_variants}), ruling out prompt design as the source.
74	
75	\subsection{Multi-Dimensional Degradation}
76	\label{sec:multi_channel}
77	
78	\begin{figure*}[t]
79	\centering
80	\includegraphics[width=\textwidth]{../../figures/paper/fig_error_taxonomy.pdf}
81	\caption{Error taxonomy decomposition. IntraSub scales monotonically with BCS in both tasks. RE missed rates remain flat (10--16\%), but NER missed rates are substantially higher (43--65\%) and non-monotonic.}
82	\label{fig:error_taxonomy}
83	\end{figure*}
84	
85	Error taxonomy decomposition (Table~\ref{tab:error_taxonomy} and Figure~\ref{fig:error_taxonomy}) shows intra-batch substitution (IntraSub) scales monotonically with BCS: $\rho = 1.0$ ($p < 0.001$) for NER and $\rho = 0.954$ ($p < 0.001$) for RE. In NER, missed rates are higher (43--65\%) and non-monotonic; confusable types impair entity detection itself. Extreme-BCS batches produce $9.9\text{--}27.5\times$ more confusion than low-BCS batches.
86	
87	These results establish two dimensions: \textbf{Dimension~1} (count predicts recall decline) and \textbf{Dimension~2} (confusability predicts type confusion). The full-range regression ($n = 69$, five count levels) serves as the primary separability test; the $2 \times 2$ factorial ($n = 54$) as a sensitivity check. TOST \citep{lakens-2017-equivalence,schuirmann-1987-tost} on FewRel at $\pm 3$\,pp yields $p = 0.003$ and at $\pm 2$\,pp yields $p = 0.047$, though equivalence below 2\,pp is inconclusive ($p = 0.278$; logit-scale also inconclusive, $p = 0.209$; Appendix~\ref{sec:appendix_factorial}). On DocRED, the interaction is larger (+5.7\,pp, 95\% CI [$-$1.6, 13.0]; $\pm$3\,pp TOST $p = 0.77$), possibly reflecting baseline compression at higher type counts; we restrict the bounded-interaction claim to sentence-level RE. In NER, batch-level BCS shows no predictive signal (\S\ref{sec:bcs_controlled}), preventing clean dimension separation; the factorial test is inconclusive ($p = 0.50$).
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
  "parentUuid": "8877d4a2-5151-464d-ad8a-a49bd498e02a",
  "isSidechain": false,
  "promptId": "8257bd0e-08b4-4530-aa87-1e185ea40a51",
  "type": "user",
  "uuid": "c1434d8b-c2eb-45af-8f3c-ecb2b1f47aec",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex",
      "content": "\\section{Results}\n\\label{sec:results}\n\nUnless otherwise noted, all experiments in this section use the v1 prompt (\\S\\ref{sec:model}; full templates in Appendix~\\ref{sec:appendix_prompts}).\n\n\\subsection{Count-Degradation Curves}\n\\label{sec:count_curves}\n\n\\begin{figure*}[t]\n\\centering\n\\begin{minipage}[t]{0.48\\textwidth}\n\\centering\n\\includegraphics[width=\\linewidth]{../../figures/paper/fig_count_curves.pdf}\n\\end{minipage}\n\\hfill\n\\begin{minipage}[t]{0.48\\textwidth}\n\\centering\n\\includegraphics[width=\\linewidth]{../../figures/paper/fig_bcs_scaling.pdf}\n\\end{minipage}\n\\caption{\\textbf{(a)} Count-degradation curves. Error bars: $\\pm 1$\\,SD across 3 seeds $\\times$ 25 batches. RE declines monotonically; NER shows a U-shape. Hollow markers: full-schema (no sampling variance). \\textbf{(b)} BCS-controlled FewRel accuracy. Slopes are consistent across the independent and within-pool 16-relation conditions ($p = 0.60$); wider BCS range at 80 relations produces larger gaps.}\n\\label{fig:main_results}\n\\end{figure*}\n\nFigure~\\ref{fig:main_results}a shows RE accuracy declines monotonically with schema size (0.86$\\to$0.50 for FewRel). NER recall declines through intermediate counts (0.51$\\to$0.27, plateauing across counts 22--44) before partial recovery at full-schema (0.41), where the elimination of type-filtering overhead restores extraction performance. DocRED replicates the monotonic RE pattern (88.0\\%$\\to$38.7\\%, $-$56\\%; Appendix). MAVEN exhibits a reversed trend attributable to centrality confounding (\\S\\ref{sec:centrality_confound}). The effect replicates on Llama-3.1-8B-Instruct ($-$43\\,pp on Few-NERD; per-batch $r = 0.725$; Table~\\ref{tab:cross_model}). The pattern is stable across three seeds (max $\\Delta = 10.7$\\,pp, within 1\\,SD; intra-batch variance exceeds inter-seed variance by ${>}$5$\\times$; Appendix~\\ref{app:variance-decomposition}). Formal trend analysis confirms monotonic RE decline (Jonckheere-Terpstra $J = 109{,}707$, $p < 0.001$). Count curves establish trend direction; magnitude estimation relies on the higher-powered BCS-controlled experiments (\\S\\ref{sec:bcs_controlled}).\n\n\\subsection{Pairwise Confusability and Type Confusion}\n\\label{sec:pairwise}\n\nWe test whether pairwise SCS predicts type-level confusion rates. For each type pair $(t_i, t_j)$, we compute the confusion rate (the fraction of $t_i$ gold instances misclassified as $t_j$) and correlate it with $\\text{SCS}(t_i, t_j)$. Table~\\ref{tab:pairwise} reports Pearson correlations with bootstrap 95\\% CIs.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llrrrrr}\n\\toprule\n\\textbf{Dataset} & \\textbf{Embed.} & \\textbf{$n$ pairs} & \\textbf{$r$} & \\textbf{$r^2$} & \\textbf{95\\% CI} & \\textbf{$p$} \\\\\n\\midrule\nFew-NERD & Qwen3 & 1{,}953 & 0.112 & 0.013 & {[}0.076, 0.156{]} & ${<}\\,0.001$ \\\\\nMAVEN & MiniLM & 11{,}026 & 0.129 & 0.017 & {[}0.104, 0.156{]} & ${<}\\,0.001$ \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Pairwise SCS--confusion correlation. Confusion rate is bidirectional $C(t_i{\\to}t_j) + C(t_j{\\to}t_i)$ divided by gold frequency sum; CIs are percentile bootstrap ($B{=}10{,}000$). FewRel ($r = 0.187$; \\S\\ref{sec:scs-validation}) excluded (per-instance RE format). Type-level cluster bootstrap CIs exclude zero (Few-NERD [0.069, 0.219]; MAVEN [0.081, 0.185]).}\n\\label{tab:pairwise}\n\\end{table}\n\nThe correlations are statistically significant but modest: $r^2 \\approx 1.3\\text{--}1.7\\%$. Type-level cluster bootstrap yields wider but still significant CIs (Few-NERD: [0.069, 0.219]; MAVEN: [0.081, 0.185]; $B = 10{,}000$). Spearman correlations corroborate: $\\rho = 0.144\\text{--}0.227$ across all pairs, strengthening to $\\rho = 0.27\\text{--}0.31$ among pairs with nonzero confusion (though conditioning on the dependent variable may inflate this).\n\nThe remaining variance likely reflects entity frequency, prompt position \\cite{lost-in-middle-2024}, mention ambiguity, and definition quality. Although pairwise $r^2$ is modest, the signal compounds at the batch level into quartile gaps of 3.9--5.3\\,pp under typical batching (\\S\\ref{sec:practical_magnitude}). The independent MiniLM embedding yields a \\emph{stronger} SCS--confusion correlation on Few-NERD ($r = 0.172$ vs.\\ Qwen3 $r = 0.138$; Appendix), indicating that shared-representation bias is conservative rather than inflationary. SCS also outperforms simpler baselines (Levenshtein, WordNet Wu-Palmer, same-parent) on pairwise confusion prediction (Appendix~\\ref{app:scs-baselines}). Appendix~\\ref{app:error-analysis} lists the most confusable type pairs and provides concrete confusion examples.\n\n\\subsection{BCS-Controlled Experiments}\n\\label{sec:bcs_controlled}\n\nWe fix type count and vary BCS. FewRel's balanced design (700 instances per type) eliminates type frequency as a confound; the within-pool analysis (\\S\\ref{sec:within_pool}) controls for pool composition.\n\nIn BCS-controlled FewRel subsets, the high-BCS quartile shows $\\Delta=-5.3$\\,pp lower accuracy than low-BCS (quartile comparison on 100 random batches; based on a single extreme batch per BCS level at 16-rel scale; full data in Appendix~\\ref{app:bcs-controlled-table}). At 80 relations, extreme-batch construction amplifies this to $-$31.2\\,pp (CI: [17.7, 42.7]), stable across count levels. An intermediate count${}\\,=\\,40$ evaluation (40-relation subsets sampled from the 80-relation pool) yields consistent gaps ($-$33.3\\,pp at count 8, $-$31.8\\,pp at count 16) and confirms monotonic decline.\n\n\\paragraph{Document-level RE (DocRED).}\nThe effect replicates on DocRED's 96-relation schema: BCS gap $-$23.3\\,pp at count 16 (slope $= -0.713$, $\\rho = -0.661$, $p < 0.001$) and $-$17.6\\,pp at count 32 (slope $= -0.690$, $\\rho = -0.509$, $p = 0.002$). BCS explains 44--53\\% of cross-batch variance ($R^2 = 0.525$ at count 16, $n = 35$; 95\\% CI [0.27, 0.73]), substantially higher than FewRel ($R^2 = 0.218$), possibly reflecting a wider confusability range in the DocRED schema, though document-level context may also provide richer cues for type confusion. Across all RE settings, BCS slopes range from $-$0.40 to $-$0.71, significant in all conditions with sufficient BCS range.\n\n\\paragraph{Within-pool controlled comparison.}\n\\label{sec:within_pool}\nWithin-pool analysis confirms slope consistency across pools (permutation $p \\approx 0.60$; Appendix~\\ref{app:within-pool-method}). The 80-relation extreme-batch gap (\\S\\ref{sec:bcs_controlled}) reflects wider BCS range, not stronger per-unit sensitivity.\n\n\\paragraph{Practical magnitude.}\n\\label{sec:practical_magnitude}\nDirect regression on 100 random 16-type batches from the 80-relation pool shows BCS explains 22\\% of cross-batch accuracy variance ($R^2 = 0.218$, $p < 0.001$), scaling to 53\\% at DocRED 96-rel. The typical BCS span (IQR = 0.054) yields an expected accuracy gap of 2.2\\,pp (95\\% CI: [0.4, 4.0]). Quartile comparison confirms: bottom-quartile BCS batches average 82.8\\% vs.\\ 78.9\\% for top-quartile ($\\Delta = 3.9$\\,pp). A post-hoc Monte Carlo simulation confirms the ${\\sim}3\\times$ pair-to-batch amplification (Appendix~\\ref{app:aggregation-sim}).\n\n\\paragraph{Cross-model validation.}\nThe effect replicates on Meta-Llama-3.1-8B-Instruct: BCS gaps of $-$27.1\\,pp (count 8) and $-$23.9\\,pp (count 16), reaching 77--87\\% of Qwen3-32B's gap. Both models converge to $\\approx$51\\% under high confusability, suggesting a task-inherent difficulty floor (Table~\\ref{tab:cross_model_bcs}). Dimension~1 replicates fully on Llama-3.1-8B (\\S\\ref{sec:count_curves}); Dimension~2 replicates on RE but shows floor effects on 8B NER (Limitations, item~1). Llama-3.1-70B-Instruct (FP8) and Gemini 2.5 Flash (API) confirm directional consistency across scales and families (Appendix~\\ref{sec:appendix_cross_model_70b}, \\ref{sec:appendix_cross_model_gemini}).\n\n\\paragraph{Prompt sensitivity.}\nUnder the v2 prompt, the extreme-batch BCS gap is $-$25.5\\,pp ($r = -0.919$, $p < 0.001$; $n{=}25$), modestly attenuated from v1 but highly significant. NER shows no batch-level BCS--F1 correlation under either prompt ($r \\approx 0$, $n = 450$; \\S\\ref{sec:multi_channel}). The effect holds across four structurally distinct prompt variants at count 32 (all $r \\leq -0.47$; Appendix~\\ref{sec:appendix_prompt_variants}), ruling out prompt design as the source.\n\n\\subsection{Multi-Dimensional Degradation}\n\\label{sec:multi_channel}\n\n\\begin{figure*}[t]\n\\centering\n\\includegraphics[width=\\textwidth]{../../figures/paper/fig_error_taxonomy.pdf}\n\\caption{Error taxonomy decomposition. IntraSub scales monotonically with BCS in both tasks. RE missed rates remain flat (10--16\\%), but NER missed rates are substantially higher (43--65\\%) and non-monotonic.}\n\\label{fig:error_taxonomy}\n\\end{figure*}\n\nError taxonomy decomposition (Table~\\ref{tab:error_taxonomy} and Figure~\\ref{fig:error_taxonomy}) shows intra-batch substitution (IntraSub) scales monotonically with BCS: $\\rho = 1.0$ ($p < 0.001$) for NER and $\\rho = 0.954$ ($p < 0.001$) for RE. In NER, missed rates are higher (43--65\\%) and non-monotonic; confusable types impair entity detection itself. Extreme-BCS batches produce $9.9\\text{--}27.5\\times$ more confusion than low-BCS batches.\n\nThese results establish two dimensions: \\textbf{Dimension~1} (count predicts recall decline) and \\textbf{Dimension~2} (confusability predicts type confusion). The full-range regression ($n = 69$, five count levels) serves as the primary separability test; the $2 \\times 2$ factorial ($n = 54$) as a sensitivity check. TOST \\citep{lakens-2017-equivalence,schuirmann-1987-tost} on FewRel at $\\pm 3$\\,pp yields $p = 0.003$ and at $\\pm 2$\\,pp yields $p = 0.047$, though equivalence below 2\\,pp is inconclusive ($p = 0.278$; logit-scale also inconclusive, $p = 0.209$; Appendix~\\ref{sec:appendix_factorial}). On DocRED, the interaction is larger (+5.7\\,pp, 95\\% CI [$-$1.6, 13.0]; $\\pm$3\\,pp TOST $p = 0.77$), possibly reflecting baseline compression at higher type counts; we restrict the bounded-interaction claim to sentence-level RE. In NER, batch-level BCS shows no predictive signal (\\S\\ref{sec:bcs_controlled}), preventing clean dimension separation; the factorial test is inconclusive ($p = 0.50$).\n\n\\subsection{Centrality Confound on Homogeneous Schemas}\n\\label{sec:centrality_confound}\n\nPer-type analysis on MAVEN reveals an anomalous \\emph{positive} BCS--F1 correlation (Qwen3 $\\rho = +0.184$, $p = 0.025$; MiniLM $\\rho = +0.208$, $p = 0.011$). This traces to same-domain embedding collapse \\cite{cai-isotropy-clusters-2021}: MAVEN's FrameNet-derived types cluster tightly, so mean BCS conflates confusability with centrality: high-BCS types are semantically central and easy to extract. Controlling for log frequency and degree centrality, the positive correlation vanishes ($p > 0.2$; Appendix~\\ref{sec:appendix_residualized_bcs}). The pairwise SCS signal remains intact ($r = 0.129$, $p < 0.001$; Table~\\ref{tab:pairwise}); the problem is per-type aggregation, not the underlying relationship. Few-NERD's cross-domain schema does not exhibit this confound ($\\rho = -0.293$, $p = 0.02$). Mean BCS is thus reliable only for cross-domain schemas; same-domain schemas require pairwise SCS or centrality adjustment.",
      "numLines": 92,
      "startLine": 1,
      "totalLines": 92
    }
  },
  "sourceToolAssistantUUID": "8877d4a2-5151-464d-ad8a-a49bd498e02a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_reviewer_2_302b64f9",
  "sessionId": "0ff1fe81-4731-4c76-91b4-02652701ddff",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Tool call

_source line 24 · 2026-05-19T04:30:52.809Z_

<details open><summary>🔧 Tool call — Read · `toolu_01CVxQknC5QT8MEj5t2sudMS`</summary>

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
  "parentUuid": "c1434d8b-c2eb-45af-8f3c-ecb2b1f47aec",
  "isSidechain": false,
  "requestId": "req_011CbBJL3Mfp6QVPxgqBTm4o",
  "type": "assistant",
  "uuid": "eda6bb7e-5b89-4e61-a6d7-916d2939a614",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_reviewer_2_302b64f9",
  "sessionId": "0ff1fe81-4731-4c76-91b4-02652701ddff",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PMdzHtBXazYPW4S8Z616zu",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2278,
      "cache_read_input_tokens": 28070,
      "output_tokens": 849,
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
          "output_tokens": 849,
          "cache_read_input_tokens": 28070,
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

_source line 25 · 2026-05-19T04:30:52.815Z_

<details><summary>↩ Tool result · `toolu_01CVxQknC5QT8MEj5t2sudMS`</summary>

```text
1	\section{Schema Decomposition: Failure, Diagnosis, and Mitigation}
2	\label{sec:sdgd}
3	
4	A natural intervention against confusability-related degradation is to partition the schema so confusable types never co-occur. We test this with \textbf{Schema-DAG-Guided Decomposition} (SDGD), which applies greedy graph coloring on the SCS graph to assign types to low-confusability batches.
5	
6	\paragraph{NER: merge amplification.}
7	All decomposition modes fall below the single-pass NER baseline (F1\,=\,0.445): SDGD obtains 0.251, random batching 0.320, per-type 0.292 (Appendix~\ref{sec:appendix_sdgd}). The core failure is \emph{merge amplification}: presenting text to the model $k$ times with different type subsets is associated with precision collapse (0.563$\to$0.210--0.249) as false positives scale with $k$, while true positives remain bounded. Confidence gating does not recover net F1. RE avoids this failure because closed-set classification requires no span reconciliation across passes.
8	
9	\paragraph{RE: oracle routing.}
10	Oracle routing achieves 0.802 accuracy versus 0.504 single-pass on FewRel 80-relation RE (+29.8\,pp; Table~\ref{tab:batch_composition}); type separation recovers performance absent merge amplification. Confusability-aware grouping yields only +1.4\,pp over random ($p \approx 0.19$, n.s.): graph coloring achieves only marginal mean BCS reduction (0.559$\to$0.552), insufficient to produce detectable accuracy improvement. All practical routing strategies fall below the single-pass baseline (Appendix~\ref{sec:appendix_routing}).
11	
12	Promising avenues include coarse-to-fine pipelines and retrieval-based routing.
13	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "eda6bb7e-5b89-4e61-a6d7-916d2939a614",
  "isSidechain": false,
  "promptId": "8257bd0e-08b4-4530-aa87-1e185ea40a51",
  "type": "user",
  "uuid": "97b2f906-27a7-4bbe-950c-a04084f516c5",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/sdgd_negative.tex",
      "content": "\\section{Schema Decomposition: Failure, Diagnosis, and Mitigation}\n\\label{sec:sdgd}\n\nA natural intervention against confusability-related degradation is to partition the schema so confusable types never co-occur. We test this with \\textbf{Schema-DAG-Guided Decomposition} (SDGD), which applies greedy graph coloring on the SCS graph to assign types to low-confusability batches.\n\n\\paragraph{NER: merge amplification.}\nAll decomposition modes fall below the single-pass NER baseline (F1\\,=\\,0.445): SDGD obtains 0.251, random batching 0.320, per-type 0.292 (Appendix~\\ref{sec:appendix_sdgd}). The core failure is \\emph{merge amplification}: presenting text to the model $k$ times with different type subsets is associated with precision collapse (0.563$\\to$0.210--0.249) as false positives scale with $k$, while true positives remain bounded. Confidence gating does not recover net F1. RE avoids this failure because closed-set classification requires no span reconciliation across passes.\n\n\\paragraph{RE: oracle routing.}\nOracle routing achieves 0.802 accuracy versus 0.504 single-pass on FewRel 80-relation RE (+29.8\\,pp; Table~\\ref{tab:batch_composition}); type separation recovers performance absent merge amplification. Confusability-aware grouping yields only +1.4\\,pp over random ($p \\approx 0.19$, n.s.): graph coloring achieves only marginal mean BCS reduction (0.559$\\to$0.552), insufficient to produce detectable accuracy improvement. All practical routing strategies fall below the single-pass baseline (Appendix~\\ref{sec:appendix_routing}).\n\nPromising avenues include coarse-to-fine pipelines and retrieval-based routing.\n",
      "numLines": 13,
      "startLine": 1,
      "totalLines": 13
    }
  },
  "sourceToolAssistantUUID": "eda6bb7e-5b89-4e61-a6d7-916d2939a614",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_reviewer_2_302b64f9",
  "sessionId": "0ff1fe81-4731-4c76-91b4-02652701ddff",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Tool call

_source line 26 · 2026-05-19T04:30:53.165Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Uka5RcKv7BhkwJL24MXfpa`</summary>

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
  "parentUuid": "97b2f906-27a7-4bbe-950c-a04084f516c5",
  "isSidechain": false,
  "requestId": "req_011CbBJL3Mfp6QVPxgqBTm4o",
  "type": "assistant",
  "uuid": "3569ff1d-03b4-4d47-b2cb-2a127714502b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_reviewer_2_302b64f9",
  "sessionId": "0ff1fe81-4731-4c76-91b4-02652701ddff",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PMdzHtBXazYPW4S8Z616zu",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2278,
      "cache_read_input_tokens": 28070,
      "output_tokens": 849,
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
          "output_tokens": 849,
          "cache_read_input_tokens": 28070,
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

_source line 27 · 2026-05-19T04:30:53.193Z_

<details><summary>↩ Tool result · `toolu_01Uka5RcKv7BhkwJL24MXfpa`</summary>

```text
1	\section{Discussion}
2	\label{sec:discussion}
3	
4	\paragraph{Boundary conditions.}
5	The two-dimensional decomposition applies to cross-domain schemas; same-domain schemas exhibit centrality confounding (\S\ref{sec:centrality_confound}). The effect generalizes to document-level RE (DocRED $R^2 = 0.51$) and persists across prompt designs (Appendix~\ref{sec:appendix_prompt_sensitivity}). Dimension~1 replicates across scales (8B--70B); Dimension~2 attenuates on smaller models.
6	
7	\paragraph{Why does embedding similarity predict LLM confusion?}
8	SCS captures semantic proximity in LLMs' type-resolution space. The unconditional pairwise $R^2$ is modest (1.3\%); conditional on nonzero confusion, $R^2$ rises to 7\%. Correlated aggregation amplifies this to batch-level $R^2$ of 18--25\% (Monte Carlo simulation; Appendix~\ref{app:aggregation-sim}), consistent with observed RE values.
9	
10	\paragraph{Task-dependent effects and format dependency.}
11	The batch-level BCS--performance relationship is RE-specific ($R^2 = 0.22$--$0.53$ vs.\ $r \approx 0$ for NER, $n = 450$). RE uses forced-choice classification where all non-null errors are type substitutions \cite{tam-2024-let-me-speak}, making BCS predictive. NER produces multi-span output where errors scatter across missed entities, boundary misalignment, and type confusion, diluting the BCS signal \cite{schall-2025-hidden-cost}. The NER U-shape (\S\ref{sec:count_curves}) likely reflects a dual-task burden: partial schemas require simultaneous span detection and type-membership filtering; at full schema, filtering becomes vacuous and recall recovers. An unconstrained decoding ablation ($n = 25$) confirms format dependency: removing the JSON enum constraint eliminates the BCS--accuracy correlation ($\rho = -0.14$, $p = 0.49$) while OOV remains near zero (0.08\%), showing that constrained decoding channels all errors into type substitution.
12	
13	\paragraph{Practical implications.}
14	For RE, pre-screening type pairs in the upper SCS quartile identifies confusability risk (3--5\,pp expected impact). For NER, reducing candidate types per prompt is the primary lever, as confusability-aware batching provides no additional benefit. Schema partitioning remains non-viable due to merge amplification (NER) and routing uncertainty (RE). We suggest four actionable directions: (1)~at schema design time, practitioners may flag type pairs with SCS${}\,>\,0.85$ for merging or definition refinement; (2)~for RE batches, monitoring mean BCS provides a lightweight quality indicator, since BCS explains 22--53\% of cross-batch variance; (3)~contrastive definitions or targeted few-shot examples for high-SCS pairs may reduce confusion without the label-unfamiliarity penalty of renaming (untested; future work); (4)~evaluation should report schema-controlled metrics alongside aggregate scores, as performance gaps between low- and high-BCS batches can reach 25--31\,pp.
15	
16	\section{Conclusion}
17	\label{sec:conclusion}
18	
19	Schema-associated degradation in training-free LLM extraction operates along two largely additive dimensions: count-related recall decline and confusability-related type substitution, with bounded interaction in sentence-level RE but not in document-level RE or NER. Count decline replicates across scales (8B--70B) and families including Gemini 2.5 Flash; confusability effects are structural (+4.3\,pp under 5-shot; Appendix~\ref{sec:appendix_fewshot_bcs}). Schema decomposition fails due to merge amplification (NER) and routing failure (RE).
20	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3569ff1d-03b4-4d47-b2cb-2a127714502b",
  "isSidechain": false,
  "promptId": "8257bd0e-08b4-4530-aa87-1e185ea40a51",
  "type": "user",
  "uuid": "e79d6891-b77d-4349-ad6e-b0ed808702ae",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/discussion.tex",
      "content": "\\section{Discussion}\n\\label{sec:discussion}\n\n\\paragraph{Boundary conditions.}\nThe two-dimensional decomposition applies to cross-domain schemas; same-domain schemas exhibit centrality confounding (\\S\\ref{sec:centrality_confound}). The effect generalizes to document-level RE (DocRED $R^2 = 0.51$) and persists across prompt designs (Appendix~\\ref{sec:appendix_prompt_sensitivity}). Dimension~1 replicates across scales (8B--70B); Dimension~2 attenuates on smaller models.\n\n\\paragraph{Why does embedding similarity predict LLM confusion?}\nSCS captures semantic proximity in LLMs' type-resolution space. The unconditional pairwise $R^2$ is modest (1.3\\%); conditional on nonzero confusion, $R^2$ rises to 7\\%. Correlated aggregation amplifies this to batch-level $R^2$ of 18--25\\% (Monte Carlo simulation; Appendix~\\ref{app:aggregation-sim}), consistent with observed RE values.\n\n\\paragraph{Task-dependent effects and format dependency.}\nThe batch-level BCS--performance relationship is RE-specific ($R^2 = 0.22$--$0.53$ vs.\\ $r \\approx 0$ for NER, $n = 450$). RE uses forced-choice classification where all non-null errors are type substitutions \\cite{tam-2024-let-me-speak}, making BCS predictive. NER produces multi-span output where errors scatter across missed entities, boundary misalignment, and type confusion, diluting the BCS signal \\cite{schall-2025-hidden-cost}. The NER U-shape (\\S\\ref{sec:count_curves}) likely reflects a dual-task burden: partial schemas require simultaneous span detection and type-membership filtering; at full schema, filtering becomes vacuous and recall recovers. An unconstrained decoding ablation ($n = 25$) confirms format dependency: removing the JSON enum constraint eliminates the BCS--accuracy correlation ($\\rho = -0.14$, $p = 0.49$) while OOV remains near zero (0.08\\%), showing that constrained decoding channels all errors into type substitution.\n\n\\paragraph{Practical implications.}\nFor RE, pre-screening type pairs in the upper SCS quartile identifies confusability risk (3--5\\,pp expected impact). For NER, reducing candidate types per prompt is the primary lever, as confusability-aware batching provides no additional benefit. Schema partitioning remains non-viable due to merge amplification (NER) and routing uncertainty (RE). We suggest four actionable directions: (1)~at schema design time, practitioners may flag type pairs with SCS${}\\,>\\,0.85$ for merging or definition refinement; (2)~for RE batches, monitoring mean BCS provides a lightweight quality indicator, since BCS explains 22--53\\% of cross-batch variance; (3)~contrastive definitions or targeted few-shot examples for high-SCS pairs may reduce confusion without the label-unfamiliarity penalty of renaming (untested; future work); (4)~evaluation should report schema-controlled metrics alongside aggregate scores, as performance gaps between low- and high-BCS batches can reach 25--31\\,pp.\n\n\\section{Conclusion}\n\\label{sec:conclusion}\n\nSchema-associated degradation in training-free LLM extraction operates along two largely additive dimensions: count-related recall decline and confusability-related type substitution, with bounded interaction in sentence-level RE but not in document-level RE or NER. Count decline replicates across scales (8B--70B) and families including Gemini 2.5 Flash; confusability effects are structural (+4.3\\,pp under 5-shot; Appendix~\\ref{sec:appendix_fewshot_bcs}). Schema decomposition fails due to merge amplification (NER) and routing failure (RE).\n",
      "numLines": 20,
      "startLine": 1,
      "totalLines": 20
    }
  },
  "sourceToolAssistantUUID": "3569ff1d-03b4-4d47-b2cb-2a127714502b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_reviewer_2_302b64f9",
  "sessionId": "0ff1fe81-4731-4c76-91b4-02652701ddff",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Tool call

_source line 28 · 2026-05-19T04:30:53.834Z_

<details open><summary>🔧 Tool call — Read · `toolu_015vvUQWL5eiwbSCjMFGhYJ9`</summary>

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
  "parentUuid": "e79d6891-b77d-4349-ad6e-b0ed808702ae",
  "isSidechain": false,
  "requestId": "req_011CbBJL3Mfp6QVPxgqBTm4o",
  "type": "assistant",
  "uuid": "a10295a6-3a11-418f-b983-e72d16b25732",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_reviewer_2_302b64f9",
  "sessionId": "0ff1fe81-4731-4c76-91b4-02652701ddff",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PMdzHtBXazYPW4S8Z616zu",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2278,
      "cache_read_input_tokens": 28070,
      "output_tokens": 849,
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
          "output_tokens": 849,
          "cache_read_input_tokens": 28070,
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

_source line 29 · 2026-05-19T04:30:53.840Z_

<details><summary>↩ Tool result · `toolu_015vvUQWL5eiwbSCjMFGhYJ9`</summary>

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
15	N/A. This is a purely analytical study of schema-associated degradation in existing LLM IE systems. It does not introduce new models, datasets, or deployment-facing artifacts. The findings characterize failure modes and are intended to inform safer schema design.
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
63	Yes. \S\ref{sec:model}: Qwen3-32B (32B parameters, FP8), Meta-Llama-3.1-70B-Instruct (70B parameters, FP8), and Meta-Llama-3.1-8B-Instruct (8B parameters). Gemini 2.5 Flash was additionally accessed via API for cross-architecture validation. Inference was conducted on NVIDIA RTX PRO 6000 GPUs (96\,GB) served via vLLM. Total compute was approximately 72 GPU-hours of inference (no training).
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
  "parentUuid": "a10295a6-3a11-418f-b983-e72d16b25732",
  "isSidechain": false,
  "promptId": "8257bd0e-08b4-4530-aa87-1e185ea40a51",
  "type": "user",
  "uuid": "5b3b3a48-023c-4db8-8301-8c0d3973e2cb",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/checklist.tex",
      "content": "\\section*{Responsible NLP Research Checklist}\n\nFor each question, the answer is \\textbf{Yes}, \\textbf{No}, or \\textbf{N/A}. If Yes, the relevant section is indicated. If No, a justification is provided.\n\n\\subsection*{A \\quad For Every Submission}\n\n\\begin{enumerate}[label=\\textbf{A\\arabic*.},leftmargin=*,itemsep=4pt]\n\n\\item \\textbf{Did you describe the limitations of your work?}\n\nYes. The Limitations section (after \\S\\ref{sec:conclusion}) discusses single-model reliance, modest pairwise effect sizes, cross-pool slope consistency, factorial interaction tests with TOST equivalence, decomposition scope, and metric scope.\n\n\\item \\textbf{Did you discuss any potential risks of your work?}\n\nN/A. This is a purely analytical study of schema-associated degradation in existing LLM IE systems. It does not introduce new models, datasets, or deployment-facing artifacts. The findings characterize failure modes and are intended to inform safer schema design.\n\n\\item \\textbf{Do the abstract and introduction summarize the paper's main claims?}\n\nYes. The abstract and \\S\\ref{sec:introduction} state the two-dimensional degradation pattern (count and confusability), the cross-model consistency check, and the negative SDGD result.\n\n\\item \\textbf{Did you use AI assistants (e.g., ChatGPT, Copilot) when working on this paper?}\n\nYes. We used Claude (Anthropic) for writing assistance and experimental code development. All scientific claims, experimental designs, and analyses were conducted by the authors.\n\n\\end{enumerate}\n\n\\subsection*{B \\quad Scientific Artifacts}\n\n\\begin{enumerate}[label=\\textbf{B\\arabic*.},leftmargin=*,itemsep=4pt]\n\n\\item \\textbf{Did you cite the creators of artifacts you used?}\n\nYes. Few-NERD \\cite{fewnerd-2021}, FewRel \\cite{fewrel-2018}, DocRED \\cite{docred-2019}, MAVEN \\cite{maven-2020}, Qwen3-32B \\cite{qwen3-2025}, Meta-Llama-3.1-70B-Instruct and Meta-Llama-3.1-8B-Instruct \\cite{llama3-2024}, vLLM \\cite{vllm-2023}, and all-MiniLM-L6-v2 \\cite{minilm-2020} are cited in \\S\\ref{sec:datasets} and \\S\\ref{sec:model}.\n\n\\item \\textbf{Did you discuss the license or terms for use and/or distribution of any artifacts?}\n\nYes. All four datasets are publicly available research benchmarks. Few-NERD is released under CC-BY-SA 4.0; FewRel, DocRED, and MAVEN are publicly released for research use. Models are used under their respective open-weight licenses.\n\n\\item \\textbf{Did you discuss if your use of existing artifacts is consistent with their intended use?}\n\nYes. All datasets are used for their intended purpose (IE evaluation). No data is used outside the scope specified by the dataset creators.\n\n\\item \\textbf{Did you discuss whether the data contains personally identifiable information or offensive content?}\n\nN/A. We use established benchmarks that have been vetted by the research community. No new data collection or annotation was performed.\n\n\\item \\textbf{Did you provide documentation of the artifacts, e.g., coverage of languages, coverage of domains, etc.?}\n\nYes. Table~\\ref{tab:datasets} reports type counts, evaluation unit counts, domain characteristics, and BCS ranges for each dataset. \\S\\ref{sec:datasets} describes dataset provenance and sampling procedures.\n\n\\item \\textbf{Did you report relevant statistics for your dataset(s)?}\n\nYes. \\S\\ref{sec:datasets} and Table~\\ref{tab:datasets} report evaluation set sizes, type counts, and sampling methodology. Count levels and batch sizes are specified in \\S\\ref{sec:exp_design}.\n\n\\end{enumerate}\n\n\\subsection*{C \\quad Computational Experiments}\n\n\\begin{enumerate}[label=\\textbf{C\\arabic*.},leftmargin=*,itemsep=4pt]\n\n\\item \\textbf{Did you report the number of parameters in the models used, the total computational budget, and computing infrastructure?}\n\nYes. \\S\\ref{sec:model}: Qwen3-32B (32B parameters, FP8), Meta-Llama-3.1-70B-Instruct (70B parameters, FP8), and Meta-Llama-3.1-8B-Instruct (8B parameters). Gemini 2.5 Flash was additionally accessed via API for cross-architecture validation. Inference was conducted on NVIDIA RTX PRO 6000 GPUs (96\\,GB) served via vLLM. Total compute was approximately 72 GPU-hours of inference (no training).\n\n\\item \\textbf{Did you discuss the experimental setup, including hyperparameter search and best-found values?}\n\nYes. \\S\\ref{sec:exp_design} describes both experimental paradigms (count curves and BCS-controlled). \\S\\ref{sec:model} reports decoding parameters (greedy, temperature${}=0$, seed${}=42$) and prompt versions. No hyperparameter search was conducted as this is a zero-shot evaluation study.\n\n\\item \\textbf{Did you report descriptive statistics about your results?}\n\nYes. All key metrics include 95\\% bootstrap confidence intervals (10{,}000 resamples, percentile method) as stated in \\S\\ref{sec:model}. Spearman correlations are reported with $p$-values throughout \\S\\ref{sec:count_curves}--\\ref{sec:centrality_confound}. Permutation tests are used for slope comparisons.\n\n\\item \\textbf{Did you report implementation details, e.g., versions of packages?}\n\nYes. \\S\\ref{sec:model} specifies vLLM v0.20.2 for model serving. Embedding models are named with version identifiers (\\S\\ref{sec:scs}). Code and scripts will be released upon acceptance.\n\n\\end{enumerate}\n\n\\subsection*{D \\quad Human Annotators or Crowdworkers}\n\n\\begin{enumerate}[label=\\textbf{D\\arabic*.},leftmargin=*,itemsep=4pt]\n\n\\item \\textbf{Did you report the full text of instructions given to participants?}\n\nN/A. No human annotation or crowdsourcing was conducted.\n\n\\item \\textbf{Did you report information about how you recruited and paid participants?}\n\nN/A.\n\n\\item \\textbf{Did you discuss whether and how consent was obtained?}\n\nN/A.\n\n\\item \\textbf{Did you report whether the data collection was approved by an institutional review board (IRB)?}\n\nN/A.\n\n\\item \\textbf{Did you report the basic demographic and geographic characteristics of the annotator population?}\n\nN/A.\n\n\\end{enumerate}\n\n\\subsection*{E \\quad AI-Assisted Research}\n\n\\begin{enumerate}[label=\\textbf{E\\arabic*.},leftmargin=*,itemsep=4pt]\n\n\\item \\textbf{Did you report the use of AI assistants?}\n\nYes. See A4 above. AI assistants were used for code development and document formatting. The research design, execution, and interpretation are the authors' own work.\n\n\\end{enumerate}\n",
      "numLines": 114,
      "startLine": 1,
      "totalLines": 114
    }
  },
  "sourceToolAssistantUUID": "a10295a6-3a11-418f-b983-e72d16b25732",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_reviewer_2_302b64f9",
  "sessionId": "0ff1fe81-4731-4c76-91b4-02652701ddff",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Tool call

_source line 30 · 2026-05-19T04:30:54.230Z_

<details open><summary>🔧 Tool call — Read · `toolu_011yMWho1M4z5MrZ1jW1A9Tq`</summary>

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
  "parentUuid": "5b3b3a48-023c-4db8-8301-8c0d3973e2cb",
  "isSidechain": false,
  "requestId": "req_011CbBJL3Mfp6QVPxgqBTm4o",
  "type": "assistant",
  "uuid": "0e7d9587-e0b0-44b0-99d7-f441568d7540",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_reviewer_2_302b64f9",
  "sessionId": "0ff1fe81-4731-4c76-91b4-02652701ddff",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PMdzHtBXazYPW4S8Z616zu",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2278,
      "cache_read_input_tokens": 28070,
      "output_tokens": 849,
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
          "output_tokens": 849,
          "cache_read_input_tokens": 28070,
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

_source line 31 · 2026-05-19T04:30:54.237Z_

<details><summary>↩ Tool result · `toolu_011yMWho1M4z5MrZ1jW1A9Tq`</summary>

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
  "parentUuid": "0e7d9587-e0b0-44b0-99d7-f441568d7540",
  "isSidechain": false,
  "promptId": "8257bd0e-08b4-4530-aa87-1e185ea40a51",
  "type": "user",
  "uuid": "914250f0-ed5f-4e00-a18f-3220d3496243",
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
  "sourceToolAssistantUUID": "0e7d9587-e0b0-44b0-99d7-f441568d7540",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_reviewer_2_302b64f9",
  "sessionId": "0ff1fe81-4731-4c76-91b4-02652701ddff",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Tool call

_source line 32 · 2026-05-19T04:30:54.834Z_

<details open><summary>🔧 Tool call — Read · `toolu_01QX4W4K2pwsZXh6HnqwQxxA`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "914250f0-ed5f-4e00-a18f-3220d3496243",
  "isSidechain": false,
  "requestId": "req_011CbBJL3Mfp6QVPxgqBTm4o",
  "type": "assistant",
  "uuid": "6c3727a5-ed97-4544-b562-0b8bf577919c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_reviewer_2_302b64f9",
  "sessionId": "0ff1fe81-4731-4c76-91b4-02652701ddff",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PMdzHtBXazYPW4S8Z616zu",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2278,
      "cache_read_input_tokens": 28070,
      "output_tokens": 849,
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
          "output_tokens": 849,
          "cache_read_input_tokens": 28070,
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

_source line 33 · 2026-05-19T04:30:55.110Z_

<details><summary>↩ Tool result · `toolu_01QX4W4K2pwsZXh6HnqwQxxA`</summary>

```text
1	@inproceedings{tam-2024-let-me-speak,
2	  title     = {Let Me Speak Freely? {A} Study on the Impact of Format Restrictions on Performance of Large Language Models},
3	  author    = {Tam, Zhi Rui and Wu, Cheng-Kuang and Tsai, Yi-Lin and Lin, Chieh-Yen and Lee, Hung-yi and Chen, Yun-Nung},
4	  booktitle = {Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing: Industry Track},
5	  year      = {2024},
6	  url       = {https://arxiv.org/abs/2408.02442}
7	}
8	
9	@inproceedings{yin-2019-zero-shot-bench,
10	  title     = {Benchmarking Zero-shot Text Classification: Datasets, Evaluation and Entailment Approach},
11	  author    = {Yin, Wenpeng and Hay, Jamaal and Roth, Dan},
12	  booktitle = {Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing},
13	  pages     = {3914--3923},
14	  year      = {2019},
15	  url       = {https://arxiv.org/abs/1909.00161}
16	}
17	
18	@article{schuirmann-1987-tost,
19	  title     = {A Comparison of the Two One-Sided Tests Procedure and the Power Approach for Assessing the Equivalence of Average Bioavailability},
20	  author    = {Schuirmann, Donald J.},
21	  journal   = {Journal of Pharmacokinetics and Biopharmaceutics},
22	  volume    = {15},
23	  number    = {6},
24	  pages     = {657--680},
25	  year      = {1987},
26	  doi       = {10.1007/BF01068419}
27	}
28	
29	@article{gemini-2025,
30	  title     = {Gemini 2.5: Pushing the Frontier with Advanced Reasoning, Multimodality, and Long Context},
31	  author    = {Comanici, Gheorghe and others},
32	  journal   = {arXiv preprint arXiv:2507.06261},
33	  year      = {2025},
34	  url       = {https://arxiv.org/abs/2507.06261}
35	}
36	
37	@inproceedings{snell2017prototypical,
38	  title     = {Prototypical Networks for Few-shot Learning},
39	  author    = {Snell, Jake and Swersky, Kevin and Zemel, Richard},
40	  booktitle = {Advances in Neural Information Processing Systems},
41	  volume    = {30},
42	  year      = {2017}
43	}
44	
45	@inproceedings{muller2019when,
46	  title     = {When Does Label Smoothing Help?},
47	  author    = {M{\"u}ller, Rafael and Kornblith, Simon and Hinton, Geoffrey E.},
48	  booktitle = {Advances in Neural Information Processing Systems},
49	  volume    = {32},
50	  year      = {2019}
51	}
52	
53	@inproceedings{peterson2019human,
54	  title     = {Human Uncertainty Makes Classification More Robust},
55	  author    = {Peterson, Joshua C. and Battleday, Ruairidh M. and Griffiths, Thomas L. and Russakovsky, Olga},
56	  booktitle = {Proceedings of the IEEE/CVF International Conference on Computer Vision},
57	  pages     = {9617--9626},
58	  year      = {2019}
59	}
60	
61	@inproceedings{jagannatha2020calibrating,
62	  title     = {Calibrating Structured Output Predictors for Natural Language Processing},
63	  author    = {Jagannatha, Abhyuday and Yu, Hong},
64	  booktitle = {Proceedings of the 58th Annual Meeting of the Association for Computational Linguistics},
65	  pages     = {2078--2092},
66	  year      = {2020}
67	}
68	
69	@article{willard2023efficient,
70	  title     = {Efficient Guided Generation for Large Language Models},
71	  author    = {Willard, Brandon T. and Louf, R{\'e}mi},
72	  journal   = {arXiv preprint arXiv:2307.09702},
73	  year      = {2023},
74	  url       = {https://arxiv.org/abs/2307.09702}
75	}
76	
77	
78	@inproceedings{lu2022fantastically,
79	  title     = {Fantastically Ordered Prompts and Where to Find Them: Overcoming Few-Shot Prompt Order Sensitivity},
80	  author    = {Lu, Yao and Bartolo, Max and Moore, Alastair and Riedel, Sebastian and Stenetorp, Pontus},
81	  booktitle = {Proceedings of the 60th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)},
82	  pages     = {8086--8098},
83	  year      = {2022},
84	  url       = {https://aclanthology.org/2022.acl-long.556/},
85	  doi       = {10.18653/v1/2022.acl-long.556}
86	}
87	
88	@inproceedings{yang2025beyond,
89	  title     = {Beyond Boundaries: Learning a Universal Entity Taxonomy across Datasets and Languages for Open Named Entity Recognition},
90	  author    = {Yang, Yuming and Zhao, Wantong and Huang, Caishuang and Ye, Junjie and Wang, Xiao and Zheng, Huiyuan and Nan, Yang and Wang, Yuran and Xu, Xueying and Huang, Kaixin and Zhang, Yunke and Gui, Tao and Zhang, Qi and Huang, Xuanjing},
91	  booktitle = {Proceedings of the 31st International Conference on Computational Linguistics},
92	  pages     = {10902--10923},
93	  year      = {2025},
94	  url       = {https://aclanthology.org/2025.coling-main.725/}
95	}
96	
97	% =============================================================================
98	% DIRECT COMPETITORS
99	% =============================================================================
100	
101	@inproceedings{llm-pee-2025,
102	    title     = {Towards Event Extraction with Massive Types: {LLM}-based Collaborative Annotation and Partitioning Extraction},
103	    author    = {Liu, Wenxuan and Li, Zixuan and Bai, Long and Zuo, Yuxin and Xu, Daozhu and Jin, Xiaolong and Guo, Jiafeng and Cheng, Xueqi},
104	    booktitle = {Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing},
105	    year      = {2025},
106	    url       = {https://aclanthology.org/2025.emnlp-main.1743/},
107	}
108	
109	@inproceedings{parse-2025,
110	    title     = {{PARSE}: {LLM} Driven Schema Optimization for Reliable Entity Extraction},
111	    author    = {Shrimal, Anubhav and Jain, Aryan and Chowdhury, Soumyajit and Yenigalla, Promod},
112	    booktitle = {Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing: Industry Track},
113	    year      = {2025},
114	    url       = {https://aclanthology.org/2025.emnlp-industry.184/},
115	}
116	
117	@inproceedings{dee-2024,
118	    title     = {Decompose, Enrich, and Extract! Schema-aware Event Extraction using {LLM}s},
119	    author    = {Shiri, Fatemeh and Nguyen, Van and Moghimifar, Farhad and Yoo, John and Haffari, Gholamreza and Li, Yuan-Fang},
120	    booktitle = {Proceedings of the IEEE International Conference on Tools with Artificial Intelligence},
121	    year      = {2024},
122	    url       = {https://arxiv.org/abs/2406.01045},
123	}
124	
125	@inproceedings{crossagentie-2025,
126	    title     = {{CROSSAGENTIE}: Cross-Type and Cross-Task Multi-Agent {LLM} Collaboration for Zero-Shot Information Extraction},
127	    author    = {Lu, Meng and Xie, Yuzhang and Bi, Zhenyu and Cao, Shuxiang and Wang, Xuan},
128	    booktitle = {Findings of the Association for Computational Linguistics: ACL 2025},
129	    year      = {2025},
130	    url       = {https://aclanthology.org/2025.findings-acl.718/},
131	}
132	
133	
134	@inproceedings{cmas-ner-2025,
135	    title     = {A Cooperative Multi-Agent Framework for Zero-Shot Named Entity Recognition},
136	    author    = {Wang, Zihan and Zhao, Ziqi and Lyu, Yougang and Chen, Zhumin and de Rijke, Maarten and Ren, Zhaochun},
137	    booktitle = {Proceedings of the ACM Web Conference 2025},
138	    year      = {2025},
139	    url       = {https://dl.acm.org/doi/10.1145/3696410.3714923},
140	    doi       = {10.1145/3696410.3714923},
141	}
142	
143	% =============================================================================
144	% METHOD COMPONENTS
145	% =============================================================================
146	
147	@inproceedings{uniner-2024,
148	    title     = {{UniversalNER}: Targeted Distillation from Large Language Models for Open Named Entity Recognition},
149	    author    = {Zhou, Wenxuan and Zhang, Sheng and Gu, Yu and Chen, Muhao and Poon, Hoifung},
150	    booktitle = {International Conference on Learning Representations},
151	    year      = {2024},
152	    url       = {https://arxiv.org/abs/2308.03279},
153	}
154	
155	@inproceedings{gollie-2024,
156	    title     = {{GoLLIE}: Annotation Guidelines improve Zero-Shot Information-Extraction},
157	    author    = {Sainz, Oscar and Garc{\'\i}a-Ferrero, Iker and Agerri, Rodrigo and Lopez de Lacalle, Oier and Rigau, German and Agirre, Eneko},
158	    booktitle = {International Conference on Learning Representations},
159	    year      = {2024},
160	    url       = {https://arxiv.org/abs/2310.03668},
161	}
162	
163	@inproceedings{gliner-2024,
164	    title     = {{GLiNER}: Generalist Model for Named Entity Recognition using Bidirectional Transformer},
165	    author    = {Zaratiana, Urchade and Tomeh, Nadi and Holat, Pierre and Charnois, Thierry},
166	    booktitle = {Proceedings of the 2024 Conference of the North American Chapter of the Association for Computational Linguistics},
167	    year      = {2024},
168	    url       = {https://arxiv.org/abs/2311.08526},
169	}
170	
171	@inproceedings{gliner2-2025,
172	    title     = {{GLiNER2}: Schema-Driven Multi-Task Learning for Structured Information Extraction},
173	    author    = {Zaratiana, Urchade and Pasternak, Gil and Boyd, Oliver and Hurn-Maloney, George and Lewis, Ash},
174	    booktitle = {Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing: System Demonstrations},
175	    year      = {2025},
176	    url       = {https://aclanthology.org/2025.emnlp-demos.10/},
177	}
178	
179	
180	@inproceedings{iepile-2024,
181	    title     = {{IEPile}: Unearthing Large Scale Schema-Conditioned Information Extraction Corpus},
182	    author    = {Gui, Honghao and Yuan, Lin and Ye, Hongbin and Zhang, Ningyu and Sun, Mengshu and Liang, Lei and Chen, Huajun},
183	    booktitle = {Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (Volume 2: Short Papers)},
184	    pages     = {127--146},
185	    year      = {2024},
186	    url       = {https://aclanthology.org/2024.acl-short.13/},
187	}
188	
189	
190	@inproceedings{dror-2018-significance,
191	    title     = {The Hitchhiker's Guide to Testing Statistical Significance in Natural Language Processing},
192	    author    = {Dror, Rotem and Baumer, Gili and Shlomov, Segev and Reichart, Roi},
193	    booktitle = {Proceedings of the 56th Annual Meeting of the Association for Computational Linguistics},
194	    year      = {2018},
195	    url       = {https://aclanthology.org/P18-1128/},
196	}
197	
198	@article{lost-in-middle-2024,
199	    title   = {Lost in the Middle: How Language Models Use Long Contexts},
200	    author  = {Liu, Nelson F. and Lin, Kevin and Hewitt, John and Paranjape, Ashwin and Bevilacqua, Michele and Petroni, Fabio and Liang, Percy},
201	    journal = {Transactions of the Association for Computational Linguistics},
202	    volume  = {12},
203	    pages   = {157--173},
204	    year    = {2024},
205	    url     = {https://arxiv.org/abs/2307.03172},
206	    doi     = {10.1162/tacl_a_00638},
207	}
208	
209	% =============================================================================
210	% ZERO-SHOT NER / RE BASELINES
211	% =============================================================================
212	
213	
214	
215	% =============================================================================
216	% EVALUATION / BENCHMARKING
217	% =============================================================================
218	
219	% =============================================================================
220	% SURVEYS / BACKGROUND
221	% =============================================================================
222	
223	@article{llm4ie-survey-2024,
224	    title   = {Large Language Models for Generative Information Extraction: A Survey},
225	    author  = {Xu, Derong and Chen, Wei and Peng, Wenjun and Zhang, Chao and Xu, Tong and Zhao, Xiangyu and Wu, Xian and Zheng, Yefeng and Wang, Yang and Chen, Enhong},
226	    journal = {Frontiers of Computer Science},
227	    volume  = {18},
228	    number  = {6},
229	    year    = {2024},
230	    url     = {https://arxiv.org/abs/2312.17617},
231	    doi     = {10.1007/s11704-024-40555-y},
232	}
233	
234	@inproceedings{knowcoder-2024,
235	    title     = {{KnowCoder}: Coding Structured Knowledge into {LLM}s for Universal Information Extraction},
236	    author    = {Li, Zixuan and Zeng, Yutao and Zuo, Yuxin and Ren, Weicheng and Liu, Wenxuan and Su, Miao and Guo, Yucan and Liu, Yantao and Li, Xiang and Hu, Zhilei and Bai, Long and Li, Wei and Liu, Yidan and Yang, Pan and Jin, Xiaolong and Guo, Jiafeng and Cheng, Xueqi},
237	    booktitle = {Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics},
238	    year      = {2024},
239	    url       = {https://arxiv.org/abs/2403.07969},
240	}
241	
242	@inproceedings{slot-2025,
243	    title     = {{SLOT}: Structuring the Output of Large Language Models},
244	    author    = {Shen, Zhengyuan and Wang, Darren Yow-Bang and Mishra, Soumya Smruti and Xu, Zhichao and Teng, Yifei and Ding, Haibo},
245	    booktitle = {Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing: Industry Track},
246	    year      = {2025},
247	    url       = {https://aclanthology.org/2025.emnlp-industry.32/},
248	}
249	
250	% =============================================================================
251	% EMBEDDING ANISOTROPY / REPRESENTATION DEGENERATION
252	% =============================================================================
253	
254	@inproceedings{gao-repr-degen-2019,
255	    title     = {Representation Degeneration Problem in Training Natural Language Generation Models},
256	    author    = {Gao, Jun and He, Di and Tan, Xu and Qin, Tao and Wang, Liwei and Liu, Tie-Yan},
257	    booktitle = {International Conference on Learning Representations},
258	    year      = {2019},
259	    url       = {https://arxiv.org/abs/1907.12009},
260	}
261	
262	@inproceedings{ethayarajh-contextual-2019,
263	    title     = {How Contextual are Contextualized Word Representations? {C}omparing the Geometry of {BERT}, {ELMo}, and {GPT-2} Embeddings},
264	    author    = {Ethayarajh, Kawin},
265	    booktitle = {Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing and the 9th International Joint Conference on Natural Language Processing},
266	    year      = {2019},
267	    url       = {https://aclanthology.org/D19-1006/},
268	}
269	
270	@inproceedings{cai-isotropy-clusters-2021,
271	    title     = {Isotropy in the Contextual Embedding Space: Clusters and Manifolds},
272	    author    = {Cai, Xingyu and Huang, Jiaji and Bian, Yuchen and Church, Kenneth},
273	    booktitle = {International Conference on Learning Representations},
274	    year      = {2021},
275	    url       = {https://openreview.net/forum?id=xYGNO86OWDH},
276	}
277	
278	
279	% =============================================================================
280	% ADDITIONAL REFERENCES (from references_survey.md only)
281	% =============================================================================
282	
283	@article{instructuie-2023,
284	    title   = {{InstructUIE}: Multi-task Instruction Tuning for Unified Information Extraction},
285	    author  = {Wang, Xiao and Zhou, Weikang and Zu, Can and Xia, Han and Chen, Tianze and Zhang, Yuansen and Zheng, Rui and Ye, Junjie and Zhang, Qi and Gui, Tao and Kang, Jihua and Yang, Jingsheng and Li, Siyuan and Du, Chunsai},
286	    journal = {arXiv preprint arXiv:2304.08085},
287	    year    = {2023},
288	    url     = {https://arxiv.org/abs/2304.08085},
289	}
290	
291	@inproceedings{codeie-2023,
292	    title     = {{CodeIE}: Large Code Generation Models are Better Few-Shot Information Extractors},
293	    author    = {Li, Peng and Sun, Tianxiang and Tang, Qiong and Yan, Hang and Wu, Yuanbin and Huang, Xuanjing and Qiu, Xipeng},
294	    booktitle = {Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics},
295	    year      = {2023},
296	    url       = {https://aclanthology.org/2023.acl-long.855/},
297	}
298	
299	@inproceedings{adelie-2024,
300	    title     = {{ADELIE}: Aligning Large Language Models on Information Extraction},
301	    author    = {Qi, Yunjia and Peng, Hao and Wang, Xiaozhi and Xu, Bin and Hou, Lei and Li, Juanzi},
302	    booktitle = {Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing},
303	    year      = {2024},
304	    url       = {https://aclanthology.org/2024.emnlp-main.419/},
305	}
306	
307	@inproceedings{oneke-2025,
308	    title     = {{OneKE}: A Dockerized Schema-Guided {LLM} Agent-based Knowledge Extraction System},
309	    author    = {Luo, Yujie and Ru, Xiangyuan and Liu, Kangwei and Yuan, Lin and Sun, Mengshu and Zhang, Ningyu and Liang, Lei and Zhang, Zhiqiang and Zhou, Jun and Wei, Lanning and Zheng, Da and Wang, Haofen and Chen, Huajun},
310	    booktitle = {Companion Proceedings of the ACM Web Conference 2025},
311	    year      = {2025},
312	    url       = {https://arxiv.org/abs/2412.20005},
313	    doi       = {10.1145/3701716.3715189},
314	}
315	
316	
317	
318	
319	% =============================================================================
320	% DATASETS
321	% =============================================================================
322	
323	@inproceedings{fewnerd-2021,
324	    title     = {Few-{NERD}: A Few-shot Named Entity Recognition Dataset},
325	    author    = {Ding, Ning and Xu, Guangwei and Chen, Yulin and Wang, Xiaobin and Han, Xu and Xie, Pengjun and Zheng, Haitao and Liu, Zhiyuan},
326	    booktitle = {Proceedings of the 59th Annual Meeting of the Association for Computational Linguistics},
327	    year      = {2021},
328	    url       = {https://aclanthology.org/2021.acl-long.248/},
329	}
330	
331	@inproceedings{fewrel-2018,
332	    title     = {{FewRel}: A Large-Scale Supervised Few-Shot Relation Classification Dataset with State-of-the-Art Evaluation},
333	    author    = {Han, Xu and Zhu, Hao and Yu, Pengfei and Wang, Ziyun and Yao, Yuan and Liu, Zhiyuan and Sun, Maosong},
334	    booktitle = {Proceedings of the 2018 Conference on Empirical Methods in Natural Language Processing},
335	    year      = {2018},
336	    url       = {https://aclanthology.org/D18-1514/},
337	}
338	
339	@inproceedings{maven-2020,
340	    title     = {{MAVEN}: A Massive General Domain Event Detection Dataset},
341	    author    = {Wang, Xiaozhi and Wang, Ziqi and Han, Xu and Jiang, Wangyi and Han, Rong and Liu, Zhiyuan and Li, Juanzi and Li, Peng and Lin, Yankai and Zhou, Jie},
342	    booktitle = {Proceedings of the 2020 Conference on Empirical Methods in Natural Language Processing},
343	    year      = {2020},
344	    url       = {https://aclanthology.org/2020.emnlp-main.129/},
345	}
346	
347	@inproceedings{docred-2019,
348	    title     = {{DocRED}: A Large-Scale Document-Level Relation Extraction Dataset},
349	    author    = {Yao, Yuan and Ye, Deming and Li, Peng and Han, Xu and Lin, Yankai and Liu, Zhenghao and Liu, Zhiyuan and Huang, Lixin and Zhou, Jie and Sun, Maosong},
350	    booktitle = {Proceedings of the 57th Annual Meeting of the Association for Computational Linguistics},
351	    year      = {2019},
352	    url       = {https://aclanthology.org/P19-1074/},
353	}
354	
355	% =============================================================================
356	% MODELS AND TOOLS
357	% =============================================================================
358	
359	@article{qwen3-2025,
360	    title   = {Qwen3 Technical Report},
361	    author  = {{Qwen Team}},
362	    journal = {arXiv preprint arXiv:2505.09388},
363	    year    = {2025},
364	    url     = {https://arxiv.org/abs/2505.09388},
365	}
366	
367	@article{llama3-2024,
368	    title   = {The {Llama} 3 Herd of Models},
369	    author  = {Dubey, Abhimanyu and Jauhri, Abhinav and Pandey, Abhinav and Kadian, Abhishek and Al-Dahle, Ahmad and Letman, Aiesha and Mathur, Akhil and Schelten, Alan and Yang, Amy and Fan, Angela and others},
370	    journal = {arXiv preprint arXiv:2407.21783},
371	    year    = {2024},
372	    url     = {https://arxiv.org/abs/2407.21783},
373	}
374	
375	@inproceedings{sentence-bert-2019,
376	    title     = {Sentence-{BERT}: Sentence Embeddings using Siamese {BERT}-Networks},
377	    author    = {Reimers, Nils and Gurevych, Iryna},
378	    booktitle = {Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing},
379	    year      = {2019},
380	    url       = {https://aclanthology.org/D19-1410/},
381	}
382	
383	@inproceedings{minilm-2020,
384	    title     = {{MiniLM}: Deep Self-Attention Distillation for Task-Agnostic Compression of Pre-Trained Transformers},
385	    author    = {Wang, Wenhui and Wei, Furu and Dong, Li and Bao, Hangbo and Yang, Nan and Zhou, Ming},
386	    booktitle = {Advances in Neural Information Processing Systems},
387	    volume    = {33},
388	    year      = {2020},
389	    url       = {https://arxiv.org/abs/2002.10957},
390	}
391	
392	@inproceedings{reflect-learn-2026,
393	    title     = {Reflect then Learn: Active Prompting for Information Extraction Guided by Introspective Confusion},
394	    author    = {Zhao, Dong and Wang, Yadong and Chen, Xiang and Wang, Chenxi and Dai, Hongliang and Geng, Chuanxing and Zhang, Shengzhong and Li, Shaoyuan and Huang, Sheng-Jun},
395	    booktitle = {Proceedings of the AAAI Conference on Artificial Intelligence},
396	    volume    = {40},
397	    pages     = {34923--34931},
398	    year      = {2026},
399	    url       = {https://arxiv.org/abs/2508.10036},
400	    doi       = {10.1609/aaai.v40i41.40796},
401	}
402	
403	@inproceedings{sclar-sensitivity-2024,
404	    title     = {Quantifying Language Models' Sensitivity to Spurious Features in Prompt Design},
405	    author    = {Sclar, Melanie and Choi, Yejin and Tsvetkov, Yulia and Suhr, Alane},
406	    booktitle = {International Conference on Learning Representations},
407	    year      = {2024},
408	    url       = {https://arxiv.org/abs/2310.11324},
409	}
410	
411	@inproceedings{vllm-2023,
412	    title     = {Efficient Memory Management for Large Language Model Serving with {PagedAttention}},
413	    author    = {Kwon, Woosuk and Li, Zhuohan and Zhuang, Siyuan and Sheng, Ying and Zheng, Lianmin and Yu, Cody Hao and Gonzalez, Joseph E. and Zhang, Hao and Stoica, Ion},
414	    booktitle = {Proceedings of the 29th Symposium on Operating Systems Principles},
415	    year      = {2023},
416	    url       = {https://dl.acm.org/doi/10.1145/3600006.3613165},
417	}
418	
419	@inproceedings{xie-zeroshot-ner-2023,
420	    title     = {Empirical Study of Zero-Shot {NER} with {ChatGPT}},
421	    author    = {Xie, Tingyu and Li, Qi and Zhang, Jian and Zhang, Yan and Liu, Zuozhu and Wang, Hongwei},
422	    booktitle = {Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing},
423	    year      = {2023},
424	    url       = {https://aclanthology.org/2023.emnlp-main.493/},
425	}
426	
427	@inproceedings{wadhwa-re-llm-2023,
428	    title     = {Revisiting Relation Extraction in the era of Large Language Models},
429	    author    = {Wadhwa, Somin and Amir, Silvio and Wallace, Byron C.},
430	    booktitle = {Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics},
431	    pages     = {15566--15589},
432	    year      = {2023},
433	    url       = {https://aclanthology.org/2023.acl-long.868/},
434	}
435	
436	@inproceedings{relationprompt-2022,
437	    title     = {{RelationPrompt}: Leveraging Prompts to Generate Synthetic Data for Zero-Shot Relation Triplet Extraction},
438	    author    = {Chia, Yew Ken and Bing, Lidong and Poria, Soujanya and Si, Luo},
439	    booktitle = {Findings of the Association for Computational Linguistics: ACL 2022},
440	    pages     = {45--57},
441	    year      = {2022},
442	    url       = {https://aclanthology.org/2022.findings-acl.5/},
443	}
444	
445	@article{promptner-2023,
446	    title   = {{PromptNER}: Prompting For Named Entity Recognition},
447	    author  = {Ashok, Dhananjay and Lipton, Zachary C.},
448	    journal = {arXiv preprint arXiv:2305.15444},
449	    year    = {2023},
450	    url     = {https://arxiv.org/abs/2305.15444},
451	}
452	
453	@article{json-schema-bench-2025,
454	    title   = {{JSONSchemaBench}: A Rigorous Benchmark of Structured Outputs for Language Models},
455	    author  = {Geng, Saibo and Cooper, Hudson and Moskal, Micha{\l} and Jenkins, Samuel and Berman, Julian and Ranchin, Nathan and West, Robert and Horvitz, Eric and Nori, Harsha},
456	    journal = {arXiv preprint arXiv:2501.10868},
457	    year    = {2025},
458	    url     = {https://arxiv.org/abs/2501.10868},
459	}
460	
461	@inproceedings{rastogi2020towards,
462	    title     = {Towards Scalable Multi-Domain Conversational Agents: The Schema-Guided Dialogue Dataset},
463	    author    = {Rastogi, Abhinav and Zang, Xiaoxue and Sunkara, Srinivas and Gupta, Raghav and Khaitan, Pranav},
464	    booktitle = {Proceedings of the AAAI Conference on Artificial Intelligence},
465	    volume    = {34},
466	    pages     = {8689--8696},
467	    year      = {2020},
468	    url       = {https://arxiv.org/abs/1909.05855},
469	}
470	
471	@article{li2023evaluating,
472	    title   = {Evaluating {ChatGPT}'s Information Extraction Capabilities: An Assessment of Performance, Explainability, Calibration, and Faithfulness},
473	    author  = {Li, Bo and Fang, Gexiang and Yang, Yang and Wang, Quansen and Ye, Wei and Zhao, Wen and Zhang, Shikun},
474	    journal = {arXiv preprint arXiv:2304.11633},
475	    year    = {2023},
476	    url     = {https://arxiv.org/abs/2304.11633},
477	}
478	
479	@inproceedings{lee2022sgd,
480	    title     = {{SGD-X}: A Benchmark for Robust Generalization in Schema-Guided Dialogue Systems},
481	    author    = {Lee, Harrison and Gupta, Raghav and Rastogi, Abhinav and Cao, Yuan and Zhang, Bin and Wu, Yonghui},
482	    booktitle = {Proceedings of the AAAI Conference on Artificial Intelligence},
483	    volume    = {36},
484	    pages     = {10938--10946},
485	    year      = {2022},
486	    url       = {https://arxiv.org/abs/2110.06800},
487	}
488	
489	@article{volkanovska2025ner,
490	    title   = {A Study of Errors in the Output of Large Language Models for Domain-Specific Few-Shot Named Entity Recognition},
491	    author  = {Volkanovska, Elena},
492	    journal = {Journal for Language Technology and Computational Linguistics},
493	    volume  = {38},
494	    number  = {2},
495	    pages   = {31--42},
496	    year    = {2025},
497	    url     = {https://jlcl.org/article/view/281/263},
498	}
499	
500	@article{haystack-to-needle-2025,
501	    title   = {From Haystack to Needle: Label Space Reduction for Zero-shot Classification},
502	    author  = {Vandemoortele, Nathan and Steenwinckel, Bram and Ongenae, Femke and Van Hoecke, Sofie},
503	    journal = {arXiv preprint arXiv:2502.08436},
504	    year    = {2025},
505	    url     = {https://arxiv.org/abs/2502.08436},
506	}
507	
508	@book{cohen-1988-power,
509	    title     = {Statistical Power Analysis for the Behavioral Sciences},
510	    author    = {Cohen, Jacob},
511	    edition   = {2nd},
512	    publisher = {Routledge},
513	    year      = {1988},
514	    doi       = {10.4324/9780203771587},
515	}
516	
517	@article{lakens-2013-effect-size,
518	    title   = {Calculating and Reporting Effect Sizes to Facilitate Cumulative Science: A Practical Primer for t-Tests and {ANOVA}s},
519	    author  = {Lakens, Dani{\"e}l},
520	    journal = {Frontiers in Psychology},
521	    volume  = {4},
522	    pages   = {863},
523	    year    = {2013},
524	    doi     = {10.3389/fpsyg.2013.00863},
525	}
526	
527	@inproceedings{deng-2010-imagenet,
528	    title     = {What Does Classifying More Than 10,000 Image Categories Tell Us?},
529	    author    = {Deng, Jia and Berg, Alexander C. and Li, Kai and Fei-Fei, Li},
530	    booktitle = {Proceedings of the 11th European Conference on Computer Vision},
531	    pages     = {71--84},
532	    year      = {2010},
533	    doi       = {10.1007/978-3-642-15555-0\_6},
534	}
535	
536	@article{rothman-1990,
537	    title   = {No Adjustments Are Needed for Multiple Comparisons},
538	    author  = {Rothman, Kenneth J.},
539	    journal = {Epidemiology},
540	    volume  = {1},
541	    number  = {1},
542	    pages   = {43--46},
543	    year    = {1990},
544	    doi     = {10.1097/00001648-199001000-00010},
545	}
546	
547	@article{lakens-2017-equivalence,
548	    title   = {Equivalence Tests: A Practical Primer for t Tests, Correlations, and Meta-Analyses},
549	    author  = {Lakens, Dani{\"e}l},
550	    journal = {Social Psychological and Personality Science},
551	    volume  = {8},
552	    number  = {4},
553	    pages   = {355--362},
554	    year    = {2017},
555	    doi     = {10.1177/1948550617697177},
556	}
557	
558	
559	@inproceedings{zhou-2025-rethinking,
560	    title     = {Rethinking Word Similarity: Semantic Similarity through Classification Confusion},
561	    author    = {Zhou, Kaitlyn and Gao, Haishan and Chen, Sarah Li and Edelstein, Dan and Jurafsky, Dan and Shani, Chen},
562	    booktitle = {Proceedings of the 2025 Conference of the North American Chapter of the Association for Computational Linguistics},
563	    pages     = {5803--5817},
564	    year      = {2025},
565	    doi       = {10.18653/v1/2025.naacl-long.299},
566	}
567	
568	@inproceedings{guo-2021-label-confusion,
569	    title     = {Label Confusion Learning to Enhance Text Classification Models},
570	    author    = {Guo, Biyang and Han, Songqiao and Han, Xiao and Huang, Hailiang and Lu, Ting},
571	    booktitle = {Proceedings of the AAAI Conference on Artificial Intelligence},
572	    volume    = {35},
573	    number    = {14},
574	    pages     = {12929--12936},
575	    year      = {2021},
576	    doi       = {10.1609/aaai.v35i14.17529},
577	}
578	
579	@inproceedings{novack-2023-chils,
580	    title     = {{CHiLS}: Zero-Shot Image Classification with Hierarchical Label Sets},
581	    author    = {Novack, Zachary and McAuley, Julian and Lipton, Zachary Chase and Garg, Saurabh},
582	    booktitle = {Proceedings of the 40th International Conference on Machine Learning},
583	    series    = {Proceedings of Machine Learning Research},
584	    volume    = {202},
585	    pages     = {26342--26362},
586	    year      = {2023},
587	    url       = {https://proceedings.mlr.press/v202/novack23a.html},
588	}
589	
590	@inproceedings{cocchieri-2025-zeroner,
591	    title     = {{ZeroNER}: Fueling Zero-Shot Named Entity Recognition via Entity Type Descriptions},
592	    author    = {Cocchieri, Alessio and Mart{\'\i}nez Galindo, Marcos and Frisoni, Giacomo and Moro, Gianluca and Sartori, Claudio and Tagliavini, Giuseppe},
593	    booktitle = {Findings of the Association for Computational Linguistics: ACL 2025},
594	    pages     = {15594--15616},
595	    year      = {2025},
596	    doi       = {10.18653/v1/2025.findings-acl.805},
597	}
598	
599	@article{dlisc-2025,
600	    title     = {Effective and Efficient Schema-aware Information Extraction Using On-Device Large Language Models},
601	    author    = {Li, Zhuoqun and Wu, Hao and Li, Xinxin and Li, Zhoujun},
602	    journal   = {arXiv preprint arXiv:2505.14992},
603	    year      = {2025},
604	    url       = {https://arxiv.org/abs/2505.14992}
605	}
606	
607	@article{spt-2025,
608	    title     = {Schema as Parameterized Tools for Universal Information Extraction},
609	    author    = {Liang, Sheng and Zhang, Yongyue and Wu, Yaxiong and Tang, Ruiming and Liu, Yong},
610	    journal   = {arXiv preprint arXiv:2506.01276},
611	    year      = {2025},
612	    url       = {https://arxiv.org/abs/2506.01276}
613	}
614	
615	@inproceedings{card-2020-power,
616	    title     = {With Little Power Comes Great Responsibility},
617	    author    = {Card, Dallas and Henderson, Peter and Khandelwal, Urvashi and Jia, Robin and Mahowald, Kyle and Jurafsky, Dan},
618	    booktitle = {Proceedings of the 2020 Conference on Empirical Methods in Natural Language Processing (EMNLP)},
619	    pages     = {9263--9274},
620	    year      = {2020},
621	    publisher = {Association for Computational Linguistics},
622	    url       = {https://aclanthology.org/2020.emnlp-main.745}
623	}
624	
625	@article{gillick-2014-entity-typing,
626	    title     = {Context-Dependent Fine-Grained Entity Type Tagging},
627	    author    = {Gillick, Daniel and Lazic, Nevena and Ganchev, Kuzman and Kirchner, Jesse and Huynh, David},
628	    journal   = {arXiv preprint arXiv:1412.1820},
629	    year      = {2014},
630	    url       = {https://arxiv.org/abs/1412.1820}
631	}
632	
633	@inproceedings{schall-2025-hidden-cost,
634	    title     = {The Hidden Cost of Structure: How Constrained Decoding Affects Language Model Performance},
635	    author    = {Schall, Maximilian and de Melo, Gerard},
636	    booktitle = {Proceedings of the 15th International Conference on Recent Advances in Natural Language Processing (RANLP)},
637	    pages     = {1074--1084},
638	    year      = {2025},
639	    address   = {Varna, Bulgaria},
640	    url       = {https://aclanthology.org/2025.ranlp-1.124}
641	}
642	
643	@article{chen-2026-multi-instance,
644	    title     = {Understanding {LLM} Performance Degradation in Multi-Instance Processing: The Roles of Instance Count and Context Length},
645	    author    = {Chen, Jingxuan and Pilehvar, Mohammad Taher and Camacho-Collados, Jose},
646	    journal   = {arXiv preprint arXiv:2603.22608},
647	    year      = {2026},
648	    url       = {https://arxiv.org/abs/2603.22608}
649	}
650	
651	@article{wei-2023-chatie,
652	    title     = {Zero-Shot Information Extraction via Chatting with {ChatGPT}},
653	    author    = {Wei, Xiang and Cui, Xingyu and Cheng, Ning and Wang, Xiaobin and Zhang, Xin and Huang, Shen and Xie, Pengjun and Xu, Jinan and Chen, Yufeng and Zhang, Meishan and Jiang, Yong and Han, Wenjuan},
654	    journal   = {arXiv preprint arXiv:2302.10205},
655	    year      = {2023},
656	    url       = {https://arxiv.org/abs/2302.10205}
657	}
658	
659	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6c3727a5-ed97-4544-b562-0b8bf577919c",
  "isSidechain": false,
  "promptId": "8257bd0e-08b4-4530-aa87-1e185ea40a51",
  "type": "user",
  "uuid": "c2b0c6d6-16c0-43cd-9c9c-4e2909cdc098",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/references.bib",
      "content": "@inproceedings{tam-2024-let-me-speak,\n  title     = {Let Me Speak Freely? {A} Study on the Impact of Format Restrictions on Performance of Large Language Models},\n  author    = {Tam, Zhi Rui and Wu, Cheng-Kuang and Tsai, Yi-Lin and Lin, Chieh-Yen and Lee, Hung-yi and Chen, Yun-Nung},\n  booktitle = {Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing: Industry Track},\n  year      = {2024},\n  url       = {https://arxiv.org/abs/2408.02442}\n}\n\n@inproceedings{yin-2019-zero-shot-bench,\n  title     = {Benchmarking Zero-shot Text Classification: Datasets, Evaluation and Entailment Approach},\n  author    = {Yin, Wenpeng and Hay, Jamaal and Roth, Dan},\n  booktitle = {Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing},\n  pages     = {3914--3923},\n  year      = {2019},\n  url       = {https://arxiv.org/abs/1909.00161}\n}\n\n@article{schuirmann-1987-tost,\n  title     = {A Comparison of the Two One-Sided Tests Procedure and the Power Approach for Assessing the Equivalence of Average Bioavailability},\n  author    = {Schuirmann, Donald J.},\n  journal   = {Journal of Pharmacokinetics and Biopharmaceutics},\n  volume    = {15},\n  number    = {6},\n  pages     = {657--680},\n  year      = {1987},\n  doi       = {10.1007/BF01068419}\n}\n\n@article{gemini-2025,\n  title     = {Gemini 2.5: Pushing the Frontier with Advanced Reasoning, Multimodality, and Long Context},\n  author    = {Comanici, Gheorghe and others},\n  journal   = {arXiv preprint arXiv:2507.06261},\n  year      = {2025},\n  url       = {https://arxiv.org/abs/2507.06261}\n}\n\n@inproceedings{snell2017prototypical,\n  title     = {Prototypical Networks for Few-shot Learning},\n  author    = {Snell, Jake and Swersky, Kevin and Zemel, Richard},\n  booktitle = {Advances in Neural Information Processing Systems},\n  volume    = {30},\n  year      = {2017}\n}\n\n@inproceedings{muller2019when,\n  title     = {When Does Label Smoothing Help?},\n  author    = {M{\\\"u}ller, Rafael and Kornblith, Simon and Hinton, Geoffrey E.},\n  booktitle = {Advances in Neural Information Processing Systems},\n  volume    = {32},\n  year      = {2019}\n}\n\n@inproceedings{peterson2019human,\n  title     = {Human Uncertainty Makes Classification More Robust},\n  author    = {Peterson, Joshua C. and Battleday, Ruairidh M. and Griffiths, Thomas L. and Russakovsky, Olga},\n  booktitle = {Proceedings of the IEEE/CVF International Conference on Computer Vision},\n  pages     = {9617--9626},\n  year      = {2019}\n}\n\n@inproceedings{jagannatha2020calibrating,\n  title     = {Calibrating Structured Output Predictors for Natural Language Processing},\n  author    = {Jagannatha, Abhyuday and Yu, Hong},\n  booktitle = {Proceedings of the 58th Annual Meeting of the Association for Computational Linguistics},\n  pages     = {2078--2092},\n  year      = {2020}\n}\n\n@article{willard2023efficient,\n  title     = {Efficient Guided Generation for Large Language Models},\n  author    = {Willard, Brandon T. and Louf, R{\\'e}mi},\n  journal   = {arXiv preprint arXiv:2307.09702},\n  year      = {2023},\n  url       = {https://arxiv.org/abs/2307.09702}\n}\n\n\n@inproceedings{lu2022fantastically,\n  title     = {Fantastically Ordered Prompts and Where to Find Them: Overcoming Few-Shot Prompt Order Sensitivity},\n  author    = {Lu, Yao and Bartolo, Max and Moore, Alastair and Riedel, Sebastian and Stenetorp, Pontus},\n  booktitle = {Proceedings of the 60th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)},\n  pages     = {8086--8098},\n  year      = {2022},\n  url       = {https://aclanthology.org/2022.acl-long.556/},\n  doi       = {10.18653/v1/2022.acl-long.556}\n}\n\n@inproceedings{yang2025beyond,\n  title     = {Beyond Boundaries: Learning a Universal Entity Taxonomy across Datasets and Languages for Open Named Entity Recognition},\n  author    = {Yang, Yuming and Zhao, Wantong and Huang, Caishuang and Ye, Junjie and Wang, Xiao and Zheng, Huiyuan and Nan, Yang and Wang, Yuran and Xu, Xueying and Huang, Kaixin and Zhang, Yunke and Gui, Tao and Zhang, Qi and Huang, Xuanjing},\n  booktitle = {Proceedings of the 31st International Conference on Computational Linguistics},\n  pages     = {10902--10923},\n  year      = {2025},\n  url       = {https://aclanthology.org/2025.coling-main.725/}\n}\n\n% =============================================================================\n% DIRECT COMPETITORS\n% =============================================================================\n\n@inproceedings{llm-pee-2025,\n    title     = {Towards Event Extraction with Massive Types: {LLM}-based Collaborative Annotation and Partitioning Extraction},\n    author    = {Liu, Wenxuan and Li, Zixuan and Bai, Long and Zuo, Yuxin and Xu, Daozhu and Jin, Xiaolong and Guo, Jiafeng and Cheng, Xueqi},\n    booktitle = {Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing},\n    year      = {2025},\n    url       = {https://aclanthology.org/2025.emnlp-main.1743/},\n}\n\n@inproceedings{parse-2025,\n    title     = {{PARSE}: {LLM} Driven Schema Optimization for Reliable Entity Extraction},\n    author    = {Shrimal, Anubhav and Jain, Aryan and Chowdhury, Soumyajit and Yenigalla, Promod},\n    booktitle = {Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing: Industry Track},\n    year      = {2025},\n    url       = {https://aclanthology.org/2025.emnlp-industry.184/},\n}\n\n@inproceedings{dee-2024,\n    title     = {Decompose, Enrich, and Extract! Schema-aware Event Extraction using {LLM}s},\n    author    = {Shiri, Fatemeh and Nguyen, Van and Moghimifar, Farhad and Yoo, John and Haffari, Gholamreza and Li, Yuan-Fang},\n    booktitle = {Proceedings of the IEEE International Conference on Tools with Artificial Intelligence},\n    year      = {2024},\n    url       = {https://arxiv.org/abs/2406.01045},\n}\n\n@inproceedings{crossagentie-2025,\n    title     = {{CROSSAGENTIE}: Cross-Type and Cross-Task Multi-Agent {LLM} Collaboration for Zero-Shot Information Extraction},\n    author    = {Lu, Meng and Xie, Yuzhang and Bi, Zhenyu and Cao, Shuxiang and Wang, Xuan},\n    booktitle = {Findings of the Association for Computational Linguistics: ACL 2025},\n    year      = {2025},\n    url       = {https://aclanthology.org/2025.findings-acl.718/},\n}\n\n\n@inproceedings{cmas-ner-2025,\n    title     = {A Cooperative Multi-Agent Framework for Zero-Shot Named Entity Recognition},\n    author    = {Wang, Zihan and Zhao, Ziqi and Lyu, Yougang and Chen, Zhumin and de Rijke, Maarten and Ren, Zhaochun},\n    booktitle = {Proceedings of the ACM Web Conference 2025},\n    year      = {2025},\n    url       = {https://dl.acm.org/doi/10.1145/3696410.3714923},\n    doi       = {10.1145/3696410.3714923},\n}\n\n% =============================================================================\n% METHOD COMPONENTS\n% =============================================================================\n\n@inproceedings{uniner-2024,\n    title     = {{UniversalNER}: Targeted Distillation from Large Language Models for Open Named Entity Recognition},\n    author    = {Zhou, Wenxuan and Zhang, Sheng and Gu, Yu and Chen, Muhao and Poon, Hoifung},\n    booktitle = {International Conference on Learning Representations},\n    year      = {2024},\n    url       = {https://arxiv.org/abs/2308.03279},\n}\n\n@inproceedings{gollie-2024,\n    title     = {{GoLLIE}: Annotation Guidelines improve Zero-Shot Information-Extraction},\n    author    = {Sainz, Oscar and Garc{\\'\\i}a-Ferrero, Iker and Agerri, Rodrigo and Lopez de Lacalle, Oier and Rigau, German and Agirre, Eneko},\n    booktitle = {International Conference on Learning Representations},\n    year      = {2024},\n    url       = {https://arxiv.org/abs/2310.03668},\n}\n\n@inproceedings{gliner-2024,\n    title     = {{GLiNER}: Generalist Model for Named Entity Recognition using Bidirectional Transformer},\n    author    = {Zaratiana, Urchade and Tomeh, Nadi and Holat, Pierre and Charnois, Thierry},\n    booktitle = {Proceedings of the 2024 Conference of the North American Chapter of the Association for Computational Linguistics},\n    year      = {2024},\n    url       = {https://arxiv.org/abs/2311.08526},\n}\n\n@inproceedings{gliner2-2025,\n    title     = {{GLiNER2}: Schema-Driven Multi-Task Learning for Structured Information Extraction},\n    author    = {Zaratiana, Urchade and Pasternak, Gil and Boyd, Oliver and Hurn-Maloney, George and Lewis, Ash},\n    booktitle = {Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing: System Demonstrations},\n    year      = {2025},\n    url       = {https://aclanthology.org/2025.emnlp-demos.10/},\n}\n\n\n@inproceedings{iepile-2024,\n    title     = {{IEPile}: Unearthing Large Scale Schema-Conditioned Information Extraction Corpus},\n    author    = {Gui, Honghao and Yuan, Lin and Ye, Hongbin and Zhang, Ningyu and Sun, Mengshu and Liang, Lei and Chen, Huajun},\n    booktitle = {Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (Volume 2: Short Papers)},\n    pages     = {127--146},\n    year      = {2024},\n    url       = {https://aclanthology.org/2024.acl-short.13/},\n}\n\n\n@inproceedings{dror-2018-significance,\n    title     = {The Hitchhiker's Guide to Testing Statistical Significance in Natural Language Processing},\n    author    = {Dror, Rotem and Baumer, Gili and Shlomov, Segev and Reichart, Roi},\n    booktitle = {Proceedings of the 56th Annual Meeting of the Association for Computational Linguistics},\n    year      = {2018},\n    url       = {https://aclanthology.org/P18-1128/},\n}\n\n@article{lost-in-middle-2024,\n    title   = {Lost in the Middle: How Language Models Use Long Contexts},\n    author  = {Liu, Nelson F. and Lin, Kevin and Hewitt, John and Paranjape, Ashwin and Bevilacqua, Michele and Petroni, Fabio and Liang, Percy},\n    journal = {Transactions of the Association for Computational Linguistics},\n    volume  = {12},\n    pages   = {157--173},\n    year    = {2024},\n    url     = {https://arxiv.org/abs/2307.03172},\n    doi     = {10.1162/tacl_a_00638},\n}\n\n% =============================================================================\n% ZERO-SHOT NER / RE BASELINES\n% =============================================================================\n\n\n\n% =============================================================================\n% EVALUATION / BENCHMARKING\n% =============================================================================\n\n% =============================================================================\n% SURVEYS / BACKGROUND\n% =============================================================================\n\n@article{llm4ie-survey-2024,\n    title   = {Large Language Models for Generative Information Extraction: A Survey},\n    author  = {Xu, Derong and Chen, Wei and Peng, Wenjun and Zhang, Chao and Xu, Tong and Zhao, Xiangyu and Wu, Xian and Zheng, Yefeng and Wang, Yang and Chen, Enhong},\n    journal = {Frontiers of Computer Science},\n    volume  = {18},\n    number  = {6},\n    year    = {2024},\n    url     = {https://arxiv.org/abs/2312.17617},\n    doi     = {10.1007/s11704-024-40555-y},\n}\n\n@inproceedings{knowcoder-2024,\n    title     = {{KnowCoder}: Coding Structured Knowledge into {LLM}s for Universal Information Extraction},\n    author    = {Li, Zixuan and Zeng, Yutao and Zuo, Yuxin and Ren, Weicheng and Liu, Wenxuan and Su, Miao and Guo, Yucan and Liu, Yantao and Li, Xiang and Hu, Zhilei and Bai, Long and Li, Wei and Liu, Yidan and Yang, Pan and Jin, Xiaolong and Guo, Jiafeng and Cheng, Xueqi},\n    booktitle = {Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics},\n    year      = {2024},\n    url       = {https://arxiv.org/abs/2403.07969},\n}\n\n@inproceedings{slot-2025,\n    title     = {{SLOT}: Structuring the Output of Large Language Models},\n    author    = {Shen, Zhengyuan and Wang, Darren Yow-Bang and Mishra, Soumya Smruti and Xu, Zhichao and Teng, Yifei and Ding, Haibo},\n    booktitle = {Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing: Industry Track},\n    year      = {2025},\n    url       = {https://aclanthology.org/2025.emnlp-industry.32/},\n}\n\n% =============================================================================\n% EMBEDDING ANISOTROPY / REPRESENTATION DEGENERATION\n% =============================================================================\n\n@inproceedings{gao-repr-degen-2019,\n    title     = {Representation Degeneration Problem in Training Natural Language Generation Models},\n    author    = {Gao, Jun and He, Di and Tan, Xu and Qin, Tao and Wang, Liwei and Liu, Tie-Yan},\n    booktitle = {International Conference on Learning Representations},\n    year      = {2019},\n    url       = {https://arxiv.org/abs/1907.12009},\n}\n\n@inproceedings{ethayarajh-contextual-2019,\n    title     = {How Contextual are Contextualized Word Representations? {C}omparing the Geometry of {BERT}, {ELMo}, and {GPT-2} Embeddings},\n    author    = {Ethayarajh, Kawin},\n    booktitle = {Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing and the 9th International Joint Conference on Natural Language Processing},\n    year      = {2019},\n    url       = {https://aclanthology.org/D19-1006/},\n}\n\n@inproceedings{cai-isotropy-clusters-2021,\n    title     = {Isotropy in the Contextual Embedding Space: Clusters and Manifolds},\n    author    = {Cai, Xingyu and Huang, Jiaji and Bian, Yuchen and Church, Kenneth},\n    booktitle = {International Conference on Learning Representations},\n    year      = {2021},\n    url       = {https://openreview.net/forum?id=xYGNO86OWDH},\n}\n\n\n% =============================================================================\n% ADDITIONAL REFERENCES (from references_survey.md only)\n% =============================================================================\n\n@article{instructuie-2023,\n    title   = {{InstructUIE}: Multi-task Instruction Tuning for Unified Information Extraction},\n    author  = {Wang, Xiao and Zhou, Weikang and Zu, Can and Xia, Han and Chen, Tianze and Zhang, Yuansen and Zheng, Rui and Ye, Junjie and Zhang, Qi and Gui, Tao and Kang, Jihua and Yang, Jingsheng and Li, Siyuan and Du, Chunsai},\n    journal = {arXiv preprint arXiv:2304.08085},\n    year    = {2023},\n    url     = {https://arxiv.org/abs/2304.08085},\n}\n\n@inproceedings{codeie-2023,\n    title     = {{CodeIE}: Large Code Generation Models are Better Few-Shot Information Extractors},\n    author    = {Li, Peng and Sun, Tianxiang and Tang, Qiong and Yan, Hang and Wu, Yuanbin and Huang, Xuanjing and Qiu, Xipeng},\n    booktitle = {Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics},\n    year      = {2023},\n    url       = {https://aclanthology.org/2023.acl-long.855/},\n}\n\n@inproceedings{adelie-2024,\n    title     = {{ADELIE}: Aligning Large Language Models on Information Extraction},\n    author    = {Qi, Yunjia and Peng, Hao and Wang, Xiaozhi and Xu, Bin and Hou, Lei and Li, Juanzi},\n    booktitle = {Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing},\n    year      = {2024},\n    url       = {https://aclanthology.org/2024.emnlp-main.419/},\n}\n\n@inproceedings{oneke-2025,\n    title     = {{OneKE}: A Dockerized Schema-Guided {LLM} Agent-based Knowledge Extraction System},\n    author    = {Luo, Yujie and Ru, Xiangyuan and Liu, Kangwei and Yuan, Lin and Sun, Mengshu and Zhang, Ningyu and Liang, Lei and Zhang, Zhiqiang and Zhou, Jun and Wei, Lanning and Zheng, Da and Wang, Haofen and Chen, Huajun},\n    booktitle = {Companion Proceedings of the ACM Web Conference 2025},\n    year      = {2025},\n    url       = {https://arxiv.org/abs/2412.20005},\n    doi       = {10.1145/3701716.3715189},\n}\n\n\n\n\n% =============================================================================\n% DATASETS\n% =============================================================================\n\n@inproceedings{fewnerd-2021,\n    title     = {Few-{NERD}: A Few-shot Named Entity Recognition Dataset},\n    author    = {Ding, Ning and Xu, Guangwei and Chen, Yulin and Wang, Xiaobin and Han, Xu and Xie, Pengjun and Zheng, Haitao and Liu, Zhiyuan},\n    booktitle = {Proceedings of the 59th Annual Meeting of the Association for Computational Linguistics},\n    year      = {2021},\n    url       = {https://aclanthology.org/2021.acl-long.248/},\n}\n\n@inproceedings{fewrel-2018,\n    title     = {{FewRel}: A Large-Scale Supervised Few-Shot Relation Classification Dataset with State-of-the-Art Evaluation},\n    author    = {Han, Xu and Zhu, Hao and Yu, Pengfei and Wang, Ziyun and Yao, Yuan and Liu, Zhiyuan and Sun, Maosong},\n    booktitle = {Proceedings of the 2018 Conference on Empirical Methods in Natural Language Processing},\n    year      = {2018},\n    url       = {https://aclanthology.org/D18-1514/},\n}\n\n@inproceedings{maven-2020,\n    title     = {{MAVEN}: A Massive General Domain Event Detection Dataset},\n    author    = {Wang, Xiaozhi and Wang, Ziqi and Han, Xu and Jiang, Wangyi and Han, Rong and Liu, Zhiyuan and Li, Juanzi and Li, Peng and Lin, Yankai and Zhou, Jie},\n    booktitle = {Proceedings of the 2020 Conference on Empirical Methods in Natural Language Processing},\n    year      = {2020},\n    url       = {https://aclanthology.org/2020.emnlp-main.129/},\n}\n\n@inproceedings{docred-2019,\n    title     = {{DocRED}: A Large-Scale Document-Level Relation Extraction Dataset},\n    author    = {Yao, Yuan and Ye, Deming and Li, Peng and Han, Xu and Lin, Yankai and Liu, Zhenghao and Liu, Zhiyuan and Huang, Lixin and Zhou, Jie and Sun, Maosong},\n    booktitle = {Proceedings of the 57th Annual Meeting of the Association for Computational Linguistics},\n    year      = {2019},\n    url       = {https://aclanthology.org/P19-1074/},\n}\n\n% =============================================================================\n% MODELS AND TOOLS\n% =============================================================================\n\n@article{qwen3-2025,\n    title   = {Qwen3 Technical Report},\n    author  = {{Qwen Team}},\n    journal = {arXiv preprint arXiv:2505.09388},\n    year    = {2025},\n    url     = {https://arxiv.org/abs/2505.09388},\n}\n\n@article{llama3-2024,\n    title   = {The {Llama} 3 Herd of Models},\n    author  = {Dubey, Abhimanyu and Jauhri, Abhinav and Pandey, Abhinav and Kadian, Abhishek and Al-Dahle, Ahmad and Letman, Aiesha and Mathur, Akhil and Schelten, Alan and Yang, Amy and Fan, Angela and others},\n    journal = {arXiv preprint arXiv:2407.21783},\n    year    = {2024},\n    url     = {https://arxiv.org/abs/2407.21783},\n}\n\n@inproceedings{sentence-bert-2019,\n    title     = {Sentence-{BERT}: Sentence Embeddings using Siamese {BERT}-Networks},\n    author    = {Reimers, Nils and Gurevych, Iryna},\n    booktitle = {Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing},\n    year      = {2019},\n    url       = {https://aclanthology.org/D19-1410/},\n}\n\n@inproceedings{minilm-2020,\n    title     = {{MiniLM}: Deep Self-Attention Distillation for Task-Agnostic Compression of Pre-Trained Transformers},\n    author    = {Wang, Wenhui and Wei, Furu and Dong, Li and Bao, Hangbo and Yang, Nan and Zhou, Ming},\n    booktitle = {Advances in Neural Information Processing Systems},\n    volume    = {33},\n    year      = {2020},\n    url       = {https://arxiv.org/abs/2002.10957},\n}\n\n@inproceedings{reflect-learn-2026,\n    title     = {Reflect then Learn: Active Prompting for Information Extraction Guided by Introspective Confusion},\n    author    = {Zhao, Dong and Wang, Yadong and Chen, Xiang and Wang, Chenxi and Dai, Hongliang and Geng, Chuanxing and Zhang, Shengzhong and Li, Shaoyuan and Huang, Sheng-Jun},\n    booktitle = {Proceedings of the AAAI Conference on Artificial Intelligence},\n    volume    = {40},\n    pages     = {34923--34931},\n    year      = {2026},\n    url       = {https://arxiv.org/abs/2508.10036},\n    doi       = {10.1609/aaai.v40i41.40796},\n}\n\n@inproceedings{sclar-sensitivity-2024,\n    title     = {Quantifying Language Models' Sensitivity to Spurious Features in Prompt Design},\n    author    = {Sclar, Melanie and Choi, Yejin and Tsvetkov, Yulia and Suhr, Alane},\n    booktitle = {International Conference on Learning Representations},\n    year      = {2024},\n    url       = {https://arxiv.org/abs/2310.11324},\n}\n\n@inproceedings{vllm-2023,\n    title     = {Efficient Memory Management for Large Language Model Serving with {PagedAttention}},\n    author    = {Kwon, Woosuk and Li, Zhuohan and Zhuang, Siyuan and Sheng, Ying and Zheng, Lianmin and Yu, Cody Hao and Gonzalez, Joseph E. and Zhang, Hao and Stoica, Ion},\n    booktitle = {Proceedings of the 29th Symposium on Operating Systems Principles},\n    year      = {2023},\n    url       = {https://dl.acm.org/doi/10.1145/3600006.3613165},\n}\n\n@inproceedings{xie-zeroshot-ner-2023,\n    title     = {Empirical Study of Zero-Shot {NER} with {ChatGPT}},\n    author    = {Xie, Tingyu and Li, Qi and Zhang, Jian and Zhang, Yan and Liu, Zuozhu and Wang, Hongwei},\n    booktitle = {Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing},\n    year      = {2023},\n    url       = {https://aclanthology.org/2023.emnlp-main.493/},\n}\n\n@inproceedings{wadhwa-re-llm-2023,\n    title     = {Revisiting Relation Extraction in the era of Large Language Models},\n    author    = {Wadhwa, Somin and Amir, Silvio and Wallace, Byron C.},\n    booktitle = {Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics},\n    pages     = {15566--15589},\n    year      = {2023},\n    url       = {https://aclanthology.org/2023.acl-long.868/},\n}\n\n@inproceedings{relationprompt-2022,\n    title     = {{RelationPrompt}: Leveraging Prompts to Generate Synthetic Data for Zero-Shot Relation Triplet Extraction},\n    author    = {Chia, Yew Ken and Bing, Lidong and Poria, Soujanya and Si, Luo},\n    booktitle = {Findings of the Association for Computational Linguistics: ACL 2022},\n    pages     = {45--57},\n    year      = {2022},\n    url       = {https://aclanthology.org/2022.findings-acl.5/},\n}\n\n@article{promptner-2023,\n    title   = {{PromptNER}: Prompting For Named Entity Recognition},\n    author  = {Ashok, Dhananjay and Lipton, Zachary C.},\n    journal = {arXiv preprint arXiv:2305.15444},\n    year    = {2023},\n    url     = {https://arxiv.org/abs/2305.15444},\n}\n\n@article{json-schema-bench-2025,\n    title   = {{JSONSchemaBench}: A Rigorous Benchmark of Structured Outputs for Language Models},\n    author  = {Geng, Saibo and Cooper, Hudson and Moskal, Micha{\\l} and Jenkins, Samuel and Berman, Julian and Ranchin, Nathan and West, Robert and Horvitz, Eric and Nori, Harsha},\n    journal = {arXiv preprint arXiv:2501.10868},\n    year    = {2025},\n    url     = {https://arxiv.org/abs/2501.10868},\n}\n\n@inproceedings{rastogi2020towards,\n    title     = {Towards Scalable Multi-Domain Conversational Agents: The Schema-Guided Dialogue Dataset},\n    author    = {Rastogi, Abhinav and Zang, Xiaoxue and Sunkara, Srinivas and Gupta, Raghav and Khaitan, Pranav},\n    booktitle = {Proceedings of the AAAI Conference on Artificial Intelligence},\n    volume    = {34},\n    pages     = {8689--8696},\n    year      = {2020},\n    url       = {https://arxiv.org/abs/1909.05855},\n}\n\n@article{li2023evaluating,\n    title   = {Evaluating {ChatGPT}'s Information Extraction Capabilities: An Assessment of Performance, Explainability, Calibration, and Faithfulness},\n    author  = {Li, Bo and Fang, Gexiang and Yang, Yang and Wang, Quansen and Ye, Wei and Zhao, Wen and Zhang, Shikun},\n    journal = {arXiv preprint arXiv:2304.11633},\n    year    = {2023},\n    url     = {https://arxiv.org/abs/2304.11633},\n}\n\n@inproceedings{lee2022sgd,\n    title     = {{SGD-X}: A Benchmark for Robust Generalization in Schema-Guided Dialogue Systems},\n    author    = {Lee, Harrison and Gupta, Raghav and Rastogi, Abhinav and Cao, Yuan and Zhang, Bin and Wu, Yonghui},\n    booktitle = {Proceedings of the AAAI Conference on Artificial Intelligence},\n    volume    = {36},\n    pages     = {10938--10946},\n    year      = {2022},\n    url       = {https://arxiv.org/abs/2110.06800},\n}\n\n@article{volkanovska2025ner,\n    title   = {A Study of Errors in the Output of Large Language Models for Domain-Specific Few-Shot Named Entity Recognition},\n    author  = {Volkanovska, Elena},\n    journal = {Journal for Language Technology and Computational Linguistics},\n    volume  = {38},\n    number  = {2},\n    pages   = {31--42},\n    year    = {2025},\n    url     = {https://jlcl.org/article/view/281/263},\n}\n\n@article{haystack-to-needle-2025,\n    title   = {From Haystack to Needle: Label Space Reduction for Zero-shot Classification},\n    author  = {Vandemoortele, Nathan and Steenwinckel, Bram and Ongenae, Femke and Van Hoecke, Sofie},\n    journal = {arXiv preprint arXiv:2502.08436},\n    year    = {2025},\n    url     = {https://arxiv.org/abs/2502.08436},\n}\n\n@book{cohen-1988-power,\n    title     = {Statistical Power Analysis for the Behavioral Sciences},\n    author    = {Cohen, Jacob},\n    edition   = {2nd},\n    publisher = {Routledge},\n    year      = {1988},\n    doi       = {10.4324/9780203771587},\n}\n\n@article{lakens-2013-effect-size,\n    title   = {Calculating and Reporting Effect Sizes to Facilitate Cumulative Science: A Practical Primer for t-Tests and {ANOVA}s},\n    author  = {Lakens, Dani{\\\"e}l},\n    journal = {Frontiers in Psychology},\n    volume  = {4},\n    pages   = {863},\n    year    = {2013},\n    doi     = {10.3389/fpsyg.2013.00863},\n}\n\n@inproceedings{deng-2010-imagenet,\n    title     = {What Does Classifying More Than 10,000 Image Categories Tell Us?},\n    author    = {Deng, Jia and Berg, Alexander C. and Li, Kai and Fei-Fei, Li},\n    booktitle = {Proceedings of the 11th European Conference on Computer Vision},\n    pages     = {71--84},\n    year      = {2010},\n    doi       = {10.1007/978-3-642-15555-0\\_6},\n}\n\n@article{rothman-1990,\n    title   = {No Adjustments Are Needed for Multiple Comparisons},\n    author  = {Rothman, Kenneth J.},\n    journal = {Epidemiology},\n    volume  = {1},\n    number  = {1},\n    pages   = {43--46},\n    year    = {1990},\n    doi     = {10.1097/00001648-199001000-00010},\n}\n\n@article{lakens-2017-equivalence,\n    title   = {Equivalence Tests: A Practical Primer for t Tests, Correlations, and Meta-Analyses},\n    author  = {Lakens, Dani{\\\"e}l},\n    journal = {Social Psychological and Personality Science},\n    volume  = {8},\n    number  = {4},\n    pages   = {355--362},\n    year    = {2017},\n    doi     = {10.1177/1948550617697177},\n}\n\n\n@inproceedings{zhou-2025-rethinking,\n    title     = {Rethinking Word Similarity: Semantic Similarity through Classification Confusion},\n    author    = {Zhou, Kaitlyn and Gao, Haishan and Chen, Sarah Li and Edelstein, Dan and Jurafsky, Dan and Shani, Chen},\n    booktitle = {Proceedings of the 2025 Conference of the North American Chapter of the Association for Computational Linguistics},\n    pages     = {5803--5817},\n    year      = {2025},\n    doi       = {10.18653/v1/2025.naacl-long.299},\n}\n\n@inproceedings{guo-2021-label-confusion,\n    title     = {Label Confusion Learning to Enhance Text Classification Models},\n    author    = {Guo, Biyang and Han, Songqiao and Han, Xiao and Huang, Hailiang and Lu, Ting},\n    booktitle = {Proceedings of the AAAI Conference on Artificial Intelligence},\n    volume    = {35},\n    number    = {14},\n    pages     = {12929--12936},\n    year      = {2021},\n    doi       = {10.1609/aaai.v35i14.17529},\n}\n\n@inproceedings{novack-2023-chils,\n    title     = {{CHiLS}: Zero-Shot Image Classification with Hierarchical Label Sets},\n    author    = {Novack, Zachary and McAuley, Julian and Lipton, Zachary Chase and Garg, Saurabh},\n    booktitle = {Proceedings of the 40th International Conference on Machine Learning},\n    series    = {Proceedings of Machine Learning Research},\n    volume    = {202},\n    pages     = {26342--26362},\n    year      = {2023},\n    url       = {https://proceedings.mlr.press/v202/novack23a.html},\n}\n\n@inproceedings{cocchieri-2025-zeroner,\n    title     = {{ZeroNER}: Fueling Zero-Shot Named Entity Recognition via Entity Type Descriptions},\n    author    = {Cocchieri, Alessio and Mart{\\'\\i}nez Galindo, Marcos and Frisoni, Giacomo and Moro, Gianluca and Sartori, Claudio and Tagliavini, Giuseppe},\n    booktitle = {Findings of the Association for Computational Linguistics: ACL 2025},\n    pages     = {15594--15616},\n    year      = {2025},\n    doi       = {10.18653/v1/2025.findings-acl.805},\n}\n\n@article{dlisc-2025,\n    title     = {Effective and Efficient Schema-aware Information Extraction Using On-Device Large Language Models},\n    author    = {Li, Zhuoqun and Wu, Hao and Li, Xinxin and Li, Zhoujun},\n    journal   = {arXiv preprint arXiv:2505.14992},\n    year      = {2025},\n    url       = {https://arxiv.org/abs/2505.14992}\n}\n\n@article{spt-2025,\n    title     = {Schema as Parameterized Tools for Universal Information Extraction},\n    author    = {Liang, Sheng and Zhang, Yongyue and Wu, Yaxiong and Tang, Ruiming and Liu, Yong},\n    journal   = {arXiv preprint arXiv:2506.01276},\n    year      = {2025},\n    url       = {https://arxiv.org/abs/2506.01276}\n}\n\n@inproceedings{card-2020-power,\n    title     = {With Little Power Comes Great Responsibility},\n    author    = {Card, Dallas and Henderson, Peter and Khandelwal, Urvashi and Jia, Robin and Mahowald, Kyle and Jurafsky, Dan},\n    booktitle = {Proceedings of the 2020 Conference on Empirical Methods in Natural Language Processing (EMNLP)},\n    pages     = {9263--9274},\n    year      = {2020},\n    publisher = {Association for Computational Linguistics},\n    url       = {https://aclanthology.org/2020.emnlp-main.745}\n}\n\n@article{gillick-2014-entity-typing,\n    title     = {Context-Dependent Fine-Grained Entity Type Tagging},\n    author    = {Gillick, Daniel and Lazic, Nevena and Ganchev, Kuzman and Kirchner, Jesse and Huynh, David},\n    journal   = {arXiv preprint arXiv:1412.1820},\n    year      = {2014},\n    url       = {https://arxiv.org/abs/1412.1820}\n}\n\n@inproceedings{schall-2025-hidden-cost,\n    title     = {The Hidden Cost of Structure: How Constrained Decoding Affects Language Model Performance},\n    author    = {Schall, Maximilian and de Melo, Gerard},\n    booktitle = {Proceedings of the 15th International Conference on Recent Advances in Natural Language Processing (RANLP)},\n    pages     = {1074--1084},\n    year      = {2025},\n    address   = {Varna, Bulgaria},\n    url       = {https://aclanthology.org/2025.ranlp-1.124}\n}\n\n@article{chen-2026-multi-instance,\n    title     = {Understanding {LLM} Performance Degradation in Multi-Instance Processing: The Roles of Instance Count and Context Length},\n    author    = {Chen, Jingxuan and Pilehvar, Mohammad Taher and Camacho-Collados, Jose},\n    journal   = {arXiv preprint arXiv:2603.22608},\n    year      = {2026},\n    url       = {https://arxiv.org/abs/2603.22608}\n}\n\n@article{wei-2023-chatie,\n    title     = {Zero-Shot Information Extraction via Chatting with {ChatGPT}},\n    author    = {Wei, Xiang and Cui, Xingyu and Cheng, Ning and Wang, Xiaobin and Zhang, Xin and Huang, Shen and Xie, Pengjun and Xu, Jinan and Chen, Yufeng and Zhang, Meishan and Jiang, Yong and Han, Wenjuan},\n    journal   = {arXiv preprint arXiv:2302.10205},\n    year      = {2023},\n    url       = {https://arxiv.org/abs/2302.10205}\n}\n\n",
      "numLines": 659,
      "startLine": 1,
      "totalLines": 659
    }
  },
  "sourceToolAssistantUUID": "6c3727a5-ed97-4544-b562-0b8bf577919c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_reviewer_2_302b64f9",
  "sessionId": "0ff1fe81-4731-4c76-91b4-02652701ddff",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Tool call

_source line 34 · 2026-05-19T04:30:55.237Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_015uS6NLQLfYjNkEAdzuR7Dh`</summary>

```json
{
  "query": "ACL ARR 2026 reviewer guidelines review form criteria dimensions"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c2b0c6d6-16c0-43cd-9c9c-4e2909cdc098",
  "isSidechain": false,
  "requestId": "req_011CbBJL3Mfp6QVPxgqBTm4o",
  "type": "assistant",
  "uuid": "54a3e20d-b3e6-4b2b-a772-e4205b085463",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_reviewer_2_302b64f9",
  "sessionId": "0ff1fe81-4731-4c76-91b4-02652701ddff",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PMdzHtBXazYPW4S8Z616zu",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2278,
      "cache_read_input_tokens": 28070,
      "output_tokens": 849,
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
          "output_tokens": 849,
          "cache_read_input_tokens": 28070,
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

_source line 35_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[Round 1 审稿请求]: ## Round 1 审稿任务 — Reviewer 2（新颖性 + Related Work 完整性 + 写作质量 + 格式合规）  ### Venue 信息 - **目标会议**: EMNLP 2026（通过 ARR May 2026 cycle 提交） - **截止日期**: 2026-05-25 - **页数限制**: Long paper, 正文 ≤ 8…",
  "leafUuid": "54a3e20d-b3e6-4b2b-a772-e4205b085463",
  "sessionId": "0ff1fe81-4731-4c76-91b4-02652701ddff"
}
```

---


### Runtime record

_source line 36_

```json
{
  "type": "ai-title",
  "aiTitle": "Review Round 1 schema-dag-extraction paper for EMNLP 2026",
  "sessionId": "0ff1fe81-4731-4c76-91b4-02652701ddff"
}
```

---


### Tool result

_source line 37 · 2026-05-19T04:31:02.118Z_

<details><summary>↩ Tool result · `toolu_015uS6NLQLfYjNkEAdzuR7Dh`</summary>

```text
Web search results for query: "ACL ARR 2026 reviewer guidelines review form criteria dimensions"

Links: [{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"https://aclrollingreview.org/"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"}]

I found information about ACL ARR 2026 reviewer guidelines and the review form. Here's what I found:

## Review Form Criteria

For Main versus Findings papers, the main criteria for Findings are soundness and reproducibility, while conference recommendations may also consider novelty, impact and other factors.

## Review Recommendation Scores

The review form uses a scale where 5 = Consider for Award (outstanding paper), 2 = Resubmit next cycle (substantial revisions needed by next cycle), 1.5 = Resubmit after next cycle (substantial revisions that cannot be completed by next cycle), and 1 = Do not resubmit (paper needs full redo or is not relevant to the *ACL community).

## General Reviewer Guidelines

Reviewers are asked to follow a workflow: (1) read the paper and get a first impression, (2) search for related work, not deliberately trying to find that particular submission.

## 2026 Specific Requirements

Papers whose authors have not registered as reviewers or ACs or have not completed their checklists as Reviewers or ACs by the designated deadline will be automatically desk-rejected.

For more detailed information, you can visit the official ARR Reviewer Guidelines at aclrollingreview.org/reviewerguidelines or the Review Form page at aclrollingreview.org/reviewform.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "54a3e20d-b3e6-4b2b-a772-e4205b085463",
  "isSidechain": false,
  "promptId": "8257bd0e-08b4-4530-aa87-1e185ea40a51",
  "type": "user",
  "uuid": "4450d882-54c3-4fb8-9e09-eebe92f078bf",
  "toolUseResult": {
    "query": "ACL ARR 2026 reviewer guidelines review form criteria dimensions",
    "results": [
      {
        "tool_use_id": "srvtoolu_01SDDGG9EA8ZHQ7PQxd7y8qa",
        "content": [
          {
            "title": "ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics",
            "url": "http://aclrollingreview.org/reviewerguidelines"
          },
          {
            "title": "aclrollingreview/cfp.md at main · acl-org/aclrollingreview",
            "url": "https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"
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
            "title": "CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics",
            "url": "http://aclrollingreview.org/cfp"
          },
          {
            "title": "ACL Rolling Review – A peer review platform for the Association for Computational Linguistics",
            "url": "https://aclrollingreview.org/"
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
            "title": "How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics",
            "url": "http://aclrollingreview.org/reviewing"
          }
        ]
      },
      "I found information about ACL ARR 2026 reviewer guidelines and the review form. Here's what I found:\n\n## Review Form Criteria\n\nFor Main versus Findings papers, the main criteria for Findings are soundness and reproducibility, while conference recommendations may also consider novelty, impact and other factors.\n\n## Review Recommendation Scores\n\nThe review form uses a scale where 5 = Consider for Award (outstanding paper), 2 = Resubmit next cycle (substantial revisions needed by next cycle), 1.5 = Resubmit after next cycle (substantial revisions that cannot be completed by next cycle), and 1 = Do not resubmit (paper needs full redo or is not relevant to the *ACL community).\n\n## General Reviewer Guidelines\n\nReviewers are asked to follow a workflow: (1) read the paper and get a first impression, (2) search for related work, not deliberately trying to find that particular submission.\n\n## 2026 Specific Requirements\n\nPapers whose authors have not registered as reviewers or ACs or have not completed their checklists as Reviewers or ACs by the designated deadline will be automatically desk-rejected.\n\nFor more detailed information, you can visit the official ARR Reviewer Guidelines at aclrollingreview.org/reviewerguidelines or the Review Form page at aclrollingreview.org/reviewform."
    ],
    "durationSeconds": 6.875190629
  },
  "sourceToolAssistantUUID": "54a3e20d-b3e6-4b2b-a772-e4205b085463",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_reviewer_2_302b64f9",
  "sessionId": "0ff1fe81-4731-4c76-91b4-02652701ddff",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Runtime record

_source line 38 · 2026-05-19T04:31:02.123Z_

```json
{
  "parentUuid": "4450d882-54c3-4fb8-9e09-eebe92f078bf",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "f43472de-504c-4ad3-83ef-3482bc65f2c3",
  "timestamp": "2026-05-19T04:31:02.123Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_reviewer_2_302b64f9",
  "sessionId": "0ff1fe81-4731-4c76-91b4-02652701ddff",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---


### Assistant

_source line 39 · 2026-05-19T04:31:05.559Z_

<details><summary>Logged reasoning block</summary>

```text
Now let me fetch the official ARR review form to get the exact scoring dimensions.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f43472de-504c-4ad3-83ef-3482bc65f2c3",
  "isSidechain": false,
  "requestId": "req_011CbBJMGVyQjAf5MHwggvdY",
  "type": "assistant",
  "uuid": "08985a8f-e97b-4078-a32f-b9d4b2bfb7f8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_reviewer_2_302b64f9",
  "sessionId": "0ff1fe81-4731-4c76-91b4-02652701ddff",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MFC6tvVKBWYLB6N1kfcwqS",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 70539,
      "cache_read_input_tokens": 11841,
      "output_tokens": 290,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 70539,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 290,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 70539,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 70539
          },
          "type": "message"
        }
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

_source line 40 · 2026-05-19T04:31:06.055Z_

获取 ARR 官方 review form 的具体评分维度。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "08985a8f-e97b-4078-a32f-b9d4b2bfb7f8",
  "isSidechain": false,
  "requestId": "req_011CbBJMGVyQjAf5MHwggvdY",
  "type": "assistant",
  "uuid": "0d7feef0-5d7f-4da5-9a12-6256ec88fce1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_reviewer_2_302b64f9",
  "sessionId": "0ff1fe81-4731-4c76-91b4-02652701ddff",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MFC6tvVKBWYLB6N1kfcwqS",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 70539,
      "cache_read_input_tokens": 11841,
      "output_tokens": 290,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 70539,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 290,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 70539,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 70539
          },
          "type": "message"
        }
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

_source line 41 · 2026-05-19T04:31:07.933Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_018zsWAD1qTbYoGWQSRf9xyK`</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract the complete review form with all scoring dimensions, their scales, and descriptions. I need every criterion that reviewers must score (e.g., soundness, excitement/novelty, overall assessment, confidence, etc.) with their exact scale descriptions."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0d7feef0-5d7f-4da5-9a12-6256ec88fce1",
  "isSidechain": false,
  "requestId": "req_011CbBJMGVyQjAf5MHwggvdY",
  "type": "assistant",
  "uuid": "f477b4a9-8f5e-4bdf-922b-86655db11a53",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_reviewer_2_302b64f9",
  "sessionId": "0ff1fe81-4731-4c76-91b4-02652701ddff",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MFC6tvVKBWYLB6N1kfcwqS",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 70539,
      "cache_read_input_tokens": 11841,
      "output_tokens": 290,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 70539,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 290,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 70539,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 70539
          },
          "type": "message"
        }
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

_source line 42 · 2026-05-19T04:31:09.037Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01V1BEJDtjYg2tBdYv1SDBsA`</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewerguidelines",
  "prompt": "Extract the complete reviewer guidelines including what reviewers should evaluate, scoring criteria, what constitutes a good review, and any specific instructions about how to assess novelty, soundness, reproducibility, etc."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f477b4a9-8f5e-4bdf-922b-86655db11a53",
  "isSidechain": false,
  "requestId": "req_011CbBJMGVyQjAf5MHwggvdY",
  "type": "assistant",
  "uuid": "25ffd187-ece9-4b08-a41d-d0a95b774b8d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_reviewer_2_302b64f9",
  "sessionId": "0ff1fe81-4731-4c76-91b4-02652701ddff",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MFC6tvVKBWYLB6N1kfcwqS",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 70539,
      "cache_read_input_tokens": 11841,
      "output_tokens": 290,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 70539,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 290,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 70539,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 70539
          },
          "type": "message"
        }
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

_source line 43 · 2026-05-19T04:31:17.136Z_

<details><summary>↩ Tool result · `toolu_01V1BEJDtjYg2tBdYv1SDBsA`</summary>

```text
# ARR Reviewer Guidelines Summary

## Core Evaluation Framework

Reviewers assess papers using three primary scores:

1. **Soundness**: Technical validity and methodological rigor
2. **Excitement**: Personal interest and subjective appeal
3. **Overall Recommendation**: Composite judgment for venue acceptance

## Key Reviewer Responsibilities

### Assignment Verification
Reviewers must confirm they possess adequate expertise and have no conflicts of interest. The guidelines note that "assignments are made based on a semi-automatic process" and imperfect matches occur, particularly for novel or interdisciplinary work.

### Initial Assessment (Task 2)
Complete a desk-rejection checklist evaluating:
- Appropriateness for ARR scope
- Hallucinated or false citations
- Anonymity violations
- Format/length compliance
- Missing limitations sections
- Ethics concerns

### Writing Strong Reviews (Task 3)

**Reading Strategy**: Review papers twice—first skimming to establish context, then in-depth analysis. The guidelines emphasize: "adjust your expectations I6 I7" by understanding the research question before examining results.

**Specificity Requirements**: Avoid vague criticism. Instead of stating "missing relevant references," identify specific papers like "papers X, Y, Z should be cited."

### Bias Awareness

The guidelines identify 17 common problematic review heuristics (H1-H17), including:
- Dismissing non-obvious findings as unsurprising
- Penalizing negative results
- Overvaluing state-of-the-art achievement
- Requiring unnecessary additional experiments

## NLP-Specific Issues

Reviewers should flag common problems across five categories:
- **Methodology** (M1-M5): LLM evaluation validation, reproducibility details
- **Artifact Terms** (T1-T2): Data ethics and license clarity
- **Results** (R1-R5): Statistical rigor and appropriate claim scope
- **General** (G1-G5): Research clarity and citation accuracy

## Engagement Requirements

Reviewers must "at least acknowledge the authors' response" during discussion periods and update assessments based on clarifications provided.

## Restrictions on AI Use

The guidelines prohibit uploading papers or reviews to non-privacy-preserving generative AI tools, explicitly stating this violates "authors' confidentiality and intellectual property rights."
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "25ffd187-ece9-4b08-a41d-d0a95b774b8d",
  "isSidechain": false,
  "promptId": "8257bd0e-08b4-4530-aa87-1e185ea40a51",
  "type": "user",
  "uuid": "602e5f0f-98bc-49d2-8c50-e08ffc1d433c",
  "toolUseResult": {
    "bytes": 100603,
    "code": 200,
    "codeText": "OK",
    "result": "# ARR Reviewer Guidelines Summary\n\n## Core Evaluation Framework\n\nReviewers assess papers using three primary scores:\n\n1. **Soundness**: Technical validity and methodological rigor\n2. **Excitement**: Personal interest and subjective appeal\n3. **Overall Recommendation**: Composite judgment for venue acceptance\n\n## Key Reviewer Responsibilities\n\n### Assignment Verification\nReviewers must confirm they possess adequate expertise and have no conflicts of interest. The guidelines note that \"assignments are made based on a semi-automatic process\" and imperfect matches occur, particularly for novel or interdisciplinary work.\n\n### Initial Assessment (Task 2)\nComplete a desk-rejection checklist evaluating:\n- Appropriateness for ARR scope\n- Hallucinated or false citations\n- Anonymity violations\n- Format/length compliance\n- Missing limitations sections\n- Ethics concerns\n\n### Writing Strong Reviews (Task 3)\n\n**Reading Strategy**: Review papers twice—first skimming to establish context, then in-depth analysis. The guidelines emphasize: \"adjust your expectations I6 I7\" by understanding the research question before examining results.\n\n**Specificity Requirements**: Avoid vague criticism. Instead of stating \"missing relevant references,\" identify specific papers like \"papers X, Y, Z should be cited.\"\n\n### Bias Awareness\n\nThe guidelines identify 17 common problematic review heuristics (H1-H17), including:\n- Dismissing non-obvious findings as unsurprising\n- Penalizing negative results\n- Overvaluing state-of-the-art achievement\n- Requiring unnecessary additional experiments\n\n## NLP-Specific Issues\n\nReviewers should flag common problems across five categories:\n- **Methodology** (M1-M5): LLM evaluation validation, reproducibility details\n- **Artifact Terms** (T1-T2): Data ethics and license clarity\n- **Results** (R1-R5): Statistical rigor and appropriate claim scope\n- **General** (G1-G5): Research clarity and citation accuracy\n\n## Engagement Requirements\n\nReviewers must \"at least acknowledge the authors' response\" during discussion periods and update assessments based on clarifications provided.\n\n## Restrictions on AI Use\n\nThe guidelines prohibit uploading papers or reviews to non-privacy-preserving generative AI tools, explicitly stating this violates \"authors' confidentiality and intellectual property rights.\"",
    "durationMs": 8095,
    "url": "https://aclrollingreview.org/reviewerguidelines"
  },
  "sourceToolAssistantUUID": "25ffd187-ece9-4b08-a41d-d0a95b774b8d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_reviewer_2_302b64f9",
  "sessionId": "0ff1fe81-4731-4c76-91b4-02652701ddff",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Tool result

_source line 44 · 2026-05-19T04:31:23.514Z_

<details><summary>↩ Tool result · `toolu_018zsWAD1qTbYoGWQSRf9xyK`</summary>

```text
# ACL Rolling Review Form - Scoring Dimensions

## 1. **Reviewer Confidence**
Scale: 1-5
- **5**: "Positive that my evaluation is correct. I read the paper very carefully and am familiar with related work."
- **4**: "Quite sure. I tried to check the important points carefully."
- **3**: "Pretty sure, but there's a chance I missed something."
- **2**: "Willing to defend my evaluation, but it is fairly likely that I missed some details."
- **1**: "Not my area, or paper is very hard to understand."

## 2. **Soundness**
Scale: 1-5 (with .5 increments)
- **5**: "Excellent: This study is one of the most thorough I have seen, given its type."
- **4**: "Strong: This study provides sufficient support for all of its claims."
- **3**: "Acceptable: This study provides sufficient support for its main claims."
- **2**: "Poor: Some of the main claims are not sufficiently supported."
- **1**: "Major Issues: This study is not yet sufficiently thorough to warrant publication."

## 3. **Excitement**
Scale: 1-5 (with .5 increments)
- **5**: "Highly Exciting: I would recommend this paper to others and/or attend its presentation."
- **4**: "Exciting: I would mention this paper to others and/or make an effort to attend."
- **3**: "Interesting: I might mention some points of this paper to others."
- **2**: "Potentially Interesting: this paper does not resonate with me."
- **1**: "Not Exciting: this paper does not resonate with me."

## 4. **Overall Assessment**
Scale: 1-5 (with .5 increments)
- **5**: "Consider for Award: Could be considered for an outstanding paper award."
- **4**: "Conference: Could be accepted to an *ACL conference."
- **3**: "Findings: Could be accepted to the Findings of the ACL."
- **2**: "Resubmit next cycle: Needs substantial revisions."
- **1**: "Do not resubmit: Fully redone or not relevant."

## 5. **Reproducibility**
Scale: 1-5
- **5**: "They could easily reproduce the results."
- **4**: "They could mostly reproduce the results."
- **3**: "They could reproduce the results with some difficulty."
- **2**: "They would be hard pressed to reproduce the results."
- **1**: "They would not be able to reproduce the results."

## 6. **Datasets** (if applicable)
Scale: 1-5
- **5**: "Enabling: Should affect research project choices."
- **4**: "Useful: Would recommend to other researchers."
- **3**: "Potentially useful: Someone might find useful."
- **2**: "Documentary: Useful for replication primarily."
- **1**: "No usable datasets submitted."

## 7. **Software** (if applicable)
Scale: 1-5
- **5**: "Enabling: Should affect research project choices."
- **4**: "Useful: Would recommend to other researchers."
- **3**: "Potentially useful: Someone might find useful."
- **2**: "Documentary: Useful for replication primarily."
- **1**: "No usable software released."

## 8. **Author Identity Knowledge**
Scale: 1-5
- **5-1**: Ranging from knowing author identity to having no educated guess.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f477b4a9-8f5e-4bdf-922b-86655db11a53",
  "isSidechain": false,
  "promptId": "8257bd0e-08b4-4530-aa87-1e185ea40a51",
  "type": "user",
  "uuid": "d3327223-7a8a-4381-9866-2c44c3a1ebb6",
  "toolUseResult": {
    "bytes": 25365,
    "code": 200,
    "codeText": "OK",
    "result": "# ACL Rolling Review Form - Scoring Dimensions\n\n## 1. **Reviewer Confidence**\nScale: 1-5\n- **5**: \"Positive that my evaluation is correct. I read the paper very carefully and am familiar with related work.\"\n- **4**: \"Quite sure. I tried to check the important points carefully.\"\n- **3**: \"Pretty sure, but there's a chance I missed something.\"\n- **2**: \"Willing to defend my evaluation, but it is fairly likely that I missed some details.\"\n- **1**: \"Not my area, or paper is very hard to understand.\"\n\n## 2. **Soundness**\nScale: 1-5 (with .5 increments)\n- **5**: \"Excellent: This study is one of the most thorough I have seen, given its type.\"\n- **4**: \"Strong: This study provides sufficient support for all of its claims.\"\n- **3**: \"Acceptable: This study provides sufficient support for its main claims.\"\n- **2**: \"Poor: Some of the main claims are not sufficiently supported.\"\n- **1**: \"Major Issues: This study is not yet sufficiently thorough to warrant publication.\"\n\n## 3. **Excitement**\nScale: 1-5 (with .5 increments)\n- **5**: \"Highly Exciting: I would recommend this paper to others and/or attend its presentation.\"\n- **4**: \"Exciting: I would mention this paper to others and/or make an effort to attend.\"\n- **3**: \"Interesting: I might mention some points of this paper to others.\"\n- **2**: \"Potentially Interesting: this paper does not resonate with me.\"\n- **1**: \"Not Exciting: this paper does not resonate with me.\"\n\n## 4. **Overall Assessment**\nScale: 1-5 (with .5 increments)\n- **5**: \"Consider for Award: Could be considered for an outstanding paper award.\"\n- **4**: \"Conference: Could be accepted to an *ACL conference.\"\n- **3**: \"Findings: Could be accepted to the Findings of the ACL.\"\n- **2**: \"Resubmit next cycle: Needs substantial revisions.\"\n- **1**: \"Do not resubmit: Fully redone or not relevant.\"\n\n## 5. **Reproducibility**\nScale: 1-5\n- **5**: \"They could easily reproduce the results.\"\n- **4**: \"They could mostly reproduce the results.\"\n- **3**: \"They could reproduce the results with some difficulty.\"\n- **2**: \"They would be hard pressed to reproduce the results.\"\n- **1**: \"They would not be able to reproduce the results.\"\n\n## 6. **Datasets** (if applicable)\nScale: 1-5\n- **5**: \"Enabling: Should affect research project choices.\"\n- **4**: \"Useful: Would recommend to other researchers.\"\n- **3**: \"Potentially useful: Someone might find useful.\"\n- **2**: \"Documentary: Useful for replication primarily.\"\n- **1**: \"No usable datasets submitted.\"\n\n## 7. **Software** (if applicable)\nScale: 1-5\n- **5**: \"Enabling: Should affect research project choices.\"\n- **4**: \"Useful: Would recommend to other researchers.\"\n- **3**: \"Potentially useful: Someone might find useful.\"\n- **2**: \"Documentary: Useful for replication primarily.\"\n- **1**: \"No usable software released.\"\n\n## 8. **Author Identity Knowledge**\nScale: 1-5\n- **5-1**: Ranging from knowing author identity to having no educated guess.",
    "durationMs": 15576,
    "url": "https://aclrollingreview.org/reviewform"
  },
  "sourceToolAssistantUUID": "f477b4a9-8f5e-4bdf-922b-86655db11a53",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_reviewer_2_302b64f9",
  "sessionId": "0ff1fe81-4731-4c76-91b4-02652701ddff",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Assistant

_source line 45 · 2026-05-19T04:31:28.140Z_

<details><summary>Logged reasoning block</summary>

```text
Good, now I have the complete ARR review form and guidelines. Let me also run the reference verification tool and check the paper format more carefully. Let me now compile my review.

Let me also check for AI writing style issues (em-dashes, -ing phrases, etc.) and format compliance (page count, anonymization, etc.).

Let me search for any missing references that might be important.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d3327223-7a8a-4381-9866-2c44c3a1ebb6",
  "isSidechain": false,
  "requestId": "req_011CbBJNr2co9XCBngt1vg1Z",
  "type": "assistant",
  "uuid": "5656f380-352f-4aec-b4bb-f8eba260d941",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_reviewer_2_302b64f9",
  "sessionId": "0ff1fe81-4731-4c76-91b4-02652701ddff",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01T9tSbFKj6b8dDG8E2qpq78",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 557,
      "cache_creation_input_tokens": 1153,
      "cache_read_input_tokens": 82380,
      "output_tokens": 464,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1153,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 557,
          "output_tokens": 464,
          "cache_read_input_tokens": 82380,
          "cache_creation_input_tokens": 1153,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1153
          },
          "type": "message"
        }
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

_source line 46 · 2026-05-19T04:31:29.108Z_

运行引用验证，同时搜索可能遗漏的相关工作。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5656f380-352f-4aec-b4bb-f8eba260d941",
  "isSidechain": false,
  "requestId": "req_011CbBJNr2co9XCBngt1vg1Z",
  "type": "assistant",
  "uuid": "c9b28cc8-e089-4daa-872d-716e00780f75",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_reviewer_2_302b64f9",
  "sessionId": "0ff1fe81-4731-4c76-91b4-02652701ddff",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01T9tSbFKj6b8dDG8E2qpq78",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 557,
      "cache_creation_input_tokens": 1153,
      "cache_read_input_tokens": 82380,
      "output_tokens": 464,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1153,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 557,
          "output_tokens": 464,
          "cache_read_input_tokens": 82380,
          "cache_creation_input_tokens": 1153,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1153
          },
          "type": "message"
        }
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

_source line 47 · 2026-05-19T04:31:31.057Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__verify_references · `toolu_01VZo7LNTXDQqfP3yD4gMWxh`</summary>

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
  "parentUuid": "c9b28cc8-e089-4daa-872d-716e00780f75",
  "isSidechain": false,
  "requestId": "req_011CbBJNr2co9XCBngt1vg1Z",
  "type": "assistant",
  "uuid": "629febd3-b175-4d17-952f-757e06a0b404",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_reviewer_2_302b64f9",
  "sessionId": "0ff1fe81-4731-4c76-91b4-02652701ddff",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01T9tSbFKj6b8dDG8E2qpq78",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 557,
      "cache_creation_input_tokens": 1153,
      "cache_read_input_tokens": 82380,
      "output_tokens": 464,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1153,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 557,
          "output_tokens": 464,
          "cache_read_input_tokens": 82380,
          "cache_creation_input_tokens": 1153,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1153
          },
          "type": "message"
        }
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

_source line 48 · 2026-05-19T04:31:32.005Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_016WZuYKC7wJdPfvXA7vG3L7`</summary>

```json
{
  "query": "schema decomposition LLM information extraction type confusability label similarity 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "629febd3-b175-4d17-952f-757e06a0b404",
  "isSidechain": false,
  "requestId": "req_011CbBJNr2co9XCBngt1vg1Z",
  "type": "assistant",
  "uuid": "ee15444a-0a62-4d21-9a44-4278fccccf36",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_reviewer_2_302b64f9",
  "sessionId": "0ff1fe81-4731-4c76-91b4-02652701ddff",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01T9tSbFKj6b8dDG8E2qpq78",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 557,
      "cache_creation_input_tokens": 1153,
      "cache_read_input_tokens": 82380,
      "output_tokens": 464,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1153,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 557,
          "output_tokens": 464,
          "cache_read_input_tokens": 82380,
          "cache_creation_input_tokens": 1153,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1153
          },
          "type": "message"
        }
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

_source line 49 · 2026-05-19T04:31:32.485Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Rn8d4rMm1mCyWCL4McmFF9`</summary>

```json
{
  "query": "inter-class similarity confusion classification NLP label space 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ee15444a-0a62-4d21-9a44-4278fccccf36",
  "isSidechain": false,
  "requestId": "req_011CbBJNr2co9XCBngt1vg1Z",
  "type": "assistant",
  "uuid": "14ada13f-70ad-4b0a-8c6d-a0d23b8e6b4c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_reviewer_2_302b64f9",
  "sessionId": "0ff1fe81-4731-4c76-91b4-02652701ddff",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01T9tSbFKj6b8dDG8E2qpq78",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 557,
      "cache_creation_input_tokens": 1153,
      "cache_read_input_tokens": 82380,
      "output_tokens": 464,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1153,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 557,
          "output_tokens": 464,
          "cache_read_input_tokens": 82380,
          "cache_creation_input_tokens": 1153,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1153
          },
          "type": "message"
        }
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

_source line 50 · 2026-05-19T04:31:33.480Z_

<details open><summary>🔧 Tool call — Grep · `toolu_0137e4upPGPNVD2zX5Ja9z4Z`</summary>

```json
{
  "pattern": "—|–",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper",
  "output_mode": "content",
  "glob": "*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "14ada13f-70ad-4b0a-8c6d-a0d23b8e6b4c",
  "isSidechain": false,
  "requestId": "req_011CbBJNr2co9XCBngt1vg1Z",
  "type": "assistant",
  "uuid": "9789ba4b-2879-443b-a258-c873bd1b9ee4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_reviewer_2_302b64f9",
  "sessionId": "0ff1fe81-4731-4c76-91b4-02652701ddff",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01T9tSbFKj6b8dDG8E2qpq78",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 557,
      "cache_creation_input_tokens": 1153,
      "cache_read_input_tokens": 82380,
      "output_tokens": 464,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1153,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 557,
          "output_tokens": 464,
          "cache_read_input_tokens": 82380,
          "cache_creation_input_tokens": 1153,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1153
          },
          "type": "message"
        }
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
  "lastPrompt": "[Round 1 审稿请求]: ## Round 1 审稿任务 — Reviewer 2（新颖性 + Related Work 完整性 + 写作质量 + 格式合规）  ### Venue 信息 - **目标会议**: EMNLP 2026（通过 ARR May 2026 cycle 提交） - **截止日期**: 2026-05-25 - **页数限制**: Long paper, 正文 ≤ 8…",
  "leafUuid": "9789ba4b-2879-443b-a258-c873bd1b9ee4",
  "sessionId": "0ff1fe81-4731-4c76-91b4-02652701ddff"
}
```

---


### Runtime record

_source line 52_

```json
{
  "type": "ai-title",
  "aiTitle": "Review Round 1 schema-dag-extraction paper for EMNLP 2026",
  "sessionId": "0ff1fe81-4731-4c76-91b4-02652701ddff"
}
```

---


### Tool result

_source line 53 · 2026-05-19T04:32:25.428Z_

<details><summary>↩ Tool result · `toolu_01VZo7LNTXDQqfP3yD4gMWxh`</summary>

```text
&lt;persisted-output>
Output too large (57.1KB). Full output saved to: /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-18-projects-schema-dag-extraction--claude-sessions-review-reviewer-2-302b64f9/0ff1fe81-4731-4c76-91b4-02652701ddff/tool-results/toolu_01VZo7LNTXDQqfP3yD4gMWxh.txt

Preview (first 2KB):
{"result":"{\"success\": true, \"data\": {\"summary\": {\"total_bib_entries\": 70, \"total_citations\": 96, \"unique_cited_keys\": 69, \"orphan_bib\": 1, \"missing_bib\": 0, \"duplicate_keys\": 0, \"online_verified\": 55, \"online_not_found\": 4, \"online_mismatch\": 11}, \"cross_check\": {\"orphan_bib\": [\"jagannatha2020calibrating\"], \"missing_bib\": [], \"orphan_count\": 1, \"missing_count\": 0}, \"bib_entries\": [{\"key\": \"tam-2024-let-me-speak\", \"type\": \"inproceedings\", \"title\": \"Let Me Speak Freely? A Study on the Impact of Format Restrictions on Performance of Large Language Models\", \"authors\": \"Tam, Zhi Rui and Wu, Cheng-Kuang and Tsai, Yi-Lin and Lin, Chieh-Yen and Lee, Hu...\", \"year\": \"2024\", \"venue\": \"Proceedings of the 2024 Conference on Empirical Methods in Natural Language Proc...\"}, {\"key\": \"yin-2019-zero-shot-bench\", \"type\": \"inproceedings\", \"title\": \"Benchmarking Zero-shot Text Classification: Datasets, Evaluation and Entailment Approach\", \"authors\": \"Yin, Wenpeng and Hay, Jamaal and Roth, Dan\", \"year\": \"2019\", \"venue\": \"Proceedings of the 2019 Conference on Empirical Methods in Natural Language Proc...\"}, {\"key\": \"schuirmann-1987-tost\", \"type\": \"article\", \"title\": \"A Comparison of the Two One-Sided Tests Procedure and the Power Approach for Assessing the Equivalence of Average Bioava...\", \"authors\": \"Schuirmann, Donald J.\", \"year\": \"1987\", \"venue\": \"Journal of Pharmacokinetics and Biopharmaceutics\"}, {\"key\": \"gemini-2025\", \"type\": \"article\", \"title\": \"Gemini 2.5: Pushing the Frontier with Advanced Reasoning, Multimodality, and Long Context\", \"authors\": \"Comanici, Gheorghe and others\", \"year\": \"2025\", \"venue\": \"arXiv preprint arXiv:2507.06261\"}, {\"key\": \"snell2017prototypical\", \"type\": \"inproceedings\", \"title\": \"Prototypical Networks for Few-shot Learning\", \"authors\": \"Snell, Jake and Swersky, Kevin and Zemel, Richard\", \"year\": \"2017\"
...
&lt;/persisted-output>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "629febd3-b175-4d17-952f-757e06a0b404",
  "isSidechain": false,
  "promptId": "8257bd0e-08b4-4530-aa87-1e185ea40a51",
  "type": "user",
  "uuid": "a8032b5d-0361-4f60-acf5-3c36d2b4fbb7",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"summary\\\": {\\\"total_bib_entries\\\": 70, \\\"total_citations\\\": 96, \\\"unique_cited_keys\\\": 69, \\\"orphan_bib\\\": 1, \\\"missing_bib\\\": 0, \\\"duplicate_keys\\\": 0, \\\"online_verified\\\": 55, \\\"online_not_found\\\": 4, \\\"online_mismatch\\\": 11}, \\\"cross_check\\\": {\\\"orphan_bib\\\": [\\\"jagannatha2020calibrating\\\"], \\\"missing_bib\\\": [], \\\"orphan_count\\\": 1, \\\"missing_count\\\": 0}, \\\"bib_entries\\\": [{\\\"key\\\": \\\"tam-2024-let-me-speak\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Let Me Speak Freely? A Study on the Impact of Format Restrictions on Performance of Large Language Models\\\", \\\"authors\\\": \\\"Tam, Zhi Rui and Wu, Cheng-Kuang and Tsai, Yi-Lin and Lin, Chieh-Yen and Lee, Hu...\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"Proceedings of the 2024 Conference on Empirical Methods in Natural Language Proc...\\\"}, {\\\"key\\\": \\\"yin-2019-zero-shot-bench\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Benchmarking Zero-shot Text Classification: Datasets, Evaluation and Entailment Approach\\\", \\\"authors\\\": \\\"Yin, Wenpeng and Hay, Jamaal and Roth, Dan\\\", \\\"year\\\": \\\"2019\\\", \\\"venue\\\": \\\"Proceedings of the 2019 Conference on Empirical Methods in Natural Language Proc...\\\"}, {\\\"key\\\": \\\"schuirmann-1987-tost\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"A Comparison of the Two One-Sided Tests Procedure and the Power Approach for Assessing the Equivalence of Average Bioava...\\\", \\\"authors\\\": \\\"Schuirmann, Donald J.\\\", \\\"year\\\": \\\"1987\\\", \\\"venue\\\": \\\"Journal of Pharmacokinetics and Biopharmaceutics\\\"}, {\\\"key\\\": \\\"gemini-2025\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Gemini 2.5: Pushing the Frontier with Advanced Reasoning, Multimodality, and Long Context\\\", \\\"authors\\\": \\\"Comanici, Gheorghe and others\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"arXiv preprint arXiv:2507.06261\\\"}, {\\\"key\\\": \\\"snell2017prototypical\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Prototypical Networks for Few-shot Learning\\\", \\\"authors\\\": \\\"Snell, Jake and Swersky, Kevin and Zemel, Richard\\\", \\\"year\\\": \\\"2017\\\", \\\"venue\\\": \\\"Advances in Neural Information Processing Systems\\\"}, {\\\"key\\\": \\\"muller2019when\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"When Does Label Smoothing Help?\\\", \\\"authors\\\": \\\"M\\\\\\\\\\\\\\\"uller, Rafael and Kornblith, Simon and Hinton, Geoffrey E.\\\", \\\"year\\\": \\\"2019\\\", \\\"venue\\\": \\\"Advances in Neural Information Processing Systems\\\"}, {\\\"key\\\": \\\"peterson2019human\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Human Uncertainty Makes Classification More Robust\\\", \\\"authors\\\": \\\"Peterson, Joshua C. and Battleday, Ruairidh M. and Griffiths, Thomas L. and Russ...\\\", \\\"year\\\": \\\"2019\\\", \\\"venue\\\": \\\"Proceedings of the IEEE/CVF International Conference on Computer Vision\\\"}, {\\\"key\\\": \\\"jagannatha2020calibrating\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Calibrating Structured Output Predictors for Natural Language Processing\\\", \\\"authors\\\": \\\"Jagannatha, Abhyuday and Yu, Hong\\\", \\\"year\\\": \\\"2020\\\", \\\"venue\\\": \\\"Proceedings of the 58th Annual Meeting of the Association for Computational Ling...\\\"}, {\\\"key\\\": \\\"willard2023efficient\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Efficient Guided Generation for Large Language Models\\\", \\\"authors\\\": \\\"Willard, Brandon T. and Louf, R\\\\\\\\'emi\\\", \\\"year\\\": \\\"2023\\\", \\\"venue\\\": \\\"arXiv preprint arXiv:2307.09702\\\"}, {\\\"key\\\": \\\"lu2022fantastically\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Fantastically Ordered Prompts and Where to Find Them: Overcoming Few-Shot Prompt Order Sensitivity\\\", \\\"authors\\\": \\\"Lu, Yao and Bartolo, Max and Moore, Alastair and Riedel, Sebastian and Stenetorp...\\\", \\\"year\\\": \\\"2022\\\", \\\"venue\\\": \\\"Proceedings of the 60th Annual Meeting of the Association for Computational Ling...\\\"}, {\\\"key\\\": \\\"yang2025beyond\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Beyond Boundaries: Learning a Universal Entity Taxonomy across Datasets and Languages for Open Named Entity Recognition\\\", \\\"authors\\\": \\\"Yang, Yuming and Zhao, Wantong and Huang, Caishuang and Ye, Junjie and Wang, Xia...\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"Proceedings of the 31st International Conference on Computational Linguistics\\\"}, {\\\"key\\\": \\\"llm-pee-2025\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Towards Event Extraction with Massive Types: LLM-based Collaborative Annotation and Partitioning Extraction\\\", \\\"authors\\\": \\\"Liu, Wenxuan and Li, Zixuan and Bai, Long and Zuo, Yuxin and Xu, Daozhu and Jin,...\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"Proceedings of the 2025 Conference on Empirical Methods in Natural Language Proc...\\\"}, {\\\"key\\\": \\\"parse-2025\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"PARSE: LLM Driven Schema Optimization for Reliable Entity Extraction\\\", \\\"authors\\\": \\\"Shrimal, Anubhav and Jain, Aryan and Chowdhury, Soumyajit and Yenigalla, Promod\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"Proceedings of the 2025 Conference on Empirical Methods in Natural Language Proc...\\\"}, {\\\"key\\\": \\\"dee-2024\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Decompose, Enrich, and Extract! Schema-aware Event Extraction using LLMs\\\", \\\"authors\\\": \\\"Shiri, Fatemeh and Nguyen, Van and Moghimifar, Farhad and Yoo, John and Haffari,...\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"Proceedings of the IEEE International Conference on Tools with Artificial Intell...\\\"}, {\\\"key\\\": \\\"crossagentie-2025\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"CROSSAGENTIE: Cross-Type and Cross-Task Multi-Agent LLM Collaboration for Zero-Shot Information Extraction\\\", \\\"authors\\\": \\\"Lu, Meng and Xie, Yuzhang and Bi, Zhenyu and Cao, Shuxiang and Wang, Xuan\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"Findings of the Association for Computational Linguistics: ACL 2025\\\"}, {\\\"key\\\": \\\"cmas-ner-2025\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"A Cooperative Multi-Agent Framework for Zero-Shot Named Entity Recognition\\\", \\\"authors\\\": \\\"Wang, Zihan and Zhao, Ziqi and Lyu, Yougang and Chen, Zhumin and de Rijke, Maart...\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"Proceedings of the ACM Web Conference 2025\\\"}, {\\\"key\\\": \\\"uniner-2024\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"UniversalNER: Targeted Distillation from Large Language Models for Open Named Entity Recognition\\\", \\\"authors\\\": \\\"Zhou, Wenxuan and Zhang, Sheng and Gu, Yu and Chen, Muhao and Poon, Hoifung\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"International Conference on Learning Representations\\\"}, {\\\"key\\\": \\\"gollie-2024\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"GoLLIE: Annotation Guidelines improve Zero-Shot Information-Extraction\\\", \\\"authors\\\": \\\"Sainz, Oscar and Garc\\\\\\\\'\\\\\\\\ia-Ferrero, Iker and Agerri, Rodrigo and Lopez de Lacall...\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"International Conference on Learning Representations\\\"}, {\\\"key\\\": \\\"gliner-2024\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"GLiNER: Generalist Model for Named Entity Recognition using Bidirectional Transformer\\\", \\\"authors\\\": \\\"Zaratiana, Urchade and Tomeh, Nadi and Holat, Pierre and Charnois, Thierry\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"Proceedings of the 2024 Conference of the North American Chapter of the Associat...\\\"}, {\\\"key\\\": \\\"gliner2-2025\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"GLiNER2: Schema-Driven Multi-Task Learning for Structured Information Extraction\\\", \\\"authors\\\": \\\"Zaratiana, Urchade and Pasternak, Gil and Boyd, Oliver and Hurn-Maloney, George ...\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"Proceedings of the 2025 Conference on Empirical Methods in Natural Language Proc...\\\"}, {\\\"key\\\": \\\"iepile-2024\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"IEPile: Unearthing Large Scale Schema-Conditioned Information Extraction Corpus\\\", \\\"authors\\\": \\\"Gui, Honghao and Yuan, Lin and Ye, Hongbin and Zhang, Ningyu and Sun, Mengshu an...\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"Proceedings of the 62nd Annual Meeting of the Association for Computational Ling...\\\"}, {\\\"key\\\": \\\"dror-2018-significance\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"The Hitchhiker's Guide to Testing Statistical Significance in Natural Language Processing\\\", \\\"authors\\\": \\\"Dror, Rotem and Baumer, Gili and Shlomov, Segev and Reichart, Roi\\\", \\\"year\\\": \\\"2018\\\", \\\"venue\\\": \\\"Proceedings of the 56th Annual Meeting of the Association for Computational Ling...\\\"}, {\\\"key\\\": \\\"lost-in-middle-2024\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Lost in the Middle: How Language Models Use Long Contexts\\\", \\\"authors\\\": \\\"Liu, Nelson F. and Lin, Kevin and Hewitt, John and Paranjape, Ashwin and Bevilac...\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"Transactions of the Association for Computational Linguistics\\\"}, {\\\"key\\\": \\\"llm4ie-survey-2024\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Large Language Models for Generative Information Extraction: A Survey\\\", \\\"authors\\\": \\\"Xu, Derong and Chen, Wei and Peng, Wenjun and Zhang, Chao and Xu, Tong and Zhao,...\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"Frontiers of Computer Science\\\"}, {\\\"key\\\": \\\"knowcoder-2024\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"KnowCoder: Coding Structured Knowledge into LLMs for Universal Information Extraction\\\", \\\"authors\\\": \\\"Li, Zixuan and Zeng, Yutao and Zuo, Yuxin and Ren, Weicheng and Liu, Wenxuan and...\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"Proceedings of the 62nd Annual Meeting of the Association for Computational Ling...\\\"}, {\\\"key\\\": \\\"slot-2025\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"SLOT: Structuring the Output of Large Language Models\\\", \\\"authors\\\": \\\"Shen, Zhengyuan and Wang, Darren Yow-Bang and Mishra, Soumya Smruti and Xu, Zhic...\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"Proceedings of the 2025 Conference on Empirical Methods in Natural Language Proc...\\\"}, {\\\"key\\\": \\\"gao-repr-degen-2019\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Representation Degeneration Problem in Training Natural Language Generation Models\\\", \\\"authors\\\": \\\"Gao, Jun and He, Di and Tan, Xu and Qin, Tao and Wang, Liwei and Liu, Tie-Yan\\\", \\\"year\\\": \\\"2019\\\", \\\"venue\\\": \\\"International Conference on Learning Representations\\\"}, {\\\"key\\\": \\\"ethayarajh-contextual-2019\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"How Contextual are Contextualized Word Representations? Comparing the Geometry of BERT, ELMo, and GPT-2 Embeddings\\\", \\\"authors\\\": \\\"Ethayarajh, Kawin\\\", \\\"year\\\": \\\"2019\\\", \\\"venue\\\": \\\"Proceedings of the 2019 Conference on Empirical Methods in Natural Language Proc...\\\"}, {\\\"key\\\": \\\"cai-isotropy-clusters-2021\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Isotropy in the Contextual Embedding Space: Clusters and Manifolds\\\", \\\"authors\\\": \\\"Cai, Xingyu and Huang, Jiaji and Bian, Yuchen and Church, Kenneth\\\", \\\"year\\\": \\\"2021\\\", \\\"venue\\\": \\\"International Conference on Learning Representations\\\"}, {\\\"key\\\": \\\"instructuie-2023\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"InstructUIE: Multi-task Instruction Tuning for Unified Information Extraction\\\", \\\"authors\\\": \\\"Wang, Xiao and Zhou, Weikang and Zu, Can and Xia, Han and Chen, Tianze and Zhang...\\\", \\\"year\\\": \\\"2023\\\", \\\"venue\\\": \\\"arXiv preprint arXiv:2304.08085\\\"}, {\\\"key\\\": \\\"codeie-2023\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"CodeIE: Large Code Generation Models are Better Few-Shot Information Extractors\\\", \\\"authors\\\": \\\"Li, Peng and Sun, Tianxiang and Tang, Qiong and Yan, Hang and Wu, Yuanbin and Hu...\\\", \\\"year\\\": \\\"2023\\\", \\\"venue\\\": \\\"Proceedings of the 61st Annual Meeting of the Association for Computational Ling...\\\"}, {\\\"key\\\": \\\"adelie-2024\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"ADELIE: Aligning Large Language Models on Information Extraction\\\", \\\"authors\\\": \\\"Qi, Yunjia and Peng, Hao and Wang, Xiaozhi and Xu, Bin and Hou, Lei and Li, Juan...\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"Proceedings of the 2024 Conference on Empirical Methods in Natural Language Proc...\\\"}, {\\\"key\\\": \\\"oneke-2025\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"OneKE: A Dockerized Schema-Guided LLM Agent-based Knowledge Extraction System\\\", \\\"authors\\\": \\\"Luo, Yujie and Ru, Xiangyuan and Liu, Kangwei and Yuan, Lin and Sun, Mengshu and...\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"Companion Proceedings of the ACM Web Conference 2025\\\"}, {\\\"key\\\": \\\"fewnerd-2021\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Few-NERD: A Few-shot Named Entity Recognition Dataset\\\", \\\"authors\\\": \\\"Ding, Ning and Xu, Guangwei and Chen, Yulin and Wang, Xiaobin and Han, Xu and Xi...\\\", \\\"year\\\": \\\"2021\\\", \\\"venue\\\": \\\"Proceedings of the 59th Annual Meeting of the Association for Computational Ling...\\\"}, {\\\"key\\\": \\\"fewrel-2018\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"FewRel: A Large-Scale Supervised Few-Shot Relation Classification Dataset with State-of-the-Art Evaluation\\\", \\\"authors\\\": \\\"Han, Xu and Zhu, Hao and Yu, Pengfei and Wang, Ziyun and Yao, Yuan and Liu, Zhiy...\\\", \\\"year\\\": \\\"2018\\\", \\\"venue\\\": \\\"Proceedings of the 2018 Conference on Empirical Methods in Natural Language Proc...\\\"}, {\\\"key\\\": \\\"maven-2020\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"MAVEN: A Massive General Domain Event Detection Dataset\\\", \\\"authors\\\": \\\"Wang, Xiaozhi and Wang, Ziqi and Han, Xu and Jiang, Wangyi and Han, Rong and Liu...\\\", \\\"year\\\": \\\"2020\\\", \\\"venue\\\": \\\"Proceedings of the 2020 Conference on Empirical Methods in Natural Language Proc...\\\"}, {\\\"key\\\": \\\"docred-2019\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"DocRED: A Large-Scale Document-Level Relation Extraction Dataset\\\", \\\"authors\\\": \\\"Yao, Yuan and Ye, Deming and Li, Peng and Han, Xu and Lin, Yankai and Liu, Zheng...\\\", \\\"year\\\": \\\"2019\\\", \\\"venue\\\": \\\"Proceedings of the 57th Annual Meeting of the Association for Computational Ling...\\\"}, {\\\"key\\\": \\\"qwen3-2025\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Qwen3 Technical Report\\\", \\\"authors\\\": \\\"Qwen Team\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"arXiv preprint arXiv:2505.09388\\\"}, {\\\"key\\\": \\\"llama3-2024\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"The Llama 3 Herd of Models\\\", \\\"authors\\\": \\\"Dubey, Abhimanyu and Jauhri, Abhinav and Pandey, Abhinav and Kadian, Abhishek an...\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"arXiv preprint arXiv:2407.21783\\\"}, {\\\"key\\\": \\\"sentence-bert-2019\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks\\\", \\\"authors\\\": \\\"Reimers, Nils and Gurevych, Iryna\\\", \\\"year\\\": \\\"2019\\\", \\\"venue\\\": \\\"Proceedings of the 2019 Conference on Empirical Methods in Natural Language Proc...\\\"}, {\\\"key\\\": \\\"minilm-2020\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"MiniLM: Deep Self-Attention Distillation for Task-Agnostic Compression of Pre-Trained Transformers\\\", \\\"authors\\\": \\\"Wang, Wenhui and Wei, Furu and Dong, Li and Bao, Hangbo and Yang, Nan and Zhou, ...\\\", \\\"year\\\": \\\"2020\\\", \\\"venue\\\": \\\"Advances in Neural Information Processing Systems\\\"}, {\\\"key\\\": \\\"reflect-learn-2026\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Reflect then Learn: Active Prompting for Information Extraction Guided by Introspective Confusion\\\", \\\"authors\\\": \\\"Zhao, Dong and Wang, Yadong and Chen, Xiang and Wang, Chenxi and Dai, Hongliang ...\\\", \\\"year\\\": \\\"2026\\\", \\\"venue\\\": \\\"Proceedings of the AAAI Conference on Artificial Intelligence\\\"}, {\\\"key\\\": \\\"sclar-sensitivity-2024\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Quantifying Language Models' Sensitivity to Spurious Features in Prompt Design\\\", \\\"authors\\\": \\\"Sclar, Melanie and Choi, Yejin and Tsvetkov, Yulia and Suhr, Alane\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"International Conference on Learning Representations\\\"}, {\\\"key\\\": \\\"vllm-2023\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Efficient Memory Management for Large Language Model Serving with PagedAttention\\\", \\\"authors\\\": \\\"Kwon, Woosuk and Li, Zhuohan and Zhuang, Siyuan and Sheng, Ying and Zheng, Lianm...\\\", \\\"year\\\": \\\"2023\\\", \\\"venue\\\": \\\"Proceedings of the 29th Symposium on Operating Systems Principles\\\"}, {\\\"key\\\": \\\"xie-zeroshot-ner-2023\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Empirical Study of Zero-Shot NER with ChatGPT\\\", \\\"authors\\\": \\\"Xie, Tingyu and Li, Qi and Zhang, Jian and Zhang, Yan and Liu, Zuozhu and Wang, ...\\\", \\\"year\\\": \\\"2023\\\", \\\"venue\\\": \\\"Proceedings of the 2023 Conference on Empirical Methods in Natural Language Proc...\\\"}, {\\\"key\\\": \\\"wadhwa-re-llm-2023\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Revisiting Relation Extraction in the era of Large Language Models\\\", \\\"authors\\\": \\\"Wadhwa, Somin and Amir, Silvio and Wallace, Byron C.\\\", \\\"year\\\": \\\"2023\\\", \\\"venue\\\": \\\"Proceedings of the 61st Annual Meeting of the Association for Computational Ling...\\\"}, {\\\"key\\\": \\\"relationprompt-2022\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"RelationPrompt: Leveraging Prompts to Generate Synthetic Data for Zero-Shot Relation Triplet Extraction\\\", \\\"authors\\\": \\\"Chia, Yew Ken and Bing, Lidong and Poria, Soujanya and Si, Luo\\\", \\\"year\\\": \\\"2022\\\", \\\"venue\\\": \\\"Findings of the Association for Computational Linguistics: ACL 2022\\\"}, {\\\"key\\\": \\\"promptner-2023\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"PromptNER: Prompting For Named Entity Recognition\\\", \\\"authors\\\": \\\"Ashok, Dhananjay and Lipton, Zachary C.\\\", \\\"year\\\": \\\"2023\\\", \\\"venue\\\": \\\"arXiv preprint arXiv:2305.15444\\\"}, {\\\"key\\\": \\\"json-schema-bench-2025\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"JSONSchemaBench: A Rigorous Benchmark of Structured Outputs for Language Models\\\", \\\"authors\\\": \\\"Geng, Saibo and Cooper, Hudson and Moskal, Micha\\\\\\\\l and Jenkins, Samuel and Berma...\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"arXiv preprint arXiv:2501.10868\\\"}, {\\\"key\\\": \\\"rastogi2020towards\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Towards Scalable Multi-Domain Conversational Agents: The Schema-Guided Dialogue Dataset\\\", \\\"authors\\\": \\\"Rastogi, Abhinav and Zang, Xiaoxue and Sunkara, Srinivas and Gupta, Raghav and K...\\\", \\\"year\\\": \\\"2020\\\", \\\"venue\\\": \\\"Proceedings of the AAAI Conference on Artificial Intelligence\\\"}, {\\\"key\\\": \\\"li2023evaluating\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Evaluating ChatGPT's Information Extraction Capabilities: An Assessment of Performance, Explainability, Calibration, and...\\\", \\\"authors\\\": \\\"Li, Bo and Fang, Gexiang and Yang, Yang and Wang, Quansen and Ye, Wei and Zhao, ...\\\", \\\"year\\\": \\\"2023\\\", \\\"venue\\\": \\\"arXiv preprint arXiv:2304.11633\\\"}, {\\\"key\\\": \\\"lee2022sgd\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"SGD-X: A Benchmark for Robust Generalization in Schema-Guided Dialogue Systems\\\", \\\"authors\\\": \\\"Lee, Harrison and Gupta, Raghav and Rastogi, Abhinav and Cao, Yuan and Zhang, Bi...\\\", \\\"year\\\": \\\"2022\\\", \\\"venue\\\": \\\"Proceedings of the AAAI Conference on Artificial Intelligence\\\"}, {\\\"key\\\": \\\"volkanovska2025ner\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"A Study of Errors in the Output of Large Language Models for Domain-Specific Few-Shot Named Entity Recognition\\\", \\\"authors\\\": \\\"Volkanovska, Elena\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"Journal for Language Technology and Computational Linguistics\\\"}, {\\\"key\\\": \\\"haystack-to-needle-2025\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"From Haystack to Needle: Label Space Reduction for Zero-shot Classification\\\", \\\"authors\\\": \\\"Vandemoortele, Nathan and Steenwinckel, Bram and Ongenae, Femke and Van Hoecke, ...\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"arXiv preprint arXiv:2502.08436\\\"}, {\\\"key\\\": \\\"cohen-1988-power\\\", \\\"type\\\": \\\"book\\\", \\\"title\\\": \\\"Statistical Power Analysis for the Behavioral Sciences\\\", \\\"authors\\\": \\\"Cohen, Jacob\\\", \\\"year\\\": \\\"1988\\\", \\\"venue\\\": \\\"\\\"}, {\\\"key\\\": \\\"lakens-2013-effect-size\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Calculating and Reporting Effect Sizes to Facilitate Cumulative Science: A Practical Primer for t-Tests and ANOVAs\\\", \\\"authors\\\": \\\"Lakens, Dani\\\\\\\\\\\\\\\"el\\\", \\\"year\\\": \\\"2013\\\", \\\"venue\\\": \\\"Frontiers in Psychology\\\"}, {\\\"key\\\": \\\"deng-2010-imagenet\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"What Does Classifying More Than 10,000 Image Categories Tell Us?\\\", \\\"authors\\\": \\\"Deng, Jia and Berg, Alexander C. and Li, Kai and Fei-Fei, Li\\\", \\\"year\\\": \\\"2010\\\", \\\"venue\\\": \\\"Proceedings of the 11th European Conference on Computer Vision\\\"}, {\\\"key\\\": \\\"rothman-1990\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"No Adjustments Are Needed for Multiple Comparisons\\\", \\\"authors\\\": \\\"Rothman, Kenneth J.\\\", \\\"year\\\": \\\"1990\\\", \\\"venue\\\": \\\"Epidemiology\\\"}, {\\\"key\\\": \\\"lakens-2017-equivalence\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Equivalence Tests: A Practical Primer for t Tests, Correlations, and Meta-Analyses\\\", \\\"authors\\\": \\\"Lakens, Dani\\\\\\\\\\\\\\\"el\\\", \\\"year\\\": \\\"2017\\\", \\\"venue\\\": \\\"Social Psychological and Personality Science\\\"}, {\\\"key\\\": \\\"zhou-2025-rethinking\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Rethinking Word Similarity: Semantic Similarity through Classification Confusion\\\", \\\"authors\\\": \\\"Zhou, Kaitlyn and Gao, Haishan and Chen, Sarah Li and Edelstein, Dan and Jurafsk...\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"Proceedings of the 2025 Conference of the North American Chapter of the Associat...\\\"}, {\\\"key\\\": \\\"guo-2021-label-confusion\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Label Confusion Learning to Enhance Text Classification Models\\\", \\\"authors\\\": \\\"Guo, Biyang and Han, Songqiao and Han, Xiao and Huang, Hailiang and Lu, Ting\\\", \\\"year\\\": \\\"2021\\\", \\\"venue\\\": \\\"Proceedings of the AAAI Conference on Artificial Intelligence\\\"}, {\\\"key\\\": \\\"novack-2023-chils\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"CHiLS: Zero-Shot Image Classification with Hierarchical Label Sets\\\", \\\"authors\\\": \\\"Novack, Zachary and McAuley, Julian and Lipton, Zachary Chase and Garg, Saurabh\\\", \\\"year\\\": \\\"2023\\\", \\\"venue\\\": \\\"Proceedings of the 40th International Conference on Machine Learning\\\"}, {\\\"key\\\": \\\"cocchieri-2025-zeroner\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"ZeroNER: Fueling Zero-Shot Named Entity Recognition via Entity Type Descriptions\\\", \\\"authors\\\": \\\"Cocchieri, Alessio and Mart\\\\\\\\'\\\\\\\\inez Galindo, Marcos and Frisoni, Giacomo and Moro...\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"Findings of the Association for Computational Linguistics: ACL 2025\\\"}, {\\\"key\\\": \\\"dlisc-2025\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Effective and Efficient Schema-aware Information Extraction Using On-Device Large Language Models\\\", \\\"authors\\\": \\\"Li, Zhuoqun and Wu, Hao and Li, Xinxin and Li, Zhoujun\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"arXiv preprint arXiv:2505.14992\\\"}, {\\\"key\\\": \\\"spt-2025\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Schema as Parameterized Tools for Universal Information Extraction\\\", \\\"authors\\\": \\\"Liang, Sheng and Zhang, Yongyue and Wu, Yaxiong and Tang, Ruiming and Liu, Yong\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"arXiv preprint arXiv:2506.01276\\\"}, {\\\"key\\\": \\\"card-2020-power\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"With Little Power Comes Great Responsibility\\\", \\\"authors\\\": \\\"Card, Dallas and Henderson, Peter and Khandelwal, Urvashi and Jia, Robin and Mah...\\\", \\\"year\\\": \\\"2020\\\", \\\"venue\\\": \\\"Proceedings of the 2020 Conference on Empirical Methods in Natural Language Proc...\\\"}, {\\\"key\\\": \\\"gillick-2014-entity-typing\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Context-Dependent Fine-Grained Entity Type Tagging\\\", \\\"authors\\\": \\\"Gillick, Daniel and Lazic, Nevena and Ganchev, Kuzman and Kirchner, Jesse and Hu...\\\", \\\"year\\\": \\\"2014\\\", \\\"venue\\\": \\\"arXiv preprint arXiv:1412.1820\\\"}, {\\\"key\\\": \\\"schall-2025-hidden-cost\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"The Hidden Cost of Structure: How Constrained Decoding Affects Language Model Performance\\\", \\\"authors\\\": \\\"Schall, Maximilian and de Melo, Gerard\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"Proceedings of the 15th International Conference on Recent Advances in Natural L...\\\"}, {\\\"key\\\": \\\"chen-2026-multi-instance\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Understanding LLM Performance Degradation in Multi-Instance Processing: The Roles of Instance Count and Context Length\\\", \\\"authors\\\": \\\"Chen, Jingxuan and Pilehvar, Mohammad Taher and Camacho-Collados, Jose\\\", \\\"year\\\": \\\"2026\\\", \\\"venue\\\": \\\"arXiv preprint arXiv:2603.22608\\\"}, {\\\"key\\\": \\\"wei-2023-chatie\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Zero-Shot Information Extraction via Chatting with ChatGPT\\\", \\\"authors\\\": \\\"Wei, Xiang and Cui, Xingyu and Cheng, Ning and Wang, Xiaobin and Zhang, Xin and ...\\\", \\\"year\\\": \\\"2023\\\", \\\"venue\\\": \\\"arXiv preprint arXiv:2302.10205\\\"}], \\\"tex_citations\\\": [{\\\"key\\\": \\\"llm4ie-survey-2024\\\", \\\"file\\\": \\\"introduction.tex\\\", \\\"line\\\": 4, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"uniner-2024\\\", \\\"file\\\": \\\"introduction.tex\\\", \\\"line\\\": 6, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"llm-pee-2025\\\", \\\"file\\\": \\\"introduction.tex\\\", \\\"line\\\": 6, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"parse-2025\\\", \\\"file\\\": \\\"introduction.tex\\\", \\\"line\\\": 6, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"fewnerd-2021\\\", \\\"file\\\": \\\"introduction.tex\\\", \\\"line\\\": 12, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"fewrel-2018\\\", \\\"file\\\": \\\"introduction.tex\\\", \\\"line\\\": 12, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"docred-2019\\\", \\\"file\\\": \\\"introduction.tex\\\", \\\"line\\\": 12, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"maven-2020\\\", \\\"file\\\": \\\"introduction.tex\\\", \\\"line\\\": 12, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"llm-pee-2025\\\", \\\"file\\\": \\\"introduction.tex\\\", \\\"line\\\": 22, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"instructuie-2023\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 5, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"knowcoder-2024\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 5, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"codeie-2023\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 5, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"gollie-2024\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 5, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"adelie-2024\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 5, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"slot-2025\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 5, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"oneke-2025\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 5, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"json-schema-bench-2025\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 5, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"willard2023efficient\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 5, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"xie-zeroshot-ner-2023\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 5, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"promptner-2023\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 5, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"uniner-2024\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 5, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"gliner-2024\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 5, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"gliner2-2025\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 5, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"gillick-2014-entity-typing\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 5, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"relationprompt-2022\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 5, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"wadhwa-re-llm-2023\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 5, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"wei-2023-chatie\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 5, \\\"command\\\": \\\"citet\\\"}, {\\\"key\\\": \\\"llm-pee-2025\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 8, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"iepile-2024\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 8, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"parse-2025\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 8, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"crossagentie-2025\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 8, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"cmas-ner-2025\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 8, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"dee-2024\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 8, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"reflect-learn-2026\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 8, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"chen-2026-multi-instance\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 8, \\\"command\\\": \\\"citet\\\"}, {\\\"key\\\": \\\"haystack-to-needle-2025\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 8, \\\"command\\\": \\\"citet\\\"}, {\\\"key\\\": \\\"dlisc-2025\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 8, \\\"command\\\": \\\"citet\\\"}, {\\\"key\\\": \\\"spt-2025\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 8, \\\"command\\\": \\\"citet\\\"}, {\\\"key\\\": \\\"rastogi2020towards\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 10, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"lee2022sgd\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 10, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"li2023evaluating\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 10, \\\"command\\\": \\\"citet\\\"}, {\\\"key\\\": \\\"lu2022fantastically\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 10, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"volkanovska2025ner\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 10, \\\"command\\\": \\\"citet\\\"}, {\\\"key\\\": \\\"deng-2010-imagenet\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 10, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"guo-2021-label-confusion\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 10, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"zhou-2025-rethinking\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 10, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"muller2019when\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 10, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"peterson2019human\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 10, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"novack-2023-chils\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 10, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"cocchieri-2025-zeroner\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 10, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"yang2025beyond\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 10, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"llm-pee-2025\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 12, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"snell2017prototypical\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 12, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"yin-2019-zero-shot-bench\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 12, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"cohen-1988-power\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 12, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"lakens-2013-effect-size\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 12, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"gao-repr-degen-2019\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 12, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"ethayarajh-contextual-2019\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 12, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"cai-isotropy-clusters-2021\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 12, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"fewnerd-2021\\\", \\\"file\\\": \\\"experimental_setup.tex\\\", \\\"line\\\": 10, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"fewrel-2018\\\", \\\"file\\\": \\\"experimental_setup.tex\\\", \\\"line\\\": 13, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"docred-2019\\\", \\\"file\\\": \\\"experimental_setup.tex\\\", \\\"line\\\": 16, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"maven-2020\\\", \\\"file\\\": \\\"experimental_setup.tex\\\", \\\"line\\\": 19, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"qwen3-2025\\\", \\\"file\\\": \\\"experimental_setup.tex\\\", \\\"line\\\": 56, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"minilm-2020\\\", \\\"file\\\": \\\"experimental_setup.tex\\\", \\\"line\\\": 56, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"sentence-bert-2019\\\", \\\"file\\\": \\\"experimental_setup.tex\\\", \\\"line\\\": 56, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"sentence-bert-2019\\\", \\\"file\\\": \\\"experimental_setup.tex\\\", \\\"line\\\": 56, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"ethayarajh-contextual-2019\\\", \\\"file\\\": \\\"experimental_setup.tex\\\", \\\"line\\\": 56, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"qwen3-2025\\\", \\\"file\\\": \\\"experimental_setup.tex\\\", \\\"line\\\": 82, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"vllm-2023\\\", \\\"file\\\": \\\"experimental_setup.tex\\\", \\\"line\\\": 82, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"sclar-sensitivity-2024\\\", \\\"file\\\": \\\"experimental_setup.tex\\\", \\\"line\\\": 82, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"llama3-2024\\\", \\\"file\\\": \\\"experimental_setup.tex\\\", \\\"line\\\": 82, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"lost-in-middle-2024\\\", \\\"file\\\": \\\"results.tex\\\", \\\"line\\\": 49, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"lakens-2017-equivalence\\\", \\\"file\\\": \\\"results.tex\\\", \\\"line\\\": 87, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"schuirmann-1987-tost\\\", \\\"file\\\": \\\"results.tex\\\", \\\"line\\\": 87, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"cai-isotropy-clusters-2021\\\", \\\"file\\\": \\\"results.tex\\\", \\\"line\\\": 92, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"tam-2024-let-me-speak\\\", \\\"file\\\": \\\"discussion.tex\\\", \\\"line\\\": 11, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"schall-2025-hidden-cost\\\", \\\"file\\\": \\\"discussion.tex\\\", \\\"line\\\": 11, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"rothman-1990\\\", \\\"file\\\": \\\"main.tex\\\", \\\"line\\\": 51, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"dror-2018-significance\\\", \\\"file\\\": \\\"main.tex\\\", \\\"line\\\": 51, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"card-2020-power\\\", \\\"file\\\": \\\"main.tex\\\", \\\"line\\\": 51, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"fewnerd-2021\\\", \\\"file\\\": \\\"checklist.tex\\\", \\\"line\\\": 33, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"fewrel-2018\\\", \\\"file\\\": \\\"checklist.tex\\\", \\\"line\\\": 33, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"docred-2019\\\", \\\"file\\\": \\\"checklist.tex\\\", \\\"line\\\": 33, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"maven-2020\\\", \\\"file\\\": \\\"checklist.tex\\\", \\\"line\\\": 33, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"qwen3-2025\\\", \\\"file\\\": \\\"checklist.tex\\\", \\\"line\\\": 33, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"llama3-2024\\\", \\\"file\\\": \\\"checklist.tex\\\", \\\"line\\\": 33, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"vllm-2023\\\", \\\"file\\\": \\\"checklist.tex\\\", \\\"line\\\": 33, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"minilm-2020\\\", \\\"file\\\": \\\"checklist.tex\\\", \\\"line\\\": 33, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"fewnerd-2021\\\", \\\"file\\\": \\\"prompt_appendix.tex\\\", \\\"line\\\": 204, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"maven-2020\\\", \\\"file\\\": \\\"prompt_appendix.tex\\\", \\\"line\\\": 205, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"fewrel-2018\\\", \\\"file\\\": \\\"prompt_appendix.tex\\\", \\\"line\\\": 206, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"rothman-1990\\\", \\\"file\\\": \\\"main.tex\\\", \\\"line\\\": 321, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"li2023evaluating\\\", \\\"file\\\": \\\"main.tex\\\", \\\"line\\\": 518, \\\"command\\\": \\\"citet\\\"}, {\\\"key\\\": \\\"gemini-2025\\\", \\\"file\\\": \\\"main.tex\\\", \\\"line\\\": 563, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"lost-in-middle-2024\\\", \\\"file\\\": \\\"main.tex\\\", \\\"line\\\": 607, \\\"command\\\": \\\"cite\\\"}], \\\"online_verification\\\": [{\\\"key\\\": \\\"tam-2024-let-me-speak\\\", \\\"title\\\": \\\"Let Me Speak Freely? A Study on the Impact of Format Restrictions on Performance of Large Language Models\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Let Me Speak Freely? A Study on the Impact of Format Restrictions on Performance of Large Language Models\\\", \\\"matched_year\\\": \\\"2024\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"yin-2019-zero-shot-bench\\\", \\\"title\\\": \\\"Benchmarking Zero-shot Text Classification: Datasets, Evaluation and Entailment Approach\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Benchmarking Zero-shot Text Classification: Datasets, Evaluation and Entailment Approach\\\", \\\"matched_year\\\": \\\"2019\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"schuirmann-1987-tost\\\", \\\"title\\\": \\\"A Comparison of the Two One-Sided Tests Procedure and the Power Approach for Assessing the Equivalence of Average Bioavailability\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"A comparison of the Two One-Sided Tests Procedure and the Power Approach for assessing the equivalence of average bioavailability\\\", \\\"matched_year\\\": \\\"1987\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"gemini-2025\\\", \\\"title\\\": \\\"Gemini 2.5: Pushing the Frontier with Advanced Reasoning, Multimodality, and Long Context\\\", \\\"status\\\": \\\"not_found\\\", \\\"confidence\\\": 0.443, \\\"matched_title\\\": \\\"MM-LLMs: Recent Advances in MultiModal Large Language Models\\\", \\\"matched_year\\\": \\\"\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"best match similarity 0.44 below threshold 0.82\\\"}, {\\\"key\\\": \\\"snell2017prototypical\\\", \\\"title\\\": \\\"Prototypical Networks for Few-shot Learning\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Prototypical Networks for Few-shot Learning\\\", \\\"matched_year\\\": \\\"2017\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"muller2019when\\\", \\\"title\\\": \\\"When Does Label Smoothing Help?\\\", \\\"status\\\": \\\"mismatch\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"When Does Label Smoothing Help?\\\", \\\"matched_year\\\": \\\"2019\\\", \\\"mismatch_fields\\\": [\\\"first_author: bib=m\\\\\\\\\\\\\\\"uller vs api=müller\\\"], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"peterson2019human\\\", \\\"title\\\": \\\"Human Uncertainty Makes Classification More Robust\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Human Uncertainty Makes Classification More Robust\\\", \\\"matched_year\\\": \\\"2019\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"jagannatha2020calibrating\\\", \\\"title\\\": \\\"Calibrating Structured Output Predictors for Natural Language Processing\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Calibrating Structured Output Predictors for Natural Language Processing\\\", \\\"matched_year\\\": \\\"2020\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"willard2023efficient\\\", \\\"title\\\": \\\"Efficient Guided Generation for Large Language Models\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Efficient Guided Generation for Large Language Models\\\", \\\"matched_year\\\": \\\"2023\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"lu2022fantastically\\\", \\\"title\\\": \\\"Fantastically Ordered Prompts and Where to Find Them: Overcoming Few-Shot Prompt Order Sensitivity\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Fantastically Ordered Prompts and Where to Find Them: Overcoming Few-Shot Prompt Order Sensitivity\\\", \\\"matched_year\\\": \\\"2022\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"yang2025beyond\\\", \\\"title\\\": \\\"Beyond Boundaries: Learning a Universal Entity Taxonomy across Datasets and Languages for Open Named Entity Recognition\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Beyond Boundaries: Learning a Universal Entity Taxonomy across Datasets and Languages for Open Named Entity Recognition\\\", \\\"matched_year\\\": \\\"2024\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"llm-pee-2025\\\", \\\"title\\\": \\\"Towards Event Extraction with Massive Types: LLM-based Collaborative Annotation and Partitioning Extraction\\\", \\\"status\\\": \\\"mismatch\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Towards Event Extraction with Massive Types: LLM-based Collaborative Annotation and Partitioning Extraction\\\", \\\"matched_year\\\": \\\"2025\\\", \\\"mismatch_fields\\\": [\\\"first_author: bib=liu vs api=2025\\\"], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"parse-2025\\\", \\\"title\\\": \\\"PARSE: LLM Driven Schema Optimization for Reliable Entity Extraction\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"PARSE: LLM Driven Schema Optimization for Reliable Entity Extraction\\\", \\\"matched_year\\\": \\\"2025\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"dee-2024\\\", \\\"title\\\": \\\"Decompose, Enrich, and Extract! Schema-aware Event Extraction using LLMs\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Decompose, Enrich, and Extract! Schema-aware Event Extraction using LLMs\\\", \\\"matched_year\\\": \\\"2024\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"crossagentie-2025\\\", \\\"title\\\": \\\"CROSSAGENTIE: Cross-Type and Cross-Task Multi-Agent LLM Collaboration for Zero-Shot Information Extraction\\\", \\\"status\\\": \\\"mismatch\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"CROSSAGENTIE: Cross-Type and Cross-Task Multi-Agent LLM Collaboration for Zero-Shot Information Extraction\\\", \\\"matched_year\\\": \\\"2025\\\", \\\"mismatch_fields\\\": [\\\"first_author: bib=lu vs api=meng\\\"], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"cmas-ner-2025\\\", \\\"title\\\": \\\"A Cooperative Multi-Agent Framework for Zero-Shot Named Entity Recognition\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"A Cooperative Multi-Agent Framework for Zero-Shot Named Entity Recognition\\\", \\\"matched_year\\\": \\\"2025\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"uniner-2024\\\", \\\"title\\\": \\\"UniversalNER: Targeted Distillation from Large Language Models for Open Named Entity Recognition\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"UniversalNER: Targeted Distillation from Large Language Models for Open Named Entity Recognition\\\", \\\"matched_year\\\": \\\"2023\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"gollie-2024\\\", \\\"title\\\": \\\"GoLLIE: Annotation Guidelines improve Zero-Shot Information-Extraction\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"GoLLIE: Annotation Guidelines improve Zero-Shot Information-Extraction\\\", \\\"matched_year\\\": \\\"2023\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"gliner-2024\\\", \\\"title\\\": \\\"GLiNER: Generalist Model for Named Entity Recognition using Bidirectional Transformer\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"GLiNER: Generalist Model for Named Entity Recognition using Bidirectional Transformer\\\", \\\"matched_year\\\": \\\"2024\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"gliner2-2025\\\", \\\"title\\\": \\\"GLiNER2: Schema-Driven Multi-Task Learning for Structured Information Extraction\\\", \\\"status\\\": \\\"mismatch\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"GLiNER2: Schema-Driven Multi-Task Learning for Structured Information Extraction\\\", \\\"matched_year\\\": \\\"2025\\\", \\\"mismatch_fields\\\": [\\\"first_author: bib=zaratiana vs api=2025\\\"], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"iepile-2024\\\", \\\"title\\\": \\\"IEPile: Unearthing Large Scale Schema-Conditioned Information Extraction Corpus\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"IEPile: Unearthing Large Scale Schema-Conditioned Information Extraction Corpus\\\", \\\"matched_year\\\": \\\"2024\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"dror-2018-significance\\\", \\\"title\\\": \\\"The Hitchhiker's Guide to Testing Statistical Significance in Natural Language Processing\\\", \\\"status\\\": \\\"not_found\\\", \\\"confidence\\\": 0.339, \\\"matched_title\\\": \\\"The Sorcerer II Global Ocean Sampling Expedition: Northwest Atlantic through Eastern Tropical Pacific\\\", \\\"matched_year\\\": \\\"\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"best match similarity 0.34 below threshold 0.82\\\"}, {\\\"key\\\": \\\"lost-in-middle-2024\\\", \\\"title\\\": \\\"Lost in the Middle: How Language Models Use Long Contexts\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Lost in the Middle: How Language Models Use Long Contexts\\\", \\\"matched_year\\\": \\\"2024\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"llm4ie-survey-2024\\\", \\\"title\\\": \\\"Large Language Models for Generative Information Extraction: A Survey\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Large language models for generative information extraction: a survey\\\", \\\"matched_year\\\": \\\"2024\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"knowcoder-2024\\\", \\\"title\\\": \\\"KnowCoder: Coding Structured Knowledge into LLMs for Universal Information Extraction\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"KnowCoder: Coding Structured Knowledge into LLMs for Universal Information Extraction\\\", \\\"matched_year\\\": \\\"2024\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"slot-2025\\\", \\\"title\\\": \\\"SLOT: Structuring the Output of Large Language Models\\\", \\\"status\\\": \\\"mismatch\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"SLOT: Structuring the Output of Large Language Models\\\", \\\"matched_year\\\": \\\"2025\\\", \\\"mismatch_fields\\\": [\\\"first_author: bib=shen vs api=wang\\\"], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"gao-repr-degen-2019\\\", \\\"title\\\": \\\"Representation Degeneration Problem in Training Natural Language Generation Models\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Representation Degeneration Problem in Training Natural Language Generation Models\\\", \\\"matched_year\\\": \\\"2019\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"ethayarajh-contextual-2019\\\", \\\"title\\\": \\\"How Contextual are Contextualized Word Representations? Comparing the Geometry of BERT, ELMo, and GPT-2 Embeddings\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"How Contextual are Contextualized Word Representations? Comparing the Geometry of BERT, ELMo, and GPT-2 Embeddings\\\", \\\"matched_year\\\": \\\"2019\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"cai-isotropy-clusters-2021\\\", \\\"title\\\": \\\"Isotropy in the Contextual Embedding Space: Clusters and Manifolds\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Isotropy in the Contextual Embedding Space: Clusters and Manifolds\\\", \\\"matched_year\\\": \\\"2021\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"instructuie-2023\\\", \\\"title\\\": \\\"InstructUIE: Multi-task Instruction Tuning for Unified Information Extraction\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"InstructUIE: Multi-task Instruction Tuning for Unified Information Extraction\\\", \\\"matched_year\\\": \\\"2023\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"codeie-2023\\\", \\\"title\\\": \\\"CodeIE: Large Code Generation Models are Better Few-Shot Information Extractors\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"CodeIE: Large Code Generation Models are Better Few-Shot Information Extractors\\\", \\\"matched_year\\\": \\\"2023\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"adelie-2024\\\", \\\"title\\\": \\\"ADELIE: Aligning Large Language Models on Information Extraction\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"ADELIE: Aligning Large Language Models on Information Extraction\\\", \\\"matched_year\\\": \\\"2024\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"oneke-2025\\\", \\\"title\\\": \\\"OneKE: A Dockerized Schema-Guided LLM Agent-based Knowledge Extraction System\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"OneKE: A Dockerized Schema-Guided LLM Agent-based Knowledge Extraction System\\\", \\\"matched_year\\\": \\\"2025\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"fewnerd-2021\\\", \\\"title\\\": \\\"Few-NERD: A Few-shot Named Entity Recognition Dataset\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Few-NERD: A Few-shot Named Entity Recognition Dataset\\\", \\\"matched_year\\\": \\\"2021\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"fewrel-2018\\\", \\\"title\\\": \\\"FewRel: A Large-Scale Supervised Few-Shot Relation Classification Dataset with State-of-the-Art Evaluation\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"FewRel: A Large-Scale Supervised Few-Shot Relation Classification Dataset with State-of-the-Art Evaluation\\\", \\\"matched_year\\\": \\\"2018\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"maven-2020\\\", \\\"title\\\": \\\"MAVEN: A Massive General Domain Event Detection Dataset\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"MAVEN: A Massive General Domain Event Detection Dataset\\\", \\\"matched_year\\\": \\\"2020\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"docred-2019\\\", \\\"title\\\": \\\"DocRED: A Large-Scale Document-Level Relation Extraction Dataset\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"DocRED: A Large-Scale Document-Level Relation Extraction Dataset\\\", \\\"matched_year\\\": \\\"2019\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"qwen3-2025\\\", \\\"title\\\": \\\"Qwen3 Technical Report\\\", \\\"status\\\": \\\"mismatch\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Qwen3 Technical Report\\\", \\\"matched_year\\\": \\\"2025\\\", \\\"mismatch_fields\\\": [\\\"first_author: bib=team vs api=yang\\\"], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"llama3-2024\\\", \\\"title\\\": \\\"The Llama 3 Herd of Models\\\", \\\"status\\\": \\\"mismatch\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"The Llama 3 herd of models\\\", \\\"matched_year\\\": \\\"2025\\\", \\\"mismatch_fields\\\": [\\\"first_author: bib=dubey vs api=aaron\\\"], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"sentence-bert-2019\\\", \\\"title\\\": \\\"Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks\\\", \\\"matched_year\\\": \\\"2019\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"minilm-2020\\\", \\\"title\\\": \\\"MiniLM: Deep Self-Attention Distillation for Task-Agnostic Compression of Pre-Trained Transformers\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"MiniLM: Deep Self-Attention Distillation for Task-Agnostic Compression of Pre-Trained Transformers\\\", \\\"matched_year\\\": \\\"2020\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"reflect-learn-2026\\\", \\\"title\\\": \\\"Reflect then Learn: Active Prompting for Information Extraction Guided by Introspective Confusion\\\", \\\"status\\\": \\\"mismatch\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Reflect Then Learn: Active Prompting for Information Extraction Guided by Introspective Confusion\\\", \\\"matched_year\\\": \\\"2026\\\", \\\"mismatch_fields\\\": [\\\"first_author: bib=zhao vs api=2026\\\"], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"sclar-sensitivity-2024\\\", \\\"title\\\": \\\"Quantifying Language Models' Sensitivity to Spurious Features in Prompt Design\\\", \\\"status\\\": \\\"not_found\\\", \\\"confidence\\\": 0.72, \\\"matched_title\\\": \\\"Quantifying Language Models' Sensitivity to Spurious Features in Prompt Design or: How I learned to start worrying about prompt formatting\\\", \\\"matched_year\\\": \\\"\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"best match similarity 0.72 below threshold 0.82\\\"}, {\\\"key\\\": \\\"vllm-2023\\\", \\\"title\\\": \\\"Efficient Memory Management for Large Language Model Serving with PagedAttention\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Efficient Memory Management for Large Language Model Serving with PagedAttention\\\", \\\"matched_year\\\": \\\"2023\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"xie-zeroshot-ner-2023\\\", \\\"title\\\": \\\"Empirical Study of Zero-Shot NER with ChatGPT\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Empirical Study of Zero-Shot NER with ChatGPT\\\", \\\"matched_year\\\": \\\"2023\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"wadhwa-re-llm-2023\\\", \\\"title\\\": \\\"Revisiting Relation Extraction in the era of Large Language Models\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Revisiting Relation Extraction in the era of Large Language Models\\\", \\\"matched_year\\\": \\\"2023\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"relationprompt-2022\\\", \\\"title\\\": \\\"RelationPrompt: Leveraging Prompts to Generate Synthetic Data for Zero-Shot Relation Triplet Extraction\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"RelationPrompt: Leveraging Prompts to Generate Synthetic Data for Zero-Shot Relation Triplet Extraction\\\", \\\"matched_year\\\": \\\"2022\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"promptner-2023\\\", \\\"title\\\": \\\"PromptNER: Prompting For Named Entity Recognition\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"PromptNER: Prompting For Named Entity Recognition\\\", \\\"matched_year\\\": \\\"2023\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"json-schema-bench-2025\\\", \\\"title\\\": \\\"JSONSchemaBench: A Rigorous Benchmark of Structured Outputs for Language Models\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"JSONSchemaBench: A Rigorous Benchmark of Structured Outputs for Language Models\\\", \\\"matched_year\\\": \\\"2025\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"rastogi2020towards\\\", \\\"title\\\": \\\"Towards Scalable Multi-Domain Conversational Agents: The Schema-Guided Dialogue Dataset\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Towards Scalable Multi-Domain Conversational Agents: The Schema-Guided Dialogue Dataset\\\", \\\"matched_year\\\": \\\"2020\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"li2023evaluating\\\", \\\"title\\\": \\\"Evaluating ChatGPT's Information Extraction Capabilities: An Assessment of Performance, Explainability, Calibration, and Faithfulness\\\", \\\"status\\\": \\\"not_found\\\", \\\"confidence\\\": 0.333, \\\"matched_title\\\": \\\"Generative AI in Medical Practice: In-Depth Exploration of Privacy and Security Challenges\\\", \\\"matched_year\\\": \\\"\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"best match similarity 0.33 below threshold 0.82\\\"}, {\\\"key\\\": \\\"lee2022sgd\\\", \\\"title\\\": \\\"SGD-X: A Benchmark for Robust Generalization in Schema-Guided Dialogue Systems\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"SGD-X: A Benchmark for Robust Generalization in Schema-Guided Dialogue Systems\\\", \\\"matched_year\\\": \\\"2022\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"volkanovska2025ner\\\", \\\"title\\\": \\\"A Study of Errors in the Output of Large Language Models for Domain-Specific Few-Shot Named Entity Recognition\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"A Study of Errors in the Output of Large Language Models for Domain-Specific Few-Shot Named Entity Recognition\\\", \\\"matched_year\\\": \\\"2025\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"haystack-to-needle-2025\\\", \\\"title\\\": \\\"From Haystack to Needle: Label Space Reduction for Zero-shot Classification\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"From Haystack to Needle: Label Space Reduction for Zero-shot Classification\\\", \\\"matched_year\\\": \\\"2025\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"cohen-1988-power\\\", \\\"title\\\": \\\"Statistical Power Analysis for the Behavioral Sciences\\\", \\\"status\\\": \\\"mismatch\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Statistical Power Analysis for the Behavioral Sciences\\\", \\\"matched_year\\\": \\\"1989\\\", \\\"mismatch_fields\\\": [\\\"first_author: bib=cohen vs api=muller\\\"], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"lakens-2013-effect-size\\\", \\\"title\\\": \\\"Calculating and Reporting Effect Sizes to Facilitate Cumulative Science: A Practical Primer for t-Tests and ANOVAs\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Calculating and reporting effect sizes to facilitate cumulative science: a practical primer for t-tests and ANOVAs\\\", \\\"matched_year\\\": \\\"2013\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"deng-2010-imagenet\\\", \\\"title\\\": \\\"What Does Classifying More Than 10,000 Image Categories Tell Us?\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"What Does Classifying More Than 10,000 Image Categories Tell Us?\\\", \\\"matched_year\\\": \\\"2010\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"rothman-1990\\\", \\\"title\\\": \\\"No Adjustments Are Needed for Multiple Comparisons\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"No Adjustments Are Needed for Multiple Comparisons\\\", \\\"matched_year\\\": \\\"1990\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"lakens-2017-equivalence\\\", \\\"title\\\": \\\"Equivalence Tests: A Practical Primer for t Tests, Correlations, and Meta-Analyses\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 0.988, \\\"matched_title\\\": \\\"Equivalence Tests: A Practical Primer for t-Tests, Correlations, and Meta-Analyses\\\", \\\"matched_year\\\": \\\"2016\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"zhou-2025-rethinking\\\", \\\"title\\\": \\\"Rethinking Word Similarity: Semantic Similarity through Classification Confusion\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Rethinking Word Similarity: Semantic Similarity through Classification Confusion\\\", \\\"matched_year\\\": \\\"2025\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"guo-2021-label-confusion\\\", \\\"title\\\": \\\"Label Confusion Learning to Enhance Text Classification Models\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Label Confusion Learning to Enhance Text Classification Models\\\", \\\"matched_year\\\": \\\"2021\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"novack-2023-chils\\\", \\\"title\\\": \\\"CHiLS: Zero-Shot Image Classification with Hierarchical Label Sets\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"CHiLS: Zero-Shot Image Classification with Hierarchical Label Sets\\\", \\\"matched_year\\\": \\\"2023\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"cocchieri-2025-zeroner\\\", \\\"title\\\": \\\"ZeroNER: Fueling Zero-Shot Named Entity Recognition via Entity Type Descriptions\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"ZeroNER: Fueling Zero-Shot Named Entity Recognition via Entity Type Descriptions\\\", \\\"matched_year\\\": \\\"2025\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"dlisc-2025\\\", \\\"title\\\": \\\"Effective and Efficient Schema-aware Information Extraction Using On-Device Large Language Models\\\", \\\"status\\\": \\\"mismatch\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Effective and Efficient Schema-aware Information Extraction Using On-Device Large Language Models\\\", \\\"matched_year\\\": \\\"2025\\\", \\\"mismatch_fields\\\": [\\\"first_author: bib=li vs api=wen\\\"], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"spt-2025\\\", \\\"title\\\": \\\"Schema as Parameterized Tools for Universal Information Extraction\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Schema as Parameterized Tools for Universal Information Extraction\\\", \\\"matched_year\\\": \\\"2025\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"card-2020-power\\\", \\\"title\\\": \\\"With Little Power Comes Great Responsibility\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"With Little Power Comes Great Responsibility\\\", \\\"matched_year\\\": \\\"2020\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"gillick-2014-entity-typing\\\", \\\"title\\\": \\\"Context-Dependent Fine-Grained Entity Type Tagging\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Context-Dependent Fine-Grained Entity Type Tagging\\\", \\\"matched_year\\\": \\\"2014\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"schall-2025-hidden-cost\\\", \\\"title\\\": \\\"The Hidden Cost of Structure: How Constrained Decoding Affects Language Model Performance\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"The Hidden Cost of Structure: How Constrained Decoding Affects Language Model Performance\\\", \\\"matched_year\\\": \\\"2025\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"chen-2026-multi-instance\\\", \\\"title\\\": \\\"Understanding LLM Performance Degradation in Multi-Instance Processing: The Roles of Instance Count and Context Length\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Understanding LLM Performance Degradation in Multi-Instance Processing: The Roles of Instance Count and Context Length\\\", \\\"matched_year\\\": \\\"2026\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"wei-2023-chatie\\\", \\\"title\\\": \\\"Zero-Shot Information Extraction via Chatting with ChatGPT\\\", \\\"status\\\": \\\"mismatch\\\", \\\"confidence\\\": 0.935, \\\"matched_title\\\": \\\"ChatIE: Zero-Shot Information Extraction via Chatting with ChatGPT\\\", \\\"matched_year\\\": \\\"2023\\\", \\\"mismatch_fields\\\": [\\\"first_author: bib=wei vs api=xiang\\\"], \\\"note\\\": \\\"\\\"}]}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"summary\": {\"total_bib_entries\": 70, \"total_citations\": 96, \"unique_cited_keys\": 69, \"orphan_bib\": 1, \"missing_bib\": 0, \"duplicate_keys\": 0, \"online_verified\": 55, \"online_not_found\": 4, \"online_mismatch\": 11}, \"cross_check\": {\"orphan_bib\": [\"jagannatha2020calibrating\"], \"missing_bib\": [], \"orphan_count\": 1, \"missing_count\": 0}, \"bib_entries\": [{\"key\": \"tam-2024-let-me-speak\", \"type\": \"inproceedings\", \"title\": \"Let Me Speak Freely? A Study on the Impact of Format Restrictions on Performance of Large Language Models\", \"authors\": \"Tam, Zhi Rui and Wu, Cheng-Kuang and Tsai, Yi-Lin and Lin, Chieh-Yen and Lee, Hu...\", \"year\": \"2024\", \"venue\": \"Proceedings of the 2024 Conference on Empirical Methods in Natural Language Proc...\"}, {\"key\": \"yin-2019-zero-shot-bench\", \"type\": \"inproceedings\", \"title\": \"Benchmarking Zero-shot Text Classification: Datasets, Evaluation and Entailment Approach\", \"authors\": \"Yin, Wenpeng and Hay, Jamaal and Roth, Dan\", \"year\": \"2019\", \"venue\": \"Proceedings of the 2019 Conference on Empirical Methods in Natural Language Proc...\"}, {\"key\": \"schuirmann-1987-tost\", \"type\": \"article\", \"title\": \"A Comparison of the Two One-Sided Tests Procedure and the Power Approach for Assessing the Equivalence of Average Bioava...\", \"authors\": \"Schuirmann, Donald J.\", \"year\": \"1987\", \"venue\": \"Journal of Pharmacokinetics and Biopharmaceutics\"}, {\"key\": \"gemini-2025\", \"type\": \"article\", \"title\": \"Gemini 2.5: Pushing the Frontier with Advanced Reasoning, Multimodality, and Long Context\", \"authors\": \"Comanici, Gheorghe and others\", \"year\": \"2025\", \"venue\": \"arXiv preprint arXiv:2507.06261\"}, {\"key\": \"snell2017prototypical\", \"type\": \"inproceedings\", \"title\": \"Prototypical Networks for Few-shot Learning\", \"authors\": \"Snell, Jake and Swersky, Kevin and Zemel, Richard\", \"year\": \"2017\", \"venue\": \"Advances in Neural Information Processing Systems\"}, {\"key\": \"muller2019when\", \"type\": \"inproceedings\", \"title\": \"When Does Label Smoothing Help?\", \"authors\": \"M\\\\\\\"uller, Rafael and Kornblith, Simon and Hinton, Geoffrey E.\", \"year\": \"2019\", \"venue\": \"Advances in Neural Information Processing Systems\"}, {\"key\": \"peterson2019human\", \"type\": \"inproceedings\", \"title\": \"Human Uncertainty Makes Classification More Robust\", \"authors\": \"Peterson, Joshua C. and Battleday, Ruairidh M. and Griffiths, Thomas L. and Russ...\", \"year\": \"2019\", \"venue\": \"Proceedings of the IEEE/CVF International Conference on Computer Vision\"}, {\"key\": \"jagannatha2020calibrating\", \"type\": \"inproceedings\", \"title\": \"Calibrating Structured Output Predictors for Natural Language Processing\", \"authors\": \"Jagannatha, Abhyuday and Yu, Hong\", \"year\": \"2020\", \"venue\": \"Proceedings of the 58th Annual Meeting of the Association for Computational Ling...\"}, {\"key\": \"willard2023efficient\", \"type\": \"article\", \"title\": \"Efficient Guided Generation for Large Language Models\", \"authors\": \"Willard, Brandon T. and Louf, R\\\\'emi\", \"year\": \"2023\", \"venue\": \"arXiv preprint arXiv:2307.09702\"}, {\"key\": \"lu2022fantastically\", \"type\": \"inproceedings\", \"title\": \"Fantastically Ordered Prompts and Where to Find Them: Overcoming Few-Shot Prompt Order Sensitivity\", \"authors\": \"Lu, Yao and Bartolo, Max and Moore, Alastair and Riedel, Sebastian and Stenetorp...\", \"year\": \"2022\", \"venue\": \"Proceedings of the 60th Annual Meeting of the Association for Computational Ling...\"}, {\"key\": \"yang2025beyond\", \"type\": \"inproceedings\", \"title\": \"Beyond Boundaries: Learning a Universal Entity Taxonomy across Datasets and Languages for Open Named Entity Recognition\", \"authors\": \"Yang, Yuming and Zhao, Wantong and Huang, Caishuang and Ye, Junjie and Wang, Xia...\", \"year\": \"2025\", \"venue\": \"Proceedings of the 31st International Conference on Computational Linguistics\"}, {\"key\": \"llm-pee-2025\", \"type\": \"inproceedings\", \"title\": \"Towards Event Extraction with Massive Types: LLM-based Collaborative Annotation and Partitioning Extraction\", \"authors\": \"Liu, Wenxuan and Li, Zixuan and Bai, Long and Zuo, Yuxin and Xu, Daozhu and Jin,...\", \"year\": \"2025\", \"venue\": \"Proceedings of the 2025 Conference on Empirical Methods in Natural Language Proc...\"}, {\"key\": \"parse-2025\", \"type\": \"inproceedings\", \"title\": \"PARSE: LLM Driven Schema Optimization for Reliable Entity Extraction\", \"authors\": \"Shrimal, Anubhav and Jain, Aryan and Chowdhury, Soumyajit and Yenigalla, Promod\", \"year\": \"2025\", \"venue\": \"Proceedings of the 2025 Conference on Empirical Methods in Natural Language Proc...\"}, {\"key\": \"dee-2024\", \"type\": \"inproceedings\", \"title\": \"Decompose, Enrich, and Extract! Schema-aware Event Extraction using LLMs\", \"authors\": \"Shiri, Fatemeh and Nguyen, Van and Moghimifar, Farhad and Yoo, John and Haffari,...\", \"year\": \"2024\", \"venue\": \"Proceedings of the IEEE International Conference on Tools with Artificial Intell...\"}, {\"key\": \"crossagentie-2025\", \"type\": \"inproceedings\", \"title\": \"CROSSAGENTIE: Cross-Type and Cross-Task Multi-Agent LLM Collaboration for Zero-Shot Information Extraction\", \"authors\": \"Lu, Meng and Xie, Yuzhang and Bi, Zhenyu and Cao, Shuxiang and Wang, Xuan\", \"year\": \"2025\", \"venue\": \"Findings of the Association for Computational Linguistics: ACL 2025\"}, {\"key\": \"cmas-ner-2025\", \"type\": \"inproceedings\", \"title\": \"A Cooperative Multi-Agent Framework for Zero-Shot Named Entity Recognition\", \"authors\": \"Wang, Zihan and Zhao, Ziqi and Lyu, Yougang and Chen, Zhumin and de Rijke, Maart...\", \"year\": \"2025\", \"venue\": \"Proceedings of the ACM Web Conference 2025\"}, {\"key\": \"uniner-2024\", \"type\": \"inproceedings\", \"title\": \"UniversalNER: Targeted Distillation from Large Language Models for Open Named Entity Recognition\", \"authors\": \"Zhou, Wenxuan and Zhang, Sheng and Gu, Yu and Chen, Muhao and Poon, Hoifung\", \"year\": \"2024\", \"venue\": \"International Conference on Learning Representations\"}, {\"key\": \"gollie-2024\", \"type\": \"inproceedings\", \"title\": \"GoLLIE: Annotation Guidelines improve Zero-Shot Information-Extraction\", \"authors\": \"Sainz, Oscar and Garc\\\\'\\\\ia-Ferrero, Iker and Agerri, Rodrigo and Lopez de Lacall...\", \"year\": \"2024\", \"venue\": \"International Conference on Learning Representations\"}, {\"key\": \"gliner-2024\", \"type\": \"inproceedings\", \"title\": \"GLiNER: Generalist Model for Named Entity Recognition using Bidirectional Transformer\", \"authors\": \"Zaratiana, Urchade and Tomeh, Nadi and Holat, Pierre and Charnois, Thierry\", \"year\": \"2024\", \"venue\": \"Proceedings of the 2024 Conference of the North American Chapter of the Associat...\"}, {\"key\": \"gliner2-2025\", \"type\": \"inproceedings\", \"title\": \"GLiNER2: Schema-Driven Multi-Task Learning for Structured Information Extraction\", \"authors\": \"Zaratiana, Urchade and Pasternak, Gil and Boyd, Oliver and Hurn-Maloney, George ...\", \"year\": \"2025\", \"venue\": \"Proceedings of the 2025 Conference on Empirical Methods in Natural Language Proc...\"}, {\"key\": \"iepile-2024\", \"type\": \"inproceedings\", \"title\": \"IEPile: Unearthing Large Scale Schema-Conditioned Information Extraction Corpus\", \"authors\": \"Gui, Honghao and Yuan, Lin and Ye, Hongbin and Zhang, Ningyu and Sun, Mengshu an...\", \"year\": \"2024\", \"venue\": \"Proceedings of the 62nd Annual Meeting of the Association for Computational Ling...\"}, {\"key\": \"dror-2018-significance\", \"type\": \"inproceedings\", \"title\": \"The Hitchhiker's Guide to Testing Statistical Significance in Natural Language Processing\", \"authors\": \"Dror, Rotem and Baumer, Gili and Shlomov, Segev and Reichart, Roi\", \"year\": \"2018\", \"venue\": \"Proceedings of the 56th Annual Meeting of the Association for Computational Ling...\"}, {\"key\": \"lost-in-middle-2024\", \"type\": \"article\", \"title\": \"Lost in the Middle: How Language Models Use Long Contexts\", \"authors\": \"Liu, Nelson F. and Lin, Kevin and Hewitt, John and Paranjape, Ashwin and Bevilac...\", \"year\": \"2024\", \"venue\": \"Transactions of the Association for Computational Linguistics\"}, {\"key\": \"llm4ie-survey-2024\", \"type\": \"article\", \"title\": \"Large Language Models for Generative Information Extraction: A Survey\", \"authors\": \"Xu, Derong and Chen, Wei and Peng, Wenjun and Zhang, Chao and Xu, Tong and Zhao,...\", \"year\": \"2024\", \"venue\": \"Frontiers of Computer Science\"}, {\"key\": \"knowcoder-2024\", \"type\": \"inproceedings\", \"title\": \"KnowCoder: Coding Structured Knowledge into LLMs for Universal Information Extraction\", \"authors\": \"Li, Zixuan and Zeng, Yutao and Zuo, Yuxin and Ren, Weicheng and Liu, Wenxuan and...\", \"year\": \"2024\", \"venue\": \"Proceedings of the 62nd Annual Meeting of the Association for Computational Ling...\"}, {\"key\": \"slot-2025\", \"type\": \"inproceedings\", \"title\": \"SLOT: Structuring the Output of Large Language Models\", \"authors\": \"Shen, Zhengyuan and Wang, Darren Yow-Bang and Mishra, Soumya Smruti and Xu, Zhic...\", \"year\": \"2025\", \"venue\": \"Proceedings of the 2025 Conference on Empirical Methods in Natural Language Proc...\"}, {\"key\": \"gao-repr-degen-2019\", \"type\": \"inproceedings\", \"title\": \"Representation Degeneration Problem in Training Natural Language Generation Models\", \"authors\": \"Gao, Jun and He, Di and Tan, Xu and Qin, Tao and Wang, Liwei and Liu, Tie-Yan\", \"year\": \"2019\", \"venue\": \"International Conference on Learning Representations\"}, {\"key\": \"ethayarajh-contextual-2019\", \"type\": \"inproceedings\", \"title\": \"How Contextual are Contextualized Word Representations? Comparing the Geometry of BERT, ELMo, and GPT-2 Embeddings\", \"authors\": \"Ethayarajh, Kawin\", \"year\": \"2019\", \"venue\": \"Proceedings of the 2019 Conference on Empirical Methods in Natural Language Proc...\"}, {\"key\": \"cai-isotropy-clusters-2021\", \"type\": \"inproceedings\", \"title\": \"Isotropy in the Contextual Embedding Space: Clusters and Manifolds\", \"authors\": \"Cai, Xingyu and Huang, Jiaji and Bian, Yuchen and Church, Kenneth\", \"year\": \"2021\", \"venue\": \"International Conference on Learning Representations\"}, {\"key\": \"instructuie-2023\", \"type\": \"article\", \"title\": \"InstructUIE: Multi-task Instruction Tuning for Unified Information Extraction\", \"authors\": \"Wang, Xiao and Zhou, Weikang and Zu, Can and Xia, Han and Chen, Tianze and Zhang...\", \"year\": \"2023\", \"venue\": \"arXiv preprint arXiv:2304.08085\"}, {\"key\": \"codeie-2023\", \"type\": \"inproceedings\", \"title\": \"CodeIE: Large Code Generation Models are Better Few-Shot Information Extractors\", \"authors\": \"Li, Peng and Sun, Tianxiang and Tang, Qiong and Yan, Hang and Wu, Yuanbin and Hu...\", \"year\": \"2023\", \"venue\": \"Proceedings of the 61st Annual Meeting of the Association for Computational Ling...\"}, {\"key\": \"adelie-2024\", \"type\": \"inproceedings\", \"title\": \"ADELIE: Aligning Large Language Models on Information Extraction\", \"authors\": \"Qi, Yunjia and Peng, Hao and Wang, Xiaozhi and Xu, Bin and Hou, Lei and Li, Juan...\", \"year\": \"2024\", \"venue\": \"Proceedings of the 2024 Conference on Empirical Methods in Natural Language Proc...\"}, {\"key\": \"oneke-2025\", \"type\": \"inproceedings\", \"title\": \"OneKE: A Dockerized Schema-Guided LLM Agent-based Knowledge Extraction System\", \"authors\": \"Luo, Yujie and Ru, Xiangyuan and Liu, Kangwei and Yuan, Lin and Sun, Mengshu and...\", \"year\": \"2025\", \"venue\": \"Companion Proceedings of the ACM Web Conference 2025\"}, {\"key\": \"fewnerd-2021\", \"type\": \"inproceedings\", \"title\": \"Few-NERD: A Few-shot Named Entity Recognition Dataset\", \"authors\": \"Ding, Ning and Xu, Guangwei and Chen, Yulin and Wang, Xiaobin and Han, Xu and Xi...\", \"year\": \"2021\", \"venue\": \"Proceedings of the 59th Annual Meeting of the Association for Computational Ling...\"}, {\"key\": \"fewrel-2018\", \"type\": \"inproceedings\", \"title\": \"FewRel: A Large-Scale Supervised Few-Shot Relation Classification Dataset with State-of-the-Art Evaluation\", \"authors\": \"Han, Xu and Zhu, Hao and Yu, Pengfei and Wang, Ziyun and Yao, Yuan and Liu, Zhiy...\", \"year\": \"2018\", \"venue\": \"Proceedings of the 2018 Conference on Empirical Methods in Natural Language Proc...\"}, {\"key\": \"maven-2020\", \"type\": \"inproceedings\", \"title\": \"MAVEN: A Massive General Domain Event Detection Dataset\", \"authors\": \"Wang, Xiaozhi and Wang, Ziqi and Han, Xu and Jiang, Wangyi and Han, Rong and Liu...\", \"year\": \"2020\", \"venue\": \"Proceedings of the 2020 Conference on Empirical Methods in Natural Language Proc...\"}, {\"key\": \"docred-2019\", \"type\": \"inproceedings\", \"title\": \"DocRED: A Large-Scale Document-Level Relation Extraction Dataset\", \"authors\": \"Yao, Yuan and Ye, Deming and Li, Peng and Han, Xu and Lin, Yankai and Liu, Zheng...\", \"year\": \"2019\", \"venue\": \"Proceedings of the 57th Annual Meeting of the Association for Computational Ling...\"}, {\"key\": \"qwen3-2025\", \"type\": \"article\", \"title\": \"Qwen3 Technical Report\", \"authors\": \"Qwen Team\", \"year\": \"2025\", \"venue\": \"arXiv preprint arXiv:2505.09388\"}, {\"key\": \"llama3-2024\", \"type\": \"article\", \"title\": \"The Llama 3 Herd of Models\", \"authors\": \"Dubey, Abhimanyu and Jauhri, Abhinav and Pandey, Abhinav and Kadian, Abhishek an...\", \"year\": \"2024\", \"venue\": \"arXiv preprint arXiv:2407.21783\"}, {\"key\": \"sentence-bert-2019\", \"type\": \"inproceedings\", \"title\": \"Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks\", \"authors\": \"Reimers, Nils and Gurevych, Iryna\", \"year\": \"2019\", \"venue\": \"Proceedings of the 2019 Conference on Empirical Methods in Natural Language Proc...\"}, {\"key\": \"minilm-2020\", \"type\": \"inproceedings\", \"title\": \"MiniLM: Deep Self-Attention Distillation for Task-Agnostic Compression of Pre-Trained Transformers\", \"authors\": \"Wang, Wenhui and Wei, Furu and Dong, Li and Bao, Hangbo and Yang, Nan and Zhou, ...\", \"year\": \"2020\", \"venue\": \"Advances in Neural Information Processing Systems\"}, {\"key\": \"reflect-learn-2026\", \"type\": \"inproceedings\", \"title\": \"Reflect then Learn: Active Prompting for Information Extraction Guided by Introspective Confusion\", \"authors\": \"Zhao, Dong and Wang, Yadong and Chen, Xiang and Wang, Chenxi and Dai, Hongliang ...\", \"year\": \"2026\", \"venue\": \"Proceedings of the AAAI Conference on Artificial Intelligence\"}, {\"key\": \"sclar-sensitivity-2024\", \"type\": \"inproceedings\", \"title\": \"Quantifying Language Models' Sensitivity to Spurious Features in Prompt Design\", \"authors\": \"Sclar, Melanie and Choi, Yejin and Tsvetkov, Yulia and Suhr, Alane\", \"year\": \"2024\", \"venue\": \"International Conference on Learning Representations\"}, {\"key\": \"vllm-2023\", \"type\": \"inproceedings\", \"title\": \"Efficient Memory Management for Large Language Model Serving with PagedAttention\", \"authors\": \"Kwon, Woosuk and Li, Zhuohan and Zhuang, Siyuan and Sheng, Ying and Zheng, Lianm...\", \"year\": \"2023\", \"venue\": \"Proceedings of the 29th Symposium on Operating Systems Principles\"}, {\"key\": \"xie-zeroshot-ner-2023\", \"type\": \"inproceedings\", \"title\": \"Empirical Study of Zero-Shot NER with ChatGPT\", \"authors\": \"Xie, Tingyu and Li, Qi and Zhang, Jian and Zhang, Yan and Liu, Zuozhu and Wang, ...\", \"year\": \"2023\", \"venue\": \"Proceedings of the 2023 Conference on Empirical Methods in Natural Language Proc...\"}, {\"key\": \"wadhwa-re-llm-2023\", \"type\": \"inproceedings\", \"title\": \"Revisiting Relation Extraction in the era of Large Language Models\", \"authors\": \"Wadhwa, Somin and Amir, Silvio and Wallace, Byron C.\", \"year\": \"2023\", \"venue\": \"Proceedings of the 61st Annual Meeting of the Association for Computational Ling...\"}, {\"key\": \"relationprompt-2022\", \"type\": \"inproceedings\", \"title\": \"RelationPrompt: Leveraging Prompts to Generate Synthetic Data for Zero-Shot Relation Triplet Extraction\", \"authors\": \"Chia, Yew Ken and Bing, Lidong and Poria, Soujanya and Si, Luo\", \"year\": \"2022\", \"venue\": \"Findings of the Association for Computational Linguistics: ACL 2022\"}, {\"key\": \"promptner-2023\", \"type\": \"article\", \"title\": \"PromptNER: Prompting For Named Entity Recognition\", \"authors\": \"Ashok, Dhananjay and Lipton, Zachary C.\", \"year\": \"2023\", \"venue\": \"arXiv preprint arXiv:2305.15444\"}, {\"key\": \"json-schema-bench-2025\", \"type\": \"article\", \"title\": \"JSONSchemaBench: A Rigorous Benchmark of Structured Outputs for Language Models\", \"authors\": \"Geng, Saibo and Cooper, Hudson and Moskal, Micha\\\\l and Jenkins, Samuel and Berma...\", \"year\": \"2025\", \"venue\": \"arXiv preprint arXiv:2501.10868\"}, {\"key\": \"rastogi2020towards\", \"type\": \"inproceedings\", \"title\": \"Towards Scalable Multi-Domain Conversational Agents: The Schema-Guided Dialogue Dataset\", \"authors\": \"Rastogi, Abhinav and Zang, Xiaoxue and Sunkara, Srinivas and Gupta, Raghav and K...\", \"year\": \"2020\", \"venue\": \"Proceedings of the AAAI Conference on Artificial Intelligence\"}, {\"key\": \"li2023evaluating\", \"type\": \"article\", \"title\": \"Evaluating ChatGPT's Information Extraction Capabilities: An Assessment of Performance, Explainability, Calibration, and...\", \"authors\": \"Li, Bo and Fang, Gexiang and Yang, Yang and Wang, Quansen and Ye, Wei and Zhao, ...\", \"year\": \"2023\", \"venue\": \"arXiv preprint arXiv:2304.11633\"}, {\"key\": \"lee2022sgd\", \"type\": \"inproceedings\", \"title\": \"SGD-X: A Benchmark for Robust Generalization in Schema-Guided Dialogue Systems\", \"authors\": \"Lee, Harrison and Gupta, Raghav and Rastogi, Abhinav and Cao, Yuan and Zhang, Bi...\", \"year\": \"2022\", \"venue\": \"Proceedings of the AAAI Conference on Artificial Intelligence\"}, {\"key\": \"volkanovska2025ner\", \"type\": \"article\", \"title\": \"A Study of Errors in the Output of Large Language Models for Domain-Specific Few-Shot Named Entity Recognition\", \"authors\": \"Volkanovska, Elena\", \"year\": \"2025\", \"venue\": \"Journal for Language Technology and Computational Linguistics\"}, {\"key\": \"haystack-to-needle-2025\", \"type\": \"article\", \"title\": \"From Haystack to Needle: Label Space Reduction for Zero-shot Classification\", \"authors\": \"Vandemoortele, Nathan and Steenwinckel, Bram and Ongenae, Femke and Van Hoecke, ...\", \"year\": \"2025\", \"venue\": \"arXiv preprint arXiv:2502.08436\"}, {\"key\": \"cohen-1988-power\", \"type\": \"book\", \"title\": \"Statistical Power Analysis for the Behavioral Sciences\", \"authors\": \"Cohen, Jacob\", \"year\": \"1988\", \"venue\": \"\"}, {\"key\": \"lakens-2013-effect-size\", \"type\": \"article\", \"title\": \"Calculating and Reporting Effect Sizes to Facilitate Cumulative Science: A Practical Primer for t-Tests and ANOVAs\", \"authors\": \"Lakens, Dani\\\\\\\"el\", \"year\": \"2013\", \"venue\": \"Frontiers in Psychology\"}, {\"key\": \"deng-2010-imagenet\", \"type\": \"inproceedings\", \"title\": \"What Does Classifying More Than 10,000 Image Categories Tell Us?\", \"authors\": \"Deng, Jia and Berg, Alexander C. and Li, Kai and Fei-Fei, Li\", \"year\": \"2010\", \"venue\": \"Proceedings of the 11th European Conference on Computer Vision\"}, {\"key\": \"rothman-1990\", \"type\": \"article\", \"title\": \"No Adjustments Are Needed for Multiple Comparisons\", \"authors\": \"Rothman, Kenneth J.\", \"year\": \"1990\", \"venue\": \"Epidemiology\"}, {\"key\": \"lakens-2017-equivalence\", \"type\": \"article\", \"title\": \"Equivalence Tests: A Practical Primer for t Tests, Correlations, and Meta-Analyses\", \"authors\": \"Lakens, Dani\\\\\\\"el\", \"year\": \"2017\", \"venue\": \"Social Psychological and Personality Science\"}, {\"key\": \"zhou-2025-rethinking\", \"type\": \"inproceedings\", \"title\": \"Rethinking Word Similarity: Semantic Similarity through Classification Confusion\", \"authors\": \"Zhou, Kaitlyn and Gao, Haishan and Chen, Sarah Li and Edelstein, Dan and Jurafsk...\", \"year\": \"2025\", \"venue\": \"Proceedings of the 2025 Conference of the North American Chapter of the Associat...\"}, {\"key\": \"guo-2021-label-confusion\", \"type\": \"inproceedings\", \"title\": \"Label Confusion Learning to Enhance Text Classification Models\", \"authors\": \"Guo, Biyang and Han, Songqiao and Han, Xiao and Huang, Hailiang and Lu, Ting\", \"year\": \"2021\", \"venue\": \"Proceedings of the AAAI Conference on Artificial Intelligence\"}, {\"key\": \"novack-2023-chils\", \"type\": \"inproceedings\", \"title\": \"CHiLS: Zero-Shot Image Classification with Hierarchical Label Sets\", \"authors\": \"Novack, Zachary and McAuley, Julian and Lipton, Zachary Chase and Garg, Saurabh\", \"year\": \"2023\", \"venue\": \"Proceedings of the 40th International Conference on Machine Learning\"}, {\"key\": \"cocchieri-2025-zeroner\", \"type\": \"inproceedings\", \"title\": \"ZeroNER: Fueling Zero-Shot Named Entity Recognition via Entity Type Descriptions\", \"authors\": \"Cocchieri, Alessio and Mart\\\\'\\\\inez Galindo, Marcos and Frisoni, Giacomo and Moro...\", \"year\": \"2025\", \"venue\": \"Findings of the Association for Computational Linguistics: ACL 2025\"}, {\"key\": \"dlisc-2025\", \"type\": \"article\", \"title\": \"Effective and Efficient Schema-aware Information Extraction Using On-Device Large Language Models\", \"authors\": \"Li, Zhuoqun and Wu, Hao and Li, Xinxin and Li, Zhoujun\", \"year\": \"2025\", \"venue\": \"arXiv preprint arXiv:2505.14992\"}, {\"key\": \"spt-2025\", \"type\": \"article\", \"title\": \"Schema as Parameterized Tools for Universal Information Extraction\", \"authors\": \"Liang, Sheng and Zhang, Yongyue and Wu, Yaxiong and Tang, Ruiming and Liu, Yong\", \"year\": \"2025\", \"venue\": \"arXiv preprint arXiv:2506.01276\"}, {\"key\": \"card-2020-power\", \"type\": \"inproceedings\", \"title\": \"With Little Power Comes Great Responsibility\", \"authors\": \"Card, Dallas and Henderson, Peter and Khandelwal, Urvashi and Jia, Robin and Mah...\", \"year\": \"2020\", \"venue\": \"Proceedings of the 2020 Conference on Empirical Methods in Natural Language Proc...\"}, {\"key\": \"gillick-2014-entity-typing\", \"type\": \"article\", \"title\": \"Context-Dependent Fine-Grained Entity Type Tagging\", \"authors\": \"Gillick, Daniel and Lazic, Nevena and Ganchev, Kuzman and Kirchner, Jesse and Hu...\", \"year\": \"2014\", \"venue\": \"arXiv preprint arXiv:1412.1820\"}, {\"key\": \"schall-2025-hidden-cost\", \"type\": \"inproceedings\", \"title\": \"The Hidden Cost of Structure: How Constrained Decoding Affects Language Model Performance\", \"authors\": \"Schall, Maximilian and de Melo, Gerard\", \"year\": \"2025\", \"venue\": \"Proceedings of the 15th International Conference on Recent Advances in Natural L...\"}, {\"key\": \"chen-2026-multi-instance\", \"type\": \"article\", \"title\": \"Understanding LLM Performance Degradation in Multi-Instance Processing: The Roles of Instance Count and Context Length\", \"authors\": \"Chen, Jingxuan and Pilehvar, Mohammad Taher and Camacho-Collados, Jose\", \"year\": \"2026\", \"venue\": \"arXiv preprint arXiv:2603.22608\"}, {\"key\": \"wei-2023-chatie\", \"type\": \"article\", \"title\": \"Zero-Shot Information Extraction via Chatting with ChatGPT\", \"authors\": \"Wei, Xiang and Cui, Xingyu and Cheng, Ning and Wang, Xiaobin and Zhang, Xin and ...\", \"year\": \"2023\", \"venue\": \"arXiv preprint arXiv:2302.10205\"}], \"tex_citations\": [{\"key\": \"llm4ie-survey-2024\", \"file\": \"introduction.tex\", \"line\": 4, \"command\": \"cite\"}, {\"key\": \"uniner-2024\", \"file\": \"introduction.tex\", \"line\": 6, \"command\": \"cite\"}, {\"key\": \"llm-pee-2025\", \"file\": \"introduction.tex\", \"line\": 6, \"command\": \"cite\"}, {\"key\": \"parse-2025\", \"file\": \"introduction.tex\", \"line\": 6, \"command\": \"cite\"}, {\"key\": \"fewnerd-2021\", \"file\": \"introduction.tex\", \"line\": 12, \"command\": \"cite\"}, {\"key\": \"fewrel-2018\", \"file\": \"introduction.tex\", \"line\": 12, \"command\": \"cite\"}, {\"key\": \"docred-2019\", \"file\": \"introduction.tex\", \"line\": 12, \"command\": \"cite\"}, {\"key\": \"maven-2020\", \"file\": \"introduction.tex\", \"line\": 12, \"command\": \"cite\"}, {\"key\": \"llm-pee-2025\", \"file\": \"introduction.tex\", \"line\": 22, \"command\": \"cite\"}, {\"key\": \"instructuie-2023\", \"file\": \"related_work.tex\", \"line\": 5, \"command\": \"cite\"}, {\"key\": \"knowcoder-2024\", \"file\": \"related_work.tex\", \"line\": 5, \"command\": \"cite\"}, {\"key\": \"codeie-2023\", \"file\": \"related_work.tex\", \"line\": 5, \"command\": \"cite\"}, {\"key\": \"gollie-2024\", \"file\": \"related_work.tex\", \"line\": 5, \"command\": \"cite\"}, {\"key\": \"adelie-2024\", \"file\": \"related_work.tex\", \"line\": 5, \"command\": \"cite\"}, {\"key\": \"slot-2025\", \"file\": \"related_work.tex\", \"line\": 5, \"command\": \"cite\"}, {\"key\": \"oneke-2025\", \"file\": \"related_work.tex\", \"line\": 5, \"command\": \"cite\"}, {\"key\": \"json-schema-bench-2025\", \"file\": \"related_work.tex\", \"line\": 5, \"command\": \"cite\"}, {\"key\": \"willard2023efficient\", \"file\": \"related_work.tex\", \"line\": 5, \"command\": \"cite\"}, {\"key\": \"xie-zeroshot-ner-2023\", \"file\": \"related_work.tex\", \"line\": 5, \"command\": \"cite\"}, {\"key\": \"promptner-2023\", \"file\": \"related_work.tex\", \"line\": 5, \"command\": \"cite\"}, {\"key\": \"uniner-2024\", \"file\": \"related_work.tex\", \"line\": 5, \"command\": \"cite\"}, {\"key\": \"gliner-2024\", \"file\": \"related_work.tex\", \"line\": 5, \"command\": \"cite\"}, {\"key\": \"gliner2-2025\", \"file\": \"related_work.tex\", \"line\": 5, \"command\": \"cite\"}, {\"key\": \"gillick-2014-entity-typing\", \"file\": \"related_work.tex\", \"line\": 5, \"command\": \"cite\"}, {\"key\": \"relationprompt-2022\", \"file\": \"related_work.tex\", \"line\": 5, \"command\": \"cite\"}, {\"key\": \"wadhwa-re-llm-2023\", \"file\": \"related_work.tex\", \"line\": 5, \"command\": \"cite\"}, {\"key\": \"wei-2023-chatie\", \"file\": \"related_work.tex\", \"line\": 5, \"command\": \"citet\"}, {\"key\": \"llm-pee-2025\", \"file\": \"related_work.tex\", \"line\": 8, \"command\": \"cite\"}, {\"key\": \"iepile-2024\", \"file\": \"related_work.tex\", \"line\": 8, \"command\": \"cite\"}, {\"key\": \"parse-2025\", \"file\": \"related_work.tex\", \"line\": 8, \"command\": \"cite\"}, {\"key\": \"crossagentie-2025\", \"file\": \"related_work.tex\", \"line\": 8, \"command\": \"cite\"}, {\"key\": \"cmas-ner-2025\", \"file\": \"related_work.tex\", \"line\": 8, \"command\": \"cite\"}, {\"key\": \"dee-2024\", \"file\": \"related_work.tex\", \"line\": 8, \"command\": \"cite\"}, {\"key\": \"reflect-learn-2026\", \"file\": \"related_work.tex\", \"line\": 8, \"command\": \"cite\"}, {\"key\": \"chen-2026-multi-instance\", \"file\": \"related_work.tex\", \"line\": 8, \"command\": \"citet\"}, {\"key\": \"haystack-to-needle-2025\", \"file\": \"related_work.tex\", \"line\": 8, \"command\": \"citet\"}, {\"key\": \"dlisc-2025\", \"file\": \"related_work.tex\", \"line\": 8, \"command\": \"citet\"}, {\"key\": \"spt-2025\", \"file\": \"related_work.tex\", \"line\": 8, \"command\": \"citet\"}, {\"key\": \"rastogi2020towards\", \"file\": \"related_work.tex\", \"line\": 10, \"command\": \"cite\"}, {\"key\": \"lee2022sgd\", \"file\": \"related_work.tex\", \"line\": 10, \"command\": \"cite\"}, {\"key\": \"li2023evaluating\", \"file\": \"related_work.tex\", \"line\": 10, \"command\": \"citet\"}, {\"key\": \"lu2022fantastically\", \"file\": \"related_work.tex\", \"line\": 10, \"command\": \"cite\"}, {\"key\": \"volkanovska2025ner\", \"file\": \"related_work.tex\", \"line\": 10, \"command\": \"citet\"}, {\"key\": \"deng-2010-imagenet\", \"file\": \"related_work.tex\", \"line\": 10, \"command\": \"citep\"}, {\"key\": \"guo-2021-label-confusion\", \"file\": \"related_work.tex\", \"line\": 10, \"command\": \"citep\"}, {\"key\": \"zhou-2025-rethinking\", \"file\": \"related_work.tex\", \"line\": 10, \"command\": \"citep\"}, {\"key\": \"muller2019when\", \"file\": \"related_work.tex\", \"line\": 10, \"command\": \"citep\"}, {\"key\": \"peterson2019human\", \"file\": \"related_work.tex\", \"line\": 10, \"command\": \"citep\"}, {\"key\": \"novack-2023-chils\", \"file\": \"related_work.tex\", \"line\": 10, \"command\": \"citep\"}, {\"key\": \"cocchieri-2025-zeroner\", \"file\": \"related_work.tex\", \"line\": 10, \"command\": \"citep\"}, {\"key\": \"yang2025beyond\", \"file\": \"related_work.tex\", \"line\": 10, \"command\": \"citep\"}, {\"key\": \"llm-pee-2025\", \"file\": \"related_work.tex\", \"line\": 12, \"command\": \"cite\"}, {\"key\": \"snell2017prototypical\", \"file\": \"related_work.tex\", \"line\": 12, \"command\": \"citep\"}, {\"key\": \"yin-2019-zero-shot-bench\", \"file\": \"related_work.tex\", \"line\": 12, \"command\": \"citep\"}, {\"key\": \"cohen-1988-power\", \"file\": \"related_work.tex\", \"line\": 12, \"command\": \"citep\"}, {\"key\": \"lakens-2013-effect-size\", \"file\": \"related_work.tex\", \"line\": 12, \"command\": \"citep\"}, {\"key\": \"gao-repr-degen-2019\", \"file\": \"related_work.tex\", \"line\": 12, \"command\": \"cite\"}, {\"key\": \"ethayarajh-contextual-2019\", \"file\": \"related_work.tex\", \"line\": 12, \"command\": \"cite\"}, {\"key\": \"cai-isotropy-clusters-2021\", \"file\": \"related_work.tex\", \"line\": 12, \"command\": \"cite\"}, {\"key\": \"fewnerd-2021\", \"file\": \"experimental_setup.tex\", \"line\": 10, \"command\": \"cite\"}, {\"key\": \"fewrel-2018\", \"file\": \"experimental_setup.tex\", \"line\": 13, \"command\": \"cite\"}, {\"key\": \"docred-2019\", \"file\": \"experimental_setup.tex\", \"line\": 16, \"command\": \"cite\"}, {\"key\": \"maven-2020\", \"file\": \"experimental_setup.tex\", \"line\": 19, \"command\": \"cite\"}, {\"key\": \"qwen3-2025\", \"file\": \"experimental_setup.tex\", \"line\": 56, \"command\": \"cite\"}, {\"key\": \"minilm-2020\", \"file\": \"experimental_setup.tex\", \"line\": 56, \"command\": \"cite\"}, {\"key\": \"sentence-bert-2019\", \"file\": \"experimental_setup.tex\", \"line\": 56, \"command\": \"cite\"}, {\"key\": \"sentence-bert-2019\", \"file\": \"experimental_setup.tex\", \"line\": 56, \"command\": \"cite\"}, {\"key\": \"ethayarajh-contextual-2019\", \"file\": \"experimental_setup.tex\", \"line\": 56, \"command\": \"cite\"}, {\"key\": \"qwen3-2025\", \"file\": \"experimental_setup.tex\", \"line\": 82, \"command\": \"cite\"}, {\"key\": \"vllm-2023\", \"file\": \"experimental_setup.tex\", \"line\": 82, \"command\": \"cite\"}, {\"key\": \"sclar-sensitivity-2024\", \"file\": \"experimental_setup.tex\", \"line\": 82, \"command\": \"cite\"}, {\"key\": \"llama3-2024\", \"file\": \"experimental_setup.tex\", \"line\": 82, \"command\": \"cite\"}, {\"key\": \"lost-in-middle-2024\", \"file\": \"results.tex\", \"line\": 49, \"command\": \"cite\"}, {\"key\": \"lakens-2017-equivalence\", \"file\": \"results.tex\", \"line\": 87, \"command\": \"citep\"}, {\"key\": \"schuirmann-1987-tost\", \"file\": \"results.tex\", \"line\": 87, \"command\": \"citep\"}, {\"key\": \"cai-isotropy-clusters-2021\", \"file\": \"results.tex\", \"line\": 92, \"command\": \"cite\"}, {\"key\": \"tam-2024-let-me-speak\", \"file\": \"discussion.tex\", \"line\": 11, \"command\": \"cite\"}, {\"key\": \"schall-2025-hidden-cost\", \"file\": \"discussion.tex\", \"line\": 11, \"command\": \"cite\"}, {\"key\": \"rothman-1990\", \"file\": \"main.tex\", \"line\": 51, \"command\": \"citep\"}, {\"key\": \"dror-2018-significance\", \"file\": \"main.tex\", \"line\": 51, \"command\": \"citep\"}, {\"key\": \"card-2020-power\", \"file\": \"main.tex\", \"line\": 51, \"command\": \"citep\"}, {\"key\": \"fewnerd-2021\", \"file\": \"checklist.tex\", \"line\": 33, \"command\": \"cite\"}, {\"key\": \"fewrel-2018\", \"file\": \"checklist.tex\", \"line\": 33, \"command\": \"cite\"}, {\"key\": \"docred-2019\", \"file\": \"checklist.tex\", \"line\": 33, \"command\": \"cite\"}, {\"key\": \"maven-2020\", \"file\": \"checklist.tex\", \"line\": 33, \"command\": \"cite\"}, {\"key\": \"qwen3-2025\", \"file\": \"checklist.tex\", \"line\": 33, \"command\": \"cite\"}, {\"key\": \"llama3-2024\", \"file\": \"checklist.tex\", \"line\": 33, \"command\": \"cite\"}, {\"key\": \"vllm-2023\", \"file\": \"checklist.tex\", \"line\": 33, \"command\": \"cite\"}, {\"key\": \"minilm-2020\", \"file\": \"checklist.tex\", \"line\": 33, \"command\": \"cite\"}, {\"key\": \"fewnerd-2021\", \"file\": \"prompt_appendix.tex\", \"line\": 204, \"command\": \"cite\"}, {\"key\": \"maven-2020\", \"file\": \"prompt_appendix.tex\", \"line\": 205, \"command\": \"cite\"}, {\"key\": \"fewrel-2018\", \"file\": \"prompt_appendix.tex\", \"line\": 206, \"command\": \"cite\"}, {\"key\": \"rothman-1990\", \"file\": \"main.tex\", \"line\": 321, \"command\": \"citep\"}, {\"key\": \"li2023evaluating\", \"file\": \"main.tex\", \"line\": 518, \"command\": \"citet\"}, {\"key\": \"gemini-2025\", \"file\": \"main.tex\", \"line\": 563, \"command\": \"citep\"}, {\"key\": \"lost-in-middle-2024\", \"file\": \"main.tex\", \"line\": 607, \"command\": \"cite\"}], \"online_verification\": [{\"key\": \"tam-2024-let-me-speak\", \"title\": \"Let Me Speak Freely? A Study on the Impact of Format Restrictions on Performance of Large Language Models\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Let Me Speak Freely? A Study on the Impact of Format Restrictions on Performance of Large Language Models\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"yin-2019-zero-shot-bench\", \"title\": \"Benchmarking Zero-shot Text Classification: Datasets, Evaluation and Entailment Approach\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Benchmarking Zero-shot Text Classification: Datasets, Evaluation and Entailment Approach\", \"matched_year\": \"2019\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"schuirmann-1987-tost\", \"title\": \"A Comparison of the Two One-Sided Tests Procedure and the Power Approach for Assessing the Equivalence of Average Bioavailability\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"A comparison of the Two One-Sided Tests Procedure and the Power Approach for assessing the equivalence of average bioavailability\", \"matched_year\": \"1987\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"gemini-2025\", \"title\": \"Gemini 2.5: Pushing the Frontier with Advanced Reasoning, Multimodality, and Long Context\", \"status\": \"not_found\", \"confidence\": 0.443, \"matched_title\": \"MM-LLMs: Recent Advances in MultiModal Large Language Models\", \"matched_year\": \"\", \"mismatch_fields\": [], \"note\": \"best match similarity 0.44 below threshold 0.82\"}, {\"key\": \"snell2017prototypical\", \"title\": \"Prototypical Networks for Few-shot Learning\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Prototypical Networks for Few-shot Learning\", \"matched_year\": \"2017\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"muller2019when\", \"title\": \"When Does Label Smoothing Help?\", \"status\": \"mismatch\", \"confidence\": 1.0, \"matched_title\": \"When Does Label Smoothing Help?\", \"matched_year\": \"2019\", \"mismatch_fields\": [\"first_author: bib=m\\\\\\\"uller vs api=müller\"], \"note\": \"\"}, {\"key\": \"peterson2019human\", \"title\": \"Human Uncertainty Makes Classification More Robust\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Human Uncertainty Makes Classification More Robust\", \"matched_year\": \"2019\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"jagannatha2020calibrating\", \"title\": \"Calibrating Structured Output Predictors for Natural Language Processing\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Calibrating Structured Output Predictors for Natural Language Processing\", \"matched_year\": \"2020\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"willard2023efficient\", \"title\": \"Efficient Guided Generation for Large Language Models\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Efficient Guided Generation for Large Language Models\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"lu2022fantastically\", \"title\": \"Fantastically Ordered Prompts and Where to Find Them: Overcoming Few-Shot Prompt Order Sensitivity\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Fantastically Ordered Prompts and Where to Find Them: Overcoming Few-Shot Prompt Order Sensitivity\", \"matched_year\": \"2022\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"yang2025beyond\", \"title\": \"Beyond Boundaries: Learning a Universal Entity Taxonomy across Datasets and Languages for Open Named Entity Recognition\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Beyond Boundaries: Learning a Universal Entity Taxonomy across Datasets and Languages for Open Named Entity Recognition\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"llm-pee-2025\", \"title\": \"Towards Event Extraction with Massive Types: LLM-based Collaborative Annotation and Partitioning Extraction\", \"status\": \"mismatch\", \"confidence\": 1.0, \"matched_title\": \"Towards Event Extraction with Massive Types: LLM-based Collaborative Annotation and Partitioning Extraction\", \"matched_year\": \"2025\", \"mismatch_fields\": [\"first_author: bib=liu vs api=2025\"], \"note\": \"\"}, {\"key\": \"parse-2025\", \"title\": \"PARSE: LLM Driven Schema Optimization for Reliable Entity Extraction\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"PARSE: LLM Driven Schema Optimization for Reliable Entity Extraction\", \"matched_year\": \"2025\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"dee-2024\", \"title\": \"Decompose, Enrich, and Extract! Schema-aware Event Extraction using LLMs\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Decompose, Enrich, and Extract! Schema-aware Event Extraction using LLMs\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"crossagentie-2025\", \"title\": \"CROSSAGENTIE: Cross-Type and Cross-Task Multi-Agent LLM Collaboration for Zero-Shot Information Extraction\", \"status\": \"mismatch\", \"confidence\": 1.0, \"matched_title\": \"CROSSAGENTIE: Cross-Type and Cross-Task Multi-Agent LLM Collaboration for Zero-Shot Information Extraction\", \"matched_year\": \"2025\", \"mismatch_fields\": [\"first_author: bib=lu vs api=meng\"], \"note\": \"\"}, {\"key\": \"cmas-ner-2025\", \"title\": \"A Cooperative Multi-Agent Framework for Zero-Shot Named Entity Recognition\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"A Cooperative Multi-Agent Framework for Zero-Shot Named Entity Recognition\", \"matched_year\": \"2025\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"uniner-2024\", \"title\": \"UniversalNER: Targeted Distillation from Large Language Models for Open Named Entity Recognition\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"UniversalNER: Targeted Distillation from Large Language Models for Open Named Entity Recognition\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"gollie-2024\", \"title\": \"GoLLIE: Annotation Guidelines improve Zero-Shot Information-Extraction\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"GoLLIE: Annotation Guidelines improve Zero-Shot Information-Extraction\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"gliner-2024\", \"title\": \"GLiNER: Generalist Model for Named Entity Recognition using Bidirectional Transformer\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"GLiNER: Generalist Model for Named Entity Recognition using Bidirectional Transformer\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"gliner2-2025\", \"title\": \"GLiNER2: Schema-Driven Multi-Task Learning for Structured Information Extraction\", \"status\": \"mismatch\", \"confidence\": 1.0, \"matched_title\": \"GLiNER2: Schema-Driven Multi-Task Learning for Structured Information Extraction\", \"matched_year\": \"2025\", \"mismatch_fields\": [\"first_author: bib=zaratiana vs api=2025\"], \"note\": \"\"}, {\"key\": \"iepile-2024\", \"title\": \"IEPile: Unearthing Large Scale Schema-Conditioned Information Extraction Corpus\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"IEPile: Unearthing Large Scale Schema-Conditioned Information Extraction Corpus\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"dror-2018-significance\", \"title\": \"The Hitchhiker's Guide to Testing Statistical Significance in Natural Language Processing\", \"status\": \"not_found\", \"confidence\": 0.339, \"matched_title\": \"The Sorcerer II Global Ocean Sampling Expedition: Northwest Atlantic through Eastern Tropical Pacific\", \"matched_year\": \"\", \"mismatch_fields\": [], \"note\": \"best match similarity 0.34 below threshold 0.82\"}, {\"key\": \"lost-in-middle-2024\", \"title\": \"Lost in the Middle: How Language Models Use Long Contexts\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Lost in the Middle: How Language Models Use Long Contexts\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"llm4ie-survey-2024\", \"title\": \"Large Language Models for Generative Information Extraction: A Survey\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Large language models for generative information extraction: a survey\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"knowcoder-2024\", \"title\": \"KnowCoder: Coding Structured Knowledge into LLMs for Universal Information Extraction\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"KnowCoder: Coding Structured Knowledge into LLMs for Universal Information Extraction\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"slot-2025\", \"title\": \"SLOT: Structuring the Output of Large Language Models\", \"status\": \"mismatch\", \"confidence\": 1.0, \"matched_title\": \"SLOT: Structuring the Output of Large Language Models\", \"matched_year\": \"2025\", \"mismatch_fields\": [\"first_author: bib=shen vs api=wang\"], \"note\": \"\"}, {\"key\": \"gao-repr-degen-2019\", \"title\": \"Representation Degeneration Problem in Training Natural Language Generation Models\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Representation Degeneration Problem in Training Natural Language Generation Models\", \"matched_year\": \"2019\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"ethayarajh-contextual-2019\", \"title\": \"How Contextual are Contextualized Word Representations? Comparing the Geometry of BERT, ELMo, and GPT-2 Embeddings\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"How Contextual are Contextualized Word Representations? Comparing the Geometry of BERT, ELMo, and GPT-2 Embeddings\", \"matched_year\": \"2019\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"cai-isotropy-clusters-2021\", \"title\": \"Isotropy in the Contextual Embedding Space: Clusters and Manifolds\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Isotropy in the Contextual Embedding Space: Clusters and Manifolds\", \"matched_year\": \"2021\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"instructuie-2023\", \"title\": \"InstructUIE: Multi-task Instruction Tuning for Unified Information Extraction\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"InstructUIE: Multi-task Instruction Tuning for Unified Information Extraction\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"codeie-2023\", \"title\": \"CodeIE: Large Code Generation Models are Better Few-Shot Information Extractors\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"CodeIE: Large Code Generation Models are Better Few-Shot Information Extractors\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"adelie-2024\", \"title\": \"ADELIE: Aligning Large Language Models on Information Extraction\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"ADELIE: Aligning Large Language Models on Information Extraction\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"oneke-2025\", \"title\": \"OneKE: A Dockerized Schema-Guided LLM Agent-based Knowledge Extraction System\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"OneKE: A Dockerized Schema-Guided LLM Agent-based Knowledge Extraction System\", \"matched_year\": \"2025\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"fewnerd-2021\", \"title\": \"Few-NERD: A Few-shot Named Entity Recognition Dataset\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Few-NERD: A Few-shot Named Entity Recognition Dataset\", \"matched_year\": \"2021\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"fewrel-2018\", \"title\": \"FewRel: A Large-Scale Supervised Few-Shot Relation Classification Dataset with State-of-the-Art Evaluation\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"FewRel: A Large-Scale Supervised Few-Shot Relation Classification Dataset with State-of-the-Art Evaluation\", \"matched_year\": \"2018\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"maven-2020\", \"title\": \"MAVEN: A Massive General Domain Event Detection Dataset\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"MAVEN: A Massive General Domain Event Detection Dataset\", \"matched_year\": \"2020\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"docred-2019\", \"title\": \"DocRED: A Large-Scale Document-Level Relation Extraction Dataset\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"DocRED: A Large-Scale Document-Level Relation Extraction Dataset\", \"matched_year\": \"2019\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"qwen3-2025\", \"title\": \"Qwen3 Technical Report\", \"status\": \"mismatch\", \"confidence\": 1.0, \"matched_title\": \"Qwen3 Technical Report\", \"matched_year\": \"2025\", \"mismatch_fields\": [\"first_author: bib=team vs api=yang\"], \"note\": \"\"}, {\"key\": \"llama3-2024\", \"title\": \"The Llama 3 Herd of Models\", \"status\": \"mismatch\", \"confidence\": 1.0, \"matched_title\": \"The Llama 3 herd of models\", \"matched_year\": \"2025\", \"mismatch_fields\": [\"first_author: bib=dubey vs api=aaron\"], \"note\": \"\"}, {\"key\": \"sentence-bert-2019\", \"title\": \"Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks\", \"matched_year\": \"2019\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"minilm-2020\", \"title\": \"MiniLM: Deep Self-Attention Distillation for Task-Agnostic Compression of Pre-Trained Transformers\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"MiniLM: Deep Self-Attention Distillation for Task-Agnostic Compression of Pre-Trained Transformers\", \"matched_year\": \"2020\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"reflect-learn-2026\", \"title\": \"Reflect then Learn: Active Prompting for Information Extraction Guided by Introspective Confusion\", \"status\": \"mismatch\", \"confidence\": 1.0, \"matched_title\": \"Reflect Then Learn: Active Prompting for Information Extraction Guided by Introspective Confusion\", \"matched_year\": \"2026\", \"mismatch_fields\": [\"first_author: bib=zhao vs api=2026\"], \"note\": \"\"}, {\"key\": \"sclar-sensitivity-2024\", \"title\": \"Quantifying Language Models' Sensitivity to Spurious Features in Prompt Design\", \"status\": \"not_found\", \"confidence\": 0.72, \"matched_title\": \"Quantifying Language Models' Sensitivity to Spurious Features in Prompt Design or: How I learned to start worrying about prompt formatting\", \"matched_year\": \"\", \"mismatch_fields\": [], \"note\": \"best match similarity 0.72 below threshold 0.82\"}, {\"key\": \"vllm-2023\", \"title\": \"Efficient Memory Management for Large Language Model Serving with PagedAttention\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Efficient Memory Management for Large Language Model Serving with PagedAttention\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"xie-zeroshot-ner-2023\", \"title\": \"Empirical Study of Zero-Shot NER with ChatGPT\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Empirical Study of Zero-Shot NER with ChatGPT\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"wadhwa-re-llm-2023\", \"title\": \"Revisiting Relation Extraction in the era of Large Language Models\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Revisiting Relation Extraction in the era of Large Language Models\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"relationprompt-2022\", \"title\": \"RelationPrompt: Leveraging Prompts to Generate Synthetic Data for Zero-Shot Relation Triplet Extraction\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"RelationPrompt: Leveraging Prompts to Generate Synthetic Data for Zero-Shot Relation Triplet Extraction\", \"matched_year\": \"2022\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"promptner-2023\", \"title\": \"PromptNER: Prompting For Named Entity Recognition\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"PromptNER: Prompting For Named Entity Recognition\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"json-schema-bench-2025\", \"title\": \"JSONSchemaBench: A Rigorous Benchmark of Structured Outputs for Language Models\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"JSONSchemaBench: A Rigorous Benchmark of Structured Outputs for Language Models\", \"matched_year\": \"2025\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"rastogi2020towards\", \"title\": \"Towards Scalable Multi-Domain Conversational Agents: The Schema-Guided Dialogue Dataset\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Towards Scalable Multi-Domain Conversational Agents: The Schema-Guided Dialogue Dataset\", \"matched_year\": \"2020\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"li2023evaluating\", \"title\": \"Evaluating ChatGPT's Information Extraction Capabilities: An Assessment of Performance, Explainability, Calibration, and Faithfulness\", \"status\": \"not_found\", \"confidence\": 0.333, \"matched_title\": \"Generative AI in Medical Practice: In-Depth Exploration of Privacy and Security Challenges\", \"matched_year\": \"\", \"mismatch_fields\": [], \"note\": \"best match similarity 0.33 below threshold 0.82\"}, {\"key\": \"lee2022sgd\", \"title\": \"SGD-X: A Benchmark for Robust Generalization in Schema-Guided Dialogue Systems\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"SGD-X: A Benchmark for Robust Generalization in Schema-Guided Dialogue Systems\", \"matched_year\": \"2022\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"volkanovska2025ner\", \"title\": \"A Study of Errors in the Output of Large Language Models for Domain-Specific Few-Shot Named Entity Recognition\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"A Study of Errors in the Output of Large Language Models for Domain-Specific Few-Shot Named Entity Recognition\", \"matched_year\": \"2025\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"haystack-to-needle-2025\", \"title\": \"From Haystack to Needle: Label Space Reduction for Zero-shot Classification\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"From Haystack to Needle: Label Space Reduction for Zero-shot Classification\", \"matched_year\": \"2025\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"cohen-1988-power\", \"title\": \"Statistical Power Analysis for the Behavioral Sciences\", \"status\": \"mismatch\", \"confidence\": 1.0, \"matched_title\": \"Statistical Power Analysis for the Behavioral Sciences\", \"matched_year\": \"1989\", \"mismatch_fields\": [\"first_author: bib=cohen vs api=muller\"], \"note\": \"\"}, {\"key\": \"lakens-2013-effect-size\", \"title\": \"Calculating and Reporting Effect Sizes to Facilitate Cumulative Science: A Practical Primer for t-Tests and ANOVAs\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Calculating and reporting effect sizes to facilitate cumulative science: a practical primer for t-tests and ANOVAs\", \"matched_year\": \"2013\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"deng-2010-imagenet\", \"title\": \"What Does Classifying More Than 10,000 Image Categories Tell Us?\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"What Does Classifying More Than 10,000 Image Categories Tell Us?\", \"matched_year\": \"2010\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"rothman-1990\", \"title\": \"No Adjustments Are Needed for Multiple Comparisons\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"No Adjustments Are Needed for Multiple Comparisons\", \"matched_year\": \"1990\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"lakens-2017-equivalence\", \"title\": \"Equivalence Tests: A Practical Primer for t Tests, Correlations, and Meta-Analyses\", \"status\": \"verified\", \"confidence\": 0.988, \"matched_title\": \"Equivalence Tests: A Practical Primer for t-Tests, Correlations, and Meta-Analyses\", \"matched_year\": \"2016\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"zhou-2025-rethinking\", \"title\": \"Rethinking Word Similarity: Semantic Similarity through Classification Confusion\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Rethinking Word Similarity: Semantic Similarity through Classification Confusion\", \"matched_year\": \"2025\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"guo-2021-label-confusion\", \"title\": \"Label Confusion Learning to Enhance Text Classification Models\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Label Confusion Learning to Enhance Text Classification Models\", \"matched_year\": \"2021\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"novack-2023-chils\", \"title\": \"CHiLS: Zero-Shot Image Classification with Hierarchical Label Sets\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"CHiLS: Zero-Shot Image Classification with Hierarchical Label Sets\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"cocchieri-2025-zeroner\", \"title\": \"ZeroNER: Fueling Zero-Shot Named Entity Recognition via Entity Type Descriptions\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"ZeroNER: Fueling Zero-Shot Named Entity Recognition via Entity Type Descriptions\", \"matched_year\": \"2025\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"dlisc-2025\", \"title\": \"Effective and Efficient Schema-aware Information Extraction Using On-Device Large Language Models\", \"status\": \"mismatch\", \"confidence\": 1.0, \"matched_title\": \"Effective and Efficient Schema-aware Information Extraction Using On-Device Large Language Models\", \"matched_year\": \"2025\", \"mismatch_fields\": [\"first_author: bib=li vs api=wen\"], \"note\": \"\"}, {\"key\": \"spt-2025\", \"title\": \"Schema as Parameterized Tools for Universal Information Extraction\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Schema as Parameterized Tools for Universal Information Extraction\", \"matched_year\": \"2025\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"card-2020-power\", \"title\": \"With Little Power Comes Great Responsibility\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"With Little Power Comes Great Responsibility\", \"matched_year\": \"2020\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"gillick-2014-entity-typing\", \"title\": \"Context-Dependent Fine-Grained Entity Type Tagging\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Context-Dependent Fine-Grained Entity Type Tagging\", \"matched_year\": \"2014\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"schall-2025-hidden-cost\", \"title\": \"The Hidden Cost of Structure: How Constrained Decoding Affects Language Model Performance\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"The Hidden Cost of Structure: How Constrained Decoding Affects Language Model Performance\", \"matched_year\": \"2025\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"chen-2026-multi-instance\", \"title\": \"Understanding LLM Performance Degradation in Multi-Instance Processing: The Roles of Instance Count and Context Length\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Understanding LLM Performance Degradation in Multi-Instance Processing: The Roles of Instance Count and Context Length\", \"matched_year\": \"2026\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"wei-2023-chatie\", \"title\": \"Zero-Shot Information Extraction via Chatting with ChatGPT\", \"status\": \"mismatch\", \"confidence\": 0.935, \"matched_title\": \"ChatIE: Zero-Shot Information Extraction via Chatting with ChatGPT\", \"matched_year\": \"2023\", \"mismatch_fields\": [\"first_author: bib=wei vs api=xiang\"], \"note\": \"\"}]}, \"error\": null, \"metadata\": {}}"
    }
  },
  "sourceToolAssistantUUID": "629febd3-b175-4d17-952f-757e06a0b404",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_reviewer_2_302b64f9",
  "sessionId": "0ff1fe81-4731-4c76-91b4-02652701ddff",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Tool result

_source line 54 · 2026-05-19T04:32:25.479Z_

<details><summary>↩ Tool result · `toolu_0137e4upPGPNVD2zX5Ja9z4Z`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/conclusion.tex:1:% DEPRECATED — this file is no longer included in main.tex.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9789ba4b-2879-443b-a258-c873bd1b9ee4",
  "isSidechain": false,
  "promptId": "8257bd0e-08b4-4530-aa87-1e185ea40a51",
  "type": "user",
  "uuid": "370b7d0e-f0ea-4924-afa0-0a68622af195",
  "toolUseResult": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/conclusion.tex:1:% DEPRECATED — this file is no longer included in main.tex.",
    "numLines": 1
  },
  "sourceToolAssistantUUID": "9789ba4b-2879-443b-a258-c873bd1b9ee4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_reviewer_2_302b64f9",
  "sessionId": "0ff1fe81-4731-4c76-91b4-02652701ddff",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Runtime record

_source line 55_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[Round 1 审稿请求]: ## Round 1 审稿任务 — Reviewer 2（新颖性 + Related Work 完整性 + 写作质量 + 格式合规）  ### Venue 信息 - **目标会议**: EMNLP 2026（通过 ARR May 2026 cycle 提交） - **截止日期**: 2026-05-25 - **页数限制**: Long paper, 正文 ≤ 8…",
  "leafUuid": "370b7d0e-f0ea-4924-afa0-0a68622af195",
  "sessionId": "0ff1fe81-4731-4c76-91b4-02652701ddff"
}
```

---


### Runtime record

_source line 56_

```json
{
  "type": "ai-title",
  "aiTitle": "Review Round 1 schema-dag-extraction paper for EMNLP 2026",
  "sessionId": "0ff1fe81-4731-4c76-91b4-02652701ddff"
}
```

---


### Tool result

_source line 57 · 2026-05-19T04:32:32.338Z_

<details><summary>↩ Tool result · `toolu_016WZuYKC7wJdPfvXA7vG3L7`</summary>

```text
Web search results for query: "schema decomposition LLM information extraction type confusability label similarity 2024 2025"

Links: [{"title":"PARSE: LLM Driven Schema Optimization for Reliable Entity Extraction","url":"https://arxiv.org/html/2510.08623v1"},{"title":"Schema-Driven Information Extraction from Heterogeneous Tables - ACL Anthology","url":"https://aclanthology.org/2024.findings-emnlp.600/"},{"title":"From LLMs to Knowledge Graphs: Building Production-Ready Graph Systems in 2025 | by Claudiu Branzan | Medium","url":"https://medium.com/@claudiubranzan/from-llms-to-knowledge-graphs-building-production-ready-graph-systems-in-2025-2b4aff1ec99a"},{"title":"Effective and Efficient Schema-aware Information Extraction Using On-Device Large Language Models","url":"https://arxiv.org/html/2505.14992v1"},{"title":"LLM-empowered knowledge graph construction: A survey","url":"https://arxiv.org/pdf/2510.20345"},{"title":"Schema-Driven Information Extraction from Heterogeneous Tables","url":"https://arxiv.org/pdf/2305.14336"},{"title":"ScrapeGraphAI-100k: A Large-Scale Dataset for LLM-Based Web Information Extraction","url":"https://arxiv.org/pdf/2602.15189"}]

I found several relevant research papers and resources related to your search query. Here's what the search returned:

## Key Findings:

**Schema Decomposition and Information Extraction:**

Recent research includes decomposing information extraction into subtasks—such as event extraction being decomposed into Event Detection and Event Argument Extraction, as well as Adaptive Schema-Aware Event Extraction (ASEE), which decomposes extraction into schema matching and schema-augmented extraction.

**LLM-Based Schema Optimization:**

LLMs struggle with complex schemas, with common error patterns including missing spans, incorrect types, and schema non-adherence, with GPT-4 showing an 11.97% invalid response rate for complex extraction tasks.

**Schema-Driven Information Extraction:**

Schema-driven information extraction is a task that transforms tabular data into structured records following a human-authored schema, evaluated across diverse domains including machine learning papers, chemistry literature, material science journals, and webpages.

**Label and Schema Similarity:**

Recent approaches like LKD-KGC introduced adaptive, embedding-based schema integration that automatically extracts and merges equivalent entity types via vector clustering and LLM-based deduplication.

The search results include recent papers from 2024-2025 covering schema optimization, information extraction challenges, and decomposition strategies for improving LLM-based extraction reliability.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ee15444a-0a62-4d21-9a44-4278fccccf36",
  "isSidechain": false,
  "promptId": "8257bd0e-08b4-4530-aa87-1e185ea40a51",
  "type": "user",
  "uuid": "b8f00907-e9df-49de-a05e-2ca8b1379b9b",
  "toolUseResult": {
    "query": "schema decomposition LLM information extraction type confusability label similarity 2024 2025",
    "results": [
      {
        "tool_use_id": "srvtoolu_01A1wkoh9wWAM5gjYuXRLTvC",
        "content": [
          {
            "title": "PARSE: LLM Driven Schema Optimization for Reliable Entity Extraction",
            "url": "https://arxiv.org/html/2510.08623v1"
          },
          {
            "title": "Schema-Driven Information Extraction from Heterogeneous Tables - ACL Anthology",
            "url": "https://aclanthology.org/2024.findings-emnlp.600/"
          },
          {
            "title": "From LLMs to Knowledge Graphs: Building Production-Ready Graph Systems in 2025 | by Claudiu Branzan | Medium",
            "url": "https://medium.com/@claudiubranzan/from-llms-to-knowledge-graphs-building-production-ready-graph-systems-in-2025-2b4aff1ec99a"
          },
          {
            "title": "Effective and Efficient Schema-aware Information Extraction Using On-Device Large Language Models",
            "url": "https://arxiv.org/html/2505.14992v1"
          },
          {
            "title": "LLM-empowered knowledge graph construction: A survey",
            "url": "https://arxiv.org/pdf/2510.20345"
          },
          {
            "title": "Schema-Driven Information Extraction from Heterogeneous Tables",
            "url": "https://arxiv.org/pdf/2305.14336"
          },
          {
            "title": "ScrapeGraphAI-100k: A Large-Scale Dataset for LLM-Based Web Information Extraction",
            "url": "https://arxiv.org/pdf/2602.15189"
          }
        ]
      },
      "I found several relevant research papers and resources related to your search query. Here's what the search returned:\n\n## Key Findings:\n\n**Schema Decomposition and Information Extraction:**\n\nRecent research includes decomposing information extraction into subtasks—such as event extraction being decomposed into Event Detection and Event Argument Extraction, as well as Adaptive Schema-Aware Event Extraction (ASEE), which decomposes extraction into schema matching and schema-augmented extraction.\n\n**LLM-Based Schema Optimization:**\n\nLLMs struggle with complex schemas, with common error patterns including missing spans, incorrect types, and schema non-adherence, with GPT-4 showing an 11.97% invalid response rate for complex extraction tasks.\n\n**Schema-Driven Information Extraction:**\n\nSchema-driven information extraction is a task that transforms tabular data into structured records following a human-authored schema, evaluated across diverse domains including machine learning papers, chemistry literature, material science journals, and webpages.\n\n**Label and Schema Similarity:**\n\nRecent approaches like LKD-KGC introduced adaptive, embedding-based schema integration that automatically extracts and merges equivalent entity types via vector clustering and LLM-based deduplication.\n\nThe search results include recent papers from 2024-2025 covering schema optimization, information extraction challenges, and decomposition strategies for improving LLM-based extraction reliability."
    ],
    "durationSeconds": 6.903128431999997
  },
  "sourceToolAssistantUUID": "ee15444a-0a62-4d21-9a44-4278fccccf36",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_reviewer_2_302b64f9",
  "sessionId": "0ff1fe81-4731-4c76-91b4-02652701ddff",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Tool result

_source line 58 · 2026-05-19T04:32:37.399Z_

<details><summary>↩ Tool result · `toolu_01Rn8d4rMm1mCyWCL4McmFF9`</summary>

```text
Web search results for query: "inter-class similarity confusion classification NLP label space 2024 2025"

Links: [{"title":"Semantic Similarity through Classification Confusion","url":"https://aclanthology.org/2025.naacl-long.299.pdf"},{"title":"Exploiting Class Similarity for Machine Learning with Confidence Labels   and Projective Loss Functions","url":"https://arxiv.org/pdf/2103.13607"},{"title":"Multi-Label Contrastive Learning : A Comprehensive Study","url":"https://arxiv.org/pdf/2412.00101"},{"title":"Pairwise Confusion for Fine-Grained Visual Classification","url":"https://arxiv.org/pdf/1705.08016"},{"title":"Label Confusion Learning to Enhance Text Classification Models","url":"https://arxiv.org/pdf/2012.04987"},{"title":"Improve Meta-learning for Few-Shot Text Classification ...","url":"https://aclanthology.org/2024.findings-emnlp.12.pdf"},{"title":"Rethinking Consistent Multi-Label Classification under ...","url":"https://arxiv.org/pdf/2510.04091"},{"title":"Rethinking Word Similarity: Semantic Similarity through Classification   Confusion","url":"https://arxiv.org/pdf/2502.05704"}]

I've found several relevant research papers on inter-class similarity, confusion in classification, and NLP label space from 2024-2025. Here are the key findings:

## Recent Research (2024-2025)

**Semantic Similarity through Classification Confusion**
A 2025 NAACL paper addresses semantic similarity through classification confusion, proposing a novel approach where a predetermined set of classes defines the similarity features used to describe the input word. The research notes that cosine similarity doesn't account for the multi-faceted nature of similarity nor align exactly with how humans perceive it.

**Text Classification and Label Confusion**
The label confusion problem refers to model difficulty in distinguishing between some labels. A Label Confusion Model has been proposed to enhance deep learning text classification models by learning label representations and calculating their semantic similarity with input text to estimate label dependency.

**Few-Shot Text Classification**
EMNLP 2024 research addresses improving meta-learning for few-shot text classification, where misclassification can occur when query samples are closest to prototypes of different classes due to intra-class differences and inter-class similarity.

**Class Similarity in Label Spaces**
Machine learning systems typically lack explicit supervision on inter-class similarity, but projective loss functions can preserve naturally occurring class similarity distributions while keeping similar classes closer together.

These papers address how inter-class similarity and label confusion affect NLP classification performance and propose various solutions through modified loss functions and similarity-aware learning approaches.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "14ada13f-70ad-4b0a-8c6d-a0d23b8e6b4c",
  "isSidechain": false,
  "promptId": "8257bd0e-08b4-4530-aa87-1e185ea40a51",
  "type": "user",
  "uuid": "b9926940-1eb4-41db-af0a-1404dec91049",
  "toolUseResult": {
    "query": "inter-class similarity confusion classification NLP label space 2024 2025",
    "results": [
      {
        "tool_use_id": "srvtoolu_01NNJ6JdPZ95V6tmT6mpBYxs",
        "content": [
          {
            "title": "Semantic Similarity through Classification Confusion",
            "url": "https://aclanthology.org/2025.naacl-long.299.pdf"
          },
          {
            "title": "Exploiting Class Similarity for Machine Learning with Confidence Labels   and Projective Loss Functions",
            "url": "https://arxiv.org/pdf/2103.13607"
          },
          {
            "title": "Multi-Label Contrastive Learning : A Comprehensive Study",
            "url": "https://arxiv.org/pdf/2412.00101"
          },
          {
            "title": "Pairwise Confusion for Fine-Grained Visual Classification",
            "url": "https://arxiv.org/pdf/1705.08016"
          },
          {
            "title": "Label Confusion Learning to Enhance Text Classification Models",
            "url": "https://arxiv.org/pdf/2012.04987"
          },
          {
            "title": "Improve Meta-learning for Few-Shot Text Classification ...",
            "url": "https://aclanthology.org/2024.findings-emnlp.12.pdf"
          },
          {
            "title": "Rethinking Consistent Multi-Label Classification under ...",
            "url": "https://arxiv.org/pdf/2510.04091"
          },
          {
            "title": "Rethinking Word Similarity: Semantic Similarity through Classification   Confusion",
            "url": "https://arxiv.org/pdf/2502.05704"
          }
        ]
      },
      "I've found several relevant research papers on inter-class similarity, confusion in classification, and NLP label space from 2024-2025. Here are the key findings:\n\n## Recent Research (2024-2025)\n\n**Semantic Similarity through Classification Confusion**\nA 2025 NAACL paper addresses semantic similarity through classification confusion, proposing a novel approach where a predetermined set of classes defines the similarity features used to describe the input word. The research notes that cosine similarity doesn't account for the multi-faceted nature of similarity nor align exactly with how humans perceive it.\n\n**Text Classification and Label Confusion**\nThe label confusion problem refers to model difficulty in distinguishing between some labels. A Label Confusion Model has been proposed to enhance deep learning text classification models by learning label representations and calculating their semantic similarity with input text to estimate label dependency.\n\n**Few-Shot Text Classification**\nEMNLP 2024 research addresses improving meta-learning for few-shot text classification, where misclassification can occur when query samples are closest to prototypes of different classes due to intra-class differences and inter-class similarity.\n\n**Class Similarity in Label Spaces**\nMachine learning systems typically lack explicit supervision on inter-class similarity, but projective loss functions can preserve naturally occurring class similarity distributions while keeping similar classes closer together.\n\nThese papers address how inter-class similarity and label confusion affect NLP classification performance and propose various solutions through modified loss functions and similarity-aware learning approaches."
    ],
    "durationSeconds": 11.962100324
  },
  "sourceToolAssistantUUID": "14ada13f-70ad-4b0a-8c6d-a0d23b8e6b4c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_reviewer_2_302b64f9",
  "sessionId": "0ff1fe81-4731-4c76-91b4-02652701ddff",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Assistant

_source line 59 · 2026-05-19T04:32:44.360Z_

<details><summary>Logged reasoning block</summary>

```text
Good. Let me now check a few more things:

1. The em-dash search found only one hit in a deprecated file - good, no AI-style dashes in the main paper.
2. Let me check for -ing phrases and other AI writing markers.
3. Let me read the full reference verification results.
4. Let me check page count.

Let me now compile all my findings into a comprehensive review.

Key findings so far:
- Reference verification: 70 bib entries, 69 cited, 1 orphan (jagannatha2020calibrating), 0 missing, 4 not found online, 11 mismatches


- No em-dash issues in the paper itself, only in deprecated files. Now I need to examine the full reference verification output and look for any other potential issues like -ing phrases or page count problems.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b9926940-1eb4-41db-af0a-1404dec91049",
  "isSidechain": false,
  "requestId": "req_011CbBJUHuzquDnpF8L3QWES",
  "type": "assistant",
  "uuid": "7bf66a4b-ef81-4904-8760-72ba9b949ea5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_reviewer_2_302b64f9",
  "sessionId": "0ff1fe81-4731-4c76-91b4-02652701ddff",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FRC8kBQtFBAvVSwr4XMw4W",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 82,
      "cache_creation_input_tokens": 3326,
      "cache_read_input_tokens": 83533,
      "output_tokens": 689,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3326,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 82,
          "output_tokens": 689,
          "cache_read_input_tokens": 83533,
          "cache_creation_input_tokens": 3326,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3326
          },
          "type": "message"
        }
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

_source line 60 · 2026-05-19T04:32:44.362Z_

检查 -ing 短语模式和页数。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7bf66a4b-ef81-4904-8760-72ba9b949ea5",
  "isSidechain": false,
  "requestId": "req_011CbBJUHuzquDnpF8L3QWES",
  "type": "assistant",
  "uuid": "3e488139-8f94-469c-9336-018e2c43aa67",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_reviewer_2_302b64f9",
  "sessionId": "0ff1fe81-4731-4c76-91b4-02652701ddff",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FRC8kBQtFBAvVSwr4XMw4W",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 82,
      "cache_creation_input_tokens": 3326,
      "cache_read_input_tokens": 83533,
      "output_tokens": 689,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3326,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 82,
          "output_tokens": 689,
          "cache_read_input_tokens": 83533,
          "cache_creation_input_tokens": 3326,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3326
          },
          "type": "message"
        }
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

_source line 61 · 2026-05-19T04:32:45.468Z_

<details open><summary>🔧 Tool call — Read · `toolu_01D6eenbCdqrfeMBCw35pLNL`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-18-projects-schema-dag-extraction--claude-sessions-review-reviewer-2-302b64f9/0ff1fe81-4731-4c76-91b4-02652701ddff/tool-results/toolu_01VZo7LNTXDQqfP3yD4gMWxh.txt",
  "offset": 0,
  "limit": 200
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3e488139-8f94-469c-9336-018e2c43aa67",
  "isSidechain": false,
  "requestId": "req_011CbBJUHuzquDnpF8L3QWES",
  "type": "assistant",
  "uuid": "bfab09a1-0481-45b8-8b5e-eaa3259b83af",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_reviewer_2_302b64f9",
  "sessionId": "0ff1fe81-4731-4c76-91b4-02652701ddff",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FRC8kBQtFBAvVSwr4XMw4W",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 82,
      "cache_creation_input_tokens": 3326,
      "cache_read_input_tokens": 83533,
      "output_tokens": 689,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3326,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 82,
          "output_tokens": 689,
          "cache_read_input_tokens": 83533,
          "cache_creation_input_tokens": 3326,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3326
          },
          "type": "message"
        }
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

_source line 62 · 2026-05-19T04:32:45.748Z_

<details><summary>↩ Tool result · `toolu_01D6eenbCdqrfeMBCw35pLNL`</summary>

```text
0	{"result":"{\"success\": true, \"data\": {\"summary\": {\"total_bib_entries\": 70, \"total_citations\": 96, \"unique_cited_keys\": 69, \"orphan_bib\": 1, \"missing_bib\": 0, \"duplicate_keys\": 0, \"online_verified\": 55, \"online_not_found\": 4, \"online_mismatch\": 11}, \"cross_check\": {\"orphan_bib\": [\"jagannatha2020calibrating\"], \"missing_bib\": [], \"orphan_count\": 1, \"missing_count\": 0}, \"bib_entries\": [{\"key\": \"tam-2024-let-me-speak\", \"type\": \"inproceedings\", \"title\": \"Let Me Speak Freely? A Study on the Impact of Format Restrictions on Performance of Large Language Models\", \"authors\": \"Tam, Zhi Rui and Wu, Cheng-Kuang and Tsai, Yi-Lin and Lin, Chieh-Yen and Lee, Hu...\", \"year\": \"2024\", \"venue\": \"Proceedings of the 2024 Conference on Empirical Methods in Natural Language Proc...\"}, {\"key\": \"yin-2019-zero-shot-bench\", \"type\": \"inproceedings\", \"title\": \"Benchmarking Zero-shot Text Classification: Datasets, Evaluation and Entailment Approach\", \"authors\": \"Yin, Wenpeng and Hay, Jamaal and Roth, Dan\", \"year\": \"2019\", \"venue\": \"Proceedings of the 2019 Conference on Empirical Methods in Natural Language Proc...\"}, {\"key\": \"schuirmann-1987-tost\", \"type\": \"article\", \"title\": \"A Comparison of the Two One-Sided Tests Procedure and the Power Approach for Assessing the Equivalence of Average Bioava...\", \"authors\": \"Schuirmann, Donald J.\", \"year\": \"1987\", \"venue\": \"Journal of Pharmacokinetics and Biopharmaceutics\"}, {\"key\": \"gemini-2025\", \"type\": \"article\", \"title\": \"Gemini 2.5: Pushing the Frontier with Advanced Reasoning, Multimodality, and Long Context\", \"authors\": \"Comanici, Gheorghe and others\", \"year\": \"2025\", \"venue\": \"arXiv preprint arXiv:2507.06261\"}, {\"key\": \"snell2017prototypical\", \"type\": \"inproceedings\", \"title\": \"Prototypical Networks for Few-shot Learning\", \"authors\": \"Snell, Jake and Swersky, Kevin and Zemel, Richard\", \"year\": \"2017\", \"venue\": \"Advances in Neural Information Processing Systems\"}, {\"key\": \"muller2019when\", \"type\": \"inproceedings\", \"title\": \"When Does Label Smoothing Help?\", \"authors\": \"M\\\\\\\"uller, Rafael and Kornblith, Simon and Hinton, Geoffrey E.\", \"year\": \"2019\", \"venue\": \"Advances in Neural Information Processing Systems\"}, {\"key\": \"peterson2019human\", \"type\": \"inproceedings\", \"title\": \"Human Uncertainty Makes Classification More Robust\", \"authors\": \"Peterson, Joshua C. and Battleday, Ruairidh M. and Griffiths, Thomas L. and Russ...\", \"year\": \"2019\", \"venue\": \"Proceedings of the IEEE/CVF International Conference on Computer Vision\"}, {\"key\": \"jagannatha2020calibrating\", \"type\": \"inproceedings\", \"title\": \"Calibrating Structured Output Predictors for Natural Language Processing\", \"authors\": \"Jagannatha, Abhyuday and Yu, Hong\", \"year\": \"2020\", \"venue\": \"Proceedings of the 58th Annual Meeting of the Association for Computational Ling...\"}, {\"key\": \"willard2023efficient\", \"type\": \"article\", \"title\": \"Efficient Guided Generation for Large Language Models\", \"authors\": \"Willard, Brandon T. and Louf, R\\\\'emi\", \"year\": \"2023\", \"venue\": \"arXiv preprint arXiv:2307.09702\"}, {\"key\": \"lu2022fantastically\", \"type\": \"inproceedings\", \"title\": \"Fantastically Ordered Prompts and Where to Find Them: Overcoming Few-Shot Prompt Order Sensitivity\", \"authors\": \"Lu, Yao and Bartolo, Max and Moore, Alastair and Riedel, Sebastian and Stenetorp...\", \"year\": \"2022\", \"venue\": \"Proceedings of the 60th Annual Meeting of the Association for Computational Ling...\"}, {\"key\": \"yang2025beyond\", \"type\": \"inproceedings\", \"title\": \"Beyond Boundaries: Learning a Universal Entity Taxonomy across Datasets and Languages for Open Named Entity Recognition\", \"authors\": \"Yang, Yuming and Zhao, Wantong and Huang, Caishuang and Ye, Junjie and Wang, Xia...\", \"year\": \"2025\", \"venue\": \"Proceedings of the 31st International Conference on Computational Linguistics\"}, {\"key\": \"llm-pee-2025\", \"type\": \"inproceedings\", \"title\": \"Towards Event Extraction with Massive Types: LLM-based Collaborative Annotation and Partitioning Extraction\", \"authors\": \"Liu, Wenxuan and Li, Zixuan and Bai, Long and Zuo, Yuxin and Xu, Daozhu and Jin,...\", \"year\": \"2025\", \"venue\": \"Proceedings of the 2025 Conference on Empirical Methods in Natural Language Proc...\"}, {\"key\": \"parse-2025\", \"type\": \"inproceedings\", \"title\": \"PARSE: LLM Driven Schema Optimization for Reliable Entity Extraction\", \"authors\": \"Shrimal, Anubhav and Jain, Aryan and Chowdhury, Soumyajit and Yenigalla, Promod\", \"year\": \"2025\", \"venue\": \"Proceedings of the 2025 Conference on Empirical Methods in Natural Language Proc...\"}, {\"key\": \"dee-2024\", \"type\": \"inproceedings\", \"title\": \"Decompose, Enrich, and Extract! Schema-aware Event Extraction using LLMs\", \"authors\": \"Shiri, Fatemeh and Nguyen, Van and Moghimifar, Farhad and Yoo, John and Haffari,...\", \"year\": \"2024\", \"venue\": \"Proceedings of the IEEE International Conference on Tools with Artificial Intell...\"}, {\"key\": \"crossagentie-2025\", \"type\": \"inproceedings\", \"title\": \"CROSSAGENTIE: Cross-Type and Cross-Task Multi-Agent LLM Collaboration for Zero-Shot Information Extraction\", \"authors\": \"Lu, Meng and Xie, Yuzhang and Bi, Zhenyu and Cao, Shuxiang and Wang, Xuan\", \"year\": \"2025\", \"venue\": \"Findings of the Association for Computational Linguistics: ACL 2025\"}, {\"key\": \"cmas-ner-2025\", \"type\": \"inproceedings\", \"title\": \"A Cooperative Multi-Agent Framework for Zero-Shot Named Entity Recognition\", \"authors\": \"Wang, Zihan and Zhao, Ziqi and Lyu, Yougang and Chen, Zhumin and de Rijke, Maart...\", \"year\": \"2025\", \"venue\": \"Proceedings of the ACM Web Conference 2025\"}, {\"key\": \"uniner-2024\", \"type\": \"inproceedings\", \"title\": \"UniversalNER: Targeted Distillation from Large Language Models for Open Named Entity Recognition\", \"authors\": \"Zhou, Wenxuan and Zhang, Sheng and Gu, Yu and Chen, Muhao and Poon, Hoifung\", \"year\": \"2024\", \"venue\": \"International Conference on Learning Representations\"}, {\"key\": \"gollie-2024\", \"type\": \"inproceedings\", \"title\": \"GoLLIE: Annotation Guidelines improve Zero-Shot Information-Extraction\", \"authors\": \"Sainz, Oscar and Garc\\\\'\\\\ia-Ferrero, Iker and Agerri, Rodrigo and Lopez de Lacall...\", \"year\": \"2024\", \"venue\": \"International Conference on Learning Representations\"}, {\"key\": \"gliner-2024\", \"type\": \"inproceedings\", \"title\": \"GLiNER: Generalist Model for Named Entity Recognition using Bidirectional Transformer\", \"authors\": \"Zaratiana, Urchade and Tomeh, Nadi and Holat, Pierre and Charnois, Thierry\", \"year\": \"2024\", \"venue\": \"Proceedings of the 2024 Conference of the North American Chapter of the Associat...\"}, {\"key\": \"gliner2-2025\", \"type\": \"inproceedings\", \"title\": \"GLiNER2: Schema-Driven Multi-Task Learning for Structured Information Extraction\", \"authors\": \"Zaratiana, Urchade and Pasternak, Gil and Boyd, Oliver and Hurn-Maloney, George ...\", \"year\": \"2025\", \"venue\": \"Proceedings of the 2025 Conference on Empirical Methods in Natural Language Proc...\"}, {\"key\": \"iepile-2024\", \"type\": \"inproceedings\", \"title\": \"IEPile: Unearthing Large Scale Schema-Conditioned Information Extraction Corpus\", \"authors\": \"Gui, Honghao and Yuan, Lin and Ye, Hongbin and Zhang, Ningyu and Sun, Mengshu an...\", \"year\": \"2024\", \"venue\": \"Proceedings of the 62nd Annual Meeting of the Association for Computational Ling...\"}, {\"key\": \"dror-2018-significance\", \"type\": \"inproceedings\", \"title\": \"The Hitchhiker's Guide to Testing Statistical Significance in Natural Language Processing\", \"authors\": \"Dror, Rotem and Baumer, Gili and Shlomov, Segev and Reichart, Roi\", \"year\": \"2018\", \"venue\": \"Proceedings of the 56th Annual Meeting of the Association for Computational Ling...\"}, {\"key\": \"lost-in-middle-2024\", \"type\": \"article\", \"title\": \"Lost in the Middle: How Language Models Use Long Contexts\", \"authors\": \"Liu, Nelson F. and Lin, Kevin and Hewitt, John and Paranjape, Ashwin and Bevilac...\", \"year\": \"2024\", \"venue\": \"Transactions of the Association for Computational Linguistics\"}, {\"key\": \"llm4ie-survey-2024\", \"type\": \"article\", \"title\": \"Large Language Models for Generative Information Extraction: A Survey\", \"authors\": \"Xu, Derong and Chen, Wei and Peng, Wenjun and Zhang, Chao and Xu, Tong and Zhao,...\", \"year\": \"2024\", \"venue\": \"Frontiers of Computer Science\"}, {\"key\": \"knowcoder-2024\", \"type\": \"inproceedings\", \"title\": \"KnowCoder: Coding Structured Knowledge into LLMs for Universal Information Extraction\", \"authors\": \"Li, Zixuan and Zeng, Yutao and Zuo, Yuxin and Ren, Weicheng and Liu, Wenxuan and...\", \"year\": \"2024\", \"venue\": \"Proceedings of the 62nd Annual Meeting of the Association for Computational Ling...\"}, {\"key\": \"slot-2025\", \"type\": \"inproceedings\", \"title\": \"SLOT: Structuring the Output of Large Language Models\", \"authors\": \"Shen, Zhengyuan and Wang, Darren Yow-Bang and Mishra, Soumya Smruti and Xu, Zhic...\", \"year\": \"2025\", \"venue\": \"Proceedings of the 2025 Conference on Empirical Methods in Natural Language Proc...\"}, {\"key\": \"gao-repr-degen-2019\", \"type\": \"inproceedings\", \"title\": \"Representation Degeneration Problem in Training Natural Language Generation Models\", \"authors\": \"Gao, Jun and He, Di and Tan, Xu and Qin, Tao and Wang, Liwei and Liu, Tie-Yan\", \"year\": \"2019\", \"venue\": \"International Conference on Learning Representations\"}, {\"key\": \"ethayarajh-contextual-2019\", \"type\": \"inproceedings\", \"title\": \"How Contextual are Contextualized Word Representations? Comparing the Geometry of BERT, ELMo, and GPT-2 Embeddings\", \"authors\": \"Ethayarajh, Kawin\", \"year\": \"2019\", \"venue\": \"Proceedings of the 2019 Conference on Empirical Methods in Natural Language Proc...\"}, {\"key\": \"cai-isotropy-clusters-2021\", \"type\": \"inproceedings\", \"title\": \"Isotropy in the Contextual Embedding Space: Clusters and Manifolds\", \"authors\": \"Cai, Xingyu and Huang, Jiaji and Bian, Yuchen and Church, Kenneth\", \"year\": \"2021\", \"venue\": \"International Conference on Learning Representations\"}, {\"key\": \"instructuie-2023\", \"type\": \"article\", \"title\": \"InstructUIE: Multi-task Instruction Tuning for Unified Information Extraction\", \"authors\": \"Wang, Xiao and Zhou, Weikang and Zu, Can and Xia, Han and Chen, Tianze and Zhang...\", \"year\": \"2023\", \"venue\": \"arXiv preprint arXiv:2304.08085\"}, {\"key\": \"codeie-2023\", \"type\": \"inproceedings\", \"title\": \"CodeIE: Large Code Generation Models are Better Few-Shot Information Extractors\", \"authors\": \"Li, Peng and Sun, Tianxiang and Tang, Qiong and Yan, Hang and Wu, Yuanbin and Hu...\", \"year\": \"2023\", \"venue\": \"Proceedings of the 61st Annual Meeting of the Association for Computational Ling...\"}, {\"key\": \"adelie-2024\", \"type\": \"inproceedings\", \"title\": \"ADELIE: Aligning Large Language Models on Information Extraction\", \"authors\": \"Qi, Yunjia and Peng, Hao and Wang, Xiaozhi and Xu, Bin and Hou, Lei and Li, Juan...\", \"year\": \"2024\", \"venue\": \"Proceedings of the 2024 Conference on Empirical Methods in Natural Language Proc...\"}, {\"key\": \"oneke-2025\", \"type\": \"inproceedings\", \"title\": \"OneKE: A Dockerized Schema-Guided LLM Agent-based Knowledge Extraction System\", \"authors\": \"Luo, Yujie and Ru, Xiangyuan and Liu, Kangwei and Yuan, Lin and Sun, Mengshu and...\", \"year\": \"2025\", \"venue\": \"Companion Proceedings of the ACM Web Conference 2025\"}, {\"key\": \"fewnerd-2021\", \"type\": \"inproceedings\", \"title\": \"Few-NERD: A Few-shot Named Entity Recognition Dataset\", \"authors\": \"Ding, Ning and Xu, Guangwei and Chen, Yulin and Wang, Xiaobin and Han, Xu and Xi...\", \"year\": \"2021\", \"venue\": \"Proceedings of the 59th Annual Meeting of the Association for Computational Ling...\"}, {\"key\": \"fewrel-2018\", \"type\": \"inproceedings\", \"title\": \"FewRel: A Large-Scale Supervised Few-Shot Relation Classification Dataset with State-of-the-Art Evaluation\", \"authors\": \"Han, Xu and Zhu, Hao and Yu, Pengfei and Wang, Ziyun and Yao, Yuan and Liu, Zhiy...\", \"year\": \"2018\", \"venue\": \"Proceedings of the 2018 Conference on Empirical Methods in Natural Language Proc...\"}, {\"key\": \"maven-2020\", \"type\": \"inproceedings\", \"title\": \"MAVEN: A Massive General Domain Event Detection Dataset\", \"authors\": \"Wang, Xiaozhi and Wang, Ziqi and Han, Xu and Jiang, Wangyi and Han, Rong and Liu...\", \"year\": \"2020\", \"venue\": \"Proceedings of the 2020 Conference on Empirical Methods in Natural Language Proc...\"}, {\"key\": \"docred-2019\", \"type\": \"inproceedings\", \"title\": \"DocRED: A Large-Scale Document-Level Relation Extraction Dataset\", \"authors\": \"Yao, Yuan and Ye, Deming and Li, Peng and Han, Xu and Lin, Yankai and Liu, Zheng...\", \"year\": \"2019\", \"venue\": \"Proceedings of the 57th Annual Meeting of the Association for Computational Ling...\"}, {\"key\": \"qwen3-2025\", \"type\": \"article\", \"title\": \"Qwen3 Technical Report\", \"authors\": \"Qwen Team\", \"year\": \"2025\", \"venue\": \"arXiv preprint arXiv:2505.09388\"}, {\"key\": \"llama3-2024\", \"type\": \"article\", \"title\": \"The Llama 3 Herd of Models\", \"authors\": \"Dubey, Abhimanyu and Jauhri, Abhinav and Pandey, Abhinav and Kadian, Abhishek an...\", \"year\": \"2024\", \"venue\": \"arXiv preprint arXiv:2407.21783\"}, {\"key\": \"sentence-bert-2019\", \"type\": \"inproceedings\", \"title\": \"Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks\", \"authors\": \"Reimers, Nils and Gurevych, Iryna\", \"year\": \"2019\", \"venue\": \"Proceedings of the 2019 Conference on Empirical Methods in Natural Language Proc...\"}, {\"key\": \"minilm-2020\", \"type\": \"inproceedings\", \"title\": \"MiniLM: Deep Self-Attention Distillation for Task-Agnostic Compression of Pre-Trained Transformers\", \"authors\": \"Wang, Wenhui and Wei, Furu and Dong, Li and Bao, Hangbo and Yang, Nan and Zhou, ...\", \"year\": \"2020\", \"venue\": \"Advances in Neural Information Processing Systems\"}, {\"key\": \"reflect-learn-2026\", \"type\": \"inproceedings\", \"title\": \"Reflect then Learn: Active Prompting for Information Extraction Guided by Introspective Confusion\", \"authors\": \"Zhao, Dong and Wang, Yadong and Chen, Xiang and Wang, Chenxi and Dai, Hongliang ...\", \"year\": \"2026\", \"venue\": \"Proceedings of the AAAI Conference on Artificial Intelligence\"}, {\"key\": \"sclar-sensitivity-2024\", \"type\": \"inproceedings\", \"title\": \"Quantifying Language Models' Sensitivity to Spurious Features in Prompt Design\", \"authors\": \"Sclar, Melanie and Choi, Yejin and Tsvetkov, Yulia and Suhr, Alane\", \"year\": \"2024\", \"venue\": \"International Conference on Learning Representations\"}, {\"key\": \"vllm-2023\", \"type\": \"inproceedings\", \"title\": \"Efficient Memory Management for Large Language Model Serving with PagedAttention\", \"authors\": \"Kwon, Woosuk and Li, Zhuohan and Zhuang, Siyuan and Sheng, Ying and Zheng, Lianm...\", \"year\": \"2023\", \"venue\": \"Proceedings of the 29th Symposium on Operating Systems Principles\"}, {\"key\": \"xie-zeroshot-ner-2023\", \"type\": \"inproceedings\", \"title\": \"Empirical Study of Zero-Shot NER with ChatGPT\", \"authors\": \"Xie, Tingyu and Li, Qi and Zhang, Jian and Zhang, Yan and Liu, Zuozhu and Wang, ...\", \"year\": \"2023\", \"venue\": \"Proceedings of the 2023 Conference on Empirical Methods in Natural Language Proc...\"}, {\"key\": \"wadhwa-re-llm-2023\", \"type\": \"inproceedings\", \"title\": \"Revisiting Relation Extraction in the era of Large Language Models\", \"authors\": \"Wadhwa, Somin and Amir, Silvio and Wallace, Byron C.\", \"year\": \"2023\", \"venue\": \"Proceedings of the 61st Annual Meeting of the Association for Computational Ling...\"}, {\"key\": \"relationprompt-2022\", \"type\": \"inproceedings\", \"title\": \"RelationPrompt: Leveraging Prompts to Generate Synthetic Data for Zero-Shot Relation Triplet Extraction\", \"authors\": \"Chia, Yew Ken and Bing, Lidong and Poria, Soujanya and Si, Luo\", \"year\": \"2022\", \"venue\": \"Findings of the Association for Computational Linguistics: ACL 2022\"}, {\"key\": \"promptner-2023\", \"type\": \"article\", \"title\": \"PromptNER: Prompting For Named Entity Recognition\", \"authors\": \"Ashok, Dhananjay and Lipton, Zachary C.\", \"year\": \"2023\", \"venue\": \"arXiv preprint arXiv:2305.15444\"}, {\"key\": \"json-schema-bench-2025\", \"type\": \"article\", \"title\": \"JSONSchemaBench: A Rigorous Benchmark of Structured Outputs for Language Models\", \"authors\": \"Geng, Saibo and Cooper, Hudson and Moskal, Micha\\\\l and Jenkins, Samuel and Berma...\", \"year\": \"2025\", \"venue\": \"arXiv preprint arXiv:2501.10868\"}, {\"key\": \"rastogi2020towards\", \"type\": \"inproceedings\", \"title\": \"Towards Scalable Multi-Domain Conversational Agents: The Schema-Guided Dialogue Dataset\", \"authors\": \"Rastogi, Abhinav and Zang, Xiaoxue and Sunkara, Srinivas and Gupta, Raghav and K...\", \"year\": \"2020\", \"venue\": \"Proceedings of the AAAI Conference on Artificial Intelligence\"}, {\"key\": \"li2023evaluating\", \"type\": \"article\", \"title\": \"Evaluating ChatGPT's Information Extraction Capabilities: An Assessment of Performance, Explainability, Calibration, and...\", \"authors\": \"Li, Bo and Fang, Gexiang and Yang, Yang and Wang, Quansen and Ye, Wei and Zhao, ...\", \"year\": \"2023\", \"venue\": \"arXiv preprint arXiv:2304.11633\"}, {\"key\": \"lee2022sgd\", \"type\": \"inproceedings\", \"title\": \"SGD-X: A Benchmark for Robust Generalization in Schema-Guided Dialogue Systems\", \"authors\": \"Lee, Harrison and Gupta, Raghav and Rastogi, Abhinav and Cao, Yuan and Zhang, Bi...\", \"year\": \"2022\", \"venue\": \"Proceedings of the AAAI Conference on Artificial Intelligence\"}, {\"key\": \"volkanovska2025ner\", \"type\": \"article\", \"title\": \"A Study of Errors in the Output of Large Language Models for Domain-Specific Few-Shot Named Entity Recognition\", \"authors\": \"Volkanovska, Elena\", \"year\": \"2025\", \"venue\": \"Journal for Language Technology and Computational Linguistics\"}, {\"key\": \"haystack-to-needle-2025\", \"type\": \"article\", \"title\": \"From Haystack to Needle: Label Space Reduction for Zero-shot Classification\", \"authors\": \"Vandemoortele, Nathan and Steenwinckel, Bram and Ongenae, Femke and Van Hoecke, ...\", \"year\": \"2025\", \"venue\": \"arXiv preprint arXiv:2502.08436\"}, {\"key\": \"cohen-1988-power\", \"type\": \"book\", \"title\": \"Statistical Power Analysis for the Behavioral Sciences\", \"authors\": \"Cohen, Jacob\", \"year\": \"1988\", \"venue\": \"\"}, {\"key\": \"lakens-2013-effect-size\", \"type\": \"article\", \"title\": \"Calculating and Reporting Effect Sizes to Facilitate Cumulative Science: A Practical Primer for t-Tests and ANOVAs\", \"authors\": \"Lakens, Dani\\\\\\\"el\", \"year\": \"2013\", \"venue\": \"Frontiers in Psychology\"}, {\"key\": \"deng-2010-imagenet\", \"type\": \"inproceedings\", \"title\": \"What Does Classifying More Than 10,000 Image Categories Tell Us?\", \"authors\": \"Deng, Jia and Berg, Alexander C. and Li, Kai and Fei-Fei, Li\", \"year\": \"2010\", \"venue\": \"Proceedings of the 11th European Conference on Computer Vision\"}, {\"key\": \"rothman-1990\", \"type\": \"article\", \"title\": \"No Adjustments Are Needed for Multiple Comparisons\", \"authors\": \"Rothman, Kenneth J.\", \"year\": \"1990\", \"venue\": \"Epidemiology\"}, {\"key\": \"lakens-2017-equivalence\", \"type\": \"article\", \"title\": \"Equivalence Tests: A Practical Primer for t Tests, Correlations, and Meta-Analyses\", \"authors\": \"Lakens, Dani\\\\\\\"el\", \"year\": \"2017\", \"venue\": \"Social Psychological and Personality Science\"}, {\"key\": \"zhou-2025-rethinking\", \"type\": \"inproceedings\", \"title\": \"Rethinking Word Similarity: Semantic Similarity through Classification Confusion\", \"authors\": \"Zhou, Kaitlyn and Gao, Haishan and Chen, Sarah Li and Edelstein, Dan and Jurafsk...\", \"year\": \"2025\", \"venue\": \"Proceedings of the 2025 Conference of the North American Chapter of the Associat...\"}, {\"key\": \"guo-2021-label-confusion\", \"type\": \"inproceedings\", \"title\": \"Label Confusion Learning to Enhance Text Classification Models\", \"authors\": \"Guo, Biyang and Han, Songqiao and Han, Xiao and Huang, Hailiang and Lu, Ting\", \"year\": \"2021\", \"venue\": \"Proceedings of the AAAI Conference on Artificial Intelligence\"}, {\"key\": \"novack-2023-chils\", \"type\": \"inproceedings\", \"title\": \"CHiLS: Zero-Shot Image Classification with Hierarchical Label Sets\", \"authors\": \"Novack, Zachary and McAuley, Julian and Lipton, Zachary Chase and Garg, Saurabh\", \"year\": \"2023\", \"venue\": \"Proceedings of the 40th International Conference on Machine Learning\"}, {\"key\": \"cocchieri-2025-zeroner\", \"type\": \"inproceedings\", \"title\": \"ZeroNER: Fueling Zero-Shot Named Entity Recognition via Entity Type Descriptions\", \"authors\": \"Cocchieri, Alessio and Mart\\\\'\\\\inez Galindo, Marcos and Frisoni, Giacomo and Moro...\", \"year\": \"2025\", \"venue\": \"Findings of the Association for Computational Linguistics: ACL 2025\"}, {\"key\": \"dlisc-2025\", \"type\": \"article\", \"title\": \"Effective and Efficient Schema-aware Information Extraction Using On-Device Large Language Models\", \"authors\": \"Li, Zhuoqun and Wu, Hao and Li, Xinxin and Li, Zhoujun\", \"year\": \"2025\", \"venue\": \"arXiv preprint arXiv:2505.14992\"}, {\"key\": \"spt-2025\", \"type\": \"article\", \"title\": \"Schema as Parameterized Tools for Universal Information Extraction\", \"authors\": \"Liang, Sheng and Zhang, Yongyue and Wu, Yaxiong and Tang, Ruiming and Liu, Yong\", \"year\": \"2025\", \"venue\": \"arXiv preprint arXiv:2506.01276\"}, {\"key\": \"card-2020-power\", \"type\": \"inproceedings\", \"title\": \"With Little Power Comes Great Responsibility\", \"authors\": \"Card, Dallas and Henderson, Peter and Khandelwal, Urvashi and Jia, Robin and Mah...\", \"year\": \"2020\", \"venue\": \"Proceedings of the 2020 Conference on Empirical Methods in Natural Language Proc...\"}, {\"key\": \"gillick-2014-entity-typing\", \"type\": \"article\", \"title\": \"Context-Dependent Fine-Grained Entity Type Tagging\", \"authors\": \"Gillick, Daniel and Lazic, Nevena and Ganchev, Kuzman and Kirchner, Jesse and Hu...\", \"year\": \"2014\", \"venue\": \"arXiv preprint arXiv:1412.1820\"}, {\"key\": \"schall-2025-hidden-cost\", \"type\": \"inproceedings\", \"title\": \"The Hidden Cost of Structure: How Constrained Decoding Affects Language Model Performance\", \"authors\": \"Schall, Maximilian and de Melo, Gerard\", \"year\": \"2025\", \"venue\": \"Proceedings of the 15th International Conference on Recent Advances in Natural L...\"}, {\"key\": \"chen-2026-multi-instance\", \"type\": \"article\", \"title\": \"Understanding LLM Performance Degradation in Multi-Instance Processing: The Roles of Instance Count and Context Length\", \"authors\": \"Chen, Jingxuan and Pilehvar, Mohammad Taher and Camacho-Collados, Jose\", \"year\": \"2026\", \"venue\": \"arXiv preprint arXiv:2603.22608\"}, {\"key\": \"wei-2023-chatie\", \"type\": \"article\", \"title\": \"Zero-Shot Information Extraction via Chatting with ChatGPT\", \"authors\": \"Wei, Xiang and Cui, Xingyu and Cheng, Ning and Wang, Xiaobin and Zhang, Xin and ...\", \"year\": \"2023\", \"venue\": \"arXiv preprint arXiv:2302.10205\"}], \"tex_citations\": [{\"key\": \"llm4ie-survey-2024\", \"file\": \"introduction.tex\", \"line\": 4, \"command\": \"cite\"}, {\"key\": \"uniner-2024\", \"file\": \"introduction.tex\", \"line\": 6, \"command\": \"cite\"}, {\"key\": \"llm-pee-2025\", \"file\": \"introduction.tex\", \"line\": 6, \"command\": \"cite\"}, {\"key\": \"parse-2025\", \"file\": \"introduction.tex\", \"line\": 6, \"command\": \"cite\"}, {\"key\": \"fewnerd-2021\", \"file\": \"introduction.tex\", \"line\": 12, \"command\": \"cite\"}, {\"key\": \"fewrel-2018\", \"file\": \"introduction.tex\", \"line\": 12, \"command\": \"cite\"}, {\"key\": \"docred-2019\", \"file\": \"introduction.tex\", \"line\": 12, \"command\": \"cite\"}, {\"key\": \"maven-2020\", \"file\": \"introduction.tex\", \"line\": 12, \"command\": \"cite\"}, {\"key\": \"llm-pee-2025\", \"file\": \"introduction.tex\", \"line\": 22, \"command\": \"cite\"}, {\"key\": \"instructuie-2023\", \"file\": \"related_work.tex\", \"line\": 5, \"command\": \"cite\"}, {\"key\": \"knowcoder-2024\", \"file\": \"related_work.tex\", \"line\": 5, \"command\": \"cite\"}, {\"key\": \"codeie-2023\", \"file\": \"related_work.tex\", \"line\": 5, \"command\": \"cite\"}, {\"key\": \"gollie-2024\", \"file\": \"related_work.tex\", \"line\": 5, \"command\": \"cite\"}, {\"key\": \"adelie-2024\", \"file\": \"related_work.tex\", \"line\": 5, \"command\": \"cite\"}, {\"key\": \"slot-2025\", \"file\": \"related_work.tex\", \"line\": 5, \"command\": \"cite\"}, {\"key\": \"oneke-2025\", \"file\": \"related_work.tex\", \"line\": 5, \"command\": \"cite\"}, {\"key\": \"json-schema-bench-2025\", \"file\": \"related_work.tex\", \"line\": 5, \"command\": \"cite\"}, {\"key\": \"willard2023efficient\", \"file\": \"related_work.tex\", \"line\": 5, \"command\": \"cite\"}, {\"key\": \"xie-zeroshot-ner-2023\", \"file\": \"related_work.tex\", \"line\": 5, \"command\": \"cite\"}, {\"key\": \"promptner-2023\", \"file\": \"related_work.tex\", \"line\": 5, \"command\": \"cite\"}, {\"key\": \"uniner-2024\", \"file\": \"related_work.tex\", \"line\": 5, \"command\": \"cite\"}, {\"key\": \"gliner-2024\", \"file\": \"related_work.tex\", \"line\": 5, \"command\": \"cite\"}, {\"key\": \"gliner2-2025\", \"file\": \"related_work.tex\", \"line\": 5, \"command\": \"cite\"}, {\"key\": \"gillick-2014-entity-typing\", \"file\": \"related_work.tex\", \"line\": 5, \"command\": \"cite\"}, {\"key\": \"relationprompt-2022\", \"file\": \"related_work.tex\", \"line\": 5, \"command\": \"cite\"}, {\"key\": \"wadhwa-re-llm-2023\", \"file\": \"related_work.tex\", \"line\": 5, \"command\": \"cite\"}, {\"key\": \"wei-2023-chatie\", \"file\": \"related_work.tex\", \"line\": 5, \"command\": \"citet\"}, {\"key\": \"llm-pee-2025\", \"file\": \"related_work.tex\", \"line\": 8, \"command\": \"cite\"}, {\"key\": \"iepile-2024\", \"file\": \"related_work.tex\", \"line\": 8, \"command\": \"cite\"}, {\"key\": \"parse-2025\", \"file\": \"related_work.tex\", \"line\": 8, \"command\": \"cite\"}, {\"key\": \"crossagentie-2025\", \"file\": \"related_work.tex\", \"line\": 8, \"command\": \"cite\"}, {\"key\": \"cmas-ner-2025\", \"file\": \"related_work.tex\", \"line\": 8, \"command\": \"cite\"}, {\"key\": \"dee-2024\", \"file\": \"related_work.tex\", \"line\": 8, \"command\": \"cite\"}, {\"key\": \"reflect-learn-2026\", \"file\": \"related_work.tex\", \"line\": 8, \"command\": \"cite\"}, {\"key\": \"chen-2026-multi-instance\", \"file\": \"related_work.tex\", \"line\": 8, \"command\": \"citet\"}, {\"key\": \"haystack-to-needle-2025\", \"file\": \"related_work.tex\", \"line\": 8, \"command\": \"citet\"}, {\"key\": \"dlisc-2025\", \"file\": \"related_work.tex\", \"line\": 8, \"command\": \"citet\"}, {\"key\": \"spt-2025\", \"file\": \"related_work.tex\", \"line\": 8, \"command\": \"citet\"}, {\"key\": \"rastogi2020towards\", \"file\": \"related_work.tex\", \"line\": 10, \"command\": \"cite\"}, {\"key\": \"lee2022sgd\", \"file\": \"related_work.tex\", \"line\": 10, \"command\": \"cite\"}, {\"key\": \"li2023evaluating\", \"file\": \"related_work.tex\", \"line\": 10, \"command\": \"citet\"}, {\"key\": \"lu2022fantastically\", \"file\": \"related_work.tex\", \"line\": 10, \"command\": \"cite\"}, {\"key\": \"volkanovska2025ner\", \"file\": \"related_work.tex\", \"line\": 10, \"command\": \"citet\"}, {\"key\": \"deng-2010-imagenet\", \"file\": \"related_work.tex\", \"line\": 10, \"command\": \"citep\"}, {\"key\": \"guo-2021-label-confusion\", \"file\": \"related_work.tex\", \"line\": 10, \"command\": \"citep\"}, {\"key\": \"zhou-2025-rethinking\", \"file\": \"related_work.tex\", \"line\": 10, \"command\": \"citep\"}, {\"key\": \"muller2019when\", \"file\": \"related_work.tex\", \"line\": 10, \"command\": \"citep\"}, {\"key\": \"peterson2019human\", \"file\": \"related_work.tex\", \"line\": 10, \"command\": \"citep\"}, {\"key\": \"novack-2023-chils\", \"file\": \"related_work.tex\", \"line\": 10, \"command\": \"citep\"}, {\"key\": \"cocchieri-2025-zeroner\", \"file\": \"related_work.tex\", \"line\": 10, \"command\": \"citep\"}, {\"key\": \"yang2025beyond\", \"file\": \"related_work.tex\", \"line\": 10, \"command\": \"citep\"}, {\"key\": \"llm-pee-2025\", \"file\": \"related_work.tex\", \"line\": 12, \"command\": \"cite\"}, {\"key\": \"snell2017prototypical\", \"file\": \"related_work.tex\", \"line\": 12, \"command\": \"citep\"}, {\"key\": \"yin-2019-zero-shot-bench\", \"file\": \"related_work.tex\", \"line\": 12, \"command\": \"citep\"}, {\"key\": \"cohen-1988-power\", \"file\": \"related_work.tex\", \"line\": 12, \"command\": \"citep\"}, {\"key\": \"lakens-2013-effect-size\", \"file\": \"related_work.tex\", \"line\": 12, \"command\": \"citep\"}, {\"key\": \"gao-repr-degen-2019\", \"file\": \"related_work.tex\", \"line\": 12, \"command\": \"cite\"}, {\"key\": \"ethayarajh-contextual-2019\", \"file\": \"related_work.tex\", \"line\": 12, \"command\": \"cite\"}, {\"key\": \"cai-isotropy-clusters-2021\", \"file\": \"related_work.tex\", \"line\": 12, \"command\": \"cite\"}, {\"key\": \"fewnerd-2021\", \"file\": \"experimental_setup.tex\", \"line\": 10, \"command\": \"cite\"}, {\"key\": \"fewrel-2018\", \"file\": \"experimental_setup.tex\", \"line\": 13, \"command\": \"cite\"}, {\"key\": \"docred-2019\", \"file\": \"experimental_setup.tex\", \"line\": 16, \"command\": \"cite\"}, {\"key\": \"maven-2020\", \"file\": \"experimental_setup.tex\", \"line\": 19, \"command\": \"cite\"}, {\"key\": \"qwen3-2025\", \"file\": \"experimental_setup.tex\", \"line\": 56, \"command\": \"cite\"}, {\"key\": \"minilm-2020\", \"file\": \"experimental_setup.tex\", \"line\": 56, \"command\": \"cite\"}, {\"key\": \"sentence-bert-2019\", \"file\": \"experimental_setup.tex\", \"line\": 56, \"command\": \"cite\"}, {\"key\": \"sentence-bert-2019\", \"file\": \"experimental_setup.tex\", \"line\": 56, \"command\": \"cite\"}, {\"key\": \"ethayarajh-contextual-2019\", \"file\": \"experimental_setup.tex\", \"line\": 56, \"command\": \"cite\"}, {\"key\": \"qwen3-2025\", \"file\": \"experimental_setup.tex\", \"line\": 82, \"command\": \"cite\"}, {\"key\": \"vllm-2023\", \"file\": \"experimental_setup.tex\", \"line\": 82, \"command\": \"cite\"}, {\"key\": \"sclar-sensitivity-2024\", \"file\": \"experimental_setup.tex\", \"line\": 82, \"command\": \"cite\"}, {\"key\": \"llama3-2024\", \"file\": \"experimental_setup.tex\", \"line\": 82, \"command\": \"cite\"}, {\"key\": \"lost-in-middle-2024\", \"file\": \"results.tex\", \"line\": 49, \"command\": \"cite\"}, {\"key\": \"lakens-2017-equivalence\", \"file\": \"results.tex\", \"line\": 87, \"command\": \"citep\"}, {\"key\": \"schuirmann-1987-tost\", \"file\": \"results.tex\", \"line\": 87, \"command\": \"citep\"}, {\"key\": \"cai-isotropy-clusters-2021\", \"file\": \"results.tex\", \"line\": 92, \"command\": \"cite\"}, {\"key\": \"tam-2024-let-me-speak\", \"file\": \"discussion.tex\", \"line\": 11, \"command\": \"cite\"}, {\"key\": \"schall-2025-hidden-cost\", \"file\": \"discussion.tex\", \"line\": 11, \"command\": \"cite\"}, {\"key\": \"rothman-1990\", \"file\": \"main.tex\", \"line\": 51, \"command\": \"citep\"}, {\"key\": \"dror-2018-significance\", \"file\": \"main.tex\", \"line\": 51, \"command\": \"citep\"}, {\"key\": \"card-2020-power\", \"file\": \"main.tex\", \"line\": 51, \"command\": \"citep\"}, {\"key\": \"fewnerd-2021\", \"file\": \"checklist.tex\", \"line\": 33, \"command\": \"cite\"}, {\"key\": \"fewrel-2018\", \"file\": \"checklist.tex\", \"line\": 33, \"command\": \"cite\"}, {\"key\": \"docred-2019\", \"file\": \"checklist.tex\", \"line\": 33, \"command\": \"cite\"}, {\"key\": \"maven-2020\", \"file\": \"checklist.tex\", \"line\": 33, \"command\": \"cite\"}, {\"key\": \"qwen3-2025\", \"file\": \"checklist.tex\", \"line\": 33, \"command\": \"cite\"}, {\"key\": \"llama3-2024\", \"file\": \"checklist.tex\", \"line\": 33, \"command\": \"cite\"}, {\"key\": \"vllm-2023\", \"file\": \"checklist.tex\", \"line\": 33, \"command\": \"cite\"}, {\"key\": \"minilm-2020\", \"file\": \"checklist.tex\", \"line\": 33, \"command\": \"cite\"}, {\"key\": \"fewnerd-2021\", \"file\": \"prompt_appendix.tex\", \"line\": 204, \"command\": \"cite\"}, {\"key\": \"maven-2020\", \"file\": \"prompt_appendix.tex\", \"line\": 205, \"command\": \"cite\"}, {\"key\": \"fewrel-2018\", \"file\": \"prompt_appendix.tex\", \"line\": 206, \"command\": \"cite\"}, {\"key\": \"rothman-1990\", \"file\": \"main.tex\", \"line\": 321, \"command\": \"citep\"}, {\"key\": \"li2023evaluating\", \"file\": \"main.tex\", \"line\": 518, \"command\": \"citet\"}, {\"key\": \"gemini-2025\", \"file\": \"main.tex\", \"line\": 563, \"command\": \"citep\"}, {\"key\": \"lost-in-middle-2024\", \"file\": \"main.tex\", \"line\": 607, \"command\": \"cite\"}], \"online_verification\": [{\"key\": \"tam-2024-let-me-speak\", \"title\": \"Let Me Speak Freely? A Study on the Impact of Format Restrictions on Performance of Large Language Models\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Let Me Speak Freely? A Study on the Impact of Format Restrictions on Performance of Large Language Models\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"yin-2019-zero-shot-bench\", \"title\": \"Benchmarking Zero-shot Text Classification: Datasets, Evaluation and Entailment Approach\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Benchmarking Zero-shot Text Classification: Datasets, Evaluation and Entailment Approach\", \"matched_year\": \"2019\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"schuirmann-1987-tost\", \"title\": \"A Comparison of the Two One-Sided Tests Procedure and the Power Approach for Assessing the Equivalence of Average Bioavailability\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"A comparison of the Two One-Sided Tests Procedure and the Power Approach for assessing the equivalence of average bioavailability\", \"matched_year\": \"1987\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"gemini-2025\", \"title\": \"Gemini 2.5: Pushing the Frontier with Advanced Reasoning, Multimodality, and Long Context\", \"status\": \"not_found\", \"confidence\": 0.443, \"matched_title\": \"MM-LLMs: Recent Advances in MultiModal Large Language Models\", \"matched_year\": \"\", \"mismatch_fields\": [], \"note\": \"best match similarity 0.44 below threshold 0.82\"}, {\"key\": \"snell2017prototypical\", \"title\": \"Prototypical Networks for Few-shot Learning\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Prototypical Networks for Few-shot Learning\", \"matched_year\": \"2017\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"muller2019when\", \"title\": \"When Does Label Smoothing Help?\", \"status\": \"mismatch\", \"confidence\": 1.0, \"matched_title\": \"When Does Label Smoothing Help?\", \"matched_year\": \"2019\", \"mismatch_fields\": [\"first_author: bib=m\\\\\\\"uller vs api=müller\"], \"note\": \"\"}, {\"key\": \"peterson2019human\", \"title\": \"Human Uncertainty Makes Classification More Robust\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Human Uncertainty Makes Classification More Robust\", \"matched_year\": \"2019\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"jagannatha2020calibrating\", \"title\": \"Calibrating Structured Output Predictors for Natural Language Processing\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Calibrating Structured Output Predictors for Natural Language Processing\", \"matched_year\": \"2020\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"willard2023efficient\", \"title\": \"Efficient Guided Generation for Large Language Models\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Efficient Guided Generation for Large Language Models\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"lu2022fantastically\", \"title\": \"Fantastically Ordered Prompts and Where to Find Them: Overcoming Few-Shot Prompt Order Sensitivity\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Fantastically Ordered Prompts and Where to Find Them: Overcoming Few-Shot Prompt Order Sensitivity\", \"matched_year\": \"2022\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"yang2025beyond\", \"title\": \"Beyond Boundaries: Learning a Universal Entity Taxonomy across Datasets and Languages for Open Named Entity Recognition\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Beyond Boundaries: Learning a Universal Entity Taxonomy across Datasets and Languages for Open Named Entity Recognition\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"llm-pee-2025\", \"title\": \"Towards Event Extraction with Massive Types: LLM-based Collaborative Annotation and Partitioning Extraction\", \"status\": \"mismatch\", \"confidence\": 1.0, \"matched_title\": \"Towards Event Extraction with Massive Types: LLM-based Collaborative Annotation and Partitioning Extraction\", \"matched_year\": \"2025\", \"mismatch_fields\": [\"first_author: bib=liu vs api=2025\"], \"note\": \"\"}, {\"key\": \"parse-2025\", \"title\": \"PARSE: LLM Driven Schema Optimization for Reliable Entity Extraction\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"PARSE: LLM Driven Schema Optimization for Reliable Entity Extraction\", \"matched_year\": \"2025\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"dee-2024\", \"title\": \"Decompose, Enrich, and Extract! Schema-aware Event Extraction using LLMs\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Decompose, Enrich, and Extract! Schema-aware Event Extraction using LLMs\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"crossagentie-2025\", \"title\": \"CROSSAGENTIE: Cross-Type and Cross-Task Multi-Agent LLM Collaboration for Zero-Shot Information Extraction\", \"status\": \"mismatch\", \"confidence\": 1.0, \"matched_title\": \"CROSSAGENTIE: Cross-Type and Cross-Task Multi-Agent LLM Collaboration for Zero-Shot Information Extraction\", \"matched_year\": \"2025\", \"mismatch_fields\": [\"first_author: bib=lu vs api=meng\"], \"note\": \"\"}, {\"key\": \"cmas-ner-2025\", \"title\": \"A Cooperative Multi-Agent Framework for Zero-Shot Named Entity Recognition\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"A Cooperative Multi-Agent Framework for Zero-Shot Named Entity Recognition\", \"matched_year\": \"2025\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"uniner-2024\", \"title\": \"UniversalNER: Targeted Distillation from Large Language Models for Open Named Entity Recognition\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"UniversalNER: Targeted Distillation from Large Language Models for Open Named Entity Recognition\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"gollie-2024\", \"title\": \"GoLLIE: Annotation Guidelines improve Zero-Shot Information-Extraction\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"GoLLIE: Annotation Guidelines improve Zero-Shot Information-Extraction\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"gliner-2024\", \"title\": \"GLiNER: Generalist Model for Named Entity Recognition using Bidirectional Transformer\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"GLiNER: Generalist Model for Named Entity Recognition using Bidirectional Transformer\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"gliner2-2025\", \"title\": \"GLiNER2: Schema-Driven Multi-Task Learning for Structured Information Extraction\", \"status\": \"mismatch\", \"confidence\": 1.0, \"matched_title\": \"GLiNER2: Schema-Driven Multi-Task Learning for Structured Information Extraction\", \"matched_year\": \"2025\", \"mismatch_fields\": [\"first_author: bib=zaratiana vs api=2025\"], \"note\": \"\"}, {\"key\": \"iepile-2024\", \"title\": \"IEPile: Unearthing Large Scale Schema-Conditioned Information Extraction Corpus\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"IEPile: Unearthing Large Scale Schema-Conditioned Information Extraction Corpus\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"dror-2018-significance\", \"title\": \"The Hitchhiker's Guide to Testing Statistical Significance in Natural Language Processing\", \"status\": \"not_found\", \"confidence\": 0.339, \"matched_title\": \"The Sorcerer II Global Ocean Sampling Expedition: Northwest Atlantic through Eastern Tropical Pacific\", \"matched_year\": \"\", \"mismatch_fields\": [], \"note\": \"best match similarity 0.34 below threshold 0.82\"}, {\"key\": \"lost-in-middle-2024\", \"title\": \"Lost in the Middle: How Language Models Use Long Contexts\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Lost in the Middle: How Language Models Use Long Contexts\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"llm4ie-survey-2024\", \"title\": \"Large Language Models for Generative Information Extraction: A Survey\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Large language models for generative information extraction: a survey\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"knowcoder-2024\", \"title\": \"KnowCoder: Coding Structured Knowledge into LLMs for Universal Information Extraction\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"KnowCoder: Coding Structured Knowledge into LLMs for Universal Information Extraction\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"slot-2025\", \"title\": \"SLOT: Structuring the Output of Large Language Models\", \"status\": \"mismatch\", \"confidence\": 1.0, \"matched_title\": \"SLOT: Structuring the Output of Large Language Models\", \"matched_year\": \"2025\", \"mismatch_fields\": [\"first_author: bib=shen vs api=wang\"], \"note\": \"\"}, {\"key\": \"gao-repr-degen-2019\", \"title\": \"Representation Degeneration Problem in Training Natural Language Generation Models\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Representation Degeneration Problem in Training Natural Language Generation Models\", \"matched_year\": \"2019\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"ethayarajh-contextual-2019\", \"title\": \"How Contextual are Contextualized Word Representations? Comparing the Geometry of BERT, ELMo, and GPT-2 Embeddings\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"How Contextual are Contextualized Word Representations? Comparing the Geometry of BERT, ELMo, and GPT-2 Embeddings\", \"matched_year\": \"2019\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"cai-isotropy-clusters-2021\", \"title\": \"Isotropy in the Contextual Embedding Space: Clusters and Manifolds\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Isotropy in the Contextual Embedding Space: Clusters and Manifolds\", \"matched_year\": \"2021\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"instructuie-2023\", \"title\": \"InstructUIE: Multi-task Instruction Tuning for Unified Information Extraction\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"InstructUIE: Multi-task Instruction Tuning for Unified Information Extraction\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"codeie-2023\", \"title\": \"CodeIE: Large Code Generation Models are Better Few-Shot Information Extractors\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"CodeIE: Large Code Generation Models are Better Few-Shot Information Extractors\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"adelie-2024\", \"title\": \"ADELIE: Aligning Large Language Models on Information Extraction\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"ADELIE: Aligning Large Language Models on Information Extraction\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"oneke-2025\", \"title\": \"OneKE: A Dockerized Schema-Guided LLM Agent-based Knowledge Extraction System\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"OneKE: A Dockerized Schema-Guided LLM Agent-based Knowledge Extraction System\", \"matched_year\": \"2025\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"fewnerd-2021\", \"title\": \"Few-NERD: A Few-shot Named Entity Recognition Dataset\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Few-NERD: A Few-shot Named Entity Recognition Dataset\", \"matched_year\": \"2021\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"fewrel-2018\", \"title\": \"FewRel: A Large-Scale Supervised Few-Shot Relation Classification Dataset with State-of-the-Art Evaluation\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"FewRel: A Large-Scale Supervised Few-Shot Relation Classification Dataset with State-of-the-Art Evaluation\", \"matched_year\": \"2018\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"maven-2020\", \"title\": \"MAVEN: A Massive General Domain Event Detection Dataset\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"MAVEN: A Massive General Domain Event Detection Dataset\", \"matched_year\": \"2020\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"docred-2019\", \"title\": \"DocRED: A Large-Scale Document-Level Relation Extraction Dataset\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"DocRED: A Large-Scale Document-Level Relation Extraction Dataset\", \"matched_year\": \"2019\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"qwen3-2025\", \"title\": \"Qwen3 Technical Report\", \"status\": \"mismatch\", \"confidence\": 1.0, \"matched_title\": \"Qwen3 Technical Report\", \"matched_year\": \"2025\", \"mismatch_fields\": [\"first_author: bib=team vs api=yang\"], \"note\": \"\"}, {\"key\": \"llama3-2024\", \"title\": \"The Llama 3 Herd of Models\", \"status\": \"mismatch\", \"confidence\": 1.0, \"matched_title\": \"The Llama 3 herd of models\", \"matched_year\": \"2025\", \"mismatch_fields\": [\"first_author: bib=dubey vs api=aaron\"], \"note\": \"\"}, {\"key\": \"sentence-bert-2019\", \"title\": \"Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks\", \"matched_year\": \"2019\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"minilm-2020\", \"title\": \"MiniLM: Deep Self-Attention Distillation for Task-Agnostic Compression of Pre-Trained Transformers\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"MiniLM: Deep Self-Attention Distillation for Task-Agnostic Compression of Pre-Trained Transformers\", \"matched_year\": \"2020\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"reflect-learn-2026\", \"title\": \"Reflect then Learn: Active Prompting for Information Extraction Guided by Introspective Confusion\", \"status\": \"mismatch\", \"confidence\": 1.0, \"matched_title\": \"Reflect Then Learn: Active Prompting for Information Extraction Guided by Introspective Confusion\", \"matched_year\": \"2026\", \"mismatch_fields\": [\"first_author: bib=zhao vs api=2026\"], \"note\": \"\"}, {\"key\": \"sclar-sensitivity-2024\", \"title\": \"Quantifying Language Models' Sensitivity to Spurious Features in Prompt Design\", \"status\": \"not_found\", \"confidence\": 0.72, \"matched_title\": \"Quantifying Language Models' Sensitivity to Spurious Features in Prompt Design or: How I learned to start worrying about prompt formatting\", \"matched_year\": \"\", \"mismatch_fields\": [], \"note\": \"best match similarity 0.72 below threshold 0.82\"}, {\"key\": \"vllm-2023\", \"title\": \"Efficient Memory Management for Large Language Model Serving with PagedAttention\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Efficient Memory Management for Large Language Model Serving with PagedAttention\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"xie-zeroshot-ner-2023\", \"title\": \"Empirical Study of Zero-Shot NER with ChatGPT\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Empirical Study of Zero-Shot NER with ChatGPT\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"wadhwa-re-llm-2023\", \"title\": \"Revisiting Relation Extraction in the era of Large Language Models\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Revisiting Relation Extraction in the era of Large Language Models\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"relationprompt-2022\", \"title\": \"RelationPrompt: Leveraging Prompts to Generate Synthetic Data for Zero-Shot Relation Triplet Extraction\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"RelationPrompt: Leveraging Prompts to Generate Synthetic Data for Zero-Shot Relation Triplet Extraction\", \"matched_year\": \"2022\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"promptner-2023\", \"title\": \"PromptNER: Prompting For Named Entity Recognition\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"PromptNER: Prompting For Named Entity Recognition\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"json-schema-bench-2025\", \"title\": \"JSONSchemaBench: A Rigorous Benchmark of Structured Outputs for Language Models\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"JSONSchemaBench: A Rigorous Benchmark of Structured Outputs for Language Models\", \"matched_year\": \"2025\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"rastogi2020towards\", \"title\": \"Towards Scalable Multi-Domain Conversational Agents: The Schema-Guided Dialogue Dataset\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Towards Scalable Multi-Domain Conversational Agents: The Schema-Guided Dialogue Dataset\", \"matched_year\": \"2020\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"li2023evaluating\", \"title\": \"Evaluating ChatGPT's Information Extraction Capabilities: An Assessment of Performance, Explainability, Calibration, and Faithfulness\", \"status\": \"not_found\", \"confidence\": 0.333, \"matched_title\": \"Generative AI in Medical Practice: In-Depth Exploration of Privacy and Security Challenges\", \"matched_year\": \"\", \"mismatch_fields\": [], \"note\": \"best match similarity 0.33 below threshold 0.82\"}, {\"key\": \"lee2022sgd\", \"title\": \"SGD-X: A Benchmark for Robust Generalization in Schema-Guided Dialogue Systems\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"SGD-X: A Benchmark for Robust Generalization in Schema-Guided Dialogue Systems\", \"matched_year\": \"2022\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"volkanovska2025ner\", \"title\": \"A Study of Errors in the Output of Large Language Models for Domain-Specific Few-Shot Named Entity Recognition\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"A Study of Errors in the Output of Large Language Models for Domain-Specific Few-Shot Named Entity Recognition\", \"matched_year\": \"2025\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"haystack-to-needle-2025\", \"title\": \"From Haystack to Needle: Label Space Reduction for Zero-shot Classification\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"From Haystack to Needle: Label Space Reduction for Zero-shot Classification\", \"matched_year\": \"2025\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"cohen-1988-power\", \"title\": \"Statistical Power Analysis for the Behavioral Sciences\", \"status\": \"mismatch\", \"confidence\": 1.0, \"matched_title\": \"Statistical Power Analysis for the Behavioral Sciences\", \"matched_year\": \"1989\", \"mismatch_fields\": [\"first_author: bib=cohen vs api=muller\"], \"note\": \"\"}, {\"key\": \"lakens-2013-effect-size\", \"title\": \"Calculating and Reporting Effect Sizes to Facilitate Cumulative Science: A Practical Primer for t-Tests and ANOVAs\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Calculating and reporting effect sizes to facilitate cumulative science: a practical primer for t-tests and ANOVAs\", \"matched_year\": \"2013\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"deng-2010-imagenet\", \"title\": \"What Does Classifying More Than 10,000 Image Categories Tell Us?\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"What Does Classifying More Than 10,000 Image Categories Tell Us?\", \"matched_year\": \"2010\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"rothman-1990\", \"title\": \"No Adjustments Are Needed for Multiple Comparisons\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"No Adjustments Are Needed for Multiple Comparisons\", \"matched_year\": \"1990\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"lakens-2017-equivalence\", \"title\": \"Equivalence Tests: A Practical Primer for t Tests, Correlations, and Meta-Analyses\", \"status\": \"verified\", \"confidence\": 0.988, \"matched_title\": \"Equivalence Tests: A Practical Primer for t-Tests, Correlations, and Meta-Analyses\", \"matched_year\": \"2016\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"zhou-2025-rethinking\", \"title\": \"Rethinking Word Similarity: Semantic Similarity through Classification Confusion\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Rethinking Word Similarity: Semantic Similarity through Classification Confusion\", \"matched_year\": \"2025\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"guo-2021-label-confusion\", \"title\": \"Label Confusion Learning to Enhance Text Classification Models\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Label Confusion Learning to Enhance Text Classification Models\", \"matched_year\": \"2021\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"novack-2023-chils\", \"title\": \"CHiLS: Zero-Shot Image Classification with Hierarchical Label Sets\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"CHiLS: Zero-Shot Image Classification with Hierarchical Label Sets\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"cocchieri-2025-zeroner\", \"title\": \"ZeroNER: Fueling Zero-Shot Named Entity Recognition via Entity Type Descriptions\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"ZeroNER: Fueling Zero-Shot Named Entity Recognition via Entity Type Descriptions\", \"matched_year\": \"2025\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"dlisc-2025\", \"title\": \"Effective and Efficient Schema-aware Information Extraction Using On-Device Large Language Models\", \"status\": \"mismatch\", \"confidence\": 1.0, \"matched_title\": \"Effective and Efficient Schema-aware Information Extraction Using On-Device Large Language Models\", \"matched_year\": \"2025\", \"mismatch_fields\": [\"first_author: bib=li vs api=wen\"], \"note\": \"\"}, {\"key\": \"spt-2025\", \"title\": \"Schema as Parameterized Tools for Universal Information Extraction\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Schema as Parameterized Tools for Universal Information Extraction\", \"matched_year\": \"2025\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"card-2020-power\", \"title\": \"With Little Power Comes Great Responsibility\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"With Little Power Comes Great Responsibility\", \"matched_year\": \"2020\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"gillick-2014-entity-typing\", \"title\": \"Context-Dependent Fine-Grained Entity Type Tagging\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Context-Dependent Fine-Grained Entity Type Tagging\", \"matched_year\": \"2014\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"schall-2025-hidden-cost\", \"title\": \"The Hidden Cost of Structure: How Constrained Decoding Affects Language Model Performance\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"The Hidden Cost of Structure: How Constrained Decoding Affects Language Model Performance\", \"matched_year\": \"2025\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"chen-2026-multi-instance\", \"title\": \"Understanding LLM Performance Degradation in Multi-Instance Processing: The Roles of Instance Count and Context Length\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Understanding LLM Performance Degradation in Multi-Instance Processing: The Roles of Instance Count and Context Length\", \"matched_year\": \"2026\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"wei-2023-chatie\", \"title\": \"Zero-Shot Information Extraction via Chatting with ChatGPT\", \"status\": \"mismatch\", \"confidence\": 0.935, \"matched_title\": \"ChatIE: Zero-Shot Information Extraction via Chatting with ChatGPT\", \"matched_year\": \"2023\", \"mismatch_fields\": [\"first_author: bib=wei vs api=xiang\"], \"note\": \"\"}]}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bfab09a1-0481-45b8-8b5e-eaa3259b83af",
  "isSidechain": false,
  "promptId": "8257bd0e-08b4-4530-aa87-1e185ea40a51",
  "type": "user",
  "uuid": "e4b0175a-8492-4687-a03b-aba18050d998",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-18-projects-schema-dag-extraction--claude-sessions-review-reviewer-2-302b64f9/0ff1fe81-4731-4c76-91b4-02652701ddff/tool-results/toolu_01VZo7LNTXDQqfP3yD4gMWxh.txt",
      "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"summary\\\": {\\\"total_bib_entries\\\": 70, \\\"total_citations\\\": 96, \\\"unique_cited_keys\\\": 69, \\\"orphan_bib\\\": 1, \\\"missing_bib\\\": 0, \\\"duplicate_keys\\\": 0, \\\"online_verified\\\": 55, \\\"online_not_found\\\": 4, \\\"online_mismatch\\\": 11}, \\\"cross_check\\\": {\\\"orphan_bib\\\": [\\\"jagannatha2020calibrating\\\"], \\\"missing_bib\\\": [], \\\"orphan_count\\\": 1, \\\"missing_count\\\": 0}, \\\"bib_entries\\\": [{\\\"key\\\": \\\"tam-2024-let-me-speak\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Let Me Speak Freely? A Study on the Impact of Format Restrictions on Performance of Large Language Models\\\", \\\"authors\\\": \\\"Tam, Zhi Rui and Wu, Cheng-Kuang and Tsai, Yi-Lin and Lin, Chieh-Yen and Lee, Hu...\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"Proceedings of the 2024 Conference on Empirical Methods in Natural Language Proc...\\\"}, {\\\"key\\\": \\\"yin-2019-zero-shot-bench\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Benchmarking Zero-shot Text Classification: Datasets, Evaluation and Entailment Approach\\\", \\\"authors\\\": \\\"Yin, Wenpeng and Hay, Jamaal and Roth, Dan\\\", \\\"year\\\": \\\"2019\\\", \\\"venue\\\": \\\"Proceedings of the 2019 Conference on Empirical Methods in Natural Language Proc...\\\"}, {\\\"key\\\": \\\"schuirmann-1987-tost\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"A Comparison of the Two One-Sided Tests Procedure and the Power Approach for Assessing the Equivalence of Average Bioava...\\\", \\\"authors\\\": \\\"Schuirmann, Donald J.\\\", \\\"year\\\": \\\"1987\\\", \\\"venue\\\": \\\"Journal of Pharmacokinetics and Biopharmaceutics\\\"}, {\\\"key\\\": \\\"gemini-2025\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Gemini 2.5: Pushing the Frontier with Advanced Reasoning, Multimodality, and Long Context\\\", \\\"authors\\\": \\\"Comanici, Gheorghe and others\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"arXiv preprint arXiv:2507.06261\\\"}, {\\\"key\\\": \\\"snell2017prototypical\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Prototypical Networks for Few-shot Learning\\\", \\\"authors\\\": \\\"Snell, Jake and Swersky, Kevin and Zemel, Richard\\\", \\\"year\\\": \\\"2017\\\", \\\"venue\\\": \\\"Advances in Neural Information Processing Systems\\\"}, {\\\"key\\\": \\\"muller2019when\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"When Does Label Smoothing Help?\\\", \\\"authors\\\": \\\"M\\\\\\\\\\\\\\\"uller, Rafael and Kornblith, Simon and Hinton, Geoffrey E.\\\", \\\"year\\\": \\\"2019\\\", \\\"venue\\\": \\\"Advances in Neural Information Processing Systems\\\"}, {\\\"key\\\": \\\"peterson2019human\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Human Uncertainty Makes Classification More Robust\\\", \\\"authors\\\": \\\"Peterson, Joshua C. and Battleday, Ruairidh M. and Griffiths, Thomas L. and Russ...\\\", \\\"year\\\": \\\"2019\\\", \\\"venue\\\": \\\"Proceedings of the IEEE/CVF International Conference on Computer Vision\\\"}, {\\\"key\\\": \\\"jagannatha2020calibrating\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Calibrating Structured Output Predictors for Natural Language Processing\\\", \\\"authors\\\": \\\"Jagannatha, Abhyuday and Yu, Hong\\\", \\\"year\\\": \\\"2020\\\", \\\"venue\\\": \\\"Proceedings of the 58th Annual Meeting of the Association for Computational Ling...\\\"}, {\\\"key\\\": \\\"willard2023efficient\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Efficient Guided Generation for Large Language Models\\\", \\\"authors\\\": \\\"Willard, Brandon T. and Louf, R\\\\\\\\'emi\\\", \\\"year\\\": \\\"2023\\\", \\\"venue\\\": \\\"arXiv preprint arXiv:2307.09702\\\"}, {\\\"key\\\": \\\"lu2022fantastically\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Fantastically Ordered Prompts and Where to Find Them: Overcoming Few-Shot Prompt Order Sensitivity\\\", \\\"authors\\\": \\\"Lu, Yao and Bartolo, Max and Moore, Alastair and Riedel, Sebastian and Stenetorp...\\\", \\\"year\\\": \\\"2022\\\", \\\"venue\\\": \\\"Proceedings of the 60th Annual Meeting of the Association for Computational Ling...\\\"}, {\\\"key\\\": \\\"yang2025beyond\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Beyond Boundaries: Learning a Universal Entity Taxonomy across Datasets and Languages for Open Named Entity Recognition\\\", \\\"authors\\\": \\\"Yang, Yuming and Zhao, Wantong and Huang, Caishuang and Ye, Junjie and Wang, Xia...\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"Proceedings of the 31st International Conference on Computational Linguistics\\\"}, {\\\"key\\\": \\\"llm-pee-2025\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Towards Event Extraction with Massive Types: LLM-based Collaborative Annotation and Partitioning Extraction\\\", \\\"authors\\\": \\\"Liu, Wenxuan and Li, Zixuan and Bai, Long and Zuo, Yuxin and Xu, Daozhu and Jin,...\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"Proceedings of the 2025 Conference on Empirical Methods in Natural Language Proc...\\\"}, {\\\"key\\\": \\\"parse-2025\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"PARSE: LLM Driven Schema Optimization for Reliable Entity Extraction\\\", \\\"authors\\\": \\\"Shrimal, Anubhav and Jain, Aryan and Chowdhury, Soumyajit and Yenigalla, Promod\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"Proceedings of the 2025 Conference on Empirical Methods in Natural Language Proc...\\\"}, {\\\"key\\\": \\\"dee-2024\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Decompose, Enrich, and Extract! Schema-aware Event Extraction using LLMs\\\", \\\"authors\\\": \\\"Shiri, Fatemeh and Nguyen, Van and Moghimifar, Farhad and Yoo, John and Haffari,...\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"Proceedings of the IEEE International Conference on Tools with Artificial Intell...\\\"}, {\\\"key\\\": \\\"crossagentie-2025\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"CROSSAGENTIE: Cross-Type and Cross-Task Multi-Agent LLM Collaboration for Zero-Shot Information Extraction\\\", \\\"authors\\\": \\\"Lu, Meng and Xie, Yuzhang and Bi, Zhenyu and Cao, Shuxiang and Wang, Xuan\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"Findings of the Association for Computational Linguistics: ACL 2025\\\"}, {\\\"key\\\": \\\"cmas-ner-2025\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"A Cooperative Multi-Agent Framework for Zero-Shot Named Entity Recognition\\\", \\\"authors\\\": \\\"Wang, Zihan and Zhao, Ziqi and Lyu, Yougang and Chen, Zhumin and de Rijke, Maart...\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"Proceedings of the ACM Web Conference 2025\\\"}, {\\\"key\\\": \\\"uniner-2024\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"UniversalNER: Targeted Distillation from Large Language Models for Open Named Entity Recognition\\\", \\\"authors\\\": \\\"Zhou, Wenxuan and Zhang, Sheng and Gu, Yu and Chen, Muhao and Poon, Hoifung\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"International Conference on Learning Representations\\\"}, {\\\"key\\\": \\\"gollie-2024\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"GoLLIE: Annotation Guidelines improve Zero-Shot Information-Extraction\\\", \\\"authors\\\": \\\"Sainz, Oscar and Garc\\\\\\\\'\\\\\\\\ia-Ferrero, Iker and Agerri, Rodrigo and Lopez de Lacall...\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"International Conference on Learning Representations\\\"}, {\\\"key\\\": \\\"gliner-2024\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"GLiNER: Generalist Model for Named Entity Recognition using Bidirectional Transformer\\\", \\\"authors\\\": \\\"Zaratiana, Urchade and Tomeh, Nadi and Holat, Pierre and Charnois, Thierry\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"Proceedings of the 2024 Conference of the North American Chapter of the Associat...\\\"}, {\\\"key\\\": \\\"gliner2-2025\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"GLiNER2: Schema-Driven Multi-Task Learning for Structured Information Extraction\\\", \\\"authors\\\": \\\"Zaratiana, Urchade and Pasternak, Gil and Boyd, Oliver and Hurn-Maloney, George ...\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"Proceedings of the 2025 Conference on Empirical Methods in Natural Language Proc...\\\"}, {\\\"key\\\": \\\"iepile-2024\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"IEPile: Unearthing Large Scale Schema-Conditioned Information Extraction Corpus\\\", \\\"authors\\\": \\\"Gui, Honghao and Yuan, Lin and Ye, Hongbin and Zhang, Ningyu and Sun, Mengshu an...\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"Proceedings of the 62nd Annual Meeting of the Association for Computational Ling...\\\"}, {\\\"key\\\": \\\"dror-2018-significance\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"The Hitchhiker's Guide to Testing Statistical Significance in Natural Language Processing\\\", \\\"authors\\\": \\\"Dror, Rotem and Baumer, Gili and Shlomov, Segev and Reichart, Roi\\\", \\\"year\\\": \\\"2018\\\", \\\"venue\\\": \\\"Proceedings of the 56th Annual Meeting of the Association for Computational Ling...\\\"}, {\\\"key\\\": \\\"lost-in-middle-2024\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Lost in the Middle: How Language Models Use Long Contexts\\\", \\\"authors\\\": \\\"Liu, Nelson F. and Lin, Kevin and Hewitt, John and Paranjape, Ashwin and Bevilac...\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"Transactions of the Association for Computational Linguistics\\\"}, {\\\"key\\\": \\\"llm4ie-survey-2024\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Large Language Models for Generative Information Extraction: A Survey\\\", \\\"authors\\\": \\\"Xu, Derong and Chen, Wei and Peng, Wenjun and Zhang, Chao and Xu, Tong and Zhao,...\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"Frontiers of Computer Science\\\"}, {\\\"key\\\": \\\"knowcoder-2024\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"KnowCoder: Coding Structured Knowledge into LLMs for Universal Information Extraction\\\", \\\"authors\\\": \\\"Li, Zixuan and Zeng, Yutao and Zuo, Yuxin and Ren, Weicheng and Liu, Wenxuan and...\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"Proceedings of the 62nd Annual Meeting of the Association for Computational Ling...\\\"}, {\\\"key\\\": \\\"slot-2025\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"SLOT: Structuring the Output of Large Language Models\\\", \\\"authors\\\": \\\"Shen, Zhengyuan and Wang, Darren Yow-Bang and Mishra, Soumya Smruti and Xu, Zhic...\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"Proceedings of the 2025 Conference on Empirical Methods in Natural Language Proc...\\\"}, {\\\"key\\\": \\\"gao-repr-degen-2019\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Representation Degeneration Problem in Training Natural Language Generation Models\\\", \\\"authors\\\": \\\"Gao, Jun and He, Di and Tan, Xu and Qin, Tao and Wang, Liwei and Liu, Tie-Yan\\\", \\\"year\\\": \\\"2019\\\", \\\"venue\\\": \\\"International Conference on Learning Representations\\\"}, {\\\"key\\\": \\\"ethayarajh-contextual-2019\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"How Contextual are Contextualized Word Representations? Comparing the Geometry of BERT, ELMo, and GPT-2 Embeddings\\\", \\\"authors\\\": \\\"Ethayarajh, Kawin\\\", \\\"year\\\": \\\"2019\\\", \\\"venue\\\": \\\"Proceedings of the 2019 Conference on Empirical Methods in Natural Language Proc...\\\"}, {\\\"key\\\": \\\"cai-isotropy-clusters-2021\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Isotropy in the Contextual Embedding Space: Clusters and Manifolds\\\", \\\"authors\\\": \\\"Cai, Xingyu and Huang, Jiaji and Bian, Yuchen and Church, Kenneth\\\", \\\"year\\\": \\\"2021\\\", \\\"venue\\\": \\\"International Conference on Learning Representations\\\"}, {\\\"key\\\": \\\"instructuie-2023\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"InstructUIE: Multi-task Instruction Tuning for Unified Information Extraction\\\", \\\"authors\\\": \\\"Wang, Xiao and Zhou, Weikang and Zu, Can and Xia, Han and Chen, Tianze and Zhang...\\\", \\\"year\\\": \\\"2023\\\", \\\"venue\\\": \\\"arXiv preprint arXiv:2304.08085\\\"}, {\\\"key\\\": \\\"codeie-2023\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"CodeIE: Large Code Generation Models are Better Few-Shot Information Extractors\\\", \\\"authors\\\": \\\"Li, Peng and Sun, Tianxiang and Tang, Qiong and Yan, Hang and Wu, Yuanbin and Hu...\\\", \\\"year\\\": \\\"2023\\\", \\\"venue\\\": \\\"Proceedings of the 61st Annual Meeting of the Association for Computational Ling...\\\"}, {\\\"key\\\": \\\"adelie-2024\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"ADELIE: Aligning Large Language Models on Information Extraction\\\", \\\"authors\\\": \\\"Qi, Yunjia and Peng, Hao and Wang, Xiaozhi and Xu, Bin and Hou, Lei and Li, Juan...\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"Proceedings of the 2024 Conference on Empirical Methods in Natural Language Proc...\\\"}, {\\\"key\\\": \\\"oneke-2025\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"OneKE: A Dockerized Schema-Guided LLM Agent-based Knowledge Extraction System\\\", \\\"authors\\\": \\\"Luo, Yujie and Ru, Xiangyuan and Liu, Kangwei and Yuan, Lin and Sun, Mengshu and...\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"Companion Proceedings of the ACM Web Conference 2025\\\"}, {\\\"key\\\": \\\"fewnerd-2021\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Few-NERD: A Few-shot Named Entity Recognition Dataset\\\", \\\"authors\\\": \\\"Ding, Ning and Xu, Guangwei and Chen, Yulin and Wang, Xiaobin and Han, Xu and Xi...\\\", \\\"year\\\": \\\"2021\\\", \\\"venue\\\": \\\"Proceedings of the 59th Annual Meeting of the Association for Computational Ling...\\\"}, {\\\"key\\\": \\\"fewrel-2018\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"FewRel: A Large-Scale Supervised Few-Shot Relation Classification Dataset with State-of-the-Art Evaluation\\\", \\\"authors\\\": \\\"Han, Xu and Zhu, Hao and Yu, Pengfei and Wang, Ziyun and Yao, Yuan and Liu, Zhiy...\\\", \\\"year\\\": \\\"2018\\\", \\\"venue\\\": \\\"Proceedings of the 2018 Conference on Empirical Methods in Natural Language Proc...\\\"}, {\\\"key\\\": \\\"maven-2020\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"MAVEN: A Massive General Domain Event Detection Dataset\\\", \\\"authors\\\": \\\"Wang, Xiaozhi and Wang, Ziqi and Han, Xu and Jiang, Wangyi and Han, Rong and Liu...\\\", \\\"year\\\": \\\"2020\\\", \\\"venue\\\": \\\"Proceedings of the 2020 Conference on Empirical Methods in Natural Language Proc...\\\"}, {\\\"key\\\": \\\"docred-2019\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"DocRED: A Large-Scale Document-Level Relation Extraction Dataset\\\", \\\"authors\\\": \\\"Yao, Yuan and Ye, Deming and Li, Peng and Han, Xu and Lin, Yankai and Liu, Zheng...\\\", \\\"year\\\": \\\"2019\\\", \\\"venue\\\": \\\"Proceedings of the 57th Annual Meeting of the Association for Computational Ling...\\\"}, {\\\"key\\\": \\\"qwen3-2025\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Qwen3 Technical Report\\\", \\\"authors\\\": \\\"Qwen Team\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"arXiv preprint arXiv:2505.09388\\\"}, {\\\"key\\\": \\\"llama3-2024\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"The Llama 3 Herd of Models\\\", \\\"authors\\\": \\\"Dubey, Abhimanyu and Jauhri, Abhinav and Pandey, Abhinav and Kadian, Abhishek an...\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"arXiv preprint arXiv:2407.21783\\\"}, {\\\"key\\\": \\\"sentence-bert-2019\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks\\\", \\\"authors\\\": \\\"Reimers, Nils and Gurevych, Iryna\\\", \\\"year\\\": \\\"2019\\\", \\\"venue\\\": \\\"Proceedings of the 2019 Conference on Empirical Methods in Natural Language Proc...\\\"}, {\\\"key\\\": \\\"minilm-2020\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"MiniLM: Deep Self-Attention Distillation for Task-Agnostic Compression of Pre-Trained Transformers\\\", \\\"authors\\\": \\\"Wang, Wenhui and Wei, Furu and Dong, Li and Bao, Hangbo and Yang, Nan and Zhou, ...\\\", \\\"year\\\": \\\"2020\\\", \\\"venue\\\": \\\"Advances in Neural Information Processing Systems\\\"}, {\\\"key\\\": \\\"reflect-learn-2026\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Reflect then Learn: Active Prompting for Information Extraction Guided by Introspective Confusion\\\", \\\"authors\\\": \\\"Zhao, Dong and Wang, Yadong and Chen, Xiang and Wang, Chenxi and Dai, Hongliang ...\\\", \\\"year\\\": \\\"2026\\\", \\\"venue\\\": \\\"Proceedings of the AAAI Conference on Artificial Intelligence\\\"}, {\\\"key\\\": \\\"sclar-sensitivity-2024\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Quantifying Language Models' Sensitivity to Spurious Features in Prompt Design\\\", \\\"authors\\\": \\\"Sclar, Melanie and Choi, Yejin and Tsvetkov, Yulia and Suhr, Alane\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"International Conference on Learning Representations\\\"}, {\\\"key\\\": \\\"vllm-2023\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Efficient Memory Management for Large Language Model Serving with PagedAttention\\\", \\\"authors\\\": \\\"Kwon, Woosuk and Li, Zhuohan and Zhuang, Siyuan and Sheng, Ying and Zheng, Lianm...\\\", \\\"year\\\": \\\"2023\\\", \\\"venue\\\": \\\"Proceedings of the 29th Symposium on Operating Systems Principles\\\"}, {\\\"key\\\": \\\"xie-zeroshot-ner-2023\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Empirical Study of Zero-Shot NER with ChatGPT\\\", \\\"authors\\\": \\\"Xie, Tingyu and Li, Qi and Zhang, Jian and Zhang, Yan and Liu, Zuozhu and Wang, ...\\\", \\\"year\\\": \\\"2023\\\", \\\"venue\\\": \\\"Proceedings of the 2023 Conference on Empirical Methods in Natural Language Proc...\\\"}, {\\\"key\\\": \\\"wadhwa-re-llm-2023\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Revisiting Relation Extraction in the era of Large Language Models\\\", \\\"authors\\\": \\\"Wadhwa, Somin and Amir, Silvio and Wallace, Byron C.\\\", \\\"year\\\": \\\"2023\\\", \\\"venue\\\": \\\"Proceedings of the 61st Annual Meeting of the Association for Computational Ling...\\\"}, {\\\"key\\\": \\\"relationprompt-2022\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"RelationPrompt: Leveraging Prompts to Generate Synthetic Data for Zero-Shot Relation Triplet Extraction\\\", \\\"authors\\\": \\\"Chia, Yew Ken and Bing, Lidong and Poria, Soujanya and Si, Luo\\\", \\\"year\\\": \\\"2022\\\", \\\"venue\\\": \\\"Findings of the Association for Computational Linguistics: ACL 2022\\\"}, {\\\"key\\\": \\\"promptner-2023\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"PromptNER: Prompting For Named Entity Recognition\\\", \\\"authors\\\": \\\"Ashok, Dhananjay and Lipton, Zachary C.\\\", \\\"year\\\": \\\"2023\\\", \\\"venue\\\": \\\"arXiv preprint arXiv:2305.15444\\\"}, {\\\"key\\\": \\\"json-schema-bench-2025\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"JSONSchemaBench: A Rigorous Benchmark of Structured Outputs for Language Models\\\", \\\"authors\\\": \\\"Geng, Saibo and Cooper, Hudson and Moskal, Micha\\\\\\\\l and Jenkins, Samuel and Berma...\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"arXiv preprint arXiv:2501.10868\\\"}, {\\\"key\\\": \\\"rastogi2020towards\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Towards Scalable Multi-Domain Conversational Agents: The Schema-Guided Dialogue Dataset\\\", \\\"authors\\\": \\\"Rastogi, Abhinav and Zang, Xiaoxue and Sunkara, Srinivas and Gupta, Raghav and K...\\\", \\\"year\\\": \\\"2020\\\", \\\"venue\\\": \\\"Proceedings of the AAAI Conference on Artificial Intelligence\\\"}, {\\\"key\\\": \\\"li2023evaluating\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Evaluating ChatGPT's Information Extraction Capabilities: An Assessment of Performance, Explainability, Calibration, and...\\\", \\\"authors\\\": \\\"Li, Bo and Fang, Gexiang and Yang, Yang and Wang, Quansen and Ye, Wei and Zhao, ...\\\", \\\"year\\\": \\\"2023\\\", \\\"venue\\\": \\\"arXiv preprint arXiv:2304.11633\\\"}, {\\\"key\\\": \\\"lee2022sgd\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"SGD-X: A Benchmark for Robust Generalization in Schema-Guided Dialogue Systems\\\", \\\"authors\\\": \\\"Lee, Harrison and Gupta, Raghav and Rastogi, Abhinav and Cao, Yuan and Zhang, Bi...\\\", \\\"year\\\": \\\"2022\\\", \\\"venue\\\": \\\"Proceedings of the AAAI Conference on Artificial Intelligence\\\"}, {\\\"key\\\": \\\"volkanovska2025ner\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"A Study of Errors in the Output of Large Language Models for Domain-Specific Few-Shot Named Entity Recognition\\\", \\\"authors\\\": \\\"Volkanovska, Elena\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"Journal for Language Technology and Computational Linguistics\\\"}, {\\\"key\\\": \\\"haystack-to-needle-2025\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"From Haystack to Needle: Label Space Reduction for Zero-shot Classification\\\", \\\"authors\\\": \\\"Vandemoortele, Nathan and Steenwinckel, Bram and Ongenae, Femke and Van Hoecke, ...\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"arXiv preprint arXiv:2502.08436\\\"}, {\\\"key\\\": \\\"cohen-1988-power\\\", \\\"type\\\": \\\"book\\\", \\\"title\\\": \\\"Statistical Power Analysis for the Behavioral Sciences\\\", \\\"authors\\\": \\\"Cohen, Jacob\\\", \\\"year\\\": \\\"1988\\\", \\\"venue\\\": \\\"\\\"}, {\\\"key\\\": \\\"lakens-2013-effect-size\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Calculating and Reporting Effect Sizes to Facilitate Cumulative Science: A Practical Primer for t-Tests and ANOVAs\\\", \\\"authors\\\": \\\"Lakens, Dani\\\\\\\\\\\\\\\"el\\\", \\\"year\\\": \\\"2013\\\", \\\"venue\\\": \\\"Frontiers in Psychology\\\"}, {\\\"key\\\": \\\"deng-2010-imagenet\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"What Does Classifying More Than 10,000 Image Categories Tell Us?\\\", \\\"authors\\\": \\\"Deng, Jia and Berg, Alexander C. and Li, Kai and Fei-Fei, Li\\\", \\\"year\\\": \\\"2010\\\", \\\"venue\\\": \\\"Proceedings of the 11th European Conference on Computer Vision\\\"}, {\\\"key\\\": \\\"rothman-1990\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"No Adjustments Are Needed for Multiple Comparisons\\\", \\\"authors\\\": \\\"Rothman, Kenneth J.\\\", \\\"year\\\": \\\"1990\\\", \\\"venue\\\": \\\"Epidemiology\\\"}, {\\\"key\\\": \\\"lakens-2017-equivalence\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Equivalence Tests: A Practical Primer for t Tests, Correlations, and Meta-Analyses\\\", \\\"authors\\\": \\\"Lakens, Dani\\\\\\\\\\\\\\\"el\\\", \\\"year\\\": \\\"2017\\\", \\\"venue\\\": \\\"Social Psychological and Personality Science\\\"}, {\\\"key\\\": \\\"zhou-2025-rethinking\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Rethinking Word Similarity: Semantic Similarity through Classification Confusion\\\", \\\"authors\\\": \\\"Zhou, Kaitlyn and Gao, Haishan and Chen, Sarah Li and Edelstein, Dan and Jurafsk...\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"Proceedings of the 2025 Conference of the North American Chapter of the Associat...\\\"}, {\\\"key\\\": \\\"guo-2021-label-confusion\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Label Confusion Learning to Enhance Text Classification Models\\\", \\\"authors\\\": \\\"Guo, Biyang and Han, Songqiao and Han, Xiao and Huang, Hailiang and Lu, Ting\\\", \\\"year\\\": \\\"2021\\\", \\\"venue\\\": \\\"Proceedings of the AAAI Conference on Artificial Intelligence\\\"}, {\\\"key\\\": \\\"novack-2023-chils\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"CHiLS: Zero-Shot Image Classification with Hierarchical Label Sets\\\", \\\"authors\\\": \\\"Novack, Zachary and McAuley, Julian and Lipton, Zachary Chase and Garg, Saurabh\\\", \\\"year\\\": \\\"2023\\\", \\\"venue\\\": \\\"Proceedings of the 40th International Conference on Machine Learning\\\"}, {\\\"key\\\": \\\"cocchieri-2025-zeroner\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"ZeroNER: Fueling Zero-Shot Named Entity Recognition via Entity Type Descriptions\\\", \\\"authors\\\": \\\"Cocchieri, Alessio and Mart\\\\\\\\'\\\\\\\\inez Galindo, Marcos and Frisoni, Giacomo and Moro...\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"Findings of the Association for Computational Linguistics: ACL 2025\\\"}, {\\\"key\\\": \\\"dlisc-2025\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Effective and Efficient Schema-aware Information Extraction Using On-Device Large Language Models\\\", \\\"authors\\\": \\\"Li, Zhuoqun and Wu, Hao and Li, Xinxin and Li, Zhoujun\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"arXiv preprint arXiv:2505.14992\\\"}, {\\\"key\\\": \\\"spt-2025\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Schema as Parameterized Tools for Universal Information Extraction\\\", \\\"authors\\\": \\\"Liang, Sheng and Zhang, Yongyue and Wu, Yaxiong and Tang, Ruiming and Liu, Yong\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"arXiv preprint arXiv:2506.01276\\\"}, {\\\"key\\\": \\\"card-2020-power\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"With Little Power Comes Great Responsibility\\\", \\\"authors\\\": \\\"Card, Dallas and Henderson, Peter and Khandelwal, Urvashi and Jia, Robin and Mah...\\\", \\\"year\\\": \\\"2020\\\", \\\"venue\\\": \\\"Proceedings of the 2020 Conference on Empirical Methods in Natural Language Proc...\\\"}, {\\\"key\\\": \\\"gillick-2014-entity-typing\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Context-Dependent Fine-Grained Entity Type Tagging\\\", \\\"authors\\\": \\\"Gillick, Daniel and Lazic, Nevena and Ganchev, Kuzman and Kirchner, Jesse and Hu...\\\", \\\"year\\\": \\\"2014\\\", \\\"venue\\\": \\\"arXiv preprint arXiv:1412.1820\\\"}, {\\\"key\\\": \\\"schall-2025-hidden-cost\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"The Hidden Cost of Structure: How Constrained Decoding Affects Language Model Performance\\\", \\\"authors\\\": \\\"Schall, Maximilian and de Melo, Gerard\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"Proceedings of the 15th International Conference on Recent Advances in Natural L...\\\"}, {\\\"key\\\": \\\"chen-2026-multi-instance\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Understanding LLM Performance Degradation in Multi-Instance Processing: The Roles of Instance Count and Context Length\\\", \\\"authors\\\": \\\"Chen, Jingxuan and Pilehvar, Mohammad Taher and Camacho-Collados, Jose\\\", \\\"year\\\": \\\"2026\\\", \\\"venue\\\": \\\"arXiv preprint arXiv:2603.22608\\\"}, {\\\"key\\\": \\\"wei-2023-chatie\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Zero-Shot Information Extraction via Chatting with ChatGPT\\\", \\\"authors\\\": \\\"Wei, Xiang and Cui, Xingyu and Cheng, Ning and Wang, Xiaobin and Zhang, Xin and ...\\\", \\\"year\\\": \\\"2023\\\", \\\"venue\\\": \\\"arXiv preprint arXiv:2302.10205\\\"}], \\\"tex_citations\\\": [{\\\"key\\\": \\\"llm4ie-survey-2024\\\", \\\"file\\\": \\\"introduction.tex\\\", \\\"line\\\": 4, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"uniner-2024\\\", \\\"file\\\": \\\"introduction.tex\\\", \\\"line\\\": 6, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"llm-pee-2025\\\", \\\"file\\\": \\\"introduction.tex\\\", \\\"line\\\": 6, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"parse-2025\\\", \\\"file\\\": \\\"introduction.tex\\\", \\\"line\\\": 6, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"fewnerd-2021\\\", \\\"file\\\": \\\"introduction.tex\\\", \\\"line\\\": 12, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"fewrel-2018\\\", \\\"file\\\": \\\"introduction.tex\\\", \\\"line\\\": 12, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"docred-2019\\\", \\\"file\\\": \\\"introduction.tex\\\", \\\"line\\\": 12, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"maven-2020\\\", \\\"file\\\": \\\"introduction.tex\\\", \\\"line\\\": 12, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"llm-pee-2025\\\", \\\"file\\\": \\\"introduction.tex\\\", \\\"line\\\": 22, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"instructuie-2023\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 5, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"knowcoder-2024\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 5, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"codeie-2023\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 5, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"gollie-2024\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 5, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"adelie-2024\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 5, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"slot-2025\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 5, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"oneke-2025\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 5, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"json-schema-bench-2025\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 5, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"willard2023efficient\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 5, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"xie-zeroshot-ner-2023\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 5, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"promptner-2023\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 5, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"uniner-2024\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 5, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"gliner-2024\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 5, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"gliner2-2025\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 5, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"gillick-2014-entity-typing\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 5, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"relationprompt-2022\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 5, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"wadhwa-re-llm-2023\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 5, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"wei-2023-chatie\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 5, \\\"command\\\": \\\"citet\\\"}, {\\\"key\\\": \\\"llm-pee-2025\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 8, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"iepile-2024\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 8, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"parse-2025\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 8, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"crossagentie-2025\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 8, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"cmas-ner-2025\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 8, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"dee-2024\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 8, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"reflect-learn-2026\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 8, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"chen-2026-multi-instance\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 8, \\\"command\\\": \\\"citet\\\"}, {\\\"key\\\": \\\"haystack-to-needle-2025\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 8, \\\"command\\\": \\\"citet\\\"}, {\\\"key\\\": \\\"dlisc-2025\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 8, \\\"command\\\": \\\"citet\\\"}, {\\\"key\\\": \\\"spt-2025\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 8, \\\"command\\\": \\\"citet\\\"}, {\\\"key\\\": \\\"rastogi2020towards\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 10, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"lee2022sgd\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 10, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"li2023evaluating\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 10, \\\"command\\\": \\\"citet\\\"}, {\\\"key\\\": \\\"lu2022fantastically\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 10, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"volkanovska2025ner\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 10, \\\"command\\\": \\\"citet\\\"}, {\\\"key\\\": \\\"deng-2010-imagenet\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 10, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"guo-2021-label-confusion\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 10, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"zhou-2025-rethinking\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 10, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"muller2019when\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 10, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"peterson2019human\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 10, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"novack-2023-chils\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 10, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"cocchieri-2025-zeroner\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 10, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"yang2025beyond\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 10, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"llm-pee-2025\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 12, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"snell2017prototypical\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 12, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"yin-2019-zero-shot-bench\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 12, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"cohen-1988-power\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 12, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"lakens-2013-effect-size\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 12, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"gao-repr-degen-2019\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 12, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"ethayarajh-contextual-2019\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 12, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"cai-isotropy-clusters-2021\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 12, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"fewnerd-2021\\\", \\\"file\\\": \\\"experimental_setup.tex\\\", \\\"line\\\": 10, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"fewrel-2018\\\", \\\"file\\\": \\\"experimental_setup.tex\\\", \\\"line\\\": 13, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"docred-2019\\\", \\\"file\\\": \\\"experimental_setup.tex\\\", \\\"line\\\": 16, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"maven-2020\\\", \\\"file\\\": \\\"experimental_setup.tex\\\", \\\"line\\\": 19, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"qwen3-2025\\\", \\\"file\\\": \\\"experimental_setup.tex\\\", \\\"line\\\": 56, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"minilm-2020\\\", \\\"file\\\": \\\"experimental_setup.tex\\\", \\\"line\\\": 56, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"sentence-bert-2019\\\", \\\"file\\\": \\\"experimental_setup.tex\\\", \\\"line\\\": 56, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"sentence-bert-2019\\\", \\\"file\\\": \\\"experimental_setup.tex\\\", \\\"line\\\": 56, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"ethayarajh-contextual-2019\\\", \\\"file\\\": \\\"experimental_setup.tex\\\", \\\"line\\\": 56, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"qwen3-2025\\\", \\\"file\\\": \\\"experimental_setup.tex\\\", \\\"line\\\": 82, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"vllm-2023\\\", \\\"file\\\": \\\"experimental_setup.tex\\\", \\\"line\\\": 82, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"sclar-sensitivity-2024\\\", \\\"file\\\": \\\"experimental_setup.tex\\\", \\\"line\\\": 82, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"llama3-2024\\\", \\\"file\\\": \\\"experimental_setup.tex\\\", \\\"line\\\": 82, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"lost-in-middle-2024\\\", \\\"file\\\": \\\"results.tex\\\", \\\"line\\\": 49, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"lakens-2017-equivalence\\\", \\\"file\\\": \\\"results.tex\\\", \\\"line\\\": 87, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"schuirmann-1987-tost\\\", \\\"file\\\": \\\"results.tex\\\", \\\"line\\\": 87, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"cai-isotropy-clusters-2021\\\", \\\"file\\\": \\\"results.tex\\\", \\\"line\\\": 92, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"tam-2024-let-me-speak\\\", \\\"file\\\": \\\"discussion.tex\\\", \\\"line\\\": 11, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"schall-2025-hidden-cost\\\", \\\"file\\\": \\\"discussion.tex\\\", \\\"line\\\": 11, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"rothman-1990\\\", \\\"file\\\": \\\"main.tex\\\", \\\"line\\\": 51, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"dror-2018-significance\\\", \\\"file\\\": \\\"main.tex\\\", \\\"line\\\": 51, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"card-2020-power\\\", \\\"file\\\": \\\"main.tex\\\", \\\"line\\\": 51, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"fewnerd-2021\\\", \\\"file\\\": \\\"checklist.tex\\\", \\\"line\\\": 33, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"fewrel-2018\\\", \\\"file\\\": \\\"checklist.tex\\\", \\\"line\\\": 33, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"docred-2019\\\", \\\"file\\\": \\\"checklist.tex\\\", \\\"line\\\": 33, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"maven-2020\\\", \\\"file\\\": \\\"checklist.tex\\\", \\\"line\\\": 33, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"qwen3-2025\\\", \\\"file\\\": \\\"checklist.tex\\\", \\\"line\\\": 33, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"llama3-2024\\\", \\\"file\\\": \\\"checklist.tex\\\", \\\"line\\\": 33, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"vllm-2023\\\", \\\"file\\\": \\\"checklist.tex\\\", \\\"line\\\": 33, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"minilm-2020\\\", \\\"file\\\": \\\"checklist.tex\\\", \\\"line\\\": 33, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"fewnerd-2021\\\", \\\"file\\\": \\\"prompt_appendix.tex\\\", \\\"line\\\": 204, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"maven-2020\\\", \\\"file\\\": \\\"prompt_appendix.tex\\\", \\\"line\\\": 205, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"fewrel-2018\\\", \\\"file\\\": \\\"prompt_appendix.tex\\\", \\\"line\\\": 206, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"rothman-1990\\\", \\\"file\\\": \\\"main.tex\\\", \\\"line\\\": 321, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"li2023evaluating\\\", \\\"file\\\": \\\"main.tex\\\", \\\"line\\\": 518, \\\"command\\\": \\\"citet\\\"}, {\\\"key\\\": \\\"gemini-2025\\\", \\\"file\\\": \\\"main.tex\\\", \\\"line\\\": 563, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"lost-in-middle-2024\\\", \\\"file\\\": \\\"main.tex\\\", \\\"line\\\": 607, \\\"command\\\": \\\"cite\\\"}], \\\"online_verification\\\": [{\\\"key\\\": \\\"tam-2024-let-me-speak\\\", \\\"title\\\": \\\"Let Me Speak Freely? A Study on the Impact of Format Restrictions on Performance of Large Language Models\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Let Me Speak Freely? A Study on the Impact of Format Restrictions on Performance of Large Language Models\\\", \\\"matched_year\\\": \\\"2024\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"yin-2019-zero-shot-bench\\\", \\\"title\\\": \\\"Benchmarking Zero-shot Text Classification: Datasets, Evaluation and Entailment Approach\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Benchmarking Zero-shot Text Classification: Datasets, Evaluation and Entailment Approach\\\", \\\"matched_year\\\": \\\"2019\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"schuirmann-1987-tost\\\", \\\"title\\\": \\\"A Comparison of the Two One-Sided Tests Procedure and the Power Approach for Assessing the Equivalence of Average Bioavailability\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"A comparison of the Two One-Sided Tests Procedure and the Power Approach for assessing the equivalence of average bioavailability\\\", \\\"matched_year\\\": \\\"1987\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"gemini-2025\\\", \\\"title\\\": \\\"Gemini 2.5: Pushing the Frontier with Advanced Reasoning, Multimodality, and Long Context\\\", \\\"status\\\": \\\"not_found\\\", \\\"confidence\\\": 0.443, \\\"matched_title\\\": \\\"MM-LLMs: Recent Advances in MultiModal Large Language Models\\\", \\\"matched_year\\\": \\\"\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"best match similarity 0.44 below threshold 0.82\\\"}, {\\\"key\\\": \\\"snell2017prototypical\\\", \\\"title\\\": \\\"Prototypical Networks for Few-shot Learning\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Prototypical Networks for Few-shot Learning\\\", \\\"matched_year\\\": \\\"2017\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"muller2019when\\\", \\\"title\\\": \\\"When Does Label Smoothing Help?\\\", \\\"status\\\": \\\"mismatch\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"When Does Label Smoothing Help?\\\", \\\"matched_year\\\": \\\"2019\\\", \\\"mismatch_fields\\\": [\\\"first_author: bib=m\\\\\\\\\\\\\\\"uller vs api=müller\\\"], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"peterson2019human\\\", \\\"title\\\": \\\"Human Uncertainty Makes Classification More Robust\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Human Uncertainty Makes Classification More Robust\\\", \\\"matched_year\\\": \\\"2019\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"jagannatha2020calibrating\\\", \\\"title\\\": \\\"Calibrating Structured Output Predictors for Natural Language Processing\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Calibrating Structured Output Predictors for Natural Language Processing\\\", \\\"matched_year\\\": \\\"2020\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"willard2023efficient\\\", \\\"title\\\": \\\"Efficient Guided Generation for Large Language Models\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Efficient Guided Generation for Large Language Models\\\", \\\"matched_year\\\": \\\"2023\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"lu2022fantastically\\\", \\\"title\\\": \\\"Fantastically Ordered Prompts and Where to Find Them: Overcoming Few-Shot Prompt Order Sensitivity\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Fantastically Ordered Prompts and Where to Find Them: Overcoming Few-Shot Prompt Order Sensitivity\\\", \\\"matched_year\\\": \\\"2022\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"yang2025beyond\\\", \\\"title\\\": \\\"Beyond Boundaries: Learning a Universal Entity Taxonomy across Datasets and Languages for Open Named Entity Recognition\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Beyond Boundaries: Learning a Universal Entity Taxonomy across Datasets and Languages for Open Named Entity Recognition\\\", \\\"matched_year\\\": \\\"2024\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"llm-pee-2025\\\", \\\"title\\\": \\\"Towards Event Extraction with Massive Types: LLM-based Collaborative Annotation and Partitioning Extraction\\\", \\\"status\\\": \\\"mismatch\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Towards Event Extraction with Massive Types: LLM-based Collaborative Annotation and Partitioning Extraction\\\", \\\"matched_year\\\": \\\"2025\\\", \\\"mismatch_fields\\\": [\\\"first_author: bib=liu vs api=2025\\\"], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"parse-2025\\\", \\\"title\\\": \\\"PARSE: LLM Driven Schema Optimization for Reliable Entity Extraction\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"PARSE: LLM Driven Schema Optimization for Reliable Entity Extraction\\\", \\\"matched_year\\\": \\\"2025\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"dee-2024\\\", \\\"title\\\": \\\"Decompose, Enrich, and Extract! Schema-aware Event Extraction using LLMs\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Decompose, Enrich, and Extract! Schema-aware Event Extraction using LLMs\\\", \\\"matched_year\\\": \\\"2024\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"crossagentie-2025\\\", \\\"title\\\": \\\"CROSSAGENTIE: Cross-Type and Cross-Task Multi-Agent LLM Collaboration for Zero-Shot Information Extraction\\\", \\\"status\\\": \\\"mismatch\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"CROSSAGENTIE: Cross-Type and Cross-Task Multi-Agent LLM Collaboration for Zero-Shot Information Extraction\\\", \\\"matched_year\\\": \\\"2025\\\", \\\"mismatch_fields\\\": [\\\"first_author: bib=lu vs api=meng\\\"], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"cmas-ner-2025\\\", \\\"title\\\": \\\"A Cooperative Multi-Agent Framework for Zero-Shot Named Entity Recognition\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"A Cooperative Multi-Agent Framework for Zero-Shot Named Entity Recognition\\\", \\\"matched_year\\\": \\\"2025\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"uniner-2024\\\", \\\"title\\\": \\\"UniversalNER: Targeted Distillation from Large Language Models for Open Named Entity Recognition\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"UniversalNER: Targeted Distillation from Large Language Models for Open Named Entity Recognition\\\", \\\"matched_year\\\": \\\"2023\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"gollie-2024\\\", \\\"title\\\": \\\"GoLLIE: Annotation Guidelines improve Zero-Shot Information-Extraction\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"GoLLIE: Annotation Guidelines improve Zero-Shot Information-Extraction\\\", \\\"matched_year\\\": \\\"2023\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"gliner-2024\\\", \\\"title\\\": \\\"GLiNER: Generalist Model for Named Entity Recognition using Bidirectional Transformer\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"GLiNER: Generalist Model for Named Entity Recognition using Bidirectional Transformer\\\", \\\"matched_year\\\": \\\"2024\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"gliner2-2025\\\", \\\"title\\\": \\\"GLiNER2: Schema-Driven Multi-Task Learning for Structured Information Extraction\\\", \\\"status\\\": \\\"mismatch\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"GLiNER2: Schema-Driven Multi-Task Learning for Structured Information Extraction\\\", \\\"matched_year\\\": \\\"2025\\\", \\\"mismatch_fields\\\": [\\\"first_author: bib=zaratiana vs api=2025\\\"], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"iepile-2024\\\", \\\"title\\\": \\\"IEPile: Unearthing Large Scale Schema-Conditioned Information Extraction Corpus\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"IEPile: Unearthing Large Scale Schema-Conditioned Information Extraction Corpus\\\", \\\"matched_year\\\": \\\"2024\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"dror-2018-significance\\\", \\\"title\\\": \\\"The Hitchhiker's Guide to Testing Statistical Significance in Natural Language Processing\\\", \\\"status\\\": \\\"not_found\\\", \\\"confidence\\\": 0.339, \\\"matched_title\\\": \\\"The Sorcerer II Global Ocean Sampling Expedition: Northwest Atlantic through Eastern Tropical Pacific\\\", \\\"matched_year\\\": \\\"\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"best match similarity 0.34 below threshold 0.82\\\"}, {\\\"key\\\": \\\"lost-in-middle-2024\\\", \\\"title\\\": \\\"Lost in the Middle: How Language Models Use Long Contexts\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Lost in the Middle: How Language Models Use Long Contexts\\\", \\\"matched_year\\\": \\\"2024\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"llm4ie-survey-2024\\\", \\\"title\\\": \\\"Large Language Models for Generative Information Extraction: A Survey\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Large language models for generative information extraction: a survey\\\", \\\"matched_year\\\": \\\"2024\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"knowcoder-2024\\\", \\\"title\\\": \\\"KnowCoder: Coding Structured Knowledge into LLMs for Universal Information Extraction\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"KnowCoder: Coding Structured Knowledge into LLMs for Universal Information Extraction\\\", \\\"matched_year\\\": \\\"2024\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"slot-2025\\\", \\\"title\\\": \\\"SLOT: Structuring the Output of Large Language Models\\\", \\\"status\\\": \\\"mismatch\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"SLOT: Structuring the Output of Large Language Models\\\", \\\"matched_year\\\": \\\"2025\\\", \\\"mismatch_fields\\\": [\\\"first_author: bib=shen vs api=wang\\\"], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"gao-repr-degen-2019\\\", \\\"title\\\": \\\"Representation Degeneration Problem in Training Natural Language Generation Models\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Representation Degeneration Problem in Training Natural Language Generation Models\\\", \\\"matched_year\\\": \\\"2019\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"ethayarajh-contextual-2019\\\", \\\"title\\\": \\\"How Contextual are Contextualized Word Representations? Comparing the Geometry of BERT, ELMo, and GPT-2 Embeddings\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"How Contextual are Contextualized Word Representations? Comparing the Geometry of BERT, ELMo, and GPT-2 Embeddings\\\", \\\"matched_year\\\": \\\"2019\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"cai-isotropy-clusters-2021\\\", \\\"title\\\": \\\"Isotropy in the Contextual Embedding Space: Clusters and Manifolds\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Isotropy in the Contextual Embedding Space: Clusters and Manifolds\\\", \\\"matched_year\\\": \\\"2021\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"instructuie-2023\\\", \\\"title\\\": \\\"InstructUIE: Multi-task Instruction Tuning for Unified Information Extraction\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"InstructUIE: Multi-task Instruction Tuning for Unified Information Extraction\\\", \\\"matched_year\\\": \\\"2023\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"codeie-2023\\\", \\\"title\\\": \\\"CodeIE: Large Code Generation Models are Better Few-Shot Information Extractors\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"CodeIE: Large Code Generation Models are Better Few-Shot Information Extractors\\\", \\\"matched_year\\\": \\\"2023\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"adelie-2024\\\", \\\"title\\\": \\\"ADELIE: Aligning Large Language Models on Information Extraction\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"ADELIE: Aligning Large Language Models on Information Extraction\\\", \\\"matched_year\\\": \\\"2024\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"oneke-2025\\\", \\\"title\\\": \\\"OneKE: A Dockerized Schema-Guided LLM Agent-based Knowledge Extraction System\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"OneKE: A Dockerized Schema-Guided LLM Agent-based Knowledge Extraction System\\\", \\\"matched_year\\\": \\\"2025\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"fewnerd-2021\\\", \\\"title\\\": \\\"Few-NERD: A Few-shot Named Entity Recognition Dataset\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Few-NERD: A Few-shot Named Entity Recognition Dataset\\\", \\\"matched_year\\\": \\\"2021\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"fewrel-2018\\\", \\\"title\\\": \\\"FewRel: A Large-Scale Supervised Few-Shot Relation Classification Dataset with State-of-the-Art Evaluation\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"FewRel: A Large-Scale Supervised Few-Shot Relation Classification Dataset with State-of-the-Art Evaluation\\\", \\\"matched_year\\\": \\\"2018\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"maven-2020\\\", \\\"title\\\": \\\"MAVEN: A Massive General Domain Event Detection Dataset\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"MAVEN: A Massive General Domain Event Detection Dataset\\\", \\\"matched_year\\\": \\\"2020\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"docred-2019\\\", \\\"title\\\": \\\"DocRED: A Large-Scale Document-Level Relation Extraction Dataset\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"DocRED: A Large-Scale Document-Level Relation Extraction Dataset\\\", \\\"matched_year\\\": \\\"2019\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"qwen3-2025\\\", \\\"title\\\": \\\"Qwen3 Technical Report\\\", \\\"status\\\": \\\"mismatch\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Qwen3 Technical Report\\\", \\\"matched_year\\\": \\\"2025\\\", \\\"mismatch_fields\\\": [\\\"first_author: bib=team vs api=yang\\\"], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"llama3-2024\\\", \\\"title\\\": \\\"The Llama 3 Herd of Models\\\", \\\"status\\\": \\\"mismatch\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"The Llama 3 herd of models\\\", \\\"matched_year\\\": \\\"2025\\\", \\\"mismatch_fields\\\": [\\\"first_author: bib=dubey vs api=aaron\\\"], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"sentence-bert-2019\\\", \\\"title\\\": \\\"Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks\\\", \\\"matched_year\\\": \\\"2019\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"minilm-2020\\\", \\\"title\\\": \\\"MiniLM: Deep Self-Attention Distillation for Task-Agnostic Compression of Pre-Trained Transformers\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"MiniLM: Deep Self-Attention Distillation for Task-Agnostic Compression of Pre-Trained Transformers\\\", \\\"matched_year\\\": \\\"2020\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"reflect-learn-2026\\\", \\\"title\\\": \\\"Reflect then Learn: Active Prompting for Information Extraction Guided by Introspective Confusion\\\", \\\"status\\\": \\\"mismatch\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Reflect Then Learn: Active Prompting for Information Extraction Guided by Introspective Confusion\\\", \\\"matched_year\\\": \\\"2026\\\", \\\"mismatch_fields\\\": [\\\"first_author: bib=zhao vs api=2026\\\"], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"sclar-sensitivity-2024\\\", \\\"title\\\": \\\"Quantifying Language Models' Sensitivity to Spurious Features in Prompt Design\\\", \\\"status\\\": \\\"not_found\\\", \\\"confidence\\\": 0.72, \\\"matched_title\\\": \\\"Quantifying Language Models' Sensitivity to Spurious Features in Prompt Design or: How I learned to start worrying about prompt formatting\\\", \\\"matched_year\\\": \\\"\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"best match similarity 0.72 below threshold 0.82\\\"}, {\\\"key\\\": \\\"vllm-2023\\\", \\\"title\\\": \\\"Efficient Memory Management for Large Language Model Serving with PagedAttention\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Efficient Memory Management for Large Language Model Serving with PagedAttention\\\", \\\"matched_year\\\": \\\"2023\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"xie-zeroshot-ner-2023\\\", \\\"title\\\": \\\"Empirical Study of Zero-Shot NER with ChatGPT\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Empirical Study of Zero-Shot NER with ChatGPT\\\", \\\"matched_year\\\": \\\"2023\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"wadhwa-re-llm-2023\\\", \\\"title\\\": \\\"Revisiting Relation Extraction in the era of Large Language Models\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Revisiting Relation Extraction in the era of Large Language Models\\\", \\\"matched_year\\\": \\\"2023\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"relationprompt-2022\\\", \\\"title\\\": \\\"RelationPrompt: Leveraging Prompts to Generate Synthetic Data for Zero-Shot Relation Triplet Extraction\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"RelationPrompt: Leveraging Prompts to Generate Synthetic Data for Zero-Shot Relation Triplet Extraction\\\", \\\"matched_year\\\": \\\"2022\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"promptner-2023\\\", \\\"title\\\": \\\"PromptNER: Prompting For Named Entity Recognition\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"PromptNER: Prompting For Named Entity Recognition\\\", \\\"matched_year\\\": \\\"2023\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"json-schema-bench-2025\\\", \\\"title\\\": \\\"JSONSchemaBench: A Rigorous Benchmark of Structured Outputs for Language Models\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"JSONSchemaBench: A Rigorous Benchmark of Structured Outputs for Language Models\\\", \\\"matched_year\\\": \\\"2025\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"rastogi2020towards\\\", \\\"title\\\": \\\"Towards Scalable Multi-Domain Conversational Agents: The Schema-Guided Dialogue Dataset\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Towards Scalable Multi-Domain Conversational Agents: The Schema-Guided Dialogue Dataset\\\", \\\"matched_year\\\": \\\"2020\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"li2023evaluating\\\", \\\"title\\\": \\\"Evaluating ChatGPT's Information Extraction Capabilities: An Assessment of Performance, Explainability, Calibration, and Faithfulness\\\", \\\"status\\\": \\\"not_found\\\", \\\"confidence\\\": 0.333, \\\"matched_title\\\": \\\"Generative AI in Medical Practice: In-Depth Exploration of Privacy and Security Challenges\\\", \\\"matched_year\\\": \\\"\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"best match similarity 0.33 below threshold 0.82\\\"}, {\\\"key\\\": \\\"lee2022sgd\\\", \\\"title\\\": \\\"SGD-X: A Benchmark for Robust Generalization in Schema-Guided Dialogue Systems\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"SGD-X: A Benchmark for Robust Generalization in Schema-Guided Dialogue Systems\\\", \\\"matched_year\\\": \\\"2022\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"volkanovska2025ner\\\", \\\"title\\\": \\\"A Study of Errors in the Output of Large Language Models for Domain-Specific Few-Shot Named Entity Recognition\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"A Study of Errors in the Output of Large Language Models for Domain-Specific Few-Shot Named Entity Recognition\\\", \\\"matched_year\\\": \\\"2025\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"haystack-to-needle-2025\\\", \\\"title\\\": \\\"From Haystack to Needle: Label Space Reduction for Zero-shot Classification\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"From Haystack to Needle: Label Space Reduction for Zero-shot Classification\\\", \\\"matched_year\\\": \\\"2025\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"cohen-1988-power\\\", \\\"title\\\": \\\"Statistical Power Analysis for the Behavioral Sciences\\\", \\\"status\\\": \\\"mismatch\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Statistical Power Analysis for the Behavioral Sciences\\\", \\\"matched_year\\\": \\\"1989\\\", \\\"mismatch_fields\\\": [\\\"first_author: bib=cohen vs api=muller\\\"], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"lakens-2013-effect-size\\\", \\\"title\\\": \\\"Calculating and Reporting Effect Sizes to Facilitate Cumulative Science: A Practical Primer for t-Tests and ANOVAs\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Calculating and reporting effect sizes to facilitate cumulative science: a practical primer for t-tests and ANOVAs\\\", \\\"matched_year\\\": \\\"2013\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"deng-2010-imagenet\\\", \\\"title\\\": \\\"What Does Classifying More Than 10,000 Image Categories Tell Us?\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"What Does Classifying More Than 10,000 Image Categories Tell Us?\\\", \\\"matched_year\\\": \\\"2010\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"rothman-1990\\\", \\\"title\\\": \\\"No Adjustments Are Needed for Multiple Comparisons\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"No Adjustments Are Needed for Multiple Comparisons\\\", \\\"matched_year\\\": \\\"1990\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"lakens-2017-equivalence\\\", \\\"title\\\": \\\"Equivalence Tests: A Practical Primer for t Tests, Correlations, and Meta-Analyses\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 0.988, \\\"matched_title\\\": \\\"Equivalence Tests: A Practical Primer for t-Tests, Correlations, and Meta-Analyses\\\", \\\"matched_year\\\": \\\"2016\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"zhou-2025-rethinking\\\", \\\"title\\\": \\\"Rethinking Word Similarity: Semantic Similarity through Classification Confusion\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Rethinking Word Similarity: Semantic Similarity through Classification Confusion\\\", \\\"matched_year\\\": \\\"2025\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"guo-2021-label-confusion\\\", \\\"title\\\": \\\"Label Confusion Learning to Enhance Text Classification Models\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Label Confusion Learning to Enhance Text Classification Models\\\", \\\"matched_year\\\": \\\"2021\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"novack-2023-chils\\\", \\\"title\\\": \\\"CHiLS: Zero-Shot Image Classification with Hierarchical Label Sets\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"CHiLS: Zero-Shot Image Classification with Hierarchical Label Sets\\\", \\\"matched_year\\\": \\\"2023\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"cocchieri-2025-zeroner\\\", \\\"title\\\": \\\"ZeroNER: Fueling Zero-Shot Named Entity Recognition via Entity Type Descriptions\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"ZeroNER: Fueling Zero-Shot Named Entity Recognition via Entity Type Descriptions\\\", \\\"matched_year\\\": \\\"2025\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"dlisc-2025\\\", \\\"title\\\": \\\"Effective and Efficient Schema-aware Information Extraction Using On-Device Large Language Models\\\", \\\"status\\\": \\\"mismatch\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Effective and Efficient Schema-aware Information Extraction Using On-Device Large Language Models\\\", \\\"matched_year\\\": \\\"2025\\\", \\\"mismatch_fields\\\": [\\\"first_author: bib=li vs api=wen\\\"], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"spt-2025\\\", \\\"title\\\": \\\"Schema as Parameterized Tools for Universal Information Extraction\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Schema as Parameterized Tools for Universal Information Extraction\\\", \\\"matched_year\\\": \\\"2025\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"card-2020-power\\\", \\\"title\\\": \\\"With Little Power Comes Great Responsibility\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"With Little Power Comes Great Responsibility\\\", \\\"matched_year\\\": \\\"2020\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"gillick-2014-entity-typing\\\", \\\"title\\\": \\\"Context-Dependent Fine-Grained Entity Type Tagging\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Context-Dependent Fine-Grained Entity Type Tagging\\\", \\\"matched_year\\\": \\\"2014\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"schall-2025-hidden-cost\\\", \\\"title\\\": \\\"The Hidden Cost of Structure: How Constrained Decoding Affects Language Model Performance\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"The Hidden Cost of Structure: How Constrained Decoding Affects Language Model Performance\\\", \\\"matched_year\\\": \\\"2025\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"chen-2026-multi-instance\\\", \\\"title\\\": \\\"Understanding LLM Performance Degradation in Multi-Instance Processing: The Roles of Instance Count and Context Length\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Understanding LLM Performance Degradation in Multi-Instance Processing: The Roles of Instance Count and Context Length\\\", \\\"matched_year\\\": \\\"2026\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"wei-2023-chatie\\\", \\\"title\\\": \\\"Zero-Shot Information Extraction via Chatting with ChatGPT\\\", \\\"status\\\": \\\"mismatch\\\", \\\"confidence\\\": 0.935, \\\"matched_title\\\": \\\"ChatIE: Zero-Shot Information Extraction via Chatting with ChatGPT\\\", \\\"matched_year\\\": \\\"2023\\\", \\\"mismatch_fields\\\": [\\\"first_author: bib=wei vs api=xiang\\\"], \\\"note\\\": \\\"\\\"}]}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
      "numLines": 1,
      "startLine": 0,
      "totalLines": 1
    }
  },
  "sourceToolAssistantUUID": "bfab09a1-0481-45b8-8b5e-eaa3259b83af",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_reviewer_2_302b64f9",
  "sessionId": "0ff1fe81-4731-4c76-91b4-02652701ddff",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Tool call

_source line 63 · 2026-05-19T04:32:46.966Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01TtdD7UyEW7oAtNAZZEfCwj`</summary>

```json
{
  "pattern": "ing,|ing\\.",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper",
  "output_mode": "content",
  "glob": "*.tex",
  "-n": true
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e4b0175a-8492-4687-a03b-aba18050d998",
  "isSidechain": false,
  "requestId": "req_011CbBJUHuzquDnpF8L3QWES",
  "type": "assistant",
  "uuid": "f19c277f-4551-476f-9a97-8667bf8ced2f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_reviewer_2_302b64f9",
  "sessionId": "0ff1fe81-4731-4c76-91b4-02652701ddff",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FRC8kBQtFBAvVSwr4XMw4W",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 82,
      "cache_creation_input_tokens": 3326,
      "cache_read_input_tokens": 83533,
      "output_tokens": 689,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3326,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 82,
          "output_tokens": 689,
          "cache_read_input_tokens": 83533,
          "cache_creation_input_tokens": 3326,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3326
          },
          "type": "message"
        }
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

_source line 64 · 2026-05-19T04:32:46.980Z_

<details><summary>↩ Tool result · `toolu_01TtdD7UyEW7oAtNAZZEfCwj`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/related_work.tex:8:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/related_work.tex:10:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex:222:For each embedding, we computed the correlation between mean BCS and candidate confounders (type frequency, degree centrality at threshold 0.7) across MAVEN's 149 active event types. The dominant confound differs by embedding:
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex:273:\caption{Batch composition on FewRel 80-relation RE with oracle routing. $^\dagger$Mean $\pm$ SD across 15 random seeds.}
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex:321:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex:420:\caption{Pearson correlation between SCS and empirical confusion rate. ``Def'' concatenates type name with definition before embedding. All correlations significant ($p < 0.001$). The inconsistent direction of $\Delta r$ indicates that definitions provide no systematic benefit.}
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex:448:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex:607:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/checklist.tex:75:Yes. \S\ref{sec:model} specifies vLLM v0.20.2 for model serving. Embedding models are named with version identifiers (\S\ref{sec:scs}). Code and scripts will be released upon acceptance.
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/checklist.tex:111:Yes. See A4 above. AI assistants were used for code development and document formatting. The research design, execution, and interpretation are the authors' own work.
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/prompt_appendix.tex:12:All prompts are injected into a single \texttt{user} message (no system prompt); the model's chat template adds the system/assistant framing.
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/experimental_setup.tex:10:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/experimental_setup.tex:16:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/experimental_setup.tex:82:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex:18:\includegraphics[width=\linewidth]{../../figures/paper/fig_bcs_scaling.pdf}
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/sdgd_negative.tex:9:\paragraph{RE: oracle routing.}
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/sdgd_negative.tex:12:Promising avenues include coarse-to-fine pipelines and retrieval-based routing.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f19c277f-4551-476f-9a97-8667bf8ced2f",
  "isSidechain": false,
  "promptId": "8257bd0e-08b4-4530-aa87-1e185ea40a51",
  "type": "user",
  "uuid": "077e506a-dfc4-4e3c-98bd-4af5377c192d",
  "toolUseResult": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/related_work.tex:8:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/related_work.tex:10:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex:222:For each embedding, we computed the correlation between mean BCS and candidate confounders (type frequency, degree centrality at threshold 0.7) across MAVEN's 149 active event types. The dominant confound differs by embedding:\n/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex:273:\\caption{Batch composition on FewRel 80-relation RE with oracle routing. $^\\dagger$Mean $\\pm$ SD across 15 random seeds.}\n/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex:321:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex:420:\\caption{Pearson correlation between SCS and empirical confusion rate. ``Def'' concatenates type name with definition before embedding. All correlations significant ($p < 0.001$). The inconsistent direction of $\\Delta r$ indicates that definitions provide no systematic benefit.}\n/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex:448:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex:607:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/checklist.tex:75:Yes. \\S\\ref{sec:model} specifies vLLM v0.20.2 for model serving. Embedding models are named with version identifiers (\\S\\ref{sec:scs}). Code and scripts will be released upon acceptance.\n/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/checklist.tex:111:Yes. See A4 above. AI assistants were used for code development and document formatting. The research design, execution, and interpretation are the authors' own work.\n/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/prompt_appendix.tex:12:All prompts are injected into a single \\texttt{user} message (no system prompt); the model's chat template adds the system/assistant framing.\n/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/experimental_setup.tex:10:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/experimental_setup.tex:16:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/experimental_setup.tex:82:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex:18:\\includegraphics[width=\\linewidth]{../../figures/paper/fig_bcs_scaling.pdf}\n/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/sdgd_negative.tex:9:\\paragraph{RE: oracle routing.}\n/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/sdgd_negative.tex:12:Promising avenues include coarse-to-fine pipelines and retrieval-based routing.",
    "numLines": 17
  },
  "sourceToolAssistantUUID": "f19c277f-4551-476f-9a97-8667bf8ced2f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_reviewer_2_302b64f9",
  "sessionId": "0ff1fe81-4731-4c76-91b4-02652701ddff",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Tool call

_source line 65 · 2026-05-19T04:32:48.323Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01AgD3B3A3XdryGQ5TNFjz6u`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper && cat main.tex abstract.tex introduction.tex related_work.tex experimental_setup.tex results.tex sdgd_negative.tex discussion.tex | wc -l",
  "description": "Count total lines in main body tex files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "077e506a-dfc4-4e3c-98bd-4af5377c192d",
  "isSidechain": false,
  "requestId": "req_011CbBJUHuzquDnpF8L3QWES",
  "type": "assistant",
  "uuid": "aa07c375-6c46-4372-a9ae-e137fb4333de",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_reviewer_2_302b64f9",
  "sessionId": "0ff1fe81-4731-4c76-91b4-02652701ddff",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FRC8kBQtFBAvVSwr4XMw4W",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 82,
      "cache_creation_input_tokens": 3326,
      "cache_read_input_tokens": 83533,
      "output_tokens": 689,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3326,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 82,
          "output_tokens": 689,
          "cache_read_input_tokens": 83533,
          "cache_creation_input_tokens": 3326,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3326
          },
          "type": "message"
        }
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

_source line 66_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[Round 1 审稿请求]: ## Round 1 审稿任务 — Reviewer 2（新颖性 + Related Work 完整性 + 写作质量 + 格式合规）  ### Venue 信息 - **目标会议**: EMNLP 2026（通过 ARR May 2026 cycle 提交） - **截止日期**: 2026-05-25 - **页数限制**: Long paper, 正文 ≤ 8…",
  "leafUuid": "aa07c375-6c46-4372-a9ae-e137fb4333de",
  "sessionId": "0ff1fe81-4731-4c76-91b4-02652701ddff"
}
```

---


### Runtime record

_source line 67_

```json
{
  "type": "ai-title",
  "aiTitle": "Review Round 1 schema-dag-extraction paper for EMNLP 2026",
  "sessionId": "0ff1fe81-4731-4c76-91b4-02652701ddff"
}
```

---


### Tool result

_source line 68 · 2026-05-19T04:32:48.523Z_

<details><summary>↩ Tool result · `toolu_01AgD3B3A3XdryGQ5TNFjz6u`</summary>

```text
950
Shell cwd was reset to /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_reviewer_2_302b64f9
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "aa07c375-6c46-4372-a9ae-e137fb4333de",
  "isSidechain": false,
  "promptId": "8257bd0e-08b4-4530-aa87-1e185ea40a51",
  "type": "user",
  "uuid": "79e6474a-f647-4797-9f64-f0fd19763e9d",
  "toolUseResult": {
    "stdout": "950",
    "stderr": "\nShell cwd was reset to /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_reviewer_2_302b64f9",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "aa07c375-6c46-4372-a9ae-e137fb4333de",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_reviewer_2_302b64f9",
  "sessionId": "0ff1fe81-4731-4c76-91b4-02652701ddff",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Runtime record

_source line 69 · 2026-05-19T04:32:48.527Z_

```json
{
  "parentUuid": "79e6474a-f647-4797-9f64-f0fd19763e9d",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "247a612c-303b-4053-a92d-0f3daf7c1ca8",
  "timestamp": "2026-05-19T04:32:48.527Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_reviewer_2_302b64f9",
  "sessionId": "0ff1fe81-4731-4c76-91b4-02652701ddff",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---


### Assistant

_source line 70 · 2026-05-19T04:32:52.694Z_

<details><summary>Logged reasoning block</summary>

```text
Now let me compile the full review. Let me also check if the paper compiles and check page count through looking at the PDF or estimating from the tex files.

Let me compile the paper to check page count.

Actually, let me check if there's a compiled PDF already.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "247a612c-303b-4053-a92d-0f3daf7c1ca8",
  "isSidechain": false,
  "requestId": "req_011CbBJV7VTmwvSKp9NsJDYi",
  "type": "assistant",
  "uuid": "91dac802-da16-4f37-b286-a28713dffb53",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_reviewer_2_302b64f9",
  "sessionId": "0ff1fe81-4731-4c76-91b4-02652701ddff",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01J9aWFptcBRTx8Y2kZRDAS4",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 22409,
      "cache_read_input_tokens": 86859,
      "output_tokens": 273,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 22409,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 273,
          "cache_read_input_tokens": 86859,
          "cache_creation_input_tokens": 22409,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 22409
          },
          "type": "message"
        }
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

_source line 71 · 2026-05-19T04:32:53.177Z_

检查是否有已编译的 PDF 及其页数。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "91dac802-da16-4f37-b286-a28713dffb53",
  "isSidechain": false,
  "requestId": "req_011CbBJV7VTmwvSKp9NsJDYi",
  "type": "assistant",
  "uuid": "794d4d59-9512-4178-b6a7-d5b3a0844f47",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_reviewer_2_302b64f9",
  "sessionId": "0ff1fe81-4731-4c76-91b4-02652701ddff",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01J9aWFptcBRTx8Y2kZRDAS4",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 22409,
      "cache_read_input_tokens": 86859,
      "output_tokens": 273,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 22409,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 273,
          "cache_read_input_tokens": 86859,
          "cache_creation_input_tokens": 22409,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 22409
          },
          "type": "message"
        }
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

_source line 72 · 2026-05-19T04:32:54.241Z_

<details open><summary>🔧 Tool call — Glob · `toolu_016Vusbea2AH8BrUwFs8Caa8`</summary>

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
  "parentUuid": "794d4d59-9512-4178-b6a7-d5b3a0844f47",
  "isSidechain": false,
  "requestId": "req_011CbBJV7VTmwvSKp9NsJDYi",
  "type": "assistant",
  "uuid": "c81e603f-223d-4e34-a414-05b952be69da",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_reviewer_2_302b64f9",
  "sessionId": "0ff1fe81-4731-4c76-91b4-02652701ddff",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01J9aWFptcBRTx8Y2kZRDAS4",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 22409,
      "cache_read_input_tokens": 86859,
      "output_tokens": 273,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 22409,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 273,
          "cache_read_input_tokens": 86859,
          "cache_creation_input_tokens": 22409,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 22409
          },
          "type": "message"
        }
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

_source line 73 · 2026-05-19T04:32:54.518Z_

<details><summary>↩ Tool result · `toolu_01U3hvQrUgsHYFjCyhwxibBd`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260515T053106/best/paper.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260515T053106/median/paper.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260515T053106/worst/paper.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260515T113743/best/paper.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260515T113743/median/paper.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260515T113743/worst/paper.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260515T140829/best/paper.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260515T140829/median/paper.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260515T140829/worst/paper.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/_project/chart/fig_count_curves.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/_project/chart/fig_count_curves_73bdd4.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/_project/chart/fig_error_taxonomy.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/_project/chart/fig_bcs_scaling.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/figures/paper/fig_sdgd_comparison.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/exp008_sdgd_zero_fewnerd_r2/chart/fig_sdgd_comparison.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.venv/lib/python3.14/site-packages/matplotlib/mpl-data/images/back.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.venv/lib/python3.14/site-packages/matplotlib/mpl-data/images/filesave.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.venv/lib/python3.14/site-packages/matplotlib/mpl-data/images/forward.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.venv/lib/python3.14/site-packages/matplotlib/mpl-data/images/hand.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.venv/lib/python3.14/site-packages/matplotlib/mpl-data/images/help.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.venv/lib/python3.14/site-packages/matplotlib/mpl-data/images/home.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.venv/lib/python3.14/site-packages/matplotlib/mpl-data/images/matplotlib.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.venv/lib/python3.14/site-packages/matplotlib/mpl-data/images/move.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.venv/lib/python3.14/site-packages/matplotlib/mpl-data/images/qt4_editor_options.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.venv/lib/python3.14/site-packages/matplotlib/mpl-data/images/subplots.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.venv/lib/python3.14/site-packages/matplotlib/mpl-data/images/zoom_to_rect.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/figures/paper/fig_re_channels.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/figures/paper/fig_re_dual_panel.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260516T073533/best/paper.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260516T073533/median/paper.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260516T073533/worst/paper.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/_project/chart/fig_count_curves_a6acd7.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/_project/chart/fig_bcs_scaling_482351.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/_project/chart/fig_error_taxonomy_d056dd.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/figures/paper/fig_error_taxonomy.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/figures/paper/fig_count_curves.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/figures/paper/fig_bcs_scaling.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.pdf
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bff012f1-49b4-45cb-b2e2-0a9f8628c3e7",
  "isSidechain": false,
  "promptId": "8257bd0e-08b4-4530-aa87-1e185ea40a51",
  "type": "user",
  "uuid": "da54be52-f442-420e-8b1a-4be1f9440fbb",
  "toolUseResult": {
    "filenames": [
      "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260515T053106/best/paper.pdf",
      "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260515T053106/median/paper.pdf",
      "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260515T053106/worst/paper.pdf",
      "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260515T113743/best/paper.pdf",
      "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260515T113743/median/paper.pdf",
      "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260515T113743/worst/paper.pdf",
      "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260515T140829/best/paper.pdf",
      "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260515T140829/median/paper.pdf",
      "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260515T140829/worst/paper.pdf",
      "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/_project/chart/fig_count_curves.pdf",
      "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/_project/chart/fig_count_curves_73bdd4.pdf",
      "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/_project/chart/fig_error_taxonomy.pdf",
      "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/_project/chart/fig_bcs_scaling.pdf",
      "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/figures/paper/fig_sdgd_comparison.pdf",
      "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/exp008_sdgd_zero_fewnerd_r2/chart/fig_sdgd_comparison.pdf",
      "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.venv/lib/python3.14/site-packages/matplotlib/mpl-data/images/back.pdf",
      "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.venv/lib/python3.14/site-packages/matplotlib/mpl-data/images/filesave.pdf",
      "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.venv/lib/python3.14/site-packages/matplotlib/mpl-data/images/forward.pdf",
      "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.venv/lib/python3.14/site-packages/matplotlib/mpl-data/images/hand.pdf",
      "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.venv/lib/python3.14/site-packages/matplotlib/mpl-data/images/help.pdf",
      "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.venv/lib/python3.14/site-packages/matplotlib/mpl-data/images/home.pdf",
      "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.venv/lib/python3.14/site-packages/matplotlib/mpl-data/images/matplotlib.pdf",
      "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.venv/lib/python3.14/site-packages/matplotlib/mpl-data/images/move.pdf",
      "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.venv/lib/python3.14/site-packages/matplotlib/mpl-data/images/qt4_editor_options.pdf",
      "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.venv/lib/python3.14/site-packages/matplotlib/mpl-data/images/subplots.pdf",
      "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.venv/lib/python3.14/site-packages/matplotlib/mpl-data/images/zoom_to_rect.pdf",
      "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/figures/paper/fig_re_channels.pdf",
      "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/figures/paper/fig_re_dual_panel.pdf",
      "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260516T073533/best/paper.pdf",
      "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260516T073533/median/paper.pdf",
      "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260516T073533/worst/paper.pdf",
      "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/_project/chart/fig_count_curves_a6acd7.pdf",
      "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/_project/chart/fig_bcs_scaling_482351.pdf",
      "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/_project/chart/fig_error_taxonomy_d056dd.pdf",
      "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/figures/paper/fig_error_taxonomy.pdf",
      "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/figures/paper/fig_count_curves.pdf",
      "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/figures/paper/fig_bcs_scaling.pdf",
      "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.pdf"
    ],
    "durationMs": 34,
    "numFiles": 38,
    "truncated": false
  },
  "sourceToolAssistantUUID": "bff012f1-49b4-45cb-b2e2-0a9f8628c3e7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_reviewer_2_302b64f9",
  "sessionId": "0ff1fe81-4731-4c76-91b4-02652701ddff",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Tool result

_source line 74 · 2026-05-19T04:32:54.265Z_

<details><summary>↩ Tool result · `toolu_016Vusbea2AH8BrUwFs8Caa8`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.pdf
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c81e603f-223d-4e34-a414-05b952be69da",
  "isSidechain": false,
  "promptId": "8257bd0e-08b4-4530-aa87-1e185ea40a51",
  "type": "user",
  "uuid": "12d1f15a-7543-424d-b66d-7e71631fda06",
  "toolUseResult": {
    "filenames": [
      "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.pdf"
    ],
    "durationMs": 13,
    "numFiles": 1,
    "truncated": false
  },
  "sourceToolAssistantUUID": "c81e603f-223d-4e34-a414-05b952be69da",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_reviewer_2_302b64f9",
  "sessionId": "0ff1fe81-4731-4c76-91b4-02652701ddff",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Tool call

_source line 75 · 2026-05-19T04:32:54.478Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01U3hvQrUgsHYFjCyhwxibBd`</summary>

```json
{
  "pattern": "**/*.pdf",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "12d1f15a-7543-424d-b66d-7e71631fda06",
  "isSidechain": false,
  "requestId": "req_011CbBJV7VTmwvSKp9NsJDYi",
  "type": "assistant",
  "uuid": "bff012f1-49b4-45cb-b2e2-0a9f8628c3e7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_reviewer_2_302b64f9",
  "sessionId": "0ff1fe81-4731-4c76-91b4-02652701ddff",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01J9aWFptcBRTx8Y2kZRDAS4",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 22409,
      "cache_read_input_tokens": 86859,
      "output_tokens": 273,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 22409,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 273,
          "cache_read_input_tokens": 86859,
          "cache_creation_input_tokens": 22409,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 22409
          },
          "type": "message"
        }
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

_source line 76 · 2026-05-19T04:32:58.234Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images · `toolu_01CwsuaTARvjVkhoPQZWxzAS`</summary>

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
  "parentUuid": "da54be52-f442-420e-8b1a-4be1f9440fbb",
  "isSidechain": false,
  "requestId": "req_011CbBJVZDXae65gHPXzJMME",
  "type": "assistant",
  "uuid": "e3809859-ee29-4f25-a501-ccc374795495",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_reviewer_2_302b64f9",
  "sessionId": "0ff1fe81-4731-4c76-91b4-02652701ddff",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016G9DhYDQAkinwUrLNUDaAP",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2228,
      "cache_read_input_tokens": 109268,
      "output_tokens": 137,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2228,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 137,
          "cache_read_input_tokens": 109268,
          "cache_creation_input_tokens": 2228,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2228
          },
          "type": "message"
        }
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

_source line 77 · 2026-05-19T04:33:01.290Z_

<details><summary>↩ Tool result · `toolu_01CwsuaTARvjVkhoPQZWxzAS`</summary>

```text
Error: result (5,415,707 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-18-projects-schema-dag-extraction--claude-sessions-review-reviewer-2-302b64f9/0ff1fe81-4731-4c76-91b4-02652701ddff/tool-results/mcp-agent-ml-research-pdf_to_images-1779165181270.txt.
Format: JSON with schema: {result: string}
Use offset and limit parameters to read specific portions of the file, search within it for specific content, and jq to make structured queries.
REQUIREMENTS FOR SUMMARIZATION/ANALYSIS/REVIEW:
- You MUST read the content from the file at /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-18-projects-schema-dag-extraction--claude-sessions-review-reviewer-2-302b64f9/0ff1fe81-4731-4c76-91b4-02652701ddff/tool-results/mcp-agent-ml-research-pdf_to_images-1779165181270.txt in sequential chunks until 100% of the content has been read.
- If you receive truncation warnings when reading the file, reduce the chunk size until you have read 100% of the content without truncation.
- Before producing ANY summary or analysis, you MUST explicitly describe what portion of the content you have read. ***If you did not read the entire content, you MUST explicitly state this.***

```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e3809859-ee29-4f25-a501-ccc374795495",
  "isSidechain": false,
  "promptId": "8257bd0e-08b4-4530-aa87-1e185ea40a51",
  "type": "user",
  "uuid": "dbeae498-2886-4f80-a09e-aaba2e1f6525",
  "toolUseResult": "Error: result (5,415,707 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-18-projects-schema-dag-extraction--claude-sessions-review-reviewer-2-302b64f9/0ff1fe81-4731-4c76-91b4-02652701ddff/tool-results/mcp-agent-ml-research-pdf_to_images-1779165181270.txt.\nFormat: JSON with schema: {result: string}\nUse offset and limit parameters to read specific portions of the file, search within it for specific content, and jq to make structured queries.\nREQUIREMENTS FOR SUMMARIZATION/ANALYSIS/REVIEW:\n- You MUST read the content from the file at /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-18-projects-schema-dag-extraction--claude-sessions-review-reviewer-2-302b64f9/0ff1fe81-4731-4c76-91b4-02652701ddff/tool-results/mcp-agent-ml-research-pdf_to_images-1779165181270.txt in sequential chunks until 100% of the content has been read.\n- If you receive truncation warnings when reading the file, reduce the chunk size until you have read 100% of the content without truncation.\n- Before producing ANY summary or analysis, you MUST explicitly describe what portion of the content you have read. ***If you did not read the entire content, you MUST explicitly state this.***\n",
  "mcpMeta": {
    "storage": "sanitized-trace-archive",
    "source_line": 77,
    "serialized_bytes": 5415744,
    "serialized_sha256": "89642f02331940d41c645865e6a806707006916d49452642b3107228d3b1d392",
    "note": "Complete sanitized source is retained in trace-files.tar.gz."
  },
  "sourceToolAssistantUUID": "e3809859-ee29-4f25-a501-ccc374795495",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_reviewer_2_302b64f9",
  "sessionId": "0ff1fe81-4731-4c76-91b4-02652701ddff",
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
  "lastPrompt": "[Round 1 审稿请求]: ## Round 1 审稿任务 — Reviewer 2（新颖性 + Related Work 完整性 + 写作质量 + 格式合规）  ### Venue 信息 - **目标会议**: EMNLP 2026（通过 ARR May 2026 cycle 提交） - **截止日期**: 2026-05-25 - **页数限制**: Long paper, 正文 ≤ 8…",
  "leafUuid": "dbeae498-2886-4f80-a09e-aaba2e1f6525",
  "sessionId": "0ff1fe81-4731-4c76-91b4-02652701ddff"
}
```

---


### Runtime record

_source line 79_

```json
{
  "type": "ai-title",
  "aiTitle": "Review Round 1 schema-dag-extraction paper for EMNLP 2026",
  "sessionId": "0ff1fe81-4731-4c76-91b4-02652701ddff"
}
```

---


### Assistant

_source line 80 · 2026-05-19T04:33:04.283Z_

<details><summary>Logged reasoning block</summary>

```text
The PDF images are too large. Let me try with fewer pages or lower DPI.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dbeae498-2886-4f80-a09e-aaba2e1f6525",
  "isSidechain": false,
  "requestId": "req_011CbBJW4Hkk6ycnNroFyBWq",
  "type": "assistant",
  "uuid": "538e899e-f595-4874-8737-cb8eeb3149cb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_reviewer_2_302b64f9",
  "sessionId": "0ff1fe81-4731-4c76-91b4-02652701ddff",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013G72A94MUXRqeoDEALrmxj",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 537,
      "cache_read_input_tokens": 111496,
      "output_tokens": 420,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 537,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 420,
          "cache_read_input_tokens": 111496,
          "cache_creation_input_tokens": 537,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 537
          },
          "type": "message"
        }
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

_source line 81 · 2026-05-19T04:33:05.297Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images · `toolu_01HtJgd8mfqQe3q45tP3zCYM`</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.pdf",
  "pages": "1-3",
  "dpi": 150
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "538e899e-f595-4874-8737-cb8eeb3149cb",
  "isSidechain": false,
  "requestId": "req_011CbBJW4Hkk6ycnNroFyBWq",
  "type": "assistant",
  "uuid": "ae635248-bc77-43ff-b2c2-20a1f2f1cb7a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_reviewer_2_302b64f9",
  "sessionId": "0ff1fe81-4731-4c76-91b4-02652701ddff",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013G72A94MUXRqeoDEALrmxj",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 537,
      "cache_read_input_tokens": 111496,
      "output_tokens": 420,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 537,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 420,
          "cache_read_input_tokens": 111496,
          "cache_creation_input_tokens": 537,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 537
          },
          "type": "message"
        }
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

_source line 82 · 2026-05-19T04:33:06.359Z_

<details><summary>↩ Tool result · `toolu_01HtJgd8mfqQe3q45tP3zCYM`</summary>

```text
Error: result (2,151,933 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-18-projects-schema-dag-extraction--claude-sessions-review-reviewer-2-302b64f9/0ff1fe81-4731-4c76-91b4-02652701ddff/tool-results/mcp-agent-ml-research-pdf_to_images-1779165186355.txt.
Format: JSON with schema: {result: string}
Use offset and limit parameters to read specific portions of the file, search within it for specific content, and jq to make structured queries.
REQUIREMENTS FOR SUMMARIZATION/ANALYSIS/REVIEW:
- You MUST read the content from the file at /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-18-projects-schema-dag-extraction--claude-sessions-review-reviewer-2-302b64f9/0ff1fe81-4731-4c76-91b4-02652701ddff/tool-results/mcp-agent-ml-research-pdf_to_images-1779165186355.txt in sequential chunks until 100% of the content has been read.
- If you receive truncation warnings when reading the file, reduce the chunk size until you have read 100% of the content without truncation.
- Before producing ANY summary or analysis, you MUST explicitly describe what portion of the content you have read. ***If you did not read the entire content, you MUST explicitly state this.***

```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ae635248-bc77-43ff-b2c2-20a1f2f1cb7a",
  "isSidechain": false,
  "promptId": "8257bd0e-08b4-4530-aa87-1e185ea40a51",
  "type": "user",
  "uuid": "5bd86d7b-4426-40f5-b64a-e64a5ccb4901",
  "toolUseResult": "Error: result (2,151,933 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-18-projects-schema-dag-extraction--claude-sessions-review-reviewer-2-302b64f9/0ff1fe81-4731-4c76-91b4-02652701ddff/tool-results/mcp-agent-ml-research-pdf_to_images-1779165186355.txt.\nFormat: JSON with schema: {result: string}\nUse offset and limit parameters to read specific portions of the file, search within it for specific content, and jq to make structured queries.\nREQUIREMENTS FOR SUMMARIZATION/ANALYSIS/REVIEW:\n- You MUST read the content from the file at /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-18-projects-schema-dag-extraction--claude-sessions-review-reviewer-2-302b64f9/0ff1fe81-4731-4c76-91b4-02652701ddff/tool-results/mcp-agent-ml-research-pdf_to_images-1779165186355.txt in sequential chunks until 100% of the content has been read.\n- If you receive truncation warnings when reading the file, reduce the chunk size until you have read 100% of the content without truncation.\n- Before producing ANY summary or analysis, you MUST explicitly describe what portion of the content you have read. ***If you did not read the entire content, you MUST explicitly state this.***\n",
  "mcpMeta": {
    "storage": "sanitized-trace-archive",
    "source_line": 82,
    "serialized_bytes": 2151970,
    "serialized_sha256": "30abc7021407418293805ed652fe68206b590518d37392a976200aa8d8857548",
    "note": "Complete sanitized source is retained in trace-files.tar.gz."
  },
  "sourceToolAssistantUUID": "ae635248-bc77-43ff-b2c2-20a1f2f1cb7a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_reviewer_2_302b64f9",
  "sessionId": "0ff1fe81-4731-4c76-91b4-02652701ddff",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Tool call

_source line 83 · 2026-05-19T04:33:07.304Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01R8FDv7NssE2uwcGfDxFNxM`</summary>

```json
{
  "command": "python3 -c \"\nimport subprocess\nresult = subprocess.run(['pdfinfo', '/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.pdf'], capture_output=True, text=True)\nprint(result.stdout)\nprint(result.stderr)\n\" 2>&1 || echo \"pdfinfo not available, trying pdftotext\" && python3 -c \"\ntry:\n    import fitz\n    doc = fitz.open('/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.pdf')\n    print(f'Total pages: {len(doc)}')\n    doc.close()\nexcept:\n    print('Cannot determine page count')\n\"",
  "description": "Get PDF page count"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5bd86d7b-4426-40f5-b64a-e64a5ccb4901",
  "isSidechain": false,
  "requestId": "req_011CbBJW4Hkk6ycnNroFyBWq",
  "type": "assistant",
  "uuid": "6de47cc2-714a-4792-8c40-d51d374c2621",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_reviewer_2_302b64f9",
  "sessionId": "0ff1fe81-4731-4c76-91b4-02652701ddff",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013G72A94MUXRqeoDEALrmxj",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 537,
      "cache_read_input_tokens": 111496,
      "output_tokens": 420,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 537,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 420,
          "cache_read_input_tokens": 111496,
          "cache_creation_input_tokens": 537,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 537
          },
          "type": "message"
        }
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
  "lastPrompt": "[Round 1 审稿请求]: ## Round 1 审稿任务 — Reviewer 2（新颖性 + Related Work 完整性 + 写作质量 + 格式合规）  ### Venue 信息 - **目标会议**: EMNLP 2026（通过 ARR May 2026 cycle 提交） - **截止日期**: 2026-05-25 - **页数限制**: Long paper, 正文 ≤ 8…",
  "leafUuid": "6de47cc2-714a-4792-8c40-d51d374c2621",
  "sessionId": "0ff1fe81-4731-4c76-91b4-02652701ddff"
}
```

---


### Runtime record

_source line 85_

```json
{
  "type": "ai-title",
  "aiTitle": "Review Round 1 schema-dag-extraction paper for EMNLP 2026",
  "sessionId": "0ff1fe81-4731-4c76-91b4-02652701ddff"
}
```

---


### Tool result

_source line 86 · 2026-05-19T04:33:07.726Z_

<details><summary>↩ Tool result · `toolu_01R8FDv7NssE2uwcGfDxFNxM`</summary>

```text
Title:           
Subject:         
Keywords:        
Author:          
Creator:         LaTeX with hyperref
Producer:        pdfTeX-1.40.28
CreationDate:    Tue May 19 01:50:40 2026 UTC
ModDate:         Tue May 19 01:50:40 2026 UTC
Custom Metadata: yes
Metadata Stream: no
Tagged:          no
UserProperties:  no
Suspects:        no
Form:            none
JavaScript:      no
Pages:           25
Encrypted:       no
Page size:       595.276 x 841.89 pts (A4)
Page rot:        0
File size:       491338 bytes
Optimized:       no
PDF version:     1.7


Total pages: 25
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6de47cc2-714a-4792-8c40-d51d374c2621",
  "isSidechain": false,
  "promptId": "8257bd0e-08b4-4530-aa87-1e185ea40a51",
  "type": "user",
  "uuid": "f01f320f-dfb1-4e0c-a19e-207a3002e792",
  "toolUseResult": {
    "stdout": "Title:           \nSubject:         \nKeywords:        \nAuthor:          \nCreator:         LaTeX with hyperref\nProducer:        pdfTeX-1.40.28\nCreationDate:    Tue May 19 01:50:40 2026 UTC\nModDate:         Tue May 19 01:50:40 2026 UTC\nCustom Metadata: yes\nMetadata Stream: no\nTagged:          no\nUserProperties:  no\nSuspects:        no\nForm:            none\nJavaScript:      no\nPages:           25\nEncrypted:       no\nPage size:       595.276 x 841.89 pts (A4)\nPage rot:        0\nFile size:       491338 bytes\nOptimized:       no\nPDF version:     1.7\n\n\nTotal pages: 25",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "6de47cc2-714a-4792-8c40-d51d374c2621",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_reviewer_2_302b64f9",
  "sessionId": "0ff1fe81-4731-4c76-91b4-02652701ddff",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Assistant

_source line 87 · 2026-05-19T04:33:11.628Z_

<details><summary>Logged reasoning block</summary>

```text
OK, the PDF is 25 pages total. I need to determine how many pages are the main body (before references/appendix). Let me render individual pages to check.

Let me try one page at a time at lower DPI.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f01f320f-dfb1-4e0c-a19e-207a3002e792",
  "isSidechain": false,
  "requestId": "req_011CbBJWXXrX4ojxV12ZRmMg",
  "type": "assistant",
  "uuid": "681bc867-7358-4a86-a566-3d8d373dd6ea",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_reviewer_2_302b64f9",
  "sessionId": "0ff1fe81-4731-4c76-91b4-02652701ddff",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011yPUjhTakQHBeSzdD4tmTw",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1067,
      "cache_read_input_tokens": 112033,
      "output_tokens": 470,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1067,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 470,
          "cache_read_input_tokens": 112033,
          "cache_creation_input_tokens": 1067,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1067
          },
          "type": "message"
        }
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

_source line 88 · 2026-05-19T04:33:12.114Z_

PDF 共 25 页。需要确认正文页数。逐页渲染关键页面检查布局。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "681bc867-7358-4a86-a566-3d8d373dd6ea",
  "isSidechain": false,
  "requestId": "req_011CbBJWXXrX4ojxV12ZRmMg",
  "type": "assistant",
  "uuid": "62beae27-1ac1-4f56-94a5-3ca215e93382",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_reviewer_2_302b64f9",
  "sessionId": "0ff1fe81-4731-4c76-91b4-02652701ddff",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011yPUjhTakQHBeSzdD4tmTw",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1067,
      "cache_read_input_tokens": 112033,
      "output_tokens": 470,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1067,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 470,
          "cache_read_input_tokens": 112033,
          "cache_creation_input_tokens": 1067,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1067
          },
          "type": "message"
        }
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

_source line 89 · 2026-05-19T04:33:13.115Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images · `toolu_01GoD3Wi1hCRh7DiWuBN1ry4`</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.pdf",
  "pages": "7",
  "dpi": 150
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "62beae27-1ac1-4f56-94a5-3ca215e93382",
  "isSidechain": false,
  "requestId": "req_011CbBJWXXrX4ojxV12ZRmMg",
  "type": "assistant",
  "uuid": "afd48b68-452a-4e12-b447-b8f377c6e39b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_reviewer_2_302b64f9",
  "sessionId": "0ff1fe81-4731-4c76-91b4-02652701ddff",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011yPUjhTakQHBeSzdD4tmTw",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1067,
      "cache_read_input_tokens": 112033,
      "output_tokens": 470,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1067,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 470,
          "cache_read_input_tokens": 112033,
          "cache_creation_input_tokens": 1067,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1067
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---
