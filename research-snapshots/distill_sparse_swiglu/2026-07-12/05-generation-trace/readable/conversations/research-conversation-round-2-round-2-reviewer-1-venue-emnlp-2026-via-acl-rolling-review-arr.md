# Research conversation: [Round 2 审稿请求]: ## Round 2 审稿任务 — Reviewer 1（方法严谨性 + 实验设计） ### Venue 信息 - **目标**: EMNLP 2026 via ACL Rolling Review (ARR

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 66
- **Recorded user turns:** 3
- **Tool calls:** 17
- **Original source:** `logs/chats/exported-trajectories/account-2/e4589542-c5a3-4a5b-a779-c62f37dfeb92.jsonl`
- **Structured JSON:** [`dda67b4c8f33e1580f25.json`](../../sessions/dd/dda67b4c8f33e1580f25.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-17T04:47:35.522Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-17T04:47:35.522Z",
  "sessionId": "e4589542-c5a3-4a5b-a779-c62f37dfeb92",
  "content": "[Round 2 审稿请求]:\n## Round 2 审稿任务 — Reviewer 1（方法严谨性 + 实验设计）\n\n### Venue 信息\n- **目标**: EMNLP 2026 via ACL Rolling Review (ARR) May 2026 cycle\n- **Deadline**: 2026-05-25\n- **页数限制**: 正文 8 页 + unlimited references; Limitations 不计页数\n- **模板**: ACL template with `[review]` option\n- **匿名规则**: Double-blind\n\n### 论文路径\n`projects/distill_sparse_swiglu/paper/main.tex`（含 abstract.tex, introduction.tex, related_work.tex, method.tex, experiments.tex, conclusion.tex, limitations.tex, appendix.tex）\n\n### 你的审查侧重\n1. **方法严谨性**：KL distillation framework 的理论支撑、Gumbel-Sigmoid 采样、Lagrangian 对偶约束的正确性\n2. **实验设计**：baseline 对比公平性、统计显著性、消融实验完整性\n3. **重点验证 Round 1 遗留 in_progress issues**：\n   - **R1-W4** (in_progress): §3.5 梯度分析从 \"theoretical contribution\" 弱化为 \"gradient-based motivation\"，且需添加实证 gradient SNR 数据 (KL/BCE=5.76×)。检查是否已完成、数据是否可信、framing 是否合理。\n   - **R1-W5** (in_progress): Lagrangian 对偶更新缺收敛分析。Appendix C 已有 convergence table (4 targets × final λ + actual sparsity)，还需 λ/sparsity 时序曲线。检查 Appendix C 是否充分。\n   - **R1-W3** (open/info): 三 seed (n=3) 统计效力——检查是否有改善或 adequate justification。\n\n### 输出格式\n请按以下结构输出审稿意见：\n1. Summary (2-3 sentences)\n2. Strengths (bullet points)\n3. Weaknesses (bullet points, 标注 severity: critical/warning/info)\n4. Round 1 Issue Status (逐条确认 R1-W4, R1-W5, R1-W3 是否已修复)\n5. Questions for authors\n6. Missing references\n7. Overall score (strong reject / weak reject / borderline / weak accept / strong accept) + confidence (1-5)"
}
```

---

### Runtime record

_source line 2 · 2026-05-17T04:47:35.526Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-17T04:47:35.526Z",
  "sessionId": "e4589542-c5a3-4a5b-a779-c62f37dfeb92"
}
```

---

## Round 1

58 recorded events

### User

_source line 3 · 2026-05-17T04:47:35.563Z_

[Round 2 审稿请求]:
## Round 2 审稿任务 — Reviewer 1（方法严谨性 + 实验设计）

### Venue 信息
- **目标**: EMNLP 2026 via ACL Rolling Review (ARR) May 2026 cycle
- **Deadline**: 2026-05-25
- **页数限制**: 正文 8 页 + unlimited references; Limitations 不计页数
- **模板**: ACL template with `[review]` option
- **匿名规则**: Double-blind

### 论文路径
`projects/distill_sparse_swiglu/paper/main.tex`（含 abstract.tex, introduction.tex, related_work.tex, method.tex, experiments.tex, conclusion.tex, limitations.tex, appendix.tex）

### 你的审查侧重
1. **方法严谨性**：KL distillation framework 的理论支撑、Gumbel-Sigmoid 采样、Lagrangian 对偶约束的正确性
2. **实验设计**：baseline 对比公平性、统计显著性、消融实验完整性
3. **重点验证 Round 1 遗留 in_progress issues**：
   - **R1-W4** (in_progress): §3.5 梯度分析从 "theoretical contribution" 弱化为 "gradient-based motivation"，且需添加实证 gradient SNR 数据 (KL/BCE=5.76×)。检查是否已完成、数据是否可信、framing 是否合理。
   - **R1-W5** (in_progress): Lagrangian 对偶更新缺收敛分析。Appendix C 已有 convergence table (4 targets × final λ + actual sparsity)，还需 λ/sparsity 时序曲线。检查 Appendix C 是否充分。
   - **R1-W3** (open/info): 三 seed (n=3) 统计效力——检查是否有改善或 adequate justification。

### 输出格式
请按以下结构输出审稿意见：
1. Summary (2-3 sentences)
2. Strengths (bullet points)
3. Weaknesses (bullet points, 标注 severity: critical/warning/info)
4. Round 1 Issue Status (逐条确认 R1-W4, R1-W5, R1-W3 是否已修复)
5. Questions for authors
6. Missing references
7. Overall score (strong reject / weak reject / borderline / weak accept / strong accept) + confidence (1-5)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "d17f6ff5-7f93-4500-81a7-61caa2f125ae",
  "type": "user",
  "uuid": "3e9604b6-cefe-44f5-bc89-16790ae7b475",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/review_reviewer_1_772f066c",
  "sessionId": "e4589542-c5a3-4a5b-a779-c62f37dfeb92",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-17T04:47:35.562Z_

```json
{
  "parentUuid": "3e9604b6-cefe-44f5-bc89-16790ae7b475",
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
  "uuid": "529a8acc-120d-4ff3-b9c3-ae92d55d11da",
  "timestamp": "2026-05-17T04:47:35.562Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/review_reviewer_1_772f066c",
  "sessionId": "e4589542-c5a3-4a5b-a779-c62f37dfeb92",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

---

### Runtime record

_source line 5 · 2026-05-17T04:47:35.562Z_

```json
{
  "parentUuid": "529a8acc-120d-4ff3-b9c3-ae92d55d11da",
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
  "uuid": "ca9a4341-5ef4-430e-a73a-c8274f55973d",
  "timestamp": "2026-05-17T04:47:35.562Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/review_reviewer_1_772f066c",
  "sessionId": "e4589542-c5a3-4a5b-a779-c62f37dfeb92",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

---

### Runtime record

_source line 6 · 2026-05-17T04:47:35.562Z_

```json
{
  "parentUuid": "ca9a4341-5ef4-430e-a73a-c8274f55973d",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "4c356dca-c6e7-4c78-9c5b-fddd4c6cfb91",
  "timestamp": "2026-05-17T04:47:35.562Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/review_reviewer_1_772f066c",
  "sessionId": "e4589542-c5a3-4a5b-a779-c62f37dfeb92",
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
  "aiTitle": "Review Round 2 distill sparse SwiGLU paper",
  "sessionId": "e4589542-c5a3-4a5b-a779-c62f37dfeb92"
}
```

---

### Assistant

_source line 8 · 2026-05-17T04:47:40.213Z_

<details><summary>Logged reasoning block</summary>

```text
The user (Review Director) is asking me to perform a Round 2 review of the paper, focusing on method rigor and experimental design. I need to:

1. First, read the paper (main.tex and its components)
2. Search for EMNLP 2026 / ACL ARR reviewer guidelines
3. Focus on the specific issues mentioned (R1-W4, R1-W5, R1-W3)
4. Output my review in the specified format

Let me start by reading the paper files and searching for reviewer guidelines.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4c356dca-c6e7-4c78-9c5b-fddd4c6cfb91",
  "isSidechain": false,
  "requestId": "req_011Cb7XzfoDT8tTx7vsnrKkP",
  "type": "assistant",
  "uuid": "33f59e06-1b84-4bfa-8935-8724f5ea6621",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/review_reviewer_1_772f066c",
  "sessionId": "e4589542-c5a3-4a5b-a779-c62f37dfeb92",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WFBZ9BUeJWWnrAa1s5fL9U",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15601,
      "cache_read_input_tokens": 11841,
      "output_tokens": 294,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 15601,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 294,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 15601,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 15601
          },
          "type": "message"
        }
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

_source line 9 · 2026-05-17T04:47:41.212Z_

开始 Round 2 审稿。先读论文材料并搜索 ARR reviewer guidelines。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "33f59e06-1b84-4bfa-8935-8724f5ea6621",
  "isSidechain": false,
  "requestId": "req_011Cb7XzfoDT8tTx7vsnrKkP",
  "type": "assistant",
  "uuid": "c011c8fc-a79e-4dcd-addb-4a6fe09ef66e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/review_reviewer_1_772f066c",
  "sessionId": "e4589542-c5a3-4a5b-a779-c62f37dfeb92",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WFBZ9BUeJWWnrAa1s5fL9U",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15601,
      "cache_read_input_tokens": 11841,
      "output_tokens": 294,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 15601,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 294,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 15601,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 15601
          },
          "type": "message"
        }
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

_source line 10 · 2026-05-17T04:47:42.510Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01Kh5igb3zJJmXXXn6qPtzxU`</summary>

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
  "parentUuid": "c011c8fc-a79e-4dcd-addb-4a6fe09ef66e",
  "isSidechain": false,
  "requestId": "req_011Cb7XzfoDT8tTx7vsnrKkP",
  "type": "assistant",
  "uuid": "ee17e5d8-1ee1-4908-bd93-9a811b856ba4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/review_reviewer_1_772f066c",
  "sessionId": "e4589542-c5a3-4a5b-a779-c62f37dfeb92",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WFBZ9BUeJWWnrAa1s5fL9U",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15601,
      "cache_read_input_tokens": 11841,
      "output_tokens": 294,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 15601,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 294,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 15601,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 15601
          },
          "type": "message"
        }
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

_source line 11 · 2026-05-17T04:47:42.525Z_

<details><summary>↩ Tool result · `toolu_01Kh5igb3zJJmXXXn6qPtzxU`</summary>

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
  "parentUuid": "ee17e5d8-1ee1-4908-bd93-9a811b856ba4",
  "isSidechain": false,
  "promptId": "d17f6ff5-7f93-4500-81a7-61caa2f125ae",
  "type": "user",
  "uuid": "25331cb8-01a4-47fb-bc0a-72ed800a84b6",
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
  "sourceToolAssistantUUID": "ee17e5d8-1ee1-4908-bd93-9a811b856ba4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/review_reviewer_1_772f066c",
  "sessionId": "e4589542-c5a3-4a5b-a779-c62f37dfeb92",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 12 · 2026-05-17T04:47:46.313Z_

<details><summary>Logged reasoning block</summary>

```text
Now let me read the paper files and search for ARR reviewer guidelines in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "25331cb8-01a4-47fb-bc0a-72ed800a84b6",
  "isSidechain": false,
  "requestId": "req_011Cb7Y1BjYPQsxi4Px2JAPp",
  "type": "assistant",
  "uuid": "078139c8-c89a-4071-a69c-ace712b219e3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/review_reviewer_1_772f066c",
  "sessionId": "e4589542-c5a3-4a5b-a779-c62f37dfeb92",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014Es7sMLrXbE3QyNkwyykj6",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2290,
      "cache_read_input_tokens": 27442,
      "output_tokens": 167,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2290,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 167,
          "cache_read_input_tokens": 27442,
          "cache_creation_input_tokens": 2290,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2290
          },
          "type": "message"
        }
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

_source line 13 · 2026-05-17T04:47:46.423Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_018GQDRX2wm3skEfh47shgYh`</summary>

```json
{
  "query": "ACL Rolling Review 2026 reviewer guidelines review form criteria"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "078139c8-c89a-4071-a69c-ace712b219e3",
  "isSidechain": false,
  "requestId": "req_011Cb7Y1BjYPQsxi4Px2JAPp",
  "type": "assistant",
  "uuid": "ad891ad9-83df-4d7d-953a-d24133d023e7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/review_reviewer_1_772f066c",
  "sessionId": "e4589542-c5a3-4a5b-a779-c62f37dfeb92",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014Es7sMLrXbE3QyNkwyykj6",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2290,
      "cache_read_input_tokens": 27442,
      "output_tokens": 167,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2290,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 167,
          "cache_read_input_tokens": 27442,
          "cache_creation_input_tokens": 2290,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2290
          },
          "type": "message"
        }
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

_source line 14 · 2026-05-17T04:47:46.942Z_

<details open><summary>🔧 Tool call — Read · `toolu_01SdB7gqJSj3c9hFrf4JmiWd`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ad891ad9-83df-4d7d-953a-d24133d023e7",
  "isSidechain": false,
  "requestId": "req_011Cb7Y1BjYPQsxi4Px2JAPp",
  "type": "assistant",
  "uuid": "f3fa479e-d2c4-492c-af07-56c6d7cb2df2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/review_reviewer_1_772f066c",
  "sessionId": "e4589542-c5a3-4a5b-a779-c62f37dfeb92",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014Es7sMLrXbE3QyNkwyykj6",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2290,
      "cache_read_input_tokens": 27442,
      "output_tokens": 167,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2290,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 167,
          "cache_read_input_tokens": 27442,
          "cache_creation_input_tokens": 2290,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2290
          },
          "type": "message"
        }
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

_source line 15 · 2026-05-17T04:47:46.962Z_

<details><summary>↩ Tool result · `toolu_01SdB7gqJSj3c9hFrf4JmiWd`</summary>

```text
1	\documentclass[11pt]{article}
2	\usepackage[review]{acl}
3	\usepackage{times}
4	\usepackage{latexsym}
5	\usepackage[T1]{fontenc}
6	\usepackage[utf8]{inputenc}
7	\usepackage{microtype}
8	% \usepackage{inconsolata} % not available on this system
9	\usepackage{graphicx}
10	\graphicspath{{../figures/paper/}}
11	\usepackage{amsmath}
12	\usepackage{amssymb}
13	\usepackage{booktabs}
14	\usepackage{multirow}
15	\usepackage{enumitem}
16	
17	\title{Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs}
18	
19	\author{Anonymous}
20	
21	\begin{document}
22	\maketitle
23	
24	\begin{abstract}
25	\input{abstract}
26	\end{abstract}
27	
28	\input{introduction}
29	\input{related_work}
30	\input{method}
31	\input{experiments}
32	\input{conclusion}
33	\input{limitations}
34	
35	\bibliography{references}
36	
37	\input{appendix}
38	
39	\end{document}
40	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f3fa479e-d2c4-492c-af07-56c6d7cb2df2",
  "isSidechain": false,
  "promptId": "d17f6ff5-7f93-4500-81a7-61caa2f125ae",
  "type": "user",
  "uuid": "1ca22023-625f-4b5d-a62c-4d339f41849e",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/main.tex",
      "content": "\\documentclass[11pt]{article}\n\\usepackage[review]{acl}\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage[T1]{fontenc}\n\\usepackage[utf8]{inputenc}\n\\usepackage{microtype}\n% \\usepackage{inconsolata} % not available on this system\n\\usepackage{graphicx}\n\\graphicspath{{../figures/paper/}}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{enumitem}\n\n\\title{Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs}\n\n\\author{Anonymous}\n\n\\begin{document}\n\\maketitle\n\n\\begin{abstract}\n\\input{abstract}\n\\end{abstract}\n\n\\input{introduction}\n\\input{related_work}\n\\input{method}\n\\input{experiments}\n\\input{conclusion}\n\\input{limitations}\n\n\\bibliography{references}\n\n\\input{appendix}\n\n\\end{document}\n",
      "numLines": 40,
      "startLine": 1,
      "totalLines": 40
    }
  },
  "sourceToolAssistantUUID": "f3fa479e-d2c4-492c-af07-56c6d7cb2df2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/review_reviewer_1_772f066c",
  "sessionId": "e4589542-c5a3-4a5b-a779-c62f37dfeb92",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-17T04:47:58.609Z_

<details><summary>↩ Tool result · `toolu_018GQDRX2wm3skEfh47shgYh`</summary>

```text
Web search results for query: "ACL Rolling Review 2026 reviewer guidelines review form criteria"

Links: [{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"ACL Rolling Review | ACL Member Portal","url":"https://www.aclweb.org/portal/content/acl-rolling-review"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"}]

I found comprehensive information about ACL Rolling Review 2026 reviewer guidelines, review form criteria, and related documents. Here's what the search revealed:

## Reviewer Guidelines

Reviewers for *ACL conferences and TACL should not actively try to discover the identity of authors and should read the paper and search for related work without deliberately trying to find that particular submission. If reviewers become aware of or can guess the authors' identity, they should disclose that in the ARR review form.

Starting in May 2025, ARR adopted a policy on 'highly irresponsible' reviewers, with program chairs considering egregious cases including extremely terse reviews, unprofessional tone, and LLM-generated reviews.

## Review Form Criteria

Each submission receives at least three reviews, with the reviewer's main tasks being checking submission appropriateness, writing a well-justified review, and updating the review based on author-reviewer discussion.

The review form includes several key evaluation areas:

- Major reasons to publish the paper, which could include novel methodology, empirical results, theoretical analysis, or clear organization of literature
- Concerns about the paper including correctness, limited impact, or lack of clarity
- Excitement assessment, which is subjective and may involve transformational/innovative/surprising elements or conceptual breakthroughs
- Ethical considerations, with reviewers asked to review the ACL code of ethics and describe any ethical issues
- Reproducibility assessment of whether there is enough information to reproduce main results

## 2026 Reviewing Incentives

From 2026, ARR intends to strictly monitor adherence to reviewing responsibilities, with papers automatically desk-rejected if authors have not registered as reviewers/ACs or completed checklists by the deadline. Reviewers/ACs who remain unresponsive and don't submit on time will be prevented from accessing reviews for their own papers.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ad891ad9-83df-4d7d-953a-d24133d023e7",
  "isSidechain": false,
  "promptId": "d17f6ff5-7f93-4500-81a7-61caa2f125ae",
  "type": "user",
  "uuid": "19f4777e-8995-4f14-8474-e83a87b95e3b",
  "toolUseResult": {
    "query": "ACL Rolling Review 2026 reviewer guidelines review form criteria",
    "results": [
      {
        "tool_use_id": "srvtoolu_015jeYsXJ3aPicibLLkRx1qA",
        "content": [
          {
            "title": "Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics",
            "url": "http://aclrollingreview.org/authors"
          },
          {
            "title": "CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics",
            "url": "http://aclrollingreview.org/cfp"
          },
          {
            "title": "ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics",
            "url": "http://aclrollingreview.org/reviewerguidelines"
          },
          {
            "title": "How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics",
            "url": "http://aclrollingreview.org/reviewing"
          },
          {
            "title": "ACL Rolling Review – A peer review platform for the Association for Computational Linguistics",
            "url": "http://aclrollingreview.org/"
          },
          {
            "title": "Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics",
            "url": "http://aclrollingreview.org/reviewform"
          },
          {
            "title": "Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics",
            "url": "http://aclrollingreview.org/incentives2026"
          },
          {
            "title": "aclrollingreview/cfp.md at main · acl-org/aclrollingreview",
            "url": "https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"
          },
          {
            "title": "ACL Rolling Review | ACL Member Portal",
            "url": "https://www.aclweb.org/portal/content/acl-rolling-review"
          },
          {
            "title": "ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics",
            "url": "http://aclrollingreview.org/acguidelines"
          }
        ]
      },
      "I found comprehensive information about ACL Rolling Review 2026 reviewer guidelines, review form criteria, and related documents. Here's what the search revealed:\n\n## Reviewer Guidelines\n\nReviewers for *ACL conferences and TACL should not actively try to discover the identity of authors and should read the paper and search for related work without deliberately trying to find that particular submission. If reviewers become aware of or can guess the authors' identity, they should disclose that in the ARR review form.\n\nStarting in May 2025, ARR adopted a policy on 'highly irresponsible' reviewers, with program chairs considering egregious cases including extremely terse reviews, unprofessional tone, and LLM-generated reviews.\n\n## Review Form Criteria\n\nEach submission receives at least three reviews, with the reviewer's main tasks being checking submission appropriateness, writing a well-justified review, and updating the review based on author-reviewer discussion.\n\nThe review form includes several key evaluation areas:\n\n- Major reasons to publish the paper, which could include novel methodology, empirical results, theoretical analysis, or clear organization of literature\n- Concerns about the paper including correctness, limited impact, or lack of clarity\n- Excitement assessment, which is subjective and may involve transformational/innovative/surprising elements or conceptual breakthroughs\n- Ethical considerations, with reviewers asked to review the ACL code of ethics and describe any ethical issues\n- Reproducibility assessment of whether there is enough information to reproduce main results\n\n## 2026 Reviewing Incentives\n\nFrom 2026, ARR intends to strictly monitor adherence to reviewing responsibilities, with papers automatically desk-rejected if authors have not registered as reviewers/ACs or completed checklists by the deadline. Reviewers/ACs who remain unresponsive and don't submit on time will be prevented from accessing reviews for their own papers."
    ],
    "durationSeconds": 12.179553754999999
  },
  "sourceToolAssistantUUID": "ad891ad9-83df-4d7d-953a-d24133d023e7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/review_reviewer_1_772f066c",
  "sessionId": "e4589542-c5a3-4a5b-a779-c62f37dfeb92",
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
  "lastPrompt": "[Round 2 审稿请求]: ## Round 2 审稿任务 — Reviewer 1（方法严谨性 + 实验设计）  ### Venue 信息 - **目标**: EMNLP 2026 via ACL Rolling Review (ARR) May 2026 cycle - **Deadline**: 2026-05-25 - **页数限制**: 正文 8 页 + unlimited refe…",
  "leafUuid": "19f4777e-8995-4f14-8474-e83a87b95e3b",
  "sessionId": "e4589542-c5a3-4a5b-a779-c62f37dfeb92"
}
```

---

### Runtime record

_source line 18_

```json
{
  "type": "ai-title",
  "aiTitle": "Review Round 2 distill sparse SwiGLU paper",
  "sessionId": "e4589542-c5a3-4a5b-a779-c62f37dfeb92"
}
```

---

### Tool call

_source line 19 · 2026-05-17T04:48:02.756Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01Rj5UWqHEgsFV1jBvKUA4g6`</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract the complete review form with all scoring dimensions, their scales (1-5 etc.), and descriptions. I need the exact criteria names, score ranges, and what each score level means."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "19f4777e-8995-4f14-8474-e83a87b95e3b",
  "isSidechain": false,
  "requestId": "req_011Cb7Y2NGKvNMKun8Y2Ln8J",
  "type": "assistant",
  "uuid": "272c929b-9ef5-471e-af74-6185162f5e4e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/review_reviewer_1_772f066c",
  "sessionId": "e4589542-c5a3-4a5b-a779-c62f37dfeb92",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TcNpbp3iC9Y9YCvhbpJtno",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 402,
      "cache_creation_input_tokens": 1087,
      "cache_read_input_tokens": 29732,
      "output_tokens": 261,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1087,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 402,
          "output_tokens": 261,
          "cache_read_input_tokens": 29732,
          "cache_creation_input_tokens": 1087,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1087
          },
          "type": "message"
        }
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

_source line 20 · 2026-05-17T04:48:03.421Z_

<details open><summary>🔧 Tool call — Read · `toolu_019kdyKV2gXyMKYnXHsNsMr7`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "272c929b-9ef5-471e-af74-6185162f5e4e",
  "isSidechain": false,
  "requestId": "req_011Cb7Y2NGKvNMKun8Y2Ln8J",
  "type": "assistant",
  "uuid": "f6fa6cd5-8324-4856-addd-9b56772de453",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/review_reviewer_1_772f066c",
  "sessionId": "e4589542-c5a3-4a5b-a779-c62f37dfeb92",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TcNpbp3iC9Y9YCvhbpJtno",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 402,
      "cache_creation_input_tokens": 1087,
      "cache_read_input_tokens": 29732,
      "output_tokens": 261,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1087,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 402,
          "output_tokens": 261,
          "cache_read_input_tokens": 29732,
          "cache_creation_input_tokens": 1087,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1087
          },
          "type": "message"
        }
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

_source line 21 · 2026-05-17T04:48:03.443Z_

<details><summary>↩ Tool result · `toolu_019kdyKV2gXyMKYnXHsNsMr7`</summary>

```text
1	Activation sparsity reduces the effective computation in SwiGLU-based LLMs by pruning FFN neurons at inference, but existing learned predictors trained with binary cross-entropy (BCE) require error compensation networks due to a structural mismatch: BCE decomposes per neuron while inference uses global top-$k$ allocation across all layers.
2	We train lightweight predictors (2.37M parameters per layer, 75.9M total, $<$1\% of the base model) with KL divergence, which couples all neurons through the output distribution via Gumbel-Sigmoid relaxation, eliminating the need for compensation.
3	On LLaMA-3.1-8B (WikiText-2), our KL-trained predictor achieves perplexity 11.79 at 50\% sparsity without compensation, compared to 23.31 for vanilla TEAL and 27.97 for BCE trained at 2.71$\times$ the compute budget, whose loss saturates, confirming a structural rather than computational failure.
4	Three-seed evaluation confirms training stability (PPL $11.92 \pm 0.07$, CV${<}$1\% under uniform allocation).
5	The KL advantage grows disproportionately with sparsity: 18\% relative improvement at 30\%, 49\% at 50\%, and 82\% at 70\%.
6	Cross-architecture evaluation on Mistral-7B-v0.3 confirms the advantage transfers across SwiGLU architectures of similar scale, with consistent KL-over-TEAL ratios (within 7\% at $\leq$50\% sparsity).
7	SPON's static bias correction proves near-orthogonal to the predictor (cosine similarity 0.196), providing only 2.4\% relative PPL improvement (12.08$\to$11.79 under \texttt{evaluate.py}).
8	We propose a two-dimensional taxonomy over correction granularity $\times$ training signal coupling that unifies prior methods and identify three distinct sparsity regimes---budget-surplus, budget-constrained, and capacity-limited---that govern the quality-sparsity tradeoff.
9	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f6fa6cd5-8324-4856-addd-9b56772de453",
  "isSidechain": false,
  "promptId": "d17f6ff5-7f93-4500-81a7-61caa2f125ae",
  "type": "user",
  "uuid": "bc114893-546c-4294-af67-460cce070604",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/abstract.tex",
      "content": "Activation sparsity reduces the effective computation in SwiGLU-based LLMs by pruning FFN neurons at inference, but existing learned predictors trained with binary cross-entropy (BCE) require error compensation networks due to a structural mismatch: BCE decomposes per neuron while inference uses global top-$k$ allocation across all layers.\nWe train lightweight predictors (2.37M parameters per layer, 75.9M total, $<$1\\% of the base model) with KL divergence, which couples all neurons through the output distribution via Gumbel-Sigmoid relaxation, eliminating the need for compensation.\nOn LLaMA-3.1-8B (WikiText-2), our KL-trained predictor achieves perplexity 11.79 at 50\\% sparsity without compensation, compared to 23.31 for vanilla TEAL and 27.97 for BCE trained at 2.71$\\times$ the compute budget, whose loss saturates, confirming a structural rather than computational failure.\nThree-seed evaluation confirms training stability (PPL $11.92 \\pm 0.07$, CV${<}$1\\% under uniform allocation).\nThe KL advantage grows disproportionately with sparsity: 18\\% relative improvement at 30\\%, 49\\% at 50\\%, and 82\\% at 70\\%.\nCross-architecture evaluation on Mistral-7B-v0.3 confirms the advantage transfers across SwiGLU architectures of similar scale, with consistent KL-over-TEAL ratios (within 7\\% at $\\leq$50\\% sparsity).\nSPON's static bias correction proves near-orthogonal to the predictor (cosine similarity 0.196), providing only 2.4\\% relative PPL improvement (12.08$\\to$11.79 under \\texttt{evaluate.py}).\nWe propose a two-dimensional taxonomy over correction granularity $\\times$ training signal coupling that unifies prior methods and identify three distinct sparsity regimes---budget-surplus, budget-constrained, and capacity-limited---that govern the quality-sparsity tradeoff.\n",
      "numLines": 9,
      "startLine": 1,
      "totalLines": 9
    }
  },
  "sourceToolAssistantUUID": "f6fa6cd5-8324-4856-addd-9b56772de453",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/review_reviewer_1_772f066c",
  "sessionId": "e4589542-c5a3-4a5b-a779-c62f37dfeb92",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-17T04:48:04.568Z_

<details><summary>↩ Tool result · `toolu_01VJiTfoqmmqqgzYaYh3ZtH5`</summary>

