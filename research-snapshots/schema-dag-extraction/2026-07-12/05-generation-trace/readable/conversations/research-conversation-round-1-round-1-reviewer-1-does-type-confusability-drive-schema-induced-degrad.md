# Research conversation: [Round 1 审稿请求]: ## Round 1 审稿任务 — Reviewer 1（方法严谨性） **论文：** "Does Type Confusability Drive Schema-Induced Degradation in

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction? (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 49
- **Recorded user turns:** 1
- **Tool calls:** 13
- **Original source:** `logs/chats/exported-trajectories/account-1/fac75791-ec7a-467d-a47d-5c20edb94374.jsonl`
- **Structured JSON:** [`f89904e99fea7c5d147c.json`](../../sessions/f8/f89904e99fea7c5d147c.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-16T00:53:36.369Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-16T00:53:36.369Z",
  "sessionId": "fac75791-ec7a-467d-a47d-5c20edb94374",
  "content": "[Round 1 审稿请求]:\n## Round 1 审稿任务 — Reviewer 1（方法严谨性）\n\n**论文：** \"Does Type Confusability Drive Schema-Induced Degradation in Training-Free LLM Information Extraction?\"\n**Venue：** EMNLP 2026 Main Conference（ARR May 25 cycle）\n**格式要求：** 长文 8 页 + 无限参考文献，ACL 模板，double-blind，mandatory Limitations section，Responsible NLP Research Checklist\n**论文路径：** `projects/schema-dag-extraction/docs/paper/main.tex`（各章节在同目录下：abstract.tex, introduction.tex, related_work.tex, experimental_setup.tex, results.tex, sdgd_negative.tex, discussion.tex；Limitations 在 main.tex 内）\n\n### 你的审查侧重\n\n**1. 实验设计与统计方法**\n- 两个实验范式（count curves + BCS-controlled）的设计是否合理？是否真正隔离了 count 和 confusability？\n- BCS-controlled 实验中 low-BCS vs high-BCS batch 的构造是否有偏？样本量（5 batches/count level, 27 total）是否足够？\n- Bootstrap CI 的使用是否恰当？是否有应报而未报的统计检验？\n- 16-rel 到 80-rel 的 3.4× amplification 是两点比较，统计可靠性如何？\n- Pairwise correlation r=0.112 (r²=1.3%) 的效应量是否被过度解读？\n\n**2. 评估指标**\n- 三个任务使用不同评估指标（text-match F1, accuracy, relaxed F1）是否合理？跨任务可比性如何？\n- NER 的 text-match 而非 exact span match 评估是否引入偏差？\n- MAVEN relaxed F1 的定义是否足够严格？\n\n**3. 可复现性**\n- 实验细节是否充分？（模型配置、prompt 模板、decoding 参数、随机种子）\n- v1/v2 prompt 切换的处理是否透明？\n- Cross-model validation (Llama-3.1-8B) 的覆盖范围是否充分？\n\n**4. SDGD 负面结果**\n- Merge amplification 的分析是否充分？是否遗漏了可能的 merge 策略？\n- 负面结果的呈现是否公平客观？\n\n请按以下格式输出审稿报告：\n- Summary (2-3 句)\n- Strengths (逐条)\n- Weaknesses (逐条，标注 [Must-Fix] 或 [Should-Fix] 或 [Minor])\n- Questions (需要作者澄清的)\n- Overall Assessment (strong reject / weak reject / borderline / weak accept / strong accept + 简要理由)"
}
```

---

### Runtime record

_source line 2 · 2026-05-16T00:53:36.372Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-16T00:53:36.372Z",
  "sessionId": "fac75791-ec7a-467d-a47d-5c20edb94374"
}
```

---

## Round 1

47 recorded events

### User

_source line 3 · 2026-05-16T00:53:36.406Z_

[Round 1 审稿请求]:
## Round 1 审稿任务 — Reviewer 1（方法严谨性）

**论文：** "Does Type Confusability Drive Schema-Induced Degradation in Training-Free LLM Information Extraction?"
**Venue：** EMNLP 2026 Main Conference（ARR May 25 cycle）
**格式要求：** 长文 8 页 + 无限参考文献，ACL 模板，double-blind，mandatory Limitations section，Responsible NLP Research Checklist
**论文路径：** `projects/schema-dag-extraction/docs/paper/main.tex`（各章节在同目录下：abstract.tex, introduction.tex, related_work.tex, experimental_setup.tex, results.tex, sdgd_negative.tex, discussion.tex；Limitations 在 main.tex 内）

### 你的审查侧重

**1. 实验设计与统计方法**
- 两个实验范式（count curves + BCS-controlled）的设计是否合理？是否真正隔离了 count 和 confusability？
- BCS-controlled 实验中 low-BCS vs high-BCS batch 的构造是否有偏？样本量（5 batches/count level, 27 total）是否足够？
- Bootstrap CI 的使用是否恰当？是否有应报而未报的统计检验？
- 16-rel 到 80-rel 的 3.4× amplification 是两点比较，统计可靠性如何？
- Pairwise correlation r=0.112 (r²=1.3%) 的效应量是否被过度解读？

**2. 评估指标**
- 三个任务使用不同评估指标（text-match F1, accuracy, relaxed F1）是否合理？跨任务可比性如何？
- NER 的 text-match 而非 exact span match 评估是否引入偏差？
- MAVEN relaxed F1 的定义是否足够严格？

**3. 可复现性**
- 实验细节是否充分？（模型配置、prompt 模板、decoding 参数、随机种子）
- v1/v2 prompt 切换的处理是否透明？
- Cross-model validation (Llama-3.1-8B) 的覆盖范围是否充分？

**4. SDGD 负面结果**
- Merge amplification 的分析是否充分？是否遗漏了可能的 merge 策略？
- 负面结果的呈现是否公平客观？

请按以下格式输出审稿报告：
- Summary (2-3 句)
- Strengths (逐条)
- Weaknesses (逐条，标注 [Must-Fix] 或 [Should-Fix] 或 [Minor])
- Questions (需要作者澄清的)
- Overall Assessment (strong reject / weak reject / borderline / weak accept / strong accept + 简要理由)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "86262a68-8f08-4a31-bae8-2266d9a0e2fa",
  "type": "user",
  "uuid": "a413950c-c0eb-4aa1-91af-120e8aa65a36",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_reviewer_1_b5f154cf",
  "sessionId": "fac75791-ec7a-467d-a47d-5c20edb94374",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-16T00:53:36.405Z_

```json
{
  "parentUuid": "a413950c-c0eb-4aa1-91af-120e8aa65a36",
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
  "uuid": "4063faf8-1ba6-48ad-bda5-6488f63c4bd5",
  "timestamp": "2026-05-16T00:53:36.405Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_reviewer_1_b5f154cf",
  "sessionId": "fac75791-ec7a-467d-a47d-5c20edb94374",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-16T00:53:36.405Z_

```json
{
  "parentUuid": "4063faf8-1ba6-48ad-bda5-6488f63c4bd5",
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
  "uuid": "4a8e3a52-29dc-48f8-9fd8-2becd6df94c3",
  "timestamp": "2026-05-16T00:53:36.405Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_reviewer_1_b5f154cf",
  "sessionId": "fac75791-ec7a-467d-a47d-5c20edb94374",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 6 · 2026-05-16T00:53:36.405Z_

```json
{
  "parentUuid": "4a8e3a52-29dc-48f8-9fd8-2becd6df94c3",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "1f61de95-7877-44fe-90d4-e8c7fb77bec8",
  "timestamp": "2026-05-16T00:53:36.405Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_reviewer_1_b5f154cf",
  "sessionId": "fac75791-ec7a-467d-a47d-5c20edb94374",
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
  "aiTitle": "Review methodological rigor of schema extraction paper",
  "sessionId": "fac75791-ec7a-467d-a47d-5c20edb94374"
}
```

---

### Assistant

_source line 8 · 2026-05-16T00:53:40.180Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to perform a Round 1 review of a paper as Reviewer 1, focusing on methodological rigor. Let me follow the instructions:

1. First, I need to do Step 0: search for EMNLP 2026 / ACL ARR reviewer guidelines
2. Then read the paper
3. Produce the review

Let me start by searching for reviewer guidelines and reading the paper in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1f61de95-7877-44fe-90d4-e8c7fb77bec8",
  "isSidechain": false,
  "requestId": "req_011Cb5LLsDi4j6NDTrGeZrw5",
  "type": "assistant",
  "uuid": "ef78be56-e364-4a8d-9a52-77f37dc3ed31",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_reviewer_1_b5f154cf",
  "sessionId": "fac75791-ec7a-467d-a47d-5c20edb94374",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NJBtNGS9YCq1CunNisV3pL",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13799,
      "cache_read_input_tokens": 11841,
      "output_tokens": 249,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 13799,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 249,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 13799,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 13799
          },
          "type": "message"
        }
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

_source line 9 · 2026-05-16T00:53:41.180Z_

开始审稿。先搜索 ACL ARR reviewer guidelines，同时读取论文各章节。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ef78be56-e364-4a8d-9a52-77f37dc3ed31",
  "isSidechain": false,
  "requestId": "req_011Cb5LLsDi4j6NDTrGeZrw5",
  "type": "assistant",
  "uuid": "7f53ec15-9567-4c79-a3e1-1b3330552906",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_reviewer_1_b5f154cf",
  "sessionId": "fac75791-ec7a-467d-a47d-5c20edb94374",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NJBtNGS9YCq1CunNisV3pL",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13799,
      "cache_read_input_tokens": 11841,
      "output_tokens": 249,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 13799,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 249,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 13799,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 13799
          },
          "type": "message"
        }
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

_source line 10 · 2026-05-16T00:53:42.809Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01Xyi85d5hBnPnEHUE4dedRo`</summary>

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
  "parentUuid": "7f53ec15-9567-4c79-a3e1-1b3330552906",
  "isSidechain": false,
  "requestId": "req_011Cb5LLsDi4j6NDTrGeZrw5",
  "type": "assistant",
  "uuid": "4c56c9c2-10bf-41b4-b111-72bbc5610e09",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_reviewer_1_b5f154cf",
  "sessionId": "fac75791-ec7a-467d-a47d-5c20edb94374",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NJBtNGS9YCq1CunNisV3pL",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13799,
      "cache_read_input_tokens": 11841,
      "output_tokens": 249,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 13799,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 249,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 13799,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 13799
          },
          "type": "message"
        }
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

_source line 11 · 2026-05-16T00:53:42.816Z_

<details><summary>↩ Tool result · `toolu_01Xyi85d5hBnPnEHUE4dedRo`</summary>

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
  "parentUuid": "4c56c9c2-10bf-41b4-b111-72bbc5610e09",
  "isSidechain": false,
  "promptId": "86262a68-8f08-4a31-bae8-2266d9a0e2fa",
  "type": "user",
  "uuid": "4c5e2708-392e-4a1c-8a74-b2824eb63b8c",
  "toolUseResult": {
    "matches": [
      "WebSearch",
      "mcp__agent-ml-research__pdf_to_images",
      "mcp__agent-ml-research__review_reviewer_post_to_director"
    ],
    "query": "select:WebSearch,mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__review_reviewer_post_to_director",
    "total_deferred_tools": 23
  },
  "sourceToolAssistantUUID": "4c56c9c2-10bf-41b4-b111-72bbc5610e09",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_reviewer_1_b5f154cf",
  "sessionId": "fac75791-ec7a-467d-a47d-5c20edb94374",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 12 · 2026-05-16T00:53:46.805Z_

<details><summary>Logged reasoning block</summary>

```text
Now let me search for ACL ARR reviewer guidelines and read the paper chapters in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4c5e2708-392e-4a1c-8a74-b2824eb63b8c",
  "isSidechain": false,
  "requestId": "req_011Cb5LMLrd6z6Sy72CAtj3x",
  "type": "assistant",
  "uuid": "1f9a913f-fe42-469c-85b2-8acbef2a96ca",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_reviewer_1_b5f154cf",
  "sessionId": "fac75791-ec7a-467d-a47d-5c20edb94374",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RNMgfhee72UexycLMRrkex",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1412,
      "cache_read_input_tokens": 25640,
      "output_tokens": 313,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1412,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 313,
          "cache_read_input_tokens": 25640,
          "cache_creation_input_tokens": 1412,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1412
          },
          "type": "message"
        }
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

_source line 13 · 2026-05-16T00:53:47.358Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01PMDjdjuuqHD2sFwXywXTpR`</summary>

```json
{
  "query": "ACL ARR review form criteria 2025 2026 reviewer guidelines scoring"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1f9a913f-fe42-469c-85b2-8acbef2a96ca",
  "isSidechain": false,
  "requestId": "req_011Cb5LMLrd6z6Sy72CAtj3x",
  "type": "assistant",
  "uuid": "c5858fcb-fcf1-4b9f-bf2a-da6f4e19dd48",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_reviewer_1_b5f154cf",
  "sessionId": "fac75791-ec7a-467d-a47d-5c20edb94374",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RNMgfhee72UexycLMRrkex",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1412,
      "cache_read_input_tokens": 25640,
      "output_tokens": 313,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1412,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 313,
          "cache_read_input_tokens": 25640,
          "cache_creation_input_tokens": 1412,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1412
          },
          "type": "message"
        }
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

_source line 14 · 2026-05-16T00:53:49.240Z_

<details open><summary>🔧 Tool call — Read · `toolu_012wSRDb8fZjjgRoiEUX5ifN`</summary>

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
  "parentUuid": "c5858fcb-fcf1-4b9f-bf2a-da6f4e19dd48",
  "isSidechain": false,
  "requestId": "req_011Cb5LMLrd6z6Sy72CAtj3x",
  "type": "assistant",
  "uuid": "246d777d-4e3d-44e1-83ec-3192f1002eb4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_reviewer_1_b5f154cf",
  "sessionId": "fac75791-ec7a-467d-a47d-5c20edb94374",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RNMgfhee72UexycLMRrkex",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1412,
      "cache_read_input_tokens": 25640,
      "output_tokens": 313,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1412,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 313,
          "cache_read_input_tokens": 25640,
          "cache_creation_input_tokens": 1412,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1412
          },
          "type": "message"
        }
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

_source line 15 · 2026-05-16T00:53:50.470Z_

<details><summary>↩ Tool result · `toolu_01Kahi7vorxAXJKrdjnoA5Pt`</summary>

