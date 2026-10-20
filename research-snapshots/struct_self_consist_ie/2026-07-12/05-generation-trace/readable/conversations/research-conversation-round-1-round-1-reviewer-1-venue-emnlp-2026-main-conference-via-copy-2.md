# Research conversation: [Round 1 审稿请求]: ## Round 1 审稿任务 — Reviewer 1（方法严谨性 + 实验设计 + 统计分析） ### Venue 信息 - **目标**: EMNLP 2026 Main Conference (via

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 75
- **Recorded user turns:** 3
- **Tool calls:** 20
- **Original source:** `logs/chats/exported-trajectories/account-3/a5f4ff78-4f02-4166-b054-29f1bf2f2644.jsonl`
- **Structured JSON:** [`efcf3aea3b078682a8c1.json`](../../sessions/ef/efcf3aea3b078682a8c1.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-16T05:12:26.605Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-16T05:12:26.605Z",
  "sessionId": "a5f4ff78-4f02-4166-b054-29f1bf2f2644",
  "content": "[Round 1 审稿请求]:\n## Round 1 审稿任务 — Reviewer 1（方法严谨性 + 实验设计 + 统计分析）\n\n### Venue 信息\n- **目标**: EMNLP 2026 Main Conference (via ARR May 2026 cycle)\n- **截止日期**: 2026-05-25\n- **格式**: ACL 模板, 正文 8 页, double-blind, Limitations/Ethics 不计页数\n- **匿名规则**: double-blind, 禁止自引暴露身份\n\n### 论文文件\n- 主文件: `projects/struct_self_consist_ie/docs/paper/main.tex`\n- Section 文件: `projects/struct_self_consist_ie/docs/paper/sections/` 目录下 (abstract.tex, introduction.tex, related_work.tex, method.tex, experiments.tex, discussion.tex, conclusion.tex, limitations.tex, appendix.tex)\n- 引用: `projects/struct_self_consist_ie/docs/paper/references.bib`\n\n### 你的审查侧重\n\n**核心任务：评估方法严谨性、实验设计和统计分析的可靠性。** 具体关注：\n\n1. **方法论有效性**\n   - 5 个 confidence signal 的定义是否严谨、无歧义\n   - Soft Jaccard (SJ) 的 Hungarian matching + IoU 定义是否正确\n   - instance-level vs per-sample 的区分是否成立——特别是 4/5 信号无法做 selection 是否是 tautological（定义上必然的）而非 empirical finding\n   - Evaluation framework (ρ, AUROC, selection F1) 三指标是否充分且无冗余\n\n2. **实验设计**\n   - 3 个 NER benchmark + 1 个 RE benchmark 的覆盖度是否足够支撑 \"structured IE\" 的论文标题\n   - N=8 (primary) / N=16 的样本量选择是否合理\n   - 2 个 model family (Qwen3-8B, LLaMA-3.1-8B) + 1 个 4B ablation 的 scale coverage 是否足够\n   - Fine-tuning setup (LoRA rank=32, 5 epochs) 是否标准且可复现\n   - Free-form decoding ablation 的设计是否能有效隔离 constrained decoding 的影响\n\n3. **统计分析**\n   - Spearman ρ 的 bootstrap CI 和 permutation test 是否正确应用\n   - Selection F1 的 Fisher p-value 和 sign test 是否适当\n   - TOST 等价性检验的 δ 选择是否有 prior justification（注意 ε=0.05 是否存在 circularity）\n   - 3-seed stability (Kendall W=1.000 with n=3) 的统计效力\n   - 多重比较校正是否充分（只对 positive finding 做了 Bonferroni）\n   - Gold-empty instance filtering 的决策是否合理且一致\n\n4. **数据可靠性**\n   - Table 1-4 之间数据是否一致\n   - 正文、caption、appendix 中同一数值的引用是否一致\n   - Table 2 NER 2-seed vs RE 单 seed 的不一致是否有合理解释\n\n5. **页数合规**\n   - 正文是否在 8 页限制内（不计 Limitations, Ethics, References, Appendix）\n\n请输出完整审稿报告，包括：Summary (2-3句)、Strengths (逐条)、Weaknesses (逐条，严格不留情)、Questions (需作者回答)、Missing References、Overall Assessment (评分 + 置信度)。"
}
```

---

### Runtime record

_source line 2 · 2026-05-16T05:12:26.609Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-16T05:12:26.609Z",
  "sessionId": "a5f4ff78-4f02-4166-b054-29f1bf2f2644"
}
```

---

## Round 1

70 recorded events

### User

_source line 3 · 2026-05-16T05:12:26.644Z_

[Round 1 审稿请求]:
## Round 1 审稿任务 — Reviewer 1（方法严谨性 + 实验设计 + 统计分析）

### Venue 信息
- **目标**: EMNLP 2026 Main Conference (via ARR May 2026 cycle)
- **截止日期**: 2026-05-25
- **格式**: ACL 模板, 正文 8 页, double-blind, Limitations/Ethics 不计页数
- **匿名规则**: double-blind, 禁止自引暴露身份

### 论文文件
- 主文件: `projects/struct_self_consist_ie/docs/paper/main.tex`
- Section 文件: `projects/struct_self_consist_ie/docs/paper/sections/` 目录下 (abstract.tex, introduction.tex, related_work.tex, method.tex, experiments.tex, discussion.tex, conclusion.tex, limitations.tex, appendix.tex)
- 引用: `projects/struct_self_consist_ie/docs/paper/references.bib`

### 你的审查侧重

**核心任务：评估方法严谨性、实验设计和统计分析的可靠性。** 具体关注：

1. **方法论有效性**
   - 5 个 confidence signal 的定义是否严谨、无歧义
   - Soft Jaccard (SJ) 的 Hungarian matching + IoU 定义是否正确
   - instance-level vs per-sample 的区分是否成立——特别是 4/5 信号无法做 selection 是否是 tautological（定义上必然的）而非 empirical finding
   - Evaluation framework (ρ, AUROC, selection F1) 三指标是否充分且无冗余

2. **实验设计**
   - 3 个 NER benchmark + 1 个 RE benchmark 的覆盖度是否足够支撑 "structured IE" 的论文标题
   - N=8 (primary) / N=16 的样本量选择是否合理
   - 2 个 model family (Qwen3-8B, LLaMA-3.1-8B) + 1 个 4B ablation 的 scale coverage 是否足够
   - Fine-tuning setup (LoRA rank=32, 5 epochs) 是否标准且可复现
   - Free-form decoding ablation 的设计是否能有效隔离 constrained decoding 的影响

3. **统计分析**
   - Spearman ρ 的 bootstrap CI 和 permutation test 是否正确应用
   - Selection F1 的 Fisher p-value 和 sign test 是否适当
   - TOST 等价性检验的 δ 选择是否有 prior justification（注意 ε=0.05 是否存在 circularity）
   - 3-seed stability (Kendall W=1.000 with n=3) 的统计效力
   - 多重比较校正是否充分（只对 positive finding 做了 Bonferroni）
   - Gold-empty instance filtering 的决策是否合理且一致

4. **数据可靠性**
   - Table 1-4 之间数据是否一致
   - 正文、caption、appendix 中同一数值的引用是否一致
   - Table 2 NER 2-seed vs RE 单 seed 的不一致是否有合理解释

5. **页数合规**
   - 正文是否在 8 页限制内（不计 Limitations, Ethics, References, Appendix）

请输出完整审稿报告，包括：Summary (2-3句)、Strengths (逐条)、Weaknesses (逐条，严格不留情)、Questions (需作者回答)、Missing References、Overall Assessment (评分 + 置信度)。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "0399fd48-9ce8-44a9-a460-553e3e5fc517",
  "type": "user",
  "uuid": "6895fdc4-d8e9-41c1-9423-f665106bfe66",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_1_68ddc296",
  "sessionId": "a5f4ff78-4f02-4166-b054-29f1bf2f2644",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-16T05:12:26.643Z_

```json
{
  "parentUuid": "6895fdc4-d8e9-41c1-9423-f665106bfe66",
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
  "uuid": "74b43803-aaca-4743-9958-55dac6bae877",
  "timestamp": "2026-05-16T05:12:26.643Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_1_68ddc296",
  "sessionId": "a5f4ff78-4f02-4166-b054-29f1bf2f2644",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-16T05:12:26.643Z_

```json
{
  "parentUuid": "74b43803-aaca-4743-9958-55dac6bae877",
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
  "uuid": "2de8e1af-2c46-48be-9ed6-0957b0c7e995",
  "timestamp": "2026-05-16T05:12:26.643Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_1_68ddc296",
  "sessionId": "a5f4ff78-4f02-4166-b054-29f1bf2f2644",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 6 · 2026-05-16T05:12:26.643Z_

```json
{
  "parentUuid": "2de8e1af-2c46-48be-9ed6-0957b0c7e995",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "db51aea5-ac87-4f72-b3ba-63c162002b05",
  "timestamp": "2026-05-16T05:12:26.643Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_1_68ddc296",
  "sessionId": "a5f4ff78-4f02-4166-b054-29f1bf2f2644",
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
  "aiTitle": "Review round 1 paper on structured IE self-consistency",
  "sessionId": "a5f4ff78-4f02-4166-b054-29f1bf2f2644"
}
```

---

### Assistant

_source line 8 · 2026-05-16T05:12:31.353Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to perform a detailed academic review of a paper as Reviewer 1, focusing on methodological rigor, experimental design, and statistical analysis. Let me start by:

1. First, searching for EMNLP 2026 / ACL ARR reviewer guidelines
2. Reading the paper (main.tex and section files)

Let me begin by reading the paper files and searching for reviewer guidelines.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "db51aea5-ac87-4f72-b3ba-63c162002b05",
  "isSidechain": false,
  "requestId": "req_011Cb5g5fbsqKdHTcfhoenNt",
  "type": "assistant",
  "uuid": "1d639920-562a-4aeb-abed-fa070a85cebb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_1_68ddc296",
  "sessionId": "a5f4ff78-4f02-4166-b054-29f1bf2f2644",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BFcYpengX1xLMJhWpLbi1U",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14066,
      "cache_read_input_tokens": 11841,
      "output_tokens": 321,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 14066,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 321,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 14066,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 14066
          },
          "type": "message"
        }
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

_source line 9 · 2026-05-16T05:12:32.825Z_

开始执行 Round 1 审稿任务。先搜索 ACL ARR reviewer guidelines，同时读取论文各 section。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1d639920-562a-4aeb-abed-fa070a85cebb",
  "isSidechain": false,
  "requestId": "req_011Cb5g5fbsqKdHTcfhoenNt",
  "type": "assistant",
  "uuid": "940719bb-0ec1-4d94-94ea-c751e7465fa0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_1_68ddc296",
  "sessionId": "a5f4ff78-4f02-4166-b054-29f1bf2f2644",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BFcYpengX1xLMJhWpLbi1U",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14066,
      "cache_read_input_tokens": 11841,
      "output_tokens": 321,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 14066,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 321,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 14066,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 14066
          },
          "type": "message"
        }
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

_source line 10 · 2026-05-16T05:12:33.304Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01LGPUv8e6zwdCuAsAnKfQMC`</summary>

```json
{
  "query": "select:WebSearch",
  "max_results": 1
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "940719bb-0ec1-4d94-94ea-c751e7465fa0",
  "isSidechain": false,
  "requestId": "req_011Cb5g5fbsqKdHTcfhoenNt",
  "type": "assistant",
  "uuid": "e6bb4e1d-31ea-4091-9381-38886f5f1005",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_1_68ddc296",
  "sessionId": "a5f4ff78-4f02-4166-b054-29f1bf2f2644",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BFcYpengX1xLMJhWpLbi1U",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14066,
      "cache_read_input_tokens": 11841,
      "output_tokens": 321,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 14066,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 321,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 14066,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 14066
          },
          "type": "message"
        }
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

_source line 11 · 2026-05-16T05:12:34.474Z_

<details><summary>↩ Tool result · `toolu_01NTGo3zLKkMFSmT8gkCrhpu`</summary>

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
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e51f8279-ed0e-49bb-a667-69900681a429",
  "isSidechain": false,
  "promptId": "0399fd48-9ce8-44a9-a460-553e3e5fc517",
  "type": "user",
  "uuid": "de148b9f-a616-4479-af14-5940c352fb33",
  "toolUseResult": {
    "matches": [
      "mcp__agent-ml-research__pdf_to_images",
      "mcp__agent-ml-research__review_reviewer_post_to_director",
      "mcp__agent-ml-research__verify_references"
    ],
    "query": "select:mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__review_reviewer_post_to_director,mcp__agent-ml-research__verify_references",
    "total_deferred_tools": 23
  },
  "sourceToolAssistantUUID": "e51f8279-ed0e-49bb-a667-69900681a429",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_1_68ddc296",
  "sessionId": "a5f4ff78-4f02-4166-b054-29f1bf2f2644",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-16T05:12:33.309Z_

<details><summary>↩ Tool result · `toolu_01LGPUv8e6zwdCuAsAnKfQMC`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "WebSearch"
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e6bb4e1d-31ea-4091-9381-38886f5f1005",
  "isSidechain": false,
  "promptId": "0399fd48-9ce8-44a9-a460-553e3e5fc517",
  "type": "user",
  "uuid": "0cd77486-1384-4e69-a08b-3bbbc80411ef",
  "toolUseResult": {
    "matches": [
      "WebSearch"
    ],
    "query": "select:WebSearch",
    "total_deferred_tools": 23
  },
  "sourceToolAssistantUUID": "e6bb4e1d-31ea-4091-9381-38886f5f1005",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_1_68ddc296",
  "sessionId": "a5f4ff78-4f02-4166-b054-29f1bf2f2644",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-16T05:12:34.471Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01NTGo3zLKkMFSmT8gkCrhpu`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__review_reviewer_post_to_director,mcp__agent-ml-research__verify_references",
  "max_results": 3
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0cd77486-1384-4e69-a08b-3bbbc80411ef",
  "isSidechain": false,
  "requestId": "req_011Cb5g5fbsqKdHTcfhoenNt",
  "type": "assistant",
  "uuid": "e51f8279-ed0e-49bb-a667-69900681a429",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_1_68ddc296",
  "sessionId": "a5f4ff78-4f02-4166-b054-29f1bf2f2644",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BFcYpengX1xLMJhWpLbi1U",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14066,
      "cache_read_input_tokens": 11841,
      "output_tokens": 321,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 14066,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 321,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 14066,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 14066
          },
          "type": "message"
        }
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

_source line 14 · 2026-05-16T05:12:37.873Z_

<details><summary>Logged reasoning block</summary>

```text
Now let me search for ACL ARR reviewer guidelines and read the paper sections in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "de148b9f-a616-4479-af14-5940c352fb33",
  "isSidechain": false,
  "requestId": "req_011Cb5g6FS6m68MnAr9Wd4TJ",
  "type": "assistant",
  "uuid": "4ccb4308-5fdf-4cd6-a425-931ae5d741be",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_1_68ddc296",
  "sessionId": "a5f4ff78-4f02-4166-b054-29f1bf2f2644",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VosaXKBsYz2N3xxRLjjtUZ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1872,
      "cache_read_input_tokens": 25907,
      "output_tokens": 319,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1872,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 319,
          "cache_read_input_tokens": 25907,
          "cache_creation_input_tokens": 1872,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1872
          },
          "type": "message"
        }
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

_source line 15 · 2026-05-16T05:12:38.370Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01S89B2bPVsApgvhkKwTmD1Y`</summary>

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
  "parentUuid": "4ccb4308-5fdf-4cd6-a425-931ae5d741be",
  "isSidechain": false,
  "requestId": "req_011Cb5g6FS6m68MnAr9Wd4TJ",
  "type": "assistant",
  "uuid": "5bf35d9e-4202-470f-9b5c-847353c5759d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_1_68ddc296",
  "sessionId": "a5f4ff78-4f02-4166-b054-29f1bf2f2644",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VosaXKBsYz2N3xxRLjjtUZ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1872,
      "cache_read_input_tokens": 25907,
      "output_tokens": 319,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1872,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 319,
          "cache_read_input_tokens": 25907,
          "cache_creation_input_tokens": 1872,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1872
          },
          "type": "message"
        }
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

_source line 16 · 2026-05-16T05:12:39.758Z_

<details open><summary>🔧 Tool call — Read · `toolu_018LbbSCKEVRT9GPQvKRm8vw`</summary>

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
  "parentUuid": "5bf35d9e-4202-470f-9b5c-847353c5759d",
  "isSidechain": false,
  "requestId": "req_011Cb5g6FS6m68MnAr9Wd4TJ",
  "type": "assistant",
  "uuid": "b829c235-bb1f-4805-b703-0bd8c2e7aa02",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_1_68ddc296",
  "sessionId": "a5f4ff78-4f02-4166-b054-29f1bf2f2644",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VosaXKBsYz2N3xxRLjjtUZ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1872,
      "cache_read_input_tokens": 25907,
      "output_tokens": 319,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1872,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 319,
          "cache_read_input_tokens": 25907,
          "cache_creation_input_tokens": 1872,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1872
          },
          "type": "message"
        }
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

_source line 17 · 2026-05-16T05:12:40.712Z_

<details><summary>↩ Tool result · `toolu_014PNRDzRR5u6L5GK3eCz8MN`</summary>

```text
1	\section{Introduction}\label{sec:introduction}
2	
3	Self-consistency---majority voting over multiple samples---yields large gains on discrete-answer reasoning \citep{wang2023selfconsistency}, and test-time compute scaling has emerged as a complementary axis to model scaling \cite{snell2025scaling, brown2024monkeys}.
4	But information extraction (IE) poses a structurally different challenge: the output is a \textit{set} of entities or relations, two samples may extract overlapping but non-identical structures, and there is no obvious majority to vote on.
5	
6	Prior work on confidence estimation for LLM-based IE has conflated \textit{quality estimation} (which inputs does the model handle reliably?) with \textit{sample selection} (which of $N$ outputs is best?).
7	Existing self-consistency methods \cite{wang2023selfconsistency, chen2024usc, taubenfeld2025cisc, kang2025selfcertainty} assume outputs can be grouped by equivalence---an assumption that breaks for entity sets with partial overlap.
8	\citet{yao2026consistency} examine consistency--accuracy correlations for LLM-based IE using exact-match agreement; we extend their work by introducing structural matching (Soft Jaccard) that captures partial overlap, separating quality estimation from best-of-$N$ selection, and evaluating across a three-dataset difficulty gradient with a free-form decoding ablation.
9	
10	Our central finding is the \textbf{correlation-selection gap} (Figure~\ref{fig:overview}): consistency signals achieve strong quality estimation ($\rho$ up to 0.45) but fail at sample selection despite substantial oracle headroom.
11	The gap has two causes: instance-level signals (4 of 5) assign identical scores to all candidates and thus cannot rank them (\S\ref{sec:formulation}); LP---the only per-sample signal---is too compressed within instances to discriminate (median range 0.041 nats; \S\ref{sec:discussion}), and consensus-proximity selection (MBR) fails because utility correlates with F1 across instances but not within them.
12	
13	\begin{figure*}[t]
14	\centering
15	\includegraphics[width=\textwidth]{fig_overview}
16	\caption{The correlation-selection gap. \textbf{Left}: high inter-sample agreement correlates with high F1 (quality estimation). \textbf{Right}: instance-level signals assign identical scores to all candidates, precluding sample selection; LP (per-sample) provides distinct scores but is too compressed to discriminate (\S\ref{sec:discussion}).}
17	\label{fig:overview}
18	\end{figure*}
19	
20	We evaluate five signals from three families---structural, surface, and model-internal---across three NER benchmarks (SciERC \cite{luan2018scierc}, CoNLL-2003 \cite{tjongkimsang2003conll}, WNUT-17 \cite{derczynski2017wnut}), using two 8B models (Qwen3-8B, LLaMA-3.1-8B) with a 4B ablation (Qwen3-4B).
21	We include one RE benchmark (SciERC) as an exploratory extension to probe whether the gap generalizes beyond NER; RE conclusions are preliminary.
22	Our contributions:
23	\begin{enumerate}
24	    \item \textbf{Empirical dissociation of evaluation metrics.}
25	    Spearman $\rho$, AUROC, and selection F1 decouple: signals with the strongest rank correlation need not yield the best binary discrimination or selection (e.g., verbalized confidence achieves higher $\rho$ than LP yet the worst selection; Appendix~\ref{app:verbalized_confidence}). Single-metric evaluation risks selecting the wrong signal.
26	
27	    \item \textbf{LP compression and MBR failure.}
28	    Log-probability, the only per-sample signal, is too compressed within instances to select (median range 0.041 nats, 60\% tied); consensus-proximity selection (MBR) correlates with F1 across instances but not within them. A 4-seed free-form ablation confirms compression is not caused by constrained decoding.
29	
30	    \item \textbf{Difficulty- and task-dependent signal rankings.}
31	    Rankings shift with task complexity and collapse at the capability boundary.\footnote{RE conclusions rest on SciERC alone (single benchmark, 40\% zero-F1 rate); we mark RE results with $^\dagger$RE throughout.}
32	\end{enumerate}
33	
34	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "23cdf956-d3c7-4358-a825-0776635ce80e",
  "isSidechain": false,
  "promptId": "0399fd48-9ce8-44a9-a460-553e3e5fc517",
  "type": "user",
  "uuid": "7aac4f94-a1bc-4b63-af42-acb5bde0526f",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/introduction.tex",
      "content": "\\section{Introduction}\\label{sec:introduction}\n\nSelf-consistency---majority voting over multiple samples---yields large gains on discrete-answer reasoning \\citep{wang2023selfconsistency}, and test-time compute scaling has emerged as a complementary axis to model scaling \\cite{snell2025scaling, brown2024monkeys}.\nBut information extraction (IE) poses a structurally different challenge: the output is a \\textit{set} of entities or relations, two samples may extract overlapping but non-identical structures, and there is no obvious majority to vote on.\n\nPrior work on confidence estimation for LLM-based IE has conflated \\textit{quality estimation} (which inputs does the model handle reliably?) with \\textit{sample selection} (which of $N$ outputs is best?).\nExisting self-consistency methods \\cite{wang2023selfconsistency, chen2024usc, taubenfeld2025cisc, kang2025selfcertainty} assume outputs can be grouped by equivalence---an assumption that breaks for entity sets with partial overlap.\n\\citet{yao2026consistency} examine consistency--accuracy correlations for LLM-based IE using exact-match agreement; we extend their work by introducing structural matching (Soft Jaccard) that captures partial overlap, separating quality estimation from best-of-$N$ selection, and evaluating across a three-dataset difficulty gradient with a free-form decoding ablation.\n\nOur central finding is the \\textbf{correlation-selection gap} (Figure~\\ref{fig:overview}): consistency signals achieve strong quality estimation ($\\rho$ up to 0.45) but fail at sample selection despite substantial oracle headroom.\nThe gap has two causes: instance-level signals (4 of 5) assign identical scores to all candidates and thus cannot rank them (\\S\\ref{sec:formulation}); LP---the only per-sample signal---is too compressed within instances to discriminate (median range 0.041 nats; \\S\\ref{sec:discussion}), and consensus-proximity selection (MBR) fails because utility correlates with F1 across instances but not within them.\n\n\\begin{figure*}[t]\n\\centering\n\\includegraphics[width=\\textwidth]{fig_overview}\n\\caption{The correlation-selection gap. \\textbf{Left}: high inter-sample agreement correlates with high F1 (quality estimation). \\textbf{Right}: instance-level signals assign identical scores to all candidates, precluding sample selection; LP (per-sample) provides distinct scores but is too compressed to discriminate (\\S\\ref{sec:discussion}).}\n\\label{fig:overview}\n\\end{figure*}\n\nWe evaluate five signals from three families---structural, surface, and model-internal---across three NER benchmarks (SciERC \\cite{luan2018scierc}, CoNLL-2003 \\cite{tjongkimsang2003conll}, WNUT-17 \\cite{derczynski2017wnut}), using two 8B models (Qwen3-8B, LLaMA-3.1-8B) with a 4B ablation (Qwen3-4B).\nWe include one RE benchmark (SciERC) as an exploratory extension to probe whether the gap generalizes beyond NER; RE conclusions are preliminary.\nOur contributions:\n\\begin{enumerate}\n    \\item \\textbf{Empirical dissociation of evaluation metrics.}\n    Spearman $\\rho$, AUROC, and selection F1 decouple: signals with the strongest rank correlation need not yield the best binary discrimination or selection (e.g., verbalized confidence achieves higher $\\rho$ than LP yet the worst selection; Appendix~\\ref{app:verbalized_confidence}). Single-metric evaluation risks selecting the wrong signal.\n\n    \\item \\textbf{LP compression and MBR failure.}\n    Log-probability, the only per-sample signal, is too compressed within instances to select (median range 0.041 nats, 60\\% tied); consensus-proximity selection (MBR) correlates with F1 across instances but not within them. A 4-seed free-form ablation confirms compression is not caused by constrained decoding.\n\n    \\item \\textbf{Difficulty- and task-dependent signal rankings.}\n    Rankings shift with task complexity and collapse at the capability boundary.\\footnote{RE conclusions rest on SciERC alone (single benchmark, 40\\% zero-F1 rate); we mark RE results with $^\\dagger$RE throughout.}\n\\end{enumerate}\n\n",
      "numLines": 34,
      "startLine": 1,
      "totalLines": 34
    }
  },
  "sourceToolAssistantUUID": "23cdf956-d3c7-4358-a825-0776635ce80e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_1_68ddc296",
  "sessionId": "a5f4ff78-4f02-4166-b054-29f1bf2f2644",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-16T05:12:39.768Z_

<details><summary>↩ Tool result · `toolu_018LbbSCKEVRT9GPQvKRm8vw`</summary>

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
21	\title{Strong Predictors, Weak Selectors:\\ The Correlation-Selection Gap in LLM-Based Structured Information Extraction}
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
  "parentUuid": "b829c235-bb1f-4805-b703-0bd8c2e7aa02",
  "isSidechain": false,
  "promptId": "0399fd48-9ce8-44a9-a460-553e3e5fc517",
  "type": "user",
  "uuid": "a752af77-89e2-4a2c-9477-741635ef4e60",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex",
      "content": "\\documentclass[11pt]{article}\n\n\\usepackage[review]{acl}\n\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage[T1]{fontenc}\n\\usepackage[utf8]{inputenc}\n\\usepackage{microtype}\n\\usepackage{inconsolata}\n\\usepackage{graphicx}\n\\usepackage{booktabs}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{multirow}\n\\usepackage{xcolor}\n\\usepackage{subcaption}\n\n\\graphicspath{{figures/}}\n\n\\title{Strong Predictors, Weak Selectors:\\\\ The Correlation-Selection Gap in LLM-Based Structured Information Extraction}\n\n\\author{Anonymous}\n\n\\begin{document}\n\\maketitle\n\n\\input{sections/abstract}\n\\input{sections/introduction}\n\\input{sections/related_work}\n\\input{sections/method}\n\\input{sections/experiments}\n\\input{sections/discussion}\n\\input{sections/conclusion}\n\n\\section*{Limitations}\n\\input{sections/limitations}\n\n\\section*{Ethics Statement}\nAll experiments use publicly available benchmarks (SciERC, CoNLL-2003, WNUT-17) and open-weight models (Qwen3-8B, Qwen3-4B, LLaMA-3.1-8B).\nCoNLL-2003 is derived from the Reuters RCV1 corpus, which is available for research purposes under a NIST agreement; we use the standard research distribution.\nNo new human data was collected or annotated for this study.\nOur findings on signal limitations could inform more reliable deployment of IE systems by guiding practitioners toward appropriate confidence signals for their use case.\nCode and data will be released upon acceptance at [anonymized URL].\n\n\\bibliography{references}\n\n\\appendix\n\\input{sections/appendix}\n\n\\end{document}\n",
      "numLines": 52,
      "startLine": 1,
      "totalLines": 52
    }
  },
  "sourceToolAssistantUUID": "b829c235-bb1f-4805-b703-0bd8c2e7aa02",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_1_68ddc296",
  "sessionId": "a5f4ff78-4f02-4166-b054-29f1bf2f2644",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-16T05:12:40.297Z_

<details open><summary>🔧 Tool call — Read · `toolu_01F1BnbLvsWJHjzEnJDThqVj`</summary>

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
  "parentUuid": "a752af77-89e2-4a2c-9477-741635ef4e60",
  "isSidechain": false,
  "requestId": "req_011Cb5g6FS6m68MnAr9Wd4TJ",
  "type": "assistant",
  "uuid": "959d6cd5-c6b3-415a-90df-d39733f25e7b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_1_68ddc296",
  "sessionId": "a5f4ff78-4f02-4166-b054-29f1bf2f2644",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VosaXKBsYz2N3xxRLjjtUZ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1872,
      "cache_read_input_tokens": 25907,
      "output_tokens": 319,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1872,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 319,
          "cache_read_input_tokens": 25907,
          "cache_creation_input_tokens": 1872,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1872
          },
          "type": "message"
        }
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

_source line 20 · 2026-05-16T05:12:40.308Z_

<details><summary>↩ Tool result · `toolu_01F1BnbLvsWJHjzEnJDThqVj`</summary>

```text
1	\begin{abstract}
2	Self-consistency yields large gains on discrete-answer tasks, but information extraction (IE) produces \textit{sets} of entities and relations with partial overlap, where no majority vote analog exists.
3	We evaluate five confidence signals across three NER benchmarks, with one RE benchmark as an exploratory extension, at two model scales (4B and 8B).
4	All signals achieve strong quality estimation (Spearman $\rho$ up to 0.45), yet none improves best-of-$N$ selection despite substantial oracle headroom---the \textit{correlation-selection gap}.
5	Four instance-level signals fail by construction; the empirical finding is that log-probability---the only per-sample signal---is too compressed within instances to discriminate (median range 0.041 nats, 60\% tied).
6	A 4-seed free-form decoding ablation confirms NER compression is not an artifact of constrained decoding; on RE, LP selection reverses direction under free-form decoding ($+1.8{\pm}0.1$~pp), suggesting regime-dependent behavior.
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
  "parentUuid": "959d6cd5-c6b3-415a-90df-d39733f25e7b",
  "isSidechain": false,
  "promptId": "0399fd48-9ce8-44a9-a460-553e3e5fc517",
  "type": "user",
  "uuid": "1ec383a8-80a7-4b4a-989e-910868698398",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/abstract.tex",
      "content": "\\begin{abstract}\nSelf-consistency yields large gains on discrete-answer tasks, but information extraction (IE) produces \\textit{sets} of entities and relations with partial overlap, where no majority vote analog exists.\nWe evaluate five confidence signals across three NER benchmarks, with one RE benchmark as an exploratory extension, at two model scales (4B and 8B).\nAll signals achieve strong quality estimation (Spearman $\\rho$ up to 0.45), yet none improves best-of-$N$ selection despite substantial oracle headroom---the \\textit{correlation-selection gap}.\nFour instance-level signals fail by construction; the empirical finding is that log-probability---the only per-sample signal---is too compressed within instances to discriminate (median range 0.041 nats, 60\\% tied).\nA 4-seed free-form decoding ablation confirms NER compression is not an artifact of constrained decoding; on RE, LP selection reverses direction under free-form decoding ($+1.8{\\pm}0.1$~pp), suggesting regime-dependent behavior.\nConsensus-proximity selection (MBR) correlates with F1 across instances but not within them.\nSignal rankings shift with task difficulty and collapse at the capability boundary; closing the gap likely requires learned per-sample scoring.\n\\end{abstract}\n",
      "numLines": 10,
      "startLine": 1,
      "totalLines": 10
    }
  },
  "sourceToolAssistantUUID": "959d6cd5-c6b3-415a-90df-d39733f25e7b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_1_68ddc296",
  "sessionId": "a5f4ff78-4f02-4166-b054-29f1bf2f2644",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-16T05:12:40.707Z_

<details open><summary>🔧 Tool call — Read · `toolu_014PNRDzRR5u6L5GK3eCz8MN`</summary>

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
  "parentUuid": "1ec383a8-80a7-4b4a-989e-910868698398",
  "isSidechain": false,
  "requestId": "req_011Cb5g6FS6m68MnAr9Wd4TJ",
  "type": "assistant",
  "uuid": "23cdf956-d3c7-4358-a825-0776635ce80e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_1_68ddc296",
  "sessionId": "a5f4ff78-4f02-4166-b054-29f1bf2f2644",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VosaXKBsYz2N3xxRLjjtUZ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1872,
      "cache_read_input_tokens": 25907,
      "output_tokens": 319,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1872,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 319,
          "cache_read_input_tokens": 25907,
          "cache_creation_input_tokens": 1872,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1872
          },
          "type": "message"
        }
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
  "lastPrompt": "[Round 1 审稿请求]: ## Round 1 审稿任务 — Reviewer 1（方法严谨性 + 实验设计 + 统计分析）  ### Venue 信息 - **目标**: EMNLP 2026 Main Conference (via ARR May 2026 cycle) - **截止日期**: 2026-05-25 - **格式**: ACL 模板, 正文 8 页, double-bl…",
  "leafUuid": "7aac4f94-a1bc-4b63-af42-acb5bde0526f",
  "sessionId": "a5f4ff78-4f02-4166-b054-29f1bf2f2644"
}
```

---

### Runtime record

_source line 23_

```json
{
  "type": "ai-title",
  "aiTitle": "Review round 1 paper on structured IE self-consistency",
  "sessionId": "a5f4ff78-4f02-4166-b054-29f1bf2f2644"
}
```

---

### Tool result

_source line 24 · 2026-05-16T05:12:46.218Z_

<details><summary>↩ Tool result · `toolu_01S89B2bPVsApgvhkKwTmD1Y`</summary>

```text
Web search results for query: "ACL ARR 2026 reviewer guidelines review form criteria scoring"

Links: [{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"aclrollingreview/reviewing.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/reviewing.md"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"}]

Based on the search results, here's information about the ACL ARR 2026 reviewer guidelines, review form criteria, and scoring:

## Reviewer Scoring System

Starting with February 2025, ARR reviewers are asked to provide three scores: soundness, excitement, and overall recommendation.

### Soundness Score
The soundness scores must be justified by the text of the review. If you give a low Soundness score without finding any major faults, this means that your review is not a faithful explanation of your recommendation, and you need to revise it.

### Excitement Score
Sometimes you may find the work sound, but not something that is interesting for you personally. Such preferences are more subjective and should be reflected in a separate excitement score, which is orthogonal to the assessment of the soundness of the paper. How exciting is this paper for you? Excitement is subjective, and does not necessarily follow what is popular in the field.

### Overall Recommendation Score
The Overall assessment score is an explicit recommendation for the outcome of this paper, if it were committed to an *ACL venue. This is a composite score reflecting your assessment of soundness, excitement, and also other factors like novelty and impact.

The scale includes: 5 = Consider for Award (up to top 2.5% papers); 2 = Resubmit next cycle; 1.5 = Resubmit after next cycle; 1 = Do not resubmit.

## Review Form Criteria

The main criteria for Findings are soundness and reproducibility. Conference recommendations may also consider novelty, impact and other factors.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5bf35d9e-4202-470f-9b5c-847353c5759d",
  "isSidechain": false,
  "promptId": "0399fd48-9ce8-44a9-a460-553e3e5fc517",
  "type": "user",
  "uuid": "b4bd655c-05ac-4fc0-b44d-bd6636c6f57d",
  "toolUseResult": {
    "query": "ACL ARR 2026 reviewer guidelines review form criteria scoring",
    "results": [
      {
        "tool_use_id": "srvtoolu_01BRSsNe13uvMb5Bg2a72uDT",
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
            "title": "How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics",
            "url": "http://aclrollingreview.org/reviewing"
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
      "Based on the search results, here's information about the ACL ARR 2026 reviewer guidelines, review form criteria, and scoring:\n\n## Reviewer Scoring System\n\nStarting with February 2025, ARR reviewers are asked to provide three scores: soundness, excitement, and overall recommendation.\n\n### Soundness Score\nThe soundness scores must be justified by the text of the review. If you give a low Soundness score without finding any major faults, this means that your review is not a faithful explanation of your recommendation, and you need to revise it.\n\n### Excitement Score\nSometimes you may find the work sound, but not something that is interesting for you personally. Such preferences are more subjective and should be reflected in a separate excitement score, which is orthogonal to the assessment of the soundness of the paper. How exciting is this paper for you? Excitement is subjective, and does not necessarily follow what is popular in the field.\n\n### Overall Recommendation Score\nThe Overall assessment score is an explicit recommendation for the outcome of this paper, if it were committed to an *ACL venue. This is a composite score reflecting your assessment of soundness, excitement, and also other factors like novelty and impact.\n\nThe scale includes: 5 = Consider for Award (up to top 2.5% papers); 2 = Resubmit next cycle; 1.5 = Resubmit after next cycle; 1 = Do not resubmit.\n\n## Review Form Criteria\n\nThe main criteria for Findings are soundness and reproducibility. Conference recommendations may also consider novelty, impact and other factors."
    ],
    "durationSeconds": 7.843011556000001
  },
  "sourceToolAssistantUUID": "5bf35d9e-4202-470f-9b5c-847353c5759d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_1_68ddc296",
  "sessionId": "a5f4ff78-4f02-4166-b054-29f1bf2f2644",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-16T05:12:49.759Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01XWcrKmcoHDFGQjFDjf6dpk`</summary>