```text
1	\section{Method}
2	\label{sec:method}
3	
4	We present a KL distillation framework for training contextual sparsity predictors in SwiGLU-based language models.
5	The method replaces per-neuron binary classification (BCE) with an output-distribution objective that couples all pruning decisions through the model's forward pass, eliminating the need for auxiliary error compensation networks at inference.
6	
7	\subsection{Problem Formulation}
8	\label{sec:method:formulation}
9	
10	Consider a pretrained transformer with $L$ layers, each containing a SwiGLU feed-forward network~\cite{shazeer2020glu}.
11	For layer $\ell$, the FFN computes:
12	\begin{align}
13	\mathbf{y}^{(\ell)} = \bigl(\sigma(\mathbf{x}^{(\ell)} \mathbf{W}_g^{(\ell)}) \odot \mathbf{x}^{(\ell)} \mathbf{W}_u^{(\ell)}\bigr) \mathbf{W}_d^{(\ell)},
14	\label{eq:swiglu}
15	\end{align}
16	where $\mathbf{x}^{(\ell)} \in \mathbb{R}^{d}$ is the hidden state after attention ($d{=}4096$), $\sigma$ denotes SiLU, $\mathbf{W}_g^{(\ell)}, \mathbf{W}_u^{(\ell)} \in \mathbb{R}^{d \times d_{\text{ff}}}$ and $\mathbf{W}_d^{(\ell)} \in \mathbb{R}^{d_{\text{ff}} \times d}$ are the gate, up-projection, and down-projection matrices, and $d_{\text{ff}}{=}14{,}336$.
17	
18	Define the gate activation $\mathbf{g}^{(\ell)} = \sigma(\mathbf{x}^{(\ell)} \mathbf{W}_g^{(\ell)}) \in \mathbb{R}^{d_{\text{ff}}}$.
19	Each element $g_j^{(\ell)}$ determines the contribution of neuron $j$ to the output.
20	We introduce a binary mask $\mathbf{m}^{(\ell)} \in \{0,1\}^{d_{\text{ff}}}$ that zeros out pruned neurons:
21	\begin{align}
22	\mathbf{y}_{\text{sparse}}^{(\ell)} = \bigl(\mathbf{m}^{(\ell)} \odot \mathbf{g}^{(\ell)} \odot \mathbf{x}^{(\ell)} \mathbf{W}_u^{(\ell)}\bigr) \mathbf{W}_d^{(\ell)}.
23	\label{eq:sparse_ffn}
24	\end{align}
25	Our goal is to learn a mask predictor $f_\theta^{(\ell)}(\mathbf{h}) \to \mathbf{s}^{(\ell)} \in (0,1)^{d_{\text{ff}}}$ that produces per-neuron importance scores from the pre-FFN hidden state $\mathbf{h}$.
26	At inference, the scores are fed to a global top-$k$ allocation mechanism~\cite{liu2025teal} that distributes the sparsity budget across layers non-uniformly, retaining the $(1{-}\rho) \times L \times d_{\text{ff}}$ highest-scoring neurons model-wide for a target sparsity ratio $\rho$.
27	
28	
29	\subsection{Predictor Architecture}
30	\label{sec:method:predictor}
31	
32	Each layer $\ell$ has an independent two-layer MLP predictor:
33	\begin{align}
34	f_\theta^{(\ell)}(\mathbf{h}) = \text{GELU}(\mathbf{h} \mathbf{W}_1^{(\ell)}) \, \mathbf{W}_2^{(\ell)},
35	\label{eq:predictor}
36	\end{align}
37	where $\mathbf{W}_1^{(\ell)} \in \mathbb{R}^{d \times d_b}$ and $\mathbf{W}_2^{(\ell)} \in \mathbb{R}^{d_b \times d_{\text{ff}}}$ with bottleneck dimension $d_b{=}128$.
38	The predictor takes the hidden state after attention (before the FFN) and outputs $d_{\text{ff}}$-dimensional logits $\mathbf{s}^{(\ell)}$, from which the mask is derived.
39	
40	Each predictor has $(4096 \times 128) + (128 \times 14336) = 2.37\text{M}$ parameters.
41	With 32 independent predictors (one per layer), the total overhead is 75.9M parameters---less than 1\% of the 8B base model.
42	The predictors operate independently across layers, requiring no cross-layer communication at inference.
43	
44	
45	\subsection{Gumbel-Sigmoid Relaxation}
46	\label{sec:method:gumbel}
47	
48	The hard mask $m_j = \mathbf{1}[s_j > \text{threshold}]$ is non-differentiable, preventing gradient flow from the KL objective through the mask to the predictor parameters.
49	We apply Gumbel-Sigmoid relaxation~\cite{jang2017gumbel} to produce differentiable soft masks:
50	\begin{align}
51	\tilde{m}_j = \sigma_\tau\!\left(\log \frac{s_j}{1 - s_j} + g_1 - g_2\right), \quad g_1, g_2 \sim \text{Gumbel}(0,1),
52	\label{eq:gumbel}
53	\end{align}
54	where $\sigma_\tau(x) = \text{sigmoid}(x / \tau)$ and $\tau$ is a temperature parameter.
55	The Gumbel noise provides stochastic exploration of mask configurations during training, while the temperature controls sharpness: as $\tau \to 0$, $\tilde{m}_j$ approaches a binary decision.
56	
57	We anneal $\tau$ linearly from 1.0 to 0.1 over training.
58	At high temperature, the soft mask permits gradient flow through all neurons, enabling broad exploration.
59	As temperature decreases, the mask concentrates on confident decisions, approximating the hard allocation used at inference.
60	
61	\paragraph{Comparison with Straight-Through Estimation.}
62	The straight-through estimator (STE)~\cite{bengio2013ste} applies a hard threshold in the forward pass and passes gradients through unchanged ($\partial m / \partial s = 1$).
63	In our setting, STE produces discontinuous gradient signals: small parameter changes can flip many neurons simultaneously, causing violent oscillations in the Lagrangian multiplier and failure to converge to the target sparsity.
64	Gumbel relaxation eliminates this pathology, contributing a 34.5\% improvement (PPL 15.77 $\to$ 11.79 at 50\% sparsity), as we verify empirically in \S\ref{sec:experiments}.
65	
66	
67	\subsection{KL Divergence Training Objective}
68	\label{sec:method:kl}
69	
70	Let $\mathbf{z}_{\text{dense}}$ denote the output logits from a full dense forward pass, and $\mathbf{z}_{\text{sparse}}$ the logits from a forward pass with predictor-generated soft masks $\{\tilde{\mathbf{m}}^{(\ell)}\}_\ell$ applied at every layer.
71	We minimize the forward KL divergence between the dense and sparse output distributions:
72	\begin{align}
73	\mathcal{L}_{\text{KL}} = D_{\text{KL}}(p_{\text{dense}} \,\|\, p_{\text{sparse}}) = \sum_{v} p_{\text{dense}}^{(v)} \log \frac{p_{\text{dense}}^{(v)}}{p_{\text{sparse}}^{(v)}},
74	\label{eq:kl_loss}
75	\end{align}
76	where $p_{\text{dense}} = \text{softmax}(\mathbf{z}_{\text{dense}})$ and $p_{\text{sparse}} = \text{softmax}(\mathbf{z}_{\text{sparse}})$, summed over the vocabulary $v$ and averaged over sequence positions.
77	The base model is frozen; only the predictor parameters receive gradients.
78	
79	We use forward KL ($D_{\text{KL}}(p_{\text{dense}} \| p_{\text{sparse}})$) rather than reverse KL ($D_{\text{KL}}(p_{\text{sparse}} \| p_{\text{dense}})$).
80	Forward KL is mean-seeking: it penalizes the sparse model heavily wherever the dense model assigns high probability, forcing the sparse distribution to cover the dense model's primary predictions.
81	This is appropriate for sparsity prediction, where the goal is to preserve the dense model's top-token behavior rather than explore alternative modes.
82	No temperature scaling ($T{=}1$) is applied, following the finding that logit-level distillation without temperature is sufficient when the student retains the teacher's architecture~\cite{hinton2015distilling}.
83	
84	
85	\subsection{Lagrangian Sparsity Constraint}
86	\label{sec:method:lagrangian}
87	
88	We enforce a model-level sparsity target $\rho$ via constrained optimization.
89	Let $\bar{s} = \frac{1}{L} \sum_\ell \frac{1}{d_{\text{ff}}} \sum_j \tilde{m}_j^{(\ell)}$ denote the average fraction of retained neurons.
90	The constrained problem is:
91	\begin{align}
92	\min_\theta \; \mathcal{L}_{\text{KL}} \quad \text{s.t.} \quad \bar{s} \leq 1 - \rho.
93	\label{eq:constrained}
94	\end{align}
95	We relax this via a penalty with an adaptive multiplicative dual variable controller:
96	\begin{align}
97	\mathcal{L} = \mathcal{L}_{\text{KL}} + \lambda \cdot \text{clamp}(|\bar{s} - (1 - \rho)| - \epsilon, \min{=}0)^2,
98	\label{eq:lagrangian}
99	\end{align}
100	where $\epsilon = 0.02$ is a deadzone margin that prevents $\lambda$ from responding to small constraint violations.
101	The dual variable $\lambda$ is updated multiplicatively at each step:
102	\begin{align}
103	\lambda \leftarrow \begin{cases} \lambda \times 2 & \text{if } \bar{s} > (1-\rho) + \epsilon \\ \lambda \times 0.5 & \text{if } \bar{s} < (1-\rho) - \epsilon \\ \lambda & \text{otherwise} \end{cases}
104	\label{eq:dual_update}
105	\end{align}
106	with $\lambda$ clamped to $[\lambda_{\text{floor}}, \lambda_{\max}]$ where $\lambda_{\text{floor}} = 0.01$ and $\lambda_{\max} \in \{1000, 5000\}$ depending on the target.
107	The geometric doubling enables rapid adaptation ($\sim$10 steps to reach steady state) while the deadzone prevents unnecessary oscillation when sparsity is within $\pm$2\% of the target.
108	Convergence analysis across all sparsity targets is in Appendix~\ref{app:lagrangian}.
109	
110	
111	\subsection{Gradient-Based Motivation: BCE vs.\ KL}
112	\label{sec:method:gradient}
113	
114	We analyze the structural difference between BCE and KL training signals to motivate why KL distillation is better suited to global top-$k$ inference.
115	
116	\paragraph{BCE gradient structure.}
117	The standard approach trains the predictor against oracle masks $m_j^* = \mathbf{1}[|g_j| \geq \text{top-}k\text{ threshold}]$ derived from the dense model's activation magnitudes.
118	The loss decomposes per neuron:
119	\begin{align}
120	\mathcal{L}_{\text{BCE}} = -\frac{1}{d_{\text{ff}}} \sum_{j=1}^{d_{\text{ff}}} \bigl[ m_j^* \log \sigma(s_j) + (1 - m_j^*) \log(1 - \sigma(s_j)) \bigr].
121	\label{eq:bce}
122	\end{align}
123	The gradient with respect to predictor logit $s_j$ is:
124	\begin{align}
125	\frac{\partial \mathcal{L}_{\text{BCE}}}{\partial s_j} = \sigma(s_j) - m_j^*.
126	\label{eq:bce_grad}
127	\end{align}
128	This gradient depends \emph{only} on neuron $j$'s own prediction and target.
129	Each neuron is trained independently---there is no inter-neuron coupling in the learning signal.
130	
131	\paragraph{KL gradient structure.}
132	Under KL distillation, the gradient for predictor logit $s_j^{(\ell)}$ in layer $\ell$ is:
133	\begin{align}
134	\frac{\partial \mathcal{L}_{\text{KL}}}{\partial s_j^{(\ell)}} = \underbrace{\frac{\partial \mathcal{L}_{\text{KL}}}{\partial \mathbf{z}_{\text{sparse}}}}_{\text{(a)}} \cdot \underbrace{\frac{\partial \mathbf{z}_{\text{sparse}}}{\partial \mathbf{h}^{(\ell)}}}_{\text{(b)}} \cdot \underbrace{\frac{\partial \mathbf{h}^{(\ell)}}{\partial \tilde{m}_j^{(\ell)}}}_{\text{(c)}} \cdot \underbrace{\frac{\partial \tilde{m}_j^{(\ell)}}{\partial s_j^{(\ell)}}}_{\text{(d)}},
135	\label{eq:kl_grad}
136	\end{align}
137	where each factor has a distinct role:
138	\begin{itemize}
139	\item[\textbf{(a)}] The KL gradient at the output, reflecting how each logit component deviates from the dense distribution.
140	\item[\textbf{(b)}] The Jacobian through all downstream layers from layer $\ell$'s output to the final logits. This factor couples neuron $j$'s gradient to the state of every other retained neuron in layers $\ell, \ell{+}1, \ldots, L$, because the sparse hidden state propagates through subsequent attention and FFN operations.
141	\item[\textbf{(c)}] The effect of mask element $\tilde{m}_j^{(\ell)}$ on the layer output: $\partial \mathbf{h}^{(\ell)} / \partial \tilde{m}_j^{(\ell)} = (g_j^{(\ell)} \cdot [\mathbf{x}^{(\ell)} \mathbf{W}_u^{(\ell)}]_j) \cdot \mathbf{W}_{d,j}^{(\ell)}$, where $\mathbf{W}_{d,j}^{(\ell)}$ is column $j$ of the down-projection. The down-projection linearly mixes all neurons' contributions, so changing $\tilde{m}_j$ affects the full $d$-dimensional hidden state.
142	\item[\textbf{(d)}] The Gumbel-Sigmoid derivative, providing the differentiable path from logit to mask.
143	\end{itemize}
144	
145	\paragraph{The structural mismatch.}
146	The key observation is that factor (b) makes the KL gradient for neuron $j$ depend on \emph{all} other neurons' mask values.
147	BCE's factorized gradient (Eq.~\ref{eq:bce_grad}) optimizes each neuron's prediction accuracy in isolation, but TEAL inference selects neurons via a global ranking across all layers.
148	Under global top-$k$, the decision to retain neuron $j$ depends on the scores of all other neurons---a combinatorial interaction that BCE cannot capture.
149	
150	Concretely, BCE achieves high per-neuron accuracy ($>$90\% oracle agreement) yet produces poor output under TEAL, because it optimizes a proxy misaligned with output preservation under global budget allocation.
151	KL directly optimizes the end-to-end objective, with gradients that reflect inter-neuron dependencies through the computation graph.
152	
153	\paragraph{Empirical verification.}
154	Measuring gradient SNR over 80 steps on LLaMA-3.1-8B (C4 calibration data), KL achieves $5.76\times$ higher average SNR than BCE ($5.77{\times}10^{-5}$ vs.\ $1.00{\times}10^{-5}$).
155	The advantage concentrates in early layers (0--4: ratio $34$--$156\times$) where factor~(b)'s Jacobian chain traverses the full remaining network; late layers (27--31) show only $2$--$4\times$ as the shorter chain reduces factor~(b)'s contribution.
156	BCE's early-layer SNR collapses to ${\sim}10^{-8}$ after step~10, explaining why extended training cannot close the gap.
157	
158	\subsection{Two-Dimensional Taxonomy of Sparsity Prediction Methods}
159	\label{sec:method:taxonomy}
160	
161	We organize prior work along two axes: \emph{correction granularity} (how the mask adapts to input) and \emph{training signal coupling} (whether the objective captures inter-neuron dependencies).
162	
163	\begin{table}[t]
164	\centering
165	\caption{Taxonomy of learned sparsity prediction methods. Rows indicate correction granularity; columns indicate training signal coupling. Our method fills a previously unexplored cell.}
166	\label{tab:taxonomy}
167	\resizebox{\columnwidth}{!}{
168	\begin{tabular}{lccc}
169	\toprule
170	 & Decomposed (BCE) & Intermediate (MSE) & Coupled (KL) \\
171	\midrule
172	Static & --- & --- & SPON \\
173	Per-layer & --- & ShadowLLM & --- \\
174	Per-token & FastForward & --- & \textbf{Ours} \\
175	\bottomrule
176	\end{tabular}}
177	\end{table}
178	
179	\paragraph{Correction granularity.}
180	\emph{Static} methods~\cite{xu2026spon} learn a fixed bias vector per layer that does not depend on the input token.
181	\emph{Per-layer} methods~\cite{akhauri2024shadowllm} condition on a layer-level summary (e.g., the attention output) but share predictions across tokens within a layer.
182	\emph{Per-token} methods~\cite{gautam2026fastforward,liu2023dejavu} produce a unique mask for each input position.
183	
184	\paragraph{Training signal coupling.}
185	\emph{Decomposed} objectives (BCE) treat each neuron independently, optimizing per-element classification against an oracle mask.
186	\emph{Intermediate} objectives (MSE on hidden states) capture local coupling within a single layer but not end-to-end output effects.
187	\emph{Coupled} objectives (KL on output distribution) propagate gradients through the full forward pass, reflecting how all mask decisions jointly affect the final distribution.
188	
189	SPON~\cite{xu2026spon} operates at the intersection of static granularity and coupled training: it distills a per-layer bias correction via KL but cannot adapt to per-input neuron importance.
190	FastForward~\cite{gautam2026fastforward} achieves per-token granularity but uses BCE training, losing inter-neuron coupling.
191	Our method combines per-token contextual prediction with coupled KL training (Table~\ref{tab:taxonomy}), unifying the advantages of both axes: input-dependent mask generation trained with a signal that captures global neuron interactions through the output distribution.
192	
193	\begin{figure}[t]
194	\centering
195	\includegraphics[width=\columnwidth]{fig1_overview.pdf}
196	\caption{Method overview: a lightweight per-layer predictor produces importance scores trained via KL divergence with Gumbel-Sigmoid relaxation. At inference, scores feed TEAL's global top-$k$ allocation without compensation networks.}
197	\label{fig:taxonomy}
198	\end{figure}
199	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5d798b53-d070-4d9b-9b2d-8e1bb12a2fea",
  "isSidechain": false,
  "promptId": "d17f6ff5-7f93-4500-81a7-61caa2f125ae",
  "type": "user",
  "uuid": "b5dc03d6-283b-4a9e-9e76-2de59840fcd4",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/method.tex",
      "content": "\\section{Method}\n\\label{sec:method}\n\nWe present a KL distillation framework for training contextual sparsity predictors in SwiGLU-based language models.\nThe method replaces per-neuron binary classification (BCE) with an output-distribution objective that couples all pruning decisions through the model's forward pass, eliminating the need for auxiliary error compensation networks at inference.\n\n\\subsection{Problem Formulation}\n\\label{sec:method:formulation}\n\nConsider a pretrained transformer with $L$ layers, each containing a SwiGLU feed-forward network~\\cite{shazeer2020glu}.\nFor layer $\\ell$, the FFN computes:\n\\begin{align}\n\\mathbf{y}^{(\\ell)} = \\bigl(\\sigma(\\mathbf{x}^{(\\ell)} \\mathbf{W}_g^{(\\ell)}) \\odot \\mathbf{x}^{(\\ell)} \\mathbf{W}_u^{(\\ell)}\\bigr) \\mathbf{W}_d^{(\\ell)},\n\\label{eq:swiglu}\n\\end{align}\nwhere $\\mathbf{x}^{(\\ell)} \\in \\mathbb{R}^{d}$ is the hidden state after attention ($d{=}4096$), $\\sigma$ denotes SiLU, $\\mathbf{W}_g^{(\\ell)}, \\mathbf{W}_u^{(\\ell)} \\in \\mathbb{R}^{d \\times d_{\\text{ff}}}$ and $\\mathbf{W}_d^{(\\ell)} \\in \\mathbb{R}^{d_{\\text{ff}} \\times d}$ are the gate, up-projection, and down-projection matrices, and $d_{\\text{ff}}{=}14{,}336$.\n\nDefine the gate activation $\\mathbf{g}^{(\\ell)} = \\sigma(\\mathbf{x}^{(\\ell)} \\mathbf{W}_g^{(\\ell)}) \\in \\mathbb{R}^{d_{\\text{ff}}}$.\nEach element $g_j^{(\\ell)}$ determines the contribution of neuron $j$ to the output.\nWe introduce a binary mask $\\mathbf{m}^{(\\ell)} \\in \\{0,1\\}^{d_{\\text{ff}}}$ that zeros out pruned neurons:\n\\begin{align}\n\\mathbf{y}_{\\text{sparse}}^{(\\ell)} = \\bigl(\\mathbf{m}^{(\\ell)} \\odot \\mathbf{g}^{(\\ell)} \\odot \\mathbf{x}^{(\\ell)} \\mathbf{W}_u^{(\\ell)}\\bigr) \\mathbf{W}_d^{(\\ell)}.\n\\label{eq:sparse_ffn}\n\\end{align}\nOur goal is to learn a mask predictor $f_\\theta^{(\\ell)}(\\mathbf{h}) \\to \\mathbf{s}^{(\\ell)} \\in (0,1)^{d_{\\text{ff}}}$ that produces per-neuron importance scores from the pre-FFN hidden state $\\mathbf{h}$.\nAt inference, the scores are fed to a global top-$k$ allocation mechanism~\\cite{liu2025teal} that distributes the sparsity budget across layers non-uniformly, retaining the $(1{-}\\rho) \\times L \\times d_{\\text{ff}}$ highest-scoring neurons model-wide for a target sparsity ratio $\\rho$.\n\n\n\\subsection{Predictor Architecture}\n\\label{sec:method:predictor}\n\nEach layer $\\ell$ has an independent two-layer MLP predictor:\n\\begin{align}\nf_\\theta^{(\\ell)}(\\mathbf{h}) = \\text{GELU}(\\mathbf{h} \\mathbf{W}_1^{(\\ell)}) \\, \\mathbf{W}_2^{(\\ell)},\n\\label{eq:predictor}\n\\end{align}\nwhere $\\mathbf{W}_1^{(\\ell)} \\in \\mathbb{R}^{d \\times d_b}$ and $\\mathbf{W}_2^{(\\ell)} \\in \\mathbb{R}^{d_b \\times d_{\\text{ff}}}$ with bottleneck dimension $d_b{=}128$.\nThe predictor takes the hidden state after attention (before the FFN) and outputs $d_{\\text{ff}}$-dimensional logits $\\mathbf{s}^{(\\ell)}$, from which the mask is derived.\n\nEach predictor has $(4096 \\times 128) + (128 \\times 14336) = 2.37\\text{M}$ parameters.\nWith 32 independent predictors (one per layer), the total overhead is 75.9M parameters---less than 1\\% of the 8B base model.\nThe predictors operate independently across layers, requiring no cross-layer communication at inference.\n\n\n\\subsection{Gumbel-Sigmoid Relaxation}\n\\label{sec:method:gumbel}\n\nThe hard mask $m_j = \\mathbf{1}[s_j > \\text{threshold}]$ is non-differentiable, preventing gradient flow from the KL objective through the mask to the predictor parameters.\nWe apply Gumbel-Sigmoid relaxation~\\cite{jang2017gumbel} to produce differentiable soft masks:\n\\begin{align}\n\\tilde{m}_j = \\sigma_\\tau\\!\\left(\\log \\frac{s_j}{1 - s_j} + g_1 - g_2\\right), \\quad g_1, g_2 \\sim \\text{Gumbel}(0,1),\n\\label{eq:gumbel}\n\\end{align}\nwhere $\\sigma_\\tau(x) = \\text{sigmoid}(x / \\tau)$ and $\\tau$ is a temperature parameter.\nThe Gumbel noise provides stochastic exploration of mask configurations during training, while the temperature controls sharpness: as $\\tau \\to 0$, $\\tilde{m}_j$ approaches a binary decision.\n\nWe anneal $\\tau$ linearly from 1.0 to 0.1 over training.\nAt high temperature, the soft mask permits gradient flow through all neurons, enabling broad exploration.\nAs temperature decreases, the mask concentrates on confident decisions, approximating the hard allocation used at inference.\n\n\\paragraph{Comparison with Straight-Through Estimation.}\nThe straight-through estimator (STE)~\\cite{bengio2013ste} applies a hard threshold in the forward pass and passes gradients through unchanged ($\\partial m / \\partial s = 1$).\nIn our setting, STE produces discontinuous gradient signals: small parameter changes can flip many neurons simultaneously, causing violent oscillations in the Lagrangian multiplier and failure to converge to the target sparsity.\nGumbel relaxation eliminates this pathology, contributing a 34.5\\% improvement (PPL 15.77 $\\to$ 11.79 at 50\\% sparsity), as we verify empirically in \\S\\ref{sec:experiments}.\n\n\n\\subsection{KL Divergence Training Objective}\n\\label{sec:method:kl}\n\nLet $\\mathbf{z}_{\\text{dense}}$ denote the output logits from a full dense forward pass, and $\\mathbf{z}_{\\text{sparse}}$ the logits from a forward pass with predictor-generated soft masks $\\{\\tilde{\\mathbf{m}}^{(\\ell)}\\}_\\ell$ applied at every layer.\nWe minimize the forward KL divergence between the dense and sparse output distributions:\n\\begin{align}\n\\mathcal{L}_{\\text{KL}} = D_{\\text{KL}}(p_{\\text{dense}} \\,\\|\\, p_{\\text{sparse}}) = \\sum_{v} p_{\\text{dense}}^{(v)} \\log \\frac{p_{\\text{dense}}^{(v)}}{p_{\\text{sparse}}^{(v)}},\n\\label{eq:kl_loss}\n\\end{align}\nwhere $p_{\\text{dense}} = \\text{softmax}(\\mathbf{z}_{\\text{dense}})$ and $p_{\\text{sparse}} = \\text{softmax}(\\mathbf{z}_{\\text{sparse}})$, summed over the vocabulary $v$ and averaged over sequence positions.\nThe base model is frozen; only the predictor parameters receive gradients.\n\nWe use forward KL ($D_{\\text{KL}}(p_{\\text{dense}} \\| p_{\\text{sparse}})$) rather than reverse KL ($D_{\\text{KL}}(p_{\\text{sparse}} \\| p_{\\text{dense}})$).\nForward KL is mean-seeking: it penalizes the sparse model heavily wherever the dense model assigns high probability, forcing the sparse distribution to cover the dense model's primary predictions.\nThis is appropriate for sparsity prediction, where the goal is to preserve the dense model's top-token behavior rather than explore alternative modes.\nNo temperature scaling ($T{=}1$) is applied, following the finding that logit-level distillation without temperature is sufficient when the student retains the teacher's architecture~\\cite{hinton2015distilling}.\n\n\n\\subsection{Lagrangian Sparsity Constraint}\n\\label{sec:method:lagrangian}\n\nWe enforce a model-level sparsity target $\\rho$ via constrained optimization.\nLet $\\bar{s} = \\frac{1}{L} \\sum_\\ell \\frac{1}{d_{\\text{ff}}} \\sum_j \\tilde{m}_j^{(\\ell)}$ denote the average fraction of retained neurons.\nThe constrained problem is:\n\\begin{align}\n\\min_\\theta \\; \\mathcal{L}_{\\text{KL}} \\quad \\text{s.t.} \\quad \\bar{s} \\leq 1 - \\rho.\n\\label{eq:constrained}\n\\end{align}\nWe relax this via a penalty with an adaptive multiplicative dual variable controller:\n\\begin{align}\n\\mathcal{L} = \\mathcal{L}_{\\text{KL}} + \\lambda \\cdot \\text{clamp}(|\\bar{s} - (1 - \\rho)| - \\epsilon, \\min{=}0)^2,\n\\label{eq:lagrangian}\n\\end{align}\nwhere $\\epsilon = 0.02$ is a deadzone margin that prevents $\\lambda$ from responding to small constraint violations.\nThe dual variable $\\lambda$ is updated multiplicatively at each step:\n\\begin{align}\n\\lambda \\leftarrow \\begin{cases} \\lambda \\times 2 & \\text{if } \\bar{s} > (1-\\rho) + \\epsilon \\\\ \\lambda \\times 0.5 & \\text{if } \\bar{s} < (1-\\rho) - \\epsilon \\\\ \\lambda & \\text{otherwise} \\end{cases}\n\\label{eq:dual_update}\n\\end{align}\nwith $\\lambda$ clamped to $[\\lambda_{\\text{floor}}, \\lambda_{\\max}]$ where $\\lambda_{\\text{floor}} = 0.01$ and $\\lambda_{\\max} \\in \\{1000, 5000\\}$ depending on the target.\nThe geometric doubling enables rapid adaptation ($\\sim$10 steps to reach steady state) while the deadzone prevents unnecessary oscillation when sparsity is within $\\pm$2\\% of the target.\nConvergence analysis across all sparsity targets is in Appendix~\\ref{app:lagrangian}.\n\n\n\\subsection{Gradient-Based Motivation: BCE vs.\\ KL}\n\\label{sec:method:gradient}\n\nWe analyze the structural difference between BCE and KL training signals to motivate why KL distillation is better suited to global top-$k$ inference.\n\n\\paragraph{BCE gradient structure.}\nThe standard approach trains the predictor against oracle masks $m_j^* = \\mathbf{1}[|g_j| \\geq \\text{top-}k\\text{ threshold}]$ derived from the dense model's activation magnitudes.\nThe loss decomposes per neuron:\n\\begin{align}\n\\mathcal{L}_{\\text{BCE}} = -\\frac{1}{d_{\\text{ff}}} \\sum_{j=1}^{d_{\\text{ff}}} \\bigl[ m_j^* \\log \\sigma(s_j) + (1 - m_j^*) \\log(1 - \\sigma(s_j)) \\bigr].\n\\label{eq:bce}\n\\end{align}\nThe gradient with respect to predictor logit $s_j$ is:\n\\begin{align}\n\\frac{\\partial \\mathcal{L}_{\\text{BCE}}}{\\partial s_j} = \\sigma(s_j) - m_j^*.\n\\label{eq:bce_grad}\n\\end{align}\nThis gradient depends \\emph{only} on neuron $j$'s own prediction and target.\nEach neuron is trained independently---there is no inter-neuron coupling in the learning signal.\n\n\\paragraph{KL gradient structure.}\nUnder KL distillation, the gradient for predictor logit $s_j^{(\\ell)}$ in layer $\\ell$ is:\n\\begin{align}\n\\frac{\\partial \\mathcal{L}_{\\text{KL}}}{\\partial s_j^{(\\ell)}} = \\underbrace{\\frac{\\partial \\mathcal{L}_{\\text{KL}}}{\\partial \\mathbf{z}_{\\text{sparse}}}}_{\\text{(a)}} \\cdot \\underbrace{\\frac{\\partial \\mathbf{z}_{\\text{sparse}}}{\\partial \\mathbf{h}^{(\\ell)}}}_{\\text{(b)}} \\cdot \\underbrace{\\frac{\\partial \\mathbf{h}^{(\\ell)}}{\\partial \\tilde{m}_j^{(\\ell)}}}_{\\text{(c)}} \\cdot \\underbrace{\\frac{\\partial \\tilde{m}_j^{(\\ell)}}{\\partial s_j^{(\\ell)}}}_{\\text{(d)}},\n\\label{eq:kl_grad}\n\\end{align}\nwhere each factor has a distinct role:\n\\begin{itemize}\n\\item[\\textbf{(a)}] The KL gradient at the output, reflecting how each logit component deviates from the dense distribution.\n\\item[\\textbf{(b)}] The Jacobian through all downstream layers from layer $\\ell$'s output to the final logits. This factor couples neuron $j$'s gradient to the state of every other retained neuron in layers $\\ell, \\ell{+}1, \\ldots, L$, because the sparse hidden state propagates through subsequent attention and FFN operations.\n\\item[\\textbf{(c)}] The effect of mask element $\\tilde{m}_j^{(\\ell)}$ on the layer output: $\\partial \\mathbf{h}^{(\\ell)} / \\partial \\tilde{m}_j^{(\\ell)} = (g_j^{(\\ell)} \\cdot [\\mathbf{x}^{(\\ell)} \\mathbf{W}_u^{(\\ell)}]_j) \\cdot \\mathbf{W}_{d,j}^{(\\ell)}$, where $\\mathbf{W}_{d,j}^{(\\ell)}$ is column $j$ of the down-projection. The down-projection linearly mixes all neurons' contributions, so changing $\\tilde{m}_j$ affects the full $d$-dimensional hidden state.\n\\item[\\textbf{(d)}] The Gumbel-Sigmoid derivative, providing the differentiable path from logit to mask.\n\\end{itemize}\n\n\\paragraph{The structural mismatch.}\nThe key observation is that factor (b) makes the KL gradient for neuron $j$ depend on \\emph{all} other neurons' mask values.\nBCE's factorized gradient (Eq.~\\ref{eq:bce_grad}) optimizes each neuron's prediction accuracy in isolation, but TEAL inference selects neurons via a global ranking across all layers.\nUnder global top-$k$, the decision to retain neuron $j$ depends on the scores of all other neurons---a combinatorial interaction that BCE cannot capture.\n\nConcretely, BCE achieves high per-neuron accuracy ($>$90\\% oracle agreement) yet produces poor output under TEAL, because it optimizes a proxy misaligned with output preservation under global budget allocation.\nKL directly optimizes the end-to-end objective, with gradients that reflect inter-neuron dependencies through the computation graph.\n\n\\paragraph{Empirical verification.}\nMeasuring gradient SNR over 80 steps on LLaMA-3.1-8B (C4 calibration data), KL achieves $5.76\\times$ higher average SNR than BCE ($5.77{\\times}10^{-5}$ vs.\\ $1.00{\\times}10^{-5}$).\nThe advantage concentrates in early layers (0--4: ratio $34$--$156\\times$) where factor~(b)'s Jacobian chain traverses the full remaining network; late layers (27--31) show only $2$--$4\\times$ as the shorter chain reduces factor~(b)'s contribution.\nBCE's early-layer SNR collapses to ${\\sim}10^{-8}$ after step~10, explaining why extended training cannot close the gap.\n\n\\subsection{Two-Dimensional Taxonomy of Sparsity Prediction Methods}\n\\label{sec:method:taxonomy}\n\nWe organize prior work along two axes: \\emph{correction granularity} (how the mask adapts to input) and \\emph{training signal coupling} (whether the objective captures inter-neuron dependencies).\n\n\\begin{table}[t]\n\\centering\n\\caption{Taxonomy of learned sparsity prediction methods. Rows indicate correction granularity; columns indicate training signal coupling. Our method fills a previously unexplored cell.}\n\\label{tab:taxonomy}\n\\resizebox{\\columnwidth}{!}{\n\\begin{tabular}{lccc}\n\\toprule\n & Decomposed (BCE) & Intermediate (MSE) & Coupled (KL) \\\\\n\\midrule\nStatic & --- & --- & SPON \\\\\nPer-layer & --- & ShadowLLM & --- \\\\\nPer-token & FastForward & --- & \\textbf{Ours} \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\n\\paragraph{Correction granularity.}\n\\emph{Static} methods~\\cite{xu2026spon} learn a fixed bias vector per layer that does not depend on the input token.\n\\emph{Per-layer} methods~\\cite{akhauri2024shadowllm} condition on a layer-level summary (e.g., the attention output) but share predictions across tokens within a layer.\n\\emph{Per-token} methods~\\cite{gautam2026fastforward,liu2023dejavu} produce a unique mask for each input position.\n\n\\paragraph{Training signal coupling.}\n\\emph{Decomposed} objectives (BCE) treat each neuron independently, optimizing per-element classification against an oracle mask.\n\\emph{Intermediate} objectives (MSE on hidden states) capture local coupling within a single layer but not end-to-end output effects.\n\\emph{Coupled} objectives (KL on output distribution) propagate gradients through the full forward pass, reflecting how all mask decisions jointly affect the final distribution.\n\nSPON~\\cite{xu2026spon} operates at the intersection of static granularity and coupled training: it distills a per-layer bias correction via KL but cannot adapt to per-input neuron importance.\nFastForward~\\cite{gautam2026fastforward} achieves per-token granularity but uses BCE training, losing inter-neuron coupling.\nOur method combines per-token contextual prediction with coupled KL training (Table~\\ref{tab:taxonomy}), unifying the advantages of both axes: input-dependent mask generation trained with a signal that captures global neuron interactions through the output distribution.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{fig1_overview.pdf}\n\\caption{Method overview: a lightweight per-layer predictor produces importance scores trained via KL divergence with Gumbel-Sigmoid relaxation. At inference, scores feed TEAL's global top-$k$ allocation without compensation networks.}\n\\label{fig:taxonomy}\n\\end{figure}\n",
      "numLines": 199,
      "startLine": 1,
      "totalLines": 199
    }
  },
  "sourceToolAssistantUUID": "5d798b53-d070-4d9b-9b2d-8e1bb12a2fea",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/review_reviewer_1_772f066c",
  "sessionId": "e4589542-c5a3-4a5b-a779-c62f37dfeb92",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-17T04:48:04.562Z_

<details open><summary>🔧 Tool call — Read · `toolu_01VJiTfoqmmqqgzYaYh3ZtH5`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bc114893-546c-4294-af67-460cce070604",
  "isSidechain": false,
  "requestId": "req_011Cb7Y2NGKvNMKun8Y2Ln8J",
  "type": "assistant",
  "uuid": "5d798b53-d070-4d9b-9b2d-8e1bb12a2fea",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/review_reviewer_1_772f066c",
  "sessionId": "e4589542-c5a3-4a5b-a779-c62f37dfeb92",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TcNpbp3iC9Y9YCvhbpJtno",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 402,
      "cache_creation_input_tokens": 1087,
      "cache_read_input_tokens": 29732,
      "output_tokens": 261,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1087,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 402,
          "output_tokens": 261,
          "cache_read_input_tokens": 29732,
          "cache_creation_input_tokens": 1087,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1087
          },
          "type": "message"
        }
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

_source line 24_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[Round 2 审稿请求]: ## Round 2 审稿任务 — Reviewer 1（方法严谨性 + 实验设计）  ### Venue 信息 - **目标**: EMNLP 2026 via ACL Rolling Review (ARR) May 2026 cycle - **Deadline**: 2026-05-25 - **页数限制**: 正文 8 页 + unlimited refe…",
  "leafUuid": "b5dc03d6-283b-4a9e-9e76-2de59840fcd4",
  "sessionId": "e4589542-c5a3-4a5b-a779-c62f37dfeb92"
}
```