```text
1	\section{Introduction}
2	\label{sec:introduction}
3	
4	Training-free LLM information extraction---prompting a large language model with a target schema and asking it to extract structured information without any task-specific fine-tuning---enables rapid deployment across new domains and ontologies. This zero-shot paradigm eliminates the need for labeled data, making it attractive for applications where annotation is expensive or schemas evolve frequently \cite{llm4ie-survey-2024}. Yet the paradigm carries a critical limitation: performance degrades sharply as the number of candidate types in the prompt schema grows. On named entity recognition, recall drops from 0.72 with a single candidate type to 0.42 with 64 types, a 42\% relative decline. On relation extraction, accuracy falls from 85.7\% with one relation to 50.4\% with 80 relations---near halving. This degradation is not academic: real-world ontologies routinely define 50--200+ types, placing them squarely in the regime where training-free extraction becomes unreliable.
5	
6	What causes this schema-induced degradation? Prior work has proposed decomposition strategies that implicitly assume different answers. \citet{uniner-2024} extract each type independently, assuming types can be treated as separable. \citet{llm-pee-2025} partition large event schemas by type embedding similarity before extraction, assuming that semantic overlap between co-presented types drives errors. \citet{parse-2025} rewrite and optimize schema definitions, assuming that description quality is the bottleneck. Each approach improves extraction under certain conditions, but none isolates \emph{why} schemas degrade performance in the first place. The closest work, LLM-PEE \cite{llm-pee-2025}, reduces both the number of co-presented types and their inter-type similarity simultaneously, making it impossible to determine which factor---or what combination---accounts for the observed gains. More broadly, all prior approaches conflate two distinct mechanisms that could independently degrade extraction: having more types to discriminate among (count) and having semantically similar types to confuse (confusability). Without disentangling these factors, decomposition strategies cannot be principled: they optimize a black-box objective without understanding its components.
7	
8	We ask three questions. \textbf{RQ1}: Does type confusability independently predict extraction degradation beyond the effect of type count? \textbf{RQ2}: Through what mechanisms do count and confusability each degrade performance? \textbf{RQ3}: Can confusability-aware schema decomposition improve extraction quality?
9	
10	To answer these questions, we conduct the first controlled empirical study that isolates type confusability from type count across three IE tasks: named entity recognition (NER), relation extraction (RE), and event detection (ED). We introduce the \emph{Schema Confusability Score} (SCS), which quantifies pairwise semantic overlap between types using embedding cosine similarity, and its batch-level aggregation, the \emph{Batch Confusability Score} (BCS). We design two complementary experimental paradigms: \emph{count curves} that vary schema size while randomizing confusability, and \emph{BCS-controlled experiments} that fix schema size while varying confusability. We evaluate on three datasets spanning diverse schema structures: Few-NERD \cite{fewnerd-2021} (66 entity types across 8 domains), FewRel \cite{fewrel-2018} (80 relation types), and MAVEN \cite{maven-2020} (168 event types from a single ontology). All experiments use Qwen3-32B in a zero-shot prompting setup with bootstrap confidence intervals.
11	
12	Our experiments yield five findings: (1)~schema-induced degradation operates through two channels---count-driven recall decline (up to $-$30\,pp) and confusability-driven type confusion---that are separable in RE but interact in NER; (2)~pairwise SCS predicts type confusion across tasks ($r = 0.112$--$0.129$), modest in magnitude but the first factor empirically isolated in controlled zero-shot IE; (3)~confusability effects amplify $3.4\times$ as schema size grows from 16 to 80 types; (4)~per-type confusability aggregation is confounded by centrality on homogeneous schemas; and (5)~confusability-aware decomposition fails due to merge amplification (best F1 = 0.32 vs.\ single-pass 0.45), a structural bottleneck for decompose-then-merge pipelines.
13	
14	Our contributions are:
15	\begin{enumerate}[leftmargin=*,itemsep=2pt,topsep=2pt]
16	    \item \textbf{Multi-channel degradation model.} We provide the first empirical decomposition of schema-induced degradation into count and confusability channels across NER, RE, and ED, revealing task-dependent interactions between channels.
17	    \item \textbf{Pairwise confusability as a robust predictor.} We demonstrate that pairwise SCS predicts type confusion across tasks and embedding models, while identifying a centrality confound that invalidates per-type aggregation on homogeneous schemas.
18	    \item \textbf{Cross-task controlled experiments.} We present BCS-controlled experiments with bootstrap confidence intervals on three datasets, establishing that confusability effects amplify $3.4\times$ as schema size grows from 16 to 80 types.
19	    \item \textbf{Informative negative result.} Our SDGD experiments identify merge amplification as a structural bottleneck for decompose-then-merge approaches, with direct implications for the design of schema decomposition methods.
20	\end{enumerate}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "dba2e334-42e2-4886-b073-2859336f7436",
  "isSidechain": false,
  "promptId": "86262a68-8f08-4a31-bae8-2266d9a0e2fa",
  "type": "user",
  "uuid": "8e25396c-85e9-412f-8333-feffc9b95c88",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/introduction.tex",
      "content": "\\section{Introduction}\n\\label{sec:introduction}\n\nTraining-free LLM information extraction---prompting a large language model with a target schema and asking it to extract structured information without any task-specific fine-tuning---enables rapid deployment across new domains and ontologies. This zero-shot paradigm eliminates the need for labeled data, making it attractive for applications where annotation is expensive or schemas evolve frequently \\cite{llm4ie-survey-2024}. Yet the paradigm carries a critical limitation: performance degrades sharply as the number of candidate types in the prompt schema grows. On named entity recognition, recall drops from 0.72 with a single candidate type to 0.42 with 64 types, a 42\\% relative decline. On relation extraction, accuracy falls from 85.7\\% with one relation to 50.4\\% with 80 relations---near halving. This degradation is not academic: real-world ontologies routinely define 50--200+ types, placing them squarely in the regime where training-free extraction becomes unreliable.\n\nWhat causes this schema-induced degradation? Prior work has proposed decomposition strategies that implicitly assume different answers. \\citet{uniner-2024} extract each type independently, assuming types can be treated as separable. \\citet{llm-pee-2025} partition large event schemas by type embedding similarity before extraction, assuming that semantic overlap between co-presented types drives errors. \\citet{parse-2025} rewrite and optimize schema definitions, assuming that description quality is the bottleneck. Each approach improves extraction under certain conditions, but none isolates \\emph{why} schemas degrade performance in the first place. The closest work, LLM-PEE \\cite{llm-pee-2025}, reduces both the number of co-presented types and their inter-type similarity simultaneously, making it impossible to determine which factor---or what combination---accounts for the observed gains. More broadly, all prior approaches conflate two distinct mechanisms that could independently degrade extraction: having more types to discriminate among (count) and having semantically similar types to confuse (confusability). Without disentangling these factors, decomposition strategies cannot be principled: they optimize a black-box objective without understanding its components.\n\nWe ask three questions. \\textbf{RQ1}: Does type confusability independently predict extraction degradation beyond the effect of type count? \\textbf{RQ2}: Through what mechanisms do count and confusability each degrade performance? \\textbf{RQ3}: Can confusability-aware schema decomposition improve extraction quality?\n\nTo answer these questions, we conduct the first controlled empirical study that isolates type confusability from type count across three IE tasks: named entity recognition (NER), relation extraction (RE), and event detection (ED). We introduce the \\emph{Schema Confusability Score} (SCS), which quantifies pairwise semantic overlap between types using embedding cosine similarity, and its batch-level aggregation, the \\emph{Batch Confusability Score} (BCS). We design two complementary experimental paradigms: \\emph{count curves} that vary schema size while randomizing confusability, and \\emph{BCS-controlled experiments} that fix schema size while varying confusability. We evaluate on three datasets spanning diverse schema structures: Few-NERD \\cite{fewnerd-2021} (66 entity types across 8 domains), FewRel \\cite{fewrel-2018} (80 relation types), and MAVEN \\cite{maven-2020} (168 event types from a single ontology). All experiments use Qwen3-32B in a zero-shot prompting setup with bootstrap confidence intervals.\n\nOur experiments yield five findings: (1)~schema-induced degradation operates through two channels---count-driven recall decline (up to $-$30\\,pp) and confusability-driven type confusion---that are separable in RE but interact in NER; (2)~pairwise SCS predicts type confusion across tasks ($r = 0.112$--$0.129$), modest in magnitude but the first factor empirically isolated in controlled zero-shot IE; (3)~confusability effects amplify $3.4\\times$ as schema size grows from 16 to 80 types; (4)~per-type confusability aggregation is confounded by centrality on homogeneous schemas; and (5)~confusability-aware decomposition fails due to merge amplification (best F1 = 0.32 vs.\\ single-pass 0.45), a structural bottleneck for decompose-then-merge pipelines.\n\nOur contributions are:\n\\begin{enumerate}[leftmargin=*,itemsep=2pt,topsep=2pt]\n    \\item \\textbf{Multi-channel degradation model.} We provide the first empirical decomposition of schema-induced degradation into count and confusability channels across NER, RE, and ED, revealing task-dependent interactions between channels.\n    \\item \\textbf{Pairwise confusability as a robust predictor.} We demonstrate that pairwise SCS predicts type confusion across tasks and embedding models, while identifying a centrality confound that invalidates per-type aggregation on homogeneous schemas.\n    \\item \\textbf{Cross-task controlled experiments.} We present BCS-controlled experiments with bootstrap confidence intervals on three datasets, establishing that confusability effects amplify $3.4\\times$ as schema size grows from 16 to 80 types.\n    \\item \\textbf{Informative negative result.} Our SDGD experiments identify merge amplification as a structural bottleneck for decompose-then-merge approaches, with direct implications for the design of schema decomposition methods.\n\\end{enumerate}",
      "numLines": 20,
      "startLine": 1,
      "totalLines": 20
    }
  },
  "sourceToolAssistantUUID": "dba2e334-42e2-4886-b073-2859336f7436",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_reviewer_1_b5f154cf",
  "sessionId": "fac75791-ec7a-467d-a47d-5c20edb94374",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-16T00:53:49.250Z_

<details><summary>↩ Tool result · `toolu_012wSRDb8fZjjgRoiEUX5ifN`</summary>

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
14	
15	\title{Does Type Confusability Drive Schema-Induced Degradation\\in Training-Free LLM Information Extraction?}
16	
17	\author{Anonymous}
18	
19	\begin{document}
20	\maketitle
21	
22	\input{abstract}
23	
24	\input{introduction}
25	
26	\input{related_work}
27	
28	\input{experimental_setup}
29	
30	\input{results}
31	
32	\input{sdgd_negative}
33	
34	\input{discussion}
35	
36	\section*{Limitations}
37	The primary experiments use Qwen3-32B. Channel~1 (count effect) has been validated on Meta-Llama-3.1-8B-Instruct (recall decline $-$43\,pp, per-batch $r = 0.725$ with Qwen3-32B). Channel~2 was validated cross-model on FewRel RE: Llama-3.1-8B-Instruct shows $\Delta = -27.1$\,pp at count 8 and $-23.9$\,pp at count 16, comparable to Qwen3-32B's $-31.2$\,pp. High-BCS accuracy is model-invariant ($\approx$0.51), with cross-model divergence confined to the low-BCS regime. On Few-NERD NER, the effect was not robustly detectable, likely due to floor effects at 8B scale and the noisier text-match metric. The pairwise confusability signal explains roughly 1.3--1.7\% of the variance in type confusion---entity frequency, prompt position effects, and type definition quality likely contribute to the remaining variance. Our decomposition experiments test only union-based merge strategies; calibration-aware or joint-decoding alternatives remain unexplored. We conducted a within-dataset $2\!\times\!2$ factorial analysis (count $\times$ BCS) on Few-NERD; the interaction term was directionally consistent but not statistically significant ($z = -0.67$, $p = 0.50$), possibly due to BCS range compression in high-count schemas. The primary evidence for count--confusability interaction remains the $3.4\times$ amplification observed across FewRel schema scales (\S\ref{sec:bcs_controlled}). An intermediate evaluation at 40-relation subsets sampled from the 80-relation pool (accuracy 0.588, BCS $\Delta = -33.3$\,pp at count 8) confirms monotonic decline, but this is not an independent schema---all 40-relation subsets draw from the same 80-type pool, so the 16-to-80 amplification ($3.4\times$) remains a two-point comparison. The $3.4\times$ amplification is a point estimate; propagating the 80-rel CI ([17.7, 42.7]\,pp) against the 9.1\,pp baseline yields a range of $1.9\text{--}4.7\times$. SCS/BCS relies on embedding cosine similarity; alternative metrics such as label entropy or ontological depth may capture complementary dimensions of schema difficulty.
38	
39	\bibliography{references}
40	
41	\appendix
42	
43	\section{Additional Figures}
44	\label{sec:appendix_figures}
45	
46	\begin{table}[h]
47	\centering
48	\small
49	\begin{tabular}{lrr}
50	\toprule
51	\textbf{Count} & \textbf{Llama-3.1-8B} & \textbf{Qwen3-32B} \\
52	\midrule
53	1 & 0.702 & 0.640 \\
54	64 & 0.273 & 0.304 \\
55	\midrule
56	Decline & $-$43\,pp & $-$34\,pp \\
57	\bottomrule
58	\end{tabular}
59	\caption{Cross-model count-curve replication on Few-NERD (text-match recall). Both models show a general declining trend in recall with schema size. Per-batch correlation $r = 0.725$. Qwen3-32B values use the v2 prompt (\S\ref{sec:model}) for fair cross-model comparison; the count-curve results in \S\ref{sec:count_curves} use the v1 prompt, yielding higher absolute recall (0.72 vs.\ 0.64 at count${}\,=\,1$) due to over-prediction under v1.}
60	\label{tab:cross_model}
61	\end{table}
62	
63	\begin{table}[h]
64	\centering
65	\small
66	\resizebox{\columnwidth}{!}{%
67	\begin{tabular}{crrrrrr}
68	\toprule
69	& \multicolumn{3}{c}{\textbf{Llama-3.1-8B}} & \multicolumn{3}{c}{\textbf{Qwen3-32B}} \\
70	\cmidrule(lr){2-4} \cmidrule(lr){5-7}
71	\textbf{Count} & \textbf{Low} & \textbf{High} & \textbf{$\Delta$} & \textbf{Low} & \textbf{High} & \textbf{$\Delta$} \\
72	\midrule
73	8 & 78.1\% & 51.0\% & $-$27.1 & 82.3\% & 51.0\% & $-$31.2 \\
74	16 & 75.5\% & 51.6\% & $-$23.9 & 82.8\% & 51.6\% & $-$31.2 \\
75	\bottomrule
76	\end{tabular}}
77	\caption{Cross-model BCS-controlled FewRel accuracy.  High-BCS accuracy converges to $\approx$51\% regardless of model, while low-BCS accuracy reflects model capacity differences.  The confusability gap ($\Delta$, in pp) is 77--87\% as large on Llama-3.1-8B as on Qwen3-32B.}
78	\label{tab:cross_model_bcs}
79	\end{table}
80	
81	\begin{figure}[h]
82	\centering
83	\includegraphics[width=\columnwidth]{../../figures/paper/fig_count_curves.pdf}
84	\caption{Count-degradation curves across three IE tasks. NER recall generally declines and RE accuracy declines monotonically with schema size; MAVEN relaxed F1 increases, reflecting same-domain disambiguation benefits (\S\ref{sec:centrality_confound}).}
85	\label{fig:count_curves}
86	\end{figure}
87	
88	\begin{figure}[h]
89	\centering
90	\includegraphics[width=\columnwidth]{../../figures/paper/fig_bcs_scaling.pdf}
91	\caption{BCS-controlled FewRel accuracy. The confusability gap between low-BCS and high-BCS batches widens from 9.1\,pp at 16 relations to 31.2\,pp at 80 relations ($3.4\times$ amplification).}
92	\label{fig:bcs_scaling}
93	\end{figure}
94	
95	\begin{figure}[h]
96	\centering
97	\includegraphics[width=\columnwidth]{../../figures/paper/fig_error_taxonomy.pdf}
98	\caption{Error taxonomy decomposition. IntraSub (intra-batch substitution) scales monotonically with BCS in both tasks. RE missed rates remain flat (10--16\%), but NER missed rates are substantially higher (43--65\%) and non-monotonic, revealing task-dependent error mechanisms.}
99	\label{fig:error_taxonomy}
100	\end{figure}
101	
102	\end{document}
103	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "246d777d-4e3d-44e1-83ec-3192f1002eb4",
  "isSidechain": false,
  "promptId": "86262a68-8f08-4a31-bae8-2266d9a0e2fa",
  "type": "user",
  "uuid": "7ce53ce3-6463-4e23-872a-e62d01c04e8c",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex",
      "content": "\\documentclass[11pt]{article}\n\n\\usepackage[review]{acl}\n\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage[T1]{fontenc}\n\\usepackage[utf8]{inputenc}\n\\usepackage{microtype}\n\\usepackage{graphicx}\n\\usepackage{booktabs}\n\\usepackage{amsmath}\n\\usepackage{enumitem}\n\n\\title{Does Type Confusability Drive Schema-Induced Degradation\\\\in Training-Free LLM Information Extraction?}\n\n\\author{Anonymous}\n\n\\begin{document}\n\\maketitle\n\n\\input{abstract}\n\n\\input{introduction}\n\n\\input{related_work}\n\n\\input{experimental_setup}\n\n\\input{results}\n\n\\input{sdgd_negative}\n\n\\input{discussion}\n\n\\section*{Limitations}\nThe primary experiments use Qwen3-32B. Channel~1 (count effect) has been validated on Meta-Llama-3.1-8B-Instruct (recall decline $-$43\\,pp, per-batch $r = 0.725$ with Qwen3-32B). Channel~2 was validated cross-model on FewRel RE: Llama-3.1-8B-Instruct shows $\\Delta = -27.1$\\,pp at count 8 and $-23.9$\\,pp at count 16, comparable to Qwen3-32B's $-31.2$\\,pp. High-BCS accuracy is model-invariant ($\\approx$0.51), with cross-model divergence confined to the low-BCS regime. On Few-NERD NER, the effect was not robustly detectable, likely due to floor effects at 8B scale and the noisier text-match metric. The pairwise confusability signal explains roughly 1.3--1.7\\% of the variance in type confusion---entity frequency, prompt position effects, and type definition quality likely contribute to the remaining variance. Our decomposition experiments test only union-based merge strategies; calibration-aware or joint-decoding alternatives remain unexplored. We conducted a within-dataset $2\\!\\times\\!2$ factorial analysis (count $\\times$ BCS) on Few-NERD; the interaction term was directionally consistent but not statistically significant ($z = -0.67$, $p = 0.50$), possibly due to BCS range compression in high-count schemas. The primary evidence for count--confusability interaction remains the $3.4\\times$ amplification observed across FewRel schema scales (\\S\\ref{sec:bcs_controlled}). An intermediate evaluation at 40-relation subsets sampled from the 80-relation pool (accuracy 0.588, BCS $\\Delta = -33.3$\\,pp at count 8) confirms monotonic decline, but this is not an independent schema---all 40-relation subsets draw from the same 80-type pool, so the 16-to-80 amplification ($3.4\\times$) remains a two-point comparison. The $3.4\\times$ amplification is a point estimate; propagating the 80-rel CI ([17.7, 42.7]\\,pp) against the 9.1\\,pp baseline yields a range of $1.9\\text{--}4.7\\times$. SCS/BCS relies on embedding cosine similarity; alternative metrics such as label entropy or ontological depth may capture complementary dimensions of schema difficulty.\n\n\\bibliography{references}\n\n\\appendix\n\n\\section{Additional Figures}\n\\label{sec:appendix_figures}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{lrr}\n\\toprule\n\\textbf{Count} & \\textbf{Llama-3.1-8B} & \\textbf{Qwen3-32B} \\\\\n\\midrule\n1 & 0.702 & 0.640 \\\\\n64 & 0.273 & 0.304 \\\\\n\\midrule\nDecline & $-$43\\,pp & $-$34\\,pp \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Cross-model count-curve replication on Few-NERD (text-match recall). Both models show a general declining trend in recall with schema size. Per-batch correlation $r = 0.725$. Qwen3-32B values use the v2 prompt (\\S\\ref{sec:model}) for fair cross-model comparison; the count-curve results in \\S\\ref{sec:count_curves} use the v1 prompt, yielding higher absolute recall (0.72 vs.\\ 0.64 at count${}\\,=\\,1$) due to over-prediction under v1.}\n\\label{tab:cross_model}\n\\end{table}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{crrrrrr}\n\\toprule\n& \\multicolumn{3}{c}{\\textbf{Llama-3.1-8B}} & \\multicolumn{3}{c}{\\textbf{Qwen3-32B}} \\\\\n\\cmidrule(lr){2-4} \\cmidrule(lr){5-7}\n\\textbf{Count} & \\textbf{Low} & \\textbf{High} & \\textbf{$\\Delta$} & \\textbf{Low} & \\textbf{High} & \\textbf{$\\Delta$} \\\\\n\\midrule\n8 & 78.1\\% & 51.0\\% & $-$27.1 & 82.3\\% & 51.0\\% & $-$31.2 \\\\\n16 & 75.5\\% & 51.6\\% & $-$23.9 & 82.8\\% & 51.6\\% & $-$31.2 \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Cross-model BCS-controlled FewRel accuracy.  High-BCS accuracy converges to $\\approx$51\\% regardless of model, while low-BCS accuracy reflects model capacity differences.  The confusability gap ($\\Delta$, in pp) is 77--87\\% as large on Llama-3.1-8B as on Qwen3-32B.}\n\\label{tab:cross_model_bcs}\n\\end{table}\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=\\columnwidth]{../../figures/paper/fig_count_curves.pdf}\n\\caption{Count-degradation curves across three IE tasks. NER recall generally declines and RE accuracy declines monotonically with schema size; MAVEN relaxed F1 increases, reflecting same-domain disambiguation benefits (\\S\\ref{sec:centrality_confound}).}\n\\label{fig:count_curves}\n\\end{figure}\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=\\columnwidth]{../../figures/paper/fig_bcs_scaling.pdf}\n\\caption{BCS-controlled FewRel accuracy. The confusability gap between low-BCS and high-BCS batches widens from 9.1\\,pp at 16 relations to 31.2\\,pp at 80 relations ($3.4\\times$ amplification).}\n\\label{fig:bcs_scaling}\n\\end{figure}\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=\\columnwidth]{../../figures/paper/fig_error_taxonomy.pdf}\n\\caption{Error taxonomy decomposition. IntraSub (intra-batch substitution) scales monotonically with BCS in both tasks. RE missed rates remain flat (10--16\\%), but NER missed rates are substantially higher (43--65\\%) and non-monotonic, revealing task-dependent error mechanisms.}\n\\label{fig:error_taxonomy}\n\\end{figure}\n\n\\end{document}\n",
      "numLines": 103,
      "startLine": 1,
      "totalLines": 103
    }
  },
  "sourceToolAssistantUUID": "246d777d-4e3d-44e1-83ec-3192f1002eb4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_reviewer_1_b5f154cf",
  "sessionId": "fac75791-ec7a-467d-a47d-5c20edb94374",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-16T00:53:50.365Z_

<details open><summary>🔧 Tool call — Read · `toolu_01BCBq8J4vfAcHQpB5ZgnszQ`</summary>

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
  "parentUuid": "7ce53ce3-6463-4e23-872a-e62d01c04e8c",
  "isSidechain": false,
  "requestId": "req_011Cb5LMLrd6z6Sy72CAtj3x",
  "type": "assistant",
  "uuid": "002c2db0-a4ed-487e-961a-0eb8c0b708b4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_reviewer_1_b5f154cf",
  "sessionId": "fac75791-ec7a-467d-a47d-5c20edb94374",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RNMgfhee72UexycLMRrkex",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1412,
      "cache_read_input_tokens": 25640,
      "output_tokens": 313,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1412,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 313,
          "cache_read_input_tokens": 25640,
          "cache_creation_input_tokens": 1412,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1412
          },
          "type": "message"
        }
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

_source line 18 · 2026-05-16T00:53:50.377Z_

<details><summary>↩ Tool result · `toolu_01BCBq8J4vfAcHQpB5ZgnszQ`</summary>

```text
1	\begin{abstract}
2	Training-free LLM information extraction---prompting models with target schemas without fine-tuning---degrades sharply as schema complexity grows: NER recall drops from 0.72 to 0.42 with 64 candidate types, and RE accuracy falls from 85.7\% to 50.4\% with 80 relations. Prior work conflates type count with type confusability, leaving the mechanisms unclear. We conduct the first controlled empirical study isolating these factors across three IE tasks and three datasets, introducing the Schema Confusability Score (SCS) and two experimental paradigms: count curves that vary schema size while randomizing confusability, and BCS-controlled experiments that fix size while varying confusability. Our experiments reveal two degradation channels: a count channel that suppresses recall as candidate types increase, and a confusability channel where semantically similar types trigger intra-batch substitution errors---cleanly separable in RE but interacting in NER. Confusability effects amplify $3.4\times$ as schema size grows from 16 to 80 types, with accuracy gaps widening from 9.1 to 31.2 percentage points. Both channels replicate on Llama-3.1-8B (count $r = 0.725$; confusability $\Delta = -27$\,pp), with high-BCS accuracy converging to a model-invariant floor. Our confusability-aware decomposition yields an informative negative result: merge amplification destroys precision across all strategies, identifying a structural bottleneck for decompose-then-merge pipelines in zero-shot IE.
3	\end{abstract}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "002c2db0-a4ed-487e-961a-0eb8c0b708b4",
  "isSidechain": false,
  "promptId": "86262a68-8f08-4a31-bae8-2266d9a0e2fa",
  "type": "user",
  "uuid": "232497e4-f7e3-4f26-9fcd-feff70eb7274",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/abstract.tex",
      "content": "\\begin{abstract}\nTraining-free LLM information extraction---prompting models with target schemas without fine-tuning---degrades sharply as schema complexity grows: NER recall drops from 0.72 to 0.42 with 64 candidate types, and RE accuracy falls from 85.7\\% to 50.4\\% with 80 relations. Prior work conflates type count with type confusability, leaving the mechanisms unclear. We conduct the first controlled empirical study isolating these factors across three IE tasks and three datasets, introducing the Schema Confusability Score (SCS) and two experimental paradigms: count curves that vary schema size while randomizing confusability, and BCS-controlled experiments that fix size while varying confusability. Our experiments reveal two degradation channels: a count channel that suppresses recall as candidate types increase, and a confusability channel where semantically similar types trigger intra-batch substitution errors---cleanly separable in RE but interacting in NER. Confusability effects amplify $3.4\\times$ as schema size grows from 16 to 80 types, with accuracy gaps widening from 9.1 to 31.2 percentage points. Both channels replicate on Llama-3.1-8B (count $r = 0.725$; confusability $\\Delta = -27$\\,pp), with high-BCS accuracy converging to a model-invariant floor. Our confusability-aware decomposition yields an informative negative result: merge amplification destroys precision across all strategies, identifying a structural bottleneck for decompose-then-merge pipelines in zero-shot IE.\n\\end{abstract}",
      "numLines": 3,
      "startLine": 1,
      "totalLines": 3
    }
  },
  "sourceToolAssistantUUID": "002c2db0-a4ed-487e-961a-0eb8c0b708b4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_reviewer_1_b5f154cf",
  "sessionId": "fac75791-ec7a-467d-a47d-5c20edb94374",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-16T00:53:50.441Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Kahi7vorxAXJKrdjnoA5Pt`</summary>

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
  "parentUuid": "232497e4-f7e3-4f26-9fcd-feff70eb7274",
  "isSidechain": false,
  "requestId": "req_011Cb5LMLrd6z6Sy72CAtj3x",
  "type": "assistant",
  "uuid": "dba2e334-42e2-4886-b073-2859336f7436",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_reviewer_1_b5f154cf",
  "sessionId": "fac75791-ec7a-467d-a47d-5c20edb94374",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RNMgfhee72UexycLMRrkex",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1412,
      "cache_read_input_tokens": 25640,
      "output_tokens": 313,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1412,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 313,
          "cache_read_input_tokens": 25640,
          "cache_creation_input_tokens": 1412,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1412
          },
          "type": "message"
        }
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

_source line 20_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[Round 1 审稿请求]: ## Round 1 审稿任务 — Reviewer 1（方法严谨性）  **论文：** \"Does Type Confusability Drive Schema-Induced Degradation in Training-Free LLM Information Extraction?\" **Venue：** EMNLP 2026 Main Conferen…",
  "leafUuid": "8e25396c-85e9-412f-8333-feffc9b95c88",
  "sessionId": "fac75791-ec7a-467d-a47d-5c20edb94374"
}
```

