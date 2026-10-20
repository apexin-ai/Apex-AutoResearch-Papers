# Research conversation: [Round 1 审稿请求]: 你是 Reviewer 1，负责 **方法严谨性 + 实验有效性**。 ## 论文信息 - **标题**: "Exception Events Are All You Need: Component Abla

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 84
- **Recorded user turns:** 3
- **Tool calls:** 20
- **Original source:** `logs/chats/exported-trajectories/account-3/98d2b939-6454-4d7d-877f-2c64a5a37485.jsonl`
- **Structured JSON:** [`efba552c999670de0f49.json`](../../sessions/ef/efba552c999670de0f49.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-19T12:51:21.262Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-19T12:51:21.262Z",
  "sessionId": "98d2b939-6454-4d7d-877f-2c64a5a37485",
  "content": "[Round 1 审稿请求]:\n你是 Reviewer 1，负责 **方法严谨性 + 实验有效性**。\n\n## 论文信息\n- **标题**: \"Exception Events Are All You Need: Component Ablation for Trace-Based Verdict Prediction\"\n- **Venue**: EMNLP 2026 (ARR May 2026)\n- **截止日期**: 2026-05-25\n- **论文路径**: projects/trace-verdict-study/docs/paper/main.tex（含 introduction.tex, method.tex, experiments.tex, discussion.tex, related_work.tex, conclusion.tex, appendix.tex）\n\n## Venue 格式要求\n- Long paper: 正文 8 页 + 参考文献不限\n- Limitations 段必须有（缺失 = desk reject）\n- Ethics Statement 不计入页数\n- Double-blind (ACL 模板, [review] option)\n- 匿名规则: 不得暴露作者身份\n\n## 你的审查侧重\n请聚焦以下方面：\n\n1. **实验设计严谨性**\n   - 数据集构造是否有偏（591 problems, 67% pass / 33% fail）\n   - 测试集 49% 重复（607 unique of 1190）对 CI 的影响\n   - 训练/测试划分是否存在信息泄露风险\n   - Multi-seed 覆盖是否充分（哪些条件仅单 seed？）\n\n2. **统计方法**\n   - Paired bootstrap 的适用性\n   - Wilson CI 的独立性假设在 duplicate-heavy 数据上是否成立\n   - 24%/76% 分解的因果推断是否过强\n\n3. **Ablation 完整性**\n   - ae_only / loop_only 仅在 Qwen-7B 上验证，tier hierarchy 能否泛化？\n   - DeepSeek seed 123 排除是否构成选择性报告？\n   - CodeLlama tail-2048 collapse (41.8%) 是否说明方法 robustness 不足？\n\n4. **可复现性**\n   - 训练超参数是否完整披露？\n   - 数据集构造流程是否可复现？\n   - VOTA 提取算法描述是否充分？\n\n5. **Cross-dataset 有效性**\n   - DebugBench 仅 3.29pp headroom，是否足以验证泛化？\n   - 主实验 + DebugBench 均为 Python，语言泛化未测\n\n请按 ARR 标准给出完整审稿意见：Summary → Strengths → Weaknesses → Questions → Missing References → Overall Assessment（使用 EMNLP 2026 评分标准：5=Award, 4=Conference, 3=Findings, 2=Resubmit, 1=Do not resubmit）。"
}
```

---

### Runtime record

_source line 2 · 2026-05-19T12:51:21.265Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-19T12:51:21.265Z",
  "sessionId": "98d2b939-6454-4d7d-877f-2c64a5a37485"
}
```

---

## Round 1

75 recorded events

### User

_source line 3 · 2026-05-19T12:51:21.300Z_

[Round 1 审稿请求]:
你是 Reviewer 1，负责 **方法严谨性 + 实验有效性**。

## 论文信息
- **标题**: "Exception Events Are All You Need: Component Ablation for Trace-Based Verdict Prediction"
- **Venue**: EMNLP 2026 (ARR May 2026)
- **截止日期**: 2026-05-25
- **论文路径**: projects/trace-verdict-study/docs/paper/main.tex（含 introduction.tex, method.tex, experiments.tex, discussion.tex, related_work.tex, conclusion.tex, appendix.tex）

## Venue 格式要求
- Long paper: 正文 8 页 + 参考文献不限
- Limitations 段必须有（缺失 = desk reject）
- Ethics Statement 不计入页数
- Double-blind (ACL 模板, [review] option)
- 匿名规则: 不得暴露作者身份

## 你的审查侧重
请聚焦以下方面：

1. **实验设计严谨性**
   - 数据集构造是否有偏（591 problems, 67% pass / 33% fail）
   - 测试集 49% 重复（607 unique of 1190）对 CI 的影响
   - 训练/测试划分是否存在信息泄露风险
   - Multi-seed 覆盖是否充分（哪些条件仅单 seed？）

2. **统计方法**
   - Paired bootstrap 的适用性
   - Wilson CI 的独立性假设在 duplicate-heavy 数据上是否成立
   - 24%/76% 分解的因果推断是否过强

3. **Ablation 完整性**
   - ae_only / loop_only 仅在 Qwen-7B 上验证，tier hierarchy 能否泛化？
   - DeepSeek seed 123 排除是否构成选择性报告？
   - CodeLlama tail-2048 collapse (41.8%) 是否说明方法 robustness 不足？

4. **可复现性**
   - 训练超参数是否完整披露？
   - 数据集构造流程是否可复现？
   - VOTA 提取算法描述是否充分？

5. **Cross-dataset 有效性**
   - DebugBench 仅 3.29pp headroom，是否足以验证泛化？
   - 主实验 + DebugBench 均为 Python，语言泛化未测

请按 ARR 标准给出完整审稿意见：Summary → Strengths → Weaknesses → Questions → Missing References → Overall Assessment（使用 EMNLP 2026 评分标准：5=Award, 4=Conference, 3=Findings, 2=Resubmit, 1=Do not resubmit）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "e3f72197-8c21-47a9-99b8-7cd49faae750",
  "type": "user",
  "uuid": "39f8223b-71a1-4ecc-a3a1-cf92d9deb796",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/.claude/sessions/review_reviewer_1_7624f219",
  "sessionId": "98d2b939-6454-4d7d-877f-2c64a5a37485",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-19T12:51:21.299Z_

```json
{
  "parentUuid": "39f8223b-71a1-4ecc-a3a1-cf92d9deb796",
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
  "uuid": "1ddec043-d906-49c1-b9dc-2dd397978b08",
  "timestamp": "2026-05-19T12:51:21.299Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/.claude/sessions/review_reviewer_1_7624f219",
  "sessionId": "98d2b939-6454-4d7d-877f-2c64a5a37485",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-19T12:51:21.299Z_

```json
{
  "parentUuid": "1ddec043-d906-49c1-b9dc-2dd397978b08",
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
  "uuid": "52f1b174-f455-4e88-85c8-8092041d9d47",
  "timestamp": "2026-05-19T12:51:21.299Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/.claude/sessions/review_reviewer_1_7624f219",
  "sessionId": "98d2b939-6454-4d7d-877f-2c64a5a37485",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 6 · 2026-05-19T12:51:21.299Z_

```json
{
  "parentUuid": "52f1b174-f455-4e88-85c8-8092041d9d47",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "0501e615-68b6-47aa-9732-02a05b5d4688",
  "timestamp": "2026-05-19T12:51:21.299Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/.claude/sessions/review_reviewer_1_7624f219",
  "sessionId": "98d2b939-6454-4d7d-877f-2c64a5a37485",
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
  "aiTitle": "Review trace-based verdict prediction paper methodology",
  "sessionId": "98d2b939-6454-4d7d-877f-2c64a5a37485"
}
```

---

### Assistant

_source line 8 · 2026-05-19T12:51:24.234Z_

我开始审稿。先加载 session start skill，然后搜索 ARR reviewer guidelines，同时读取论文材料。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0501e615-68b6-47aa-9732-02a05b5d4688",
  "isSidechain": false,
  "requestId": "req_011CbBxW7VQyvJMXMzr1EWmC",
  "type": "assistant",
  "uuid": "b1f7790d-4044-44f9-acf9-0b4f60791df7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/.claude/sessions/review_reviewer_1_7624f219",
  "sessionId": "98d2b939-6454-4d7d-877f-2c64a5a37485",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VE1EoW4S4FyCSAWN4wprp2",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14623,
      "cache_read_input_tokens": 11841,
      "output_tokens": 241,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 14623,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 241,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 14623,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 14623
          },
          "type": "message"
        }
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

_source line 9 · 2026-05-19T12:51:26.130Z_

<details open><summary>🔧 Tool call — Read · `toolu_01C1QzK9WjfsdVhWM3J52g3j`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/.claude/skills/review-reviewer-session-start.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b1f7790d-4044-44f9-acf9-0b4f60791df7",
  "isSidechain": false,
  "requestId": "req_011CbBxW7VQyvJMXMzr1EWmC",
  "type": "assistant",
  "uuid": "dca63890-00bf-48b0-b06d-2247be0fcf26",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/.claude/sessions/review_reviewer_1_7624f219",
  "sessionId": "98d2b939-6454-4d7d-877f-2c64a5a37485",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VE1EoW4S4FyCSAWN4wprp2",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14623,
      "cache_read_input_tokens": 11841,
      "output_tokens": 241,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 14623,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 241,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 14623,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 14623
          },
          "type": "message"
        }
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

_source line 10 · 2026-05-19T12:51:26.157Z_

<details><summary>↩ Tool result · reported error · `toolu_01C1QzK9WjfsdVhWM3J52g3j`</summary>

```text
File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/.claude/sessions/review_reviewer_1_7624f219.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "dca63890-00bf-48b0-b06d-2247be0fcf26",
  "isSidechain": false,
  "promptId": "e3f72197-8c21-47a9-99b8-7cd49faae750",
  "type": "user",
  "uuid": "929e6099-6cf0-4765-9ddc-5e07d2f55de5",
  "toolUseResult": "Error: File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/.claude/sessions/review_reviewer_1_7624f219.",
  "sourceToolAssistantUUID": "dca63890-00bf-48b0-b06d-2247be0fcf26",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/.claude/sessions/review_reviewer_1_7624f219",
  "sessionId": "98d2b939-6454-4d7d-877f-2c64a5a37485",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-19T12:51:27.618Z_

<details><summary>↩ Tool result · `toolu_013DZ7Pnr7dgv6utYgwzg2Jj`</summary>

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
  "parentUuid": "74771406-8989-4d4b-ac4e-9f78a077174f",
  "isSidechain": false,
  "promptId": "e3f72197-8c21-47a9-99b8-7cd49faae750",
  "type": "user",
  "uuid": "392a007c-515d-4d6c-b9f3-8b7f413c5460",
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
  "sourceToolAssistantUUID": "74771406-8989-4d4b-ac4e-9f78a077174f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/.claude/sessions/review_reviewer_1_7624f219",
  "sessionId": "98d2b939-6454-4d7d-877f-2c64a5a37485",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-19T12:51:27.613Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_013DZ7Pnr7dgv6utYgwzg2Jj`</summary>

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
  "parentUuid": "929e6099-6cf0-4765-9ddc-5e07d2f55de5",
  "isSidechain": false,
  "requestId": "req_011CbBxW7VQyvJMXMzr1EWmC",
  "type": "assistant",
  "uuid": "74771406-8989-4d4b-ac4e-9f78a077174f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/.claude/sessions/review_reviewer_1_7624f219",
  "sessionId": "98d2b939-6454-4d7d-877f-2c64a5a37485",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VE1EoW4S4FyCSAWN4wprp2",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14623,
      "cache_read_input_tokens": 11841,
      "output_tokens": 241,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 14623,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 241,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 14623,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 14623
          },
          "type": "message"
        }
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

_source line 13 · 2026-05-19T12:51:31.623Z_

<details><summary>Logged reasoning block</summary>

```text
Let me start by searching for ARR reviewer guidelines and reading the paper. I'll do these in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "392a007c-515d-4d6c-b9f3-8b7f413c5460",
  "isSidechain": false,
  "requestId": "req_011CbBxWaiGtfmtJUwrCmUmm",
  "type": "assistant",
  "uuid": "ce644437-d9b4-4ecb-8caa-1ca63c06723f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/.claude/sessions/review_reviewer_1_7624f219",
  "sessionId": "98d2b939-6454-4d7d-877f-2c64a5a37485",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01R1sT5ERSKZ8Kwu6qmidk7R",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2333,
      "cache_read_input_tokens": 26464,
      "output_tokens": 211,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2333,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 211,
          "cache_read_input_tokens": 26464,
          "cache_creation_input_tokens": 2333,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2333
          },
          "type": "message"
        }
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

_source line 14 · 2026-05-19T12:51:32.652Z_

开始搜索 ARR reviewer guidelines，同时读取论文各章节。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ce644437-d9b4-4ecb-8caa-1ca63c06723f",
  "isSidechain": false,
  "requestId": "req_011CbBxWaiGtfmtJUwrCmUmm",
  "type": "assistant",
  "uuid": "951440f5-02e3-45fa-9f07-56450b6ec9a5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/.claude/sessions/review_reviewer_1_7624f219",
  "sessionId": "98d2b939-6454-4d7d-877f-2c64a5a37485",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01R1sT5ERSKZ8Kwu6qmidk7R",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2333,
      "cache_read_input_tokens": 26464,
      "output_tokens": 211,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2333,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 211,
          "cache_read_input_tokens": 26464,
          "cache_creation_input_tokens": 2333,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2333
          },
          "type": "message"
        }
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

_source line 15 · 2026-05-19T12:51:33.581Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01MMv5rV6qGXRmeeFBCkBJn8`</summary>

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
  "parentUuid": "951440f5-02e3-45fa-9f07-56450b6ec9a5",
  "isSidechain": false,
  "requestId": "req_011CbBxWaiGtfmtJUwrCmUmm",
  "type": "assistant",
  "uuid": "ca175890-4e98-4d51-b86b-658f4fc14d71",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/.claude/sessions/review_reviewer_1_7624f219",
  "sessionId": "98d2b939-6454-4d7d-877f-2c64a5a37485",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01R1sT5ERSKZ8Kwu6qmidk7R",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2333,
      "cache_read_input_tokens": 26464,
      "output_tokens": 211,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2333,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 211,
          "cache_read_input_tokens": 26464,
          "cache_creation_input_tokens": 2333,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2333
          },
          "type": "message"
        }
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

_source line 16 · 2026-05-19T12:51:35.282Z_

<details><summary>↩ Tool result · `toolu_01YRFvPuvEVkzBzLLzHUfdTU`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/artifacts/_project/paper/related_work.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/artifacts/_project/paper/section3_experimental_setup_d4f1e8.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/artifacts/_project/paper/section3_experimental_setup.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/artifacts/_project/paper/ethics_statement.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/artifacts/_project/paper/ethics_statement_77cf5f.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/artifacts/_project/paper/arr_checklist.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/artifacts/_project/paper/main_results_tables.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/artifacts/_project/paper/main_results_tables_d8c8b6.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/artifacts/_project/paper/experiments.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/method.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/arr_checklist.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/main.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/introduction.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/experiments.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/appendix.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/discussion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/related_work.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/conclusion.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9640d785-faec-4070-a9e9-5d7bc87238fc",
  "isSidechain": false,
  "promptId": "e3f72197-8c21-47a9-99b8-7cd49faae750",
  "type": "user",
  "uuid": "6f3b6d85-166d-4b61-90e5-aed0345376d9",
  "toolUseResult": {
    "filenames": [
      "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/artifacts/_project/paper/related_work.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/artifacts/_project/paper/section3_experimental_setup_d4f1e8.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/artifacts/_project/paper/section3_experimental_setup.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/artifacts/_project/paper/ethics_statement.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/artifacts/_project/paper/ethics_statement_77cf5f.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/artifacts/_project/paper/arr_checklist.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/artifacts/_project/paper/main_results_tables.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/artifacts/_project/paper/main_results_tables_d8c8b6.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/artifacts/_project/paper/experiments.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/method.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/arr_checklist.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/main.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/introduction.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/experiments.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/appendix.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/discussion.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/related_work.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/conclusion.tex"
    ],
    "durationMs": 18,
    "numFiles": 18,
    "truncated": false
  },
  "sourceToolAssistantUUID": "9640d785-faec-4070-a9e9-5d7bc87238fc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/.claude/sessions/review_reviewer_1_7624f219",
  "sessionId": "98d2b939-6454-4d7d-877f-2c64a5a37485",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-19T12:51:35.260Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01YRFvPuvEVkzBzLLzHUfdTU`</summary>

```json
{
  "pattern": "**/paper/**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ca175890-4e98-4d51-b86b-658f4fc14d71",
  "isSidechain": false,
  "requestId": "req_011CbBxWaiGtfmtJUwrCmUmm",
  "type": "assistant",
  "uuid": "9640d785-faec-4070-a9e9-5d7bc87238fc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/.claude/sessions/review_reviewer_1_7624f219",
  "sessionId": "98d2b939-6454-4d7d-877f-2c64a5a37485",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01R1sT5ERSKZ8Kwu6qmidk7R",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2333,
      "cache_read_input_tokens": 26464,
      "output_tokens": 211,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2333,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 211,
          "cache_read_input_tokens": 26464,
          "cache_creation_input_tokens": 2333,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2333
          },
          "type": "message"
        }
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

_source line 18 · 2026-05-19T12:51:41.025Z_

<details><summary>↩ Tool result · `toolu_01MMv5rV6qGXRmeeFBCkBJn8`</summary>

```text
Web search results for query: "ACL ARR 2025 2026 reviewer guidelines review form criteria scoring"

Links: [{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"https://aclrollingreview.org/"}]

Based on the search results, here are the key findings about ACL ARR 2025-2026 reviewer guidelines:

## Scoring System

Starting with February 2025, ARR reviewers are asked to provide three scores: soundness, excitement, and overall recommendation.

### Soundness Score
The soundness scores must be justified by the text of the review, and if you give a low soundness score without finding any major faults, this means that your review is not a faithful explanation of your recommendation.

### Excitement Score
You may find the work sound, but not something that is interesting for you personally. Such preferences are more subjective and should be reflected in a separate excitement score, which is orthogonal to the assessment of the soundness of the paper.

## Area Chair Metareview Scoring

The ARR metareview score has changed in February 2025 to be more aligned with reviewer scores, with the score backed up by the meta-review text. The options include: 5 = Consider for Award: papers that could be considered for an outstanding paper award (up to top 2.5%).

For more detailed reviewer guidelines, you can visit the official ARR Reviewer Guidelines at: http://aclrollingreview.org/reviewerguidelines


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ca175890-4e98-4d51-b86b-658f4fc14d71",
  "isSidechain": false,
  "promptId": "e3f72197-8c21-47a9-99b8-7cd49faae750",
  "type": "user",
  "uuid": "7725ebd1-52b4-4e22-a5a4-576719de3560",
  "toolUseResult": {
    "query": "ACL ARR 2025 2026 reviewer guidelines review form criteria scoring",
    "results": [
      {
        "tool_use_id": "srvtoolu_01GuAmP3h54NZr55fz5ECNTP",
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
            "title": "ACL Rolling Review – A peer review platform for the Association for Computational Linguistics",
            "url": "https://aclrollingreview.org/"
          }
        ]
      },
      "Based on the search results, here are the key findings about ACL ARR 2025-2026 reviewer guidelines:\n\n## Scoring System\n\nStarting with February 2025, ARR reviewers are asked to provide three scores: soundness, excitement, and overall recommendation.\n\n### Soundness Score\nThe soundness scores must be justified by the text of the review, and if you give a low soundness score without finding any major faults, this means that your review is not a faithful explanation of your recommendation.\n\n### Excitement Score\nYou may find the work sound, but not something that is interesting for you personally. Such preferences are more subjective and should be reflected in a separate excitement score, which is orthogonal to the assessment of the soundness of the paper.\n\n## Area Chair Metareview Scoring\n\nThe ARR metareview score has changed in February 2025 to be more aligned with reviewer scores, with the score backed up by the meta-review text. The options include: 5 = Consider for Award: papers that could be considered for an outstanding paper award (up to top 2.5%).\n\nFor more detailed reviewer guidelines, you can visit the official ARR Reviewer Guidelines at: http://aclrollingreview.org/reviewerguidelines"
    ],
    "durationSeconds": 7.440053250999999
  },
  "sourceToolAssistantUUID": "ca175890-4e98-4d51-b86b-658f4fc14d71",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/.claude/sessions/review_reviewer_1_7624f219",
  "sessionId": "98d2b939-6454-4d7d-877f-2c64a5a37485",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 19_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[Round 1 审稿请求]: 你是 Reviewer 1，负责 **方法严谨性 + 实验有效性**。  ## 论文信息 - **标题**: \"Exception Events Are All You Need: Component Ablation for Trace-Based Verdict Prediction\" - **Venue**: EMNLP 2026 (ARR May 2026)…",
  "leafUuid": "7725ebd1-52b4-4e22-a5a4-576719de3560",
  "sessionId": "98d2b939-6454-4d7d-877f-2c64a5a37485"
}
```

---

### Runtime record

_source line 20_

```json
{
  "type": "ai-title",
  "aiTitle": "Review trace-based verdict prediction paper methodology",
  "sessionId": "98d2b939-6454-4d7d-877f-2c64a5a37485"
}
```

---

### Assistant

_source line 21 · 2026-05-19T12:51:45.273Z_

<details><summary>Logged reasoning block</summary>

```text
Let me fetch the ARR reviewer guidelines page for detailed scoring criteria, and start reading the paper files.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7725ebd1-52b4-4e22-a5a4-576719de3560",
  "isSidechain": false,
  "requestId": "req_011CbBxXZmk8tG2UuzF5HGtE",
  "type": "assistant",
  "uuid": "3084fa97-9e37-4562-9165-b2aadcfd7306",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/.claude/sessions/review_reviewer_1_7624f219",
  "sessionId": "98d2b939-6454-4d7d-877f-2c64a5a37485",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011pmtVu66V2M1KDfxLsGtDp",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 747,
      "cache_creation_input_tokens": 836,
      "cache_read_input_tokens": 28797,
      "output_tokens": 414,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 836,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 747,
          "output_tokens": 414,
          "cache_read_input_tokens": 28797,
          "cache_creation_input_tokens": 836,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 836
          },
          "type": "message"
        }
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

_source line 22 · 2026-05-19T12:51:45.801Z_

获取 ARR reviewer guidelines 详细内容，同时开始读论文。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3084fa97-9e37-4562-9165-b2aadcfd7306",
  "isSidechain": false,
  "requestId": "req_011CbBxXZmk8tG2UuzF5HGtE",
  "type": "assistant",
  "uuid": "3986eb23-d092-4384-9fd7-df731a45bfbc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/.claude/sessions/review_reviewer_1_7624f219",
  "sessionId": "98d2b939-6454-4d7d-877f-2c64a5a37485",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011pmtVu66V2M1KDfxLsGtDp",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 747,
      "cache_creation_input_tokens": 836,
      "cache_read_input_tokens": 28797,
      "output_tokens": 414,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 836,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 747,
          "output_tokens": 414,
          "cache_read_input_tokens": 28797,
          "cache_creation_input_tokens": 836,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 836
          },
          "type": "message"
        }
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

_source line 23 · 2026-05-19T12:51:48.643Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01YWKwYvLvp6YLuLKmdhYnZq`</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewerguidelines",
  "prompt": "Extract the complete review form criteria, scoring dimensions, and their scales. I need: 1) All scoring dimensions (soundness, excitement, overall assessment, etc.) 2) The exact scale and description for each score level 3) Any specific instructions about what reviewers should evaluate. Return the full details."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3986eb23-d092-4384-9fd7-df731a45bfbc",
  "isSidechain": false,
  "requestId": "req_011CbBxXZmk8tG2UuzF5HGtE",
  "type": "assistant",
  "uuid": "538b1bc4-2015-417f-a8e2-4899a27a09de",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/.claude/sessions/review_reviewer_1_7624f219",
  "sessionId": "98d2b939-6454-4d7d-877f-2c64a5a37485",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011pmtVu66V2M1KDfxLsGtDp",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 747,
      "cache_creation_input_tokens": 836,
      "cache_read_input_tokens": 28797,
      "output_tokens": 414,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 836,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 747,
          "output_tokens": 414,
          "cache_read_input_tokens": 28797,
          "cache_creation_input_tokens": 836,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 836
          },
          "type": "message"
        }
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

_source line 24 · 2026-05-19T12:51:50.278Z_

<details><summary>↩ Tool result · `toolu_01WJyV8SgYtHH5U7z1BRMLJo`</summary>

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
14	The \texttt{exception\_only} format collapses passing solutions into identical rows (39.45\% train, 48.99\% test duplicates); these duplicates arise from multiple candidate solutions per problem, with the train--test split enforced at the problem level (472 train / 119 test problems, zero crossover; Appendix~\ref{sec:dedup_stats}).
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
  "parentUuid": "ffdc119d-5e87-46fa-a3a8-0d7b70b7fcbd",
  "isSidechain": false,
  "promptId": "e3f72197-8c21-47a9-99b8-7cd49faae750",
  "type": "user",
  "uuid": "beb485dd-3945-46de-8cce-f77a28488313",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/method.tex",
      "content": "\\section{Method}\n\n\\subsection{Task Definition}\n\nWe study \\emph{verdict prediction}: given a Python function, a test input, and an optional execution trace, predict whether the test passes or fails.\nThe model produces a single token (\\texttt{pass} or \\texttt{fail}), making this a binary classification task.\nUnlike code generation \\citep{chen2025tracepile} or output prediction \\citep{gu2024cruxeval}, verdict prediction isolates the model's ability to detect faults from its ability to simulate execution.\n\n\\subsection{Dataset}\n\\label{sec:dataset}\n\nWe sampled 10 candidate solutions per problem from Qwen-2.5-Coder-7B-Instruct (temperature 0.8, top\\_p 0.95) for 591 problems from HumanEval \\citep{chen2021evaluating} (164) and MBPP-sanitized \\citep{austin2021program} (427), executed each against canonical tests with \\texttt{sys.settrace} to obtain line-level traces and pass/fail verdicts, yielding 5,910 pairs (67\\% pass, 33\\% fail).\nThe dataset is split 80/20 by problem ID into 4,720 training and 1,190 test samples (majority baseline: 71.51\\%).\nThe \\texttt{exception\\_only} format collapses passing solutions into identical rows (39.45\\% train, 48.99\\% test duplicates); these duplicates arise from multiple candidate solutions per problem, with the train--test split enforced at the problem level (472 train / 119 test problems, zero crossover; Appendix~\\ref{sec:dedup_stats}).\n\n\\subsection{Trace Representations}\n\nWe define seven conditions that vary the trace information available (Figure~\\ref{fig:trace_overview}):\n\\begin{itemize}\n\\item \\texttt{no\\_trace}: Source code and test input only.\n\\item \\texttt{full\\_trace}: Complete line-by-line trace with variable states.\n\\item \\texttt{VOTA}: Exception events + assertion-point comparisons + loop compression.\n\\item \\texttt{exception\\_only}: Only exception/error events.\n\\item \\texttt{ae\\_only}: Only assertion-point actual/expected pairs.\n\\item \\texttt{loop\\_only}: Only loop compression summaries.\n\\item \\texttt{VOTA\\_no\\_ae}: VOTA without assertion-point information.\n\\end{itemize}\n\n\\begin{figure*}[t]\n\\centering\n\\includegraphics[width=\\textwidth]{fig1_trace_overview}\n\\caption{Overview of the verdict prediction pipeline. Source code and a test input are executed to produce a full raw trace. Four conditions vary the trace information: \\texttt{no\\_trace} (75.13\\%), \\texttt{full\\_trace} (81.76\\%), VOTA (99.41\\%), and \\texttt{exception\\_only} (99.83\\%). Accuracies for Qwen-2.5-7B (seed=42, $N{=}1{,}190$).}\n\\label{fig:trace_overview}\n\\end{figure*}\n\n\\subsection{Models and Training}\n\nWe evaluate four models spanning three architecture families: \\textbf{Qwen-2.5-Coder-7B/1.5B-Instruct} \\citep{qwen2025coder}, \\textbf{CodeLlama-13B-Instruct} \\citep{roziere2024code}, and \\textbf{DeepSeek-Coder-6.7B-Instruct} \\citep{deepseek2024coder}, covering a 1.5B--13B parameter range (8.7$\\times$).\nAll conditions use LoRA \\citep{hu2022lora} (rank=16, $\\alpha$=32, dropout=0.05) on all linear layers, 3 epochs, effective batch size 32, LR $2 \\times 10^{-4}$ with linear warmup/decay, max sequence length 2{,}048 tokens.\nSequences exceeding this limit are truncated while preserving the verdict label.\nThe primary seed is 42; seeds 123 and 456 test \\texttt{exception\\_only} robustness (Appendix~\\ref{sec:training_details}).\n\n\\subsection{Loss Ablation}\n\nTo disentangle training signal from input signal quality, we introduce \\texttt{full\\_trace\\_label\\_only}: identical full-trace input but loss computed only on the verdict token (trace positions masked).\nImprovement over standard \\texttt{full\\_trace} is attributable to \\emph{gradient dilution}; the remaining gap to VOTA reflects \\emph{information overload} at inference time.\n",
      "numLines": 47,
      "startLine": 1,
      "totalLines": 47
    }
  },
  "sourceToolAssistantUUID": "ffdc119d-5e87-46fa-a3a8-0d7b70b7fcbd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/.claude/sessions/review_reviewer_1_7624f219",
  "sessionId": "98d2b939-6454-4d7d-877f-2c64a5a37485",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-19T12:51:49.628Z_

<details open><summary>🔧 Tool call — Read · `toolu_01TwVxQDXjYCSrR2Jco1tPrT`</summary>

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
  "parentUuid": "538b1bc4-2015-417f-a8e2-4899a27a09de",
  "isSidechain": false,
  "requestId": "req_011CbBxXZmk8tG2UuzF5HGtE",
  "type": "assistant",
  "uuid": "d1086092-6c84-4e77-83e9-510b723a4ca0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/.claude/sessions/review_reviewer_1_7624f219",
  "sessionId": "98d2b939-6454-4d7d-877f-2c64a5a37485",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011pmtVu66V2M1KDfxLsGtDp",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 747,
      "cache_creation_input_tokens": 836,
      "cache_read_input_tokens": 28797,
      "output_tokens": 414,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 836,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 747,
          "output_tokens": 414,
          "cache_read_input_tokens": 28797,
          "cache_creation_input_tokens": 836,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 836
          },
          "type": "message"
        }
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

_source line 26 · 2026-05-19T12:51:49.645Z_

<details><summary>↩ Tool result · `toolu_01TwVxQDXjYCSrR2Jco1tPrT`</summary>

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
11	\usepackage{algorithm}
12	\usepackage{algorithmic}
13	
14	\title{Exception Events Are All You Need: \\Component Ablation for Trace-Based Verdict Prediction}
15	\author{Anonymous ACL submission}
16	
17	\begin{document}
18	\maketitle
19	
20	\begin{abstract}
21	Execution traces are increasingly used to enhance code language models, yet more trace information does not mean better performance.
22	We present the first systematic component ablation of trace representations for verdict prediction (classifying whether a test passes or fails) across four models, three architecture families, and a 1.5B--13B parameter range.
23	Exception events alone achieve ${\geq}$99.83\% accuracy on three of four models (DeepSeek-6.7B 3-seed mean 96.58\% due to one seed exhibiting format collapse), while complete traces plateau at 82--88\% despite containing strictly more information.
24	Training dynamics reveal the mechanism: \texttt{exception\_only} converges to 99.33\% within 50 training steps, while \texttt{full\_trace} oscillates across the entire training (82--89\%) without stable convergence, a signature of overfitting to spurious patterns in verbose content.
25	The performance gap approximately decomposes into information overload (${\sim}$76\%) and gradient dilution (${\sim}$24\%).
26	A tail-truncation budget sweep reveals a phase transition at ${\sim}$500 tokens, and even on silent logic errors (55.5\% of failures), \texttt{exception\_only} maintains 100\% recall because test assertions generate exception events.
27	These results show that information density, not information quantity, determines learning efficiency for trace-based verdict prediction: a compact exception event (median 150 tokens) outperforms traces 10$\times$ longer across all tested scales.
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
55	Training uses parameter-efficient LoRA fine-tuning on two RTX PRO 6000 Blackwell GPUs, with each experiment using a single GPU.
56	Total compute is approximately 320 GPU-hours across all conditions, models, seeds, and iterative refinements (including approximately 170 hours for successful experiments; individual runs range from 0.5h for small models to 2.2h for CodeLlama-13B, with the total reflecting 4 models $\times$ multiple conditions $\times$ multiple seeds $\times$ iterative development).
57	We do not foresee direct negative societal impacts from this work; verdict prediction is a developer-facing tool for automated testing.
58	
59	\bibliography{references}
60	
61	\appendix
62	\input{appendix}
63	
64	\end{document}
65	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d1086092-6c84-4e77-83e9-510b723a4ca0",
  "isSidechain": false,
  "promptId": "e3f72197-8c21-47a9-99b8-7cd49faae750",
  "type": "user",
  "uuid": "c0a56a5a-9d7a-4541-a705-7e8f5ffe2eda",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/main.tex",
      "content": "\\documentclass[11pt,a4paper]{article}\n\\usepackage[review]{acl}\n% \\usepackage{acl}  % uncomment for camera-ready (remove [review])\n\\usepackage{times,latexsym}\n\\usepackage{amsmath,amssymb}\n\\usepackage{graphicx}\n\\graphicspath{{../../figures/paper/}}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{xcolor}\n\\usepackage{algorithm}\n\\usepackage{algorithmic}\n\n\\title{Exception Events Are All You Need: \\\\Component Ablation for Trace-Based Verdict Prediction}\n\\author{Anonymous ACL submission}\n\n\\begin{document}\n\\maketitle\n\n\\begin{abstract}\nExecution traces are increasingly used to enhance code language models, yet more trace information does not mean better performance.\nWe present the first systematic component ablation of trace representations for verdict prediction (classifying whether a test passes or fails) across four models, three architecture families, and a 1.5B--13B parameter range.\nException events alone achieve ${\\geq}$99.83\\% accuracy on three of four models (DeepSeek-6.7B 3-seed mean 96.58\\% due to one seed exhibiting format collapse), while complete traces plateau at 82--88\\% despite containing strictly more information.\nTraining dynamics reveal the mechanism: \\texttt{exception\\_only} converges to 99.33\\% within 50 training steps, while \\texttt{full\\_trace} oscillates across the entire training (82--89\\%) without stable convergence, a signature of overfitting to spurious patterns in verbose content.\nThe performance gap approximately decomposes into information overload (${\\sim}$76\\%) and gradient dilution (${\\sim}$24\\%).\nA tail-truncation budget sweep reveals a phase transition at ${\\sim}$500 tokens, and even on silent logic errors (55.5\\% of failures), \\texttt{exception\\_only} maintains 100\\% recall because test assertions generate exception events.\nThese results show that information density, not information quantity, determines learning efficiency for trace-based verdict prediction: a compact exception event (median 150 tokens) outperforms traces 10$\\times$ longer across all tested scales.\n\\end{abstract}\n\n\\input{introduction}\n\\input{method}\n\\input{experiments}\n\\input{discussion}\n\\input{related_work}\n\\input{conclusion}\n\n\\section*{Limitations}\n\nOur study has several limitations.\nFirst, our primary experiments use a single dataset (591 problems from HumanEval and MBPP-sanitized); while a cross-dataset evaluation on DebugBench (\\S\\ref{sec:debugbench}) confirms that exception dominance generalizes to synthetically injected bugs, generalization to other languages, larger codebases, or real-world fault distributions remains untested.\nSecond, while we evaluate four models spanning 1.5B to 13B parameters across three architecture families, all are code-specialized; generalization to general-purpose models or larger scales remains untested.\nThird, DeepSeek \\texttt{exception\\_only} exhibits seed-dependent variance: 2/3 seeds achieve 99.33\\% while seed 123 yields 91.09\\% ($\\sigma{=}4.76$pp, $n{=}3$), which we hypothesize reflects LoRA initialization sensitivity in DeepSeek-Coder, though direct evidence is lacking (fail recall = 70.5\\% for the outlier vs.\\ 100\\% for others).\nQwen \\texttt{exception\\_only} shows perfect seed robustness ($\\sigma{=}0$, $n{=}3$), but Qwen \\texttt{ae\\_only} also exhibits seed variance ($\\sigma{=}$0.40pp; seed 123 = 99.08\\% vs.\\ seeds 42/456 = 99.92\\%), though far smaller than DeepSeek's ($\\sigma{=}$4.76pp).\nWhether training stabilization techniques can eliminate DeepSeek's seed sensitivity is unexplored; other conditions use a single seed.\nFourth, the initial DeepSeek \\texttt{full\\_trace} run was invalidated by context overflow; a re-run with extended context yields 79.16\\% (CI [76.80\\%, 81.30\\%]), 2.60pp below Qwen (Table~\\ref{tab:cross_model}).\nFifth, the candidate solutions were generated by Qwen-2.5-Coder-7B-Instruct, which also serves as one of our evaluation models; this does not affect verdict prediction but may influence the pass/fail distribution.\nSixth, self-familiarity bias may inflate absolute accuracy: both Qwen-2.5-Coder and DeepSeek-Coder were likely exposed to HumanEval and MBPP solutions during pretraining, so the models may partially recognize solutions rather than purely reasoning from trace signals; our cross-dataset evaluation on DebugBench mitigates but does not eliminate this concern.\nSeventh, the error distribution in our test set may not reflect real-world fault distributions: exceptions (especially \\texttt{TypeError}, \\texttt{ValueError}) dominate LLM-generated failures, but production code may exhibit a broader spectrum of silent logic errors where no exception is raised, potentially reducing the effectiveness of exception-based verdict prediction.\nFinally, our analysis is limited to verdict prediction; whether exception dominance extends to other classification tasks or generation tasks is an open question.\n\n\\section*{Ethics Statement}\n\nThis work uses publicly available benchmarks (HumanEval, MBPP-sanitized, DebugBench) and does not involve human subjects, crowdsourced annotations, or personally identifiable information.\nAll models evaluated are open-source and publicly accessible.\nTraining uses parameter-efficient LoRA fine-tuning on two RTX PRO 6000 Blackwell GPUs, with each experiment using a single GPU.\nTotal compute is approximately 320 GPU-hours across all conditions, models, seeds, and iterative refinements (including approximately 170 hours for successful experiments; individual runs range from 0.5h for small models to 2.2h for CodeLlama-13B, with the total reflecting 4 models $\\times$ multiple conditions $\\times$ multiple seeds $\\times$ iterative development).\nWe do not foresee direct negative societal impacts from this work; verdict prediction is a developer-facing tool for automated testing.\n\n\\bibliography{references}\n\n\\appendix\n\\input{appendix}\n\n\\end{document}\n",
      "numLines": 65,
      "startLine": 1,
      "totalLines": 65
    }
  },
  "sourceToolAssistantUUID": "d1086092-6c84-4e77-83e9-510b723a4ca0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/.claude/sessions/review_reviewer_1_7624f219",
  "sessionId": "98d2b939-6454-4d7d-877f-2c64a5a37485",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-19T12:51:50.106Z_

<details open><summary>🔧 Tool call — Read · `toolu_01BNNu3Labtmj4KXyRAs6i88`</summary>

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
  "parentUuid": "c0a56a5a-9d7a-4541-a705-7e8f5ffe2eda",
  "isSidechain": false,
  "requestId": "req_011CbBxXZmk8tG2UuzF5HGtE",
  "type": "assistant",
  "uuid": "45bd87b2-7a1b-4ef8-bbf5-835fdfe848d6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/.claude/sessions/review_reviewer_1_7624f219",
  "sessionId": "98d2b939-6454-4d7d-877f-2c64a5a37485",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011pmtVu66V2M1KDfxLsGtDp",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 747,
      "cache_creation_input_tokens": 836,
      "cache_read_input_tokens": 28797,
      "output_tokens": 414,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 836,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 747,
          "output_tokens": 414,
          "cache_read_input_tokens": 28797,
          "cache_creation_input_tokens": 836,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 836
          },
          "type": "message"
        }
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

_source line 28 · 2026-05-19T12:51:50.111Z_

<details><summary>↩ Tool result · `toolu_01BNNu3Labtmj4KXyRAs6i88`</summary>

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
14	The results are counterintuitive: complete traces (82--88\%) underperform a single compact component (${\geq}$99\%) despite containing strictly more information, because verbose content drowns the diagnostic signal.
15	
16	\textbf{Exception events alone achieve ${\geq}$99.83\% verdict accuracy on three of four models (${\geq}$99.33\% on 2/3 seeds for the fourth; one seed reaches 100\%).}
17	DeepSeek-6.7B is the exception: its 3-seed mean is 96.58\% ($\pm$4.76pp) due to one seed exhibiting format collapse (fail recall = 70.5\%), though even this outlier outperforms VOTA (84.45\%) by 6.64pp.
18	This near-perfect accuracy holds from 1.5B to 13B parameters, while the code-only baseline (\texttt{no\_trace}) varies from 67.3\% to 76.5\% with strong scale dependence.
19	Training dynamics expose the mechanism (Figure~\ref{fig:training_dynamics}): \texttt{exception\_only} converges to 99.33\% within 50 training steps and saturates at 99.83\% by step 150, while \texttt{full\_trace} oscillates between 82\% and 89\% across the entire training without stable convergence, consistent with overfitting to spurious patterns in verbose content.
20	
21	Adding trace information beyond exceptions provides no benefit and can degrade performance: VOTA (3-seed mean 99.05\%) underperforms \texttt{exception\_only} (99.83\%) on Qwen-7B, with the gap reaching 14.96pp on DeepSeek due to tokenizer-driven truncation.
22	The performance gap approximately decomposes into information overload (${\sim}$76\%) and gradient dilution (${\sim}$24\%).
23	A tail-truncation budget sweep across four models reveals a phase transition at ${\sim}$500 tokens, with \texttt{tail\_2048} recovering 95--98\% of \texttt{exception\_only}'s accuracy.
24	Even on silent logic errors (55.5\% of failures), \texttt{exception\_only} maintains 100\% recall because test assertions generate exception events.
25	
26	Our contributions:
27	\begin{enumerate}
28	\item \textbf{Exception events are the minimal sufficient signal for verdict prediction on LLM-generated code}: ${\geq}$99.83\% on three of four models, ${\geq}$99.33\% on 2/3 DeepSeek seeds (1.5B--13B, three families), with ${\sim}$91\% of the signal being semantic rather than format-driven (\S\ref{sec:cross_model}, \S\ref{sec:nomarker}). Cross-dataset evaluation on DebugBench ($N{=}426$) yields 100\% (\S\ref{sec:debugbench}).
29	\item \textbf{Training dynamics reveal the convergence mechanism}: \texttt{exception\_only} converges within 50 steps while \texttt{full\_trace} oscillates (82--89\%) without stable convergence, consistent with overfitting to verbose content. SFT on exception events closes a 6--49pp zero-shot gap across all four models (\S\ref{sec:ablation}, Appendix~\ref{sec:training_dynamics}).
30	\item \textbf{Richer traces provide no additional benefit}: We approximately decompose the performance gap into gradient dilution (${\sim}$24\%) and information overload (${\sim}$76\%), based on Qwen-7B (3 seeds). A budget sweep across four models reveals a phase transition at ${\sim}$500 tail tokens, with \texttt{tail\_2048} recovering 95--98\% of \texttt{exception\_only} (\S\ref{sec:density}, \S\ref{sec:trace_length}).
31	\item \textbf{Two-tier diagnostic hierarchy (observed on Qwen-7B)}: Tier~1 signals (exceptions, assertions) individually achieve ${\geq}$99\%; Tier~2 (loop compression) reaches 86.1\%, still +10.9pp over no trace. Cross-model \texttt{exception\_only} consistency suggests this hierarchy may generalize, though direct verification on other models remains future work (\S\ref{sec:ablation}).
32	\end{enumerate}
33	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "45bd87b2-7a1b-4ef8-bbf5-835fdfe848d6",
  "isSidechain": false,
  "promptId": "e3f72197-8c21-47a9-99b8-7cd49faae750",
  "type": "user",
  "uuid": "cca11100-8b7b-4196-b50e-b7e369689b99",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/introduction.tex",
      "content": "\\section{Introduction}\n\nExecution traces (line-by-line records of a program's runtime behavior) have emerged as a promising input modality for code language models \\citep{chen2025tracepile,ding2024traced,wang2025dcsh,ni2024next}.\nYet feeding thousands of trace lines to a model can be no better than feeding none: the diagnostic signal drowns in routine execution steps.\n\\emph{Which trace components actually carry the signal that matters?}\n\nPrior work found no single trace representation consistently outperforms others \\citep{wang2025dcsh}, but focused on generation-oriented tasks.\n\\emph{Verdict prediction}, classifying whether a test passes or fails, is fundamentally different: it is fault detection, not generation.\nThe model need not simulate execution; it need only determine whether something went wrong.\nThis distinction suggests that a small, fault-specific trace component may suffice.\n\nWe test this hypothesis through the first systematic component ablation of trace representations for verdict prediction.\nUsing 591 problems from HumanEval \\citep{chen2021evaluating} and MBPP-sanitized \\citep{austin2021program}, we decompose a multi-component trace representation (VOTA: exception events + assertion-point comparisons + loop compression) into individual components across four models spanning 1.5B to 13B parameters and three architecture families: Qwen-2.5-Coder-7B/1.5B-Instruct \\citep{qwen2025coder}, CodeLlama-13B-Instruct \\citep{roziere2024code}, and DeepSeek-Coder-6.7B-Instruct \\citep{deepseek2024coder}.\nThe results are counterintuitive: complete traces (82--88\\%) underperform a single compact component (${\\geq}$99\\%) despite containing strictly more information, because verbose content drowns the diagnostic signal.\n\n\\textbf{Exception events alone achieve ${\\geq}$99.83\\% verdict accuracy on three of four models (${\\geq}$99.33\\% on 2/3 seeds for the fourth; one seed reaches 100\\%).}\nDeepSeek-6.7B is the exception: its 3-seed mean is 96.58\\% ($\\pm$4.76pp) due to one seed exhibiting format collapse (fail recall = 70.5\\%), though even this outlier outperforms VOTA (84.45\\%) by 6.64pp.\nThis near-perfect accuracy holds from 1.5B to 13B parameters, while the code-only baseline (\\texttt{no\\_trace}) varies from 67.3\\% to 76.5\\% with strong scale dependence.\nTraining dynamics expose the mechanism (Figure~\\ref{fig:training_dynamics}): \\texttt{exception\\_only} converges to 99.33\\% within 50 training steps and saturates at 99.83\\% by step 150, while \\texttt{full\\_trace} oscillates between 82\\% and 89\\% across the entire training without stable convergence, consistent with overfitting to spurious patterns in verbose content.\n\nAdding trace information beyond exceptions provides no benefit and can degrade performance: VOTA (3-seed mean 99.05\\%) underperforms \\texttt{exception\\_only} (99.83\\%) on Qwen-7B, with the gap reaching 14.96pp on DeepSeek due to tokenizer-driven truncation.\nThe performance gap approximately decomposes into information overload (${\\sim}$76\\%) and gradient dilution (${\\sim}$24\\%).\nA tail-truncation budget sweep across four models reveals a phase transition at ${\\sim}$500 tokens, with \\texttt{tail\\_2048} recovering 95--98\\% of \\texttt{exception\\_only}'s accuracy.\nEven on silent logic errors (55.5\\% of failures), \\texttt{exception\\_only} maintains 100\\% recall because test assertions generate exception events.\n\nOur contributions:\n\\begin{enumerate}\n\\item \\textbf{Exception events are the minimal sufficient signal for verdict prediction on LLM-generated code}: ${\\geq}$99.83\\% on three of four models, ${\\geq}$99.33\\% on 2/3 DeepSeek seeds (1.5B--13B, three families), with ${\\sim}$91\\% of the signal being semantic rather than format-driven (\\S\\ref{sec:cross_model}, \\S\\ref{sec:nomarker}). Cross-dataset evaluation on DebugBench ($N{=}426$) yields 100\\% (\\S\\ref{sec:debugbench}).\n\\item \\textbf{Training dynamics reveal the convergence mechanism}: \\texttt{exception\\_only} converges within 50 steps while \\texttt{full\\_trace} oscillates (82--89\\%) without stable convergence, consistent with overfitting to verbose content. SFT on exception events closes a 6--49pp zero-shot gap across all four models (\\S\\ref{sec:ablation}, Appendix~\\ref{sec:training_dynamics}).\n\\item \\textbf{Richer traces provide no additional benefit}: We approximately decompose the performance gap into gradient dilution (${\\sim}$24\\%) and information overload (${\\sim}$76\\%), based on Qwen-7B (3 seeds). A budget sweep across four models reveals a phase transition at ${\\sim}$500 tail tokens, with \\texttt{tail\\_2048} recovering 95--98\\% of \\texttt{exception\\_only} (\\S\\ref{sec:density}, \\S\\ref{sec:trace_length}).\n\\item \\textbf{Two-tier diagnostic hierarchy (observed on Qwen-7B)}: Tier~1 signals (exceptions, assertions) individually achieve ${\\geq}$99\\%; Tier~2 (loop compression) reaches 86.1\\%, still +10.9pp over no trace. Cross-model \\texttt{exception\\_only} consistency suggests this hierarchy may generalize, though direct verification on other models remains future work (\\S\\ref{sec:ablation}).\n\\end{enumerate}\n",
      "numLines": 33,
      "startLine": 1,
      "totalLines": 33
    }
  },
  "sourceToolAssistantUUID": "45bd87b2-7a1b-4ef8-bbf5-835fdfe848d6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/.claude/sessions/review_reviewer_1_7624f219",
  "sessionId": "98d2b939-6454-4d7d-877f-2c64a5a37485",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-19T12:51:50.274Z_

<details open><summary>🔧 Tool call — Read · `toolu_01WJyV8SgYtHH5U7z1BRMLJo`</summary>

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
  "parentUuid": "cca11100-8b7b-4196-b50e-b7e369689b99",
  "isSidechain": false,
  "requestId": "req_011CbBxXZmk8tG2UuzF5HGtE",
  "type": "assistant",
  "uuid": "ffdc119d-5e87-46fa-a3a8-0d7b70b7fcbd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/.claude/sessions/review_reviewer_1_7624f219",
  "sessionId": "98d2b939-6454-4d7d-877f-2c64a5a37485",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011pmtVu66V2M1KDfxLsGtDp",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 747,
      "cache_creation_input_tokens": 836,
      "cache_read_input_tokens": 28797,
      "output_tokens": 414,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 836,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 747,
          "output_tokens": 414,
          "cache_read_input_tokens": 28797,
          "cache_creation_input_tokens": 836,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 836
          },
          "type": "message"
        }
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
  "lastPrompt": "[Round 1 审稿请求]: 你是 Reviewer 1，负责 **方法严谨性 + 实验有效性**。  ## 论文信息 - **标题**: \"Exception Events Are All You Need: Component Ablation for Trace-Based Verdict Prediction\" - **Venue**: EMNLP 2026 (ARR May 2026)…",
  "leafUuid": "beb485dd-3945-46de-8cce-f77a28488313",
  "sessionId": "98d2b939-6454-4d7d-877f-2c64a5a37485"
}
```

---

### Runtime record

_source line 31_

```json
{
  "type": "ai-title",
  "aiTitle": "Review trace-based verdict prediction paper methodology",
  "sessionId": "98d2b939-6454-4d7d-877f-2c64a5a37485"
}
```

---

### Tool result

_source line 32 · 2026-05-19T12:51:54.540Z_

<details><summary>↩ Tool result · `toolu_01YWKwYvLvp6YLuLKmdhYnZq`</summary>

```text
# ARR Review Form Criteria Summary

Based on the guidelines provided, here's what I found regarding the review form structure:

## Scoring Dimensions

The document states that **"starting with February 2025, ARR reviewers are asked to provide three scores: soundness, excitement, and overall recommendation."**

### 1. **Soundness Score**
The guidelines emphasize that **"soundness scores must be justified by the text of the review."** Low soundness scores require explicit justification in the review content; otherwise, the review lacks credibility.

### 2. **Excitement Score**
This dimension captures subjective interest. The guidelines note: **"Such preferences are more subjective and should be reflected in a separate excitement score, which is orthogonal to the assessment of the soundness."** Personal taste in this category doesn't require explicit reasoning.

### 3. **Overall Assessment Score**
Described as **"an explicit recommendation for the outcome of this paper, if it were committed to an *ACL venue."** This composite score reflects soundness, excitement, novelty, and potential impact combined.

## Key Instructions

- Soundness and overall assessment must align with review justifications
- Excitement scores can be subjective without detailed explanation
- Papers can be sound yet unexciting, or exciting yet have limitations
- All three dimensions inform the final acceptance decision

**Note:** The document doesn't specify the exact numerical scale (e.g., 1-5 or 1-10) for these scores.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "538b1bc4-2015-417f-a8e2-4899a27a09de",
  "isSidechain": false,
  "promptId": "e3f72197-8c21-47a9-99b8-7cd49faae750",
  "type": "user",
  "uuid": "6a94304f-20ba-472b-810b-db7f3f770821",
  "toolUseResult": {
    "bytes": 100603,
    "code": 200,
    "codeText": "OK",
    "result": "# ARR Review Form Criteria Summary\n\nBased on the guidelines provided, here's what I found regarding the review form structure:\n\n## Scoring Dimensions\n\nThe document states that **\"starting with February 2025, ARR reviewers are asked to provide three scores: soundness, excitement, and overall recommendation.\"**\n\n### 1. **Soundness Score**\nThe guidelines emphasize that **\"soundness scores must be justified by the text of the review.\"** Low soundness scores require explicit justification in the review content; otherwise, the review lacks credibility.\n\n### 2. **Excitement Score**\nThis dimension captures subjective interest. The guidelines note: **\"Such preferences are more subjective and should be reflected in a separate excitement score, which is orthogonal to the assessment of the soundness.\"** Personal taste in this category doesn't require explicit reasoning.\n\n### 3. **Overall Assessment Score**\nDescribed as **\"an explicit recommendation for the outcome of this paper, if it were committed to an *ACL venue.\"** This composite score reflects soundness, excitement, novelty, and potential impact combined.\n\n## Key Instructions\n\n- Soundness and overall assessment must align with review justifications\n- Excitement scores can be subjective without detailed explanation\n- Papers can be sound yet unexciting, or exciting yet have limitations\n- All three dimensions inform the final acceptance decision\n\n**Note:** The document doesn't specify the exact numerical scale (e.g., 1-5 or 1-10) for these scores.",
    "durationMs": 5892,
    "url": "https://aclrollingreview.org/reviewerguidelines"
  },
  "sourceToolAssistantUUID": "538b1bc4-2015-417f-a8e2-4899a27a09de",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/.claude/sessions/review_reviewer_1_7624f219",
  "sessionId": "98d2b939-6454-4d7d-877f-2c64a5a37485",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 33 · 2026-05-19T12:51:54.551Z_

```json
{
  "parentUuid": "6a94304f-20ba-472b-810b-db7f3f770821",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "f2deeb54-0e21-412b-a48b-24ff6b34b5ad",
  "timestamp": "2026-05-19T12:51:54.551Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/.claude/sessions/review_reviewer_1_7624f219",
  "sessionId": "98d2b939-6454-4d7d-877f-2c64a5a37485",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 34 · 2026-05-19T12:52:08.836Z_

<details><summary>Logged reasoning block</summary>

```text
Let me continue reading the experiments, discussion, related work, conclusion, and appendix sections.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f2deeb54-0e21-412b-a48b-24ff6b34b5ad",
  "isSidechain": false,
  "requestId": "req_011CbBxYZacdvvTopGQWJJSJ",
  "type": "assistant",
  "uuid": "3183b219-4e60-4092-ba26-4f990c4e3eb2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/.claude/sessions/review_reviewer_1_7624f219",
  "sessionId": "98d2b939-6454-4d7d-877f-2c64a5a37485",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015epz2VUxFsL8CTLMw4NsRx",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 4545,
      "cache_creation_input_tokens": 1625,
      "cache_read_input_tokens": 29633,
      "output_tokens": 354,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1625,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 4545,
          "output_tokens": 354,
          "cache_read_input_tokens": 29633,
          "cache_creation_input_tokens": 1625,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1625
          },
          "type": "message"
        }
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

_source line 35 · 2026-05-19T12:52:09.805Z_

继续读取其余章节和 ARR 评分标准详情。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3183b219-4e60-4092-ba26-4f990c4e3eb2",
  "isSidechain": false,
  "requestId": "req_011CbBxYZacdvvTopGQWJJSJ",
  "type": "assistant",
  "uuid": "d998d8f8-3054-48d5-ae12-7e7faa3e7f77",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/.claude/sessions/review_reviewer_1_7624f219",
  "sessionId": "98d2b939-6454-4d7d-877f-2c64a5a37485",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015epz2VUxFsL8CTLMw4NsRx",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 4545,
      "cache_creation_input_tokens": 1625,
      "cache_read_input_tokens": 29633,
      "output_tokens": 354,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1625,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 4545,
          "output_tokens": 354,
          "cache_read_input_tokens": 29633,
          "cache_creation_input_tokens": 1625,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1625
          },
          "type": "message"
        }
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

_source line 36 · 2026-05-19T12:52:11.710Z_

<details open><summary>🔧 Tool call — Read · `toolu_01JebXLJDTY5KCc5cfSuNqaE`</summary>

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
  "parentUuid": "d998d8f8-3054-48d5-ae12-7e7faa3e7f77",
  "isSidechain": false,
  "requestId": "req_011CbBxYZacdvvTopGQWJJSJ",
  "type": "assistant",
  "uuid": "dba4834a-f10f-40d4-bad5-df17bdf2741b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/.claude/sessions/review_reviewer_1_7624f219",
  "sessionId": "98d2b939-6454-4d7d-877f-2c64a5a37485",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015epz2VUxFsL8CTLMw4NsRx",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 4545,
      "cache_creation_input_tokens": 1625,
      "cache_read_input_tokens": 29633,
      "output_tokens": 354,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1625,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 4545,
          "output_tokens": 354,
          "cache_read_input_tokens": 29633,
          "cache_creation_input_tokens": 1625,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1625
          },
          "type": "message"
        }
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

_source line 37 · 2026-05-19T12:52:13.107Z_

<details><summary>↩ Tool result · `toolu_01No4BFkgoFwapGQwQgUSWvS`</summary>

```text
1	\section{Conclusion}
2	
3	We presented the first systematic component ablation of trace representations for verdict prediction across four models (1.5B--13B, three families).
4	Exception events alone achieve ${\geq}$99.83\% on three of four models while complete traces plateau at 82--88\%: \texttt{exception\_only} converges within 50 steps while \texttt{full\_trace} oscillates without stable convergence, with the gap decomposing into information overload (${\sim}$76\%) and gradient dilution (${\sim}$24\%) on Qwen-7B (3 seeds).
5	Cross-dataset evaluation on DebugBench confirms generalization (100\%, $N{=}426$), and ${\sim}$91\% of the signal is semantic rather than format-driven.
6	
7	Verdict prediction is fault detection, not an information-starved task: the runtime has already surfaced the diagnostic signal, and the model need only determine whether it indicates a terminal fault.
8	This suggests extracting the highest-specificity signal (median 150 tokens) and discarding everything else, though generalization beyond LLM-generated Python code remains open.
9	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e735c19a-92fe-4d23-8f13-123517130f95",
  "isSidechain": false,
  "promptId": "e3f72197-8c21-47a9-99b8-7cd49faae750",
  "type": "user",
  "uuid": "34daa36d-6939-46da-95c1-27b48e83684a",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/conclusion.tex",
      "content": "\\section{Conclusion}\n\nWe presented the first systematic component ablation of trace representations for verdict prediction across four models (1.5B--13B, three families).\nException events alone achieve ${\\geq}$99.83\\% on three of four models while complete traces plateau at 82--88\\%: \\texttt{exception\\_only} converges within 50 steps while \\texttt{full\\_trace} oscillates without stable convergence, with the gap decomposing into information overload (${\\sim}$76\\%) and gradient dilution (${\\sim}$24\\%) on Qwen-7B (3 seeds).\nCross-dataset evaluation on DebugBench confirms generalization (100\\%, $N{=}426$), and ${\\sim}$91\\% of the signal is semantic rather than format-driven.\n\nVerdict prediction is fault detection, not an information-starved task: the runtime has already surfaced the diagnostic signal, and the model need only determine whether it indicates a terminal fault.\nThis suggests extracting the highest-specificity signal (median 150 tokens) and discarding everything else, though generalization beyond LLM-generated Python code remains open.\n",
      "numLines": 9,
      "startLine": 1,
      "totalLines": 9
    }
  },
  "sourceToolAssistantUUID": "e735c19a-92fe-4d23-8f13-123517130f95",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/.claude/sessions/review_reviewer_1_7624f219",
  "sessionId": "98d2b939-6454-4d7d-877f-2c64a5a37485",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-19T12:52:11.715Z_

<details><summary>↩ Tool result · `toolu_01JebXLJDTY5KCc5cfSuNqaE`</summary>

```text
1	\section{Experiments}
2	
3	We evaluate across two research questions:
4	(1)~Do Tier~1 exception signals generalize across models?
5	(2)~What is the relative contribution of each trace component?
6	All experiments use $N{=}1{,}190$ test samples; accuracy is reported with Wilson 95\% CIs.\footnote{Data is partitioned at the problem level (472 train / 119 test problems, zero crossover; \S\ref{sec:dataset}). The \texttt{exception\_only} format collapses passing solutions into identical rows (48.99\% test duplicates; Appendix~\ref{sec:dedup_stats}), but these arise from within-problem variants, not cross-set leakage; deduplication sensitivity analysis confirms 0.00pp delta across all 19 experimental conditions.}
7	Pairwise comparisons use paired bootstrap resampling ($B{=}10{,}000$, seed=42); all differences are significant at $p{<}0.0001$ unless noted.
8	
9	\subsection{Cross-Model Comparison}
10	\label{sec:cross_model}
11	
12	Table~\ref{tab:cross_model} compares four models spanning an 8.7$\times$ parameter range (1.5B--13B) and three architecture families (Qwen, DeepSeek, CodeLlama) under key conditions.
13	
14	\begin{table}[t]
15	\centering
16	\caption{Cross-model verdict accuracy (\%, $N{=}1{,}190$). Bold: best accuracy per model. Multi-seed entries show mean$\pm$std (3 seeds). $^\dag$DeepSeek 3-seed mean 96.58\%$\pm$4.76pp; seed 123 (91.09\%, fail recall = 70.5\%) exhibits format collapse on long inputs (Appendix~\ref{sec:training_dynamics}), reported here as 2-seed mean excluding the outlier. VOTA on Qwen-7B: 3-seed mean 99.05\% (99.41/98.66/99.08\%, $\sigma{=}$0.38). \texttt{ae\_only} tested on Qwen-7B with 3 seeds (99.92/99.08/99.92\%, mean 99.64\%); \texttt{loop\_only} 3 seeds (85.63/85.88/86.64\%, mean 86.05\%). Qwen-1.5B \texttt{exception\_only} confirmed at 99.83\% across all 3 seeds ($\sigma{=}$0). Cross-model validation focused on the primary conditions. Full CIs in Appendix~\ref{sec:full_results}.}
17	\label{tab:cross_model}
18	\small
19	\resizebox{\columnwidth}{!}{%
20	\begin{tabular}{lcccc}
21	\toprule
22	\textbf{Condition} & \textbf{Qwen-7B} & \textbf{Qwen-1.5B} & \textbf{CL-13B} & \textbf{DS-6.7B} \\
23	\midrule
24	exception\_only & \textbf{99.83}{\scriptsize$\pm$0.00} & \textbf{99.83}{\scriptsize$\pm$0.00} & \textbf{99.89}{\scriptsize$\pm$0.10} & \textbf{99.33}$^\dag$ \\
25	ae\_only & 99.64{\scriptsize$\pm$0.49} & --- & --- & --- \\
26	VOTA & 99.05{\scriptsize$\pm$0.38} & 99.58 & 98.57 & 84.45 \\
27	no\_trace & 75.13 & 67.31 & 76.47 & 73.36 \\
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
43	In contrast, \texttt{no\_trace} scales monotonically with capacity: 67.31\% (1.5B) $\to$ 75.13\% (7B) $\to$ 76.47\% (13B), a 9.16pp range that exception events completely eliminate (Figure~\ref{fig:cross_scale}).
44	
45	\begin{figure}[t]
46	\centering
47	\includegraphics[width=\columnwidth]{fig3_cross_model_gap}
48	\caption{Verdict accuracy vs.\ model scale. \texttt{exception\_only} maintains ${\geq}$99.33\% regardless of scale (1.5B--13B), while \texttt{no\_trace} shows monotonic scale sensitivity (+9.16pp from 1.5B to 13B). The \texttt{nomarker} condition (format markers removed) shows no degradation at smaller scale (${\sim}$97.7--97.8\%).}
49	\label{fig:cross_scale}
50	\end{figure}
51	
52	\paragraph{VOTA cross-family variation.}
53	VOTA accuracy varies across families: 99.58\% (Qwen-1.5B) $>$ 99.05\%$\pm$0.38 (Qwen-7B, 3 seeds) $>$ 98.57\% (CodeLlama-13B; CI [97.9, 99.2]) $\gg$ 84.45\% (DeepSeek-6.7B).
54	The CodeLlama result (17 errors) narrows the gap: among models without tokenizer-driven truncation, the VOTA range is only 1.01pp (98.57--99.58\%), suggesting that the 14.96pp DeepSeek deficit is primarily a truncation artifact rather than an inherent model capability limitation (91.7\% of DeepSeek training samples were affected; Appendix~\ref{sec:tokenizer_analysis}).
55	In contrast, \texttt{exception\_only} inputs are compact (median 150 tokens, mean 398 due to verbose fail-class exceptions), making the cross-model comparison clean.
56	
57	\subsection{Component Ablation}
58	\label{sec:ablation}
59	
60	We restrict \texttt{ae\_only} and \texttt{loop\_only} ablations to Qwen-7B, as these component-level analyses target the trace composition mechanism rather than cross-model generalization.
61	Table~\ref{tab:ablation} decomposes VOTA on Qwen-2.5-7B and reveals a two-tier hierarchy on this model; the cross-model consistency of \texttt{exception\_only} (${\geq}$99.33\% on all four models) suggests Tier~1 generalizes, though direct Tier~2 verification on other models remains future work.
62	
63	\begin{table}[t]
64	\centering
65	\caption{Component ablation on Qwen-2.5-7B ($N{=}1{,}190$). Tier~1 signals achieve near-perfect accuracy; combining them (VOTA) slightly dilutes performance. $^\dag$\texttt{ae\_only}: 3-seed mean 99.64\%$\pm$0.49 (seeds 42/123/456: 99.92/99.08/99.92). \texttt{exception\_only}: 99.83\%$\pm$0.00 (3 seeds). $^\S$VOTA: 3-seed mean 99.05\%$\pm$0.38 (99.41/98.66/99.08). $^\ddag$\texttt{loop\_only}: 3-seed mean 86.05\%$\pm$0.52 (85.63/85.88/86.64). Seed variance negatively correlates with information density: $\sigma{=}$0.00 (exception) ${<}$ 0.38 (VOTA) ${<}$ 0.49 (ae) ${<}$ 0.52 (loop).}
66	\label{tab:ablation}
67	\small
68	\resizebox{\columnwidth}{!}{%
69	\begin{tabular}{llccc}
70	\toprule
71	\textbf{Condition} & \textbf{Components} & \textbf{Acc (\%)} & \textbf{95\% CI} & \textbf{Tier} \\
72	\midrule
73	ae\_only & assertion-point & 99.64$^\dag$ & [99.26, 99.87] & 1 \\
74	exception\_only & exception events & \textbf{99.83} & [99.58, 100.00] & 1 \\
75	VOTA & exc+ae+loop & 99.05$^\S$ & [98.49, 99.50] & --- \\
76	VOTA\_no\_ae & exc+loop & 99.41 & [98.90, 99.80] & --- \\
77	loop\_only & loop compression & 86.05$^\ddag$ & [83.97, 87.96] & 2 \\
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
89	Tier~1 signals are individually sufficient: \texttt{exception\_only} (99.83\%$\pm$0.00) exceeds VOTA (99.05\%$\pm$0.38) by +0.78pp (2/3 seeds $p{<}0.05$, all directionally consistent), implying that combining signals introduces noise.
90	Removing assertion points has no effect (\texttt{VOTA\_no\_ae} = 99.41\%, single seed), confirming exception dominance.
91	Tier~2 \texttt{loop\_only} (86.05\%, 3-seed mean) improves 10.92pp over \texttt{no\_trace} ($p{<}0.0001$) but falls far short of Tier~1.
92	\paragraph{Rule-based baseline comparison.}
93	The strongest non-trivial regex heuristic (B4: exception class name matching) achieves 93.61\% accuracy (F1=0.876), trailing SFT \texttt{exception\_only} (99.83\%, F1=0.997) by 6.22pp (McNemar $p{<}0.001$).
94	The gap concentrates on caught-exception boundary cases: regex flags all exception events as failures, while SFT learns to distinguish caught exceptions (benign, inside \texttt{try/except}) from uncaught faults, correctly resolving 6/8 boundary samples (Appendix~\ref{sec:regex_baselines}).
95	Across trace formats, SFT consistently outperforms the best applicable regex, from +3.62pp (\texttt{no\_trace} over majority baseline) to +23.86pp (VOTA), with the largest gains on formats requiring semantic interpretation (Appendix~\ref{sec:regex_baselines}).
96	
97	\paragraph{Zero-shot and few-shot LLM baselines.}
98	Zero-shot prompting spans 51.0--93.5\% across four models (42.44pp range), with performance uncorrelated with model size (Qwen-1.5B: 93.45\% vs.\ CodeLlama-13B: 51.01\%).
99	Three-shot ICL on Qwen-7B (90.84\%) improves only 1.76pp and still trails SFT by 8.99pp.
100	SFT compresses this 42.44pp range to 0.56pp (99.33--99.89\%), closing a 6--49pp gap with 4,720 training samples (Appendix~\ref{sec:zeroshot_cross_model}).
101	
102	\subsection{Format Marker Ablation}
103	\label{sec:nomarker}
104	
105	The \texttt{exception\_only} format includes a \texttt{[No exception data in trace]} marker in all pass-class samples (regex baseline B5 exploits this for 99.33\% accuracy; Appendix~\ref{sec:regex_baselines}).
106	To quantify the marker's contribution, we retrain with all format markers removed (\texttt{nomarker} condition).
107	
108	Qwen-7B 3-seed mean: 97.65\% $\pm$ 0.96 (seeds 42/123/456: 96.55/98.32/98.07\%), a drop of 2.18pp from \texttt{exception\_only} (99.83\%).
109	Qwen-1.5B: 97.82\%, drop of 2.01pp.
110	The marker contribution (${\sim}$2pp) accounts for only ${\sim}$9\% of the total exception lift over \texttt{no\_trace} (24.70pp on 7B).
111	Exception events thus provide two signal layers that show no degradation at smaller scale: structural markers (${\sim}$2pp, regex-learnable) and semantic exception content (${\sim}$22pp, requiring SFT to distinguish caught from uncaught exceptions).
112	
113	\subsection{Information Density Decomposition}
114	\label{sec:density}
115	
116	The 17.29pp gap between \texttt{full\_trace} (81.76\%) and VOTA (99.05\%, 3-seed mean) decomposes via \texttt{full\_trace\_label\_only} (85.94\%$\pm$1.12, 3 seeds), which retains the full trace but masks all trace tokens from the loss.
117	
118	\begin{table}[t]
119	\centering
120	\caption{Approximate information density decomposition: gradient dilution (${\sim}$24\%) vs.\ information overload (${\sim}$76\%). \texttt{label\_only} and VOTA are 3-seed means on Qwen-7B.}
121	\label{tab:density}
122	\small
123	\begin{tabular}{lccc}
124	\toprule
125	\textbf{Condition} & \textbf{Acc (\%)} & \textbf{$\Delta$ vs.\ full\_trace} & \textbf{Gap explained} \\
126	\midrule
127	full\_trace & 81.76 & --- & --- \\
128	label\_only & 85.94{\scriptsize$\pm$1.12} & +4.18pp & 24\% \\
129	VOTA & 99.05{\scriptsize$\pm$0.38} & +17.29pp & 100\% \\
130	\bottomrule
131	\end{tabular}
132	\end{table}
133	
134	Gradient dilution accounts for approximately 24\% of the gap (+4.18pp, 3-seed mean): when the model no longer wastes gradient updates on predicting trace tokens, accuracy improves even with identical input.
135	The remaining ${\sim}$76\% (+13.11pp) reflects information overload at inference: the model receives thousands of irrelevant trace lines that compete for attention with the diagnostic signal, regardless of loss design.
136	This asymmetry implies that trace compression methods should prioritize \emph{content selection} (removing irrelevant lines) over \emph{loss engineering} (masking non-target tokens), as the larger bottleneck is what the model sees, not how it is trained.
137	The two factors may interact, so this decomposition is approximate.
138	Label-only loss simultaneously changes multiple optimization dynamics (effective gradient norm, implicit regularization from trace token prediction); the 24\%/76\% attribution should be interpreted as an approximate decomposition rather than a strict causal partition.
139	This analysis uses 3 seeds on a single model (Qwen-7B); cross-model validation remains future work.
140	
141	\subsection{Additional Analyses}
142	\label{sec:additional}
143	
144	\paragraph{Trace length ablation.}
145	\label{sec:trace_length}
146	Varying the head-truncated trace token budget (256--no limit) on Qwen-7B yields accuracy in a narrow 77.2\%--81.8\% band with a non-monotonic pattern: 1024-token prefixes (77.23\%) underperform 512-token prefixes (80.42\%, $p{=}0.002$), because mid-length prefixes retain enough irrelevant content to mislead the model while discarding diagnostic events near the trace terminus (Appendix~\ref{sec:trace_length_full}).
147	This non-monotonicity is specific to head-truncation; under tail-truncation, accuracy increases monotonically for two of three models (Table~\ref{tab:tail_cross_model} in Appendix), with only DeepSeek showing a mild architecture-specific reversal at tail-1024$\to$tail-2048 ($-$1.5pp).
148	
149	\paragraph{Truncation direction and budget curve.}
150	Tail-truncation (retaining the last $k$ tokens) dramatically outperforms head-truncation: among the three models with complete data, tail-2048 exceeds head-2048 by 15.5--22.6pp, with the gap widening at smaller scale (Qwen-1.5B: +22.6pp vs.\ Qwen-7B: +15.5pp; Appendix~\ref{sec:trace_length_full}, Table~\ref{tab:head_vs_tail}).
151	All four models' head-2048 accuracies converge into a narrow 75.3--81.8\% band (6.5pp), comparable to the tail-256 band (72.6--78.9\%, 6.3pp), indicating that signal-poor conditions produce a shared performance floor regardless of scale or architecture.
152	
153	A cross-model budget sweep across four models and three architecture families reveals a phase transition localized between 384 and 512 tail tokens.
154	At tail-384, all models remain near baseline (73.6--82.9\%, only +1.0--6.5pp over tail-256); the steep jump occurs at 384$\to$512 (+11.0--22.0pp), crossing from near-baseline to near-ceiling (${\sim}$94--98\%).
155	This localizes the critical threshold to ${\sim}$400--500 tokens, matching the typical exception traceback length (Table~\ref{tab:tail_cross_model}).
156	Beyond 512 tokens, accuracy converges further: multi-seed validation across all 12 model$\times$seed combinations confirms all tail-512 accuracies fall within a 4.63pp band [93.61\%, 98.24\%] (Table~\ref{tab:tail512_seeds}); at tail-1024, three models reach 96.5--98.2\%, compressing the 6.3pp cross-model spread observed at tail-256.
157	\texttt{tail\_2048} captures 95--98\% of \texttt{exception\_only}'s accuracy across all completed configurations.
158	The residual 2--5pp gap confirms that semantic extraction (identifying exception type and message) still outperforms positional extraction (retaining a fixed window containing non-diagnostic lines).
159	
160	\paragraph{Calibration.}
161	\label{sec:calibration}
162	Calibration mirrors the tier hierarchy: \texttt{exception\_only} ECE = 0.0027 vs.\ \texttt{no\_trace} ECE = 0.171, a 63$\times$ gap.
163	This calibration advantage generalizes across models: all three tested architectures achieve ECE ${<}$ 0.007 under \texttt{exception\_only} (Appendix~\ref{sec:calibration_full}).
164	
165	\paragraph{Error orthogonality.}
166	\texttt{exception\_only}'s 2 errors have zero overlap with all other conditions' error sets (Jaccard = 0.000), confirming it operates on an independent signal dimension (Appendix~\ref{sec:error_overlap}).
167	
168	\paragraph{Exception type breakdown.}
169	A per-exception-type breakdown (Appendix~\ref{sec:exception_type}) confirms that all standard exception types achieve 100\% accuracy; the only failures arise from \texttt{GeneratorExit}, a benign \texttt{BaseException} subclass.
170	
171	\paragraph{Cross-dataset generalization.}
172	\label{sec:debugbench}
173	On DebugBench \citep{tian2024debugbench} ($N{=}426$), the ranking is preserved: \texttt{exception\_only} 100\%, VOTA 99.77\%, \texttt{no\_trace} 96.71\%; narrow margins reflect a ceiling effect from structurally distinctive mutations (Appendix~\ref{sec:debugbench_full}).
174	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "dba4834a-f10f-40d4-bad5-df17bdf2741b",
  "isSidechain": false,
  "promptId": "e3f72197-8c21-47a9-99b8-7cd49faae750",
  "type": "user",
  "uuid": "08520bd5-0b14-4e34-9e1a-8e3677eb5b09",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/experiments.tex",
      "content": "\\section{Experiments}\n\nWe evaluate across two research questions:\n(1)~Do Tier~1 exception signals generalize across models?\n(2)~What is the relative contribution of each trace component?\nAll experiments use $N{=}1{,}190$ test samples; accuracy is reported with Wilson 95\\% CIs.\\footnote{Data is partitioned at the problem level (472 train / 119 test problems, zero crossover; \\S\\ref{sec:dataset}). The \\texttt{exception\\_only} format collapses passing solutions into identical rows (48.99\\% test duplicates; Appendix~\\ref{sec:dedup_stats}), but these arise from within-problem variants, not cross-set leakage; deduplication sensitivity analysis confirms 0.00pp delta across all 19 experimental conditions.}\nPairwise comparisons use paired bootstrap resampling ($B{=}10{,}000$, seed=42); all differences are significant at $p{<}0.0001$ unless noted.\n\n\\subsection{Cross-Model Comparison}\n\\label{sec:cross_model}\n\nTable~\\ref{tab:cross_model} compares four models spanning an 8.7$\\times$ parameter range (1.5B--13B) and three architecture families (Qwen, DeepSeek, CodeLlama) under key conditions.\n\n\\begin{table}[t]\n\\centering\n\\caption{Cross-model verdict accuracy (\\%, $N{=}1{,}190$). Bold: best accuracy per model. Multi-seed entries show mean$\\pm$std (3 seeds). $^\\dag$DeepSeek 3-seed mean 96.58\\%$\\pm$4.76pp; seed 123 (91.09\\%, fail recall = 70.5\\%) exhibits format collapse on long inputs (Appendix~\\ref{sec:training_dynamics}), reported here as 2-seed mean excluding the outlier. VOTA on Qwen-7B: 3-seed mean 99.05\\% (99.41/98.66/99.08\\%, $\\sigma{=}$0.38). \\texttt{ae\\_only} tested on Qwen-7B with 3 seeds (99.92/99.08/99.92\\%, mean 99.64\\%); \\texttt{loop\\_only} 3 seeds (85.63/85.88/86.64\\%, mean 86.05\\%). Qwen-1.5B \\texttt{exception\\_only} confirmed at 99.83\\% across all 3 seeds ($\\sigma{=}$0). Cross-model validation focused on the primary conditions. Full CIs in Appendix~\\ref{sec:full_results}.}\n\\label{tab:cross_model}\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Condition} & \\textbf{Qwen-7B} & \\textbf{Qwen-1.5B} & \\textbf{CL-13B} & \\textbf{DS-6.7B} \\\\\n\\midrule\nexception\\_only & \\textbf{99.83}{\\scriptsize$\\pm$0.00} & \\textbf{99.83}{\\scriptsize$\\pm$0.00} & \\textbf{99.89}{\\scriptsize$\\pm$0.10} & \\textbf{99.33}$^\\dag$ \\\\\nae\\_only & 99.64{\\scriptsize$\\pm$0.49} & --- & --- & --- \\\\\nVOTA & 99.05{\\scriptsize$\\pm$0.38} & 99.58 & 98.57 & 84.45 \\\\\nno\\_trace & 75.13 & 67.31 & 76.47 & 73.36 \\\\\n\\midrule\nMajority baseline & \\multicolumn{4}{c}{71.51} \\\\\n\\bottomrule\n\\end{tabular}%\n}\n\\end{table}\n\n\\paragraph{Exception dominance across families.}\nUnder \\texttt{exception\\_only}, the Qwen and CodeLlama families achieve ${\\geq}$99.83\\% (mean): Qwen-7B (99.83\\%$\\pm$0.00, 3 seeds), Qwen-1.5B (99.83\\%), and CodeLlama-13B (99.89\\%$\\pm$0.10, 3 seeds; seed 123 achieves 100\\%).\nDeepSeek-6.7B reaches 99.33\\% on 2/3 seeds with one LoRA-sensitivity outlier at 91.09\\% (seed 123; fail recall = 70.5\\%); even the outlier outperforms VOTA (84.45\\%) by 6.64pp.\nExcluding the DeepSeek outlier, the cross-model range is 0.56pp (99.33--99.89\\%), the tightest of any condition.\n\n\\paragraph{Scale invariance of exception signals.}\nException-based accuracy is shared by models spanning 1.5B to 13B parameters (8.7$\\times$): both Qwen-1.5B and CodeLlama-13B achieve 99.83\\%+ on the same representation.\nCodeLlama-13B seed 123 achieves 100\\% (0/1190 errors), confirming that Qwen's two persistent errors (from \\texttt{GeneratorExit}; Appendix~\\ref{sec:irreducible}) are high-probability convergence artifacts rather than hard data limitations.\nIn contrast, \\texttt{no\\_trace} scales monotonically with capacity: 67.31\\% (1.5B) $\\to$ 75.13\\% (7B) $\\to$ 76.47\\% (13B), a 9.16pp range that exception events completely eliminate (Figure~\\ref{fig:cross_scale}).\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{fig3_cross_model_gap}\n\\caption{Verdict accuracy vs.\\ model scale. \\texttt{exception\\_only} maintains ${\\geq}$99.33\\% regardless of scale (1.5B--13B), while \\texttt{no\\_trace} shows monotonic scale sensitivity (+9.16pp from 1.5B to 13B). The \\texttt{nomarker} condition (format markers removed) shows no degradation at smaller scale (${\\sim}$97.7--97.8\\%).}\n\\label{fig:cross_scale}\n\\end{figure}\n\n\\paragraph{VOTA cross-family variation.}\nVOTA accuracy varies across families: 99.58\\% (Qwen-1.5B) $>$ 99.05\\%$\\pm$0.38 (Qwen-7B, 3 seeds) $>$ 98.57\\% (CodeLlama-13B; CI [97.9, 99.2]) $\\gg$ 84.45\\% (DeepSeek-6.7B).\nThe CodeLlama result (17 errors) narrows the gap: among models without tokenizer-driven truncation, the VOTA range is only 1.01pp (98.57--99.58\\%), suggesting that the 14.96pp DeepSeek deficit is primarily a truncation artifact rather than an inherent model capability limitation (91.7\\% of DeepSeek training samples were affected; Appendix~\\ref{sec:tokenizer_analysis}).\nIn contrast, \\texttt{exception\\_only} inputs are compact (median 150 tokens, mean 398 due to verbose fail-class exceptions), making the cross-model comparison clean.\n\n\\subsection{Component Ablation}\n\\label{sec:ablation}\n\nWe restrict \\texttt{ae\\_only} and \\texttt{loop\\_only} ablations to Qwen-7B, as these component-level analyses target the trace composition mechanism rather than cross-model generalization.\nTable~\\ref{tab:ablation} decomposes VOTA on Qwen-2.5-7B and reveals a two-tier hierarchy on this model; the cross-model consistency of \\texttt{exception\\_only} (${\\geq}$99.33\\% on all four models) suggests Tier~1 generalizes, though direct Tier~2 verification on other models remains future work.\n\n\\begin{table}[t]\n\\centering\n\\caption{Component ablation on Qwen-2.5-7B ($N{=}1{,}190$). Tier~1 signals achieve near-perfect accuracy; combining them (VOTA) slightly dilutes performance. $^\\dag$\\texttt{ae\\_only}: 3-seed mean 99.64\\%$\\pm$0.49 (seeds 42/123/456: 99.92/99.08/99.92). \\texttt{exception\\_only}: 99.83\\%$\\pm$0.00 (3 seeds). $^\\S$VOTA: 3-seed mean 99.05\\%$\\pm$0.38 (99.41/98.66/99.08). $^\\ddag$\\texttt{loop\\_only}: 3-seed mean 86.05\\%$\\pm$0.52 (85.63/85.88/86.64). Seed variance negatively correlates with information density: $\\sigma{=}$0.00 (exception) ${<}$ 0.38 (VOTA) ${<}$ 0.49 (ae) ${<}$ 0.52 (loop).}\n\\label{tab:ablation}\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llccc}\n\\toprule\n\\textbf{Condition} & \\textbf{Components} & \\textbf{Acc (\\%)} & \\textbf{95\\% CI} & \\textbf{Tier} \\\\\n\\midrule\nae\\_only & assertion-point & 99.64$^\\dag$ & [99.26, 99.87] & 1 \\\\\nexception\\_only & exception events & \\textbf{99.83} & [99.58, 100.00] & 1 \\\\\nVOTA & exc+ae+loop & 99.05$^\\S$ & [98.49, 99.50] & --- \\\\\nVOTA\\_no\\_ae & exc+loop & 99.41 & [98.90, 99.80] & --- \\\\\nloop\\_only & loop compression & 86.05$^\\ddag$ & [83.97, 87.96] & 2 \\\\\nfull\\_trace & complete trace & 81.76 & [79.70, 83.90] & --- \\\\\nno\\_trace & none & 75.13 & [72.77, 77.48] & --- \\\\\n\\midrule\nRegex (best) & exc.\\ type regex & 93.61 & --- & --- \\\\\n3-shot (Qwen-7B) & in-context learning & 90.84 & --- & --- \\\\\nZero-shot (4 models) & prompting & 51.0--93.5 & --- & --- \\\\\n\\bottomrule\n\\end{tabular}%\n}\n\\end{table}\n\nTier~1 signals are individually sufficient: \\texttt{exception\\_only} (99.83\\%$\\pm$0.00) exceeds VOTA (99.05\\%$\\pm$0.38) by +0.78pp (2/3 seeds $p{<}0.05$, all directionally consistent), implying that combining signals introduces noise.\nRemoving assertion points has no effect (\\texttt{VOTA\\_no\\_ae} = 99.41\\%, single seed), confirming exception dominance.\nTier~2 \\texttt{loop\\_only} (86.05\\%, 3-seed mean) improves 10.92pp over \\texttt{no\\_trace} ($p{<}0.0001$) but falls far short of Tier~1.\n\\paragraph{Rule-based baseline comparison.}\nThe strongest non-trivial regex heuristic (B4: exception class name matching) achieves 93.61\\% accuracy (F1=0.876), trailing SFT \\texttt{exception\\_only} (99.83\\%, F1=0.997) by 6.22pp (McNemar $p{<}0.001$).\nThe gap concentrates on caught-exception boundary cases: regex flags all exception events as failures, while SFT learns to distinguish caught exceptions (benign, inside \\texttt{try/except}) from uncaught faults, correctly resolving 6/8 boundary samples (Appendix~\\ref{sec:regex_baselines}).\nAcross trace formats, SFT consistently outperforms the best applicable regex, from +3.62pp (\\texttt{no\\_trace} over majority baseline) to +23.86pp (VOTA), with the largest gains on formats requiring semantic interpretation (Appendix~\\ref{sec:regex_baselines}).\n\n\\paragraph{Zero-shot and few-shot LLM baselines.}\nZero-shot prompting spans 51.0--93.5\\% across four models (42.44pp range), with performance uncorrelated with model size (Qwen-1.5B: 93.45\\% vs.\\ CodeLlama-13B: 51.01\\%).\nThree-shot ICL on Qwen-7B (90.84\\%) improves only 1.76pp and still trails SFT by 8.99pp.\nSFT compresses this 42.44pp range to 0.56pp (99.33--99.89\\%), closing a 6--49pp gap with 4,720 training samples (Appendix~\\ref{sec:zeroshot_cross_model}).\n\n\\subsection{Format Marker Ablation}\n\\label{sec:nomarker}\n\nThe \\texttt{exception\\_only} format includes a \\texttt{[No exception data in trace]} marker in all pass-class samples (regex baseline B5 exploits this for 99.33\\% accuracy; Appendix~\\ref{sec:regex_baselines}).\nTo quantify the marker's contribution, we retrain with all format markers removed (\\texttt{nomarker} condition).\n\nQwen-7B 3-seed mean: 97.65\\% $\\pm$ 0.96 (seeds 42/123/456: 96.55/98.32/98.07\\%), a drop of 2.18pp from \\texttt{exception\\_only} (99.83\\%).\nQwen-1.5B: 97.82\\%, drop of 2.01pp.\nThe marker contribution (${\\sim}$2pp) accounts for only ${\\sim}$9\\% of the total exception lift over \\texttt{no\\_trace} (24.70pp on 7B).\nException events thus provide two signal layers that show no degradation at smaller scale: structural markers (${\\sim}$2pp, regex-learnable) and semantic exception content (${\\sim}$22pp, requiring SFT to distinguish caught from uncaught exceptions).\n\n\\subsection{Information Density Decomposition}\n\\label{sec:density}\n\nThe 17.29pp gap between \\texttt{full\\_trace} (81.76\\%) and VOTA (99.05\\%, 3-seed mean) decomposes via \\texttt{full\\_trace\\_label\\_only} (85.94\\%$\\pm$1.12, 3 seeds), which retains the full trace but masks all trace tokens from the loss.\n\n\\begin{table}[t]\n\\centering\n\\caption{Approximate information density decomposition: gradient dilution (${\\sim}$24\\%) vs.\\ information overload (${\\sim}$76\\%). \\texttt{label\\_only} and VOTA are 3-seed means on Qwen-7B.}\n\\label{tab:density}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Condition} & \\textbf{Acc (\\%)} & \\textbf{$\\Delta$ vs.\\ full\\_trace} & \\textbf{Gap explained} \\\\\n\\midrule\nfull\\_trace & 81.76 & --- & --- \\\\\nlabel\\_only & 85.94{\\scriptsize$\\pm$1.12} & +4.18pp & 24\\% \\\\\nVOTA & 99.05{\\scriptsize$\\pm$0.38} & +17.29pp & 100\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nGradient dilution accounts for approximately 24\\% of the gap (+4.18pp, 3-seed mean): when the model no longer wastes gradient updates on predicting trace tokens, accuracy improves even with identical input.\nThe remaining ${\\sim}$76\\% (+13.11pp) reflects information overload at inference: the model receives thousands of irrelevant trace lines that compete for attention with the diagnostic signal, regardless of loss design.\nThis asymmetry implies that trace compression methods should prioritize \\emph{content selection} (removing irrelevant lines) over \\emph{loss engineering} (masking non-target tokens), as the larger bottleneck is what the model sees, not how it is trained.\nThe two factors may interact, so this decomposition is approximate.\nLabel-only loss simultaneously changes multiple optimization dynamics (effective gradient norm, implicit regularization from trace token prediction); the 24\\%/76\\% attribution should be interpreted as an approximate decomposition rather than a strict causal partition.\nThis analysis uses 3 seeds on a single model (Qwen-7B); cross-model validation remains future work.\n\n\\subsection{Additional Analyses}\n\\label{sec:additional}\n\n\\paragraph{Trace length ablation.}\n\\label{sec:trace_length}\nVarying the head-truncated trace token budget (256--no limit) on Qwen-7B yields accuracy in a narrow 77.2\\%--81.8\\% band with a non-monotonic pattern: 1024-token prefixes (77.23\\%) underperform 512-token prefixes (80.42\\%, $p{=}0.002$), because mid-length prefixes retain enough irrelevant content to mislead the model while discarding diagnostic events near the trace terminus (Appendix~\\ref{sec:trace_length_full}).\nThis non-monotonicity is specific to head-truncation; under tail-truncation, accuracy increases monotonically for two of three models (Table~\\ref{tab:tail_cross_model} in Appendix), with only DeepSeek showing a mild architecture-specific reversal at tail-1024$\\to$tail-2048 ($-$1.5pp).\n\n\\paragraph{Truncation direction and budget curve.}\nTail-truncation (retaining the last $k$ tokens) dramatically outperforms head-truncation: among the three models with complete data, tail-2048 exceeds head-2048 by 15.5--22.6pp, with the gap widening at smaller scale (Qwen-1.5B: +22.6pp vs.\\ Qwen-7B: +15.5pp; Appendix~\\ref{sec:trace_length_full}, Table~\\ref{tab:head_vs_tail}).\nAll four models' head-2048 accuracies converge into a narrow 75.3--81.8\\% band (6.5pp), comparable to the tail-256 band (72.6--78.9\\%, 6.3pp), indicating that signal-poor conditions produce a shared performance floor regardless of scale or architecture.\n\nA cross-model budget sweep across four models and three architecture families reveals a phase transition localized between 384 and 512 tail tokens.\nAt tail-384, all models remain near baseline (73.6--82.9\\%, only +1.0--6.5pp over tail-256); the steep jump occurs at 384$\\to$512 (+11.0--22.0pp), crossing from near-baseline to near-ceiling (${\\sim}$94--98\\%).\nThis localizes the critical threshold to ${\\sim}$400--500 tokens, matching the typical exception traceback length (Table~\\ref{tab:tail_cross_model}).\nBeyond 512 tokens, accuracy converges further: multi-seed validation across all 12 model$\\times$seed combinations confirms all tail-512 accuracies fall within a 4.63pp band [93.61\\%, 98.24\\%] (Table~\\ref{tab:tail512_seeds}); at tail-1024, three models reach 96.5--98.2\\%, compressing the 6.3pp cross-model spread observed at tail-256.\n\\texttt{tail\\_2048} captures 95--98\\% of \\texttt{exception\\_only}'s accuracy across all completed configurations.\nThe residual 2--5pp gap confirms that semantic extraction (identifying exception type and message) still outperforms positional extraction (retaining a fixed window containing non-diagnostic lines).\n\n\\paragraph{Calibration.}\n\\label{sec:calibration}\nCalibration mirrors the tier hierarchy: \\texttt{exception\\_only} ECE = 0.0027 vs.\\ \\texttt{no\\_trace} ECE = 0.171, a 63$\\times$ gap.\nThis calibration advantage generalizes across models: all three tested architectures achieve ECE ${<}$ 0.007 under \\texttt{exception\\_only} (Appendix~\\ref{sec:calibration_full}).\n\n\\paragraph{Error orthogonality.}\n\\texttt{exception\\_only}'s 2 errors have zero overlap with all other conditions' error sets (Jaccard = 0.000), confirming it operates on an independent signal dimension (Appendix~\\ref{sec:error_overlap}).\n\n\\paragraph{Exception type breakdown.}\nA per-exception-type breakdown (Appendix~\\ref{sec:exception_type}) confirms that all standard exception types achieve 100\\% accuracy; the only failures arise from \\texttt{GeneratorExit}, a benign \\texttt{BaseException} subclass.\n\n\\paragraph{Cross-dataset generalization.}\n\\label{sec:debugbench}\nOn DebugBench \\citep{tian2024debugbench} ($N{=}426$), the ranking is preserved: \\texttt{exception\\_only} 100\\%, VOTA 99.77\\%, \\texttt{no\\_trace} 96.71\\%; narrow margins reflect a ceiling effect from structurally distinctive mutations (Appendix~\\ref{sec:debugbench_full}).\n",
      "numLines": 174,
      "startLine": 1,
      "totalLines": 174
    }
  },
  "sourceToolAssistantUUID": "dba4834a-f10f-40d4-bad5-df17bdf2741b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/.claude/sessions/review_reviewer_1_7624f219",
  "sessionId": "98d2b939-6454-4d7d-877f-2c64a5a37485",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-19T12:52:12.200Z_

<details open><summary>🔧 Tool call — Read · `toolu_01PkRpUNZPKSiMAGMzf9LxRd`</summary>

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
  "parentUuid": "08520bd5-0b14-4e34-9e1a-8e3677eb5b09",
  "isSidechain": false,
  "requestId": "req_011CbBxYZacdvvTopGQWJJSJ",
  "type": "assistant",
  "uuid": "64eb3ef4-33ef-437d-bd9b-965f6afbc4a9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/.claude/sessions/review_reviewer_1_7624f219",
  "sessionId": "98d2b939-6454-4d7d-877f-2c64a5a37485",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015epz2VUxFsL8CTLMw4NsRx",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 4545,
      "cache_creation_input_tokens": 1625,
      "cache_read_input_tokens": 29633,
      "output_tokens": 354,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1625,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 4545,
          "output_tokens": 354,
          "cache_read_input_tokens": 29633,
          "cache_creation_input_tokens": 1625,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1625
          },
          "type": "message"
        }
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

_source line 40 · 2026-05-19T12:52:12.205Z_

<details><summary>↩ Tool result · `toolu_01PkRpUNZPKSiMAGMzf9LxRd`</summary>

```text
1	\section{Discussion}
2	
3	Verdict prediction is fundamentally fault detection.
4	Exception events succeed because they are the runtime's primary fault indicator: error type, stack frame, and error message, packaged in a compact format.
5	Non-exception components (variable states, loop iterations, control flow) record \emph{how} the program ran, not \emph{whether} it failed.
6	
7	This explains three key results: (1)~adding trace information beyond exceptions provides no benefit (VOTA $<$ \texttt{exception\_only}, Table~\ref{tab:ablation}), because non-diagnostic content competes for attention; (2)~a budget sweep reveals a phase transition at 384$\to$512 tail tokens (+11.0--22.0pp), matching typical exception traceback length, with \texttt{tail\_2048} capturing 95--98\% of \texttt{exception\_only}; (3)~the 6.22pp SFT advantage over the best regex concentrates on caught-exception boundary cases (Appendix~\ref{sec:regex_baselines}), confirming the model learns to distinguish \emph{whether an exception terminated execution}.
8	The 0.56pp cross-model gap and the format-collapse nature of the DeepSeek outlier support that the signal, not the model, is the binding constraint.
9	
10	\paragraph{Why exception\_only outperforms ae\_only.}
11	Although \texttt{ae\_only} is a strict superset, multi-seed evaluation reveals that extra content introduces noise: \texttt{ae\_only} achieves 99.64\%$\pm$0.49 while \texttt{exception\_only} achieves 99.83\%$\pm$0.00, indicating that \texttt{exception\_only} captures a minimal sufficient signal with zero seed variance.
12	
13	\paragraph{SFT vs.\ regex: semantic understanding.}
14	A regex baseline (B5) achieves 99.33\% by exploiting a format marker, but a \emph{nomarker} ablation (\S\ref{sec:nomarker}) resolves this concern: removing markers drops accuracy by only ${\sim}$2pp (Qwen-7B 97.65\%, Qwen-1.5B 97.82\%), leaving a 4.04pp gap over the best non-trivial regex (93.61\%).
15	On 8 boundary samples where pass-labeled code triggers exceptions, SFT classifies 6/8 correctly vs.\ 0/8 for regex (McNemar $p{=}0.041$), confirming ${\sim}$91\% of the signal is semantic.
16	
17	\paragraph{Why zero-shot and few-shot prompting fall short.}
18	Zero-shot prompting spans 51.0--93.5\% across four models (42.44pp range), while SFT compresses this to 0.56pp.
19	The bottleneck is verdict calibration: models recognize exceptions but cannot distinguish caught from uncaught ones, and three-shot ICL (90.84\%) improves only marginally, trailing SFT by 8.99pp.
20	
21	\paragraph{Near-perfect floor, not hard ceiling.}
22	The 2 errors (both \texttt{GeneratorExit} from Python's \texttt{all()} short-circuit) are shared across most configurations (Appendix~\ref{sec:error_overlap}); CodeLlama-13B seed 123 achieves 100\%, confirming 99.83\% is a convergence \emph{floor}.
23	Exception-only accuracy is \emph{signal-limited} rather than \emph{capacity-limited}: three families (1.5B--13B) converge on the same floor, while \texttt{no\_trace} shows monotonic scale dependence (67.3\%$\to$76.5\%).
24	
25	\paragraph{Tokenizer efficiency.}
26	CodeLlama's tokenizer produces ${\sim}$20\% more tokens than Qwen's on identical inputs, reducing the verdict label's loss share to ${\sim}$0.085\%.
27	A label-only loss variant recovers CodeLlama to 98.2\% at tail-1024 but collapses at tail-2048 (41.8\%), indicating LoRA long-sequence instability (Appendix~\ref{sec:tokenizer_analysis}).
28	
29	\paragraph{Tier hierarchy: practical implications.}
30	The two-tier structure (Tier~1 ${\geq}$99\%; Tier~2 = 86.1\%) suggests a fallback design: extract exception events first (median 150 tokens), resort to Tier~2 only when no exception is raised (+10.50pp over no-trace).
31	ML-based verdict prediction adds value in settings where the full suite cannot run: patch correctness prediction, flaky test detection, and offline trace analysis.
32	
33	\paragraph{Exception events capture test verdict signals, not just crashes.}
34	Although 188/339 fail samples (55.5\%) are silent logic errors, \texttt{exception\_only} achieves 100\% fail recall because test assertions generate \texttt{AssertionError} events; \texttt{no\_trace} and \texttt{full\_trace} achieve only 62.8\% and 50.0\%, confirming ``exception events'' encompasses both crashes and assertion failures.
35	
36	\begin{figure}[t]
37	\centering
38	\includegraphics[width=\columnwidth]{training_dynamics}
39	\caption{Training dynamics comparison. Exception-only (blue) converges to 99.33\% within 50 steps and saturates at 99.83\% by step 150. Full-trace with label-only loss (red, dashed) oscillates between 82\% and 89\% across all 444 training steps without stable convergence, consistent with overfitting to spurious patterns in verbose trace content.}
40	\label{fig:training_dynamics}
41	\end{figure}
42	
43	\paragraph{Information density and learning dynamics.}
44	Training dynamics provide direct evidence that information density determines learning efficiency (Figure~\ref{fig:training_dynamics}).
45	\texttt{exception\_only} reaches 99.33\% at step 50 (${\sim}$11\% of training) and saturates at 99.83\% by step 150.
46	In contrast, \texttt{full\_trace} oscillates between 82\% and 89\% across the entire training: accuracy drops 5.3pp at step 100, recovers, then drops 3.5pp at steps 250--300, as the model repeatedly latches onto and loses spurious correlations.
47	The \texttt{full\_trace} train loss reaches 0.0085 while eval accuracy stalls at 88\%, confirming overfitting to noise; a compact exception event (median 150 tokens) enables stable convergence while traces 10$\times$ longer remain trapped in oscillation (Appendix~\ref{sec:training_dynamics}).
48	Seed variance also negatively correlates with density ($\sigma{=}$0.00/0.38/1.12 for exception/VOTA/label-only), confirming compact inputs stabilize learning across initializations.
49	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "64eb3ef4-33ef-437d-bd9b-965f6afbc4a9",
  "isSidechain": false,
  "promptId": "e3f72197-8c21-47a9-99b8-7cd49faae750",
  "type": "user",
  "uuid": "61f9db3d-aefb-4092-a764-8c903268feb1",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/discussion.tex",
      "content": "\\section{Discussion}\n\nVerdict prediction is fundamentally fault detection.\nException events succeed because they are the runtime's primary fault indicator: error type, stack frame, and error message, packaged in a compact format.\nNon-exception components (variable states, loop iterations, control flow) record \\emph{how} the program ran, not \\emph{whether} it failed.\n\nThis explains three key results: (1)~adding trace information beyond exceptions provides no benefit (VOTA $<$ \\texttt{exception\\_only}, Table~\\ref{tab:ablation}), because non-diagnostic content competes for attention; (2)~a budget sweep reveals a phase transition at 384$\\to$512 tail tokens (+11.0--22.0pp), matching typical exception traceback length, with \\texttt{tail\\_2048} capturing 95--98\\% of \\texttt{exception\\_only}; (3)~the 6.22pp SFT advantage over the best regex concentrates on caught-exception boundary cases (Appendix~\\ref{sec:regex_baselines}), confirming the model learns to distinguish \\emph{whether an exception terminated execution}.\nThe 0.56pp cross-model gap and the format-collapse nature of the DeepSeek outlier support that the signal, not the model, is the binding constraint.\n\n\\paragraph{Why exception\\_only outperforms ae\\_only.}\nAlthough \\texttt{ae\\_only} is a strict superset, multi-seed evaluation reveals that extra content introduces noise: \\texttt{ae\\_only} achieves 99.64\\%$\\pm$0.49 while \\texttt{exception\\_only} achieves 99.83\\%$\\pm$0.00, indicating that \\texttt{exception\\_only} captures a minimal sufficient signal with zero seed variance.\n\n\\paragraph{SFT vs.\\ regex: semantic understanding.}\nA regex baseline (B5) achieves 99.33\\% by exploiting a format marker, but a \\emph{nomarker} ablation (\\S\\ref{sec:nomarker}) resolves this concern: removing markers drops accuracy by only ${\\sim}$2pp (Qwen-7B 97.65\\%, Qwen-1.5B 97.82\\%), leaving a 4.04pp gap over the best non-trivial regex (93.61\\%).\nOn 8 boundary samples where pass-labeled code triggers exceptions, SFT classifies 6/8 correctly vs.\\ 0/8 for regex (McNemar $p{=}0.041$), confirming ${\\sim}$91\\% of the signal is semantic.\n\n\\paragraph{Why zero-shot and few-shot prompting fall short.}\nZero-shot prompting spans 51.0--93.5\\% across four models (42.44pp range), while SFT compresses this to 0.56pp.\nThe bottleneck is verdict calibration: models recognize exceptions but cannot distinguish caught from uncaught ones, and three-shot ICL (90.84\\%) improves only marginally, trailing SFT by 8.99pp.\n\n\\paragraph{Near-perfect floor, not hard ceiling.}\nThe 2 errors (both \\texttt{GeneratorExit} from Python's \\texttt{all()} short-circuit) are shared across most configurations (Appendix~\\ref{sec:error_overlap}); CodeLlama-13B seed 123 achieves 100\\%, confirming 99.83\\% is a convergence \\emph{floor}.\nException-only accuracy is \\emph{signal-limited} rather than \\emph{capacity-limited}: three families (1.5B--13B) converge on the same floor, while \\texttt{no\\_trace} shows monotonic scale dependence (67.3\\%$\\to$76.5\\%).\n\n\\paragraph{Tokenizer efficiency.}\nCodeLlama's tokenizer produces ${\\sim}$20\\% more tokens than Qwen's on identical inputs, reducing the verdict label's loss share to ${\\sim}$0.085\\%.\nA label-only loss variant recovers CodeLlama to 98.2\\% at tail-1024 but collapses at tail-2048 (41.8\\%), indicating LoRA long-sequence instability (Appendix~\\ref{sec:tokenizer_analysis}).\n\n\\paragraph{Tier hierarchy: practical implications.}\nThe two-tier structure (Tier~1 ${\\geq}$99\\%; Tier~2 = 86.1\\%) suggests a fallback design: extract exception events first (median 150 tokens), resort to Tier~2 only when no exception is raised (+10.50pp over no-trace).\nML-based verdict prediction adds value in settings where the full suite cannot run: patch correctness prediction, flaky test detection, and offline trace analysis.\n\n\\paragraph{Exception events capture test verdict signals, not just crashes.}\nAlthough 188/339 fail samples (55.5\\%) are silent logic errors, \\texttt{exception\\_only} achieves 100\\% fail recall because test assertions generate \\texttt{AssertionError} events; \\texttt{no\\_trace} and \\texttt{full\\_trace} achieve only 62.8\\% and 50.0\\%, confirming ``exception events'' encompasses both crashes and assertion failures.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{training_dynamics}\n\\caption{Training dynamics comparison. Exception-only (blue) converges to 99.33\\% within 50 steps and saturates at 99.83\\% by step 150. Full-trace with label-only loss (red, dashed) oscillates between 82\\% and 89\\% across all 444 training steps without stable convergence, consistent with overfitting to spurious patterns in verbose trace content.}\n\\label{fig:training_dynamics}\n\\end{figure}\n\n\\paragraph{Information density and learning dynamics.}\nTraining dynamics provide direct evidence that information density determines learning efficiency (Figure~\\ref{fig:training_dynamics}).\n\\texttt{exception\\_only} reaches 99.33\\% at step 50 (${\\sim}$11\\% of training) and saturates at 99.83\\% by step 150.\nIn contrast, \\texttt{full\\_trace} oscillates between 82\\% and 89\\% across the entire training: accuracy drops 5.3pp at step 100, recovers, then drops 3.5pp at steps 250--300, as the model repeatedly latches onto and loses spurious correlations.\nThe \\texttt{full\\_trace} train loss reaches 0.0085 while eval accuracy stalls at 88\\%, confirming overfitting to noise; a compact exception event (median 150 tokens) enables stable convergence while traces 10$\\times$ longer remain trapped in oscillation (Appendix~\\ref{sec:training_dynamics}).\nSeed variance also negatively correlates with density ($\\sigma{=}$0.00/0.38/1.12 for exception/VOTA/label-only), confirming compact inputs stabilize learning across initializations.\n",
      "numLines": 49,
      "startLine": 1,
      "totalLines": 49
    }
  },
  "sourceToolAssistantUUID": "64eb3ef4-33ef-437d-bd9b-965f6afbc4a9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/.claude/sessions/review_reviewer_1_7624f219",
  "sessionId": "98d2b939-6454-4d7d-877f-2c64a5a37485",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-19T12:52:12.773Z_

<details open><summary>🔧 Tool call — Read · `toolu_01B1xeJ6YQR4644h8tXDkjp3`</summary>

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
  "parentUuid": "61f9db3d-aefb-4092-a764-8c903268feb1",
  "isSidechain": false,
  "requestId": "req_011CbBxYZacdvvTopGQWJJSJ",
  "type": "assistant",
  "uuid": "32f1d57c-e0f5-4cf8-a71c-9e5fa6c826d0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/.claude/sessions/review_reviewer_1_7624f219",
  "sessionId": "98d2b939-6454-4d7d-877f-2c64a5a37485",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015epz2VUxFsL8CTLMw4NsRx",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 4545,
      "cache_creation_input_tokens": 1625,
      "cache_read_input_tokens": 29633,
      "output_tokens": 354,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1625,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 4545,
          "output_tokens": 354,
          "cache_read_input_tokens": 29633,
          "cache_creation_input_tokens": 1625,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1625
          },
          "type": "message"
        }
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

_source line 42 · 2026-05-19T12:52:12.782Z_

<details><summary>↩ Tool result · `toolu_01B1xeJ6YQR4644h8tXDkjp3`</summary>

```text
1	\section{Related Work}
2	
3	\paragraph{Execution Traces for Code LLMs.}
4	TracePile \citep{chen2025tracepile} scaled trace-augmented training to 2.6M samples; \citet{wang2025dcsh} found trace utility task- and format-dependent, which we extend by identifying exception events as the dominant signal.
5	NExT \citep{ni2024next} and ET-CoT \citep{eguchi2025etcot} used trace chain-of-thought for repair and execution reasoning; \citet{ferrando2025execute} found compact traces comparable to full traces, supporting our density finding.
6	\citet{liu2023codeexecution} pre-trained on execution traces; \citet{chen2024selfdebug} demonstrated LLM self-debugging from execution results.
7	CRUXEval \citep{gu2024cruxeval}, extended to 19 languages \citep{xu2025cruxevalx}, established execution reasoning benchmarks.
8	None decompose which trace components contribute to \emph{classification} accuracy.
9	
10	\paragraph{Code Verdict and Patch Classification.}
11	TRACED \citep{ding2024traced} showed execution-aware pretraining improves vulnerability detection; DeepDFA \citep{steenhoek2024deepdfa} and learned program slicing \citep{yadavally2024slicing} combined classical analysis with deep learning.
12	In patch correctness, \citet{tian2020patchcorrectness}, CC2Vec \citep{hoang2020cc2vec}, LLM4PatchCorrect \citep{zhou2024llm4patch} (84.4\%), and APPT \citep{appt2024} (79.7\%) developed representation learning of code changes.
13	Test oracle generation progressed from ATLAS \citep{watson2020atlas} through retrieval-augmented approaches \citep{yu2022assertion,nashid2023assertion} to TOGA \citep{dinella2022toga}; FuseFL \citep{widyasari2024fusefl} and \citet{foster2025mutation} demonstrated structured fault signals.
14	None isolate individual trace components or compare against rule-based baselines.
15	
16	\paragraph{Fault Localization.}
17	Spectrum-based fault localization (SBFL) ranks program elements by suspiciousness from test spectra \citep{abreu2007accuracy,jones2002visualization,wong2014dstar}; recent LLM-based approaches \citep{kang2024autofl,qin2024agentfl,widyasari2024llm4fl,mukherjee2025llmfl} share our insight that anomalous execution events carry the strongest diagnostic signal.
18	Verdict prediction is a prerequisite to FL (determining \emph{whether} a fault exists before localizing \emph{where}), and both exploit the same signal type at different granularities.
19	
20	\paragraph{Trace Compression and Selection.}
21	TraceCoder \citep{huang2026tracecoder} and InspectCoder \citep{wang2025inspectcoder} use selective trace extraction; RepairAgent \citep{bouzenia2025repairagent} and Agentless \citep{xia2024agentless} incorporate execution feedback in repair workflows.
22	\citet{haque2025traces} found raw traces provide limited repair benefit; SWE-bench \citep{jimenez2024swebench} provides a realistic benchmark.
23	Our approximate decomposition (gradient dilution ${\sim}$24\% vs.\ information overload ${\sim}$76\%) provides the first quantitative framework for \emph{why} compression helps, complementing these methods' focus on \emph{how}.
24	
25	\paragraph{Calibration and Defect Prediction.}
26	Neural network calibration \citep{guo2017calibration}, extended to LLMs \citep{kadavath2022language,geng2024calibration,spiess2025calibration}, studies confidence-correctness alignment; our ECE ${<}$ 0.007 suggests compact inputs improve calibration.
27	Just-in-time defect prediction \citep{kamei2013large,hoang2019deepjit,pornprasit2021jitline} shares our fault detection motivation but operates on code change features rather than traces.
28	
29	\paragraph{Training Efficiency and Data Selection.}
30	Curriculum learning \citep{bengio2009curriculum}, dataset cartography via training dynamics \citep{swayamdipta2020cartography}, and data selection methods \citep{sachdeva2024dataefficient,xie2023doremi} show that data quality and ordering improve convergence, consistent with our finding that compact exceptions enable rapid convergence while verbose traces trap the model in oscillation.
31	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "32f1d57c-e0f5-4cf8-a71c-9e5fa6c826d0",
  "isSidechain": false,
  "promptId": "e3f72197-8c21-47a9-99b8-7cd49faae750",
  "type": "user",
  "uuid": "8d0c7ba9-88b4-484d-a22b-8920c565e5ca",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/related_work.tex",
      "content": "\\section{Related Work}\n\n\\paragraph{Execution Traces for Code LLMs.}\nTracePile \\citep{chen2025tracepile} scaled trace-augmented training to 2.6M samples; \\citet{wang2025dcsh} found trace utility task- and format-dependent, which we extend by identifying exception events as the dominant signal.\nNExT \\citep{ni2024next} and ET-CoT \\citep{eguchi2025etcot} used trace chain-of-thought for repair and execution reasoning; \\citet{ferrando2025execute} found compact traces comparable to full traces, supporting our density finding.\n\\citet{liu2023codeexecution} pre-trained on execution traces; \\citet{chen2024selfdebug} demonstrated LLM self-debugging from execution results.\nCRUXEval \\citep{gu2024cruxeval}, extended to 19 languages \\citep{xu2025cruxevalx}, established execution reasoning benchmarks.\nNone decompose which trace components contribute to \\emph{classification} accuracy.\n\n\\paragraph{Code Verdict and Patch Classification.}\nTRACED \\citep{ding2024traced} showed execution-aware pretraining improves vulnerability detection; DeepDFA \\citep{steenhoek2024deepdfa} and learned program slicing \\citep{yadavally2024slicing} combined classical analysis with deep learning.\nIn patch correctness, \\citet{tian2020patchcorrectness}, CC2Vec \\citep{hoang2020cc2vec}, LLM4PatchCorrect \\citep{zhou2024llm4patch} (84.4\\%), and APPT \\citep{appt2024} (79.7\\%) developed representation learning of code changes.\nTest oracle generation progressed from ATLAS \\citep{watson2020atlas} through retrieval-augmented approaches \\citep{yu2022assertion,nashid2023assertion} to TOGA \\citep{dinella2022toga}; FuseFL \\citep{widyasari2024fusefl} and \\citet{foster2025mutation} demonstrated structured fault signals.\nNone isolate individual trace components or compare against rule-based baselines.\n\n\\paragraph{Fault Localization.}\nSpectrum-based fault localization (SBFL) ranks program elements by suspiciousness from test spectra \\citep{abreu2007accuracy,jones2002visualization,wong2014dstar}; recent LLM-based approaches \\citep{kang2024autofl,qin2024agentfl,widyasari2024llm4fl,mukherjee2025llmfl} share our insight that anomalous execution events carry the strongest diagnostic signal.\nVerdict prediction is a prerequisite to FL (determining \\emph{whether} a fault exists before localizing \\emph{where}), and both exploit the same signal type at different granularities.\n\n\\paragraph{Trace Compression and Selection.}\nTraceCoder \\citep{huang2026tracecoder} and InspectCoder \\citep{wang2025inspectcoder} use selective trace extraction; RepairAgent \\citep{bouzenia2025repairagent} and Agentless \\citep{xia2024agentless} incorporate execution feedback in repair workflows.\n\\citet{haque2025traces} found raw traces provide limited repair benefit; SWE-bench \\citep{jimenez2024swebench} provides a realistic benchmark.\nOur approximate decomposition (gradient dilution ${\\sim}$24\\% vs.\\ information overload ${\\sim}$76\\%) provides the first quantitative framework for \\emph{why} compression helps, complementing these methods' focus on \\emph{how}.\n\n\\paragraph{Calibration and Defect Prediction.}\nNeural network calibration \\citep{guo2017calibration}, extended to LLMs \\citep{kadavath2022language,geng2024calibration,spiess2025calibration}, studies confidence-correctness alignment; our ECE ${<}$ 0.007 suggests compact inputs improve calibration.\nJust-in-time defect prediction \\citep{kamei2013large,hoang2019deepjit,pornprasit2021jitline} shares our fault detection motivation but operates on code change features rather than traces.\n\n\\paragraph{Training Efficiency and Data Selection.}\nCurriculum learning \\citep{bengio2009curriculum}, dataset cartography via training dynamics \\citep{swayamdipta2020cartography}, and data selection methods \\citep{sachdeva2024dataefficient,xie2023doremi} show that data quality and ordering improve convergence, consistent with our finding that compact exceptions enable rapid convergence while verbose traces trap the model in oscillation.\n",
      "numLines": 31,
      "startLine": 1,
      "totalLines": 31
    }
  },
  "sourceToolAssistantUUID": "32f1d57c-e0f5-4cf8-a71c-9e5fa6c826d0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/.claude/sessions/review_reviewer_1_7624f219",
  "sessionId": "98d2b939-6454-4d7d-877f-2c64a5a37485",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-19T12:52:13.103Z_

<details open><summary>🔧 Tool call — Read · `toolu_01No4BFkgoFwapGQwQgUSWvS`</summary>

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
  "parentUuid": "8d0c7ba9-88b4-484d-a22b-8920c565e5ca",
  "isSidechain": false,
  "requestId": "req_011CbBxYZacdvvTopGQWJJSJ",
  "type": "assistant",
  "uuid": "e735c19a-92fe-4d23-8f13-123517130f95",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/.claude/sessions/review_reviewer_1_7624f219",
  "sessionId": "98d2b939-6454-4d7d-877f-2c64a5a37485",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015epz2VUxFsL8CTLMw4NsRx",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 4545,
      "cache_creation_input_tokens": 1625,
      "cache_read_input_tokens": 29633,
      "output_tokens": 354,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1625,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 4545,
          "output_tokens": 354,
          "cache_read_input_tokens": 29633,
          "cache_creation_input_tokens": 1625,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1625
          },
          "type": "message"
        }
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

_source line 44_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[Round 1 审稿请求]: 你是 Reviewer 1，负责 **方法严谨性 + 实验有效性**。  ## 论文信息 - **标题**: \"Exception Events Are All You Need: Component Ablation for Trace-Based Verdict Prediction\" - **Venue**: EMNLP 2026 (ARR May 2026)…",
  "leafUuid": "34daa36d-6939-46da-95c1-27b48e83684a",
  "sessionId": "98d2b939-6454-4d7d-877f-2c64a5a37485"
}
```

---

### Runtime record

_source line 45_

```json
{
  "type": "ai-title",
  "aiTitle": "Review trace-based verdict prediction paper methodology",
  "sessionId": "98d2b939-6454-4d7d-877f-2c64a5a37485"
}
```

---

### Assistant

_source line 46 · 2026-05-19T12:52:17.302Z_

<details><summary>Logged reasoning block</summary>

```text
Now let me read the appendix for detailed supporting material, and also fetch the ARR review form for specific scoring scales.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "34daa36d-6939-46da-95c1-27b48e83684a",
  "isSidechain": false,
  "requestId": "req_011CbBxZx4zdNmNNR5SBPDGF",
  "type": "assistant",
  "uuid": "12d58e63-331d-43de-a3a8-c1952586ba82",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/.claude/sessions/review_reviewer_1_7624f219",
  "sessionId": "98d2b939-6454-4d7d-877f-2c64a5a37485",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Qbmhv51dWzSbKXeQBzsmi5",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14130,
      "cache_read_input_tokens": 31258,
      "output_tokens": 308,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 14130,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 308,
          "cache_read_input_tokens": 31258,
          "cache_creation_input_tokens": 14130,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 14130
          },
          "type": "message"
        }
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

_source line 47 · 2026-05-19T12:52:17.842Z_

读取 appendix 获取完整实验细节。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "12d58e63-331d-43de-a3a8-c1952586ba82",
  "isSidechain": false,
  "requestId": "req_011CbBxZx4zdNmNNR5SBPDGF",
  "type": "assistant",
  "uuid": "ba8c2400-b459-4c86-bc55-e54d08a8c714",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/.claude/sessions/review_reviewer_1_7624f219",
  "sessionId": "98d2b939-6454-4d7d-877f-2c64a5a37485",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Qbmhv51dWzSbKXeQBzsmi5",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14130,
      "cache_read_input_tokens": 31258,
      "output_tokens": 308,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 14130,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 308,
          "cache_read_input_tokens": 31258,
          "cache_creation_input_tokens": 14130,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 14130
          },
          "type": "message"
        }
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

_source line 48 · 2026-05-19T12:52:19.715Z_

<details open><summary>🔧 Tool call — Read · `toolu_011t6poWn5VXTvFYNA7igdvA`</summary>

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
  "parentUuid": "ba8c2400-b459-4c86-bc55-e54d08a8c714",
  "isSidechain": false,
  "requestId": "req_011CbBxZx4zdNmNNR5SBPDGF",
  "type": "assistant",
  "uuid": "61f0b016-ba41-4371-b6b5-ffbd7ae987ff",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/.claude/sessions/review_reviewer_1_7624f219",
  "sessionId": "98d2b939-6454-4d7d-877f-2c64a5a37485",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Qbmhv51dWzSbKXeQBzsmi5",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14130,
      "cache_read_input_tokens": 31258,
      "output_tokens": 308,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 14130,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 308,
          "cache_read_input_tokens": 31258,
          "cache_creation_input_tokens": 14130,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 14130
          },
          "type": "message"
        }
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

_source line 49 · 2026-05-19T12:52:19.976Z_

<details><summary>↩ Tool result · `toolu_011t6poWn5VXTvFYNA7igdvA`</summary>

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
17	Full Trace (LO)   & Qwen-2.5-7B & 85.94 & 88.21 & 93.18 & 90.63 & 80.07 & 68.73 & 73.97 \\
18	VOTA              & Qwen-2.5-7B & 99.05 & 100.00 & 99.18 & 99.59 & 97.98 & 100.00 & 98.98 \\
19	Exception Only    & Qwen-2.5-7B & 99.83 & 100.00 & 99.76 & 99.88 & 99.41 & 100.00 & 99.71 \\
20	AE Only           & Qwen-2.5-7B & 99.92 & 100.00 & 99.88 & 99.94 & 99.71 & 100.00 & 99.85 \\
21	Loop Only         & Qwen-2.5-7B & 86.05 & 92.39 & 87.07 & 89.66 & 71.65 & 82.01 & 76.48 \\
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
102	\section{VOTA Extraction Algorithm}
103	\label{sec:vota_algorithm}
104	
105	Algorithm~\ref{alg:vota} describes the three-component VOTA extraction pipeline applied to a raw \texttt{sys.settrace} execution log.
106	
107	\begin{algorithm}[t]
108	\caption{VOTA Trace Extraction}
109	\label{alg:vota}
110	\small
111	\begin{algorithmic}[1]
112	\REQUIRE Raw trace $T$ from \texttt{sys.settrace} (list of events)
113	\ENSURE Compressed VOTA representation $V$
114	\STATE $V \leftarrow$ empty string
115	\STATE \textbf{// Component 1: Exception summary}
116	\FOR{each event $e$ in $T$ with type \texttt{exception}}
117	  \STATE Parse traceback $\rightarrow$ extract error type, message, file, line
118	  \STATE Append \texttt{[ERROR] type: message (file:line)} to $V$
119	\ENDFOR
120	\IF{no exception events found}
121	  \STATE Append \texttt{[No exception data in trace]} to $V$
122	\ENDIF
123	\STATE \textbf{// Component 2: Assertion-point comparison}
124	\FOR{each \texttt{assert} or \texttt{return} event $e$ in $T$}
125	  \STATE Extract actual value from execution state
126	  \STATE Extract expected value from test assertion
127	  \STATE Append \texttt{[ASSERT] actual=... expected=... match=T/F} to $V$
128	\ENDFOR
129	\STATE \textbf{// Component 3: Loop compression}
130	\FOR{each consecutive repeated line sequence $S$ in $T$}
131	  \IF{$|S| \geq 2$ iterations of same loop body}
132	    \STATE Replace $S$ with single iteration + \texttt{[repeated $\times$N]}
133	  \ENDIF
134	\ENDFOR
135	\STATE Append compressed non-exception lines to $V$
136	\RETURN $V$
137	\end{algorithmic}
138	\end{algorithm}
139	
140	%% ============================================================
141	\section{VOTA Trace Examples}
142	\label{sec:vota_examples}
143	
144	We provide two representative VOTA trace examples illustrating the fail and pass cases.
145	In the fail case, the exception event provides an unambiguous fault signal.
146	In the pass case, the absence of an exception event combined with a matching assertion point confirms correct execution.
147	
148	\paragraph{Fail example.}
149	A \texttt{ZeroDivisionError} triggers an \texttt{[ERROR]} event, providing a direct fault signal that is sufficient for the model to predict \texttt{fail}.
150	
151	\begin{small}
152	\begin{verbatim}
153	## Function
154	def divide(a, b):
155	    return a / b
156	
157	## Test Input
158	divide(1, 0)
159	
160	## Expected Output
161	inf
162	
163	## VOTA Trace
164	[ERROR] ZeroDivisionError: division by zero
165	
166	## Verdict
167	fail
168	\end{verbatim}
169	\end{small}
170	
171	\paragraph{Pass example.}
172	No exception is raised, and the assertion point confirms that the actual output matches the expected value.
173	
174	\begin{small}
175	\begin{verbatim}
176	## Function
177	def add(a, b):
178	    return a + b
179	
180	## Test Input
181	add(2, 3)
182	
183	## Expected Output
184	5
185	
186	## VOTA Trace
187	[LOOP] No loops detected.
188	[ASSERT] actual=5, expected=5
189	
190	## Verdict
191	pass
192	\end{verbatim}
193	\end{small}
194	
195	These examples illustrate the core asymmetry exploited by the \texttt{exception\_only} condition: fail cases produce an explicit \texttt{[ERROR]} event, while pass cases are characterized by its absence.
196	This binary signal (presence vs.\ absence of an exception) is sufficient for near-perfect verdict prediction.
197	
198	%% ============================================================
199	\section{Full Experimental Results}
200	\label{sec:full_results}
201	
202	Tables~\ref{tab:full_qwen} and \ref{tab:full_deepseek} report the complete experimental results across all conditions, models, and seeds.
203	
204	\begin{table}[t]
205	\centering
206	\caption{Full results for Qwen-2.5-Coder-7B across all conditions and seeds. Conditions with a single seed report no variance. \texttt{exception\_only} achieves 99.83\% across all three seeds ($\sigma{=}$0). \texttt{ae\_only} achieves 99.64\% mean ($\pm$0.49; seed 123 at 99.08\% is the outlier).}
207	\label{tab:full_qwen}
208	\small
209	\resizebox{\columnwidth}{!}{%
210	\begin{tabular}{lcccc}
211	\toprule
212	\textbf{Condition} & \textbf{S42} & \textbf{S123} & \textbf{S456} & \textbf{Mean $\pm$ Std} \\
213	\midrule
214	exception\_only & 99.83 & 99.83 & 99.83 & 99.83 $\pm$ 0.00 \\
215	ae\_only        & 99.92 & 99.08 & 99.92 & 99.64 $\pm$ 0.49 \\
216	VOTA                     & 99.41 & 98.66 & 99.08 & 99.05 $\pm$ 0.38 \\
217	VOTA\_no\_ae    & 99.41 & ---   & ---   & --- \\
218	label\_only     & 86.22 & 86.89 & 84.70 & 85.94 $\pm$ 1.12 \\
219	loop\_only      & 85.63 & 85.88 & 86.64 & 86.05 $\pm$ 0.52 \\
220	full\_trace     & 81.76 & ---   & ---   & --- \\
221	no\_trace       & 75.13 & ---   & ---   & --- \\
222	\bottomrule
223	\end{tabular}%
224	}
225	\end{table}
226	
227	\begin{table}[t]
228	\centering
229	\caption{Full results for DeepSeek-Coder-6.7B across all conditions and seeds. \texttt{exception\_only} shows bimodal seed behavior: seeds 42 and 456 achieve 99.33\%, while seed 123 yields 91.09\% (LoRA initialization outlier, fail recall = 70.5\%).}
230	\label{tab:full_deepseek}
231	\small
232	\resizebox{\columnwidth}{!}{%
233	\begin{tabular}{llcc}
234	\toprule
235	\textbf{Condition} & \textbf{Seed} & \textbf{Accuracy} & \textbf{Notes} \\
236	\midrule
237	exception\_only & 42  & 99.33 & epoch 1: 99.83 \\
238	exception\_only & 456 & 99.33 & CI [98.82, 99.75] \\
239	exception\_only & 123 & 91.09 & fail recall = 70.5\%; CI [89.40, 92.60] \\
240	\midrule
241	VOTA                     & 42  & 84.45 & \\
242	no\_trace       & 42  & 73.36 & \\
243	full\_trace     & 42  & 79.16 & CI [76.80, 81.30] \\
244	\bottomrule
245	\end{tabular}%
246	}
247	\end{table}
248	
249	%% ============================================================
250	\section{Tokenizer and Truncation Analysis}
251	\label{sec:tokenizer_analysis}
252	
253	The VOTA cross-model gap (14.96pp, Table~\ref{tab:cross_model}; confounded by tokenizer-driven truncation; 91.7\% of DeepSeek training samples were affected) is driven by a training-time truncation asymmetry.
254	The DeepSeek tokenizer averages 2{,}626 tokens per VOTA sample versus 1{,}929 for Qwen, causing 91.7\% of DeepSeek VOTA training samples to exceed the 2{,}048-token context window.
255	The training framework preserves the verdict label but truncates trace content, so the model trains with incomplete diagnostic information for the majority of samples.
256	
257	A post-hoc group analysis provides directional evidence: partitioning DeepSeek VOTA test samples by whether their training-set counterparts exceeded the context window, intact samples ($N{=}99$) achieve 100\% accuracy while truncated samples ($N{=}1{,}091$) achieve 83.04\% (95\% CI [80.75\%, 85.24\%]; Fisher exact $p{<}0.001$), with all 185 errors concentrated in the fail class (fail recall = 31.23\%).
258	Per-class analysis (Table~\ref{tab:per_class}) confirms that DeepSeek VOTA achieves 100\% fail precision but only 45.43\% fail recall, systematically defaulting to \texttt{pass}, in contrast to Qwen VOTA, which achieves 100\% fail recall.
259	
260	Seed robustness diverges across models: Qwen \texttt{exception\_only} produces identical 99.83\% across all three seeds ($\sigma{=}0$), while DeepSeek shows bimodal behavior: seeds 42 and 456 achieve 99.33\% (fail recall = 100\%), seed 123 yields 91.09\% (fail recall = 70.5\%).
261	Because \texttt{exception\_only} test inputs contain 48.99\% duplicates (607 unique of 1,190; \S\ref{sec:dataset}), CIs assume $n{=}1{,}190$ independent trials; under deduplication ($n{=}607$), Qwen's accuracy is 99.67\% (Wilson CI [98.81, 99.91]).
262	
263	%% ============================================================
264	\section{Irreducible Sample Analysis}
265	\label{sec:irreducible}
266	
267	The \texttt{exception\_only} condition with Qwen-2.5-Coder-7B misclassifies exactly 2 out of 1,190 test samples across all three seeds (42, 123, 456), with 100\% overlap across seeds.
268	Both samples (IDs 901 and 905) share the following characteristics:
269	
270	\begin{itemize}
271	\item \textbf{Function:} \texttt{check\_dict\_case} (HumanEval/95), a function that checks whether all dictionary keys are uniformly upper-case or lower-case strings.
272	\item \textbf{Ground-truth label:} \texttt{pass}.
273	\item \textbf{Predicted label:} \texttt{fail} (false negative).
274	\item \textbf{Cross-seed consistency:} Both samples are misclassified identically by all three seeds, indicating a systematic rather than stochastic error.
275	\end{itemize}
276	
277	Manual inspection reveals the root cause: \texttt{check\_dict\_case} uses \texttt{all()} over a generator expression, and Python's \texttt{all()} short-circuits on the first \texttt{True} value, raising \texttt{GeneratorExit} to terminate the generator.
278	Because \texttt{GeneratorExit} is a \texttt{BaseException} subclass, the tracer records it as seven \texttt{[ERROR] GeneratorExit} lines, even though the function executes correctly and the test passes.
279	The model observes these spurious error markers and reasonably but incorrectly predicts \texttt{fail}.
280	This is not a model failure but a representation ambiguity: the \texttt{exception\_only} format cannot distinguish genuine exceptions from benign \texttt{BaseException} subclasses triggered by Python's iterator protocol.
281	
282	Most configurations converge to these same 2 errors: Qwen-1.5B, Qwen-7B (3 seeds), CodeLlama-13B (seeds 42/456), and DeepSeek-6.7B (seeds 42/456) all produce error set $\{901, 905\}$.
283	However, CodeLlama-13B seed 123 achieves 100\% accuracy (0/1190 errors), correctly classifying both samples.
284	This demonstrates that 99.83\% is a near-perfect \emph{floor} (the convergence attractor for most LoRA initializations) rather than a hard data ceiling: the representation supports perfect accuracy, but most initializations converge to the same 2-error basin.
285	The practical implication is that these errors are high-probability convergence artifacts addressable through seed selection or ensemble methods, not fundamental limitations of the exception-based representation.
286	
287	%% ============================================================
288	\section{Exception Type Accuracy Breakdown}
289	\label{sec:exception_type}
290	
291	Table~\ref{tab:exception_type} reports \texttt{exception\_only} accuracy stratified by exception type on Qwen-2.5-7B (seed=42, $N{=}1{,}190$).
292	All standard exception types (\texttt{TypeError}, \texttt{ValueError}, \texttt{IndexError}, etc.) achieve 100\% accuracy.
293	The only misclassifications arise from \texttt{GeneratorExit}, a \texttt{BaseException} subclass that is not an \texttt{Exception}. It is raised by Python's iterator protocol during generator short-circuiting, not by actual program errors.
294	
295	\begin{table}[t]
296	\centering
297	\caption{Exception type accuracy breakdown for \texttt{exception\_only} (Qwen-7B, seed=42). All true error types achieve 100\%. The only failures come from \texttt{GeneratorExit} (a \texttt{BaseException} subclass, not an \texttt{Exception}), which appears in 2 passing samples.}
298	\label{tab:exception_type}
299	\small
300	\begin{tabular}{lcc}
301	\toprule
302	\textbf{Exception Type} & \textbf{Samples} & \textbf{Accuracy} \\
303	\midrule
304	TypeError & 96 & 100\% \\
305	ValueError & 62 & 100\% \\
306	IndexError & 41 & 100\% \\
307	KeyError & 28 & 100\% \\
308	AttributeError & 19 & 100\% \\
309	AssertionError & 15 & 100\% \\
310	RecursionError & 12 & 100\% \\
311	Other Exception & 66 & 100\% \\
312	\midrule
313	GeneratorExit (BaseException) & 2 & 0\% \\
314	No exception (pass class) & 849 & 100\% \\
315	\bottomrule
316	\end{tabular}
317	\end{table}
318	
319	This confirms that the model has learned a clean decision boundary: any true \texttt{Exception} subclass in the trace implies failure.
320	The \texttt{GeneratorExit} case represents a semantic ambiguity in the trace format rather than a model failure, as discussed in \S\ref{sec:irreducible}.
321	
322	%% ============================================================
323	\section{Trace Length Ablation}
324	\label{sec:trace_length_full}
325	
326	To test whether the \texttt{full\_trace} performance gap is caused by input truncation at training time, we vary the maximum trace token budget on Qwen-2.5-7B (seed=42) while keeping all other hyperparameters fixed.
327	
328	\begin{table}[t]
329	\centering
330	\caption{Trace length and truncation direction ablation on Qwen-2.5-7B ($N{=}1{,}190$, seed=42). Head = standard left-truncation (retain first $k$ tokens); Tail = retain last $k$ tokens. Per-condition bootstrap 95\% CIs ($B{=}10{,}000$).}
331	\label{tab:trace_length}
332	\small
333	\begin{tabular}{llcc}
334	\toprule
335	\textbf{Direction} & \textbf{Max Tokens} & \textbf{Acc (\%)} & \textbf{95\% CI} \\
336	\midrule
337	Head & 256  & 78.82 & [76.4, 81.0] \\
338	Head & 512  & 80.42 & [78.2, 82.6] \\
339	Head & 1024 & 77.23 & [74.9, 79.6] \\
340	Head & no\_limit ($\infty$) & 81.76 & [79.7, 83.9] \\
341	\midrule
342	Tail & 256  & 77.48 & --- \\
343	Tail & 512  & 93.61 & --- \\
344	Tail & 1024 & 96.47 & --- \\
345	Tail & 2048 & 97.31 & --- \\
346	\bottomrule
347	\end{tabular}
348	\end{table}
349	
350	\begin{figure}[t]
351	\centering
352	\includegraphics[width=\columnwidth]{budget_curve}
353	\caption{Cross-model tail-truncation budget curve ($N{=}1{,}190$, four models, three architecture families). All models remain near baseline at tail-256/384, then jump +13.7--22.0pp at 384$\to$512, converging into a 93.6--98.2\% band by tail-1024. The shaded region marks the transition zone where the exception traceback (${\sim}$400--500 tokens) is captured. Dashed line: \texttt{exception\_only} range (99.3--99.9\%); dotted line: \texttt{no\_trace} range (67--77\%).}
354	\label{fig:trace_length}
355	\end{figure}
356	
357	As shown in Table~\ref{tab:trace_length} and Figure~\ref{fig:trace_length}, all four trace length conditions fall within a 5pp range (77.2\%--81.8\%).
358	To quantify the reliability of the observed differences, Table~\ref{tab:trace_length_pairwise} reports paired bootstrap comparisons ($B{=}10{,}000$, seed=42) across all condition pairs.
359	
360	\begin{table}[t]
361	\centering
362	\caption{Pairwise paired bootstrap comparisons for trace length ablation ($B{=}10{,}000$, seed=42). $\Delta$ = accuracy difference between the two conditions (first $-$ second in the budget group; condition $-$ baseline in the other groups). **$p{<}0.01$; ***$p{<}0.001$.}
363	\label{tab:trace_length_pairwise}
364	\small
365	\resizebox{\columnwidth}{!}{%
366	\begin{tabular}{llccc}
367	\toprule
368	& \textbf{Comparison} & \textbf{$\Delta$ (pp)} & \textbf{95\% CI} & \textbf{$p$-value} \\
369	\midrule
370	\multirow{4}{*}{\rotatebox{90}{\scriptsize Budget}}
371	& 512 vs.\ 256           & $+$1.60  & [$-$0.34, $+$3.53]   & 0.117 \\
372	& 1024 vs.\ 512          & $-$3.19  & [$-$5.29, $-$1.09]   & 0.002** \\
373	& no\_limit vs.\ 1024    & $+$4.54  & [$+$2.52, $+$6.55]   & ${<}$0.001*** \\
374	& no\_limit vs.\ 256     & $+$2.94  & [$+$0.84, $+$5.04]   & 0.006** \\
375	\midrule
376	\multirow{4}{*}{\rotatebox{90}{\scriptsize vs.\ no\_trace}}
377	& 256 $-$ no\_trace       & $+$3.70  & [$+$1.43, $+$6.05]   & 0.002** \\
378	& 512 $-$ no\_trace       & $+$5.29  & [$+$3.03, $+$7.56]   & ${<}$0.001*** \\
379	& 1024 $-$ no\_trace      & $+$2.10  & [$-$0.17, $+$4.37]   & 0.078 \\
380	& no\_limit $-$ no\_trace & $+$6.64  & [$+$4.37, $+$8.99]   & ${<}$0.001*** \\
381	\midrule
382	\multirow{4}{*}{\rotatebox{90}{\scriptsize vs.\ exc.}}
383	& 256 $-$ exc\_only       & $-$21.01 & [$-$23.45, $-$18.74] & ${<}$0.001*** \\
384	& 512 $-$ exc\_only       & $-$19.41 & [$-$21.76, $-$17.14] & ${<}$0.001*** \\
385	& 1024 $-$ exc\_only      & $-$22.61 & [$-$25.04, $-$20.25] & ${<}$0.001*** \\
386	& no\_limit $-$ exc\_only & $-$18.07 & [$-$20.34, $-$15.88] & ${<}$0.001*** \\
387	\bottomrule
388	\end{tabular}%
389	}
390	\end{table}
391	
392	\paragraph{Non-monotonic pattern (head-truncation).}
393	Under head-truncation (retaining trace prefixes), the trend is non-monotonic: 512 tokens (80.42\%) slightly outperforms 256 tokens (78.82\%), but doubling to 1024 tokens \emph{decreases} accuracy to 77.23\%, a statistically significant 3.19pp drop ($p{=}0.002$, 95\% CI [$-$5.29, $-$1.09]).
394	The no-limit condition (81.76\%) recovers and significantly exceeds 1024 tokens ($p{<}0.001$), but 1024 tokens is not significantly better than \texttt{no\_trace} (75.13\%; $\Delta{=}{+}2.10$pp, $p{=}0.078$, 95\% CI [$-$0.17, $+$4.37]).
395	This non-monotonicity is specific to head-truncation: the 1024-token prefix retains enough irrelevant content to mislead the model while discarding diagnostic events that appear near the trace terminus.
396	Under tail-truncation, accuracy increases monotonically for Qwen-7B and Qwen-1.5B (Table~\ref{tab:tail_cross_model}); only DeepSeek-6.7B shows a mild $-$1.5pp decrease at tail-1024$\to$tail-2048, attributable to architecture-specific long-context sensitivity rather than a systematic mid-length pathology.
397	
398	\paragraph{Comparison to baselines.}
399	All four trace budget conditions significantly exceed \texttt{no\_trace} except 1024 tokens ($p{=}0.078$), confirming that raw trace content provides some signal but unreliably so.
400	The gap to \texttt{exception\_only} (99.83\%) is massive for every budget condition (18--23pp, all $p{<}0.001$), underscoring that even unlimited raw traces cannot substitute for targeted signal extraction.
401	The best full-trace condition (no\_limit, 81.76\%) still lags \texttt{exception\_only} by 18.07pp (95\% CI [$-$20.34, $-$15.88]).
402	
403	\paragraph{Interpretation.}
404	These results rule out input truncation as the primary explanation for the full-trace performance gap: even with unlimited tokens, the model cannot extract the diagnostic signal that VOTA's targeted compression provides.
405	The non-monotonic dip at 1024 tokens is consistent with a ``worst-of-both-worlds'' regime where the model receives enough noisy context to dilute the signal but not enough to compensate through broader coverage.
406	The result reinforces the information density interpretation (\S\ref{sec:density}): the gap between full traces and VOTA is driven by the \emph{content} of the trace (irrelevant lines diluting the diagnostic signal), not its \emph{length}.
407	In contrast, VOTA's compressed representation concentrates the diagnostic signal into fewer tokens, making it sensitive to truncation when those tokens are removed (\S\ref{sec:cross_model}).
408	
409	\paragraph{Truncation direction.}
410	Tail-truncation (retaining the last $k$ tokens) dramatically outperforms head-truncation: \texttt{tail\_2048} achieves 97.31\% vs.\ \texttt{head\_2048} (no\_limit) at 81.76\%, a 15.55pp improvement.
411	Even \texttt{tail\_512} (93.61\%) exceeds every head-truncation condition by over 11pp.
412	
413	However, \texttt{tail\_256} (77.48\%) performs at the \texttt{no\_trace} baseline level (75.13\%), indicating that the diagnostic signal does not reside in the very last trace lines.
414	The critical jump occurs between 256 and 512 tail tokens (+16.13pp), localizing the signal window to approximately 256--512 tokens from the trace terminus.
415	This is consistent with Python's execution model: exception tracebacks and assertion comparisons appear near the end of the trace but are preceded by the final function call frames, placing them typically 300--500 tokens from the terminus rather than at the absolute end.
416	
417	The 18.07pp gap from \texttt{full\_trace} to \texttt{exception\_only} decomposes as: 86\% positional concentration (recovered by tail-truncation at 2048 tokens) and 14\% residual content noise (the 2.52pp gap from \texttt{tail\_2048} to \texttt{exception\_only} that persists regardless of truncation direction).
418	The fact that \texttt{exception\_only} (99.83\%) still outperforms \texttt{tail\_2048} (97.31\%) confirms that semantic extraction (identifying the exception type and message) is superior to positional extraction (keeping a fixed window), because the model need not filter out non-diagnostic lines that happen to fall within the window.
419	
420	\paragraph{Cross-model budget curve.}
421	Table~\ref{tab:tail_cross_model} extends the tail-truncation analysis to a full budget sweep across four models spanning three architecture families and an 8.7$\times$ parameter range.
422	
423	\begin{table}[t]
424	\centering
425	\caption{Cross-model tail-truncation budget curve ($N{=}1{,}190$). All four models exhibit a transition between tail-384 and tail-512 (+13--23pp). $\downarrow$: non-monotonic decrease. $^\dag$CodeLlama tail-1024 trained with label-only loss to address tokenizer-driven gradient dilution (\S\ref{sec:tokenizer_analysis}). $^\ddag$CodeLlama tail-2048 outlier (41.8\%): LoRA long-sequence instability under label-only loss; excluded from cross-model analysis.}
426	\label{tab:tail_cross_model}
427	\small
428	\resizebox{\columnwidth}{!}{%
429	\begin{tabular}{lcccccc}
430	\toprule
431	\textbf{Model} & \textbf{tail-256} & \textbf{tail-384} & \textbf{tail-512} & \textbf{tail-1024} & \textbf{tail-2048} & \textbf{exc\_only} \\
432	\midrule
433	Qwen-7B (7B) & 78.9 & 79.9 & 93.6 & 96.5 & 97.3 & 99.83 \\
434	DeepSeek (6.7B) & 76.4 & 82.9 & 93.9 & 96.5 & 95.0$\downarrow$ & 99.33 \\
435	CodeLlama (13B) & 77.9 & 80.6 & 98.2 & 98.2$^\dag$ & 41.8$^\ddag$ & 99.89 \\
436	Qwen-1.5B (1.5B) & 72.6 & 73.6 & 95.6 & 96.6 & 97.9 & 99.83 \\
437	\bottomrule
438	\end{tabular}%
439	}
440	\end{table}
441	
442	\begin{table}[t]
443	\centering
444	\caption{Cross-model truncation direction comparison ($N{=}1{,}190$). Head-truncation retains the first 2,048 tokens; tail-truncation retains the last 2,048. All four models' head-2048 accuracies converge into a narrow 75.3--81.8\% band (6.5pp), comparable to the tail-256 signal-poor band (72.6--78.9\%, 6.3pp). $^\dag$CodeLlama tail-2048 pending retraining (\S\ref{sec:tokenizer_analysis}).}
445	\label{tab:head_vs_tail}
446	\small
447	\begin{tabular}{lccc}
448	\toprule
449	\textbf{Model} & \textbf{head-2048 (\%)} & \textbf{tail-2048 (\%)} & \textbf{Gap (pp)} \\
450	\midrule
451	Qwen-1.5B & 75.3 & 97.9 & +22.6 \\
452	DeepSeek-6.7B & 78.7 & 95.0 & +16.3 \\
453	CodeLlama-13B & 79.9 & ---$^\dag$ & ---$^\dag$ \\
454	Qwen-7B & 81.8 & 97.3 & +15.5 \\
455	\bottomrule
456	\end{tabular}
457	\end{table}
458	
459	Four patterns emerge from the budget curve.
460	\emph{Phase transition between 384 and 512 tokens}: the tail-384 column reveals that the transition is not instantaneous at 256$\to$512 but localized between 384 and 512 tokens.
461	At tail-384, all four models remain near baseline (73.6--82.9\%), gaining only +1.0--6.5pp over tail-256.
462	The steep jump occurs at 384$\to$512: +13.7pp (Qwen-7B), +11.0pp (DeepSeek), +17.6pp (CodeLlama), +22.0pp (Qwen-1.5B), crossing from near-baseline to near-ceiling.
463	This localizes the critical threshold to ${\sim}$400--500 tokens, consistent with the typical exception traceback length: below ${\sim}$384 tokens, the traceback is truncated and no diagnostic event is captured; above ${\sim}$512, it is fully included regardless of model capacity or architecture.
464	
465	\emph{Convergence at tail-512+}: once the phase transition is crossed, accuracy converges across all models into a 93.6--98.2\% band at tail-512 (seed 42).
466	Multi-seed validation confirms robustness: across all 12 model$\times$seed combinations at tail-512 (Table~\ref{tab:tail512_seeds}), all accuracies fall within [93.61\%, 98.24\%], a 4.63pp band that compresses the signal-poor tail-256 spread (6.3pp) by 27\%.
467	CodeLlama-13B shows perfect per-model convergence at tail-512: all three seeds achieve 98.24\% ($\sigma{=}$0), consistent with the 13B scale and label-only loss providing a stronger optimization signal in the signal-rich regime (Table~\ref{tab:tail512_seeds}).
468	
469	\begin{table}[t]
470	\centering
471	\caption{Cross-seed convergence at the tail-512 truncation point ($N{=}1{,}190$ per seed). All 12 model$\times$seed combinations fall within a 4.63pp band [93.61\%, 98.24\%]. CodeLlama-13B achieves identical accuracy across all three seeds ($\sigma{=}$0).}
472	\label{tab:tail512_seeds}
473	\small
474	\begin{tabular}{lccccr}
475	\toprule
476	\textbf{Model} & \textbf{S42} & \textbf{S123} & \textbf{S456} & \textbf{Mean} & \textbf{$\sigma$} \\
477	\midrule
478	Qwen-7B (7B)      & 93.61 & 96.00 & 97.65 & 95.75 & 2.05 \\
479	DeepSeek (6.7B)    & 93.95 & 95.04 & 96.10 & 95.03 & 1.08 \\
480	Qwen-1.5B (1.5B)  & 95.63 & 97.65 & 96.72 & 96.67 & 1.01 \\
481	CodeLlama (13B)    & 98.24 & 98.24 & 98.24 & \textbf{98.24} & \textbf{0.00} \\
482	\midrule
483	\multicolumn{4}{l}{Cross-model band} & \multicolumn{2}{r}{[93.61, 98.24] = 4.63pp} \\
484	\bottomrule
485	\end{tabular}
486	\end{table}
487	
488	At tail-1024, four models reach 96.5--98.2\% (CodeLlama 98.2\% under label-only loss, three others 96.5--96.6\%).
489	Scale and architecture differences that dominate the signal-poor regime (tail-256 range: 72.6--78.9\%, 6.3pp) compress dramatically in the signal-rich regime.
490	
491	\emph{Signal-poor convergence band}: head-2048 accuracies across all four models also converge into a narrow 75.3--81.8\% band (6.5pp; Table~\ref{tab:head_vs_tail}), comparable in width to the tail-256 band (72.6--78.9\%, 6.3pp).
492	When the diagnostic signal is absent (head-truncation discards trace terminus) or unreachable (tail-256 is too short), models of different scale and architecture collapse to similar performance, suggesting a shared floor determined by code comprehension rather than trace processing.
493	
494	\emph{Scale behavior inversion}: in the signal-poor regime (tail-256), smaller models perform worse (Qwen-1.5B 72.6\% vs.\ Qwen-7B 78.9\%, $-$6.3pp), mirroring the \texttt{no\_trace} scale pattern.
495	In the signal-rich regime (tail-512+), this reverses: Qwen-1.5B matches or exceeds Qwen-7B (95.6\% vs.\ 93.6\% at tail-512; 97.9\% vs.\ 97.3\% at tail-2048), confirming that sufficient trace signal eliminates the capacity advantage.
496	
497	\emph{Non-monotonicity at long sequences}: two models show accuracy decreases beyond tail-1024.
498	DeepSeek-6.7B drops $-$1.5pp from tail-1024 (96.5\%) to tail-2048 (95.0\%), consistent with its known long-context sensitivity (\S\ref{sec:training_dynamics}).
499	CodeLlama-13B exhibits a more severe collapse: tail-2048 under label-only loss drops to 41.8\% (vs.\ tail-1024 = 98.2\%), which we attribute to LoRA long-sequence instability under the label-only loss regime; this outlier is excluded from cross-model tail-2048 analysis.
500	Qwen-7B and Qwen-1.5B increase monotonically across all budgets.
501	
502	Table~\ref{tab:head_vs_tail} confirms the truncation direction effect: among the three models with complete data, tail-2048 outperforms head-2048 by 15.5--22.6pp.
503	The gap is largest for Qwen-1.5B (+22.6pp), indicating that smaller models benefit most from positional proximity to the diagnostic signal, as they lack the capacity to locate it within longer, noisier prefixes.
504	
505	%% ============================================================
506	\section{Calibration Analysis}
507	\label{sec:calibration_full}
508	
509	Beyond accuracy, we evaluate whether trace conditions affect prediction calibration, motivated by recent findings that code LLM confidence is often poorly calibrated \citep{spiess2025calibration}.
510	
511	\begin{table}[t]
512	\centering
513	\caption{Calibration metrics on Qwen-2.5-7B ($N{=}1{,}190$, seed=42). ECE = expected calibration error; Brier = Brier score. Lower is better for both.}
514	\label{tab:calibration}
515	\small
516	\begin{tabular}{lcc}
517	\toprule
518	\textbf{Condition} & \textbf{ECE $\downarrow$} & \textbf{Brier $\downarrow$} \\
519	\midrule
520	ae\_only & \textbf{0.0004} & \textbf{0.0008} \\
521	exception\_only & 0.0027 & 0.0013 \\
522	VOTA & 0.0054 & 0.005 \\
523	full\_trace & 0.096 & 0.144 \\
524	no\_trace & 0.171 & 0.197 \\
525	\bottomrule
526	\end{tabular}
527	\end{table}
528	
529	Table~\ref{tab:calibration} shows that calibration quality mirrors the Tier~1/2 hierarchy.
530	Tier~1 conditions (\texttt{ae\_only}: ECE=0.0004; \texttt{exception\_only}: ECE=0.0027) produce near-perfectly calibrated predictions, while \texttt{full\_trace} (ECE=0.096) and \texttt{no\_trace} (ECE=0.171) exhibit substantial miscalibration.
531	VOTA (ECE=0.0054) is well-calibrated but slightly worse than either Tier~1 component alone, reinforcing the pattern that combining trace signals dilutes rather than improves the prediction signal.
532	
533	The Brier scores tell a consistent story: \texttt{ae\_only} (0.0008) and \texttt{exception\_only} (0.0013) achieve near-zero scores, while \texttt{no\_trace} (0.197) indicates substantial miscalibration.
534	
535	\paragraph{Cross-model calibration.}
536	Table~\ref{tab:calibration_cross} extends the calibration analysis to three models under \texttt{exception\_only}.
537	All three models achieve ECE ${<}$ 0.007 and Brier ${<}$ 0.007, confirming that calibration quality generalizes across architectures.
538	CodeLlama-13B achieves the lowest ECE (0.0020) and MCE (0.0411), while DeepSeek-6.7B shows the highest ECE (0.0064) and Brier (0.0061), consistent with its higher error rate (8 errors vs.\ 2 for Qwen/CodeLlama).
539	
540	\begin{table}[t]
541	\centering
542	\caption{Cross-model calibration for \texttt{exception\_only} ($N{=}1{,}190$, seed=42). ECE = expected calibration error; Brier = Brier score; MCE = maximum calibration error. All models achieve ECE ${<}$ 0.007.}
543	\label{tab:calibration_cross}
544	\small
545	\begin{tabular}{lccc}
546	\toprule
547	\textbf{Model} & \textbf{ECE $\downarrow$} & \textbf{Brier $\downarrow$} & \textbf{MCE $\downarrow$} \\
548	\midrule
549	CodeLlama-13B & \textbf{0.0020} & \textbf{0.0013} & \textbf{0.0411} \\
550	Qwen-7B & 0.0027 & \textbf{0.0013} & 0.8355 \\
551	DeepSeek-6.7B & 0.0064 & 0.0061 & 0.7756 \\
552	\bottomrule
553	\end{tabular}
554	\end{table}
555	
556	\begin{figure}[t]
557	\centering
558	\includegraphics[width=\columnwidth]{fig2_calibration}
559	\caption{Reliability diagrams for four trace conditions on Qwen-2.5-7B ($N{=}1{,}190$, seed=42). \texttt{exception\_only} (ECE=0.0027) clusters near the diagonal, while \texttt{no\_trace} (ECE=0.171) exhibits systematic overconfidence, a 63$\times$ gap.}
560	\label{fig:calibration}
561	\end{figure}
562	
563	%% ============================================================
564	\section{Error Overlap Analysis}
565	\label{sec:error_overlap}
566	
567	We analyze the overlap between error sets of different conditions to determine whether they fail on the same samples (Figure~\ref{fig:error_overlap}).
568	
569	\texttt{exception\_only}'s 2 errors (samples 901 and 905) have zero intersection with the error sets of all other conditions (Jaccard = 0.000 in all pairwise comparisons).
570	This orthogonality arises because \texttt{exception\_only} errors are caused by \texttt{GeneratorExit} false positives (pass samples misclassified as fail due to benign \texttt{BaseException} events), while errors from other conditions are predominantly fail samples misclassified as pass due to insufficient signal.
571	
572	Among non-exception conditions, error sets exhibit hierarchical containment: \texttt{ae\_only} $\subset$ VOTA $\subset$ \texttt{loop\_only} $\subset$ \texttt{no\_trace}, with pairwise Jaccard indices increasing with signal overlap.
573	\texttt{loop\_only} and \texttt{full\_trace} share the highest overlap (Jaccard ${\sim}$0.65), reflecting their shared reliance on behavioral patterns rather than explicit fault indicators.
574	
575	This analysis confirms that \texttt{exception\_only} operates on an independent signal dimension: its errors are representation ambiguities (iterator protocol artifacts) rather than information deficits, explaining why combining it with other signals cannot eliminate these specific errors.
576	
577	\begin{figure}[t]
578	\centering
579	\includegraphics[width=\columnwidth]{error_overlap}
580	\caption{Jaccard similarity between error sets of different conditions (Qwen-7B, seed=42, $N{=}1{,}190$). \texttt{exception\_only} (exc\_only) has zero overlap with all other conditions, confirming it operates on an independent signal dimension.}
581	\label{fig:error_overlap}
582	\end{figure}
583	
584	%% ============================================================
585	\section{Cross-Dataset Generalization: DebugBench}
586	\label{sec:debugbench_full}
587	
588	To test whether exception-based verdict prediction generalizes beyond LLM-generated solutions, we evaluate on DebugBench \citep{tian2024debugbench}, a dataset of human-written programs with synthetically injected bugs (single-point mutations such as operator replacement, variable misuse, and missing statements).
589	After filtering for executable Python samples with valid traces, we retain 426 samples with a near-balanced class distribution (majority baseline: 51.4\%).
590	
591	\begin{table}[t]
592	\centering
593	\caption{Generalization to DebugBench ($N{=}426$, Qwen-2.5-7B, seed=42). Wilson 95\% CIs. The component ranking (exception\_only $\geq$ VOTA $>$ no\_trace) is preserved, and exception\_only achieves perfect accuracy.}
594	\label{tab:debugbench}
595	\small
596	\begin{tabular}{lcc}
597	\toprule
598	\textbf{Condition} & \textbf{Acc (\%)} & \textbf{95\% CI} \\
599	\midrule
600	exception\_only & \textbf{100.00} & [99.14, 100.00] \\
601	VOTA & 99.77 & [99.30, 100.00] \\
602	no\_trace & 96.71 & [94.80, 98.40] \\
603	\midrule
604	Majority baseline & 51.41 & --- \\
605	\bottomrule
606	\end{tabular}
607	\end{table}
608	
609	Table~\ref{tab:debugbench} shows that the component ranking from the main experiments is preserved: \texttt{exception\_only} (100.00\%) $\geq$ VOTA (99.77\%) $>$ \texttt{no\_trace} (96.71\%).
610	The \texttt{exception\_only} condition achieves perfect accuracy, confirming that the exception-based representation generalizes to a different fault distribution without degradation.
611	
612	The absolute margins are much narrower than on the main dataset: the \texttt{no\_trace} baseline already achieves 96.71\% (compared to 75.13\% on HumanEval+MBPP), leaving only 3.29pp of headroom for trace-based improvement.
613	This ceiling effect reflects a fundamental difference in fault characteristics: DebugBench bugs are synthetically injected single-point mutations, which produce code that is structurally dissimilar from the original correct solution; a model can often identify the fault from source code alone.
614	In contrast, the HumanEval+MBPP solutions are LLM-generated, producing natural errors (logic mistakes, edge-case failures) where the faulty and correct solutions may be structurally similar, making code-only verdict prediction substantially harder.
615	
616	These results support exception-based verdict prediction as a generalizable approach: the method does not degrade on an out-of-distribution dataset, and the exception dominance ranking (exception\_only $\geq$ VOTA $>$ no\_trace) is consistent across both datasets. However, the narrow DebugBench margins are insufficient to independently validate trace importance.
617	The 24.70pp trace lift on the main dataset (no\_trace 75.13\% $\to$ exception\_only 99.83\%) remains the primary evidence for the value of exception-based trace signals.
618	
619	%% ============================================================
620	\section{Cross-Model Robustness Analysis}
621	\label{sec:robustness_analysis}
622	
623	The cross-model gap pattern (Table~\ref{tab:cross_model}) suggests a design principle: \emph{trace representations should match the model capability floor, not the ceiling.}
624	Exception events are consistently the most effective component on both models, and their structural simplicity (a fixed-format error message) ensures that the relative advantage over richer representations holds across all seeds.
625	Two of three DeepSeek seeds match Qwen-level accuracy (99.33\%); the outlier (seed 123, 91.09\%) we hypothesize reflects LoRA initialization sensitivity landing in a suboptimal basin (fail recall = 70.5\%, though direct evidence is lacking), not a failure of the exception signal itself; even this outlier outperforms VOTA (84.45\%) by 6.64pp.
626	The VOTA cross-model gap is confounded by two factors: (1)~tokenizer efficiency (the DeepSeek tokenizer averages 2{,}626 tokens per VOTA sample versus Qwen's 1{,}929, causing 91.7\% of training samples to exceed the 2{,}048-token context window; content-aware truncation preferentially removes the terminal structured prompt, preserving the verdict label but truncating trace content) and (2)~base model capability differences, consistent with findings that SFT generalization depends on pretrain quality \citep{yang2024generalization}.
627	The two factors cannot be disentangled in the current experimental design.
628	Our \texttt{exception\_only} design sidesteps the truncation confound entirely: inputs have a median of 150 tokens (mean 398), well below the 2{,}048-token context window, so no training samples are truncated on either model.
629	The resulting 0.56pp cross-model gap (Table~\ref{tab:cross_model}) is therefore a clean measure of model capability differences, making the ``capability floor'' principle directly testable.
630	The practical implication is that trace-based systems should default to the simplest sufficient signal; for smaller models, training stability (multi-seed selection, warmup schedules) is a secondary but addressable concern.
631	
632	%% ============================================================
633	\section{Training Dynamics and Loss Decoupling}
634	\label{sec:training_dynamics}
635	
636	The DeepSeek \texttt{exception\_only} results reveal two instructive training dynamics.
637	First, epoch-level analysis shows mild degradation in 2/3 seeds: seed 42 peaks at 99.83\% after epoch~1 but settles at 99.33\% by epoch~3 ($-$0.50pp), seed 123 degrades from 91.43\% to 91.09\% ($-$0.34pp), while seed 456 shows no epoch degradation (99.33\% at both epoch~1 and epoch~3).
638	Early stopping may yield marginal gains for some seeds, but the epoch effect is small (${\leq}$0.5pp) compared to the seed effect (8.24pp between seeds 42 and 123).
639	
640	Second, seeds 123 and 456 converge to nearly identical final training losses (0.122 and 0.123 respectively), yet their accuracies differ by 8.24pp (91.09\% vs.\ 99.33\%).
641	The critical difference lies in fail recall: seeds 42 and 456 achieve 100\%, while seed 123 achieves only 70.5\%. The LoRA initialization in seed 123 fails to learn the exception$\to$fail mapping for a substantial fraction of failing samples, even though the per-token loss appears converged.
642	This demonstrates that token-level training loss can mask fundamental differences in sample-level classification ability, suggesting a parallel to the eval-loss/accuracy decoupling observed in DeepSeek VOTA (where eval loss rose 65\% from epoch 1 to 3 while accuracy improved by 6.3pp) at the training phase.
643	The practical recommendation is twofold: (1)~use task-specific metrics (accuracy, fail recall) for checkpoint and seed selection rather than training or evaluation loss, and (2)~for deployment on smaller models, train multiple seeds and select the best, as a single run may not reliably converge to the correct classification boundary.
644	
645	\paragraph{Format collapse, not semantic failure.}
646	The 100 errors of seed 123 are not semantic failures but generation format collapse: on inputs exceeding 4,000 characters (those containing verbose locals dumps), the model echoes trace content instead of emitting a verdict token, while achieving zero errors on shorter inputs.
647	This indicates that the LoRA initialization of seed 123 specifically compromises long-context format compliance rather than exception signal comprehension, further supporting the robustness advantage of compact \texttt{exception\_only} inputs.
648	
649	The contrast with VOTA is instructive: DeepSeek VOTA accuracy monotonically increases from 78.15\% to 84.45\% across epochs, but is consistent with a performance limit associated with the high trace truncation rate (\S\ref{sec:cross_model}): the model progressively extracts signal from samples with intact trace content but cannot fully compensate for the information loss in the truncated majority.
650	The 84.45\% accuracy reflects a combination of trace information loss and model capability constraints.
651	
652	%% ============================================================
653	\section{Deduplication Statistics}
654	\label{sec:dedup_stats}
655	
656	Table~\ref{tab:dedup} reports the duplication rates across trace formats.
657	Because multiple passing solutions to the same problem produce identical (input, output) pairs in the \texttt{exception\_only} format (correct executions raise no exceptions, so the trace content is the same regardless of the solution's internal logic), the dataset contains duplicate rows.
658	Train--test input overlap is zero (split by problem ID), so no information leakage occurs.
659	The high duplication in \texttt{exception\_only} does not affect our experimental conclusions: after deduplication the training set still contains 2,858 unique samples and the test set 607, providing sufficient coverage for the 591-problem benchmark.
660	
661	\paragraph{Problem-level partitioning and sensitivity analysis.}
662	Data is partitioned at the problem level: 472 training problems and 119 test problems, with zero crossover.
663	Duplicates arise from multiple candidate solutions per problem (up to 10 solutions each), not from cross-problem overlap.
664	To verify that deduplication does not alter any finding, we ran a sensitivity analysis across all 19 experimental conditions (7 trace formats $\times$ 4 models, minus conditions not run): deduplication produces a 0.00pp accuracy delta in every case.
665	This confirms that duplicate samples neither inflate nor deflate accuracy, because duplicates share the same ground-truth label and the model's prediction is deterministic at inference time.
666	The \texttt{exception\_only} test set contains 48.99\% duplicate inputs due to representation compactness; all confidence intervals treat samples as independent Bernoulli trials.
667	
668	\begin{table}[t]
669	\centering
670	\caption{Deduplication statistics. The \texttt{exception\_only} format collapses multiple passing solutions into identical rows because correct executions produce no exception events. Train--test input overlap is 0 (no leakage).}
671	\label{tab:dedup}
672	\small
673	\begin{tabular}{lccc}
674	\toprule
675	\textbf{Split} & \textbf{Total} & \textbf{Unique} & \textbf{Dup.\ rate} \\
676	\midrule
677	exception\_only train & 4{,}720 & 2{,}858 & 39.45\% \\
678	exception\_only test  & 1{,}190 &   607 & 48.99\% \\
679	raw\_traces (full)    & 5{,}910 & 5{,}803 &  1.81\% \\
680	\bottomrule
681	\end{tabular}
682	\end{table}
683	
684	%% ============================================================
685	\section{Regex Baseline Analysis}
686	\label{sec:regex_baselines}
687	
688	To establish a non-learning upper bound, we evaluate six regex-based baselines on the \texttt{exception\_only} test set ($N{=}1{,}190$) and two format-specific baselines on VOTA and \texttt{full\_trace} inputs.
689	
690	\begin{table}[t]
691	\centering
692	\caption{Regex baseline accuracy ($N{=}1{,}190$). B4 is the strongest semantic baseline (6.22pp below SFT \texttt{exception\_only}, McNemar $p{<}0.001$). B6 uses an error count threshold. $^\ddag$B5 exploits a data formatting artifact: the \texttt{[No exception data in trace]} marker is deterministically present in all pass samples, making this a format-level shortcut rather than a genuine exception-based heuristic.}
693	\label{tab:regex}
694	\small
695	\begin{tabular}{llc}
696	\toprule
697	\textbf{Baseline} & \textbf{Method} & \textbf{Acc (\%)} \\
698	\midrule
699	B1: \texttt{[ERROR]} presence & string match & 93.45 \\
700	B2: Traceback presence & string match & 71.51 \\
701	B3: Any keyword & union of B1+B2+Exception & 93.45 \\
702	B4: Exception type regex & regex on exception class names & \textbf{93.61} \\
703	B5: Format marker & \texttt{[No exception data]} $\to$ pass & 99.33$^\ddag$ \\
704	B6: Error count $\geq$2 & count threshold & 92.02 \\
705	\midrule
706	VOTA format regex & best regex on VOTA traces & 75.55 \\
707	full\_trace format regex & best regex on full traces & 77.39 \\
708	\bottomrule
709	\end{tabular}
710	\end{table}
711	
712	The strongest legitimate baseline (B4, 93.61\%) applies regex pattern-matching on Python exception class names (e.g., \texttt{ValueError}, \texttt{TypeError}).
713	Its errors concentrate on 8 boundary samples where a \texttt{ValueError} is raised inside a \texttt{try/except} block and caught; the program passes despite an exception occurring in the trace.
714	SFT \texttt{exception\_only} correctly classifies 6 of these 8 samples, indicating that the model learns the semantic distinction between caught (benign) and uncaught (fault-indicating) exceptions.
715	B5 (99.33\%) achieves near-SFT accuracy but relies on the deterministic presence of a format marker in pass-class traces, which is an artifact of the trace preprocessing pipeline rather than a generalizable signal; McNemar test vs.\ SFT yields $p{=}0.041$, confirming a statistically significant difference.
716	
717	\paragraph{Cross-format comparison.}
718	Table~\ref{tab:regex_cross_format} compares SFT and the best applicable regex baseline for each trace format.
719	The SFT advantage increases with format complexity: \texttt{no\_trace} (+3.62pp over majority baseline) $<$ \texttt{full\_trace} (+4.37pp) $<$ \texttt{exception\_only} (+6.22pp) $\ll$ VOTA (+23.86pp).
720	The VOTA gap is largest because its structured multi-component format carries semantic content that regex cannot parse, while \texttt{exception\_only}'s simpler format allows regex to capture most of the signal.
721	
722	\begin{table}[t]
723	\centering
724	\caption{SFT vs.\ best regex baseline by trace format ($N{=}1{,}190$). Regex baselines: majority class for \texttt{no\_trace}, keyword matching for \texttt{full\_trace}, pattern matching for VOTA, exception type regex (B4) for \texttt{exception\_only}.}
725	\label{tab:regex_cross_format}
726	\small
727	\begin{tabular}{lccc}
728	\toprule
729	\textbf{Format} & \textbf{SFT (\%)} & \textbf{Regex (\%)} & \textbf{$\Delta$ (pp)} \\
730	\midrule
731	exception\_only & 99.83 & 93.61 & +6.22 \\
732	VOTA & 99.05 & 75.55 & +23.50 \\
733	full\_trace & 81.76 & 77.39 & +4.37 \\
734	no\_trace & 75.13 & 71.51 & +3.62 \\
735	\bottomrule
736	\end{tabular}
737	\end{table}
738	
739	%% ============================================================
740	\section{Cross-Model Zero-Shot Comparison}
741	\label{sec:zeroshot_cross_model}
742	
743	Table~\ref{tab:zeroshot_cross_model} compares zero-shot and SFT \texttt{exception\_only} accuracy across four models.
744	Zero-shot performance does not correlate with model size: the smallest model (Qwen-1.5B, 93.45\%) outperforms all larger models, while the largest (CodeLlama-13B) falls below majority baseline.
745	SFT compresses the 42.44pp zero-shot range to 0.56pp, eliminating architecture-dependent variance.
746	
747	\begin{table}[t]
748	\centering
749	\caption{Zero-shot vs.\ SFT \texttt{exception\_only} across four models ($N{=}1{,}190$). Zero-shot accuracy is uncorrelated with model size; SFT normalizes cross-architecture variance from 42.44pp to 0.56pp.}
750	\label{tab:zeroshot_cross_model}
751	\small
752	\begin{tabular}{llccc}
753	\toprule
754	\textbf{Model} & \textbf{Size} & \textbf{Zero-shot (\%)} & \textbf{SFT (\%)} & \textbf{$\Delta$ (pp)} \\
755	\midrule
756	Qwen-1.5B & 1.5B & 93.45 & 99.83 & +6.38 \\
757	DeepSeek-6.7B & 6.7B & 90.59 & 99.33 & +8.74 \\
758	Qwen-7B & 7B & 89.08 & 99.83 & +10.75 \\
759	CodeLlama-13B & 13B & 51.01 & 99.89 & +48.88 \\
760	\midrule
761	Range & --- & 42.44pp & 0.56pp & --- \\
762	\bottomrule
763	\end{tabular}
764	\end{table}
765	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "61f0b016-ba41-4371-b6b5-ffbd7ae987ff",
  "isSidechain": false,
  "promptId": "e3f72197-8c21-47a9-99b8-7cd49faae750",
  "type": "user",
  "uuid": "61f6def3-5e4d-46ea-b897-5c6625ee59e3",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/appendix.tex",
      "content": "\\section{Per-Class Performance Breakdown}\n\\label{sec:per_class}\n\nTable~\\ref{tab:per_class} reports per-class precision, recall, and F1 for all experimental conditions.\n\n\\begin{table*}[t]\n\\centering\n\\caption{Per-class precision, recall, and F1 for all experimental conditions (seed 42). DeepSeek VOTA achieves 100\\% fail precision but only 45.4\\% fail recall, indicating systematic bias toward predicting \\texttt{pass}. DeepSeek \\texttt{exception\\_only} seed 42 achieves 100\\% fail recall, but seed 123 drops to 70.5\\% (see Table~\\ref{tab:full_deepseek}).}\n\\label{tab:per_class}\n\\small\n\\begin{tabular}{llccccccc}\n\\toprule\n\\textbf{Condition} & \\textbf{Model} & \\textbf{Acc} & \\textbf{Pass P} & \\textbf{Pass R} & \\textbf{Pass F1} & \\textbf{Fail P} & \\textbf{Fail R} & \\textbf{Fail F1} \\\\\n\\midrule\nNo Trace          & Qwen-2.5-7B & 75.13 & 87.76 & 75.79 & 81.34 & 54.73 & 73.45 & 62.72 \\\\\nFull Trace        & Qwen-2.5-7B & 81.76 & 87.74 & 86.60 & 87.17 & 67.43 & 69.62 & 68.51 \\\\\nFull Trace (LO)   & Qwen-2.5-7B & 85.94 & 88.21 & 93.18 & 90.63 & 80.07 & 68.73 & 73.97 \\\\\nVOTA              & Qwen-2.5-7B & 99.05 & 100.00 & 99.18 & 99.59 & 97.98 & 100.00 & 98.98 \\\\\nException Only    & Qwen-2.5-7B & 99.83 & 100.00 & 99.76 & 99.88 & 99.41 & 100.00 & 99.71 \\\\\nAE Only           & Qwen-2.5-7B & 99.92 & 100.00 & 99.88 & 99.94 & 99.71 & 100.00 & 99.85 \\\\\nLoop Only         & Qwen-2.5-7B & 86.05 & 92.39 & 87.07 & 89.66 & 71.65 & 82.01 & 76.48 \\\\\nVOTA\\_no\\_ae       & Qwen-2.5-7B & 99.41 & 99.88 & 99.29 & 99.59 & 98.26 & 99.71 & 98.98 \\\\\n\\midrule\nNo Trace          & DeepSeek-6.7B & 73.36 & 81.71 & 80.85 & 81.28 & 53.16 & 54.57 & 53.86 \\\\\nFull Trace        & DeepSeek-6.7B & 79.16 & 85.70 & 85.10 & 85.40 & 63.20 & 64.30 & 63.70 \\\\\nVOTA              & DeepSeek-6.7B & 84.45 & 82.14 & 100.00 & 90.20 & 100.00 & 45.40 & 62.50 \\\\\nException Only    & DeepSeek-6.7B & 99.33 & 100.00 & 99.06 & 99.53 & 97.69 & 100.00 & 98.83 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table*}\n\n%% ============================================================\n\\section{Training Details}\n\\label{sec:training_details}\n\nTable~\\ref{tab:hyperparams} summarizes the training hyperparameters shared across all conditions.\nAll experiments use the HuggingFace TRL \\texttt{SFTTrainer} with LoRA \\citep{hu2022lora} applied to all linear layers.\n\n\\begin{table}[t]\n\\centering\n\\caption{Training hyperparameters (shared across all conditions).}\n\\label{tab:hyperparams}\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{ll}\n\\toprule\n\\textbf{Hyperparameter} & \\textbf{Value} \\\\\n\\midrule\nLoRA rank ($r$)            & 16 \\\\\nLoRA alpha ($\\alpha$)      & 32 \\\\\nLoRA dropout               & 0.05 \\\\\nLoRA target modules        & all linear layers \\\\\n\\midrule\nEpochs                     & 3 \\\\\nPer-device batch size       & 4 \\\\\nGradient accumulation steps & 8 \\\\\nEffective batch size        & 32 \\\\\n\\midrule\nLearning rate               & $2 \\times 10^{-4}$ \\\\\nLR scheduler                & linear decay \\\\\nWarmup ratio                & 0.1 \\\\\nWeight decay                & 0.01 \\\\\n\\midrule\nMax sequence length         & 2048 tokens \\\\\nPrimary seed                & 42 \\\\\nRobustness seeds            & 123, 456 \\\\\n\\midrule\nHardware                    & 1$\\times$ RTX PRO 6000 Blackwell (96\\,GB VRAM) \\\\\nFramework                   & HuggingFace TRL SFTTrainer \\\\\n\\bottomrule\n\\end{tabular}%\n}\n\\end{table}\n\nTable~\\ref{tab:train_time} reports per-condition training wall-clock times.\nConditions with longer trace inputs (e.g., \\texttt{full\\_trace}, VOTA) require proportionally more training time due to increased sequence lengths.\n\n\\begin{table}[t]\n\\centering\n\\caption{Training wall-clock time per condition on a single RTX PRO 6000 Blackwell GPU. Where multiple seeds were run, individual times are listed.}\n\\label{tab:train_time}\n\\small\n\\begin{tabular}{llr}\n\\toprule\n\\textbf{Condition} & \\textbf{Seed(s)} & \\textbf{Time (h)} \\\\\n\\midrule\nno\\_trace       & 42         & ${\\sim}$0.5 \\\\\nfull\\_trace     & 42         & ${\\sim}$2.2 \\\\\nlabel\\_only     & 42         & ${\\sim}$2.2 \\\\\nVOTA                     & 42         & ${\\sim}$2.3 \\\\\nexception\\_only & 42         & ${\\sim}$2.1 \\\\\nexception\\_only & 123        & ${\\sim}$2.1 \\\\\nexception\\_only & 456        & ${\\sim}$1.3 \\\\\nae\\_only        & 42         & ${\\sim}$1.8 \\\\\nloop\\_only      & 42         & ${\\sim}$2.1 \\\\\nVOTA\\_no\\_ae    & 42         & ${\\sim}$1.8 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n%% ============================================================\n\\section{VOTA Extraction Algorithm}\n\\label{sec:vota_algorithm}\n\nAlgorithm~\\ref{alg:vota} describes the three-component VOTA extraction pipeline applied to a raw \\texttt{sys.settrace} execution log.\n\n\\begin{algorithm}[t]\n\\caption{VOTA Trace Extraction}\n\\label{alg:vota}\n\\small\n\\begin{algorithmic}[1]\n\\REQUIRE Raw trace $T$ from \\texttt{sys.settrace} (list of events)\n\\ENSURE Compressed VOTA representation $V$\n\\STATE $V \\leftarrow$ empty string\n\\STATE \\textbf{// Component 1: Exception summary}\n\\FOR{each event $e$ in $T$ with type \\texttt{exception}}\n  \\STATE Parse traceback $\\rightarrow$ extract error type, message, file, line\n  \\STATE Append \\texttt{[ERROR] type: message (file:line)} to $V$\n\\ENDFOR\n\\IF{no exception events found}\n  \\STATE Append \\texttt{[No exception data in trace]} to $V$\n\\ENDIF\n\\STATE \\textbf{// Component 2: Assertion-point comparison}\n\\FOR{each \\texttt{assert} or \\texttt{return} event $e$ in $T$}\n  \\STATE Extract actual value from execution state\n  \\STATE Extract expected value from test assertion\n  \\STATE Append \\texttt{[ASSERT] actual=... expected=... match=T/F} to $V$\n\\ENDFOR\n\\STATE \\textbf{// Component 3: Loop compression}\n\\FOR{each consecutive repeated line sequence $S$ in $T$}\n  \\IF{$|S| \\geq 2$ iterations of same loop body}\n    \\STATE Replace $S$ with single iteration + \\texttt{[repeated $\\times$N]}\n  \\ENDIF\n\\ENDFOR\n\\STATE Append compressed non-exception lines to $V$\n\\RETURN $V$\n\\end{algorithmic}\n\\end{algorithm}\n\n%% ============================================================\n\\section{VOTA Trace Examples}\n\\label{sec:vota_examples}\n\nWe provide two representative VOTA trace examples illustrating the fail and pass cases.\nIn the fail case, the exception event provides an unambiguous fault signal.\nIn the pass case, the absence of an exception event combined with a matching assertion point confirms correct execution.\n\n\\paragraph{Fail example.}\nA \\texttt{ZeroDivisionError} triggers an \\texttt{[ERROR]} event, providing a direct fault signal that is sufficient for the model to predict \\texttt{fail}.\n\n\\begin{small}\n\\begin{verbatim}\n## Function\ndef divide(a, b):\n    return a / b\n\n## Test Input\ndivide(1, 0)\n\n## Expected Output\ninf\n\n## VOTA Trace\n[ERROR] ZeroDivisionError: division by zero\n\n## Verdict\nfail\n\\end{verbatim}\n\\end{small}\n\n\\paragraph{Pass example.}\nNo exception is raised, and the assertion point confirms that the actual output matches the expected value.\n\n\\begin{small}\n\\begin{verbatim}\n## Function\ndef add(a, b):\n    return a + b\n\n## Test Input\nadd(2, 3)\n\n## Expected Output\n5\n\n## VOTA Trace\n[LOOP] No loops detected.\n[ASSERT] actual=5, expected=5\n\n## Verdict\npass\n\\end{verbatim}\n\\end{small}\n\nThese examples illustrate the core asymmetry exploited by the \\texttt{exception\\_only} condition: fail cases produce an explicit \\texttt{[ERROR]} event, while pass cases are characterized by its absence.\nThis binary signal (presence vs.\\ absence of an exception) is sufficient for near-perfect verdict prediction.\n\n%% ============================================================\n\\section{Full Experimental Results}\n\\label{sec:full_results}\n\nTables~\\ref{tab:full_qwen} and \\ref{tab:full_deepseek} report the complete experimental results across all conditions, models, and seeds.\n\n\\begin{table}[t]\n\\centering\n\\caption{Full results for Qwen-2.5-Coder-7B across all conditions and seeds. Conditions with a single seed report no variance. \\texttt{exception\\_only} achieves 99.83\\% across all three seeds ($\\sigma{=}$0). \\texttt{ae\\_only} achieves 99.64\\% mean ($\\pm$0.49; seed 123 at 99.08\\% is the outlier).}\n\\label{tab:full_qwen}\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Condition} & \\textbf{S42} & \\textbf{S123} & \\textbf{S456} & \\textbf{Mean $\\pm$ Std} \\\\\n\\midrule\nexception\\_only & 99.83 & 99.83 & 99.83 & 99.83 $\\pm$ 0.00 \\\\\nae\\_only        & 99.92 & 99.08 & 99.92 & 99.64 $\\pm$ 0.49 \\\\\nVOTA                     & 99.41 & 98.66 & 99.08 & 99.05 $\\pm$ 0.38 \\\\\nVOTA\\_no\\_ae    & 99.41 & ---   & ---   & --- \\\\\nlabel\\_only     & 86.22 & 86.89 & 84.70 & 85.94 $\\pm$ 1.12 \\\\\nloop\\_only      & 85.63 & 85.88 & 86.64 & 86.05 $\\pm$ 0.52 \\\\\nfull\\_trace     & 81.76 & ---   & ---   & --- \\\\\nno\\_trace       & 75.13 & ---   & ---   & --- \\\\\n\\bottomrule\n\\end{tabular}%\n}\n\\end{table}\n\n\\begin{table}[t]\n\\centering\n\\caption{Full results for DeepSeek-Coder-6.7B across all conditions and seeds. \\texttt{exception\\_only} shows bimodal seed behavior: seeds 42 and 456 achieve 99.33\\%, while seed 123 yields 91.09\\% (LoRA initialization outlier, fail recall = 70.5\\%).}\n\\label{tab:full_deepseek}\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llcc}\n\\toprule\n\\textbf{Condition} & \\textbf{Seed} & \\textbf{Accuracy} & \\textbf{Notes} \\\\\n\\midrule\nexception\\_only & 42  & 99.33 & epoch 1: 99.83 \\\\\nexception\\_only & 456 & 99.33 & CI [98.82, 99.75] \\\\\nexception\\_only & 123 & 91.09 & fail recall = 70.5\\%; CI [89.40, 92.60] \\\\\n\\midrule\nVOTA                     & 42  & 84.45 & \\\\\nno\\_trace       & 42  & 73.36 & \\\\\nfull\\_trace     & 42  & 79.16 & CI [76.80, 81.30] \\\\\n\\bottomrule\n\\end{tabular}%\n}\n\\end{table}\n\n%% ============================================================\n\\section{Tokenizer and Truncation Analysis}\n\\label{sec:tokenizer_analysis}\n\nThe VOTA cross-model gap (14.96pp, Table~\\ref{tab:cross_model}; confounded by tokenizer-driven truncation; 91.7\\% of DeepSeek training samples were affected) is driven by a training-time truncation asymmetry.\nThe DeepSeek tokenizer averages 2{,}626 tokens per VOTA sample versus 1{,}929 for Qwen, causing 91.7\\% of DeepSeek VOTA training samples to exceed the 2{,}048-token context window.\nThe training framework preserves the verdict label but truncates trace content, so the model trains with incomplete diagnostic information for the majority of samples.\n\nA post-hoc group analysis provides directional evidence: partitioning DeepSeek VOTA test samples by whether their training-set counterparts exceeded the context window, intact samples ($N{=}99$) achieve 100\\% accuracy while truncated samples ($N{=}1{,}091$) achieve 83.04\\% (95\\% CI [80.75\\%, 85.24\\%]; Fisher exact $p{<}0.001$), with all 185 errors concentrated in the fail class (fail recall = 31.23\\%).\nPer-class analysis (Table~\\ref{tab:per_class}) confirms that DeepSeek VOTA achieves 100\\% fail precision but only 45.43\\% fail recall, systematically defaulting to \\texttt{pass}, in contrast to Qwen VOTA, which achieves 100\\% fail recall.\n\nSeed robustness diverges across models: Qwen \\texttt{exception\\_only} produces identical 99.83\\% across all three seeds ($\\sigma{=}0$), while DeepSeek shows bimodal behavior: seeds 42 and 456 achieve 99.33\\% (fail recall = 100\\%), seed 123 yields 91.09\\% (fail recall = 70.5\\%).\nBecause \\texttt{exception\\_only} test inputs contain 48.99\\% duplicates (607 unique of 1,190; \\S\\ref{sec:dataset}), CIs assume $n{=}1{,}190$ independent trials; under deduplication ($n{=}607$), Qwen's accuracy is 99.67\\% (Wilson CI [98.81, 99.91]).\n\n%% ============================================================\n\\section{Irreducible Sample Analysis}\n\\label{sec:irreducible}\n\nThe \\texttt{exception\\_only} condition with Qwen-2.5-Coder-7B misclassifies exactly 2 out of 1,190 test samples across all three seeds (42, 123, 456), with 100\\% overlap across seeds.\nBoth samples (IDs 901 and 905) share the following characteristics:\n\n\\begin{itemize}\n\\item \\textbf{Function:} \\texttt{check\\_dict\\_case} (HumanEval/95), a function that checks whether all dictionary keys are uniformly upper-case or lower-case strings.\n\\item \\textbf{Ground-truth label:} \\texttt{pass}.\n\\item \\textbf{Predicted label:} \\texttt{fail} (false negative).\n\\item \\textbf{Cross-seed consistency:} Both samples are misclassified identically by all three seeds, indicating a systematic rather than stochastic error.\n\\end{itemize}\n\nManual inspection reveals the root cause: \\texttt{check\\_dict\\_case} uses \\texttt{all()} over a generator expression, and Python's \\texttt{all()} short-circuits on the first \\texttt{True} value, raising \\texttt{GeneratorExit} to terminate the generator.\nBecause \\texttt{GeneratorExit} is a \\texttt{BaseException} subclass, the tracer records it as seven \\texttt{[ERROR] GeneratorExit} lines, even though the function executes correctly and the test passes.\nThe model observes these spurious error markers and reasonably but incorrectly predicts \\texttt{fail}.\nThis is not a model failure but a representation ambiguity: the \\texttt{exception\\_only} format cannot distinguish genuine exceptions from benign \\texttt{BaseException} subclasses triggered by Python's iterator protocol.\n\nMost configurations converge to these same 2 errors: Qwen-1.5B, Qwen-7B (3 seeds), CodeLlama-13B (seeds 42/456), and DeepSeek-6.7B (seeds 42/456) all produce error set $\\{901, 905\\}$.\nHowever, CodeLlama-13B seed 123 achieves 100\\% accuracy (0/1190 errors), correctly classifying both samples.\nThis demonstrates that 99.83\\% is a near-perfect \\emph{floor} (the convergence attractor for most LoRA initializations) rather than a hard data ceiling: the representation supports perfect accuracy, but most initializations converge to the same 2-error basin.\nThe practical implication is that these errors are high-probability convergence artifacts addressable through seed selection or ensemble methods, not fundamental limitations of the exception-based representation.\n\n%% ============================================================\n\\section{Exception Type Accuracy Breakdown}\n\\label{sec:exception_type}\n\nTable~\\ref{tab:exception_type} reports \\texttt{exception\\_only} accuracy stratified by exception type on Qwen-2.5-7B (seed=42, $N{=}1{,}190$).\nAll standard exception types (\\texttt{TypeError}, \\texttt{ValueError}, \\texttt{IndexError}, etc.) achieve 100\\% accuracy.\nThe only misclassifications arise from \\texttt{GeneratorExit}, a \\texttt{BaseException} subclass that is not an \\texttt{Exception}. It is raised by Python's iterator protocol during generator short-circuiting, not by actual program errors.\n\n\\begin{table}[t]\n\\centering\n\\caption{Exception type accuracy breakdown for \\texttt{exception\\_only} (Qwen-7B, seed=42). All true error types achieve 100\\%. The only failures come from \\texttt{GeneratorExit} (a \\texttt{BaseException} subclass, not an \\texttt{Exception}), which appears in 2 passing samples.}\n\\label{tab:exception_type}\n\\small\n\\begin{tabular}{lcc}\n\\toprule\n\\textbf{Exception Type} & \\textbf{Samples} & \\textbf{Accuracy} \\\\\n\\midrule\nTypeError & 96 & 100\\% \\\\\nValueError & 62 & 100\\% \\\\\nIndexError & 41 & 100\\% \\\\\nKeyError & 28 & 100\\% \\\\\nAttributeError & 19 & 100\\% \\\\\nAssertionError & 15 & 100\\% \\\\\nRecursionError & 12 & 100\\% \\\\\nOther Exception & 66 & 100\\% \\\\\n\\midrule\nGeneratorExit (BaseException) & 2 & 0\\% \\\\\nNo exception (pass class) & 849 & 100\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThis confirms that the model has learned a clean decision boundary: any true \\texttt{Exception} subclass in the trace implies failure.\nThe \\texttt{GeneratorExit} case represents a semantic ambiguity in the trace format rather than a model failure, as discussed in \\S\\ref{sec:irreducible}.\n\n%% ============================================================\n\\section{Trace Length Ablation}\n\\label{sec:trace_length_full}\n\nTo test whether the \\texttt{full\\_trace} performance gap is caused by input truncation at training time, we vary the maximum trace token budget on Qwen-2.5-7B (seed=42) while keeping all other hyperparameters fixed.\n\n\\begin{table}[t]\n\\centering\n\\caption{Trace length and truncation direction ablation on Qwen-2.5-7B ($N{=}1{,}190$, seed=42). Head = standard left-truncation (retain first $k$ tokens); Tail = retain last $k$ tokens. Per-condition bootstrap 95\\% CIs ($B{=}10{,}000$).}\n\\label{tab:trace_length}\n\\small\n\\begin{tabular}{llcc}\n\\toprule\n\\textbf{Direction} & \\textbf{Max Tokens} & \\textbf{Acc (\\%)} & \\textbf{95\\% CI} \\\\\n\\midrule\nHead & 256  & 78.82 & [76.4, 81.0] \\\\\nHead & 512  & 80.42 & [78.2, 82.6] \\\\\nHead & 1024 & 77.23 & [74.9, 79.6] \\\\\nHead & no\\_limit ($\\infty$) & 81.76 & [79.7, 83.9] \\\\\n\\midrule\nTail & 256  & 77.48 & --- \\\\\nTail & 512  & 93.61 & --- \\\\\nTail & 1024 & 96.47 & --- \\\\\nTail & 2048 & 97.31 & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{budget_curve}\n\\caption{Cross-model tail-truncation budget curve ($N{=}1{,}190$, four models, three architecture families). All models remain near baseline at tail-256/384, then jump +13.7--22.0pp at 384$\\to$512, converging into a 93.6--98.2\\% band by tail-1024. The shaded region marks the transition zone where the exception traceback (${\\sim}$400--500 tokens) is captured. Dashed line: \\texttt{exception\\_only} range (99.3--99.9\\%); dotted line: \\texttt{no\\_trace} range (67--77\\%).}\n\\label{fig:trace_length}\n\\end{figure}\n\nAs shown in Table~\\ref{tab:trace_length} and Figure~\\ref{fig:trace_length}, all four trace length conditions fall within a 5pp range (77.2\\%--81.8\\%).\nTo quantify the reliability of the observed differences, Table~\\ref{tab:trace_length_pairwise} reports paired bootstrap comparisons ($B{=}10{,}000$, seed=42) across all condition pairs.\n\n\\begin{table}[t]\n\\centering\n\\caption{Pairwise paired bootstrap comparisons for trace length ablation ($B{=}10{,}000$, seed=42). $\\Delta$ = accuracy difference between the two conditions (first $-$ second in the budget group; condition $-$ baseline in the other groups). **$p{<}0.01$; ***$p{<}0.001$.}\n\\label{tab:trace_length_pairwise}\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llccc}\n\\toprule\n& \\textbf{Comparison} & \\textbf{$\\Delta$ (pp)} & \\textbf{95\\% CI} & \\textbf{$p$-value} \\\\\n\\midrule\n\\multirow{4}{*}{\\rotatebox{90}{\\scriptsize Budget}}\n& 512 vs.\\ 256           & $+$1.60  & [$-$0.34, $+$3.53]   & 0.117 \\\\\n& 1024 vs.\\ 512          & $-$3.19  & [$-$5.29, $-$1.09]   & 0.002** \\\\\n& no\\_limit vs.\\ 1024    & $+$4.54  & [$+$2.52, $+$6.55]   & ${<}$0.001*** \\\\\n& no\\_limit vs.\\ 256     & $+$2.94  & [$+$0.84, $+$5.04]   & 0.006** \\\\\n\\midrule\n\\multirow{4}{*}{\\rotatebox{90}{\\scriptsize vs.\\ no\\_trace}}\n& 256 $-$ no\\_trace       & $+$3.70  & [$+$1.43, $+$6.05]   & 0.002** \\\\\n& 512 $-$ no\\_trace       & $+$5.29  & [$+$3.03, $+$7.56]   & ${<}$0.001*** \\\\\n& 1024 $-$ no\\_trace      & $+$2.10  & [$-$0.17, $+$4.37]   & 0.078 \\\\\n& no\\_limit $-$ no\\_trace & $+$6.64  & [$+$4.37, $+$8.99]   & ${<}$0.001*** \\\\\n\\midrule\n\\multirow{4}{*}{\\rotatebox{90}{\\scriptsize vs.\\ exc.}}\n& 256 $-$ exc\\_only       & $-$21.01 & [$-$23.45, $-$18.74] & ${<}$0.001*** \\\\\n& 512 $-$ exc\\_only       & $-$19.41 & [$-$21.76, $-$17.14] & ${<}$0.001*** \\\\\n& 1024 $-$ exc\\_only      & $-$22.61 & [$-$25.04, $-$20.25] & ${<}$0.001*** \\\\\n& no\\_limit $-$ exc\\_only & $-$18.07 & [$-$20.34, $-$15.88] & ${<}$0.001*** \\\\\n\\bottomrule\n\\end{tabular}%\n}\n\\end{table}\n\n\\paragraph{Non-monotonic pattern (head-truncation).}\nUnder head-truncation (retaining trace prefixes), the trend is non-monotonic: 512 tokens (80.42\\%) slightly outperforms 256 tokens (78.82\\%), but doubling to 1024 tokens \\emph{decreases} accuracy to 77.23\\%, a statistically significant 3.19pp drop ($p{=}0.002$, 95\\% CI [$-$5.29, $-$1.09]).\nThe no-limit condition (81.76\\%) recovers and significantly exceeds 1024 tokens ($p{<}0.001$), but 1024 tokens is not significantly better than \\texttt{no\\_trace} (75.13\\%; $\\Delta{=}{+}2.10$pp, $p{=}0.078$, 95\\% CI [$-$0.17, $+$4.37]).\nThis non-monotonicity is specific to head-truncation: the 1024-token prefix retains enough irrelevant content to mislead the model while discarding diagnostic events that appear near the trace terminus.\nUnder tail-truncation, accuracy increases monotonically for Qwen-7B and Qwen-1.5B (Table~\\ref{tab:tail_cross_model}); only DeepSeek-6.7B shows a mild $-$1.5pp decrease at tail-1024$\\to$tail-2048, attributable to architecture-specific long-context sensitivity rather than a systematic mid-length pathology.\n\n\\paragraph{Comparison to baselines.}\nAll four trace budget conditions significantly exceed \\texttt{no\\_trace} except 1024 tokens ($p{=}0.078$), confirming that raw trace content provides some signal but unreliably so.\nThe gap to \\texttt{exception\\_only} (99.83\\%) is massive for every budget condition (18--23pp, all $p{<}0.001$), underscoring that even unlimited raw traces cannot substitute for targeted signal extraction.\nThe best full-trace condition (no\\_limit, 81.76\\%) still lags \\texttt{exception\\_only} by 18.07pp (95\\% CI [$-$20.34, $-$15.88]).\n\n\\paragraph{Interpretation.}\nThese results rule out input truncation as the primary explanation for the full-trace performance gap: even with unlimited tokens, the model cannot extract the diagnostic signal that VOTA's targeted compression provides.\nThe non-monotonic dip at 1024 tokens is consistent with a ``worst-of-both-worlds'' regime where the model receives enough noisy context to dilute the signal but not enough to compensate through broader coverage.\nThe result reinforces the information density interpretation (\\S\\ref{sec:density}): the gap between full traces and VOTA is driven by the \\emph{content} of the trace (irrelevant lines diluting the diagnostic signal), not its \\emph{length}.\nIn contrast, VOTA's compressed representation concentrates the diagnostic signal into fewer tokens, making it sensitive to truncation when those tokens are removed (\\S\\ref{sec:cross_model}).\n\n\\paragraph{Truncation direction.}\nTail-truncation (retaining the last $k$ tokens) dramatically outperforms head-truncation: \\texttt{tail\\_2048} achieves 97.31\\% vs.\\ \\texttt{head\\_2048} (no\\_limit) at 81.76\\%, a 15.55pp improvement.\nEven \\texttt{tail\\_512} (93.61\\%) exceeds every head-truncation condition by over 11pp.\n\nHowever, \\texttt{tail\\_256} (77.48\\%) performs at the \\texttt{no\\_trace} baseline level (75.13\\%), indicating that the diagnostic signal does not reside in the very last trace lines.\nThe critical jump occurs between 256 and 512 tail tokens (+16.13pp), localizing the signal window to approximately 256--512 tokens from the trace terminus.\nThis is consistent with Python's execution model: exception tracebacks and assertion comparisons appear near the end of the trace but are preceded by the final function call frames, placing them typically 300--500 tokens from the terminus rather than at the absolute end.\n\nThe 18.07pp gap from \\texttt{full\\_trace} to \\texttt{exception\\_only} decomposes as: 86\\% positional concentration (recovered by tail-truncation at 2048 tokens) and 14\\% residual content noise (the 2.52pp gap from \\texttt{tail\\_2048} to \\texttt{exception\\_only} that persists regardless of truncation direction).\nThe fact that \\texttt{exception\\_only} (99.83\\%) still outperforms \\texttt{tail\\_2048} (97.31\\%) confirms that semantic extraction (identifying the exception type and message) is superior to positional extraction (keeping a fixed window), because the model need not filter out non-diagnostic lines that happen to fall within the window.\n\n\\paragraph{Cross-model budget curve.}\nTable~\\ref{tab:tail_cross_model} extends the tail-truncation analysis to a full budget sweep across four models spanning three architecture families and an 8.7$\\times$ parameter range.\n\n\\begin{table}[t]\n\\centering\n\\caption{Cross-model tail-truncation budget curve ($N{=}1{,}190$). All four models exhibit a transition between tail-384 and tail-512 (+13--23pp). $\\downarrow$: non-monotonic decrease. $^\\dag$CodeLlama tail-1024 trained with label-only loss to address tokenizer-driven gradient dilution (\\S\\ref{sec:tokenizer_analysis}). $^\\ddag$CodeLlama tail-2048 outlier (41.8\\%): LoRA long-sequence instability under label-only loss; excluded from cross-model analysis.}\n\\label{tab:tail_cross_model}\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lcccccc}\n\\toprule\n\\textbf{Model} & \\textbf{tail-256} & \\textbf{tail-384} & \\textbf{tail-512} & \\textbf{tail-1024} & \\textbf{tail-2048} & \\textbf{exc\\_only} \\\\\n\\midrule\nQwen-7B (7B) & 78.9 & 79.9 & 93.6 & 96.5 & 97.3 & 99.83 \\\\\nDeepSeek (6.7B) & 76.4 & 82.9 & 93.9 & 96.5 & 95.0$\\downarrow$ & 99.33 \\\\\nCodeLlama (13B) & 77.9 & 80.6 & 98.2 & 98.2$^\\dag$ & 41.8$^\\ddag$ & 99.89 \\\\\nQwen-1.5B (1.5B) & 72.6 & 73.6 & 95.6 & 96.6 & 97.9 & 99.83 \\\\\n\\bottomrule\n\\end{tabular}%\n}\n\\end{table}\n\n\\begin{table}[t]\n\\centering\n\\caption{Cross-model truncation direction comparison ($N{=}1{,}190$). Head-truncation retains the first 2,048 tokens; tail-truncation retains the last 2,048. All four models' head-2048 accuracies converge into a narrow 75.3--81.8\\% band (6.5pp), comparable to the tail-256 signal-poor band (72.6--78.9\\%, 6.3pp). $^\\dag$CodeLlama tail-2048 pending retraining (\\S\\ref{sec:tokenizer_analysis}).}\n\\label{tab:head_vs_tail}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Model} & \\textbf{head-2048 (\\%)} & \\textbf{tail-2048 (\\%)} & \\textbf{Gap (pp)} \\\\\n\\midrule\nQwen-1.5B & 75.3 & 97.9 & +22.6 \\\\\nDeepSeek-6.7B & 78.7 & 95.0 & +16.3 \\\\\nCodeLlama-13B & 79.9 & ---$^\\dag$ & ---$^\\dag$ \\\\\nQwen-7B & 81.8 & 97.3 & +15.5 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nFour patterns emerge from the budget curve.\n\\emph{Phase transition between 384 and 512 tokens}: the tail-384 column reveals that the transition is not instantaneous at 256$\\to$512 but localized between 384 and 512 tokens.\nAt tail-384, all four models remain near baseline (73.6--82.9\\%), gaining only +1.0--6.5pp over tail-256.\nThe steep jump occurs at 384$\\to$512: +13.7pp (Qwen-7B), +11.0pp (DeepSeek), +17.6pp (CodeLlama), +22.0pp (Qwen-1.5B), crossing from near-baseline to near-ceiling.\nThis localizes the critical threshold to ${\\sim}$400--500 tokens, consistent with the typical exception traceback length: below ${\\sim}$384 tokens, the traceback is truncated and no diagnostic event is captured; above ${\\sim}$512, it is fully included regardless of model capacity or architecture.\n\n\\emph{Convergence at tail-512+}: once the phase transition is crossed, accuracy converges across all models into a 93.6--98.2\\% band at tail-512 (seed 42).\nMulti-seed validation confirms robustness: across all 12 model$\\times$seed combinations at tail-512 (Table~\\ref{tab:tail512_seeds}), all accuracies fall within [93.61\\%, 98.24\\%], a 4.63pp band that compresses the signal-poor tail-256 spread (6.3pp) by 27\\%.\nCodeLlama-13B shows perfect per-model convergence at tail-512: all three seeds achieve 98.24\\% ($\\sigma{=}$0), consistent with the 13B scale and label-only loss providing a stronger optimization signal in the signal-rich regime (Table~\\ref{tab:tail512_seeds}).\n\n\\begin{table}[t]\n\\centering\n\\caption{Cross-seed convergence at the tail-512 truncation point ($N{=}1{,}190$ per seed). All 12 model$\\times$seed combinations fall within a 4.63pp band [93.61\\%, 98.24\\%]. CodeLlama-13B achieves identical accuracy across all three seeds ($\\sigma{=}$0).}\n\\label{tab:tail512_seeds}\n\\small\n\\begin{tabular}{lccccr}\n\\toprule\n\\textbf{Model} & \\textbf{S42} & \\textbf{S123} & \\textbf{S456} & \\textbf{Mean} & \\textbf{$\\sigma$} \\\\\n\\midrule\nQwen-7B (7B)      & 93.61 & 96.00 & 97.65 & 95.75 & 2.05 \\\\\nDeepSeek (6.7B)    & 93.95 & 95.04 & 96.10 & 95.03 & 1.08 \\\\\nQwen-1.5B (1.5B)  & 95.63 & 97.65 & 96.72 & 96.67 & 1.01 \\\\\nCodeLlama (13B)    & 98.24 & 98.24 & 98.24 & \\textbf{98.24} & \\textbf{0.00} \\\\\n\\midrule\n\\multicolumn{4}{l}{Cross-model band} & \\multicolumn{2}{r}{[93.61, 98.24] = 4.63pp} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nAt tail-1024, four models reach 96.5--98.2\\% (CodeLlama 98.2\\% under label-only loss, three others 96.5--96.6\\%).\nScale and architecture differences that dominate the signal-poor regime (tail-256 range: 72.6--78.9\\%, 6.3pp) compress dramatically in the signal-rich regime.\n\n\\emph{Signal-poor convergence band}: head-2048 accuracies across all four models also converge into a narrow 75.3--81.8\\% band (6.5pp; Table~\\ref{tab:head_vs_tail}), comparable in width to the tail-256 band (72.6--78.9\\%, 6.3pp).\nWhen the diagnostic signal is absent (head-truncation discards trace terminus) or unreachable (tail-256 is too short), models of different scale and architecture collapse to similar performance, suggesting a shared floor determined by code comprehension rather than trace processing.\n\n\\emph{Scale behavior inversion}: in the signal-poor regime (tail-256), smaller models perform worse (Qwen-1.5B 72.6\\% vs.\\ Qwen-7B 78.9\\%, $-$6.3pp), mirroring the \\texttt{no\\_trace} scale pattern.\nIn the signal-rich regime (tail-512+), this reverses: Qwen-1.5B matches or exceeds Qwen-7B (95.6\\% vs.\\ 93.6\\% at tail-512; 97.9\\% vs.\\ 97.3\\% at tail-2048), confirming that sufficient trace signal eliminates the capacity advantage.\n\n\\emph{Non-monotonicity at long sequences}: two models show accuracy decreases beyond tail-1024.\nDeepSeek-6.7B drops $-$1.5pp from tail-1024 (96.5\\%) to tail-2048 (95.0\\%), consistent with its known long-context sensitivity (\\S\\ref{sec:training_dynamics}).\nCodeLlama-13B exhibits a more severe collapse: tail-2048 under label-only loss drops to 41.8\\% (vs.\\ tail-1024 = 98.2\\%), which we attribute to LoRA long-sequence instability under the label-only loss regime; this outlier is excluded from cross-model tail-2048 analysis.\nQwen-7B and Qwen-1.5B increase monotonically across all budgets.\n\nTable~\\ref{tab:head_vs_tail} confirms the truncation direction effect: among the three models with complete data, tail-2048 outperforms head-2048 by 15.5--22.6pp.\nThe gap is largest for Qwen-1.5B (+22.6pp), indicating that smaller models benefit most from positional proximity to the diagnostic signal, as they lack the capacity to locate it within longer, noisier prefixes.\n\n%% ============================================================\n\\section{Calibration Analysis}\n\\label{sec:calibration_full}\n\nBeyond accuracy, we evaluate whether trace conditions affect prediction calibration, motivated by recent findings that code LLM confidence is often poorly calibrated \\citep{spiess2025calibration}.\n\n\\begin{table}[t]\n\\centering\n\\caption{Calibration metrics on Qwen-2.5-7B ($N{=}1{,}190$, seed=42). ECE = expected calibration error; Brier = Brier score. Lower is better for both.}\n\\label{tab:calibration}\n\\small\n\\begin{tabular}{lcc}\n\\toprule\n\\textbf{Condition} & \\textbf{ECE $\\downarrow$} & \\textbf{Brier $\\downarrow$} \\\\\n\\midrule\nae\\_only & \\textbf{0.0004} & \\textbf{0.0008} \\\\\nexception\\_only & 0.0027 & 0.0013 \\\\\nVOTA & 0.0054 & 0.005 \\\\\nfull\\_trace & 0.096 & 0.144 \\\\\nno\\_trace & 0.171 & 0.197 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:calibration} shows that calibration quality mirrors the Tier~1/2 hierarchy.\nTier~1 conditions (\\texttt{ae\\_only}: ECE=0.0004; \\texttt{exception\\_only}: ECE=0.0027) produce near-perfectly calibrated predictions, while \\texttt{full\\_trace} (ECE=0.096) and \\texttt{no\\_trace} (ECE=0.171) exhibit substantial miscalibration.\nVOTA (ECE=0.0054) is well-calibrated but slightly worse than either Tier~1 component alone, reinforcing the pattern that combining trace signals dilutes rather than improves the prediction signal.\n\nThe Brier scores tell a consistent story: \\texttt{ae\\_only} (0.0008) and \\texttt{exception\\_only} (0.0013) achieve near-zero scores, while \\texttt{no\\_trace} (0.197) indicates substantial miscalibration.\n\n\\paragraph{Cross-model calibration.}\nTable~\\ref{tab:calibration_cross} extends the calibration analysis to three models under \\texttt{exception\\_only}.\nAll three models achieve ECE ${<}$ 0.007 and Brier ${<}$ 0.007, confirming that calibration quality generalizes across architectures.\nCodeLlama-13B achieves the lowest ECE (0.0020) and MCE (0.0411), while DeepSeek-6.7B shows the highest ECE (0.0064) and Brier (0.0061), consistent with its higher error rate (8 errors vs.\\ 2 for Qwen/CodeLlama).\n\n\\begin{table}[t]\n\\centering\n\\caption{Cross-model calibration for \\texttt{exception\\_only} ($N{=}1{,}190$, seed=42). ECE = expected calibration error; Brier = Brier score; MCE = maximum calibration error. All models achieve ECE ${<}$ 0.007.}\n\\label{tab:calibration_cross}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Model} & \\textbf{ECE $\\downarrow$} & \\textbf{Brier $\\downarrow$} & \\textbf{MCE $\\downarrow$} \\\\\n\\midrule\nCodeLlama-13B & \\textbf{0.0020} & \\textbf{0.0013} & \\textbf{0.0411} \\\\\nQwen-7B & 0.0027 & \\textbf{0.0013} & 0.8355 \\\\\nDeepSeek-6.7B & 0.0064 & 0.0061 & 0.7756 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{fig2_calibration}\n\\caption{Reliability diagrams for four trace conditions on Qwen-2.5-7B ($N{=}1{,}190$, seed=42). \\texttt{exception\\_only} (ECE=0.0027) clusters near the diagonal, while \\texttt{no\\_trace} (ECE=0.171) exhibits systematic overconfidence, a 63$\\times$ gap.}\n\\label{fig:calibration}\n\\end{figure}\n\n%% ============================================================\n\\section{Error Overlap Analysis}\n\\label{sec:error_overlap}\n\nWe analyze the overlap between error sets of different conditions to determine whether they fail on the same samples (Figure~\\ref{fig:error_overlap}).\n\n\\texttt{exception\\_only}'s 2 errors (samples 901 and 905) have zero intersection with the error sets of all other conditions (Jaccard = 0.000 in all pairwise comparisons).\nThis orthogonality arises because \\texttt{exception\\_only} errors are caused by \\texttt{GeneratorExit} false positives (pass samples misclassified as fail due to benign \\texttt{BaseException} events), while errors from other conditions are predominantly fail samples misclassified as pass due to insufficient signal.\n\nAmong non-exception conditions, error sets exhibit hierarchical containment: \\texttt{ae\\_only} $\\subset$ VOTA $\\subset$ \\texttt{loop\\_only} $\\subset$ \\texttt{no\\_trace}, with pairwise Jaccard indices increasing with signal overlap.\n\\texttt{loop\\_only} and \\texttt{full\\_trace} share the highest overlap (Jaccard ${\\sim}$0.65), reflecting their shared reliance on behavioral patterns rather than explicit fault indicators.\n\nThis analysis confirms that \\texttt{exception\\_only} operates on an independent signal dimension: its errors are representation ambiguities (iterator protocol artifacts) rather than information deficits, explaining why combining it with other signals cannot eliminate these specific errors.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{error_overlap}\n\\caption{Jaccard similarity between error sets of different conditions (Qwen-7B, seed=42, $N{=}1{,}190$). \\texttt{exception\\_only} (exc\\_only) has zero overlap with all other conditions, confirming it operates on an independent signal dimension.}\n\\label{fig:error_overlap}\n\\end{figure}\n\n%% ============================================================\n\\section{Cross-Dataset Generalization: DebugBench}\n\\label{sec:debugbench_full}\n\nTo test whether exception-based verdict prediction generalizes beyond LLM-generated solutions, we evaluate on DebugBench \\citep{tian2024debugbench}, a dataset of human-written programs with synthetically injected bugs (single-point mutations such as operator replacement, variable misuse, and missing statements).\nAfter filtering for executable Python samples with valid traces, we retain 426 samples with a near-balanced class distribution (majority baseline: 51.4\\%).\n\n\\begin{table}[t]\n\\centering\n\\caption{Generalization to DebugBench ($N{=}426$, Qwen-2.5-7B, seed=42). Wilson 95\\% CIs. The component ranking (exception\\_only $\\geq$ VOTA $>$ no\\_trace) is preserved, and exception\\_only achieves perfect accuracy.}\n\\label{tab:debugbench}\n\\small\n\\begin{tabular}{lcc}\n\\toprule\n\\textbf{Condition} & \\textbf{Acc (\\%)} & \\textbf{95\\% CI} \\\\\n\\midrule\nexception\\_only & \\textbf{100.00} & [99.14, 100.00] \\\\\nVOTA & 99.77 & [99.30, 100.00] \\\\\nno\\_trace & 96.71 & [94.80, 98.40] \\\\\n\\midrule\nMajority baseline & 51.41 & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:debugbench} shows that the component ranking from the main experiments is preserved: \\texttt{exception\\_only} (100.00\\%) $\\geq$ VOTA (99.77\\%) $>$ \\texttt{no\\_trace} (96.71\\%).\nThe \\texttt{exception\\_only} condition achieves perfect accuracy, confirming that the exception-based representation generalizes to a different fault distribution without degradation.\n\nThe absolute margins are much narrower than on the main dataset: the \\texttt{no\\_trace} baseline already achieves 96.71\\% (compared to 75.13\\% on HumanEval+MBPP), leaving only 3.29pp of headroom for trace-based improvement.\nThis ceiling effect reflects a fundamental difference in fault characteristics: DebugBench bugs are synthetically injected single-point mutations, which produce code that is structurally dissimilar from the original correct solution; a model can often identify the fault from source code alone.\nIn contrast, the HumanEval+MBPP solutions are LLM-generated, producing natural errors (logic mistakes, edge-case failures) where the faulty and correct solutions may be structurally similar, making code-only verdict prediction substantially harder.\n\nThese results support exception-based verdict prediction as a generalizable approach: the method does not degrade on an out-of-distribution dataset, and the exception dominance ranking (exception\\_only $\\geq$ VOTA $>$ no\\_trace) is consistent across both datasets. However, the narrow DebugBench margins are insufficient to independently validate trace importance.\nThe 24.70pp trace lift on the main dataset (no\\_trace 75.13\\% $\\to$ exception\\_only 99.83\\%) remains the primary evidence for the value of exception-based trace signals.\n\n%% ============================================================\n\\section{Cross-Model Robustness Analysis}\n\\label{sec:robustness_analysis}\n\nThe cross-model gap pattern (Table~\\ref{tab:cross_model}) suggests a design principle: \\emph{trace representations should match the model capability floor, not the ceiling.}\nException events are consistently the most effective component on both models, and their structural simplicity (a fixed-format error message) ensures that the relative advantage over richer representations holds across all seeds.\nTwo of three DeepSeek seeds match Qwen-level accuracy (99.33\\%); the outlier (seed 123, 91.09\\%) we hypothesize reflects LoRA initialization sensitivity landing in a suboptimal basin (fail recall = 70.5\\%, though direct evidence is lacking), not a failure of the exception signal itself; even this outlier outperforms VOTA (84.45\\%) by 6.64pp.\nThe VOTA cross-model gap is confounded by two factors: (1)~tokenizer efficiency (the DeepSeek tokenizer averages 2{,}626 tokens per VOTA sample versus Qwen's 1{,}929, causing 91.7\\% of training samples to exceed the 2{,}048-token context window; content-aware truncation preferentially removes the terminal structured prompt, preserving the verdict label but truncating trace content) and (2)~base model capability differences, consistent with findings that SFT generalization depends on pretrain quality \\citep{yang2024generalization}.\nThe two factors cannot be disentangled in the current experimental design.\nOur \\texttt{exception\\_only} design sidesteps the truncation confound entirely: inputs have a median of 150 tokens (mean 398), well below the 2{,}048-token context window, so no training samples are truncated on either model.\nThe resulting 0.56pp cross-model gap (Table~\\ref{tab:cross_model}) is therefore a clean measure of model capability differences, making the ``capability floor'' principle directly testable.\nThe practical implication is that trace-based systems should default to the simplest sufficient signal; for smaller models, training stability (multi-seed selection, warmup schedules) is a secondary but addressable concern.\n\n%% ============================================================\n\\section{Training Dynamics and Loss Decoupling}\n\\label{sec:training_dynamics}\n\nThe DeepSeek \\texttt{exception\\_only} results reveal two instructive training dynamics.\nFirst, epoch-level analysis shows mild degradation in 2/3 seeds: seed 42 peaks at 99.83\\% after epoch~1 but settles at 99.33\\% by epoch~3 ($-$0.50pp), seed 123 degrades from 91.43\\% to 91.09\\% ($-$0.34pp), while seed 456 shows no epoch degradation (99.33\\% at both epoch~1 and epoch~3).\nEarly stopping may yield marginal gains for some seeds, but the epoch effect is small (${\\leq}$0.5pp) compared to the seed effect (8.24pp between seeds 42 and 123).\n\nSecond, seeds 123 and 456 converge to nearly identical final training losses (0.122 and 0.123 respectively), yet their accuracies differ by 8.24pp (91.09\\% vs.\\ 99.33\\%).\nThe critical difference lies in fail recall: seeds 42 and 456 achieve 100\\%, while seed 123 achieves only 70.5\\%. The LoRA initialization in seed 123 fails to learn the exception$\\to$fail mapping for a substantial fraction of failing samples, even though the per-token loss appears converged.\nThis demonstrates that token-level training loss can mask fundamental differences in sample-level classification ability, suggesting a parallel to the eval-loss/accuracy decoupling observed in DeepSeek VOTA (where eval loss rose 65\\% from epoch 1 to 3 while accuracy improved by 6.3pp) at the training phase.\nThe practical recommendation is twofold: (1)~use task-specific metrics (accuracy, fail recall) for checkpoint and seed selection rather than training or evaluation loss, and (2)~for deployment on smaller models, train multiple seeds and select the best, as a single run may not reliably converge to the correct classification boundary.\n\n\\paragraph{Format collapse, not semantic failure.}\nThe 100 errors of seed 123 are not semantic failures but generation format collapse: on inputs exceeding 4,000 characters (those containing verbose locals dumps), the model echoes trace content instead of emitting a verdict token, while achieving zero errors on shorter inputs.\nThis indicates that the LoRA initialization of seed 123 specifically compromises long-context format compliance rather than exception signal comprehension, further supporting the robustness advantage of compact \\texttt{exception\\_only} inputs.\n\nThe contrast with VOTA is instructive: DeepSeek VOTA accuracy monotonically increases from 78.15\\% to 84.45\\% across epochs, but is consistent with a performance limit associated with the high trace truncation rate (\\S\\ref{sec:cross_model}): the model progressively extracts signal from samples with intact trace content but cannot fully compensate for the information loss in the truncated majority.\nThe 84.45\\% accuracy reflects a combination of trace information loss and model capability constraints.\n\n%% ============================================================\n\\section{Deduplication Statistics}\n\\label{sec:dedup_stats}\n\nTable~\\ref{tab:dedup} reports the duplication rates across trace formats.\nBecause multiple passing solutions to the same problem produce identical (input, output) pairs in the \\texttt{exception\\_only} format (correct executions raise no exceptions, so the trace content is the same regardless of the solution's internal logic), the dataset contains duplicate rows.\nTrain--test input overlap is zero (split by problem ID), so no information leakage occurs.\nThe high duplication in \\texttt{exception\\_only} does not affect our experimental conclusions: after deduplication the training set still contains 2,858 unique samples and the test set 607, providing sufficient coverage for the 591-problem benchmark.\n\n\\paragraph{Problem-level partitioning and sensitivity analysis.}\nData is partitioned at the problem level: 472 training problems and 119 test problems, with zero crossover.\nDuplicates arise from multiple candidate solutions per problem (up to 10 solutions each), not from cross-problem overlap.\nTo verify that deduplication does not alter any finding, we ran a sensitivity analysis across all 19 experimental conditions (7 trace formats $\\times$ 4 models, minus conditions not run): deduplication produces a 0.00pp accuracy delta in every case.\nThis confirms that duplicate samples neither inflate nor deflate accuracy, because duplicates share the same ground-truth label and the model's prediction is deterministic at inference time.\nThe \\texttt{exception\\_only} test set contains 48.99\\% duplicate inputs due to representation compactness; all confidence intervals treat samples as independent Bernoulli trials.\n\n\\begin{table}[t]\n\\centering\n\\caption{Deduplication statistics. The \\texttt{exception\\_only} format collapses multiple passing solutions into identical rows because correct executions produce no exception events. Train--test input overlap is 0 (no leakage).}\n\\label{tab:dedup}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Split} & \\textbf{Total} & \\textbf{Unique} & \\textbf{Dup.\\ rate} \\\\\n\\midrule\nexception\\_only train & 4{,}720 & 2{,}858 & 39.45\\% \\\\\nexception\\_only test  & 1{,}190 &   607 & 48.99\\% \\\\\nraw\\_traces (full)    & 5{,}910 & 5{,}803 &  1.81\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n%% ============================================================\n\\section{Regex Baseline Analysis}\n\\label{sec:regex_baselines}\n\nTo establish a non-learning upper bound, we evaluate six regex-based baselines on the \\texttt{exception\\_only} test set ($N{=}1{,}190$) and two format-specific baselines on VOTA and \\texttt{full\\_trace} inputs.\n\n\\begin{table}[t]\n\\centering\n\\caption{Regex baseline accuracy ($N{=}1{,}190$). B4 is the strongest semantic baseline (6.22pp below SFT \\texttt{exception\\_only}, McNemar $p{<}0.001$). B6 uses an error count threshold. $^\\ddag$B5 exploits a data formatting artifact: the \\texttt{[No exception data in trace]} marker is deterministically present in all pass samples, making this a format-level shortcut rather than a genuine exception-based heuristic.}\n\\label{tab:regex}\n\\small\n\\begin{tabular}{llc}\n\\toprule\n\\textbf{Baseline} & \\textbf{Method} & \\textbf{Acc (\\%)} \\\\\n\\midrule\nB1: \\texttt{[ERROR]} presence & string match & 93.45 \\\\\nB2: Traceback presence & string match & 71.51 \\\\\nB3: Any keyword & union of B1+B2+Exception & 93.45 \\\\\nB4: Exception type regex & regex on exception class names & \\textbf{93.61} \\\\\nB5: Format marker & \\texttt{[No exception data]} $\\to$ pass & 99.33$^\\ddag$ \\\\\nB6: Error count $\\geq$2 & count threshold & 92.02 \\\\\n\\midrule\nVOTA format regex & best regex on VOTA traces & 75.55 \\\\\nfull\\_trace format regex & best regex on full traces & 77.39 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe strongest legitimate baseline (B4, 93.61\\%) applies regex pattern-matching on Python exception class names (e.g., \\texttt{ValueError}, \\texttt{TypeError}).\nIts errors concentrate on 8 boundary samples where a \\texttt{ValueError} is raised inside a \\texttt{try/except} block and caught; the program passes despite an exception occurring in the trace.\nSFT \\texttt{exception\\_only} correctly classifies 6 of these 8 samples, indicating that the model learns the semantic distinction between caught (benign) and uncaught (fault-indicating) exceptions.\nB5 (99.33\\%) achieves near-SFT accuracy but relies on the deterministic presence of a format marker in pass-class traces, which is an artifact of the trace preprocessing pipeline rather than a generalizable signal; McNemar test vs.\\ SFT yields $p{=}0.041$, confirming a statistically significant difference.\n\n\\paragraph{Cross-format comparison.}\nTable~\\ref{tab:regex_cross_format} compares SFT and the best applicable regex baseline for each trace format.\nThe SFT advantage increases with format complexity: \\texttt{no\\_trace} (+3.62pp over majority baseline) $<$ \\texttt{full\\_trace} (+4.37pp) $<$ \\texttt{exception\\_only} (+6.22pp) $\\ll$ VOTA (+23.86pp).\nThe VOTA gap is largest because its structured multi-component format carries semantic content that regex cannot parse, while \\texttt{exception\\_only}'s simpler format allows regex to capture most of the signal.\n\n\\begin{table}[t]\n\\centering\n\\caption{SFT vs.\\ best regex baseline by trace format ($N{=}1{,}190$). Regex baselines: majority class for \\texttt{no\\_trace}, keyword matching for \\texttt{full\\_trace}, pattern matching for VOTA, exception type regex (B4) for \\texttt{exception\\_only}.}\n\\label{tab:regex_cross_format}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Format} & \\textbf{SFT (\\%)} & \\textbf{Regex (\\%)} & \\textbf{$\\Delta$ (pp)} \\\\\n\\midrule\nexception\\_only & 99.83 & 93.61 & +6.22 \\\\\nVOTA & 99.05 & 75.55 & +23.50 \\\\\nfull\\_trace & 81.76 & 77.39 & +4.37 \\\\\nno\\_trace & 75.13 & 71.51 & +3.62 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n%% ============================================================\n\\section{Cross-Model Zero-Shot Comparison}\n\\label{sec:zeroshot_cross_model}\n\nTable~\\ref{tab:zeroshot_cross_model} compares zero-shot and SFT \\texttt{exception\\_only} accuracy across four models.\nZero-shot performance does not correlate with model size: the smallest model (Qwen-1.5B, 93.45\\%) outperforms all larger models, while the largest (CodeLlama-13B) falls below majority baseline.\nSFT compresses the 42.44pp zero-shot range to 0.56pp, eliminating architecture-dependent variance.\n\n\\begin{table}[t]\n\\centering\n\\caption{Zero-shot vs.\\ SFT \\texttt{exception\\_only} across four models ($N{=}1{,}190$). Zero-shot accuracy is uncorrelated with model size; SFT normalizes cross-architecture variance from 42.44pp to 0.56pp.}\n\\label{tab:zeroshot_cross_model}\n\\small\n\\begin{tabular}{llccc}\n\\toprule\n\\textbf{Model} & \\textbf{Size} & \\textbf{Zero-shot (\\%)} & \\textbf{SFT (\\%)} & \\textbf{$\\Delta$ (pp)} \\\\\n\\midrule\nQwen-1.5B & 1.5B & 93.45 & 99.83 & +6.38 \\\\\nDeepSeek-6.7B & 6.7B & 90.59 & 99.33 & +8.74 \\\\\nQwen-7B & 7B & 89.08 & 99.83 & +10.75 \\\\\nCodeLlama-13B & 13B & 51.01 & 99.89 & +48.88 \\\\\n\\midrule\nRange & --- & 42.44pp & 0.56pp & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n",
      "numLines": 765,
      "startLine": 1,
      "totalLines": 765
    }
  },
  "sourceToolAssistantUUID": "61f0b016-ba41-4371-b6b5-ffbd7ae987ff",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/.claude/sessions/review_reviewer_1_7624f219",
  "sessionId": "98d2b939-6454-4d7d-877f-2c64a5a37485",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 50 · 2026-05-19T12:52:22.943Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01U9beG4NPRQ4Fmc3VeW1Zug`</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewerguidelines",
  "prompt": "Extract the EXACT numerical scoring scales for: 1) Soundness (what does each score 1-5 mean?), 2) Excitement (what does each score 1-5 mean?), 3) Overall Assessment (what does each score 1-5 mean?). I need the full text description for each score level. Also extract any information about what reviewers should look for regarding: reproducibility, limitations, ethical considerations, confidence score."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "61f6def3-5e4d-46ea-b897-5c6625ee59e3",
  "isSidechain": false,
  "requestId": "req_011CbBxZx4zdNmNNR5SBPDGF",
  "type": "assistant",
  "uuid": "658eec0b-98c6-4fdb-9b7e-7fd15d6d7b37",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/.claude/sessions/review_reviewer_1_7624f219",
  "sessionId": "98d2b939-6454-4d7d-877f-2c64a5a37485",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Qbmhv51dWzSbKXeQBzsmi5",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14130,
      "cache_read_input_tokens": 31258,
      "output_tokens": 308,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 14130,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 308,
          "cache_read_input_tokens": 31258,
          "cache_creation_input_tokens": 14130,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 14130
          },
          "type": "message"
        }
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
  "lastPrompt": "[Round 1 审稿请求]: 你是 Reviewer 1，负责 **方法严谨性 + 实验有效性**。  ## 论文信息 - **标题**: \"Exception Events Are All You Need: Component Ablation for Trace-Based Verdict Prediction\" - **Venue**: EMNLP 2026 (ARR May 2026)…",
  "leafUuid": "658eec0b-98c6-4fdb-9b7e-7fd15d6d7b37",
  "sessionId": "98d2b939-6454-4d7d-877f-2c64a5a37485"
}
```

---

### Runtime record

_source line 52_

```json
{
  "type": "ai-title",
  "aiTitle": "Review trace-based verdict prediction paper methodology",
  "sessionId": "98d2b939-6454-4d7d-877f-2c64a5a37485"
}
```

---

### Tool result

_source line 53 · 2026-05-19T12:52:28.652Z_

<details><summary>↩ Tool result · `toolu_01U9beG4NPRQ4Fmc3VeW1Zug`</summary>

```text
# ARR Reviewer Scoring Scales

I've carefully reviewed the ARR Reviewer Guidelines document, and I must report that **the specific numerical scoring scale definitions (1-5) for Soundness, Excitement, and Overall Assessment are NOT provided in this document**.

The guidelines mention these three scores exist:
- "Starting with February 2025, ARR reviewers are asked to provide three scores: soundness, excitement, and overall recommendation."

However, the detailed rubric for what each numerical level means is absent from this resource.

## What IS Specified:

**Soundness:** Should be "justified by the text of the review" and reflects technical validity.

**Excitement:** Described as "orthogonal to the assessment of soundness" and reflects "personal taste."

**Overall Assessment:** A "composite score reflecting your assessment of soundness, excitement, and also other factors like novelty and impact."

## Additional Reviewer Expectations:

**Reproducibility:** Reviewers should verify "enough details to reproduce the experiments, including hyperparameter selection" and assess "whether the code/data/etc will be publicly available."

**Limitations:** Guidelines warn that "limitations != weaknesses" and advise against simply listing acknowledged limitations as rejection reasons.

**Confidence Score:** The guidelines mention reviewers "will also be able to indicate your confidence score in the ARR form" but provide no scale details.

**Ethical Considerations:** Reviewers should flag papers for ethics review when issues involve data collection ethics, potential harms, or disadvantages for minority groups.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "658eec0b-98c6-4fdb-9b7e-7fd15d6d7b37",
  "isSidechain": false,
  "promptId": "e3f72197-8c21-47a9-99b8-7cd49faae750",
  "type": "user",
  "uuid": "b0363fd0-e4ee-42f4-99dc-7d2f36fb49be",
  "toolUseResult": {
    "bytes": 100603,
    "code": 200,
    "codeText": "OK",
    "result": "# ARR Reviewer Scoring Scales\n\nI've carefully reviewed the ARR Reviewer Guidelines document, and I must report that **the specific numerical scoring scale definitions (1-5) for Soundness, Excitement, and Overall Assessment are NOT provided in this document**.\n\nThe guidelines mention these three scores exist:\n- \"Starting with February 2025, ARR reviewers are asked to provide three scores: soundness, excitement, and overall recommendation.\"\n\nHowever, the detailed rubric for what each numerical level means is absent from this resource.\n\n## What IS Specified:\n\n**Soundness:** Should be \"justified by the text of the review\" and reflects technical validity.\n\n**Excitement:** Described as \"orthogonal to the assessment of soundness\" and reflects \"personal taste.\"\n\n**Overall Assessment:** A \"composite score reflecting your assessment of soundness, excitement, and also other factors like novelty and impact.\"\n\n## Additional Reviewer Expectations:\n\n**Reproducibility:** Reviewers should verify \"enough details to reproduce the experiments, including hyperparameter selection\" and assess \"whether the code/data/etc will be publicly available.\"\n\n**Limitations:** Guidelines warn that \"limitations != weaknesses\" and advise against simply listing acknowledged limitations as rejection reasons.\n\n**Confidence Score:** The guidelines mention reviewers \"will also be able to indicate your confidence score in the ARR form\" but provide no scale details.\n\n**Ethical Considerations:** Reviewers should flag papers for ethics review when issues involve data collection ethics, potential harms, or disadvantages for minority groups.",
    "durationMs": 5704,
    "url": "https://aclrollingreview.org/reviewerguidelines"
  },
  "sourceToolAssistantUUID": "658eec0b-98c6-4fdb-9b7e-7fd15d6d7b37",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/.claude/sessions/review_reviewer_1_7624f219",
  "sessionId": "98d2b939-6454-4d7d-877f-2c64a5a37485",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 54 · 2026-05-19T12:52:32.683Z_

<details><summary>Logged reasoning block</summary>

```text
I've now read through the entire paper. Let me also check the ARR checklist and references, then look at the official ARR review form for scoring. Let me search more specifically for the ARR scoring rubric.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b0363fd0-e4ee-42f4-99dc-7d2f36fb49be",
  "isSidechain": false,
  "requestId": "req_011CbBxb5SXQGgU4nJRG8s2k",
  "type": "assistant",
  "uuid": "af75d0cb-f64f-4852-99f0-546ebe1cf88d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/.claude/sessions/review_reviewer_1_7624f219",
  "sessionId": "98d2b939-6454-4d7d-877f-2c64a5a37485",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0173ZABs8ihQMqhey9dcHAWK",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 19374,
      "cache_read_input_tokens": 45388,
      "output_tokens": 339,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 19374,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 339,
          "cache_read_input_tokens": 45388,
          "cache_creation_input_tokens": 19374,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 19374
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "unavailable"
      }
    }
  }
}
```

</details>

---

### Assistant

_source line 55 · 2026-05-19T12:52:33.340Z_

搜索 ARR 评分量表的具体定义，同时检查引用。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "af75d0cb-f64f-4852-99f0-546ebe1cf88d",
  "isSidechain": false,
  "requestId": "req_011CbBxb5SXQGgU4nJRG8s2k",
  "type": "assistant",
  "uuid": "2c0e5cb0-bfb9-45e0-92ba-3e7e2c977445",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/.claude/sessions/review_reviewer_1_7624f219",
  "sessionId": "98d2b939-6454-4d7d-877f-2c64a5a37485",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0173ZABs8ihQMqhey9dcHAWK",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 19374,
      "cache_read_input_tokens": 45388,
      "output_tokens": 339,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 19374,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 339,
          "cache_read_input_tokens": 45388,
          "cache_creation_input_tokens": 19374,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 19374
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "unavailable"
      }
    }
  }
}
```

</details>

---

### Tool call

_source line 56 · 2026-05-19T12:52:34.896Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01BamDEs6TrKyJCdMvKAbRUk`</summary>

```json
{
  "query": "ACL ARR review form soundness score 1 2 3 4 5 scale definition \"major flaws\" \"minor issues\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2c0e5cb0-bfb9-45e0-92ba-3e7e2c977445",
  "isSidechain": false,
  "requestId": "req_011CbBxb5SXQGgU4nJRG8s2k",
  "type": "assistant",
  "uuid": "648f30d8-1ccd-4f52-a6b1-008d229f1726",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/.claude/sessions/review_reviewer_1_7624f219",
  "sessionId": "98d2b939-6454-4d7d-877f-2c64a5a37485",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0173ZABs8ihQMqhey9dcHAWK",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 19374,
      "cache_read_input_tokens": 45388,
      "output_tokens": 339,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 19374,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 339,
          "cache_read_input_tokens": 45388,
          "cache_creation_input_tokens": 19374,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 19374
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "unavailable"
      }
    }
  }
}
```

</details>

---

### Tool call

_source line 57 · 2026-05-19T12:52:36.836Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__verify_references · `toolu_01XTkqqyPTdPBpCSbPiqukFU`</summary>

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
  "parentUuid": "648f30d8-1ccd-4f52-a6b1-008d229f1726",
  "isSidechain": false,
  "requestId": "req_011CbBxb5SXQGgU4nJRG8s2k",
  "type": "assistant",
  "uuid": "311b3d5f-5139-4484-9357-54b46b4571d0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/.claude/sessions/review_reviewer_1_7624f219",
  "sessionId": "98d2b939-6454-4d7d-877f-2c64a5a37485",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0173ZABs8ihQMqhey9dcHAWK",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 19374,
      "cache_read_input_tokens": 45388,
      "output_tokens": 339,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 19374,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 339,
          "cache_read_input_tokens": 45388,
          "cache_creation_input_tokens": 19374,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 19374
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "unavailable"
      }
    }
  }
}
```

</details>

---

### Tool call

_source line 58 · 2026-05-19T12:52:37.399Z_

<details open><summary>🔧 Tool call — Read · `toolu_01DW2LNGv67YQ8Af1F3cwCzW`</summary>

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
  "parentUuid": "311b3d5f-5139-4484-9357-54b46b4571d0",
  "isSidechain": false,
  "requestId": "req_011CbBxb5SXQGgU4nJRG8s2k",
  "type": "assistant",
  "uuid": "b79d75da-06af-4ca0-87a1-b4ca916628db",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/.claude/sessions/review_reviewer_1_7624f219",
  "sessionId": "98d2b939-6454-4d7d-877f-2c64a5a37485",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0173ZABs8ihQMqhey9dcHAWK",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 19374,
      "cache_read_input_tokens": 45388,
      "output_tokens": 339,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 19374,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 339,
          "cache_read_input_tokens": 45388,
          "cache_creation_input_tokens": 19374,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 19374
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "unavailable"
      }
    }
  }
}
```

</details>

---

### Tool result

_source line 59 · 2026-05-19T12:52:41.270Z_

<details><summary>↩ Tool result · `toolu_01BamDEs6TrKyJCdMvKAbRUk`</summary>

```text
Web search results for query: "ACL ARR review form soundness score 1 2 3 4 5 scale definition "major flaws" "minor issues""

Links: [{"title":"aclrollingreview/reviewerguidelines.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/reviewerguidelines.md"},{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"ACL’23 Peer Review Form - ACL 2023","url":"https://2023.aclweb.org/blog/review-form/"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"ACL’23 Peer Review Policies - ACL 2023","url":"https://2023.aclweb.org/blog/review-acl23/"}]

Based on the search results, I found the ACL/ARR soundness score scale definitions. Here's what the review form specifies:

**5 = Excellent:** This study is one of the most thorough seen, given its type.

**4 = Strong:** This study provides sufficient support for all of its claims. Some extra experiments could be nice, but not essential.

**3 = Acceptable:** This study provides sufficient support for its main claims. Some minor points may need extra support or details.

**2 = Poor:** Some of the main claims are not sufficiently supported.

The search results also provide guidance on these scores: Soundness scores must be justified by the text of the review. If you give a low Soundness score without finding any major faults, this means that your review is not a faithful explanation of your recommendation.

While the specific phrases "major flaws" and "minor issues" you mentioned don't appear in the exact form in the definitions, the scale does distinguish between major problems (2 = Poor, where "main claims are not sufficiently supported") and minor issues (3 = Acceptable, where "some minor points may need extra support or details").


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "648f30d8-1ccd-4f52-a6b1-008d229f1726",
  "isSidechain": false,
  "promptId": "e3f72197-8c21-47a9-99b8-7cd49faae750",
  "type": "user",
  "uuid": "6995ac02-1f53-4f66-acb3-a3b867676b90",
  "toolUseResult": {
    "query": "ACL ARR review form soundness score 1 2 3 4 5 scale definition \"major flaws\" \"minor issues\"",
    "results": [
      {
        "tool_use_id": "srvtoolu_01QkmkhcUyYurxdmztKxkcRF",
        "content": [
          {
            "title": "aclrollingreview/reviewerguidelines.md at main · acl-org/aclrollingreview",
            "url": "https://github.com/acl-org/aclrollingreview/blob/main/reviewerguidelines.md"
          },
          {
            "title": "ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics",
            "url": "http://aclrollingreview.org/reviewerguidelines"
          },
          {
            "title": "ACL’23 Peer Review Form - ACL 2023",
            "url": "https://2023.aclweb.org/blog/review-form/"
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
            "title": "Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics",
            "url": "http://aclrollingreview.org/authors"
          },
          {
            "title": "ACL’23 Peer Review Policies - ACL 2023",
            "url": "https://2023.aclweb.org/blog/review-acl23/"
          }
        ]
      },
      "Based on the search results, I found the ACL/ARR soundness score scale definitions. Here's what the review form specifies:\n\n**5 = Excellent:** This study is one of the most thorough seen, given its type.\n\n**4 = Strong:** This study provides sufficient support for all of its claims. Some extra experiments could be nice, but not essential.\n\n**3 = Acceptable:** This study provides sufficient support for its main claims. Some minor points may need extra support or details.\n\n**2 = Poor:** Some of the main claims are not sufficiently supported.\n\nThe search results also provide guidance on these scores: Soundness scores must be justified by the text of the review. If you give a low Soundness score without finding any major faults, this means that your review is not a faithful explanation of your recommendation.\n\nWhile the specific phrases \"major flaws\" and \"minor issues\" you mentioned don't appear in the exact form in the definitions, the scale does distinguish between major problems (2 = Poor, where \"main claims are not sufficiently supported\") and minor issues (3 = Acceptable, where \"some minor points may need extra support or details\")."
    ],
    "durationSeconds": 6.369015096999996
  },
  "sourceToolAssistantUUID": "648f30d8-1ccd-4f52-a6b1-008d229f1726",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/.claude/sessions/review_reviewer_1_7624f219",
  "sessionId": "98d2b939-6454-4d7d-877f-2c64a5a37485",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 60 · 2026-05-19T12:53:25.510Z_

<details><summary>↩ Tool result · `toolu_01XTkqqyPTdPBpCSbPiqukFU`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"summary\": {\"total_bib_entries\": 54, \"total_citations\": 69, \"unique_cited_keys\": 54, \"orphan_bib\": 0, \"missing_bib\": 0, \"duplicate_keys\": 0, \"online_verified\": 39, \"online_not_found\": 8, \"online_mismatch\": 7}, \"cross_check\": {\"orphan_bib\": [], \"missing_bib\": [], \"orphan_count\": 0, \"missing_count\": 0}, \"bib_entries\": [{\"key\": \"chen2025tracepile\", \"type\": \"inproceedings\", \"title\": \"Chain of Execution Supervision Promotes General Reasoning in Large Language Models\", \"authors\": \"Nuo Chen and Zehua Li and Keqin Bao and Junyang Lin and Dayiheng Liu\", \"year\": \"2025\", \"venue\": \"Advances in Neural Information Processing Systems (NeurIPS)\"}, {\"key\": \"ding2024traced\", \"type\": \"inproceedings\", \"title\": \"TRACED: Execution-aware Pre-training for Source Code\", \"authors\": \"Yangruibo Ding and Ben Steenhoek and Kexin Pei and Gail Kaiser and Wei Le and Ba...\", \"year\": \"2024\", \"venue\": \"Proceedings of the 46th IEEE/ACM International Conference on Software Engineerin...\"}, {\"key\": \"chen2021evaluating\", \"type\": \"article\", \"title\": \"Evaluating Large Language Models Trained on Code\", \"authors\": \"Chen, Mark and Tworek, Jerry and Jun, Heewoo and Yuan, Qiming and Pinto, Henriqu...\", \"year\": \"2021\", \"venue\": \"arXiv preprint arXiv:2107.03374\"}, {\"key\": \"austin2021program\", \"type\": \"article\", \"title\": \"Program Synthesis with Large Language Models\", \"authors\": \"Austin, Jacob and Odena, Augustus and Nye, Maxwell and Bosma, Maarten and Michal...\", \"year\": \"2021\", \"venue\": \"arXiv preprint arXiv:2108.07732\"}, {\"key\": \"gu2024cruxeval\", \"type\": \"inproceedings\", \"title\": \"CRUXEval: A Benchmark for Code Reasoning, Understanding and Execution\", \"authors\": \"Alex Gu and Baptiste Rozi\\\\`ere and Hugh Leather and Armando Solar-Lezama and Gab...\", \"year\": \"2024\", \"venue\": \"Proceedings of the 41st International Conference on Machine Learning (ICML)\"}, {\"key\": \"hu2022lora\", \"type\": \"inproceedings\", \"title\": \"LoRA: Low-Rank Adaptation of Large Language Models\", \"authors\": \"Edward J. Hu and Yelong Shen and Phillip Wallis and Zeyuan Allen-Zhu and Yuanzhi...\", \"year\": \"2022\", \"venue\": \"Proceedings of the 10th International Conference on Learning Representations (IC...\"}, {\"key\": \"qwen2025coder\", \"type\": \"article\", \"title\": \"Qwen2.5-Coder Technical Report\", \"authors\": \"Qwen Team\", \"year\": \"2024\", \"venue\": \"arXiv preprint arXiv:2409.12186\"}, {\"key\": \"deepseek2024coder\", \"type\": \"article\", \"title\": \"DeepSeek-Coder: When the Large Language Model Meets Programming -- The Rise of Code Intelligence\", \"authors\": \"Daya Guo and Qihao Zhu and Dejian Yang and Zhenda Xie and Kai Dong and Wentao Zh...\", \"year\": \"2024\", \"venue\": \"arXiv preprint arXiv:2401.14196\"}, {\"key\": \"wang2025dcsh\", \"type\": \"inproceedings\", \"title\": \"Do Code Semantics Help? A Comprehensive Study on Execution Trace-Based Information for Code Large Language Models\", \"authors\": \"Jian Wang and Xiaofei Xie and Qiang Hu and Shangqing Liu and Yi Li\", \"year\": \"2025\", \"venue\": \"Findings of the Association for Computational Linguistics: EMNLP 2025\"}, {\"key\": \"ni2024next\", \"type\": \"inproceedings\", \"title\": \"NExT: Teaching Large Language Models to Reason about Code Execution\", \"authors\": \"Ansong Ni and Miltiadis Allamanis and Arman Cohan and Yinlin Deng and Kensen Shi...\", \"year\": \"2024\", \"venue\": \"Proceedings of the 41st International Conference on Machine Learning (ICML)\"}, {\"key\": \"eguchi2025etcot\", \"type\": \"inproceedings\", \"title\": \"Making LLMs Program Interpreters via Execution Trace Chain of Thought\", \"authors\": \"Koshi Eguchi and Takuya Akiba\", \"year\": \"2025\", \"venue\": \"ICML 2025 Workshop on Programmatic Representations for Agent Learning (PRAL)\"}, {\"key\": \"ferrando2025execute\", \"type\": \"article\", \"title\": \"What I Cannot Execute, I Do Not Understand: Training and Evaluating LLMs on Program Execution Traces\", \"authors\": \"Jordi Armengol-Estape and Quentin Carbonneaux and Tianjun Zhang and Aram H. Mark...\", \"year\": \"2025\", \"venue\": \"arXiv preprint arXiv:2503.05703\"}, {\"key\": \"xu2025cruxevalx\", \"type\": \"inproceedings\", \"title\": \"CRUXEval-X: A Benchmark for Multilingual Code Reasoning, Understanding and Execution\", \"authors\": \"Ruiyang Xu and others\", \"year\": \"2025\", \"venue\": \"Proceedings of the 63rd Annual Meeting of the Association for Computational Ling...\"}, {\"key\": \"appt2024\", \"type\": \"article\", \"title\": \"APPT: Boosting Automated Patch Correctness Prediction via Fine-tuning Pre-trained Models\", \"authors\": \"Quanjun Zhang and Chunrong Fang and Weisong Sun and Yan Liu and Tieke He and Xia...\", \"year\": \"2024\", \"venue\": \"IEEE Transactions on Software Engineering\"}, {\"key\": \"zhou2024llm4patch\", \"type\": \"article\", \"title\": \"Leveraging Large Language Model for Automatic Patch Correctness Assessment\", \"authors\": \"Xin Zhou and Bowen Xu and Kisub Kim and DongGyun Han and Hung Huu Nguyen and Tha...\", \"year\": \"2024\", \"venue\": \"IEEE Transactions on Software Engineering\"}, {\"key\": \"spiess2025calibration\", \"type\": \"inproceedings\", \"title\": \"Calibration and Correctness of Language Models for Code\", \"authors\": \"Claudio Spiess and David Gros and others\", \"year\": \"2025\", \"venue\": \"Proceedings of the 47th IEEE/ACM International Conference on Software Engineerin...\"}, {\"key\": \"foster2025mutation\", \"type\": \"inproceedings\", \"title\": \"Mutation-Guided LLM-based Test Generation at Meta\", \"authors\": \"Christopher Foster and Abhishek Gulati and Mark Harman and Inna Harper and Ke Ma...\", \"year\": \"2025\", \"venue\": \"Proceedings of the ACM International Conference on the Foundations of Software E...\"}, {\"key\": \"widyasari2024fusefl\", \"type\": \"inproceedings\", \"title\": \"Demystifying Faulty Code: Step-by-Step Reasoning for Explainable Fault Localization\", \"authors\": \"Ratnadira Widyasari and Jia Wei Ang and Truong Giang Nguyen and Neil Sharma and ...\", \"year\": \"2024\", \"venue\": \"Proceedings of the IEEE International Conference on Software Analysis, Evolution...\"}, {\"key\": \"huang2026tracecoder\", \"type\": \"inproceedings\", \"title\": \"TraceCoder: A Trace-Driven Multi-Agent Framework for Automated Debugging of LLM-Generated Code\", \"authors\": \"Jiangping Huang and Wenguang Ye and Weisong Sun and Jian Zhang and Mingyue Zhang...\", \"year\": \"2026\", \"venue\": \"Proceedings of the 48th IEEE/ACM International Conference on Software Engineerin...\"}, {\"key\": \"wang2025inspectcoder\", \"type\": \"article\", \"title\": \"InspectCoder: Dynamic Analysis-Enabled Self Repair through Interactive LLM-Debugger Collaboration\", \"authors\": \"Yunkun Wang and Yue Zhang and Guochang Li and Chen Zhi and Binhua Li and Fei Hua...\", \"year\": \"2025\", \"venue\": \"arXiv preprint arXiv:2510.18327\"}, {\"key\": \"haque2025traces\", \"type\": \"inproceedings\", \"title\": \"Towards Effectively Leveraging Execution Traces for Program Repair with Code LLMs\", \"authors\": \"Mirazul Haque and Petr Babkin and Farima Farmahinifarahani and Manuela Veloso\", \"year\": \"2025\", \"venue\": \"KnowledgeNLP Workshop at ACL 2025\"}, {\"key\": \"yang2024generalization\", \"type\": \"inproceedings\", \"title\": \"Unveiling the Generalization Power of Fine-Tuned Large Language Models\", \"authors\": \"Haoran Yang and Yumeng Zhang and Jiaqi Xu and Hongyuan Lu and Pheng Ann Heng and...\", \"year\": \"2024\", \"venue\": \"Proceedings of the 2024 Conference of the North American Chapter of the Associat...\"}, {\"key\": \"tian2024debugbench\", \"type\": \"inproceedings\", \"title\": \"DebugBench: Evaluating Debugging Capability of Large Language Models\", \"authors\": \"Runchu Tian and Yining Ye and Yujia Qin and Xin Cong and Yankai Lin and Yinxu Pa...\", \"year\": \"2024\", \"venue\": \"Findings of the Association for Computational Linguistics: ACL 2024\"}, {\"key\": \"abreu2007accuracy\", \"type\": \"article\", \"title\": \"On the Accuracy of Spectrum-based Fault Localization\", \"authors\": \"Rui Abreu and Peter Zoeteweij and Arjan J.C. van Gemund\", \"year\": \"2007\", \"venue\": \"Testing: Academic and Industrial Conference Practice and Research Techniques (MU...\"}, {\"key\": \"jones2002visualization\", \"type\": \"inproceedings\", \"title\": \"Visualization of Test Information to Assist Fault Localization\", \"authors\": \"James A. Jones and Mary Jean Harrold and John Stasko\", \"year\": \"2002\", \"venue\": \"Proceedings of the 24th International Conference on Software Engineering (ICSE)\"}, {\"key\": \"wong2014dstar\", \"type\": \"article\", \"title\": \"DStar: An Effective Spectrum-Based Fault Localization Technique\", \"authors\": \"W. Eric Wong and Vidroha Debroy and Ruizhi Gao and Yihao Li\", \"year\": \"2014\", \"venue\": \"Journal of Systems and Software\"}, {\"key\": \"kang2024autofl\", \"type\": \"inproceedings\", \"title\": \"AutoFL: Automated Fault Localization via Large Language Models\", \"authors\": \"Sungmin Kang and Gabin An and Shin Yoo\", \"year\": \"2024\", \"venue\": \"Proceedings of the 46th IEEE/ACM International Conference on Software Engineerin...\"}, {\"key\": \"qin2024agentfl\", \"type\": \"inproceedings\", \"title\": \"AgentFL: Scaling LLM-based Fault Localization to Project-Level Context\", \"authors\": \"Yihao Qin and Shangwen Wang and Yiling Lou and Jinhao Dong and Kaixin Wang and X...\", \"year\": \"2024\", \"venue\": \"Proceedings of the 39th IEEE/ACM International Conference on Automated Software ...\"}, {\"key\": \"widyasari2024llm4fl\", \"type\": \"inproceedings\", \"title\": \"LLM4FL: An LLM-based Fault Localization Integrated Debugging Framework for Automated Program Repair\", \"authors\": \"Ratnadira Widyasari and Gopi Krishnan Rajbahadur and Shin Hwei Tan and Xin Xia a...\", \"year\": \"2025\", \"venue\": \"Proceedings of the 47th IEEE/ACM International Conference on Software Engineerin...\"}, {\"key\": \"mukherjee2025llmfl\", \"type\": \"inproceedings\", \"title\": \"Can Large Language Models Localize Faults like Developers? A Comprehensive Study\", \"authors\": \"Soneya Binta Hossain and Nan Jiang and Qiang Zhou and Xiaopeng Li and Wen-Hao Ch...\", \"year\": \"2025\", \"venue\": \"Proceedings of the 47th IEEE/ACM International Conference on Software Engineerin...\"}, {\"key\": \"roziere2024code\", \"type\": \"article\", \"title\": \"Code Llama: Open Foundation Models for Code\", \"authors\": \"Baptiste Rozi\\\\`ere and Jonas Gehring and Fabian Gloeckle and Sten Sootla and Ita...\", \"year\": \"2024\", \"venue\": \"arXiv preprint arXiv:2308.12950\"}, {\"key\": \"dinella2022toga\", \"type\": \"inproceedings\", \"title\": \"TOGA: A Neural Method for Test Oracle Generation\", \"authors\": \"Elizabeth Dinella and Gabriel Ryan and Todd Mytkowicz and Shuvendu K. Lahiri\", \"year\": \"2022\", \"venue\": \"Proceedings of the 44th IEEE/ACM International Conference on Software Engineerin...\"}, {\"key\": \"steenhoek2024deepdfa\", \"type\": \"inproceedings\", \"title\": \"Dataflow Analysis-Inspired Deep Learning for Efficient Vulnerability Detection\", \"authors\": \"Benjamin Steenhoek and Hongyang Gao and Wei Le\", \"year\": \"2024\", \"venue\": \"Proceedings of the 46th IEEE/ACM International Conference on Software Engineerin...\"}, {\"key\": \"jimenez2024swebench\", \"type\": \"inproceedings\", \"title\": \"SWE-bench: Can Language Models Resolve Real-World GitHub Issues?\", \"authors\": \"Carlos E. Jimenez and John Yang and Alexander Wettig and Shunyu Yao and Kexin Pe...\", \"year\": \"2024\", \"venue\": \"Proceedings of the 12th International Conference on Learning Representations (IC...\"}, {\"key\": \"kadavath2022language\", \"type\": \"article\", \"title\": \"Language Models (Mostly) Know What They Know\", \"authors\": \"Saurav Kadavath and Tom Conerly and Amanda Askell and Tom Henighan and Dawn Drai...\", \"year\": \"2022\", \"venue\": \"arXiv preprint arXiv:2207.05221\"}, {\"key\": \"kamei2013large\", \"type\": \"article\", \"title\": \"A Large-Scale Empirical Study of Just-in-Time Quality Assurance\", \"authors\": \"Yasutaka Kamei and Emad Shihab and Bram Adams and Ahmed E. Hassan and Audris Moc...\", \"year\": \"2013\", \"venue\": \"IEEE Transactions on Software Engineering\"}, {\"key\": \"bouzenia2025repairagent\", \"type\": \"inproceedings\", \"title\": \"RepairAgent: An Autonomous, LLM-Based Agent for Program Repair\", \"authors\": \"Islem Bouzenia and Premkumar Devanbu and Michael Pradel\", \"year\": \"2025\", \"venue\": \"Proceedings of the 47th IEEE/ACM International Conference on Software Engineerin...\"}, {\"key\": \"chen2024selfdebug\", \"type\": \"inproceedings\", \"title\": \"Teaching Large Language Models to Self-Debug\", \"authors\": \"Xinyun Chen and Maxwell Lin and Nathanael Sch\\\\\\\"arli and Denny Zhou\", \"year\": \"2024\", \"venue\": \"Proceedings of the 12th International Conference on Learning Representations (IC...\"}, {\"key\": \"liu2023codeexecution\", \"type\": \"inproceedings\", \"title\": \"Code Execution with Pre-trained Language Models\", \"authors\": \"Chenxiao Liu and Shuai Lu and Weizhu Chen and Daxin Jiang and Alexey Svyatkovski...\", \"year\": \"2023\", \"venue\": \"Findings of the Association for Computational Linguistics: ACL 2023\"}, {\"key\": \"tian2020patchcorrectness\", \"type\": \"inproceedings\", \"title\": \"Evaluating Representation Learning of Code Changes for Predicting Patch Correctness in Program Repair\", \"authors\": \"Haoye Tian and Kui Liu and Abdoul Kader Kabor\\\\'e and Anil Koyuncu and Li Li and ...\", \"year\": \"2020\", \"venue\": \"Proceedings of the 35th IEEE/ACM International Conference on Automated Software ...\"}, {\"key\": \"watson2020atlas\", \"type\": \"inproceedings\", \"title\": \"On Learning Meaningful Assert Statements for Unit Test Cases\", \"authors\": \"Cody Watson and Michele Tufano and Kevin Moran and Gabriele Bavota and Denys Pos...\", \"year\": \"2020\", \"venue\": \"Proceedings of the ACM/IEEE 42nd International Conference on Software Engineerin...\"}, {\"key\": \"yu2022assertion\", \"type\": \"inproceedings\", \"title\": \"Automated Assertion Generation via Information Retrieval and Its Integration with Deep Learning\", \"authors\": \"Hao Yu and Yiling Lou and Ke Sun and Dezhi Ran and Tao Xie and Dan Hao and Ying ...\", \"year\": \"2022\", \"venue\": \"Proceedings of the 44th IEEE/ACM International Conference on Software Engineerin...\"}, {\"key\": \"nashid2023assertion\", \"type\": \"inproceedings\", \"title\": \"Revisiting and Improving Retrieval-Augmented Deep Assertion Generation\", \"authors\": \"Noor Nashid and Taha Shabani and Ali Mesbah\", \"year\": \"2023\", \"venue\": \"Proceedings of the 38th IEEE/ACM International Conference on Automated Software ...\"}, {\"key\": \"yadavally2024slicing\", \"type\": \"inproceedings\", \"title\": \"A Learning-Based Approach to Static Program Slicing\", \"authors\": \"Aashish Yadavally and Yi Li and Shaohua Wang and Tien N. Nguyen\", \"year\": \"2024\", \"venue\": \"Proceedings of the ACM on Programming Languages (OOPSLA)\"}, {\"key\": \"xia2024agentless\", \"type\": \"article\", \"title\": \"Agentless: Demystifying LLM-based Software Engineering Agents\", \"authors\": \"Chunqiu Steven Xia and Yinlin Deng and Soren Dunn and Lingming Zhang\", \"year\": \"2024\", \"venue\": \"arXiv preprint arXiv:2407.01489\"}, {\"key\": \"guo2017calibration\", \"type\": \"inproceedings\", \"title\": \"On Calibration of Modern Neural Networks\", \"authors\": \"Chuan Guo and Geoff Pleiss and Yu Sun and Kilian Q. Weinberger\", \"year\": \"2017\", \"venue\": \"Proceedings of the 34th International Conference on Machine Learning (ICML)\"}, {\"key\": \"geng2024calibration\", \"type\": \"inproceedings\", \"title\": \"A Survey of Confidence Estimation and Calibration in Large Language Models\", \"authors\": \"Jiahui Geng and Fengyu Cai and Yuxia Wang and Heinz Koeppl and Preslav Nakov and...\", \"year\": \"2024\", \"venue\": \"Proceedings of the 2024 Conference of the North American Chapter of the Associat...\"}, {\"key\": \"hoang2019deepjit\", \"type\": \"inproceedings\", \"title\": \"DeepJIT: An End-to-End Deep Learning Framework for Just-in-Time Defect Prediction\", \"authors\": \"Thong Hoang and Hoa Khanh Dam and Yasutaka Kamei and David Lo and Naoyasu Ubayas...\", \"year\": \"2019\", \"venue\": \"Proceedings of the 16th International Conference on Mining Software Repositories...\"}, {\"key\": \"hoang2020cc2vec\", \"type\": \"inproceedings\", \"title\": \"CC2Vec: Distributed Representations of Code Changes\", \"authors\": \"Thong Hoang and Hong Jin Kang and Julia Lawall and David Lo\", \"year\": \"2020\", \"venue\": \"Proceedings of the ACM/IEEE 42nd International Conference on Software Engineerin...\"}, {\"key\": \"pornprasit2021jitline\", \"type\": \"inproceedings\", \"title\": \"JITLine: A Simpler, Better, Faster, Finer-grained Just-In-Time Defect Prediction\", \"authors\": \"Chanathip Pornprasit and Chakkrit Tantithamthavorn\", \"year\": \"2021\", \"venue\": \"Proceedings of the 18th International Conference on Mining Software Repositories...\"}, {\"key\": \"bengio2009curriculum\", \"type\": \"inproceedings\", \"title\": \"Curriculum Learning\", \"authors\": \"Yoshua Bengio and J\\\\'er\\\\^ome Louradour and Ronan Collobert and Jason Weston\", \"year\": \"2009\", \"venue\": \"Proceedings of the 26th Annual International Conference on Machine Learning (ICM...\"}, {\"key\": \"sachdeva2024dataefficient\", \"type\": \"article\", \"title\": \"How to Train Data-Efficient LLMs\", \"authors\": \"Noveen Sachdeva and Benjamin Coleman and Wang-Cheng Kang and Jianmo Ni and Licha...\", \"year\": \"2024\", \"venue\": \"arXiv preprint arXiv:2402.09668\"}, {\"key\": \"swayamdipta2020cartography\", \"type\": \"inproceedings\", \"title\": \"Dataset Cartography: Mapping and Diagnosing Datasets with Training Dynamics\", \"authors\": \"Swabha Swayamdipta and Roy Schwartz and Nicholas Lourie and Yizhong Wang and Han...\", \"year\": \"2020\", \"venue\": \"Proceedings of the 2020 Conference on Empirical Methods in Natural Language Proc...\"}, {\"key\": \"xie2023doremi\", \"type\": \"inproceedings\", \"title\": \"DoReMi: Optimizing Data Mixtures Speeds Up Language Model Pretraining\", \"authors\": \"Sang Michael Xie and Hieu Pham and Xuanyi Dong and Nan Du and Hanxiao Liu and Yi...\", \"year\": \"2023\", \"venue\": \"Advances in Neural Information Processing Systems (NeurIPS)\"}], \"tex_citations\": [{\"key\": \"chen2025tracepile\", \"file\": \"introduction.tex\", \"line\": 3, \"command\": \"citep\"}, {\"key\": \"ding2024traced\", \"file\": \"introduction.tex\", \"line\": 3, \"command\": \"citep\"}, {\"key\": \"wang2025dcsh\", \"file\": \"introduction.tex\", \"line\": 3, \"command\": \"citep\"}, {\"key\": \"ni2024next\", \"file\": \"introduction.tex\", \"line\": 3, \"command\": \"citep\"}, {\"key\": \"wang2025dcsh\", \"file\": \"introduction.tex\", \"line\": 7, \"command\": \"citep\"}, {\"key\": \"chen2021evaluating\", \"file\": \"introduction.tex\", \"line\": 13, \"command\": \"citep\"}, {\"key\": \"austin2021program\", \"file\": \"introduction.tex\", \"line\": 13, \"command\": \"citep\"}, {\"key\": \"qwen2025coder\", \"file\": \"introduction.tex\", \"line\": 13, \"command\": \"citep\"}, {\"key\": \"roziere2024code\", \"file\": \"introduction.tex\", \"line\": 13, \"command\": \"citep\"}, {\"key\": \"deepseek2024coder\", \"file\": \"introduction.tex\", \"line\": 13, \"command\": \"citep\"}, {\"key\": \"chen2025tracepile\", \"file\": \"method.tex\", \"line\": 7, \"command\": \"citep\"}, {\"key\": \"gu2024cruxeval\", \"file\": \"method.tex\", \"line\": 7, \"command\": \"citep\"}, {\"key\": \"chen2021evaluating\", \"file\": \"method.tex\", \"line\": 12, \"command\": \"citep\"}, {\"key\": \"austin2021program\", \"file\": \"method.tex\", \"line\": 12, \"command\": \"citep\"}, {\"key\": \"qwen2025coder\", \"file\": \"method.tex\", \"line\": 38, \"command\": \"citep\"}, {\"key\": \"roziere2024code\", \"file\": \"method.tex\", \"line\": 38, \"command\": \"citep\"}, {\"key\": \"deepseek2024coder\", \"file\": \"method.tex\", \"line\": 38, \"command\": \"citep\"}, {\"key\": \"hu2022lora\", \"file\": \"method.tex\", \"line\": 39, \"command\": \"citep\"}, {\"key\": \"tian2024debugbench\", \"file\": \"experiments.tex\", \"line\": 173, \"command\": \"citep\"}, {\"key\": \"chen2025tracepile\", \"file\": \"related_work.tex\", \"line\": 4, \"command\": \"citep\"}, {\"key\": \"wang2025dcsh\", \"file\": \"related_work.tex\", \"line\": 4, \"command\": \"citet\"}, {\"key\": \"ni2024next\", \"file\": \"related_work.tex\", \"line\": 5, \"command\": \"citep\"}, {\"key\": \"eguchi2025etcot\", \"file\": \"related_work.tex\", \"line\": 5, \"command\": \"citep\"}, {\"key\": \"ferrando2025execute\", \"file\": \"related_work.tex\", \"line\": 5, \"command\": \"citet\"}, {\"key\": \"liu2023codeexecution\", \"file\": \"related_work.tex\", \"line\": 6, \"command\": \"citet\"}, {\"key\": \"chen2024selfdebug\", \"file\": \"related_work.tex\", \"line\": 6, \"command\": \"citet\"}, {\"key\": \"gu2024cruxeval\", \"file\": \"related_work.tex\", \"line\": 7, \"command\": \"citep\"}, {\"key\": \"xu2025cruxevalx\", \"file\": \"related_work.tex\", \"line\": 7, \"command\": \"citep\"}, {\"key\": \"ding2024traced\", \"file\": \"related_work.tex\", \"line\": 11, \"command\": \"citep\"}, {\"key\": \"steenhoek2024deepdfa\", \"file\": \"related_work.tex\", \"line\": 11, \"command\": \"citep\"}, {\"key\": \"yadavally2024slicing\", \"file\": \"related_work.tex\", \"line\": 11, \"command\": \"citep\"}, {\"key\": \"tian2020patchcorrectness\", \"file\": \"related_work.tex\", \"line\": 12, \"command\": \"citet\"}, {\"key\": \"hoang2020cc2vec\", \"file\": \"related_work.tex\", \"line\": 12, \"command\": \"citep\"}, {\"key\": \"zhou2024llm4patch\", \"file\": \"related_work.tex\", \"line\": 12, \"command\": \"citep\"}, {\"key\": \"appt2024\", \"file\": \"related_work.tex\", \"line\": 12, \"command\": \"citep\"}, {\"key\": \"watson2020atlas\", \"file\": \"related_work.tex\", \"line\": 13, \"command\": \"citep\"}, {\"key\": \"yu2022assertion\", \"file\": \"related_work.tex\", \"line\": 13, \"command\": \"citep\"}, {\"key\": \"nashid2023assertion\", \"file\": \"related_work.tex\", \"line\": 13, \"command\": \"citep\"}, {\"key\": \"dinella2022toga\", \"file\": \"related_work.tex\", \"line\": 13, \"command\": \"citep\"}, {\"key\": \"widyasari2024fusefl\", \"file\": \"related_work.tex\", \"line\": 13, \"command\": \"citep\"}, {\"key\": \"foster2025mutation\", \"file\": \"related_work.tex\", \"line\": 13, \"command\": \"citet\"}, {\"key\": \"abreu2007accuracy\", \"file\": \"related_work.tex\", \"line\": 17, \"command\": \"citep\"}, {\"key\": \"jones2002visualization\", \"file\": \"related_work.tex\", \"line\": 17, \"command\": \"citep\"}, {\"key\": \"wong2014dstar\", \"file\": \"related_work.tex\", \"line\": 17, \"command\": \"citep\"}, {\"key\": \"kang2024autofl\", \"file\": \"related_work.tex\", \"line\": 17, \"command\": \"citep\"}, {\"key\": \"qin2024agentfl\", \"file\": \"related_work.tex\", \"line\": 17, \"command\": \"citep\"}, {\"key\": \"widyasari2024llm4fl\", \"file\": \"related_work.tex\", \"line\": 17, \"command\": \"citep\"}, {\"key\": \"mukherjee2025llmfl\", \"file\": \"related_work.tex\", \"line\": 17, \"command\": \"citep\"}, {\"key\": \"huang2026tracecoder\", \"file\": \"related_work.tex\", \"line\": 21, \"command\": \"citep\"}, {\"key\": \"wang2025inspectcoder\", \"file\": \"related_work.tex\", \"line\": 21, \"command\": \"citep\"}, {\"key\": \"bouzenia2025repairagent\", \"file\": \"related_work.tex\", \"line\": 21, \"command\": \"citep\"}, {\"key\": \"xia2024agentless\", \"file\": \"related_work.tex\", \"line\": 21, \"command\": \"citep\"}, {\"key\": \"haque2025traces\", \"file\": \"related_work.tex\", \"line\": 22, \"command\": \"citet\"}, {\"key\": \"jimenez2024swebench\", \"file\": \"related_work.tex\", \"line\": 22, \"command\": \"citep\"}, {\"key\": \"guo2017calibration\", \"file\": \"related_work.tex\", \"line\": 26, \"command\": \"citep\"}, {\"key\": \"kadavath2022language\", \"file\": \"related_work.tex\", \"line\": 26, \"command\": \"citep\"}, {\"key\": \"geng2024calibration\", \"file\": \"related_work.tex\", \"line\": 26, \"command\": \"citep\"}, {\"key\": \"spiess2025calibration\", \"file\": \"related_work.tex\", \"line\": 26, \"command\": \"citep\"}, {\"key\": \"kamei2013large\", \"file\": \"related_work.tex\", \"line\": 27, \"command\": \"citep\"}, {\"key\": \"hoang2019deepjit\", \"file\": \"related_work.tex\", \"line\": 27, \"command\": \"citep\"}, {\"key\": \"pornprasit2021jitline\", \"file\": \"related_work.tex\", \"line\": 27, \"command\": \"citep\"}, {\"key\": \"bengio2009curriculum\", \"file\": \"related_work.tex\", \"line\": 30, \"command\": \"citep\"}, {\"key\": \"swayamdipta2020cartography\", \"file\": \"related_work.tex\", \"line\": 30, \"command\": \"citep\"}, {\"key\": \"sachdeva2024dataefficient\", \"file\": \"related_work.tex\", \"line\": 30, \"command\": \"citep\"}, {\"key\": \"xie2023doremi\", \"file\": \"related_work.tex\", \"line\": 30, \"command\": \"citep\"}, {\"key\": \"hu2022lora\", \"file\": \"appendix.tex\", \"line\": 37, \"command\": \"citep\"}, {\"key\": \"spiess2025calibration\", \"file\": \"appendix.tex\", \"line\": 509, \"command\": \"citep\"}, {\"key\": \"tian2024debugbench\", \"file\": \"appendix.tex\", \"line\": 588, \"command\": \"citep\"}, {\"key\": \"yang2024generalization\", \"file\": \"appendix.tex\", \"line\": 626, \"command\": \"citep\"}], \"online_verification\": [{\"key\": \"chen2025tracepile\", \"title\": \"Chain of Execution Supervision Promotes General Reasoning in Large Language Models\", \"status\": \"not_found\", \"confidence\": 0.452, \"matched_title\": \"A Survey of Large Language Models\", \"matched_year\": \"\", \"mismatch_fields\": [], \"note\": \"best match similarity 0.45 below threshold 0.82\"}, {\"key\": \"ding2024traced\", \"title\": \"TRACED: Execution-aware Pre-training for Source Code\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"TRACED: Execution-aware Pre-training for Source Code\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"chen2021evaluating\", \"title\": \"Evaluating Large Language Models Trained on Code\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Evaluating Large Language Models Trained on Code\", \"matched_year\": \"2021\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"austin2021program\", \"title\": \"Program Synthesis with Large Language Models\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Program Synthesis with Large Language Models\", \"matched_year\": \"2021\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"gu2024cruxeval\", \"title\": \"CRUXEval: A Benchmark for Code Reasoning, Understanding and Execution\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"CRUXEval: A Benchmark for Code Reasoning, Understanding and Execution\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"hu2022lora\", \"title\": \"LoRA: Low-Rank Adaptation of Large Language Models\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"LoRA: Low-Rank Adaptation of Large Language Models\", \"matched_year\": \"2021\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"qwen2025coder\", \"title\": \"Qwen2.5-Coder Technical Report\", \"status\": \"mismatch\", \"confidence\": 1.0, \"matched_title\": \"Qwen2.5-Coder Technical Report\", \"matched_year\": \"2024\", \"mismatch_fields\": [\"first_author: bib=team vs api=hui\"], \"note\": \"\"}, {\"key\": \"deepseek2024coder\", \"title\": \"DeepSeek-Coder: When the Large Language Model Meets Programming -- The Rise of Code Intelligence\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"DeepSeek-Coder: When the Large Language Model Meets Programming -- The Rise of Code Intelligence\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"wang2025dcsh\", \"title\": \"Do Code Semantics Help? A Comprehensive Study on Execution Trace-Based Information for Code Large Language Models\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Do Code Semantics Help? A Comprehensive Study on Execution Trace-Based Information for Code Large Language Models\", \"matched_year\": \"2025\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"ni2024next\", \"title\": \"NExT: Teaching Large Language Models to Reason about Code Execution\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"NExT: Teaching Large Language Models to Reason about Code Execution\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"eguchi2025etcot\", \"title\": \"Making LLMs Program Interpreters via Execution Trace Chain of Thought\", \"status\": \"not_found\", \"confidence\": 0.203, \"matched_title\": \"From ChatGPT to ThreatGPT: Impact of Generative AI in Cybersecurity and Privacy\", \"matched_year\": \"\", \"mismatch_fields\": [], \"note\": \"best match similarity 0.20 below threshold 0.82\"}, {\"key\": \"ferrando2025execute\", \"title\": \"What I Cannot Execute, I Do Not Understand: Training and Evaluating LLMs on Program Execution Traces\", \"status\": \"not_found\", \"confidence\": 0.199, \"matched_title\": \"Sparks of Artificial General Intelligence: Early experiments with GPT-4\", \"matched_year\": \"\", \"mismatch_fields\": [], \"note\": \"best match similarity 0.20 below threshold 0.82\"}, {\"key\": \"xu2025cruxevalx\", \"title\": \"CRUXEval-X: A Benchmark for Multilingual Code Reasoning, Understanding and Execution\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"CRUXEVAL-X: A Benchmark for Multilingual Code Reasoning, Understanding and Execution\", \"matched_year\": \"2025\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"appt2024\", \"title\": \"APPT: Boosting Automated Patch Correctness Prediction via Fine-tuning Pre-trained Models\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"APPT: Boosting Automated Patch Correctness Prediction via Fine-Tuning Pre-Trained Models\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"zhou2024llm4patch\", \"title\": \"Leveraging Large Language Model for Automatic Patch Correctness Assessment\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Leveraging Large Language Model for Automatic Patch Correctness Assessment\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"spiess2025calibration\", \"title\": \"Calibration and Correctness of Language Models for Code\", \"status\": \"mismatch\", \"confidence\": 1.0, \"matched_title\": \"Calibration and Correctness of Language Models for Code\", \"matched_year\": \"2025\", \"mismatch_fields\": [\"first_author: bib=spiess vs api=spieß\"], \"note\": \"\"}, {\"key\": \"foster2025mutation\", \"title\": \"Mutation-Guided LLM-based Test Generation at Meta\", \"status\": \"mismatch\", \"confidence\": 1.0, \"matched_title\": \"Mutation-Guided LLM-based Test Generation at Meta\", \"matched_year\": \"2025\", \"mismatch_fields\": [\"first_author: bib=foster vs api=harman\"], \"note\": \"\"}, {\"key\": \"widyasari2024fusefl\", \"title\": \"Demystifying Faulty Code: Step-by-Step Reasoning for Explainable Fault Localization\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Demystifying Faulty Code: Step-by-Step Reasoning for Explainable Fault Localization\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"huang2026tracecoder\", \"title\": \"TraceCoder: A Trace-Driven Multi-Agent Framework for Automated Debugging of LLM-Generated Code\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"TraceCoder: A Trace-Driven Multi-Agent Framework for Automated Debugging of LLM-Generated Code\", \"matched_year\": \"2026\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"wang2025inspectcoder\", \"title\": \"InspectCoder: Dynamic Analysis-Enabled Self Repair through Interactive LLM-Debugger Collaboration\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"InspectCoder: Dynamic Analysis-Enabled Self Repair through interactive LLM-Debugger Collaboration\", \"matched_year\": \"2025\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"haque2025traces\", \"title\": \"Towards Effectively Leveraging Execution Traces for Program Repair with Code LLMs\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Towards Effectively Leveraging Execution Traces for Program Repair with Code LLMs\", \"matched_year\": \"2025\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"yang2024generalization\", \"title\": \"Unveiling the Generalization Power of Fine-Tuned Large Language Models\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Unveiling the Generalization Power of Fine-Tuned Large Language Models\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"tian2024debugbench\", \"title\": \"DebugBench: Evaluating Debugging Capability of Large Language Models\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"DebugBench: Evaluating Debugging Capability of Large Language Models\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"abreu2007accuracy\", \"title\": \"On the Accuracy of Spectrum-based Fault Localization\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"On the Accuracy of Spectrum-based Fault Localization\", \"matched_year\": \"2007\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"jones2002visualization\", \"title\": \"Visualization of Test Information to Assist Fault Localization\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Visualization of test information to assist fault localization\", \"matched_year\": \"2002\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"wong2014dstar\", \"title\": \"DStar: An Effective Spectrum-Based Fault Localization Technique\", \"status\": \"not_found\", \"confidence\": 0.561, \"matched_title\": \"MSFL: A Model for Fault Localization Using Mutation-Spectra Technique\", \"matched_year\": \"\", \"mismatch_fields\": [], \"note\": \"best match similarity 0.56 below threshold 0.82\"}, {\"key\": \"kang2024autofl\", \"title\": \"AutoFL: Automated Fault Localization via Large Language Models\", \"status\": \"not_found\", \"confidence\": 0.45, \"matched_title\": \"A Survey on Large Language Models for Software Engineering\", \"matched_year\": \"\", \"mismatch_fields\": [], \"note\": \"best match similarity 0.45 below threshold 0.82\"}, {\"key\": \"qin2024agentfl\", \"title\": \"AgentFL: Scaling LLM-based Fault Localization to Project-Level Context\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"AgentFL: Scaling LLM-based Fault Localization to Project-Level Context\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"widyasari2024llm4fl\", \"title\": \"LLM4FL: An LLM-based Fault Localization Integrated Debugging Framework for Automated Program Repair\", \"status\": \"not_found\", \"confidence\": 0.448, \"matched_title\": \"A Multi-Agent Approach to Fault Localization via Graph-Based Retrieval and Reflexion\", \"matched_year\": \"\", \"mismatch_fields\": [], \"note\": \"best match similarity 0.45 below threshold 0.82\"}, {\"key\": \"mukherjee2025llmfl\", \"title\": \"Can Large Language Models Localize Faults like Developers? A Comprehensive Study\", \"status\": \"not_found\", \"confidence\": 0.186, \"matched_title\": \"Internet of Things (IoT): A vision, architectural elements, and future directions\", \"matched_year\": \"\", \"mismatch_fields\": [], \"note\": \"best match similarity 0.19 below threshold 0.82\"}, {\"key\": \"roziere2024code\", \"title\": \"Code Llama: Open Foundation Models for Code\", \"status\": \"mismatch\", \"confidence\": 1.0, \"matched_title\": \"Code Llama: Open Foundation Models for Code\", \"matched_year\": \"2023\", \"mismatch_fields\": [\"first_author: bib=rozi\\\\`ere vs api=rozière\"], \"note\": \"\"}, {\"key\": \"dinella2022toga\", \"title\": \"TOGA: A Neural Method for Test Oracle Generation\", \"status\": \"not_found\", \"confidence\": 0.623, \"matched_title\": \"TOGLL: Correct and Strong Test Oracle Generation with LLMs\", \"matched_year\": \"\", \"mismatch_fields\": [], \"note\": \"best match similarity 0.62 below threshold 0.82\"}, {\"key\": \"steenhoek2024deepdfa\", \"title\": \"Dataflow Analysis-Inspired Deep Learning for Efficient Vulnerability Detection\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Dataflow Analysis-Inspired Deep Learning for Efficient Vulnerability Detection\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"jimenez2024swebench\", \"title\": \"SWE-bench: Can Language Models Resolve Real-World GitHub Issues?\", \"status\": \"mismatch\", \"confidence\": 1.0, \"matched_title\": \"SWE-bench: Can Language Models Resolve Real-World GitHub Issues?\", \"matched_year\": \"2023\", \"mismatch_fields\": [\"first_author: bib=jimenez vs api=jimenez-gomez\"], \"note\": \"\"}, {\"key\": \"kadavath2022language\", \"title\": \"Language Models (Mostly) Know What They Know\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Language Models (Mostly) Know What They Know\", \"matched_year\": \"2022\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"kamei2013large\", \"title\": \"A Large-Scale Empirical Study of Just-in-Time Quality Assurance\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"A large-scale empirical study of just-in-time quality assurance\", \"matched_year\": \"2012\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"bouzenia2025repairagent\", \"title\": \"RepairAgent: An Autonomous, LLM-Based Agent for Program Repair\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"RepairAgent: An Autonomous, LLM-Based Agent for Program Repair\", \"matched_year\": \"2025\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"chen2024selfdebug\", \"title\": \"Teaching Large Language Models to Self-Debug\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Teaching Large Language Models to Self-Debug\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"liu2023codeexecution\", \"title\": \"Code Execution with Pre-trained Language Models\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Code Execution with Pre-trained Language Models\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"tian2020patchcorrectness\", \"title\": \"Evaluating Representation Learning of Code Changes for Predicting Patch Correctness in Program Repair\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Evaluating representation learning of code changes for predicting patch correctness in program repair\", \"matched_year\": \"2020\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"watson2020atlas\", \"title\": \"On Learning Meaningful Assert Statements for Unit Test Cases\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"On learning meaningful assert statements for unit test cases\", \"matched_year\": \"2020\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"yu2022assertion\", \"title\": \"Automated Assertion Generation via Information Retrieval and Its Integration with Deep Learning\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Automated assertion generation via information retrieval and its integration with deep learning\", \"matched_year\": \"2022\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"nashid2023assertion\", \"title\": \"Revisiting and Improving Retrieval-Augmented Deep Assertion Generation\", \"status\": \"mismatch\", \"confidence\": 1.0, \"matched_title\": \"Revisiting and Improving Retrieval-Augmented Deep Assertion Generation\", \"matched_year\": \"2023\", \"mismatch_fields\": [\"first_author: bib=nashid vs api=sun\"], \"note\": \"\"}, {\"key\": \"yadavally2024slicing\", \"title\": \"A Learning-Based Approach to Static Program Slicing\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"A Learning-Based Approach to Static Program Slicing\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"xia2024agentless\", \"title\": \"Agentless: Demystifying LLM-based Software Engineering Agents\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Agentless: Demystifying LLM-based Software Engineering Agents\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"guo2017calibration\", \"title\": \"On Calibration of Modern Neural Networks\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"On Calibration of Modern Neural Networks\", \"matched_year\": \"2017\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"geng2024calibration\", \"title\": \"A Survey of Confidence Estimation and Calibration in Large Language Models\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"A Survey of Confidence Estimation and Calibration in Large Language Models\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"hoang2019deepjit\", \"title\": \"DeepJIT: An End-to-End Deep Learning Framework for Just-in-Time Defect Prediction\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"DeepJIT: An End-to-End Deep Learning Framework for Just-in-Time Defect Prediction\", \"matched_year\": \"2019\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"hoang2020cc2vec\", \"title\": \"CC2Vec: Distributed Representations of Code Changes\", \"status\": \"mismatch\", \"confidence\": 1.0, \"matched_title\": \"CC2Vec: Distributed Representations of Code Changes\", \"matched_year\": \"2020\", \"mismatch_fields\": [\"first_author: bib=hoang vs api=thong\"], \"note\": \"\"}, {\"key\": \"pornprasit2021jitline\", \"title\": \"JITLine: A Simpler, Better, Faster, Finer-grained Just-In-Time Defect Prediction\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"JITLine: A Simpler, Better, Faster, Finer-grained Just-In-Time Defect Prediction\", \"matched_year\": \"2021\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"bengio2009curriculum\", \"title\": \"Curriculum Learning\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Curriculum learning\", \"matched_year\": \"2009\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"sachdeva2024dataefficient\", \"title\": \"How to Train Data-Efficient LLMs\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"How to Train Data-Efficient LLMs\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"swayamdipta2020cartography\", \"title\": \"Dataset Cartography: Mapping and Diagnosing Datasets with Training Dynamics\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Dataset Cartography: Mapping and Diagnosing Datasets with Training Dynamics\", \"matched_year\": \"2020\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"xie2023doremi\", \"title\": \"DoReMi: Optimizing Data Mixtures Speeds Up Language Model Pretraining\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"DoReMi: Optimizing Data Mixtures Speeds Up Language Model Pretraining\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}]}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "311b3d5f-5139-4484-9357-54b46b4571d0",
  "isSidechain": false,
  "promptId": "e3f72197-8c21-47a9-99b8-7cd49faae750",
  "type": "user",
  "uuid": "f0aed6cc-45eb-4dbf-b76a-bad399939f47",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"summary\\\": {\\\"total_bib_entries\\\": 54, \\\"total_citations\\\": 69, \\\"unique_cited_keys\\\": 54, \\\"orphan_bib\\\": 0, \\\"missing_bib\\\": 0, \\\"duplicate_keys\\\": 0, \\\"online_verified\\\": 39, \\\"online_not_found\\\": 8, \\\"online_mismatch\\\": 7}, \\\"cross_check\\\": {\\\"orphan_bib\\\": [], \\\"missing_bib\\\": [], \\\"orphan_count\\\": 0, \\\"missing_count\\\": 0}, \\\"bib_entries\\\": [{\\\"key\\\": \\\"chen2025tracepile\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Chain of Execution Supervision Promotes General Reasoning in Large Language Models\\\", \\\"authors\\\": \\\"Nuo Chen and Zehua Li and Keqin Bao and Junyang Lin and Dayiheng Liu\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"Advances in Neural Information Processing Systems (NeurIPS)\\\"}, {\\\"key\\\": \\\"ding2024traced\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"TRACED: Execution-aware Pre-training for Source Code\\\", \\\"authors\\\": \\\"Yangruibo Ding and Ben Steenhoek and Kexin Pei and Gail Kaiser and Wei Le and Ba...\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"Proceedings of the 46th IEEE/ACM International Conference on Software Engineerin...\\\"}, {\\\"key\\\": \\\"chen2021evaluating\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Evaluating Large Language Models Trained on Code\\\", \\\"authors\\\": \\\"Chen, Mark and Tworek, Jerry and Jun, Heewoo and Yuan, Qiming and Pinto, Henriqu...\\\", \\\"year\\\": \\\"2021\\\", \\\"venue\\\": \\\"arXiv preprint arXiv:2107.03374\\\"}, {\\\"key\\\": \\\"austin2021program\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Program Synthesis with Large Language Models\\\", \\\"authors\\\": \\\"Austin, Jacob and Odena, Augustus and Nye, Maxwell and Bosma, Maarten and Michal...\\\", \\\"year\\\": \\\"2021\\\", \\\"venue\\\": \\\"arXiv preprint arXiv:2108.07732\\\"}, {\\\"key\\\": \\\"gu2024cruxeval\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"CRUXEval: A Benchmark for Code Reasoning, Understanding and Execution\\\", \\\"authors\\\": \\\"Alex Gu and Baptiste Rozi\\\\\\\\`ere and Hugh Leather and Armando Solar-Lezama and Gab...\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"Proceedings of the 41st International Conference on Machine Learning (ICML)\\\"}, {\\\"key\\\": \\\"hu2022lora\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"LoRA: Low-Rank Adaptation of Large Language Models\\\", \\\"authors\\\": \\\"Edward J. Hu and Yelong Shen and Phillip Wallis and Zeyuan Allen-Zhu and Yuanzhi...\\\", \\\"year\\\": \\\"2022\\\", \\\"venue\\\": \\\"Proceedings of the 10th International Conference on Learning Representations (IC...\\\"}, {\\\"key\\\": \\\"qwen2025coder\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Qwen2.5-Coder Technical Report\\\", \\\"authors\\\": \\\"Qwen Team\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"arXiv preprint arXiv:2409.12186\\\"}, {\\\"key\\\": \\\"deepseek2024coder\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"DeepSeek-Coder: When the Large Language Model Meets Programming -- The Rise of Code Intelligence\\\", \\\"authors\\\": \\\"Daya Guo and Qihao Zhu and Dejian Yang and Zhenda Xie and Kai Dong and Wentao Zh...\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"arXiv preprint arXiv:2401.14196\\\"}, {\\\"key\\\": \\\"wang2025dcsh\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Do Code Semantics Help? A Comprehensive Study on Execution Trace-Based Information for Code Large Language Models\\\", \\\"authors\\\": \\\"Jian Wang and Xiaofei Xie and Qiang Hu and Shangqing Liu and Yi Li\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"Findings of the Association for Computational Linguistics: EMNLP 2025\\\"}, {\\\"key\\\": \\\"ni2024next\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"NExT: Teaching Large Language Models to Reason about Code Execution\\\", \\\"authors\\\": \\\"Ansong Ni and Miltiadis Allamanis and Arman Cohan and Yinlin Deng and Kensen Shi...\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"Proceedings of the 41st International Conference on Machine Learning (ICML)\\\"}, {\\\"key\\\": \\\"eguchi2025etcot\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Making LLMs Program Interpreters via Execution Trace Chain of Thought\\\", \\\"authors\\\": \\\"Koshi Eguchi and Takuya Akiba\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"ICML 2025 Workshop on Programmatic Representations for Agent Learning (PRAL)\\\"}, {\\\"key\\\": \\\"ferrando2025execute\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"What I Cannot Execute, I Do Not Understand: Training and Evaluating LLMs on Program Execution Traces\\\", \\\"authors\\\": \\\"Jordi Armengol-Estape and Quentin Carbonneaux and Tianjun Zhang and Aram H. Mark...\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"arXiv preprint arXiv:2503.05703\\\"}, {\\\"key\\\": \\\"xu2025cruxevalx\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"CRUXEval-X: A Benchmark for Multilingual Code Reasoning, Understanding and Execution\\\", \\\"authors\\\": \\\"Ruiyang Xu and others\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"Proceedings of the 63rd Annual Meeting of the Association for Computational Ling...\\\"}, {\\\"key\\\": \\\"appt2024\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"APPT: Boosting Automated Patch Correctness Prediction via Fine-tuning Pre-trained Models\\\", \\\"authors\\\": \\\"Quanjun Zhang and Chunrong Fang and Weisong Sun and Yan Liu and Tieke He and Xia...\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"IEEE Transactions on Software Engineering\\\"}, {\\\"key\\\": \\\"zhou2024llm4patch\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Leveraging Large Language Model for Automatic Patch Correctness Assessment\\\", \\\"authors\\\": \\\"Xin Zhou and Bowen Xu and Kisub Kim and DongGyun Han and Hung Huu Nguyen and Tha...\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"IEEE Transactions on Software Engineering\\\"}, {\\\"key\\\": \\\"spiess2025calibration\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Calibration and Correctness of Language Models for Code\\\", \\\"authors\\\": \\\"Claudio Spiess and David Gros and others\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"Proceedings of the 47th IEEE/ACM International Conference on Software Engineerin...\\\"}, {\\\"key\\\": \\\"foster2025mutation\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Mutation-Guided LLM-based Test Generation at Meta\\\", \\\"authors\\\": \\\"Christopher Foster and Abhishek Gulati and Mark Harman and Inna Harper and Ke Ma...\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"Proceedings of the ACM International Conference on the Foundations of Software E...\\\"}, {\\\"key\\\": \\\"widyasari2024fusefl\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Demystifying Faulty Code: Step-by-Step Reasoning for Explainable Fault Localization\\\", \\\"authors\\\": \\\"Ratnadira Widyasari and Jia Wei Ang and Truong Giang Nguyen and Neil Sharma and ...\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"Proceedings of the IEEE International Conference on Software Analysis, Evolution...\\\"}, {\\\"key\\\": \\\"huang2026tracecoder\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"TraceCoder: A Trace-Driven Multi-Agent Framework for Automated Debugging of LLM-Generated Code\\\", \\\"authors\\\": \\\"Jiangping Huang and Wenguang Ye and Weisong Sun and Jian Zhang and Mingyue Zhang...\\\", \\\"year\\\": \\\"2026\\\", \\\"venue\\\": \\\"Proceedings of the 48th IEEE/ACM International Conference on Software Engineerin...\\\"}, {\\\"key\\\": \\\"wang2025inspectcoder\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"InspectCoder: Dynamic Analysis-Enabled Self Repair through Interactive LLM-Debugger Collaboration\\\", \\\"authors\\\": \\\"Yunkun Wang and Yue Zhang and Guochang Li and Chen Zhi and Binhua Li and Fei Hua...\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"arXiv preprint arXiv:2510.18327\\\"}, {\\\"key\\\": \\\"haque2025traces\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Towards Effectively Leveraging Execution Traces for Program Repair with Code LLMs\\\", \\\"authors\\\": \\\"Mirazul Haque and Petr Babkin and Farima Farmahinifarahani and Manuela Veloso\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"KnowledgeNLP Workshop at ACL 2025\\\"}, {\\\"key\\\": \\\"yang2024generalization\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Unveiling the Generalization Power of Fine-Tuned Large Language Models\\\", \\\"authors\\\": \\\"Haoran Yang and Yumeng Zhang and Jiaqi Xu and Hongyuan Lu and Pheng Ann Heng and...\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"Proceedings of the 2024 Conference of the North American Chapter of the Associat...\\\"}, {\\\"key\\\": \\\"tian2024debugbench\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"DebugBench: Evaluating Debugging Capability of Large Language Models\\\", \\\"authors\\\": \\\"Runchu Tian and Yining Ye and Yujia Qin and Xin Cong and Yankai Lin and Yinxu Pa...\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"Findings of the Association for Computational Linguistics: ACL 2024\\\"}, {\\\"key\\\": \\\"abreu2007accuracy\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"On the Accuracy of Spectrum-based Fault Localization\\\", \\\"authors\\\": \\\"Rui Abreu and Peter Zoeteweij and Arjan J.C. van Gemund\\\", \\\"year\\\": \\\"2007\\\", \\\"venue\\\": \\\"Testing: Academic and Industrial Conference Practice and Research Techniques (MU...\\\"}, {\\\"key\\\": \\\"jones2002visualization\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Visualization of Test Information to Assist Fault Localization\\\", \\\"authors\\\": \\\"James A. Jones and Mary Jean Harrold and John Stasko\\\", \\\"year\\\": \\\"2002\\\", \\\"venue\\\": \\\"Proceedings of the 24th International Conference on Software Engineering (ICSE)\\\"}, {\\\"key\\\": \\\"wong2014dstar\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"DStar: An Effective Spectrum-Based Fault Localization Technique\\\", \\\"authors\\\": \\\"W. Eric Wong and Vidroha Debroy and Ruizhi Gao and Yihao Li\\\", \\\"year\\\": \\\"2014\\\", \\\"venue\\\": \\\"Journal of Systems and Software\\\"}, {\\\"key\\\": \\\"kang2024autofl\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"AutoFL: Automated Fault Localization via Large Language Models\\\", \\\"authors\\\": \\\"Sungmin Kang and Gabin An and Shin Yoo\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"Proceedings of the 46th IEEE/ACM International Conference on Software Engineerin...\\\"}, {\\\"key\\\": \\\"qin2024agentfl\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"AgentFL: Scaling LLM-based Fault Localization to Project-Level Context\\\", \\\"authors\\\": \\\"Yihao Qin and Shangwen Wang and Yiling Lou and Jinhao Dong and Kaixin Wang and X...\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"Proceedings of the 39th IEEE/ACM International Conference on Automated Software ...\\\"}, {\\\"key\\\": \\\"widyasari2024llm4fl\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"LLM4FL: An LLM-based Fault Localization Integrated Debugging Framework for Automated Program Repair\\\", \\\"authors\\\": \\\"Ratnadira Widyasari and Gopi Krishnan Rajbahadur and Shin Hwei Tan and Xin Xia a...\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"Proceedings of the 47th IEEE/ACM International Conference on Software Engineerin...\\\"}, {\\\"key\\\": \\\"mukherjee2025llmfl\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Can Large Language Models Localize Faults like Developers? A Comprehensive Study\\\", \\\"authors\\\": \\\"Soneya Binta Hossain and Nan Jiang and Qiang Zhou and Xiaopeng Li and Wen-Hao Ch...\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"Proceedings of the 47th IEEE/ACM International Conference on Software Engineerin...\\\"}, {\\\"key\\\": \\\"roziere2024code\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Code Llama: Open Foundation Models for Code\\\", \\\"authors\\\": \\\"Baptiste Rozi\\\\\\\\`ere and Jonas Gehring and Fabian Gloeckle and Sten Sootla and Ita...\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"arXiv preprint arXiv:2308.12950\\\"}, {\\\"key\\\": \\\"dinella2022toga\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"TOGA: A Neural Method for Test Oracle Generation\\\", \\\"authors\\\": \\\"Elizabeth Dinella and Gabriel Ryan and Todd Mytkowicz and Shuvendu K. Lahiri\\\", \\\"year\\\": \\\"2022\\\", \\\"venue\\\": \\\"Proceedings of the 44th IEEE/ACM International Conference on Software Engineerin...\\\"}, {\\\"key\\\": \\\"steenhoek2024deepdfa\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Dataflow Analysis-Inspired Deep Learning for Efficient Vulnerability Detection\\\", \\\"authors\\\": \\\"Benjamin Steenhoek and Hongyang Gao and Wei Le\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"Proceedings of the 46th IEEE/ACM International Conference on Software Engineerin...\\\"}, {\\\"key\\\": \\\"jimenez2024swebench\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"SWE-bench: Can Language Models Resolve Real-World GitHub Issues?\\\", \\\"authors\\\": \\\"Carlos E. Jimenez and John Yang and Alexander Wettig and Shunyu Yao and Kexin Pe...\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"Proceedings of the 12th International Conference on Learning Representations (IC...\\\"}, {\\\"key\\\": \\\"kadavath2022language\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Language Models (Mostly) Know What They Know\\\", \\\"authors\\\": \\\"Saurav Kadavath and Tom Conerly and Amanda Askell and Tom Henighan and Dawn Drai...\\\", \\\"year\\\": \\\"2022\\\", \\\"venue\\\": \\\"arXiv preprint arXiv:2207.05221\\\"}, {\\\"key\\\": \\\"kamei2013large\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"A Large-Scale Empirical Study of Just-in-Time Quality Assurance\\\", \\\"authors\\\": \\\"Yasutaka Kamei and Emad Shihab and Bram Adams and Ahmed E. Hassan and Audris Moc...\\\", \\\"year\\\": \\\"2013\\\", \\\"venue\\\": \\\"IEEE Transactions on Software Engineering\\\"}, {\\\"key\\\": \\\"bouzenia2025repairagent\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"RepairAgent: An Autonomous, LLM-Based Agent for Program Repair\\\", \\\"authors\\\": \\\"Islem Bouzenia and Premkumar Devanbu and Michael Pradel\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"Proceedings of the 47th IEEE/ACM International Conference on Software Engineerin...\\\"}, {\\\"key\\\": \\\"chen2024selfdebug\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Teaching Large Language Models to Self-Debug\\\", \\\"authors\\\": \\\"Xinyun Chen and Maxwell Lin and Nathanael Sch\\\\\\\\\\\\\\\"arli and Denny Zhou\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"Proceedings of the 12th International Conference on Learning Representations (IC...\\\"}, {\\\"key\\\": \\\"liu2023codeexecution\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Code Execution with Pre-trained Language Models\\\", \\\"authors\\\": \\\"Chenxiao Liu and Shuai Lu and Weizhu Chen and Daxin Jiang and Alexey Svyatkovski...\\\", \\\"year\\\": \\\"2023\\\", \\\"venue\\\": \\\"Findings of the Association for Computational Linguistics: ACL 2023\\\"}, {\\\"key\\\": \\\"tian2020patchcorrectness\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Evaluating Representation Learning of Code Changes for Predicting Patch Correctness in Program Repair\\\", \\\"authors\\\": \\\"Haoye Tian and Kui Liu and Abdoul Kader Kabor\\\\\\\\'e and Anil Koyuncu and Li Li and ...\\\", \\\"year\\\": \\\"2020\\\", \\\"venue\\\": \\\"Proceedings of the 35th IEEE/ACM International Conference on Automated Software ...\\\"}, {\\\"key\\\": \\\"watson2020atlas\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"On Learning Meaningful Assert Statements for Unit Test Cases\\\", \\\"authors\\\": \\\"Cody Watson and Michele Tufano and Kevin Moran and Gabriele Bavota and Denys Pos...\\\", \\\"year\\\": \\\"2020\\\", \\\"venue\\\": \\\"Proceedings of the ACM/IEEE 42nd International Conference on Software Engineerin...\\\"}, {\\\"key\\\": \\\"yu2022assertion\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Automated Assertion Generation via Information Retrieval and Its Integration with Deep Learning\\\", \\\"authors\\\": \\\"Hao Yu and Yiling Lou and Ke Sun and Dezhi Ran and Tao Xie and Dan Hao and Ying ...\\\", \\\"year\\\": \\\"2022\\\", \\\"venue\\\": \\\"Proceedings of the 44th IEEE/ACM International Conference on Software Engineerin...\\\"}, {\\\"key\\\": \\\"nashid2023assertion\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Revisiting and Improving Retrieval-Augmented Deep Assertion Generation\\\", \\\"authors\\\": \\\"Noor Nashid and Taha Shabani and Ali Mesbah\\\", \\\"year\\\": \\\"2023\\\", \\\"venue\\\": \\\"Proceedings of the 38th IEEE/ACM International Conference on Automated Software ...\\\"}, {\\\"key\\\": \\\"yadavally2024slicing\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"A Learning-Based Approach to Static Program Slicing\\\", \\\"authors\\\": \\\"Aashish Yadavally and Yi Li and Shaohua Wang and Tien N. Nguyen\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"Proceedings of the ACM on Programming Languages (OOPSLA)\\\"}, {\\\"key\\\": \\\"xia2024agentless\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Agentless: Demystifying LLM-based Software Engineering Agents\\\", \\\"authors\\\": \\\"Chunqiu Steven Xia and Yinlin Deng and Soren Dunn and Lingming Zhang\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"arXiv preprint arXiv:2407.01489\\\"}, {\\\"key\\\": \\\"guo2017calibration\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"On Calibration of Modern Neural Networks\\\", \\\"authors\\\": \\\"Chuan Guo and Geoff Pleiss and Yu Sun and Kilian Q. Weinberger\\\", \\\"year\\\": \\\"2017\\\", \\\"venue\\\": \\\"Proceedings of the 34th International Conference on Machine Learning (ICML)\\\"}, {\\\"key\\\": \\\"geng2024calibration\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"A Survey of Confidence Estimation and Calibration in Large Language Models\\\", \\\"authors\\\": \\\"Jiahui Geng and Fengyu Cai and Yuxia Wang and Heinz Koeppl and Preslav Nakov and...\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"Proceedings of the 2024 Conference of the North American Chapter of the Associat...\\\"}, {\\\"key\\\": \\\"hoang2019deepjit\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"DeepJIT: An End-to-End Deep Learning Framework for Just-in-Time Defect Prediction\\\", \\\"authors\\\": \\\"Thong Hoang and Hoa Khanh Dam and Yasutaka Kamei and David Lo and Naoyasu Ubayas...\\\", \\\"year\\\": \\\"2019\\\", \\\"venue\\\": \\\"Proceedings of the 16th International Conference on Mining Software Repositories...\\\"}, {\\\"key\\\": \\\"hoang2020cc2vec\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"CC2Vec: Distributed Representations of Code Changes\\\", \\\"authors\\\": \\\"Thong Hoang and Hong Jin Kang and Julia Lawall and David Lo\\\", \\\"year\\\": \\\"2020\\\", \\\"venue\\\": \\\"Proceedings of the ACM/IEEE 42nd International Conference on Software Engineerin...\\\"}, {\\\"key\\\": \\\"pornprasit2021jitline\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"JITLine: A Simpler, Better, Faster, Finer-grained Just-In-Time Defect Prediction\\\", \\\"authors\\\": \\\"Chanathip Pornprasit and Chakkrit Tantithamthavorn\\\", \\\"year\\\": \\\"2021\\\", \\\"venue\\\": \\\"Proceedings of the 18th International Conference on Mining Software Repositories...\\\"}, {\\\"key\\\": \\\"bengio2009curriculum\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Curriculum Learning\\\", \\\"authors\\\": \\\"Yoshua Bengio and J\\\\\\\\'er\\\\\\\\^ome Louradour and Ronan Collobert and Jason Weston\\\", \\\"year\\\": \\\"2009\\\", \\\"venue\\\": \\\"Proceedings of the 26th Annual International Conference on Machine Learning (ICM...\\\"}, {\\\"key\\\": \\\"sachdeva2024dataefficient\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"How to Train Data-Efficient LLMs\\\", \\\"authors\\\": \\\"Noveen Sachdeva and Benjamin Coleman and Wang-Cheng Kang and Jianmo Ni and Licha...\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"arXiv preprint arXiv:2402.09668\\\"}, {\\\"key\\\": \\\"swayamdipta2020cartography\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Dataset Cartography: Mapping and Diagnosing Datasets with Training Dynamics\\\", \\\"authors\\\": \\\"Swabha Swayamdipta and Roy Schwartz and Nicholas Lourie and Yizhong Wang and Han...\\\", \\\"year\\\": \\\"2020\\\", \\\"venue\\\": \\\"Proceedings of the 2020 Conference on Empirical Methods in Natural Language Proc...\\\"}, {\\\"key\\\": \\\"xie2023doremi\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"DoReMi: Optimizing Data Mixtures Speeds Up Language Model Pretraining\\\", \\\"authors\\\": \\\"Sang Michael Xie and Hieu Pham and Xuanyi Dong and Nan Du and Hanxiao Liu and Yi...\\\", \\\"year\\\": \\\"2023\\\", \\\"venue\\\": \\\"Advances in Neural Information Processing Systems (NeurIPS)\\\"}], \\\"tex_citations\\\": [{\\\"key\\\": \\\"chen2025tracepile\\\", \\\"file\\\": \\\"introduction.tex\\\", \\\"line\\\": 3, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"ding2024traced\\\", \\\"file\\\": \\\"introduction.tex\\\", \\\"line\\\": 3, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"wang2025dcsh\\\", \\\"file\\\": \\\"introduction.tex\\\", \\\"line\\\": 3, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"ni2024next\\\", \\\"file\\\": \\\"introduction.tex\\\", \\\"line\\\": 3, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"wang2025dcsh\\\", \\\"file\\\": \\\"introduction.tex\\\", \\\"line\\\": 7, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"chen2021evaluating\\\", \\\"file\\\": \\\"introduction.tex\\\", \\\"line\\\": 13, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"austin2021program\\\", \\\"file\\\": \\\"introduction.tex\\\", \\\"line\\\": 13, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"qwen2025coder\\\", \\\"file\\\": \\\"introduction.tex\\\", \\\"line\\\": 13, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"roziere2024code\\\", \\\"file\\\": \\\"introduction.tex\\\", \\\"line\\\": 13, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"deepseek2024coder\\\", \\\"file\\\": \\\"introduction.tex\\\", \\\"line\\\": 13, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"chen2025tracepile\\\", \\\"file\\\": \\\"method.tex\\\", \\\"line\\\": 7, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"gu2024cruxeval\\\", \\\"file\\\": \\\"method.tex\\\", \\\"line\\\": 7, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"chen2021evaluating\\\", \\\"file\\\": \\\"method.tex\\\", \\\"line\\\": 12, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"austin2021program\\\", \\\"file\\\": \\\"method.tex\\\", \\\"line\\\": 12, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"qwen2025coder\\\", \\\"file\\\": \\\"method.tex\\\", \\\"line\\\": 38, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"roziere2024code\\\", \\\"file\\\": \\\"method.tex\\\", \\\"line\\\": 38, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"deepseek2024coder\\\", \\\"file\\\": \\\"method.tex\\\", \\\"line\\\": 38, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"hu2022lora\\\", \\\"file\\\": \\\"method.tex\\\", \\\"line\\\": 39, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"tian2024debugbench\\\", \\\"file\\\": \\\"experiments.tex\\\", \\\"line\\\": 173, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"chen2025tracepile\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 4, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"wang2025dcsh\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 4, \\\"command\\\": \\\"citet\\\"}, {\\\"key\\\": \\\"ni2024next\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 5, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"eguchi2025etcot\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 5, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"ferrando2025execute\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 5, \\\"command\\\": \\\"citet\\\"}, {\\\"key\\\": \\\"liu2023codeexecution\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 6, \\\"command\\\": \\\"citet\\\"}, {\\\"key\\\": \\\"chen2024selfdebug\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 6, \\\"command\\\": \\\"citet\\\"}, {\\\"key\\\": \\\"gu2024cruxeval\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 7, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"xu2025cruxevalx\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 7, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"ding2024traced\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 11, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"steenhoek2024deepdfa\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 11, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"yadavally2024slicing\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 11, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"tian2020patchcorrectness\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 12, \\\"command\\\": \\\"citet\\\"}, {\\\"key\\\": \\\"hoang2020cc2vec\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 12, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"zhou2024llm4patch\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 12, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"appt2024\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 12, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"watson2020atlas\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 13, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"yu2022assertion\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 13, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"nashid2023assertion\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 13, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"dinella2022toga\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 13, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"widyasari2024fusefl\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 13, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"foster2025mutation\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 13, \\\"command\\\": \\\"citet\\\"}, {\\\"key\\\": \\\"abreu2007accuracy\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 17, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"jones2002visualization\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 17, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"wong2014dstar\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 17, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"kang2024autofl\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 17, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"qin2024agentfl\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 17, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"widyasari2024llm4fl\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 17, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"mukherjee2025llmfl\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 17, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"huang2026tracecoder\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 21, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"wang2025inspectcoder\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 21, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"bouzenia2025repairagent\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 21, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"xia2024agentless\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 21, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"haque2025traces\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 22, \\\"command\\\": \\\"citet\\\"}, {\\\"key\\\": \\\"jimenez2024swebench\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 22, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"guo2017calibration\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 26, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"kadavath2022language\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 26, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"geng2024calibration\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 26, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"spiess2025calibration\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 26, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"kamei2013large\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 27, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"hoang2019deepjit\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 27, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"pornprasit2021jitline\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 27, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"bengio2009curriculum\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 30, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"swayamdipta2020cartography\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 30, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"sachdeva2024dataefficient\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 30, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"xie2023doremi\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 30, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"hu2022lora\\\", \\\"file\\\": \\\"appendix.tex\\\", \\\"line\\\": 37, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"spiess2025calibration\\\", \\\"file\\\": \\\"appendix.tex\\\", \\\"line\\\": 509, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"tian2024debugbench\\\", \\\"file\\\": \\\"appendix.tex\\\", \\\"line\\\": 588, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"yang2024generalization\\\", \\\"file\\\": \\\"appendix.tex\\\", \\\"line\\\": 626, \\\"command\\\": \\\"citep\\\"}], \\\"online_verification\\\": [{\\\"key\\\": \\\"chen2025tracepile\\\", \\\"title\\\": \\\"Chain of Execution Supervision Promotes General Reasoning in Large Language Models\\\", \\\"status\\\": \\\"not_found\\\", \\\"confidence\\\": 0.452, \\\"matched_title\\\": \\\"A Survey of Large Language Models\\\", \\\"matched_year\\\": \\\"\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"best match similarity 0.45 below threshold 0.82\\\"}, {\\\"key\\\": \\\"ding2024traced\\\", \\\"title\\\": \\\"TRACED: Execution-aware Pre-training for Source Code\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"TRACED: Execution-aware Pre-training for Source Code\\\", \\\"matched_year\\\": \\\"2024\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"chen2021evaluating\\\", \\\"title\\\": \\\"Evaluating Large Language Models Trained on Code\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Evaluating Large Language Models Trained on Code\\\", \\\"matched_year\\\": \\\"2021\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"austin2021program\\\", \\\"title\\\": \\\"Program Synthesis with Large Language Models\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Program Synthesis with Large Language Models\\\", \\\"matched_year\\\": \\\"2021\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"gu2024cruxeval\\\", \\\"title\\\": \\\"CRUXEval: A Benchmark for Code Reasoning, Understanding and Execution\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"CRUXEval: A Benchmark for Code Reasoning, Understanding and Execution\\\", \\\"matched_year\\\": \\\"2024\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"hu2022lora\\\", \\\"title\\\": \\\"LoRA: Low-Rank Adaptation of Large Language Models\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"LoRA: Low-Rank Adaptation of Large Language Models\\\", \\\"matched_year\\\": \\\"2021\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"qwen2025coder\\\", \\\"title\\\": \\\"Qwen2.5-Coder Technical Report\\\", \\\"status\\\": \\\"mismatch\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Qwen2.5-Coder Technical Report\\\", \\\"matched_year\\\": \\\"2024\\\", \\\"mismatch_fields\\\": [\\\"first_author: bib=team vs api=hui\\\"], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"deepseek2024coder\\\", \\\"title\\\": \\\"DeepSeek-Coder: When the Large Language Model Meets Programming -- The Rise of Code Intelligence\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"DeepSeek-Coder: When the Large Language Model Meets Programming -- The Rise of Code Intelligence\\\", \\\"matched_year\\\": \\\"2024\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"wang2025dcsh\\\", \\\"title\\\": \\\"Do Code Semantics Help? A Comprehensive Study on Execution Trace-Based Information for Code Large Language Models\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Do Code Semantics Help? A Comprehensive Study on Execution Trace-Based Information for Code Large Language Models\\\", \\\"matched_year\\\": \\\"2025\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"ni2024next\\\", \\\"title\\\": \\\"NExT: Teaching Large Language Models to Reason about Code Execution\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"NExT: Teaching Large Language Models to Reason about Code Execution\\\", \\\"matched_year\\\": \\\"2024\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"eguchi2025etcot\\\", \\\"title\\\": \\\"Making LLMs Program Interpreters via Execution Trace Chain of Thought\\\", \\\"status\\\": \\\"not_found\\\", \\\"confidence\\\": 0.203, \\\"matched_title\\\": \\\"From ChatGPT to ThreatGPT: Impact of Generative AI in Cybersecurity and Privacy\\\", \\\"matched_year\\\": \\\"\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"best match similarity 0.20 below threshold 0.82\\\"}, {\\\"key\\\": \\\"ferrando2025execute\\\", \\\"title\\\": \\\"What I Cannot Execute, I Do Not Understand: Training and Evaluating LLMs on Program Execution Traces\\\", \\\"status\\\": \\\"not_found\\\", \\\"confidence\\\": 0.199, \\\"matched_title\\\": \\\"Sparks of Artificial General Intelligence: Early experiments with GPT-4\\\", \\\"matched_year\\\": \\\"\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"best match similarity 0.20 below threshold 0.82\\\"}, {\\\"key\\\": \\\"xu2025cruxevalx\\\", \\\"title\\\": \\\"CRUXEval-X: A Benchmark for Multilingual Code Reasoning, Understanding and Execution\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"CRUXEVAL-X: A Benchmark for Multilingual Code Reasoning, Understanding and Execution\\\", \\\"matched_year\\\": \\\"2025\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"appt2024\\\", \\\"title\\\": \\\"APPT: Boosting Automated Patch Correctness Prediction via Fine-tuning Pre-trained Models\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"APPT: Boosting Automated Patch Correctness Prediction via Fine-Tuning Pre-Trained Models\\\", \\\"matched_year\\\": \\\"2024\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"zhou2024llm4patch\\\", \\\"title\\\": \\\"Leveraging Large Language Model for Automatic Patch Correctness Assessment\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Leveraging Large Language Model for Automatic Patch Correctness Assessment\\\", \\\"matched_year\\\": \\\"2024\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"spiess2025calibration\\\", \\\"title\\\": \\\"Calibration and Correctness of Language Models for Code\\\", \\\"status\\\": \\\"mismatch\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Calibration and Correctness of Language Models for Code\\\", \\\"matched_year\\\": \\\"2025\\\", \\\"mismatch_fields\\\": [\\\"first_author: bib=spiess vs api=spieß\\\"], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"foster2025mutation\\\", \\\"title\\\": \\\"Mutation-Guided LLM-based Test Generation at Meta\\\", \\\"status\\\": \\\"mismatch\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Mutation-Guided LLM-based Test Generation at Meta\\\", \\\"matched_year\\\": \\\"2025\\\", \\\"mismatch_fields\\\": [\\\"first_author: bib=foster vs api=harman\\\"], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"widyasari2024fusefl\\\", \\\"title\\\": \\\"Demystifying Faulty Code: Step-by-Step Reasoning for Explainable Fault Localization\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Demystifying Faulty Code: Step-by-Step Reasoning for Explainable Fault Localization\\\", \\\"matched_year\\\": \\\"2024\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"huang2026tracecoder\\\", \\\"title\\\": \\\"TraceCoder: A Trace-Driven Multi-Agent Framework for Automated Debugging of LLM-Generated Code\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"TraceCoder: A Trace-Driven Multi-Agent Framework for Automated Debugging of LLM-Generated Code\\\", \\\"matched_year\\\": \\\"2026\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"wang2025inspectcoder\\\", \\\"title\\\": \\\"InspectCoder: Dynamic Analysis-Enabled Self Repair through Interactive LLM-Debugger Collaboration\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"InspectCoder: Dynamic Analysis-Enabled Self Repair through interactive LLM-Debugger Collaboration\\\", \\\"matched_year\\\": \\\"2025\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"haque2025traces\\\", \\\"title\\\": \\\"Towards Effectively Leveraging Execution Traces for Program Repair with Code LLMs\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Towards Effectively Leveraging Execution Traces for Program Repair with Code LLMs\\\", \\\"matched_year\\\": \\\"2025\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"yang2024generalization\\\", \\\"title\\\": \\\"Unveiling the Generalization Power of Fine-Tuned Large Language Models\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Unveiling the Generalization Power of Fine-Tuned Large Language Models\\\", \\\"matched_year\\\": \\\"2024\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"tian2024debugbench\\\", \\\"title\\\": \\\"DebugBench: Evaluating Debugging Capability of Large Language Models\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"DebugBench: Evaluating Debugging Capability of Large Language Models\\\", \\\"matched_year\\\": \\\"2024\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"abreu2007accuracy\\\", \\\"title\\\": \\\"On the Accuracy of Spectrum-based Fault Localization\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"On the Accuracy of Spectrum-based Fault Localization\\\", \\\"matched_year\\\": \\\"2007\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"jones2002visualization\\\", \\\"title\\\": \\\"Visualization of Test Information to Assist Fault Localization\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Visualization of test information to assist fault localization\\\", \\\"matched_year\\\": \\\"2002\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"wong2014dstar\\\", \\\"title\\\": \\\"DStar: An Effective Spectrum-Based Fault Localization Technique\\\", \\\"status\\\": \\\"not_found\\\", \\\"confidence\\\": 0.561, \\\"matched_title\\\": \\\"MSFL: A Model for Fault Localization Using Mutation-Spectra Technique\\\", \\\"matched_year\\\": \\\"\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"best match similarity 0.56 below threshold 0.82\\\"}, {\\\"key\\\": \\\"kang2024autofl\\\", \\\"title\\\": \\\"AutoFL: Automated Fault Localization via Large Language Models\\\", \\\"status\\\": \\\"not_found\\\", \\\"confidence\\\": 0.45, \\\"matched_title\\\": \\\"A Survey on Large Language Models for Software Engineering\\\", \\\"matched_year\\\": \\\"\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"best match similarity 0.45 below threshold 0.82\\\"}, {\\\"key\\\": \\\"qin2024agentfl\\\", \\\"title\\\": \\\"AgentFL: Scaling LLM-based Fault Localization to Project-Level Context\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"AgentFL: Scaling LLM-based Fault Localization to Project-Level Context\\\", \\\"matched_year\\\": \\\"2024\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"widyasari2024llm4fl\\\", \\\"title\\\": \\\"LLM4FL: An LLM-based Fault Localization Integrated Debugging Framework for Automated Program Repair\\\", \\\"status\\\": \\\"not_found\\\", \\\"confidence\\\": 0.448, \\\"matched_title\\\": \\\"A Multi-Agent Approach to Fault Localization via Graph-Based Retrieval and Reflexion\\\", \\\"matched_year\\\": \\\"\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"best match similarity 0.45 below threshold 0.82\\\"}, {\\\"key\\\": \\\"mukherjee2025llmfl\\\", \\\"title\\\": \\\"Can Large Language Models Localize Faults like Developers? A Comprehensive Study\\\", \\\"status\\\": \\\"not_found\\\", \\\"confidence\\\": 0.186, \\\"matched_title\\\": \\\"Internet of Things (IoT): A vision, architectural elements, and future directions\\\", \\\"matched_year\\\": \\\"\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"best match similarity 0.19 below threshold 0.82\\\"}, {\\\"key\\\": \\\"roziere2024code\\\", \\\"title\\\": \\\"Code Llama: Open Foundation Models for Code\\\", \\\"status\\\": \\\"mismatch\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Code Llama: Open Foundation Models for Code\\\", \\\"matched_year\\\": \\\"2023\\\", \\\"mismatch_fields\\\": [\\\"first_author: bib=rozi\\\\\\\\`ere vs api=rozière\\\"], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"dinella2022toga\\\", \\\"title\\\": \\\"TOGA: A Neural Method for Test Oracle Generation\\\", \\\"status\\\": \\\"not_found\\\", \\\"confidence\\\": 0.623, \\\"matched_title\\\": \\\"TOGLL: Correct and Strong Test Oracle Generation with LLMs\\\", \\\"matched_year\\\": \\\"\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"best match similarity 0.62 below threshold 0.82\\\"}, {\\\"key\\\": \\\"steenhoek2024deepdfa\\\", \\\"title\\\": \\\"Dataflow Analysis-Inspired Deep Learning for Efficient Vulnerability Detection\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Dataflow Analysis-Inspired Deep Learning for Efficient Vulnerability Detection\\\", \\\"matched_year\\\": \\\"2024\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"jimenez2024swebench\\\", \\\"title\\\": \\\"SWE-bench: Can Language Models Resolve Real-World GitHub Issues?\\\", \\\"status\\\": \\\"mismatch\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"SWE-bench: Can Language Models Resolve Real-World GitHub Issues?\\\", \\\"matched_year\\\": \\\"2023\\\", \\\"mismatch_fields\\\": [\\\"first_author: bib=jimenez vs api=jimenez-gomez\\\"], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"kadavath2022language\\\", \\\"title\\\": \\\"Language Models (Mostly) Know What They Know\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Language Models (Mostly) Know What They Know\\\", \\\"matched_year\\\": \\\"2022\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"kamei2013large\\\", \\\"title\\\": \\\"A Large-Scale Empirical Study of Just-in-Time Quality Assurance\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"A large-scale empirical study of just-in-time quality assurance\\\", \\\"matched_year\\\": \\\"2012\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"bouzenia2025repairagent\\\", \\\"title\\\": \\\"RepairAgent: An Autonomous, LLM-Based Agent for Program Repair\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"RepairAgent: An Autonomous, LLM-Based Agent for Program Repair\\\", \\\"matched_year\\\": \\\"2025\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"chen2024selfdebug\\\", \\\"title\\\": \\\"Teaching Large Language Models to Self-Debug\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Teaching Large Language Models to Self-Debug\\\", \\\"matched_year\\\": \\\"2023\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"liu2023codeexecution\\\", \\\"title\\\": \\\"Code Execution with Pre-trained Language Models\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Code Execution with Pre-trained Language Models\\\", \\\"matched_year\\\": \\\"2023\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"tian2020patchcorrectness\\\", \\\"title\\\": \\\"Evaluating Representation Learning of Code Changes for Predicting Patch Correctness in Program Repair\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Evaluating representation learning of code changes for predicting patch correctness in program repair\\\", \\\"matched_year\\\": \\\"2020\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"watson2020atlas\\\", \\\"title\\\": \\\"On Learning Meaningful Assert Statements for Unit Test Cases\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"On learning meaningful assert statements for unit test cases\\\", \\\"matched_year\\\": \\\"2020\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"yu2022assertion\\\", \\\"title\\\": \\\"Automated Assertion Generation via Information Retrieval and Its Integration with Deep Learning\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Automated assertion generation via information retrieval and its integration with deep learning\\\", \\\"matched_year\\\": \\\"2022\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"nashid2023assertion\\\", \\\"title\\\": \\\"Revisiting and Improving Retrieval-Augmented Deep Assertion Generation\\\", \\\"status\\\": \\\"mismatch\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Revisiting and Improving Retrieval-Augmented Deep Assertion Generation\\\", \\\"matched_year\\\": \\\"2023\\\", \\\"mismatch_fields\\\": [\\\"first_author: bib=nashid vs api=sun\\\"], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"yadavally2024slicing\\\", \\\"title\\\": \\\"A Learning-Based Approach to Static Program Slicing\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"A Learning-Based Approach to Static Program Slicing\\\", \\\"matched_year\\\": \\\"2024\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"xia2024agentless\\\", \\\"title\\\": \\\"Agentless: Demystifying LLM-based Software Engineering Agents\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Agentless: Demystifying LLM-based Software Engineering Agents\\\", \\\"matched_year\\\": \\\"2024\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"guo2017calibration\\\", \\\"title\\\": \\\"On Calibration of Modern Neural Networks\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"On Calibration of Modern Neural Networks\\\", \\\"matched_year\\\": \\\"2017\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"geng2024calibration\\\", \\\"title\\\": \\\"A Survey of Confidence Estimation and Calibration in Large Language Models\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"A Survey of Confidence Estimation and Calibration in Large Language Models\\\", \\\"matched_year\\\": \\\"2024\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"hoang2019deepjit\\\", \\\"title\\\": \\\"DeepJIT: An End-to-End Deep Learning Framework for Just-in-Time Defect Prediction\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"DeepJIT: An End-to-End Deep Learning Framework for Just-in-Time Defect Prediction\\\", \\\"matched_year\\\": \\\"2019\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"hoang2020cc2vec\\\", \\\"title\\\": \\\"CC2Vec: Distributed Representations of Code Changes\\\", \\\"status\\\": \\\"mismatch\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"CC2Vec: Distributed Representations of Code Changes\\\", \\\"matched_year\\\": \\\"2020\\\", \\\"mismatch_fields\\\": [\\\"first_author: bib=hoang vs api=thong\\\"], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"pornprasit2021jitline\\\", \\\"title\\\": \\\"JITLine: A Simpler, Better, Faster, Finer-grained Just-In-Time Defect Prediction\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"JITLine: A Simpler, Better, Faster, Finer-grained Just-In-Time Defect Prediction\\\", \\\"matched_year\\\": \\\"2021\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"bengio2009curriculum\\\", \\\"title\\\": \\\"Curriculum Learning\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Curriculum learning\\\", \\\"matched_year\\\": \\\"2009\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"sachdeva2024dataefficient\\\", \\\"title\\\": \\\"How to Train Data-Efficient LLMs\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"How to Train Data-Efficient LLMs\\\", \\\"matched_year\\\": \\\"2024\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"swayamdipta2020cartography\\\", \\\"title\\\": \\\"Dataset Cartography: Mapping and Diagnosing Datasets with Training Dynamics\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Dataset Cartography: Mapping and Diagnosing Datasets with Training Dynamics\\\", \\\"matched_year\\\": \\\"2020\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"xie2023doremi\\\", \\\"title\\\": \\\"DoReMi: Optimizing Data Mixtures Speeds Up Language Model Pretraining\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"DoReMi: Optimizing Data Mixtures Speeds Up Language Model Pretraining\\\", \\\"matched_year\\\": \\\"2023\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}]}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"summary\": {\"total_bib_entries\": 54, \"total_citations\": 69, \"unique_cited_keys\": 54, \"orphan_bib\": 0, \"missing_bib\": 0, \"duplicate_keys\": 0, \"online_verified\": 39, \"online_not_found\": 8, \"online_mismatch\": 7}, \"cross_check\": {\"orphan_bib\": [], \"missing_bib\": [], \"orphan_count\": 0, \"missing_count\": 0}, \"bib_entries\": [{\"key\": \"chen2025tracepile\", \"type\": \"inproceedings\", \"title\": \"Chain of Execution Supervision Promotes General Reasoning in Large Language Models\", \"authors\": \"Nuo Chen and Zehua Li and Keqin Bao and Junyang Lin and Dayiheng Liu\", \"year\": \"2025\", \"venue\": \"Advances in Neural Information Processing Systems (NeurIPS)\"}, {\"key\": \"ding2024traced\", \"type\": \"inproceedings\", \"title\": \"TRACED: Execution-aware Pre-training for Source Code\", \"authors\": \"Yangruibo Ding and Ben Steenhoek and Kexin Pei and Gail Kaiser and Wei Le and Ba...\", \"year\": \"2024\", \"venue\": \"Proceedings of the 46th IEEE/ACM International Conference on Software Engineerin...\"}, {\"key\": \"chen2021evaluating\", \"type\": \"article\", \"title\": \"Evaluating Large Language Models Trained on Code\", \"authors\": \"Chen, Mark and Tworek, Jerry and Jun, Heewoo and Yuan, Qiming and Pinto, Henriqu...\", \"year\": \"2021\", \"venue\": \"arXiv preprint arXiv:2107.03374\"}, {\"key\": \"austin2021program\", \"type\": \"article\", \"title\": \"Program Synthesis with Large Language Models\", \"authors\": \"Austin, Jacob and Odena, Augustus and Nye, Maxwell and Bosma, Maarten and Michal...\", \"year\": \"2021\", \"venue\": \"arXiv preprint arXiv:2108.07732\"}, {\"key\": \"gu2024cruxeval\", \"type\": \"inproceedings\", \"title\": \"CRUXEval: A Benchmark for Code Reasoning, Understanding and Execution\", \"authors\": \"Alex Gu and Baptiste Rozi\\\\`ere and Hugh Leather and Armando Solar-Lezama and Gab...\", \"year\": \"2024\", \"venue\": \"Proceedings of the 41st International Conference on Machine Learning (ICML)\"}, {\"key\": \"hu2022lora\", \"type\": \"inproceedings\", \"title\": \"LoRA: Low-Rank Adaptation of Large Language Models\", \"authors\": \"Edward J. Hu and Yelong Shen and Phillip Wallis and Zeyuan Allen-Zhu and Yuanzhi...\", \"year\": \"2022\", \"venue\": \"Proceedings of the 10th International Conference on Learning Representations (IC...\"}, {\"key\": \"qwen2025coder\", \"type\": \"article\", \"title\": \"Qwen2.5-Coder Technical Report\", \"authors\": \"Qwen Team\", \"year\": \"2024\", \"venue\": \"arXiv preprint arXiv:2409.12186\"}, {\"key\": \"deepseek2024coder\", \"type\": \"article\", \"title\": \"DeepSeek-Coder: When the Large Language Model Meets Programming -- The Rise of Code Intelligence\", \"authors\": \"Daya Guo and Qihao Zhu and Dejian Yang and Zhenda Xie and Kai Dong and Wentao Zh...\", \"year\": \"2024\", \"venue\": \"arXiv preprint arXiv:2401.14196\"}, {\"key\": \"wang2025dcsh\", \"type\": \"inproceedings\", \"title\": \"Do Code Semantics Help? A Comprehensive Study on Execution Trace-Based Information for Code Large Language Models\", \"authors\": \"Jian Wang and Xiaofei Xie and Qiang Hu and Shangqing Liu and Yi Li\", \"year\": \"2025\", \"venue\": \"Findings of the Association for Computational Linguistics: EMNLP 2025\"}, {\"key\": \"ni2024next\", \"type\": \"inproceedings\", \"title\": \"NExT: Teaching Large Language Models to Reason about Code Execution\", \"authors\": \"Ansong Ni and Miltiadis Allamanis and Arman Cohan and Yinlin Deng and Kensen Shi...\", \"year\": \"2024\", \"venue\": \"Proceedings of the 41st International Conference on Machine Learning (ICML)\"}, {\"key\": \"eguchi2025etcot\", \"type\": \"inproceedings\", \"title\": \"Making LLMs Program Interpreters via Execution Trace Chain of Thought\", \"authors\": \"Koshi Eguchi and Takuya Akiba\", \"year\": \"2025\", \"venue\": \"ICML 2025 Workshop on Programmatic Representations for Agent Learning (PRAL)\"}, {\"key\": \"ferrando2025execute\", \"type\": \"article\", \"title\": \"What I Cannot Execute, I Do Not Understand: Training and Evaluating LLMs on Program Execution Traces\", \"authors\": \"Jordi Armengol-Estape and Quentin Carbonneaux and Tianjun Zhang and Aram H. Mark...\", \"year\": \"2025\", \"venue\": \"arXiv preprint arXiv:2503.05703\"}, {\"key\": \"xu2025cruxevalx\", \"type\": \"inproceedings\", \"title\": \"CRUXEval-X: A Benchmark for Multilingual Code Reasoning, Understanding and Execution\", \"authors\": \"Ruiyang Xu and others\", \"year\": \"2025\", \"venue\": \"Proceedings of the 63rd Annual Meeting of the Association for Computational Ling...\"}, {\"key\": \"appt2024\", \"type\": \"article\", \"title\": \"APPT: Boosting Automated Patch Correctness Prediction via Fine-tuning Pre-trained Models\", \"authors\": \"Quanjun Zhang and Chunrong Fang and Weisong Sun and Yan Liu and Tieke He and Xia...\", \"year\": \"2024\", \"venue\": \"IEEE Transactions on Software Engineering\"}, {\"key\": \"zhou2024llm4patch\", \"type\": \"article\", \"title\": \"Leveraging Large Language Model for Automatic Patch Correctness Assessment\", \"authors\": \"Xin Zhou and Bowen Xu and Kisub Kim and DongGyun Han and Hung Huu Nguyen and Tha...\", \"year\": \"2024\", \"venue\": \"IEEE Transactions on Software Engineering\"}, {\"key\": \"spiess2025calibration\", \"type\": \"inproceedings\", \"title\": \"Calibration and Correctness of Language Models for Code\", \"authors\": \"Claudio Spiess and David Gros and others\", \"year\": \"2025\", \"venue\": \"Proceedings of the 47th IEEE/ACM International Conference on Software Engineerin...\"}, {\"key\": \"foster2025mutation\", \"type\": \"inproceedings\", \"title\": \"Mutation-Guided LLM-based Test Generation at Meta\", \"authors\": \"Christopher Foster and Abhishek Gulati and Mark Harman and Inna Harper and Ke Ma...\", \"year\": \"2025\", \"venue\": \"Proceedings of the ACM International Conference on the Foundations of Software E...\"}, {\"key\": \"widyasari2024fusefl\", \"type\": \"inproceedings\", \"title\": \"Demystifying Faulty Code: Step-by-Step Reasoning for Explainable Fault Localization\", \"authors\": \"Ratnadira Widyasari and Jia Wei Ang and Truong Giang Nguyen and Neil Sharma and ...\", \"year\": \"2024\", \"venue\": \"Proceedings of the IEEE International Conference on Software Analysis, Evolution...\"}, {\"key\": \"huang2026tracecoder\", \"type\": \"inproceedings\", \"title\": \"TraceCoder: A Trace-Driven Multi-Agent Framework for Automated Debugging of LLM-Generated Code\", \"authors\": \"Jiangping Huang and Wenguang Ye and Weisong Sun and Jian Zhang and Mingyue Zhang...\", \"year\": \"2026\", \"venue\": \"Proceedings of the 48th IEEE/ACM International Conference on Software Engineerin...\"}, {\"key\": \"wang2025inspectcoder\", \"type\": \"article\", \"title\": \"InspectCoder: Dynamic Analysis-Enabled Self Repair through Interactive LLM-Debugger Collaboration\", \"authors\": \"Yunkun Wang and Yue Zhang and Guochang Li and Chen Zhi and Binhua Li and Fei Hua...\", \"year\": \"2025\", \"venue\": \"arXiv preprint arXiv:2510.18327\"}, {\"key\": \"haque2025traces\", \"type\": \"inproceedings\", \"title\": \"Towards Effectively Leveraging Execution Traces for Program Repair with Code LLMs\", \"authors\": \"Mirazul Haque and Petr Babkin and Farima Farmahinifarahani and Manuela Veloso\", \"year\": \"2025\", \"venue\": \"KnowledgeNLP Workshop at ACL 2025\"}, {\"key\": \"yang2024generalization\", \"type\": \"inproceedings\", \"title\": \"Unveiling the Generalization Power of Fine-Tuned Large Language Models\", \"authors\": \"Haoran Yang and Yumeng Zhang and Jiaqi Xu and Hongyuan Lu and Pheng Ann Heng and...\", \"year\": \"2024\", \"venue\": \"Proceedings of the 2024 Conference of the North American Chapter of the Associat...\"}, {\"key\": \"tian2024debugbench\", \"type\": \"inproceedings\", \"title\": \"DebugBench: Evaluating Debugging Capability of Large Language Models\", \"authors\": \"Runchu Tian and Yining Ye and Yujia Qin and Xin Cong and Yankai Lin and Yinxu Pa...\", \"year\": \"2024\", \"venue\": \"Findings of the Association for Computational Linguistics: ACL 2024\"}, {\"key\": \"abreu2007accuracy\", \"type\": \"article\", \"title\": \"On the Accuracy of Spectrum-based Fault Localization\", \"authors\": \"Rui Abreu and Peter Zoeteweij and Arjan J.C. van Gemund\", \"year\": \"2007\", \"venue\": \"Testing: Academic and Industrial Conference Practice and Research Techniques (MU...\"}, {\"key\": \"jones2002visualization\", \"type\": \"inproceedings\", \"title\": \"Visualization of Test Information to Assist Fault Localization\", \"authors\": \"James A. Jones and Mary Jean Harrold and John Stasko\", \"year\": \"2002\", \"venue\": \"Proceedings of the 24th International Conference on Software Engineering (ICSE)\"}, {\"key\": \"wong2014dstar\", \"type\": \"article\", \"title\": \"DStar: An Effective Spectrum-Based Fault Localization Technique\", \"authors\": \"W. Eric Wong and Vidroha Debroy and Ruizhi Gao and Yihao Li\", \"year\": \"2014\", \"venue\": \"Journal of Systems and Software\"}, {\"key\": \"kang2024autofl\", \"type\": \"inproceedings\", \"title\": \"AutoFL: Automated Fault Localization via Large Language Models\", \"authors\": \"Sungmin Kang and Gabin An and Shin Yoo\", \"year\": \"2024\", \"venue\": \"Proceedings of the 46th IEEE/ACM International Conference on Software Engineerin...\"}, {\"key\": \"qin2024agentfl\", \"type\": \"inproceedings\", \"title\": \"AgentFL: Scaling LLM-based Fault Localization to Project-Level Context\", \"authors\": \"Yihao Qin and Shangwen Wang and Yiling Lou and Jinhao Dong and Kaixin Wang and X...\", \"year\": \"2024\", \"venue\": \"Proceedings of the 39th IEEE/ACM International Conference on Automated Software ...\"}, {\"key\": \"widyasari2024llm4fl\", \"type\": \"inproceedings\", \"title\": \"LLM4FL: An LLM-based Fault Localization Integrated Debugging Framework for Automated Program Repair\", \"authors\": \"Ratnadira Widyasari and Gopi Krishnan Rajbahadur and Shin Hwei Tan and Xin Xia a...\", \"year\": \"2025\", \"venue\": \"Proceedings of the 47th IEEE/ACM International Conference on Software Engineerin...\"}, {\"key\": \"mukherjee2025llmfl\", \"type\": \"inproceedings\", \"title\": \"Can Large Language Models Localize Faults like Developers? A Comprehensive Study\", \"authors\": \"Soneya Binta Hossain and Nan Jiang and Qiang Zhou and Xiaopeng Li and Wen-Hao Ch...\", \"year\": \"2025\", \"venue\": \"Proceedings of the 47th IEEE/ACM International Conference on Software Engineerin...\"}, {\"key\": \"roziere2024code\", \"type\": \"article\", \"title\": \"Code Llama: Open Foundation Models for Code\", \"authors\": \"Baptiste Rozi\\\\`ere and Jonas Gehring and Fabian Gloeckle and Sten Sootla and Ita...\", \"year\": \"2024\", \"venue\": \"arXiv preprint arXiv:2308.12950\"}, {\"key\": \"dinella2022toga\", \"type\": \"inproceedings\", \"title\": \"TOGA: A Neural Method for Test Oracle Generation\", \"authors\": \"Elizabeth Dinella and Gabriel Ryan and Todd Mytkowicz and Shuvendu K. Lahiri\", \"year\": \"2022\", \"venue\": \"Proceedings of the 44th IEEE/ACM International Conference on Software Engineerin...\"}, {\"key\": \"steenhoek2024deepdfa\", \"type\": \"inproceedings\", \"title\": \"Dataflow Analysis-Inspired Deep Learning for Efficient Vulnerability Detection\", \"authors\": \"Benjamin Steenhoek and Hongyang Gao and Wei Le\", \"year\": \"2024\", \"venue\": \"Proceedings of the 46th IEEE/ACM International Conference on Software Engineerin...\"}, {\"key\": \"jimenez2024swebench\", \"type\": \"inproceedings\", \"title\": \"SWE-bench: Can Language Models Resolve Real-World GitHub Issues?\", \"authors\": \"Carlos E. Jimenez and John Yang and Alexander Wettig and Shunyu Yao and Kexin Pe...\", \"year\": \"2024\", \"venue\": \"Proceedings of the 12th International Conference on Learning Representations (IC...\"}, {\"key\": \"kadavath2022language\", \"type\": \"article\", \"title\": \"Language Models (Mostly) Know What They Know\", \"authors\": \"Saurav Kadavath and Tom Conerly and Amanda Askell and Tom Henighan and Dawn Drai...\", \"year\": \"2022\", \"venue\": \"arXiv preprint arXiv:2207.05221\"}, {\"key\": \"kamei2013large\", \"type\": \"article\", \"title\": \"A Large-Scale Empirical Study of Just-in-Time Quality Assurance\", \"authors\": \"Yasutaka Kamei and Emad Shihab and Bram Adams and Ahmed E. Hassan and Audris Moc...\", \"year\": \"2013\", \"venue\": \"IEEE Transactions on Software Engineering\"}, {\"key\": \"bouzenia2025repairagent\", \"type\": \"inproceedings\", \"title\": \"RepairAgent: An Autonomous, LLM-Based Agent for Program Repair\", \"authors\": \"Islem Bouzenia and Premkumar Devanbu and Michael Pradel\", \"year\": \"2025\", \"venue\": \"Proceedings of the 47th IEEE/ACM International Conference on Software Engineerin...\"}, {\"key\": \"chen2024selfdebug\", \"type\": \"inproceedings\", \"title\": \"Teaching Large Language Models to Self-Debug\", \"authors\": \"Xinyun Chen and Maxwell Lin and Nathanael Sch\\\\\\\"arli and Denny Zhou\", \"year\": \"2024\", \"venue\": \"Proceedings of the 12th International Conference on Learning Representations (IC...\"}, {\"key\": \"liu2023codeexecution\", \"type\": \"inproceedings\", \"title\": \"Code Execution with Pre-trained Language Models\", \"authors\": \"Chenxiao Liu and Shuai Lu and Weizhu Chen and Daxin Jiang and Alexey Svyatkovski...\", \"year\": \"2023\", \"venue\": \"Findings of the Association for Computational Linguistics: ACL 2023\"}, {\"key\": \"tian2020patchcorrectness\", \"type\": \"inproceedings\", \"title\": \"Evaluating Representation Learning of Code Changes for Predicting Patch Correctness in Program Repair\", \"authors\": \"Haoye Tian and Kui Liu and Abdoul Kader Kabor\\\\'e and Anil Koyuncu and Li Li and ...\", \"year\": \"2020\", \"venue\": \"Proceedings of the 35th IEEE/ACM International Conference on Automated Software ...\"}, {\"key\": \"watson2020atlas\", \"type\": \"inproceedings\", \"title\": \"On Learning Meaningful Assert Statements for Unit Test Cases\", \"authors\": \"Cody Watson and Michele Tufano and Kevin Moran and Gabriele Bavota and Denys Pos...\", \"year\": \"2020\", \"venue\": \"Proceedings of the ACM/IEEE 42nd International Conference on Software Engineerin...\"}, {\"key\": \"yu2022assertion\", \"type\": \"inproceedings\", \"title\": \"Automated Assertion Generation via Information Retrieval and Its Integration with Deep Learning\", \"authors\": \"Hao Yu and Yiling Lou and Ke Sun and Dezhi Ran and Tao Xie and Dan Hao and Ying ...\", \"year\": \"2022\", \"venue\": \"Proceedings of the 44th IEEE/ACM International Conference on Software Engineerin...\"}, {\"key\": \"nashid2023assertion\", \"type\": \"inproceedings\", \"title\": \"Revisiting and Improving Retrieval-Augmented Deep Assertion Generation\", \"authors\": \"Noor Nashid and Taha Shabani and Ali Mesbah\", \"year\": \"2023\", \"venue\": \"Proceedings of the 38th IEEE/ACM International Conference on Automated Software ...\"}, {\"key\": \"yadavally2024slicing\", \"type\": \"inproceedings\", \"title\": \"A Learning-Based Approach to Static Program Slicing\", \"authors\": \"Aashish Yadavally and Yi Li and Shaohua Wang and Tien N. Nguyen\", \"year\": \"2024\", \"venue\": \"Proceedings of the ACM on Programming Languages (OOPSLA)\"}, {\"key\": \"xia2024agentless\", \"type\": \"article\", \"title\": \"Agentless: Demystifying LLM-based Software Engineering Agents\", \"authors\": \"Chunqiu Steven Xia and Yinlin Deng and Soren Dunn and Lingming Zhang\", \"year\": \"2024\", \"venue\": \"arXiv preprint arXiv:2407.01489\"}, {\"key\": \"guo2017calibration\", \"type\": \"inproceedings\", \"title\": \"On Calibration of Modern Neural Networks\", \"authors\": \"Chuan Guo and Geoff Pleiss and Yu Sun and Kilian Q. Weinberger\", \"year\": \"2017\", \"venue\": \"Proceedings of the 34th International Conference on Machine Learning (ICML)\"}, {\"key\": \"geng2024calibration\", \"type\": \"inproceedings\", \"title\": \"A Survey of Confidence Estimation and Calibration in Large Language Models\", \"authors\": \"Jiahui Geng and Fengyu Cai and Yuxia Wang and Heinz Koeppl and Preslav Nakov and...\", \"year\": \"2024\", \"venue\": \"Proceedings of the 2024 Conference of the North American Chapter of the Associat...\"}, {\"key\": \"hoang2019deepjit\", \"type\": \"inproceedings\", \"title\": \"DeepJIT: An End-to-End Deep Learning Framework for Just-in-Time Defect Prediction\", \"authors\": \"Thong Hoang and Hoa Khanh Dam and Yasutaka Kamei and David Lo and Naoyasu Ubayas...\", \"year\": \"2019\", \"venue\": \"Proceedings of the 16th International Conference on Mining Software Repositories...\"}, {\"key\": \"hoang2020cc2vec\", \"type\": \"inproceedings\", \"title\": \"CC2Vec: Distributed Representations of Code Changes\", \"authors\": \"Thong Hoang and Hong Jin Kang and Julia Lawall and David Lo\", \"year\": \"2020\", \"venue\": \"Proceedings of the ACM/IEEE 42nd International Conference on Software Engineerin...\"}, {\"key\": \"pornprasit2021jitline\", \"type\": \"inproceedings\", \"title\": \"JITLine: A Simpler, Better, Faster, Finer-grained Just-In-Time Defect Prediction\", \"authors\": \"Chanathip Pornprasit and Chakkrit Tantithamthavorn\", \"year\": \"2021\", \"venue\": \"Proceedings of the 18th International Conference on Mining Software Repositories...\"}, {\"key\": \"bengio2009curriculum\", \"type\": \"inproceedings\", \"title\": \"Curriculum Learning\", \"authors\": \"Yoshua Bengio and J\\\\'er\\\\^ome Louradour and Ronan Collobert and Jason Weston\", \"year\": \"2009\", \"venue\": \"Proceedings of the 26th Annual International Conference on Machine Learning (ICM...\"}, {\"key\": \"sachdeva2024dataefficient\", \"type\": \"article\", \"title\": \"How to Train Data-Efficient LLMs\", \"authors\": \"Noveen Sachdeva and Benjamin Coleman and Wang-Cheng Kang and Jianmo Ni and Licha...\", \"year\": \"2024\", \"venue\": \"arXiv preprint arXiv:2402.09668\"}, {\"key\": \"swayamdipta2020cartography\", \"type\": \"inproceedings\", \"title\": \"Dataset Cartography: Mapping and Diagnosing Datasets with Training Dynamics\", \"authors\": \"Swabha Swayamdipta and Roy Schwartz and Nicholas Lourie and Yizhong Wang and Han...\", \"year\": \"2020\", \"venue\": \"Proceedings of the 2020 Conference on Empirical Methods in Natural Language Proc...\"}, {\"key\": \"xie2023doremi\", \"type\": \"inproceedings\", \"title\": \"DoReMi: Optimizing Data Mixtures Speeds Up Language Model Pretraining\", \"authors\": \"Sang Michael Xie and Hieu Pham and Xuanyi Dong and Nan Du and Hanxiao Liu and Yi...\", \"year\": \"2023\", \"venue\": \"Advances in Neural Information Processing Systems (NeurIPS)\"}], \"tex_citations\": [{\"key\": \"chen2025tracepile\", \"file\": \"introduction.tex\", \"line\": 3, \"command\": \"citep\"}, {\"key\": \"ding2024traced\", \"file\": \"introduction.tex\", \"line\": 3, \"command\": \"citep\"}, {\"key\": \"wang2025dcsh\", \"file\": \"introduction.tex\", \"line\": 3, \"command\": \"citep\"}, {\"key\": \"ni2024next\", \"file\": \"introduction.tex\", \"line\": 3, \"command\": \"citep\"}, {\"key\": \"wang2025dcsh\", \"file\": \"introduction.tex\", \"line\": 7, \"command\": \"citep\"}, {\"key\": \"chen2021evaluating\", \"file\": \"introduction.tex\", \"line\": 13, \"command\": \"citep\"}, {\"key\": \"austin2021program\", \"file\": \"introduction.tex\", \"line\": 13, \"command\": \"citep\"}, {\"key\": \"qwen2025coder\", \"file\": \"introduction.tex\", \"line\": 13, \"command\": \"citep\"}, {\"key\": \"roziere2024code\", \"file\": \"introduction.tex\", \"line\": 13, \"command\": \"citep\"}, {\"key\": \"deepseek2024coder\", \"file\": \"introduction.tex\", \"line\": 13, \"command\": \"citep\"}, {\"key\": \"chen2025tracepile\", \"file\": \"method.tex\", \"line\": 7, \"command\": \"citep\"}, {\"key\": \"gu2024cruxeval\", \"file\": \"method.tex\", \"line\": 7, \"command\": \"citep\"}, {\"key\": \"chen2021evaluating\", \"file\": \"method.tex\", \"line\": 12, \"command\": \"citep\"}, {\"key\": \"austin2021program\", \"file\": \"method.tex\", \"line\": 12, \"command\": \"citep\"}, {\"key\": \"qwen2025coder\", \"file\": \"method.tex\", \"line\": 38, \"command\": \"citep\"}, {\"key\": \"roziere2024code\", \"file\": \"method.tex\", \"line\": 38, \"command\": \"citep\"}, {\"key\": \"deepseek2024coder\", \"file\": \"method.tex\", \"line\": 38, \"command\": \"citep\"}, {\"key\": \"hu2022lora\", \"file\": \"method.tex\", \"line\": 39, \"command\": \"citep\"}, {\"key\": \"tian2024debugbench\", \"file\": \"experiments.tex\", \"line\": 173, \"command\": \"citep\"}, {\"key\": \"chen2025tracepile\", \"file\": \"related_work.tex\", \"line\": 4, \"command\": \"citep\"}, {\"key\": \"wang2025dcsh\", \"file\": \"related_work.tex\", \"line\": 4, \"command\": \"citet\"}, {\"key\": \"ni2024next\", \"file\": \"related_work.tex\", \"line\": 5, \"command\": \"citep\"}, {\"key\": \"eguchi2025etcot\", \"file\": \"related_work.tex\", \"line\": 5, \"command\": \"citep\"}, {\"key\": \"ferrando2025execute\", \"file\": \"related_work.tex\", \"line\": 5, \"command\": \"citet\"}, {\"key\": \"liu2023codeexecution\", \"file\": \"related_work.tex\", \"line\": 6, \"command\": \"citet\"}, {\"key\": \"chen2024selfdebug\", \"file\": \"related_work.tex\", \"line\": 6, \"command\": \"citet\"}, {\"key\": \"gu2024cruxeval\", \"file\": \"related_work.tex\", \"line\": 7, \"command\": \"citep\"}, {\"key\": \"xu2025cruxevalx\", \"file\": \"related_work.tex\", \"line\": 7, \"command\": \"citep\"}, {\"key\": \"ding2024traced\", \"file\": \"related_work.tex\", \"line\": 11, \"command\": \"citep\"}, {\"key\": \"steenhoek2024deepdfa\", \"file\": \"related_work.tex\", \"line\": 11, \"command\": \"citep\"}, {\"key\": \"yadavally2024slicing\", \"file\": \"related_work.tex\", \"line\": 11, \"command\": \"citep\"}, {\"key\": \"tian2020patchcorrectness\", \"file\": \"related_work.tex\", \"line\": 12, \"command\": \"citet\"}, {\"key\": \"hoang2020cc2vec\", \"file\": \"related_work.tex\", \"line\": 12, \"command\": \"citep\"}, {\"key\": \"zhou2024llm4patch\", \"file\": \"related_work.tex\", \"line\": 12, \"command\": \"citep\"}, {\"key\": \"appt2024\", \"file\": \"related_work.tex\", \"line\": 12, \"command\": \"citep\"}, {\"key\": \"watson2020atlas\", \"file\": \"related_work.tex\", \"line\": 13, \"command\": \"citep\"}, {\"key\": \"yu2022assertion\", \"file\": \"related_work.tex\", \"line\": 13, \"command\": \"citep\"}, {\"key\": \"nashid2023assertion\", \"file\": \"related_work.tex\", \"line\": 13, \"command\": \"citep\"}, {\"key\": \"dinella2022toga\", \"file\": \"related_work.tex\", \"line\": 13, \"command\": \"citep\"}, {\"key\": \"widyasari2024fusefl\", \"file\": \"related_work.tex\", \"line\": 13, \"command\": \"citep\"}, {\"key\": \"foster2025mutation\", \"file\": \"related_work.tex\", \"line\": 13, \"command\": \"citet\"}, {\"key\": \"abreu2007accuracy\", \"file\": \"related_work.tex\", \"line\": 17, \"command\": \"citep\"}, {\"key\": \"jones2002visualization\", \"file\": \"related_work.tex\", \"line\": 17, \"command\": \"citep\"}, {\"key\": \"wong2014dstar\", \"file\": \"related_work.tex\", \"line\": 17, \"command\": \"citep\"}, {\"key\": \"kang2024autofl\", \"file\": \"related_work.tex\", \"line\": 17, \"command\": \"citep\"}, {\"key\": \"qin2024agentfl\", \"file\": \"related_work.tex\", \"line\": 17, \"command\": \"citep\"}, {\"key\": \"widyasari2024llm4fl\", \"file\": \"related_work.tex\", \"line\": 17, \"command\": \"citep\"}, {\"key\": \"mukherjee2025llmfl\", \"file\": \"related_work.tex\", \"line\": 17, \"command\": \"citep\"}, {\"key\": \"huang2026tracecoder\", \"file\": \"related_work.tex\", \"line\": 21, \"command\": \"citep\"}, {\"key\": \"wang2025inspectcoder\", \"file\": \"related_work.tex\", \"line\": 21, \"command\": \"citep\"}, {\"key\": \"bouzenia2025repairagent\", \"file\": \"related_work.tex\", \"line\": 21, \"command\": \"citep\"}, {\"key\": \"xia2024agentless\", \"file\": \"related_work.tex\", \"line\": 21, \"command\": \"citep\"}, {\"key\": \"haque2025traces\", \"file\": \"related_work.tex\", \"line\": 22, \"command\": \"citet\"}, {\"key\": \"jimenez2024swebench\", \"file\": \"related_work.tex\", \"line\": 22, \"command\": \"citep\"}, {\"key\": \"guo2017calibration\", \"file\": \"related_work.tex\", \"line\": 26, \"command\": \"citep\"}, {\"key\": \"kadavath2022language\", \"file\": \"related_work.tex\", \"line\": 26, \"command\": \"citep\"}, {\"key\": \"geng2024calibration\", \"file\": \"related_work.tex\", \"line\": 26, \"command\": \"citep\"}, {\"key\": \"spiess2025calibration\", \"file\": \"related_work.tex\", \"line\": 26, \"command\": \"citep\"}, {\"key\": \"kamei2013large\", \"file\": \"related_work.tex\", \"line\": 27, \"command\": \"citep\"}, {\"key\": \"hoang2019deepjit\", \"file\": \"related_work.tex\", \"line\": 27, \"command\": \"citep\"}, {\"key\": \"pornprasit2021jitline\", \"file\": \"related_work.tex\", \"line\": 27, \"command\": \"citep\"}, {\"key\": \"bengio2009curriculum\", \"file\": \"related_work.tex\", \"line\": 30, \"command\": \"citep\"}, {\"key\": \"swayamdipta2020cartography\", \"file\": \"related_work.tex\", \"line\": 30, \"command\": \"citep\"}, {\"key\": \"sachdeva2024dataefficient\", \"file\": \"related_work.tex\", \"line\": 30, \"command\": \"citep\"}, {\"key\": \"xie2023doremi\", \"file\": \"related_work.tex\", \"line\": 30, \"command\": \"citep\"}, {\"key\": \"hu2022lora\", \"file\": \"appendix.tex\", \"line\": 37, \"command\": \"citep\"}, {\"key\": \"spiess2025calibration\", \"file\": \"appendix.tex\", \"line\": 509, \"command\": \"citep\"}, {\"key\": \"tian2024debugbench\", \"file\": \"appendix.tex\", \"line\": 588, \"command\": \"citep\"}, {\"key\": \"yang2024generalization\", \"file\": \"appendix.tex\", \"line\": 626, \"command\": \"citep\"}], \"online_verification\": [{\"key\": \"chen2025tracepile\", \"title\": \"Chain of Execution Supervision Promotes General Reasoning in Large Language Models\", \"status\": \"not_found\", \"confidence\": 0.452, \"matched_title\": \"A Survey of Large Language Models\", \"matched_year\": \"\", \"mismatch_fields\": [], \"note\": \"best match similarity 0.45 below threshold 0.82\"}, {\"key\": \"ding2024traced\", \"title\": \"TRACED: Execution-aware Pre-training for Source Code\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"TRACED: Execution-aware Pre-training for Source Code\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"chen2021evaluating\", \"title\": \"Evaluating Large Language Models Trained on Code\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Evaluating Large Language Models Trained on Code\", \"matched_year\": \"2021\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"austin2021program\", \"title\": \"Program Synthesis with Large Language Models\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Program Synthesis with Large Language Models\", \"matched_year\": \"2021\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"gu2024cruxeval\", \"title\": \"CRUXEval: A Benchmark for Code Reasoning, Understanding and Execution\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"CRUXEval: A Benchmark for Code Reasoning, Understanding and Execution\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"hu2022lora\", \"title\": \"LoRA: Low-Rank Adaptation of Large Language Models\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"LoRA: Low-Rank Adaptation of Large Language Models\", \"matched_year\": \"2021\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"qwen2025coder\", \"title\": \"Qwen2.5-Coder Technical Report\", \"status\": \"mismatch\", \"confidence\": 1.0, \"matched_title\": \"Qwen2.5-Coder Technical Report\", \"matched_year\": \"2024\", \"mismatch_fields\": [\"first_author: bib=team vs api=hui\"], \"note\": \"\"}, {\"key\": \"deepseek2024coder\", \"title\": \"DeepSeek-Coder: When the Large Language Model Meets Programming -- The Rise of Code Intelligence\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"DeepSeek-Coder: When the Large Language Model Meets Programming -- The Rise of Code Intelligence\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"wang2025dcsh\", \"title\": \"Do Code Semantics Help? A Comprehensive Study on Execution Trace-Based Information for Code Large Language Models\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Do Code Semantics Help? A Comprehensive Study on Execution Trace-Based Information for Code Large Language Models\", \"matched_year\": \"2025\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"ni2024next\", \"title\": \"NExT: Teaching Large Language Models to Reason about Code Execution\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"NExT: Teaching Large Language Models to Reason about Code Execution\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"eguchi2025etcot\", \"title\": \"Making LLMs Program Interpreters via Execution Trace Chain of Thought\", \"status\": \"not_found\", \"confidence\": 0.203, \"matched_title\": \"From ChatGPT to ThreatGPT: Impact of Generative AI in Cybersecurity and Privacy\", \"matched_year\": \"\", \"mismatch_fields\": [], \"note\": \"best match similarity 0.20 below threshold 0.82\"}, {\"key\": \"ferrando2025execute\", \"title\": \"What I Cannot Execute, I Do Not Understand: Training and Evaluating LLMs on Program Execution Traces\", \"status\": \"not_found\", \"confidence\": 0.199, \"matched_title\": \"Sparks of Artificial General Intelligence: Early experiments with GPT-4\", \"matched_year\": \"\", \"mismatch_fields\": [], \"note\": \"best match similarity 0.20 below threshold 0.82\"}, {\"key\": \"xu2025cruxevalx\", \"title\": \"CRUXEval-X: A Benchmark for Multilingual Code Reasoning, Understanding and Execution\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"CRUXEVAL-X: A Benchmark for Multilingual Code Reasoning, Understanding and Execution\", \"matched_year\": \"2025\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"appt2024\", \"title\": \"APPT: Boosting Automated Patch Correctness Prediction via Fine-tuning Pre-trained Models\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"APPT: Boosting Automated Patch Correctness Prediction via Fine-Tuning Pre-Trained Models\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"zhou2024llm4patch\", \"title\": \"Leveraging Large Language Model for Automatic Patch Correctness Assessment\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Leveraging Large Language Model for Automatic Patch Correctness Assessment\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"spiess2025calibration\", \"title\": \"Calibration and Correctness of Language Models for Code\", \"status\": \"mismatch\", \"confidence\": 1.0, \"matched_title\": \"Calibration and Correctness of Language Models for Code\", \"matched_year\": \"2025\", \"mismatch_fields\": [\"first_author: bib=spiess vs api=spieß\"], \"note\": \"\"}, {\"key\": \"foster2025mutation\", \"title\": \"Mutation-Guided LLM-based Test Generation at Meta\", \"status\": \"mismatch\", \"confidence\": 1.0, \"matched_title\": \"Mutation-Guided LLM-based Test Generation at Meta\", \"matched_year\": \"2025\", \"mismatch_fields\": [\"first_author: bib=foster vs api=harman\"], \"note\": \"\"}, {\"key\": \"widyasari2024fusefl\", \"title\": \"Demystifying Faulty Code: Step-by-Step Reasoning for Explainable Fault Localization\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Demystifying Faulty Code: Step-by-Step Reasoning for Explainable Fault Localization\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"huang2026tracecoder\", \"title\": \"TraceCoder: A Trace-Driven Multi-Agent Framework for Automated Debugging of LLM-Generated Code\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"TraceCoder: A Trace-Driven Multi-Agent Framework for Automated Debugging of LLM-Generated Code\", \"matched_year\": \"2026\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"wang2025inspectcoder\", \"title\": \"InspectCoder: Dynamic Analysis-Enabled Self Repair through Interactive LLM-Debugger Collaboration\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"InspectCoder: Dynamic Analysis-Enabled Self Repair through interactive LLM-Debugger Collaboration\", \"matched_year\": \"2025\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"haque2025traces\", \"title\": \"Towards Effectively Leveraging Execution Traces for Program Repair with Code LLMs\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Towards Effectively Leveraging Execution Traces for Program Repair with Code LLMs\", \"matched_year\": \"2025\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"yang2024generalization\", \"title\": \"Unveiling the Generalization Power of Fine-Tuned Large Language Models\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Unveiling the Generalization Power of Fine-Tuned Large Language Models\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"tian2024debugbench\", \"title\": \"DebugBench: Evaluating Debugging Capability of Large Language Models\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"DebugBench: Evaluating Debugging Capability of Large Language Models\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"abreu2007accuracy\", \"title\": \"On the Accuracy of Spectrum-based Fault Localization\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"On the Accuracy of Spectrum-based Fault Localization\", \"matched_year\": \"2007\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"jones2002visualization\", \"title\": \"Visualization of Test Information to Assist Fault Localization\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Visualization of test information to assist fault localization\", \"matched_year\": \"2002\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"wong2014dstar\", \"title\": \"DStar: An Effective Spectrum-Based Fault Localization Technique\", \"status\": \"not_found\", \"confidence\": 0.561, \"matched_title\": \"MSFL: A Model for Fault Localization Using Mutation-Spectra Technique\", \"matched_year\": \"\", \"mismatch_fields\": [], \"note\": \"best match similarity 0.56 below threshold 0.82\"}, {\"key\": \"kang2024autofl\", \"title\": \"AutoFL: Automated Fault Localization via Large Language Models\", \"status\": \"not_found\", \"confidence\": 0.45, \"matched_title\": \"A Survey on Large Language Models for Software Engineering\", \"matched_year\": \"\", \"mismatch_fields\": [], \"note\": \"best match similarity 0.45 below threshold 0.82\"}, {\"key\": \"qin2024agentfl\", \"title\": \"AgentFL: Scaling LLM-based Fault Localization to Project-Level Context\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"AgentFL: Scaling LLM-based Fault Localization to Project-Level Context\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"widyasari2024llm4fl\", \"title\": \"LLM4FL: An LLM-based Fault Localization Integrated Debugging Framework for Automated Program Repair\", \"status\": \"not_found\", \"confidence\": 0.448, \"matched_title\": \"A Multi-Agent Approach to Fault Localization via Graph-Based Retrieval and Reflexion\", \"matched_year\": \"\", \"mismatch_fields\": [], \"note\": \"best match similarity 0.45 below threshold 0.82\"}, {\"key\": \"mukherjee2025llmfl\", \"title\": \"Can Large Language Models Localize Faults like Developers? A Comprehensive Study\", \"status\": \"not_found\", \"confidence\": 0.186, \"matched_title\": \"Internet of Things (IoT): A vision, architectural elements, and future directions\", \"matched_year\": \"\", \"mismatch_fields\": [], \"note\": \"best match similarity 0.19 below threshold 0.82\"}, {\"key\": \"roziere2024code\", \"title\": \"Code Llama: Open Foundation Models for Code\", \"status\": \"mismatch\", \"confidence\": 1.0, \"matched_title\": \"Code Llama: Open Foundation Models for Code\", \"matched_year\": \"2023\", \"mismatch_fields\": [\"first_author: bib=rozi\\\\`ere vs api=rozière\"], \"note\": \"\"}, {\"key\": \"dinella2022toga\", \"title\": \"TOGA: A Neural Method for Test Oracle Generation\", \"status\": \"not_found\", \"confidence\": 0.623, \"matched_title\": \"TOGLL: Correct and Strong Test Oracle Generation with LLMs\", \"matched_year\": \"\", \"mismatch_fields\": [], \"note\": \"best match similarity 0.62 below threshold 0.82\"}, {\"key\": \"steenhoek2024deepdfa\", \"title\": \"Dataflow Analysis-Inspired Deep Learning for Efficient Vulnerability Detection\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Dataflow Analysis-Inspired Deep Learning for Efficient Vulnerability Detection\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"jimenez2024swebench\", \"title\": \"SWE-bench: Can Language Models Resolve Real-World GitHub Issues?\", \"status\": \"mismatch\", \"confidence\": 1.0, \"matched_title\": \"SWE-bench: Can Language Models Resolve Real-World GitHub Issues?\", \"matched_year\": \"2023\", \"mismatch_fields\": [\"first_author: bib=jimenez vs api=jimenez-gomez\"], \"note\": \"\"}, {\"key\": \"kadavath2022language\", \"title\": \"Language Models (Mostly) Know What They Know\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Language Models (Mostly) Know What They Know\", \"matched_year\": \"2022\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"kamei2013large\", \"title\": \"A Large-Scale Empirical Study of Just-in-Time Quality Assurance\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"A large-scale empirical study of just-in-time quality assurance\", \"matched_year\": \"2012\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"bouzenia2025repairagent\", \"title\": \"RepairAgent: An Autonomous, LLM-Based Agent for Program Repair\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"RepairAgent: An Autonomous, LLM-Based Agent for Program Repair\", \"matched_year\": \"2025\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"chen2024selfdebug\", \"title\": \"Teaching Large Language Models to Self-Debug\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Teaching Large Language Models to Self-Debug\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"liu2023codeexecution\", \"title\": \"Code Execution with Pre-trained Language Models\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Code Execution with Pre-trained Language Models\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"tian2020patchcorrectness\", \"title\": \"Evaluating Representation Learning of Code Changes for Predicting Patch Correctness in Program Repair\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Evaluating representation learning of code changes for predicting patch correctness in program repair\", \"matched_year\": \"2020\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"watson2020atlas\", \"title\": \"On Learning Meaningful Assert Statements for Unit Test Cases\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"On learning meaningful assert statements for unit test cases\", \"matched_year\": \"2020\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"yu2022assertion\", \"title\": \"Automated Assertion Generation via Information Retrieval and Its Integration with Deep Learning\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Automated assertion generation via information retrieval and its integration with deep learning\", \"matched_year\": \"2022\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"nashid2023assertion\", \"title\": \"Revisiting and Improving Retrieval-Augmented Deep Assertion Generation\", \"status\": \"mismatch\", \"confidence\": 1.0, \"matched_title\": \"Revisiting and Improving Retrieval-Augmented Deep Assertion Generation\", \"matched_year\": \"2023\", \"mismatch_fields\": [\"first_author: bib=nashid vs api=sun\"], \"note\": \"\"}, {\"key\": \"yadavally2024slicing\", \"title\": \"A Learning-Based Approach to Static Program Slicing\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"A Learning-Based Approach to Static Program Slicing\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"xia2024agentless\", \"title\": \"Agentless: Demystifying LLM-based Software Engineering Agents\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Agentless: Demystifying LLM-based Software Engineering Agents\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"guo2017calibration\", \"title\": \"On Calibration of Modern Neural Networks\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"On Calibration of Modern Neural Networks\", \"matched_year\": \"2017\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"geng2024calibration\", \"title\": \"A Survey of Confidence Estimation and Calibration in Large Language Models\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"A Survey of Confidence Estimation and Calibration in Large Language Models\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"hoang2019deepjit\", \"title\": \"DeepJIT: An End-to-End Deep Learning Framework for Just-in-Time Defect Prediction\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"DeepJIT: An End-to-End Deep Learning Framework for Just-in-Time Defect Prediction\", \"matched_year\": \"2019\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"hoang2020cc2vec\", \"title\": \"CC2Vec: Distributed Representations of Code Changes\", \"status\": \"mismatch\", \"confidence\": 1.0, \"matched_title\": \"CC2Vec: Distributed Representations of Code Changes\", \"matched_year\": \"2020\", \"mismatch_fields\": [\"first_author: bib=hoang vs api=thong\"], \"note\": \"\"}, {\"key\": \"pornprasit2021jitline\", \"title\": \"JITLine: A Simpler, Better, Faster, Finer-grained Just-In-Time Defect Prediction\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"JITLine: A Simpler, Better, Faster, Finer-grained Just-In-Time Defect Prediction\", \"matched_year\": \"2021\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"bengio2009curriculum\", \"title\": \"Curriculum Learning\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Curriculum learning\", \"matched_year\": \"2009\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"sachdeva2024dataefficient\", \"title\": \"How to Train Data-Efficient LLMs\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"How to Train Data-Efficient LLMs\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"swayamdipta2020cartography\", \"title\": \"Dataset Cartography: Mapping and Diagnosing Datasets with Training Dynamics\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Dataset Cartography: Mapping and Diagnosing Datasets with Training Dynamics\", \"matched_year\": \"2020\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"xie2023doremi\", \"title\": \"DoReMi: Optimizing Data Mixtures Speeds Up Language Model Pretraining\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"DoReMi: Optimizing Data Mixtures Speeds Up Language Model Pretraining\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}]}, \"error\": null, \"metadata\": {}}"
    }
  },
  "sourceToolAssistantUUID": "311b3d5f-5139-4484-9357-54b46b4571d0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/.claude/sessions/review_reviewer_1_7624f219",
  "sessionId": "98d2b939-6454-4d7d-877f-2c64a5a37485",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 61 · 2026-05-19T12:53:25.529Z_

<details><summary>↩ Tool result · `toolu_01DW2LNGv67YQ8Af1F3cwCzW`</summary>

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
18	\textit{Yes.} A dedicated Limitations section discusses: single-dataset scope (with DebugBench cross-validation), four models across three architecture families (1.5B--13B), seed-dependent variance on DeepSeek, the invalidated full\_trace run, generator--evaluator overlap, self-familiarity bias, error distribution assumptions, and task scope limited to verdict prediction.
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
48	\item Total compute: ${\sim}$320 GPU-hours across all conditions, models, seeds, and iterative refinements (${\sim}$170h for successful experiments; individual runs 0.5--2.2h). See Appendix~B for per-condition wall-clock times.
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
  "parentUuid": "b79d75da-06af-4ca0-87a1-b4ca916628db",
  "isSidechain": false,
  "promptId": "e3f72197-8c21-47a9-99b8-7cd49faae750",
  "type": "user",
  "uuid": "ca0dcc09-5a4b-4527-88a5-95f4aefa1b29",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/arr_checklist.tex",
      "content": "\\documentclass[11pt,a4paper]{article}\n\\usepackage[review]{acl}\n\\usepackage{times,latexsym}\n\\usepackage{booktabs}\n\n\\title{ARR Reproducibility Checklist\\\\(Supplementary Material)}\n\\author{Anonymous ACL submission}\n\n\\begin{document}\n\\maketitle\n\n\\section*{Responsible NLP Research Checklist}\n\n\\subsection*{A. Limitations and Risks}\n\n\\begin{enumerate}\n\\item \\textbf{Did you discuss the limitations of your work?} \\\\\n\\textit{Yes.} A dedicated Limitations section discusses: single-dataset scope (with DebugBench cross-validation), four models across three architecture families (1.5B--13B), seed-dependent variance on DeepSeek, the invalidated full\\_trace run, generator--evaluator overlap, self-familiarity bias, error distribution assumptions, and task scope limited to verdict prediction.\n\n\\item \\textbf{Did you discuss any potential risks of your work?} \\\\\n\\textit{Yes.} The Ethics Statement notes that the work uses public benchmarks, involves no human subjects, and has minimal environmental impact. Verdict prediction is a developer-facing tool with no direct end-user impact.\n\\end{enumerate}\n\n\\subsection*{B. Did you use or create scientific artifacts?}\n\n\\begin{enumerate}\n\\item \\textbf{Did you cite the creators of artifacts you used?} \\\\\n\\textit{Yes.} HumanEval \\cite{chen2021evaluating}, MBPP-sanitized \\cite{austin2021program}, DebugBench \\cite{tian2024debugbench}, Qwen-2.5-Coder-7B/1.5B-Instruct \\cite{qwen2025coder}, CodeLlama-13B-Instruct \\cite{roziere2024code}, DeepSeek-Coder-6.7B-Instruct \\cite{deepseek2024coder}, LoRA \\cite{hu2022lora}, and TRL SFTTrainer are all cited.\n\n\\item \\textbf{Did you discuss the license or terms for use and/or distribution of any artifacts?} \\\\\n\\textit{Partial.} All base models and datasets are publicly available. HumanEval is released under MIT license; MBPP under CC-BY-4.0; DebugBench under MIT. Model licenses: Qwen-2.5-Coder under Apache 2.0; DeepSeek-Coder under the DeepSeek License.\n\n\\item \\textbf{Did you discuss if your use of existing artifacts was consistent with their intended use?} \\\\\n\\textit{Yes.} HumanEval and MBPP are standard code generation benchmarks; we use their canonical test cases for verdict evaluation, consistent with their evaluation purpose. DebugBench is designed for debugging evaluation.\n\n\\item \\textbf{Did you discuss the steps taken to check whether the data contains any information that names or uniquely identifies individual people or offensive content?} \\\\\n\\textit{N/A.} All datasets contain only programming problems and solutions with no personal information.\n\\end{enumerate}\n\n\\subsection*{C. Computational Experiments}\n\n\\begin{enumerate}\n\\item \\textbf{Did you report the number of parameters in the models used, the total computational budget, and computing infrastructure?} \\\\\n\\textit{Yes.}\n\\begin{itemize}\n\\item Models: Qwen-2.5-Coder-7B/1.5B-Instruct (7B/1.5B parameters), CodeLlama-13B-Instruct (13B parameters), DeepSeek-Coder-6.7B-Instruct (6.7B parameters). Only LoRA adapters are trained (rank=16, $\\alpha$=32, targeting all linear layers).\n\\item Hardware: 2$\\times$ RTX PRO 6000 Blackwell (${\\sim}$96\\,GB VRAM each); each experiment uses a single GPU.\n\\item Total compute: ${\\sim}$320 GPU-hours across all conditions, models, seeds, and iterative refinements (${\\sim}$170h for successful experiments; individual runs 0.5--2.2h). See Appendix~B for per-condition wall-clock times.\n\\end{itemize}\n\n\\item \\textbf{Did you report all hyperparameters?} \\\\\n\\textit{Yes.} Appendix~B (Table~5) reports: LoRA rank (16), alpha (32), dropout (0.05), target modules (all linear layers), epochs (3), per-device batch size (4), gradient accumulation steps (8), effective batch size (32), learning rate ($2 \\times 10^{-4}$), LR scheduler (linear decay), warmup ratio (0.1), weight decay (0.01), max sequence length (2,048 tokens).\n\n\\item \\textbf{Did you report descriptive statistics about your results?} \\\\\n\\textit{Yes.} All accuracy values include Wilson 95\\% confidence intervals. Pairwise comparisons use paired bootstrap resampling ($B{=}10{,}000$, seed=42) with reported $p$-values. We report multi-seed results (seeds 42, 123, 456) for the exception\\_only condition; other conditions report single-seed results. Standard deviations are provided where multiple seeds are available.\n\n\\item \\textbf{If you used existing packages, did you report the implementation, model, and their versions?} \\\\\n\\textit{Yes.} HuggingFace TRL SFTTrainer with LoRA via PEFT. Base model identifiers: \\texttt{Qwen/Qwen2.5-Coder-7B-Instruct} and \\texttt{deepseek-ai/deepseek-coder-6.7b-instruct}.\n\\end{enumerate}\n\n\\subsection*{D. Human Annotations}\n\n\\begin{enumerate}\n\\item \\textbf{Did you use human annotators?} \\\\\n\\textit{No.} All labels (pass/fail) are derived from automated test execution. No human annotation was involved.\n\\end{enumerate}\n\n\\subsection*{E. Data and Code Availability}\n\n\\begin{itemize}\n\\item \\textbf{Code}: Training, evaluation, and trace preprocessing scripts will be released upon acceptance.\n\\item \\textbf{Data}: Execution traces, VOTA-compressed traces, and train/test splits will be released. Raw traces are generated deterministically from publicly available benchmarks using Python \\texttt{sys.settrace}.\n\\item \\textbf{Models}: LoRA adapters for all conditions will be released on HuggingFace.\n\\end{itemize}\n\n\\subsection*{F. Reproducibility Summary}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{lc}\n\\toprule\n\\textbf{Item} & \\textbf{Status} \\\\\n\\midrule\nAll hyperparameters reported & Yes \\\\\nRandom seeds specified & Yes (42, 123, 456) \\\\\nError bars / CIs reported & Yes (Wilson 95\\% CI) \\\\\nStatistical tests reported & Yes (bootstrap, McNemar) \\\\\nComputing infrastructure reported & Yes \\\\\nTraining time reported & Yes \\\\\nCode release planned & Yes \\\\\nData release planned & Yes \\\\\nModel release planned & Yes \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\bibliography{references}\n\n\\end{document}\n",
      "numLines": 101,
      "startLine": 1,
      "totalLines": 101
    }
  },
  "sourceToolAssistantUUID": "b79d75da-06af-4ca0-87a1-b4ca916628db",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/.claude/sessions/review_reviewer_1_7624f219",
  "sessionId": "98d2b939-6454-4d7d-877f-2c64a5a37485",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 62 · 2026-05-19T12:53:25.535Z_

```json
{
  "parentUuid": "ca0dcc09-5a4b-4527-88a5-95f4aefa1b29",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "4da49bdf-71b1-4758-9f73-7c2c93cf16f2",
  "timestamp": "2026-05-19T12:53:25.535Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/.claude/sessions/review_reviewer_1_7624f219",
  "sessionId": "98d2b939-6454-4d7d-877f-2c64a5a37485",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 63_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[Round 1 审稿请求]: 你是 Reviewer 1，负责 **方法严谨性 + 实验有效性**。  ## 论文信息 - **标题**: \"Exception Events Are All You Need: Component Ablation for Trace-Based Verdict Prediction\" - **Venue**: EMNLP 2026 (ARR May 2026)…",
  "leafUuid": "4da49bdf-71b1-4758-9f73-7c2c93cf16f2",
  "sessionId": "98d2b939-6454-4d7d-877f-2c64a5a37485"
}
```

---

### Runtime record

_source line 64_

```json
{
  "type": "ai-title",
  "aiTitle": "Review trace-based verdict prediction paper methodology",
  "sessionId": "98d2b939-6454-4d7d-877f-2c64a5a37485"
}
```

---

### Assistant

_source line 65 · 2026-05-19T12:53:29.013Z_

<details><summary>Logged reasoning block</summary>

```text
Now let me fetch the exact ARR review form to get the scoring scales.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4da49bdf-71b1-4758-9f73-7c2c93cf16f2",
  "isSidechain": false,
  "requestId": "req_011CbBxfGcbR5w3GiLibsaVV",
  "type": "assistant",
  "uuid": "bde12862-082e-48bc-b739-a0fcfd8bde4a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/.claude/sessions/review_reviewer_1_7624f219",
  "sessionId": "98d2b939-6454-4d7d-877f-2c64a5a37485",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XK4Z5E6c5KHyfSMdJY9LAT",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 37928,
      "cache_read_input_tokens": 45388,
      "output_tokens": 203,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 37928,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 203,
          "cache_read_input_tokens": 45388,
          "cache_creation_input_tokens": 37928,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 37928
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

_source line 66 · 2026-05-19T12:53:29.528Z_

获取 ARR review form 评分量表详情。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bde12862-082e-48bc-b739-a0fcfd8bde4a",
  "isSidechain": false,
  "requestId": "req_011CbBxfGcbR5w3GiLibsaVV",
  "type": "assistant",
  "uuid": "3b8bbcac-4b37-4e94-882e-314bf1571b22",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/.claude/sessions/review_reviewer_1_7624f219",
  "sessionId": "98d2b939-6454-4d7d-877f-2c64a5a37485",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XK4Z5E6c5KHyfSMdJY9LAT",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 37928,
      "cache_read_input_tokens": 45388,
      "output_tokens": 203,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 37928,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 203,
          "cache_read_input_tokens": 45388,
          "cache_creation_input_tokens": 37928,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 37928
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

_source line 67 · 2026-05-19T12:53:32.539Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_011f1LuZAzSy7FAA9p35FMDA`</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract the EXACT scoring scales and descriptions for ALL review form fields: soundness, excitement, overall assessment, confidence, and any other scoring dimensions. I need the complete text for each score level (e.g., 5=..., 4=..., 3=..., 2=..., 1=...). Return ALL details verbatim."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3b8bbcac-4b37-4e94-882e-314bf1571b22",
  "isSidechain": false,
  "requestId": "req_011CbBxfGcbR5w3GiLibsaVV",
  "type": "assistant",
  "uuid": "1d3def5d-ee06-4c92-87ac-3284f72ca36c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/.claude/sessions/review_reviewer_1_7624f219",
  "sessionId": "98d2b939-6454-4d7d-877f-2c64a5a37485",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XK4Z5E6c5KHyfSMdJY9LAT",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 37928,
      "cache_read_input_tokens": 45388,
      "output_tokens": 203,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 37928,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 203,
          "cache_read_input_tokens": 45388,
          "cache_creation_input_tokens": 37928,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 37928
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

_source line 68 · 2026-05-19T12:53:43.399Z_

<details><summary>↩ Tool result · `toolu_011f1LuZAzSy7FAA9p35FMDA`</summary>

```text
# ACL Rolling Review Form - Scoring Scales

## Reviewer Confidence
- **5:** "Positive that my evaluation is correct. I read the paper very carefully and am familiar with related work."
- **4:** "Quite sure. I tried to check the important points carefully. It's unlikely, though conceivable, that I missed something that should affect my ratings."
- **3:** "Pretty sure, but there's a chance I missed something. Although I have a good feel for this area in general, I did not carefully check the paper's details, e.g., the math or experimental design."
- **2:** "Willing to defend my evaluation, but it is fairly likely that I missed some details, didn't understand some central points, or can't be sure about the novelty of the work."
- **1:** "Not my area, or paper is very hard to understand. My evaluation is just an educated guess."

## Soundness
- **5:** "Excellent: This study is one of the most thorough I have seen, given its type."
- **4:** "Strong: This study provides sufficient support for all of its claims. Some extra experiments could be nice, but not essential."
- **3:** "Acceptable: This study provides sufficient support for its main claims. Some minor points may need extra support or details."
- **2:** "Poor: Some of the main claims are not sufficiently supported. There are major technical/methodological problems."
- **1:** "Major Issues: This study is not yet sufficiently thorough to warrant publication or is not relevant to ACL."

## Excitement
- **5:** "Highly Exciting: I would recommend this paper to others and/or attend its presentation in a conference."
- **4:** "Exciting: I would mention this paper to others and/or make an effort to attend its presentation in a conference."
- **3:** "Interesting: I might mention some points of this paper to others and/or attend its presentation if there's time."
- **2:** "Potentially Interesting: this paper does not resonate with me, but it might with others in the *ACL community."
- **1:** "Not Exciting: this paper does not resonate with me, and I don't think it would with others in the *ACL community."

## Overall Assessment
- **5:** "Consider for Award: I think this paper could be considered for an outstanding paper award at an *ACL conference (up to top 2.5% papers)."
- **4.5:** Borderline Award
- **4:** "Conference: I think this paper could be accepted to an *ACL conference."
- **3.5:** Borderline Conference
- **3:** "Findings: I think this paper could be accepted to the Findings of the ACL."
- **2.5:** Borderline Findings
- **2:** "Resubmit next cycle: I think this paper needs substantial revisions that can be completed by the next ARR cycle."
- **1.5:** "Resubmit after next cycle: I think this paper needs substantial revisions that cannot be completed by the next ARR cycle."
- **1:** "Do not resubmit: This paper has to be fully redone, or it is not relevant to the *ACL community."

## Reproducibility
- **5:** "They could easily reproduce the results."
- **4:** "They could mostly reproduce the results, but there may be some variation because of sample variance or minor variations in their interpretation of the protocol or method."
- **3:** "They could reproduce the results with some difficulty. The settings of parameters are underspecified or subjectively determined, and/or the training/evaluation data are not widely available."
- **2:** "They would be hard pressed to reproduce the results: The contribution depends on data that are simply not available outside the author's institution or consortium and/or not enough details are provided."
- **1:** "They would not be able to reproduce the results here no matter how hard they tried."

## Datasets
- **5:** "Enabling: The newly released datasets should affect other people's choice of research or development projects to undertake."
- **4:** "Useful: I would recommend the new datasets to other researchers or developers for their ongoing work."
- **3:** "Potentially useful: Someone might find the new datasets useful for their work."
- **2:** "Documentary: The new datasets will be useful to study or replicate the reported research, although for other purposes they may have limited interest or limited usability."
- **1:** "No usable datasets submitted."

## Software
- **5:** "Enabling: The newly released software should affect other people's choice of research or development projects to undertake."
- **4:** "Useful: I would recommend the new software to other researchers or developers for their ongoing work."
- **3:** "Potentially useful: Someone might find the new software useful for their work."
- **2:** "Documentary: The new software will be useful to study or replicate the reported research, although for other purposes it may have limited interest or limited usability."
- **1:** "No usable software released."

## Author Identity Knowledge
- **5:** "From a violation of double-blind-submission rules, I know/can guess at least one author's name."
- **4:** "From a preprint or allowed workshop paper, I know/can guess at least one author's name."
- **3:** "From the contents of the submission itself, I know/can guess at least one author's name."
- **2:** "From social media/a talk/other informal communication, I know/can guess at least one author's name."
- **1:** "I do not have even an educated guess about author identity."
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1d3def5d-ee06-4c92-87ac-3284f72ca36c",
  "isSidechain": false,
  "promptId": "e3f72197-8c21-47a9-99b8-7cd49faae750",
  "type": "user",
  "uuid": "6b308349-0eaf-4ba4-a415-ea5576a0559a",
  "toolUseResult": {
    "bytes": 25365,
    "code": 200,
    "codeText": "OK",
    "result": "# ACL Rolling Review Form - Scoring Scales\n\n## Reviewer Confidence\n- **5:** \"Positive that my evaluation is correct. I read the paper very carefully and am familiar with related work.\"\n- **4:** \"Quite sure. I tried to check the important points carefully. It's unlikely, though conceivable, that I missed something that should affect my ratings.\"\n- **3:** \"Pretty sure, but there's a chance I missed something. Although I have a good feel for this area in general, I did not carefully check the paper's details, e.g., the math or experimental design.\"\n- **2:** \"Willing to defend my evaluation, but it is fairly likely that I missed some details, didn't understand some central points, or can't be sure about the novelty of the work.\"\n- **1:** \"Not my area, or paper is very hard to understand. My evaluation is just an educated guess.\"\n\n## Soundness\n- **5:** \"Excellent: This study is one of the most thorough I have seen, given its type.\"\n- **4:** \"Strong: This study provides sufficient support for all of its claims. Some extra experiments could be nice, but not essential.\"\n- **3:** \"Acceptable: This study provides sufficient support for its main claims. Some minor points may need extra support or details.\"\n- **2:** \"Poor: Some of the main claims are not sufficiently supported. There are major technical/methodological problems.\"\n- **1:** \"Major Issues: This study is not yet sufficiently thorough to warrant publication or is not relevant to ACL.\"\n\n## Excitement\n- **5:** \"Highly Exciting: I would recommend this paper to others and/or attend its presentation in a conference.\"\n- **4:** \"Exciting: I would mention this paper to others and/or make an effort to attend its presentation in a conference.\"\n- **3:** \"Interesting: I might mention some points of this paper to others and/or attend its presentation if there's time.\"\n- **2:** \"Potentially Interesting: this paper does not resonate with me, but it might with others in the *ACL community.\"\n- **1:** \"Not Exciting: this paper does not resonate with me, and I don't think it would with others in the *ACL community.\"\n\n## Overall Assessment\n- **5:** \"Consider for Award: I think this paper could be considered for an outstanding paper award at an *ACL conference (up to top 2.5% papers).\"\n- **4.5:** Borderline Award\n- **4:** \"Conference: I think this paper could be accepted to an *ACL conference.\"\n- **3.5:** Borderline Conference\n- **3:** \"Findings: I think this paper could be accepted to the Findings of the ACL.\"\n- **2.5:** Borderline Findings\n- **2:** \"Resubmit next cycle: I think this paper needs substantial revisions that can be completed by the next ARR cycle.\"\n- **1.5:** \"Resubmit after next cycle: I think this paper needs substantial revisions that cannot be completed by the next ARR cycle.\"\n- **1:** \"Do not resubmit: This paper has to be fully redone, or it is not relevant to the *ACL community.\"\n\n## Reproducibility\n- **5:** \"They could easily reproduce the results.\"\n- **4:** \"They could mostly reproduce the results, but there may be some variation because of sample variance or minor variations in their interpretation of the protocol or method.\"\n- **3:** \"They could reproduce the results with some difficulty. The settings of parameters are underspecified or subjectively determined, and/or the training/evaluation data are not widely available.\"\n- **2:** \"They would be hard pressed to reproduce the results: The contribution depends on data that are simply not available outside the author's institution or consortium and/or not enough details are provided.\"\n- **1:** \"They would not be able to reproduce the results here no matter how hard they tried.\"\n\n## Datasets\n- **5:** \"Enabling: The newly released datasets should affect other people's choice of research or development projects to undertake.\"\n- **4:** \"Useful: I would recommend the new datasets to other researchers or developers for their ongoing work.\"\n- **3:** \"Potentially useful: Someone might find the new datasets useful for their work.\"\n- **2:** \"Documentary: The new datasets will be useful to study or replicate the reported research, although for other purposes they may have limited interest or limited usability.\"\n- **1:** \"No usable datasets submitted.\"\n\n## Software\n- **5:** \"Enabling: The newly released software should affect other people's choice of research or development projects to undertake.\"\n- **4:** \"Useful: I would recommend the new software to other researchers or developers for their ongoing work.\"\n- **3:** \"Potentially useful: Someone might find the new software useful for their work.\"\n- **2:** \"Documentary: The new software will be useful to study or replicate the reported research, although for other purposes it may have limited interest or limited usability.\"\n- **1:** \"No usable software released.\"\n\n## Author Identity Knowledge\n- **5:** \"From a violation of double-blind-submission rules, I know/can guess at least one author's name.\"\n- **4:** \"From a preprint or allowed workshop paper, I know/can guess at least one author's name.\"\n- **3:** \"From the contents of the submission itself, I know/can guess at least one author's name.\"\n- **2:** \"From social media/a talk/other informal communication, I know/can guess at least one author's name.\"\n- **1:** \"I do not have even an educated guess about author identity.\"",
    "durationMs": 10854,
    "url": "https://aclrollingreview.org/reviewform"
  },
  "sourceToolAssistantUUID": "1d3def5d-ee06-4c92-87ac-3284f72ca36c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/.claude/sessions/review_reviewer_1_7624f219",
  "sessionId": "98d2b939-6454-4d7d-877f-2c64a5a37485",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 69 · 2026-05-19T12:54:34.552Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the information I need to write a thorough review. Let me compile my findings and write the review.

Key observations from my reading:

**Strengths:**
1. Clear, well-defined research question — first systematic component ablation of trace representations for verdict prediction
2. Comprehensive experimental design across 4 models, 3 architecture families, 1.5B-13B parameter range
3. Strong results — exception_only achieves ≥99.83% on 3/4 models
4. Thorough analysis: training dynamics, calibration, error overlap, cross-dataset, budget sweep


5. Rigorous statistical methods including Wilson confidence intervals, paired bootstrap, and McNemar tests
6. Extensive appendix with detailed ablation results, well-articulated Limitations section, and complete hyperparameter disclosure

**Weaknesses (Method/Experiment Rigor):**

The main concern is potential data leakage since Qwen-2.5-Coder-7B-Instruct generated the solutions but also serves as one of the evaluation models — while the Limitations section addresses this, it could still skew the error distribution. Additionally, the dataset is relatively small with only 591 problems drawn from HumanEval (164).

The test set has significant duplication issues: 48.99% of the exception_only set are duplicates (607 unique out of 1190), which violates the independence assumption underlying Wilson CIs. The paper's deduplication sensitivity analysis shows accuracy doesn't change, but this doesn't address that confidence interval widths should actually be narrower with the reduced effective sample size. There's also an unexplained exclusion of a DeepSeek seed that appears to be treated as an outlier in the reported results.

The ae_only and loop_only conditions are only evaluated on Qwen-7B, so the tier hierarchy isn't actually validated across models despite claims about cross-model consistency. Most other conditions beyond the main exception_only test rely on single seeds, making it difficult to assess their reliability. The paper's causal claims about the 24%/76% decomposition also lack sufficient support.

The CodeLlama tail-2048 collapse at 41.8% is a critical robustness failure that the paper excludes from analysis, suggesting the method becomes unstable with label-only loss on longer sequences. DebugBench validation is also weak due to ceiling effects—only 3.29 percentage points of headroom over the baseline. Additionally, the Wilson confidence intervals assume statistical independence across 1190 trials, but with 48.99% duplicates in the data, the effective sample size is substantially smaller, which undermines the precision claims.

The method relies heavily on format markers—B5 regex achieves 99.33% by exploiting them, and while the no-marker ablation shows a ~2 percentage point drop, this suggests a significant portion of the signal comes from a trivial shortcut. The framing around "exception events are all you need" is somewhat misleading since the exceptions originate from test assertions rather than actual runtime crashes in the code itself, even though the paper does acknowledge that 55.5% are silent logic errors detected through test assertions.

This raises questions about how the method would generalize to code with different testing approaches, more realistic and diverse codebases like SWE-bench, and why certain ablations like ae_only and loop_only weren't tested across other models.

Now I'm thinking through the effective sample size for confidence interval computation and what references might strengthen the analysis—work on test oracle sufficiency and a more explicit connection to mutation testing would be valuable additions.

Looking at the overall assessment, the paper has a clear, well-supported finding, and while there are real statistical gaps and the scope is narrow (single language, LLM-generated code, small benchmarks), the authors are quite transparent about their limitations. The core insight—that exception events contain useful information—is somewhat straightforward, but the execution is solid enough that this feels like borderline conference material.

Reconsidering the scores more carefully: the main claim holds up across four models, though the Wilson CI violations from duplicates, the selective DeepSeek reporting, and the limited ablations on exception-only and loop-only cases are legitimate methodological concerns. The 24%/76% decomposition pushes too hard toward causality. I'd rate soundness at 3—the work supports its claims adequately but needs more rigor in places. For excitement, the finding is useful and clear, but the practical applications remain somewhat speculative since running the test already gives you the verdict. The insight itself isn't particularly surprising to experienced developers.

Putting it together, this is a well-executed empirical study with honest limitations, though the methodological gaps and narrow scope—Python only, small benchmarks, LLM-generated code—constrain its impact. I'm settling on 3.5 overall, which puts it at the borderline for a conference venue; it might be better suited for a findings track given the limited novelty and scope.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6b308349-0eaf-4ba4-a415-ea5576a0559a",
  "isSidechain": false,
  "requestId": "req_011CbBxgbC56bZhv9BjCW1Gt",
  "type": "assistant",
  "uuid": "03f3c8b1-4fc6-4e81-9f2a-a72f2bd414a0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/.claude/sessions/review_reviewer_1_7624f219",
  "sessionId": "98d2b939-6454-4d7d-877f-2c64a5a37485",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NQ25zVDztdnxQ95bt5byCj",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1496,
      "cache_read_input_tokens": 83316,
      "output_tokens": 7043,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1496,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 7043,
          "cache_read_input_tokens": 83316,
          "cache_creation_input_tokens": 1496,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1496
          },
          "type": "message"
        }
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

_source line 70 · 2026-05-19T12:54:37.976Z_

论文全文和 ARR 评分标准已获取。引用验证完成（54 条 bib、0 条 orphan、0 条 missing；8 条 not_found 主要是近期预印本，7 条 mismatch 均为作者名格式差异，无虚假引用）。下面撰写完整审稿意见。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "03f3c8b1-4fc6-4e81-9f2a-a72f2bd414a0",
  "isSidechain": false,
  "requestId": "req_011CbBxgbC56bZhv9BjCW1Gt",
  "type": "assistant",
  "uuid": "562470c4-9b89-46fd-9fc0-c9c1c9ffae9b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/.claude/sessions/review_reviewer_1_7624f219",
  "sessionId": "98d2b939-6454-4d7d-877f-2c64a5a37485",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NQ25zVDztdnxQ95bt5byCj",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1496,
      "cache_read_input_tokens": 83316,
      "output_tokens": 7043,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1496,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 7043,
          "cache_read_input_tokens": 83316,
          "cache_creation_input_tokens": 1496,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1496
          },
          "type": "message"
        }
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

_source line 71 · 2026-05-19T12:56:39.881Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director · `toolu_01KvCXSfWXBvN2hFfPpmpWcH`</summary>

```json
{
  "text": "## Reviewer 1 审稿意见\n\n**论文**: \"Exception Events Are All You Need: Component Ablation for Trace-Based Verdict Prediction\"\n**Venue**: EMNLP 2026 (ARR May 2026)\n**审查侧重**: 方法严谨性 + 实验有效性\n\n---\n\n## 总体评分\n\n**Overall Assessment**: 3.5 — Borderline Conference\n**一句话总结**: 实验设计总体严谨、分析透彻，但数据规模有限（591题/单语言）、统计独立性假设在高重复率数据上存疑、核心 ablation 仅在单模型验证，限制了结论的普适性；适合 Findings，Conference 需要补充跨模型 Tier-2 验证和统计修正。\n\n## 官方维度打分（ACL ARR Review Form, Feb 2025+）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3/5 | 主要 claim 有充分实验支撑，但 Wilson CI 独立性假设在 49% 重复数据上不成立、24%/76% 因果分解过强、ae_only/loop_only tier 仅单模型验证 |\n| Excitement | 3/5 | 明确的 negative result（richer traces 反而更差）有价值，但任务本身实用场景有限（能跑测试就已知 verdict），scope 局限于 Python/LLM 生成代码 |\n| Reproducibility | 4/5 | 超参数完整披露，代码/数据/模型计划释放，VOTA 算法有伪代码；但部分条件仅单 seed，完全复现需等代码发布 |\n| Confidence | 4/5 | 仔细阅读了全文及附录，熟悉 trace-based code analysis 和 LoRA fine-tuning 相关工作 |\n\n---\n\n## Summary\n\n本文对 verdict prediction（判断测试是否通过）任务进行了首次系统性 trace component ablation。在 4 个模型（Qwen-7B/1.5B, CodeLlama-13B, DeepSeek-6.7B）上，仅使用 exception events 即可达到 ≥99.33%（3/4 模型 ≥99.83%），而完整 trace 仅 82–88%。论文进一步将性能差距分解为 information overload (~76%) 和 gradient dilution (~24%)，并通过 tail-truncation budget sweep 发现 ~500 token 的相变点。整体实验设计全面，统计报告详尽，但在数据规模、统计假设和 ablation 泛化性方面存在需修正的问题。\n\n---\n\n## 主要优势\n\n1. **研究问题定义清晰、有价值**：首次将 trace representation 作为独立变量进行系统 ablation，而非仅用作 feature augmentation。将 verdict prediction 与 code generation 明确区分（fault detection vs. simulation），立论准确（§1, §2.1）。\n\n2. **实验覆盖面宽**：4 个模型 × 7 个 trace condition × 多种分析维度（cross-model, budget sweep, calibration, error overlap, cross-dataset），构成了一个完整的实证框架。跨模型 exception_only 的 0.56pp 极窄 band 是一个很强的发现（Table 1, §3.1）。\n\n3. **Training dynamics 分析具有洞察力**：exception_only 在 50 步内收敛 vs. full_trace 全程振荡（Figure 2）直观展示了 information density 的效应，不仅报告了最终数字，还展示了学习过程。\n\n4. **统计报告规范**：Wilson CI、paired bootstrap ($B$=10,000)、McNemar 检验、多 seed 方差均有报告。Limitations 部分异常坦诚（9 条限制），包括承认 DeepSeek seed 123 问题和 self-familiarity bias。\n\n5. **Format marker ablation 设计巧妙**：nomarker 条件（§3.3）有效回应了\"模型只是学了一个 trivial shortcut\"的质疑，证明 ~91% 的 signal 是 semantic 的。\n\n6. **Cross-model budget sweep (Table 11)**：在 4 个模型上完整展示 tail-truncation 曲线，phase transition at ~500 tokens 的一致性很有说服力。\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] Wilson CI 独立性假设在高重复率数据上不成立\n\n- **具体位置**: §2.2, §3 footnote 1, Appendix H (Table 13)\n- **问题**: exception_only 测试集有 48.99% 重复（607 unique / 1190 total）。Wilson CI 假设 $n$ 个独立 Bernoulli trial，但重复样本的预测结果完全相同（论文自己在 Appendix H 确认\"model's prediction is deterministic at inference time\"），所以有效独立样本数是 607 而非 1190。论文在 Appendix F 提到 \"under deduplication ($n$=607), Qwen's accuracy is 99.67% (Wilson CI [98.81, 99.91])\"，但主文所有 CI 仍按 $n$=1190 报告。例如，exception_only 的 CI [99.58, 100.00] 在 $n$=607 下应宽得多（约 [98.8, 99.9]）。\n- **为什么影响接收**: 这不只是呈现问题——论文的 pairwise bootstrap 和 significance 判断都依赖样本独立性。在 49% 重复下，bootstrap 会低估方差，p-value 可能被高估。这影响 §3.2 中 exception_only vs. VOTA 的 \"2/3 seeds $p$<0.05\" 结论的可靠性。\n- **建议修改方向**: (1) 主文 CI 改用 $n$=unique samples 报告；(2) Bootstrap 重采样改为 problem-level resampling（以 problem 为单位而非 sample）以尊重聚类结构；(3) 在 sensitivity analysis 中不仅报告 accuracy delta=0，还要报告 CI width 变化。\n\n**N2** [critical] ae_only / loop_only ablation 仅限 Qwen-7B，Tier hierarchy 泛化性未验证\n\n- **具体位置**: §3.2, Table 2, Introduction contribution 4\n- **问题**: 论文的 contribution 4 声称\"Two-tier diagnostic hierarchy\"，但 ae_only 和 loop_only 仅在 Qwen-7B 上测试。论文措辞是 \"observed on Qwen-7B\" 且称\"direct verification on other models remains future work\"（Introduction），但 Discussion §\"Tier hierarchy: practical implications\" 段直接建议了一个基于该 hierarchy 的 fallback design，暗示了超出单模型验证的泛化性。\n- **为什么影响接收**: 如果 ae_only 在 DeepSeek 或 CodeLlama 上表现显著不同（考虑到 DeepSeek 已展现出对 seed 和 tokenizer 的敏感性），整个 tier hierarchy 可能不成立。论文的 exception_only 跨模型一致性不能替代 ae_only/loop_only 的跨模型验证——这是不同的 claim。\n- **建议修改方向**: (1) 至少在 1 个非 Qwen 模型（最好是 DeepSeek，因其行为最不同）上补做 ae_only 和 loop_only 实验；(2) 或者将 contribution 4 明确降格为 \"Qwen-7B observation\"，不在 Discussion 中做泛化性 implication。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] DeepSeek seed 123 的报告方式构成潜在选择性报告\n\n- **具体位置**: Table 1 caption, Abstract (\"≥99.33%\"), Introduction (\"≥99.33% on 2/3 seeds for the fourth\")\n- **问题**: 主表 Table 1 中 DeepSeek exception_only 报告为 \"99.33†\"（2-seed mean，排除 seed 123），但 3-seed mean 是 96.58%±4.76pp。Abstract 使用 \"≥99.83% accuracy on three of four models\" 和 \"DeepSeek-6.7B 3-seed mean 96.58%\"，Introduction 的 bold claim \"≥99.33% on 2/3 DeepSeek seeds\" 强调了好的 seed 而非整体均值。这不是造假——信息都有披露——但呈现方式倾向于 favorable interpretation。\n- **建议**: Table 1 中 DeepSeek 行应直接报告 3-seed mean 96.58%±4.76，与其他模型保持一致的 reporting convention。当前 \"†\" 注脚虽然透明但读者容易忽略。\n\n**W2** [warning] 24%/76% 因果分解的 claim 过强\n\n- **具体位置**: §3.4, Table 3, Abstract, Conclusion\n- **问题**: label_only 和 full_trace 的对比被框架为\"gradient dilution 贡献 ~24%\"。但 label_only 改变的不仅是 gradient signal——它同时改变了 effective gradient norm（从全序列降到单 token）、隐式正则化（trace token prediction 的 regularization effect 被移除）、以及 LoRA 的有效 rank 利用。论文在 §3.4 最后一段确实承认\"两个因素可能交互，所以这个分解是近似的\"和\"label-only loss simultaneously changes multiple optimization dynamics\"，但 Abstract 和 Conclusion 中 \"the performance gap approximately decomposes into information overload (~76%) and gradient dilution (~24%)\" 的表述没有传达这些 caveats。\n- **建议**: Abstract/Conclusion 中的表述应加入 \"on a single model (Qwen-7B)\" 和 \"approximate\" 修饰，并在 §3.4 讨论为什么这不是一个 clean causal decomposition（至少需要 effective gradient norm 的对照实验）。\n\n**W3** [warning] CodeLlama tail-2048 collapse (41.8%) 暴露方法 robustness 不足\n\n- **具体位置**: Table 11 (Appendix G), Discussion \"Tokenizer efficiency\" 段\n- **问题**: CodeLlama-13B 在 tail-2048 + label-only loss 条件下崩塌到 41.8%（低于 majority baseline 71.51%），但论文仅归因于 \"LoRA long-sequence instability under label-only loss\" 并从 cross-model analysis 中排除。这不仅是一个 outlier——它表明 label-only loss（论文 24%/76% 分解的关键组件）在某些 model×length 条件下根本不可用，且论文没有诊断具体原因（是 gradient vanishing？LoRA rank 不足？还是 label position bias？）。\n- **建议**: (1) 提供 tail-2048 CodeLlama 的 training loss curve 以诊断崩塌原因；(2) 讨论 label-only loss 的适用边界条件；(3) 在 24%/76% 分解的 validity 讨论中加入此 caveat。\n\n**W4** [warning] DebugBench 作为 cross-dataset validation 证据不足\n\n- **具体位置**: §3.5, Appendix K (Table 12)\n- **问题**: DebugBench 上 no_trace 已达 96.71%，只有 3.29pp headroom。exception_only 100% vs. VOTA 99.77%——差距 0.23pp，在 $N$=426 下不可能统计显著。论文自己承认 \"narrow DebugBench margins are insufficient to independently validate trace importance\"（Appendix K）。但 Introduction contribution 1 仍将 \"Cross-dataset evaluation on DebugBench ($N$=426) yields 100%\" 作为 evidence。\n- **为什么重要**: 唯一的 cross-dataset validation 本质上是 ceiling effect 导致的无区分力测试。读者可能被 \"100%\" 吸引而忽视其统计无力。\n- **建议**: (1) Introduction 中降低 DebugBench 的证据权重（改为\"ranking preserved but margins are narrow due to ceiling effect\"）；(2) 考虑增加一个更有挑战性的 cross-dataset benchmark（如来自 SWE-bench 的真实 bug 样本）。\n\n**W5** [warning] 数据集构造偏差：generator-evaluator overlap\n\n- **具体位置**: §2.2, Limitations 第 5/6 条\n- **问题**: 候选解由 Qwen-2.5-Coder-7B-Instruct 生成，该模型同时也是 4 个评估模型之一。论文称 \"this does not affect verdict prediction\" 但未提供证据。Generator overlap 可能导致两个偏差：(1) Qwen 生成的错误代码可能更容易被 Qwen 识别为错误（familiarity bias）；(2) 错误分布不代表一般分布——LLM 生成的错误以 TypeError/ValueError 为主（Table 9），而真实代码可能有更多 silent logic errors。Limitations 第 7 条提到了后者但没有量化。\n- **建议**: 在 Discussion 中补充一个简短分析：按 error type 分组比较 Qwen vs. 非 Qwen 模型的 accuracy，如果无显著差异则可 substantiate \"does not affect\" 的 claim。\n\n---\n\n## 小问题（不影响接收）\n\n- **引用格式**: `eguchi2025etcot` 和 `ferrando2025execute` 在 OpenAlex 上 not_found（可能是近期预印本），建议确认 venue 信息准确。\n- **Table 1 caption 过长**: 超过 10 行，建议将部分细节移到 footnote 或 Appendix。\n- **\"Exception Events Are All You Need\" 标题**: 标题暗示方法对所有类型的 fault 都有效，但 55.5% 的 failures 是 silent logic errors，exception_only 之所以有效是因为 test assertion 产生了 AssertionError——这实质上依赖于 test oracle 的完整性，不是 exception 本身。建议 Discussion 更显式地澄清这一点。\n- **Figure 2 caption 不准确**: \"Full-trace with label-only loss (red, dashed)\" 但该曲线是 full_trace 还是 label_only？根据正文描述应该是 full_trace 标准训练。\n- **VOTA extraction Algorithm 1**: 步骤 22–24（assertion-point）的 \"Extract expected value from test assertion\" 在实现上如何获取？test assertion 的 expected value 在 trace 中未必可见。建议补充说明或引用实现细节。\n- **Multi-seed 覆盖不均匀**: exception_only 有 3 seeds × 4 models，但 full_trace、no_trace、VOTA_no_ae 均为单 seed。虽然论文聚焦 exception_only 的 robustness，但 comparator 的 variance 未知使得 pairwise comparison 的统计功效降低。\n\n---\n\n## Questions to Authors\n\n**Q1**: Wilson CI 在 49% 重复数据上的 validity：你们的 sensitivity analysis 显示 accuracy delta=0，但 CI width 在 $n$=607 下会如何变化？是否考虑过 cluster bootstrap（以 problem 为 cluster）？\n\n**Q2**: ae_only 和 loop_only 未在 DeepSeek/CodeLlama 上测试的原因是什么？是计算资源限制还是有特定理由？如果 ae_only 在 DeepSeek 上因 tokenizer truncation 表现很差，是否会改变 tier hierarchy 的结论？\n\n**Q3**: CodeLlama tail-2048 + label-only loss 崩塌到 41.8% 的 training loss curve 是什么样的？是收敛后崩塌还是从未收敛？\n\n**Q4**: 对于不使用 assert 语句而使用 print/return 比较的测试，exception_only 方法的表现如何？当前数据集中这类测试的比例是多少？\n\n**Q5**: 论文提到 \"exception events encompass both crashes and assertion failures\"——如果测试框架使用 soft assertion（如 pytest.warns 或自定义 comparator），是否仍会产生 exception event？\n\n---\n\n## Missing References\n\n- **Mutation testing 连接**: 论文引用了 foster2025mutation 但未讨论 mutation testing 中 \"equivalent mutant\" 问题与 silent logic errors 的类比——二者都是 fault detection without exception signals 的挑战。\n- **Test oracle adequacy**: 论文的核心发现本质上是\"test oracle 的信号（assertion failures）比 execution trace 更有信息量\"，可引用 test oracle 相关文献（如 Barr et al., 2015, \"The Oracle Problem in Software Testing: A Survey\"）来加强 framing。\n\n---\n\n## 审稿结论\n\n这是一篇执行良好的实证研究，核心发现（exception events 是 verdict prediction 的 minimal sufficient signal）清晰且有说服力。统计报告比同类论文详尽得多，Limitations 部分坦诚。主要不足在于：(1) 统计独立性假设在高重复率数据上需要修正（N1）；(2) Tier hierarchy 的核心 ablation 仅限单模型（N2）。如果这两个问题能在修订中解决（N1 需要重新计算 CI/bootstrap，N2 需要补实验），论文可达到 Conference 水平。当前状态更适合 Findings。",
  "reviewer_id": "1",
  "project": "trace-verdict-study"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "562470c4-9b89-46fd-9fc0-c9c1c9ffae9b",
  "isSidechain": false,
  "requestId": "req_011CbBxgbC56bZhv9BjCW1Gt",
  "type": "assistant",
  "uuid": "db775ec9-d4da-4e54-ba5d-74751fc613de",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/.claude/sessions/review_reviewer_1_7624f219",
  "sessionId": "98d2b939-6454-4d7d-877f-2c64a5a37485",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NQ25zVDztdnxQ95bt5byCj",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1496,
      "cache_read_input_tokens": 83316,
      "output_tokens": 7043,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1496,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 7043,
          "cache_read_input_tokens": 83316,
          "cache_creation_input_tokens": 1496,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1496
          },
          "type": "message"
        }
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

_source line 72_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[Round 1 审稿请求]: 你是 Reviewer 1，负责 **方法严谨性 + 实验有效性**。  ## 论文信息 - **标题**: \"Exception Events Are All You Need: Component Ablation for Trace-Based Verdict Prediction\" - **Venue**: EMNLP 2026 (ARR May 2026)…",
  "leafUuid": "db775ec9-d4da-4e54-ba5d-74751fc613de",
  "sessionId": "98d2b939-6454-4d7d-877f-2c64a5a37485"
}
```

---

### Runtime record

_source line 73_

```json
{
  "type": "ai-title",
  "aiTitle": "Review trace-based verdict prediction paper methodology",
  "sessionId": "98d2b939-6454-4d7d-877f-2c64a5a37485"
}
```

---

### Tool result

_source line 74 · 2026-05-19T12:56:45.546Z_

<details><summary>↩ Tool result · `toolu_01KvCXSfWXBvN2hFfPpmpWcH`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_47a2f37b5c77af2e2351362f8def77a1:director\"}, \"error\": \"\"}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "db775ec9-d4da-4e54-ba5d-74751fc613de",
  "isSidechain": false,
  "promptId": "e3f72197-8c21-47a9-99b8-7cd49faae750",
  "type": "user",
  "uuid": "bedc7b7d-7bd0-4d23-ae32-59ef2e823881",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"review_director_key\\\": \\\"feishu:group:oc_47a2f37b5c77af2e2351362f8def77a1:director\\\"}, \\\"error\\\": \\\"\\\"}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_47a2f37b5c77af2e2351362f8def77a1:director\"}, \"error\": \"\"}"
    }
  },
  "sourceToolAssistantUUID": "db775ec9-d4da-4e54-ba5d-74751fc613de",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/.claude/sessions/review_reviewer_1_7624f219",
  "sessionId": "98d2b939-6454-4d7d-877f-2c64a5a37485",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 75_

```json
{
  "type": "ai-title",
  "aiTitle": "Review trace-based verdict prediction paper methodology",
  "sessionId": "98d2b939-6454-4d7d-877f-2c64a5a37485"
}
```

---

### Runtime record

_source line 76 · 2026-05-19T12:59:47.913Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-19T12:59:47.913Z",
  "sessionId": "98d2b939-6454-4d7d-877f-2c64a5a37485",
  "content": "[Round 1 审稿请求]:\n## 交叉分享：Reviewer 2 的完整审稿意见\n\n请逐条回应以下 Reviewer 2 的意见。对每一条：\n- **[AGREE]** 同意，并说明理由\n- **[REBUT]** 不同意，并提供具体证据（cite 论文的 Section/Table/Figure）\n\n特别关注以下分歧点：\n1. R2 给了 Excitement 2/5，认为核心发现\"近乎同义反复\"——你给了 3/5，请说明你为何认为 novelty 更高\n2. R2 的 N3 认为 \"richer traces hurt\" 主要是 truncation artifact——你是否同意？\n3. R2 认为 verdict prediction 缺乏实用动机——你如何评价？\n\n---\n\n以下是 Reviewer 2 的完整审稿：\n\n**Overall**: 3.0 (Findings)\n**Soundness**: 3/5, **Excitement**: 2/5, **Confidence**: 4/5\n\n### Must-Fix 问题\n\n**N1** [critical] 核心发现接近同义反复（near-tautological），novelty 存疑\n- exception events 本身就是 runtime 的 fault indicator——有 exception = fail，无 exception = pass\n- SFT 相对于 regex B4 的增量仅 6.22pp，去除 format marker 后仅 4.04pp\n- 4pp 的语义增量（区分 caught vs uncaught exceptions，6/8 boundary samples）作为核心贡献显得单薄\n- 建议重新框定贡献：转向 \"为什么 richer traces hurt training\" 作为核心贡献\n\n**N2** [critical] 实际应用动机缺失——verdict prediction 的使用场景不清晰\n- CI/CD 中 test framework 直接报告 pass/fail\n- 要获取 execution trace 必须先运行测试——此时已经有了 verdict\n- Discussion 中的三个应用场景无实验验证\n- 建议明确至少一个具体场景或重新定位为分析性工作\n\n**N3** [critical] \"Richer traces actively hurt\" 的 claim 被 truncation artifact 混淆\n- full_trace 和 VOTA 的低性能很大程度上是训练 2048-token context window 的截断导致\n- DeepSeek VOTA 91.7% 样本被截断，未截断样本 100% accuracy vs 截断样本 83.04%\n- tail_2048 可恢复 95-98% 的 exception_only accuracy\n- 建议至少用 8k+ context window 重跑 full_trace，或明确限定 claim scope\n\n### Should-Fix 问题\n\n**W1** Information density decomposition 仅在单一模型上验证\n**W2** Tier 2 hierarchy 仅在 Qwen-7B 上验证（与你的 N2 同点）\n**W3** Figure 3 图例与 caption 不一致（红色虚线标注冲突）\n**W4** Figure 2 x 轴混淆不同模型家族\n**W5** Abstract 信息密度过高\n**W6** 标题 \"X Is All You Need\" 引起审美疲劳\n\n### 缺失引用\n1. Test result parsing / build log analysis（LogParse 系列）\n2. Code agents with execution feedback（SWE-agent, OpenHands）\n3. Selective context / input pruning for LLMs\n\n### 格式合规：全部通过，仅 bib key 与 year 有少量 mismatch"
}
```

---

### Runtime record

_source line 77 · 2026-05-19T12:59:47.914Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-19T12:59:47.914Z",
  "sessionId": "98d2b939-6454-4d7d-877f-2c64a5a37485"
}
```

---

## Round 2

2 recorded events

### User

_source line 78 · 2026-05-19T12:59:47.901Z_

Continue from where you left off.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bedc7b7d-7bd0-4d23-ae32-59ef2e823881",
  "isSidechain": false,
  "promptId": "9ce812a6-28aa-43ad-bb19-d9326fe80d79",
  "type": "user",
  "isMeta": true,
  "uuid": "d58eb417-f1ef-4756-ae1c-14cb3e39da59",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/.claude/sessions/review_reviewer_1_7624f219",
  "sessionId": "98d2b939-6454-4d7d-877f-2c64a5a37485",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 79 · 2026-05-19T12:59:47.901Z_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d58eb417-f1ef-4756-ae1c-14cb3e39da59",
  "isSidechain": false,
  "type": "assistant",
  "uuid": "58b53fcc-8c55-4995-b60e-ac56b271518a",
  "isApiErrorMessage": false,
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/.claude/sessions/review_reviewer_1_7624f219",
  "sessionId": "98d2b939-6454-4d7d-877f-2c64a5a37485",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "id": "087033fc-1544-4805-9f11-cfdaf0955068",
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

5 recorded events

### User

_source line 80 · 2026-05-19T12:59:48.019Z_

[Round 1 审稿请求]:
## 交叉分享：Reviewer 2 的完整审稿意见

请逐条回应以下 Reviewer 2 的意见。对每一条：
- **[AGREE]** 同意，并说明理由
- **[REBUT]** 不同意，并提供具体证据（cite 论文的 Section/Table/Figure）

特别关注以下分歧点：
1. R2 给了 Excitement 2/5，认为核心发现"近乎同义反复"——你给了 3/5，请说明你为何认为 novelty 更高
2. R2 的 N3 认为 "richer traces hurt" 主要是 truncation artifact——你是否同意？
3. R2 认为 verdict prediction 缺乏实用动机——你如何评价？

---

以下是 Reviewer 2 的完整审稿：

**Overall**: 3.0 (Findings)
**Soundness**: 3/5, **Excitement**: 2/5, **Confidence**: 4/5

### Must-Fix 问题

**N1** [critical] 核心发现接近同义反复（near-tautological），novelty 存疑
- exception events 本身就是 runtime 的 fault indicator——有 exception = fail，无 exception = pass
- SFT 相对于 regex B4 的增量仅 6.22pp，去除 format marker 后仅 4.04pp
- 4pp 的语义增量（区分 caught vs uncaught exceptions，6/8 boundary samples）作为核心贡献显得单薄
- 建议重新框定贡献：转向 "为什么 richer traces hurt training" 作为核心贡献

**N2** [critical] 实际应用动机缺失——verdict prediction 的使用场景不清晰
- CI/CD 中 test framework 直接报告 pass/fail
- 要获取 execution trace 必须先运行测试——此时已经有了 verdict
- Discussion 中的三个应用场景无实验验证
- 建议明确至少一个具体场景或重新定位为分析性工作

**N3** [critical] "Richer traces actively hurt" 的 claim 被 truncation artifact 混淆
- full_trace 和 VOTA 的低性能很大程度上是训练 2048-token context window 的截断导致
- DeepSeek VOTA 91.7% 样本被截断，未截断样本 100% accuracy vs 截断样本 83.04%
- tail_2048 可恢复 95-98% 的 exception_only accuracy
- 建议至少用 8k+ context window 重跑 full_trace，或明确限定 claim scope

### Should-Fix 问题

**W1** Information density decomposition 仅在单一模型上验证
**W2** Tier 2 hierarchy 仅在 Qwen-7B 上验证（与你的 N2 同点）
**W3** Figure 3 图例与 caption 不一致（红色虚线标注冲突）
**W4** Figure 2 x 轴混淆不同模型家族
**W5** Abstract 信息密度过高
**W6** 标题 "X Is All You Need" 引起审美疲劳

### 缺失引用
1. Test result parsing / build log analysis（LogParse 系列）
2. Code agents with execution feedback（SWE-agent, OpenHands）
3. Selective context / input pruning for LLMs

### 格式合规：全部通过，仅 bib key 与 year 有少量 mismatch

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "58b53fcc-8c55-4995-b60e-ac56b271518a",
  "isSidechain": false,
  "promptId": "9ce812a6-28aa-43ad-bb19-d9326fe80d79",
  "type": "user",
  "uuid": "03f55059-596b-425f-86ce-62f046cc920f",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/.claude/sessions/review_reviewer_1_7624f219",
  "sessionId": "98d2b939-6454-4d7d-877f-2c64a5a37485",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 81 · 2026-05-19T13:00:23.318Z_

<details><summary>Logged reasoning block</summary>

```text
Let me carefully review Reviewer 2's comments and compare them with my own assessment. I need to go through each point and provide [AGREE] or [REBUT] with specific evidence from the paper.

Let me organize my response:

**R2-N1**: Core finding is near-tautological
**R2-N2**: Practical motivation missing
**R2-N3**: "Richer traces hurt" confounded by truncation
**R2-W1-W6**: Various should-fix issues
**Missing references**: Three categories

I also need to address the three specific divergence points the Director highlighted.


---

For R2-N1, I see the real novelty isn't that exceptions signal faults—that's indeed obvious—but rather the counterintuitive finding that adding more information actually degrades performance, plus the specific training dynamics showing rapid convergence versus oscillation and the quantitative magnitude of these effects.

For R2-N2, R2 raises a fair point about practical motivation that I acknowledged myself, though I think the analytical contribution stands on its own even if the applications aren't fully validated.

For R2-N3, this is where we genuinely disagree. R2 attributes full_trace's poor performance to truncation, but looking at the Qwen-7B results with no truncation limit, the model still only achieves 81.76%, which contradicts that explanation.

However, I need to be more careful here — even the "no_limit" setting is capped at 2048 tokens by the model's max sequence length, so R2 does have a point that we haven't tested with truly long contexts. But the tail-truncation experiments are revealing: even when truncating to just the last 2048 tokens, performance only reaches 97.3%, still 2.52 percentage points below exception_only's 99.83%. And the head-truncation results show non-monotonic patterns that suggest this isn't purely a length problem.

Looking at the information density decomposition, the label_only condition has the same input length as full_trace but achieves much higher accuracy, which tells me about 24% of the gap is gradient dilution independent of truncation. The remaining 76% "information overload" component could be partially due to truncation, but I'm realizing I need to clarify what "no_limit" actually means in the trace length ablation — whether it's an unlimited trace budget that still gets capped at 2048 by the model, or something else entirely.

Actually, I think I've been interpreting this correctly: even with no trace budget limit, the model's 2048 context window still applies, so full_trace samples that exceed this get truncated. But the tail-truncation experiments are revealing — tail-2048 hits 97.3% while head-2048 only reaches 81.76%, which shows the problem isn't truncation itself but which part gets truncated. The fact that tail-2048 still underperforms exception_only by 2.52 percentage points, combined with the label_only evidence of gradient dilution, suggests R2's critique has some validity but oversimplifies the issue. Truncation is definitely a contributing factor, but it's not the whole story — the claim that richer traces actively hurt needs more nuance.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "03f55059-596b-425f-86ce-62f046cc920f",
  "isSidechain": false,
  "requestId": "req_011CbBy9U3Te6wy7DTDHf5GH",
  "type": "assistant",
  "uuid": "2d9ae9e4-d6d5-4b67-88fa-3025b94b8b1b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/.claude/sessions/review_reviewer_1_7624f219",
  "sessionId": "98d2b939-6454-4d7d-877f-2c64a5a37485",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018vx4kJX4Xqy1qJKwzDfXa5",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1025,
      "cache_read_input_tokens": 91927,
      "output_tokens": 4889,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1025,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 4889,
          "cache_read_input_tokens": 91927,
          "cache_creation_input_tokens": 1025,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1025
          },
          "type": "message"
        }
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

_source line 82 · 2026-05-19T13:00:23.321Z_

逐条回应 Reviewer 2 意见如下。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2d9ae9e4-d6d5-4b67-88fa-3025b94b8b1b",
  "isSidechain": false,
  "requestId": "req_011CbBy9U3Te6wy7DTDHf5GH",
  "type": "assistant",
  "uuid": "bf8f58f5-6b41-4485-a9db-37bda6ae0b55",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/.claude/sessions/review_reviewer_1_7624f219",
  "sessionId": "98d2b939-6454-4d7d-877f-2c64a5a37485",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018vx4kJX4Xqy1qJKwzDfXa5",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1025,
      "cache_read_input_tokens": 91927,
      "output_tokens": 4889,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1025,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 4889,
          "cache_read_input_tokens": 91927,
          "cache_creation_input_tokens": 1025,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1025
          },
          "type": "message"
        }
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

_source line 83 · 2026-05-19T13:01:44.953Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director · `toolu_01Hdf5eLNKtryBWS7sSvYhKv`</summary>

```json
{
  "text": "## Reviewer 1 对 Reviewer 2 意见的交叉回应\n\n---\n\n### R2-N1: 核心发现接近同义反复（near-tautological）\n\n**[REBUT] 部分不同意。**\n\nR2 的论点是\"有 exception = fail，无 exception = pass\"是 trivial 的。如果论文的贡献仅仅是这一点，我会完全同意。但论文的实际贡献有两个非 trivial 的维度：\n\n（1）**\"Adding more information actively hurts\" 是反直觉的。** VOTA 是 exception+assertion+loop 的超集，包含了 exception_only 的全部信息，却在 Qwen-7B 上 underperform 0.78pp（Table 2: 99.05% vs 99.83%，2/3 seeds $p$<0.05）。在 DeepSeek 上差距扩大到 14.96pp（84.45% vs 99.33%）。如果发现只是\"exception 有用\"，那 VOTA ≥ exception_only 才是预期。\"strictly more information → worse performance\" 需要 mechanism-level 的解释，论文通过 training dynamics（Figure 2: 50-step 收敛 vs. 全程振荡）和 information density decomposition（§3.4）提供了这一解释。这不是同义反复。\n\n（2）**量化 scale 本身有价值。** 完整 trace 和 exception_only 之间 18pp 的差距（Table 2），以及 exception_only 跨 4 个模型/3 个架构仅 0.56pp 变异（Table 1），这些定量发现不能从\"exception 是 fault indicator\"的先验知识中推导出来。先验上完全可能出现 full_trace > exception_only（因为完整 trace 包含更多上下文帮助模型做判断）。\n\n**但我同意 R2 的部分观点：** SFT over regex B4 的增量仅 6.22pp（去 marker 后 4.04pp），且核心语义增量（caught vs uncaught, 6/8 boundary samples）确实单薄。论文在 framing 上过度强调了 exception_only 的绝对性能，而对\"为什么 richer traces hurt training\"的 mechanism 分析的贡献权重不足。\n\n**我与 R2 的分歧在于程度**：R2 给 Excitement 2/5（\"does not resonate\"），我给 3/5。我认为 \"more information can degrade SFT performance through attention competition\" 这一发现对 trace-augmented training 社区有实际指导价值——它不仅回答了 \"which component\"，还回答了 \"why combining components fails\"。但我同意这不足以支撑 Excitement 4/5。3/5 是合理的中间评估。\n\n---\n\n### R2-N2: 实际应用动机缺失\n\n**[AGREE] 大体同意，补充一点。**\n\nR2 的核心论点成立：要获取 execution trace 必须运行测试，此时 test framework 已直接报告 verdict。Discussion 中提到的三个场景（patch correctness prediction, flaky test detection, offline trace analysis）均无实验验证。\n\n不过我认为 R2 的 framing 稍显绝对。论文在 Conclusion 最后一句明确将自己定位为 analytical work（\"information density, not information quantity, determines learning efficiency\"），这一原则的适用范围超出 verdict prediction 本身——它对任何 trace-augmented LLM 训练都有参考价值。\n\n**实际影响**：同意这一弱点存在，但这主要影响 Excitement 评分而非 Soundness。作为分析性工作，verdict prediction 是一个干净的 testbed（binary classification, 无 generation 噪声），即使 task 本身实用性有限，方法论发现仍有迁移价值。我在 Overall 评分中已将此纳入考虑（3.5 而非 4）。\n\n---\n\n### R2-N3: \"Richer traces actively hurt\" 被 truncation artifact 混淆\n\n**[REBUT] 部分不同意——truncation 是一个因素但不是主要因素。R2 过度归因于 truncation。**\n\nR2 的关键论据：\n- DeepSeek VOTA 91.7% 样本被截断\n- 未截断样本 100% vs 截断样本 83.04%\n- tail_2048 恢复了 95-98%\n\n我的反驳，基于论文中的具体数据：\n\n**(1) full_trace \"no_limit\" 仍然只有 81.76%（Table 8，Appendix G）。** 这是 Qwen-7B 上的结果，Qwen tokenizer 比 DeepSeek 高效得多（1929 vs 2626 tokens/sample）。即使在 Qwen 上截断压力小得多，full_trace 仍比 exception_only 低 18pp。如果 truncation 是唯一问题，Qwen full_trace 应表现远好于此。\n\n*但需要承认*：即使 \"no_limit\" 也受制于 2048 max_seq_len（§2.4），所以 Qwen full_trace 仍有部分样本被截断。R2 建议的 8k+ context 实验确实能更 cleanly 分离 truncation 效应。\n\n**(2) tail-truncation 实验提供了部分反驳。** tail-2048 在 Qwen-7B 上达到 97.3%（Table 11），但仍比 exception_only 低 2.52pp。这 2.52pp 的残余 gap 在不存在 truncation 问题的条件下仍然存在（tail-2048 保留了 trace 末端的完整 exception traceback），证明\"information overload\"（非 truncation）是一个真实效应——模型需要从 2048 token 的窗口中过滤掉非诊断行，这比直接接收 150 token 的 exception 更难。\n\n**(3) Information density decomposition 提供了独立证据。** §3.4 的 label_only 实验使用**完全相同的 full_trace 输入**，仅改变 loss mask。label_only (85.94%) vs full_trace (81.76%) 的 4.18pp 差距不可能由 truncation 解释——输入完全一样，只有 loss 计算不同。这证明了 gradient dilution 是一个真实的、独立于 truncation 的因素。\n\n**(4) 但 R2 对 DeepSeek VOTA 的分析是对的。** DeepSeek 的 14.96pp VOTA gap 确实主要是 truncation artifact，论文在 Appendix F（§F）自己也这么说。论文不应在主文中将 DeepSeek VOTA 的 84.45% 与 Qwen VOTA 的 99.05% 并列比较而不强调 truncation confound。\n\n**我的结论**：R2 正确地指出了 truncation 是一个重要 confound（特别是对 DeepSeek），但 \"主要是 truncation artifact\" 的 claim 过强。Qwen 数据（较少 truncation 压力下仍有显著 gap）和 label_only 实验（相同输入不同 loss 下仍有 gap）共同表明 information overload 和 gradient dilution 是真实效应。论文应该更 carefully 限定 \"richer traces hurt\" 的 claim scope，区分 (a) truncation-driven degradation（DeepSeek VOTA）和 (b) genuine information overload（Qwen full_trace vs exception_only 的残余 gap）。\n\nR2 建议的 8k+ context 实验确实有价值——它能 definitively 分离 truncation 效应。但即使不做这个实验，现有数据也不支持 \"主要是 truncation\" 的结论。\n\n---\n\n### R2-W1: Information density decomposition 仅单模型\n\n**[AGREE]** 与我的 W2 一致。论文在 §3.4 最后一句承认 \"cross-model validation remains future work\"，但 Abstract 和 Conclusion 中 24%/76% 数字出现时未加此限定。至少应在 Abstract 中明确 \"on Qwen-7B\"。\n\n---\n\n### R2-W2: Tier 2 hierarchy 仅 Qwen-7B\n\n**[AGREE]** 与我的 N2 完全一致。这是我列为 Must-Fix 的问题之一。不再赘述。\n\n---\n\n### R2-W3: Figure 3 图例与 caption 不一致\n\n**[AGREE]** 未独立验证此视觉问题（我的审查基于 tex 源码），但如果图例确实有标注冲突，应当修正。我在小问题中也提到了 Figure 2 caption 中 \"Full-trace with label-only loss (red, dashed)\" 的描述可能不准确。\n\n---\n\n### R2-W4: Figure 2 x 轴混淆不同模型家族\n\n**[AGREE]** 如果 x 轴混合了不同模型的 training steps 而未标注，这会误导读者。不同模型的 step 数不同（Appendix B: training time 从 0.5h 到 2.3h），直接叠加 training curves 需要明确标注各曲线对应的模型和条件。\n\n---\n\n### R2-W5: Abstract 信息密度过高\n\n**[AGREE]** Abstract 确实包含了过多的具体数字（99.83%, 82-88%, 50 steps, 76%/24%, ~500 tokens, 55.5%, 150 tokens, 10×）。对于 8 页的 empirical paper，Abstract 更应该传达 narrative arc 而非数据密度。建议保留 3-4 个关键数字，其余留给正文。\n\n---\n\n### R2-W6: 标题 \"X Is All You Need\"\n\n**[AGREE]** \"X Is All You Need\" 确实已经 overused。更严谨的标题如 \"Exception Events Suffice for Trace-Based Verdict Prediction\" 或 \"Less Is More: Why Exception Events Outperform Complete Traces for Verdict Prediction\" 更能传达核心 insight 而不引起审美疲劳。\n\n---\n\n### R2 缺失引用\n\n**[AGREE]** R2 提出的三类缺失引用（LogParse 系列、SWE-agent/OpenHands、selective context pruning）均有道理：\n- LogParse 系列与 trace parsing 直接相关\n- SWE-agent/OpenHands 代表了 execution feedback 在 agent 中的最新应用，是论文的下游使用场景之一\n- Selective context / input pruning（如 LLMLingua, Compresso）与论文 \"information density\" 的核心论点有直接联系\n\n我自己额外建议引用 test oracle 文献（Barr et al., 2015）。\n\n---\n\n## 综合评估\n\nR2 和我的评分差距主要在 **Excitement**（R2: 2, 我: 3）和 **Overall**（R2: 3.0, 我: 3.5）。\n\n**Excitement 分歧的理由**：R2 认为核心发现 near-tautological，我认为 \"more info → worse SFT\" 和 training dynamics mechanism 有独立贡献。但我承认 R2 的 practical motivation 批评成立，这确实拉低了 excitement。如果必须调整，我会维持 3/5 但附注\"仅作为 analytical contribution 有价值\"。\n\n**Overall 分歧**：R2 的三个 Must-Fix 中，N1（tautological）和 N2（practical motivation）更多是 framing/positioning 问题而非 technical flaw，可通过重写 Introduction/Discussion 解决。N3（truncation confound）我部分不同意，但同意论文需要更 carefully qualify claims。我维持 3.5 (Borderline Conference) 的评分，认为修订后有潜力达到 Conference；如果 Tier-2 跨模型实验和 CI 修正无法在修订中完成，则 3.0 (Findings) 更合适。\n\n**两位 Reviewer 的共识**：\n1. Tier hierarchy 需要跨模型验证（我的 N2 = R2 的 W2）\n2. 24%/76% 分解需要更谨慎的 causal language\n3. DebugBench 作为 cross-dataset validation 证据不足\n4. 部分 claim 的 scope 需要限定（单模型、单语言、LLM 生成代码）\n5. Abstract 和 Introduction 的数字密度可适当降低",
  "reviewer_id": "1",
  "project": "trace-verdict-study"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bf8f58f5-6b41-4485-a9db-37bda6ae0b55",
  "isSidechain": false,
  "requestId": "req_011CbBy9U3Te6wy7DTDHf5GH",
  "type": "assistant",
  "uuid": "0835a2aa-65d5-4f08-acd3-bd10bce700b8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/.claude/sessions/review_reviewer_1_7624f219",
  "sessionId": "98d2b939-6454-4d7d-877f-2c64a5a37485",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018vx4kJX4Xqy1qJKwzDfXa5",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1025,
      "cache_read_input_tokens": 91927,
      "output_tokens": 4889,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1025,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 4889,
          "cache_read_input_tokens": 91927,
          "cache_creation_input_tokens": 1025,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1025
          },
          "type": "message"
        }
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

_source line 84 · 2026-05-19T13:01:49.071Z_

<details><summary>↩ Tool result · `toolu_01Hdf5eLNKtryBWS7sSvYhKv`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_47a2f37b5c77af2e2351362f8def77a1:director\"}, \"error\": \"\"}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0835a2aa-65d5-4f08-acd3-bd10bce700b8",
  "isSidechain": false,
  "promptId": "9ce812a6-28aa-43ad-bb19-d9326fe80d79",
  "type": "user",
  "uuid": "2fc9669e-86e1-438c-96cf-c4a3768d65b6",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"review_director_key\\\": \\\"feishu:group:oc_47a2f37b5c77af2e2351362f8def77a1:director\\\"}, \\\"error\\\": \\\"\\\"}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_47a2f37b5c77af2e2351362f8def77a1:director\"}, \"error\": \"\"}"
    }
  },
  "sourceToolAssistantUUID": "0835a2aa-65d5-4f08-acd3-bd10bce700b8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/.claude/sessions/review_reviewer_1_7624f219",
  "sessionId": "98d2b939-6454-4d7d-877f-2c64a5a37485",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---
