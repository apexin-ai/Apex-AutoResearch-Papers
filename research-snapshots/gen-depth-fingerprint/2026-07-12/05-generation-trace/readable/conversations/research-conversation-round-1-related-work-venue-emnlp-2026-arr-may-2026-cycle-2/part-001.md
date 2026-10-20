# Research conversation: [Round 1 审稿请求]: 你负责**新颖性 + 完整性 + Related Work + 格式**。 ## Venue 信息 - **目标**: EMNLP 2026（ARR May 2026 cycle） - **截止日期**: 2 — Part 1 of 3

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text (July export snapshot)** · Conversation logs

[Transcript overview](../research-conversation-round-1-related-work-venue-emnlp-2026-arr-may-2026-cycle-2.md) · [Part 2 →](part-002.md) · [Structured JSON](../../../sessions/59/59fd22fa121392665ccb.json)

## Before a recorded user message

## Before a recorded user message

2 recorded events


### Runtime record

_source line 1 · 2026-05-17T17:19:10.290Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-17T17:19:10.290Z",
  "sessionId": "b64a1fb5-cc00-4ec5-a8b3-b55f8a4cf13d",
  "content": "[Round 1 审稿请求]:\n你负责**新颖性 + 完整性 + Related Work + 格式**。\n\n## Venue 信息\n- **目标**: EMNLP 2026（ARR May 2026 cycle）\n- **截止日期**: 2026-05-25\n- **页数限制**: Long paper 正文 8 页（不含 limitations/ethics/references）\n- **模板**: ACL official style files（`\\usepackage[review]{acl}`）\n- **匿名**: Double-blind\n- **附录**: 允许，参与审稿\n\n## 论文路径\n`/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/main.tex`\n\n## 论文概要\n\"Depth Fingerprinting: Detecting Recursive Generation Depth in LLM Text Chains\"——提出 generation depth classification（gen-0/gen-1/gen-2+），利用 differential depth response（DDR）中 drifting vs stationary features 的互补性，用 7-feature XGBoost ensemble 在 8 个 base model generator 上实现 3-class LOGO F1=0.762。\n\n## 你的审查重点\n\n请严格评估以下方面：\n\n1. **新颖性评估**：\n   - \"Generation depth classification\" 作为 task formulation 的新颖性有多大？是否只是把 binary detection 分得更细？\n   - DDR（differential depth response）是一个 genuine insight 还是一个 trivial observation（递归生成当然会让 entropy 下降）？\n   - 7-feature ensemble 方法本身是否有技术新颖性？还是只是 feature engineering + XGBoost？\n   - 相比 Broken Telephone 和 Markovian Chains 两篇 concurrent work，本文的增量贡献是否足够？\n\n2. **Related Work 完整性**：\n   - 是否遗漏重要相关工作？特别是：\n     - 多轮 LLM 生成的质量衰减研究\n     - Model collapse / self-consuming models 方向的最新进展\n     - 数据污染检测方法\n     - Ordinal classification 文献\n   - 与 concurrent works（Broken Telephone, Markovian Chains）的比较是否公平充分？\n   - 引用数量和覆盖度是否达到 EMNLP 水准？\n\n3. **论文完整性**：\n   - Abstract/Introduction 的 claims 是否都有实验支撑？\n   - 各章节逻辑是否连贯（story line 是否统一）？\n   - Contribution 列表是否准确反映实际贡献（有无 overclaim/underclaim）？\n   - Downstream utility（Contribution 3）的 narrative 定位是否合理——\"detectability does not entail downstream degradation\" 这个 claim 是否 well-motivated？\n   - Limitations 是否充分坦诚？\n\n4. **格式与写作**：\n   - 是否符合 ACL style 格式要求？\n   - 正文是否在 8 页内？\n   - 写作质量（AI 痕迹、dash 使用、-ing phrases、过度分段）\n   - 图表信息密度和清晰度\n   - 引用格式是否统一？\n\n请给出完整审稿意见，包含 Strengths、Weaknesses（逐条编号）、Questions、Minor Issues。"
}
```

---


### Runtime record

_source line 2 · 2026-05-17T17:19:10.293Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-17T17:19:10.293Z",
  "sessionId": "b64a1fb5-cc00-4ec5-a8b3-b55f8a4cf13d"
}
```

---


## Round 1

## Round 1

142 recorded events


### User

_source line 3 · 2026-05-17T17:19:10.323Z_

[Round 1 审稿请求]:
你负责**新颖性 + 完整性 + Related Work + 格式**。

## Venue 信息
- **目标**: EMNLP 2026（ARR May 2026 cycle）
- **截止日期**: 2026-05-25
- **页数限制**: Long paper 正文 8 页（不含 limitations/ethics/references）
- **模板**: ACL official style files（`\usepackage[review]{acl}`）
- **匿名**: Double-blind
- **附录**: 允许，参与审稿

## 论文路径
`/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/main.tex`

## 论文概要
"Depth Fingerprinting: Detecting Recursive Generation Depth in LLM Text Chains"——提出 generation depth classification（gen-0/gen-1/gen-2+），利用 differential depth response（DDR）中 drifting vs stationary features 的互补性，用 7-feature XGBoost ensemble 在 8 个 base model generator 上实现 3-class LOGO F1=0.762。

## 你的审查重点

请严格评估以下方面：

1. **新颖性评估**：
   - "Generation depth classification" 作为 task formulation 的新颖性有多大？是否只是把 binary detection 分得更细？
   - DDR（differential depth response）是一个 genuine insight 还是一个 trivial observation（递归生成当然会让 entropy 下降）？
   - 7-feature ensemble 方法本身是否有技术新颖性？还是只是 feature engineering + XGBoost？
   - 相比 Broken Telephone 和 Markovian Chains 两篇 concurrent work，本文的增量贡献是否足够？

2. **Related Work 完整性**：
   - 是否遗漏重要相关工作？特别是：
     - 多轮 LLM 生成的质量衰减研究
     - Model collapse / self-consuming models 方向的最新进展
     - 数据污染检测方法
     - Ordinal classification 文献
   - 与 concurrent works（Broken Telephone, Markovian Chains）的比较是否公平充分？
   - 引用数量和覆盖度是否达到 EMNLP 水准？

3. **论文完整性**：
   - Abstract/Introduction 的 claims 是否都有实验支撑？
   - 各章节逻辑是否连贯（story line 是否统一）？
   - Contribution 列表是否准确反映实际贡献（有无 overclaim/underclaim）？
   - Downstream utility（Contribution 3）的 narrative 定位是否合理——"detectability does not entail downstream degradation" 这个 claim 是否 well-motivated？
   - Limitations 是否充分坦诚？

4. **格式与写作**：
   - 是否符合 ACL style 格式要求？
   - 正文是否在 8 页内？
   - 写作质量（AI 痕迹、dash 使用、-ing phrases、过度分段）
   - 图表信息密度和清晰度
   - 引用格式是否统一？

请给出完整审稿意见，包含 Strengths、Weaknesses（逐条编号）、Questions、Minor Issues。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "c6349ba0-ce02-4cbb-9474-95572d1cbd3f",
  "type": "user",
  "uuid": "59afecb4-0b21-41a0-831b-e86dcbdf64f6",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/review_reviewer_2_3f564e41",
  "sessionId": "b64a1fb5-cc00-4ec5-a8b3-b55f8a4cf13d",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---


### Runtime record

_source line 4 · 2026-05-17T17:19:10.322Z_

```json
{
  "parentUuid": "59afecb4-0b21-41a0-831b-e86dcbdf64f6",
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
  "uuid": "ea81d633-6c53-4bc9-b0bc-9eab13c9b493",
  "timestamp": "2026-05-17T17:19:10.322Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/review_reviewer_2_3f564e41",
  "sessionId": "b64a1fb5-cc00-4ec5-a8b3-b55f8a4cf13d",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

---


### Runtime record

_source line 5 · 2026-05-17T17:19:10.322Z_

```json
{
  "parentUuid": "ea81d633-6c53-4bc9-b0bc-9eab13c9b493",
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
  "uuid": "2e0713bc-5aa4-4694-b5fe-4af6713256b0",
  "timestamp": "2026-05-17T17:19:10.322Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/review_reviewer_2_3f564e41",
  "sessionId": "b64a1fb5-cc00-4ec5-a8b3-b55f8a4cf13d",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

---


### Runtime record

_source line 6 · 2026-05-17T17:19:10.322Z_

```json
{
  "parentUuid": "2e0713bc-5aa4-4694-b5fe-4af6713256b0",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "f499759c-4c3b-4f1e-a530-dc5350d0f956",
  "timestamp": "2026-05-17T17:19:10.322Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/review_reviewer_2_3f564e41",
  "sessionId": "b64a1fb5-cc00-4ec5-a8b3-b55f8a4cf13d",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

---


### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Review depth fingerprinting paper for EMNLP 2026",
  "sessionId": "b64a1fb5-cc00-4ec5-a8b3-b55f8a4cf13d"
}
```

---


### Assistant

_source line 8 · 2026-05-17T17:19:15.851Z_

<details><summary>Logged reasoning block</summary>

```text
The Review Director has asked me to conduct a Round 1 review of the paper "Depth Fingerprinting: Detecting Recursive Generation Depth in LLM Text Chains" for EMNLP 2026. My focus areas are: novelty, completeness, related work, and formatting.

Let me start by following my session start procedure and then read the paper carefully.

First, I need to:
1. Search for EMNLP 2026 / ACL ARR reviewer guidelines
2. Read the paper PDF/tex files

Let me begin by searching for the reviewer guidelines and reading the paper.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f499759c-4c3b-4f1e-a530-dc5350d0f956",
  "isSidechain": false,
  "requestId": "req_011Cb8XJoAcouMDmfSePDAap",
  "type": "assistant",
  "uuid": "4a554f5e-e714-4244-8af8-373abf45181d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/review_reviewer_2_3f564e41",
  "sessionId": "b64a1fb5-cc00-4ec5-a8b3-b55f8a4cf13d",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Peog1qQ5Wu8pnkB3eJYLiK",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 16407,
      "cache_read_input_tokens": 11841,
      "output_tokens": 298,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 16407,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 298,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 16407,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 16407
          },
          "type": "message"
        }
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

_source line 9 · 2026-05-17T17:19:16.856Z_

我将开始审稿流程：先搜索 ACL ARR 官方评审标准，同时读取论文内容。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4a554f5e-e714-4244-8af8-373abf45181d",
  "isSidechain": false,
  "requestId": "req_011Cb8XJoAcouMDmfSePDAap",
  "type": "assistant",
  "uuid": "e6167c76-ac5d-4e61-b86c-04a098ff32f4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/review_reviewer_2_3f564e41",
  "sessionId": "b64a1fb5-cc00-4ec5-a8b3-b55f8a4cf13d",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Peog1qQ5Wu8pnkB3eJYLiK",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 16407,
      "cache_read_input_tokens": 11841,
      "output_tokens": 298,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 16407,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 298,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 16407,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 16407
          },
          "type": "message"
        }
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

_source line 10 · 2026-05-17T17:19:18.073Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01L2oksHGxtzeLUBtY6UbWHh`</summary>

```json
{
  "query": "select:WebSearch,mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__review_reviewer_post_to_director",
  "max_results": 3
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e6167c76-ac5d-4e61-b86c-04a098ff32f4",
  "isSidechain": false,
  "requestId": "req_011Cb8XJoAcouMDmfSePDAap",
  "type": "assistant",
  "uuid": "22f64ee1-80a3-41a1-926e-278e8dedfe88",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/review_reviewer_2_3f564e41",
  "sessionId": "b64a1fb5-cc00-4ec5-a8b3-b55f8a4cf13d",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Peog1qQ5Wu8pnkB3eJYLiK",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 16407,
      "cache_read_input_tokens": 11841,
      "output_tokens": 298,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 16407,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 298,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 16407,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 16407
          },
          "type": "message"
        }
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

_source line 11 · 2026-05-17T17:19:18.079Z_

<details><summary>↩ Tool result · `toolu_01L2oksHGxtzeLUBtY6UbWHh`</summary>

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
  "tool_name": "mcp__agent-ml-research__pdf_to_images"
}
```

```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__review_reviewer_post_to_director"
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "22f64ee1-80a3-41a1-926e-278e8dedfe88",
  "isSidechain": false,
  "promptId": "c6349ba0-ce02-4cbb-9474-95572d1cbd3f",
  "type": "user",
  "uuid": "00147580-45c1-4ccc-a967-9910b836bdb3",
  "toolUseResult": {
    "matches": [
      "WebSearch",
      "mcp__agent-ml-research__pdf_to_images",
      "mcp__agent-ml-research__review_reviewer_post_to_director"
    ],
    "query": "select:WebSearch,mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__review_reviewer_post_to_director",
    "total_deferred_tools": 23
  },
  "sourceToolAssistantUUID": "22f64ee1-80a3-41a1-926e-278e8dedfe88",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/review_reviewer_2_3f564e41",
  "sessionId": "b64a1fb5-cc00-4ec5-a8b3-b55f8a4cf13d",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---


### Assistant

_source line 12 · 2026-05-17T17:19:24.496Z_

<details><summary>Logged reasoning block</summary>

```text
Good, I have the tools loaded. Now let me:
1. Search for ACL ARR reviewer guidelines
2. Read the paper (main.tex and related files)

Let me do these in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "00147580-45c1-4ccc-a967-9910b836bdb3",
  "isSidechain": false,
  "requestId": "req_011Cb8XKNVpsze55WmKyre4U",
  "type": "assistant",
  "uuid": "b55bb7cf-0a2e-4e5c-97a8-b7969d4fbc3e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/review_reviewer_2_3f564e41",
  "sessionId": "b64a1fb5-cc00-4ec5-a8b3-b55f8a4cf13d",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0168ewozDs19D1jvu7fEMedC",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1462,
      "cache_read_input_tokens": 28248,
      "output_tokens": 201,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1462,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 201,
          "cache_read_input_tokens": 28248,
          "cache_creation_input_tokens": 1462,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1462
          },
          "type": "message"
        }
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

_source line 13 · 2026-05-17T17:19:24.980Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01W97VohwzLTeT3ibt1beuxY`</summary>

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
  "parentUuid": "b55bb7cf-0a2e-4e5c-97a8-b7969d4fbc3e",
  "isSidechain": false,
  "requestId": "req_011Cb8XKNVpsze55WmKyre4U",
  "type": "assistant",
  "uuid": "e4130985-360b-41e6-8320-7c79ab061a5e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/review_reviewer_2_3f564e41",
  "sessionId": "b64a1fb5-cc00-4ec5-a8b3-b55f8a4cf13d",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0168ewozDs19D1jvu7fEMedC",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1462,
      "cache_read_input_tokens": 28248,
      "output_tokens": 201,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1462,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 201,
          "cache_read_input_tokens": 28248,
          "cache_creation_input_tokens": 1462,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1462
          },
          "type": "message"
        }
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

_source line 14 · 2026-05-17T17:19:25.449Z_

<details open><summary>🔧 Tool call — Read · `toolu_01ApscT9N2foNNvzjAW6q5fN`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e4130985-360b-41e6-8320-7c79ab061a5e",
  "isSidechain": false,
  "requestId": "req_011Cb8XKNVpsze55WmKyre4U",
  "type": "assistant",
  "uuid": "7b2417d7-e2ac-4243-be38-f258575fbc1b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/review_reviewer_2_3f564e41",
  "sessionId": "b64a1fb5-cc00-4ec5-a8b3-b55f8a4cf13d",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0168ewozDs19D1jvu7fEMedC",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1462,
      "cache_read_input_tokens": 28248,
      "output_tokens": 201,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1462,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 201,
          "cache_read_input_tokens": 28248,
          "cache_creation_input_tokens": 1462,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1462
          },
          "type": "message"
        }
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

_source line 15 · 2026-05-17T17:19:25.457Z_

<details><summary>↩ Tool result · `toolu_01ApscT9N2foNNvzjAW6q5fN`</summary>

```text
1	% EMNLP 2026 ARR Submission — ACL 2023 Template
2	\documentclass[11pt]{article}
3	\usepackage[review]{acl}
4	\usepackage{times}
5	\usepackage{latexsym}
6	\usepackage{graphicx}
7	\usepackage{booktabs}
8	\usepackage{enumitem}
9	\usepackage{amsmath}
10	\usepackage{lineno}
11	\linenumbers
12	
13	\graphicspath{{../chart/}}
14	
15	\title{Depth Fingerprinting: Detecting Recursive Generation Depth\\in LLM Text Chains}
16	
17	\author{Anonymous}
18	
19	\begin{document}
20	\maketitle
21	
22	\input{abstract}
23	
24	\input{introduction}
25	\input{related_work}
26	\input{method}
27	\input{results}
28	
29	\input{discussion}
30	\input{conclusion}
31	\input{limitations}
32	\input{ethics}
33	
34	\bibliography{references}
35	
36	\appendix
37	
38	\noindent\textbf{Note:} Unless otherwise stated, appendix experiments use the original six-generator subset (Pythia-2.8B/1B, OLMo-2-1B, Qwen3-1.7B/0.6B/8B).
39	Main paper results (\S\ref{sec:results}) use the full eight-generator set (adding Llama-3.2-3B and Mistral-7B-v0.3).
40	
41	\input{appendix_dataset_stats}
42	
43	\section{Length Confound Analysis}
44	\label{app:length}
45	\input{appendix_length}
46	
47	\section{Prompt Type Generalization}
48	\label{app:prompt-type}
49	\input{appendix_prompt_type}
50	
51	\section{Finer-Grained Depth Classification}
52	\label{app:finer-depth}
53	\input{appendix_finer_depth}
54	
55	\section{End-to-End Depth Classification (QLoRA)}
56	\label{app:qlora}
57	\input{appendix_qlora}
58	
59	\section{Leave-One-Feature-Out Analysis}
60	\label{app:lofo}
61	\input{appendix_lofo}
62	
63	\section{Confusion Matrix}
64	\label{app:confusion}
65	\input{appendix_confusion_matrix}
66	
67	\section{Classifier Sensitivity}
68	\label{app:classifier}
69	\input{appendix_classifier}
70	
71	\section{Robustness to Text Perturbation}
72	\label{app:human-edit}
73	\input{appendix_human_edit}
74	
75	\section{Cross-Domain Generalization}
76	\label{app:domain}
77	\input{appendix_domain}
78	
79	\section{Error Analysis of Binary Classification}
80	\label{app:error-analysis}
81	\input{appendix_error_analysis}
82	
83	\section{Downstream Utility}
84	\label{app:downstream}
85	\input{appendix_downstream}
86	
87	\section{Cross-Model Chain Per-Class Detail}
88	\label{app:cross-model-detail}
89	\input{appendix_cross_model_detail}
90	
91	\section{Feature Distribution Analysis}
92	\label{app:feature-distributions}
93	\input{appendix_feature_distributions}
94	
95	\section{Cross-Temperature Transfer}
96	\label{app:cross-temp}
97	\input{appendix_cross_temp}
98	
99	\end{document}
100	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7b2417d7-e2ac-4243-be38-f258575fbc1b",
  "isSidechain": false,
  "promptId": "c6349ba0-ce02-4cbb-9474-95572d1cbd3f",
  "type": "user",
  "uuid": "b36b7139-14ea-482d-b3ec-0e7b214d4981",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/main.tex",
      "content": "% EMNLP 2026 ARR Submission — ACL 2023 Template\n\\documentclass[11pt]{article}\n\\usepackage[review]{acl}\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage{graphicx}\n\\usepackage{booktabs}\n\\usepackage{enumitem}\n\\usepackage{amsmath}\n\\usepackage{lineno}\n\\linenumbers\n\n\\graphicspath{{../chart/}}\n\n\\title{Depth Fingerprinting: Detecting Recursive Generation Depth\\\\in LLM Text Chains}\n\n\\author{Anonymous}\n\n\\begin{document}\n\\maketitle\n\n\\input{abstract}\n\n\\input{introduction}\n\\input{related_work}\n\\input{method}\n\\input{results}\n\n\\input{discussion}\n\\input{conclusion}\n\\input{limitations}\n\\input{ethics}\n\n\\bibliography{references}\n\n\\appendix\n\n\\noindent\\textbf{Note:} Unless otherwise stated, appendix experiments use the original six-generator subset (Pythia-2.8B/1B, OLMo-2-1B, Qwen3-1.7B/0.6B/8B).\nMain paper results (\\S\\ref{sec:results}) use the full eight-generator set (adding Llama-3.2-3B and Mistral-7B-v0.3).\n\n\\input{appendix_dataset_stats}\n\n\\section{Length Confound Analysis}\n\\label{app:length}\n\\input{appendix_length}\n\n\\section{Prompt Type Generalization}\n\\label{app:prompt-type}\n\\input{appendix_prompt_type}\n\n\\section{Finer-Grained Depth Classification}\n\\label{app:finer-depth}\n\\input{appendix_finer_depth}\n\n\\section{End-to-End Depth Classification (QLoRA)}\n\\label{app:qlora}\n\\input{appendix_qlora}\n\n\\section{Leave-One-Feature-Out Analysis}\n\\label{app:lofo}\n\\input{appendix_lofo}\n\n\\section{Confusion Matrix}\n\\label{app:confusion}\n\\input{appendix_confusion_matrix}\n\n\\section{Classifier Sensitivity}\n\\label{app:classifier}\n\\input{appendix_classifier}\n\n\\section{Robustness to Text Perturbation}\n\\label{app:human-edit}\n\\input{appendix_human_edit}\n\n\\section{Cross-Domain Generalization}\n\\label{app:domain}\n\\input{appendix_domain}\n\n\\section{Error Analysis of Binary Classification}\n\\label{app:error-analysis}\n\\input{appendix_error_analysis}\n\n\\section{Downstream Utility}\n\\label{app:downstream}\n\\input{appendix_downstream}\n\n\\section{Cross-Model Chain Per-Class Detail}\n\\label{app:cross-model-detail}\n\\input{appendix_cross_model_detail}\n\n\\section{Feature Distribution Analysis}\n\\label{app:feature-distributions}\n\\input{appendix_feature_distributions}\n\n\\section{Cross-Temperature Transfer}\n\\label{app:cross-temp}\n\\input{appendix_cross_temp}\n\n\\end{document}\n",
      "numLines": 100,
      "startLine": 1,
      "totalLines": 100
    }
  },
  "sourceToolAssistantUUID": "7b2417d7-e2ac-4243-be38-f258575fbc1b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/review_reviewer_2_3f564e41",
  "sessionId": "b64a1fb5-cc00-4ec5-a8b3-b55f8a4cf13d",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---


### Tool result

_source line 16 · 2026-05-17T17:19:32.563Z_

<details><summary>↩ Tool result · `toolu_01W97VohwzLTeT3ibt1beuxY`</summary>

```text
Web search results for query: "ACL ARR 2025 2026 reviewer guidelines review form criteria scoring"

Links: [{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"ACLRollingReview (@ReviewAcl) / X","url":"https://x.com/reviewacl"},{"title":"aclrollingreview/reviewing.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/reviewing.md"}]

Here's a summary of the ACL Rolling Review (ARR) reviewer guidelines for 2025-2026:

## Review Scoring System

Starting with February 2025, ARR reviewers are asked to provide three scores: soundness, excitement, and overall recommendation. The soundness scores must be justified by the text of the review.

## Overall Recommendation Scale

The overall recommendation scale includes: 2 = Resubmit next cycle (substantial revisions that can be completed by the next ARR cycle), 1.5 = Resubmit after next cycle (substantial revisions that cannot be completed by the next ARR cycle), and 1 = Do not resubmit (paper has to be fully redone or is not relevant to the *ACL community, such as work not related to computational processing of language).

## Key Review Form Criteria

The review form includes assessment of:

- Limitations and potential positive and negative societal impacts of the work, with suggestions for improvement if not adequately addressed
- Ethical issues with the paper and the extent to which they have been acknowledged or addressed by the authors
- Reproducibility—whether there is enough information for readers to reproduce the main results or build upon the work

## Reviewer Expectations

ARR reviewers are instructed to write a review as if the paper were being considered for the ACL conference, so low scores may indicate the submission is not a good fit for ACL, even if it may be suitable for other venues.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e4130985-360b-41e6-8320-7c79ab061a5e",
  "isSidechain": false,
  "promptId": "c6349ba0-ce02-4cbb-9474-95572d1cbd3f",
  "type": "user",
  "uuid": "5a5dbc14-1177-45dc-a447-659ec4d7d4be",
  "toolUseResult": {
    "query": "ACL ARR 2025 2026 reviewer guidelines review form criteria scoring",
    "results": [
      {
        "tool_use_id": "srvtoolu_01FfJ7emUknrkuTfPwepyKjB",
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
            "title": "aclrollingreview/cfp.md at main · acl-org/aclrollingreview",
            "url": "https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"
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
      "Here's a summary of the ACL Rolling Review (ARR) reviewer guidelines for 2025-2026:\n\n## Review Scoring System\n\nStarting with February 2025, ARR reviewers are asked to provide three scores: soundness, excitement, and overall recommendation. The soundness scores must be justified by the text of the review.\n\n## Overall Recommendation Scale\n\nThe overall recommendation scale includes: 2 = Resubmit next cycle (substantial revisions that can be completed by the next ARR cycle), 1.5 = Resubmit after next cycle (substantial revisions that cannot be completed by the next ARR cycle), and 1 = Do not resubmit (paper has to be fully redone or is not relevant to the *ACL community, such as work not related to computational processing of language).\n\n## Key Review Form Criteria\n\nThe review form includes assessment of:\n\n- Limitations and potential positive and negative societal impacts of the work, with suggestions for improvement if not adequately addressed\n- Ethical issues with the paper and the extent to which they have been acknowledged or addressed by the authors\n- Reproducibility—whether there is enough information for readers to reproduce the main results or build upon the work\n\n## Reviewer Expectations\n\nARR reviewers are instructed to write a review as if the paper were being considered for the ACL conference, so low scores may indicate the submission is not a good fit for ACL, even if it may be suitable for other venues."
    ],
    "durationSeconds": 7.578271274999999
  },
  "sourceToolAssistantUUID": "e4130985-360b-41e6-8320-7c79ab061a5e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/review_reviewer_2_3f564e41",
  "sessionId": "b64a1fb5-cc00-4ec5-a8b3-b55f8a4cf13d",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---


### Runtime record

_source line 17_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[Round 1 审稿请求]: 你负责**新颖性 + 完整性 + Related Work + 格式**。  ## Venue 信息 - **目标**: EMNLP 2026（ARR May 2026 cycle） - **截止日期**: 2026-05-25 - **页数限制**: Long paper 正文 8 页（不含 limitations/ethics/references） - **模…",
  "leafUuid": "5a5dbc14-1177-45dc-a447-659ec4d7d4be",
  "sessionId": "b64a1fb5-cc00-4ec5-a8b3-b55f8a4cf13d"
}
```

---


### Runtime record

_source line 18_

```json
{
  "type": "ai-title",
  "aiTitle": "Review depth fingerprinting paper for EMNLP 2026",
  "sessionId": "b64a1fb5-cc00-4ec5-a8b3-b55f8a4cf13d"
}
```

---


### Assistant

_source line 19 · 2026-05-17T17:19:36.492Z_

<details><summary>Logged reasoning block</summary>

```text
I need to read the actual paper content - abstract, introduction, related work, method, results, discussion, conclusion, limitations, and ethics sections. Let me also search for the official ARR review form to get the exact scoring dimensions.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5a5dbc14-1177-45dc-a447-659ec4d7d4be",
  "isSidechain": false,
  "requestId": "req_011Cb8XLSEbDP1fjeW6JefBi",
  "type": "assistant",
  "uuid": "762d7d4a-e09b-4fd2-910a-7d6b1424938b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/review_reviewer_2_3f564e41",
  "sessionId": "b64a1fb5-cc00-4ec5-a8b3-b55f8a4cf13d",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01M6zzyEFJAubjv5sPCUpsUd",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1061,
      "cache_creation_input_tokens": 1042,
      "cache_read_input_tokens": 29710,
      "output_tokens": 386,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1042,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1061,
          "output_tokens": 386,
          "cache_read_input_tokens": 29710,
          "cache_creation_input_tokens": 1042,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1042
          },
          "type": "message"
        }
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

_source line 20 · 2026-05-17T17:19:37.441Z_

让我获取 ARR 官方 review form 的详细评分维度，同时读取论文各章节。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "762d7d4a-e09b-4fd2-910a-7d6b1424938b",
  "isSidechain": false,
  "requestId": "req_011Cb8XLSEbDP1fjeW6JefBi",
  "type": "assistant",
  "uuid": "6ba84068-e88e-4a49-9731-4d16d9aadc23",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/review_reviewer_2_3f564e41",
  "sessionId": "b64a1fb5-cc00-4ec5-a8b3-b55f8a4cf13d",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01M6zzyEFJAubjv5sPCUpsUd",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1061,
      "cache_creation_input_tokens": 1042,
      "cache_read_input_tokens": 29710,
      "output_tokens": 386,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1042,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1061,
          "output_tokens": 386,
          "cache_read_input_tokens": 29710,
          "cache_creation_input_tokens": 1042,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1042
          },
          "type": "message"
        }
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

_source line 21 · 2026-05-17T17:19:38.402Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01JK3BQAEdhWWmuWMNbtQXD4`</summary>

```json
{
  "query": "ACL Rolling Review review form soundness excitement scoring scale 1-5 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6ba84068-e88e-4a49-9731-4d16d9aadc23",
  "isSidechain": false,
  "requestId": "req_011Cb8XLSEbDP1fjeW6JefBi",
  "type": "assistant",
  "uuid": "295a1a00-61cb-4026-baf1-1f8e4d9c567e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/review_reviewer_2_3f564e41",
  "sessionId": "b64a1fb5-cc00-4ec5-a8b3-b55f8a4cf13d",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01M6zzyEFJAubjv5sPCUpsUd",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1061,
      "cache_creation_input_tokens": 1042,
      "cache_read_input_tokens": 29710,
      "output_tokens": 386,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1042,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1061,
          "output_tokens": 386,
          "cache_read_input_tokens": 29710,
          "cache_creation_input_tokens": 1042,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1042
          },
          "type": "message"
        }
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

_source line 22 · 2026-05-17T17:19:40.015Z_

<details><summary>↩ Tool result · `toolu_019radH38e5XCYBqUgPCCQ1x`</summary>

```text
1	\section{Related Work}
2	\label{sec:related}
3	
4	\subsection{AI-Generated Text Detection}
5	\label{sec:related-detection}
6	
7	Methods for distinguishing human-written from machine-generated text have evolved from statistical tests \cite{gltr,grover,release_strategies} to zero-shot reference-model approaches \cite{detectgpt,fast_detectgpt,binoculars,dna_gpt} and learned classifiers \cite{ghostbuster,feat_aug_transformer,reliable_detection,ld_score}.
8	Recent work pursues diverse signals including intrinsic dimensionality \cite{intrinsic_dimension}, surprisal diversity \cite{diveye}, and distributional gap measures \cite{generator_barrier}; see \citet{wu_survey_2025} and \citet{jawahar_survey} for surveys.
9	A persistent limitation is that these methods produce binary (real vs.\ synthetic) decisions.
10	Recent multi-class extensions (role recognition in human-LLM collaboration \cite{beyond_binary}, multi-generator attribution \cite{semeval2024_task8}) discriminate among different \emph{sources} rather than recursive generation \emph{depth}.
11	Even when detection scores correlate with depth, they exhibit high cross-generator variance as ordinal predictors (binary F1 from 0.52 to 0.71; Table~\ref{tab:baselines}), because each captures a single distributional property that generalizes inconsistently \cite{paraphrase_evades,detection_possibilities}.
12	Adversarial training approaches (e.g., RADAR \cite{radar}) improve robustness to paraphrasing but remain binary detectors without depth awareness.
13	Our contribution is not a new detection method but the task formulation (generation depth classification, framed within the broader ordinal classification literature \cite{gutierrez_ordinal_survey,coral_ordinal}) and the finding that combining drifting and stationary features yields consistent cross-generator performance.
14	This is orthogonal to source attribution \cite{uchendu_attribution,munir_looking_glass}, which identifies \emph{which} model generated text; our LOGO evaluation decouples generator identity from depth.
15	
16	\subsection{Model Collapse and Iterative Generation}
17	\label{sec:related-collapse}
18	
19	Self-consuming generative models progressively lose distributional coverage \cite{self_consuming_mad}, and model collapse is inevitable without fresh human data \cite{curse_of_recursion}, though careful data mixing can mitigate this \cite{model_collapse_avoidable,strong_model_collapse}.
20	These studies focus on \emph{training-loop} degradation; our setting studies \emph{inference chains}, where a fixed model generates text conditioned on its own prior output without retraining.
21	Iterative self-refinement \cite{self_refine} represents another form of recursive LLM processing, but targets output improvement through feedback loops rather than open-ended continuation; the distributional drift we study arises specifically from unconstrained recursive generation.
22	
23	Two concurrent works are most directly relevant.
24	\citet{broken_telephone} analyze paraphrasing and translation chains, showing progressive information loss.
25	\citet{markovian_chains} demonstrate that semantic-preservation constraints induce attractor dynamics bounding distinguishable depth to approximately three classes; their analysis focuses on characterizing convergence behavior through model-based perplexity tracking.
26	We differ in three respects: (i) we study \emph{non-paraphrastic continuation} chains, where the absence of semantic anchoring permits richer depth signal; (ii) we use handcrafted features rather than model-internal representations, enabling the DDR decomposition into drifting vs.\ stationary components; and (iii) we focus on \emph{estimating} depth from text rather than characterizing the convergence dynamics of the generation process.
27	
28	That both works independently converge on approximately three distinguishable classes reflects different mechanisms reaching the same practical ceiling.
29	\citet{markovian_chains} derive this bound from Markovian attractor dynamics: semantic-preservation constraints create fixed points where successive outputs become indistinguishable under model-internal perplexity.
30	We observe the same bound empirically through feature-space compression: inter-class KS statistics drop sharply after depth 2 (gen-1$\rightarrow$gen-2: KS\,=\,0.28 vs.\ gen-2$\rightarrow$gen-3: KS\,=\,0.09 for entropy mean), collapsing discriminative margins.
31	The approaches are complementary: their theoretical framework explains \emph{why} convergence occurs (attractor dynamics in semantic space), while our DDR decomposition reveals \emph{what} converges (location properties) versus what remains stable (distributional shape), providing an empirical signature that can be exploited for detection without access to model internals.
32	
33	\subsection{Vocabulary Diversity and Stylometry}
34	\label{sec:related-diversity}
35	
36	Declining lexical diversity in LLM-generated text is documented in both training \cite{curious_decline} and deployment \cite{writing_diversity} settings.
37	Our surface features (TTR and hapax ratio) are classical stylometric measures \cite{stamatatos_survey,koppel_authorship} that we apply to inference chains, showing monotonic diversity decline across depths without model retraining.
38	We push beyond generator identity \cite{uchendu_attribution} to the \emph{depth} dimension, and show that diversity declines monotonically even under top-$p$ sampling \cite{nucleus_sampling}.
39	
40	\subsection{Data Quality and Provenance}
41	\label{sec:related-provenance}
42	
43	Scalable data curation relies on quality signals \cite{dsir,qurating,ccnet}; generation depth is a complementary provenance signal characterizing \emph{how many steps removed} text is from a human source.
44	Proactive watermarking \cite{watermark_llm,synthid_text,aaronson_watermark} embeds identifiable patterns, but watermark strength decays across multi-step chains \cite{chainwash}, motivating passive post-hoc methods like ours.
45	At the feature level, our NLL analysis connects to \citet{min_k_percent}, who use the probability tail for membership inference; we analyze the full NLL distribution for generation depth classification.
46	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3df2fb92-ac7b-4e92-924f-b099619e44ef",
  "isSidechain": false,
  "promptId": "c6349ba0-ce02-4cbb-9474-95572d1cbd3f",
  "type": "user",
  "uuid": "74c1465a-95dd-4b3f-82d0-cfed5922f79c",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/related_work.tex",
      "content": "\\section{Related Work}\n\\label{sec:related}\n\n\\subsection{AI-Generated Text Detection}\n\\label{sec:related-detection}\n\nMethods for distinguishing human-written from machine-generated text have evolved from statistical tests \\cite{gltr,grover,release_strategies} to zero-shot reference-model approaches \\cite{detectgpt,fast_detectgpt,binoculars,dna_gpt} and learned classifiers \\cite{ghostbuster,feat_aug_transformer,reliable_detection,ld_score}.\nRecent work pursues diverse signals including intrinsic dimensionality \\cite{intrinsic_dimension}, surprisal diversity \\cite{diveye}, and distributional gap measures \\cite{generator_barrier}; see \\citet{wu_survey_2025} and \\citet{jawahar_survey} for surveys.\nA persistent limitation is that these methods produce binary (real vs.\\ synthetic) decisions.\nRecent multi-class extensions (role recognition in human-LLM collaboration \\cite{beyond_binary}, multi-generator attribution \\cite{semeval2024_task8}) discriminate among different \\emph{sources} rather than recursive generation \\emph{depth}.\nEven when detection scores correlate with depth, they exhibit high cross-generator variance as ordinal predictors (binary F1 from 0.52 to 0.71; Table~\\ref{tab:baselines}), because each captures a single distributional property that generalizes inconsistently \\cite{paraphrase_evades,detection_possibilities}.\nAdversarial training approaches (e.g., RADAR \\cite{radar}) improve robustness to paraphrasing but remain binary detectors without depth awareness.\nOur contribution is not a new detection method but the task formulation (generation depth classification, framed within the broader ordinal classification literature \\cite{gutierrez_ordinal_survey,coral_ordinal}) and the finding that combining drifting and stationary features yields consistent cross-generator performance.\nThis is orthogonal to source attribution \\cite{uchendu_attribution,munir_looking_glass}, which identifies \\emph{which} model generated text; our LOGO evaluation decouples generator identity from depth.\n\n\\subsection{Model Collapse and Iterative Generation}\n\\label{sec:related-collapse}\n\nSelf-consuming generative models progressively lose distributional coverage \\cite{self_consuming_mad}, and model collapse is inevitable without fresh human data \\cite{curse_of_recursion}, though careful data mixing can mitigate this \\cite{model_collapse_avoidable,strong_model_collapse}.\nThese studies focus on \\emph{training-loop} degradation; our setting studies \\emph{inference chains}, where a fixed model generates text conditioned on its own prior output without retraining.\nIterative self-refinement \\cite{self_refine} represents another form of recursive LLM processing, but targets output improvement through feedback loops rather than open-ended continuation; the distributional drift we study arises specifically from unconstrained recursive generation.\n\nTwo concurrent works are most directly relevant.\n\\citet{broken_telephone} analyze paraphrasing and translation chains, showing progressive information loss.\n\\citet{markovian_chains} demonstrate that semantic-preservation constraints induce attractor dynamics bounding distinguishable depth to approximately three classes; their analysis focuses on characterizing convergence behavior through model-based perplexity tracking.\nWe differ in three respects: (i) we study \\emph{non-paraphrastic continuation} chains, where the absence of semantic anchoring permits richer depth signal; (ii) we use handcrafted features rather than model-internal representations, enabling the DDR decomposition into drifting vs.\\ stationary components; and (iii) we focus on \\emph{estimating} depth from text rather than characterizing the convergence dynamics of the generation process.\n\nThat both works independently converge on approximately three distinguishable classes reflects different mechanisms reaching the same practical ceiling.\n\\citet{markovian_chains} derive this bound from Markovian attractor dynamics: semantic-preservation constraints create fixed points where successive outputs become indistinguishable under model-internal perplexity.\nWe observe the same bound empirically through feature-space compression: inter-class KS statistics drop sharply after depth 2 (gen-1$\\rightarrow$gen-2: KS\\,=\\,0.28 vs.\\ gen-2$\\rightarrow$gen-3: KS\\,=\\,0.09 for entropy mean), collapsing discriminative margins.\nThe approaches are complementary: their theoretical framework explains \\emph{why} convergence occurs (attractor dynamics in semantic space), while our DDR decomposition reveals \\emph{what} converges (location properties) versus what remains stable (distributional shape), providing an empirical signature that can be exploited for detection without access to model internals.\n\n\\subsection{Vocabulary Diversity and Stylometry}\n\\label{sec:related-diversity}\n\nDeclining lexical diversity in LLM-generated text is documented in both training \\cite{curious_decline} and deployment \\cite{writing_diversity} settings.\nOur surface features (TTR and hapax ratio) are classical stylometric measures \\cite{stamatatos_survey,koppel_authorship} that we apply to inference chains, showing monotonic diversity decline across depths without model retraining.\nWe push beyond generator identity \\cite{uchendu_attribution} to the \\emph{depth} dimension, and show that diversity declines monotonically even under top-$p$ sampling \\cite{nucleus_sampling}.\n\n\\subsection{Data Quality and Provenance}\n\\label{sec:related-provenance}\n\nScalable data curation relies on quality signals \\cite{dsir,qurating,ccnet}; generation depth is a complementary provenance signal characterizing \\emph{how many steps removed} text is from a human source.\nProactive watermarking \\cite{watermark_llm,synthid_text,aaronson_watermark} embeds identifiable patterns, but watermark strength decays across multi-step chains \\cite{chainwash}, motivating passive post-hoc methods like ours.\nAt the feature level, our NLL analysis connects to \\citet{min_k_percent}, who use the probability tail for membership inference; we analyze the full NLL distribution for generation depth classification.\n",
      "numLines": 46,
      "startLine": 1,
      "totalLines": 46
    }
  },
  "sourceToolAssistantUUID": "3df2fb92-ac7b-4e92-924f-b099619e44ef",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/review_reviewer_2_3f564e41",
  "sessionId": "b64a1fb5-cc00-4ec5-a8b3-b55f8a4cf13d",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---


### Tool call

_source line 23 · 2026-05-17T17:19:38.994Z_

<details open><summary>🔧 Tool call — Read · `toolu_018grp8woqN9u6Jw15it1MhH`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "295a1a00-61cb-4026-baf1-1f8e4d9c567e",
  "isSidechain": false,
  "requestId": "req_011Cb8XLSEbDP1fjeW6JefBi",
  "type": "assistant",
  "uuid": "b049f353-254b-46f9-888b-743f26c3fe73",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/review_reviewer_2_3f564e41",
  "sessionId": "b64a1fb5-cc00-4ec5-a8b3-b55f8a4cf13d",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01M6zzyEFJAubjv5sPCUpsUd",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1061,
      "cache_creation_input_tokens": 1042,
      "cache_read_input_tokens": 29710,
      "output_tokens": 386,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1042,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1061,
          "output_tokens": 386,
          "cache_read_input_tokens": 29710,
          "cache_creation_input_tokens": 1042,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1042
          },
          "type": "message"
        }
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

_source line 24 · 2026-05-17T17:19:38.999Z_

<details><summary>↩ Tool result · `toolu_018grp8woqN9u6Jw15it1MhH`</summary>

```text
1	% Abstract — Depth Fingerprinting of Recursive LLM Generation Chains
2	\begin{abstract}
3	LLM-generated text increasingly re-enters the web and seeds subsequent generation, producing recursive chains whose outputs progressively diverge from human-written text.
4	We ask whether this drift is structured enough to classify how many generation steps a text has undergone, framing this as \emph{generation depth classification} (gen-0\,/\,gen-1\,/\,gen-2+ rather than binary real-vs-synthetic).
5	Studying eight base models from five families, we identify a \emph{differential depth response} (DDR): central-tendency features (mean entropy, lexical diversity) drift monotonically with generation depth, while shape features (entropy max, vocabulary tail slope) remain near-stationary.
6	This pattern is consistent with a location shift in the token-level negative log-likelihood (NLL) distribution that preserves distributional shape.
7	Exploiting this complementarity, a 7-feature ensemble achieves binary F1\,=\,0.764 on heterogeneous cross-model chains and 0.694 under leave-one-generator-out (LOGO) evaluation across eight generators (3-class macro F1\,=\,0.809 and 0.762, respectively), with competitive performance at substantially lower computational cost than multi-detector alternatives.
8	A TOST equivalence test further confirms that depth-aware data selection yields training utility equivalent to random subsampling ($\pm$2\% margin, $p < 0.001$) within $\leq$4 generations, indicating that the detected distributional shift does not translate to downstream perplexity degradation.
9	\end{abstract}
10	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b049f353-254b-46f9-888b-743f26c3fe73",
  "isSidechain": false,
  "promptId": "c6349ba0-ce02-4cbb-9474-95572d1cbd3f",
  "type": "user",
  "uuid": "0fa5f5cc-880e-44d2-97c9-4bfea93d7db4",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/abstract.tex",
      "content": "% Abstract — Depth Fingerprinting of Recursive LLM Generation Chains\n\\begin{abstract}\nLLM-generated text increasingly re-enters the web and seeds subsequent generation, producing recursive chains whose outputs progressively diverge from human-written text.\nWe ask whether this drift is structured enough to classify how many generation steps a text has undergone, framing this as \\emph{generation depth classification} (gen-0\\,/\\,gen-1\\,/\\,gen-2+ rather than binary real-vs-synthetic).\nStudying eight base models from five families, we identify a \\emph{differential depth response} (DDR): central-tendency features (mean entropy, lexical diversity) drift monotonically with generation depth, while shape features (entropy max, vocabulary tail slope) remain near-stationary.\nThis pattern is consistent with a location shift in the token-level negative log-likelihood (NLL) distribution that preserves distributional shape.\nExploiting this complementarity, a 7-feature ensemble achieves binary F1\\,=\\,0.764 on heterogeneous cross-model chains and 0.694 under leave-one-generator-out (LOGO) evaluation across eight generators (3-class macro F1\\,=\\,0.809 and 0.762, respectively), with competitive performance at substantially lower computational cost than multi-detector alternatives.\nA TOST equivalence test further confirms that depth-aware data selection yields training utility equivalent to random subsampling ($\\pm$2\\% margin, $p < 0.001$) within $\\leq$4 generations, indicating that the detected distributional shift does not translate to downstream perplexity degradation.\n\\end{abstract}\n",
      "numLines": 10,
      "startLine": 1,
      "totalLines": 10
    }
  },
  "sourceToolAssistantUUID": "b049f353-254b-46f9-888b-743f26c3fe73",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/review_reviewer_2_3f564e41",
  "sessionId": "b64a1fb5-cc00-4ec5-a8b3-b55f8a4cf13d",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---


### Tool call

_source line 25 · 2026-05-17T17:19:39.911Z_

<details open><summary>🔧 Tool call — Read · `toolu_01RSxUevaVaWqaK7LwZcHDjQ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0fa5f5cc-880e-44d2-97c9-4bfea93d7db4",
  "isSidechain": false,
  "requestId": "req_011Cb8XLSEbDP1fjeW6JefBi",
  "type": "assistant",
  "uuid": "a9733133-d675-46a9-95f1-694d184fbb23",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/review_reviewer_2_3f564e41",
  "sessionId": "b64a1fb5-cc00-4ec5-a8b3-b55f8a4cf13d",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01M6zzyEFJAubjv5sPCUpsUd",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1061,
      "cache_creation_input_tokens": 1042,
      "cache_read_input_tokens": 29710,
      "output_tokens": 386,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1042,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1061,
          "output_tokens": 386,
          "cache_read_input_tokens": 29710,
          "cache_creation_input_tokens": 1042,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1042
          },
          "type": "message"
        }
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

_source line 26 · 2026-05-17T17:19:39.916Z_

<details><summary>↩ Tool result · `toolu_01RSxUevaVaWqaK7LwZcHDjQ`</summary>

```text
1	\section{Introduction}
2	\label{sec:introduction}
3	
4	LLM-generated text increasingly re-enters the web and seeds subsequent generation \cite{dolma,fineweb}, with estimates suggesting that 7--17\% of recent scientific papers and peer reviews contain substantial LLM-modified content \cite{mapping_llm_science,monitoring_ai_review}.
5	The result is recursive generation chains whose outputs progressively diverge from human-written text.
6	Understanding how distributional features evolve across recursive generation depths is a fundamental question for characterizing recursive generation dynamics, yet existing methods \cite{fast_detectgpt,binoculars,ld_score,detectgpt} provide only binary real-vs-synthetic decisions, conflating qualitatively different material: a first-generation continuation retains much of the source distribution's lexical properties, while deeper recursive text exhibits measurably reduced vocabulary diversity and compressed perplexity.
7	
8	We formulate \emph{generation depth classification}, classifying text by generation depth (gen-0\,/\,gen-1\,/\,gen-2+) rather than a binary label, and refer to the overall framework as \emph{depth fingerprinting}.
9	No existing method addresses this task in non-paraphrastic continuation chains.
10	
11	The key finding is a \emph{differential depth response} (DDR): when we measure how eight base-model generators from five families (Pythia, OLMo, Qwen, Llama, Mistral; 0.6B--8B parameters) transform text across recursive depths, central-tendency and diversity features (reference-model mean entropy, type-token ratio, hapax ratio) drift monotonically, while shape features (entropy max, tail decay) remain near-stationary.
12	This pattern is consistent with recursive generation inducing a location shift in the token-level NLL distribution while preserving its shape: the softmax architecture and fixed sampling parameters constrain distributional shape under standard decoding regimes, while each successive generation compresses the location toward the model's preferred output distribution.
13	We restrict to base (pretrained) models as a deliberate design choice, since instruction-tuning introduces confounds (length regulation, format constraints, safety-driven shaping) that obscure this intrinsic mechanism; preliminary experiments confirm substantially degraded depth signal under instruction tuning (\S\ref{sec:discussion}).
14	
15	The combination of drifting and stationary features yields a 7-feature ensemble that achieves 3-class macro F1\,=\,0.809 on heterogeneous cross-model chains and F1\,=\,0.762 under leave-one-generator-out evaluation (binary F1\,=\,0.764 on cross-model chains), outperforming all individual detection baselines by 6--11\,pp while requiring only a single 410M-parameter reference model (multi-detector ensembles achieve slightly higher 3-class performance at 2.4$\times$ the computational cost; \S\ref{sec:results-baselines}).
16	The signal is prompt-type dependent: continuation chains show stronger drift than elaboration or rewriting (\S\ref{sec:discussion}).
17	
18	Our contributions are threefold:
19	\begin{enumerate}[nosep,leftmargin=*]
20	    \item We formulate generation depth classification, moving beyond binary real-vs-synthetic detection to classify text as gen-0\,/\,gen-1\,/\,gen-2+, and construct an evaluation suite of 37K texts from eight base-model generators spanning five families (0.6B--8B parameters).
21	    \item We identify \emph{differential depth response} (DDR), showing that recursive generation induces monotonic drift in central-tendency features ($|\rho| > 0.60$) while preserving distributional shape ($|\rho| < 0.10$). A 7-feature ensemble exploiting this structure achieves 3-class F1\,=\,0.809 on cross-model chains with a single 410M reference model.
22	    \item We demonstrate via equivalence testing (TOST $\pm$2\%, $p < 0.001$) that depth-aware data curation yields training utility indistinguishable from random subsampling at equal sample count, confirming that the detected distributional shift does not translate to downstream perplexity degradation (\S\ref{sec:results-downstream}).
23	\end{enumerate}
24	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a9733133-d675-46a9-95f1-694d184fbb23",
  "isSidechain": false,
  "promptId": "c6349ba0-ce02-4cbb-9474-95572d1cbd3f",
  "type": "user",
  "uuid": "8767ffbe-70ec-4a1c-a3c3-d06af12d8116",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/introduction.tex",
      "content": "\\section{Introduction}\n\\label{sec:introduction}\n\nLLM-generated text increasingly re-enters the web and seeds subsequent generation \\cite{dolma,fineweb}, with estimates suggesting that 7--17\\% of recent scientific papers and peer reviews contain substantial LLM-modified content \\cite{mapping_llm_science,monitoring_ai_review}.\nThe result is recursive generation chains whose outputs progressively diverge from human-written text.\nUnderstanding how distributional features evolve across recursive generation depths is a fundamental question for characterizing recursive generation dynamics, yet existing methods \\cite{fast_detectgpt,binoculars,ld_score,detectgpt} provide only binary real-vs-synthetic decisions, conflating qualitatively different material: a first-generation continuation retains much of the source distribution's lexical properties, while deeper recursive text exhibits measurably reduced vocabulary diversity and compressed perplexity.\n\nWe formulate \\emph{generation depth classification}, classifying text by generation depth (gen-0\\,/\\,gen-1\\,/\\,gen-2+) rather than a binary label, and refer to the overall framework as \\emph{depth fingerprinting}.\nNo existing method addresses this task in non-paraphrastic continuation chains.\n\nThe key finding is a \\emph{differential depth response} (DDR): when we measure how eight base-model generators from five families (Pythia, OLMo, Qwen, Llama, Mistral; 0.6B--8B parameters) transform text across recursive depths, central-tendency and diversity features (reference-model mean entropy, type-token ratio, hapax ratio) drift monotonically, while shape features (entropy max, tail decay) remain near-stationary.\nThis pattern is consistent with recursive generation inducing a location shift in the token-level NLL distribution while preserving its shape: the softmax architecture and fixed sampling parameters constrain distributional shape under standard decoding regimes, while each successive generation compresses the location toward the model's preferred output distribution.\nWe restrict to base (pretrained) models as a deliberate design choice, since instruction-tuning introduces confounds (length regulation, format constraints, safety-driven shaping) that obscure this intrinsic mechanism; preliminary experiments confirm substantially degraded depth signal under instruction tuning (\\S\\ref{sec:discussion}).\n\nThe combination of drifting and stationary features yields a 7-feature ensemble that achieves 3-class macro F1\\,=\\,0.809 on heterogeneous cross-model chains and F1\\,=\\,0.762 under leave-one-generator-out evaluation (binary F1\\,=\\,0.764 on cross-model chains), outperforming all individual detection baselines by 6--11\\,pp while requiring only a single 410M-parameter reference model (multi-detector ensembles achieve slightly higher 3-class performance at 2.4$\\times$ the computational cost; \\S\\ref{sec:results-baselines}).\nThe signal is prompt-type dependent: continuation chains show stronger drift than elaboration or rewriting (\\S\\ref{sec:discussion}).\n\nOur contributions are threefold:\n\\begin{enumerate}[nosep,leftmargin=*]\n    \\item We formulate generation depth classification, moving beyond binary real-vs-synthetic detection to classify text as gen-0\\,/\\,gen-1\\,/\\,gen-2+, and construct an evaluation suite of 37K texts from eight base-model generators spanning five families (0.6B--8B parameters).\n    \\item We identify \\emph{differential depth response} (DDR), showing that recursive generation induces monotonic drift in central-tendency features ($|\\rho| > 0.60$) while preserving distributional shape ($|\\rho| < 0.10$). A 7-feature ensemble exploiting this structure achieves 3-class F1\\,=\\,0.809 on cross-model chains with a single 410M reference model.\n    \\item We demonstrate via equivalence testing (TOST $\\pm$2\\%, $p < 0.001$) that depth-aware data curation yields training utility indistinguishable from random subsampling at equal sample count, confirming that the detected distributional shift does not translate to downstream perplexity degradation (\\S\\ref{sec:results-downstream}).\n\\end{enumerate}\n",
      "numLines": 24,
      "startLine": 1,
      "totalLines": 24
    }
  },
  "sourceToolAssistantUUID": "a9733133-d675-46a9-95f1-694d184fbb23",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/review_reviewer_2_3f564e41",
  "sessionId": "b64a1fb5-cc00-4ec5-a8b3-b55f8a4cf13d",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---


### Tool call

_source line 27 · 2026-05-17T17:19:40.011Z_

<details open><summary>🔧 Tool call — Read · `toolu_019radH38e5XCYBqUgPCCQ1x`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8767ffbe-70ec-4a1c-a3c3-d06af12d8116",
  "isSidechain": false,
  "requestId": "req_011Cb8XLSEbDP1fjeW6JefBi",
  "type": "assistant",
  "uuid": "3df2fb92-ac7b-4e92-924f-b099619e44ef",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/review_reviewer_2_3f564e41",
  "sessionId": "b64a1fb5-cc00-4ec5-a8b3-b55f8a4cf13d",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01M6zzyEFJAubjv5sPCUpsUd",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1061,
      "cache_creation_input_tokens": 1042,
      "cache_read_input_tokens": 29710,
      "output_tokens": 386,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1042,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1061,
          "output_tokens": 386,
          "cache_read_input_tokens": 29710,
          "cache_creation_input_tokens": 1042,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1042
          },
          "type": "message"
        }
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

_source line 28_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[Round 1 审稿请求]: 你负责**新颖性 + 完整性 + Related Work + 格式**。  ## Venue 信息 - **目标**: EMNLP 2026（ARR May 2026 cycle） - **截止日期**: 2026-05-25 - **页数限制**: Long paper 正文 8 页（不含 limitations/ethics/references） - **模…",
  "leafUuid": "74c1465a-95dd-4b3f-82d0-cfed5922f79c",
  "sessionId": "b64a1fb5-cc00-4ec5-a8b3-b55f8a4cf13d"
}
```

---


### Runtime record

_source line 29_

```json
{
  "type": "ai-title",
  "aiTitle": "Review depth fingerprinting paper for EMNLP 2026",
  "sessionId": "b64a1fb5-cc00-4ec5-a8b3-b55f8a4cf13d"
}
```

---


### Tool result

_source line 30 · 2026-05-17T17:19:45.890Z_

<details><summary>↩ Tool result · `toolu_01JK3BQAEdhWWmuWMNbtQXD4`</summary>

```text
Web search results for query: "ACL Rolling Review review form soundness excitement scoring scale 1-5 2025"

Links: [{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"aclrollingreview/acguidelines.md at main · yoshitomo-matsubara/aclrollingreview","url":"https://github.com/yoshitomo-matsubara/aclrollingreview/blob/main/acguidelines.md"},{"title":"ACL 2026 on X: \"Checkout the blog post on the soundness/excitement scores https://t.co/AKSO9DjiYP . It clarifies the reasoning behind the separation of overall scores and how it might make the reviewer recommendation more robust. #ACL2023Toronto #ACL2023NLP #NLProc\" / X","url":"https://x.com/aclmeeting/status/1637827267173953540"},{"title":"aclrollingreview/reviewerguidelines.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/reviewerguidelines.md"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"aclrollingreview/acguidelines.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/acguidelines.md"},{"title":"Conference Decisions · GitHub","url":"https://gist.github.com/antonisa/2158dee79179c7c49304ef353887bfa0"}]

I found information about the ACL Rolling Review (ARR) review form with soundness and excitement scoring. Here's what the review form specifies for 2025:

## Soundness Scale (1-5)

The soundness scale includes: 5 = Excellent (one of the most thorough studies), 4 = Strong (provides sufficient support for all claims), and 3 = Acceptable (provides sufficient support for main claims).

The soundness assessment asks whether the paper is sufficiently sound and thorough, clearly states scientific claims, and provides adequate support for them, considering factors like research question depth, technical soundness of experiments, and methodological validity.

## Excitement Scale (1-5)

The excitement scale ranges from: 5 = Highly Exciting (would recommend to others and/or attend presentation) to 4 = Exciting (would mention to others and/or make effort to attend). A score of 1 = Not Exciting indicates the paper doesn't resonate and wouldn't appeal to the *ACL community.

Excitement is subjective and can reflect papers perceived as transformational/innovative/surprising due to conceptual breakthroughs, challenging common assumptions, or potential impact on communities through lowering barriers, reducing costs, or enabling new applications.

## Implementation Notes for 2025

Starting with February 2025, ARR reviewers are asked to provide three scores: soundness, excitement, and overall recommendation. Soundness scores must be justified by the review text; giving a low soundness score without finding major faults means the review is not a faithful explanation.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "295a1a00-61cb-4026-baf1-1f8e4d9c567e",
  "isSidechain": false,
  "promptId": "c6349ba0-ce02-4cbb-9474-95572d1cbd3f",
  "type": "user",
  "uuid": "4c030da1-967a-483b-9045-c48aab706258",
  "toolUseResult": {
    "query": "ACL Rolling Review review form soundness excitement scoring scale 1-5 2025",
    "results": [
      {
        "tool_use_id": "srvtoolu_019b5ySb6EK7yfL6w9uWGMKK",
        "content": [
          {
            "title": "Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics",
            "url": "http://aclrollingreview.org/reviewform"
          },
          {
            "title": "ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics",
            "url": "http://aclrollingreview.org/acguidelines"
          },
          {
            "title": "ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics",
            "url": "http://aclrollingreview.org/reviewerguidelines"
          },
          {
            "title": "Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics",
            "url": "http://aclrollingreview.org/authors"
          },
          {
            "title": "aclrollingreview/acguidelines.md at main · yoshitomo-matsubara/aclrollingreview",
            "url": "https://github.com/yoshitomo-matsubara/aclrollingreview/blob/main/acguidelines.md"
          },
          {
            "title": "ACL 2026 on X: \"Checkout the blog post on the soundness/excitement scores https://t.co/AKSO9DjiYP . It clarifies the reasoning behind the separation of overall scores and how it might make the reviewer recommendation more robust. #ACL2023Toronto #ACL2023NLP #NLProc\" / X",
            "url": "https://x.com/aclmeeting/status/1637827267173953540"
          },
          {
            "title": "aclrollingreview/reviewerguidelines.md at main · acl-org/aclrollingreview",
            "url": "https://github.com/acl-org/aclrollingreview/blob/main/reviewerguidelines.md"
          },
          {
            "title": "ACL Rolling Review – A peer review platform for the Association for Computational Linguistics",
            "url": "http://aclrollingreview.org/"
          },
          {
            "title": "aclrollingreview/acguidelines.md at main · acl-org/aclrollingreview",
            "url": "https://github.com/acl-org/aclrollingreview/blob/main/acguidelines.md"
          },
          {
            "title": "Conference Decisions · GitHub",
            "url": "https://gist.github.com/antonisa/2158dee79179c7c49304ef353887bfa0"
          }
        ]
      },
      "I found information about the ACL Rolling Review (ARR) review form with soundness and excitement scoring. Here's what the review form specifies for 2025:\n\n## Soundness Scale (1-5)\n\nThe soundness scale includes: 5 = Excellent (one of the most thorough studies), 4 = Strong (provides sufficient support for all claims), and 3 = Acceptable (provides sufficient support for main claims).\n\nThe soundness assessment asks whether the paper is sufficiently sound and thorough, clearly states scientific claims, and provides adequate support for them, considering factors like research question depth, technical soundness of experiments, and methodological validity.\n\n## Excitement Scale (1-5)\n\nThe excitement scale ranges from: 5 = Highly Exciting (would recommend to others and/or attend presentation) to 4 = Exciting (would mention to others and/or make effort to attend). A score of 1 = Not Exciting indicates the paper doesn't resonate and wouldn't appeal to the *ACL community.\n\nExcitement is subjective and can reflect papers perceived as transformational/innovative/surprising due to conceptual breakthroughs, challenging common assumptions, or potential impact on communities through lowering barriers, reducing costs, or enabling new applications.\n\n## Implementation Notes for 2025\n\nStarting with February 2025, ARR reviewers are asked to provide three scores: soundness, excitement, and overall recommendation. Soundness scores must be justified by the review text; giving a low soundness score without finding major faults means the review is not a faithful explanation."
    ],
    "durationSeconds": 7.484714513000003
  },
  "sourceToolAssistantUUID": "295a1a00-61cb-4026-baf1-1f8e4d9c567e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/review_reviewer_2_3f564e41",
  "sessionId": "b64a1fb5-cc00-4ec5-a8b3-b55f8a4cf13d",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---


### Assistant

_source line 31 · 2026-05-17T17:19:49.844Z_

<details><summary>Logged reasoning block</summary>

```text
Good, I have the abstract, introduction, and related work. Let me now read the method, results, discussion, conclusion, and limitations sections.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4c030da1-967a-483b-9045-c48aab706258",
  "isSidechain": false,
  "requestId": "req_011Cb8XMRGpRjUWH8BmPNN3N",
  "type": "assistant",
  "uuid": "629d2b1a-bced-4f27-a595-d8619bfa626b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/review_reviewer_2_3f564e41",
  "sessionId": "b64a1fb5-cc00-4ec5-a8b3-b55f8a4cf13d",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BN5w5R6jgmeJcv1zoXT7mM",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3104,
      "cache_creation_input_tokens": 2417,
      "cache_read_input_tokens": 30752,
      "output_tokens": 302,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2417,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3104,
          "output_tokens": 302,
          "cache_read_input_tokens": 30752,
          "cache_creation_input_tokens": 2417,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2417
          },
          "type": "message"
        }
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

_source line 32 · 2026-05-17T17:19:50.344Z_

继续读取 method、results、discussion、conclusion 和 limitations 章节。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "629d2b1a-bced-4f27-a595-d8619bfa626b",
  "isSidechain": false,
  "requestId": "req_011Cb8XMRGpRjUWH8BmPNN3N",
  "type": "assistant",
  "uuid": "417acc8f-14d8-4576-ab97-1f9e0e5c1e74",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/review_reviewer_2_3f564e41",
  "sessionId": "b64a1fb5-cc00-4ec5-a8b3-b55f8a4cf13d",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BN5w5R6jgmeJcv1zoXT7mM",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3104,
      "cache_creation_input_tokens": 2417,
      "cache_read_input_tokens": 30752,
      "output_tokens": 302,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2417,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3104,
          "output_tokens": 302,
          "cache_read_input_tokens": 30752,
          "cache_creation_input_tokens": 2417,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2417
          },
          "type": "message"
        }
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

_source line 33 · 2026-05-17T17:19:52.676Z_

<details open><summary>🔧 Tool call — Read · `toolu_012Rh9LnD8YgVWEdcUaTcWYe`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "417acc8f-14d8-4576-ab97-1f9e0e5c1e74",
  "isSidechain": false,
  "requestId": "req_011Cb8XMRGpRjUWH8BmPNN3N",
  "type": "assistant",
  "uuid": "553aaf45-0063-412c-adc5-88d3d1982530",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/review_reviewer_2_3f564e41",
  "sessionId": "b64a1fb5-cc00-4ec5-a8b3-b55f8a4cf13d",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BN5w5R6jgmeJcv1zoXT7mM",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3104,
      "cache_creation_input_tokens": 2417,
      "cache_read_input_tokens": 30752,
      "output_tokens": 302,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2417,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3104,
          "output_tokens": 302,
          "cache_read_input_tokens": 30752,
          "cache_creation_input_tokens": 2417,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2417
          },
          "type": "message"
        }
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

_source line 34 · 2026-05-17T17:19:53.619Z_

<details><summary>↩ Tool result · `toolu_018PwuSutJUvpbyPqGDHkJA2`</summary>

```text
1	\section{Discussion}
2	\label{sec:discussion}
3	
4	The near-stationarity of shape features across recursive depths is consistent with the softmax architecture and fixed sampling parameters constraining distributional shape: recursive generation shifts context toward high-probability regions without altering the generation mechanism itself.
5	One hypothesis is that standard decoding regimes inherently preserve the functional form of the NLL distribution while allowing its location to drift.
6	Sampling ablation supports this as a tendency rather than an architectural guarantee ($t \in [0.5, 0.7]$: ${\leq}0.3$\,pp degradation; $t = 1.0$: $-6$\,pp; Appendix~\ref{app:sampling-sensitivity}).
7	Prompt-type dependence further modulates the effect: semantic-preservation constraints attenuate drift (elaboration F1\,=\,0.730 vs.\ continuation 0.781; Appendix~\ref{app:prompt-type}), consistent with \citet{broken_telephone} showing that tasks anchoring the output distribution to the input leave less room for recursive drift to accumulate.
8	Cross-type transfer remains viable (F1\,=\,0.753).
9	
10	At the document level, gen-1 per-class F1\,=\,0.63 is insufficient for automated filtering but sufficient for corpus-level flagging, where error scales as $O(1/\sqrt{n})$.
11	The gen-1\,/\,gen-2+ boundary concentrates 86\% of binary errors as false negatives (gen-2+ predicted as gen-1), with depth-2 error rate at 48\% vs.\ 20\% for depth-4, consistent with DDR predictions that the first recursive step produces the smallest location shift; larger generators exacerbate this (Mistral-7B error rate 45\% vs.\ Pythia-1B 18\%; Appendix~\ref{app:error-analysis}).
12	Reference-model family bias is limited: Pythia generators show slightly higher F1 with the Pythia-410M reference, but cross-reference spread is only 0.013\,pp (Table~\ref{tab:cross-ref}).
13	Cross-temperature transfer presents a more significant limitation: classifiers trained at $t{=}0.7$ degrade substantially when tested at $t{=}1.0$ (Qwen3-1.7B LOGO F1 drops from 0.789 to 0.418; Appendix~\ref{app:cross-temp}), indicating that deployment under unknown temperature conditions requires temperature-specific calibration or multi-temperature training.
14	
15	Three classes represent the practical resolution ceiling: 5-class LOGO F1 drops to ${\approx}$0.50 with depths 2--4 mutually indistinguishable (Appendix~\ref{app:finer-depth}).
16	QLoRA fine-tuning recovers F1\,=\,0.905 (Appendix~\ref{app:qlora}), confirming richer signal beyond the seven summary statistics, at the cost of interpretability.
17	DDR is fundamentally different from model collapse \cite{curse_of_recursion,strong_model_collapse}, which describes degradation when models are retrained on their own outputs: inference-chain drift occurs with fixed parameters and is fully reversible, and preserves distributional shape while shifting location, suggesting compression within existing capacity rather than erosion of it.
18	Instruction-tuned models show substantially weaker fingerprints (OLMo-Instruct LOGO F1\,=\,0.338 vs.\ 0.763 base), as alignment-imposed length regulation and format constraints compress the distributional variation that depth fingerprinting exploits, justifying our restriction to base models for isolating the phenomenon.
19	Under text perturbation, LLM-simulated regeneration causes comparable degradation to random word replacement (Appendix~\ref{app:human-edit}), confirming depth signal resides in generative structure.
20	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6f1eb37c-fb99-4668-92ba-70cdccfc4254",
  "isSidechain": false,
  "promptId": "c6349ba0-ce02-4cbb-9474-95572d1cbd3f",
  "type": "user",
  "uuid": "8a30330f-3d19-4256-852d-f2d6e23cc856",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/discussion.tex",
      "content": "\\section{Discussion}\n\\label{sec:discussion}\n\nThe near-stationarity of shape features across recursive depths is consistent with the softmax architecture and fixed sampling parameters constraining distributional shape: recursive generation shifts context toward high-probability regions without altering the generation mechanism itself.\nOne hypothesis is that standard decoding regimes inherently preserve the functional form of the NLL distribution while allowing its location to drift.\nSampling ablation supports this as a tendency rather than an architectural guarantee ($t \\in [0.5, 0.7]$: ${\\leq}0.3$\\,pp degradation; $t = 1.0$: $-6$\\,pp; Appendix~\\ref{app:sampling-sensitivity}).\nPrompt-type dependence further modulates the effect: semantic-preservation constraints attenuate drift (elaboration F1\\,=\\,0.730 vs.\\ continuation 0.781; Appendix~\\ref{app:prompt-type}), consistent with \\citet{broken_telephone} showing that tasks anchoring the output distribution to the input leave less room for recursive drift to accumulate.\nCross-type transfer remains viable (F1\\,=\\,0.753).\n\nAt the document level, gen-1 per-class F1\\,=\\,0.63 is insufficient for automated filtering but sufficient for corpus-level flagging, where error scales as $O(1/\\sqrt{n})$.\nThe gen-1\\,/\\,gen-2+ boundary concentrates 86\\% of binary errors as false negatives (gen-2+ predicted as gen-1), with depth-2 error rate at 48\\% vs.\\ 20\\% for depth-4, consistent with DDR predictions that the first recursive step produces the smallest location shift; larger generators exacerbate this (Mistral-7B error rate 45\\% vs.\\ Pythia-1B 18\\%; Appendix~\\ref{app:error-analysis}).\nReference-model family bias is limited: Pythia generators show slightly higher F1 with the Pythia-410M reference, but cross-reference spread is only 0.013\\,pp (Table~\\ref{tab:cross-ref}).\nCross-temperature transfer presents a more significant limitation: classifiers trained at $t{=}0.7$ degrade substantially when tested at $t{=}1.0$ (Qwen3-1.7B LOGO F1 drops from 0.789 to 0.418; Appendix~\\ref{app:cross-temp}), indicating that deployment under unknown temperature conditions requires temperature-specific calibration or multi-temperature training.\n\nThree classes represent the practical resolution ceiling: 5-class LOGO F1 drops to ${\\approx}$0.50 with depths 2--4 mutually indistinguishable (Appendix~\\ref{app:finer-depth}).\nQLoRA fine-tuning recovers F1\\,=\\,0.905 (Appendix~\\ref{app:qlora}), confirming richer signal beyond the seven summary statistics, at the cost of interpretability.\nDDR is fundamentally different from model collapse \\cite{curse_of_recursion,strong_model_collapse}, which describes degradation when models are retrained on their own outputs: inference-chain drift occurs with fixed parameters and is fully reversible, and preserves distributional shape while shifting location, suggesting compression within existing capacity rather than erosion of it.\nInstruction-tuned models show substantially weaker fingerprints (OLMo-Instruct LOGO F1\\,=\\,0.338 vs.\\ 0.763 base), as alignment-imposed length regulation and format constraints compress the distributional variation that depth fingerprinting exploits, justifying our restriction to base models for isolating the phenomenon.\nUnder text perturbation, LLM-simulated regeneration causes comparable degradation to random word replacement (Appendix~\\ref{app:human-edit}), confirming depth signal resides in generative structure.\n",
      "numLines": 20,
      "startLine": 1,
      "totalLines": 20
    }
  },
  "sourceToolAssistantUUID": "6f1eb37c-fb99-4668-92ba-70cdccfc4254",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/review_reviewer_2_3f564e41",
  "sessionId": "b64a1fb5-cc00-4ec5-a8b3-b55f8a4cf13d",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---


### Tool result

_source line 35 · 2026-05-17T17:19:52.681Z_

<details><summary>↩ Tool result · `toolu_012Rh9LnD8YgVWEdcUaTcWYe`</summary>

```text
1	\section{Method}
2	\label{sec:method}
3	
4	\begin{figure*}[t]
5	\centering
6	\includegraphics[width=\textwidth]{fig2_framework.pdf}
7	\caption{Overview of the depth fingerprinting framework. Given a text, reference-model features (entropy statistics under Pythia-410M) and surface features (lexical diversity) are extracted and fed to an XGBoost classifier trained under Leave-One-Generator-Out cross-validation. The feature set combines drifting indicators (entropy mean, TTR, hapax ratio) that capture the monotonic location shift with stationary indicators (entropy max, tail decay) that provide a stable baseline, exploiting their differential depth response for ordinal classification.}
8	\label{fig:framework}
9	\end{figure*}
10	
11	\subsection{Task Formulation}
12	\label{sec:task}
13	
14	Given a text $x$, the goal is to predict its \emph{generation depth} $d \in \{0, 1, 2{+}\}$, where $d{=}0$ denotes human-written text, $d{=}1$ denotes first-generation LLM output conditioned on human text, and $d{=}2{+}$ denotes text produced by recursively conditioning an LLM on its own prior output at least twice.
15	Formally, let $\mathcal{C}_0$ be a reference corpus of human-written text.
16	A generation chain of depth $k$ is defined recursively: $x^{(0)} \sim \mathcal{C}_0$, and $x^{(k)} = G(x^{(k-1)})$ for $k \geq 1$, where $G$ denotes stochastic LLM generation conditioned on its input.
17	We frame depth estimation as an ordinal classification task over three classes rather than binary real-vs-synthetic detection, enabling finer-grained provenance characterization.
18	Depths beyond 2 are merged into a single $2{+}$ class, consistent with monotonic feature convergence that compresses inter-class margins beyond depth 2 (\S\ref{sec:results-differential}).
19	
20	\subsection{Generation Chain Construction}
21	\label{sec:generation}
22	
23	We construct generation chains using eight generators spanning five model families: \textbf{Pythia} (2.8B, 1B) \cite{pythia}, \textbf{OLMo} (OLMo-2-1B) \cite{olmo}, \textbf{Qwen} (Qwen3-1.7B, Qwen3-0.6B, Qwen3-8B-Base) \cite{qwen3}, \textbf{Llama} (Llama-3.2-3B) \cite{llama3}, and \textbf{Mistral} (Mistral-7B-v0.3) \cite{mistral7b}.
24	This selection covers parameter scales from 0.6B to 8B and diverse pretraining corpora, enabling evaluation of cross-generator and cross-scale generalization.
25	
26	For each generator, we sample approximately 1{,}000 seed passages from English Wikipedia as $\mathcal{C}_0$.
27	The same pool of seed passages serves as gen-0 for all generators.
28	We use shared seeds across generators to ensure that cross-generator comparisons control for input content, isolating the effect of the generation model from source text variation.
29	In LOGO evaluation, gen-0 samples from the held-out generator's chains also appear (with the same text) in the training generators' chains, creating a potential train--test overlap for the gen-0 class.
30	We address this with a supplementary binary evaluation excluding gen-0 entirely (\S\ref{sec:results-baselines}).
31	Each seed is iteratively fed through the generator to produce a chain of depth 4 (i.e., gen-0 through gen-4), using the prompt ``\texttt{Continue the following text: \{text\}}''.
32	All generation uses temperature $\tau{=}0.7$, nucleus sampling with $p{=}0.9$, and maximum length of 256 new tokens.
33	The theoretical yield is $8 \times {\sim}1{,}000 \times 5 \approx 40{,}000$ texts; after removing generation failures, exact duplicates, and passages shorter than 50 tokens, 37{,}058 texts remain (Appendix~\ref{app:dataset-stats}).
34	For classification, depths 2--4 are collapsed into the $2{+}$ class.
35	
36	\subsection{Feature Extraction}
37	\label{sec:features}
38	
39	The seven features are motivated by two complementary views of distributional drift.
40	Reference-model features capture how the text's token-level surprise distribution shifts relative to a fixed model; surface features capture how lexical diversity contracts under recursive generation.
41	Together, they span both the generative mechanism (what the model produces) and the surface manifestation (how the vocabulary changes); Figure~\ref{fig:framework} provides an overview.
42	This two-pronged design is not post-hoc: it follows directly from the hypothesis that recursive generation induces a location shift in the NLL distribution (\S\ref{sec:results-differential}).
43	
44	We extract seven distributional features per text, organized into two groups based on what they measure rather than how they are computed.
45	
46	\paragraph{Reference-model features.}
47	A held-out reference model (Pythia-410M, chosen to be smaller than all generators) computes per-token negative log-likelihood (NLL) for each text.
48	Although Pythia-410M shares the GPT-NeoX architecture with two of the eight generators, cross-family reference model experiments (\S\ref{sec:results-differential}) confirm that depth features are not reference-specific (LOGO F1 varies by $\leq$0.013 across Pythia, OLMo, and Qwen references).
49	From the resulting NLL sequence, we extract five statistics:
50	\begin{itemize}[nosep,leftmargin=*]
51	    \item \textbf{entropy\_mean}\footnote{We use ``entropy'' as shorthand for token-level negative log-likelihood under the reference model, following convention in prior detection work. These are point-wise NLL values, not Shannon entropy of the full distribution.}: mean token-level NLL, capturing the average predictability of the text under the reference model;
52	    \item \textbf{entropy\_std}: standard deviation of token-level NLL, measuring the spread of per-token surprise;
53	    \item \textbf{entropy\_max}: maximum token-level NLL, capturing the most surprising token;
54	    \item \textbf{entropy\_min}: minimum token-level NLL, capturing the most predictable token. As generation depth increases, the floor of token-level surprise drops, reflecting the model's increasing confidence on its own outputs.
55	    Although entropy\_min shows near-zero marginal impact in leave-one-feature-out analysis ($\Delta$F1\,=\,+0.01\,pp), we retain it for completeness of the NLL summary statistics (mean, std, max, min) and because removing it does not improve performance;
56	    \item \textbf{tail\_decay}: slope of the vocabulary-level averaged log-probability distribution in the mid-rank region (ranks 100--1000).
57	    For each text, we compute the mean log-probability of each vocabulary token across all positions under the reference model, sort tokens in descending order of mean log-probability, and fit a linear regression to ranks 100--1000.
58	    The slope captures how steeply the reference model's probability mass decays beyond high-probability tokens, characterizing the shape of the distribution tail.
59	\end{itemize}
60	
61	\paragraph{Surface features.}
62	Two features capture lexical diversity without requiring a reference model:
63	\begin{itemize}[nosep,leftmargin=*]
64	    \item \textbf{TTR}: type-token ratio (number of unique word types divided by total tokens);
65	    \item \textbf{hapax\_ratio}: proportion of words appearing exactly once (\emph{hapax legomena}).
66	\end{itemize}
67	
68	\paragraph{Feature complementarity.}
69	The grouping reflects an empirical pattern we term \emph{differential depth response}: central-tendency and diversity features (entropy\_mean, TTR, hapax\_ratio) show substantial monotonic drift with generation depth ($|\rho| = 0.60$--$0.63$); entropy\_min and entropy\_std show moderate drift ($|\rho| = 0.17$--$0.41$); and shape features (entropy\_max, tail\_decay) remain near-stationary ($|\rho| < 0.10$).
70	This differential behavior, consistent with recursive generation shifting the location of the NLL distribution while preserving distributional shape, motivates combining both feature types.
71	As shown in \S\ref{sec:results}, the full 7-feature set significantly outperforms either group alone.
72	
73	\subsection{Evaluation Protocol}
74	\label{sec:evaluation}
75	
76	\paragraph{Cross-validation.}
77	To evaluate generalization to unseen generators, we use \textbf{Leave-One-Generator-Out (LOGO)} cross-validation: in each fold, one of the eight generators is held out for testing and the remaining seven provide training data.
78	We additionally report \textbf{Leave-One-Family-Out (LOFO)} results, where an entire model family (e.g., all Qwen models) is held out, testing generalization across architectural lineages.
79	
80	\paragraph{Classifier.}
81	We use XGBoost \cite{xgboost} throughout ($n\_\text{estimators}{=}200$, $\max\_\text{depth}{=}6$, learning rate $0.1$), with identical hyperparameters across all methods in Table~\ref{tab:baselines}.
82	LOGO F1 is stable across random seeds (std\,$<$\,0.001 over 5 seeds).
83	Alternative classifiers and ordinal-specific methods (CORAL \cite{coral_ordinal}, Frank-Hall \cite{frank_hall_ordinal}) yield comparable performance (Appendix~\ref{app:classifier}), confirming that discriminative power resides in the features.
84	
85	\paragraph{Metrics and statistical testing.}
86	The primary metric is \textbf{macro-averaged F1} over the three depth classes.
87	We report 95\% confidence intervals via percentile bootstrap ($n{=}1{,}000$), McNemar tests for pairwise comparisons, and paired bootstrap for baseline comparisons.
88	All $p$-values are two-sided; Bonferroni correction is applied where multiple comparisons arise.
89	Feature--depth correlations (\S\ref{sec:results-differential}) use class-balanced subsamples to control for depth-class imbalance.
90	
91	\paragraph{Baselines.}
92	We compare the 7-feature ensemble against four single-score detection methods repurposed as depth predictors: Avg-LogProb, FastDetectGPT \cite{fast_detectgpt}, Binoculars \cite{binoculars}, and LD-Score \cite{ld_score}.
93	Each baseline score is used as a univariate feature in the same XGBoost framework under LOGO cross-validation, ensuring a controlled comparison.
94	
95	\paragraph{Length confound control.}
96	Since TTR and hapax\_ratio are mechanically length-dependent, we verify depth signal is not a length artifact via length-matched subsampling that equalizes length distributions across depth classes (\S\ref{sec:results-classification}; Appendix~\ref{app:length}).
97	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "553aaf45-0063-412c-adc5-88d3d1982530",
  "isSidechain": false,
  "promptId": "c6349ba0-ce02-4cbb-9474-95572d1cbd3f",
  "type": "user",
  "uuid": "c817b32a-ff19-4a1e-9edb-acb39e0ebb91",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/method.tex",
      "content": "\\section{Method}\n\\label{sec:method}\n\n\\begin{figure*}[t]\n\\centering\n\\includegraphics[width=\\textwidth]{fig2_framework.pdf}\n\\caption{Overview of the depth fingerprinting framework. Given a text, reference-model features (entropy statistics under Pythia-410M) and surface features (lexical diversity) are extracted and fed to an XGBoost classifier trained under Leave-One-Generator-Out cross-validation. The feature set combines drifting indicators (entropy mean, TTR, hapax ratio) that capture the monotonic location shift with stationary indicators (entropy max, tail decay) that provide a stable baseline, exploiting their differential depth response for ordinal classification.}\n\\label{fig:framework}\n\\end{figure*}\n\n\\subsection{Task Formulation}\n\\label{sec:task}\n\nGiven a text $x$, the goal is to predict its \\emph{generation depth} $d \\in \\{0, 1, 2{+}\\}$, where $d{=}0$ denotes human-written text, $d{=}1$ denotes first-generation LLM output conditioned on human text, and $d{=}2{+}$ denotes text produced by recursively conditioning an LLM on its own prior output at least twice.\nFormally, let $\\mathcal{C}_0$ be a reference corpus of human-written text.\nA generation chain of depth $k$ is defined recursively: $x^{(0)} \\sim \\mathcal{C}_0$, and $x^{(k)} = G(x^{(k-1)})$ for $k \\geq 1$, where $G$ denotes stochastic LLM generation conditioned on its input.\nWe frame depth estimation as an ordinal classification task over three classes rather than binary real-vs-synthetic detection, enabling finer-grained provenance characterization.\nDepths beyond 2 are merged into a single $2{+}$ class, consistent with monotonic feature convergence that compresses inter-class margins beyond depth 2 (\\S\\ref{sec:results-differential}).\n\n\\subsection{Generation Chain Construction}\n\\label{sec:generation}\n\nWe construct generation chains using eight generators spanning five model families: \\textbf{Pythia} (2.8B, 1B) \\cite{pythia}, \\textbf{OLMo} (OLMo-2-1B) \\cite{olmo}, \\textbf{Qwen} (Qwen3-1.7B, Qwen3-0.6B, Qwen3-8B-Base) \\cite{qwen3}, \\textbf{Llama} (Llama-3.2-3B) \\cite{llama3}, and \\textbf{Mistral} (Mistral-7B-v0.3) \\cite{mistral7b}.\nThis selection covers parameter scales from 0.6B to 8B and diverse pretraining corpora, enabling evaluation of cross-generator and cross-scale generalization.\n\nFor each generator, we sample approximately 1{,}000 seed passages from English Wikipedia as $\\mathcal{C}_0$.\nThe same pool of seed passages serves as gen-0 for all generators.\nWe use shared seeds across generators to ensure that cross-generator comparisons control for input content, isolating the effect of the generation model from source text variation.\nIn LOGO evaluation, gen-0 samples from the held-out generator's chains also appear (with the same text) in the training generators' chains, creating a potential train--test overlap for the gen-0 class.\nWe address this with a supplementary binary evaluation excluding gen-0 entirely (\\S\\ref{sec:results-baselines}).\nEach seed is iteratively fed through the generator to produce a chain of depth 4 (i.e., gen-0 through gen-4), using the prompt ``\\texttt{Continue the following text: \\{text\\}}''.\nAll generation uses temperature $\\tau{=}0.7$, nucleus sampling with $p{=}0.9$, and maximum length of 256 new tokens.\nThe theoretical yield is $8 \\times {\\sim}1{,}000 \\times 5 \\approx 40{,}000$ texts; after removing generation failures, exact duplicates, and passages shorter than 50 tokens, 37{,}058 texts remain (Appendix~\\ref{app:dataset-stats}).\nFor classification, depths 2--4 are collapsed into the $2{+}$ class.\n\n\\subsection{Feature Extraction}\n\\label{sec:features}\n\nThe seven features are motivated by two complementary views of distributional drift.\nReference-model features capture how the text's token-level surprise distribution shifts relative to a fixed model; surface features capture how lexical diversity contracts under recursive generation.\nTogether, they span both the generative mechanism (what the model produces) and the surface manifestation (how the vocabulary changes); Figure~\\ref{fig:framework} provides an overview.\nThis two-pronged design is not post-hoc: it follows directly from the hypothesis that recursive generation induces a location shift in the NLL distribution (\\S\\ref{sec:results-differential}).\n\nWe extract seven distributional features per text, organized into two groups based on what they measure rather than how they are computed.\n\n\\paragraph{Reference-model features.}\nA held-out reference model (Pythia-410M, chosen to be smaller than all generators) computes per-token negative log-likelihood (NLL) for each text.\nAlthough Pythia-410M shares the GPT-NeoX architecture with two of the eight generators, cross-family reference model experiments (\\S\\ref{sec:results-differential}) confirm that depth features are not reference-specific (LOGO F1 varies by $\\leq$0.013 across Pythia, OLMo, and Qwen references).\nFrom the resulting NLL sequence, we extract five statistics:\n\\begin{itemize}[nosep,leftmargin=*]\n    \\item \\textbf{entropy\\_mean}\\footnote{We use ``entropy'' as shorthand for token-level negative log-likelihood under the reference model, following convention in prior detection work. These are point-wise NLL values, not Shannon entropy of the full distribution.}: mean token-level NLL, capturing the average predictability of the text under the reference model;\n    \\item \\textbf{entropy\\_std}: standard deviation of token-level NLL, measuring the spread of per-token surprise;\n    \\item \\textbf{entropy\\_max}: maximum token-level NLL, capturing the most surprising token;\n    \\item \\textbf{entropy\\_min}: minimum token-level NLL, capturing the most predictable token. As generation depth increases, the floor of token-level surprise drops, reflecting the model's increasing confidence on its own outputs.\n    Although entropy\\_min shows near-zero marginal impact in leave-one-feature-out analysis ($\\Delta$F1\\,=\\,+0.01\\,pp), we retain it for completeness of the NLL summary statistics (mean, std, max, min) and because removing it does not improve performance;\n    \\item \\textbf{tail\\_decay}: slope of the vocabulary-level averaged log-probability distribution in the mid-rank region (ranks 100--1000).\n    For each text, we compute the mean log-probability of each vocabulary token across all positions under the reference model, sort tokens in descending order of mean log-probability, and fit a linear regression to ranks 100--1000.\n    The slope captures how steeply the reference model's probability mass decays beyond high-probability tokens, characterizing the shape of the distribution tail.\n\\end{itemize}\n\n\\paragraph{Surface features.}\nTwo features capture lexical diversity without requiring a reference model:\n\\begin{itemize}[nosep,leftmargin=*]\n    \\item \\textbf{TTR}: type-token ratio (number of unique word types divided by total tokens);\n    \\item \\textbf{hapax\\_ratio}: proportion of words appearing exactly once (\\emph{hapax legomena}).\n\\end{itemize}\n\n\\paragraph{Feature complementarity.}\nThe grouping reflects an empirical pattern we term \\emph{differential depth response}: central-tendency and diversity features (entropy\\_mean, TTR, hapax\\_ratio) show substantial monotonic drift with generation depth ($|\\rho| = 0.60$--$0.63$); entropy\\_min and entropy\\_std show moderate drift ($|\\rho| = 0.17$--$0.41$); and shape features (entropy\\_max, tail\\_decay) remain near-stationary ($|\\rho| < 0.10$).\nThis differential behavior, consistent with recursive generation shifting the location of the NLL distribution while preserving distributional shape, motivates combining both feature types.\nAs shown in \\S\\ref{sec:results}, the full 7-feature set significantly outperforms either group alone.\n\n\\subsection{Evaluation Protocol}\n\\label{sec:evaluation}\n\n\\paragraph{Cross-validation.}\nTo evaluate generalization to unseen generators, we use \\textbf{Leave-One-Generator-Out (LOGO)} cross-validation: in each fold, one of the eight generators is held out for testing and the remaining seven provide training data.\nWe additionally report \\textbf{Leave-One-Family-Out (LOFO)} results, where an entire model family (e.g., all Qwen models) is held out, testing generalization across architectural lineages.\n\n\\paragraph{Classifier.}\nWe use XGBoost \\cite{xgboost} throughout ($n\\_\\text{estimators}{=}200$, $\\max\\_\\text{depth}{=}6$, learning rate $0.1$), with identical hyperparameters across all methods in Table~\\ref{tab:baselines}.\nLOGO F1 is stable across random seeds (std\\,$<$\\,0.001 over 5 seeds).\nAlternative classifiers and ordinal-specific methods (CORAL \\cite{coral_ordinal}, Frank-Hall \\cite{frank_hall_ordinal}) yield comparable performance (Appendix~\\ref{app:classifier}), confirming that discriminative power resides in the features.\n\n\\paragraph{Metrics and statistical testing.}\nThe primary metric is \\textbf{macro-averaged F1} over the three depth classes.\nWe report 95\\% confidence intervals via percentile bootstrap ($n{=}1{,}000$), McNemar tests for pairwise comparisons, and paired bootstrap for baseline comparisons.\nAll $p$-values are two-sided; Bonferroni correction is applied where multiple comparisons arise.\nFeature--depth correlations (\\S\\ref{sec:results-differential}) use class-balanced subsamples to control for depth-class imbalance.\n\n\\paragraph{Baselines.}\nWe compare the 7-feature ensemble against four single-score detection methods repurposed as depth predictors: Avg-LogProb, FastDetectGPT \\cite{fast_detectgpt}, Binoculars \\cite{binoculars}, and LD-Score \\cite{ld_score}.\nEach baseline score is used as a univariate feature in the same XGBoost framework under LOGO cross-validation, ensuring a controlled comparison.\n\n\\paragraph{Length confound control.}\nSince TTR and hapax\\_ratio are mechanically length-dependent, we verify depth signal is not a length artifact via length-matched subsampling that equalizes length distributions across depth classes (\\S\\ref{sec:results-classification}; Appendix~\\ref{app:length}).\n",
      "numLines": 97,
      "startLine": 1,
      "totalLines": 97
    }
  },
  "sourceToolAssistantUUID": "553aaf45-0063-412c-adc5-88d3d1982530",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/review_reviewer_2_3f564e41",
  "sessionId": "b64a1fb5-cc00-4ec5-a8b3-b55f8a4cf13d",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---


### Tool call

_source line 36 · 2026-05-17T17:19:53.207Z_

<details open><summary>🔧 Tool call — Read · `toolu_01KHwQz8Ub11NrbwVRZxjX4t`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/results.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c817b32a-ff19-4a1e-9edb-acb39e0ebb91",
  "isSidechain": false,
  "requestId": "req_011Cb8XMRGpRjUWH8BmPNN3N",
  "type": "assistant",
  "uuid": "d8431543-ad1b-4c8c-9b78-94297f492507",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/review_reviewer_2_3f564e41",
  "sessionId": "b64a1fb5-cc00-4ec5-a8b3-b55f8a4cf13d",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BN5w5R6jgmeJcv1zoXT7mM",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3104,
      "cache_creation_input_tokens": 2417,
      "cache_read_input_tokens": 30752,
      "output_tokens": 302,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2417,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3104,
          "output_tokens": 302,
          "cache_read_input_tokens": 30752,
          "cache_creation_input_tokens": 2417,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2417
          },
          "type": "message"
        }
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

_source line 37 · 2026-05-17T17:19:53.217Z_

<details><summary>↩ Tool result · `toolu_01KHwQz8Ub11NrbwVRZxjX4t`</summary>

```text
1	\section{Results}
2	\label{sec:results}
3	
4	\subsection{Depth Classification Performance}
5	\label{sec:results-classification}
6	
7	The 7-feature ensemble achieves 3-class LOGO F1\,=\,0.762 (95\% CI [0.758, 0.766]; $N$\,=\,37{,}058) across eight generators from five families (Table~\ref{tab:logo-results}).
8	Because gen-0 seeds are shared across generators (\S\ref{sec:generation}), the 3-class metric may carry upward bias from memorized gen-0 patterns; we therefore also report a leak-free binary metric (gen-1 vs.\ gen-2+): F1\,=\,0.694, CI [0.688, 0.700], which is unaffected by this sharing.
9	Per-generator binary F1 ranges from 0.633 (Mistral-7B) to 0.724 (Pythia-2.8B); the primary difficulty is distinguishing gen-1 from gen-2+ (Appendix~\ref{app:confusion}).
10	Larger generators show moderate degradation (Qwen3-8B: 0.692, Mistral-7B: 0.633) relative to the 0.694 average.
11	
12	\paragraph{Cross-model generalization.}
13	Cross-model chains (randomly selected generator per step) yield 3-class F1\,=\,0.809 and binary F1\,=\,0.764 under 5-fold CV,\footnote{Cross-model chains use the original five-generator subset (Pythia, OLMo, Qwen); Llama and Mistral were added later for single-generator evaluation.} confirming that depth signal persists when text passes through heterogeneous generators.
14	The higher cross-model performance relative to single-generator LOGO (3-class: 0.809 vs.\ 0.762) suggests that generator heterogeneity amplifies distributional shifts between depths, making each recursive step more distinct.
15	Under class balancing, macro F1 reaches 0.831 (per-class breakdown in Appendix~\ref{app:cross-model-detail}).
16	
17	Leave-one-family-out (LOFO) evaluation yields average binary F1\,=\,0.686, confirming transfer across architectural families.
18	A scale effect emerges: Pythia generators achieve the highest binary F1 (0.718--0.724), while larger models show degradation (Mistral-7B: 0.633), consistent with higher-capacity models compressing the feature margins DDR exploits.
19	The signal generalizes across text domains with variation (Appendix~\ref{app:domain}).
20	
21	\paragraph{Length confound control.}
22	Length-matched subsampling yields binary F1\,=\,0.724 (vs.\ 0.770 unmatched; $\Delta$\,=\,$-$0.046); a random-subsample control at equal $N$ (F1\,=\,0.767) confirms the drop reflects deconfounding, not sample-size reduction.
23	Length accounts for $\approx$6\% of discriminative performance (Appendix~\ref{app:length}).
24	
25	
26	\begin{table}[t]
27	\centering
28	\footnotesize
29	\resizebox{\columnwidth}{!}{%
30	\begin{tabular}{llcccc}
31	\toprule
32	\textbf{Model} & \textbf{Family} & \textbf{Params} & \textbf{3-cl F1} & \textbf{Bin F1} & \textbf{95\% CI} \\
33	\midrule
34	Pythia-2.8B     & Pythia  & 2.8B & 0.798 & \textbf{0.724} & [.707, .742] \\
35	Pythia-1B       & Pythia  & 1.0B & \textbf{0.806} & 0.718 & [.700, .735] \\
36	Qwen3-1.7B     & Qwen    & 1.7B & 0.772 & 0.709 & [.693, .726] \\
37	Llama-3.2-3B   & Llama   & 3.2B & 0.775 & 0.697 & [.680, .713] \\
38	OLMo-2-1B      & OLMo    & 1.5B & 0.781 & 0.695 & [.679, .711] \\
39	Qwen3-8B       & Qwen    & 8.2B & 0.714 & 0.692 & [.674, .708] \\
40	Qwen3-0.6B     & Qwen    & 0.6B & 0.780 & 0.691 & [.673, .709] \\
41	Mistral-7B     & Mistral & 7.0B & 0.682 & 0.633 & [.617, .648] \\
42	\midrule
43	\multicolumn{3}{l}{\textbf{Average (8-gen LOGO)}} & \textbf{0.762} & \textbf{0.694} & [.688, .700] \\
44	\bottomrule
45	\end{tabular}}
46	\caption{8-generator LOGO macro-F1 for the 7-feature ensemble (bootstrap 95\% CIs, $n$\,=\,1000). Binary F1 (gen-1 vs.\ gen-2+) is the primary metric. Note: 3-class F1 may carry upward bias from gen-0 seed sharing across generators; binary F1 is leak-free. Cross-model chains (Table~\ref{tab:cross-ref}) use sample-level CV without this issue.}
47	\label{tab:logo-results}
48	\end{table}
49	
50	\subsection{Differential Depth Response}
51	\label{sec:results-differential}
52	
53	Features exhibit \emph{differential depth response} (DDR): central-tendency and diversity measures drift monotonically with depth, while shape measures remain near-stationary, consistent with recursive generation inducing a location shift in the NLL distribution while preserving its functional form.
54	
55	\begin{figure}[t]
56	\centering
57	\includegraphics[width=\columnwidth]{fig1_differential_response.pdf}
58	\caption{Differential depth response: Spearman correlations between individual features and generation depth. Central-tendency and diversity features (hapax ratio, TTR, entropy mean) show substantial monotonic drift; entropy std ($|\rho|{=}0.17$) occupies an intermediate position; shape features (entropy max, tail decay) remain near-stationary ($|\rho| < 0.10$).}
59	\label{fig:feature-drift}
60	\end{figure}
61	
62	Pooled class-balanced Spearman correlations with depth confirm the split (Figure~\ref{fig:feature-drift}):
63	drifting features show substantial monotonic trends (hapax ratio $\rho = -0.63$, TTR $\rho = -0.61$, entropy mean $\rho = -0.60$),
64	while shape features remain near-stationary (tail decay $|\rho| = 0.04$); entropy std occupies an intermediate position ($|\rho| = 0.17$).
65	
66	\paragraph{Distributional shift quantification.}
67	Two-sample Kolmogorov--Smirnov tests between gen-1 and gen-2+ distributions isolate the recursive depth effect (excluding the initial human$\rightarrow$LLM transition): drifting features exhibit large distributional shifts (entropy mean KS\,=\,0.537, TTR\,=\,0.517, hapax ratio\,=\,0.516; all $p \approx 0$), while shape features show order-of-magnitude smaller shifts (entropy max KS\,=\,0.043, tail decay\,=\,0.052).
68	All seven features reach statistical significance after Bonferroni correction, but shape-feature KS statistics are ${\sim}10\times$ smaller than drifting features, supporting the ``approximately stationary'' characterization.
69	Entropy std occupies an intermediate position (KS\,=\,0.285), consistent with its borderline rank correlation.
70	Levene tests for variance homogeneity reject equal variance for all seven features ($p < 10^{-10}$), indicating that recursive generation alters spread as well as location, though the magnitude of variance change is substantially smaller for shape features (coefficient of variation shift $<$3\% for entropy max vs.\ $>$15\% for hapax ratio).
71	
72	\paragraph{Feature complementarity.}
73	Under 10-fold stratified CV, the full 7-feature set (F1\,=\,0.773) outperforms surface-only (F1\,=\,0.688) and reference-only (F1\,=\,0.713; McNemar $p \approx 0$; Table~\ref{tab:ablation}).
74	Reference-only yields higher binary F1 (0.833 vs.\ 0.695) since surface features introduce noise at the gen-1/gen-2+ boundary, but surface features are essential for 3-class gen-0 discrimination (Full 0.773 vs.\ Reference-only 0.713).
75	Permutation importance: hapax ratio (0.35), entropy mean (0.23), TTR (0.18); leave-one-feature-out confirms 6 of 7 features contribute positively (Appendix~\ref{app:lofo}).
76	
77	\paragraph{Cross-family reference models.}
78	Alternative references (OLMo-2-1B, Qwen3-0.6B) achieve comparable LOGO F1 (spread 0.013; Table~\ref{tab:cross-ref}), with consistently negative entropy drift, confirming DDR is a property of recursive generation.
79	
80	\paragraph{Temperature robustness.}
81	The method operates reliably within $t \in [0.5, 0.9]$: F1 varies by at most 1\,pp from the default $t{=}0.7$ across this range (Appendix~\ref{app:sampling-sensitivity}).
82	At $t{=}1.0$, performance degrades by ${\sim}6$\,pp as the primary depth signal collapses: entropy mean's Spearman correlation with depth drops from $\rho = -0.60$ to $\rho = -0.002$, indicating that high-temperature sampling injects sufficient token-level randomness to mask the systematic location shift that DDR exploits.
83	
84	\input{table4}
85	
86	\begin{table}[t]
87	\centering
88	\footnotesize
89	\begin{tabular}{lcc}
90	\toprule
91	\textbf{Feature set} & \textbf{F1} & \textbf{Top feature (imp.)} \\
92	\midrule
93	Full (7 features)     & 0.773 & hapax\_ratio (0.35) \\
94	Surface only (2)      & 0.688 & hapax\_ratio (0.41) \\
95	Reference only (5)    & 0.713 & entropy\_mean (0.27) \\
96	\bottomrule
97	\end{tabular}
98	\caption{Feature ablation (8-gen, 10-fold stratified CV, 3-class). Full $>$ surface (+8.5\,pp) and Full $>$ reference (+6.0\,pp) confirms complementarity.}
99	\label{tab:ablation}
100	\end{table}
101	
102	
103	\subsection{Comparison with Detection Baselines}
104	\label{sec:results-baselines}
105	
106	We repurpose four detection scores as ordinal depth predictors using the same XGBoost framework and LOGO splits (Table~\ref{tab:baselines}, Figure~\ref{fig:baseline-ci}).
107	
108	\begin{figure}[t]
109	\centering
110	\includegraphics[width=\columnwidth]{fig3_baseline_comparison.png}
111	\caption{LOGO binary F1 with 95\% bootstrap CIs. Per-generator variance is higher for single detectors than for the ensemble.}
112	\label{fig:baseline-ci}
113	\end{figure}
114	
115	\begin{table}[t]
116	\centering
117	\footnotesize
118	\begin{tabular}{lcccc}
119	\toprule
120	\textbf{Method} & \textbf{Feat.} & \textbf{3-cl F1} & \textbf{Bin F1} & \textbf{ms/text} \\
121	\midrule
122	4-det.\ + surface     & 6 & \textbf{0.795} & \textbf{0.708} & 22.8 \\
123	4-detector ens.\      & 4 & 0.785 & 0.700 & 22.8 \\
124	7-feature (ours)      & 7 & 0.774 & 0.705 & \textbf{9.7} \\
125	Avg-LogProb           & 1 & 0.707 & 0.673 & --- \\
126	FastDetectGPT         & 1 & 0.660 & 0.569 & --- \\
127	LD-Score              & 1 & 0.630 & 0.675 & --- \\
128	Binoculars            & 1 & 0.411 & 0.539 & --- \\
129	\bottomrule
130	\end{tabular}
131	\caption{Depth classification (8-gen pooled LOGO). All methods use XGBoost with $n_\text{estimators}{=}200$, $\max_\text{depth}{=}6$. Binary: gen-1 vs.\ gen-2+. Inference cost: 7-feature requires one 410M reference model (905\,MB); 4-det ensembles require two models totaling 1.4B parameters (2{,}868\,MB).}
132	\label{tab:baselines}
133	\end{table}
134	
135	Our 7-feature ensemble outperforms all individual baselines by 6--11\,pp in 3-class F1.
136	Multi-detector ensembles achieve moderately higher 3-class F1 (0.785--0.795 vs.\ 0.774) with indistinguishable binary performance ($\leq$0.3\,pp), but require 2.4$\times$ longer inference and 3.2$\times$ more GPU memory (two models, 1.4B parameters vs.\ our single 410M reference).
137	
138	
139	\subsection{Downstream Utility}
140	\label{sec:results-downstream}
141	
142	If depth fingerprinting reliably identifies recursive text, can it improve data curation?
143	Fine-tuning OLMo-2-0425-1B on five data variants (3 seeds each) yields two conclusions.
144	At equal sample count ($n$\,=\,3{,}951), depth-aware selection is practically equivalent to random subsampling (ppl 2.387 vs.\ 2.367; TOST $\pm$2\% relative margin, $p = 1.1 \times 10^{-4}$).
145	However, data quantity dominates: the full dataset ($n$\,=\,12{,}299, ppl\,=\,2.335) yields significantly lower perplexity than any depth-filtered subset, and TOST rejects equivalence at the same margin (Appendix~\ref{app:downstream}).
146	Depth composition per se does not determine training utility at fixed sample count.
147	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d8431543-ad1b-4c8c-9b78-94297f492507",
  "isSidechain": false,
  "promptId": "c6349ba0-ce02-4cbb-9474-95572d1cbd3f",
  "type": "user",
  "uuid": "31a5dfa5-a3bf-4939-90ec-cd02ed835254",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/results.tex",
      "content": "\\section{Results}\n\\label{sec:results}\n\n\\subsection{Depth Classification Performance}\n\\label{sec:results-classification}\n\nThe 7-feature ensemble achieves 3-class LOGO F1\\,=\\,0.762 (95\\% CI [0.758, 0.766]; $N$\\,=\\,37{,}058) across eight generators from five families (Table~\\ref{tab:logo-results}).\nBecause gen-0 seeds are shared across generators (\\S\\ref{sec:generation}), the 3-class metric may carry upward bias from memorized gen-0 patterns; we therefore also report a leak-free binary metric (gen-1 vs.\\ gen-2+): F1\\,=\\,0.694, CI [0.688, 0.700], which is unaffected by this sharing.\nPer-generator binary F1 ranges from 0.633 (Mistral-7B) to 0.724 (Pythia-2.8B); the primary difficulty is distinguishing gen-1 from gen-2+ (Appendix~\\ref{app:confusion}).\nLarger generators show moderate degradation (Qwen3-8B: 0.692, Mistral-7B: 0.633) relative to the 0.694 average.\n\n\\paragraph{Cross-model generalization.}\nCross-model chains (randomly selected generator per step) yield 3-class F1\\,=\\,0.809 and binary F1\\,=\\,0.764 under 5-fold CV,\\footnote{Cross-model chains use the original five-generator subset (Pythia, OLMo, Qwen); Llama and Mistral were added later for single-generator evaluation.} confirming that depth signal persists when text passes through heterogeneous generators.\nThe higher cross-model performance relative to single-generator LOGO (3-class: 0.809 vs.\\ 0.762) suggests that generator heterogeneity amplifies distributional shifts between depths, making each recursive step more distinct.\nUnder class balancing, macro F1 reaches 0.831 (per-class breakdown in Appendix~\\ref{app:cross-model-detail}).\n\nLeave-one-family-out (LOFO) evaluation yields average binary F1\\,=\\,0.686, confirming transfer across architectural families.\nA scale effect emerges: Pythia generators achieve the highest binary F1 (0.718--0.724), while larger models show degradation (Mistral-7B: 0.633), consistent with higher-capacity models compressing the feature margins DDR exploits.\nThe signal generalizes across text domains with variation (Appendix~\\ref{app:domain}).\n\n\\paragraph{Length confound control.}\nLength-matched subsampling yields binary F1\\,=\\,0.724 (vs.\\ 0.770 unmatched; $\\Delta$\\,=\\,$-$0.046); a random-subsample control at equal $N$ (F1\\,=\\,0.767) confirms the drop reflects deconfounding, not sample-size reduction.\nLength accounts for $\\approx$6\\% of discriminative performance (Appendix~\\ref{app:length}).\n\n\n\\begin{table}[t]\n\\centering\n\\footnotesize\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llcccc}\n\\toprule\n\\textbf{Model} & \\textbf{Family} & \\textbf{Params} & \\textbf{3-cl F1} & \\textbf{Bin F1} & \\textbf{95\\% CI} \\\\\n\\midrule\nPythia-2.8B     & Pythia  & 2.8B & 0.798 & \\textbf{0.724} & [.707, .742] \\\\\nPythia-1B       & Pythia  & 1.0B & \\textbf{0.806} & 0.718 & [.700, .735] \\\\\nQwen3-1.7B     & Qwen    & 1.7B & 0.772 & 0.709 & [.693, .726] \\\\\nLlama-3.2-3B   & Llama   & 3.2B & 0.775 & 0.697 & [.680, .713] \\\\\nOLMo-2-1B      & OLMo    & 1.5B & 0.781 & 0.695 & [.679, .711] \\\\\nQwen3-8B       & Qwen    & 8.2B & 0.714 & 0.692 & [.674, .708] \\\\\nQwen3-0.6B     & Qwen    & 0.6B & 0.780 & 0.691 & [.673, .709] \\\\\nMistral-7B     & Mistral & 7.0B & 0.682 & 0.633 & [.617, .648] \\\\\n\\midrule\n\\multicolumn{3}{l}{\\textbf{Average (8-gen LOGO)}} & \\textbf{0.762} & \\textbf{0.694} & [.688, .700] \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{8-generator LOGO macro-F1 for the 7-feature ensemble (bootstrap 95\\% CIs, $n$\\,=\\,1000). Binary F1 (gen-1 vs.\\ gen-2+) is the primary metric. Note: 3-class F1 may carry upward bias from gen-0 seed sharing across generators; binary F1 is leak-free. Cross-model chains (Table~\\ref{tab:cross-ref}) use sample-level CV without this issue.}\n\\label{tab:logo-results}\n\\end{table}\n\n\\subsection{Differential Depth Response}\n\\label{sec:results-differential}\n\nFeatures exhibit \\emph{differential depth response} (DDR): central-tendency and diversity measures drift monotonically with depth, while shape measures remain near-stationary, consistent with recursive generation inducing a location shift in the NLL distribution while preserving its functional form.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{fig1_differential_response.pdf}\n\\caption{Differential depth response: Spearman correlations between individual features and generation depth. Central-tendency and diversity features (hapax ratio, TTR, entropy mean) show substantial monotonic drift; entropy std ($|\\rho|{=}0.17$) occupies an intermediate position; shape features (entropy max, tail decay) remain near-stationary ($|\\rho| < 0.10$).}\n\\label{fig:feature-drift}\n\\end{figure}\n\nPooled class-balanced Spearman correlations with depth confirm the split (Figure~\\ref{fig:feature-drift}):\ndrifting features show substantial monotonic trends (hapax ratio $\\rho = -0.63$, TTR $\\rho = -0.61$, entropy mean $\\rho = -0.60$),\nwhile shape features remain near-stationary (tail decay $|\\rho| = 0.04$); entropy std occupies an intermediate position ($|\\rho| = 0.17$).\n\n\\paragraph{Distributional shift quantification.}\nTwo-sample Kolmogorov--Smirnov tests between gen-1 and gen-2+ distributions isolate the recursive depth effect (excluding the initial human$\\rightarrow$LLM transition): drifting features exhibit large distributional shifts (entropy mean KS\\,=\\,0.537, TTR\\,=\\,0.517, hapax ratio\\,=\\,0.516; all $p \\approx 0$), while shape features show order-of-magnitude smaller shifts (entropy max KS\\,=\\,0.043, tail decay\\,=\\,0.052).\nAll seven features reach statistical significance after Bonferroni correction, but shape-feature KS statistics are ${\\sim}10\\times$ smaller than drifting features, supporting the ``approximately stationary'' characterization.\nEntropy std occupies an intermediate position (KS\\,=\\,0.285), consistent with its borderline rank correlation.\nLevene tests for variance homogeneity reject equal variance for all seven features ($p < 10^{-10}$), indicating that recursive generation alters spread as well as location, though the magnitude of variance change is substantially smaller for shape features (coefficient of variation shift $<$3\\% for entropy max vs.\\ $>$15\\% for hapax ratio).\n\n\\paragraph{Feature complementarity.}\nUnder 10-fold stratified CV, the full 7-feature set (F1\\,=\\,0.773) outperforms surface-only (F1\\,=\\,0.688) and reference-only (F1\\,=\\,0.713; McNemar $p \\approx 0$; Table~\\ref{tab:ablation}).\nReference-only yields higher binary F1 (0.833 vs.\\ 0.695) since surface features introduce noise at the gen-1/gen-2+ boundary, but surface features are essential for 3-class gen-0 discrimination (Full 0.773 vs.\\ Reference-only 0.713).\nPermutation importance: hapax ratio (0.35), entropy mean (0.23), TTR (0.18); leave-one-feature-out confirms 6 of 7 features contribute positively (Appendix~\\ref{app:lofo}).\n\n\\paragraph{Cross-family reference models.}\nAlternative references (OLMo-2-1B, Qwen3-0.6B) achieve comparable LOGO F1 (spread 0.013; Table~\\ref{tab:cross-ref}), with consistently negative entropy drift, confirming DDR is a property of recursive generation.\n\n\\paragraph{Temperature robustness.}\nThe method operates reliably within $t \\in [0.5, 0.9]$: F1 varies by at most 1\\,pp from the default $t{=}0.7$ across this range (Appendix~\\ref{app:sampling-sensitivity}).\nAt $t{=}1.0$, performance degrades by ${\\sim}6$\\,pp as the primary depth signal collapses: entropy mean's Spearman correlation with depth drops from $\\rho = -0.60$ to $\\rho = -0.002$, indicating that high-temperature sampling injects sufficient token-level randomness to mask the systematic location shift that DDR exploits.\n\n\\input{table4}\n\n\\begin{table}[t]\n\\centering\n\\footnotesize\n\\begin{tabular}{lcc}\n\\toprule\n\\textbf{Feature set} & \\textbf{F1} & \\textbf{Top feature (imp.)} \\\\\n\\midrule\nFull (7 features)     & 0.773 & hapax\\_ratio (0.35) \\\\\nSurface only (2)      & 0.688 & hapax\\_ratio (0.41) \\\\\nReference only (5)    & 0.713 & entropy\\_mean (0.27) \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Feature ablation (8-gen, 10-fold stratified CV, 3-class). Full $>$ surface (+8.5\\,pp) and Full $>$ reference (+6.0\\,pp) confirms complementarity.}\n\\label{tab:ablation}\n\\end{table}\n\n\n\\subsection{Comparison with Detection Baselines}\n\\label{sec:results-baselines}\n\nWe repurpose four detection scores as ordinal depth predictors using the same XGBoost framework and LOGO splits (Table~\\ref{tab:baselines}, Figure~\\ref{fig:baseline-ci}).\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{fig3_baseline_comparison.png}\n\\caption{LOGO binary F1 with 95\\% bootstrap CIs. Per-generator variance is higher for single detectors than for the ensemble.}\n\\label{fig:baseline-ci}\n\\end{figure}\n\n\\begin{table}[t]\n\\centering\n\\footnotesize\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Method} & \\textbf{Feat.} & \\textbf{3-cl F1} & \\textbf{Bin F1} & \\textbf{ms/text} \\\\\n\\midrule\n4-det.\\ + surface     & 6 & \\textbf{0.795} & \\textbf{0.708} & 22.8 \\\\\n4-detector ens.\\      & 4 & 0.785 & 0.700 & 22.8 \\\\\n7-feature (ours)      & 7 & 0.774 & 0.705 & \\textbf{9.7} \\\\\nAvg-LogProb           & 1 & 0.707 & 0.673 & --- \\\\\nFastDetectGPT         & 1 & 0.660 & 0.569 & --- \\\\\nLD-Score              & 1 & 0.630 & 0.675 & --- \\\\\nBinoculars            & 1 & 0.411 & 0.539 & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Depth classification (8-gen pooled LOGO). All methods use XGBoost with $n_\\text{estimators}{=}200$, $\\max_\\text{depth}{=}6$. Binary: gen-1 vs.\\ gen-2+. Inference cost: 7-feature requires one 410M reference model (905\\,MB); 4-det ensembles require two models totaling 1.4B parameters (2{,}868\\,MB).}\n\\label{tab:baselines}\n\\end{table}\n\nOur 7-feature ensemble outperforms all individual baselines by 6--11\\,pp in 3-class F1.\nMulti-detector ensembles achieve moderately higher 3-class F1 (0.785--0.795 vs.\\ 0.774) with indistinguishable binary performance ($\\leq$0.3\\,pp), but require 2.4$\\times$ longer inference and 3.2$\\times$ more GPU memory (two models, 1.4B parameters vs.\\ our single 410M reference).\n\n\n\\subsection{Downstream Utility}\n\\label{sec:results-downstream}\n\nIf depth fingerprinting reliably identifies recursive text, can it improve data curation?\nFine-tuning OLMo-2-0425-1B on five data variants (3 seeds each) yields two conclusions.\nAt equal sample count ($n$\\,=\\,3{,}951), depth-aware selection is practically equivalent to random subsampling (ppl 2.387 vs.\\ 2.367; TOST $\\pm$2\\% relative margin, $p = 1.1 \\times 10^{-4}$).\nHowever, data quantity dominates: the full dataset ($n$\\,=\\,12{,}299, ppl\\,=\\,2.335) yields significantly lower perplexity than any depth-filtered subset, and TOST rejects equivalence at the same margin (Appendix~\\ref{app:downstream}).\nDepth composition per se does not determine training utility at fixed sample count.\n",
      "numLines": 147,
      "startLine": 1,
      "totalLines": 147
    }
  },
  "sourceToolAssistantUUID": "d8431543-ad1b-4c8c-9b78-94297f492507",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/review_reviewer_2_3f564e41",
  "sessionId": "b64a1fb5-cc00-4ec5-a8b3-b55f8a4cf13d",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---


### Tool call

_source line 38 · 2026-05-17T17:19:53.616Z_

<details open><summary>🔧 Tool call — Read · `toolu_018PwuSutJUvpbyPqGDHkJA2`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "31a5dfa5-a3bf-4939-90ec-cd02ed835254",
  "isSidechain": false,
  "requestId": "req_011Cb8XMRGpRjUWH8BmPNN3N",
  "type": "assistant",
  "uuid": "6f1eb37c-fb99-4668-92ba-70cdccfc4254",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/review_reviewer_2_3f564e41",
  "sessionId": "b64a1fb5-cc00-4ec5-a8b3-b55f8a4cf13d",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BN5w5R6jgmeJcv1zoXT7mM",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3104,
      "cache_creation_input_tokens": 2417,
      "cache_read_input_tokens": 30752,
      "output_tokens": 302,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2417,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3104,
          "output_tokens": 302,
          "cache_read_input_tokens": 30752,
          "cache_creation_input_tokens": 2417,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2417
          },
          "type": "message"
        }
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

_source line 39 · 2026-05-17T17:19:53.633Z_

```json
{
  "parentUuid": "8a30330f-3d19-4256-852d-f2d6e23cc856",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "af662828-474a-4395-8774-782212c9ed27",
  "timestamp": "2026-05-17T17:19:53.633Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/review_reviewer_2_3f564e41",
  "sessionId": "b64a1fb5-cc00-4ec5-a8b3-b55f8a4cf13d",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

---


### Runtime record

_source line 40_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[Round 1 审稿请求]: 你负责**新颖性 + 完整性 + Related Work + 格式**。  ## Venue 信息 - **目标**: EMNLP 2026（ARR May 2026 cycle） - **截止日期**: 2026-05-25 - **页数限制**: Long paper 正文 8 页（不含 limitations/ethics/references） - **模…",
  "leafUuid": "af662828-474a-4395-8774-782212c9ed27",
  "sessionId": "b64a1fb5-cc00-4ec5-a8b3-b55f8a4cf13d"
}
```

---


### Runtime record

_source line 41_

```json
{
  "type": "ai-title",
  "aiTitle": "Review depth fingerprinting paper for EMNLP 2026",
  "sessionId": "b64a1fb5-cc00-4ec5-a8b3-b55f8a4cf13d"
}
```

---


### Assistant

_source line 42 · 2026-05-17T17:19:57.572Z_

<details><summary>Logged reasoning block</summary>

```text
Let me continue reading the conclusion, limitations, ethics sections, and also check the references.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "af662828-474a-4395-8774-782212c9ed27",
  "isSidechain": false,
  "requestId": "req_011Cb8XMzJvMexo6ZSdrGZTi",
  "type": "assistant",
  "uuid": "25711931-32ac-464c-b5ed-b70dbe122530",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/review_reviewer_2_3f564e41",
  "sessionId": "b64a1fb5-cc00-4ec5-a8b3-b55f8a4cf13d",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YBs1xfudFTNskwbqPjkRsC",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11606,
      "cache_read_input_tokens": 33169,
      "output_tokens": 360,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11606,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 360,
          "cache_read_input_tokens": 33169,
          "cache_creation_input_tokens": 11606,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11606
          },
          "type": "message"
        }
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

_source line 43 · 2026-05-17T17:19:59.088Z_

<details open><summary>🔧 Tool call — Read · `toolu_011Vgb5Cmx2XDgC5Q9hEN9L6`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "25711931-32ac-464c-b5ed-b70dbe122530",
  "isSidechain": false,
  "requestId": "req_011Cb8XMzJvMexo6ZSdrGZTi",
  "type": "assistant",
  "uuid": "0cd3bfaa-c2ea-4d4f-b49b-95903e5516b5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/review_reviewer_2_3f564e41",
  "sessionId": "b64a1fb5-cc00-4ec5-a8b3-b55f8a4cf13d",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YBs1xfudFTNskwbqPjkRsC",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11606,
      "cache_read_input_tokens": 33169,
      "output_tokens": 360,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11606,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 360,
          "cache_read_input_tokens": 33169,
          "cache_creation_input_tokens": 11606,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11606
          },
          "type": "message"
        }
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

_source line 44 · 2026-05-17T17:19:59.100Z_

<details><summary>↩ Tool result · `toolu_011Vgb5Cmx2XDgC5Q9hEN9L6`</summary>

```text
1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	We introduced generation depth classification and documented a differential depth response across eight base-model generators from five families: recursive generation is consistent with a systematic location shift in the token-level NLL distribution that preserves distributional shape, and this structured drift is detectable with a lightweight 7-feature ensemble (binary F1\,=\,0.764 on cross-model chains, 0.694 under LOGO; 3-class: 0.809 and 0.762, respectively).
5	A TOST equivalence test confirms that depth-aware data curation yields training utility equivalent to random subsampling ($\pm$2\%, $p < 0.001$) within chains of $\leq$4 generations as measured by perplexity, indicating that detectability does not entail downstream perplexity degradation.
6	
7	Two boundaries define the scope: instruction tuning compresses the distributional variation that fingerprinting exploits, and frontier-scale models (70B+) may further compress feature margins.
8	All code, data, and trained models will be released upon publication.
9	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0cd3bfaa-c2ea-4d4f-b49b-95903e5516b5",
  "isSidechain": false,
  "promptId": "c6349ba0-ce02-4cbb-9474-95572d1cbd3f",
  "type": "user",
  "uuid": "2f5bc44e-e600-428d-b299-6297a2717f2b",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/conclusion.tex",
      "content": "\\section{Conclusion}\n\\label{sec:conclusion}\n\nWe introduced generation depth classification and documented a differential depth response across eight base-model generators from five families: recursive generation is consistent with a systematic location shift in the token-level NLL distribution that preserves distributional shape, and this structured drift is detectable with a lightweight 7-feature ensemble (binary F1\\,=\\,0.764 on cross-model chains, 0.694 under LOGO; 3-class: 0.809 and 0.762, respectively).\nA TOST equivalence test confirms that depth-aware data curation yields training utility equivalent to random subsampling ($\\pm$2\\%, $p < 0.001$) within chains of $\\leq$4 generations as measured by perplexity, indicating that detectability does not entail downstream perplexity degradation.\n\nTwo boundaries define the scope: instruction tuning compresses the distributional variation that fingerprinting exploits, and frontier-scale models (70B+) may further compress feature margins.\nAll code, data, and trained models will be released upon publication.\n",
      "numLines": 9,
      "startLine": 1,
      "totalLines": 9
    }
  },
  "sourceToolAssistantUUID": "0cd3bfaa-c2ea-4d4f-b49b-95903e5516b5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/review_reviewer_2_3f564e41",
  "sessionId": "b64a1fb5-cc00-4ec5-a8b3-b55f8a4cf13d",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---


### Tool result

_source line 45 · 2026-05-17T17:20:01.322Z_

<details><summary>↩ Tool result · `toolu_01LUsiPpDXViaPrgnru8YNuz`</summary>

```text
1	% ===== Detection =====
2	
3	@inproceedings{detectgpt,
4	  title = {{DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature}},
5	  author = {Mitchell, Eric and Lee, Yoonho and Khazatsky, Alexander and Manning, Christopher D. and Finn, Chelsea},
6	  booktitle = {Proceedings of the International Conference on Machine Learning},
7	  year = {2023},
8	}
9	
10	@inproceedings{gltr,
11	  title = {{GLTR: Statistical Detection and Visualization of Generated Text}},
12	  author = {Gehrmann, Sebastian and Strobelt, Hendrik and Rush, Alexander M.},
13	  booktitle = {Proceedings of the Annual Meeting of the Association for Computational Linguistics: System Demonstrations},
14	  year = {2019},
15	}
16	
17	@inproceedings{dna_gpt,
18	  title = {{DNA-GPT: Divergent N-Gram Analysis for Training-Free Detection of GPT-Generated Text}},
19	  author = {Yang, Xianjun and Cheng, Wei and Wu, Yue and Petzold, Linda and Wang, William Yang and Chen, Haifeng},
20	  booktitle = {Proceedings of the International Conference on Learning Representations},
21	  year = {2024},
22	}
23	
24	@inproceedings{binoculars,
25	  title = {{Spotting LLMs With Binoculars: Zero-Shot Detection of Machine-Generated Text}},
26	  author = {Hans, Abhimanyu and Schwarzschild, Avi and Cherepanova, Valeriia and Kazemi, Hamid and Saha, Aniruddha and Goldblum, Micah and Geiping, Jonas and Goldstein, Tom},
27	  booktitle = {Proceedings of the International Conference on Machine Learning},
28	  year = {2024},
29	}
30	
31	@inproceedings{fast_detectgpt,
32	  title = {{Fast-DetectGPT: Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature}},
33	  author = {Bao, Guangsheng and Zhao, Yanbin and Teng, Zhiyang and Yang, Linyi and Zhang, Yue},
34	  booktitle = {Proceedings of the International Conference on Learning Representations},
35	  year = {2024},
36	}
37	
38	@article{ld_score,
39	  title = {{Beyond Perplexity: Character Distribution Signatures and the MDTA Benchmark for AI Text Detection}},
40	  author = {Narayanasamy, Priyadarshan and Agrawal, Swastik and Faber, Klint and Alam, Fardina Fathmiul},
41	  journal = {arXiv preprint arXiv:2605.01647},
42	  year = {2026},
43	}
44	
45	@inproceedings{intrinsic_dimension,
46	  title = {{Intrinsic Dimension Estimation for Robust Detection of AI-Generated Texts}},
47	  author = {Tulchinskii, Eduard and Kuznetsov, Kristian and Kushnareva, Laida and Cherniavskii, Daniil and Nikolenko, Sergey and Burnaev, Evgeny and Barannikov, Serguei and Piontkovskaya, Irina},
48	  booktitle = {Advances in Neural Information Processing Systems},
49	  year = {2023},
50	}
51	
52	@article{diveye,
53	  title = {{Diversity Boosts AI-Generated Text Detection}},
54	  author = {Basani, Advik Raj and Chen, Pin-Yu},
55	  journal = {Transactions on Machine Learning Research},
56	  year = {2026},
57	}
58	
59	@article{generator_barrier,
60	  title = {{Breaking the Generator Barrier: Disentangled Representation for Generalizable AI-Text Detection}},
61	  author = {Pu, Xiao and Cheng, Zepeng and Yuan, Lin and Wu, Yu and Bi, Xiuli},
62	  journal = {arXiv preprint arXiv:2604.13692},
63	  year = {2026},
64	}
65	
66	@article{feat_aug_transformer,
67	  title = {{Feature-Augmented Transformers for Robust AI-Text Detection Across Domains and Generators}},
68	  author = {Mady, Mohamed and Reschke, Johannes and Schuller, Bj{\"o}rn},
69	  journal = {arXiv preprint arXiv:2605.03969},
70	  year = {2026},
71	}
72	
73	@article{reliable_detection,
74	  title = {{Can AI-Generated Text be Reliably Detected? Stress Testing AI Text Detectors Under Various Attacks}},
75	  author = {Sadasivan, Vinu Sankar and Kumar, Aounon and Balasubramanian, Sriram and Wang, Wenxiao and Feizi, Soheil},
76	  journal = {Transactions on Machine Learning Research},
77	  year = {2025},
78	  url = {https://openreview.net/forum?id=OOgsAZdFOt},
79	}
80	
81	@inproceedings{paraphrase_evades,
82	  title = {{Paraphrasing Evades Detectors of AI-Generated Text, but Retrieval is an Effective Defense}},
83	  author = {Krishna, Kalpesh and Song, Yixiao and Karpinska, Marzena and Wieting, John and Iyyer, Mohit},
84	  booktitle = {Advances in Neural Information Processing Systems},
85	  year = {2023},
86	}
87	
88	@inproceedings{detection_possibilities,
89	  title = {{Position: On the Possibilities of AI-Generated Text Detection}},
90	  author = {Chakraborty, Souradip and Bedi, Amrit Singh and Zhu, Sicheng and An, Bang and Manocha, Dinesh and Huang, Furong},
91	  booktitle = {Proceedings of the International Conference on Machine Learning},
92	  year = {2024},
93	}
94	
95	@inproceedings{grover,
96	  title = {{Defending Against Neural Fake News}},
97	  author = {Zellers, Rowan and Holtzman, Ari and Rashkin, Hannah and Bisk, Yonatan and Farhadi, Ali and Roesner, Franziska and Choi, Yejin},
98	  booktitle = {Advances in Neural Information Processing Systems},
99	  year = {2019},
100	}
101	
102	@article{release_strategies,
103	  title = {{Release Strategies and the Social Impacts of Language Models}},
104	  author = {Solaiman, Irene and Brundage, Miles and Clark, Jack and Askell, Amanda and Herbert-Voss, Ariel and Wu, Jeff and Radford, Alec and Krueger, Gretchen and Kim, Jong Wook and Kreps, Sarah and McCain, Miles and Newhouse, Alex and Blazakis, Jason and McGuffie, Kris and Wang, Jasmine},
105	  journal = {arXiv preprint arXiv:1908.09203},
106	  year = {2019},
107	}
108	
109	@inproceedings{beyond_binary,
110	  title = {{Beyond Binary: Towards Fine-Grained LLM-Generated Text Detection via Role Recognition and Involvement Measurement}},
111	  author = {Cheng, Zihao and Zhou, Li and Jiang, Feng and Wang, Benyou and Li, Haizhou},
112	  booktitle = {Proceedings of the ACM Web Conference},
113	  year = {2025},
114	}
115	
116	@inproceedings{semeval2024_task8,
117	  title = {{SemEval-2024 Task 8: Multidomain, Multimodel and Multilingual Machine-Generated Text Detection}},
118	  author = {Wang, Yuxia and Mansurov, Jonibek and Ivanov, Petar and Su, Jinyan and Shelmanov, Artem and Tsvigun, Akim and Afzal, Osama Mohammed and Mahmoud, Tarek and Puccetti, Giovanni and Arnold, Thomas and Whitehouse, Chenxi and Aji, Alham Fikri and Habash, Nizar and Gurevych, Iryna and Nakov, Preslav},
119	  booktitle = {Proceedings of the International Workshop on Semantic Evaluation},
120	  year = {2024},
121	}
122	
123	% ===== Model Collapse =====
124	
125	@inproceedings{self_consuming_mad,
126	  title = {{Self-Consuming Generative Models Go MAD}},
127	  author = {Alemohammad, Sina and Casco-Rodriguez, Josue and Luzi, Lorenzo and Humayun, Ahmed Imtiaz and Babaei, Hossein and LeJeune, Daniel and Siahkoohi, Ali and Baraniuk, Richard G.},
128	  booktitle = {Proceedings of the International Conference on Learning Representations},
129	  year = {2024},
130	}
131	
132	@article{curse_of_recursion,
133	  title = {{AI models collapse when trained on recursively generated data}},
134	  author = {Shumailov, Ilia and Shumaylov, Zakhar and Zhao, Yiren and Papernot, Nicolas and Anderson, Ross and Gal, Yarin},
135	  journal = {Nature},
136	  volume = {631},
137	  pages = {755--759},
138	  year = {2024},
139	}
140	
141	@inproceedings{strong_model_collapse,
142	  title = {{Strong Model Collapse}},
143	  author = {Dohmatob, Elvis and Feng, Yunzhen and Subramonian, Arjun and Kempe, Julia},
144	  booktitle = {Proceedings of the International Conference on Learning Representations},
145	  year = {2025},
146	}
147	
148	@inproceedings{model_collapse_avoidable,
149	  title = {{Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data}},
150	  author = {Gerstgrasser, Matthias and Schaeffer, Rylan and Dey, Apratim and Rafailov, Rafael and Sleight, Henry and Hughes, John and Korbak, Tomasz and Agrawal, Rajashree and Pai, Dhruv and Gromov, Andrey and Roberts, Daniel A. and Yang, Diyi and Donoho, David L. and Koyejo, Sanmi},
151	  booktitle = {Proceedings of the First Conference on Language Modeling (COLM)},
152	  year = {2024},
153	}
154	
155	% ===== Fine-tuning =====
156	
157	@inproceedings{qlora,
158	  title = {{QLoRA: Efficient Finetuning of Quantized Language Models}},
159	  author = {Dettmers, Tim and Pagnoni, Artidoro and Holtzman, Ari and Zettlemoyer, Luke},
160	  booktitle = {Advances in Neural Information Processing Systems},
161	  year = {2023},
162	}
163	
164	% ===== Data Quality =====
165	
166	@inproceedings{fineweb,
167	  title = {{The FineWeb Datasets: Decanting the Web for the Finest Text Data at Scale}},
168	  author = {Penedo, Guilherme and Kydl{\'\i}{\v{c}}ek, Hynek and Ben Allal, Loubna and Lozhkov, Anton and Mitchell, Margaret and Raffel, Colin and Von Werra, Leandro and Wolf, Thomas},
169	  booktitle = {Advances in Neural Information Processing Systems: Datasets and Benchmarks Track},
170	  year = {2024},
171	}
172	
173	@inproceedings{dolma,
174	  title = {{Dolma: an Open Corpus of Three Trillion Tokens for Language Model Pretraining Research}},
175	  author = {Soldaini, Luca and Kinney, Rodney and Bhagia, Akshita and Schwenk, Dustin and Atkinson, David and Authur, Russell and Bogin, Ben and Chandu, Khyathi and Dumas, Jennifer and Elazar, Yanai and Hofmann, Valentin and Jha, Ananya Harsh and Kumar, Sachin and Lucy, Li and Lyu, Xinxi and Lambert, Nathan and Magnusson, Ian and Morrison, Jacob and Muennighoff, Niklas and Naik, Aakanksha and Nam, Crystal and Peters, Matthew E. and Ravichander, Abhilasha and Richardson, Kyle and Shen, Zejiang and Strubell, Emma and Subramani, Nishant and Tafjord, Oyvind and Walsh, Evan Pete and Zettlemoyer, Luke and Smith, Noah A. and Hajishirzi, Hannaneh and Beltagy, Iz and Groeneveld, Dirk and Dodge, Jesse and Lo, Kyle},
176	  booktitle = {Proceedings of the Annual Meeting of the Association for Computational Linguistics},
177	  year = {2024},
178	}
179	
180	@inproceedings{dsir,
181	  title = {{Data Selection for Language Models via Importance Resampling}},
182	  author = {Xie, Sang Michael and Santurkar, Shibani and Ma, Tengyu and Liang, Percy},
183	  booktitle = {Advances in Neural Information Processing Systems},
184	  year = {2023},
185	}
186	
187	@inproceedings{qurating,
188	  title = {{QuRating: Selecting High-Quality Data for Training Language Models}},
189	  author = {Wettig, Alexander and Gupta, Aatmik and Malik, Saumya and Chen, Danqi},
190	  booktitle = {Proceedings of the International Conference on Machine Learning},
191	  year = {2024},
192	}
193	
194	@inproceedings{ccnet,
195	  title = {{CCNet: Extracting High Quality Monolingual Datasets from Web Crawl Data}},
196	  author = {Wenzek, Guillaume and Lachaux, Marie-Anne and Conneau, Alexis and Chaudhary, Vishrav and Guzm{\'a}n, Francisco and Joulin, Armand and Grave, Edouard},
197	  booktitle = {Proceedings of the Language Resources and Evaluation Conference},
198	  year = {2020},
199	}
200	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "71b11de3-f88d-49a8-bab5-ec87c6ec8995",
  "isSidechain": false,
  "promptId": "c6349ba0-ce02-4cbb-9474-95572d1cbd3f",
  "type": "user",
  "uuid": "36360c78-5fa3-45a6-a83a-4d9ae002a948",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/references.bib",
      "content": "% ===== Detection =====\n\n@inproceedings{detectgpt,\n  title = {{DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature}},\n  author = {Mitchell, Eric and Lee, Yoonho and Khazatsky, Alexander and Manning, Christopher D. and Finn, Chelsea},\n  booktitle = {Proceedings of the International Conference on Machine Learning},\n  year = {2023},\n}\n\n@inproceedings{gltr,\n  title = {{GLTR: Statistical Detection and Visualization of Generated Text}},\n  author = {Gehrmann, Sebastian and Strobelt, Hendrik and Rush, Alexander M.},\n  booktitle = {Proceedings of the Annual Meeting of the Association for Computational Linguistics: System Demonstrations},\n  year = {2019},\n}\n\n@inproceedings{dna_gpt,\n  title = {{DNA-GPT: Divergent N-Gram Analysis for Training-Free Detection of GPT-Generated Text}},\n  author = {Yang, Xianjun and Cheng, Wei and Wu, Yue and Petzold, Linda and Wang, William Yang and Chen, Haifeng},\n  booktitle = {Proceedings of the International Conference on Learning Representations},\n  year = {2024},\n}\n\n@inproceedings{binoculars,\n  title = {{Spotting LLMs With Binoculars: Zero-Shot Detection of Machine-Generated Text}},\n  author = {Hans, Abhimanyu and Schwarzschild, Avi and Cherepanova, Valeriia and Kazemi, Hamid and Saha, Aniruddha and Goldblum, Micah and Geiping, Jonas and Goldstein, Tom},\n  booktitle = {Proceedings of the International Conference on Machine Learning},\n  year = {2024},\n}\n\n@inproceedings{fast_detectgpt,\n  title = {{Fast-DetectGPT: Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature}},\n  author = {Bao, Guangsheng and Zhao, Yanbin and Teng, Zhiyang and Yang, Linyi and Zhang, Yue},\n  booktitle = {Proceedings of the International Conference on Learning Representations},\n  year = {2024},\n}\n\n@article{ld_score,\n  title = {{Beyond Perplexity: Character Distribution Signatures and the MDTA Benchmark for AI Text Detection}},\n  author = {Narayanasamy, Priyadarshan and Agrawal, Swastik and Faber, Klint and Alam, Fardina Fathmiul},\n  journal = {arXiv preprint arXiv:2605.01647},\n  year = {2026},\n}\n\n@inproceedings{intrinsic_dimension,\n  title = {{Intrinsic Dimension Estimation for Robust Detection of AI-Generated Texts}},\n  author = {Tulchinskii, Eduard and Kuznetsov, Kristian and Kushnareva, Laida and Cherniavskii, Daniil and Nikolenko, Sergey and Burnaev, Evgeny and Barannikov, Serguei and Piontkovskaya, Irina},\n  booktitle = {Advances in Neural Information Processing Systems},\n  year = {2023},\n}\n\n@article{diveye,\n  title = {{Diversity Boosts AI-Generated Text Detection}},\n  author = {Basani, Advik Raj and Chen, Pin-Yu},\n  journal = {Transactions on Machine Learning Research},\n  year = {2026},\n}\n\n@article{generator_barrier,\n  title = {{Breaking the Generator Barrier: Disentangled Representation for Generalizable AI-Text Detection}},\n  author = {Pu, Xiao and Cheng, Zepeng and Yuan, Lin and Wu, Yu and Bi, Xiuli},\n  journal = {arXiv preprint arXiv:2604.13692},\n  year = {2026},\n}\n\n@article{feat_aug_transformer,\n  title = {{Feature-Augmented Transformers for Robust AI-Text Detection Across Domains and Generators}},\n  author = {Mady, Mohamed and Reschke, Johannes and Schuller, Bj{\\\"o}rn},\n  journal = {arXiv preprint arXiv:2605.03969},\n  year = {2026},\n}\n\n@article{reliable_detection,\n  title = {{Can AI-Generated Text be Reliably Detected? Stress Testing AI Text Detectors Under Various Attacks}},\n  author = {Sadasivan, Vinu Sankar and Kumar, Aounon and Balasubramanian, Sriram and Wang, Wenxiao and Feizi, Soheil},\n  journal = {Transactions on Machine Learning Research},\n  year = {2025},\n  url = {https://openreview.net/forum?id=OOgsAZdFOt},\n}\n\n@inproceedings{paraphrase_evades,\n  title = {{Paraphrasing Evades Detectors of AI-Generated Text, but Retrieval is an Effective Defense}},\n  author = {Krishna, Kalpesh and Song, Yixiao and Karpinska, Marzena and Wieting, John and Iyyer, Mohit},\n  booktitle = {Advances in Neural Information Processing Systems},\n  year = {2023},\n}\n\n@inproceedings{detection_possibilities,\n  title = {{Position: On the Possibilities of AI-Generated Text Detection}},\n  author = {Chakraborty, Souradip and Bedi, Amrit Singh and Zhu, Sicheng and An, Bang and Manocha, Dinesh and Huang, Furong},\n  booktitle = {Proceedings of the International Conference on Machine Learning},\n  year = {2024},\n}\n\n@inproceedings{grover,\n  title = {{Defending Against Neural Fake News}},\n  author = {Zellers, Rowan and Holtzman, Ari and Rashkin, Hannah and Bisk, Yonatan and Farhadi, Ali and Roesner, Franziska and Choi, Yejin},\n  booktitle = {Advances in Neural Information Processing Systems},\n  year = {2019},\n}\n\n@article{release_strategies,\n  title = {{Release Strategies and the Social Impacts of Language Models}},\n  author = {Solaiman, Irene and Brundage, Miles and Clark, Jack and Askell, Amanda and Herbert-Voss, Ariel and Wu, Jeff and Radford, Alec and Krueger, Gretchen and Kim, Jong Wook and Kreps, Sarah and McCain, Miles and Newhouse, Alex and Blazakis, Jason and McGuffie, Kris and Wang, Jasmine},\n  journal = {arXiv preprint arXiv:1908.09203},\n  year = {2019},\n}\n\n@inproceedings{beyond_binary,\n  title = {{Beyond Binary: Towards Fine-Grained LLM-Generated Text Detection via Role Recognition and Involvement Measurement}},\n  author = {Cheng, Zihao and Zhou, Li and Jiang, Feng and Wang, Benyou and Li, Haizhou},\n  booktitle = {Proceedings of the ACM Web Conference},\n  year = {2025},\n}\n\n@inproceedings{semeval2024_task8,\n  title = {{SemEval-2024 Task 8: Multidomain, Multimodel and Multilingual Machine-Generated Text Detection}},\n  author = {Wang, Yuxia and Mansurov, Jonibek and Ivanov, Petar and Su, Jinyan and Shelmanov, Artem and Tsvigun, Akim and Afzal, Osama Mohammed and Mahmoud, Tarek and Puccetti, Giovanni and Arnold, Thomas and Whitehouse, Chenxi and Aji, Alham Fikri and Habash, Nizar and Gurevych, Iryna and Nakov, Preslav},\n  booktitle = {Proceedings of the International Workshop on Semantic Evaluation},\n  year = {2024},\n}\n\n% ===== Model Collapse =====\n\n@inproceedings{self_consuming_mad,\n  title = {{Self-Consuming Generative Models Go MAD}},\n  author = {Alemohammad, Sina and Casco-Rodriguez, Josue and Luzi, Lorenzo and Humayun, Ahmed Imtiaz and Babaei, Hossein and LeJeune, Daniel and Siahkoohi, Ali and Baraniuk, Richard G.},\n  booktitle = {Proceedings of the International Conference on Learning Representations},\n  year = {2024},\n}\n\n@article{curse_of_recursion,\n  title = {{AI models collapse when trained on recursively generated data}},\n  author = {Shumailov, Ilia and Shumaylov, Zakhar and Zhao, Yiren and Papernot, Nicolas and Anderson, Ross and Gal, Yarin},\n  journal = {Nature},\n  volume = {631},\n  pages = {755--759},\n  year = {2024},\n}\n\n@inproceedings{strong_model_collapse,\n  title = {{Strong Model Collapse}},\n  author = {Dohmatob, Elvis and Feng, Yunzhen and Subramonian, Arjun and Kempe, Julia},\n  booktitle = {Proceedings of the International Conference on Learning Representations},\n  year = {2025},\n}\n\n@inproceedings{model_collapse_avoidable,\n  title = {{Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data}},\n  author = {Gerstgrasser, Matthias and Schaeffer, Rylan and Dey, Apratim and Rafailov, Rafael and Sleight, Henry and Hughes, John and Korbak, Tomasz and Agrawal, Rajashree and Pai, Dhruv and Gromov, Andrey and Roberts, Daniel A. and Yang, Diyi and Donoho, David L. and Koyejo, Sanmi},\n  booktitle = {Proceedings of the First Conference on Language Modeling (COLM)},\n  year = {2024},\n}\n\n% ===== Fine-tuning =====\n\n@inproceedings{qlora,\n  title = {{QLoRA: Efficient Finetuning of Quantized Language Models}},\n  author = {Dettmers, Tim and Pagnoni, Artidoro and Holtzman, Ari and Zettlemoyer, Luke},\n  booktitle = {Advances in Neural Information Processing Systems},\n  year = {2023},\n}\n\n% ===== Data Quality =====\n\n@inproceedings{fineweb,\n  title = {{The FineWeb Datasets: Decanting the Web for the Finest Text Data at Scale}},\n  author = {Penedo, Guilherme and Kydl{\\'\\i}{\\v{c}}ek, Hynek and Ben Allal, Loubna and Lozhkov, Anton and Mitchell, Margaret and Raffel, Colin and Von Werra, Leandro and Wolf, Thomas},\n  booktitle = {Advances in Neural Information Processing Systems: Datasets and Benchmarks Track},\n  year = {2024},\n}\n\n@inproceedings{dolma,\n  title = {{Dolma: an Open Corpus of Three Trillion Tokens for Language Model Pretraining Research}},\n  author = {Soldaini, Luca and Kinney, Rodney and Bhagia, Akshita and Schwenk, Dustin and Atkinson, David and Authur, Russell and Bogin, Ben and Chandu, Khyathi and Dumas, Jennifer and Elazar, Yanai and Hofmann, Valentin and Jha, Ananya Harsh and Kumar, Sachin and Lucy, Li and Lyu, Xinxi and Lambert, Nathan and Magnusson, Ian and Morrison, Jacob and Muennighoff, Niklas and Naik, Aakanksha and Nam, Crystal and Peters, Matthew E. and Ravichander, Abhilasha and Richardson, Kyle and Shen, Zejiang and Strubell, Emma and Subramani, Nishant and Tafjord, Oyvind and Walsh, Evan Pete and Zettlemoyer, Luke and Smith, Noah A. and Hajishirzi, Hannaneh and Beltagy, Iz and Groeneveld, Dirk and Dodge, Jesse and Lo, Kyle},\n  booktitle = {Proceedings of the Annual Meeting of the Association for Computational Linguistics},\n  year = {2024},\n}\n\n@inproceedings{dsir,\n  title = {{Data Selection for Language Models via Importance Resampling}},\n  author = {Xie, Sang Michael and Santurkar, Shibani and Ma, Tengyu and Liang, Percy},\n  booktitle = {Advances in Neural Information Processing Systems},\n  year = {2023},\n}\n\n@inproceedings{qurating,\n  title = {{QuRating: Selecting High-Quality Data for Training Language Models}},\n  author = {Wettig, Alexander and Gupta, Aatmik and Malik, Saumya and Chen, Danqi},\n  booktitle = {Proceedings of the International Conference on Machine Learning},\n  year = {2024},\n}\n\n@inproceedings{ccnet,\n  title = {{CCNet: Extracting High Quality Monolingual Datasets from Web Crawl Data}},\n  author = {Wenzek, Guillaume and Lachaux, Marie-Anne and Conneau, Alexis and Chaudhary, Vishrav and Guzm{\\'a}n, Francisco and Joulin, Armand and Grave, Edouard},\n  booktitle = {Proceedings of the Language Resources and Evaluation Conference},\n  year = {2020},\n}\n",
      "numLines": 200,
      "startLine": 1,
      "totalLines": 447
    }
  },
  "sourceToolAssistantUUID": "71b11de3-f88d-49a8-bab5-ec87c6ec8995",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/review_reviewer_2_3f564e41",
  "sessionId": "b64a1fb5-cc00-4ec5-a8b3-b55f8a4cf13d",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---


### Tool call

_source line 46 · 2026-05-17T17:20:00.104Z_

<details open><summary>🔧 Tool call — Read · `toolu_0188FB7fHAi83MjJ6zRNiFMP`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2f5bc44e-e600-428d-b299-6297a2717f2b",
  "isSidechain": false,
  "requestId": "req_011Cb8XMzJvMexo6ZSdrGZTi",
  "type": "assistant",
  "uuid": "7c75de69-a79a-4123-91d7-79c6e10d8613",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/review_reviewer_2_3f564e41",
  "sessionId": "b64a1fb5-cc00-4ec5-a8b3-b55f8a4cf13d",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YBs1xfudFTNskwbqPjkRsC",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11606,
      "cache_read_input_tokens": 33169,
      "output_tokens": 360,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11606,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 360,
          "cache_read_input_tokens": 33169,
          "cache_creation_input_tokens": 11606,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11606
          },
          "type": "message"
        }
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

_source line 47 · 2026-05-17T17:20:00.108Z_

<details><summary>↩ Tool result · `toolu_0188FB7fHAi83MjJ6zRNiFMP`</summary>

```text
1	\section*{Limitations}
2	\label{sec:limitations}
3	
4	All eight generators are base (pretrained) models.
5	This is a deliberate design choice: base models isolate the generation mechanism from instruction-tuning effects, enabling controlled study of recursive distributional drift.
6	However, web text is predominantly produced by instruction-tuned and RLHF-aligned models.
7	Preliminary instruct experiments confirm that depth signal degrades substantially under instruction tuning: OLMo-2-1B-Instruct drops to LOGO F1\,=\,0.338 (vs.\ 0.763 base) and Qwen3-0.6B with chat template to 0.667 (vs.\ 0.816 under a 7-generator split).
8	Length-matched analysis yields near-zero correlations ($|\rho| < 0.02$) and binary classification near chance (F1\,$\approx$\,0.5) for Qwen models, leaving interpretation ambiguous.
9	Extending depth fingerprinting to instruct models requires addressing these confounds (length regulation, format constraints, safety-driven distribution shaping) that instruction tuning introduces.
10	
11	Our experiments include generators up to 8.2B parameters (Qwen3-8B).
12	Depth signal persists at this scale (Qwen3-8B 3-class F1\,=\,0.714), but cross-scale transfer incurs a moderate gap vs.\ $\leq$2.8B generators (F1\,=\,0.77--0.81).
13	Frontier models (70B+) remain untested; their higher fluency may further compress feature margins.
14	
15	Differential depth response strength is prompt-type dependent: continuation chains show strongest drift (within-type F1\,=\,0.781) compared to elaboration (0.730), rewriting (0.737), and paraphrastic chains (binary F1\,=\,0.671 vs.\ 0.749 for continuation).
16	DDR is most reliably detected in continuation-style generation; near-paraphrastic settings approach the method's detection floor.
17	Cross-prompt-type transfer (LOPTO F1\,=\,0.753) confirms shared signal, yet additional prompt types (e.g., summarization, instruction following) and cross-generator $\times$ cross-prompt interactions remain untested.
18	
19	Our primary evaluation uses single-generator chains; cross-model chains (\S\ref{sec:results-classification}) confirm depth signal under generator heterogeneity (3-class F1\,=\,0.809, binary F1\,=\,0.764), though the eight generators represent a controlled laboratory setting rather than the full diversity of real-world contamination.
20	Simulated human editing (\S\ref{sec:discussion}) suggests graceful degradation, but the gap between simulated token replacement and real-world post-processing remains untested.
21	
22	The reference model is fixed to Pythia-410M throughout, although cross-family reference experiments (\S\ref{sec:results-differential}) confirm the phenomenon is not reference-specific (spread 0.013 across three references).
23	All seed texts in the main evaluation are English Wikipedia excerpts.
24	Cross-domain evaluation (Appendix~\ref{app:domain}) shows that depth signal persists across News, Academic, and Code domains (binary F1 $>$ 0.73 under LOGO at $t{=}1.0$), though a domain $\times$ temperature interaction exists: certain domain/generator combinations at lower temperature approach chance level (e.g., Academic domain binary F1\,=\,0.628 at $t{=}0.7$), suggesting that reference model calibration is critical for cross-domain deployment.
25	The reference model dependency (Pythia-410M, English-centric pretraining) limits non-English applicability and adds inference overhead relative to surface-feature-only approaches.
26	Generalization to other languages remains untested.
27	
28	Our default analysis uses fixed decoding parameters (temperature 0.7, nucleus $p{=}0.9$). A sampling ablation (Appendix~\ref{app:sampling-sensitivity}) shows robustness to moderate variation ($t \in [0.5, 0.7]$, ${\leq}0.3$\,pp) but substantial degradation at $t{=}1.0$ ($-6$\,pp), indicating that depth fingerprinting assumes standard decoding regimes.
29	
30	We use 3-class granularity (gen-0\,/\,gen-1\,/\,gen-2+). A 5-class evaluation (Appendix~\ref{app:finer-depth}) yields LOGO F1\,$\approx$\,0.50, with depths 2--4 mutually indistinguishable, validating the 3-class design as the practical resolution limit.
31	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7c75de69-a79a-4123-91d7-79c6e10d8613",
  "isSidechain": false,
  "promptId": "c6349ba0-ce02-4cbb-9474-95572d1cbd3f",
  "type": "user",
  "uuid": "7c9a8ec3-1a50-4fba-a6d1-e2bbbbf5f0ac",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/limitations.tex",
      "content": "\\section*{Limitations}\n\\label{sec:limitations}\n\nAll eight generators are base (pretrained) models.\nThis is a deliberate design choice: base models isolate the generation mechanism from instruction-tuning effects, enabling controlled study of recursive distributional drift.\nHowever, web text is predominantly produced by instruction-tuned and RLHF-aligned models.\nPreliminary instruct experiments confirm that depth signal degrades substantially under instruction tuning: OLMo-2-1B-Instruct drops to LOGO F1\\,=\\,0.338 (vs.\\ 0.763 base) and Qwen3-0.6B with chat template to 0.667 (vs.\\ 0.816 under a 7-generator split).\nLength-matched analysis yields near-zero correlations ($|\\rho| < 0.02$) and binary classification near chance (F1\\,$\\approx$\\,0.5) for Qwen models, leaving interpretation ambiguous.\nExtending depth fingerprinting to instruct models requires addressing these confounds (length regulation, format constraints, safety-driven distribution shaping) that instruction tuning introduces.\n\nOur experiments include generators up to 8.2B parameters (Qwen3-8B).\nDepth signal persists at this scale (Qwen3-8B 3-class F1\\,=\\,0.714), but cross-scale transfer incurs a moderate gap vs.\\ $\\leq$2.8B generators (F1\\,=\\,0.77--0.81).\nFrontier models (70B+) remain untested; their higher fluency may further compress feature margins.\n\nDifferential depth response strength is prompt-type dependent: continuation chains show strongest drift (within-type F1\\,=\\,0.781) compared to elaboration (0.730), rewriting (0.737), and paraphrastic chains (binary F1\\,=\\,0.671 vs.\\ 0.749 for continuation).\nDDR is most reliably detected in continuation-style generation; near-paraphrastic settings approach the method's detection floor.\nCross-prompt-type transfer (LOPTO F1\\,=\\,0.753) confirms shared signal, yet additional prompt types (e.g., summarization, instruction following) and cross-generator $\\times$ cross-prompt interactions remain untested.\n\nOur primary evaluation uses single-generator chains; cross-model chains (\\S\\ref{sec:results-classification}) confirm depth signal under generator heterogeneity (3-class F1\\,=\\,0.809, binary F1\\,=\\,0.764), though the eight generators represent a controlled laboratory setting rather than the full diversity of real-world contamination.\nSimulated human editing (\\S\\ref{sec:discussion}) suggests graceful degradation, but the gap between simulated token replacement and real-world post-processing remains untested.\n\nThe reference model is fixed to Pythia-410M throughout, although cross-family reference experiments (\\S\\ref{sec:results-differential}) confirm the phenomenon is not reference-specific (spread 0.013 across three references).\nAll seed texts in the main evaluation are English Wikipedia excerpts.\nCross-domain evaluation (Appendix~\\ref{app:domain}) shows that depth signal persists across News, Academic, and Code domains (binary F1 $>$ 0.73 under LOGO at $t{=}1.0$), though a domain $\\times$ temperature interaction exists: certain domain/generator combinations at lower temperature approach chance level (e.g., Academic domain binary F1\\,=\\,0.628 at $t{=}0.7$), suggesting that reference model calibration is critical for cross-domain deployment.\nThe reference model dependency (Pythia-410M, English-centric pretraining) limits non-English applicability and adds inference overhead relative to surface-feature-only approaches.\nGeneralization to other languages remains untested.\n\nOur default analysis uses fixed decoding parameters (temperature 0.7, nucleus $p{=}0.9$). A sampling ablation (Appendix~\\ref{app:sampling-sensitivity}) shows robustness to moderate variation ($t \\in [0.5, 0.7]$, ${\\leq}0.3$\\,pp) but substantial degradation at $t{=}1.0$ ($-6$\\,pp), indicating that depth fingerprinting assumes standard decoding regimes.\n\nWe use 3-class granularity (gen-0\\,/\\,gen-1\\,/\\,gen-2+). A 5-class evaluation (Appendix~\\ref{app:finer-depth}) yields LOGO F1\\,$\\approx$\\,0.50, with depths 2--4 mutually indistinguishable, validating the 3-class design as the practical resolution limit.\n",
      "numLines": 31,
      "startLine": 1,
      "totalLines": 31
    }
  },
  "sourceToolAssistantUUID": "7c75de69-a79a-4123-91d7-79c6e10d8613",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/review_reviewer_2_3f564e41",
  "sessionId": "b64a1fb5-cc00-4ec5-a8b3-b55f8a4cf13d",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---


### Tool call

_source line 48 · 2026-05-17T17:20:00.645Z_

<details open><summary>🔧 Tool call — Read · `toolu_016h693w1cHiWkAxM6TdarR5`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/ethics.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7c9a8ec3-1a50-4fba-a6d1-e2bbbbf5f0ac",
  "isSidechain": false,
  "requestId": "req_011Cb8XMzJvMexo6ZSdrGZTi",
  "type": "assistant",
  "uuid": "d27a6b6a-ad1d-4d5a-8d80-930ed1f75640",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/review_reviewer_2_3f564e41",
  "sessionId": "b64a1fb5-cc00-4ec5-a8b3-b55f8a4cf13d",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YBs1xfudFTNskwbqPjkRsC",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11606,
      "cache_read_input_tokens": 33169,
      "output_tokens": 360,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11606,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 360,
          "cache_read_input_tokens": 33169,
          "cache_creation_input_tokens": 11606,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11606
          },
          "type": "message"
        }
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

_source line 49 · 2026-05-17T17:20:00.649Z_

<details><summary>↩ Tool result · `toolu_016h693w1cHiWkAxM6TdarR5`</summary>

```text
1	\section*{Ethics Statement}
2	\label{sec:ethics}
3	
4	All texts analyzed in this work are LLM-generated from publicly available Wikipedia seeds; no personal or sensitive data is involved.
5	Our method estimates the generation depth of a text passage (how many recursive generation steps it has undergone), not the identity of its author.
6	Individual authorship attribution is outside both the scope and the capability of this approach; privacy implications are minimal.
7	We acknowledge that depth estimation tools could in principle be used to selectively suppress machine-generated text in contexts where such content is legitimate (e.g., accessibility tools, assistive writing).
8	We encourage deployment in data governance pipelines where provenance transparency, rather than content removal, is the objective.
9	
10	\paragraph{Licenses.}
11	All generator models are publicly available under permissive licenses (Apache 2.0 for Pythia, OLMo, and Mistral; Qwen License for Qwen3; Llama Community License for Llama 3.2).
12	Wikipedia seed passages are distributed under CC BY-SA 3.0.
13	
14	\paragraph{Compute budget.}
15	All experiments were conducted on 4$\times$ NVIDIA RTX 5090 GPUs (32\,GB each), totaling approximately 62 GPU-hours.
16	
17	\paragraph{Software.}
18	Experiments used Python 3.12.3, PyTorch 2.10.0 (CUDA 12.8), Transformers 4.57.6, XGBoost 3.2.0, scikit-learn 1.8.0, NumPy 2.2.6, pandas 3.0.2, and SciPy 1.17.1.
19	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d27a6b6a-ad1d-4d5a-8d80-930ed1f75640",
  "isSidechain": false,
  "promptId": "c6349ba0-ce02-4cbb-9474-95572d1cbd3f",
  "type": "user",
  "uuid": "1937a5ff-0258-4e97-a1df-84e7a468404e",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/ethics.tex",
      "content": "\\section*{Ethics Statement}\n\\label{sec:ethics}\n\nAll texts analyzed in this work are LLM-generated from publicly available Wikipedia seeds; no personal or sensitive data is involved.\nOur method estimates the generation depth of a text passage (how many recursive generation steps it has undergone), not the identity of its author.\nIndividual authorship attribution is outside both the scope and the capability of this approach; privacy implications are minimal.\nWe acknowledge that depth estimation tools could in principle be used to selectively suppress machine-generated text in contexts where such content is legitimate (e.g., accessibility tools, assistive writing).\nWe encourage deployment in data governance pipelines where provenance transparency, rather than content removal, is the objective.\n\n\\paragraph{Licenses.}\nAll generator models are publicly available under permissive licenses (Apache 2.0 for Pythia, OLMo, and Mistral; Qwen License for Qwen3; Llama Community License for Llama 3.2).\nWikipedia seed passages are distributed under CC BY-SA 3.0.\n\n\\paragraph{Compute budget.}\nAll experiments were conducted on 4$\\times$ NVIDIA RTX 5090 GPUs (32\\,GB each), totaling approximately 62 GPU-hours.\n\n\\paragraph{Software.}\nExperiments used Python 3.12.3, PyTorch 2.10.0 (CUDA 12.8), Transformers 4.57.6, XGBoost 3.2.0, scikit-learn 1.8.0, NumPy 2.2.6, pandas 3.0.2, and SciPy 1.17.1.\n",
      "numLines": 19,
      "startLine": 1,
      "totalLines": 19
    }
  },
  "sourceToolAssistantUUID": "d27a6b6a-ad1d-4d5a-8d80-930ed1f75640",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/review_reviewer_2_3f564e41",
  "sessionId": "b64a1fb5-cc00-4ec5-a8b3-b55f8a4cf13d",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---


### Tool call

_source line 50 · 2026-05-17T17:20:01.311Z_

<details open><summary>🔧 Tool call — Read · `toolu_01LUsiPpDXViaPrgnru8YNuz`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/references.bib",
  "limit": 200
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1937a5ff-0258-4e97-a1df-84e7a468404e",
  "isSidechain": false,
  "requestId": "req_011Cb8XMzJvMexo6ZSdrGZTi",
  "type": "assistant",
  "uuid": "71b11de3-f88d-49a8-bab5-ec87c6ec8995",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/review_reviewer_2_3f564e41",
  "sessionId": "b64a1fb5-cc00-4ec5-a8b3-b55f8a4cf13d",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YBs1xfudFTNskwbqPjkRsC",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11606,
      "cache_read_input_tokens": 33169,
      "output_tokens": 360,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11606,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 360,
          "cache_read_input_tokens": 33169,
          "cache_creation_input_tokens": 11606,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11606
          },
          "type": "message"
        }
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
  "lastPrompt": "[Round 1 审稿请求]: 你负责**新颖性 + 完整性 + Related Work + 格式**。  ## Venue 信息 - **目标**: EMNLP 2026（ARR May 2026 cycle） - **截止日期**: 2026-05-25 - **页数限制**: Long paper 正文 8 页（不含 limitations/ethics/references） - **模…",
  "leafUuid": "36360c78-5fa3-45a6-a83a-4d9ae002a948",
  "sessionId": "b64a1fb5-cc00-4ec5-a8b3-b55f8a4cf13d"
}
```

---


### Runtime record

_source line 52_

```json
{
  "type": "ai-title",
  "aiTitle": "Review depth fingerprinting paper for EMNLP 2026",
  "sessionId": "b64a1fb5-cc00-4ec5-a8b3-b55f8a4cf13d"
}
```

---


### Assistant

_source line 53 · 2026-05-17T17:20:05.848Z_

<details><summary>Logged reasoning block</summary>

```text
Let me continue reading the references and also look at the table4 file for the baselines, and some appendices to understand the full picture.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "36360c78-5fa3-45a6-a83a-4d9ae002a948",
  "isSidechain": false,
  "requestId": "req_011Cb8XNZWhLmFAaGYKGmtj2",
  "type": "assistant",
  "uuid": "6f88595c-0584-45e2-ba47-5fa7a2ff9bff",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/review_reviewer_2_3f564e41",
  "sessionId": "b64a1fb5-cc00-4ec5-a8b3-b55f8a4cf13d",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JKYZKGNbNAfrbDAxAnUwV9",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6315,
      "cache_read_input_tokens": 44775,
      "output_tokens": 320,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 6315,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 320,
          "cache_read_input_tokens": 44775,
          "cache_creation_input_tokens": 6315,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 6315
          },
          "type": "message"
        }
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

_source line 54 · 2026-05-17T17:20:08.199Z_

<details open><summary>🔧 Tool call — Read · `toolu_011qrasEyzwKhVNiFme13mEb`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/references.bib",
  "offset": 200,
  "limit": 200
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6f88595c-0584-45e2-ba47-5fa7a2ff9bff",
  "isSidechain": false,
  "requestId": "req_011Cb8XNZWhLmFAaGYKGmtj2",
  "type": "assistant",
  "uuid": "aa72f73c-7882-42d4-8780-6fb16d9766d6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/review_reviewer_2_3f564e41",
  "sessionId": "b64a1fb5-cc00-4ec5-a8b3-b55f8a4cf13d",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JKYZKGNbNAfrbDAxAnUwV9",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6315,
      "cache_read_input_tokens": 44775,
      "output_tokens": 320,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 6315,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 320,
          "cache_read_input_tokens": 44775,
          "cache_creation_input_tokens": 6315,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 6315
          },
          "type": "message"
        }
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

_source line 55 · 2026-05-17T17:20:08.206Z_

<details><summary>↩ Tool result · `toolu_011qrasEyzwKhVNiFme13mEb`</summary>

```text
200	
201	% ===== Watermarking =====
202	
203	@inproceedings{watermark_llm,
204	  title = {{A Watermark for Large Language Models}},
205	  author = {Kirchenbauer, John and Geiping, Jonas and Wen, Yuxin and Katz, Jonathan and Miers, Ian and Goldstein, Tom},
206	  booktitle = {Proceedings of the International Conference on Machine Learning},
207	  year = {2023},
208	}
209	
210	@article{synthid_text,
211	  title = {{Scalable Watermarking for Identifying Large Language Model Outputs}},
212	  author = {Dathathri, Sumanth and See, Abigail and Ghaisas, Sumedh and Huang, Po-Sen and McAdam, Rob and Welbl, Johannes and Bachani, Vandana and Kaskasoli, Alex and Stanforth, Robert and Matejovicova, Tatiana and Hayes, Jamie and Vyas, Nidhi and Al Merey, Majd and Brown-Cohen, Jonah and Bunel, Rudy and Balle, Borja and Cemgil, Taylan and Ahmed, Zahra and Stacpoole, Kitty and Shumailov, Ilia and Baetu, Ciprian and Gowal, Sven and Hassabis, Demis and Kohli, Pushmeet},
213	  journal = {Nature},
214	  volume = {634},
215	  pages = {818--823},
216	  year = {2024},
217	}
218	
219	@misc{aaronson_watermark,
220	  title = {{Watermarking GPT Outputs}},
221	  author = {Aaronson, Scott and Kirchner, Hendrik},
222	  year = {2022},
223	  howpublished = {Technical Talk},
224	  url = {https://scottaaronson.blog/?p=6823},
225	}
226	
227	@article{chainwash,
228	  title = {{Chainwash: Multi-Step Rewriting Attacks on Diffusion Language Model Watermarks}},
229	  author = {Ameen, Mohd Ruhul and Islam, Akif and Mahmud, Nadim and Hamid, Md. Ekramul},
230	  journal = {arXiv preprint arXiv:2605.05503},
231	  year = {2026},
232	}
233	
234	% ===== Vocabulary Diversity =====
235	
236	@inproceedings{curious_decline,
237	  title = {{The Curious Decline of Linguistic Diversity: Training Language Models on Synthetic Text}},
238	  author = {Guo, Yanzhu and Shang, Guokan and Vazirgiannis, Michalis and Clavel, Chlo\'{e}},
239	  booktitle = {Findings of the Association for Computational Linguistics: NAACL},
240	  year = {2024},
241	}
242	
243	@inproceedings{writing_diversity,
244	  title = {{Does Writing with Language Models Reduce Content Diversity?}},
245	  author = {Padmakumar, Vishakh and He, He},
246	  booktitle = {Proceedings of the International Conference on Learning Representations},
247	  year = {2024},
248	}
249	
250	@inproceedings{nucleus_sampling,
251	  title = {{The Curious Case of Neural Text Degeneration}},
252	  author = {Holtzman, Ari and Buys, Jan and Du, Li and Forbes, Maxwell and Choi, Yejin},
253	  booktitle = {Proceedings of the International Conference on Learning Representations},
254	  year = {2020},
255	}
256	
257	@inproceedings{mapping_llm_science,
258	  title = {{Mapping the Increasing Use of LLMs in Scientific Papers}},
259	  author = {Liang, Weixin and Zhang, Yaohui and Wu, Zhengxuan and Lepp, Haley and Ji, Wenlong and Zhao, Xuandong and Cao, Hancheng and Liu, Sheng and He, Siyu and Huang, Zhi and Yang, Diyi and Potts, Christopher and Manning, Christopher D. and Zou, James Y.},
260	  booktitle = {Proceedings of the Conference on Language Modeling},
261	  year = {2024},
262	}
263	
264	@inproceedings{monitoring_ai_review,
265	  title = {{Monitoring AI-Modified Content at Scale: A Case Study on the Impact of ChatGPT on AI Conference Peer Reviews}},
266	  author = {Liang, Weixin and Izzo, Zachary and Zhang, Yaohui and Lepp, Haley and Cao, Hancheng and Zhao, Xuandong and Chen, Lingjiao and Ye, Haotian and Liu, Sheng and Huang, Zhi and McFarland, Daniel A. and Zou, James Y.},
267	  booktitle = {Proceedings of the International Conference on Machine Learning},
268	  year = {2024},
269	}
270	
271	% ===== Stylometry =====
272	
273	@article{stamatatos_survey,
274	  title = {{A Survey of Modern Authorship Attribution Methods}},
275	  author = {Stamatatos, Efstathios},
276	  journal = {Journal of the American Society for Information Science and Technology},
277	  year = {2009},
278	}
279	
280	@article{koppel_authorship,
281	  title = {{Computational Methods in Authorship Attribution}},
282	  author = {Koppel, Moshe and Schler, Jonathan and Argamon, Shlomo},
283	  journal = {Journal of the American Society for Information Science and Technology},
284	  year = {2009},
285	}
286	
287	@inproceedings{uchendu_attribution,
288	  title = {{Authorship Attribution for Neural Text Generation}},
289	  author = {Uchendu, Adaku and Le, Thai and Shu, Kai and Lee, Dongwon},
290	  booktitle = {Proceedings of the Conference on Empirical Methods in Natural Language Processing},
291	  year = {2020},
292	}
293	
294	@inproceedings{munir_looking_glass,
295	  title = {{Through the Looking Glass: Learning to Attribute Synthetic Text Generated by Language Models}},
296	  author = {Munir, Shaoor and Batool, Brishna and Shafiq, Zubair and Srinivasan, Padmini and Zaffar, Fareed},
297	  booktitle = {Proceedings of the Conference of the European Chapter of the Association for Computational Linguistics},
298	  year = {2021},
299	}
300	
301	% ===== Iterative Generation =====
302	
303	@inproceedings{broken_telephone,
304	  title = {{LLM as a Broken Telephone: Iterative Generation Distorts Information}},
305	  author = {Mohamed, Amr and Geng, Mingmeng and Vazirgiannis, Michalis and Shang, Guokan},
306	  booktitle = {Proceedings of the Annual Meeting of the Association for Computational Linguistics},
307	  year = {2025},
308	}
309	
310	@article{markovian_chains,
311	  title = {{Markovian Generation Chains in Large Language Models}},
312	  author = {Geng, Mingmeng and Mohamed, Amr and Shang, Guokan and Vazirgiannis, Michalis and Poibeau, Thierry},
313	  journal = {arXiv preprint arXiv:2603.11228},
314	  year = {2026},
315	}
316	
317	@inproceedings{self_refine,
318	  title = {{Self-Refine: Iterative Refinement with Self-Feedback}},
319	  author = {Madaan, Aman and Tandon, Niket and Gupta, Prakhar and Hallinan, Skyler and Gao, Luyu and Wiegreffe, Sarah and Alon, Uri and Dziri, Nouha and Prabhumoye, Shrimai and Yang, Yiming and Gupta, Shashank and Majumder, Bodhisattwa Prasad and Hermann, Katherine and Welleck, Sean and Yazdanbakhsh, Amir and Clark, Peter},
320	  booktitle = {Advances in Neural Information Processing Systems},
321	  year = {2023},
322	}
323	
324	% ===== Membership Inference =====
325	
326	@inproceedings{min_k_percent,
327	  title = {{Detecting Pretraining Data from Large Language Models}},
328	  author = {Shi, Weijia and Ajith, Anirudh and Xia, Mengzhou and Huang, Yangsibo and Liu, Daogao and Blevins, Terra and Chen, Danqi and Zettlemoyer, Luke},
329	  booktitle = {Proceedings of the International Conference on Learning Representations},
330	  year = {2024},
331	}
332	
333	% ===== Survey =====
334	
335	@article{wu_survey_2025,
336	  title = {{A Survey on LLM-Generated Text Detection: Necessity, Methods, and Future Directions}},
337	  author = {Wu, Junchao and Yang, Shu and Zhan, Runzhe and Yuan, Yulin and Chao, Lidia Sam and Wong, Derek Fai},
338	  journal = {Computational Linguistics},
339	  publisher = {MIT Press},
340	  year = {2025},
341	}
342	
343	@inproceedings{jawahar_survey,
344	  title = {{Automatic Detection of Machine Generated Text: A Critical Survey}},
345	  author = {Jawahar, Ganesh and Abdul-Mageed, Muhammad and Lakshmanan, Laks V.S.},
346	  booktitle = {Proceedings of the International Conference on Computational Linguistics},
347	  year = {2020},
348	}
349	
350	% ===== Models =====
351	
352	@inproceedings{pythia,
353	  title = {{Pythia: A Suite for Analyzing Large Language Models Across Training and Scaling}},
354	  author = {Biderman, Stella and Schoelkopf, Hailey and Anthony, Quentin Gregory and Bradley, Herbie and O'Brien, Kyle and Hallahan, Eric and Khan, Mohammad Aflah and Purohit, Shivanshu and Prashanth, USVSN Sai and Raff, Edward and Skowron, Aviya and Sutawika, Lintang and {van der Wal}, Oskar},
355	  booktitle = {Proceedings of the International Conference on Machine Learning},
356	  year = {2023},
357	}
358	
359	@inproceedings{olmo,
360	  title = {{OLMo: Accelerating the Science of Language Models}},
361	  author = {Groeneveld, Dirk and Beltagy, Iz and Walsh, Evan and Bhagia, Akshita and Kinney, Rodney and Tafjord, Oyvind and Jha, Ananya Harsh and Ivison, Hamish and Magnusson, Ian and Wang, Yizhong and Arora, Shane and Atkinson, David and Authur, Russell and Chandu, Khyathi Raghavi and Cohan, Arman and Dumas, Jennifer and Elazar, Yanai and Gu, Yuling and Hessel, Jack and Khot, Tushar and Merrill, William and Morrison, Jacob and Muennighoff, Niklas and Naik, Aakanksha and Nam, Crystal and Peters, Matthew E. and Pyatkin, Valentina and Ravichander, Abhilasha and Schwenk, Dustin and Shah, Saurabh and Smith, Will and Strubell, Emma and Subramani, Nishant and Wortsman, Mitchell and Dasigi, Pradeep and Lambert, Nathan and Richardson, Kyle and Zettlemoyer, Luke and Dodge, Jesse and Lo, Kyle and Soldaini, Luca and Smith, Noah A. and Hajishirzi, Hannaneh},
362	  booktitle = {Proceedings of the Annual Meeting of the Association for Computational Linguistics},
363	  year = {2024},
364	}
365	
366	@article{qwen3,
367	  title = {{Qwen3 Technical Report}},
368	  author = {{Qwen Team}},
369	  journal = {arXiv preprint arXiv:2505.09388},
370	  year = {2025},
371	}
372	
373	@inproceedings{ghostbuster,
374	  title = {{Ghostbuster: Detecting Text Ghostwritten by Large Language Models}},
375	  author = {Verma, Vivek and Fleisig, Eve and Tomlin, Nicholas and Jurafsky, Dan},
376	  booktitle = {Proceedings of the Annual Meeting of the Association for Computational Linguistics},
377	  year = {2024},
378	}
379	
380	@inproceedings{radar,
381	  title = {{RADAR: Robust AI-Text Detection via Adversarial Learning}},
382	  author = {Hu, Xiaomeng and Chen, Pin-Yu and Ho, Tsung-Yi},
383	  booktitle = {Advances in Neural Information Processing Systems},
384	  year = {2023},
385	}
386	
387	% ===== Machine Learning =====
388	
389	@article{gutierrez_ordinal_survey,
390	  title = {{Ordinal Regression Methods: Survey and Experimental Study}},
391	  author = {Guti{\'e}rrez, Pedro Antonio and Perez-Ortiz, Maria and Sanchez-Monedero, Javier and Fernandez-Navarro, Francisco and Hervas-Martinez, Cesar},
392	  journal = {IEEE Transactions on Knowledge and Data Engineering},
393	  volume = {28},
394	  number = {1},
395	  pages = {127--146},
396	  year = {2016},
397	}
398	
399	@article{coral_ordinal,
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "aa72f73c-7882-42d4-8780-6fb16d9766d6",
  "isSidechain": false,
  "promptId": "c6349ba0-ce02-4cbb-9474-95572d1cbd3f",
  "type": "user",
  "uuid": "b0fb14f5-b44f-41ea-a470-65ee24a667eb",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/references.bib",
      "content": "\n% ===== Watermarking =====\n\n@inproceedings{watermark_llm,\n  title = {{A Watermark for Large Language Models}},\n  author = {Kirchenbauer, John and Geiping, Jonas and Wen, Yuxin and Katz, Jonathan and Miers, Ian and Goldstein, Tom},\n  booktitle = {Proceedings of the International Conference on Machine Learning},\n  year = {2023},\n}\n\n@article{synthid_text,\n  title = {{Scalable Watermarking for Identifying Large Language Model Outputs}},\n  author = {Dathathri, Sumanth and See, Abigail and Ghaisas, Sumedh and Huang, Po-Sen and McAdam, Rob and Welbl, Johannes and Bachani, Vandana and Kaskasoli, Alex and Stanforth, Robert and Matejovicova, Tatiana and Hayes, Jamie and Vyas, Nidhi and Al Merey, Majd and Brown-Cohen, Jonah and Bunel, Rudy and Balle, Borja and Cemgil, Taylan and Ahmed, Zahra and Stacpoole, Kitty and Shumailov, Ilia and Baetu, Ciprian and Gowal, Sven and Hassabis, Demis and Kohli, Pushmeet},\n  journal = {Nature},\n  volume = {634},\n  pages = {818--823},\n  year = {2024},\n}\n\n@misc{aaronson_watermark,\n  title = {{Watermarking GPT Outputs}},\n  author = {Aaronson, Scott and Kirchner, Hendrik},\n  year = {2022},\n  howpublished = {Technical Talk},\n  url = {https://scottaaronson.blog/?p=6823},\n}\n\n@article{chainwash,\n  title = {{Chainwash: Multi-Step Rewriting Attacks on Diffusion Language Model Watermarks}},\n  author = {Ameen, Mohd Ruhul and Islam, Akif and Mahmud, Nadim and Hamid, Md. Ekramul},\n  journal = {arXiv preprint arXiv:2605.05503},\n  year = {2026},\n}\n\n% ===== Vocabulary Diversity =====\n\n@inproceedings{curious_decline,\n  title = {{The Curious Decline of Linguistic Diversity: Training Language Models on Synthetic Text}},\n  author = {Guo, Yanzhu and Shang, Guokan and Vazirgiannis, Michalis and Clavel, Chlo\\'{e}},\n  booktitle = {Findings of the Association for Computational Linguistics: NAACL},\n  year = {2024},\n}\n\n@inproceedings{writing_diversity,\n  title = {{Does Writing with Language Models Reduce Content Diversity?}},\n  author = {Padmakumar, Vishakh and He, He},\n  booktitle = {Proceedings of the International Conference on Learning Representations},\n  year = {2024},\n}\n\n@inproceedings{nucleus_sampling,\n  title = {{The Curious Case of Neural Text Degeneration}},\n  author = {Holtzman, Ari and Buys, Jan and Du, Li and Forbes, Maxwell and Choi, Yejin},\n  booktitle = {Proceedings of the International Conference on Learning Representations},\n  year = {2020},\n}\n\n@inproceedings{mapping_llm_science,\n  title = {{Mapping the Increasing Use of LLMs in Scientific Papers}},\n  author = {Liang, Weixin and Zhang, Yaohui and Wu, Zhengxuan and Lepp, Haley and Ji, Wenlong and Zhao, Xuandong and Cao, Hancheng and Liu, Sheng and He, Siyu and Huang, Zhi and Yang, Diyi and Potts, Christopher and Manning, Christopher D. and Zou, James Y.},\n  booktitle = {Proceedings of the Conference on Language Modeling},\n  year = {2024},\n}\n\n@inproceedings{monitoring_ai_review,\n  title = {{Monitoring AI-Modified Content at Scale: A Case Study on the Impact of ChatGPT on AI Conference Peer Reviews}},\n  author = {Liang, Weixin and Izzo, Zachary and Zhang, Yaohui and Lepp, Haley and Cao, Hancheng and Zhao, Xuandong and Chen, Lingjiao and Ye, Haotian and Liu, Sheng and Huang, Zhi and McFarland, Daniel A. and Zou, James Y.},\n  booktitle = {Proceedings of the International Conference on Machine Learning},\n  year = {2024},\n}\n\n% ===== Stylometry =====\n\n@article{stamatatos_survey,\n  title = {{A Survey of Modern Authorship Attribution Methods}},\n  author = {Stamatatos, Efstathios},\n  journal = {Journal of the American Society for Information Science and Technology},\n  year = {2009},\n}\n\n@article{koppel_authorship,\n  title = {{Computational Methods in Authorship Attribution}},\n  author = {Koppel, Moshe and Schler, Jonathan and Argamon, Shlomo},\n  journal = {Journal of the American Society for Information Science and Technology},\n  year = {2009},\n}\n\n@inproceedings{uchendu_attribution,\n  title = {{Authorship Attribution for Neural Text Generation}},\n  author = {Uchendu, Adaku and Le, Thai and Shu, Kai and Lee, Dongwon},\n  booktitle = {Proceedings of the Conference on Empirical Methods in Natural Language Processing},\n  year = {2020},\n}\n\n@inproceedings{munir_looking_glass,\n  title = {{Through the Looking Glass: Learning to Attribute Synthetic Text Generated by Language Models}},\n  author = {Munir, Shaoor and Batool, Brishna and Shafiq, Zubair and Srinivasan, Padmini and Zaffar, Fareed},\n  booktitle = {Proceedings of the Conference of the European Chapter of the Association for Computational Linguistics},\n  year = {2021},\n}\n\n% ===== Iterative Generation =====\n\n@inproceedings{broken_telephone,\n  title = {{LLM as a Broken Telephone: Iterative Generation Distorts Information}},\n  author = {Mohamed, Amr and Geng, Mingmeng and Vazirgiannis, Michalis and Shang, Guokan},\n  booktitle = {Proceedings of the Annual Meeting of the Association for Computational Linguistics},\n  year = {2025},\n}\n\n@article{markovian_chains,\n  title = {{Markovian Generation Chains in Large Language Models}},\n  author = {Geng, Mingmeng and Mohamed, Amr and Shang, Guokan and Vazirgiannis, Michalis and Poibeau, Thierry},\n  journal = {arXiv preprint arXiv:2603.11228},\n  year = {2026},\n}\n\n@inproceedings{self_refine,\n  title = {{Self-Refine: Iterative Refinement with Self-Feedback}},\n  author = {Madaan, Aman and Tandon, Niket and Gupta, Prakhar and Hallinan, Skyler and Gao, Luyu and Wiegreffe, Sarah and Alon, Uri and Dziri, Nouha and Prabhumoye, Shrimai and Yang, Yiming and Gupta, Shashank and Majumder, Bodhisattwa Prasad and Hermann, Katherine and Welleck, Sean and Yazdanbakhsh, Amir and Clark, Peter},\n  booktitle = {Advances in Neural Information Processing Systems},\n  year = {2023},\n}\n\n% ===== Membership Inference =====\n\n@inproceedings{min_k_percent,\n  title = {{Detecting Pretraining Data from Large Language Models}},\n  author = {Shi, Weijia and Ajith, Anirudh and Xia, Mengzhou and Huang, Yangsibo and Liu, Daogao and Blevins, Terra and Chen, Danqi and Zettlemoyer, Luke},\n  booktitle = {Proceedings of the International Conference on Learning Representations},\n  year = {2024},\n}\n\n% ===== Survey =====\n\n@article{wu_survey_2025,\n  title = {{A Survey on LLM-Generated Text Detection: Necessity, Methods, and Future Directions}},\n  author = {Wu, Junchao and Yang, Shu and Zhan, Runzhe and Yuan, Yulin and Chao, Lidia Sam and Wong, Derek Fai},\n  journal = {Computational Linguistics},\n  publisher = {MIT Press},\n  year = {2025},\n}\n\n@inproceedings{jawahar_survey,\n  title = {{Automatic Detection of Machine Generated Text: A Critical Survey}},\n  author = {Jawahar, Ganesh and Abdul-Mageed, Muhammad and Lakshmanan, Laks V.S.},\n  booktitle = {Proceedings of the International Conference on Computational Linguistics},\n  year = {2020},\n}\n\n% ===== Models =====\n\n@inproceedings{pythia,\n  title = {{Pythia: A Suite for Analyzing Large Language Models Across Training and Scaling}},\n  author = {Biderman, Stella and Schoelkopf, Hailey and Anthony, Quentin Gregory and Bradley, Herbie and O'Brien, Kyle and Hallahan, Eric and Khan, Mohammad Aflah and Purohit, Shivanshu and Prashanth, USVSN Sai and Raff, Edward and Skowron, Aviya and Sutawika, Lintang and {van der Wal}, Oskar},\n  booktitle = {Proceedings of the International Conference on Machine Learning},\n  year = {2023},\n}\n\n@inproceedings{olmo,\n  title = {{OLMo: Accelerating the Science of Language Models}},\n  author = {Groeneveld, Dirk and Beltagy, Iz and Walsh, Evan and Bhagia, Akshita and Kinney, Rodney and Tafjord, Oyvind and Jha, Ananya Harsh and Ivison, Hamish and Magnusson, Ian and Wang, Yizhong and Arora, Shane and Atkinson, David and Authur, Russell and Chandu, Khyathi Raghavi and Cohan, Arman and Dumas, Jennifer and Elazar, Yanai and Gu, Yuling and Hessel, Jack and Khot, Tushar and Merrill, William and Morrison, Jacob and Muennighoff, Niklas and Naik, Aakanksha and Nam, Crystal and Peters, Matthew E. and Pyatkin, Valentina and Ravichander, Abhilasha and Schwenk, Dustin and Shah, Saurabh and Smith, Will and Strubell, Emma and Subramani, Nishant and Wortsman, Mitchell and Dasigi, Pradeep and Lambert, Nathan and Richardson, Kyle and Zettlemoyer, Luke and Dodge, Jesse and Lo, Kyle and Soldaini, Luca and Smith, Noah A. and Hajishirzi, Hannaneh},\n  booktitle = {Proceedings of the Annual Meeting of the Association for Computational Linguistics},\n  year = {2024},\n}\n\n@article{qwen3,\n  title = {{Qwen3 Technical Report}},\n  author = {{Qwen Team}},\n  journal = {arXiv preprint arXiv:2505.09388},\n  year = {2025},\n}\n\n@inproceedings{ghostbuster,\n  title = {{Ghostbuster: Detecting Text Ghostwritten by Large Language Models}},\n  author = {Verma, Vivek and Fleisig, Eve and Tomlin, Nicholas and Jurafsky, Dan},\n  booktitle = {Proceedings of the Annual Meeting of the Association for Computational Linguistics},\n  year = {2024},\n}\n\n@inproceedings{radar,\n  title = {{RADAR: Robust AI-Text Detection via Adversarial Learning}},\n  author = {Hu, Xiaomeng and Chen, Pin-Yu and Ho, Tsung-Yi},\n  booktitle = {Advances in Neural Information Processing Systems},\n  year = {2023},\n}\n\n% ===== Machine Learning =====\n\n@article{gutierrez_ordinal_survey,\n  title = {{Ordinal Regression Methods: Survey and Experimental Study}},\n  author = {Guti{\\'e}rrez, Pedro Antonio and Perez-Ortiz, Maria and Sanchez-Monedero, Javier and Fernandez-Navarro, Francisco and Hervas-Martinez, Cesar},\n  journal = {IEEE Transactions on Knowledge and Data Engineering},\n  volume = {28},\n  number = {1},\n  pages = {127--146},\n  year = {2016},\n}\n\n@article{coral_ordinal,",
      "numLines": 200,
      "startLine": 200,
      "totalLines": 447
    }
  },
  "sourceToolAssistantUUID": "aa72f73c-7882-42d4-8780-6fb16d9766d6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/review_reviewer_2_3f564e41",
  "sessionId": "b64a1fb5-cc00-4ec5-a8b3-b55f8a4cf13d",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---


### Tool result

_source line 56 · 2026-05-17T17:20:09.349Z_

<details><summary>↩ Tool result · `toolu_01XxVVbtmbwJ4FZBEcAqX9vg`</summary>

```text
1	Can depth-aware data curation improve downstream language model quality?
2	We fine-tune OLMo-2-0425-1B on five data variants (3 seeds each) and evaluate perplexity on a held-out test set (Table~\ref{tab:downstream}).
3	
4	\begin{table}[h]
5	\centering
6	\small
7	\begin{tabular}{lrc}
8	\toprule
9	\textbf{Variant} & \textbf{$n$} & \textbf{Test PPL} \\
10	\midrule
11	All depths            & 12{,}299 & 2.335 $\pm$ 0.000 \\
12	Size-matched (random) & 3{,}951  & 2.367 $\pm$ 0.000 \\
13	Depth 0--1 only       & 3{,}951  & 2.387 $\pm$ 0.001 \\
14	Binary-filtered       & 3{,}951  & 2.389 $\pm$ 0.000 \\
15	Depth 0 only          & 797      & 2.681 $\pm$ 0.001 \\
16	\bottomrule
17	\end{tabular}
18	\caption{Downstream fine-tuning perplexity (OLMo-2-0425-1B, mean $\pm$ std across 3 seeds). At equal sample count, random subsampling (2.367) outperforms depth-aware curation (depth 0--1: 2.387, binary-filtered: 2.389).}
19	\label{tab:downstream}
20	\end{table}
21	
22	The results are unambiguous: data quantity dominates depth composition.
23	Training on all 12{,}299 samples yields the lowest perplexity (2.335).
24	At equal sample count ($n$\,=\,3{,}951), random subsampling (2.367) \emph{outperforms} both depth-stratified selection (depth 0--1: 2.387) and binary detection filtering (2.389).
25	Cross-seed variance is below 0.002 across all variants, confirming the robustness of this null result.
26	
27	Restricting training to human-only text (depth 0, $n$\,=\,797) produces a sharp perplexity increase to 2.681, driven primarily by the 5$\times$ reduction in data volume rather than depth composition per se.
28	
29	\paragraph{Equivalence testing.}
30	We apply a two one-sided $t$-test (TOST) with a $\pm$2\% relative margin (equivalence bounds $\pm$0.047 on the ppl scale) to formally assess whether the depth-aware and random subsampling conditions produce practically indistinguishable perplexity.
31	At equal sample count ($n$\,=\,3{,}951): size-matched (random) ppl\,=\,2.367 vs.\ depth 0--1 ppl\,=\,2.387, $\Delta$\,=\,0.020.
32	TOST confirms equivalence ($p = 1.1 \times 10^{-4}$), indicating the two curation strategies yield practically indistinguishable downstream quality within the $\pm$2\% margin.
33	Cross-seed standard deviation is below 0.001 for both variants.
34	
35	Comparing the full dataset ($n$\,=\,12{,}299, ppl\,=\,2.335) against the depth-filtered subset ($n$\,=\,3{,}951, ppl\,=\,2.387): TOST \emph{rejects} equivalence (minimum equivalence margin\,=\,0.053, exceeding the $\pm$2\% bound), confirming that data quantity drives perplexity reduction beyond what depth-aware selection can recover.
36	
37	Knowing the generation depth of a document does not, by itself, make it more or less useful for training; at fixed sample count, depth-aware curation is statistically equivalent to uninformed random subsampling.
38	
39	\subsection*{Margin Sensitivity Analysis}
40	
41	To assess the robustness of the equivalence conclusion to margin choice, we repeat the TOST procedure across multiple equivalence margins \cite{lakens_equivalence}, following the recommendation to report sensitivity across plausible bounds rather than relying on a single threshold (Table~\ref{tab:tost-margins}).
42	
43	\begin{table}[h]
44	\centering
45	\small
46	\resizebox{\linewidth}{!}{%
47	\begin{tabular}{llcc}
48	\toprule
49	\textbf{Comparison} & \textbf{Margin} & \textbf{Equiv?} & \textbf{TOST $p$} \\
50	\midrule
51	Full (12{,}299) vs.\ Random (3{,}951) & $\pm$1\% & No & 1.0 \\
52	                                        & $\pm$2\% & Yes & $1 \times 10^{-6}$ \\
53	                                        & $\pm$3\% & Yes & $< 10^{-10}$ \\
54	                                        & $\pm$5\% & Yes & $< 10^{-10}$ \\
55	\midrule
56	Full (12{,}299) vs.\ Depth 0--1 (3{,}951) & $\pm$1\% & No & 1.0 \\
57	                                            & $\pm$2\% & No & 1.0 \\
58	                                            & $\pm$3\% & Yes & $< 10^{-10}$ \\
59	                                            & $\pm$5\% & Yes & $< 10^{-10}$ \\
60	\bottomrule
61	\end{tabular}}
62	\caption{TOST equivalence testing across multiple margins. ``Equiv?'' indicates whether equivalence is established at $\alpha = 0.05$.}
63	\label{tab:tost-margins}
64	\end{table}
65	
66	The full dataset vs.\ random subsample comparison passes equivalence at the $\pm$2\% margin ($p = 10^{-6}$), while the full vs.\ depth 0--1 comparison requires a $\pm$3\% margin.
67	In absolute terms, perplexity differences are small: $\Delta$\,=\,0.032 (full vs.\ random, 1.4\% of baseline) and $\Delta$\,=\,0.052 (full vs.\ depth 0--1, 2.2\% of baseline).
68	
69	Cohen's $d$ values are 86.0 (full vs.\ random) and 119.7 (full vs.\ depth 0--1).
70	These appear large but are unreliable: with only $n$\,=\,3 seeds per condition, the pooled standard deviation is extremely small ($<$0.001), artificially inflating $d$.
71	The inflated effect sizes reflect low seed-level variance (confirming reproducibility) rather than practically meaningful perplexity differences.
72	The TOST framework with pre-specified relative margins provides a more appropriate assessment than Cohen's $d$ in this low-seed regime.
73	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "23ddbcb5-60eb-49b6-b1c4-0b9a1d5592f3",
  "isSidechain": false,
  "promptId": "c6349ba0-ce02-4cbb-9474-95572d1cbd3f",
  "type": "user",
  "uuid": "8c6026c8-f389-4622-967c-d8e526e7d53b",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_downstream.tex",
      "content": "Can depth-aware data curation improve downstream language model quality?\nWe fine-tune OLMo-2-0425-1B on five data variants (3 seeds each) and evaluate perplexity on a held-out test set (Table~\\ref{tab:downstream}).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{lrc}\n\\toprule\n\\textbf{Variant} & \\textbf{$n$} & \\textbf{Test PPL} \\\\\n\\midrule\nAll depths            & 12{,}299 & 2.335 $\\pm$ 0.000 \\\\\nSize-matched (random) & 3{,}951  & 2.367 $\\pm$ 0.000 \\\\\nDepth 0--1 only       & 3{,}951  & 2.387 $\\pm$ 0.001 \\\\\nBinary-filtered       & 3{,}951  & 2.389 $\\pm$ 0.000 \\\\\nDepth 0 only          & 797      & 2.681 $\\pm$ 0.001 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Downstream fine-tuning perplexity (OLMo-2-0425-1B, mean $\\pm$ std across 3 seeds). At equal sample count, random subsampling (2.367) outperforms depth-aware curation (depth 0--1: 2.387, binary-filtered: 2.389).}\n\\label{tab:downstream}\n\\end{table}\n\nThe results are unambiguous: data quantity dominates depth composition.\nTraining on all 12{,}299 samples yields the lowest perplexity (2.335).\nAt equal sample count ($n$\\,=\\,3{,}951), random subsampling (2.367) \\emph{outperforms} both depth-stratified selection (depth 0--1: 2.387) and binary detection filtering (2.389).\nCross-seed variance is below 0.002 across all variants, confirming the robustness of this null result.\n\nRestricting training to human-only text (depth 0, $n$\\,=\\,797) produces a sharp perplexity increase to 2.681, driven primarily by the 5$\\times$ reduction in data volume rather than depth composition per se.\n\n\\paragraph{Equivalence testing.}\nWe apply a two one-sided $t$-test (TOST) with a $\\pm$2\\% relative margin (equivalence bounds $\\pm$0.047 on the ppl scale) to formally assess whether the depth-aware and random subsampling conditions produce practically indistinguishable perplexity.\nAt equal sample count ($n$\\,=\\,3{,}951): size-matched (random) ppl\\,=\\,2.367 vs.\\ depth 0--1 ppl\\,=\\,2.387, $\\Delta$\\,=\\,0.020.\nTOST confirms equivalence ($p = 1.1 \\times 10^{-4}$), indicating the two curation strategies yield practically indistinguishable downstream quality within the $\\pm$2\\% margin.\nCross-seed standard deviation is below 0.001 for both variants.\n\nComparing the full dataset ($n$\\,=\\,12{,}299, ppl\\,=\\,2.335) against the depth-filtered subset ($n$\\,=\\,3{,}951, ppl\\,=\\,2.387): TOST \\emph{rejects} equivalence (minimum equivalence margin\\,=\\,0.053, exceeding the $\\pm$2\\% bound), confirming that data quantity drives perplexity reduction beyond what depth-aware selection can recover.\n\nKnowing the generation depth of a document does not, by itself, make it more or less useful for training; at fixed sample count, depth-aware curation is statistically equivalent to uninformed random subsampling.\n\n\\subsection*{Margin Sensitivity Analysis}\n\nTo assess the robustness of the equivalence conclusion to margin choice, we repeat the TOST procedure across multiple equivalence margins \\cite{lakens_equivalence}, following the recommendation to report sensitivity across plausible bounds rather than relying on a single threshold (Table~\\ref{tab:tost-margins}).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\linewidth}{!}{%\n\\begin{tabular}{llcc}\n\\toprule\n\\textbf{Comparison} & \\textbf{Margin} & \\textbf{Equiv?} & \\textbf{TOST $p$} \\\\\n\\midrule\nFull (12{,}299) vs.\\ Random (3{,}951) & $\\pm$1\\% & No & 1.0 \\\\\n                                        & $\\pm$2\\% & Yes & $1 \\times 10^{-6}$ \\\\\n                                        & $\\pm$3\\% & Yes & $< 10^{-10}$ \\\\\n                                        & $\\pm$5\\% & Yes & $< 10^{-10}$ \\\\\n\\midrule\nFull (12{,}299) vs.\\ Depth 0--1 (3{,}951) & $\\pm$1\\% & No & 1.0 \\\\\n                                            & $\\pm$2\\% & No & 1.0 \\\\\n                                            & $\\pm$3\\% & Yes & $< 10^{-10}$ \\\\\n                                            & $\\pm$5\\% & Yes & $< 10^{-10}$ \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{TOST equivalence testing across multiple margins. ``Equiv?'' indicates whether equivalence is established at $\\alpha = 0.05$.}\n\\label{tab:tost-margins}\n\\end{table}\n\nThe full dataset vs.\\ random subsample comparison passes equivalence at the $\\pm$2\\% margin ($p = 10^{-6}$), while the full vs.\\ depth 0--1 comparison requires a $\\pm$3\\% margin.\nIn absolute terms, perplexity differences are small: $\\Delta$\\,=\\,0.032 (full vs.\\ random, 1.4\\% of baseline) and $\\Delta$\\,=\\,0.052 (full vs.\\ depth 0--1, 2.2\\% of baseline).\n\nCohen's $d$ values are 86.0 (full vs.\\ random) and 119.7 (full vs.\\ depth 0--1).\nThese appear large but are unreliable: with only $n$\\,=\\,3 seeds per condition, the pooled standard deviation is extremely small ($<$0.001), artificially inflating $d$.\nThe inflated effect sizes reflect low seed-level variance (confirming reproducibility) rather than practically meaningful perplexity differences.\nThe TOST framework with pre-specified relative margins provides a more appropriate assessment than Cohen's $d$ in this low-seed regime.\n",
      "numLines": 73,
      "startLine": 1,
      "totalLines": 73
    }
  },
  "sourceToolAssistantUUID": "23ddbcb5-60eb-49b6-b1c4-0b9a1d5592f3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/review_reviewer_2_3f564e41",
  "sessionId": "b64a1fb5-cc00-4ec5-a8b3-b55f8a4cf13d",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---


### Tool call

_source line 57 · 2026-05-17T17:20:08.730Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Mh6ZctWj9m5oeXC9nsaA46`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/table4.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b0fb14f5-b44f-41ea-a470-65ee24a667eb",
  "isSidechain": false,
  "requestId": "req_011Cb8XNZWhLmFAaGYKGmtj2",
  "type": "assistant",
  "uuid": "10351051-2287-41ef-987e-881f88a15232",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/review_reviewer_2_3f564e41",
  "sessionId": "b64a1fb5-cc00-4ec5-a8b3-b55f8a4cf13d",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JKYZKGNbNAfrbDAxAnUwV9",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6315,
      "cache_read_input_tokens": 44775,
      "output_tokens": 320,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 6315,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 320,
          "cache_read_input_tokens": 44775,
          "cache_creation_input_tokens": 6315,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 6315
          },
          "type": "message"
        }
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

_source line 58 · 2026-05-17T17:20:08.734Z_

<details><summary>↩ Tool result · `toolu_01Mh6ZctWj9m5oeXC9nsaA46`</summary>

```text
1	\begin{table}[t]
2	\centering
3	\footnotesize
4	\resizebox{\linewidth}{!}{%
5	\begin{tabular}{llccc}
6	\toprule
7	\textbf{Reference} & \textbf{Family} & \textbf{Params} & \textbf{LOGO F1} & \textbf{Ent.\ Drift} \\
8	\midrule
9	Pythia-410M & Pythia & 410M & 0.803 & [$-$1.19, $-$1.40] \\
10	OLMo-2-1B  & OLMo   & 1.5B & 0.807 & [$-$0.61, $-$0.91] \\
11	Qwen3-0.6B & Qwen   & 0.6B & 0.816 & [$-$0.96, $-$1.35] \\
12	\bottomrule
13	\end{tabular}}
14	\caption{Cross-family reference model validation (5-gen LOGO subset). Drift direction is consistent (negative) across all three references; magnitude varies with capacity. Spread in LOGO F1 is 0.013.}
15	\label{tab:cross-ref}
16	\end{table}
17	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "10351051-2287-41ef-987e-881f88a15232",
  "isSidechain": false,
  "promptId": "c6349ba0-ce02-4cbb-9474-95572d1cbd3f",
  "type": "user",
  "uuid": "c3fb58f5-5302-4d55-a92b-0fd764fe7d1d",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/table4.tex",
      "content": "\\begin{table}[t]\n\\centering\n\\footnotesize\n\\resizebox{\\linewidth}{!}{%\n\\begin{tabular}{llccc}\n\\toprule\n\\textbf{Reference} & \\textbf{Family} & \\textbf{Params} & \\textbf{LOGO F1} & \\textbf{Ent.\\ Drift} \\\\\n\\midrule\nPythia-410M & Pythia & 410M & 0.803 & [$-$1.19, $-$1.40] \\\\\nOLMo-2-1B  & OLMo   & 1.5B & 0.807 & [$-$0.61, $-$0.91] \\\\\nQwen3-0.6B & Qwen   & 0.6B & 0.816 & [$-$0.96, $-$1.35] \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Cross-family reference model validation (5-gen LOGO subset). Drift direction is consistent (negative) across all three references; magnitude varies with capacity. Spread in LOGO F1 is 0.013.}\n\\label{tab:cross-ref}\n\\end{table}\n",
      "numLines": 17,
      "startLine": 1,
      "totalLines": 17
    }
  },
  "sourceToolAssistantUUID": "10351051-2287-41ef-987e-881f88a15232",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/review_reviewer_2_3f564e41",
  "sessionId": "b64a1fb5-cc00-4ec5-a8b3-b55f8a4cf13d",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---


### Tool call

_source line 59 · 2026-05-17T17:20:09.345Z_

<details open><summary>🔧 Tool call — Read · `toolu_01XxVVbtmbwJ4FZBEcAqX9vg`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_downstream.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c3fb58f5-5302-4d55-a92b-0fd764fe7d1d",
  "isSidechain": false,
  "requestId": "req_011Cb8XNZWhLmFAaGYKGmtj2",
  "type": "assistant",
  "uuid": "23ddbcb5-60eb-49b6-b1c4-0b9a1d5592f3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/review_reviewer_2_3f564e41",
  "sessionId": "b64a1fb5-cc00-4ec5-a8b3-b55f8a4cf13d",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JKYZKGNbNAfrbDAxAnUwV9",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6315,
      "cache_read_input_tokens": 44775,
      "output_tokens": 320,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 6315,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 320,
          "cache_read_input_tokens": 44775,
          "cache_creation_input_tokens": 6315,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 6315
          },
          "type": "message"
        }
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

_source line 60_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[Round 1 审稿请求]: 你负责**新颖性 + 完整性 + Related Work + 格式**。  ## Venue 信息 - **目标**: EMNLP 2026（ARR May 2026 cycle） - **截止日期**: 2026-05-25 - **页数限制**: Long paper 正文 8 页（不含 limitations/ethics/references） - **模…",
  "leafUuid": "8c6026c8-f389-4622-967c-d8e526e7d53b",
  "sessionId": "b64a1fb5-cc00-4ec5-a8b3-b55f8a4cf13d"
}
```

---


### Runtime record

_source line 61_

```json
{
  "type": "ai-title",
  "aiTitle": "Review depth fingerprinting paper for EMNLP 2026",
  "sessionId": "b64a1fb5-cc00-4ec5-a8b3-b55f8a4cf13d"
}
```

---


### Assistant

_source line 62 · 2026-05-17T17:20:15.207Z_

<details><summary>Logged reasoning block</summary>

```text
Let me also read the remaining references and check the paper visually using pdf_to_images. Let me also look at the appendix on dataset stats to understand scale.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8c6026c8-f389-4622-967c-d8e526e7d53b",
  "isSidechain": false,
  "requestId": "req_011Cb8XP9jjdhpxRNeAWhGjP",
  "type": "assistant",
  "uuid": "bb61cc3d-6148-45a0-bcbd-95b483e400a0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/review_reviewer_2_3f564e41",
  "sessionId": "b64a1fb5-cc00-4ec5-a8b3-b55f8a4cf13d",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PfgUZLpd2rp9DG4JiftknY",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6408,
      "cache_read_input_tokens": 51090,
      "output_tokens": 253,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 6408,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 253,
          "cache_read_input_tokens": 51090,
          "cache_creation_input_tokens": 6408,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 6408
          },
          "type": "message"
        }
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

_source line 63 · 2026-05-17T17:20:17.757Z_

<details open><summary>🔧 Tool call — Read · `toolu_012yYEbNRVKD12Z3ZZkHnSQH`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/references.bib",
  "offset": 399,
  "limit": 100
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bb61cc3d-6148-45a0-bcbd-95b483e400a0",
  "isSidechain": false,
  "requestId": "req_011Cb8XP9jjdhpxRNeAWhGjP",
  "type": "assistant",
  "uuid": "031f560b-823e-4136-98c1-99e3bf945525",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/review_reviewer_2_3f564e41",
  "sessionId": "b64a1fb5-cc00-4ec5-a8b3-b55f8a4cf13d",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PfgUZLpd2rp9DG4JiftknY",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6408,
      "cache_read_input_tokens": 51090,
      "output_tokens": 253,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 6408,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 253,
          "cache_read_input_tokens": 51090,
          "cache_creation_input_tokens": 6408,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 6408
          },
          "type": "message"
        }
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

_source line 64 · 2026-05-17T17:20:17.760Z_

<details><summary>↩ Tool result · `toolu_012yYEbNRVKD12Z3ZZkHnSQH`</summary>

```text
399	@article{coral_ordinal,
400	  title = {{Rank Consistent Ordinal Regression for Neural Networks with Application to Age Estimation}},
401	  author = {Cao, Wenzhi and Mirjalili, Vahid and Raschka, Sebastian},
402	  journal = {Pattern Recognition Letters},
403	  volume = {140},
404	  pages = {325--331},
405	  year = {2020},
406	}
407	
408	@inproceedings{frank_hall_ordinal,
409	  title = {{A Simple Approach to Ordinal Classification}},
410	  author = {Frank, Eibe and Hall, Mark},
411	  booktitle = {Proceedings of the European Conference on Machine Learning},
412	  year = {2001},
413	}
414	
415	@inproceedings{xgboost,
416	  title = {{XGBoost: A Scalable Tree Boosting System}},
417	  author = {Chen, Tianqi and Guestrin, Carlos},
418	  booktitle = {Proceedings of the ACM SIGKDD International Conference on Knowledge Discovery and Data Mining},
419	  year = {2016},
420	}
421	
422	@article{lakens_equivalence,
423	  title = {{Equivalence Tests: A Practical Primer for $t$ Tests, Correlations, and Meta-Analyses}},
424	  author = {Lakens, Dani{\"e}l},
425	  journal = {Social Psychological and Personality Science},
426	  volume = {8},
427	  number = {4},
428	  pages = {355--362},
429	  year = {2017},
430	}
431	
432	% ===== Generator Model References =====
433	
434	@article{llama3,
435	  title = {{The Llama 3 Herd of Models}},
436	  author = {Grattafiori, Aaron and Dubey, Abhimanyu and Jauhri, Abhinav and Pandey, Abhinav and Kadian, Abhishek and Al-Dahle, Ahmad and Letman, Aiesha and Mathur, Akhil and Schelten, Alan and Yang, Amy and others},
437	  journal = {arXiv preprint arXiv:2407.21783},
438	  year = {2024},
439	}
440	
441	@article{mistral7b,
442	  title = {{Mistral 7B}},
443	  author = {Jiang, Albert Q. and Sablayrolles, Alexandre and Mensch, Arthur and Bamford, Chris and Chaplot, Devendra Singh and Casas, Diego de las and Bressand, Florian and Lengyel, Gianna and Lample, Guillaume and Saulnier, Lucile and others},
444	  journal = {arXiv preprint arXiv:2310.06825},
445	  year = {2023},
446	}
447	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "031f560b-823e-4136-98c1-99e3bf945525",
  "isSidechain": false,
  "promptId": "c6349ba0-ce02-4cbb-9474-95572d1cbd3f",
  "type": "user",
  "uuid": "c9386889-1193-4d91-9aa1-760055269570",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/references.bib",
      "content": "@article{coral_ordinal,\n  title = {{Rank Consistent Ordinal Regression for Neural Networks with Application to Age Estimation}},\n  author = {Cao, Wenzhi and Mirjalili, Vahid and Raschka, Sebastian},\n  journal = {Pattern Recognition Letters},\n  volume = {140},\n  pages = {325--331},\n  year = {2020},\n}\n\n@inproceedings{frank_hall_ordinal,\n  title = {{A Simple Approach to Ordinal Classification}},\n  author = {Frank, Eibe and Hall, Mark},\n  booktitle = {Proceedings of the European Conference on Machine Learning},\n  year = {2001},\n}\n\n@inproceedings{xgboost,\n  title = {{XGBoost: A Scalable Tree Boosting System}},\n  author = {Chen, Tianqi and Guestrin, Carlos},\n  booktitle = {Proceedings of the ACM SIGKDD International Conference on Knowledge Discovery and Data Mining},\n  year = {2016},\n}\n\n@article{lakens_equivalence,\n  title = {{Equivalence Tests: A Practical Primer for $t$ Tests, Correlations, and Meta-Analyses}},\n  author = {Lakens, Dani{\\\"e}l},\n  journal = {Social Psychological and Personality Science},\n  volume = {8},\n  number = {4},\n  pages = {355--362},\n  year = {2017},\n}\n\n% ===== Generator Model References =====\n\n@article{llama3,\n  title = {{The Llama 3 Herd of Models}},\n  author = {Grattafiori, Aaron and Dubey, Abhimanyu and Jauhri, Abhinav and Pandey, Abhinav and Kadian, Abhishek and Al-Dahle, Ahmad and Letman, Aiesha and Mathur, Akhil and Schelten, Alan and Yang, Amy and others},\n  journal = {arXiv preprint arXiv:2407.21783},\n  year = {2024},\n}\n\n@article{mistral7b,\n  title = {{Mistral 7B}},\n  author = {Jiang, Albert Q. and Sablayrolles, Alexandre and Mensch, Arthur and Bamford, Chris and Chaplot, Devendra Singh and Casas, Diego de las and Bressand, Florian and Lengyel, Gianna and Lample, Guillaume and Saulnier, Lucile and others},\n  journal = {arXiv preprint arXiv:2310.06825},\n  year = {2023},\n}\n",
      "numLines": 49,
      "startLine": 399,
      "totalLines": 447
    }
  },
  "sourceToolAssistantUUID": "031f560b-823e-4136-98c1-99e3bf945525",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/review_reviewer_2_3f564e41",
  "sessionId": "b64a1fb5-cc00-4ec5-a8b3-b55f8a4cf13d",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---


### Tool result

_source line 65 · 2026-05-17T17:20:18.281Z_

<details><summary>↩ Tool result · `toolu_013r7GmfV4JbRLmcQjyajBfE`</summary>

```text
1	\section{Dataset Statistics}
2	\label{app:dataset-stats}
3	
4	Table~\ref{tab:dataset-stats} reports per-generator sample counts after filtering (removing generation failures, exact duplicates, and passages shorter than 50 whitespace tokens).
5	
6	\begin{table}[t]
7	\centering
8	\small
9	\begin{tabular}{llcc}
10	\toprule
11	\textbf{Generator} & \textbf{Family} & \textbf{Params} & \textbf{Samples} \\
12	\midrule
13	Pythia-1B       & Pythia  & 1.0B & 4{,}555 \\
14	Pythia-2.8B     & Pythia  & 2.8B & 4{,}609 \\
15	OLMo-2-1B      & OLMo    & 1.5B & 4{,}713 \\
16	Qwen3-0.6B     & Qwen    & 0.6B & 4{,}538 \\
17	Qwen3-1.7B     & Qwen    & 1.7B & 4{,}617 \\
18	Qwen3-8B       & Qwen    & 8.2B & 4{,}497 \\
19	Llama-3.2-3B   & Llama   & 3.2B & 4{,}680 \\
20	Mistral-7B-v0.3 & Mistral & 7.0B & 4{,}849 \\
21	\midrule
22	\multicolumn{3}{l}{\textbf{Total}} & \textbf{37{,}058} \\
23	\bottomrule
24	\end{tabular}
25	\caption[Per-generator sample counts]{Per-generator sample counts after filtering (8 generators, 5 families). Each generator starts from ${\sim}$1{,}000 shared Wikipedia seeds and produces chains of depth 4 (5 texts per chain). Attrition varies by generator due to differing generation failure rates.\protect\footnotemark}
26	\label{tab:dataset-stats}
27	\end{table}
28	\footnotetext{Table~\ref{tab:baselines} evaluates on a subset of 34{,}131 samples for which all detector scores (FastDetectGPT, Binoculars, LD-Score, Avg-LogProb) are available.}
29	
30	Figure~\ref{fig:violin} shows the full distribution of each feature across five generation depths (0--4), pooled across all eight generators ($N$\,=\,37{,}058).
31	The violin plots confirm the DDR pattern: drifting features (entropy mean, TTR, hapax ratio) show progressive narrowing and location shift, while shape features (entropy max, tail decay) maintain approximately constant distributions across depths.
32	
33	\begin{figure*}[ht]
34	\centering
35	\includegraphics[width=\textwidth]{fig_appendix_violin.pdf}
36	\caption{Feature distributions by generation depth (violin plots, $N$\,=\,37{,}058). Drifting features (entropy mean, TTR, hapax ratio: $|\rho| > 0.60$) show clear location shifts and narrowing with increasing depth. Shape features (entropy max, tail decay: $|\rho| < 0.10$) remain approximately stationary. Quartile lines indicate median and interquartile range.}
37	\label{fig:violin}
38	\end{figure*}
39	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "534deb47-689a-43e5-9afc-07350ec74a5c",
  "isSidechain": false,
  "promptId": "c6349ba0-ce02-4cbb-9474-95572d1cbd3f",
  "type": "user",
  "uuid": "1460eeae-3c20-46ba-83d8-34d592a8b739",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_dataset_stats.tex",
      "content": "\\section{Dataset Statistics}\n\\label{app:dataset-stats}\n\nTable~\\ref{tab:dataset-stats} reports per-generator sample counts after filtering (removing generation failures, exact duplicates, and passages shorter than 50 whitespace tokens).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{llcc}\n\\toprule\n\\textbf{Generator} & \\textbf{Family} & \\textbf{Params} & \\textbf{Samples} \\\\\n\\midrule\nPythia-1B       & Pythia  & 1.0B & 4{,}555 \\\\\nPythia-2.8B     & Pythia  & 2.8B & 4{,}609 \\\\\nOLMo-2-1B      & OLMo    & 1.5B & 4{,}713 \\\\\nQwen3-0.6B     & Qwen    & 0.6B & 4{,}538 \\\\\nQwen3-1.7B     & Qwen    & 1.7B & 4{,}617 \\\\\nQwen3-8B       & Qwen    & 8.2B & 4{,}497 \\\\\nLlama-3.2-3B   & Llama   & 3.2B & 4{,}680 \\\\\nMistral-7B-v0.3 & Mistral & 7.0B & 4{,}849 \\\\\n\\midrule\n\\multicolumn{3}{l}{\\textbf{Total}} & \\textbf{37{,}058} \\\\\n\\bottomrule\n\\end{tabular}\n\\caption[Per-generator sample counts]{Per-generator sample counts after filtering (8 generators, 5 families). Each generator starts from ${\\sim}$1{,}000 shared Wikipedia seeds and produces chains of depth 4 (5 texts per chain). Attrition varies by generator due to differing generation failure rates.\\protect\\footnotemark}\n\\label{tab:dataset-stats}\n\\end{table}\n\\footnotetext{Table~\\ref{tab:baselines} evaluates on a subset of 34{,}131 samples for which all detector scores (FastDetectGPT, Binoculars, LD-Score, Avg-LogProb) are available.}\n\nFigure~\\ref{fig:violin} shows the full distribution of each feature across five generation depths (0--4), pooled across all eight generators ($N$\\,=\\,37{,}058).\nThe violin plots confirm the DDR pattern: drifting features (entropy mean, TTR, hapax ratio) show progressive narrowing and location shift, while shape features (entropy max, tail decay) maintain approximately constant distributions across depths.\n\n\\begin{figure*}[ht]\n\\centering\n\\includegraphics[width=\\textwidth]{fig_appendix_violin.pdf}\n\\caption{Feature distributions by generation depth (violin plots, $N$\\,=\\,37{,}058). Drifting features (entropy mean, TTR, hapax ratio: $|\\rho| > 0.60$) show clear location shifts and narrowing with increasing depth. Shape features (entropy max, tail decay: $|\\rho| < 0.10$) remain approximately stationary. Quartile lines indicate median and interquartile range.}\n\\label{fig:violin}\n\\end{figure*}\n",
      "numLines": 39,
      "startLine": 1,
      "totalLines": 39
    }
  },
  "sourceToolAssistantUUID": "534deb47-689a-43e5-9afc-07350ec74a5c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/review_reviewer_2_3f564e41",
  "sessionId": "b64a1fb5-cc00-4ec5-a8b3-b55f8a4cf13d",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---


### Tool call

_source line 66 · 2026-05-17T17:20:18.278Z_

<details open><summary>🔧 Tool call — Read · `toolu_013r7GmfV4JbRLmcQjyajBfE`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_dataset_stats.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c9386889-1193-4d91-9aa1-760055269570",
  "isSidechain": false,
  "requestId": "req_011Cb8XP9jjdhpxRNeAWhGjP",
  "type": "assistant",
  "uuid": "534deb47-689a-43e5-9afc-07350ec74a5c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/review_reviewer_2_3f564e41",
  "sessionId": "b64a1fb5-cc00-4ec5-a8b3-b55f8a4cf13d",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PfgUZLpd2rp9DG4JiftknY",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6408,
      "cache_read_input_tokens": 51090,
      "output_tokens": 253,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 6408,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 253,
          "cache_read_input_tokens": 51090,
          "cache_creation_input_tokens": 6408,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 6408
          },
          "type": "message"
        }
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

_source line 67 · 2026-05-17T17:20:22.475Z_

<details><summary>Logged reasoning block</summary>

```text
Now let me look at the paper visually to check formatting, page count, and overall presentation. Let me also check what the PDF looks like.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1460eeae-3c20-46ba-83d8-34d592a8b739",
  "isSidechain": false,
  "requestId": "req_011Cb8XPosfuXPrNNKQsHaC9",
  "type": "assistant",
  "uuid": "a515adfa-ddc0-43e3-967a-cc9b3bf54cc2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/review_reviewer_2_3f564e41",
  "sessionId": "b64a1fb5-cc00-4ec5-a8b3-b55f8a4cf13d",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WJ91d1yJ1VVB8NpiDbeh6v",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2003,
      "cache_read_input_tokens": 57498,
      "output_tokens": 193,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2003,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 193,
          "cache_read_input_tokens": 57498,
          "cache_creation_input_tokens": 2003,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2003
          },
          "type": "message"
        }
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

_source line 68 · 2026-05-17T17:20:23.095Z_

让我检查论文 PDF 的视觉格式和页数。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a515adfa-ddc0-43e3-967a-cc9b3bf54cc2",
  "isSidechain": false,
  "requestId": "req_011Cb8XPosfuXPrNNKQsHaC9",
  "type": "assistant",
  "uuid": "34ff44e5-8afd-42a9-a41c-ca2e092d2636",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/review_reviewer_2_3f564e41",
  "sessionId": "b64a1fb5-cc00-4ec5-a8b3-b55f8a4cf13d",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WJ91d1yJ1VVB8NpiDbeh6v",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2003,
      "cache_read_input_tokens": 57498,
      "output_tokens": 193,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2003,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 193,
          "cache_read_input_tokens": 57498,
          "cache_creation_input_tokens": 2003,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2003
          },
          "type": "message"
        }
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

_source line 69 · 2026-05-17T17:20:24.063Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01YUrdi53YdgxyvdGqQ4KxQJ`</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/ -name \"*.pdf\" -not -path \"*_pdf_images*\" | head -5",
  "description": "Find compiled PDF files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "34ff44e5-8afd-42a9-a41c-ca2e092d2636",
  "isSidechain": false,
  "requestId": "req_011Cb8XPosfuXPrNNKQsHaC9",
  "type": "assistant",
  "uuid": "ee296baf-1746-40a2-9e8b-77e43babc801",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/review_reviewer_2_3f564e41",
  "sessionId": "b64a1fb5-cc00-4ec5-a8b3-b55f8a4cf13d",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WJ91d1yJ1VVB8NpiDbeh6v",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2003,
      "cache_read_input_tokens": 57498,
      "output_tokens": 193,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2003,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 193,
          "cache_read_input_tokens": 57498,
          "cache_creation_input_tokens": 2003,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2003
          },
          "type": "message"
        }
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

_source line 70 · 2026-05-17T17:20:24.195Z_

<details><summary>↩ Tool result · `toolu_01YUrdi53YdgxyvdGqQ4KxQJ`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/figures/fig2_framework.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/fig1_differential_response.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/fig3_baseline_comparison.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/main.pdf
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ee296baf-1746-40a2-9e8b-77e43babc801",
  "isSidechain": false,
  "promptId": "c6349ba0-ce02-4cbb-9474-95572d1cbd3f",
  "type": "user",
  "uuid": "ac2b9045-b865-4785-b615-24bcecad291b",
  "toolUseResult": {
    "stdout": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/figures/fig2_framework.pdf\n/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/fig1_differential_response.pdf\n/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/fig3_baseline_comparison.pdf\n/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/main.pdf",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "ee296baf-1746-40a2-9e8b-77e43babc801",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/review_reviewer_2_3f564e41",
  "sessionId": "b64a1fb5-cc00-4ec5-a8b3-b55f8a4cf13d",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---


### Runtime record

_source line 71 · 2026-05-17T17:20:24.197Z_

```json
{
  "parentUuid": "ac2b9045-b865-4785-b615-24bcecad291b",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "ecce030a-480c-49cd-8000-d48230fd7231",
  "timestamp": "2026-05-17T17:20:24.197Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/review_reviewer_2_3f564e41",
  "sessionId": "b64a1fb5-cc00-4ec5-a8b3-b55f8a4cf13d",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

---


### Tool call

_source line 72 · 2026-05-17T17:20:29.114Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images · `toolu_01BGgP75BjMA6MfNuaibxKmu`</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/main.pdf",
  "pages": "1-12",
  "dpi": 150
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ecce030a-480c-49cd-8000-d48230fd7231",
  "isSidechain": false,
  "requestId": "req_011Cb8XQGWoN4GMM4G6fPY1G",
  "type": "assistant",
  "uuid": "782945fd-2cd3-4320-8a4a-9670aac19503",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/review_reviewer_2_3f564e41",
  "sessionId": "b64a1fb5-cc00-4ec5-a8b3-b55f8a4cf13d",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JyN5jz1qFU29Ms1va2SLkM",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 477,
      "cache_read_input_tokens": 59501,
      "output_tokens": 140,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 477,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 140,
          "cache_read_input_tokens": 59501,
          "cache_creation_input_tokens": 477,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 477
          },
          "type": "message"
        }
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

_source line 73 · 2026-05-17T17:20:32.399Z_

<details><summary>↩ Tool result · `toolu_01BGgP75BjMA6MfNuaibxKmu`</summary>

```text
Error: result (8,180,559 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-3-projects-gen-depth-fingerprint--claude-sessions-review-reviewer-2-3f564e41/b64a1fb5-cc00-4ec5-a8b3-b55f8a4cf13d/tool-results/mcp-agent-ml-research-pdf_to_images-1779038432384.txt.
Format: JSON with schema: {result: string}
- For targeted queries (find a value, filter by field): use jq on the file directly.
- For analysis or summarization that requires reading the full content: first probe the structure (e.g., jq 'type, length, keys?' /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-3-projects-gen-depth-fingerprint--claude-sessions-review-reviewer-2-3f564e41/b64a1fb5-cc00-4ec5-a8b3-b55f8a4cf13d/tool-results/mcp-agent-ml-research-pdf_to_images-1779038432384.txt), then extract slices with jq or python — Read's line-based offset/limit will not chunk this file.
- If the Agent tool is available, do this inside a subagent so the full output stays out of your main context. Give it the instruction above verbatim, and be explicit about what it must return — e.g. "/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-3-projects-gen-depth-fingerprint--claude-sessions-review-reviewer-2-3f564e41/b64a1fb5-cc00-4ec5-a8b3-b55f8a4cf13d/tool-results/mcp-agent-ml-research-pdf_to_images-1779038432384.txt is JSON with schema: {result: string}; probe the structure with jq (type/length/keys), then extract and read the content in full with jq or python, then summarize and quote any key findings verbatim." A vague "summarize this" may lose detail.

```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "782945fd-2cd3-4320-8a4a-9670aac19503",
  "isSidechain": false,
  "promptId": "c6349ba0-ce02-4cbb-9474-95572d1cbd3f",
  "type": "user",
  "uuid": "b13abbda-d806-4863-bfea-7fdd11481b1f",
  "toolUseResult": "Error: result (8,180,559 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-3-projects-gen-depth-fingerprint--claude-sessions-review-reviewer-2-3f564e41/b64a1fb5-cc00-4ec5-a8b3-b55f8a4cf13d/tool-results/mcp-agent-ml-research-pdf_to_images-1779038432384.txt.\nFormat: JSON with schema: {result: string}\n- For targeted queries (find a value, filter by field): use jq on the file directly.\n- For analysis or summarization that requires reading the full content: first probe the structure (e.g., jq 'type, length, keys?' /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-3-projects-gen-depth-fingerprint--claude-sessions-review-reviewer-2-3f564e41/b64a1fb5-cc00-4ec5-a8b3-b55f8a4cf13d/tool-results/mcp-agent-ml-research-pdf_to_images-1779038432384.txt), then extract slices with jq or python — Read's line-based offset/limit will not chunk this file.\n- If the Agent tool is available, do this inside a subagent so the full output stays out of your main context. Give it the instruction above verbatim, and be explicit about what it must return — e.g. \"/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-3-projects-gen-depth-fingerprint--claude-sessions-review-reviewer-2-3f564e41/b64a1fb5-cc00-4ec5-a8b3-b55f8a4cf13d/tool-results/mcp-agent-ml-research-pdf_to_images-1779038432384.txt is JSON with schema: {result: string}; probe the structure with jq (type/length/keys), then extract and read the content in full with jq or python, then summarize and quote any key findings verbatim.\" A vague \"summarize this\" may lose detail.\n",
  "mcpMeta": {
    "storage": "sanitized-trace-archive",
    "source_line": 73,
    "serialized_bytes": 8180596,
    "serialized_sha256": "eab9355d74dfc8e541b192e21e58367068d156c87fd9fa41ac18c01755e2b2a7",
    "note": "Complete sanitized source is retained in trace-files.tar.gz."
  },
  "sourceToolAssistantUUID": "782945fd-2cd3-4320-8a4a-9670aac19503",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/review_reviewer_2_3f564e41",
  "sessionId": "b64a1fb5-cc00-4ec5-a8b3-b55f8a4cf13d",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---


### Runtime record

_source line 74_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[Round 1 审稿请求]: 你负责**新颖性 + 完整性 + Related Work + 格式**。  ## Venue 信息 - **目标**: EMNLP 2026（ARR May 2026 cycle） - **截止日期**: 2026-05-25 - **页数限制**: Long paper 正文 8 页（不含 limitations/ethics/references） - **模…",
  "leafUuid": "b13abbda-d806-4863-bfea-7fdd11481b1f",
  "sessionId": "b64a1fb5-cc00-4ec5-a8b3-b55f8a4cf13d"
}
```

---


### Runtime record

_source line 75_

```json
{
  "type": "ai-title",
  "aiTitle": "Review depth fingerprinting paper for EMNLP 2026",
  "sessionId": "b64a1fb5-cc00-4ec5-a8b3-b55f8a4cf13d"
}
```

---


### Assistant

_source line 76 · 2026-05-17T17:20:36.142Z_

<details><summary>Logged reasoning block</summary>

```text
Let me try rendering just a few pages at a time to check the formatting visually.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b13abbda-d806-4863-bfea-7fdd11481b1f",
  "isSidechain": false,
  "requestId": "req_011Cb8XQrQ1385bMn3v16SMp",
  "type": "assistant",
  "uuid": "65c7415f-a03e-49b9-91f0-84acb90ad659",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/review_reviewer_2_3f564e41",
  "sessionId": "b64a1fb5-cc00-4ec5-a8b3-b55f8a4cf13d",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LUJggK5Tbbk5NLSd85QPpC",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 716,
      "cache_read_input_tokens": 59978,
      "output_tokens": 173,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 716,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 173,
          "cache_read_input_tokens": 59978,
          "cache_creation_input_tokens": 716,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 716
          },
          "type": "message"
        }
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

_source line 77 · 2026-05-17T17:20:36.807Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images · `toolu_0149sB6hEd8fK6aL6X5C3yf6`</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/main.pdf",
  "pages": "1-2",
  "dpi": 150
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "65c7415f-a03e-49b9-91f0-84acb90ad659",
  "isSidechain": false,
  "requestId": "req_011Cb8XQrQ1385bMn3v16SMp",
  "type": "assistant",
  "uuid": "b600fbe6-eb60-40da-8c34-0831ff26dd89",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/review_reviewer_2_3f564e41",
  "sessionId": "b64a1fb5-cc00-4ec5-a8b3-b55f8a4cf13d",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LUJggK5Tbbk5NLSd85QPpC",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 716,
      "cache_read_input_tokens": 59978,
      "output_tokens": 173,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 716,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 173,
          "cache_read_input_tokens": 59978,
          "cache_creation_input_tokens": 716,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 716
          },
          "type": "message"
        }
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

_source line 78 · 2026-05-17T17:20:37.492Z_

&lt;details>&lt;summary>↩ Tool result · `toolu_0149sB6hEd8fK6aL6X5C3yf6`&lt;/summary>

```text
Error: result (1,304,174 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-3-projects-gen-depth-fingerprint--claude-sessions-review-reviewer-2-3f564e41/b64a1fb5-cc00-4ec5-a8b3-b55f8a4cf13d/tool-results/mcp-agent-ml-research-pdf_to_images-1779038437489.txt.
Format: JSON with schema: {result: string}
- For targeted queries (find a value, filter by field): use jq on the file directly.
- For analysis or summarization that requires reading the full content: first probe the structure (e.g., jq 'type, length, keys?' /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-3-projects-gen-depth-fingerprint--claude-sessions-review-reviewer-2-3f564e41/b64a1fb5-cc00-4ec5-a8b3-b55f8a4cf13d/tool-results/mcp-agent-ml-research-pdf_to_images-1779038437489.txt), then extract slices with jq or python — Read's line-based offset/limit will not chunk this file.
- If the Agent tool is available, do this inside a subagent so the full output stays out of your main context. Give it the instruction above verbatim, and be explicit about what it must return — e.g. "/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-3-projects-gen-depth-fingerprint--claude-sessions-review-reviewer-2-3f564e41/b64a1fb5-cc00-4ec5-a8b3-b55f8a4cf13d/tool-results/mcp-agent-ml-research-pdf_to_images-1779038437489.txt is JSON with schema: {result: string}; probe the structure with jq (type/length/keys), then extract and read the content in full with jq or python, then summarize and quote any key findings verbatim." A vague "summarize this" may lose detail.

```

&lt;/details>

&lt;details>&lt;summary>Recorded metadata&lt;/summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b600fbe6-eb60-40da-8c34-0831ff26dd89",
  "isSidechain": false,
  "promptId": "c6349ba0-ce02-4cbb-9474-95572d1cbd3f",
  "type": "user",
  "uuid": "813ea201-b7ed-474d-a9bf-560650988f42",
  "toolUseResult": "Error: result (1,304,174 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-3-projects-gen-depth-fingerprint--claude-sessions-review-reviewer-2-3f564e41/b64a1fb5-cc00-4ec5-a8b3-b55f8a4cf13d/tool-results/mcp-agent-ml-research-pdf_to_images-1779038437489.txt.\nFormat: JSON with schema: {result: string}\n- For targeted queries (find a value, filter by field): use jq on the file directly.\n- For analysis or summarization that requires reading the full content: first probe the structure (e.g., jq 'type, length, keys?' /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-3-projects-gen-depth-fingerprint--claude-sessions-review-reviewer-2-3f564e41/b64a1fb5-cc00-4ec5-a8b3-b55f8a4cf13d/tool-results/mcp-agent-ml-research-pdf_to_images-1779038437489.txt), then extract slices with jq or python — Read's line-based offset/limit will not chunk this file.\n- If the Agent tool is available, do this inside a subagent so the full output stays out of your main context. Give it the instruction above verbatim, and be explicit about what it must return — e.g. \"/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-3-projects-gen-depth-fingerprint--claude-sessions-review-reviewer-2-3f564e41/b64a1fb5-cc00-4ec5-a8b3-b55f8a4cf13d/tool-results/mcp-agent-ml-research-pdf_to_images-1779038437489.txt is JSON with schema: {result: string}; probe the structure with jq (type/length/keys), then extract and read the content in full with jq or python, then summarize and quote any key findings verbatim.\" A vague \"summarize this\" may lose detail.\n",
  "mcpMeta": {
    "structuredContent": {

````

---

### Large event (continued)

```text
      "result": "{\"success\": true, \"data\": {\"images\": [{\"page\": 1, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/_pdf_images/main_p1.png\", \"base64\": \"iVBORw0KGgoAAAANSUhEUgAABNkAAAbaCAIAAAB3QTY3AAAACXBIWXMAABcSAAAXEgFnn9JSAAbXnElEQVR4nOzdd5wV1R03fhQQUYyiYEMQ7DVqFEvsvSsaWyxJNHYfNZaI/WVMTOzR2I0lNtSIDVHsLWpiwYYaUVFQwYIoRRGk7O/77PxynvHu7mV2gdldfb//4MWee2bmTLkz53OntakBAACAcrVp7gYAAADwoyOLAgAAUDZZFAAAgLLJogAAAJRNFgUAAKBssigAAABlk0UBAAAomywKAABA2WRRAAAAyiaLAgAAUDZZFAAAgLLJogAAAJRNFgUAAKBssigAAABlk0UBAAAomywKAABA2WRRAAAAyiaLAgAAUDZZFAAAgLLJogAAAJRNFgUAAKBssigAAABlk0UBAAAomywKAABA2WRRAAAAyiaLAgAAUDZZFAAAgLLJogAAAJRNFgUAAKBssigAAABlk0UBAAAomywKAABA2WRRAAAAyiaLAgAAUDZZFAAAgLLJogAAAJRNFgUAAKBssigAAABlk0UBAAAomywKAABA2WRRAAAAyiaLAgAAUDZZFAAAgLLJogAAAJRNFgUAAKBssigAAABlk0UBAAAomywKAABA2WRRAAAAyiaLAgAAUDZZFAAAgLLJogAAAJRNFgUAAKBssigAAABlk0UBAAAomywKAABA2WRRAAAAyiaLAgAAUDZZFAAAgLLJogAAAJRNFgUAAKBssigAAABlk0UBAAAomywKAABA2WRRAAAAyiaLAgAAUDZZFAAAgLLJogAAAJRNFgUAAKBssigAAABlk0UBAAAomywKAABA2WRRAAAAyiaLAgAAUDZZFAAAgLLJogAAAJRNFgUAAKBssigAAABlk0UBAAAomywKAABA2WRRAAAAyiaLAgAAUDZZFAAAgLLJogAAAJRNFgUAAKBssigAAABlk0UBAAAomywKAABA2WRRAAAAyiaLAgAAUDZZFAAAgLLJogAAAJRNFgUAAKBssigAAABlk0UBAAAomywKAABA2WRRAAAAyiaLAgAAUDZZFAAAgLLJogAAAJRNFgUAAKBssigAAABlk0UBAAAomywKAABA2WRRAAAAyiaLAgAAUDZZFAAAgLLJogAAAJRNFgUAAKBssigAAABlk0UBAAAomywKAABA2WRRAAAAyiaLAgAAUDZZFAAAgLLJogAAAJRNFgUAAKBssigAAABlk0UBAAAomywKAABA2WRRAAAAyiaLAgAAUDZZFAAAgLLJogAAAJRNFgUAAKBssigAAABlk0UBAAAomywKAABA2WRRAAAAyiaLAgAAUDZZFAAAgLLJogAAAJRNFgUAAKBssigAAABlk0UBAAAomywKAABA2WRRAAAAyiaLAgAAUDZZFAAAgLLJogAAAJRNFgUAAKBssigAAABlk0UBAAAomywKAABA2WRRAAAAyiaLAgAAUDZZFAAAgLLJogAAAJRNFgUAAKBssigAAABlk0UBAAAomywKAABA2WRRAAAAyiaLAgAAUDZZFAAAgLLJogAAAJRNFgUAAKBssigAAABlk0UBAAAomywKAABA2WRRAAAAyiaLAgAAUDZZFAAAgLLJogAAAJRNFgUAAKBssiitw5QpU15s2JAhQz7++ONJkyY1dzPrMXLkyIrWfv3117NkPDP0+eefZ8OOGTPmtNNOO/roo996661ZOnM/EKUtn1a0IkaMGNHQdjV48OD33nvvyy+/bO42zi4DBw489NBDr7jiiqlTpzZjM2JHUeXb/eqrr44aNap5W1i+FrJq8l5//fWLLrro2GOP3X///fv27XvVVVd98MEH+U9vu+225mtdC9IS1p2OBLRAsiitQ+x2995770UXXbRNHV27du3Ro8ectdZYY43f/e53b7zxRnO39/+57777lltuuXyD//3vfzdtPDvvvPPcc89dMftzzTXXCiussPzyyy+22GIVH11yySUx4LRp01ZbbbWsZL755otD2qyexdattOXTulZEdKA33njjul+3du3aLbPMMj/5yU+yr15sk9ddd923337b3O2dZe688840s8cdd1wztmT48OF77bXXIossUrEK5phjjqWXXjorj/8vvPDCv/jFLwYNGhQbWDO2tgQtZ9WE6dOn33zzzcsuu2w0pnPnzkcdddTf//73s88+O9ZF7JN/9rOfnXfeeY899lj851e/+lXzNrUlaCHrTkcCWiBZlNZk4sSJ0Q/O747jeJ99NG7cuHPPPTc6AVn5dttt9/HHHzdLI/fff/+nnnoqXxJti8PbLDmEvP766xVH0GHDhuUndO+9926wwQbZR1kWHTp0aL7+jTfe2OSp/yDNpuVTdzNojSvimmuuybc5+nCxjWUfPffcc+uvv35W3qVLl+iIz5Ip1l1us8+LL764xx57VBRG/Evz26tXr3JaUsWECRMqfma66KKLso8+//zzfGsjoL7yyivN29rZquWsmi+++GKjjTbKWvLzn/88XYGSefPNN9ddd93U1B9bFm35XysdCWhRZFFamf322y9/CPnXv/6V//TRRx9NO+vOnTuX1qlNLr300pj0fffdV1GenUeaJYeQhRZaKI1qnnnmqVth2rRp0RVo878sOn78+KiWBokIMTNT/+GZHcun3s2gNa6I999/P/9122yzzfKfTpo0acstt0yf7rnnnjN59V1DX5/ZITp20Sf+2c9+VlF+2mmnpTnaaqutSmjJDGVf5+SJJ55IH8WXPX+2JHYOo0aNar6Wzl4tZNV8+umnEfuzZiy88MIVQTQTX4Qddtghq/OjyqKt5WulIwEthyxKK3PAAQdUOYSEY445Jn06//zzl3mZTTSmffv2s/sQsvjii6dR1ZtFa2pPmHTq1CnLouGee+5ZaqmlFllkkXPOOWdmJv1DNWuXT5XNoNWtiI8++qhKFg0ff/xxbGmpwoEHHtjkaVVZbrNcRLjtttsuplW30zxhwoTdd999gQUW2Gijjd57773Z3ZIiDj744IayaPjTn/6U/7Rv377N1MzZriWsmilTpmy44YZpaZ977rkN1Zw4ceLaa6/9o8qirehrpSMBLYcsSiszw0NIRe953XXXLadhQ4YM6dKlSzbR5sqib7/99ujRo7P/77333imLUprqm0GrM8MsGn7729/m6zz00ENNmFCZy2369OmHHXZYNq26neYWqHoWvfHGG/OfRlJqpmb+KPztb3/LL+16T4omsUOOUPEjyaKt62ulIwEthyxKKzPDQ0jI36sTBg4cWLdOHDgjtk2cOLH4pL/66quU9CoMHjx4wQUXTFMseAiZNGnSZ599VrwBmSpZtE+fPo888kj2//79+zf5+Y3jx49PtwVWEUvvk08+mTJlygxrNmFp19T+lB6q14mpjxo1qlFPPpw2bVos9mhSoxqT19DymeFmMKsmVKHgipg8eXKRlZVXJItG+MzXWXPNNesdVZWtvfhyK74hTZ069dNPP637UKVY+/l9yMx3mguuoxCzH5WbMInqWXTAgAH5TzfaaKOGxlN8hxPtbMKuqVEa+nbHKs6vuG+++WY2PXa1CTulaFX+sTerrrrqDAc55JBDqmTRpu0Yi2xy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55xzzjvvvFdcccWkSZPSXcptZjqL7rLLLqmwYsPLf5TuVi05i9bbkahpzJ6tCccsWZQfIVmUVqbIIST/JJXoJWddmbFjx+YHzE7dNKRKFk0PKmyTe4RpTcvIouedd97zzz9fd5BZmLWiLxIJPOthRyfmxBNPzB5P37179/vvvz9Va9TSnvksmn9dSufOnVP5DzWL1hReETOpSBateMLHSSedlJUfffTRqbDiZrC6GlpuBTekcePG5aul91vWq7QsWlN7pW52c+8yyyxz2mmnZakveva//OUvCwbRmoafo5u/3LdN7cXJFU+lKrgKfve736VqvXv3rtKS2ZpFa2rfxnn44YenAJ9JW1T1LFrz/VAdazZWU/4a40btlOr15Zdf5vN/jx49GqqZj1IhPX+1UW1o1CbXqDEX3DEOGDAgrYt0L8AszKKnnnpqKqw4L5p/tM+hhx7ahAVSXZM7EjWN2bM14Zgli/IjJIvSyszwEBJ99PytR/nbn/J305155plVplIliy644ILpo/wL1lpCFm3ILIxANbXvX918882jP3HRRRddffXVt9xyy1NPPZU6W0nxpT3zWTT/DsPoE6fyH3AWrSm8IjJvvfVWZNfjjjuuehioUCSL5t/WECs9/cCfT0rzzjtv/vUPdVVZbgU3pG7duqVqFf3aCmVm0QkTJsQIo370X6+99tprrrnm3nvvbewZuYayaASt/BOb2tTeZplfzgVXQbQqP5L8k2wrzKYs+t577+Uvjo2tLv80rK233jorn2EWzT8Lp01993MW3yk1JB+f2uSe2Fxh1113TXXmnHPOprWhsZtc8TEX2TG+8MILKYjm31wyC7No/iFAET7z9dN1H+Hmm29u2gKpYmY6EsX3bE04Zsmi/AjJorQyMzyE5I95cXjL30OV79/06tUrPaA18/TTT/fr1y/7f0NZ9O23307liy22WP62tPwhJLqbWWE6KP4wsmj0fbOfhLfccssZTrT40p75LBrZI3108cUXp/LmzaLFN4PZuiJqap9Tmp7/vOCCC3766adFhqopkEWjHxZfhOzT6LnmX+0YASPdvxoiLecHjMx80kknpRfrVVluBTek/HNQoiV1n5GTQnK+07z66qtnhZEPs6/zLMyiEVSWXHLJKHzuuecKLe4GHHjggflJ5F+kEbMZO4H8p4ccckj6tOAqiHmfe+65U7WY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WNVsGnbkyJH1DjLDBwVHhXoHjBFWGeqll16q3tS6XnnlleotaUbTp0//97//fe6558YmccABB5xyyin/+Mc/YnWkCo8//vijjz5aU99ynh2vApp92ycAPwCyKEBrNW3atNVWWy29vK566GqsJ554Ytddd51nnnkqXrc7xxxzbLbZZgcddNBsGnbAgAE77LDD3HPPXTHsHXfcUb3Bd999d8Ug7du3j1Hdd999VYaqGKRr167dunXLl3Tv3n2hhRaqeE9g9ZY0i8mTJ1900UWLLbZYtDBm4cQTT7z22mvPPPPM7bffvm3bthtttNGVV145aNCgmJ0//vGPUT8Wy3LLLZefrwixs7ZJs3X7BOAHQBYFaK2GDh2azxI33njjLJ/E22+/HQGyUZlwVg0755xz5oeNNFV9kE033bQiWD755JPVB5k6dWpWc8EFFzz//PPHjRsXhX/961/zI/n73/9eU3t+LyJcBKooiYxdcC6aZv/993/qqacaNch77723wgorZA3ebbfdJk6cmP/02WefXX755dMcZVm0pvZ1yvmFPMuzaAnbJwCtmiwK0FqNHz8+f+7xueeemx1TqThP+M0335Q2bPfu3fODv/766w1Vfuuttzp37ty7d+9Ued55553hJCZNmhQ1O3bsGNE3FdabRTMvvPBC27Zt55577uJz0ViXXnppTLT6udwKQ4YMiSydtXbVVVeNmapbZ8KECWussUZFFg0/+clPZl8WLWf7BKD1kkUBWrF77rlnqaWWWmSRRc4555zZNIkYf4oTc845Z5nDnnnmme3atUtjqHJx72GHHXbMMcdstNFGqfLiiy8+w0l8/fXXUfPcc8/NF1bJoqFv377t27dv1IwU969//StG3qgs+uWXX+YXcmwPDdX85JNPevToUWYWrSll+wSg9ZJFAaimGbNo5MA99tgjjaFjx45fffVV3Zrjxo2bb7753n333cZm0bFjx0bNYcOG5QurZ9EXX3yxsTNS0JAhQ7p06ZJNtHgWPfzww1NTF1pooWnTplWp/NBDD5WcRQGgClkU4Mcigspnn31WPa7U1bxZ9JlnnsknwwsuuKBuzYsvvnjLLbeM/zQhi26++eYVhdWzaCy99dZbL/05ffr00aNHV9yf2QSDBw9O19kWz6IfffRRdh41s9tuu81wkJjfGWbRSZMm5R+9W8WYMWPq/XWgaYpsn19//XUs8PTn+PHjZ9XUASifLArQKl1zzTU//74333wzyh988MGK8ieeeCICw29/+9vs4bQdO3bcfffdP/3004ITat4sGv9ZffXV00h69epVkVUiDS677LJ33313TeOzaL2qZ9FkwoQJhx9+eOfOnbt06RL/rrjiimeddVZq28iRI9dff/2KFRElTz/99CuvvLLBBhukwiOPPPLVV1/NZ8IQY8s+/fzzz6s09fzzz88P9Yc//GGGcxcbyfPPP5/+rMii0ewItG3bto0/46Mjjjii7otepkyZctNNN6277roLLLDAkksuGZU7deoUf95www2TJ09O1Wbt9hkL9pJLLom1P8ccc8TSXmSRRfbaa6/9999/jz32mOEsA9BiyaIArVL0zvv165ePIum8Vvxnrrnmyqep5ZdfPjr6+cJVVlklQkWRCTV7Fr322mvzs1lxzjCyzRJLLJG9fbS0LPrGG29kT6bdYYcdIgxHBoucGX9uuumm6RzpSy+9NP/88+dn/+OPP84+GjduXMxdu3btLrroovHjx8f6OvbYYyNipcp9+vQ5ttbYsWOrNHXzzTfPNzUiYmNnNp9FIz127do1gmX+4brRknz92GZ23nnnKN9vv/2+/fbbKBk1alR6cctmm22W4uis3T733XffKNx4443ff//9+DPyfPYLhSwK0KrJogCtWMeOHev29cOqq66ayhdbbLELL7wwQsLo0aMjoaXyW265pcgkmj2LRubJX7+61VZb5attv/326aLTcrJoZKRll102+/TRRx/NCvv375+VnH322anmbbfdlh/VzTffnJV/8MEHkbtuvfXW/Gjzb/sseI1ufm2GAQMGNHZm81k0FvLtt98eGXLo0KH5WDh48OBUP/0uEIs9FcZ8pcoV52ZnyfY5aNCgrCTCbRrDF1980aNHD1kUoFWTRQFasYaePfOzn/0slf/5z39O5QcddFAqP+6444pMotmzaPj973+fD10RlrLy999/v0OHDul6znKyaPbalUz2StLw8ssvZyULLLBA/rrWnXbaKVVeaKGFoqkRrddaa63jjz++YrSNzaLTp0/PP2S4TS4YF5fffvK/TeRf1nrNNdek8l//+tep/NVXX80K8/f0brDBBg2Nv8nbZ/wnK9l3333zI48VIYsCtGqyKEArVqSvn79086STTkrl++yzT5FJtIQsOnz48PyFo0ceeWRWHikln0bKyaLZ1bkh/3KXSMVpkIcffjiVjxw5Mr+Otttuu9/85jdbbLFFdlFxXhOyaH6ZhIceeqixM9vQ9rP77run8j/96U+p/I9//GOa91gpWWEMmCr36NGjyPgbtX1mF+hmdttttzTdb775ZsiQIY2dZQBaDlkUoBVrbF//5JNPTuV77713kUm0hCwastsUM/PNN9/48eMnTpy4wAILPPnkk6lOCVl0ypQp2aN9wjzzzHPJ/5x11llpkBhDfpAYQ36E3bt3HzNmTN3pNuEa3UUWWSQ/5uwBTo3S0PaTf5VO/rm7kydPjrk79dRTUwj87rvvrrzyylR5JrNovdvnRRddlJ/Ndu3aHXDAAR988EFjZxaAlkYWBWjFfjxZ9NFHH80HkksvvTQ+XWmllfKDlJBFhw4dmv90u+2226mOG264oWKcm222WRokVtnIkSPrTrcJWXSDDTbIN+aKK65o7Mw2NosmU6dOfeCBB2ITmn/++Xv27Jkqz44s+u2336YbdJNIpOecc05j5xeAFkUWBWjFWlQWnTRp0pZbbpl/58pMDluRA1dcccU0thVWWOGnP/1pJNJ8hRKy6EsvvZT/9MMPPywyzmHDhuWf4rPjjjvWrdOELJo/GRuOPfbYIkPlNSGLTpky5ZJLLunevXub2gfnvv3220888USqPDuyaPjss8823HDDNnXkrx8GoNWRRQFasRaVRa+++uqVV155Fg5bkQMvu+yyfA6Zd955x48fn69QQhYdO3Zs/tOnn366yDgHDx48zzzz5AeseIhuTZOy6Lvvvpu/ZTTyecF5TBqbRSdOnJgeaxRBdPr06VFYQhatqb0/tn///rGR5Bdjhw4d0uOjAGh1ZFGAVqzlZNFIKUssscQvf/nLWThsRQ6cMGFCfn4POeSQivGU8+yirl27pk/PPPPMGY5wzJgxkdCuueaaLbbYIg3YpUuXL774Il+tCVm05vsPtg2vv/569fqffvppPj83Novm79pNj+2d3Vn08ssv/+STT7L/RyK94447unXrlqr95z//KbisAGhpZFGAVqzlZNE999wzKlTcwjeTw0YIqah51FFHpRG+9tprFZ/ms+iiiy5aZO7quuCCC/Lp7qqrrqqo8Jvf/CZ92qtXr0mTJuU/jaSXfw1mZKftt98+W9QjRozo1KlTQ8s/n0XvvfferPDdd9+t3trPPvssYnwaMD1huF6jRo1accUVt91221TSqCw6duzY/GnYV155JSuf3Vk0VmuslIq5Tm8iffPNN6svIgBaLFkUoBXLZ5v8+a7VV189lV933XWp/Pjjj0/lFechGxKhLp/NpkyZUlFh3Lhxhx56aPbpoEGDZtWwCy200IknnlhR/5133skq//znP6/b1HzC6dixY3YFaWOdcsop+TbXfUDORx99NPfcc6cKETWzF4rG3N1+++2RDKORqfIZZ5wRqSldS3zJJZfkR37//fenmmuttVYqz165GVF8v/32m2GDX3755c6dO6dhow31Vnvssce6desWuS7/+tOGtp8+ffqk8piFrDDCZ77x2TnhmLX8k5m6d++en+gs2T6jzUsuuWTFtbjZi17mnXfeum/HAaC1kEUBWqs333yzbjaoqb0odP7550/lv/71r7Py7777bu21107la6655gzTWv/+/dt831VXXZU9YWj06NH/+c9/Lrroovw1q6NGjZolw954441REp9G0Kpo0tZbbx0f3XLLLRXlzzzzTPv27fOT+9vf/tbYODp8+PBlllkmP5LVVlvts88+q6h22WWX5c8QtmvXbo011ojcFQE4/5LP7HLfww8/PJV8++23+UZGcP3yyy+zj44++uj8dCN9LbLIIp9++mmRZr/33nurrrpqGvaAAw5IF+tOnjz54Ycf3nbbbaP8wAMPjD/TUG+//XZ+iuk5QN98803+R4Qdd9wxy3uTJk1aaKGFUvkcc8yx3nrrxZYWoTE/npjKP//5z5pZt31mp7tjFmKzyWrGQsvOBl988cVFlg8ALZMsCtAqXX755RXRK5xwwgkPPPDAfPPNV1Hep0+fmu8/hzaz9NJLp/59hVtvvbVLly5t6tO2bduKJ/Fkov7MD3vuuecuuOCC+Y+6det21113pYYNHDgwMmo+U8Wn+etU8yLz1L3Qt16PPPJIr1698gkziai57LLLPvHEE/n68We6TDTz05/+9MUXX8w+HTduXMq0Mcu9e/eOwiFDhuRff5JZaqmlskG++uqrddddN5Uvt9xyb7zxRpGWZyIuXnfddSussEIaQwTjxRZbLHsb6k477VRxX+WVV17ZoUOHfEsiWx5//PFff/31AgssUNHImJdsqEGDBuVjZATmbNVsvvnmqXDPPfecOHHiLNw+I4tuXCs2km222WavvfaKDSAaf9ZZZ+UfvAxAqyOLAkBTTJky5amnnrr++uv79ev30ksvzfwIp0+fPnjw4DvvvPO5555rcsp6//33b7zxxrPPPjuC30UXXTRgwIAPPvhg5tuWRDiM/Blz/eyzz6ZGTp48+e67747lEFOfhdPKDBw4MLuueOzYsY888khE7oceeqih31AAaEVkUQAAAMomiwIAAFA2WRQAAICyyaIAAACUTRYFAACgbLIoAAAAZZNFAQAAKJssCgAAQNlkUQAAAMomiwIAAFA2WRQAAICyyaIAAACUTRYFAACgbLIoAAAAZZNFAQAAKJssCgAAQNlkUQAAAMomiwIAAFA2WRQAAICyyaIAAACUTRYFAACgbLIoAAAAZZNFAQAAKJssCgAAQNlkUQAAAMomiwIAAFA2WRQAAICyyaIAAACUTRYFAACgbLIoAAAAZZNFAQAAKJssCgAAQNlkUQAAAMomiwIAAFA2WRQAAICyyaIAAACUTRYFAACgbLIoAAAAZZNFAQAAKJssCgAAQNlkUQAAAMomiwIAAFA2WRQAAICyyaIAAACUTRYFAACgbLIoAAAAZZNFAQAAKJssCgAAQNlkUQAAAMomiwIAAFA2WRQAAICyyaIAAACUTRYFAACgbLIoAAAAZZNFAQAAKJssCgAAQNlkUQAAAMomiwIAAFA2WRQAAICyyaIAAACUTRYFAACgbLIoAAAAZZNFAQAAKJssCgAAQNlkUQAAAMomiwIAAFA2WRQAAICyyaIAAACUTRYFAACgbLIoAAAAZZNFAQAAKJssCgAAQNlkUQAAAMomiwIAAFA2WRQAAICyyaIAAACUTRYFAACgbLIoAAAAZZNFAQAAKJssCgAAQNlkUQAAAMomiwK0CO+8805zN4H/56uvvho9enSjBhkzZsybb745bNiwyZMnp8Lp06d/+umns7p1rcmkSZPefvvtKVOmtMCxAdC8ZFGA5vfxxx+3bdv2tddea+6G8P875JBD+vTpU6TmF198cdJJJy277LLzzjvvDjvssOuuuy699NIbb7zxJZdc8tFHH1122WV77LFHVOvXr98666yz3PetvPLKMUis/dk8N98zYcKEDTfcMLVh3333nX3TGjlyZPfu3du0abPGGmtMnDixRY0NgGYniwI0vzPOOCN62AceeGBzN4T/K9Jap06d5pxzzhEjRlSvefvtt//kJz/J0tGYMWPy5QsvvHCbWlkWDd99913k2zb/s9BCC0VYnY2z0bDJkyd369Yta8ZGG200+yZ04YUXpvm97777WtTYAGh2sihAM5s6dWoWDDp27Pjll182d3Ooueqqq7LA07dv3yrVLr/88qxajx496l7QO3z48EUXXTSfRcMVV1yR0tQOO+wwW1pfzLbbbltCFh04cGA2lQj2//3vf1vU2ABodrIoQDMbMGBAyifnnXdeczeHmjXWWCNbHQsuuOC3335bb51nnnmmbdu2WbU//elP9dZ56aWX2rVrl8+if//739O6zpeXb7vttishi4brr7/+wAMPfOCBB1rg2ABoXrIoQDNLZ6hCz549p02b1twt+lF74YUX2uRE+Km32tprr53qvP/++w2N7ZhjjvmRZ1EAaIgsCtCcRowYsdRSS62zzjopogwYMKButbPOOuuP/5Olo/vvv3+33XbbbLPNjj766E8++aTuIE899dSJJ5649dZb77fffpdcckn+6t9//etff8wZNmzY6NGjTzrppBhbjPO2225LNR944IE/fl/WvMhU2Z/nnHPO119/na9w11131dQ+qqdPnz6Rcw477LAPP/wwG9sNN9yw/fbbb7XVVmecccY333xT0eCxY8deeumlv/rVr6LNffv2ffzxx9NHFZN48MEHozAq5AtjplL9SZMmXXDBBdGATTfdNNLg3XfffcghhxRcIwcccMBee+2VVscaa6xRt86///3vVKF79+5VxvbZZ59FS9KfM59FG5q1xi6ifBYdM2bMqaeeus0228TCj3U0ffr0rE7F2v/iiy9ic/3d7363ySabxHq86aabsmoffPDBEUccsfHGG++zzz5PP/10mkTF4PnnCb/44osHH3xwjOcXv/hFrPTrrrvu1ltvrT6DVcZWU3XjqWnS1weAEsiiAM3p5JNPPvPMM6NbnyLKFltsUbdadPE7d+6cVVh77bUjy80111zt2rXLShZZZJH8g3MmTpx46KGHRnl09CM/PPLII23btl1iiSWefPLJrEIkz6xC5uqrr45ANe+886aSP//5z1nNkSNHbrjhhqn8yCOPjHBVUxs/dtxxx/nnn3/QoEHTpk2L5BPtSRFr//33n2eeedIlrDHyaMaee+4Zk5hjjjmywt69e+fPAMcMRrX27ds/9thjUXnnnXeOOgcddFD2uNSoefvtt6dmHH744dlcRDtTYcSMbFSRylZeeeWYeoTqjz766PLLL4/GRPOKrI5x48bFwpwwYcIyyyyTxvzss89WVIvklj5dc801i63q/2sms2iVWWvUIqrJZdEll1xynXXW2XvvvdPTjGLNxoRqatd+NDINHnFxwQUXnG+++VLJhRdeGAsntsxOnTqlwnvvvTebxIcffhijSuWvvPJKVh7JMzaDaMCbb745ePDgzTffPD79y1/+Un0GGxpbzYw2nppGfn0AKI0sCtBspkyZsvjii0cne9KkSV26dEn97Hqfy7LDDjtkn0a/PzJh9LMjEEb/OyvM37J48MEHZ4XpnaW77rpr/Dn33HOnq0kjA6TJrbTSSv/5z3+i8MADD8xKouZ3332X1Xz++edTzZNOOilN5fjjj48gnf5cd911szoRUCP/xKwNHTp0zjnnzAp79ux56aWXTp8+PfJw3dAybNiwmGKU/PKXv8xKhgwZktWJeUmT6Nq1az5o1dSm7rpBK1oVf2666aZpwDvvvLNgFo1GZk8zzj+yda+99qqoli3PzLbbbltkzJmZzKIznLWCi6gml0U7duyYbRWjRo1Kg5922mlZtYceeigN/vOf/zzbMvfZZ5+sJILiNttsE9thJOHNNtssK1x99dXzzUuDZ+lx7NixMcX4M51BnTx5cuT5LItWn8G6Y6spvPEU//oAUBpZFKDZRN966623zv7ft2/f1M8+4ogj6lZOZ6iWXXbZVBj9/opg89xzz6U+d7rYMrraWeH222+flUSoSJO75ZZbssIIh6kwn4c32mijrLBbt27pZOYyyyzz3nvvpTopikRiSYW9evWqm7vSGdQUjWIhZCXp0U1Tp07t0KFDlMwxxxwvvPBCVtijR4+KoBVS3E1jy07kRkyKFJ2qFUyMq6yyShbLv/rqqywyhXbt2lVcxpk/V5wiUBEzmUVnOGsFF1FNA/eL/p//83/SxhOhsab2cu7U4EceeSSrduONN9bdTtIJ2Ah4aSMZNGhQqpmlx8cffzwtt/R7x4ABAy6//PIZzmDdsdUU3ngKfn0AKJMsCtBstthiizvuuCP7//Dhw9P1q5EExo8fX1E5daZ/+tOfpsIIfllhRIus5KijjspKVlhhhVTtmmuuSZ34CRMm1Hw/i959991ZtQgbqfDFF19Mg99zzz2p/P7774+SCGwRG/LNS1k0/pMKV1pppazwV7/6VSrMXsgZTjjhhJra1JdGfvvtt6dq6ZLR448/PispGLS22mqrrCQy5MEHHxwLtsCq+L+effbZaHD6c//9908NO+OMM/I1t9lmm/RRWvJFzGQWneGszWQW/ec//5ma99RTT9V8P4um201jo02FH3zwQVb417/+NRWmhw/XTY/5W21jE+3Xr1/+Uu3qM1h3bMU3noJfHwDKJIsCNI9hw4Z17dp18uTJqWT77bdPHetLLrmkon7BzvQmm2ySleTvY7zlllvSmLPzfo3KopEWunfvnpXvsssuNbUn0K677rp885qcRSPzpIkOHDgwVUt3bKZTxwWDVv5Kzja1p+mitZMmTZrRCqnZb7/9LrzwwvRn/jLmRRZZJJ3Eq8ldzBzWWmutGY45mcksOsNZm8ksmk5ahmuuuaZmNmTRqVOnprORmRVXXDFdr1t9BuuOrfjGI4sCtECyKEDz+P3vf9+hQ4ceOQsssEDqWC+33HLpCttMwc70qquumpX07t07Vct38bO7NBuVRcOZZ56Zlbdr127kyJE9e/bMzq8mTc6id911V5po/r2Rq6yySlaY7j8sHrQuv/zydCtgZtNNN61YnhW+/PLLWB2ROfNrJD+Gfv36pcq33nprKq/+HN0KRbLolClTTjnllIbGUH3WZjKLxkpPo42m1syGLFpT+0ik/Btx2tRuVOkC4CozWHdsxTceWRSgBZJFAZrB5MmTu3bt+swzz3ySM2rUqHT6MTz88MP5QQp2puutdvPNN6fRZg80amwWjfyQnosbaXO//farmKMmZ9F6WxKWXnrprDDdkFk8aNXUXvN8wAEHpDZXZJW6IkrtvPPOn3zfxRdfnAZfb731UuVx48blfzgYOnRolTHnFcmiN954Y58+faqMpMqszcLzorFx1syeLFpTe6Y9tsn8w4rzP500NIN1x1Z845FFAVogWRSgGdx66631XtuZHjLUps4DWgt2ps8+++ysJLrjqdpVV12VFUYOzG7Pa2wWDRGQ0qdPPPFExadNzqJTpkxJr5OJfJKqLbroollhej/nkksumZVUD1r77rvv1KlTs/8PGzZsgw02yCpEWKq7wDPTp09ffvnls1th87755pv8K0zSg3Dyyzn84Q9/aGjMn3766XHHHZduiZxhFo2UG7N5+umn1zu2Gc5awUVU00AW7d+/f1Y411xzffXVVzWzIYsOHDgwPSsr5uWKK67InmUVW8UMZ7Du2IpvPLIoQAskiwI0g969e+dvTUzefffdNjlvvvlm+qhgZzp7Q2YWJ9LNqBGHKrrmTcii6fUePXv2rHu9a5OzaE0u16VQN378+OxJTosvvnh6jNM666yTVYvEkpV88cUX6YFP6fFCPXr0yN86GINnaeeee+6pu8AzDzzwwIILLhjBpu5He++9d1om+fQY8TI9wXXhhRceNWpU3WHfe++95ZZbLntbSSb9KNCmviz63XffZeO88847623nDGet4CKqyWXRGCQVpu2kb9++Wcksz6LXX3/9Wmutld9+TjzxxPh0tdVWm+EM1nuWteDGI4sCtECyKEDZbrrppuj+9u/fv+5HkyZNateuXepwRzJJp9TSQ4nmn3/+VJjO/6y66qppJJFkspFE372mNjVF/zv+XH/99VPcyj/0JQXUK6+8MhXeddddFW2L/LDUUkvFR/WetUtPLl1mmWWykqlTp6aTiumhu19++WWaRHr9Y2SwLETFv1lKyW5wbd++/YABA9IkstDSpvYcWrT56quvjqybTvrF3GXvyYw80717948++igbKlJiJJMoqfto4szXX38dS2+VVVap94bSU089tU1OduVq5ptvvtl9992z8l69eqU7HrOJnnzyyTH7F198cX5shx56aBpVTDSdA4z1fvfdd6drVt999916mzrDWSu4iGr+l0Vj8NhUYqXU1L75M7vEd8UVV0w3A+efwJzOZ5533nmp8PHHH88Kjz766FSYXoFz6aWXpsLsJ4/IovH/M888s2KZZAuq+gzWHVtN4Y2n+NcHgNLIogClOvzww7OTNnPPPfcWW2zx2muvpY9++9vfphdyJmuttVb0yNNZx0wEp0iVm266ab4wvTs0vPTSSyuvvHJ0tSNK7bDDDh06dIholIJodNa7dOmSBoyWREK4//770+WOoWvXrlmUzTvnnHPio5RnMuPGjat4FM2OO+4Y0/rZz36WLzzggAMiokTOSSWRFo466qhsJJEoTjjhhLnmmqtPnz6nnHJKTD3yc/4Ow5ra810pUYQY/5AhQ+aZZ57OnTv//Oc/32uvvc4666ya2utUI8P37Nlzv/32O/DAA2NUyy23XN3TvJmYRLpHN6pFlksfPfroozG57E2VScTLihPaEdrTnC6++OIbbLDBYostFqs4Yuqrr76aqt18883pLHGy8MILx/pdYokl0qnLNrVv12zoMUsznLWCi6imNovusssuH3/8cWTIddddNzaPyGORSw866KDI2Fmdq666Kp3EblObbyN53nDDDZ06dUqFsSENHjz47LPPjq0oFS611FKxYV9xxRX5LWqBBRaIJB9bWkTumOuYaEx6ww03bNu27THHHJPlwyozWO/YCm48jf36AFAOWRTgB+vTTz998MEHo1Ne79WnTfDcc89tvPHGs2RU9YpQ8fLLL0ebP/vss3orREiLkDNw4MCUh+PPiuSWXUo6derUmPF77703Rph/Hcts8tFHH/Xv3//SSy+98sorH3744ch4s2MqRWatyCIKb7zxRvr/559/Hm1+4YUXirz5ZiYNHz78ww8/jP/EKn7sscdiXaeTqDUzt+5muPEA0NLIogA0KDLMI488cv/992dh5vjjj88/IQYAoMlkUQAa1K9fv+wKxvvuu2/MmDHLLLNMCafOAIAfA1kUgAaddtppWRbdfffdt9pqq4on8QAANJksCkCDPv/88/XWWy+yaIcOHfLvyQQAmEmyKAAzMG7cuPT2EQCAWUIWBQAAoGyyKAAAAGWTRQEAACibLAoAAEDZZFEAAADKJosCAABQNlkUAACAssmiAAAAlE0WBQAAoGyyKAAAAGWTRQEAACibLAoAAEDZZFEAAADKJosCAABQNlkUAACAssmiAAAAlE0WBQAAoGyyKAAAAGWTRQEAACibLAoAAEDZZFEAAADKJosCAABQNlkUAACAssmiAAAAlE0WBQAAoGyyKAAAAGWTRQEAACibLAoAAEDZZFEAAADKJosCAABQNlkUAACAssmiAAAAlE0WBQAAoGyyKAAAAGWTRQEAACibLAoAAEDZZFEAAADKJosCAABQNlkUAACAssmiAAAAlE0WBQAAoGyyKAAAAGWTRQEAACibLAoAAEDZZFEAAADKJosCAABQNlkUAACAssmiAAAAlE0WBQAAoGyyKAAAAGWTRQEAACibLAoAAEDZZFEAAADKJosCAABQNlkUAACAssmiAAAAlE0WBQAAoGyyKAAAAGWTRQEAACibLAoAAEDZZFEAAADKJosCAABQNlkUAACAssmiAAAAlE0WBQAAoGyyKAAAAGWTRQEAACibLAoAAEDZZFEAAADKJosCAABQNlkUAACAssmiAAAAlE0WBQAAoGyyKAAAAGWTRQEAACibLAoAAEDZZFEAAADKJosCAABQNlkUAACAssmiAAAAlE0WBQAAoGyyKAAAAGWTRQEAACibLAoAAEDZZFEAAADKJosCAABQNlkUAACAssmiAAAAlE0WBQAAoGyyKAAAAGWTRQEAACibLAoAAEDZZFEAAADKJosCAABQNlkUAACAssmiAAAAlE0WBQAAoGyyKAAAAGWTRQEAACibLAoAAEDZZFEAAADKJosCAABQNlkUAACAssmiAAAAlE0WBQAAoGyyKAAAAGWTRQEAACibLAoAAEDZZFEAAADKJosCAABQNlkUAACAssmiAAAAlE0WBQAAoGyyKAAAAGWTRQEAACibLAoAAEDZZFEAAADKJosCAABQNlkUAACAssmiAAAAlE0WBQAAoGyyKAAAAGWTRQEAACibLAoAAEDZZFEAAADKJosCAABQNlkUAACAssmiAAAAlE0WBQAAoGyyKAAAAGWTRQEAACibLAoAAEDZZFEAAADKJosCAABQNlkUAACAssmiAAAAlE0WBQAAoGyyKPyIfPXVV6NHj27uVgAAgCwKPyaHHHJInz59Gvp0woQJG2644XL/s++++5bZNgAAflRkUfixiKjZqVOnOeecc8SIEQ3VmTx5crdu3drU2mijjWZ+ohdffPGQIUNmfjyttwFAC/T888/fcMMN06dPn1UjjJ3ngw8++Oqrr86qEVYxfvz4fv36jR07Nvtz4sSJV1555TvvvFPCpEvz2Wef3XHHHeeff/5TTz01bdq05m5OPWKNDxo0aOjQoc3dkBbnn//85xNPPNHcraDVkEXhx+Kqq67KQmbfvn2rVNt2221nVRZ99NFH55hjjmY8JjV7A4CWqUePHrGXe/bZZ2d+VMOHD///2Dvv8Bqy/49fUcJGRG9B9N5Z3WK1KFEWIdrqLXq3dvPondWXiN5CsHpYNWpitRA9sYgu8RUiG7HM7/2bz5PzHDP3zp17cyXBef9xnztnzpw5debzmtM8PT3TpUuHAFesWJHwADV09+7ddu3apU6dGvf6559/yHH16tU4bNCgwWe9dWLqxIkTbdq0uXTpUrNmzZC00aNHJ3WMPtHHjx/xGnV0dETc/vzzz6SOTvISqiWyBc0hLi4uqeMi9GVIsKiQ0LeiChUqEGRmzpz533//NeWtadOmNmFR2Ey4EcJJKhRM8ggICSWC/vvvv6SOwhepBQsWdOjQITo62lYBuru7JwKLSjII0egVxqL3799v1arVtm3bPvetE0dRUVHp06ffsGGDJA/nadGihZ+fX1JHyoioxAWLKvThw4fu3bt7eXkp3I0+qcTjS0gSLCok9I3o3LlzBk6rV6825dMmLBoWFubi4kLhJAkKJnkEhIQSR127dk3qKAj9v3755ZfEYVGoSpUqPIt+ZaIhPGfPnk3qiJhRnz59BIvql/pJtWrVqoCAgCSJjFCyku1Z9N27d9euXTstKyQkhO9++fjxIwzEoKCgEydOXL58+X//+5/68mfPnl24cOH169c2j5iQ0LesHj16dOjQgbFohQoVTPnkWTQyMvLXX391dXXFW0Q9tyo2Nnbu3LmtWrWqV6/esGHD8Eru27cv3G/evJk7d252r+7du0+ePHn//v2SPJZscrxwLVyuXLnSqVOn+vXrr1+/noUcHBw8fPjwFi1a1KlTx8PDY9asWREREeqo4vGCAPv3748IwNvmzZvpI6tGBISEviYtXboUNTypYyH0/xIsaiv169dPsOhXJvWT6uLFi/b29uJL8efQkydPzp8/D87H78OHD9UeoqKiLsgClClOvX//HoCGUzDDEiWy/y8bv8OQBjw+ULeOHz+OXMAfHMJgpbNXr149Jgssil94ePnyJX/5q1evTp06hVMKdyEhoYQIz50cOXK8efOmcOHCjNBMTZRiLOri4lK1atWOHTuy1Yzc3NzYkDb8KVWqVMqUKX19fcPDw/Gm+e6779KkSYNTu3btAkayGzVp0gQkTKh548aN8uXLs6HCeFDQJCsSGBJ+QL80qfX58+d37typVasWTT45fPgwH088LkuWLImXGa0eQbO/EMMPHz5oREBIKPkIhgItfHLt2jUfHx+8+9gMq/v375+VhVPkcunSJXJBIyKXbdu2pUqViqx2iH3effz48ebNm9EwcS2MEktjhcfF3r17JXmBHPxZt26derUzNNXr16+jre3YsQO2OPtKBRdYMGvXrt20aRM1Z7UQq1WrVm3duvXu3bvqsy9evDh58iT+IEVr1qzhP0z//fffyKWdO3eqN6YKCQmB5z179uBZ9PTpU52nkP8Uh3v37p2NF0xkOhsZGUku/HJEEREReLx4e3sjMopvczyLvn379iwn3JpFRlFY+oWooiy2bNmCPFGzKErtr7/+kuRBj/yt8RQlDygXcuG/62lkqakiRu1CHFavXo0KaXRJIZh8R44cWbZsGX5jYmIsSiMyCjFs1KgRUoeIUYTZWTQQWIlI/sqVK4OCgpg77oLX2fLly1HKiJ4iTMQcNueDBw8oD1EZcMhijjtu3LgRTUlj3oop8SyKkkWE9+3bx0KGxcuX/rt371ihPHr0KOHRQ0VdLevKlSuKU8gilKkkf649ePAgsovC1xDqD4seBcjiz1wkrgKzC40WClhg//79SDIdqp9UeAiQXbFkyRK48E8YjSZmRbq+QQE+edSC8HzjPSBXkbd0Sl15YHSxyxMtzjZmUTQbJODMmTN4oaIunjt3DoeE3bCDiVFRa5EReJviEORNF+IQlfhYvASLCgnZUIsXL+7Vqxf+zJs3jxFahw4djHpmLAr8I0MNb/ds2bKR42+//UbeyPCqV68eu3D79u3EopJs4rAbKT58TpkyhYVfoUKFWbNmpU+fnlzwWITBRP8RVfIPA4tcMmbMyOaWwMJ2cnKC48CBA8mlQYMG5O3UqVPaERASSlqhGk+cOLFo0aJkcLu7u6PhUF2tVq0awQNAaMiQIXCpUaMGXQXTEK0YLrDUJfmVikC+++47uHjJIqyFGVe5cuVDhw6BJdq0aVOiRAn9EQsMDMQl9vb2BQsWRKtBE6OIwY6E2QcPeLMvXLiwevXqcISxSPPlIBpoByMGp0aPHo1r0X5xuZubG49/ePX379+/efPmsATwJMGF+fPnR3LwzIExipi3atUqderUHTt2xCOLQkYaJdm0wL0mTJiAu1eqVClDhgx8ZxSeRa1btwYawfYoVaoUbqF9CsbupEmTihUrxkACzxN67jk6OuLRQdfCOh8xYoSDgwP7Cgba8fDwQNyGDx+OeCIhbCVb6VMWhRX+xx9/UBKmT5/OgBBlhPsiEIsGfyHbe/fu3bhxY6AOzHrkWM6cORmLwihv27YtSq1s2bKS/DkAiSLTf8CAAQx6YW7lyJEDeUv2laks1S5ikA/ucuDAAfxBXmXJkqVu3brIOvp4AZ08ebJly5YofaQat0NiAbT6Uwp8RU0uWbIk7ti1a1eq2CC38ePHFypUiGCmePHi9PogPEPyUcmXLl2Ka1EuSPjYsWOJgvCLQsmTJw/8o3Z5enrCJ32QRdmhBaEg4EIBIiH640kiFl2/fn3Dhg1dXFxoeQLUNzqL0qlduzZcEAdJxjO8m9DAqUokJHqodT/++CMKHRV7w4YNKLuRI0fSKeQ2igyVIXv27DjLAoQfNXXwwu0QIHziQvocg6cBLodLrVq12Bcx1KKsWbMiqmgyRgsF1+Is/OCQ6p7RJxUQlC9lFCKFb6qJWZ2ub01o/tSlR5SOYqKeP1Q/5gcNCo6nT59Ws2h0dDQeznTqC2bR8+fPIwHsWx2hKX0pCQ0NxX/UITpFaArRIwP1m4b1ChYVErK5SpcujfcK/uDdwPoh8c422mdidL4okI8cwY30bqC3LF4w/PfpJk2a0B8NFPz999/ZqXXr1sEFD8o6derAOsT/HTt20CmYR+QfJjjzzzoo2rdvTy7MBhozZgy50MYGgkWFkrNAaNT5U6FChf379wMAAHJlypSBC+o2+aHvMoxFpfhaTSxKgmVm+HTkGygFdjn9j4mJgR2pP1Yw7v39/cmmRIO6d+9ebGzsggUL4JIiRQrYo6Dox48fwywmCxVPFfiHCQvjBm/tbNmy8Wt0w0JNmTIlEsXMIEAOLmRmQJcuXXA4atQouODWQERQBFxg165atSokJKRz585Hjx4FweJpQ52lkkyS4ENYpWRsAblxCQMePCJ69OhB/02dwr3w6KtYsaKBG2D58OFDgDciDARlSVi2bBlbwRV4zy9USw8cwB5zUY/RpTXJQXTMBVmRO3fuZ8+e6S8UqFOnTt9//z3LRlhW9I2AbC1kyMaNG3FILEpCxChvmQuyEeQQGRlJ/01lqUYRw05D/uABTlehjAzy50gUH3WrolYDPhn9AlnhAW8fS3dkIQBmz+23b9+GhYVlypQJjqgziCRIpnv37pKMvnDEjdi1s2fPhku/fv2Yy08//QQXpJfMbiSQepXhwkYh0jgaWOEWxZNYFAmkD6Awa+kDByxh8kBth1iUjx6xqNXRGzp0KA7ZRxNUDxyy4RIoTbRWlCayiD550JcdeNNODpoAyjdHjhysN5Jex5TVJJwqUKAAbABThYLmg1cwrfPMd/6rn1SKUpbMNTGr0/VNCQ2cuv2o0aG80Ebgwp45eNfABVULz3M1i168eBEghtL8slmU0swM3OfPn1OmIDtogC5rLcgOwk6+sqIRChYVErKt8GQpWbIkO8RznEHahAkT1P6NsujWrVvZVfSBnCxpYlq8khWDQHSyKD9UiRQdHV2/fn1nZ+c1a9aQC8+iZDzhLYh3ErmwAXV4O+JdyJ6egkWFkrmGDRumQBfgKNVYGrFGhzyLwujXZlFYwzhs06YNsyZBUxbFCkYeQgAv8Y5k7DLGIxtR8fQg+FEMuyUbmtFL5cqVYeyyuMH05NlbiqeXOnXq8IEgi1xcXN5zatiwIbzNmjULZ/fs2YP/ixYtYv5ZkjVOQT179jR8OtkPCYTLH3/8wVzAA/Rkg3GSN29e0BeLA/DDIH+bY6ClZlEYPwpEBNchTyRLFBQUhEBoUVkmmunAvvuDIhQ3QrTt7OxQjmwsyeHDhxlUaGepZKKIR44cyR7CkvysBhIDXZiHjh07du3alYUZGxtLvWHnzp2zKMlqSoGqVq2qxsVSpUqhXHgX2JY0iocNuxs+fLhB7r1kfmgaCEusFP+VhA3G0Sli0S1btjAXyje2NCDyWcGi9PrjWdSK6MFDxowZ2TzAyZMn4ywNXiVlyJCBjVGS5HVYFNXDlKjBsoEAyMzMmTPjXmyqHap9t27dmH+jhQJRf6lFLKqniVmdrm9H1AXID6KmAarsWXHz5k2YcDExMWoWffr0KVzw+/jx4y+bRYkk2XAUAnQItQovUfxhezGjbtEpfpaCYFEhIZurS5cu/CsWb2gGaTAj1DuAGWXRo0ePsqt8fHwkeUSugVPq1KkHDhzI3lg6WVR7ig6ep0OHDi1SpIiCRfk1gU1NrxcsKpTMpbZBIZAnHPft2ydZxaIQdffVr1/f1HRNbRHNFixYkHckaARJ0qHRRXoKFCgAzlT0gG3atMkgT9imw1y5cuGQvfSfPHmCQw8PD8WNgDR8IIDVrFmzNlWJHmuwnAh4PD09FZMwNU5JxhaeoY5oYB4d3rp1y9XVlf5TFyvKQh0NNgjZaLaQsU4zOaHOnTvzzKBHffv2RQhskCRJMV+UclJhlLdq1cogD/6kww4dOtDoGMlclppKC0oKjvz2KkWLFkWZskMalKsOFsVqUZKNsig1DTQK5vLgwQODsbG1vXv35llO3dCocxK/zIU2aNXeeVstdRWikOfMmUOH1rGonuixTwynT5/Gm9rw6dcKBbPhPQsP+fLlM5uivXv38g0QNjwNpNq6dSu5oALznKMuFBJNQLCIRfU0MavT9e0IzwRkKf/1h8arUhlFRUUxLlWwKDANdYkGrXzZLPrx40cFXgIpTbGo2rMkWFRIyNZCU7K3t4eJkI8Tz5AwFhWXGGVRHu2YgbJ06VIaisNUr1496vRICIviObB8+XIgaPr06ZcsWYLLFSzKd9KaWh1XsKhQMpdRFv3555/huGrVKslaFsVLltp4qlSpRo0aZemKLEZZ9N69e3BkHVBqUImJiaGhCoq1amC2GuRJoXTYunVrA9drdPHiRYO8eAnzb5RFS5YsCaLTiDPoLm3atLgQfKXYrUrjlNFFUGvWrGmIH2M5evToHTt2kDsAzPDpWFC1jPIbfbNr2LChJOcSMlb9+U9bNBtCseqSHhY9fPgwHJs1aybJszNwCTtlNkuNpoV659jOHHhQZ8qUqW3btnQYERFhBc4ZlU4WpV7077//XnE5SA/urPtOP+zBp0XxNMWiLGTbsigfvQ8fPqxbt6579+6omV5eXooQtJlt/PjxRTmVKVOGD9bZ2RlNhmbiTJ48eeDAgWja9FEGaKrIbRuyqJ4mJljUrNQseuHCBWJR2GZ4sgUGBtIXQwWLwsPx48ffvn0rfeksKsnd99TDS4fgTJo1K8mrb/FjdEGnhJ383AzBokJCthXefC1btnzyqWgSC6l69eqKS8z2i9LcGBKM1B49eqRMmVIBh1az6Lt371gE6FHIB0UsiucpczE1qkqwqFAyl1EWHTRokIFbCsgKFpXkj999+/YlOCxfvjy/vo5ZGWVRvJENXAeUGlTw7qYZjOxzMyk0NNQgL8hEh+Hh4cWLF8+RI0dQUFBsbCwsaVr4mvk3yqJ58uQBSSpW1FQI96UpjoZPp7dpnDLKotSR27t3b6SoQoUKbIrmypUrDZ8O91XLKL8hdTSyIzg42NfXd+jQoRohGBVdzq/lK+ljUahYsWJ2dnbIdgD/4sWLmbvZLDWaFjycf/rpJzzt165di//Ik0KFCrE5WWFhYbgEHixNoFo6WZQmi/IdsyQfHx+4jx07lg6/Pha9f/9+rVq1QInUO0pjdPWzKHz24eTp6cknihYVW758Oa5C3cPDpHHjxqhFDx8+nDNnjqIJ2JBF9TQxwaJmRYvoqsfoos4QkeElEiqL1osFmsKKi4uLA4jiP53Cw4rmV+I/Wwz5s8rGLEppY8uXE1ufOXNGkoe78AgeExND2Mkbo4JFhYRsKJgasEVovB+vt2/fOjo6MlRTTOYxyqLbtm0jR7wJ6AXTuXNnNkwIVgjtvGKInxtmNYvS4iUQXmbkomZRxB+vRnLhv+nyEiwqlMxllEVbt26Nuk3DhaxgUQAev1QPWYT8BEizMsqieHHDEZxMh0ZBpVy5cgbVtEa8/eEIe5cPqn79+kCyUaNG7dmzR3F3oyxKQxAVWzpJcpcjWBG5hDiTi5+fHy3KTV+9NU5JJlgUNhmy1MHBYfPmzQxmJHn+ETzXrFlTnV3sAWtqf1GY9QZ5fZcWLVpYseYnSACXs/nzJJ0sSp8dJ0yYgOcz/0lCO0s10oL0NmjQYMSIEUOGDAHysUkZktzBAEz97rvv1N8++BmVeqSTRXEjesIzm5M0bdo0OKIE6fDrY1GUPioze/9ayqLaArSkSJECt0C9pV5u6rFErqKCKca625BF9TQxwaJm9ezZM0WXJi0Ki0cETQdV69SpU2jIRk9B1FP6uWVjFiXgxPuSvrcRW9M8B8ogpJkGqNAyTXhR8V/mBIsKCdlQ+/fvz5w5M7+WNxOsPYZqeCXwpxiL8oO4YHyQIxuChRcAW8NWkpc8oY4Rmg1Fo+9INL9ozpw5tK8dz6Lqx1yFChXoFGJO71p+RC5bNsPT05M58t/7Q0NDfX19tSMgJJQcpLZBYRBkzZqV9d09fvwYHvLkycN6DmGTGeIHfJJoQwg2MhbGHyNGSd6u0PDpmqJmZZRF582blypVKjQuOjQKKkuWLIEjwIl3BAuBT65evUqH4MCffvpJozvOKIsCpSgf+HW/AwIC6FkEEmAjaaX4xV0JfjROSSZYVJJHMMI9U6ZM/DpMwB7YwXCfOnUqc3z37p2HhwdbgM0Uv6FYnZ2dkYGsf9gi0YjTihUr8h3IRP5sn3pTLIpoAw6dnJx+/vln3l07S02lBXXD1dVVvRMpU506dagOMEyCZs2axZeCHrVr104Pi0K0DcmMGTN4x1atWuXPn581iiRkUepm5+szrf8ErmMulkaPFuxBbWSDvUePHg2XtWvXMv8JZDb6/IE8pEGOqOdZsmRxcHDo0qWLwqd+FlU8qST5c7aBm2Wjp4kJFjUr5BhhFGU+DDOGlMj8x5xo7O7ff/+NUqbVs5muX79OY1rx36gBaXPZmEWjoqKOHz9+TN44lNJ5TN4GV5I5k+j87NmzYFTyplh7U7CokJCtFB0dXaZMmdKlSxu1/GilPiZ+2C2xaIoUKWA8UUtEE6YZaCVKlGD9DHDJmzcvPwgCl8CFFlvHJazrElf16tUL5gX5hGXM7qteeYiRsEGe6TRkyBB+7SJYSLRkH56zLi4uzB0vex8fHyQKKEs7PWhEQEgoOYhsUFharIVOnDgxd+7cbHlMKd6Ag+V6+/Zt2KNdu3bFYc6cOQMDA8lEIFvQz88PFd7X1xftAhDFaAGtFa1g9+7d+mNFLJo6dWrWg4f4AKW8vLyYH9pSgl/nU5IHo9auXRsPAWZcIjKFChViOxJD9evXB2yDlufOnbt8+XJY6keOHOG70Xbt2mXg1joiwa6g7QqRG4MHDwYg9e7du2rVqjTBByTAj+Dw9/eH0UzGq8YpKR5jFP2NkjyQGPzM7y1Bot42CM8oMDZQAQ9YHgDoA9nChQvVuUqgzn810y8Ykch/XI4nGOATZLt06VJak6l///40tfXatWs4xCNRfTnxEqwv3lE7SyUTRTxlyhRUp27dugGPEQfg0969e/nqSgufEjlPmjQJflCUbPll/apXrx4C2bZtG+9ISwcrRvGgNLNly5YjRw5mTF66dAmZg7JmfmjxJ350AKH4uHHjmAsVUM+ePS2KZ4cOHQzxs7tJtI4uq/NotmgRadOmRUaFhISggeOlZvh0aTFLo4f6QJvHokLeunVr0aJFtD4WKsPhw4cBqDCk0X5Rh9mwI1pmGRmlM100yRkRYy601zFvJ5CMFgpEtYu38BVPKin+ewdaDfAJDzc8QLSbWMLT9Y0Ij25g1MmTJ69evUqbmyhG+JOM7ulC+uLni0ryHFHANCElrEb+qxuaEECU9fyiFSmsZMGiQkI2Ed7HwEJ6rBctWpQfbIbXVd26de3t7XkWdXR0ZBMv8Rpo3bo1nvJ4/VSrVg0vDLwP8PKDscJ3Y8Luady4cf78+bt06QLSw/sAN2I7nklyPySjwUaNGhHEwv7mJ5fiqmHDhvExB53CsKCzuOmAAQMA1fTCM8gf/tmwNDwlYE2yzV0gNzc3/oFjNAJCQslExKKow2hfMPtgtTds2FCx5e9ff/2VMWNGeENNhn+cRaNAuwM80DQe2OtUyatXrx4ZGQn8y5w5c5UqVZYtWwbzDkDFjwbUI2JR4C4eArgcEUPrYztkvn79GlDq5ORkkFfhnjlzJn36ISFKo0aNwrXAD9jTuFyxNNq6desIonhlyJCB8BV3oe0Z8YhAOPzGxaGhoWRwG+TPZMAhxtsATgBVixYtNm7ciCYPk5fBsKlTd+7cQfRoTSM8tdSI2KpVK7b8LBPMFbAZiz8efTDZ6RTKZfLkydSrU7BgQeCoYvYBbLs0adLQ3p5WiOYHsmc1rHPkRrly5WCs40G9YcMGNiF24MCBbPtWEsxQtjIwL1NZqlHEFy5c4L8AklD9kHYW7IEDB3Lnzk2n0qdPD3zl+0jNClQzcuRIqtIomvnz59+9exfYRsBmkCkXiMuv//T06dOWLVsWKFBg9OjRI0aMAOaxjb5QmREC7YFZokQJ6nsEvBHb4+0D4EFJIT/piyfazty5cxXrbxnV+/fvAU4ODg64qlChQrRRNuoYMRiaALlAM2bMoOQgS3EjwBjqSefOnVEVrY4efunFh+q9e/du2NK0iODgwYPDwsLYtm14NV+RRQBskIfZoyrqSV2+fPlYr7skc4ui191UocDsp92SIFdXVzYOX/GkkuQaiBQZ5B2kyHLQaGKoBglP1zcitDi0eoZaaLZG10v7yllUkr+P4o2I2qbu20VVQ/PDI4+fZiAkJJR8FBISwv4/f/4c1jDsA3WDpeGyeOrB9IHdhte/+nn36NGjo0ePsglaOgVj6NChQ4GBgcyeo63G8EhVP1LgGS8/f39/xZShhERASCgRxMbmvX37Njg4ODo62qg3mJ44S8MN0NzUe5OgkrP+B7xhqanCmEDDNBWmhvgxukAgxVpEeoQ4wDg2ahpu2bJl3rx5sEEDAgL27t3r6+vr4+MDO1LnDoEwKmBjKRKF9OKOyBmYznh28Y8IjVPaAluaGkgM8+b69evIcO21lBRCYhVTIazQy5cvkQpCO8U3C22pt3FmMpqlpgSztX///njSnj17FigFrFq9evXEiRNz5cqliA9qDnIpcUb3kd69e4fo8WthJh8hkxE3ej8ihjZZDAYEjlbG38LoG9BqqSuYRi3SKf5JRUJuoJ4ompJ1TUxIIZhPQC007S8iGz8LiwoJCQkJCQlpyOjaRUkuo/NFbaJt27YhWKOGkRXDOL8subq6KkbJfnEKDQ1VzKFlmjRpEuAz8aMkJCT0dUiwqJCQkJCQUGLrW2PRypUr58yZU91zdfz48blz59r8dkmuJ0+e+Pv7R0REbN68mV8M+QsVLbrDz8IgPXjwYMCAAUkSJSEhoa9DgkWFhISEhIQSWz169DDE74GUfBQeHm6QV5HlV221icaNG4eQ8+bNO2rUKG9vbx8fnylTpri5ueHXtjdKJmrevDlNZkudOjVbSfjLFbjazs7OwcGhV69eS5YsWbNmzezZsz08PHr27GnRBrZCQkJCCgkWFRISEhISSjxFRUUBzHLmzJkhQ4ZChQp5eXklkynN+/fvb9iwYQZZ7du3By7aNvz169fXr1/f2dkZROrq6vrLL79YNO/xy9KePXtKlChRoUKFr2Z/41OnTrm7u6PGZs+evXbt2v3791eskyQkJCRkhQSLCgkJCQkJCQkJCQkJCSW2BIsKCQkJCQkJCQkJCQkJJbYEiwoJCQkJCQkJCQkJCQkltgSLCgkJCQkJCQkJCQkJCSW2BIsKCQkJCQkJCQkJCQkJJbYEiwoJCQkJCQkJCQkJCQkltgSLCgkJCQkJCQkJCQkJCSW2BIsKCQkJCQkJaSkuLu6NSrwHxan//vvP6ntdvnz54MGDCY5yUur9+/eHDh26cuUKc9m6dWvibzR679493DeRb2qR1BkVFBS0du3ajx8/2vZG6mCfP3++evVq295FSqKCfvfu3YEDB9BwLLrqw4cPgYGB8+fPX7du3aNHjz5T3ISEzEqwqJCQkJCQkJCWYOaOHDkyQ4YMBlk1atSYNWsW72Hq1KlFixbFKfgZPnx4eHi4FXfx9vbOnz8/AunatauNIp7Yio2NHTZsmJOTE1LBUOeff/7BYbp06YD0iRONs2fP1q5dGzctW7Zs4tzRUhnNKChfvnxwOX36tG1vxwcbHBzcoEGDFClSpEmTxrZ3SfyCvnfvnqenJ+6I+65YsUL/hYhhu3btduzY4efnh3xInz494PzzxVNISEOCRYWEhISEhJJGCek/TJwAeU2YMAEmL4x4Raco6f79+zjr6+ubkFvAnk4EFv2suQR17NiRR6wPHz50797dy8vrs95UoRs3biRnFiUpMgpasGBBhw4doqOjdYagsygVwb569cpWLMpHIEkKGnJ3d7eURRHJQoUK0f9Nmza5ubnFxsYmMBqfu1kJfa0SLCokJCQkJJQEWrVqVUBAgA0DhKk9YMAAGwaokLe3N0xeR0dHUx4yZcp0/fr1hNzC39//c7NoSEjI7NmzP1/40OjRoxWIlfh68uRJ8mfRBGZUQip8hgwZEs6iNm/C1umXX36xlEVz5crVqFEjG8bhcz98hL5iCRYVEhISEhJKbF28eNHe3t62U8vc3d1/+OEHGwaoEHVawog35SFfvnz//PNPQm7xuVn01atXRYoU+dw9V4JFdSqBGZWQCp9wFv0cTdg6Wcqiz549g3/bsujnfvgI6Rfa/vnz5wMCAvD78OFDtYeoqKgLssLCwpjjnTt3Lnyq+/fvJ06EBYsKCQkJCQklqq5du+bs7AxzcMmSJWfPnuVf+REREbt27fL29v7777/ZUis3b948y0mSJwSS7t69K8mDA0eOHIkAy5cvT+5wsXm0rWBR2OshISH4ExoaumrVKqCmelmaf//9Fwb98uXLYTmZYlHkho+Pz86dO1+8eKE4hWtBmK9fv165cmVQUBA5xsTE7NmzZ82aNXB59OgRjR783//+V69ePYTfo0cPZNHVq1dZICiCzZs3L1u27MSJE+/fv+fDR8i4L8Xz4MGDuMuDBw/UaY+MjIQ3pPHevXtqxEKY+/fvf/fuHe+CxL58+RIZgkiixJFX6mAfP368ZcsWBHXp0iWLypRnUZiee/fuRcyptiiEItu+fTuyF5nMJjriElbHaG0hZJfCRZI7mVmd1CntjIJQDRTxxF1QlCjQ8PDwp0+fSpoV3mh9UAfLWBTxWb9+/bp16xAfOoV6wrc1CCY7HbIATTVhdUFrZDKTnmaiUUUtYlHE1s/PD/6rVq1KieJnd8fGxh45cgR3wS8akZ44qMsCp1gGoiLBD5otc+FH+MP95MmTFCsUMUqNndJo8mgUiIavry9KAfVcT6q/HQE+j8lCGdEfVrFJqFrIWzrFLxt25syZY5/qxo0biRNnwaJCQkJCQkKJKtivJUuWJOjy8vJiy8aCxzw8PBYvXjx8+PDUqVM3b94cVrUkG7L9+vWjdYNg6cIFphj+//bbb2QEwyYbMGAAXECDXrLU1nDCZRGLLly4sHDhwmSsjxgxAqcyZsyIw+7du/OXBAYGFipU6Pfffw8ICBg1ahTsYwWLwlB2d3efMGECAqxUqRLu/ueff0oya40fPx7Xwj8M2eLFi9OyMSBGkEPRokU3bdqEP9OmTYM7rcuyb9++pk2b4vCHH35AFiG3JdkyGzp0KJgNETh8+DD+gFfJXL5+/TpubW9vnz17dqBgiRIlKEWIA2/DUc6gQDdu3IgQcEnp0qUZYqFoPD09s2bNChdAjiTD7ZAhQ7JkyUKr6TRq1AjBgotSpEgBc5wPFiEgPgcOHMAfR0dHXFK3bl0kAWBptrAYi+7YsQMXIn8Q/nfffQeLk/lBTLp169ayZUvcAjCGaCONsFMleWHktm3bIgSknSAZJYWzcKlVqxYSRSFcuHABSUMCzcbHbEZFRERMmjSpWLFicKEiJgG0WrdujfxHzEuVKtW/f3/JWIVHQzBaH2CaGw2WWHT37t0ODg7Usuzs7BYsWCDJHx1QeciRiOvBgwdLly7FIetKVTdhdUGbzWRJXzPRqKIsi3SyKLgRsVVkHbCTzgILEc958+ZNnz49R44cyDQ25F4jDuqyANAigZkzZ4bjoUOHJBnvUWmpzhPh79q1q1WrVnjKdezYEU88yu2JEydKpps8CRdWrlwZwd68ebNNmzbITLOp/naE8j116hQwkr6X4SGA/ygy/uPFo0eP4IgnD8+i//33Hw7Pnz//gpPRdQE+hwSLCgkJCQkJJbZouRF+gB+sqwYNGrDDMWPGwAObggVbkPr0yOIcN27clClT+ABprZpkNUZ38ODB8A8sBARKslFeoEABuNy5c4c8hISEwLiHcckuIaOWsShSXbt2beo5kWRcATkADmFpvX37FqiZKVMm+O/SpQtcYM2TBd++fft27dqxMGFes57MP/74A/75Mbq4O1zYDFIfHx8cwhu7IxAOd0TI1GlDdnOnTp1YCLgEjMd2xYBVV6ZMGYZYUVFRt2/fhs3NIwr8VKhQAS4oU5yV5MVdwULOzs4sWGBeypQpQel0uGrVKvIPKlP3FKlFLOrk5AR4A1yxpDVr1oz5QX2rVq0a64IDsbu4uIDfqBBBcYgAmIR5ANaqMQllSl9MzEo7oxBJxLlixYo8NII3cMiI6PLlyz169KD/igpvqj4YDVaSWRQZDkpEYl++fIl8RkEzdpLkyc+MRUmIPD+sV9GEjRa02UyWdDQT7SoqWT5G1+iz4unTp4BPFnOQM/yAnKnDWTsORgMEavL5CdGXIGJRtKyxY8fisHjx4qjbeBR07tz56NGjGk2eXHLmzLl06VL6HxMTU6tWLZ2p/hYUGRmJCnn8+HEqNWQmchIuz549Iw9xcXFwwdPm2rVrPIui1uGQnkWJL8GiQkJCQkJCiS2FIQu7PG/evLDJ3sfr1KlT8JA+fXo2+PDu3buwhrNly7Z79+6aNWsqVq1MhiwK+x7+p02bxlyod5chgaura+HChfkQyORlLIo7wnB/z6lhw4bwwHaUoX5U2F58IACPggULMqva39+fjVJTsyhsbuQqjcKV5K4heBgyZAjzoJhYSHPt2DzMN2/eZM+evWfPnnwEhg4dqhh6Sv11PKK0aNECLnwvJXXlMT807pEZ5dHR0YgGyFDSJ2JRvtcoNjaWOq/okAZqosrxV1GRIW58JA8fPkyHMGQzZ86cMWNGtuYqailwTk98dGYUPPA1ZM+ePThctGgR87Bs2TL6Y7TCG60P6mAluVgVK0IPHz6cen3pMHfu3AoWVdQE9eckSVXQejLZbDMxW0VtwqIdO3ZEu2MNDUWMm8LbuXPnzMbBVIAKFqXqxEY+E+7WqVOHv0q7yaO88L9NmzaM7Vl9EJLkLmVUSH7MPIoPLuyxfPPmzYCAADC8gkWfPn2Kw6tXr54/f/706dOXL1/W+YHJJhIsKiQkJCQklNhSGLLU/1OjRo2mKtEEOdKCBQvgzd7ePjQ0VBFgsmXR6dOnMxd+fiDShf9t27blQ1DMF23fvn3WrFnVeTJv3jzygBzje5BIBBWgAhi7ihiqWVTi9qIICwvr06cPPPDIpCCQf//9lyc6X19fGmDJB6ieBkmbr6pZlLcaq1SpAheWgR4eHjgEzPCB5MqVS9Ino2sXASccHBzof/fu3eFBsQzs48eP4Qg/ZOvv3bsXh4AKOhsZGUlbWW7dupVcOnfurHOyqM6MovxnGIZKQkTk6enJ555kosIbrQ/qYCVjaxfdvn0bftKmTUtpt45FFQWtJ5O1mwlJu4rahEVpUK66rTGY1IiDdSyKU3ztIplt8tTFXb9+fTwzdab32xGeHqiQ9PmABLaEC7WIqKgoxqUKFr179y7NEUVdPX78OP1XtLjPJ8GiQkJCQkJCiS2FIUv9J2p2UgjGa/ny5Q3xs0Z5JQKLwjjWZtE8efLAzmaH2kb20aNH8b9v3758CAoWLVmyZNWqVTWiZJQ9oqOjGzRoYJAF85dfSdIoi0InTpzo0aPHwoULib7YQFDJHIv+9ttvBtWuqjZhUUSGzwqQQKZMmRToriFTLArRf+pCVFcke3t7uNM85A8fPjg7OwPPqJNk8uTJAwcOTJEihaurqySj6ffff68zPjozSg2NO3fuRATgCEThfdqcRSG4wBsNgbYJi+rJZD0sKmlW0YSzaEREBFzGjBmjfaGpONiQRc02+du3b6P14cJUqVKNGjWKxp8LkdQseuHCBWJRvDvApYGBgTTQRsGiYWFhf//9N/IWZ1HniWBxbeJEW7CokJCQkJBQYkthyK5cuVIxFtGorl+/XqpUKfgE9fFrTkqJwqJHjhwxyEu8qBf5JKVPn55fM0nbyKblYVq2bMmHoGBRJBMEYup2kmn2gEU1f/58R0dHnAXCXb58mdzVLApbFqCCcF6+fCnFDz7Uz6K9e/fGIe7F390mLIqc/Omnn1KmTLl27Vr8Rw0pVKiQ/lVDzbLojz/+CA/e3t6KCwGfoE22hiox5PLly5HwIkWKREVFNW7cGHUAhD9nzhyzNZZJZ0apoVGS8aNu3br0cYHNVv0cLIq0Ozk50X+bsKieTDbLomaraMJZFCgCF9Q3U5dox8GGLGq2yUty/17fvn1pfm/58uUTczRpMhctoqseo3v//v0XL17gz6VLl0JlBQUF4RBoqlhll0RDdgMCArQLwlYSLCokJCQkJJTYUhiy+IPDmjVrKry9efOGVjSR5Nl61apVu3btWq9evdQ9ionAorBaiAeM7lkXEREB85130TayYQbhf/78+XlzR8GiSI6Bm6/ItH37doIEo+zBNkd5/vy5m5sbPCC3yUXNohQltleHpSw6Y8YMHP788898BGzCopJc+g0aNBgxYsSQIUN8fHzYLE09MsuiCNPw6VBPSe54R2IRW+YCKxZGP+IGHKV+M+rDnzZtGgLXP4pPZ0YpoBEly6Z04r7p06fHWdpqwuYsSmln0xdtwqJ6Mtksi5qtoglnUSQzZcqUqBtqrtuyZYvZONiQRbWbPJoAv5AV5Ta/jNM3rmfPntFuLsyF1svF04DwUq1Tp05JcgWA2KOYwJWtgfS5JVhUSEhISEgosdW5c2d+8B5MQFi6cJk6dSrz8+7dOw8PD7bu6Pjx42nPg6ioKNrbkLeDqWdDMWYS5sWtW7dsFWdYKpUqVTJwSwfxgkk9bNgwhYuGkR0dHU1LlfLr6O7cuRMuyBw6nDBhAnUC8/2BAQEBbDChUfbo0qUL+w9bysXFpXjx4nRI/c+jRo1iHmi3D2ZkEwzz6/FosygMa4M8g5ef1ksEgnsxFytYFAzm6uqqZ8lcozLLosHBwcAPJycnHnHhqDbuGzduTF8NKI2ollmyZHFwcODz2ax0ZpQCGvFnx44d7CwtJkx0ZLTCJ4RF//77b/g5evQoHRYpUoQP6vXr12DyVKlSMf+KJkxSFLSeTDbLomarqKUsCpxToyMgHI4oa35RNLR0yn/tOBgtC+oJ52NVuXJlA7del1EW1W7yyNhBgwYx97t378Jzv379dCb8qxfaJj/Vk1bHhd6+fRsTE/OYE43dRZ2n9kjL7bJtcm/cuKEY6/tZJVhUSEhISEgosUXmo6enJ6wHGJ1AJtoJE2ratOmCBQtmz55dpkyZtWvXkn9YYyVLloyLi6NDWm8WeEA7Z0ry9gYwlNOmTQt74ubNm4SpLVu2NKiW8UyIQBSwyO3s7BAm+4gOi2fx4sWw3RXgNGnSJNwdKWUutJwp25KBlmJydHSEvQvGu337NvWKgPTWr18PGAN104aNsE0HDx4MuxYGbtWqVeFOIdDsWYXNVK5cObZloiQzHoNkMn8rVqyI7Nq3b194eHj16tVpdCLuvm3bttatW+MQyH3x4kVYurDLU6dODZxg09IePnwID9myZWPh094VKB0YdoB/3Dpv3rwGef8VthEopYIfDkc79PC9RrQEK+v2mTJlCm06AkpBjiFDEJrRHmmjunXrFkJDTJgLUTTCZLWIKuHYsWPpEAXatm3bunXrKjpDtm/fruiHJ4akHhX90pNRtKkp22cV9MgjExAIDExfZ4xWeKP1QR0sBJxGVkRERNAhQqtfv/7AgQOZh06dOlHFQE7ivl27dqUPQH5+flT91E1YMlbQZjPZbDPRrqLwgDjAZeHChToL4sSJE/BfqlQp3pEW7qbWgSjh7k2aNGE9n9pxMFoWtO8LIBbYA4hF/aHZsyBtmlVODzHchY+GdpMHYmXKlIk9Z/CIQCHu3r1bZ8K/BV25cgX5D7a8evUqESabocBLMV+USu348ePwTJgK8Z+NPqsEiwoJCQkJCSW2QkNDaS/43Llz08b3MFJnzZpFq4YSZ4IByPOyZcsyZsxYo0YNBiogVfJWunRptuIRbVQIoxAWJIEidb7ZkEUleQQsGabp06evVasW0CJdunTt27fnVy2CNmzYAGsS3nLlykVWNZvAWbRoUdbZBQMadEGMBOrYuHEjDjt37oxEkbGOjCITFgIGg83IEoXxBOuWWc+4BUMs+Eespk6dumXLli5duiBubPYj2JLW4UTkly9fDheYX05OTgZ5XVNcAkai3R0RGZhltA6qQd6y8oqsZs2akcugQYMoyQgcGQ5ehWOaNGkGDBgwcuRIFOuIESMuXbqE8AktIFdX1z179oAJJ0+eTBtRIif3798fGRkJWmZ+zp8/L8mLjri4uBg+FXIJ15oto7NnzzZq1Igu6d+/f1hYGEJr06YNuXh4eLAOECAuEKt58+bTpk0DYIwZM4YflUqCS758+RAIc4Ehq+hx1SPtjLpz586ECRNomSLUkMWLF0syi6IWoRqjYsyZMwdNgO+H5Cv8jRs3jNYHo8FKcg88vCFdHTp0AMs1bNhw3bp1fGyRRSVKlGCF8uTJE8AbLpk+fTrZ6IomrC5oFpRGJutpJhpVFK0A9YGGVBQsWBCtSXstH1y7ZMkS2tvWIG9fzC/UjEZHI5OpgUyZMoX1kWrEgbrg1A8f+KFvYZSWc+fO4XbIcFT14OBgb29v6mtFfRg1ahTrcZVMN3lJZlHkeZUqVfBIBP83aNCA708WkuRHHB5cbAguGj57MPJSsCiuAruyqwICAtiGrokgwaJCQkJCQkJJoKioKLClYnEIABgc7927Z92iEbBN+YGgsDB4hLChEHlYOf7+/jAx+U0arRAlmTp4ESzjRl6gNRhY0dHRegKkEJAPIBzWb8wEywxWF7/GEuIPm4zhAU7dunXL0vwHAyCQt2/fSvKsrYTPs0JowMjw8HCAJQAMzADje+LEiYAW/SsY6dSjR4+0k6y+Ixs6bqksyqjY2FjEiqpxSEiImpMVFd5SoTIgWETD6FncFzWTfWRRj5c22oRNyWwma8gmVVSnAOFIlDqrzcbBaFkgtNu3b5M31gutR0abPMKh0c4oFLRunQ+Eb1BoZaiuyB+LKglaJR6YL1++NIqvn0+CRYWEhISEhISEkpFCQ0MzZcpEIzAVmjRpEuvVFBISEvrSJVhUSOgL0FezZDktB/8FKTIy0rYBoigTZ5F0ISGhL1cjR440GAw0eJvXgwcPBgwYkCRREhISEvocEiwqZF5bt251d3f/UVaTJk2mT59udAzVjBkzcJa8tW/fXrFNM+nFixdTpkxp3Lgx/DRs2FBjaE3Hjh0pqMGDB4eEhNgwOV+QYHZ4eXl9//33lStXTuq42ECwq+zs7EaMGJHUEdGrefPmwRy0yboI4eHhkydPrlu3bqpUqcTe3EJCQtry9/fH09LBwaFXr15LlixZs2bN7NmzPTw8evbs+dV8mhQSEhKSBIsK6dT9+/dpHrmvr6+Gt7Vr19Jcc8UiFgotX76cQgO+GvVw+PBh8qDebe+bUlxc3MWLF2klhqSOiw109+7d0qVL88v3J3Pt3LmzZMmSFy5cSHhQ7969e/ToES3DKFhUSEjIrE6dOuXu7l6oUKHs2bPXrl27f//+ly5dSupICQkJCdlYtmdRmFzXrl07LSskJIS3uj5+/BgWFhYUFHTixInLly/zfWIfPnyAnRoYGHj8+PGzZ8/euXNHPW1aKGlFy9AFBwdr+EHhwk/GjBm1gwoICKDQcubMyS8gwdSsWTNAi+HTHbS+aG3bts3ostp6lCFDhoSwKFqW0T5qK4TCmjJlik2C+jbVoEGDr5tFE1LPhYSEhISEhL412ZhFAZAgSdqjBryBPzhkO/yy9YLBorRkMJs8dv36dTp16tQp+nP+/HkxqypZiXYaQCFq+KGtojNnzqwd1MmTJ93c3GjpcPVmA3fu3ClatOjYsWNxlu1t9UXr5s2bjo6O6pk/OpUQFo2JiSlXrtzs2bOtu1yhPn36NG3a1CZBfZuiXRa+VhZNYD0XEhISEhIS+tZkYxYNDw8HRp45cyYuLg5ceu7cORzSgvJv3rwhRqWlO27cuEH73kjy0sPEnzSwE4BKh+rls4WSULZl0Z9++mnWrFkGedtrxUcHT0/PJUuW0PbQelgUl+/atWvChAk+Pj6oV2oPwcHBv//++8yZMwMDA3l31Eza+fr69eugtT/++EMxDxaHvr6+CHndunX8FB3c8dChQ7gXquiiRYtQq8kdVRdx8PLyWrFiBRulfOvWrYIFCyItU6dO3bx5M78O/l9//QVHJFa96cL58+cRpfnz5z979sxqFn39+nWTJk1w644dO+LW/Pgu9a2vXbu2OV44i/jT/y1btpCHX3/9FUGVL18ejgcPHrQiPpKcG2zLRCk+x/BweP78ube3N8pIvaXVw4cP4ee3337btGkTT3EhISGHDx9+9+4d3PmOX1PFLckbfKPWIeFIoOLU3r17p0+fvmrVqrNnz7L1ilDQqKunT59m3szWGUkeHYCgUHa4kG3ORuJZFJFhGc6KZseOHThk275bKivyxKisaDKm6rmljchoQQgJCQkJCQl9lbIxi8KABkP+888/dEhoSjvYhoaG4j8zuQhNIZhNERERhKnMbgPN8uEIJQfZnEWjoqJoQ+d9+/axU7BW8+bN+/btW50sGhsbW7du3cmTJz958oQWHsySJUvZsmVhJZOHESNGTJs2DXb/lClTcHb06NF0l4EDB9L+y2CGxo0b0/bl9evXZyHDHG/bti3i5u/vX6ZMGRcXFwJd2OL58+eHZ9yiRo0aKVKkgAkuyQOPM2bMCMgBAQ4dOjRHjhyo85K853jz5s3hH5a9n58f7dIGP+3atUNQqPbu7u7p0qVjhIZWMGjQoPbt29+5cwd82KJFi1SpUlnHoojAmDFjaJd23Jo2NTZ1a7DB+vXraeNpGrDQu3dvZAtQUJJ3UaOziAmCOnLkiKWRQaNGPiME8Bi5sD3ugS4oxA4dOiAyWbNm5dfaRSYj90BEt2/fLigLkIys/uGHH3AhChGYnT59evzH08ZUcUvykA1UOTc3N+ANnkK4C2oLu0vPnj2HDx+OWnfz5k1UP0QVjsA52ombttLWU2egsWPH4i4oZVyOgrO3t0flYdWYZ1Fkac2aNXEIyGc77OHCtGnTarcyo7IiT0zJuiZjtJ5b2oiMFoSQkJCQkJDQ1yobsygYAwzJ9kR+/vw5QSbMXBqgy7qt4uLiiEX/97//wTKDT7YHLjyfPn0ap9Q9JEJJKJuzqCRbvfBfp04ddmr27Nnjxo3DH50sOnXqVLAT62+BRQsIZGfBA/yMUwAPwoTRTIegVqDCzp076dDDwwNnb926JckTIwG09+7do1Mw9HmIovHDLVu2hDdkyP79+ynwDBkykAda6mn8+PF0CPNasTo/MG/t2rX0H5Y3kAyZRrs2w5QvUKAA+y7z6NGjhKxdtGfPHlzOj9HVuLUUv5GAj48PELR69ep8P+SbN29wKiFjdMPCwvhshFAN4IISp75xb29vHC5fvpzO4tEBIGGD/H///XecXbx4Mf4fPHgQ/4sUKYJ44umBFCEEjeKmEkQIdAreAIrUp4fL+YnQwCQ8fOj/ypUrGYuSNOqMJK81wn9b6d69Ow6BVexyxRhdihUgnHk4dOhQ586drcteS/PEqKxuMpKqnlvaiDQKQkhISEhISOirlI1ZlPASJgUdRkZGksv79+8vXbqEP7dv36ZTHz58MDUQF3Y8EezXOqvqC9XnYFEYzUACZr8CwAoXLkyjW3WyaL169RAxdjh48GBcRV15EKCua9euf8SrYcOGOPvbb7/R2aJFi2bPnp1dS2OGafTpunXrkAp24cKFC3EKUSUuWrRokXpJ4S1bthAmSXLfI7/wksJGJ1IFRbPwXVxc4HL06FFc6OTkhLTzISdkvqiCRTVuTR7Q6AAzSPuPP/54/vx5PqiEsygCV7Bonz594MI+UZ07dw6HoBQ6LF269JgxY5hnZD7KhdY8Qz2Ez759+/LhaxQ3rkLdYEMthg0bhlO0XzxqC/67ubkhgZLcXcn2l/f391ewqEadkeQ96PmC/vPPP3G4YcMG5l89X7Rq1aopU6Zk391QZ6zocyZZmidGZXWTkVT13NJGpFEQQkJCQkJCQl+lbMmiHz9+VOAlm/mpZlG1Z3KkobwAUQa0QslEn4NFIRi+uMTd3R3//fz8cEjuChZ99eqVHycgFrl37tyZQYUkd5Pa2dlRfxdsWZyaNm3asU/FyEdhWFO3G4UMVgGSHVOJKILMaJCGOmkRERELFiwYN24czdIkR4WNvnv3bhzu379fEfiTJ0+QMzi1YsUKPkwbsqjGrdkl1Ln3ww8/KIJKBBbFUwKHyC78j46OTpEihbe3t9GgiLuAl8zFbHGTQN0gq+rVq8PznTt3yJH693LlysVzo6SDRfk6I8X3o7Ju59OnT/OoJhljUeJVSjIgrWzZslav2WZpnpw5c4ZvU2FhYQlpMpKqnlvRiEwVhJCQkJCQkNBXKRv3i9IquE+fPqVDcOYxeb1cSV5Ug7dpQKdkl8D6IRfYYRcuXDgmL6XLb/cilEz0mViUDGgA5N27d2vWrMlG6ClYFO5pOOXLl4/cDx06BGLp168fHdarV8/T05P+086cCq7jpWFY0zK/pi40akajSk+aNAlsjPpP2GaKRefNm8eDEC8fHx+cWrp0Ke9oQxbVuDVTZGRklixZ4I0NxSQlMovS/6lTpxoNSs1dZov7ypUruPXWrVul+BJh+YCyGzVqFCohHBs0aMCWzLGURVH0WbNmrVChAn0NQX1AwbExxpIxFgV5FitWLH369K9evdqxY4dGj6VZWZonbdu25dsUvCWkyUiqem5dIzJaEEJWCFULZYE6nNQREUoMhYeH48UhbCerhVfDsWQzKQBPQtg2tMTDZ9K7d+/wcGAzLD6H8B5ctmwZ64ISEjIlG7NoUFAQGjMtmAE9fvz4mLysriSvsoj/rGmhjvLfyKOjo4ljYQwZ3XBSKMmlwaLXr19HwUnmWBR2J81L5FkUcnV1NcizRvllYPSvo7tv375s2bJ16tQJVuz8+fPZTEsa8kc9rrzYw1fDsO7Zsyf+I138hbDt6Klq1Ixu2bJl2bJl6e7aLLphwwaDvGqLOmLbtm1jMMZkQxbVuDX736FDB1Cok5NTzpw5ecsmkVn0yZMn+I+6oQiE5garuUu7uAMDA4FbyF5y5FkUDxzCRTydaDEh1CXyZimLSvJurvnz52/WrBkq8MiRI/l1mCQTe7rQB4iZM2e2a9dOvaKyflmaJ2olpMlIqnpuaSPSKAghixQXFzdp0qRcuXLxTyGhr1s0wsjUxzshbf3zzz/IvXTp0qHtJG1M8AwcNmwY3r+Ij602BlcID+ExY8bQypFGh3fZSog/fVX8fLcQ+jpkYxYl4IRBScPMgoODcXjt2jX8f/bsGfV5UlN/8OABYepHWQSxsBfRDuPipdgOQShppcGiTZo0oUmeGiwKqqlbty79P3ToEI80R48eNciiRYBINMzVLIsCkHr16qWw+EmoV7Cb7ezs+A08EE82BVHDsF66dCn+//jjj+/fv2ceZsyYQYa12owODQ2FC1iCDiMjI3krEJBs4BaAQYvAIUiPzWuV5HV6Vq1aReHAiOTfiGDRcuXKaeeDKSFLeZrSuDX937hx46BBg6R4QOKXsYmJiVGQpKWyiEUhmsvKj3EFxhBIq7lLu7hBNTwX0ZKwxKIIavPmzeSO4gYFIX/o0AoWHT169OXLl03lgFEWBYM5Ozvjpo0bNzadeeZlaZ6olZAmI6nquaWNSKMghKwQWopg0W9Hhw8fbtGiRUhISFJH5IsRb2F++PChe/fuXl5eSRgfXmi2NmdRhUXt7u7+uVn0/v37rVq1Yp+AhYRMycYsGhUVBbv2mLxxKA24hagfA82AVseFpQJGJW+0xCKbVqqQWLgi+Sg6OppwkTdSaZ9YV1fXMmXKkMu+ffvgx97e/vXr18wbjTaBFUuQI8lGaqFChfjwK1WqVLx4cX6mHK1B6ubmph2x/v3748LFixfv3LkTdwkMDGQLMkvyriEIxMnJafz48Yg5jLPq1auzfnugTsaMGZlnWnhmx44dksxduXPnpk96a9euBdF16dKFjZ+kka78lDZiSNwINA4Uge2eIkWKGjVq4F5oFOQfSINWQKsEtW7dGi7FihWDNY9o4xXYrFkzMtnpJQSspT7JFStWIKjvvvsO8VdvZWlWNOqyefPmAB7cSPvWaI8lSpSglWMgUIRipK6joyOy5cWLF4BGK7b/RdEgwNq1azOXn3/+GS4M3k6cOIFDVk82bdpkkFe7GTZsGChlxIgRKA4COUpXz549+fA1iptYtHfv3k+ePPH19QXb45BGKAGB6tWrxwLp0aMH+1BC3dT8uFmNOiPJo7wcHByAW35+fgcOHDh16hRbRZZE266wiQlMhG0JtDwszROjsrrJSPHtgtVzSxuRRkEIWSG0bsGiQkJGtWrVKpo+ljw1evRom7MoW4yDRB+CPyuLCgnplI1ZVJLniKKFE0wCOPk1Ud6+fQsQZagJK5DYg7YhFSyabAULu379+sSigKKSJUuWLVsWMJM2bVpypK0aYYIXLlyYXLJly1a6dGl4y58/f8qUKckRpPro0aOxY8fCnMVhixYtWJcX8IDNUgsJCRk+fDgFDg4BmWh8692yZQt12PIaMGAAnUUFg2WcLl06codNTOMDURVp70RoyJAhT58+3bt3L/XCgZRokCF8Vq5cmfwgwmw7kDVr1hQsWBCOwDbEmQ0pB+fAEdwI8EO1J5Br2LAh7oUajgzBYbVq1ZADkrzQroeHB+UMfvv27csIENjfrVs3OCKoPHnyIPMzZ87cqFGjdevW8TMPdQo5ACTGXfLly0eTYUzd+vDhw0WLFoVnwic05JYtWxrkYUss7dRZjdyYM2eOpTEBZxJmp0mTZubMmc+fP9+4cSNNTG3SpMmFCxeCg4Mp05ydndluq7AYqLZAbdq0efbsmSR35JLPDBkyICaMlEwVNwTcpSLImjUruAgh2NnZweeuXbuAQHAErIKppk6dChyiAFEnqQKgYnh7e+upM6io5MILWQr4fPjw4eTJk2nVaFCWYo3iyMhIVGNWB6yQFXliVAlpMup6blEjMlUQQtZJsKiQkFFdvHjR3t4++cwOVcvmLEqfO3kXwaJfsWCCwsYAi+GXHwTHBJuEugz5aUF4+wO78DanC8ncShzZnkUlebTD//73P1hX/NAsEpIKewtmrhVWtZCQWn5+fkuWLLlz586pU6f8/f23bdu2bNkymL/8Zp7//fffrVu3rFvUAdUYgescLv7gwQM2WhitgO0gIsmEqegik+Te1xs3bhjduwiOsOMRCMXBipgzoRkiCRSUnltrC48qK7pnEyJaXpttIWtWpoobiUU+sL53WmKK/JOQNLYgs3UCiw4dOhQEFRgY+Ndff+E1D+hyd3fn93c1qqNHj+qZGm21LG0CVjcZo/VcZyOyYUF8QYIpsHHjxvXr16OSkwueIWc50bsSrZi5sAH8aNTBwcFr167dtGkTv40tScGiKBcWAk3vl+SiIRd+YHlERMSuXbu8vb3xFLVuVWcU4pEjR/Ao3rp1q9F9wnHfPXv2wD5GJBUVAwm5fv06krZjxw60ID4CeKJu377dx8cHEVPP63v8+PHmzZt9fX2vXbvGfwSX5IaJlog7om2ytRX1CxbLyZMn8QcZhXD4UT/q4tNOJtLFSoHGRyBw5sJ/jUK506QVpHr58uWsWWkkE1kdFBQkWVKFJHlmDbJ0586dVgx1IaHV79u3D8V94sQJU28HU3dBrPDiRoRprhZqHaucvDTqpKnSwR/cDuYBspF/fSDfnJ2d0TRwCpewRw1iAp+K9Uq0m5gkYy19K0cFWLVqFdJi9ULoqC2IMAJBWRtlUY1MQCooEx49eoQKiXD4pzfsIvoMSqVPp3gWRRJQOihEhZ2AuwBLECU0Z5CJ0clQ2kIl5wfTSbLtgUaBkkJxI7ZWzMUzVbJCJMAn9eehPdIfxUuZlrWjU2wRHziiaSgupG/KiaDPwqJCQomjgwcPFihQQO0Oy+DSpUuJHx+hb1mwC7NmzaoezQHzl/UHmlLr1q3ZCtJC34hg9Q4ZMsTT0xOs0q5duxQpUvz666+SPAf+t99+o85kGKOEDbARt2zZApe5c+eS9Qa8r169OmxWWAzz5s1zcnJyc3PjQUvBoqifTZs2hYujoyP7VAdLccSIEQ4ODocPHyYXYI+Hh8fixYuHDx+eOnXq5s2bW2rtoSbnz59/8uTJV69enThxor29PRvmQFq0aFH9+vVhMcMkzZ07d5EiRWDHI5kLFy6kzZZgbdNkNogGUsL67NatW8uWLQ8cOLBu3brSpUuXKFGC/+AIG71y5cpIMoChTZs2OMtO/fLLL2hfeCOcOXOmVKlS/fv3158WBNuqVSvkA7IReUJRQqIk08WnnUyyAjNnzoxwaNIEwGDv3r00QoTmWiOq4IRMmTLhqsDAwPTp0+MUrbZgNJmoGyi12rVrG+Kni+usQng0IZ8nTJiAnK9UqVKGDBms6CU7d+5c8eLFgRZIBcolXbp0VatWRU1j0+xN3QVligykhJ8+fbpRo0aFCxdOkyYNchKh8bcwVSc1SgfZniNHDj8/vwsXLrRt2zZv3rxssQAwTMmSJeGza9euXl5esCJggqMc8fSGI49w2k0MyaGBYAgQjShfvnw0hKd79+6W5qEkT8ZBrBBttERkF3JSwaKmMgGQXKtWLRpug5KlDMQhko+ikeTKgDyh4WNesmgtOmJRGEsNGzZ0cXGhOomWwu6IGl6vXj3U6tu3b4NmUXC0Cr1OIWOR82j+ZcuWZY5hYWFFixZFnPFn2rRpuKOl2zdqlKyQJDdzWgiWPgLisU+7mfBdgyBMONKsScaiNFkSPlFh8JhCASEcjcUvbCvBokJfsHr16pU2bVrFcMeLFy+OHDnS6m+TQkLWCe9Ig2o/HrwJYB0afd3Ckhg/fvyqVatmzpzZokWLxIqmUHIRGAnAxg6rVauG+gMbS5LtCTJG+eXcgB9VqlSh/7AbsmXLxq9BBYxJmTJlmTJlmM2hHqP78OFDmKrwxs9YXrZsGaxtdgm/6CXCN3BTHnSqfPnyMHzZYZ48eWA7sgfyypUrEUk2IgPWMw2/Bx09fvwYxIVD2NZgMH9/f9ia9GEesUL+sEDQoGA9A3vY2JOcOXOyphcTE4MQWKYZuEXLYFpZNAAhIiJi7NixCAG4haYaEhLSuXNnmvOvUXwayaRDEBRjURJ9JiAWBQ7RygtgG5AASg2os2DBAlPJRLYgQ/r162fgli4zW4VwFfCVOtMopQ4ODiAHo/3YpgSzFTDAHl+wX2maAN7CVDTad0GhV6hQAZeAeWguQHBwsJ2dnbOzM7uFRp00VTqRkZGo5Gy2Oa3mwC8PTl862BhdNAfcHYDHs6ieJobcxiWAK5SXJNN1gQIFDOZ2TVPLx8cHTYb1QSFbcBeeRTUyAZFHJTHISx6CV2lMIq2PgKJh3bzZs2c3OkYXlQTIIclFWaxYMbgwgwpPBlzFGt38+fPXrVunP1EoHXon8izavn17tsSjJO8+YFF9M1uyQsgimiBJXdwoPrQ+uLABt3FxcXBBQ6NeUMaidGhp1bWVBIsKfcG6dOkSrBw8jMqVK4fXYcOGDb///vsZM2ZYMfRUSCiBghEAOw+1MX/+/E2aNGnevDlqIwxEWmJaLbwP6EN+7ty5xcTIb003btyAUQXb/X28pk6dapDnTpOH9evXK8ys8ePHM1sQZijOKjrh8QyEI+uENzpfFCRm+HRXJ6ACjeCCBQzjFTY9ixKMVHhOnz69YuSetgBIqPnskKYxUx8O7E6gyKZNm9hZWNKNGzdm63iTkT1hwgQ+QAAeHJkfEq3hTBRE202B9JjdDDOa/tCmVosWLWIXslM6deDAAYO85RjvqF18ZpNJM+d5FqWyY2tQx8bGGuS5+vyQV41kSvH7dfHLaGtXoRUrVoDn33PCCxT+Z82apT9ziJl5JqflCdhwVrN3oYTTzn8kgCVjQrN10mjpgMwzZ848atQo5gK+5deiV7AoqVChQjyL6mliVAmnTZvGPNAXAYu6l1GsQD7FmnNDhw5lLGo2E3bv3q1o6bgkX7581O1JLqZYdMuWLcyFWh8D4OHDh6dIkYL1jIEt2acWnaJNwngWrVixYsGCBVkm+/v7q+d0aMhsyQrR+jvsSSLJIxfgwj7boW0GBATgwaJg0cDAQByiyFAicLx161ZCFrCwVIJFhb5soUVt27YNdsD8+fPxalevUCoklGiCjXj06NE5c+ZMnz59586dZglzx44d8+bNU0z6EvoWBIqAnddUJbaLUlxcHMzH1KlT0/w6GJ18P1uBAgXAQgpEpHWnGc0aZdHg4GA4li9fng5hcLAtfKkLESyhjpVFcyxpnzZKAoxXmNEIltbPgD3Ng4patK00W8eORGuqK1Y9ffz4MRyBfHQv2Lg4rF+/viJwxJxGJ3p6elq3ZIDRbNQuPrPJNMui4A36SqW40FQyoc2bNytYVLsKtW/fPmvWrOok4ImkP3O8vb0VPedEOGyBNLN3USQcoi96ZDqbrZOmFuhisxBR6LR9FL90v1EWLVq0KM+iepoYsSi/6ZcVaw75+vrSQF/ekQ/HbCbQBxdFhz81JVpXUjLNojw2z549Gy5sYUIK1tHRccGCBdbtsEibhPMsSntQoywOHDhgRYCSuZIVQsNBxabh2aTz58+zDk9YyIxLFSxKc0TZTFHqXLVihrB1EiwqJCQkJCSUqKJeF+0RHOPHj2emob+/P9vrKCYmhqaEKdaJgUFP3fJ0aMpMr1mzJhuJB5OXbclD3Y9W24i8YPFMnToV+HfmzBnqF6XvMkgC/muMyjPKolWrVlWMNSXZ29vDndaeAfxQR1CqVKlGjRrFZ+zOnTtpVXZAkRULkxrNRu3iM5tMq1lUI5lqFpVMVyGoZMmSyFjttJsVfdpAlWPM5ubmBuxhh2bvos2iZuukxmLRYWFhyI1ff/317t27dnZ2BQsWZKfMsqjOJmYTFqWZvSBS3pEPx2wmGGXRNWvWwLFLly50qJ9F+ZX2aAg0VKZMGb7vWqfULBodHd2gQQMKE0VvdIlXs9IoWSE1i9L+mrRwIx77gYGB1DwVLEoboJw6dQpNAMVEV/Fz8j+rBIsKCQkJCQklqjp37gxr7OrVqxp+wG+wtGAi43+7du3Y1lb//fdfmjRp+N4nEs2eqlatGh2aMtOpb6d37940W49Nflu5cqXh0+Gs1gk2jYuLC9CIDnkWhWWsZgBeRlmUQvD29lZ4dnZ2BjAwWgAA9+3blxCifPny/JJLyCiaiWqwfGkZo9moXXxmk2k1i0qmk2mURU1VIUmexws4T/jCCjNnzsQtQLmvX7++fPlyjhw5jhw5ov8u2ixqtk6aquRLliwBtMPapkNLWVRnE7MJi9JucPPnz+cd+XDMZoJRFt2xY4chfiUnyVoWleQliGj/LeShpZ9y1Cwqyf3zSKyjoyNOZcqUydLVcbRLVogW0VWP0b1///6LFy/w59KlS6GygoKCcAg0pWHSNK2UVfjnz59T76hFEzSslmBRISEhISGhRJWXlxdMsfHjxyvcg4ODb9y4wQ5pkRuYlbSMKlO5cuXgvmHDBt7xzJkzcISJSYemzHQauung4AB6GTt2LHOH2QH/NWvWVPh/8+YNLc2iR0+fPoWVycb9Sp+yKE2qhPGtuArWEg29M8qiQ4YMgaNiQh3wBrRAlBUbG8uvTkRQQXNi79y5w2Y9+fn50Zq0fA6bldFs1C4+s8m0jkU1kimZYFHJdBX64Ycf4M7WT2bavn27ejc+bfXq1QssOnDgwDlz5ihmHJi9izaLmq2TRkvH398fjoBk5mIpi0r6mphNWHTGjBm45Oeff+Yd+XDMZoJRFl24cCGVOx1awaJsc513795R523OnDkt+nihZlEWJlDHzc3NYOHKQ2ZLVujZs2c01Ja50Hq5KAs8nI8ZEy1eRcjKeqrfvn1LZ60bnm2pBIsKCQkJCQklqo4fP04jLXmDGHZAu3bteGsPRjy8OTk5KazbJUuWwL1x48a844IFC1KmTMk66zSGL9LQzUyZMvFLs7x69SpDhgxwB0oxR5ihHh4e+neZo8lvPIsSWtBIWlii+I9IwqZkHgBvbCFfoywKwMMlyAR+W3IaHUokBn7gR58iUTjVr18//IepzcxxKX4mJ79ei1kZzUbt4jObTOoK45NZuXJlA7eEj1EW1UimZJpFTVWhCRMmwD1Pnjw8PQYEBPArx+oREJSHaoXM3kWbRc3WSaOl07dvX55YYFUbuIG1Uny3tmLUt4JF9TQxm7Aojfu1t7fnZ2XT95eVK1fqyQSjLArSK1KkCPusgCIwfDrk2CyLDhs2jN8Mlnr72XKseqRmUTZmWJI7SF1cXIoXL64/QLMlK4SKQQxJNfn169d0iLxC6T/mxEbhUsW7c+cO9ZpSOPfu3VP0r35WCRYVEhISEhJKbNGCounTp4dl7O3tDQyD7ajeZrZYsWKwRBXz1mDG1a5dO0WKFMyehuVRqFCh3377jfnZtm2b4dMNA5nCw8NhUvO7RJBoxz+oadOmMLthlZYpU2bt2rX6E/XXX3/h8tSpUx84cABpGTduHO1ysWHDBhq62bVrVxwi5sC2WbNmAa5gqrJNj2j5UPVSrsSorBcXvNe2bdu6devS+DGkHVzN7OY3b97Y2dnt3r1bkln0hx9+YOEADh0cHCzawH3Xrl0GbrkaJu3i006mj48PzqJkYQ4GBQXBwqY5sSAZWnY7KirKIK/MxA+Q00imFM9Oiu41ktEqhFvQjpqgFBAswBiEjGhYtP4fLegKYANzLlq0aM2aNSB/Nn5Sz13q1aun6CKm9WxZD7B2nTRaOqh1cKTiOH78OKALOZkmTZrLly/TPDqqTp6enjDcwY2UyRRPtqyrniY2adIkXILQmEvPnj0Nqp29zIr6rkuWLAkwAD2ipdCKX8icvXv3ms0EYlGUMgPpo0ePpk2blp9iSusb+/n5gWxpbmqHDh0Mny5PTevosgSivPjEonJWqFDBonShJiBAACdzKVeuHD+Eu0qVKiBe/QGaLVkh6MqVK8DIkydPXr16lUbeGh0IrZgvGh0dTVNG8VBC9hLBWjeh1woJFhWyXl/QorXJLaqITzLcAdXSTe0/h5JbSQnpFCzjuLi4pI7FlyTkWKdOncCEZGXC8FWDqCR3xYDQ1O4wo0eNGpUzZ84ePXqABACWbBMRPFsABrRbYLp06SZPnswW9GeC+Qs7XuGICwFOtPAsdThs377dokQhBNAvXQ7kAFHQGiqwF2kGKUzt4cOH07JDULNmzajL9PXr115eXk5OTnDMkSPHzJkzFWv/rF+/3tnZuXnz5rDLcQvYzazPByZ45syZYdcuW7YMaIGsYF1VYFFQUIsWLTZu3DhnzhxY5Oo1kDQEyKRsRDEht8GN7JR28ZlKJjvbsmVLOlW0aFGY0QMGDMiXLx/scgQCMGvUqBGdBcqyfl1TyURM5s+fj8IyyKueTp06VbHusakqFBoaSgxM2NytWze+H0yPXr58SaNwFQIysaeBqbv8+++/qJm0q2f16tVRLpGRkcgB8unq6krLa2nUSVOlg+RTJyfcO3bsiHwDouMQ9Ycsb0QJOWmQe56Bf6AaYki6L9COwtFoYpK8iQ51NubKlYvgk02DxN353niziomJwS2oLqGloDKMHDkScRsxYgT1U2k3TGLRWrVqIZ89ZFWsWFHRo7Vt2zY7OzvK6mfPnqERgeIM8iK0tM0PWgfRONJLLkOGDMFZEDsIFiCKgrZo80nkD5ukPXDgQEoIYgjkRhXdsmVLly5d2rdvr/hEoi2zJSskybOdAZ9sCC7Y0uirWcGikvyEIXYloZkkmpkqWFTIYqGiL168GI9svEWSOi5mhEfnuHHjypQpwzYZT1rFxsbiddWkSRNkXWLu3aQtvMLxqihQoACMp6SKQ3IrKSGLhIqdLVu2SpUqJXVEvjzBIofdoMEAsNU0NiOBrXDr1i1Te9hq6MmTJ6bsjA8fPoAh7927Z7Uhcvv2bX5MJoJSfOeCbQQbCOxhaciPHj1CehURwyEN30U+wOSNjo5mp+COs3hnhYWFhYSEWDoT0qy0i087maBTZBSlJSIiwuy9NJKpLe0qhOghCfpD4wUW7d69O0oE9u7BgwcBYMCYuXPn4lGgGAidkLtIltdJ5PzVq1f5l+zNmzfBluwwKioKAeoJzeomZqlQl1Bb3r59K8mz/tRrxpjKBDZGF/UcHkztwIS2Y9FmnkSJiBUajmKfVatFYaI2ogKzYQIWyWzJCpFQcHguocVZ9BiHZzQNXMhPiEgECRYVskZ4idIXwaSOiBnhCfXnn38inj/99FNSx+X/hXdJeHh4kSJFEKXkw6J4PdA6B0nIosmtpIQsEip2/fr11Yu1CAkJfa0CFYA5jc6NPHHihEVDu4USIqPzRYWEviDZniVgU167du20rJCQEH7/KwB3WFhYUFAQnlOXL1/mP9TBlKElho8fP3727Fl4S5y1m4T0a9u2bfygc1odMQnjo1OoZsmNcGi1huTDotClS5eSlkWlZFlSCRGehFOmTEnqWHwufd2pExISMqt9+/YZVFuASHKHzIABA6zr9RKyQoJFhb502Zgl3r9/D5I8duwYkJJmweKQdfVevXqVRiGDRfELDy9fvqRTMIXpFBuszE9/F0py3bx509HRkd/3VrCo1RIsalTJsKQSoj59+jRt2jSpY/G59HWnTkhIyKyePHlCsy5btmw5b968tWvXzp8/v3///q1atdLeOFfItlq/fj1KAXZFUkdESMhK2ZglwsPDgZFnzpyJi4sDl9J+NWFhYZI8vZ4Y9dWrVx8/frxx4wbNqZXiFx3GKfzBqbt37xKO2nxqh5B1unXrFm12PHXq1M2bN9MihIxFUb5Lly6dOXOmekZBcHDw77//jlOBgYEW3fHhw4eb43Xnzh3+cOfOneQHf3DIFsE3dTtGOKhOqGNTpkzZtm2bdbMLTpw4MWvWLGTCX3/9xbu/fPnSx8cHNfz58+fe3t7qVTegf/75B6dw7ZUrV6xjUWT7ggUL5s6du3//fsWbHqdWrFgxceLE3bt3KyaZxMTE+Pr6TpgwYd26deopWwcPHpw8efKaNWuCgoIULKpxOz26ePEi8mrJkiWnTp0KDQ2VZNylEqQFElFbFAWqp6TUwTKhUJC9OEUPHF4ojtWrV//yyy+bNm1CgPAZGxuLBFIEcC9JXkSO1TE8iPSEjGpG66DgYYVs5BeT+PXXXw3yTvQIDZlsae6hOKZPnw7D7vTp0+oRIqaKW089NJWWkJCQw4cPI3OQRWzQHWoIEjVp0iQ0K35dFqOpe/HihWIrDghPeNwLRblnzx5+jIykmXtCQkJfhO7duzdw4MCSJUtmyZKlYsWKXbp04fcIEUoE4QFbqlSpDBkyoAiGDh2qME6EhL4I2ZhFz58/D8OCLdlHaEqLm8Fw5PeuITSFYP3AcoKVT1wqcfvhJPLcWSFTOnv2bPPmzQ3ytk5+fn60KAWx6Pr166tXr96pU6fvvvvOycmJnzQ/YsSIadOmoWRhiRrk1er13xH2N+0ARtPxYXD/8ccfOCxdujRbJeLGjRupU6cGJ2vfjginVatWrVu3BlHTXufVqlWzaNkM0BEYyc3NDVehDmfNmnXkyJF0auHChbQeHezyunXrdujQIV26dPDA+vwl+bNl5cqV0RAA1YMGDaJvyRaxKPitQIECtPbG+PHjGzZsyE4BHvr06XP06FHcJWPGjPXq1aPFDyQZztu2bbtv3z5/f/8yZcq4uLiwTd6RjXXq1AHwPH78GBBSoUIFnkU1bqdH4F5EA/UEmd+oUSOUiyQvIgKrxRC/GxuKFViOvMqePTtdZbakjAYryU+Mdu3agahBle7u7giTBxtcBSMJ7AoU37JlC2U+Qvj48SPtyIegyCeyolKlSnBhuWQqZHighS5//vnn3r17I8K4hSF+/7eoqCj6UA1HtBd+CXs9Gjt2LGoakomSTZUqlb29PcqOjb8yVdxm66GptAQEBNBKmCidjh07Urbj0Y3cKFasGFoTwvf19UVMyMpUpw7EiyjBQ5o0aVgqYmJiunXr1r17d7wO8F5AZUNotNG5du4JCQkJCQkJfTuyMYvSCFu2gB4gkzo8YfbRAF1m5MXFxfH7sTLBJ1ErQ1Oh5CBQCoxF9RhdWMB0uHr1ahzOnTuXDmExwxJlnmlpb4u2zUU1IDJhLkWLFs2XLx9bEwyhgVfN3o4IJ1u2bBR5EFGzZs0M8t5i+iMDex2X/P7773SIe8HyZmuRA1Nxdty4cRQ3b29vHC5fvpzOAkHt7OxYJx780KLkFrEoDXyi/yBzmPj0H8GWK1eOdZ1NnDiRwd67d+/Kli3L1s2jJDDucnV17dq1Kwt/48aNPIuaup1OlShRYsGCBfQfKDJhwgT6T/OL+J3BixQpomBRjZIyFSx4hq2TAXACkgE4acHGEydOpEyZkt/QolatWob4Dc1pp2yWJ1L8HvTsMaURMh5o8Alip25eFEHevHlz5sxJnlG4tLGBRfkmxe/Xh4yiQ+Q8Dm/evEmHGsUtmauHGmk5ePCgQd607eHDh3howxtCoMDZ18P8+fPXrFnTVOrgH22TZ9ERI0YgQNZti0ucnZ2RRXpyT0hISEhISOgbkY1ZlPCSzVmPjIxko21pRujt27fpFGwUOsUvhv7s2TOYYnA8ffq02KouWckUi7JDmO88NsDKBOr8ES/aFpzfN1mP6tWrlzp1arbY/aBBgxAI62UaNmzYyZMnzd6OCKdly5Ys2EePHoFPYDfrXx8LgQwePJghDe2BxvaL69OnDw8w586dM3DbsiOjatSowYdmxRjdnj17pkuXzt/fnw7ZIlJglWrVqrGEI/8N8k53ktwfCNhgp2ilXCA0GA/5Zvh0e3HFfFFTt9OpQoUKFS5cmOE3uxwBKlgUWK5gUY2SMhosSoG61FhKXVxc4HL06FGc/f777xs0aMDHjYCNWPTff/9VsChflNohP3nyBP/d3d3ZtU2aNIELjeawmkVp83TW0Ght4Q0bNtChRnFLmvVQOy1Ehn379uVjgiqB+sCewxUqVACO0n+jqatSpQpjUTzVUXBosLwHLy8v9kFHO/eEhISEhISEvhHZkkU/fvyowMuXL1+aYlG1Z0neYotG+ULBwcGJtsuqkFmZZVFwGlvJLSoqCv+nTZt27FMxK1mnfH19EQ51haEKlS9f3t7envpCQRGsl0b7dkZXxKlevTocWW3UL9juQFy6nO37rGAAnusAUTDQO3bsyAdiBYsiTNrnun379g8fPmTuIIR27dopEk4dwgDmIkWKHFOJdhjn4y+pWNTU7XSKeuRQWMgrfidrPSyqUVJGg929ezcc9+/fr0gmaIeQqV+/fnyA+llUI2TJGE3xxWo1i65cuRIXsg7M06dP45DNydQobkmzHmqnhVh08ODB6vi8e/cOJIwMzy2LHM2yKJoJPAA+eQ+HDh2CI7Vf7dwTEhISEhIS+kZk435R6tVkkwbBmcfk9XIleW0MnkaAFmQMASQUgcBMpFP8jDuhpJVFLHrx4kX8Vy9kYqlgB2fNmhUIiv8wiGHaenh4pEuX7vXr1+vXr583bx55076dUcIBYvEdm3p05coVQMvWrVul+NzQw6I00hj8wAdlndmNzC9evDgudHBw2LhxIzk6OjoqQJfJzc2NwYNCnTp1Qjg0PFIdZ43b6RfNZsTlBQsWZOM8rWBRRUmpg0U1UHA10/nz53GqZ8+evKN+FtUIWfpsLIqHJ+o8mJNge9KkSRUrVmS9hRrFLWnWQ+20mGLR7du3N27cmCZ5Ihr6WZS+Iim2G71586YhftS9YFEhISEhISEhyeYsGhQUBIYMDw+nw8ePHx+Tl9WV5LVY8R8GPZ2CpcV6aYCjDx48YLNMJXmJxWPcGkhCSS6LWPThw4cKQ/P/2DsTOB2r9/8/thj7GkJIske2kEj4RtkjW5RClkrfL9rQP2QN2U2S7OvYsqWxjX3LUvaQfV/DZO35v7uv5vyO+362WcwMzuc1r3k959znPut1zn19znIdgbIzFNl00arLlSt3/vz5ZcuW4fz+++8rV66sTNr4Ts4jw0EhTpMmTeDZQCDRs0NCQvRcBcJFybPLsvKixxYFtVssu0LOBwwYkCxZsgQJEshSYZ48ebJkyWKznUvNnDt3Dg5mI5xuaz8CL8rezvnz5yt/Gxf1llykcnv27FnJQ/bs2WWPQxS4qN5SHqOdNGkSv0eNGmXLwz4LPFLr54LAuaiPmN33jYu6LQvDuXLleu211z7//PNOnTrpU3I+mtvtUw59l8UjFx08eHDixIkZw8UZKS66fft2AlSsWFEPsGPHDjy7du3qNlzUwMDAwMDAwEIMc1EhnOhAonqifKyIuCn0zJkz/F6zZo0cQIJ8Ck0l5OnTp4WXyvQ/CqI4lRpkEOfo3Lmz617jQz64KG0KwUiYMKFuXpzW/OSTTyKbrqyllChRQs6eEXNuC/rqkO/kPDKcvHnzRuouTdtCotiDDYSLAigTTv1aFFG7bTes+Aa0RP0WRic2aRo0aOC69yAu/att27bQyJEjR/KIZtLvRurbty+lkI2gr7/+uvKXPHfo0MF3clHI7ccff8zrwnmWLl3quteicrZs2TJlyiS//baUx2gZXvgBQ9P3Eq9cuXLs2LFUQooUKRIlSrRz5071SCxCCxelZvgNiVJP9Yb2EbPbH5sKDw+3sdzAQdG8HdD10dxun3LouyweuajeNKBw4cKKi3osnc5FyRWdlC6pj+EzZszAR1az/XJROrUyB21gYGBgYGDwsCKGueiVK1fQb1ZYVnCBUErRue/cubN27Vo53QRHlWBi5BPFRTb3rlq1Cq1Igq1evdrYsYg/kD1+ffr0oR3F3okc5BOrmO4IdVZRRLGUkyZNmi5dukARR40aRXi1YB4pvPjii9AJtUtTzjrKnZAKPpKT06S63jxt2rRnnnlG5TwQCEVp1aoVOjSvFy1aFCckTSjWW2+9hVPxB8QYpzLc8t133+EsUKCALC1u3rw5Xbp0+AwbNkxZ+fILeKMy1HT06FFe37Rpk9tagEqQIIHkbd68edOnT69YsaIcL4QwQB54VKVKlfHjxy9atKhZs2ZCY6AuUAUeff311/QynLLSCOeXG5i8JRcgqF5lH3vixInp06eXvnzixAnYCOScwYFoP/vssxw5chA5icI9/LaUt2jr1q3Li/ny5fvmm29CQ0O/+OKL1157TRh4p06deER7rVu3jtEGwZA6UfHwFs6ZM2deuHAhODhYLhchHr8xE5vrXktLlSpVwkctY6ZKlYq0zp07B/vST8X7BoQN/ty3b1+y9NNPPzEwKkvIbp/N7fYnhz7KIrvcbZuZ4aKyB4GWGjJkSMaMGZMkSYL8S090lq5QoUKEV/bAkDey2q5dO3HiX6FChY8++kicvmsPYaDJSI4aCLDeDAwMDAwMDB5ExDAXdVtnRMPCwoSFQhj0nbfXr1+HiCqzGejxyjoRqqH+iN/msGi8ArwuU6ZMLuu+R/TIfv36oSnibN68Oe24ZcuWV199FWfatGnF7AotC3ENCgpyWYAORcFQkGDKlCn67SPHjx8vXLiwLYzv5MjtU089VbVq1c8//7xNmzbo8bLbM3Cg30vx0cgpIIINpyI5+MDkyZMzZMjAo+rVq0OxduzYISvGqPLqlku0f7n7kUg6duxYs2ZNVG144JkzZwLMQMOGDYsUKQLlhn5AIdTVJm7ropSsWbNKwWFripkAKqFkyZLyiKZRd9K4rY2g5cqVwz9ZsmQFCxakFClTpoSsytqyj+QCAUQX4jFp0qTRo0dDlujR6hEsS9hU3rx5oaCVK1cuVqxY7969pUV8t5S3aAnTuHHjRIkSES3/33vvPbW8BqXkkdRArly5qCt9j67bMqiTJk0afFKnTj1u3LiePXtClaFMYq3XW8zUXpMmTfCk0mhHxG/QoEGPPfYYPi1btpS1R5i2VPuAAQMCr7qdO3eKhVsdtJQ6V++tuf3KobeyIMwSkhogq2rCCDlPnDgx/pBMWkrmgKhD6Vl66X7//Xe5AMZlGeNVWwCIOX/+/FQ4lfPGG2+o+5/81h7E9emnn8ZZq1atwKvuwQVVCucfPny4vnsixsEgpg8ODwfQE5D8B05bmDFjhj4qxgJiR8Y8QgxSxnKisYPItiOj68iRI20XGT7KCA8PDw4OjrJyaPDQIOa5qNu6r4XOduHCBX1zoAC1AwUIvupc8+Qt9C20c/7bDkQZxAdcu3ZNX6IJBOiUMNVojrxEYlM1lHGsSCWHLs6QF2XR+uuvv9C51ewJeYjU2TbSJXUxSKNOugYO2YR5+fLl3bt365ZpFY4cOeLN4C3JkXOPF9hQsdKmlE6P1m9ygeT21KlTNIczXRI9ePCg1KTHxvLWUr6jJZ979uyhIM4IqYETJ07IbxsXdVtl37t3r5wdoMhO890+YvYNSFdkaw8uChNGZdmwYcPPP/88Z84cGDJEDs6mB/PR3L4RqbLQUkePHlVOREUf0gMsHZUf2XHDbfWXdevWNWvWLLIvPnD45ptvIPbr16+H57ssW8cxnsTo0aMlcn1S70HH6tWra9eunTBhQpd3o1zxE3KeJSgoKNYurosFGfOIiRMnygYcjza6H3REoR3pgC7rbq37mrEHCHIvve3eNYNHEPeFixoYGBjETzi5aPwBNDtjxoxwPJs/1FRf034U8Pfff3fq1ElsDTzEWLFiBdIo0wq//vorOpnN2FhMQU4KPBBcNPBrn+/evZslS5YHgovqhSLbLVq0sN14dP8QazLmEaNGjYqfXDRwMfOGKLTj0qVLa9WqpdsveMRx5MiROnXqKKuQBo8sDBc1MDB4hMCXL95y0cmTJ5O3kSNH6p4QVDS5wI8WPxyYMmWKbJN+uNGoUSNl8Om+QiyQxX8uOnbsWLkELkDIQYN4zkUjW6iYRazJmEdMnTo1HnJR2KBtp4mBgUEcwnBRAwODRwXnz5+X05irVq2K67x4AAy5dOnSciyzevXqNWrUKFWqVJs2bYxF8YcV+fPnN1xUYevWrUmTJo3UAbz4z0WjUKiYRazJmEfEQy56+fLlvHnzxtq6tIFB7OPUqVNbtmwJCwvjv8fjPFeuXBETswcPHnRbG5F+8YLIWleJGgwXNTAweCTAqNqrV68vLPTu3Tt+Xl/MJ2H58uUDBgzo06fP3Llzo2Z62iD+Y9euXevXrxfrxOst4HPkyBH1W4Jt27ZNfNRVPQIYjuz0O3DgwNixY6GaznPOcjvat99+izrikYuiZCBjI0aMWLRoke2KKWJbtWqVnBY+dOjQuHHjcKoj3Ijl5MmTQ0JCnAePb9y4sWzZsuDgYP7bjhNLcpKxJUuWiIlmvULEdDP5obzKcLoU9gcL6n5yhcC5KBlbs2bN8OHDZ8yYce3atdu3bzMguCPsJgokJMqZOMWouA4eUfCJEyc6F+1PnjwJ75o2bRoFUSYbvRWK1KlzOQCvQPXu2LFj/PjxU6ZM2bt3r7MIgTS6Do8yFnhycgkCrUZLOavChgsXLsyfP3/kyJGhoaH69ledi6ITkxY+zvvMqBn8ERvEzGZnhIaTA66M2Aizfvjch2DIixRh1KhRs2fPVvo0zS0mu9955x0qxGbJafPmzWPGjEFKnZbPPdaGrR15ut4TdPlE5m2VGUiz4rN69Wrqh+QCtMruo958iLHbS1NSUVIW+SRRZFU6ZYvBR6Iee4cAUiQWE0lLrzS1FQgpFZ/z58+rt3y0lAEdTazA0pvkh81kA+JEBcoj6Tv4rPCC2LEMZ7iogYGBgYFBrAKN9osvvkiePDlqscyP4IMW2KFDB7GcLMFQAVu2bKnfdTR06FAxMgy96dix45NPPpk2bVqcLVq00OPfsGFDnjx5vvnmm7CwsM6dOz///PM2Looymjlz5pkzZ0LJ6tevnyNHDjlGiJb5+eefy63I8+bNa9++fYECBSTFGjVqXL16tXHjxvjkz58fn5deeklPVOwJDRo0qE+fPkSeL18+iZP/b7zxRtKkSR9//HHYtYowderUikVQnIIFC0omqQ0x+Yv2//LLL5M93po0aRLhO3XqpKcYIBdF+8+bN2///v35ARctVKjQM888I9fbQowhSGIFWlgQbEEuZ9aXE6kWmoba4FGDBg0SJEjQtWtX9ZSKKlmyJLo7pO7111+ngN4KhS5OJPBD20kBilC2bNmPP/4Y5Y8KTJMmTc2aNZWVvgAb3QaPMuY3OahCly5dEB6XdaO4NHRQUJAPg2fDhg2rXLkyEgWHeeKJJ6hqRXIUF/30008zZMggxpOeeuopVXaU4I8++ujZZ59FUJcuXcoPuKLYBaTRW7dunS5dOuJEnlOmTKlEzq9gLFu2DNmgumgUIiQAeXNbdsjF5n+FChWoEHVvNhQLefjyyy+p6hIlShB+zpw5PmoDAulsx+XLl5PVbt26fW2hZ8+eYrecVGD+/H/xxRf1VeIAmxVWRm6pQOKvV69ewoQJCxcuTCnoiR6bw0e9+RZjH00Jt5TMyy3f9JQ1a9aUKVPGZV315ztRb72D7kALMizQ6G5rcoQ6F+Pt7dq1U7XKAMVg0qRJEyFF3lrKQEA1yh2ZMtOHAPObzqVP8Zw4cQJPuT5TcdFz92LPnj1yp4nTBu39gOGiBgYGBgYGcQC4GYqX7rNjxw6di7qtFQDXvffuosvKjT4o1m5rNUaslSpKtnPnTngUKqB6Bd1O56KQXrRk1Flxom7yVLiZQEx8oX2KpnLnzh3ZPY4POZQwtWrVcmlXPcNkIJ9Kg/zpp594itIsq6nnz59H8UXvRM+WRarhw4cToGnTpipRMoCPvp0VloIPNSBOuedZXyIOhIuiJSdJkkSvDVR/W3nlzmdd64LC6VwUFRxqoZyihcPkxZklSxZ1zDs8PLx8+fLeCnXlypX9+/fLjWiqrlCyM2XK9Mknn6i3UAFpoCJFiqgs+W10b3DKmO/krl+/fvDgQamQZs2aodFSXT5IL/yWFxVTHThwIC9COcQpXBR+EhwcLMt9b775Jj7qpivaxWXddC3OMWPG4Bw1apTbWsOksHJ3FJTp+PHjEDa5YMy3YED4eUU2H7otMuOyLlSTDIg5JX2PLv4ItrpSG1lNkSIFskrZvdWGx3ZE5tVFbgCqz1M4898WoJRt2rSx7VgOpFnr1q1LBqQf0UAweQLMmDHD2/U8PurNtxj7bkpiUFxUQKspLuojUW+9g3oWEwnCRQUyUnXu3FlvnTx58sjtAz5aymNVPIKgouRCTREYWVHHR90geOvWLXwYxukmiovaQDOtWrWKSNRlcvcbhosaGBgYGBjEAZw8AR3UxkWhUjYu+s033+DTu3dv5SM6rlofqFat2tNPP61HKxq/4qKoxenTp9cVvoQJExYtWlQ5//e//xF+4sSJygf9Ep/+/fsrn6FDh+IzaNAgcTZp0oT4b0fgxo0bsiK3adMmCZA6dWqd3aEb2dRQJxclUVRbdd5JLrmVjb6CQLhohQoVbFdSL1261MZFIUs2LqrnFpIDVYOTqNL16tXLZd3ly9OrV6+Kyq62VsK7fBQKyDqb4jCif9sMaAvVVwa0/Ta6NzhlLJDkZCFdTTR4AxwAMjBlyhTlg/L6yiuvjB07VpzCRcmqCiCTFEoUcSInqk3RknnaoUMHcSJFsg5p2+/tWzAQqlatWtmK3L59e/nt5KLfffddzpw5b2uoWrWqLu3easPWjlSp2tAIT6ZPUTn69shJkybZuKjfZkW6EiRIAKFVAWCDBNBlzAmP9eZbjP02pdji1rmoZF64qLdEffcOWtA2CFBd1Bv9UW0PpreqqRC/LWVw7NgxWc9UPozA+KhDSXv37g0LC6ONfHBRPjrOnb33FYaLGhgYGBgYxAGiw0WVCuiOWIH54Ycf3Nb6JL/r16+vR+s8L6pUPTTpYcOG8RTFWj11clFZA9Gtj8rdgGp5TTblvupAaGioBLBx0b/++ovXn3zySeXjkbapfK5duxZWSQAUevXULxfdv38/Ad566y3dU645CZyLoj3DB5xFe/vttyVA8eLFeb1y5crOg5ceC/XMM8/oHCZ37tyQBNuNyrJzWHiC21+j+4BTxgJJLsDNzxAVgnk8bipw2i6Sdf7XXntN+agmhia1bt2ap++++6740CKyrOqM2ZtgQAh9UzUnF23YsGHGjBmd7avmWbzVhq0dFW7dulW4cGGXwyi6szb8NqsIcMGCBW2RjB492lsB3V7qzbcY+21Kv1zUW2P56B2nTp2ycVF3hK17tZGhUaNGGzZskN9+W8oAzsloo2YAwZYtW/AR6b1y5Yripd64KF8Q2cHrvOP9/sFwUQMDAwMDgzjA/eCiy5cv5/d7772nR+vRdhGqP2px165dUd8TJkz41FNPqUeBc1FCuq3Ncjov9YiocVH0oQkTJrRo0WLmzJnwB1uu/FKmOXPmEID60T0jy0VlIdHHgUkIAwUhTOLEiTt37qyH9MtFw8PDYQg4bUt/69evd1kmtcUZU1w0wOQC5KIffPABwXzskPTGRdX+cMGqVaveeeedoUOHLliwwGUZFhJ/H1zUm2DMnj2b3zzyliUnF4XpPf/88z6KGVku2q1bN/wrVapks0IUBS4Krc2cOTM+assxvIsW9LicpeCx3nyLsd+mjDIX9dE7PHJR2bYgsxViW1498ttSBk4u+ssvvwgXRRrhpRB7IZneuOjGjRvx101SxQIMFzWIX3Ba2Isa5HSBgcLVq1f5qsV1Lu5BlI8ixI5ht+gg1k5ZGDzQuB9cVBa4ateurUfr5KIjRoxAQVSGVaPJRVGU+V2vXj0fhY0CFz1y5Ej58uXff/99WQSTrZiR4qJyNNRm5SWyXFSOOHo7niegy8P/heYVK1ZMfcj8clGKRkI4Udn1MHKIt0yZMuKMKS4aYHIBctFmzZo5S6fDLxdFDFq3bk1yMqrLHl2/XNSHYMj6no8rW5xcNHv27BkzZvRhlDhSXHT79u2QrhQpUjhNtUeBi7otbpYmTZoXXnjh+PHj586de+655/r16+ctqwKP9eZbjP02ZZS5qNt77/DIRUG+fPkYkY4dO0b/HT58uPL321IGYkTXuUeXLoPw8IMPygELwjmhpvpeXFk4DQsL061hxwIMFzWIF6BX8F3JnTu3aDbRxKBBgxjgfvzxx+hH9XDgxo0bmTJlKlGiRFxn5B/wqeZjnCtXrqjd8CbncDp27BjjGYs+Tp8+3b1795IlS1asWDGu82LwAOB+cFF0C1ng0jU2GxcVp67RRpOLooYmSpQoefLkzsnE6dOny48ocNHSpUunTJlSaUVR4KLz5893KruR5aKy7NalSxdb5Dt27NizZw+jq5gLdluDm/ATsb7jsVBuB4cpWrSo6969x2DdunV4wtPEGYN7dANJLkAuKgcObYcz3Zb6K63ml4tKKdQ1JwFyUR+CsXbtWn7nz5/fpkwzOMsRWScXlS2+UD5bKrNmzRKRCJyLEh6u6LJM4ypPMQvssTYCbNbRo0c3adKkffv2PXr0YEBw+4PHevMtxn6bMmpc1Hfv8MZFxU7Sl19+Wb58eX1I8dtSBmfOnJHbXJSP2MulqmXzrRNr1qxRgfft24eP73m3+wHDRQ3iBcLDw8USRoxw0blz5xYsWFCujzNwW9uZKleu7PzMxAmuX7/O18v31LUPoE8ULlxYXU4Qr8DnkG+Ay7owIK7zYvAAIFOmTDaecPLkSXyyZ8+uzuqIdcqqVauqML7112vXronZT91yLEMiPm+++aY433vvPZ2L0iVd2v5Md+S5KKhYsSLOV155RecA/fv3nz17tvz2y0Vl3UbuJ3RHGDfiLbWhQ4o5fvx49YpfykR9yi0Rur4lG3d1Lpo3b149nj///DNBggS8KM6VK1e6rB2GOqU8fvx4gwYNIPxQkQ8++ED5y3lFZa3HViiBjcPI4i1Vp4dBHYfeK6UwylzUKWOBJBcgF926dSvBeHHx4sXKE2KjNkX75aL58uXTuajMkqiDuB7pjW/BQJfIkiWLjXTRoC1atJDwfDtc91pqhfNIp9OvvgwLC1N7zgPnosLoXnrpJX0mSOUkalx0+vTpkf1Weqw332LstyllwwWUWD3t1KmTSzO85DFR373DGxeFfyZPnjxNmjS2k95+W8rg5s2bwjBFLJF8cTLI0zVOapC9u/RHdXeU29qrjydPYznbMc9FqYhdu3attbBz5059azjifvDgQQYd1LXt27c7N9m7rXtvfrGgDBAbPCKQ6f8Y4aIG8Rwy+R01Lhr/kTBhwoeVizK8f/XVVzEYYUhICN+CGIzwAQKaseyW1O9wd1v70ETD279/Pypp8+bNcaJeb9iwQeb+e/ToYVugePfdd12aoRRZVUiVKhU8kE8w8ch6AsQPenn16tXPPvsMJwRsx44daKitW7dOkSIFmaEt5KCRkFW1fOGO0AJ5UfkIpVFmZiB7LgvFixcnh2SmevXqaoELgpokSRI0XaUSiAlNmJKKUAyEtm/fHjGj4ORTaCRVsW/fvmHDhok507Zt2y5dulR4RaFChfDxfXZOKidjxoxjxoxB8fruu++ENutcVC4FqVevHgmhi1Pn2bJlc1nXXch+ezHXmTJlSrjl6NGjyarUntvStiH/586dk6jINiOA2pVjK5RMMci9lGprHJ4vvvgi7FdRVuLMkydPt27dVA79NrpHeJSxQJIrVqyYS7OB7AMin8QGpenfvz/EA2px9uxZefrtt9+6rNtQVHixo0sGxFm2bFmpeaSU0aBu3bo4S5QoATWCt1D5OBFO3YwKWrVvwZBZElC+fHnqjQ9N/vz51WREaGioSCmq+cKFC48dO0Yq0iJ0PYgiEtKqVSviVEctvNWGrR13795NbUOidBvFKPrKCq50GZ1f+W1WxCYoKKhIkSJwQvo1RHrGjBkQBt8nbjzWm9unGPttShqIR8mSJVuwYAG6fffu3V977TWXZpTIY6K+ewdkgVdy5szpLIJYsYJH2Mrlu6UMAOMhfBIt67fffpMLXTx+ZJ3nRREqncfGJmKYi/KlFFbN5y0sLEx2Ld+4cUOeUi9STrio7Ei2nfsipDwCDBAxmzeDeA7DRR8dGC76gAL9wGZ0JDpAg4EvqUsCHynMmTOnfv36ojH/5z//CQ4OVrZkfv75Z7nyHkFiPDx16hSa9yuvvILihWI6adIkIatZs2YVhXXw4MFUo8u6pVAtQg4dOhSlUCJBGidPnowTBRQmgKaIfixLOpDDJk2aoHmgH+OEgMF4iVBWVgsUKCBLo6j7ws2gjijE8Mnx48fLWmL69OkHDhwomSdy2ewq+u5XX30la6So5i1atBB/aMmvFkSRBai8Mg1/4MABYpOlFZEKYpYzZhQZ/RXiITc6ooZu2bIFgicxoOurncBOkFvZKAsoV8+ePZctW2bjokeOHKGwEqZatWrUOSwXutKnTx9ZNECHhq9SXRJGv2eV2iPbpUuXphFhQVWqVNGXuWyFQjUSsiEJzZ8/X4LRsp07d86SJQvsHdpPJPrtGgE2euAy5iM5eqXMRAhhIznftAetDylNmjSpvEKzUpnyiEYRIUH2EAZSnzt3rmxhRaS7dOlCzFRImjRpJEyvXr2ITS7YRGjJP9mWaGFHejF9CIYsSFJjUu0uywitupHSbU2LiGVXRBSqrJpJCK2Qsbffflvok7fa8NiOMsdBQ9eyULNmzTJlykBNYYDID02WK1culzVJREmRqwCb9f3333c58PTTT6t6tgGy7a3efIix76YU9O3bl/GERzQZI8DMmTNTp07NqLJo0SJvifroHRT/pZdeklcoo23vMfSpWLFiztJ5aykDBSSc2lNbcH/55RePXdjJRS9fviyvKNYWa4hhLio326xbt46SI9ZyZFbMf9EHhKNSWgaLPXv2SB3pr1M1EFSho4aLxivw6eIrwrh88eJF1BpGUtt81ZkzZ6ZNm+a2juLwnZDbzN3WbVGMWXzt+NTpOwEEyMmSJUtQDsaNG7dx40ZXBBfFc6oFmc1FPRInoqW/fv36ddm+wjiuL6TL9b56DhFCknBbM5dff/31qFGjbFYEeWXevHnkc8yYMfpd6pGFt3o4ceIEqmT37t35cNqmKkka7ZNPNRlTW6QCqYGdO3cuXbqUpqFu1ZYeEkJZJGk+D/qmf8ZrMuC2tjCRQ4lNXXJN1xMfZazPR4YjBcbEb775hiamjMpTcVEyTz579OjhVCV///13CkKLkCub6T80D/1KcWSSVmOEOXv27OjRo/v162czBrh169b+/fuPGDFizZo1fMkilX9EdGoEkCicqvaAtC+Nwm91u53ioog0mSFddV5IwKeC2uDRoEGD9HMdAm8t6LYO9lCZvKhs3EcB3lJHFZBCyfEe+IM4Vbnkhkn0AzyRT/Fcv369rEUsXLiQVkYFEfrB+C8VNWPGDAmJIEmE0gQ0olzazmCCp7Lat2DBApSVsWPHEvMja4GMTkpbi3RRn1Gbpabb0pSyrHHlyhXbiEeTIV26ZDK80x+jl/F/gP5KulE7vkU+eVff38hXA1FRTkQiaroBL1JAidl5XtRt1TNJq81pHhVcBiIGNNsj4hTVjXfpRNeuXfNbKG8gDIWNtQ1yMZgc4oRSG7UOixDyrhIYhJBc+a2uQARj//79Hg3DivA7pZ1IaF9nC8Yh6MWfffYZIzaf+2XLlqGloICh8NStW1e/tTVS8CjGCr6bEn+eCrdBsP2OGH57hw/4MOUaD1sqvoFWpompogfC1FMMc1G5x0ZZDxNqKicB0D/EgpM8EmoKlCijUIqtJzloa7ho/AGcJEOGDC7rsFCBAgXKlCmTLFkynLKlB/bSrFmzRIkSPfvsswMGDBD74zKbjt5cvnx5mABh2rVrlyZNGn2ul35SsWJF9E4GKdRZmS4VLspAI1NfYg2MsQxCa9Me4DNEPn/+fOju66+/HhQUJKcgSEKOoMj02+XLl2Va8Zlnnhk8ePArr7yiNpaoqIj/pZdeQpM+deqUHIGgvBRH36LmFz7qgSy1bt16+fLlONOmTVupUiVYtLxF2atUqQJdoddAD3ilb9++fmsgLCxMNt1RtCZNmqRMmZLfdBk0nty5c/PR4rvepUsXOWPGx5jUEydOrA5rEafMjKoDMHxaGjRo8NZbb8k3xkeGAwe6XcuWLT/88ENyRVSkSM0LrRUu+tFHH9Ec9evXL1WqFM5PP/1UvUsF5syZEzp0/PhxhASRE00F1scrLs2Ui1r/gc/QiI0aNUISMmbMqPZcTJgwgfzTsij0vKXfKh4gZJtZwYIF5cvHgJY8eXKKQz1LAD7JefPmlckOdwQX/eCDD0hObpBX1indFsd74YUXEEWafvHixVmzZn311VeVWuCxBQUdO3Yk87DHr776yuW4piJA+EgdGZOeIh2H5kPnoDIff/xxKSPCIIsDM2fORCuiEeUOvVatWtEoNKKMEuRZlA/GfAYKJXViStEVsfMTIaxRo4bLOrVIhHL+591332UEQNigDTly5LDNPRkYxAg8clEDg3gIviO2q5gEfCBs9zYZGDy4iGEuKluT1anis2fPyloovFw26KoVJ9u+ZAJstICqarhoPIQcFmratKlMrsO7xDyATC6gO6J/p0qVKjQ0FDV00qRJ58+fX7BgAfq6btYcvRwfNR9RrVo1fZCdPHmyS9ujK5xQWaYWkx5Ke0C0yIDaXSD7e2Gk4hTjBPpGKbTkpEmTqhWexo0bE0DNqvbq1YuMKXNtTz31FEwyCrXksR7QyIsWLarseXTv3l3lDbGHEiuT5XQKSBRZDaQGlixZ4rJOfMHWqA2YKrG1bdu2Tp06EoCu1KJFC/nNoyeffFI3HCJb5nR7dBAn6XQ+Mhwp9OjRQ7WI22p94hH+JlyUVGTSmrSocxi1hLx58yZZJbw4hYSrrMrtEbpZ0Xr16rmsk2wy/zd69GicavNVgQIFhgwZIr+RRiQ5sgWhJqk9mkbN3MO+SEItseJfqFAhtXqMDKRPnx76LU45hCN7QAhTunRpdcTOHWH8Q12G4a0Fp0yZoux5ANnapNttD7AgvlMXMzl6WyNgwkXd1gSi696LAcUYBmWXpRUGB9mlpiq8ZMmSutSJ9Qs1xSMGctQeXcQYp9ozBrf3ccGAgUGUYbiowQMBGXJr1KjhXNoaOHAgw2+c5MrAIMYRw1xU6KU663zhwgXxQVeDLfBDXWmFViSPZEoelVTxUsNF4yHE2ps63OKOuDdFXa2B8p0vXz79FZhGkSJFdB/RAIRjCBuBs6mntvOiYk1Oadtib01pD++//77tymN4ppIuscWnq9TPPPOMUqndlnVHAqh9hpUqVUqePLl6+uGHH/IUjhdo7Whw1gN0okyZMqMiIGecxHLDrFmzEiRIoO+dQy9X+rfvGvjtt99cjhvtoRlBQUHKDp5+YB0SorMCsRnQsGFDcR45ckQREh8ZDhynT5+G3v/000/K58SJE1AR+aY6z4vKgS5lYAPGuGzZMvn9448/ujTjmWJ+U+eiYuRAzXNt2rRJX2XNkyfP008/rXhj1CzliIUJZXFBrlPv2rWrymHPnj1VYNt5UblCICQkxB1hztR2vkuWuGWOxlsL5s6dG06rGkVMUOi2RgKB39R9dxwnF3We8RZyq24PskmdmJH0xkXFmE3NmjVl4+iVK1d0EyAGBjEFmd5i2I/rjBgY+IHYdipZsuRXX331ww8/jBw5kk9b9erV9VMqBgYPOmKSi6Jl6vTSHbHt1iMX1QOLySJ1B5HhovEQTi4qZAbFUZxwMN0w982bN6EiNgsueLosYwPuiAvBdCPpkeKipUqVsl1frsMvF7UVR8zuq2P6vXr1gk7YjlcFCFs9gOeee65BgwYr7oWUq3PnzlmzZvUWVSBcVLcO77bqEFItJNPGpW2swG2trSVJkkR6a/fu3ZVNRR8ZDhzE5nJcp67g5KKyeGjr9Xv37kVOZBFbDru6A+CiNkGSZdKkSZPC3KLWpm6LSCMSasWyUaNGTzzxxJNPPinUml6gn2yxcVEx6ii7tcmDy3HZoFjalFtqPLag2Cfs3bu3rVEie7DZb+rR56Juy7ZkqlSp5HekuKg7YsMCncJ2+aGBQYzg6NGjXbp0yZ07d+rUqRFUhiDbWXQDg3iF69evM/Kj8GTKlCl//vz16tUbOnSoEVqDhwwxvC66Zs0aFB1logY1d4VlL9dt2VnRlSfYqahTqFkQEnl0wILYLkLLcZq6MYgrOLnopUuX8FGE0MbBaDvZQWqLJ3PmzGnTpnVH2NBXExDuSHJRNIkqVap4y21kuWhoaGiCBAmUJYBKlSq1b98+gFrxACcXRS/Xr+TSUatWLTR1b5aBosBF3dbKKl8sl2WWcPLkycrfyUVDQkJc1hlgCBW8VGXDR4YDh9SwzcCVgl8uev78efLQo0ePGzduyG31UeaiQE694vnUU08FclG4R9SoUSNx4sSMaUeOHKlcubJQ3GXLluFUHFXgg4vKgUn91DQIDg7W97U6W1AWG1UNRBl+U48RLor8qxmWyHJRvgudO3cWU4108EfWdpGBgYGBgcEjghjmohs3btSXNE+ePClmdd2W1cQVmvng8PBw4aJolmJT1wllGsQgzuHkonJnsdqa6ORgaP9Jkya1TeDhWb58eX7Izk89wkhxUVTkDBky2AzqqAOfkeWibuukXKZMmWDIqMKDBw/Wr2uPFJz1kCdPnixZstgIJ0o2rEZIlLrmW4A6LuWKAhcVw5s3b94cMGBAsmTJINhqZdLJRUnoiSeeyJs3L4RK32LqI8OB14Owjn79+tn8pY18c9FLly7lzJlTTQdEk4tKnZw9e1ZM8GfPnj1qZuUkG8hGhw4dEDCiTZ48+ZtvvtmlS5cFCxboIX1wUV7nt+3MqtwGKXuSPbagbF51Hm/TzUgGAr+pxwgXzZEjh7pPL1JclFKL0SM+Ey+88ILLOqAeqQIaGBgYGBgYPFiIYS4qhBMFRbS9HTt24Ny1a5fbuuuC32vWrBFDnXJAFJpKSNTTkxrEABJE1Hb7qEEcwkneQkJCEidOrDbZOjmYrHyqGx3cEbZJhg4d6o4wL6TbthG9FkVfnKj4ONXBuQMHDrise6vEKbfh6ZZX4W+8Ir8jy0VRslu2bBkj8uasB/JsO9pHF2jbti2a97hx43j00ksv6bc59ejRQw5O+64Bj1xUvzJbKkGZ8HFyUXeEXaLChQvrW0x9ZDjwejh48CCULGPGjPpWYWRGVkp9c9ExY8a4tMu+Z82aFR0uqteJ0PvIUjjBnTt3smXLli9fPmiS+CCEQUFBpUqVsvF2H1yUTCZKlKhAgQJ6eOoWhiwTEB5bkEES6SVa/V4chspPPvkkUkXwm/rSpUtd91ropciZMmWS3+Hh4baad3LR06dPk09lUpi6wqkuDrG1bOfOnfXZFkQasiq/b9++zbtZsmSJVAENDAwMDAwMHizEMBe9cuXKypUrV1gXhwJZ3pSVEDQ5OQiK5gFHlWCHDx92RmLOi8ZDCHlTq2fwAVTwTp06qQCpUqXKkyeP/gq6crp06UqUKKEO6UGuSpYsKUuOEBu50vrrr7+GieGUZSvCyzrhtGnTZJ/e0aNHUXnbt2+fIEGCvHnziuXVQ4cOyY3MsNkJEyb07t27bNmye/fulYRk96nOpnLmzCl7gwViikYZcUEdz58///Dhw+fOnRsaGrphwwZlRCeycNbD9u3b5VbuVq1azZs3b/r06RUrVhSzSVRFwYIFpdQjRowIDg5G0VfquO8akH2buk1UQG2oS70JRoBNmzaJs1ChQjht672nTp1KnDixsljrN8ORghibzZw5M60zadKkt99+Wy11wqlcmuErd4QtXJnaEMYCef7jjz9gR3Xr1sUJ7xK2SdO47rWlJBMTyszPqlWrcH7wwQfifOaZZ9T1jBDC9OnTR/keZzlvqfa4CqO2LTPC212a8R4wbNgwnUt/+umnONXNrmfPniVLc+bMEae3Fhw6dKjLumGcTkTtjRo1CoGPwiDpO3U5Fgs1ZfQm9c8++yxHjhyydC/Ti4j3E088ce7cOQRS/rusS1wUG6faaTjllF3BcE5abdGiRXKdUqNGjaRFxP5Znz59EMvly5fDRXVzMu+8846+BmtgYGBgYGDw8CGGuajbOiMaFhYmLBTCqe53cVsrVxBRtQXX23XGhovGQwgXrV27NtQIVvDyyy/LNZhua71OFqZkhWTLli3qrcOHDxO+TJkyEE54CIqpvqsWPlmuXDneSpYsGZRs8uTJKVOmbNasmSz+oJ7WrFlTooWhnT59GvKJ1jt27Fh5Hf0YmiEBihUrptKFwsF48YR/jh49mhTlPkZZdCWeBQsW8Ej4jOwPhG6JwRgd7dq1i1QV+aiHhQsXZs2aVR6RZ53X0UEolHC/xx9/XD/L56MG6Fk0Af6pU6ceMGCA6iwNGzYsUqQIvIUSoffLIUAInqx/uiy7u2j8erYbNGjg5Jk+Mhw4bt68CTN57LHHiIT/n3/+udyJArmSK0myZMnyww8/UEykS+4IhZEiFVevXpXLZhEM+OqFCxfgYDiJAZ7ZpEkTibBfv35QKcRGrrWsXr06DGrHjh1SM9myZRNLg7lz565QoQJkGGGAVK+IxjUh0DNqQ+fzhQsX1hd++S0yAKND6q5cuTJ37lyR0meffVaRzBEjRsDx6BF0IppYz5LHFnRbxt7gbEFBQdIodCtvdqH8wkfqAE+Rxrx589LFKleuTOfq3bu3bB6GnfIobdq0SJ07Yl20fPnyNCgtVb9+/aZNm+r3j1NjctkvcX700UekJaeR5TYC5DZTpkwu6/5VaDCSmTFjRmKYPXt2r1694KXmK2BgYGBgYPBwI+a5qNu6r+XSpUtokOo6PgU0KhRNsZ17P5I2uE9Qm1pRSeE2kTpxFx4ejt7s7QTmxYsXZXn8r7/+cpo5RRlV0xlqdUvHCQuBZ8YjZs6ciYJOudasWbN48eKQkJDg4GAIrW5VJfo4cuSIt3tiIC1QWY9GjPzWgA7ZRnv58uXdu3cHaDNW3cAUqQwHDrK0d+/eyPZ3qgKZUW9Bb/RZrchmwG1x/n379kX5GLCCrbqiY1+N6nUuv/tuQfJPKfyKQZRTF9AlDx48KH3cmdahQ4dUxtQeXbJNxjy2MnmmKYXK8qJtpzctq3bH3IkASSij1gYGBgYGBgYPMe4LFzV4+OA8L/rQYMmSJblz53b6T5w4Mco2Vw0MHgV4tF1kYGBgYGBgYBAgDBc1CAjCRX/88ce4zkjMo2XLlsmSJdO31Lqt05idOnWKmsFVA4NHBMJF//vf/8Z1RgziEuHh4cHBwVHeNB4juH37dmhoqDLUH29x7NixkSNHxsjWhocbM2bMiM55ioe1ninRhAkTYnxfIdWl3wAXIxHeunXrxo3bV6/e1P+uXYuEBUSDRweGixoEhBYtWqB0du/ePa4zEvNAn86cOTOlK1q0aK1atapWrVqqVKm+ffua66QNDHxj/PjxcnjVeRzD4NGBWIr2ceHzfQV6+X//+185Uk5O4iQPgUMMhvfq1SuuMxKv8ccff1BLQUFBcu1CFPDw1fOJEyeaNm2aKFEiyhWDHHvlypVly5YlzieffDKm4pw2bVq3bt3u3r27bNmh//3vpxQperlc/4+/ggWHFykyMmvWATlyDPrPfyZMm/bbrVvRPTVj8HDAcFED/+AD/0UEhg0bpm5oeGgQHh4eEhLCd2vw4MGhoaFXrlyJ6xwZGMR3LF++vHv37jIsDBgwIG6XxQxiE7Zz10eOHKlTpw5DaFzlB4hJs/jPRZcuXVqrVq0H9O706J+3DxDQmBYtWuiXfvmFLW8PdD3r0Mv1999/y7x5zK73/v777zHIRYcPH65byAcdOy6BiGbM+H+XjW/ffqp8+e/xfPXVSbdvezCTYfCowXBRAwMDAwMDg4Bw7dq1yNoYjwXI1cHxn4s+0GjevHlcZ8Ez4Jxff/11XOci5uHsa2KVPWa5qFzZHSNcNCQkpEiRIrZtMoMGrYN2PvHEAN3z4sXw9On74j969Ba3wSMPw0UNDAwMDAwMAsIbb7xRoUKFuM6FHYaL3m+MHDmSGo7rXHjA5cuX8+bNG6lF1AcFzr4Wn7moXCm/dOlSm/8336x3clHw6quT8H/rrTnRTNfAiVOnTm3ZsiUsLIz/Hm9DuHLlyi8WDh48qDz//PPPHTt2rF69etWqVdu2bYvN49bxcWQxMDAwMDB4FIACN336dEgU336PtzrduHFj2bJlwcHB/Ldd84PqMHfuXLelTS5ZsuT7778/evSoM4bNmzePGTOGkOfOnbM92rt37+7du0l39uzZc+bMUdbajhw5MnXqVBJFKVGrHATr1KmT3Oe83oLKMJqN3Autg9yuXbv222+/nT9/PsW0PQ0w8z5w4cIFYhg7duzhw4d1Lrpv3771GiQwjEWc6oLlQDJw584dqfwZM2Y4n5LQpk2bJCchISFUoLpAm+QWLFgwbtw457VPxLNx40ZnWagl+F5oaKhtuynVyCOi4q0TJ05EYaMsiqleIXIIhbZWPrrgeZQWSpc4cWJqWMIHqKSi5k6ePHnixIkHDhxQntSYSnfXrl1kRjn1W6aQukWLFulXQJFhdGuamxY5c+bMxYsX3ZYtn0qVKpGxd955R29ct6d63rp1q+zaJT/Es3jxYqd5wmvXri1cuFAkP8B70VT2eEWE5NChQ7QXTlWxYhyIanTaoaDU8+bNGz16NDWv8uOtrykueuvWrTVr1tC5RAKdcSLSlGLFihVyn5YNxMaAQ6JUAkLr5KJUFEVA8Mh5gFeXtWvXDi7qHMS8cdFKlcbh3779Qpv/1q0nGQ75+/VXD+nevfv3jh2nx4/fPmXKr3v32gc0A7d1z/kKC0ig/FAXpwkQM4RNHil7b1evXqV/4bNy5Ur1g3EsdvJsuKiBgYGBgUEcAO707LPP/vTTT/xIlSpVhgwZXnrppVdffRUaIwFWr15du3btQYMG9enTJ3PmzPny5YM64s//N954I2nSpI8//jg6ZYECBZ5++mkUytSpU+u2ZNEjCfbll18OHTq0RIkSPIUv4Y8ii4/YLEEfJYzLAioIaspHH31Ervi9dOlSfqDri40AmAPqpqitck4YqoDKW79+fXJCSL1o+JMryBXM4X//+x9M5tNPPxVqEWDmfeO7774rWLAg+j2ZJLbChQsrLrp///7nn38eZ968eZWBdBTuAQMGJEuWDP0swAzs2LEjV65cPXv2hOF0796d8LNmzZJH48ePhyTwyueff04ZaZfixYvjzJEjBxyJxsqdO3epUqUSJEiQNWtWuQEbHR3m8OKLLxLsww8/1MsybNiwypUrUxZU/yeeeIJsK/IGnYN+TJkyhR+9e/fmXR83QnsDRLdly5a8S34QNqFYNDS6Jj5Il1Agb9JC61P85MmTE4O0OyTcd4o0dIcOHdq3b0/lNGjQgFS6du0qj+BOUgnUzO+//05mkLc0adLAfIQkI2a8mDFjRn0BkAiRQyKhcWF05G3GjBn4wxvpL4SsUKECGaOGPdYzJZImHjFiRMeOHRHgtGnT4mzRooWebfKWP39+ckIHRKKCgoIQJOKnQX0XFjHInj07EcIqybySqBo1alB7jRs3xoeY8aGD6++SVZ4OHz6cPpIkSRLCi/bvsa+5I7go1JT4kTrkGeeQIUNUhDTlwIEDkUbqB3GqWbMmJZ00aZKe6KlTp8qUKUPlLF++nAr5z3/+Y+OiFKdu3bp0jXXr1hUqVKht27a+m9ttzexQXciP85FHLrp9+6nHHuuRMOGXmzb936rd5ct/vfzyuPr1p2/bdmrSpB2pU/fu1GmJ/tbvv18oW3bMxx//vGLFH4MGrUuTpk/NmlNOn37YLJhEB8j/mjVrYJIyLUJb85vBXN84zYiE59q1a3UuSqfGuX37dr4Od+7cYZDEGWsnrg0XNTAwMDAwiG388ssviRIl+uabb8Q5duxYNEIUblRAWZI6ffo06qZSx2ERBEBFlpWH8+fPo+JDkNCnZekDjZYATZs2lfBopWjksFlxEj5FihSER0dB1Th58iRqMeHLly+/YcOGxYsXQynRUVCm8VSn78aMGYNz1KhR4tyzZ4/o/aoURAuJwlPnoiSKDxlWPkSIT5s2bdRbvjPvG+QKaiQcz22tXhYpUkTfo7t582ac2bJl01dpUNk/+OCDwDMA2yQV5YRsZM6cWa1cQW8ID1mVxVUAncAHhqxUf2gePrA7aQ5oJDVg46Lff/89mVfLZRAJArz++uvibNiwIVxOBa5du3ZkV48FUL4MGTIQs25jDLJN0vLbh7SID7w98D26kBk4vHLCfHh35syZ4qQeMmXKRP3v3buXBkKcVq1apQLDSMkkxEznosHBwWRAVf7gwYMnTJggvxFOIcmqIB7rmd/4wOWgr26LO+XOnRsf+LAEgDTmyJGjVq1a4oT8y/TE1q1b//jjD79FrlevHuGpQ1HukcnSpUuLD/UsYYgcn5UrV4ozNDRUtz79ySef8FQdEHX2NXcEF4WyysZLwiROnBi2qQwO9+rVi4ZTa9pUL3SUV6ZPny4+N27cyJMnD/xfxUm76FyURsEpc17uf0jj9nfeecdv8eG9vKU3uoJw0fTp+86Zs4e/ceO2deiwOGXKXsWLBy9adI/Fu48+WkzIzZv/7ddNm87CuWfPv2W5eDE8U6b+n3wSqsKvX38sUaLuRYqMNAaQFC5cuCBLmjL00R3o1PicOXNGAiAq+CCTu3bt0rmoONWGXkQIJx+j2Mm24aIGjy74WsSgydxYvsrs9u3b165dU04GoNhMPRZw6tSpeH6tziNub1n2yBlEGbIHT2n/dOfHHnsMtqMCNGnSpHnz5rcjgBIpa1NqVx6KMq+o8GgbOif87rvvcubMeVtD1apVCdC/f38JILqvMCUFCCSpKH4lrLJDhw7i9Kgfo77YuGihQoVQ6/UwKEDQD4LBwAPJvA/AGaAl7777ru6Jbm07L1qxYkV8Zs+erXzgBrpq5TcDsPRSpUop58svv0wAtWlNlG9dTV+2bBk+1atXVz7oefhABpQPNFXnSDA9mMOUKVNUAEaVV155ZezYseIsXrz4U089pT4uixcvtm23Cxw0NEkrNu62DtmqqRC/0hI4F0VIEiVKBJdTUUGQbDUDNcKncuXKffr06dy5szMS+JLOReH5cFd4kTihyorZ2riowFbP7og70nv37q18hK/K2q/bWmK1saly5crhAzcLpNQyEzFx4kTl07VrV70C3RHzF4MGDXJb6gd9hIZWtbRmzRqepkyZUliEDy6qeAWQLQDClhGnZMmSNWvWTH+FSiMAA4t8T/v164dTP0OIyOlcVAR72LBhKkBwcLDf4kthR4wY4XwkXDR58q9atfqxefPZ//nPhLRp++Bs1GgmZPLeSJbx6Pjxfz+sPXuG8eLcuXvE2a7dApyHDt3z3alVawqeJOE3h48Ijh07BodUZxPc1mo/Pmo+BXkOCwsLDw+3cdGzZ8/i3LhxI53uzz//3Lp1K05ii51sGy5q8OgCFQGtSx/WowD6OR8hNBg+CTGVMd/gG9y0adN06dLxzRAfmX3/8ccfYycD9xvoW+3atUPJS5IkSSC7g2IZ6BDDhw+vVq0a2YvrvMQZNm/enDBhQpvtfoNIoXHjxvpikdtSNLNmzaqcsin3VQdCQ/9dGbCxKZsNkoYNG2bMmNH5uqjCbmvxivCQEFvG1IlE6ETr1q0Jo4ifR/341KlTOotDIXbuRQStWrXSVXPfmfeBadOmObVep+0ihhF8ypYtK84DBw4UK1ZMf8VvBv624LaINM0Ec9CVeCcXlcVYalj5yD2Z+qdh6tSpOkeSxXAfbEcYDsRMX2SOGuBvyS3ILBJFI1q149evtATORaEu8EZnVG+//bYerG7durKMrB8KVbAZ6ZHaTpUq1ZAhQ2wnZj1yUVs9uyO4qL7b1iYzo0eP1pclgQh/gLdVObmo7AXQDfzKTbyffPKJO2L5EbrrrCg5n+mDi+oT37JFWfaiT5gwweXpHvi8efOqOSyGFBpaf2qTfFKXOa/27dsHPsMuvZtqdz5y7tFF9iZM2J40ac8ECb4cMmSDHvjOnX9XONeuPVqhAr3j/02a9O+qcu7cgxMl6n737j1HfKdM+ZUw1avfswn5UQZjDhxSP0WMbOAj6/9XrlxRvNTGRd3WILlCw86dO50Hqu8TDBc1eHTRpUuX0qVLK2sTUUN4eLhMZxJVTGXMN9AkRItVXHTu3Ll80dWCwwONbdu2BQUFyYkmPm81atSI6xx5wJEjR+R0UFxnJM5w6NChwoULf//993GdkQcYskii7slAw06XLl39+vXFCXNQaqs3+GZTjAm+J8i8cVGwatUqWBY5XLBggc64AuGispdYX1EUQAPwV4Qkyly0W7duhISR6p4e7ejKxt1169bxu0ePHvqxugAzgOrWq1cvlHIikXVRtVAQOBctXry48rFxpA8++ACnj223165dq1KlistCrVq1PJrEDBzvv/++WhukievUqaMe+ZWWwLmoHHT0u6sFsaH+06RJ47Rr5fZEuj799FOpB5pV2lQQU1x0x44dLmvTtdrXXbNmTUrt0aKYE4FzUUK6I3bG+phiiBQXRfbcETsdnOvMciJ0/Pjxt27dSpQoEXRUf+qUfDQKOYkKaw3QNvWbb75p24ag4M120SefhOKfOHH3gwf/b6kTqglNbdFi7syZu774YjkBJk78h4uGh9+CuOLkhx7J+vXH8MyV65tAMvkowMlF0QyFi0Is4aUbNmwQkbZxUTlZunLlSvyRPX482OuiN2/epCRrLcCq9fGIijh48ODGjRsZBLdv3653p6tXr/7igMfZMgODeIgkSZLEGhd1R3xWFRd9mNC6devcuXPHdS78QxTTuM5F/IIyTyJgAP/qq6/iKjPxH9RPvXr1UA3REfkNsc+TJw8KgTyV42oE8BGDbzaVPXt2VEkfE9seuSiR0AfLlSsnq2eyRzdSXFRe0Rd4BXL0FEYRSOZ9QFZgBg8erHt65KIQAzzr1q3Lb7JnMyPsNwNhYWE5c+ZUSz33g4s2a9YMJzqfj/KiOFLYVKlSETJdunRqn2oUcPjwYeQtS5YsyNt77703b9489civtATORYWW6CZtPWLs2LGyEVcd0dTh8fKSJUuWPPXUU/gnTJhQtXVMcVG3tX+VmD/44IM///yTes6cOfOyZcsCKbI78lyU/u66dyusDVHgoj179uR348aNbVE1bdoUf2oP2s8P+L/+1GPX279/v5wndzksPHmEHMf1SFy9cdFlyw7hz9/YsVvF58iRy+XLf//++wtldVT26AoXxeexx3rg3L//vB7JgQMX8CxTxsOE2qMJMaLr3KN75MgRdQT0gAW4GE6oqWz754eyeOSOoKZr1qyJnaXRGNalbt++TRXoRoFx3rhxQ54yNumGhgmgThxJsW1QLxoYxHOg0xguGiOQ81FxnQv/MFzUBpS/FClS6D5QGl0vN3Di6tWrVapU6dixY4cOHaBq+iePjym0IXny5E6r+soMiW82hRaL03nd36xZs8SmokcuKgq6ugwjClyUDIsKa5tTFzOwitpFmYv27duXkG+99ZYz2zZVmGLmyJEjQYIEM2bMEEaqw3cGTp8+Df2rVq2aCnA/uKgcpIRd2/KG+ig7Ubdu/VdNP3v2rBih8WiqNHA0atSISL799tuCBQvqpjX9SkvgXBRaSMguXbrY/Hfs2IH8yG9qhmpBVAoVKuRc5XY7SJeqB1i0LIzDqEVLjkEuClq2bAkXff/99wcMGKAmhgJBZLkoKi6/X3jhBVs8jAliXSkKXHTu3Ln8fvrpp21xytFfiCg1FhQUxG/91LFN8n///Xexm+22Fm9TpkzJU9Vw3iDVq44f3/vIMxf9+ecDwkWnTft32qJ06dEpU/ZS23R1LgqKFh2lb9kVrFt3FM/WrR+SA0rRx5kzZ4RkKR+xl4swM6Y5eZYQzlu3bslvJVrXr18Xn2juHAwQMaxLyanZdevWUTDGL6HjcpUqwq3uq6E/INk41a5C2aYMIz+nIcCtEQaxAD4ADHN79+69ePHi5MmT+YIi33oAOoB8TmjHgQMHqiutGPLGjx//5ZdfTpkyxXlLFZIwb948nqKH2QY7HoWGhuKJJAwbNkyZnnP/M4T9TAZGjBih39LrtgxVDxkyhNQXLVqkT8p680fzCwkJkXkgRv+pERA7QKQrTjXDFB4eThnJ7YQJE2wKos5FiVNFJZYeCSxOj1eBBQjGCHTQ7t27L1682MZFxVSatAjfJJW6qlJexKnPgqMWEEm/fv02bLjntIa3dkQ35Ss+ePBgUnFecOcttkgBbYNMomGg9Ej+5WIDqp0PPN9LxK9///7qtgOygSSQ6KBBg/SRV7B9+3a5gIFKoCA0mZTl2rVr1EOPHj0Cn/D2CMVFEcKRI0eSjUOHDsmjJUuWSP7lujzqRJz6vrLjx4+jDrotFRMyQMWKjsugFxYWhtZOr7ENgJSR4iP5tosc6ZJ0HwZYoho9ejQ58W1pU+pZcOXKFd0pOaSi9Pr31hP37dunrrhAFJMlS0YvkBcZ/MWURbFixXBSISp1b6JCNY4bN85tXfiB9oZ+GanL/R5E0GRQHeednwpifeeVV17RexwyoDbC+WZTYqsme/bsukqNdKl9vx65aL58+XQuKqcu1cZaWa217b+1cVFQv359fCCNerA6derkypVLNWuUuSgDMiGTJk2qf1Ag83g6N42LddwUKVI4Z+58Z0BOpepcVMyiHjlyRJwxwkXpfTgTJUpEPasw9DVokvzW7dAwIOTMmTN//vziZCijM0Z2yp4voFSIMCIFv9IipxIC6ZXkipCJEyfW13sZ8Ro0aCDskYIg2zKS8E1MmDBhxowZbR3BRrr++9//6gFkPVlsPcgCo21jatS4KBRUHcaOLCLLRdEKkECcDOkqAIpW48aNRW3w2Nd8c1FoAxKCUx9d0cb5pKopDNmvq9vRlckj2lecc+bM0bfaypFmNf/lDbLDmWZyPho4cJ1HLtq27QKxaXTy5D+f5jNnruFMnbr3rVv/Dncff/wzPuPH/7sRYMSITThfeWWiHsmQIRsSJer+22/RsvrxMAER0lklX3NFKem8JzXI3l0kh4FUbsdVx0rdEfe+gChcaBwFxDAXlTOyyl6TUFP5qgnbVFbshJoC2Yj766+/8luZpTaIV0BZEXPwjKoFChQoU6aMnCXo1q2b2xox+TDwNUUXGTBgQObMmdWIzOhfvnx5PreEadeuXZo0aXSDgXxEX3rppZ49e/LxE5OSpEIkqKFopWgtLusugXLlyiVIkEDWyuhXfM94ymeMsTUoKEhpw6iwuXPn3rlzJ3pwly5dqlat6sNfdg+SH5d1VZfbogSSoq6ZwWALFy4sjIKhFgULyorSUKRIEUZ8nTzrXHT//v3p06cnKv2rxlBO1UX54mBGjUKFCvGF4OsL33jiiScUF6VKRX2UryydCJ0PJ42iBhEyT5Mpy/IdO3aE7TD0UAmEFL3HRzt++umnNWvWpJlICw0DLZAaUEqYx9iiANjjzJkzSRe9ZKaFXbt20WTywabsYoBB0oX4vfDCC1A4hlRaJGvWrHySRVmhIA0bNnRZZhthRK+//nqLFi1Qd/iBMPC/bdu2JUuWdEXP2pNwUeqnbNmyTZs2TZ48OeIkyvGFCxfEtqGIFnIOsVQLGnwPKBT1TLl4vVatWuQHyUcJZvRv1aoVua1duzbhlWUgRLdevXo0ATEzhFI/9Bd5NHToUNRKWW6iNzVq1IhOQQAfRm4RQrnpTpQwNNq33npLNmIpRTM4OBhx5evlsSdCWSFIeKLWSHhqkl6GYEjDkbpsj0QLx6lov0dRIT9yjA01iwYl5tdee81l2diMcus8EKASEEtoHj135MiR1NiCBQv0A4FyEF2qsUePHoRBpFW/o3cnSZIEQVIHYcSebaZMmcR55coVuaQRLROlnJEN6UIylf1nsT2r2/kEcuko8iYXOYqBmRIlSjCM0+mQEEYABhMo2d69e4Vs0E8Jw5CoIkGSyQZ9WS2/ILf0EcW4/GbeN2SIK1iwIIoUvQMBE8NClSpVUlezChjqs2XLRk70NcBAMvDzz+jBLsL89NNPjJyfffaZXAEyadIkkWchq/oqpXAwZS1J1UyePHmUz4gRI1z3Luo2b97cZd38yaeNtvjggw8YgZVJoaJFi+qzZnxllLovgxi9MrKb6GSmwLaH1q+0iFFZujMd1rmMaYMsxKVMmfLNN9/kg/X5558zeqsPEOxL3/Ypcsj4ps++SWaU/JAl0TcEDB3PPfec/OY7K30E4eQDLZN6znqmB7ms+2CVz7vvvosP3Uqc0t0Yf6Dlw4YNY+jjo0MLBlCj/+C9995zabcfuSPoPZKjfCRXyhKY7BSQ+QuUDfQrPqx8LOSpx76WJUsWwqt5T3eEHd3ly5eLc9GiRbxVoUIFdcaNsvCWGljQJRh2XNaxYXQbxmo534snIalwuKi+GEuf5ROj7k/yAfojMun0l5tagoK+unr13ywdP36lY8clclh0woR/qeb167dw4sknYt++88OGbXz++e9wQlmXLj0IQb179+8XXxybIMGX6iaYS5f+ypNnSLduy/3m7ZGC8KnVq1fTx+VCF48b+23nRRnwhZQRmK4qvwOX/2gihrmoFFvNq4mNYAZoxkrZoKvUd9uK8IYNG1BQ9u3bh5YDd4W4mkXReAUZVdG5RVtF3ZcxUSYX0FkZyFKlSsVXAc2brzVjHDoBX3r9Yi7UbnzUfAQfJJyKnqHj6vcZiKEClHKGVISHEdZtnRRSIzWJMkTC+uRqExR6ZYkB4VGfOm/+7ohjLWrZU2zQ6TuL4Mny0SUP6AfquxgWFqYr4m7HHt3u3RlSXbLwJeATGGVDL1evXkVD0qdv5eJyNdMvE8NqxpcPFc2hb/6hY/KllN/wSd2eoZwJkUrw2I7yhZZdQ4AKdGmGH33EFjUgBra1EbmbTjRmWdmmHalt/VIHWV5Qh+uoMZdld0GZQJQzZmRV+DkBIE7R2UEqXBQqKE6Z8B44cKA4ZW5F1YOc0tHVVpR7l3adANUo6pTSQdH8aAjJrcib2v5EKdA2FG+Ue+3QeEQlFWuQuuw5IQKjTLmgpqAK0x1UAGRJiavHnihz9noXIPP6ZYzSBHoN+xYV2Dgtoq4SEetcfBF8lOJBB0qhLGLooAPqt0pAhGTiSTR76KuIBH1ceqLMOv1qQTi8y7q3Q+zB8CUVVVXYDvUv8zV//vnnF198IZNxjLr6Wjrfa/FndGWIhsIJB0M9lY+1HAxDAmHFiByjhDpX9v7776vh/fTp08gM70IbOnbsWLlyZbXNMsDM+wDCT+p8PgjP2IsyTY+jokjIeSEefd9m8DmQDFA04eEuyxDu7t27ISeS3NSpUxFmvgjSKHRMCBujMUOu1HPXrl3FgoisQbksG1T0ncGDB8vMDl2bupWpK2r4f//7H8IvIcmGWnp1W0wDFZ/A06dPJ6sNGzZUHV/4HrDtD/ILMs/44/T3Ji2CkJAQ4TCQbb9XiNH90RakgVzaHZt8YuDSLmvmS+bL+C+nGaXsfFmQQGGJLmtdWj5zHTp0gNK3b98eMoxEIY1qAYceweAjbcG4R9LOekZKZV03a9asQj7VEdxnnnlGlgHJiWxUtoFBzPcyiaSYLl06AhcoUEAmcOF12bJlc1mzG4y0f/31F6qLTKeitPCloB2RMb5rYrTWZZlNUnPrAr2v0UMpvoSsUqUKHwXK1blzZ1pKRJQvtby1efNmiDpNzEiC8L/++uvqsyJAMvnISlT8YBCmZZFVVCDKwleJukJbmzx58oABA/gSyZjvF4go8egT7pDGNm3mw0JlL26aNH1y5x7M/wwZ+pUqNfq99+bbLmgZOHCdGCjKnn3gjz/uhZEmSfLPGdEPP1wkX7ebN+907vxzlixfv/PO3C+/XFGlyvgpU3615+ORBz0CPqm24PKh8SjANi6KWiVTHgoEsE3h3T/EMBeVAii5l0tXAeXhC8EPpRpSbHkke3FV4WWZ2BuPN4grOA8oyj0i6hvP8Gozzla0aFF1j7ZghXVAQhkqqFSpkq68yrCrZu8Yyl33HiPhC+2yNrSMioBocjIjyNcrKChIzbsr+fHm747YoqO0YbrrExbUciIfXenDjNEUUKUrBjD5Qqj9UTYuiuRTNCpEzVgXLlxY7XeNLPiiMMTrZsBszSH76PTdRw0aNHBpZzz4kqmCox02b95clUUUGjXl7GxHmU6WLUBuawOPy1ocCCS2KMDJRYVr6fvx5FSMzWSfqBFKE7W1CNqA616L83z40UKinE/beVE524OuIE6baMkmRp2LipKq2lQ2OLVu3VoFQBHER+b14AD0DjWtI8qcUljl4gHV1ps2bXJpFmI84tq1a+hhamHBbVkcpZsoEYVdqFMizp7ojtjQGCku6ltUaIvHH39cBUZFc1nGNnyU4kEHSkDbtm2PHTuGnKDtoWT/8MMP3bt3R122HVSjreFCUVYLGI7o/vp1xL5B25E3ldzNmzf37dunL76hsgR42QPvEtV9uokXISRyEdQzZ854m78uWbIktRe1JNBY9LY4fPhwlPe2+AYfGsri5HjCPKltRjYbo3BbAwtMNfCWFfDV1pfvbPAhLSdOnIjU7aY0EFH52IUeOKQeiHDnzp36qqCA2oPqR9PaJVwUhoyoo7sz8vB94bsPaYTU+d2hGh0gt8gnFetxfTvwvmYDnQ6J8lEnkFuZxSBd/fOKVoMPWhBPZUNZgCny1muvvea8USZSOH36KhRUOS9cCD92zD56kBBhZGevgTfQWeh6dORI7Zug9c9biOXb3WOSi1JgRS/Fh77tjYvqgSkzmu6WLVtEE5Kjt8DcpR5/4OSisvtI3eINh9HPCzECJkqUyHbsHk+XdixBliWVSg3JhHGpSV/RgNXCkdvaB4gPStuKeyG6guwBI0DDhg31fW7e/N0OwuCOWM+Uc5VhYWHqCAraf968eVc4oLqr03aRUGupMZKwXT8dKUB7YMi6j18uKitpciaEwYgYxF9ute7du7etIIrJ2NrRHbGGppaj165dq0iC39iiAG9cVP8ei+2KFfcan5TDb2o1z9YiYt9C56KQH30dPrKwcVE5GKb2T0aWiwqV1bmoMEzbxYPLly+n7LKLUi0L2LgoAu+KOJIEEOaZGhTblB1lslhBKrJoILUHm23Tpo1K1NkT3ZHnon5FxcZFH2LrXIIDBw6kS5fOqVW7rdkffWXMIDrYuHFjlSpV4joX9wsrV670eELPB/jC5smTJ7L09aEHbBbO6dEM7KpVq9Tnz8A34DCFCxeOkdkHg0cKMbwuumbNGtQLNcUiFoRRi/m9c+dOXfOAnYou4nHGVIwLR2oGzuC+wqkawg1cmvVwG4dBBngKf7PFg/afNm1a+R0aGpogQQKl9VaqVEktK7k9acCyEqtUcCc2b94sB+FSpEgxefJkv/5OLgpnSJw4sSjQb7/9tkoLym1jgzY4uSjaJGz8xRdfdFuXyKnjHFFAtmzZbMeo/HJRt7USS6PcuHGD7+uYMWPEU/ayerxRUODkojRlxowZn3vuOZkmQFGGdciCsN/YooBAuKjwKP3ssds64ujS9p0GwkV18hNZxA4XVQPmr7/+yiszZsxwRxjJCJCLUsbHNKhdr9J2Mlvx7rvvLlu2DDpavnx5t7WKrrZTumOIi/oVlUeNi8oubrXdQOHo0aPt2rWLkyw9TGC83b59+8WLFxkEbLa+HhrQZxGVAJetGEDgVPRKXtFPMBoIFi5c6LrXzpCAgY4ac65IG3gDH6Y6dercp+0DBg8rYpiLyn01yuj5yZMnV1hmdd2W0cUV2tZk9Fq1snT37l3GU91YE19oHnmcMzaIEzhVQ1oHH3W0yclh4JxJkya1LfTjKfqugA8ALKtp06adO3cePHiwLgNODXjSpEmue20DCES9lgWfmzdvDhgwIFmyZLBcWYT35u/2xEXd1u5WwuzatUst+bojjBzYNnr9/fffKiqPd7rIMRjk//nnn4/OHU1i9V7f4hsIFx05ciSecO8aNWqoWXCxz+G8FUBRFGc7uq22zpUr12uvvfb555+jQ6sNC35jiwIC4aKICj5ffvmlHkx24So7Hw8TF92wYQPFCQkJkUeR4qI+AHvMmDEjw7XsXxDLt7/88kvFihX1YDHCRf2KyqPGRemzCRMmTJEiRcuWLUeMGDFu3Dj04MaNGzPUGDUumkCGXRFo1KhRXGfnfiHwuxZQscQCHGCAfegtVEcBDNFicbB27dqDBg0aP348XxkxNuH3olQDG/imfPjhh9HcMm3wSCGGuagQTpQh0bzFFpMYYpKdt3KPjdua/RWaSkgxt7t69WqhIgyUK1euXKGdOzWIczhVQzTjxIkTK4XYyWGEiclKjoAGdWnmXtBW0cO87cR2asCyK1i3COe2NimNHTvWbW3RVJ7CzcR8izd/txcuKrtb8+XLpx8REV4H/dAnofv27avYqUcuunPnTt7KnTu37eqzyEI2Mw8fPlz5SHMoQy8euSjVmypVKlR8fZmF7obGjxKsrxWcPHlSGe73yEWpKI/nt/3GFgUEwkXhXYkSJSpQoIAeDL0he/bsSj+LWy7apUsXnOqU8oEDB3A2aNBAhY8UF5WupIRNrM5Gn4vKSnKJEiXk5K0UgfofPXq0HixALlqqVCn9hgyGcT2AX1F51Lio29pGBDnPkycPBX/xxRcRYKfdHYMogFGavsZo0KZNm1g+9RRv0atXL8bVatWq+b7w6VHG4cOHGVoLFiyYIUOG4sWLN2vWzDboGRgY3CfEMBe9cuWK0MhfLMjKp8zywjPlxlVUfziqBJNduGgtEAChpqjvYox306ZNxpRu/IGohmoVlA88qqe6WAJAe3TL9W5L0UyXLh2arpqFRUEvWbKkWvxE98qfPz8UC04VGhq6YcMGuT1FIDtylY0cgRg2hCiSH16B47322mvCD19//XUkR4LxuSWYXObpzR+IVTrn7tnChQtnzJhRn9WjCGLNskqVKuPHj1+0aBEfKmV2hRIlSJCgWLFiznoTG0LRXOEX6kUN//TTT2JmQKz5v/3223IDZEhIiMuTxSApoE3BFcNLadKkoTkgBpC0smXLqr0MznacMWNGihQpIN4zZ84kAyjQ+uZ537FFAdQ8YqP7yA3vtrO+YtyVLInz7NmzsGilOjB0QHv0FpFVU7VX2W3ZLqKwUc6nHNpUC85ya1+TJk3EKfc9IC2IHPVPQyAhefPmVYqgmB5VJxTEdhGcU8Uvtotkr6xw0VatWp06dYqYixYtKkRXFhXlRhY1WbBq1SqXZQvUbxH+/PNPWla3sAXBTpkypbroXOCxJ9JVXZZ5TOUjzcTwfuHCBbk4muql15w7d44a4L9vUcmZM6fave+OsJhlM09lYGBgYGBg8JAhhrmo2zojKsRyhXWbi26D7vr162gqymqFbpqPt+SsqQBVxmwjiVcQLlq7dm3U608++QSdVd1jDh2SlRlZjdmyZYt6C9JC+DJlynz99deo4++9956+rWj69OnKmrmCLOKNGzfuqaeeclkW0r/77jtFC9GeGzduLJbi+U+ESm9u2LBhkSJF0HeJFoKqzg169IcDjBgxIlOmTC7rSjqbuc6RI0c6zZDu379fGCBAaVYXbFBeoQ3kp0+fPjYaNmvWLJsBp6hh6dKlcoFe6tSpq1Wr1r1792zZsnXs2HHnzp2QE8kY2rxtRWv37t1Uvi0qOh35DAoKkrLQQLLT2Fs7koTz5oly5coJj/IWWxRAinJhvYgBhB+m99VXX4mQ1KhRw3YdKC1InSBXiCJESJky+v333yUe6N/gwYMvX77Mi4ULF8YHSeA3ZEmMVLmsuxZsLNcvbt261a9fvyRJkvB68+bNGcfIuVw4jmCIlYs7d+4IN5O1wdOnTydNmrRq1apjx46l3pBGucKhTZs2VBfDnaz9wtOQPaT922+/FeGsVasWT+GZ4oSoEz/jKkybOp83b97kyZPl7t/q1asTEk4rC7aIh+16AI+A3+rmOqZOnapbLXJ76YnQXVi3y7rfgqqQDSwLFy5MZIE6kemhzz77TOpkwIB/bjn3JiqMCXLdKKDhqKsFCxaIyMF1nScqDQwMDAwMDB4axDwXdVuLEpcuXULhc56qRx2BPMA81WUYCmhvvIVaE1kbxAaxALVlDjaIrh+pBgoPD0fp1M+CCmbOnAmdILY1a9YsXrw4JCQkODgYWuVX+yTCPXv22DZfiZYM8YCA6RMZ3vx9gJi9XUKAVJNhZ1m8oVu3bnLbWIzg6NGjsnRMTwlw18CZM2c8+lMESFQgxuLhoh999BEce8OGDT///POcOXPgJ2+88YZu5iHw2GIcR44c0ZfT4xWoNDUZF83KQSb1fgdhs61eRg3Isy7MjNh+bw70AYTNdrDi0KFDtk4Xh6JiYGBgYGBgEN9wX7iowcOHGD++tWTJkty5czv9YW4PzaGpGzduFCtW7IE+wQ+Vypgxo3OPMSxLrQwbGBgYGBgYGBgYRAGGixoEBOGitk2S0UHLli2TJUumb+h1Wxc/dOrU6UFfFd+5c+dnn302a9asRo0aPeiEbfLkybT7yJEjdU8I6ocffmhMixkYGBgYGBgYGEQHhosaBIQWLVrASbp37x5TEW7bti1z5szEWbRo0Vq1alWtWrVUqVJ9+/Z9CMwe9uzZUw6/VapUKfDdvPETly5dKl26NGXJlStX9erVa9SoQTO1adPm5MmTcZ01AwMDAwMDAwODBxuGixr4xw8//PBFBIYNGxYjB9Xc1rHPkJCQXr16DR48ODQ01NsRzQcO1M/o0aO///77B3p3rsLff/+9fPnyAQMG9OnTZ+7cudGxkWtgYGBgYGBgYGCgYLiogYGBgYHBI4GLF8MnT/6V//cj8sOHL/34496NG4/fuGE3Wyi4du3m2rVHZ8/effCg52ulw8NvrVt3dMGCfceO+Z+a3LnzzOrVR6KV43+mDm/a/u7c+dcs3PXrt2yPbt16sPe5RBl//HFp4sQd9yNmavu3387Mnbtn166z3o7nxDexuXv3byUSf/3lQdTJjy42N28+omJjYBAgDBc1MDAwMDB4yIH+Xbv21IQJv3S5/t/vv0fdWrJHnDz55yuvTCRm+XviiQELF9rvdpo69bfcuQf37BkGqylVavT77y+0cY9x47alStVbRdKs2ewrV+z29hUuXfore/aBb7wxIzrZhiT06bO6SJGRKtvdui0/ceJPeTp69JYqVcbLo+TJv/roo8Xbtp3yHeHDBxqrePFgqZwYj3zjxuNPPz1Etfjzz3+3d+85W5h4KDanTl3t1GmJJJo6de99++yG3KdN+61OnamSn7ffnhMWdthjPAYGBgLDRQ0MDAwMDOIj1BpdjODu3b+zZPk6xrnotWs3n3lmaOvWP44fv71fvzX58w8jiSRJeuzYcVqFmT9/H57QBnGeOXMtffq+7dsvVAGCgzcTyZAhG77/fuu7784Tztyw4UxviUInCBBNUiHYteus0IbJk3+1PYKswkJ5BBGNfkKxhpgVmz17zt0PLop4PP54/y++WD5hwvbPPluaNm0fUsmTZwjipMLEZ7FZv/6YiA0Cf/Wq/TwOfY2M1a49NfoJGRg89DBc1MDAwMDAIN5h584zX3+9NmbjLFduTIxz0c8/Xzpq1P9dCn3jxu2yZf9J5c03Z4kP1OjJJwfxp78F/SCMrDReuvTXc88F68tZQkL487gtE/bSosXcmCIVFy+GS1rLl9svrwI5cgziUf/+a6KfUOxg7NitMbsQd/v23fvBRStXHr916//ZwDt69LLQUVil+MRzsfnrr9tElShRd/7XrTvNucG4Xr1pPXuGRT8hA4OHHoaLGhgYGBgYxC9cvvxX3rxDv/hiecxGez+4KDq3zWfJkgOkUrjwCHHOnbsHZ/Pms51hWracx+/x47cTxhZJmTLfEWDWrN02/z/+uASN4X9MkQoojRCYFSv+cD6FC/EoxicF7hNgd0mT9vRYkCjjfnDRI0cuO5eaP/00lITef//fZc94LjZw0cce6zFkyAYRnl69VtkCtGr148iRm6KfkIFBZHHq1KktW7aEhYXx//jx484AV65c+cXCwYMHlefVq1e3b9++evXq9evX79279/Ztz8f+7wcMFzUwiF+4fPlybCZ369at8PAYM2QSH4wh+87DxYuerV/EFPw2H8M9de7xEd+PaN5pdOFCDJ8DNLjfOHjw4uTJv06cuOPAgf9rO9hRpUrjUHDfeWfu+vXHfvvtTOAR3rlzd9myQ8HBm2fM2Hn0qF0aY5yL/v33385UYBqk8sIL34uzTZv5OEeMuEcvh2zjmTJlL7e1JuZcVnr77TkEWLr0oO5J6apWnbBv3/ljx644ScWNGzfmzp0b2T4eNS4K6/vhh238/frradsjiiNRnT9/ffr0nVOn/mbbw0lhw8IOjx27lZY6c+ZaFExJeRSbXbvOZss2UKoasaEVAo/Qh9jcDy765583nKWGW5JQly7LxBnPxUa4KD9gy8SZIMGXixf/rgdo3fpHfb+AwIfYnDt3XYwq0Xbjxm2jisSfH1Bu6mHRov0UX4XfvPkEIeWPphdP6kR89NaPjqz6yIBg584z5Hb+/H8MR50+fTXAF2m4VasOi6QdOnSRGHDevftvaxIV4h0SskuZhjp16qoqLH+yGE4kyke9awD5XGFh1apV8uPw4Xs2SlBvmzdvlke//vrvwQQ0k5UrV8pb8gMeG2t01HBRg4ccAwYMqFy58ssWunfvfv78eTrhe++9Jz41a9bs06ePugV0/Pjx+ODfvHnz/fvttjfuK44dO9ajR49y5cqlT58+dlKcP39+kyZN0qZNy6ATzahOnz5N3ZYsWbJixYoxkLMogUYcPnx4tWrVkiRJ4i0MTZ8wYcKOHTvGeOpHjx794osvSpUqRSX4CIbSkylTphIlStj8Fy9e3K5du3feeYfMt23bNmp5GDQIpdn1448/Ru11g1jGzZt3OnRY3L79wpEjNzVoMANdtmvXf7XwhQv3v/rqJBTcChXGfvHF8m+/3RJgnDt2nM6V65uePcOgr927r0yatKdtgeh+rIs6sXHjcVLp1u3fRV0xfjNt2m+2YLK/ERXcYyTVqk1Mnvwrm2ZM0US/90gq6IN0AcbwSOU2slwUrfrll8fVrz9927ZTkybtSJ26d6dOS+TRTz/9Xr7895KxKVN+zZFjUPbs/5DDggWHh4f/OwNFu1eqNI623r//PNo2r0P/As+tD7FB6SchWUtEbJYsORBgnL7F5j7t0XWiX781+k7peC42ioveuHG7ZMlviTZt2j761ICNi/oQm3nz9tapMzVJkh5NmoQMH75RpJGG4BGULHPmr2fO3PXLLyd5F4navftf2klFpU/fl5D4q3Rhg40azSxUaMQff1zynWggsuo7A25rf37dutOIfN26oyTatu0Cvy8iwLwlaVFwJLlAgeFiwqpGjck0XOPGIfjIsfOXXvpBYrtwIbxly3nC+cm55BBOtXLlH/gMGrTOmxHmRw13795ds2YNSh06idua4OZ3WFiYzipPnDiB59q1a3UuumPHDpz8pyZv3bq1ceNGnEeORNdQeYAwXNTg4cfHH3/Ml0bneNeuXXvyySfxdNISFPqcOXMSIHbz+M/6JN0+VapUqVOnjp0UoeV16tShEqLPRRnmVq1aRVQVKlSIiaxFEVRg9uzZyYa3AIcOHSpcuPD3338f40nTfFu3biXp4sWL+wjGd6Jy5cqtWrXSPbdt2xYUFCSr0zyqUaNG1PIwd+7cggUL/vLLL1F73SCWgUKmHyeTvYWobuJEi8UZ2T26xYqNQhFXThQ+1EFdS4sdLvrllyvIhrpgQxbrbKtGIF26fzRpVFVnDKikKVL0+vDDRbrnpk3Ha9WaIr89koqpU6cmTZq0a9eukcqt4qLjx2/fs+ec7S9r1gE2LvrRR4vx2bz5hDibNp2Fk5DinDPnn52ljz/ev2/f1XfvUvd/wxjxGTPm344ZHLyZp6pRBg9eP2HC9sBz61tsxDZPZPfo+habWOOiFSv+ULToKJVuPBcbxUUlWtpU9qVfv/4vkbNxUR9ic/78ddmfDAEbO3brzp1n3nxzFlQTAgbxfvXVSfIKhNOW+f79/2HvkDc9Y9Da2bN3+03UHYCs+s7A3r3/GLVS1HT79lPvvDM3kBfd1sZ+fF58caws1d65c7d06dHio2ye0Wr4wDbFCf/MkKEfPvv3/5/hYgIXKTLSZ0M9Wrhw4QIa3cqVK1E23BZdX716NT5nzvy7uQZdBR84565du3QuaguGsoRz82b7wv59Qsxz0Zs3b1LCtRZ27typbzmjUg4ePAjbRm3dvn37pUuX9Bf//PNPKoXqWLdu3e7du71tYzOIK4SEhNBq8S2qQHD58uXkyZPDE/bt+//snQd4FUUXhkMHIfSmdBApgogFRUGkCRZQfwFBLIAIAhZQUanSQm+hi/TeDb1X6T30oHRCDR1CQnH/N/fAOOy92VsSEsp+T548O7NzZ6ecmTnflDMhyrNfv374lChRwhT4hx9+6NKlS5ylzYTnn38+zrioETVb3NFnLkpL79Spk+6TMGHCuOeiJlkqV66cBRe936DurLmoSzRo0CBPnjwmzzhuI17BW6XNhjNQB9HVDhw4j6IvfwEBq1Cz3n77jvbmGxctVWr4yy8PVc5y5aI2+uq74+KAi6IywiICA9crnzRpomzSrF5tnmKXJcd581zsQOnff0OOHL3VNkXDYa2XxKtNgC5JheHQtLxNsOKicLBnnuln+pNVOJ2Ltm69NG3aLseP32HaMEMCqIOL27adxFmx4hgVfvLkXfgogvTDDwsSJGiH4i5OeIhikm7hVmx846LWYhM3XBRSkSRJh82bQ5XPAy42Ohc1HHcmJU7cXo/cxEWtxWbBgr9xwsb1T5w5E2U3uHnzRconYcJ20HXlvHQpInXqziTj5Mk7GaTWaH3qItwYyqp1AsRSFGWu3g4ZssnDlNMK+K1+aS1J9bvXSFi/flFncXv3Xqt82rVbjs+33/431/Dzz4v69Fln2LiLY8eOodGtW/dfmWzcuBGfQ4cOiXPfvn0rV64MDw/Xuajj1MBKnGFhYXo8kLW4SXYsK203b96kCISUS8ZwRkTc6Rd27typb2ImgNqgf+nSJfFU+5vXr1+vdk7aiHcgvv7+/rEyRxKLUXmOunXrQlF++eUX5YPIpUiRAs9du+7ZHwUbpBHGZdp0wGQeFi4Kg3rnnXd0n7jnos6y9DByUX6SN29e3Sde2oiHmDhxYsqUKeM7FQ89UNogJO+8M870V6fOnxLANy76rwNGlG59C4YjNmCVJmrECRdt2XKJsqArEPKwaJF5y6iscsgZOR0ostBCxdYE9evP1A3VREcqfIAP50XVpSlr1hx9440RBBg37o5WLfr9W2/9p9/Pn/+3n2aDRzR4f//O0HVvL19xKza+cVFrsYkDLsrXX399uFqOEzzgYmPiomDQoI0iSCItzudFLcRm8eIDOD/55J4VTv0nSCmsz89x7Y0eADKGZ4sWS8Q5fPjW77+f7zIGH2TVOgEwfLnxqEmTubz1KuXOXJRCMzW0kSO34fPLL4uVT1jYNb7Inxw2RmyIk3o3bNwFnBONDv6pfDZv3ozP339H7S9A71W81LQuKpR1796oxkLBbtmyRbiYrK/eb8Sy0iZMeu3atTdu3ICXSt7ETNOVK1eEo168GHXcnAzjVNvJtm7dihMNDP55/fp1GOzq1attOxwPCEJCQtCVUfEDAgLQREND78xchoeHT5o0qV27dmPGjFEmW6jHiXex3QF5FsITXVT3G8uWLeOjWbNm1Sc4ChQogGezZs2Uz7Zt28qXL6//cNGiRSR14MCBurUxD0ErmD59eocOHfr06RMcHKy/QshHjhzZpUuXyZMn016Uv85F9ZL08PAq7Uj9hE5Hd8pXLl++LM5//oka4BUXpa1NmDCBpK5ZYzbRQR398ccf7du3nzVrluqVWrduzQ/h7US1cOGd8yeKi27YsKFbt24UGq1ej8qlwBiOjm/x4sX0CWfPnu3fvz+9hCeZdSlLiotSX4MGDSIZBw8eNP2KStF95syZQ0WMGDGCbseHPoeOvkePHn379j19+rSJi+7atWvJkiWRkZGULdUtnuSR8pRnqSDEMnPmzKpefG4jshtHr8HoxMxDOJfM7NmzkydPnjRpUkmtHEEh41Sr4ZDYXr16kX55K/V49epVJYSIn55aGlenTp0ovZ07zUfCHnk0bjwHNUtZ5nCGb1zUcCyVBASsQjtcu/aoLHCpvbLG/eeiMIfKlcdGRt4zjyzH0pxX/2QdST9iZziYDzEsWHDPzsx58/aXLDkMJUr9TZmyS46T8RzDK0x84KK3b/8rF4SQKepI16o90e9lQyZ/RYsOopo8T6pbsfGNixqWYhMHXLR166XOov6Ai40zFwVffhl1pjFhwnZLlhxw5qIWYhMdFzUcdqq++24eRXTw4Hlizpu3r/725MkrJCNduq5yLyt1p9/ra/1RT2TVOgHw/OTJ0SJ+y5ixG9TR85R7zkUJqcf5zTdz8ezcOWq9btWqwx98YN/geg+cuaiwSrgoYy7qyvr160WRM3HREydOCPnctGmTrCkK4uYgbixzUeHfai1YqCmKqRG1X/wfntH15ZVQU4CihoYqNNXel/tgArl87733UI7R7KdOnXryZNS8I+SqWrVqc+fOnT9/ftGiRXPlyiUTKtRmkyZNZPsrxA9ttVChQm3atBE11GVUcQCak5wkRJkWH2Q1W7Zs+GTMmFEJXtOmTaFJ8kyCq1evPmrUKCSzRo0aKVKkMHEYa9Cw4bqo2teuXUNTT5w48Z9/3pm6pogoMbJP+aDuE7P6lc5FIRJPPfXUDz/8cOqU2fZddIDgFSxYkEwJ84EGfPHFFzjr1q2rjOUOGTKEGiFVxl0uGhgY+Morr3z66ac5c+ZMkCDBvHn/bYCBRDVo0AAmP3bs2LRp05YtW5YfwnJxytlIcrF06R3LGcJFv/3227feeqtq1aoEePXVV1VU0QkMJZw7d24CDx48+LXXXiMBpkXC6OBSloSLkrySJUvWrl37iSeeSJMmjRQgZKxSpUq8JXkqki+//JISJlP79u3LkSOHV4SN6iOzH3/8Mb083TpZppaFi65cuZKi4FvffPPNJ598kipVKp7pCSlMwsDlJIbt27eT8ixZsiCEUx2AQvvWRqgpmVtRO8wtxMwTuCyZWbNm5cmTJ1myZJLa/fv3f/bZZ4kSJXruued69uxJRkgALQjaqZczbeHFF1/ER2pcfCpUqDBw4EAGC7LJq65du3qVvIcdn34adXDLwkCub1wU9TpXrj4TJ97h9nHMRXfvPlOlygR1Xk5BDq2ZLDBduRKJZ4YM3Uy6TqNGc/7803xRh+wtjO7PmRJ4BW+56JEjF6FJ6MSy8iNp81a/X7jwH1Rz4S3OSnx0cCs2vnFRa7G531x03LjgH39c6Oz/gIuNSy4aGXlLTvCSwkqVxupc1FpsouOiAwduRAKVmVxnLgrq1Yu6NLVfv/UnTlx+8cXf9Vcxl1W3Cdi/PwxuL0UK4/Xwhz5z0cOHLyRK1D5r1h4UdcOGs2fO3GfY0CBGdJ336B45cuTs2bPCwv5xQKwTQU3Fyi4N6uDBg2JBd/Xq1Xv27BH7RnGT7FjmonL4VSlPZ86cEZJJJmWDrtJF0P6Fi164cAFNUfKMjkv+CXn06FHbKNYDBbRS9EW1aTAyMhLtU9mJRvPWVU90X0gIOjfVDfeoU6eORVRxhubNm/Pd999/X5yNGzeGBeXPnx/PadOiBgBoM3q2Wsr76quvRo8eLc9o5ClTpkyfPr3nNo3at29PzGryBbr1+uuvy/OUKVPSpUunQlI+StoVF4VI1KpVKygoyPASw4cPF3opTjom2B08UwWAqyjjPcJF+ZCc66Ynwqls59BbFStWTK0kS46E6lBKPDvv0aWIIK7i/Pzzzwkjex+sBebXX3+VqiEYzV8nw9ZwliXhov369RMnnBxnr169xAnT079LB4VTLVkjD15tV4ZEITCqfEJDQ3XbRQsXLsSJgFEFfAhZko1wEH7FRQVwbzyt8+UJpOoVF7UQM7ewKBkyCMNXIWka1Lu/v//ixYsjIiLGjRsXFhaGp4nz05oUFyUZ5cuXHzBggLxiLICKZ8iQwavMPuyQBQp1fYVCcPApsSziAxc9deqKv3/nypXHKp+45KIHDpx///2J+lE9w3F6zXAslvLRL7+cqb9atoze5rePP56qe7ZosWT8+B2mmOGKKNmbNoXqf3K+rmLFMTy7NGPjObzloiVKDE2VKkBtQfRWv9+69U5qUabbtIkSAxRrD9umW7HxgYu6FZv7ykVnzw5RF4oqyIbPB1xswsNvuGSzfJQKFYnSuai12LjkoiI53br9d4TSJRcVG0K5c/dBSmGk+qsYyqp1AuhGlL3iqVN38yG/u4aR3KbcZy4KatacKpMUhQsPQDgNGxpOnz5tOucp9nLhZUK1nAHzVIFv377N8E13JJw2zkwhxjIXlYyhx4hTDDoBtHyUch7UVkMyLK9g6rJ8inoqjFzwwNrteDxhUo7HjBkD6xh8F2IHCPKpzgbv2bMHhbtkyZKvvPKK6b7H+OKikBxJJG2VdGbLlg1C1blzZzwrV65sOHYkwsok8JEjR2STpMpjrly58FFEyy0QeHKqVlyLFy8OHZVn9HWi6tSpk+gfO3bsUHtfhYuKhVvfegHYMsSAzymfokWLpkiRQm2PfPPNN2VR1HB1XjRz5szPPvusPNetW/fVV19VJSDL3aVLlzai56L6eVF+oni+tcD0798fp+zz9ArRcVHlhPzgJOXihHLrHIneVkz5ywQEgmra0GsByjNNmjQtW7bUPfU9uiJvDRs2NP2wRIkS94mLzp8/X+eiFmLmFhYlY+KigJotUKCA7mMqZ8Nxulhx0enTpydIkEC/1VbuOvMqsw87Vqw4hDqVOHF7nTYcP36pevUpUl/Dh28lgG78wy0mTULkftNJhZim1G8adOai0EX9QClCgu7CuOxVdkJDL0NETTdGXr9+U4yg3L79b65cfUzn3IRW6ZZp0Fz/+MPc6c2atW/OnBDDCSdP0gWZD/6R+LVr13q+kUQQFnZNmIO6TUSHWHNVJlVOn76KM3Xqzso8jBzYGz36jsbiVr9v1myBfh/JZ59F3U5JtJ4k1a3YyMKpS7s+0cGt2LjkoiaxYdxBf1MKgIcgF199NcvEww8dutC161/GAy82Z85ESYJLLrRu3bEkSTroXNSt2Ljkog0bztYZ3bVrN4RzOn/xo48m8ypduq4Is/KMuaxaJ+DPP/cqg71gxIioLmvy5F2epDwmXHTnztP4p0wZ4PzKRmRkpFrnMxyKijjR+hhzT2iQvbsMviL5sDO0VoZ+wzFfLAcnH8o7XUi9opfic/78+ei4qB6Y3MpzSEiIFJY4lUEnG/EOk3LcrFmz/PnzO8+v6GaTIXL8pG3bttZRxSVgZXy6R48e0J5PPvnEuLtsCI4dO1a9evW5c+9M0M6aNYuQ8+bNM2XQ203F9AtQgjZt2jzlgHgybMt67EsvvSQ72BVE0Uez/+ijj3zOJvxHLWrt27dPNifLWujGjRu//vprFdKZi0KK1BZZCC1lYioB2fvhCReVNcmxY6NUHGuBES6q9jB7Drdc9NAhVDe/evXqidOZI9WqVQufJ598kmry6tN//fUXP1QnPwXOXPS7774z/TDOuKiFmHmC6ErGJRd97rnndB9rLtq8eXOidfnRixcvTtWgdtQ/kqhYcQwaVapUAfCHoUM3t2y5JH/+fuqsl+imL7wwJDz8xty5+/W1zegg60gowQsW/E08LVosyZMnahfouHHBS5feYVnPPjsQH3XlfUTEzcyZuydK1F5dk/DTTz9RUxkyZPD8oDLqb+HCA4oVG1yu3Cj198YbI9Kk6UK+JMzs2SEJErRTRlPQ4zNm7PbFF/81ebR2lGY9Bv6INmfO3i4N/LgkFXJRZJo0aUx3u1tj69YTfnfvdDG9ovDlOJxau0OrlvOKnTuvCgkJ699/wyuvRO3JbNRozpIlB1D6V606jBPOryIh1/hAF8UJP1c3rxoOelC8+BDPU2stNjj9HLZkIiNvocpD59xG6FZshKvDc9RPnMWGToaSf+211zzffLFx43F//85lyozUaxwanCxZRwpWwjzIYiMtFNrp8u2wYVt0LupWbGbO3Oen2UMWUBd4Sv2uWHGoQYNZELCkSTts336S0tND7t59hpAwUt0z5rJqnQC4KM1c/RYey9vQ0MuepFzIqr5uLDZylREmw7HL13lhXFCtWhT3ttis/jhjx44dKFeoKCghslnV5dqe6byoXOKyYsUKfGR2eNWqVd7OLvmMWF4XlStW1fSS7E5euTLqLqxdu3Yt1/bowk5FGb106ZKsiwK1iKQbPbLxIMCkHFepUkUxq+iATPOTVKlSyZW70UUVl+jevTufLliwIFryggV3ZtTkDCGpQj9WEti7d288xfKYz5g+fTqRb9261XBo8HqJ0UbeffddPwfgaaY9uqIO9u1r3orjIeSiy6ZNmxqOU39Lly6FjpYqVcqIOlhST9IjsOai/v7+wtid4S0XtRaYeOSidERQI1KOf4UKFTy3XTRs2DB+MmjQPTebPVBc1IhezDxBdCUTcy5atWpVSsDlIm1wcHBSDaZiecRw5Upk7drT5coQv3sv1jMcVighosI6TEfmogP1++GHkyQ2lM49e86MGhW1sIAKOHHizi1bTkBR5C36uixfXL8eRSpQWJX2L3OIavbKLW7evP3SS7/7uTqPR8rVFj7DwXnQTVu3Xoqazk+aNp2vbPDMmLEHyuEykvbtXVsyc0kqAgMDJfEDBw70JPFwqlatlj7zTD/5VoYM3Zo1W3D06MW7sa0X8zlShujEGzZEqdG9eq2V1GbP3mvWrH0UnSyCQTJR7qlHngnQocOKs2evzZ27v2DB/rKM0737auro++/n58sXSF1MnbobIoo279WWaWux+eefc+nTd5VlTHWrpDWsxQaOVKnSWHkLo1izJmo0dxabihUrSsl7qLYdOHBe0un89+abI/WQD6DYHD9+iWRI+rNm7UEl6nKuAN3SuZaF2Pz++6YCBaKEhGpt3nyRiJnh2D4twon/J59Mu3DhOjwcZ7ZsvdR0kgKl5LwUHENZtU4AXJRoq1adMH78jp4918Bp1YK8xQ/Xrz/Wt+86uSS2UKEBsjQKT5YNCJkydafdUcWjR28nR/hQzuQiPPyeU+gTJuwwnYy1oXDr1i3Ip5rx37Jli0tbPCYuyogsNE0AiTVtabyviGUuKmdh1ZUYssIpRi9CQkL0bIu9IlkYkWOl8FilKkkZialPGw8CTMoxDAfnnj179DBUn1r3hquULl160iRGOD/4mEVUcYnQ0NAECRL43WtQd/LkyTIOkSkVUvY3Dh482BSDfkOpNWCSiRMnpgmIU+eiartsUFBQjhw5+BDERgWDz0ADXnvttUSJEsk8jg8gnowZM9IShRyK2Vu6pDJlyujBrLlovnz5KCgTZ4CTnD171lsuai0w8cVFIyMjZdqPfun111/nVe3atT389LRp02QKQ/d8oLiohZi5hUXJxJyLyrNpqRaZV1vHHyugdW3fflLftKlw48atnTtPm2zSusX+/WHqskHDYepDv1/UGZcuRajbFwVhYWF16tRR9rFjETR5qM6KFYfOnQt3H9on0EE1adLEh87EK1BiioY5PhruycK1QLRq6n3XrtMHD573LQEWYkOFUsjeWtyIudicPHmycOHCnptU8BwPqdjQfk+cuKz7+CA20gnoXHffvrPOfcL58+G5c/dxuRQcE1m1TkBExE2qho8eOHAeYTZtV/Yw5b7hxx8XmmwU2zCBURhVjfboVVdA+NOnT8NC49hkTyxzUSGc27Ztk2wEBwfjhFgadw/UQjiFoB89elRoKiHxkZOisr8ZpUTWV+PMyKoNtxDDP8o216BBg3Ci98ulDoKuXbsqslG/fv0ZM6KOHKDCElIZAXKOShBnd8kKV9HvcUHnTpcuHZ667oXQCmWV3fMCpHTEiBGGZ8iWLVumTJmUs0iRIoqLDhw4UHFU2oW/v3/NmjXFqWwXQSNR8TNnzqwnwHMMGTKE9L/44otSC0LJ4DxDhw7Vg1lz0erVq/O2TZs26i1NtVGjRmL72kQ2DEsuai0wPnNRZ1nyiotCFydOvGMRnoRBuqhxDz/9zz//yBZWfcaRuitWrJiK3Gcu6rKNuIWJi1qImVtYlMzLL79sSr8zF+Unfg5L2spH+gGp7lGjRvH85ptv6vt/OnToIP2/jXiHLKfHzbVysQ6IdOXKlfV+xkbcgPFRH1gfLjzsYtOt2+qAgFXuwz0SCA+/kS9foNxhY+PRQCxzUci0sMotDsjKp1wkCNkQa04oWHBUCaZ254v54L/++mvXrl0QVKGpccZPbLiF7FlFzaVSli1bBhWBWcnmPXjmvHnzPvvsM0VaZs6cqWyxnjt3LmPGjGnTplW2T0xRGY47PFOmTNmnj4sT+bEOIUjKvK2gcePGpNA0Dn344YeELFCgAAlbvHhx27Zt0c88H6vkwpjhw4cfPXo0MDCQQkiSJMnJkyePHDkC9YIEqpBQkR49esgzTOaJJ56QqZy5c+cSA1q+MgbmOS5fvkyRkng1uQVJS5UqlenCzxYtWvCJOXPmKB94heLM27dvl2Xkr776ijqdPHlymTJlFGOH2xDy7NmzFCb/oWTCflVUwjDlRKW1wIhIeHti03AlSyVLlsRHzc0LIVQ7jVE4/O6aX5K3ZcuWVbFBWU0rvdYgWmKDsQuJIqcUF9WHPJNf2SmtL7YLnn32Wfz1zg3Z0A3eusyXJ5ClWlWqFmLmFhYlU6VKFeHJNG0xr4Uk5MuXzxSDXDAzdepUgg0ZMuSFF17ASVOCf5KpwoULi7RAmHn71ltvKeprI34RGhpao0aNh3QimI6I9ujVqT8bsYKlS5cyjD6kXO4hFRso2bx5+w8durBnz5lcufq4XCR/lLBjx6lVqw5fuRLZuPEc/VipjUcAscxFDUerXrlypbBQCKc+pF27dk2/QTUkJEQpyqadyuvXr9dvRbcR7zh27FimTJn8HDdGik2L/fv3i7kCAJFTTBLNEnW8fv36YpYGpVa0UrRV4TzOUY0ZMwbn999/HwcZQa5Itslz8+bNn3/+uXPIWrVqJUqUiLTxv2HDhiYiZw0YV+LEifkt3GPDhg2yApk7d27KbcCAATlz5vz111///PNPooWVMYQfOnSoVatW8rlmzZrt2bMnODhYLmzMkydP9+7dvc0pBFJuGRWg6+tWiwwHdSEZUhE0uhMnTvBdqdCWLVuKmVP48JNPPimezzzzjL50LDyWqu/Zs+fx48dl42XChAk7dep06dKloKAgwguX/uuvKKOI0QnMqFGjoEl4FipUCDoXGenFZKcuS2gS3bp1g/DjpDbpXqhWGJR8jupYtWqVsMekSZMSEoaPcMIDa9euPWPGjICAANiXOl/gCWC8derUocqgoNmzZ58yZQpMHlqFPENHZYU2derUlI9E+/fff8u9OH4O+7p8nRQi9uKDJqcus3FuI24xadIkKd5cuXLJ6rdLMfMwaxYlg0gkcoBC3rdvn9S7bFcmOyqGxYsXp0mTRkqAKkb+KaKmTZvKyQvGhYoVK8pMR+bMmSdMmOBxqdu4v5DJgvhOhY+44UB8p+JxxEO9wf4hFZtevdaq87EeHil/eHH79r+pU3eWzObN29d0fNTGw47Y56KGg1heuHDh3LlzzqoP5BOFHr7q0joTaiivUGQf0t1BjzbQvJ0nDqllNGxvdRfnqGBicbY93aXp9ujsuUPJ9u7dq9sH9hznz5/X7TaRZWkRQreIE1Xec2M53oKY9Xrh0z5/68iRIy63Ch88eFC/mcPDVPkgMBZwKZYe4tZdkBGfbZdTj9Bs6bJisTZjki9BTMTMumROnz7tyVq9fFqUvIsXLzo3cLp6qKnd29uwYcOGtzhw4HypUsPz5Qs03Sn6qCIgYFXOnL0rVx6rrIvZeGRwX7ioDRs2bNiwYcOGDRs2bNiwYQGbi9qwYcOGDRs2bNiwYcOGjbiGzUVt2LBhw4YNGzZs2LBhw0Zcw+aiNmzYsGHDhg0bNmzYsGEjrmFzURs2bNiwYcOGDRs2bNiwEdewuagNGzZs2LBhw4YNGzZs2Ihr2FzUhg0bNmzYsGHDhg0bNmzENWwuasOGDRs2bDyCOHTowtixwTGP59at2zt3ng4K2rt795noLoK+ejVyzZqjM2bsOXDgvMsA4eE31q49OmdOyLFjl9x+8dKliPnz/+7bd92uXac9SeGNG7euXIlUf9aBr1+/qUJeu3ZDPEnVoEEbL1zw5SpphcOHL0yZsismMThX2fnz4ePH7+B/TKKNIWIxDRTRrFn7Nmw4HhFhvn9e4FaQPJHGgwfPz5y5b+XKw8Sm+//9998xTH/cYMqUKcuXL7cOc+zYsfHjx8dJcqLF+fPnSQP/YxJJSEjIzJkzLQKEh4cPGTJk//79MfmKjQcZNhe1YcOGDRs2HinAZ154YYif329PPdUzhlFBG55+OpCo5O+VV/7Yt++sKczEiTvz5OnbseNKvvvyy0O/+WauiSSMGrXN37+ziuSzz2bANl1+7vjxSw0azMqfv19g4PojRzy91D44+FTLlksyZ+4u8UNUogsJa6VMJFjZsqOGDdsi/p9/PgOfgIBVHn7RhHXrjpUuPYIYnntukG8xOFfZX38def/9iQkTtsPz77/P+RZtDBGLaThx4nKlSmOVDJDNuXPN7MKtILmVxlOnrnzwwUQVIEuWHosXH1BvZ8+e3axZsxs3bsQkI/cbhw4d8vPzS5EiRXTpXLFiRcmSJQmTM2fOOE6bwl9//fX+++8nTJiQZPjM8P/8889ChQoRw1tvvWURbOTIkYSpUKGCb1+x8eDD5qI2HlxcunQpulnPhxTkKL6T4DsYF69du3afIj93zrWWExkZGRoaGuufe6grwsbjg1u3bvv82717z8aci8LxIHht2y4bM2Z7ixZL0qbtQpz58gXqy02zZ4fgCdsU5+nTV9On79qkyVwVYMiQTc88E8Uthw/f+uWXM4XYfPzxVOfPESZZso516vx5+bJrpmqNP/7YIgzktdeGRRdmwoQdEuaJJzrpS3NLlhyoWnWC8zKs51UgBe4zFzVcVdnt2/9mzdoj5jwwJoIUK2lAYJCBBg1mjR69vVu31QUL9ifCJEk6IGAqjFtBciuNkZG33nxzJGJw/nw4P2/TZhkB0qXrqovrypUra9WqdfOm61XZBwG3b9+uW7du27ZtLcJA/+KXixqOdGbNmjUmXBTMmjXLLRc9cuTIBx98MG3aNJ+/YuMBh81FbTxwiIiI6Nu379tvv50kSZIrV67Ed3JiAdu3b//uu+9y585tPbo8mKA6+vfv/7///c/f33/+/Pn34xO9e/dmNGJM0j3Dw8MbN27cqVMnhtscOXIEB8fCVsNTp061b9/+pZdeKlOmTMxjs2HjvgJe1KPHGp9/fvPm7Zhz0fLlR2/dekI5jx69KAQAVik+kJycOXvzp/8KnkCYbdtO8nzhwvXixYfoq6BCOfgzbcL8+edFeOrcw1vMm7dfrb6uWXPUZZgSJYbCVAmQI0dvlwF0jBixdeXKwx5+/eTJKzHkoi6rTFIbEx4YQ0GKlTS0bLlk8OBNyhkRcbNkyag4P/10uvi4FSTDA2kcNy54xYpDegwVKowmwOrVR3TP5s2b//jjjz7n5UHA9evX452LGlGC8VoMuei2bdvcclEbjzxsLmrjgcPt27ePHTuWP39+eqhHg4teu3atSxeGTL+HkYtSHefPn69atSrpv09cNCgoqHDhwlu2bNE9q1Wr1rJlSx527NiRJ08et4dnPMHNmzdXrVpFRt54442Yx2bDxv3DxYvX8+fv17btMp9jiDkXPXLkYtOm5ib/66+Lifabb+4wxqCgvTg//3yGHmbhwn/wrF8/6gzY6NHbnXfMvvrqHwSYPn2P8pkyZRc+sNbIyFs+J3j+/L/femtMkSIDieqDDyY6B1i79miuXH169lxDABPtcQa0J1myjsuXH/Lw6w8mF425IMU8DeB//5tk8hEhobLE6VaQPJHGvXvNu8ebNVtAANNy97lz59KkSbNgwQKfsxPvsLmoDQucPHly8+bNK1eu5P/x48eV/7///kuBb7kXaldaZGTk7t271ziwa9cuZCzOEhz7XNQiM5TCgQMHNmzYgDq4ffv2CxcuiH9oaOgWVwgJCYn15NnwGdOmTaPW4uxzQn4eDS5qOA5XxBYXPXjw4MiRI2Mej1cICAi4f1zUGfSeCRIkGDNmzP2IPGHChDYXtfGA4MCB8+PH7xg7Nviff/5T9C9cuF627Ch06Hr1gtatO7ZzZ7T2e27dur106cEhQzbB5Y4eved0Zcy56OXLEc7mauCWRNuq1VJxfv31bJwDB27Uw8B/8EyVKsBwLF45H7WoU+dPAixZckB9KH36rtbnPCMiIoKCgqytpAgXHTUK7fa3BAnahYSEmQJUrz6lT591/LnkoiR1w4Y7etvu3WeyZeslWaMKTCdXt2w5MWzYlnHjgnV/nYteuhQxZ07I8OFbDx50kWCXlW7EjIuGhV2bOXPf0KGbN20KVQUeK4LkeRqiA+lxjpOiI87XXx8uTreC5Ik0OqNMmZHONBjUqlWrSJEi1oeA0ONFC0WnHTZs2PLly00HOM+ePcvIbkSdFl43atSoy5cvq1dhYWELFy4cMmQIv9L9d+zYse4u/vnnH/E8dOiQ+DC4i8/NmzfnzZuHOq1/7vbt2xCJoUOHMhBfu3bNJRdFxx4/fvzYsWNV5BYgwuDg4NGjR0+YMGHfvn3OAbZu3YoazwOxjRgxgu+aSkznovCfdRrkIAzhlQ+fc/6EzkX3799P7lw2c2JbtGiR2xzZMBzq03IHoFrycPjwnc0dMLLlTjh1KmqfPCJHHeFcsWIFJJYHnPS6cZPmWOai1pnZuXOnXkAEEIGj8TiXDjCtk9iIR9BP+fv7b9q0yX3QWILNRV0iPDy8WLFiPXr0iJVUeQ5Z140zLjp7NnqJHwPq/Yjc5qI2HgRERt76/vv5TZrMHTRoIxwJ7tS69R2Veu7c/e+8Mw4l+403RrRtu+z33ze7jCE4+FTu3H06dlwJx2jffkWyZB31lcZY2aPrjG7dVhPtsmV3lGYxtzNp0k5TsESJ2uN/9qzrE+aVK4994olOyuAtnI3A/v6dt2498eOPCz/8cFLTpvN1kzOAzpM+oUqVKhZpEy6qrBM1aHDPtn/oEIwXSmPiordv/0sJi+Wh776bJ56QosKFB8hKHVWwcOEdzR5uWanSWMgPyfv223lks02bO0uOiovOmLEnQ4ZuBQv2p07J5tq1/+0Wtqh0IwZclPTXqjVtwIANP/ywIEmSDu+9Nx4WZ8SSIHmYBm8B7SdOVXq+CZJJGk0YNy74k0+mXb/u4mgoLBFxmjvXxYbwW7dutW/f/plnniEAFLRGjRpJkyb1c+DVV189c+YMYWbOnPnBBx8kSZLkk08+GTBggLzlV4aDffXq1euFF16YMmUKAxkSmzZt2nHjxknkcL/cuXMTuGTJklBQ8Tx69Gj58uWfe+45qC+8t0mTJhkzZiSMWrAxHEyPr3/33XfLli0bOHAg5M3ERSGu33//Pb8dNGhQ9erVEyRI0Lp1a5fFIoBAkoaff/4ZZbt3795p0qQhqUJLQL9+/Z5++mk+wbd+/PFHPkQucNatW1ePROei586dq1+/Pk4+vWDBAnQVKQ3oAD58wiXzV1yU1BJMSjJDhgz8SgJA6atVq5YsWTLKxyI7NgQQ/tWrV1OnCJXhEBthW3JAOiwsDOfevXvPahCOduzYMV6tXbv2xo0bBN64cSNO2FncJDuWuahFZiAVwlEvXoyaJaUsFNu8evWqXi6nT59GcectscVu8mz4BvrHvHnz0kEEBARMnDjxyJEjkyZN4oGuVgLMmjVrogP6VNyuXbuWLFlC/zhhwgR9HY++uE+fPt26dVu/fr3pQ3TNQ4cO5Ss7duyICRcNDQ39448/GBhImD4Vd/78eYYW4mQ44UOkQZqrDmSSzrdTp06MImpVnwglg9I/IrET70Kf8kSwGaLatWvHV5BwPVrFRSmQefPmdejQYfLkyd7mi2+9/fbbxMP4x6fpxNWrw4cPjx49mk9T2mo48QHHjx8n8W3atCEefVODMxeljU+fPp2MUJumw5z8kBrnJ+SR3sCtP+VG+axZs0aiJWvffPMNn2vcuDHPQUFB+/btUwXOyCS/osMVHxnzPIfiohs2bEAGqG6TmKGLLFq0iFcMn6tW/WdXk/FVvvjnn3/qTiX5/HeWCk9Asf/+++88IJmIbt++faX3Q3oZRTp37kzlmiaVSVj37t1pLKbZYgsh5ycqwUp4ZsyYgXPOnDleJVhAAVKbpJa6o9BMb2PSDB8HtGy5BO1fOWXb6tSpu8U5ePAmnNZbK59/fjBURzmzZ++VJUsPpfDdJy5apszIYsUGq6/I4iEk0BQsXbqodc4tW044RYAyEJkyZYBifYaDmhI4c+buUKlRo7a1a7dcjOXoezKRUvRRa/VauCgP3btHURQ41enTV9Xbn39eBNHlwcRFycuZM1dlXU5PVY0aU/DR9+heu3bjmWf6TZiwQ5wQS1nOlS2gwkXTpOnSqNEc4T/DhkXZUnr33f8u3rCudN+4KKy4QoXRyvnLL1HbVhs3vtOiYy5InqTBB1DLfFRd8OODIBlO0qhw/PglCD8/RJDGj9/h/EOhQI0aNXIZLWOokL3ixYszXjMqQbeKFi2Kz8cff2w4dPpff/0VZ8GCBUeMGIG28+mnn8ISDcceopQpU6LKSlR0fXA8QqoRf+rUqThffvll/YtEK8PrpUuX9u/fD8vVuShsIV++fE2bNlXhJRKdi7Zs2bJjx47KCXElAMFcZpBOOFOmTL/88ovyWbduXaJEicijsuoE7yUGOLkwdga1PHnymHbkmvboMhZDI/HR719BPSBal8kw7lZE+vTpGSnIL5rM559/jk/q1KkpZCnq8ePH42NzUU9w7tw5oVoy5opyhQ/EynDMevAs8ykmbN68mVdqfkTYHEN83CQ7lrmoRWbQ0nhWCpBQU2DahGA4lunxh43Ebtps+Aw6qffee4++AK2Rru3kyZPUZvLkyZMmTSoB6D0bNmxIgMGDBxsOO3Xo+jhhFLCmVKlS8Sy69Y8//ohijU4M2cPz559/Vl8ZO3bsSy+9hLSgl3/77bf0Tb5xUUhUgwYNGBWIMG3atGXLlhXrr/369WOEIE50mjfffLNmzZopUqTImDGj2g1CN1qnTp26desiwEhymTJlChQosHVrlFEE2jO/0k81nDhx4sUXX8RHcU5GC6JlMKB8fvrpJ5nbo/eUMhEuylhSqVKlatWqMQ7hZDDzKmsUO4MHP/zss8+oCNVGYIOlSpUiqQcOHIC/pUmThkLwttyMKK1lMBW9fv162mBeB8imvDJxUfwpHCqRsp00aVLixImFnkkxMvCQPMgJDIdCtvYnqURF5HzCcHBRwiAAwkV5nj17NqNjs2bN8ClXrpxiyHQdFC9sx9tsChflE9SmTHkwbKu3Bw8efP311+FX5JH8Pvnkk++8844oFhS4qAiykwquRQJwkgbp90ln7dq1kSLPE0OxtGrVCiWAoReJJT2oR0gOSgbxf/XVVwjk+++/z1eUsQ2+8r///Q/9hlGHHhUZRt7klbWQ007JGm9R6BU5RFxpyzt3mpcj3ALpJQ38nBpEAOAJ1G+9evXkrc/N8DHB3r1nEyVqf+DAeeiH/AUErEJ1fvvtO+snnlCIUqWGv/zyUOUsVy5qN6YsiBn3h4sGB59KkqTD5s3/mbaGejnbhgEwPfznzXNxJWD//hty5OitW8rNly/qlg7dts3hwxfELI2+5OX2Kg7FRS9dihAjRmrVERqZKVN32Snqco/uuHHBbrnot9/Og4vqzGfkyG2VKo2VMhcuWqjQAPU2IuKm/iG3le4DF7116zaFOWLEVhUndSH7Wm/fjkpnzAXJbRp8QHj4DchnYOB/89E+CJKzNApOnLgM0a1XLwhGLYasnCkuCgm90PPPPx9dCmXE0ccXMV0LjhyJSuSCBQt4NpnBQ9enO2WA1j23b99OyCxZssjgRd8r5jCU8kDPTOepyxXMU+eiqF449YN//ETnokTFIIICcPMu5FjN22+/7TJ3jK1qIFOQ0RB1Qpw84ERhUwG+/vprfNRYb7g6L9quXTt8GF6VD2qeitMZwkV1Zk45oArKOCU+ZNzmoh5CaBdKu/KRRUHhZfv27eM5JCQENW/t2rW7d+9WG1eFsjKgixO+Kpw2bi6ziGUuapEZ2aCr2h6DinBRfROCEXW84QKeq1evfsAvgHrc8MMPP9AX6Ht06SwUFzUcqqfiooZjWwVOOlw6EcRg9OjRyABhdDUdTZQw0magoDAEtaxKYNkh4y0XJYZixYqpJZr27dsrkmNEmU/4H84WLVpI6xo6dChOWY8yHDyZBCsdnU9ny5YtR44cV69GzazL8Qz9hD08QR9O6PoZDC5evHMqBiLH2KMCCxclbbIERAoJAEv3KnfG3c2r+h5deB3fVRNAhmNEwUdfNfUEtFMyqzomGYcGDLijV5m4qBSs+kTu3LkhOfI8ZcqUdOnSqWipcSnt6PyNqB16w/VqMhwTE/joy+mXL1+GrWXPnl1VLj6QWB86SiQtffr0ModtRN0rGDULK3s0qP0SJUp8+eWXKjAMn7dIjjg//fRTnGodWMSe9KvwlStX9uSgjgkyr6HGeIn2hRdeUPOXDPn+/v6S95UrV+oaAyUJFVSLw9ZCLr+FAapPL168mEx5m2C6aH2HG4QZpzpxFJNm+JhgyJBNCRK0e+edcaa/OnXuyIAnFOJfBwzHnZlTp+6Gk/CT48fvLDTFOhflW6+/PlxdyCkQqrBokVnmM2RAe/7tr7/M1OLMmavZs/favv2k7pkyJXrzb7qJVPDTTwwiv9WuPd3zFCouakT15wvlPg9YqOEoz5o176wRueSiEyfudMtFKWGXV9EIXNoueuKJTuROnt1Wug9cdN++qGtgCOMc7alTV4zYECS3afABLVsuURZ0Bd4KkktpNOHq1cgPP5zEz3WmLWB8p9t58skno/ut6DymcyJCvaTfo+eUPUp6gDFjxqjNujqEfMIKxBkYGChz0+Kk9+vataseXvQfpR4z0mXMmFEPYLJdNGTIkAQJErzjhOgmRvPkyYOSYNprI+OOoq+iA+jjMqzSNC47c9GwsLAnHJDpRaoJXu1yIU7g0naRDArKE05hc1EPgSoIh1KSZtxdI5Q6Qp8xHSVVbEucqqZkfRXEze1HscxFLTKDwPGgFu5pA/JK7WQwHFILJ7F35z6AcOaiqOw6F5VlQ8VFd+5kXPdr2LChHgndH3r/4LuoWLEiYdq0aWNETcSWo1PTA/u2Rxed+NVXX1WfaNKkCZGULl1a3jZo0EBnjzRXtTiJHNI165N5xt0TSqL0S9ev95im2MqWLUv/q97K/hY1kel8XrRGjRr4yC4Uz+HMRVH6TRtgaEGEoQC9irlIkSL6jh1IKcOqGgtNXJTmjEioCaPixYtDR+V53LhxhOzUqZMoNzt27JABLzp/I0qDnO+WixpRe89+kfU0cY4ePdp6w150MJ0XRU6IVu4uCwoK4nnGjHtsOcoivxBvMcPbrFkzeUUXh7NUqVLiRIoY/n1IkuwHU0u+cF2cCJgKgEqBj0zzUSlIl5p9kPl7mao3LIVc8MorryDqalssMS9dGq3lj+jQoUMHvUOAReNUZ6J8boaPDxo3noOK7PIkm8ATCmE4FgADAlY1aTJ37dqjspylNj3GOhdt3Xqpc3pKlRqu7zJVSJw46pifs22eypXHLlhgXqTKm7cvgfWrJo2oox/78HzpJS8mKXQuSjlIGvr330CfU7Bg/02b7iyg+cZFz58Px1m3blB0X4+Oi6rtr24r3QcuSsnz1rlIFWIuSG7T4C0gnIiByWCyV4JkRCONzoCOpk/fNVmyjrJKrIBI0O1YTAe75KJffPEFniNGjDCi4aIySDVv3twUm/TwjFnivHjxItpC+vTpZfKXEUS2UCroXJRxlh4bOqoHMHFRWef00PBpeHi4nMw0HW9Zt4524aeGct+4KJAjNrKgyoj5wQcfWCTGJRddu3YtnoULFxaniYueOnXqmXsBd/Uk448DnLnoli1bFBfdvn07o7bsd7t69aosHx44cIDmYGJk58+ff1i5qHVmTFzUObARdbXxaVlcdmluy0Y8wjcuisasAsiWEronk4UqVNJbt24RlalP942LQoqqV69u+oTarmBSgqUTJGs8L1u2zM/JtpAMNrJq5JaLyoqZogQBAQFwHtXXO3NRWY7zdtrFxEUjIyMZpUyWePAkTPbs2T2Pll6JwcmiQ3dpu4gPQT/atGnzlAMqKpkDlh3X+idc+hsec1EGJOTkhRdeEGflypV9O1hv4qJ8Rekc5IXn5ffeH9OyZUt98bNgwYKZMmWSDvr3338n47yVtdDu3bv7cAzYcOKiCJWJi4qwmUwdIrQkuGTJkro2YCHkAuGN4oMmxADvw9qyLGUr1WrNmjU41VFen5shKtpUDUi7twl7WPDpp9PRsC3smnpCIVauPJwrVx9IlDjvKxcdNy5YDlua0LQpjfc3k1GcK1fogn7LkKGbSbQaNZrz558uLOW+/XaUfR1lH0iwdesJPF94YYjnidS5qHG3kHPn7jNnTghUR/n7xkUPHjwvRoCi+7pbLuq20n3gomL2Cb4dXZwxFyS3afAKu3efqVJlgixW6/BKkKKTRpf46KPJVIGJi9LV0O3kyJEjul+55KJyeGTlyqgTvy65aMeOHfGsVauWKbbatWvrPaRxd1/VhAkT9uzZ89FHH5nC61wU5sBzmjRp9AAmLirqh4dHLUTj8rv3VKfh2M/ip51Y8ZmLHj58GLUka9asaAgNGzacOXOmRWJcclFJiZpPN3FRiqXBvXior+eJXYgRXec9uko11SFbduWCDLF4pKyNQM2WO4wexU2yY3ld1CIzu3bt0vfoosmJgiJ2nwWUyHLtuKmNBwcx56Ky19Hl6T7pd1BedU/fuKi/v79pbNBhoQRPmjSJZ4YHPTwNFU+Z1XPLRRmZoHNff/21OMuWLdukSRMV+D5xUdqan2MvtClYlixZ0qZN63m0UhTw5+gCOHPR6dOnV6pUSc7Twg8VF5VUvfvuu34ONGvWTKkR0fl7yEWNu+M3HOzMmTPlypXzPIM6LLioHHs2nbYVi4uBgYHi7NWrF07GVznWQqPwc5xswQktdD4A7wk85KJK2Hbs2MFPxHiYtE3PuSjpLFCgQKpUqdDGZsyYIRsTvAVVmTFjRjinzLZ06NABGVAbvH1uhsHBwUk1xPvtefcPcAM/V3dRBAefkjsS3VKIU6eu+Pt3rlz5P135/nHR2bND1BWOChcuRInrokVRN0B++eU96uayZQfxNG1nbdFiibMVGYlEzO2Y7vNYs+YonqadnNaYN2+/zkV37DglxwUzZuym3xbjGxeFzCRL1jFJkg6HDt1zsAh/uQnGLRd1W+k+cFGS56fdjKIAi5s7N4ppxFyQ3KbBcxw4cP799yfqR4UNx8UthjeCZCGNLlGr1jR9JuJuSg7Q7aijJc5wyUU//PBDhg9ZQXHJRWVnzdNPP22KTXaBKfsLxt3NL2XKlOFDOkcV6FyUHjtFihQ41c0chhMXlT1crVq1MsXDV0xmFAXFihXz03ayCGQ1Uo07PnNRULNmTT/HyYvChQtbL6y55KIyudmuXTtx2nt0PYcs6ek2FynM5Y6zkwiSnCVWr6g4XokWZ9qUiqwud1iijZtkxzIXtchMSEjIcs0iERqMcFGlfqHHiI8cz7PxQCHmXFROn9eoUcMUM4IRFhbm5zgdp/v7xkXz5cuXNWtW07r6uXPnZPCwUILFuoDJDoGMFrIR1C0XNaIM6M/NlClT7dq1mzdv3rdvX92y6H3iogDOmSxZMtPmHDzVxlFPIH195cqVTf7q+KuJi5K7xIkTq5FV56LKhCyjco4cOfwcZvEt/A1vuKhYjyCdAwYMkI1SPsCCi5IvfQgUyNketZEVcUXy33//fTIixrcoanSCRYsWKfNC3sIrLrp+/XoSIJuKDe+5qBFl3hPNMsoUWfXq1X022n7w4MHcuXO/++67LVu2/Omnn3TjQz43w8cHK1ZEUYjEidvrxxGPH79UvfoUmaOR9a7mzaO9Um/SpCjupFOIEiWG4qNuvHRJbND79XOAjLYrVqywvkSOFH711SzTwhR8rGvXqJsVYWK5cvXJly9QfyukS7dD063b6j/+MB/tmzVr35w5Ufc37tlzJkGCdqVL39Oi5erIadPubNpEnNAlrI2ET5myC9ak+0BNiYTk6ctiPXqg6f6WPXsvPaQzF5VlTN1qTtWqE/AhzqtX70w5USw//bRw//6ooxZuuajbSveBi1KhqVNHWWkKCPhP+4yMvAUBCw2N6nJjLkgu02ASJGoHlVff5uYM0gMRNd0Rev36TSlzDwXJWhqdcevW7Tx5+jpPgtCL+jlOrUeXWmcuSjPJmDGjutTEJRe9du1arly58NevCbhx40bmzJmdlR+xJPf8888770wxnReVAUK3oyvrumr3E60YJ4OyvqkHpYse3uW2l4EDBxK+UqVKuicjXaJEidTiaky4qGiAKVOmdNuxu+SiaDjp06dX4mRzUc8RGRkpTEqEB71LnEimMhkrS4C0WaFssjwuHI3qEIFB+8W5e7d5z/x9QixzUYvMCFlXx2TFsjBDi2oncg2O3Otg40ED5Mrvrp0hAd0oOr3iiqLdDhp0Zxh25qJUNN0xP9GvoIDMyBlFulTTDhPhoooLeQh6Xr+7Z1AFyFujRo1ktcpCCSZYnjx5SJ4+czllyhR85KDgzZs3CQwDV29l182ePXfuYaMo6tevH5050NjiovPmzTMND5IMdb+O4bAZhk+/fv28illGUH2Clh5KTS6YuGi2bNlg3SpkkSJFFBdlkFNlSKv39/cXSznR+RvecFFQrVo1XvFFn++eteCiYo2wUKFCenjkB/kUM7CCjz/+mFEfYZADnKNGjSIGCJhcjO4DvOKiJsGTwzlecVGaAzUIXTTpIl4BvUT29jjD52b4WKFixTFi7xTOM3To5pYtl+TP30+dmVy8+IDsUA0PvzF37n59kUog60hJknRYsOBvftWixRJ0bnzGjQteujTKPGZY2DUx3qN+EhFxM3Pm7okStRfuZDhM0FH4KJTR7dPeuPG4v3/nMmVGlis3Sv3BVZIl6xgScieS2bNDYJJ8V5xnzlzNmLHbF1/8Z2xz8OBN8CU9Bv4KFx6QM2dvqIKE+eGHBaR25sw7u9BhJlBTgqlIZOUnTZo0+uqQCZRhmjRd9AOZS5ZEFeOAAfdsYZXbPpIn70jZKs+BAzfiqSeb2PAhMNRu5MhtJGnv3rNkHM+nnw788ceF3buvfv314TBbCU+B8CpHjv+WW0kJPgkTtrtx4868pHWlO1cZePZZaMNvO3ZES8I7d14ly7/vvDMuMHA96SladBBMXt7GXJCc0+AsSMp0fGio2aqtyho1XqzYYF0G3nhjBPVFOUgYt4LkVhqRtGrVJq9Z898dUbDZ+vVd7BHt2bOnn2Z+zxnCRWvVqqWaRvv27RnmlA2ImTNn+rkyVMsYzejAEKP2yPTv35/OVreCK5AZfJfbkeR+USXqW7ZsYdjyc5xyCgsLQ82QA6J4ErkEk6XXVKlSffrpp0OHDm3ZsmX+/PlN160pwENKly6dIEECUis+UBeGML3TFqMAxKN8vvzyS13NM6IE41l8XF57ISO1223Du3bt8nPcnaPmLslOzpw5J02apMJAIgiDimIdlQ0B1QGZQuek8OVEqIzUyiLPqlWreLV+/XrZuCqbmyCoK1asWO64a1OOmAJvNXCfEctc1CIzt27dkpVi+AzNQ4Lpg4pc5eKt8U8bcYPevXsLW6AexQCp7GaEo9Iz0p3J3kvYhUzGyI5c3R6p4bjOQZSJVq1awUjhOSVLlhQy9scff/AKDiAzNJs2bUqXLh0+9LMWFticQZOTQ/lfffUVQ8XkyZPLlCmj+JUYHlAKtNihUfaKyAW/pYsXJzllONFnIuXqkalTp547d27IkCEvvPCCn8OykawqoGoXLFhwwIABQUFBixcvpp3rdonIr592LYdx15qo84SiNaRg33vvPcY5vmI4+Dxl9eKLL6qzqRQvKqbzfY/WEBt6DKLNmjVjjCSpFSpUUOxIFEF18AMm4+c4Qnn06NHAwEAGziRJkkDMjhw5QpXpt5zlzZtXVnGj8wfTpk0zUReZtXVJp2VYgsl7lTsFSBE/p7iUDwnz03aPy61x6lo2xC99+vS6FXvj7ulitaMbmgq1Ni2qewWxKa0OLMiCPJxTBRDbRbKXRrgoX6fAGbBltxV8XpiwtZAroE9Ex/Y9wZQpU1KmTNm1a1cKasGCBatXr9Y785g0w8cHV65E1q49HYVeiATUSzfeA0mDPwhvMR2iE6BYiI1Q/l555Y89e86MGgWr/y1p0g4TJ+6E1FWqNFbeNmgwS7RzqBEUInHi9opGiv4KXC6PHzhwXu7PdP57882Rekj4DJyqdeulw4Zteeml35s2na8I4YwZeyAYLiNp336FHkm/fuv53Pffzx8xYmuVKhMaNpytc0XZngDoHJyTunr1EUiLFCblpl8WAl1RpxP/+usIzIQikgSULDmMj1IRffuuy527Dz5QnYCAVWKB9p9/zkn2n3qqp7J7tGXLiUKFBsjPeasWe9etOyZrsPw1ajSHoiPkRx9NFp9atabJMqNFpTtXGTEIbeaPXEyevMs54yIJsOInnugkIcnI9Ol71NsYCpLLNDgLktwg4nevUXGFmzdvIxUuZYBUUSYqpIUgeSKNrVotFZ8KFUb/8MMCUu7yMhhQwQGXrwTCRSFURYsWRduBc9JY1CURkD3RBxIlSoQWZLKAgAIDuWKUYcijD/zoo49cqjEMRpAu01I/urFQPj/HDiB1Zh71mMDizwOKNET0LWRuzBiZluU/QwPpkTBQzeiIqAAVgpRDkuvVq9euXTtKQz+cMm7cOFkhePLJJ4V89u3bl2HOz3Hj6IwZM9DwxSidn+OuNWdDCcSmj7MWQHigwYULF27QoEHdunXJlL4Fj5TI+OjnuCbQ5ghuge4nBx4F1JQyM3n16lU5PipYu3Yt2qz64dmzZ6Gm8go5VNIeB4hlLmpYZgaNjfajSgHNSZ+LlbJzubXdRrwDxpgpUyY/x7l2mfiEhEhfjNIJYaPu5JDYCgfom/wctxX37NlTLf1R3bBZOfkA6Pv0o/OQOrl4kA9BhKpUqYKSDV0x2Zdzi7lz59J7yifoNJUGPH78eLmFmUGFxkk3LYmEVk2ffudIEimHT8IS4d41atQwcSG4H0Ra8jVq1CiGGTpr8i52a+iLn3jiCb97IcyWxi+dKf0+2j89hcos3zLd8WUNylB2xTAaqd040AAKk6qhuBgeGDj1RTzPMWLEiLRp00rKGT6l5OnFGIqEfJYqVWrWrFmGw4YtrBWfZ599lmFYDDbkzp2bCoWNkzYYHfyNlHz22WdyPiE6f9iULM7kypWLAZ4BElooVo7gq4MHD3aeaC9SpIjJvJCHOH78uCzKMYp36tQJ7hcUFCS7oZ577rm//rqzywtlN0eOHJQkXAs5dP4WtcDAqc8jEK1vVotIA2KWLFky0vD1119TgAinzFMgbJQ8BfL7779L66tatSpv6SrFmTFjRioCoSU7NCtYnydCLmAEQlx9XlvetWuXLKTrQDIVnY5JM3ysgKq9ffvJs2ddNNgbN27t3HnaZG7UhP37w06e/K8SDx++oF8L6YxLlyKEaCkwRiPMMT8aQ6OAxqxYcejcuXD3oaMBpGXbtpMQS7UJVgdCS6s0TQzdV1BcZMp50Zgy37v3rFrU9RYWle4zbt+OKn8EwDm1cSNIYWFhderUcT766C1iKEj//HNuwYK/N28OdSlCgj179jCImyz3mKD26DKY0k350EDoDHfs2GFtQSC6ZeTogN4l00aUksv96tevX2eAsN4srYN4UMX17WCxBbQ4ta/KE1DCpNznIcmGCUgCYkCpmjoEnJcvXz5z5gzy6WwmFp8LFy7Q08aN+VyF2OeihmVmKAVEjQKyPqBi4wEEMm3aHAWnojeXc4Dh4eEeWm3hV/R9pntlBUgOEcr6nj5b4wOOHDnivCXGQ/Dp6LaB0bz37dsnk0wXL17UG/nUqVPhMPCT1atXz58/f9q0aUOGDBHbNr4lIzrQrPiKcydCuVF63i6HmkCOoNaebMw4f/68uhfEcPBhae8iBlJQeiVG5+8t6EB8M/3qLRAhixt3TPPc9GkxLHmvQDEiA7pRKG+H8GXLltWrV8/nBMBFmzZteuzYsfXr1y9atAh6MGrUqBo1augnmY2YNUMbcYMVK1aoO4oecNAeK1euHMdKkg0PIabpHopLEMqVK2cySuQMl7aLbHgItJF8+fLZxl9seIj7wkVt2HjcsHDhwjx58jj7M5LZW0piF4EOxHcqHnp8+OGH1ju4LHDy5MmMGTM6r+dDTeUyXhsPC5YuXdq4ceOHgt2dPXu2evXqFodFbcQjQkNDa9SoEZeb+nzGTz/9NGSI+4uCbC7qA3bs2LFq1aorV67Qq1jYhbJhwwSbi9qwEQuoX79+8uTJN2++5zTO1q1bGfbiYAXvcUDv3r379u07adKkQoUK2dt4fMPFixdbtWo1YsSIbt26qavbfMD48eP97rVgYTgI6nfffefV6W4b8Q7fNvPHC244EN+psOEaERERcbkxxGcEBgauWLHCfTjDqFevnp/DHsT9TtIjg9u3b6dOnVrOZeTNm1cZsLBhwy1sLmrDRixg27ZtWbJkoQsuVqwYWn7FihVffvnlrl27mq5aseEbKEY5Xps0aVL7VmufIcacwVNPPeWtAWcdFy5cKFGihJwQfvvtt9977z2k/euvv74fh45s2LBhIy5x6dKlFi1aZM2aFWaVL1++tm3b2nZMPERAQEDOnDkrV66sn9+xYcMtbC5qw0bsIDw8fNq0afTFffv2Xbx4sTLiYiNWsHHjxm7dukV3iYgNDzFjxozevXvHfCvdv//+u2zZsp49e3bp0iUoKCgmzNaGDRs2bNiw8djC5qI2bNiwYcOGDRs2bNiwYSOuYXNRGzZs2LBhw4YNGzZs2LAR17C5qA0bNmzYsGHDhg0bNmzYiGvYXNSGDRs2bNiwYcOGDRs2bMQ1bC5qw4YNGzZs2LBhw4YNGzbiGjYXtfFA4MqVK/bdcY8wHg2rwjdv3rx69Wp8pyIe8O+//x49evT27dvxnRAbNmzYsGHDxiMFm4vaiH9ERERkypTpxRdfjO+E2IhlbN++/bvvvsudO3fbtm3jOy0xwtSpU2vXrp0uXbrZs2fHd1riGt26dWvTpk3p0qVTp049evTo+E6ODRs2bNiwYePRgc1FbcQ/bt++Xb58+a+++iq+E2IjlnHt2rUuXbr4+fk97Fz0/PnztWrVIiOPGxcdOHDga6+9xsPly5dLlCgBL43vFNl4mEDDGT9+PP/jOyFxgQsXLowZMyYiIiIW49ywYcPo0aP//fffWIzTcGzxWLx48Y4dO2IlNq8SeezYsUGDBlFWsfLphxEMi0FBQT169Fi0aNGlS5d2797NQ0wivE9CEl+IjIxcsGCBfpd4eHj4kCFD9u/fH4+psnFfEftcFDGiaa1xYNeuXdevX1evaCoHDhyg2axatQo50zsj2Mjhw4fXr1+/YsWKdevWEezWrVuxnjYbDwgQkk6dOsV3KqLFA548b9G6det4jOqvv/56BLgo6NOnz2PIRZ955pm6devGdypsPHyg4b///vsJEyak1fz999/xnZz7i9DQ0Nq1aydKlIjMxi7LypkzJ3GiTcVWhFDlZs2apUmThmhHjhwZK3F6lcjPP/+cwAEBAbHy6YcOx48ff/nll+FaU6ZMSZIkiZ8DlElM4ox1IYkvwAKaNGmSIkUKsvPHH38ofwQVnwoVKsRj2mzcV8QyF7158yZMcvny5VDKlStX8oBTTRPu3LlzuQNwUf4TQE2X7tmzR38FgoODH5lpHhsmNGjQ4J133onvVESLBzx5XmHixIkpU6aMx6hsLvrw4sqVK2S5Xr168Z0QGw8lbt++nTVr1keYi+oz5qgrWbJkiTkXNc3CBwYG1qxZM9aPqX/yySexyEW9SuSSJUuqVq26a9euWPn0Q4cPHJDnoKCg119/3QcuGjdCEl+oUaOGiYseOXKEQps2bVo8psrGfUUsc9Fjx45BI9euXXvjxg146caNG3EeOHDAcKg1wlEvXrxIr713716cW7ZsMRzLUMI/w8LCDMdmMILhfGSa1iODRYsWBQQEDBw4UOpUgXGFAYZ6nDBhghrekIHp06d36NABJT44OFgFbt26NR3N888/D7dZuHCheJ49e1bvegSIB9/q1KkTBEBfYAfr16+fN28eD8hJx44d+ZAP2SFOUtulS5fJkycjtBbJA2SBjHTr1o1P65FQFOPHjzcc+2S6du06YsQI04a0rVu3du/enYysXr36n3/+8TaRqHGMNO3atSM9pkJwC8otefLkSZMmnegATVL8Q0NDKe327dvPmjVLGaShECbexYkTJ6hred69e7dFVG6huCjiQZUhD3zI8zz6Vnokb9KkScQ2ZcoU8SGnknIVCemZOXPmjh07IiIipk6dSsKoQVM8qJWkloKaP3++Sy7qskXQvy1evJguDqnu378/vZny54tkc9iwYbx1TraFwBP/qFGjDMe0XY8ePQYPHhweHq4HwEmWiXzMmDH0sR4WlAUWLFjAV8jym2++KUVHzywfGjt2LMnbt28fVaPKM7pKpOcfN24cEkWBU86dO3emTuUVotWvXz8K9jHZw/kY4rXXXntUuSj6SePGjXWfZ555JoZclJGU1h3jpLnHzz//HItc1IaHQENOkCBBq1atlA8ji7dcNM6EJL7QsmVLExe18cgjlrno5s2b4QaHDh0Sp1BT0fBQWXjetm2bvBJqClBQrl27xgO6ploI3bRpEz6P84mCBw2oodWrV0cbRrGuUaNGihQphP6tXLnyjTfeoOP45ptvPvnkk1SpUvFMvaN6FihQAK2aykVFTpw48Z9//mk47KmiyBLmhRdeQDFdunTp0aNHGzRoQAB4jvoc+m6dOnXq1q2LLCFUZcqUITZRYVHi33rrLWL44osvvvrqqw8//JCofNjzwyeKFi1KGm7dujVnzhxy5DJ5EvjHH39Eh161ahU54i0DueGYq6tSpQrO4sWL//LLLwULFsyXLx/O3LlzK2YCMShbtuzJkycRZpJNJF4lsmfPnrly5Tp48ODx48cphFdffdVzEmg4CFiePHmSJUs21QGZTJ0wYQIFvmzZMnKaNm1akkcd4X/mzBniJ/1k1nBsJUqZMiVcTr7oMipPIFy0adOmlSpVqlat2ssvv4zz119/9SSPMSk9Ohwhz+KkZhs2bMin4VeGg0NKZTGov/POOzVr1syePXvChAmRZxUDzPDZZ5+dMWPG6dOnhw4d+tRTT+lcNLoWgQ8CIB9CEUfzyJs3r+HYGgep69ixI9n56aefCJAhQ4bnnntO0mMh8BBLGhfh0XT79u1LMb777rs4y5cvr5IaHBxM2c6dOxfNBqmmPF1yXa8Anf7999/5EImRSqcc0KJSp06NJ8WSP39+tWoaXSVSGpkyZSIY9PuDDz6gCooUKUI5U7Zdu3YlzfXr10eobLtljyoeYS5Kq2fs031iyEVp6bSpuNlCYnPReAHDKMWun7r3lovGpZDEF2wuGnOgZqBIoM/wn0FZ+UOyYGFb7sW5c+f03xIGjSIkJCQuExzLXBS9Ew5JKYgT7VbWQsmbbNBVGtKNGzeEi0rHLSuo6GHoZKGhobK4ah8ZfXAA61MmNKEusJT06dPLwvXChQvpOOgfkXhqXM7Qt2/fHk819YB2/vrrr8uzbPzTN8ESPmfOnDoXhQ4RoVqy4yfZsmXLkSOHfBFZIgao0Z49ewzHfhVeZc2a1ascwbLSpUunnDABmQpxTh7kjbfKCaMgwLp16wzH2lqSJEmeeOIJcRp3x3i1CadQoUKBgYHyjHi3a9fO8xQSOWVStWpVcVKwxLxkyRKvsgmpJnnKCUMrVqyYallSTV26dBEnTS9NmjRwJ4gTfEkW4qKLykMIF+WjR48eNRyVRfypUqXyJI8xKT3w0ksv6UJFPSouCvr3748TaieriPv378cJKZW3iAEkStfVYE06F7VoETBtQr7//vvkDlmVBfyAgIBEiRKpFUsKIUuWLCpya4EHEFc4W1BQkDjFkJKMFnwFTnv48GF5xfDDK6i7V2XlEseOHXPWk2TConv37jyTNTJoXYlkDWezZs0kd8gYzowZM6pVaNE8Nm3aFPMEP3TYunWrbFakYY4YMQLF1PlkypEjRyZOnDhkyJBVq1aZpqJopyJdtI7ff/8dGaAY192F7GgAND3xISqLxDjHpl7J7o+xY8e63JtALkY64GwLxxMuyodUmtWaOeqR+CgTJpQMsk0pLV269PTp056spZ84cYKimzRpEkUhaglNdZ0GJFxCUgvio5ikRdUgyTKd9Pzzz8uvRLYVF0W9Wb16NWWIYuOcqrCwsJkzZw4dOpTKUnHyq7Jly8rkDhHSrFR4tMmDBw+aIqF86IsGDRq0ePFiDzUlfkIHQl4ocJdcFAGgbJE0/pu2XQhQW4cNGzZu3DhnQXJOpHPhKyCQzptQKBZ0Cb6O+idbMHTgI73f9evXCTZ8+HAZUHRQX4xZFAvVeurUKevSiA7kgpECIqREUQdNY/r06RQCded8Cx1JIvGSF9lnRE+u3lKtrVq1kol7JYGy3caZi7psU14JiSd9C+PL3LlzpW9xWePRQTolBlPR8fbt28fQRitQ+ZJb3M6ePat89KIwLLs1l1yUCGNo4enxAaq46cyj6sxpPsudoDcWOhNqU+1ajTPEMheVjEFIxEnfJz6IGiLLgzKEhdTKK4TVcHSCwmMFDDnOnZGN+AK9hiw8Dr6LXLly4bNs2TLjLjNs2LCh/hOq+4cfflCddfHixaGj8uxM9kCJEiUUbUAk0Nq//fZbPUDbtm35FR234Zjy4blGjRrq7dtvv42PVwYMGVD5SadOnaSDpscXfcI5eZBehgqV94oVKxKgTZs28jZ16tSQNBUYvVwWgqTnzZcv39NPP60UON00nCeAfam1WZlS9fZSDROBrFu3LlxC5aVJkybEWbp0aRWAMV541P/+9z/rqDyE83lROQ0iG/INyzzGsPR0oTIc5111LmpyghQpUlA48tyxY8eECRPqe031PbrWLUJYLkqYnhh0CL30vvvuO8LIhKVbgTccam7mzJnVW6ggb2UP+ZgxY6DBKiX9+vXjVeLEiWNuz9MlF0Uw8DSpehaVKIaU0YRU4LRp05Id5RTuSnXEMLUPF6gmZJuMDxw4ELqeM2dOigWnbimKrqlp06bPPfccAyLcngekSDoWOtgGDRqkS5fuqaeeWr9+vWxIefPNN5FAhIHnatWqqYZDZdWsWfPZZ59VW5ZMiC42w9Ghff/993QU0J7q1asnSJBAN2CGAlquXDm+RQz0qHSGkDQ9Zk+4KP05/S3B/P391ZQEqifFkjJlSpnUIBnknU+jQkybNo0Pqe330QG+99JLL0HVUK0++uijQoUKSTyy81zm4JSuEhISUqBAgVq1aqF4uK0ayFXjxo3x4VVbB4jWuMtFUbv5ObElT54cp5pNE0BQ+cqAAQMYH5MkSfLee+/J/BSUQArhjTfeIEKC0UN26NCBePCUXUUK9DDly5cfP3483RFVlj9/frfnF9DsCxcuzE8oT3rgIkWKmLio2Jrq3bs3xZIlSxa+K1O9AnhOpUqVoFKUJz0V/ZWMgNEl0mXhM8KSL4YbAtMBqsDIea9evRhfqFNyVKVKFQoccZK3JIMEJ0uWjA4QMSMqqR1kQOdpEJgPP/yQAGvXrkXUGzVqZF0gzoCY8avatWuTBooLUX/33XcVQ0Mw6tSpQxEtWLCALpcCJCVKXPEsVaqUqCVQ2Rw5cmTPnh0nZS4xkHeqtUKFCn4OGzxt70IO7up9rEWb8lBIPOlbDMcKUMGCBWHvc+bMITsMf6+88grxq7lpl0CpozegMdLPb9iwAVb84osvMtzs3buXeqRApP+h6g0HeSbyDBkyqOl7w7JbU1Wpc1GGOUoDASCkt3X6GAJJW716NTRKJmvoXYVSCeFHYGRR8KwGURWoLERO0deHmIsiYTq9NBz23KPjonpgiLhsykWyCSDPjIjO00424gWiXM6bN880myKTncJF9aFFgRGazpRB6ykHxNMtF0Wd8nOydkPXhuenn35quOKiVatWVfTPQzDwyCZDhkx9jtaUPFQinJ07dzblXa3wm7gooN/kJzKrOnToUJ7pRikEr+YddTCcQ41kKczbjSsmAlm8eHEUSlNe1CAhELIt87sWUXkIZy4qdhTVioTAZR5jWHreclG9KtEGlMQKdC5q3SKEi5rUR0QXT7WeAI+F60qm3Aq84cRF9cQ0a9YMSXae7PT2dLEzLLioy42ILivRmYuSEZ2LSkUMGTLEcOhhUzU82paiZD6CokDFNBzKbp48eXTmhkLv59hGLs5hw4YpiaX8+RVOtEwY2vHjx1E6hfbIPAW1oH/rgw8+mDFjRnQpsYgNvZA6VSFlVZyqESc6pb6mjR6PU98f7uEeXb5IU4XhyHKKAJGQ0xDyjNiohZ2+ffvCB6zjzJo1K/xZnmloUAX1SuYu6V6UDyoK7f306dPidFs15FEogf5F4aLQS5ljIgw6OkWqNBkatW4L9JdffiG8OnQqJFn1A7Rf+hM5gaJ3JsOHDy9atKhq3bA4AsD3LIoCyaHrDg0NFScaFzHoXPTUqVPwGdWoYVa8hZ/I/Oy1a9fIGhRL3jKsC9+QixJcJtJl4VN9kP+vv/7apDDQGaZMmVLpjXxUDr8oywIo0DBDBgLYlKxSQOYJgLxJAHoenIo8b9++3QeLa3S2+sVy1CNx8iFxUnEIv5JAMpIrVy74m5rfIfuER0q7du1KFgjJUOvnOJ6g4qQt6y3acLVH17pNeSgkbgUYPQfCrDazHDhwQOg9ekt0M1YCMsXAqkQaWRL7ZCqFdDWKiwqEPys1w6JbE5i4KLU/fvx4fGwu6glkCXDFihXSeJFDWeeTzk2W7tUcnA4CyAUoQkcfYi4KhI6rKXM6F2HkhmP7hK7B0/WLwsTYQ3geKALZakIJQkTxMWmrNuILvXv3ttAnouOi06dPr1SpklAy+krPueikSZMIYLpuVAYb2fsaK1zUcAzAcvTOz7GH0OUeXdJvzQCduagMA2raRY5l4pM3b161adlD0At/8sknHTp0iIiIQC+PORf19/cnQuuftGvXzs9xYta09es+cVHrPMak9GLCRbNly5YpUyY9Np3+WbcIl1yUsRl1Cj1MnGXLlm3SpIk8uxV4w5KLoreZaHNswXMualGJHnJRqYjg4OCkGnLmzHk/8vWAQCpRPwUtarqSHCgBLU5tzJam9P3334uTosaJNmyapmFIRZIpPbUxEoaPPFvP7bqMjfEafoieevMuoA0Eg8tJAIgrzVOdR4K18lYl2PDmvCjkwdQeS5curbaW/fDDDzQftTMCeVN82CWkG4ehKfIgkx0CFDWTaot8Kr3c8KBqLLioIrTglVdewUeUezlLMmLECFWY6Eu8TZUqlWiNJpoh+PLLL/XvokpC2xQtNBzVzThLtBZFQYsjHt1TCI/iojRemrlKGMKA4BFA9hh/++23ZE3f4ckP1ekG50RaF77sSFIKAzlKnjz5Z599piePiiZMlixZFOUWkVYBKGS9BqXPoeNVAfQveoIZM2YQw4kTJ5TP5s2b33zzTSkBhI23pkIWIVFiw/CEs2LFiioAXNqkGnnCRa3blCdCYnggwDL3pE8zSVNl3LEoJdRywpjs2YopYKXby0qvzkVFPVNc1LpbM1zt0aU0bC7qIcRMj77AoI5AGg69gueQkBBI1tq1a3fv3u28f4ru+qHnohs2bNA5JA17uePkp+HYA8Oz2lPBgKcm7+WVvjufAsJHHXexEb+QwUPXEgRyXM0lF+3bt2/ixIlVz+4VF5VxqEyZMnoAlFQ8ZXtYrHBRtQmcPhEVQc1fmpInnaD+LT3vhisuyrBKXoTIyVfOnDkjo0X27Nk9v6kIdT9XrlyKscQKF82XL1/WrFnVuUTBuXPn1Jw0hQ/ZaN68Od/q2rWrRVQewpqLWucxJqVnxIyLPvvss7zVTwro9M+6RbjkooZj+Iff1q5dm+KlgSiq71bgDUsuKoWjb6gzHLOhMb8Z3EMual2JXnHRxwpSifqOOOdTfEpIIIQNGjTgrSIVcAacLqchJJ4WLVqIc/jw4bqq5xIuY0OhhwG+4wT9/LxK4Zo1a8SOndpdaXjDRUXgn3/+eXHSlCpXrqzeilD5+/sHBgZ6eDxSFovKly/vUr0WlqhOoH366ac6hXZbNRZcVG8asiIEqzHuzi5RIM7lKdP3LmmGVLrqTKBDbgmDCTLVNXDgQN3TlB3ZlOucMGEUjI8ff/yxxSdMiTQsC1/au1IYxowZg7N9+/amYLJrSR24NXFR9EY/xx5pcVKAQp7phXyzHcWorR/gN6Fu3bpErlu2Mxz6LZ4pU6aUUUm4qH5Q35lnesJFDcs25YmQGB4IsOw50g1BSyTWo4bsedFPkgNJoedc1LDs1gxXXFRUPpuLegI4J+xJP6kuNmWlE4ZnCfNSe3FXr15tmqZ8FLiosErapDRORhdFKU+fPq1nW1aKoamEPHLkiKwpy6ELxFQuKfXhAgwb9wPUIB0BHEa3x0V9yTShSy5qWlYqUqSI0nLCw8P9nGyr6LQBCcmTJ0/ChAn1ScopU6bgIytjscJFGZtV/AgnWo7YrTElD/lEdebT+rl5fvjLL7/IszMXhcZ88cUX8kyvqvxlMPDcOpnsXVE7naZPn+4DF3355Zf1IVx2DanDroajtBs1aiRNLyIi4tVXX6VtMtKjCiRLlkzXJExReQhrLmqdx5iUnuGYr6XilFSYvmXNRWVLrdqgZdwd3UVhtW4RLrkoyahfv75LgytuBd6w5KLkiOdy5crpFiC6du2q2KnPl2N5yEWtK9HmotHBEy4KUBrq1avXr1+/OXPm+GnXvVpwUXpImmq6dOmk6pEN/VYtl3AZm5yKtN7sffv2begEyvrUqVPlkPPYsWPVWxMXrVix4jMaTIt1ssAizI2iMG0qFpNgoGjRouoKLkjIM/dC7bxFq4ar+DnOTjdv3tyUC5FSWcWiz8+bN6+ukMUuF5X9lrK2tmDBguhK0hOa8e233+J0NttjAXp7P6fj63p2wsLCeFYjmgl0WX5ORw1NcOZCFoVv4qKyUZkwpjjFWr46dm7NRQ3HnLIc0M2YMaMP9oERKjrh6N7KzIVY9tLBEOl39+RFLHJRizYVW1xUpn5y586tJqarVKlCz2yapzYBNujcIfjARY3ouzXDAy5q0eptOHNRWKXiotu3b6c7Ek2D0UG275ruaHwUuOilS5fkalCxFCy0WzZywDDXrFkja8c0Awkm8ytItnB0WTIWIrpy5Ur7ftEHBx9++CF9QYECBejj6GXoCt99913RfWUXq0mrgIviKcbuAgMDGR6SJElChyK9NsQPpefs2bN037IiJ8tQaraMTj9BggRq0g5/+rumTZuKE7Hxc9jXUZ8T43Je3VIIYdA3qKCLqBHClDwxBpMmTZpWrVrBSBkMSpYsqRb/GSPJnTKKjf6ECqh0BXpJpZownKRPn95zizKi4sPS6VyWLFkiVcDI7dV1HXLwhjZFCmmS9EQUrJ9jR+jMmTMnT55cpkwZdY1qs2bNevbsKc9ijpUxWCXYFJWHCaDE/O7eEyMQMiM9o3UeY1J6QC5xQctB2UKiZD92zZo1Jc5Ro0bh7Nu3rwRGxlCb0EjEKbsTkQR0x3///ZfB76WXXiJ8nTp1ZI7MokXIDl59dQhA+AsWLAi5RWci/Pr165X1JsOdwINcuXKlTZtWOTt06ODnuFjFcGjSct9MhQoVUN2I6rPPPlPTDaK86rMPnkMoNznVPUUMdBJuXYliqxlhU+HJCP2DcortIgrNhxQ+1HCrLzIyomVC56Rnk2kdT7iocXfLK30XaocnV+a4jE1mZHRznSbQn5cqVeqbb76Rrlv2E1pw0datWzfQQPL02MTSNV0TsRUvXtz5/ip6KjpqwiRMmFBKibbc4F7oZE9ucpIe7/nnn9fv3UXnlpU3tBF4mt7WjPvDRcUsnL6P1ARPaAZN28/VYX4LUJ56R+ecHTkr6GysTnDw4EHnnJrgzIWM6AvfxEVFZkzHm4275yTV2OSWixoOAixW7t2SZ2fkyJGDDj+6fezlypXzu/eAsYB+jAzKtvbY4qLWbSq2uCjo1q0b7YgB4vLlyygGWbJkUfbnogOqjp/T2qm3XNS6WzM84KLWrf4xhxjRdd6j69KIumzZNVmFfBS4qOE4I4oWKywUwqnb8hZz6sq0RkhIiNpxh1Dqr2CtatOgjQcB9FaMFnTW9Aj8Z4yR5SaqWLpphgpojGJo6Jdo9vhDMjds2CD9ae7cuaUXa9GihZ/DTgY/Qe5FW/VzGONVeg8xo7szQKKk1qhRQ2ktDI3S2aVKlYo+HREiAKMUPvXr19dVZGvAChjJfv31V3pwvssYr1QfPXmGY2mUPj1FihSSSDR+vS8m4/AEeIj0iYyF+iRTnjx56KmhJQxjsD6vdAhKGIWMLyZPnhwuBwOED+PUVwvdYu7cuYkckONA4vPkk09KXlCeZLDnW99//72fZmgBSiM1WL58eTEN7xyVW9AJinKQNWtWRkEGV8bIlClTiupDVVrnMSalZzg2X4iBQdQFdE1+LsdlES16GOGWhQoVgtGdOXMGrig6LkIlGgm0SjZvU8WVK1dGStE8SKSURnQtAoor6jIxM5rKgrPhODsku8h06FukohN4uk251dbPcagGVjxnzhwx21u6dGlRcxFIyY7IrbK+azguKxJP6wlvZ8yaNYtc+znOEHbt2hVN6+rVq6REcvHee+8RQEJaVCJavtzjihisWrUqNDRU9AzQqlUrWuuiRYsk5YULF9b56uMAt/qiOJVlNa+4qOwIpctFnk2UzyVcxiZrMtSUKTD8TVTPEiVK0A+rOUS3XNQatLvMmTPTP0BX9CuIDceMpzzQoGShjy7FYsd+RESEbslGWKJp7V2uz6XnR1c23UZzP7ionLVTd5sp0HzEwIwnNEPO65rOlhuOnja6rcs0Xj/Hddy6p54dqp4ejHatc3UBvRb9RrJkyZIkSWIyaYO/kkxTIq0L38RFg4KCcD799NOmT4sJPbVVxJqLImBq/8vUqVPFELRXk7Zi4VY/iCsQnV4GR9OEO+JHktQWj9jiotZtKha5qOG4qOz/7J15vE3V//+PeZ5CZtcQZZ6HSplDCKEIhZSPOWPmh3nKPCUlUciYlKQohJB5yizpmkIIGarze37P+3HXb7X3Ofucc++5g2u9/jiPs9dee43vtfb7tdda7zdcFN6LqmPxu+MVdiNJ7uC5qPO05jZ7dKMG2YLK21aFyCogbYjEyoFwdUtop8V9UTzhom7PJMV0jEZiV1hpC6YMZUTY8hTqHe14/fr1YNUmg5jB7du3mXECtM959epVfSvRL7/8ossDPCQQy6hIkeVwQqggJIG6oLRZXP16LR7vhqNHj9rPosjGTgSbR+x3JRdmAZ6NhL9cBgI0Qw0WyEAgLwwLGFN2s2lnzpwJnLc7JxVFONQxiq3n9vQaicuxTzpUMcPAgQzLAiada5+XAh8RaEgzZsxglt+8eTP6x7Jly2bNmgUNs/jVjIrA8yzp2xuK+bZcuXKRSzNAhERQHzb41RflS4pS2kRtVWc1nbkoaNy4MREyZMigr8D7gtfUxMZP4sSJ9c9AzBtNmzZlxhP7MUyAajVJyq/7nQqKiwJxwEiZLc4Su3fvrn+eluVB3UqQBYxW3UmSLO4py2ECxDVHjhzUTnlyUvDbNbKWaBlWzlwUpkdbuTy+oFQEZqTmzZuLhVtZOLXsVrXQDNmFBHXUN70zBSmDw3bAAVwea+S6HyYhV+Qol5UrV3Z5nC3rs8e4ceNk54VwCViW2qpG7/fq1Ut9k7UU0rnxLVz01q1b8mVt27Zt6hH5KqEfw3HmomSt7+iWU7XKDC/NqyfuFdLjJKgfDWPSFhK4b98+2jxdunS64irbXBXHDoSLio1rBy7qd0wFIiTuwLgoFFRnjIFANu3D2/XPQLJxV3FRWYfXmaR8bVT76p2nNbfholEDU4os6clEhPIjlww0yJcyGeuO+Jz0vebfRBB/uKiBwcMD+3lRAwML1q5d6/UwEopOsMaBI4FPPIjuXAyChWy01rc5iBkqdfL2ySefdHl2EIhTTdn8XKZMGQgJ+r24m0qVKpWvT7eyxdrZ24eCr9RkeSp16tQtW7acPXs2pS1QoICcPkW5ka0To0aNOnr06LRp0+RYXYcOHdatWyfKtBy+sKw6OuDs2bMo/brjEwHURd9njmJdqlQph3TQwyC0ir6ihCVMmFCt5CvMmDHD9d9j4QK/XXP79m3qnjx58jNnzsg+N7fHkQlxdBYtDSJuhwENJZsC4KhTpkyBkxQrVkzRDHHjxNuExFevXi2bjMRD2EcffaTSlPP2CRIkaNq0KdwG1oeO7vyJUNxsFC5cGFZ8//799evXy46PqlWrfvnll26PBwQpGLlTd6pZp04dtVQFzZCDkY899ljPnj3J9Omnn9YJlaWQzo0vba6v08oenGeffVZ9K0SW9NP4MOQkSZIgGOqrn9gUVDYpoGH6GjX0BkkWhn/lyhUpvDLl5RVkLXu206dPD5uaMGFCs2bNGjRooEiXECS1XE84ta5SpYoaL5s2bXJ5bFOpNMXEHd2kQmg9QmhhFbJkyRJClGkov2MqQCHxK8DS47Vq1RoyZAi58Cxk3q+5UGSbjnB5rHVQXwQJdvroo4/qXFSObEA4ITNQnfbt20sVGLOyyu08rRFB3J7ruzlkKgsLC3MunoGA+ZYZ6Ycffjhw4ICcCJVduAitkE/6jlvir2Tjxo2WdRfDRQ0MHjzARZ21IgODdu3aobaKURYFXr29evUKyjJwJMC7x5yliYNAT82ZMycKVrZs2URBnDx5cpo0aVyenfOyyLNhwwbZ7YxiPXLkSFiEOAlE7Ub5FuMuouz68h2Kei1kwxkouL5Sg0i0aNFC9qK7PNvCdTNIqOxyIJC6QDbQnkVVhToi7aJTujyGtdQilV9AnOy7tbt165Y/f34SXLp0KUotLeC81godeuSRR8qXLz9r1qy5c+dCbvU1IgWU46RJk1r2xQTSNe4I310wBzjbr7/+qipLXqh3Fy5c6N27tzQOujiqv9ujC0Lk1F79PHnyLF++XOUL45I9kDD/9957jwrCE8QeD/kqwowY9OjRQ/gVqFu3rteTYDrQNSmkdCL1hT8w82TPnh1qpL6FMUvIsXMpwIgRI/Q1UhTTQoUKyV0aVq1ZeS2kr8ZHlmhJau3ymERGpNVSLSSZ1yiEZPjw4VDBxo0bK3YNPxEzti7Phur9HihnbFBxOpHhQJe98MILCxYsGD9+PIRQ2Rm6du0alFVE1LmVyBEGLl1Gt9LIFh39448/zpEjR7169SCKMKi3335bbfVC42doyDcCeCA8HKL4xBNPyOCl06GsNI6UJEuWLHISBGGWVpUjTsK0HcYU8hOIkAQiwFevXpW9tRY8//zzzs6foMQZM2aUmlasWBEKatmjS5vA4SU1stuxYwfyljt37u7du8vU4TCtiYdq2T6QL18+6ChtQnXUMeDOnTvHwNfbBx0ICeRTnXlk8Ko+vXnzphwfFWzdutW+K9BwUQODBwynT592eXaUBWU2yeBhA69P9A9EpUSJEihMNWvWLFeu3JgxYwLc7m7w0AL1Hc1bqbx3797V7Sw4g0kJvT9ym9stQFBRbrwacYBO6Nat0Wyi6BhczjVZAoUVUIyDBw9atu96BSnIdkqIihx19hoNom731xU4UJ0j4UEEWnL48OFffvnFXk1UxgMHDgRylICYCIZdj3QArccjt27dcnv2gnpdTofWUjZf5gDoGiiHX4kKsPHtuH79OiWMxEkKshOedvLkSSTEUn4ukd4nn3wykKRu3LgBZXI4QBQeHh74GIwcnMdU4ELiACYHGD65QDnWrl0LQZ0/fz40uEyZMn4/G4kAyz5Pt+28qABBOnbsmLSS/YxAVKY1gwDBeGfGZvRZGpZLhPzSpUtx6jik4aIGBpEEU+3IkSMHezBq1KgNGzbEdokM4i5QbpYtW4bATJ48+dtvv1UvcgODaMLYsWP1o4kGdtSuXXvLli2xXQqDaMfQoUMfNtNoDoDNwjm9er7ZtGmTft47EHjlogYGQcFwUQMDAwMDg/iA27dvf/XVV6dPnz58+HBYWJgxR2/H+fPn16xZc/ny5UWLFumn+wziKyZOnDhjxozYLkUcwurVq13/NaEk+Ouvvzp27BiseULDRQ2iDsNFDQwMDAwM4gMmTJigjn699957sV2cuIh69epJ+yRJksTBdapBvIFsSzZQOH/+/COPPOLyOGmHqM+bN2/y5MkdOnRo2LBhsCPi33//FR9muhMRA4NgYbiogYGBgYFBfMDJkycrVaqUP3/+QHyKPpz44osvChUqVKpUqWD9FRsYxBv88ssvnTt3Lly4cMaMGUuXLt2qVSuL19BAsHDhwkaNGqX1oGrVqhs3boyOoho8DDBc1MDAwMDAwMDAwMDAwCCmYbioQaCIO6Zine2+BGVa0CB+AOGMol1BX7h//36w52eCBfIcW7vI4s6gNjAwMDAwMHgIYbioQUD46aefEiZM2LNnz1gsw969e7t27ZonT57Bgwf7ijNx4kSXy2X3aW4QHdi5c+e7774biwX466+/xowZkytXrkSJEoXcMu369evr1auXJEkS3WN4CAHLHTFihLhWO3bsWHRk4fa4Bxg3bpylcf7++2+y7tat24cfflixYsVly5ZFU+6LFy/+5ptvoilxAwMDAwMDgwcdhosaBIRTp04VLVp0zpw5sViGW7dujR49GsXdgYuuXLmycOHCMeyl96GFWAEJxN1ftCJPnjzly5ePjpTnzZtHBaP1XFn16tX9OmGPCsSYDZxTD2zWrFnr1q3lP0z+1Vdfjabc06RJQ/rRlLiBgYGBgYHBg47Qc9G7d+8eOnRoiwcHDx7Unbn/+++/J0+e3L59+6ZNm/bu3as7iebW6dOnt23btnHjxj179kT3pjiDBwWI04gRI9TlDz/84MxFDaIV4eHhuqNzumPUqFGxWB63x2k7ItG3b9+QpHb79m3dDUbnzp1TpkwZTbt/3Z71Sdha9FFB8Ouvv/bv31+fUZcuXZooUSLlPP3q1av37t0LVXZnzpzRL+fMmbNkyZJQJW5gYGBgYGAQzxBiLnr//v0ff/zx+++/37BhA6ySP1zeuXNH7h44cOB7D+Ci/BJBnVaCvsottFv5c+HChdCWzeBBxJtvvvn888+rS8NFYxGnTp0qVarUv//+G9sF+Q8WLFiASKxbty7qSf3111/VqlU7ePCgCilUqFDt2rWjnrIvMD1S+Pnz50dfFnaUKFGiZs2a0ZHyl19+2bx58+hI2cDAwMDAwCBeIsRc9OzZs9DIrVu33rt3D166Y8cOLk+ePMmtP//8UzjqtWvXUGd//vlnLmUv5fXr14V/covL3377TUjpP//8E9riGUQFR48eXb58ubq8evXqBx98QLdeunRp9uzZY8eO/fXXXy2PnD59eurUqaNGjVq9enUkrLMMHDgQTb1kyZKLFi1au3atW+Oid+/e/eqrr4YNG7Z48WL9EUSLOFu2bFEhEIy5c+eOHj2amEhmsGUAmzZtGjdu3MiRI+0n31C+SfnDDz+EVETFZhJtePnyZV93qVR4eLh9dU7tLLh586av5iX84sWLlsC///5bxhop69sTBOfOnWPwckv+SOC2bdty5crVrFkzPSZ3vZ7SJE0KbA8nPgIj/6lvVAY4z0oWrVu3TpYsmb7/QsAUpJb+FMhUPo3xx7L5gtSqVKmSNWtWFUL1EbaJEyfKJS0WlfVDCszMZulEhIos7G1FQ0mg+qPfYqCRGh2kN76vcPd/DRQx8ZKjxfO7vSNoJftwdi4boyxp0qQWn5aIn/oWqSCi5dVskgpERI1dJQMDAwMDg3iPEHPRnTt3QiNhIHIp1HT79u38P3HiBP/37Nkjt4SaApQzIZ8Sze3RQmRNVd8sZxCLgMLVqlULFfa5556TEBhmqlSpCIElosFDUVKkSJEpUyZdffzss88KFy587NixHTt2ZM+ePWHChI8//njx4sUDzBR9+uOPPyaL0qVLL126dP369e4ILvrWW29RniZNmpQrV07fn7lw4UKyIAR+KCG3b98uVqwYjyNU8EYKGVTF0bZffPHF+vXrwzMRXSrYq1cvdff111/v0aMH2vaRI0fgaZEgunCAadOmlS9ffsqUKa+99lrFihW5hNaqCGjtkydPJiPCyZ2WdHsaluqnT59+xIgRpABjT5kyJd1x6NAhPXFG3CuvvDJ27Ni6deu+/PLLEkgzvvTSS5C32bNnM07poMSJEx89elTuLlu2rGHDhlBrqtm1a1eaS4jEzJkzpWEpIY/TNfPnz3/mmWdIZ8WKFXqm0PXGjRuPHz8eClewYEHVJhSDahJ/8+bNCAlxkIcCBQoorhsUED+K8e677w4dOjRnzpyWVT7mlk6dOvXp06dnz5758uWjg2Cq06dPz5w5c6JEiagsTU3ZqA6VFRq2YcMGqkMI8UlZukDE78CBA1D9tm3bQrSyZMkSCQtJMFj6qEuXLgsWLGjVqpVuCalq1ao0rB6Z8lApSkgLI+f16tUjjrqLDBMfYejevXvevHmVPzev4VSKuqRLl46s3R4WyiXDgUo9//zzL3lApyRPnnzWrFkqi4sXL1LZQYMGLVmypFq1avrnJ19lI7x9+/bQeFJmsDAobty4gQzQyEiX/pEFeUbUmzdvPmfOnDfffJOp4/z584Tv3r27ZcuWOXLkqF69OpdkSmpIiOWYq4EdvGQZnvYvSpEGffTTTz+tWbMmVAnqQDCYpeVDmNszPyN7Xg13IYfM20gRwqy+lXgNNIgEULfmzZsX+CaXaJWKQEB3M0swb/DWQ+tgTo6tkjygcBhrBgaxjhBzUdlhK+qF27PaI2uhTGSyQRd9SG6hnwkX5SX6yy+/8AceK7dkaYsQ+7KGQWzh5MmTOhcFkDRC+vXrJ+8zuA2XalUEPgBZUswN5ZW7usobCEhE9GYVIly0RIkSsmgDw4Q8pE6dWkXgXaVzUfTpDBkyqLutW7cOaospGg+pTZo0ST2Obs2c7vbINrf27dsntz766KNIWLh5++23YQJq40CCBAnQxRUXhbOh7nfs2PFfDx555JEJEybIrcGDB5P7/v37qem2bdvgkFxCdVTKhOTJkweSzH/YbJo0aVTFeZETmeEGGeC9DmH47bffCB8zZkyZMmVETWR4Qr1gvCrBd955h6ckpgABgNoptRJdoW/fvtBLNfwhKtmzZ1ds89lnn4VOo0PAl86dOwdd9Lok6AxSg5lDh0QTnTFjBomoZnF7DgLAymS1fO/evdxVhqygYSVLlqSQ0oNNmzbl7sqVK+UumhaXn3zyiUrq1VdfhRHBxqHltCTUlwjBuvNGUMuVK6dE6JVXXqFh5cwtDBlyTv+qyBSsUaNGVFA6S8SPflERkHaIovyneWlG53DYKSnAVFUKjKa0adMqYSBxIhw/flwukWG4vXzyAHSfkMNAykbK+fPn1+uOxCJR6vLKlSvEadCggYgEDZsiRQr4sMqaBKdOnUqPzJ079/fff+eyXbt2Abf0QwqklIYaOXJk1JNi1A8bNixbtmwkiKBGPUEdp06dYsQlSZKExNXXajqayxo1algib9q0qXHjxnv27Klbty4R+vTp4yvQIHLInTs3bahvIPKFaJWKACFTx8yZM5Ec2UtSpEiRuHZaJI7D11gzMIgLCDEXFXqpNr8xg0gIygevEP6orzKoknLrdw/kv2y0u3z5slyKjm4QF0DXWLgoTIYQ9XEB/VVfokRv4BICI5d//PEHlyiyQWXqi4vq50XRZQlRay9r1qzRuSjUgksYl7y3IG9BfU2n2PAQpTlBokhNrLPAymQVSDadXr9+PVhzsiQO+VRtQgok2LJlS7mkwNCA0qVLi+IO102ZMqXiDA0bNoRqQj6FaAnlgIbJ3Q0bNpCyrFjeunWrUKFCdJbKt3fv3lAsNDl9kyqkDo6ktmXCGElw/PjxKgK81LKClyNHjieffFJdEplHYHQqpH379oQcPnzY7RnvGTNmhMwPHz5c1nCgsoQE1WKgTZs2VEftyB0wYABZqAVhZpJHH31UlgEBlPWJJ56QHqd5EyZMmCtXLrV0L+5/VB2FlSkiLRWkOxA2oXadO3cmQlAbR8maJqpQoYJSm3bu3PnVV1/J//Xr15OgvrDcpEkTdCwlonBI+WqgIlB++l2qv3TpUr/hLVq0QPvX1xAyZMigj2KIKw/Kf6qZPn16xEPdpWxKqJzLhpSmTp2aHlfPnjhxQr5VqZB69eplzpxZ30yORBEi/6dMmSK0GVF3e74pcIlg+2zc+ALdGFgk4q9bt+6FF17QDzlHEfLNJTpYB6OAMaVzUeZSpjKLSyGGKrIkX4WYXakdIu01MOQlDBzB9lpcy5rh1qxZs8BXF6NPKvwCseE9qJswhI6WKlUqcntqdMRiJ8YALLXzOtYMDOIIQslFmTIUvZQQ9DZfXFSPjH4jFo9gGrt370aTllvqjWUQ6/DLRelfLnv06CGXEDMuld8IuhiqE6yx00C4qCwLqCV0CxflXVugQAFCypYtqzaBRwLffffdoEGD4BX6IlLz5s25zJYtm76YFjigkTw+ffp0uZTlSuWuU1Tz1atXM1IgimFhYZRBbvGOSZs2LZr93LlzJQRCTjHk/40bN3Lnzk193Z7zus8++yzl1A868l6Hoem7HyFgJNipUycVAl8id7WjnsdTpUqlR4BhEmHIkCFyeeTIkWTJkuk9BZ5++mlF3WXVkc5Sq5RZsmSxnD71i2+//dbiPLZx48a6Q5RGjRqlSJECjk2/d+jQoWTJkmohV7iTvjIPZZVN5nJZs2ZNuJa6K+cqaTrVCBAnadXAMXnyZBJRy4wW9O/fP0GCBIrciujqugK0EOqofz0R7t29e3dLUl7DkRyYeeXKlVUI0y/Rhg4dKpe0Ekz1jTfekMsGDRpkypTJ68Fjv2XbunWrJcLMmTMJYTKXS/GOoz5OuT3rookSJVJMGOFBLIcNGyaXovuq3ePxFQzDoFba6TJ9IT06IKMsmlhH+fLldS7qFe+99x5x9KMKvgJjC8H2WggRAwLgFdEqFc5YuXKlvr0lVDh48KA+HcU/RKt5dgOD0CLE66KbN2/WTeDKgqfM2ox8fY8u7FQIp5y/YoYVQ0dg375927Zt40+w+/cMog/BclFQqVIlCIwsbm/atAm2E+xCd9S5KEAaZU+XKOvBbuzZv38/tRa/FNRO56LIMBp5woQJZetLsLaLoJQ5cuSQZahr164VLFiwVq1a8i0TNT1dunS03ogRI/73v/+NHz9e/4C9ZcsWcqxQoYIwAWqUMWPG1157Te6OHTuWu7AyUm7fvr2FgcvWx8cee0z/qAwbgRTpW+Iht4888ohqK2l2tZ3VHcGy1HFQUuBSsWW35+sDPZ4vXz65lI1Vas2NVuVSVsACBIWh2Iq6uD2sO02aNGphmZrK/u2BAwe2a9du8eLFel/T9fSUbsYJ+YQLyYezu3fvQmK7deum7k6fPp3U4HhyKcvgpBx4gd0ezTt37ty+7tKD+hbWgh6oMiMDuXLlatiwof4Iw5BGoLPoEb/hskVZd7oj2wRQK+VS+LkQSASM9vGlvvgt2/Dhw3Ve7fYwWwRYfQQpUKAALawT3Z07d5J7mzZt3BEfO9KnT6+EEAEOCwvz1XTxA7t3706WLFlQe/sZmM8++2y0lej/EOtclBnPTju9BsYKItFrIUQMCIBXxCIXhXuH/LMUL1xmpHhskF8+BcZ2KQxiDefPn+cNC/niVz9axUscXX3Xf6F0V3Qq7qJFoLEz0UXFHmewCLGwog7q5zzPnTsnZnXdHius/EcHlVu3b9/W9+UK+C+6i3DamGwIA2dEgovCJKtXr/7kk0/CQHidqJiBI+pclKElf+BRaM/c+uCDDwIvwLZt25ImTapWe3QuCnsRuz6ItCwAtmjRItgKMl+g4g8ZMgQu9+6776pVJjmMh5ru1bOlHBZVWz1lfVWt71WpUkUnzBYsXLhQX4x1e+amDBkylCtXToVAKV0euz4qhBJCVNTRULdnFQu2rHYBiSkgZSMXQAUJUauv6E8pU6ZUu4InTJjAXXWsMRCI+xOdLk6aNElfixs6dCiXc+bM8fq5oXjx4voK4aFDh+BOihtv2LCBZ7/44gsVQaiUIlfQ5mBVYfrOcuZWB5IJE1Zn3oQ36vtjpZenTJkilxbZqFixonO4O+KIr77Fl9aj1mpQyKXUUVpAP/+p4LdsgLYtXbq0upSl+7p168olci57E/RkYRfo9LK/Wg6Lqix4HOnSN5bHP1Bx2bA6Y8YM5Er3y4oSMNcD9bp0ezq6V69eLo9d8R89UF3/66+/yicnuvJHDTJBiaM1gfo0wK3169fPmjWLXzk+rWBhHT/99JN6XG2GJ0cJsbiT9YpTp07Nnz+fCQHBs3PR69evK/vkTOOkyVtGJmrJwmugnv7JkycXLFjw8ccfnzhxwpL1kSNHDh8+TEOtWLHis88+0z+m+Ko+zcVLhJYkMq06e/ZsukPddeg1O0gBlU4OPtAIzCFcql6jXhSb6ctuAzxYAXB7uonG4TVnt/goHgpofOZG/dMkM4PlXAlxSIGq8XLRZ3u3Dy568ODBYNeHHbKw448//qCalSpVIuulS5dKrdEnv/zyS+oi1hCcq0kXUEJeQ3T0xYsXZa4j2apVq5Jm27ZtSVAdQ3DAzZs3V69ejcDQgxaBEThIlFTZ7VGi1q5dS/G8miiPhBgjfrz3pVT6x2WEKnHixPLCAsqwmT7WFCjtli1b3nvvPV5/9jey83DwC5QTxPKTTz6xjxSqs2/fvnnz5qGTWLoy6vk+5BBzsN9HuM8Ev/zyi9xCCL+3QZYPb926JZtSGTLqQQf/DqFFiLmoEE5oiYwWRI1LeYExEfAfkimvQ0aj0FTxQMAjaDwynOSUqfHpEqcQCS66ZMmSoIifHcySlkyD5aK889T0igSmSZMmqH2h0EtXxIlHd8SJQaF5vMAU/UNuoaO6O5AA0ahRI33ZSoFXDhkNHz5cD1RKBnwjd+7c6oUkC6FMGbzDCCxWrBjvIX3s8CpSLyqaSy0GCpiGdCJNR7/++utJkiSZOHGi8qvxzDPPoES6Pe9Lt4cq0JIU3u3RqNweIzf6iiVAYXrxxRflv+wFVUdhQe3atYsWLer27BoNsK3ef/99fQ8zJYEAC5VixqC+sudWXxgkUMovq8H6annz5s0LFCigtMBBgwbRLCgNqoJwIV1UKHzGjBlJ0BfJt0POSFv2LSseyIufu2gGUFZmyE8//VT/UILI8SAhvICpAuUZMGCAYv60XsKECaVPfYWDOnXqUGZEQo0OpBTxUIUpUaKELMxSKlQcyx5aVVq/ZWOcwrrh1fyXd56cHp86dSqFQcBoNJe2Y9/tkTqIqDoO2rdvXyIoJUyWuJcvX86rIb46mmZqKly4sMuzcZ0JTXxWoUxXq1atSZMmTKcocPB5Zf4NIZEFIsb+YA+QXjRIsf/ctWtXt+fjHZIse0BgMvKqRWjlw9CECRNEVBgjDRo0YIAzIrJkyfL444+rKc5tYx3ffffdI488QgilUh1EpzA6ihQp4rzCSQHeeOONWrVqocejHzOTi7FleYoqkyZioIyro8dTL71ZAOWxB8r8xtjp1q1bp06dZs6c2bRpU2YD2blAvsieHKlAixWbAq4Iw2O+qo+0kxpDxuUx6kNpH3vsMQSbZNUODq+9ZgcF69+/f86cOYn5+eefU8JChQqRGpf16tWjm5h/CHniiScIqVKlinowKAGQL5WMbio4ZMgQqsxw5hHGstvzAYjJIX/+/MJJJK8UKVKgpw4bNkzsoktMAUSI1oDywR8oQK5cuRykQoQtZcqUrmB2zzpnYQfaBbOKNGO7du3437t3bxSP1KlTCzt1qCajg/aBcyISvGUQP1pG9jchjTKDPfvsszSjxQ2VHcxmJIsMwIF5bZF4hQoVSEG9UHxJFL9itf7RRx+lQ5UMUBL9K0MkxJhZ/a233mLg8H/dunX8oabyLZjfoUOHSteInKCW28eagHBKRb4MPZQ3NAemYpGrQIaDA06dOsXAp2uQHF7NvF6ZmtRd3gjUiw5F1afdeNvWr19fpvoo5mvA3CiLefLJgwEi9FIUAzHHw8j6XYN8tRRHm7x8iUkicqxStwASrQgxF0V1EGItK79CrOXrF29BBItL5gs4qkQTxYUhJyx827ZtBw8elP/2j0MGsQgkmKkBvUeFvPbaa4Ts3btXLsVYkTIbwwuPeU38WDD1MxKYlyNhbADOA89htDAw+EV3J5eePXuqCGLOVzEEsSirZj2UXZ3R5cuXL6gjIsJFUacYz2jk6O5cQneZ3OGiurONtm3bWliHXzBTML3yWiV9Wk+/xTwOqUCxkC+st27dQgeSbzqMJm7pJwPr1q3Ly48GF0+YaPzqPe32HOSDRShqmi1bNnQdPS8SJD68jvmI7Hh5yPkcXk4jR45kRPNuoytRiXgTyyuWkgjTgC3IO7Vhw4a8/NT3YLRe3jRqUVF4lzrnyXtU7NyQBbIRYHOJPi1rZahfvDJ51eXNm5dcJk+e7I44kagOtdK8NIh8EpZn1RZiGpNXsj7DoFuULVv2yJEjKI5uz3q46792iVGbXnjhBSqrB/oFGkyGDBnU538kRz3Oi5/XMyx9zJgxtBv5kqNstD5z5gwCjNxC4KmpSCwqrPqkjUaojrb6CgeZMmVq1KgRM6oIAzMwfaQOmyFUCBLdumjRIl4/NBfZKdkQ5yuiZfot29dff+3ymB2iYWUXrtg3ZnKgC5AfsqYwarxwicDoho5Kly5dqlQpdSl2sEifvLxuDYgfEOVS3+2JfunSDIDJ/KO+98kZZrVFkz66dOmSbF4VLur2KCKoyy5t34Tbs64i35LcHhrJdKGWSqTveERNEXbWMW7cOJfn7LReeHrQ4s/JDspfrlw5Ne3ToeiUiovyTmE4cGnRj+3N4isQvqdP7xUrVpSpDwE7d+6c7BCpVKkSw5mhhy4eHh7uXH0eRA4JQVblMxm6CsMkR44cziXxCnk38dKUSZLEZVmYEGWAnVnFpR2rDkoA3B4ZIDX1AY4mTZUqFZSD4cxIPHnyJPMPj7Rq1YoQRmWbNm0gabzOGHE6F71y5QrTkXqFieExZePa7U0qqE7JkiWzZs0a4PYWv1n4AvXVG8Ed8Y6TwvuqJrdmzZoFCVQfbXlNzJ8/X/7LcfRA9ugyfcnkL5fiUAAyuXv3bhFjZ4miR3jL0yMUST7tyekPfRdVJMRY5mSlzPCK1z/UAiru0vboeh1r8mWfAqsQ2UrDlCKXgQwHr6BT0CgWLlwol8zh8j1LTKzxys6cOfPbb7+t4kMKkI1ixYrJXBHpfA3cEYt5TCnqDJf4JZEDSrIKaHGuLhCXnOoknWxrFTcoMVDs0G8ohzCId1Cphm6XEgEVG0UCFHpVSZpPqLwAldcY7I47gCnxEmJqQJMYO3Yscsy8Jh+u6tSpg8LKTIEWyyWThTgkpK/lFaIjZ86cyhJMgOjXrx8Ppk+fHvV0x44dMi/z/ps7dy4T1qRJk8TNKW99+Bt0EUbBZVhY2OzZs92eeT937tzwFt5b6L68q4LiwyjTTJokiCYN1UGemRBTpEjBmwAuSiBvFBQyOBuTZrAuiJggunXr1rJlS6kCKeh7llDimZ2pKVVu166detXRvK7/ehZp3LixfAWQRQ9IKXM67z9eac8995zuH1JOaeobdAVi8Jaa0olMVWvXrnV5dlTKMQNRGiiJcg1CTV2eQ6cqhLcyLzl4Ds8OGzZsyJAhuhG/zp0702iKqTK0yQvtwe8HaR08Lt8CyBdehEZVu3ZtIZ+y/kOO4qYFBli9enVxvirPwvbpuIEDB/Iup6E6dOhg2UaFZMK31Q5VniUdtSInDnXoJpTywAvs9rxiSblAgQK0AGXTTfv06dOHLAiUzUtUR2qHuMrebFkqpKZSO3oTzW/lypVTp05F0VFrEb7CAQ2VLl06VWbpfUVRaAE0Ksi80G+3xy1T8uTJK1eujDww3tWXe79lE0dKxFGvMdF70J8U4UcwsmXLNnPmTEYiraE3hahryqKSO0JdY0To53vjH+ysBhFlrlPHe9BQXdo5bTsVcUecAVZc1B3hF1fX8gcMGKC0cHr21VdfvR+BO3fuyBKKsrBlZx3Xr19HVJj81ducmYqpXreIZocsblvsuiGrLm2PrhzDjhwXpTWYIRE5VRc5lM4rSSKg7Lo0+2oBVl/Ioe4sWpba1AwcOBeVMx10hwqhfwnRpxGGLSHyGdEdvAC8//77vOzua6hZs6aeRYUKFXSuq/D666/rXJR3OlOcvg+fCZMRrS697tFlYgz8feo3C1+wc1HZk6Uv6nqtJu3PxKI+lzPPqE+0gXPR1atXu/67R+mpp54iRG0r9StRMnbU48xpusxHTowhkOSiBENYpX6AxcJF3d7GWpEiRaDZehxGtCg86j3idzh4BS9Z3b6A2+NRplatWqLhyPK+ZX+4ZKScn0UuXwO3Rz2TNT8VIrZ4ZNZFboV8bdu2jeY9dOiQLIq6PSyMQao2i4WHh8su35gpdrQcbkYFRGKomH2eQjr//PNPtSisg8hXr16lLeLxh/CHB0w6EAA00d27d69fv37VqlULFy5E/27QoEGwSTFneT2hEQhElhhdjMDIHT/m2ePHj6tZFX4iO2H+jgDFC+TQlAXQMOXuAt4+evRoXsz6Dme35/Mhred38uX9oQ4DCBiAvOGOHTsW+AcdItNEKj5V1hVN3pSWYwPkaPFuwrNEC3ALK+Lh9cucM5giIEiK89My9kPIcGniWKaX/PnzQ7Nv3LiBXuLVjQEzkrNLHiprP4gVCGjGw4cPM+NbLOzTRwcOHNAbmdrt27dPqaGIrt6YEk6zU2U9KV/hbs+rRZdM1FbUF/1wmix664/QOHv27LFvvHQuG11/8OBBy7E3ymPpBZ4iWoD0kjLEb48Lbh+sRtV6y5YtooUrOueVi4r9bZ2LIlRookmSJBGJRdKKFSumekf2ED5vg7Jo5ZV1yKcTNWXNmTNHV3y9Qr5wqSOmAst5UTlIHDkuOmvWLJiGvSJqK3j//v15BLHX0/FbfVGCdU3OUuaocFFZd9L35ojXR32NKCgBePnllzNlymSvjiK3Qpzs07Kdzql8mVfFSZjuLjgktoucs/CFQLio12rKfpw0adJMmTLFMpkEzkXFcbpuu1hyV6dL/EqUhYvKcSdl0y5yYuzWGpPXrhRJ95ln56KWscaL0vXf/eECMUOovmX4HQ5eAcVFMn3dzZs3L/TbcgRPLFkoBh65fA3cnlcns5NuvV8WPGV0oFJajpKqg5M6eHfLwmGMmbI3hrYMQg/ZOKR7DVGwu6N4CME4R1PUjZu5PR+qHaZvg0gDPuayHb59CNGiRYvOnTvHdikM/j+8shpUtPnz57dp02bp0qViI0qRmQC5qDvCx4/4zpW9ABIuRy105mOHV9aBIos+nSFDBvmUU61aNbXL1BfkIKvluG8IuaisrtgN/yjYlfhAqh8rXFT/ChmUABQuXLhChQoOZQici7o9rAZBGjhwoBwSUVbQ3aGzo+uQhS9Emou6Iw6ig2LFiumLbHYuWrNmzYIaFK9DzomZJ08exZ3q168P01NbcP1KlDMXjYQYK0An2rZtO3XqVLGIzn91yy8Xlb3Eus1CwejRo13a2f5IcMKrV6+6Igyk23H79m24NxEsCwxim1BZnXDOl1ml4H8h++AM3N64qJyXlNGxd+/en376SfbVM5nL9l2Lh4sbN24IEeXBGPsibLioQegRHh4u7y39c4us/m3evDkWCxZHIF5Y1HdTQe3atWPXe3t8xYcffujyHH+N7YLEAnjfI1f79+9n9OXKlUs/MWEQ67CzmjNnzlSqVKlz586iAcgWzUhw0bNnz6Loo6Lxv2nTpnJMyx1x2k0ZFfMKX6wDTdflOSWOHqP7IvIFceysdkgKQshFW7ZsSYiDEVS7Eh9I9WOXiwYrADlz5syUKZPD/pfAueiMGTMgSGodOzq4qHMWvhAVLur2nA4gF+6SnfLIbeei0OM3NSDn6tbYsWN5tkuXLrKzJkuWLOptEohEOXPRSIixJEIhqbXsTpI9ukFxUXlEuSVXkKOnyhV8JLio+Jb35XkIwZZD4xazhXIUSNmBd873jz/+ePO/0E+9PuQQI7r2Pbpet+/Jll19lkZ7F2s+jLiYNB9ruKhBtEB2eqRPn75GjRoNGjRg0qxfv37I3VU/uGDqLFu27KxZs7Zu3bpq1SpUySjaHDbwCqZasYKAPud1d278BipLjhw5Ro8e3bp1a/MZKK7BzmrQt1KnTq0+RUeai7o9toUIX7Fihb4N7/79+4kSJUqZMqXdncbixYvljy/WwVCShQuolK6p+0KtWrVcNh/CIeSismaoPAAr7Nu3T3iLXYkPpPqxy0WDFQDhaevWrbNkvXz5cjkhFSAXFfvzkC4VIeRc1G8WvhBpLqq8gNy9e1fsS2fNmlV4e+B7dAXt2rWDi3bu3Hn8+PH6F71AJMqZi0ZCjN0Re+aV65pIcFGxWejSfBAIRo0a5dJcxEWCi0JgkiVLliRJEkscwqXAYn3AcpIcRcgVYZswcvkaCMRliX7OU6zGIgBywFs/O8mQ4ZYaKceOHRNDP0H52wsJDBc1iC4cOnRo2rRpQ4cOXbhwofowb6DAjHDgwAGGPdNBvD8aF1v46aeflEU0r17d4j1u376tXE0axCnIkoiyJiVGTdBc1XYS0TjnzZsnl7IIY9lW54uLwk8IT5cunVoLElSuXJlwiKI+54wbN04ZxXVgHWImLUOGDIE4nZPNfqVLl9Y/rosaqraEeeWiYoHMQvbsgeIRN3HixHrgb7/9RkzhG16VeL/V96sEW3rNAcFy0UgIwJAhQ1weo4A6Qdq4caPaNRogF5XDvYoo3rp1y6VtmHT7kAr4jOWkiQP8ZuELkeai3bt31w/5t2rVijhyXl3MremGlBwABbVsYtLhV6KcuWjkxFhc8iguKjxfd5oljnD0fbD2sdakSROXzad0w4YN6RT1YOQ4oTz13HPPqe+/1KVXr16yFipW1i2et6dMmQKrV+vDhotGGnfv3hWFR0yN3LhxQy4ZcX/++af8v379ujvi6wCX0i8XLlyQu4jfPQ0xU2zDRQ0MDAwMDGIaomV26tQJ7QFOIs6TCBk1atTRo0enTZsm1kE7dOgAsUQnQEEkQvLkyc+cOSN7q9wRip143LEAhRU92HIua/PmzbIeAkscNmzYzJkz69Spo6+oiFss8R5sgThzgpEGUjtUnxw5crg8xqIhUXfu3CEvMTFKjXbu3KkSDAsL0x+sWrUqgbqlZV+BYjM2derU8MPZs2fTngUKFFAHWcU/isX2td/qS0Y69xDflcoTpqXXHLaxCfvSPW0IdVQmoNwR3SenE2mxYAUAnTJTpkxCR7t27QpjeeONN3hKdE13hOFi/fCYQHiIWrUWe/XSerAjyF6qVKlgUHv37pVn7VJBhz766KPwhwB9RPvNwhfsVRCr/vpHFq/VpEF0n5YQe+U4Sqg1MkCTrl692sEGvggMxIm+o0doMUimbpHLWaIgqEmSJKGV1IlQsWebOXNmlUIkxFicjr744oviOpV+4bJMmTK7d+8WI3xCzpcuXXrt2rVPP/3U7W2shYeHU4wsWbIo24d79uxhhMJsVRy/w8Erfv7552TJkrk8Ru979uxJ4Z9++mn1CYYh88wzzyRIkEB90IE1kazeWZHL10Cwf/9+JocffvgBbi8nQmUX7r///ivkc9OmTdzatm3b9x7Xo/KOUGaNLIiZMhsuamBgYGBgENM4ceKEuN3Lnj27uJScMGGCGPaAWqxatQpCgiIry56ySMIfWUVB2b1x48bkyZPz5Mnj8hgLHTlypMVQ0JQpU1Bk7fl+/fXX5CgKNBrwiBEjZEmHLNC2ZcklRYoUw4cPt69CoCUrT05+IacfJSNKOG/ePGhSiRIl0ErRyD/55BPx0QU6d+6MHgyX6NWrV8KECV0ej8fUDsXaa6CkD3tv0aIFir4kovx20jKDBw9Oly4dgajaY8eO1fdE+Ko+bEEc5xKOro+ifOXKle7du0vM2rVrC3+295odFIxyitPLQoUKydIobSvkHAJA15AdDSKnakmQrkcjDEoAJITyCGUFPNu6dWtZDISsChkWmgRHkiWO48ePQ6sgtNKe4uJLjMEQQmPC9OAG4j+cAtOkXqWC8sNFKUmAljYdslDuoyw4f/48RZUGQZAgjXBsejNt2rRS+AULFviqJujWrRsEplOnTlAyiOizzz6rFk7pcfGwigA4uxa7evWq3TsdeP7551VGviQKQW3Tpo2Et2rVar8HdevWlZAuXbrITshIiDFkXsLh8wz8+/fv582b1+XZvy2rYRBUGTJIMmJsH2uqUxo0aMCztA+ksXr16mq7ZoDDwRd27dqF5EtkxNuyrnv37t3evXtnzZoVMaaLa9SooZyRRjFfA7dHvCGfikzSF0pWb968KcdHBVu3blUOJoS1Gi5qYGBgYGDwEAHd2uJMG+1QV+5RFCyLNijfATrZg9s4xIQoknVQ/pbRy6G+wR4o4KmDBw/KU9FhPQvlFcUrWJdLkai+gr3XQojICQDRfDmsChBoqwcOHNCdPJGRs4M92sHy+SPkWUQFstqDeCB+dpddUhi/uSO98El6BIV+7dq1K1asmD9//oQJE8qUKaNOhAqiIlHu4MWYZoTZquyoCIXUZTI8PNzi7M0XeJak1Fp6CMF4tzsbU6C0lDnmjyY+JECiECfmBMtMxeWNGzcuXbpEj8ekdSJnGC5qYGBgYGBg4Adjx44dOXJkbJfCwCCGAF+Fc1pOXAs2bdqkzvEaGBhEEYaLGhgYGBgYGHjB7du3v/rqq9OnTx8+fDgsLCzY5UcDgwcXq1evdv3X1pTgr7/+6tix46VLl2KlVAYG8Q+Gixo8kAhwf1RM2gELFeJOmaNpE1qkER2biOJIjrJtxtfdv//+O+brHpO4du1aXBM2A8GECRPUGTnnk3UGBvEM58+fl7PBDRo0mDhx4rx58yZPntyhQ4eGDRs6eAQ1MDAIFoaLGgSHmzdvDho0yMHuXLTiyJEjvBVat27Ny6BJkyZ+XQvky5dPeW2ORdy/f3/OnDlFixYNJHJcKPOXX35Zrly5ZMmS5cyZs1u3bvoJn5jHhQsXhg4dWrZs2cqVK8e/HDdu3Pjmm29mz5592rRpvuLUr18/ZcqU4o0gPoFpZPjw4VWqVEmcOLGyM2kQp3Dy5MlKlSrlz58/EJ+iBgbxDL/88kvnzp0LFy6cMWPG0qVLt2rVSvclY2BgEBIYLmoQBK5evQoJjC0/jT///HOqVKnUt/m33367ZMmSFMlX/F27drlcLn5jqoDe8fnnn4tLOuiE38hxoczTp08vWLBg165dX3311fTp04tlv1g84w6T37Rpk+u/Tt7jTY7w/N69e5OXAxcdMGBA+fLlb926Fd2FiWHcvXs3PDxcjIsaLmpgYGBgYPAQIvRcFPXi0KFDWzw4ePCgVw3jxIkTaNuWTVnnz5/fuXPnxo0b+Q3cgbJBjOHevXtPPfXUhg0bYqsAVapUyZcvn7pEtFKkSNGtWzdf8SGrefPmjZGiOeHOnTv8hoWFBcJFY73MDL3q1asr64KMyly5ckEVVq1aFcMlGThwoH6ZMGHC6GaGMZ+j4LPPPnPmovEbNWrUMFzUwMDAwMDg4USIuej9+/d//PHH77//HsYCq+QPl6KLC+Cf586dE681OhdFA5bATZs2yZ8ArVEbxBgGDBgQoJfz6IB4ahaf4ArVqlVLly6dr/Wi/Pnz9+7dO0ZK5x+FCxcOhIvGepknT5588OBBPWT69Om0/NChQ+2RV69ebfEbFiosWrQoVapUekh0M8OYz1HhIeeizz33nOGiBgYGBgYGDydCzEXPnj0r7lPv3bsHLxWfqidPnnR71kv37t3LLeVBVXHRf/75Z/PmzYTI5s/z58/zHyobaU9NBiHHxYsXkyVL9umnn9pvbd++ffTo0XCYLVu22B1J7du3b9KkSWPHjt22bZsejlR89NFH/Dl8+PA777zz7rvvijcwXyB9FNZZs2bpgX369CHw888/t8ffvXs3t3z5Io+ZMusIhIvGhTLbj+CuXbuWUk2ZMsUeuWPHjuXLl3eulAD5EeFhaE+YMEHZ6dm0adO4ceNGjhz5zTffqMhffPFF8uTJkyZNusgDmQcUM6QdqOaMGTMsp1ipF1kMGTJk/vz5165dU+HMM99+++3PP//8+++/w/e8LuxHLsfjx4/TLOTIIzqVYq5DJvfv33/nzp2lS5cOGzaMFBwaR3FRmmXFihW0hqWQpLNs2TJ9bzy9/NVXX0l7Dh8+fPny5ZY0fZXN3hqkvCgC4eHhbo8lIblkAvdaYF9N6qsL3J7t/R988MHgwYPff/99i0M5w0UNDAwMDAweWoSYi+7cuRPd6PTp03Ip1FT0MNQp2bj7ww8/WLjolStXZClVzqQRLnHin62OBxewIPRFesoS3rdv3/r1658/f37hwoWJEyeGrxYrVqxt27Zyt2fPnqNGjYJvjBgxgsehjm6Pptu5c2cuCxYsCLOqVatW3bp1uaxevbpDAV599VXiLFmyRA8cM2aML5rUr1+/sLAwr0nFWJl1BMJF41qZBbNnz+YpuI39ViBcFDLcqlWrRIkSFS9efPz48VmyZCG1jz/+GL734osvUimEas+ePZkyZerVq5c8smrVqrx581LHpR4I8RZm2KVLF6jLCy+8QCIVK1ZUuUDFmzRpsnr16jVr1tAyNCNMiXB4eJ48eYgMCX/qqacSJEigb/NWiESO1IVcTp069dtvv1WuXJlbwmAh1fnz5xdPAM8//3yzZs1y5sxJUhs3bvTVRMJFBw0aRE898cQTtBWX7du3d3toLX2aLl06Qn788Ue359S0kLfXXnvtjTfeaNSoUenSpbnUHT/6KpvX1jh27JjYioReqhQWL15cqFAhC58U+GpSX13g9thnSp8+PS0D2X7rrbeQgRMnTqgEDRc1MDAwMDB4aBFiLiocEo1ZLi9duiQkU9+Oe/nyZQsXFcoqmpZAFlQVpzWIdVStWhWF2BK4efNmlEi0T7ls06YNl0eOHJFLWFPr1q1V5CpVqih9GmTMmBHVf+XKlXLZvHlz7h49etRXAWrXrk2EtWvX6oGzZs0isEePHvb4jz32GAzNHh6TZdYRCBeNa2UW1KxZk6e83gpwXfTWrVuQsTRp0sB27ty588knnzAJwE8oyaRJkyQOVYBjqzVb+JWluUgByvTdd9/JpXybECNPEDaIrtrVLynDcOQSGi9G+Yl24MABWU60I9gckyZNCkGVW/PmzePWunXr5HLatGlcQv6Fy0H2uISU+mof4aLwOlkw/PXXXyHGhCxbtkwiiO0r1afUgkviHD582O3x+JIrV66sWbPKXeeyeW2NoUOHWjx29O/ff86cOb4KbE/EuQuQybRp08r/M2fOcGvAgAEqNcNFDQwMDAwMHlqEmIsKyVQugGXBE+i7be1cFM7Jpb4fTNZXvS7FGMQKsmTJYrepM2zYMH1PqajUMA25JD7q+7sRgNLI4o/cLViw4KOPPqqSGjdunJ1q6kDxJYIiBoIPP/yQwDfffNMSee/evYR73RgZk2XW4ZeLxsEyuz17QR0c3Ae+RxdS9/jjj+shf/zxR9euXdX3pu7du1MwiIpcemWG+ulNaqrY2vz580lftcDUqVO5BbOVk+rCDL1uL9cRVI5gyJAh69evl/+rVq3iFqxPLhctWiTLhurZFClS6GuqFkiHTp48WYUsXrxYX8GWveiKi54/f57Ll156ScWvU6cOIepkvkPZvLYGEzV1p4PUnFy0aFEHf6f2RJy7gOpMnz5dYpIst/SvJ4aLGhgYGBgYPLQIJRdFjxGSqTTXq1evRo6L7tq1y3DROAXUSpR1S+CcOXN0NXfLli2K51y/fp3/o0aN+v6/UNv2LBxp0qRJxP/iiy/cns2lSzVIYI8ePYig1vf0p/r3728pGCG5cuXyWpGYLLMOv1w05svM+NLLbDlo6vYc/6tUqZLu1BuumFZDkiRJIGx6iNezu24PFy1evLjXW9999x3M+cknn9R3AvtlhnPnzpW9vm4Pjy1QoMD3Ngi9EeLk1ylcUDkqHDlyZPjw4bLarMw42bkoLWMfPgp220VQOEKyZcsml365qGwhthxn9Vo2X63RtWtXJRhk1KpVK1+l9ZqIcxcImPmnTJnSr18/nn3llVdUuM5F/Y6jeI8lS5bQbrFdiv/brDRz5sw//vgjtgsSMsSRhg0t7t69u2bNmqD2uQSFY8eO8faZPn26/haI3SLFJ+zdu1f/Lrx9+3be8hYHE1GHfSzzZmf2Drm7imgqPyVfvXp17Do5N4huhHhdVEwQXbhwQS4hpWKFSI9j56JiRNe+R1ctkhjEOlKnTg2bsgTS0ZkyZSpVqpRsrRw2bBgKt6yEiBkeByOrDhxp3759STXkzp3bHbEqJWZ4FAYPHmynBwC1GOXYa74xWWYdfrlozJcZRqGXuWXLlvqDDM/WrVszovVAqO8kDU8//TQ11UN8fT/yykX3798PD5EzwPKtIXJctH79+tmzZ/fVAtHERZnHIFT0BR1Be4aWi7o9OxHy5Mkj/4Plog5l89UaTLaJEiV65pln+N+lSxfLBgQL7Ik4d8H9+/cpDAKGJFNIBy7qdxzFb5w+fZqmSJEixb1792K3JLIjXT+E/EAj7jRsqMD8/Pbbb6dJkyaQyS1yYD7v168f046cD/d1uiEmixRvMHv2bGlVBpoKZLojZMuWLaHNSx/LV65cadOmTfLkyfUXSqgQTeWvUKECyZYsWdJustEg3iDEXHT79u1wyLNnz8qluG/ZunWrHsfORS9evPi9x5uLioM06+dODWIdjz32mFdd89SpU0ypdevW7d+/f69eva5evSrhv/32m0VdFqjPpQ4cySuYN+1LoLLmY/lmgTrrPM/GWJl1OHPROFhmclGHDH0hqD26Fi66bds2yIba8hoVLvr666/zXw5PKjC9HDt2zB09XPSPP/4ICwvr1KmT3IoOLpo+fXp15jMoLupcNofWaNGiBbeYrnn3O3/btifi3AUNGjSg90WTcOaiDyF0Beuff/5BUxw8eHDsFgMw9hEqi3unOIWgFNNYbNhoBZNANBE/FDBSlqWz/fv316hRwzK6FSwdEX1FimdgTrZw0SlTpjRr1uzmzZsBphDgELCP5VKlSoWEi1oKEGz5A8TLL7/s8kDZyDCIfwgxF0UDZgrbs2ePqDJo2FweOnRIj2Pnonfv3pUQ2UVw48YNufTlN9Ig5sGMmSxZMvvch5a8d+9ee3w6FwqENq/76jh37tzbb78t/yPBkfLnz//UU0/pIdmyZeMdaYk2YMCAHDlyOCjTMVlmBWcuGtfKPGzYsFWrVukhyimLjqhwUWE+Sr8Rk7+Ki5YrVw6mqsd3YIYzZ87kf7Vq1fSzAGPGjJHEA+SiQeX4wQcf8J985dby5ctDy0XDw8P1bgqKizqXzaE1UFZcHpNIflV2eyIOXXDixAluNW3aVAKvXLliuKjChx9+6GBgOcaA+shYju1SBAddiX9o8eabb0YT8YNUWOZDX7B0RPQVKZ5hzZo1Fi4aLCL9rLwvoshFeV+88847UUkhcPBqK1mypIMJA4MHHSHmotevX9+wYQM0cpcHQiktjgHsXNTt+fBGyA8//HDgwAExxutV8zaILXz++eeuCCOiCkuWLEmVKhUa59KlS7/++uvNmzcrQ5pA7JekS5cOogVTQjV/8skn1Zp5WFhY+vTpVWQxz7NixQqHMqBVJ0qUSJ0r5jJJkiQ7d+60RHv88ce7devmK5EYLrMCtNnh1R6nyjx+/PhChQp11MA7L0+ePGrvvULgXDRNmjT58+fXQ4SLvvHGGzArWG6JEiW4VAeN6tevLy9LqAtSd+/ePS7LlCmjHhc6JBTr9u3b2bNn57JGjRrz5s376quvWrVqpaw3TZw40aWZevKFoHIUvkfdT58+vW7dukaNGnEJ/1eOZFyaLaK///47ceLExYoV85W1DK7Ro0erkPbt2+tsrVOnTi7NcBe97/KYsVURqlatSoisljuXzbk1YIzcPXXqlHNb2RNx6ALhosjnTz/9xKxOSRIkSPDUU08horwviADhJ4L8f6iwe/fuZMmSxYVDjC+99JL+2SXuQ759xHYpYh/RR/yeeOKJQLiovSMMFw0QUeSiURkCUeeiaPUFChSIsY0GTJJe3SUY+AJqFbrxxo0b+dUPBkO79uzZs+u/UM4a6Vbu/uABf7w6dYsmhH42//3336m/sE14qX2frVcuirqGmqIsXoguGPKyGUQadFbx4sUnTJigBx48eBCq4/ov0DJFreQR1OsUKVJIOEqqbNi7deuWuMEEEDAYzpdffinpPPPMM8parFcsXryYYkC33nnnnaJFiyo3Jwri7sJyyjF2y7x27douXbrIs927d7e/pONUmefPn+/yhiZNmtgjB8JFoSKinbg83nfUtwPGe+bMmQnMlCkT7IW5ImHChNRCrB/Rs4k84FUN9ZIUiECNqPXKlSsLFixICMLApOn22NgoW7as5AL3Vq5ioIX58uUjEHYNjbx7966vcgaV459//inbnJInT96zZ0+mcnEB2r9//y1btkhJyBHOf+nSpQ4dOkhSCK3Xae3mzZutW7ema6AEAwcOhIWOHz9epkeynjFjhjQUhBNZgigSgcvUqVOTINFghmiNhLRr1463jkPZ/LbG8uXL/XISX4n46gLwxhtvEAgFrVevHm+EatWqcVmzZs3jx48PHz4cos5l27Zt7d+V4jEOHTqUI0cOKk7/ohSqgwb3798XHzkqJiGorVevXqWvt2/fPnv2bEis3Prnn39+jIDMBrx/VYjF2gdZLFq0aNasWZs2bVLL16TQq1cvl+c4ljwlXr7dHt9CdrPet2/fRsLfe++9L774QlwQ6bhx44aYl/vrr7+Q1Tlz5pCI36Y4cuTI4cOHyZfxwvSoKwZMUx988AFp6qa8ly1bJjIjBVZGWdAi1q9fTwWXLFliz9fesIGUlrkXgaeyZ8+etX+Ms+Do0aPyqZRBRyGpi9rbhVbH9EtSKhG6Q8qvNo6h/EmIsjynQIKUAfrx7bff6ruTdOJHUWkr5jHVgw4gzr59+5h4Fy5caNn6SHkoA9NykiRJLCW0wGtHBFikO3fuSGfxq1x5OcChI3zVJfDRQbi8RwgnF339jfmWZJno1KDTcfLkyQULFnz88ce6w2QHIGnotwwf5jqvXJRwy6dARhnD9tNPP6UXlDrtawj4GkqWsay4KO8jXrhMKche4I1GdvL1k0mbQN2ulb38bo/Oz/iir6m7fW2Tssn3OKKh4FFZy8SFhKDAWDbleW0WA4GY4JGTj/JHrV6IBFogA4pXjCwlqqegcjFmMipaviwizQgrs6e+XysQ0EzIPZpZyC1xGUQd27ZtK1CggK5M83p46623eDdw65tvvmHuYx5Hn9Z3bjCD8IYOoT1GhIr5jheDV17BvMYr30F+YqXMzngQyxwSMN5hI6riYthG3b148aLyDhUgmHNIMNIWDoLKkVkO9qXcqDBrRf2NSAsEorv7RaTLNmjQILslsKDgqwuolzrkTPGM72goaOHChUUZHTx4MLoaSlWnTp3gAASq4yooYRkzZnR5LII899xzjz32WNKkSWH1YsWNsQNbe+SRR4gAS3F71EQmE3lErXsQjQmkePHi6Bbr1q3jD6qkjDUy7dixI5Fz58492ANGJbryM888Q2DXrl31MlPIQoUKwYjQDnv06IE23LdvX5mH0YCZkZIlS/boo4+i1xKNopJC2rRp9+/f77UFeJVMnTpVDGijDcs5QyCblpnuCBkyZAhxypQpQzpCbyj20KFDU6ZMSUwpsOykgI3kyZNn+PDhaMZEoCTLly+XjOwNG2Bp+/fv36hRIyJs3bq1SJEiHTp08NWbECHIvHzxoX0ef/zx0qVLc5krVy7EfvTo0Xnz5i1Xrhwdly1btvDwcLdnpNC58lVREqHk7dq1c2mOeQXTpk2rXr06nAcmlj17dt7CivkI8WPM1qxZMywsTCSBMjvLHiOUZu/Tpw/q5sSJE9OlS1e/fn1F8ODktKrewl5dDfvqiECKBPFr0KABWdMyWbJkobl8HUb12xEOdQlkdMDEGjZsCOt+5ZVXpk+fLhJIvdyeaZOMWrRoQbPDRem7unXrKtqM2NN9yBXd3bRpU+4OHDjQudl5fefPn3/SpElIeO/evcUkj3BRaNiwYcNoB9d/l5QpXtmyZSk8JLNx48YIqteWR0PwOpSE99rHsnBR+ojyqM/N1JRXRiCNtnr16ueff57LZ599ltzJwlf5SW3ChAmMhSVLltCMdE369OnVhpqvv/66UqVKLs95Ewg/gyVnzpxcMjHqnyfsmp7XZjEQ8HoVI7KiS/DqF1YpdEzWAn/++effNYiqIGcqkSV6jRDZoBpj3kzMLheDIDBlyhS13IGI83a3fwNDh9CXROIUTJkNDHyB1w/6tMPSsUFoISqj2qN7/fr1Y8eOoRYryuT2fGOSVW7Yo+x3QGNImDBhjhw5VDoo00pxFIimqLiobAJXn65kF7c6z4xeImqlXKKIXLp06X//+59Ff0U1IQT1UYWQICHElEu0HDRyCF6bNm1k9UOUe3Rcr9WnaufOnatSpQpxUEnR1NesWdOkSROoGmVAgZalKkk5VapUpKy+1MAhXf/doIjo6gfyUWohOWpzgb1h/ZYWNdelHWjfu3dv27ZtvVZEIGcl4MPK8ZjYY0OxVsq3bG6HYMulmKzTjSBAAyxcFB5YrFgxdZoazZ4I6N9yKcSvaNGisq0GliJ8wGGLAdw4c+bMyqCA27MYmChRInLRFw/sLewV9mh+iwRRJER1BBIl8X0t5zp0RCB1cR4diEHfvn25fOKJJz788EMU8ZYtW8ppCP688cYb6ql69eoRTflJhh4PHz5c3a1YsSJ3ly5d6quhSDlp0qS6zzP5BiRclP7lRS/fL3QulzVrVnXyX1ysqVt6y/saSr/99pvXsSxclJjbt2+/desW3DJDhgwuzTak3ylF/BqoPbq+yj9y5EhGrtrUQBfLWZjFixdLiNhKoC5jxozhLgNWzokwR/lqSedmMbhy5YpsSpUBRZMKq7x48aI7YhXa6zd3RuimTZtUZ8nByRizF2W4qEFwYMpYtGgRfxYsWODSTKQImI+Y8oJdzooxmDIbGFiAktSvX7/ly5c3a9bMfN2ISVi4qEBWKvQNDqI46ubo0Zv1OLJnW1ccLefBUPfhaYojCatUB9QtXFQAfbLor0WKFLE4QL53757sHld2BNKmTasfMkT7cXm2tTs0AkRCp2eC999/Pyws7L6GmjVrEm3cuHESwU6B0EfLlSunLmUfuH7eyd6wzqUVA9S6RbFZs2Y5VETi63x1/fr1hNSpU0eFoN4Rgjoul8ePH7dw0T179uhcFMURVX7hwoUqAry6Vq1asCa5FOKnNHt3RHvOnTvXVzmFAlk+borA6MM/ilzUoUiIKwRM9eydO3dkiU/3MK/DoSMCqUsgo4PLypUr64msWLGCQH0XOpo6ZE8KyZCB8Z48eVLVAtJl6WsLateu/dhjj+kh8oVI36Mr1sgVlxOT440bN1Zbh3QJtLe816Hk9jaWpQV0Jz3SyClSpJDvMn4bzcJFvZYf6U2ePLnFVfXevXuJkyVLFvm8IgLP6FYRkByXbUeGDudmMTh79qxXH5myFwluyf+jR49u27aNd8qhQ4fU/ikd9I4srqqjpNENw0UNgsbatWvDw8N5qZcvX16+BDMF16tXD1Xgf//7n/0QUdyBKbOBgQXDhw+XPVpVq1Y1DtxiEl65qBxLtnNRXbeQCUHtc/arOLo17wso0MIWUBwlxCsXFVvQSiNEreQSXdxSBTkJrCiihd2h0Lg8u38dGqF///4um4fkl19+OVOmTM/bMHHiRIlgV8T/9cDtYchLly6FNrsiXJII7A3rXNoLFy4IR+rUqVMgZx/sXFQWOSm2ChE3pxUqVJBLv1wUzulydGVhNxQki9Xjx4/39UjevHnhUZZFSOiuhUpFkYs6FEk25do7VxdgHQ4dEUhd/I4Obrn+a9kbwKAop69aQ34SJEhgr0Lr1q19VcFls7lgPy9qbzpZaaxevbpdBuwt73UouW1j2d4Cbs+KpRxfl8DIcVFL+cX2hGx41lGgQAH16cEi8F6bxQ6HZjFgkuGdon/Z2blzp9ptu3v3bstRUjinxYzFrl275OCoxV1itMJwUYPIg3f/d999xztm9OjRK1euVLZb4zJMmQ0MdPz555+zZ8+eM2eO2Z0bw4hJLgpQPmBKU6dO/fLLL3XWFAgXlbUjfeFRwIxEuFLBQ8VFCxcurAibV3hlStevXx85ciSMZevWrbIuqk+VwXJRwGSbPHlyl8e+msNKoyBwLqrcO/nlomL0zuEMuS/i58vZxu3btyFRRLCYCxL33Xny5FEhIeeiUqTLly+7PGa9/aasw2tHBFiXyHHRYsWKQXR9lUfWYwN3Q8Xrm/jt27fXAwPhoseOHUMgCUycOHHv3r31HEPLRYFsPZBtxiHhorJOS7Et5REnXvPmzXNHlos6NIuBnYuKTxPhonv37mVekpWMmzdvyvbdkydP6ikcOHBgy5YtcspUWXmIbhguamBgYGBgENOIMS6KroaaCOcRxUL26AbFReWRbNmyWaogR0/79u0rl6Hiojlz5oR1OJhzsyviqE1hYWFyfsQdsUc3ilzU7dF65RgeaNOmjUNFooOLtmrVyi4hOoLlon///bfY3JazxwrieKlixYoqJJq4KFov/1988UW/KVtg74gA6xI5LporV65EiRL58ubQsmVLHtHtxzpDlmp1L1zuwLio2/OFBRIrrLtkyZJq23nIuah4WRODuiHhorLjpnnz5pbySEZr1651R5aLOjSLgRjRte/R9brIKVt27R40GVxiysir+ejogOGiBgYGBgYGMY0Y46J9+vThUjl1iAQXRdUTGmDZlDFq1CgCFQMMFRcVl7Pr1q2zRF6+fLnYpLEo4hcuXEiTJk3t2rVVSNS5KERRmfVeunRp6tSpuWv3tqIQHVxUTiHqFnQEKJey6TpYLgrEk7PFw/DWrVsJJDUVEk1clO6D46VMmdJOHvQjpjocOiKQukSOi9aoUYNA/aSuQJ6Cg3F3wIABlruo714lZNu2bS7PUq3+ecUvF71z545usUkEWJkcCzkXpcoMB9kdExIuunLlSi4tp2TdEQuwsjQXCS7q3CwGFy9elC24KkQWOc+fP4/4yfFmdYvBpQjnrx6oXQZMqmIDKWbcmhguamBgYGBgENOQ1RXdgog7UlxUDm3qOqg4elXmjsSQqeKiou2pjbWyVGXZf2vXX5s0aULImDFj9GgNGzZEw1bqS6i46JAhQwjMmTOn7oto48aNam+n+H5Q+X766adc6lxUmkhfCgiWi6JSr1ixQt2Vo5u++JI7UlwUdVyqqU48rl692qWZckFH5BLyRpepRGA7ffr0kf+R4KIzZswgQq1atfTAKVOmkIu+0CdWqXwlomDpiECKVLlyZSmAfjp93LhxemvrcOiIQOrid3R45aKTJk0SYdAdh8KExeUVCrrLs0FU/5D022+/NW3a1KvifvPmTTFUq9vRFarGJOCr6ZDVLl26qLunTp1yaWar7S0fFS6K8GfMmHHQoEEBNtqcOXNctv23lvLfunVL/JlDxVWce/fuwaJfeukluYwEF3VuFoO7d+/KQVDlGEwu6Y4///xT/ovnWKYdXgpcys4CuknMGkk6zDNcwmNjptiGixoYGBgYGMQ0RHfs1KkT2sPcuXOFkIgbTOWaHIhbeX2NQkzCqsUB2SgL4dy1axe6Rfv27cV1IYxFFh/E8eCLL76IzrFs2bJGjRpxWaZMGagOmhzqLFp18uTJYW6yZcsdoeW/9tprKtPw8HD4SZYsWVTZ0CNTpkypaBLUIkmSJNAAdXwL7ZxEeMqhEd566y2XZv1IgKok7YDCjQ6NToxyTKVEhQJPPfWUy3O27dq1axDRb775hkty//rrr/ft29evX7+8efPKitn69evlEUvD+i0tKrW+Vkw1U6VKJa5BvUL4sFKy3RGMhcZXIYcOHSKE7lMhwihGjRpF1yADqOBcZs2aFb1Qli8kJEGCBPAcWgktvHjx4sqCerNmzbirzOq6Iw7pKVJhB2L2zDPPkKD6CILOSpH0RyAMsv318uXLvtIRWDoikCJt3rzZ5QGcfNiwYTNnzqxTp46DvxyHjgikLn5Hh9iztZjAZUiKiZ306dMjexMmTKBeDRo0UFRTFvdSp04NmZw9ezZjmfjInq9awJCJnyZNGng1Ikd3y+I/dBd+Kwu/8rlHXAdLXWCwyscGcRImTLhq1SpfLe91KLm9jeXGjRsTogxrA4YMbFONBb+NJgSeHmT2WL16tWxAsJQf0C/MLdRUGSOYNm0a4q2Mim3atMn1360BYvUXaffVks7NYuCOcMfyww8/HDhwQE6Eyi5cpFfIJ83OLSGfGzdulC8azI3CVHfu3El8+W85Shp9MFzUwMDAwMAgpnHixAnxKZ89e/affvoJ6iJOEWSJ74svvkA1HD58uDjGhNKg2F25cqV79+4qjvhshLSgJUtgwYIFd+zY0bFjR3RcYopyTMrp0qXjLkr8yJEjiS9UDR1Rvp3D92SdB0pw48aNyZMn58mTR1Rn4l+4cEEKzB8y4llU0p49e1avXl2dJoLTtmnTRsrQqlWr/R7UrVtXQmBQdrvfZDR48GApGBR37NixupEeGkfUX2FirVu3VtongFGjgEqz0CboWEKwXR4rtbB0FGL+Q6gWLVpkb9hASgsFgii+8MILCxYsGD9+POqyZQVbx8KFC6GIQk4mTZoEZyaXp59+Wgo/cOBAMSgiVltcHuM94okEFg3bIYTq9OjR4/z58/RCrVq1oN+ivtNZhCdLlkwepJCy2Es4DJYOFXI7f/58AimnUG7UfQnxClLu3bs3cejuIUOG1KhRQ9+MSsWFVMiC1axZsyzGgXToHXHx4sUAi/T1118j85IFLTZixAgHC97OHeFcF7e/0QGNlF0DiRIlIh21dwBA+CGociKRTqEX9HaAArVo0YKnJGUosQMRFUydOlUahxZj6FEdLqGytMbRo0cpvNhnopDixZSxyfxQvnx5umDu3LlUbfTo0V5bHhbhdShRSK9j+eDBg/QsMREnGCxtS931w7F+pxT6S4zZ0n3vvffe8ePH7eUXMLOVKlWqTJkyTGWwemiw+pICTaLdZIwMGzaMAQ6tFYdVtAyk2usis3OzGLg9vaPIJNi1a5fq3Js3b8rxUcHWrVuV1xZaW75FKvz888++vP6GHIaLGsRnMAId3qNBgeGtvsrHWai5mz8hn0QCNw8Qp9qK97EvExS+EPLCx53WiBmgyvDOCzByIA4z4isQDIhTSA7kQFGOHTsmSdmXsxgF0C11UggNHvVXzxctJMCO4FmSihmRRk9CqfIqS+Hh4frqsdtj3kbf08vdqFg0uXPnDu3DVHby5El0d/2QVWjBGwr9Xvw6kp3XXmAGo81D6+uP2iEDUfcNZu+IAIHEIvx+GzaQjvBbF+fR4QD6hd7xpUX89ddfyKf+lcQZvJSpspAxRpCzckJpxfcj9dqzZ499FES65VX6p06dEvOqXuHcaMjkgQMHArS+TmUR4JCYavfbLAYChBPJpH0s7xcukWqEkE6xa4k8ddmDGLZObLioQfzEF1988corr6RPn97BCGFQqF+/fsqUKS9evOg35oQJE2Jsk72AUrVu3TpHjhzFixevXr36gAEDOnbsuGTJkpAkvn379s6dO+fNm7dHjx4BPhJ4W0U3eGllzpy5TJkygUS+cOHC0KFDy5Yta/F7Hmkw448fP75q1aoOruriGZYuXdqiRYsMGTIwAJ1j7tixA4lCYp29dxgYGBgYGBjEYxguahA/cfny5YYNG7ocDeIHBQhe+fLlb926FUjkPn36fPPNNyHJ1y+gWyj00Cf5oP777783b96cik+aNCkk6d++fXvq1KkkGDgXDaqtohX//PMP5NxuiNIr7t+/L8dXLDZFIw35lp8mTZpHHnkkJAnGfVy9elXEzy8XRa7k5BiiEjNlMzAwMDAwMIhrCD0XvXv37qFDh7Z4cPDgQa/rvCdOnNi1a5fXjUkXL17kluxXMTAICqdOndI9kot7q0hz0YEDB0a6JFCgihUrKuMi0YrFixdb7BC4PQYkevXqpS4ZlSNGjIh0FmLsLnAu+kBDDvM4RFi2bJndH5cDihcv/vBwUXeECUq/XFSQJEkSw0UNDAwMDAweWoSYi96/f//HH38UpzQbN24Uj6uyt1sA/zx37pyci7Vz0WvXrm3evJlb4pLbwCBw3L59u0SJErot+6hw0UWLFqVKlSoq5Vm1alWRIkVCckDCGVLN8ePH64FnzpyxGIvXXQsEC8NFFY4cOZImTZqffvop8AQNF3VA0qRJDRc1MDAwMDB4aBFiLnr27FkxzXTv3j14qdhrEqPAKOV79+7llrLRpHPRn3/+WWwNCwwXjVNA814UAeXKefHixVwqf1l//fXX3LlzR48eTbhyQuUL9sj0uMri008/FWMzx44dkxA5oI8Ikd3+/fvv3LmzdOnSYcOGKat3N27cqFOnjsvjJYz4cCe3xkWvXLmycOFC4tuPcYaHh7///vtDhw6FOqpj3KjRyZMnFxuMQIwlkOmyZct0S49ujxuADz74YNCgQaRv2QJAamnTpp01a1awrR0sxAZ66tSpde/G7giv3G7PAi8RSpYsSV3Wrl1L40i9ZNn21KlTcmlZWaULiEwbfvTRR7Sz4qLkonpK2hmsWLGCyy+//FIu7W21bds2MX5Id5Dm8uXLLbWgB8loyJAh9L6y2xkU9u3bBwsaO3as7s3M7dm0bHe5dvr06alTp44aNWr16tWWvcSKi1JrUpsxY4bytH706NF8+fLRFCNHjqS+Dg4edCgueuDAgfHjx8+ZM0cZEhTQ1DQI8kn5LcYYHYaVV9ENBH///fc333wj4kF3UBe6RlI4d+7c/PnzCbF7bN+1axdNMWLECLHvarn7xx9/UEIKs2bNGjsXvX37Nt1K55K4xZyMnYsiRdT3ww8/pIShNdZiYGBgYGBgENcQYi66c+dOlBvlg1uoqRAG1FPZuCvubixcFEVH7houGgeBrixnL1u1aqVsr6M0Q9hEdUbXLFasGPyQu6iSKVKkcEjNV2T4jHAq3cZ0x44dX331Vdgg2rN41XvnnXeef/75Zs2a5cyZE9qwceNGt2fXtzgxo4SkDF91R3DRKVOmVKhQoWXLlrlz59Ydkbk9hvjffPPN77777uOPP06fPn3VqlWFlqDc582bN1myZEs9oMCo4GIwXXcP/e6779arVw/mA2fO54HFjh/0uGDBglFufj9gZIkb9yRJkgwYMMDCE65fv07tXB5XYNRl/fr1xO/cuTMhYgmdXqC56IVHH31UPQV/q1y5MhGo0bp160qVKqW4KAmKrwIorqJA58+fRxjEqp6lrWA14sngtddee+ONNxo1aiS24CE8Krvjx4+HhYV9++23EOPq1au7PF7XoHCBLz/27NkTYglPJneXxw0agZBh+jdx4sS6R3u3x0lA4cKF6bUdO3Zkz54dKXr88cfJTu4KF+3SpQvFFp/gFStWlFvUiB4nBI5KY+pGOx0gXBSGljlz5qxZs4p7A2Y8uUsLkzvFRvYgbJRW+Qp3GFa+RNcvGC9lypQRrxKtW7dmcNWqVYvL6dOnky/DvFOnTjly5EibNq1yAUcxiNmmTRsmdmZ4BIMCK2cebs/sXaRIEcbvxYsXZ8+eLd4aFBdlimjSpAmcH5pKdehonehauOjrr7+OmFGXI0eO5MqVy+9XLQMDAwMDA4MHGiHmosIzlYp26dIl2a+r087Lly/72qOLymW4aNwEJAEdHRKiQujr9u3by/8lS5ZkyJBB3UJzdfBS4BC5SpUqaLFHjx5Vd8kRnin/p02bxl1UZ1lagUtwCSmVu+i+wlTVs8JFmzdvLvSMKnAJl5C7JFuiRAlFrYcOHaroGYAvpUyZUi82bFbnokg1urLafy5rQbpbLXeEj2/1aSb6EB4eLgQPwKK//vpr/e6ff/5JuL5HF2KgVxYUKFBA56K1a9eGpajLBQsW6Ht04TN6y7s9nq/1LcGWtoKjSsFkJZY2p+ngYyp+jRo1ypYtK/9/+eUXIr/88suBVx9ihhSpS5EiyR3RgtbqXJTWgLypw7Tz588nsr58jZxDHaF5cim+5hV1pBG4DHaPLmnOmzdPqDsknBRgZXIpgqdWmPPkyaNGma+R4iy6fgGtFYd4aomS3k+WLNmMGTPkUvyYq6EEzyeC+u5AA0JW6UExps8lHFs/p92uXTvFRe/evUv1leMBkRxIvoqsc1HeF9xVK8MfffRRqAyPGRgYGBgYGMRNhJiLCpNUO9CuXLkiIbpLKMNFH1A0bdoUTVGtabRt21ZZcJFtoiNGjJA+3b9/v8OmQYfIkChuvfnmm3J55swZ/eTeokWLuPvuu++qkBQpUqg1K19cVFdnoVtFihSR/23atOHZdyPQqVMnUdDlrp2L9unTR+dXRYsWhWqqu5BSWI3FNdyYMWMCPzgXRTB24MPiSlstDArsXHTNmjUW9lKwYEHFRX/44QfuQkjUXft50QoVKiRKlEjtwoUmrV+/Xt21tNX58+e5fOmll1QE2VAtTJ7JAUKiFw/2kj9//sDrDsuFMaqurFmzJokPGjRI7kJ1dC4qlnKVnNBlXL7++usqguW8KAkSYdmyZXIZOS6aLl06PaRQoUIksnnzZrenbUlTeUAtVaoUdFT++xopzqLrF/SLRUJk14P6hsi4U8Pw999/p6O7dOmipzB48GBlqJlRRovpq/H6Hl0GBcReFVUMMidOnFh9xNG56G+//cbd+vXry6bo69evnzp1KsBKGRgYGBgYGDyICCUXRWESJqk8/0IpDReNN5A1jbfeeov/N2/erFatmrrFZYECBbhbtmxZdYYTbN26dakGOTnsK7KgRIkSyZIlk88ZcmxM3bJz0bRp00Ia5X8gXDR37tz58uWT/yj9sOvv/wtFn5y5KFVIkCDB7NmznVts1qxZPPLRRx85RwshYBGyIVanmsFyUWk33QW2nYt+9tlnKkScyujD2S8Xlb2v6hxmrly5FAFze5ZJ1ScGv4CxkNSoUaMsXak+mli4qCyPq3VU2B13+/btqyJYuOjcuXOJ//HHH8tl5LioxXZRv379SESXn7t378I84c/ZPZBAXyPFWXT9ws5F6Rqdi0p/ydL0d999x3/Ip56CLJzKSjjzgCqwQOei3bt3pwrf26C4q2WPrviDyZYtG60RYHUMDAwMDAwMHlyEeF1UrOAq0yOQUi7lRJ+C4aIPLooWLYpWDfdAQf/ggw/0W3R63bp1hQWhgErnNmnSJKkGZULGa2TBwoUL1aIWhETRFXeouWiaNGleeeUVXzV15qLCzfQTj14xffp0okWrVs2Q0ZtIQl588UXyTZEihay2BctFW7RowV3dIY2di9Jljz/+eOrUqa9du7ZixQq1CCkIlouKdaXFixe7PacTU6VKpdYh/WL37t08a7dOpGDhoqBSpUpkIV9GNm3ahBTJf0EMcFH5SDFv3jy5XL58ea1ateQEJoKnUzuvI8VZdP0iQC4q/fXpp5/y3+Kg9ciRIwQ2bNiQ/zly5MicObN+V+ei9evXtzBVCyxc9P79+71796YLSKFGjRrGdpGBgYGBgUH8Roi5qNjCPXv2rFyK+xaL/QnDRR9czJw5Ex1xwYIF9erVk9NiAuUPduXKlbly5SKOhanqcI6MDISFhaG779ixQz+y6A41F82fP3/WrFkte4nRfWVV35mLirJeu3ZtS9UsNkKlAPpm15Dj1q1bOscTyLk7IBQrWC4qez71rcVefbrQay6PFZ+mTZvqXM4dPBdlKujbty890skDihd4C8jGTnsjqFPHdi5KvtWrV3/yySehPR07drTYjI0BLjplyhRXxBnRyZMnJ06cWFm90rmor5HiLLp+ERQX3bt3L/8rV66sp7Bv3z6Xx3gV/4sUKcJ/3SO0zkVff/11y3cNt6e7jx07Jv91Lnr37l3Zu7t//36xj9WiRYtAamRgYGBgYGDwgCLEXBT9D9UfHUt4JioLl4cOHdLjGC764AIlPk2aNPAWNHg9fMaMGUqZvnjxInF0wzYW+I1MBJfH1I3FcokzF/3qq68s/MqZi8rxV31B7969ex06dBCPoOXKlbMQGAu/gjBzuXbtWhUB9VovG3jrrbcSJEigCKoyNhNa5MiRw+LFBJaSPHlyuLTkePv2bdd/DcasW7fOwkb01a05c+Zwt3HjxuqucNFu3brpudBQPAUpqlWrlqVIwXJR2CAcL3LtwzQCi4ZAfvPNNyoQAVOnee1cdMmSJQ7fSpy5KPTV9V9zyn5h56Lt2rVDwIRMWtYVixYtqrior5HiLLp+ERQXJWVGIm2i24imAQkRLi12qnSrXcJFxUWQfL2qVq2afkxjzJgxip3qXPTAgQOMcflPfOiobuAqXuL06dNKtEKC7du3z5s3z8F0XLAIeQnjLJgnZ82apb6SxE388ssvjD6HCGfPnmXQWSwXoFAtWLAg5GoVeZFsaNM0UAj5WDYwiLMIMRe9fv36hg0b0P53eSDE0rJYZLjoAw1ZNFNmPwXTpk2D+KlL+J6+PmmB38io1Dlz5syTJ49FQj766COynjx5slwiLYkTJy5WrJhcyl7N/8femcfbVP3//xivWRlCCJmnkCFjCRVlnkpRKjNRKUOGB9eskDEJSYYMSZqI5AofZQiZQ+aITCFK7d/zt9/fux6rvc/Z59x7j3uva73+OI+z11577TW819rv1xre7/r16/O4LEXKqTzl9BJACZSiv23bNoii7D/89NNPFyxY8NBDDylu2aBBA6Ecv//+u9hQlYIr86qyl5gMvPLKKyjQPXv2rFOnjsOfCsq0WlA6c+YMinWTJk0CVUusUaNGjVy5cu3du1eFSN4iIyNVCDSGgpMHGo7fEydOwCWoZIp29OhRKkqW3fj4UedUIPRDFpmvXbvGpaxulS9f3nG+V5iGbkNV4KgrMY3bqFEjFeHhhx8mRHXz4sWL16tXDw68bNkynqIpQ/RQIhCLOJkzZ+7Xrx+M9J133qlSpYranSELd4roHj9+nFZ76aWX0KK++OKLqKgoeJFiSlAvKalKXKw3qz3AY8eOlSkPElQF9EbZsmXTp0+vXnHw4EHIs/KJAhclQcpOQ4wfPz5btmypUqWCDR45ciRQT/EW3aDQD34LxHaRMlgttovoAnL55Zdf8jo1/UTB4erq8T179qRIkQIBW758OcJz6tSpChUq+OwTuSSIfi8uXugd6FUk1aZNG8WiSYqUqR+5hIsiGCpXL7zwgr6Yn8QAwRPb1957mGOKe+65hzTdjpRjgZuUw0QLmXVCUBM6I/7Bx4ihnhwq71N+IXa/1fmR7777joFXNr3rJgDiCNQ8xlif7XwrXGkaOBDGvmxgkMgRZi5q2To3uo5QSgYstws+w0VvaaC4u+3KTJo0iXGzT58+n3zySceOHVE39WWQWETu1q2bw1wKI7LouPCWJUuW/Pbbb507d+aSrywKOhQCcapatap8HRGhxYsXy1BObrk8efIkpFF2rr7xxhuoyJbt2gQWJ4FFihTRtXlupbDBpx06Onny5OzZsxMNXVlFmzlz5h133CGPN2vW7PTp03qGL1y4wOOKCcNAuCxTpkzMqjsEoLI3bNjwgQceeO655wYNGvTUU09lyJBh6NCh+h5OoeXk9q233pKQkSNHCp8pXLgwDLN27dpQguHDh8tmy0OHDkllpkmTpkSJEtA20qSl9LVHy94Xmi5dOv3A6sWLFx11RVJPP/20z/YcS0vRTNC51KlTE9KuXTtxYikbX3WkTZt29uzZIdYAaUIOeUSeRZuUxQ10L/F3ApA0qI5l72qGSjleBy2HpZOZDh06iFBRgZRl6dKl4rsV/Q+tzrKXAqR0yBWUPpTsQcDKlSuHWk8xoXAtWrTQlUIYGtyYBOHMNIQs5ufPn58iePQUD9H1BqUQh6IUed68eXQc2itTpkwiw5s3b961a5cYECKQDMhaKyN5sWLFmjZtStu1bNkS8q+nuWrVKpnL4JG6detS5xDsnj177ty507L3C0jPFQkU67uW7Ywavkog/YLmo2JpIKj4M888QwdHmUZ+1IRCkgQ0PuxMb/z48YwA+gGKuOBm5DDxwLER48iRI40bNw79pHr8Q5rDm4vSGfkcSNcT8CEQt8Zh5KKWPboaLnpTEd6+7IGw79i6SVvADJIwws9FLXvsO3/+PHqqByExuHXhIF2WvZLJ759//rl3796g5kZCiVyzZk3lkzB0IG98ID3cyfgFKogwIgcopvJOFAiwoAMHDjhW/gWjR48W4y4K8GHHwmlYoM5qXrt2bdOmTVu2bBGm7QCc0BF+7tw5npUpIceeLhVBWoFs+01z9erVMOE45p8M9O/f/9tvv0V/gvPA3hcsWABr1X1ahgK+f/v27fNbEB00Vvv27Wm1rVu3fvPNN8uWLYOS9erVS1+29QbKQSyEE9ZH9vwKAPWsvONY9jKyjJxBe0og0b1JIA8eBacIZ8+etWxZcjccz9I3vXWUG9FAVilaWPKcmEErJ3Kml/hzGGvQix0nTRI/ZPO8Nxf1C5lYDC8XZVwyXDQJ4GZ0BIelDwODoLgpXNTAIC7Yvn37zdjLGp9Ak65YsaKo5kkYNBONFcdE+vXr16ZNG3d4z549YzqtEBTw3ho1auiOghReeeWV8L7LwMAbiZ/pJf4cxhotW7bUj4XfEjBc1CDsCHtHkJM7YUzQIBZgrNi8eXNUVBS/+oQ1KtCPP/645b9wzHQz7G/bto3wuGt3ocNIjEFiwbJlyyIjIz/99NNy5crRfxI6O7EHPb9169a6rZekhAsXLsAeoXOjRo1q2LBh3BMsVKhQyZIl9cV2KOiiRYvefffduCfuwIkTJ/hMPv300+LtRnDlypURI0asW7cu7K8zMPBAIKZ39uxZhsFp06Zt2rRJnWTZu3fv/zRY9gFCwaFDh/THGTwdIZa9LWLevHnvvfeeOqiscOPGjW+++Wbq1KkLFy7U1+c9cujGkSNHZBM7XWzu3LlLly517FC4du3al19+adnGkOja+gL71atX169fT+Bnn33mHjYvXrwoJx0uXbrEn9mzZ/tdMz948CDv/fDDD9WxZwWqbvfu3YwqS5Ys+eSTTyjva6+9RrnKli0rFajmvHiX4xiCFaA5VM7J86xZs77//nsKHqOtibt27VIteO7cOapLb185psRgK5eyWV3nolItM2bMcLc1jeg42O+Xi9Ii0u78+t324gYVhSJLVXz11VcMm365qEdDeN9FbsX4OTUzffr0b7/9Vh+lg+bZQ8DccIiEatagdeLuR3rDqTLKpaMVzpw5I32EW8iMsj2+c+dOLhEkWlk5RFR1Iu1LcdRb1KuhEBICc1CPeIirAxQ/UEcAPE4r0JGVefbLly/rInrMhrqUxlq8eLEcOZHAoNuU/MrDDz/8oJJFGBB1dZnk5/fDAlRQOe24du1a+aO6w59//ul29+2QOgYK9Xi85dlwUYPEglq1asmhMsdJ0VsODMchWjS9FcHXVJoJDTUsx/nkwGSqVKmqVavWuHHjhx56qHr16t62IuOC9u3by8HFOnXqNGrUCC2tQYMGYp7KwCA+4ZfpoUa3atVq0qRJr776Kp2ifv36cgQADbtTp07S9UTnFrviAwYMEG6GlhYZGVm0aFECUa9VgmiQnTt3fuaZZ1B20aGTJUv2xBNPKD17+/bt+fPnHzJkyE8//TR48OCIiIiPP/7YO4cOoJrTYYn2wgsvjBkzJnXq1HIQPUeOHOiUlm2Fu0OHDnfeeSfpbNy4MUOGDNytWbOmPL5ixYrixYtPmTIF7Z8iMxT06dNHxk8iN2vWjCzde++9KEaZM2eWc+bEgYOpDBC5R48eXbt2JZEWLVrwdvE2hHI8YcIEMbGDai7Gon22X98uXboIjxpogxTIRvPmzXmXY9UxUHNYthpdpEgRis+f4cOHk2DQMx061qxZw+t8tq+sSzYGDRokOXz//fflED6/3bt3p+qEpCkuCoPKmjVrsWLFKGy6dOnEbR5EgtyKfSOe0t/l5qJi02js2LEjRoygpRAbh+MlN3h75cqVSXn16tWTJ09+9NFHHVw0UEN434XAI3hyLB/yQzNJK8uZfL1KA+XZW8B0BBKJqKiooHUSqB+h3IuxQCBnK44ePSprg8p+O+SQTxvy8/TTT4vXcUCpufXGG280adKEItCIJUuW5BWWv75M5T/++ONcZsyYUXkUg6T17Nkzffr0q1atkhAPcXUDmufuCJZtE4GaQRqpq/Lly2fKlEnywF1GHjl7TGZomtOnT9P3yfby5cvF1TmFQiBFiwPKs5obHtLCuCFinCtXLoSWSn755Zfp/jB2ihwoQQMB48C6desYMGViEcnhPxIuwin2evbs2XNGg7hSEyDnDE3r1683XNTgNgU9B1Xmiy++SOiMGAQBmhAfbLdZsljj1KlTM2fO5DPGN55P8s0+Z843eOLEibwOHUI38mFgEJ9wM72VK1fqdlx79+5NBHWa699//xUD1GLVuW/fvkOHDlWR0YnpkmL5VueirVu3bt++vbpEPfVpPnjKli2rO1LOkycPWrhaTgmFi6IdokSK4ogqLKYiUNkJyZs3LxonIYzqMgFEzOPHj6NAjx8/3oqe2EKRVam9+eabhMC6pUTiCTlt2rRUxeHDh9GZxDcvmqvyFYc2r5ubhsAQYdGiRSjHJ0+ehJNwicYMSyE1COeJEyfECJC+NREVbe7cuY4dsN7N8eSTT6JDq7vQGMeqclB07NiRBNHFVQhvJ0RPh7sUUP4LF0Uph7HIyXNx8gwpsmzxgB7IhIU3F2W8heeoNSvqn7ulSpXyOBNBzRcsWFA3vk0NO7hooIYIepf8CLMtV64cbAfGSFZLly5NCJUcNM8eAuaAh0gErRPvfgQTVlxUQLdSXBTp6tOnDxGKFSvGl46PDqlB6ffu3evT3C9v27ZN7C/47cuUiwRTpEih87GpU6cq71ze4uoX7o4gx1hk/VZyDteNiIhQMglF8dku9+jaVGaJEiUcfq3vuuuuUPboeksLkpw9e3a6OVVEE5DD+ORFtzQYfsVwrIguDUprEiJbz2hH/nvMmm3duhUiKtEMFzUwMDAwMEjKcDA9FGXIG6rq39FYt26dzzZArRTiQ4cOoeOipS1btqxatWruTaHifknpr0uWLOFS3/i6efNmdHFZsQRo5BUrVlR3ZXOKWksJcY8umZGt7yqEjIkZc/FNCpMRSunY91iyZEmKrIfAQ8ROtWxVuHTpkjsDQnRFaxeXQgcPHlSVNmzYMO7Wq1dPIotGPmjQID0Ftwpu2bq+zkWDNgdU4d5771XsBVYTU5Nm4reZdlQhY8aMIWT06NEq5JFHHvnll1/kv3DR4sWLq7tSsTohnDNnTlAuSks9++yzqlwkImtZSircGDVqFBH0g2cwIv3V3g0RtJnEyr1ynWVF2+kFsuzvnedAAuYXfkXCO/2g/Ug8V+lcNFOmTLpfayG3yseb4LPPPiNw4sSJKgRuqf47+rJl28z3/dfFOrxRpC6U0cMNd0egCfLly/e3BiTQIZMy3wGTrFu3rnvxIBQuGlQewIIFCwipXbv2iBEjXn/9de8EDRSOHTsGjdRdoCOlhMgwArfn/759+zZu3Lhhw4Zdu3bpi6KnTp2SLbuIuuGiBgYGBgYGSRwOpieLJNCGx13Qz/PIwmBERITf83jilEjpr23atMmRI4dHHv61YdkkcNGiReKbR1GOELmoqNQOk9pvvPEGga+99lqgdI4ePep3L6Xsohfd948//uA/lE+PsHLlSgIrVKhg2bp7smTJ3DXWtm1bPRs6ybECcFGHZaCgzSGeqAoWLKiv68YU5cuXJxHxQQV69eqls034GOp+oBwKoEzp06dXl7Jz25uLygZUd7nEL7dfED9btmx6iMN2kXdDBG0mqUyZuXBkW9iOd55jZGTLr0h4px+0HwXloiK0+nyNZav+wni7du3qPlrp6MuWvaPeZx/vlEsYhRKPEEcPB9wd4cknn6Sh3YmMHTtWxaFXykyTXyv6oXDRoPIgaNKkCUmVKFEiCR96CjvgnNBIfV5p8+bNhEj337p1q+Mo6bp16+SsL9K7fv36H3/80bKdPhguamBgYGBgkMThUKBl02NQYgN1RBn1RZ8adcChv5YuXbpAgQLeCV68eHHYsGFowxs2bJB1UXUOPC5cdNasWQSKiWy/6chKkb4qKxgxYgThopX65aKHDx/22RuA+S8H3jx8ZcWaiwZtjsuXL9epU0fW7ho2bBg770rvvvsuj/ft29eyCwuzlVVfMXvTs2dP/fhuIC6q77IOykXPnj3L/969e4eeSVTVFClSQNX0QAcX9W6IoM3kl4s+99xzBM6cOTNonuPIRYOmH7QfxY6LgqVLl6ZJk4ZbMMD3339fv+XmoqBatWoEinHHXr16LVmyRMJDHD0ccHcEiN8DDzwQ9EFyxYPEdC+6hsJFg8qDAIGnDjNnzuwwaQa7LvJfTJs2LWiebxO4ueiWLVsUF922bdumTZukPhnBZPuu+AUkwpo1a65cuWIZLmpgYGBgYHA7wKFAz5gxw7Fhzy92795dsmRJYubJk0eZ4lRw6K8QNliE2x6pQlRUVL58+SAwchlGLirbGsVAi9905LBorly5HKnJGcg+ffpYAbjouXPn1IJq69at+f/TTz8FylusuWgozYEi/vbbb2fMmJGYd955p27ONETQgunTp6dmSGrs2LFU18aNG0mtY8eO165do6F1ehMWLoreyf+mTZuGnkkUU599TlUPdHBR74YI2kx+uehLL73ksw0LBc1zHLlo0PSD9qNYc1Gwf/9+OcIKnn/+eRXul4uKnaT27dvfuHGjXLly6o0hjh4OuDsCowqs2NsAr2UvFBcsWJBnx40b57gVChcNKg+CmTNnylscFvvPnz/f4b+Iy96EJAYxouveo+vX/Lhs2WXgQrYhogw+B2xs375dDp3yP34WpQ0XNTAwMDAwiG84FGgxCqKfHhTAx9ShLDSGypUr79q1q127dsJYHJEd+qss3KG/OqKJpnLq1Cl4lL4LNIxcdMKECQTKuo3fdC5cuCD6t8Mct9ikFXrsl4vu2LGDQIgK/wcOHMj/fv36ObKELoWebcWBiwZtDuVa47fffmvQoAGRW7Zs6V1RfiGHAKnD4sWLi6O/EiVKQPzg5I6VurBwUdoCWsUjbgurCxYs8JtDmEnatGlJQT8Q6+Ci3g0RtJn8ctEmTZokT578zJkzQfMcRy4aNH3vfmTFlovSImIw2bIXNsUCsFSIFYCLMgJA9tKnT09Dy3yNIJTRww13R+A/Icowr8LHH3+sSsf/Z555BpaS1oasqimEwkWDyoNlr+/df//9tIhMvX300UfeaRoITp8+7VjSFKO4jB50ZDmdq26J+xaGsmvXrrl9vQhkpfRmw3BRgxgDmQ66uSKe8c8//xw6dMjhsfemgl599OhRD6sAsYZ4lnNA/0beuHEj6Vk291tqBzzM08cFHvVJeHwKVVAgbw6jhX6hDgEqxMjzYaJCGM01JzY4FGjEG/2VkGHDhqk4169fb9Wq1YkTJ+QS7U1WGpHM3LlzExldQU/Tob+OGzdOCIN+uBStV5R+1Dvu6ly0UqVKvmhrMe4cBoJfLgo9K1y4sOg9gdJp3rw54SNHjtQDGzdunD9/fjFC45eLjh07NmXKlFKiNWvW+GwvL3o9HD9+vEWLFtIF/HJRWQdzbA92ML2gzSHbjwV0zHz58hUrVkxdov+F0lUt23WNz3aB06NHDwkRC0YZM2Z0aPlh4aLgoYce4vKxxx7Th4XRo0erDZ9uiJ1b3Y6uTCXkyZNHLr0bImgzubkoynG2bNnUOqF3nuN+XtQ7fe9+BBB1vYYvXbqULFkyyqsi++Wi9FO9zmfOnEkcNSPgl4ta9iAg6/C6a9lQRg833B1BHAvRrPrAGxUVpaZFTp06Vbx4cfHzKYL68MMP658bniXQ24hUUHmgB9EiRLPsZb3kyZMjDCF2qNscNLpwSDmBjCgqSslwKv9F4aGSv//+ey73798vJqYVdu/eLZ5g+H+z/RoIDBc1iAG++uqrLl26oHOkSpVKHGElOE6fPt2+fXu+GX379mXAqlevXjzsKBg1atSAAQNq1KjB6P/BBx+EMeVNmzZRip49e8rlxx9/TG2jdCq77Zat5KF8iIXupAFHqR1guOzWrVuBAgXQV27G2/3WJ5/5tm3bDhw4MCIiokqVKvEzNegB8X2XNm1aMQZj2fQSVcDhwI1AIowYMQLtc/r06ZZ9bI+Kbdq0qXsNLZ6BEkM/DXEa5dixY127ds2SJYt7D2eSgZxSQ6dUIbIk6LPd940fP/7NN98sXbq0GmHQDEqUKKE2Cn766afEhLbpBvqF3dHocslgKFryHXfcwTiJwDz11FMIkih8X3/9NbcYzJcvX759+3aGUHoZIXPmzPnmm2/85tAvhIvqLjFWr16dJk0atXFObK6mT5/eMXmHlpw9e3ZomFpw+/HHH+mMfGjkUrgoOdyxY4eEoLAyHuo+qMXOZ4YMGVq3bj1t2jSYBkWmOHIX+uT7rxVQgKKMHkwOYd2yS82yXT0RE0oZYnOUKVNGakkAjX/llVfkP32Qp7JmzepBA3SUKlWK/Ci3GTQol7Vr13ZEo7P7og/KCmRxksFTScXkyZMJee655/QHZWVJ1aFYWAX3339/ZGTklClT+G76tUOjsGXLFt7CI9QJUnHu3Dk58kfgxIkTpfm8G8L7rnBRiJNiNYMHD4ZbqlO43nkOJGB+4VckvNP37kdWtG1nhlnaCOl99tlnZaoIviojnvRW3U6sZXNRfU2SBymCkhlHX1ZgbEyRIoXuvkXgLa5+4e4I5BbWJ3S0e/fuMHbK+8ADD0gp+L5A12fPni2PU9tifIt3qTRl4oOCQ489FjO95QFGrW9XlibjS30zZv+THujpNCU6w08//SQnQuX4AOIq5HPt2rXc2rhxoxBO98SBOS9qkHiBlqBspjM81a9fP6Fz9P8X01AdxMwDYERLnTp1TJ28xRR87BltLXvCCf0DXhrGxKFA6CXKkzuqmFjy0Llov379eG+Cs6MwwlFqBxA52e93k7iouz6vXbvGl1gsKL7//vuFChUKZdn2ZgOtgkpQajraoS/aNowCypP4KkBTefLJJ1EaZNKaTzukLugpoJsKmUSfOXNmiPH//vvviIgINJWbmquEAropWp3ojh06dFi/fr1l6wqoyGJaU3imMl0zdepU9GBGHuWNUFxx+mwviLC+n3/+maYXOyhFihRRng8hNmjAyZIlk4UIOpHSPHidWKr02WZISFkMDjGKzp8/328O/UK4aPXq1UmklQ0UerV9kX4kq2qgRYsWjsW3U6dOodPDgRnievbsCQFTe1+taC6aM2dO8olId+zYsWzZsg47JcSBCaCdyytq1KghGi3jM5Q1c+bMPnvVkYFa/zSgZ0uF0GWoB+i3OrPXrVs3MSbp0RyAwpYoUYKetWDBAroh3U1VrDioAIHGNAdgPg4LovAQR0VRn6oaO3fufPDgQUaAZs2aSQh1TvO9/fbbZNJnr6mSB+qWOF27dpU4tWrVUmtuCIxsKxU+MHTo0KBbJ9BNxXqqz14hJD8QUbLEICMbTQM1hHczCYSLUmroE62MxMJVHHsiAuXZW8B0eIuEd5149CMAlytevLg8W7duXXIO/6cX8PmmFZDYokWLcoviv/7660pjgYvyoWnYsOHcuXPfeustercYJAvUlxUaN25M93QEeotrIDg6AiEHDhxAtiURyotkyoIkuZK96Mp3686dOytWrCgxSefy5csELl68WKYtqlSp4rGrKJA88CEWBz9wUfns8itU32e70oUzBy3UbQ7kFvKpNtkyCKi5KtpIjo8KNmzY4LeNkgIXvX79+q5du9bbQFL9buZE1qkdXTGSPZbQ9DVr1jDGIfTxsy5sEDpQR4KaZIxn8F0pXLiwHuJhXSBc4Nugz9jdbNCPfP/lorchxBFfuLho//79vSPIPrebPakRU6CAojHI996yRR351xV3Rk5YhOgN3L148WL27NmVyqK7EYsfoKvpu6qozzfeeMPDy7YDaGy0gsO25O0AvobwisOHD4dx7gAtHFXP78a5/fv360o/743pZni1RxcdiJx7+JAIBNSGHTt2uNfM9T26qPvK94kbaBqoXzHaxYdS63ak4Uag5pDKJAVGJ7dUnz17FiV+xYoVoeSE4js0QlokHpaAqFKKFiNdi14sO4epDb8N7d0Qge6qPbpQEQRVjXJhyXOM4J2+Rz8S4VcWX0MRRcZkqpEHqVK05dALJWf//N6KxejhtyMgkLSUR0N44MSJEyH62o1FtzUIEdQtFUsLOiSBS8SYIYvxNvGsM4eZi9KX0IfE/lJUVJRYc9J1IGpBCDfQK0h2J4uvG/mzefPmhJ3FN3BAXHsndC7+g0qVKomXuXiD6Ebe25nCC3qQ4aJh5KLwTN0dn1+IYuQwqZLgKFSokNs0hY7mzZvrvtQnT54MNY1/CirgQ1irVi0UrFinIDsCEtuMgIEbfs+LhgV+z4veEoCnPfHEE4lH1Uvk8Gu7yMDA4DZBmLko2pss+/7111/wUlkLllm069evb9u2jVtqdVhRTbQWCZEppXPnzsmlmSxJJNi6dSsafM6cOe+66675NuQEPy24cuXKPXv20FITJ06Ug+aCLVu2oAoPHToUNcWxNo4YyNYRHhwzZszs2bPFM8Hly5c//fTTyMhI/RBOIBw+fJhs3HnnnQULFpwfjRkzZgwfPjwqKsqyjyCqcGWZbcGCBbL3TKXz9ddfDxs2jKw6rET4xfLly9955x2f7U5AUlY+FdauXTt69GiSIkH9EXSpOXPmINjI/6JFi8ieWsjatWvXhAkTxo0b59j/uW/fPn1rjZuLwi4WL17s0NG3b99OUqNGjdq4caMeTuW///77qPWUnd4XtIwOSNMLLl68qF9KatSALhKCGNWq31Jb9sreihUrhgwZMmvWLFkic3DRQG+hBmSnE2MIj+vJIo1p0qSRLYhA5qH1+jx+/DjhYk2UlKWYNK4qtWzes2yXFVx+/vnnQYtG+06fPn3gwIHvvfeew09aKLho48iRI2RJPyZn2VPX6j+SFhER8cYbb6iQqjbcCdJtT5w44T5WTT5lTD5//rxDh6Yt3MycDqu2ITjWhUifPsKI4X6FOz+UQvb4cVd3UlKnTh3otzu+QWKD4aIOIP8tW7ZMwma3wg7DRQ0MbmeEmYtu3rwZ/e+XX36RS6GmsjkehU827spRWp2Lnj17VpZS1e58oawqHYOEBewRHpUjR45s2bItsoH2D0OQoynQM1TeZMmSicZw9erVtm3bPv/88zQf8vDQQw8VLVpUCBhPPfnkkz77BH///v2bNWtGtOTJk/Nn9+7d/Hbu3LlChQpEWLZsmXeWhItCKgoUKCAk4YMPPpBDI2+//bZla8+NGzf22QfqlFxB2KAi6jRRixYtKAWCh96QNm3aoIcrIN7impxCST2QCHymadOmDRo0QKWGqFBFyroMiWfPnp34UBEy07Fjx1KlSlFeiPrIkSObN2/erl07+EP58uUlPmIvB7QoiHqpzkXhD9B7Oe6i+4/q2bMnLBfKxF2duNIWpUuXJp/UAKyJMobY4goXLlwoVqyY2ioJ/RD/4zSc2qc0derU4sWLy3nLWNSq31KfOXOGSoZCQ95WrVpVrlw5nYsGesuePXtEBshk+/btmzRpcv/99/s004LIFQJDnUvzUQRHfaJEEi5cdMqUKfyH2UIFxcM4QqtIGoomshTUQ1pUVNQdd9wBbSbPL7/8Mp1IJ+3eOHToEJ1iwIABNK7YVBT+v3///ldeeeXuu+8Wi5p0KyqhcuXKPts6P/+rV69ev359Lmk7LpU8MOTSO1588cWJEyciqOIOGxrJZd68ecUKJXWOiKpjqJCBrl27ylk+OjitfOrUKRqClDNmzMioTg1I66gDbzRKjRo1hELwdipWmol6Fj8cCjt27KBfjB07dty4cWK/UR1QQdSp3gS3t2QQCqAQPpcPwLAAFcJnG0+6tRYY6Re3ruXqBIE4tnE7qzQwMLgdEGYuKjxTTQei5QjJ1HfbCvN0rIsSU4xEW7bCJP5wzO6sRAU0S+VMTNCnTx++H40aNUJxRCWVxSh01sKFCyvVAV02d+7caLpy8EDmudGD1ckfOIMosvLxluWdxx9/PJQspUuXDrKhLhcsWODT3D2jyqNV69sakU+l3fJeZWIODTt9+vRZsmQJejpCdKNnn31WhUA29I8oBUmZMqXiadQGd2EOUiFQHSm+sl4g9uU3bdokl2JjPRAXFYifaMVF582bp9u9EAsccnfhwoW6DUyixWLfuzjRVuYKjh8/nixZMt2iDOxFmeiIXa26S123bl29kufOnatzUY+3IIfEhHCKiReECtnTF+gQGN0FguWqTytaMdLnwqSVn3rqKRWycuXKUMzq0ByZMmWS/7K26Xaq5hdwYHqcMu+RPXt2OK1ScKWYuuXhHj16EKJG0aVLl3KpTwScO3cOgtqlSxfx+EKNjRkzRt0tUqRIq1atoPd0n4oVK8oCLG8pWrSo2DvZtm0bCW7ZssWyiWKqVKmg+vRiBBjNu2TJkvoaJvLss82xqhCSJURfRqYC8+XLpwpIRWXIkEEttIrR/0WLFoVSVwYJiMmTJ9P6CHnWrFlffvllx8aQuIAPyiOPPJLJxpNPPil2oQ2SGC5evNi3b1+GaFq5YMGCjDxqH5OBgcFtgjBzUSGZar/W77//LiH6mWw3F3UAjU0YbGJzYnmbw81FRb/UzXafOXMmRYoUjtUP8Wus2Frq1KkrVaqk7kJyfNGezQX58+dHMw4lSw4uiuaqc1HQokULn+Y8Go4htq2FFQwbNuydaKAWE7J69WrvN7q56Pnz57t37654i5iAUw765Mybsn0KYBR66cQ4qiq+2Oj35qL817kTvIv8qIKIqfQBAwZwCzLA/6FDh0pf27FjRyyWF+B4GTNmLFeunAopXbp02rRp1XZKWIQsisa6Vh2l/u6777gUM7YC/byo91vEBZ/udL5evXqEqGOTbi7qqE/LHxe1bLOZyLaaIIPYh7KZHCKnrCBSY/r6oQf27t2bJk0aZTof7pc8efLmzZurCOjlJKXr/VWqVNHlCvWOCGpaEAGoXbs2ZZehGM5JJeje8Eif6tWNQtOX77rrLtWXn3vuuWLFion8QCBl3ZiuLaIFD2natKl6duTIkfrbLdvnAfRVzUrQDVOmTLlw4UIVoXz58k888YS67N+/v06tDQwMDAwMDJIkwslFUUoc5zzVyc8QuSghBw4cECIaurlFg/hBIC6q+2KGD7hPtYmXZ7WI5OCicgJT56Ko1Dly5AglS0G5qCxniYdu9OBatWpJ+LJlywj/8ssvv/0vgp7wcXNRvewwQCiBT/N57eai6Pc6ZxCTrVOnTpXLmHJR8as2fPhwR0GEflNk8YpWoUIFtRIbC3Ts2JFEZAkLmiTOrGUt9IcffujUqZNEi3WtOko9ZMgQvQ6t/3JR77e4uWjDhg0JkROJVhy4KHKu8gCzve+++0JfZGbQGz9+vPBDh7tzN0i2evXq5FOlv3PnTtnpreK0aNECsqpm6xhgudRZbp06dfLnz68uZcbniy++IM3JkyfD3vUJAjnvBxXUB+omTZqkTZuWcRgp6ty5c9myZZWvvzfffBPuSr3JfATCxuPvvvuuevaRRx4pWbKkXiLEXtlV4rJy5cqlSpVSBbxw4QJMVd+hV7VqVd7oXVEGBgYGBgYGtzrCvC4qVnCVpW9I6be2K1U9TiAuinq3ZcuWb21TuqFYWjeIZ4TCRT/66CNC2rdvr0eDvRDYuHFjuQyFi6K5hpKloFzUst2IZ8mSBel6//33lTY/duxYB9sJEX656I4dO+BRssgjNhhiykWpBLmMKRfdunUr/997771AGRZzjj4br7zySuxsU8tbhNK/+OKL33zzDXQUvmTZtE1ZY4p1rTpKLc7ElB9F679c1PstN4+LUnVFixbNkCEDxGnJkiWy8hwUsLvIyMjWrVvTELJBPSgXldN3uotzOUupqOA///yDSMP3VASpHyUGZPWOO+5QL0L4M2fOnD59+qFDh3bq1Omtt95y7JoWD4S69xQxFlWmTJn+/fu3a9duwYIFuuRAdOnFyo+feH9VRvyvX78Oie3Ro4eKL/t7hw8fLpfz5s3jcu7cuSqCDAJqvy4VlTJlSn0HsoGBgYGBgUGSRJi5KBoMZFJZXBT3LQ7rnX65KLqR8Fj0WreBR4PEgFC4qCidumMJK3pHn3LqGM9cdMqUKaL41q9fX6ngsnlVMUCFffv2eb/RzUU3btxIiRYvXiyX8cxF4ScO6qUXRG2jXbp0ad68eR1razEC9ZwtWzaK/+CDD1rRWyi3bNmit3Wsa9VRaqFGn332mYqgc1Hvt9w8LmpF74wdNWpUixYtQjQR3KhRo/vuu0+dhQ6Fi4r5JTUfB5NEZvRlRjmNCaVUIWJSSzlQoSq4VHuDZXfA888/H2hoLVy4cI4cOfRF0cGDB8vSt3vygsaKiIioWLGiCqFn6SItRz315nvzzTcJ2bx5s6qTFClSKOE8c+YM1PrOO+9U7/ryyy8dvcbAwMDAwMAgSSLMXBQdCD6J4ihaBSSEy127dulx3FyUP0JiUetRvP6KhrFEl6gQChel1QoUKJA8eXLdd8XChQsJUc4w4pmLQgAyZsxIml26dFGByCQxc+bMqdaaLFuHnjlzpvcb3VzUsYjXrVu3+OSisvuR6tWPDlL5vXv3tmyzIqohTp8+TT0o6zt0tBi5C586dSovLV++vKyGwdN8tqHUadOmqTixrlVHqcVaUrNmzVQE4aKy1Ob9lqBcFBKFBOpvD52LwuVy587Nqx977DHvEgkOHDhAOhBXufz9999D4aJ33323Lv/Dhg1TZZeTC6NHjyZkx44dp06dkkZ88cUXM2fOrEZUoetqvZom43LIkCH6W9RJisOHD6v0FV566SUCv/vuOxXyzz//iEeWFStWqB3alr3wmyFDBsSe/yL2AwYMEKqp6Hq9evWyZs1K9mSasmjRolSjSpn6L168eIMGDVQBX3311ZQpU16+fPnQoUNmj4yBgYGBgUESRpi56MWLF1EKYZVbbAjnvHDhgh7HzUXVsVIHUETCmz2DuCBbtmy6UVYrerekbi3Tstc0kiVLpojfjRs3HnzwQdneadkaLcRJPwkmJ9n09br8+fPDmoLmB/lB5S1RooQKkc2Nuv0VgayzKTIsaNKkCYGoxePGjVu5cuXAgQMd5+X8QogQz6oQ4aLt27eHBX300UdlypQR8inLdLK+pHs0veOOO3RFXGwXUZNySe/gskaNGioCHUHtj9WLo877yQ5JqEi/fv1gpNDaKlWqiNIPLdcZCNTxzTfftGwmmSlTphw5coTu7hJqkT59eqpLddtatWpBQhTHE8SuVh2lhvIVKFCAEHILZ+YSriVMWE69erxFmFWjRo1U4g8//DAhyrMlnEeYJ8xQrMI66hM0b95cyJ47q7LMrm9n9YBwUZpm06ZN27Zt6927N12jatWqtA5DZaCnihUrRh+RFpw8efLbb7/tsz3vLVy4UFY+yV6WLFkYV5XYlC5dWjc9DZOkfdVcnhiUpvbEvPOVK1dIVk0RypqqTjutaLGkZuTy6NGjvEtoIUSRfqfqc/PmzT7bgNmkSZNkxH7ggQcqVKiwd+9eJfYMHTQZmRe7uHR/HhGmOm3aND4ZERERkZGRs2bNkjq///77kWFepwpoYGBgYGBgkCQRZi5q2dPtUVFRQiZRMtxmS9xcVNyQGi6aaIG6KR4jACRTfLegOMJtCClevPh7772nb/+j3dGnmzZtiirZsmVLyJKE//zzz5IOGjkaNsr0smXLSpUqRQjKNP+hB0LeAIq7vvDlAMqx7Ib12XZiEarly5dXqlSJy4IFC6qTbILdu3dXrlzZkQLkqlWrVmjVPMJvx44dHbTKDXJYt25d4qdNm3bkyJFCbuEY4kQUhRsNnrKj9xMBRRwFncxwq2bNmmvXrj1x4oR4cPHZjj0oHdRR/KnCqIlPnKeffprL1KlTw6h/++03AsWzJfQVzkDngkXI66BYK1assGxOPmLECN4oKdepU0f5y4Ee3HPPPX369Pnkk08oYJs2bYSw7dmzJ02aNL4Y+nODb+scbP78+cpqUVxq1V1qy6ZPcDYCySeVM3fuXHgv+Zfl30Bv4SlJisjwWGoGCSRZQtq1ayfi9MUXX6Sw8eyzzyJvjvpkLHrrrbdg3YTUrl2bBlVeRgQ8ki5duqCF0itNBL5+/foMhuK59JFHHhHLw34B7SR75AFSh1TL0U36mqKLlMWnuXglKUSOgqgUeFA3umvZ00akmTNnTkSRx/XFRlgiNeAwsAyPFRvUdGTqgS6mItBhSUTFFO8yhQoVUmcx8uTJkzJlSjqIisNdCPno0aPlcs6cOWQGiYUer1q1ivxzmStXLvqORKAjZ8yY8eWXXzbnNQwMDAwMDJI2ws9FLXvtC10HpS1GmwANkhgQAGXOJMFx+vRpv+Fo8xCzOHoP4nFotppbESs1cUkwFoA87Nu3z7GhUVR5srd3716aQ79FwceMGRN096wOUtC3zdO7HWnqice9Vi17x4SIEEkpl61xfwvCEGsz3atXr37hhRdi9MjRo0fVKiJjo3vrrxuI0LZt21TRduzYoVsbgh7rBx/kOKhyI0SjR0REKP+rCuRh69atMdrySs55tXKHEwgnT57UqfWZM2cc04jIicqeQAqoUnYsFNN9bgcfg7SU2kARCN9//z1NqZ/aRXS9l+XpF1OnTlUTUgaxBk2jb2lxg3bZtGlTYj7YTM/SjYTFP+jmMmd6q4Ahet26dRs3boxLInTt5cuXiwO5xAlHu7jHmXgGgjplyhRzIuO2xU3hogYGBokcDPpt27Y1LnxjiiZNmihzr4kEgwYN0j1zrlmz5q677vJYdzVIcKDz9e7dO2PGjI7z9m7cc889xFm/fr1l21+oU6dOsmTJHAeeHYCpyv6IMGf6dgKNUrx4ccfRfR1//fVXZGRkrly5QjkBniBgHBAHYw4rD/GGadOm5c+f3xfABVrixJAhQ7Jly0aeR4wYEbsUDh8+3LVrV9mm5GHfPgHht130cSZBQGZ8ttvwhMqAQcLCcFEDg9sRY8aMcTj2MAiECxcu9OvXb+bMmaNGjWrYsGFCZ+f/0KJFi1WrVsFqihUr9uOPPw4fPlwOA7/wwgsO810GiRMtW7YMykXHjx//1FNPqa6KKAblokeOHGncuLGy7K1gbAHGCOLHOBAXFYjhvcTJRS37UEwCclEAGbu1uCh45ZVX4sJFBdK1EycXtfy1i2OciX/wLePbqkzBK5hR6zaB4aIGBgYGXvjuu+/kLO7dd9+tHFYlOCpWrNijR49evXqJY9vXXnutWrVqs2bN4k9CZ80gJHTo0CEoF3UjU6ZM3lzUL9AydUPiBkEhtru9uejKlSsTMxcV++QJyEW/+uqrW46Ljhs3Lu5cVAxDJFouequ0y8yZM6OiohI6FwbxAcNFDQwMDIJgyZIlY8eOdVtiS0D8/fffGzduVF46LftYqYe5L4PEhvjkoi1bthTPwAYhwnDRuONW4Tw6DBdNJNi6dWtERMS3336b0Bm5JYGusnnzZpg8v7pW8O+//zKybfkvlOGPn3/+2XHLYejh5sFwUQMDAwMDg/iGzkV37tw5ffr0L774wmHQ2LLNmOu2oBQXRYH48MMPZ8+e7TYRd/HiReVwmARfe+01XlS2bNn/2VCv4KWzZs367LPPjh07durUqRhlHp1m7dq1R48etWz71aTDpUpZTOYsXrzYfSL92rVr33zzzdSpU/l1GyRD9Zk/fz53Sc1t+9CdYeJLoZQ1LzQtCXGYvxL3cpcuXZoxY4a4hvJ+o85F9+/fP23atKVLlyojZAIHF923b9//NEggL5XLn376KbSqDZLhs2fPfvrpp+Rn06ZNbmMzNAE55y5848qVK4qLnj9/3pGxgwcPyqWeuADRopKnTJlCAd2bJL0zQIuT83fffRe5jSnn4V16BSoLc9u3b5cQXq0i//LLLx9//DG9hmw4rJ0LkDRy8s477yxZskSfsxNAdd634fDdpXPRdevW8TiJKIPeNKLkRDbIEK5ye+LECZWIXy5K6UTyFy5cKB1Hx969e3fv3k3zkVvGhJMnT+pVIabdqG0V4h4ovBG0XdQ4w3ii3qKcVCMSEqIbZPKQhDNnzojhdx6hz6r6p1x0t48++ogO65jbpU6UKHI3d+7cZHLy5MmkQCclcngrJAkD8im+SBjT5I/6RogYOKAG/w0bNjhuxZsRQcNFDQwMDAwM4hvCReGTjzzySL58+bJkyaL7LkbPi4yMLFq0qGPtVLjosmXLxPMQSJ48+fjx4+XuihUrmjdvHhERcd9990kIWl2XLl2Ekwy0IYo16jLvgregf5QsWbJz584hZpvHeTZPnjw+23Ny165dixcvXqhQIS7r16//xx9/tGrVipBixYqJOyv9WdTTRo0ajR07Fl0/R44clA79W26hVr788stkOyoqatWqVfx5+OGHdYPkfjOMiix+wqpWrSrRYAvi9EhoJCpsv379xLcWCqvkKm3atOhk3m9UXLR///7JkiWTqs6aNavyPGS5uCiU9YEHHiCkcOHCaPYSCCF866230qRJg14YSvV6ZNiyvQFTvZMmTXr11VdTpUpFhev+23m2cuXK3bt3X716NUo8mVdclMfnzZsnpRDKjeov3pIdy+wTJ06sXbv23LlzoaN33303ZTlw4IC6652BjRs3knPoHFX6+uuvS22EzkWhE4h6ypQpxXucsqq6ZcsWpIV6lrkAiE3btm0RpOXLl8+ePbtUqVLIG3RITwrWh0hQCbQRzUqvoThyiwzXqlWLbkITz5kzh1v6uQbhogMGDBD/bYKyZcsK+YQA16hRgxCk0bI3p8BXqXPHUqqbi0Kn8+fPP2TIEORz8ODB9FCItGUbwZowYYJYmYLUyUFTQG5FjJE9iimzNkgs4kcIPShGNm892sU9ziBFjz/+OJcZM2ZUtQr369mzJ2MOPUVCAkkCY0Ljxo0Job24K8WhyHKrQoUKtAjEu1mzZrSaNDpJSa0iupI4DVeiRAnJJEMWwxo9PYwVkoQhhqChkTLfQWvyn3aXXi8+NWGYZzSIQfsbN25wi4FLvxVvLiEMFzUwMDAwMIhvCBdFk0Z1sGxPNqIRCo2BPKBG3H///W4uCvlEF0ctRjVHvxSmhIZn2aoGLIJLxUUt258wIfoeXXRBQhQP3LZtW0w9FTVt2pQU0CBlWQk9Rtw7E6IMTTds2JAQRd5OnTpFARXBQKGU4suCBnoql2J/C0yfPp3Ld955J2iGeZ3ORQEKtOKiUMGDBw/eeeedhLRp0wb9DDX3+eefD/pG4aJZsmRBjSbPhw8fFlOf1L9anXPv0ZVX586dW1+lGT9+/EsvvRRixXpkmNfp5pF79+4tnE0uUSjhG7BrFWHRokWOPbqSrL78my5dOp2Lzpgxo3Tp0mo1e8yYMcSHNqjyemRg586dJKV7wZFJkJjuBZWnoEwqBJpB0dROQvIA/VPc47fffsuXLx90XbnL2rVr1x133EE1yiVUlgSzZ88uj1BFXCqW9cwzz3Cp1n+Ei5Lg4sWLITyIQbly5QipVq2aRKA1FRcVIEJBuShslqpWl3ny5IFdkx86zsmTJ2vWrEn86tWrQxq/+uorePKJEyd4e9asWQnX/TMh7TRQjOrTu138jjPHjx/nkRQpUuiutqZOndqrVy/57yEJ9I4+ffr4bN/UM2fO5O2tW7devXo1t3LmzDllyhR5hNJRXstuXFqwU6dOOhe1ou0/6Xt0w1UhSRt0EyqNUVeGIKr3u+++I0T8GjKe8N+vT7tLly5xK6GcgRkuamBgYGBgEN8QLrpgwQIVIiqd7j70xRdfdHNRyKc+Xf3qq6+KIiuX6JFBuehnn31GiG5vGUUzRpmXl3744YcqpH///oSMHj1ahUyYMIGQsWPHyiWcDfX372jAndDOifDDDz9YNjXlcunSpRJZDIb16NEjaIbFWqzORd1HPWUhSF/SDPpGSaRixYoqPlpdhQoVCKSkEuL3vOhDDz1E4JIlS1QILJ3UgtXof+DOMKQlb968KPeqAtetW0ecDBkyiNI5atQoLvWzYRAJBxe9++67HVxUP36Mnpo+ffp58+bpKTz22GPihjpoBurWrVuoUCG9FML2Y8pFof3Jkycnq2p78KpVq4SNW9EE2+EZWwikMnKO8Ldv316PAE3q2rWr/Kf5YKqqooYMGcKzSgwkKZ0Jo7hHREQQ+M0331jRRmh1Luo+YurmonRPXZZq1apFBLWkLB1/0KBBjqoghHB9IgM2yOsCV54fhNIu7nHmhRde0KdmQI0aNWSrZ1BJkGkmOoL+UoYsmddQkwj6mDNnzpygXDRcFZK0cezYMSpNbcUHDLCEyEzN3r17+b9v376NGzdu2LBh165dysv3qVOnuPXTTz9t3rx5/fr127Zt07c83GwYLmpgYGBgYBDfcNsukgWWt956yyOO23bR/v37iZMmTRpR8n799degXBS1Q3ggCnrs/Mu7uahkXi0zWtGeTtGz5VI25T7ugqzoWpr/hoMHD0rBUZGDZjgULspdQojpKIXHG/3aLpo2bZoe6JeLymG8KlWqyOWBAwfKli3rUZN+4c6wrAwT7q5AOe5F3WbLlk1PxG27yJuLwi64y4v8Zsk7A4C7zZs3d1dFLGzkNG7c2GfvAJfLp556CtVZ/kNKueUwr3ry5EkCIdJ0gUOHDvHfe25FtTs6N/2C+HAhCfFru6hVq1YqMHZc9F8blr0pFzoNl9MnDgLZOjp79mw6G7I5WdaH/S5qBUKI7eIeZ2S7gRJd2AucVv4HFcVANr1k9bV27dpuGZs/f34oXDTuFZLkAeek0mSCTwC3JEQGk61btzqOkq5bt06OW9NxJITOtWbNGvkfu69DLGC4qEFcEVOjF6HjypUr+hYRA4OEBUM2MpmweYjPqcpYAOXg6NGjxoxEKAjERXU6FwoXBYQQ7cyZM1ZoXBQsXboU+ko4BEZfiQ0RoXNRYlq2Eqnz0kBAQ3rhhRcmTJjw+eefE1/fORwow3Hhoh5v9MtFN2zYQGCJEiXkMpDOXbp0acKJzP/IyEh1mjd0uDMs64HLly/3G5+hKUWKFNBRPTCmXPSll17irtusTigZWL16NXc7duyoB8aai65atYoHn3jiCcu2ulSpUiV1S1aMv/zyS8cjsnR55MiRJUuW8Gf27Nke6TNAEQFaS6EGDhyoS7JfLjp8+HBf9B7U2HFRy15kHjZsWNeuXREMWRdVHsI87O5269aNW2TAsmUVlu5RLjdCbBe/Nr2rVavmiz4y0KtXL7XU7y0JVuB+sX//fqSRWylTpnz99dd1w2YhclErzhWS5OHmolu2bFFcdNu2bZs2bTp58qRlO/qS7buym51fbtFG9A6GCGGwPBs/2TZc1CCWOHToEIPCnXfeWaFChbAnjqpRpkyZZMmSqSlzAw/QFn379oUGTJ48uUmTJrWiUbt2bUbqF198kfB9+/Y5ngo9Mh/RAQMG1KlTR0VGRSMmX1/HtjfLPmK0fv36m1vg+MW1a9cmTpzYtGnTjBkz8hVPkDx8//33dLcCBQqIZp84MWrUKOSkRo0aKLgffPBBQmcnsSOMXDR37tyZM2eW/yFyUctWDeWgGlB7IENETLkoig7/6USBEkQxpbBwMFnxkB2zjlOsfjMcay7q/Ua/XPTAgQM+bS9oIJ2bavFFm6GiIWSOIEZwZ3jGjBm+/+5S1iELg0oGVAFjxEXbtGnjV/sPJQNiGKlRo0Z6YFx8h8CrkydPDlvjezRp0iQVLixu2rRpjvh0ARSGq1evyuouDDNQyvDV6tWrM5zK6qjs0fXmonKWWPaCxo6LRkVF5cuXD8allyIULnr48OEUKVLkzJnz+vXrUEr92GcoCLFd/HJRebZ9+/ZUVLly5ZTYeEuC5enrCF2CUsgR97Jly6qp1dC5aBwrJMlDjOi69+j69c4iW3Z128gKsmUXuY0fo1CGixrEHgg3g4U6zh5etG3bNiIiwu0SwMCBrVu3tmrVShmdl5MbANXq999/37Fjx8KFC+XL98gjjzgsdMcosniGKFy4MIMUqg+DlOykeuihhxwW8xEJ5VIiCeCff/5BWxVDLAnFRdGx5PRdouWiqIzCBxCGSpUqwUsTOkeJHeHiougKhKjTWaFwUUiOOnG6aNGiDBky+DTzLaEgplwURRYNMl26dO6FfTkxy6BBZOXUwcEMPTIcay7q/Ua/XHT9+vU+7VxfIJ2bwubNmxeFm+FUGUaOEdwZRi/0aRZ0FKiWL774AhlImzYtEXQHPzHlosOGDRPu4XgFuqzY2PTIwMaNG7mbP39+XXONCxcVE0FUNbxRlxkxm6y2UgukCxQpUsSKbqNixYo5vNHw2RKfJYxOyI+6GwoXlZqRiddYcFFenTFjRrXH1YoJF7XsLcrcfffdd0uUKOF2dOSNENvFLxf966+/7rrrrvTp00MU+/Tpo8K9JcEK0C+uXbum2x6jsXzaedTQuagVtwpJ8jh9+rRswVUh9AhC+C4gA3K+V91ihOGWeO6RW0pOzpw5o9tAutkIPxdFJ961a9d6Gzt37vTLJQ4cOLBlyxa9b1BaAvkqUHII/cGDB91erQwSG/jQMiKsWLEiLKmdOHFCb/RSpUrVrl07LCknYaB58NFVBgYtuxqFXjq63pIlS+D2fFfEaGcsIjP0E5OPqAqh26IoOD7MEl65cmX14UkkUBZHYgdRR4JyUdSdWOx4DAWiHCdaLopuEdO1tdsc4eKiYrtVLFVa/riorEnqplNIUDeuI0tJuhWloIgpF7Wijfo89thj+jg/evRoyYnYEFbMUNTltm3bBs2wLAnmyZNH6UwoxDKbpuL75aLeb/TLRSldlixZ1Dqnx/qPeLNgCFWuRGIEd4bhYzQ9gQxEKhB1q1WrVuLZUjy46HZ0eURqRoUULlxYT/bSpUsQ5pQpU8olKil3U6RIoY9yEH6ZbvbOwOXLl8VIr75OtXTpUkJat24dixrgdenSpcucOfNzzz2nh2/fvp0cEq5srljRhxuF2Fy9ejVnzpxc9uvXT0WgpIxOkCs0dZ9tDFm5JJUpCbWPwy8Xffzxx9VUjqwW6o0us7Sya1Tg4JYfffQRlzoXFaPTaqnKm4v+9NNPIkuxGPxDbBe/XBRQh4STgu7iOKgo+u0X58+f120OybHeTp06yaWbi5I9n7/N2FbcKiTJg4bQj3qKdVxw5cqVP/74Q/7L2TcGTEY/ZTtX9usqmaTjO/b63lSEmYvCqmGSQqajoqJkpVgfMuCffDmkOnQuyrgvgVIdQLmuNki0aNeuXapUqcJygo6BqVy5ckok5INhlla8QXXVqFFD379kRWuibnppRRveQB1Rt2IUWeaDdS5qRTM0mKfj8WXLlpUsWVKt1iY4+NTx6YpLCmgnQbkoalCZMmV0dTyMSMxcVGwkxtQvyG0Omd3XLYKKOc0BAwaokObNmxMya9YsFZI1a9bkyZMrtyKIXO3atbt166Yi8On02U4pVAhx4Btp0qRBz5BNWSid+jIpUk3vED0yRHTs2NH3XzObYuKyb9++KmTy5Mn6EpbahXH//fdHRkZOmTKlXr16SmbExWLTpk1RjBYvXtykSRMuy5cvD0Hi6+CdYXF2ChngWQiwOF+BkGzcuFEWAcqWLeuLNtir4P3GnTt3cslXSVHcw4cP33PPPfAKlQJP+TSXsDoY+nLnzp0jR47Yrdv4zbCcWgRQo/HjxzPOlC5dWpGoLVu2IBhSD4jHuXPnxHUHgRMnTpT1UvFfQpH37dtHHVJRZJKQRYsWiXoqVQdBbdGixejRoyEP9913n7IN450BWcnMmDHjkiVL+GpQq2IWiEr78MMPY+GoUAiS+8SHMDe1Usd3kG5Ss2ZN1VIyCeKzjUsjaQMHDixWrJjMq6KuiP9SykIlUDNyALVz586rVq2CoMokgjKnbNk+e++66y61a4ByUT/0ps8//xwhGTx48BNPPOH7r0merl27EjJhwgS5/Prrr7lEWVq+fDm0mT5SoEABn20wSWzzipsZ3Qa1AzIOwMFiWodWaO3iHmcEx44dg/nr7lsE3pIgdnrp3fojUCM4rZrH4b1IJnqCXMpYoc87SCtTk3QlGtSxOheXCkny2LFjh5Ap6kcolezCpacI+Vy7di23GB5lF644a5VPA9yNyHLEFNw8czAOhJmLijXhDRs20KUZgmWbspyLRZ4oIbe+jYYiHkLcqQL+iBk0iWAW3xMnrl27Jq6K8ufP7z6DZNnDvUTQwddRZiX447B7RpfImzcvmpkKkalH2Tlg2bsFQs+e0tL01UIV4t4hdvnyZTnJzeCoJuxl0kT+HD9+nDh+34WIot5JT3ZA2R/jWTdd50Ex8UL6bvtMdB+1e8cDMrsJn9QDPegl7xLP6eqbF6PIfrmoLI/oSxACipYpUybdmCE9euHChUELJWCsGDdu3JAhQ9x7fQmBAPPpUu7jBEiRzKHyIh4UT+KCzz77DNUhderU823IwIKIilpJ/DFjxqhtxgzTFJlXOF4dlIuSAl9fmQ/mLboXh1jkWYAkoAlxCy2Br4ibi8Y6ZWRywYIFaGlQAumtKK/zo0HNyLoBiouE6Hv/HEDBgpOQN9RBiawqE7aA2KCuoXM4lImff/4ZJQYCQ/zbbSs+EogyB5ui0goWLCh2Vt56661s2bIJiSKE+qFyxFpPkSJF1JQTvR4uhx7JgImiRtfTzbSg3aoTlRBUJYTdu3f32SZD4H50bagd/K1hw4Zz587lvVWrVvW7/uAXjJNvv/22LLYUL15clkbR6YXVZM+enWalQVFMZRUuS5Ys9C8ZJBEV2Sbqsz1ADB06VA25KACZM2eW5Q5EmioSfZ1PDGOpd4bpBXfccYfwLjoIwxolfeyxx5A9VC6hzcKBkXa1IOb9RsueaKN1SpQoASl6/vnnH330UeWUkjqkyLKymjZtWrqYcm6p0L59+549e4YsFP8HNMJAGealDE1iT9hnb7x09Gs6u9iGEabxv//9jwoh20iIUA6+VjSZRKhbty4VVbJkSd7C4CZKJ5VABYodIJ9tPUg/ZhY0A7AvkWreSzXSWFy2bt2ado/FTj++AoFMECN1yFv9+vXpR02aNOndu7dDXaQjIHiST1oQjVzdQhrlvCISxbgEI4Ul+uxFOQpI07dt25Y+CI+FkTKYQ3scGvnIkSOF9iM/yDlMno8dxUQmqVKEQZYN7733XiqEvkCyMtMBoL67d+9mPOc/n6SZM2cyCIsc5siRY9SoUX5tR6ERlS9fPqYVqODRLhTf7zij0LhxY/eZTA9JmDZtmvQLSOzrr7+u9h1QsbRIpUqV0ArglvBbWXyW8YQUhDDT6aS2Dxw4IC3IiKH6XbgqJGmDQZW+o6gWxFKNIaijwssEMDKlJ/MUo6W6BUcNZMbsZiDMXFQsL6lBWaipyCI8RDbuqpVP3VUx+p+y16TWlPUFVYPEAPSJLl26dO7cmQFLrM/p+1Ise/hg7GY85Rv25JNPWvaRFSKjoDAwMeo999xzck6AAU4+TnxrZeSqXLlyy5YthZihMGXNmlUmJkS1csyxubFz585evXqhkbRq1YqXiit2teaAQk/G0B74Eutn7iMjI3kvKgvfG/gwvZFPLwMo6gUjHaKL9sMXghHcsdhFl0YRpCoY1skh2oMUB50JHYhsoGYR0r9/f8Zrxn19nf/zzz+nyGTjlVdeQfvRzdMzLpMsBUGJ4UvmveaMkuH28uxBL63ouUZleyNGkd1clMdF9fG7K5UmkwM8lk1N+cz4tF1JgUATtGvXDrWAD/bq1asRG2RJ6paRoUWLFnzFUSIRFdpIvn979uyR/WlIF/ofX32xHa92EKFwUM8oWItswK/atGlDyvfddx96Le3rs3cbos0gNg0aNGB0RomHGLz22msqY0G5KMIv61okzlt27NgRlzxb9hTMQw89xHtPnjy5atUqcbmuuGhcUmYQRtOCosMwmzVrxrNyLEdMUEIS1PeJPkiXF7eQgQq+cuVK2b9NbqWGhYuiLqDE04jULT3i4YcfVvJMtefLl4/effz4cZ6iD5qZxxgB3YIRzz3l5wFIjpog49tKy9LXDh48SDrxXPkMAvRu90sZ/eg1Kvz69et8MkRPCJphvk3bt28XwSNaiK4IPN6owFCPYheLZb0KFSrcjHMKDIYkS88NZFMEDVJmpojgXtagcnhcZlqtAPO8SBfV4p7MDSUDclemm/ma+52oDR3ea/XcdbeXDoZ6v/o01aLb56Ok7slfioBqHqhriHkFUfEpZig7gMiMPnFMBYZuFB19QN+DEAvEul3knKFHmh6iqIM4otIje3xeA83v6yCfpO838bhXSJIHSh29m3p2VCCXjJNIAtXrniHiG82tc+fOKfoaPwgzFxWeqfobRZIFT70uzp49696jq0AgKt238WhK2CBEMHxXrFhxxowZcil7JPRmWrx4cf78+WWbyttvvw33UE0MZSpbtmyfPn1kBESH9mnepeWgke6kGz0VKssY16NHD8ZrVG2YQ9CJVWFW06ZNgxLwC5f74osveApOhbIrykSjRo3q168v8flK+aKPPNE51Xkq+qHPNj0nrJUunSdPHjKgPtt8hGBZip2uXbvWp21XE5ZOHFjExo0bZR8XlFXlk4ypnWko6Eot4MsHR5VDUGg/jup1gI9fmjRpHPbxrGD0UqZjaaZYRBYuWrVqVZp43bp1gwcPplqg2YF2FgkxUzNTkHOoe9CPVmRkJOxIXYrFILRPy15nULuAGDF5dZYsWeSTJgdIIJyi/Ikz7pw5c6p04GPp0qVTlzyePHlyRBQexQdyzpw5jEtRUVG+aGOJlm09K2XKlOqbHcoeXdid779H5uKS57p16+rmJRAhnYvGOmWGZf4LVbait/6qOpepH11Rq1atGmOyR6kte9rR919jGDxSpkwZteqFtPiiT2EhuqlTp1ZzHJSCW5Bt71cYGNxC+P777907Gw0MYgG+QQULFgyFvN0mMBWS9BBmLiokU+3A/P333927bT246OnTp9FxubV+/fp4JuUG3kBfL1asmG6bBA01e/bsqhHXrFmTLFkyMS+BZly8ePEOHTrIrYsXL6L3ow2L6XwwduxYn+bS/bHHHtMdo4ldxEmTJqF2iy5bqlQp9Nqgmfzyyy99th0d3dEI3AYSIrOeqOZp06adN2+e3IImEV/Wby3bPKP8EUdzirKCBg0a+KIdbcGNc+fO/fjjj6u74k4agi2XjRs3hr/BHIRJQmh9/z3YQFUQQeifeilE96677lKH+5977jkq3IN+i79pt7UYb3opnsEgLbGILFyUTLZp00Y2NUEvPXZXjhw5kjgxMt1BTcL5dcdlJ06coL0QMzHaPGzYsHeikS9fPl+0yRYpSMuWLdWDsl1W7a1wcFFAuRzu+M6fP9+9e3dFnl955RV9ITcWXDQueRarnrpPI/28aFxS7tat2wMPPKBne+nSpWK9wLJ3URJTdV5e5HcfvgNuLopkVq5cWWVPDlDVqFFD7g4aNEgOSln2qrVPsx1iYHDrgg64bds2vnSVKlVKSrbEDeIfO3bsWLt27R9//NGlSxf9GPZtC1MhSRjh5KLoi0Iy1fIRI3KMuCi3ZJcv2L59e/y4tTEIBRA8WJy+wyRr1qzPPPOM/L906dI999wjjkZR5VFeW7VqpWYThNrpRwfFp7b42iJa+vTpUVXVXTl71rt3b9nBIkxP3y0ZCKjpmTNnfv3111UIbDBlypTyLEJVuHBhaLD+iHhzdhyH6NmzJ4HKDoEV7btcit+2bVvff61KiGNuMcAIec6UKRM8Vm1bhRLkypVLT19s00F19MAmTZpQw7/99tvly5c7d+5ctmxZfaHYDbFc77Zk400vhRirQzgxiqzv0ZVbOXLk8MgkLe7zZw7BAzKboHiRDmEsRPj2v5BGcbMvWVBVO+v8clHd1qgOFMoBAwaIaRNlc9LBRTds2LBIg2yKc3DRuORZPA3ohjR1LhqXlCtWrEj39GiFMmXKREREyJQipdaN6wSCm4uWK1euRYsWjuzpTs8sez6FYpIZX7QNSbq8Xquxs0FqYJAg4HPji4Zu/sDAIKYQgwsiS/fee28ctzonAZgKSdoI87qorGqqIwrioEY/DmcF26Nr2asTEkEtoxkkLA4dOgSj002crVmzxmdbgZPLUaNG+WxzgvDAjh07qtPqAkhX8uTJ9aNN1atXV1teZf1H7dcFzZo1I0RNKvMWLtUqigdKliyZKlUqncnUrVtXWF+PHj1gpO4zIbt27eIROJV+NgY1mqTU5bVr1yi+LMxCvfTlHcFbb71FoFgQEYr4wAMPyJImQg5pd1ilh/gVKlQoWbJkyqCCmKXhFf3792/Xrt2CBQuCTsSI3tOlSxdHuDe9FJ9dyiVsjCI7zouKFdDy5csHWhoVg4RKSEKB2NN3G060otfSHV4ZFMLFRXfs2PHoo4+KjSUxyxSIizZv3jy1BqFSDi4alzyLxUv9vJnOReOSMl90792DYjlMrLmqze3ecHPRjBkz+vV1IeArwN3IyEg6l1SaVOD27dv1WtVdIxoYJHL8/fffLVq0yJMnT6dOnW43c1wGYcewYcMYANFh4tOETGKGqZAkjDBzUbEXrDR+cd+yYcMGPY6bi168eBHZ0tfcxNaw2zCdQYJAtHCdLopqqzZjyxmzQJoxGr/yw27Z9A8aplYvBw0aBFNVh/ihcJCEKlWqqPgQuQwZMgS1DSCuMvWjhmgGcMhixYopq5461PZXFGKfZiAeUkr2lDdzK3qdVsw2ihcsfZEWMS5RokSRIkVkok4Oiyobj8IYZQVYf6kcTVSuUOQ03YwZM0LfCyDldav7HvQSIg0fy549u2q4GEV2cNHLly9TcELU8rgDsrKn7zINCqlety8fxEOmJNzmCuRkY1i4KMMO/Gfx4sVy6c1F/cLBReOSZ9nUqi8M6lw0Likjq1mzZnWYxdKtaNy4cSNfvnzUzw8//BCin3o3Fy1YsGDOnDkdm8zpXGfOnDl//jzpq60QOhc1MDAwMDAwuK0QZi6KJgSHRGcSlXr79u3fujyFurnoqVOnJESOM6EWy6Wy6WKQsIDwoCwq/1qff/555syZZZ1QiErp0qVhfbreibopG7NRPX3/9RzdqlUr3WtljRo1KlWqZNkO2S3bFDPx3333XRU/b968jRs3tuxzpB6ZFJdiOmEWE0QOHyRqA7kin3/99VemTJnUoTgxNaQ2E3L3nnvuadOmjVwKH9PPtvHGVKlSKSND0EviK9mWFWNk/sCBAwT269dPWXOpW7cuJFxqSTYt63bnqcyg+wJQ6GvXru0IDEQvIeTiVUx59IppZPE4qtfn3r17M2TI4PuvtR6Fl19+GVbvIDneJUIGqJNs2bLpW39pkfXr14vXROiNfmvNmjWygzQoF61YsSI8U3+Xm4s6liK7desWUy4qe4yVtMclzzNmzHDMrQgXFcd3cUn5ueee0ydfLPuAt+4X3or29lagQIFvbfu6QeHmomKfTHeVSVfq3Lnz9evXp0+fzq0pU6ZI+Mcff2y4qIGBgYGBwe2JMHPRixcvog+JFVzlLNVht9rNRdFRZHOvOGBF7/zW9tNqfLokEnTq1Ekt7tFGU6dOTZs27QsvvIByLMaK5AilMsOzYcMG1E2hpgsWLPBFm1SxbB0XAqDMcqIcy3lO+K1wADF4ozTsQ4cO+WzTpqSjO2x046mnnkqfPr2DU+XPnx+yRCJySSKKS+TKlUv25SKHuXPnVqs0FDZFihRy2BXuRLJo1cpim5i3jYyMlMtTp06VLFlSHQ1F1KFS+kHQJ554omjRohRHzqnWr19f7T2G4audwGJKVOXh6NGjxA/qlgCyB4t2LD2JDVWf5neUSiaHZIOqUGaQYxF56NChxHTwt4ULF/ps3+huF2TVqlXT18P5D7fx9lJj2eZhffZJ1OHDh8+ZMwfRUtUiLtrIG/KwcuXKgQMHUr1C5g8fPuyzTR+rdB5++GFCFJ8X61P/+9//aHSZOMiYMWPBggX1VwsXJQPUxkcffVSmTBkhn7LYKCve7mLq2Lp1q8+2egXjkgXhWOeZFMTbITyfkZDLF1980WdvipY98LFOme4g/gMhurNnz6aeq1Spop+OlrfnyZOH7hPiQr1wY7KkQugp4sSP+qTS6HoIwIoVK7glXLRSpUq//PLLqlWrpCC9e/dWs10GBgYGBgYGtwnCzEUte90pKipK2Ca8VN95K/B7XhS1GzVRN3FhDosmHsBYsmTJgmaJdj5q1CgYGkQFVV6tXsK1SpcuTYTKlSs/+uijuv9rNFHoWf/+/dHpX3rppc6dO+uHziGlsrwDF5WQ2rVrFy9eXEXYvn27z3Yr8sUXX3jkUI5l6otIAmSJcDhqjRo1UM3FNYhlC2G2bNngJyjH5KpmzZqK+BUuXBimDcWaO3duq1atJkyY4EiTGiA/S5cuhUBCD5RvDCt6hUc/IC1nX3mFLAlSP2XLluVZki1VqpRaTeWurCMVK1aMGhDfpB7lFZw4cQJSoft9mTRpUoUKFYReUqvlypWjyR588ME2bdpMnDjRQW5Dj3zx4sVBgwZRYxL5+eefV5MLoEePHj7bsTWkUR27hZYTopqV4uTLl0+MM3kXChZEdaVOndpnuwJ/4403lOWzS5cu0SIkK6/r2LGjLPRBrmTpHrGEuSEMMHlJoV27djKvgfyksPHss8/Cuzp06CBlefXVV8U8smXTp+zZsxNISWlchi9EV/x2TpkyJXfu3NyqXr26vlbsAK+uWrWqz3Y0LyuKcckzcSS1NGnSlChRAoEkMq0j0xlxSRk2K25+fbZtKlUDOrp16wa/9W4sARUiB7Opq5EjR6o5I+o8V65c8hZeJ0TUsuc7xFcq5erZsycyI67eaetQXmdgYGBgYGCQZBB+LmrZeieKLBpGjDxo8xQq7+nTp/06YDVIWKA+bt26VU0Q/PLLL45ZBppsz549+/fvdyykFCxYsFatWujNKPp+/UEdPHgQZujxarTnoItpHvjzzz95tcNlNgnKLuJdu3bp5+DFNNGQIUOI79cbu8CjOA789ddfhw8f1tO37GUr6sq9YZWcwGxjtB1gzJgxHhZiEhCjR4+WndUKVJp3Q+uAkcIY/VbF1atXqb1YmAZhbAnKhEn2559/1o8PxNTHPTJDCo4RLNZ5tuyt5iJCPO42HhiXlE/YCHS3Zs2auujGGkeOHHEbW6Z+GCtU+9KV3LOWBgYGBgYGBkkeN4WLGhgIxAsi1C6hMxIqZK+sfm4z8aN58+Z+17USELR7xYoVQ2eeBokN27dv1zfcGhgYGBgYGBjcDBguanATMXPmTF9o7lgSCdq0aZMyZcpb66Dy9evX27VrB3lI6Iz8H44fP966dWtjeOxWxLJlyyIjIz/99NNy5coltgkOAwMDAwMDg6QHw0UNbhb27t0rp8I+/PDDULazJiz+/fffqKiotGnTpkuXbtu2bTHaXp7gIPOzZ88O3R/MTcXixYuDOuAxSJyoVauWHO8M8aSogYGBgYGBgUFcYLiowc3Cpk2blDGqxO+bGPL5rQa/LkkNDJI26KdjxozxthNmkJhx7NixuXPnJnQukhQSc5X+8ssvH374YRgTXLhwYYhunAwMDAzCBcNFDQwMDAwMbm2sWbOmSpUqYsM5ofOSRJCYqxQKev/995O3u+++O1xpwmzFGra4NDMwMDCIHxguamBgYGBgcMvj559/TpzE6dZFYq7SPXv2hJeL/vPPP88//7x7f77b5LuBgYFBGGG4qIGBgYGBwS2PP//8M9ESp1sUiblK//777/By0UB49tlnb/YrDAwMbmcYLmpgYGBgYHDLIzETp1sUiblK44eLTpkyhbfc1FcYGBiEF7/++uvmzZujoqL41f17//vvvz/++OOW/+L3339Xdw8dOrRp0yZ58PTp0/GWYTPEGBgYGBgYJABu3LjxzTffTJ06deHChW4Db4SIIZmzZ88uWLBg/vz5f/zxhyPOP//8g24xbdq0r7766sqVKyESJ/SP6dOnz5kz58iRI+67v/zyy8cff0wElBL30cF9+/b98MMP/EGDWbx48SeffMJ75daFCxc+//zzWbNmnTp1Sn8E1vTll19evnyZ1NatW/fee++RZ0eye/fu3b17N8VZsmQJaSqr4NeuXZMq4vfq1auOp3bu3MnrPvvss2PHjukvFbvoM2fO5Ck0qnPnzulPeacZ0yq9ePEipebPpUuX+DN79my/tXrw4MG5c+d++OGHBw4cCKXsQZMNxEWRlk8//ZT803yqGnnF/zQQov6jfepp0lLKEDrtmzJlSt4iMc+fP0+a6sFdu3ZJNARVQvwW3MDAID4B+RQbnGvXrpU/hw8fllt//vnnty7IyMlYQY92PHjixIn4ybPhogYGBvEHtJmwpONQLuMCFOg4usMhBfU/jBkLHVAaNNf4f68bZMO7Mj2ySriaoL0dsH379vz58w8ZMuSnn34aPHhwREQEDFBuLV++vHr16nCAli1bzps3L2/evHny5OGyRIkSOnf69ddfK1eu3L1799WrV0+ePPnRRx8NSpwgHo899li/fv1Wrlz50ksvpUiRYsCAAeoutKdt27aNGjUiA5CfUqVKFS9eHPohdz/44IOyZcvyijfeeGPKlClFixYV8zlkD7EfMWJEgQIFKlasmCxZsly5cokSw2+XLl2yZcsmfKZkyZKpU6cWv0EdOnSA+cBOJ0yYICaCoE+UV+7CJHn8u+++IzNjx44l8Rw5cvBGOJvKLdlo0qQJvHHDhg2k3LlzZwmHSj388MP9+/ffv38/bCpTpkxQffWUd5oxqtKNGzc2a9aMhrv33nvR2zJnziylg7/NmDFDRSM/PXr06Nq1K5XWokUL6oe8ER6o7O+8804oyfrlou+++26rVq0mTZr06quvpkqVqn79+jI6/fLLL506dZL0YZuEzJ8/n/+0vhBI1FByKC0lo/Qff/yBWKZLl06cPIF9+/ZRLVmyZCGkefPmilSjyz711FM0AW/xkD0DA4ObjX/++WfdunXKewUDGv8ZTsVP4dmzZ7ncs2fPGQ3Xrl2zbNVFYtLx+YgfPHiQdLZt2xY/2TZc1CDpgE/4mjVrEjoXBn7www8/oBvdd999DzzwQNxTQzlOnjx5z54945LIsWPHoAE1a9ZEw/vzzz9jkcL333/frVs39G+KFsaMxQINGjRAZYz1jpoxY8asX78+LhngY/b222/Xq1cP9de9dqfDb1YhSFAglF30b1Rztc6WtAGvoyrUJWwTaqSY/CeffILGf9ddd40cORL1gnBoDCHTp0+XCNR5wYIFX375ZZXCokWLvLkoFVukSBHIrVzCkYRX7Ny5U0Lq1KkDE1N5+O233/Lly5c2bVrFMeBOxIdCL126VEIQfiHJc+bMkRBoHiGDBg2ybLqFTkMphFdv3ryZsqxatQp+SMjUqVNv3Lhx8uRJuiGX0G/Y3VdffQXPgcTCcCCKavYKekwc6DEpWPZCH5eKRqIzvfDCC/KfZHmjKgWSCa+W/95pxrRKGTfIrdie7d279+HDh0lh/PjxhEA41bIhnJmhRj1FDROBlAOVnRoLJVk3F125ciUtqC55lghdunSRSyoEik7Ie++9x2Xfvn2HDh2qIl+8eBHqTv9VXFQgbaeXevTo0YTAePXAxo0bL1myxG8tGRgYxBt+//13KCWasIxp9PrvvvuOEPnmyl4bBnb3g7Io+vPPP8d3jm0YLmqQFEB/69Sp09dff53QGTHwj6tXr65btw4NplKlSnFPDeqC+qgvEcQCKOLou7lz5yZXseOiFEpUc8VFw5KxWKBfv35UbFwoXK9eveLSffjswe0LFy5MbXhzUXdW0bOhYajR/H///fcLFSqUIGvL8Q/oR8WKFdVlrVq1qD21xv7jjz9y+cgjj6gICxYsIKR79+5yOWrUKC71s0DQCW8u+tJLL8FF9YVrKvyxxx6Tlwrvmjlzpv7IuHHjCGzYsKFcfvbZZ1wq1ge++eYbQurVq6dCduzYQUiDBg1USLly5QjRtRwYNSH33nuvXAprEvqq8PTTTz/77LN/RwM5kTU62SEsOZk4caKKDwWVP/RHOJua0T979ixFCyXNWFTppUuX3IuTzzzzjKqlPXv2pEiRAnqpXjps2DC9xvyWPWiylouLwmzz5s1L86kXyZCbIUMG0Uote4CivNmzZ1+2bFm1atXcBnKh4kG5KHWSKVOm1KlT//rrrxKC/DCQGk8wBgYJDj7EUErZhy9gcCNE5hP37t3L/3379m3cuHHDhg3wT1kUtexdHtxi9Dt8+DBjOHG8P+XhRfi5KBoexVtvY+fOnX6VvAMHDmzZssXvVi60QzlNG5+nZg1CweLFi+NtvT6meO211wYPHpzQuYhXoFWgRyZ0LmKGVKlShYWLhhF16tSJNRe1ogmD4qKJB4zD+qJHUKCtVq5cWd+sGAvAWIJyUTdkr6DjtOStKN4xxb82LHvxELIEkdCJkIjWo48+quLLWpkyalq0aNFs2bLpCQY1tMMrnnzyyUB3n3/+ebU5VuHkyZMEpk+fXrLq5qKbNm0i5PHHH1ch4qZS3wEhW3lRklTIlStXZAnu8uXLlr1yqNbrFGQD7eMuyLTFqVOnhEZ27drVsfNfMpkxY8bx48c76JZ3mrGoUqRdJ9UCUiOwQoUKls2QIcbuN7Zt21Yi+y170GQtFxeVheKqVau636WfpJX11YiICPexVVCkSJGgXNSyp64I7Nu3r1zOmDGjR48egarIwMAg3sDwC6WUyTXB5s2b1YLn1q1bHSdC161bJ7NIEqLCZXE13uaFw8xFGRyh41IGPmnCzhXttuyvL982KaebixJTVYT+3TJIcPCd49OuDg4lKvCFzpMnjy5mSR5Xr14tU6bMm2++mdAZiRlSp06d2LionAdLely0Q4cOOj0IBcuWLStZsqQyWxILxI6LyiZPfcC/RcU7Frh48eKwYcNgUxs2bJB1UVUP3lwU7SFFihRwJz01b+KEVsFdCGegzMAe1WFCHfAWwuVUYehcFP6pQtxcFOTLl49AMZzj5mNnz54lpHfv3oFyC5YuXZomTRqiQSAdMxd9+vSRs5GlS5embkNJMxZVagUgjYcPH/bZx2j536VLF+8RJnQuqidrubioLGsvX7480IsE6F1y6Nfd0FbIXPTXX39lML/zzjtlKgHR3b59u/d7DQwM4gFuLrplyxbFRbdt28aIDQvjP51Xtu8ePHiQS6FsUFO6P7fkqXjT+cPMRWV1mKGfYZ2BUpaGpZyoONQCtxTndnPRXbt2UR1CRw0XTTzYt28fH0U+SKhN8+fPRyn56KOP+KMMQqDFzrehT7Xu3Llz1apVtPu8efN0RYGP1rhx40aNGrVx40b9LSdOnBg/fvyYMWP4Rv7000+hZ48va8eOHfWQGzdufP3117JLAVki26Qp+5TohLNnzyZkz549jnQCZcyyZ4xGjx7NU459jKh306dPR2/47bffpk2bxrNuY5jeQO2mMgcNGkSudBM41Nunn366Y8cOODZKRmRk5Pfffy+3Ll26VK9ePZrj6aefps6VRcpAFc6YMnny5KFDh6JHOlQiMe1o2UcfR44cOXPmTJkG43d+NMieTJvt379fQpRNtpjCzUX9Fl9MhgpoL+pc/quDUpYtk8rQi4DxhJgUEw7jkB9ppoEDB6LwySisEAsuSm2sWLFiyJAhs2bNot4cXFRljG6iSqHWmpBGCVGEDbEnV4MHD6YTqa10UjMffvghGdu7dy+yJz2LS1p2xIgRVJHSsC17Fm/x4sVK9vr370+u6Be8iKySgsoJlxKHT46EKFs4vD1Tpkxqo2OI4MuH5NM1kFUHFz19+jSNK6WmXyO3jqweP36cDAgHQ0T5T6ECiXfSA1IBH6OMchkjLirLlZkzZ9YT9CZOsD7uPvjgg4HyIxmgNR3huXPnTpYsmchJGLkoLDFlypRiUcPNxxiaCGnatGmg3AoYlOS8pZtmI+ry2UqePLmMh95pxqJKrQCkUWg/GeN/69at+e/xRQudi+rJWi4uOmPGDMemZb/YvXt3yZIliZknTx7pkjpC5KIAGSB8woQJ1Fv58uW9X2pgYBA/ECO67j26fm1cy5Zd2fAovJQRVW6h0wpT09WSm4cwc1FZC1Z2DoSaig6NCiIbd6XAbi4qRpyoL+IYLpqogFjXr1+fDw9cC17066+/ohmnSZMGaiERLl78f+y9ebxO1fv/f5uKooxJyhBlyJA3PoQMIRSpiCZFk4hS8m589yhTCG+9DUUkhSRDFJUyJJUMhVBKA6VJyhAZqvv3/O7X46zfau/77Ps+59xnwHr9cR5nr3vvtddwreu6Xmu49h7YYMQLABj1fCw8Hi579eqFQ1mwYEHjiPTt23fw4MFQOzgDif/+97+VAwayfPnysCns60MPPWSfkopbNvKxoybwdkyj5r+7du2K69aqVSsux4wZM3fu3Msvv/yOO+7Au8Ltts8FpVYwyoPv0q5du127duEdFi9e/N5779VPmOGTTz6Zm/Em8Q+uvvrqAgUKcEPiuxpgvx07dlywYAFeJp4ZjqkYMpxK53agVTh55IzfgEclSkPj64hRly5d6A44QGoNjvtIC+CiMSQZm02aNKlUqdJHH30U9ZgSleK2WrVqkVvlypX1xnLlymnyiCaNeGeN7G9P9ezZU6etEqygDz4umlr1UYIK76EgQHQT7Txz5ky9F7qiDrXddPyhFi1awGeoqQ59Qa31E41TuHBhmhTHq0+fPiVLlrRnTNLKRXfu3EkzwgZ5I8xfB+HERYMFGz58OJcVK1Y0xyMZKfi1xt2fPn36bbfdtmTJEmgnhWzWrBl30msMAQV3oRd0CBPPj3RaSSFPXnvtNYQtmrIXFwc64sUp1SvITWSAmxcvXky73X333aRANkxNebBGjRo+DxgSiDOaYFMAXlSnTh00PH3Uu3dvBcLBjUaEEM48efLwChqBNicdPuArKjycEooCjRs3jv9XrlwZFO/Ey3MU4ccffyxUqFDr1q1NSpq4KIMRAeDSnhgKJ064FCeeeGK+fPl8wU5Jl42+6667ePzmm2+2f+VFDFsjFUnkokWKFEGe9X+QjyG0yM9JJ51kz9AJL730En+/+OILM+uBnEjpSYFIxUU9If/Pf/5D+umnn05FwvNMR5NGUyGNOjHLiOD/Rx55hP8Z0b4H0X4qbeJc1M42GuCieE1cNmzYMFhCdKz+P3z4MKp106ZNt9xyCzf75nCjaeGi2hKMvcBIYQpTax8HB4esxE8//aSttiZFlAq/XTrQ9t/QovwkhSnKarxiXBExteCp8sxAkrmoeKY50S5ivWzZMpt2Kqawj4vy/4cesIuOi+ZAaB+dvV6PD2q4aNTzqg0XjXpz0lziRiPZiMGUKVPoYu4xh2SA5rPllfbo0QOWqHRkIGQjmQ/9+/cnE99BVjx1Ei+88ELjc1AS/DC4ii518MZsAgwpGEyG///73//qJ27LmzevWUqCpka8YzMSZjgGl+PHj0+k5CIDxu/Ri4zrOXr0aC5NWJHPP/+cS0ipfpVHaG9ijNngcDlSzLQWTgkk/KyzztLGKgqAY4pnZqbQdArIdITaYcuWLeYtODoxTxklCJuLhlcflgJpwRU7ePAg5P+5556z89H6hrmZmjZv3nzMmDG6xN8qXrx4sWLFTC3gdfofBu7zC9PKRSEP5sAemDZtmr0u6isYLQ8RzZ8/v1l/QHLq1q0raaEla9asaRT9Y489xrOwXF2KjQ8bNoz/tVMANo77bl6NKBoVqrUX049yZG16QAFohDPPPNO8jpRKlSr5JgRFAhP8MAPqOnfu3EYeyEqOrBgCloxfoVuMNTpx6tSpaP5gUaMpCyz2S4PifexhxowZ1NHmogyNSMpW2GgC50UlunbQV3SF1rtSe6kWrnlQGiDq9RrjS3PhsCOoGuPOPu9Aoq3Yk8VF8X5IMeFtY/KxJk2aSAfazhAjQjOPc+fOtacgn332WW4WTb377rt37txpfurSpQs/KQJFeJ7paNKYpHHkyJGYCQ0N/J+I9zmWpd6nYgW09FVXXaXRlzgXtbONBrgoRdUE1qBBg8wjqNlrrrnGfCQQ1afACnv27FHYNrtU0VhcVB8TCn6FFXTo0IGfUEoa2qZUtslwcHDISjDkxbA0ijH0usQio1X0vz6rpllIsxYqXmo2IuGb+dZXMxVJ5qKqp4kXrODCwCbiMbmoAg2r7RwXzYEIclE8J5uLKgCJcVlwnYPTruXLl8eReioFLVu2jHjfN+Onm2++uUCBAjhbujPxIEmdO3eOBAKfaLHUrG1GvYjzpJhZEnGS2267LW7BkMk777zTOMpaXzL+IjmYyfioN7HE5f33359IyfHDihYtal6qiKy4GnIEfe0JaB/4if4POuvBBscbw7M0k+iCJukNtcZ3sV1GtFiJEiUMndAHD0wrUeuQDX6JwOai4dWPpmw5a9++fXBPnRYrjJs+e/Zss4dQQFCNj4V7amiqolPa8w5p4qLvvvsuNyvMieA7L+orGBg3blzE+3aFqfWoUaP0f7du3ehQ0wJ33HGHJlD0q6Y57KAj0DlSBg4cKM25YcMGM8ugSYQQLhpN4ZlmR+iUKVP0kUMbQ4YM4R6kK5HWuOiiixo0aGCn+Pbo0r++03fBokaPVy66aNEi6pgvXz5GGXzvgQceQAuRQi8vXrw46p0LiHihaMwjEgA4jC7Xrl0L2ydl8ODBWNVff/1VRxNJHD16dMyN9GgqHf6sWLFi37594WANGza021m8yGgwJK1jx45NmzY1kiYK3alTJ/OIuNYFF1xgUjZt2kRKhQoVTIq4qJmkQ8+gY+1soX9m5sVAYWBFa/v3789QatOmjaHBcFFbHWE7Tj75ZJEuNLb90VRErlatWonkmY4m1VijH80CPjwTmoemNffIoBQsWPD666+fMGECjXzOOeeYA5Yx655Itjr+as9PUWzVjrH/5JNP0rPVq1dnpOvXd955p2rVqiba7bx58yLewqb9gQd9X9SuKRIY8b5AA9fVlnsDdTSM1E5EY0cC0ZgdHByyDCgN/B/cFdxCLRDKo9aan1ZN+UmBc1EL8p1+//13HRlFDaKdRNPszYOZimRyUeqp0pspSW27jctFFbLIhHB0XDQHIn1c1Hx+IJoSHB9jufSfEJHDp1dQRLhlmqRfcVB94VKCXFSfETdclH/0rrgFM1iyZAn+jb5Lbj5O4OOiaYpkA63FI1kagHhRkIvavDE1Lmo3OAWOeN8ot1+qBWFcomCeAq4nN5hNbjVr1sR5lbPy+OOPZ9DDsLloePUF+XC+mftogPL169evVKlS4a9G7eCc4fFHvIOIJj1NXHTAgAGRf36aIi4XRTILFSp0/vnn6xLH12zhxj+GV/iqb0iauKi9QIGp0H5dbYu1C5YIF1W4EdPdrVu31mZsG3BmHvStQsfEn3/+SW52S0ZjcdEaNWr4HnRcVMD8XXHFFWIO9erVw/zR7PxPqzL2cSAuvPDCiPc9SSgTJnXBggWVK1eOeCFt4S2ynghMmTJllAn/0KqwJsTv+eefTy2CFH5GlSpV9Agd5FuOi3r7ruE8bdu2RSVSwvvuu8+Y7+nTp9OholX//e9/0Zz0FGxW5Xz44YcVNkNjKuKdklBoInFROrp27dp33HFH/fr14XgiRXv37kVHaed2yZIlfUfuIepnnHGGcuOlAwcONOuZcNEzzzwTkZs2bdrw4cOhTCYYz1133QUT5kUwKOQNymqP2ZA809GkGmunn346bYUx6t69O4Pdd+aWe6677ro8efIoW3pWRDSk7nGzhUnqREDEmy7U94GRCmRDllQ80xyqZ2gXLlyYVjKOFuNLt1WrVo02WbZs2c0336wUlIOZkJo1a5b4ObbPnNcwQCO99tprdoqUgOOiDg7ZBRQa5NM4Feh8MwOFF6G9uML7779vD2r8DXOIEmzdujXm504yA0leF12xYgUVMHP5WFDRbvueIBfV0jAO/VYPil2Ek2evCThkLzLORbUpK+j6GJC5cbYUUCcR6CCrvSMrmjAX1ex+3IJt2LABX0SBmtQOSeGi7dq1830+zkbGuahWMG699VY7Wx3yMbtwg1yUHLjBnF/X1mstMuBBZvB7UzYXDa++8Oijj0a8FQzfiQUf5cP7IefUTtjjSePNQ7/RJ/Lw0s1F9X0/+8Mncbko0IIn4o1f3qVLF5MOR/VxORtBLhr1Dhleeuml8hch80aFJsJFAcJA+pIlS37++eeLLroo+NIxY8ZEvKW5uE2Boo5Ya3SC46JpBQPNKKWoty0qeJQxLiAwmlZAHhI0mrwUrRVyEGjHjh1btmxJliNi9uji96BO03rgfNu2bQw631MHDx6keFSBuivQgPlJ0/wMRtJFhhPM0yDxJrU305Kn0ZxBUB4cRJ+pyni2QaAJqRqylKzuQxhirgn/+uuv0F2fFKlHkvJeBweHdAOFg7aBfPr0AJd79+7FB9izZ0/Qa+JX0nkwi79MkWQuqvVfs6Spz7fY8R6jsbgoRjG4PAIwJMktnkO6kXEu+t1330X+ublL0NkSHag7dOjQ8OHD8+fPnytXrgStr2Iw2NPe0TRy0fCCrVy5kmrOmjXLboekcFFNQvu+6MigUMUzzkXxe0hp0qSJnb9Of5nNmUEuClmivsa94J+yZctCKlatWmWfk0wfbC4aXn2VHz7Wr1+/iBWISPBRPvWCb6kQL1MRg9q3bw8jUo0yyEXFKu0trIlwUepIIoIKpX/33XdNeoUKFU4//XSfMcBZl7ca5KLm0Okrr7yib1FOnDhRKQlyUeRWix5wzpgLF1r4tTchpwbtD/QJj+OiDjERM3bRsYGYBztzbLbJxdChQ+2zqQ4ODg7pQ5K5KO67ljTFM7Xn2P4SQzQWF929e/f3FrRGDBHNsq+sOsSFKIHtQTZs2DB37tzG78QtjnjBMHUZpEZ092mnncYj9mdR6G597e3BBx80iQrRkWAEoMmTJ3PzihUr7MQ0cdHwgvmWwnr16pUsLqqThBdddJE9Nw/p0rvCuejChQsjVpybaKwGP3z4cPny5amX/RWTmTNnkmKOpwe56HnnnXfjjTfaKWPHjiVnsrL3yh48eDAd0XRtLhpeffKvX7/+9u3bYXeKO/XZZ5+Z23yUT5sbmzZtas/k9e/fHyLnW76D6WWEi+oIq30+Sj1uvvMek4tGvfhJJ598si86NKUya84CXdajRw994TPIRekI05U//fRToUKFTCwrH8E7cOBAzGJEU/ZgV6tWLeYSd58+fXLlypXg0pyCmtgfqxAXNY+nm4sGxdvhqIbjojkk24wD3cLwZLSiqMuWLZvgMq+Dg4NDCJLMRffs2bNs2TJtUNaXUoHPs4kZu8iGOy+aAzFy5Eh5h3/++eeSJUtI0Udc4Kh0KMZJWwdxjuU9a+Or7/MAik9z6qmnPvTQQxA/iNYFF1ygjsa/N0tGMBBus7/VGwKccojKiBEj7EQFZbXDISp2kYlAqNhF7dq1i1swcdFbb70V+jpjxoyaNWtyCVvWqim0LWJF8VW4EV+4oNSAUdexpRYtWkyZMoU27NKli2Em4lcmzg3NnjdvXvMJBDVv27Zt4S1axYrZ4OQJtejZs6fJpHHjxnazwEWLFy9uDgzMmTOnSJEivkBQvALWUa5cOTNgcUR4sGTJkr5vdYaDt1MYc3IyvPp333338OHD9b96s169eoZqalHOhPkh56pVq5JSu3ZtCNvTTz8NDVOQHnFRenb16tV003333UcZGjRoQOcqlJy+haP/44KmUICZJ554gsJwqdVd3qtVWV/BDGbNmhWxQkYJlIfCSLrmzZv30ksvNWnSxHz/U1/csc9Ojx49esCAAeYSP9WsHGrBVgNTgKnSvHiKsGXbX1S4kdSWuBs2bOhbSA/BM888Q1ZVqlTRUjYtjPBEvC8c6oAxZbAD2KRWVNFj+9stQfF2OKqh73wek5+KRZNEvABCyf0KXyZlm3FgaiMpSHC+2MHBwSEcSeaiUe+MqGIxLfW+5mIfhhEcFz0aQXcowmr9+vUVqxDGUqlSpYgXtQJ6Q5fp/NsyD/pWHowFRmG6kh6HzeobbiIhZkNm586dIVpwQjxyaO2TTz6ZeNl69eqF22ou4bQK6gCDmj59+uHDh+EnCnYP412zZg3u+DXXXKPijRkzBn83pGAQBlUczgZlomq5c+fmTsjDtGnTihUrxk9t2rRR5DHVunTp0iZiRDh4S506dfTSwoULG67CEFA6jj78EM++R48eES+cI/SDGlFghTcsU6aMBlrMBo96US4rV6585ZVXjhw5slOnTr4PwXF/2bJlafDbPDRt2jTmUR9a2I6B9Omnn+bPnz9IrkJAs3ft2pVH8uTJQ1OrhDGrv2/fPn3n0GxAhabCw0lp3rz5xo0bIfyIWcSL8jJ06FDRHvRMy5YtRe1OO+00+t28Wock+Qkh4TY1FDd/8cUXUDvlfNNNN1HCRCry1VdfqeVpAQgwMlCwYEFY9KJFi2IWTDhy5EjFihWDGz0WLFhQqlQptcC5554rIvr7778PHDhQAUgo8/z583Uzskp333///XPnzu3evTsvJVtYNOItEW3WrJmhsorSRKsaSm9QrVq1YDioqLc/hd7xRSIJB12mT+xSgL59+8Kfa9asiYjCzLVlIOJtE1DbBouKGFA85UDnMr4UYsEn3omXxyGnAWXL4DrFA306ZMgQ8zmZYwCoJjSJaocJMyorZ2abFGAgGjVqVKFCBfdNUQcHh2Qh+Vw06h2d/+2333bt2pWOXXwOORb4EL4ABn/++Sd0QsfYDhw4oL2FccFTW7Zs8QVl0bN4w5s3b475KbMQ4OKfffbZ9h7O9CFmwaLexkt4i5k6UQicDL7LBiOF/NP6QWEGF08lOGvOK2IGn9AeXaoGxQpW3ACO6nucPhoxYkRSgiWmr/oxAdvZunVrsE22b99ueCC/Jvj9zBCQmxoE2UhQXPV5w5jYtm1bIrGjNUZ4I6IeDGgZBH0aLBuiW6NGjZjzgMOGDTNBrRIH7YkS0IsSKVWCSJN4Ozg4ODg4OBylyBQu6uCQxVi5cqU5O+eQOILnRYNYv379FVdc4UuEuHbt2jXBY5YOOQdPegimw4fr1q1rf7PewcHBwcHBwSGz4biowzGCN99887777nMLKWkCXNR8Bd6H+fPn9+/ff968edwQ3L86YsSIY2mv3TGPkSNHjho1asaMGVWqVAmu6n/33XfXX399mk7/Ojg4ODg4ODhkHI6LOhw7+OKLL3wBdR1C8PXXXys8RsyA1TpXCeyTog5HI/744w+dyTzhhBPeeOON4A2zZs1KcIO9g4ODg4ODg0MS4biog8PxiM8//3zQoEGPeBg8ePCyZct8N2zfvn3EiBELFizIluI5JBerVq0aOnSoCfjs4ODg4ODg4JAT4Liog4ODg4ODg4ODg4ODQ1bDcVEHBwcHBwcHBwcHBweHrIbjog4ODg4ODkcZjhw5su+f+Ouvv4KJdrDrAwcOxExPN/bv379o0aJhw4bNmzcvuV+6Sha+/vrrF154IbtL4ZBk7Nq16+OPP546dWqC34VOB/7+++9t27a96iEz8t+7d+8HH3wwYcKEL774IjPyTxC//PLLa6+9Nn78+E2bNmVjMRyOczgu6uDg4ODgcJRh48aNbdu2VYCxk046adCgQbiVn3766T333JM7d26lX3fddTia5pHJkydXq1aN9Bo1asyZMyeDBdixY0fLli0//PDDhx9+mDz/7//+L4MZJhdQ0H/9618U7IwzzsjushxTWLBgQfPmzTP+leZ0Y//+/aNGjSpRogSd++6772bSW55++unzzz+fVwwbNizpmdN6jNMTTjiB/BP5uHQGgXLo1KlT8CsDEydOZNiuWLHiq6++QmmMHj06U4vBW5o1axYzfp7DcQ7HRR0cHBwcHI4+/P333w0aNMCd9X0luG/fviTiXAY/vPTyyy8XKlQoZujstKJx48Y333yzeeP999+f8TyTC5h5Orjon3/+mUnlOTZw00030arPPPNM9hYDElWgQIHDhw9n3ivuu+8+avrxxx9nUv5I5rnnnptJmds4++yzqYhvAXbq1KknnXSSPuW1c+dO1MKAAQMytRgvvPACxbj22msz9S0ORyMcF3Vw+H9IinMm/Pbbb76U3bt3JyvzNGHfvn1xTfWePXuypjA5B4k0S6Yi8+Qhe3sz/O0xmz04WBzShIULF4p22p+H/eGHH/LmzUv6zJkzffc/8sgjt912W8bfu2XLFvJ//PHHM55V5uHIkSNp5aKw9549e2ZekY46wMw3b95sp3z11VdPPvlk9m7J5u1IeMuWLZOb7SeffGJfXnDBBcWLF//777+T+xZBI6hHjx6ZkbkPy5cvf+655+yUn376qXDhwnfddZdJYbAk/b1Ijr0YS68hOchP0l/kcLTDcVEHh+jq1atx5vr27ZuRTFatWnXPPffUqFGjXr16Spk9e/ZNN91UunTpf//738koZtpw8ODBEiVK1K5dO+aveBhjxoxp3bp1vnz5srhg2YvwZslUbN++HSZQt27dOnXqJDfn7O3NRN7ua/bgYHFIH3CUzzrrLJzaIUOG2OkdO3YkMeis0+Dvv/9+xt/70ksvHZNctFOnTo0bN868Ih1dgEhcf/312b4EGsSrr75Kzw4dOjSJeY4fP57Kmsu9e/fmyZOnc+fOSXyFjXHjxlEFnIRMyj8cAwYM4O0fffRR5r0Ct6pq1aqZl79DCH744Yc1a9a88847/LU3gWMvPv7447X/xK5du0hfmwoYCFlQYMdFHRz+30RvtWrVJk2alJFMDhw4sGLFCvvc1L59+/DVSMkWLoob0bx581tvvTW1G7Zt23bmmWdSvKwsVbYjbrNkHg4fPoztD+6oTAqytzfjvt3X7MHB4pBuaCehb7PfE088QWKuXLm++eYbk7hly5ZzzjnHvu3gwYOLFy9++umn+UunJPK6PXv2fPDBB/fff79WdT7wYC+J//LLL2+++SZ5Ll26NOjH8MaFCxdGvSNzeP+meJRt1apVUS8szaxZs+bOnbt//379tHv37tdee+2555778ccflfLbb799kAKlfPnll7r88MMPzbtS46IMw8keNmzYYBIR0XvvvZf7zz//fGVlL+ngWE+cOPGVV17ZuXNnIq10DOD333+/+uqraRBGd3aXxY8777yTgtEpSckNR3z48OFkOGXKFJMouptBryAEHTp0YHhmZENWyGbyuPvMK1eujMZO96vj4u233y5cuHDXrl0z7xUOqQHyudTD8uXL9Y9Rs3/88cfSANCrDIFgupDEPYMhSL7jcujQoU2bNr3nYePGjTGD9W3duhW2be98wGsP0nGySnrxHI4NwB7xJLK7FDGQL18+271mFGQXF40JnLx169aZy4suuuiY56KokYEDB2Z3Kf5/nHLKKcniojmqN9Pxdt9gcUgfMLiKVIS2MYm1atU6+eSTSXzkkUdM4oMPPmgfCXv33Xfbt28/cuTIxx9/vGTJkpUqVfLtxowJWB95XnLJJWTeuHHjRzyQGPV8+hEjRiDeM2fOxJVv164d/ujUqVP14Mcff3zbbbcVKVIEcrhy5cqCBQuSQ9OmTSEAChJD8caNG0cxFHPorLPOwg2ibOXLl69bty6Oe6lSpXbs2BH1PKrp06er1tpbuH37di00nXDCCaaoQS4KrUVQO3bsqCisDEb4p2nGnj17cn+ZMmVUKXkg3377badOnR599NH//e9/tWvX5hF4cpo6CEcI4kHdu3fvfsEFF1BfSJTvKC8tD7GH4depU+ehhx6Keutyo0aNwpuvUaMGryYFv5D/ixcv/uKLL/peAW0eM2YM+d9666203meffRb1ZnzGjh3LqytWrAiTP3jw4O23307722txNOO1115L7Xr16gXvKlSokPg5jYNI0Bp58uS5+OKLBw8eLMJ2zTXXVK9ePWjRFixYcN111z3wwAPdunVr06aNOZpIPuTcoEEDaC2X+MStWrXiLffcc0+a2pAK0hqdO3fu168fNa1SpUrRokV9wXiCbQhGjx5N+ZGl/v37r1q1qlmzZieeeGLp0qXNnlVcTVpVskTvmIVQ0V3xcFrp3HPPJZMVK1akqdjcT4/QLPfddx/F+Omnn5ROY1L+oCFAvOmju+++m/LTdIg9smp+xU+msy699FL6i5GL8jQt8OmnnzZp0oTG50WMOy3wfv/997qTETR//vyox1IoRvPmzakagnRxChjIVatWnTdvXiKFFz788EN6nDHbt2/fOXPmkJuk9LfffjMx1RjLPMjYROTIiua98MILfVVm3N1yyy29e/dGqOrXr79o0SKlI0IYbqSXwmv9lq6EPyPMLuRvCBAJOg5dQbNHvQVS/n/nnXekJ3/55RcukZadFtAMCOTOf4J7uPODDz7IjM3bQSTZcaHQFJ0KLFu2jMqrJtTT3ECFGR5i2zYXVXv5YD/o4GCAia1Zs+YTTzyR3QWJATwh271G/nMOF8VBwQmw55KPBy6KC4jfnN2l+P+RLC6a03ozHW/3DRaHdENc7qabbtLlunXrKlSooPC2ONByWDG4ZcuWNYe1fvzxRzxFc173jTfe4OZq1aoFg23GxFNPPeUjulEvXCcE2KwckhVuMbe99NJLUc9JhbFwCUGlbLjFeLFPPvkkP+HFkl6uXLlXXnlFz8JVSME/NlQWzkwKvrV5HbTKcFHhpJNOCueiffr0sdfTcKa5xOvSpWId2Xt0aTS8ZxOsFU+OCkJm5OclgoULF0Ln4HK6vOqqq7R3esuWLeae559/nr5QMeDe3A/ZpvVgJpAu7t+6deusWbNgBTAKLhlr9isgCbALSPXfHgoUKGCYGIADKAfcfUg1/2s+gvyhW40aNdL6Mz4YrXfaaaeZB7/88ktuhkna77rssstI1Mq2gJ8Ghz/vvPNoHKVUrlwZ8dM6xK+//nrDDTfwyMSJE6ky/7/33nulSpXKmzdvgpIW9VZooTd33XWXlvuGDBlChtTFvidmG+onTIA29I4YMYKsYKRIDjdoAkVgmCD8dobUSJsI6Due1dyHCdYVFxSV0YHwaDhowsicz9QGGXi1/QjDlhFqZjpgpNwzbtw4cwPjJX/+/KrX4sWLaWfzU+3ateGi+p/BBaE1xYD0Ull7hwJ9Qc5PP/20SdHUktnMGV54MG3atDJlypgZB00e2TNZkGFSjEiA//73v8EqP/PMM4icGY8UO1++fKKahw4dWr9+fa5cubR+i0hTbIa/EWCHmNi1a5comFH7qC9SNJWA4uL/n3/+OTwTfOzly5eTSZZFoEiy4/Ltt99Sz/fff//w4cOYAcY8lxrwCBYjjZ8M1bS5KIpSPN7m5YmrKofMBrpp0aJF2hBFT+FzYI3UQd9//z1mgBRj0Q2++eabKVOmoD7Q42Z7lYBUaGIS/QWrxLMJ7hBbu3bt2LFjBw4c+Oqrrxq7gkpt06aNorG9+OKLdoy7mPcn+DrMpO/kBvJJlcmN+30hDVDBuFDUiwL4XhTCRbHKL6ZgxowZiuPy+eefK8XeShcT2AnzOAWwL40Dxz9cmvNgDCJz1IcKKpgePcU9Wl4w/IH2weZhcdMaV+Drr7/Gj8Ra42WaPXUGNDI1paGQEDtgD02BXdm3bx86ccKECbw36Nthh7Be/LRy5Uo7HZVKnlFPDvEtjIlFdQ4bNozamYnVqGeVtemOKr/55pvBZjHIoKyGY82aNTw4atQoCh/kovQF5XnsscdwNG2lRyvROGhOCoBg87ix/ZnUmzYgJ5Iu+UbmEqCuo57S1qW6IO7bg80e5KKpCYxDOBgINH7BggW12gbHQJxof61OSPIZLw0aNDCPoD8hBkdSAKOAinCzNsrGRZCLMoRxlLt06WLfhtHntpIlS0pP8hYuIUu+EaT9kIZLRz1XmxRUvUnZsGEDKZBbkwLJ9HFRBlc4F0UhwISNz61Tc0Z/BrkoEgs9OGIBGhlJ+DsfDF5eBzEzeya12ma2Fkc9Ao//rWYX9a1Zs6b5lbdDyNGB4iQKeGM3FCqldOnSl19+uS7ffvttu0aAFoP7oaX5ifx5kQoDl6NgRn+ivXnwmmuuMQ+ifEjxrZVVr16dFjaqngxbtGhBs9uhs8T9kDddImYwCpQnVEr67fTTT0d9JdKAUW8xsFatWq1btzYeI5yc/O1gPOFt2KxZMwqgVTuB5iIHVL0uscJc9unTx9yACSAFjo0ieuutt0jhLynIT4LF5tkTTzzRaGy0IqPP2CBtCTaXUW+ZkfFrM0/tGKdsJuXiiy+2t0ybuEdUmXfRpGoiXopC0E8wEx5p2LChXTbNDpgN6jxVvHhxe5N/eOEpZN68eTHQ5v46der4dsJzidm1U3r37s1LEUKTotFnz2tgTWytgnehXhg/frw2ffAPKe6LwSEQC7M1jIiYPsL02Wef8T9qBJWCowjtj7nmh19t7+zNAiSZi+JymTpHUxpF5zeosDbuiqP7uCijgpTsDW7pkBreeeed2rVrowLuu+++rl27oshatWrF5ZgxY/BTUet33HEH5hCDZB+Shkg0atToo48+QpGhTU499VSpflzMXr166YAT7jVZXXrppVw2b97cPIunwou6deuGLCFUTZo0qVSpkvZp4AHrfBROz8svvyx9GnJ/3NcxIFUdFL0pAJYVEwsBIEO86ogVGgQrouUFKsuL6tevbztD4euic+bMkcuIhVAKo4DGkVMY3gs4EJprxBHhf4y63MFq1aqZhQh8KUwyiga/EIcAg2E8M0qinTNUh3b74Ycfoin8Ac1+wQUXXHfddTijdJOPiYWA3sdPwlii7LA9uXPnptlr1KihX7FVHTt2hKO+/vrreDA0mmYr8Am0exDD07Rp06uvvhrfFFtoH0vAa4HfQi8HDhxoGhBBotPz5MnDK+gFbSGj8DTdlVdeiculD6CTlfbd7dmzR0Hk4X5UGe822CxCRmQ1bq9hgzt37oxdR+9fdtllvN3moryIIi1ZsoSi4rbiNuHnoQnxWelK3oUzVK5cOR7BnaKh9LnIzOhNHxhZKoAoJXRXO9nwzuVQ0uy8xZwICnl7as3uGyypCYxDXCAA+qbo5MmT4T8MAU0Bo6BIvOqqq/ifnkJjmEe0KfeSAOR5x0WQiyKopMCBfXeec845huKmdoAzyEVXr15Nir2jQY6pHewqHVw0ah2lwxuBdnKDWXoNclFGLo0ZbKWRI0cm0koYl8g/Y6WiZyLW1zXwjlBo3bt3j3q24KGHHkIJmIgyOI7cjAJ58MEHlSKFZgoc9agm41RzeXT6mWeeSUcb54qhWrRoUcam2YosyOm3fXo1+LPPPmtSIKuUzV4YgfdyDzrKpIwePTq4PC7VNGvWLF3CPNEJEEhNlOAWpmmBkerTp/aZVbQ9OUjpxW1DhkP+/Pkpg+1zq99NCSXMaB5zw7Rp0zTTp3lPgA0ixZ7oDAH6PHz5TpHeDKVHUM877zysjH3OEzE766yz7KdkDTEiurQnf7XtFkPm+2nmzJmk9+/f386HgY8TYuY9165dyz14cYkUHnNAe9pDlcIz7uxJKI0jn8hVqVIF+2V6gQ7CIvjihGlOzZTk6aef1ryPOZCl7wkhQjHL5hD19CRkyp5SFC+TzqHZfUdJV6xY4WNeWG3SUY9ZuRyYZC4qnml0xM8//6zFYpt2ar+yj4vC0WkafGh0N5oFvuEWRXMU8IBRARdeeKFZrMDDOPHEE2FrutSsodk3y/2YB/tz2ChQUswyZrFixXjcTN9ec801PG62LUFFyN/IwL59++C66GUZMzku9h7d8Pvjvk6bkQwXRTLR7DBtXTJQcUfIIeoZNuyiMQZTpkzxTfXF3aML+7JfDRo2bKiFprjgNp41U+AA61WmTBkzlHidiQRIIj/Znpm2vQV3dZoJYzQ+l2ZKNRw0Mibf2Bt5ombbDw0FdTHzau+8847dwnIm8E5Uck3Ajx8/Xr9Cz+yYB2oxzfNhYvG5CxUqhLxh1fDJ0CfK3JhhnsXIaeGFQvo82mCzZFBWwwFXLF++vPEwYHQRK3YRHVqzZk3zK358xIpNKiKBHEqwEXvqXqpUKS0xJbc3Y0JzH2b+W7vU7GAeeFRGdMPfHmz26D8HS7jAOMRFixYtaDGoDh62WQaRghJXKVKkiNkyxz+aW0z364JcVFOEvj140ZTFHEWFyTgXtedx0sdFGU0oq27dur388suU36ZkQS5atWrVjIR61tK0YZIbN27kslWrVqYkKHBSMEB4hBidq666ylYs2rpMutlKfeONN5JiTu6hALkkkQ4dPnw4HAMNbPtOuKTcABPT1gkBekkKN9t3KhiVUYNaK6tfv75dHTE0My1LMU466STa3PdlJkY6t1HZaMpqNkPbnLR87rnnSKHxE2lAPMNcuXKJZ5qClS1b1ix7xm1DHEt+9R1PxXJFvH3LuuzQoQMmw/5KDeLhewrBg4MluCMGYkmGqe1vxKM4+eSTbTGDbvE6mtek7N27F6Nzww032A+SqBBxCLAvT/gG1oFHfIbplltu4X57bxGl8k2nDh48mBQdKI1b+DZt2vCrvWL25ptvahbMpGCzIv9c9ZXhM5If9TYVR6zFc0ELtsb1uuKKK6iRoaagXLlyLjZvOIJcdO3atYaLrlu3DtWqXQy4x6Js9mb1qDe5Q6KtMbIASeaiIplmL7I2LgPbWgS5KNrEbNw1ZN2OyeGQ7QhyKu1yMfMO27Zt49J8uQ5TUb16dTsH+tSe0sN+2EdTpIulvHbu3AkT6N27t/24nAbxDR8XjXt/+OuiXiQM2/GdPXs29s+2OoxeozQfffTRxYsX63+d3rGD78XlojqXZRqKdkvTJwSaNWuGZ2l8Su17MeW5++67zdGmqPc18ES4qLmUK2ar/hDIxptewB2xZ7sxlkWLFn0qBXKqsGGaFtUmLrPqJYcJZ0iXkDdsknlWm+L+85//6FeyxYuyS8Kr77zzTuNF6ZiN5tGDXDTYLBmR1XDgOpx66qnGExXsPbp4PHh7pqa0vGZ89KuOZtkekk7faWk0ub0ZE+pi2lOX2u4F29El485u2Lhv9zV79J+DJVxgHOJCtFN+v5nW2b9/v0IEXXDBBbYjqNm3K6+8Mt2vC3JR7bizN3kKOpOp8ZLtXBS1gAD36tVLE0AqcwgXxfXP4BcmO3bsiIbBKcIXRHHhypv5XO2nhbnde++9EydOtKfDBO3CGD16tF0ee+tjw4YN1eZYJXILDhZVEPVoJ2ox056lwtjBTimJSdHmavvcaTSFKpglRy1b+b56Ik+gSpUqutRmVFvSkAdYU4LBOXWO0f4KkUTFTKPEbUNN8Nk5rF+/nhSzX11Lx75drGSofcW6RPVxmWDcAU0Zh5yEVwhxs4OAApQoUQJ6bEuyTlcGAzS+/vrrEe/EtXG9DLRyy0i3xRXezs32pIOWPY09jXqzveZAaXjhP/nkE35t27atnSg7Zbd8+/bt7Y3c0ZSpSbObQAv+JUuWtPOh2BUqVKAkYkqMUKwnzW4mQ1U2eyu1QxAKohvcoxszGra27Npsa8+ePUu9WEdxQzEnF8nkoiYosNkxiLpJhIvCBDA8a9as0WD46aefdEPWhBJ2SARBTqUoCEYh8o8xS4cOHUKh+CgWidxgwoj7/HtpXsxMNEVX+rb9aN1Vi34+Lhr3/vDXRQNctF+/fqVKlQpvEMYwZl5LZPYpuERiF+GanHjiiZqyefzxx+1tUXExY8YMMlTAD4YVfglZqZrUwmdQ08pF5e3ZHmEINOVvFjCxdrzL8EkIzDnnnLM0AK3p+bjoxx9/bCahNWs7ePBg34PmZvwGsw3YByQBE4sxjqTsgovLRTMoq+F49913feIR/ScXrVWr1lVXXeWrqbEiQS46duxYY9GT25upoXLlyvhJUuAwHHn/Wk+AkysmTYJvD+ei4QLjEBfISYECBSJeIFl7nUq72nx+LR2K2J900knBQ7l2n4YgyEVfeeUVUipWrOi7U3NJ8i+znYsib5Bz42bF5aLazGnvfBFmz56dYHhJ9Dy0B72kQwf2T/ril4/vGWj1jMKbHXTy4A0N0ylBeF3IfI3Iqn3mMJpC8OzzfmKM9tc1tVty2bJl9oMUBm1gPDeFHR40aJB9jw41zJkzR5darrcDn0J6E1xqRg/nzZsXqbbJlXaLmIKFtyG48MILixUrZpMxvBSyNacltUPVjomF7SClQ4cOJuXll1+O/DOMUAgWLVoUPtEjemwWiiXq9nYnRqVk2yxY2StX2q5ieJ35CVWp/fBmsiBYkWjKXCqc1jzFkDGeQ3jh9aUouR/Ce++9ly9fPvvzMDQ1HNIEUhKuvfbaSMpSeTSlPZEN+x7GVMTbkW5y5tIOI6y5jzfeeCNm2RwEEShb1dCS2q/KONKhd/MTEsJP9mdmt2zZQoovQkoWIMnrogolbE4oQUrFsO17Yu7R9WHlypVLs/bgrEM4EuSiCm2nc/++D9lFvRNKhQsX1v8h/r3olu8LkDLD0tc+Lhr3/vDXRQNcFA6Adk5tlzgCjGLt378/HoBKklYuqr2OmpisX7++TTbiQofBNDU+depUfEH4MNZ67969eFS+U0yZykWj3tknvCXZQnQfjqCxi+3atQv5xHwIF1WAwZCvq8fkojgWdN/MmTNNNRPkohmU1XAoXKHPg7G5aKFChZCl1B4PctG5c+eSMmHChGhWcVG5pPPmzUNd16lTR27Tww8/zCWc3/7sVga5aLjAOCQCfQ3S50dqEQbn2ze3K5++VatW9vw3fqphEeHQB1RsLrp///6yZctG/rkhEB7F2DEhT5PLReV5m7OX6MBcuXJRU3OD73U67sgANOxOS0lmY4uWi+vWrWtyUNxOXG17GQqXJsHtzdgIyHlqXzPW8T+bBUU9Zahhpd0Zffv2NT9pKmrJkiV0JY1MxzGCqK/tXPK/8Sz37NmTJ08ehq3vvdWqVSMfswdvzZo12ksyfvx4WkYkjZbHrFASc5xMAX6kr8SjFIfJjvkH8c6fP7+ZoDxw4ABsuXbt2uYGRWTF9qFA4pIKPEButqMc6asevIKCffvtt3RoeBsikzAle0TgZCMk9qlm8StqRIaSJc2z2LuIb7/9dlIoz1YP4cX+8MMPI16oZDuR1jZBIqDH2E1aFZGms8TBbrnlFnMz1LpZs2aQ9qhnEGkrxMDYVm0jMvuWr7jiCvOgeKY546rDLxhTpMJ8d1eem9EGEjMGMuIEDwkvvCYazF5iOLNO5+qDPbD6aMrIpV94qdmlxRgsXbp01POI8KxkyHwhmpGT6tWrm2Ba2tqmTUACvBSBR6h4hbaG/f7778uWLXN7Z2wg+WJYmpGkPXXJWMCX0P/agE1HaDuuPVelL6HYociyBknmoqqYOVisz7fYuyOiqezRRWpti6gtkRkJAumQXKSJi0a98xgYId+aBolmg1+If6/dQb55Ne2rURQ7HxeNe3/466IBLiqmZH8zPerZeAYzwxt/y+w8TB8XRdTJBE6FUfEdCEkEIiGY2wYNGjCaFHBy0qRJzZs3N9ZOyGwuimrjpXCSfv369ezZ0440c/PNN0f+GeQ96k3kS+uFcNHvvvsuEojXH/Wm6/RPkIvillFNE4giTVw0mjFZDQdFigSOKtlctEKFCjgcvlkPOlFbS4Jc9NlnnyVFBj5ruCgCRlu1b9/+lVdekRjTLGXKlFm0aJHtJSfy9nAuGi4wDolAX0zxBT6NepwtePJWHFXsrn///nDLNm3aJC4tPBIJ7ABfuHCh4pGYSQrIAxJuYtpp1wOOuE/mNZ9oj3pczIi34dCkiMYwZEyKdv/CNFAOr7/+OroUf1csQs6WjsUWKVJE96PAKV7E23bBI5StXr16ES+20Ntvvw03wM3lBqjOtm3btHuNfIoXLy46CvVC1UMseSrBTx2ghRQArGrVqkOHDvXtq1QXwLU0fY8KGjVq1MSJE/Wrzt/axL5z586yuX369JG+UsSa4cOH6wZoJKzJLAYoVJ45f26goaqJS5jtgAEDxL4Y1GhybJyWZOvXr49tNcRDUXC4c/r06XLqFEXigQce0A0UifLQPobq60CKOV8aTVnamj9/Plwl7tBWd3A/BBJVALN68cUX6Y5KlSohUfpMTngbaker+aAOdK5cuXI0iL0QAu/KnTs3GZpydujQwRe06bzzzitWrBjU11Q2vNglS5bEppjVFPrl3nvvlcwzNBCJpk2bwgY1laPtM+XLl0dcYQ73338/ahCL06JFC8qvRXuKZIIJ6Sy9IZwUzFA+OLYd5wnBjniL0oxWc66HtrLPpCg0Iz1F19OG4YXXPgIKQy3wz3v37r1mzRoxT8RJXFSnT9FFtKfa8Oeff9boRpzkLCHDCJg9uuG0+DP2GUVGWaFChezpTgqGsmJMmVBMderUiXjbrTOyi/7Yg2LBIhUMHJ0I1S5cWkkcbfny5fykNT/EyZxHY+TaPDYrkWQuquVdPEtJBnyAS993aYNcVOF2aTLRUdoFO7Q0gW/gOGQZ0spF5SVonUqQPjKhTUL8e8YDehnzYM/NkBUpCieDx2Ob2Lj3h78uGuCiCq6AtbDn21B/jE/fSpdmNNPKRaMpM9wUe+k/z+4nAi351q5dW7tZGEflPQRX2HzeP8Ym8s/PCWSQvdDIxur7oGUT8rfn7DFOIhshXJTq0FP0nR2xkJ41CxFBLiphMzRGc7fioiiTSCAEjq9ZMiKr4dD5llKlStlx6uCiJvCGPjZoH93hThwIGeAgF8X1r1ixopo0Hb0Z/OhOItCWNhpNg12jA0rgC5KRQS4aLjAOiYCmq1KlSjAcPd6h1tJ9wAHVVsCIF9wbhzKRM0Ly2hkREW+NEfdXn1sQVq9eXatWLbQTbiu0BLfV2PG33npLcYwiXmhfswALt1GIZsrA4MJ/ZXBpc2muXLkefvhhReMwz6IKNE+Nz63Pb4LWrVsjn3AGvFVMA141nFwB0iPe+XwVcsSIEeQpbgkjQobFFeGZcki01ofAI7pKYRSLsqo8Xbt2NaeQ4kIzOChqBf3G//ZtgcasoOsKFChAC1BaO+IIzUgj2062qAUU0cQuQsupBRRqG01i2yx9WTQYjBrire/3QGNoTF6hE6TVqlXTrMGuXbtoAQpmrzeK9SEwZtYv6i1eod/QCZMnT7766qvNtzEFLbfaQ1ibM0uXLm3LTAi0BZdmR+GIlWm6gQ41iiKkDTVh165dOxxuaPAll1wS3G6tb2O2bdtWHrmOj9o0KeodVZB7k2DsIhg+zVKiRIkbbrgBrksJzcjiH+g0qq9bt26aUKD9kV7yz58/P6ZBe6f1UVAzy3DhhRdi4pHeadOmMbiMNfz999/pRDqOQQQJh6XbAqZFY/I0MqDZGTuEgc6Zk4O5J6TwDDHtfYAl0mJ4RDpBWqRIEePJqM0pidmwgEwi+dTOtnSICq+ghDhRt99+u/2WqBcDgj5VAHADifott9xi7tT+/4i1mdkh6skY5NOcc1m7dq0xCvq+rvnp/ffftxcwdu/erfSsX2pOMhfFiohGrvWgWvlOpAS5KMMbTaF22bhxo3g87eVC6eYcaCrOPjWu2EVmv4oiFpiPv0EeUE8oTaO7H3rooTp16hgloiP1JjfNshvvBLaJ+enZs6cueapx48bm7drGiSrEZdcXCMLvj/s6KWgTM4bHq1atKr4HacSG4Qa9+OKL0ZRdlzjQuEdYtSuuuEK+kfQ4D1IMO7aENsAET9tTcpwhHIj0zedRVAyVmf7UbKXvbE/Um80l3bS5PhaPdScFe0OKjlaaaMOyKyG7Rm3gteCv4GZhHRcsWICE4HMY/4B+l5vbokULrB0d1KVLF2OKFA3SnJhXjBxzUERxa0499VRkBkb61FNPUU6z2wIraK+NRFPIJI4XlnLGjBmY3oh3HkZkifspCe4jjFdOpK9ZMiir4dA5GWyqJhqfeeYZJARHkHrxOlpAnjGFx3XGjWjSpImJiiQuaua8ETnKaaIdprU3yTx4MjYR6Dy22WcIoaVJfdsQ4r49Gmh232AJFxiHBBEz+CEmOOQgAGrEHrlJAZ7Ahg0b7DWNTAJSROHNLGQiLBGaak+j4Ir5PhHx2WefBZcFuI3RasQ7EaBGzAIO5cSCwC3xyH2bpckZbyeRby/hEX3++ee++QIuN23axHBL0yfxKAMvNWtl9D79Zeewffv2YBwg3h6M4rF3797Vq1fTaAnaMrJN06QYvbNmzRrT8hQsyK5Ta0NsAToTOcRniBm7JeqNDvvobEwwfIKtEQ4ak37hvcHK0uy+FRqabqMH4/RiXm2xFNf6+eefaWrbo0ZtSvi/+uor5NNHIciWqtmJWsq2ZzD1Lp/whBQe/oxvbx+go+vtIvEspta3zwjTHDxzR78gt8FipwYKE9wsSc54a2kamMcJ6AL0IS3jG5hcMmaRJbR0ziFZSeaiUc8YiFgu9b7mEgz2FfO8KE/prKnh8Wn9mrxD5gFvWBPM0Kfp06eja2Bop5xySsTbrYGdQG0pig+JY8aMkQuC6sGtrF+//hNPPHHHHXd0795deo2/mq4Dd911F/YD/ajJNiiW2XOI8FSuXPnKK6/E5+7UqZP9oWokp0GDBhEvep6ZjUvt/rivgwiJMJxwwglDhw7VLD5y27JlS/EEHAjzUWx9d1tTmH379sUEQpk00Ug7dO3alf/x+GEIGBLYhWb3S5cuPX78eJ9n1qtXL1+8pcRBeezNvdiSatWq2Td88cUXCpAQ8Q6W6CQ6RSpRooRm1ukdKqs1AbLCOaP8imkB77IjA6cGGlaBPWwgIWYtGsdFW2iUp4lpDHctVqxYxPuQPSMdY6klNVpJR4/oXxpQgVhETrSba+vWrVpQjXiLqBRYGWLMVK/ixYtTciRB0+TarKgPo1OA4cOHx2yWaIZlNQRYAqQCkUCWaJyZM2cWLVr04osvfv7552WAofGlSpXSK84991w7PK+4KL2DVFNfZN4+YZXW3nz22Wclz6aDEgTdgbE3k9xRb1nbnn1HIYS/PdjswcESIjAODkcd9PlEH8PX1y/iMh+HpEBTzO3bt8/uguQg9OvXr0aNGsfSjlbMvYn07nD0IvlcNOrN3v3222+46Wmaav3zzz95CiYQ5PEORy8OHDgQnMpNHEhRzBBWiBYObnBSJ7X704c9e/YEP3WryWkzk4e4BidcEkHTpk3TXVTa0zc/nci0etQrbbLaZ/fu3bfeeivtg9e1ePHi+fPnw5D//e9/+2w/PUJPpUMAFEohwXMLf/zxB28xeoPWsBeCvvrqq0TmtjIoq+HFI2cJku9Mr7Bt2zZzps7A7NGlOjG/7p3W3qTLOnTokI7tTL7jEjt37sy8gO/pFhgHh5wDBZjxDfbly5cXK1bMyXbWQCdozDbX4xZYlkceeUQey7nnnpvI6ZKjBTgePXv2TO6eDodsQaZwUQcHh3CsX7/eDn931AHWd+GFF8b8Go2bpEwWgudFM4hPPvnk3nvvTVZuDg4OqeGvv/669NJLUfJmH+zatWsbNWrkC+XokHnQdqcED1Mcw1DQ2o0bN44dO/YYs87pi4DgkAPhuKiDQ9Zh/vz5/fv3nzdvXq1atcwW06MRO3bs0GlA+5wJhuHxxx83n01zyCDERU2M+wzi119/xRdJSlYODg5xAR2FCPXt2/fBBx8cMmTIs88+604eZRkGDx7cuXPnTp069erV6zj/IiVyOHLkyH79+iX46WAHh6yH46IODlkHHYyM/PO7fEcpFKSxcOHCLVq0aN++fYMGDdq1a6eo7g4Zxx9//KHgjb7vMzs4ODg4ODg4HDNwXNTBIeuwffv2ESNGLFiwILsLkhxs2rRp9OjRjz322PTp0zdu3JjdxTl2sG/fvuHDhz/ioX///lOnTs3uEjk4ODg4ODg4JB+Oizo4ODg4ODg4ODg4ODhkNRwXdXBwcHBwcHBwcHBwcMhqOC7q4ODg4ODg4ODg4ODgkNVwXNTBwcHBwcHBwcHBwcEhq+G4qIODg4ODg4ODg4ODg0NWw3FRhyRgz5492V0EPw4dOrRjx47sLoWDQxKQwfH122+/JaskmYQ///wzWMfdu3f//fff2VKeHIJff/112rRp/M3Ut8ycOXPp0qXB9P379y9atGjYsGHz5s3bt29fIll9+OGHU6ZMOR567a+//lqxYsXKlSuzuyA5Gt9+++24ceOyUf/s3bt3+vTpaJLMewW1e/755w8ePJjBfL766quklCeDOHLkyLp162bPnp3g988PHz78wgsvbN68ObML5nBsw3FRh/QDnXXnnXeWK1cuR30t88CBAz179hw4cGCZMmXOOuus9evXZ3eJko+33357woQJ2V0Kh8zFF1988cADD1SvXr1Dhw7peHzVqlX33HNPjRo16tWrl/SyJRft2rU76aSTfvrpp6jnvw4YMKBp06Z58+b9448/srto2YN33323ffv2uXPnjkQiiEHmvejrr7/mFQUKFMCntNN37NjRsmVLuOXDDz/MDf/3f/+XSG6oXG5+7733MqewOQXIZ/Hixanp448/nt1lydG44YYbaKVBgwZl/auhdldddVW+fPkoAEKeGa9gjFx33XV58uThFRnh23/++Sce1IwZM5JYtvTho48+qlatWvfu3WfNmtWxY8dGjRrFpfELFy6k+itWrMiaEjocq3Bc1CH92L9/P8YYTZSjuCg69MEHH+SfDRs2lC9fPuaU/1GNSZMmwbSzuxQOmY5Dhw7NnTuX8XXllVem4/EDBw7gIiROJLIRDz30EIVEn0RTdjSULl2akh+3XDTqrbydfvrpmc1FeUu3bt2CCrxx48Y333yz/u/bt+/999+fSG5PPvnk1Vdf/fvvvye5lKkDPz5b8rz77rsdFw3C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xunTpz/66KP8+fOnTZu2aNGiLVq0WL58+dPOlAMHTwcjRozIli1b9erV/fcj5cCBg6cIh4s6cODAgQMHDhw4cODAgYOYhsNFHcRePE+HVdy+fVu51faGmPSgTWbu3r0bY69TUA7Enxbshewte//3f/939uzZiPqQePz4cfTVaUxqizdEwkOjAwcOHDhw4MCBgsNFHcRS7N69O27cuL169XraGQkAHjx4kD59em+nnMFYJk6cWL169QQJEsRATiZMmFC/fv2goKAff/wxul9nwtixY10u16pVq2L4vW7DIeGQIUOKFStWvnx5b3G8ZW/UqFGffvppuXLlUqRIESGvpLVr106aNOmVK1cil2eP8Kcg0Y1du3Z17949T548derUeVp5cODAgQMHDhw8B3C4qINYilOnThUoUMDPU55jOZ48eVK5cuV27dp5i3DmzBk5hzoGcnLjxo133nmHd8U8F12xYkX+/Pl/++23GH4v+Oeff0JCQij1f//7X29xPGZv0qRJZcqUcRtneZcoUQJe6v9LBwwYwCOBnX/2pyDRjfv378PYyQOK9LTy4MCBAwcOHDh4DhB42/fhw4eHDx/eZuDQoUNYLdY4J06cwODTj1LFRD59+nRoaOivv/66Y8eOkydPOg7EHPiPJUuWhIWFBSQpOLDHk/oCDlOeK1WqFANcVDBixIiY4aIBrJeAIG7cuBGlcK+99lqrVq30ELq44cOHBzRfvjFw4ED9MhIF8YkIVdbNmzcdLurAgQMHDhw4iCICbPv+888/MMlffvkFSrl582b+cPngwQMVAf558eLFXwzoXPTIkSMSGBISIn/279+vR3DgwBuOHj0aFBS0e/fuqCd17969QoUKWU/qCziseY5JLvr555/HABcNYL0EChGlcLdv30ZQrVu31gPbt2//9ttvBzprdpg/f36yZMn0kIBz0YhWlkjG4aIOHDhw4MCBg6ggwLbvuXPnoJHbt29/9OgRvHTXrl1cnjx50m1MJoSFhXHrl3AoqsktCfnzzz/dxlo4qCyXd+7cCWz2HEQR1OBXX301bNiwn376yXTr9OnTs2fPHjx48Lx58y5fvqzfunHjxvTp0zFer169Om3atFGjRpk8re/du3f06NGTJk3aunXriRMnVPixY8eWLl1qH5M4OXPmxCweMWIEJvuFCxckJqxywYIF5GfOnDm6hxWU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7JQPLBhMsZo1a6ZJk+bmIznYOpi5r776anIL8v+ja9euD7pQp04d98YYBxhNHTp0wDJLmzZt+/btk0ZagySDXy762GOPocBiK4iRrQJahMJFjx07xjxcr149lRIKFx09ejSJMFIrEVzUW1oVUgW1f/PNN/lXnjx55FtYKFx00KBBXOq+iASYWX6/3MvKmH6UUSAm2qJFi/hviRIlHP996KGHfAmnTFMOFw3ap6FwUfHWq29/teytv+nSpbvzzjvlMlwuGrRTgnJRb53xW0JQIZWmnThxQvxR0T5+5TcwuPmAdeo457lhwwZSmJouX74sXPT8+fPyLzkUunXrVrkUagoX1U/aJw0MFzVILK5evfrnn38++uijTPqhc9HevXvff//9HuuoFFu7dm33e+76AWF4w1ELDy4aVOyUD2xBJiAJSXfzcdEDBw6ULVv2o48+Sm5B/j8cOnQoJiYmb96892rImTOnbnr6BfaockvDKGjQoEGSyGuQdHBz0UuXLuXKlUsFqJCwHMpSFw7zzDPPyKVfLjp79mwSdd7CfKU2YVoBuCgme1xcnDj9j5iLekvbrVs33XmjLKnJR739+/fzW/fNY7lICASDy9SpU+uvGNggPMTyB2EshQoV0oO+zJs3T1qbCbxw4cJk+Oabb9R/MdTuuOMOxVuCcki/YkfAReXQZoECBdQqhHhIVu6OgvapOKd17L91cNHt27fTelmzZkXHVB5x4at8HYfLRYN2SlAu6q0zfksIKqTukoompaPvuusulSKrQ36rY2BwEwADTwinuO86e/asXIrVygAUP0aW/SmKGUCWQC37m5fk/O233y5rSBqxo89FaYhdu3ZtsLFz507d2GUSjI+PJ33dunVbtmyhwu4tgrycvvvuO3fUaYMUDvlEGjoXdQMWEeidd/2Aug4cOFBdyndZDy5600DWDVIgF50/f37Ut1T16dMnugWGjgEDBrgHBabqiBEjvG/ElPQ48BYWHEpukEIgXLRFixbqPdivXz+4pTrhJmE8H3/8cYnJ+dhjj3F53333wQGYLc+cOeOzHc/oO6lWrVpFYtq0aVeuXImd8frrr0vEixkzZnz++edWAheFAyhHo1988UWGDBmUo5c9e/b47BAvqkxmCdlVq+ySrl27kvLOO+/o1fGWFjrx5ptvqszwhwoVKsjvixcvpkmTBhngCbt375b1vbFjx3L7008/rW6BvJESExPTrFkzHt25c2fGUaDQkei8OCLKli1b27Zthw8f/uSTTzZq1Eg1NcyNh/773/9W2xPGjBmTJ08e1fjr1693LFeKT1cVL8Sv2Bg/5IH/qLuClmPZMVp8tm9Ymo6XoNQUYaDKV65cCdqn8mmgY8eO1IXbRR+aNm1K4pQpU9RTJFuvXr3kkqYgT82aNZX+9O/fnwxkU7eIM95x48b5beSgnTJ+/HhfwjlkgfjRrV69ulx664zlTw2CCnnPPfdIswjg7d26dZPf2JaIWqRIkSQ7BWdgkPTYsWMH0xHW7I8//igBXZRNJZFaAHmElwL5OsOg+9IfkkbmKHNR5k0587p27VoIp+xalu9wzHdMrFI3aR33kdnTp0/LUdqb7MTXrQBZUYyYi/Je5xWi4owlGbD4dT8Ktw4XFS8dKY2LYtLFxsZGN7zyxx9/rLsATWLoJzEEWF20fNAwAxKZICoyOJTcIIVAuCh8oFy5cu3atatfv/5DDz109OhRlYHXaNasWYVwDho0iNerkBAY1CeffCJDWFiNbK+1bIIhBj3417/+FR8fL36J0qVLJ6cNhYtWq1aN/7awgaapw0X8UMW2b99+//79KHCTJk0khcxwLaZHkSp37txDhw5Vrms8pIX3dunSpXjx4vClefPmQURJ1N/+EjQSavfcc8+dPXt25MiREAaf7XeXoo4dO2bZ1gUtJr52fLYvVrUw6BcwIpoU7iElc68j+A3zDHwY5jNgwAD4KtVUJIoXAXxJWBbk548//li2bNldd90ltYN0CafVxSYFciiRV0GnTp1++OGHEMuBbcKZhfAjJzpAmXXr1v3www+hl0H7dN++fTly5PDZi+RUiobt27cvJNlnx+FUIVXB9OnT8+fP36BBA3gvZfbs2VMWwy2bIQslzps3r/A6deSSQpSCOeDRKXPmzJHPAdR04MCBNP6iRYtocGmx3r17X7582UNnDh8+7FaDUISkiUqXLk1+BIAGN2/eXPX71q1b6QgeYbiowU0M1Bvyqcgkc7i+vMmMrf61fv16mV0te9K7ebioRLbZuHEjNWdakSOzEjuV6VVfKT5w4IBcShv99NNPmzdvVpU3XDSlgTciLxKoAl0zc+ZMJvoNGzboGfxyUQzuqVOn8l6cNWuW0njBpUuX5s+fL3YMxgdGg8+OesfLlVe45OHNrW8DQ4bFixfv2LGDezFoeLWrvT0Kv/zyy+jRo3nR8soPupNWwr6XL1+eh4q/CsVFedby5ct5hAp97hZbcOTIkVGjRg0fPpz8P/74o/cTLftk+cSJE998803axEEFT58+vWDBgn79+k2YMEF2TSicO3eO1/Dvv/+OYNSdCqpTMViHVPm///2vPmqC9pdfLopJRM6xY8eqeMcC5jUEs+xxSk2nTZsmOxfOnz9Pj9BK+ndo1Sz0HXVZsmSJvm6DPFSf6mD2UU3dlt2zZ4/4NUEGeoQSJB3TihZGi0jUBcZEW716NSKhJ2PGjMGsUeWItJZteWOTidEGeOjHCZg9e7ZMPpBDSQk9DF0gkUIBtcP698hAz1Jsnjx57rjjDhFM32cYqI+oC7WmL9CE7du3q3SHkjO4pEwsWsueh+VShfiz7M0pNA4/mIrpbrVLJVCfBkIEOnBLQe3RZaaiy9QZHh20EjOeIgyMa9Q7qMsxVFrntCi2ikWp9uhir6ADjmk5kfCQVvgAg2Xnzp2y5OUAk5VaqvUAes4jTp06FaJIaC9t62ChOs6cOUOBQQ9vB0KIYgcFEiKnjDW6xl2mR59adi3ozRB90TEwQ9Gi0BFup+iITMM9IH1NAzLXuZfNsVE9lMHA4KYBky2mEa8V92hihmG08iJW4y7ZEWUuKnFsZC+ylUBNhTBgTn2p+WtiOtD3NJMu23oNF02BwKDMmTMnFsy7775bqlSpypUryzdXfc+Vm4tiE1erVg3DGqO5Q4cOWbNmFU8SsmNQvobK93h0Q5zst2nTBqLFmwnb9MUXX0yTJg0sQkrDBC9evLjI8PDDDz/55JMFChRIlSqVHjDtk08+KV26NO/sLVu25MuXj/+WLFnScfBJgZc3ViAFQgx4qLAp4aJdu3atW7du06ZNK1WqpDY1ucUGvP6LFi2KdcWQ7t27tx7Q3C/ef//9Bg0afPPNNwhZzIY6I75mzZp77rln6dKlpJAtffr0PXr0EAt+ypQpt99+O8/Fgm/cuHG7du3Kli1L7Rg1Q4YMQc4XXniB/MrPUyj95eCi2EDNmjXjQTC6J554ImPGjELn6LvmzZuTs379+rCaJk2aPPvsszyaH9Sdv+3bt69YsSIZ4BuqcDqa7vviiy9o4WzZstWqVUu+C8CZM2XKRGbIT82aNelEHpQrVy4Z77QqjcN/ISf0iBhew4YNK1y4MMYrHL5GjRrURWZPRJVP5rRV1apVY2JiaMyNGzfScT7tdBZS0UE0zjwbTMHiMjRz5szKcmKmRj+feuqpEOflQCKFCHpZD9TuBswfUXPnzk3LiNhCOwP1kWVvvEHV0U/aGRrJwJFzYm4lv3TpUqdOnXwJB65oEIYbRcF7pbsZg6lTp2bUUE1k8CUcaAzUp4EQmQ7cUvDru+h6w+95UQMDAwMDg+RClLmoLPKqr3cnTpyQ/bpYexhSXKp4GNglQjv1o6EYRoaLpkz07dsXC6ZVq1byTRGbNU+ePKSoNUwHF4VTYdGqrxLg0UcfJUXlF3cLitSJhaTv0UVnChUqpLioZZ/nIQ9kQ74Hy15HbFn577lz5zB5JVy7lRDN/IMPPvCoFLf4ro11JlwUtiALNSgkDAfeojI4xIaJQQ7lN7xROR3xCwZCwYIFlesI8cEgG6jgErGxsTNmzFCZ5b9UWS5fffVVLrt16ybs9MiRI1xiwauVYTkLpHa3Bu0vBxdt27atRNWz7LEJW8iRI4cs1Egr8SwaXGX22R4mZKcTGSB7qhn37dtHA6pNUP369fNpriYef/xxLl9//XX5VjdhwgQux48fL/8V61zVAv6PAqA5comE/BfSLpcSrrBRo0Zk+/HHH8V1hzgU0T2FQMN0tytA9tHpQZwfeOABfe3RA94iBYX4zAwlfjSKh/7rKR59JI2sOheWTo3kt1vJxTOK7vwjLi5OuKiUnCpVKrRx9erV6Co6efLkSe8+dSMxOnDrwHBRAwMDAwODKHNRYZJqX8SpU6ckxbFugD0th2uxpPXlY8NFUyyEGmHHqJQRI0aQooJnOLgolmi5cuX0EuhWnx17Wi7F950HF7VsrwM6FxWXesrpH8iYMWPlypXlt7iIUCX873//87lc2DsQiIvq50XFXT7muF+xKR8ZVK29ne6ULVu2Z8+e6hJDH8Is+wLE4b6u9sgG2YBdywBxLzvzL+WL30ogRSoAXdD+0rnowYMHZWfs+wkQJ5NffPGFZKYX6AtV1KhRo/RnWTb5UcJAyOkUVVTHjh19mrMK8e6odiBv2bLFp7nTcHBRyybVagPwkiVLfAmR6K2EbxOym1RB/Kx4c1Hxn4Ekckn1HYEZvOEhUlAMHjy4TJkyoeR0cFHvPoKF0nTqTEiFChXoEfntVnJxVqkzSfpOcVEAxS1ZsqQujHefupEYHbh1ACGk4gzVpHyorJOredjAwMDAwCB5EU0uitEsTFK5bse2dnPRv/76S47Vfv31145dXoaLpli4uY04DGzYsKFc6mSJLk6dOrXDvifRZ3uul8uocNEsWbKoo3cHDhzwae7gr169yr3eBm4oXFT8BKpIbg6x4QDwHFKaN2+uHDD6xfnz52NiYtyhxgWY6fzXcQavatWqlCz7M91cFPKgc1FpHLUOHLS/dC4qhGr58uWOM+tqg4ODi9IFDi6KJLlz55bfEKFmzZo5ilIt5uAhEvAAHiWXbi4q2L1794ABA1q0aOHTIkkIF1VBCwShcFHL/laSPn16+WpG206aNMkKE35FCory5cvrO6XB4sWL52lQ+0QcXDRoH1n2EJsxYwbl57MhiZFxUcfOdu8+dSNiHTh9+rTeGroC30w4c+bM66+/nidPHmaw4sWLM+E4zodfJ4wdO7ZMmTI8NGfOnF27dl21alUSPNTAwMDAwMADUV4XFS+4yh0CpJRL/UQfpoYcCt26dase50pguGiKhZvbyMIjtrhc6mQJBeB3XFycoxDoSrZs2eR31LkoqFatWqZMmYS8rV+/nv86/Ls4kHguatnOGJVfxJkzZwZ6lhjcgwYN8vtfCbPmiC8sBzXFD02IXNQRKc6jv3QuKkumDqfWOkLhoorMxMbGtmzZMlBR4XLRkydPUlr//v2ZLkRJosJFZ82a5Us4QFu5cuWwIs55iOSNffv2qQ5VoN3SaVDbdx1cNGgfLViwoG7duuLRiipHl4t696kbEesAjaO3hmOXsoGBgYGBgcFNhihzUfGFqwx3CWWzceNGuTx+/PjatWtJwd7y64bRcNEUCze3kXXIAQMGyKWDLME506dP73AxSiJ0UX5fDy6K2V27du0qVar06NGjQ4cOQZcaEs9FZRXrr7/+GjZsWIYMGWJiYtShSgckBroer1wgZ18bNWrEf5UnWEHjxo1Tp04tn2wSz0Ud/aVzUYl3pzesQPGisLho8eLF8+TJ4xjgp06dku0SYXFR+HPhwoU7duwol1Hkokw1lAzp2rJliwo6Hwq8RfIGnUjjhPggBxf17qORI0emSZNGfcuIOhf17lM3EqMDBgYGBgYGBrcOosxFMYxgktgWcsht+/btXO7atcuyHedKxFEuL2vQ7RXDRVMs3Nxm/vz5mL9qocZBllq1asXl3LlzVf4TJ06QMnr0aLl0kLrly5f7XN5QwuWiPG7ixImhVwqddPCWcLmoHnFbTHwPFyxywE+CxwggrlIdxPbZAf30/KVKlXrsscfkd+K5qKO/dC4q23f1OO+W7WlJ7VwNi4s2a9bMd63PXoY5VZOoCd48pEePHnrzSrOoIOYLFiyIgItWqlRJ1yIFiaJetGjRL7UIWjB/b6e43iJ5o0KFCuhPKDktFxf17qP8+fPffvvtKr1s2bKKi7qVfM2aNaTokjhud3NR7z51IzE6YGBgYGBgYHDrIMpc9MyZM7Ly+Z0NIZay8qMCijqgx9EyXDTFQriNWlXD4sfEV05rAfyNDIsXL5bL33//PXv27Pfdd5+K5dW7d++KFSsq15rizkR5x/n++++5bNCgAdbq6tWrJbFMmTIkqlskwPfIkSPlknTIlfKQhI3OZefOnWfOnLls2bJ169bFx8cHDbYRGxuL1f7HH39gEPN31apVPs3Bj5Xg81NROIfYTZo0gb7K70OHDvGvLVu2BHqW7AtFyG7dukHkeEqdOnWEDf7zzz9Vq1aFWqsHQRiyZs2q4oaLJ1LVvJa9yAyFUJfiu2jEiBFyGbS//v3vf5NB+bWWWOolS5bkRtqf3nzkkUek9a5evZoqVary5cure8V3kU77ixQpQkvK723btkl8+bZt2yLwnDlzatSooRj4008/zb+UkyfxOEWvyaXsRIV407k0shA/aPAvv/xCg4iQPXv2FBojmXXnw5a9gdZ3rVudhg0bCr89deqUiill2avZBQoUQHLlPo2n0AW5c+d2bJbW4S2SB8TBrzsibiDkypWLEaSnePQRmsC/PvroI5SQ3uHetGnTHj16VPTHoeRHjhyhQ6k7rUH+119/vWDBgiKbNAX5Heu33n3qRmJ0wMDAwMDAwODWQZS5qGWfEZX1zy/taC7KtYY4zjVc9AaFcJtGjRpBn7C8H3zwwSFDhsi/Ll++PG7cOLGGq1WrpuJM/vrrr2SuXLnyu+++C4Vr166duKqC/4wdO1YCZtaqVUssVCFjpBQqVAgFgJIJ+wLc+OOPP27YsEHiWJYqVWrhwoUnTpxo3749l1jVlI8MFC78SgcGtwp04RcY4mSD1w0bNgwaKdE+8uTJM3nyZLSRWkssRBjp9u3b3WI3b94cMjx69GisbYgBNMC7GSdNmsSzRDZ47PHjx9W/kP+ll16688474Rh9+vShqWlA+dfs2bMltiriYbjDJSSCC4DhQ8Kh0NI4pUuXFr7q0V/kh6NCiX12aIetW7da9mbjFi1apE6dmkT+0uZyhJKOEB+/UIuRI0eePn2a/i1btiwpVJzfEDzVUzxIVu2WLVuWN29eSaRGioTMnDlTAp/Wr18fIkSTIhiXKI+Eyjx8+LC0MGpDNZGhQoUKXGbIkAHqzrMkvivVnzJlSrFixUQfPvzwQ1lwo3FatmxJYrp06YYOHSquiRAmtQ13BNFOnTrpa+DwSQnE6uHa1EMk766n/dHGUGK40yPS5qBDhw4Sq8ajjyz7S4R0aJkyZaCU9C+/odmyY1xXciWMcMW4uDjy165du3z58oMHD4YfyqKlLFSKbggC9WkgRKwDBgYGBgYGBrcOos9FLXshBYaJlRZWCHiDlAy15xODGH4SikktuHjxIgaxWtv0ANpCyX4PEocCaFLbtm337dv3/ffff/7559CkWbNmvfbaa/Ax7xsPHDigFm/DhVAgHh0fHx9iITQdQspmATdoKJorYnkUIusvngsfc5zyjRgHDx709i3sF+fPn1ck3LInExpE+Tnjv7rn2BAB51eBpnTA7fVnWXYLDB8+3NutbmQiHTp0SK1yJwaB+ujPP/+UoLgC6qVPv24lJ//+/ftFMfQPgt4It08j0wEDAwMDAwODWwTXhYsa3Hxwnz9MUcCkrl69ul8K0a1bt6SXJ9mRwvsrJWD79u3qOK4CrOyZZ56JFhs3MDAwMDAwMDDwgOGiBiFBuI3af5vScOTIEcRr2bLl5cuXVeKFCxfefvvtr7/+OhkFSy6k8P5KRtAm/fv3X7x4cYUKFfQ9qILhw4efP38+WQQzMAgX6Oq5YFBBvP/3v/9NmzbNHUrtemDnzp3z589PggeFjn379s2ZM2fgwIHjx4/nfZH4Ag8fPqwH8bp48eIHH3wQyI96EiDZBYgA//zzD32xceNGJPe7dcUB2nzu3Ln64Xx3yg2KY8eOrV69euTIkboNExnCbdWIn3Lw4MFPbVynRxjcOjBc1CAkPPvss3Cbfv36JbcgAdG2bVs5FFenTp1GjRpVrVq1YcOGuq+aWwopv7+SC3I60Xett2QDgxsO2ILqYPxtt92WI0cOOTOcPn16fvNX/lWsWDEM01atWslJ49D3Y0eGSZMmxcXF8SBm4Ov6oNDx999/d+/evXPnzjCWxYsX01aZM2eGmkZc4Nq1a6tUqSLeDVTi5MmTSeHtEw2RI0GyCxABfv75Z/F6mDFjRuWU+8CBA7Vq1Vq5cqUj83vvvdeiRQvxdQ/L8puSQjBo0KAnnngi9ANH69atoyLUokSJEol/ut9WjTpo8PLly/OUd9555zo9wuDWgeGiBsHBS+6tBIwZM0Z5TElp2LVrF+JBwGbNmrVz587kFifZcKP0V7Lg0KFDw4cPX7ZsWXILYmCQKEi0nm7duil6Kd9ZXnzxRbk8evQoFFSi+0Bcc+fOnQRc1EqIjJVyuChNpDO0zz77rHjx4ol8QWDuO7jowYMHGzdunIyrwckuQGS4cOFCTEyM3kHTp0+XXU56NupVsGDBS5cunT9/vlixYpMmTXKnJLnsASF+9ZRX/FAgGqUGbyLhbtXrgZ49eyKzt3tIA4NQYLiogYGBgYHBDYY///yzVKlSulsyBxe17GBOKjzPnXfemTRcVKzqFMJFjx07li5duuHDh0e3WIljrHNRg8iwcuVKWnLw4MEq5dy5c6NGjTpw4IBKgXDS1PpOFndKMuLUqVOOMGDr16+fMmVKWIWMHz/ed21I9sTA3aqJx99//x0fH6+nVKlSJVeuXKF7sjQwCATDRQ0MDAwMDG4w/PHHH0OHDtVT3FwU9OjRQ37cmlx03rx5CIOhH91iDReNFl555RVfsMDLM2fOJI9+vN+dklw4efJkuXLlwloC9YtmzZpRIwZ1VKQKpVXDwtWrV1u3bv3hhx+qlLNnz6ZOnbp58+bReoRBFHH06FFGx7p16/jrcGV/+fLln376adOmTV999dW2bdv0fXOnT5/+4YcfvrLBj0DhHq4HDBc1MDAwMDC44eGXiyooLoot8vXXX0PPtmzZ4s62f/9+DP3p06dHfKLSwUXj4+M3JUA/wI8Rv3jx4gkTJnz77bdqaYXfKvOuXbsk8dChQ5ISVlQkrGduefnllxGmV69eqthVq1ZRuy+++ELPzCO+/PJLkWrOnDkff/yx+2gDBWKfIfCKFSsuXLjg5qJnzpyh8HCLtezTJZMmTZo7d66+GBgB3ALQsNijFP75558fP3484sjttDzCf/DBB+vXr49urL677747S5Ys3lHfHnnkkdtuu01/rjslWUB/IX+RIkUSWQ7dlCtXrnvuuScqUlmhtWroOH/+/JNPPonC6wPw008/JeWjjz6KyiMMogjI55c2GK3yQ8WuY/Jn2idl7dq1zAz84K9MSkwOJOp3qX8lAQwXNTAwMDAwuOERCheFjJUoUaJkyZIZMmTgctSoUSrDX3/91aVLl44dO44bN65Zs2YxMTF9+vSJQAwHF/3999+rVatWtGjRWbNmqeUjmHCLFi3ee++9V155JW3atA0aNJBv8FDEHDlycHvTpk0VGT527BimcJkyZX755ZfQxaA6r732GmJQ2n/+85/XbHTu3FnO8nXo0EGyrVy5EvFIeeKJJ5CwYMGCBQoU4LJ06dJ6SN6jR49WrlwZZouEY8eOpUCdi3722WcInD59ejhAWMVCQtq3b0/1sQLffPNNMkBsKPzhhx8Oi3i7BZAWqFWrFp24d+/e+fPnQ04i2AKKhF27dqVYDNM1a9bwgzITY6GeOnUKNXvuuee6d+8uR0NVDPAFCxa0bdu2SpUq1atXt+x+/48NNCRTpkz8qFGjBv/SU4DSiqtXr6JR7dq1o5B777139+7dln2smv5q0qQJaj9lypRLly699NJL2bNn51ked6GoAwcO5C709vvvvydlzJgx9CCFqE8kr776qngIu/322xFj6dKlqHrfvn2pDnc5nNjz3P79+7/wwgtvvfUWebp165Y/f371CWb79u2Uw1i4Hq2qsGLFiueff75Hjx5ly5ZV1adeCI9+Ih4shc6lUsim9hjPmDFDjpqnTp2anGrfr3zlES1Fw5leKCSCsAUbNmxAJAYLUnFJCRR1//33q8aJj49njPTq1atixYq9e/eOqHluIaDPtCFMUuKNM3EJq5QPNwcOHOBy69atTA7k3LZtG5llBKGE/Gvnzp20POr61VdfcZn4Bf8QYbiogYGBgYHBDY9QuCi0R7Zs/fTTT2nSpMmWLZuKIfHGG28MGDBA5Yd6kX/evHnhiuHgoljGmMU6e1m9erXuVUU8oChy+M4773AJU9XLbNy48cKFC8OVBIhD0ffff1+lTJ06lRQsaZXyySefkHLHHXcMGTIE+wxTTDZMTpw4UTJgmRUvXhxKpm6Rrb+Ki548eVJ2jepUMGixYPTo0br3lzZt2nCJaU5KWFGO/QrwwQcf8HRl048cOXLatGmhlylYvHgxxb777rtyifCO9gwL6MZdd901Z84cuaxbt66jNIlGpjaWAwgwKSiJRwo4fvx47dq1YWL/2MiYMaPOW8TN/r59+zp37vzEE0/wW1Q90F1Y6pjmMTEx8E8uSaTicEh1o+Cjjz4iRfE6yz5UmSNHDmjb2bNnVeKff/4JhYa7yiXVz5AhA8qgMowYMYJyli9fHlGjBm9Vxjjay/xw5swZLqGUDzzwgPovMwb5hw4dKiHNYKRwdaqwf/9+ycAPMnTq1El/aJkyZeLi4vgBO+Ve6Ch54LoRyA+H595WrVpBjVq2bJk3b97bbrtNok+hsSVLlpSYPW+//TZSmejf3jh16pQse4obZ7RaWCWqzuXGjRv57XcrOAR1/fr16l87duwgp3yaSQIYLmqQsiBzpQeS4LyTX3gIxusnqNhJDCYg/V3oBhNWkglzA+F6uGG4cuWKx9a7pIn36BcpTWkNEolQuKhYJIJ//etfpMhHcaw9sT6vJGDQoEH8t379+uGKoXNRaFi3bt304BbMlgULFpw0aZJ60Ndff03+zJkzSzbUMkuWLOnSpTt69Kjccvr06fz580cWd9HNRT/++GMHF4X4kfLQQw+pFMx6PQ+mNpf6sSuEdOzR5b8OKhi0WFCxYkWaXU07sHQyRHYGzy3AK6+8ApvCvpdL+GoEXxZWrlwJMVi0aJFcipPkLl26RCAh1m3OnDlhFCpFQuOoDYQArkgKbFOlQHV818bKdqeg1WhI48aN5VLIqpIZNGzYEIYD8+dftDZ0Cz30votxIZ9Ixo8fv2HDBivBvdD06dNVsS1atKCF9Z3PvFjJozM9LBbYFARYpSxbtow8EyZMUCmPPPJImjRpIlttDtqq1BfyWaRIEbGdkJDxpfdgrVq1qAWNo1JoE0qAXsolonK5ePFileHYsWPSOHBFlNZKUN3IdlJ8//333Dts2LCnnnqKSeDw4cOy3MoUlDZtWjlKQC3g81HcxnyzgtaDQ27atEmlyKZc9BljQzbfMqPu3bsXzdm3b5/fqD8QfllcTTJD0XBRgxQBzJfXX3+9XLlyTZo08ZuB4cSblRct9lNSCsaLHNOBedzDZR/vOd7WupGXjFi3bh3GaL58+caMGRMoj3yFdWwiSkZs3rwZmR8MDP1QCsYrl7KfJ1rYvXt3o0aNnnnmGd7BTZs2xWgLlJPZHOvcLSEmlCMn79SZM2fWq1evbdu22Dd+WS5mTY4cOaJYkVAQikob3IgI8byoSnn44YeVA5gPPvgAe/RhFxgU4YohXLRy5codO3Z0C8NYE6bqfhYGruR57bXXyMMbQS4Z75GRHyscLoq9rlJWrFhBCpaxXMIlcuXKpRfr9l0Ec/bLRT2KBRAk3WONFOJYEw4RbgHkRF9sbOyoUaMSc3RQ3bt//35ZQ4tg+YtCKlSoULp0af3DBLMfbatnK1WqVMaMGfUvdMKL9JUcdwqvYEiLbEpEyAIFCqC3asrliTyI0dG9e3f9Wd53MSJ8dvDMyZMnS8pzzz1HCra+KiF37twVK1bUy5w7dy55+vfvr1JoMXim/jny3XffJY9K4Y2WOXNmnb6GjlBadfjw4Txu9uzZlu2jGIUsX7684s9QkQwZMuTJk0dv83//+9/couIDQaRTp06tf7uURXi4ohRrJYxZx3HlEIF+yicYfRM+VgEPbdeunWUT0d69e2fLlk32Sxt4gDaEQ+q+AJjhZbctve84Rwo2bNjgoKPfffedHBwN65hAImG4qEGKAINBdjQ9/vjjfjNcvHhRPp/ff//9SSnYhQsX3n77bZ7rYbgzSyIVOZNSsEBguunRowcCe3BRqBFvL92PSLKDV2nx4sURm1fauQRgbSBkrVq1lA2xePHi1q1bkw3yH61H//TTT5kyZVKeNnv27Km/qh2YMWMGT4+Li7tXQ7p06d544w09G7N/mTJlsH50w8WBX3/9FTMx6bloKCptcCMiMi767bff8rtDhw78jsr+N+GiRYoUQb2zZ8/u2BQgu1tXrlzpUQK0ijHFvefPn5d6bd++PTJhEs9FL1++jE3soEzR4qKPPfYYKYrtyALR2LFjI6ipWwDQq1cvn41y5cpt3LgxgmIFGK8wsdGjRy9dupTS+B1uCbL1WlEXyz665lhiPXLkCCl169bVb8yXL5/sBQ2UInPy008/ffLkyWHDhtFT0Eidm2GXkwG6Rfmh30XXpE+fvmPHjioFlea9qS537tzps91i6bK98MILJH7zzTdyyY+YmBgS9TyVK1fWNYd+iXg2Dtqq+/btoxbFihXDgoIn81biDatPAvSsz3VUFdYnW5qtBL9KyKxnePbZZx138R6E0+pnoUNH/fr1Ge/6xmw6Quar/fv3Y/jVrl27WbNme/bsURlef/11/RXscEV2K8PNRTGihIueOXNG+CcpTK2ogSx+Og6F/vjjjxBUOWUasbezcBF9Lgqp2LVr1wYbjFX93Xbp0qX4+HjSqSEt9dtvv+kfrhhCjFvo+KZNm2iaZPeQZpDEYGB4cFFB2rRpk5iLWgm7km4gw11YvQcXTZmoV6+eX7H37t2r3qzy7bZw4cJR5KI1a9bkVa0umbIyZswYaB2mVatWDtsawoypqn+vXbVqFeQWTfbY8cuM16hRo0qVKiU9F7USrdKRbcQyuN5IDBeVTzxYIYkXQ+3RlTWi8uXL6xaqHLELOjvJGhTk5/fff7/vvvsiFibxXFQOs2XNmlUvNlpc9PDhw3fddVfu3Lk3b97M5IaJ37BhQ50RhQ6/XNSy3RqJu6ZUqVIp0hs6qCkaRW+KVSpTR7hcFLMQehMbG6sbhBJ3RP8qgXikjBgxQqVI48MYPVIeeOABWUzu27fvmjVr3KceBgwY4OjxoHf9/fff9Dg0Un0EgZiRXz8zPHLkSMd2Yst+N1FT1YO8Bcijf/aVzw26DgwcOJAUrGK/TeeBUFq1d+/eXFarVq1nz57z5893U4t+/fqRQf9OIY6U1Hnvbdu2celwGoTm0zgq3OipU6dkV0W4VbDsdzovXAizHqNV9kvzlO7du0+cONHttKxXr14tNXh8873VIE503Xt0Dx48qNZF1Z4CjCuhpo5C0H9xZZRkC9FR5qIQSJpA9xfMpQxyBidUUxpCjtLqdBydlhSh6eLoyYTQvaUQChdNly6d4aJBcYNyUbGM/YrteBWVLl06Wlx0165d7i1n2PQYIu6Fbgnq4EicMGGC7tOflyL3kuIdm2vQoEFYBo8++ugNx0Ux5WHaURfJIPFIDBcVzuZ2U4lFIo5DQod+XvSll17id5s2bdR/ebn7rj1QJ8BOWrZsmbqUrbyMo3fffVc/yRYuEs9FxaWN79pjjdHiopZ93q927dqQnB49enz66acR19QtgLIjIS3ipDdPnjzhmlWy91JFqoyMi0qn16tXT6UwPWbJkiVDhgw6j4JUkG3nzp0qZdGiRb5rj1Y6UqgONAaa7XHwXmgnZrdKCXrXhg0bfLYzZ5UiW3Z15tygQQMK0eUXzdfPGTFVZs+eXS+Zu3zXhkKpWbMmCub32J43QmlVcfjsIMw6qlevnjNnTv3zR/PmzdOkSYNayqVs8cWk96imbHYYN25cuFWwEminY1+67NwxXnMjwPHjx2UXrkqRRU7mh8uXLwu9kv0mlr0TQdiWZQegAuq74bFjx4TKJQ0RizIXlVOzGzdupM7wUqHj4oxLPAsDsfDEszAgJ8NGfst3kT///NPB3Q1SAnixvfPOO2PHjv36668doeewV/773/8OHTpUbU0RbNu2TVzMYc0wo02bNk0c6jASFi9e3L9//88//1xlVlwUzWEADBw4EGPdMUG7uSgjZ/bs2X379qXwUCLzMo2OGjWK/Fgk7g1pCExFBgwYoB97UIY7wixfvhyxlcM6Ae8zRJVjJwoM8g8//LBfv35LliyRiR6b7+MEKPNOgs7pXgECNSYFIjnNiAzeyxeKi9LaCxcuhPboLxIrwbWa+GMQMEjFh3t8fDzGH6abY7NNoHajqNWrV1MdRitP5EFMgqqairkhBpdLly71ENsvF8UGcjSsFVUuKt+2sTP0RDG/9E7xQJ06dfStSryhZT3H4xamftm1FToXRbcZSqgTRpiDGzBhTpw4EVP+xIkT/BfNcbeYA0FV2vKnwJZ9Ag1Dh2Eo/at2r/jNbNnDc/r06SgM1ILZQ80bf//9N0MMUUeMGKG/NQ0SAznl1bZtW7//9eaijFx+Y4NKPEzBb7/91qxZs3BtEZ2LMjdWqFBB33cq5rLPPmymbkEPMUb1LZRWwlDClPc4vx0UUTkvKga9viZGLUgRJ6uCyLgoY9l7A0XocAvQrVs33YgSJ73h+jUoWbKkzkWlCuGeIublojNYpggak5RatWpZGmfOly9f/vz5+bFp0yaZRl5//XXHcr0jhZmE6Qi91XfS8VuVeebMmdSpUztOdQa9S9RGf2HBS7mFCY3xgkJSQmxsbO3atS07EJHkER8/zIQURYuJH6MSJUqoQqCgNB2Je/bsQdsx95kbKVaUhCkxLPdFobQqEjqYpGW/VeUH1njatGn1BQAaNiYmhplcpTBLCFXG8BP/YYwm37UetuWT06+//rrPRuhVAN27d+de/TuUlbBWjL2hJzKgImDstxpoIiFQMtVjBOrMC+0VP0aWbbzJ4qdYFLJYqDZCkyinSZNG7ChzUTkjqxYxhJqK3qOg+lowQ1q1FwNb+Lc6Ii9+h8MKJmZwXQHTY4LjbUd/6TGmLDvKFpcYlDJ9YMdbNrdp3ry5z3bD2KdPH6yKZ599NlWqVPyA7fC3ffv2vB58mgcd4aKNGzd+7LHHihUrljlzZp/tAEN35OXgogwk3hDMYrwgy5UrV7hwYe9P+MOGDSPPgQMHsLFq1KhB4epVhO5BDzBQEI9XC2+vRx55RF6HYrgzy9etW5fHVapUyZdwSoRhT62zZs3qswP3qQfNmjXrxRdfpBwM8WzZstF0TATM4+J0AZtAqTpVwLhXG4H8NqZlU8SiRYvu3LkTgXv37q37ZnRDuOibb76J9XnXXXdRFy7FB4DIJuaFeN7DqOrUqROXZIaYUUcqzqW8Zb3bjXdhkSJFxNTD9OQdRsfx7pfv0PS7oiVoDtX0ptB+uSgvWvdSpDcX5aFXAsPhwwO7kIc6wu4NGTLEd23oxUBg7qJ51QYnLD/sG9phxowZDRo0oPGplIPmoQk0snyUCZGLrlmz5p577pH4dTR1+vTpe/ToIW0L6c2UKRPSYmHXrFnzySefxG7IlSuX9zEPD5UW+FVg0hmt6CECzLMhjek3MzM8iiqsY+HChXFxccpsQpHQEJSN6jBy8+bNSyuZL4+JB13jWCfRkSdPHp/mMcVK8KOrLGlmFZ/tz7Z169ZY1W+88Qa9FsFBTdlroDxe8uqnTIYJg0JSxA8qoN8ZZe+++y6z99SpU/2WE8ibXYgQ6/ydd95RKVAFByGUI3NqU6KVcJhQRd3AbuHlRQqSM+QZXHK8lkTmK1kvFWmZJ0Mv1rKpAqO1c+fOw4cPHz9+PEPp888/D+WjqhtuAXid8RZQl7xNKlSoEG6x4pQVuiJBSuWA63333QfV8XAP7oCsfRUvXpyqMTm88sorFOWz1/CZi5i7yHPixAmfHY5127Zt9JHcSPvkzJlT5+p+U3y2F1a53LFjB9RI+cFi8lEvOx3edzE0oJo688mdO/e99977888/i18iOeTJnInwisFi1ZBIR5AHPeF1g8Xis/fo8pv+XbBgARXkVYjFz/uRWsg3ILgfxrN7CCS+VcWQoNekLjQyNoZ6YcmXBWXOYbbxQqetVPNitPB+4Y1Pp8ycOVMSGZIOV0ZlypShU44fP678jYUOxr6jqS07yiiCYU5Ij8DYeV/owZAMPCDhWNABLC7ZhaqcafPOFeZFHuGlQL6AMI+pTankl98qrs/1RpS5qFRbuWJH79UiL7YXl0p9GTlSVdLRM/6lvn2SWdaUg37dN0gylCpVSpnmv/zyi/pexbtT/0SKNaxYGfrNb160am+MxPgiv5iwZMCoVWcMhIvefvvt8p3+0qVLQop05wE6F2Xyuvvuu9W+qXXr1jk+QjtAfm7H+pdLiTKn9q7w8tCNHrL5EjYLieGOaSUKifBClVVmOWqluCi2F5kV55HzGPIu5OWN+aLvT6NwnSUGakxecsr1PCQEYh+omlYCF8UGko0GiC1GqnKLJ0e29NczLxL6Qrmzb9GihXy7Ddpu4hujUaNGZGPikwhp0hfwIlX+6tWraSUPma0ELlqxYkU5AdK8eXOxlcPlokIvA0F3PmElHFL97LPP9ETZjhVK5HFsJqiUenNLjDX4GHYAmkk7CM3TPzPTlSogeChclE7kVa3seCshBJ8i7XIkCSNAxJBv88oVk194q7SHAlu2jwq98b0zS4xKYQKyno/2MoT1TdFygMp7c76BN95777369euLhsfExDB+dbv28OHDzKLy3zp16qCWWHg9evQgJymMMlFIJuRWrVrJpytQvXr1CIjo9OnTZXlWLPVdNhh0IhhzAnY5iopKoEWSDfNXj9CoAzLsvZnCAzyFMXLHHXf47AVMWZidMmUK7zKh3GgptgdjgZqKeLwF/vjjj2XLlt11112kYIUjpwwrDJJChQqJwPxgWmYm53Uzbdo02o3hKdO1zw7DyJQVYrHcrtpBIUuWLOGGmnQLQGKXLl0gKnT9vHnzIKL0SwSR67Hf5GMrYg8aNAhOJW8TSgs9vhqVFf2kskwX6IAcv+RSLVnzxucR8DTFn7mLR+svDneKZa/DS5+iSMxO3K7vvBWrw/2R2uMu6kXn6p8MLNsEIvMLL7wgc534KM6ePbu+fUaIHxVUj5PPLugATxEPQzJd83YT9iWnMSG6Q4YMCbExw2pVNLxhw4Yk8oovX748L0f9WKYcLiUDcwJvPV7Bjt28p06dSpMmDa2hTD5xSlylShU9myg2NDtc30Vy+tdvECNGDc/NmDEjZl7dunV1ZzwG3kBFFZmUJUA9IBYvffWv9evXq+8vqNPu3bu/1IAaR3Z2PQJEmYtKBSCWcilBV4HDERHVE+K+efNm9+6UgwcPCoM1MW1TDnillShRQu2+UF9ZeC0xu72fAPmyrt4ljmVM8dwtn+sETNB33nmn/BYuCqtR/z1y5AiGEYUoS1cvkLc4c6J6tAQNZ970ODfCfKp2BS9ZsoT8YrExGnmQfhSER8MrRDndh+skWLb6eiJbOhUXhShigivBxArELpH/Srhz9a567rnnQmlMbHcm5RUrVjja3y+Ei44cOVKlSFw7tdQpX0N1LkovYLSpS/HOpxhaoHYDWHu+a/34CTBwaVL1OQmOre/H9gvhorwdN9nYsGEDXQDTC5eLbty4cXpgOE5koW8+bWlIMGnSJF/gc3c66CP9W4mcctG/DZ8+fRomid5KcEJaT/e4GwoXxaCkTH2dE9sXow3GK/opURaURonTSId3Rwe8VdpbgR1c1DuzGF7qbWclHPdauHChLo+wF3dHGyQ9eO0yvSTBMjVmQHx8/K+//hpohyo6zwsiMcFIog4mNFkoQGZdqyMGM/OIESN4sUIGYN1MpBMnTuzcubPbBVEEEGJAh+7cuTP0NUw3mHAw2JQVB4nas2dPuPuKyb9r164ff/xR3xOk1i0EXOqHcuXMsL6vxJ0ioEwpPKwgtGHddeHCBUcbcq9j97hsenRYIOgMZEB5Hzh79iw36hlkw1HoYjueGLRVLduo3rp1qzvkOAwWOk2Hfv/994ECeCB/0C2KaMj12MYIg+B1FpWBdguCgc80fv78efdQRVtoWyZYt49Y7jppI4n5VzS5KBV2nPNUJz/1CqP3Qtm//vprh3cQSpCtvBBRRWgNUgJksSV9+vRQI/XpS+J9Dx48+MtrocxiBxeVYwY6F4UC5c6dW3779V0kG4TUyqpeYLdu3eLi4r50IegQ4n02YMAAWfqTvUDLly/3XevbQIfbcJeVN+W6zcFFK1SoAOF0SKX+K2uGcvSIaeLBBx8MpTEx0+XzefPmzYO+t9y+i3g7kgKvk8ugXFRW3hy0zd1uVgIX5Yl+ZZClRZ6OaRXUdvG7R3f48OHhctGwIB+G9ajoVkL1HWFa3GA2h2/rPBbS7nOFZJADQgsWLOCdWq9ePd3uCYWLwutiYmIcnyerVq3qs/3dWy4uKqfUvBd1vVXaW4EdXNQ7s3BRff1EfKh8qR1KBDS1z/bnAXWfpyExrlwMbnQMHTpUP1N682H+/PnFihXzOzFGEDTl5sO4cePy5MmjL7W5UwwiBnzD8fXfwCC5EOV1UfGCqz5jQEq/tGPUqAyYGrL/duvWrY6vR1xKGBwKCX3vh0GSQQ6D+exN/EIPZHOdoiVuhMJFFQXyy0Xl0Kn6YqcX2LBhw3z58oVVBSbfli1b9u/fH2WTPTYivHCPQKe0w+WisbGxPMVDjLJly8JAkGHy5MnqCETQxvz222/VFi91csMv/PrRhfMrd6/hctFA7WYF5qIYWCVLlsycOTNDfuHChfqxpUDwy0W53W15RJGLik6K3yYFcVyBwnvfS9/lzJlTX7eR82AOA1o2bo0ePRomX6hQIT0qWtasWWGz8juQgSWHe/WNVVbCuJAtlFHnot4K7OCi3pndXLRdu3akzJo1S88mm6JHjRpFjdJp0P2UGtwKYBQsX778l19+iY+PL1y48M19irhixYowK/3cnWDt2rXDhw9PFpGSHUz4vCxkvbFWrVq8DtwpyS3jTYIFCxb4tBOzBgbJiChz0c2bN0MmlY0ux2TVOenjx48zyX5pe2pyfOY/f/688FgscuMpKwVCdnecOHHi+eef99nHbyAbv/32mxwScGRWnrgSz0UbN26sB3bTCxRJVIQrAVIFWt6kfIwbtaNS51TiWXHo0KGOW8SHRLhctHjx4lgYDg0/deqUsqvGjRtHfvhkgwYNlHNt78aU9mdo8ObIkCFDTExMoGpaAbhotmzZ1JnPsLioR7tZgbmoZVM1adVmzZqFcgLeI6aLA95ctEePHsUCw+HZhV5zL4HK2m+gPUsK//nPfxzBYLZu3cqNHTp00BNHjBjhs10yrl69+rVrQbPTm/I70Lwnu4gdjhAZF5BY+ZwXdS7qrcAOLuqd2c1FxXGxw0Gi7N4Puovb4KaHBJAQeJ95vgkgLmELFizIlDVhwgQmzIEDBzZs2JC/yS1asoFJQF49y5Yt48Vx5coVd0pyy3iTQCLoOI5LGBgkC6LMRbGb4ZMYQ7LtRPwFy+b4ixcvSsRRLi9rwIghs5DYb775ButK/StFHRS5xaEb60K95MQIBCZVqlR6BJTff/+9Z8+e8jvxXDQuLk63qvUChdE9+OCD+stpyJAhDnaqINRIhcCSj4LCqWBK1CJXrlz69tf58+fLSmm4XFROhOorgShz+/btFdk4d+5cbGwsdddJi3dj6u0vTNLDUHNz0SNHjujrnGFxUY92szy5KPXNnz8/RKVu3bqBRNUhbhgSz0WR8I3AcEdbgU3pvi5B3rx569Spoy79TkTi1EGd4BXQiRUqVNDDjVq2J8/06dP7PfSCtgfdoyvtj/7oiaVKlXrsscfkd9S5qLcCV6pUiWGo/uWd2c1FkRMWjfy6POQvUKCAO6Crwa0GpuJq1aoxJBMTU/QGwvTp02vXrs08CSOtV68eE5T7sN8tBaZQZrzu3btPmjRJJl53ikHiMXjw4ObNmz/xxBOdOnXSPWUYGCQLosxFz5w5Iyuf39mQs0OyuKQCijqAmaKOlTqQmNP2BtEFXEUZlLw+ZYupZYeUwNbMmjVr7969IVGwzSpVqohFe/XqVZhV+fLlVSGy+qE75sZqh5XJbzkwqTvCnT17Ns9VK4e8h2JiYlSBFy9ezJcvn8/2DDl16tTly5e3adPGYy+o2PRQ2V9++WXNmjXimx6mJ0a8eNvLnTs3c/SMGTOeeeYZtRJIvfjXq6++qooSC1v5JBR/Lerc4LZt28RBJWUuXrx4zpw5NWrUcHhqlVscJyE9GrNJkybwB8l26NAhsnm4leOhDqrZrl07fSOleH7X26pw4cLZsmVTl/3791dfTL3bTRb9dC+vOuR7weTJkwOJquPee+91SBUIcEWdDiUScFfYkWpPLtOmTSvRny37oAF0WhE/hY8++ihLlixupxfC89UmaihZoUKF+vTp4/fRoXBRTDGoMs9S+kYvoCRq2fbpp5/micqdlUSS6Ny5s0eZ3irtrcDilXHTpk2wcSb5UDI7TjiL72UVnu7EiRM0gt/PGQYGBgYGBgY3N6LMRS3bdJP1zy9tF0TqI584zvXLRSUMqeGiKRlFixb997//DeWYMGECtqZyPYKhDOfJmDGj7KqCFsreUYxa8f/5/9g783ifqu//v81DJFOZ50TmDBEqUxQ+NJChRFLmIZQpD3MIISQhQ0SGkDlTGSJzmaMMEaIUyVCd3/N31vfux+6c9/u8h/u+17Rff9zHPfvs9zl7r732Wuu1p0OcOnLkyAsXLixatKhw4cKkFClShP8JZOXzD0JsJFodMmRInjx5qlWr1qNHj5YtWxLdqpPf4AZyBgy0gTcKQ+Nd8pFSn/0hjXfffdejChcvXpSvridPnpwonALIUfUy5QhnIHyXr4Hxl0SZboWiyFn5EBI4FXyYt8gXHQnfd+/ePXbs2IwZM/rsD0yrEHzJkiXwJSkYdNpBRC37e6Fly5Z1JAYSpmXvD0RukFVi/Zo1a3p/+hL2jqygl/Xr14cFwUKHDRumTsiA4YvQyEBr/vnnn7KhEdBkp0+fXrx4Mbd89mmoW7du9ZDblClTaC/+L1iw4IcffuheZUrmlClTBv1+95YtW2QsQNqRJwc6lA9J0kySs1OnTtEiMEi1aNGikP933nkHLdW/u33kyBFUTn0sUaF69eqNGzf2+zQ4PNrSpUuXqVOnkq1///6BDkYPhYta9hGOdAcUqXfv3jRonTp11GmTkN706dP77A/5wgxRyMqVK3OZNWvWQN/J8FZpsboeCsytRDaaNGkifcRvZpQQvZIDt2rVqqU+Iyyg12TPnr1NmzaDBw+GrzqOMjIwMDAwMDC4QxB9LmrZE2IwTMJQs7L/toHQjJ9//vngwYPudTKkkB6tE6fgn3Cw0L9rhKZBfUNZvcMzebI6NItw2bEgimoeOHDA46swYeHYsWMeZ96eOXPGb7pfYYr8ofSQ2NBPEYRYRuUjvUHlFghr1qy5VQ6ExFht27bN7371U6dOuQ9n3r9/v+NAfx1IbM+ePXDsKB6MjmLQCvF5hmQgBUZ13eece2t7oOd7yNDAwMDAwMDgtkeccFEDAwMD8PTTT8tZrwYGBgYGBgYGBgYOGC5qYGAQTVy4cKFnz56TJ08eMmSIOrnXwMDAwMDAwMDAwAHDRQ0MDKIJOaMVZMmSRR01bGBgYGBgYGBgYOCA4aIGBgZRxvz580eMGHGHf5zAwMDAwMDAwMDAG4aLGhgYGBgYGBgYGBgYGMQ3DBc1MDAwMDAwiHOcOHHi2rVrV65cufhf/Pnnnx6/un79uiP/pUuX1Eeq/IIHOn7iPh9b4ccffwzlGPZ4AIVctmzZwYMHb3RBDG4u3OqKsWXLlqlTp3r3WQdu9SobhAXDRQ0MDAwMDAziFrNmzXrrrbf++eef5cuXN2/ePEGCBLKxPFeuXLlz506VKtV9991Xo0aNIUOGOL53tW/fvjfffDNt2rSSP0OGDAUKFEiTJg0p5cqVe+ONN/bs2eN414QJE8qXLy/5kyRJUrBgwWzZsuXIkePRRx/t3Lmz49PlxLtNmzY9depUnIsgMAjTqWPq1KkpcLQ+m2xwG+D2UAy6HuXfuHFjKJlvjyobhAXDRQ0MDAwMDAziEGPGjIEE6imVK1cm1oQxqpQjR468/vrrxKDJkiXr3r27Y66yf//+QizVJOr58+dHjhwJlSW9bt26jm/VXrx4Uegu5FZSfv311169epGSMmXKVatW6Zl//vlnaPAN3+Jev359E38buHGrK8aoUaMaNGhw6dKl0H8SYpVvkhUNBrGE4aIGBgYGBgYGcYW5c+cWKVLk+vXremLDhg2JNd2ffTp8+HDevHm5VadOHT19woQJJN59992O/FDTmjVryvwqbFO/JVMrH374oZ74wgsvkMgrHM9ZunRp2bJlHYWMZ7z66qu3NOUwiCPcgYoRSpUht61bt463IhnEHQwXNTAw+D8Qh4U+cnnhwoWwtn944/fff4/shxcvXrx27Vq0ihFvoL6RSS+yX9GyjnWJoT8K8UaxoQ3uNJw6dSpt2rSOeUjQqFEjv1wUHDp0KFmyZNydNm2aSoRS+uWi4MqVKwUKFOBus2bN9HQyu7nolClTZO2uexa0QoUK3bp1C6t20cUdSDkMQsEdqBihVLl+/fqPPvpovBXpFgLGbdu2bV9++SV/f/rpJ/0WDn3//v1ff/31+vXrd+3aRQTl+C3RAunbt2/fvXt3vBXYcFEDAwNrzpw5jRs3JmT8/PPPvXOeOHGif//+jz/+eOLEif/6669Yvvf06dN9+/YtVarUY489FsHPiUEzZsxYsmTJWBYj3kCBR44c+eSTTyZJksTtAzzw999/Dx8+vEaNGq+99lrFihVnzJgRyq/++ecfcvKrFi1aLFiwQFHKffv20dydO3duYOPkyZOBnnDgwIEUKVJ89913oRfVIGLc8PVmcVGA1q1bY1hQRUe6BxcFXbp04W66dOnU6JgHFwVLliwRhkmMpRL9clE6oOT87bffHA+ZMGFC0qRJ9dCNDkvHcUy3hoivNSDYY8eOOVLIc/z4cbmUwTg9/t6zZ8/EiROpl1t0lGr16tXjx4/n7+XLl/Vbf/zxBwXmH4zzihUrJk2axCsiKDzlUUX99ttvScEIOFKkkJKi//bIkSOYnenTpx8+fDiCVwswVl999ZUU/ocffpgyZQqXShS4IV4xd+5ctw/yEA6gFT755BPu8jTHHDhvJHafPHkyPzxz5ow0umq1vXv3SradO3dKCgG9/vO1a9deuHAB+SPzLVu2qPRz584tXLgQ1dq6dWvEg3ohKgYp8IepU6fOnDkT063SEZdqu6NHj5JNV0VSpPqOmoYL75pCitzjobwLgX/66afuW95V5h8xEcWLF5diu6VxxwILttYGSi7/SBNbNhH95ptvSFm3bh3azj/8dYQi33//vfp5vJXZcFEDA4P/v5NKlswF5aJXr16FumTNmpXMseeiRAPYOx4V2egm7qdKlSoQrVgWI95AgQkL7r//fqocFhdt3rx5njx5ZKfczz//TIxOxOP9E3x/oUKFKleuzBv19M2bN9911127du2Sy549e2bOnNnvcYX4LXg+RTVcNI6ADkDJatas2adPnzp16pQpU0Yiqvfee++JJ57Inj17v379CB0qVaqULFkyOh0RueMJBHOvvPJKu3bt3njjjbJly65cuVLSiTC6detWvXr1/Pnz08vQnFatWt1zzz10NP1E2UAFUFi2bBm617Vr18KFC8+bNy/cChKap0iRon79+u5b3lx0+/btwhg3bdokKd5clDrK4UaDBg1SiW4uSraKFSuSWK5cOfdDCN+5RYyrUnr37k1K7dq1Q6irE0OGDJEqzJo1C6kSDj799NNcpk+fntYROdM3H3vsMQqjc1FYXLVq1XLmzEk355Jf6Y9dv349LTVixIi33377vvvue+CBB/bt22fZA0zIGT2599574UsFCxbMly+fSExRx9CBYjz33HP8nKft2LHDsu0GzySlQoUKiq7QTBkyZGjTpo1colodOnTgcty4cfXq1UuQIEGvXr3CfTUP6dGjR7Zs2XgX3IanqbrUqlWLguGqSJGZ8McffzwU4Vg21+rYsWPRokUR/qpVq/iHbqWMMC/lktIeOnQIiovQIEiWvSeZGvGiRx55RHJiDOlxpNBDLdsaY0JlVTmMSEqFzotz/OCDDyjtmDFjXn/99SRJklB++Gq4ArFCUwwohBzlBYtAAmnSpEFvT58+bdknRUvBqCMqhyhmz55NIUlp27atnNpF4scff0zKnDlzIihhoJpCUDFiNIRjkpPXYZHIBil66623ZI09In3qqafg/0GrjAa2bt2alBw5cvS24XFQ9h0FDMuGDRvQARnHQT+FcMrIC5yfS2IDxEVOwgAyox7q55cuXaJFNm7ceMtzUWqIlmy0sWfPHj1avXLlCnaBdOSCf4W7q7EThHL48OEtW7YgBfrzkSNHbvgIsYHBHYV33303FC4qqFq1alS4qCBhwoR31Eob4u+wuCgG07FeEe+Ov3ccN6oDTgLhfOaZZxzj01w+9NBDeiBOI5LTLyUgIoTMGC4ad+jcuXPy5MmlH61evZp4Ud2SUAw+M3z4cOIDPCZcK1GiRDhHlQeWBVXYunWrXLZs2RKtEJ7AT8aPH88TGjdufPny5RdffHHFihXEeaQQr4dSgGvXrhG7V65cWWgSYaJ+zlCIwJ7wxv79+7tveXNR3i5EjhhXVdaDiwLYAhkaNGigUhxclNhDdpbCHHQx6uAn8Bx1+cknn8DuIiBUlt3XhAAoOgQxSJw4ce7cufVscLYvvvhC/pdGh/YTIFo2IZQgnthRPYEUNaO7fPlyyS/Mlrgf+keBmzVr9scff1j2kVGiAxGUnwgNfYPRKRsyf/58x0JoblEdxa+wGHpbly1bNmJug+3itxUrVhQiTUBYpkwZSVFLB8WQEjTKpbdwoLVcvvPOO3J34sSJXL7//vtySWehK6majhw5UtlbXqdzUUCPU1z0zz//RJdkHIReBgEYO3asiIhmxVGqX7355pvkiWx/Y1DF+PXXXzNmzMgr1E8IpGk+tU971qxZ5EfZVIZ27do53AqKqlczdHjUFNsCHcLpOLjo6NGjSdm5c6dcIjouu3btSoqYo6BV3r9/f8Sj2Lcxzp8/L9OeovaoNAafFIkWNm3axP+//PJLoJ/v2LEDO4ka39pcFKWnA+jzv1xCQS2bbW7evFlmfkU04Pvvv5cfon+OWxGvEzAwMIgAYXFR3LDhohEjXC4qExT60kHspGMKSMeJEyfSpEmTK1cu9xj8wYMH3dvqatWqRaK+pgvgh9q3by9aYbhoHEH6kcwDgFatWqlblSpVglcQsamUunXrknnmzJlyKefKLl26VGWAOJHSu3dvufzoo4+4/PTTT7t06XL27FlS4Gmk6PPkgQpABMMtVEgie+IbSFqHDh3CraCcW0t07r7lzUXBPffcQwYVXgfloiKfhx9+WKUIF82WLVv+/PnlHKPatWtPmjRJYhK/yJMnD9n0jhOb7ejSfXr27KlSpK998803cgmTKVGihKJAEn/Pnj1b5ZewnqaUS4TWpEmT6zGgIilTptQfSJWTJk2qfk4Ayt2iRYtGVn6xVGqvL6JIly4d7aIECE9o2rSp/A83kLESVbyBAwfy8yeffDKCV7/++usyLaZSRJeGDh2qUoTPjBgxQi69hQM15VIWMFsxJlSpNK+ju6nVIrB6RaEJUx1clHhVcVEBWqezYssmz9mzZ588ebIqD7IiT6pUqSJYTRpUMWSS0LHSVZoPJbTstsuQIUOKFCnU0Qyy9EBvnQEDBkydOjXcsoVS0+bNmzu4aKlSpdAWpfmwWTI8//zzoVfZcFG/wLwL81Ipsij3xx9/pEcIvcK+HTp06Ntvvz18+LA+n3z69Gnu8vfUqVO3NhcVKcC80Xs0UkQgA5AyUwxkmZnMFANy/vHHH0Jf+QfVVLdu7Il2Bm5s2bLl7bffHjly5MaNG90T1ydPniRc6Nu376JFi3Rr++uvv06cOJHIm3howoQJQ4YMce9gWblyJX6LkMU9XH306FHsY58+fQjCZMGJZY96zJo1i9hLFtIAXvqJDX2Pyo4dO3BdPBbjGO7eFRQVO0hgN27cOH0C6vLlyzhIaBixOw9Xj6V7z5s3j+pTR8dOEo+ShF5CBI6UxMTQOxAXYajIGcMxbdo0Utzv9Ss9BQJN6kiZly1b5peLBmqXyLgobApNeOuttyiM/lvFRVEw1IPXOXiaqBBtgYI5PgP4yy+/6GvwMKwLFy7EyGJ2CSb69eunb92xbC0dNWrU8OHDkV64FIughN8iTNRML3/Ql1r2KikUA2GSLSwuiklMmzbtfffdpyfydp+9VcbvT5599lnu6jRGgVCMW+3atdMTW7Zs6fD6xCs1atRA1cPlokRp0g1lLghjLpcqBLRCMwh3CAj+dD6mvlaCRiVPnjxTpkw6a6KPkHnu3LmWbTcSJ07siMPQajKoBZMEdtASzLWaR4JoOc6PDVQAeRQ21rJnJOjvKFsE2yZbtGjBc1AA9y1vLoplwyzoE1lBuehjjz1GhqeeekqlCBfFgKNphMv8T9fw3rMnEzgEaiFVLxjg8DQBZFg5RJncU5wfYoxLVfnd57VQfVKGDRsml7Lu9CkX1Myqg4uKociRI0dk5V+8eDE/p6VUdWRhp3K7L7zwgop6x48fD51zl02R1bDg5qIiCqUPVsxoixqtCCocFbTgzkTUcCRJkQn81KlTY+EdsU0oXFTm5NXkihWz3pt0d3ncjjgogipG7ty5oXYOlouf1dlm586d9WUCOH0u6WXiUvktfdy9wzYoQqmpu/yZM2cmRU3QQRC4bNiwYehVNlzUL4g0iA/V4JRl79aRmT8suWMfKSCYFzpKUM3/MlN9y3NRqbNafCzUVMIy4mz+3759u9xC40UQRMP4Ceqsbgk1BR6Dlwbxj27dutWuXRuTgYEjDEqWLFmRIkVefvlluUsitmPNmjU4j3vuuadSpUoS1hAQ33XXXRKOPP744w0aNMCZZciQQYU1NHe9evWmTJmybt26+vXrc1fflUQoXKFCBQIvnEfr1q3TpEmjpgXQKMI15XeJnl977TV91Q30jGJQYHQMtxFoEskv1q9fz3vxT3A5whdKhUKitD179pT4Zv78+bLrTySwatWqYsWK4bnpwxQA4XTt2lU5hkAlCb2EX375pezcw+/i2ps0aSKLJ8eMGYOxrlu3LgFo1qxZKZs+e+YhPcseFi1UqBAVgWlDCbJkyaJzUe92iYCLIpZatWpt3ryZOC+PDcUqhYtCkHis8LSyZcvqdUejYMUUqWPHjgQcQtohMKgcqqh0gDyybwenhSNE2YgCeThPkAwQJHz2nj17MLs0ZbVq1UIvPy4wZ86ckCskTNSrPv8Q9KWATlGqVCksIb+lmrL1JUQuijkls75uUICOIRZ3frw7MiEo/PjjjxF4gQIFKJXimRJ/ODYaIQoS4ckqpVmzZrJJLFwuitFu27YtP5EIm6gO7o3y3HvvvZIhqEG4o4BKy744faWcZU9Kk0g4rifKPKEov1gDjJKeAbMgNsGyhzDSp0+PZsqsiGWfwuJzLRH0WwBegXbRQ7F4sA6sxBtvvOE+6ScUyAdUMDLuW95cVNQerF69WlKCclEYFxn09bT6Gl16X5IkSXwBFgwrCOFX0UjsIXPRso8Xt1KjRo38+fOrqcVy5crpzCRQ/C0E7Ny5czr18ovoclFcGG4FPysTxYiO3o1toRaWTU1Lly6tMsvUXLQWy4TORaWbhCIcy+5ZuGyskNBsFcBYdoQjKkdgo3YpW5Fy0Tlz5pCyfPnySCrvgrdi0E/lU7oOJvn111/77H2YcimLYtQGjcqVK8tWWPkALwKhcSMoWyg1dZdf9k6rSU7cje+/Cyi8q2wZLhoAbi6KNRMuSpAs3IqUS5cuYdJlZ6noLX8J9iRuv+W5qKywVUelQzJlwhO/iM/jUi0PoMIiFNnVoEBOB2s1uBkgiy6WLFkil4SqPm1RH00GE1OjiX379lXBqBWz8aN79+4yIC2fiVO7gFq0aKGWhaAVxKnq7ESMY6JEifR91QQupKg9BsT3ut+VUUDFRQnfR40aJf/zkD59+oRYWRQ1U6ZM6rwHcTwwUrmUPTCyUkjm1ui3qVOnJvRXT5AI/r333vMuSVglFN9ZsWJFtX4MMkzIqMy3rHJRltpbehChjBkzKk8A5DwGxUU92sUKn4tiBLJnz65Gl0Q+EjRbNhfl4WvWrJFLCamVBYCxqABU4mm15g2NIszSdQCZkwGiLlKC9/q0LWStWrWCt8v/hFmOpaoeuHr1Km9RcTOS8WlL17xfShBMBdWkN2UmGA2di/JzBzkXwMn9PkR6AcEuZO/o0aNQYuJFUuiVlj0tTGGQp5oBs2IWv6nxZn6oOm8Ea3TlRFN9tgdFVVzUCmYQ7jTI6ADtpX9iREyoHhDrm9ZkIsIxVY4wYZ50cBni2bZtG3kgEio8lQ1yCxcuDFoAGZuoUKECkf3cuXNjM0zQvn17PeLU4c1FRfGwUWqJrDcXFSsN1DJLy7VfFFMpefRZegdwZD7XWsfYALOmrEHt2rXpj4MHD/bZc86YOPqCntk7/j5y5Aj/O37iQHS5KJBzZeiePIqOTAiHocOG/PTTT1gM5eOsmHGHaK3nD5eLBhUO5Ue89CDRZ1mjq3NRsGLFClmkTQWV0kbGRSdNmqTHALGEt2IQetHoPtd8Pk7H4Tvk4C4MCNwPx4pM6PgPPPCAZa8ej6ztQqmpu/wnTpwoUKAARgwHR2CAL6Z36PO6hotGBjlE171Gl9hJzYuq6WgURtgWZpYgbfPmzYdt4G6EuzkW8cYdosxFpZ6yNcWK2UTrXm2LwhHoy5SpvmDmzJkzQtM3btx4K34z8DZGv3796PbqkAwMBJeKfWFHsHfvx6BNmzbCmuSu2BS1fJSOwaV8xk2oxcCBA9Vvc+bMSYrQEsKCIkWK6MVAN/TwpUyZMrrfle1SiosSmeXLl09xAD1G8Ubbtm31TUeWvbJRWXmJpPXBbBlc1CM2+jzkDSsv6h2oJGGVUMY433jjDZUi+6NUBCnCRNpy6S29/v374251Mqmv0fVuFyt8Llq4cGF9xBrfM23aNDXT4tgvyut8MWsRwezZsxVr/eOPP7ilL/ry1gGQIkUK5YybN2/OJcG3XIauEqBPnz5qimbRokW8RXF175dWrlzZcSBEWGt0KaTemxRkzaH7G4mQQGF6KgWGnDp1avWxClk+8NJLL4mN5fkSfsnc6fHjx/WYIAIuKtxG56Jwb52LehiEOwf6oncJ4tW2N8sOGdOnT69HZs8//3zixIllgEwmIvTDQsC8efN82upr2aqnzzPIE9Tgr0cBpHe7vwgaAUR/1NysDg8uisbKbK3q+FYwLir7MNWIocB9jm7jxo199k62PXv2+H0O70VKEaxUDAQZI0iWLBkGXKak6LOJEiVCyJgjx2ySd/xNHMUPU6ZM6d4HrhY+RJ2L4gsSJEiAmYWOig0X9Rs0aFDRokX12XI5c1jfHCsgrnVvHgmKcLloUOHgOsmsdk84uKgsA7HsYUeh35kyZRL3HRkXFW/rPu4Ls6/G9ENHUGImYyj6gLhlH1SjhwSWvUJHoogGDRqI7slsNiKK4GQyQSg19fuxUKxZlSpVOnbs2LVrV/dBFYaLRgZolGNKUw7Fxezg8YWRqUmFkydPrrWP1VVbSd3Qh63jDtHkovRbB+cmOndzUbo60Q+J0E5HJc+dOyerfAH2y3xg/eaBDH2p4Bvl5nLFihVyWaJEiXr16jk0WA3MOEJPsePiPySmX7p0qeO3dBv0BNfiMDQk+uyzKOTSm4fIfAtBAK4lrNiidOnS+r4FB4SL6j6YwBFv7diqIc5JAr5AJQmUvnDhwjkaJHx0c9H69evrbER2XMju/6DSgyBlyZJFv6tzUY92kcxhcVEMH/KhsoEyOLioRBh6FGLZxmHUqFFQLJ+2f8kKgYsSnD300EPyP7onp1kgJccHoEPEgQMHoPHy/RsV43q8VEas9QJbYXJRspGZUMORLnG2e8wOzuxznRYDeydRVlnzE7QIcnjXXXcRQEAaS5Ysibbgw9Bhyqa+RWbFCxfVDQJxpK75IZ6kdSuic+fOig0KG3/ttdfkEreYJEkSfYYH+dODZGbbihkKdCyooxGLFCmiqCYdioeoATKcacaMGWVEQ8ZiPApAgOj770Eslj0/H0E1ZTq3U6dO7luyeNXNRdGBatWq+ewzP/UYAC7kl4uitHKoCWp2/vx5/ZasBtctD7ItVKgQiXny5HFktmwppUiRwvG5FxQ1lp8ulInQ++67T83Hwpxp0AcffNAR5ASNv2VPbPXq1fU9jUOHDlWroKPORYHsB8mVK5eMwOJH0qdPj2xffPFFPRsKQzaY/Fpt6Thm1tGOISJcLmoFE46cwqrUWMyUGtZERfXDReVYVzkn4tSpU+I3lRrI0g99i4ebi6LGYqL1vQ+IDt/h8T3nQAiqGDLnT931X+ExMey69ZaJUJqvVKlSkiInGNGakydPDrdUglBq6i4/3cp9zHtYVZaZcH2VuIFlS16iNYlR1Z5HYVtbt25dG7OPEuHL/CdtQZc5pWHfvn1r7S/B8H/8HNwT5XlRmdVUU0b0bamPyoDWCkcXIu73IUhQZHdn7iC6OUGbZsiQAc4plKlfv36E2qoFU6dO7Yi2dXiEniNGjHBYcP2N3Lr//vsd6Xh0tU0uKA+RzasSeaiVvUGBYXXMOehwc1Fxco4zdWA7JKpTQwKVxG86gXtSDfLtxxC5qHzKL6j0smbNSmyq39K5qEe7CMLiotLiuqNywJuLYgrRtxdeeIFKCTGLmItati2WDy3gfWfMmBFK+QWQYd5LSVB7OegiFC4qq6T0k/St8M/RRR9y5sypp+BFiGXRGXdm+UacQ9pyRI3jNCNpPlnwKedbrF+/Pm3atA9pkOkpgmb+178F4oHYcFH6i675sYyhb2Y8++yzauOifLNHDgqyYgSodo8TckEDkKeK2+jpaK9OmXr27Ek0rCI/VAtKoAem0soIGTokQxIeBRBtefrpp2V11tmzZyGu+oLhsIDyqMBXhywXVKEktTt27BjVRNVp+t69eztiIJmtol5q4gsjjK2QTRN0MceHCogffDb4oZ6OOZUzdR9//HE1PyCQhc36LO7IkSN99rc6Iqu7QD7lgtlRLShHiCFnR07h5zorEJqtqiCbZQD9EVs0btw4eq6a3COgTJIkCfRDWWaooM9e6hyb8suUuxqqsGKWAsnHNnTIIEKqVKkw1xMmTOjRowc+SDnBsOA4/cGKGWXTV3wIAVPnD3kLh/7isxfxyhdEZb9iyZIld+zY8cMPP7Rv317XE/ws0Y66FDNIl+S3qJzsIsmUKdPmzZtFS4sXL+7TTjMWkF/K89RTT0ELIVFFihSJ4KBaKwTFgCfLmLg6WJvekTdvXofyW/ayL72zW/acqmPXRrgIWlM5Cl7/PHKVKlUIKdu1azd8+PAPPvhg5syZq1ev1ue0g1aZWJRulTx5cuwG9m3tfzfP38mQZaf46++++042TqolYLIRFJBHeClwhyK3/H7RLVu2UAF1ZLzUR/mwM2fOrFu3jhScgT7Q+Pvvvx8/flxfbCZff9G3uhnccGCvCYlq1qyJg+nSpYs+UoDJwy47Bo/Pnz8vwYFH6Clxs+5vBMK+YE3JkiVzEB4SK1SoIP978xCZIiCQkvPEcSchjs4SOqdPn95hmpWVdHPROnXq+FzTCHXr1iUmELoeqCRhlTAsLmoFk55MDui7tXUu6t0uVphcVAomx13oUCL15qKIt2jRojLUHUsuKvUlwh42bBg+DM8d4oGZNDchsjqhNHQuKidq6GTYCp+LIm2crq6QsiXV735XiacdR9TI4MLixYvd+VEY4ldZsgjteeO/kA/JEs/xf4gL7WLDRe8cEDjmzp2bOGzGjBkExPoKdpkRkr2F48ePJ7xzL5f97LPPIBiQGXhCy5Ytibz1uSBZ10AsrlLog/QyGKyaMPcoAP2at/MEzCBBNpG3Y6AtLMyePZtX61HmwoULZahOwFtwH2nTpsW/0NkxRPQa/QmQGfRZJjlBypQps2fPjinLkiULfLJXr16OzxFZ9owQBFjlb9WqlX4CBVREbhUsWFAPdgcOHEgx9I4pVjGWXNSyPyKqh+YQGCqrxzykENBLHfGncpQUZop4XWiPOlxq+fLlcs6csD50QJoeBy3nOEiBv7Uh31P12Yu3I25EypYjRw59UffevXv9ficG0TVu3BjHJy/VvwUaOnjIyJEj5YudNJA4gvfeey9r1qzCq2lcVBR5yvGB6dKlQ41llDyQcCx72jZNmjQ+exSShqZS6L/PXuSJeYddI3Ys/Jw5c7B1JOpDsStXrpQhYzSZ7knDyVgPLoBwX2iz2Hk6nVqrgjcfOnSorMTx2RPL+vl/ISJ0xcCvde3alRTMNbwd060fVahA2yE33VxgExwnq4cLj5oiRgqDt/XZKxfUqnuKrfIr4Dfh0qFXWbaj0xZU2ayjVKBxZfGpQLaDqrvy7VABbNPvqc63PBclVKUCxBaiFjL/K18KxVLIF0e5vKYBAiPftFkbc3AuVkYuY+P/DKIODHSg/XU4Wt9/h59pWdy/DKt7hJ4ogxgXfcEkPkPiA9nbo46Pt2za5tOmd8qXL49vUKGDHM6hIjA4s154bikq5Y2XXnrJ998NbNAAtQ3GzUXlvfq3AS37XCJ1WmmgkoRVwnC5qLf0ZIeYvh1Loi5ZRebdLlb4+0Vlu6la1G3ZbEqRNw8u6phXPH/+fGy4qC5woUwhHpnjUC2ZKAiFi1oxY+r6Qinhou59TYGA6yW/+jKBFbO6e+PGjSpFxRbY3hIlSqizEwUdO3ZMliyZ2+vIxILfr78I5FimsNboQpwciuqYhDdc1IrZrkmX3Lp1q0MTihUrRiCO8dyxY4f68qcbZKBdsMkhHjh/5swZfebQowACXr1t2zbH4YIRAIWEEakFxjctECOBr2PHnWUH07EPc5GzY6w2goWaOmidffv2xdt379z70j3Kj19ALR3T1PGJQMIhVICfq3R6EA5XGleoLCXfs2eP35OryEBAK90BYxv6sdK0O4U5evRo/JAl3kKlvINnR2tS66gsQgyrprNnzx4xYgT+HV6wePHiWbNm4WShxOF+C/fAgQORHfF924NmpQ9eunTJ3RwoMKEUjX7zfDgzylz0999/l5nP7TaEUoqfU18NdQA1grfI4l5YOM5VFvGuX7/efNPl5gGU5q677ho8ePCcOXOWL19Oe+mbynA8cqR4ixYtFi5ciJV57LHHFPEQaqd4rHyuQI3DyVKZBx54AC5EtN27d28CF+kh2FNispIlS6q9lBDCUqVKqbBbxiO7du167ty5pUuXyhhwgwYNxDblz59fGSmITbp06ULUKHSVwN1nn4QBDRg0aFC5cuXU0LvMGOgkja7+yCOPQD/USCrheJo0aVQcGagkYZVQ1tFBKlSKnF2kjj6SA4conlx6S0++S546dWpak/LDUmQaoWnTpvJAj3axYr58oI7FDgo53DVx4sSdOnWCuXXu3Llq1apCZen+PnutlMos/EeYnnBRhEnEjAq9+eabaBrSPnHihLxdJniVSkyZMoXLkSNHyiXpvFSd4USDqoWmx48f97lWVQWCcFF4748//kjjinAojBAq75fKmSsFCxaUOVgqIkP+VFMd8+YNHgi9VC2LxLjUv8tSpUqVHDlyKNogNFutQCbk4q7+rQt5Zv/+/VOmTOnNxiPgonJULwwcF4CQu3fvLscsqZPqvA3CHQ6ZSK9Tp86NLkg0QaUKFy58A8lJKIAtq9WeBgYGcYe5c+fmyZPHL2V1nGxscIcgylzUsveIyvznWvtEYDUAIyuY/XJRy14C9/XXX6tE/jebRW8q7NmzR6a2dEAJFBtZsmSJfLxYVmIoIkpAnD59ep+9IY3YdPfu3ZUrV/bZHxuQVRwE0A0bNpRVPfyFXupLpGC8kJayZcu+8847bdq04a6+UpFIV/Zqwk8gaWiO7FyV5bK5c+eGMn388ccTJkyAG4e1nYC4WT68AYoXL75t2zbLPoNnwIABsrCkVq1aixYtUvkpVcuWLfkJnI2gn1BS5+qBShJ6CWFQcoAEIT68DjYyduxYOTAAfkXx9u7dKwfqkDhmzBiZkfaWHpxKSAI/qVGjBqEYjQJLlOWagdoFEg6HgWv57KWbIplQMHnyZFnmJGWWYyF4msySwV6QLeq0YMECkXzRokWFN7Zo0UKaGJljT0R/qlWrhkmRT1/47L1MMowljBriN3/+fJheq1at5OFIAKE9//zzUMTRo0fPnj0baq0+qBMU1B36x6OSJ0+OiM6fPy/LvXr06BH0pZY95ywrjjJmzMjPYZXFihXjrgghFPBGelDTpk1nzZrFzxs3bqy6Hh4dv54sWTJ9tJuSZMqUqUuXLlOnTkVzaDI1LYOJRt/ovC+++KKupX4RARe17MNaZHDq/vvvpytBlelEgwYNQqmCGoQ7HDLlrr6vc9vg+++/r1u3buhrAeIZiL1Zs2axPKPIwMAgFOAxcU/usWwit+HDh9+QIhncWESfi1r2TD3ckuAprPlffoVqEpzx17iEmw3wE8jeiRMnNm/evHLlys8++2zKlCn169fXD7Wz7Km5yI4nvXz58v79+wOt+eTuoUOH9B0OCiRyS2aEyKZ/Ckn+J0A/ePCg398GxUkboeeXwrjP7A1UktiXMBR4SM+y+bzszqLPuvudd7uEC/l6cATxKIVUg1MUMuKd5CJwCrBv375wP9vAexGjmri+dOmSe91a0J/LS90HeIaI06dPy9F2jnSosnuKlTfSbaGCjuYj7F69enXou1UjA+115MgRGfk2a6hCh3zpRB2LejsB99G+ffv4+VpdWFixYsUd+3lbA4P4h5yHnz179q5du06YMGHixIkDBgyoXbu2+zQvgzsEccJFDW4zEHNnyJDBvYmC2MLvh+MMDAwMDMLFoEGDnn/++fr167dt29bx5UkDAwOD2wbTp0+vUqVK1qxZYaQ1atTo0aNHWGO7BrcZDBc1CI4ZM2b4/nsqo2UT1Pbt24e44c3AwMDAwMDAwMDAwECH4aIGwfHbb7+VKVPGZx/V/eSTT9aqVat06dItW7Y0Bx0bGBgYGBgYGBgYGEQGw0UNQsK///67Zs2aYcOGvf322wsWLFCfkDUwMDAwMDAwMDAwMIgAhosaGBgYGBgYGBgYGBgYxDcMFzUwMDAwMDAwMDAwMDCIbxguamBgYGBgYGBgYGBgYBDfMFzUwMDAwMDAwMDAwMDAIL5huKiBgYGBgUF84/Lly5999tlPP/10owsS37h+/foXX3zx7bffhpj/6tWry5cv37VrV5yW6o7FoUOHJk2aNGbMmO++++5Gl+U/OHv27NKlSwcPHvzuu+/u3r07fl76zz//bN68eeTIkdOmTTt58mRcvOLEiRPjxo377bff9MRff/11xowZ/FUpW7ZsmTp16r///hsXZXAX6dq1a3/++efF/+Lvv/+O4lu2bdu2du1a72K4JWNwJ8BwUYPIceHChVv04QYGcQHimIgze3v9sJ58o2D6bIg4f/58s2bNkidP7vP5vv766xtdnPjDlStXOnXqlCZNGir+0UcfBc1/9OjRNm3apEiRgvwffvhh3BfwjgM0r3v37ihhrly5EDLc70aX6P8wa9as//3vfxs2bNi1a1f+/Pkp2+zZs+P6pfCxevXqzZ8/f86cOUmTJk2VKlVcfEG9SZMmVGfgwIFyuX79+jp16iRMmJDE77//XmXLkSMHKRs3box6ARxA1G+99RYuBh5YtmxZn43UqVMXKFAgY8aM/K1du/bYsWNhqhG/Yvr06blz5+ax7du398jmkIzBnQPDRQ3CxvHjx3v37l26dOlSpUpF/eHz5s17+eWXs2bN+sYbb0T94QYGHnj//ffXrVu3ZcuWV199tbKNKlWqEKjp8YEb169fHzZs2EMPPVSwYMFy5crly5evUaNGW7duDZQfr1ypUiXCcYI/HD9uvmfPnjzh+eefj+DJixcvDiWmj1OYPhsZSpQocadxUQFqHCIXFdSvX//25qLRnX0KHWvXrkWwMjP/7bffVq1add++fTekJA4sXLjw3nvvVZOEhBxFihSZOnVqXL+XwCZv3rzy/8yZMzHOV65cifpbVq1aBc3es2ePSoEHZsqUycFFR40a1aBBg0uXLkW9ADrGjBnTuXNndQn3Fi46adIkSUExatasSUr+/PnDXcShKzbuNSgXdUvG4A6B4aIGYePatWs7duzArBAlR/3hFy9efPvtt3m4iWsN4g3//vtvy5YtV65cKZdEBkQkKOFrr73m/cODBw+WLl36/vvv37lzp6T89ddfcMsECRKgwI7lVTjyGjVqJEyYsF+/fr/88oskHj58+KmnnuJd1atXj+zJc+fOvbEDyabPRgairjuTi6InYXHRHj163MZcdPLkyV9++eUNeTVUJ2nSpDfk1d4oVqxYrVq14v+9mTNnfuKJJ+L/veCRRx5xcNF4AL4Dkn/9+nU9ERdDST755BOVAiEvVKgQic8++2zoD3coNg8MykUN7lhEn4tevXp17969G23s2bOH+EndQqH37dtHOgr6zTffEJm5l8KfPHlyu40zZ85EvWwGUcTdd98dF1wUoCEmrr1VgDO7Cfdx/fDDD2HNFnbp0qVv3756CqQRJRw1apTHry5cuJApU6YMGTIoYqnw5ptv8vNBgwap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2aJDbvREdxtgYEHgDDLuWqMXn7Xh/dkx7DBc1MDgP2CK8nbZH16EoikmTShDu5sa3rN7nBtD6ErDrYHbrbwGtxvq1q27devWG52L2wKQtCJFisT5y8WtinffffeNN9640bkwMEgQGC5qYPD/ceXKlezZswe1Doo/duzY8corr5QpU8b7/L0kiNOnTw8cOLBChQrVq1e/0XmJO5YuXdquXbs8efI4nJToiENjOHHixIABAypWrIh8wpHNpI5QxGhgcJPil19++eKLL86ePTt//nx9a65BQmDv3r2bN2++dOlS165dDenyC4bZefPm3ehcGBiEH4aLGhj8f/z77781a9Z0+xkPOy5fvixb/x988MGEfld4cf36dfGb4jgu4uYCGo+4rPQgUXFoDNeuXRP3gA888EA4spnUEYoYDQxuUjzxxBOyVy1VqlRB/egYxAcMtrItWXYmh25jfLth+vTpbn/IBgY3O8LPRa9evRoVFbXVRmRkpG5zLCdQEb5p06YdO3acPHlS2TEzEh07diwiImLjxo3ffPPNjz/+mDh+hA1uPdAChwwZkhCRww5UnBvIRY8ePTpjxowQI/fv31+/FCcZ4c9TIoKByEGiwtUYUKpC5KJhbH6OCko0JJwYDQxuLD7//PP77rvv/vvv1w+WMEggDB06NH/+/HXr1tW94xgYGNwOCDMXvX79OkySgRtKCeHkD5eyox22CdUU70ziZVg/ygaOqtw6yZ89e/aYc4QM4oCOHTvWr18/ISKHHalTp75RXPTy5cvimzGUyPPnz8+QIYMecgtwUYYmB4kKV2MInYuG643uCko0JJwYDQwMDAwMDG55hJmL/vzzz9DIbdu2Xbt2DV66Y8cOLuWM5l9++UU/cfXo0aNySUx1Nqt4J7t48SJUlkuzeT2p4fvvv3/vvfcGDx68Zs0ax61jx47NnDnz7bffnjdvnnISLbh06dKcOXNOnTpFRS9evHjYsGG7d++WW1FRUePHjyfN33//XcXn/7Rp04hMy5k4ceLYsWPVN4vvvvtuvg05oopWJJfLli2TCP3790czLleuHIFffvmlBNLGli5dOmjQIF6kuwX3G/m3335zn+q+a9cucjJkyJDPP//c4V6MTMq5bWQJajd58mSHfRGZHzduHJLhLY5nY8VF6TgLFy4cMGDApEmTzpw5o9/6559/qJERI0aMGTNm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
```

---