---

### Runtime record

_source line 21_

```json
{
  "type": "ai-title",
  "aiTitle": "Review methodological rigor of schema extraction paper",
  "sessionId": "fac75791-ec7a-467d-a47d-5c20edb94374"
}
```

---

### Tool result

_source line 22 · 2026-05-16T00:53:54.655Z_

<details><summary>↩ Tool result · `toolu_01PMDjdjuuqHD2sFwXywXTpR`</summary>

```text
Web search results for query: "ACL ARR review form criteria 2025 2026 reviewer guidelines scoring"

Links: [{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"aclrollingreview/reviewerguidelines.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/reviewerguidelines.md"},{"title":"ACLRollingReview (@ReviewAcl) / X","url":"https://x.com/reviewacl"}]

Based on the search results, here's the key information about ACL ARR review form criteria, reviewer guidelines, and scoring for 2025-2026:

## Reviewer Scoring System

Starting with February 2025, ARR reviewers are asked to provide three scores: soundness, excitement, and overall recommendation. The soundness scores must be justified by the text of the review.

## Overall Recommendation Scale

The review form uses the following overall recommendation scale:

- 5 = Consider for Award: I think this paper could be considered for an outstanding paper award at an *ACL conference (up to top 2.5% papers). Outstanding papers should be either fascinating, controversial, surprising, impressive, or potentially field-changing.
- 2 = Resubmit next cycle: I think this paper needs substantial revisions that can be completed by the next ARR cycle.
- 1.5 = Resubmit after next cycle: I think this paper needs substantial revisions that cannot be completed by the next ARR cycle.
- 1 = Do not resubmit: This paper has to be fully redone, or it is not relevant to the *ACL community (e.g. it is in no way related to computational processing of language).

## Additional Review Criteria

Reviewers are also expected to address several other aspects, including whether the authors have adequately discussed the limitations and potential positive and negative societal impacts of their work, with constructive suggestions for improvement if not.

The official reviewer guidelines are available at aclrollingreview.org/reviewerguidelines for the most comprehensive and up-to-date information.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c5858fcb-fcf1-4b9f-bf2a-da6f4e19dd48",
  "isSidechain": false,
  "promptId": "86262a68-8f08-4a31-bae8-2266d9a0e2fa",
  "type": "user",
  "uuid": "a141d301-f1e9-4850-9a23-5c12e5aa3670",
  "toolUseResult": {
    "query": "ACL ARR review form criteria 2025 2026 reviewer guidelines scoring",
    "results": [
      {
        "tool_use_id": "srvtoolu_01PUsJnAwcX4t4H9TMnTJSCu",
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
            "title": "aclrollingreview/reviewerguidelines.md at main · acl-org/aclrollingreview",
            "url": "https://github.com/acl-org/aclrollingreview/blob/main/reviewerguidelines.md"
          },
          {
            "title": "ACLRollingReview (@ReviewAcl) / X",
            "url": "https://x.com/reviewacl"
          }
        ]
      },
      "Based on the search results, here's the key information about ACL ARR review form criteria, reviewer guidelines, and scoring for 2025-2026:\n\n## Reviewer Scoring System\n\nStarting with February 2025, ARR reviewers are asked to provide three scores: soundness, excitement, and overall recommendation. The soundness scores must be justified by the text of the review.\n\n## Overall Recommendation Scale\n\nThe review form uses the following overall recommendation scale:\n\n- 5 = Consider for Award: I think this paper could be considered for an outstanding paper award at an *ACL conference (up to top 2.5% papers). Outstanding papers should be either fascinating, controversial, surprising, impressive, or potentially field-changing.\n- 2 = Resubmit next cycle: I think this paper needs substantial revisions that can be completed by the next ARR cycle.\n- 1.5 = Resubmit after next cycle: I think this paper needs substantial revisions that cannot be completed by the next ARR cycle.\n- 1 = Do not resubmit: This paper has to be fully redone, or it is not relevant to the *ACL community (e.g. it is in no way related to computational processing of language).\n\n## Additional Review Criteria\n\nReviewers are also expected to address several other aspects, including whether the authors have adequately discussed the limitations and potential positive and negative societal impacts of their work, with constructive suggestions for improvement if not.\n\nThe official reviewer guidelines are available at aclrollingreview.org/reviewerguidelines for the most comprehensive and up-to-date information."
    ],
    "durationSeconds": 7.2915403570000015
  },
  "sourceToolAssistantUUID": "c5858fcb-fcf1-4b9f-bf2a-da6f4e19dd48",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_reviewer_1_b5f154cf",
  "sessionId": "fac75791-ec7a-467d-a47d-5c20edb94374",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 23 · 2026-05-16T00:53:57.058Z_

<details><summary>Logged reasoning block</summary>

```text
Let me now read the remaining paper sections and fetch the ACL ARR review form details.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a141d301-f1e9-4850-9a23-5c12e5aa3670",
  "isSidechain": false,
  "requestId": "req_011Cb5LNDGVcfywho2MMd1a4",
  "type": "assistant",
  "uuid": "e795a853-0d75-4de0-acf6-14e9209f86e9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_reviewer_1_b5f154cf",
  "sessionId": "fac75791-ec7a-467d-a47d-5c20edb94374",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012QXDoWJwahjZmSyGmkDdco",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 4013,
      "cache_creation_input_tokens": 1195,
      "cache_read_input_tokens": 27052,
      "output_tokens": 490,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1195,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 4013,
          "output_tokens": 490,
          "cache_read_input_tokens": 27052,
          "cache_creation_input_tokens": 1195,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1195
          },
          "type": "message"
        }
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

_source line 24 · 2026-05-16T00:53:58.056Z_

继续读取剩余章节并获取 ARR review form 详情。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e795a853-0d75-4de0-acf6-14e9209f86e9",
  "isSidechain": false,
  "requestId": "req_011Cb5LNDGVcfywho2MMd1a4",
  "type": "assistant",
  "uuid": "d270fbf1-50b3-4506-96a5-45047f460c1c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_reviewer_1_b5f154cf",
  "sessionId": "fac75791-ec7a-467d-a47d-5c20edb94374",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012QXDoWJwahjZmSyGmkDdco",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 4013,
      "cache_creation_input_tokens": 1195,
      "cache_read_input_tokens": 27052,
      "output_tokens": 490,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1195,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 4013,
          "output_tokens": 490,
          "cache_read_input_tokens": 27052,
          "cache_creation_input_tokens": 1195,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1195
          },
          "type": "message"
        }
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

_source line 25 · 2026-05-16T00:54:00.009Z_

<details open><summary>🔧 Tool call — Read · `toolu_01RoGSJAyAApn1NxpAUaTAtB`</summary>

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
  "parentUuid": "d270fbf1-50b3-4506-96a5-45047f460c1c",
  "isSidechain": false,
  "requestId": "req_011Cb5LNDGVcfywho2MMd1a4",
  "type": "assistant",
  "uuid": "fb40b043-0f7c-4407-8c21-4477cb8c4927",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_reviewer_1_b5f154cf",
  "sessionId": "fac75791-ec7a-467d-a47d-5c20edb94374",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012QXDoWJwahjZmSyGmkDdco",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 4013,
      "cache_creation_input_tokens": 1195,
      "cache_read_input_tokens": 27052,
      "output_tokens": 490,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1195,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 4013,
          "output_tokens": 490,
          "cache_read_input_tokens": 27052,
          "cache_creation_input_tokens": 1195,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1195
          },
          "type": "message"
        }
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

_source line 26 · 2026-05-16T00:54:02.889Z_

<details><summary>↩ Tool result · `toolu_01FJSvHcYZVt6vdcQu1FpXC3`</summary>

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
  "parentUuid": "ba974e50-1914-4a80-8d75-1b10a156ecda",
  "isSidechain": false,
  "promptId": "86262a68-8f08-4a31-bae8-2266d9a0e2fa",
  "type": "user",
  "uuid": "3edb87b7-3dd8-4eb5-8bce-c16363ff668a",
  "toolUseResult": {
    "matches": [
      "WebFetch"
    ],
    "query": "select:WebFetch",
    "total_deferred_tools": 23
  },
  "sourceToolAssistantUUID": "ba974e50-1914-4a80-8d75-1b10a156ecda",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_reviewer_1_b5f154cf",
  "sessionId": "fac75791-ec7a-467d-a47d-5c20edb94374",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-16T00:54:00.024Z_

<details><summary>↩ Tool result · `toolu_01RoGSJAyAApn1NxpAUaTAtB`</summary>