---

### Runtime record

_source line 25_

```json
{
  "type": "ai-title",
  "aiTitle": "Review Round 2 distill sparse SwiGLU paper",
  "sessionId": "e4589542-c5a3-4a5b-a779-c62f37dfeb92"
}
```

---

### Tool result

_source line 26 · 2026-05-17T04:48:07.508Z_

<details><summary>↩ Tool result · `toolu_01Rj5UWqHEgsFV1jBvKUA4g6`</summary>

```text
# ACL Rolling Review Form - Scoring Dimensions

## 1. **Reviewer Confidence** (1-5 scale)
- **5**: "Positive that my evaluation is correct"
- **4**: "Quite sure" with unlikely but possible errors
- **3**: "Pretty sure" but chance of missing details
- **2**: "Willing to defend" but likely gaps in understanding
- **1**: "Not my area" or highly unclear paper

## 2. **Soundness** (1-5 scale with .5 increments)
- **5**: Exceptionally thorough research for its type
- **4**: Adequate support for claims; extra experiments optional
- **3**: Main claims sufficiently supported with minor gaps
- **2**: Insufficient support; major technical problems
- **1**: Insufficient rigor or not relevant to ACL

## 3. **Excitement** (1-5 scale with .5 increments)
- **5**: "Highly Exciting" - would recommend widely
- **4**: "Exciting" - would mention to others
- **3**: "Interesting" - might discuss selectively
- **2**: "Potentially Interesting" - limited personal resonance
- **1**: "Not Exciting" - lacks community relevance

## 4. **Overall Assessment** (1-5 scale with .5 increments)
- **5**: Consider for award consideration
- **4**: Conference acceptance
- **3**: Findings track acceptance
- **2**: Needs revision by next cycle
- **1**: Reject or not ACL-relevant
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "272c929b-9ef5-471e-af74-6185162f5e4e",
  "isSidechain": false,
  "promptId": "d17f6ff5-7f93-4500-81a7-61caa2f125ae",
  "type": "user",
  "uuid": "f6cda3e4-2117-45d6-852f-d10667a03f76",
  "toolUseResult": {
    "bytes": 25365,
    "code": 200,
    "codeText": "OK",
    "result": "# ACL Rolling Review Form - Scoring Dimensions\n\n## 1. **Reviewer Confidence** (1-5 scale)\n- **5**: \"Positive that my evaluation is correct\"\n- **4**: \"Quite sure\" with unlikely but possible errors\n- **3**: \"Pretty sure\" but chance of missing details\n- **2**: \"Willing to defend\" but likely gaps in understanding\n- **1**: \"Not my area\" or highly unclear paper\n\n## 2. **Soundness** (1-5 scale with .5 increments)\n- **5**: Exceptionally thorough research for its type\n- **4**: Adequate support for claims; extra experiments optional\n- **3**: Main claims sufficiently supported with minor gaps\n- **2**: Insufficient support; major technical problems\n- **1**: Insufficient rigor or not relevant to ACL\n\n## 3. **Excitement** (1-5 scale with .5 increments)\n- **5**: \"Highly Exciting\" - would recommend widely\n- **4**: \"Exciting\" - would mention to others\n- **3**: \"Interesting\" - might discuss selectively\n- **2**: \"Potentially Interesting\" - limited personal resonance\n- **1**: \"Not Exciting\" - lacks community relevance\n\n## 4. **Overall Assessment** (1-5 scale with .5 increments)\n- **5**: Consider for award consideration\n- **4**: Conference acceptance\n- **3**: Findings track acceptance\n- **2**: Needs revision by next cycle\n- **1**: Reject or not ACL-relevant",
    "durationMs": 4745,
    "url": "https://aclrollingreview.org/reviewform"
  },
  "sourceToolAssistantUUID": "272c929b-9ef5-471e-af74-6185162f5e4e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/review_reviewer_1_772f066c",
  "sessionId": "e4589542-c5a3-4a5b-a779-c62f37dfeb92",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-17T04:48:11.791Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Qawa85eAdBvp5vuRY6aDXa`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f6cda3e4-2117-45d6-852f-d10667a03f76",
  "isSidechain": false,
  "requestId": "req_011Cb7Y32F65JCSzUjAH7NPn",
  "type": "assistant",
  "uuid": "7035771c-4af4-44e5-b4fb-f21e7ed050cd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/review_reviewer_1_772f066c",
  "sessionId": "e4589542-c5a3-4a5b-a779-c62f37dfeb92",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KkHZHeh3i4ShZNd2zi3CuC",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6120,
      "cache_creation_input_tokens": 1053,
      "cache_read_input_tokens": 30819,
      "output_tokens": 160,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1053,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 6120,
          "output_tokens": 160,
          "cache_read_input_tokens": 30819,
          "cache_creation_input_tokens": 1053,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1053
          },
          "type": "message"
        }
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

_source line 28 · 2026-05-17T04:48:11.799Z_

<details><summary>↩ Tool result · `toolu_01Qawa85eAdBvp5vuRY6aDXa`</summary>

```text
1	\section{Experiments}
2	\label{sec:experiments}
3	
4	\subsection{Experimental Setup}
5	
6	\paragraph{Model and Predictor.}
7	We evaluate on LLaMA-3.1-8B~\cite{grattafiori2024llama3}, which uses SwiGLU FFN blocks~\cite{shazeer2020glu} with $d_{\text{model}}=4096$ and $d_{\text{ff}}=14336$ across 32 layers.
8	The sparsity predictor is a two-layer MLP with 2.37M parameters per layer (75.9M total), implemented as Linear($4096 \to 128$) + GELU + Linear($128 \to 14336$), trained to produce per-neuron importance scores that minimize output-distribution divergence under sparsity.
9	
10	\paragraph{Training.}
11	All predictors are trained for 1000 steps on WikiText-103 with sequence length 2048 and batch size 4, using AdamW with learning rate $1 \times 10^{-3}$ and cosine decay.
12	The KL predictor uses Gumbel-Sigmoid relaxation~\cite{jang2017gumbel} with temperature $\tau=1.0$ annealed to $0.1$ over training.
13	
14	\paragraph{Evaluation.}
15	We report perplexity on WikiText-2~\cite{merity2017pointer} (seq\_len=2048) and downstream accuracy on ARC-Challenge (25-shot), WinoGrande (5-shot), MMLU (5-shot), and GSM8K (8-shot).
16	
17	\paragraph{Inference Protocol.}
18	At inference, the predictor produces per-neuron scores that are passed to TEAL's global top-$k$ allocation mechanism~\cite{liu2025teal}, which distributes the sparsity budget across layers non-uniformly.
19	We term this \textit{predictor-TEAL}: the predictor replaces TEAL's magnitude-based scoring while retaining its allocation strategy.
20	
21	\paragraph{Baselines.}
22	We compare against: (1) \textbf{Vanilla TEAL}~\cite{liu2025teal}, which uses activation magnitudes directly; (2) \textbf{BCE predictor}, trained with per-neuron binary cross-entropy loss for 1000 and 2700 steps; (3) \textbf{Uniform allocation}, which distributes the sparsity budget equally across layers; and (4) \textbf{WINA}~\cite{liu2025teal}, an importance-weighted variant.
23	
24	
25	\subsection{Main Results}
26	
27	Table~\ref{tab:main} presents the primary comparison across sparsity levels.
28	At 30\% sparsity, KL distillation with global TEAL allocation achieves PPL 8.98, reducing TEAL's degradation from dense (10.97 $\to$ 8.98, an 18\% improvement). % exp_id: kl_30_global_teal
29	Uniform allocation at 30\% recovers MMLU to 40.61\% (+15.3pp over KL-global's 25.27\%), indicating that at low sparsity, global top-$k$ starves knowledge-critical layers and uniform budget prevents this. % exp_id: bench_kl30_uniform
30	
31	At 50\% sparsity, KL distillation over vanilla TEAL widens the PPL advantage: 11.79 vs.\ 23.31, a 49\% reduction. % exp_id: bench_kl50_global, bench_teal50
32	The predictor also generalizes to out-of-domain text (C4 validation: 52.5\% advantage over TEAL; see Appendix~\ref{app:ood}).
33	However, all methods exhibit downstream collapse on MMLU (27.89\% vs.\ 27.77\% for global vs.\ uniform, both $\approx$ random) and GSM8K ($<$2.2\%), indicating a capacity-limited regime where no allocation strategy can recover. % exp_id: bench_kl50_global, d030_kl50_uniform
34	
35	\begin{table}[t]
36	\centering
37	\caption{Main results on LLaMA-3.1-8B. PPL$\downarrow$ on WikiText-2; accuracy$\uparrow$ on downstream tasks. \textbf{Bold}: best among compensation-free methods per sparsity level. BCE uses a different inference protocol (hard mask + compensation network). Multi-seed variance (3 seeds, 50\% uniform): PPL std=0.07; see Appendix~\ref{app:stability}.}
38	\label{tab:main}
39	\resizebox{\columnwidth}{!}{
40	\begin{tabular}{llccccc}
41	\toprule
42	Sparsity & Method & PPL$\downarrow$ & ARC-c & WG & MMLU & GSM8K \\
43	\midrule
44	0\% & Dense & 6.12 & 58.28 & 78.06 & 65.27 & 48.75 \\
45	\midrule
46	\multirow{3}{*}{30\%}
47	& TEAL vanilla & 10.97 & \textbf{42.32} & 66.06 & 38.61 & 7.88 \\ % exp_id: bench_teal30
48	& KL global (Ours) & 8.98 & 39.68 & \textbf{70.17} & 25.27 & \textbf{8.79} \\ % exp_id: lm_eval_kl_30pct_s42
49	& KL uniform & \textbf{8.82} & 40.78 & 68.59 & \textbf{40.61} & 7.35 \\ % exp_id: bench_kl30_uniform
50	\midrule
51	\multirow{4}{*}{50\%}
52	& TEAL vanilla & 23.31 & 28.41 & 53.04 & \textbf{28.32} & 1.97 \\ % exp_id: bench_teal50
53	& KL global (Ours) & \textbf{11.79} & \textbf{32.85} & \textbf{63.46} & 27.89 & 1.29 \\ % exp_id: bench_kl50_global
54	& KL uniform & 11.96 & 32.76 & 62.90 & 27.77 & \textbf{2.12} \\ % exp_id: d030_kl50_uniform
55	& BCE (2700 steps)$^\ast$ & 27.97 & 23.98 & 50.59 & 30.02 & 4.85 \\ % exp_id: eval_bce_v3_s42
56	\bottomrule
57	\end{tabular}}
58	\end{table}
59	
60	
61	\subsection{Iso-Compute Analysis}
62	\label{sec:isocompute}
63	
64	To test whether BCE simply requires more compute, we train it for 2700 steps (2.71$\times$ the KL budget).
65	The BCE predictor achieves PPL 27.97, still 2.37$\times$ worse than KL at 1000 steps (PPL 11.79). % exp_id: bce_isocompute_s42
66	The failure is structural: BCE's factorized objective cannot learn inter-neuron correlations required for global top-$k$ allocation.
67	Training loss saturates between steps 500 and 2700 ($\Delta = -0.006$), confirming diminishing returns under the wrong objective.
68	
69	
70	\subsection{Ablation Studies}
71	
72	Table~\ref{tab:ablation} isolates the contribution of each design choice at 50\% sparsity.
73	
74	\begin{table}[t]
75	\centering
76	\caption{Ablation at 50\% sparsity on LLaMA-3.1-8B (WikiText-2 PPL$\downarrow$, unified benchmark protocol).}
77	\label{tab:ablation}
78	\small
79	\begin{tabular}{lcc}
80	\toprule
81	Configuration & PPL$\downarrow$ & $\Delta$ from Ours \\
82	\midrule
83	\multicolumn{3}{l}{\textit{KL-based variants}} \\
84	KL + Gumbel (Ours) & \textbf{11.79} & --- \\ % exp_id: bench_kl50_global
85	KL + STE & 15.77 & +3.98 \\ % exp_id: ste_baseline_s42
86	\midrule
87	\multicolumn{3}{l}{\textit{BCE-based variants}} \\
88	BCE + Compensation (hard mask) & 25.44 & +13.65 \\ % exp_id: bce_comp_staged_s42
89	BCE (no compensation) & 27.97 & +16.18 \\ % exp_id: eval_bce_v3_s42
90	BCE + Gumbel + Lagrangian (no KL) & 38.02 & +26.23 \\ % exp_id: bce_gumbel_lagrangian_isolation
91	\bottomrule
92	\end{tabular}
93	\end{table}
94	
95	\paragraph{Gumbel vs.\ STE.}
96	Replacing Gumbel-Sigmoid with STE~\cite{bengio2013ste} degrades PPL from 11.79 to 15.77 (+3.98), accounting for 34.5\% of the improvement over vanilla TEAL. % exp_id: ste_baseline_s42
97	
98	\paragraph{SPON Contribution.}
99	Adding SPON~\cite{xu2026spon} bias correction reduces PPL from 12.08 to 11.79 (2.4\% relative) under the \texttt{evaluate.py} protocol;\footnote{SPON analysis uses \texttt{evaluate.py}; main results use the unified benchmark. The coincidental 11.79 in both does not imply equivalence.} see \S\ref{sec:spon} for decomposition analysis. % exp_id: spon_2048_s42, mvp_kl_norm_v2_s42
100	
101	\paragraph{Loss Function Isolation.}
102	Training BCE with identical Gumbel-Sigmoid sampling and Lagrangian enforcement yields PPL 38.02 (best of 3 LR sweeps), worse than vanilla BCE (27.97): the Lagrangian penalty interferes with per-neuron optimization when the loss cannot coordinate neurons globally. % exp_id: bce_gumbel_lagrangian_isolation
103	The loss function's effect ($\Delta$PPL=26.23) is $6.6\times$ larger than the relaxation method's ($\Delta$PPL=3.98), confirming distribution-level supervision as the decisive factor.
104	
105	\paragraph{BCE + Compensation.}
106	Compensation improves BCE from 27.97 to 25.44 (9.0\% relative) under a hard-mask protocol, still 2.16$\times$ worse than KL under TEAL. % exp_id: bce_comp_staged_s42
107	
108	\paragraph{Hyperparameter Robustness.}
109	Additional ablations in Appendix~\ref{app:db_sensitivity} confirm robustness to predictor capacity ($d_b$, $<$3\%), temperature schedule ($<$1.8\%), and training duration (saturated by 800 steps). % exp_id: db_sensitivity_sweep, tau_schedule_sweep, training_steps_sweep
110	
111	
112	\subsection{Sparsity Scaling and Regime Analysis}
113	\label{sec:scaling}
114	
115	Table~\ref{tab:scaling} and Figure~\ref{fig:sparsity_sweep} show PPL as a function of sparsity for KL-predictor-TEAL and vanilla TEAL.
116	
117	\begin{figure}[t]
118	\centering
119	\includegraphics[width=\columnwidth]{fig2_sparsity_sweep.pdf}
120	\caption{Perplexity scaling with sparsity. The KL predictor's advantage grows disproportionately as more neurons are pruned.}
121	\label{fig:sparsity_sweep}
122	\end{figure}
123	
124	\begin{table}[t]
125	\centering
126	\caption{PPL scaling with sparsity (WikiText-2). KL advantage grows disproportionately with sparsity.}
127	\label{tab:scaling}
128	\small
129	\begin{tabular}{lccc}
130	\toprule
131	Sparsity & KL (Ours) & TEAL vanilla & Relative advantage \\
132	\midrule
133	30\% & \textbf{8.98} & 10.97 & 18\% \\ % exp_id: kl_30_global_teal
134	50\% & \textbf{11.79} & 23.31 & 49\% \\ % exp_id: bench_kl50_global
135	70\% & \textbf{17.91} & 100.11 & 82\% \\ % exp_id: kl_70_global_teal
136	\bottomrule
137	\end{tabular}
138	\end{table}
139	
140	The KL advantage grows from 18\% at 30\% to 82\% at 70\%, where TEAL collapses (PPL 100.11) while the learned predictor maintains coherent allocation.
141	
142	\paragraph{Three Regimes: Allocation vs.\ Capacity.}
143	Table~\ref{tab:phase} presents global vs.\ uniform allocation at three sparsity levels, revealing qualitative regime shifts.
144	
145	\begin{table}[t]
146	\centering
147	\caption{Allocation analysis: global (TEAL) vs.\ uniform per-layer allocation across sparsity levels. \textbf{Bold}: best per column within each sparsity group (compensation-free). Each row uses a predictor trained at the respective sparsity target.}
148	\label{tab:phase}
149	\resizebox{\columnwidth}{!}{
150	\begin{tabular}{llccccc}
151	\toprule
152	Sparsity & Allocation & PPL$\downarrow$ & ARC-c & WG & MMLU & GSM8K \\
153	\midrule
154	0\% & Dense & 6.12 & 58.28 & 78.06 & 65.27 & 48.75 \\
155	\midrule
156	\multirow{3}{*}{30\%}
157	& TEAL vanilla & 10.97 & \textbf{42.32} & 66.06 & 38.61 & 7.88 \\ % exp_id: bench_teal30
158	& KL global & 8.98 & 39.68 & \textbf{70.17} & 25.27 & \textbf{8.79} \\ % exp_id: lm_eval_kl_30pct_s42
159	& KL uniform & \textbf{8.82} & 40.78 & 68.59 & \textbf{40.61} & 7.35 \\ % exp_id: bench_kl30_uniform
160	\midrule
161	\multirow{2}{*}{40\%}
162	& KL global & 10.12 & 40.96 & 65.35 & \textbf{38.06} & \textbf{5.00} \\ % exp_id: bench_kl40_global
163	& KL uniform & \textbf{8.36} & \textbf{41.81} & \textbf{67.17} & 30.68 & 3.94 \\ % exp_id: d030_kl40_uniform
164	\midrule
165	\multirow{3}{*}{50\%}
166	& TEAL vanilla & 23.31 & 28.41 & 53.04 & \textbf{28.32} & 1.97 \\ % exp_id: bench_teal50
167	& KL global & \textbf{11.79} & \textbf{32.85} & \textbf{63.46} & 27.89 & 1.29 \\ % exp_id: bench_kl50_global
168	& KL uniform & 11.96 & 32.76 & 62.90 & 27.77 & \textbf{2.12} \\ % exp_id: d030_kl50_uniform
169	\bottomrule
170	\end{tabular}}
171	\end{table}
172	
173	The allocation preference is \emph{non-monotonic} across sparsity levels, revealing three distinct regimes:
174	
175	\noindent\textbf{Budget-surplus ($\leq$30\%).}
176	Uniform allocation recovers MMLU from 25.27\% to 40.61\% (+15.3pp); global top-$k$ starves knowledge-critical layers when the budget is ample. % exp_id: bench_kl30_uniform, lm_eval_kl_30pct_s42
177	
178	\noindent\textbf{Budget-constrained ($\sim$40\%).}
179	The preference reverses: global achieves MMLU 38.06\% vs.\ uniform's 30.68\% (+7.4pp). % exp_id: bench_kl40_global, d030_kl40_uniform
180	PPL remains low (8.36) but downstream accuracy degrades, confirming PPL is a poor proxy for reasoning.
181	
182	\noindent\textbf{Capacity-limited ($\geq$50\%).}
183	Global/uniform gap vanishes (MMLU 27.89\% vs.\ 27.77\%, both $\approx$ random). % exp_id: bench_kl50_global, d030_kl50_uniform
184	This regime boundary is confirmed on both architectures (\S\ref{sec:cross_arch}); exact boundaries may shift with model scale.
185	
186	
187	\subsection{SPON Orthogonality Analysis}
188	\label{sec:spon}
189	
190	At 50\% sparsity, the predictor's hidden-state perturbation (L2=482.65) and SPON's additive correction (L2=76.2, cosine similarity 0.196) are near-orthogonal; SPON yields only 2.4\% PPL improvement (12.08$\to$11.79), confirming the KL predictor already captures most recoverable signal. % exp_id: spon_decomposition, spon_2048_s42, mvp_kl_norm_v2_s42
191	
192	\paragraph{Cross-Architecture Validation.}
193	\label{sec:cross_arch}
194	Table~\ref{tab:cross_arch} evaluates on Mistral-7B-v0.3~\cite{jiang2023mistral} (GQA + sliding window, dense PPL 5.52).
195	
196	\begin{table}[t]
197	\centering
198	\caption{Cross-architecture comparison (WikiText-2 PPL$\downarrow$). Adv = TEAL / KL.}
199	\label{tab:cross_arch}
200	\small
201	\begin{tabular}{l@{\hspace{4pt}}cc@{\hspace{3pt}}c@{\hspace{6pt}}|@{\hspace{6pt}}cc@{\hspace{3pt}}c}
202	\toprule
203	 & \multicolumn{3}{c}{Mistral-7B} & \multicolumn{3}{c}{LLaMA-8B} \\
204	 & KL & TEAL & Adv & KL & TEAL & Adv \\
205	\midrule
206	30\% & \textbf{6.77} & 8.38 & 1.24$\times$ & \textbf{8.98} & 10.97 & 1.22$\times$ \\ % exp_id: kl_30_mistral, teal_30_mistral
207	50\% & \textbf{8.65} & 18.31 & 2.12$\times$ & \textbf{11.79} & 23.31 & 1.98$\times$ \\ % exp_id: kl_50_mistral, teal_50_mistral
208	70\% & \textbf{13.33} & 61.72 & 4.63$\times$ & \textbf{17.91} & 100.11 & 5.59$\times$ \\ % exp_id: kl_70_mistral, teal_70_mistral
209	\bottomrule
210	\end{tabular}
211	\end{table}
212	
213	The KL advantage ratio scales consistently across architectures (within 7\% at $\leq$50\% sparsity); the pattern persists at 70\% with larger variance (4.63$\times$ vs.\ 5.59$\times$) due to differential baseline collapse.
214	Mistral's TEAL baseline is uniformly stronger (its gate distribution favors magnitude pruning), yet the KL-over-TEAL ratio remains consistent, indicating the advantage stems from modeling inter-neuron dependencies rather than exploiting a specific model's redundancy.
215	This consistency across different training distributions and weight configurations provides evidence that the method exploits a structural property of SwiGLU networks.
216	
217	
218	\paragraph{Inference Efficiency.}
219	The pipeline adds 6.4\% overhead to dense inference while eliminating the compensation network ($-$2.7\% latency, $-$67.2M params); see Appendix~\ref{app:latency}.
220	
221	\paragraph{Training Stability.}
222	Three-seed evaluation (50\% uniform): PPL $11.92 \pm 0.07$ (CV$<$1\%); see Appendix~\ref{app:stability}.
223	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7035771c-4af4-44e5-b4fb-f21e7ed050cd",
  "isSidechain": false,
  "promptId": "d17f6ff5-7f93-4500-81a7-61caa2f125ae",
  "type": "user",
  "uuid": "d5dc06e7-1b53-4c41-aa95-0d825e08ab34",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/experiments.tex",
      "content": "\\section{Experiments}\n\\label{sec:experiments}\n\n\\subsection{Experimental Setup}\n\n\\paragraph{Model and Predictor.}\nWe evaluate on LLaMA-3.1-8B~\\cite{grattafiori2024llama3}, which uses SwiGLU FFN blocks~\\cite{shazeer2020glu} with $d_{\\text{model}}=4096$ and $d_{\\text{ff}}=14336$ across 32 layers.\nThe sparsity predictor is a two-layer MLP with 2.37M parameters per layer (75.9M total), implemented as Linear($4096 \\to 128$) + GELU + Linear($128 \\to 14336$), trained to produce per-neuron importance scores that minimize output-distribution divergence under sparsity.\n\n\\paragraph{Training.}\nAll predictors are trained for 1000 steps on WikiText-103 with sequence length 2048 and batch size 4, using AdamW with learning rate $1 \\times 10^{-3}$ and cosine decay.\nThe KL predictor uses Gumbel-Sigmoid relaxation~\\cite{jang2017gumbel} with temperature $\\tau=1.0$ annealed to $0.1$ over training.\n\n\\paragraph{Evaluation.}\nWe report perplexity on WikiText-2~\\cite{merity2017pointer} (seq\\_len=2048) and downstream accuracy on ARC-Challenge (25-shot), WinoGrande (5-shot), MMLU (5-shot), and GSM8K (8-shot).\n\n\\paragraph{Inference Protocol.}\nAt inference, the predictor produces per-neuron scores that are passed to TEAL's global top-$k$ allocation mechanism~\\cite{liu2025teal}, which distributes the sparsity budget across layers non-uniformly.\nWe term this \\textit{predictor-TEAL}: the predictor replaces TEAL's magnitude-based scoring while retaining its allocation strategy.\n\n\\paragraph{Baselines.}\nWe compare against: (1) \\textbf{Vanilla TEAL}~\\cite{liu2025teal}, which uses activation magnitudes directly; (2) \\textbf{BCE predictor}, trained with per-neuron binary cross-entropy loss for 1000 and 2700 steps; (3) \\textbf{Uniform allocation}, which distributes the sparsity budget equally across layers; and (4) \\textbf{WINA}~\\cite{liu2025teal}, an importance-weighted variant.\n\n\n\\subsection{Main Results}\n\nTable~\\ref{tab:main} presents the primary comparison across sparsity levels.\nAt 30\\% sparsity, KL distillation with global TEAL allocation achieves PPL 8.98, reducing TEAL's degradation from dense (10.97 $\\to$ 8.98, an 18\\% improvement). % exp_id: kl_30_global_teal\nUniform allocation at 30\\% recovers MMLU to 40.61\\% (+15.3pp over KL-global's 25.27\\%), indicating that at low sparsity, global top-$k$ starves knowledge-critical layers and uniform budget prevents this. % exp_id: bench_kl30_uniform\n\nAt 50\\% sparsity, KL distillation over vanilla TEAL widens the PPL advantage: 11.79 vs.\\ 23.31, a 49\\% reduction. % exp_id: bench_kl50_global, bench_teal50\nThe predictor also generalizes to out-of-domain text (C4 validation: 52.5\\% advantage over TEAL; see Appendix~\\ref{app:ood}).\nHowever, all methods exhibit downstream collapse on MMLU (27.89\\% vs.\\ 27.77\\% for global vs.\\ uniform, both $\\approx$ random) and GSM8K ($<$2.2\\%), indicating a capacity-limited regime where no allocation strategy can recover. % exp_id: bench_kl50_global, d030_kl50_uniform\n\n\\begin{table}[t]\n\\centering\n\\caption{Main results on LLaMA-3.1-8B. PPL$\\downarrow$ on WikiText-2; accuracy$\\uparrow$ on downstream tasks. \\textbf{Bold}: best among compensation-free methods per sparsity level. BCE uses a different inference protocol (hard mask + compensation network). Multi-seed variance (3 seeds, 50\\% uniform): PPL std=0.07; see Appendix~\\ref{app:stability}.}\n\\label{tab:main}\n\\resizebox{\\columnwidth}{!}{\n\\begin{tabular}{llccccc}\n\\toprule\nSparsity & Method & PPL$\\downarrow$ & ARC-c & WG & MMLU & GSM8K \\\\\n\\midrule\n0\\% & Dense & 6.12 & 58.28 & 78.06 & 65.27 & 48.75 \\\\\n\\midrule\n\\multirow{3}{*}{30\\%}\n& TEAL vanilla & 10.97 & \\textbf{42.32} & 66.06 & 38.61 & 7.88 \\\\ % exp_id: bench_teal30\n& KL global (Ours) & 8.98 & 39.68 & \\textbf{70.17} & 25.27 & \\textbf{8.79} \\\\ % exp_id: lm_eval_kl_30pct_s42\n& KL uniform & \\textbf{8.82} & 40.78 & 68.59 & \\textbf{40.61} & 7.35 \\\\ % exp_id: bench_kl30_uniform\n\\midrule\n\\multirow{4}{*}{50\\%}\n& TEAL vanilla & 23.31 & 28.41 & 53.04 & \\textbf{28.32} & 1.97 \\\\ % exp_id: bench_teal50\n& KL global (Ours) & \\textbf{11.79} & \\textbf{32.85} & \\textbf{63.46} & 27.89 & 1.29 \\\\ % exp_id: bench_kl50_global\n& KL uniform & 11.96 & 32.76 & 62.90 & 27.77 & \\textbf{2.12} \\\\ % exp_id: d030_kl50_uniform\n& BCE (2700 steps)$^\\ast$ & 27.97 & 23.98 & 50.59 & 30.02 & 4.85 \\\\ % exp_id: eval_bce_v3_s42\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\n\n\\subsection{Iso-Compute Analysis}\n\\label{sec:isocompute}\n\nTo test whether BCE simply requires more compute, we train it for 2700 steps (2.71$\\times$ the KL budget).\nThe BCE predictor achieves PPL 27.97, still 2.37$\\times$ worse than KL at 1000 steps (PPL 11.79). % exp_id: bce_isocompute_s42\nThe failure is structural: BCE's factorized objective cannot learn inter-neuron correlations required for global top-$k$ allocation.\nTraining loss saturates between steps 500 and 2700 ($\\Delta = -0.006$), confirming diminishing returns under the wrong objective.\n\n\n\\subsection{Ablation Studies}\n\nTable~\\ref{tab:ablation} isolates the contribution of each design choice at 50\\% sparsity.\n\n\\begin{table}[t]\n\\centering\n\\caption{Ablation at 50\\% sparsity on LLaMA-3.1-8B (WikiText-2 PPL$\\downarrow$, unified benchmark protocol).}\n\\label{tab:ablation}\n\\small\n\\begin{tabular}{lcc}\n\\toprule\nConfiguration & PPL$\\downarrow$ & $\\Delta$ from Ours \\\\\n\\midrule\n\\multicolumn{3}{l}{\\textit{KL-based variants}} \\\\\nKL + Gumbel (Ours) & \\textbf{11.79} & --- \\\\ % exp_id: bench_kl50_global\nKL + STE & 15.77 & +3.98 \\\\ % exp_id: ste_baseline_s42\n\\midrule\n\\multicolumn{3}{l}{\\textit{BCE-based variants}} \\\\\nBCE + Compensation (hard mask) & 25.44 & +13.65 \\\\ % exp_id: bce_comp_staged_s42\nBCE (no compensation) & 27.97 & +16.18 \\\\ % exp_id: eval_bce_v3_s42\nBCE + Gumbel + Lagrangian (no KL) & 38.02 & +26.23 \\\\ % exp_id: bce_gumbel_lagrangian_isolation\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Gumbel vs.\\ STE.}\nReplacing Gumbel-Sigmoid with STE~\\cite{bengio2013ste} degrades PPL from 11.79 to 15.77 (+3.98), accounting for 34.5\\% of the improvement over vanilla TEAL. % exp_id: ste_baseline_s42\n\n\\paragraph{SPON Contribution.}\nAdding SPON~\\cite{xu2026spon} bias correction reduces PPL from 12.08 to 11.79 (2.4\\% relative) under the \\texttt{evaluate.py} protocol;\\footnote{SPON analysis uses \\texttt{evaluate.py}; main results use the unified benchmark. The coincidental 11.79 in both does not imply equivalence.} see \\S\\ref{sec:spon} for decomposition analysis. % exp_id: spon_2048_s42, mvp_kl_norm_v2_s42\n\n\\paragraph{Loss Function Isolation.}\nTraining BCE with identical Gumbel-Sigmoid sampling and Lagrangian enforcement yields PPL 38.02 (best of 3 LR sweeps), worse than vanilla BCE (27.97): the Lagrangian penalty interferes with per-neuron optimization when the loss cannot coordinate neurons globally. % exp_id: bce_gumbel_lagrangian_isolation\nThe loss function's effect ($\\Delta$PPL=26.23) is $6.6\\times$ larger than the relaxation method's ($\\Delta$PPL=3.98), confirming distribution-level supervision as the decisive factor.\n\n\\paragraph{BCE + Compensation.}\nCompensation improves BCE from 27.97 to 25.44 (9.0\\% relative) under a hard-mask protocol, still 2.16$\\times$ worse than KL under TEAL. % exp_id: bce_comp_staged_s42\n\n\\paragraph{Hyperparameter Robustness.}\nAdditional ablations in Appendix~\\ref{app:db_sensitivity} confirm robustness to predictor capacity ($d_b$, $<$3\\%), temperature schedule ($<$1.8\\%), and training duration (saturated by 800 steps). % exp_id: db_sensitivity_sweep, tau_schedule_sweep, training_steps_sweep\n\n\n\\subsection{Sparsity Scaling and Regime Analysis}\n\\label{sec:scaling}\n\nTable~\\ref{tab:scaling} and Figure~\\ref{fig:sparsity_sweep} show PPL as a function of sparsity for KL-predictor-TEAL and vanilla TEAL.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{fig2_sparsity_sweep.pdf}\n\\caption{Perplexity scaling with sparsity. The KL predictor's advantage grows disproportionately as more neurons are pruned.}\n\\label{fig:sparsity_sweep}\n\\end{figure}\n\n\\begin{table}[t]\n\\centering\n\\caption{PPL scaling with sparsity (WikiText-2). KL advantage grows disproportionately with sparsity.}\n\\label{tab:scaling}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\nSparsity & KL (Ours) & TEAL vanilla & Relative advantage \\\\\n\\midrule\n30\\% & \\textbf{8.98} & 10.97 & 18\\% \\\\ % exp_id: kl_30_global_teal\n50\\% & \\textbf{11.79} & 23.31 & 49\\% \\\\ % exp_id: bench_kl50_global\n70\\% & \\textbf{17.91} & 100.11 & 82\\% \\\\ % exp_id: kl_70_global_teal\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe KL advantage grows from 18\\% at 30\\% to 82\\% at 70\\%, where TEAL collapses (PPL 100.11) while the learned predictor maintains coherent allocation.\n\n\\paragraph{Three Regimes: Allocation vs.\\ Capacity.}\nTable~\\ref{tab:phase} presents global vs.\\ uniform allocation at three sparsity levels, revealing qualitative regime shifts.\n\n\\begin{table}[t]\n\\centering\n\\caption{Allocation analysis: global (TEAL) vs.\\ uniform per-layer allocation across sparsity levels. \\textbf{Bold}: best per column within each sparsity group (compensation-free). Each row uses a predictor trained at the respective sparsity target.}\n\\label{tab:phase}\n\\resizebox{\\columnwidth}{!}{\n\\begin{tabular}{llccccc}\n\\toprule\nSparsity & Allocation & PPL$\\downarrow$ & ARC-c & WG & MMLU & GSM8K \\\\\n\\midrule\n0\\% & Dense & 6.12 & 58.28 & 78.06 & 65.27 & 48.75 \\\\\n\\midrule\n\\multirow{3}{*}{30\\%}\n& TEAL vanilla & 10.97 & \\textbf{42.32} & 66.06 & 38.61 & 7.88 \\\\ % exp_id: bench_teal30\n& KL global & 8.98 & 39.68 & \\textbf{70.17} & 25.27 & \\textbf{8.79} \\\\ % exp_id: lm_eval_kl_30pct_s42\n& KL uniform & \\textbf{8.82} & 40.78 & 68.59 & \\textbf{40.61} & 7.35 \\\\ % exp_id: bench_kl30_uniform\n\\midrule\n\\multirow{2}{*}{40\\%}\n& KL global & 10.12 & 40.96 & 65.35 & \\textbf{38.06} & \\textbf{5.00} \\\\ % exp_id: bench_kl40_global\n& KL uniform & \\textbf{8.36} & \\textbf{41.81} & \\textbf{67.17} & 30.68 & 3.94 \\\\ % exp_id: d030_kl40_uniform\n\\midrule\n\\multirow{3}{*}{50\\%}\n& TEAL vanilla & 23.31 & 28.41 & 53.04 & \\textbf{28.32} & 1.97 \\\\ % exp_id: bench_teal50\n& KL global & \\textbf{11.79} & \\textbf{32.85} & \\textbf{63.46} & 27.89 & 1.29 \\\\ % exp_id: bench_kl50_global\n& KL uniform & 11.96 & 32.76 & 62.90 & 27.77 & \\textbf{2.12} \\\\ % exp_id: d030_kl50_uniform\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\nThe allocation preference is \\emph{non-monotonic} across sparsity levels, revealing three distinct regimes:\n\n\\noindent\\textbf{Budget-surplus ($\\leq$30\\%).}\nUniform allocation recovers MMLU from 25.27\\% to 40.61\\% (+15.3pp); global top-$k$ starves knowledge-critical layers when the budget is ample. % exp_id: bench_kl30_uniform, lm_eval_kl_30pct_s42\n\n\\noindent\\textbf{Budget-constrained ($\\sim$40\\%).}\nThe preference reverses: global achieves MMLU 38.06\\% vs.\\ uniform's 30.68\\% (+7.4pp). % exp_id: bench_kl40_global, d030_kl40_uniform\nPPL remains low (8.36) but downstream accuracy degrades, confirming PPL is a poor proxy for reasoning.\n\n\\noindent\\textbf{Capacity-limited ($\\geq$50\\%).}\nGlobal/uniform gap vanishes (MMLU 27.89\\% vs.\\ 27.77\\%, both $\\approx$ random). % exp_id: bench_kl50_global, d030_kl50_uniform\nThis regime boundary is confirmed on both architectures (\\S\\ref{sec:cross_arch}); exact boundaries may shift with model scale.\n\n\n\\subsection{SPON Orthogonality Analysis}\n\\label{sec:spon}\n\nAt 50\\% sparsity, the predictor's hidden-state perturbation (L2=482.65) and SPON's additive correction (L2=76.2, cosine similarity 0.196) are near-orthogonal; SPON yields only 2.4\\% PPL improvement (12.08$\\to$11.79), confirming the KL predictor already captures most recoverable signal. % exp_id: spon_decomposition, spon_2048_s42, mvp_kl_norm_v2_s42\n\n\\paragraph{Cross-Architecture Validation.}\n\\label{sec:cross_arch}\nTable~\\ref{tab:cross_arch} evaluates on Mistral-7B-v0.3~\\cite{jiang2023mistral} (GQA + sliding window, dense PPL 5.52).\n\n\\begin{table}[t]\n\\centering\n\\caption{Cross-architecture comparison (WikiText-2 PPL$\\downarrow$). Adv = TEAL / KL.}\n\\label{tab:cross_arch}\n\\small\n\\begin{tabular}{l@{\\hspace{4pt}}cc@{\\hspace{3pt}}c@{\\hspace{6pt}}|@{\\hspace{6pt}}cc@{\\hspace{3pt}}c}\n\\toprule\n & \\multicolumn{3}{c}{Mistral-7B} & \\multicolumn{3}{c}{LLaMA-8B} \\\\\n & KL & TEAL & Adv & KL & TEAL & Adv \\\\\n\\midrule\n30\\% & \\textbf{6.77} & 8.38 & 1.24$\\times$ & \\textbf{8.98} & 10.97 & 1.22$\\times$ \\\\ % exp_id: kl_30_mistral, teal_30_mistral\n50\\% & \\textbf{8.65} & 18.31 & 2.12$\\times$ & \\textbf{11.79} & 23.31 & 1.98$\\times$ \\\\ % exp_id: kl_50_mistral, teal_50_mistral\n70\\% & \\textbf{13.33} & 61.72 & 4.63$\\times$ & \\textbf{17.91} & 100.11 & 5.59$\\times$ \\\\ % exp_id: kl_70_mistral, teal_70_mistral\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe KL advantage ratio scales consistently across architectures (within 7\\% at $\\leq$50\\% sparsity); the pattern persists at 70\\% with larger variance (4.63$\\times$ vs.\\ 5.59$\\times$) due to differential baseline collapse.\nMistral's TEAL baseline is uniformly stronger (its gate distribution favors magnitude pruning), yet the KL-over-TEAL ratio remains consistent, indicating the advantage stems from modeling inter-neuron dependencies rather than exploiting a specific model's redundancy.\nThis consistency across different training distributions and weight configurations provides evidence that the method exploits a structural property of SwiGLU networks.\n\n\n\\paragraph{Inference Efficiency.}\nThe pipeline adds 6.4\\% overhead to dense inference while eliminating the compensation network ($-$2.7\\% latency, $-$67.2M params); see Appendix~\\ref{app:latency}.\n\n\\paragraph{Training Stability.}\nThree-seed evaluation (50\\% uniform): PPL $11.92 \\pm 0.07$ (CV$<$1\\%); see Appendix~\\ref{app:stability}.\n",
      "numLines": 223,
      "startLine": 1,
      "totalLines": 223
    }
  },
  "sourceToolAssistantUUID": "7035771c-4af4-44e5-b4fb-f21e7ed050cd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/review_reviewer_1_772f066c",
  "sessionId": "e4589542-c5a3-4a5b-a779-c62f37dfeb92",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-17T04:48:12.261Z_

<details open><summary>🔧 Tool call — Read · `toolu_01JDYsVa2655itnm5u38e9bQ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d5dc06e7-1b53-4c41-aa95-0d825e08ab34",
  "isSidechain": false,
  "requestId": "req_011Cb7Y32F65JCSzUjAH7NPn",
  "type": "assistant",
  "uuid": "d4fa3273-e264-478a-8907-b3ce1d55f87b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/review_reviewer_1_772f066c",
  "sessionId": "e4589542-c5a3-4a5b-a779-c62f37dfeb92",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KkHZHeh3i4ShZNd2zi3CuC",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6120,
      "cache_creation_input_tokens": 1053,
      "cache_read_input_tokens": 30819,
      "output_tokens": 160,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1053,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 6120,
          "output_tokens": 160,
          "cache_read_input_tokens": 30819,
          "cache_creation_input_tokens": 1053,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1053
          },
          "type": "message"
        }
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