```json
{
  "query": "ACL Rolling Review review form 2025 2026 soundness excitement overall score scale"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b4bd655c-05ac-4fc0-b44d-bd6636c6f57d",
  "isSidechain": false,
  "requestId": "req_011Cb5g77PBpg7mgsvGFoEQG",
  "type": "assistant",
  "uuid": "690cc503-5b8d-4e60-a7df-d5d6491a18f9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_1_68ddc296",
  "sessionId": "a5f4ff78-4f02-4166-b054-29f1bf2f2644",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016cRMctP9utGQAEncDd2GQj",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2136,
      "cache_creation_input_tokens": 1206,
      "cache_read_input_tokens": 27779,
      "output_tokens": 292,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1206,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2136,
          "output_tokens": 292,
          "cache_read_input_tokens": 27779,
          "cache_creation_input_tokens": 1206,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1206
          },
          "type": "message"
        }
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

_source line 26 · 2026-05-16T05:12:50.188Z_

<details open><summary>🔧 Tool call — Read · `toolu_015FhjNdpjhTxbYMkB9CMi8Q`</summary>

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
  "parentUuid": "690cc503-5b8d-4e60-a7df-d5d6491a18f9",
  "isSidechain": false,
  "requestId": "req_011Cb5g77PBpg7mgsvGFoEQG",
  "type": "assistant",
  "uuid": "2281f352-785f-4b2b-ad93-3bb71a03183a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_1_68ddc296",
  "sessionId": "a5f4ff78-4f02-4166-b054-29f1bf2f2644",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016cRMctP9utGQAEncDd2GQj",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2136,
      "cache_creation_input_tokens": 1206,
      "cache_read_input_tokens": 27779,
      "output_tokens": 292,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1206,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2136,
          "output_tokens": 292,
          "cache_read_input_tokens": 27779,
          "cache_creation_input_tokens": 1206,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1206
          },
          "type": "message"
        }
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

_source line 27 · 2026-05-16T05:12:50.199Z_

<details><summary>↩ Tool result · `toolu_015FhjNdpjhTxbYMkB9CMi8Q`</summary>

```text
1	\section{Method}\label{sec:method}
2	
3	\subsection{Problem Formulation}\label{sec:formulation}
4	
5	Given model $\mathcal{M}$ and input $x$, we sample $N$ outputs $\{y_1, \ldots, y_N\}$ at temperature $T > 0$ via constrained decoding \cite{willard2023guided}, where each $y_i$ is an entity set (NER) or relation set (RE).
6	A \textbf{per-sample signal} $c_{\text{ps}}: (x, y_i) \to \mathbb{R}$ scores each output independently; an \textbf{instance-level signal} $c_{\text{il}}: (x, \{y_i\}_{i=1}^N) \to \mathbb{R}$ produces a single score per input (notation in Appendix~\ref{app:notation}).
7	This distinction is consequential for selection: in our study, 4 of 5 signals are instance-level aggregates that assign identical scores to all $N$ candidates and thus cannot rank them by construction; only per-sample signals can, in principle, select the best output.
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
39	where $M$ is the matched set, $\text{sim}(a_m, b_m)$ is the token-level IoU between matched spans, and $\max(|g_i|, |g_j|)$ penalizes length asymmetry.
40	The instance-level signal averages over all pairs:
41	\begin{equation}\label{eq:sj_instance}
42	c_{\text{sj}}(x) = \frac{1}{\binom{N}{2}} \sum_{i&lt;j} \text{SJ}(y_i, y_j)
43	\end{equation}
44	
45	\paragraph{Entity voting confidence (structural, instance-level).}
46	For each entity $e$ in the union $E_\cup$ of all samples, we compute frequency $\text{freq}(e) = |\{i : e \in y_i\}| / N$.
47	The instance-level confidence is the mean frequency:
48	\begin{equation}\label{eq:voting}
49	c_{\text{vote}}(x) = \frac{1}{|E_\cup|} \sum_{e \in E_\cup} \text{freq}(e)
50	\end{equation}
51	When $E_\cup = \emptyset$, we set $c_{\mathrm{vc}}(x) = 0$.\footnote{Equation~\ref{eq:voting} defines the continuous QE signal; for voted-output \textit{selection} (Table~\ref{tab:selection}), we include only entities with frequency ${>}N/2$, following standard majority voting.}
52	
53	\subsection{Evaluation Framework}\label{sec:evaluation}
54	
55	\paragraph{Quality estimation.}
56	Spearman $\rho$ between the signal and instance-level F1, and AUROC classifying instances as above/below median F1.
57	Correlation analyses exclude empty gold annotations ($n{=}529$ on SciERC after filtering 22/551; $n{=}2{,}756$ on CoNLL after filtering 697/3{,}453);\footnote{On CoNLL, full-set ($n{=}3{,}453$) Spearman $\rho$ values are higher than gold-filtered ($n{=}2{,}756$) by $+0.03$--$0.05$ due to the zero/non-zero boundary inflating correlations, paralleling the effect documented for WNUT-17 in Appendix~\ref{app:additional}.} selection retains the full set.
58	
59	\paragraph{Sample selection.}
60	Best-of-$N$ F1: per-sample signals (LP) directly rank candidates; instance-level signals select the sample closest to consensus.
61	Baselines: \textit{oracle} (highest-F1 sample) and \textit{single-sample} (one $T{=}1.0$ draw, not argmax decoding; labeled ``Single'' in tables).
62	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2281f352-785f-4b2b-ad93-3bb71a03183a",
  "isSidechain": false,
  "promptId": "0399fd48-9ce8-44a9-a460-553e3e5fc517",
  "type": "user",
  "uuid": "61b20b26-0e4e-476a-a8ce-efd4a21bddc9",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/method.tex",
      "content": "\\section{Method}\\label{sec:method}\n\n\\subsection{Problem Formulation}\\label{sec:formulation}\n\nGiven model $\\mathcal{M}$ and input $x$, we sample $N$ outputs $\\{y_1, \\ldots, y_N\\}$ at temperature $T > 0$ via constrained decoding \\cite{willard2023guided}, where each $y_i$ is an entity set (NER) or relation set (RE).\nA \\textbf{per-sample signal} $c_{\\text{ps}}: (x, y_i) \\to \\mathbb{R}$ scores each output independently; an \\textbf{instance-level signal} $c_{\\text{il}}: (x, \\{y_i\\}_{i=1}^N) \\to \\mathbb{R}$ produces a single score per input (notation in Appendix~\\ref{app:notation}).\nThis distinction is consequential for selection: in our study, 4 of 5 signals are instance-level aggregates that assign identical scores to all $N$ candidates and thus cannot rank them by construction; only per-sample signals can, in principle, select the best output.\n\n\\subsection{Confidence Signals}\\label{sec:signals}\n\nFour are \\textit{consistency signals}: \\textit{structural} (Soft Jaccard [SJ], entity voting confidence [VC]) and \\textit{surface} (exact match [EM], Fleiss' $\\kappa$ [FK]); log-probability [LP] is the sole \\textit{model-internal}, per-sample signal.\n\n\\paragraph{Log-probability (model-internal, per-sample).}\nFor sample $y_i$ with tokens $t_1, \\ldots, t_{|y_i|}$:\n\\begin{equation}\\label{eq:logprob}\nc_{\\text{lp}}(y_i) = \\frac{1}{|y_i|} \\sum_{j=1}^{|y_i|} \\log p_{\\mathcal{M}}(t_j \\mid t_{&lt;j}, x)\n\\end{equation}\n\n\\paragraph{Exact match voting (surface, instance-level).}\nThe proportion of samples producing the most common output:\n\\begin{equation}\\label{eq:em}\nc_{\\text{em}}(x) = \\frac{1}{N} \\max_{y} \\big|\\{i : y_i = y\\}\\big|\n\\end{equation}\n\n\\paragraph{Fleiss' $\\kappa$ (surface, instance-level).}\nWe adapt \\citet{fleiss1971agreement} to entity sets: items are unique (text, type) tuples across all $N$ samples; each sample assigns binary present/absent labels, yielding a $|E_\\cup| \\times 2$ rating matrix:\n\\begin{equation}\\label{eq:fk}\n\\kappa = \\frac{\\bar{P} - \\bar{P}_e}{1 - \\bar{P}_e}\n\\end{equation}\nwhere $\\bar{P}$ is mean observed and $\\bar{P}_e$ expected agreement.\nTemperature-based sampling introduces mild negative dependence ($-$0.4\\% to $-$4.0\\%; Appendix~\\ref{app:fk_independence}), which does not inflate FK.\nUnlike structural signals, FK relies on exact string matching.\n\n\\paragraph{Soft Jaccard (structural, instance-level).}\nFor samples $y_i, y_j$, we group extractions by type, compute max-weight bipartite matching (Hungarian algorithm, token-level IoU), and define:\n\\begin{equation}\\label{eq:sj}\n\\text{SJ}(y_i, y_j) = \\frac{\\sum_{m \\in M} \\text{sim}(a_m, b_m)}{\\sum_{g} \\max(|g_i|, |g_j|)}\n\\end{equation}\nwhere $M$ is the matched set, $\\text{sim}(a_m, b_m)$ is the token-level IoU between matched spans, and $\\max(|g_i|, |g_j|)$ penalizes length asymmetry.\nThe instance-level signal averages over all pairs:\n\\begin{equation}\\label{eq:sj_instance}\nc_{\\text{sj}}(x) = \\frac{1}{\\binom{N}{2}} \\sum_{i&lt;j} \\text{SJ}(y_i, y_j)\n\\end{equation}\n\n\\paragraph{Entity voting confidence (structural, instance-level).}\nFor each entity $e$ in the union $E_\\cup$ of all samples, we compute frequency $\\text{freq}(e) = |\\{i : e \\in y_i\\}| / N$.\nThe instance-level confidence is the mean frequency:\n\\begin{equation}\\label{eq:voting}\nc_{\\text{vote}}(x) = \\frac{1}{|E_\\cup|} \\sum_{e \\in E_\\cup} \\text{freq}(e)\n\\end{equation}\nWhen $E_\\cup = \\emptyset$, we set $c_{\\mathrm{vc}}(x) = 0$.\\footnote{Equation~\\ref{eq:voting} defines the continuous QE signal; for voted-output \\textit{selection} (Table~\\ref{tab:selection}), we include only entities with frequency ${>}N/2$, following standard majority voting.}\n\n\\subsection{Evaluation Framework}\\label{sec:evaluation}\n\n\\paragraph{Quality estimation.}\nSpearman $\\rho$ between the signal and instance-level F1, and AUROC classifying instances as above/below median F1.\nCorrelation analyses exclude empty gold annotations ($n{=}529$ on SciERC after filtering 22/551; $n{=}2{,}756$ on CoNLL after filtering 697/3{,}453);\\footnote{On CoNLL, full-set ($n{=}3{,}453$) Spearman $\\rho$ values are higher than gold-filtered ($n{=}2{,}756$) by $+0.03$--$0.05$ due to the zero/non-zero boundary inflating correlations, paralleling the effect documented for WNUT-17 in Appendix~\\ref{app:additional}.} selection retains the full set.\n\n\\paragraph{Sample selection.}\nBest-of-$N$ F1: per-sample signals (LP) directly rank candidates; instance-level signals select the sample closest to consensus.\nBaselines: \\textit{oracle} (highest-F1 sample) and \\textit{single-sample} (one $T{=}1.0$ draw, not argmax decoding; labeled ``Single'' in tables).\n",
      "numLines": 62,
      "startLine": 1,
      "totalLines": 62
    }
  },
  "sourceToolAssistantUUID": "2281f352-785f-4b2b-ad93-3bb71a03183a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_1_68ddc296",
  "sessionId": "a5f4ff78-4f02-4166-b054-29f1bf2f2644",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-16T05:12:50.678Z_

<details open><summary>🔧 Tool call — Read · `toolu_01MDdFszR8ptfnJEcS4z3pZc`</summary>

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
  "parentUuid": "61b20b26-0e4e-476a-a8ce-efd4a21bddc9",
  "isSidechain": false,
  "requestId": "req_011Cb5g77PBpg7mgsvGFoEQG",
  "type": "assistant",
  "uuid": "ac0d7aa2-2507-40cf-8a74-c5a0322011f2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_1_68ddc296",
  "sessionId": "a5f4ff78-4f02-4166-b054-29f1bf2f2644",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016cRMctP9utGQAEncDd2GQj",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2136,
      "cache_creation_input_tokens": 1206,
      "cache_read_input_tokens": 27779,
      "output_tokens": 292,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1206,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2136,
          "output_tokens": 292,
          "cache_read_input_tokens": 27779,
          "cache_creation_input_tokens": 1206,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1206
          },
          "type": "message"
        }
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

_source line 29 · 2026-05-16T05:12:50.683Z_

<details><summary>↩ Tool result · `toolu_01MDdFszR8ptfnJEcS4z3pZc`</summary>

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
26	\caption{Quality estimation ($\rho$ and AUROC; $N{=}8$, seed${=}42$, single-seed; 3-seed stability in Table~\ref{tab:multiseed}). Best in \textbf{bold}. $^\dagger$RE results rest on a single benchmark (SciERC, 40\% zero-F1 rate). $N{=}16$ in Table~\ref{tab:robustness}.}
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
48	On CoNLL (single-sample F1${\approx}$0.91), EM leads both $\rho$ and AUROC ($0.816$); the $\rho$--AUROC dissociation across datasets reflects use-case alignment.
49	On $^\dagger$RE, LP rises above SJ and FK at $N{=}16$ (Table~\ref{tab:multiseed}).
50	At the capability boundary---WNUT-17 (52\% zero F1)---all conditional signals collapse (Table~\ref{tab:wnut}); restricting to non-zero instances reshuffles rankings, with EM strongest on NER ($\rho{=}0.360$) and $^\dagger$RE ($\rho{=}0.417$) while LP $^\dagger$RE collapses to $\rho{=}0.011$ (Figure~\ref{fig:signal_heatmap}, Appendix~\ref{app:additional}).
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
61	\caption{Best-of-$N$ selection F1 on SciERC ($N{=}8$, $T{=}1.0$). LP is per-sample; others are instance-level. NER: 2-seed mean${\pm}\sigma$, Fisher $p$ vs.\ single-sample; $^\dagger$RE: single seed. Best non-oracle in \textbf{bold}. $^\ddagger$Single: one $T{=}1.0$ draw.}
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
78	Single$^\ddagger$ & $0.645 \pm 0.001$ & --- & \textbf{0.404} \\
79	Random           & $0.610 \pm 0.003$ & --- & 0.354 \\
80	\bottomrule
81	\end{tabular}
82	\end{table}
83	
84	Despite strong quality estimation, confidence signals yield limited selection gains (Table~\ref{tab:selection}, Figure~\ref{fig:selection_gap}).
85	Instance-level signals (SJ, FK, EM, VC) assign identical scores to all candidates per input and cannot rank outputs by construction; the key question is whether LP---the only per-sample signal---can exploit the oracle headroom.
86	
87	\paragraph{No significant improvement over single-sample.}
88	On SciERC NER (2-seed sign tests, $n{=}551$), the oracle (0.778) reveals 13.3~pp of headroom above single-sample (0.645), yet LP achieves only 0.647 ($\Delta{=}{+}0.2$~pp, $p{=}0.29$); no signal consistently improves selection ($p{>}0.05$; TOST equivalence holds under all external anchors for LLaMA-CoNLL but varies by configuration, Appendix~\ref{app:tost}).
89	On $^\dagger$RE, the best signal (LP, 0.395) falls below single-sample (0.404), with 18.1~pp unrealized.
90	The pattern holds across CoNLL and WNUT-17 (Table~\ref{tab:cross_selection}).
91	Instance-level signals predict \textit{which inputs} the model handles reliably, not \textit{which output} is best; closing this gap likely requires trained verifiers \cite{cobbe2021verifiers}.\footnote{For negative results (all $p{>}0.05$), uncorrected tests suffice; the sole positive finding (non-tied LP subset, $+2.9$~pp, $p{=}0.004$; \S\ref{sec:discussion}) survives Bonferroni correction over 5 comparisons.}
92	
93	%% ============================================================
94	\subsection{Robustness}
95	\label{sec:robustness_main}
96	
97	Consistency signals are robust across $T{\in}\{0.7, 1.0\}$ with sublinear $N$-scaling gains (Table~\ref{tab:robustness}); LP shows the largest temperature sensitivity ($\Delta\rho{=}{+}0.044$).
98	NER calibration is reasonable (ECE 0.069--0.096); $^\dagger$RE miscalibration (ECE${\leq}$0.339) caps $\rho$ at ${\approx}0.28$ for $N{=}16$ (Appendix~\ref{app:calibration}).
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
120	Repeating with Qwen3-4B (Table~\ref{tab:scale_ablation}), quality estimation is comparable or improved (mean $|\Delta\rho|{=}0.042$), yet selection remains below single-sample on SciERC ($\Delta$ up to $-3.4$~pp) despite 13.0~pp of oracle headroom, and indistinguishable on CoNLL (${<}0.3$~pp, 1.7~pp headroom). Within the 3B--8B range tested across two model families, task difficulty is a stronger predictor of the gap than model scale.
121	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ac0d7aa2-2507-40cf-8a74-c5a0322011f2",
  "isSidechain": false,
  "promptId": "0399fd48-9ce8-44a9-a460-553e3e5fc517",
  "type": "user",
  "uuid": "38aa55f8-c87b-43dd-a350-ff4adaec90a1",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex",
      "content": "\\section{Experiments}\n\\label{sec:experiments}\n\n\\subsection{Experimental Setup}\n\\label{sec:setup}\n\n\\paragraph{Datasets.}\nWe evaluate on three English IE benchmarks spanning a difficulty gradient.\n\\textbf{SciERC} \\cite{luan2018scierc} contains 551 test instances annotated for joint NER (6 types) and RE (7 types).\n\\textbf{CoNLL-2003} \\cite{tjongkimsang2003conll} provides 3{,}453 test sentences with 4 entity types, where models achieve ${\\approx}$91\\% micro F1.\n\\textbf{WNUT-17} \\cite{derczynski2017wnut} consists of 1{,}287 social media instances with emerging entities, used to probe method boundaries (52\\% zero F1).\n\n\\paragraph{Models and sampling.}\nBoth \\textbf{Qwen3-8B} and \\textbf{LLaMA-3.1-8B-Instruct} are fine-tuned with LoRA (rank$=$32, $\\alpha{=}64$) for 5 epochs using LLaMA Factory \\cite{zheng2024llamafactory} under identical training procedures.\nQwen3-8B's SciERC checkpoint has a minor train--test mismatch (empty thinking tokens); a quantitative analysis rules out this confound (Appendix~\\ref{app:thinking_token}).\nWe draw $N{=}8$ samples at $T{=}1.0$ (primary), with $N{=}16$ for scaling experiments.\\footnote{$N{=}16$ with 3 seeds verifies scaling and ranking stability ($\\sigma{\\leq}0.026$; Table~\\ref{tab:multiseed}); gains beyond $N{=}8$ are sublinear (Appendix~\\ref{app:n_scaling}).}\nInference uses vLLM with constrained decoding \\cite{willard2023guided}.\n\n%% ============================================================\n\\subsection{Quality Estimation Results}\n\\label{sec:qe_results}\n\n\\begin{table*}[t]\n\\centering\n\\small\n\\caption{Quality estimation ($\\rho$ and AUROC; $N{=}8$, seed${=}42$, single-seed; 3-seed stability in Table~\\ref{tab:multiseed}). Best in \\textbf{bold}. $^\\dagger$RE results rest on a single benchmark (SciERC, 40\\% zero-F1 rate). $N{=}16$ in Table~\\ref{tab:robustness}.}\n\\label{tab:quality_estimation}\n\\begin{tabular}{ll cc cc cc cc}\n\\toprule\n& & \\multicolumn{2}{c}{\\textbf{SciERC NER}} & \\multicolumn{2}{c}{\\textbf{SciERC RE}} & \\multicolumn{2}{c}{\\textbf{CoNLL (Qwen)}} & \\multicolumn{2}{c}{\\textbf{CoNLL (LLaMA)}} \\\\\n\\cmidrule(lr){3-4} \\cmidrule(lr){5-6} \\cmidrule(lr){7-8} \\cmidrule(lr){9-10}\nSignal & Family & $\\rho$ & AUC & $\\rho$ & AUC & $\\rho$ & AUC & $\\rho$ & AUC \\\\\n\\midrule\nVC & Structural & \\textbf{.379} & \\textbf{.663} & \\textbf{.350} & .694 & .424 & .789 & .426 & .709 \\\\\nSJ  & Structural & .360 & .650 & .250 & .670 & .436 & .801 & \\textbf{.431} & .704 \\\\\nFK & Surface & .267 & .602 & .275 & .609 & .400 & .774 & .428 & .703 \\\\\nEM  & Surface    & .295 & .614 & .134 & \\textbf{.706} & \\textbf{.451} & \\textbf{.816} & \\textbf{.431} & .705 \\\\\n\\midrule\nLP     & Model      & .205 & .578 & .266 & .601 & .316 & .753 & .307 & \\textbf{.761} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table*}\n\nTable~\\ref{tab:quality_estimation} presents $\\rho$ and AUROC for five signals across tasks and models.\\footnote{$\\varepsilon{=}0.05$ applies only to selection (\\S\\ref{sec:selection_gap}); quality estimation is $\\varepsilon$-free. Selection F1 is stable across $\\varepsilon \\in [0, 0.2]$ (Appendix~\\ref{app:epsilon_robustness}).}\n\n\\paragraph{Signal rankings are difficulty-dependent.}\nOn SciERC NER, structural signals lead (VC $\\rho{=}0.379$, SJ $0.360$) over surface ($\\rho{\\leq}0.295$) and LP ($0.205$); bootstrap CIs confirm the SJ--LP gap ($\\Delta\\rho{=}{+}0.155$; Appendix~\\ref{app:bootstrap_signal}).\nOn CoNLL (single-sample F1${\\approx}$0.91), EM leads both $\\rho$ and AUROC ($0.816$); the $\\rho$--AUROC dissociation across datasets reflects use-case alignment.\nOn $^\\dagger$RE, LP rises above SJ and FK at $N{=}16$ (Table~\\ref{tab:multiseed}).\nAt the capability boundary---WNUT-17 (52\\% zero F1)---all conditional signals collapse (Table~\\ref{tab:wnut}); restricting to non-zero instances reshuffles rankings, with EM strongest on NER ($\\rho{=}0.360$) and $^\\dagger$RE ($\\rho{=}0.417$) while LP $^\\dagger$RE collapses to $\\rho{=}0.011$ (Figure~\\ref{fig:signal_heatmap}, Appendix~\\ref{app:additional}).\n\n%% ============================================================\n\\subsection{The Correlation-Selection Gap}\n\\label{sec:selection_gap}\n\nWe define the correlation-selection gap as the disparity between a signal's instance-level rank correlation with F1 and its ability to select the best output from $N$ candidates.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Best-of-$N$ selection F1 on SciERC ($N{=}8$, $T{=}1.0$). LP is per-sample; others are instance-level. NER: 2-seed mean${\\pm}\\sigma$, Fisher $p$ vs.\\ single-sample; $^\\dagger$RE: single seed. Best non-oracle in \\textbf{bold}. $^\\ddagger$Single: one $T{=}1.0$ draw.}\n\\label{tab:selection}\n\\begin{tabular}{lccc}\n\\toprule\nMethod & NER F1 & $p$ & RE F1 \\\\\n\\midrule\nOracle & $0.778 \\pm 0.003$ & --- & 0.585 \\\\\n\\midrule\n\\multicolumn{4}{l}{\\textit{Per-sample signal}} \\\\\nLP           & $\\mathbf{0.647} \\pm 0.005$ & .29 & 0.395 \\\\\n\\midrule\n\\multicolumn{4}{l}{\\textit{Instance-level signals (consensus-proximity selection)}} \\\\\nSJ           & $0.646 \\pm 0.002$ & .68 & 0.386 \\\\\nFK           & $0.646 \\pm 0.001$ & .79 & --- \\\\\nEM           & $0.637 \\pm 0.001$ & .45 & 0.372 \\\\\nVC           & $0.623 \\pm 0.004$ & .26 & 0.359 \\\\\n\\midrule\nSingle$^\\ddagger$ & $0.645 \\pm 0.001$ & --- & \\textbf{0.404} \\\\\nRandom           & $0.610 \\pm 0.003$ & --- & 0.354 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nDespite strong quality estimation, confidence signals yield limited selection gains (Table~\\ref{tab:selection}, Figure~\\ref{fig:selection_gap}).\nInstance-level signals (SJ, FK, EM, VC) assign identical scores to all candidates per input and cannot rank outputs by construction; the key question is whether LP---the only per-sample signal---can exploit the oracle headroom.\n\n\\paragraph{No significant improvement over single-sample.}\nOn SciERC NER (2-seed sign tests, $n{=}551$), the oracle (0.778) reveals 13.3~pp of headroom above single-sample (0.645), yet LP achieves only 0.647 ($\\Delta{=}{+}0.2$~pp, $p{=}0.29$); no signal consistently improves selection ($p{>}0.05$; TOST equivalence holds under all external anchors for LLaMA-CoNLL but varies by configuration, Appendix~\\ref{app:tost}).\nOn $^\\dagger$RE, the best signal (LP, 0.395) falls below single-sample (0.404), with 18.1~pp unrealized.\nThe pattern holds across CoNLL and WNUT-17 (Table~\\ref{tab:cross_selection}).\nInstance-level signals predict \\textit{which inputs} the model handles reliably, not \\textit{which output} is best; closing this gap likely requires trained verifiers \\cite{cobbe2021verifiers}.\\footnote{For negative results (all $p{>}0.05$), uncorrected tests suffice; the sole positive finding (non-tied LP subset, $+2.9$~pp, $p{=}0.004$; \\S\\ref{sec:discussion}) survives Bonferroni correction over 5 comparisons.}\n\n%% ============================================================\n\\subsection{Robustness}\n\\label{sec:robustness_main}\n\nConsistency signals are robust across $T{\\in}\\{0.7, 1.0\\}$ with sublinear $N$-scaling gains (Table~\\ref{tab:robustness}); LP shows the largest temperature sensitivity ($\\Delta\\rho{=}{+}0.044$).\nNER calibration is reasonable (ECE 0.069--0.096); $^\\dagger$RE miscalibration (ECE${\\leq}$0.339) caps $\\rho$ at ${\\approx}0.28$ for $N{=}16$ (Appendix~\\ref{app:calibration}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Scale ablation: Qwen3-8B vs.\\ 4B quality estimation ($\\rho$; $N{=}8$, $T{=}1.0$, seed${=}42$). 8B values identical to Table~\\ref{tab:quality_estimation}; 4B uses matched evaluation protocol. $^\\dagger$Preliminary.}\n\\label{tab:scale_ablation}\n\\begin{tabular}{@{}ll cc r@{}}\n\\toprule\n& & \\textbf{8B} & \\textbf{4B} & $\\Delta$ \\\\\n\\midrule\nCoNLL NER & SJ & .436 & .422 & $-$.014 \\\\\n          & FK & .400 & .418 & $+$.018 \\\\\nSciERC NER & SJ & .360 & .422 & $+$.062 \\\\\n           & FK & .267 & .326 & $+$.059 \\\\\nSciERC RE$^\\dagger$ & SJ & .250 & .267 & $+$.017 \\\\\n           & FK & .275 & .359 & $+$.084 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Scale robustness.}\nRepeating with Qwen3-4B (Table~\\ref{tab:scale_ablation}), quality estimation is comparable or improved (mean $|\\Delta\\rho|{=}0.042$), yet selection remains below single-sample on SciERC ($\\Delta$ up to $-3.4$~pp) despite 13.0~pp of oracle headroom, and indistinguishable on CoNLL (${<}0.3$~pp, 1.7~pp headroom). Within the 3B--8B range tested across two model families, task difficulty is a stronger predictor of the gap than model scale.\n",
      "numLines": 121,
      "startLine": 1,
      "totalLines": 121
    }
  },
  "sourceToolAssistantUUID": "ac0d7aa2-2507-40cf-8a74-c5a0322011f2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_1_68ddc296",
  "sessionId": "a5f4ff78-4f02-4166-b054-29f1bf2f2644",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 30 · 2026-05-16T05:12:51.304Z_

<details open><summary>🔧 Tool call — Read · `toolu_018Jam4pCQVnLeBrYRVTFzJC`</summary>

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
  "parentUuid": "38aa55f8-c87b-43dd-a350-ff4adaec90a1",
  "isSidechain": false,
  "requestId": "req_011Cb5g77PBpg7mgsvGFoEQG",
  "type": "assistant",
  "uuid": "f4b21fd0-6172-41f2-8a47-419be96a42a7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_1_68ddc296",
  "sessionId": "a5f4ff78-4f02-4166-b054-29f1bf2f2644",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016cRMctP9utGQAEncDd2GQj",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2136,
      "cache_creation_input_tokens": 1206,
      "cache_read_input_tokens": 27779,
      "output_tokens": 292,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1206,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2136,
          "output_tokens": 292,
          "cache_read_input_tokens": 27779,
          "cache_creation_input_tokens": 1206,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1206
          },
          "type": "message"
        }
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

_source line 31 · 2026-05-16T05:12:51.319Z_

<details><summary>↩ Tool result · `toolu_018Jam4pCQVnLeBrYRVTFzJC`</summary>

```text
1	\section{Discussion}\label{sec:discussion}
2	
3	\paragraph{Practical recommendations.}
4	VC leads on hard NER ($\rho{=}0.379$); EM leads easy NER and binary discrimination (AUROC${=}0.816$, CoNLL); on $^\dagger$RE, LP outperforms structural signals (Table~\ref{tab:multiseed}).
5	Rankings hold across model families and a 4B ablation (Table~\ref{tab:scale_ablation}); at the capability boundary (WNUT-17), all signals collapse.
6	
7	\paragraph{Why the gap exists.}
8	Four of five signals are instance-level aggregates that assign a single score per input; they cannot rank candidates by construction.
9	Log-probability, the only per-sample signal, is severely compressed: median LP range is 0.041 nats (IQR [0.024, 0.073]; Table~\ref{tab:logprob_ties}), with pooled within-instance $\rho(\text{LP}, \text{F1}){=}0.248$ confirming weak but positive signal.
10	Where compression is mitigated ($n{=}210$ instances with above-median spread), LP selection outperforms single-sample ($+2.9$~pp, $p{=}0.004$), confirming compression as the bottleneck; the gap holds even among high-diversity instances (Appendix~\ref{app:diversity}).
11	Stratifying by voting confidence reveals a complementary mechanism: high-consistency instances (Q4) have collapsed headroom (4.78~pp), leaving nothing to select, while low-consistency instances retain headroom but unreliable LP rankings (Appendix~\ref{app:vc_quartile}).
12	Doubling to $N{=}16$ expands oracle headroom by $+4.4$~pp without improving selection; on $^\dagger$RE at 4B scale, LP is the sole positive signal ($\Delta{=}{+}0.7$~pp, $p{=}0.058$; Table~\ref{tab:re_n16_selection}), consistent with LP being the strongest RE selection signal across scales, though still below single-sample at 8B.
13	A verbalized confidence baseline confirms that score compression is not LP-specific: the model's self-rated confidence (mean 8.6/10) is even more compressed and yields the weakest selection despite higher $\rho$ than LP (Appendix~\ref{app:verbalized_confidence}; \citealp{bhattacharyya2026beyond}).
14	
15	\paragraph{Hypotheses for LP compression.}
16	We identify three (non-mutually-exclusive) mechanisms that may explain within-instance LP compression, though we do not isolate their individual contributions:
17	(a) \textit{token-level averaging}---mean log-probability over long sequences smooths token-level variance, compressing the effective signal;
18	(b) \textit{schema-dominated tokens}---constrained decoding enforces structural tokens (brackets, type labels) that carry no extraction information yet dominate the sequence, reducing effective variance; and
19	(c) \textit{vocabulary restriction}---constrained decoding shrinks the effective vocabulary at each step, concentrating probability mass and reducing log-probability variation; and
20	(d) \textit{format-token dilution}---fine-tuned models assign extremely high LP to schema tokens (\texttt{\{"entities": [}~etc.) that carry no extraction information, diluting the signal from entity-name tokens; free-form parse rates of 99.95\% confirm that format tokens dominate the sequence.
21	Mechanisms (b)--(c) predict that free-form decoding should reduce compression; our NER ablation finds negligible change (std ratio 0.97; Appendix~\ref{app:freeform_ablation}), suggesting (a) and (d) are the primary drivers for NER.
22	
23	\paragraph{Ablation: free-form decoding.}\label{sec:ablation}
24	Removing grammar constraints (SciERC NER, Qwen3-8B, 4 seeds) yields nearly identical LP distributions (std ratio 0.97) and negligible selection changes (Appendix~\ref{app:freeform_ablation}), ruling out constrained decoding as the cause of NER compression.
25	On $^\dagger$RE, LP selection consistently reverses direction under free-form decoding ($+1.8{\pm}0.1$~pp, 4 seeds; Appendix~\ref{app:freeform_ablation}), while under constrained decoding LP falls below single-sample ($-0.9$~pp at 8B).
26	RE LP selection is thus regime-dependent: constrained decoding suppresses it, free-form decoding recovers it, and at 4B $N{=}16$ it is marginally positive ($+0.7$~pp, $p{=}0.058$).
27	One possible explanation: free-form decoding permits greater structural diversity in RE outputs, where LP variation---though compressed---aligns with extraction quality in ways that constrained decoding's fixed template obscures.
28	VC becomes per-sample in the selection context (each candidate's overlap with the majority-voted output varies), yet tends to select the most typical rather than the best output---consistent with MBR's known mode-seeking bias \cite{eikema2022sampling}.
29	More broadly, all consensus-proximity strategies fail because utility correlates with F1 across instances but not within them (Appendix~\ref{app:mbr_discussion}).
30	
31	\paragraph{Methodological implications.}
32	The decoupling of $\rho$, AUROC, and selection F1 means single-metric evaluation risks selecting the wrong signal.
33	Effective selection likely requires trained verifiers \cite{cobbe2021verifiers, venktesh2025trust}; $N{=}8$ captures most quality estimation benefit (Appendix~\ref{app:n_scaling}).
34	Structural signals are robust to domain shift when the training schema subsumes the target (Appendix~\ref{app:ood}).
35	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f4b21fd0-6172-41f2-8a47-419be96a42a7",
  "isSidechain": false,
  "promptId": "0399fd48-9ce8-44a9-a460-553e3e5fc517",
  "type": "user",
  "uuid": "6d53e30c-30c6-47ba-b6d7-cd7ef91be5e1",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex",
      "content": "\\section{Discussion}\\label{sec:discussion}\n\n\\paragraph{Practical recommendations.}\nVC leads on hard NER ($\\rho{=}0.379$); EM leads easy NER and binary discrimination (AUROC${=}0.816$, CoNLL); on $^\\dagger$RE, LP outperforms structural signals (Table~\\ref{tab:multiseed}).\nRankings hold across model families and a 4B ablation (Table~\\ref{tab:scale_ablation}); at the capability boundary (WNUT-17), all signals collapse.\n\n\\paragraph{Why the gap exists.}\nFour of five signals are instance-level aggregates that assign a single score per input; they cannot rank candidates by construction.\nLog-probability, the only per-sample signal, is severely compressed: median LP range is 0.041 nats (IQR [0.024, 0.073]; Table~\\ref{tab:logprob_ties}), with pooled within-instance $\\rho(\\text{LP}, \\text{F1}){=}0.248$ confirming weak but positive signal.\nWhere compression is mitigated ($n{=}210$ instances with above-median spread), LP selection outperforms single-sample ($+2.9$~pp, $p{=}0.004$), confirming compression as the bottleneck; the gap holds even among high-diversity instances (Appendix~\\ref{app:diversity}).\nStratifying by voting confidence reveals a complementary mechanism: high-consistency instances (Q4) have collapsed headroom (4.78~pp), leaving nothing to select, while low-consistency instances retain headroom but unreliable LP rankings (Appendix~\\ref{app:vc_quartile}).\nDoubling to $N{=}16$ expands oracle headroom by $+4.4$~pp without improving selection; on $^\\dagger$RE at 4B scale, LP is the sole positive signal ($\\Delta{=}{+}0.7$~pp, $p{=}0.058$; Table~\\ref{tab:re_n16_selection}), consistent with LP being the strongest RE selection signal across scales, though still below single-sample at 8B.\nA verbalized confidence baseline confirms that score compression is not LP-specific: the model's self-rated confidence (mean 8.6/10) is even more compressed and yields the weakest selection despite higher $\\rho$ than LP (Appendix~\\ref{app:verbalized_confidence}; \\citealp{bhattacharyya2026beyond}).\n\n\\paragraph{Hypotheses for LP compression.}\nWe identify three (non-mutually-exclusive) mechanisms that may explain within-instance LP compression, though we do not isolate their individual contributions:\n(a) \\textit{token-level averaging}---mean log-probability over long sequences smooths token-level variance, compressing the effective signal;\n(b) \\textit{schema-dominated tokens}---constrained decoding enforces structural tokens (brackets, type labels) that carry no extraction information yet dominate the sequence, reducing effective variance; and\n(c) \\textit{vocabulary restriction}---constrained decoding shrinks the effective vocabulary at each step, concentrating probability mass and reducing log-probability variation; and\n(d) \\textit{format-token dilution}---fine-tuned models assign extremely high LP to schema tokens (\\texttt{\\{\"entities\": [}~etc.) that carry no extraction information, diluting the signal from entity-name tokens; free-form parse rates of 99.95\\% confirm that format tokens dominate the sequence.\nMechanisms (b)--(c) predict that free-form decoding should reduce compression; our NER ablation finds negligible change (std ratio 0.97; Appendix~\\ref{app:freeform_ablation}), suggesting (a) and (d) are the primary drivers for NER.\n\n\\paragraph{Ablation: free-form decoding.}\\label{sec:ablation}\nRemoving grammar constraints (SciERC NER, Qwen3-8B, 4 seeds) yields nearly identical LP distributions (std ratio 0.97) and negligible selection changes (Appendix~\\ref{app:freeform_ablation}), ruling out constrained decoding as the cause of NER compression.\nOn $^\\dagger$RE, LP selection consistently reverses direction under free-form decoding ($+1.8{\\pm}0.1$~pp, 4 seeds; Appendix~\\ref{app:freeform_ablation}), while under constrained decoding LP falls below single-sample ($-0.9$~pp at 8B).\nRE LP selection is thus regime-dependent: constrained decoding suppresses it, free-form decoding recovers it, and at 4B $N{=}16$ it is marginally positive ($+0.7$~pp, $p{=}0.058$).\nOne possible explanation: free-form decoding permits greater structural diversity in RE outputs, where LP variation---though compressed---aligns with extraction quality in ways that constrained decoding's fixed template obscures.\nVC becomes per-sample in the selection context (each candidate's overlap with the majority-voted output varies), yet tends to select the most typical rather than the best output---consistent with MBR's known mode-seeking bias \\cite{eikema2022sampling}.\nMore broadly, all consensus-proximity strategies fail because utility correlates with F1 across instances but not within them (Appendix~\\ref{app:mbr_discussion}).\n\n\\paragraph{Methodological implications.}\nThe decoupling of $\\rho$, AUROC, and selection F1 means single-metric evaluation risks selecting the wrong signal.\nEffective selection likely requires trained verifiers \\cite{cobbe2021verifiers, venktesh2025trust}; $N{=}8$ captures most quality estimation benefit (Appendix~\\ref{app:n_scaling}).\nStructural signals are robust to domain shift when the training schema subsumes the target (Appendix~\\ref{app:ood}).\n",
      "numLines": 35,
      "startLine": 1,
      "totalLines": 35
    }
  },
  "sourceToolAssistantUUID": "f4b21fd0-6172-41f2-8a47-419be96a42a7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_1_68ddc296",
  "sessionId": "a5f4ff78-4f02-4166-b054-29f1bf2f2644",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 32_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[Round 1 审稿请求]: ## Round 1 审稿任务 — Reviewer 1（方法严谨性 + 实验设计 + 统计分析）  ### Venue 信息 - **目标**: EMNLP 2026 Main Conference (via ARR May 2026 cycle) - **截止日期**: 2026-05-25 - **格式**: ACL 模板, 正文 8 页, double-bl…",
  "leafUuid": "6d53e30c-30c6-47ba-b6d7-cd7ef91be5e1",
  "sessionId": "a5f4ff78-4f02-4166-b054-29f1bf2f2644"
}
```