```text
1	\section{Related Work}
2	\label{sec:related_work}
3	
4	\subsection{Training-Free LLM Information Extraction}
5	\label{sec:rw_training_free}
6	
7	Recent surveys categorize LLM-based IE along instruction-tuning and code-generation axes \cite{llm4ie-survey-2024}. Approaches span instruction tuning for unified IE \cite{instructuie-2023}, code-style schema encoding \cite{knowcoder-2024,codeie-2023}, annotation-guided zero-shot extraction \cite{gollie-2024,adelie-2024}, and schema-driven decoding \cite{slot-2025,oneke-2025}. For NER, methods include zero-shot decomposition by entity type \cite{xie-zeroshot-ner-2023,promptner-2023}, ChatGPT distillation \cite{uniner-2024}, bidirectional transformers \cite{gliner-2024,gliner2-2025}, self-improvement \cite{self-improve-ner-2024}, type descriptions \cite{zeroner-2025}, and guided synthesis \cite{guidex-2025,nuner-2024}. Relation extraction benefits from self-prompting \cite{self-prompting-re-2024} and retrieval-augmented code generation \cite{code4uie-2024}. \citet{familiarity-2025} highlight evaluation pitfalls by quantifying label shifts in zero-shot NER. Separately, constrained decoding via JSON schema enforcement \cite{json-schema-bench-2025} guarantees structurally valid outputs; all our experiments use vLLM's constrained JSON decoding (\S\ref{sec:model}).
8	
9	These methods perform well with moderate schemas (4--20 types) but none investigates how performance degrades as schema complexity scales, nor proposes quantitative metrics for inter-type confusability. Our work fills both gaps.
10	
11	\subsection{Schema Complexity in IE}
12	\label{sec:rw_schema}
13	
14	The most directly related work is LLM-PEE \cite{llm-pee-2025}, which addresses event extraction with massive type inventories by partitioning schemas based on type embedding similarity. LLM-PEE clusters event types and assigns each cluster to a separate extraction prompt, demonstrating improved performance on schemas with hundreds of types. Our work is complementary in three respects. First, whereas LLM-PEE develops an engineering solution---partition to improve extraction---we conduct controlled empirical analysis to understand \emph{why} extraction degrades. Second, LLM-PEE does not disentangle the effects of type count from type confusability; their partitioning simultaneously reduces both. Our BCS-controlled experiments (\S\ref{sec:bcs_controlled}) isolate these as independent degradation channels. Third, our pairwise SCS analysis provides a theoretical explanation for why their similarity-based partitioning works: it reduces Batch Confusability Scores, directly targeting the Channel~2 degradation mechanism. Our SDGD experiments (\S\ref{sec:sdgd}) further reveal that the merge step---not partitioning quality---is the bottleneck in decompose-then-merge pipelines, a limitation that applies to LLM-PEE's approach as well.
15	
16	Other approaches address schema complexity from different angles: hard negative mining during training \cite{iepile-2024}, schema definition optimization \cite{parse-2025}, event schema decomposition \cite{dee-2024}, multi-agent debate for cross-type IE \cite{crossagentie-2025,cmas-ner-2025}, schema-as-tool parameterization \cite{spt-2025}, on-device schema-aware IE \cite{dlisc-2025}, and schema-constrained knowledge graph generation \cite{kggen-2025}. All treat schema complexity as an engineering problem; we instead treat it as a scientific question about the independent mechanisms by which schema properties degrade extraction.
17	
18	\subsection{Representation Degeneration and Embedding Anisotropy}
19	\label{sec:rw_anisotropy}
20	
21	Our centrality confound analysis (\S\ref{sec:centrality_confound}) connects to the representation degeneration literature. \citet{gao-repr-degen-2019} showed that word embeddings degenerate into narrow cones, and \citet{ethayarajh-contextual-2019} extended this to contextual representations. Crucially, \citet{cai-isotropy-clusters-2021} showed that while the global space is anisotropic, local clusters can be isotropic---directly explaining our MAVEN results where single-ontology types form one dense cluster conflating confusability with centrality. \citet{godey-anisotropy-inherent-2024} proved anisotropy is inherent to self-attention, suggesting the centrality confound persists across architectures. Our work provides the first empirical demonstration that this anisotropy creates a measurable confound in IE schema analysis.
22	
23	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fb40b043-0f7c-4407-8c21-4477cb8c4927",
  "isSidechain": false,
  "promptId": "86262a68-8f08-4a31-bae8-2266d9a0e2fa",
  "type": "user",
  "uuid": "e8da9bbe-7279-4f7f-b4fc-ce6f72e41f06",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/related_work.tex",
      "content": "\\section{Related Work}\n\\label{sec:related_work}\n\n\\subsection{Training-Free LLM Information Extraction}\n\\label{sec:rw_training_free}\n\nRecent surveys categorize LLM-based IE along instruction-tuning and code-generation axes \\cite{llm4ie-survey-2024}. Approaches span instruction tuning for unified IE \\cite{instructuie-2023}, code-style schema encoding \\cite{knowcoder-2024,codeie-2023}, annotation-guided zero-shot extraction \\cite{gollie-2024,adelie-2024}, and schema-driven decoding \\cite{slot-2025,oneke-2025}. For NER, methods include zero-shot decomposition by entity type \\cite{xie-zeroshot-ner-2023,promptner-2023}, ChatGPT distillation \\cite{uniner-2024}, bidirectional transformers \\cite{gliner-2024,gliner2-2025}, self-improvement \\cite{self-improve-ner-2024}, type descriptions \\cite{zeroner-2025}, and guided synthesis \\cite{guidex-2025,nuner-2024}. Relation extraction benefits from self-prompting \\cite{self-prompting-re-2024} and retrieval-augmented code generation \\cite{code4uie-2024}. \\citet{familiarity-2025} highlight evaluation pitfalls by quantifying label shifts in zero-shot NER. Separately, constrained decoding via JSON schema enforcement \\cite{json-schema-bench-2025} guarantees structurally valid outputs; all our experiments use vLLM's constrained JSON decoding (\\S\\ref{sec:model}).\n\nThese methods perform well with moderate schemas (4--20 types) but none investigates how performance degrades as schema complexity scales, nor proposes quantitative metrics for inter-type confusability. Our work fills both gaps.\n\n\\subsection{Schema Complexity in IE}\n\\label{sec:rw_schema}\n\nThe most directly related work is LLM-PEE \\cite{llm-pee-2025}, which addresses event extraction with massive type inventories by partitioning schemas based on type embedding similarity. LLM-PEE clusters event types and assigns each cluster to a separate extraction prompt, demonstrating improved performance on schemas with hundreds of types. Our work is complementary in three respects. First, whereas LLM-PEE develops an engineering solution---partition to improve extraction---we conduct controlled empirical analysis to understand \\emph{why} extraction degrades. Second, LLM-PEE does not disentangle the effects of type count from type confusability; their partitioning simultaneously reduces both. Our BCS-controlled experiments (\\S\\ref{sec:bcs_controlled}) isolate these as independent degradation channels. Third, our pairwise SCS analysis provides a theoretical explanation for why their similarity-based partitioning works: it reduces Batch Confusability Scores, directly targeting the Channel~2 degradation mechanism. Our SDGD experiments (\\S\\ref{sec:sdgd}) further reveal that the merge step---not partitioning quality---is the bottleneck in decompose-then-merge pipelines, a limitation that applies to LLM-PEE's approach as well.\n\nOther approaches address schema complexity from different angles: hard negative mining during training \\cite{iepile-2024}, schema definition optimization \\cite{parse-2025}, event schema decomposition \\cite{dee-2024}, multi-agent debate for cross-type IE \\cite{crossagentie-2025,cmas-ner-2025}, schema-as-tool parameterization \\cite{spt-2025}, on-device schema-aware IE \\cite{dlisc-2025}, and schema-constrained knowledge graph generation \\cite{kggen-2025}. All treat schema complexity as an engineering problem; we instead treat it as a scientific question about the independent mechanisms by which schema properties degrade extraction.\n\n\\subsection{Representation Degeneration and Embedding Anisotropy}\n\\label{sec:rw_anisotropy}\n\nOur centrality confound analysis (\\S\\ref{sec:centrality_confound}) connects to the representation degeneration literature. \\citet{gao-repr-degen-2019} showed that word embeddings degenerate into narrow cones, and \\citet{ethayarajh-contextual-2019} extended this to contextual representations. Crucially, \\citet{cai-isotropy-clusters-2021} showed that while the global space is anisotropic, local clusters can be isotropic---directly explaining our MAVEN results where single-ontology types form one dense cluster conflating confusability with centrality. \\citet{godey-anisotropy-inherent-2024} proved anisotropy is inherent to self-attention, suggesting the centrality confound persists across architectures. Our work provides the first empirical demonstration that this anisotropy creates a measurable confound in IE schema analysis.\n\n",
      "numLines": 23,
      "startLine": 1,
      "totalLines": 23
    }
  },
  "sourceToolAssistantUUID": "fb40b043-0f7c-4407-8c21-4477cb8c4927",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_reviewer_1_b5f154cf",
  "sessionId": "fac75791-ec7a-467d-a47d-5c20edb94374",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-16T00:54:00.520Z_

<details open><summary>🔧 Tool call — Read · `toolu_01P4n2SERg9SdvT8oUmid3mE`</summary>

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
  "parentUuid": "e8da9bbe-7279-4f7f-b4fc-ce6f72e41f06",
  "isSidechain": false,
  "requestId": "req_011Cb5LNDGVcfywho2MMd1a4",
  "type": "assistant",
  "uuid": "73174e44-a7d9-4475-88b1-ae0458fe01f2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_reviewer_1_b5f154cf",
  "sessionId": "fac75791-ec7a-467d-a47d-5c20edb94374",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012QXDoWJwahjZmSyGmkDdco",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 4013,
      "cache_creation_input_tokens": 1195,
      "cache_read_input_tokens": 27052,
      "output_tokens": 490,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1195,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 4013,
          "output_tokens": 490,
          "cache_read_input_tokens": 27052,
          "cache_creation_input_tokens": 1195,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1195
          },
          "type": "message"
        }
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

_source line 29 · 2026-05-16T00:54:00.528Z_

<details><summary>↩ Tool result · `toolu_01P4n2SERg9SdvT8oUmid3mE`</summary>

```text
1	\section{Experimental Setup}
2	\label{sec:experimental_setup}
3	
4	We evaluate how prompt schema size and inter-type confusability affect zero-shot LLM extraction across three information extraction tasks: named entity recognition (NER), relation extraction (RE), and event detection (ED).
5	
6	\subsection{Tasks and Datasets}
7	\label{sec:datasets}
8	
9	\paragraph{Few-NERD (NER).}
10	Few-NERD \cite{fewnerd-2021} provides 66 fine-grained entity types organized into 8 coarse categories (person, location, organization, building, art, product, event, other). The dataset spans diverse domains, making it suitable for cross-domain evaluation. We sample 1{,}000 test instances and evaluate with token-level text matching.
11	
12	\paragraph{FewRel (RE).}
13	FewRel \cite{fewrel-2018} contains 80 relation types sourced from Wikidata. Since the validation split covers only 16 relations, we combine the training and validation splits to obtain the full 80-relation pool required for schema-scale experiments, and sample 1{,}000 balanced instances. Each instance provides a sentence with marked head and tail entities; the task is to classify the relation.
14	
15	\paragraph{MAVEN (ED).}
16	MAVEN \cite{maven-2020} defines 168 event types derived from the FrameNet ontology, making it a same-domain schema. We use the validation set (8{,}042 sentences containing 18{,}904 event mentions) for evaluation, as test set labels are not publicly available. The task requires both trigger identification and event type classification.
17	
18	Table~\ref{tab:datasets} summarizes the dataset statistics, including the Schema Confusability Score (SCS) ranges defined in \S\ref{sec:scs}.
19	
20	\begin{table}[t]
21	\centering
22	\small
23	\resizebox{\columnwidth}{!}{%
24	\begin{tabular}{llrrlll}
25	\toprule
26	\textbf{Dataset} & \textbf{Task} & \textbf{\# Types} & \textbf{\# Eval Units} & \textbf{Domain} & \textbf{BCS Range} & \textbf{Embedding} \\
27	\midrule
28	Few-NERD & NER & 66 & 1{,}000 & Cross & 0.77--0.93 & Qwen3-32B \\
29	FewRel & RE & 80 & 1{,}000 & Cross & 0.42--0.97 & MiniLM \\
30	MAVEN & ED & 168 & 18{,}904\rlap{$^\dagger$} & Same & 0.87--0.97 & MiniLM \\
31	\bottomrule
32	\end{tabular}}
33	\caption{Dataset statistics. BCS Range indicates the min--max Batch Confusability Scores across count-curve batches (Experiment~1). Embedding column indicates the model used for SCS/BCS computation. $^\dagger$Trigger mentions across 8{,}042 sentences in 710 documents.}
34	\label{tab:datasets}
35	\end{table}
36	
37	\subsection{Schema Confusability Score (SCS)}
38	\label{sec:scs}
39	
40	We introduce the Schema Confusability Score to quantify semantic overlap between types in a schema. Given a type $t$ with name string $\text{name}(t)$, an embedding function $\text{embed}(\cdot)$ maps the type name to a vector representation. The \textbf{pairwise SCS} between types $t_i$ and $t_j$ is:
41	{\small
42	\[
43	\text{SCS}(t_i, t_j) = \cos\bigl(\text{embed}(\text{name}(t_i)),\; \text{embed}(\text{name}(t_j))\bigr)
44	\]
45	}
46	
47	For a batch of types $B = \{t_1, \ldots, t_k\}$, the \textbf{Batch Confusability Score (BCS)} aggregates all pairwise similarities:
48	\[
49	\text{BCS}(B) = \frac{1}{\binom{k}{2}} \sum_{i < j,\; t_i, t_j \in B} \text{SCS}(t_i, t_j)
50	\]
51	
52	We compute SCS with two embedding models: (1)~Qwen3-32B \cite{qwen3-2025} hidden-state representations (5{,}120-d), which capture the extraction model's own type representations, and (2)~all-MiniLM-L6-v2 \cite{minilm-2019}, a 384-dimensional general-purpose sentence encoder. Both use type name strings only, without definitions or descriptions, to reflect the information available to the model at inference time.
53	
54	\subsection{Experimental Design}
55	\label{sec:exp_design}
56	
57	We conduct two complementary experimental paradigms.
58	
59	\paragraph{Experiment 1: Count Curves.}
60	We vary the number of types presented in the prompt schema to measure performance as a function of schema size. For each count level, we sample 5 random type batches and evaluate the same 1{,}000 test samples across all batches. At count${}=1$, every type is evaluated individually as a solo baseline. The count levels follow natural partition points in each schema's type hierarchy rather than uniform spacing: \{1, 2, 6, 12, 22, 44, 64\} for Few-NERD, \{1, 4, 8, 16, 32, 64, 80\} for FewRel, and \{1, 6, 12, 22, 44, 64\} for MAVEN.
61	
62	\paragraph{Experiment 2: BCS-Controlled.}
63	We fix the type count and vary the Batch Confusability Score to isolate the effect of inter-type similarity from schema size. For each count level, we construct one low-BCS batch (types with the lowest pairwise similarities), one high-BCS batch (types with the highest pairwise similarities), and 25 random batches (27 total per count level). We run this paradigm on Few-NERD at count$\,\in\{6, 12\}$ and on FewRel at count$\,\in\{8, 16\}$, the latter evaluated on both a 16-relation pool and the full 80-relation pool. For MAVEN, we conduct analogous BCS-controlled experiments at count$\,\in\{6, 12\}$ with 27 batches per level; however, the same-domain nature of MAVEN's FrameNet-derived types introduces a centrality confound that complicates BCS interpretation. We report these results separately in \S\ref{sec:centrality_confound}.
64	
65	\subsection{Evaluation Metrics}
66	\label{sec:metrics}
67	
68	We use task-appropriate metrics that reflect the distinct nature of each extraction problem.
69	
70	\paragraph{NER (Few-NERD): Text-match F1.}
71	A predicted entity is a true positive if the predicted text string exactly matches (case-insensitive) a gold entity text \emph{and} the predicted type matches the gold type. This text-match evaluation operates at the entity level rather than the token level. We report Precision, Recall, and F1.
72	
73	\paragraph{RE (FewRel): Accuracy.}
74	Each sample has exactly one ground-truth relation. A prediction is correct if the predicted relation label exactly matches the gold label. We report Accuracy.
75	
76	\paragraph{ED (MAVEN): Relaxed F1.}
77	A predicted trigger is a true positive if (a)~any token overlap exists between the predicted trigger span and a gold trigger span, \emph{and} (b)~the predicted event type matches the gold event type. This relaxed matching is necessary because event triggers are inherently ambiguous in boundary (e.g., ``was killed'' vs.\ ``killed''). We report Relaxed F1.
78	
79	The choice of different metrics across tasks reflects their structural differences: NER is span-level extraction where precision--recall trade-offs are informative; RE is a classification task where accuracy directly measures correctness; ED combines trigger identification with type classification, requiring relaxed span matching to avoid penalizing legitimate boundary variation.
80	
81	\subsection{Model and Inference}
82	\label{sec:model}
83	
84	\paragraph{Primary model.}
85	We use Qwen3-32B-FP8 \cite{qwen3-2025}, selected for its strong instruction-following capability, native structured JSON output support, and the practical advantage that the FP8-quantized 32B model fits on a single NVIDIA RTX PRO 6000 Blackwell Server Edition (96\,GB). The model is served via vLLM (v0.20.2) \cite{vllm-2023} with \texttt{max\_model\_len=4096} and \texttt{gpu\_memory\_utilization=0.95}. We use two prompt versions across experiments. The v1 prompt (used for count-curve and BCS-controlled NER experiments) requests start/end character offsets alongside entity text; however, the model fabricates offsets in 96.5\% of predictions, so we evaluate exclusively via text matching (\S\ref{sec:metrics}), which is robust to offset errors. The v2 prompt (used for all subsequent experiments) drops the offset requirement and adds explicit output format constraints and role instructions, doubling precision with minimal recall loss. Both versions provide a JSON-formatted schema listing all type names for the current batch; the model outputs structured JSON containing extracted entities, relations, or events. We use greedy decoding (temperature${}\,=\,0$) and a fixed random seed (42) for all batch sampling and bootstrap resampling, ensuring full reproducibility.
86	
87	\paragraph{Cross-model validation.}
88	To test whether schema-induced degradation generalizes beyond the primary model, we replicate both experimental paradigms on Few-NERD and FewRel using Meta-Llama-3.1-8B-Instruct, a $4\times$ smaller model from a different model family. For NER we use text-match recall (Llama does not reliably produce span offsets); for RE we use accuracy.
89	
90	\paragraph{Statistical estimation.}
91	All key metrics are accompanied by 95\% bootstrap confidence intervals computed from 1{,}000 bootstrap resamples using the percentile method.
92	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "73174e44-a7d9-4475-88b1-ae0458fe01f2",
  "isSidechain": false,
  "promptId": "86262a68-8f08-4a31-bae8-2266d9a0e2fa",
  "type": "user",
  "uuid": "aac55d94-efd6-41a2-8ea5-56271a4913c0",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/experimental_setup.tex",
      "content": "\\section{Experimental Setup}\n\\label{sec:experimental_setup}\n\nWe evaluate how prompt schema size and inter-type confusability affect zero-shot LLM extraction across three information extraction tasks: named entity recognition (NER), relation extraction (RE), and event detection (ED).\n\n\\subsection{Tasks and Datasets}\n\\label{sec:datasets}\n\n\\paragraph{Few-NERD (NER).}\nFew-NERD \\cite{fewnerd-2021} provides 66 fine-grained entity types organized into 8 coarse categories (person, location, organization, building, art, product, event, other). The dataset spans diverse domains, making it suitable for cross-domain evaluation. We sample 1{,}000 test instances and evaluate with token-level text matching.\n\n\\paragraph{FewRel (RE).}\nFewRel \\cite{fewrel-2018} contains 80 relation types sourced from Wikidata. Since the validation split covers only 16 relations, we combine the training and validation splits to obtain the full 80-relation pool required for schema-scale experiments, and sample 1{,}000 balanced instances. Each instance provides a sentence with marked head and tail entities; the task is to classify the relation.\n\n\\paragraph{MAVEN (ED).}\nMAVEN \\cite{maven-2020} defines 168 event types derived from the FrameNet ontology, making it a same-domain schema. We use the validation set (8{,}042 sentences containing 18{,}904 event mentions) for evaluation, as test set labels are not publicly available. The task requires both trigger identification and event type classification.\n\nTable~\\ref{tab:datasets} summarizes the dataset statistics, including the Schema Confusability Score (SCS) ranges defined in \\S\\ref{sec:scs}.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llrrlll}\n\\toprule\n\\textbf{Dataset} & \\textbf{Task} & \\textbf{\\# Types} & \\textbf{\\# Eval Units} & \\textbf{Domain} & \\textbf{BCS Range} & \\textbf{Embedding} \\\\\n\\midrule\nFew-NERD & NER & 66 & 1{,}000 & Cross & 0.77--0.93 & Qwen3-32B \\\\\nFewRel & RE & 80 & 1{,}000 & Cross & 0.42--0.97 & MiniLM \\\\\nMAVEN & ED & 168 & 18{,}904\\rlap{$^\\dagger$} & Same & 0.87--0.97 & MiniLM \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Dataset statistics. BCS Range indicates the min--max Batch Confusability Scores across count-curve batches (Experiment~1). Embedding column indicates the model used for SCS/BCS computation. $^\\dagger$Trigger mentions across 8{,}042 sentences in 710 documents.}\n\\label{tab:datasets}\n\\end{table}\n\n\\subsection{Schema Confusability Score (SCS)}\n\\label{sec:scs}\n\nWe introduce the Schema Confusability Score to quantify semantic overlap between types in a schema. Given a type $t$ with name string $\\text{name}(t)$, an embedding function $\\text{embed}(\\cdot)$ maps the type name to a vector representation. The \\textbf{pairwise SCS} between types $t_i$ and $t_j$ is:\n{\\small\n\\[\n\\text{SCS}(t_i, t_j) = \\cos\\bigl(\\text{embed}(\\text{name}(t_i)),\\; \\text{embed}(\\text{name}(t_j))\\bigr)\n\\]\n}\n\nFor a batch of types $B = \\{t_1, \\ldots, t_k\\}$, the \\textbf{Batch Confusability Score (BCS)} aggregates all pairwise similarities:\n\\[\n\\text{BCS}(B) = \\frac{1}{\\binom{k}{2}} \\sum_{i < j,\\; t_i, t_j \\in B} \\text{SCS}(t_i, t_j)\n\\]\n\nWe compute SCS with two embedding models: (1)~Qwen3-32B \\cite{qwen3-2025} hidden-state representations (5{,}120-d), which capture the extraction model's own type representations, and (2)~all-MiniLM-L6-v2 \\cite{minilm-2019}, a 384-dimensional general-purpose sentence encoder. Both use type name strings only, without definitions or descriptions, to reflect the information available to the model at inference time.\n\n\\subsection{Experimental Design}\n\\label{sec:exp_design}\n\nWe conduct two complementary experimental paradigms.\n\n\\paragraph{Experiment 1: Count Curves.}\nWe vary the number of types presented in the prompt schema to measure performance as a function of schema size. For each count level, we sample 5 random type batches and evaluate the same 1{,}000 test samples across all batches. At count${}=1$, every type is evaluated individually as a solo baseline. The count levels follow natural partition points in each schema's type hierarchy rather than uniform spacing: \\{1, 2, 6, 12, 22, 44, 64\\} for Few-NERD, \\{1, 4, 8, 16, 32, 64, 80\\} for FewRel, and \\{1, 6, 12, 22, 44, 64\\} for MAVEN.\n\n\\paragraph{Experiment 2: BCS-Controlled.}\nWe fix the type count and vary the Batch Confusability Score to isolate the effect of inter-type similarity from schema size. For each count level, we construct one low-BCS batch (types with the lowest pairwise similarities), one high-BCS batch (types with the highest pairwise similarities), and 25 random batches (27 total per count level). We run this paradigm on Few-NERD at count$\\,\\in\\{6, 12\\}$ and on FewRel at count$\\,\\in\\{8, 16\\}$, the latter evaluated on both a 16-relation pool and the full 80-relation pool. For MAVEN, we conduct analogous BCS-controlled experiments at count$\\,\\in\\{6, 12\\}$ with 27 batches per level; however, the same-domain nature of MAVEN's FrameNet-derived types introduces a centrality confound that complicates BCS interpretation. We report these results separately in \\S\\ref{sec:centrality_confound}.\n\n\\subsection{Evaluation Metrics}\n\\label{sec:metrics}\n\nWe use task-appropriate metrics that reflect the distinct nature of each extraction problem.\n\n\\paragraph{NER (Few-NERD): Text-match F1.}\nA predicted entity is a true positive if the predicted text string exactly matches (case-insensitive) a gold entity text \\emph{and} the predicted type matches the gold type. This text-match evaluation operates at the entity level rather than the token level. We report Precision, Recall, and F1.\n\n\\paragraph{RE (FewRel): Accuracy.}\nEach sample has exactly one ground-truth relation. A prediction is correct if the predicted relation label exactly matches the gold label. We report Accuracy.\n\n\\paragraph{ED (MAVEN): Relaxed F1.}\nA predicted trigger is a true positive if (a)~any token overlap exists between the predicted trigger span and a gold trigger span, \\emph{and} (b)~the predicted event type matches the gold event type. This relaxed matching is necessary because event triggers are inherently ambiguous in boundary (e.g., ``was killed'' vs.\\ ``killed''). We report Relaxed F1.\n\nThe choice of different metrics across tasks reflects their structural differences: NER is span-level extraction where precision--recall trade-offs are informative; RE is a classification task where accuracy directly measures correctness; ED combines trigger identification with type classification, requiring relaxed span matching to avoid penalizing legitimate boundary variation.\n\n\\subsection{Model and Inference}\n\\label{sec:model}\n\n\\paragraph{Primary model.}\nWe use Qwen3-32B-FP8 \\cite{qwen3-2025}, selected for its strong instruction-following capability, native structured JSON output support, and the practical advantage that the FP8-quantized 32B model fits on a single NVIDIA RTX PRO 6000 Blackwell Server Edition (96\\,GB). The model is served via vLLM (v0.20.2) \\cite{vllm-2023} with \\texttt{max\\_model\\_len=4096} and \\texttt{gpu\\_memory\\_utilization=0.95}. We use two prompt versions across experiments. The v1 prompt (used for count-curve and BCS-controlled NER experiments) requests start/end character offsets alongside entity text; however, the model fabricates offsets in 96.5\\% of predictions, so we evaluate exclusively via text matching (\\S\\ref{sec:metrics}), which is robust to offset errors. The v2 prompt (used for all subsequent experiments) drops the offset requirement and adds explicit output format constraints and role instructions, doubling precision with minimal recall loss. Both versions provide a JSON-formatted schema listing all type names for the current batch; the model outputs structured JSON containing extracted entities, relations, or events. We use greedy decoding (temperature${}\\,=\\,0$) and a fixed random seed (42) for all batch sampling and bootstrap resampling, ensuring full reproducibility.\n\n\\paragraph{Cross-model validation.}\nTo test whether schema-induced degradation generalizes beyond the primary model, we replicate both experimental paradigms on Few-NERD and FewRel using Meta-Llama-3.1-8B-Instruct, a $4\\times$ smaller model from a different model family. For NER we use text-match recall (Llama does not reliably produce span offsets); for RE we use accuracy.\n\n\\paragraph{Statistical estimation.}\nAll key metrics are accompanied by 95\\% bootstrap confidence intervals computed from 1{,}000 bootstrap resamples using the percentile method.\n",
      "numLines": 92,
      "startLine": 1,
      "totalLines": 92
    }
  },
  "sourceToolAssistantUUID": "73174e44-a7d9-4475-88b1-ae0458fe01f2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_reviewer_1_b5f154cf",
  "sessionId": "fac75791-ec7a-467d-a47d-5c20edb94374",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 30 · 2026-05-16T00:54:01.074Z_

<details open><summary>🔧 Tool call — Read · `toolu_01DTc9DwdXCkpkZ4XgiwbvuY`</summary>

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
  "parentUuid": "aac55d94-efd6-41a2-8ea5-56271a4913c0",
  "isSidechain": false,
  "requestId": "req_011Cb5LNDGVcfywho2MMd1a4",
  "type": "assistant",
  "uuid": "8e499ff3-4884-4137-92a8-e19f40e07adc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_reviewer_1_b5f154cf",
  "sessionId": "fac75791-ec7a-467d-a47d-5c20edb94374",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012QXDoWJwahjZmSyGmkDdco",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 4013,
      "cache_creation_input_tokens": 1195,
      "cache_read_input_tokens": 27052,
      "output_tokens": 490,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1195,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 4013,
          "output_tokens": 490,
          "cache_read_input_tokens": 27052,
          "cache_creation_input_tokens": 1195,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1195
          },
          "type": "message"
        }
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

_source line 31 · 2026-05-16T00:54:01.079Z_

<details><summary>↩ Tool result · `toolu_01DTc9DwdXCkpkZ4XgiwbvuY`</summary>