_source line 30 · 2026-05-17T04:48:12.268Z_

<details><summary>↩ Tool result · `toolu_01JDYsVa2655itnm5u38e9bQ`</summary>

```text
1	\appendix
2	
3	\section{Inference Efficiency}
4	\label{app:latency}
5	
6	Table~\ref{tab:latency} reports inference throughput on a single NVIDIA RTX PRO 6000 Blackwell Server Edition GPU (batch size 1, sequence length 2048, fp16, averaged over 100 forward passes).
7	
8	\begin{table}[h]
9	\centering
10	\caption{Inference latency on LLaMA-3.1-8B (RTX PRO 6000 Blackwell, batch=1, seq=2048, fp16, 100 forward passes). Overhead is relative to dense inference.}
11	\label{tab:latency}
12	\small
13	\begin{tabular}{llcccc}
14	\toprule
15	Method & Sparsity & ms/fwd & tok/s & Overhead \\
16	\midrule
17	Dense & 0\% & 119.11$\pm$0.57 & 17{,}195 & --- \\
18	\midrule
19	KL predictor-only & 30\% & 126.64$\pm$0.70 & 16{,}172 & +6.3\% \\ % exp_id: latency_bench
20	KL predictor-only & 50\% & 126.78$\pm$0.31 & 16{,}154 & +6.4\% \\ % exp_id: latency_bench
21	\midrule
22	Predictor + compensation & 30\% & 129.94$\pm$0.75 & 15{,}761 & +9.1\% \\ % exp_id: latency_bench
23	Predictor + compensation & 50\% & 129.71$\pm$0.53 & 15{,}789 & +8.9\% \\ % exp_id: latency_bench
24	\bottomrule
25	\end{tabular}
26	\end{table}
27	
28	The full KL-sparse pipeline adds 6.4\% overhead to dense inference (126.78 vs.\ 119.11\,ms/forward), of which the predictor's 32-layer forward pass contributes 3.17\,ms (2.7\%); the remainder arises from mask application and sparse FFN indexing.
29	Eliminating the compensation network saves an additional $\sim$2.7\% latency overhead and 67.2M parameters (the per-layer GEMV required for output rescaling), confirming that KL distillation provides both quality and efficiency advantages over BCE-based approaches.
30	The overhead is near-identical at 30\% and 50\% sparsity because the predictor runs the same computation regardless of target sparsity; only the top-$k$ threshold changes.
31	
32	Note that the current implementation uses unstructured element-wise masks, which do not translate to wall-clock speedup without sparse kernel support.
33	The pipeline adds $\sim$6.4\% overhead; net acceleration requires kernel-level sparse computation optimizations (e.g., Triton block-sparse, cuSPARSE) that are beyond the scope of this work.
34	Our contribution is prediction quality and inference simplification (eliminating the compensation network), not end-to-end latency reduction.
35	
36	
37	\section{Predictor Bottleneck Sensitivity}
38	\label{app:db_sensitivity}
39	
40	Table~\ref{tab:db_sensitivity} reports the effect of predictor bottleneck dimension $d_b$ on PPL at 50\% sparsity under both TEAL global allocation (the paper's primary inference protocol) and per-token evaluation.
41	
42	\begin{table}[h]
43	\centering
44	\caption{Predictor bottleneck sensitivity at 50\% sparsity (WikiText-2 PPL$\downarrow$). TEAL global is the primary inference protocol; per-token shown for reference.}
45	\label{tab:db_sensitivity}
46	\small
47	\begin{tabular}{lcccc}
48	\toprule
49	$d_b$ & Params & TEAL global & $\Delta$ & Per-token \\
50	\midrule
51	64 & 38.2M (0.48\%) & 12.076 & +0.9\% & 10.16 \\ % exp_id: db_sensitivity_sweep
52	128 & 75.9M (0.95\%) & 11.963 & --- & 9.218 \\ % exp_id: db_sensitivity_sweep
53	256 & 151.5M (1.89\%) & 12.105 & +1.2\% & 8.586 \\ % exp_id: db_sensitivity_sweep
54	512 & 302.5M (3.77\%) & 12.315 & +2.9\% & 7.93 \\ % exp_id: db_sensitivity_sweep
55	\bottomrule
56	\end{tabular}
57	\end{table}
58	
59	Under TEAL global allocation, increasing $d_b$ beyond 128 provides no benefit (PPL slightly worsens), while per-token evaluation shows monotonic improvement (10.16$\to$7.93).
60	This divergence indicates that the global top-$k$ allocation mechanism, not predictor capacity, is the binding constraint: additional predictor capacity produces better per-neuron scores, but the global ranking and budget distribution cannot exploit them.
61	The $d_b{=}128$ configuration (75.9M params, $<$1\% of base model) is therefore optimal for the TEAL inference protocol.
62	
63	\subsection{Temperature Schedule Sensitivity}
64	\label{app:tau_sensitivity}
65	
66	\begin{table}[h]
67	\centering
68	\caption{Temperature schedule sensitivity at 50\% sparsity (WikiText-2 PPL$\downarrow$, TEAL global).}
69	\label{tab:tau_sensitivity}
70	\small
71	\begin{tabular}{lc}
72	\toprule
73	$\tau$ Schedule & PPL$\downarrow$ \\
74	\midrule
75	Fixed $\tau{=}0.5$ & \textbf{11.861} \\ % exp_id: tau_schedule_sweep
76	Linear $1.0 \to 0.1$ (default) & 11.963 \\ % exp_id: tau_schedule_sweep
77	Fixed $\tau{=}0.1$ & 12.072 \\ % exp_id: tau_schedule_sweep
78	\bottomrule
79	\end{tabular}
80	\end{table}
81	
82	Temperature schedule has minimal impact ($<$1.8\% PPL variation).
83	The linear annealing default is a conservative choice; even removing annealing entirely (fixed $\tau{=}0.5$) yields comparable performance.
84	
85	\subsection{Training Convergence}
86	\label{app:training_convergence}
87	
88	\begin{table}[h]
89	\centering
90	\caption{Training convergence at 50\% sparsity (WikiText-2 PPL$\downarrow$, TEAL global).}
91	\label{tab:training_convergence}
92	\small
93	\begin{tabular}{cc}
94	\toprule
95	Steps & PPL$\downarrow$ \\
96	\midrule
97	200 & 15.158 \\ % exp_id: training_steps_sweep
98	400 & 12.538 \\ % exp_id: training_steps_sweep
99	600 & 12.046 \\ % exp_id: training_steps_sweep
100	800 & 11.907 \\ % exp_id: training_steps_sweep
101	1000 & \textbf{11.906} \\ % exp_id: training_steps_sweep
102	\bottomrule
103	\end{tabular}
104	\end{table}
105	
106	Training converges rapidly: 95\% of the quality gap closes by step 600, and performance saturates by step 800 ($\Delta < 0.001$ between 800 and 1000 steps).
107	Our default of 1000 steps provides a conservative margin.
108	
109	
110	\section{Lagrangian Training Dynamics}
111	\label{app:lagrangian}
112	
113	Table~\ref{tab:lagrangian} reports the convergence of the multiplicative dual variable controller across sparsity targets.
114	The geometric doubling pattern ($1 \to 2 \to 4 \to 8 \to \ldots$) enables $\lambda$ to reach steady state within $\sim$10 steps; the deadzone ($\epsilon = 0.02$) then stabilizes $\lambda$ once actual sparsity is within $\pm$2\% of the target.
115	
116	\begin{table}[h]
117	\centering
118	\caption{Lagrangian convergence across sparsity targets (multiplicative controller, margin $\epsilon=0.02$, 1000 training steps). Deviation is $|$actual $-$ target$|$ / target.}
119	\label{tab:lagrangian}
120	\small
121	\begin{tabular}{lccccc}
122	\toprule
123	Target $\rho$ & $\lambda_{\max}$ & Final $\lambda$ & Actual sparsity & Deviation \\
124	\midrule
125	30\% & 5000 & 5000 (cap) & 0.285 & 5.0\% \\ % exp_id: kl_30pct_s42
126	40\% & 5000 & 625 & 0.398 & 0.5\% \\ % exp_id: kl_40pct_s42
127	50\% & 1000 & 8 & 0.504 & 0.8\% \\ % exp_id: kl_50pct_s42
128	70\% & 1000 & 1000 (cap) & 0.688 & 1.7\% \\ % exp_id: kl_70pct_s42
129	\bottomrule
130	\end{tabular}
131	\end{table}
132	
133	At 50\% sparsity, the SwiGLU gate distribution already clusters near the target, so $\lambda$ remains low (8); the constraint is nearly satisfied by the initial predictor outputs.
134	At 30\% and 70\%, the gap between the gate prior and target is larger, driving $\lambda$ to its respective caps.
135	The 40\% target converges to $\lambda = 625$ with only 0.5\% deviation, illustrating the controller's precision when the target is reachable without saturating.
136	
137	Temperature $\tau$ is annealed linearly from 1.0 to 0.1 over 1000 steps.
138	A mild loss increase in the final $\sim$100 steps is expected: as masks become more binary ($\tau \to 0$), discrete rounding noise slightly increases KL divergence, confirming the training is converging toward the hard-mask inference regime.
139	
140	The controller reliably drives actual sparsity to within 5\% of the target across all tested regimes, with $\lambda$ spanning three orders of magnitude (8 to 5000) via geometric doubling.
141	
142	
143	\section{Out-of-Distribution Evaluation}
144	\label{app:ood}
145	
146	To address concerns about data homogeneity between training (WikiText-103) and evaluation (WikiText-2), we evaluate on C4 validation set at 50\% sparsity under TEAL global allocation.
147	
148	\begin{table}[h]
149	\centering
150	\caption{Out-of-distribution evaluation on C4 validation (50\% sparsity, PPL$\downarrow$).}
151	\label{tab:ood}
152	\small
153	\begin{tabular}{lc}
154	\toprule
155	Method & C4 PPL$\downarrow$ \\
156	\midrule
157	Dense & 9.21 \\
158	KL predictor (Ours) & \textbf{18.40} \\ % exp_id: eval_c4_ood_kl50
159	TEAL vanilla & 38.75 \\
160	\bottomrule
161	\end{tabular}
162	\end{table}
163	
164	The KL-trained predictor achieves 52.5\% relative advantage over TEAL on out-of-domain data (18.40 vs.\ 38.75), comparable to or slightly exceeding the 49\% advantage observed on WikiText-2 (11.79 vs.\ 23.31), suggesting that KL-trained predictions generalize robustly when the evaluation distribution differs from training.
165	This confirms that the predictor learns generalizable neuron importance patterns rather than overfitting to the WikiText training distribution.
166	
167	
168	\section{Training Stability}
169	\label{app:stability}
170	
171	Three-seed evaluation ($s \in \{42, 123, 456\}$) at 50\% sparsity under uniform allocation yields PPL $11.92 \pm 0.07$ (CV=0.6\%), confirming training stability across random initializations. % exp_id: multi_seed_kl50_uniform
172	Downstream metrics are similarly stable: ARC-c $33.8 \pm 1.2$\%, WinoGrande $62.9 \pm 0.1$\%, MMLU $28.0 \pm 0.6$\%, GSM8K $2.2 \pm 0.1$\%.
173	The low variance indicates that the KL training landscape is well-conditioned for this predictor architecture, with low sensitivity to initialization.
174	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d4fa3273-e264-478a-8907-b3ce1d55f87b",
  "isSidechain": false,
  "promptId": "d17f6ff5-7f93-4500-81a7-61caa2f125ae",
  "type": "user",
  "uuid": "424de6ed-ae06-4cc6-98b7-2f66acb5a974",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/appendix.tex",
      "content": "\\appendix\n\n\\section{Inference Efficiency}\n\\label{app:latency}\n\nTable~\\ref{tab:latency} reports inference throughput on a single NVIDIA RTX PRO 6000 Blackwell Server Edition GPU (batch size 1, sequence length 2048, fp16, averaged over 100 forward passes).\n\n\\begin{table}[h]\n\\centering\n\\caption{Inference latency on LLaMA-3.1-8B (RTX PRO 6000 Blackwell, batch=1, seq=2048, fp16, 100 forward passes). Overhead is relative to dense inference.}\n\\label{tab:latency}\n\\small\n\\begin{tabular}{llcccc}\n\\toprule\nMethod & Sparsity & ms/fwd & tok/s & Overhead \\\\\n\\midrule\nDense & 0\\% & 119.11$\\pm$0.57 & 17{,}195 & --- \\\\\n\\midrule\nKL predictor-only & 30\\% & 126.64$\\pm$0.70 & 16{,}172 & +6.3\\% \\\\ % exp_id: latency_bench\nKL predictor-only & 50\\% & 126.78$\\pm$0.31 & 16{,}154 & +6.4\\% \\\\ % exp_id: latency_bench\n\\midrule\nPredictor + compensation & 30\\% & 129.94$\\pm$0.75 & 15{,}761 & +9.1\\% \\\\ % exp_id: latency_bench\nPredictor + compensation & 50\\% & 129.71$\\pm$0.53 & 15{,}789 & +8.9\\% \\\\ % exp_id: latency_bench\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe full KL-sparse pipeline adds 6.4\\% overhead to dense inference (126.78 vs.\\ 119.11\\,ms/forward), of which the predictor's 32-layer forward pass contributes 3.17\\,ms (2.7\\%); the remainder arises from mask application and sparse FFN indexing.\nEliminating the compensation network saves an additional $\\sim$2.7\\% latency overhead and 67.2M parameters (the per-layer GEMV required for output rescaling), confirming that KL distillation provides both quality and efficiency advantages over BCE-based approaches.\nThe overhead is near-identical at 30\\% and 50\\% sparsity because the predictor runs the same computation regardless of target sparsity; only the top-$k$ threshold changes.\n\nNote that the current implementation uses unstructured element-wise masks, which do not translate to wall-clock speedup without sparse kernel support.\nThe pipeline adds $\\sim$6.4\\% overhead; net acceleration requires kernel-level sparse computation optimizations (e.g., Triton block-sparse, cuSPARSE) that are beyond the scope of this work.\nOur contribution is prediction quality and inference simplification (eliminating the compensation network), not end-to-end latency reduction.\n\n\n\\section{Predictor Bottleneck Sensitivity}\n\\label{app:db_sensitivity}\n\nTable~\\ref{tab:db_sensitivity} reports the effect of predictor bottleneck dimension $d_b$ on PPL at 50\\% sparsity under both TEAL global allocation (the paper's primary inference protocol) and per-token evaluation.\n\n\\begin{table}[h]\n\\centering\n\\caption{Predictor bottleneck sensitivity at 50\\% sparsity (WikiText-2 PPL$\\downarrow$). TEAL global is the primary inference protocol; per-token shown for reference.}\n\\label{tab:db_sensitivity}\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n$d_b$ & Params & TEAL global & $\\Delta$ & Per-token \\\\\n\\midrule\n64 & 38.2M (0.48\\%) & 12.076 & +0.9\\% & 10.16 \\\\ % exp_id: db_sensitivity_sweep\n128 & 75.9M (0.95\\%) & 11.963 & --- & 9.218 \\\\ % exp_id: db_sensitivity_sweep\n256 & 151.5M (1.89\\%) & 12.105 & +1.2\\% & 8.586 \\\\ % exp_id: db_sensitivity_sweep\n512 & 302.5M (3.77\\%) & 12.315 & +2.9\\% & 7.93 \\\\ % exp_id: db_sensitivity_sweep\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nUnder TEAL global allocation, increasing $d_b$ beyond 128 provides no benefit (PPL slightly worsens), while per-token evaluation shows monotonic improvement (10.16$\\to$7.93).\nThis divergence indicates that the global top-$k$ allocation mechanism, not predictor capacity, is the binding constraint: additional predictor capacity produces better per-neuron scores, but the global ranking and budget distribution cannot exploit them.\nThe $d_b{=}128$ configuration (75.9M params, $<$1\\% of base model) is therefore optimal for the TEAL inference protocol.\n\n\\subsection{Temperature Schedule Sensitivity}\n\\label{app:tau_sensitivity}\n\n\\begin{table}[h]\n\\centering\n\\caption{Temperature schedule sensitivity at 50\\% sparsity (WikiText-2 PPL$\\downarrow$, TEAL global).}\n\\label{tab:tau_sensitivity}\n\\small\n\\begin{tabular}{lc}\n\\toprule\n$\\tau$ Schedule & PPL$\\downarrow$ \\\\\n\\midrule\nFixed $\\tau{=}0.5$ & \\textbf{11.861} \\\\ % exp_id: tau_schedule_sweep\nLinear $1.0 \\to 0.1$ (default) & 11.963 \\\\ % exp_id: tau_schedule_sweep\nFixed $\\tau{=}0.1$ & 12.072 \\\\ % exp_id: tau_schedule_sweep\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTemperature schedule has minimal impact ($<$1.8\\% PPL variation).\nThe linear annealing default is a conservative choice; even removing annealing entirely (fixed $\\tau{=}0.5$) yields comparable performance.\n\n\\subsection{Training Convergence}\n\\label{app:training_convergence}\n\n\\begin{table}[h]\n\\centering\n\\caption{Training convergence at 50\\% sparsity (WikiText-2 PPL$\\downarrow$, TEAL global).}\n\\label{tab:training_convergence}\n\\small\n\\begin{tabular}{cc}\n\\toprule\nSteps & PPL$\\downarrow$ \\\\\n\\midrule\n200 & 15.158 \\\\ % exp_id: training_steps_sweep\n400 & 12.538 \\\\ % exp_id: training_steps_sweep\n600 & 12.046 \\\\ % exp_id: training_steps_sweep\n800 & 11.907 \\\\ % exp_id: training_steps_sweep\n1000 & \\textbf{11.906} \\\\ % exp_id: training_steps_sweep\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTraining converges rapidly: 95\\% of the quality gap closes by step 600, and performance saturates by step 800 ($\\Delta < 0.001$ between 800 and 1000 steps).\nOur default of 1000 steps provides a conservative margin.\n\n\n\\section{Lagrangian Training Dynamics}\n\\label{app:lagrangian}\n\nTable~\\ref{tab:lagrangian} reports the convergence of the multiplicative dual variable controller across sparsity targets.\nThe geometric doubling pattern ($1 \\to 2 \\to 4 \\to 8 \\to \\ldots$) enables $\\lambda$ to reach steady state within $\\sim$10 steps; the deadzone ($\\epsilon = 0.02$) then stabilizes $\\lambda$ once actual sparsity is within $\\pm$2\\% of the target.\n\n\\begin{table}[h]\n\\centering\n\\caption{Lagrangian convergence across sparsity targets (multiplicative controller, margin $\\epsilon=0.02$, 1000 training steps). Deviation is $|$actual $-$ target$|$ / target.}\n\\label{tab:lagrangian}\n\\small\n\\begin{tabular}{lccccc}\n\\toprule\nTarget $\\rho$ & $\\lambda_{\\max}$ & Final $\\lambda$ & Actual sparsity & Deviation \\\\\n\\midrule\n30\\% & 5000 & 5000 (cap) & 0.285 & 5.0\\% \\\\ % exp_id: kl_30pct_s42\n40\\% & 5000 & 625 & 0.398 & 0.5\\% \\\\ % exp_id: kl_40pct_s42\n50\\% & 1000 & 8 & 0.504 & 0.8\\% \\\\ % exp_id: kl_50pct_s42\n70\\% & 1000 & 1000 (cap) & 0.688 & 1.7\\% \\\\ % exp_id: kl_70pct_s42\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nAt 50\\% sparsity, the SwiGLU gate distribution already clusters near the target, so $\\lambda$ remains low (8); the constraint is nearly satisfied by the initial predictor outputs.\nAt 30\\% and 70\\%, the gap between the gate prior and target is larger, driving $\\lambda$ to its respective caps.\nThe 40\\% target converges to $\\lambda = 625$ with only 0.5\\% deviation, illustrating the controller's precision when the target is reachable without saturating.\n\nTemperature $\\tau$ is annealed linearly from 1.0 to 0.1 over 1000 steps.\nA mild loss increase in the final $\\sim$100 steps is expected: as masks become more binary ($\\tau \\to 0$), discrete rounding noise slightly increases KL divergence, confirming the training is converging toward the hard-mask inference regime.\n\nThe controller reliably drives actual sparsity to within 5\\% of the target across all tested regimes, with $\\lambda$ spanning three orders of magnitude (8 to 5000) via geometric doubling.\n\n\n\\section{Out-of-Distribution Evaluation}\n\\label{app:ood}\n\nTo address concerns about data homogeneity between training (WikiText-103) and evaluation (WikiText-2), we evaluate on C4 validation set at 50\\% sparsity under TEAL global allocation.\n\n\\begin{table}[h]\n\\centering\n\\caption{Out-of-distribution evaluation on C4 validation (50\\% sparsity, PPL$\\downarrow$).}\n\\label{tab:ood}\n\\small\n\\begin{tabular}{lc}\n\\toprule\nMethod & C4 PPL$\\downarrow$ \\\\\n\\midrule\nDense & 9.21 \\\\\nKL predictor (Ours) & \\textbf{18.40} \\\\ % exp_id: eval_c4_ood_kl50\nTEAL vanilla & 38.75 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe KL-trained predictor achieves 52.5\\% relative advantage over TEAL on out-of-domain data (18.40 vs.\\ 38.75), comparable to or slightly exceeding the 49\\% advantage observed on WikiText-2 (11.79 vs.\\ 23.31), suggesting that KL-trained predictions generalize robustly when the evaluation distribution differs from training.\nThis confirms that the predictor learns generalizable neuron importance patterns rather than overfitting to the WikiText training distribution.\n\n\n\\section{Training Stability}\n\\label{app:stability}\n\nThree-seed evaluation ($s \\in \\{42, 123, 456\\}$) at 50\\% sparsity under uniform allocation yields PPL $11.92 \\pm 0.07$ (CV=0.6\\%), confirming training stability across random initializations. % exp_id: multi_seed_kl50_uniform\nDownstream metrics are similarly stable: ARC-c $33.8 \\pm 1.2$\\%, WinoGrande $62.9 \\pm 0.1$\\%, MMLU $28.0 \\pm 0.6$\\%, GSM8K $2.2 \\pm 0.1$\\%.\nThe low variance indicates that the KL training landscape is well-conditioned for this predictor architecture, with low sensitivity to initialization.\n",
      "numLines": 174,
      "startLine": 1,
      "totalLines": 174
    }
  },
  "sourceToolAssistantUUID": "d4fa3273-e264-478a-8907-b3ce1d55f87b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/review_reviewer_1_772f066c",
  "sessionId": "e4589542-c5a3-4a5b-a779-c62f37dfeb92",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Runtime record

_source line 31_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[Round 2 审稿请求]: ## Round 2 审稿任务 — Reviewer 1（方法严谨性 + 实验设计）  ### Venue 信息 - **目标**: EMNLP 2026 via ACL Rolling Review (ARR) May 2026 cycle - **Deadline**: 2026-05-25 - **页数限制**: 正文 8 页 + unlimited refe…",
  "leafUuid": "424de6ed-ae06-4cc6-98b7-2f66acb5a974",
  "sessionId": "e4589542-c5a3-4a5b-a779-c62f37dfeb92"
}
```