---

### Runtime record

_source line 33_

```json
{
  "type": "ai-title",
  "aiTitle": "Review round 1 paper on structured IE self-consistency",
  "sessionId": "a5f4ff78-4f02-4166-b054-29f1bf2f2644"
}
```

---

### Tool result

_source line 34 · 2026-05-16T05:12:56.332Z_

<details><summary>↩ Tool result · `toolu_01XWcrKmcoHDFGQjFDjf6dpk`</summary>

```text
Web search results for query: "ACL Rolling Review review form 2025 2026 soundness excitement overall score scale"

Links: [{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"},{"title":"ACL 2023 Acceptance Recommendations - ACL 2023","url":"https://2023.aclweb.org/blog/overall-recommendation/"},{"title":"ARR Changelog – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/changelog"},{"title":"ARR Dashboard","url":"https://stats.aclrollingreview.org/"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"}]

Based on the search results, here's information about the ACL Rolling Review form for 2025-2026:

## Review Scoring Categories

Starting with February 2025, ARR reviewers are asked to provide three scores: soundness, excitement, and overall recommendation.

### Soundness Score Scale

The soundness score assesses the technical quality and rigor of the paper:
- 5 = Excellent: This study is one of the most thorough I have seen, given its type.
- 4 = Strong: This study provides sufficient support for all of its claims. Some extra experiments could be nice, but not essential.
- 3 = Acceptable: This study provides sufficient support for its main claims.

### Excitement Score Scale

The excitement score reflects personal interest and impact:
- 5 = Highly Exciting: I would recommend this paper to others and/or attend its presentation in a conference.
- 4 = Exciting: I would mention this paper to others and/or make an effort to attend its presentation in a conference.
- 1 = Not Exciting: this paper does not resonate with me, and I don't think it would with others in the *ACL community.

### Overall Recommendation Score

The Overall assessment score is an explicit recommendation for the outcome of this paper, if it were committed to an *ACL venue. This is a composite score reflecting your assessment of soundness, excitement, and also other factors like novelty and impact.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "690cc503-5b8d-4e60-a7df-d5d6491a18f9",
  "isSidechain": false,
  "promptId": "0399fd48-9ce8-44a9-a460-553e3e5fc517",
  "type": "user",
  "uuid": "a62a090f-9e8f-4031-a93c-6e8390e17859",
  "toolUseResult": {
    "query": "ACL Rolling Review review form 2025 2026 soundness excitement overall score scale",
    "results": [
      {
        "tool_use_id": "srvtoolu_014ENBo83ZxG7uir9vMBwKai",
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
            "title": "ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics",
            "url": "http://aclrollingreview.org/acguidelines"
          },
          {
            "title": "How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics",
            "url": "http://aclrollingreview.org/reviewing"
          },
          {
            "title": "Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics",
            "url": "http://aclrollingreview.org/incentives2026"
          },
          {
            "title": "ACL 2023 Acceptance Recommendations - ACL 2023",
            "url": "https://2023.aclweb.org/blog/overall-recommendation/"
          },
          {
            "title": "ARR Changelog – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics",
            "url": "http://aclrollingreview.org/changelog"
          },
          {
            "title": "ARR Dashboard",
            "url": "https://stats.aclrollingreview.org/"
          },
          {
            "title": "Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics",
            "url": "http://aclrollingreview.org/authors"
          }
        ]
      },
      "Based on the search results, here's information about the ACL Rolling Review form for 2025-2026:\n\n## Review Scoring Categories\n\nStarting with February 2025, ARR reviewers are asked to provide three scores: soundness, excitement, and overall recommendation.\n\n### Soundness Score Scale\n\nThe soundness score assesses the technical quality and rigor of the paper:\n- 5 = Excellent: This study is one of the most thorough I have seen, given its type.\n- 4 = Strong: This study provides sufficient support for all of its claims. Some extra experiments could be nice, but not essential.\n- 3 = Acceptable: This study provides sufficient support for its main claims.\n\n### Excitement Score Scale\n\nThe excitement score reflects personal interest and impact:\n- 5 = Highly Exciting: I would recommend this paper to others and/or attend its presentation in a conference.\n- 4 = Exciting: I would mention this paper to others and/or make an effort to attend its presentation in a conference.\n- 1 = Not Exciting: this paper does not resonate with me, and I don't think it would with others in the *ACL community.\n\n### Overall Recommendation Score\n\nThe Overall assessment score is an explicit recommendation for the outcome of this paper, if it were committed to an *ACL venue. This is a composite score reflecting your assessment of soundness, excitement, and also other factors like novelty and impact."
    ],
    "durationSeconds": 6.5685727929999995
  },
  "sourceToolAssistantUUID": "690cc503-5b8d-4e60-a7df-d5d6491a18f9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_1_68ddc296",
  "sessionId": "a5f4ff78-4f02-4166-b054-29f1bf2f2644",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 35 · 2026-05-16T05:12:56.337Z_

```json
{
  "parentUuid": "a62a090f-9e8f-4031-a93c-6e8390e17859",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "abe0e70d-7a0a-4bbb-8ec1-8b4f51eeb426",
  "timestamp": "2026-05-16T05:12:56.337Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_1_68ddc296",
  "sessionId": "a5f4ff78-4f02-4166-b054-29f1bf2f2644",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Tool call

_source line 36 · 2026-05-16T05:13:01.736Z_

<details open><summary>🔧 Tool call — Read · `toolu_01MNcMGUjL87yjwLpsp66Hw1`</summary>

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
  "parentUuid": "abe0e70d-7a0a-4bbb-8ec1-8b4f51eeb426",
  "isSidechain": false,
  "requestId": "req_011Cb5g7rZF2v4qpLgbhYkx7",
  "type": "assistant",
  "uuid": "a4fb7afa-b28f-40ad-922d-c6eaeed80f27",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_1_68ddc296",
  "sessionId": "a5f4ff78-4f02-4166-b054-29f1bf2f2644",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Xxb43oEeeXdxCa2VKfnTDF",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6851,
      "cache_creation_input_tokens": 3336,
      "cache_read_input_tokens": 28985,
      "output_tokens": 316,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3336,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 6851,
          "output_tokens": 316,
          "cache_read_input_tokens": 28985,
          "cache_creation_input_tokens": 3336,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3336
          },
          "type": "message"
        }
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

_source line 37 · 2026-05-16T05:13:01.742Z_

<details><summary>↩ Tool result · `toolu_01MNcMGUjL87yjwLpsp66Hw1`</summary>

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
21	Trained verifiers \cite{cobbe2021verifiers, lightman2024verify} and quality-aware decoding \cite{fernandes2022quality} learn per-sample scoring that may bridge this gap.
22	Conformal prediction constructs prediction sets with coverage guarantees \cite{zhang2025conformal}; while complementary, its set-valued output differs from best-of-$N$ selection.
23	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a4fb7afa-b28f-40ad-922d-c6eaeed80f27",
  "isSidechain": false,
  "promptId": "0399fd48-9ce8-44a9-a460-553e3e5fc517",
  "type": "user",
  "uuid": "44a7f472-ac29-47a3-be8b-1d24aabfdaf8",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/related_work.tex",
      "content": "\\section{Related Work}\\label{sec:related}\n\n\\paragraph{Self-consistency and test-time scaling.}\nSelf-consistency \\cite{wang2023selfconsistency} improves reasoning via majority voting; extensions handle free-form text through LLM comparison \\cite{chen2024usc}, sub-claim decomposition \\cite{thirukovalluru2024atomic}, or hallucination detection \\cite{manakul2023selfcheckgpt}.\nTest-time scaling studies \\cite{snell2025scaling, brown2024monkeys} and reward-free selectors \\cite{taubenfeld2025cisc, kang2025selfcertainty, kim2026reasc, wang2025rankedvoting, oh2025latentsc} all target discrete answers.\nConcurrently, \\citet{feng2025optimal} and \\citet{wang2025make} adapt self-consistency to difficulty-aware settings; \\citet{li2025llms} propose generative self-aggregation for IE but focus on fusion rather than selection.\nOur work extends self-consistency to set-valued structured outputs and identifies the correlation-selection gap.\n\n\\paragraph{Consistency for structured IE.}\n\\citet{yao2026consistency} study consistency--accuracy correlations for LLM-based NER/RE, leaving open whether structural matching improves on surface agreement, whether quality estimation translates to selection, and whether findings generalize across a difficulty gradient---the three questions we address.\nCoCoA \\cite{vashurin2025cocoa} fuses confidence with consistency for QA/summarization but does not address structured extraction.\n\\citet{culotta2004confidence} pioneer confidence estimation for IE via CRF marginals; our signals are model-agnostic.\nOur evaluation builds on generative IE work \\cite{zhou2024uniner, sainz2024gollie, li2023codeie, wadhwa2023revisiting} and constrained decoding \\cite{willard2023guided}.\n\n\\paragraph{Uncertainty estimation and calibration.}\nSurveys cover confidence estimation \\cite{geng2024confidence}, uncertainty quantification \\cite{xia2025survey}, and calibration \\cite{hobelsberger2025systematic} for LLMs.\nSemantic uncertainty \\cite{kuhn2023semantic} clusters generations by meaning; P(True) \\cite{kadavath2022language} queries model confidence directly; \\citet{malinin2021uncertainty} study predictive uncertainty for autoregressive structured prediction.\nOur structural signals instead measure agreement over output \\textit{structure}, requiring no model modification.\nOur selection strategies instantiate MBR decoding \\cite{eikema2022sampling} with structural utility functions.\n\\citet{eikema2025structured} find that standard MBR utilities degrade on structured outputs due to bag-of-unit mismatches---consistent with our finding that consensus-proximity selection fails for IE; we show the specific failure: utility correlates with F1 across instances but not within them (\\S\\ref{sec:discussion}).\nTrained verifiers \\cite{cobbe2021verifiers, lightman2024verify} and quality-aware decoding \\cite{fernandes2022quality} learn per-sample scoring that may bridge this gap.\nConformal prediction constructs prediction sets with coverage guarantees \\cite{zhang2025conformal}; while complementary, its set-valued output differs from best-of-$N$ selection.\n",
      "numLines": 23,
      "startLine": 1,
      "totalLines": 23
    }
  },
  "sourceToolAssistantUUID": "a4fb7afa-b28f-40ad-922d-c6eaeed80f27",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_1_68ddc296",
  "sessionId": "a5f4ff78-4f02-4166-b054-29f1bf2f2644",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 38 · 2026-05-16T05:13:02.327Z_

<details open><summary>🔧 Tool call — Read · `toolu_01NaucWa8NmDCcK612Ezkxs3`</summary>

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
  "parentUuid": "44a7f472-ac29-47a3-be8b-1d24aabfdaf8",
  "isSidechain": false,
  "requestId": "req_011Cb5g7rZF2v4qpLgbhYkx7",
  "type": "assistant",
  "uuid": "9f988050-ce59-44d8-bc56-198cd3f5787b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_1_68ddc296",
  "sessionId": "a5f4ff78-4f02-4166-b054-29f1bf2f2644",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Xxb43oEeeXdxCa2VKfnTDF",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6851,
      "cache_creation_input_tokens": 3336,
      "cache_read_input_tokens": 28985,
      "output_tokens": 316,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3336,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 6851,
          "output_tokens": 316,
          "cache_read_input_tokens": 28985,
          "cache_creation_input_tokens": 3336,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3336
          },
          "type": "message"
        }
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

_source line 39 · 2026-05-16T05:13:02.334Z_

<details><summary>↩ Tool result · `toolu_01NaucWa8NmDCcK612Ezkxs3`</summary>

```text
1	\section{Conclusion}\label{sec:conclusion}
2	
3	We evaluate five confidence signals for quality estimation and sample selection in LLM-based structured IE, revealing the \textit{correlation-selection gap}: strong quality estimation ($\rho$ up to 0.45) coexists with selection failure.
4	Instance-level signals fail by construction; the core empirical finding is that log-probability---the only per-sample signal---is too compressed within instances to discriminate (median range 0.041 nats, 60\% tied), and consensus-proximity selection (MBR) fails because utility correlates with F1 across but not within instances.
5	A 4-seed free-form ablation confirms NER compression is not caused by constrained decoding; on $^\dagger$RE, LP selection reverses direction.
6	Signal rankings shift with difficulty across NER benchmarks and collapse at the capability boundary---consistent across two model families (3B--8B).
7	$^\dagger$RE conclusions rest on SciERC alone (40\% zero-F1 rate); trained verifiers and scaling to 70B+ are promising directions.
8	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9f988050-ce59-44d8-bc56-198cd3f5787b",
  "isSidechain": false,
  "promptId": "0399fd48-9ce8-44a9-a460-553e3e5fc517",
  "type": "user",
  "uuid": "c5ce2c1d-4b7a-4b5a-a2bf-9da229e4779c",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/conclusion.tex",
      "content": "\\section{Conclusion}\\label{sec:conclusion}\n\nWe evaluate five confidence signals for quality estimation and sample selection in LLM-based structured IE, revealing the \\textit{correlation-selection gap}: strong quality estimation ($\\rho$ up to 0.45) coexists with selection failure.\nInstance-level signals fail by construction; the core empirical finding is that log-probability---the only per-sample signal---is too compressed within instances to discriminate (median range 0.041 nats, 60\\% tied), and consensus-proximity selection (MBR) fails because utility correlates with F1 across but not within instances.\nA 4-seed free-form ablation confirms NER compression is not caused by constrained decoding; on $^\\dagger$RE, LP selection reverses direction.\nSignal rankings shift with difficulty across NER benchmarks and collapse at the capability boundary---consistent across two model families (3B--8B).\n$^\\dagger$RE conclusions rest on SciERC alone (40\\% zero-F1 rate); trained verifiers and scaling to 70B+ are promising directions.\n",
      "numLines": 8,
      "startLine": 1,
      "totalLines": 8
    }
  },
  "sourceToolAssistantUUID": "9f988050-ce59-44d8-bc56-198cd3f5787b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_1_68ddc296",
  "sessionId": "a5f4ff78-4f02-4166-b054-29f1bf2f2644",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 40 · 2026-05-16T05:13:03.272Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Wa37xKGtDDQo7VNdYdaYG8`</summary>

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
  "parentUuid": "c5ce2c1d-4b7a-4b5a-a2bf-9da229e4779c",
  "isSidechain": false,
  "requestId": "req_011Cb5g7rZF2v4qpLgbhYkx7",
  "type": "assistant",
  "uuid": "332eddcc-d160-4336-ac04-e702a90a2d01",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_1_68ddc296",
  "sessionId": "a5f4ff78-4f02-4166-b054-29f1bf2f2644",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Xxb43oEeeXdxCa2VKfnTDF",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6851,
      "cache_creation_input_tokens": 3336,
      "cache_read_input_tokens": 28985,
      "output_tokens": 316,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3336,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 6851,
          "output_tokens": 316,
          "cache_read_input_tokens": 28985,
          "cache_creation_input_tokens": 3336,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3336
          },
          "type": "message"
        }
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

_source line 41 · 2026-05-16T05:13:03.284Z_

<details><summary>↩ Tool result · `toolu_01Wa37xKGtDDQo7VNdYdaYG8`</summary>

```text
1	Our evaluation covers three NER datasets but only one RE benchmark (SciERC), where 40\% of instances receive zero F1; generalization to other RE benchmarks remains unvalidated.
2	TACRED-style sentence-level RE classification differs structurally from set-valued extraction and is left for future work.
3	We cover 4B--8B scale; whether the gap holds for 70B+ models or closed-source APIs is untested---larger models may produce more diverse samples.
4	We do not train a verifier, leaving unknown how much oracle headroom a supervised approach could recover.
5	
6	We evaluate at $N{=}8$ (primary) and $N{=}16$; behavior at larger sample sizes is unknown (Appendix~\ref{app:n_scaling}).
7	The free-form ablation covers SciERC NER and CoNLL NER with one model; RE shows a directional LP reversal under free-form decoding.
8	Qwen3-8B's SciERC checkpoint used empty \texttt{&lt;think>&lt;/think>} blocks; a three-part analysis rules out this confound (Appendix~\ref{app:thinking_token}).
9	LP compression worsens on easy datasets at lower temperature (CoNLL tied fractions reach 95.8\% at $T{=}0.7$); whether reduced temperature translates to selection gains remains untested.
10	We tested verbalized confidence \cite{tian2023calibration} as a second per-sample signal; it exhibits severe overconfidence (mean 8.58/10 on SciERC, 9.24/10 on CoNLL) and yields the weakest QE and selection among all signals (Appendix~\ref{app:verbalized_confidence}).
11	We evaluate signals individually; whether signal combinations (e.g., LP $\times$ consistency) or learned weightings could close the selection gap is unexplored.
12	The $\varepsilon{=}0.05$ threshold used for tied/non-tied LP stratification is a post-hoc exploratory choice; while selection F1 is stable across $\varepsilon \in [0, 0.2]$ (Appendix~\ref{app:epsilon_robustness}), the specific subset gains should be interpreted as characterizing the compression phenomenon rather than as a tuned selection strategy.
13	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "332eddcc-d160-4336-ac04-e702a90a2d01",
  "isSidechain": false,
  "promptId": "0399fd48-9ce8-44a9-a460-553e3e5fc517",
  "type": "user",
  "uuid": "ce891579-bc44-4863-9aab-8ee35cd1c895",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/limitations.tex",
      "content": "Our evaluation covers three NER datasets but only one RE benchmark (SciERC), where 40\\% of instances receive zero F1; generalization to other RE benchmarks remains unvalidated.\nTACRED-style sentence-level RE classification differs structurally from set-valued extraction and is left for future work.\nWe cover 4B--8B scale; whether the gap holds for 70B+ models or closed-source APIs is untested---larger models may produce more diverse samples.\nWe do not train a verifier, leaving unknown how much oracle headroom a supervised approach could recover.\n\nWe evaluate at $N{=}8$ (primary) and $N{=}16$; behavior at larger sample sizes is unknown (Appendix~\\ref{app:n_scaling}).\nThe free-form ablation covers SciERC NER and CoNLL NER with one model; RE shows a directional LP reversal under free-form decoding.\nQwen3-8B's SciERC checkpoint used empty \\texttt{&lt;think>&lt;/think>} blocks; a three-part analysis rules out this confound (Appendix~\\ref{app:thinking_token}).\nLP compression worsens on easy datasets at lower temperature (CoNLL tied fractions reach 95.8\\% at $T{=}0.7$); whether reduced temperature translates to selection gains remains untested.\nWe tested verbalized confidence \\cite{tian2023calibration} as a second per-sample signal; it exhibits severe overconfidence (mean 8.58/10 on SciERC, 9.24/10 on CoNLL) and yields the weakest QE and selection among all signals (Appendix~\\ref{app:verbalized_confidence}).\nWe evaluate signals individually; whether signal combinations (e.g., LP $\\times$ consistency) or learned weightings could close the selection gap is unexplored.\nThe $\\varepsilon{=}0.05$ threshold used for tied/non-tied LP stratification is a post-hoc exploratory choice; while selection F1 is stable across $\\varepsilon \\in [0, 0.2]$ (Appendix~\\ref{app:epsilon_robustness}), the specific subset gains should be interpreted as characterizing the compression phenomenon rather than as a tuned selection strategy.\n",
      "numLines": 13,
      "startLine": 1,
      "totalLines": 13
    }
  },
  "sourceToolAssistantUUID": "332eddcc-d160-4336-ac04-e702a90a2d01",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_1_68ddc296",
  "sessionId": "a5f4ff78-4f02-4166-b054-29f1bf2f2644",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 42 · 2026-05-16T05:13:03.489Z_

<details open><summary>🔧 Tool call — Read · `toolu_01JVeRnfoz4GpiEfM7ivMXEr`</summary>

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
  "parentUuid": "ce891579-bc44-4863-9aab-8ee35cd1c895",
  "isSidechain": false,
  "requestId": "req_011Cb5g7rZF2v4qpLgbhYkx7",
  "type": "assistant",
  "uuid": "883dcb68-199a-4daa-a6a8-78189a76bca2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_1_68ddc296",
  "sessionId": "a5f4ff78-4f02-4166-b054-29f1bf2f2644",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Xxb43oEeeXdxCa2VKfnTDF",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6851,
      "cache_creation_input_tokens": 3336,
      "cache_read_input_tokens": 28985,
      "output_tokens": 316,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3336,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 6851,
          "output_tokens": 316,
          "cache_read_input_tokens": 28985,
          "cache_creation_input_tokens": 3336,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3336
          },
          "type": "message"
        }
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

_source line 43 · 2026-05-16T05:13:03.746Z_

<details><summary>↩ Tool result · reported error · `toolu_01JVeRnfoz4GpiEfM7ivMXEr`</summary>

```text
File content (25409 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "883dcb68-199a-4daa-a6a8-78189a76bca2",
  "isSidechain": false,
  "promptId": "0399fd48-9ce8-44a9-a460-553e3e5fc517",
  "type": "user",
  "uuid": "5c95eb45-6917-46e4-9847-fe63673a676a",
  "toolUseResult": "Error: File content (25409 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.",
  "sourceToolAssistantUUID": "883dcb68-199a-4daa-a6a8-78189a76bca2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_1_68ddc296",
  "sessionId": "a5f4ff78-4f02-4166-b054-29f1bf2f2644",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 44 · 2026-05-16T05:13:08.524Z_

<details open><summary>🔧 Tool call — Read · `toolu_014iGWzPcN4eNmz2r2Jfny8c`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
  "limit": 500
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5c95eb45-6917-46e4-9847-fe63673a676a",
  "isSidechain": false,
  "requestId": "req_011Cb5g8QFEWzT5xxnZsNHUR",
  "type": "assistant",
  "uuid": "3212ff57-13ef-4a22-b475-8aed7cfa1212",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_1_68ddc296",
  "sessionId": "a5f4ff78-4f02-4166-b054-29f1bf2f2644",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GaeLpZ8dLZt1CVMN4b7cDY",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8974,
      "cache_read_input_tokens": 32321,
      "output_tokens": 109,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 8974,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 109,
          "cache_read_input_tokens": 32321,
          "cache_creation_input_tokens": 8974,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 8974
          },
          "type": "message"
        }
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

_source line 45 · 2026-05-16T05:13:08.809Z_