```text
1	\section{Results}
2	\label{sec:results}
3	
4	\subsection{Count-Degradation Curves}
5	\label{sec:count_curves}
6	
7	We first examine how extraction performance changes as the number of types in the prompt schema increases (Experiment~1; see Figure~\ref{fig:count_curves} in the Appendix for visualizations).
8	
9	\paragraph{NER (Few-NERD).}
10	Recall generally declines from 0.72 at count${}\,=\,1$ to 0.42 at count${}\,=\,64$, a 42\% relative drop, with minor non-monotonicity at intermediate counts (e.g., 0.527 at count${}\,=\,22$ to 0.551 at count${}\,=\,44$). Precision moves in the opposite direction, rising from 0.11 to 0.52, reflecting a shift from over-prediction to under-prediction as more candidate types compete in the prompt. F1 exhibits an inverted-U shape, peaking at intermediate counts where the precision--recall trade-off is most balanced.
11	
12	\paragraph{RE (FewRel).}
13	Accuracy drops monotonically from 85.7\% at count${}\,=\,1$ through 58.8\% at count${}\,=\,40$ to 50.4\% at count${}\,=\,80$, a near-halving when the model must discriminate among all 80 relation types simultaneously. (The count${}\,=\,40$ evaluation uses 40-relation subsets sampled from the 80-relation pool, not an independent schema.)
14	
15	\paragraph{ED (MAVEN).}
16	In contrast to NER and RE, MAVEN relaxed F1 \emph{increases} from 0.106 at count${}\,=\,1$ to 0.247 at count${}\,=\,44$. This reversal arises from three properties of the MAVEN setup: (i)~trigger-level relaxed matching, which requires only token overlap rather than exact span match; (ii)~MAVEN's 168 event types derive from the FrameNet ontology, forming a same-domain hierarchy where co-presented types provide disambiguating context; and (iii)~extreme class imbalance---rare event types benefit from being presented alongside related types that prime the model toward the correct semantic region. We investigate this reversal further in \S\ref{sec:centrality_confound}.
17	
18	\paragraph{Cross-model replication.}
19	Channel~1 replicates across model families: on Few-NERD, Meta-Llama-3.1-8B-Instruct shows a $-$43\,pp recall decline (0.702 at count${}\,=\,1$ to 0.273 at count${}\,=\,64$), compared to $-$34\,pp for Qwen3-32B (Table~\ref{tab:cross_model} in the Appendix). Per-batch recall correlation between the two models is $r = 0.725$, indicating that schema configuration drives difficulty rather than model-specific factors.
20	
21	\paragraph{Summary.}
22	Schema size degrades extraction quality for NER and RE (Channel~1: count $\to$ recall decline), but this pattern does not hold universally. MAVEN's reversed trend demonstrates that task structure and evaluation protocol mediate the count--performance relationship. Both channels replicate on Llama-3.1-8B: the count channel ($r = 0.725$) and the confusability channel on RE (\S\ref{sec:bcs_controlled}).
23	
24	\subsection{Pairwise Confusability and Type Confusion}
25	\label{sec:pairwise}
26	
27	We test whether pairwise SCS predicts type-level confusion rates. For each type pair $(t_i, t_j)$, we compute the confusion rate---the fraction of $t_i$ gold instances misclassified as $t_j$---and correlate it with $\text{SCS}(t_i, t_j)$. Table~\ref{tab:pairwise} reports Pearson correlations with bootstrap 95\% CIs.
28	
29	\begin{table}[t]
30	\centering
31	\small
32	\resizebox{\columnwidth}{!}{%
33	\begin{tabular}{llrrrrr}
34	\toprule
35	\textbf{Dataset} & \textbf{Embed.} & \textbf{$n$ pairs} & \textbf{$r$} & \textbf{$r^2$} & \textbf{95\% CI} & \textbf{$p$} \\
36	\midrule
37	Few-NERD & Qwen3 & 1{,}953 & 0.112 & 0.013 & {[}0.076, 0.156{]} & ${<}10^{-12}$ \\
38	MAVEN & MiniLM & 11{,}026 & 0.129 & 0.017 & {[}0.104, 0.156{]} & ${<}10^{-10}$ \\
39	\bottomrule
40	\end{tabular}}
41	\caption{Pairwise SCS--confusion correlation. $r^2$ indicates the fraction of variance in type confusion explained by embedding similarity. Both correlations are modest in magnitude but robust across datasets and embedding models ($p < 10^{-10}$).}
42	\label{tab:pairwise}
43	\end{table}
44	
45	The correlations are modest: $r^2 \approx 1.3\text{--}1.7\%$, meaning pairwise confusability explains roughly 1.5\% of the variance in type confusion. Other factors---entity frequency, prompt position effects \cite{lost-in-middle-2024}, and type definition quality---likely contribute to the remaining variance. We omit FewRel from the pairwise analysis: RE is a per-instance classification task where each sample maps to exactly one relation, so the directional confusion matrix between all type pairs is not directly comparable to the span-level confusion rates used for NER and ED. The BCS-controlled experiments (\S\ref{sec:bcs_controlled}) provide stronger, interventional evidence for the confusability effect on RE. Nevertheless, the signal is robust: both correlations survive bootstrap resampling with CIs bounded well above zero, and replicate across two unrelated embedding spaces (Qwen3 hidden states and MiniLM sentence embeddings).
46	
47	Spearman rank correlations from the SCS validation experiment (exp-015) corroborate these findings. Across all type pairs, Qwen3 yields $\rho = 0.168$ ($p = 7.3 \times 10^{-14}$) and MiniLM yields $\rho = 0.144$ ($p = 1.7 \times 10^{-10}$). Restricting to pairs with nonzero confusion strengthens the association: $\rho = 0.272$ ($p = 5 \times 10^{-5}$) for Qwen3 and $\rho = 0.306$ ($p = 4.6 \times 10^{-6}$) for MiniLM, indicating that among types the model actually confuses, embedding similarity is a stronger predictor.
48	
49	We frame these results as identifying one factor among several that drive type confusion, but the first to be empirically isolated in a controlled zero-shot IE setting. Although pairwise $r^2$ is modest, the signal concentrates among types the model actually confuses ($\rho = 0.27\text{--}0.31$) and compounds at the batch level into accuracy gaps reaching 31.2\,pp (\S\ref{sec:bcs_controlled}). Qwen3 yields stronger overall correlation ($\rho = 0.168$ vs.\ $0.144$), while MiniLM yields a stronger association among nonzero-confusion pairs ($\rho = 0.306$ vs.\ $0.272$); extraction-model embeddings are preferable when available.
50	
51	\subsection{BCS-Controlled Experiments}
52	\label{sec:bcs_controlled}
53	
54	To move from correlational to interventional evidence, we fix the type count and vary BCS. Table~\ref{tab:bcs_controlled} reports FewRel accuracy under low-BCS and high-BCS batches at two schema sizes.
55	
56	\begin{table}[t]
57	\centering
58	\small
59	\resizebox{\columnwidth}{!}{%
60	\begin{tabular}{lcrrrr}
61	\toprule
62	\textbf{Schema} & \textbf{Count} & \textbf{Low-BCS} & \textbf{High-BCS} & \textbf{$\Delta$ (pp)} & \textbf{95\% CI} \\
63	\midrule
64	16-rel & 8 & 88.9\% & 79.8\% & $-$9.1 & --- \\
65	80-rel & 8 & 82.3\% & 51.0\% & $-$31.2 & {[}17.7, 42.7{]} \\
66	80-rel & 16 & 82.8\% & 51.6\% & $-$31.2 & {[}22.9, 39.6{]} \\
67	\bottomrule
68	\end{tabular}}
69	\caption{BCS-controlled FewRel accuracy. Low-BCS batches contain maximally dissimilar types; high-BCS batches contain maximally similar types. The confusability gap widens from 9.1\,pp at 16 relations to 31.2\,pp at 80 relations. The 16-relation condition used a single extreme batch per BCS level; bootstrap CIs require multiple batches.}
70	\label{tab:bcs_controlled}
71	\end{table}
72	
73	At the 16-relation scale, switching from low-BCS to high-BCS batches reduces accuracy by 9.1 percentage points. Scaling to the full 80-relation pool amplifies this gap to 31.2\,pp (95\% CI: [17.7, 42.7])---a $3.4\times$ amplification ($31.2 / 9.1$; range $1.9\text{--}4.7\times$ given the 80-rel CI). The effect is stable across count levels: at count${}\,=\,16$, the gap remains 31.2\,pp (CI: [22.9, 39.6]). An intermediate evaluation at count${}\,=\,40$ (40-relation subsets sampled from the 80-relation pool) yields accuracy 0.588 and BCS gaps of $-$33.3\,pp (count 8) and $-$31.8\,pp (count 16), consistent with the 80-relation results and confirming monotonic decline within the pool.
74	
75	This amplification has a natural interpretation. A larger type pool provides more opportunities for semantically similar types to co-occur, expanding the confusion space. BCS captures this expanded space: at 80 relations, extreme high-BCS batches pack tightly clustered types that the model cannot reliably distinguish, while the same count of well-separated types preserves near-solo-evaluation accuracy.
76	
77	\paragraph{Cross-model validation.}
78	The confusability effect replicates on Meta-Llama-3.1-8B-Instruct: on FewRel, the BCS gap is $-$27.1\,pp at count${}\,=\,8$ (low-BCS 78.1\% vs.\ high-BCS 51.0\%) and $-$23.9\,pp at count${}\,=\,16$ (75.5\% vs.\ 51.6\%), reaching 77--87\% of Qwen3-32B's $-$31.2\,pp. Strikingly, high-BCS accuracy is model-invariant: both models converge to $\approx$51\% under high confusability (count${}\,=\,8$: 51.0\% vs.\ 51.0\%; count${}\,=\,16$: 51.6\% vs.\ 51.6\%), while cross-model divergence is confined to the low-BCS regime where model capacity matters. This pattern indicates that confusable type sets create a task-inherent difficulty floor independent of model scale.
79	
80	\subsection{Multi-Channel Degradation}
81	\label{sec:multi_channel}
82	
83	We now decompose extraction errors into an error taxonomy to distinguish the mechanisms behind performance loss. Table~\ref{tab:error_taxonomy} quantifies how each error type scales with BCS.
84	
85	\begin{table}[t]
86	\centering
87	\small
88	\resizebox{\columnwidth}{!}{%
89	\begin{tabular}{llrrrrrrr}
90	\toprule
91	 & & \multicolumn{5}{c}{\textbf{BCS Bin}} & & \\
92	\cmidrule(lr){3-7}
93	\textbf{Task} & \textbf{Error} & \textbf{Solo} & \textbf{Low} & \textbf{Mid} & \textbf{High} & \textbf{V.High} & \textbf{$\rho$} & \textbf{$p$} \\
94	\midrule
95	NER & IntraSub & 0\% & 1.6\% & 10.6\% & 49.4\% & --- & 1.000 & ${<}0.001$ \\
96	RE  & IntraSub & 0\% & 4.2\% & 13.0\% & 20.3\% & 32.3\% & 0.954 & ${<}10^{-6}$ \\
97	\midrule
98	NER & Missed & --- & 42.8\% & 64.8\% & 49.9\% & --- & --- & --- \\
99	RE  & Missed & --- & 10.4\% & 11.3\% & 13.1\% & 15.7\% & --- & --- \\
100	\bottomrule
101	\end{tabular}}
102	\caption{Intra-batch substitution (IntraSub) and missed-entity rates by BCS bin, with Spearman $\rho$ computed over $n=154$ individual batches (RE) and $n=148$ batches (NER). NER has 4 BCS bins; RE has 5. RE missed rates remain flat (10--16\%), but NER missed rates are substantially higher (43--65\%) and non-monotonic, revealing task-dependent error mechanisms.}
103	\label{tab:error_taxonomy}
104	\end{table}
105	
106	Three findings emerge. First, intra-batch substitution scales monotonically with BCS in both tasks: NER IntraSub rises from 0\% (solo) to 49.4\% (high BCS) with $\rho = 1.0$ ($p < 0.001$), and RE IntraSub rises from 0\% through 20.3\% (high) to 32.3\% (very high) with $\rho = 0.954$ ($p < 10^{-6}$). Second, 100\% of type confusion errors in RE are intra-batch---the model exclusively confuses types present in the current prompt, never hallucinating types outside the schema. Third, the tasks diverge on missed-entity rates: RE rates remain flat across BCS bins (10.4--15.7\%), but NER rates are substantially higher (42.8--64.8\%) and non-monotonic. This suggests that in span-level extraction, confusable type sets impair entity detection itself, not only type discrimination.
107	
108	The extreme-batch analysis sharpens this picture. At count${}\,=\,6$, high-BCS batches produce $27.5\times$ more confusion than low-BCS batches under extreme selection, versus $1.7\times$ under random batching. At count${}\,=\,12$, the ratios are $9.9\times$ (extreme) versus $2.4\times$ (random). These multiplicative gaps confirm that BCS captures a functionally relevant dimension of schema difficulty, not merely a correlate.
109	
110	Taken together, these results establish two degradation channels: \textbf{Channel~1} (count $\to$ recall decline, \S\ref{sec:count_curves}) and \textbf{Channel~2} (confusability $\to$ type confusion, this section). In RE, the channels are cleanly separable---confusability drives substitution errors while detection remains stable. In NER, Channel~2 additionally impairs entity detection, suggesting that the two channels interact for span-level extraction tasks where type ambiguity and boundary ambiguity are coupled.
111	
112	\subsection{Centrality Confound on Homogeneous Schemas}
113	\label{sec:centrality_confound}
114	
115	Per-type analysis on MAVEN reveals an anomaly: the correlation between mean BCS and per-type error rate is \emph{positive}---Qwen3 $\rho = +0.189$ ($p = 0.021$) and MiniLM $\rho = +0.208$ ($p = 0.011$)---opposite to the negative direction predicted by the confusability hypothesis.
116	
117	This reversal traces to a property of same-domain schemas documented by \citet{cai-isotropy-clusters-2021}: when all types derive from a single ontology (here, FrameNet), their embeddings collapse into a single cluster in representation space. In this regime, a type's mean BCS conflates two distinct properties: (i)~confusability with neighbors, which should increase errors, and (ii)~centrality within the cluster, which correlates with being a well-represented, high-frequency type that LLMs extract reliably. The centrality signal dominates, flipping the aggregate correlation.
118	
119	Critically, the pairwise SCS--confusion correlation remains intact: MAVEN MiniLM pairwise $r = 0.129$ (CI: [0.104, 0.156], $p < 10^{-10}$), consistent with the values in Table~\ref{tab:pairwise}. The problem lies in the aggregation step (mean BCS per type), not in the pairwise signal itself.
120	
121	Few-NERD, whose 66 types span 8 coarse categories across diverse domains, does not exhibit this confound. Its per-type correlation is $\rho = -0.293$ ($p = 0.02$, $n = 63$), in the expected negative direction: types with higher mean confusability have higher error rates. The cross-domain schema spans multiple embedding clusters, breaking the centrality--confusability conflation.
122	
123	This analysis carries a practical implication: mean BCS is a reliable predictor of schema difficulty only for cross-domain schemas. For same-domain schemas where types form a single semantic cluster, pairwise SCS should be used directly, or the centrality component must be factored out before aggregation.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8e499ff3-4884-4137-92a8-e19f40e07adc",
  "isSidechain": false,
  "promptId": "86262a68-8f08-4a31-bae8-2266d9a0e2fa",
  "type": "user",
  "uuid": "f21ad4b6-77a5-499e-a796-2ed41313b659",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex",
      "content": "\\section{Results}\n\\label{sec:results}\n\n\\subsection{Count-Degradation Curves}\n\\label{sec:count_curves}\n\nWe first examine how extraction performance changes as the number of types in the prompt schema increases (Experiment~1; see Figure~\\ref{fig:count_curves} in the Appendix for visualizations).\n\n\\paragraph{NER (Few-NERD).}\nRecall generally declines from 0.72 at count${}\\,=\\,1$ to 0.42 at count${}\\,=\\,64$, a 42\\% relative drop, with minor non-monotonicity at intermediate counts (e.g., 0.527 at count${}\\,=\\,22$ to 0.551 at count${}\\,=\\,44$). Precision moves in the opposite direction, rising from 0.11 to 0.52, reflecting a shift from over-prediction to under-prediction as more candidate types compete in the prompt. F1 exhibits an inverted-U shape, peaking at intermediate counts where the precision--recall trade-off is most balanced.\n\n\\paragraph{RE (FewRel).}\nAccuracy drops monotonically from 85.7\\% at count${}\\,=\\,1$ through 58.8\\% at count${}\\,=\\,40$ to 50.4\\% at count${}\\,=\\,80$, a near-halving when the model must discriminate among all 80 relation types simultaneously. (The count${}\\,=\\,40$ evaluation uses 40-relation subsets sampled from the 80-relation pool, not an independent schema.)\n\n\\paragraph{ED (MAVEN).}\nIn contrast to NER and RE, MAVEN relaxed F1 \\emph{increases} from 0.106 at count${}\\,=\\,1$ to 0.247 at count${}\\,=\\,44$. This reversal arises from three properties of the MAVEN setup: (i)~trigger-level relaxed matching, which requires only token overlap rather than exact span match; (ii)~MAVEN's 168 event types derive from the FrameNet ontology, forming a same-domain hierarchy where co-presented types provide disambiguating context; and (iii)~extreme class imbalance---rare event types benefit from being presented alongside related types that prime the model toward the correct semantic region. We investigate this reversal further in \\S\\ref{sec:centrality_confound}.\n\n\\paragraph{Cross-model replication.}\nChannel~1 replicates across model families: on Few-NERD, Meta-Llama-3.1-8B-Instruct shows a $-$43\\,pp recall decline (0.702 at count${}\\,=\\,1$ to 0.273 at count${}\\,=\\,64$), compared to $-$34\\,pp for Qwen3-32B (Table~\\ref{tab:cross_model} in the Appendix). Per-batch recall correlation between the two models is $r = 0.725$, indicating that schema configuration drives difficulty rather than model-specific factors.\n\n\\paragraph{Summary.}\nSchema size degrades extraction quality for NER and RE (Channel~1: count $\\to$ recall decline), but this pattern does not hold universally. MAVEN's reversed trend demonstrates that task structure and evaluation protocol mediate the count--performance relationship. Both channels replicate on Llama-3.1-8B: the count channel ($r = 0.725$) and the confusability channel on RE (\\S\\ref{sec:bcs_controlled}).\n\n\\subsection{Pairwise Confusability and Type Confusion}\n\\label{sec:pairwise}\n\nWe test whether pairwise SCS predicts type-level confusion rates. For each type pair $(t_i, t_j)$, we compute the confusion rate---the fraction of $t_i$ gold instances misclassified as $t_j$---and correlate it with $\\text{SCS}(t_i, t_j)$. Table~\\ref{tab:pairwise} reports Pearson correlations with bootstrap 95\\% CIs.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llrrrrr}\n\\toprule\n\\textbf{Dataset} & \\textbf{Embed.} & \\textbf{$n$ pairs} & \\textbf{$r$} & \\textbf{$r^2$} & \\textbf{95\\% CI} & \\textbf{$p$} \\\\\n\\midrule\nFew-NERD & Qwen3 & 1{,}953 & 0.112 & 0.013 & {[}0.076, 0.156{]} & ${<}10^{-12}$ \\\\\nMAVEN & MiniLM & 11{,}026 & 0.129 & 0.017 & {[}0.104, 0.156{]} & ${<}10^{-10}$ \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Pairwise SCS--confusion correlation. $r^2$ indicates the fraction of variance in type confusion explained by embedding similarity. Both correlations are modest in magnitude but robust across datasets and embedding models ($p < 10^{-10}$).}\n\\label{tab:pairwise}\n\\end{table}\n\nThe correlations are modest: $r^2 \\approx 1.3\\text{--}1.7\\%$, meaning pairwise confusability explains roughly 1.5\\% of the variance in type confusion. Other factors---entity frequency, prompt position effects \\cite{lost-in-middle-2024}, and type definition quality---likely contribute to the remaining variance. We omit FewRel from the pairwise analysis: RE is a per-instance classification task where each sample maps to exactly one relation, so the directional confusion matrix between all type pairs is not directly comparable to the span-level confusion rates used for NER and ED. The BCS-controlled experiments (\\S\\ref{sec:bcs_controlled}) provide stronger, interventional evidence for the confusability effect on RE. Nevertheless, the signal is robust: both correlations survive bootstrap resampling with CIs bounded well above zero, and replicate across two unrelated embedding spaces (Qwen3 hidden states and MiniLM sentence embeddings).\n\nSpearman rank correlations from the SCS validation experiment (exp-015) corroborate these findings. Across all type pairs, Qwen3 yields $\\rho = 0.168$ ($p = 7.3 \\times 10^{-14}$) and MiniLM yields $\\rho = 0.144$ ($p = 1.7 \\times 10^{-10}$). Restricting to pairs with nonzero confusion strengthens the association: $\\rho = 0.272$ ($p = 5 \\times 10^{-5}$) for Qwen3 and $\\rho = 0.306$ ($p = 4.6 \\times 10^{-6}$) for MiniLM, indicating that among types the model actually confuses, embedding similarity is a stronger predictor.\n\nWe frame these results as identifying one factor among several that drive type confusion, but the first to be empirically isolated in a controlled zero-shot IE setting. Although pairwise $r^2$ is modest, the signal concentrates among types the model actually confuses ($\\rho = 0.27\\text{--}0.31$) and compounds at the batch level into accuracy gaps reaching 31.2\\,pp (\\S\\ref{sec:bcs_controlled}). Qwen3 yields stronger overall correlation ($\\rho = 0.168$ vs.\\ $0.144$), while MiniLM yields a stronger association among nonzero-confusion pairs ($\\rho = 0.306$ vs.\\ $0.272$); extraction-model embeddings are preferable when available.\n\n\\subsection{BCS-Controlled Experiments}\n\\label{sec:bcs_controlled}\n\nTo move from correlational to interventional evidence, we fix the type count and vary BCS. Table~\\ref{tab:bcs_controlled} reports FewRel accuracy under low-BCS and high-BCS batches at two schema sizes.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lcrrrr}\n\\toprule\n\\textbf{Schema} & \\textbf{Count} & \\textbf{Low-BCS} & \\textbf{High-BCS} & \\textbf{$\\Delta$ (pp)} & \\textbf{95\\% CI} \\\\\n\\midrule\n16-rel & 8 & 88.9\\% & 79.8\\% & $-$9.1 & --- \\\\\n80-rel & 8 & 82.3\\% & 51.0\\% & $-$31.2 & {[}17.7, 42.7{]} \\\\\n80-rel & 16 & 82.8\\% & 51.6\\% & $-$31.2 & {[}22.9, 39.6{]} \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{BCS-controlled FewRel accuracy. Low-BCS batches contain maximally dissimilar types; high-BCS batches contain maximally similar types. The confusability gap widens from 9.1\\,pp at 16 relations to 31.2\\,pp at 80 relations. The 16-relation condition used a single extreme batch per BCS level; bootstrap CIs require multiple batches.}\n\\label{tab:bcs_controlled}\n\\end{table}\n\nAt the 16-relation scale, switching from low-BCS to high-BCS batches reduces accuracy by 9.1 percentage points. Scaling to the full 80-relation pool amplifies this gap to 31.2\\,pp (95\\% CI: [17.7, 42.7])---a $3.4\\times$ amplification ($31.2 / 9.1$; range $1.9\\text{--}4.7\\times$ given the 80-rel CI). The effect is stable across count levels: at count${}\\,=\\,16$, the gap remains 31.2\\,pp (CI: [22.9, 39.6]). An intermediate evaluation at count${}\\,=\\,40$ (40-relation subsets sampled from the 80-relation pool) yields accuracy 0.588 and BCS gaps of $-$33.3\\,pp (count 8) and $-$31.8\\,pp (count 16), consistent with the 80-relation results and confirming monotonic decline within the pool.\n\nThis amplification has a natural interpretation. A larger type pool provides more opportunities for semantically similar types to co-occur, expanding the confusion space. BCS captures this expanded space: at 80 relations, extreme high-BCS batches pack tightly clustered types that the model cannot reliably distinguish, while the same count of well-separated types preserves near-solo-evaluation accuracy.\n\n\\paragraph{Cross-model validation.}\nThe confusability effect replicates on Meta-Llama-3.1-8B-Instruct: on FewRel, the BCS gap is $-$27.1\\,pp at count${}\\,=\\,8$ (low-BCS 78.1\\% vs.\\ high-BCS 51.0\\%) and $-$23.9\\,pp at count${}\\,=\\,16$ (75.5\\% vs.\\ 51.6\\%), reaching 77--87\\% of Qwen3-32B's $-$31.2\\,pp. Strikingly, high-BCS accuracy is model-invariant: both models converge to $\\approx$51\\% under high confusability (count${}\\,=\\,8$: 51.0\\% vs.\\ 51.0\\%; count${}\\,=\\,16$: 51.6\\% vs.\\ 51.6\\%), while cross-model divergence is confined to the low-BCS regime where model capacity matters. This pattern indicates that confusable type sets create a task-inherent difficulty floor independent of model scale.\n\n\\subsection{Multi-Channel Degradation}\n\\label{sec:multi_channel}\n\nWe now decompose extraction errors into an error taxonomy to distinguish the mechanisms behind performance loss. Table~\\ref{tab:error_taxonomy} quantifies how each error type scales with BCS.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llrrrrrrr}\n\\toprule\n & & \\multicolumn{5}{c}{\\textbf{BCS Bin}} & & \\\\\n\\cmidrule(lr){3-7}\n\\textbf{Task} & \\textbf{Error} & \\textbf{Solo} & \\textbf{Low} & \\textbf{Mid} & \\textbf{High} & \\textbf{V.High} & \\textbf{$\\rho$} & \\textbf{$p$} \\\\\n\\midrule\nNER & IntraSub & 0\\% & 1.6\\% & 10.6\\% & 49.4\\% & --- & 1.000 & ${<}0.001$ \\\\\nRE  & IntraSub & 0\\% & 4.2\\% & 13.0\\% & 20.3\\% & 32.3\\% & 0.954 & ${<}10^{-6}$ \\\\\n\\midrule\nNER & Missed & --- & 42.8\\% & 64.8\\% & 49.9\\% & --- & --- & --- \\\\\nRE  & Missed & --- & 10.4\\% & 11.3\\% & 13.1\\% & 15.7\\% & --- & --- \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Intra-batch substitution (IntraSub) and missed-entity rates by BCS bin, with Spearman $\\rho$ computed over $n=154$ individual batches (RE) and $n=148$ batches (NER). NER has 4 BCS bins; RE has 5. RE missed rates remain flat (10--16\\%), but NER missed rates are substantially higher (43--65\\%) and non-monotonic, revealing task-dependent error mechanisms.}\n\\label{tab:error_taxonomy}\n\\end{table}\n\nThree findings emerge. First, intra-batch substitution scales monotonically with BCS in both tasks: NER IntraSub rises from 0\\% (solo) to 49.4\\% (high BCS) with $\\rho = 1.0$ ($p < 0.001$), and RE IntraSub rises from 0\\% through 20.3\\% (high) to 32.3\\% (very high) with $\\rho = 0.954$ ($p < 10^{-6}$). Second, 100\\% of type confusion errors in RE are intra-batch---the model exclusively confuses types present in the current prompt, never hallucinating types outside the schema. Third, the tasks diverge on missed-entity rates: RE rates remain flat across BCS bins (10.4--15.7\\%), but NER rates are substantially higher (42.8--64.8\\%) and non-monotonic. This suggests that in span-level extraction, confusable type sets impair entity detection itself, not only type discrimination.\n\nThe extreme-batch analysis sharpens this picture. At count${}\\,=\\,6$, high-BCS batches produce $27.5\\times$ more confusion than low-BCS batches under extreme selection, versus $1.7\\times$ under random batching. At count${}\\,=\\,12$, the ratios are $9.9\\times$ (extreme) versus $2.4\\times$ (random). These multiplicative gaps confirm that BCS captures a functionally relevant dimension of schema difficulty, not merely a correlate.\n\nTaken together, these results establish two degradation channels: \\textbf{Channel~1} (count $\\to$ recall decline, \\S\\ref{sec:count_curves}) and \\textbf{Channel~2} (confusability $\\to$ type confusion, this section). In RE, the channels are cleanly separable---confusability drives substitution errors while detection remains stable. In NER, Channel~2 additionally impairs entity detection, suggesting that the two channels interact for span-level extraction tasks where type ambiguity and boundary ambiguity are coupled.\n\n\\subsection{Centrality Confound on Homogeneous Schemas}\n\\label{sec:centrality_confound}\n\nPer-type analysis on MAVEN reveals an anomaly: the correlation between mean BCS and per-type error rate is \\emph{positive}---Qwen3 $\\rho = +0.189$ ($p = 0.021$) and MiniLM $\\rho = +0.208$ ($p = 0.011$)---opposite to the negative direction predicted by the confusability hypothesis.\n\nThis reversal traces to a property of same-domain schemas documented by \\citet{cai-isotropy-clusters-2021}: when all types derive from a single ontology (here, FrameNet), their embeddings collapse into a single cluster in representation space. In this regime, a type's mean BCS conflates two distinct properties: (i)~confusability with neighbors, which should increase errors, and (ii)~centrality within the cluster, which correlates with being a well-represented, high-frequency type that LLMs extract reliably. The centrality signal dominates, flipping the aggregate correlation.\n\nCritically, the pairwise SCS--confusion correlation remains intact: MAVEN MiniLM pairwise $r = 0.129$ (CI: [0.104, 0.156], $p < 10^{-10}$), consistent with the values in Table~\\ref{tab:pairwise}. The problem lies in the aggregation step (mean BCS per type), not in the pairwise signal itself.\n\nFew-NERD, whose 66 types span 8 coarse categories across diverse domains, does not exhibit this confound. Its per-type correlation is $\\rho = -0.293$ ($p = 0.02$, $n = 63$), in the expected negative direction: types with higher mean confusability have higher error rates. The cross-domain schema spans multiple embedding clusters, breaking the centrality--confusability conflation.\n\nThis analysis carries a practical implication: mean BCS is a reliable predictor of schema difficulty only for cross-domain schemas. For same-domain schemas where types form a single semantic cluster, pairwise SCS should be used directly, or the centrality component must be factored out before aggregation.",
      "numLines": 123,
      "startLine": 1,
      "totalLines": 123
    }
  },
  "sourceToolAssistantUUID": "8e499ff3-4884-4137-92a8-e19f40e07adc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_reviewer_1_b5f154cf",
  "sessionId": "fac75791-ec7a-467d-a47d-5c20edb94374",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 32 · 2026-05-16T00:54:01.419Z_

<details open><summary>🔧 Tool call — Read · `toolu_01YChcELu7NG3pCqTYuyiUYB`</summary>

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
  "parentUuid": "f21ad4b6-77a5-499e-a796-2ed41313b659",
  "isSidechain": false,
  "requestId": "req_011Cb5LNDGVcfywho2MMd1a4",
  "type": "assistant",
  "uuid": "43a35be6-4ca3-4809-b91b-859d0d7d047f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_reviewer_1_b5f154cf",
  "sessionId": "fac75791-ec7a-467d-a47d-5c20edb94374",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012QXDoWJwahjZmSyGmkDdco",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 4013,
      "cache_creation_input_tokens": 1195,
      "cache_read_input_tokens": 27052,
      "output_tokens": 490,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1195,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 4013,
          "output_tokens": 490,
          "cache_read_input_tokens": 27052,
          "cache_creation_input_tokens": 1195,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1195
          },
          "type": "message"
        }
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

_source line 33 · 2026-05-16T00:54:01.424Z_

<details><summary>↩ Tool result · `toolu_01YChcELu7NG3pCqTYuyiUYB`</summary>

```text
1	\section{Why Naive Decomposition Fails}
2	\label{sec:sdgd}
3	
4	The multi-channel degradation model (\S\ref{sec:results}) raises an interventional question: if confusability drives type confusion, can we decompose the schema so that confusable types never co-occur in the same prompt?  We test this idea with \textbf{Schema-DAG-Guided Decomposition} (SDGD), a method that uses the pairwise SCS matrix to partition types into low-confusability batches, runs extraction independently on each batch, and merges the results.
5	
6	\paragraph{Decomposition protocol.}
7	We construct a thresholded confusability graph $G = (V, E)$ where each type is a vertex and an edge connects types $t_i, t_j$ whenever $\text{SCS}(t_i, t_j) > \tau$. Greedy graph coloring (\textsc{largest\_first}) assigns each type to a color such that no two adjacent---i.e., highly confusable---types share a color. Each color class forms one extraction batch, and predictions are merged via set union. We compare four modes: (i)~\textbf{single\_pass}, the undecomposed baseline; (ii)~\textbf{sdgd\_zero}, SCS-guided partitioning; (iii)~\textbf{random\_batch}, random partitioning with matched batch sizes; and (iv)~\textbf{per\_type}, the extreme case where each type is extracted in isolation, following the strategy of \citet{uniner-2024}. Table~\ref{tab:sdgd_results} summarizes the results on Few-NERD.
8	
9	\paragraph{All decomposition modes degrade F1.}
10	Table~\ref{tab:sdgd_results} reports the outcome.  Single-pass extraction achieves F1\,=\,0.445 (P\,=\,0.563, R\,=\,0.368).  SDGD obtains F1\,=\,0.251 (P\,=\,0.210, R\,=\,0.314), a 44\% relative drop.  Random batching reaches F1\,=\,0.320 (P\,=\,0.249, R\,=\,0.446), and per-type extraction yields F1\,=\,0.292 (P\,=\,0.194, R\,=\,0.586).  Every decomposition mode falls below the single-pass baseline.
11	
12	\begin{table}[t]
13	\centering
14	\small
15	\resizebox{\columnwidth}{!}{%
16	\begin{tabular}{lrccc}
17	\toprule
18	\textbf{Mode} & \textbf{\# Batches} & \textbf{Precision} & \textbf{Recall} & \textbf{F1} \\
19	\midrule
20	single\_pass & 1 & 0.563 & 0.368 & 0.445 \\
21	\midrule
22	sdgd\_zero (v1) & 8 & 0.210 & 0.314 & 0.251 \\
23	random\_batch (v1) & 8 & 0.249 & 0.446 & 0.320 \\
24	per\_type & 66 & 0.194 & 0.586 & 0.292 \\
25	\midrule
26	sdgd\_zero (v2) & 4 & 0.324 & 0.191 & 0.241 \\
27	random\_batch (v2) & 8 & 0.331 & 0.276 & 0.301 \\
28	\bottomrule
29	\end{tabular}}
30	\caption{Few-NERD extraction under decomposition modes.  V1 uses union merge; v2 uses confidence-gated merge with \texttt{min\_batch\_size=8} (reducing 8$\to$4 batches for sdgd\_zero).  All decomposition modes produce lower F1 than the single-pass baseline.  More batches amplify false positives through merge.}
31	\label{tab:sdgd_results}
32	\end{table}
33	
34	\paragraph{Merge amplification.}
35	The pattern across modes is consistent: decomposition boosts recall (per-type recall reaches 0.586 versus single-pass 0.368) but devastates precision (0.194 versus 0.563).  The mechanism is straightforward.  When the same text is presented to the model $k$ times with different type subsets, each pass independently generates entity predictions.  Because LLM outputs are not calibrated across passes, the union merge step accumulates overlapping and contradictory predictions, inflating false positives.  Smaller batches amplify the effect: per-type extraction runs the most passes and suffers the worst precision.  This \emph{merge amplification} is a structural consequence of decompose-then-merge pipelines, independent of how the decomposition is constructed.
36	
37	\paragraph{Confidence-gated merge does not help.}
38	A natural remedy is to resolve merge conflicts using model confidence.  Our v2 merge ranks competing predictions by the LLM's self-reported confidence and retains only the highest-scoring candidate for each span.  Confidence gating does improve precision (sdgd\_zero: 0.210$\to$0.324; random\_batch: 0.249$\to$0.331), but at the cost of disproportionate recall loss (0.314$\to$0.191; 0.446$\to$0.276), yielding lower F1 in both modes (sdgd\_zero: 0.251$\to$0.241; random\_batch: 0.320$\to$0.301).  The failure is consistent with prior findings that LLM confidence scores are poorly calibrated in generative IE settings \cite{llm-calibration-survey-2024}: poorly calibrated scores discard correct predictions as aggressively as false positives.
39	
40	\paragraph{Connection to prior work and implications.}
41	\citet{llm-pee-2025} independently proposed similarity-based partitioning for event extraction. Our negative result complements their work by identifying the merge step---not partitioning quality---as the bottleneck. SDGD successfully separates confusable types by construction, yet F1 still drops because merge amplification is independent of decomposition quality. This is a general limitation of decompose-then-merge pipelines: future approaches must address cross-batch calibration before decomposition can translate confusability signals into extraction gains.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "43a35be6-4ca3-4809-b91b-859d0d7d047f",
  "isSidechain": false,
  "promptId": "86262a68-8f08-4a31-bae8-2266d9a0e2fa",
  "type": "user",
  "uuid": "d16e84bb-6ce5-41f0-8bcf-32797749db55",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/sdgd_negative.tex",
      "content": "\\section{Why Naive Decomposition Fails}\n\\label{sec:sdgd}\n\nThe multi-channel degradation model (\\S\\ref{sec:results}) raises an interventional question: if confusability drives type confusion, can we decompose the schema so that confusable types never co-occur in the same prompt?  We test this idea with \\textbf{Schema-DAG-Guided Decomposition} (SDGD), a method that uses the pairwise SCS matrix to partition types into low-confusability batches, runs extraction independently on each batch, and merges the results.\n\n\\paragraph{Decomposition protocol.}\nWe construct a thresholded confusability graph $G = (V, E)$ where each type is a vertex and an edge connects types $t_i, t_j$ whenever $\\text{SCS}(t_i, t_j) > \\tau$. Greedy graph coloring (\\textsc{largest\\_first}) assigns each type to a color such that no two adjacent---i.e., highly confusable---types share a color. Each color class forms one extraction batch, and predictions are merged via set union. We compare four modes: (i)~\\textbf{single\\_pass}, the undecomposed baseline; (ii)~\\textbf{sdgd\\_zero}, SCS-guided partitioning; (iii)~\\textbf{random\\_batch}, random partitioning with matched batch sizes; and (iv)~\\textbf{per\\_type}, the extreme case where each type is extracted in isolation, following the strategy of \\citet{uniner-2024}. Table~\\ref{tab:sdgd_results} summarizes the results on Few-NERD.\n\n\\paragraph{All decomposition modes degrade F1.}\nTable~\\ref{tab:sdgd_results} reports the outcome.  Single-pass extraction achieves F1\\,=\\,0.445 (P\\,=\\,0.563, R\\,=\\,0.368).  SDGD obtains F1\\,=\\,0.251 (P\\,=\\,0.210, R\\,=\\,0.314), a 44\\% relative drop.  Random batching reaches F1\\,=\\,0.320 (P\\,=\\,0.249, R\\,=\\,0.446), and per-type extraction yields F1\\,=\\,0.292 (P\\,=\\,0.194, R\\,=\\,0.586).  Every decomposition mode falls below the single-pass baseline.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lrccc}\n\\toprule\n\\textbf{Mode} & \\textbf{\\# Batches} & \\textbf{Precision} & \\textbf{Recall} & \\textbf{F1} \\\\\n\\midrule\nsingle\\_pass & 1 & 0.563 & 0.368 & 0.445 \\\\\n\\midrule\nsdgd\\_zero (v1) & 8 & 0.210 & 0.314 & 0.251 \\\\\nrandom\\_batch (v1) & 8 & 0.249 & 0.446 & 0.320 \\\\\nper\\_type & 66 & 0.194 & 0.586 & 0.292 \\\\\n\\midrule\nsdgd\\_zero (v2) & 4 & 0.324 & 0.191 & 0.241 \\\\\nrandom\\_batch (v2) & 8 & 0.331 & 0.276 & 0.301 \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Few-NERD extraction under decomposition modes.  V1 uses union merge; v2 uses confidence-gated merge with \\texttt{min\\_batch\\_size=8} (reducing 8$\\to$4 batches for sdgd\\_zero).  All decomposition modes produce lower F1 than the single-pass baseline.  More batches amplify false positives through merge.}\n\\label{tab:sdgd_results}\n\\end{table}\n\n\\paragraph{Merge amplification.}\nThe pattern across modes is consistent: decomposition boosts recall (per-type recall reaches 0.586 versus single-pass 0.368) but devastates precision (0.194 versus 0.563).  The mechanism is straightforward.  When the same text is presented to the model $k$ times with different type subsets, each pass independently generates entity predictions.  Because LLM outputs are not calibrated across passes, the union merge step accumulates overlapping and contradictory predictions, inflating false positives.  Smaller batches amplify the effect: per-type extraction runs the most passes and suffers the worst precision.  This \\emph{merge amplification} is a structural consequence of decompose-then-merge pipelines, independent of how the decomposition is constructed.\n\n\\paragraph{Confidence-gated merge does not help.}\nA natural remedy is to resolve merge conflicts using model confidence.  Our v2 merge ranks competing predictions by the LLM's self-reported confidence and retains only the highest-scoring candidate for each span.  Confidence gating does improve precision (sdgd\\_zero: 0.210$\\to$0.324; random\\_batch: 0.249$\\to$0.331), but at the cost of disproportionate recall loss (0.314$\\to$0.191; 0.446$\\to$0.276), yielding lower F1 in both modes (sdgd\\_zero: 0.251$\\to$0.241; random\\_batch: 0.320$\\to$0.301).  The failure is consistent with prior findings that LLM confidence scores are poorly calibrated in generative IE settings \\cite{llm-calibration-survey-2024}: poorly calibrated scores discard correct predictions as aggressively as false positives.\n\n\\paragraph{Connection to prior work and implications.}\n\\citet{llm-pee-2025} independently proposed similarity-based partitioning for event extraction. Our negative result complements their work by identifying the merge step---not partitioning quality---as the bottleneck. SDGD successfully separates confusable types by construction, yet F1 still drops because merge amplification is independent of decomposition quality. This is a general limitation of decompose-then-merge pipelines: future approaches must address cross-batch calibration before decomposition can translate confusability signals into extraction gains.",
      "numLines": 41,
      "startLine": 1,
      "totalLines": 41
    }
  },
  "sourceToolAssistantUUID": "43a35be6-4ca3-4809-b91b-859d0d7d047f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_reviewer_1_b5f154cf",
  "sessionId": "fac75791-ec7a-467d-a47d-5c20edb94374",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 34 · 2026-05-16T00:54:02.447Z_