---

### Runtime record

_source line 32_

```json
{
  "type": "ai-title",
  "aiTitle": "Review Round 2 distill sparse SwiGLU paper",
  "sessionId": "e4589542-c5a3-4a5b-a779-c62f37dfeb92"
}
```

---

### Tool call

_source line 33 · 2026-05-17T04:48:16.901Z_

<details open><summary>🔧 Tool call — Read · `toolu_01UNjw8nH3ZS9d36jXQyWAYS`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "424de6ed-ae06-4cc6-98b7-2f66acb5a974",
  "isSidechain": false,
  "requestId": "req_011Cb7Y3P7wxQKwbP5SdAc6F",
  "type": "assistant",
  "uuid": "fa8bb710-4e88-4294-9f0a-3316ce7e4693",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/review_reviewer_1_772f066c",
  "sessionId": "e4589542-c5a3-4a5b-a779-c62f37dfeb92",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013LNiYtAdYJuKsjB18Vbj1S",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 15753,
      "cache_read_input_tokens": 31872,
      "output_tokens": 232,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 15753,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 232,
          "cache_read_input_tokens": 31872,
          "cache_creation_input_tokens": 15753,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 15753
          },
          "type": "message"
        }
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

_source line 34 · 2026-05-17T04:48:16.908Z_

<details><summary>↩ Tool result · `toolu_01UNjw8nH3ZS9d36jXQyWAYS`</summary>

```text
1	\section{Introduction}
2	
3	SwiGLU feed-forward networks~\cite{shazeer2020glu} in modern LLMs exhibit high contextual sparsity: at any given token, a large fraction of FFN neurons contribute negligibly to the output.
4	Exploiting this sparsity can simplify inference by pruning 50\% of FFN neurons per token---without modifying the pretrained weights---eliminating the need for auxiliary compensation networks.
5	Yet the gap between potential and practice remains wide.
6	Training-free methods such as TEAL~\cite{liu2025teal} select neurons by activation magnitude alone, degrading perplexity from 6.12 (dense) to 23.31 at 50\% sparsity on LLaMA-3.1-8B~\cite{grattafiori2024llama3}---a 281\% increase.
7	Learned predictors~\cite{liu2023dejavu,gautam2026fastforward} close part of this gap by training small auxiliary networks to anticipate which neurons will be important, but they rely on error compensation modules (output rescaling networks or additive correction layers) that add 67.2M parameters and $\sim$2.7\% additional latency overhead at inference.
8	The question is whether a predictor can be trained so that compensation becomes unnecessary.
9	
10	The answer depends on the training objective.
11	Current learned predictors use binary cross-entropy (BCE) loss: each neuron is independently classified as ``keep'' or ``prune'' against an oracle mask derived from the dense model's activations.
12	The gradient of BCE with respect to neuron $j$'s score is $\partial \mathcal{L}_{\text{BCE}} / \partial s_j = \sigma(s_j) - m_j^*$---a function of neuron $j$ alone, independent of every other neuron in the network.
13	But at inference, no neuron is evaluated in isolation.
14	TEAL's global top-$k$ mechanism~\cite{liu2025teal} ranks all neurons across all layers and retains only those above a model-wide threshold.
15	Whether neuron $j$ survives depends not on its own score but on how that score compares to the scores of all $L \times d_{\text{ff}}$ neurons.
16	This creates a structural mismatch: the training objective decomposes per neuron, while the inference allocation is a global combinatorial decision.
17	BCE can achieve $>$90\% per-neuron classification accuracy against oracle masks yet still produce poor output quality under global allocation, because it optimizes a proxy misaligned with the true objective.
18	
19	KL divergence resolves this mismatch by coupling all neurons through the output distribution.
20	Instead of classifying individual neurons, we minimize $D_{\text{KL}}(p_{\text{dense}} \| p_{\text{sparse}})$ between the dense and sparse model outputs, training the predictor to preserve the full next-token distribution under pruning.
21	The gradient for neuron $j$ in layer $\ell$ factors as:
22	\begin{equation*}
23	\frac{\partial \mathcal{L}_{\text{KL}}}{\partial s_j^{(\ell)}} = \frac{\partial \mathcal{L}_{\text{KL}}}{\partial \mathbf{z}} \cdot \frac{\partial \mathbf{z}}{\partial \mathbf{h}^{(\ell)}} \cdot \frac{\partial \mathbf{h}^{(\ell)}}{\partial \tilde{m}_j^{(\ell)}} \cdot \frac{\partial \tilde{m}_j^{(\ell)}}{\partial s_j^{(\ell)}},
24	\end{equation*}
25	where the Jacobian $\partial \mathbf{z} / \partial \mathbf{h}^{(\ell)}$ propagates through all downstream layers, making each neuron's gradient dependent on every other neuron's mask state.
26	Changing one neuron's mask affects all output logits; KL captures this because it measures distributional divergence over the entire vocabulary.
27	A Gumbel-Sigmoid relaxation~\cite{jang2017gumbel} provides differentiable mask sampling during training, bridging the gap between soft training masks and hard inference decisions.
28	The predictor itself is a lightweight two-layer MLP (Linear $4096 \to 128$, GELU, Linear $128 \to 14336$) with 2.37M parameters per layer and 75.9M total---under 1\% of the base model---and requires no compensation network at inference.
29	
30	Empirically, the structural argument is borne out across sparsity levels, training budgets, and architectures.
31	At 50\% sparsity on LLaMA-3.1-8B, the KL-trained predictor achieves PPL 11.79 under TEAL's global allocation, compared to 23.31 for vanilla TEAL.
32	BCE trained for 2700 steps (2.71$\times$ our compute budget) reaches only 27.97, and its training loss saturates with $\Delta = -0.006$ over the final 2200 steps---confirming that the failure is structural, not computational.
33	The KL advantage grows disproportionately with sparsity: 18\% relative improvement at 30\%, 49\% at 50\%, and 82\% at 70\%.
34	Evaluation on Mistral-7B-v0.3~\cite{jiang2023mistral} across three sparsity levels confirms the advantage transfers across SwiGLU architectures of similar scale, with KL-over-TEAL ratios consistent within 7\% at $\leq$50\% sparsity and the same regime boundary where magnitude-based methods catastrophically degrade.
35	We also analyze SPON's~\cite{xu2026spon} static bias correction and find it near-orthogonal to the predictor's effect (cosine similarity 0.196), providing only 2.4\% relative PPL improvement (12.08$\to$11.79)---the KL predictor already captures most of the recoverable signal.
36	
37	To situate these findings, we propose a two-dimensional taxonomy (Figure~\ref{fig:taxonomy}) that classifies sparsity prediction methods along \emph{correction granularity} (static, per-layer, per-token) and \emph{training signal coupling} (decomposed, intermediate, coupled).
38	Prior methods occupy distinct cells: SPON~\cite{xu2026spon} combines static correction with coupled KL training; ShadowLLM~\cite{akhauri2024shadowllm} uses per-layer prediction with intermediate MSE; FastForward~\cite{gautam2026fastforward} and DejaVu~\cite{liu2023dejavu} achieve per-token granularity but with decomposed BCE objectives.
39	No prior work has combined per-token contextual prediction with a coupled training signal.
40	Our method fills this cell, unifying input-dependent mask generation with an objective that reflects global neuron interactions through the output distribution.
41	
42	Our contributions are:
43	\begin{itemize}[nosep,leftmargin=*]
44	\item We show that a KL-trained contextual predictor eliminates the need for error compensation networks in activation sparsity, and provide a formal gradient analysis explaining the structural mismatch between per-neuron BCE training and global top-$k$ inference allocation.
45	\item We organize prior work via a 2D framework (correction granularity $\times$ training signal coupling, Figure~\ref{fig:taxonomy}) that situates our method in a previously unexplored cell: per-token prediction with coupled training signals.
46	\item We identify three distinct sparsity regimes---budget-surplus ($\leq$30\%, where predictor and allocation choices recover downstream performance), budget-constrained ($\sim$40\%), and capacity-limited ($\geq$50\%, where no method recovers reasoning ability)---and confirm via SPON orthogonality analysis that static correction provides diminishing returns once a coupled predictor is present.
47	\end{itemize}
48	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fa8bb710-4e88-4294-9f0a-3316ce7e4693",
  "isSidechain": false,
  "promptId": "d17f6ff5-7f93-4500-81a7-61caa2f125ae",
  "type": "user",
  "uuid": "2ae9aa9e-6ad7-4044-8527-612b92bea9f6",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/introduction.tex",
      "content": "\\section{Introduction}\n\nSwiGLU feed-forward networks~\\cite{shazeer2020glu} in modern LLMs exhibit high contextual sparsity: at any given token, a large fraction of FFN neurons contribute negligibly to the output.\nExploiting this sparsity can simplify inference by pruning 50\\% of FFN neurons per token---without modifying the pretrained weights---eliminating the need for auxiliary compensation networks.\nYet the gap between potential and practice remains wide.\nTraining-free methods such as TEAL~\\cite{liu2025teal} select neurons by activation magnitude alone, degrading perplexity from 6.12 (dense) to 23.31 at 50\\% sparsity on LLaMA-3.1-8B~\\cite{grattafiori2024llama3}---a 281\\% increase.\nLearned predictors~\\cite{liu2023dejavu,gautam2026fastforward} close part of this gap by training small auxiliary networks to anticipate which neurons will be important, but they rely on error compensation modules (output rescaling networks or additive correction layers) that add 67.2M parameters and $\\sim$2.7\\% additional latency overhead at inference.\nThe question is whether a predictor can be trained so that compensation becomes unnecessary.\n\nThe answer depends on the training objective.\nCurrent learned predictors use binary cross-entropy (BCE) loss: each neuron is independently classified as ``keep'' or ``prune'' against an oracle mask derived from the dense model's activations.\nThe gradient of BCE with respect to neuron $j$'s score is $\\partial \\mathcal{L}_{\\text{BCE}} / \\partial s_j = \\sigma(s_j) - m_j^*$---a function of neuron $j$ alone, independent of every other neuron in the network.\nBut at inference, no neuron is evaluated in isolation.\nTEAL's global top-$k$ mechanism~\\cite{liu2025teal} ranks all neurons across all layers and retains only those above a model-wide threshold.\nWhether neuron $j$ survives depends not on its own score but on how that score compares to the scores of all $L \\times d_{\\text{ff}}$ neurons.\nThis creates a structural mismatch: the training objective decomposes per neuron, while the inference allocation is a global combinatorial decision.\nBCE can achieve $>$90\\% per-neuron classification accuracy against oracle masks yet still produce poor output quality under global allocation, because it optimizes a proxy misaligned with the true objective.\n\nKL divergence resolves this mismatch by coupling all neurons through the output distribution.\nInstead of classifying individual neurons, we minimize $D_{\\text{KL}}(p_{\\text{dense}} \\| p_{\\text{sparse}})$ between the dense and sparse model outputs, training the predictor to preserve the full next-token distribution under pruning.\nThe gradient for neuron $j$ in layer $\\ell$ factors as:\n\\begin{equation*}\n\\frac{\\partial \\mathcal{L}_{\\text{KL}}}{\\partial s_j^{(\\ell)}} = \\frac{\\partial \\mathcal{L}_{\\text{KL}}}{\\partial \\mathbf{z}} \\cdot \\frac{\\partial \\mathbf{z}}{\\partial \\mathbf{h}^{(\\ell)}} \\cdot \\frac{\\partial \\mathbf{h}^{(\\ell)}}{\\partial \\tilde{m}_j^{(\\ell)}} \\cdot \\frac{\\partial \\tilde{m}_j^{(\\ell)}}{\\partial s_j^{(\\ell)}},\n\\end{equation*}\nwhere the Jacobian $\\partial \\mathbf{z} / \\partial \\mathbf{h}^{(\\ell)}$ propagates through all downstream layers, making each neuron's gradient dependent on every other neuron's mask state.\nChanging one neuron's mask affects all output logits; KL captures this because it measures distributional divergence over the entire vocabulary.\nA Gumbel-Sigmoid relaxation~\\cite{jang2017gumbel} provides differentiable mask sampling during training, bridging the gap between soft training masks and hard inference decisions.\nThe predictor itself is a lightweight two-layer MLP (Linear $4096 \\to 128$, GELU, Linear $128 \\to 14336$) with 2.37M parameters per layer and 75.9M total---under 1\\% of the base model---and requires no compensation network at inference.\n\nEmpirically, the structural argument is borne out across sparsity levels, training budgets, and architectures.\nAt 50\\% sparsity on LLaMA-3.1-8B, the KL-trained predictor achieves PPL 11.79 under TEAL's global allocation, compared to 23.31 for vanilla TEAL.\nBCE trained for 2700 steps (2.71$\\times$ our compute budget) reaches only 27.97, and its training loss saturates with $\\Delta = -0.006$ over the final 2200 steps---confirming that the failure is structural, not computational.\nThe KL advantage grows disproportionately with sparsity: 18\\% relative improvement at 30\\%, 49\\% at 50\\%, and 82\\% at 70\\%.\nEvaluation on Mistral-7B-v0.3~\\cite{jiang2023mistral} across three sparsity levels confirms the advantage transfers across SwiGLU architectures of similar scale, with KL-over-TEAL ratios consistent within 7\\% at $\\leq$50\\% sparsity and the same regime boundary where magnitude-based methods catastrophically degrade.\nWe also analyze SPON's~\\cite{xu2026spon} static bias correction and find it near-orthogonal to the predictor's effect (cosine similarity 0.196), providing only 2.4\\% relative PPL improvement (12.08$\\to$11.79)---the KL predictor already captures most of the recoverable signal.\n\nTo situate these findings, we propose a two-dimensional taxonomy (Figure~\\ref{fig:taxonomy}) that classifies sparsity prediction methods along \\emph{correction granularity} (static, per-layer, per-token) and \\emph{training signal coupling} (decomposed, intermediate, coupled).\nPrior methods occupy distinct cells: SPON~\\cite{xu2026spon} combines static correction with coupled KL training; ShadowLLM~\\cite{akhauri2024shadowllm} uses per-layer prediction with intermediate MSE; FastForward~\\cite{gautam2026fastforward} and DejaVu~\\cite{liu2023dejavu} achieve per-token granularity but with decomposed BCE objectives.\nNo prior work has combined per-token contextual prediction with a coupled training signal.\nOur method fills this cell, unifying input-dependent mask generation with an objective that reflects global neuron interactions through the output distribution.\n\nOur contributions are:\n\\begin{itemize}[nosep,leftmargin=*]\n\\item We show that a KL-trained contextual predictor eliminates the need for error compensation networks in activation sparsity, and provide a formal gradient analysis explaining the structural mismatch between per-neuron BCE training and global top-$k$ inference allocation.\n\\item We organize prior work via a 2D framework (correction granularity $\\times$ training signal coupling, Figure~\\ref{fig:taxonomy}) that situates our method in a previously unexplored cell: per-token prediction with coupled training signals.\n\\item We identify three distinct sparsity regimes---budget-surplus ($\\leq$30\\%, where predictor and allocation choices recover downstream performance), budget-constrained ($\\sim$40\\%), and capacity-limited ($\\geq$50\\%, where no method recovers reasoning ability)---and confirm via SPON orthogonality analysis that static correction provides diminishing returns once a coupled predictor is present.\n\\end{itemize}\n",
      "numLines": 48,
      "startLine": 1,
      "totalLines": 48
    }
  },
  "sourceToolAssistantUUID": "fa8bb710-4e88-4294-9f0a-3316ce7e4693",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/review_reviewer_1_772f066c",
  "sessionId": "e4589542-c5a3-4a5b-a779-c62f37dfeb92",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-17T04:48:17.313Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Dzu19X3PmtYVikSbXCw8DC`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2ae9aa9e-6ad7-4044-8527-612b92bea9f6",
  "isSidechain": false,
  "requestId": "req_011Cb7Y3P7wxQKwbP5SdAc6F",
  "type": "assistant",
  "uuid": "319adde0-12f8-4b46-a59e-3d92b101dfd6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/review_reviewer_1_772f066c",
  "sessionId": "e4589542-c5a3-4a5b-a779-c62f37dfeb92",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013LNiYtAdYJuKsjB18Vbj1S",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 15753,
      "cache_read_input_tokens": 31872,
      "output_tokens": 232,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 15753,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 232,
          "cache_read_input_tokens": 31872,
          "cache_creation_input_tokens": 15753,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 15753
          },
          "type": "message"
        }
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

_source line 36 · 2026-05-17T04:48:17.567Z_

<details><summary>↩ Tool result · `toolu_01YVDGgwrxEah5LeiuyenMdV`</summary>

```text
1	\section*{Limitations}
2	
3	Our primary evaluation uses WikiText-2 perplexity, and downstream benchmarks reveal that perplexity is a poor proxy for reasoning ability at moderate sparsity: 40\% sparsity achieves PPL 8.36 but MMLU already degrades, motivating 30\% as the recommended operating point for downstream fidelity.
4	Training requires 1000 steps on WikiText-103 ($\sim$17 minutes on A6000), but a separate predictor must be trained for each sparsity target.
5	All experiments use 7--8B parameter models (LLaMA-3.1-8B, Mistral-7B-v0.3); scaling behavior to 13B or 70B models remains untested.
6	While we motivate our work with inference speedup potential, actual wall-clock acceleration depends on sparse kernel implementations (e.g., Triton, cuSPARSE) and hardware-specific memory access patterns; this work focuses on prediction quality rather than systems optimization.
7	Future directions include N:M structured sparsity for hardware-native acceleration, scaling to 13B+ models, and training a single predictor that serves multiple sparsity targets simultaneously.
8	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4ef35024-2ba2-40f5-a327-55fb6f658cd1",
  "isSidechain": false,
  "promptId": "d17f6ff5-7f93-4500-81a7-61caa2f125ae",
  "type": "user",
  "uuid": "2425ea49-b05e-426c-8ee5-17b67d75f99c",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/limitations.tex",
      "content": "\\section*{Limitations}\n\nOur primary evaluation uses WikiText-2 perplexity, and downstream benchmarks reveal that perplexity is a poor proxy for reasoning ability at moderate sparsity: 40\\% sparsity achieves PPL 8.36 but MMLU already degrades, motivating 30\\% as the recommended operating point for downstream fidelity.\nTraining requires 1000 steps on WikiText-103 ($\\sim$17 minutes on A6000), but a separate predictor must be trained for each sparsity target.\nAll experiments use 7--8B parameter models (LLaMA-3.1-8B, Mistral-7B-v0.3); scaling behavior to 13B or 70B models remains untested.\nWhile we motivate our work with inference speedup potential, actual wall-clock acceleration depends on sparse kernel implementations (e.g., Triton, cuSPARSE) and hardware-specific memory access patterns; this work focuses on prediction quality rather than systems optimization.\nFuture directions include N:M structured sparsity for hardware-native acceleration, scaling to 13B+ models, and training a single predictor that serves multiple sparsity targets simultaneously.\n",
      "numLines": 8,
      "startLine": 1,
      "totalLines": 8
    }
  },
  "sourceToolAssistantUUID": "4ef35024-2ba2-40f5-a327-55fb6f658cd1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/review_reviewer_1_772f066c",
  "sessionId": "e4589542-c5a3-4a5b-a779-c62f37dfeb92",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool result

_source line 37 · 2026-05-17T04:48:17.319Z_

<details><summary>↩ Tool result · `toolu_01Dzu19X3PmtYVikSbXCw8DC`</summary>

```text
1	\section{Related Work}
2	
3	\paragraph{Training-Free Activation Sparsity.}
4	TEAL~\cite{liu2025teal} applies global top-$k$ selection by activation magnitude, achieving 40--50\% sparsity with no training cost.
5	CATS~\cite{lee2024cats} adapts per-layer thresholds for SiLU/SwiGLU activations; R-Sparse~\cite{zhang2025rsparse} predicts sparsity from rank-aware SVD projections; DIP~\cite{federici2025dip} combines dynamic input pruning with cache-aware masking.
6	All training-free methods determine masks from fixed statistics or input-independent criteria, while our predictor generates \emph{input-dependent} masks trained to minimize output-distribution divergence.
7	
8	\paragraph{Predictor-Based Contextual Sparsity.}
9	DejaVu~\cite{liu2023dejavu} introduced learned sparsity predictors trained via BCE to classify each neuron independently.
10	ShadowLLM~\cite{akhauri2024shadowllm} uses attention-based routing with MSE supervision but retains per-neuron decomposition.
11	FastForward~\cite{gautam2026fastforward} adds a 67.2M-parameter compensation network using BCE for mask prediction---adding inference latency.
12	PowerInfer~\cite{song2024powerinfer} exploits power-law activation frequencies for GPU--CPU scheduling.
13	MaskLLM~\cite{fang2024maskllm} also employs learnable masks with Gumbel relaxation and frozen weights, but targets N:M semi-structured \emph{weight} sparsity (2:4 patterns) via Gumbel-Softmax, producing fixed masks independent of input tokens.
14	In contrast, our method learns \emph{activation} masks that are contextual (per-token), unstructured (budget-constrained global top-$k$), and trained with Gumbel-Sigmoid to minimize output-distribution divergence.
15	All prior predictor-based methods use decomposed (BCE) or intermediate (MSE) objectives where each neuron's gradient is independent of other mask states.
16	Our \emph{coupled} KL objective propagates gradients through all downstream layers, optimizing for global allocation quality without compensation.
17	
18	\paragraph{Static Bias Correction.}
19	SPON~\cite{xu2026spon} learns input-independent bias vectors via closed-form KL minimization per layer, absorbed into weights at deployment.
20	Our method is fundamentally different: a per-token contextual predictor trained end-to-end across all layers, producing input-dependent masks.
21	SPON solves a static per-layer problem; we solve a global dynamic prediction problem. The two are near-orthogonal (cosine similarity 0.196; \S\ref{sec:experiments}).
22	
23	\paragraph{Activation Function Engineering.}
24	ReLU Strikes Back~\cite{mirzadeh2024relu} replaces SiLU with ReLU for $>$90\% natural sparsity; TurboSparse~\cite{song2024turbosparse} and ProSparse~\cite{song2025prosparse} engineer extreme sparsity through activation modifications; the Sparsing Law~\cite{luo2024sparsinglaw} formalizes how activation density increases with training compute.
25	MiniTron~\cite{muralidharan2024minitron} combines structured pruning with distillation but modifies architecture permanently.
26	All require retraining or weight modification; our method is a plug-in predictor on \emph{unmodified} SwiGLU models.
27	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "319adde0-12f8-4b46-a59e-3d92b101dfd6",
  "isSidechain": false,
  "promptId": "d17f6ff5-7f93-4500-81a7-61caa2f125ae",
  "type": "user",
  "uuid": "8df09ee8-6d0c-495b-8785-231f864f5db3",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/related_work.tex",
      "content": "\\section{Related Work}\n\n\\paragraph{Training-Free Activation Sparsity.}\nTEAL~\\cite{liu2025teal} applies global top-$k$ selection by activation magnitude, achieving 40--50\\% sparsity with no training cost.\nCATS~\\cite{lee2024cats} adapts per-layer thresholds for SiLU/SwiGLU activations; R-Sparse~\\cite{zhang2025rsparse} predicts sparsity from rank-aware SVD projections; DIP~\\cite{federici2025dip} combines dynamic input pruning with cache-aware masking.\nAll training-free methods determine masks from fixed statistics or input-independent criteria, while our predictor generates \\emph{input-dependent} masks trained to minimize output-distribution divergence.\n\n\\paragraph{Predictor-Based Contextual Sparsity.}\nDejaVu~\\cite{liu2023dejavu} introduced learned sparsity predictors trained via BCE to classify each neuron independently.\nShadowLLM~\\cite{akhauri2024shadowllm} uses attention-based routing with MSE supervision but retains per-neuron decomposition.\nFastForward~\\cite{gautam2026fastforward} adds a 67.2M-parameter compensation network using BCE for mask prediction---adding inference latency.\nPowerInfer~\\cite{song2024powerinfer} exploits power-law activation frequencies for GPU--CPU scheduling.\nMaskLLM~\\cite{fang2024maskllm} also employs learnable masks with Gumbel relaxation and frozen weights, but targets N:M semi-structured \\emph{weight} sparsity (2:4 patterns) via Gumbel-Softmax, producing fixed masks independent of input tokens.\nIn contrast, our method learns \\emph{activation} masks that are contextual (per-token), unstructured (budget-constrained global top-$k$), and trained with Gumbel-Sigmoid to minimize output-distribution divergence.\nAll prior predictor-based methods use decomposed (BCE) or intermediate (MSE) objectives where each neuron's gradient is independent of other mask states.\nOur \\emph{coupled} KL objective propagates gradients through all downstream layers, optimizing for global allocation quality without compensation.\n\n\\paragraph{Static Bias Correction.}\nSPON~\\cite{xu2026spon} learns input-independent bias vectors via closed-form KL minimization per layer, absorbed into weights at deployment.\nOur method is fundamentally different: a per-token contextual predictor trained end-to-end across all layers, producing input-dependent masks.\nSPON solves a static per-layer problem; we solve a global dynamic prediction problem. The two are near-orthogonal (cosine similarity 0.196; \\S\\ref{sec:experiments}).\n\n\\paragraph{Activation Function Engineering.}\nReLU Strikes Back~\\cite{mirzadeh2024relu} replaces SiLU with ReLU for $>$90\\% natural sparsity; TurboSparse~\\cite{song2024turbosparse} and ProSparse~\\cite{song2025prosparse} engineer extreme sparsity through activation modifications; the Sparsing Law~\\cite{luo2024sparsinglaw} formalizes how activation density increases with training compute.\nMiniTron~\\cite{muralidharan2024minitron} combines structured pruning with distillation but modifies architecture permanently.\nAll require retraining or weight modification; our method is a plug-in predictor on \\emph{unmodified} SwiGLU models.\n",
      "numLines": 27,
      "startLine": 1,
      "totalLines": 27
    }
  },
  "sourceToolAssistantUUID": "319adde0-12f8-4b46-a59e-3d92b101dfd6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/review_reviewer_1_772f066c",
  "sessionId": "e4589542-c5a3-4a5b-a779-c62f37dfeb92",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 38 · 2026-05-17T04:48:17.558Z_