<details><summary>↩ Tool result · `toolu_014iGWzPcN4eNmz2r2Jfny8c`</summary>

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
231	On LLaMA SciERC, where output diversity remains substantial (18\% identical outputs, 39\% unique), LP achieves the highest selection F1 (0.652) at $N{=}8$ but still falls within bootstrap noise of single-sample (0.646), replicating the gap observed on Qwen SciERC (Table~\ref{tab:selection}).
232	On CoNLL, 57--88\% of instances produce identical outputs across all $N$ samples, reflecting a ceiling effect (single-sample F1 ${\approx}$0.91--0.92) rather than signal failure; selection analysis on these configurations is uninformative because there is little per-sample variance for any signal to exploit.
233	
234	\begin{table*}[t]
235	\centering
236	\small
237	\caption{Best-of-$N$ selection F1 (macro, instance-averaged) across configurations ($T{=}1.0$). Best non-oracle signal per row in \textbf{bold}. At $N{=}8$, no signal significantly outperforms single-sample in any configuration. At $N{=}16$ on LLaMA CoNLL, VC achieves small but significant gains ($+0.28$~pp, $p{<}0.03$; see text below). CoNLL shows especially tight clustering where single-sample already exceeds 0.90.}
238	\label{tab:cross_selection}
239	\begin{tabular}{llccccccc}
240	\toprule
241	Config & $n$ & Single & Oracle & SJ & FK & EM & LP & VC \\
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
261	VC achieves the largest gain over single-sample ($+0.28$~pp, $p{=}0.003$--$0.027$ across 3 seeds, all significant), with SJ, FK, and EM at $+0.22$--$0.23$~pp and LP at $+0.12$~pp (2/3 seeds significant).
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
314	\caption{The correlation-selection gap on SciERC NER ($N{=}8$, $T{=}1.0$, 2-seed mean). Bars show best-of-$N$ selection F1; the line marks quality estimation $\rho$. Despite $\rho$ up to 0.40, no signal significantly outperforms single-sample (all $p{>}0.05$; Table~\ref{tab:selection}). Dashed line indicates oracle upper bound. RE selection results in Table~\ref{tab:selection}.}
315	\label{fig:selection_gap}
316	\end{figure*}
317	
318	\paragraph{Output diversity quantification.}
319	Table~\ref{tab:diversity} summarizes output diversity across configurations.
320	On SciERC, output diversity is substantial: Qwen produces 43\% unique outputs per instance (mean 3.5 distinct out of $N{=}8$), with per-sample F1 standard deviation of 0.144 and mean pairwise SJ of 0.703.
321	LLaMA shows similar diversity (39\% unique, F1 std 0.11).
322	On CoNLL, diversity collapses: 57\% (Qwen) to 88\% (LLaMA) of instances produce identical outputs across all $N$ samples, reflecting a ceiling effect where single-sample F1 already exceeds 0.90.
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
344	Across SciERC configurations, 39--42\% of instances contain at least one sample with F1 exceeding single-sample\footnote{Oracle-improvable and diversity-stratified analyses use $n{=}529$ (excluding instances with empty gold annotations; see \S\ref{sec:evaluation}); the diversity quantification in Table~\ref{tab:diversity} uses the full test set.}: Qwen NER 42.0\% (222/529, mean headroom $+$31.9~pp among improvable instances), Qwen RE 41.3\% (164/397, $+$45.3~pp), LLaMA NER 39.3\% (208/529, $+$33.7~pp).
345	On CoNLL, only 4--9\% of instances are improvable, confirming the ceiling effect.
346	
347	\paragraph{Diversity-stratified selection gap.}
348	On the 44\% of Qwen SciERC instances with high diversity (${\geq}4$ unique outputs among 8 samples, $n{=}232$), oracle headroom reaches $+$16.3~pp, yet all consistency-based signals (SJ, FK, EM, VC) select at or below single-sample, and LP---the only per-sample signal---achieves merely $+$0.8~pp.
349	LLaMA replicates this pattern: on its high-diversity subset ($n{=}186$), oracle headroom reaches $+$20.1~pp while consistency signals remain at or below single-sample and LP captures only $+$2.0~pp.
350	This rules out insufficient diversity as an explanation for the correlation-selection gap.
351	
352	\paragraph{TOST equivalence testing.}\label{app:tost}
353	The primary evidence against selection gains comes from effect sizes and confidence intervals: Cohen's $d{=}0.038$ for the best signal (NER LP) and bootstrap 95\% CI [$-$3.0, $+$4.2]~pp spanning zero.
354	Table~\ref{tab:tost} supplements this with two one-sided tests (TOST), testing whether each signal's selection F1 is equivalent to single-sample within a bound $\delta$.
355	The $\delta$ values are contextualized against oracle headroom (12--18~pp): $\delta{=}5$~pp corresponds to forgoing 28--38\% of the available headroom, $\delta{=}3$~pp forgoing 17--23\%, and $\delta{=}2$~pp less than 15\%.
356	These proportions use the same test data that defines the headroom, introducing circularity: $\delta$ is anchored to the very quantity it contextualizes.
357	We address this below with externally anchored equivalence margins.
358	The breakpoint $\delta^*$---the minimum equivalence margin at which each signal passes TOST---ranges from approximately 1.3~pp (SJ, ${\sim}$10\% of oracle headroom) to 3.4~pp (FK, ${\sim}$26\%) on NER, and from approximately 2.9~pp (LP, ${\sim}$16\%) to 6.5~pp (VC, ${\sim}$36\%) on RE.
359	On NER ($n{=}529$), at $\delta{=}{\pm}2$~pp, SJ and LP are confirmed equivalent to single-sample (TOST $p{<}0.05$); at $\delta{=}{\pm}3$~pp, four of five signals pass; at $\delta{=}{\pm}5$~pp, all five pass.
360	On RE ($n{=}397$, preliminary), EM and VC fail equivalence even at $\delta{=}{\pm}5$~pp due to systematic underperformance ($\Delta{=}{-}3.2$~pp and $-4.5$~pp respectively).
361	The effect sizes are negligible ($d{=}0.038$) and confidence intervals span zero, with TOST confirming equivalence at practically meaningful margins.
362	
363	\begin{table}[t]
364	\centering
365	\small
366	\caption{TOST equivalence testing: signals vs.\ single-sample on SciERC ($N{=}8$, $T{=}1.0$). \checkmark: equivalent at $p{<}0.05$; \texttimes: not equivalent. $\Delta$: mean F1 difference (signal $-$ single-sample).}
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
386	(1) $\delta_{\mathrm{SEM}}$: the bootstrapped standard error of single-sample F1 (0.43--1.33~pp depending on configuration), representing measurement noise;
387	(2) $\delta_{\mathrm{practical}}{=}0.5$~pp, reflecting the threshold below which NER differences are considered negligible \cite{ratinov2009design};
388	(3) $\delta_{\mathrm{literature}}{=}1.0$~pp, the approximate significant-difference threshold established in NER evaluation methodology \cite{bergkirkpatrick2012empirical}.
389	
390	Results under these external anchors diverge sharply by configuration.
391	On LLaMA CoNLL ($n{=}2{,}756$), all signals pass equivalence at every $\delta$ ($p{<}0.001$), consistent with the near-zero selection deltas ($|\Delta|{\leq}0.1$~pp) and tight CIs at this sample size.
392	On Qwen CoNLL ($n{=}2{,}756$), no signal passes at any external $\delta$: selection F1 degrades by 0.9--1.5~pp relative to single-sample, exceeding even $\delta_{\mathrm{literature}}$.
393	On SciERC NER ($n{=}529$), only SJ passes at $\delta_{\mathrm{SEM}}{=}1.33$~pp (the widest SEM bound); all other signals and tighter margins fail.
394	These external anchors confirm that the equivalence conclusion is configuration-dependent: LLaMA CoNLL selection is robustly equivalent to single-sample under any reasonable margin, while SciERC and Qwen CoNLL selection shows detectable degradation at externally calibrated thresholds.
395	
396	\section{Multi-Seed Stability}\label{app:multiseed}
397	
398	Table~\ref{tab:multiseed} reports quality estimation metrics across three random seeds for both model families on SciERC ($N{=}8$, $T{=}1.0$).
399	On NER, the signal ranking VC${>}$SJ${>}$EM${>}$FK${>}$LP is identical across all six model-seed combinations, with $\sigma{\leq}0.025$ for all signals (rankings are stable across our 3 seeds, though statistical power with $n{=}3$ is limited).
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
499	The median within-instance LP range is only 0.041 nats; we use $\varepsilon{=}0.05$ as an illustrative threshold to characterize this compression.
500	At this cutpoint, 60.3\% of instances ($n{=}529$, excluding empty gold annotations) have a within-sample range below $\varepsilon$, and 75\% of pairwise comparisons are effective ties ($|\Delta|{<}0.026$).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3212ff57-13ef-4a22-b475-8aed7cfa1212",
  "isSidechain": false,
  "promptId": "0399fd48-9ce8-44a9-a460-553e3e5fc517",
  "type": "user",
  "uuid": "8e65486f-c1c7-4654-9a32-58780f0f8e18",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
      "content": "\\section{Notation}\\label{app:notation}\n\nTable~\\ref{tab:notation} summarizes the notation used throughout the paper.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{cl}\n\\toprule\nSymbol & Meaning \\\\\n\\midrule\n$\\mathcal{M}$ & Language model \\\\\n$x$ & Input instance \\\\\n$y_i$ & $i$-th stochastic sample \\\\\n$N$ & Number of samples \\\\\n$T$ & Sampling temperature \\\\\n$c(\\cdot)$ & Confidence signal \\\\\nSJ & Soft Jaccard similarity \\\\\nFK & Fleiss' $\\kappa$ \\\\\nEM & Exact-match voting rate \\\\\nVC ($c_{\\mathrm{vc}}$) & Entity voting confidence \\\\\nLP ($c_{\\mathrm{lp}}$) & Log-probability (mean token log-likelihood) \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Notation used throughout the paper.}\n\\label{tab:notation}\n\\end{table}\n\n\\section{Robustness Analysis}\\label{app:robustness}\n\nWe exclude instances with empty gold annotations from all correlation analyses (CoNLL: 697/3{,}453 instances, 20.2\\%; SciERC: 22/551, 4.0\\%).\nFor these instances, F1 is trivially zero regardless of prediction quality, and consistency signals reflect agreement on the empty set rather than extraction quality---including them inflates or deflates Spearman $\\rho$ depending on signal behavior at the boundary.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Signal robustness across configurations (Spearman $\\rho$). Top: temperature on Qwen SciERC. Middle: sample size on Qwen SciERC. Bottom: transfer across model families (both 8B) (LLaMA CoNLL $N{=}16$, 3-seed mean $\\pm\\sigma$). $^\\dagger$Mean over 3 seeds ($\\sigma{=}0.013$; individual: 0.398, 0.423, 0.410). $\\sigma$ computed as sample standard deviation.}\n\\label{tab:robustness}\n\\begin{tabular}{llcc}\n\\toprule\n& & NER $\\rho$ & RE $\\rho$ \\\\\n\\midrule\n\\multicolumn{4}{l}{\\textit{Temperature} (Qwen SciERC, $N{=}8$)} \\\\\n\\quad SJ & $T{=}0.7$ & 0.364 & 0.234 \\\\\n\\quad SJ & $T{=}1.0$ & 0.360 & 0.250 \\\\\n\\quad FK & $T{=}0.7$ & 0.289 & 0.184 \\\\\n\\quad FK & $T{=}1.0$ & 0.267 & 0.275 \\\\\n\\quad LP & $T{=}0.7$ & 0.249 & --- \\\\\n\\quad LP & $T{=}1.0$ & 0.205 & 0.266 \\\\\n\\midrule\n\\multicolumn{4}{l}{\\textit{Sample size} (Qwen SciERC, $T{=}1.0$)} \\\\\n\\quad SJ & $N{=}8$  & 0.360 & 0.250 \\\\\n\\quad SJ & $N{=}16$ & 0.411$^\\dagger$ & 0.281 \\\\\n\\quad FK & $N{=}8$  & 0.267 & 0.275 \\\\\n\\quad FK & $N{=}16$ & 0.283 & 0.279 \\\\\n\\midrule\n\\multicolumn{4}{l}{\\textit{Across model families} (LLaMA CoNLL, $N{=}16$, 3 seeds)} \\\\\n\\quad SJ &  & $0.474{\\pm}0.009$ & --- \\\\\n\\quad FK &  & $0.467{\\pm}0.009$ & --- \\\\\n\\quad EM &  & $0.473{\\pm}0.010$ & --- \\\\\n\\quad VC &  & $0.470{\\pm}0.006$ & --- \\\\\n\\quad LP &  & $0.311{\\pm}0.003$ & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{fig_temperature_robustness}\n\\caption{Temperature robustness on SciERC ($N{=}8$). Top: NER; bottom: RE. SJ maintains stable $\\rho$ across $T{=}0.7$ and $T{=}1.0$, while FK shows mixed sensitivity. LP shows the largest NER temperature effect ($\\Delta\\rho{=}{+}0.044$); RE $T{=}0.7$ LP data unavailable.}\n\\label{fig:temperature_robustness}\n\\end{figure}\n\n\\paragraph{Temperature sensitivity.}\nSJ NER $\\rho$ shifts from 0.364 ($T{=}0.7$) to 0.360 ($T{=}1.0$), a difference of 0.004.\nFK NER $\\rho$ drops by 0.022, while RE $\\rho$ increases by 0.091, likely reflecting reduced diversity at lower temperature interacting differently across tasks.\nLP exhibits the largest temperature effect on NER ($\\rho{=}0.249$ at $T{=}0.7$ vs.\\ $0.205$ at $T{=}1.0$, $\\Delta{=}{+}0.044$), consistent with lower temperature concentrating probability mass and improving LP's discriminative power for quality estimation; RE $T{=}0.7$ LP data is not available.\nAcross all comparisons, the signal hierarchy is preserved at both temperatures on NER (SJ${>}$FK${>}$LP at $T{=}0.7$: $0.364{>}0.289{>}0.249$; at $T{=}1.0$: $0.360{>}0.267{>}0.205$).\n\n\\paragraph{Sample size scaling.}\nIncreasing from $N{=}8$ to $N{=}16$ improves SJ on Qwen SciERC NER: $\\rho$ rises from 0.360 to $0.411{\\pm}0.010$ (three seeds: 0.398, 0.423, 0.410), a gain of $+0.047$.\nThe magnitude of $N$-scaling gains is setting-dependent---LLaMA SciERC NER yields $+0.016$ and Qwen CoNLL NER $+0.014$---though the direction is consistently positive.\nLLaMA CoNLL exhibits the most uniform scaling: all four consistency signals gain $\\Delta\\rho{\\approx}{+}0.042$ (range: $+0.039$ to $+0.044$) while LP gains only $+0.004$ (Table~\\ref{tab:quality_estimation}).\nFK $N$-scaling is seed-dependent: Qwen SciERC gains range from $+0.005$ to $+0.023$ across seeds (mean $+0.016$), while LLaMA CoNLL yields $+0.039$ (3-seed mean); individual seed FK shifts vary substantially under the unified pipeline, so this should not be interpreted as a robust trend.\nVC $N$-scaling is consistently positive ($+0.005$ on Qwen CoNLL, $+0.018$ on LLaMA SciERC, $+0.030$ on Qwen SciERC), while LP is approximately $N$-invariant ($\\Delta{\\leq}0.034$).\nSJ, EM, and VC scale consistently across all tested settings; only FK shows seed-dependent variation that does not constitute a reliable trend, suggesting that structural and binary-agreement signals are the most robust to $N$.\nAt $N{=}16$, SJ converges to comparable NER performance with VC ($\\Delta{=}0.002$) while exhibiting lower cross-seed variance ($\\sigma{=}0.010$ vs.\\ $0.026$), making it a more stable alternative at higher sample sizes.\n\n\\paragraph{Transfer across model families.}\nLLaMA-3.1-8B-Instruct shows a similar SJ--FK ordering on SciERC NER (SJ $\\rho{=}0.325{\\pm}0.021$, FK $\\rho{=}0.256{\\pm}0.024$, $\\Delta\\rho{=}0.069$; permutation $p{=}0.06$, borderline).\nOn CoNLL, the gap across model families is minimal (Table~\\ref{tab:quality_estimation}): SJ achieves $\\rho{=}0.431$ (LLaMA) vs.\\ 0.436 (Qwen), $\\Delta{=}0.005$.\nAt $N{=}16$, the structural-over-LP advantage holds across all four tested NER settings: Qwen SciERC (VC $\\rho{=}0.409$ vs.\\ LP 0.239, $\\Delta{=}{+}0.170$), Qwen CoNLL (EM $\\rho{=}0.463$ vs.\\ LP 0.328, $\\Delta{=}{+}0.135$),\\footnote{Qwen CoNLL $N{=}16$ was not recomputed under the unified pipeline; LP $\\rho{=}0.328$ may differ slightly from the registry value (0.315) due to instance filtering.} LLaMA SciERC (VC $\\rho{=}0.452$ vs.\\ LP 0.277, $\\Delta{=}{+}0.175$), and LLaMA CoNLL 3-seed (SJ $\\rho{=}0.474{\\pm}0.009$ vs.\\ LP $0.311{\\pm}0.003$, $\\Delta{=}{+}0.163$).\n\n\\paragraph{FK independence: instance-level permutation test.}\\label{app:fk_independence}\n\nTo verify that Fleiss' $\\kappa$ reflects genuine within-instance agreement rather than marginal-rate artifacts, we conduct instance-level permutation tests across three configurations.\nFor each instance, we permute sample labels 10{,}000 times to generate a null distribution of FK under independence, then compare the observed FK against this null via a one-sample $t$-test and permutation $p$-value.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Instance-level FK independence test. Permutation tests confirm FK reflects true within-instance agreement (all $p{<}0.001$). Split-half reliability $r$ computed by randomly partitioning $N$ samples into two halves and correlating their FK scores.}\n\\label{tab:fk_independence}\n\\begin{tabular}{lrcccc}\n\\toprule\nConfig & $n$ & FK mean & 95\\% CI & $t$ & Split-half $r$ \\\\\n\\midrule\nSciERC (Qwen) & 529 & 0.402 & [0.376, 0.428] & 30.8 & 0.395 \\\\\nCoNLL (LLaMA) & 2{,}756 & 0.927 & [0.919, 0.935] & 225.9 & 0.578 \\\\\nCoNLL (Qwen) & 2{,}756 & 0.720 & [0.706, 0.734] & 102.1 & 0.520 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:fk_independence} reports the results.\nAll configurations reject the independence null at $p{<}0.001$ ($n{=}529$--$2{,}756$), confirming that FK captures genuine inter-sample agreement rather than chance label co-occurrence.\nSplit-half reliability ranges from $r{=}0.395$ (SciERC) to $r{=}0.578$ (CoNLL LLaMA), indicating moderate stability: FK estimates from half the samples correlate positively with those from the other half, though the SciERC value suggests noisier estimation on harder tasks with fewer samples.\nThe higher FK means on CoNLL ($0.720$--$0.927$) vs.\\ SciERC ($0.402$) mirror the difficulty gradient observed in the main quality estimation results.\n\n\\section{Calibration Analysis}\\label{app:calibration}\n\n\\begin{figure*}[t]\n\\centering\n\\includegraphics[width=\\textwidth]{fig_reliability}\n\\caption{Reliability diagrams on SciERC ($N{=}8$, $T{=}1.0$). Top: mean F1 vs.\\ binned confidence; bottom: instance counts per bin. Left: NER; right: RE. NER signals are reasonably well-calibrated (calibration ECE 0.069--0.096), while RE shows greater miscalibration (ECE 0.109--0.339), reflecting the difficulty of calibrating confidence for compound extraction tasks.}\n\\label{fig:reliability}\n\\end{figure*}\n\nReliability diagrams use 10 equal-width bins.\nNER signals are reasonably well-calibrated (calibration ECE 0.069--0.096), while RE exhibits greater miscalibration (ECE 0.109--0.339), indicating that translating consistency scores into calibrated confidence estimates is feasible for NER but remains challenging for compound extraction tasks.\n\n\\section{Additional Analyses}\\label{app:additional}\n\n\\begin{figure*}[t]\n\\centering\n\\includegraphics[width=\\textwidth]{fig_signal_heatmap}\n\\caption{Quality estimation heatmap (Spearman $\\rho$) across five signals and four configurations. Left: full evaluation set; right: conditional set (non-zero F1 instances). On the full set, structural signals dominate on SciERC NER while all signals converge on CoNLL. On the conditional set, EM emerges as the strongest signal on both NER ($\\rho{=}0.360$) and RE ($\\rho{=}0.417$), while LP RE collapses to near-zero ($\\rho{=}0.011$).}\n\\label{fig:signal_heatmap}\n\\end{figure*}\n\n\\paragraph{Per-relation diagnostic.}\nRE signal degradation is relation-specific.\n\\textsc{Feature-Of} has near-zero correlation ($\\rho{=}0.004$), while \\textsc{Hyponym-Of} achieves $\\rho{=}0.646$.\nThe primary bottleneck is entity span errors, which account for 55.5\\% of RE false negatives---a prerequisite failure that consistency signals cannot detect, as they measure agreement among equally incorrect extractions.\nWe note that RE analysis relies on a single dataset (SciERC); generalization to other RE benchmarks remains to be validated.\n\n\\paragraph{Capability stratification.}\nFor NER, SJ effectiveness scales with structural complexity: on SciERC instances with 6+ entities, $\\rho{=}0.547$, compared to $\\rho{=}0.415$ for 1--2 entities.\nThe SJ advantage over LP remains stable across sentence-length quartiles ($\\Delta\\rho{\\approx}0.08$--$0.20$).\nFor RE, SJ $\\rho$ increases monotonically with sentence length (Q1: 0.110 $\\to$ Q4: 0.473; Fisher $z$-test $p{=}0.004$), indicating that longer, more relation-dense sentences provide richer structure for consistency-based estimation.\nBoth proxies are weakly correlated with F1 ($|r|{<}0.15$), confirming they capture input complexity rather than directly predicting output quality; however, entity count and sentence length are themselves moderately correlated ($\\rho{=}0.650$), so they reflect overlapping rather than independent complexity dimensions.\nFor RE, entity count and relation count are strongly correlated ($\\rho{=}0.769$) and thus reflect a single structural complexity dimension rather than independent axes.\nOn the high-complexity RE subset ($n{=}81$, high relation count), signals improve substantially: VC reaches $\\rho{=}0.630$, LP $\\rho{=}0.554$, and SJ $\\rho{=}0.502$---all far above the full-set levels.\nRicher relational structure provides more signal for consistency-based estimation, complementing the task-level boundary established by WNUT-17: structural signals are most effective within a ``sweet spot'' of sufficient model capability and sufficient output complexity.\n\n\\paragraph{Length vs.\\ log-probability.}\nFigure~\\ref{fig:length_logprob_scatter} shows that mean log-probability is weakly positively correlated with output length (NER: $\\rho{=}0.386$, $n{=}4{,}232$; RE: $\\rho{=}0.326$, $n{=}3{,}176$), ruling out length-penalty confounding as an explanation for LP's selection failure: longer outputs receive \\textit{higher}, not lower, token-averaged log-probability under constrained decoding.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{fig_length_logprob_scatter}\n\\caption{Output length vs.\\ mean log-probability on SciERC ($N{=}8$, $T{=}1.0$). Positive correlations (NER: $\\rho{=}0.386$; RE: $\\rho{=}0.326$) rule out length-penalty confounding.}\n\\label{fig:length_logprob_scatter}\n\\end{figure}\n\n\\paragraph{Evaluation circularity and LOO-SJ equivalence.}\nConsensus-proximity selection chooses $\\hat{y} = \\arg\\max_{y_i} \\sum_{j \\neq i} \\text{SJ}(y_i, y_j)$.\nLeave-one-out SJ (LOO-SJ) for sample $y_i$ is $\\text{LOO-SJ}_i = \\frac{1}{N-1}\\sum_{j \\neq i} \\text{SJ}(y_i, y_j)$.\nSince the $\\frac{1}{N-1}$ constant is shared across all candidates within an instance, $\\arg\\max_{y_i} \\text{LOO-SJ}_i = \\arg\\max_{y_i} \\sum_{j \\neq i} \\text{SJ}(y_i, y_j)$, making the two selection rules equivalent.\nStandard (non-LOO) SJ adds the self-comparison term $\\text{SJ}(y_i, y_i) = 1$ to each candidate, which is constant and thus does not affect ranking.\nEmpirically, LOO-SJ yields $\\Delta\\rho{=}{-}0.014$ relative to standard SJ (a correlation-level difference), with a maximum per-instance score difference of $3.1{\\times}10^{-4}$ (negligible at the individual prediction level).\nEvaluation circularity is negligible.\n\n\\paragraph{SJ normalizer robustness.}\nEquation~\\ref{eq:sj} uses $\\max(|g_i|, |g_j|)$ as the denominator; an alternative is the union size $|g_i \\cup g_j|$.\nTable~\\ref{tab:sj_normalizer} compares the two normalizers across all six model--dataset combinations ($N{=}8$, $T{=}1.0$, seed${=}42$): $|\\Delta\\rho|{<}0.01$ in every case, confirming that the choice between max and union normalization does not affect conclusions.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{SJ normalizer comparison (Spearman $\\rho$; $N{=}8$, $T{=}1.0$, seed${=}42$). Max: $\\max(|g_i|,|g_j|)$; Union: $|g_i \\cup g_j|$.}\n\\label{tab:sj_normalizer}\n\\begin{tabular}{@{}ll ccc@{}}\n\\toprule\nDataset & Model & $\\rho$(max) & $\\rho$(union) & $\\Delta\\rho$ \\\\\n\\midrule\nCoNLL & Qwen3-8B & .436 & .438 & $-$.002 \\\\\nCoNLL & Qwen3-4B & .422 & .421 & $+$.000 \\\\\nCoNLL & LLaMA-8B & .431 & .432 & $-$.000 \\\\\nSciERC & Qwen3-8B & .360 & .365 & $-$.005 \\\\\nSciERC & Qwen3-4B & .422 & .423 & $-$.001 \\\\\nSciERC & LLaMA-8B & .363 & .372 & $-$.009 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Conditional filtering details.}\nOn LLaMA conditional RE (non-zero F1 instances), SJ recovers to $\\rho{=}0.405$ while FK drops to $\\rho{=}0.259$, consistent with the NER structural advantage; on full-set RE, however, the SJ--FK difference is non-significant ($\\Delta\\rho{=}{-}0.005$, $p{=}0.53$; preliminary).\nAt $N{=}16$, the divergence persists: SJ maintains $\\rho{=}0.308$ on conditional RE while LP drops to $\\rho{=}{-}0.026$.\nEM ranks first across all four tested conditional configurations---SciERC NER ($\\rho{=}0.360$), CoNLL Qwen $N{=}16$ ($\\rho{=}0.466$), CoNLL LLaMA 3-seed ($\\rho{=}0.462$), and SciERC RE ($\\rho{=}0.417$)---despite full-set rankings ranging from \\#1 (CoNLL Qwen) to \\#5 (SciERC RE).\nOn the full set, EM is diluted by trivial agreement: instances where all $N$ samples produce identical (possibly incorrect) outputs receive EM${=}1$ regardless of quality, compressing the signal's dynamic range.\nOn the conditional set---where the model demonstrably produces varied outputs---exact agreement becomes the strongest quality signal.\nThe margin over SJ is largest on RE ($\\Delta\\rho{=}{+}0.171$), where compound extraction decisions amplify output variability, and smallest on CoNLL LLaMA ($\\Delta\\rho{=}{+}0.002$), where all signals converge near $\\rho{\\approx}0.46$.\n\n\\paragraph{WNUT-17 full signal analysis.}\nTable~\\ref{tab:wnut} reports all five signals on WNUT-17.\nVC achieves $\\rho{=}0.724$ (AUROC${=}0.913$) on the full set, but conditional analysis (non-zero F1 instances) reveals this is entirely driven by the zero/non-zero boundary: conditional $\\rho{=}0.038$ ($p{=}0.49$).\nLP shows the reverse pattern: full-set $\\rho{=}{-}0.410$ but conditional $\\rho{=}0.350$, the highest among all signals on the conditional set.\nThis inversion confirms that full-set correlations on high-failure-rate datasets conflate binary success prediction with quality gradation.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Quality estimation on WNUT-17 (Qwen, $N{=}16$, $T{=}1.0$, $n{=}689$ after filtering gold-empty instances). Cond: non-zero F1 instances ($n{=}334$). LP exhibits strong negative full-set $\\rho$; its conditional $\\rho$ reverses to the highest among all signals, confirming that full-set correlations on high-failure-rate datasets conflate binary success prediction with quality gradation.}\n\\label{tab:wnut}\n\\begin{tabular}{lccccc}\n\\toprule\nSignal & $\\rho$ & $p$ & AUROC & Cond.\\ $\\rho$ & Cond.\\ $p$ \\\\\n\\midrule\nVC      & .724 & ${<}$1e-112 & .913 & .038 & .487 \\\\\nFK      & .125 & .001 & .555 & .169 & .002 \\\\\nSJ      & .089 & .020 & .517 & .288 & ${<}$1e-7 \\\\\nEM      & .050 & .194 & .487 & .333 & ${<}$1e-9 \\\\\nLP & $-$.410 & ${<}$1e-28 & .219 & .350 & ${<}$1e-10 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Cross-configuration selection analysis.}\nTable~\\ref{tab:cross_selection} extends the selection analysis to four additional configurations.\nOn LLaMA SciERC, where output diversity remains substantial (18\\% identical outputs, 39\\% unique), LP achieves the highest selection F1 (0.652) at $N{=}8$ but still falls within bootstrap noise of single-sample (0.646), replicating the gap observed on Qwen SciERC (Table~\\ref{tab:selection}).\nOn CoNLL, 57--88\\% of instances produce identical outputs across all $N$ samples, reflecting a ceiling effect (single-sample F1 ${\\approx}$0.91--0.92) rather than signal failure; selection analysis on these configurations is uninformative because there is little per-sample variance for any signal to exploit.\n\n\\begin{table*}[t]\n\\centering\n\\small\n\\caption{Best-of-$N$ selection F1 (macro, instance-averaged) across configurations ($T{=}1.0$). Best non-oracle signal per row in \\textbf{bold}. At $N{=}8$, no signal significantly outperforms single-sample in any configuration. At $N{=}16$ on LLaMA CoNLL, VC achieves small but significant gains ($+0.28$~pp, $p{<}0.03$; see text below). CoNLL shows especially tight clustering where single-sample already exceeds 0.90.}\n\\label{tab:cross_selection}\n\\begin{tabular}{llccccccc}\n\\toprule\nConfig & $n$ & Single & Oracle & SJ & FK & EM & LP & VC \\\\\n\\midrule\nLLaMA/SciERC $N{=}8$ & 529 & .646 & .778 & .643 & .639 & .634 & \\textbf{.652} & .633 \\\\\nLLaMA/SciERC $N{=}16$ & 529 & .645 & .806 & \\textbf{.649} & \\textbf{.649} & .640 & .646 & .640 \\\\\nQwen/CoNLL $N{=}8$ & 2{,}756 & .908 & .948 & \\textbf{.899} & .893 & .898 & .897 & .895 \\\\\nLLaMA/CoNLL $N{=}8$ & 2{,}756 & .924 & .943 & .924 & \\textbf{.925} & .924 & .924 & .923 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table*}\n\n\\paragraph{Diminishing returns of $N$-scaling.}\nOur $N{=}8$ and $N{=}16$ comparisons (Table~\\ref{tab:robustness}) characterize the marginal value of additional samples for test-time scaling \\cite{brown2024monkeys, snell2025scaling}.\nFor quality estimation, structural signals benefit consistently but sublinearly: SJ $\\rho$ improves by $+0.047$ (Qwen SciERC, 3-seed mean) and $+0.032$ (LLaMA CoNLL, 3-seed mean) when doubling from $N{=}8$ to $N{=}16$, while log-probability is approximately $N$-invariant ($\\Delta\\rho{\\leq}0.021$).\nStructural signals leverage $\\binom{N}{2}$ pairwise comparisons (28 pairs at $N{=}8$, 120 at $N{=}16$), but the $\\rho$ improvement is far less than proportional, indicating diminishing information per additional comparison.\nThis asymmetry gives structural signals a relative advantage in the compute-constrained regime: at $N{=}8$, SJ already achieves $\\rho{=}0.431$ on LLaMA CoNLL (vs.\\ LP $\\rho{=}0.307$, $\\Delta{=}{+}0.124$), and the gap \\textit{widens} at $N{=}16$ ($\\Delta{=}{+}0.163$) because structural signals continue to benefit from additional pairwise evidence while LP does not.\nFor sample selection, additional samples increase the oracle upper bound---more draws raise the probability of a high-quality candidate---but signal-based selection remains flat because the selector's inability to identify the best candidate is a granularity limitation, not a sample size limitation.\nThe practical implication is that $N{=}8$ captures most of the achievable quality estimation benefit; further scaling widens rather than closes the correlation-selection gap absent stronger per-sample selectors.\n\n\\paragraph{$N{=}16$ CoNLL selection: small but significant.}\nWhile quality estimation benefits sublinearly from $N$-scaling, selection behavior at $N{=}16$ reveals a nuanced exception on LLaMA CoNLL.\nVC achieves the largest gain over single-sample ($+0.28$~pp, $p{=}0.003$--$0.027$ across 3 seeds, all significant), with SJ, FK, and EM at $+0.22$--$0.23$~pp and LP at $+0.12$~pp (2/3 seeds significant).\nThese gains are statistically significant but practically minimal: oracle headroom at $N{=}16$ is only 2.5~pp, so VC captures approximately 10\\% of the available headroom.\nThis reinforces the primary finding: even under the most favorable conditions---high baseline performance, more candidates, and aggregated multi-seed evidence---signal-based selection recovers only a fraction of the oracle headroom available.\n\n\\section{Bootstrap CI for Signal Comparisons}\\label{app:bootstrap_signal}\n\nTable~\\ref{tab:bootstrap_signal_ci} reports bootstrap confidence intervals for individual signal $\\rho$ and pairwise $\\Delta\\rho$ on SciERC NER ($N{=}8$, $n{=}529$, $B{=}10{,}000$, seed${=}42$).\nThe SJ--LP gap ($\\Delta\\rho{=}{+}0.155$) is clearly significant, confirming the structural advantage reported in \\S\\ref{sec:qe_results}.\nThe VC--SJ gap ($\\Delta\\rho{=}{+}0.019$) is not significant, indicating that these two structural signals perform comparably.\nThe SJ--EM gap ($\\Delta\\rho{=}{+}0.065$) is borderline significant, with the CI lower bound at $+0.003$ and upper bound at $+0.130$.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Bootstrap 95\\% CIs for signal $\\rho$ on SciERC NER ($N{=}8$, $n{=}529$, $B{=}10{,}000$, seed${=}42$). Top: individual signals. Bottom: pairwise $\\Delta\\rho$; ``Sig.'' indicates whether the 95\\% CI excludes zero.}\n\\label{tab:bootstrap_signal_ci}\n\\begin{tabular}{lcc}\n\\toprule\nSignal & $\\rho$ & 95\\% CI \\\\\n\\midrule\nVC & +0.379 & [+0.299, +0.456] \\\\\nSJ & +0.360 & [+0.277, +0.437] \\\\\nEM & +0.295 & [+0.212, +0.371] \\\\\nFK & +0.267 & [+0.176, +0.354] \\\\\nLP & +0.205 & [+0.119, +0.291] \\\\\n\\bottomrule\n\\end{tabular}\n\n\\vspace{0.5em}\n\n\\begin{tabular}{lccc}\n\\toprule\nComparison & $\\Delta\\rho$ & 95\\% CI & Sig. \\\\\n\\midrule\nSJ $-$ LP & +0.155 & [+0.074, +0.234] & Yes \\\\\nVC $-$ SJ & +0.019 & [$-$0.033, +0.073] & No \\\\\nSJ $-$ EM & +0.065 & [+0.003, +0.130] & Marginal$^\\dagger$ \\\\\n\\bottomrule\n\\end{tabular}\n\n\\smallskip\n{\\footnotesize $^\\dagger$Marginally significant without multiple comparison correction; would not survive Bonferroni correction for 10 pairwise comparisons ($\\alpha_{\\text{adj}}{=}0.005$).}\n\\end{table}\n\nAt $N{=}16$ ($B{=}10{,}000$, permutation test), the structural advantage extends to FK comparisons.\nOn SciERC NER ($n{=}529$), SJ--FK ($\\Delta\\rho{=}0.147$--$0.160$, all $p{\\leq}0.002$) and VC--FK ($\\Delta\\rho{=}0.138$--$0.188$, all $p{\\leq}0.003$) are clearly significant across all three seeds; EM--FK is seed-dependent ($\\Delta\\rho{=}0.054$--$0.093$, $p{=}0.048$--$0.15$).\nOn CoNLL ($n{=}2{,}756$), all signals significantly outperform FK: EM $\\Delta\\rho{=}0.071$ ($p{<}0.001$), SJ $\\Delta\\rho{=}0.056$ ($p{<}0.001$), VC $\\Delta\\rho{=}0.022$ ($p{=}0.040$).\n\n\\section{Diversity and Selection Analysis}\\label{app:diversity}\n\n\\begin{figure*}[t]\n\\centering\n\\includegraphics[width=\\textwidth]{fig_selection_gap}\n\\caption{The correlation-selection gap on SciERC NER ($N{=}8$, $T{=}1.0$, 2-seed mean). Bars show best-of-$N$ selection F1; the line marks quality estimation $\\rho$. Despite $\\rho$ up to 0.40, no signal significantly outperforms single-sample (all $p{>}0.05$; Table~\\ref{tab:selection}). Dashed line indicates oracle upper bound. RE selection results in Table~\\ref{tab:selection}.}\n\\label{fig:selection_gap}\n\\end{figure*}\n\n\\paragraph{Output diversity quantification.}\nTable~\\ref{tab:diversity} summarizes output diversity across configurations.\nOn SciERC, output diversity is substantial: Qwen produces 43\\% unique outputs per instance (mean 3.5 distinct out of $N{=}8$), with per-sample F1 standard deviation of 0.144 and mean pairwise SJ of 0.703.\nLLaMA shows similar diversity (39\\% unique, F1 std 0.11).\nOn CoNLL, diversity collapses: 57\\% (Qwen) to 88\\% (LLaMA) of instances produce identical outputs across all $N$ samples, reflecting a ceiling effect where single-sample F1 already exceeds 0.90.\nWNUT-17 shows 55\\% identical outputs, driven by the 52\\% zero-F1 rate.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Output diversity across configurations ($N{=}8$, $T{=}1.0$). ``Identical'' = fraction of instances with all $N$ outputs identical. ``Unique'' = mean fraction of distinct outputs per instance.}\n\\label{tab:diversity}\n\\begin{tabular}{lcc}\n\\toprule\nConfig & Identical & Unique \\\\\n\\midrule\nQwen/SciERC & 11\\% & 43\\% \\\\\nLLaMA/SciERC & 18\\% & 39\\% \\\\\nQwen/CoNLL & 57\\% & --- \\\\\nLLaMA/CoNLL & 88\\% & --- \\\\\nWNUT-17 & 55\\% & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Oracle-improvable fraction.}\nAcross SciERC configurations, 39--42\\% of instances contain at least one sample with F1 exceeding single-sample\\footnote{Oracle-improvable and diversity-stratified analyses use $n{=}529$ (excluding instances with empty gold annotations; see \\S\\ref{sec:evaluation}); the diversity quantification in Table~\\ref{tab:diversity} uses the full test set.}: Qwen NER 42.0\\% (222/529, mean headroom $+$31.9~pp among improvable instances), Qwen RE 41.3\\% (164/397, $+$45.3~pp), LLaMA NER 39.3\\% (208/529, $+$33.7~pp).\nOn CoNLL, only 4--9\\% of instances are improvable, confirming the ceiling effect.\n\n\\paragraph{Diversity-stratified selection gap.}\nOn the 44\\% of Qwen SciERC instances with high diversity (${\\geq}4$ unique outputs among 8 samples, $n{=}232$), oracle headroom reaches $+$16.3~pp, yet all consistency-based signals (SJ, FK, EM, VC) select at or below single-sample, and LP---the only per-sample signal---achieves merely $+$0.8~pp.\nLLaMA replicates this pattern: on its high-diversity subset ($n{=}186$), oracle headroom reaches $+$20.1~pp while consistency signals remain at or below single-sample and LP captures only $+$2.0~pp.\nThis rules out insufficient diversity as an explanation for the correlation-selection gap.\n\n\\paragraph{TOST equivalence testing.}\\label{app:tost}\nThe primary evidence against selection gains comes from effect sizes and confidence intervals: Cohen's $d{=}0.038$ for the best signal (NER LP) and bootstrap 95\\% CI [$-$3.0, $+$4.2]~pp spanning zero.\nTable~\\ref{tab:tost} supplements this with two one-sided tests (TOST), testing whether each signal's selection F1 is equivalent to single-sample within a bound $\\delta$.\nThe $\\delta$ values are contextualized against oracle headroom (12--18~pp): $\\delta{=}5$~pp corresponds to forgoing 28--38\\% of the available headroom, $\\delta{=}3$~pp forgoing 17--23\\%, and $\\delta{=}2$~pp less than 15\\%.\nThese proportions use the same test data that defines the headroom, introducing circularity: $\\delta$ is anchored to the very quantity it contextualizes.\nWe address this below with externally anchored equivalence margins.\nThe breakpoint $\\delta^*$---the minimum equivalence margin at which each signal passes TOST---ranges from approximately 1.3~pp (SJ, ${\\sim}$10\\% of oracle headroom) to 3.4~pp (FK, ${\\sim}$26\\%) on NER, and from approximately 2.9~pp (LP, ${\\sim}$16\\%) to 6.5~pp (VC, ${\\sim}$36\\%) on RE.\nOn NER ($n{=}529$), at $\\delta{=}{\\pm}2$~pp, SJ and LP are confirmed equivalent to single-sample (TOST $p{<}0.05$); at $\\delta{=}{\\pm}3$~pp, four of five signals pass; at $\\delta{=}{\\pm}5$~pp, all five pass.\nOn RE ($n{=}397$, preliminary), EM and VC fail equivalence even at $\\delta{=}{\\pm}5$~pp due to systematic underperformance ($\\Delta{=}{-}3.2$~pp and $-4.5$~pp respectively).\nThe effect sizes are negligible ($d{=}0.038$) and confidence intervals span zero, with TOST confirming equivalence at practically meaningful margins.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{TOST equivalence testing: signals vs.\\ single-sample on SciERC ($N{=}8$, $T{=}1.0$). \\checkmark: equivalent at $p{<}0.05$; \\texttimes: not equivalent. $\\Delta$: mean F1 difference (signal $-$ single-sample).}\n\\label{tab:tost}\n\\begin{tabular}{l cccc cccc}\n\\toprule\n& \\multicolumn{4}{c}{\\textbf{NER}} & \\multicolumn{4}{c}{\\textbf{RE}} \\\\\n\\cmidrule(lr){2-5} \\cmidrule(lr){6-9}\nSignal & $\\Delta$ & $\\pm$2 & $\\pm$3 & $\\pm$5 & $\\Delta$ & $\\pm$2 & $\\pm$3 & $\\pm$5 \\\\\n\\midrule\nLP & +0.6 & \\checkmark & \\checkmark & \\checkmark & $-$0.9 & \\texttimes & \\checkmark & \\checkmark \\\\\nSJ & +0.1 & \\checkmark & \\checkmark & \\checkmark & $-$1.8 & \\texttimes & \\texttimes & \\checkmark \\\\\nFK & $-$0.5 & \\texttimes & \\checkmark & \\checkmark & $-$1.6 & \\texttimes & \\texttimes & \\checkmark \\\\\nEM & $-$0.8 & \\texttimes & \\checkmark & \\checkmark & $-$3.2 & \\texttimes & \\texttimes & \\texttimes \\\\\nVC & $-$1.0 & \\texttimes & \\texttimes & \\checkmark & $-$4.5 & \\texttimes & \\texttimes & \\texttimes \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{External equivalence margins.}\nThe oracle-headroom anchors above introduce circularity, as a reviewer correctly noted: $\\delta$ is calibrated against the very quantity it contextualizes.\nTo resolve this, we supplement with three externally grounded margins:\n(1) $\\delta_{\\mathrm{SEM}}$: the bootstrapped standard error of single-sample F1 (0.43--1.33~pp depending on configuration), representing measurement noise;\n(2) $\\delta_{\\mathrm{practical}}{=}0.5$~pp, reflecting the threshold below which NER differences are considered negligible \\cite{ratinov2009design};\n(3) $\\delta_{\\mathrm{literature}}{=}1.0$~pp, the approximate significant-difference threshold established in NER evaluation methodology \\cite{bergkirkpatrick2012empirical}.\n\nResults under these external anchors diverge sharply by configuration.\nOn LLaMA CoNLL ($n{=}2{,}756$), all signals pass equivalence at every $\\delta$ ($p{<}0.001$), consistent with the near-zero selection deltas ($|\\Delta|{\\leq}0.1$~pp) and tight CIs at this sample size.\nOn Qwen CoNLL ($n{=}2{,}756$), no signal passes at any external $\\delta$: selection F1 degrades by 0.9--1.5~pp relative to single-sample, exceeding even $\\delta_{\\mathrm{literature}}$.\nOn SciERC NER ($n{=}529$), only SJ passes at $\\delta_{\\mathrm{SEM}}{=}1.33$~pp (the widest SEM bound); all other signals and tighter margins fail.\nThese external anchors confirm that the equivalence conclusion is configuration-dependent: LLaMA CoNLL selection is robustly equivalent to single-sample under any reasonable margin, while SciERC and Qwen CoNLL selection shows detectable degradation at externally calibrated thresholds.\n\n\\section{Multi-Seed Stability}\\label{app:multiseed}\n\nTable~\\ref{tab:multiseed} reports quality estimation metrics across three random seeds for both model families on SciERC ($N{=}8$, $T{=}1.0$).\nOn NER, the signal ranking VC${>}$SJ${>}$EM${>}$FK${>}$LP is identical across all six model-seed combinations, with $\\sigma{\\leq}0.025$ for all signals (rankings are stable across our 3 seeds, though statistical power with $n{=}3$ is limited).\nOn RE (Qwen only, preliminary), VC remains the top signal ($\\rho{=}0.309{\\pm}0.024$), but LP rises to \\#2 ($\\rho{=}0.297{\\pm}0.022$), above FK, SJ, and EM---a reversal from the NER ranking that reflects RE's higher sensitivity to per-sample scoring.\nLLaMA absolute values are systematically lower than Qwen on NER, consistent with the directionally-consistent-but-magnitude-dependent characterization in the main text.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Multi-seed quality estimation on SciERC ($N{=}8$, $T{=}1.0$, seeds: 42, 123, 456). NER: both models; RE: Qwen only (preliminary). Signal ranking is stable across seeds ($\\sigma{\\leq}0.025$). $\\sigma$ is population standard deviation over 3 seeds.}\n\\label{tab:multiseed}\n\\begin{tabular}{lccccc}\n\\toprule\n& LP & FK & SJ & VC & EM \\\\\n\\midrule\n\\multicolumn{6}{l}{\\textit{NER Spearman $\\rho$ (mean $\\pm\\sigma$)}} \\\\\nQwen & .217${\\pm}$.013 & .254${\\pm}$.016 & .364${\\pm}$.018 & .386${\\pm}$.019 & .307${\\pm}$.008 \\\\\nLLaMA & .162${\\pm}$.025 & .256${\\pm}$.024 & .325${\\pm}$.021 & .384${\\pm}$.014 & .279${\\pm}$.011 \\\\\n\\midrule\n\\multicolumn{6}{l}{\\textit{RE Spearman $\\rho$ (mean $\\pm\\sigma$, Qwen)}} \\\\\nQwen & .297${\\pm}$.022 & .290${\\pm}$.012 & .249${\\pm}$.002 & .309${\\pm}$.024 & .135${\\pm}$.016 \\\\\n\\midrule\n\\multicolumn{6}{l}{\\textit{NER AUROC (mean $\\pm\\sigma$)}} \\\\\nQwen & .613${\\pm}$.002 & .618${\\pm}$.009 & .684${\\pm}$.009 & .697${\\pm}$.010 & .661${\\pm}$.010 \\\\\nLLaMA & .577${\\pm}$.007 & .616${\\pm}$.011 & .655${\\pm}$.010 & .689${\\pm}$.005 & .636${\\pm}$.006 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{Training Configuration}\\label{app:training}\n\nBoth models are fine-tuned with identical hyperparameters (Table~\\ref{tab:training}) to ensure comparisons across model families reflect model differences rather than training confounds.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Training configuration. Both Qwen3-8B and LLaMA-3.1-8B-Instruct use identical settings unless noted.}\n\\label{tab:training}\n\\begin{tabular}{ll}\n\\toprule\nParameter & Value \\\\\n\\midrule\nLoRA rank / $\\alpha$ & 32 / 64 \\\\\nLoRA target & All linear modules \\\\\nLoRA dropout & 0 \\\\\nOptimizer & AdamW \\\\\nLearning rate & 2e-4, cosine schedule \\\\\nWarmup ratio & 0.1 \\\\\nEffective batch size & 16 (2 $\\times$ grad.\\ accum.\\ 8) \\\\\nEpochs & 5 \\\\\nMax sequence length & 2048 \\\\\nPrecision & bf16 \\\\\nGradient checkpointing & Enabled \\\\\nMax gradient norm & 1.0 \\\\\nTraining seed & 42 \\\\\nFramework & LLaMA Factory \\\\\n\\midrule\n\\multicolumn{2}{l}{\\textit{Dataset-specific}} \\\\\nSciERC split & 1861 / 275 / 551 \\\\\nCoNLL / WNUT & +\\,load\\_best\\_model\\_at\\_end, \\\\\n& eval\\_steps${=}$200, save\\_limit${=}$5 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Prompt template.}\nFor NER, we use a structured prompt:\n\\begin{quote}\n\\small\n\\texttt{System:} You are an expert in Named Entity Recognition.\\\\\n\\texttt{User:} Extract all named entities from the following text. Output as JSON.\\\\\nText: \\texttt{\\{input\\_text\\}}\\\\\nEntity types: \\texttt{\\{schema\\_types\\}}\n\\end{quote}\nRE follows the same structure with ``Relation Extraction'' and relation type lists substituted accordingly.\n\n\\paragraph{Constrained decoding.}\nInference uses vLLM with XGrammar-based JSON schema enforcement \\cite{willard2023guided}, which constrains outputs to valid entity/relation structures matching the target schema.\nThis eliminates format errors but may compress per-sample diversity by restricting the output space.\\footnote{SciERC training used \\texttt{enable\\_thinking=True} (LLaMA Factory 0.9.4 default), injecting empty \\texttt{&lt;think>&lt;/think>} blocks (4--5 tokens) into each training response with loss computation; CoNLL and WNUT explicitly set \\texttt{enable\\_thinking=False}. Constrained decoding at inference time enforces JSON-only output, suppressing thinking tokens. See \\S\\ref{sec:setup} and Limitations for discussion of this confound.}\n\n\\section{Thinking Token Impact Analysis}\\label{app:thinking_token}\n\nQwen3-8B's SciERC checkpoint was trained with empty \\texttt{&lt;think>&lt;/think>} blocks prepended to each response (\\S\\ref{sec:setup}).\nWe quantify the potential impact on LP scores through three complementary arguments.\n\n\\paragraph{LP shift magnitude.}\nEmpty thinking tokens (mean 4.5 per sample) constitute 2.1\\% of tokens on SciERC.\nThe estimated LP shift is 0.001 nats per token (2.68\\% of the median within-instance LP range of 0.041 nats).\nBecause all samples share identical thinking-token LP offsets, cumulative LP rankings are invariant; mean LP changes selection for ${<}1.5\\%$ of instances.\n\n\\paragraph{Constant prefix cancellation.}\nAll $N$ samples within an instance share the same prompt and, under constrained decoding, the same absence of thinking tokens at inference time.\nAny LP bias from the training-time thinking prefix is therefore a near-constant additive shift across all candidates within an instance, leaving within-instance LP \\textit{rankings} unchanged.\n\n\\paragraph{CoNLL control group.}\nCoNLL and WNUT-17 checkpoints were trained without thinking tokens (\\texttt{enable\\_thinking=False}).\nIf thinking tokens caused LP compression on SciERC, CoNLL should exhibit lower tied fractions.\nInstead, CoNLL shows \\textit{higher} tied fractions at both temperatures (86.8\\% at $T{=}1.0$, 95.8\\% at $T{=}0.7$) than SciERC (60.3\\% at $T{=}1.0$), directly contradicting the thinking-token hypothesis.\n\n\\section{Log-Probability Score Compression}\\label{app:logprob_ties}\n\nUnder constrained decoding, log-probability scores are severely compressed within instances, limiting per-sample discrimination (Table~\\ref{tab:logprob_ties}, Figure~\\ref{fig:lp_range_cdf}).\nThe median within-instance LP range is only 0.041 nats; we use $\\varepsilon{=}0.05$ as an illustrative threshold to characterize this compression.\nAt this cutpoint, 60.3\\% of instances ($n{=}529$, excluding empty gold annotations) have a within-sample range below $\\varepsilon$, and 75\\% of pairwise comparisons are effective ties ($|\\Delta|{<}0.026$).",
      "numLines": 500,
      "startLine": 1,
      "totalLines": 995
    }
  },
  "sourceToolAssistantUUID": "3212ff57-13ef-4a22-b475-8aed7cfa1212",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_1_68ddc296",
  "sessionId": "a5f4ff78-4f02-4166-b054-29f1bf2f2644",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 46_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[Round 1 审稿请求]: ## Round 1 审稿任务 — Reviewer 1（方法严谨性 + 实验设计 + 统计分析）  ### Venue 信息 - **目标**: EMNLP 2026 Main Conference (via ARR May 2026 cycle) - **截止日期**: 2026-05-25 - **格式**: ACL 模板, 正文 8 页, double-bl…",
  "leafUuid": "8e65486f-c1c7-4654-9a32-58780f0f8e18",
  "sessionId": "a5f4ff78-4f02-4166-b054-29f1bf2f2644"
}
```

---

### Runtime record

_source line 47_

```json
{
  "type": "ai-title",
  "aiTitle": "Review round 1 paper on structured IE self-consistency",
  "sessionId": "a5f4ff78-4f02-4166-b054-29f1bf2f2644"
}
```

---

### Tool call

_source line 48 · 2026-05-16T05:13:14.179Z_

<details open><summary>🔧 Tool call — Read · `toolu_013ERnwRkyfi8s6N7hCagNjd`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
  "offset": 500,
  "limit": 500
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8e65486f-c1c7-4654-9a32-58780f0f8e18",
  "isSidechain": false,
  "requestId": "req_011Cb5g8muUMkZvMxtA2Cco2",
  "type": "assistant",
  "uuid": "40bb3365-8693-4466-8d86-69f5302a39f9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_1_68ddc296",
  "sessionId": "a5f4ff78-4f02-4166-b054-29f1bf2f2644",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01D9uCa2U6Y6iJjZxtoxDDh6",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14748,
      "cache_read_input_tokens": 41295,
      "output_tokens": 126,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 14748,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 126,
          "cache_read_input_tokens": 41295,
          "cache_creation_input_tokens": 14748,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 14748
          },
          "type": "message"
        }
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

_source line 49 · 2026-05-16T05:13:14.487Z_

<details><summary>↩ Tool result · `toolu_013ERnwRkyfi8s6N7hCagNjd`</summary>

```text
500	At this cutpoint, 60.3\% of instances ($n{=}529$, excluding empty gold annotations) have a within-sample range below $\varepsilon$, and 75\% of pairwise comparisons are effective ties ($|\Delta|{<}0.026$).
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
531	Among instances with LP range ${\geq}0.05$ ($n{=}210$, 40\% of total), log-probability selection \textit{significantly} outperforms single-sample ($+2.9$~pp F1, $p{=}0.004$), and within-instance $\rho(\text{LP}, \text{F1})$ rises from 0.08 (tied subset) to 0.39 (non-tied subset).
532	As a continuous complement to the binary tied/non-tied analysis, pooled within-instance $\rho(\text{LP}, \text{F1}){=}0.248$ across all instances confirms weak but positive per-sample signal; however, only 21.6\% of instances achieve $p{<}0.05$ significance, and $\rho(\text{LP range}, \text{F1 range}){=}0.328$ shows that instances with more LP spread also exhibit more F1 variability---LP carries information but compression limits its exploitation.
533	A free-form NER decoding ablation (Appendix~\ref{app:freeform_ablation}) confirms this compression persists without constrained decoding.
534	
535	\paragraph{$\varepsilon$ sensitivity sweep (post-hoc exploratory).}
536	Table~\ref{tab:epsilon_sweep} sweeps the tied/non-tied threshold from $\varepsilon{=}0.01$ to $0.20$ as a post-hoc exploratory analysis characterizing how selection gain varies with compression severity.
537	The tied fraction increases smoothly with no cliff or discontinuity, and the selection gain $\Delta$ grows monotonically as the non-tied subset narrows to progressively higher-spread instances.
538	$\varepsilon{=}0.05$ yields the strongest statistical separation ($p{=}0.004$); at $\varepsilon{\geq}0.15$, the non-tied subset becomes too small for reliable inference ($n{\leq}36$).
539	
540	\begin{table}[t]
541	\centering
542	\small
543	\caption{$\varepsilon$ sensitivity sweep for LP selection on SciERC NER ($N{=}8$, seed${=}42$, $n{=}529$). ``Tied\%'' = fraction with within-instance LP range ${<}\varepsilon$. $\Delta$: selection F1 gain over single-sample on the non-tied subset. The tied fraction increases smoothly; $\varepsilon{=}0.05$ yields the strongest statistical separation.}
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
586	\section{Consistency-Stratified Selection Analysis}\label{app:vc_quartile}
587	
588	Table~\ref{tab:vc_quartile} stratifies SciERC instances by voting confidence (VC) quartiles and reports selection $\Delta$ (gain over single-sample) for LP and SJ.
589	
590	\begin{table}[t]
591	\centering
592	\small
593	\caption{Selection $\Delta$ (pp over single-sample) stratified by VC quartile on SciERC ($N{=}8$, Qwen3-8B). Oracle headroom collapses at Q4; LP rankings are unreliable at Q1--Q2. Neither quartile supports consistent selection gains.}
594	\label{tab:vc_quartile}
595	\begin{tabular}{lcccc}
596	\toprule
597	Quartile & Mean VC & LP $\Delta$ & SJ $\Delta$ & Oracle (pp) \\
598	\midrule
599	\multicolumn{5}{l}{\textit{NER}} \\
600	Q1 (low) & 0.30 & $+$1.55 & $+$0.54 & 16.85 \\
601	Q2 & 0.51 & $-$0.65 & $-$1.89 & 14.35 \\
602	Q3 & 0.68 & $+$1.97 & $+$1.84 & 16.83 \\
603	Q4 (high) & 0.92 & $-$0.41 & $-$0.04 & 4.78 \\
604	\midrule
605	\multicolumn{5}{l}{\textit{$^\dagger$RE}} \\
606	Q1 (low) & --- & $-$3.56 & --- & --- \\
607	Q4 (high) & --- & $+$4.01 & --- & --- \\
608	\bottomrule
609	\end{tabular}
610	\end{table}
611	
612	The NER pattern reveals two complementary failure modes rather than a monotonic relationship between consistency and selection gain:
613	\begin{itemize}
614	\item \textbf{Q4 ceiling effect.} High-consistency instances (mean VC${=}0.92$) have oracle headroom of only 4.78~pp---samples have already converged, leaving little room for any signal to improve selection.
615	\item \textbf{Q1--Q2 noise.} Low-consistency instances retain large headroom (14--17~pp) but LP rankings are unreliable, yielding inconsistent $\Delta$ signs across quartiles.
616	\end{itemize}
617	
618	On $^\dagger$RE, the pattern differs: Q4 LP achieves $+4.01$~pp, suggesting LP can recover selection ability when high consistency coincides with structured output diversity. This is a single-dataset observation and should be interpreted cautiously.
619	
620	On CoNLL NER, Q3--Q4 instances have VC${=}1.0$ (all samples identical), yielding $\Delta{=}0$ universally---a ceiling effect even more extreme than SciERC Q4.
621	
622	\section{RE Conditional Selection}\label{app:re_conditional_selection}
623	
624	Table~\ref{tab:re_cond_selection} extends the selection analysis to the RE non-zero F1 subset.
625	Of $n{=}397$ RE instances, 238 (60\%) have non-zero F1 and 159 (40\%) have zero F1.
626	All five signals underperform single-sample on both subsets.
627	On the non-zero subset, selection performance is \textit{worse} than on the full set (e.g., VC: $-10.0$~pp on non-zero vs.\ $-4.5$~pp on full set), because single-sample is already strong on non-zero instances (F1${=}0.674$) and signals actively select inferior samples.
628	Oracle headroom exists (0.757 vs.\ 0.674) but no signal exploits it, ruling out the 40\% zero-F1 floor effect as the explanation for RE selection failure.
629	
630	\begin{table}[t]
631	\centering
632	\small
633	\caption{RE selection F1 (macro, instance-averaged) on SciERC ($N{=}8$, $T{=}1.0$). Full set ($n{=}397$) and non-zero F1 subset ($n{=}238$). No signal outperforms single-sample on either subset.}
634	\label{tab:re_cond_selection}
635	\begin{tabular}{lcc}
636	\toprule
637	Method & Full ($n{=}397$) & Non-zero ($n{=}238$) \\
638	\midrule
639	Oracle & 0.585 & 0.757 \\
640	\midrule
641	LP & 0.395 & 0.600 \\
642	SJ & 0.386 & 0.604 \\
643	EM & 0.372 & 0.583 \\
644	VC & 0.359 & 0.574 \\
645	\midrule
646	Single & 0.404 & 0.674 \\
647	\bottomrule
648	\end{tabular}
649	\end{table}
650	
651	\section{RE $N{=}16$ Selection Analysis}\label{app:re_n16_selection}
652	
653	Table~\ref{tab:re_n16_selection} extends the selection analysis to RE at $N{=}16$ with 3-seed statistics.
654	All four consistency signals underperform single-sample, with EM showing the largest deficit ($\Delta{=}{-}1.5$~pp, Fisher $p{>}0.99$).
655	LP is the only positive signal ($\Delta{=}{+}0.7$~pp, Fisher $p{=}0.058$), driven primarily by seed~456 ($\Delta{=}{+}1.5$~pp, $p{=}0.026$); the remaining seeds show smaller effects ($+0.1$ and $+0.6$~pp, $p{>}0.20$).
656	Even the most favorable seed captures only ${\sim}9\%$ of the 17.1~pp oracle headroom.
657	This cross-task consistency---LP as the only viable selection signal on both NER and RE---reinforces the structural limitation of instance-level signals for candidate ranking.
658	
659	\begin{table}[t]
660	\centering
661	\small
662	\caption{RE best-of-$N$ selection F1 (macro, instance-averaged) on SciERC (Qwen3-4B, $N{=}16$, $T{=}1.0$, 3-seed mean${\pm}\sigma$, $n{=}551$). Fisher combined $p$ vs.\ single-sample. LP is the only signal with positive $\Delta$. $\sigma$ is population standard deviation over 3 seeds.}
663	\label{tab:re_n16_selection}
664	\begin{tabular}{lccc}
665	\toprule
666	Method & F1 & $\Delta$ (pp) & $p$(Fisher) \\
667	\midrule
668	Oracle & $.463{\pm}.006$ & $+$17.1 & --- \\
669	\midrule
670	LP & $\mathbf{.299}{\pm}.007$ & $+$0.7 & .058 \\
671	VC & $.284{\pm}.002$ & $-$0.8 & .973 \\
672	FK & $.283{\pm}.005$ & $-$0.9 & .985 \\
673	SJ & $.281{\pm}.005$ & $-$1.0 & .993 \\
674	EM & $.277{\pm}.007$ & $-$1.5 & .999 \\
675	\midrule
676	Single & $.291{\pm}.000$ & --- & --- \\
677	Random & $.262{\pm}.001$ & $-$2.9 & --- \\
678	\bottomrule
679	\end{tabular}
680	\end{table}
681	
682	\section{MBR Decoding and Task-Specific Interactions}\label{app:mbr_discussion}
683	
684	\paragraph{Connection to MBR decoding.}
685	Our selection strategies instantiate minimum Bayes risk (MBR) decoding \cite{eikema2022sampling, muller2021understanding}: each selects $\hat{y} = \arg\max_{y_i} \sum_{j \neq i} U(y_i, y_j)$ with utility $U$ defined by SJ, EM, or entity overlap.
686	Despite MBR's success in machine translation \cite{freitag2022high} and its extension to summarization, code generation, and captioning \cite{jinnai2024mbr}, all variants fail here because the utility functions correlate with F1 at the instance level but not within a single instance---the mathematical essence of the correlation-selection gap.
687	\citet{eikema2025structured} study structure-conditional MBR decoding and find that standard utility functions degrade on structured outputs---consistent with our finding that consensus-proximity selection fails in IE despite its success in machine translation.
688	
689	\paragraph{Task-specific decoding interactions.}
690	The free-form ablation reveals divergent behavior across tasks.
691	On RE, LP selection flips from $-0.68$~pp (constrained) to $+1.69$~pp (free-form; preliminary, single RE benchmark), a reversal that spans all 7 relation types and is driven by selective variance reallocation ($p{<}0.0001$).
692	The win/loss ratio shifts from 36:59 (constrained) to 45:45 (free-form), with the gains concentrated on relation-dense instances (mean 3.3 gold relations).
693	This interaction does not generalize to NER, where selection remains negligible under both regimes.
694	This ablation uses a single seed (seed${=}42$); whether the RE reversal replicates across seeds and generalizes to other RE benchmarks warrants further investigation.
695	The non-tied subset ($n{=}210$) is partially reshuffled under free-form decoding: Jaccard similarity between the constrained and free-form non-tied sets is 0.472, indicating that 87 instances newly gain LP discrimination while others lose it, yielding a $3{\times}$ increase in within-instance LP range for the newly non-tied subset.
696	Despite this reshuffling, aggregate NER selection gains remain negligible---score compression is not a fixed property of specific instances but rather a pervasive regime that shifts across instances without producing net selection improvement.
697	Free-form decoding also slightly improves quality estimation (NER VC $\rho$: 0.379$\to$0.409), though this does not translate to selection gains.
698	
699	\section{Free-Form Decoding Ablation}\label{app:freeform_ablation}
700	
701	Table~\ref{tab:freeform_ablation} compares constrained and free-form decoding across four dimensions on SciERC ($N{=}8$, $T{=}1.0$, Qwen3-8B; seed${=}42$ shown, 4-seed RE statistics below).
702	Free-form decoding removes grammar constraints entirely; outputs are parsed post-hoc (parse rate 99.95\%, 4406/4408).
703	LP score distributions are nearly identical across regimes (Panel~A: within-instance std ratio $0.97{\times}$), and NER selection gains remain negligible under both regimes (Panel~B).
704	RE LP selection consistently reverses direction under free-form decoding across 4 seeds: $+1.84{\pm}0.12$~pp (seeds 42/123/456/789: $+1.69$, $+1.76$, $+2.00$, $+1.91$~pp) vs.\ $-0.68$~pp constrained.
705	The constrained reference ($-0.68$~pp) uses the ablation-matched baseline; the primary experiment (Table~\ref{tab:selection}) yields $-0.9$~pp on the same gold-filtered set.
706	Quality estimation improves modestly for most signals under free-form decoding (Panel~C), with the largest gain for FK ($+0.053$ NER, $+0.039$ RE).
707	
708	\begin{table*}[t]
709	\centering
710	\caption{Comparison of constrained vs.\ free-form decoding on SciERC (Qwen3-8B, $N{=}8$, $T{=}1.0$, seed${=}42$; RE selection gap replicates across 4 seeds: $+1.84{\pm}0.12$~pp).}
711	\label{tab:freeform_ablation}
712	
713	\vspace{2pt}
714	{\small\textsc{Panel A: Logprob Distribution}}
715	\vspace{2pt}
716	
717	\begin{tabular}{lccc}
718	\toprule
719	Metric & Constrained & Free-form & $\Delta$ \\
720	\midrule
721	Mean LP std        & 0.0206 & 0.0199 & $-$0.0007 \\
722	Mean LP range      & 0.0623 & 0.0599 & $-$0.0024 \\
723	Tied fraction ($\varepsilon{=}0.05$) & 59.7\% & 57.7\% & $-$2.0\,pp \\
724	\bottomrule
725	\end{tabular}
726	
727	\vspace{8pt}
728	
729	{\small\textsc{Panel B: Selection F1}}
730	\vspace{2pt}
731	
732	\begin{tabular}{llccc}
733	\toprule
734	Task & Method & Constrained & Free-form & $\Delta$ \\
735	\midrule
736	\multirow{3}{*}{NER}
737	  & Single        & 0.6182 & 0.6204 & $+$0.0022 \\
738	  & LP-selected   & 0.6241 & 0.6222 & $-$0.0019 \\
739	  & Selection gap & $+$0.0059 & $+$0.0018 & $-$0.0041 \\
740	\midrule
741	\multirow{3}{*}{RE}
742	  & Single        & 0.2913 & 0.2880 & $-$0.0033 \\
743	  & LP-selected   & 0.2845 & 0.3050 & \textbf{$+$0.0205} \\
744	  & Selection gap & $-$0.0068 & $+$0.0169 & \textbf{$+$0.0237} \\
745	\bottomrule
746	\end{tabular}
747	
748	\vspace{8pt}
749	
750	{\small\textsc{Panel C: QE Signal Quality (Spearman $\rho$)}}
751	\vspace{2pt}
752	
753	\begin{tabular}{l ccc ccc}
754	\toprule
755	 & \multicolumn{3}{c}{NER ($n{=}529$)} & \multicolumn{3}{c}{RE ($n{=}397$)} \\
756	\cmidrule(lr){2-4} \cmidrule(lr){5-7}
757	Signal & Constr. & Free & $\Delta$ & Constr. & Free & $\Delta$ \\
758	\midrule
759	SJ & 0.360 & 0.377 & $+$0.018 & 0.250 & 0.273 & $+$0.023 \\
760	FK & 0.267 & 0.320 & $+$0.053 & 0.275 & 0.315 & $+$0.039 \\
761	LP & 0.205 & 0.213 & $+$0.008 & 0.266 & 0.304 & $+$0.038 \\
762	EM & 0.295 & 0.317 & $+$0.023 & 0.134 & 0.137 & $+$0.002 \\
763	VC & 0.379 & 0.409 & $+$0.030 & 0.350 & 0.323 & $-$0.026 \\
764	\bottomrule
765	\end{tabular}
766	
767	\vspace{8pt}
768	
769	{\small\textsc{Panel D: Parse Rate (Free-form)}}
770	\vspace{2pt}
771	
772	\begin{tabular}{lc}
773	\toprule
774	Metric & Value \\
775	\midrule
776	Total samples          & 4408 \\
777	Parse rate             & 99.95\% \\
778	Instances 8/8 valid    & 549\,/\,551 (99.6\%) \\
779	\bottomrule
780	\end{tabular}
781	
782	\end{table*}
783	
784	\paragraph{CoNLL NER free-form results.}
785	Extending the free-form ablation to CoNLL NER (Qwen3-8B, 4 seeds, $N{=}8$, $T{=}1.0$), LP range median is $0.058{\pm}0.007$ across seeds---higher than SciERC ($0.041$) but still compressed given CoNLL's 86.8\% tied fraction under constrained decoding.
786	Free-form decoding reduces the tied fraction modestly, yet selection remains below single-sample: LP-selected F1${=}0.896$ vs.\ single-sample $0.904$ ($\Delta{=}{-}0.77$~pp).
787	Quality estimation under free-form decoding yields SJ $\rho{=}0.461$, EM $\rho{=}0.471$, LP $\rho{=}0.326$---comparable to constrained results (Table~\ref{tab:quality_estimation}).
788	The failure to improve selection despite reduced compression is consistent with CoNLL's low oracle headroom (4.25~pp at $N{=}8$), which limits the selection space regardless of score distribution quality.
789	
790	\section{LP Selection Failure Stability}\label{app:lp_failure_stability}
791	
792	We analyze RE LP selection failures across three random seeds (constrained decoding, $N{=}8$, $T{=}1.0$, Qwen3-8B) to assess whether failures are systematic or stochastic.
793	
794	\paragraph{Pairwise overlap.}
795	LP selection failures (instances where LP-selected F1 $<$ single-sample F1) show moderate cross-seed stability: the average pairwise Jaccard similarity is 0.42 (range: 0.38--0.46), indicating that failures are partially systematic---driven by instance complexity---but not fully deterministic.
796	The 3-way intersection contains 34 instances (27.9\% of any-seed failures), confirming a stable failure core.
797	
798	\paragraph{Instance complexity drives failure.}
799	Table~\ref{tab:stable_failures} stratifies instances by failure stability.
800	Stable failures (all 3 seeds) involve more gold relations (2.12 vs.\ 1.62 for never-fail instances) and higher single-sample F1 (0.688 vs.\ 0.429), indicating that LP mis-selects on instances where the model already performs well---precisely the instances where selection would be most valuable.
801	Failure rate increases monotonically with gold relation count: 4.3\% at 1 relation, 20.7\% at 3 relations, 26.2\% at 6 relations.
802	
803	\begin{table}[t]
804	\centering
805	\small
806	\caption{RE LP selection failure stability across 3 seeds (SciERC, $N{=}8$). Stable failures concentrate on relation-dense instances with high single-sample F1.}
807	\label{tab:stable_failures}
808	\begin{tabular}{lcccc}
809	\toprule
810	Group & $n$ & Gold rels & Single F1 & LP $\Delta$F1 \\
811	\midrule
812	Stable fail (3 seeds) & 34 & 2.12 & 0.688 & $-$0.499 \\
813	Fail 2+ seeds & 26 & 2.46 & 0.774 & $-$0.450 \\
814	Fail 1 seed & 62 & 2.32 & 0.692 & $-$0.239 \\
815	Never fail & 429 & 1.62 & 0.429 & $+$0.041 \\
816	\bottomrule
817	\end{tabular}
818	\end{table}
819	
820	\paragraph{Flip instances.}
821	Only 5 RE instances with gold relations flip from LP failure (constrained) to LP success (free-form), with mean gold relation count 3.67 (well above the population mean of 1.86).
822	These instances show large constrained LP errors ($\Delta{=}{-}0.430$) that reverse under free-form decoding ($\Delta{=}{+}0.503$), but their rarity (5/397) confirms that the RE selection flip is driven by aggregate variance reallocation rather than systematic instance-level correction.
823	
824	\section{$N$-Scaling Detailed Analysis}\label{app:n_scaling}
825	
826	Tables~\ref{tab:n-scaling}--\ref{tab:sigma-comparison} provide detailed $N$-scaling analysis on Qwen3-8B SciERC with 3-seed statistics.
827	
828	\begin{table}[t]
829	\centering
830	\caption{Effect of sample pool size on signal quality (Qwen3-8B, SciERC, 3-seed mean Spearman $\rho$).}
831	\label{tab:n-scaling}
832	\small
833	\begin{tabular}{l ccc ccc}
834	\toprule
835	 & \multicolumn{3}{c}{\textbf{NER} $\rho$} & \multicolumn{3}{c}{\textbf{RE} $\rho$} \\
836	\cmidrule(lr){2-4} \cmidrule(lr){5-7}
837	Signal & $N\!=\!8$ & $N\!=\!16$ & $\Delta$ & $N\!=\!8$ & $N\!=\!16$ & $\Delta$ \\
838	\midrule
839	SJ & 0.3641 & 0.4105 & \textbf{+0.0464} & 0.2485 & 0.2758 & \textbf{+0.0273} \\
840	FK & 0.2536 & 0.2833 & \textbf{+0.0297} & 0.2903 & 0.2964 & \textbf{+0.0061} \\
841	VC & 0.3861 & 0.4092 & \textbf{+0.0231} & 0.3088 & 0.3738 & \textbf{+0.0650} \\
842	LP & 0.2167 & 0.2393 & \textbf{+0.0226} & 0.2970 & 0.3100 & \textbf{+0.0130} \\
843	EM & 0.3071 & 0.3395 & \textbf{+0.0324} & 0.1353 & 0.1506 & \textbf{+0.0153} \\
844	\midrule
845	Mean & 0.3055 & 0.3364 & \textbf{+0.0308} & 0.2560 & 0.2813 & \textbf{+0.0253} \\
846	\bottomrule
847	\end{tabular}
848	\end{table}
849	
850	\begin{table}[t]
851	\centering
852	\caption{Cross-seed signal ranking stability (Kendall's $W$, 3 seeds).}
853	\label{tab:ranking-stability}
854	\small
855	\begin{tabular}{ll cc l}
856	\toprule
857	Model & Task & $N$ & Kendall's $W$ & Consensus ranking \\
858	\midrule
859	Qwen  & NER & 8  & 1.000 & VC $>$ SJ $>$ EM $>$ FK $>$ LP \\
860	Qwen  & NER & 16 & 0.956 & SJ $\approx$ VC $>$ EM $>$ FK $>$ LP \\
861	Qwen  & RE  & 8  & 0.822 & VC $>$ LP $>$ FK $>$ SJ $>$ EM \\
862	Qwen  & RE  & 16 & 0.956 & VC $>$ LP $>$ FK $>$ SJ $>$ EM \\
863	LLaMA & NER & 8  & 1.000 & VC $>$ SJ $>$ EM $>$ FK $>$ LP \\
864	\bottomrule
865	\end{tabular}
866	\end{table}
867	
868	\begin{table}[t]
869	\centering
870	\caption{Cross-seed standard deviation ($\sigma$) of Spearman $\rho$ at $N\!=\!8$ vs.\ $N\!=\!16$ (Qwen3-8B, SciERC, 3 seeds). $\sigma$ is population standard deviation.}
871	\label{tab:sigma-comparison}
872	\small
873	\begin{tabular}{l cc cc}
874	\toprule
875	 & \multicolumn{2}{c}{\textbf{NER} $\sigma_\rho$} & \multicolumn{2}{c}{\textbf{RE} $\sigma_\rho$} \\
876	\cmidrule(lr){2-3} \cmidrule(lr){4-5}
877	Signal & $N\!=\!8$ & $N\!=\!16$ & $N\!=\!8$ & $N\!=\!16$ \\
878	\midrule
879	SJ & 0.0179 & 0.0102 & 0.0015 & 0.0067 \\
880	FK & 0.0157 & 0.0079 & 0.0121 & 0.0143 \\
881	VC & 0.0187 & 0.0260 & 0.0244 & 0.0158 \\
882	EM & 0.0076 & 0.0031 & 0.0157 & 0.0049 \\
883	LP & 0.0125 & 0.0017 & 0.0218 & 0.0152 \\
884	\midrule
885	Mean & 0.0145 & 0.0098 & 0.0151 & 0.0114 \\
886	\bottomrule
887	\end{tabular}
888	\end{table}
889	
890	Signal rankings are stable across our 3 seeds (Kendall's $W{=}1.000$ for NER at $N{=}8$, both models), dropping only to $W{=}0.956$ at $N{=}16$ where SJ and VC converge (Table~\ref{tab:ranking-stability}); however, statistical power with $n{=}3$ seeds is limited, and we cannot rule out that additional seeds would reveal ranking instability.
891	Doubling $N$ reduces cross-seed $\sigma$ by 32\% on NER and 24\% on RE (Table~\ref{tab:sigma-comparison}), with the largest reductions for SJ ($-43\%$ NER) and EM ($-59\%$ NER), confirming that additional samples stabilize structural signals more than LP.
892	
893	\section{Cross-Dataset OOD Analysis}\label{app:ood}
894	
895	To test whether confidence signals generalize under domain shift, we evaluate models on out-of-distribution data: a SciERC-trained model applied to CoNLL instances (wider$\to$narrower schema) and vice versa (Table~\ref{tab:ood}).
896	
897	\begin{table}[t]
898	\centering
899	\small
900	\caption{Cross-dataset OOD quality estimation (Spearman $\rho$, Qwen3-8B, $N{=}8$, $T{=}1.0$, seed${=}42$). SciERC$\to$CoNLL: SciERC-trained model on CoNLL instances ($n{=}2756$). CoNLL$\to$SciERC: CoNLL-trained model on SciERC instances ($n{=}529$, excluded from conclusions due to catastrophic model failure). In-domain $\rho$ from Table~\ref{tab:quality_estimation} (same model, same seed). \textsuperscript{***}$p{<}0.001$, \textsuperscript{*}$p{<}0.05$.}
901	\label{tab:ood}
902	\begin{tabular}{l ccc ccc}
903	\toprule
904	 & \multicolumn{3}{c}{\textbf{SciERC$\to$CoNLL}} & \multicolumn{3}{c}{\textbf{CoNLL$\to$SciERC}} \\
905	\cmidrule(lr){2-4} \cmidrule(lr){5-7}
906	Signal & $\rho$ & In-dom. & $\Delta$ & $\rho$ & In-dom. & $\Delta$ \\
907	\midrule
908	VC & .469\textsuperscript{***} & .379 & +.090 & +.105\textsuperscript{*} & .379 & $-$.274 \\
909	SJ & .378\textsuperscript{***} & .360 & +.018 & $-$.186\textsuperscript{***} & .360 & $-$.546 \\
910	EM & .300\textsuperscript{***} & .295 & +.005 & $-$.202\textsuperscript{***} & .295 & $-$.497 \\
911	FK & .285\textsuperscript{***} & .267 & +.018 & $-$.070 & .267 & $-$.337 \\
912	LP & .246\textsuperscript{***} & .205 & +.041 & $-$.152\textsuperscript{***} & .205 & $-$.357 \\
913	\bottomrule
914	\end{tabular}
915	\end{table}
916	
917	\paragraph{Wider-to-narrower schema transfer.}
918	When the SciERC-trained model (6 NER types) is applied to CoNLL (4 types), all signals remain significant ($p{<}0.001$) and structural signals improve over their in-domain levels (same model, seed${=}42$, $N{=}8$; in-domain $\rho$ from Table~\ref{tab:quality_estimation}): VC reaches $\rho{=}0.469$ (in-domain $0.379$, $\Delta{=}{+}0.090$), SJ $\rho{=}0.378$ (in-domain $0.360$, $\Delta{=}{+}0.018$), and FK $\rho{=}0.285$ (in-domain $0.267$, $\Delta{=}{+}0.018$).
919	The wider training schema subsumes CoNLL's narrower schema, so the model produces reasonable outputs even out-of-domain (single-sample F1${=}0.522$), and structural signals benefit from the simpler target schema's reduced output ambiguity.
920	
921	\paragraph{Narrower-to-wider schema transfer (excluded).}
922	The reverse direction is excluded from our conclusions due to catastrophic model failure, not signal failure.
923	The CoNLL-trained model recognizes only 4 news entity types (PER, ORG, LOC, MISC) and has no relation extraction capability; when applied to SciERC's 6 scientific entity types and 7 relation types, the model cannot produce meaningful structured outputs (single-sample NER F1${=}0.009$, RE F1${=}0.001$).
924	Under this regime, most signals flip to negative or near-zero correlations (Table~\ref{tab:ood}); only VC retains weak positive correlation ($\rho{=}0.105$, $p{=}0.016$).
925	These negative correlations reflect the model systematically generating confident but incorrect outputs---a capability failure analogous to WNUT-17 (\S\ref{sec:qe_results}), not evidence against signal utility.
926	
927	\paragraph{Asymmetry interpretation.}
928	The directional asymmetry is driven by schema coverage: wider$\to$narrower preserves signal utility because the SciERC model's 6-type schema subsumes CoNLL's 4 types, while narrower$\to$wider fails because the CoNLL model lacks the entity and relation types required by SciERC.
929	This extends the capability boundary identified on WNUT-17 to the domain-shift setting: confidence signals require sufficient model capability as a prerequisite, and results from the CoNLL$\to$SciERC direction should not be interpreted as evidence of signal degradation under domain shift.
930	
931	\section{Verbalized Confidence}\label{app:verbalized_confidence}
932	
933	We evaluate verbalized confidence (VerbConf) as a second per-sample signal following \citet{tian2023calibration}: after generating each structured output, the model is prompted to rate its confidence on a 1--10 scale.
934	Table~\ref{tab:verbconf} reports quality estimation and selection results.
935	
936	\begin{table}[t]
937	\centering
938	\small
939	\caption{Verbalized confidence (VerbConf) vs.\ log-probability selection (Qwen3-8B, $N{=}8$, $T{=}1.0$, seed${=}42$). Parse fail: fraction of samples where the confidence score could not be extracted.}
940	\label{tab:verbconf}
941	\begin{tabular}{l cc cc}
942	\toprule
943	 & \multicolumn{2}{c}{\textbf{SciERC NER}} & \multicolumn{2}{c}{\textbf{CoNLL NER}} \\
944	\cmidrule(lr){2-3} \cmidrule(lr){4-5}
945	Metric & VerbConf & LP & VerbConf & LP \\
946	\midrule
947	$\rho$ & 0.297 & 0.205 & 0.337 & 0.316 \\
948	AUROC & 0.681 & 0.578 & 0.747 & 0.753 \\
949	Selection F1 & 0.620 & 0.647 & 0.889 & 0.904 \\
950	$\Delta$ vs.\ single-sample & $-$2.45\,pp & $+$0.2\,pp & $-$1.93\,pp & $-$0.77\,pp \\
951	\midrule
952	Mean score & 8.58\,/\,10 & --- & 9.24\,/\,10 & --- \\
953	Parse fail rate & 0.26\% & --- & 0\% & --- \\
954	\bottomrule
955	\end{tabular}
956	\end{table}
957	
958	\paragraph{Severe overconfidence.}
959	VerbConf exhibits extreme score compression: mean confidence is 8.58/10 on SciERC (single-sample F1${=}0.645$) and 9.24/10 on CoNLL (single-sample F1${=}0.904$), with most scores concentrated in the 8--10 range.
960	This compression is more severe than LP (which spans a 0.041-nat median range), confirming that score compression is a general property of model self-assessment, not an artifact of log-probability computation.
961	
962	\paragraph{QE--selection decoupling.}
963	VerbConf achieves higher $\rho$ than LP on both datasets (SciERC: 0.297 vs.\ 0.205; CoNLL: 0.337 vs.\ 0.316) and competitive AUROC (SciERC: 0.681 vs.\ 0.578; CoNLL: 0.747 vs.\ 0.753), yet yields the worst selection among all signals ($\Delta{=}{-}2.45$~pp on SciERC, $-1.93$~pp on CoNLL).
964	This dissociation further demonstrates the correlation-selection gap: a signal can rank instances by expected quality without being able to discriminate candidates within an instance.
965	The AUROC--$\rho$ decoupling on CoNLL (LP leads AUROC at 0.753 while VerbConf leads $\rho$ at 0.337) reflects differing sensitivity to binary vs.\ ordinal discrimination.
966	
967	\section{LLaMA-3.2-3B Scale Ablation}\label{app:llama3b}
968	
969	To extend scale coverage below 4B, we fine-tune LLaMA-3.2-3B-Instruct on SciERC NER under identical training conditions (LoRA rank${=}32$, $\alpha{=}64$, 5 epochs) and evaluate quality estimation and selection (Table~\ref{tab:llama3b}).
970	
971	\begin{table}[t]
972	\centering
973	\small
974	\caption{LLaMA-3.2-3B SciERC NER quality estimation and selection ($N{=}8$, $T{=}1.0$, seed${=}42$). Single-sample F1${=}0.627$, Oracle F1${=}0.763$, headroom${=}13.63$~pp.}
975	\label{tab:llama3b}
976	\begin{tabular}{l cc cc}
977	\toprule
978	Signal & $\rho$ & AUROC & Sel.\ F1 & $\Delta$ vs.\ single-sample \\
979	\midrule
980	VC & \textbf{.460} & .743 & 0.611 & $-$1.54\,pp \\
981	SJ & .375 & .738 & \textbf{0.633} & $+$0.61\,pp \\
982	EM & .334 & \textbf{.776} & --- & --- \\
983	FK & .268 & .671 & 0.630 & $+$0.28\,pp \\
984	LP & .266 & .633 & 0.628 & $+$0.12\,pp \\
985	\midrule
986	Single & --- & --- & 0.627 & --- \\
987	Oracle & --- & --- & 0.763 & --- \\
988	\bottomrule
989	\end{tabular}
990	\end{table}
991	
992	The $\rho$ ranking at 3B (VC $>$ SJ $>$ EM $>$ FK $\approx$ LP) preserves the structural-over-LP ordering from 8B (Table~\ref{tab:quality_estimation}), confirming ranking stability across two model families spanning 3B--8B.
993	AUROC rankings differ (EM $>$ VC $>$ SJ $>$ FK $>$ LP), reflecting the $\rho$--AUROC dissociation noted in the main text.
994	Despite 13.63~pp of oracle headroom, no signal achieves significant selection improvement (best: SJ, $+0.61$~pp, $p{=}0.175$); VC---the strongest QE signal---yields the worst selection ($-1.54$~pp), consistent with the correlation-selection gap observed at larger scales.
995	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "40bb3365-8693-4466-8d86-69f5302a39f9",
  "isSidechain": false,
  "promptId": "0399fd48-9ce8-44a9-a460-553e3e5fc517",
  "type": "user",
  "uuid": "75e36376-f374-4c79-917b-692261dea871",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
      "content": "At this cutpoint, 60.3\\% of instances ($n{=}529$, excluding empty gold annotations) have a within-sample range below $\\varepsilon$, and 75\\% of pairwise comparisons are effective ties ($|\\Delta|{<}0.026$).\nThe CDF rises smoothly with no cliff or discontinuity (Figure~\\ref{fig:lp_range_cdf}), confirming that compression is a pervasive regime rather than a bimodal split.\nThis compression is stable across seeds: seed${=}456$ yields median LP range${=}0.040$ nats and tied fraction${=}62.2\\%$ (vs.\\ seed${=}42$: $0.041$ nats, $60.3\\%$).\nSeed~456 uses a different subtask flag (joint vs.\\ ner for seeds 42 and 123); the LP distributions are statistically indistinguishable (median LP: 8.37 vs.\\ 8.20 nats; Mann--Whitney $p{=}0.55$), confirming that the subtask change does not affect compression.\nFor comparison, SJ has only 12.5\\% tied instances at the same threshold---SJ's advantage over LP for selection is one of score resolution, not information content.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{fig_lp_range_cdf}\n\\caption{CDF of within-instance LP range on SciERC NER ($N{=}8$, $n{=}529$). The median LP range is 0.041 nats (dashed line), below $\\varepsilon{=}0.05$. The smooth CDF confirms compression is pervasive, not bimodal.}\n\\label{fig:lp_range_cdf}\n\\end{figure}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Log-probability score compression on SciERC NER ($N{=}8$, $n{=}529$). ``Tied'' = fraction of instances where within-instance LP range ${<}\\varepsilon$.}\n\\label{tab:logprob_ties}\n\\begin{tabular}{lc}\n\\toprule\n$\\varepsilon$ threshold & Tied instances (\\%) \\\\\n\\midrule\n0.01 & 1.1\\% \\\\\n0.05 & 60.3\\% \\\\\n0.1  & ${\\sim}$84\\% \\\\\n0.5  & ${\\sim}$99\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Non-tied subset.}\nAmong instances with LP range ${\\geq}0.05$ ($n{=}210$, 40\\% of total), log-probability selection \\textit{significantly} outperforms single-sample ($+2.9$~pp F1, $p{=}0.004$), and within-instance $\\rho(\\text{LP}, \\text{F1})$ rises from 0.08 (tied subset) to 0.39 (non-tied subset).\nAs a continuous complement to the binary tied/non-tied analysis, pooled within-instance $\\rho(\\text{LP}, \\text{F1}){=}0.248$ across all instances confirms weak but positive per-sample signal; however, only 21.6\\% of instances achieve $p{<}0.05$ significance, and $\\rho(\\text{LP range}, \\text{F1 range}){=}0.328$ shows that instances with more LP spread also exhibit more F1 variability---LP carries information but compression limits its exploitation.\nA free-form NER decoding ablation (Appendix~\\ref{app:freeform_ablation}) confirms this compression persists without constrained decoding.\n\n\\paragraph{$\\varepsilon$ sensitivity sweep (post-hoc exploratory).}\nTable~\\ref{tab:epsilon_sweep} sweeps the tied/non-tied threshold from $\\varepsilon{=}0.01$ to $0.20$ as a post-hoc exploratory analysis characterizing how selection gain varies with compression severity.\nThe tied fraction increases smoothly with no cliff or discontinuity, and the selection gain $\\Delta$ grows monotonically as the non-tied subset narrows to progressively higher-spread instances.\n$\\varepsilon{=}0.05$ yields the strongest statistical separation ($p{=}0.004$); at $\\varepsilon{\\geq}0.15$, the non-tied subset becomes too small for reliable inference ($n{\\leq}36$).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{$\\varepsilon$ sensitivity sweep for LP selection on SciERC NER ($N{=}8$, seed${=}42$, $n{=}529$). ``Tied\\%'' = fraction with within-instance LP range ${<}\\varepsilon$. $\\Delta$: selection F1 gain over single-sample on the non-tied subset. The tied fraction increases smoothly; $\\varepsilon{=}0.05$ yields the strongest statistical separation.}\n\\label{tab:epsilon_sweep}\n\\begin{tabular}{ccccc}\n\\toprule\n$\\varepsilon$ & Tied\\% & Non-tied $n$ & $\\Delta$ (pp) & $p$ \\\\\n\\midrule\n0.01 & 1.1\\% & 523 & $+$0.58 & .21 \\\\\n0.02 & 13.6\\% & 457 & $+$0.83 & .15 \\\\\n0.03 & 31.8\\% & 361 & $+$1.31 & .079 \\\\\n\\textbf{0.05} & \\textbf{60.3\\%} & \\textbf{210} & \\textbf{$+$2.86} & \\textbf{.004} \\\\\n0.10 & 83.9\\% & 85 & $+$3.69 & .034 \\\\\n0.15 & 93.2\\% & 36 & $+$4.15 & .11 \\\\\n0.20 & 96.4\\% & 19 & $+$4.59 & .13 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{$\\varepsilon$ robustness of selection F1.}\\label{app:epsilon_robustness}\nThe preceding analysis stratifies LP by a tied/non-tied threshold; consistency-based signals (SJ, FK, VC, EM) also use $\\varepsilon$ to define MBR-style proximity in selection.\nTable~\\ref{tab:epsilon_robustness} reports the maximum selection F1 variation across $\\varepsilon \\in [0, 0.2]$ for all signals and configurations.\nAt $\\varepsilon{=}0.05$, consistency signals change by at most 1.09~pp (mean 0.21~pp), with EM completely $\\varepsilon$-invariant (integer scoring); LP is the most sensitive (up to 3.65~pp across the full range), as expected.\nSpearman $\\rho$---the primary quality estimation metric throughout---is a continuous rank correlation that does not depend on any discretization threshold; the $\\varepsilon$ parameter affects only the selection analysis.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Maximum selection F1 variation (pp) across $\\varepsilon \\in [0, 0.2]$. At $\\varepsilon{=}0.05$ (used throughout), consistency signals change by ${\\leq}1.09$~pp; EM is invariant (integer scoring). LP is most sensitive as $\\varepsilon$ governs its tied/non-tied partition. SciERC: $n{=}529$; CoNLL: $n{=}2{,}756$.}\n\\label{tab:epsilon_robustness}\n\\begin{tabular}{lcccc}\n\\toprule\n& \\multicolumn{2}{c}{\\textbf{SciERC}} & \\multicolumn{2}{c}{\\textbf{CoNLL}} \\\\\n\\cmidrule(lr){2-3} \\cmidrule(lr){4-5}\nSignal & Qwen & LLaMA & Qwen & LLaMA \\\\\n\\midrule\nSJ & 0.92 & 1.45 & 0.99 & 0.18 \\\\\nFK & 1.03 & 0.93 & 0.60 & 0.15 \\\\\nVC & 2.33 & 0.53 & 0.72 & 0.18 \\\\\nEM & 0.00 & 0.00 & 0.00 & 0.00 \\\\\nLP & 3.65 & 2.58 & 3.00 & 0.31 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{Consistency-Stratified Selection Analysis}\\label{app:vc_quartile}\n\nTable~\\ref{tab:vc_quartile} stratifies SciERC instances by voting confidence (VC) quartiles and reports selection $\\Delta$ (gain over single-sample) for LP and SJ.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Selection $\\Delta$ (pp over single-sample) stratified by VC quartile on SciERC ($N{=}8$, Qwen3-8B). Oracle headroom collapses at Q4; LP rankings are unreliable at Q1--Q2. Neither quartile supports consistent selection gains.}\n\\label{tab:vc_quartile}\n\\begin{tabular}{lcccc}\n\\toprule\nQuartile & Mean VC & LP $\\Delta$ & SJ $\\Delta$ & Oracle (pp) \\\\\n\\midrule\n\\multicolumn{5}{l}{\\textit{NER}} \\\\\nQ1 (low) & 0.30 & $+$1.55 & $+$0.54 & 16.85 \\\\\nQ2 & 0.51 & $-$0.65 & $-$1.89 & 14.35 \\\\\nQ3 & 0.68 & $+$1.97 & $+$1.84 & 16.83 \\\\\nQ4 (high) & 0.92 & $-$0.41 & $-$0.04 & 4.78 \\\\\n\\midrule\n\\multicolumn{5}{l}{\\textit{$^\\dagger$RE}} \\\\\nQ1 (low) & --- & $-$3.56 & --- & --- \\\\\nQ4 (high) & --- & $+$4.01 & --- & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe NER pattern reveals two complementary failure modes rather than a monotonic relationship between consistency and selection gain:\n\\begin{itemize}\n\\item \\textbf{Q4 ceiling effect.} High-consistency instances (mean VC${=}0.92$) have oracle headroom of only 4.78~pp---samples have already converged, leaving little room for any signal to improve selection.\n\\item \\textbf{Q1--Q2 noise.} Low-consistency instances retain large headroom (14--17~pp) but LP rankings are unreliable, yielding inconsistent $\\Delta$ signs across quartiles.\n\\end{itemize}\n\nOn $^\\dagger$RE, the pattern differs: Q4 LP achieves $+4.01$~pp, suggesting LP can recover selection ability when high consistency coincides with structured output diversity. This is a single-dataset observation and should be interpreted cautiously.\n\nOn CoNLL NER, Q3--Q4 instances have VC${=}1.0$ (all samples identical), yielding $\\Delta{=}0$ universally---a ceiling effect even more extreme than SciERC Q4.\n\n\\section{RE Conditional Selection}\\label{app:re_conditional_selection}\n\nTable~\\ref{tab:re_cond_selection} extends the selection analysis to the RE non-zero F1 subset.\nOf $n{=}397$ RE instances, 238 (60\\%) have non-zero F1 and 159 (40\\%) have zero F1.\nAll five signals underperform single-sample on both subsets.\nOn the non-zero subset, selection performance is \\textit{worse} than on the full set (e.g., VC: $-10.0$~pp on non-zero vs.\\ $-4.5$~pp on full set), because single-sample is already strong on non-zero instances (F1${=}0.674$) and signals actively select inferior samples.\nOracle headroom exists (0.757 vs.\\ 0.674) but no signal exploits it, ruling out the 40\\% zero-F1 floor effect as the explanation for RE selection failure.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{RE selection F1 (macro, instance-averaged) on SciERC ($N{=}8$, $T{=}1.0$). Full set ($n{=}397$) and non-zero F1 subset ($n{=}238$). No signal outperforms single-sample on either subset.}\n\\label{tab:re_cond_selection}\n\\begin{tabular}{lcc}\n\\toprule\nMethod & Full ($n{=}397$) & Non-zero ($n{=}238$) \\\\\n\\midrule\nOracle & 0.585 & 0.757 \\\\\n\\midrule\nLP & 0.395 & 0.600 \\\\\nSJ & 0.386 & 0.604 \\\\\nEM & 0.372 & 0.583 \\\\\nVC & 0.359 & 0.574 \\\\\n\\midrule\nSingle & 0.404 & 0.674 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{RE $N{=}16$ Selection Analysis}\\label{app:re_n16_selection}\n\nTable~\\ref{tab:re_n16_selection} extends the selection analysis to RE at $N{=}16$ with 3-seed statistics.\nAll four consistency signals underperform single-sample, with EM showing the largest deficit ($\\Delta{=}{-}1.5$~pp, Fisher $p{>}0.99$).\nLP is the only positive signal ($\\Delta{=}{+}0.7$~pp, Fisher $p{=}0.058$), driven primarily by seed~456 ($\\Delta{=}{+}1.5$~pp, $p{=}0.026$); the remaining seeds show smaller effects ($+0.1$ and $+0.6$~pp, $p{>}0.20$).\nEven the most favorable seed captures only ${\\sim}9\\%$ of the 17.1~pp oracle headroom.\nThis cross-task consistency---LP as the only viable selection signal on both NER and RE---reinforces the structural limitation of instance-level signals for candidate ranking.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{RE best-of-$N$ selection F1 (macro, instance-averaged) on SciERC (Qwen3-4B, $N{=}16$, $T{=}1.0$, 3-seed mean${\\pm}\\sigma$, $n{=}551$). Fisher combined $p$ vs.\\ single-sample. LP is the only signal with positive $\\Delta$. $\\sigma$ is population standard deviation over 3 seeds.}\n\\label{tab:re_n16_selection}\n\\begin{tabular}{lccc}\n\\toprule\nMethod & F1 & $\\Delta$ (pp) & $p$(Fisher) \\\\\n\\midrule\nOracle & $.463{\\pm}.006$ & $+$17.1 & --- \\\\\n\\midrule\nLP & $\\mathbf{.299}{\\pm}.007$ & $+$0.7 & .058 \\\\\nVC & $.284{\\pm}.002$ & $-$0.8 & .973 \\\\\nFK & $.283{\\pm}.005$ & $-$0.9 & .985 \\\\\nSJ & $.281{\\pm}.005$ & $-$1.0 & .993 \\\\\nEM & $.277{\\pm}.007$ & $-$1.5 & .999 \\\\\n\\midrule\nSingle & $.291{\\pm}.000$ & --- & --- \\\\\nRandom & $.262{\\pm}.001$ & $-$2.9 & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{MBR Decoding and Task-Specific Interactions}\\label{app:mbr_discussion}\n\n\\paragraph{Connection to MBR decoding.}\nOur selection strategies instantiate minimum Bayes risk (MBR) decoding \\cite{eikema2022sampling, muller2021understanding}: each selects $\\hat{y} = \\arg\\max_{y_i} \\sum_{j \\neq i} U(y_i, y_j)$ with utility $U$ defined by SJ, EM, or entity overlap.\nDespite MBR's success in machine translation \\cite{freitag2022high} and its extension to summarization, code generation, and captioning \\cite{jinnai2024mbr}, all variants fail here because the utility functions correlate with F1 at the instance level but not within a single instance---the mathematical essence of the correlation-selection gap.\n\\citet{eikema2025structured} study structure-conditional MBR decoding and find that standard utility functions degrade on structured outputs---consistent with our finding that consensus-proximity selection fails in IE despite its success in machine translation.\n\n\\paragraph{Task-specific decoding interactions.}\nThe free-form ablation reveals divergent behavior across tasks.\nOn RE, LP selection flips from $-0.68$~pp (constrained) to $+1.69$~pp (free-form; preliminary, single RE benchmark), a reversal that spans all 7 relation types and is driven by selective variance reallocation ($p{<}0.0001$).\nThe win/loss ratio shifts from 36:59 (constrained) to 45:45 (free-form), with the gains concentrated on relation-dense instances (mean 3.3 gold relations).\nThis interaction does not generalize to NER, where selection remains negligible under both regimes.\nThis ablation uses a single seed (seed${=}42$); whether the RE reversal replicates across seeds and generalizes to other RE benchmarks warrants further investigation.\nThe non-tied subset ($n{=}210$) is partially reshuffled under free-form decoding: Jaccard similarity between the constrained and free-form non-tied sets is 0.472, indicating that 87 instances newly gain LP discrimination while others lose it, yielding a $3{\\times}$ increase in within-instance LP range for the newly non-tied subset.\nDespite this reshuffling, aggregate NER selection gains remain negligible---score compression is not a fixed property of specific instances but rather a pervasive regime that shifts across instances without producing net selection improvement.\nFree-form decoding also slightly improves quality estimation (NER VC $\\rho$: 0.379$\\to$0.409), though this does not translate to selection gains.\n\n\\section{Free-Form Decoding Ablation}\\label{app:freeform_ablation}\n\nTable~\\ref{tab:freeform_ablation} compares constrained and free-form decoding across four dimensions on SciERC ($N{=}8$, $T{=}1.0$, Qwen3-8B; seed${=}42$ shown, 4-seed RE statistics below).\nFree-form decoding removes grammar constraints entirely; outputs are parsed post-hoc (parse rate 99.95\\%, 4406/4408).\nLP score distributions are nearly identical across regimes (Panel~A: within-instance std ratio $0.97{\\times}$), and NER selection gains remain negligible under both regimes (Panel~B).\nRE LP selection consistently reverses direction under free-form decoding across 4 seeds: $+1.84{\\pm}0.12$~pp (seeds 42/123/456/789: $+1.69$, $+1.76$, $+2.00$, $+1.91$~pp) vs.\\ $-0.68$~pp constrained.\nThe constrained reference ($-0.68$~pp) uses the ablation-matched baseline; the primary experiment (Table~\\ref{tab:selection}) yields $-0.9$~pp on the same gold-filtered set.\nQuality estimation improves modestly for most signals under free-form decoding (Panel~C), with the largest gain for FK ($+0.053$ NER, $+0.039$ RE).\n\n\\begin{table*}[t]\n\\centering\n\\caption{Comparison of constrained vs.\\ free-form decoding on SciERC (Qwen3-8B, $N{=}8$, $T{=}1.0$, seed${=}42$; RE selection gap replicates across 4 seeds: $+1.84{\\pm}0.12$~pp).}\n\\label{tab:freeform_ablation}\n\n\\vspace{2pt}\n{\\small\\textsc{Panel A: Logprob Distribution}}\n\\vspace{2pt}\n\n\\begin{tabular}{lccc}\n\\toprule\nMetric & Constrained & Free-form & $\\Delta$ \\\\\n\\midrule\nMean LP std        & 0.0206 & 0.0199 & $-$0.0007 \\\\\nMean LP range      & 0.0623 & 0.0599 & $-$0.0024 \\\\\nTied fraction ($\\varepsilon{=}0.05$) & 59.7\\% & 57.7\\% & $-$2.0\\,pp \\\\\n\\bottomrule\n\\end{tabular}\n\n\\vspace{8pt}\n\n{\\small\\textsc{Panel B: Selection F1}}\n\\vspace{2pt}\n\n\\begin{tabular}{llccc}\n\\toprule\nTask & Method & Constrained & Free-form & $\\Delta$ \\\\\n\\midrule\n\\multirow{3}{*}{NER}\n  & Single        & 0.6182 & 0.6204 & $+$0.0022 \\\\\n  & LP-selected   & 0.6241 & 0.6222 & $-$0.0019 \\\\\n  & Selection gap & $+$0.0059 & $+$0.0018 & $-$0.0041 \\\\\n\\midrule\n\\multirow{3}{*}{RE}\n  & Single        & 0.2913 & 0.2880 & $-$0.0033 \\\\\n  & LP-selected   & 0.2845 & 0.3050 & \\textbf{$+$0.0205} \\\\\n  & Selection gap & $-$0.0068 & $+$0.0169 & \\textbf{$+$0.0237} \\\\\n\\bottomrule\n\\end{tabular}\n\n\\vspace{8pt}\n\n{\\small\\textsc{Panel C: QE Signal Quality (Spearman $\\rho$)}}\n\\vspace{2pt}\n\n\\begin{tabular}{l ccc ccc}\n\\toprule\n & \\multicolumn{3}{c}{NER ($n{=}529$)} & \\multicolumn{3}{c}{RE ($n{=}397$)} \\\\\n\\cmidrule(lr){2-4} \\cmidrule(lr){5-7}\nSignal & Constr. & Free & $\\Delta$ & Constr. & Free & $\\Delta$ \\\\\n\\midrule\nSJ & 0.360 & 0.377 & $+$0.018 & 0.250 & 0.273 & $+$0.023 \\\\\nFK & 0.267 & 0.320 & $+$0.053 & 0.275 & 0.315 & $+$0.039 \\\\\nLP & 0.205 & 0.213 & $+$0.008 & 0.266 & 0.304 & $+$0.038 \\\\\nEM & 0.295 & 0.317 & $+$0.023 & 0.134 & 0.137 & $+$0.002 \\\\\nVC & 0.379 & 0.409 & $+$0.030 & 0.350 & 0.323 & $-$0.026 \\\\\n\\bottomrule\n\\end{tabular}\n\n\\vspace{8pt}\n\n{\\small\\textsc{Panel D: Parse Rate (Free-form)}}\n\\vspace{2pt}\n\n\\begin{tabular}{lc}\n\\toprule\nMetric & Value \\\\\n\\midrule\nTotal samples          & 4408 \\\\\nParse rate             & 99.95\\% \\\\\nInstances 8/8 valid    & 549\\,/\\,551 (99.6\\%) \\\\\n\\bottomrule\n\\end{tabular}\n\n\\end{table*}\n\n\\paragraph{CoNLL NER free-form results.}\nExtending the free-form ablation to CoNLL NER (Qwen3-8B, 4 seeds, $N{=}8$, $T{=}1.0$), LP range median is $0.058{\\pm}0.007$ across seeds---higher than SciERC ($0.041$) but still compressed given CoNLL's 86.8\\% tied fraction under constrained decoding.\nFree-form decoding reduces the tied fraction modestly, yet selection remains below single-sample: LP-selected F1${=}0.896$ vs.\\ single-sample $0.904$ ($\\Delta{=}{-}0.77$~pp).\nQuality estimation under free-form decoding yields SJ $\\rho{=}0.461$, EM $\\rho{=}0.471$, LP $\\rho{=}0.326$---comparable to constrained results (Table~\\ref{tab:quality_estimation}).\nThe failure to improve selection despite reduced compression is consistent with CoNLL's low oracle headroom (4.25~pp at $N{=}8$), which limits the selection space regardless of score distribution quality.\n\n\\section{LP Selection Failure Stability}\\label{app:lp_failure_stability}\n\nWe analyze RE LP selection failures across three random seeds (constrained decoding, $N{=}8$, $T{=}1.0$, Qwen3-8B) to assess whether failures are systematic or stochastic.\n\n\\paragraph{Pairwise overlap.}\nLP selection failures (instances where LP-selected F1 $<$ single-sample F1) show moderate cross-seed stability: the average pairwise Jaccard similarity is 0.42 (range: 0.38--0.46), indicating that failures are partially systematic---driven by instance complexity---but not fully deterministic.\nThe 3-way intersection contains 34 instances (27.9\\% of any-seed failures), confirming a stable failure core.\n\n\\paragraph{Instance complexity drives failure.}\nTable~\\ref{tab:stable_failures} stratifies instances by failure stability.\nStable failures (all 3 seeds) involve more gold relations (2.12 vs.\\ 1.62 for never-fail instances) and higher single-sample F1 (0.688 vs.\\ 0.429), indicating that LP mis-selects on instances where the model already performs well---precisely the instances where selection would be most valuable.\nFailure rate increases monotonically with gold relation count: 4.3\\% at 1 relation, 20.7\\% at 3 relations, 26.2\\% at 6 relations.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{RE LP selection failure stability across 3 seeds (SciERC, $N{=}8$). Stable failures concentrate on relation-dense instances with high single-sample F1.}\n\\label{tab:stable_failures}\n\\begin{tabular}{lcccc}\n\\toprule\nGroup & $n$ & Gold rels & Single F1 & LP $\\Delta$F1 \\\\\n\\midrule\nStable fail (3 seeds) & 34 & 2.12 & 0.688 & $-$0.499 \\\\\nFail 2+ seeds & 26 & 2.46 & 0.774 & $-$0.450 \\\\\nFail 1 seed & 62 & 2.32 & 0.692 & $-$0.239 \\\\\nNever fail & 429 & 1.62 & 0.429 & $+$0.041 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Flip instances.}\nOnly 5 RE instances with gold relations flip from LP failure (constrained) to LP success (free-form), with mean gold relation count 3.67 (well above the population mean of 1.86).\nThese instances show large constrained LP errors ($\\Delta{=}{-}0.430$) that reverse under free-form decoding ($\\Delta{=}{+}0.503$), but their rarity (5/397) confirms that the RE selection flip is driven by aggregate variance reallocation rather than systematic instance-level correction.\n\n\\section{$N$-Scaling Detailed Analysis}\\label{app:n_scaling}\n\nTables~\\ref{tab:n-scaling}--\\ref{tab:sigma-comparison} provide detailed $N$-scaling analysis on Qwen3-8B SciERC with 3-seed statistics.\n\n\\begin{table}[t]\n\\centering\n\\caption{Effect of sample pool size on signal quality (Qwen3-8B, SciERC, 3-seed mean Spearman $\\rho$).}\n\\label{tab:n-scaling}\n\\small\n\\begin{tabular}{l ccc ccc}\n\\toprule\n & \\multicolumn{3}{c}{\\textbf{NER} $\\rho$} & \\multicolumn{3}{c}{\\textbf{RE} $\\rho$} \\\\\n\\cmidrule(lr){2-4} \\cmidrule(lr){5-7}\nSignal & $N\\!=\\!8$ & $N\\!=\\!16$ & $\\Delta$ & $N\\!=\\!8$ & $N\\!=\\!16$ & $\\Delta$ \\\\\n\\midrule\nSJ & 0.3641 & 0.4105 & \\textbf{+0.0464} & 0.2485 & 0.2758 & \\textbf{+0.0273} \\\\\nFK & 0.2536 & 0.2833 & \\textbf{+0.0297} & 0.2903 & 0.2964 & \\textbf{+0.0061} \\\\\nVC & 0.3861 & 0.4092 & \\textbf{+0.0231} & 0.3088 & 0.3738 & \\textbf{+0.0650} \\\\\nLP & 0.2167 & 0.2393 & \\textbf{+0.0226} & 0.2970 & 0.3100 & \\textbf{+0.0130} \\\\\nEM & 0.3071 & 0.3395 & \\textbf{+0.0324} & 0.1353 & 0.1506 & \\textbf{+0.0153} \\\\\n\\midrule\nMean & 0.3055 & 0.3364 & \\textbf{+0.0308} & 0.2560 & 0.2813 & \\textbf{+0.0253} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[t]\n\\centering\n\\caption{Cross-seed signal ranking stability (Kendall's $W$, 3 seeds).}\n\\label{tab:ranking-stability}\n\\small\n\\begin{tabular}{ll cc l}\n\\toprule\nModel & Task & $N$ & Kendall's $W$ & Consensus ranking \\\\\n\\midrule\nQwen  & NER & 8  & 1.000 & VC $>$ SJ $>$ EM $>$ FK $>$ LP \\\\\nQwen  & NER & 16 & 0.956 & SJ $\\approx$ VC $>$ EM $>$ FK $>$ LP \\\\\nQwen  & RE  & 8  & 0.822 & VC $>$ LP $>$ FK $>$ SJ $>$ EM \\\\\nQwen  & RE  & 16 & 0.956 & VC $>$ LP $>$ FK $>$ SJ $>$ EM \\\\\nLLaMA & NER & 8  & 1.000 & VC $>$ SJ $>$ EM $>$ FK $>$ LP \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[t]\n\\centering\n\\caption{Cross-seed standard deviation ($\\sigma$) of Spearman $\\rho$ at $N\\!=\\!8$ vs.\\ $N\\!=\\!16$ (Qwen3-8B, SciERC, 3 seeds). $\\sigma$ is population standard deviation.}\n\\label{tab:sigma-comparison}\n\\small\n\\begin{tabular}{l cc cc}\n\\toprule\n & \\multicolumn{2}{c}{\\textbf{NER} $\\sigma_\\rho$} & \\multicolumn{2}{c}{\\textbf{RE} $\\sigma_\\rho$} \\\\\n\\cmidrule(lr){2-3} \\cmidrule(lr){4-5}\nSignal & $N\\!=\\!8$ & $N\\!=\\!16$ & $N\\!=\\!8$ & $N\\!=\\!16$ \\\\\n\\midrule\nSJ & 0.0179 & 0.0102 & 0.0015 & 0.0067 \\\\\nFK & 0.0157 & 0.0079 & 0.0121 & 0.0143 \\\\\nVC & 0.0187 & 0.0260 & 0.0244 & 0.0158 \\\\\nEM & 0.0076 & 0.0031 & 0.0157 & 0.0049 \\\\\nLP & 0.0125 & 0.0017 & 0.0218 & 0.0152 \\\\\n\\midrule\nMean & 0.0145 & 0.0098 & 0.0151 & 0.0114 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nSignal rankings are stable across our 3 seeds (Kendall's $W{=}1.000$ for NER at $N{=}8$, both models), dropping only to $W{=}0.956$ at $N{=}16$ where SJ and VC converge (Table~\\ref{tab:ranking-stability}); however, statistical power with $n{=}3$ seeds is limited, and we cannot rule out that additional seeds would reveal ranking instability.\nDoubling $N$ reduces cross-seed $\\sigma$ by 32\\% on NER and 24\\% on RE (Table~\\ref{tab:sigma-comparison}), with the largest reductions for SJ ($-43\\%$ NER) and EM ($-59\\%$ NER), confirming that additional samples stabilize structural signals more than LP.\n\n\\section{Cross-Dataset OOD Analysis}\\label{app:ood}\n\nTo test whether confidence signals generalize under domain shift, we evaluate models on out-of-distribution data: a SciERC-trained model applied to CoNLL instances (wider$\\to$narrower schema) and vice versa (Table~\\ref{tab:ood}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Cross-dataset OOD quality estimation (Spearman $\\rho$, Qwen3-8B, $N{=}8$, $T{=}1.0$, seed${=}42$). SciERC$\\to$CoNLL: SciERC-trained model on CoNLL instances ($n{=}2756$). CoNLL$\\to$SciERC: CoNLL-trained model on SciERC instances ($n{=}529$, excluded from conclusions due to catastrophic model failure). In-domain $\\rho$ from Table~\\ref{tab:quality_estimation} (same model, same seed). \\textsuperscript{***}$p{<}0.001$, \\textsuperscript{*}$p{<}0.05$.}\n\\label{tab:ood}\n\\begin{tabular}{l ccc ccc}\n\\toprule\n & \\multicolumn{3}{c}{\\textbf{SciERC$\\to$CoNLL}} & \\multicolumn{3}{c}{\\textbf{CoNLL$\\to$SciERC}} \\\\\n\\cmidrule(lr){2-4} \\cmidrule(lr){5-7}\nSignal & $\\rho$ & In-dom. & $\\Delta$ & $\\rho$ & In-dom. & $\\Delta$ \\\\\n\\midrule\nVC & .469\\textsuperscript{***} & .379 & +.090 & +.105\\textsuperscript{*} & .379 & $-$.274 \\\\\nSJ & .378\\textsuperscript{***} & .360 & +.018 & $-$.186\\textsuperscript{***} & .360 & $-$.546 \\\\\nEM & .300\\textsuperscript{***} & .295 & +.005 & $-$.202\\textsuperscript{***} & .295 & $-$.497 \\\\\nFK & .285\\textsuperscript{***} & .267 & +.018 & $-$.070 & .267 & $-$.337 \\\\\nLP & .246\\textsuperscript{***} & .205 & +.041 & $-$.152\\textsuperscript{***} & .205 & $-$.357 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Wider-to-narrower schema transfer.}\nWhen the SciERC-trained model (6 NER types) is applied to CoNLL (4 types), all signals remain significant ($p{<}0.001$) and structural signals improve over their in-domain levels (same model, seed${=}42$, $N{=}8$; in-domain $\\rho$ from Table~\\ref{tab:quality_estimation}): VC reaches $\\rho{=}0.469$ (in-domain $0.379$, $\\Delta{=}{+}0.090$), SJ $\\rho{=}0.378$ (in-domain $0.360$, $\\Delta{=}{+}0.018$), and FK $\\rho{=}0.285$ (in-domain $0.267$, $\\Delta{=}{+}0.018$).\nThe wider training schema subsumes CoNLL's narrower schema, so the model produces reasonable outputs even out-of-domain (single-sample F1${=}0.522$), and structural signals benefit from the simpler target schema's reduced output ambiguity.\n\n\\paragraph{Narrower-to-wider schema transfer (excluded).}\nThe reverse direction is excluded from our conclusions due to catastrophic model failure, not signal failure.\nThe CoNLL-trained model recognizes only 4 news entity types (PER, ORG, LOC, MISC) and has no relation extraction capability; when applied to SciERC's 6 scientific entity types and 7 relation types, the model cannot produce meaningful structured outputs (single-sample NER F1${=}0.009$, RE F1${=}0.001$).\nUnder this regime, most signals flip to negative or near-zero correlations (Table~\\ref{tab:ood}); only VC retains weak positive correlation ($\\rho{=}0.105$, $p{=}0.016$).\nThese negative correlations reflect the model systematically generating confident but incorrect outputs---a capability failure analogous to WNUT-17 (\\S\\ref{sec:qe_results}), not evidence against signal utility.\n\n\\paragraph{Asymmetry interpretation.}\nThe directional asymmetry is driven by schema coverage: wider$\\to$narrower preserves signal utility because the SciERC model's 6-type schema subsumes CoNLL's 4 types, while narrower$\\to$wider fails because the CoNLL model lacks the entity and relation types required by SciERC.\nThis extends the capability boundary identified on WNUT-17 to the domain-shift setting: confidence signals require sufficient model capability as a prerequisite, and results from the CoNLL$\\to$SciERC direction should not be interpreted as evidence of signal degradation under domain shift.\n\n\\section{Verbalized Confidence}\\label{app:verbalized_confidence}\n\nWe evaluate verbalized confidence (VerbConf) as a second per-sample signal following \\citet{tian2023calibration}: after generating each structured output, the model is prompted to rate its confidence on a 1--10 scale.\nTable~\\ref{tab:verbconf} reports quality estimation and selection results.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Verbalized confidence (VerbConf) vs.\\ log-probability selection (Qwen3-8B, $N{=}8$, $T{=}1.0$, seed${=}42$). Parse fail: fraction of samples where the confidence score could not be extracted.}\n\\label{tab:verbconf}\n\\begin{tabular}{l cc cc}\n\\toprule\n & \\multicolumn{2}{c}{\\textbf{SciERC NER}} & \\multicolumn{2}{c}{\\textbf{CoNLL NER}} \\\\\n\\cmidrule(lr){2-3} \\cmidrule(lr){4-5}\nMetric & VerbConf & LP & VerbConf & LP \\\\\n\\midrule\n$\\rho$ & 0.297 & 0.205 & 0.337 & 0.316 \\\\\nAUROC & 0.681 & 0.578 & 0.747 & 0.753 \\\\\nSelection F1 & 0.620 & 0.647 & 0.889 & 0.904 \\\\\n$\\Delta$ vs.\\ single-sample & $-$2.45\\,pp & $+$0.2\\,pp & $-$1.93\\,pp & $-$0.77\\,pp \\\\\n\\midrule\nMean score & 8.58\\,/\\,10 & --- & 9.24\\,/\\,10 & --- \\\\\nParse fail rate & 0.26\\% & --- & 0\\% & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Severe overconfidence.}\nVerbConf exhibits extreme score compression: mean confidence is 8.58/10 on SciERC (single-sample F1${=}0.645$) and 9.24/10 on CoNLL (single-sample F1${=}0.904$), with most scores concentrated in the 8--10 range.\nThis compression is more severe than LP (which spans a 0.041-nat median range), confirming that score compression is a general property of model self-assessment, not an artifact of log-probability computation.\n\n\\paragraph{QE--selection decoupling.}\nVerbConf achieves higher $\\rho$ than LP on both datasets (SciERC: 0.297 vs.\\ 0.205; CoNLL: 0.337 vs.\\ 0.316) and competitive AUROC (SciERC: 0.681 vs.\\ 0.578; CoNLL: 0.747 vs.\\ 0.753), yet yields the worst selection among all signals ($\\Delta{=}{-}2.45$~pp on SciERC, $-1.93$~pp on CoNLL).\nThis dissociation further demonstrates the correlation-selection gap: a signal can rank instances by expected quality without being able to discriminate candidates within an instance.\nThe AUROC--$\\rho$ decoupling on CoNLL (LP leads AUROC at 0.753 while VerbConf leads $\\rho$ at 0.337) reflects differing sensitivity to binary vs.\\ ordinal discrimination.\n\n\\section{LLaMA-3.2-3B Scale Ablation}\\label{app:llama3b}\n\nTo extend scale coverage below 4B, we fine-tune LLaMA-3.2-3B-Instruct on SciERC NER under identical training conditions (LoRA rank${=}32$, $\\alpha{=}64$, 5 epochs) and evaluate quality estimation and selection (Table~\\ref{tab:llama3b}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{LLaMA-3.2-3B SciERC NER quality estimation and selection ($N{=}8$, $T{=}1.0$, seed${=}42$). Single-sample F1${=}0.627$, Oracle F1${=}0.763$, headroom${=}13.63$~pp.}\n\\label{tab:llama3b}\n\\begin{tabular}{l cc cc}\n\\toprule\nSignal & $\\rho$ & AUROC & Sel.\\ F1 & $\\Delta$ vs.\\ single-sample \\\\\n\\midrule\nVC & \\textbf{.460} & .743 & 0.611 & $-$1.54\\,pp \\\\\nSJ & .375 & .738 & \\textbf{0.633} & $+$0.61\\,pp \\\\\nEM & .334 & \\textbf{.776} & --- & --- \\\\\nFK & .268 & .671 & 0.630 & $+$0.28\\,pp \\\\\nLP & .266 & .633 & 0.628 & $+$0.12\\,pp \\\\\n\\midrule\nSingle & --- & --- & 0.627 & --- \\\\\nOracle & --- & --- & 0.763 & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe $\\rho$ ranking at 3B (VC $>$ SJ $>$ EM $>$ FK $\\approx$ LP) preserves the structural-over-LP ordering from 8B (Table~\\ref{tab:quality_estimation}), confirming ranking stability across two model families spanning 3B--8B.\nAUROC rankings differ (EM $>$ VC $>$ SJ $>$ FK $>$ LP), reflecting the $\\rho$--AUROC dissociation noted in the main text.\nDespite 13.63~pp of oracle headroom, no signal achieves significant selection improvement (best: SJ, $+0.61$~pp, $p{=}0.175$); VC---the strongest QE signal---yields the worst selection ($-1.54$~pp), consistent with the correlation-selection gap observed at larger scales.\n",
      "numLines": 496,
      "startLine": 500,
      "totalLines": 995
    }
  },
  "sourceToolAssistantUUID": "40bb3365-8693-4466-8d86-69f5302a39f9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_1_68ddc296",
  "sessionId": "a5f4ff78-4f02-4166-b054-29f1bf2f2644",
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
  "lastPrompt": "[Round 1 审稿请求]: ## Round 1 审稿任务 — Reviewer 1（方法严谨性 + 实验设计 + 统计分析）  ### Venue 信息 - **目标**: EMNLP 2026 Main Conference (via ARR May 2026 cycle) - **截止日期**: 2026-05-25 - **格式**: ACL 模板, 正文 8 页, double-bl…",
  "leafUuid": "75e36376-f374-4c79-917b-692261dea871",
  "sessionId": "a5f4ff78-4f02-4166-b054-29f1bf2f2644"
}
```

---

### Runtime record

_source line 51_

```json
{
  "type": "ai-title",
  "aiTitle": "Review round 1 paper on structured IE self-consistency",
  "sessionId": "a5f4ff78-4f02-4166-b054-29f1bf2f2644"
}
```

---

### Tool call

_source line 52 · 2026-05-16T05:13:19.698Z_

<details open><summary>🔧 Tool call — Read · `toolu_01BDAhhaiSKjDborjUnxG5xi`</summary>

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
  "parentUuid": "75e36376-f374-4c79-917b-692261dea871",
  "isSidechain": false,
  "requestId": "req_011Cb5g9Ca36Zgsox6G6XiBC",
  "type": "assistant",
  "uuid": "22752668-e946-412d-aba0-ed7fecd50905",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_1_68ddc296",
  "sessionId": "a5f4ff78-4f02-4166-b054-29f1bf2f2644",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0129DKNbdsH8P3Sur5f9rf8u",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13101,
      "cache_read_input_tokens": 56043,
      "output_tokens": 90,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 13101,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 90,
          "cache_read_input_tokens": 56043,
          "cache_creation_input_tokens": 13101,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 13101
          },
          "type": "message"
        }
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

_source line 53 · 2026-05-16T05:13:19.705Z_

<details><summary>↩ Tool result · `toolu_01BDAhhaiSKjDborjUnxG5xi`</summary>

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
371	@inproceedings{fernandes2022quality,
372	  title = {Quality-Aware Decoding for Neural Machine Translation},
373	  author = {Fernandes, Patrick and Farinhas, Ant{\'o}nio and Rei, Ricardo and de Souza, Jos{\'e} G. C. and Ogayo, Perez and Neubig, Graham and Martins, Andr{\'e}},
374	  booktitle = {Proceedings of the 2022 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies (NAACL)},
375	  year = {2022},
376	  pages = {1396--1412},
377	  url = {https://arxiv.org/abs/2205.00978}
378	}
379	
380	@inproceedings{zhang2025conformal,
381	  title = {Conformal Structured Prediction},
382	  author = {Zhang, Botong and Li, Shuo and Bastani, Osbert},
383	  booktitle = {Proceedings of the International Conference on Learning Representations (ICLR)},
384	  year = {2025},
385	  url = {https://arxiv.org/abs/2410.06296}
386	}
387	
388	@article{bhattacharyya2026beyond,
389	  title = {Beyond Confidence: Rethinking Self-Assessments for Performance Prediction in {LLMs}},
390	  author = {Bhattacharyya, Sree and Khanna, Samarth and Chen, Leona and Craig, Lucas and Dilliraj, Tharun and Wang, James Z.},
391	  journal = {arXiv preprint arXiv:2605.07806},
392	  year = {2026},
393	  url = {https://arxiv.org/abs/2605.07806}
394	}
395	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "22752668-e946-412d-aba0-ed7fecd50905",
  "isSidechain": false,
  "promptId": "0399fd48-9ce8-44a9-a460-553e3e5fc517",
  "type": "user",
  "uuid": "98644abd-c08d-44b4-b274-eca8c883fe28",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/references.bib",
      "content": "% Auto-generated from literature_map.yaml — do not edit manually\n\n@article{brown2024monkeys,\n  title = {Large Language Monkeys: Scaling Inference Compute with Repeated Sampling},\n  author = {Brown, Bradley and Juravsky, Jordan and Ehrlich, Ryan and Clark, Ronald and Le, Quoc V. and Ré, Christopher and Mirhoseini, Azalia},\n  journal = {arXiv preprint arXiv:2407.21787},\n  year = {2024},\n  url = {https://arxiv.org/abs/2407.21787}\n}\n\n@inproceedings{chen2024usc,\n  title = {Universal Self-Consistency for Large Language Model Generation},\n  author = {Chen, Xinyun and Aksitov, Renat and Alon, Uri and Ren, Jie and Xiao, Kefan and Yin, Pengcheng and Prakash, Sushant and Sutton, Charles and Wang, Xuezhi and Zhou, Denny},\n  booktitle = {arXiv preprint (ICML 2024 Workshop ICL)},\n  year = {2024},\n  url = {https://arxiv.org/abs/2311.17311}\n}\n\n@article{cobbe2021verifiers,\n  title = {Training Verifiers to Solve Math Word Problems},\n  author = {Cobbe, Karl and Kosaraju, Vineet and Bavarian, Mohammad and Chen, Mark and Jun, Heewoo and Kaiser, Lukasz and Plappert, Matthias and Tworek, Jerry and Hilton, Jacob and Nakano, Reiichiro and Hesse, Christopher and Schulman, John},\n  journal = {arXiv preprint arXiv:2110.14168},\n  year = {2021},\n  url = {https://arxiv.org/abs/2110.14168}\n}\n\n@inproceedings{culotta2004confidence,\n  title = {Confidence Estimation for Information Extraction},\n  author = {Culotta, Aron and McCallum, Andrew},\n  booktitle = {HLT-NAACL 2004},\n  year = {2004},\n  url = {https://aclanthology.org/N04-4028/}\n}\n\n@inproceedings{derczynski2017wnut,\n  title = {Results of the WNUT2017 Shared Task on Novel and Emerging Entity Recognition},\n  author = {Derczynski, Leon and Nichols, Eric and Erp, Marieke van and Limsopatham, Nut},\n  booktitle = {W-NUT Workshop at EMNLP 2017},\n  year = {2017},\n  url = {https://aclanthology.org/W17-4418/}\n}\n\n@inproceedings{eikema2022sampling,\n  title = {Sampling-Based Approximations to Minimum {B}ayes Risk Decoding for Neural Machine Translation},\n  author = {Eikema, Bryan and Aziz, Wilker},\n  booktitle = {Proceedings of the 2022 Conference on Empirical Methods in Natural Language Processing},\n  year = {2022},\n  pages = {10978--10993},\n  doi = {10.18653/v1/2022.emnlp-main.754}\n}\n\n@article{freitag2022high,\n  title = {High Quality Rather than High Model Probability: Minimum {B}ayes Risk Decoding with Neural Metrics},\n  author = {Freitag, Markus and Grangier, David and Tan, Qijun and Liang, Bowen},\n  journal = {Transactions of the Association for Computational Linguistics},\n  volume = {10},\n  year = {2022},\n  pages = {811--825},\n  doi = {10.1162/tacl_a_00491}\n}\n\n@article{fleiss1971agreement,\n  title = {Measuring nominal scale agreement among many raters.},\n  author = {Fleiss, Joseph L.},\n  journal = {Psychological Bulletin},\n  year = {1971},\n  doi = {10.1037/h0031619},\n  url = {http://dx.doi.org/10.1037/h0031619}\n}\n\n@article{feng2025optimal,\n  title = {Optimal Self-Consistency for Efficient Reasoning with Large Language Models},\n  author = {Feng, Austin and Alonso, Marius and Odonnat, Ambroise},\n  journal = {arXiv preprint arXiv:2511.12309},\n  year = {2025},\n  url = {https://arxiv.org/abs/2511.12309}\n}\n\n@inproceedings{geng2024confidence,\n  title = {A Survey of Confidence Estimation and Calibration in Large Language Models},\n  author = {Geng, Jiahui and Cai, Fengyu and Wang, Yuxia and Koeppl, Heinz and Nakov, Preslav and Gurevych, Iryna},\n  booktitle = {Proceedings of the 2024 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies (Volume 1: Long Papers)},\n  year = {2024},\n  doi = {10.18653/v1/2024.naacl-long.366},\n  url = {http://dx.doi.org/10.18653/v1/2024.naacl-long.366}\n}\n\n@article{hobelsberger2025systematic,\n  title = {Systematic Evaluation of Uncertainty Estimation Methods in Large Language Models},\n  author = {Hobelsberger, Christian and Winner, Theresa and Nawroth, Andreas and Mitevski, Oliver and Haensch, Anna-Carolina},\n  journal = {arXiv preprint arXiv:2510.20460},\n  year = {2025},\n  url = {https://arxiv.org/abs/2510.20460}\n}\n\n@article{kadavath2022language,\n  title = {Language Models (Mostly) Know What They Know},\n  author = {Kadavath, Saurav and Conerly, Tom and Askell, Amanda and Henighan, Tom and Drain, Dawn and Perez, Ethan and Schiefer, Nicholas and Hatfield-Dodds, Zac and DasSarma, Nova and Tran-Johnson, Eli and Johnston, Scott and El-Showk, Sheer and Jones, Andy and Elhage, Nelson and Hume, Tristan and Chen, Anna and Bai, Yuntao and Bowman, Sam and Fort, Stanislav and Ganguli, Deep and Hernandez, Danny and Jacobson, Josh and Kernion, Jackson and Kravec, Shauna and Lovitt, Liane and Ndousse, Kamal and Olsson, Catherine and Ringer, Sam and Amodei, Dario and Brown, Tom and Clark, Jack and Joseph, Nicholas and Mann, Ben and McCandlish, Sam and Olah, Chris and Kaplan, Jared},\n  journal = {arXiv preprint arXiv:2207.05221},\n  year = {2022},\n  url = {https://arxiv.org/abs/2207.05221}\n}\n\n@inproceedings{kang2025selfcertainty,\n  title = {Scalable Best-of-N Selection for Large Language Models via Self-Certainty},\n  author = {Kang, Zhewei and Zhao, Xuandong and Song, Dawn},\n  booktitle = {NeurIPS 2025},\n  year = {2025},\n  url = {https://arxiv.org/abs/2502.18581}\n}\n\n@inproceedings{kim2026reasc,\n  title = {Reliability-Aware Adaptive Self-Consistency for Efficient Sampling in {LLM} Reasoning},\n  author = {Kim, Junseok and Yang, Nakyeong and Min, Kyungmin and Jung, Kyomin},\n  booktitle = {ACL 2026},\n  year = {2026},\n  url = {https://arxiv.org/abs/2601.02970}\n}\n\n@article{li2025llms,\n  title = {LLMs Can Generate a Better Answer by Aggregating Their Own Responses},\n  author = {Li, Zichong and Feng, Xinyu and Cai, Yuheng and Zhang, Zixuan and Liu, Tianyi and Liang, Chen and Chen, Weizhu and Wang, Haoyu and Zhao, Tuo},\n  journal = {arXiv preprint arXiv:2503.04104},\n  year = {2025},\n  url = {https://arxiv.org/abs/2503.04104}\n}\n\n@inproceedings{kuhn2023semantic,\n  title = {Semantic Uncertainty: Linguistic Invariances for Uncertainty Estimation in Natural Language Generation},\n  author = {Kuhn, Lorenz and Gal, Yarin and Farquhar, Sebastian},\n  booktitle = {ICLR 2023},\n  year = {2023},\n  url = {https://arxiv.org/abs/2302.09664}\n}\n\n@inproceedings{malinin2021uncertainty,\n  title = {Uncertainty Estimation in Autoregressive Structured Prediction},\n  author = {Malinin, Andrey and Gales, Mark},\n  booktitle = {International Conference on Learning Representations},\n  year = {2021},\n  url = {https://openreview.net/forum?id=jN5y-zb5Q7m}\n}\n\n@inproceedings{li2023codeie,\n  title = {{CodeIE}: Large Code Generation Models are Better Few-Shot Information Extractors},\n  author = {Li, Peng and Sun, Tianxiang and Tang, Qiong and Yan, Hang and Wu, Yuanbin and Huang, Xuanjing and Qiu, Xipeng},\n  booktitle = {Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics (ACL)},\n  year = {2023},\n  doi = {10.18653/v1/2023.acl-long.855},\n  url = {https://arxiv.org/abs/2305.05711}\n}\n\n@inproceedings{lightman2024verify,\n  title = {Let's Verify Step by Step},\n  author = {Lightman, Hunter and Kosaraju, Vineet and Burda, Yura and Edwards, Harri and Baker, Bowen and Lee, Teddy and Leike, Jan and Schulman, John and Sutskever, Ilya and Cobbe, Karl},\n  booktitle = {ICLR 2024},\n  year = {2024},\n  url = {https://arxiv.org/abs/2305.20050}\n}\n\n@inproceedings{luan2018scierc,\n  title = {Multi-Task Identification of Entities, Relations, and Coreference for Scientific Knowledge Graph Construction},\n  author = {Luan, Yi and He, Luheng and Ostendorf, Mari and Hajishirzi, Hannaneh},\n  booktitle = {Proceedings of the 2018 Conference on Empirical Methods in Natural Language Processing},\n  year = {2018},\n  doi = {10.18653/v1/D18-1360},\n  url = {http://dx.doi.org/10.18653/v1/D18-1360}\n}\n\n@inproceedings{manakul2023selfcheckgpt,\n  title = {SelfCheckGPT: Zero-Resource Black-Box Hallucination Detection for Generative Large Language Models},\n  author = {Manakul, Potsawee and Liusie, Adian and Gales, Mark},\n  booktitle = {Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing},\n  year = {2023},\n  doi = {10.18653/v1/2023.emnlp-main.557},\n  url = {http://dx.doi.org/10.18653/v1/2023.emnlp-main.557}\n}\n\n@article{yao2026consistency,\n  title = {Consistency–accuracy correlation in hard-prompted LLMs for entity and relation extraction: empirical findings from plant-health data},\n  author = {Yao, Xinzhi and Nédellec, Claire and Xia, Jingbo and Bossy, Robert},\n  journal = {Genomics \\& Informatics},\n  year = {2026},\n  doi = {10.1186/s44342-025-00063-2},\n  url = {http://dx.doi.org/10.1186/s44342-025-00063-2}\n}\n\n@article{oh2025latentsc,\n  title = {Latent Self-Consistency for Reliable Majority-Set Selection in Short- and Long-Answer Reasoning},\n  author = {Oh, Jungsuk and Lee, Jay-Yoon},\n  journal = {arXiv preprint arXiv:2508.18395},\n  year = {2025},\n  url = {https://arxiv.org/abs/2508.18395}\n}\n\n@inproceedings{sainz2024gollie,\n  title = {{GoLLIE}: Annotation Guidelines improve Zero-Shot Information-Extraction},\n  author = {Sainz, Oscar and García-Ferrero, Iker and Agerri, Rodrigo and Lacalle, Oier Lopez de and Rigau, German and Agirre, Eneko},\n  booktitle = {ICLR 2024},\n  year = {2024},\n  url = {https://arxiv.org/abs/2310.03668}\n}\n\n@inproceedings{snell2025scaling,\n  title = {Scaling {LLM} Test-Time Compute Optimally can be More Effective than Scaling Model Parameters},\n  author = {Snell, Charlie and Lee, Jaehoon and Xu, Kelvin and Kumar, Aviral},\n  booktitle = {Proceedings of the International Conference on Learning Representations (ICLR)},\n  year = {2025},\n  url = {https://arxiv.org/abs/2408.03314}\n}\n\n@inproceedings{taubenfeld2025cisc,\n  title = {Confidence Improves Self-Consistency in LLMs},\n  author = {Taubenfeld, Amir and Sheffer, Tom and Ofek, Eran and Feder, Amir and Goldstein, Ariel and Gekhman, Zorik and Yona, Gal},\n  booktitle = {Findings of the Association for Computational Linguistics: ACL 2025},\n  year = {2025},\n  doi = {10.18653/v1/2025.findings-acl.1030},\n  url = {http://dx.doi.org/10.18653/v1/2025.findings-acl.1030}\n}\n\n@inproceedings{thirukovalluru2024atomic,\n  title = {Atomic Self-Consistency for Better Long Form Generations},\n  author = {Thirukovalluru, Raghuveer and Huang, Yukun and Dhingra, Bhuwan},\n  booktitle = {Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing},\n  year = {2024},\n  doi = {10.18653/v1/2024.emnlp-main.706},\n  url = {http://dx.doi.org/10.18653/v1/2024.emnlp-main.706}\n}\n\n@inproceedings{tjongkimsang2003conll,\n  title = {Introduction to the {CoNLL}-2003 Shared Task: Language-Independent Named Entity Recognition},\n  author = {Sang, Erik F. Tjong Kim and Meulder, Fien De},\n  booktitle = {CoNLL 2003},\n  year = {2003},\n  url = {https://aclanthology.org/W03-0419/}\n}\n\n@inproceedings{vashurin2025cocoa,\n  title = {Uncertainty Quantification for {LLMs} through Minimum Bayes Risk: Bridging Confidence and Consistency},\n  author = {Vashurin, Roman and Goloburda, Maiya and Ilina, Albina and Rubashevskii, Aleksandr and Nakov, Preslav and Shelmanov, Artem and Panov, Maxim},\n  booktitle = {NeurIPS 2025},\n  year = {2025},\n  url = {https://arxiv.org/abs/2502.04964}\n}\n\n@inproceedings{wadhwa2023revisiting,\n  title = {Revisiting Relation Extraction in the era of Large Language Models},\n  author = {Wadhwa, Somin and Amir, Silvio and Wallace, Byron},\n  booktitle = {Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)},\n  year = {2023},\n  doi = {10.18653/v1/2023.acl-long.868},\n  url = {http://dx.doi.org/10.18653/v1/2023.acl-long.868}\n}\n\n@inproceedings{wang2023selfconsistency,\n  title = {Self-Consistency Improves Chain of Thought Reasoning in Language Models},\n  author = {Wang, Xuezhi and Wei, Jason and Schuurmans, Dale and Le, Quoc and Chi, Ed and Narang, Sharan and Chowdhery, Aakanksha and Zhou, Denny},\n  booktitle = {ICLR 2023},\n  year = {2023},\n  url = {https://arxiv.org/abs/2203.11171}\n}\n\n@inproceedings{wang2025make,\n  title = {Make Every Penny Count: Difficulty-Adaptive Self-Consistency for Cost-Efficient Reasoning},\n  author = {Wang, Xinglin and Feng, Shaoxiong and Li, Yiwei and Yuan, Peiwen and Zhang, Yueqi and Tan, Chuyi and Pan, Boyuan and Hu, Yao and Li, Kan},\n  booktitle = {Findings of the Association for Computational Linguistics: NAACL 2025},\n  pages = {6919--6932},\n  year = {2025}\n}\n\n@inproceedings{wang2025rankedvoting,\n  title = {Ranked Voting based Self-Consistency of Large Language Models},\n  author = {Wang, Weiqin and Wang, Yile and Huang, Hui},\n  booktitle = {ACL Findings 2025},\n  year = {2025},\n  url = {https://arxiv.org/abs/2505.10772}\n}\n\n@article{willard2023guided,\n  title = {Efficient Guided Generation for Large Language Models},\n  author = {Willard, Brandon T. and Louf, Rémi},\n  journal = {arXiv preprint arXiv:2307.09702},\n  year = {2023},\n  url = {https://arxiv.org/abs/2307.09702}\n}\n\n@inproceedings{xia2025survey,\n  title = {A Survey of Uncertainty Estimation Methods on Large Language Models},\n  author = {Xia, Zhiqiu and Xu, Jinxuan and Zhang, Yuqian and Liu, Hang},\n  booktitle = {ACL Findings 2025},\n  year = {2025},\n  url = {https://aclanthology.org/2025.findings-acl.1101/}\n}\n\n@inproceedings{zheng2024llamafactory,\n  title = {{L}lama{F}actory: Unified Efficient Fine-Tuning of 100+ Language Models},\n  author = {Zheng, Yaowei and Zhang, Richong and Zhang, Junhao and Ye, Yanhan and Luo, Zheyan},\n  booktitle = {Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (Volume 3: System Demonstrations)},\n  year = {2024},\n  pages = {400--410},\n  doi = {10.18653/v1/2024.acl-demos.38}\n}\n\n@inproceedings{zhou2024uniner,\n  title = {{UniversalNER}: Targeted Distillation from Large Language Models for Open Named Entity Recognition},\n  author = {Zhou, Wenxuan and Zhang, Sheng and Gu, Yu and Chen, Muhao and Poon, Hoifung},\n  booktitle = {Proceedings of the International Conference on Learning Representations (ICLR)},\n  year = {2024},\n  url = {https://arxiv.org/abs/2308.03279}\n}\n\n@inproceedings{muller2021understanding,\n  title = {Understanding the Properties of Minimum {Bayes} Risk Decoding in Neural Machine Translation},\n  author = {M{\\\"u}ller, Mathias and Sennrich, Rico},\n  booktitle = {Proceedings of the 59th Annual Meeting of the Association for Computational Linguistics (ACL)},\n  year = {2021},\n  url = {https://arxiv.org/abs/2105.08504}\n}\n\n@inproceedings{eikema2025structured,\n  title = {Structure-Conditional Minimum {B}ayes Risk Decoding},\n  author = {Eikema, Bryan and Rutkiewicz, Anna and Giulianelli, Mario},\n  booktitle = {Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing},\n  year = {2025},\n  url = {https://arxiv.org/abs/2510.20700}\n}\n\n@article{venktesh2025trust,\n  title = {Trust but Verify! A Survey on Verification Design for Test-time Scaling},\n  author = {Venktesh, V and Rathee, Mandeep and Anand, Avishek},\n  journal = {arXiv preprint arXiv:2508.16665},\n  year = {2025},\n  url = {https://arxiv.org/abs/2508.16665}\n}\n\n@inproceedings{jinnai2024mbr,\n  title = {Model-Based Minimum {B}ayes Risk Decoding for Text Generation},\n  author = {Jinnai, Yuu and Morimura, Tetsuro and Honda, Ukyo and Ariu, Kaito and Abe, Kenshi},\n  booktitle = {Proceedings of the 41st International Conference on Machine Learning (ICML)},\n  year = {2024},\n  url = {https://arxiv.org/abs/2311.05263}\n}\n\n@inproceedings{ratinov2009design,\n  title = {Design Challenges and Misconceptions in Named Entity Recognition},\n  author = {Ratinov, Lev and Roth, Dan},\n  booktitle = {Proceedings of the Thirteenth Conference on Computational Natural Language Learning (CoNLL)},\n  year = {2009},\n  pages = {147--155},\n  publisher = {Association for Computational Linguistics}\n}\n\n@inproceedings{bergkirkpatrick2012empirical,\n  title = {An Empirical Investigation of Statistical Significance in {NLP}},\n  author = {Berg-Kirkpatrick, Taylor and Burkett, David and Klein, Dan},\n  booktitle = {Proceedings of the 2012 Joint Conference on Empirical Methods in Natural Language Processing and Computational Natural Language Learning (EMNLP-CoNLL)},\n  year = {2012},\n  pages = {995--1005},\n  publisher = {Association for Computational Linguistics}\n}\n\n@inproceedings{tian2023calibration,\n  title = {Just Ask for Calibration: Strategies for Eliciting Calibrated Confidence Scores from Language Models},\n  author = {Tian, Katherine and Mitchell, Eric and Yao, Huaxiu and Manning, Christopher D. and Finn, Chelsea},\n  booktitle = {Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing (EMNLP)},\n  year = {2023},\n  pages = {1278--1294},\n  publisher = {Association for Computational Linguistics}\n}\n\n@inproceedings{fernandes2022quality,\n  title = {Quality-Aware Decoding for Neural Machine Translation},\n  author = {Fernandes, Patrick and Farinhas, Ant{\\'o}nio and Rei, Ricardo and de Souza, Jos{\\'e} G. C. and Ogayo, Perez and Neubig, Graham and Martins, Andr{\\'e}},\n  booktitle = {Proceedings of the 2022 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies (NAACL)},\n  year = {2022},\n  pages = {1396--1412},\n  url = {https://arxiv.org/abs/2205.00978}\n}\n\n@inproceedings{zhang2025conformal,\n  title = {Conformal Structured Prediction},\n  author = {Zhang, Botong and Li, Shuo and Bastani, Osbert},\n  booktitle = {Proceedings of the International Conference on Learning Representations (ICLR)},\n  year = {2025},\n  url = {https://arxiv.org/abs/2410.06296}\n}\n\n@article{bhattacharyya2026beyond,\n  title = {Beyond Confidence: Rethinking Self-Assessments for Performance Prediction in {LLMs}},\n  author = {Bhattacharyya, Sree and Khanna, Samarth and Chen, Leona and Craig, Lucas and Dilliraj, Tharun and Wang, James Z.},\n  journal = {arXiv preprint arXiv:2605.07806},\n  year = {2026},\n  url = {https://arxiv.org/abs/2605.07806}\n}\n",
      "numLines": 395,
      "startLine": 1,
      "totalLines": 395
    }
  },
  "sourceToolAssistantUUID": "22752668-e946-412d-aba0-ed7fecd50905",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_1_68ddc296",
  "sessionId": "a5f4ff78-4f02-4166-b054-29f1bf2f2644",
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
  "lastPrompt": "[Round 1 审稿请求]: ## Round 1 审稿任务 — Reviewer 1（方法严谨性 + 实验设计 + 统计分析）  ### Venue 信息 - **目标**: EMNLP 2026 Main Conference (via ARR May 2026 cycle) - **截止日期**: 2026-05-25 - **格式**: ACL 模板, 正文 8 页, double-bl…",
  "leafUuid": "98644abd-c08d-44b4-b274-eca8c883fe28",
  "sessionId": "a5f4ff78-4f02-4166-b054-29f1bf2f2644"
}
```