<details open><summary>🔧 Tool call — Read · `toolu_01MMJpUHAtL6g5fesVx582TR`</summary>

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
  "parentUuid": "d16e84bb-6ce5-41f0-8bcf-32797749db55",
  "isSidechain": false,
  "requestId": "req_011Cb5LNDGVcfywho2MMd1a4",
  "type": "assistant",
  "uuid": "019d5f01-5d36-47b1-83d2-89fa940f8771",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_reviewer_1_b5f154cf",
  "sessionId": "fac75791-ec7a-467d-a47d-5c20edb94374",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012QXDoWJwahjZmSyGmkDdco",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 4013,
      "cache_creation_input_tokens": 1195,
      "cache_read_input_tokens": 27052,
      "output_tokens": 490,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1195,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 4013,
          "output_tokens": 490,
          "cache_read_input_tokens": 27052,
          "cache_creation_input_tokens": 1195,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1195
          },
          "type": "message"
        }
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

_source line 35 · 2026-05-16T00:54:02.453Z_

<details><summary>↩ Tool result · `toolu_01MMJpUHAtL6g5fesVx582TR`</summary>

```text
1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	We isolated schema-induced degradation into count-driven recall decline and confusability-driven type confusion, showed these channels are separable in RE but interact in NER, and confirmed that both channels replicate across model families on RE (Meta-Llama-3.1-8B-Instruct: count $r = 0.725$, confusability $\Delta = -27$\,pp), with high-BCS accuracy converging to a model-invariant floor. We further identified a centrality confound on same-domain schemas and demonstrated that merge amplification is the bottleneck for decompose-then-merge pipelines. Cross-batch calibration or joint decoding is the key next step.
5	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "019d5f01-5d36-47b1-83d2-89fa940f8771",
  "isSidechain": false,
  "promptId": "86262a68-8f08-4a31-bae8-2266d9a0e2fa",
  "type": "user",
  "uuid": "46499232-d7a8-4458-b2dc-1d1970136e9c",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/discussion.tex",
      "content": "\\section{Conclusion}\n\\label{sec:conclusion}\n\nWe isolated schema-induced degradation into count-driven recall decline and confusability-driven type confusion, showed these channels are separable in RE but interact in NER, and confirmed that both channels replicate across model families on RE (Meta-Llama-3.1-8B-Instruct: count $r = 0.725$, confusability $\\Delta = -27$\\,pp), with high-BCS accuracy converging to a model-invariant floor. We further identified a centrality confound on same-domain schemas and demonstrated that merge amplification is the bottleneck for decompose-then-merge pipelines. Cross-batch calibration or joint decoding is the key next step.\n",
      "numLines": 5,
      "startLine": 1,
      "totalLines": 5
    }
  },
  "sourceToolAssistantUUID": "019d5f01-5d36-47b1-83d2-89fa940f8771",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_reviewer_1_b5f154cf",
  "sessionId": "fac75791-ec7a-467d-a47d-5c20edb94374",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 36 · 2026-05-16T00:54:02.886Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01FJSvHcYZVt6vdcQu1FpXC3`</summary>

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
  "parentUuid": "46499232-d7a8-4458-b2dc-1d1970136e9c",
  "isSidechain": false,
  "requestId": "req_011Cb5LNDGVcfywho2MMd1a4",
  "type": "assistant",
  "uuid": "ba974e50-1914-4a80-8d75-1b10a156ecda",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_reviewer_1_b5f154cf",
  "sessionId": "fac75791-ec7a-467d-a47d-5c20edb94374",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012QXDoWJwahjZmSyGmkDdco",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 4013,
      "cache_creation_input_tokens": 1195,
      "cache_read_input_tokens": 27052,
      "output_tokens": 490,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1195,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 4013,
          "output_tokens": 490,
          "cache_read_input_tokens": 27052,
          "cache_creation_input_tokens": 1195,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1195
          },
          "type": "message"
        }
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

