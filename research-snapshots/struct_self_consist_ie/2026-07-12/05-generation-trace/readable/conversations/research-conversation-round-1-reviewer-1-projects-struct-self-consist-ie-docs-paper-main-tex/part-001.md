# Research conversation: [Round 1 审稿请求]: 你是 Reviewer 1，负责**方法严谨性 + 实验设计**。 ## 审稿对象 - 论文路径：`projects/struct_self_consist_ie/docs/paper/main.tex`（分 — Part 1 of 5

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap (July export snapshot)** · Conversation logs

[Transcript overview](../research-conversation-round-1-reviewer-1-projects-struct-self-consist-ie-docs-paper-main-tex.md) · [Part 2 →](part-002.md) · [Structured JSON](../../../sessions/4a/4ad7dc6fcca93b52b6a4.json)

## Before a recorded user message

## Before a recorded user message

2 recorded events


### Runtime record

_source line 1 · 2026-05-15T03:57:30.669Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-15T03:57:30.669Z",
  "sessionId": "8e0e70e7-e72a-426a-9f89-26576a55a64e",
  "content": "[Round 1 审稿请求]:\n你是 Reviewer 1，负责**方法严谨性 + 实验设计**。\n\n## 审稿对象\n- 论文路径：`projects/struct_self_consist_ie/docs/paper/main.tex`（分节结构，各节在 `sections/` 下）\n- 目标 venue：**EMNLP 2026 Main Conference**（通过 ARR May 2026 cycle 提交）\n- 截止日期：2026-05-25\n- 格式：ACL 模板 `[review]`，长文 8 页正文，Limitations/Ethics 不计入页数，double-blind\n\n## 你的审查侧重\n\n### 1. 方法定义严谨性\n- 5 个 confidence signal（logprob, EM, FK, SJ, voting）的数学定义是否清晰、无歧义\n- Soft Jaccard 的 Hungarian matching + token-level IoU 定义是否完整（threshold? denominator 选择理由？）\n- Per-sample vs instance-level 信号的区分是否准确且一致\n- \"Correlation-selection gap\" 概念是否严格定义，还是仅为经验观察的命名\n\n### 2. 实验设计\n- 数据集选择（SciERC, CoNLL-2003, WNUT-17）是否覆盖足够的 difficulty gradient\n- N=8/16 的采样规模是否足够，是否需要更大 N 的实验\n- 两个模型（Qwen3-8B, LLaMA-3.1-8B）是否足以支撑跨模型结论\n- LoRA fine-tuning 设置是否公平（rank=32, α=64, 5 epochs）\n- 温度设置（T=0.7, T=1.0）是否充分\n\n### 3. 统计检验\n- Bootstrap resampling（B=10,000）的规范是否完整\n- p-value、CI、effect size 报告是否充分\n- 多重比较校正是否需要但缺失\n- \"no signal reliably surpasses greedy\" 的统计论证是否严谨\n\n### 4. 数据一致性\n- 表格数字与正文引用是否一致\n- 不同 section 对同一实验结果的描述是否矛盾\n- Figure 和 Table 的引用是否完整\n\n### 5. RE 单数据集问题\n- RE 结论仅基于 SciERC，论文是否对此做了充分的措辞限定\n- 44% zero-F1 对 RE 信号评估的影响是否充分讨论\n\n请输出标准审稿格式：Summary → Strengths → Weaknesses（分 Must-Fix / Should-Fix / Minor） → Questions → Missing References → Score (1-10) + Confidence (1-5)。"
}
```

---


### Runtime record

_source line 2 · 2026-05-15T03:57:30.673Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-15T03:57:30.673Z",
  "sessionId": "8e0e70e7-e72a-426a-9f89-26576a55a64e"
}
```

---


## Round 1

## Round 1

83 recorded events


### User

_source line 3 · 2026-05-15T03:57:30.720Z_

[Round 1 审稿请求]:
你是 Reviewer 1，负责**方法严谨性 + 实验设计**。

## 审稿对象
- 论文路径：`projects/struct_self_consist_ie/docs/paper/main.tex`（分节结构，各节在 `sections/` 下）
- 目标 venue：**EMNLP 2026 Main Conference**（通过 ARR May 2026 cycle 提交）
- 截止日期：2026-05-25
- 格式：ACL 模板 `[review]`，长文 8 页正文，Limitations/Ethics 不计入页数，double-blind

## 你的审查侧重

### 1. 方法定义严谨性
- 5 个 confidence signal（logprob, EM, FK, SJ, voting）的数学定义是否清晰、无歧义
- Soft Jaccard 的 Hungarian matching + token-level IoU 定义是否完整（threshold? denominator 选择理由？）
- Per-sample vs instance-level 信号的区分是否准确且一致
- "Correlation-selection gap" 概念是否严格定义，还是仅为经验观察的命名

### 2. 实验设计
- 数据集选择（SciERC, CoNLL-2003, WNUT-17）是否覆盖足够的 difficulty gradient
- N=8/16 的采样规模是否足够，是否需要更大 N 的实验
- 两个模型（Qwen3-8B, LLaMA-3.1-8B）是否足以支撑跨模型结论
- LoRA fine-tuning 设置是否公平（rank=32, α=64, 5 epochs）
- 温度设置（T=0.7, T=1.0）是否充分

### 3. 统计检验
- Bootstrap resampling（B=10,000）的规范是否完整
- p-value、CI、effect size 报告是否充分
- 多重比较校正是否需要但缺失
- "no signal reliably surpasses greedy" 的统计论证是否严谨

### 4. 数据一致性
- 表格数字与正文引用是否一致
- 不同 section 对同一实验结果的描述是否矛盾
- Figure 和 Table 的引用是否完整

### 5. RE 单数据集问题
- RE 结论仅基于 SciERC，论文是否对此做了充分的措辞限定
- 44% zero-F1 对 RE 信号评估的影响是否充分讨论

请输出标准审稿格式：Summary → Strengths → Weaknesses（分 Must-Fix / Should-Fix / Minor） → Questions → Missing References → Score (1-10) + Confidence (1-5)。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "06c85d14-4a07-4193-8916-587ad0c60656",
  "type": "user",
  "uuid": "b1e4edf7-f31c-4aee-a450-7d7acb684c99",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_1_68ddc296",
  "sessionId": "8e0e70e7-e72a-426a-9f89-26576a55a64e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Runtime record

_source line 4 · 2026-05-15T03:57:30.718Z_

```json
{
  "parentUuid": "b1e4edf7-f31c-4aee-a450-7d7acb684c99",
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
  "uuid": "c97b52ad-0363-4693-a48c-e9ac4acdeb31",
  "timestamp": "2026-05-15T03:57:30.718Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_1_68ddc296",
  "sessionId": "8e0e70e7-e72a-426a-9f89-26576a55a64e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---


### Runtime record

_source line 5 · 2026-05-15T03:57:30.718Z_

```json
{
  "parentUuid": "c97b52ad-0363-4693-a48c-e9ac4acdeb31",
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
  "uuid": "db5e96a6-e0ec-450a-90bd-66b5debd5254",
  "timestamp": "2026-05-15T03:57:30.718Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_1_68ddc296",
  "sessionId": "8e0e70e7-e72a-426a-9f89-26576a55a64e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---


### Runtime record

_source line 6 · 2026-05-15T03:57:30.718Z_

```json
{
  "parentUuid": "db5e96a6-e0ec-450a-90bd-66b5debd5254",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "3cea9ded-4205-4199-af69-c2571cc8de1f",
  "timestamp": "2026-05-15T03:57:30.718Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_1_68ddc296",
  "sessionId": "8e0e70e7-e72a-426a-9f89-26576a55a64e",
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
  "aiTitle": "Review paper on structural self-consistency for information extraction",
  "sessionId": "8e0e70e7-e72a-426a-9f89-26576a55a64e"
}
```

---


### Assistant

_source line 8 · 2026-05-15T03:57:53.851Z_

<details><summary>Logged reasoning block</summary>

```text
The user (Review Director) is asking me to perform a detailed review of a paper as Reviewer 1, focusing on methodological rigor and experimental design. Let me follow the instructions:

1. First, I need to do Step 0 - search for EMNLP 2026 / ACL ARR reviewer guidelines
2. Then read the paper using pdf_to_images or by reading the tex files
3. Provide a structured review

Let me start by:
1. Searching for the reviewer guidelines
2. Reading the paper (the tex file and its sections)

Since the paper is in LaTeX format at `projects/struct_self_consist_ie/docs/paper/main.tex` with sections in `sections/`, I need to use pdf_to_images for the PDF, or read the tex files. 

I'm noticing a mismatch here - the paper path is given as a .tex file, but the available reading channel is pdf_to_images for PDFs. Let me check if there's a compiled PDF version available or if I should read the LaTeX source files directly. I'm noticing a mismatch between the isolation rules that specify using pdf_to_images for papers and the fact that I've been given a .tex file path instead of a PDF. Let me check if there's a compiled PDF available at either the path in CLAUDE.md or the one the director mentioned, and if not, I'll need to read the .tex source directly since that's what's actually provided. I'm ready to begin the review process—let me search for the EMNLP guidelines and locate the paper files to get started.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3cea9ded-4205-4199-af69-c2571cc8de1f",
  "isSidechain": false,
  "requestId": "req_011Cb3gZLYgB11qU72swePrM",
  "type": "assistant",
  "uuid": "149924d6-88ea-46cc-ae70-b6c27784b7e1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_1_68ddc296",
  "sessionId": "8e0e70e7-e72a-426a-9f89-26576a55a64e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JRwx96o8Wgrjd6FwevEKsL",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13802,
      "cache_read_input_tokens": 11841,
      "output_tokens": 1177,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 13802,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1177,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 13802,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 13802
          },
          "type": "message"
        }
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

_source line 9 · 2026-05-15T03:57:54.138Z_

开始审稿。先并行搜索 ACL ARR reviewer guidelines 和定位论文文件。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "149924d6-88ea-46cc-ae70-b6c27784b7e1",
  "isSidechain": false,
  "requestId": "req_011Cb3gZLYgB11qU72swePrM",
  "type": "assistant",
  "uuid": "b79d1448-d961-4c66-8faf-29ddfb4483f4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_1_68ddc296",
  "sessionId": "8e0e70e7-e72a-426a-9f89-26576a55a64e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JRwx96o8Wgrjd6FwevEKsL",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13802,
      "cache_read_input_tokens": 11841,
      "output_tokens": 1177,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 13802,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1177,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 13802,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 13802
          },
          "type": "message"
        }
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

_source line 10 · 2026-05-15T03:57:55.546Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01CzwL7vyKgsiJXcLHBgnHAM`</summary>

```json
{
  "query": "select:WebSearch,mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__review_reviewer_post_to_director,mcp__agent-ml-research__verify_references",
  "max_results": 4
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b79d1448-d961-4c66-8faf-29ddfb4483f4",
  "isSidechain": false,
  "requestId": "req_011Cb3gZLYgB11qU72swePrM",
  "type": "assistant",
  "uuid": "2a289f3a-5252-404e-a979-bafd668b9410",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_1_68ddc296",
  "sessionId": "8e0e70e7-e72a-426a-9f89-26576a55a64e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JRwx96o8Wgrjd6FwevEKsL",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13802,
      "cache_read_input_tokens": 11841,
      "output_tokens": 1177,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 13802,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1177,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 13802,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 13802
          },
          "type": "message"
        }
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

_source line 11 · 2026-05-15T03:57:55.553Z_

<details><summary>↩ Tool result · `toolu_01CzwL7vyKgsiJXcLHBgnHAM`</summary>

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
  "parentUuid": "2a289f3a-5252-404e-a979-bafd668b9410",
  "isSidechain": false,
  "promptId": "06c85d14-4a07-4193-8916-587ad0c60656",
  "type": "user",
  "uuid": "b8c5a152-f711-4b50-9172-402787459394",
  "toolUseResult": {
    "matches": [
      "WebSearch",
      "mcp__agent-ml-research__pdf_to_images",
      "mcp__agent-ml-research__review_reviewer_post_to_director",
      "mcp__agent-ml-research__verify_references"
    ],
    "query": "select:WebSearch,mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__review_reviewer_post_to_director,mcp__agent-ml-research__verify_references",
    "total_deferred_tools": 23
  },
  "sourceToolAssistantUUID": "2a289f3a-5252-404e-a979-bafd668b9410",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_1_68ddc296",
  "sessionId": "8e0e70e7-e72a-426a-9f89-26576a55a64e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Assistant

_source line 12 · 2026-05-15T03:57:59.871Z_

<details><summary>Logged reasoning block</summary>

```text
Good, tools are loaded. Now let me:
1. Search for ACL ARR reviewer guidelines
2. Find the paper files (check both paths mentioned)
3. Look for a compiled PDF

Let me do these in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b8c5a152-f711-4b50-9172-402787459394",
  "isSidechain": false,
  "requestId": "req_011Cb3gbAx2DTiXDEABggsAX",
  "type": "assistant",
  "uuid": "12ac3d13-e708-4012-a0ac-e6704dc9bca6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_1_68ddc296",
  "sessionId": "8e0e70e7-e72a-426a-9f89-26576a55a64e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NqeSPht6qEUccqyqervstq",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2681,
      "cache_read_input_tokens": 25643,
      "output_tokens": 386,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2681,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 386,
          "cache_read_input_tokens": 25643,
          "cache_creation_input_tokens": 2681,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2681
          },
          "type": "message"
        }
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

_source line 13 · 2026-05-15T03:58:00.354Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01MbpK8yZfTyw6RdV2jih4Q1`</summary>

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
  "parentUuid": "12ac3d13-e708-4012-a0ac-e6704dc9bca6",
  "isSidechain": false,
  "requestId": "req_011Cb3gbAx2DTiXDEABggsAX",
  "type": "assistant",
  "uuid": "bdff710e-7b3e-454b-935b-435c33552063",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_1_68ddc296",
  "sessionId": "8e0e70e7-e72a-426a-9f89-26576a55a64e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NqeSPht6qEUccqyqervstq",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2681,
      "cache_read_input_tokens": 25643,
      "output_tokens": 386,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2681,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 386,
          "cache_read_input_tokens": 25643,
          "cache_creation_input_tokens": 2681,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2681
          },
          "type": "message"
        }
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

_source line 14 · 2026-05-15T03:58:02.353Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01BwRZy4ey1Q2SN5E8SSgS2j`</summary>

```json
{
  "pattern": "**/docs/paper/**",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bdff710e-7b3e-454b-935b-435c33552063",
  "isSidechain": false,
  "requestId": "req_011Cb3gbAx2DTiXDEABggsAX",
  "type": "assistant",
  "uuid": "43dfd278-8a39-4664-a547-c945543adddc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_1_68ddc296",
  "sessionId": "8e0e70e7-e72a-426a-9f89-26576a55a64e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NqeSPht6qEUccqyqervstq",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2681,
      "cache_read_input_tokens": 25643,
      "output_tokens": 386,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2681,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 386,
          "cache_read_input_tokens": 25643,
          "cache_creation_input_tokens": 2681,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2681
          },
          "type": "message"
        }
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

_source line 15 · 2026-05-15T03:58:03.551Z_

<details><summary>↩ Tool result · `toolu_01HqCYiYc4KBcuNYz5QWxe4Z`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/figures/paper/fig_overview.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/figures/paper/fig_selection_gap.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/exp010_selection_curves/figures/paper/fig_selection_curves.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/figures/paper/fig_signal_heatmap.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/figures/paper/fig_reliability.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/figures/paper/fig_selection_curves.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/figures/fig_overview.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/figures/fig_reliability.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/figures/fig_signal_heatmap.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/figures/fig_selection_gap.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/figures/fig_temperature_robustness.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/figures/fig_length_logprob_scatter.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.pdf
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5af83fb8-5dff-4f5c-8d6b-3773e50015aa",
  "isSidechain": false,
  "promptId": "06c85d14-4a07-4193-8916-587ad0c60656",
  "type": "user",
  "uuid": "d79fbe9d-e299-477d-916d-3a2012ddd75e",
  "toolUseResult": {
    "filenames": [
      "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/figures/paper/fig_overview.pdf",
      "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/figures/paper/fig_selection_gap.pdf",
      "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/exp010_selection_curves/figures/paper/fig_selection_curves.pdf",
      "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/figures/paper/fig_signal_heatmap.pdf",
      "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/figures/paper/fig_reliability.pdf",
      "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/figures/paper/fig_selection_curves.pdf",
      "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/figures/fig_overview.pdf",
      "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/figures/fig_reliability.pdf",
      "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/figures/fig_signal_heatmap.pdf",
      "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/figures/fig_selection_gap.pdf",
      "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/figures/fig_temperature_robustness.pdf",
      "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/figures/fig_length_logprob_scatter.pdf",
      "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.pdf"
    ],
    "durationMs": 27,
    "numFiles": 13,
    "truncated": false
  },
  "sourceToolAssistantUUID": "5af83fb8-5dff-4f5c-8d6b-3773e50015aa",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_1_68ddc296",
  "sessionId": "8e0e70e7-e72a-426a-9f89-26576a55a64e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Tool result

_source line 16 · 2026-05-15T03:58:02.396Z_

<details><summary>↩ Tool result · `toolu_01BwRZy4ey1Q2SN5E8SSgS2j`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/acl.sty
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/acl_natbib.bst
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/figures/fig_overview.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/figures/fig_reliability.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/figures/fig_signal_heatmap.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/figures/fig_selection_gap.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/figures/fig_temperature_robustness.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/references.bib
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/related_work.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/figures/fig_length_logprob_scatter.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/conclusion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/method.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/limitations.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/abstract.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/introduction.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.blg
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.bbl
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.aux
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.out
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.fls
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.log
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.fdb_latexmk
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "43dfd278-8a39-4664-a547-c945543adddc",
  "isSidechain": false,
  "promptId": "06c85d14-4a07-4193-8916-587ad0c60656",
  "type": "user",
  "uuid": "79f2c32a-8afc-44ee-9e92-72002b97e494",
  "toolUseResult": {
    "filenames": [
      "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/acl.sty",
      "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/acl_natbib.bst",
      "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/figures/fig_overview.pdf",
      "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/figures/fig_reliability.pdf",
      "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/figures/fig_signal_heatmap.pdf",
      "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/figures/fig_selection_gap.pdf",
      "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/figures/fig_temperature_robustness.pdf",
      "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/references.bib",
      "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/related_work.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/figures/fig_length_logprob_scatter.pdf",
      "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/conclusion.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/method.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/limitations.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/abstract.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/introduction.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.blg",
      "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.bbl",
      "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.aux",
      "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.out",
      "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.fls",
      "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.log",
      "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.pdf",
      "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.fdb_latexmk"
    ],
    "durationMs": 33,
    "numFiles": 27,
    "truncated": false
  },
  "sourceToolAssistantUUID": "43dfd278-8a39-4664-a547-c945543adddc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_1_68ddc296",
  "sessionId": "8e0e70e7-e72a-426a-9f89-26576a55a64e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Tool call

_source line 17 · 2026-05-15T03:58:03.364Z_

<details open><summary>🔧 Tool call — Glob · `toolu_013EqGQgeKr3qDtkTQ5eNJsz`</summary>

```json
{
  "pattern": "**/paper/**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "79f2c32a-8afc-44ee-9e92-72002b97e494",
  "isSidechain": false,
  "requestId": "req_011Cb3gbAx2DTiXDEABggsAX",
  "type": "assistant",
  "uuid": "46ed0a5b-02fa-425a-abf2-39e352bcb8b3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_1_68ddc296",
  "sessionId": "8e0e70e7-e72a-426a-9f89-26576a55a64e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NqeSPht6qEUccqyqervstq",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2681,
      "cache_read_input_tokens": 25643,
      "output_tokens": 386,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2681,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 386,
          "cache_read_input_tokens": 25643,
          "cache_creation_input_tokens": 2681,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2681
          },
          "type": "message"
        }
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

_source line 18 · 2026-05-15T03:58:03.394Z_

<details><summary>↩ Tool result · `toolu_013EqGQgeKr3qDtkTQ5eNJsz`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper/experiments.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper/introduction.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper/related_work.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper/discussion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper/abstract.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper/conclusion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper/limitations.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/related_work.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/conclusion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/method.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/limitations.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/abstract.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/introduction.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "46ed0a5b-02fa-425a-abf2-39e352bcb8b3",
  "isSidechain": false,
  "promptId": "06c85d14-4a07-4193-8916-587ad0c60656",
  "type": "user",
  "uuid": "488acce6-597a-4935-a88d-c06ac0c2d49d",
  "toolUseResult": {
    "filenames": [
      "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper/experiments.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper/introduction.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper/related_work.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper/discussion.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper/abstract.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper/conclusion.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper/limitations.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/related_work.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/conclusion.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/method.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/limitations.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/abstract.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/introduction.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex"
    ],
    "durationMs": 25,
    "numFiles": 17,
    "truncated": false
  },
  "sourceToolAssistantUUID": "46ed0a5b-02fa-425a-abf2-39e352bcb8b3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_1_68ddc296",
  "sessionId": "8e0e70e7-e72a-426a-9f89-26576a55a64e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Tool call

_source line 19 · 2026-05-15T03:58:03.520Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01HqCYiYc4KBcuNYz5QWxe4Z`</summary>

```json
{
  "pattern": "**/paper/**/*.pdf",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "488acce6-597a-4935-a88d-c06ac0c2d49d",
  "isSidechain": false,
  "requestId": "req_011Cb3gbAx2DTiXDEABggsAX",
  "type": "assistant",
  "uuid": "5af83fb8-5dff-4f5c-8d6b-3773e50015aa",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_1_68ddc296",
  "sessionId": "8e0e70e7-e72a-426a-9f89-26576a55a64e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NqeSPht6qEUccqyqervstq",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2681,
      "cache_read_input_tokens": 25643,
      "output_tokens": 386,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2681,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 386,
          "cache_read_input_tokens": 25643,
          "cache_creation_input_tokens": 2681,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2681
          },
          "type": "message"
        }
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
  "lastPrompt": "[Round 1 审稿请求]: 你是 Reviewer 1，负责**方法严谨性 + 实验设计**。  ## 审稿对象 - 论文路径：`projects/struct_self_consist_ie/docs/paper/main.tex`（分节结构，各节在 `sections/` 下） - 目标 venue：**EMNLP 2026 Main Conference**（通过 ARR May 202…",
  "leafUuid": "d79fbe9d-e299-477d-916d-3a2012ddd75e",
  "sessionId": "8e0e70e7-e72a-426a-9f89-26576a55a64e"
}
```

---


### Runtime record

_source line 21_

```json
{
  "type": "ai-title",
  "aiTitle": "Review paper on structural self-consistency for information extraction",
  "sessionId": "8e0e70e7-e72a-426a-9f89-26576a55a64e"
}
```

---


### Tool result

_source line 22 · 2026-05-15T03:58:07.414Z_

<details><summary>↩ Tool result · `toolu_01MbpK8yZfTyw6RdV2jih4Q1`</summary>

```text
Web search results for query: "ACL ARR 2026 reviewer guidelines review form criteria scoring"

Links: [{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"aclrollingreview/reviewing.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/reviewing.md"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"ACLRollingReview (@ReviewAcl) / Posts / X","url":"https://x.com/ReviewAcl"}]

Based on the search results, here's information about ACL ARR 2026 reviewer guidelines, review form criteria, and scoring:

## Review Scoring System

Starting with February 2025, ARR reviewers are asked to provide three scores: soundness, excitement, and overall recommendation. The soundness scores must be justified by the text of the review.

## Overall Recommendation Score

The "Consider for Award" score (5) indicates the reviewer thinks the paper could be considered for an outstanding paper award at an *ACL conference (up to top 2.5% papers). Other recommendation levels include "Resubmit next cycle" (2) for substantial revisions completable by the next ARR cycle, and "Resubmit after next cycle" (1.5) for revisions that cannot be completed by the next cycle.

## Review Criteria

The main criteria for Findings are soundness and reproducibility, while conference recommendations may also consider novelty, impact and other factors.

Excitement is assessed by asking "How exciting is this paper for you?" and excitement is subjective and does not necessarily follow what is popular in the field.

## Key Review Guidelines

The overall assessment score is an explicit recommendation for the outcome of the paper, reflecting the reviewer's assessment of soundness, excitement, and other factors like novelty and impact.

For more detailed information, you can visit the official ARR reviewer guidelines at http://aclrollingreview.org/reviewerguidelines and the review form at http://aclrollingreview.org/reviewform.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bdff710e-7b3e-454b-935b-435c33552063",
  "isSidechain": false,
  "promptId": "06c85d14-4a07-4193-8916-587ad0c60656",
  "type": "user",
  "uuid": "a055cc50-df7c-43d7-9ecf-f52aee30c12c",
  "toolUseResult": {
    "query": "ACL ARR 2026 reviewer guidelines review form criteria scoring",
    "results": [
      {
        "tool_use_id": "srvtoolu_017jeMQm1GVZGAgkx3UoSCfR",
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
            "title": "aclrollingreview/cfp.md at main · acl-org/aclrollingreview",
            "url": "https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"
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
            "title": "aclrollingreview/reviewing.md at main · acl-org/aclrollingreview",
            "url": "https://github.com/acl-org/aclrollingreview/blob/main/reviewing.md"
          },
          {
            "title": "ACL Rolling Review – A peer review platform for the Association for Computational Linguistics",
            "url": "http://aclrollingreview.org/"
          },
          {
            "title": "ACLRollingReview (@ReviewAcl) / Posts / X",
            "url": "https://x.com/ReviewAcl"
          }
        ]
      },
      "Based on the search results, here's information about ACL ARR 2026 reviewer guidelines, review form criteria, and scoring:\n\n## Review Scoring System\n\nStarting with February 2025, ARR reviewers are asked to provide three scores: soundness, excitement, and overall recommendation. The soundness scores must be justified by the text of the review.\n\n## Overall Recommendation Score\n\nThe \"Consider for Award\" score (5) indicates the reviewer thinks the paper could be considered for an outstanding paper award at an *ACL conference (up to top 2.5% papers). Other recommendation levels include \"Resubmit next cycle\" (2) for substantial revisions completable by the next ARR cycle, and \"Resubmit after next cycle\" (1.5) for revisions that cannot be completed by the next cycle.\n\n## Review Criteria\n\nThe main criteria for Findings are soundness and reproducibility, while conference recommendations may also consider novelty, impact and other factors.\n\nExcitement is assessed by asking \"How exciting is this paper for you?\" and excitement is subjective and does not necessarily follow what is popular in the field.\n\n## Key Review Guidelines\n\nThe overall assessment score is an explicit recommendation for the outcome of the paper, reflecting the reviewer's assessment of soundness, excitement, and other factors like novelty and impact.\n\nFor more detailed information, you can visit the official ARR reviewer guidelines at http://aclrollingreview.org/reviewerguidelines and the review form at http://aclrollingreview.org/reviewform."
    ],
    "durationSeconds": 7.054081485999999
  },
  "sourceToolAssistantUUID": "bdff710e-7b3e-454b-935b-435c33552063",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_1_68ddc296",
  "sessionId": "8e0e70e7-e72a-426a-9f89-26576a55a64e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Assistant

_source line 23 · 2026-05-15T03:58:21.369Z_

<details><summary>Logged reasoning block</summary>

```text
Found the paper. There's a compiled PDF at `/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.pdf`. Let me also fetch the ACL ARR review form details. Let me read the paper via pdf_to_images and also fetch the review form page.

Let me do:
1. Fetch the ACL ARR review form page for detailed scoring criteria
2. Convert the PDF to images to read the paper
3. Also read the .tex source files for detailed technical content verification

Actually, for a thorough technical review I need to read the source files carefully. 

I'll start by converting the PDF to images for the visual content, and since the director explicitly provided the .tex path, I can reference those files to verify specific numbers and formulas in tables. Let me pull the PDF images first.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a055cc50-df7c-43d7-9ecf-f52aee30c12c",
  "isSidechain": false,
  "requestId": "req_011Cb3gc3aYWLTeEvkB9d7Yd",
  "type": "assistant",
  "uuid": "5366585b-3f80-4bb5-8514-3b1dad61cd93",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_1_68ddc296",
  "sessionId": "8e0e70e7-e72a-426a-9f89-26576a55a64e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013dZ8fdZ7TADQ8PsD1Ndnse",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2426,
      "cache_creation_input_tokens": 1242,
      "cache_read_input_tokens": 28324,
      "output_tokens": 571,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1242,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2426,
          "output_tokens": 571,
          "cache_read_input_tokens": 28324,
          "cache_creation_input_tokens": 1242,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1242
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

_source line 24 · 2026-05-15T03:58:21.681Z_

找到编译好的 PDF。先获取 ARR review form 详细标准，同时渲染论文 PDF。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5366585b-3f80-4bb5-8514-3b1dad61cd93",
  "isSidechain": false,
  "requestId": "req_011Cb3gc3aYWLTeEvkB9d7Yd",
  "type": "assistant",
  "uuid": "db938d48-a462-4f42-87ee-2e973e491999",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_1_68ddc296",
  "sessionId": "8e0e70e7-e72a-426a-9f89-26576a55a64e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013dZ8fdZ7TADQ8PsD1Ndnse",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2426,
      "cache_creation_input_tokens": 1242,
      "cache_read_input_tokens": 28324,
      "output_tokens": 571,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1242,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2426,
          "output_tokens": 571,
          "cache_read_input_tokens": 28324,
          "cache_creation_input_tokens": 1242,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1242
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

_source line 25 · 2026-05-15T03:58:22.737Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_018i8ZibEPva3gWEWVLBrA5x`</summary>

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
  "parentUuid": "db938d48-a462-4f42-87ee-2e973e491999",
  "isSidechain": false,
  "requestId": "req_011Cb3gc3aYWLTeEvkB9d7Yd",
  "type": "assistant",
  "uuid": "aa300914-17ee-459a-9567-8840bdb386eb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_1_68ddc296",
  "sessionId": "8e0e70e7-e72a-426a-9f89-26576a55a64e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013dZ8fdZ7TADQ8PsD1Ndnse",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2426,
      "cache_creation_input_tokens": 1242,
      "cache_read_input_tokens": 28324,
      "output_tokens": 571,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1242,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2426,
          "output_tokens": 571,
          "cache_read_input_tokens": 28324,
          "cache_creation_input_tokens": 1242,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1242
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

_source line 26 · 2026-05-15T03:58:22.742Z_

<details><summary>↩ Tool result · `toolu_018i8ZibEPva3gWEWVLBrA5x`</summary>

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
  "parentUuid": "aa300914-17ee-459a-9567-8840bdb386eb",
  "isSidechain": false,
  "promptId": "06c85d14-4a07-4193-8916-587ad0c60656",
  "type": "user",
  "uuid": "eba118af-7d3c-446c-950c-d6f2bd9398e3",
  "toolUseResult": {
    "matches": [
      "WebFetch"
    ],
    "query": "select:WebFetch",
    "total_deferred_tools": 23
  },
  "sourceToolAssistantUUID": "aa300914-17ee-459a-9567-8840bdb386eb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_1_68ddc296",
  "sessionId": "8e0e70e7-e72a-426a-9f89-26576a55a64e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Tool call

_source line 27 · 2026-05-15T03:58:23.452Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images · `toolu_013v3ChpCVdJXShjwJGDQtL5`</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.pdf",
  "pages": "1-10",
  "dpi": 200
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "eba118af-7d3c-446c-950c-d6f2bd9398e3",
  "isSidechain": false,
  "requestId": "req_011Cb3gc3aYWLTeEvkB9d7Yd",
  "type": "assistant",
  "uuid": "74a20be0-00d1-4062-b1c8-c93ae92b88cb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_1_68ddc296",
  "sessionId": "8e0e70e7-e72a-426a-9f89-26576a55a64e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013dZ8fdZ7TADQ8PsD1Ndnse",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2426,
      "cache_creation_input_tokens": 1242,
      "cache_read_input_tokens": 28324,
      "output_tokens": 571,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1242,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2426,
          "output_tokens": 571,
          "cache_read_input_tokens": 28324,
          "cache_creation_input_tokens": 1242,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1242
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

_source line 28 · 2026-05-15T03:58:27.502Z_

<details><summary>↩ Tool result · `toolu_013v3ChpCVdJXShjwJGDQtL5`</summary>

```text
Error: result (8,755,474 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie--claude-sessions-review-reviewer-1-68ddc296/8e0e70e7-e72a-426a-9f89-26576a55a64e/tool-results/mcp-agent-ml-research-pdf_to_images-1778817507485.txt.
Format: JSON with schema: {result: string}
- For targeted queries (find a value, filter by field): use jq on the file directly.
- For analysis or summarization that requires reading the full content: first probe the structure (e.g., jq 'type, length, keys?' /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie--claude-sessions-review-reviewer-1-68ddc296/8e0e70e7-e72a-426a-9f89-26576a55a64e/tool-results/mcp-agent-ml-research-pdf_to_images-1778817507485.txt), then extract slices with jq or python — Read's line-based offset/limit will not chunk this file.
- If the Agent tool is available, do this inside a subagent so the full output stays out of your main context. Give it the instruction above verbatim, and be explicit about what it must return — e.g. "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie--claude-sessions-review-reviewer-1-68ddc296/8e0e70e7-e72a-426a-9f89-26576a55a64e/tool-results/mcp-agent-ml-research-pdf_to_images-1778817507485.txt is JSON with schema: {result: string}; probe the structure with jq (type/length/keys), then extract and read the content in full with jq or python, then summarize and quote any key findings verbatim." A vague "summarize this" may lose detail.

```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "74a20be0-00d1-4062-b1c8-c93ae92b88cb",
  "isSidechain": false,
  "promptId": "06c85d14-4a07-4193-8916-587ad0c60656",
  "type": "user",
  "uuid": "0f8cc45b-5906-4c97-8289-5838a9dc95e5",
  "toolUseResult": "Error: result (8,755,474 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie--claude-sessions-review-reviewer-1-68ddc296/8e0e70e7-e72a-426a-9f89-26576a55a64e/tool-results/mcp-agent-ml-research-pdf_to_images-1778817507485.txt.\nFormat: JSON with schema: {result: string}\n- For targeted queries (find a value, filter by field): use jq on the file directly.\n- For analysis or summarization that requires reading the full content: first probe the structure (e.g., jq 'type, length, keys?' /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie--claude-sessions-review-reviewer-1-68ddc296/8e0e70e7-e72a-426a-9f89-26576a55a64e/tool-results/mcp-agent-ml-research-pdf_to_images-1778817507485.txt), then extract slices with jq or python — Read's line-based offset/limit will not chunk this file.\n- If the Agent tool is available, do this inside a subagent so the full output stays out of your main context. Give it the instruction above verbatim, and be explicit about what it must return — e.g. \"/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie--claude-sessions-review-reviewer-1-68ddc296/8e0e70e7-e72a-426a-9f89-26576a55a64e/tool-results/mcp-agent-ml-research-pdf_to_images-1778817507485.txt is JSON with schema: {result: string}; probe the structure with jq (type/length/keys), then extract and read the content in full with jq or python, then summarize and quote any key findings verbatim.\" A vague \"summarize this\" may lose detail.\n",
  "mcpMeta": {
    "storage": "sanitized-trace-archive",
    "source_line": 28,
    "serialized_bytes": 8755511,
    "serialized_sha256": "1582c3379ba0931424c96b7ed6fa5ad4a0cf850485097c5fc778ea2d5833814c",
    "note": "Complete sanitized source is retained in trace-files.tar.gz."
  },
  "sourceToolAssistantUUID": "74a20be0-00d1-4062-b1c8-c93ae92b88cb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_1_68ddc296",
  "sessionId": "8e0e70e7-e72a-426a-9f89-26576a55a64e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Runtime record

_source line 29_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[Round 1 审稿请求]: 你是 Reviewer 1，负责**方法严谨性 + 实验设计**。  ## 审稿对象 - 论文路径：`projects/struct_self_consist_ie/docs/paper/main.tex`（分节结构，各节在 `sections/` 下） - 目标 venue：**EMNLP 2026 Main Conference**（通过 ARR May 202…",
  "leafUuid": "0f8cc45b-5906-4c97-8289-5838a9dc95e5",
  "sessionId": "8e0e70e7-e72a-426a-9f89-26576a55a64e"
}
```

---


### Runtime record

_source line 30_

```json
{
  "type": "ai-title",
  "aiTitle": "Review paper on structural self-consistency for information extraction",
  "sessionId": "8e0e70e7-e72a-426a-9f89-26576a55a64e"
}
```

---


### Assistant

_source line 31 · 2026-05-15T03:58:32.242Z_

<details><summary>Logged reasoning block</summary>

```text
The PDF images were too large to return directly. Let me fetch the ARR review form and read the tex source files instead. I'll read the paper section by section from the .tex files, which is more practical for a detailed technical review.

Let me:
1. Fetch the ARR review form
2. Read the main.tex and all section files in parallel
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0f8cc45b-5906-4c97-8289-5838a9dc95e5",
  "isSidechain": false,
  "requestId": "req_011Cb3gdXhzyZheeXCfNSoDT",
  "type": "assistant",
  "uuid": "44d3c125-6f79-4bf6-9f4f-c8d1381c302e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_1_68ddc296",
  "sessionId": "8e0e70e7-e72a-426a-9f89-26576a55a64e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GTPM78Kk95tE4jx4dyGEHe",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 4126,
      "cache_read_input_tokens": 29566,
      "output_tokens": 571,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4126,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 571,
          "cache_read_input_tokens": 29566,
          "cache_creation_input_tokens": 4126,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4126
          },
          "type": "message"
        }
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

_source line 32 · 2026-05-15T03:58:33.654Z_

PDF 太大无法直接返回。改为逐节读取 .tex 源文件进行技术审查，同时获取 ARR review form。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "44d3c125-6f79-4bf6-9f4f-c8d1381c302e",
  "isSidechain": false,
  "requestId": "req_011Cb3gdXhzyZheeXCfNSoDT",
  "type": "assistant",
  "uuid": "b4decf82-b929-4332-a653-05f3d45b1617",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_1_68ddc296",
  "sessionId": "8e0e70e7-e72a-426a-9f89-26576a55a64e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GTPM78Kk95tE4jx4dyGEHe",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 4126,
      "cache_read_input_tokens": 29566,
      "output_tokens": 571,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4126,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 571,
          "cache_read_input_tokens": 29566,
          "cache_creation_input_tokens": 4126,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4126
          },
          "type": "message"
        }
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

_source line 33 · 2026-05-15T03:58:36.700Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01PkTG1FyKkfJ9X2CqSus8Dp`</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract the complete ACL ARR review form: all scoring dimensions, their scales (1-5, 1-10, etc.), descriptions for each score level, and any required fields. I need the exact scoring criteria for soundness, excitement, overall assessment, confidence, and any other dimensions."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b4decf82-b929-4332-a653-05f3d45b1617",
  "isSidechain": false,
  "requestId": "req_011Cb3gdXhzyZheeXCfNSoDT",
  "type": "assistant",
  "uuid": "68b15818-6b4f-450f-bcc7-69c399ddc271",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_1_68ddc296",
  "sessionId": "8e0e70e7-e72a-426a-9f89-26576a55a64e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GTPM78Kk95tE4jx4dyGEHe",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 4126,
      "cache_read_input_tokens": 29566,
      "output_tokens": 571,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4126,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 571,
          "cache_read_input_tokens": 29566,
          "cache_creation_input_tokens": 4126,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4126
          },
          "type": "message"
        }
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

_source line 34 · 2026-05-15T03:58:39.070Z_

<details><summary>↩ Tool result · `toolu_01HcVS93yfs4NX2Ki8haF2tK`</summary>

```text
1	\section{Method}\label{sec:method}
2	
3	\subsection{Problem Formulation}\label{sec:formulation}
4	
5	Given a language model $\mathcal{M}$ and input $x$, we sample $N$ structured outputs $\{y_1, \ldots, y_N\}$ at temperature $T > 0$ via constrained decoding \cite{willard2023guided}.
6	Each $y_i$ is an entity set (NER) or relation set (RE).
7	A confidence signal $c$ serves two purposes: (a) \textit{quality estimation}---predicting which instances the model handles reliably, and (b) \textit{sample selection}---identifying the best output among $N$ candidates.
8	
9	A \textbf{per-sample signal} scores each $y_i$ independently, $c_{\text{ps}}: (x, y_i) \to \mathbb{R}$, enabling direct candidate ranking.
10	An \textbf{instance-level signal} aggregates over all $N$ samples, $c_{\text{il}}: (x, \{y_i\}_{i=1}^N) \to \mathbb{R}$, producing a single score per input.
11	This asymmetry---between predicting \textit{which inputs} are easy and selecting \textit{which output} is best---is central to the correlation-selection gap we investigate.
12	Notation is summarized in Appendix~\ref{app:notation}.
13	
14	\subsection{Confidence Signals}\label{sec:signals}
15	
16	We compare five signals from three families: \textit{model-internal} (log-probability), \textit{surface} (exact match, Fleiss' $\kappa$), and \textit{structural} (Soft Jaccard, entity voting).
17	
18	\paragraph{Log-probability (model-internal, per-sample).}
19	The only per-sample signal.
20	For sample $y_i$ with tokens $t_1, \ldots, t_{|y_i|}$:
21	\begin{equation}\label{eq:logprob}
22	c_{\text{lp}}(y_i) = \frac{1}{|y_i|} \sum_{j=1}^{|y_i|} \log p_{\mathcal{M}}(t_j \mid t_{<j}, x)
23	\end{equation}
24	
25	\paragraph{Exact match voting (surface, instance-level).}
26	The majority fraction---the proportion of samples producing the most common output:
27	\begin{equation}\label{eq:em}
28	c_{\text{em}}(x) = \frac{1}{N} \max_{y} \big|\{i : y_i = y\}\big|
29	\end{equation}
30	
31	\paragraph{Fleiss' $\kappa$ (surface, instance-level).}
32	We adapt \citet{fleiss1971agreement} to entity sets: items are unique (text, type) tuples across all $N$ samples; each sample assigns binary present/absent labels, yielding a $|E_\cup| \times 2$ rating matrix:
33	\begin{equation}\label{eq:fk}
34	\kappa = \frac{\bar{P} - \bar{P}_e}{1 - \bar{P}_e}
35	\end{equation}
36	where $\bar{P}$ is mean observed pairwise agreement and $\bar{P}_e$ is expected agreement under random assignment.
37	While FK assumes independent raters, temperature-based sampling provides sufficient response diversity for the statistic to capture inter-sample agreement patterns.
38	Unlike structural signals, FK relies on exact string matching and does not tolerate surface variations.
39	
40	\paragraph{Soft Jaccard (structural, instance-level).}
41	Our core structural signal extends Jaccard similarity \cite{jaccard1901distribution} to extracted entity/relation sets.
42	For samples $y_i, y_j$, we group extractions by type, compute bipartite matching via the Hungarian algorithm with span overlap, and define:
43	\begin{equation}\label{eq:sj}
44	\text{SJ}(y_i, y_j) = \frac{\sum_{m \in M} \text{sim}(a_m, b_m)}{\sum_{g} \max(|g_i|, |g_j|)}
45	\end{equation}
46	where $M$ is the matched set from the Hungarian algorithm (without minimum similarity threshold), $\text{sim}(a_m, b_m)$ is the token-level IoU (intersection of tokens divided by union of tokens) between matched entity spans $a_m$ and $b_m$, and $g_i, g_j$ index per-type extraction counts.
47	We use $\max(|g_i|, |g_j|)$ rather than $|g_i \cup g_j|$ as the normalizer to penalize length asymmetry between samples.
48	The instance-level signal averages over all pairs:
49	\begin{equation}\label{eq:sj_instance}
50	c_{\text{sj}}(x) = \frac{1}{\binom{N}{2}} \sum_{i<j} \text{SJ}(y_i, y_j)
51	\end{equation}
52	
53	\paragraph{Entity voting confidence (structural, instance-level).}
54	For each entity $e$ in the union $E_\cup$ of all samples, we compute frequency $\text{freq}(e) = |\{i : e \in y_i\}| / N$.
55	The instance-level confidence is the mean frequency:
56	\begin{equation}\label{eq:voting}
57	c_{\text{vote}}(x) = \frac{1}{|E_\cup|} \sum_{e \in E_\cup} \text{freq}(e)
58	\end{equation}
59	
60	\subsection{Evaluation Framework}\label{sec:evaluation}
61	
62	\paragraph{Quality estimation.}
63	We measure rank correlation (Spearman $\rho$) between the confidence signal and instance-level F1, and binary discrimination (AUROC) by classifying instances as above or below median F1.
64	
65	\paragraph{Sample selection.}
66	We report best-of-$N$ F1: for each instance, the signal selects one sample.
67	Per-sample signals (logprob) directly rank candidates; instance-level signals select the sample closest to the consensus output (the consensus-proximity score for SJ is mathematically equivalent to leave-one-out SJ selection).
68	We compare against an \textit{oracle} (highest-F1 sample) and \textit{greedy} ($T{=}0$, $N{=}1$).
69	
70	\paragraph{Complementarity.}
71	High rank correlation does not guarantee effective sample selection: if per-sample variance is low, even a perfect quality estimator cannot distinguish among near-identical candidates (\S\ref{sec:selection_gap}).
72	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "29084bd3-0f9d-45cf-8ee2-779fd197c784",
  "isSidechain": false,
  "promptId": "06c85d14-4a07-4193-8916-587ad0c60656",
  "type": "user",
  "uuid": "17bf66ef-8b9e-4e9b-a1cb-419c835913f8",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/method.tex",
      "content": "\\section{Method}\\label{sec:method}\n\n\\subsection{Problem Formulation}\\label{sec:formulation}\n\nGiven a language model $\\mathcal{M}$ and input $x$, we sample $N$ structured outputs $\\{y_1, \\ldots, y_N\\}$ at temperature $T > 0$ via constrained decoding \\cite{willard2023guided}.\nEach $y_i$ is an entity set (NER) or relation set (RE).\nA confidence signal $c$ serves two purposes: (a) \\textit{quality estimation}---predicting which instances the model handles reliably, and (b) \\textit{sample selection}---identifying the best output among $N$ candidates.\n\nA \\textbf{per-sample signal} scores each $y_i$ independently, $c_{\\text{ps}}: (x, y_i) \\to \\mathbb{R}$, enabling direct candidate ranking.\nAn \\textbf{instance-level signal} aggregates over all $N$ samples, $c_{\\text{il}}: (x, \\{y_i\\}_{i=1}^N) \\to \\mathbb{R}$, producing a single score per input.\nThis asymmetry---between predicting \\textit{which inputs} are easy and selecting \\textit{which output} is best---is central to the correlation-selection gap we investigate.\nNotation is summarized in Appendix~\\ref{app:notation}.\n\n\\subsection{Confidence Signals}\\label{sec:signals}\n\nWe compare five signals from three families: \\textit{model-internal} (log-probability), \\textit{surface} (exact match, Fleiss' $\\kappa$), and \\textit{structural} (Soft Jaccard, entity voting).\n\n\\paragraph{Log-probability (model-internal, per-sample).}\nThe only per-sample signal.\nFor sample $y_i$ with tokens $t_1, \\ldots, t_{|y_i|}$:\n\\begin{equation}\\label{eq:logprob}\nc_{\\text{lp}}(y_i) = \\frac{1}{|y_i|} \\sum_{j=1}^{|y_i|} \\log p_{\\mathcal{M}}(t_j \\mid t_{<j}, x)\n\\end{equation}\n\n\\paragraph{Exact match voting (surface, instance-level).}\nThe majority fraction---the proportion of samples producing the most common output:\n\\begin{equation}\\label{eq:em}\nc_{\\text{em}}(x) = \\frac{1}{N} \\max_{y} \\big|\\{i : y_i = y\\}\\big|\n\\end{equation}\n\n\\paragraph{Fleiss' $\\kappa$ (surface, instance-level).}\nWe adapt \\citet{fleiss1971agreement} to entity sets: items are unique (text, type) tuples across all $N$ samples; each sample assigns binary present/absent labels, yielding a $|E_\\cup| \\times 2$ rating matrix:\n\\begin{equation}\\label{eq:fk}\n\\kappa = \\frac{\\bar{P} - \\bar{P}_e}{1 - \\bar{P}_e}\n\\end{equation}\nwhere $\\bar{P}$ is mean observed pairwise agreement and $\\bar{P}_e$ is expected agreement under random assignment.\nWhile FK assumes independent raters, temperature-based sampling provides sufficient response diversity for the statistic to capture inter-sample agreement patterns.\nUnlike structural signals, FK relies on exact string matching and does not tolerate surface variations.\n\n\\paragraph{Soft Jaccard (structural, instance-level).}\nOur core structural signal extends Jaccard similarity \\cite{jaccard1901distribution} to extracted entity/relation sets.\nFor samples $y_i, y_j$, we group extractions by type, compute bipartite matching via the Hungarian algorithm with span overlap, and define:\n\\begin{equation}\\label{eq:sj}\n\\text{SJ}(y_i, y_j) = \\frac{\\sum_{m \\in M} \\text{sim}(a_m, b_m)}{\\sum_{g} \\max(|g_i|, |g_j|)}\n\\end{equation}\nwhere $M$ is the matched set from the Hungarian algorithm (without minimum similarity threshold), $\\text{sim}(a_m, b_m)$ is the token-level IoU (intersection of tokens divided by union of tokens) between matched entity spans $a_m$ and $b_m$, and $g_i, g_j$ index per-type extraction counts.\nWe use $\\max(|g_i|, |g_j|)$ rather than $|g_i \\cup g_j|$ as the normalizer to penalize length asymmetry between samples.\nThe instance-level signal averages over all pairs:\n\\begin{equation}\\label{eq:sj_instance}\nc_{\\text{sj}}(x) = \\frac{1}{\\binom{N}{2}} \\sum_{i<j} \\text{SJ}(y_i, y_j)\n\\end{equation}\n\n\\paragraph{Entity voting confidence (structural, instance-level).}\nFor each entity $e$ in the union $E_\\cup$ of all samples, we compute frequency $\\text{freq}(e) = |\\{i : e \\in y_i\\}| / N$.\nThe instance-level confidence is the mean frequency:\n\\begin{equation}\\label{eq:voting}\nc_{\\text{vote}}(x) = \\frac{1}{|E_\\cup|} \\sum_{e \\in E_\\cup} \\text{freq}(e)\n\\end{equation}\n\n\\subsection{Evaluation Framework}\\label{sec:evaluation}\n\n\\paragraph{Quality estimation.}\nWe measure rank correlation (Spearman $\\rho$) between the confidence signal and instance-level F1, and binary discrimination (AUROC) by classifying instances as above or below median F1.\n\n\\paragraph{Sample selection.}\nWe report best-of-$N$ F1: for each instance, the signal selects one sample.\nPer-sample signals (logprob) directly rank candidates; instance-level signals select the sample closest to the consensus output (the consensus-proximity score for SJ is mathematically equivalent to leave-one-out SJ selection).\nWe compare against an \\textit{oracle} (highest-F1 sample) and \\textit{greedy} ($T{=}0$, $N{=}1$).\n\n\\paragraph{Complementarity.}\nHigh rank correlation does not guarantee effective sample selection: if per-sample variance is low, even a perfect quality estimator cannot distinguish among near-identical candidates (\\S\\ref{sec:selection_gap}).\n",
      "numLines": 72,
      "startLine": 1,
      "totalLines": 72
    }
  },
  "sourceToolAssistantUUID": "29084bd3-0f9d-45cf-8ee2-779fd197c784",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_1_68ddc296",
  "sessionId": "8e0e70e7-e72a-426a-9f89-26576a55a64e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Tool call

_source line 35 · 2026-05-15T03:58:37.498Z_

<details open><summary>🔧 Tool call — Read · `toolu_014zVVnb1jLNgBHR1CsURr4J`</summary>

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
  "parentUuid": "68b15818-6b4f-450f-bcc7-69c399ddc271",
  "isSidechain": false,
  "requestId": "req_011Cb3gdXhzyZheeXCfNSoDT",
  "type": "assistant",
  "uuid": "3e746b3c-cc87-4647-9963-e48d7a0ca23a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_1_68ddc296",
  "sessionId": "8e0e70e7-e72a-426a-9f89-26576a55a64e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GTPM78Kk95tE4jx4dyGEHe",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 4126,
      "cache_read_input_tokens": 29566,
      "output_tokens": 571,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4126,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 571,
          "cache_read_input_tokens": 29566,
          "cache_creation_input_tokens": 4126,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4126
          },
          "type": "message"
        }
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

_source line 36 · 2026-05-15T03:58:37.517Z_

<details><summary>↩ Tool result · `toolu_014zVVnb1jLNgBHR1CsURr4J`</summary>

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
21	\title{Strong Predictors, Weak Selectors: A Systematic Comparison of Confidence Signals for Test-Time Scaling in Information Extraction}
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
39	\bibliography{references}
40	
41	\appendix
42	\input{sections/appendix}
43	
44	\end{document}
45	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3e746b3c-cc87-4647-9963-e48d7a0ca23a",
  "isSidechain": false,
  "promptId": "06c85d14-4a07-4193-8916-587ad0c60656",
  "type": "user",
  "uuid": "e1cad3d8-13e5-4903-bd9f-0b08170725d8",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex",
      "content": "\\documentclass[11pt]{article}\n\n\\usepackage[review]{acl}\n\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage[T1]{fontenc}\n\\usepackage[utf8]{inputenc}\n\\usepackage{microtype}\n\\usepackage{inconsolata}\n\\usepackage{graphicx}\n\\usepackage{booktabs}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{multirow}\n\\usepackage{xcolor}\n\\usepackage{subcaption}\n\n\\graphicspath{{figures/}}\n\n\\title{Strong Predictors, Weak Selectors: A Systematic Comparison of Confidence Signals for Test-Time Scaling in Information Extraction}\n\n\\author{Anonymous}\n\n\\begin{document}\n\\maketitle\n\n\\input{sections/abstract}\n\\input{sections/introduction}\n\\input{sections/related_work}\n\\input{sections/method}\n\\input{sections/experiments}\n\\input{sections/discussion}\n\\input{sections/conclusion}\n\n\\section*{Limitations}\n\\input{sections/limitations}\n\n\\bibliography{references}\n\n\\appendix\n\\input{sections/appendix}\n\n\\end{document}\n",
      "numLines": 45,
      "startLine": 1,
      "totalLines": 45
    }
  },
  "sourceToolAssistantUUID": "3e746b3c-cc87-4647-9963-e48d7a0ca23a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_1_68ddc296",
  "sessionId": "8e0e70e7-e72a-426a-9f89-26576a55a64e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Tool call

_source line 37 · 2026-05-15T03:58:37.957Z_

<details open><summary>🔧 Tool call — Read · `toolu_011k53StrtTHjaRcCPJZnctf`</summary>

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
  "parentUuid": "e1cad3d8-13e5-4903-bd9f-0b08170725d8",
  "isSidechain": false,
  "requestId": "req_011Cb3gdXhzyZheeXCfNSoDT",
  "type": "assistant",
  "uuid": "ef7aad45-0667-4f3a-9e26-69861e40b159",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_1_68ddc296",
  "sessionId": "8e0e70e7-e72a-426a-9f89-26576a55a64e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GTPM78Kk95tE4jx4dyGEHe",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 4126,
      "cache_read_input_tokens": 29566,
      "output_tokens": 571,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4126,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 571,
          "cache_read_input_tokens": 29566,
          "cache_creation_input_tokens": 4126,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4126
          },
          "type": "message"
        }
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

_source line 38 · 2026-05-15T03:58:37.963Z_

<details><summary>↩ Tool result · `toolu_011k53StrtTHjaRcCPJZnctf`</summary>

```text
1	\begin{abstract}
2	Test-time scaling through multi-sample generation promises quality improvements for LLM-based information extraction, but which confidence signals best serve quality estimation versus sample selection remains unclear.
3	We systematically compare five confidence signals from three families---structural (entity voting, Soft Jaccard), surface (exact match, Fleiss' $\kappa$), and model-internal (log-probability)---across NER (three datasets of varying difficulty) and RE (SciERC) with two model families (Qwen3-8B, LLaMA-3.1-8B).
4	We find that the strongest signals achieve $\rho{=}0.38$ (entity voting) and AUROC${=}0.75$ (exact match) for quality estimation, with ranking and classification favoring different signals across task complexity; however, this strong quality estimation does not translate into selection gains---no signal reliably surpasses greedy decoding in any of six tested configurations spanning two models and three datasets ($p{>}0.39$, bootstrap) despite 13--18~pp of oracle headroom.
5	We term this disconnect the \textit{correlation-selection gap}: instance-level consistency signals predict which inputs the model handles reliably, not which output is best among $N$ candidates.
6	Signal rankings further depend on task difficulty---exact match dominates easy tasks, structural signals dominate hard tasks, and when model capability is insufficient, apparent correlations are driven by zero/non-zero separation rather than genuine quality gradation---establishing that signal choice should be guided by task difficulty and intended application.
7	These results reframe consistency signals as quality estimators rather than output selectors for structured IE.
8	\end{abstract}
9	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ef7aad45-0667-4f3a-9e26-69861e40b159",
  "isSidechain": false,
  "promptId": "06c85d14-4a07-4193-8916-587ad0c60656",
  "type": "user",
  "uuid": "22904002-26c1-4bab-ad78-a0f7ff4177fc",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/abstract.tex",
      "content": "\\begin{abstract}\nTest-time scaling through multi-sample generation promises quality improvements for LLM-based information extraction, but which confidence signals best serve quality estimation versus sample selection remains unclear.\nWe systematically compare five confidence signals from three families---structural (entity voting, Soft Jaccard), surface (exact match, Fleiss' $\\kappa$), and model-internal (log-probability)---across NER (three datasets of varying difficulty) and RE (SciERC) with two model families (Qwen3-8B, LLaMA-3.1-8B).\nWe find that the strongest signals achieve $\\rho{=}0.38$ (entity voting) and AUROC${=}0.75$ (exact match) for quality estimation, with ranking and classification favoring different signals across task complexity; however, this strong quality estimation does not translate into selection gains---no signal reliably surpasses greedy decoding in any of six tested configurations spanning two models and three datasets ($p{>}0.39$, bootstrap) despite 13--18~pp of oracle headroom.\nWe term this disconnect the \\textit{correlation-selection gap}: instance-level consistency signals predict which inputs the model handles reliably, not which output is best among $N$ candidates.\nSignal rankings further depend on task difficulty---exact match dominates easy tasks, structural signals dominate hard tasks, and when model capability is insufficient, apparent correlations are driven by zero/non-zero separation rather than genuine quality gradation---establishing that signal choice should be guided by task difficulty and intended application.\nThese results reframe consistency signals as quality estimators rather than output selectors for structured IE.\n\\end{abstract}\n",
      "numLines": 9,
      "startLine": 1,
      "totalLines": 9
    }
  },
  "sourceToolAssistantUUID": "ef7aad45-0667-4f3a-9e26-69861e40b159",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_1_68ddc296",
  "sessionId": "8e0e70e7-e72a-426a-9f89-26576a55a64e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Tool call

_source line 39 · 2026-05-15T03:58:38.981Z_

<details open><summary>🔧 Tool call — Read · `toolu_01NMJUkowySfEmFc4RkQSbzB`</summary>

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
  "parentUuid": "22904002-26c1-4bab-ad78-a0f7ff4177fc",
  "isSidechain": false,
  "requestId": "req_011Cb3gdXhzyZheeXCfNSoDT",
  "type": "assistant",
  "uuid": "d1499ffb-f64b-4a08-8599-534094e57a91",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_1_68ddc296",
  "sessionId": "8e0e70e7-e72a-426a-9f89-26576a55a64e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GTPM78Kk95tE4jx4dyGEHe",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 4126,
      "cache_read_input_tokens": 29566,
      "output_tokens": 571,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4126,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 571,
          "cache_read_input_tokens": 29566,
          "cache_creation_input_tokens": 4126,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4126
          },
          "type": "message"
        }
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

_source line 40 · 2026-05-15T03:58:38.994Z_

<details><summary>↩ Tool result · `toolu_01NMJUkowySfEmFc4RkQSbzB`</summary>

```text
1	\section{Introduction}\label{sec:introduction}
2	
3	Self-consistency---sampling multiple outputs and aggregating them---has become a powerful strategy for improving language model reasoning.
4	On discrete-answer tasks such as arithmetic and commonsense QA, majority voting over chain-of-thought samples yields large gains: +18 percentage points on GSM8K (PaLM-540B; \citealp{wang2023selfconsistency}).
5	More broadly, test-time compute scaling through repeated sampling and selection has emerged as a complementary axis to model scaling, offering substantial quality improvements at inference time \cite{snell2024scaling, brown2024monkeys}.
6	These results rest on a shared assumption: that among $N$ stochastic samples, a selection mechanism can identify better outputs.
7	For tasks with a single correct answer, this assumption holds naturally---the majority vote is the selector.
8	But information extraction (IE) poses a fundamentally different challenge.
9	The output is not a single token or number; it is a \textit{set} of entities or relations with internal dependencies, where two samples may extract overlapping but non-identical structures.
10	There is no obvious majority to vote on, partial agreement is the norm rather than the exception, and the space of valid outputs is combinatorially large.
11	Can self-consistency still provide useful signal in this structured setting?
12	
13	Prior work on confidence estimation for LLM-based IE has conflated two distinct objectives: \textit{quality estimation} (which inputs does the model handle reliably?) and \textit{sample selection} (which of $N$ outputs is best?).
14	These require fundamentally different signal properties: the former benefits from instance-level aggregation, while the latter demands per-sample discrimination.
15	Self-consistency methods for discrete answers \cite{wang2023selfconsistency, chen2024usc} and weighted variants \cite{taubenfeld2025cisc, kang2025selfcertainty} assume outputs can be grouped by equivalence---an assumption that breaks for entity sets with partial overlap.
16	The most relevant study, \citet{nedellec2026consistency}, examines consistency--accuracy correlations for LLM-based IE but (i)~relies on surface-level matching, explicitly acknowledging it ``overlooks semantically consistent outputs,'' (ii)~evaluates only quality estimation without studying best-of-$N$ selection, and (iii)~covers a single domain with hard prompting rather than a difficulty gradient across benchmarks.
17	No existing work compares confidence signals from multiple families---surface-level, structural consistency, and probabilistic---for both quality estimation and sample selection in generative structured IE.
18	
19	Our central finding is that consistency-based signals are effective quality estimators but poor sample selectors for structured IE.
20	Entity voting achieves $\rho{=}0.38$ on SciERC NER and exact match leads AUROC${=}0.75$, both practically useful for quality-aware routing.
21	Yet no signal reliably surpasses greedy decoding on best-of-$N$ selection ($p{>}0.39$, bootstrap) despite 13--18~pp of oracle headroom.
22	We term this the \textbf{correlation-selection gap} (Figure~\ref{fig:overview}): instance-level signals predict \textit{which inputs} are hard, not \textit{which output} is best.
23	
24	\begin{figure*}[t]
25	\centering
26	\includegraphics[width=\textwidth]{fig_overview}
27	\caption{The correlation-selection gap. Left: consistency signals (here entity voting) predict instance-level quality---high agreement correlates with high F1 ($\rho{\approx}0.38$, AUROC${\approx}0.69$). Right: the same instance-level signal assigns identical scores to all $N$ candidates from a given input, precluding sample selection. No signal reliably surpasses greedy on either task ($p{=}0.39$ for NER logprob).}
28	\label{fig:overview}
29	\end{figure*}
30	
31	We systematically evaluate five confidence signals from three families---structural (entity voting, Soft Jaccard), surface (exact match, Fleiss' $\kappa$), and model-internal (log-probability)---across NER and RE on SciERC \cite{luan2018scierc}, CoNLL-2003 \cite{tjongkimsang2003conll}, and WNUT-17 \cite{derczynski2017wnut}, using Qwen3-8B and LLaMA-3.1-8B.
32	
33	Our contributions are as follows:
34	\begin{enumerate}
35	    \item \textbf{First multi-family comparison of confidence signals for generative IE.}
36	    We evaluate five signals from three families on quality estimation for NER and RE.
37	    Entity voting achieves the strongest $\rho{=}0.38$ while exact match leads AUROC${=}0.75$; signal rankings depend on both task complexity and evaluation metric, with structural signals leading rank correlation on complex schemas (SciERC) and surface signals leading on simpler tasks (CoNLL).
38	
39	    \item \textbf{Identification of the correlation-selection gap.}
40	    We demonstrate a fundamental disconnect between quality estimation and sample selection in structured IE.
41	    Despite strong instance-level correlations ($\rho$ up to 0.38), no signal reliably surpasses greedy in any of six tested configurations spanning two models and three datasets ($p{>}0.39$, bootstrap) despite 13--18~pp of oracle headroom.
42	    This gap reflects the instance-level nature of consistency signals, which predict input difficulty rather than discriminating among individual samples.
43	
44	    \item \textbf{Task-complexity boundary conditions.}
45	    Signal rankings depend on task difficulty: exact match leads on easy tasks (CoNLL), Soft Jaccard dominates on hard tasks (SciERC), and when model capability is insufficient (WNUT-17, 54\% zero F1), inflated full-set correlations collapse on the conditional set---all signals converge toward weak or non-significant correlations once the zero/non-zero boundary is removed.
46	    While our NER findings are validated across three datasets of varying difficulty, our RE conclusions are based on a single benchmark (SciERC) and warrant further validation.
47	\end{enumerate}
48	
49	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d1499ffb-f64b-4a08-8599-534094e57a91",
  "isSidechain": false,
  "promptId": "06c85d14-4a07-4193-8916-587ad0c60656",
  "type": "user",
  "uuid": "80971a70-ebe6-47c5-9fa1-9599a479b4e5",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/introduction.tex",
      "content": "\\section{Introduction}\\label{sec:introduction}\n\nSelf-consistency---sampling multiple outputs and aggregating them---has become a powerful strategy for improving language model reasoning.\nOn discrete-answer tasks such as arithmetic and commonsense QA, majority voting over chain-of-thought samples yields large gains: +18 percentage points on GSM8K (PaLM-540B; \\citealp{wang2023selfconsistency}).\nMore broadly, test-time compute scaling through repeated sampling and selection has emerged as a complementary axis to model scaling, offering substantial quality improvements at inference time \\cite{snell2024scaling, brown2024monkeys}.\nThese results rest on a shared assumption: that among $N$ stochastic samples, a selection mechanism can identify better outputs.\nFor tasks with a single correct answer, this assumption holds naturally---the majority vote is the selector.\nBut information extraction (IE) poses a fundamentally different challenge.\nThe output is not a single token or number; it is a \\textit{set} of entities or relations with internal dependencies, where two samples may extract overlapping but non-identical structures.\nThere is no obvious majority to vote on, partial agreement is the norm rather than the exception, and the space of valid outputs is combinatorially large.\nCan self-consistency still provide useful signal in this structured setting?\n\nPrior work on confidence estimation for LLM-based IE has conflated two distinct objectives: \\textit{quality estimation} (which inputs does the model handle reliably?) and \\textit{sample selection} (which of $N$ outputs is best?).\nThese require fundamentally different signal properties: the former benefits from instance-level aggregation, while the latter demands per-sample discrimination.\nSelf-consistency methods for discrete answers \\cite{wang2023selfconsistency, chen2024usc} and weighted variants \\cite{taubenfeld2025cisc, kang2025selfcertainty} assume outputs can be grouped by equivalence---an assumption that breaks for entity sets with partial overlap.\nThe most relevant study, \\citet{nedellec2026consistency}, examines consistency--accuracy correlations for LLM-based IE but (i)~relies on surface-level matching, explicitly acknowledging it ``overlooks semantically consistent outputs,'' (ii)~evaluates only quality estimation without studying best-of-$N$ selection, and (iii)~covers a single domain with hard prompting rather than a difficulty gradient across benchmarks.\nNo existing work compares confidence signals from multiple families---surface-level, structural consistency, and probabilistic---for both quality estimation and sample selection in generative structured IE.\n\nOur central finding is that consistency-based signals are effective quality estimators but poor sample selectors for structured IE.\nEntity voting achieves $\\rho{=}0.38$ on SciERC NER and exact match leads AUROC${=}0.75$, both practically useful for quality-aware routing.\nYet no signal reliably surpasses greedy decoding on best-of-$N$ selection ($p{>}0.39$, bootstrap) despite 13--18~pp of oracle headroom.\nWe term this the \\textbf{correlation-selection gap} (Figure~\\ref{fig:overview}): instance-level signals predict \\textit{which inputs} are hard, not \\textit{which output} is best.\n\n\\begin{figure*}[t]\n\\centering\n\\includegraphics[width=\\textwidth]{fig_overview}\n\\caption{The correlation-selection gap. Left: consistency signals (here entity voting) predict instance-level quality---high agreement correlates with high F1 ($\\rho{\\approx}0.38$, AUROC${\\approx}0.69$). Right: the same instance-level signal assigns identical scores to all $N$ candidates from a given input, precluding sample selection. No signal reliably surpasses greedy on either task ($p{=}0.39$ for NER logprob).}\n\\label{fig:overview}\n\\end{figure*}\n\nWe systematically evaluate five confidence signals from three families---structural (entity voting, Soft Jaccard), surface (exact match, Fleiss' $\\kappa$), and model-internal (log-probability)---across NER and RE on SciERC \\cite{luan2018scierc}, CoNLL-2003 \\cite{tjongkimsang2003conll}, and WNUT-17 \\cite{derczynski2017wnut}, using Qwen3-8B and LLaMA-3.1-8B.\n\nOur contributions are as follows:\n\\begin{enumerate}\n    \\item \\textbf{First multi-family comparison of confidence signals for generative IE.}\n    We evaluate five signals from three families on quality estimation for NER and RE.\n    Entity voting achieves the strongest $\\rho{=}0.38$ while exact match leads AUROC${=}0.75$; signal rankings depend on both task complexity and evaluation metric, with structural signals leading rank correlation on complex schemas (SciERC) and surface signals leading on simpler tasks (CoNLL).\n\n    \\item \\textbf{Identification of the correlation-selection gap.}\n    We demonstrate a fundamental disconnect between quality estimation and sample selection in structured IE.\n    Despite strong instance-level correlations ($\\rho$ up to 0.38), no signal reliably surpasses greedy in any of six tested configurations spanning two models and three datasets ($p{>}0.39$, bootstrap) despite 13--18~pp of oracle headroom.\n    This gap reflects the instance-level nature of consistency signals, which predict input difficulty rather than discriminating among individual samples.\n\n    \\item \\textbf{Task-complexity boundary conditions.}\n    Signal rankings depend on task difficulty: exact match leads on easy tasks (CoNLL), Soft Jaccard dominates on hard tasks (SciERC), and when model capability is insufficient (WNUT-17, 54\\% zero F1), inflated full-set correlations collapse on the conditional set---all signals converge toward weak or non-significant correlations once the zero/non-zero boundary is removed.\n    While our NER findings are validated across three datasets of varying difficulty, our RE conclusions are based on a single benchmark (SciERC) and warrant further validation.\n\\end{enumerate}\n\n",
      "numLines": 49,
      "startLine": 1,
      "totalLines": 49
    }
  },
  "sourceToolAssistantUUID": "d1499ffb-f64b-4a08-8599-534094e57a91",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_1_68ddc296",
  "sessionId": "8e0e70e7-e72a-426a-9f89-26576a55a64e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Tool call

_source line 41 · 2026-05-15T03:58:39.065Z_

<details open><summary>🔧 Tool call — Read · `toolu_01HcVS93yfs4NX2Ki8haF2tK`</summary>

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
  "parentUuid": "80971a70-ebe6-47c5-9fa1-9599a479b4e5",
  "isSidechain": false,
  "requestId": "req_011Cb3gdXhzyZheeXCfNSoDT",
  "type": "assistant",
  "uuid": "29084bd3-0f9d-45cf-8ee2-779fd197c784",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_1_68ddc296",
  "sessionId": "8e0e70e7-e72a-426a-9f89-26576a55a64e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GTPM78Kk95tE4jx4dyGEHe",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 4126,
      "cache_read_input_tokens": 29566,
      "output_tokens": 571,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4126,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 571,
          "cache_read_input_tokens": 29566,
          "cache_creation_input_tokens": 4126,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4126
          },
          "type": "message"
        }
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

_source line 42_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[Round 1 审稿请求]: 你是 Reviewer 1，负责**方法严谨性 + 实验设计**。  ## 审稿对象 - 论文路径：`projects/struct_self_consist_ie/docs/paper/main.tex`（分节结构，各节在 `sections/` 下） - 目标 venue：**EMNLP 2026 Main Conference**（通过 ARR May 202…",
  "leafUuid": "17bf66ef-8b9e-4e9b-a1cb-419c835913f8",
  "sessionId": "8e0e70e7-e72a-426a-9f89-26576a55a64e"
}
```

---


### Runtime record

_source line 43_

```json
{
  "type": "ai-title",
  "aiTitle": "Review paper on structural self-consistency for information extraction",
  "sessionId": "8e0e70e7-e72a-426a-9f89-26576a55a64e"
}
```

---


### Tool result

_source line 44 · 2026-05-15T03:58:44.146Z_

<details><summary>↩ Tool result · `toolu_01PkTG1FyKkfJ9X2CqSus8Dp`</summary>

```text
# ACL ARR Review Form Scoring Dimensions

## Reviewer Confidence (1-5 scale)
- **5**: "Positive that my evaluation is correct. I read the paper very carefully and am familiar with related work."
- **4**: "Quite sure. I tried to check the important points carefully."
- **3**: "Pretty sure, but there's a chance I missed something."
- **2**: "Willing to defend my evaluation, but it is fairly likely that I missed some details."
- **1**: "Not my area, or paper is very hard to understand."

## Soundness (1-5 scale with half-point increments)
- **5**: "Excellent: This study is one of the most thorough I have seen, given its type."
- **4**: "Strong: This study provides sufficient support for all of its claims."
- **3**: "Acceptable: This study provides sufficient support for its main claims."
- **2**: "Poor: Some of the main claims are not sufficiently supported."
- **1**: "Major Issues: This study is not yet sufficiently thorough to warrant publication."

## Excitement (1-5 scale with half-point increments)
- **5**: "Highly Exciting: I would recommend this paper to others and/or attend its presentation."
- **4**: "Exciting: I would mention this paper to others and/or make an effort to attend."
- **3**: "Interesting: I might mention some points of this paper to others."
- **2**: "Potentially Interesting: this paper does not resonate with me, but it might with others."
- **1**: "Not Exciting: this paper does not resonate with me, and I don't think it would with others."

## Overall Assessment (1-5 scale with half-point increments)
- **5**: "Consider for Award: could be considered for an outstanding paper award (top 2.5%)."
- **4**: "Conference: paper could be accepted to an *ACL conference."
- **3**: "Findings: paper could be accepted to the Findings of the ACL."
- **2**: "Resubmit next cycle: paper needs substantial revisions."
- **1**: "Do not resubmit: paper has to be fully redone or is not relevant."

## Reproducibility (1-5 scale)
- **5**: "They could easily reproduce the results."
- **4**: "They could mostly reproduce the results, but there may be some variation."
- **3**: "They could reproduce the results with some difficulty."
- **2**: "They would be hard pressed to reproduce the results."
- **1**: "They would not be able to reproduce the results."

## Datasets & Software Value (1-5 scales)
Both use identical scales ranging from "Enabling" (5) to "No usable [datasets/software] submitted" (1).

## Author Identity Knowledge (1-5 scale)
- **5**: Known/guessed from double-blind violation
- **4**: Known from preprint/workshop
- **3**: Known from submission contents
- **2**: Known from informal communication
- **1**: No educated guess about identity
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "68b15818-6b4f-450f-bcc7-69c399ddc271",
  "isSidechain": false,
  "promptId": "06c85d14-4a07-4193-8916-587ad0c60656",
  "type": "user",
  "uuid": "2d4259c5-6b3e-4c40-8806-e7465c1481c0",
  "toolUseResult": {
    "bytes": 25365,
    "code": 200,
    "codeText": "OK",
    "result": "# ACL ARR Review Form Scoring Dimensions\n\n## Reviewer Confidence (1-5 scale)\n- **5**: \"Positive that my evaluation is correct. I read the paper very carefully and am familiar with related work.\"\n- **4**: \"Quite sure. I tried to check the important points carefully.\"\n- **3**: \"Pretty sure, but there's a chance I missed something.\"\n- **2**: \"Willing to defend my evaluation, but it is fairly likely that I missed some details.\"\n- **1**: \"Not my area, or paper is very hard to understand.\"\n\n## Soundness (1-5 scale with half-point increments)\n- **5**: \"Excellent: This study is one of the most thorough I have seen, given its type.\"\n- **4**: \"Strong: This study provides sufficient support for all of its claims.\"\n- **3**: \"Acceptable: This study provides sufficient support for its main claims.\"\n- **2**: \"Poor: Some of the main claims are not sufficiently supported.\"\n- **1**: \"Major Issues: This study is not yet sufficiently thorough to warrant publication.\"\n\n## Excitement (1-5 scale with half-point increments)\n- **5**: \"Highly Exciting: I would recommend this paper to others and/or attend its presentation.\"\n- **4**: \"Exciting: I would mention this paper to others and/or make an effort to attend.\"\n- **3**: \"Interesting: I might mention some points of this paper to others.\"\n- **2**: \"Potentially Interesting: this paper does not resonate with me, but it might with others.\"\n- **1**: \"Not Exciting: this paper does not resonate with me, and I don't think it would with others.\"\n\n## Overall Assessment (1-5 scale with half-point increments)\n- **5**: \"Consider for Award: could be considered for an outstanding paper award (top 2.5%).\"\n- **4**: \"Conference: paper could be accepted to an *ACL conference.\"\n- **3**: \"Findings: paper could be accepted to the Findings of the ACL.\"\n- **2**: \"Resubmit next cycle: paper needs substantial revisions.\"\n- **1**: \"Do not resubmit: paper has to be fully redone or is not relevant.\"\n\n## Reproducibility (1-5 scale)\n- **5**: \"They could easily reproduce the results.\"\n- **4**: \"They could mostly reproduce the results, but there may be some variation.\"\n- **3**: \"They could reproduce the results with some difficulty.\"\n- **2**: \"They would be hard pressed to reproduce the results.\"\n- **1**: \"They would not be able to reproduce the results.\"\n\n## Datasets & Software Value (1-5 scales)\nBoth use identical scales ranging from \"Enabling\" (5) to \"No usable [datasets/software] submitted\" (1).\n\n## Author Identity Knowledge (1-5 scale)\n- **5**: Known/guessed from double-blind violation\n- **4**: Known from preprint/workshop\n- **3**: Known from submission contents\n- **2**: Known from informal communication\n- **1**: No educated guess about identity",
    "durationMs": 7443,
    "url": "https://aclrollingreview.org/reviewform"
  },
  "sourceToolAssistantUUID": "68b15818-6b4f-450f-bcc7-69c399ddc271",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_1_68ddc296",
  "sessionId": "8e0e70e7-e72a-426a-9f89-26576a55a64e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Runtime record

_source line 45 · 2026-05-15T03:58:44.196Z_

```json
{
  "parentUuid": "2d4259c5-6b3e-4c40-8806-e7465c1481c0",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "ac41837e-69f6-4a10-b67d-674bba1a8e9c",
  "timestamp": "2026-05-15T03:58:44.196Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_1_68ddc296",
  "sessionId": "8e0e70e7-e72a-426a-9f89-26576a55a64e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---


### Assistant

_source line 46 · 2026-05-15T03:58:50.078Z_

<details><summary>Logged reasoning block</summary>

```text
Good, I now have the ARR review form criteria and the main.tex, abstract, introduction, and method sections. Let me now read the remaining sections: experiments, discussion, related work, conclusion, limitations, and appendix.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ac41837e-69f6-4a10-b67d-674bba1a8e9c",
  "isSidechain": false,
  "requestId": "req_011Cb3gekhNWyzyow6auZ6L1",
  "type": "assistant",
  "uuid": "bbbf3a46-2e3d-4f35-9584-d13797b4093a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_1_68ddc296",
  "sessionId": "8e0e70e7-e72a-426a-9f89-26576a55a64e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Er5EDNuwXGiMqkng4nsnq6",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 4243,
      "cache_creation_input_tokens": 1431,
      "cache_read_input_tokens": 33692,
      "output_tokens": 538,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1431,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 4243,
          "output_tokens": 538,
          "cache_read_input_tokens": 33692,
          "cache_creation_input_tokens": 1431,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1431
          },
          "type": "message"
        }
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

_source line 47 · 2026-05-15T03:58:50.533Z_

继续读取剩余章节。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bbbf3a46-2e3d-4f35-9584-d13797b4093a",
  "isSidechain": false,
  "requestId": "req_011Cb3gekhNWyzyow6auZ6L1",
  "type": "assistant",
  "uuid": "a4ebf1bb-e8eb-4848-b5c9-ab70996c75ca",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_1_68ddc296",
  "sessionId": "8e0e70e7-e72a-426a-9f89-26576a55a64e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Er5EDNuwXGiMqkng4nsnq6",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 4243,
      "cache_creation_input_tokens": 1431,
      "cache_read_input_tokens": 33692,
      "output_tokens": 538,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1431,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 4243,
          "output_tokens": 538,
          "cache_read_input_tokens": 33692,
          "cache_creation_input_tokens": 1431,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1431
          },
          "type": "message"
        }
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

_source line 48 · 2026-05-15T03:58:52.528Z_

<details open><summary>🔧 Tool call — Read · `toolu_016p6MUsRwpnVx4H4cJeT7Za`</summary>

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
  "parentUuid": "a4ebf1bb-e8eb-4848-b5c9-ab70996c75ca",
  "isSidechain": false,
  "requestId": "req_011Cb3gekhNWyzyow6auZ6L1",
  "type": "assistant",
  "uuid": "44e9f231-a78d-4358-99ba-1f565bd74bdc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_1_68ddc296",
  "sessionId": "8e0e70e7-e72a-426a-9f89-26576a55a64e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Er5EDNuwXGiMqkng4nsnq6",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 4243,
      "cache_creation_input_tokens": 1431,
      "cache_read_input_tokens": 33692,
      "output_tokens": 538,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1431,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 4243,
          "output_tokens": 538,
          "cache_read_input_tokens": 33692,
          "cache_creation_input_tokens": 1431,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1431
          },
          "type": "message"
        }
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

_source line 49 · 2026-05-15T03:58:55.500Z_

<details><summary>↩ Tool result · `toolu_01R9HEKxhwnX9D1cejLFMqhP`</summary>

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
21	$c_{\text{vote}}$ & Entity voting confidence \\
22	$c_{\text{lp}}$ & Log-probability (mean token log-likelihood) \\
23	\bottomrule
24	\end{tabular}
25	\caption{Notation used throughout the paper.}
26	\label{tab:notation}
27	\end{table}
28	
29	\section{Robustness Analysis}\label{app:robustness}
30	
31	\begin{table}[t]
32	\centering
33	\small
34	\caption{Signal robustness across configurations (Spearman $\rho$). Top: temperature on Qwen SciERC. Middle: sample size on Qwen SciERC. Bottom: cross-model transfer (LLaMA CoNLL $N{=}16$, 3-seed mean $\pm\sigma$). $^\dagger$Mean over 3 seeds ($\sigma{=}0.025$; individual: 0.428, 0.424, 0.384).}
35	\label{tab:robustness}
36	\begin{tabular}{llcc}
37	\toprule
38	& & NER $\rho$ & RE $\rho$ \\
39	\midrule
40	\multicolumn{4}{l}{\textit{Temperature} (Qwen SciERC, $N{=}8$)} \\
41	\quad SJ & $T{=}0.7$ & 0.388 & 0.234 \\
42	\quad SJ & $T{=}1.0$ & 0.360 & 0.250 \\
43	\quad FK & $T{=}0.7$ & 0.321 & 0.184 \\
44	\quad FK & $T{=}1.0$ & 0.267 & 0.275 \\
45	\midrule
46	\multicolumn{4}{l}{\textit{Sample size} (Qwen SciERC, $T{=}1.0$)} \\
47	\quad SJ & $N{=}8$  & 0.360 & 0.250 \\
48	\quad SJ & $N{=}16$ & 0.412$^\dagger$ & 0.281 \\
49	\quad FK & $N{=}8$  & 0.267 & 0.275 \\
50	\quad FK & $N{=}16$ & 0.280 & 0.279 \\
51	\midrule
52	\multicolumn{4}{l}{\textit{Cross-model} (LLaMA CoNLL, $N{=}16$, 3 seeds)} \\
53	\quad SJ &  & $0.463{\pm}0.007$ & --- \\
54	\quad FK &  & $0.455{\pm}0.006$ & --- \\
55	\quad EM &  & $0.460{\pm}0.008$ & --- \\
56	\quad Voting &  & $0.458{\pm}0.003$ & --- \\
57	\quad Logprob &  & $0.310{\pm}0.005$ & --- \\
58	\bottomrule
59	\end{tabular}
60	\end{table}
61	
62	\begin{figure}[t]
63	\centering
64	\includegraphics[width=\columnwidth]{fig_temperature_robustness}
65	\caption{Temperature robustness on SciERC ($N{=}8$). Top: NER; bottom: RE. SJ maintains stable $\rho$ across $T{=}0.7$ and $T{=}1.0$, while FK shows mixed sensitivity. Logprob $T{=}0.7$ data unavailable.}
66	\label{fig:temperature_robustness}
67	\end{figure}
68	
69	\paragraph{Temperature sensitivity.}
70	SJ NER $\rho$ shifts from 0.388 ($T{=}0.7$) to 0.360 ($T{=}1.0$), a difference of 0.028 whose bootstrap confidence interval includes zero.
71	FK shows mixed behavior: NER $\rho$ drops by 0.054, while RE $\rho$ increases by 0.091, likely reflecting reduced diversity at lower temperature interacting differently across tasks.
72	Across all comparisons, the SJ--FK relative ordering is preserved at both temperatures on NER (0.388 vs.\ 0.321 at $T{=}0.7$; 0.360 vs.\ 0.267 at $T{=}1.0$), indicating a stable signal hierarchy despite numerically small temperature effects.
73	
74	\paragraph{Sample size scaling.}
75	Increasing from $N{=}8$ to $N{=}16$ improves SJ on Qwen SciERC NER: $\rho$ rises from 0.360 to $0.412{\pm}0.025$ (three seeds: 0.428, 0.424, 0.384), a gain of $+0.052$.
76	The magnitude of $N$-scaling gains is setting-dependent---LLaMA SciERC NER yields $+0.016$ and Qwen CoNLL NER $+0.014$---though the direction is consistently positive.
77	LLaMA CoNLL exhibits the most uniform scaling: all four consistency signals gain $\Delta\rho{\approx}{+}0.030$ (range: $+0.027$ to $+0.032$) while logprob gains only $+0.003$ (Table~\ref{tab:quality_estimation}).
78	FK $N$-scaling is inconsistent: degradation on SciERC ($-0.007$ to $-0.019$) but improvement on CoNLL with LLaMA ($+0.027$), suggesting sensitivity to both model and task characteristics.
79	Voting confidence $N$-scaling is consistently positive ($+0.005$ on Qwen CoNLL, $+0.018$ on LLaMA SciERC, $+0.062$ on Qwen SciERC), while logprob is approximately $N$-invariant ($\Delta{\leq}0.021$).
80	SJ, EM, and voting confidence scale consistently across all tested settings; only FK shows setting-dependent variation, suggesting that structural and binary-agreement signals are the most robust to $N$.
81	
82	\paragraph{Cross-model transfer.}
83	LLaMA-3.1-8B-Instruct replicates the structural-over-surface ordering on SciERC NER (SJ $\rho{=}0.363$, FK $\rho{=}0.327$).
84	On CoNLL, the cross-model gap is minimal (Table~\ref{tab:quality_estimation}): SJ achieves $\rho{=}0.431$ (LLaMA) vs.\ 0.436 (Qwen), $\Delta{=}0.005$.
85	At $N{=}16$, the structural-over-logprob advantage holds across all four tested settings: Qwen SciERC (Voting $\rho{=}0.411$ vs.\ logprob 0.259, $\Delta{=}{+}0.152$), Qwen CoNLL (EM $\rho{=}0.463$ vs.\ logprob 0.328, $\Delta{=}{+}0.135$), LLaMA SciERC (Voting $\rho{=}0.452$ vs.\ logprob 0.277, $\Delta{=}{+}0.175$), and LLaMA CoNLL 3-seed (SJ $\rho{=}0.463{\pm}0.007$ vs.\ logprob $0.310{\pm}0.005$, $\Delta{=}{+}0.153$).
86	
87	\section{Calibration Analysis}\label{app:calibration}
88	
89	\begin{figure*}[t]
90	\centering
91	\includegraphics[width=\textwidth]{fig_reliability}
92	\caption{Reliability diagrams on SciERC ($N{=}8$, $T{=}1.0$). Top: mean F1 vs.\ binned confidence; bottom: instance counts per bin. Left: NER; right: RE. NER signals are reasonably well-calibrated (calibration ECE 0.069--0.096), while RE shows greater miscalibration (ECE 0.109--0.339), reflecting the difficulty of calibrating confidence for compound extraction tasks.}
93	\label{fig:reliability}
94	\end{figure*}
95	
96	NER signals are reasonably well-calibrated (calibration ECE 0.069--0.096), while RE exhibits greater miscalibration (ECE 0.109--0.339), indicating that translating consistency scores into calibrated confidence estimates is feasible for NER but remains challenging for compound extraction tasks.
97	
98	\section{Additional Analyses}\label{app:additional}
99	
100	\paragraph{Per-relation diagnostic.}
101	RE signal degradation is relation-specific.
102	\textsc{Feature-Of} has near-zero correlation ($\rho{=}0.004$), while \textsc{Hyponym-Of} achieves $\rho{=}0.646$.
103	The primary bottleneck is entity span errors, which account for 55.5\% of RE false negatives---a prerequisite failure that consistency signals cannot detect, as they measure agreement among equally incorrect extractions.
104	We note that RE analysis relies on a single dataset (SciERC); generalization to other RE benchmarks remains to be validated.
105	
106	\paragraph{Capability stratification.}
107	For NER, SJ effectiveness scales with structural complexity: on SciERC instances with 6+ entities, $\rho{=}0.547$, compared to $\rho{=}0.415$ for 1--2 entities.
108	The SJ advantage over logprob remains stable across sentence-length quartiles ($\Delta\rho{\approx}0.08$--$0.20$).
109	For RE, SJ $\rho$ increases monotonically with sentence length (Q1: 0.110 $\to$ Q4: 0.473; Fisher $z$-test $p{=}0.004$), indicating that longer, more relation-dense sentences provide richer structure for consistency-based estimation.
110	Both proxies are weakly correlated with F1 ($|r|{<}0.15$), confirming they capture input complexity rather than directly predicting output quality; however, entity count and sentence length are themselves moderately correlated ($\rho{=}0.650$), so they reflect overlapping rather than independent complexity dimensions.
111	For RE, entity count and relation count are strongly correlated ($\rho{=}0.769$) and thus reflect a single structural complexity dimension rather than independent axes.
112	On the high-complexity RE subset ($n{=}81$, high relation count), signals improve substantially: Voting reaches $\rho{=}0.630$, logprob $\rho{=}0.554$, and SJ $\rho{=}0.502$---all far above the full-set levels.
113	Richer relational structure provides more signal for consistency-based estimation, complementing the task-level boundary established by WNUT-17: structural signals are most effective within a ``sweet spot'' of sufficient model capability and sufficient output complexity.
114	
115	\paragraph{Length vs.\ log-probability.}
116	Figure~\ref{fig:length_logprob_scatter} shows that mean log-probability is weakly positively correlated with output length (NER: $\rho{=}0.386$, $n{=}4{,}232$; RE: $\rho{=}0.326$, $n{=}3{,}176$), ruling out length-penalty confounding as an explanation for logprob's selection failure: longer outputs receive \textit{higher}, not lower, token-averaged log-probability under constrained decoding.
117	
118	\begin{figure}[t]
119	\centering
120	\includegraphics[width=\columnwidth]{fig_length_logprob_scatter}
121	\caption{Output length vs.\ mean log-probability on SciERC ($N{=}8$, $T{=}1.0$). Positive correlations (NER: $\rho{=}0.386$; RE: $\rho{=}0.326$) rule out length-penalty confounding.}
122	\label{fig:length_logprob_scatter}
123	\end{figure}
124	
125	\paragraph{Evaluation circularity.}
126	Leave-one-out SJ (LOO-SJ), which excludes the target sample when computing confidence, yields $\Delta\rho{=}{-}0.014$ relative to standard SJ, with a maximum per-instance $\Delta\rho$ of $3.1{\times}10^{-4}$.
127	Evaluation circularity is negligible.
128	
129	\paragraph{Conditional filtering details.}
130	On LLaMA conditional RE (non-zero F1 instances), SJ recovers to $\rho{=}0.405$ while FK drops to $\rho{=}0.259$, confirming that structural advantage is robust across both models and evaluation conditions.
131	At $N{=}16$, the divergence persists: SJ maintains $\rho{=}0.308$ on conditional RE while logprob drops to $\rho{=}{-}0.026$.
132	EM ranks first across all four tested conditional configurations---SciERC NER ($\rho{=}0.360$), CoNLL Qwen $N{=}16$ ($\rho{=}0.466$), CoNLL LLaMA 3-seed ($\rho{=}0.462$), and SciERC RE ($\rho{=}0.417$)---despite full-set rankings ranging from \#1 (CoNLL Qwen) to \#5 (SciERC RE).
133	On the full set, EM is diluted by trivial agreement: instances where all $N$ samples produce identical (possibly incorrect) outputs receive EM${=}1$ regardless of quality, compressing the signal's dynamic range.
134	On the conditional set---where the model demonstrably produces varied outputs---exact agreement becomes the strongest quality signal.
135	The margin over SJ is largest on RE ($\Delta\rho{=}{+}0.171$), where compound extraction decisions amplify output variability, and smallest on CoNLL LLaMA ($\Delta\rho{=}{+}0.002$), where all signals converge near $\rho{\approx}0.46$.
136	
137	\paragraph{WNUT-17 full signal analysis.}
138	Table~\ref{tab:wnut} reports all five signals on WNUT-17.
139	Voting achieves $\rho{=}0.724$ (AUROC${=}0.913$) on the full set, but conditional analysis (non-zero F1 instances) reveals this is entirely driven by the zero/non-zero boundary: conditional $\rho{=}0.038$ ($p{=}0.49$).
140	Logprob shows the reverse pattern: full-set $\rho{=}{-}0.410$ but conditional $\rho{=}0.350$, the highest among all signals on the conditional set.
141	This inversion confirms that full-set correlations on high-failure-rate datasets conflate binary success prediction with quality gradation.
142	
143	\begin{table}[t]
144	\centering
145	\small
146	\caption{Quality estimation on WNUT-17 (Qwen, $N{=}8$, $T{=}1.0$, $n{=}689$ after filtering gold-empty instances). Cond: non-zero F1 instances ($n{=}334$). Logprob exhibits strong negative full-set $\rho$; its conditional $\rho$ reverses to the highest among all signals, confirming that full-set correlations on high-failure-rate datasets conflate binary success prediction with quality gradation.}
147	\label{tab:wnut}
148	\begin{tabular}{lccccc}
149	\toprule
150	Signal & $\rho$ & $p$ & AUROC & Cond.\ $\rho$ & Cond.\ $p$ \\
151	\midrule
152	Voting  & .724 & ${<}$1e-112 & .913 & .038 & .487 \\
153	FK      & .125 & .001 & .555 & .169 & .002 \\
154	SJ      & .089 & .020 & .517 & .288 & ${<}$1e-7 \\
155	EM      & .050 & .194 & .487 & .333 & ${<}$1e-9 \\
156	Logprob & $-$.410 & ${<}$1e-28 & .219 & .350 & ${<}$1e-10 \\
157	\bottomrule
158	\end{tabular}
159	\end{table}
160	
161	\paragraph{Cross-configuration selection analysis.}
162	Table~\ref{tab:cross_selection} extends the correlation-selection gap analysis with per-signal best-of-$N$ selection F1 across four additional configurations (supplementing Table~\ref{tab:selection} for Qwen SciERC).
163	No signal reliably surpasses greedy in any setting.
164	On CoNLL, where greedy already exceeds 0.90 F1, all signals perform at or below greedy, confirming the gap is not specific to a single model--dataset combination.
165	
166	\begin{table*}[t]
167	\centering
168	\small
169	\caption{Best-of-$N$ selection F1 across configurations ($T{=}1.0$). Best non-oracle signal per row in \textbf{bold}. No signal reliably surpasses greedy in any configuration; CoNLL shows especially tight clustering where greedy already exceeds 0.90.}
170	\label{tab:cross_selection}
171	\begin{tabular}{llccccccc}
172	\toprule
173	Config & $n$ & Greedy & Oracle & SJ & FK & EM & LP & VC \\
174	\midrule
175	LLaMA/SciERC $N{=}8$ & 529 & .646 & .778 & .643 & .639 & .634 & \textbf{.652} & .633 \\
176	LLaMA/SciERC $N{=}16$ & 529 & .645 & .806 & \textbf{.649} & \textbf{.649} & .640 & .646 & .640 \\
177	Qwen/CoNLL $N{=}8$ & 2{,}756 & .908 & .948 & \textbf{.899} & .893 & .898 & .897 & .895 \\
178	LLaMA/CoNLL $N{=}8$ & 2{,}756 & .924 & .943 & .924 & \textbf{.925} & .924 & .924 & .923 \\
179	\bottomrule
180	\end{tabular}
181	\end{table*}
182	
183	\paragraph{Diminishing returns of $N$-scaling.}
184	Our $N{=}8$ and $N{=}16$ comparisons (Table~\ref{tab:robustness}) characterize the marginal value of additional samples for test-time scaling \cite{brown2024monkeys, snell2024scaling}.
185	For quality estimation, structural signals benefit consistently but sublinearly: SJ $\rho$ improves by $+0.052$ (Qwen SciERC, 3-seed mean) and $+0.032$ (LLaMA CoNLL, 3-seed mean) when doubling from $N{=}8$ to $N{=}16$, while log-probability is approximately $N$-invariant ($\Delta\rho{\leq}0.021$).
186	Structural signals leverage $\binom{N}{2}$ pairwise comparisons (28 pairs at $N{=}8$, 120 at $N{=}16$), but the $\rho$ improvement is far less than proportional, indicating diminishing information per additional comparison.
187	This asymmetry gives structural signals a relative advantage in the compute-constrained regime: at $N{=}8$, SJ already achieves $\rho{=}0.431$ on LLaMA CoNLL (vs.\ logprob $\rho{=}0.307$, $\Delta{=}{+}0.124$), and the gap \textit{widens} at $N{=}16$ ($\Delta{=}{+}0.153$) because structural signals continue to benefit from additional pairwise evidence while logprob does not.
188	For sample selection, additional samples increase the oracle upper bound---more draws raise the probability of a high-quality candidate---but signal-based selection remains flat because the selector's inability to identify the best candidate is a granularity limitation, not a sample size limitation.
189	The practical implication is that $N{=}8$ captures most of the achievable quality estimation benefit; further scaling widens rather than closes the correlation-selection gap absent stronger per-sample selectors.
190	
191	\section{Bootstrap CI for Signal Comparisons}\label{app:bootstrap_signal}
192	
193	Table~\ref{tab:bootstrap_signal_ci} reports bootstrap confidence intervals for individual signal $\rho$ and pairwise $\Delta\rho$ on SciERC NER ($N{=}8$, $n{=}529$, $B{=}10{,}000$, seed${=}42$).
194	The SJ--logprob gap ($\Delta\rho{=}{+}0.155$) is clearly significant, confirming the structural advantage reported in \S\ref{sec:qe_results}.
195	The Voting--SJ gap ($\Delta\rho{=}{+}0.019$) is not significant, indicating that these two structural signals perform comparably.
196	The SJ--EM gap ($\Delta\rho{=}{+}0.065$) is borderline significant, with the CI lower bound at $+0.003$ and upper bound at $+0.130$.
197	
198	\begin{table}[t]
199	\centering
200	\small
201	\caption{Bootstrap 95\% CIs for signal $\rho$ on SciERC NER ($N{=}8$, $n{=}529$, $B{=}10{,}000$, seed${=}42$). Top: individual signals. Bottom: pairwise $\Delta\rho$; ``Sig.'' indicates whether the 95\% CI excludes zero.}
202	\label{tab:bootstrap_signal_ci}
203	\begin{tabular}{lcc}
204	\toprule
205	Signal & $\rho$ & 95\% CI \\
206	\midrule
207	Voting Conf. & +0.379 & [+0.299, +0.456] \\
208	Soft Jaccard & +0.360 & [+0.277, +0.437] \\
209	Exact Match & +0.295 & [+0.212, +0.371] \\
210	Fleiss' $\kappa$ & +0.267 & [+0.176, +0.354] \\
211	Log-prob & +0.205 & [+0.119, +0.291] \\
212	\bottomrule
213	\end{tabular}
214	
215	\vspace{0.5em}
216	
217	\begin{tabular}{lccc}
218	\toprule
219	Comparison & $\Delta\rho$ & 95\% CI & Sig. \\
220	\midrule
221	SJ $-$ Logprob & +0.155 & [+0.074, +0.234] & Yes \\
222	Voting $-$ SJ & +0.019 & [$-$0.033, +0.073] & No \\
223	SJ $-$ EM & +0.065 & [+0.003, +0.130] & Yes$^\dagger$ \\
224	\bottomrule
225	\end{tabular}
226	
227	\smallskip
228	{\footnotesize $^\dagger$Borderline significant (CI barely excludes zero).}
229	\end{table}
230	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "220ff36d-8a8d-4644-80f0-3e027ea6966d",
  "isSidechain": false,
  "promptId": "06c85d14-4a07-4193-8916-587ad0c60656",
  "type": "user",
  "uuid": "9df3d12a-51ea-4981-9422-a7ba3c37bdad",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
      "content": "\\section{Notation}\\label{app:notation}\n\nTable~\\ref{tab:notation} summarizes the notation used throughout the paper.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{cl}\n\\toprule\nSymbol & Meaning \\\\\n\\midrule\n$\\mathcal{M}$ & Language model \\\\\n$x$ & Input instance \\\\\n$y_i$ & $i$-th stochastic sample \\\\\n$N$ & Number of samples \\\\\n$T$ & Sampling temperature \\\\\n$c(\\cdot)$ & Confidence signal \\\\\nSJ & Soft Jaccard similarity \\\\\nFK & Fleiss' $\\kappa$ \\\\\nEM & Exact-match voting rate \\\\\n$c_{\\text{vote}}$ & Entity voting confidence \\\\\n$c_{\\text{lp}}$ & Log-probability (mean token log-likelihood) \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Notation used throughout the paper.}\n\\label{tab:notation}\n\\end{table}\n\n\\section{Robustness Analysis}\\label{app:robustness}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Signal robustness across configurations (Spearman $\\rho$). Top: temperature on Qwen SciERC. Middle: sample size on Qwen SciERC. Bottom: cross-model transfer (LLaMA CoNLL $N{=}16$, 3-seed mean $\\pm\\sigma$). $^\\dagger$Mean over 3 seeds ($\\sigma{=}0.025$; individual: 0.428, 0.424, 0.384).}\n\\label{tab:robustness}\n\\begin{tabular}{llcc}\n\\toprule\n& & NER $\\rho$ & RE $\\rho$ \\\\\n\\midrule\n\\multicolumn{4}{l}{\\textit{Temperature} (Qwen SciERC, $N{=}8$)} \\\\\n\\quad SJ & $T{=}0.7$ & 0.388 & 0.234 \\\\\n\\quad SJ & $T{=}1.0$ & 0.360 & 0.250 \\\\\n\\quad FK & $T{=}0.7$ & 0.321 & 0.184 \\\\\n\\quad FK & $T{=}1.0$ & 0.267 & 0.275 \\\\\n\\midrule\n\\multicolumn{4}{l}{\\textit{Sample size} (Qwen SciERC, $T{=}1.0$)} \\\\\n\\quad SJ & $N{=}8$  & 0.360 & 0.250 \\\\\n\\quad SJ & $N{=}16$ & 0.412$^\\dagger$ & 0.281 \\\\\n\\quad FK & $N{=}8$  & 0.267 & 0.275 \\\\\n\\quad FK & $N{=}16$ & 0.280 & 0.279 \\\\\n\\midrule\n\\multicolumn{4}{l}{\\textit{Cross-model} (LLaMA CoNLL, $N{=}16$, 3 seeds)} \\\\\n\\quad SJ &  & $0.463{\\pm}0.007$ & --- \\\\\n\\quad FK &  & $0.455{\\pm}0.006$ & --- \\\\\n\\quad EM &  & $0.460{\\pm}0.008$ & --- \\\\\n\\quad Voting &  & $0.458{\\pm}0.003$ & --- \\\\\n\\quad Logprob &  & $0.310{\\pm}0.005$ & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{fig_temperature_robustness}\n\\caption{Temperature robustness on SciERC ($N{=}8$). Top: NER; bottom: RE. SJ maintains stable $\\rho$ across $T{=}0.7$ and $T{=}1.0$, while FK shows mixed sensitivity. Logprob $T{=}0.7$ data unavailable.}\n\\label{fig:temperature_robustness}\n\\end{figure}\n\n\\paragraph{Temperature sensitivity.}\nSJ NER $\\rho$ shifts from 0.388 ($T{=}0.7$) to 0.360 ($T{=}1.0$), a difference of 0.028 whose bootstrap confidence interval includes zero.\nFK shows mixed behavior: NER $\\rho$ drops by 0.054, while RE $\\rho$ increases by 0.091, likely reflecting reduced diversity at lower temperature interacting differently across tasks.\nAcross all comparisons, the SJ--FK relative ordering is preserved at both temperatures on NER (0.388 vs.\\ 0.321 at $T{=}0.7$; 0.360 vs.\\ 0.267 at $T{=}1.0$), indicating a stable signal hierarchy despite numerically small temperature effects.\n\n\\paragraph{Sample size scaling.}\nIncreasing from $N{=}8$ to $N{=}16$ improves SJ on Qwen SciERC NER: $\\rho$ rises from 0.360 to $0.412{\\pm}0.025$ (three seeds: 0.428, 0.424, 0.384), a gain of $+0.052$.\nThe magnitude of $N$-scaling gains is setting-dependent---LLaMA SciERC NER yields $+0.016$ and Qwen CoNLL NER $+0.014$---though the direction is consistently positive.\nLLaMA CoNLL exhibits the most uniform scaling: all four consistency signals gain $\\Delta\\rho{\\approx}{+}0.030$ (range: $+0.027$ to $+0.032$) while logprob gains only $+0.003$ (Table~\\ref{tab:quality_estimation}).\nFK $N$-scaling is inconsistent: degradation on SciERC ($-0.007$ to $-0.019$) but improvement on CoNLL with LLaMA ($+0.027$), suggesting sensitivity to both model and task characteristics.\nVoting confidence $N$-scaling is consistently positive ($+0.005$ on Qwen CoNLL, $+0.018$ on LLaMA SciERC, $+0.062$ on Qwen SciERC), while logprob is approximately $N$-invariant ($\\Delta{\\leq}0.021$).\nSJ, EM, and voting confidence scale consistently across all tested settings; only FK shows setting-dependent variation, suggesting that structural and binary-agreement signals are the most robust to $N$.\n\n\\paragraph{Cross-model transfer.}\nLLaMA-3.1-8B-Instruct replicates the structural-over-surface ordering on SciERC NER (SJ $\\rho{=}0.363$, FK $\\rho{=}0.327$).\nOn CoNLL, the cross-model gap is minimal (Table~\\ref{tab:quality_estimation}): SJ achieves $\\rho{=}0.431$ (LLaMA) vs.\\ 0.436 (Qwen), $\\Delta{=}0.005$.\nAt $N{=}16$, the structural-over-logprob advantage holds across all four tested settings: Qwen SciERC (Voting $\\rho{=}0.411$ vs.\\ logprob 0.259, $\\Delta{=}{+}0.152$), Qwen CoNLL (EM $\\rho{=}0.463$ vs.\\ logprob 0.328, $\\Delta{=}{+}0.135$), LLaMA SciERC (Voting $\\rho{=}0.452$ vs.\\ logprob 0.277, $\\Delta{=}{+}0.175$), and LLaMA CoNLL 3-seed (SJ $\\rho{=}0.463{\\pm}0.007$ vs.\\ logprob $0.310{\\pm}0.005$, $\\Delta{=}{+}0.153$).\n\n\\section{Calibration Analysis}\\label{app:calibration}\n\n\\begin{figure*}[t]\n\\centering\n\\includegraphics[width=\\textwidth]{fig_reliability}\n\\caption{Reliability diagrams on SciERC ($N{=}8$, $T{=}1.0$). Top: mean F1 vs.\\ binned confidence; bottom: instance counts per bin. Left: NER; right: RE. NER signals are reasonably well-calibrated (calibration ECE 0.069--0.096), while RE shows greater miscalibration (ECE 0.109--0.339), reflecting the difficulty of calibrating confidence for compound extraction tasks.}\n\\label{fig:reliability}\n\\end{figure*}\n\nNER signals are reasonably well-calibrated (calibration ECE 0.069--0.096), while RE exhibits greater miscalibration (ECE 0.109--0.339), indicating that translating consistency scores into calibrated confidence estimates is feasible for NER but remains challenging for compound extraction tasks.\n\n\\section{Additional Analyses}\\label{app:additional}\n\n\\paragraph{Per-relation diagnostic.}\nRE signal degradation is relation-specific.\n\\textsc{Feature-Of} has near-zero correlation ($\\rho{=}0.004$), while \\textsc{Hyponym-Of} achieves $\\rho{=}0.646$.\nThe primary bottleneck is entity span errors, which account for 55.5\\% of RE false negatives---a prerequisite failure that consistency signals cannot detect, as they measure agreement among equally incorrect extractions.\nWe note that RE analysis relies on a single dataset (SciERC); generalization to other RE benchmarks remains to be validated.\n\n\\paragraph{Capability stratification.}\nFor NER, SJ effectiveness scales with structural complexity: on SciERC instances with 6+ entities, $\\rho{=}0.547$, compared to $\\rho{=}0.415$ for 1--2 entities.\nThe SJ advantage over logprob remains stable across sentence-length quartiles ($\\Delta\\rho{\\approx}0.08$--$0.20$).\nFor RE, SJ $\\rho$ increases monotonically with sentence length (Q1: 0.110 $\\to$ Q4: 0.473; Fisher $z$-test $p{=}0.004$), indicating that longer, more relation-dense sentences provide richer structure for consistency-based estimation.\nBoth proxies are weakly correlated with F1 ($|r|{<}0.15$), confirming they capture input complexity rather than directly predicting output quality; however, entity count and sentence length are themselves moderately correlated ($\\rho{=}0.650$), so they reflect overlapping rather than independent complexity dimensions.\nFor RE, entity count and relation count are strongly correlated ($\\rho{=}0.769$) and thus reflect a single structural complexity dimension rather than independent axes.\nOn the high-complexity RE subset ($n{=}81$, high relation count), signals improve substantially: Voting reaches $\\rho{=}0.630$, logprob $\\rho{=}0.554$, and SJ $\\rho{=}0.502$---all far above the full-set levels.\nRicher relational structure provides more signal for consistency-based estimation, complementing the task-level boundary established by WNUT-17: structural signals are most effective within a ``sweet spot'' of sufficient model capability and sufficient output complexity.\n\n\\paragraph{Length vs.\\ log-probability.}\nFigure~\\ref{fig:length_logprob_scatter} shows that mean log-probability is weakly positively correlated with output length (NER: $\\rho{=}0.386$, $n{=}4{,}232$; RE: $\\rho{=}0.326$, $n{=}3{,}176$), ruling out length-penalty confounding as an explanation for logprob's selection failure: longer outputs receive \\textit{higher}, not lower, token-averaged log-probability under constrained decoding.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{fig_length_logprob_scatter}\n\\caption{Output length vs.\\ mean log-probability on SciERC ($N{=}8$, $T{=}1.0$). Positive correlations (NER: $\\rho{=}0.386$; RE: $\\rho{=}0.326$) rule out length-penalty confounding.}\n\\label{fig:length_logprob_scatter}\n\\end{figure}\n\n\\paragraph{Evaluation circularity.}\nLeave-one-out SJ (LOO-SJ), which excludes the target sample when computing confidence, yields $\\Delta\\rho{=}{-}0.014$ relative to standard SJ, with a maximum per-instance $\\Delta\\rho$ of $3.1{\\times}10^{-4}$.\nEvaluation circularity is negligible.\n\n\\paragraph{Conditional filtering details.}\nOn LLaMA conditional RE (non-zero F1 instances), SJ recovers to $\\rho{=}0.405$ while FK drops to $\\rho{=}0.259$, confirming that structural advantage is robust across both models and evaluation conditions.\nAt $N{=}16$, the divergence persists: SJ maintains $\\rho{=}0.308$ on conditional RE while logprob drops to $\\rho{=}{-}0.026$.\nEM ranks first across all four tested conditional configurations---SciERC NER ($\\rho{=}0.360$), CoNLL Qwen $N{=}16$ ($\\rho{=}0.466$), CoNLL LLaMA 3-seed ($\\rho{=}0.462$), and SciERC RE ($\\rho{=}0.417$)---despite full-set rankings ranging from \\#1 (CoNLL Qwen) to \\#5 (SciERC RE).\nOn the full set, EM is diluted by trivial agreement: instances where all $N$ samples produce identical (possibly incorrect) outputs receive EM${=}1$ regardless of quality, compressing the signal's dynamic range.\nOn the conditional set---where the model demonstrably produces varied outputs---exact agreement becomes the strongest quality signal.\nThe margin over SJ is largest on RE ($\\Delta\\rho{=}{+}0.171$), where compound extraction decisions amplify output variability, and smallest on CoNLL LLaMA ($\\Delta\\rho{=}{+}0.002$), where all signals converge near $\\rho{\\approx}0.46$.\n\n\\paragraph{WNUT-17 full signal analysis.}\nTable~\\ref{tab:wnut} reports all five signals on WNUT-17.\nVoting achieves $\\rho{=}0.724$ (AUROC${=}0.913$) on the full set, but conditional analysis (non-zero F1 instances) reveals this is entirely driven by the zero/non-zero boundary: conditional $\\rho{=}0.038$ ($p{=}0.49$).\nLogprob shows the reverse pattern: full-set $\\rho{=}{-}0.410$ but conditional $\\rho{=}0.350$, the highest among all signals on the conditional set.\nThis inversion confirms that full-set correlations on high-failure-rate datasets conflate binary success prediction with quality gradation.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Quality estimation on WNUT-17 (Qwen, $N{=}8$, $T{=}1.0$, $n{=}689$ after filtering gold-empty instances). Cond: non-zero F1 instances ($n{=}334$). Logprob exhibits strong negative full-set $\\rho$; its conditional $\\rho$ reverses to the highest among all signals, confirming that full-set correlations on high-failure-rate datasets conflate binary success prediction with quality gradation.}\n\\label{tab:wnut}\n\\begin{tabular}{lccccc}\n\\toprule\nSignal & $\\rho$ & $p$ & AUROC & Cond.\\ $\\rho$ & Cond.\\ $p$ \\\\\n\\midrule\nVoting  & .724 & ${<}$1e-112 & .913 & .038 & .487 \\\\\nFK      & .125 & .001 & .555 & .169 & .002 \\\\\nSJ      & .089 & .020 & .517 & .288 & ${<}$1e-7 \\\\\nEM      & .050 & .194 & .487 & .333 & ${<}$1e-9 \\\\\nLogprob & $-$.410 & ${<}$1e-28 & .219 & .350 & ${<}$1e-10 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Cross-configuration selection analysis.}\nTable~\\ref{tab:cross_selection} extends the correlation-selection gap analysis with per-signal best-of-$N$ selection F1 across four additional configurations (supplementing Table~\\ref{tab:selection} for Qwen SciERC).\nNo signal reliably surpasses greedy in any setting.\nOn CoNLL, where greedy already exceeds 0.90 F1, all signals perform at or below greedy, confirming the gap is not specific to a single model--dataset combination.\n\n\\begin{table*}[t]\n\\centering\n\\small\n\\caption{Best-of-$N$ selection F1 across configurations ($T{=}1.0$). Best non-oracle signal per row in \\textbf{bold}. No signal reliably surpasses greedy in any configuration; CoNLL shows especially tight clustering where greedy already exceeds 0.90.}\n\\label{tab:cross_selection}\n\\begin{tabular}{llccccccc}\n\\toprule\nConfig & $n$ & Greedy & Oracle & SJ & FK & EM & LP & VC \\\\\n\\midrule\nLLaMA/SciERC $N{=}8$ & 529 & .646 & .778 & .643 & .639 & .634 & \\textbf{.652} & .633 \\\\\nLLaMA/SciERC $N{=}16$ & 529 & .645 & .806 & \\textbf{.649} & \\textbf{.649} & .640 & .646 & .640 \\\\\nQwen/CoNLL $N{=}8$ & 2{,}756 & .908 & .948 & \\textbf{.899} & .893 & .898 & .897 & .895 \\\\\nLLaMA/CoNLL $N{=}8$ & 2{,}756 & .924 & .943 & .924 & \\textbf{.925} & .924 & .924 & .923 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table*}\n\n\\paragraph{Diminishing returns of $N$-scaling.}\nOur $N{=}8$ and $N{=}16$ comparisons (Table~\\ref{tab:robustness}) characterize the marginal value of additional samples for test-time scaling \\cite{brown2024monkeys, snell2024scaling}.\nFor quality estimation, structural signals benefit consistently but sublinearly: SJ $\\rho$ improves by $+0.052$ (Qwen SciERC, 3-seed mean) and $+0.032$ (LLaMA CoNLL, 3-seed mean) when doubling from $N{=}8$ to $N{=}16$, while log-probability is approximately $N$-invariant ($\\Delta\\rho{\\leq}0.021$).\nStructural signals leverage $\\binom{N}{2}$ pairwise comparisons (28 pairs at $N{=}8$, 120 at $N{=}16$), but the $\\rho$ improvement is far less than proportional, indicating diminishing information per additional comparison.\nThis asymmetry gives structural signals a relative advantage in the compute-constrained regime: at $N{=}8$, SJ already achieves $\\rho{=}0.431$ on LLaMA CoNLL (vs.\\ logprob $\\rho{=}0.307$, $\\Delta{=}{+}0.124$), and the gap \\textit{widens} at $N{=}16$ ($\\Delta{=}{+}0.153$) because structural signals continue to benefit from additional pairwise evidence while logprob does not.\nFor sample selection, additional samples increase the oracle upper bound---more draws raise the probability of a high-quality candidate---but signal-based selection remains flat because the selector's inability to identify the best candidate is a granularity limitation, not a sample size limitation.\nThe practical implication is that $N{=}8$ captures most of the achievable quality estimation benefit; further scaling widens rather than closes the correlation-selection gap absent stronger per-sample selectors.\n\n\\section{Bootstrap CI for Signal Comparisons}\\label{app:bootstrap_signal}\n\nTable~\\ref{tab:bootstrap_signal_ci} reports bootstrap confidence intervals for individual signal $\\rho$ and pairwise $\\Delta\\rho$ on SciERC NER ($N{=}8$, $n{=}529$, $B{=}10{,}000$, seed${=}42$).\nThe SJ--logprob gap ($\\Delta\\rho{=}{+}0.155$) is clearly significant, confirming the structural advantage reported in \\S\\ref{sec:qe_results}.\nThe Voting--SJ gap ($\\Delta\\rho{=}{+}0.019$) is not significant, indicating that these two structural signals perform comparably.\nThe SJ--EM gap ($\\Delta\\rho{=}{+}0.065$) is borderline significant, with the CI lower bound at $+0.003$ and upper bound at $+0.130$.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Bootstrap 95\\% CIs for signal $\\rho$ on SciERC NER ($N{=}8$, $n{=}529$, $B{=}10{,}000$, seed${=}42$). Top: individual signals. Bottom: pairwise $\\Delta\\rho$; ``Sig.'' indicates whether the 95\\% CI excludes zero.}\n\\label{tab:bootstrap_signal_ci}\n\\begin{tabular}{lcc}\n\\toprule\nSignal & $\\rho$ & 95\\% CI \\\\\n\\midrule\nVoting Conf. & +0.379 & [+0.299, +0.456] \\\\\nSoft Jaccard & +0.360 & [+0.277, +0.437] \\\\\nExact Match & +0.295 & [+0.212, +0.371] \\\\\nFleiss' $\\kappa$ & +0.267 & [+0.176, +0.354] \\\\\nLog-prob & +0.205 & [+0.119, +0.291] \\\\\n\\bottomrule\n\\end{tabular}\n\n\\vspace{0.5em}\n\n\\begin{tabular}{lccc}\n\\toprule\nComparison & $\\Delta\\rho$ & 95\\% CI & Sig. \\\\\n\\midrule\nSJ $-$ Logprob & +0.155 & [+0.074, +0.234] & Yes \\\\\nVoting $-$ SJ & +0.019 & [$-$0.033, +0.073] & No \\\\\nSJ $-$ EM & +0.065 & [+0.003, +0.130] & Yes$^\\dagger$ \\\\\n\\bottomrule\n\\end{tabular}\n\n\\smallskip\n{\\footnotesize $^\\dagger$Borderline significant (CI barely excludes zero).}\n\\end{table}\n",
      "numLines": 230,
      "startLine": 1,
      "totalLines": 230
    }
  },
  "sourceToolAssistantUUID": "220ff36d-8a8d-4644-80f0-3e027ea6966d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_1_68ddc296",
  "sessionId": "8e0e70e7-e72a-426a-9f89-26576a55a64e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Tool result

_source line 50 · 2026-05-15T03:58:52.539Z_

<details><summary>↩ Tool result · `toolu_016p6MUsRwpnVx4H4cJeT7Za`</summary>

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
11	\textbf{WNUT-17} \cite{derczynski2017wnut} consists of 1{,}287 social media instances with emerging entities, used to probe method boundaries (54\% zero F1).
12	
13	\paragraph{Models and sampling.}
14	Both \textbf{Qwen3-8B} and \textbf{LLaMA-3.1-8B-Instruct} are fine-tuned with LoRA (rank$=$32, $\alpha{=}64$) for 5 epochs using LLaMA Factory under identical training procedures, ensuring cross-model comparisons reflect architectural differences rather than training confounds.
15	We draw $N{=}8$ samples at $T{=}1.0$ (primary), with $N{=}16$ for scaling experiments.\footnote{$N{=}16$ results for CoNLL (Qwen) and SciERC (LLaMA) are in Table~\ref{tab:robustness} (Appendix~\ref{app:robustness}).}
16	Quality estimation uses Spearman $\rho$ and AUROC; downstream utility uses best-of-$N$ selection F1 with exact span matching (NER) and head-tail-label matching (RE).
17	Inference uses vLLM with constrained decoding \cite{willard2023guided}.
18	
19	%% ============================================================
20	\subsection{Quality Estimation Results}
21	\label{sec:qe_results}
22	
23	\begin{table*}[t]
24	\centering
25	\small
26	\caption{Quality estimation across tasks and models (Spearman $\rho$ and AUROC). Best value per block and column in \textbf{bold}. SciERC evaluates joint NER (6 types) and RE (7 types); CoNLL evaluates NER (4 types). $N{=}8$ results use seed${=}42$; $N{=}16$ results are averaged across seeds \{42, 123, 456\}.}
27	\label{tab:quality_estimation}
28	\begin{tabular}{ll cc cc cc cc}
29	\toprule
30	& & \multicolumn{2}{c}{\textbf{SciERC NER}} & \multicolumn{2}{c}{\textbf{SciERC RE}} & \multicolumn{2}{c}{\textbf{CoNLL (Qwen)}} & \multicolumn{2}{c}{\textbf{CoNLL (LLaMA)}} \\
31	\cmidrule(lr){3-4} \cmidrule(lr){5-6} \cmidrule(lr){7-8} \cmidrule(lr){9-10}
32	Signal & Family & $\rho$ & AUC & $\rho$ & AUC & $\rho$ & AUC & $\rho$ & AUC \\
33	\midrule
34	\multicolumn{10}{l}{\textit{$N{=}8$}} \\
35	Voting Conf. & Structural & \textbf{.379} & .684 & \textbf{.350} & .693 & .424 & .789 & .426 & .709 \\
36	Soft Jaccard  & Structural & .360 & .692 & .250 & .670 & .436 & .801 & \textbf{.431} & .704 \\
37	Fleiss' $\kappa$ & Surface & .267 & .629 & .275 & .609 & .400 & .774 & .428 & .703 \\
38	Exact Match  & Surface    & .295 & \textbf{.749} & .134 & \textbf{.706} & \textbf{.451} & \textbf{.816} & \textbf{.431} & .705 \\
39	Log-prob     & Model      & .205 & .578 & .266 & .600 & .316 & .753 & .307 & \textbf{.761} \\
40	\midrule
41	\multicolumn{10}{l}{\textit{$N{=}16$ (3-seed)}} \\
42	Voting Conf. & Structural & & & & & & & .458${\pm}$.003 & \\
43	Soft Jaccard  & Structural & & & & & & & \textbf{.463${\pm}$.007} & \\
44	Fleiss' $\kappa$ & Surface & & & & & & & .455${\pm}$.006 & \\
45	Exact Match  & Surface    & & & & & & & .460${\pm}$.008 & \\
46	Log-prob     & Model      & & & & & & & .310${\pm}$.005 & \\
47	\bottomrule
48	\end{tabular}
49	\end{table*}
50	
51	\begin{figure*}[t]
52	\centering
53	\includegraphics[width=\textwidth]{fig_signal_heatmap}
54	\caption{Quality estimation heatmap (Spearman $\rho$) across five signals and four configurations. Left: full evaluation set; right: conditional set (non-zero F1 instances). On the full set, structural signals dominate on SciERC while all signals converge on CoNLL. On the conditional set, EM emerges as the strongest signal on both NER ($\rho{=}0.360$) and RE ($\rho{=}0.417$), while logprob RE collapses to near-zero ($\rho{=}0.011$).}
55	\label{fig:signal_heatmap}
56	\end{figure*}
57	
58	Table~\ref{tab:quality_estimation} presents rank correlation ($\rho$) and AUROC for five confidence signals across tasks and models.
59	
60	\paragraph{Structural signals dominate on complex schemas.}
61	On SciERC NER, Voting achieves $\rho{=}0.379$ and SJ $\rho{=}0.360$, both outperforming surface ($\rho{\leq}0.295$) and logprob ($\rho{=}0.205$).
62	The structural advantage persists on RE (Voting $\rho{=}0.350$), though all signals weaken due to the 44\% zero-F1 floor effect.
63	Entity voting and SJ show moderate instance-level correlation (NER: $\rho{=}0.659$; RE: $\rho{=}0.605$), indicating information overlap but not redundancy; their differential behavior across difficulty levels reflects the complementary granularity of entity-level frequency vs.\ span-level set overlap.
64	While the best $\rho{=}0.38$ (Voting) explains approximately 14\% of F1 variance, the best AUROC reaches 0.749 (EM), indicating strong binary discriminative power for the quality/failure classification most relevant to practitioners in quality-aware routing.\footnote{For context, semantic entropy achieves AUROC $\approx$ 0.75--0.85 on discrete-answer QA tasks \cite{kuhn2023semantic}; direct comparison is complicated by the fundamentally different output spaces of structured IE versus closed-form QA.}
65	Bootstrap CIs for signal pair differences on SciERC NER ($N{=}8$): SJ$-$logprob $\Delta\rho{=}{+}0.155$ [+0.074, +0.234]; Voting$-$SJ $\Delta\rho{=}{+}0.019$ [$-$0.033, +0.073]; SJ$-$EM $\Delta\rho{=}{+}0.065$ [+0.003, +0.130].
66	The SJ advantage over logprob is significant, while the Voting--SJ gap is not; the SJ--EM difference is marginal (CI lower bound +0.003; see Table~\ref{tab:bootstrap_signal_ci}, Appendix~\ref{app:bootstrap_signal} for individual signal CIs).
67	
68	\paragraph{$\rho$--AUROC dissociation.}
69	On NER, EM leads AUROC (0.749) despite ranking third in $\rho$ (0.295); on RE, EM achieves the highest AUROC (0.706) while ranking last in $\rho$ (0.134).
70	Binary agreement provides clean separation between reliable and unreliable instances, while structural signals capture finer-grained quality variation.
71	On CoNLL with LLaMA, logprob achieves the highest AUROC (0.761) yet the lowest $\rho$ (0.307), confirming this dissociation across datasets.
72	
73	\paragraph{Signal rankings shift with task difficulty.}
74	On CoNLL (greedy F1${\approx}$0.91), EM leads ($\rho{=}0.451$, AUROC${=}0.816$), surpassing SJ and Voting.
75	When most samples are near-correct, binary agreement captures remaining variance more efficiently than set-level similarity.
76	This reversal---EM${>}$SJ on easy tasks vs.\ SJ${>}$EM on hard tasks---demonstrates that optimal signal choice depends on task difficulty.
77	Cross-model stability is strong: SJ achieves $\rho{=}0.436$ (Qwen) vs.\ $0.431$ (LLaMA) on CoNLL ($\Delta{=}0.005$, within 3-seed $\sigma{\approx}0.007$).
78	On WNUT-17, where 54\% of instances receive zero F1, full-set correlations are misleading: voting achieves $\rho{=}0.724$ (AUROC${=}0.913$), but this is entirely driven by the zero/non-zero boundary (conditional $\rho{=}0.038$, n.s.; Table~\ref{tab:wnut}).
79	Logprob exhibits strong \textit{negative} correlation ($\rho{=}{-}0.410$, AUROC${=}0.219$), indicating that higher model confidence associates with lower extraction quality on this noisy domain---further undermining logprob as a general-purpose IE quality signal.
80	On the conditional set, all signals collapse toward weak or non-significant correlations ($\rho{\leq}0.35$), with SJ achieving only $\rho{=}0.089$ ($p{=}0.020$) on the full set---suggesting a capability boundary beyond which consistency signals capture binary success/failure but not quality gradation.
81	
82	\paragraph{Conditional filtering.}
83	Filtering to non-zero F1 instances reshuffles rankings (Figure~\ref{fig:signal_heatmap}, right).
84	EM emerges as the strongest conditional signal on both NER ($\rho{=}0.360$) and RE ($\rho{=}0.417$), while Voting and FK drop substantially (Voting NER: $0.379{\to}0.300$; FK NER: $0.267{\to}0.176$).
85	Logprob RE collapses to $\rho{=}0.011$, confirming its full-set correlation was driven by zero/non-zero separation.
86	This creates a natural complementarity: Voting and SJ are preferred on the full set, while EM provides the most precise ranking within the non-trivial subset (see Appendix~\ref{app:additional} for details).
87	
88	%% ============================================================
89	\subsection{The Correlation-Selection Gap}
90	\label{sec:selection_gap}
91	
92	\begin{figure*}[t]
93	\centering
94	\includegraphics[width=\textwidth]{fig_selection_gap}
95	\caption{The correlation-selection gap on SciERC ($N{=}8$, $T{=}1.0$). Left: NER; right: RE. Bars show best-of-$N$ selection F1; the line marks quality estimation $\rho$. Despite $\rho$ up to 0.38, no signal reliably surpasses greedy on either task ($p{=}0.39$ for NER logprob, the best signal). Dashed line indicates oracle upper bound.}
96	\label{fig:selection_gap}
97	\end{figure*}
98	
99	\begin{table}[t]
100	\centering
101	\small
102	\caption{Best-of-$N$ selection F1 on SciERC ($N{=}8$, $T{=}1.0$). Best non-oracle result per column in \textbf{bold}. EM is omitted because exact-match plurality is degenerate in structured IE: with $N{=}8$, the probability of two identical structured outputs is negligible.}
103	\label{tab:selection}
104	\begin{tabular}{lcc}
105	\toprule
106	Method & NER F1 & RE F1 \\
107	\midrule
108	Oracle & 0.776 & 0.585 \\
109	\midrule
110	Log-prob           & \textbf{0.650} & 0.395 \\
111	Soft Jaccard       & 0.645 & 0.386 \\
112	Voting             & 0.634 & 0.359 \\
113	Exact Match        & ---   & ---   \\
114	\midrule
115	Greedy ($T{=}0$)   & 0.644 & \textbf{0.404} \\
116	Random             & 0.608 & 0.354 \\
117	\bottomrule
118	\end{tabular}
119	\end{table}
120	
121	Despite strong quality estimation, confidence signals yield limited gains when used for best-of-$N$ selection (Table~\ref{tab:selection}, Figure~\ref{fig:selection_gap}).
122	
123	\paragraph{No signal reliably surpasses greedy.}
124	We exclude 22 instances with empty gold annotations, yielding $n{=}529$ for statistical analysis.
125	We evaluate statistical significance using instance-level paired bootstrap resampling ($B{=}10{,}000$, with replacement) over these instances, reporting 95\% percentile CIs.
126	The three random seeds (42, 123, 456) refer to independent inference runs; we average $\rho$ across seeds and report the bootstrap $p$-value of the paired difference (best signal vs.\ greedy).
127	On NER, the oracle (0.776) reveals 13.2~pp of headroom above greedy (0.644).
128	Logprob achieves the highest selection F1 (0.650, +0.6~pp), but this is not statistically significant ($p{=}0.39$; 95\% CI: [$-$3.0, +4.2]~pp; Cohen's $d{=}0.038$; sign test: 61W/70L, win\%${=}$46.6\%).
129	On RE, the gap is complete: the best signal (logprob, 0.395) falls below greedy (0.404, $-0.9$\,pp, $p{=}0.80$), while 18.1~pp of oracle headroom remains.
130	Voting ($\rho{=}0.379$, the best quality estimator) selects to only 0.634 on NER---\textit{below} greedy.
131	The correlation-selection gap is consistent across all six tested configurations (Table~\ref{tab:cross_selection}), with no signal significantly outperforming greedy in any setting.
132	
133	\paragraph{Quality estimation $\neq$ output selection.}
134	Instance-level confidence signals predict \textit{which inputs} the model handles reliably, not \textit{which output} among $N$ candidates is best.
135	When per-sample variance is low relative to instance-level difficulty, even perfect quality estimation cannot discriminate among near-identical candidates.
136	This gap has direct consequences for test-time scaling in IE \cite{brown2024monkeys, snell2024scaling}: closing it likely requires per-sample signals such as trained verifiers \cite{cobbe2021verifiers}.
137	
138	%% ============================================================
139	\subsection{Robustness}
140	\label{sec:robustness_main}
141	
142	Consistency-based signals (SJ, Voting, FK) show robust performance across $T{\in}\{0.7, 1.0\}$; logprob temperature sensitivity remains uncharacterized due to unavailable $T{=}0.7$ data (Table~\ref{tab:robustness}, Appendix~\ref{app:robustness}).
143	SJ NER $\rho$ shifts by only 0.028 between $T{=}0.7$ and $T{=}1.0$ (bootstrap CI includes zero).
144	Doubling from $N{=}8$ to $N{=}16$ yields sublinear gains: SJ improves by $+0.052$ on Qwen SciERC NER, while logprob is approximately $N$-invariant ($\Delta\rho{\leq}0.021$).
145	The structural-over-logprob advantage is consistent across tested model families, holding across all four $N{=}16$ settings ($\Delta\rho{=}{+}0.135$ to ${+}0.175$).
146	NER signals are reasonably well-calibrated (ECE 0.069--0.096; Appendix~\ref{app:calibration}), while RE exhibits greater miscalibration (ECE 0.109--0.339).
147	For RE at $N{=}16$, SJ, FK, and logprob all plateau at $\rho{\approx}0.28$, suggesting compound errors impose a ceiling.
148	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "44e9f231-a78d-4358-99ba-1f565bd74bdc",
  "isSidechain": false,
  "promptId": "06c85d14-4a07-4193-8916-587ad0c60656",
  "type": "user",
  "uuid": "2eeaed6e-8b0f-4bb3-9f13-b5ac3bac35a2",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex",
      "content": "\\section{Experiments}\n\\label{sec:experiments}\n\n\\subsection{Experimental Setup}\n\\label{sec:setup}\n\n\\paragraph{Datasets.}\nWe evaluate on three English IE benchmarks spanning a difficulty gradient.\n\\textbf{SciERC} \\cite{luan2018scierc} contains 551 test instances annotated for joint NER (6 types) and RE (7 types).\n\\textbf{CoNLL-2003} \\cite{tjongkimsang2003conll} provides 3{,}453 test sentences with 4 entity types, where models achieve ${\\approx}$91\\% micro F1.\n\\textbf{WNUT-17} \\cite{derczynski2017wnut} consists of 1{,}287 social media instances with emerging entities, used to probe method boundaries (54\\% zero F1).\n\n\\paragraph{Models and sampling.}\nBoth \\textbf{Qwen3-8B} and \\textbf{LLaMA-3.1-8B-Instruct} are fine-tuned with LoRA (rank$=$32, $\\alpha{=}64$) for 5 epochs using LLaMA Factory under identical training procedures, ensuring cross-model comparisons reflect architectural differences rather than training confounds.\nWe draw $N{=}8$ samples at $T{=}1.0$ (primary), with $N{=}16$ for scaling experiments.\\footnote{$N{=}16$ results for CoNLL (Qwen) and SciERC (LLaMA) are in Table~\\ref{tab:robustness} (Appendix~\\ref{app:robustness}).}\nQuality estimation uses Spearman $\\rho$ and AUROC; downstream utility uses best-of-$N$ selection F1 with exact span matching (NER) and head-tail-label matching (RE).\nInference uses vLLM with constrained decoding \\cite{willard2023guided}.\n\n%% ============================================================\n\\subsection{Quality Estimation Results}\n\\label{sec:qe_results}\n\n\\begin{table*}[t]\n\\centering\n\\small\n\\caption{Quality estimation across tasks and models (Spearman $\\rho$ and AUROC). Best value per block and column in \\textbf{bold}. SciERC evaluates joint NER (6 types) and RE (7 types); CoNLL evaluates NER (4 types). $N{=}8$ results use seed${=}42$; $N{=}16$ results are averaged across seeds \\{42, 123, 456\\}.}\n\\label{tab:quality_estimation}\n\\begin{tabular}{ll cc cc cc cc}\n\\toprule\n& & \\multicolumn{2}{c}{\\textbf{SciERC NER}} & \\multicolumn{2}{c}{\\textbf{SciERC RE}} & \\multicolumn{2}{c}{\\textbf{CoNLL (Qwen)}} & \\multicolumn{2}{c}{\\textbf{CoNLL (LLaMA)}} \\\\\n\\cmidrule(lr){3-4} \\cmidrule(lr){5-6} \\cmidrule(lr){7-8} \\cmidrule(lr){9-10}\nSignal & Family & $\\rho$ & AUC & $\\rho$ & AUC & $\\rho$ & AUC & $\\rho$ & AUC \\\\\n\\midrule\n\\multicolumn{10}{l}{\\textit{$N{=}8$}} \\\\\nVoting Conf. & Structural & \\textbf{.379} & .684 & \\textbf{.350} & .693 & .424 & .789 & .426 & .709 \\\\\nSoft Jaccard  & Structural & .360 & .692 & .250 & .670 & .436 & .801 & \\textbf{.431} & .704 \\\\\nFleiss' $\\kappa$ & Surface & .267 & .629 & .275 & .609 & .400 & .774 & .428 & .703 \\\\\nExact Match  & Surface    & .295 & \\textbf{.749} & .134 & \\textbf{.706} & \\textbf{.451} & \\textbf{.816} & \\textbf{.431} & .705 \\\\\nLog-prob     & Model      & .205 & .578 & .266 & .600 & .316 & .753 & .307 & \\textbf{.761} \\\\\n\\midrule\n\\multicolumn{10}{l}{\\textit{$N{=}16$ (3-seed)}} \\\\\nVoting Conf. & Structural & & & & & & & .458${\\pm}$.003 & \\\\\nSoft Jaccard  & Structural & & & & & & & \\textbf{.463${\\pm}$.007} & \\\\\nFleiss' $\\kappa$ & Surface & & & & & & & .455${\\pm}$.006 & \\\\\nExact Match  & Surface    & & & & & & & .460${\\pm}$.008 & \\\\\nLog-prob     & Model      & & & & & & & .310${\\pm}$.005 & \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table*}\n\n\\begin{figure*}[t]\n\\centering\n\\includegraphics[width=\\textwidth]{fig_signal_heatmap}\n\\caption{Quality estimation heatmap (Spearman $\\rho$) across five signals and four configurations. Left: full evaluation set; right: conditional set (non-zero F1 instances). On the full set, structural signals dominate on SciERC while all signals converge on CoNLL. On the conditional set, EM emerges as the strongest signal on both NER ($\\rho{=}0.360$) and RE ($\\rho{=}0.417$), while logprob RE collapses to near-zero ($\\rho{=}0.011$).}\n\\label{fig:signal_heatmap}\n\\end{figure*}\n\nTable~\\ref{tab:quality_estimation} presents rank correlation ($\\rho$) and AUROC for five confidence signals across tasks and models.\n\n\\paragraph{Structural signals dominate on complex schemas.}\nOn SciERC NER, Voting achieves $\\rho{=}0.379$ and SJ $\\rho{=}0.360$, both outperforming surface ($\\rho{\\leq}0.295$) and logprob ($\\rho{=}0.205$).\nThe structural advantage persists on RE (Voting $\\rho{=}0.350$), though all signals weaken due to the 44\\% zero-F1 floor effect.\nEntity voting and SJ show moderate instance-level correlation (NER: $\\rho{=}0.659$; RE: $\\rho{=}0.605$), indicating information overlap but not redundancy; their differential behavior across difficulty levels reflects the complementary granularity of entity-level frequency vs.\\ span-level set overlap.\nWhile the best $\\rho{=}0.38$ (Voting) explains approximately 14\\% of F1 variance, the best AUROC reaches 0.749 (EM), indicating strong binary discriminative power for the quality/failure classification most relevant to practitioners in quality-aware routing.\\footnote{For context, semantic entropy achieves AUROC $\\approx$ 0.75--0.85 on discrete-answer QA tasks \\cite{kuhn2023semantic}; direct comparison is complicated by the fundamentally different output spaces of structured IE versus closed-form QA.}\nBootstrap CIs for signal pair differences on SciERC NER ($N{=}8$): SJ$-$logprob $\\Delta\\rho{=}{+}0.155$ [+0.074, +0.234]; Voting$-$SJ $\\Delta\\rho{=}{+}0.019$ [$-$0.033, +0.073]; SJ$-$EM $\\Delta\\rho{=}{+}0.065$ [+0.003, +0.130].\nThe SJ advantage over logprob is significant, while the Voting--SJ gap is not; the SJ--EM difference is marginal (CI lower bound +0.003; see Table~\\ref{tab:bootstrap_signal_ci}, Appendix~\\ref{app:bootstrap_signal} for individual signal CIs).\n\n\\paragraph{$\\rho$--AUROC dissociation.}\nOn NER, EM leads AUROC (0.749) despite ranking third in $\\rho$ (0.295); on RE, EM achieves the highest AUROC (0.706) while ranking last in $\\rho$ (0.134).\nBinary agreement provides clean separation between reliable and unreliable instances, while structural signals capture finer-grained quality variation.\nOn CoNLL with LLaMA, logprob achieves the highest AUROC (0.761) yet the lowest $\\rho$ (0.307), confirming this dissociation across datasets.\n\n\\paragraph{Signal rankings shift with task difficulty.}\nOn CoNLL (greedy F1${\\approx}$0.91), EM leads ($\\rho{=}0.451$, AUROC${=}0.816$), surpassing SJ and Voting.\nWhen most samples are near-correct, binary agreement captures remaining variance more efficiently than set-level similarity.\nThis reversal---EM${>}$SJ on easy tasks vs.\\ SJ${>}$EM on hard tasks---demonstrates that optimal signal choice depends on task difficulty.\nCross-model stability is strong: SJ achieves $\\rho{=}0.436$ (Qwen) vs.\\ $0.431$ (LLaMA) on CoNLL ($\\Delta{=}0.005$, within 3-seed $\\sigma{\\approx}0.007$).\nOn WNUT-17, where 54\\% of instances receive zero F1, full-set correlations are misleading: voting achieves $\\rho{=}0.724$ (AUROC${=}0.913$), but this is entirely driven by the zero/non-zero boundary (conditional $\\rho{=}0.038$, n.s.; Table~\\ref{tab:wnut}).\nLogprob exhibits strong \\textit{negative} correlation ($\\rho{=}{-}0.410$, AUROC${=}0.219$), indicating that higher model confidence associates with lower extraction quality on this noisy domain---further undermining logprob as a general-purpose IE quality signal.\nOn the conditional set, all signals collapse toward weak or non-significant correlations ($\\rho{\\leq}0.35$), with SJ achieving only $\\rho{=}0.089$ ($p{=}0.020$) on the full set---suggesting a capability boundary beyond which consistency signals capture binary success/failure but not quality gradation.\n\n\\paragraph{Conditional filtering.}\nFiltering to non-zero F1 instances reshuffles rankings (Figure~\\ref{fig:signal_heatmap}, right).\nEM emerges as the strongest conditional signal on both NER ($\\rho{=}0.360$) and RE ($\\rho{=}0.417$), while Voting and FK drop substantially (Voting NER: $0.379{\\to}0.300$; FK NER: $0.267{\\to}0.176$).\nLogprob RE collapses to $\\rho{=}0.011$, confirming its full-set correlation was driven by zero/non-zero separation.\nThis creates a natural complementarity: Voting and SJ are preferred on the full set, while EM provides the most precise ranking within the non-trivial subset (see Appendix~\\ref{app:additional} for details).\n\n%% ============================================================\n\\subsection{The Correlation-Selection Gap}\n\\label{sec:selection_gap}\n\n\\begin{figure*}[t]\n\\centering\n\\includegraphics[width=\\textwidth]{fig_selection_gap}\n\\caption{The correlation-selection gap on SciERC ($N{=}8$, $T{=}1.0$). Left: NER; right: RE. Bars show best-of-$N$ selection F1; the line marks quality estimation $\\rho$. Despite $\\rho$ up to 0.38, no signal reliably surpasses greedy on either task ($p{=}0.39$ for NER logprob, the best signal). Dashed line indicates oracle upper bound.}\n\\label{fig:selection_gap}\n\\end{figure*}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Best-of-$N$ selection F1 on SciERC ($N{=}8$, $T{=}1.0$). Best non-oracle result per column in \\textbf{bold}. EM is omitted because exact-match plurality is degenerate in structured IE: with $N{=}8$, the probability of two identical structured outputs is negligible.}\n\\label{tab:selection}\n\\begin{tabular}{lcc}\n\\toprule\nMethod & NER F1 & RE F1 \\\\\n\\midrule\nOracle & 0.776 & 0.585 \\\\\n\\midrule\nLog-prob           & \\textbf{0.650} & 0.395 \\\\\nSoft Jaccard       & 0.645 & 0.386 \\\\\nVoting             & 0.634 & 0.359 \\\\\nExact Match        & ---   & ---   \\\\\n\\midrule\nGreedy ($T{=}0$)   & 0.644 & \\textbf{0.404} \\\\\nRandom             & 0.608 & 0.354 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nDespite strong quality estimation, confidence signals yield limited gains when used for best-of-$N$ selection (Table~\\ref{tab:selection}, Figure~\\ref{fig:selection_gap}).\n\n\\paragraph{No signal reliably surpasses greedy.}\nWe exclude 22 instances with empty gold annotations, yielding $n{=}529$ for statistical analysis.\nWe evaluate statistical significance using instance-level paired bootstrap resampling ($B{=}10{,}000$, with replacement) over these instances, reporting 95\\% percentile CIs.\nThe three random seeds (42, 123, 456) refer to independent inference runs; we average $\\rho$ across seeds and report the bootstrap $p$-value of the paired difference (best signal vs.\\ greedy).\nOn NER, the oracle (0.776) reveals 13.2~pp of headroom above greedy (0.644).\nLogprob achieves the highest selection F1 (0.650, +0.6~pp), but this is not statistically significant ($p{=}0.39$; 95\\% CI: [$-$3.0, +4.2]~pp; Cohen's $d{=}0.038$; sign test: 61W/70L, win\\%${=}$46.6\\%).\nOn RE, the gap is complete: the best signal (logprob, 0.395) falls below greedy (0.404, $-0.9$\\,pp, $p{=}0.80$), while 18.1~pp of oracle headroom remains.\nVoting ($\\rho{=}0.379$, the best quality estimator) selects to only 0.634 on NER---\\textit{below} greedy.\nThe correlation-selection gap is consistent across all six tested configurations (Table~\\ref{tab:cross_selection}), with no signal significantly outperforming greedy in any setting.\n\n\\paragraph{Quality estimation $\\neq$ output selection.}\nInstance-level confidence signals predict \\textit{which inputs} the model handles reliably, not \\textit{which output} among $N$ candidates is best.\nWhen per-sample variance is low relative to instance-level difficulty, even perfect quality estimation cannot discriminate among near-identical candidates.\nThis gap has direct consequences for test-time scaling in IE \\cite{brown2024monkeys, snell2024scaling}: closing it likely requires per-sample signals such as trained verifiers \\cite{cobbe2021verifiers}.\n\n%% ============================================================\n\\subsection{Robustness}\n\\label{sec:robustness_main}\n\nConsistency-based signals (SJ, Voting, FK) show robust performance across $T{\\in}\\{0.7, 1.0\\}$; logprob temperature sensitivity remains uncharacterized due to unavailable $T{=}0.7$ data (Table~\\ref{tab:robustness}, Appendix~\\ref{app:robustness}).\nSJ NER $\\rho$ shifts by only 0.028 between $T{=}0.7$ and $T{=}1.0$ (bootstrap CI includes zero).\nDoubling from $N{=}8$ to $N{=}16$ yields sublinear gains: SJ improves by $+0.052$ on Qwen SciERC NER, while logprob is approximately $N$-invariant ($\\Delta\\rho{\\leq}0.021$).\nThe structural-over-logprob advantage is consistent across tested model families, holding across all four $N{=}16$ settings ($\\Delta\\rho{=}{+}0.135$ to ${+}0.175$).\nNER signals are reasonably well-calibrated (ECE 0.069--0.096; Appendix~\\ref{app:calibration}), while RE exhibits greater miscalibration (ECE 0.109--0.339).\nFor RE at $N{=}16$, SJ, FK, and logprob all plateau at $\\rho{\\approx}0.28$, suggesting compound errors impose a ceiling.\n",
      "numLines": 148,
      "startLine": 1,
      "totalLines": 148
    }
  },
  "sourceToolAssistantUUID": "44e9f231-a78d-4358-99ba-1f565bd74bdc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_1_68ddc296",
  "sessionId": "8e0e70e7-e72a-426a-9f89-26576a55a64e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Tool call

_source line 51 · 2026-05-15T03:58:53.063Z_

<details open><summary>🔧 Tool call — Read · `toolu_01AKLs973bCgYvopzgG1TXwD`</summary>

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
  "parentUuid": "2eeaed6e-8b0f-4bb3-9f13-b5ac3bac35a2",
  "isSidechain": false,
  "requestId": "req_011Cb3gekhNWyzyow6auZ6L1",
  "type": "assistant",
  "uuid": "6c595994-b563-418b-9a97-40f5138c49f8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_1_68ddc296",
  "sessionId": "8e0e70e7-e72a-426a-9f89-26576a55a64e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Er5EDNuwXGiMqkng4nsnq6",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 4243,
      "cache_creation_input_tokens": 1431,
      "cache_read_input_tokens": 33692,
      "output_tokens": 538,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1431,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 4243,
          "output_tokens": 538,
          "cache_read_input_tokens": 33692,
          "cache_creation_input_tokens": 1431,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1431
          },
          "type": "message"
        }
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

_source line 52 · 2026-05-15T03:58:53.069Z_

<details><summary>↩ Tool result · `toolu_01AKLs973bCgYvopzgG1TXwD`</summary>

```text
1	\section{Discussion}\label{sec:discussion}
2	
3	\paragraph{Practical recommendations.}
4	For per-instance quality ranking, entity voting provides the strongest rank correlation ($\rho{=}0.38$, Table~\ref{tab:quality_estimation}), though exact match leads binary discrimination on SciERC (AUROC${=}0.749$).
5	When temperature or cross-condition robustness is required, SJ is preferable: its temperature sensitivity is small with bootstrap CIs including zero (Table~\ref{tab:robustness}).
6	Under conditional filtering, EM leads on both NER and RE ($\rho{=}0.360$, $0.417$), extending binary-agreement advantages to the within-capability regime.
7	Signal rankings depend on task difficulty: EM dominates on easy tasks (CoNLL, F1${\approx}$0.91), Voting and SJ dominate on hard tasks (SciERC, F1$\,{\approx}\,$0.66), and when model capability is insufficient (WNUT-17), full-set correlations are inflated by zero/non-zero separation (Voting $\rho{=}0.724$, conditional $\rho{=}0.038$, n.s.) while all signals converge toward weak or non-significant conditional correlations.
8	This ordering is consistent across tested model families, suggesting the difficulty gradient determines which signal family is most informative.
9	Conditional filtering confirms this pattern: removing zero-F1 instances shifts effective difficulty toward the easy-task regime, and EM reclaims the lead while Voting and SJ drop substantially (Voting RE: $0.350{\to}0.241$).
10	While our NER findings are validated across three datasets, our RE conclusions rest on SciERC alone and warrant further validation.
11	
12	\paragraph{Why quality estimators fail as selectors.}
13	The four instance-level signals (Voting, SJ, FK, EM) produce a single score per input, which by construction cannot rank $N$ candidates; the consensus-proximity strategy (\S\ref{sec:evaluation}) converts them to per-sample scores, but the resulting selection performance (Table~\ref{tab:selection}) shows this conversion adds no reliable value.
14	Quality estimation ranks \textit{instances} by expected output quality; sample selection ranks \textit{candidates within a single instance}, requiring per-sample quality information that instance-level aggregation discards.
15	On SciERC NER, the random baseline (0.608) falls 3.6~pp below greedy (0.644), confirming per-instance sample variance exists; yet the oracle gap of 13.2~pp shows substantially better candidates exist, and the best signal captures only +0.6~pp ($p{=}0.39$).
16	We observe a notable $\rho$--AUROC dissociation: on SciERC, EM achieves AUROC of 0.749 (NER) and 0.706 (RE) yet ranks third or last in $\rho$, because EM${=}1$ collapses both all-correct and all-wrong instances into the same binary outcome, destroying rank order while preserving discriminative power (see Appendix~\ref{app:additional} for details).
17	The practical implication is that these signals are well-suited for routing and triage---flagging uncertain instances for human review---but not for fine-grained ranking within a difficulty tier.
18	
19	\paragraph{Why logprob fails as a selector.}
20	Log-probability---the sole per-sample signal---also fails at selection despite its structural advantage for candidate ranking.
21	Under constrained decoding, logprob primarily reflects grammar compliance rather than semantic extraction quality: a sample may have high token-level confidence yet extract the wrong relation arguments.
22	Bootstrap analysis reveals that 75\% of instance-level logprob comparisons are effectively ties (win\%${=}$46.6\%, comparable to random), consistent with the non-significant selection result ($p{=}0.39$).
23	Mean log-probability is weakly positively correlated with output length (NER: $\rho{=}0.39$; RE: $\rho{=}0.33$; Figure~\ref{fig:length_logprob_scatter}), ruling out length-penalty confounding as an explanation for logprob's selection failure.
24	NER signals are reasonably well-calibrated (ECE 0.069--0.096), but RE miscalibration (ECE 0.109--0.339; Appendix~\ref{app:calibration}) suggests that logprob confidence scores are poorly aligned with extraction quality for compound tasks.
25	Constrained decoding enforces schema compliance at the token level, which may compress per-sample diversity beyond what free-form generation would exhibit---affecting not only logprob but also consensus-proximity selection (SJ, Voting), since reduced per-sample diversity limits any selector's ability to discriminate among near-identical candidates.
26	The random baseline gap (3.6~pp) confirms meaningful variance exists even under constraints, but the correlation-selection gap may partially reflect this reduced diversity.
27	Future work should compare constrained vs.\ unconstrained decoding to disentangle these effects.
28	
29	\paragraph{Methodological implications.}
30	The decoupling of quality estimation ($\rho$), binary discrimination (AUROC), and sample selection (best-of-$N$ F1) means that evaluating confidence signals on a single metric risks selecting the wrong signal for the intended use case.
31	Effective best-of-$N$ selection likely requires per-sample signals such as trained verifiers \cite{cobbe2021verifiers} that can evaluate individual outputs rather than distribution-level properties.
32	Further $N$-scaling analysis (Appendix~\ref{app:additional}) shows that $N{=}8$ captures most achievable quality estimation benefit; additional samples widen the correlation-selection gap absent stronger selectors.
33	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6c595994-b563-418b-9a97-40f5138c49f8",
  "isSidechain": false,
  "promptId": "06c85d14-4a07-4193-8916-587ad0c60656",
  "type": "user",
  "uuid": "bb82187e-a16e-4120-bcc3-7d099a8f3e95",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex",
      "content": "\\section{Discussion}\\label{sec:discussion}\n\n\\paragraph{Practical recommendations.}\nFor per-instance quality ranking, entity voting provides the strongest rank correlation ($\\rho{=}0.38$, Table~\\ref{tab:quality_estimation}), though exact match leads binary discrimination on SciERC (AUROC${=}0.749$).\nWhen temperature or cross-condition robustness is required, SJ is preferable: its temperature sensitivity is small with bootstrap CIs including zero (Table~\\ref{tab:robustness}).\nUnder conditional filtering, EM leads on both NER and RE ($\\rho{=}0.360$, $0.417$), extending binary-agreement advantages to the within-capability regime.\nSignal rankings depend on task difficulty: EM dominates on easy tasks (CoNLL, F1${\\approx}$0.91), Voting and SJ dominate on hard tasks (SciERC, F1$\\,{\\approx}\\,$0.66), and when model capability is insufficient (WNUT-17), full-set correlations are inflated by zero/non-zero separation (Voting $\\rho{=}0.724$, conditional $\\rho{=}0.038$, n.s.) while all signals converge toward weak or non-significant conditional correlations.\nThis ordering is consistent across tested model families, suggesting the difficulty gradient determines which signal family is most informative.\nConditional filtering confirms this pattern: removing zero-F1 instances shifts effective difficulty toward the easy-task regime, and EM reclaims the lead while Voting and SJ drop substantially (Voting RE: $0.350{\\to}0.241$).\nWhile our NER findings are validated across three datasets, our RE conclusions rest on SciERC alone and warrant further validation.\n\n\\paragraph{Why quality estimators fail as selectors.}\nThe four instance-level signals (Voting, SJ, FK, EM) produce a single score per input, which by construction cannot rank $N$ candidates; the consensus-proximity strategy (\\S\\ref{sec:evaluation}) converts them to per-sample scores, but the resulting selection performance (Table~\\ref{tab:selection}) shows this conversion adds no reliable value.\nQuality estimation ranks \\textit{instances} by expected output quality; sample selection ranks \\textit{candidates within a single instance}, requiring per-sample quality information that instance-level aggregation discards.\nOn SciERC NER, the random baseline (0.608) falls 3.6~pp below greedy (0.644), confirming per-instance sample variance exists; yet the oracle gap of 13.2~pp shows substantially better candidates exist, and the best signal captures only +0.6~pp ($p{=}0.39$).\nWe observe a notable $\\rho$--AUROC dissociation: on SciERC, EM achieves AUROC of 0.749 (NER) and 0.706 (RE) yet ranks third or last in $\\rho$, because EM${=}1$ collapses both all-correct and all-wrong instances into the same binary outcome, destroying rank order while preserving discriminative power (see Appendix~\\ref{app:additional} for details).\nThe practical implication is that these signals are well-suited for routing and triage---flagging uncertain instances for human review---but not for fine-grained ranking within a difficulty tier.\n\n\\paragraph{Why logprob fails as a selector.}\nLog-probability---the sole per-sample signal---also fails at selection despite its structural advantage for candidate ranking.\nUnder constrained decoding, logprob primarily reflects grammar compliance rather than semantic extraction quality: a sample may have high token-level confidence yet extract the wrong relation arguments.\nBootstrap analysis reveals that 75\\% of instance-level logprob comparisons are effectively ties (win\\%${=}$46.6\\%, comparable to random), consistent with the non-significant selection result ($p{=}0.39$).\nMean log-probability is weakly positively correlated with output length (NER: $\\rho{=}0.39$; RE: $\\rho{=}0.33$; Figure~\\ref{fig:length_logprob_scatter}), ruling out length-penalty confounding as an explanation for logprob's selection failure.\nNER signals are reasonably well-calibrated (ECE 0.069--0.096), but RE miscalibration (ECE 0.109--0.339; Appendix~\\ref{app:calibration}) suggests that logprob confidence scores are poorly aligned with extraction quality for compound tasks.\nConstrained decoding enforces schema compliance at the token level, which may compress per-sample diversity beyond what free-form generation would exhibit---affecting not only logprob but also consensus-proximity selection (SJ, Voting), since reduced per-sample diversity limits any selector's ability to discriminate among near-identical candidates.\nThe random baseline gap (3.6~pp) confirms meaningful variance exists even under constraints, but the correlation-selection gap may partially reflect this reduced diversity.\nFuture work should compare constrained vs.\\ unconstrained decoding to disentangle these effects.\n\n\\paragraph{Methodological implications.}\nThe decoupling of quality estimation ($\\rho$), binary discrimination (AUROC), and sample selection (best-of-$N$ F1) means that evaluating confidence signals on a single metric risks selecting the wrong signal for the intended use case.\nEffective best-of-$N$ selection likely requires per-sample signals such as trained verifiers \\cite{cobbe2021verifiers} that can evaluate individual outputs rather than distribution-level properties.\nFurther $N$-scaling analysis (Appendix~\\ref{app:additional}) shows that $N{=}8$ captures most achievable quality estimation benefit; additional samples widen the correlation-selection gap absent stronger selectors.\n",
      "numLines": 33,
      "startLine": 1,
      "totalLines": 33
    }
  },
  "sourceToolAssistantUUID": "6c595994-b563-418b-9a97-40f5138c49f8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_1_68ddc296",
  "sessionId": "8e0e70e7-e72a-426a-9f89-26576a55a64e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Tool call

_source line 53 · 2026-05-15T03:58:53.864Z_

<details open><summary>🔧 Tool call — Read · `toolu_01JJKocirJ5EwWfhn9wqCfJD`</summary>

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
  "parentUuid": "bb82187e-a16e-4120-bcc3-7d099a8f3e95",
  "isSidechain": false,
  "requestId": "req_011Cb3gekhNWyzyow6auZ6L1",
  "type": "assistant",
  "uuid": "dd51b926-6462-4ddf-b28f-8dc33703a55e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_1_68ddc296",
  "sessionId": "8e0e70e7-e72a-426a-9f89-26576a55a64e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Er5EDNuwXGiMqkng4nsnq6",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 4243,
      "cache_creation_input_tokens": 1431,
      "cache_read_input_tokens": 33692,
      "output_tokens": 538,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1431,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 4243,
          "output_tokens": 538,
          "cache_read_input_tokens": 33692,
          "cache_creation_input_tokens": 1431,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1431
          },
          "type": "message"
        }
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

_source line 54 · 2026-05-15T03:58:53.869Z_

<details><summary>↩ Tool result · `toolu_01JJKocirJ5EwWfhn9wqCfJD`</summary>

```text
1	\section{Related Work}\label{sec:related}
2	
3	\paragraph{Self-consistency and test-time scaling.}
4	Self-consistency decoding \cite{wang2023selfconsistency} improves reasoning by majority voting over chain-of-thought samples, assuming a discrete answer space.
5	Extensions to free-form text use LLM-based comparison \cite{chen2024usc}, atomic sub-claim decomposition \cite{thirukovalluru2024atomic}, or cross-sample hallucination detection \cite{manakul2023selfcheckgpt}.
6	For test-time scaling, \citet{snell2024scaling} characterize compute scaling laws and \citet{brown2024monkeys} show best-of-$N$ gains across tasks.
7	Recent reward-free selectors include confidence-weighted voting \cite{taubenfeld2025cisc}, KL-based self-certainty \cite{kang2025selfcertainty}, adaptive sampling \cite{kim2026reasc}, ranked aggregation \cite{wang2025rankedvoting}, and latent-space consistency \cite{oh2025latentsc}.
8	Concurrently, \citet{feng2025optimal} and \citet{wang2025make} adapt self-consistency to difficulty-aware settings, echoing our finding that signal rankings shift with task complexity; \citet{li2025llms} propose generative self-aggregation for IE but focus on output fusion rather than confidence-based selection.
9	All of the above target reasoning/QA with discrete answers or specific aggregation strategies.
10	Our work extends self-consistency to set-valued structured outputs and identifies the correlation-selection gap: strong quality estimation ($\rho{=}0.38$) coexists with selection failure ($p{>}0.39$).
11	
12	\paragraph{Consistency for structured IE.}
13	\citet{nedellec2026consistency} study consistency--accuracy correlations for LLM-based NER/RE, corroborating our quality-estimation findings.
14	However, their work differs in three key respects: (i)~it relies on surface-level matching, explicitly acknowledging it ``overlooks semantically consistent outputs''; (ii)~it evaluates only quality estimation without studying best-of-$N$ selection, leaving the correlation-selection gap unexamined; and (iii)~it covers a single domain with hard prompting rather than a difficulty gradient across benchmarks.
15	Our Soft Jaccard signal addresses limitation (i) through type-aware bipartite matching with token-level span overlap; our selection analysis (\S\ref{sec:selection_gap}) directly addresses (ii); and our three-dataset evaluation spanning easy (CoNLL) to hard (SciERC) tasks addresses (iii).
16	CoCoA \cite{vashurin2025cocoa} fuses model confidence with inter-sample consistency for QA/summarization but does not address structured extraction.
17	Our evaluation builds on generative IE work \cite{zhou2024uniner, sainz2024gollie, josifoski2022genie, li2023codeie, wadhwa2023revisiting, wang2023instructuie} and constrained decoding \cite{willard2023guided}.
18	
19	\paragraph{Uncertainty estimation and calibration.}
20	Several surveys cover confidence estimation \cite{geng2024confidence}, selective abstention \cite{wen2025know}, uncertainty quantification \cite{xia2025survey}, and their intersection with calibration \cite{hobelsberger2025systematic} for LLMs.
21	Semantic uncertainty \cite{kuhn2023semantic} clusters generations by meaning; \citet{kossen2024semantic} distill semantic entropy into lightweight probes; P(True) \cite{kadavath2022language} queries model confidence directly; our structural signals instead measure agreement over output \textit{structure}.
22	Modern neural networks are often miscalibrated \cite{guo2017calibration, desai2020calibration}; our reliability diagrams extend calibration analysis to structured prediction.
23	Deep ensembles \cite{lakshminarayanan2017ensembles} and MC-dropout \cite{gal2016dropout} obtain uncertainty from model variation; our approach requires no model modification.
24	Prior NER uncertainty work \cite{xiao2019uncertainty, shelmanov2021active, zhang2023ener} operates within discriminative paradigms, inapplicable to generative settings.
25	Conformal prediction \cite{fisch2021conformal, angelopoulos2021conformal} provides coverage guarantees; trained verifiers \cite{cobbe2021verifiers, lightman2024verify} and reward models \cite{wang2024mathshepherd} learn per-sample scoring from labeled data.
26	Selective prediction \cite{geifman2017selective} and confidence-based IE filtering \cite{culotta2004confidence} establish the broader framework; our contribution is characterizing which signals support quality estimation vs.\ sample selection for generative IE.
27	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "dd51b926-6462-4ddf-b28f-8dc33703a55e",
  "isSidechain": false,
  "promptId": "06c85d14-4a07-4193-8916-587ad0c60656",
  "type": "user",
  "uuid": "898e7599-c973-4c90-af90-2f6767e16d4e",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/related_work.tex",
      "content": "\\section{Related Work}\\label{sec:related}\n\n\\paragraph{Self-consistency and test-time scaling.}\nSelf-consistency decoding \\cite{wang2023selfconsistency} improves reasoning by majority voting over chain-of-thought samples, assuming a discrete answer space.\nExtensions to free-form text use LLM-based comparison \\cite{chen2024usc}, atomic sub-claim decomposition \\cite{thirukovalluru2024atomic}, or cross-sample hallucination detection \\cite{manakul2023selfcheckgpt}.\nFor test-time scaling, \\citet{snell2024scaling} characterize compute scaling laws and \\citet{brown2024monkeys} show best-of-$N$ gains across tasks.\nRecent reward-free selectors include confidence-weighted voting \\cite{taubenfeld2025cisc}, KL-based self-certainty \\cite{kang2025selfcertainty}, adaptive sampling \\cite{kim2026reasc}, ranked aggregation \\cite{wang2025rankedvoting}, and latent-space consistency \\cite{oh2025latentsc}.\nConcurrently, \\citet{feng2025optimal} and \\citet{wang2025make} adapt self-consistency to difficulty-aware settings, echoing our finding that signal rankings shift with task complexity; \\citet{li2025llms} propose generative self-aggregation for IE but focus on output fusion rather than confidence-based selection.\nAll of the above target reasoning/QA with discrete answers or specific aggregation strategies.\nOur work extends self-consistency to set-valued structured outputs and identifies the correlation-selection gap: strong quality estimation ($\\rho{=}0.38$) coexists with selection failure ($p{>}0.39$).\n\n\\paragraph{Consistency for structured IE.}\n\\citet{nedellec2026consistency} study consistency--accuracy correlations for LLM-based NER/RE, corroborating our quality-estimation findings.\nHowever, their work differs in three key respects: (i)~it relies on surface-level matching, explicitly acknowledging it ``overlooks semantically consistent outputs''; (ii)~it evaluates only quality estimation without studying best-of-$N$ selection, leaving the correlation-selection gap unexamined; and (iii)~it covers a single domain with hard prompting rather than a difficulty gradient across benchmarks.\nOur Soft Jaccard signal addresses limitation (i) through type-aware bipartite matching with token-level span overlap; our selection analysis (\\S\\ref{sec:selection_gap}) directly addresses (ii); and our three-dataset evaluation spanning easy (CoNLL) to hard (SciERC) tasks addresses (iii).\nCoCoA \\cite{vashurin2025cocoa} fuses model confidence with inter-sample consistency for QA/summarization but does not address structured extraction.\nOur evaluation builds on generative IE work \\cite{zhou2024uniner, sainz2024gollie, josifoski2022genie, li2023codeie, wadhwa2023revisiting, wang2023instructuie} and constrained decoding \\cite{willard2023guided}.\n\n\\paragraph{Uncertainty estimation and calibration.}\nSeveral surveys cover confidence estimation \\cite{geng2024confidence}, selective abstention \\cite{wen2025know}, uncertainty quantification \\cite{xia2025survey}, and their intersection with calibration \\cite{hobelsberger2025systematic} for LLMs.\nSemantic uncertainty \\cite{kuhn2023semantic} clusters generations by meaning; \\citet{kossen2024semantic} distill semantic entropy into lightweight probes; P(True) \\cite{kadavath2022language} queries model confidence directly; our structural signals instead measure agreement over output \\textit{structure}.\nModern neural networks are often miscalibrated \\cite{guo2017calibration, desai2020calibration}; our reliability diagrams extend calibration analysis to structured prediction.\nDeep ensembles \\cite{lakshminarayanan2017ensembles} and MC-dropout \\cite{gal2016dropout} obtain uncertainty from model variation; our approach requires no model modification.\nPrior NER uncertainty work \\cite{xiao2019uncertainty, shelmanov2021active, zhang2023ener} operates within discriminative paradigms, inapplicable to generative settings.\nConformal prediction \\cite{fisch2021conformal, angelopoulos2021conformal} provides coverage guarantees; trained verifiers \\cite{cobbe2021verifiers, lightman2024verify} and reward models \\cite{wang2024mathshepherd} learn per-sample scoring from labeled data.\nSelective prediction \\cite{geifman2017selective} and confidence-based IE filtering \\cite{culotta2004confidence} establish the broader framework; our contribution is characterizing which signals support quality estimation vs.\\ sample selection for generative IE.\n",
      "numLines": 27,
      "startLine": 1,
      "totalLines": 27
    }
  },
  "sourceToolAssistantUUID": "dd51b926-6462-4ddf-b28f-8dc33703a55e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_1_68ddc296",
  "sessionId": "8e0e70e7-e72a-426a-9f89-26576a55a64e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Tool call

_source line 55 · 2026-05-15T03:58:54.497Z_

<details open><summary>🔧 Tool call — Read · `toolu_017i1Gt4ABhckQE8QyjCgc8i`</summary>

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
  "parentUuid": "898e7599-c973-4c90-af90-2f6767e16d4e",
  "isSidechain": false,
  "requestId": "req_011Cb3gekhNWyzyow6auZ6L1",
  "type": "assistant",
  "uuid": "6ade26b3-5117-4514-a63c-ce876b5b2fa6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_1_68ddc296",
  "sessionId": "8e0e70e7-e72a-426a-9f89-26576a55a64e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Er5EDNuwXGiMqkng4nsnq6",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 4243,
      "cache_creation_input_tokens": 1431,
      "cache_read_input_tokens": 33692,
      "output_tokens": 538,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1431,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 4243,
          "output_tokens": 538,
          "cache_read_input_tokens": 33692,
          "cache_creation_input_tokens": 1431,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1431
          },
          "type": "message"
        }
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

_source line 56 · 2026-05-15T03:58:54.506Z_

<details><summary>↩ Tool result · `toolu_017i1Gt4ABhckQE8QyjCgc8i`</summary>

```text
1	\section{Conclusion}\label{sec:conclusion}
2	
3	This work provides the first multi-family comparison of confidence signals for test-time scaling in generative information extraction.
4	By comparing five signals from three families---structural, surface, and model-internal---across NER and RE tasks of varying difficulty, we disentangle two objectives that prior work has conflated: quality estimation (ranking instances by expected performance) and sample selection (choosing the best output among $N$ candidates).
5	Our experiments on SciERC, CoNLL-2003, and WNUT-17 with Qwen3-8B and LLaMA-3.1-8B reveal that these objectives require fundamentally different signal properties.
6	
7	Three findings anchor our analysis.
8	First, consistency-based signals are effective quality estimators: entity voting achieves the strongest rank correlation ($\rho{=}0.38$) while exact match leads binary discrimination (AUROC${=}0.75$) on SciERC NER, with signal rankings depending on both task complexity and evaluation metric.
9	Second, the \textit{correlation-selection gap} shows that strong instance-level correlation does not yield substantial selection gains---no signal reliably surpasses greedy on either task (NER logprob: +0.6~pp, $p{=}0.39$; RE: $-$0.9~pp) despite 13--18~pp of oracle headroom---because instance-level signals cannot discriminate among candidates with similar consistency profiles.
10	Third, signal rankings depend on task difficulty: exact match leads on easy tasks, Soft Jaccard and voting lead on hard tasks, and when model capability is insufficient, inflated full-set correlations (driven by zero/non-zero separation) mask the collapse of all signals on the conditional set.
11	This ordering is consistent across tested model families, suggesting the difficulty gradient determines which signal family is most informative.
12	While our NER findings are validated across three datasets, our RE conclusions rest on SciERC alone and warrant further validation.
13	
14	Several directions remain open.
15	Trained verifiers or reward models could close the selection gap by learning per-sample quality discrimination that unsupervised consistency signals lack.
16	Cross-task transfer of confidence signals beyond IE---to structured prediction tasks such as semantic parsing and code generation---would test the generality of our findings.
17	Integration with conformal prediction could convert continuous confidence scores into calibrated coverage guarantees.
18	Finally, scaling analysis with larger models (70B+) and more diverse IE tasks would clarify whether increased model capability narrows or widens the correlation-selection gap.
19	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6ade26b3-5117-4514-a63c-ce876b5b2fa6",
  "isSidechain": false,
  "promptId": "06c85d14-4a07-4193-8916-587ad0c60656",
  "type": "user",
  "uuid": "082e8582-7094-4c90-b909-e99569d77bd6",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/conclusion.tex",
      "content": "\\section{Conclusion}\\label{sec:conclusion}\n\nThis work provides the first multi-family comparison of confidence signals for test-time scaling in generative information extraction.\nBy comparing five signals from three families---structural, surface, and model-internal---across NER and RE tasks of varying difficulty, we disentangle two objectives that prior work has conflated: quality estimation (ranking instances by expected performance) and sample selection (choosing the best output among $N$ candidates).\nOur experiments on SciERC, CoNLL-2003, and WNUT-17 with Qwen3-8B and LLaMA-3.1-8B reveal that these objectives require fundamentally different signal properties.\n\nThree findings anchor our analysis.\nFirst, consistency-based signals are effective quality estimators: entity voting achieves the strongest rank correlation ($\\rho{=}0.38$) while exact match leads binary discrimination (AUROC${=}0.75$) on SciERC NER, with signal rankings depending on both task complexity and evaluation metric.\nSecond, the \\textit{correlation-selection gap} shows that strong instance-level correlation does not yield substantial selection gains---no signal reliably surpasses greedy on either task (NER logprob: +0.6~pp, $p{=}0.39$; RE: $-$0.9~pp) despite 13--18~pp of oracle headroom---because instance-level signals cannot discriminate among candidates with similar consistency profiles.\nThird, signal rankings depend on task difficulty: exact match leads on easy tasks, Soft Jaccard and voting lead on hard tasks, and when model capability is insufficient, inflated full-set correlations (driven by zero/non-zero separation) mask the collapse of all signals on the conditional set.\nThis ordering is consistent across tested model families, suggesting the difficulty gradient determines which signal family is most informative.\nWhile our NER findings are validated across three datasets, our RE conclusions rest on SciERC alone and warrant further validation.\n\nSeveral directions remain open.\nTrained verifiers or reward models could close the selection gap by learning per-sample quality discrimination that unsupervised consistency signals lack.\nCross-task transfer of confidence signals beyond IE---to structured prediction tasks such as semantic parsing and code generation---would test the generality of our findings.\nIntegration with conformal prediction could convert continuous confidence scores into calibrated coverage guarantees.\nFinally, scaling analysis with larger models (70B+) and more diverse IE tasks would clarify whether increased model capability narrows or widens the correlation-selection gap.\n",
      "numLines": 19,
      "startLine": 1,
      "totalLines": 19
    }
  },
  "sourceToolAssistantUUID": "6ade26b3-5117-4514-a63c-ce876b5b2fa6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_1_68ddc296",
  "sessionId": "8e0e70e7-e72a-426a-9f89-26576a55a64e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Tool call

_source line 57 · 2026-05-15T03:58:55.405Z_

<details open><summary>🔧 Tool call — Read · `toolu_01AS68Wa9GXQzEvfwhRDJfJH`</summary>

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
  "parentUuid": "082e8582-7094-4c90-b909-e99569d77bd6",
  "isSidechain": false,
  "requestId": "req_011Cb3gekhNWyzyow6auZ6L1",
  "type": "assistant",
  "uuid": "ab7b190c-97e2-40f4-8a9f-747efb0d2d3f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_1_68ddc296",
  "sessionId": "8e0e70e7-e72a-426a-9f89-26576a55a64e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Er5EDNuwXGiMqkng4nsnq6",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 4243,
      "cache_creation_input_tokens": 1431,
      "cache_read_input_tokens": 33692,
      "output_tokens": 538,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1431,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 4243,
          "output_tokens": 538,
          "cache_read_input_tokens": 33692,
          "cache_creation_input_tokens": 1431,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1431
          },
          "type": "message"
        }
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

_source line 58 · 2026-05-15T03:58:55.411Z_

<details><summary>↩ Tool result · `toolu_01AS68Wa9GXQzEvfwhRDJfJH`</summary>

```text
1	Our evaluation covers three datasets but only one RE benchmark (SciERC), where 44\% of instances receive zero F1, compressing the discriminable range and limiting signal differentiation for relation extraction.
2	WNUT-17 confirms the capability boundary of our approach, but our positive results on formal-domain text (CoNLL, SciERC) have not been validated on informal or noisy text where models achieve non-trivial performance.
3	
4	We evaluate two model families (Qwen3-8B and LLaMA-3.1-8B), both at 8B parameters.
5	Whether our findings---particularly the correlation-selection gap and the difficulty-dependent signal ordering, which are consistent across our two tested model families---hold for larger models (70B+) or closed-source APIs remains untested.
6	Larger models may produce higher-quality and more diverse samples, potentially altering the signal landscape.
7	
8	Our analysis of selection potential uses only unsupervised signals.
9	We do not train a dedicated verifier or reward model, leaving unknown how much of the oracle headroom a supervised approach could recover.
10	
11	We evaluate at $N{=}8$ and $N{=}16$.
12	The behavior of confidence signals at larger sample sizes (e.g., $N{=}64$ or $N{=}128$) is unknown, and $N$-scaling gains are setting-dependent: SJ improves by $+0.052$ on Qwen SciERC NER but only $+0.016$ on LLaMA SciERC NER when doubling from $N{=}8$ to $N{=}16$.
13	
14	On CoNLL with LLaMA, the SJ--FK gap is only 0.003 ($\rho{=}0.431$ vs.\ $0.428$), so the structural advantage over surface signals may not generalize to all simple-schema datasets.
15	Constrained decoding (Outlines/vLLM) enforces schema compliance, potentially compressing per-sample diversity and contributing to the correlation-selection gap beyond what free-form generation would exhibit.
16	Finally, log-probability was excluded from the temperature comparison ($T{=}0.7$ vs.\ $T{=}1.0$) due to missing $T{=}0.7$ logprob data, leaving its temperature sensitivity uncharacterized.
17	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ab7b190c-97e2-40f4-8a9f-747efb0d2d3f",
  "isSidechain": false,
  "promptId": "06c85d14-4a07-4193-8916-587ad0c60656",
  "type": "user",
  "uuid": "e2c5bbd1-b419-4eae-93f1-4ec26a7e3ea6",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/limitations.tex",
      "content": "Our evaluation covers three datasets but only one RE benchmark (SciERC), where 44\\% of instances receive zero F1, compressing the discriminable range and limiting signal differentiation for relation extraction.\nWNUT-17 confirms the capability boundary of our approach, but our positive results on formal-domain text (CoNLL, SciERC) have not been validated on informal or noisy text where models achieve non-trivial performance.\n\nWe evaluate two model families (Qwen3-8B and LLaMA-3.1-8B), both at 8B parameters.\nWhether our findings---particularly the correlation-selection gap and the difficulty-dependent signal ordering, which are consistent across our two tested model families---hold for larger models (70B+) or closed-source APIs remains untested.\nLarger models may produce higher-quality and more diverse samples, potentially altering the signal landscape.\n\nOur analysis of selection potential uses only unsupervised signals.\nWe do not train a dedicated verifier or reward model, leaving unknown how much of the oracle headroom a supervised approach could recover.\n\nWe evaluate at $N{=}8$ and $N{=}16$.\nThe behavior of confidence signals at larger sample sizes (e.g., $N{=}64$ or $N{=}128$) is unknown, and $N$-scaling gains are setting-dependent: SJ improves by $+0.052$ on Qwen SciERC NER but only $+0.016$ on LLaMA SciERC NER when doubling from $N{=}8$ to $N{=}16$.\n\nOn CoNLL with LLaMA, the SJ--FK gap is only 0.003 ($\\rho{=}0.431$ vs.\\ $0.428$), so the structural advantage over surface signals may not generalize to all simple-schema datasets.\nConstrained decoding (Outlines/vLLM) enforces schema compliance, potentially compressing per-sample diversity and contributing to the correlation-selection gap beyond what free-form generation would exhibit.\nFinally, log-probability was excluded from the temperature comparison ($T{=}0.7$ vs.\\ $T{=}1.0$) due to missing $T{=}0.7$ logprob data, leaving its temperature sensitivity uncharacterized.\n",
      "numLines": 17,
      "startLine": 1,
      "totalLines": 17
    }
  },
  "sourceToolAssistantUUID": "ab7b190c-97e2-40f4-8a9f-747efb0d2d3f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_1_68ddc296",
  "sessionId": "8e0e70e7-e72a-426a-9f89-26576a55a64e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Tool call

_source line 59 · 2026-05-15T03:58:55.491Z_

<details open><summary>🔧 Tool call — Read · `toolu_01R9HEKxhwnX9D1cejLFMqhP`</summary>

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
  "parentUuid": "e2c5bbd1-b419-4eae-93f1-4ec26a7e3ea6",
  "isSidechain": false,
  "requestId": "req_011Cb3gekhNWyzyow6auZ6L1",
  "type": "assistant",
  "uuid": "220ff36d-8a8d-4644-80f0-3e027ea6966d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_1_68ddc296",
  "sessionId": "8e0e70e7-e72a-426a-9f89-26576a55a64e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Er5EDNuwXGiMqkng4nsnq6",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 4243,
      "cache_creation_input_tokens": 1431,
      "cache_read_input_tokens": 33692,
      "output_tokens": 538,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1431,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 4243,
          "output_tokens": 538,
          "cache_read_input_tokens": 33692,
          "cache_creation_input_tokens": 1431,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1431
          },
          "type": "message"
        }
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
  "lastPrompt": "[Round 1 审稿请求]: 你是 Reviewer 1，负责**方法严谨性 + 实验设计**。  ## 审稿对象 - 论文路径：`projects/struct_self_consist_ie/docs/paper/main.tex`（分节结构，各节在 `sections/` 下） - 目标 venue：**EMNLP 2026 Main Conference**（通过 ARR May 202…",
  "leafUuid": "9df3d12a-51ea-4981-9422-a7ba3c37bdad",
  "sessionId": "8e0e70e7-e72a-426a-9f89-26576a55a64e"
}
```

---


### Runtime record

_source line 61_

```json
{
  "type": "ai-title",
  "aiTitle": "Review paper on structural self-consistency for information extraction",
  "sessionId": "8e0e70e7-e72a-426a-9f89-26576a55a64e"
}
```

---


### Assistant

_source line 62 · 2026-05-15T04:00:22.234Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have read the entire paper. Let me also check the reference file for completeness and verify references. Let me also look at some of the figures via pdf_to_images for key pages.

Actually, let me now compile my review. I have a thorough understanding of the paper. Let me also verify references.

Let me also check if there are any issues with the WNUT data - the paper mentions filtering gold-empty instances (n=689 from 1287), but also says 54% zero F1. Let me calculate: 1287 - 689 = 598 gold-empty instances filtered. Then of the 689 remaining, 54% have zero F1, which would be ~372. 

Wait, there's a discrepancy here. The WNUT table shows n=689 after filtering and Cond n=334 for non-zero F1 instances, which means 355 instances have zero F1. That's 51.5%, not the 54% stated in the paper. Let me verify this calculation against what's written in the experiments section. So there's a discrepancy here—the paper claims 54% zero F1 across all 1287 instances, but my calculation shows only 51.5% when looking at the 689 instances after filtering out gold-empty cases. The question is whether that 54% figure includes the gold-empty instances as zero F1, or if there's a different way they're computing it.

It's also possible the 54% comes from a different random seed or calculation method, since they mention N=8 sampling. I'll note this as a minor inconsistency and move on to examining the technical rigor of their methods, starting with how they define soft Jaccard.

The Hungarian matching applies per-type group using max(|g_i|, |g_j|) in the denominator instead of union size, which penalizes length asymmetry. But they don't justify why they allow any span pair to match without a minimum similarity threshold—a very dissimilar match could still contribute to the score. On the Fleiss' kappa adaptation, they treat unique (text, type) tuples as binary items, but they acknowledge temperature sampling doesn't produce truly independent samples like kappa assumes. They wave this away by claiming "sufficient response diversity" without actually validating whether the independence assumption holds. The "correlation-selection gap" is their term for the mismatch between quality estimation and selection, though the definition seems to cut off here.

The distinction between per-sample and instance-level signals is clearer—they correctly note that four of five signals operate at the instance level while only logprob is per-sample. On the experimental side, both models are 8B parameters, which limits their claim about cross-model consistency to just one size class. They test N=8 and N=16, arguing N=8 captures most benefit, but they don't explore whether larger N values might reveal selection signals. They also only evaluate on SciERC, which is a narrow dataset choice.

The LoRA configuration (rank=32, α=64, 5 epochs) follows standard practice but isn't justified, and different ranks could plausibly affect sample diversity. Temperature is only tested at T=0.7 and T=1.0, with notably missing logprob data at T=0.7. They acknowledge that constrained decoding might compress per-sample diversity and could explain the correlation-selection gap, but they don't actually test this potential confound. For statistical testing, they use B=10,000 bootstrap samples, which is reasonable, though they report multiple pairwise comparisons without multiple comparison corrections like Bonferroni or FDR.

For the 5 signals tested, that's 10 pairwise comparisons, and the borderline significant SJ-EM result (CI lower bound +0.003) would likely disappear under correction. Their argument that no signal reliably surpasses greedy relies on p>0.39, but that's testing the null hypothesis of no difference—absence of evidence isn't evidence of absence, and equivalence testing or power analysis would strengthen this claim. The N=8 results use only seed=42 while N=16 uses 3 seeds, which is inconsistent, though the small variance across seeds for N=16 (σ~0.003-0.008) suggests the single seed might be acceptable. The p-values and confidence intervals are well-reported overall.

Now I'm checking the data consistency claims. The 54% zero F1 on WNUT is slightly off—the table shows 355/689 ≈ 51.5%. The ρ=0.38 and AUROC=0.75 claims in the abstract match the table values when rounded appropriately. For the oracle headroom claim, the NER difference between oracle (0.776) and greedy (0.644) is 0.132, which is about 13 percentage points.

For relation extraction, the oracle-greedy gap is 0.181 or 18.1 percentage points, confirming the "13-18 pp of oracle headroom" statement. There's a presentation issue with Table 1 being partially empty for N=16 results—the footnote mentions these are in Table 5, but they're missing from the main table. Looking at the SJ advantage claim, the text says it improves by +0.052 on Qwen SciERC NER from N=8 to N=16, and checking Table 5 shows SJ at 0.360 for N=8 and 0.412 for N=16, which is a 0.052 difference.

The paper does acknowledge the single-dataset RE limitation across multiple sections (Introduction, Discussion, Conclusion, Limitations), but there's a disconnect between the broad "Information Extraction" title and the fact that RE evidence comes from just one dataset with 44% zero F1. On the methods side, the FK independence assumption gets only a sentence of acknowledgment without empirical validation, which seems light for a methods paper. The exclusion of exact-match plurality from selection experiments is justified by the claim that identical structured outputs are negligible with N=8, but this reasoning could use empirical support. The consensus-proximity strategy appears to be cut off mid-thought.

For the instance-level signals, the consensus-proximity approach converts them to per-sample scores, but the paper doesn't explore whether alternative conversion strategies might work better. Looking at the length-confounding analysis in Figure 5, the positive correlation between length and logprob does rule out one direction of confounding, but since this is only shown on SciERC, it's not clear how general this finding is. The evaluation does include a good sanity check showing the LOO-SJ versus standard SJ difference is negligible. The core issue with the correlation-selection gap is that instance-level signals can't differentiate samples from the same input since they assign identical scores to all of them.

The paper's framing combines two separate observations: that instance-level signals inherently can't do per-sample selection, which is somewhat predictable by design, and that logprob—the only true per-sample signal—also fails because constrained decoding makes it reflect grammar compliance rather than semantic quality. The second finding is more interesting and nuanced than the first.

Now I'm evaluating the paper's overall quality. The methodology is reasonably sound with some limitations: single seed for the small sample size, missing data points, no correction for multiple comparisons, and the constrained decoding confound wasn't directly tested. The correlation-selection gap is a useful conceptual contribution, though the finding that instance-level signals can't do per-sample selection is somewhat expected. The practical value is moderate—practitioners learn that consistency signals estimate quality but don't select samples well.

The reproducibility is decent with good documentation of LoRA settings and evaluation protocols, though code and data availability aren't mentioned and the missing logprob data is concerning. I'm quite confident in this assessment given my familiarity with self-consistency, uncertainty estimation, and IE evaluation. Now I should write up the review and quickly check the references.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9df3d12a-51ea-4981-9422-a7ba3c37bdad",
  "isSidechain": false,
  "requestId": "req_011Cb3gfbGckPbMCucgtW6dw",
  "type": "assistant",
  "uuid": "cc15ed5d-4898-4d50-acae-c9e79d4e8afb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_1_68ddc296",
  "sessionId": "8e0e70e7-e72a-426a-9f89-26576a55a64e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0122HsMNre9GvbVMtDiG624Y",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 19951,
      "cache_read_input_tokens": 35123,
      "output_tokens": 3515,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 19951,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3515,
          "cache_read_input_tokens": 35123,
          "cache_creation_input_tokens": 19951,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 19951
          },
          "type": "message"
        }
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

_source line 63 · 2026-05-15T04:00:22.240Z_

已读完全文。现在验证引用并查看关键 figure。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cc15ed5d-4898-4d50-acae-c9e79d4e8afb",
  "isSidechain": false,
  "requestId": "req_011Cb3gfbGckPbMCucgtW6dw",
  "type": "assistant",
  "uuid": "b368f64b-0db1-40ad-af24-13763af19ff4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_1_68ddc296",
  "sessionId": "8e0e70e7-e72a-426a-9f89-26576a55a64e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0122HsMNre9GvbVMtDiG624Y",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 19951,
      "cache_read_input_tokens": 35123,
      "output_tokens": 3515,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 19951,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3515,
          "cache_read_input_tokens": 35123,
          "cache_creation_input_tokens": 19951,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 19951
          },
          "type": "message"
        }
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

_source line 64 · 2026-05-15T04:00:24.595Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__verify_references · `toolu_01F9hvEYJGhtbQZrnyvywjnn`</summary>

```json
{
  "paper_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper",
  "project": "struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b368f64b-0db1-40ad-af24-13763af19ff4",
  "isSidechain": false,
  "requestId": "req_011Cb3gfbGckPbMCucgtW6dw",
  "type": "assistant",
  "uuid": "f08f6b57-c544-44b1-85a5-d86917275869",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_1_68ddc296",
  "sessionId": "8e0e70e7-e72a-426a-9f89-26576a55a64e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0122HsMNre9GvbVMtDiG624Y",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 19951,
      "cache_read_input_tokens": 35123,
      "output_tokens": 3515,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 19951,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3515,
          "cache_read_input_tokens": 35123,
          "cache_creation_input_tokens": 19951,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 19951
          },
          "type": "message"
        }
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

_source line 65 · 2026-05-15T04:00:25.165Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images · `toolu_01S3KCKWZHWuEz24QPT69Czj`</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.pdf",
  "pages": "1-3",
  "dpi": 150
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f08f6b57-c544-44b1-85a5-d86917275869",
  "isSidechain": false,
  "requestId": "req_011Cb3gfbGckPbMCucgtW6dw",
  "type": "assistant",
  "uuid": "d8832dc2-09cb-47e6-a638-bf0af8806ebd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_1_68ddc296",
  "sessionId": "8e0e70e7-e72a-426a-9f89-26576a55a64e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0122HsMNre9GvbVMtDiG624Y",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 19951,
      "cache_read_input_tokens": 35123,
      "output_tokens": 3515,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 19951,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3515,
          "cache_read_input_tokens": 35123,
          "cache_creation_input_tokens": 19951,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 19951
          },
          "type": "message"
        }
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

_source line 66 · 2026-05-15T04:01:09.579Z_

<details><summary>↩ Tool result · `toolu_01F9hvEYJGhtbQZrnyvywjnn`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"summary\": {\"total_bib_entries\": 49, \"total_citations\": 69, \"unique_cited_keys\": 49, \"orphan_bib\": 0, \"missing_bib\": 0, \"duplicate_keys\": 0, \"online_verified\": 45, \"online_not_found\": 2, \"online_mismatch\": 2}, \"cross_check\": {\"orphan_bib\": [], \"missing_bib\": [], \"orphan_count\": 0, \"missing_count\": 0}, \"bib_entries\": [{\"key\": \"angelopoulos2021conformal\", \"type\": \"inproceedings\", \"title\": \"Uncertainty Sets for Image Classifiers using Conformal Prediction\", \"authors\": \"Angelopoulos, Anastasios N. and Bates, Stephen and Malik, Jitendra and Jordan, M...\", \"year\": \"2021\", \"venue\": \"ICLR 2021\"}, {\"key\": \"brown2024monkeys\", \"type\": \"article\", \"title\": \"Large Language Monkeys: Scaling Inference Compute with Repeated Sampling\", \"authors\": \"Brown, Bradley and Juravsky, Jordan and Ehrlich, Ryan and Clark, Ronald and Le, ...\", \"year\": \"2024\", \"venue\": \"arXiv preprint arXiv:2407.21787\"}, {\"key\": \"chen2024usc\", \"type\": \"inproceedings\", \"title\": \"Universal Self-Consistency for Large Language Model Generation\", \"authors\": \"Chen, Xinyun and Aksitov, Renat and Alon, Uri and Ren, Jie and Xiao, Kefan and Y...\", \"year\": \"2024\", \"venue\": \"arXiv preprint (ICML 2024 Workshop ICL)\"}, {\"key\": \"cobbe2021verifiers\", \"type\": \"article\", \"title\": \"Training Verifiers to Solve Math Word Problems\", \"authors\": \"Cobbe, Karl and Kosaraju, Vineet and Bavarian, Mohammad and Chen, Mark and Jun, ...\", \"year\": \"2021\", \"venue\": \"arXiv preprint arXiv:2110.14168\"}, {\"key\": \"culotta2004confidence\", \"type\": \"inproceedings\", \"title\": \"Confidence Estimation for Information Extraction\", \"authors\": \"Culotta, Aron and McCallum, Andrew\", \"year\": \"2004\", \"venue\": \"HLT-NAACL 2004\"}, {\"key\": \"derczynski2017wnut\", \"type\": \"inproceedings\", \"title\": \"Results of the WNUT2017 Shared Task on Novel and Emerging Entity Recognition\", \"authors\": \"Derczynski, Leon and Nichols, Eric and Erp, Marieke van and Limsopatham, Nut\", \"year\": \"2017\", \"venue\": \"W-NUT Workshop at EMNLP 2017\"}, {\"key\": \"desai2020calibration\", \"type\": \"inproceedings\", \"title\": \"Calibration of Pre-trained Transformers\", \"authors\": \"Desai, Shrey and Durrett, Greg\", \"year\": \"2020\", \"venue\": \"Proceedings of the 2020 Conference on Empirical Methods in Natural Language Proc...\"}, {\"key\": \"fisch2021conformal\", \"type\": \"inproceedings\", \"title\": \"Few-Shot Conformal Prediction with Auxiliary Tasks\", \"authors\": \"Fisch, Adam and Schuster, Tal and Jaakkola, Tommi and Barzilay, Regina\", \"year\": \"2021\", \"venue\": \"ICML 2021\"}, {\"key\": \"fleiss1971agreement\", \"type\": \"article\", \"title\": \"Measuring nominal scale agreement among many raters.\", \"authors\": \"Fleiss, Joseph L.\", \"year\": \"1971\", \"venue\": \"Psychological Bulletin\"}, {\"key\": \"gal2016dropout\", \"type\": \"inproceedings\", \"title\": \"Dropout as a Bayesian Approximation: Representing Model Uncertainty in Deep Learning\", \"authors\": \"Gal, Yarin and Ghahramani, Zoubin\", \"year\": \"2016\", \"venue\": \"ICML 2016\"}, {\"key\": \"geifman2017selective\", \"type\": \"inproceedings\", \"title\": \"Selective Classification for Deep Neural Networks\", \"authors\": \"Geifman, Yonatan and El-Yaniv, Ran\", \"year\": \"2017\", \"venue\": \"NeurIPS 2017\"}, {\"key\": \"feng2025optimal\", \"type\": \"article\", \"title\": \"Optimal Self-Consistency for Efficient Reasoning with Large Language Models\", \"authors\": \"Feng, Austin and Alonso, Marius and Odonnat, Ambroise\", \"year\": \"2025\", \"venue\": \"arXiv preprint arXiv:2511.12309\"}, {\"key\": \"geng2024confidence\", \"type\": \"inproceedings\", \"title\": \"A Survey of Confidence Estimation and Calibration in Large Language Models\", \"authors\": \"Geng, Jiahui and Cai, Fengyu and Wang, Yuxia and Koeppl, Heinz and Nakov, Presla...\", \"year\": \"2024\", \"venue\": \"Proceedings of the 2024 Conference of the North American Chapter of the Associat...\"}, {\"key\": \"guo2017calibration\", \"type\": \"inproceedings\", \"title\": \"On Calibration of Modern Neural Networks\", \"authors\": \"Guo, Chuan and Pleiss, Geoff and Sun, Yu and Weinberger, Kilian Q.\", \"year\": \"2017\", \"venue\": \"ICML 2017\"}, {\"key\": \"hobelsberger2025systematic\", \"type\": \"article\", \"title\": \"Systematic Evaluation of Uncertainty Estimation Methods in Large Language Models\", \"authors\": \"Hobelsberger, Christian and Winner, Theresa and Nawroth, Andreas and Mitevski, O...\", \"year\": \"2025\", \"venue\": \"arXiv preprint arXiv:2510.20460\"}, {\"key\": \"jaccard1901distribution\", \"type\": \"article\", \"title\": \"Étude comparative de la distribution florale dans une portion des Alpes et du Jura\", \"authors\": \"Jaccard, Paul\", \"year\": \"1901\", \"venue\": \"Bulletin de la Société Vaudoise des Sciences Naturelles\"}, {\"key\": \"josifoski2022genie\", \"type\": \"inproceedings\", \"title\": \"GenIE: Generative Information Extraction\", \"authors\": \"Josifoski, Martin and De Cao, Nicola and Peyrard, Maxime and Petroni, Fabio and ...\", \"year\": \"2022\", \"venue\": \"Proceedings of the 2022 Conference of the North American Chapter of the Associat...\"}, {\"key\": \"kadavath2022language\", \"type\": \"article\", \"title\": \"Language Models (Mostly) Know What They Know\", \"authors\": \"Kadavath, Saurav and Conerly, Tom and Askell, Amanda and Henighan, Tom and Drain...\", \"year\": \"2022\", \"venue\": \"arXiv preprint arXiv:2207.05221\"}, {\"key\": \"kang2025selfcertainty\", \"type\": \"inproceedings\", \"title\": \"Scalable Best-of-N Selection for Large Language Models via Self-Certainty\", \"authors\": \"Kang, Zhewei and Zhao, Xuandong and Song, Dawn\", \"year\": \"2025\", \"venue\": \"NeurIPS 2025\"}, {\"key\": \"kim2026reasc\", \"type\": \"inproceedings\", \"title\": \"Reliability-Aware Adaptive Self-Consistency for Efficient Sampling in LLM Reasoning\", \"authors\": \"Kim, Junseok and Yang, Nakyeong and Min, Kyungmin and Jung, Kyomin\", \"year\": \"2026\", \"venue\": \"ACL 2026\"}, {\"key\": \"kossen2024semantic\", \"type\": \"article\", \"title\": \"Semantic Entropy Probes: Robust and Cheap Hallucination Detection in LLMs\", \"authors\": \"Kossen, Jannik and Han, Jiatong and Razzak, Muhammed and Schut, Lisa and Malik, ...\", \"year\": \"2024\", \"venue\": \"arXiv preprint arXiv:2406.15927\"}, {\"key\": \"li2025llms\", \"type\": \"article\", \"title\": \"LLMs Can Generate a Better Answer by Aggregating Their Own Responses\", \"authors\": \"Li, Zichong and Feng, Xinyu and Cai, Yuheng and Zhang, Zixuan and Liu, Tianyi an...\", \"year\": \"2025\", \"venue\": \"arXiv preprint arXiv:2503.04104\"}, {\"key\": \"kuhn2023semantic\", \"type\": \"inproceedings\", \"title\": \"Semantic Uncertainty: Linguistic Invariances for Uncertainty Estimation in Natural Language Generation\", \"authors\": \"Kuhn, Lorenz and Gal, Yarin and Farquhar, Sebastian\", \"year\": \"2023\", \"venue\": \"ICLR 2023\"}, {\"key\": \"lakshminarayanan2017ensembles\", \"type\": \"inproceedings\", \"title\": \"Simple and Scalable Predictive Uncertainty Estimation using Deep Ensembles\", \"authors\": \"Lakshminarayanan, Balaji and Pritzel, Alexander and Blundell, Charles\", \"year\": \"2017\", \"venue\": \"NeurIPS 2017\"}, {\"key\": \"li2023codeie\", \"type\": \"inproceedings\", \"title\": \"CodeIE: Large Code Generation Models are Better Few-Shot Information Extractors\", \"authors\": \"Li, Peng and Sun, Tianxiang and Tang, Qiong and Yan, Hang and Wu, Yuanbin and Hu...\", \"year\": \"2023\", \"venue\": \"Proceedings of the 61st Annual Meeting of the Association for Computational Ling...\"}, {\"key\": \"lightman2024verify\", \"type\": \"inproceedings\", \"title\": \"Let's Verify Step by Step\", \"authors\": \"Lightman, Hunter and Kosaraju, Vineet and Burda, Yura and Edwards, Harri and Bak...\", \"year\": \"2024\", \"venue\": \"ICLR 2024\"}, {\"key\": \"luan2018scierc\", \"type\": \"inproceedings\", \"title\": \"Multi-Task Identification of Entities, Relations, and Coreference for Scientific Knowledge Graph Construction\", \"authors\": \"Luan, Yi and He, Luheng and Ostendorf, Mari and Hajishirzi, Hannaneh\", \"year\": \"2018\", \"venue\": \"Proceedings of the 2018 Conference on Empirical Methods in Natural Language Proc...\"}, {\"key\": \"manakul2023selfcheckgpt\", \"type\": \"inproceedings\", \"title\": \"SelfCheckGPT: Zero-Resource Black-Box Hallucination Detection for Generative Large Language Models\", \"authors\": \"Manakul, Potsawee and Liusie, Adian and Gales, Mark\", \"year\": \"2023\", \"venue\": \"Proceedings of the 2023 Conference on Empirical Methods in Natural Language Proc...\"}, {\"key\": \"nedellec2026consistency\", \"type\": \"article\", \"title\": \"Consistency–accuracy correlation in hard-prompted LLMs for entity and relation extraction: empirical findings from plant...\", \"authors\": \"Yao, Xinzhi and Nédellec, Claire and Xia, Jingbo and Bossy, Robert\", \"year\": \"2026\", \"venue\": \"Genomics \\\\& Informatics\"}, {\"key\": \"oh2025latentsc\", \"type\": \"article\", \"title\": \"Latent Self-Consistency for Reliable Majority-Set Selection in Short- and Long-Answer Reasoning\", \"authors\": \"Oh, Jungsuk and Lee, Jay-Yoon\", \"year\": \"2025\", \"venue\": \"arXiv preprint arXiv:2508.18395\"}, {\"key\": \"sainz2024gollie\", \"type\": \"inproceedings\", \"title\": \"GoLLIE: Annotation Guidelines improve Zero-Shot Information-Extraction\", \"authors\": \"Sainz, Oscar and García-Ferrero, Iker and Agerri, Rodrigo and Lacalle, Oier Lope...\", \"year\": \"2024\", \"venue\": \"ICLR 2024\"}, {\"key\": \"shelmanov2021active\", \"type\": \"inproceedings\", \"title\": \"Active Learning for Sequence Tagging with Deep Pre-trained Models and Bayesian Uncertainty Estimates\", \"authors\": \"Shelmanov, Artem and Puzyrev, Dmitri and Kupriyanova, Lyubov and Belyakov, Denis...\", \"year\": \"2021\", \"venue\": \"Proceedings of the 16th Conference of the European Chapter of the Association fo...\"}, {\"key\": \"snell2024scaling\", \"type\": \"inproceedings\", \"title\": \"Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters\", \"authors\": \"Snell, Charlie and Lee, Jaehoon and Xu, Kelvin and Kumar, Aviral\", \"year\": \"2024\", \"venue\": \"ICLR 2025\"}, {\"key\": \"taubenfeld2025cisc\", \"type\": \"inproceedings\", \"title\": \"Confidence Improves Self-Consistency in LLMs\", \"authors\": \"Taubenfeld, Amir and Sheffer, Tom and Ofek, Eran and Feder, Amir and Goldstein, ...\", \"year\": \"2025\", \"venue\": \"Findings of the Association for Computational Linguistics: ACL 2025\"}, {\"key\": \"thirukovalluru2024atomic\", \"type\": \"inproceedings\", \"title\": \"Atomic Self-Consistency for Better Long Form Generations\", \"authors\": \"Thirukovalluru, Raghuveer and Huang, Yukun and Dhingra, Bhuwan\", \"year\": \"2024\", \"venue\": \"Proceedings of the 2024 Conference on Empirical Methods in Natural Language Proc...\"}, {\"key\": \"tjongkimsang2003conll\", \"type\": \"inproceedings\", \"title\": \"Introduction to the CoNLL-2003 Shared Task: Language-Independent Named Entity Recognition\", \"authors\": \"Sang, Erik F. Tjong Kim and Meulder, Fien De\", \"year\": \"2003\", \"venue\": \"CoNLL 2003\"}, {\"key\": \"vashurin2025cocoa\", \"type\": \"inproceedings\", \"title\": \"Uncertainty Quantification for LLMs through Minimum Bayes Risk: Bridging Confidence and Consistency\", \"authors\": \"Vashurin, Roman and Goloburda, Maiya and Ilina, Albina and Rubashevskii, Aleksan...\", \"year\": \"2025\", \"venue\": \"NeurIPS 2025\"}, {\"key\": \"wadhwa2023revisiting\", \"type\": \"inproceedings\", \"title\": \"Revisiting Relation Extraction in the era of Large Language Models\", \"authors\": \"Wadhwa, Somin and Amir, Silvio and Wallace, Byron\", \"year\": \"2023\", \"venue\": \"Proceedings of the 61st Annual Meeting of the Association for Computational Ling...\"}, {\"key\": \"wang2023instructuie\", \"type\": \"article\", \"title\": \"InstructUIE: Multi-task Instruction Tuning for Unified Information Extraction\", \"authors\": \"Wang, Xiao and Zhou, Weikang and Zu, Can and Xia, Han and Chen, Tianze and Zhang...\", \"year\": \"2023\", \"venue\": \"arXiv preprint arXiv:2304.08085\"}, {\"key\": \"wang2023selfconsistency\", \"type\": \"inproceedings\", \"title\": \"Self-Consistency Improves Chain of Thought Reasoning in Language Models\", \"authors\": \"Wang, Xuezhi and Wei, Jason and Schuurmans, Dale and Le, Quoc and Chi, Ed and Na...\", \"year\": \"2023\", \"venue\": \"ICLR 2023\"}, {\"key\": \"wang2025make\", \"type\": \"inproceedings\", \"title\": \"Make Every Penny Count: Difficulty-Adaptive Self-Consistency for Cost-Efficient Reasoning\", \"authors\": \"Wang, Xinglin and Feng, Shaoxiong and Li, Yiwei and Yuan, Peiwen and Zhang, Yueq...\", \"year\": \"2025\", \"venue\": \"Findings of the Association for Computational Linguistics: NAACL 2025\"}, {\"key\": \"wang2024mathshepherd\", \"type\": \"inproceedings\", \"title\": \"Math-Shepherd: Verify and Reinforce LLMs Step-by-step without Human Annotations\", \"authors\": \"Wang, Peiyi and Li, Lei and Shao, Zhihong and Xu, Runxin and Dai, Damai and Li, ...\", \"year\": \"2024\", \"venue\": \"ACL 2024\"}, {\"key\": \"wang2025rankedvoting\", \"type\": \"inproceedings\", \"title\": \"Ranked Voting based Self-Consistency of Large Language Models\", \"authors\": \"Wang, Weiqin and Wang, Yile and Huang, Hui\", \"year\": \"2025\", \"venue\": \"ACL Findings 2025\"}, {\"key\": \"wen2025know\", \"type\": \"article\", \"title\": \"Know Your Limits: A Survey of Abstention in Large Language Models\", \"authors\": \"Wen, Bingbing and Yao, Jihan and Feng, Shangbin and Xu, Chenjun and Tsvetkov, Yu...\", \"year\": \"2025\", \"venue\": \"Transactions of the Association for Computational Linguistics\"}, {\"key\": \"willard2023guided\", \"type\": \"article\", \"title\": \"Efficient Guided Generation for Large Language Models\", \"authors\": \"Willard, Brandon T. and Louf, Rémi\", \"year\": \"2023\", \"venue\": \"arXiv preprint arXiv:2307.09702\"}, {\"key\": \"xia2025survey\", \"type\": \"inproceedings\", \"title\": \"A Survey of Uncertainty Estimation Methods on Large Language Models\", \"authors\": \"Xia, Zhiqiu and Xu, Jinxuan and Zhang, Yuqian and Liu, Hang\", \"year\": \"2025\", \"venue\": \"ACL Findings 2025\"}, {\"key\": \"xiao2019uncertainty\", \"type\": \"article\", \"title\": \"Quantifying Uncertainties in Natural Language Processing Tasks\", \"authors\": \"Xiao, Yijun and Wang, William Yang\", \"year\": \"2019\", \"venue\": \"Proceedings of the AAAI Conference on Artificial Intelligence\"}, {\"key\": \"zhang2023ener\", \"type\": \"inproceedings\", \"title\": \"E-NER: Evidential Deep Learning for Trustworthy Named Entity Recognition\", \"authors\": \"Zhang, Zhen and Hu, Mengting and Zhao, Shiwan and Huang, Minlie and Wang, Haotia...\", \"year\": \"2023\", \"venue\": \"Findings of the Association for Computational Linguistics: ACL 2023\"}, {\"key\": \"zhou2024uniner\", \"type\": \"inproceedings\", \"title\": \"UniversalNER: Targeted Distillation from Large Language Models for Open Named Entity Recognition\", \"authors\": \"Zhou, Wenxuan and Zhang, Sheng and Gu, Yu and Chen, Muhao and Poon, Hoifung\", \"year\": \"2024\", \"venue\": \"Proceedings of the International Conference on Learning Representations (ICLR)\"}], \"tex_citations\": [{\"key\": \"wang2023selfconsistency\", \"file\": \"sections/introduction.tex\", \"line\": 4, \"command\": \"citealp\"}, {\"key\": \"snell2024scaling\", \"file\": \"sections/introduction.tex\", \"line\": 5, \"command\": \"cite\"}, {\"key\": \"brown2024monkeys\", \"file\": \"sections/introduction.tex\", \"line\": 5, \"command\": \"cite\"}, {\"key\": \"wang2023selfconsistency\", \"file\": \"sections/introduction.tex\", \"line\": 15, \"command\": \"cite\"}, {\"key\": \"chen2024usc\", \"file\": \"sections/introduction.tex\", \"line\": 15, \"command\": \"cite\"}, {\"key\": \"taubenfeld2025cisc\", \"file\": \"sections/introduction.tex\", \"line\": 15, \"command\": \"cite\"}, {\"key\": \"kang2025selfcertainty\", \"file\": \"sections/introduction.tex\", \"line\": 15, \"command\": \"cite\"}, {\"key\": \"nedellec2026consistency\", \"file\": \"sections/introduction.tex\", \"line\": 16, \"command\": \"citet\"}, {\"key\": \"luan2018scierc\", \"file\": \"sections/introduction.tex\", \"line\": 31, \"command\": \"cite\"}, {\"key\": \"tjongkimsang2003conll\", \"file\": \"sections/introduction.tex\", \"line\": 31, \"command\": \"cite\"}, {\"key\": \"derczynski2017wnut\", \"file\": \"sections/introduction.tex\", \"line\": 31, \"command\": \"cite\"}, {\"key\": \"wang2023selfconsistency\", \"file\": \"sections/related_work.tex\", \"line\": 4, \"command\": \"cite\"}, {\"key\": \"chen2024usc\", \"file\": \"sections/related_work.tex\", \"line\": 5, \"command\": \"cite\"}, {\"key\": \"thirukovalluru2024atomic\", \"file\": \"sections/related_work.tex\", \"line\": 5, \"command\": \"cite\"}, {\"key\": \"manakul2023selfcheckgpt\", \"file\": \"sections/related_work.tex\", \"line\": 5, \"command\": \"cite\"}, {\"key\": \"snell2024scaling\", \"file\": \"sections/related_work.tex\", \"line\": 6, \"command\": \"citet\"}, {\"key\": \"brown2024monkeys\", \"file\": \"sections/related_work.tex\", \"line\": 6, \"command\": \"citet\"}, {\"key\": \"taubenfeld2025cisc\", \"file\": \"sections/related_work.tex\", \"line\": 7, \"command\": \"cite\"}, {\"key\": \"kang2025selfcertainty\", \"file\": \"sections/related_work.tex\", \"line\": 7, \"command\": \"cite\"}, {\"key\": \"kim2026reasc\", \"file\": \"sections/related_work.tex\", \"line\": 7, \"command\": \"cite\"}, {\"key\": \"wang2025rankedvoting\", \"file\": \"sections/related_work.tex\", \"line\": 7, \"command\": \"cite\"}, {\"key\": \"oh2025latentsc\", \"file\": \"sections/related_work.tex\", \"line\": 7, \"command\": \"cite\"}, {\"key\": \"feng2025optimal\", \"file\": \"sections/related_work.tex\", \"line\": 8, \"command\": \"citet\"}, {\"key\": \"wang2025make\", \"file\": \"sections/related_work.tex\", \"line\": 8, \"command\": \"citet\"}, {\"key\": \"li2025llms\", \"file\": \"sections/related_work.tex\", \"line\": 8, \"command\": \"citet\"}, {\"key\": \"nedellec2026consistency\", \"file\": \"sections/related_work.tex\", \"line\": 13, \"command\": \"citet\"}, {\"key\": \"vashurin2025cocoa\", \"file\": \"sections/related_work.tex\", \"line\": 16, \"command\": \"cite\"}, {\"key\": \"zhou2024uniner\", \"file\": \"sections/related_work.tex\", \"line\": 17, \"command\": \"cite\"}, {\"key\": \"sainz2024gollie\", \"file\": \"sections/related_work.tex\", \"line\": 17, \"command\": \"cite\"}, {\"key\": \"josifoski2022genie\", \"file\": \"sections/related_work.tex\", \"line\": 17, \"command\": \"cite\"}, {\"key\": \"li2023codeie\", \"file\": \"sections/related_work.tex\", \"line\": 17, \"command\": \"cite\"}, {\"key\": \"wadhwa2023revisiting\", \"file\": \"sections/related_work.tex\", \"line\": 17, \"command\": \"cite\"}, {\"key\": \"wang2023instructuie\", \"file\": \"sections/related_work.tex\", \"line\": 17, \"command\": \"cite\"}, {\"key\": \"willard2023guided\", \"file\": \"sections/related_work.tex\", \"line\": 17, \"command\": \"cite\"}, {\"key\": \"geng2024confidence\", \"file\": \"sections/related_work.tex\", \"line\": 20, \"command\": \"cite\"}, {\"key\": \"wen2025know\", \"file\": \"sections/related_work.tex\", \"line\": 20, \"command\": \"cite\"}, {\"key\": \"xia2025survey\", \"file\": \"sections/related_work.tex\", \"line\": 20, \"command\": \"cite\"}, {\"key\": \"hobelsberger2025systematic\", \"file\": \"sections/related_work.tex\", \"line\": 20, \"command\": \"cite\"}, {\"key\": \"kuhn2023semantic\", \"file\": \"sections/related_work.tex\", \"line\": 21, \"command\": \"cite\"}, {\"key\": \"kossen2024semantic\", \"file\": \"sections/related_work.tex\", \"line\": 21, \"command\": \"citet\"}, {\"key\": \"kadavath2022language\", \"file\": \"sections/related_work.tex\", \"line\": 21, \"command\": \"cite\"}, {\"key\": \"guo2017calibration\", \"file\": \"sections/related_work.tex\", \"line\": 22, \"command\": \"cite\"}, {\"key\": \"desai2020calibration\", \"file\": \"sections/related_work.tex\", \"line\": 22, \"command\": \"cite\"}, {\"key\": \"lakshminarayanan2017ensembles\", \"file\": \"sections/related_work.tex\", \"line\": 23, \"command\": \"cite\"}, {\"key\": \"gal2016dropout\", \"file\": \"sections/related_work.tex\", \"line\": 23, \"command\": \"cite\"}, {\"key\": \"xiao2019uncertainty\", \"file\": \"sections/related_work.tex\", \"line\": 24, \"command\": \"cite\"}, {\"key\": \"shelmanov2021active\", \"file\": \"sections/related_work.tex\", \"line\": 24, \"command\": \"cite\"}, {\"key\": \"zhang2023ener\", \"file\": \"sections/related_work.tex\", \"line\": 24, \"command\": \"cite\"}, {\"key\": \"fisch2021conformal\", \"file\": \"sections/related_work.tex\", \"line\": 25, \"command\": \"cite\"}, {\"key\": \"angelopoulos2021conformal\", \"file\": \"sections/related_work.tex\", \"line\": 25, \"command\": \"cite\"}, {\"key\": \"cobbe2021verifiers\", \"file\": \"sections/related_work.tex\", \"line\": 25, \"command\": \"cite\"}, {\"key\": \"lightman2024verify\", \"file\": \"sections/related_work.tex\", \"line\": 25, \"command\": \"cite\"}, {\"key\": \"wang2024mathshepherd\", \"file\": \"sections/related_work.tex\", \"line\": 25, \"command\": \"cite\"}, {\"key\": \"geifman2017selective\", \"file\": \"sections/related_work.tex\", \"line\": 26, \"command\": \"cite\"}, {\"key\": \"culotta2004confidence\", \"file\": \"sections/related_work.tex\", \"line\": 26, \"command\": \"cite\"}, {\"key\": \"willard2023guided\", \"file\": \"sections/method.tex\", \"line\": 5, \"command\": \"cite\"}, {\"key\": \"fleiss1971agreement\", \"file\": \"sections/method.tex\", \"line\": 32, \"command\": \"citet\"}, {\"key\": \"jaccard1901distribution\", \"file\": \"sections/method.tex\", \"line\": 41, \"command\": \"cite\"}, {\"key\": \"luan2018scierc\", \"file\": \"sections/experiments.tex\", \"line\": 9, \"command\": \"cite\"}, {\"key\": \"tjongkimsang2003conll\", \"file\": \"sections/experiments.tex\", \"line\": 10, \"command\": \"cite\"}, {\"key\": \"derczynski2017wnut\", \"file\": \"sections/experiments.tex\", \"line\": 11, \"command\": \"cite\"}, {\"key\": \"willard2023guided\", \"file\": \"sections/experiments.tex\", \"line\": 17, \"command\": \"cite\"}, {\"key\": \"kuhn2023semantic\", \"file\": \"sections/experiments.tex\", \"line\": 64, \"command\": \"cite\"}, {\"key\": \"brown2024monkeys\", \"file\": \"sections/experiments.tex\", \"line\": 136, \"command\": \"cite\"}, {\"key\": \"snell2024scaling\", \"file\": \"sections/experiments.tex\", \"line\": 136, \"command\": \"cite\"}, {\"key\": \"cobbe2021verifiers\", \"file\": \"sections/experiments.tex\", \"line\": 136, \"command\": \"cite\"}, {\"key\": \"cobbe2021verifiers\", \"file\": \"sections/discussion.tex\", \"line\": 31, \"command\": \"cite\"}, {\"key\": \"brown2024monkeys\", \"file\": \"sections/appendix.tex\", \"line\": 184, \"command\": \"cite\"}, {\"key\": \"snell2024scaling\", \"file\": \"sections/appendix.tex\", \"line\": 184, \"command\": \"cite\"}], \"online_verification\": [{\"key\": \"angelopoulos2021conformal\", \"title\": \"Uncertainty Sets for Image Classifiers using Conformal Prediction\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Uncertainty Sets for Image Classifiers using Conformal Prediction\", \"matched_year\": \"2020\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"brown2024monkeys\", \"title\": \"Large Language Monkeys: Scaling Inference Compute with Repeated Sampling\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Large Language Monkeys: Scaling Inference Compute with Repeated Sampling\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"chen2024usc\", \"title\": \"Universal Self-Consistency for Large Language Model Generation\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Universal Self-Consistency for Large Language Model Generation\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"cobbe2021verifiers\", \"title\": \"Training Verifiers to Solve Math Word Problems\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Training Verifiers to Solve Math Word Problems\", \"matched_year\": \"2021\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"culotta2004confidence\", \"title\": \"Confidence Estimation for Information Extraction\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Confidence estimation for information extraction\", \"matched_year\": \"2004\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"derczynski2017wnut\", \"title\": \"Results of the WNUT2017 Shared Task on Novel and Emerging Entity Recognition\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Results of the WNUT2017 Shared Task on Novel and Emerging Entity Recognition\", \"matched_year\": \"2017\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"desai2020calibration\", \"title\": \"Calibration of Pre-trained Transformers\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Calibration of Pre-trained Transformers\", \"matched_year\": \"2020\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"fisch2021conformal\", \"title\": \"Few-Shot Conformal Prediction with Auxiliary Tasks\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Few-shot Conformal Prediction with Auxiliary Tasks\", \"matched_year\": \"2021\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"fleiss1971agreement\", \"title\": \"Measuring nominal scale agreement among many raters.\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Measuring nominal scale agreement among many raters.\", \"matched_year\": \"1971\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"gal2016dropout\", \"title\": \"Dropout as a Bayesian Approximation: Representing Model Uncertainty in Deep Learning\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Dropout as a Bayesian Approximation: Representing Model Uncertainty in Deep Learning\", \"matched_year\": \"2015\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"geifman2017selective\", \"title\": \"Selective Classification for Deep Neural Networks\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Selective Classification for Deep Neural Networks\", \"matched_year\": \"2017\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"feng2025optimal\", \"title\": \"Optimal Self-Consistency for Efficient Reasoning with Large Language Models\", \"status\": \"mismatch\", \"confidence\": 1.0, \"matched_title\": \"Optimal Self-Consistency for Efficient Reasoning with Large Language Models\", \"matched_year\": \"2025\", \"mismatch_fields\": [\"first_author: bib=feng vs api=austin\"], \"note\": \"\"}, {\"key\": \"geng2024confidence\", \"title\": \"A Survey of Confidence Estimation and Calibration in Large Language Models\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"A Survey of Confidence Estimation and Calibration in Large Language Models\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"guo2017calibration\", \"title\": \"On Calibration of Modern Neural Networks\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"On Calibration of Modern Neural Networks\", \"matched_year\": \"2017\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"hobelsberger2025systematic\", \"title\": \"Systematic Evaluation of Uncertainty Estimation Methods in Large Language Models\", \"status\": \"not_found\", \"confidence\": 0.236, \"matched_title\": \"A new criterion for assessing discriminant validity in variance-based structural equation modeling\", \"matched_year\": \"\", \"mismatch_fields\": [], \"note\": \"best match similarity 0.24 below threshold 0.82\"}, {\"key\": \"jaccard1901distribution\", \"title\": \"Étude comparative de la distribution florale dans une portion des Alpes et du Jura\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Étude comparative de la distribution florale dans une portion des Alpes et du Jura\", \"matched_year\": \"1901\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"josifoski2022genie\", \"title\": \"GenIE: Generative Information Extraction\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"GenIE: Generative Information Extraction\", \"matched_year\": \"2022\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"kadavath2022language\", \"title\": \"Language Models (Mostly) Know What They Know\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Language Models (Mostly) Know What They Know\", \"matched_year\": \"2022\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"kang2025selfcertainty\", \"title\": \"Scalable Best-of-N Selection for Large Language Models via Self-Certainty\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Scalable Best-of-N Selection for Large Language Models via Self-Certainty\", \"matched_year\": \"2025\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"kim2026reasc\", \"title\": \"Reliability-Aware Adaptive Self-Consistency for Efficient Sampling in LLM Reasoning\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Reliability-Aware Adaptive Self-Consistency for Efficient Sampling in LLM Reasoning\", \"matched_year\": \"2026\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"kossen2024semantic\", \"title\": \"Semantic Entropy Probes: Robust and Cheap Hallucination Detection in LLMs\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Semantic Entropy Probes: Robust and Cheap Hallucination Detection in LLMs\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"li2025llms\", \"title\": \"LLMs Can Generate a Better Answer by Aggregating Their Own Responses\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"LLMs Can Generate a Better Answer by Aggregating Their Own Responses\", \"matched_year\": \"2025\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"kuhn2023semantic\", \"title\": \"Semantic Uncertainty: Linguistic Invariances for Uncertainty Estimation in Natural Language Generation\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Semantic Uncertainty: Linguistic Invariances for Uncertainty Estimation in Natural Language Generation\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"lakshminarayanan2017ensembles\", \"title\": \"Simple and Scalable Predictive Uncertainty Estimation using Deep Ensembles\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Simple and Scalable Predictive Uncertainty Estimation using Deep Ensembles\", \"matched_year\": \"2016\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"li2023codeie\", \"title\": \"CodeIE: Large Code Generation Models are Better Few-Shot Information Extractors\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"CodeIE: Large Code Generation Models are Better Few-Shot Information Extractors\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"lightman2024verify\", \"title\": \"Let's Verify Step by Step\", \"status\": \"not_found\", \"confidence\": 0.246, \"matched_title\": \"Development and dosimetric verification of static SHArc: Step‐and‐shoot carbon ion arc therapy for LET &lt;sub>d&lt;/sub> escalation in pancreatic tumors\", \"matched_year\": \"\", \"mismatch_fields\": [], \"note\": \"best match similarity 0.25 below threshold 0.82\"}, {\"key\": \"luan2018scierc\", \"title\": \"Multi-Task Identification of Entities, Relations, and Coreference for Scientific Knowledge Graph Construction\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Multi-Task Identification of Entities, Relations, and Coreference for Scientific Knowledge Graph Construction\", \"matched_year\": \"2018\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"manakul2023selfcheckgpt\", \"title\": \"SelfCheckGPT: Zero-Resource Black-Box Hallucination Detection for Generative Large Language Models\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"SelfCheckGPT: Zero-Resource Black-Box Hallucination Detection for Generative Large Language Models\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"nedellec2026consistency\", \"title\": \"Consistency–accuracy correlation in hard-prompted LLMs for entity and relation extraction: empirical findings from plant-health data\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Consistency–accuracy correlation in hard-prompted LLMs for entity and relation extraction: empirical findings from plant-health data\", \"matched_year\": \"2026\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"oh2025latentsc\", \"title\": \"Latent Self-Consistency for Reliable Majority-Set Selection in Short- and Long-Answer Reasoning\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Latent Self-Consistency for Reliable Majority-Set Selection in Short- and Long-Answer Reasoning\", \"matched_year\": \"2026\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"sainz2024gollie\", \"title\": \"GoLLIE: Annotation Guidelines improve Zero-Shot Information-Extraction\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"GoLLIE: Annotation Guidelines improve Zero-Shot Information-Extraction\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"shelmanov2021active\", \"title\": \"Active Learning for Sequence Tagging with Deep Pre-trained Models and Bayesian Uncertainty Estimates\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Active Learning for Sequence Tagging with Deep Pre-trained Models and Bayesian Uncertainty Estimates\", \"matched_year\": \"2021\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"snell2024scaling\", \"title\": \"Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters\", \"status\": \"mismatch\", \"confidence\": 1.0, \"matched_title\": \"Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters\", \"matched_year\": \"2024\", \"mismatch_fields\": [\"first_author: bib=snell vs api=charlie\"], \"note\": \"\"}, {\"key\": \"taubenfeld2025cisc\", \"title\": \"Confidence Improves Self-Consistency in LLMs\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Confidence Improves Self-Consistency in LLMs\", \"matched_year\": \"2025\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"thirukovalluru2024atomic\", \"title\": \"Atomic Self-Consistency for Better Long Form Generations\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Atomic Self-Consistency for Better Long Form Generations\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"tjongkimsang2003conll\", \"title\": \"Introduction to the CoNLL-2003 Shared Task: Language-Independent Named Entity Recognition\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Introduction to the CoNLL-2003 Shared Task: Language-Independent Named Entity Recognition\", \"matched_year\": \"2003\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"vashurin2025cocoa\", \"title\": \"Uncertainty Quantification for LLMs through Minimum Bayes Risk: Bridging Confidence and Consistency\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Uncertainty Quantification for LLMs through Minimum Bayes Risk: Bridging Confidence and Consistency\", \"matched_year\": \"2025\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"wadhwa2023revisiting\", \"title\": \"Revisiting Relation Extraction in the era of Large Language Models\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Revisiting Relation Extraction in the era of Large Language Models\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"wang2023instructuie\", \"title\": \"InstructUIE: Multi-task Instruction Tuning for Unified Information Extraction\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"InstructUIE: Multi-task Instruction Tuning for Unified Information Extraction\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"wang2023selfconsistency\", \"title\": \"Self-Consistency Improves Chain of Thought Reasoning in Language Models\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Self-Consistency Improves Chain of Thought Reasoning in Language Models\", \"matched_year\": \"2022\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"wang2025make\", \"title\": \"Make Every Penny Count: Difficulty-Adaptive Self-Consistency for Cost-Efficient Reasoning\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Make Every Penny Count: Difficulty-Adaptive Self-Consistency for Cost-Efficient Reasoning\", \"matched_year\": \"2025\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"wang2024mathshepherd\", \"title\": \"Math-Shepherd: Verify and Reinforce LLMs Step-by-step without Human Annotations\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Math-Shepherd: Verify and Reinforce LLMs Step-by-step without Human Annotations\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"wang2025rankedvoting\", \"title\": \"Ranked Voting based Self-Consistency of Large Language Models\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Ranked Voting based Self-Consistency of Large Language Models\", \"matched_year\": \"2025\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"wen2025know\", \"title\": \"Know Your Limits: A Survey of Abstention in Large Language Models\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Know Your Limits: A Survey of Abstention in Large Language Models\", \"matched_year\": \"2025\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"willard2023guided\", \"title\": \"Efficient Guided Generation for Large Language Models\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Efficient Guided Generation for Large Language Models\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"xia2025survey\", \"title\": \"A Survey of Uncertainty Estimation Methods on Large Language Models\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"A Survey of Uncertainty Estimation Methods on Large Language Models\", \"matched_year\": \"2025\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"xiao2019uncertainty\", \"title\": \"Quantifying Uncertainties in Natural Language Processing Tasks\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Quantifying Uncertainties in Natural Language Processing Tasks\", \"matched_year\": \"2019\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"zhang2023ener\", \"title\": \"E-NER: Evidential Deep Learning for Trustworthy Named Entity Recognition\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"E-NER: Evidential Deep Learning for Trustworthy Named Entity Recognition\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"zhou2024uniner\", \"title\": \"UniversalNER: Targeted Distillation from Large Language Models for Open Named Entity Recognition\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"UniversalNER: Targeted Distillation from Large Language Models for Open Named Entity Recognition\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}]}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f08f6b57-c544-44b1-85a5-d86917275869",
  "isSidechain": false,
  "promptId": "06c85d14-4a07-4193-8916-587ad0c60656",
  "type": "user",
  "uuid": "03ff3561-7736-4f11-aac4-208cb478ce5f",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"summary\\\": {\\\"total_bib_entries\\\": 49, \\\"total_citations\\\": 69, \\\"unique_cited_keys\\\": 49, \\\"orphan_bib\\\": 0, \\\"missing_bib\\\": 0, \\\"duplicate_keys\\\": 0, \\\"online_verified\\\": 45, \\\"online_not_found\\\": 2, \\\"online_mismatch\\\": 2}, \\\"cross_check\\\": {\\\"orphan_bib\\\": [], \\\"missing_bib\\\": [], \\\"orphan_count\\\": 0, \\\"missing_count\\\": 0}, \\\"bib_entries\\\": [{\\\"key\\\": \\\"angelopoulos2021conformal\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Uncertainty Sets for Image Classifiers using Conformal Prediction\\\", \\\"authors\\\": \\\"Angelopoulos, Anastasios N. and Bates, Stephen and Malik, Jitendra and Jordan, M...\\\", \\\"year\\\": \\\"2021\\\", \\\"venue\\\": \\\"ICLR 2021\\\"}, {\\\"key\\\": \\\"brown2024monkeys\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Large Language Monkeys: Scaling Inference Compute with Repeated Sampling\\\", \\\"authors\\\": \\\"Brown, Bradley and Juravsky, Jordan and Ehrlich, Ryan and Clark, Ronald and Le, ...\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"arXiv preprint arXiv:2407.21787\\\"}, {\\\"key\\\": \\\"chen2024usc\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Universal Self-Consistency for Large Language Model Generation\\\", \\\"authors\\\": \\\"Chen, Xinyun and Aksitov, Renat and Alon, Uri and Ren, Jie and Xiao, Kefan and Y...\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"arXiv preprint (ICML 2024 Workshop ICL)\\\"}, {\\\"key\\\": \\\"cobbe2021verifiers\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Training Verifiers to Solve Math Word Problems\\\", \\\"authors\\\": \\\"Cobbe, Karl and Kosaraju, Vineet and Bavarian, Mohammad and Chen, Mark and Jun, ...\\\", \\\"year\\\": \\\"2021\\\", \\\"venue\\\": \\\"arXiv preprint arXiv:2110.14168\\\"}, {\\\"key\\\": \\\"culotta2004confidence\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Confidence Estimation for Information Extraction\\\", \\\"authors\\\": \\\"Culotta, Aron and McCallum, Andrew\\\", \\\"year\\\": \\\"2004\\\", \\\"venue\\\": \\\"HLT-NAACL 2004\\\"}, {\\\"key\\\": \\\"derczynski2017wnut\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Results of the WNUT2017 Shared Task on Novel and Emerging Entity Recognition\\\", \\\"authors\\\": \\\"Derczynski, Leon and Nichols, Eric and Erp, Marieke van and Limsopatham, Nut\\\", \\\"year\\\": \\\"2017\\\", \\\"venue\\\": \\\"W-NUT Workshop at EMNLP 2017\\\"}, {\\\"key\\\": \\\"desai2020calibration\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Calibration of Pre-trained Transformers\\\", \\\"authors\\\": \\\"Desai, Shrey and Durrett, Greg\\\", \\\"year\\\": \\\"2020\\\", \\\"venue\\\": \\\"Proceedings of the 2020 Conference on Empirical Methods in Natural Language Proc...\\\"}, {\\\"key\\\": \\\"fisch2021conformal\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Few-Shot Conformal Prediction with Auxiliary Tasks\\\", \\\"authors\\\": \\\"Fisch, Adam and Schuster, Tal and Jaakkola, Tommi and Barzilay, Regina\\\", \\\"year\\\": \\\"2021\\\", \\\"venue\\\": \\\"ICML 2021\\\"}, {\\\"key\\\": \\\"fleiss1971agreement\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Measuring nominal scale agreement among many raters.\\\", \\\"authors\\\": \\\"Fleiss, Joseph L.\\\", \\\"year\\\": \\\"1971\\\", \\\"venue\\\": \\\"Psychological Bulletin\\\"}, {\\\"key\\\": \\\"gal2016dropout\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Dropout as a Bayesian Approximation: Representing Model Uncertainty in Deep Learning\\\", \\\"authors\\\": \\\"Gal, Yarin and Ghahramani, Zoubin\\\", \\\"year\\\": \\\"2016\\\", \\\"venue\\\": \\\"ICML 2016\\\"}, {\\\"key\\\": \\\"geifman2017selective\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Selective Classification for Deep Neural Networks\\\", \\\"authors\\\": \\\"Geifman, Yonatan and El-Yaniv, Ran\\\", \\\"year\\\": \\\"2017\\\", \\\"venue\\\": \\\"NeurIPS 2017\\\"}, {\\\"key\\\": \\\"feng2025optimal\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Optimal Self-Consistency for Efficient Reasoning with Large Language Models\\\", \\\"authors\\\": \\\"Feng, Austin and Alonso, Marius and Odonnat, Ambroise\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"arXiv preprint arXiv:2511.12309\\\"}, {\\\"key\\\": \\\"geng2024confidence\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"A Survey of Confidence Estimation and Calibration in Large Language Models\\\", \\\"authors\\\": \\\"Geng, Jiahui and Cai, Fengyu and Wang, Yuxia and Koeppl, Heinz and Nakov, Presla...\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"Proceedings of the 2024 Conference of the North American Chapter of the Associat...\\\"}, {\\\"key\\\": \\\"guo2017calibration\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"On Calibration of Modern Neural Networks\\\", \\\"authors\\\": \\\"Guo, Chuan and Pleiss, Geoff and Sun, Yu and Weinberger, Kilian Q.\\\", \\\"year\\\": \\\"2017\\\", \\\"venue\\\": \\\"ICML 2017\\\"}, {\\\"key\\\": \\\"hobelsberger2025systematic\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Systematic Evaluation of Uncertainty Estimation Methods in Large Language Models\\\", \\\"authors\\\": \\\"Hobelsberger, Christian and Winner, Theresa and Nawroth, Andreas and Mitevski, O...\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"arXiv preprint arXiv:2510.20460\\\"}, {\\\"key\\\": \\\"jaccard1901distribution\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Étude comparative de la distribution florale dans une portion des Alpes et du Jura\\\", \\\"authors\\\": \\\"Jaccard, Paul\\\", \\\"year\\\": \\\"1901\\\", \\\"venue\\\": \\\"Bulletin de la Société Vaudoise des Sciences Naturelles\\\"}, {\\\"key\\\": \\\"josifoski2022genie\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"GenIE: Generative Information Extraction\\\", \\\"authors\\\": \\\"Josifoski, Martin and De Cao, Nicola and Peyrard, Maxime and Petroni, Fabio and ...\\\", \\\"year\\\": \\\"2022\\\", \\\"venue\\\": \\\"Proceedings of the 2022 Conference of the North American Chapter of the Associat...\\\"}, {\\\"key\\\": \\\"kadavath2022language\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Language Models (Mostly) Know What They Know\\\", \\\"authors\\\": \\\"Kadavath, Saurav and Conerly, Tom and Askell, Amanda and Henighan, Tom and Drain...\\\", \\\"year\\\": \\\"2022\\\", \\\"venue\\\": \\\"arXiv preprint arXiv:2207.05221\\\"}, {\\\"key\\\": \\\"kang2025selfcertainty\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Scalable Best-of-N Selection for Large Language Models via Self-Certainty\\\", \\\"authors\\\": \\\"Kang, Zhewei and Zhao, Xuandong and Song, Dawn\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"NeurIPS 2025\\\"}, {\\\"key\\\": \\\"kim2026reasc\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Reliability-Aware Adaptive Self-Consistency for Efficient Sampling in LLM Reasoning\\\", \\\"authors\\\": \\\"Kim, Junseok and Yang, Nakyeong and Min, Kyungmin and Jung, Kyomin\\\", \\\"year\\\": \\\"2026\\\", \\\"venue\\\": \\\"ACL 2026\\\"}, {\\\"key\\\": \\\"kossen2024semantic\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Semantic Entropy Probes: Robust and Cheap Hallucination Detection in LLMs\\\", \\\"authors\\\": \\\"Kossen, Jannik and Han, Jiatong and Razzak, Muhammed and Schut, Lisa and Malik, ...\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"arXiv preprint arXiv:2406.15927\\\"}, {\\\"key\\\": \\\"li2025llms\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"LLMs Can Generate a Better Answer by Aggregating Their Own Responses\\\", \\\"authors\\\": \\\"Li, Zichong and Feng, Xinyu and Cai, Yuheng and Zhang, Zixuan and Liu, Tianyi an...\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"arXiv preprint arXiv:2503.04104\\\"}, {\\\"key\\\": \\\"kuhn2023semantic\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Semantic Uncertainty: Linguistic Invariances for Uncertainty Estimation in Natural Language Generation\\\", \\\"authors\\\": \\\"Kuhn, Lorenz and Gal, Yarin and Farquhar, Sebastian\\\", \\\"year\\\": \\\"2023\\\", \\\"venue\\\": \\\"ICLR 2023\\\"}, {\\\"key\\\": \\\"lakshminarayanan2017ensembles\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Simple and Scalable Predictive Uncertainty Estimation using Deep Ensembles\\\", \\\"authors\\\": \\\"Lakshminarayanan, Balaji and Pritzel, Alexander and Blundell, Charles\\\", \\\"year\\\": \\\"2017\\\", \\\"venue\\\": \\\"NeurIPS 2017\\\"}, {\\\"key\\\": \\\"li2023codeie\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"CodeIE: Large Code Generation Models are Better Few-Shot Information Extractors\\\", \\\"authors\\\": \\\"Li, Peng and Sun, Tianxiang and Tang, Qiong and Yan, Hang and Wu, Yuanbin and Hu...\\\", \\\"year\\\": \\\"2023\\\", \\\"venue\\\": \\\"Proceedings of the 61st Annual Meeting of the Association for Computational Ling...\\\"}, {\\\"key\\\": \\\"lightman2024verify\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Let's Verify Step by Step\\\", \\\"authors\\\": \\\"Lightman, Hunter and Kosaraju, Vineet and Burda, Yura and Edwards, Harri and Bak...\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"ICLR 2024\\\"}, {\\\"key\\\": \\\"luan2018scierc\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Multi-Task Identification of Entities, Relations, and Coreference for Scientific Knowledge Graph Construction\\\", \\\"authors\\\": \\\"Luan, Yi and He, Luheng and Ostendorf, Mari and Hajishirzi, Hannaneh\\\", \\\"year\\\": \\\"2018\\\", \\\"venue\\\": \\\"Proceedings of the 2018 Conference on Empirical Methods in Natural Language Proc...\\\"}, {\\\"key\\\": \\\"manakul2023selfcheckgpt\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"SelfCheckGPT: Zero-Resource Black-Box Hallucination Detection for Generative Large Language Models\\\", \\\"authors\\\": \\\"Manakul, Potsawee and Liusie, Adian and Gales, Mark\\\", \\\"year\\\": \\\"2023\\\", \\\"venue\\\": \\\"Proceedings of the 2023 Conference on Empirical Methods in Natural Language Proc...\\\"}, {\\\"key\\\": \\\"nedellec2026consistency\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Consistency–accuracy correlation in hard-prompted LLMs for entity and relation extraction: empirical findings from plant...\\\", \\\"authors\\\": \\\"Yao, Xinzhi and Nédellec, Claire and Xia, Jingbo and Bossy, Robert\\\", \\\"year\\\": \\\"2026\\\", \\\"venue\\\": \\\"Genomics \\\\\\\\& Informatics\\\"}, {\\\"key\\\": \\\"oh2025latentsc\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Latent Self-Consistency for Reliable Majority-Set Selection in Short- and Long-Answer Reasoning\\\", \\\"authors\\\": \\\"Oh, Jungsuk and Lee, Jay-Yoon\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"arXiv preprint arXiv:2508.18395\\\"}, {\\\"key\\\": \\\"sainz2024gollie\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"GoLLIE: Annotation Guidelines improve Zero-Shot Information-Extraction\\\", \\\"authors\\\": \\\"Sainz, Oscar and García-Ferrero, Iker and Agerri, Rodrigo and Lacalle, Oier Lope...\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"ICLR 2024\\\"}, {\\\"key\\\": \\\"shelmanov2021active\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Active Learning for Sequence Tagging with Deep Pre-trained Models and Bayesian Uncertainty Estimates\\\", \\\"authors\\\": \\\"Shelmanov, Artem and Puzyrev, Dmitri and Kupriyanova, Lyubov and Belyakov, Denis...\\\", \\\"year\\\": \\\"2021\\\", \\\"venue\\\": \\\"Proceedings of the 16th Conference of the European Chapter of the Association fo...\\\"}, {\\\"key\\\": \\\"snell2024scaling\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters\\\", \\\"authors\\\": \\\"Snell, Charlie and Lee, Jaehoon and Xu, Kelvin and Kumar, Aviral\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"ICLR 2025\\\"}, {\\\"key\\\": \\\"taubenfeld2025cisc\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Confidence Improves Self-Consistency in LLMs\\\", \\\"authors\\\": \\\"Taubenfeld, Amir and Sheffer, Tom and Ofek, Eran and Feder, Amir and Goldstein, ...\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"Findings of the Association for Computational Linguistics: ACL 2025\\\"}, {\\\"key\\\": \\\"thirukovalluru2024atomic\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Atomic Self-Consistency for Better Long Form Generations\\\", \\\"authors\\\": \\\"Thirukovalluru, Raghuveer and Huang, Yukun and Dhingra, Bhuwan\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"Proceedings of the 2024 Conference on Empirical Methods in Natural Language Proc...\\\"}, {\\\"key\\\": \\\"tjongkimsang2003conll\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Introduction to the CoNLL-2003 Shared Task: Language-Independent Named Entity Recognition\\\", \\\"authors\\\": \\\"Sang, Erik F. Tjong Kim and Meulder, Fien De\\\", \\\"year\\\": \\\"2003\\\", \\\"venue\\\": \\\"CoNLL 2003\\\"}, {\\\"key\\\": \\\"vashurin2025cocoa\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Uncertainty Quantification for LLMs through Minimum Bayes Risk: Bridging Confidence and Consistency\\\", \\\"authors\\\": \\\"Vashurin, Roman and Goloburda, Maiya and Ilina, Albina and Rubashevskii, Aleksan...\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"NeurIPS 2025\\\"}, {\\\"key\\\": \\\"wadhwa2023revisiting\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Revisiting Relation Extraction in the era of Large Language Models\\\", \\\"authors\\\": \\\"Wadhwa, Somin and Amir, Silvio and Wallace, Byron\\\", \\\"year\\\": \\\"2023\\\", \\\"venue\\\": \\\"Proceedings of the 61st Annual Meeting of the Association for Computational Ling...\\\"}, {\\\"key\\\": \\\"wang2023instructuie\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"InstructUIE: Multi-task Instruction Tuning for Unified Information Extraction\\\", \\\"authors\\\": \\\"Wang, Xiao and Zhou, Weikang and Zu, Can and Xia, Han and Chen, Tianze and Zhang...\\\", \\\"year\\\": \\\"2023\\\", \\\"venue\\\": \\\"arXiv preprint arXiv:2304.08085\\\"}, {\\\"key\\\": \\\"wang2023selfconsistency\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Self-Consistency Improves Chain of Thought Reasoning in Language Models\\\", \\\"authors\\\": \\\"Wang, Xuezhi and Wei, Jason and Schuurmans, Dale and Le, Quoc and Chi, Ed and Na...\\\", \\\"year\\\": \\\"2023\\\", \\\"venue\\\": \\\"ICLR 2023\\\"}, {\\\"key\\\": \\\"wang2025make\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Make Every Penny Count: Difficulty-Adaptive Self-Consistency for Cost-Efficient Reasoning\\\", \\\"authors\\\": \\\"Wang, Xinglin and Feng, Shaoxiong and Li, Yiwei and Yuan, Peiwen and Zhang, Yueq...\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"Findings of the Association for Computational Linguistics: NAACL 2025\\\"}, {\\\"key\\\": \\\"wang2024mathshepherd\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Math-Shepherd: Verify and Reinforce LLMs Step-by-step without Human Annotations\\\", \\\"authors\\\": \\\"Wang, Peiyi and Li, Lei and Shao, Zhihong and Xu, Runxin and Dai, Damai and Li, ...\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"ACL 2024\\\"}, {\\\"key\\\": \\\"wang2025rankedvoting\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Ranked Voting based Self-Consistency of Large Language Models\\\", \\\"authors\\\": \\\"Wang, Weiqin and Wang, Yile and Huang, Hui\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"ACL Findings 2025\\\"}, {\\\"key\\\": \\\"wen2025know\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Know Your Limits: A Survey of Abstention in Large Language Models\\\", \\\"authors\\\": \\\"Wen, Bingbing and Yao, Jihan and Feng, Shangbin and Xu, Chenjun and Tsvetkov, Yu...\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"Transactions of the Association for Computational Linguistics\\\"}, {\\\"key\\\": \\\"willard2023guided\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Efficient Guided Generation for Large Language Models\\\", \\\"authors\\\": \\\"Willard, Brandon T. and Louf, Rémi\\\", \\\"year\\\": \\\"2023\\\", \\\"venue\\\": \\\"arXiv preprint arXiv:2307.09702\\\"}, {\\\"key\\\": \\\"xia2025survey\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"A Survey of Uncertainty Estimation Methods on Large Language Models\\\", \\\"authors\\\": \\\"Xia, Zhiqiu and Xu, Jinxuan and Zhang, Yuqian and Liu, Hang\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"ACL Findings 2025\\\"}, {\\\"key\\\": \\\"xiao2019uncertainty\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Quantifying Uncertainties in Natural Language Processing Tasks\\\", \\\"authors\\\": \\\"Xiao, Yijun and Wang, William Yang\\\", \\\"year\\\": \\\"2019\\\", \\\"venue\\\": \\\"Proceedings of the AAAI Conference on Artificial Intelligence\\\"}, {\\\"key\\\": \\\"zhang2023ener\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"E-NER: Evidential Deep Learning for Trustworthy Named Entity Recognition\\\", \\\"authors\\\": \\\"Zhang, Zhen and Hu, Mengting and Zhao, Shiwan and Huang, Minlie and Wang, Haotia...\\\", \\\"year\\\": \\\"2023\\\", \\\"venue\\\": \\\"Findings of the Association for Computational Linguistics: ACL 2023\\\"}, {\\\"key\\\": \\\"zhou2024uniner\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"UniversalNER: Targeted Distillation from Large Language Models for Open Named Entity Recognition\\\", \\\"authors\\\": \\\"Zhou, Wenxuan and Zhang, Sheng and Gu, Yu and Chen, Muhao and Poon, Hoifung\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"Proceedings of the International Conference on Learning Representations (ICLR)\\\"}], \\\"tex_citations\\\": [{\\\"key\\\": \\\"wang2023selfconsistency\\\", \\\"file\\\": \\\"sections/introduction.tex\\\", \\\"line\\\": 4, \\\"command\\\": \\\"citealp\\\"}, {\\\"key\\\": \\\"snell2024scaling\\\", \\\"file\\\": \\\"sections/introduction.tex\\\", \\\"line\\\": 5, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"brown2024monkeys\\\", \\\"file\\\": \\\"sections/introduction.tex\\\", \\\"line\\\": 5, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"wang2023selfconsistency\\\", \\\"file\\\": \\\"sections/introduction.tex\\\", \\\"line\\\": 15, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"chen2024usc\\\", \\\"file\\\": \\\"sections/introduction.tex\\\", \\\"line\\\": 15, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"taubenfeld2025cisc\\\", \\\"file\\\": \\\"sections/introduction.tex\\\", \\\"line\\\": 15, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"kang2025selfcertainty\\\", \\\"file\\\": \\\"sections/introduction.tex\\\", \\\"line\\\": 15, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"nedellec2026consistency\\\", \\\"file\\\": \\\"sections/introduction.tex\\\", \\\"line\\\": 16, \\\"command\\\": \\\"citet\\\"}, {\\\"key\\\": \\\"luan2018scierc\\\", \\\"file\\\": \\\"sections/introduction.tex\\\", \\\"line\\\": 31, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"tjongkimsang2003conll\\\", \\\"file\\\": \\\"sections/introduction.tex\\\", \\\"line\\\": 31, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"derczynski2017wnut\\\", \\\"file\\\": \\\"sections/introduction.tex\\\", \\\"line\\\": 31, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"wang2023selfconsistency\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 4, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"chen2024usc\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 5, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"thirukovalluru2024atomic\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 5, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"manakul2023selfcheckgpt\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 5, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"snell2024scaling\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 6, \\\"command\\\": \\\"citet\\\"}, {\\\"key\\\": \\\"brown2024monkeys\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 6, \\\"command\\\": \\\"citet\\\"}, {\\\"key\\\": \\\"taubenfeld2025cisc\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 7, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"kang2025selfcertainty\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 7, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"kim2026reasc\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 7, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"wang2025rankedvoting\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 7, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"oh2025latentsc\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 7, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"feng2025optimal\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 8, \\\"command\\\": \\\"citet\\\"}, {\\\"key\\\": \\\"wang2025make\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 8, \\\"command\\\": \\\"citet\\\"}, {\\\"key\\\": \\\"li2025llms\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 8, \\\"command\\\": \\\"citet\\\"}, {\\\"key\\\": \\\"nedellec2026consistency\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 13, \\\"command\\\": \\\"citet\\\"}, {\\\"key\\\": \\\"vashurin2025cocoa\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 16, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"zhou2024uniner\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 17, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"sainz2024gollie\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 17, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"josifoski2022genie\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 17, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"li2023codeie\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 17, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"wadhwa2023revisiting\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 17, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"wang2023instructuie\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 17, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"willard2023guided\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 17, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"geng2024confidence\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 20, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"wen2025know\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 20, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"xia2025survey\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 20, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"hobelsberger2025systematic\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 20, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"kuhn2023semantic\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 21, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"kossen2024semantic\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 21, \\\"command\\\": \\\"citet\\\"}, {\\\"key\\\": \\\"kadavath2022language\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 21, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"guo2017calibration\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 22, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"desai2020calibration\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 22, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"lakshminarayanan2017ensembles\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 23, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"gal2016dropout\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 23, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"xiao2019uncertainty\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 24, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"shelmanov2021active\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 24, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"zhang2023ener\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 24, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"fisch2021conformal\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 25, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"angelopoulos2021conformal\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 25, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"cobbe2021verifiers\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 25, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"lightman2024verify\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 25, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"wang2024mathshepherd\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 25, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"geifman2017selective\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 26, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"culotta2004confidence\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 26, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"willard2023guided\\\", \\\"file\\\": \\\"sections/method.tex\\\", \\\"line\\\": 5, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"fleiss1971agreement\\\", \\\"file\\\": \\\"sections/method.tex\\\", \\\"line\\\": 32, \\\"command\\\": \\\"citet\\\"}, {\\\"key\\\": \\\"jaccard1901distribution\\\", \\\"file\\\": \\\"sections/method.tex\\\", \\\"line\\\": 41, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"luan2018scierc\\\", \\\"file\\\": \\\"sections/experiments.tex\\\", \\\"line\\\": 9, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"tjongkimsang2003conll\\\", \\\"file\\\": \\\"sections/experiments.tex\\\", \\\"line\\\": 10, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"derczynski2017wnut\\\", \\\"file\\\": \\\"sections/experiments.tex\\\", \\\"line\\\": 11, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"willard2023guided\\\", \\\"file\\\": \\\"sections/experiments.tex\\\", \\\"line\\\": 17, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"kuhn2023semantic\\\", \\\"file\\\": \\\"sections/experiments.tex\\\", \\\"line\\\": 64, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"brown2024monkeys\\\", \\\"file\\\": \\\"sections/experiments.tex\\\", \\\"line\\\": 136, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"snell2024scaling\\\", \\\"file\\\": \\\"sections/experiments.tex\\\", \\\"line\\\": 136, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"cobbe2021verifiers\\\", \\\"file\\\": \\\"sections/experiments.tex\\\", \\\"line\\\": 136, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"cobbe2021verifiers\\\", \\\"file\\\": \\\"sections/discussion.tex\\\", \\\"line\\\": 31, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"brown2024monkeys\\\", \\\"file\\\": \\\"sections/appendix.tex\\\", \\\"line\\\": 184, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"snell2024scaling\\\", \\\"file\\\": \\\"sections/appendix.tex\\\", \\\"line\\\": 184, \\\"command\\\": \\\"cite\\\"}], \\\"online_verification\\\": [{\\\"key\\\": \\\"angelopoulos2021conformal\\\", \\\"title\\\": \\\"Uncertainty Sets for Image Classifiers using Conformal Prediction\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Uncertainty Sets for Image Classifiers using Conformal Prediction\\\", \\\"matched_year\\\": \\\"2020\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"brown2024monkeys\\\", \\\"title\\\": \\\"Large Language Monkeys: Scaling Inference Compute with Repeated Sampling\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Large Language Monkeys: Scaling Inference Compute with Repeated Sampling\\\", \\\"matched_year\\\": \\\"2024\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"chen2024usc\\\", \\\"title\\\": \\\"Universal Self-Consistency for Large Language Model Generation\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Universal Self-Consistency for Large Language Model Generation\\\", \\\"matched_year\\\": \\\"2023\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"cobbe2021verifiers\\\", \\\"title\\\": \\\"Training Verifiers to Solve Math Word Problems\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Training Verifiers to Solve Math Word Problems\\\", \\\"matched_year\\\": \\\"2021\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"culotta2004confidence\\\", \\\"title\\\": \\\"Confidence Estimation for Information Extraction\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Confidence estimation for information extraction\\\", \\\"matched_year\\\": \\\"2004\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"derczynski2017wnut\\\", \\\"title\\\": \\\"Results of the WNUT2017 Shared Task on Novel and Emerging Entity Recognition\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Results of the WNUT2017 Shared Task on Novel and Emerging Entity Recognition\\\", \\\"matched_year\\\": \\\"2017\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"desai2020calibration\\\", \\\"title\\\": \\\"Calibration of Pre-trained Transformers\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Calibration of Pre-trained Transformers\\\", \\\"matched_year\\\": \\\"2020\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"fisch2021conformal\\\", \\\"title\\\": \\\"Few-Shot Conformal Prediction with Auxiliary Tasks\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Few-shot Conformal Prediction with Auxiliary Tasks\\\", \\\"matched_year\\\": \\\"2021\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"fleiss1971agreement\\\", \\\"title\\\": \\\"Measuring nominal scale agreement among many raters.\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Measuring nominal scale agreement among many raters.\\\", \\\"matched_year\\\": \\\"1971\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"gal2016dropout\\\", \\\"title\\\": \\\"Dropout as a Bayesian Approximation: Representing Model Uncertainty in Deep Learning\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Dropout as a Bayesian Approximation: Representing Model Uncertainty in Deep Learning\\\", \\\"matched_year\\\": \\\"2015\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"geifman2017selective\\\", \\\"title\\\": \\\"Selective Classification for Deep Neural Networks\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Selective Classification for Deep Neural Networks\\\", \\\"matched_year\\\": \\\"2017\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"feng2025optimal\\\", \\\"title\\\": \\\"Optimal Self-Consistency for Efficient Reasoning with Large Language Models\\\", \\\"status\\\": \\\"mismatch\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Optimal Self-Consistency for Efficient Reasoning with Large Language Models\\\", \\\"matched_year\\\": \\\"2025\\\", \\\"mismatch_fields\\\": [\\\"first_author: bib=feng vs api=austin\\\"], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"geng2024confidence\\\", \\\"title\\\": \\\"A Survey of Confidence Estimation and Calibration in Large Language Models\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"A Survey of Confidence Estimation and Calibration in Large Language Models\\\", \\\"matched_year\\\": \\\"2024\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"guo2017calibration\\\", \\\"title\\\": \\\"On Calibration of Modern Neural Networks\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"On Calibration of Modern Neural Networks\\\", \\\"matched_year\\\": \\\"2017\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"hobelsberger2025systematic\\\", \\\"title\\\": \\\"Systematic Evaluation of Uncertainty Estimation Methods in Large Language Models\\\", \\\"status\\\": \\\"not_found\\\", \\\"confidence\\\": 0.236, \\\"matched_title\\\": \\\"A new criterion for assessing discriminant validity in variance-based structural equation modeling\\\", \\\"matched_year\\\": \\\"\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"best match similarity 0.24 below threshold 0.82\\\"}, {\\\"key\\\": \\\"jaccard1901distribution\\\", \\\"title\\\": \\\"Étude comparative de la distribution florale dans une portion des Alpes et du Jura\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Étude comparative de la distribution florale dans une portion des Alpes et du Jura\\\", \\\"matched_year\\\": \\\"1901\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"josifoski2022genie\\\", \\\"title\\\": \\\"GenIE: Generative Information Extraction\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"GenIE: Generative Information Extraction\\\", \\\"matched_year\\\": \\\"2022\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"kadavath2022language\\\", \\\"title\\\": \\\"Language Models (Mostly) Know What They Know\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Language Models (Mostly) Know What They Know\\\", \\\"matched_year\\\": \\\"2022\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"kang2025selfcertainty\\\", \\\"title\\\": \\\"Scalable Best-of-N Selection for Large Language Models via Self-Certainty\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Scalable Best-of-N Selection for Large Language Models via Self-Certainty\\\", \\\"matched_year\\\": \\\"2025\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"kim2026reasc\\\", \\\"title\\\": \\\"Reliability-Aware Adaptive Self-Consistency for Efficient Sampling in LLM Reasoning\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Reliability-Aware Adaptive Self-Consistency for Efficient Sampling in LLM Reasoning\\\", \\\"matched_year\\\": \\\"2026\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"kossen2024semantic\\\", \\\"title\\\": \\\"Semantic Entropy Probes: Robust and Cheap Hallucination Detection in LLMs\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Semantic Entropy Probes: Robust and Cheap Hallucination Detection in LLMs\\\", \\\"matched_year\\\": \\\"2024\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"li2025llms\\\", \\\"title\\\": \\\"LLMs Can Generate a Better Answer by Aggregating Their Own Responses\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"LLMs Can Generate a Better Answer by Aggregating Their Own Responses\\\", \\\"matched_year\\\": \\\"2025\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"kuhn2023semantic\\\", \\\"title\\\": \\\"Semantic Uncertainty: Linguistic Invariances for Uncertainty Estimation in Natural Language Generation\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Semantic Uncertainty: Linguistic Invariances for Uncertainty Estimation in Natural Language Generation\\\", \\\"matched_year\\\": \\\"2023\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"lakshminarayanan2017ensembles\\\", \\\"title\\\": \\\"Simple and Scalable Predictive Uncertainty Estimation using Deep Ensembles\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Simple and Scalable Predictive Uncertainty Estimation using Deep Ensembles\\\", \\\"matched_year\\\": \\\"2016\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"li2023codeie\\\", \\\"title\\\": \\\"CodeIE: Large Code Generation Models are Better Few-Shot Information Extractors\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"CodeIE: Large Code Generation Models are Better Few-Shot Information Extractors\\\", \\\"matched_year\\\": \\\"2023\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"lightman2024verify\\\", \\\"title\\\": \\\"Let's Verify Step by Step\\\", \\\"status\\\": \\\"not_found\\\", \\\"confidence\\\": 0.246, \\\"matched_title\\\": \\\"Development and dosimetric verification of static SHArc: Step‐and‐shoot carbon ion arc therapy for LET &lt;sub>d&lt;/sub> escalation in pancreatic tumors\\\", \\\"matched_year\\\": \\\"\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"best match similarity 0.25 below threshold 0.82\\\"}, {\\\"key\\\": \\\"luan2018scierc\\\", \\\"title\\\": \\\"Multi-Task Identification of Entities, Relations, and Coreference for Scientific Knowledge Graph Construction\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Multi-Task Identification of Entities, Relations, and Coreference for Scientific Knowledge Graph Construction\\\", \\\"matched_year\\\": \\\"2018\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"manakul2023selfcheckgpt\\\", \\\"title\\\": \\\"SelfCheckGPT: Zero-Resource Black-Box Hallucination Detection for Generative Large Language Models\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"SelfCheckGPT: Zero-Resource Black-Box Hallucination Detection for Generative Large Language Models\\\", \\\"matched_year\\\": \\\"2023\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"nedellec2026consistency\\\", \\\"title\\\": \\\"Consistency–accuracy correlation in hard-prompted LLMs for entity and relation extraction: empirical findings from plant-health data\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Consistency–accuracy correlation in hard-prompted LLMs for entity and relation extraction: empirical findings from plant-health data\\\", \\\"matched_year\\\": \\\"2026\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"oh2025latentsc\\\", \\\"title\\\": \\\"Latent Self-Consistency for Reliable Majority-Set Selection in Short- and Long-Answer Reasoning\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Latent Self-Consistency for Reliable Majority-Set Selection in Short- and Long-Answer Reasoning\\\", \\\"matched_year\\\": \\\"2026\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"sainz2024gollie\\\", \\\"title\\\": \\\"GoLLIE: Annotation Guidelines improve Zero-Shot Information-Extraction\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"GoLLIE: Annotation Guidelines improve Zero-Shot Information-Extraction\\\", \\\"matched_year\\\": \\\"2023\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"shelmanov2021active\\\", \\\"title\\\": \\\"Active Learning for Sequence Tagging with Deep Pre-trained Models and Bayesian Uncertainty Estimates\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Active Learning for Sequence Tagging with Deep Pre-trained Models and Bayesian Uncertainty Estimates\\\", \\\"matched_year\\\": \\\"2021\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"snell2024scaling\\\", \\\"title\\\": \\\"Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters\\\", \\\"status\\\": \\\"mismatch\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters\\\", \\\"matched_year\\\": \\\"2024\\\", \\\"mismatch_fields\\\": [\\\"first_author: bib=snell vs api=charlie\\\"], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"taubenfeld2025cisc\\\", \\\"title\\\": \\\"Confidence Improves Self-Consistency in LLMs\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Confidence Improves Self-Consistency in LLMs\\\", \\\"matched_year\\\": \\\"2025\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"thirukovalluru2024atomic\\\", \\\"title\\\": \\\"Atomic Self-Consistency for Better Long Form Generations\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Atomic Self-Consistency for Better Long Form Generations\\\", \\\"matched_year\\\": \\\"2024\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"tjongkimsang2003conll\\\", \\\"title\\\": \\\"Introduction to the CoNLL-2003 Shared Task: Language-Independent Named Entity Recognition\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Introduction to the CoNLL-2003 Shared Task: Language-Independent Named Entity Recognition\\\", \\\"matched_year\\\": \\\"2003\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"vashurin2025cocoa\\\", \\\"title\\\": \\\"Uncertainty Quantification for LLMs through Minimum Bayes Risk: Bridging Confidence and Consistency\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Uncertainty Quantification for LLMs through Minimum Bayes Risk: Bridging Confidence and Consistency\\\", \\\"matched_year\\\": \\\"2025\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"wadhwa2023revisiting\\\", \\\"title\\\": \\\"Revisiting Relation Extraction in the era of Large Language Models\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Revisiting Relation Extraction in the era of Large Language Models\\\", \\\"matched_year\\\": \\\"2023\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"wang2023instructuie\\\", \\\"title\\\": \\\"InstructUIE: Multi-task Instruction Tuning for Unified Information Extraction\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"InstructUIE: Multi-task Instruction Tuning for Unified Information Extraction\\\", \\\"matched_year\\\": \\\"2023\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"wang2023selfconsistency\\\", \\\"title\\\": \\\"Self-Consistency Improves Chain of Thought Reasoning in Language Models\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Self-Consistency Improves Chain of Thought Reasoning in Language Models\\\", \\\"matched_year\\\": \\\"2022\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"wang2025make\\\", \\\"title\\\": \\\"Make Every Penny Count: Difficulty-Adaptive Self-Consistency for Cost-Efficient Reasoning\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Make Every Penny Count: Difficulty-Adaptive Self-Consistency for Cost-Efficient Reasoning\\\", \\\"matched_year\\\": \\\"2025\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"wang2024mathshepherd\\\", \\\"title\\\": \\\"Math-Shepherd: Verify and Reinforce LLMs Step-by-step without Human Annotations\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Math-Shepherd: Verify and Reinforce LLMs Step-by-step without Human Annotations\\\", \\\"matched_year\\\": \\\"2024\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"wang2025rankedvoting\\\", \\\"title\\\": \\\"Ranked Voting based Self-Consistency of Large Language Models\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Ranked Voting based Self-Consistency of Large Language Models\\\", \\\"matched_year\\\": \\\"2025\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"wen2025know\\\", \\\"title\\\": \\\"Know Your Limits: A Survey of Abstention in Large Language Models\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Know Your Limits: A Survey of Abstention in Large Language Models\\\", \\\"matched_year\\\": \\\"2025\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"willard2023guided\\\", \\\"title\\\": \\\"Efficient Guided Generation for Large Language Models\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Efficient Guided Generation for Large Language Models\\\", \\\"matched_year\\\": \\\"2023\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"xia2025survey\\\", \\\"title\\\": \\\"A Survey of Uncertainty Estimation Methods on Large Language Models\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"A Survey of Uncertainty Estimation Methods on Large Language Models\\\", \\\"matched_year\\\": \\\"2025\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"xiao2019uncertainty\\\", \\\"title\\\": \\\"Quantifying Uncertainties in Natural Language Processing Tasks\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Quantifying Uncertainties in Natural Language Processing Tasks\\\", \\\"matched_year\\\": \\\"2019\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"zhang2023ener\\\", \\\"title\\\": \\\"E-NER: Evidential Deep Learning for Trustworthy Named Entity Recognition\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"E-NER: Evidential Deep Learning for Trustworthy Named Entity Recognition\\\", \\\"matched_year\\\": \\\"2023\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"zhou2024uniner\\\", \\\"title\\\": \\\"UniversalNER: Targeted Distillation from Large Language Models for Open Named Entity Recognition\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"UniversalNER: Targeted Distillation from Large Language Models for Open Named Entity Recognition\\\", \\\"matched_year\\\": \\\"2023\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}]}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"summary\": {\"total_bib_entries\": 49, \"total_citations\": 69, \"unique_cited_keys\": 49, \"orphan_bib\": 0, \"missing_bib\": 0, \"duplicate_keys\": 0, \"online_verified\": 45, \"online_not_found\": 2, \"online_mismatch\": 2}, \"cross_check\": {\"orphan_bib\": [], \"missing_bib\": [], \"orphan_count\": 0, \"missing_count\": 0}, \"bib_entries\": [{\"key\": \"angelopoulos2021conformal\", \"type\": \"inproceedings\", \"title\": \"Uncertainty Sets for Image Classifiers using Conformal Prediction\", \"authors\": \"Angelopoulos, Anastasios N. and Bates, Stephen and Malik, Jitendra and Jordan, M...\", \"year\": \"2021\", \"venue\": \"ICLR 2021\"}, {\"key\": \"brown2024monkeys\", \"type\": \"article\", \"title\": \"Large Language Monkeys: Scaling Inference Compute with Repeated Sampling\", \"authors\": \"Brown, Bradley and Juravsky, Jordan and Ehrlich, Ryan and Clark, Ronald and Le, ...\", \"year\": \"2024\", \"venue\": \"arXiv preprint arXiv:2407.21787\"}, {\"key\": \"chen2024usc\", \"type\": \"inproceedings\", \"title\": \"Universal Self-Consistency for Large Language Model Generation\", \"authors\": \"Chen, Xinyun and Aksitov, Renat and Alon, Uri and Ren, Jie and Xiao, Kefan and Y...\", \"year\": \"2024\", \"venue\": \"arXiv preprint (ICML 2024 Workshop ICL)\"}, {\"key\": \"cobbe2021verifiers\", \"type\": \"article\", \"title\": \"Training Verifiers to Solve Math Word Problems\", \"authors\": \"Cobbe, Karl and Kosaraju, Vineet and Bavarian, Mohammad and Chen, Mark and Jun, ...\", \"year\": \"2021\", \"venue\": \"arXiv preprint arXiv:2110.14168\"}, {\"key\": \"culotta2004confidence\", \"type\": \"inproceedings\", \"title\": \"Confidence Estimation for Information Extraction\", \"authors\": \"Culotta, Aron and McCallum, Andrew\", \"year\": \"2004\", \"venue\": \"HLT-NAACL 2004\"}, {\"key\": \"derczynski2017wnut\", \"type\": \"inproceedings\", \"title\": \"Results of the WNUT2017 Shared Task on Novel and Emerging Entity Recognition\", \"authors\": \"Derczynski, Leon and Nichols, Eric and Erp, Marieke van and Limsopatham, Nut\", \"year\": \"2017\", \"venue\": \"W-NUT Workshop at EMNLP 2017\"}, {\"key\": \"desai2020calibration\", \"type\": \"inproceedings\", \"title\": \"Calibration of Pre-trained Transformers\", \"authors\": \"Desai, Shrey and Durrett, Greg\", \"year\": \"2020\", \"venue\": \"Proceedings of the 2020 Conference on Empirical Methods in Natural Language Proc...\"}, {\"key\": \"fisch2021conformal\", \"type\": \"inproceedings\", \"title\": \"Few-Shot Conformal Prediction with Auxiliary Tasks\", \"authors\": \"Fisch, Adam and Schuster, Tal and Jaakkola, Tommi and Barzilay, Regina\", \"year\": \"2021\", \"venue\": \"ICML 2021\"}, {\"key\": \"fleiss1971agreement\", \"type\": \"article\", \"title\": \"Measuring nominal scale agreement among many raters.\", \"authors\": \"Fleiss, Joseph L.\", \"year\": \"1971\", \"venue\": \"Psychological Bulletin\"}, {\"key\": \"gal2016dropout\", \"type\": \"inproceedings\", \"title\": \"Dropout as a Bayesian Approximation: Representing Model Uncertainty in Deep Learning\", \"authors\": \"Gal, Yarin and Ghahramani, Zoubin\", \"year\": \"2016\", \"venue\": \"ICML 2016\"}, {\"key\": \"geifman2017selective\", \"type\": \"inproceedings\", \"title\": \"Selective Classification for Deep Neural Networks\", \"authors\": \"Geifman, Yonatan and El-Yaniv, Ran\", \"year\": \"2017\", \"venue\": \"NeurIPS 2017\"}, {\"key\": \"feng2025optimal\", \"type\": \"article\", \"title\": \"Optimal Self-Consistency for Efficient Reasoning with Large Language Models\", \"authors\": \"Feng, Austin and Alonso, Marius and Odonnat, Ambroise\", \"year\": \"2025\", \"venue\": \"arXiv preprint arXiv:2511.12309\"}, {\"key\": \"geng2024confidence\", \"type\": \"inproceedings\", \"title\": \"A Survey of Confidence Estimation and Calibration in Large Language Models\", \"authors\": \"Geng, Jiahui and Cai, Fengyu and Wang, Yuxia and Koeppl, Heinz and Nakov, Presla...\", \"year\": \"2024\", \"venue\": \"Proceedings of the 2024 Conference of the North American Chapter of the Associat...\"}, {\"key\": \"guo2017calibration\", \"type\": \"inproceedings\", \"title\": \"On Calibration of Modern Neural Networks\", \"authors\": \"Guo, Chuan and Pleiss, Geoff and Sun, Yu and Weinberger, Kilian Q.\", \"year\": \"2017\", \"venue\": \"ICML 2017\"}, {\"key\": \"hobelsberger2025systematic\", \"type\": \"article\", \"title\": \"Systematic Evaluation of Uncertainty Estimation Methods in Large Language Models\", \"authors\": \"Hobelsberger, Christian and Winner, Theresa and Nawroth, Andreas and Mitevski, O...\", \"year\": \"2025\", \"venue\": \"arXiv preprint arXiv:2510.20460\"}, {\"key\": \"jaccard1901distribution\", \"type\": \"article\", \"title\": \"Étude comparative de la distribution florale dans une portion des Alpes et du Jura\", \"authors\": \"Jaccard, Paul\", \"year\": \"1901\", \"venue\": \"Bulletin de la Société Vaudoise des Sciences Naturelles\"}, {\"key\": \"josifoski2022genie\", \"type\": \"inproceedings\", \"title\": \"GenIE: Generative Information Extraction\", \"authors\": \"Josifoski, Martin and De Cao, Nicola and Peyrard, Maxime and Petroni, Fabio and ...\", \"year\": \"2022\", \"venue\": \"Proceedings of the 2022 Conference of the North American Chapter of the Associat...\"}, {\"key\": \"kadavath2022language\", \"type\": \"article\", \"title\": \"Language Models (Mostly) Know What They Know\", \"authors\": \"Kadavath, Saurav and Conerly, Tom and Askell, Amanda and Henighan, Tom and Drain...\", \"year\": \"2022\", \"venue\": \"arXiv preprint arXiv:2207.05221\"}, {\"key\": \"kang2025selfcertainty\", \"type\": \"inproceedings\", \"title\": \"Scalable Best-of-N Selection for Large Language Models via Self-Certainty\", \"authors\": \"Kang, Zhewei and Zhao, Xuandong and Song, Dawn\", \"year\": \"2025\", \"venue\": \"NeurIPS 2025\"}, {\"key\": \"kim2026reasc\", \"type\": \"inproceedings\", \"title\": \"Reliability-Aware Adaptive Self-Consistency for Efficient Sampling in LLM Reasoning\", \"authors\": \"Kim, Junseok and Yang, Nakyeong and Min, Kyungmin and Jung, Kyomin\", \"year\": \"2026\", \"venue\": \"ACL 2026\"}, {\"key\": \"kossen2024semantic\", \"type\": \"article\", \"title\": \"Semantic Entropy Probes: Robust and Cheap Hallucination Detection in LLMs\", \"authors\": \"Kossen, Jannik and Han, Jiatong and Razzak, Muhammed and Schut, Lisa and Malik, ...\", \"year\": \"2024\", \"venue\": \"arXiv preprint arXiv:2406.15927\"}, {\"key\": \"li2025llms\", \"type\": \"article\", \"title\": \"LLMs Can Generate a Better Answer by Aggregating Their Own Responses\", \"authors\": \"Li, Zichong and Feng, Xinyu and Cai, Yuheng and Zhang, Zixuan and Liu, Tianyi an...\", \"year\": \"2025\", \"venue\": \"arXiv preprint arXiv:2503.04104\"}, {\"key\": \"kuhn2023semantic\", \"type\": \"inproceedings\", \"title\": \"Semantic Uncertainty: Linguistic Invariances for Uncertainty Estimation in Natural Language Generation\", \"authors\": \"Kuhn, Lorenz and Gal, Yarin and Farquhar, Sebastian\", \"year\": \"2023\", \"venue\": \"ICLR 2023\"}, {\"key\": \"lakshminarayanan2017ensembles\", \"type\": \"inproceedings\", \"title\": \"Simple and Scalable Predictive Uncertainty Estimation using Deep Ensembles\", \"authors\": \"Lakshminarayanan, Balaji and Pritzel, Alexander and Blundell, Charles\", \"year\": \"2017\", \"venue\": \"NeurIPS 2017\"}, {\"key\": \"li2023codeie\", \"type\": \"inproceedings\", \"title\": \"CodeIE: Large Code Generation Models are Better Few-Shot Information Extractors\", \"authors\": \"Li, Peng and Sun, Tianxiang and Tang, Qiong and Yan, Hang and Wu, Yuanbin and Hu...\", \"year\": \"2023\", \"venue\": \"Proceedings of the 61st Annual Meeting of the Association for Computational Ling...\"}, {\"key\": \"lightman2024verify\", \"type\": \"inproceedings\", \"title\": \"Let's Verify Step by Step\", \"authors\": \"Lightman, Hunter and Kosaraju, Vineet and Burda, Yura and Edwards, Harri and Bak...\", \"year\": \"2024\", \"venue\": \"ICLR 2024\"}, {\"key\": \"luan2018scierc\", \"type\": \"inproceedings\", \"title\": \"Multi-Task Identification of Entities, Relations, and Coreference for Scientific Knowledge Graph Construction\", \"authors\": \"Luan, Yi and He, Luheng and Ostendorf, Mari and Hajishirzi, Hannaneh\", \"year\": \"2018\", \"venue\": \"Proceedings of the 2018 Conference on Empirical Methods in Natural Language Proc...\"}, {\"key\": \"manakul2023selfcheckgpt\", \"type\": \"inproceedings\", \"title\": \"SelfCheckGPT: Zero-Resource Black-Box Hallucination Detection for Generative Large Language Models\", \"authors\": \"Manakul, Potsawee and Liusie, Adian and Gales, Mark\", \"year\": \"2023\", \"venue\": \"Proceedings of the 2023 Conference on Empirical Methods in Natural Language Proc...\"}, {\"key\": \"nedellec2026consistency\", \"type\": \"article\", \"title\": \"Consistency–accuracy correlation in hard-prompted LLMs for entity and relation extraction: empirical findings from plant...\", \"authors\": \"Yao, Xinzhi and Nédellec, Claire and Xia, Jingbo and Bossy, Robert\", \"year\": \"2026\", \"venue\": \"Genomics \\\\& Informatics\"}, {\"key\": \"oh2025latentsc\", \"type\": \"article\", \"title\": \"Latent Self-Consistency for Reliable Majority-Set Selection in Short- and Long-Answer Reasoning\", \"authors\": \"Oh, Jungsuk and Lee, Jay-Yoon\", \"year\": \"2025\", \"venue\": \"arXiv preprint arXiv:2508.18395\"}, {\"key\": \"sainz2024gollie\", \"type\": \"inproceedings\", \"title\": \"GoLLIE: Annotation Guidelines improve Zero-Shot Information-Extraction\", \"authors\": \"Sainz, Oscar and García-Ferrero, Iker and Agerri, Rodrigo and Lacalle, Oier Lope...\", \"year\": \"2024\", \"venue\": \"ICLR 2024\"}, {\"key\": \"shelmanov2021active\", \"type\": \"inproceedings\", \"title\": \"Active Learning for Sequence Tagging with Deep Pre-trained Models and Bayesian Uncertainty Estimates\", \"authors\": \"Shelmanov, Artem and Puzyrev, Dmitri and Kupriyanova, Lyubov and Belyakov, Denis...\", \"year\": \"2021\", \"venue\": \"Proceedings of the 16th Conference of the European Chapter of the Association fo...\"}, {\"key\": \"snell2024scaling\", \"type\": \"inproceedings\", \"title\": \"Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters\", \"authors\": \"Snell, Charlie and Lee, Jaehoon and Xu, Kelvin and Kumar, Aviral\", \"year\": \"2024\", \"venue\": \"ICLR 2025\"}, {\"key\": \"taubenfeld2025cisc\", \"type\": \"inproceedings\", \"title\": \"Confidence Improves Self-Consistency in LLMs\", \"authors\": \"Taubenfeld, Amir and Sheffer, Tom and Ofek, Eran and Feder, Amir and Goldstein, ...\", \"year\": \"2025\", \"venue\": \"Findings of the Association for Computational Linguistics: ACL 2025\"}, {\"key\": \"thirukovalluru2024atomic\", \"type\": \"inproceedings\", \"title\": \"Atomic Self-Consistency for Better Long Form Generations\", \"authors\": \"Thirukovalluru, Raghuveer and Huang, Yukun and Dhingra, Bhuwan\", \"year\": \"2024\", \"venue\": \"Proceedings of the 2024 Conference on Empirical Methods in Natural Language Proc...\"}, {\"key\": \"tjongkimsang2003conll\", \"type\": \"inproceedings\", \"title\": \"Introduction to the CoNLL-2003 Shared Task: Language-Independent Named Entity Recognition\", \"authors\": \"Sang, Erik F. Tjong Kim and Meulder, Fien De\", \"year\": \"2003\", \"venue\": \"CoNLL 2003\"}, {\"key\": \"vashurin2025cocoa\", \"type\": \"inproceedings\", \"title\": \"Uncertainty Quantification for LLMs through Minimum Bayes Risk: Bridging Confidence and Consistency\", \"authors\": \"Vashurin, Roman and Goloburda, Maiya and Ilina, Albina and Rubashevskii, Aleksan...\", \"year\": \"2025\", \"venue\": \"NeurIPS 2025\"}, {\"key\": \"wadhwa2023revisiting\", \"type\": \"inproceedings\", \"title\": \"Revisiting Relation Extraction in the era of Large Language Models\", \"authors\": \"Wadhwa, Somin and Amir, Silvio and Wallace, Byron\", \"year\": \"2023\", \"venue\": \"Proceedings of the 61st Annual Meeting of the Association for Computational Ling...\"}, {\"key\": \"wang2023instructuie\", \"type\": \"article\", \"title\": \"InstructUIE: Multi-task Instruction Tuning for Unified Information Extraction\", \"authors\": \"Wang, Xiao and Zhou, Weikang and Zu, Can and Xia, Han and Chen, Tianze and Zhang...\", \"year\": \"2023\", \"venue\": \"arXiv preprint arXiv:2304.08085\"}, {\"key\": \"wang2023selfconsistency\", \"type\": \"inproceedings\", \"title\": \"Self-Consistency Improves Chain of Thought Reasoning in Language Models\", \"authors\": \"Wang, Xuezhi and Wei, Jason and Schuurmans, Dale and Le, Quoc and Chi, Ed and Na...\", \"year\": \"2023\", \"venue\": \"ICLR 2023\"}, {\"key\": \"wang2025make\", \"type\": \"inproceedings\", \"title\": \"Make Every Penny Count: Difficulty-Adaptive Self-Consistency for Cost-Efficient Reasoning\", \"authors\": \"Wang, Xinglin and Feng, Shaoxiong and Li, Yiwei and Yuan, Peiwen and Zhang, Yueq...\", \"year\": \"2025\", \"venue\": \"Findings of the Association for Computational Linguistics: NAACL 2025\"}, {\"key\": \"wang2024mathshepherd\", \"type\": \"inproceedings\", \"title\": \"Math-Shepherd: Verify and Reinforce LLMs Step-by-step without Human Annotations\", \"authors\": \"Wang, Peiyi and Li, Lei and Shao, Zhihong and Xu, Runxin and Dai, Damai and Li, ...\", \"year\": \"2024\", \"venue\": \"ACL 2024\"}, {\"key\": \"wang2025rankedvoting\", \"type\": \"inproceedings\", \"title\": \"Ranked Voting based Self-Consistency of Large Language Models\", \"authors\": \"Wang, Weiqin and Wang, Yile and Huang, Hui\", \"year\": \"2025\", \"venue\": \"ACL Findings 2025\"}, {\"key\": \"wen2025know\", \"type\": \"article\", \"title\": \"Know Your Limits: A Survey of Abstention in Large Language Models\", \"authors\": \"Wen, Bingbing and Yao, Jihan and Feng, Shangbin and Xu, Chenjun and Tsvetkov, Yu...\", \"year\": \"2025\", \"venue\": \"Transactions of the Association for Computational Linguistics\"}, {\"key\": \"willard2023guided\", \"type\": \"article\", \"title\": \"Efficient Guided Generation for Large Language Models\", \"authors\": \"Willard, Brandon T. and Louf, Rémi\", \"year\": \"2023\", \"venue\": \"arXiv preprint arXiv:2307.09702\"}, {\"key\": \"xia2025survey\", \"type\": \"inproceedings\", \"title\": \"A Survey of Uncertainty Estimation Methods on Large Language Models\", \"authors\": \"Xia, Zhiqiu and Xu, Jinxuan and Zhang, Yuqian and Liu, Hang\", \"year\": \"2025\", \"venue\": \"ACL Findings 2025\"}, {\"key\": \"xiao2019uncertainty\", \"type\": \"article\", \"title\": \"Quantifying Uncertainties in Natural Language Processing Tasks\", \"authors\": \"Xiao, Yijun and Wang, William Yang\", \"year\": \"2019\", \"venue\": \"Proceedings of the AAAI Conference on Artificial Intelligence\"}, {\"key\": \"zhang2023ener\", \"type\": \"inproceedings\", \"title\": \"E-NER: Evidential Deep Learning for Trustworthy Named Entity Recognition\", \"authors\": \"Zhang, Zhen and Hu, Mengting and Zhao, Shiwan and Huang, Minlie and Wang, Haotia...\", \"year\": \"2023\", \"venue\": \"Findings of the Association for Computational Linguistics: ACL 2023\"}, {\"key\": \"zhou2024uniner\", \"type\": \"inproceedings\", \"title\": \"UniversalNER: Targeted Distillation from Large Language Models for Open Named Entity Recognition\", \"authors\": \"Zhou, Wenxuan and Zhang, Sheng and Gu, Yu and Chen, Muhao and Poon, Hoifung\", \"year\": \"2024\", \"venue\": \"Proceedings of the International Conference on Learning Representations (ICLR)\"}], \"tex_citations\": [{\"key\": \"wang2023selfconsistency\", \"file\": \"sections/introduction.tex\", \"line\": 4, \"command\": \"citealp\"}, {\"key\": \"snell2024scaling\", \"file\": \"sections/introduction.tex\", \"line\": 5, \"command\": \"cite\"}, {\"key\": \"brown2024monkeys\", \"file\": \"sections/introduction.tex\", \"line\": 5, \"command\": \"cite\"}, {\"key\": \"wang2023selfconsistency\", \"file\": \"sections/introduction.tex\", \"line\": 15, \"command\": \"cite\"}, {\"key\": \"chen2024usc\", \"file\": \"sections/introduction.tex\", \"line\": 15, \"command\": \"cite\"}, {\"key\": \"taubenfeld2025cisc\", \"file\": \"sections/introduction.tex\", \"line\": 15, \"command\": \"cite\"}, {\"key\": \"kang2025selfcertainty\", \"file\": \"sections/introduction.tex\", \"line\": 15, \"command\": \"cite\"}, {\"key\": \"nedellec2026consistency\", \"file\": \"sections/introduction.tex\", \"line\": 16, \"command\": \"citet\"}, {\"key\": \"luan2018scierc\", \"file\": \"sections/introduction.tex\", \"line\": 31, \"command\": \"cite\"}, {\"key\": \"tjongkimsang2003conll\", \"file\": \"sections/introduction.tex\", \"line\": 31, \"command\": \"cite\"}, {\"key\": \"derczynski2017wnut\", \"file\": \"sections/introduction.tex\", \"line\": 31, \"command\": \"cite\"}, {\"key\": \"wang2023selfconsistency\", \"file\": \"sections/related_work.tex\", \"line\": 4, \"command\": \"cite\"}, {\"key\": \"chen2024usc\", \"file\": \"sections/related_work.tex\", \"line\": 5, \"command\": \"cite\"}, {\"key\": \"thirukovalluru2024atomic\", \"file\": \"sections/related_work.tex\", \"line\": 5, \"command\": \"cite\"}, {\"key\": \"manakul2023selfcheckgpt\", \"file\": \"sections/related_work.tex\", \"line\": 5, \"command\": \"cite\"}, {\"key\": \"snell2024scaling\", \"file\": \"sections/related_work.tex\", \"line\": 6, \"command\": \"citet\"}, {\"key\": \"brown2024monkeys\", \"file\": \"sections/related_work.tex\", \"line\": 6, \"command\": \"citet\"}, {\"key\": \"taubenfeld2025cisc\", \"file\": \"sections/related_work.tex\", \"line\": 7, \"command\": \"cite\"}, {\"key\": \"kang2025selfcertainty\", \"file\": \"sections/related_work.tex\", \"line\": 7, \"command\": \"cite\"}, {\"key\": \"kim2026reasc\", \"file\": \"sections/related_work.tex\", \"line\": 7, \"command\": \"cite\"}, {\"key\": \"wang2025rankedvoting\", \"file\": \"sections/related_work.tex\", \"line\": 7, \"command\": \"cite\"}, {\"key\": \"oh2025latentsc\", \"file\": \"sections/related_work.tex\", \"line\": 7, \"command\": \"cite\"}, {\"key\": \"feng2025optimal\", \"file\": \"sections/related_work.tex\", \"line\": 8, \"command\": \"citet\"}, {\"key\": \"wang2025make\", \"file\": \"sections/related_work.tex\", \"line\": 8, \"command\": \"citet\"}, {\"key\": \"li2025llms\", \"file\": \"sections/related_work.tex\", \"line\": 8, \"command\": \"citet\"}, {\"key\": \"nedellec2026consistency\", \"file\": \"sections/related_work.tex\", \"line\": 13, \"command\": \"citet\"}, {\"key\": \"vashurin2025cocoa\", \"file\": \"sections/related_work.tex\", \"line\": 16, \"command\": \"cite\"}, {\"key\": \"zhou2024uniner\", \"file\": \"sections/related_work.tex\", \"line\": 17, \"command\": \"cite\"}, {\"key\": \"sainz2024gollie\", \"file\": \"sections/related_work.tex\", \"line\": 17, \"command\": \"cite\"}, {\"key\": \"josifoski2022genie\", \"file\": \"sections/related_work.tex\", \"line\": 17, \"command\": \"cite\"}, {\"key\": \"li2023codeie\", \"file\": \"sections/related_work.tex\", \"line\": 17, \"command\": \"cite\"}, {\"key\": \"wadhwa2023revisiting\", \"file\": \"sections/related_work.tex\", \"line\": 17, \"command\": \"cite\"}, {\"key\": \"wang2023instructuie\", \"file\": \"sections/related_work.tex\", \"line\": 17, \"command\": \"cite\"}, {\"key\": \"willard2023guided\", \"file\": \"sections/related_work.tex\", \"line\": 17, \"command\": \"cite\"}, {\"key\": \"geng2024confidence\", \"file\": \"sections/related_work.tex\", \"line\": 20, \"command\": \"cite\"}, {\"key\": \"wen2025know\", \"file\": \"sections/related_work.tex\", \"line\": 20, \"command\": \"cite\"}, {\"key\": \"xia2025survey\", \"file\": \"sections/related_work.tex\", \"line\": 20, \"command\": \"cite\"}, {\"key\": \"hobelsberger2025systematic\", \"file\": \"sections/related_work.tex\", \"line\": 20, \"command\": \"cite\"}, {\"key\": \"kuhn2023semantic\", \"file\": \"sections/related_work.tex\", \"line\": 21, \"command\": \"cite\"}, {\"key\": \"kossen2024semantic\", \"file\": \"sections/related_work.tex\", \"line\": 21, \"command\": \"citet\"}, {\"key\": \"kadavath2022language\", \"file\": \"sections/related_work.tex\", \"line\": 21, \"command\": \"cite\"}, {\"key\": \"guo2017calibration\", \"file\": \"sections/related_work.tex\", \"line\": 22, \"command\": \"cite\"}, {\"key\": \"desai2020calibration\", \"file\": \"sections/related_work.tex\", \"line\": 22, \"command\": \"cite\"}, {\"key\": \"lakshminarayanan2017ensembles\", \"file\": \"sections/related_work.tex\", \"line\": 23, \"command\": \"cite\"}, {\"key\": \"gal2016dropout\", \"file\": \"sections/related_work.tex\", \"line\": 23, \"command\": \"cite\"}, {\"key\": \"xiao2019uncertainty\", \"file\": \"sections/related_work.tex\", \"line\": 24, \"command\": \"cite\"}, {\"key\": \"shelmanov2021active\", \"file\": \"sections/related_work.tex\", \"line\": 24, \"command\": \"cite\"}, {\"key\": \"zhang2023ener\", \"file\": \"sections/related_work.tex\", \"line\": 24, \"command\": \"cite\"}, {\"key\": \"fisch2021conformal\", \"file\": \"sections/related_work.tex\", \"line\": 25, \"command\": \"cite\"}, {\"key\": \"angelopoulos2021conformal\", \"file\": \"sections/related_work.tex\", \"line\": 25, \"command\": \"cite\"}, {\"key\": \"cobbe2021verifiers\", \"file\": \"sections/related_work.tex\", \"line\": 25, \"command\": \"cite\"}, {\"key\": \"lightman2024verify\", \"file\": \"sections/related_work.tex\", \"line\": 25, \"command\": \"cite\"}, {\"key\": \"wang2024mathshepherd\", \"file\": \"sections/related_work.tex\", \"line\": 25, \"command\": \"cite\"}, {\"key\": \"geifman2017selective\", \"file\": \"sections/related_work.tex\", \"line\": 26, \"command\": \"cite\"}, {\"key\": \"culotta2004confidence\", \"file\": \"sections/related_work.tex\", \"line\": 26, \"command\": \"cite\"}, {\"key\": \"willard2023guided\", \"file\": \"sections/method.tex\", \"line\": 5, \"command\": \"cite\"}, {\"key\": \"fleiss1971agreement\", \"file\": \"sections/method.tex\", \"line\": 32, \"command\": \"citet\"}, {\"key\": \"jaccard1901distribution\", \"file\": \"sections/method.tex\", \"line\": 41, \"command\": \"cite\"}, {\"key\": \"luan2018scierc\", \"file\": \"sections/experiments.tex\", \"line\": 9, \"command\": \"cite\"}, {\"key\": \"tjongkimsang2003conll\", \"file\": \"sections/experiments.tex\", \"line\": 10, \"command\": \"cite\"}, {\"key\": \"derczynski2017wnut\", \"file\": \"sections/experiments.tex\", \"line\": 11, \"command\": \"cite\"}, {\"key\": \"willard2023guided\", \"file\": \"sections/experiments.tex\", \"line\": 17, \"command\": \"cite\"}, {\"key\": \"kuhn2023semantic\", \"file\": \"sections/experiments.tex\", \"line\": 64, \"command\": \"cite\"}, {\"key\": \"brown2024monkeys\", \"file\": \"sections/experiments.tex\", \"line\": 136, \"command\": \"cite\"}, {\"key\": \"snell2024scaling\", \"file\": \"sections/experiments.tex\", \"line\": 136, \"command\": \"cite\"}, {\"key\": \"cobbe2021verifiers\", \"file\": \"sections/experiments.tex\", \"line\": 136, \"command\": \"cite\"}, {\"key\": \"cobbe2021verifiers\", \"file\": \"sections/discussion.tex\", \"line\": 31, \"command\": \"cite\"}, {\"key\": \"brown2024monkeys\", \"file\": \"sections/appendix.tex\", \"line\": 184, \"command\": \"cite\"}, {\"key\": \"snell2024scaling\", \"file\": \"sections/appendix.tex\", \"line\": 184, \"command\": \"cite\"}], \"online_verification\": [{\"key\": \"angelopoulos2021conformal\", \"title\": \"Uncertainty Sets for Image Classifiers using Conformal Prediction\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Uncertainty Sets for Image Classifiers using Conformal Prediction\", \"matched_year\": \"2020\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"brown2024monkeys\", \"title\": \"Large Language Monkeys: Scaling Inference Compute with Repeated Sampling\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Large Language Monkeys: Scaling Inference Compute with Repeated Sampling\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"chen2024usc\", \"title\": \"Universal Self-Consistency for Large Language Model Generation\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Universal Self-Consistency for Large Language Model Generation\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"cobbe2021verifiers\", \"title\": \"Training Verifiers to Solve Math Word Problems\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Training Verifiers to Solve Math Word Problems\", \"matched_year\": \"2021\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"culotta2004confidence\", \"title\": \"Confidence Estimation for Information Extraction\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Confidence estimation for information extraction\", \"matched_year\": \"2004\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"derczynski2017wnut\", \"title\": \"Results of the WNUT2017 Shared Task on Novel and Emerging Entity Recognition\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Results of the WNUT2017 Shared Task on Novel and Emerging Entity Recognition\", \"matched_year\": \"2017\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"desai2020calibration\", \"title\": \"Calibration of Pre-trained Transformers\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Calibration of Pre-trained Transformers\", \"matched_year\": \"2020\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"fisch2021conformal\", \"title\": \"Few-Shot Conformal Prediction with Auxiliary Tasks\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Few-shot Conformal Prediction with Auxiliary Tasks\", \"matched_year\": \"2021\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"fleiss1971agreement\", \"title\": \"Measuring nominal scale agreement among many raters.\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Measuring nominal scale agreement among many raters.\", \"matched_year\": \"1971\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"gal2016dropout\", \"title\": \"Dropout as a Bayesian Approximation: Representing Model Uncertainty in Deep Learning\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Dropout as a Bayesian Approximation: Representing Model Uncertainty in Deep Learning\", \"matched_year\": \"2015\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"geifman2017selective\", \"title\": \"Selective Classification for Deep Neural Networks\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Selective Classification for Deep Neural Networks\", \"matched_year\": \"2017\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"feng2025optimal\", \"title\": \"Optimal Self-Consistency for Efficient Reasoning with Large Language Models\", \"status\": \"mismatch\", \"confidence\": 1.0, \"matched_title\": \"Optimal Self-Consistency for Efficient Reasoning with Large Language Models\", \"matched_year\": \"2025\", \"mismatch_fields\": [\"first_author: bib=feng vs api=austin\"], \"note\": \"\"}, {\"key\": \"geng2024confidence\", \"title\": \"A Survey of Confidence Estimation and Calibration in Large Language Models\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"A Survey of Confidence Estimation and Calibration in Large Language Models\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"guo2017calibration\", \"title\": \"On Calibration of Modern Neural Networks\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"On Calibration of Modern Neural Networks\", \"matched_year\": \"2017\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"hobelsberger2025systematic\", \"title\": \"Systematic Evaluation of Uncertainty Estimation Methods in Large Language Models\", \"status\": \"not_found\", \"confidence\": 0.236, \"matched_title\": \"A new criterion for assessing discriminant validity in variance-based structural equation modeling\", \"matched_year\": \"\", \"mismatch_fields\": [], \"note\": \"best match similarity 0.24 below threshold 0.82\"}, {\"key\": \"jaccard1901distribution\", \"title\": \"Étude comparative de la distribution florale dans une portion des Alpes et du Jura\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Étude comparative de la distribution florale dans une portion des Alpes et du Jura\", \"matched_year\": \"1901\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"josifoski2022genie\", \"title\": \"GenIE: Generative Information Extraction\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"GenIE: Generative Information Extraction\", \"matched_year\": \"2022\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"kadavath2022language\", \"title\": \"Language Models (Mostly) Know What They Know\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Language Models (Mostly) Know What They Know\", \"matched_year\": \"2022\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"kang2025selfcertainty\", \"title\": \"Scalable Best-of-N Selection for Large Language Models via Self-Certainty\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Scalable Best-of-N Selection for Large Language Models via Self-Certainty\", \"matched_year\": \"2025\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"kim2026reasc\", \"title\": \"Reliability-Aware Adaptive Self-Consistency for Efficient Sampling in LLM Reasoning\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Reliability-Aware Adaptive Self-Consistency for Efficient Sampling in LLM Reasoning\", \"matched_year\": \"2026\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"kossen2024semantic\", \"title\": \"Semantic Entropy Probes: Robust and Cheap Hallucination Detection in LLMs\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Semantic Entropy Probes: Robust and Cheap Hallucination Detection in LLMs\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"li2025llms\", \"title\": \"LLMs Can Generate a Better Answer by Aggregating Their Own Responses\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"LLMs Can Generate a Better Answer by Aggregating Their Own Responses\", \"matched_year\": \"2025\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"kuhn2023semantic\", \"title\": \"Semantic Uncertainty: Linguistic Invariances for Uncertainty Estimation in Natural Language Generation\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Semantic Uncertainty: Linguistic Invariances for Uncertainty Estimation in Natural Language Generation\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"lakshminarayanan2017ensembles\", \"title\": \"Simple and Scalable Predictive Uncertainty Estimation using Deep Ensembles\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Simple and Scalable Predictive Uncertainty Estimation using Deep Ensembles\", \"matched_year\": \"2016\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"li2023codeie\", \"title\": \"CodeIE: Large Code Generation Models are Better Few-Shot Information Extractors\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"CodeIE: Large Code Generation Models are Better Few-Shot Information Extractors\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"lightman2024verify\", \"title\": \"Let's Verify Step by Step\", \"status\": \"not_found\", \"confidence\": 0.246, \"matched_title\": \"Development and dosimetric verification of static SHArc: Step‐and‐shoot carbon ion arc therapy for LET &lt;sub>d&lt;/sub> escalation in pancreatic tumors\", \"matched_year\": \"\", \"mismatch_fields\": [], \"note\": \"best match similarity 0.25 below threshold 0.82\"}, {\"key\": \"luan2018scierc\", \"title\": \"Multi-Task Identification of Entities, Relations, and Coreference for Scientific Knowledge Graph Construction\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Multi-Task Identification of Entities, Relations, and Coreference for Scientific Knowledge Graph Construction\", \"matched_year\": \"2018\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"manakul2023selfcheckgpt\", \"title\": \"SelfCheckGPT: Zero-Resource Black-Box Hallucination Detection for Generative Large Language Models\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"SelfCheckGPT: Zero-Resource Black-Box Hallucination Detection for Generative Large Language Models\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"nedellec2026consistency\", \"title\": \"Consistency–accuracy correlation in hard-prompted LLMs for entity and relation extraction: empirical findings from plant-health data\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Consistency–accuracy correlation in hard-prompted LLMs for entity and relation extraction: empirical findings from plant-health data\", \"matched_year\": \"2026\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"oh2025latentsc\", \"title\": \"Latent Self-Consistency for Reliable Majority-Set Selection in Short- and Long-Answer Reasoning\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Latent Self-Consistency for Reliable Majority-Set Selection in Short- and Long-Answer Reasoning\", \"matched_year\": \"2026\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"sainz2024gollie\", \"title\": \"GoLLIE: Annotation Guidelines improve Zero-Shot Information-Extraction\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"GoLLIE: Annotation Guidelines improve Zero-Shot Information-Extraction\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"shelmanov2021active\", \"title\": \"Active Learning for Sequence Tagging with Deep Pre-trained Models and Bayesian Uncertainty Estimates\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Active Learning for Sequence Tagging with Deep Pre-trained Models and Bayesian Uncertainty Estimates\", \"matched_year\": \"2021\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"snell2024scaling\", \"title\": \"Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters\", \"status\": \"mismatch\", \"confidence\": 1.0, \"matched_title\": \"Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters\", \"matched_year\": \"2024\", \"mismatch_fields\": [\"first_author: bib=snell vs api=charlie\"], \"note\": \"\"}, {\"key\": \"taubenfeld2025cisc\", \"title\": \"Confidence Improves Self-Consistency in LLMs\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Confidence Improves Self-Consistency in LLMs\", \"matched_year\": \"2025\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"thirukovalluru2024atomic\", \"title\": \"Atomic Self-Consistency for Better Long Form Generations\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Atomic Self-Consistency for Better Long Form Generations\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"tjongkimsang2003conll\", \"title\": \"Introduction to the CoNLL-2003 Shared Task: Language-Independent Named Entity Recognition\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Introduction to the CoNLL-2003 Shared Task: Language-Independent Named Entity Recognition\", \"matched_year\": \"2003\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"vashurin2025cocoa\", \"title\": \"Uncertainty Quantification for LLMs through Minimum Bayes Risk: Bridging Confidence and Consistency\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Uncertainty Quantification for LLMs through Minimum Bayes Risk: Bridging Confidence and Consistency\", \"matched_year\": \"2025\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"wadhwa2023revisiting\", \"title\": \"Revisiting Relation Extraction in the era of Large Language Models\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Revisiting Relation Extraction in the era of Large Language Models\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"wang2023instructuie\", \"title\": \"InstructUIE: Multi-task Instruction Tuning for Unified Information Extraction\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"InstructUIE: Multi-task Instruction Tuning for Unified Information Extraction\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"wang2023selfconsistency\", \"title\": \"Self-Consistency Improves Chain of Thought Reasoning in Language Models\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Self-Consistency Improves Chain of Thought Reasoning in Language Models\", \"matched_year\": \"2022\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"wang2025make\", \"title\": \"Make Every Penny Count: Difficulty-Adaptive Self-Consistency for Cost-Efficient Reasoning\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Make Every Penny Count: Difficulty-Adaptive Self-Consistency for Cost-Efficient Reasoning\", \"matched_year\": \"2025\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"wang2024mathshepherd\", \"title\": \"Math-Shepherd: Verify and Reinforce LLMs Step-by-step without Human Annotations\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Math-Shepherd: Verify and Reinforce LLMs Step-by-step without Human Annotations\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"wang2025rankedvoting\", \"title\": \"Ranked Voting based Self-Consistency of Large Language Models\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Ranked Voting based Self-Consistency of Large Language Models\", \"matched_year\": \"2025\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"wen2025know\", \"title\": \"Know Your Limits: A Survey of Abstention in Large Language Models\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Know Your Limits: A Survey of Abstention in Large Language Models\", \"matched_year\": \"2025\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"willard2023guided\", \"title\": \"Efficient Guided Generation for Large Language Models\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Efficient Guided Generation for Large Language Models\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"xia2025survey\", \"title\": \"A Survey of Uncertainty Estimation Methods on Large Language Models\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"A Survey of Uncertainty Estimation Methods on Large Language Models\", \"matched_year\": \"2025\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"xiao2019uncertainty\", \"title\": \"Quantifying Uncertainties in Natural Language Processing Tasks\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Quantifying Uncertainties in Natural Language Processing Tasks\", \"matched_year\": \"2019\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"zhang2023ener\", \"title\": \"E-NER: Evidential Deep Learning for Trustworthy Named Entity Recognition\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"E-NER: Evidential Deep Learning for Trustworthy Named Entity Recognition\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"zhou2024uniner\", \"title\": \"UniversalNER: Targeted Distillation from Large Language Models for Open Named Entity Recognition\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"UniversalNER: Targeted Distillation from Large Language Models for Open Named Entity Recognition\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}]}, \"error\": null, \"metadata\": {}}"
    }
  },
  "sourceToolAssistantUUID": "f08f6b57-c544-44b1-85a5-d86917275869",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_1_68ddc296",
  "sessionId": "8e0e70e7-e72a-426a-9f89-26576a55a64e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Runtime record

_source line 67_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[Round 1 审稿请求]: 你是 Reviewer 1，负责**方法严谨性 + 实验设计**。  ## 审稿对象 - 论文路径：`projects/struct_self_consist_ie/docs/paper/main.tex`（分节结构，各节在 `sections/` 下） - 目标 venue：**EMNLP 2026 Main Conference**（通过 ARR May 202…",
  "leafUuid": "03ff3561-7736-4f11-aac4-208cb478ce5f",
  "sessionId": "8e0e70e7-e72a-426a-9f89-26576a55a64e"
}
```

---


### Runtime record

_source line 68_

```json
{
  "type": "ai-title",
  "aiTitle": "Review paper on structural self-consistency for information extraction",
  "sessionId": "8e0e70e7-e72a-426a-9f89-26576a55a64e"
}
```

---


### Large event (continued)

````text
### Tool result

_source line 69 · 2026-05-15T04:01:10.527Z_

&lt;details>&lt;summary>↩ Tool result · `toolu_01S3KCKWZHWuEz24QPT69Czj`&lt;/summary>

```text
Error: result (1,976,553 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie--claude-sessions-review-reviewer-1-68ddc296/8e0e70e7-e72a-426a-9f89-26576a55a64e/tool-results/mcp-agent-ml-research-pdf_to_images-1778817670520.txt.
Format: JSON with schema: {result: string}
- For targeted queries (find a value, filter by field): use jq on the file directly.
- For analysis or summarization that requires reading the full content: first probe the structure (e.g., jq 'type, length, keys?' /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie--claude-sessions-review-reviewer-1-68ddc296/8e0e70e7-e72a-426a-9f89-26576a55a64e/tool-results/mcp-agent-ml-research-pdf_to_images-1778817670520.txt), then extract slices with jq or python — Read's line-based offset/limit will not chunk this file.
- If the Agent tool is available, do this inside a subagent so the full output stays out of your main context. Give it the instruction above verbatim, and be explicit about what it must return — e.g. "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie--claude-sessions-review-reviewer-1-68ddc296/8e0e70e7-e72a-426a-9f89-26576a55a64e/tool-results/mcp-agent-ml-research-pdf_to_images-1778817670520.txt is JSON with schema: {result: string}; probe the structure with jq (type/length/keys), then extract and read the content in full with jq or python, then summarize and quote any key findings verbatim." A vague "summarize this" may lose detail.

```

&lt;/details>

&lt;details>&lt;summary>Recorded metadata&lt;/summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d8832dc2-09cb-47e6-a638-bf0af8806ebd",
  "isSidechain": false,
  "promptId": "06c85d14-4a07-4193-8916-587ad0c60656",
  "type": "user",
  "uuid": "c9b7d789-01cf-44f6-9b7c-46f2acf33b93",
  "toolUseResult": "Error: result (1,976,553 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie--claude-sessions-review-reviewer-1-68ddc296/8e0e70e7-e72a-426a-9f89-26576a55a64e/tool-results/mcp-agent-ml-research-pdf_to_images-1778817670520.txt.\nFormat: JSON with schema: {result: string}\n- For targeted queries (find a value, filter by field): use jq on the file directly.\n- For analysis or summarization that requires reading the full content: first probe the structure (e.g., jq 'type, length, keys?' /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie--claude-sessions-review-reviewer-1-68ddc296/8e0e70e7-e72a-426a-9f89-26576a55a64e/tool-results/mcp-agent-ml-research-pdf_to_images-1778817670520.txt), then extract slices with jq or python — Read's line-based offset/limit will not chunk this file.\n- If the Agent tool is available, do this inside a subagent so the full output stays out of your main context. Give it the instruction above verbatim, and be explicit about what it must return — e.g. \"/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie--claude-sessions-review-reviewer-1-68ddc296/8e0e70e7-e72a-426a-9f89-26576a55a64e/tool-results/mcp-agent-ml-research-pdf_to_images-1778817670520.txt is JSON with schema: {result: string}; probe the structure with jq (type/length/keys), then extract and read the content in full with jq or python, then summarize and quote any key findings verbatim.\" A vague \"summarize this\" may lose detail.\n",
  "mcpMeta": {
    "structuredContent": {

````

---

### Large event (continued)

```text
      "result": "{\"success\": true, \"data\": {\"images\": [{\"page\": 1, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/_pdf_images/main_p1.png\", \"base64\": \"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jjzcihUrZmfO3/pKSzFrvm7duoEDB2qX8p///Kd0ZyRcRhtRbgUW3eLFi/1Pd7UFWHI7kI8++iikRS1btqyY49+4ceOYMWO07evodtttt/3rX//KSbV3F7tOQ8pif/LDDz+Ubp3jt+usLyAcWRS5sWXLliFDhlSvXj0vL69GjRr9+/cfPXr0nXfe2apVq/z8/KZNm6rjro5azZo177rrrjgr9vnnnzdv3ly1OvDAA1VD9Qh79uzpXlzWqVOnzZs3h399+PDhbhbsdWfnnntuPDWPzdSpU4844oiCggJl9eeff37YsGEdOnTQLFesWFGLbu+9937ggQds4HHjxtmi6NOnTylWOyVVr1KlSv7r6T777LOcjFlJ45JLLnHjvP76659++uly5cpVqFDh7bffzsn4i3T77bf787XXXnsdeeSRe+yxh5Xsueee9erVK1u2rD/Y4MGD46leCdV8+/btxx57rCvR0l6+fHlpz01qGW1EuaVFdMYZZ/iL7qKLLvI/3aUWYInuQG644YYTTjghL8n+++/ftm3b8ePHF2fk06ZNO+iggzS2ww477Nlnn9UI9f8LLrjgl19+yVX9d2W7TkNSTTp37tygQYPkFX3wwQcfffTR2hIrV64c+GjmzJmlVeFSseusL6BIZFHkwKJFi+rXr+/2ejpC//TTT/6n7733nrqedkiIM4sqiGov7KZrmWHVqlVWmVGjRkUZT48ePewrv7Is+sorr7gw8OGHH/rlM2bMOPTQQ90s+93o9u3b26KoU6dO7PUtmvocfhckV1l0wIABboTVqlXbsWPHwoUL3Z/Vq1fPyfiLdMstt7gptmjR4oMPPlBXQ4X77bef3w9LFL7X8V//+lfTpk2T112uzJ492087JVrzBQsW+GvzySefzPnsFF+mG1FJOOuss2wp+WtnV1uAMexAHnroIX+WDzjggOJfHbBmzRprsSNHjlRJx44d3Z+PPvpoLmq9a1HYmz59ul+yqzUkueCCC/wqXX755f6n33777eDBgw8//HD3afGzaKb7vTjtFusLSIcsiuKaP39+xYoV3f7umGOOSXmm8fvvv2/YsKEbJs4s2rJlSzfRgoIC5QdX+NFHH9kOeuDAgVHGc++999pXfk1ZdN26dVWrVtVMNW/ePPnTr776St24QDdaS8wWhbq/MVY2KkUd/xickyyqmOROiUijRo1U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rVvnlx900EF5hVwWla1btyrf5v1XpUqVFFZLcDbS27JlS40aNVw1mjZtWnITGjx4sM3vK6+8skuNDQBQ6siiAFDKtm3b5oLBPvvss379+tKuDhKPPvqoCzz9+vULGWz48OFusFq1aiVf0PvVV19Vq1bNz6IyYsQIS1OtW7cukdpHc/bZZ8eQRSdPnuymomD/2Wef7VJjAwCUOrIoAJSySZMmWT554IEHSrs6SDRs2NCtjooVK/78888ph/nXv/6Vn5/vBrv77rtTDjNnzpyyZcv6WfSxxx6zde2Xx69ly5YxZFH529/+1rVr19dee20XHBsAoHSRRQGglNkZKqldu/b27dtLu0a/aR988EGeR+En5WAnnHCCDbNkyZJ0Y7v++ut/41kUAIB0yKIAUJq+/vrrww477MQTT7SIMmnSpOTB7rnnnrv+y6WjV199tW3btmeccca11167cuXK5K9Mnz69f//+zZs3v+yyy4YOHepf/fvuu+/e5Vm8ePGaNWsGDBigsWmczz33nA352muv3bUzVz1lKvfnn//85x9++MEf4OWXX04UPqrn/PPPV87p0aPH0qVL3djGjBnTqlWrs8466/bbb//xxx8DFd6wYcOwYcM6deqkOvfr12/atGn2UWASU6dOVaEG8As1Uzb85s2bH3roIVXg9NNPVxocP3781VdfHXGNdOnSpX379rY6GjZsmDzMzJkzbYCaNWuGjG316tWqif1Z/CyabtYyXUR+Fl23bt2tt97aokULLXytox07drhhAmt/7dq1aq7XXXfdaaedpvU4duxYN9iXX37Zq1evU089tWPHjv/85z9tEoGv+88Tnj17drdu3TSeCy+8UCv9iSeeePbZZ8NnMGRsidDGk8hq8wEAxIAsCgCl6eabb77zzjvVrbeIcuaZZyYPpi7+gQce6AY44YQTlOX22muvsmXLupKqVav6D8756aefunfvrnJ19JUf3nzzzfz8/EMOOeSdd95xAyh5ugGcUaNGKVAVFBRYyaBBg9yQy5cvP+WUU6z8mmuuUbhKFMaPc845Z//9958yZcr27duVfFQfi1idO3cuX768XcKqkasaF198sSZRpkwZV9i4cWP/DLBmUIPtueeeb731lgY+77zzNMxVV13lHpeqIZ9//nmrRs+ePd1cqJ5WqJjhRqVUdtRRR2nqCtXLli0bPny4KqPq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Ylts+RbJ09vbO06cOKoQG9L+/fsHDBiArUgVpkuXDhv2uHHj9C0qfvz4SPLY0hC5MdeYKCZdokQJDw+Pdu3aST50MYMOx+bmxvOmuw8REZmDWZSI6D/r+vXra9asQaPc4dWnYbBz585SpUqFy6gcQqg4cOAA6hwQEOBwAIQ0hJwVK1aoPIyXhuQml5I+e/YMM7506VKMUH8cyzty+fLlBQsWjB49evz48evWrUPGexdTcWfW3FlEcOzYMfX3jRs3UOe9e/e68+Sbt3ThwoVLly7hD6zijRs3Yl2rk6jWt1t3oW48REQU2TCLEhGRU8gw69evX7lypYSZjh076j3EEBEREYUZsygRETk1e/ZsuYJx+fLlt2/fzpAhgwmnzoiIiOhDwCxKRERO/fHHH5JFa9asWb58eUNPPERERERhxixKRERO3bhxo0iRIsiinp6e+nMyiYiIiN4SsygREYUiMDBQPX2EiIiIKFwwixIREREREZHZmEWJiIiIiIjIbMyiREREREREZDZmUSIiIiIiIjIbsygRERERERGZjVmUiIiIiIiIzMYsSkRERERERGZjFiUiIiIiIiKzMYsSERERERGR2ZhFiYiIiIiIyGzMokRERERERGQ2ZlEiIiIiIiIyG7MoERERERERmY1ZlIiIiIiIiMzGLEpERERERERmYxYlIiIiIiIiszGLEhERERERkdmYRYmIiIiIiMhszKJERERERERkNmZRIiIiIiIiMhuzKBEREREREZmNWZSIiIiIiIjMxixKREREREREZmMWJSIiIiIiIrMxixIREREREZHZmEWJiIiIiIjIbMyiREREREREZDZmUSIiIiIiIjIbsygRERERERGZjVmUiIiIiIiIzMYsSkRERERERGZjFiUiIiIiIiKzMYsSERERERGR2ZhFiYiIiIiIyGzMokRERERERGQ2ZlEiIiIiIiIyG7MoERERERERmY1ZlIiIiIiIiMzGLEpERERERERmYxYlIiIiIiIiszGLEhERERERkdmYRYmIiIiIiMhszKJERERERERkNmZRIiIiIiIiMhuzKBEREREREZmNWZSIiIiIiIjMxixKREREREREZmMWJSIiIiIiIrMxixIREREREZHZmEWJiIiIiIjIbMyiREREREREZDZmUSIiIiIiIjIbsygRERERERGZjVmUiIiIiIiIzMYsSkRERERERGZjFiUiIiIiIiKzMYsSERERERGR2ZhFiYiIiIiIyGzMokRERERERGQ2ZlEiIiIiIiIyG7MoERERERERmY1ZlIiIiIiIiMzGLEpERERERERmYxYlIiIiIiIiszGLEhERERERkdmYRYmIiIiIiMhszKJERERERERkNmZRIiIiIiIiMhuzKBEREREREZmNWZSIiIiIiIjMxixKREREREREZmMWJSIiIiIiIrMxixIREREREZHZmEWJiIiIiIjIbMyiREREREREZDZmUSIiIiIiIjIbsygRERERERGZjVmUiIiIiIiIzMYsSkRERERERGZjFiUiIiIiIiKzMYsSERERERGR2ZhFiYiIiIiIyGzMokRERERERGQ2ZlEiIiIiIiIyG7MoERERERERmY1ZlIiIiIiIiMzGLEpERERERERmYxYlIiIiIiIiszGLEhERERERkdmYRYmIiIiIiMhszKJERERERERkNmZRIiIiIiIiMhuzKBEREREREZmNWZSIiIiIiIjMxixKREREREREZmMWJSIiIiIiIrMxixIREREREZHZmEWJiIiIiIjIbMyiREREREREZDZmUSIiIiIiIjIbsygRERERERGZjVmUiIiIiIiIzMYsSkRERERERGZjFiUiIiIiIiKzMYsSERERERGR2ZhFiYiIiIiIyGzMokRERERERGQ2ZlEiIiIiIiIyG7MoERERERERmY1ZlIiIiIiIiMzGLEpERERERERmYxYlIiIiIiIiszGLEhERERERkdmYRYmIiIiIiMhszKJERERERERkNmZRIiIiIiIiMhuzKBEREREREZmNWZSIiIiIiIjMxixKREREREREZmMWJSIiIiIiIrMxixIREREREZHZmEWJiIiIiIjIbMyiREREREREZDZmUSIiIiIiIjIbsygRERERERGZjVmUiIiIiIiIzMYsSkRERERERGZjFiUiIiIiIiKzMYsSERERERGR2ZhFiYiIiIiIyGzMokRERERERGQ2ZlEiIiIiIiIyG7MoERERERERmY1ZlIiIiIiIiMzGLEpERERERERmYxYlIiIiIiIiszGLEhERERERkdmYRYk+IHfv3r1582ZE14KIiIiIiFmU6EPSrFmzqlWrOnv3wYMHJUqUyPRKvXr1zKwbEREREX1QmEWJPhSImnHixIkaNerFixedDRMSEpIiRQqLTcmS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f/31lClTyplpgXDz5s1MmTJly5Yt9rjJdsCvv/768ccfFypUKFeuXC4fOXnyJI9cuXJl/vz5lN5jjz323nvvRWkiQ44pU6bUqVPn4YcfDu/ZfS6fHT16tMfjmTx5sjew5NSuXTtRokRy0GIE8N13340ZMyZizxoYGBgYGBgYxCoYLmoQrYCwHTx4MHny5A888EAMJuPSpUtyRHVQLvr333+fP38eEkJkZy4KXn31VbhH6JIZhbh69ermzZvJVI4cOdzEhztVq1ZNJkIvX748dOhQOe87ipMZYkCn5RT7CHBRN88uXrwYbi/HQweSnF69ehUsWPDMmTMRysE/WLhwYYcOHSL8uIGBgYGBgYFBLEHouej169d37dr1sw87d+6UM4Ut2L9//6ZNmywHsP7555+//vrrqlWr+H/s2LGQJ8wg9iB//vwxy0XB/Pnz3XBRgVCvoFw0AujcuXPETloPCVKmTOmGi0LDiHbo0CEVsm3btnuRi3p9p/9FjItG7Fk3koO6GzlyZLhS0r59+8GDB4frEQMDAwMDAwOD2IYQc9GbN2+uW7duxYoVK1euhFXyg0t9Bx3888SJEyt80Lko1pgErl69Wn4cPnw4tGkziD2457jo8OHDo4KLShr8HpgePUidOrUbLlqhQoVu3brpITt27DBc1A2CSs7169eLFi3aqVOncKXkr7/+Spcu3YYNG8L1lIGBgYGBgYFBrEKIuejRo0ehkWvXrr1x4wYW9saNG7k8cOCA12dybd26lVsr7kBx0du3b69Zs4aQP/74w+ubIOU3VDYGbXQDOy5evDh58uSuXbuOGjVq//79+q3Dhw9/8cUX/Dh06NCwYcOGDBliX4K4bdu2zz//fODAgcRxw0V37tw5ffp0eScG/ejRo0+dOuX1eYJBPPr06fPll19admYiUdwaPHhw//79lyxZYp9vvHTp0rx586BVc+bM4Yedi/J4v379PvvsM7iWHu6Si54/f378+PH6d3/99ddvvvmGH9AG0jxp0iQl1d9///1DDz3Ea8kmb1bubWgpJK979+68irag527lypWbNm2iIsaNGyevdf6EQAqQiqPELF5z3HDRpUuXksjdu3frgX65aNDyP378OPXYo0cPSLj9mHg7UCOLFi1Cb1A4lEnPnj0pND0CYkam+LF+/foBAwao4iL+ggULevXqNWLECMpHf0TxydOnT0+dOpWk/vLLL5bvBioxN8+SElmjK7BLDvW7cOHCffv2STqrVq1KhOrVqxNn3bp1e/fu/eoOyII8smXLFgk5ceKEek+9evVKliwZtAzdw6GBg2vXrs2dO5e2M3ToUH2GnHASdu7cOQIHDRq0efNmdWv79u1jx45Fkqk7i+BRCBQg4jpt2rSff/5ZH69EcmiDPEhp0KGEMIMGBgYGBgYGsQ0h5qKYfdhhylIRaiqD91gbsnAXS87CRbFjZCpVqAXhEke4h0FsAHZhqlSp4G9hYWEY/cmSJVuzZo3XZ7+2bt0aYzp9+vSwoPLly7/22mvx48fPli2bsi+p1g4dOlSqVGnXrl0HDhyoW7cujztwUeTnrbfe4p3FixfH3K9Ro8b7778PbcuXLx9kpkGDBu+++261atWI8OGHH6qn/vjjjzJlykBXiLNq1ao8efIUKVJE9xADuc2bNy+2L3I1e/bsJ598UueiV69efeONN7CAV69e3axZM7IAc1bPBuWifL1p06aJEiUimqxLh1S8+uqrXFIgbdq0qVKlSqlSpbgka/LIt99+mzNnTkK+/vpr0nPlyhV5ivxC1ZYtW0Z8uCJ5IRySQJESGXO/XLlyCRMm5FsQQudPeH2Hmz366KMwSWjb66+//tRTT+nDBG64aOXKlbNmzWoJtHPRoOW/ePHi7Nmzw0+oCO7yODnKnz8/Wfb73QkTJqRLl45ossESYUiePDmX5AKJOnjwIJJAOWTMmJGYmTNn5pZM3lKDvHbWrFlQ05kzZ/IUIqeovvBJGFfKlCml/EHnzp3dlJjzszNmzJB8tW/fXr1NlxwIGOyLMieE0iCE5tClSxcua9asiQxs3Ljx5s2bNBZCChcurM4rh9VTxUi7PvhCronGI87V5xKBGrgAgv3cc8+RwiNHjrRo0YLWgUDSZMh7ihQpRIZpXPwoXbq016ftP/jgA9KMAFDdtWrVeuSRR9Q4Ag2E3E2cOJHM8pWkSZMiM3KrefPmCBVaBXGivctoVJzC1q1bx48ff+PGjZhOSBSCPIr8Rx1OnjxJQz59+nSUfiVWwY3kYFxhj9G5RGlKUHRffPGFZTxXcP78+YULF6JhfvjhB78buFyCjFhG/QxiP6jxy8GA8MR0Mg1iACHmosIh1ewEPYGQTH057tmzZy1cVCgrxpCKIxOq+ui7QcyiQoUKCRIkEFMYQ/PBBx+sXbu2ugsf4O7UqVPlsmPHjlil2LVyOWzYMCxRRU3RR0F9FxEZexeDeNu2bRJC78U74VrqHBGM4yRJkojmQpa4xPZVb0AIsXHhBtI3YzdnypRp6NChKkLv3r11LtqyZcsRI0bIb7L5xBNPkCOZvPK6nhfNlSuX4qKAx7mE2KipuRIlShCijv0gzfoaXX5go2O7y+Xhw4e5S0qk2Lt3784lfA/WChPD+g/6CR6kEHhEbtESuTV69GiV4KBclCTxhrJly1rCLVw0aPlTJmnTpm3UqJHchS5ahhL8ol+/fkSDY1+6dMnrUx1CeKZMmeL1WTxIUeLEiefMmQNbgylRYtigEEVVlV4f59eTKnyyXr16IkgIGAkjRMwa5xJzfhZAfR24qOD9999XXBT8+OOPXOprdJFVXgvHk+EJQe7cucm+Xji//PILDyIVzmXoEg4NHFmi7fz8889ySQlT7FSEXFJWJKNdu3Zen/4XBosGQCeoJk/tFC1alNYq061oBt6vps1h4xKOncqr1IeWL1+ObR2S3N1DkOEMNSV+n4E+QgYB69atG6Ufat68OV9p3bp1lH4lViGo5PTq1StDhgzEadasWZSmBIXMVwoWLGgJ37x5c8WKFbds2dK4cWMiVKpUKWLvJyPp06fnDSjkSCfWIPqA5n/99ddlDBcDD9vjaR/o3bJmzSpD+fSPMZ1MgxhAiLmokEw1GCkTnkBfNGjnonBOLvUBfplfVUzAIMYxf/582KC6hMPo6wMta25nzZqFThHfKmFhYUSG6elvc7NG9+GHH9Zp0nfffWcx2Rs2bEiI7CteuHChOktDoUmTJgTKGs7+/fvzW18Xqu8XPX78OL+xiUffAZyQkFGjRklkl1xU/KwqLvrXX39x+fLLL6sITZs2JWTTpk1yaeGivB8iNFoDbFytj/3iiy/4rbMsN5+Aci9atEh+b9++3TIHGJSLHjhwgEdq1aplCbdw0aDlv27dOkv1wbWKFSvm8GnvnSNS1BgHIC+ElCtXTi4hPGnSpNEfadOmjZIKBfKoAoVPQjLV3c8++0zPo0OJBX0WMhaUi/bs2dOZi6o4auiE0tN5vkCGIezhEYNDAyfXmAt65J9++kmpa0gFyVADKF6f2k+YMGGDBg30R2bMmEE02qxXY+xCR//44w+ZeYblSuXKgl46iK1bt4Ykd7EZlqXsNHPEKTJulmM5Jk6cGA1cdM2aNVWqVIlTG6rdSE6PHj2igotaZJiGXLNmTUt3cO3atXTp0g0aNEjiowp0hRNefPLJJyHhovaNJDHoStA9oi6R0ZD9fPnyyRCzJfzChQsI8DvvvBPVCTCIhQglF5XdYkBpQ0z/iHFRLGnDRWMhLl68CD2DsyVJkqRo0aIq3MItdZonJASTXX9PBLio3WSHCBEi1qosdPz222/1N0yZMoVAocGwNV6o39UT+f333/ObkBV3Q7Y6e22MAuo1WwNdr4QH5aIffvghIWoJgIWLtmvXLmvWrCtskElO4aKyL1ch6CcENDFyKjRVZ0pBuSitkkdglZZwCxcNWv5Hjx7ld7Vq1dTdJ598UvVG+/fv18tz+fLlEm7nojdu3IgXL16WLFnkMqMP+kdfeOEFHlErcgV0b2qi3u5/6MiRI4RY6JbfEgv6bKi4KNWaLFkysimy0bx5c8tGWa9PkXp8a2LJ7JZIQKeRfhs4Ulq5cmVvAAgX1XU11Wc3EyGcBGKFeH2T5Llz5+YyT5480Fo9mtRUmjRpxowZc0+c0xtJzJo1636dAg0EUbxRzUUN/GLSpEkh56I0Z7XgxQEyGkXth+Sj0jVEkovaW5/LvMQ46JjQ1SF/LWrc4qQwKlCxYkXqTl9Yp0C3W69evahOgEEsRIjnRcUFkTLNIaXihUiPY+ei4kTXvkYXOy+0yTOIMLALBwwY8Nprr8nkEhzGJRedPHkyvy0joCHkohjT3jvrHrFf9TfIAkuZinnssccwr/W7eiKHDRumaK1fWBgF/OcBDUuXLpXwSHLRGjVqpEyZMlAaIsZFiUAJwHKvXLkiBDJcXFQmBuvXr28Jt3DRoOUPXnrppQQJEkghw0z4rSYYMSz08oRPqnALFwXp06eHychvOxeVbZyWPaj0r2qG1s4nb926FT9+/EKFCgUtsaDPhoqLgrZt20reEQ/ebydmMotYvnx5tOXTkUCpUqW8jg2c3w4z2HYuKtOederU0aNJQT3++ONySS9Qq1Ytjw8YH6rJEA0mLIu1ihQpcn97U9+5c2fS/2fvzeN1qtr4/xvHPJPpyXSizERCpiKSJHN4JHMRQoYQXhHJmDmEzCSVisKXHmQsc+ZoIEpFJzmZ8t3f929fv7Ney9773uc+59wOjvX5437de+1pDdda+/qsda3rSp8+XNr5nQLDRW8hbgYXbdOmDR/0WC/r06fPbcVFPXtfiGW5tRCdyuENLuHge1eiRIlYN84kHOLkwpOLWvbWpJudgbsBwWJkQrvQmXfdCLVrLCoqirNf2eCP2hCXCAgzF92xYwccUjk/lPAtW7du1a9xc9GzZ89KNBd1zZYtW/R9pwa3HM2aNStUqJDaVh46F12xYoV7YS3sXFSiODp2B61Zs4bE8ePH879MmTL8192Q6pl8//33+T9mzBhHHg4fPix/wmWj689FO3fuzKHbNatkIx5c9MKFC7SammiMBxf97bffPM1pHFw01vq37G2QDRo0gFb16tWrS5cualugD9xclEEjderUyjDVzUUbNmwYcG2aEoMucfHq5pO0l+LM/jXmf68VVi6KrELJSpYsuWrVKs+IL4cOHQrc6KcqIfDp4OQBpc2h+tCacrGbi0rsWcduscuXLytBUjP6lF3mDmggy94ALH3n6NGjMndeqVKlsJTuNgSdOn/+/JRx1KhR9Fa9ApE6NfIoUP/r16+nR6xevdpth4ke+cEHH1j2Bm/0j5kzZx48eDDEnGzfvl18jJ0+fXrRokWff/652ujLS1euXAmBUc6ldOzdu5dTDJ6e7o7RY8jq1KlTP/vsM91Pss5FGV6WL18+b9489/Pp6VIQsqS7QBPQOxheLFuW6Ow8Qc2AK6A/6P63LFsI6U3kmXSu1/djnz9/Xsw6/v33X3rx7NmzlVEMOaFFZs2aFSeXP9QJLTJ9+nR3CCj/oiWkKT0lhyqiTflwMGJ4clFehPY1Y8YMLnOvtu3fv192fKDRMhR/+OGHuldCGVoLFy68zYb69kVHRytTDqqCU+JuUKRdrkRL3hYDNRGMSEiKf6l1Lkr2OOR1DnMYgaeUunufT1ks2/5l2bJlc+bMcTtkQnJkUpVxDyFxy6EDtD5Fo+kRWvKmTzLycHn1999/LymqftT4QPdBdyKfDJ6kKwef9CCxJ2JwQH6WLl2q9Gd6sXqOuG+QFtGLyTVoEUIRSVR7fCzbn+L8+fN57/Hjx2MtXSgIxkXJv6MFETl6N5JJh1We/BTEzb5lT8tyjW7gc5fDJ0Ymze22vJNmFUnW72L88exTNwNh5qLoEBQAeiA8k87JoWNMcXNRVBBJEXUHdVAO3cJncEsghohPPvmkSsmQIUOIXJQ+kCxZsixZsugffq6PiIjwf2mcuCiCh+KeJ08efWSHIMFbRKUQ278333zTkcnhw4fL7fxH/9ZDWZCoHMPcJC4qBqXqemGbFStW1L+CfEQlZEs8uChfO/ncyik+MHHlopZtTKu3tcDBRWOtf8v2IaS7Jg4Fbi4q67SffvqpHLq5qChbjkU5CGqxYsWE87v5JCpRIMZljn+N+d9rxYuLikWrfouCzE1AEd0RVizbCIWz6PqeVRcn+Hdw2fdLZtRZ9PVXX31VVFI3F6WeyTOJulosBFX84qKgK2WL0b5AgQLly5e3bAURbU/S+To0btyYW/RxIymBhmMYFJ1syJAhqI/nzp0bMWKEeKBxdHM6gngVhoC1bduWwZahTHZ2oSm2bNkyTZo0yZMnR04eeughenQKG8p7nCf47A4aNEg0cnTN1157rUiRIuIbjD9UO7kqWLDgww8/zJNz5MihOrJlK3+0+4ABA6ZMmVKjRg36vmMXBlyOwW3u3LnQUYqZM2dO1WsUFx0/fnzWrFnvv/9+DvlA6Fo+haIUffv2JXHatGl8LMT7gGWHmKpevTrfFAZbOhE5FAfjKodIDpSAs1yjr76if/MuTnEZmiv1I7PkKF7169enCLyR/v7II48gjXx9eCalQMHlkFplcCOld+/esbYsozcDRaNGjah/mjVdunTlypVTxMCnaPFuSh/JWbx4MQM43QqFiuGaZzq46Ndff/3MM8+MGTOGbFCTuXLlUmbziKjstGfI4mueN29e8RjEyCBjKaqdfG5IH2IDIgRjb9GiBaVWIzMP5NSDDz4YsLfWqyvRdMX3W506ddRYERUVhShS//57feXT0KNHD2osEIN7771Xn8n1kVJ37/Msi2WPdQzOjIE0VocOHbigdevW//zzD6egSU2aNOEbB7lihKfVOEt+fLKNOkROunbtyrBPEeh99C/dW6GoEOrDSiUgSIq5QQzQSUQ4yRWZpLy8+tFHH0XaaUe+X+QHoeKCtGnTyqQGAinepIDIITUDtUbS1Ci9atUqiS5G4/JYNS+PgoR2QTZQtKpWrVq7dm2f0oWIYFyUD5DqJij/1BKvg22SVQaT3Llz60HO+B4hPIgZDSdSRA9NeN6SAPxjZAr/otF/1yCfcuFrSCNDKCniiTbRdkqGmYv+9ddfQqxl5VcopWOd181FLVvFJIXCM0BLFdwNXivuFIhDV8Y4mubQoUPDhg1jmONLw4gm89l8sRj+1Poe5IHruUwO27dvL98bmcNj1ONRwjEcrkF1cA1KqjoU30V8e1SK+C5SNEDsMJXLU74W0A/lJpdPO58iBl9GZ74uCKoMiI899phMAfL55BDN5q233uJrOnbsWEZeZbogXnzFyNMHjOMBzU0uo0AgJsqFXhXKBIDhmEOKxshLQdAOKTIpvBqVAq2rZ8+eSp3i88kpB53zf4UY86BfMqDQdnIKFR8mIHSXoVyZTQZD//79qTr5+irIPlK1Hhhr/f/2228o0HxiaXS+LowSDHz6aoknROHo1auXHDJi8O2vW7euukD8zeq3cA1tivDIJIVl74GhmGqngJiKKSqIMDRo0ECt6PrXmP+9lh23hgu6deumUtySgw5ByocffiiHfBUCtoNoaoxq0UMy0LkoiNjQuoEqj5Ialo0M/h0cJV4C4aIroNSizyGfao1ITG0dwzVn0cyaN2+uBnlEhRFA/tOsUFl1MXqG+E6kKipVqqRuGTx4MKQo4aW7bfH8888HNKtFBIwKr1KlioNR0ND0Hb2hGQb1+Qu+sDKiogeL40CZuVOm7D547rnnuBKKoibIaLWAvbMXFVBSZOTRuyE6IqOWHDJq5cuXjwsUh1m6dCmsRnxfA0Sds0WLFpVD4aJwHkWnxUO4vk8MMSBFjQ90AURdLQGJwUW2bNmQIukvAwcOJKVLly6SPSpBpo10LtqmTZtatWqpQ7qt2pcuHtr4OsCCZKATowNoScOGDWWpkHRx9RmrWylGOQZ2JcaMBvpUjn/R4teUwSQHIsp3WdcmhdgoLsr3F36uCICUmhFVfcJkqZBvhMwiUdviN1vJxg8//MChbtfKvdLEjllCGUuFHSnwOSPRwXBoBeiQT3mtmE8D9GP27NkXL15UEdRy5MghgherlDp6n2dZLJuMMeyrQ/lkMzRJ7ZHPgL2UyqjIN0I+cMHyTMZgy/qkHoKHGFPhymJrxowZgRuDpYkfeJ25yfyRMlThsTK/yddw3LhxyBKUlTokBXFVs37iQlk3NhQHjWoWQKZxdRtdqRClYnGvGsMTAmmpihUrLojBzJkzxbWyyl79+vX5CitHSvQ+6Tjy8aXs0i8YGPv27ctdI0aMME6VBf4xMiGo/9P8y+rYuXMneqMa34SUBQu5F3aEmYtatoUAap+wTarDbWfryUWRObQZtWQMPUjaAdbuOMgHVWgPvE4mCEuUKMF3DpVCTnXv3h2lFmmWGVAGaLGg4EvJ+Ct7wPh4TJw4sUyZMoxE/PHkogzQslkuYC+u8pVFaeC9ohwwbCEt06dPl+CT6MdKi0JRzps3L3kbM2YMOgRfYv2xZExm0DNkyMC4hoKVNWtWLhYDG75nqMsyoShDv3wekEM+e0IRGbsdz1SgTvhoycxoq1attm/fzjegdevW8j2gpAymEBLeKHkW3Z3volQLlEbWf7hLDHcD9rzmgAEDhOFzrywgkBPyI/M7sb4Ciiv0mAsoKUqVPAT+QA5lvUu+rEePHg3W9PTo9OnTqz2xlj0fLM2RPXv2KVOmqMkmn/pHFRATIB18g2XJNxhE4ahXr16NGjXQO/mGIYcyMlDhaFTyHAqib0pHz0Nvpq25hY/0008/Lda5qqVgs5xFF0GFpSr4BquzPjXGe/3vRT+TgDro2UgX9zokBxWBFFlg4S2Kjj7++OPSNZYvX+6oAbRnCWDjBqfCZaBrBe/gstUEYi+rLgE7Kuzq1astu8ugAYirZzRUh9UAvRKtDjmESrVr107RBstuVuQE1YHWR5OgWUXdRytCnaJWqYexY8fCUfkchquAtyHc2rAVwzMVo2AUSpcuHRRCvwZVDOIEhxEP25ZtIMBdiv6BLFmyJEuWLNZgfaJM66uaCxcuDNhRfFXKsWPHAvZ0iRzOnTuXZrqmQfRIkUYynClTJlRqdTvDNfxWOaMWoqK75papEJ0DwCLgrmpyU0xglE4sHqTVJm0rZtWdkVOlyN4QnYtyFnVcsb6DBw/qgwYXO5zbydq+qmEgS3D/841pKW7w9OH0p59+qlmzpurs/kWzEtCUDslhKIP5NG7cWL9GqI7iovBzLtCbUoY7FUtJjHHUNIQVsx1DGSh58je+CCFyUTLJR8RRz9R8rJsG5dOg+1xVM7nKUYWPlFqhcVEkDZUA6VIPkd5BxcoF4hMBfcY/twLx8e4Y0ySatFpNlXl8nYvK/KYPF7VsY4HAjeZRli1pAW1iVJQfXSGXL50PFxW+xzdUpegB4eIN4aLohy/FANkQpVGyJ275J02apN/FR4dE5c8PopXMhpo3MRD4x8iEW/KfAQoNcOvWrQyDnksCKO2yuJpo1Rt+LmrZUkI/oQy6+9xQQPlRfFFxdJpqcJsArVSfEkay4+Tokk8FHUDZCYQ/fzE4YyPY2dOnT4txPB9793wH3ZKhOTHNAqkK93wN3Ye6Cst0DG3EB1WtavLMeKykwf9DN87xrH9oGN9X6hZW8+WXX3722WdLly6FyagwlZ5QNrqoLFRInNzNM4bAqXSVzgHqQSmmOkKpsWD3xg+Uize6R0tSihUr5rlV4cCBAyjWYdm9oxBrB6fIcRUetFJawTGey8ePX9pUr8Z/bfBS3vL9998n+a+AJxeVBT3FKMQRlL4yI5B90SrCkxAYfW+PKKyxLuK5uah7HUaML9Qa9XPPPQc7esoF0XpFWVfhjt1w+y4i27p+LxDZ4xddXHb7ywyIFcNFy5Urpy4WFqG7wpZS6G+RlSJ0WbWmp8PNRR2rRlYMb6RFghUNdOjQIUOGDD4X+BfNSkBTOiRHlqNlE4qCY79o3rx5IX7upmTAlwuEi+orTo4neHJRadBQuKgVs2dBmdigH6uQXT7w9F1EYQMx3tr9pdQKjYvOnj2blLp16zoeUq9ePWkg2ZRBSqwZtmL86jnGc5lGUZHJ4sdFhTQ+88wz+pOXLFkSsG2s5DAeXBQdPmPGjCS2adMmjN5bPG10Ge2VKbu4QlRr2uoCmWdXJs3JkydPly5duHKVZOAfI3P37t2OraRwToequWvXLrFvTUz3sTeFixoYGCQxoCvoClOcwFekRo0ajmlOgb/XPk8/uncPFi9e7LmPFMJWu3ZtZWFocIciFC4qDEqsT3XIGouy90sELoouK4fQJ0cAJHf+9WUuB4JxUQd1QWUfN24cSvmaNWvEgkPZxsePi166dKl+/fqytl+9enVHDkPnov7DEXflyJHD5wL/olnh46ISStTh21xnkrJ66e9TNxG4qMSvSpkypZhgIOrBjI90eHLRTz75RAmGv5RaoXFRWWr2qfnQueiVK1fEbMphHnnhwgWRSZmVCyMXFV8G999/vxzGg4tatj18+vTpA7Y12ZgxY8ISfTTYflGETVbhxNrcPWdUtmxZ0t9//305NFzUE/4xMvfu3fvNN9/IasHFixfFfFf3BWDZ3kDEfezGjRvPnz+fONk2XNTAwCB28BHq1q2bIz5TiOArK9PVuk+mq1evzpo1S7YhBYMoHMGMVJMqJk6ciKq6fPlyfSuXAvVGQ8TJpafB7YlQuOhbb70VsM3UHfdKunKulphctGDBgqinwUxGxUuc8i7mRihcdOvWrYUKFVI8SkhgArmoZU+KUbFiFJo6dWp94SVcXDQyMpJrfGI/+hfNCh8XldjIjo2XOpMUj2X+Bi+JwEWtmD38vEWMhPXPRDB4ctHt27cHYhzX+UupFRoXFZ8UjkgQOkLnotevX0+bNm3Ay2QAUYSKi11MGLmomNYr9wrx46KWbUL/9NNPC2GuVatWrLbiscI/pguoU6cOF4wdO9YzXSkhhot6Ik4xMsVk1+2dB31PXBnp+5tuKgwXNTAwCBWLFy92ODEKEbIdMWPGjDVr1mzUqFHVqlXFDab/XeJIVndYleTBl17MovjQehL19evX+5igG9xBCIWLyv7DXLlyOVYkZF1UbbdOTC4q25vde5u3bNmC2irOutyK5okTJ0QPjpWLkuesWbNWqVJFXRAWLqrCVERFRQnH0Lf5hYuLSiwi97Y62REaa9Gs8HHRcePGBVzhuHQmCTtKlSpVRESEe8Jr6dKlYiGfOFyUAY2cZMiQgboNMfapJxeVTcISzNxfSq3QuKgY/Xbt2tXxkD/++EMcKMTJRvfhhx8OaHb1AlkXVaIYRi4qHtolXJYVLy5Kn1VvobziRdnfxUMoiJWL9u3blwtU5DYFWRdVWTJc1BM+MTLp1LLtWZ1iLFWE86QNpeD9+uuv4vQncTbLGC5qYGCQGDh69OjUqVNff/31efPm7dy5M9YBjk/jkBhMmDDB0/NbkgRK86hRo/xDGhgkAYgzFYdFooNRXL58uXDhwgHX7qmqVasWK1ZM7fNJTC4qzuqyZ8+uhxo6duyY+F/Zv39/smTJAjfuq0Q9gv5Jl4+Vi8pGR52widMgVQPx46ItWrRwVCA0TDH8cHFRmEbA9rGnh6ihLzPuhVI0K3xcVEw00df1EKbTp08PaKbd4t6mUqVK+lLkJ598onzgx8pFT58+HdAMQQWeXFQWzD0361oxk5Xp06cPcR3Gk4v26dMnT548sijtL6WWV+9zl2Xr1q2kIM86ZaV0jRo1EmvSOHHRWbNmcbHEr1JYv349iQsXLpTDjz76KHDjYrXcpfsSkwFBn5H05KKvvvpq2rRpxfIZlCpVSl/jvX79ujgWVsbqixYtCtwYCp5OpM+HSlaVLQZ9xx3MNhSIF0Pde5kDZCllypSpUqXSDURpVphnhw4dVIrhop7wiZGJ6Mp/6SPIAEMThzJEbN++XdwayXNoXA5DiQMfFhguamBgYGBgkNiQVZdWrVpBKWE44jKtTZs2Dvu0L7/8ErWsTJkyyhHXunXrUMJUxE44noQcVIseKBmyui4h5nwgBEZ3lSnekvTwJxLyRLlXIZ/iCxrG9eKLL6Ir9+rVq0iRIkrpF84mi3JvvfUWOjFnFTeTEL56ZCbxo0sRhKyiAMnty5cvP3jwoHg443DQoEGyfghd4VAPjCy8KzIyUqVIcCbdtvmhhx5S8QkByr2iEMKd0qRJo/vwEE8zuiom8W8mT57sU5/Xrl0Tj9M0EPR73LhxcJ6KFStK28VatIQ0pVtyJFBZgQIFNm3aRNF27dolrpIgM5AfdFPqTTYxQuMHDhw4c+ZM2HuNGjXU2sj48eMdy3Q8P6A5sKW8EhAV/nDq1CmpYWlQsq1POIqd57Rp0zwz/+uvv6ZOnTpEh7RWDEPTHYkjYAikuO63QpBSd+/zLItE3SRvCAwEmCZD8NTaoIQXgsyHkmdqQ2iYms7g1dS2ziF/+umnFClSwH7phkeOHJk0aZJEkUG2v/nmG5k6kSXfGTNm0ILiyF246L333qu82UEksmbNqs8xCffmXkq3ceNGpEWEYdiwYSJsErAaKo6sMrbs27cPLkqvUfM13EjG1CSpSJeKRBo6pGe5g5brkKmE9u3bq5TXXnutYMGCyq3r5cuXZZogFIvuuw3BYmQigUI+GRA4JeQTYZD+TrcVpsqwoMKaOLaS3jwYLmpgYGBgYJDYgF3kypVLaB5UBC0ZvVBi5OTLl2/ChAmKEqA3oO9CcgYPHty9e3c0WhX2DQVCcb9GjRpt3bqVFFmDkqUSFWjXAZTviRMnSmQsiRSFpgJFkfUTFOLXX3+dHKKpiE1dwDZWhEFZtsZcvXr1QAygGXoQS+gT5Epi0oJHHnlExbF4//33ixYtGrBjJqFc/v7776g7sjonqqcs44iaG7CjCm3btm3Dhg1CmYYMGQI5rFmzppzt168fhUWHrlatmqT06dPnhx9+oFyydgSHp8YkxCLZ4NUcfvDBBy+99BJ1KIo7upp6HTUJ0aUhxEpQMv/RRx/RECNHjhSWiLKuQp544vz5840bN6YC5QmtW7fWlzR9ihbvpgwmOejr3bp1k7Bh5IdnQgUzZ85MPa9bt07c+ZIBVHx5BdXVo0cPNeWxZMkSOQWrgVRfuXJl0aJFefPmDdjhuKCpctmAAQOEFTRo0IA3Ll68WDUohIfqRbV99dVXJRtkb/To0Z6xmmBl/jxfhzhmh31BaSgjlVy3bl2HPyp/KXX0Ps+yWHZkS1icZD5gh56G+MnFUHc4vKTTK0NxJgevo6Wgx3B+yHC9evWQK4e7cvinxJaDGFNX9H2YMJmHdop15apVq+QC3i72xsJFy5UrR3nJOe1bunRpxxL0mTNnJG6KkOdjx44hpYUKFULUpVPT/cVpUNq0aWXxEy5KDdepU2f+/PlTpkypWrXqnDlz1AMlELFYRIcIZEP5DwvYgbt9YrbT7xA/Oju8lPZ9/vnn1TZsyivG8AF7UTrWwO93G3xiZDLsy/ZRAYOMovcIgGwfVTh8+HCcgmUkBIaLGhgYGBgY3AKgUh84cCDE7z1qxL59++K3YftmICoqCnakwgs7gD5E0eIddggCqTvb+OWXXxIYwUjqDaKFlnb69OmEPCoUREdH8yLd1FYh7EXzBxwS7id6PDzZ0/cMRAXO4xlpMBTA8RK4hwJdGZoaD6ed3EKn8Fkc85FSz97nWRYqjbeEMa4JMiDxHj1BblWh+HVL0dmzZ3XbY2WjKwHJgkVn5ezRo0eV7LmtvuG6iIEaYZCH6zZ4IPlxiIe8K4SyJgi0BW0UFv+9dxuCxcjkkGGQimVMcH96uOsPG4m84Gy4qIGBgYGBgYGBwa3B/PnzdUtggzjBc7+ogcEdBMNFDQwMDAwMDAwMEg+XLl36/PPPZR0vMjJSOU0xiCsMFzW402G4qEESRzATssTH9evX1VacuwGnTp26TUxr1I6IRIMudRcvXgwWk+3vv/92G0px8fHjx8MuKjww0fZ+hAV3W38xMLirII6RBOJn2CB+WLZsGXVYuXLlW50RA4N4wnBRg9ixZMmSxo0b16xZ84knnnAEzL18+fLIkSPr1q3L2QYNGrz77rs7dux48cUXawaH+Gz84osvWrVqpadze69evaZNmwaHCT1vc+fOdUQ7EOzdu7dHjx733Xefw+37LQE5bN++fa5cudxx55IkJk6cOHDgwCeffDJ9+vTjxo27tZmZPHly4MYIEzcP+/fv7927d7FixSTeumUTy9y5cxctWtRx5c8//9yuXTvxOFKqVKmzZ8/K7SRSe0hL8uTJdff68QYvGj58OP0rZcqUsYaFCAYaUY9XdrNxt/UXA4O7ED/88EP16tUjIyMZoBInhmGSxNSpU/mCZMqUKXPmzF26dPnwww9vdY4MDOIMw0UNQsLJkycl7lnZsmXdzjNmz57NqW+++UYOr1+/Lv7lGBn/jsG5c+cOHDiAjt6wYUO57MKFC2nTphVXbH/++ed33303a9as/Pnzp0iRQvdF7oOePXu6g1kLyOSYMWMCrhBktwR//fXXSy+9FPCKgZ70MG/ePAkXfvny5Vq1at3y+ofYQA4TJ0zWpUuXJEqbCs+IjlWnTp3nnntOv+zatWuFCxf+6KOPLDuaX8GCBU+cOLFz584CBQooLyZw2ixZsuhhqeMHyPCZM2fEH2a8uSgYOHDgZ599lsDMhIi7qr8YGBgYGBjczQg/F0X1OXjw4BYbcA9PX0zHjx/ftWuX50zY2bNnOWVMs25DPPXUU+J9Xg8gLoBGZsyYUU+BcHLlyJEjHVdGR0c3adJEHYqKrDyqA4QnYEfo1mOFe2LQoEG9evXSUyDMKtI32LZt223CRcGCBQtC160dBbkZWLlypQoUFl6UKVNGD8x9t+HUqVM6F/XEihUrAlqQccETTzzRokULPUWPdphASHA/nYvGQwCqVq3K4ByuLPkjTv3FwMDAwMDA4A5FmLnotWvXIAD/+9//NmzYsHHjRv5wqHuChn+eOXNGYte4uWhUVNTmzZs5FQ/X3gY3G3DRUaNGSWArh+El7aXHGQeNGzf25KKWbZmj/t93330OLmrFENRJkyb5ZAbpypEjh+7rHDErX768HrT9DuWi7oKEHcePH8+cOfNXX30V9idfuXIlViaWtBEKFx04cCDXHD58WKVQb/Sszp0736RcScR2xUXjJwDr16+nm1+8ePEmZNAJw0UNDAwMDAzuBoSZi6KHSfjUq1evwkslpuqJEycsW9nau3cvp1QcVZ2Lopbt2LFDnTJc9DYEXBR2N23aNFm3VBGfwZ9//gmr1C/25KKwrE8//VRPcXNRpAItmcS5c+f6ZKZChQqtWrVShxcuXJCVn2bNmi1ZsgTBszQu+u+//5Jb2B3P1L3pXLp0aeHChX/99RciOnbsWLUSSz6XLVv2+uuvz5kzxx1qDI2cck2cONGxruUGT16+fDnP+fjjj926dVRUFM8fMmTI9OnTFT/3LIhlz/KsWLFi+PDh5FMlqtzycLK0ePHizZs36wX0LMixY8ckEDzpvELFItu/f/+YMWMmTZq0YcMGf5eGJ0+e5I3kfP78+frm3tWrV8+aNUtCaS+xIdsgdezcuXNJDFSFIxUcLl26VJzreNaMgDpHWqgNKhZRZNxQT1MWpN98842kKOq1ZcsWCqUewjNl2RlKNmHCBJoSAXaXcerUqcjMJ598okJsBwN1vm7dOlqHx1J1Di567ty5mTNnynD3888/k7E6derIhA7/EScyzLtIqV27tirOjBkzePuBAwf0F/3yyy/UzKBBg5BkmYihKqg3uUW1ghzqAeV1LuoWgE2bNqn3qsXSVatWcfj+++/rGciTJ4/nBJMCIzwiSs5pU32E54tAA9H6ZJgqHTZsGOO8417//mJgYGBgYGCQ9BBmLoqqgYah1EehpqLcoBaL4e5XX33l5qK7du2Ss4aL3rYQLsqfF154ATUxa9asMstghcxFV65cCcHQU9xcFCWblOzZs/vElUbMuAZtVaVAKmStqXnz5h988AEXWDFctHPnzvXr1yc/VatW5VB27v3zzz8o9JkyZSIF9bdYsWL8qVevnmWzHS5GXV67du0jjzySM2dOpZ1HR0fzfPjGxo0bO3ToEBER4WNJu2/fvhIlSggfW7RokSz2Kt0aUc+SJQva+cWLF4cOHQr9FutHz4L8+uuvPIp0MrBmzZrkyZOr90Kny5YtO2/ePFR86FaaNGkUcQpWEKqlQYMGvALCwCvEGRV8pkqVKjAl8tO0adOePXsGK9eUKVMqVqwIH4bDkKW0adNOnjxZTkH4YUo8uXz58h/YcDN58tmkSROuIW9qM+Tp06fJucxuBKsZ6vyxxx7jxnbt2rVv314mLLZv3963b1/+kCW1jZnHPvHEE4MHD2aEgZ9L45JVy2Y7PXr04PA///kPdQj3a9iwYbJkyUqWLKlzeAT1gQceOHjwII14//33cz3krXTp0uTTXSFQzccff5zXMdwxuFWuXFlxUQgt4iemBFJYnkC1CBeF+fOfVoOLyt5mniOEcPbs2TQrKTSfehF1y42bN29GSDibO3dumTKgG6ZLl46L5TLq7bXXXlNFFuhc1C0AFy5cqF69Oim9evVS9QDXpSH0KSeAWObIkcNzewU3cpaa5y3IXmRkZOvWreUURF2qEbrOq7lMOr5OdP37i4GBgYGBgUGSRJi5qPBMxSLQRMVeV9dd/vjjj2A2umgzhovetlBc9OrVq/AWNEU0eDHYC8ZFy5Qp818bLVu2RO9PmTKlJxdFyd6/fz9qN5dBtHisY+nPASgud0lmFCC0ol6rFOGiRYsW/e677yQFjgTxUNIl7BQWwf8vv/ySl1K0Bx988MiRI3LB4cOHpZhy2LVr1xkzZsh/qAV8JnXq1J78hGqBKkydOlWl9O/fX9eta9WqlSpVKukCMAFKDbkNVpARI0aQorzvUIpChQrJ/48++ggeomJ1QMzE+Y1/Qfr168ehbqJZqlSpUaNGyX/qB8LmWfOrV6+mAnXj0k6dOvGozz//XA7hIbEGOoOzQc/Ev5Hg+++/l4kA/5pZv349Dy9QoADsi0zOnTv3ypUrVHXWrFmzZ8+u9gIwjFA/8HY5FGdCOjHLkycPGVALid27d+cCBEAO4bTZsmWjreWQonEWdhesOE8//TTsXR2uWbPGsS4qNEz3QiSOefbs2aNSvv32W1L0aO/S6Gqxl9Yn28o+VgqlclWpUiXFRS1bmH24qOUlANJZKItKOXDgQI0aNRyFffPNN7nMc9coOeQU2ZbDPn36cKiWzWfOnMkhjJfx37L9AqRIkaJatWpyNtb+YmBgYGBgYJAkEWYuKkxSLYacO3dOUnQ9zHDROxSKi1q2Kpk3b16URdHCg3HRLl26bIsBNAaa4clFUXmFFkIq9u3bF2tOnnvuOS522JEG46L6flHhAHv37pVDCAOHx48fVxcsXrw4U6ZM72iAbYpK/fPPP/Nn6NCh6hT8zbE8qyBEQrftdNgcLl++XN9zC/t68skngxUEot6zZ0/lBgxWnyZNGvm/dOlSLh4wYIAsZ0Hq5KU+BbG8qEiRIkXgeIpkqipyoGzZsoULF9ZThOXCe+UwFC4KWrduzWVqxmHQoEEqMI9Pzci7dNtsAUJFupomgA22b99enWU8cRAzaDAEXh3KWu7s2bPlcOvWrXr9U7HkoU6dOp4FEQKmW56794vKkmNcuahMuCguSs2//PLL6uz169eRKOV0VxZjfYocKxdV+VQyABt0yzaCFMx+PioqihweO3ZMDoW1KpuCjz/+WJaC1fX58uVjDJH/sfYXAwMDAwMDgySJcHJRuKUwSaXxQCkNF00y0LmoZZtVw4hkJSREG1301GA2umJrKhaYseakbt26XOmw/wyFi/JfX1AVLqrveOzbt29kZOT/XEDPlvUxWIfjlNpvqaNmzZrZsmXTUzx1a+ptypQp1EmKFCm4JVhBBHSi999/f/DgwbDB5MmTSyL1JjaoEOONGzeGUhDLi4rMmzePlJQpU/bp00f3CKXj6tWrERERFSpUcKRTUtKvXLlihcxFv/nmG9XW0KoqVaqopV2fmhEuqvNMwblz5+CWVIs8BKKrR3CJlYs6mubkyZNiI60uyJ07tyMoiwLNxMW6z+ebwUVpZVp84sSJnnmwwsRFRfCkehmcqSV39CaZ+xg7dmywnFi2dQwN9/jjj+uvcHNR+n7OnDnlf4j9xcAH0dHRSMvBgwdvdUb+v5msWbNmxeoFmp7iOZF3q/DJJ58o+47wggpZsWLFzXiyQZLBX3/9tXjxYn/VN8SeZWBwxyHM66LiBVfN1qP6cKiryJbhoncsHFzUshff0BeTJUu2aNGiULgoOHPmjH6o7xf94YcfsmbNyuGECRP8c9KoUSMHh7TCxEV58j333OP50kmTJnGxw5dMMNx7772OIDcO3RpRp3LIgLw9VapU/lwUDly7dm3J+RNPPKG4qGX3Mqlt0KFDB/lQ+RTECkJFILrZs2cnncx7elilX3NWrWUplClThnRhuSFyUfDwww+nTZuWuyjv8OHDVbpPzQTjokB2gX744YfQp/Lly+un4spFATyK94pvqiNHjkDRgxmNt2rVint3796tUm4GF5WzgwYN8syDFSYuCh588EEKSyfllJ4ZhYULF3JjMFYMEapTp868efMY2yX/IXLRWPuLgQ9OnDhBx6fhqDFleX4LUaJEicCNW50dYBx79NFHA/a27cTMmA9+++23gO2TL4y6B0Mxw7gYEDFoh+uxBkkMp0+fbt26tbgVUPuJPBFrzzIwuEMRZi4qvnCVci/hW7Zu3apfY7joHQo3F7Xs9TcGR0hFiFzUspdcPvjgA/nv8F0k2xFRCNasWeOTky5dunCX7ibUChMXffHFFx0kQQAhkRWht99+233KnUP5Zugrtw7dukmTJkWKFFETnP5cdPLkyVSLWoDVuaiKxEvViXNU2bDnUxDLi4rIc+h3snkSYuAZGThLliy82hH+t2jRovny5ZP/oXPR+fPnB+zIPS1atND9VPnUjA8XlT2oFSpUgFGrja+CeHDR6OjoevXqwWkRGITtm2++CVaKrl27cu+yZcv0nISdi547d47/qO+Otyv3v+HioiLknO3cubNn9FGZkeEy9ylqKXXq1DSrnv8QuWis/SUJQ3ealRDUr1//NuGi7777btOmTfVgtgK9pN9///1txUUtu1f6+GyLN8Qb393JRcMl20kSjsrJnz9/rFw0WM8yMLjTEWYuevToUdQgdCzhmfv27ePQYTVkuOgdCijB/1xhGK5fv/7kk08yhobORWfPnt2/f3/5HxkZGbjRj+6wYcNIyZw5syfHE8jijMPD59q1a0nUbYDjwUXFwwqavR4Ud86cOV9++aXE6rjnnnvQotQpJHz06NHuHMp+SP2U6NZTpkzhP6wyoPmJoQ51S1R3QQoUKECFKCvWxx57THHR6dOnnzx5Uv7DTPLkycNZ/4LwZ8CAAZzVW5MU9Z9sc9ZhzqCXi+eoFCgrvK53795yGDoXvXLlSo4cORAbuKhK9K8ZHy4K2rVrx9n777/f4YE5Hlx0xYoV0lKxQvaa1q1bV6UIF4VRq5Sw7BeViYaPPvpIXXDmzBnVv2SVSVFT7grYu4jVxQ4u6hYAASMwFZgpUyblVcgB2ZorvpcdaNOmTUBzazR06NDQuah/f0nCWLZsWbhWOcS9+e3ART3hKCmyertx0ZsEusBdy0W7dOkSa0CsuxNwztdff11P4asUKxc1MEiqCDMXZdzZsGEDKs4uG/oWNQXDRe9E0Fj58+eH+bhP0b7orw4uKo52dW3Ysj2Uvvvuu6lSpRIlmOaWqCr6riFeVK9ePSEV7oggAkQobdq0sFY9UbT5WrVqwb54PjRGvIm++OKL6hpR15QKLra+Ounl3nz58gVsh59w5jVr1vA17dSpk5xt1qyZsG5U6nXr1sEEIH6euyshrhEREWQSFZycIM81atQI2GFjyKcwLs5u3br1wIED6PfUiZCos2fPugsCFxW9/Oeff542bZoYfR07duz48eMwKN3F68MPPyy00L8gkydPDtgOhKnt9evXW7bvIkVUPv/8c/LmWflkDzZeokQJtTTKoyIjI1UlnDhxImA7o/JsOAckeg3cW6X418z+/fsDN+7k1MG91Lnyx6sgxExf8XjggQdSp06tpqXFH8+kSZPk8Ndff+WlnTt3RixXrlzJgEaLyG5YN65evapidSLePJP657BgwYKQeXlFuXLlAjc65hHnW5s2bVIpX3/9NSnPP/+8ShHWp6KeLF++XGwIu3btunjxYnpW1apVz507J2dleZZfGhGxF0FFONV2idq1a5OifD67BUBBPPQG2xH65JNPlilTxvOUcFFYJY314YcfimvfuXPnijMkOFLAjumiroeIZs2aVf779xfP1yUBIOHp06enyGF52u3MRd0lNVw0yUMWhN2hmw0uXrzIN1T3RWcZLmoQVvAV3rlzJ0oIv+iNKp0v/p49e3bdCKVICK5du7Z3717SQ/EkGi6EmYta9sII5RdKiRrnjhJpuOgdBxRicReUJUsWmI9EZdABnUPhlv87duyQOB+iOkNyKlasWKFCBf6ga5KYLl06NPsvvvhCqCCANb3xxhuq0cUTkij0wRZG0PhlAVCHxJ9Ev4F+oNzXrFkzYIcqhb9Z9hKi7Ickffv27SNGjEA9EtanbIYtO8KnqNGAC4YOHaoWJGFcqNopUqQI2LtkYRQ+1jIIv8RIzJgxI4Rw/PjxsDgIIa+2YshDwA4pCYmCXwXssJzyQL0glk0PZDMYrIzHUhD+58iRgzLCo6i9Pn36rFixArrVsGFDFcvEpyD0yty5cwds/7cSJBZCVbly5Xnz5s2ZM4e3+6zVMK4hDGR11KhRr7zySqtWrVTDffrpp08//TSPhVfQoG6LbgdOnTpVrFgxxzgQrGbIEi0l8vPWW2/p3o8VoGf6yqFlr8ZIJeTJk4e6ioqKEv+uwk7JAMytePHiAdv5k7CyS5cuieToQHIc6/AKZFJWPmkjGggaBtFt0qQJf44dO0Y9ICrCM/kq8MZx48YhEqRUqVLlvffeQy8hXdYt4WZTp05lGFy4cKGYDFDwdevWyYtIFAEW1VaFcbbsHUdi5hqw9wxD2ulr9C+kgvaCAYr8/Pe//928ebOnACjQN9OkSQPzd5eUmuEU2fCsB0hjrly5ZJSgFOQBMaCzvPvuu1u2bGEQCNhhWiEk0PJXX31Vcjtw4ECZrPTvL0kPUHSxyqMf0VN0HfTMmTPILaMWTa+6swKD7fz586lGuoCaa7Bu5KI04jYNemehLejja9as4d5gk30K+kNofW7RU6ThaE051AUSYVAOmT1LqnNRykhJZ86c6dh24Q//WgqGy5cvr1q1in5HR6A4KkiSZVthMALoU+f0RB4uMziUCElWkZ8cz6Q+GV642DHzbgXnotQAOWEwJye60USs4BWrV6+mi/F10M1eVGb4BM+aNWv58uW6CY8CAkDv5rIFCxaoecCrV6+uXLnSsmfiZsyYobtFiDWf1MxcG3qsL+QzVapUAdt8iUb3HE8cEOdblIuh3n09siE2Fwxo5JzR1V12T9mOtwz7F9yzGkMBj0UYAvY+Dt6oDEkUF0Xq+CLQCmrk16H3LEGwAcEfPIfPPSKNtLhVcZ9Rwn3qp59+ktpT7vcPHjwoKY7oX6gKotJQRvrF7Nmz1deHPJAl5NZdajqg9Du0I1S1pUuX+gSfN7DsPiJMatOmTQ4Xm3QBt0tLh9gghOr2RMtz+LmoZY/p9DeodpxGWIM7GvrUSyLgwoUL6P2OkY4BTobyhD8fAYZIeAownZmPQYjaD9xDxmu+do6ncUqxegZi9Ab1SXAXhPzoDnu5V77Esl7Hfz5InsQ4WEHIv66pyHMYknhOKN2WNx49ejThHdzz2+lTMz6gCPCxhPsYpKU6duxIPezZs4dPIN9OPn4wediUz13Us+gx1MlNNUuT2KrudEZdZEZUK6oiVvl0CIACfapx48aet6AmPv744z5tQddA2NSUB40Y11URn/6SxEBlivaJSjpkyBA1HTZgwIAHHngADR4NuEaNGoi0volg+PDhKLKojwhn1apVa9eurU7pXJQmgMNz+NRTT8GvRLOnPjl8+eWXGb4gM/DAN9980z+TY8eOlSkDKB89i6YR8/KAvUdaZAw617t37/Tp0+/bt4+P/ogRI2RaBDXXp6SKi9LFcufOXaxYsYiIiGTJkqn9xv7wr6Vg4Bq+Gui7dCJ0/RQpUogzCyqEapHZGaHKf//99yuvvJIjRw5SqCtyft9998ncpb7pw7I5UvHixakftPPq1aunTJmyTJky1LOycfDkohCYpk2bTp48edCgQRkyZChfvrynP3Y3UN+rVasG8SNX1GrOnDn1Xd8bNmygKsaNG4ceOWzYMNhgq1atZNED9X3w4MFUWsC2DKpQoYK0I8Svc+fO99xzT7p06aAQ/JGZu1DySX0+88wzPXv2pOwSlql169aIGbXHgClGT/369aPRfbbcC+CW1DatjxR16dIlc+bMynwJ+ZFsv/HGGyNHjsybNy+l5pAiqCHCR7bjKsP+BQ9WjSqWVayA38rMI/dSM2rbgvQRnon8IKUyX8mXSM569izLd0AIBlqHuqpbty6N8tFHH+XPn5+Squ+mT00GO0XexG8I1SJXUhuyR0PtwoDV1K9fn97BNXxiHnnkEapUJASRPnDgAIcPPfQQgkeK2vLDaPboo48yLFBjMOfUqVOLh6e0adPq6wcGOhj8xYms7N5CYsWDrHQWWQukBX/XoE/r0BcYRrZs2ZIUuKiBQSJg7969jFCOWCAGdy3mzJnD9y+BD4FoPfbYY7KQ7oDDpCqpAm3Sc6vw6dOn0RUcfrANEgLoCnqVbrmKTk+K2k4vW527d+8uhz/88AOHKl4RSoYe9lbnov/880/jxo2V2bkAAiM2KXIICUGrjjWT4iVbKSUoNOigDn+zaJPSO2TdSTZo6Bqzu6TCRdEpkTeZu0HqAl5uut3wryUftGnTplatWuoQEiXrLWQAdirav1qgllhTpFSsWFEmPSla1qxZKbvqBZS3cOHCanM1z5GHoKkrNxluLkplVqpUSc3pyB6BYDu0dSxduhRKrPZHwN+4sWjRonIItSBvyqrfsve9cwHvoiyQLuRHWByycfz48cWLFzdr1gyFFUpPIsQVRoFQwXmEb/vnE/0V+gRRVK8rWbJkQNtWIIvhocxGUSLezrvkkKwiGKVKlVIX0NYB205q0aJFlr2KK6ZDymmcv2zHSYb9Cx6sGh3+/Pzx3nvvcbunjS7lEloLZ5a3iFGDZ8/yHxCCQSpTuYeUzSDKnsinJn1OiTcNxUUtm/HqXNSK2b+TJk2a1157TaKFHTp0SK5p2LChDAKkIzZQVplYp1Ylato999wzbty4s2fP8lhuFyskz7lUg3PnzolRqujGiDFDECkyI0l/57+PRczu3buRKLnMcFEDg5CwefNmVBATbutuxttvvz1+/Pjly5fzIXRbj8cVjNcB2/OQPlPI/ylTpiThCIFRUVF84NHGJk6c6DZ9t2wi2qpVK+UlyyAscDM0Pv9oe/PmzZNDlMuAvYlADoUz6B62dYdbiouixj355JNuu0HZnq3Ui3///XfmzJmxZnLGjBncpbaaA7Gv1udreJ1uNygBlkLhoqih+jK7bIyPlb3415IPKleunDt3bmX/CV3Up12EsejG0v/9738DdkxplYLSHNDc5gkN7tWrl7pAdk3rhNDBRSlvZGTkpEmTrsVAvJ0p1hEMEOBMmTLRHCqFFmzevLkK9VS2bNls2bI5zBbENl41tDg5cwxl6KzJbOjbxmLNJ8Q1b968uvEO9KZGjRpKEkLnolyDJHTo0EGlMJhHRESoQ2TJUc+MVAHNI52/bMdJhkNpIM9qDB0+XFT39CmypPcaR8/yHxCCYcSIERkzZpSIZVbMTn5xv2/51qTPKakinYtCnh1cFJCCDOsphQoVIlFlBrRs2TKgOfUQV44OswJxf9CtW7dYC3sXgrag9vQdUl9//TUpYrd15MgR/h89enT79u1bt25F3nRV59dffxWTXYmBYriogUGoQD/23FZhcDeAD54YzqVIkQI6GpZnigUXn8yaNWuieorhk9vlbFLC5s2bRdnKkSOHp/OMZcuWuXdnGSQQboZmaZEe0AZkyUIZh0MVZNkNJdW9Y0q4KIpp4cKFPTfZMk7KUiR6Z+it+ffff2ewoay+xWG1iuKLgu6YvxB35aFwUYfvIvHy5U/JBD615ANZUcmXL58ehMnxdjcXVb6sVUGUfaAEpkJ7VheMHz9ev8BycVFZHapQocJTLvhvsBfv8Tt37vQ8K8GfHaGVrRjOptx6y054t8Vs8uTJddfioeQTFuF2FKcjdC5qaQ2KmM2ZM0cijSspFS6qW0cLnWOslkN/2Y6TDIfSQMGqMUT4cFFd/KQfzZo1y5Giepb/gOADVdv79u1DNngC5FxSfGrS51S8uah0On0mS8YxFTZM+LbDM7/wZz7NoRf57gGcE3VFj4jOoEGKiNbu3bsdW0n5+styzrVr17Zs2SLu/Q0XNTAwMIgDGGdHjRoVb7XAE0eOHJk6derQoUMXLFjgjtGaJLFixYpx48aFsunOIFzw5KKWPY3dqVMnpHrv3r2iFqtTa9askckXFOsxY8boq1Kiwz344INiPei5rXf48OEy6RAZGSm+akKBPHnu3LmWvUJetGhR2fAmLo7Rjx3OexPIRUN0JepTS8GAfixRWAO2g3F9Ncbz7bFyUQaKgO3YTEVj7tOnT8qUKfWgRw4uKnaz8djtJrXqyLOC8IRixYo50j/99NOAZscbOhf1z+eFCxc426xZM58Mx4mLWjaf6d27d9++fZEr2ZCpajVWLmrFJtuhy3AoDZSYXFTvR+4UnwHBHxSwbdu25ETCkvXr10+d8qnJYKfCzkVVbAVPLspHP2C7crRsG+MHbkToDpySJNxcVGKaiGgxWiK3ssvg4sWLYr4rHqS4YMOGDTJfY7iogYGBgYFB0oeboV25cqV79+7wSVGnxPrUwbJ+/PFH8VYdsA1T1fYt0eEWLVok7qaV0Z0DqBfK5XIo+0UteypdrUKgDU+fPn316tUB2xM1GmeRIkUcEY9uNhcNpZaCAYpOxsQfderUqVetWuXz9li5KJg0aVJERARXnjt3DgpauHDh2bNn6290cNF58+ZxGKvXKDdkKU83GNYhrqogJJ7patEvdC7qn8+TJ09ytmzZsj4ZjhMXpdIQBqVAx4OLWr6yHboMh9JAtw8XtYIPCMEAFecyJFmulDVGnYtavjXpeSqRueixY8cCMWG9GfFeuBF3eRghcaLrttH1jAouJrsQ1KtXr0JEGS6O29i3b59sOuV/rBIVFhguamBgYGBgkNhwM7RBgwaRojYdOFjWiRMnlJq1du1acW2iNq3p+0XvvffeZMmS6UTLsmfH5c+///47YcKEFClSwEBC3GJdvnx5Ho6mgrp5+fLl69evwzTuueeeGTNmOLRY6+ZzUf9a8oGqgaioqLZt23KXHiw3flzUsr2ade7cuWvXrhCYo0ePOl7q4KJiD1+qVCmH1z1Isn9s2NGjRwdsX8SOdKSCGrh48aLQAz0cixWzLtqjRw85DJ2L+ueTX65Hxhyvs+yYH/IndC66fv16rtQDZceVi4Yi2yHKcCgNdJtwUf8BIRgg5BEREeI9yHJxUZ+a9DmVyFxUQscr72UGOs6ePetY0hSnuIwSyLBsgVanJHzL7t27JZq9J0KPmJUQGC5qYGBgYGCQ2OjYsSMa1eLFi1WKeCJVLEum/9WuNkiR+BEViAavfEfrfnRRPlA3M2fOrIea6N27tx55Sxidp89kN2bNmsXFuXPnHjt2rKRIzAY0S0d8WstLh3aXNCFc1L+WfNCiRQv9UJRyZdYYPy766quveu4+VXBw0b///ls2Q/bs2VO/rG/fvp7BSxX2798vkYrVVjrL1jsh1WKP3apVK8726dNHv4tWTp06tdqCGzoXjTWfss+wcuXKujfaadOmqeoqXLgwF4Tiebtbt24OLiqxPZQSHCsXDUW2Q5ThUBrIsxoPHTqkex7yAb04cKMvJSteXNR/QPDEuXPnArZFAMWUlJkzZ+pi41OTPqeQAalJNX2AyAVsBwT628PFRel0adOmTeQ4gncKrly5IhxS5ikuXLigKCWNLv/Fa/H169d37NjBIUMow+AZDQizRILhf+IEVzNc1MDAwMDAILEhm6+gEFevXkX3unjxYvXq1cXQ7ujRo6tWrZK1u+zZs+/bt2/37t2ong899JDiTqgLkBOUCTkUr5vK08m4ceM4zJ8/v1qpQ5HV1WtoQ86cOXlpKFlFj8mYMSM6ulJhT506BYFx+LfUc6I0fs+S/vTTT6SkT59eX30SP7qU1D8z/rXkcyO198knn6jDZs2aPfXUU463686BZHOpvlxZr149UlQQ1F27dgVsC1j08kmTJs2ZMweaCkXRt+2tXLkycKOflbffflvWMKE01BI3ctbBIT0hajogY2+99RYaeZEiRWTHo2VHAYHbo+urlNOnT9PESIJ6QqVKlQJaPA/B5cuXSUSWFJEIJZ/wN/hAwPYF9fLLL3MBuWrXrp26/fHHH+fsjBkzEB6oo0+5xPvUvffeS9Vt27aNp+XKlYsUGlecxolHKIqvbpGooep1och26DIcawO5q1FW6hwTLsEgS6/3338/POGrr76SoKYFCxYkUd/mJ/2IsjtSVM/yHxA8QVunSpUqYDsrgoEgsWLST2PxatidT036V7JMPVBL0Only5fTKzNkyEB+kH8JeCNRXtKkSaMHPkCAA1pYGvDcc8+RMnnyZDkULopsqF2gEFcakTaKtZ7vWuzfv5+Og2gxFMiO0L1791r22r6Qz02bNnFq+/btQjjVIrmC2S9qYGBgYGCQ9HHy5EnRueFRX3zxhWWvZ2bLlk00tl69eqE4ygpMoUKFUBxRPdHJ6tSpAxeaMmUK+jGqJHd9//33AwYMEI+aRYsW5dSVK1cWLlwoy2g8sEePHn/88Ufv3r3vu+++Dh06wJfQ/itXruzpbjcYYAjDhg3TUyBmju2Lx48f5xp0UKEoEyZMEC3HUVL4Rt26dUV3R/VEF0d/7dKli6RANf0z5l9LPjc+8sgj1M/gwYOpgZdeegkSIgouKlfnzp3l7dQq5JNnvvnmmzyflNKlS7///vukUDTR40uUKCEFR8nmIQEXihcvLhZxtIVsroPzDBw4UFm0ki7tJWtHHIbSBPB2SG+6dOnkRoqD0qlfcO7cuZYtW+bNm7d79+6IBNWi7LTh7RRZRKJYsWITJ06MioqybF1ftQXMXEXKCSWfFEd8ZQVi3KvqSyi8OiIiQmrjxx9/9CnX77//LrVE9sgDFFqiSqZPnx6ZpzmEp8FA4NXI9qJFiygjKZkzZxaqFqJshyLD/gUPVo2IdOrUqUl88sknfUoqQDAkUiiVNnToUCgxGVNtCnmD4A0fPlycEuXPn58a8OxZwQYEf0DzUqRIEbCDdnI9FJFqlNbnvT416V/JdCIqSkrx/PPP0zV4fsWKFUePHv3bb7/BiFq0aCFnX3jhhd27d1Oivn37qlJ/9NFHlGjkyJGZMmUSoi7TasJFy5Urx7DQoEGD9u3b0x/9LREM/v33X8inMrLdtWuX4v80sWwfFWzdulWP5KRguKiBgRO6Q0jHFg4f6IZDNxsOl5Wh+7KLK2ItFDmJU9DtJABEQs1zxwrRG/yB1h76A0OHu+0cmUlMiVXw9LZ6S3D75CQxgaSh0OvDGroC3EyFTODUoUOHRMWXTW4AzV6/JkQILeSuw4cPo1KHPpYK/vzzT8e6GfpK6K3mLmlC4FNLPpAaYIREUYPwJDwbf/31V8eOHSnXnj17UJo//vjjhQsXoutDSBwWnm5QdbQCGnlc64TvC2/0cRZKPXBBwoMtC2LNJ0zy22+/9Yzyffbs2VAi9FgxhdI3l3JjiIv2VsiyHScZjmsDRUdHL1261GF5Gwy0EZXmXo+KE+I9IEAO6S+q4ORc2Qb71GSslcwpsqG4DYKRgML9/1A2uryOTPpPahjoQNRpAjqRQ8JFS0QGGL7CNSAnHIaLGsSOVatWtWzZsmYMHn/88WeffXbgwIFLlixxDKYjR47kM1wzCLp27er/og9tyH+e3L9//wIFChQvXvzRRx/t27dvv379QgnODoYNG5YsWbLNmzfzf8eOHXwegmUJiFUMCkS9evVUYq1atdq0aTN8+PC1a9cG+1bt37//+eefL1myZN68eStVqlSnTp0+ffpMmjRJdiUxXnO75xc6ftiwYQOFooY9z6IMUb358uW7e2xX1q1b16FDh5w5c/obgFm2HzlUQwTJPyDewYMH27dv37t374iICP9wBXGFLpCnTp3isFq1avrOGf/GTQjQDOhHulbHJ2ro0KElbVSsWLFo0aLdunULi94QD6CTjRo1KjIyMkWKFEWKFHn//fdvSTYMDOIKRPeRRx6ZOnWq+xRKnsPFq0GSB2r9f//7X33ro0HC4blf1CDpwXBRg5Dw22+/JU+enEFh+fLl58+fP3DgAOpsqlSp8uTJ4wjAKFvhc+XKJetLICoq6sSJEzDJBx980OcVo0eP1qkm7LdgwYLih/rChQt82gOx7ctXgCSXKFFC2WuhNEDSuJ1X/B0D8TaGEqx2EEGDxWzm+++/5+y2bdtk6wIKh8MZ4JUrV1555RW0Z2jnDz/8IIknT56UkGVwdUn59ttvO3bsGK5l0kOHDlGoYHHPoqOjYTi8/e7hojQiDJMix8pF//nnH/HroG8PcwAZy5EjhwjzG2+8UalSpTBmVRdIhAc6yrt0ZyH+jRtvnD59umHDhroRzv79+3lRuXLl1HoFXbtp06a5c+devXp1eN8eCtq2bcvIsG7dujlz5oj3161btyZ+NgwM4oo1a9YwpDhsPi172WHw4MH+2/YMkh46deq0du3aW52LpAbDRe8ShJ+LomkdPHhwiw0Yi8MiQoAatGvXLoftJQRg+/btGzZsgAN89913ieO7ySB0ZMmSJXCjnzdxj4Feq1+2cePGwI3evRUaNGgQ7OHz5s1r3ry5Ovzxxx95yOuvv65f07Vr1xdffDF+mX/ssccCN3qhECxYsAB2Lf/37dsXcLl2lMhdugc/K2Z7vacVFqfgrupw1qxZvXv3jl+eY8XFixd1ByEyaofORWfPnn2ne6ITf/SxclHLHmH8uai4akyg0VToqFq1qsNxZdgRHR1dpkwZ5cjEss2Ps2bNGhkZ6fDSTuXUqFEjefLkjnmlmw2Get0PpPj/GDBgQGLmwcAgfjh79uw999wTsOMcMg7zCZsyZQpfCg5vybSOwa1F4oS+uNuwbNmygO2u+VZnxODmIsxcFAKJeiExUuEkEnFVt2KHf8qmWKBzUfEgDDZv3ix/du7ceXfuILptIe4idC568OBB2XouHqIF4sLek4sGs/UnHaKr86K1a9eKWwv9sj///DPelpPi3MLNRaFzyjoRrd3NRadOnUqivqL7+eefB2yPIJ47M8+dO6dHuqNHFC5c+CZNl7Zq1er5559Xh3Hiovv370+TJo1a1L1DEToXtWyH8j5cVHxUes6d3QxUr179ZnPRbt26OeZuOnToQBnfeecd98Xi2rFixYqJOeo6PM1InA9HJHcDg9sWp06d6tWrV8mSJbNnz166dOnmzZvPnj3bTKMbGIQFaF+lSpXKlClT5syZu3TpojZwGSQ9hJmLMjSLa6arV68yIou/JonddOXKlb1793JKeXBSSg/6n6RIKKrz58/L4a3awmTgCTcXFdoZERGhTzcE46I+40jHjh31tUQrJmQcWLhwoZ7ucI53/fr1lStXDhs2bMKECTrRRbS+/PJL3b+/Jxfdtm2b7sHCk4uKQ79q1aqpFPGB3rdv32DFcfiye/XVVz2Nk+ksS2Jw8uRJKlYdivuyv//+Ww5V0Q4dOqT8IvJYyRgXUOeWxkWjo6NXrFgxdOhQh+9+hcOHD0sg8kmTJnH72bNn1at37tz5119/qUO1aPzJJ59wqHucp/ao9rfeeov3+uyA/+OPP2bNmgXNoDgLFiwYM2aMEiGyPXLkSBId/IexAsI/YsSIKVOmuFfqEDYandJ98MEHixcvdnBRHiUiAaVxuPcIxkWlISpXrhywozXwX5zsW/Zsy/jx43naxx9/rJcxroVyC6Sbi+qNK6Ddp02bNnz48PXr1+vpPI325S3kdsuWLZ4uK3766acUKVLokyCMrtKnEDb39UD8c9Ka1H885OGbb74ZPXo01aWchUpWZXqRP7QpNSlBGjyBuObLly9cPlcMDAwMDAwMbn+EmYuiuKBqqMUWoaaycQKFSQx3JdyNzkVRPmQpVe2sE8p6py/aJDE4uCjNJ6HAn332Wf0yTy6KZuy4TOHixYtp0qQZMmSII11CaQfskNCeLkbR1GvUqAHx48/LL7+M5i10FxpQqFAhxwKLJxeFA+sWjG4uGhUVVaxYMX0pSYXncvi+94Gso7pjyl+7dq158+ZiAExlQgAGDBggWyOUH1eoSOnSpS9duoRCL+HaqHPL9o1BwTl89NFHoWSyxU64aP/+/Uls0aKF5Nwzn9DIOnXqcJbnczvFnDx5MoeVKlWShcHPPvtMqkJFKoeVpU6dWrok2aM1qXM6OM3Ni6pWrepp7gthE9NuslG/fv3OnTvDgbNmzYo8dOvWrU2bNg0bNuSs3vrHjh2rWLEiN/7yyy9Lly7NkCHDCy+8QOXIWRIfeeQRcssfmvu+++7TuaisnENQIX5UV44cOfRdW8G4KDmnEoSLIjz8F6mADBcvXpwynjhxgj/KhjyuhfIUSJ2LOhpXMHfuXGqYUXH69OmIHI9Vp7hs8ODBiCLjbaZMmTyjyUuMe32Z94svvuAVPCrYyqcEW4dXW7Yrr9DlAfTo0WPcuHGbNm3iDz1RNn4fPnxYykVByDNNw7DAoee0FPVMu4foddPAwMDAwMAgaSDMXFR4JmqiHP72229CMnXtR5inY12UK9V0OOlQVi4INn9vcEsgXHTdunW7d++eP3++BByH8+gGulYMF82YMeN/Y1CvXj009caNG3s+VjxAuCnTP//806hRI6GjOXPmhJboZ69fv16tWjX0dTn89ddfU6ZMCQeTQzGsdXPRKlWqSJbgFeXLlyfFzUVz5cp19OjR7du3jx07tnDhwvDkN954Q12D8i1ZkqXIUADV4fqBAwe6Tx04cIBTUGI5jI6OhnrpobfffPNNVUaxiFZ05ffffw/YgbzUxcJF4Q/0JssmZmnTpkW/98yV+IJSXAJinDt3bsqrLoDnw3PUmht0V9Ghrl27li1bVl1JP4XhUMOeL+JiXgSvk0PoSsCOzKa4Kxnm1fL/33//LVOmTK9evdTt77//vu4ghFzB99RZCZKuuGjbtm0VzyFXDuNqfxtd2DUXqFkAxC8iIkJV79ChQzkLX4pHoSwvgXSsizoaFwmsUKGCGiHbtWvHWXGyJeUSYxPJmOecHRkoWLCgniLR4YsWLRqsBpo2baokKk7yQOdVjUKeId70GlmUhi0H7HiM4oTs3Llz9NNatWrp72XkR85leLnvvvsoe7AcGhgYGBgYGCQxhJmLCskUVdiyNQ9J0XdQuLmoA2gtwmATbe+WQSgQZfGZZ56RBbeqVauePXvWfZlw0fz582+LAa354osvBuOiEyZM4PrPPvvM8+yyZcsgomqBVNlJko5Sq8sVTEyZVn788ceeXBRWKVnasmULJOc///mPm4uiRrdu3VoWvnr27OlwSPDdd99JZpDPkGrNXvgNBHcEB1fMnDmzEvW6desmT55czeZAAFQGZDddrFxU3y9aunRpqLXnex1c1Iox+lVW0KNHj+ZQeXaFH0pIEjgGOXQ4mGnWrBkXe0ZGFrr4zTffyCFjgmMtXRxBSQ3wOv7rlqWw0zx58qROnfrKlSvi24bmU2f1/aIyTTBmzJh3YiCRwZWUxomLWvbSInIi/ydNmsRZtcoap0JZXgLp4KKOxqVZuUAVRKKEd+nSxbIdv8kckDwcauoZqxqhcjgVGzx4sNDCYDUgeX766aflMER5AHT2jh07qtzyXq6UcOTSKHp8i8jISJ3iStnpuTxZ7MYd5voGBgYGBgYGSRjh5KJwS8c+T7XzM0QuSgqalhBRRWgNbhMoG92ffvopa9as/PcMBuhpowujaNeunedj0fj9lxlRtVu1aiUMEP1YEnv37o1SG+yWYFzUYaOLeh3MRleMEjNlyuRwr0JB4MCcCjHSqSAiIqJKlSqep8R9q9QkJUVN53DcuHEc7tq1q3PnzurKeHDRChUq6EEsdbi5qNBs9Ua4EK0szAQeqHbMyjq2WHIqyITCxIkT3S9y0DbInoO2tW/fnhRZRuvfv79+saBBgwYkQleETSmibt3IRT/55BP+r1+//n83QrmYiisXFezdu/f111+vW7euLqVxKpQVdy764IMPtm7d2lGQ/fv3y1mxF0D+V65c6VkWpJQLHCvVsrc2bdq0wSYBIYFc0KFDBzkMUR6ioqK4bPz48Y7cilWLm4syMsA5PTPAp6FMmTJKLOG6H2jQ293AwMDAwMAgaSDM66LipkJpYKjLHDp2ygXjopcvX0b5Fle6jnCOBrcD9P2iq1at4j/KtNKPFYL5LvLc1WbZu/ICtscUPREF13GZcCdInZgE169fP2PGjMGyGiIXRcz0tXfHftE+ffqI4aWDnxQvXpz00CO1IOfJkydX9sMO8PD06dNDdfg/fPjwRYsWlS5dGo3csj270iP03N5ULgogGFmyZKEn0gc7duz48ssvU+G8iHoTegwWLlzIjboZLVi+fDmJ5N/9ohBpmzANcfT66aef6k8Qg1iyJNtrlaGsdSMXhQ7xP5iYWXHnomfPnm3atCmPhdrJ/sm4clFFn+LKRZHtTp06BcsqVLBbt24yO9OyZUtP30UpU6Z0+MGHVMstur8uHbly5eKs7nkrFHnYvXs3d0F0PZ8ZJy4KkH9pa/43bNgwlYbPP/882F0GBgYGBgYGdyjCzEV37NgBmVTKooRvccQu9+SiFy9eFB6LZqP8lBjcVnD4LurXr1/A3t/lcCzkE9PFskmLI2X27Nm67Z+gcePGDs/4SEXq1Km5EpXaionAoa9qWjYlECPeELmo4ODBg4cOHbJcXJQMVKlShRQyo8vqW2+95W/r6IDQjGCumyx7NyBk9ccff4Q68lJZY9y2bRt0xf2cm8pF58+fL9aVFPnIkSPCXiZNmlSnTh1l7AABI7FevXr6jbLmRrW7XxQn2jZmzBj+60FTLTuGOIkU/8UXXwzcaB2tc9EFCxYEXI6XLXvvpfyJExdlmEIS+vfvL4eJzEXpVoUKFXLk8MSJE4gHzPDq1auWPdjKKqLb7xfImzdv8eLF9RRkGHkIxOw7dUBMf+HAuhvbUOSB0V5fTVWQao8rF92yZQvXe1odGxgYGBgYGCQ9hJmLon/AJ/fs2SO6+759+zhE19evcXNR/giJ3b59u2haAuVW1+B2gNjlKi5K61SrVo0UFFM93IUPF/3yyy91d6CCw4cPc/2UKVP0xCZNmjhSQJ48eVKkSPHPP/9YdtwUoRaKsiIwAwYMiCsXRfZgBULJ9u/fH7jRj+7p06clmrnyUmPZC/gFChQgcdasWZ4VBW/RiTQUQowYPS+2YvTvcuXKCY1Ey4+IiIiMjJw6dap+mYOunD9/PnCj59U4cdHu3bsHbozQY9kOe7j+wQcfbNSokaTAdgoWLKizLIoPz0mVKpW+dg0dypYtm6c5Q5xo27fffgstd/hbooFq1KjBn+nTp3Ml16tTwkVnz55txUwlUG86k6GN1LbGOHFReRdkTA5l0TXRuCjcz9GU1HaPHj34w+i6YsUKSYyOjqajVa1a1bM42bNndyTu3LkzWbJkUpkO9OzZMxBjHK4QijzQg+gjyIMeb4mRXzIfVy5Ke93lYc0h/FSCTDckzuu++OKLBD7kr7/+WrZsmacnbYUrV66sXLmS0T6B77pTQAuuX79e39xu2bWtOu8tx6lTpxYsWHCrcxES+Ky/9957jr0b8UYid7FbiJtU0jtIcgzuFISZi/JN2rBhA6xylw3hnA57SzcXVdtKHfj+++/Dmz2DeOPSpUvwwIDmy8SyqVqOHDkcBqsffvhhwBWlE+L62WefwWY9h7AiRYo899xzesqrr76aMmVK3YfNunXrdNNQhlfZWokijoo/YcIE/qi8iR3ppEmT1O0lS5Z0kAHLXrdv1arVfffdp78iffr0OpMkD8ls6KtJ8IGiRYuSw+HDh+sWktBOWLRjjVc8wfp7B+VpWbJkUUSoYcOGadKkcXQc8cerWAHdJ3Xq1MWKFaPTSZDJTz/91EGbixcvzjWeb3zzzTelQiTYkkqXtUeVMnHiRA4dcUo/+ugjEgcNGiSHZBt+IoTQDdkCqh4obn6UgxzQunVrUlRnh3EFbHfNcrh//35aREJWIoTQYNoCokgbXbhw4YknnuBi6vzIkSNcUK9evYDtO3fatGk0HHyb4shzoFWcql27tmcmLdtrlG7i+8477wTskDknT55Eh37sscc4nDt3rrworoVyC+TDDz+M/KhDR+PK4jO0/OWXX161ahXvfeSRR2RSD9mrX7++upEa4Bp3cZYuXRrQ3O0q0FOowH79+ulCTn3Su/XNyQqhyIN46M2ZM+cbb7zxf/7P/xkzZkzNmjUvXrzIKarLsWr6Hxvyf+PGjdSk4jAQ8oceeuguD+tSokSJYGvX4QVDsQyh+nxWXPHVV181btxYPg0O3qXw+++/d+rUSaLXOsbGJIkff/yRkYdRi/KOHDnSsr9WdA3GLlJ0N+m3CrQUI5v7M33bAlZPbqnAsDwt0brYLUfYS3rHSY7BnYIwc1HL/vCgYQiZhJe6HU64uaiEITVc9LYF2vBTTz0VsFGqVCndhBLOgGpLeoMGDb799ls+vZGRkXIlo1X58uXRoWFE4pY2EGQ737x58/Lly6fbwc6aNauqjWeffXbIkCHt2rXLkCEDBFWf4UNsZGE2YJsK87mSdLTwsmXLBuytnvBACGrbtm3lMrR/SClZQuWV0JQB2z2vZUfdkIEboOvrIRDFu1JERAQahgpgA7fp2bNnxowZIdiMzs2aNatSpYoiRTrat2+vsxRPvP3223rQF8iPYwF506ZNsnDHG6ETouhDQkjJkSPH/Pnzd+zYQXVxCC1cvnw5PG3YsGFSHPKp/PcowFKkUdCN9Kg8UB19YYreSjW6vd3ARgoVKvTcc89BPGh62KlnuZYsWSJryFQp/ApCLguGadOmnTx5cnR0NGRYVp5btmwphJN3IWDc1bt3bxQ4qk7SBceOHaPtAvZe5UqVKlFvFJ92IduWTWagcyKQkHkaTmwrvv76a3F/xV3c4jABhW2OGjWK67mgYcOG4keKOpH5C26B3n/33XepUqVCBtDg41ooh0Ait6+//jo8U5rm0KFDno1LlcpDAMRV7RympBSZN3788ccUkI7pblzLnv2BaXhOEEjw1aJFi1JvVHKFChVg757m6yHKw/Xr1wcPHiwm9KB58+bieQ4Zk3JREOguNfPaa6/JNQgnPUgsn6l5+iCnhg4d6r+2liThMP9BeJo2bapMoG8qxLokIVzUsjusjPnBuKigRo0atwMXTTRjKwZwxUUFc+fOvbVcVC87ytUdxCiioqIYSfS5vIQgWBe7rQzxwpKZcA0md67kGNwpCD8XtWzVBKUQhc+x5c/AwBMIzGOPPabzGUZP0bAZBPfv3w+fdDs4FZw/f94zvmLiAG6Msr527VqogiclQCln1I51qefSpUt6AamQEL8fqPuermtCARnW/QApOF7tGblHnQrmCCfh4JvnCF2rQK3Ke7nAPcjA5Y4cOZJwwyRkD+qrnsOAlvg+1agER/2TK8SDUiNU/q5l169fD8kM5jVXtuaC6tWr+w/UIcoDD6Hag/XTYKBWN27cePjw4bvzY7Fs2bJbuD4jpuMJ5KJWzA4Ify76/PPP33Iu+t13373++uuJ86433njDwUVl98qt4qIOSZNNAYZRKNzanuhGly5dgn3+EhmOXmMkx+Bm4KZwUQODuOLnn3+uVatWvGnVbYv27dsHczFqYHCzMWjQILczJwW1Stm6dWvjMS7xceDAgfTp03t6/Eoc3FVc9OLFiyVKlPA0aL8ZuK24qFvSDKPQcct7ogOyhH47hJNw9xojOXcEfvnll507d27cuJFf3dro//7f/7tnz55dN0JZin333XeOUz/99FPiZNhwUYPbBXwPOnXqJK6JkgbGjBnDR+VW58Lgrka/fv0cAZN0rFixolSpUgHbddbatWuDLaIahB2HDx/Onz8/NT9q1ChYnO5F7Ntvv3X7+EEFXL9+/TvvvLN69Wq30QQqo9C8a9euoX/MnDnT4TLQEzoX/e2335YvXz5v3jxPSwe0mU8++WTGjBmbN2+Ojo52nA3GRblryZIlCxYsOHv2rCcX3bJly5w5c9asWfPrr7/GGlE8lDIiwHJq0aJFemhoak/2lj/77LPkEx2LlG0xENuHU6dOqRQ91hdnJZAvmaQG1JaBYO8SxMpFuWWbBsnD5cuXVYp/bYQOT0nTGQUNum7dOgrijtAGUEaXLVtGMzm81gfDlStXPvvsMxESGmj27Nlff/21GlhOnjxJddGObik6c+YML5o2bRqZcZ9FMXC7faK6duzYMWvWLETXc0sXAobscRlCqLuf0LuYu35oaL1plGvx3bt3S0qwFUsqUN0lzvktW2wkRa9An5zTK1OlShWwA91xl26HQqutWrVq+vTpdMMQDUncgwkdjfqnFfbu3eu/J8Lda6y4SE48cuszIPCETZs20QE///zz22TF+LYFzSr7HKkx+fPjjz/KKUY293ZIFYZz69atjlOJ5m3OcFGD2wgMuwl36nibgD4s4WcMDG4t0PB8pnhQE9FXpkyZ0qNHj169ejkC6hjcJEydOrV06dKi5w0ZMgTt8Ny5cyNGjJBd6w4va1DQUqVKoT6ipbVt2xZV9c0335RNXEeOHGnZsmWaNGmSJ09+/Pjxhx566IEHHkhhI9gubgXFRcePH581a9b777+fwyxZsuhKM+pm165da9euDR9DkKpVq5Y7d26HNaObi5K3V155pWrVquQBffTpp58mVzoXRbN86qmnXn75ZcZJ2DWqLSUKls8Qy8hlpPft25f8Q2kiIiKUX2jy8Mwzz5CBChUqUNtjxoxBJ5OoyIEYf9coZBRQ9o2LBrZnz57OnTvfc8896dKlg1bJ/u08efL4v0sQKxelIJUrV5YHbt++XVqTaqFuSUTn9m+70OGWNEtjFF9++SUNWqxYMYqQLFky5TncshuxX79+nTp1ooAS+bl169Y+I8kPP/zAxZkzZ+bKffv2NWvWDKEVj03cGBUV1aRJk+LFi/MuaQh9F+KAAQOoT9gXvKVGjRr0ArV/hMQWLVqkT58esddft2HDBi6j2tGYhw0bxtlWrVrJCg8NOnjwYBE5zkosKwArdncxd/2cP3+edpdbxPmCXAnjorE6duwoW/rd4ALxB0YxlbdCqCy1ly1bNuWG3Sfnf//999ChQzNlysRDqHzyo7wHQ6ebNm06efLkQYMGZciQoXz58opguBFsMGEAKVmyJH0Zyt2lSxfdf54b7l5jhSY5cc2tFduAQMOREzJApd133325cuVS/kEMHLh+/boEyDx58qRl9wX+b9y4UaYDxF8Plfy7BjFIpD9yaufOnfqpuG66iTcMFzUwMDAwMEhsyFKhsgyEHUGHJKaxrj5CFNFWdVsp8TWNqiqHaPniOArCJosJEt4JNdE/A8JFUewUs0UPJkX3al6/fn2UV0UboCKVKlXiGn3S0M1F4SRFihRRq4sQWuEkiovOnTsXgqcswyFgkAefrIZSRsmY2uhRvXp1yKpaVnrvvfc467DRRZkOaLGXQLly5RQXRe2Wt1D/0E4uQ7+HY8f6Lis0G10J2JsxY0Z9GXbdunWOyNIJh0PSrBhGkTZtWliirDKhrQZu9FU7fPjwPn36qEPxQ+bfTDSoOAVs3ry5kEkERlxbwTDVOjY0lZRPP/1UDiFIHKpgzijEHHbv3l0OZUu5tIJ6EQwtefLk4mdOsGLFCq6hXdDFkTeIcc6cOQN2eHBo/+LFi3kpkuPZxdz1Q8uKbGzdulUlQkpz5Mjh6RhCAf4WsEOL6YnUpGJW/jmXFFmn1W10N23axAVqeVncvFerVi1YNoINJgUKFFCe9nka0u5vC+PuNaFITlxza/kOCNCn+++/X3XSQ4cO8bTMmTObMNSeoFrEcayIE63AyEOKjE4QVP57GqEg2Jxym3gkDgwXNTAwMDAwSGy4NWArhmcq9fHMmTOoaCrYjwB1ME2aNJAfZQf4n//8h7t0LTlLlizJkiXz3wYsXLRp06Yq5ccffySldOnScihhohz+S1evXk1ivnz5lN2dg4vu2bOHV0+ePFm/q0WLFjoXHThwIIforHII1505c6ZPVkMpY+3atYsWLapy9cILLwS0cESeXFSIk85FZQ1NWaahz0lML4fi6/8uK+T9ohJKavr06Sqlbdu2jiWmhCMYF4Wt6VRE3IMLBfruu+8iIiL27dt3LQYSmOree+/1fxdEmsvEsblA1lSnTZumUmhrUoYMGSKHaMAI+bx58+SQ5uBsrVq11PVkkszoXLRs2bLZsmVz8KiKFStyoxIkiT7itux1dDHP+gGjR48WUq1SyGG7du38i2/ZQZi5EYamUuhQytA3lJw7uKi4qqYbqraA58uyrb9bREdJr169KhKo5HbOnDn+TjqCcVEfyYlfbn0GhDZt2jRu3PiaBrHgCBbg/S6HxCXRZwa//vprUsTH55EjR/h/9OjR7du3b9269eDBg0oAfv31V059++23O3fuZCjbu3evI6zgTYXhogYGBgYGBokNTw34lVde0dVHiROrL08JGjZsSPqUKVPkUHiabk8l6qy/O2637yKeoPMNiS67atUq/S50zaxZs5Kudk46uGi3bt043Lx5s7uwiotKMOe0adOOGDEiRJd1oZRRlgL4/eKLL4QSwJzlVPy4KEiePDlMyZ0fn3dZIXNRSSxUqJA8TUIoh91pQjAu6vBAI2vCQhhmz57Nf6jyUzeiXr16/mZ7bi4qIv3OO++olCVLlpCigj9bWtSQM2fOwFE5Cz3TH5vKhvxHaeaC8uXLO14t0Y+bNGkihyKWysbVkZ9YueiFCxeyZMlC66sozbVr13ZItSdE0lq0aCGHkFLVxULMuYOLkoGAbSj7lAv++4rdJZWV0sqVK+/evTvWgljBuaiP5MQvtz4DAj2CDuJ+WqyzV3cn4JxQSvinSoFbkiIbxWl3x1ZSRFo2q3///feSgsRu2LBB/ieaAy3DRQ0MDAwMDBIboXBR8XXcpUsXx729evUivXPnznIYXi6qFE3RXJctW+a4UeLlKjtDBxeVUKKOSMtu30XDhw+X1ZLIyEhxDuSPUMoYHR09bty4F154Yc2aNZ06dQpotsRh56I+77Li4kdXr2R+Jd61ZXudeSbBEHPrOHFR0VllSS0eoSlD56Lt27fXb0R7puyjRo0S02UaQj+rc1HhLW4TdFnGL1q0qBwmkItaN/Y+hCRWo3cBVCp79uwpU6aU2qMJ1E7REHPu4KJixBsPH9TukkJUZFExWbJkHTp0iJVpxImLiuTEO7eeA0JUVBQpL730UrC7hgwZ8sCNUJ547k64ueiuXbsUF6Vz0SPOnDlj2d7gxHxXZlv45dSxY8ckaJwwWBXY/GbDcFEDAwMDA4PERihc9K233uKwXr16jnslfejQoXJ4k7honTp1OHS7s5J0ZYXo4KLinAY9xl1Yh4a6adMmca8SiG0jYihl3Lp1a6FChZS9q9jN3iQu6v8uKy5cVHYYos3zH/a4Y8cOST916tTbCYbkMB5ctG3btoEbd0uGiHhw0StXrnTv3v3BBx8UFiE2uj5cdPv27VyQIUMGx6sl/bHHHpPDhHNRRCtt2rRp0qT57bffqEx4coiV0L9/fx44evRoqNTDDz/syGGsOXdw0Xnz5nHo49wrGNwltew5lN69e0dERARsS3v/8Ozx4KLxzq3lNSD89NNP/K9du3awWxYtWvTCjbgdYuHcQogTXbeNrmd0FjHZ9fSyKSa7DPKJ413fcFEDAwMDA4PERihc9PPPPw/Y7oV0p6NWzLqo2gt3k7ho3759A5rpoIKsiyqdz8FFn376aQ7Hjx/vLqziomq6nXJNmDAhRYoUUD61p84T/mXkN2vWrFWqVFFnbx4XjfVdVhzji4of12XLllGxPjUQb8SDi8oiVdeuXR2Poo304ChuxIOLDho0iMN169bJYaxc9OLFi0JXlJW4QFYXe/ToIYcJ56IAksyp1157rWLFirqc+OPUqVOIdKFChabYUOkh5tzBRTdv3sxhqVKllHMjASSBmvTJhqOkV69eVcFXaGVIsv5ST8SDi8Yvt8EGBB5Cu8Oc3ZW/dOlSE4TMjbNnz4oJrkrZsmULKVQg1SUbbtUpmoxTYrAtp1SVMsrpPpBuNgwXNYgzTP9PCBKh9pJkAzFKHj9+POGBxaKjo0OMdQYSLY6ZCZh2F6Jjx44obYsXL9YTHerj5cuXJUqEY9Nm1apVixUrJvt8rJvGRQ8dOpQyZUp0wfPnz6trkFW4WYcOHVSKg4uOHTs2YO+B1D0nNW/ePKCZ9fbu3VuPbShsRHf34oZ/GT/88EP+6/ywZcuWer0tWrSIQ2UBK5Dgumr1D60rX758pCinUJYXF431XVYcuag8MH369A4CHy64JS1WRkGdBGxLTp2hUfmNGjXy918aDy5asmRJnYseO3Ys4NpUqXNR0KpVq4BrHzVSlDp1auUgJ3Qu6tkTBUgpz6Rp6tev71NqN5o0aRKwt147xvZQci5dXgwp/x977x5vU7X//y8hlFsuoSjXXDsRQimKU0pCSEKopCu6OFR4EBVKF3eFEEISuRxO6iBEkUvlkpIKoTg4+MSp1vf5m6/fHo9hzrXmnnvvtbeN+fpjP/Yca8wxx+U9xni/xniP94g61a4T2t27d7ff6tGjxyeffOKTB1dJSYeSml95zJUrl9mMjQlvr0lWclKXW58B4e9//3vE8TNsu5ueO3fu888/75PzcxaMuvZRT3nHBWg+NI3+l0wy3K1Zs8b4zpW9rtk+3bJli8vWN10RctEQQbFx48a7776b8YUphFHemGB9/fXXzzzzTIMGDW5Kwq233tqxY8d+/fq5jgz5gC7BeKfXGzZsyLsx1yCZ2hs1aqRo7du3ZwpPURHWrVvH6KzXzY0IXsybN09xmE6mTJnijfDHH38wMganNAKjZ7Vq1dDtihYt2qdPH9dGR0x8+OGHV111lf92gUHaG4gcMvcELxFKp5Ll76BBg9CbP/roI+ZafQX97J133lFMZhGmogYOjGFhQDA4ovi+9tprDz74YNasWR977LEUvW4wbty4Zs2aMfv6WyVFnfYdPnw4U2DBggVT962AyLAPhciE0NYT/QVKSU/RpYUdOnSInGoWiwKHFs44YFzIorXDjswhtL/++ksXEpoxEyUjT548hOiKuXiQNR2jgQmRH11SM+tZL774YuTUo33PPfdcyZIlbUJSvXp14pgb/+jsRBDvQqGhdAzUSDghjN7aPGQctlXVUaNGXXzxxfGubQxSRl0EEnEuhPzmm29eeOEFMRyUWn1R2zXlypWjGqk6RstoEglhUIJ8ovhS+fJChJqrDzGmiZLZenCy34o6urVCzFvz588npG7dujELyNSQLVu2mHctpB1eSZPpIxTL3vSQN1Tj1UZ3S8KRWrVqBZOkmFdccYXXLa0LoiVGOKNJHrDMVSLRJMdId955px5FX5n3t23bBp+XeTACQxuZzLi4KBUFHUIkzF24u3fvRoTsW151787ixYtdOfR2sZg90QBBjcTyx+sP3XRiL9kEzzkCGXHumIU/vP3224Qw/UnkmFjJ+bBhwxAkr0sz/5JCRXLnzm0ubqXpUUV0a2g8eHtNEMlJRW59BoS1a9eed955EefW1mefffbNN9+85557brzxxoS7+DprsGnTJsYo2gsZE8OUFS6jqMjn8uXL+Wn16tWywlVNyl536dKlRNYRU5Bhh29DLhoiEBDTAgUKmNXilStX5syZ07Yyl9/2xo0b62Ir9CeNp/4WIDagdlqT9j84JHfwDIX+13z5oEmTJqTA6BaPk5irsWOa0UeTlrGnT58e/KMQIaZeJlqmtDp16vC6/+GTVatWMTTrUEcQBxKJaiBm4jfeeCN4ueTiAh3FhKDO6iZAFDVXZAoeXB4E5unLLrvM3BuOhsf0maIUDCi1LpdPlotGnVIUKVIEjSF13wqODPtQiMwGSBRNL7UbDvPdd99BgVAWI845rtdff90oW+gNKNaVK1dmbHz88cfheGYVCfmRgSho3rw54wYhnTp1Ugh0wt6hsjFjxowKFSoQJ3v27NBLWWRpC0Lk02xTzJ49G26JWgkvbd++/b333mu2elBZNAJEHKNKOIbC6bZQC4XnypVrwIABvEUivXr1kgpORy5dujSD0nvvvde3b186JopRvIoKWEZdGwOoqM8++wylSiqs7g5BD5OXIPJjlsP27NlTtWpVvUUNf/vtt4zSZcqU6dGjByTzo48+0p0r4LbbbjOXjvh/S9eQamuIwQqO8dtvv40YMUIH4YiGPu0y0QQ0veFmCYdL0siwKVe7du0gGNu3b3/44YcVAjNUWyB+cHXEQ+HwbSrE5yvff/898qnIUAW4N1wCKqKqgIANHz5cZE8nihH1l1566cCBA8xWTF6EMGc98cQT8H9tadIQ5rZDFxeNOvcotmnTpnjx4vSIZ555hlfMvjTzxSOPPJIlS5aI4yiIGU23U8TrYq76cZULxR1elNKl56iz6x5ThfDJucCjpn7YF6KuQERIiy+gcOHCtumvFzFLqh3LatWq8e6UKVNQhB577DF/C0xXrwkoOSnNbTS5AYH+peWtiHPNLGNOqtW/cwF//PEHgvfvJDBKGwsauqSOjwqMpWZVkbcYnM1PcFT/pczEIvFc9MSJEwziKx0w4NqriQb0E2rHtiSkPxAIZUfmEHcGtSC7RiEyDIxZ5tI5oWzZsj179jSPMCuGCRQOE4L06xjMvHnzAn6lfv36xPffmtNyI19PSfZPwdNPP82cF48n01HN6fljx47FTEEsDmYV8IukY2/DMi8ySfi/Lrfm8hEShIsmsIGYY4I3GXmDeaJg2Sv68irpOpoFmE6Mf/yAgJC7KsqMqqmANNp4XJTxyt5pZzpMNUVEKbctjtLvQ0EgjTD90k8PuKrobAXaISUNeCCHdkT5O127AXRwspqieRnKumnTJlnqutbXVQpGuS1btsAcEnUkaceOHbaLDmih/V3oBMqWqwL5NBkwbwX3HOv/rZQCRu1lQQlEiiTNBs2H1AU/Kpk6SLbNZR7kc/PmzTb9g4FACL0vEodyBTQd8oFP/bz22ms+VlQ+2L17t8+v/jnft2+f9zZOdGZklfDU9Rdel0JO4l9++WXA2yNj9pqAnwue2yADwp49e8hJwCugQtDWjGb0LNehLR5h8oznjM/eekZZ5aeDBw+mRdFKBRLMRZFamKT2eeEM8uZkiw61gDyJdtsVtH79egVqQxlAaBObtxBpQePGjfPnz2+4GRoJjz169DARXn75ZRfVAXAhAoOP41oN9T+Or1M39kZcSkF+xEkghN7h+J577nnrrbfERWOupDBQ1q1bV2Zpa9euDfJFZN5l9gMJtI9pxcOdd94ZkIsmsIG2b9/OrB9cr9IWARO2CVm3bh0hBQoUsA+Mffvtt/YJq4CoWLFio0aNUvpWPPhwUXSR8uXLyyBKSDVFRP/OmTNnPMabwA8FRNu2bV3tnsnhraIQIc5iMFZUrlz5rDznnyhky5bNdkibYUBZr1ChQkZuEIUIcQ4iwVz0559/1rYvlBpeqr1g7YSglW7YsIGfzBawGXl1uBb6yj8EmhtXU2EUESKdIE8MnTp1UqvNmTMHbds+bRiT6sgHnX1QxB8J5KK///476fTr12/EiBGu9UWo1zvvvCMncq7DEr/88kupUqV0Oj8eF+3atevUqVN14qV9+/YBi2aD9OEeQW7NDs5FE9tAtWrVCm5MKx+A9q4sXEImRvbWVp8+fcaOHWsed+7cOWrUqIEDB5pjZi4wDtCCuXLlqlq16rtJIIXnn3/eblAorgTmyy+/fOmll2hZ11IftTdlyhTeWrlyZTwuevjwYVkndunShdRkEmwo4ubNm19//XXItqsh9u/fP2bMmL59+06cONH4PNyyZYtcqgwbNoykXP7lU/ch2nT+/PkU4a233vJZIzh69Oi4ceMGDRo0e/Zs45ZQyw3XX389n9MhLupn4cKFVO+uXbteffVVY0XGEE04wkCXcRl20ptmzZpFtdOy1DBxjNW0ASGkNnjwYBrUu6T6xRdfDBkyhAgu68Qff/yR8lLqJUuWyHlpzCoKEeLsgzxYIvC33HLLhAkTTnd2Mh0OHDignQxUwRQtaqcdX331FRopwx3De+pm+RAhQgRHgrmobkc1qp6oqe7LYkyR4a7Z+TRcFJVu+fLlRnkyfp/CvfjMg2PHjsknQbNmzSAYFSpUcFEpL9VBs8yfP/9FF13kb6liI1FcFMErXbr08OHDyTbqb548eWxvYOKi06dPJ53ixYvbSx5MPPAZOZOMyUVJsGzZsmjtx48fp3Tnn3/+vn37ApZOIM0WLVp4z1LGRHAumtgG6tGjByQwJhX3AuKh0z6GwEDU5fTSvheRLBlvnJA3KD2TPVyOOuzQoYM3WXHRLFmywHJFRFHXdLhL7vUOHTqkkypwuf79+99+++0wLpdt8GeffVa5cuV//vOfUDh4b6FChWJyUViWXA4+8sgj7733nvwBiiJCKUm2devWWbNmLVeunJGWjz76iKpbtWoVhWrTpk358uVFO/miLKth2iTl2nhPxYdItlWrVtOmTdMR38KFC5sbCG0gtNQwJf3jjz+of1KIOryOSuNz9erV43Pk9u233xZVhrVKYOTYE0pfq1YtAn/55Re6Ru7cueHt2tZevHixzuqMHDkSlkhhKTgR7L2CqVOnktrOnTupFrpb9uzZq1SpQkz92q1bt6FDhzLI8w+le/PNNxUODaYj82mG+vvuu0/eGmNWUYgQZxlgoZEk1K9fP9wUdYEZ7YILLpDrviVLljDFZJgblT///DNfvnxqGqaMdHIoFSJECIMEc1HxTHO0gD6sDU97nGVk8droGhCILqLjtonNW4g0goarUaNGxHEq6PVhIKqDBowKe//996OzwjFQLmNesBsPieKizz33nKEcqLk5c+a0/UCKi6KySyk3ntzhVKVKlTpw4IAPF33rrbfM6qzc6wV3LE76kyZNMm4bgvjlC85FowltoClTphDZ31OFDdcBUTgVxClbtmwQD40GEOOmTZvq123btl1zzTWm+8sHydy5c2OmfN5559m3IMA5I6c6aaQmIXLGaXD16tVz5MihrVF4IKzJ3puVw8aY1rPQHn5ymc5SBBPyzDPPEGHRokV6vO6665Af/a8zzMZpMCTK51RqSj/UsWNHUwToHz9ByL3JTp48uXjx4uaRt/QPwuNag5Dcwv+ppVUO6AvofE888YSJM2PGDFu2dUvHXXfdpR4xb948ezsdNk4rmMd+/frxq1kKQeaN62MavUyZMvRHqZU0fbt27fTT0aNHzWWG3ioKEeIsA52uTZs2l156afv27cMrnWKCkbBy5coM6W3btk2RIpF2DBo06PLLL7/xxhuD3wUQIkSIVCPBXFQk0ywjodZ7rW19uOi+ffvQYPhp5cqVGXxwNkSyOH78eOvWraXNQ2NcjFFUp1GjRkuXLkVVfemll5hFRAIDHpGPJo6Lrl27FsZoBKxAgQL2mUNxUf4ZOnQoSTHVKRwCBk+LJl2yF5OLEnnHjh36X9egFStWLKCsEu2rr75asmSJXDTBoJLdU00RF01gA+n6AfsIqD9IM+I4IaSM33//PcQmmuSvWFbQXbp0mTlzpiLDi8jk6CTouOnDDz8cM2UXF5Upss1FIYSVKlUyj2K22unt06dPrly5bG8rPudFY1JE+xinLmMcM2aMHmWnrf83bdoUsRwjp4KLxvsQiagOTXXJNaJXcsaNG0e48YFsLG+9XFSSYLiuyZJ9hT2VhmDD6rU1qhvPiaZfRYnNVXW8GLFusfviiy9s4aGBiGnyr81YCQMqZp48ecyt3CbPIRcNESJEiBAhzhEkkoui+otkGtX54MGDKeKi/CQrX7Bx48bQaiXz4OjRo7Vr15a6OWLECG152Sf9vCagELlmzZpFTr2/zh+J9V0EN0NBFyEhZRNuuOiRI0fkdlw2n7Vq1dKdKPG46GeffVauXLn3LJQqVSpy6h3ZyLwdIeZhSBR9XaGWrLYdk4vCVexPiGsltoF0q9hzzz3nnz0Dumrx4sV5hbxR4UOGDIkm3XxTsWJF+AyExFRm1apV27dv/+9TAZ2LmXJKuajNNq+//nqXnKSFi/7zn//08vNffvmFwspUmLwpMI1c1P7Q3LlzI87Nja7q8nq0P3z4sC55q1+/vrnaJxqfi5qdZNCrV6+I51L4pk2bEqhrGF1clFLbaX799dc8mm1VXUCni3kPHTrE/6+++qor/7LvXbNmDXQ3S5YsnTt3tu+rDLloiBAhQoQIcY4gwfui2tU0Zv26skyKvoG/jW7UOR+lCOZ0WYjTju7du+fLl8802fz589EgzY5iNI5rHPFGEPDQVwK56NSpUxs3biwDmwIFCsTkolHnhuWIc0Pd6tWrDeeJx0XbtWvXqVOnZy1oTw8Sa+KsW7fufAvxLm7ZvXs3Lw4cONC/FDG5KMWxPyEPvYltIO1z9uvXzz97NnS3e5MmTeDnuk0bCqpzpFAdc3QQwP91MjAI0sJFixQpUrp0aTu1BHLRkydPUi4Kwnj11VdfpRMXhcXx/549e2Im5cKuXbvUg7Jly2ZuTg/CRXX37Icffmin9uijjxpTW38uCmrUqFG4cGHZY0+aNAkZkNmhDsXZizUurFy5kjaKOHfQLVmyJF4VhQgRIkSIECHOSiSYi65ZswYVR5po1LnKQm517TheLorW8tNPP9kXWEEMbB9IIU47rrzyyvr169sh1113HTzBGEDGpDoIgKhOEJ+xUV8uumXLFh0h9uei2o0ZNGjQhRdeaHZafLgogpc1a1ZoG8Ux17vF5KL79u0rWbKk63o9eTAipu0bKSCyZ88+e/Zs/zjBbXQT20AyEx09enSgkjgwrjjq1atnAsXKtF9qAuEeZcqUcb3+/fffx/SbnRYuWr58ebi6fa9MArloo0aN6tSpo0Es/bgogmr2GG14vcuandKpU6fKRZPYZhAuqhDXHaQ6AyyHTMly0UOHDlGKG2+8EX7erVs34w2LuYCYcN2Y+Vee6UR9+vShG15wwQVaWAm5aIgQIUKECHGOIMFcFA0DFWf9+vVS0TZu3Oi9KdTLRffu3Ws7zoUA6DHgbkCIDEDDhg1dHlO6d+9epEgR8xiT6shKM0eOHLA7hfz5558+lyb7cNEmTZrs2rUr6stFv/jiC224kbFSpUqZ8Dx58thctGvXruZsG2jdujUJVqhQwb5kyMtFUZdj+pTXtSht27aNV6iY+O677/Lly2c76It5iXxwLpqoBhJ0Yw300oQEua6aOoxY5wajSUcHL7zwQrsmVSjb2BUmE+8KmbRwUbWsWXcwv+qWKRdmz57tyrwPRdy6dWvEuUFHP4mHGy4qkYhnC5CiD4nlyqWWiTBu3Djv4s6wYcNMnG+//TZLliy9e/eOOkbjpGBfZuvlonyFera396OOnye4pf5PlotOmjTJ/GqDPgUxPv/881evXm0CmRdUOnvjXeddZVXuraIQIUKECBEixFmJBHPRw4cPL126VF5wgSilyzOKl4uePHlSxr3Lly9HK1q5ciX/o26Gd7pkHqBroh2uXbtWj7TdNddcYzvehKdFTr3Dg0YsWLBgxLkKQiHwGWhDzpw5XVvlBlWqVIl4juRB2+644w54jh5Fn+Qmx8SB6kycOLFAgQIzZszg8eKLL444/lF498UXX7zgggvKlSu3e/duZI9fyeTTTz9t3hVfsvcA5ZQImB1+XsyfP7/t3MVg8eLFxMyaNauPHTLpwAzN3in1cPfddyurwrx58yBsFMH1osi5bTIQDwlpIIOHHnqoRIkShn9Clqj/ZF00Pf/887AO142aFStWbNWqlR2iCof8dO3adcGCBZS6Tp06rhUrgS+6NlqfffZZQqhzEwLftndZIV2GB27atAlKRhnFXWlWeU5+4YUXvFWKTEacC2P/+OOPTz75hJBq1apRHFMJ2qwbNGhQ1Nml53/EDFq1Zs0aUdwOHTrIJhyRE5XSRVZp+VDUEdeI4zt31KhRSCBEt0uXLt66ote8+uqr+p/v5smTR3vRSEKOHDloBQZnMsNPyt78+fPt17t160agsZKl6hBIcxfomDFj7O1Zqtfmt3B75B8Be/fddxcuXEht0+/M8C4fvNQVXP2jjz6CCSPV2v9s1qyZ8Zf+2WefkU+tP3qrKESIECFChAhxViLBXDTqmIQtW7ZMbBNe6tX5Yp4XRX9FFzGeLfg/PCya2YByXLx4cf5OnTq1efPm6N9aLIBFPPfcczJVBeXLl//b3/526aWXXnHFFS1atLDvQoRayL2K2VAyWL16tdz5gOzZs8N8SAQFGhqpQFRwor300ktyFxRxHNheeeWV+lYkCWKbb775Jsoxj/CxzZs3P/DAA/xfu3ZtVGE+DT+BDz/11FOGajZt2vTYsWP6H42ft5Ra3bp133nnnS+//LJWrVoiRS5fRMuXL6eMigzdden3BlBE9OyIczC1b9++PXv2dNn0jh071t5Y0ytQJpUCpRwtP1lXXmlvIIPSpUubA4fwAZLNly+fa+/UCxgI33UFDh48ePr06a7A2bNny44U1KxZM+YFTj/99JM2GOFpZIYGgr2r9WkIhgj4DJWpRCggXGvy5Ml58+blsU2bNjt37iQRuG7RokUJueiii6jG++67j+JTsd4rVSkmnFDtSH6oRlX+I488gpwwlJFPbchLBu69914xar7F8FW2bFkexRLhZqrtm2++2XtbQ0o/ROLUKkJLIHLbu3fvmFvor7/+OpXTr18/6haWaO/hw/kjzoFM6uftt99WH6xevfqkSZNMHKQL0shP9Avk8PbbbzdEFG551VVX6RXI8I4dO7SzDcnXQVDKWKdOncip4BVt+8Ox+/TpI/kHrVu3NuYALVu2JNro0aNhuX//+9+Np2W7iuI5tQoRIkSIECFCnAVIPBeNOsoH+tOBAwdiHgDzeQudZt++ffwNYhAYIuOB9g+JWrlypW0xmCKgZS5atKh79+6JzZgXv/76q803fvjhh9Prlvn48eOwPhimIb0uJOR0dNobCMDYq1SpYh+zpEsGXBvy3jVy5MgR79U4Aqwm2VttEgLqVpzQv1pOnjxpb+gFTzbqOGoySxtRp9T2Yxo/FHVaduvWrT5b02ovpGvLli1eAgw9DmhmQqOk9LZDavXBBx+kNhDvJUuWzJkz55133unYseOzzz5r4jAXkH/XcobyzOvk2Za3aKqqKESIECFChAhxxiFduGiIEPEAF+3atav2rEJkQsAbr7vuupgWsyFCxET9+vW9Z7xh4ynyw3xuAr7t42Q4c+Kvv/76rwcpWndOHX788cfRo0d7bzMKgj179kyfPv3VV1/97LPPEp6xhIPeZB+JD2GDFvT6cktX/Pnnn2gsSLhX7NFnjh496g23ofMI9BpzM/k5js2bN4918O23357uvITILAi5aIgMxeTJk1EpTncuQsQGRPTBBx+MaTEbIkRM7N27NxKJ3Hfffbbl8IEDB5588smwp/tg0qRJVatWjQS7KjlTAfV6yJAh1157rYyuCxYsePXVV5csWbJo0aJXXXVVv3795GQu4dBR8Ndffz2lLy5evLhNmzZffvllvXr1vP4IMht0GDt//vyhUUBMXHLJJdTPhg0bMuZzv/zyy/333w9r+u67755//nldQAXKli07YMCA77//nr6gIwwgb968lZJQrlw5XWmWM2dOJfXSSy9NmDAhY7KdaTHAwfLly4sUKXLeeecZDxchznGEXDREiBD/P5YsWRLEZ2+IEDY6dOiAylWoUKGbb775jjvuuOaaa9q3bx/eyJUsNm7cmHAuGvMscXrg0KFD0r+nTp2qkCNHjvTv319ns1NnWOGfeSgl0uW9zcgfDGg5cuSYM2dO1PFV0ahRI+OgK/PALjj/06HgLacxPwGRMcLm+srQoUPbtm3rMulPJ+zevbt+/fr2YZ9FixZJ7O2Nay0fgLlz59qv//XXX++///75559vQl544YUU3ZR2lmH+/PmRpHvCVq1axXyRTutWIc44hFw0RIgQIUKkCRs2bBg2bNiAAQPkvPp0Z+fMgO4xTiAXXb9+/fDhwxOVWrLIlStXxLrpR9C1tHXr1k1paiNHjkwPi4w33niD/Hz11VcJTzlRSKeCpzcOHz6cAX4fMlikbRw/frxy5coLFy60Azdt2iTaaRvcElOBH330kTcdczNW1GGn1atXP2d9gzdr1qxAgQKnOxchMiNCLhoiRIgQIUJkNBLLRf/zn/+UKlXq5ZdfTkhqQSAn5y4u+sEHH0ScK4tTdIL0888/P//887/44otE5zHaqVOnzMxF06/g6Y3mzZvfdttt6fqJjBdpG127dr3llltcgbrwOZJ0hbXwf//3fz5c9KeffrIfFyxYUKxYsXPznghaM+SiGYNffvll7dq1y5Yt46+9+fzXX3+tX79+3akwPh11qpnhSC9mjGtJIeSiIUKECBEiREYjHhdFA5g9e/a4ceNiHoo7fvz4xx9/PGrUqLlz5/K/AlFtdRjyscce++yzzzZv3mzi//HHHygfb7/99syZM7///ntXaigfpHbs2DH0/rfeemvjxo3B8x+Ti7777rs67qhH3dYGVq9erZBt27Yp5Msvv1QI+j3aOW+RScJ9zPZ27tzp2kKEy23ZsiXqXPlLjf373/82P8EBSK1+/foyJOZ/F+WjNqgTPkr9eM1Nv/nmm+3btxM+Y8YMszlGhb///vtRp95IcPz48WZ/jJhk5s033zTlMoCW/+tf/xo9ejTv6gZd/4ITf/78+a7zov7tePLkSUjOkSNH/vzzz5UrV5INWwZ8QLsQed68eeZeaHL4mQVkA6nQ/0qTnHTv3p1sX3vttXbL+sgSNU9dTZ48WY3lQkpFmnr2ein3b00fOYkJJO28886jZlzhKeWi3mveqCX4mO1j3AtakxYh2RMnTixdupSqi9ma+/fvRzLHjBmzfPlyr3/+o0ePzpkzhzp3sRHh22+/5adp06Z5T/UTmV5Mv6ar7t271yefUceZPJ1r7Nixq1at8rn/4uuvv6YR8zqQLJE4n7blKurIiUJs45pUy/Y5C1pQt2MiGPrHuAtFqP7tgVoZyWTQc73ovf0unRBy0RAhQoQIESKjEZOLjhgxom3btiNHjkQFRxvmf6OdR53jahAAND+4Ta1atQoXLoxyFnVU3kaNGpFaw4YN+/bta26O3bp16zXXXNO7d2+0ikGDBuXKlatdu3ZiHb/88stzzz2nC3shePqHBIPn38tFURbFH4z1JqrPO++8o5t4FQJnePHFFwm57LLLTJErVKhAyAMPPEDmly1b5voQyaJw161blzhGiX/jjTfkSAba89BDD11++eV58uSxI0AMSI3qNSmbQ5iHDh2iYlu1akUcmAnp1KxZU1wFxXfYsGG1a9fmrSlTptx2222iGdR8p06dcufOTUFQlG+66abq1avny5ePn1DcoTpVqlShqi+66KIsWbLYdQI1oqQvv/zypk2bnn76aTJpLqn2Fhxd8OGHHy5YsCCB9sayTzuio3ft2pXv8sqaNWtuuOGGcuXKZXMQ775rAfW0ZcuWAwYMoCYrV65M0ytjkMDhw4dTTBIcMmQIdGjDhg083n///eIA8AoqXP57yHb//v19ZIlMIhLUNtR0woQJOXPmJE07G8FF+rfffuNblM7F+nxaM4icxESPHj2I4+VpKeKi1OTtt9/uTbxJkybkwe7XBqj+RgAQKmr4/PPPV+LUsIlGjxg8eDAiMXv27A8++ABpLFq0qN3cUE0kf8aMGXS3nj178rpZ2iC3jz76KDLDIEP2kJNXX33VvDhr1ixqDzFDFG+55Zbrr78+XhWRIGNUjRo1aC8oMe3SrFmzeLeOUfk0ImXhc30d0GsOHDhACuSN/CsawkM7EnLvvfdG0yDb5zKQjRUrVtCC2pCnb/I/Y4vGEzoRj/SOXy3ovjfEVTGZmGhcJId0MsxJWMhFQ4QIESJEiIyGl4suWLCgcePG5hGKQoTnn39ej2jz+fPnNyZ/ixcv5terrrpKj/AHHm2DRlQ9lFrUdxMi3yHS/I4dOwankl7euXPnXbt2DR06FM0veP7FRdHa0YZnzpzJp+FjcAm0fNu1DGpN3rx5DReNJunuhouCO++8k5B4pqqksH//ftWGTSEeeeQRQipWrKgDeChVhQoVyp49u32N8B133OFN+UYH5hFWVqBAAd7lxT/++GPPnj3XXXcdbxEHJknp0I8hPGT74osv1k6deOC2bdtgnsWKFWvTpo1uUf75559RlP/2t7+ZxPnf2CWiDtKC9q+ugh8+fBjamTVrVpuL+rejkiVNQm6++WZtgKBQ8ghbjlmfUUdhhW/DdvQI6eKjKP1md1QEBvIWdfa677nnHvt1UTJjo+sjS/y1baQRbz5kPOSlSKSpYRRrOa21WZ9PayokiJy4cOWVV+bOndsb7s9FqbR3HEyePJkaoP5pEW8iAwcOJDLc2/uT7lUWF23Xrh1MAIGcM2cOHJ6QefPmKRrCQL2ZxoJLyK+1Wcdp0aIFMmmSrVu3rqG+dFhTpYhB+fLl7RepGbMbDDlp2LBhvCqSNb45zfvKK6/wSGC8+IBxgEHDDoF82pIM/vnPfxouGk2VbJ/jQKqhlEuXLtU2NYPnp59+SogMbulr/M9w6n1Rm6Lbt2/P6Bw7CLloiBAhQoQIkdFwcVG0rksvvXTatGn/SwI6KBHKlCkTdVQKmN6jjz5qXiekbdu2hql6uejDDz9MCOq7/dGaNWsSCHXUozT71N2sIC6Ktnrfffe1bNlSSi0MZ9SoUS4jSSiczUUpWoq4qDBx4kQXF6WwhNi7OmSDEPsSUS8XpezazLQT1z4YNabHbt268Yh67cqD1GLDAUDZsmUJsS1v4TwQVFMDkAR7c+nqq6/OkSOHf8Evv/xym4sGaUft39rmwZAKPhTvYpgxY8bQXv+zUK1aNW0FKwL0Bsmk1RYsWIDg2UWOerioEFOWaC+YldF9n3zySeLIrDcVIh1N8tptuGiQ1gwiJzbki8iWT1fB43FRhO2RJLRv3x6xj8lFR48eTWR7ccEFmDARbDtkmRLccMMNUWfhgJZ98MEH7VcWLlwovq1HBJXmM5fxMqocPnw46uxp06a7d+827S5z6/vvvz/qbGLzv01ikZN4meSLjABQRz3Ck3l30KBB8eJHY3HRLVu2uLgoLWtz0WjKZfscB2IDpbRl+/PPPydEErt161b+37ZtG31w1apV8E9tikYdc31+2rVrF5x/06ZNxGGGyrBsh1w0RFpx7NgxI80Zg0OHDmXk51ygf/qci+An17Qd4kzEGedb4ozLcLJgVNFe09kKFxfdvHlzxPFAe9upuP3220+ePPn999/z6/jx4+Ol5lXcS5UqlStXLlc06eWdO3fWI9TIy3MCwmuji/pSvXp1lcLeGk0IF5Wtr5eL2veFwooJMfpxNBYXlTcjsyUoEIHAcuXK6VGUycVworG4qLcCr7nmGkLMQTtmBCnNVMjUqVO1s2qYasyCy6bUcNEg7Sh9ff369a5E4vWgVq1akZPbPDDW3eDTTz8VxfLaQ8bkovFkyRQWTVeVo2t1UiHS0aQmNlw0SGsGkRMbP/30k7096y14PC7qstFF7/d6P4omnak2VNkLiZl9vxoMIZJ0DHvy5MkRx3zafgUxy507t1kWke0r1HTp0qV2tFGjRmXNmtXb7k899ZQiiAY3btzYdhQcD6Zl6fjt2rWLnGpI7EVauGhw2T7HgWTS0ewesXbtWrPhCaV3nQhdsWKFLKsVYsK1uZphekXIRUOkCVrLZ2jwoWeJwgcffMDUe/nll7tWBDMGFHDkyJEMizly5PC5hPOuu+7Knj37t99+m5F5ywCgTo0dO7Z3794vvPDCM888E9PGwwZD2KBBg4iJVvfoo48yK7sioIj069ePBIkwYcKEVFxVxwBKZtLDQ+amTZuYsDt27JjwlNMJic0wFdu9e3fj7SDjgaS1aNEC1SrexsXZARcXhdTx6NIdDWbPns2v06ZNi5eaS3HX3k6WLFlc/mz1FXPnSmK5aNS6a/HFF180gZmKi9aqVYsQ170aDOmqLqllaeei9qYW8fv379+1a1eUQsU3jZIsFw3YjinV1ytVqlSvXr2YP9mAEpCI97LTlHJRRniaZs6cOdqFE2dLqUgLLi4apDVTykVhVvxas2ZN708p9V3k3VqPJm0hQt7iFdzLRaNJVyidOHFC5tN9+vRxvUWbEq5Dv0eOHNHJbdC6dWszXz/yyCP0RJ/ZdvPmzWh0EccVNhN0vPOfBtR8p06dRo8eLYLtfwo3PbgoUnTFqQjCos9ieLnounXrDBfdsGEDo40WLI4ePSrzXflCW7Zsmagp4xU/6a0Mc/EdctEQaQUjRatWrTLgQ6huuizutHDRqLNcqkHQh4sOHDiwatWqPhHOUNx9990DBgzQ/8wKjPi2WZoLFL9NmzbmFBDzMfzcnqdXr17dt29fM89NnDgR7pGi5Yxjx46hxsHBUlySANi1a9eVV145dOjQ9Eg8PZDwDKMB33PPPehkiUowRdi7d68UqXOKi44fPz7ieFiJGRltnl9NH/TCpbijbsrrietKCbgugXQ3PSaciwJIZsQ5bGlCMhUXRfElZPLkyXbif/31F9SlYMGCekwgF0VZp6TmHF1KuWjAdkwpFy1evDiUI+ZPBocPH65evXqePHmgJa6hIDgX3blzZ506dZ5++mkN76pYzQUpFWnBxUWDtGZKuaiobMzLllJxp4sXU6ZMIfLjjz8eL0JMLlq4cGFajX+oMX6FAbre0pj59ddf6xHJoeAXXnghgcWKFZNnWu1e+p8JPHjwoOoHXH/99fFEiDmCaPXr15f1rwh2xnPRVatWPXgqkvX9e3ZDTnS9NrpeR1zRJJNdOSgSLzX7KPv379fuaAbsM0XTg4ueOHHim2++WemAXhFTjukVcO6Y1t67d+/WjTcZebNNiDMFGzduPI1cNJo0LJ59VNMfc+fOzZcvn71E2rlz55YtW8aLz6yP+mLOMh04cIBKQyMxERo2bOga4NDJVqxYETA/vHvzzTeb9NOORYsWLV++3D9O7969U7F5m05gvhk5cmS6foKpqEqVKj7uPdIVcnlyTnFRZn0eGzRo4IrGVKjlan6lRVzzJqqD2siruOv8nu4gMdB+mjmSlx5c9JJLLok4Zn4mJFNxUZ0Ffeyxx+zERT8Mf04UF92zZ0/u3LmbNWvmih+ci0aDtWNKuegNN9zAr94h1x5UO3bsOG3aNB1uhJPYghecixJYoEAB867NRVMh0lEPFw3SminlorJ3RWi9P6WOi3bp0uXo0aPmcdiwYZFYp5ENvFwUvZqQW2+9lf91jJx6c71VqVKl888/X2JjJAGNWnRdVdS3b1/+HzhwoOvdZcuWQeGgl8aCac2aNVpUcgmegZrS3NxzurhoCBc0X9j6DFyMEDomHU2HhM1P27dv5yedxRVlNdf/HDt2TFw0Y9SeBHNRCon2IDtjbfjyaB8mpC4YnVVCLxclpjFW9t4fFSKEZoKQi2YwWrVq5VI70FFgmzG90oPp06fzq1FSNY9WqFBBj3DaCy+80HXo9+mnn0bXDJifwYMHBzEwC4gdO3ZcdNFF/kva8hnoMpM7XaA+0Xf9Z/2EoH///k2aNEnvr8TEOchFYTjyRGo7WUGFbdmy5ZEjR9AMihQp4tIj9+/fb04Mjh071iYn0SRVvnnz5vZHe/bsSe8zt8bF5A8oiEH8gsi3p4uLrl27Vnq5vVaiSz7Mzt6PP/7IY4kSJUyEu+++mxD/9aDUcVEE2EX2dENJ4cKF7e68aNEion344Yd6TBQX1Q6YzUV1x4w5TBuz4C4uGqQdU6qv9+7dm19pF3sumzt3rjmFSFVozEcSIKJEtt3YyIrV3vqOWRU65ViwYEGjzjJ3E7J48eKoo+ymVKSjHi4apDVTykWjSf5+vROcVsOBfcUrBfHhov/617+qVatmh6jyXWdcbXi5qLzLyv6Wz9F3eLTNgpBJ5twnnnhCjx06dDA/MeHSBPXr1+d/UuBFKOuqVatMBMi/znfwRXNwNOqcLYzE97FUpkwZm4vKRrdXr17xCgUY31xcVEdz5Z5NmDRpEiHt27c3ISEXTREYW8ShzJ1PekRsmHH0v7ay//zzzzVr1pi9UPFSU887d+507a+mKxLMReXBCSlH+hkaxLPVaXVLFT+Zc7He2e6bb76BwYqOhlw0swEeyJg+bNiwTz75xL6x+uDBg+PGjXOtnTBHjh49mlkEJd51+hkSMnHiRKYc/pk8eTLzkOvIH0kxKb7wwgvMi/aIGY3DRZnYBg0axLxFtwkuNvRGstG3b99Ro0bZFysLv//++/vvv9+vX7833njDXgE1XJRZdsKECWTeHiKjjpwzBbpsYDZv3ow+QYnksyHqDMHvJsH4dkeNU4hR2qglvkI2Zs6cmeqRl45Ggqle3GLAgqrZvvWiSXs45gp4L2zNgFITGbZpQpga69SpYyqWvNWoUcPnjnsbiBNKGK3m/UmX76FzuCSKUVWmj3wRAUbXN9M8LaUL69BxqXmjYUBQZ8yYof/lMJA4U6dOJQ4D+qxZs0zz6RVGPBi43ZrxgGgpJuAftYuRB+OFkq/QCxCwESNG2K4pCddWDwou8c1UYWdY+SHbqOCkP2/ePHqi9D8baFroynQBuqEt5AZyLmKuQ0wWPj032V4fdaaPt99+e8CAAbx7LnBRaeo2JaOZIs45NxgU7f7SSy9VqFDBeI5hmJXKCwfQsW1+NSZ50lahDRq76CY0B70sW7Zs9AvF2bNnz8UXX2z3nYoVK/IWM68JkeKuyzx8IGMHYCzDEbk5c+bACgi8/fbb7fn9rrvuIrBt27YoPQyPKL758uUjY+juUvf/8Y9/SJFllLPd59jQAQ3b7WqfPn0ipxp5Nm3alJDZs2ebEGog4twOaielz1GHJudUKZk0EeS61mt6IP3bnmXkPVgXbwpVqlSJJJlKyrsppJ0xcN26dYyBOoxnDDG8BafedKHib7/9pgSDtKPo4qeffqpHEsmfPz8h8VyPoKcWKFCACCVLloR4Mzyi/Tdo0EA7B0zfhBujPpgnxAwiYYrJKEQIjQjzRK8TrfLKEnqw7illyN26dSuiUrVqVdFLtUhKRZpAxj0CGYGDt2YQOXFBCx+mwg3UoK6f5HVME4QdmQyjBdH6NsGLOpfQlCpVysf0UVzUGB4fPXr0mmuuad26tYlAJ6L+GzVqZOZZ+G3ZsmWN41yE0F7guOKKK4yHW22T5s2bl25IuyOTNJzGf912Y2SGxiWmayQ3kCfnu+++m049bdq0W2+9lcdbbrll9erVMa0aaURGNuLYDB9B1XoEszZiNmbMGIoZcVaujePclMp2iE2bNiGf1BiTrCxvZYVL1Yl8Ihv8JMe5cC61CGKmHURGqo0bN4qmBdTK0o4Ec1H5azJqjagphY86gijDXVWNl4vqolWGP20oh1w0UwE1t3bt2jTKsWPH7rnnngceeCDqKNDM2dmzZ3etUTGFMGfTH5hUKleuzK+lS5dmeGU2YnbX2j9jPSMyDIcZMUeOHEYxRVu98sormV3oGIgBE/Drr79uUvZyUVQTHiGWZIYXXZNBPKDjMt8zFVEc9ObcuXPb1kp00Wuvvfa9995DGnXjPGq0fhIXRWOuVasWkzeciuJLwmGhL774oiZ4e8GVSYK5kE4OHaU4DLWahGSoQwpm/qAO69ev3717d00w0PgOHTqgxDDvFi9enAo0q+ABQRdj+n/88ceZKtAOze1kKcLevXsjzm3sdqBWTO2m8QHciXlLS3GC7iKD4KGjoBVRk16mFA+UKHKqiVTUoVVMimPHjmWQlXsG5Y2PylsGqhut1rBhwxYtWvArAimti7aWmRxtRIuTLFOvWpnpX4lTb9I46QXEQTK/++47+cO0TdoY7png7fXyeIAiqtcYrkVLoYddd9112i6mFDQ3iaMNwFfpMnQ6OVgnfalWZJvMoAV6M4zMaPsFna958+aoZXq0zyIi23RSUqDj0A35FZ2Aj5pLHQQET4ZhycKn5ybb66OOzSFfp+AUGa1R1XsWc1F6N9IoFVZebaKOGKBSy0mJFDLX0gYyLD0s4tywZy+EoYJLhUUIjT8YhLxbt27FihVjkGQggmyY9SNGY21SRZyLWFCaFc546M9F6VN9+/aVv1xAb0KxRnguvPBCxIxxxuxHGSC0WvEBLVu2ZK4vWrQoYywKqASezKhcl19+uU1mBCQfWZLFIOP24MGDSQFBlTEw4VAaBlWqDqFSzXz88cd0DTiA1F9Uc8ZbW68aP348eaAT8RZ5RlOXQsJoTP+iDnkL3shIpeNn27dvl88YFYFOt3PnThNCU9JSxIRVKuTmm29mzCdXJK6QG264YceOHRr66A7aQ3MVfOnSpXIMC+BLpvV92pFZg25Od+OVevXqkSzThO5ijTh+a+Kd+iZcO5kAYsOwqZmIobhSpUrUrXGjhaxqD5zRwFiviK4zjiG98WQJULFqAoSEcYnxVrenGn9IwUUazkPTqIkZamwHvPFaM+psTfvLSczKgf9D7ZBzE7JlyxYaV0Ko1Gh96pA4mh0EOgIvMr8wxKngLn0AleP8888313LGhEp93333MaSj4TB7Mju4uCtjI5WAHjJw4ED0BOZQo0iAGjVqoHpRD++++y7jf+fOnc1iNNGQCq0RiD2aI4JwURQSWvAtB4zVPne60Joa1WkduidyqGtRmXG86+aIkBYRQJMmTZipDYtesGCBuhsy3K9fP4g9rYPw03Cplu1zHLQ12ojZ9oNbmgNWzM7aIxQYx+xjOChjhqAB9JwMuzgnwVxUxTBGGjr8yohml+e3337zclHxdUB/C7loJgSjnll3ZCzr0qWL+QmFKWJxUf4pVKiQrquKOlq1lC0TH62aEGY+DUZMtxHrHD96RsS6eZkByD624eKiaCQ8IjB6/OSTT5hsghSnUaNGzIga3JnmGfvMMio9ExXEpIl6wcxhzmZI6WdGlPTKgYTtRYCasece6K59rlJ3o4nZ6nY1piubYTL3SDlD0alYsaKxb9fderbhTRC0bdvWtBqdixGf3sc4BcG+LwCk0TJR8WkYnZ2yTJV8bkiLOny1R48ederUQa9lAnb9yuwlnxww0uBEFKDk0XauQORnxIgR+p9mRe8hjtmdRhfh0WhRzOsRa1H82WefjZxqXiX6bahd1LkkMHKqja5UdlO9UWcp3ZhIJQs0DF6HZ5oQdDttm/N1lDNTnGjSURwj9jpRYxsrejOMJhFx3GzKgyJCBcOhF5sIjRs3RmHS/7RO7ty5UYC8+UTgUUOD7Mn791z/Xs/ESUfQ2q0gnnYWc1Ef0EO//vrreDMg4waqf8xlqRMnTjBCel1f0iPQpIO7YKDjJFwFod3hWiYP3mMOiKhtbpMxoJK9RjEJBxqzXfl80T49GLzgKW3HIKAhGMzjnbbwARJCZoLcr4ZCaBsKMVi5ipAKkY6JxLYm6gQTh3fmSiMY2CGK/sc9jI0uozdDgc8OKuSB+vGmphEbBQluH/PMP+VivHVtLdIQsh6nLXgxWalAFeTrhuWSZurqnxcRQnUKdJ6MvNbyLAYygAhRq67BnEcaDtE6fPiwV7T4lXBezOCbGhPMRUUyjf9o+oBC7K4Sk4v+9NNPxr455KKZEOXLly9RooQxnrHvHZbJh9FWUR9dinK+fPlq1aplHl3Wd0hLxLHp0iOf6Natm5kAmjdvHrFuY3NxUangDRo0kOQgUbY664MPPvjAvp6rQIECxjn+k08+WalSJTuyltj1v+u8qJwW2GcX5ePOcNErrriidevWo5Og00HG7bAuCjPnYVavXm2OylDGatWqmRflcqBw4cJBSieMGjUK7mF6mQwCtWXBuP9ZAMhTrur8H//4h5249kV79uyZbDbQQm699Vba15icCRBdmJss6LJnzx5wizXq7NQVKlTIDmHi1AKBqS6t9xsbNqZ2eK+Jr+vRjW2hl4uC8847z5+LMprDGIsUKWKG7FtuucV0kGTxww8/wL7MgSsEyfQRqoVvua5U0camAr1c1JthHXC1L2OoWLEihFP/MwNBTSmU+fWOO+4gP17lQxwySLn8e65/r2/UqJHNk73xQ4QIESKDwbRrTFsTAkh4uXLlkr3yLaYf3RAhzmIkkoui9Ypkmi4ks9tkuahcFpmjCCEXzYTQgfJs2bKhKNvGllEPF6XhZF9kIpQtW9b2gOLSMqGREceiyU4TFXbWrFm9e/fWlVkmca+NriyaChYsOGbMmJT6nqYg0BU4DHq50eNR0I2K7IXXd5FrP8rmonJpwHz271Oxbt06RT5x4oQctUtlf+CBBwzJr1mzJvTg3x4ELCMJkqx9oEhrBAFtmG3Af3gRim4H6ryo1x1fTDAO5MyZs3r16ibzDz/8sM5iMQgYA07vjeoxQWOZS8wFneGBfbnqypjLurioi6eljouaF998882oo2TYjoKDQMc+ZWU0ZcoU47FGx2Nca8OSc+3lpo6LuiqhdOnS9BpTImQvb9683kxq/zbepZdexOu5Pr0eGaBNqQ07nZCLhggR4rTjscceS93ZFi+OHDmCImSv48dDyEVDnGtI8L7oihUrUAHN9T70JR2NteN4uajcN23ZsuU7B/JdtH79+nP8mqDMhvfee09+KYoWLWp88EQ9XBT8/e9/z5o1q7Yof/rpJ/63ddlkuSicpEGDBjp5r7N8PlwU3RcyqdN3NWrUcO0mxQOkaMiQIS1atFD8AgUKGD2e/+1dXBdSxEU3bdoUSe5Q5XPPPaftyqNHj9rXOVx00UU2n08p5PXBvgJUnj+Mx/bgOHTokKwr7cC5c+cSaNuR+qNu3brEX7BgQdQ5j+RywCgHQjRfkKSoGfs2iGjSyVufLfF04qL79++HRJUtWxZxonrHjh0bJP8Gcukks95GjRoZSyqdPnK1VL9+/QiUd5OEcNEXX3wxkuSdhaG4TJkyMS/6k825MVn3h0/P9en1WuxwnUoNuWiIECFOOxgbmeYCXhzqAxSVp556KuAWi06lpmKyDhHiDEWCuah8NJn+putbXG64vFwUFurd/wHBDd5CpDe0F4oGieqcJUuWnDlzmoMiXi56/PhxeFS1atWI/PDDD7sUWX8uOmrUKB7NqQN/LnrixAn9tG3bNrlxq127dpDitGrVCuXbONa3uWiVKlUuvPBC22u/SqTIKeKi+/bti3guYYs65rJm14v/4epkfty4cRMmTDBxKlSokD9/fpND4eTJk0Fc40QdS2Nzh4pADZcoUYJOx6TYvXv3BwPAnGaEHdEQdmpyMxjPK/0NN9xA69uHfLQHCGHjf6Zk20BaoL/ny5cvSNEqVqyYJ08eO2TGjBkRzzV0UWdg0T/pxEWjSduGs2bNqlevnsteIGBZoNZItX0SWD4eYPt2TPlE0Zp6Qrho1KGjxYsXp6HpkhMnTox5RJCeYvdHH/j3XJ9er8UO1153yEVDhAhxruGbb77p1KlTXgfMKYMHDw54VjZEiDMaCeaiUAJtaUqtkV9gl1s8LxdFF9ljQQ6QIKKhy+bMgx49epj/tQ2lPa5oLC46b948n81Afy5asmRJqKA5ZiYnhPG4KGTD8DfESeqv7RYiJnS7XaNGjUxI7ty5jR7fuXPnyKluJMlMz549dSwwRVw0mnTtu+07HhZK/m29H3Ufek8i9mk9ndPr1q2bnfOnn346oCvdq6++2vYv9cMPP8BV4Cd6XLt27acBYBaVIEIkaKcPmYTAG5tbOLPZ1qOAWq2wXSbIlb+2xyFILh/3Ucefx3XXXRekaHKjZ9eVLrsjPzZlItC4VvLnonJL67przkXtZDfrdeHz008/kXKpUqXs+9CCQ/ytQoUK9oLd22+/HXGcBNoxIagQV5HhTz75JOI5wZtSLvr9998/9thjrsUOLxo0aBDwlLJ/z/Xv9bp/0q4Exbe9W4cIESJEiBAhzj4kmIsePnwYdVMn4oA4p8vTWkzfRTbC86KZEFdccYXxfYcqjFJr7sDU1d6GeOzfv59foVvvvPPO/PnzkYeNGzfaLrnk/N1Y7ep8qTHavPzyyyPOZVOQrrFjx0pJXb9+vY77f/755zzqXuaow0Vr165tBAlSUb58+WTLIpvAHDlyQLc2b978/PPP58qVC9K4d+9ePkp+dJkkZBWiS07q1q1rbJLJZ8TyK6Pb6m0HpLrr7P3339ejbusmfcJhO5MmTSLD9sXr0SRXw8anqEDG5HW9Xbt2s2bNmjNnDsq97SvfB3RD3jX+e6n8WrVquYxsU4StW7fCLXfs2GFC6tSpY7uQRQaIYCSkcePG9uVmImz16tUTd6Upy5Yt67LAf+aZZwxV9sfixYupFttKPJp0ZTx0aNCgQfz0yiuv0GpGJpHebNmymV1Nbeoal1HUKo89evRAkLQ7KpdUxnlyNOmCxAULFhw7dsy1zw+ji8S6iS4Ijh49mjdvXpfbHrJRv3595NNcb7B9+3Zk0hx2QOwjzhUREHL60cmTJ70Z1s3j/fr1MyGlS5dGKkxnqVat2k033fTWW2/NnTv3448/Ria9LjEhlvnz53dd5xMP/j3Xv9erRWg+GVrzil6Hkca8+DREiBAhQoQIcXYgwVw06pwR1X2p/3ZuczH3uxiEXPRMBOQB+jHRARrkjBkzos5e1sCBA0WZ2rZtu3r16qizRXbzzTdHTkW+fPlgU1HHe6puDiQO8UlBWj5s7fXXX0ckiKCrPlCd//Wvf0lJ5XVEAqUZPhNxPBWNGDFCrvALFSoE6YKtQT+uv/76TZs2BSmO+EPEcYFLHu6//37+r1y5si6gQ4HWtajKhm7lRuN/+eWXdc3anXfeidIMQ2vfvn3EuWEPYkZ+YDXFihXTTqmho2jnF154oVKrWbOmLiN1oWrVqt7DIXCqEiVK6EWosrmSJFnMnz9ffJhcwUmaNGkS/GBnPMycOZO6+uabbw4ePPjkk09ScNtgtWPHjpUqVTI70pDADh060CK6T5hSkwebfFI0UoPq016ffPIJzRGQZgtQa7irHcKnyYMuIgMIlc7KQh11MFJsf+fOnZBkbdIi0vKWBIVWq8HlaIUVK1bo6p0sWbL0799f6w6wNZ1Jbtq0qWvjnTIiJKm+A4NcyfuRjd9///2JJ54g2Z49ew4YMOD22293ebxo0KABmSHbSL43w2SJKpL0EoEMyw+zdtq1ZNC7d29zxZzAI4GuohEY8NiST89NttdHnRUB3TJH70a6HnroIdJ59tlnwxvkQoQIESJEiLMYieeiUccxzH/+8x/0Uf87lEKcQdDGJlos9M//AINsUIkGo4NmzJs3b/r06ZAie9PGHwiPvRkCP4x3z9UfDpC3H3/8cceOHSniAyRrm9ryRZeLWgpLssET9AEpb9++3cctno+bLvJJNlJUtKeeekr7w7QanDkVd8fFxP79+ydPnjxq1Cj7OnIfbNy4cZKDr776yvvriRMnYKRjxoxBQlzXvQRJuXjx4vbV3gLlRfCSNdL2giqyd31jgkx6V9bAyJEjbVPYlIJxMl6HotGhbd5iRh3JR6LSMsAOHDhw4cKFmzdvXrZsGf+89957I0aMqFy5sm3nfPfdd7vYqT+C99yYUHl1lDrmnXghQoQIESJEiLMM6cJFQ5yzQJu88cYbhw0b5v2pa9euGZ+fcxPVq1e3XQ2flZg4cWKvXr1Ody7+v1WGq6+++owjTv3792/evLk3/LXXXjNkcvHixY0bNw7XE0OECBEiRIgQ6YeQi4ZIJOQ5tmnTpraXl5MnT44bNy4VN1uGSAV0WPTdd9893RlJd4wZMybmqkcGYMuWLTDhmTNndu7c2XbrdaagQoUKZcqUkUW6wbJly4xv3pUrV1I0+5h3iBAhQoQIESJEwhFy0RAJho5i5smT56abbmrevHndunX5x+WkNET6QTeLniN3865evfq03Pw0aNAgnbGsVq1aokygMxI625k1a9batWs3a9aMHnrNNdeMGDFCu6AnTpzQgfAQIUKECBEiRIh0RchFQyQe27ZtGzlyZL9+/SZNmrR27dpUu3UJkQrs2bNn1qxZpzsXZzmOHTs2bty4MWPG8M/pzksq8euvv06cOLF///6jR49etmzZmciozz4wVK5Zs8blI/rswMmTJz/++GPXhbE///zz+PHjE/4tbzVu2LCBDhvzYPbOnTunTJny2muvyfeecPDgwQ8//HDIkCGLFi3y3uR0ZoFKDu73LiYOHz48c+ZMlxkFVSp/hGcW/vzzz/8GgBnYKfu0adPC+wVd2Lt3Lzre/v37T3dGQpwlCLloiBAhQoQIcZoxcODAokWLRiKRtFy/lAkB2Xv88cflS9x4+YId6TIw+87bhCBmNcov+ty5c12RJ06c2KVLl3Xr1tWsWZMIr7zyCoFffvnlrbfeun79el1l3Lhx48TmMMMA85fn+UsuuSR1KXz66ad33nln1qxZzeXA8PkBAwYUL17cvh/4DIJuUBNy585doECBLFmy8H/OnDn5X57AwWWXXbZ79+727dvLN/v27dtPd8YzFx599FGqpXv37qc7IyHOEoRcNESIECFChDj9eP75588ULvrHH3+kKL6uHbI9Tuue54Rz0Wisanzrrbdatmzp8mQOBSXa2rVr+f+XX36BWS1evPj3338vXLiwSCll7Nix45AhQxKew+BIaT27sGPHjrRw0aizyazLfu09bTj8GcpFFy1aBPkcN26cOQxfunRpytK3b1897tmz55577rn44ov1CCnNtFw0jbKRlpRXrFjRpEmTmBfUZTDSrxJCZCRCLhoiRIgQIUKcfrz99ttnChd9+OGHDx8+HDz+gAEDXFwUnHfeeenBRQNWY+fOnYn2n//8xw6cNm0agR988EHCc5U6pLSeXaB0aeSi4KabbnJx0U8//fQM5aK0bKdOnewQFxcF//d//1eyZEn9/7e//S3TctE0ykY8UPz7778/4cmmB2iXfv36ne5chEgAQi4aIkSIECFCnH6cKVxU22IuFuePTMhFa9So4S3F008/nXm4aCrq2YWQi7qwcOHCjz76yA7xctGoIwb6J9Ny0bTLRjx06NCBUic82YTj6NGjlStXDi8LjIlffvll7dq1y5Yt46990vuvv/5av379ulNx4MABwtfFQcwbzhOOkIuGCBEiRIgQpweHDx9GP37rrbc2b94ck0QdO3Zs3rx5I0eOnDt37r59+1yv79ixY8WKFfzz3//+d/78+dOmTTO33Z44cQLO8Oabb27atMn73R9//HHmzJkTJkz46quvXD/t2bNn8eLFyhsfnTRpku2XG56mY3Xo9PATO0skRWTKsmbNGpfLumS5KJ/4zMJvv/2m8C+//FIh/ltAyVYjeduyZYv+/+abb0iwRIkSphSoXD///DP/NG3alMDBgwfro7bjIp8aO3jw4NKlS/ln48aN48aNs6srPerZi//973+IwZgxY2bMmGHHtLkogrRkyZKY8kBjobby09SpU7/99lvXr8G5KJ9bsGAB2SAzrquJYQ7vvfeesqpv0Qregvz666/vv/8+7cjnEOCYhd2wYQNNTElpMp86CYiYXNTAcNE//vgDtX7s2LExXYv5FDwmqHCKT23T6BTnzz//ND8hJ5I9urZCTKcwlDiebOzevfuTTz6JOtVIbU+fPh1OYnJo0pETLwm8Ledko1evXiRbtmxZr/y7QMoaeQx+//13KoGmIRxJpsV9asBf+A3gUfxKtZOm7SmQ4iB+ZPWuu+5S//X51rkGKu3fDpYvX65/du7cqZ9o0H97QM0jkN5wIWMcd4VcNMQZCXvsThYurYh3M8y1b3iY4fTi0KFDCUyNydVfI8yEgKLYQpiZHULSMdNjmT8zA+qI2gdRYcp/8MEHq1ev7iJR6OWFCxeePHkyJOfhhx/Oly8fMfUT2pvi8yLpVKpUqWbNmlmzZr3gggsgG7Nnzy5TpkytWrVy585NoL3Rhzz84x//6Ny586hRo+6//35SaN++vRwp/+tf/7rhhhuyZMmii7hKliwpTZ08fP/991FHnPr37583b14CSQQN/osvvlD4bbfdduutt/LIpy+77LKWLVvafmuT5aJI5kMPPSTPMbNmzTKL8ZSlWLFiDzzwgI9q61ONMPMXXnhBvotgOIo/fvx4cp4/f34Cn376af5/+eWXP/74Y/6pWrUqgWS+rwMdMfWpMRTlFi1a5MiRg+K/++67lIhf27Rpk071HBMrV6689tprhw4dShFat25NZszFy4aLQlGKFi1asWLFbNmy8V0kyry+devWK664okePHrAgskoEkrLTD8hF33nnHept+PDhvXv3Rupq1KghDZj0qZCcOXNSOd999x2tw+eyOkBU7BSgl+SQKoW9X3rppXny5KFcVKyO70adBYt77rnnmWeeGTFixI033pg9e/bXXnstXrUERBAuilxdddVV5cqVI0s8Io1BCh4P/ErmH330URpl9OjRdBZ6rrmcjF9V4UiyQtasWdO8eXPxrmgc2UD26tWrR8vecccdjAzIgLwu5cqVS0sAkBC6lfqXCCqVST3TLoRomQZ63LVrVx4vvvhiW/5toDuNGzeOHPIt2sKEw2ypH35CgKGONO6qVatiFj9Z4RdgnlTR3//+9/nz55PP66+/HgE27scgvZSUt6655hr1X58KP6fANApvR2J/+umnqLNkwP/Lli3TEslvv/3GI839q4Xff/+dZv31VBCHmPT6IGsraUfIRUOkBvfdd59rSSzqLMWhcDA/3eSgbdu2jI/m19WrVzOC66cu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1FNPPQ656PTp01EeDNeRPISfHwNcdO3atZnHRQkcL7/88n//+9+Z8fDjDSeccEJ6uejDDz+8e/fuTCpPDsHXX3/9xBNPmMtff/31SLhoSsqQjfj0008zzEW//fbbnM9FwVlnnZXFXPRogfxajuKiOadrOORApJiL/vDDD3DIhQsXHjp0iPhsyZIlXEI1o14ssmrVKm4Zqmm46N69e3da2L59O2aUDMFzaByyEZs3b37jjTfMJU08a9aspUuX/vXXX+++++5TTz31wQcf+H6yf//+iRMnPv744+PHj8e9Jf+u1atXv/jii8899xy/8nFRFOmdd97BrqkMr732WpcuXTC7d91112seli1bxl+8VP78+ZXC08zP0at+/fpBXIm87TeieOPGjeOfxYsXDxgw4P/+7/+UvmPHjtGjR2NDp0yZYk/yh1efSy155e0zZswIryyvGDp0KC99++23KXzMmhqEiDSZFlm0aNHAgQO5xbt8G2iDXJSfI6sRI0bwq2Q6I8Hu2LFjKduwYcM2bdrku3vgwIG33noLSQ4ePNguOelI6ZdffiGRsq1YsULp2Acaa9CgQf3796ckviFVhDNhwoRnnnkGaXz22Wf2gFfyxUZcJ598Mi01adIkymDOuKIkL7/8MhVBJXwH8KA2qOVLL700b968L7/8Uok+LkqrSfFef/11ek1CuUknAQX23frxxx8pGyVBsL7m3rdvH89HzrQjzd2nTx+KpFvUmvx9+/Zdv369/RN0Y+bMmQh2zpw55OfJ9rFeMbkocp46deqTTz45cuRI0yko8GtpoL9s3LhR/9ub02zt5S233HILD7/11lvJRjW/+uor8wTTQVauXKkULa3nV/QLuQ8HG+nlopoiO7aPkiKKqFSp0j//+U+TkvVcNFiGbITjosczchoXzVFd43gAzppg8pNPPuEvUYRJx/vjZ31LUIm+dBefC03DdMhHH+EYfbqQYi5KtQlTTMwkaqqFNASLWrgrnmlzUR+IbLi7Zs2a1JbNIcNYuHDhTTfdhGm7/PLLlUIsC28hBVbTpEmT22+/XZf/+c9/zK++++67cuXKvfnmm99//33Lli25e/rpp0MsIQ8h7yKw7t69e8OGDb/44gvCUIxpwYIFFXgR3cI9oEw8SpvyYV8833DRNz1AZvhbpkyZk046SSminbC4O+64A4oyf/78Rx55hHgO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v/5KedkcMoznnnvueOaiP/7449ChQ83l0qVLw7lopqJXr17HYe8YPHiwj4sG4WumLMbs2bPnz5+fZa/7888/e/funWWvC8E///lPx0UdHBwcHBwcMoAUc1HCIyKSjz76CEr5ySef8A+XBw4cMBngn9u2bfvIg81F169fr0SCOf2zevVqO4ND9uJ45qIHDx68/PLL7Q95ZyMXnT59Oq+mo2X9q7MXL7/8cjgXDTZTVmLz5s1Fixb973//m2Vv7Nix45VXXpllrwuB46IODg4ODg4OGUOKuegPP/wAjVy4cOGhQ4cIl5csWcLlN998E/UixVWrVnHrozQYqsktpfz8889c7tmzByrLpTspJ+fAcFFaZ9q0aU8++eR7773ny0OD0mqDBg3q37//Bx98YObuZs+e/ZqH119/ncv58+e/loZly5ZFve9l63LDhg3maTyqX79+L7zwwtq1a5VCZvNDdEmJs2bNUooZ8li/fj28pW/fvnPmzLGLt3PnznHjxvHP4sWLBwwY8H//93/JVPz333+/5ZZbqPutt97KWxRwGy56+PDhefPm9enTZ+TIkaix/UPeYq/P5O6ECROeeeaZiRMnfvbZZ/YATUzEzE9lTz75ZF49adIkCqODfOLVi7szZsygbEOGDJGcbZDy9ttv88/nn3/OW8aMGRPkt++///5TTz01bNiwFStWJD8w9MUXX/CTnj178nbkw18St27dqmYSW+NppikxGua3aMLYsWMff/xxnrBp0yb7sUEuiojeeeedr7/+Ohqrmb766ivzCpUBrFy5Uinbtm0Lr0U8LQLoNpo5YsQI3qLCU4bzzjuPt8OEebgsXjSgA/v27aMLUC/E8u6779I0KI9u8Rwqzut4r/0uOhGFJ52WxXiadNqF151//vl27WyBGISoAVYajUKZeQvl4ZlULVwsBhQYnXn66acpVZCLxjMFGROvQ9YAIzNz5kz6b3YXxCEngk6Ns8jK4TaAEcADZvZb9u/fP3Xq1J9++imzX5SNwPV8+umn4Xk2b96c2fMNyRQjeTiTdcwgxVyUWIcQ5Ntvv9WlqCn2K+opjRbuoog+LkqIxuWCBQtMCuERKTn8kMzjCuKiRJZXXnnlnXfeWbFiRS4hiibD999/f9111xGbwjo++eSTSpUqVatWTceoYClOOukk8kNpuPz555/r1avHZdeuXQ3/GT58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Y+ZW7HvkEkQzF2UEYVbT13+5hIJaNllnSJJlXxENcEwexFRrysbhkkGUMWnSpJw5cwa7u2vXrhQpUqi57TbjoitWrLjZhb4XX3wxrmxvhAlGSab2N99889aTiv+F/T/2zjzspnL941soY8gcHUqKoiKFn1SSNJ6SnFIalI5ZNOqoLooiclAUERqRlJKhhCZFw0nhUGlwcFJxEEnT+n2u9b3e+3qstffa+33t9yWt7x/72mutZz3rGe7nvu/vM+47iG5HMfYQl19+eYAZooVcZnjjjTfi9eJe6xInWGPd+PqHHXYYDu4vOYAI8WKpUqXMz07KRdN+0cuAizZs2BA+aa45NMMmgK1bty7AReFmZOGMM86wO//4xz8IAx8LpAEnye7AplzvH08dpmRdSPfccw9PNUkywzSDWrVquXGCgw8+2OVj+GphIu0igotOnTrV7qhfYOLEiak+napakyKitMNVLLp12mmnBSI59NBDA7wxkHdyjWJ0X+nWrVv37t31PykXTRunyqF///7uW0jgVVddZXKLy6fByaVLl/J0yZIl/Nfmz4YTTjghgou+9NJLPH3wwQftjolW9Le8DLiokAfJ0XRuTZb2/C2vCF+5cuWkWfj555+rVav22muvJX0aI0auAHUS87I7mpRLC9IkfLBlyxY4J57w559/bpPPv/nmGx598skn77///ttvv42CKshDfbPMRVUKGBVaF41fRaDONo0UAw1BaKQYuDusrFixAgYrOhpz0X0QVOjQoUPvvffed999N/AI0R8xYsTgwYNxdNylEb///rsmDPAHmnT33XcHFD1N4plnnvH85UD33XffE088EVhZgekdM2bMwIEDw8qakLNmzSJOPm0WGqaB3i9fvjzRPvfcc4FX8Cdwr7ETo0aNIgAGxuWiiN+gQYNwIwJbveNRkTDM6rRp09S3Eg3iXLt2bdLD5bmJU5V05gM3pRegXq6NT3Xf8ztuN23a5N7BCpL98CIcYtBCGtKvWV6ebyM7duyIY+QaWmrKvXSTQasMz2VAYVkPHH5V+MUwSIyi+slH4Cl3NmzY4N55+eWXqSP18QcQLgHLBZG45ZCVzJJyG0S1YowGybDFV2Hgx6gE+BNYkqS3yCDK030Ff1TT5yKwcuVKd0vG6FZGNvHsuf/4449jhJSepO2IR1zSEB566CF3aVPaZq6M4GXeeeed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MWP69u17zjnn2OrWGDH2M8yZM+eAAw4oWbJkp06dsAWTJk0aOnRo+/btr7vuuvABMzFixPDyiYvGiBEjxp8T2mwzMJh5+umnZ3g6aM2aNQM7gcWI8cfFjh077r333pNOOqlixYp16tS5+OKLR40aFegnihFjP8Nbb731t7/9rVatWpUqVWrevHnXrl3Dx+rGiBHDEHPRGDFixMgafvvtt7Jly9pxCJ4/A/m4447LZOrp119/ndj90MgYMWLEiBEjRoz9GDEXjREjRoxsYtasWSeffPL48eMXL148ffr0zp07v/jii2nf+u6773RawI033piVudwxYsSIESNGjBj7OGIuGiNGjBhZxq5du5YtW/b6669nvqJyzZo1tqPbypUr8zuFMWLEiBEjRowYex0xF40RI0aMGDFixIgRI0aMGAWNmIvGiBEjRowYMWLEiBEjRoyCRsxFY8SIESNGjBgxYsSIESNGQSPmojFixIgRI0aMGDFixIgRo6ARc9EYMWLEiBHjD4bff//9hxAy3CjL8NFHH40fP/7nn3/Op0QWJFatWvX000/v7VTsHSxfvvyJJ5645557Hnvsse+++y5t+DVr1jzzzDMFkLB9BDNnzpw9e/Ze+XTBN7Gffvpp0aJFw4YNmzp16rfffpvFmLdv3x5QOLt27drDkDt37rQwO3bsiE4AWXPj3NP8xNhnEHPRGLnAli1bCuAr27Zt++233wrgQ5lj8+bNezsJ+YUCPj6kYEQoD/jf//5n/xG/vZjOX375JcIk5zZttKbM+cnezXiMXAFXbMCAATVq1Ej4qFChQu3atStWrHjsscdedNFF48aN+/HHH9NGQmDexVMvgATnHyZOnFinTh0yctRRR+3ttBQ0EINLLrnk3nvv/fzzzydPnlykSJFDDjnkv//9b6rwM2bMOO644yirY445piDTuRcBHyO/BxxwwF6x4wXcxDDorVq1ev311x9++GGpBchetiJ/4IEHTj75ZCmcEiVK9O7d+4033tjDkLNnz+7evftBBx2kwCtWrEj1dQwZKk7BTjzxxCFDhmQnVzH2AcRcNEZ6vP/++zfffHODBg3q1auXf19Zt27doEGDWrZsWbRo0Ux6dgsM//rXvwoXLtylS5e9nZDs48EHH0StT5kyJb8/VDAilAfgpiB1zZs3r1Spkt28+OKLMY1ff/11ASfmpZde6tChA64kf1KFyTBtv/766+jRo88555wDDzww8/7jvZXxGHnGyy+/LOfs7bff1p133nnntNNOE9nYsGFD9OuPPvooTGaf0rd5w4cffvjn5KItWrTAlbfLZ5555sgjj/zqq68iXoEV7N9cFO0XuNOtWzfo0F75egE3sb/+9a/nnXee/o8aNerSSy/N7VyJaMDnpXD69u2brZAA/0qBr7rqqlRhXnzxxUQOInpbYvwREXPRGOnx448/vvfee/ltvXbt2oXnVLNmTT60T/lGuOb169d/6KGH9nZCsg8c2bp165oXm38oGBHKA3755ZfPPvusWLFiMEC7OWDAgIYNG7ojpQWDTZs2tW3bllKK4KKZpw251aBZ5lx0b2U8Rp4hDgb+9a9/2c1t27ZJkbZr124vpq0ggW/6J+SiCxYsINdz5szJ1VtffvnlPqiKs4iuXbtu3bp1r3x62rRpe3GWwbp16woVKtSrV698/Urx4sWRnzFjxmQx5KBBg0qXLk3gIkWKrF27NmmY0047rVmzZoQhj7lOdIx9G9nnojCKFStWvO1j+fLl7vSAn376aeXKldx//fXXly5dSrOxDhu8pQ9CSDW/PMZeQalSpQrAep1//vn7GhfNFWbNmrVkyZK9nYp9FAUjQnkALqzLRXOLO++8M1spue+++6K5aK5w1lln5YqLFjzi9rKHgIKGuSi4/vrruVmyZMnsjorss/hzctHbbrvNHRLPEPs3F500aRK52ysdani8tLjnn3++4D8taJZEfnPREiVK8JWHH344iyExfKisMmXKEP6GG24IB/jwww8rV678yCOPaLp1XtL9ZwL68P3334dq8QvVch/9/PPP//73v995550333zzo48+ct0DjMUXX3zx3nvv6cWNGzcWWIKzzEV/+eUXcrhw4cJFixaRGf5wCQX1/JVI77777kIfFIH+fPbZZ3qRglsYgl6MsY/g4IMPLgDr9de//vWPy0U///xzlCnivbcTso+iYEQoD9gTLjp9+vTChQtnKyV/Ki4at5c9RyouKpaCZGKUdQfGgm+BVX3iiSdeeeUVC/nJJ5/gmgSixX2ZOXPm2LFj33rrrfDqZbyZWbNm8eebb74hDC54OGFbt259JwcffPABdz799NN3HIgk/+c//9Glu3AdIvHaa6/hws6dOzdsC5J+PcBF16xZ434r2pfg6ZIlS8aP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/vrr92IaYiSFuGhAYGLEiBEjRowYMTJEzEVjxPiDQRskgJNPPjniULg84KmnntJm+k2bNr3oootatGjRpEmT8ePH791dxGxL4exmNsYe4qeffqpXr15i960+Y8SIESNGjBgxMkfMRWPE+INh+/btjz766Lhx4zLfxzJzfPfdd5MmTRowYMAjjzzyxhtvFPCagTAWLFhAYu7yMXTo0PARdjH2Cn744Ydhw4apXqggd++QGDFixIgRI0aMDBFz0RgxYsSIESNGjBgxYsSIUdCIuWiMGDFixIgRI0aMGDFixChoxFw0RowYMWLEiBEjRowYMWIUNGIuGiNGjBgxYsSIESNGjBgxChoxF40RI0aMGDFixIgRI0aMGAWNmIvGyDt+/fXX7du37+1U5AK///771q1bMwxM7n744YfoMAQosPNOfvrpp8DGuVu2bCmYT6cF5UBx2eWOHTtytQFv2ozsOznNJ0Q3JWTsf//7X+axFaRYxogRI0aMGDFi5BkxF42RF7z88ssdOnQoX778s88+u7fTkhHmzZt3/fXXH3rooffdd190yF27do0ePbpdu3Zly5Z95plnkobB0SfMueeee9BBB3333Xf5kN7dMHbs2LZt25YqVeqdd97h8vnnnycvNWrU+Pvf/57fn47GunXrBg0a1LJly6JFi/73v//VzV9++aVatWpHHHFEWjr02Wef9evX74QTTiCGpAHef//9m2++uUGDBnXq1Mly0vcZZNKU/va3v1HCn376aXRUBSyWMWLEiBEjRowYe4iYi8bICzZt2oR/nEgk/ihcdNu2bbfccgsJTstFf//9982bN1966aUETsVFwdq1a6FbhCkAp/+bb7457bTT+Ja46A8//DBy5Egu9zoXhbdv2LChVq1aJMa4KIAOQeYzef2ll17i3TPOOCNpgB9//PHDDz8kwFFHHZW1RO9jyKQpDRw4EMaeiaQVpFjG2EPs2LFj2rRp33///d5OiPfvf/971qxZ4fs//fTTDyH89ttv4ZsBpJoWwX2a/FdffZXPGSogbNmyhRocPnz4G2+8gbJ6++23P/jggwL7+saNGydPnlxgn8stkJPXX3/9vffesztvvfXW1KlT8xzhHr6eH1ixYsXs2bMjAuzcuXPs2LGff/55PiXgyy+/fOSRR9Ak+RT/Pot169bNmTNnzJgxezshMbKD7HNR/Eva59s+li9f7s4qxA6tXLmS+2iopUuXIkz4/fYUtvDxxx+/+eabixcvJtjPP/+c9bTF2BPMnTsXi2uXQ4cO/QNxUc8fTsyEiwoiexFc1PMZV4E5/b169TIuCpYtW7YvcFHhoosuCnDRzIHbGsFFhbJly+5TXBTFNXr06CxGmN2mVJBiaQgoh30wwn0KmzZtuvrqqw866CBqCh64F1OCVjzmmGNIxl//+tfw04ULF954440lS5ZM+GjduvUDDzywYcOGfv36VaxYUTerVat2TA5q1qxZrFgxbnbq1CkQFczklltuUVREWxB5y2d89tlnDRs2xJ8ZNWpUIgcPPvhgAXwa/X/WWWcVKlTo4IMPLoDP5QGDBg2ShPzzn/+0m5UqVeIO5Za3OPfw9exixowZRx99NOn529/+FhEMF4Iw5513Xj4lQ/2Y48ePz6f4901gHeR1RHsOMf5AyDIX/eWXX3CXsTSLFi2CcPKHS3WRYorefffdhT4gnPpjamXr1q14HtzRLyCwuwItxt7FF198Ua5cuVdffdXu7N9cFJdiX+ain3zyyb7DRS+++OJ85aKHHHLIvsNFd+3adfLJJ//jH//IYpx/dC4aVg77WoT7JkQC9y4XBbNmzUrFRYWbbrqJADRD7LvdfPjhh7l5wAEH0CLcwNu3b7/aR9Ko+Mp+w0VPPfVU08CURv369XPLRffEw8FlSstF964HJbFxuej999+PYGSeqkDI3L6eh0/kCmjstFx0/fr1bdq0eeGFF/L8lQACCZ4zZw6s7Msvv8xW/H8UvPXWWxT+oEGD9nZCYmQHWeai//nPfzAzixcv/vnnn7FbS5cu5XLNmjU8wlUVydR0ArwNXWr888MPP+T/qlWraGk7d+7E50bUNm3alN3kxcgbPvvss9q1a9PyccGhZ6pQc6C3bds2Y8aMAQMGhGd5ffvtt4899lj//v2nTZsW2HcnjOXLlz/11FOeP+0Ei45137hxo+crX2Tj3nvvnTx5cmAJ4u+//86jBx54YMiQIfPmzQvbFaWNBEyfPp0/YS7K64MHD8Zewu7c+7niouvWrSObAwcO/Ne//uUGID0zZ85EXWJEaRTuoy1btkyaNIny4c/jjz/Ou4EEeH5rmjhx4j333MO7mXBRnEKySUWMHz8+wAz50OjRo0kGRvH999+PyNRPP/1Erml61MKwYcNomGkjD3PRzZs3E8ytDjwn8nvXXXeNGTPGnbBkXJSaJZvU8pNPPhnYX8rlom+88cYzObDSoOq5nDJlSoaOBSUg52DJkiV8kUJ2nWwvtVyRWjnTmH83AQHMnTtXKSRJgTSr8MmgLlevXu1l0JQo/BdffDEwIEBNPffcc8j2yJEjXV8krVgmRaos40spqWKGBLO8IJ9eCuWAVicLH330ESWG2CDDNpMtbxHulzjrrLP2BS6KeERz0eHDhxOgbt267k0EkpsHHnhgOPyGDRuuuOKKpFFdddVV+wcXXbFiBRkZMWKE3cGI5JaLXnfddXuShoN9pHr6v//9Dza4J/HvIVQgLhfNFVDOY8eOzW6SwtiTKkD/p+WiWcceysx+A2yK6xHF+KMjy1wUTwszY46RqCk6hf84oPy31RQ//vijuCgaU/8XLVoUz8vdN/Huu++Kb9x55514zKpfOdB4rv/3f/93+eWX46kEDM/zzz9/9dVXz58/H2e0evXqxx13HG5o0viJEN+F15s0aUKEbdq06dy5c4kSJerXr88rRHLttddeeOGFBICS2Vtr1649/fTTUUmEef3114899thGjRq5+7tAbuvVqwe3gdOS7COPPNLlokjdZZddhrWDKnTr1u2AAw5wHYvMuShMpnHjxldeeWX58uWLFi0qafd8+kf6b7311u3btyPeRYoUsfihhaVLl+bdJ554okWLFu3bt4duHXTQQS4dJcGUGGmD45FHTU+K4KKrVq2i3ChzCvzUU08lQspEjyiTww47jKYHwXjooYcoh6TZoUDuuOOOMmXKEPPUqVMpOv6cdtpp0ZF7u3NRKqVr166UA3es94FklytXDpa1Y8cO+HCpUqXeeustPRIX5SutW7f+y1/+UrZsWS5r1arl1qPLRWFrlBhhevToYQSSlFetWhViFlFZVkqqtbZt2/bp0+eCCy4gO1y6rnOEXMGLaAKEJ8tU0NKlS5N+BT9V0y/F5L///vtWrVpxefPNN1uaH3nkERiXNmqOaEqwUNgyJcCdOXPm2CdokgQmDV9//TVFgfRC9fUoWiyTIiLLcEXaLxGefPLJCkx21Bg1kBtWDhMmTND0PC1zpVFL2tu1a/fbb7/lIcK01foHxR+Fi4pUHHPMMe5NrfROykUBYpn0/n7DRZ966ikygqjbndxy0WHDhtGu9yQNEVyUVnb++efTjvYk/j3EnnDRTZs2YbPye8LzHlZBwXPRPZeZ/Qa4ATgSgU7kGAb8MegY1pzfdevWuY/gWRgdpPfNN99Uf7Hna4wPUgCnqwASnGUuqsm3NkKCOy6SST7JD5c24oFXKi7K/W+++YY/b7/9Nk9XrlyJn41v5C4ljbHX8Y9//AO1G56ji+MrSeUXj/Pwww/X06+++gqX2nawwFEmcKqJW54/yIM/jXJZtmyZ7kBaeAWqYOd54HwXL15cU8IQDy5hFBYDUleyZEncaPVowE+qVas2cuRICzBo0CCXi/bs2RNipv+4yKS8cOHCNvSUORfFY5asIudcduzYUU+hFlwaZ4NuwSftXSgHT+HAUqavvPIKlyRJT1EQhQoV4tfCn3nmmRFclEgaNmwI97bC5yk50jAy0fK6++mITMFJePeWW27x/OYMaYyO3Es2LlqnTh2Xi5599tmUrcJT0fA0s9/iokgOpaeK6NKli3FgITBH97333iOAmyPUxYknnhiRKRdUMa/DXW18uGnTptzRLIy0ckUT0JBd9Fc6depEMGXKy/FaevfubQGQw3Hjxul/dFMCnTt3drkoSUW2UZi6RH9CCerVq6fLaLEMI22WqRSXOno5bdMmFYeVw+DBg7kD1VeOYJvq2nj88cfzFuF+CeOi2sToscceS7pV8pIlS8aPH//kk0+GV8oh+ZCi55577vPPP9csEgPVunjx4rFjx86ePTvsTPz6668ad3rjjTeyy0U3bNjgKq4AjIsiA3g5NIHwqmCkbu7cuWPGjHnhhRfwGTLPcgCUKiJEPC+//HJgIrHnax6axiOPPDJv3rzNmzcHnn7xxRdqX+vXr0doZ86caTMFKFiac58+fchIv3793snBDTfcEOaixExSScP8+fMxSXZ/ypQpqESYpN61R9G1BlavXo2cPP/88+QoFRclqUoMypzIUXRKs6BuKSTN7ti8CZQ8l24XG8qf16Hc5CJV/4KL7du3U56PPvooUp2UixI/EmKXiAElQ46wNegxlQOF1rx5c9698cYbCe82isDriMqLL76IoSGdmFq+m3Q1KYVGJU6cONGNKlUVBBBRAi4XReYffvhh8h6OBweG+4GblM/kyZNJQ4An5CHBa9asUQ1iF95xIP2PnOvSpjh5voafPn06xW5m3YDUIV1PPPEEcbqDB7Qm7hcMLUkLeRHnnHPO3k7IPgqESvTK1jzadnE0Gc1XtXWU/CIkmhiVFGH1mB/IMhdV0s1+0DZ0J9B7gQL6+OOPNWRKEWj4lBKhdCz/EfYsRsEjFRd1F7nhXMInZbOhSQ0aNHg4B3fddReBK1asGPEJlKxLOXAgAk7/Nddcwx01Ks0Qs7Eg4frrr+emthYUFXRbkbteFCUrf91SCN3ijm3Llof1olhEl0Sh5XEIbIO7Nm3a8NQcmsCcW5oMl+eff74uIW/169d3vxU9R5d0Qh4edgCrJ8DKlSs9n8kULVoU26PArk0KQyTZNVHRkXvJuOgZZ5zhclFKHrJhT+GWp5xyiv7buKg9xcfSqNqKFSssfGC9qOI3FUGdWrdCWvzvf//jXWiA3enatSt3NGUjrVxlyEWJjWB43nanXLly5Mumfpx66ql2oGh0U/Jy5iMZF8VFCxCD1157zTzIaLEMI22WQYA6BhIcVg5aTIhDY3e0KNEO78lthPslxEVxMatUqZLIQf/+/S0ABrRZs2YdO3ZctmwZrKlIkSL82lPoa9OmTbGbGFNYB8zfHkGlaJX33nsvTODII4+sVq3au+++a0+hcyhnChmDO2jQIBpjFrkofMCt9wDERdFFjRs3rlWrlgbMBwwYYAHw+6tXrz5y5Egy1a1bN9q+m/KILAeA+aDo4PDQWnQpcfKKPUUj1a1bF18cknDllVeWKFHCND/hmzRpoo7CUaNG8aLUkX0LZwZzpvkUFNpdOVBtulyU+HkdyUdvt2jR4oQTTpBrhNIjyxRdsWLF9K5IdXSt0ZDbt2/ftm1b0kzDbN26Ne54Ui6K9sY0kJg6deoQOaYQL0s6BGi2PGH+7//+j0sMn/X/Uvhly5bt27evxXPiiSfefffd+GMkGCOCqozYspVg1Ckiyp9OnTqRX+Oi33//PTFox3Vop+WINKC9IZCUFeIt20SJqTCxg6R/6tSp4dchRT179kSpcgfWhDjVrl0bqkaRWied5/NA3Aa0GcpTndE9evSgNFJVQbgkI0rAuKgsiICpMgKJLGH3+QqFbHHCIbt06dKnT5/Ro0efeeaZVKK781DmCcbgUtSqRCpXcnXbbbcpGTNnzhQXpZCJh6/YKokRI0bQDPm6lDzugfnnq1atQmZonp9//jneC83TEobRITBpS1X7LjTHCnFFlsgdBaipxfhjJJXKReNZgWPmmjdvfu2117ox6OCD7t27Ew/ZbNWqlcs81cE6bNiwTBLzZwP06q233kJi0fNezupIdKZqWasjaek4WoTEiSLwl19+ibR8tzv+/e9/a8efghl8ziYXNWJtbhCSF+aiFAH55yZFoFb99ddfK9jq1asR4g0bNuhyX9jsPoaQCReVeRYDOemkk7DT4S6WiDMnA1w07PTLvoqBaKok/pAbw+OPP57IGV1E3wXstMtF0cv8504gebY4LW97FwU8bM/Xs2h29Kn2KTF6FuCWLkGiHRUvXjzgGkZzUbT2X/7yl3Bpa6wPgyr2CNdNu7m8uKjbuxwduZcBFxW2bt2Kw0fFkTsrpaR7F6nTwUQrzEUlG5g6XeIuZN51F+aibtmmlasMuahSRU7VkTx//vxDDz1UIsfl4sWLcV8sZHRT8kJcFP/Dui3CyEQsXaTNcjiGPHBRSHihQoUOO+ywvEW4X0ION6QCmoScQDA0ud26jaBDbmOENMKabDykfPnyGmf2/LFx0xjoHFxzG+zSykZKXrNUsLkQJJf+yeXNGxeFPzyRA+gEig4yk5aL0jTEf7D1aGmaifXL8BVaiv5zEx8aFmevp8pyAOSdkKaRIDOuktEkFHelGX4wd2x1ovY+JRli/ngsmDPuuMeTqHd14sSJgVIyLoqrjcDbJJTXXnuNpzjlFp6Mu/Mto2vN83szyYLNF4NxESDVHF2NdbtzdIm/Ro0a3KTcdGfp0qVcEq2FwTrXrFlTdQFtpird7RWoVsJfdtllSb/4wQcfIAzu2g3N5REXRZVR1zKCxkUpK3f2R+/evW1XhUBhJn0dr1J3UIYawZOJRwFanFB3zfERNGHHYghUQQBpS0BcFEmD3WHIIHIyfPXr15efg1XS/kYuF4WF2nQtRKtatWrIiS3PyTzBSAIpVIMSF/X8WtZaJHdwG30C4dT/F1988aKLLrJH7dq1Szhd8AiMzaAh/iZNmlhIKCWNcfjw4amKy4Dko9sHDhyoSxoRDdxEEUNALtwDw2HsAZNKyz3hhBNsRJ3cFS5ceMiQIRZAra8gz0/6A0FDgNB1CSH1qPmqIv80MZejpQJW5o033iCSwOYd+Ycsj4uKjpuyI8Ni5BZgy5Yt6FDxclOyGhddmLOPkedrSZcYxNjryC0XLVeu3IUXXpirT2TIRWWtNWvRHSXwcnrL1HWH3UUDuk9dLqpd+CPG3rPCRWfNmtWyZUtNQhNhy4SLahJsYP5JNBfFn8BqRiSVnB5//PEJfxwj2pyEuWjayNNyUXTi/fffj5XVmDbWNJqLytJgNXWZdB/dRo0aHXDAAV9++SVObSr3KCmiuWhaucqciz766KOE1ERcPofhLF26tDhkhw4d3FGa3HJRCgS3NdV3c8tF02Y5HEMeuKjnH8lg+9/EXNTL4aIuKdJsjuOOO06Xt956a8WKFa2fRZRJ3UncTOw+9Rp505/Ro0cfe+yxvzjA4ycwPp/nyxKcwd0XUJwkb1yUNtgtB126dCESsdNUUcl1hg3aHZ3NYL44UuFOvz/iiCNw1vU/Issu8L3IvrttDyWAjhIB4CnKJJAXPBAygpbTehBxDPeEZDgkdyDbdictF4U7lSlTxjxyPpHYfV16gAhF1xrepKsShRIlSmTORS0X7roViqJYsWLmbkKYjbRolUHAZyV8wll44gId3qBBA/eOJt67c3R1arcxq549e2KPbBQRlWjjwEkX3wZe93JakM3QwdBAWqzDa9q0aUij202J0CJdZqqiuWjaEpCcuKZkx44dUNNETp+j5/eYuFwUOSeF3LRaVsfrbbfdlrcEo7ddLmp3evToYXew4HJ1+FzVqlX5in1di6fMmsCi69WrZx1D8E93rVwm+7mQ1Jo1a7obLBGJ2UHPJwUJfzDWAmC+ubNgwQIrMZw36wb1cgTJ3XOxefPmtNaIgY0/M8SnXLMiPoWzBOcS1ULR0e5ocViT8PoFz1cgC52ZvQWALHPRJUuWkAFth+j56nihv62uLuHlmoW7evVqV4y0rBQea3K/YsUK7uTfAcExcovcctE6deqgLAJSji6L6F/IFRfV+Z/uAjzP30+Vm+Jaol7u2hKXi6qnnCwE0mD7iOw5Fx0zZow5jl5uuChqgv+1a9d2vxXNRbXG0u22d7MjV+PXX3/FSlHIhAwvXzGEuWh05F4GXBSvrlatWiYMabmoJhrZ4pykXFT733Tv3v3mm2/OFWmJ5qJp5SpzLopFh3yS0w8//FCrMTHAOCIYAHeox8s9F8VdKFmyJBlxI/nxxx9VwrnlommzHI4hD1wU3X7QQQfZqtSYi3rJ9i76/vvvIUWFChWyjlrN06b04G86NcR60KAuCX9LZ83FMlxyySVVqlQ5NwT5x7A7nEU3fHbXi0J40nLRhc7eRSLYtrLaHAOEH6ZXxocFTpVlF6hcwmhL9jAwQAlnwq1Bcx3lEIf3pAkvfUzLRT3n+A08H80+cPtnA7wiutZUSoH1ihF7FyXlojhmiJYxRmSscuXKCWcHJrJsHn/16tXdKZqCGiZ5CdwX0w5M4AwXmoyLkUnpcMgbjCiwP0hSLhp43UvWgtwygfmn2qjPAkdw0bQlkHTvIq3UNQMh6mVcdPTo0UWLFg3XsgbM85Bg9Xi6XBS7QzC8L5kPVAqyrUcabMe4BL6O7CkA9jThj+sGtv3PHERVqVIlbYfjxmmi+9xzz7meFU0DHYJpMI1HIWDd3EmRyJXLPLF0lKE7uhvDBZwTBesOjGtPWZw66kVc1NaRLvR36gk46raDT0Gy/SxzUUgmeUAPSrMsW7aMS637QoC0UpbLnx2QW37FUeVd/fLLLxpfzduJhTHyAzKl7k6e0Q60zAZ62Y0E2pBqK10vl1wUSUMfVa1a1W0teNUoNdHdjh07Evjee++1p+Ki6qjm9YR/Yp7b38FNm7q251wUhw+Vau7I+eefnyEXBeoRd+2Bwtv2swEuKoPUuHFjd1osfFsnl9x66612kyaZ8Dd0TZWpMBeNjtxLx0UxQgl/5Y89LVWqVDQXPe+881yumJSLUu84psWKFSNhrh+zY8eO6G3PorloWrnCWyWwW6QREI1v1KiRZhNpESlkwOYZCrnlolrnQ+QWHjGDwMuc55aLps0ygEK7VSBHfNq0aboMK4cwF4WBJ5yBndxGuF8i6T66VAQ3bfdgrOG4ceOuu+662bNnS6e5O81ooWmJEiXuv/9+q766devautwAkCjYSGCjr+xyUVLlDnsGkIqLunc2bdqEAPTp0weZobG4dCtVll3I2Z0xY0bSBCjZ4QONpfegCl72uKjnL8Dr1q3boEGDtOOaW8gBXhFRa0BLWG3AymLIFRcFrVu3TuSMQkNBO3XqhApt3ry557OmgFouUqRIQJfKFhh1MajrKnCETFou6uXoXtCsWTMb3vSyxEXr1asX2HYhgAgumkkJJOWitNaEs1NAgIt27do1HKchDwkOc1Evh/49/fTTnq/Jbc4LCtb1IsLYunUrFaEagQEGujvTQpsCuBOvUF8VK1Z0Z+Rq3YENEvTu3dttj3CERM7WiQKmrUKFCm7DmT9/PmFGjRpldxC8hg72+s7kexdhLorjIS5K/Yp/cgdlQv2KagV2/NKYYoSvnh/IMhclq2KV2gvYhoM950DRACTuqCH+o2UwNprQzO/ePak5hgs5l+gI1KjGKzThx93yRNv/WIUecMABXHbo0GH69OnwFsgYkUR8At+3Ro0adqm9i1w2q9kstjNB//79ubQ4f/zxR8y5re6AZOJhY2hx8REkJFM++umnny5ioJkhMMbBgwej3YYNG3bKKafY1DVNC7G9W5JCh4vYNAZZL5tfp8U52FSa9NixY0UvcRE0JUm82kYD1K9sw2Val0LaNAbCK3odyy0nVdPqrB96165d+hxZwDjhC6LibakSxlITvTy/05Qy0bmXSYGVTew+ezk6cnDOOeckdu+zx6dJ5OxMqynHVC6tG6lAbIoXL37ooYd+8803lAzUMcCUyBrWyx0/x+8MjOQIcjpxCu3OzJkzqXSqIEJ1wJkTu+/lI2/Y9vOMlivsXMLvWuZ+2mOoxPxd3nvCCSfgTARW0kY3Jc/vTeDSDq1BWigTMfzHHnsMGaNqkGE9jRbLpIjOspczy2D8+PGbN29+5plnKL2EP89KQ+5h5aA70Am9zv22bdu6085zG+F+iaRclJJBhm2fCZrGHXfcIedVguqeFvv999/rNKyEP6tfb1WvXv0vf/lL0i+uXbuWkDbrVciPM11SIS0XpboPO+ww22clwEW9FFl2QYtIJJvzIvAhnh599NGB+xrO0krdbHFRnPJatWpRiV6Oho/gohG15uX0TgZmiuWBi2ooUqSxQYMG69ata9++PXdIJBbQdoBDrUGZEs7iUgE7nvBnowSi1fLywKGymXBRz1fjWkuPYTIllhUuiiCVLFkyaflY4FRcNJMSSMpFFcAWBge4KO5QwulpCiAPCU7KRTX+KXcCbmlzsCdMmBAQ2jBoUAMHDqQu5IHkipA0bdq0cOHC7t7X8mRcLw5eamO/ODaaoj9o0CDdOe+88xK7d4VrCpsrRRqadrdXxFJcngOEMO1R9vs3tIlueI4uHpqNi1pXNVWw0Dlr0/NJnFZWFjD/yjIX9fy2p/FPLZ+10RJtnJuKi/7222/Ilt18991395HNo2MIGzduVId9vXr1Vq1ahUmTdcTHnTVr1pYtW9CGhQoVUo+g9Bd2Bd0qpwFjEzFxC+KBdVRIPGC0/4IFC+SeVqpUady4cZpfqv0M8b+tmWmjwuuuuw7PA6WmjkAD7AJXhldKlSrVpEmT0aNHlytXjsBigLAyuJzsjSyK+uowQrjCYl+YkECcAmH4ovQ19h7mRplceeWVCX8BFYqVBPMijlrCHweDv0kplylTBvHmkc4LxZQi6ngYfJ1LSNqIESPkd5IGzactX748MXfp0oV40MKrV6+GcalweIT3YH09mmameG6//Xbz0nRkJa4GtQbVTDWmR4GQcu1yBGN3x4RTRY7W0x593L/00ktp+OQFS6ZuCKyC1v/06NFD75JsAlAF/D/22GO1nT0eG8YJdte3b9+ePXviG1mn6fvvv68xwIQ/LYq8uwmmkEmMu6SBgtWnUxEYMqJqwt0fOXIkpGvy5MnajBG5MgYeLVctW7ZM+KfC2B4zEaDcXOeJag0MSkc3JUwFr6jpQUuMjuJrar6iBEx9DZmIZap0pm1KWgdFXRMA2cAl6tixo4buA8rByyGTOBb4Q7fddtu5556LDLi8PbcR7pdIykWrVKlisyhPOOEEysFGUVwuumPHDmsOCJhGC1977TUvZ1Dd3YJVmDZtGnYWpYQwuP5ifnBR4reeCBfRXBTDgS/uLv92uWhEll1oaWWjRo0C92kOtHeobMIf73JXzAJRMsWfFS6Klk44+yGl5aIRteblzDQJHKGcBy5KG8SMUnQvv/yyxu40/6h///4ImzsOJvUS2NJMg36WKYPK3I6VcgskgotarwqmR6vWbX/1rHBRFRpKNZBaK+ToObppSyApF+VRwpkAEuCiEpvBgwcHvkUiEe88JDgpF/X8FZUJf9mqe5CeOmJat24dCIwDprnZViPwFln8O+64I3nphIDHTnjbEcDz+zS195LNcEGxc6nVpKg1TKHORlIG0U6YA1vu6/niillM7L5YFMYbfSLDnxwUsmbh2h3t0QMXozzFsGyGBSp3ob99jwXW5Fb3rPuCQfa5qOeLFEoNXZ/bvYB37dpF04WXx4uS90GgWdTFmyvAN9Br+Xpa7AYfqZ7S2NS1ia4Mj2L99NNPWLLA3KdsgVbg9oBSFKkOMUsKCg3mpqUXAc8p4ouokkA2NXWT7K9cudJdyJFbJI08Q5B3d9YoxRJo41hiWEeuNMaKFSvcIUdBe+K7E1TyjFRyBaP77LPPMkxq4IDEnTt32nm5ew6sTiaH/mWOiKaEcqaC1OWMLAWyH1AONkdX/CEpB85VhPslwp40WU7kzC+lyagXz5SneqzUh41jof1OBHmZ2pYG95H/Rx55pEstJk2apGWB6sZy99HFEUw4B0qF8cADDyT8A0Lcm+Jaqbhox44deSt8P5qLPvnkk4ndd2qtVKlSqVKl9D8iyy5Q5uq1dBOwdu3aXr166f8FF1wQJlRHH320rSPIhItqGnkEF1WPm31F8yncQq5QoYK7u150rWnmgrvOHP1ZokQJK5wANDKW9ABGHc4BHZW7iXRpOK5Dhw5usOHDhydCu+b+/e9/p0bCW2tyRz2n7rZGOmTYrYUAmezRo4c75AAbt03yRo8eTUj3JLDw6146Lqq1D9Sse4bnoEGDzPMOVEEAaUsgKReF+8HqzboFuKi2Uy5WrJjr/cMAtdVQHhKciotqL+gyZcq4xYVoqa9Zc9GFzZs3t23bVmbdJa6obr7lLsuknCMcOZS52wdEyL59+/71r3+FXprbo6lMNHPPL97ly5c3bty4dOnSGIhXX31VU5YoPYuTAmnTpg1yjnX46KOPKFVad5EiRVTmEP547mQYGFZ3nI8mpkudWvLee+8t9Pcx8vw60jpKtwUh1dyJ8KjzCfnCRWPEiBEjv6FD2AI3YT7dunXbK+mJYUi6j26MADQhzdx3/K127drZSUX4EBrkx3HEVxgyZIgGamA78+fPx2+rXLmysQI8zsKFC4td4Fzi0xOyVq1at95667hx43Dd8Cnlty1evFjj5A899BCvr1+/Hn+RO8QG80m6g7/WdBGn2w+lFfWFChUKLCojqVpMkXSXck3Js11G7Y7GkXTUFu7yokWL8Jn4ruaPvOMjIssBaCtR0KpVq/vuu++WW2455phjbAIFfli5cuWOOOII6x179tlnDznkENvQVYe+uEeDiCi6uw9oHM8Ow/ByZtrbmYd8lMvjjz8eWjhv3jyt9YVq2jINzcPX3DGIfXStkWsR7E6dOkFU8Mj79etH9hP+bOTwjoBbtmyhiqEu33777ZIlS9y6WLlyZYCmKneB3XGRRnjFgQceaNsWfPHFF3CbqVOnhgvcy2GefJHM4g1TfRoTa9Kkie0soNUcL7/8si7hde5BHWeccYbxOo26t2zZkqigVeosDrzu+UNkCWdfPQKTa8iPHa1Zs2bNhD+7qnv37lRN69at3bWIgSoI5ChtCUARE/4cInuFlFBNbk9ogIt6OZ1BmqIFk7zhhhsQEp23kYcEazFReAMImiqRhOeiq1MDyUG0UCyQ2KOOOsr4KlVmk860954t3NCeBYEt7lxI5IiZ7H/zzTdYYQSPNLjbYuvrfA7tASPVNA0KUJPFqD54JpGgQ/hP9rlPFcBOeUU78Wqx6D//+c8FCxYEtpWOYdAsVAoN9agDXUwD2JGZhBEvBTZEYQOnuV0qvOeIuWiMGDH+MMBBx3PChONJ44gEuml5ipXK10H4GJlAXDSwRVOMAKAlLVq0qFKlCn5hr1698DtHjBjhBoD8iFPVrl37rbfegiPB/fDVkH+cUfz+Zs2aTZgwQUfeu6WNM4cDp3fx9nBV3TVUc+bM0RRoYqtfvz4uXbFixaABs2bNCowzwCu6du1avHhxRXXqqacOGDDgP//5Dy6piJPir1atGh6t9h3VzfLlyweaIZ79oEGDFBUfnTFjBs4usWmGf4MGDXQgnvgGwIXlQ6JJ5BQHNzrLAeC5aqQu4e+LE5gIvXbtWmgqnjrx9+jR47zzzrPN/3HdxHBIGPyKROI0a7/ZGjVqaJ7zqFGjlH2Yg4aYIKUKQ01pdQOMUStEKB94BeV/yimnaOBIcyU0CJzwVwdo4Ci61j777DMdc6oCwSknDRAbSiNpD4KOJCGevn37Bh6REpd5QrGOPfbYcAx8HUZB5ZL+22+/3c4nSwqqm+JS/UJILrnkEi4hZgg2nA36TVFr0QqEShXXpUsXiuvGG2989tlne/bsSY1Y7wBURD0v5PH5558Pv07aEB6xcRJGdr766itbSHz99derQvG8tX4+kWy/q3AV5KoEyHK/fv2QAWqNAFdeeeUFF1wQWAsa5qJwtrZt26qbKRHaFDrzBCNFGDsaHZeUM8wtMOnp1ltvDegTpZly0zoO9ZW4WxnRDOvVqzd06FCYIXmBJ1srVldLBBf1clZyqs8FAq8JF9Y74+VMYKZlaTsltA2tBv5pM4FJW8LvKSMG7favObq2dbP4PzXidgPFCICChXzamscPPvjA7UZE3uwR8uyuiEY4dd+2NS4wxFw0RowYfxjIvCX8PZC1QXeMfRDaQDiwjXaMpMDXXL16dapDStavX+/uWMOlpuvzFv46niKcB7cj6XYdeKsff/xxqp081qxZI38dL7zADjRPC3K0atUqd2Y7PERZyCTLLgi/cuXKiN34yfiyZctytW4iVyC1lL/Fj4MI23SpBZXuzsYUomuNpzZVMvqgAcIQMum+G4H9eDyfAqWKh2Sjad0zNiLwyy+/LF++XMsQeCV6IYNKZseOHeTX+gIMeMOffPJJbtd5JcX//p+9N4/XqXr//28dPhzHdIyZMmYWMmQqhCJzSCpkTMkUhQxfc+Z5nso8JpLxHeGNDEU4yCwiCm/zlLp/z8e+fmc9lr3ve5/7jKb1+uN+3Hvttdd4rbWv115rXdf//kdSPk+X+OwCGyJsAeqLIPlU34WL2px4ea1Vxz179vhbfYpmgQWXL1/2xyhoVdJ32iWSHmGG2b17t7NsNmurPnHixAl6U3oNou7RXAcLaEl9tuG/beo7deoUuauSI/C2wxrMh8bFRiBgDkH8kDTn13lEml5GQmJkfMUIDBc1MDB4nPDtt98OGzYsZs9JGsQgvvzyy17hGDVqlO3ErIGBgcFTAmY/+Jh+DvPpwQsvvJAhQ4aHXQqDxwOGixoYGBgYGBgYGBjEANSapLjX1v11PSUQw9HK7ZyBgTsMFzUwMDAwMDAwMDCILv7555/Q0NDChQvDSOfMmZMzZ86oGZ9/rCG2u8TgkIFBhDBc1MDAwMDAwMDAwCAG0Ldv33z58pUoUaJZs2YBHrV9YnDo0KFevXpVqFDhlVdeqV+/vu4/xsDAHwwXNTAwMDAwMDAwMDAwMIhrGC5qECguX74c5Wfv3r0be+YKn2z873//CwsL279/P7/irVjhzp07hw4dOnHixKlTpw4fPiwGNh8u/v33X91KXiAyE/eerCIL3QydzelFHLf59evX4967t1jF9IdHQeoMDAwMDAwMHlMYLmoQEPbt2xcUFBSFk+izZs1q0KBBsmTJlD9lg0hh69at/fv3F2drrVq10m+dO3euS5cuKVKkSJs2bdu2bXfs2PGwCum1XBG2bNkyQ4YMX3zxhYS4y8zFixeJWb58+ZCQkDgsZiQAy2rdunWmTJlo/FdeeeWTTz4ZMGCAcnTmDfeiGQd2KX7//XeyrlixYoIECeLMnP3SpUubNGmSPn36zz//3F+cOGsBAwMDAwMDgycShosaBAS04YIFCw4fPjyyD54/f/7VV19FYTVcNDpo3rz5Cy+8EBwc7FxpbNGixc6dOx9KqXRcu3ZNzBUoLuouM3///feJEyeSJk36f//3f3FYzEBx7969EiVKFClS5MKFC15rQbJTp07x4sVr2rSpirN69eo8efL88MMPsV2Yu3fvnjt3LkeOHDRvnHFRqiwO4ly4aJy1gIGBgYGBgcETiZjnoqhNBw4c2GohLCxMd9l8586dgwcPEr5p0ya0Z1RV2fx29uzZn33h8OHDMV48g7jHJ598EhtcFPl5So7F37hxo3379lOnTqUZhw0bZrtrWyx9iPjmm290LhoIINiBc9E1a9Zs3rw5SkWLNL799lvqMm3aND2wX79+r732WtwUwInatWvHJRf1Wmvd7lzUwMDAwMDAwCA6iGEu+vfff//4448//PDDxo0bIZz84VL8LP3zzz/bt2//wQK0RP4cPXqUW8ePH//BF6CjMVs8g4eC2OCid+/eLVGixFOiJUMJFi1adOvWrdDQ0KxZszKU1K3r16937tz5IZZNR6xy0RMnTlD9//znP1EtXeQwdOhQ6vLZZ5/pgcxv5cuXj5sCOPHmm2/GMReltQ0XNTAwMDAwMIg9xDAXPXPmDBxy27Zt9+7dQ2/buXMnl1BNbqFCCcMU+ytolnJJzBs3bvyl4cKFC0JWSS1mi2cQHdBlCxcu1EP279+Pyj5mzJgNGzYcOnTI34OKi/7555+zZ88ePHjwrl27bHG4NWPGjN69e0O69LV0n7lAwGrWrEmatWvXnj9//o8//ugv66tXr3711Ve9evWaMGHCsWPH9FthYWFz587lz8mTJ8eOHTtx4kTZjXn//n1kb+DAgTNnztRZn9eyYcOt4cOHUwX4oc2KzKlTp6ZOnSoJUtoRI0YgzLby7NmzZ6iF9evXQ6f9FduGbt26Sdk6depErVesWKFurVq1avny5YEkQgo0RY8ePWhn3bwQoAGHDRvWt2/fZcuW6VVmbJI+nUVNyZQI1NqW7LVr15YuXUrHLVmyhD82LuqUGbB3795Ro0bRCDSUk4v6LMzRo0eff/554UX0uEwpXuuTBPn26dNn2rRpNpKGRI0fP37IkCGk89NPPwXSRDpIluwSJEigt7bXOr6rX8r3Nduzq1evpvyI3O7du3W7R4CSUB7+7NixAxn78ssvmSf1CC4SGyEXJa+NGzf+/PPPJDJlyhTJyD1Nd6HVuSiDjq6cb4E/XPpsgeiPAmRs0KBBkydPRhLMK8DAwMDAwODJRgxzUTQt9BK0ELkUaiomVdCB9KXOW7duCRd1WtE8cuQI4fv27YvZshlEGdu2bXvjjTfQSkuUKKEC0UdLlixJF9+8efOdd95p0aKFv8eFi6IKp0iRInfu3B4LkCIV4ZtvvmnSpMn3338PAciUKRP85OzZsy65QEV69uxJImjnixcv9ndaEl02NDQUgsSzcJIkSZJs2bLFa2nJ7777Lo+TMqyyTp06H3zwQeLEiQsWLEi+lKRZs2a1atUiQrt27VRqp0+fLl++fL9+/YizadOm/PnzFytWDFn1Wrp+hw4diJ82bVrYRaVKlerWrfvMM89kz55dNgUIeJYUeByukjRp0vjx4+fLl69MmTIRtn/z5s3lD9QuXrx4lStXVre6du0aiB1a+GfFihU3b95M05UqVSplypS//PKL19qtQKu++uqrMNXDhw/nyZOH1pBH6I5cuXJRKWgVgW+99ZZcCtMQwOcLFCgwZ84cHqcjcubMqbioT5khuy5dulSrVu3AgQOUhKzpFMVFXQoD4REmRr+Tkcwwv/76KxEQHor6yiuvUCn6ReLTL5kzZ2a2gUWPGzeOgkXYRDZAEZFDcqTBP/roI2cjz5s3TwxK6WunPFW1alUE/vz588OHD+duSEgI6bRv357SSoMgGx07dqxRowZl5hJRVI/7k1iBOxeFbSJvsoubvka6INIwPX9pBiK0tnVRyC2RqbjYxLa1QIyMgjZt2rRq1YqkGG6MR/laZGAQ97h06VKUTXzfu3ePsSNzrD9wd9q0acQMPFkeYdREtjDMRePHj//zzz8j++AjC94d8+fPf9ileABMWcyH0fE18NAR2VZFK5s+fXqE0aImtAZPG2KYi8p6ptKWmP5kv+6///577do1LtWCDIqRcFHC9RSY/QlEW4rUHG0Q2+B9ZuMVaIoDBgyQ/3QidM7fs8JF33vvPXEOsXfv3tSpUxMiyymnTp3Kmzev0lZRqbkFIXTPJZDdg1WqVAkKCpK1NdJPmDAhhEpucYmWjF5OYSQENZ0EoQfKg0Xp0qWDg4Nl3QYB5hLdWiWOkEMz0MWVoGbIkIHsZs+eLZfdunUjQTiAXEKYuYS2ySUEj0t4lEv5BXJYVF1C5HgQYiOXLs2uAC2EHqihJztpP/74Y6+1Osf/Pn36yK3evXtzqZa45YRq2bJlRY+hZWgQekTuQkgyZsw4evRolRE9pa+LOmVmzJgx6dKlU319+/Zt3XaRe2Hoay7VHl1Y34svvggZlkukiLvZsmWT7m7bti1cSOULxY2wlZz466+/qLt8OkmTJs3MmTNtERYsWGDjovBAQtRqXoUKFbhUCsrRo0e5TJ8+vVqnLVWqFCHKLYqLxHoDWBel6YgA00Nm1Iq0e5ruQquPsl27diF76iORvxaIziigobhUK88bNmywndd9IsHgQlZViz2y4KWMaO3evTvus477Jlq3bh1zSBT8kPGmQOaTJUtm+2znhHzHCXBXC3WXL31RmMratGnDgx06dIjsg48gmEnkE2G+fPkedln+fzAlNmrUKH78+JRKDp09dohsqyKNvNaJ736+JjpCa/C0IYa5qNBL9QUOHUtCbPvQUIz27dsnS6b6Hjb+E2J25z6agLzpvCJ37tyZM2dWZMBFRxEuunHjRhUycuRIQurVq+e1TO8UKVJkYjh69eolqr97LoFwUXRcGKa6TJkyJdRCXaIu5MqVS12uXLnSluD7779PCCTHG27Jxua7omXLlgQqimLbbrpo0SLuKiuyMDSdSu3Zs4fLLl26uJRfIIdF9UvFJMV0bYQpwNk++ugjdckomzt3rgwxUmjXrp3ie3BFEl+/fr1cOs9/5s2bFwIv/wcPHqwTLZ/xdZm5efMmXYCGp5dNbzT3wti46Pz580NCQiZqoGBEOHjwoNei6AkSJFiyZIlEjrICTVvNmDGDYgsjrVu3rr6B/L///a+Nib322muEqH2nIudr1qyRy//9739c6taPPvzwQ0LUbhF3iY2Qi8q3g3HjxumB7mm6C60aZStWrGA4OFVzZwtEZxTIx4uKFSvKehSN776y9GQA8aDWgeyPeLigmyhn9+7d4z7rOG6iefPmwS5sBzQiBR6PkItylzegcwe7PzARRU2t37JlS40aNR6Wx68Y94e8efPmR4GL2ur13HPPPb5c1Bv5VpWPvxHaeoiy0Bo8bYhJLiqn6YCaXtFTnVwURQ0NQxY/5eyowoULF8TcUXReAwaxBBsXhYMxy8SPH79jx46284c2OG0X/fbbb2riK168eM2aNZ2Wq0QG/OUSuFUVnpowYULPnj2Dg4P18tu4qDNBSDIhog3LlmDb0cFZs2YRqMiVTQu3EbPZs2dzOWrUKLk8e/YslyNGjIiw/OqwqIBRRrHhXTC3VatWQZLdH4c7BQUFReiMZ9u2bb169apatSqlUjtqnNxSryOcijbUE3Hnooxr7kLP9Ed82i7yWRgbF4WE8/p3io2sMYaFhQk1rV69uu2EZBTAhPbee+8JHdUXFZ1MrFmzZkpmAJyfS8WEnVwU7k2I7cCzP4kNkIv61ID9pekutDIoChcuTD/6tBoVIReN7Cho2rQpIalSpZo0adJT8hbghThu3DjnmZSHfkpl//79+uW5c+cYvHGz1dNWd39NFBtYu3Zt1qxZ1XHoqEHGtTsXjSxkKD12av2HH37orh5EFidPnnzoXJS3qjo4I5B1xceXi0ahVXkpRMhFH1OhNYh7xPC6KPQSdfD8+fNyiQ7HpTrE5bW2+W3dupXAn376ST9EJBCOqo6bGjxSsHFRsHjx4jRp0jDXPPvss99//72/B51c9P79+6RWpEgR/oeGhtaqVcslX5+5BMJF0WWHDBlSt25dWdtMmTJlFLjonj17vNY6G//Rj/X0N27cSOD7778vl+5aOByJ8ufMmVP2AMNj06dPr5NMf7C988Do0aNl+atr165qR7E/oFC6L8AeOnSoSpUq06ZNo7nGjh0bOBfNkiULxEZPyp2Lyu5rfY3O62g0l8LYuGidOnVSpEjhUnEmk0KFCsm320A4vw7k03Z2AHTu3FnoqNrX7WRizHUw//r168t2D5hV5cqVFaeKkIu6S2zUuKh7moFw0datW0P7edA5M0eWi0Y4Cmh5CHOCBAl4qlixYlLmpxCLFi3SN5nHPZDM3r17P5SsH2LdL168iHxG/yyi4aICmfOjfOzWJx4FLtqkSRMmOj3EcFGfeByF9skAegIkC4WE399//12/de/ePRQttA5e36hJ+nc31B7UG8I3b96M6huzI9cdMcxFbTtsz507J2Z15RKdA/WdkMOHDzu/eUNNZWXjxo0bMVsqgxiBjYvKx06EtWPHjvHixUuUKJE/XuTkordv31YsLk+ePJAKmzlNRovYSvWXSyBcFEqQI0cOlXJ0uKjQP9uRG9kuq3iOuxbutc76kyPkBA758ccfnz592qXwAtthUQFtkiRJkty5c0MSIkwB7Z9ilC5d2hYus8zPP/9MkyoLBJHiosL0GOMuVdZlZtmyZdxt2bKlXgw9QffC2LgodefSaZBZtviK2EBsJk2aJGe3nBaAXcBc5Pw+Ar1MlSoVSSnLwE4m5rW+UKRJkwbZ69atG7RK3/oRIRd1l9iocVH3NAPhorQ8Ezv8kMi2nSyR5aJe11FAIWULNC8IWRUvWbKkv8o+wZg8eXJQUNCgQYPiMlO1d4kuaNGiBY2/ffv2uCyA4KHUXaFTp05Iry7kiOuP4RCmgW6nQtThkQMHDkiINKPORXkKSrZkyRLb2PFaHwqd9ud5wa1Zs2b8+PErVqzQv9frav2ff/5JgjNnzrSd3/YHJg3dCprXWnmWowHoqbNnz/76669tawNMngz/v/76C1WNaZa6bN26VW1MpeRS3xMnTkiIrZWkwDSmTNqEq09OZLRy5covv/ySIp0/fz4QfY+ZgdyZzJld/bEmKrJ8+XLkx7nhTsD0S74kQgTbqTGvZSB9xowZvCYoksviP63BxEUBcubMKfWVKUtxUZoICaEYPr/Oky9aPndXrVoVyHIxFUcMpDrIGC/HnTt3qnNtTJ5z585dvHixs77EIT53ERL4hs89JoG0Ks/SU7zynOfmIstFXYSW0sKapkyZQoHFHqQOdAx5fdNidDEpqOUuA59gLAiZQtjkj/qqi2ot/k2U301+hY7yKyHqFn8iXO2IKcQwF0WHoAKo7zJaYNhcMiS8lqUTqR6X9zSoQSJOX2wuEwweHdi4qH5SUY72MdH7fNDJRZmsPeFGSpin+G9jXJ07d5YJy18uGzZscNIAHbINuEqVKioE/hZlLopgo4unT59en9MhqAkTJlT+RSLUwnv16mVTCCKE7bCogpwzRHMKJBHxhqL7Vrl48aKYCJIzseookZh+DZCLynbKgQMHqrsSv3///ipElxlmw3jx4qVIkUJXPkgwfvz48t+9MLJNWl0K73rppZf0A5zUURyZ6ILBLERM3QtrIEeYMmfOjIzZAgsUKEBSSgF1MjFmOfR4f29Kdy4aocRGgYtGmGaAXNQbPvr0Lco+WyA6owC9HHVQ/vMGkfo+wZ8mkdXWrVuXLVtWqYAwhKJFi8ry+4svvoiooLbWqVMnXbp05cqVUw/CbdKmTeuyFUUBAWjbti0dxOP0nW6dYezYsVB9JljGXc2aNVEEvdaaZMaMGaUAlSpVatOmjdc69vzee+8VKVKEIa8KwK3SpUvXr1/fa80nTOPJkydnqpcIcBumHQaR86j2t99+26BBA4YzBUM3TZkypWTtrDsatrOJFLjbu3fvxo0bM5VVrly5Y8eOcp4ZgWFmbtasGQWW062kTApM+Moumk+QYNKkSW1LsujoYmSIsslu/3Xr1mXIkIGQ119/XdmQo5q8HWhJeUHIuJ4wYQI1TW+By4IFC8pkdenSpQEDBkiyti9HkI2XX36Z5oWOMpToZfXeVGr9iBEjQkNDZVZnOrVtpdZBd0+bNu3VV19l4lVrU7BcsYjer18/BmamTJnIxWMZmROGxpuXzpVAZIxeFkopIiEfMZnMSZYQ3pKSLPM2gqqmCPRaWlu+AyJ+jHr5bgiloeSUivemfHdQaxX+AB3iEV40KJAUuHz58jbWRMdRYGTgu+++Q4BpwGeffdZmFAq+Xa9ePWS+R48ezIH6ngtq/cYbb4ipApqdztVfajagvkrn0j69LMiRNOGiaLCFChWitAgSlzbnAnAABtrQoUN5tWXPnp1BrawhOIHgtWzZkjHlsXbiMNCQHzqLy0aNGsEQ6tatSyPkzZtX+k5/qVG1ChUq0Ca8wiZOnPjcc88VL15cvbYCbFXeYshMt27dxo0bR2roP7bzNZHioi5CyyBCIJmICGTIoA+oI0WMtVdeeQXpRdh49WfNmlVsxadJk0bpXQY2MAXJBlX5zivEil6W0S3eNNHA7969S0zEgMiy40noGyHwMsTp4MGDXNrEJvYQw1z06tWrsvL5swVh5EKslUNRG9QqsLhyEdXf4FGDrGSii6sQpg/1pZMpj1nJ30KfbG5ULAIpr1WrllpjROKZ1DyWoV1UE5SP6tWrM4G658Jrw2OZvUX/QOScVpflbD1ckXc5WfTt2zc4OJjXDDOssFxuZcmSRcUX20U6JRZqpD6OiFlXVTDy5TWgK9kUlWlUfXCVo3HkK5doYOQIT4Mv0RSUCoF3PxHHXd6vzqU/aTSP4/yqP4jbTyZ0tLp58+bxMka9kPXMJk2acKthw4Zc8toQLyO8sOVr/fz587nUt+rxJqCzRKNFM+P9lChRosWLF9OnjH3xWcJbTb64O2VGjlOiw0mf0ua0CSG0Feqse2FoeS55Y5E7HImZlO7zWGZ+0ed4aSFRSt9CH1IWg9BNKeSCBQvkskaNGigBEX5Y5e2LlqxPR9u3b6fuys2M1/Ij6gm3IyVAIc6WLRuqMG1OkVCz9O0xvBWIr5MKaZDNmzd7A5BYWSqEXfgrM1qmRzuNGUia7kIrNmMUjadVPdbuAEVpnC0QnVFAR8OOVOLQldy5c/ur7JMBse2hzIYLGDKIqGqHa9euiaarFDjGF9qY3uw+wVyKNIquL0qhMuDMtMYlI9drfSmn19SXF3RrbgnJVBBjPMp4G4NdLLeNGTOG0cq4Q6uGxMq2eVRJehweSISuXbvq6TD5oFIz2L0WBxCLL/reb1vd/TURChOyoaYmOYkgvIhnKRJsVmZvZIx5jz9IPiPapblknwtD2NmMhDMhqBA0Zo9jm0yOHDnUq0roCpq3fDmlpszkhMimDyZGBmCZMmVsXJQ5iglWnQ6AzxMhT548cik9SOPAH4R4iN1s3pv+akRT/Pnnn/ItWN8nKSt7aPbiMwkBECoi3z25RFuTTxLMOTSg6Kwy3yp+BZPUuSjgfWT7XCX9q+/0ox91tk8bOj/56Th69Cgd9+WXX6oQ+SimsyamdMRGkTFezUwjusrBBKtPLPIqgbLKJVKdOHFitXMEEsvM41IkWUL0uUeXZpRlPZpdyLyyVoDMIw/qS6K8waGayoi6ExRJqFeDBg1kWZKqMaJFGmWNx2vtfCFEWY5Afug7fc8UtA3JJy+1iSnCVqWtkFi1ukBJMmfO7NFMCXojw0XdhVY6Sy3L894PCgpSQ0lGJeXv0qWLqHmyQ+rDDz90z/qphZiMRSuWFytdKf5NpEl5Heg2fXQgUdxSGoscsYwzRhbDXNRrVUDWP6U51NgTw7kuXFQOizq3rBg8dGzZskV4AnyGqUQ+KObMmbNUqVJfWWBm1JfdbGA65pXGrNq4cWPmkXr16umToNdyZSkzHUBR1m33u+RSsWJFj+UhQ5lLtQFdTdJE+6cMzZs353/+/PnRSzp16iS3IJOoBbwOiSMfO6dMmSJ7O+WQapUqVdQWSrSiTJkykc7QoUNr164Nr5PwmzdvMtVKgm3btqV9ePkVLlzYY+3k+e6777zWNyf5KKiDEOeOFAEvad6vSZMmRU30abuSF3DgNiFgleJHR15jKtOwsLBnn31WXoojR47kFcXbhV5Gm6SVXnrpJW7RcbQwjE5MHAtjl3mNasrLMkmSJLxR4EKhoaG0DwPfp8yghPGOlNOAdBycrVChQuTCH17VLoXxWjv8ZXmBZpHlCBQmSLUUiTdrt27dFAVC8cqbN++wYcMoOfKmL9zxuuVVR3e4txg6VrVq1ajUu+++i8oLaQwJCfnoo4+UpojeJh5ZeNFScVmTQW2VpQAdiBAVp7Si0FN96kv8mTNn0lwSQcwd+ZPYXbt2DRgwQHg7eol+Al+B1ETAUBlRttTWGn9p0rzuQotmLOoyCiWDAl1BPNYA1JRVq1bZWoAejOYoYPJHSukveo28UBYfuv2e2Ib4vFEfSrzhxoR1r7Nea8Hf8+Cpb6ZQd+d+Y8eOZewodZx+R+FWmwhEHWcek0skXKkg4qfH5k1HOlpfkxcNGLnt3LkzqipqIumjR9J3QmlkX4Nue7xp06aIir4BkumU3nevu7OJGA7MDGqRVoDkMAmo7xoMcyZzJEq+g1A8xh0E1aXFxMOQciGmwOuActKYapsig4vByHSk+M/27dsZmOoR4aIMChUiJyd1h9XMoh6Ni8ITmDogeHq+pKkccYtaL8bnBfKlyUaKnBAurXNR2UChs245hKJvC5Ie182qocUSoniCfGbSuah8mXLnoszYTPKKaaD++pzNFHjPIjP6llrmEI/GmsTEPVRKf0o+oqFU8CC6OPyNCH+Hg36UmUeIonAb+SDotZpdFur9wYWLKn7oDf/OqxxWcfnmm2/+rUFmQne3VfJBVucDMoFPmDBBhVBaj+W/XS7pVi5tM6cYwW7YsKFcRtiqiCsDSi+t7NvXx2bgXNRdaHmb5MmTRxVG9qOpNQBxhCa2RQSy0cl57MhAgHj/YJmAVSGyKRe5VQchmcF45yIkDAH1FUZ8cO7YsYMBi56ze/fuH+LQp0nMc1GvtZ5DZWDnzk35Bk8M5DsWLxXe9wE6g/3tt99crPWgDBFB/yLungvvDOYpdxkjTf0LEKMx+sY5z1mI7FPM9TAZBjbzAtwb/WDOnDmo7C5ftWMc0CFZkdBBC+trU4xcZxx3nD17VpYZmb8CkQTmPlpDOs6Wl3th4G/qeJICcUjNlq+IDeU5ePCgzSQmibhsc1U4fvy4FIOUUbiZ2Z3WjJxYsWIFJIpneZWuXbt26dKlEAY4beB+MmNDYmMjzajBfRTct0DZmAfoaNtU8ESiWLFikBxdyGkQj+YpSsCQkSPiKgQFWnenZAPqGmqiUgFnzJgBE5Pt64KwsDCPtVlOVA39vJkou/ry+9WrV2EguvpI16RJkyZ79uywWRkXW7Zs8ViLFWpZvnr16h7tPLkwIt0dMfoQddfdTfmsu62JGL+0A7WznToLCQnxhO/oFrKB9v/pp5+KqENfPREdapCDD2rniw7ZFNOvXz+5RDhlL49aOGrUqNEPlrtsgdN2kawZ6qq8LFeqOFJ3tXDthNMMDDMbIRkzZnSplMrayUXVhmqv9WmDEL0v5DOfbVVENvfK4ljUuKislsMSfZ49sUGMHVSsWFEPtJ1sFLOCtvNByKd85kPOmY091i7WNxwQfZ2JyGN9zRwwYIDToKYTLlxUt10k/atm/kyZMuXIkcNZBnfe6+SikqwupbJ9SXkaZ3RwaTtBKvwtVapU3sBalQmZycFZWn0vRtRsF/kUWhmk/CJCYodCbWsSLqp/RXoUjFc9yqB9mIt4w6oQZhVCaEka33aOVM5FKjoKNdVXC
```

---