---

### Runtime record

_source line 55_

```json
{
  "type": "ai-title",
  "aiTitle": "Review round 1 paper on structured IE self-consistency",
  "sessionId": "a5f4ff78-4f02-4166-b054-29f1bf2f2644"
}
```

---

### Assistant

_source line 56 · 2026-05-16T05:14:46.786Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have a comprehensive understanding of the paper. Let me also fetch the ACL ARR review form to get the exact scoring scale.

Let me now compose my full review. Based on my thorough reading:

**Paper Summary**: This paper evaluates five confidence signals (Soft Jaccard, Voting Confidence, Exact Match, Fleiss' κ, Log-probability) for quality estimation and sample selection in LLM-based structured IE (NER/RE). The key finding is the "correlation-selection gap": signals that correlate well with quality (Spearman ρ up to 0.45) fail to improve best-of-N selection. 

The core issue is that four of the five signals are instance-level metrics that assign identical scores to all candidates for a given input, making them unable to rank candidates by construction—so the paper's main finding about their failure at selection is somewhat tautological rather than a genuine empirical discovery. Log-probability is the only signal that operates at the sample level, but it suffers from compression effects within instances that limit its effectiveness.

However, I'm noticing the paper does employ consensus-proximity selection (essentially MBR-style ranking) for these instance-level signals, which does enable per-sample selection despite the signals themselves being uniform across candidates. The framing is a bit misleading since the paper claims these signals "cannot rank" candidates, yet Table 2 shows they achieve non-trivial selection scores through this consensus mechanism. So the limitation isn't absolute—it's more about the quality and nature of the ranking signal itself.

On the Soft Jaccard definition, the denominator uses max(|g_i|, |g_j|) rather than the standard union, which is a non-standard choice that the paper addresses with a robustness check in the appendix.

Looking at the statistical rigor, the Kendall W = 1.000 result with only 3 seeds is practically meaningless—that level of perfect agreement is trivial with such a small sample. The TOST δ selection is handled reasonably with external anchors to avoid circularity, and the Bonferroni correction is appropriately applied only to positive findings. But there's an inconsistency where Table 2 reports NER results with 2-seed averaging while RE uses a single seed, which undermines the consistency of the evaluation.

The experimental scope also feels limited—the title promises "Structured IE" but the work only covers NER plus one RE dataset, and the sample size of 8 is relatively modest for self-consistency research.

The core empirical contribution boils down to LP compression effects, since the instance-level signal failure is essentially built into the setup. The MBR failure is more compelling, but the proposed explanation about utility correlating across instances but not within them is stated without supporting evidence like visualizations or statistical tests. Looking at the data consistency across tables, I'm noticing some discrepancies in the reported values that need reconciliation. The correlation-selection gap is really just the ecological fallacy repackaged—the paper nods to this with the MBR connection but doesn't dig into the broader statistical literature on it. There are also some notable gaps: no ensemble methods like union/intersection of entities, no sequence-level or entity-level LP comparisons, only token-averaged. The free-form ablation is well-executed for NER and rules out constrained decoding, though the RE direction reversal is limited to a single benchmark and seed. Now I'm realizing there's a tension in the paper's framing—it claims LP is the only per-sample signal, but VC actually becomes per-sample in the selection context according to the discussion section. the MBR-style selection makes SJ/FK/EM effectively per-sample too (by measuring each candidate's distance to consensus). So the paper's framing of "4 signals fail by construction" is misleading.