_source line 37 · 2026-05-16T00:54:02.951Z_

```json
{
  "parentUuid": "3edb87b7-3dd8-4eb5-8bce-c16363ff668a",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "63ec3a44-8115-4660-a6d0-4d1c51ceadb4",
  "timestamp": "2026-05-16T00:54:02.951Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_reviewer_1_b5f154cf",
  "sessionId": "fac75791-ec7a-467d-a47d-5c20edb94374",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 38_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[Round 1 审稿请求]: ## Round 1 审稿任务 — Reviewer 1（方法严谨性）  **论文：** \"Does Type Confusability Drive Schema-Induced Degradation in Training-Free LLM Information Extraction?\" **Venue：** EMNLP 2026 Main Conferen…",
  "leafUuid": "63ec3a44-8115-4660-a6d0-4d1c51ceadb4",
  "sessionId": "fac75791-ec7a-467d-a47d-5c20edb94374"
}
```

---

### Runtime record

_source line 39_

```json
{
  "type": "ai-title",
  "aiTitle": "Review methodological rigor of schema extraction paper",
  "sessionId": "fac75791-ec7a-467d-a47d-5c20edb94374"
}
```

---

### Assistant

_source line 40 · 2026-05-16T00:54:05.959Z_

<details><summary>Logged reasoning block</summary>

```text
Now let me fetch the official ACL ARR review form to get the exact scoring criteria.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "63ec3a44-8115-4660-a6d0-4d1c51ceadb4",
  "isSidechain": false,
  "requestId": "req_011Cb5LNpgULReVPu6W7QZzG",
  "type": "assistant",
  "uuid": "1c8253e2-47d0-4ac9-aa17-a7e3194b81db",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_reviewer_1_b5f154cf",
  "sessionId": "fac75791-ec7a-467d-a47d-5c20edb94374",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TxGesv7Ynn7k37HdjeXUJQ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15887,
      "cache_read_input_tokens": 28247,
      "output_tokens": 176,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 15887,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 176,
          "cache_read_input_tokens": 28247,
          "cache_creation_input_tokens": 15887,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 15887
          },
          "type": "message"
        }
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

_source line 41 · 2026-05-16T00:54:06.449Z_

正在获取 ACL ARR 官方 review form 评分标准。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1c8253e2-47d0-4ac9-aa17-a7e3194b81db",
  "isSidechain": false,
  "requestId": "req_011Cb5LNpgULReVPu6W7QZzG",
  "type": "assistant",
  "uuid": "fd0bbe38-7a77-45d3-9824-2b5f797ca83f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_reviewer_1_b5f154cf",
  "sessionId": "fac75791-ec7a-467d-a47d-5c20edb94374",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TxGesv7Ynn7k37HdjeXUJQ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15887,
      "cache_read_input_tokens": 28247,
      "output_tokens": 176,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 15887,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 176,
          "cache_read_input_tokens": 28247,
          "cache_creation_input_tokens": 15887,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 15887
          },
          "type": "message"
        }
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

_source line 42 · 2026-05-16T00:54:08.422Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_016WZ4TmvLQmrRYAfKjBCPNd`</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract the complete review form criteria, scoring scales, and all dimensions that reviewers must evaluate. Include the exact scale descriptions for soundness, excitement, overall recommendation, and any other scored dimensions."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fd0bbe38-7a77-45d3-9824-2b5f797ca83f",
  "isSidechain": false,
  "requestId": "req_011Cb5LNpgULReVPu6W7QZzG",
  "type": "assistant",
  "uuid": "070f9d5f-e330-43e6-98dc-eba554ec277a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_reviewer_1_b5f154cf",
  "sessionId": "fac75791-ec7a-467d-a47d-5c20edb94374",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TxGesv7Ynn7k37HdjeXUJQ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15887,
      "cache_read_input_tokens": 28247,
      "output_tokens": 176,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 15887,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 176,
          "cache_read_input_tokens": 28247,
          "cache_creation_input_tokens": 15887,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 15887
          },
          "type": "message"
        }
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

_source line 43 · 2026-05-16T00:54:14.696Z_

<details><summary>↩ Tool result · `toolu_016WZ4TmvLQmrRYAfKjBCPNd`</summary>