<details open><summary>🔧 Tool call — Read · `toolu_01YVDGgwrxEah5LeiuyenMdV`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8df09ee8-6d0c-495b-8785-231f864f5db3",
  "isSidechain": false,
  "requestId": "req_011Cb7Y3P7wxQKwbP5SdAc6F",
  "type": "assistant",
  "uuid": "4ef35024-2ba2-40f5-a327-55fb6f658cd1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/review_reviewer_1_772f066c",
  "sessionId": "e4589542-c5a3-4a5b-a779-c62f37dfeb92",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013LNiYtAdYJuKsjB18Vbj1S",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 15753,
      "cache_read_input_tokens": 31872,
      "output_tokens": 232,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 15753,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 232,
          "cache_read_input_tokens": 31872,
          "cache_creation_input_tokens": 15753,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 15753
          },
          "type": "message"
        }
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

_source line 39 · 2026-05-17T04:48:17.627Z_

```json
{
  "parentUuid": "2425ea49-b05e-426c-8ee5-17b67d75f99c",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "2440385e-bbbb-4030-87c6-19ad4eef0f3a",
  "timestamp": "2026-05-17T04:48:17.627Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/review_reviewer_1_772f066c",
  "sessionId": "e4589542-c5a3-4a5b-a779-c62f37dfeb92",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

---

### Tool call

_source line 40 · 2026-05-17T04:48:20.499Z_

<details open><summary>🔧 Tool call — Read · `toolu_01WKcvvDoBaxPAk6xQ6bZZwD`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2440385e-bbbb-4030-87c6-19ad4eef0f3a",
  "isSidechain": false,
  "requestId": "req_011Cb7Y3mb4Ygv1xbnKNXqmu",
  "type": "assistant",
  "uuid": "24ed4924-3904-4917-926a-60defefffdda",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/review_reviewer_1_772f066c",
  "sessionId": "e4589542-c5a3-4a5b-a779-c62f37dfeb92",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YNcw4QwESwCycdgHzhTrpP",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3631,
      "cache_read_input_tokens": 47625,
      "output_tokens": 160,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3631,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 160,
          "cache_read_input_tokens": 47625,
          "cache_creation_input_tokens": 3631,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3631
          },
          "type": "message"
        }
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

_source line 41 · 2026-05-17T04:48:20.508Z_

<details><summary>↩ Tool result · `toolu_01WKcvvDoBaxPAk6xQ6bZZwD`</summary>

```text
1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	Training sparsity predictors with KL divergence eliminates error compensation networks by coupling all neurons through the output distribution, resolving BCE's structural mismatch with global top-$k$ allocation.
5	The resulting predictor (75.9M params, $<$1\% of base) achieves PPL 11.79 at 50\% sparsity vs.\ 23.31 for TEAL, transfers across SwiGLU architectures of similar scale (within 7\% ratio consistency), and reveals three sparsity regimes governing the quality-allocation tradeoff.
6	
7	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "24ed4924-3904-4917-926a-60defefffdda",
  "isSidechain": false,
  "promptId": "d17f6ff5-7f93-4500-81a7-61caa2f125ae",
  "type": "user",
  "uuid": "c568e774-13ff-46f4-bd1a-572de42cc1e8",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/conclusion.tex",
      "content": "\\section{Conclusion}\n\\label{sec:conclusion}\n\nTraining sparsity predictors with KL divergence eliminates error compensation networks by coupling all neurons through the output distribution, resolving BCE's structural mismatch with global top-$k$ allocation.\nThe resulting predictor (75.9M params, $<$1\\% of base) achieves PPL 11.79 at 50\\% sparsity vs.\\ 23.31 for TEAL, transfers across SwiGLU architectures of similar scale (within 7\\% ratio consistency), and reveals three sparsity regimes governing the quality-allocation tradeoff.\n\n",
      "numLines": 7,
      "startLine": 1,
      "totalLines": 7
    }
  },
  "sourceToolAssistantUUID": "24ed4924-3904-4917-926a-60defefffdda",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/review_reviewer_1_772f066c",
  "sessionId": "e4589542-c5a3-4a5b-a779-c62f37dfeb92",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 42 · 2026-05-17T04:48:20.831Z_

<details open><summary>🔧 Tool call — Read · `toolu_01AWCC1UfZi2SsykGDcJz4YW`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c568e774-13ff-46f4-bd1a-572de42cc1e8",
  "isSidechain": false,
  "requestId": "req_011Cb7Y3mb4Ygv1xbnKNXqmu",
  "type": "assistant",
  "uuid": "69fc7680-9cf3-4fbe-bea9-164b993e46b8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/review_reviewer_1_772f066c",
  "sessionId": "e4589542-c5a3-4a5b-a779-c62f37dfeb92",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YNcw4QwESwCycdgHzhTrpP",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3631,
      "cache_read_input_tokens": 47625,
      "output_tokens": 160,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3631,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 160,
          "cache_read_input_tokens": 47625,
          "cache_creation_input_tokens": 3631,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3631
          },
          "type": "message"
        }
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

_source line 43 · 2026-05-17T04:48:20.841Z_

<details><summary>↩ Tool result · `toolu_01AWCC1UfZi2SsykGDcJz4YW`</summary>

```text
1	% =============================================================================
2	% Direction 1: KL distillation for structured/activation sparsity
3	% =============================================================================
4	
5	@inproceedings{fang2024maskllm,
6	  title = {MaskLLM: Learnable Semi-Structured Sparsity for Large Language Models},
7	  author = {Gongfan Fang and Hongxu Yin and Saurav Muralidharan and Greg Heinrich and Jeff Pool and Jan Kautz and Pavlo Molchanov and Xinchao Wang},
8	  year = {2024},
9	  booktitle = {Advances in Neural Information Processing Systems (NeurIPS)},
10	  url = {https://arxiv.org/abs/2409.17481},
11	}
12	
13	@inproceedings{xu2026spon,
14	  title = {Resting Neurons, Active Insights: Robustify Activation Sparsity for Large Language Models},
15	  author = {Haotian Xu and Jiannan Yang and Tian Gao and Tsui-Wei Weng and Tengfei Ma},
16	  year = {2026},
17	  booktitle = {Proceedings of the International Conference on Machine Learning (ICML)},
18	  url = {https://arxiv.org/abs/2512.12744},
19	}
20	
21	@inproceedings{muralidharan2024minitron,
22	  title = {Compact Language Models via Pruning and Knowledge Distillation},
23	  author = {Saurav Muralidharan and Sharath Turuvekere Sreenivas and Raviraj Joshi and Marcin Chochowski and Mostofa Patwary and Mohammad Shoeybi and Bryan Catanzaro and Jan Kautz and Pavlo Molchanov},
24	  year = {2024},
25	  booktitle = {Advances in Neural Information Processing Systems (NeurIPS)},
26	  url = {https://arxiv.org/abs/2407.14679},
27	}
28	
29	
30	% =============================================================================
31	% Direction 3: SPON and learnable bias correction for sparsity
32	% =============================================================================
33	
34	@article{gautam2026fastforward,
35	  title = {Fast Forward: Accelerating LLM Prefill with Predictive FFN Sparsity},
36	  author = {Aayush Gautam and Mukul Gagrani and Junyoung Park and Mingu Lee and Chiris Lott and Narasimha Reddy},
37	  year = {2026},
38	  journal = {arXiv preprint arXiv:2602.00397},
39	  url = {https://arxiv.org/abs/2602.00397},
40	}
41	
42	
43	% =============================================================================
44	% Direction 4: Predictor-based activation sparsity
45	% =============================================================================
46	
47	@inproceedings{liu2025teal,
48	  title = {Training-Free Activation Sparsity in Large Language Models},
49	  author = {James Liu and Pragaash Ponnusamy and Tianle Cai and Han Guo and Yoon Kim and Ben Athiwaratkun},
50	  year = {2025},
51	  booktitle = {Proceedings of the International Conference on Learning Representations (ICLR)},
52	  url = {https://arxiv.org/abs/2408.14690},
53	}
54	
55	@inproceedings{liu2023dejavu,
56	  title = {Deja Vu: Contextual Sparsity for Efficient LLMs at Inference Time},
57	  author = {Zichang Liu and Jue Wang and Tri Dao and Tianyi Zhou and Binhang Yuan and Zhao Song and Anshumali Shrivastava and Ce Zhang and Yuandong Tian and Christopher Re and Beidi Chen},
58	  year = {2023},
59	  booktitle = {Proceedings of the International Conference on Machine Learning (ICML)},
60	  url = {https://arxiv.org/abs/2310.17157},
61	}
62	
63	@inproceedings{akhauri2024shadowllm,
64	  title = {ShadowLLM: Predictor-based Contextual Sparsity for Large Language Models},
65	  author = {Yash Akhauri and Ahmed F AbouElhamayed and Jordan Dotzel and Zhiru Zhang and Alexander M Rush and Safeen Huda and Mohamed S Abdelfattah},
66	  year = {2024},
67	  booktitle = {Proceedings of the Conference on Empirical Methods in Natural Language Processing (EMNLP)},
68	  url = {https://arxiv.org/abs/2406.16635},
69	}
70	
71	
72	@article{lee2024cats,
73	  title = {CATS: Contextually-Aware Thresholding for Sparsity in Large Language Models},
74	  author = {Donghyun Lee and Je-Yong Lee and Genghan Zhang and Mo Tiwari and Azalia Mirhoseini},
75	  year = {2024},
76	  journal = {arXiv preprint arXiv:2404.08763},
77	  url = {https://arxiv.org/abs/2404.08763},
78	}
79	
80	@inproceedings{zhang2025rsparse,
81	  title = {R-Sparse: Rank-Aware Activation Sparsity for Efficient LLM Inference},
82	  author = {Zhenyu Zhang and Zechun Liu and Yuandong Tian and Harshit Khaitan and Zhangyang Wang and Steven Li},
83	  year = {2025},
84	  booktitle = {Proceedings of the International Conference on Learning Representations (ICLR)},
85	  url = {https://arxiv.org/abs/2504.19449},
86	}
87	
88	@inproceedings{federici2025dip,
89	  title = {Efficient LLM Inference using Dynamic Input Pruning and Cache-Aware Masking},
90	  author = {Marco Federici and Davide Belli and Mart van Baalen and Amir Jalalirad and Andrii Skliar and Bence Major and Markus Nagel and Paul Whatmough},
91	  year = {2024},
92	  booktitle = {Proceedings of Machine Learning and Systems (MLSys)},
93	  url = {https://arxiv.org/abs/2412.01380},
94	}
95	
96	% =============================================================================
97	% Activation function replacement and sparsity enhancement
98	% =============================================================================
99	
100	@inproceedings{mirzadeh2024relu,
101	  title = {ReLU Strikes Back: Exploiting Activation Sparsity in Large Language Models},
102	  author = {Iman Mirzadeh and Keivan Alizadeh and Sachin Mehta and Carlo C Del Mundo and Oncel Tuzel and Golnoosh Samei and Mohammad Rastegari and Mehrdad Farajtabar},
103	  year = {2024},
104	  booktitle = {Proceedings of the International Conference on Learning Representations (ICLR)},
105	  url = {https://arxiv.org/abs/2310.04564},
106	}
107	
108	@article{song2024turbosparse,
109	  title = {Turbo Sparse: Achieving LLM SOTA Performance with Minimal Activated Parameters},
110	  author = {Yixin Song and Haotong Xie and Zhengyan Zhang and Bo Wen and Li Ma and Zeyu Mi and Haibo Chen},
111	  year = {2024},
112	  journal = {arXiv preprint arXiv:2406.05955},
113	  url = {https://arxiv.org/abs/2406.05955},
114	}
115	
116	@inproceedings{song2025prosparse,
117	  title = {ProSparse: Introducing and Enhancing Intrinsic Activation Sparsity within Large Language Models},
118	  author = {Chenyang Song and Xu Han and Zhengyan Zhang and Shengding Hu and Xiyu Shi and Kuai Li and Chen Chen and Zhiyuan Liu and Guangli Li and Tao Yang and Maosong Sun},
119	  year = {2025},
120	  booktitle = {Proceedings of the International Conference on Computational Linguistics (COLING)},
121	  url = {https://arxiv.org/abs/2402.13516},
122	}
123	
124	@article{luo2024sparsinglaw,
125	  title = {Sparsing Law: Towards Large Language Models with Greater Activation Sparsity},
126	  author = {Yuqi Luo and Chenyang Song and Xu Han and Yingfa Chen and Chaojun Xiao and Xiaojun Meng and Liqun Deng and Jiansheng Wei and Zhiyuan Liu and Maosong Sun},
127	  year = {2024},
128	  journal = {arXiv preprint arXiv:2411.02335},
129	  url = {https://arxiv.org/abs/2411.02335},
130	}
131	
132	
133	@inproceedings{song2024powerinfer,
134	  title = {PowerInfer: Fast Large Language Model Serving with a Consumer-grade GPU},
135	  author = {Yixin Song and Zeyu Mi and Haotong Xie and Haibo Chen},
136	  year = {2024},
137	  booktitle = {Proceedings of the ACM Symposium on Operating Systems Principles (SOSP)},
138	  url = {https://arxiv.org/abs/2312.12456},
139	}
140	
141	
142	% =============================================================================
143	% KL distillation for model compression
144	% =============================================================================
145	
146	
147	% =============================================================================
148	% Foundational references
149	% =============================================================================
150	
151	@article{grattafiori2024llama3,
152	  title = {The Llama 3 Herd of Models},
153	  author = {Aaron Grattafiori and Abhimanyu Dubey and Abhinav Jauhri and Abhinav Pandey and Abhishek Kadian and Ahmad Al-Dahle and Aieleen Lakber and Aimin Chen and Ait Mokhtar Salma and Ajay Menon},
154	  year = {2024},
155	  journal = {arXiv preprint arXiv:2407.21783},
156	  url = {https://arxiv.org/abs/2407.21783},
157	}
158	
159	@article{jiang2023mistral,
160	  title = {Mistral 7B},
161	  author = {Albert Q. Jiang and Alexandre Sablayrolles and Arthur Mensch and Chris Bamford and Devendra Singh Chaplot and Diego de las Casas and Florian Bressand and Gianna Lengyel and Guillaume Lample and Lucile Saulnier},
162	  year = {2023},
163	  journal = {arXiv preprint arXiv:2310.06825},
164	  url = {https://arxiv.org/abs/2310.06825},
165	}
166	
167	@inproceedings{jang2017gumbel,
168	  title = {Categorical Reparameterization with Gumbel-Softmax},
169	  author = {Eric Jang and Shixiang Gu and Ben Poole},
170	  year = {2017},
171	  booktitle = {Proceedings of the International Conference on Learning Representations (ICLR)},
172	  url = {https://arxiv.org/abs/1611.01144},
173	}
174	
175	@article{shazeer2020glu,
176	  title = {GLU Variants Improve Transformer},
177	  author = {Noam Shazeer},
178	  year = {2020},
179	  journal = {arXiv preprint arXiv:2002.05202},
180	  url = {https://arxiv.org/abs/2002.05202},
181	}
182	
183	@inproceedings{merity2017pointer,
184	  title = {Pointer Sentinel Mixture Models},
185	  author = {Stephen Merity and Caiming Xiong and James Bradbury and Richard Socher},
186	  year = {2017},
187	  booktitle = {Proceedings of the International Conference on Learning Representations (ICLR)},
188	  url = {https://arxiv.org/abs/1609.07843},
189	}
190	
191	@inproceedings{hinton2015distilling,
192	  title = {Distilling the Knowledge in a Neural Network},
193	  author = {Geoffrey Hinton and Oriol Vinyals and Jeff Dean},
194	  year = {2015},
195	  booktitle = {NeurIPS 2014 Deep Learning Workshop},
196	  url = {https://arxiv.org/abs/1503.02531},
197	}
198	
199	@article{bengio2013ste,
200	  title = {Estimating or Propagating Gradients Through Stochastic Neurons for Conditional Computation},
201	  author = {Yoshua Bengio and Nicholas L\'{e}onard and Aaron Courville},
202	  year = {2013},
203	  journal = {arXiv preprint arXiv:1308.3432},
204	  url = {https://arxiv.org/abs/1308.3432},
205	}
206	
207	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "69fc7680-9cf3-4fbe-bea9-164b993e46b8",
  "isSidechain": false,
  "promptId": "d17f6ff5-7f93-4500-81a7-61caa2f125ae",
  "type": "user",
  "uuid": "a58a6f9c-ed86-48f8-b713-da519fa14c87",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/references.bib",
      "content": "% =============================================================================\n% Direction 1: KL distillation for structured/activation sparsity\n% =============================================================================\n\n@inproceedings{fang2024maskllm,\n  title = {MaskLLM: Learnable Semi-Structured Sparsity for Large Language Models},\n  author = {Gongfan Fang and Hongxu Yin and Saurav Muralidharan and Greg Heinrich and Jeff Pool and Jan Kautz and Pavlo Molchanov and Xinchao Wang},\n  year = {2024},\n  booktitle = {Advances in Neural Information Processing Systems (NeurIPS)},\n  url = {https://arxiv.org/abs/2409.17481},\n}\n\n@inproceedings{xu2026spon,\n  title = {Resting Neurons, Active Insights: Robustify Activation Sparsity for Large Language Models},\n  author = {Haotian Xu and Jiannan Yang and Tian Gao and Tsui-Wei Weng and Tengfei Ma},\n  year = {2026},\n  booktitle = {Proceedings of the International Conference on Machine Learning (ICML)},\n  url = {https://arxiv.org/abs/2512.12744},\n}\n\n@inproceedings{muralidharan2024minitron,\n  title = {Compact Language Models via Pruning and Knowledge Distillation},\n  author = {Saurav Muralidharan and Sharath Turuvekere Sreenivas and Raviraj Joshi and Marcin Chochowski and Mostofa Patwary and Mohammad Shoeybi and Bryan Catanzaro and Jan Kautz and Pavlo Molchanov},\n  year = {2024},\n  booktitle = {Advances in Neural Information Processing Systems (NeurIPS)},\n  url = {https://arxiv.org/abs/2407.14679},\n}\n\n\n% =============================================================================\n% Direction 3: SPON and learnable bias correction for sparsity\n% =============================================================================\n\n@article{gautam2026fastforward,\n  title = {Fast Forward: Accelerating LLM Prefill with Predictive FFN Sparsity},\n  author = {Aayush Gautam and Mukul Gagrani and Junyoung Park and Mingu Lee and Chiris Lott and Narasimha Reddy},\n  year = {2026},\n  journal = {arXiv preprint arXiv:2602.00397},\n  url = {https://arxiv.org/abs/2602.00397},\n}\n\n\n% =============================================================================\n% Direction 4: Predictor-based activation sparsity\n% =============================================================================\n\n@inproceedings{liu2025teal,\n  title = {Training-Free Activation Sparsity in Large Language Models},\n  author = {James Liu and Pragaash Ponnusamy and Tianle Cai and Han Guo and Yoon Kim and Ben Athiwaratkun},\n  year = {2025},\n  booktitle = {Proceedings of the International Conference on Learning Representations (ICLR)},\n  url = {https://arxiv.org/abs/2408.14690},\n}\n\n@inproceedings{liu2023dejavu,\n  title = {Deja Vu: Contextual Sparsity for Efficient LLMs at Inference Time},\n  author = {Zichang Liu and Jue Wang and Tri Dao and Tianyi Zhou and Binhang Yuan and Zhao Song and Anshumali Shrivastava and Ce Zhang and Yuandong Tian and Christopher Re and Beidi Chen},\n  year = {2023},\n  booktitle = {Proceedings of the International Conference on Machine Learning (ICML)},\n  url = {https://arxiv.org/abs/2310.17157},\n}\n\n@inproceedings{akhauri2024shadowllm,\n  title = {ShadowLLM: Predictor-based Contextual Sparsity for Large Language Models},\n  author = {Yash Akhauri and Ahmed F AbouElhamayed and Jordan Dotzel and Zhiru Zhang and Alexander M Rush and Safeen Huda and Mohamed S Abdelfattah},\n  year = {2024},\n  booktitle = {Proceedings of the Conference on Empirical Methods in Natural Language Processing (EMNLP)},\n  url = {https://arxiv.org/abs/2406.16635},\n}\n\n\n@article{lee2024cats,\n  title = {CATS: Contextually-Aware Thresholding for Sparsity in Large Language Models},\n  author = {Donghyun Lee and Je-Yong Lee and Genghan Zhang and Mo Tiwari and Azalia Mirhoseini},\n  year = {2024},\n  journal = {arXiv preprint arXiv:2404.08763},\n  url = {https://arxiv.org/abs/2404.08763},\n}\n\n@inproceedings{zhang2025rsparse,\n  title = {R-Sparse: Rank-Aware Activation Sparsity for Efficient LLM Inference},\n  author = {Zhenyu Zhang and Zechun Liu and Yuandong Tian and Harshit Khaitan and Zhangyang Wang and Steven Li},\n  year = {2025},\n  booktitle = {Proceedings of the International Conference on Learning Representations (ICLR)},\n  url = {https://arxiv.org/abs/2504.19449},\n}\n\n@inproceedings{federici2025dip,\n  title = {Efficient LLM Inference using Dynamic Input Pruning and Cache-Aware Masking},\n  author = {Marco Federici and Davide Belli and Mart van Baalen and Amir Jalalirad and Andrii Skliar and Bence Major and Markus Nagel and Paul Whatmough},\n  year = {2024},\n  booktitle = {Proceedings of Machine Learning and Systems (MLSys)},\n  url = {https://arxiv.org/abs/2412.01380},\n}\n\n% =============================================================================\n% Activation function replacement and sparsity enhancement\n% =============================================================================\n\n@inproceedings{mirzadeh2024relu,\n  title = {ReLU Strikes Back: Exploiting Activation Sparsity in Large Language Models},\n  author = {Iman Mirzadeh and Keivan Alizadeh and Sachin Mehta and Carlo C Del Mundo and Oncel Tuzel and Golnoosh Samei and Mohammad Rastegari and Mehrdad Farajtabar},\n  year = {2024},\n  booktitle = {Proceedings of the International Conference on Learning Representations (ICLR)},\n  url = {https://arxiv.org/abs/2310.04564},\n}\n\n@article{song2024turbosparse,\n  title = {Turbo Sparse: Achieving LLM SOTA Performance with Minimal Activated Parameters},\n  author = {Yixin Song and Haotong Xie and Zhengyan Zhang and Bo Wen and Li Ma and Zeyu Mi and Haibo Chen},\n  year = {2024},\n  journal = {arXiv preprint arXiv:2406.05955},\n  url = {https://arxiv.org/abs/2406.05955},\n}\n\n@inproceedings{song2025prosparse,\n  title = {ProSparse: Introducing and Enhancing Intrinsic Activation Sparsity within Large Language Models},\n  author = {Chenyang Song and Xu Han and Zhengyan Zhang and Shengding Hu and Xiyu Shi and Kuai Li and Chen Chen and Zhiyuan Liu and Guangli Li and Tao Yang and Maosong Sun},\n  year = {2025},\n  booktitle = {Proceedings of the International Conference on Computational Linguistics (COLING)},\n  url = {https://arxiv.org/abs/2402.13516},\n}\n\n@article{luo2024sparsinglaw,\n  title = {Sparsing Law: Towards Large Language Models with Greater Activation Sparsity},\n  author = {Yuqi Luo and Chenyang Song and Xu Han and Yingfa Chen and Chaojun Xiao and Xiaojun Meng and Liqun Deng and Jiansheng Wei and Zhiyuan Liu and Maosong Sun},\n  year = {2024},\n  journal = {arXiv preprint arXiv:2411.02335},\n  url = {https://arxiv.org/abs/2411.02335},\n}\n\n\n@inproceedings{song2024powerinfer,\n  title = {PowerInfer: Fast Large Language Model Serving with a Consumer-grade GPU},\n  author = {Yixin Song and Zeyu Mi and Haotong Xie and Haibo Chen},\n  year = {2024},\n  booktitle = {Proceedings of the ACM Symposium on Operating Systems Principles (SOSP)},\n  url = {https://arxiv.org/abs/2312.12456},\n}\n\n\n% =============================================================================\n% KL distillation for model compression\n% =============================================================================\n\n\n% =============================================================================\n% Foundational references\n% =============================================================================\n\n@article{grattafiori2024llama3,\n  title = {The Llama 3 Herd of Models},\n  author = {Aaron Grattafiori and Abhimanyu Dubey and Abhinav Jauhri and Abhinav Pandey and Abhishek Kadian and Ahmad Al-Dahle and Aieleen Lakber and Aimin Chen and Ait Mokhtar Salma and Ajay Menon},\n  year = {2024},\n  journal = {arXiv preprint arXiv:2407.21783},\n  url = {https://arxiv.org/abs/2407.21783},\n}\n\n@article{jiang2023mistral,\n  title = {Mistral 7B},\n  author = {Albert Q. Jiang and Alexandre Sablayrolles and Arthur Mensch and Chris Bamford and Devendra Singh Chaplot and Diego de las Casas and Florian Bressand and Gianna Lengyel and Guillaume Lample and Lucile Saulnier},\n  year = {2023},\n  journal = {arXiv preprint arXiv:2310.06825},\n  url = {https://arxiv.org/abs/2310.06825},\n}\n\n@inproceedings{jang2017gumbel,\n  title = {Categorical Reparameterization with Gumbel-Softmax},\n  author = {Eric Jang and Shixiang Gu and Ben Poole},\n  year = {2017},\n  booktitle = {Proceedings of the International Conference on Learning Representations (ICLR)},\n  url = {https://arxiv.org/abs/1611.01144},\n}\n\n@article{shazeer2020glu,\n  title = {GLU Variants Improve Transformer},\n  author = {Noam Shazeer},\n  year = {2020},\n  journal = {arXiv preprint arXiv:2002.05202},\n  url = {https://arxiv.org/abs/2002.05202},\n}\n\n@inproceedings{merity2017pointer,\n  title = {Pointer Sentinel Mixture Models},\n  author = {Stephen Merity and Caiming Xiong and James Bradbury and Richard Socher},\n  year = {2017},\n  booktitle = {Proceedings of the International Conference on Learning Representations (ICLR)},\n  url = {https://arxiv.org/abs/1609.07843},\n}\n\n@inproceedings{hinton2015distilling,\n  title = {Distilling the Knowledge in a Neural Network},\n  author = {Geoffrey Hinton and Oriol Vinyals and Jeff Dean},\n  year = {2015},\n  booktitle = {NeurIPS 2014 Deep Learning Workshop},\n  url = {https://arxiv.org/abs/1503.02531},\n}\n\n@article{bengio2013ste,\n  title = {Estimating or Propagating Gradients Through Stochastic Neurons for Conditional Computation},\n  author = {Yoshua Bengio and Nicholas L\\'{e}onard and Aaron Courville},\n  year = {2013},\n  journal = {arXiv preprint arXiv:1308.3432},\n  url = {https://arxiv.org/abs/1308.3432},\n}\n\n",
      "numLines": 207,
      "startLine": 1,
      "totalLines": 207
    }
  },
  "sourceToolAssistantUUID": "69fc7680-9cf3-4fbe-bea9-164b993e46b8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/review_reviewer_1_772f066c",
  "sessionId": "e4589542-c5a3-4a5b-a779-c62f37dfeb92",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Runtime record

_source line 44_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[Round 2 审稿请求]: ## Round 2 审稿任务 — Reviewer 1（方法严谨性 + 实验设计）  ### Venue 信息 - **目标**: EMNLP 2026 via ACL Rolling Review (ARR) May 2026 cycle - **Deadline**: 2026-05-25 - **页数限制**: 正文 8 页 + unlimited refe…",
  "leafUuid": "a58a6f9c-ed86-48f8-b713-da519fa14c87",
  "sessionId": "e4589542-c5a3-4a5b-a779-c62f37dfeb92"
}
```