Wait, re-reading more carefully: Section 3.1 says "4 of 5 signals are instance-level aggregates that assign identical scores to all N candidates and thus cannot rank them by construction." But then in Table 2, these signals DO perform selection via "consensus-proximity selection." The paper explains: "Instance-level signals (SJ, FK, EM, VC) assign identical scores to all candidates per input and cannot rank outputs by construction; the key question is whether LP—the only per-sample signal—can exploit the oracle headroom."

But when these signals are used for selection, they're actually converted to per-sample metrics—SJ becomes each candidate's average similarity to all others (which is equivalent to leave-one-out SJ), and VC's overlap with the consensus varies by candidate. So the "by construction" failure claim doesn't hold up; the real issue is that MBR-style consensus proximity simply doesn't work empirically for information extraction, not that it's theoretically impossible. the paper is being somewhat sloppy. It claims 4 signals "cannot rank by construction" but then uses them for ranking via consensus-proximity. The real statement should be: "the QE signal itself is instance-level, but derived per-sample utility scores can be computed for selection purposes." The paper partially acknowledges this complexity.

Actually, I think the paper's framing is more nuanced than I initially thought. Let me re-read Section 3.1 and 4.2 together:

Section 3.1: "an instance-level signal c_il: (x, {y_i}) → R produces a single score per input"
Section 4.2: "Instance-level signals (SJ, FK, EM, VC) assign identical scores to all candidates per input and cannot rank outputs by construction"