```text
# ACL Rolling Review Form - Complete Evaluation Criteria

## Primary Scored Dimensions

### Reviewer Confidence
Scale 1-5, where:
- **5**: "Positive that my evaluation is correct. I read the paper very carefully and am familiar with related work."
- **4**: "Quite sure. I tried to check the important points carefully."
- **3**: "Pretty sure, but there's a chance I missed something."
- **2**: "Willing to defend my evaluation, but it is fairly likely that I missed some details."
- **1**: "Not my area, or paper is very hard to understand."

### Soundness
Scale 1-5 (with .5 increments):
- **5**: "This study is one of the most thorough I have seen, given its type."
- **4**: "This study provides sufficient support for all of its claims."
- **3**: "This study provides sufficient support for its main claims."
- **2**: "Some of the main claims are not sufficiently supported."
- **1**: "This study is not yet sufficiently thorough to warrant publication."

### Excitement
Scale 1-5 (with .5 increments):
- **5**: "I would recommend this paper to others and/or attend its presentation."
- **4**: "I would mention this paper to others and/or make an effort to attend."
- **3**: "I might mention some points of this paper to others."
- **2**: "Does not resonate with me, but it might with others."
- **1**: "Does not resonate with me, and I don't think it would with others."

### Overall Assessment
Scale 1-5 (with .5 increments):
- **5**: Consider for Award (top 2.5%)
- **4**: Conference acceptance
- **3**: Findings acceptance
- **2**: Resubmit next cycle
- **1**: Do not resubmit

## Additional Evaluation Sections

**Reproducibility** (1-5 scale), **Datasets** (1-5 scale), **Software** (1-5 scale), **Author Identity Knowledge** (1-5 scale), plus qualitative sections addressing limitations, ethical concerns, and ethics review necessity.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "070f9d5f-e330-43e6-98dc-eba554ec277a",
  "isSidechain": false,
  "promptId": "86262a68-8f08-4a31-bae8-2266d9a0e2fa",
  "type": "user",
  "uuid": "9475b9d6-0d25-4b61-a3de-689b4cbf7fb8",
  "toolUseResult": {
    "bytes": 25365,
    "code": 200,
    "codeText": "OK",
    "result": "# ACL Rolling Review Form - Complete Evaluation Criteria\n\n## Primary Scored Dimensions\n\n### Reviewer Confidence\nScale 1-5, where:\n- **5**: \"Positive that my evaluation is correct. I read the paper very carefully and am familiar with related work.\"\n- **4**: \"Quite sure. I tried to check the important points carefully.\"\n- **3**: \"Pretty sure, but there's a chance I missed something.\"\n- **2**: \"Willing to defend my evaluation, but it is fairly likely that I missed some details.\"\n- **1**: \"Not my area, or paper is very hard to understand.\"\n\n### Soundness\nScale 1-5 (with .5 increments):\n- **5**: \"This study is one of the most thorough I have seen, given its type.\"\n- **4**: \"This study provides sufficient support for all of its claims.\"\n- **3**: \"This study provides sufficient support for its main claims.\"\n- **2**: \"Some of the main claims are not sufficiently supported.\"\n- **1**: \"This study is not yet sufficiently thorough to warrant publication.\"\n\n### Excitement\nScale 1-5 (with .5 increments):\n- **5**: \"I would recommend this paper to others and/or attend its presentation.\"\n- **4**: \"I would mention this paper to others and/or make an effort to attend.\"\n- **3**: \"I might mention some points of this paper to others.\"\n- **2**: \"Does not resonate with me, but it might with others.\"\n- **1**: \"Does not resonate with me, and I don't think it would with others.\"\n\n### Overall Assessment\nScale 1-5 (with .5 increments):\n- **5**: Consider for Award (top 2.5%)\n- **4**: Conference acceptance\n- **3**: Findings acceptance\n- **2**: Resubmit next cycle\n- **1**: Do not resubmit\n\n## Additional Evaluation Sections\n\n**Reproducibility** (1-5 scale), **Datasets** (1-5 scale), **Software** (1-5 scale), **Author Identity Knowledge** (1-5 scale), plus qualitative sections addressing limitations, ethical concerns, and ethics review necessity.",
    "durationMs": 6268,
    "url": "https://aclrollingreview.org/reviewform"
  },
  "sourceToolAssistantUUID": "070f9d5f-e330-43e6-98dc-eba554ec277a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_reviewer_1_b5f154cf",
  "sessionId": "fac75791-ec7a-467d-a47d-5c20edb94374",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 44 · 2026-05-16T00:55:09.644Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the information needed. Let me compile a thorough review. Let me re-read key parts of the paper carefully to identify specific issues.

Key things I need to focus on as Reviewer 1 (methodological rigor):

1. **Experimental design & statistical methods**
2. **Evaluation metrics**
3. **Reproducibility**
4. **SDGD negative results**

Let me think through each:

### 1. Experimental Design & Statistical Methods

**Count curves:**
- 5 random batches per count level — is this enough? With 5 batches, variance could be high. 
- The count levels are non-uniform (e.g., {1, 2, 6, 12, 22, 44, 64} for Few-NERD) — justified as "natural partition points" but this makes interpolation questionable. I also need to verify whether confidence intervals are actually reported across these measurements.

**BCS-controlled experiments:**
- 27 batches per count level (1 low, 1 high, 25 random) is problematic because the extreme batches are single instances. At 16-rel, there's only one low-BCS and one high-BCS batch with no confidence intervals reported, which severely limits the statistical validity of those comparisons.

The 3.4× amplification claim (31.2/9.1) is comparing across different schema pools entirely — 16-rel versus 80-rel — so the type pools aren't matched. The 16-rel pool is just the validation split while 80-rel combines train and validation, which confounds the comparison. The baseline of 9.1pp has no confidence interval since it's based on a single batch, which undermines the strength of the amplification claim. Bootstrap confidence intervals are used appropriately elsewhere, but this gap at 16-rel is a real weakness.

The pairwise correlation of r=0.112 yields an r² of just 1.3%, which is a very small effect size despite the highly significant p-value — that significance is really driven by the large sample size of 1,953 pairs rather than a strong relationship. The restricted analysis conditioning on nonzero confusion pairs inflates the apparent strength artificially. On Few-NERD, the 2×2 factorial test for the interaction between count and BCS wasn't significant (z=-0.67, p=0.50), which contradicts the paper's claim about channel interactions for NER — this finding gets buried in the limitations rather than highlighted upfront.

For the sample sizes, NER and RE used 1,000 test instances which is reasonable, and MAVEN had 18,904 which is solid, but I'm wondering about the sampling procedure for that 1,000 — was there any sampling bias introduced?

On the evaluation metrics side, text-match F1 for NER is non-standard since the field typically uses exact span matching, and the fact that the model fabricates offsets 96.5% of the time means they had to resort to text matching anyway. This raises a fundamental question about whether the model is actually performing NER or just doing keyword extraction. For MAVEN, the relaxed F1 metric allowing any token overlap is quite lenient, and while the paper justifies it due to trigger boundary ambiguity, this leniency could be inflating the apparent performance.

The different metrics across tasks make it hard to compare results directly, which undermines the credibility of the "two-channel" framing since the evidence isn't really commensurable.

On reproducibility, there's a concerning inconsistency where the paper switches between v1 and v2 prompts — v1 was used for count curves and BCS-controlled NER, while v2 appears in later experiments and the appendix. Since v1 has the offset requirement that fails 96.5% of the time, it's unclear why that prompt was used at all rather than redoing everything with v2. The decoding parameters are solid though — temperature 0 and seed 42 provide good reproducibility.

The SDGD negative results section only tests two merge strategies (union and confidence-gated) when there are other approaches like majority voting and calibration-based methods that could address the claimed "structural" bottleneck. Plus, the evaluation is limited to Few-NERD alone, so it's hard to know if these findings generalize to other datasets like FewRel or MAVEN.

There's also an unfair comparison between v1 and v2 since they use different batch sizes. The embedding model choices are inconsistent across datasets—Qwen3-32B for Few-NERD but MiniLM for the others—without clear justification. Combining FewRel's training and validation splits is unconventional and could introduce distributional bias. Cross-model validation only covers Llama-3.1-8B, and even then the effect wasn't robustly detectable on Few-NERD NER. Interestingly, MAVEN actually shows results that contradict the main findings.

The two-channel model doesn't generalize well across all IE tasks and schemas—the paper attributes this to a "centrality confound," which suggests the framework has real limitations. Looking at the overall assessment: the core claims about the count and confusability channels are reasonably supported, but there are methodological concerns like using a single-batch baseline for the amplification analysis and conditioning on outcomes for pairwise comparisons. The factorial test wasn't significant either. The SDGD negative result deserves more investigation. The research question is timely and the controlled experimental design is genuinely novel, with the two-channel decomposition offering a useful lens. But the effect sizes are modest and the SDGD failure somewhat predictable. This feels like a borderline paper—strong conceptually with interesting methodology, though the empirical support has gaps.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9475b9d6-0d25-4b61-a3de-689b4cbf7fb8",
  "isSidechain": false,
  "requestId": "req_011Cb5LPgtgtp4BoYUFA8dhX",
  "type": "assistant",
  "uuid": "b63474b5-0c30-4cef-b84b-b6110aec2f10",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_reviewer_1_b5f154cf",
  "sessionId": "fac75791-ec7a-467d-a47d-5c20edb94374",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AEQykDTRM7Ai71PM1u9Wua",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 699,
      "cache_read_input_tokens": 44134,
      "output_tokens": 8379,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 699,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 8379,
          "cache_read_input_tokens": 44134,
          "cache_creation_input_tokens": 699,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 699
          },
          "type": "message"
        }
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

_source line 45 · 2026-05-16T00:56:48.151Z_

论文全文和 ARR review form 均已读完。现在撰写审稿报告。

---

## Review — Reviewer 1（方法严谨性）

### Summary

本文首次对 training-free LLM 信息抽取中的 schema-induced degradation 进行了受控实验分析，将性能退化分解为 count channel（类型数量→recall 下降）和 confusability channel（语义相似性→类型替换错误），并提出 SCS/BCS 指标量化 schema 混淆度。实验涵盖 NER/RE/ED 三个任务，辅以跨模型验证，最后通过 SDGD 实验给出 decompose-then-merge 失败的负面结果。研究问题有价值、实验设计新颖，但若干方法论问题削弱了核心 claim 的可靠性。

---

### Strengths

**S1.** 研究问题定义清晰且有实际意义。将 count 和 confusability 拆分为独立 channel 的思路是该领域的空白，实验设计（count curves + BCS-controlled）逻辑上互补，从 correlational 到 interventional 层层递进。

**S2.** Error taxonomy 分析（§5.4, Table 4）质量高。IntraSub 随 BCS 单调递增（RE: ρ=0.954）、RE 中 100% confusion 为 intra-batch 的发现清晰有力，为 Channel 2 提供了机制层面的证据。NER 与 RE 在 missed-entity pattern 上的分歧也被如实报告，体现了科学态度。

**S3.** Centrality confound 分析（§5.5）是对 BCS 指标局限性的坦诚自省，与 representation degeneration 文献的连接恰当（Cai et al., 2021; Godey et al., 2024）。这为后续研究提供了明确的方法论警示。

**S4.** 跨模型验证设计合理：选择了不同家族（Qwen vs. Llama）、不同规模（32B vs. 8B）的模型。High-BCS accuracy 在两个模型上收敛到 ≈51% 的 model-invariant floor 是一个有趣的发现。

**S5.** Limitations section 异常详尽，主动披露了 factorial 检验不显著（z=−0.67, p=0.50）、3.4× 为两点比较、NER 跨模型效应不可靠等问题。这种透明度值得肯定。

---

### Weaknesses

**W1 [Must-Fix] 3.4× amplification 的统计基础薄弱**

3.4× amplification（31.2pp / 9.1pp）是论文最突出的定量 claim（出现在 abstract、introduction、contributions、results），但存在两个严重问题：

(a) **基线无 CI**。16-rel 条件下 low-BCS 和 high-BCS 各只有 **1 个 batch**（Table 3 注释承认："The 16-relation condition used a single extreme batch per BCS level; bootstrap CIs require multiple batches"）。9.1pp 这个基线是单次观测，无法评估其不确定性。论文只对 80-rel 的 CI 做了传播（1.9–4.7×），但分母的方差被完全忽略。

(b) **跨 pool 比较引入混淆**。16-rel 来自 FewRel validation split（16 个 relation），80-rel 来自 train+val 合并的 80 个 relation。这两个 pool 的 type 组成完全不同，amplification 可能部分归因于 type pool 本身的差异（例如 80-rel pool 中本身包含更多高相似 pair），而非纯粹的 scale 效应。论文未讨论这一混淆。

**建议**：在 80-rel pool 内构造 16-type 子集的 BCS-controlled 实验（多个 low/high batch），获取与 80-rel 完全可比的 16-rel baseline 并附 CI。当前的 3.4× 应降格为描述性观察而非核心 contribution。

---

**W2 [Must-Fix] Pairwise SCS 效应量极小，framing 过度**

Pairwise r=0.112, r²=1.3%（Table 2）。论文将其定位为 "the first factor empirically isolated in controlled zero-shot IE"，但这个 framing 掩盖了实质：embedding similarity 仅解释 1.3% 的 confusion 方差，剩余 98.7% 由未知因素主导。

更关键的是，§5.2 中对 nonzero-confusion 子集的分析（ρ=0.27–0.31）存在 **conditioning on the outcome** 问题：剔除 confusion=0 的 pair 后再衡量预测力，这在统计上会人为抬高相关性，因为零值 pair 包含了大量 SCS 也低的"正确不混淆"数据。这不是 "the signal concentrates among types the model actually confuses"，而是一个选择偏差。

**建议**：(1) 明确承认 r²=1.3% 意味着 SCS 作为单一预测因子解释力有限；(2) 删除或重新框定 nonzero-confusion 子集分析，至少加上 conditioning bias 的讨论；(3) 考虑报告其他效应量指标（如 Cohen's f² 或分位数回归）。

---

**W3 [Must-Fix] NER 上 count×confusability 交互的证据不足**

论文在 §5.4 声称 NER 中 Channel 1 和 Channel 2 "interact"，但 Limitations 中披露的 2×2 factorial 检验不显著（z=−0.67, p=0.50）。这个交互声明缺乏统计支撑。论文将不显著归因于 "BCS range compression in high-count schemas"，但这只是事后假设，没有验证。

"在 RE 中可分离、在 NER 中交互"是论文的核心理论贡献之一（Contribution 1），如果 NER 交互不成立，multi-channel degradation model 的普遍性就大打折扣。

**建议**：要么提供更有力的交互证据（如更大样本、更宽 BCS 范围的 factorial 设计），要么将 NER 交互降级为 "suggestive but not statistically confirmed"。

---

**W4 [Should-Fix] SDGD 负面结果仅覆盖两种 merge 策略，overclaim "structural bottleneck"**

§6 仅测试了 union merge 和 confidence-gated merge 两种策略，就声称 merge amplification 是 "structural bottleneck" 和 "structural consequence of decompose-then-merge pipelines"。但文献中存在多种未测试的替代方案：span-level NMS、majority voting、calibration-based reranking（如 temperature scaling 后再 merge）、基于 mutual information 的跨 batch 去重。

此外，SDGD 仅在 Few-NERD 上测试。为什么不在 FewRel（最干净的 Channel 2 效应）或 MAVEN 上验证？单数据集 + 两种 merge 策略不足以支撑 "structural" 这个强修饰语。

**建议**：(1) 至少再测试 1–2 种 merge 策略（如 span-level NMS、calibration-adjusted merge）；(2) 在 FewRel 上复现 SDGD 实验；(3) 将 "structural bottleneck" 改为 "observed bottleneck under union and confidence-gated merge"。

---

**W5 [Should-Fix] v1/v2 prompt 切换引入实验内混淆**

论文在实验中使用了两个不同 prompt 版本：v1（含 offset 要求，模型在 96.5% 情况下 fabricate offset）用于 count curves 和 BCS-controlled NER；v2（无 offset，增加了 format constraints 和 role instructions，"doubling precision"）用于后续实验。Cross-model 比较中 Qwen3 用 v2 而 count curves 用 v1（Table 5 caption 确认）。

这意味着：(1) NER count curve 的绝对数值（recall 0.72→0.42）与后续实验不直接可比；(2) SDGD 实验的 single_pass baseline（F1=0.445，使用哪个 prompt？）与 count curve 结果对不上；(3) v1 prompt 让模型 fabricate offset 本身可能干扰抽取质量，使 v1 下的性能不能代表模型真实 NER 能力。

**建议**：统一使用 v2 prompt 重跑核心实验（至少 count curves），或至少提供 v1 vs v2 的对照消融，让读者理解 prompt 版本对结论的影响。

---

**W6 [Should-Fix] Embedding 模型不一致**

Few-NERD 的 SCS 用 Qwen3-32B hidden states（5120-d），FewRel 和 MAVEN 用 MiniLM（384-d）。Table 1 记录了这一差异但未充分论证原因。不同 embedding 空间的 BCS 值不可直接比较，这削弱了跨任务结论的一致性。§5.2 报告了两种 embedding 的 Spearman 相关差异（Qwen3 ρ=0.168 vs MiniLM ρ=0.144），但只在 Few-NERD 上做了交叉验证。

**建议**：在所有数据集上同时报告两种 embedding 的 SCS/BCS 结果，或论证为什么某些数据集只用一种 embedding。

---

**W7 [Should-Fix] FewRel 数据集构造可能引入偏差**

§4.1 说 FewRel validation split 仅 16 relations，因此合并 train+val 得到 80 relations 用于 schema-scale 实验。但 FewRel training split 的设计用途是 few-shot learning（每 relation 700 instances），validation split 的分布可能不同。合并后的 1,000 balanced instances 的抽样方式未说明——是从每个 relation 均匀采样，还是随机采样？这影响 accuracy 的解读。

---

**W8 [Minor] 完整 prompt 模板未提供**

§4.5 描述了 v1/v2 prompt 的设计差异但未给出完整模板。对于 zero-shot prompting 研究，prompt 的 exact wording 对结果影响极大。应在 appendix 中提供完整 prompt。

---

**W9 [Minor] MAVEN 结果实质上反驳了 count channel 的普遍性**

MAVEN F1 随 count 增加而 *上升*（0.106→0.247），与 NER/RE 趋势完全相反。虽然 §5.5 给出了合理解释（same-domain disambiguation），但这意味着 "Channel 1: count → recall decline" 不具有跨任务普遍性。Abstract 和 Introduction 对 count channel 的表述应更谨慎。

---

**W10 [Minor] 缺少与 supervised IE 系统的 baseline 对比**

论文专注 training-free setting，但缺少与 supervised 或 few-shot IE 系统（如 fine-tuned BERT/RoBERTa span extractors）的性能参照。这使得读者难以判断观测到的性能退化在多大程度上是 zero-shot paradigm 特有的问题。

---

### Questions for Authors

**Q1.** 3.4× amplification 的 16-rel baseline（9.1pp）来自单个 batch。如果在 80-rel pool 内抽取 16-type 子集做 BCS-controlled 实验，amplification 的估计值是否会改变？

**Q2.** Pairwise SCS 的 r²=1.3% 表明 SCS 的预测力有限。作者是否探索过多变量模型（如加入 type frequency、prompt position、type name length 等特征）来提升解释力？如果有，增量是多少？

**Q3.** 在 SDGD 实验中，single_pass baseline 使用的是 v1 还是 v2 prompt？如果与 count curve 实验的 prompt 版本不同，baseline 数值为何不一致？

**Q4.** NER cross-model validation 中效应 "not robustly detectable"（Limitations），这是否意味着 NER 上的 confusability channel 可能是 Qwen3 特有现象？作者如何排除这个可能性？

**Q5.** High-BCS accuracy 在两个模型上收敛到 ≈51%。这个 floor 是否接近随机猜测水平（对于 8-type batch 随机准确率=12.5%）？如果不是，floor 的来源是什么——是否部分 type pair 即使 high-BCS 仍可区分？

---

### Overall Assessment

**Soundness**: 3/5 — 主要 claim（两个 degradation channel 的存在）有足够支撑，但核心定量 claim（3.4× amplification）的统计基础薄弱（单 batch baseline、跨 pool 混淆），pairwise SCS 效应量极小且 framing 偏强，NER 交互声明缺乏统计支撑。

**Excitement**: 3.5/5 — 研究问题切中 training-free IE 的核心痛点，controlled experimental design 在该领域属于首创，centrality confound 分析有洞见。但效应量偏小、SDGD 负面结果的分析深度不足。

**Overall**: 3/5 (Findings acceptance) — 论文研究问题好、实验设计有新意、写作透明度高（Limitations 详尽），但 W1–W3 三个 Must-Fix 问题（amplification 统计基础、SCS 效应量 framing、NER 交互证据）需要实质性修正才能达到 Main Conference 接收标准。建议修改后以 Findings 投稿，或补充实验后提升到 Main Conference 水平。

**Confidence**: 4/5 — 我仔细阅读了全文并熟悉 zero-shot IE 和实验设计方法论。

---

将审稿报告提交给 Review Director。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b63474b5-0c30-4cef-b84b-b6110aec2f10",
  "isSidechain": false,
  "requestId": "req_011Cb5LPgtgtp4BoYUFA8dhX",
  "type": "assistant",
  "uuid": "78df4e83-e9d0-4011-8a77-7701a7524d39",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_reviewer_1_b5f154cf",
  "sessionId": "fac75791-ec7a-467d-a47d-5c20edb94374",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AEQykDTRM7Ai71PM1u9Wua",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 699,
      "cache_read_input_tokens": 44134,
      "output_tokens": 8379,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 699,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 8379,
          "cache_read_input_tokens": 44134,
          "cache_creation_input_tokens": 699,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 699
          },
          "type": "message"
        }
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

_source line 46 · 2026-05-16T00:57:22.228Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director · `toolu_017W3yFepKLpC1ze6R7TRE7s`</summary>

```json
{
  "text": "## Reviewer 1 — Round 1 审稿报告（方法严谨性）\n\n### Summary\n\n本文首次对 training-free LLM 信息抽取中的 schema-induced degradation 进行了受控实验分析，将性能退化分解为 count channel（类型数量→recall 下降）和 confusability channel（语义相似性→类型替换错误），并提出 SCS/BCS 指标量化 schema 混淆度。实验涵盖 NER/RE/ED 三个任务，辅以跨模型验证，最后通过 SDGD 实验给出 decompose-then-merge 失败的负面结果。研究问题有价值、实验设计新颖，但若干方法论问题削弱了核心 claim 的可靠性。\n\n---\n\n### Strengths\n\n**S1.** 研究问题定义清晰且有实际意义。将 count 和 confusability 拆分为独立 channel 的思路是该领域的空白，实验设计（count curves + BCS-controlled）逻辑上互补，从 correlational 到 interventional 层层递进。\n\n**S2.** Error taxonomy 分析（§5.4, Table 4）质量高。IntraSub 随 BCS 单调递增（RE: ρ=0.954）、RE 中 100% confusion 为 intra-batch 的发现清晰有力，为 Channel 2 提供了机制层面的证据。NER 与 RE 在 missed-entity pattern 上的分歧也被如实报告。\n\n**S3.** Centrality confound 分析（§5.5）是对 BCS 指标局限性的坦诚自省，与 representation degeneration 文献的连接恰当。\n\n**S4.** 跨模型验证设计合理：不同家族（Qwen vs. Llama）、不同规模（32B vs. 8B）。High-BCS accuracy 在两个模型上收敛到 ≈51% 的 model-invariant floor 是一个有趣的发现。\n\n**S5.** Limitations section 异常详尽，主动披露了 factorial 检验不显著（z=−0.67, p=0.50）、3.4× 为两点比较等问题。\n\n---\n\n### Weaknesses\n\n**W1 [Must-Fix] 3.4× amplification 的统计基础薄弱**\n\n3.4× amplification（31.2pp / 9.1pp）是论文最突出的定量 claim（出现在 abstract、introduction、contributions、results），但存在两个严重问题：\n\n(a) 基线无 CI。16-rel 条件下 low-BCS 和 high-BCS 各只有 1 个 batch（Table 3 注释确认）。9.1pp 基线是单次观测，无法评估不确定性。论文只对 80-rel CI 做了传播（1.9–4.7×），但分母方差被完全忽略。\n\n(b) 跨 pool 比较引入混淆。16-rel 来自 validation split，80-rel 来自 train+val 合并的 80 relations。type pool 组成完全不同，amplification 可能部分归因于 pool 差异而非 scale 效应。\n\n建议：在 80-rel pool 内构造 16-type 子集的 BCS-controlled 实验（多个 low/high batch），获取可比 baseline 并附 CI。当前 3.4× 应降格为描述性观察。\n\n**W2 [Must-Fix] Pairwise SCS 效应量极小，framing 过度**\n\nr=0.112, r²=1.3%（Table 2）。论文将其定位为 \"the first factor empirically isolated\"，掩盖了 embedding similarity 仅解释 1.3% confusion 方差的事实。§5.2 中 nonzero-confusion 子集分析（ρ=0.27–0.31）存在 conditioning on the outcome 问题——剔除 confusion=0 的 pair 人为抬高相关性。\n\n建议：明确承认解释力有限；删除或重新框定 nonzero-confusion 分析并讨论 conditioning bias。\n\n**W3 [Must-Fix] NER 上 count×confusability 交互的证据不足**\n\n§5.4 声称 NER 中两个 channel \"interact\"，但 Limitations 中的 2×2 factorial 检验不显著（z=−0.67, p=0.50）。这是 Contribution 1 的核心组成部分，缺乏统计支撑。\n\n建议：提供更有力的交互证据，或降级为 \"suggestive but not statistically confirmed\"。\n\n**W4 [Should-Fix] SDGD 负面结果仅覆盖两种 merge 策略，overclaim \"structural bottleneck\"**\n\n§6 仅测试 union merge 和 confidence-gated merge 就声称 \"structural bottleneck\"。未测试 span-level NMS、majority voting、calibration-based reranking 等替代方案。且仅在 Few-NERD 上测试，单数据集 + 两种策略不足以支撑 \"structural\" 修饰语。\n\n建议：测试更多 merge 策略，在 FewRel 上复现，或弱化表述。\n\n**W5 [Should-Fix] v1/v2 prompt 切换引入实验内混淆**\n\nv1（fabricate offset 96.5%）用于 count curves 和 BCS-controlled NER；v2 用于后续实验和跨模型比较。绝对数值跨实验不直接可比。\n\n建议：统一用 v2 重跑核心实验，或提供 v1/v2 对照消融。\n\n**W6 [Should-Fix] Embedding 模型不一致**\n\nFew-NERD 用 Qwen3-32B embeddings，FewRel/MAVEN 用 MiniLM。不同 embedding 空间的 BCS 不可直接比较，削弱跨任务一致性。\n\n**W7 [Should-Fix] FewRel 数据集构造可能引入偏差**\n\n合并 train+val splits 且未说明 1,000 balanced instances 的抽样方式。\n\n**W8 [Minor] 完整 prompt 模板未在 appendix 中提供，影响可复现性。\n\n**W9 [Minor] MAVEN 结果实质上反驳 count channel 的普遍性（F1 随 count 上升），abstract/introduction 表述应更谨慎。\n\n**W10 [Minor] 缺少与 supervised IE baseline 的参照。\n\n---\n\n### Questions\n\nQ1. 如果在 80-rel pool 内抽 16-type 子集做 BCS-controlled，amplification 估计值是否变化？\nQ2. 是否探索过多变量模型（加入 type frequency、prompt position 等）提升解释力？\nQ3. SDGD 的 single_pass baseline 用的是 v1 还是 v2 prompt？\nQ4. NER cross-model 效应 \"not robustly detectable\"，如何排除 confusability channel 为 Qwen3 特有？\nQ5. High-BCS ≈51% floor 的来源？是否接近随机猜测？\n\n---\n\n### Overall Assessment\n\n**Soundness**: 3/5\n**Excitement**: 3.5/5\n**Overall**: 3/5 (Findings acceptance)\n**Confidence**: 4/5\n\n论文研究问题好、实验设计有新意、写作透明度高，但 W1–W3 三个 Must-Fix 问题需要实质性修正才能达到 Main Conference 接收标准。建议修改后以 Findings 投稿，或补充实验后提升至 Main Conference 水平。",
  "reviewer_id": "1",
  "project": "schema-dag-extraction"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "78df4e83-e9d0-4011-8a77-7701a7524d39",
  "isSidechain": false,
  "requestId": "req_011Cb5LPgtgtp4BoYUFA8dhX",
  "type": "assistant",
  "uuid": "0dbd2ffc-c19f-40c1-b6e8-4d39a27abdc4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_reviewer_1_b5f154cf",
  "sessionId": "fac75791-ec7a-467d-a47d-5c20edb94374",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AEQykDTRM7Ai71PM1u9Wua",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 699,
      "cache_read_input_tokens": 44134,
      "output_tokens": 8379,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 699,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 8379,
          "cache_read_input_tokens": 44134,
          "cache_creation_input_tokens": 699,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 699
          },
          "type": "message"
        }
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
  "lastPrompt": "[Round 1 审稿请求]: ## Round 1 审稿任务 — Reviewer 1（方法严谨性）  **论文：** \"Does Type Confusability Drive Schema-Induced Degradation in Training-Free LLM Information Extraction?\" **Venue：** EMNLP 2026 Main Conferen…",
  "leafUuid": "0dbd2ffc-c19f-40c1-b6e8-4d39a27abdc4",
  "sessionId": "fac75791-ec7a-467d-a47d-5c20edb94374"
}
```

---

### Runtime record

_source line 48_

```json
{
  "type": "ai-title",
  "aiTitle": "Review methodological rigor of schema extraction paper",
  "sessionId": "fac75791-ec7a-467d-a47d-5c20edb94374"
}
```

---

### Tool result

_source line 49 · 2026-05-16T00:57:25.977Z_

<details><summary>↩ Tool result · `toolu_017W3yFepKLpC1ze6R7TRE7s`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director\"}, \"error\": \"\"}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0dbd2ffc-c19f-40c1-b6e8-4d39a27abdc4",
  "isSidechain": false,
  "promptId": "86262a68-8f08-4a31-bae8-2266d9a0e2fa",
  "type": "user",
  "uuid": "396e1a54-1299-4953-9ebb-ebd5a8a2edeb",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"review_director_key\\\": \\\"feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director\\\"}, \\\"error\\\": \\\"\\\"}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director\"}, \"error\": \"\"}"
    }
  },
  "sourceToolAssistantUUID": "0dbd2ffc-c19f-40c1-b6e8-4d39a27abdc4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_reviewer_1_b5f154cf",
  "sessionId": "fac75791-ec7a-467d-a47d-5c20edb94374",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---