---

### Runtime record

_source line 45_

```json
{
  "type": "ai-title",
  "aiTitle": "Review Round 2 distill sparse SwiGLU paper",
  "sessionId": "e4589542-c5a3-4a5b-a779-c62f37dfeb92"
}
```

---

### Assistant

_source line 46 · 2026-05-17T04:49:09.416Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have read the full paper. Let me review the specific items from Round 1:

1. **R1-W4**: §3.5 (now §3.6, "Gradient-Based Motivation: BCE vs. KL") - Check if it has been weakened from "theoretical contribution" to "gradient-based motivation" and if empirical gradient SNR data (KL/BCE=5.76×) has been added.

Looking at section 3.6 (method.tex line 111-156):
- The section is titled "Gradient-Based Motivation: BCE vs. KL" (line 111) - yes, it's been reframed as "motivation" rather than "theoretical contribution"


- The empirical verification is now present (line 153-156), showing KL achieves 5.76× higher average SNR than BCE on LLaMA-3.1-8B with C4 calibration data, with particularly strong advantages in early layers (34–156× ratio). So R1-W4 appears to have been addressed.

2. **R1-W5**: Checking Appendix C for the Lagrangian dual update convergence analysis with the convergence table showing 4 targets and their final λ values.

Looking at appendix.tex (Section C, "Lagrangian Training Dynamics", line 110-140), I can see the convergence table exists with the 4 sparsity targets (30%, 40%, 50%, 70%), final λ values, actual sparsity achieved, and deviation metrics. However, the time-series curves tracking how λ and sparsity evolve during training are missing—there's no figure reference for these trajectories. So R1-W5 is partially addressed with the table present but the visualization of the dynamics over training steps still needs to be added.

3. **R1-W3**: Checking for the three-seed statistical power evaluation.

The abstract mentions three-seed evaluation confirming training stability with PPL 11.92 ± 0.07 and coefficient of variation under 1% under uniform allocation, so this appears to be covered. The sample size of n=3 remains unchanged with no real justification beyond the low coefficient of variation—claiming CV<1% is sufficient doesn't address the fundamental lack of statistical power to detect meaningful differences between methods. Let me dig into the technical choices more carefully, starting with how they handle the binary pruning decisions and the penalty formulation they're using.

The multiplicative update for λ (doubling or halving based on constraint violation) is actually a heuristic penalty controller, not a true Lagrangian dual approach. They're calling it "Lagrangian" but it's really just an adaptive penalty method—a standard dual update would be additive based on subgradient information, not multiplicative scaling. It's a practical approach that works, but the terminology is technically misleading.

For the KL divergence choice, they use forward KL which is mean-seeking and forces the sparse model to match the dense model's high-probability predictions. Looking at the gradient analysis, the chain rule decomposition through the KL loss, logits, Jacobian, and Gumbel derivative is sound, and the empirical SNR measurements show KL achieves 5.76× higher signal-to-noise ratio than BCE over 80 steps on C4 data. The early layers show much stronger SNR gains (34-156×) compared to later layers (2-4×), though the exact definition of SNR—whether it's mean-to-std ratio of gradients across steps—isn't explicitly stated in the paper.

However, there are some statistical gaps: the reported performance improvements (18%, 49%, 82%) lack confidence intervals despite being based on just n=3 runs, and the cross-architecture generalization claim of "within 7%" is similarly unsupported by uncertainty quantification. The paper also doesn't provide direct numerical comparisons with DejaVu, CATS, R-Sparse, DIP, or ShadowLLM—it mainly benchmarks against TEAL and BCE baselines. On the experimental side, training on WikiText-103 while evaluating on WikiText-2 keeps the domain consistent, but the 80-step sample for SNR estimation feels thin for drawing strong conclusions.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a58a6f9c-ed86-48f8-b713-da519fa14c87",
  "isSidechain": false,
  "requestId": "req_011Cb7Y41KoZUALQhd9gHuqn",
  "type": "assistant",
  "uuid": "4368ff11-a703-448a-8b7c-ae532fae5e31",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/review_reviewer_1_772f066c",
  "sessionId": "e4589542-c5a3-4a5b-a779-c62f37dfeb92",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014dZL4AfNxjjtnZPGJY7m32",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3986,
      "cache_read_input_tokens": 51256,
      "output_tokens": 1886,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3986,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1886,
          "cache_read_input_tokens": 51256,
          "cache_creation_input_tokens": 3986,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3986
          },
          "type": "message"
        }
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

_source line 47 · 2026-05-17T04:49:09.550Z_

已读完全部论文章节。现在检查 ARR 官方 review form 的完整评分量表。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4368ff11-a703-448a-8b7c-ae532fae5e31",
  "isSidechain": false,
  "requestId": "req_011Cb7Y41KoZUALQhd9gHuqn",
  "type": "assistant",
  "uuid": "1eb5a576-b5e4-4340-949c-4e9da412e517",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/review_reviewer_1_772f066c",
  "sessionId": "e4589542-c5a3-4a5b-a779-c62f37dfeb92",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014dZL4AfNxjjtnZPGJY7m32",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3986,
      "cache_read_input_tokens": 51256,
      "output_tokens": 1886,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3986,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1886,
          "cache_read_input_tokens": 51256,
          "cache_creation_input_tokens": 3986,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3986
          },
          "type": "message"
        }
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

_source line 48 · 2026-05-17T04:49:09.555Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01DnHbZ3Bdrhyn8uhYJyqZNz`</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract the COMPLETE review form with ALL fields, scoring dimensions, their exact scales, and the complete description of each score level. Include all fields such as soundness, excitement, overall assessment, confidence, and any other dimensions."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1eb5a576-b5e4-4340-949c-4e9da412e517",
  "isSidechain": false,
  "requestId": "req_011Cb7Y41KoZUALQhd9gHuqn",
  "type": "assistant",
  "uuid": "c75a2e72-69e4-4a06-baff-3d5ce4c6aac4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/review_reviewer_1_772f066c",
  "sessionId": "e4589542-c5a3-4a5b-a779-c62f37dfeb92",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014dZL4AfNxjjtnZPGJY7m32",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3986,
      "cache_read_input_tokens": 51256,
      "output_tokens": 1886,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3986,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1886,
          "cache_read_input_tokens": 51256,
          "cache_creation_input_tokens": 3986,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3986
          },
          "type": "message"
        }
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

_source line 49 · 2026-05-17T04:49:10.589Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01MqayNTGG4o4RT6XLMyCdFa`</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewerguidelines",
  "prompt": "Extract the key reviewer guidelines: what aspects should reviewers focus on, what counts as major/minor weaknesses, guidance on soundness evaluation, and what makes a good review."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c75a2e72-69e4-4a06-baff-3d5ce4c6aac4",
  "isSidechain": false,
  "requestId": "req_011Cb7Y41KoZUALQhd9gHuqn",
  "type": "assistant",
  "uuid": "e579ec1f-0eca-491b-88d6-3d3520dfdbe8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/review_reviewer_1_772f066c",
  "sessionId": "e4589542-c5a3-4a5b-a779-c62f37dfeb92",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014dZL4AfNxjjtnZPGJY7m32",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3986,
      "cache_read_input_tokens": 51256,
      "output_tokens": 1886,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3986,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1886,
          "cache_read_input_tokens": 51256,
          "cache_creation_input_tokens": 3986,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3986
          },
          "type": "message"
        }
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

_source line 50 · 2026-05-17T04:49:16.292Z_

<details><summary>↩ Tool result · `toolu_01MqayNTGG4o4RT6XLMyCdFa`</summary>

```text
# Key ARR Reviewer Guidelines Summary

## Core Review Focus Areas

Reviewers should concentrate on four main tasks:

1. **Assignment validation** – Confirm expertise match and absence of conflicts of interest
2. **Technical soundness** – Evaluate methodology, proofs, and experimental rigor
3. **Clarity and specificity** – Identify vague claims and missing details
4. **Constructive feedback** – Provide actionable suggestions in professional tone

## Major vs. Minor Weaknesses

**Major weaknesses** include:
- Fundamental methodological flaws or incomplete proofs
- Missing critical comparisons directly relevant to core claims
- Anonymity violations or ethics violations
- Hallucinated references or plagiarism

**Minor weaknesses** (suggestions, not rejection grounds):
- Missing recent preprints or concurrent work
- Potential additional experiments beyond the paper's scope
- Writing improvements or clarity enhancements
- Acknowledged limitations already disclosed by authors

## Soundness Evaluation Guidance

The guidelines emphasize that "soundness scores must be justified by the review text." Key principles include:

- Distinguish between technical validity and personal interest (reflected separately in excitement scores)
- Specify exactly what aspects were checked versus unchecked
- Justify confidence levels through concrete evidence
- Avoid conflating limitations with fundamental flaws

## Hallmarks of Strong Reviews

Effective reviews demonstrate:

- **Specificity**: Reference concrete line numbers, methods, or results rather than vague complaints
- **Evidence-based critique**: Support claims with citations or reasoning
- **Professional tone**: Constructive feedback written as colleague-to-colleague
- **Calibrated expectations**: Assess papers against their stated contributions, not personal preferences
- **Good faith engagement**: Acknowledge author responses and update assessments accordingly
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e579ec1f-0eca-491b-88d6-3d3520dfdbe8",
  "isSidechain": false,
  "promptId": "d17f6ff5-7f93-4500-81a7-61caa2f125ae",
  "type": "user",
  "uuid": "72feb043-15d5-4528-8f4c-53100d8715ac",
  "toolUseResult": {
    "bytes": 100603,
    "code": 200,
    "codeText": "OK",
    "result": "# Key ARR Reviewer Guidelines Summary\n\n## Core Review Focus Areas\n\nReviewers should concentrate on four main tasks:\n\n1. **Assignment validation** – Confirm expertise match and absence of conflicts of interest\n2. **Technical soundness** – Evaluate methodology, proofs, and experimental rigor\n3. **Clarity and specificity** – Identify vague claims and missing details\n4. **Constructive feedback** – Provide actionable suggestions in professional tone\n\n## Major vs. Minor Weaknesses\n\n**Major weaknesses** include:\n- Fundamental methodological flaws or incomplete proofs\n- Missing critical comparisons directly relevant to core claims\n- Anonymity violations or ethics violations\n- Hallucinated references or plagiarism\n\n**Minor weaknesses** (suggestions, not rejection grounds):\n- Missing recent preprints or concurrent work\n- Potential additional experiments beyond the paper's scope\n- Writing improvements or clarity enhancements\n- Acknowledged limitations already disclosed by authors\n\n## Soundness Evaluation Guidance\n\nThe guidelines emphasize that \"soundness scores must be justified by the review text.\" Key principles include:\n\n- Distinguish between technical validity and personal interest (reflected separately in excitement scores)\n- Specify exactly what aspects were checked versus unchecked\n- Justify confidence levels through concrete evidence\n- Avoid conflating limitations with fundamental flaws\n\n## Hallmarks of Strong Reviews\n\nEffective reviews demonstrate:\n\n- **Specificity**: Reference concrete line numbers, methods, or results rather than vague complaints\n- **Evidence-based critique**: Support claims with citations or reasoning\n- **Professional tone**: Constructive feedback written as colleague-to-colleague\n- **Calibrated expectations**: Assess papers against their stated contributions, not personal preferences\n- **Good faith engagement**: Acknowledge author responses and update assessments accordingly",
    "durationMs": 5700,
    "url": "https://aclrollingreview.org/reviewerguidelines"
  },
  "sourceToolAssistantUUID": "e579ec1f-0eca-491b-88d6-3d3520dfdbe8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/review_reviewer_1_772f066c",
  "sessionId": "e4589542-c5a3-4a5b-a779-c62f37dfeb92",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool result

_source line 51 · 2026-05-17T04:49:17.875Z_

<details><summary>↩ Tool result · `toolu_01DnHbZ3Bdrhyn8uhYJyqZNz`</summary>

```text
# ACL Rolling Review Form - Complete Structure

## Primary Evaluation Dimensions

### 1. **Reviewer Confidence** (5-point scale)
- **5**: "Positive that my evaluation is correct. I read the paper very carefully and am familiar with related work."
- **4**: "Quite sure. I tried to check the important points carefully."
- **3**: "Pretty sure, but there's a chance I missed something."
- **2**: "Willing to defend my evaluation, but it is fairly likely that I missed some details."
- **1**: "Not my area, or paper is very hard to understand."

### 2. **Soundness** (1-5 scale with half-point increments)
- **5**: "Excellent: This study is one of the most thorough I have seen."
- **4**: "Strong: This study provides sufficient support for all of its claims."
- **3**: "Acceptable: This study provides sufficient support for its main claims."
- **2**: "Poor: Some of the main claims are not sufficiently supported."
- **1**: "Major Issues: This study is not yet sufficiently thorough to warrant publication."

### 3. **Excitement** (1-5 scale with half-point increments)
- **5**: "Highly Exciting: I would recommend this paper to others."
- **4**: "Exciting: I would mention this paper to others."
- **3**: "Interesting: I might mention some points of this paper."
- **2**: "Potentially Interesting: this paper does not resonate with me."
- **1**: "Not Exciting: this paper does not resonate with me."

### 4. **Overall Assessment** (1-5 scale with half-point increments)
- **5**: "Consider for Award: up to top 2.5% papers"
- **4.5**: "Borderline Award"
- **4**: "Conference: I think this paper could be accepted."
- **3.5**: "Borderline Conference"
- **3**: "Findings: I think this paper could be accepted to the Findings of the ACL."
- **2.5**: "Borderline Findings"
- **2**: "Resubmit next cycle: substantial revisions needed"
- **1.5**: "Resubmit after next cycle: substantial revisions cannot be completed soon"
- **1**: "Do not resubmit"

## Additional Assessment Fields

### 5. **Reproducibility** (1-5 scale)
- **5**: "They could easily reproduce the results."
- **4**: "They could mostly reproduce the results."
- **3**: "They could reproduce the results with some difficulty."
- **2**: "They would be hard pressed to reproduce the results."
- **1**: "They would not be able to reproduce the results."

### 6. **Dataset Value** (1-5 scale)
- **5**: "Enabling: The newly released datasets should affect other people's research projects."
- **4**: "Useful: I would recommend the new datasets to other researchers."
- **3**: "Potentially useful: Someone might find the new datasets useful."
- **2**: "Documentary: useful for study or replication."
- **1**: "No usable datasets submitted."

### 7. **Software Value** (1-5 scale)
- **5**: "Enabling: The newly released software should affect other people's research projects."
- **4**: "Useful: I would recommend the new software to other researchers."
- **3**: "Potentially useful: Someone might find the new software useful."
- **2**: "Documentary: useful for study or replication."
- **1**: "No usable software released."

### 8. **Author Identity Knowledge** (1-5 scale)
- **5**: "From a violation of double-blind-submission rules"
- **4**: "From a preprint or allowed workshop paper"
- **3**: "From the contents of the submission itself"
- **2**: "From social media/a talk/other informal communication"
- **1**: "I do not have even an educated guess about author identity"

## Narrative Sections
- Paper Summary
- Summary of Strengths
- Summary of Weaknesses (numbered)
- Comments/Suggestions/Typos
- Limitations and Societal Impact
- Ethical Concerns
- Needs Ethics Review
- Best Paper Justification
- Optional Author Identity Conjecture
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c75a2e72-69e4-4a06-baff-3d5ce4c6aac4",
  "isSidechain": false,
  "promptId": "d17f6ff5-7f93-4500-81a7-61caa2f125ae",
  "type": "user",
  "uuid": "aa5a8242-606c-4e3f-95a9-8b557e0e9f84",
  "toolUseResult": {
    "bytes": 25365,
    "code": 200,
    "codeText": "OK",
    "result": "# ACL Rolling Review Form - Complete Structure\n\n## Primary Evaluation Dimensions\n\n### 1. **Reviewer Confidence** (5-point scale)\n- **5**: \"Positive that my evaluation is correct. I read the paper very carefully and am familiar with related work.\"\n- **4**: \"Quite sure. I tried to check the important points carefully.\"\n- **3**: \"Pretty sure, but there's a chance I missed something.\"\n- **2**: \"Willing to defend my evaluation, but it is fairly likely that I missed some details.\"\n- **1**: \"Not my area, or paper is very hard to understand.\"\n\n### 2. **Soundness** (1-5 scale with half-point increments)\n- **5**: \"Excellent: This study is one of the most thorough I have seen.\"\n- **4**: \"Strong: This study provides sufficient support for all of its claims.\"\n- **3**: \"Acceptable: This study provides sufficient support for its main claims.\"\n- **2**: \"Poor: Some of the main claims are not sufficiently supported.\"\n- **1**: \"Major Issues: This study is not yet sufficiently thorough to warrant publication.\"\n\n### 3. **Excitement** (1-5 scale with half-point increments)\n- **5**: \"Highly Exciting: I would recommend this paper to others.\"\n- **4**: \"Exciting: I would mention this paper to others.\"\n- **3**: \"Interesting: I might mention some points of this paper.\"\n- **2**: \"Potentially Interesting: this paper does not resonate with me.\"\n- **1**: \"Not Exciting: this paper does not resonate with me.\"\n\n### 4. **Overall Assessment** (1-5 scale with half-point increments)\n- **5**: \"Consider for Award: up to top 2.5% papers\"\n- **4.5**: \"Borderline Award\"\n- **4**: \"Conference: I think this paper could be accepted.\"\n- **3.5**: \"Borderline Conference\"\n- **3**: \"Findings: I think this paper could be accepted to the Findings of the ACL.\"\n- **2.5**: \"Borderline Findings\"\n- **2**: \"Resubmit next cycle: substantial revisions needed\"\n- **1.5**: \"Resubmit after next cycle: substantial revisions cannot be completed soon\"\n- **1**: \"Do not resubmit\"\n\n## Additional Assessment Fields\n\n### 5. **Reproducibility** (1-5 scale)\n- **5**: \"They could easily reproduce the results.\"\n- **4**: \"They could mostly reproduce the results.\"\n- **3**: \"They could reproduce the results with some difficulty.\"\n- **2**: \"They would be hard pressed to reproduce the results.\"\n- **1**: \"They would not be able to reproduce the results.\"\n\n### 6. **Dataset Value** (1-5 scale)\n- **5**: \"Enabling: The newly released datasets should affect other people's research projects.\"\n- **4**: \"Useful: I would recommend the new datasets to other researchers.\"\n- **3**: \"Potentially useful: Someone might find the new datasets useful.\"\n- **2**: \"Documentary: useful for study or replication.\"\n- **1**: \"No usable datasets submitted.\"\n\n### 7. **Software Value** (1-5 scale)\n- **5**: \"Enabling: The newly released software should affect other people's research projects.\"\n- **4**: \"Useful: I would recommend the new software to other researchers.\"\n- **3**: \"Potentially useful: Someone might find the new software useful.\"\n- **2**: \"Documentary: useful for study or replication.\"\n- **1**: \"No usable software released.\"\n\n### 8. **Author Identity Knowledge** (1-5 scale)\n- **5**: \"From a violation of double-blind-submission rules\"\n- **4**: \"From a preprint or allowed workshop paper\"\n- **3**: \"From the contents of the submission itself\"\n- **2**: \"From social media/a talk/other informal communication\"\n- **1**: \"I do not have even an educated guess about author identity\"\n\n## Narrative Sections\n- Paper Summary\n- Summary of Strengths\n- Summary of Weaknesses (numbered)\n- Comments/Suggestions/Typos\n- Limitations and Societal Impact\n- Ethical Concerns\n- Needs Ethics Review\n- Best Paper Justification\n- Optional Author Identity Conjecture",
    "durationMs": 8317,
    "url": "https://aclrollingreview.org/reviewform"
  },
  "sourceToolAssistantUUID": "c75a2e72-69e4-4a06-baff-3d5ce4c6aac4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/review_reviewer_1_772f066c",
  "sessionId": "e4589542-c5a3-4a5b-a779-c62f37dfeb92",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 52 · 2026-05-17T04:49:39.809Z_

<details><summary>Logged reasoning block</summary>