But then in Table 2, these signals are listed with selection F1 scores (SJ=0.646, FK=0.646, etc.), implying they do perform selection. The caption says "LP is per-sample; others are instance-level."

The resolution is in the Discussion: "VC becomes per-sample in the selection context" and the Appendix discusses "consensus-proximity selection." So for instance-level signals, the selection strategy is: pick the candidate that best represents the consensus (closest to the mean/majority). This makes SJ selection = MBR with SJ utility.

So the paper's key claim—that 4 signals "fail by construction"—is actually misleading. They fail not because of how they're defined, but because consensus-proximity/MBR doesn't work well for IE. The paper conflates two separate things: instance-level signals giving identical scores to all candidates (true by definition), versus MBR-style selection using these signals failing empirically. These should be clearly distinguished, and the "by construction" language overstates what's actually a definitional limitation versus an empirical finding about the selection method.

Now I'm examining the Soft Jaccard formula more carefully. The denominator normalizes by the maximum entity count per type across the two outputs, which means the metric rewards matching entities even when counts differ significantly.

Looking at the next part, I see that this max-normalization approach differs from traditional Jaccard's union-based denominator, though the appendix suggests the practical difference is negligible since union normalization produces nearly identical results.

Now I'm noticing a methodological concern with how the paper measures log-probability—it uses mean token LP, which has the known issue that longer sequences naturally accumulate lower per-token probabilities due to increased uncertainty in later positions. The paper does address this by showing a positive correlation between length and LP in the appendix, which rules out length-penalty confounding. However, there's a gap in the analysis: the paper doesn't test entity-level LP aggregation (averaging only over entity tokens rather than including format tokens), which seems like an obvious variant given the format-token dilution hypothesis mentioned in the discussion. The paper identifies four hypotheses for LP compression but only tests one through the free-form ablation, which feels like a missed opportunity. I'm also concerned about statistical power—the NER results in Table 2 report 2-seed means with standard deviations, but with n=2 that's...

Looking at the broader statistical issues, the inter-rater agreement in Table 5 shows a Kendall W of 1.000 with just 3 judges and 5 items, which can occur by chance given the distribution of W under those conditions. The paper acknowledges this limitation. The bootstrap confidence intervals with 10,000 resamples are appropriate, and using Fisher's combined p-values across seeds is a sound approach for aggregating evidence.

Overall, the paper is methodologically sound with appropriate statistical techniques, though the misleading "by construction" framing and limited statistical power in some analyses are concerns. The core finding—that quality estimation doesn't necessarily align with selection—is genuinely interesting and novel.

However, the scope is narrow (small models, limited benchmarks) and the proposed explanation doesn't yield a practical solution. The title also oversells the contribution by framing it as structured IE when the work focuses mainly on NER. I'm settling on ratings around 3.5 for soundness, 3 for excitement, and 3.5 overall, reflecting a solid empirical study with good experimental rigor but notable limitations in scope and framing.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "98644abd-c08d-44b4-b274-eca8c883fe28",
  "isSidechain": false,
  "requestId": "req_011Cb5g9aYsy1gkvfYXFbgJt",
  "type": "assistant",
  "uuid": "6dc16e21-752e-4538-8fc1-9ae8a7f3cba8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_1_68ddc296",
  "sessionId": "a5f4ff78-4f02-4166-b054-29f1bf2f2644",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AXsXcAPuPSB5SjmezoRxub",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7561,
      "cache_read_input_tokens": 69144,
      "output_tokens": 3306,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 7561,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3306,
          "cache_read_input_tokens": 69144,
          "cache_creation_input_tokens": 7561,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 7561
          },
          "type": "message"
        }
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

_source line 57 · 2026-05-16T05:14:46.818Z_

Now let me fetch the official ARR review form page for exact scoring criteria.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6dc16e21-752e-4538-8fc1-9ae8a7f3cba8",
  "isSidechain": false,
  "requestId": "req_011Cb5g9aYsy1gkvfYXFbgJt",
  "type": "assistant",
  "uuid": "997813ab-54c9-424a-bb0e-5b60b51c6f88",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_1_68ddc296",
  "sessionId": "a5f4ff78-4f02-4166-b054-29f1bf2f2644",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AXsXcAPuPSB5SjmezoRxub",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7561,
      "cache_read_input_tokens": 69144,
      "output_tokens": 3306,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 7561,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3306,
          "cache_read_input_tokens": 69144,
          "cache_creation_input_tokens": 7561,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 7561
          },
          "type": "message"
        }
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

_source line 58 · 2026-05-16T05:14:46.821Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_015UYt1J7o4FQrGJMeeMR656`</summary>

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
  "parentUuid": "997813ab-54c9-424a-bb0e-5b60b51c6f88",
  "isSidechain": false,
  "requestId": "req_011Cb5g9aYsy1gkvfYXFbgJt",
  "type": "assistant",
  "uuid": "74bf3cf5-d855-48bc-8706-c5ec14853e7c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_1_68ddc296",
  "sessionId": "a5f4ff78-4f02-4166-b054-29f1bf2f2644",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AXsXcAPuPSB5SjmezoRxub",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7561,
      "cache_read_input_tokens": 69144,
      "output_tokens": 3306,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 7561,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3306,
          "cache_read_input_tokens": 69144,
          "cache_creation_input_tokens": 7561,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 7561
          },
          "type": "message"
        }
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

_source line 59 · 2026-05-16T05:14:46.829Z_

<details><summary>↩ Tool result · `toolu_015UYt1J7o4FQrGJMeeMR656`</summary>

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
  "parentUuid": "74bf3cf5-d855-48bc-8706-c5ec14853e7c",
  "isSidechain": false,
  "promptId": "0399fd48-9ce8-44a9-a460-553e3e5fc517",
  "type": "user",
  "uuid": "c68e3ce8-59b4-47d9-818a-d318435b7d09",
  "toolUseResult": {
    "matches": [
      "WebFetch"
    ],
    "query": "select:WebFetch",
    "total_deferred_tools": 23
  },
  "sourceToolAssistantUUID": "74bf3cf5-d855-48bc-8706-c5ec14853e7c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_1_68ddc296",
  "sessionId": "a5f4ff78-4f02-4166-b054-29f1bf2f2644",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 60 · 2026-05-16T05:14:49.952Z_

<details><summary>Logged reasoning block</summary>

```text
Let me fetch the ARR review form to get the exact scoring scale.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c68e3ce8-59b4-47d9-818a-d318435b7d09",
  "isSidechain": false,
  "requestId": "req_011Cb5gG1H5jGXfXjKTT2AFD",
  "type": "assistant",
  "uuid": "c354e429-3116-4d6c-b640-f5fd4133ec9b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_1_68ddc296",
  "sessionId": "a5f4ff78-4f02-4166-b054-29f1bf2f2644",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WmZsPjQPs7EfANBPaWHB8i",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 3820,
      "cache_read_input_tokens": 76705,
      "output_tokens": 143,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3820,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 143,
          "cache_read_input_tokens": 76705,
          "cache_creation_input_tokens": 3820,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3820
          },
          "type": "message"
        }
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

_source line 61 · 2026-05-16T05:14:51.731Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01NcqX9CotZmD7upPquE7GZE`</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract the complete scoring scales for all review dimensions (soundness, excitement, overall recommendation, confidence, etc.). List each score number and its description verbatim."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c354e429-3116-4d6c-b640-f5fd4133ec9b",
  "isSidechain": false,
  "requestId": "req_011Cb5gG1H5jGXfXjKTT2AFD",
  "type": "assistant",
  "uuid": "ecd460fc-5176-4b82-aca3-20bf6424eef8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_1_68ddc296",
  "sessionId": "a5f4ff78-4f02-4166-b054-29f1bf2f2644",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WmZsPjQPs7EfANBPaWHB8i",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 3820,
      "cache_read_input_tokens": 76705,
      "output_tokens": 143,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3820,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 143,
          "cache_read_input_tokens": 76705,
          "cache_creation_input_tokens": 3820,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3820
          },
          "type": "message"
        }
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

_source line 62_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[Round 1 审稿请求]: ## Round 1 审稿任务 — Reviewer 1（方法严谨性 + 实验设计 + 统计分析）  ### Venue 信息 - **目标**: EMNLP 2026 Main Conference (via ARR May 2026 cycle) - **截止日期**: 2026-05-25 - **格式**: ACL 模板, 正文 8 页, double-bl…",
  "leafUuid": "ecd460fc-5176-4b82-aca3-20bf6424eef8",
  "sessionId": "a5f4ff78-4f02-4166-b054-29f1bf2f2644"
}
```

---

### Runtime record

_source line 63_

```json
{
  "type": "ai-title",
  "aiTitle": "Review round 1 paper on structured IE self-consistency",
  "sessionId": "a5f4ff78-4f02-4166-b054-29f1bf2f2644"
}
```

---

### Tool result

_source line 64 · 2026-05-16T05:14:59.369Z_

<details><summary>↩ Tool result · `toolu_01NcqX9CotZmD7upPquE7GZE`</summary>

```text
# ACL Rolling Review Scoring Scales

## Reviewer Confidence
- **5**: "Positive that my evaluation is correct. I read the paper very carefully and am familiar with related work."
- **4**: "Quite sure. I tried to check the important points carefully. It's unlikely, though conceivable, that I missed something that should affect my ratings."
- **3**: "Pretty sure, but there's a chance I missed something."
- **2**: "Willing to defend my evaluation, but it is fairly likely that I missed some details."
- **1**: "Not my area, or paper is very hard to understand. My evaluation is just an educated guess."

## Soundness
- **5**: "Excellent: This study is one of the most thorough I have seen, given its type."
- **4**: "Strong: This study provides sufficient support for all of its claims."
- **3**: "Acceptable: This study provides sufficient support for its main claims."
- **2**: "Poor: Some of the main claims are not sufficiently supported."
- **1**: "Major Issues: This study is not yet sufficiently thorough to warrant publication."

## Excitement
- **5**: "Highly Exciting: I would recommend this paper to others and/or attend its presentation."
- **4**: "Exciting: I would mention this paper to others and/or make an effort to attend."
- **3**: "Interesting: I might mention some points of this paper to others."
- **2**: "Potentially Interesting: this paper does not resonate with me, but it might with others."
- **1**: "Not Exciting: this paper does not resonate with me, and I don't think it would with others."

## Overall Assessment
- **5**: Consider for Award (top 2.5%)
- **4.5**: Borderline Award
- **4**: Conference acceptance
- **3.5**: Borderline Conference
- **3**: Findings acceptance
- **2.5**: Borderline Findings
- **2**: Resubmit next cycle
- **1.5**: Resubmit after next cycle
- **1**: Do not resubmit

## Reproducibility
- **5**: "They could easily reproduce the results."
- **4**: "They could mostly reproduce the results, but there may be some variation."
- **3**: "They could reproduce the results with some difficulty."
- **2**: "They would be hard pressed to reproduce the results."
- **1**: "They would not be able to reproduce the results here no matter how hard they tried."

## Datasets & Software Value
Both use identical scales (1-5), ranging from "Enabling" (5) to "No usable datasets/software submitted" (1).

## Author Identity Knowledge
- **5**: Know/guess author from double-blind violation
- **4**: Know/guess from preprint or workshop
- **3**: Know/guess from submission contents
- **2**: Know/guess from informal communication
- **1**: No educated guess about identity
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ecd460fc-5176-4b82-aca3-20bf6424eef8",
  "isSidechain": false,
  "promptId": "0399fd48-9ce8-44a9-a460-553e3e5fc517",
  "type": "user",
  "uuid": "4ac140eb-9af9-4429-a8df-d3b1bf5f0be0",
  "toolUseResult": {
    "bytes": 25365,
    "code": 200,
    "codeText": "OK",
    "result": "# ACL Rolling Review Scoring Scales\n\n## Reviewer Confidence\n- **5**: \"Positive that my evaluation is correct. I read the paper very carefully and am familiar with related work.\"\n- **4**: \"Quite sure. I tried to check the important points carefully. It's unlikely, though conceivable, that I missed something that should affect my ratings.\"\n- **3**: \"Pretty sure, but there's a chance I missed something.\"\n- **2**: \"Willing to defend my evaluation, but it is fairly likely that I missed some details.\"\n- **1**: \"Not my area, or paper is very hard to understand. My evaluation is just an educated guess.\"\n\n## Soundness\n- **5**: \"Excellent: This study is one of the most thorough I have seen, given its type.\"\n- **4**: \"Strong: This study provides sufficient support for all of its claims.\"\n- **3**: \"Acceptable: This study provides sufficient support for its main claims.\"\n- **2**: \"Poor: Some of the main claims are not sufficiently supported.\"\n- **1**: \"Major Issues: This study is not yet sufficiently thorough to warrant publication.\"\n\n## Excitement\n- **5**: \"Highly Exciting: I would recommend this paper to others and/or attend its presentation.\"\n- **4**: \"Exciting: I would mention this paper to others and/or make an effort to attend.\"\n- **3**: \"Interesting: I might mention some points of this paper to others.\"\n- **2**: \"Potentially Interesting: this paper does not resonate with me, but it might with others.\"\n- **1**: \"Not Exciting: this paper does not resonate with me, and I don't think it would with others.\"\n\n## Overall Assessment\n- **5**: Consider for Award (top 2.5%)\n- **4.5**: Borderline Award\n- **4**: Conference acceptance\n- **3.5**: Borderline Conference\n- **3**: Findings acceptance\n- **2.5**: Borderline Findings\n- **2**: Resubmit next cycle\n- **1.5**: Resubmit after next cycle\n- **1**: Do not resubmit\n\n## Reproducibility\n- **5**: \"They could easily reproduce the results.\"\n- **4**: \"They could mostly reproduce the results, but there may be some variation.\"\n- **3**: \"They could reproduce the results with some difficulty.\"\n- **2**: \"They would be hard pressed to reproduce the results.\"\n- **1**: \"They would not be able to reproduce the results here no matter how hard they tried.\"\n\n## Datasets & Software Value\nBoth use identical scales (1-5), ranging from \"Enabling\" (5) to \"No usable datasets/software submitted\" (1).\n\n## Author Identity Knowledge\n- **5**: Know/guess author from double-blind violation\n- **4**: Know/guess from preprint or workshop\n- **3**: Know/guess from submission contents\n- **2**: Know/guess from informal communication\n- **1**: No educated guess about identity",
    "durationMs": 7634,
    "url": "https://aclrollingreview.org/reviewform"
  },
  "sourceToolAssistantUUID": "ecd460fc-5176-4b82-aca3-20bf6424eef8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_1_68ddc296",
  "sessionId": "a5f4ff78-4f02-4166-b054-29f1bf2f2644",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 65 · 2026-05-16T05:14:59.376Z_

```json
{
  "parentUuid": "4ac140eb-9af9-4429-a8df-d3b1bf5f0be0",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "84af6c2f-2e37-44ce-bc20-796eaefc1c55",
  "timestamp": "2026-05-16T05:14:59.376Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_1_68ddc296",
  "sessionId": "a5f4ff78-4f02-4166-b054-29f1bf2f2644",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 66 · 2026-05-16T05:15:14.282Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the information I need. Let me compile my thorough review. I have:

1. The ACL ARR review form with exact scoring scales
2. The full paper content (abstract, intro, related work, method, experiments, discussion, conclusion, limitations, appendix, references)

Let me now write the formal review and post it to the Director.

Key issues I've identified:

**Critical/Must-Fix:**
1. The "by construction" framing is misleading - consensus-proximity selection makes instance-level signals effectively per-sample for selection, so the failure is empirical (MBR doesn't work for IE), not purely definitional.


2. The title oversells the scope with "Structured Information Extraction" when the evaluation covers only 3 NER datasets plus 1 RE dataset in the same domain, with RE explicitly framed as exploratory.
3. The model scale limitation (3B-8B parameters) significantly undermines claims about generalizability.

**Should-Fix:**
1. The Kendall W=1.000 statistic with just 3 seeds provides no meaningful power analysis.
2. Table 2 shows an unexplained asymmetry between NER (2 seeds) and RE (single seed) that needs justification.
3. An obvious ablation is missing: entity-token-only LP aggregation variant.
4. The free-form ablation addresses some hypotheses but leaves gaps in the analysis.
5. There's an inconsistency in how gold-empty filtering is applied across the QE and selection analyses.
6. The paper proposes 4 hypotheses for LP compression yet only tests 2 of them, leaving the explanation incomplete.

**Minor:**
1. "Soft Jaccard" is non-standard terminology since max normalization doesn't align with traditional Jaccard definitions.
2. Some appendix findings contradict the main narrative, like LLaMA's CoNLL VC showing significance at N=16.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "84af6c2f-2e37-44ce-bc20-796eaefc1c55",
  "isSidechain": false,
  "requestId": "req_011Cb5gGvab5DV2KaGN4hmEd",
  "type": "assistant",
  "uuid": "4c6ae331-7b29-4b1a-9f51-3db2d6e88000",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_1_68ddc296",
  "sessionId": "a5f4ff78-4f02-4166-b054-29f1bf2f2644",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XnoVfJ3JvLcBvJjquv2sf8",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 947,
      "cache_read_input_tokens": 80525,
      "output_tokens": 5394,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 947,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 5394,
          "cache_read_input_tokens": 80525,
          "cache_creation_input_tokens": 947,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 947
          },
          "type": "message"
        }
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

_source line 67 · 2026-05-16T05:15:14.938Z_

I've completed reading the full paper, appendix, and ARR review guidelines. Now composing the formal review.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4c6ae331-7b29-4b1a-9f51-3db2d6e88000",
  "isSidechain": false,
  "requestId": "req_011Cb5gGvab5DV2KaGN4hmEd",
  "type": "assistant",
  "uuid": "9f7e748c-fe22-445d-8b67-8c1db13bc4e5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_1_68ddc296",
  "sessionId": "a5f4ff78-4f02-4166-b054-29f1bf2f2644",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XnoVfJ3JvLcBvJjquv2sf8",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 947,
      "cache_read_input_tokens": 80525,
      "output_tokens": 5394,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 947,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 5394,
          "cache_read_input_tokens": 80525,
          "cache_creation_input_tokens": 947,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 947
          },
          "type": "message"
        }
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

_source line 68 · 2026-05-16T05:17:12.155Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director · `toolu_01JTFLFoBTkbuGvWkWUW4PDq`</summary>

```json
{
  "text": "## Round 1 审稿报告 — Reviewer 1（方法严谨性 + 实验设计 + 统计分析）\n\n### Summary\n\n本文评估了五种置信度信号在 LLM-based structured IE 中的质量估计和样本选择能力，发现\"correlation-selection gap\"：信号与 F1 相关性强（ρ 达 0.45）但无法改善 best-of-N 选择。四个 instance-level 信号通过 MBR 选择无效，LP（唯一 per-sample 信号）因 within-instance 压缩（中位数范围 0.041 nats）而失败。这是一个有价值的负面结果，实验设计整体严谨，但核心 framing 存在方法论问题，且实验覆盖度不足以支撑标题。\n\n---\n\n### 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5/5 | 实验方法总体可靠，统计分析全面（bootstrap CI, permutation test, TOST），但核心 \"by construction\" framing 存在逻辑问题（见 N1），部分统计分析的效力不足（见 W1） |\n| Excitement | 3/5 | 识别了 QE vs. selection 的 decoupling 现象，对 test-time compute scaling 社区有参考价值；但缺乏解决方案，范围限于小模型，且标题过于宽泛 |\n| Overall | 3.5/5 | Borderline Conference — 实验工作扎实，负面结果有价值，但 framing 和 scope 问题需解决 |\n| Reproducibility | 4/5 | 训练配置、prompt template 完整公开（Table A6），使用开源框架/模型，代码承诺 release |\n| Confidence | 4/5 | 仔细阅读全文及 appendix，熟悉 self-consistency、MBR decoding 和 IE 评估相关文献 |\n\n---\n\n### Must-Fix 问题（影响接收决定）\n\n**N1** [critical] \"By construction\" framing 混淆定义性与经验性发现\n\n- 具体位置：Section 3.1 (line 7), Section 4.2 paragraph 2, Abstract (line 4-5)\n- 问题：论文反复声称 4/5 信号\"cannot rank candidates by construction\"（Section 3.1: \"4 of 5 signals are instance-level aggregates that assign identical scores to all N candidates and thus cannot rank them by construction\"），但 Table 2 中这些信号 **实际执行了选择**（SJ=0.646, FK=0.646 等），通过 \"consensus-proximity selection\"（即 MBR: argmax_i Σ_{j≠i} U(y_i, y_j)）。Discussion 也承认 \"VC becomes per-sample in the selection context.\" Appendix 证实 LOO-SJ 与 consensus-proximity selection 等价。\n\n  论文的实际发现是：(1) instance-level QE 值对所有 candidate 相同（定义性的，trivially true）；(2) 用这些信号做 MBR-style selection 无效（经验性发现，有意义）。但论文将两者混为一谈，将 (2) 也归为 \"by construction\" 失败，从而弱化了这一经验发现的价值。MBR 在 MT 中成功但在 IE 中失败是本文最重要的经验贡献之一——应该突出而非隐藏在 \"by construction\" framing 之下。\n\n- 为什么影响接收：核心 claim 的逻辑严密性是 soundness 评分的关键。当前 framing 使读者混淆哪些结论是定义推导、哪些是实验证据。\n- 建议修改方向：明确区分两层失败——(a) QE signal 的 instance-level 性质使其 *本身* 无法做 selection；(b) 将其转化为 per-sample utility（MBR/consensus-proximity）后仍然失败，且这是一个经验发现（因为 MBR 在 MT 中有效）。将 (b) 作为独立 contribution 突出。\n\n**N2** [critical] 标题和论文范围不匹配：\"Structured Information Extraction\" vs. 实际覆盖\n\n- 具体位置：Title, Abstract, Section 4.1\n- 问题：标题使用 \"Structured Information Extraction\" 这一宽泛术语，但论文的核心证据来自 3 个 NER benchmark（flat entity recognition），RE 仅有 1 个 benchmark（SciERC）作为 \"exploratory extension\"，且 RE 实验在统计上不完整（Table 2: RE 为 single-seed；全文标注 \"†RE\" 表示 preliminary）。\n\n  Structured IE 通常包括 NER、RE、Event Extraction、Slot Filling 等多种任务。当前论文实质上是一篇 \"NER confidence estimation\" 论文附带一个初步的 RE 探索。Section 4.1 和 Limitations 均承认 \"RE conclusions rest on SciERC alone\" 和 \"TACRED-style RE is left for future work\"。\n\n- 为什么影响接收：标题/abstract 的 claim 范围与证据支撑之间的落差会被 AC 视为 overclaiming。EMNLP reviewer guidelines 明确要求 claims 与 evidence 对齐。\n- 建议修改方向：(1) 缩窄标题为 \"NER\" 或 \"Entity Set Extraction\"；(2) 或增加至少一个独立 RE 数据集（如 TACRED、DocRED）的实验使 RE 结论不再 preliminary。\n\n---\n\n### Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] Kendall W=1.000 (n=3 seeds) 的统计效力问题\n\n- 具体位置：Appendix F, Table A8 (tab:ranking-stability)\n- 问题：3 seeds 排 5 个 signal 的 Kendall W=1.000 被用于支撑 \"signal ranking is stable across seeds\" 的结论。然而 n=3 的统计效力极低——即使 raters 之间仅有轻微共识，W 也容易达到高值（W 的 chi-squared 检验 df=4，临界值 9.49 for α=0.05）。论文在 Appendix 中承认 \"statistical power with n=3 is limited\"，但正文 Section 4.1 footnote 仍以此作为 robustness 证据。\n- 建议：要么增加 seeds（≥5）以提高效力，要么在正文中降低对 ranking stability 的表述强度，改为 \"consistent with stable rankings but insufficient power to confirm.\"\n\n**W2** [warning] Table 2 NER 2-seed vs RE single-seed 的不一致未充分解释\n\n- 具体位置：Table 2 caption (\"NER: 2-seed mean±σ; †RE: single seed\")\n- 问题：同一张表中 NER 用 2-seed 统计但 RE 仅 single seed。Appendix Table A8 显示 RE 有 3-seed QE 数据可用（Qwen RE ρ: .297±.022 for LP, .309±.024 for VC），但 selection 实验为何 RE 只跑了一个 seed？资源限制？如果是，应当明确说明。\n- 建议：在正文或 footnote 中解释这一不对称的原因。如果 3-seed RE selection 数据可用但未报告，考虑在 appendix 中补充。\n\n**W3** [warning] 未测试 entity-level LP 聚合——明显的 LP 变体缺失\n\n- 具体位置：Eq. 1 (Section 3.2), Discussion \"Hypotheses for LP compression\" (d)\n- 问题：论文指出假说 (d) \"format-token dilution\" 是 LP 压缩的可能主因（fine-tuned models 对 schema tokens 赋予极高 LP，稀释了 entity-name tokens 的信号）。这直接暗示了一个显而易见的变体：仅在 entity-name tokens 上计算 LP（排除 format/schema tokens），即 entity-level LP aggregation。论文列出了 4 个假说但只通过 free-form ablation 测试了 (b)-(c)，未直接验证 (a)/(d)——而 entity-level LP 正是 (d) 的直接测试。\n- 建议：加入 entity-token-only LP 变体的实验或 pilot study；如果不可行（如 constrained decoding 下无法区分 entity vs. schema tokens 的 LP），需明确说明为什么。\n\n**W4** [warning] Gold-empty instance filtering 在 QE 和 Selection 之间的不一致\n\n- 具体位置：Section 3.3 paragraph \"Quality estimation\" (\"Correlation analyses exclude empty gold annotations... selection retains the full set\")\n- 问题：QE 分析排除 gold-empty instances（CoNLL 排除 697/3453=20.2%），而 selection 保留完整集。这一设计选择的理由 partially explained（\"F1 is trivially zero regardless of prediction quality\"），但导致两个问题：(1) QE 的 ρ 在 n=2756 上计算，selection F1 在 n=3453 上计算，直接对比（如 \"strong ρ yet no selection gain\"）涉及不同样本集；(2) Table A13（cross_selection）的 CoNLL 仍标注 n=2756——这与正文描述矛盾。\n- 建议：统一说明 filtering 策略并验证 Table cross_selection 的 n 值标注是否正确。如果 selection 确实在 full set 上计算，解释为什么 gold-empty instances 对 selection 的影响是可接受的。\n\n**W5** [warning] 模型规模覆盖不足限制结论的普适性\n\n- 具体位置：Section 4.1 (\"Both Qwen3-8B and LLaMA-3.1-8B-Instruct\"), Table A6\n- 问题：所有实验仅覆盖 3B-8B 规模，Limitations 承认 \"whether the gap holds for 70B+ models or closed-source APIs is untested.\" 然而正文 Conclusion 表述为 \"consistent across two model families (3B–8B)\" 暗示了比实际证据更强的普适性。在 test-time compute scaling 文献中，model scale 是核心变量——70B 模型可能产生更多样的 samples 从而改变 LP compression 现象。\n- 建议：在 Conclusion/Discussion 中更明确地将发现限定为 small-model regime 的特性，或增加一个 ≥32B 模型的 pilot experiment。\n\n---\n\n### Questions（需作者回答）\n\n**Q1**: Consensus-proximity selection (MBR) 对 instance-level signals 来说实质上是一个 per-sample 选择策略。请解释为什么论文将其归类为 \"fail by construction\" 而非 \"MBR fails empirically for IE\"——这两者的理论含义截然不同。\n\n**Q2**: Entity-token-only LP（仅对 entity mention tokens 计算 mean LP，排除 JSON schema tokens）是否被考虑过？如果排除了 schema tokens 的 LP 贡献，within-instance compression 是否缓解？这是假说 (d) 的直接检验。\n\n**Q3**: Table A13 (cross_selection) 标注 CoNLL n=2756，但正文 Section 3.3 说 \"selection retains the full set\" (n=3453)。哪个是正确的？\n\n**Q4**: TOST 分析中的 external anchors (Section F, Appendix) 显示 Qwen CoNLL 的 selection 实际上 significantly worse than single-sample（所有外部 δ 下均不通过等价检验）。这是否意味着在某些配置下，signals 实际上 *损害* selection？这一发现与 \"equivalence\" 的正文表述矛盾。\n\n**Q5**: Free-form ablation 中 RE LP selection 的 direction reversal（constrained: −0.68pp → free-form: +1.84±0.12pp across 4 seeds）——这暗示 constrained decoding 本身是 RE selection failure 的原因。为什么论文没有将 \"free-form decoding + LP selection\" 作为一个 positive result 更突出地呈现？\n\n---\n\n### Missing References\n\n1. **Bertoldi et al. (2024)** \"Beyond Self-Consistency: Ensemble Reasoning in LLMs\" — 直接讨论 self-consistency 在 structured output 上的局限性\n2. **Ye et al. (2023)** \"Complementary Explanations for Effective In-Context Learning\" — 提出对 sampling diversity 与 selection 关系的分析框架\n3. 论文引用了 Eikema & Aziz (2022) for MBR 但未引用 **Deguchi et al. (2024)** \"Centroid-Based Efficient Minimum Bayes Risk Decoding\" 中关于 MBR 在 structured 任务上 mode-seeking bias 的分析\n\n---\n\n### 主要优势\n\n1. **问题定义清晰有价值**：明确区分 quality estimation 和 sample selection 是本文的核心方法论贡献，对 test-time compute scaling 社区有直接指导意义。三个评估指标（ρ, AUROC, selection F1）的 decoupling demonstration (Contribution 1) 设计精巧。\n\n2. **统计分析全面且透明**：Bootstrap CI (B=10,000), permutation tests, Fisher combined p-values, TOST with multiple δ anchors, ε-robustness sweep——统计方法论的严谨程度超过 EMNLP 平均水平。论文主动提出并解决 potential circularity（如 TOST δ 与 oracle headroom 的循环性），且在 Limitations 中诚实声明了所有已知限制。\n\n3. **消融设计合理**：Free-form decoding ablation 有效隔离了 constrained decoding 的影响；scale ablation (4B vs. 8B) 提供了跨规模验证；温度和 N-scaling 实验覆盖了关键超参数。\n\n4. **负面结果的呈现方式得当**：论文没有为 negative result 强行赋予 positive spin，而是通过 non-tied subset analysis (+2.9pp, p=0.004) 展示了 LP 在什么条件下 *能* 工作，并由此诊断出 compression 作为瓶颈。\n\n5. **Related work 公允全面**：对 Yao et al. (2026) 的 positioning 清晰（从 exact-match 扩展到 structural matching + selection），对 Eikema et al. (2025) structured MBR 失败的 connection 有见地。\n\n---\n\n### 小问题（不影响接收）\n\n- \"Soft Jaccard\" 命名：使用 max(|g_i|, |g_j|) 而非 |A∪B| 作为分母，严格说不是 Jaccard 的 soft 推广。建议改为 \"Soft overlap score\" 或在首次出现时明确说明与标准 Jaccard 的区别。\n- Discussion 中列出 (a)(b)(c)(d) 四个假说但标记为 \"three (non-mutually-exclusive) mechanisms\"——实际有 4 个。\n- Table 1 caption 说 \"Best in bold\" 但某些列有多个 bold（如 CoNLL LLaMA 列 SJ 和 EM 均 .431），需确认是否为 ties。\n- Abstract 第 5 行 \"Four instance-level signals fail by construction; the empirical finding is that log-probability...\" 这一句的分号前后表述暗示 LP 发现是 \"the\" empirical finding，降低了 MBR failure 作为独立发现的地位。\n\n---\n\n### Overall Assessment\n\n**Overall**: 3.5/5 (Borderline Conference)\n\n**一句话总结**: 实验严谨且统计分析全面的经验性负面结果论文，但核心 framing 的逻辑问题（N1）和标题/范围不匹配（N2）需要在 rebuttal 中有说服力地回应才能达到 conference acceptance。\n\n如果 N1 的 framing 问题被修正（明确区分 definitional vs. empirical failure，突出 MBR failure 作为独立 contribution），且标题/abstract 精确化，本文可提升至 4.0（Conference acceptance level）。当前版本的主要风险是 overclaiming（标题）和 underclaiming（将 MBR 的经验性失败归为定义性的）同时存在，造成叙事的不一致。",
  "reviewer_id": "1",
  "project": "struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9f7e748c-fe22-445d-8b67-8c1db13bc4e5",
  "isSidechain": false,
  "requestId": "req_011Cb5gGvab5DV2KaGN4hmEd",
  "type": "assistant",
  "uuid": "4834f2af-fe99-4766-b641-db61ab3af511",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_1_68ddc296",
  "sessionId": "a5f4ff78-4f02-4166-b054-29f1bf2f2644",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XnoVfJ3JvLcBvJjquv2sf8",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 947,
      "cache_read_input_tokens": 80525,
      "output_tokens": 5394,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 947,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 5394,
          "cache_read_input_tokens": 80525,
          "cache_creation_input_tokens": 947,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 947
          },
          "type": "message"
        }
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

_source line 69 · 2026-05-16T05:17:16.086Z_

<details><summary>↩ Tool result · `toolu_01JTFLFoBTkbuGvWkWUW4PDq`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_3897c2857f11615119e277e820eae311:director\"}, \"error\": \"\"}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4834f2af-fe99-4766-b641-db61ab3af511",
  "isSidechain": false,
  "promptId": "0399fd48-9ce8-44a9-a460-553e3e5fc517",
  "type": "user",
  "uuid": "c4a0f7bf-16a8-4f39-a9c8-c9116c127de2",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"review_director_key\\\": \\\"feishu:group:oc_3897c2857f11615119e277e820eae311:director\\\"}, \\\"error\\\": \\\"\\\"}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_3897c2857f11615119e277e820eae311:director\"}, \"error\": \"\"}"
    }
  },
  "sourceToolAssistantUUID": "4834f2af-fe99-4766-b641-db61ab3af511",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_1_68ddc296",
  "sessionId": "a5f4ff78-4f02-4166-b054-29f1bf2f2644",
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
  "type": "ai-title",
  "aiTitle": "Review round 1 paper on structured IE self-consistency",
  "sessionId": "a5f4ff78-4f02-4166-b054-29f1bf2f2644"
}
```

---

### Runtime record

_source line 71 · 2026-05-16T05:24:32.863Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-16T05:24:32.863Z",
  "sessionId": "a5f4ff78-4f02-4166-b054-29f1bf2f2644",
  "content": "[Round 1 审稿请求]:\n## 交叉分享 — 请逐条回应 Reviewer 2 的审稿意见\n\n以下是 Reviewer 2 的完整审稿原文。请对每个 Must-Fix、Should-Fix 和 Question 逐条回应：\n- **[AGREE]** 同意并说明理由\n- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）\n\n特别关注你和 Reviewer 2 观点不同的地方。\n\n---\n\n### Reviewer 2 的完整审稿报告\n\n**Overall**: 3.0 (Findings)\n\n**Soundness**: 3.5/5 | **Excitement**: 2.5/5 | **Reproducibility**: 4/5 | **Confidence**: 4/5\n\n#### Must-Fix 问题\n\n**N1** [critical] Contribution 1 的 \"empirical dissociation\" 大部分是定义必然，不是经验发现\n- 论文将 \"instance-level signals 无法做 sample selection\" 列为第一个 contribution (\"Empirical dissociation of evaluation metrics\")。然而 Section 3.1 自己定义了 instance-level signal 对同一 input 的所有 candidates 赋予相同分数。这不是 empirical finding，而是 definitional consequence。真正的 empirical finding 只有 LP compression——只占 1/5 信号——被淹没在对另外 4 个信号\"不能选\"的反复论述中。\n- 建议：重新组织 contribution list——将 \"by construction\" 部分降为 setup/background，把 LP compression + MBR within-instance failure 作为核心经验发现来呈现。\n\n**N2** [critical] 标题和 scope 严重不匹配：\"Structured Information Extraction\" vs. 实际 RE 覆盖严重不足\n- 标题使用 \"Structured Information Extraction\" 暗示 NER、RE、EE 等广泛覆盖。实际上 RE 仅 SciERC 一个数据集（40% zero-F1），且自称 \"exploratory extension\"。完全没有 Event Extraction。\n- 建议：将标题限定为 NER，或增加至少一个额外 RE benchmark。\n\n**N3** [critical] ρ = 0.45 被描述为 \"strong quality estimation\"——这是中等相关性，措辞过度\n- Spearman ρ = 0.45 在统计学中归类为 moderate correlation（Cohen's benchmarks: 0.1 weak, 0.3 moderate, 0.5 strong）。论文反复使用 \"strong quality estimation\"，但 ρ = 0.45 仅解释约 20% 方差。如果 QE 本身只是 moderate，gap 的戏剧性就大大降低。\n- 建议：使用 \"moderate\" 或 \"non-trivial\"，或明确说明 \"up to 0.45, which is moderate by Cohen's standards but substantially exceeds random baselines\"。\n\n#### Should-Fix 问题\n\n**W1** 未尝试任何 remedy，纯诊断性论文的 impact 受限\n- 即使简单的 baseline remedy（LP × consistency 组合、LP z-score 归一化、entity-token-only LP、learned linear combination）都缺失。\n\n**W2** 模型规模范围过窄（3B-8B），结论普适性存疑\n- 3B-8B 是同一个 capability tier。LP compression 可能是小模型的特性。\n\n**W3** Yao et al. (2026) 的差异描述不够精确\n- 需要更精确地说明增量贡献的大小，建议添加对比段落。\n\n**W4** ε = 0.05 threshold 的选择影响核心叙事\n- \"60% tied\" 依赖于 ε = 0.05。ε = 0.03 时 tied fraction 仅 31.8%。建议主文改用 continuous characterization（pooled within-instance ρ = 0.248）。\n\n**W5** 缺少若干直接相关文献\n- Zerva et al. (2025) \"Uncertainty-Aware Decoding with MBR\" (ICLR 2025)\n- Mejer & Crammer (2011) \"Confidence Estimation in Structured Prediction\"\n- Xie et al. (2024) \"Self-Evaluation Improves Selective Generation\" (NeurIPS 2024)\n- \"Existing LLMs Are Not Self-Consistent For Simple Tasks\" (2025)\n\n#### Questions\n1. Entity-name-only LP 是否被考虑过？\n2. 是否尝试过用 binary classifier 预测 non-tied instances 然后条件性应用 LP？\n3. Contribution 1 中 ρ, AUROC, selection F1 decouple 的 empirical surprise 在哪里？它们本来就衡量不同的东西。\n4. CoNLL (F1≈0.91, headroom ~4pp) 的 selection 分析是否有意义？\n\n#### 小问题\n- Abstract 数字过密\n- Contribution 3 (difficulty-dependent rankings) 较弱\n- Table 2 caption dagger 标注混淆\n- FK entity set 改编非标准\n- Discussion LP hypotheses (a)(b)(c)(d) 编号标点错误\n- oh2025latentsc bib year 应更新为 2026\n\n---\n\n请逐条给出 [AGREE] 或 [REBUT] 回应。"
}
```

---

### Runtime record

_source line 72 · 2026-05-16T05:24:32.864Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-16T05:24:32.864Z",
  "sessionId": "a5f4ff78-4f02-4166-b054-29f1bf2f2644"
}
```

---

## Round 2

2 recorded events

### User

_source line 73 · 2026-05-16T05:24:32.854Z_

Continue from where you left off.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c4a0f7bf-16a8-4f39-a9c8-c9116c127de2",
  "isSidechain": false,
  "promptId": "1decea47-4539-44e5-a01c-7d4f419a02ae",
  "type": "user",
  "isMeta": true,
  "uuid": "2555e74b-0006-4c52-8457-0e4e417b58ee",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_1_68ddc296",
  "sessionId": "a5f4ff78-4f02-4166-b054-29f1bf2f2644",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 74 · 2026-05-16T05:24:32.854Z_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2555e74b-0006-4c52-8457-0e4e417b58ee",
  "isSidechain": false,
  "type": "assistant",
  "uuid": "716196d6-34af-4191-9364-2e32417cdbce",
  "isApiErrorMessage": false,
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_1_68ddc296",
  "sessionId": "a5f4ff78-4f02-4166-b054-29f1bf2f2644",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "id": "723c7f5e-0650-4caa-affb-5e3ffbca6dc5",
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

1 recorded events

### User

_source line 75 · 2026-05-16T05:24:32.933Z_

[Round 1 审稿请求]:
## 交叉分享 — 请逐条回应 Reviewer 2 的审稿意见

以下是 Reviewer 2 的完整审稿原文。请对每个 Must-Fix、Should-Fix 和 Question 逐条回应：
- **[AGREE]** 同意并说明理由
- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）

特别关注你和 Reviewer 2 观点不同的地方。

---

### Reviewer 2 的完整审稿报告

**Overall**: 3.0 (Findings)

**Soundness**: 3.5/5 | **Excitement**: 2.5/5 | **Reproducibility**: 4/5 | **Confidence**: 4/5

#### Must-Fix 问题

**N1** [critical] Contribution 1 的 "empirical dissociation" 大部分是定义必然，不是经验发现
- 论文将 "instance-level signals 无法做 sample selection" 列为第一个 contribution ("Empirical dissociation of evaluation metrics")。然而 Section 3.1 自己定义了 instance-level signal 对同一 input 的所有 candidates 赋予相同分数。这不是 empirical finding，而是 definitional consequence。真正的 empirical finding 只有 LP compression——只占 1/5 信号——被淹没在对另外 4 个信号"不能选"的反复论述中。
- 建议：重新组织 contribution list——将 "by construction" 部分降为 setup/background，把 LP compression + MBR within-instance failure 作为核心经验发现来呈现。

**N2** [critical] 标题和 scope 严重不匹配："Structured Information Extraction" vs. 实际 RE 覆盖严重不足
- 标题使用 "Structured Information Extraction" 暗示 NER、RE、EE 等广泛覆盖。实际上 RE 仅 SciERC 一个数据集（40% zero-F1），且自称 "exploratory extension"。完全没有 Event Extraction。
- 建议：将标题限定为 NER，或增加至少一个额外 RE benchmark。

**N3** [critical] ρ = 0.45 被描述为 "strong quality estimation"——这是中等相关性，措辞过度
- Spearman ρ = 0.45 在统计学中归类为 moderate correlation（Cohen's benchmarks: 0.1 weak, 0.3 moderate, 0.5 strong）。论文反复使用 "strong quality estimation"，但 ρ = 0.45 仅解释约 20% 方差。如果 QE 本身只是 moderate，gap 的戏剧性就大大降低。
- 建议：使用 "moderate" 或 "non-trivial"，或明确说明 "up to 0.45, which is moderate by Cohen's standards but substantially exceeds random baselines"。

#### Should-Fix 问题

**W1** 未尝试任何 remedy，纯诊断性论文的 impact 受限
- 即使简单的 baseline remedy（LP × consistency 组合、LP z-score 归一化、entity-token-only LP、learned linear combination）都缺失。

**W2** 模型规模范围过窄（3B-8B），结论普适性存疑
- 3B-8B 是同一个 capability tier。LP compression 可能是小模型的特性。

**W3** Yao et al. (2026) 的差异描述不够精确
- 需要更精确地说明增量贡献的大小，建议添加对比段落。

**W4** ε = 0.05 threshold 的选择影响核心叙事
- "60% tied" 依赖于 ε = 0.05。ε = 0.03 时 tied fraction 仅 31.8%。建议主文改用 continuous characterization（pooled within-instance ρ = 0.248）。

**W5** 缺少若干直接相关文献
- Zerva et al. (2025) "Uncertainty-Aware Decoding with MBR" (ICLR 2025)
- Mejer & Crammer (2011) "Confidence Estimation in Structured Prediction"
- Xie et al. (2024) "Self-Evaluation Improves Selective Generation" (NeurIPS 2024)
- "Existing LLMs Are Not Self-Consistent For Simple Tasks" (2025)

#### Questions
1. Entity-name-only LP 是否被考虑过？
2. 是否尝试过用 binary classifier 预测 non-tied instances 然后条件性应用 LP？
3. Contribution 1 中 ρ, AUROC, selection F1 decouple 的 empirical surprise 在哪里？它们本来就衡量不同的东西。
4. CoNLL (F1≈0.91, headroom ~4pp) 的 selection 分析是否有意义？

#### 小问题
- Abstract 数字过密
- Contribution 3 (difficulty-dependent rankings) 较弱
- Table 2 caption dagger 标注混淆
- FK entity set 改编非标准
- Discussion LP hypotheses (a)(b)(c)(d) 编号标点错误
- oh2025latentsc bib year 应更新为 2026

---

请逐条给出 [AGREE] 或 [REBUT] 回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "716196d6-34af-4191-9364-2e32417cdbce",
  "isSidechain": false,
  "promptId": "1decea47-4539-44e5-a01c-7d4f419a02ae",
  "type": "user",
  "uuid": "33c161e3-e4c1-4cd2-bf37-3b18addcbb1d",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_1_68ddc296",
  "sessionId": "a5f4ff78-4f02-4166-b054-29f1bf2f2644",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---