```text
Good, I now have all the information needed to write a comprehensive review. Let me synthesize my findings.

Key issues I've identified:

1. **R1-W4 (Gradient SNR)**: The section is now titled "Gradient-Based Motivation" (§3.6) rather than "theoretical contribution" - this reframing is appropriate. Empirical SNR data is present (5.76× ratio, early/late layer breakdown). However, the SNR definition is never explicitly stated (what exactly is "gradient SNR"? Signal/noise over what?), and 80 steps is a small sample.


2. **R1-W5 (Lagrangian convergence)**: The table shows the final results with targets, λ values, and sparsity deviations, but there are no time-series curves tracking how λ and sparsity evolve during training—the Director specifically requested these trajectories and they're absent.
3. **R1-W3 (n=3 statistical power)**: The sample size remains at n=3 with only CV<1% as justification, which doesn't address the underlying statistical concern.
4. **Lagrangian formulation is misleading**: Equation 9 is actually a penalty method rather than a true Lagrangian dual, and the "dual variable" update mechanism doesn't follow standard Lagrangian principles.
5. **30% sparsity creates a major anomaly**: At this sparsity level, KL global achieves only 25.27% on MMLU while KL uniform reaches 40.61%—a 15 percentage point gap that contradicts the paper's main claim about global top-k being superior, though the paper does acknowledge this limitation.
6. **No actual wall-clock speedup demonstrated**: The paper reports a 6.4% computational overhead and notes that real acceleration depends on sparse kernel support, but the main results only show latency overhead rather than actual speedup gains.
7. **The "within 7%" cross-architecture claim is overstated**: This ratio holds only at ≤50% sparsity (1.24× vs 1.22×), but at 70% the variance jumps to 17% difference, which the paper attributes to differential baseline collapse but the abstract doesn't adequately capture this limitation.
8. **Missing statistical rigor**: No significance tests or confidence intervals are provided for any of the comparisons, so all claims rest on point estimates alone.
9. **Training data overlap concerns**: The model was trained on WikiText-103,

The next chunk addresses evaluation on WikiText-2 from the same source, plus some out-of-distribution testing on C4 that's limited to perplexity metrics without downstream task evaluation on the OOD data.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "aa5a8242-606c-4e3f-95a9-8b557e0e9f84",
  "isSidechain": false,
  "requestId": "req_011Cb7Y8DAoobub1DCWyhzDw",
  "type": "assistant",
  "uuid": "70b5b73b-463e-4752-bc61-cd929aa501a0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/review_reviewer_1_772f066c",
  "sessionId": "e4589542-c5a3-4a5b-a779-c62f37dfeb92",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FaEmYoTnrhVhJwX7qXNg5m",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 425,
      "cache_creation_input_tokens": 2942,
      "cache_read_input_tokens": 55242,
      "output_tokens": 4753,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2942,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 425,
          "output_tokens": 4753,
          "cache_read_input_tokens": 55242,
          "cache_creation_input_tokens": 2942,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2942
          },
          "type": "message"
        }
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

_source line 53 · 2026-05-17T04:49:40.652Z_

论文已全部通读。现在汇总审稿意见。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "70b5b73b-463e-4752-bc61-cd929aa501a0",
  "isSidechain": false,
  "requestId": "req_011Cb7Y8DAoobub1DCWyhzDw",
  "type": "assistant",
  "uuid": "2a372a98-b6c4-48ec-bdb8-1f9e8bc67ae2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/review_reviewer_1_772f066c",
  "sessionId": "e4589542-c5a3-4a5b-a779-c62f37dfeb92",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FaEmYoTnrhVhJwX7qXNg5m",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 425,
      "cache_creation_input_tokens": 2942,
      "cache_read_input_tokens": 55242,
      "output_tokens": 4753,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2942,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 425,
          "output_tokens": 4753,
          "cache_read_input_tokens": 55242,
          "cache_creation_input_tokens": 2942,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2942
          },
          "type": "message"
        }
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

_source line 54 · 2026-05-17T04:51:08.312Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director · `toolu_01E2YntXTsf8YhDyeQc1apZ3`</summary>

```json
{
  "text": "## Round 2 Review — Reviewer 1（方法严谨性 + 实验设计）\n\n### 1. Summary\n\n本文提出用 KL 散度替代 BCE 训练 SwiGLU LLM 的上下文稀疏预测器，通过 Gumbel-Sigmoid 松弛和自适应惩罚系数实现端到端可微训练。方法在 LLaMA-3.1-8B 上 50% 稀疏度达到 PPL 11.79（对比 TEAL 23.31），并在 Mistral-7B 上验证跨架构一致性。论文还提出了二维分类法和三种稀疏 regime 的分析框架。\n\n---\n\n### 2. Strengths\n\n- **核心贡献清晰且可验证**：KL vs BCE 的结构性差异论证（§3.6 梯度分析）逻辑自洽，且有实证 SNR 数据支撑（5.76×）。\n- **消融设计良好**：Table 3 系统隔离了 loss function（ΔP=26.23）vs relaxation method（ΔP=3.98），明确了 KL 是主要贡献因素。BCE+Gumbel+Lagrangian 实验（PPL 38.02）特别有说服力，排除了 Gumbel 本身带来改进的假设。\n- **Iso-compute 分析**（§4.3）：BCE 2700 步 loss 饱和（Δ=-0.006）证明了结构性失败而非计算不足。\n- **Cross-architecture 验证**：两个不同架构（LLaMA/Mistral）上 advantage ratio 的一致性（≤50% 时 within 7%）增强了泛化性 claim 的可信度。\n- **Regime 分析有实用价值**：budget-surplus/constrained/capacity-limited 三分法对实践者选择稀疏度有指导意义。\n- **Limitations 诚实**：明确承认无实际加速、仅 7-8B 模型、per-target 训练的限制。\n\n---\n\n### 3. Weaknesses\n\n**W1 [critical] \"Lagrangian\" 术语不准确，非标准对偶方法**\n- 具体位置：§3.5, Eq. 9-10\n- 问题：Eq. 9 是带 deadzone 的二次惩罚项 λ·clamp(|s̄-(1-ρ)|-ε, min=0)²，Eq. 10 的更新规则是几何倍增/减半（×2/×0.5），这既不是标准 augmented Lagrangian（需 λ ← λ + η·violation），也不是对偶上升法。将其称为 \"Lagrangian\" 和 \"dual variable\" 存在术语误导。这是一个带自适应权重的惩罚方法（penalty method with adaptive coefficient）。\n- 影响：审稿人可能质疑作者对优化理论的理解深度；更重要的是，penalty method 不保证满足 KKT 条件，论文也未讨论这一局限。\n- 建议：(1) 改称 \"adaptive penalty controller\" 或明确说明这是对 Lagrangian 的工程化简化；(2) 讨论为何不使用标准对偶上升以及当前方案的收敛保证。\n\n**W2 [critical] Appendix C 缺少 λ/sparsity 时序曲线（R1-W5 未完全修复）**\n- 具体位置：Appendix C (§C, Table 7)\n- 问题：Table 7 仅报告最终状态（final λ + actual sparsity + deviation），满足\"是否收敛\"的验证。但缺少训练过程中 λ 和 actual sparsity 随 step 变化的时序曲线。Director 明确要求 \"还需 λ/sparsity 时序曲线\"。\n- 为什么重要：(1) 30% 和 70% target 的 λ 均 hit cap（5000 和 1000），表明系统可能在 cap boundary 震荡而非真正收敛；(2) 文中提到 \"最后 ~100 步 loss 轻微上升\"（Appendix C 末段），时序曲线可以展示这是否与 λ 动态相关；(3) 无曲线无法验证 \"~10 步达到稳态\" 的 claim。\n- 建议：补充 Figure 展示至少 30%/50%/70% 三个 target 的 (step, λ) 和 (step, actual_sparsity) 曲线。\n\n**W3 [warning] 梯度 SNR 定义不明确且样本量小**\n- 具体位置：§3.6, \"Empirical verification\" 段落\n- 问题：(1) \"gradient SNR\" 未给出数学定义——是 mean(|grad|)/std(|grad|) over steps? over neurons? over layers? 读者无法 verify 或 reproduce 这个数字。(2) 仅 80 步的测量，对于 SNR 估计（尤其是分层报告 early/late layers）样本量偏小。(3) 数值 5.77×10⁻⁵ vs 1.00×10⁻⁵ 的 ratio 是 5.77×，但文中写 \"5.76×\"——小数点精度不一致。\n- 建议：(1) 明确 SNR 的数学公式；(2) 增加到至少 200+ steps 或报告 bootstrap CI；(3) 修正 5.77/1.00=5.77 vs claim 5.76 的不一致。\n\n**W4 [warning] n=3 seeds 统计效力不足（R1-W3 未改善）**\n- 具体位置：§4.7, Appendix E\n- 问题：论文仍使用 3 seeds，仅以 CV<1% 作为 justification。CV<1% 说明方法 variance 小，但不等于效力足够检测方法间差异。对于主表中 KL global (11.79) vs KL uniform (11.96) 之差（0.17），以 std=0.07 计算，即使 paired t-test 也仅有 n=3 自由度=2，无法确信 p<0.05。\n- 此外，cross-arch claim \"within 7%\" 完全基于点估计（无 CI），无法区分真实差异与噪声。\n- 建议：(1) 至少补充 5 seeds，或明确声明 \"global vs uniform 差异不显著\"；(2) 对 cross-arch ratio 报告 bootstrap CI。\n\n**W5 [warning] 无实际推理加速，且 overhead 表述可能误导读者**\n- 具体位置：Appendix A, Table 5\n- 问题：论文动机强调 \"reduces effective computation\"（Abstract 第一句），但实测增加 6.4% latency overhead。虽然 Limitations 中诚实说明了这一点，但 Abstract/Introduction 的 framing 可能让读者期望实际加速。\"Eliminating compensation network\" 节省的 2.7% latency 被 predictor 自身的 6.4% overhead 抵消，net effect 是变慢。\n- 建议：Abstract 首句明确 \"prediction quality\" 而非暗示 \"reduces computation\"；或在 Experiments 主文中简要说明当前无加速。\n\n**W6 [info] 30% 稀疏度 MMLU 异常未充分解释**\n- 具体位置：Table 2, §4.5\n- 问题：KL global 在 30% 稀疏度的 MMLU 仅 25.27%（接近随机），而 KL uniform 达 40.61%。这是 15pp 差异，暗示全局分配在低稀疏度时 actively harmful for knowledge tasks。论文将此归因于 \"global top-k starves knowledge-critical layers\"，但缺乏进一步分析：具体哪些 layers 被 starved？layer-wise allocation 分布是什么样？\n- 建议：补充 30% 稀疏度下 global top-k 的 per-layer 实际保留率分布，验证 \"starve\" 假设。\n\n---\n\n### 4. Round 1 Issue Status\n\n| Issue | Status | 评估 |\n|-------|--------|------|\n| **R1-W4** (gradient motivation reframing + SNR data) | ✅ 基本完成 | §3.6 标题改为 \"Gradient-Based Motivation\"，framing 合理。SNR 5.76× 数据已添加且与 layer-depth 理论一致。但 SNR 定义不明确（see W3 above）。 |\n| **R1-W5** (Lagrangian convergence) | ⚠️ 部分完成 | Table 7 提供了 4 targets 的最终收敛状态，满足基本验证。但缺少 λ/sparsity 时序曲线（see W2 above），且两个 target hit cap 的情况未充分讨论。 |\n| **R1-W3** (n=3 statistical power) | ❌ 未改善 | 仍为 3 seeds，仅增加了 downstream metric 的 std 报告。未增加 seed 数量，也未提供 adequate justification（如 power analysis 或 paired comparison CI）。 |\n\n---\n\n### 5. Questions for Authors\n\n1. Eq. 10 的几何倍增如何保证收敛？当 λ hit cap 时（30%: λ=5000, 70%: λ=1000），是否意味着约束无法被精确满足？30% 的 5% deviation 是否可接受？\n2. Gradient SNR 的精确定义是什么？是 E[grad²] / Var[grad] 还是 |E[grad]| / std(grad)？over what dimensions (neurons? steps? sequences)?\n3. 如果将 KL global 在 30% 稀疏度的 MMLU 25.27% 与 dense 的 65.27% 比较，这是 40pp 的退化。论文推荐的实际使用方案是什么——30% uniform？还是 50% global？\n4. BCE+Gumbel+Lagrangian (PPL 38.02) 比 vanilla BCE (27.97) 更差，作者解释为 \"Lagrangian 干扰 per-neuron optimization\"。但这是否也说明 Gumbel-Sigmoid 本身引入了噪声？如果去掉 Lagrangian 只用 BCE+Gumbel 结果如何？\n5. 论文 claim SPON cosine similarity 0.196 为 \"near-orthogonal\"，但 0.196 并不特别接近 0。在 14336 维空间中，随机向量的 expected cosine similarity ≈ 0。0.196 是否实际上表示 moderate positive correlation？\n\n---\n\n### 6. Missing References\n\n- **Wanda (Sun et al., 2024)**: 结构化/非结构化剪枝的重要 baseline，尤其在讨论 neuron importance 时应对比。\n- **SparseGPT (Frantar & Alistarh, 2023)**: one-shot pruning 的代表方法，作为 broader pruning landscape 的参照。\n- **Mixture-of-Experts (Fedus et al., 2022)**: conditional computation 的另一范式，Related Work 中应 acknowledge。\n- 缺少对 Gumbel-Sigmoid 变体的直接引用——Jang et al. 2017 是 Gumbel-Softmax (categorical)，Gumbel-Sigmoid (binary) 的标准引用应为 Maddison et al. 2017 (Concrete distribution) 或 Louizos et al. 2018 (L0 regularization)。\n\n---\n\n### 7. Overall Assessment\n\n**Soundness**: 3.5/5\n核心 KL vs BCE 的结构性论证正确且实验支撑充分。但 \"Lagrangian\" 术语误用、SNR 定义缺失、n=3 统计效力不足降低了 rigor。消融实验设计良好。\n\n**Excitement**: 3.5/5\n贡献有实用价值（消除 compensation network、regime 分析），但 scope 限于 7-8B 模型 + WikiText，且无实际加速演示，限制了 impact。\n\n**Reproducibility**: 4/5\n超参数详尽，实验 protocol 清晰。缺少代码发布承诺和 SNR 测量的精确定义。\n\n**Overall**: 3.5 (Borderline Conference)\n论文有一个清晰的核心贡献（KL training for sparsity prediction），消融充分，跨架构验证有说服力。但 Lagrangian 术语问题（W1）和缺少收敛曲线（W2）是方法严谨性的硬伤；n=3 统计效力（W4）和 SNR 定义缺失（W3）进一步削弱可信度。如果 W1+W2 能在 revision 中修复（改称 penalty method + 补充曲线），且 W3 的 SNR 给出明确定义，可升至 weak accept。\n\n**Confidence**: 4/5\n\"Quite sure. I tried to check the important points carefully.\" 对优化理论和稀疏推理均有经验，仔细检查了梯度推导和实验设计。",
  "reviewer_id": "1",
  "project": "distill_sparse_swiglu"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2a372a98-b6c4-48ec-bdb8-1f9e8bc67ae2",
  "isSidechain": false,
  "requestId": "req_011Cb7Y8DAoobub1DCWyhzDw",
  "type": "assistant",
  "uuid": "47e1162a-15d7-452a-80e8-afd8e9fdb147",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/review_reviewer_1_772f066c",
  "sessionId": "e4589542-c5a3-4a5b-a779-c62f37dfeb92",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FaEmYoTnrhVhJwX7qXNg5m",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 425,
      "cache_creation_input_tokens": 2942,
      "cache_read_input_tokens": 55242,
      "output_tokens": 4753,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2942,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 425,
          "output_tokens": 4753,
          "cache_read_input_tokens": 55242,
          "cache_creation_input_tokens": 2942,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2942
          },
          "type": "message"
        }
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
  "lastPrompt": "[Round 2 审稿请求]: ## Round 2 审稿任务 — Reviewer 1（方法严谨性 + 实验设计）  ### Venue 信息 - **目标**: EMNLP 2026 via ACL Rolling Review (ARR) May 2026 cycle - **Deadline**: 2026-05-25 - **页数限制**: 正文 8 页 + unlimited refe…",
  "leafUuid": "47e1162a-15d7-452a-80e8-afd8e9fdb147",
  "sessionId": "e4589542-c5a3-4a5b-a779-c62f37dfeb92"
}
```

---

### Runtime record

_source line 56_

```json
{
  "type": "ai-title",
  "aiTitle": "Review Round 2 distill sparse SwiGLU paper",
  "sessionId": "e4589542-c5a3-4a5b-a779-c62f37dfeb92"
}
```

---

### Tool result

_source line 57 · 2026-05-17T04:51:12.636Z_

<details><summary>↩ Tool result · `toolu_01E2YntXTsf8YhDyeQc1apZ3`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director\"}, \"error\": \"\"}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "47e1162a-15d7-452a-80e8-afd8e9fdb147",
  "isSidechain": false,
  "promptId": "d17f6ff5-7f93-4500-81a7-61caa2f125ae",
  "type": "user",
  "uuid": "1279924b-bc7d-4621-b6d1-42b380c336de",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"review_director_key\\\": \\\"feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director\\\"}, \\\"error\\\": \\\"\\\"}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director\"}, \"error\": \"\"}"
    }
  },
  "sourceToolAssistantUUID": "47e1162a-15d7-452a-80e8-afd8e9fdb147",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/review_reviewer_1_772f066c",
  "sessionId": "e4589542-c5a3-4a5b-a779-c62f37dfeb92",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Runtime record

_source line 58_

```json
{
  "type": "ai-title",
  "aiTitle": "Review Round 2 distill sparse SwiGLU paper",
  "sessionId": "e4589542-c5a3-4a5b-a779-c62f37dfeb92"
}
```

---

### Runtime record

_source line 59 · 2026-05-17T04:52:13.443Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-17T04:52:13.443Z",
  "sessionId": "e4589542-c5a3-4a5b-a779-c62f37dfeb92",
  "content": "[Round 2 审稿请求]:\n## 交叉分享 — Reviewer 2 的完整审稿意见\n\n请逐条回应 Reviewer 2 的每个 Weakness：对每一条标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n以下是 Reviewer 2 的完整审稿意见：\n\n### Summary\nThis paper proposes training lightweight MLP sparsity predictors with KL divergence (instead of BCE) combined with Gumbel-Sigmoid relaxation to predict which FFN neurons to prune at inference in SwiGLU-based LLMs. The key argument is that KL couples all neurons through the output distribution, resolving BCE's structural mismatch with global top-k allocation. Experiments on LLaMA-3.1-8B and Mistral-7B show substantial PPL improvements over TEAL baselines, with analysis of sparsity regimes and a 2D taxonomy positioning the contribution.\n\n### Strengths\n- Clear structural argument: The BCE vs. KL gradient analysis (§3.5) is well-motivated and the formal derivation (Eq. 7-8) makes the \"coupling through downstream Jacobian\" argument concrete and verifiable.\n- Thorough ablation design: The loss-function isolation experiment (BCE + Gumbel + Lagrangian → PPL 38.02) cleanly demonstrates that the KL objective, not the relaxation mechanism, is the decisive factor.\n- Honest limitations: The paper explicitly acknowledges that 6.4% overhead does NOT translate to speedup without sparse kernels, and that PPL is a poor proxy for reasoning (§4.4). The regime analysis (budget-surplus vs. capacity-limited) is a genuinely useful framework.\n- Reproducibility: Training details are sufficient (1000 steps, WikiText-103, batch=4, AdamW, lr=1e-3, cosine decay). Three-seed variance reported.\n- SPON orthogonality analysis is convincing: Cosine similarity 0.196 with quantitative PPL decomposition clearly separates the two methods' contributions.\n\n### Weaknesses\n\n**W1 [critical] — Novelty is incremental: known components in a predictable configuration**\nThe paper combines: (1) KL distillation (standard in model compression since Hinton 2015), (2) Gumbel-Sigmoid relaxation (Jang et al. 2017), (3) lightweight MLP predictor (DejaVu 2023). The 2D taxonomy frames this as \"filling an unexplored cell,\" but the combination is the obvious next step once you observe that SPON uses KL (static) and FastForward uses per-token (BCE). A reviewer could ask: why hadn't anyone done this already? If the answer is \"it's straightforward to combine,\" the novelty bar for a main conference paper may not be met.\n\n**W2 [critical] — The \"relative advantage grows with sparsity\" claim is partially an artifact of baseline collapse**\nThe paper's central scaling narrative (18% → 49% → 82% advantage) measures (TEAL - KL) / TEAL. When TEAL collapses from 23.31 to 100.11, any reasonable method will show a growing \"relative advantage.\" It would be more informative to report KL/Dense ratio across sparsity levels: 1.47× at 30%, 1.93× at 50%, 2.93× at 70%.\n\n**W3 [warning] — Scale limitation undermines generality claims**\nOnly two models tested (LLaMA-3.1-8B and Mistral-7B-v0.3), both 7-8B parameters with SwiGLU. No experiments on 13B, 70B, or non-SwiGLU architectures. Introduction/Abstract still frame it as if it's a general structural property.\n\n**W4 [warning] — Downstream task collapse at 50% sparsity raises practical concerns**\nAt 50% sparsity, all methods collapse on MMLU (27.89% ≈ random) and GSM8K (<2.2%). At 30%, KL-global hurts MMLU (25.27% vs. TEAL 38.61%). The practical operating point is ≤30%, where PPL advantage is modest (8.98 vs. 10.97).\n\n**W5 [warning] — Em-dash usage signals AI-generated text**\n12+ instances of explanatory em-dashes (---) in running text across introduction.tex, method.tex, abstract.tex, related_work.tex.\n\n**W6 [warning] — \"Lagrangian\" formulation is misleading terminology**\nEq. 7-8 describe a squared penalty with deadzone and multiplicative weight update, not a true Lagrangian relaxation. \"Adaptive penalty method\" would be more accurate.\n\n**W7 [info] — Reference count is low for EMNLP**\n22 unique references is below typical EMNLP papers (30-50). Missing: MoE, Wanda, SparseGPT, sequence-level KD, Triton.\n\n### Questions for Authors\n1. Have you measured per-neuron prediction accuracy of the KL predictor against the oracle top-k mask?\n2. What happens when you train a single predictor on multiple sparsity targets?\n3. The gradient SNR analysis reports absolute values of ~10⁻⁵. Is this measured on the raw gradient or after optimizer adaptation?\n4. At 30% sparsity, KL-global MMLU (25.27%) is significantly worse than both TEAL (38.61%) and KL-uniform (40.61%). Can you explain why?\n\n### Overall Score\n3/5 (Findings) — Solid execution of a logical idea with clear experimental validation, but novelty is incremental and scale is limited. Suitable for Findings of EMNLP rather than the main conference.\nConfidence: 4/5"
}
```

---

### Runtime record

_source line 60 · 2026-05-17T04:52:13.443Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-17T04:52:13.443Z",
  "sessionId": "e4589542-c5a3-4a5b-a779-c62f37dfeb92"
}
```

---

## Round 2

2 recorded events

### User

_source line 61 · 2026-05-17T04:52:13.432Z_

Continue from where you left off.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1279924b-bc7d-4621-b6d1-42b380c336de",
  "isSidechain": false,
  "promptId": "fa245021-979b-4942-9f52-416e04a360db",
  "type": "user",
  "isMeta": true,
  "uuid": "9084b1f5-1500-4f7e-a6dd-5bf7d4f4ed63",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/review_reviewer_1_772f066c",
  "sessionId": "e4589542-c5a3-4a5b-a779-c62f37dfeb92",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 62 · 2026-05-17T04:52:13.432Z_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9084b1f5-1500-4f7e-a6dd-5bf7d4f4ed63",
  "isSidechain": false,
  "type": "assistant",
  "uuid": "70945a68-52c0-4a02-8c2c-4bbcedf77d0b",
  "isApiErrorMessage": false,
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/review_reviewer_1_772f066c",
  "sessionId": "e4589542-c5a3-4a5b-a779-c62f37dfeb92",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "id": "88f82ea0-48a8-4d03-868b-545fe4e0eb03",
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

4 recorded events

### User

_source line 63 · 2026-05-17T04:52:13.575Z_

[Round 2 审稿请求]:
## 交叉分享 — Reviewer 2 的完整审稿意见

请逐条回应 Reviewer 2 的每个 Weakness：对每一条标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。

---

以下是 Reviewer 2 的完整审稿意见：

### Summary
This paper proposes training lightweight MLP sparsity predictors with KL divergence (instead of BCE) combined with Gumbel-Sigmoid relaxation to predict which FFN neurons to prune at inference in SwiGLU-based LLMs. The key argument is that KL couples all neurons through the output distribution, resolving BCE's structural mismatch with global top-k allocation. Experiments on LLaMA-3.1-8B and Mistral-7B show substantial PPL improvements over TEAL baselines, with analysis of sparsity regimes and a 2D taxonomy positioning the contribution.

### Strengths
- Clear structural argument: The BCE vs. KL gradient analysis (§3.5) is well-motivated and the formal derivation (Eq. 7-8) makes the "coupling through downstream Jacobian" argument concrete and verifiable.
- Thorough ablation design: The loss-function isolation experiment (BCE + Gumbel + Lagrangian → PPL 38.02) cleanly demonstrates that the KL objective, not the relaxation mechanism, is the decisive factor.
- Honest limitations: The paper explicitly acknowledges that 6.4% overhead does NOT translate to speedup without sparse kernels, and that PPL is a poor proxy for reasoning (§4.4). The regime analysis (budget-surplus vs. capacity-limited) is a genuinely useful framework.
- Reproducibility: Training details are sufficient (1000 steps, WikiText-103, batch=4, AdamW, lr=1e-3, cosine decay). Three-seed variance reported.
- SPON orthogonality analysis is convincing: Cosine similarity 0.196 with quantitative PPL decomposition clearly separates the two methods' contributions.

### Weaknesses

**W1 [critical] — Novelty is incremental: known components in a predictable configuration**
The paper combines: (1) KL distillation (standard in model compression since Hinton 2015), (2) Gumbel-Sigmoid relaxation (Jang et al. 2017), (3) lightweight MLP predictor (DejaVu 2023). The 2D taxonomy frames this as "filling an unexplored cell," but the combination is the obvious next step once you observe that SPON uses KL (static) and FastForward uses per-token (BCE). A reviewer could ask: why hadn't anyone done this already? If the answer is "it's straightforward to combine," the novelty bar for a main conference paper may not be met.

**W2 [critical] — The "relative advantage grows with sparsity" claim is partially an artifact of baseline collapse**
The paper's central scaling narrative (18% → 49% → 82% advantage) measures (TEAL - KL) / TEAL. When TEAL collapses from 23.31 to 100.11, any reasonable method will show a growing "relative advantage." It would be more informative to report KL/Dense ratio across sparsity levels: 1.47× at 30%, 1.93× at 50%, 2.93× at 70%.

**W3 [warning] — Scale limitation undermines generality claims**
Only two models tested (LLaMA-3.1-8B and Mistral-7B-v0.3), both 7-8B parameters with SwiGLU. No experiments on 13B, 70B, or non-SwiGLU architectures. Introduction/Abstract still frame it as if it's a general structural property.

**W4 [warning] — Downstream task collapse at 50% sparsity raises practical concerns**
At 50% sparsity, all methods collapse on MMLU (27.89% ≈ random) and GSM8K (<2.2%). At 30%, KL-global hurts MMLU (25.27% vs. TEAL 38.61%). The practical operating point is ≤30%, where PPL advantage is modest (8.98 vs. 10.97).

**W5 [warning] — Em-dash usage signals AI-generated text**
12+ instances of explanatory em-dashes (---) in running text across introduction.tex, method.tex, abstract.tex, related_work.tex.

**W6 [warning] — "Lagrangian" formulation is misleading terminology**
Eq. 7-8 describe a squared penalty with deadzone and multiplicative weight update, not a true Lagrangian relaxation. "Adaptive penalty method" would be more accurate.

**W7 [info] — Reference count is low for EMNLP**
22 unique references is below typical EMNLP papers (30-50). Missing: MoE, Wanda, SparseGPT, sequence-level KD, Triton.

### Questions for Authors
1. Have you measured per-neuron prediction accuracy of the KL predictor against the oracle top-k mask?
2. What happens when you train a single predictor on multiple sparsity targets?
3. The gradient SNR analysis reports absolute values of ~10⁻⁵. Is this measured on the raw gradient or after optimizer adaptation?
4. At 30% sparsity, KL-global MMLU (25.27%) is significantly worse than both TEAL (38.61%) and KL-uniform (40.61%). Can you explain why?

### Overall Score
3/5 (Findings) — Solid execution of a logical idea with clear experimental validation, but novelty is incremental and scale is limited. Suitable for Findings of EMNLP rather than the main conference.
Confidence: 4/5

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "70945a68-52c0-4a02-8c2c-4bbcedf77d0b",
  "isSidechain": false,
  "promptId": "fa245021-979b-4942-9f52-416e04a360db",
  "type": "user",
  "uuid": "fb3ebc3f-cfb2-431e-b918-63dd5ec85e11",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/review_reviewer_1_772f066c",
  "sessionId": "e4589542-c5a3-4a5b-a779-c62f37dfeb92",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 64 · 2026-05-17T04:52:28.717Z_

<details><summary>Logged reasoning block</summary>

```text
The Director wants me to respond to each of Reviewer 2's weaknesses with [AGREE] or [REBUT], citing specific evidence from the paper. Let me go through each one carefully.

**W1 [critical] — Novelty is incremental**: This is a judgment call. I need to decide whether I agree the combination is "obvious" or whether there's genuine novelty. The paper does combine known components, but the key question is whether the combination is trivial. The fact that BCE+Gumbel+Lagrangian (PPL 38.02) is WORSE than vanilla BCE (27.97) suggests the combination is NOT straightforward - you can't just plug in Gumbel and expect it to work with any loss. The KL objective is the critical ingredient. 

On the other hand, using KL for distillation is standard practice, so I need to weigh whether the specific application here constitutes meaningful novelty or just a reasonable engineering choice.

**W2 [critical] — Relative advantage artifact**: This is a valid statistical point. When baseline collapses, relative advantage inflates. The KL/Dense ratio framing would be more informative.

**W3 [warning] — Scale limitation**: Valid. Only 7-8B models.

**W4 [warning] — Downstream collapse**: Valid concern. The practical operating point is limited.

**W5 [warning] — Em-dash usage**: I should verify this. LaTeX "---" produces em-dashes, and I recall seeing this in abstract.tex and the introduction, so this appears to be accurate.

**W6 [warning] — Lagrangian terminology**: I already flagged this as W1 in my own review, so I should acknowledge the overlap.

**W7 [info] — Reference count**: I noted similar gaps in citations, so I can partially agree with this point.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fb3ebc3f-cfb2-431e-b918-63dd5ec85e11",
  "isSidechain": false,
  "requestId": "req_011Cb7YMAThPCY6fpgaNCcGT",
  "type": "assistant",
  "uuid": "4bb80bb3-f531-43ee-9999-047be119302b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/review_reviewer_1_772f066c",
  "sessionId": "e4589542-c5a3-4a5b-a779-c62f37dfeb92",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JnfGtwrMA3U5L1x4uhkH7f",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 53075,
      "cache_read_input_tokens": 11841,
      "output_tokens": 2898,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 53075,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 2898,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 53075,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 53075
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "system_changed",
        "cache_missed_input_tokens": 35353
      }
    }
  }
}
```

</details>

---

### Tool call

_source line 65 · 2026-05-17T04:53:21.335Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director · `toolu_01MX3CWn9YhSf5fhk2qmiBUK`</summary>

```json
{
  "text": "## 交叉回应 — Reviewer 1 对 Reviewer 2 意见的逐条回应\n\n---\n\n**[REBUT] R2-W1: Novelty is incremental**\n\n不完全同意 \"predictable combination\" 的判断。关键证据是 Table 3 的 BCE+Gumbel+Lagrangian 实验（PPL 38.02）：如果组合是 \"obvious\"，那为什么将 Gumbel-Sigmoid 和 Lagrangian 直接应用于 BCE 反而比 vanilla BCE（27.97）更差？这说明 Gumbel 松弛与 loss function 之间存在非平凡的交互——Lagrangian penalty 在 BCE 下会干扰 per-neuron optimization（§4.4 第三段明确讨论）。仅仅 \"填表格\" 不足以构成贡献，但论文的核心洞察不是 \"KL 比 BCE 好\" 这个 general statement，而是具体机制：BCE 梯度 factorize per-neuron（Eq. 8）导致无法学到 global top-k 所需的 inter-neuron coupling。这个 mismatch 的诊断（§3.6 gradient analysis）+ 实证验证（iso-compute saturation）超越了简单 component combination。\n\n但 R2 的质疑并非无理：论文 2D taxonomy 的 framing 确实有 \"填空\" 嫌疑，且 KL distillation 本身不新。如果这篇论文去掉 gradient analysis 和 regime analysis，只剩 \"KL 比 BCE 好\"，那确实 incremental。目前版本的 contribution 在 borderline。\n\n---\n\n**[AGREE] R2-W2: Relative advantage 部分是 baseline collapse 的 artifact**\n\n完全同意。(TEAL-KL)/TEAL 作为 metric 在 TEAL 崩溃时会 inflate。Table 4 数据：\n- 30%: KL/Dense = 8.98/6.12 = 1.47×\n- 50%: KL/Dense = 11.79/6.12 = 1.93×\n- 70%: KL/Dense = 17.91/6.12 = 2.93×\n\n这个 framing 更诚实地反映了 KL predictor 自身的质量退化曲线。论文 Abstract 第 5 行 \"18% at 30%, 49% at 50%, and 82% at 70%\" 的叙事过度依赖于 TEAL 的失败来 inflate 自己的优势。建议作者至少同时报告 KL/Dense ratio。\n\n不过补充一点：即使 reframe 为 KL/Dense，从 1.47× 到 2.93× 的增长仍然表明 KL predictor 在高稀疏度下也显著退化（dense 到 2.93× 的 gap 并不小）。这更凸显了 capacity-limited regime（§4.5）的诚实性。\n\n---\n\n**[AGREE] R2-W3: Scale limitation undermines generality claims**\n\n同意。两个 7-8B SwiGLU 模型不足以支撑 \"structural property of SwiGLU networks\"（§4.6 末句）的泛化 claim。尤其是：\n- 13B/70B 模型的 layer 数和 d_ff 不同，Jacobian chain（factor (b) in Eq. 12）的 depth 效应可能质变\n- Limitations 中承认了这一点，但 Introduction 和 Abstract 的 framing 仍然偏 general\n\n不过严格来说，论文使用的措辞是 \"transfers across SwiGLU architectures of similar scale\"（Abstract 第 6 行），加了 \"of similar scale\" 的限定词，这在 Round 1 后已有改进。问题在于 §4.6 最后一句 \"evidence that the method exploits a structural property of SwiGLU networks\" 仍然过强——应加 \"at 7-8B scale\" 限定。\n\n---\n\n**[AGREE] R2-W4: Downstream collapse raises practical concerns**\n\n同意这是一个重要的实践限制。数据支撑：\n- 50% sparsity: MMLU 27.89% ≈ random（Table 2）\n- 30% KL-global: MMLU 25.27%，甚至比 TEAL 的 38.61% 更差（Table 2）\n- 实际推荐操作点仅为 30% uniform（MMLU 40.61%），PPL 优势仅 8.82 vs 10.97\n\n论文的 regime 分析（§4.5）诚实地展示了这些数据，并且 Limitations 中推荐 30% 为 \"recommended operating point for downstream fidelity\"。但 R2 的批评是合理的：如果实际有用的区间只有 ≤30%，那 50%/70% 的大幅 PPL 优势在实践中意义有限（downstream 都崩了）。\n\n论文核心贡献仍然成立（方法论 + 分析框架），但 impact 确实被这一限制约束。\n\n---\n\n**[REBUT] R2-W5: Em-dash usage signals AI-generated text**\n\n部分不同意将此列为 [warning] 级别问题。\n\n首先事实确认：LaTeX 中 `---` 产生 em-dash，论文中确实有多处使用（如 Abstract 第 8 行 \"three distinct sparsity regimes---budget-surplus, budget-constrained, and capacity-limited---\"；Introduction 中也有类似用法）。\n\n但作为审稿意见，这属于 stylistic preference 而非学术质量问题。Em-dash 在英文学术写作中是合法标点（Chicago Manual of Style 认可），许多人类作者也使用。将 em-dash 等同于 \"AI-generated\" 是一种 heuristic，不是 evidence。这个问题最多属于 [info] 级别的 minor suggestion，不应影响接收决定。\n\n如果真要修，建议作者减少使用频率即可（改为逗号或拆分句子），但这不应是审稿意见中的 warning。\n\n---\n\n**[AGREE] R2-W6: \"Lagrangian\" formulation is misleading terminology**\n\n完全同意，这与我 Round 2 review 中的 W1 是同一问题。Eq. 9 是二次惩罚 + deadzone，Eq. 10 是几何倍增/减半——这不是 Lagrangian dual ascent。\"Adaptive penalty controller\" 更准确。两位 reviewer 独立指出同一问题，增强了这个 concern 的权重。\n\n---\n\n**[AGREE] R2-W7: Reference count is low**\n\n同意。我在自己的 review 中也指出缺少 Wanda、SparseGPT、MoE、Louizos et al. 2018 (L0/Concrete distribution) 等引用。22 refs 对 EMNLP main 偏少，30-40 是更合理的密度。尤其是 pruning 领域的经典工作（Wanda, SparseGPT）和 conditional computation（MoE）应该在 Related Work 中有所 acknowledge。\n\n---\n\n### 总结\n\n与 Reviewer 2 的主要分歧点：\n1. **W1 (novelty)**: 我认为论文的 gradient mismatch 诊断 + iso-compute verification + regime analysis 超越了简单 component combination，但同意 2D taxonomy framing 有填空嫌疑。Overall novelty borderline。\n2. **W5 (em-dash)**: 不应作为 warning 级别问题。\n\n与 Reviewer 2 的一致点：\n- W2 (relative advantage inflation)、W3 (scale)、W4 (downstream collapse)、W6 (Lagrangian 术语)、W7 (reference count) 均为有效批评。\n\n我的 overall 评价维持 3.5 (Borderline Conference)，略高于 R2 的 3.0 (Findings)。分歧在于对 novelty 和 analytical contribution 的权重：如果重视方法论洞察（gradient coupling mechanism + regime analysis），主会可接受；如果要求 novel algorithm 或 scaling evidence，Findings 更合适。",
  "reviewer_id": "1",
  "project": "distill_sparse_swiglu"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4bb80bb3-f531-43ee-9999-047be119302b",
  "isSidechain": false,
  "requestId": "req_011Cb7YMAThPCY6fpgaNCcGT",
  "type": "assistant",
  "uuid": "f9d85923-3736-4533-bd1e-aa175b0b59ba",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/review_reviewer_1_772f066c",
  "sessionId": "e4589542-c5a3-4a5b-a779-c62f37dfeb92",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JnfGtwrMA3U5L1x4uhkH7f",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 53075,
      "cache_read_input_tokens": 11841,
      "output_tokens": 2898,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 53075,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 2898,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 53075,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 53075
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "system_changed",
        "cache_missed_input_tokens": 35353
      }
    }
  }
}
```

</details>

---

### Tool result

_source line 66 · 2026-05-17T04:53:25.001Z_

<details><summary>↩ Tool result · `toolu_01MX3CWn9YhSf5fhk2qmiBUK`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director\"}, \"error\": \"\"}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f9d85923-3736-4533-bd1e-aa175b0b59ba",
  "isSidechain": false,
  "promptId": "fa245021-979b-4942-9f52-416e04a360db",
  "type": "user",
  "uuid": "d35155ed-2a2c-4218-b604-50a18c5cbbd9",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"review_director_key\\\": \\\"feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director\\\"}, \\\"error\\\": \\\"\\\"}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director\"}, \"error\": \"\"}"
    }
  },
  "sourceToolAssistantUUID": "f9d85923-3736-4533-bd1e-aa175b0b59ba",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/review_reviewer_1_772f066c",
  "sessionId": "e4589542-c5a3-4a5b-a779-c62f37dfeb92",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---
