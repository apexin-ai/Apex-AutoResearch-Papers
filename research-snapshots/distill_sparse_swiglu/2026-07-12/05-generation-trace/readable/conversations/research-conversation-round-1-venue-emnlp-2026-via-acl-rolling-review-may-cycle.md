# Research conversation: [Round 1 审稿请求]: 你负责**方法严谨性 + 实验有效性**的审查。 ## Venue 信息 - **目标会议**: EMNLP 2026 (via ACL Rolling Review, May cycle) - **截止日期

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 91
- **Recorded user turns:** 3
- **Tool calls:** 23
- **Original source:** `logs/chats/exported-trajectories/account-2/fd7408d6-e7e0-4bb4-8dde-4202758b928d.jsonl`
- **Structured JSON:** [`7a01791a92805dd14d72.json`](../../sessions/7a/7a01791a92805dd14d72.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-17T08:10:55.614Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-17T08:10:55.614Z",
  "sessionId": "fd7408d6-e7e0-4bb4-8dde-4202758b928d",
  "content": "[Round 1 审稿请求]:\n你负责**方法严谨性 + 实验有效性**的审查。\n\n## Venue 信息\n- **目标会议**: EMNLP 2026 (via ACL Rolling Review, May cycle)\n- **截止日期**: 2026-05-25\n- **页数限制**: Long paper ≤8 页正文 + unlimited references + appendix\n- **模板**: ACL format with `[review]` option\n- **匿名规则**: Double-blind\n- **附录规则**: 允许，reviewer 可选择性阅读\n\n## 论文路径\n`projects/distill_sparse_swiglu/paper/main.tex`（含 abstract.tex, introduction.tex, method.tex, experiments.tex, related_work.tex, conclusion.tex, limitations.tex, appendix.tex）\n\n## 你的审查侧重\n\n1. **方法正确性**：\n   - KL 梯度分析（Eq. 7-8）是否数学上严格？factor (a)-(d) 的分解是否完整？\n   - Gumbel-Sigmoid relaxation 的使用是否正确？与标准 Concrete distribution 的关系是否清晰？\n   - Adaptive penalty controller (Eq. 5-6) 的收敛保证——论文称其为 \"adaptive penalty controller\" 而非 Lagrangian，这个表述是否准确？multiplicative schedule 是否有理论支撑？\n   - BCE vs KL structural mismatch argument 是否有逻辑漏洞？\n\n2. **实验有效性**：\n   - 主实验对比是否公平？KL 和 BCE 的计算量对比（1000 vs 2700 steps）是否充分说明 structural failure？\n   - 消融实验是否覆盖所有关键设计选择？是否有遗漏的 confounding factors？\n   - 三 seed 统计（PPL 11.92±0.07）——3 seeds 的统计效力是否足够？\n   - Cross-architecture evaluation (Mistral-7B) 是否充分验证 generalization？仅两个 7-8B 模型是否足够？\n   - OOD evaluation (C4) 是否足够？训练和评估都在 WikiText 系列上是否存在 data leakage concern？\n   - Downstream task collapse（MMLU/GSM8K 在 50% 时 ≈ random）——这是否 undermines the practical value？\n\n3. **可重复性**：\n   - 超参数是否充分报告？\n   - 训练细节（WikiText-103, 1000 steps, batch=4, seq=2048）是否足够 reproduce？\n   - Inference protocol（predictor-TEAL）是否描述清晰？\n\n4. **Latency claim**：\n   - 论文声称 6.4% overhead 但目前没有 wall-clock speedup——这对一篇 efficiency-motivated paper 意味着什么？\n   - \"eliminates compensation network\" 节省 2.7% latency，但 predictor 本身加 6.4%——净效果是增加 overhead，这与 paper framing 是否矛盾？\n\n请按 ARR review form 格式输出：Summary → Strengths → Weaknesses → Questions → Soundness (1-5) → Overall (1-5)"
}
```

---

### Runtime record

_source line 2 · 2026-05-17T08:10:55.618Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-17T08:10:55.618Z",
  "sessionId": "fd7408d6-e7e0-4bb4-8dde-4202758b928d"
}
```

---

## Round 1

73 recorded events

### User

_source line 3 · 2026-05-17T08:10:55.655Z_

[Round 1 审稿请求]:
你负责**方法严谨性 + 实验有效性**的审查。

## Venue 信息
- **目标会议**: EMNLP 2026 (via ACL Rolling Review, May cycle)
- **截止日期**: 2026-05-25
- **页数限制**: Long paper ≤8 页正文 + unlimited references + appendix
- **模板**: ACL format with `[review]` option
- **匿名规则**: Double-blind
- **附录规则**: 允许，reviewer 可选择性阅读

## 论文路径
`projects/distill_sparse_swiglu/paper/main.tex`（含 abstract.tex, introduction.tex, method.tex, experiments.tex, related_work.tex, conclusion.tex, limitations.tex, appendix.tex）

## 你的审查侧重

1. **方法正确性**：
   - KL 梯度分析（Eq. 7-8）是否数学上严格？factor (a)-(d) 的分解是否完整？
   - Gumbel-Sigmoid relaxation 的使用是否正确？与标准 Concrete distribution 的关系是否清晰？
   - Adaptive penalty controller (Eq. 5-6) 的收敛保证——论文称其为 "adaptive penalty controller" 而非 Lagrangian，这个表述是否准确？multiplicative schedule 是否有理论支撑？
   - BCE vs KL structural mismatch argument 是否有逻辑漏洞？

2. **实验有效性**：
   - 主实验对比是否公平？KL 和 BCE 的计算量对比（1000 vs 2700 steps）是否充分说明 structural failure？
   - 消融实验是否覆盖所有关键设计选择？是否有遗漏的 confounding factors？
   - 三 seed 统计（PPL 11.92±0.07）——3 seeds 的统计效力是否足够？
   - Cross-architecture evaluation (Mistral-7B) 是否充分验证 generalization？仅两个 7-8B 模型是否足够？
   - OOD evaluation (C4) 是否足够？训练和评估都在 WikiText 系列上是否存在 data leakage concern？
   - Downstream task collapse（MMLU/GSM8K 在 50% 时 ≈ random）——这是否 undermines the practical value？

3. **可重复性**：
   - 超参数是否充分报告？
   - 训练细节（WikiText-103, 1000 steps, batch=4, seq=2048）是否足够 reproduce？
   - Inference protocol（predictor-TEAL）是否描述清晰？

4. **Latency claim**：
   - 论文声称 6.4% overhead 但目前没有 wall-clock speedup——这对一篇 efficiency-motivated paper 意味着什么？
   - "eliminates compensation network" 节省 2.7% latency，但 predictor 本身加 6.4%——净效果是增加 overhead，这与 paper framing 是否矛盾？

请按 ARR review form 格式输出：Summary → Strengths → Weaknesses → Questions → Soundness (1-5) → Overall (1-5)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "e22b3aa5-f147-4b55-a02c-533b2c761d41",
  "type": "user",
  "uuid": "a507557f-1401-4ae9-8239-ee5f2ded637e",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/review_reviewer_1_772f066c",
  "sessionId": "fd7408d6-e7e0-4bb4-8dde-4202758b928d",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-17T08:10:55.655Z_

```json
{
  "parentUuid": "a507557f-1401-4ae9-8239-ee5f2ded637e",
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
  "uuid": "bc9b02fe-ca2f-44f3-9387-2fddcdc2bc59",
  "timestamp": "2026-05-17T08:10:55.655Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/review_reviewer_1_772f066c",
  "sessionId": "fd7408d6-e7e0-4bb4-8dde-4202758b928d",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

---

### Runtime record

_source line 5 · 2026-05-17T08:10:55.655Z_

```json
{
  "parentUuid": "bc9b02fe-ca2f-44f3-9387-2fddcdc2bc59",
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
  "uuid": "dc884b70-8511-4620-a6bc-0f34d893ca54",
  "timestamp": "2026-05-17T08:10:55.655Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/review_reviewer_1_772f066c",
  "sessionId": "fd7408d6-e7e0-4bb4-8dde-4202758b928d",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

---

### Runtime record

_source line 6 · 2026-05-17T08:10:55.655Z_

```json
{
  "parentUuid": "dc884b70-8511-4620-a6bc-0f34d893ca54",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "30d1c180-3748-43f9-a6ed-45e0557b2259",
  "timestamp": "2026-05-17T08:10:55.655Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/review_reviewer_1_772f066c",
  "sessionId": "fd7408d6-e7e0-4bb4-8dde-4202758b928d",
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
  "aiTitle": "Review paper on sparse SwiGLU distillation methods",
  "sessionId": "fd7408d6-e7e0-4bb4-8dde-4202758b928d"
}
```

---

### Assistant

_source line 8 · 2026-05-17T08:11:07.934Z_

<details><summary>Logged reasoning block</summary>

```text
The user (Review Director) is asking me to perform a Round 1 review of a paper on distilling sparse SwiGLU networks, focusing on methodological rigor and experimental validity. I need to:

1. First, run the session start skill to initialize
2. Search for ACL ARR reviewer guidelines
3. Read the paper thoroughly
4. Produce a detailed review

Let me start by reading the paper and searching for reviewer guidelines. But first, let me check if I should run the session-start skill.

Actually, looking at the instructions, the session-start skill is for "Review Reviewer 角色 session 启动时自动使用". 

I should read the paper first to understand what I'm reviewing, then locate the ACL ARR review form and guidelines to structure my feedback properly. Let me start by finding the paper file in the project directory and reading through it.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "30d1c180-3748-43f9-a6ed-45e0557b2259",
  "isSidechain": false,
  "requestId": "req_011Cb7oVziJzAu5fMsmkzp24",
  "type": "assistant",
  "uuid": "c01d9fe1-51e6-4400-b51e-d0a4853f5f97",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/review_reviewer_1_772f066c",
  "sessionId": "fd7408d6-e7e0-4bb4-8dde-4202758b928d",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01E2pnfEtQzQxbDvHnMva6St",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15833,
      "cache_read_input_tokens": 11841,
      "output_tokens": 511,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 15833,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 511,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 15833,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 15833
          },
          "type": "message"
        }
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

_source line 9 · 2026-05-17T08:11:07.938Z_

开始审稿。先并行读取论文和搜索 ARR reviewer guidelines。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c01d9fe1-51e6-4400-b51e-d0a4853f5f97",
  "isSidechain": false,
  "requestId": "req_011Cb7oVziJzAu5fMsmkzp24",
  "type": "assistant",
  "uuid": "3de3446b-7692-443a-a211-c7e8a34d1a52",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/review_reviewer_1_772f066c",
  "sessionId": "fd7408d6-e7e0-4bb4-8dde-4202758b928d",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01E2pnfEtQzQxbDvHnMva6St",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15833,
      "cache_read_input_tokens": 11841,
      "output_tokens": 511,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 15833,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 511,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 15833,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 15833
          },
          "type": "message"
        }
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

_source line 10 · 2026-05-17T08:11:08.594Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01TbWQMt3TqhXFJNxjJc9C1E`</summary>

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
  "parentUuid": "3de3446b-7692-443a-a211-c7e8a34d1a52",
  "isSidechain": false,
  "requestId": "req_011Cb7oVziJzAu5fMsmkzp24",
  "type": "assistant",
  "uuid": "42e25398-8e10-45d7-9466-65fda6c00f6b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/review_reviewer_1_772f066c",
  "sessionId": "fd7408d6-e7e0-4bb4-8dde-4202758b928d",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01E2pnfEtQzQxbDvHnMva6St",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15833,
      "cache_read_input_tokens": 11841,
      "output_tokens": 511,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 15833,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 511,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 15833,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 15833
          },
          "type": "message"
        }
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

_source line 11 · 2026-05-17T08:11:08.600Z_

<details><summary>↩ Tool result · `toolu_01TbWQMt3TqhXFJNxjJc9C1E`</summary>

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
  "parentUuid": "42e25398-8e10-45d7-9466-65fda6c00f6b",
  "isSidechain": false,
  "promptId": "e22b3aa5-f147-4b55-a02c-533b2c761d41",
  "type": "user",
  "uuid": "39c7901b-cfd3-4a08-ab50-c4559ee536d7",
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
  "sourceToolAssistantUUID": "42e25398-8e10-45d7-9466-65fda6c00f6b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/review_reviewer_1_772f066c",
  "sessionId": "fd7408d6-e7e0-4bb4-8dde-4202758b928d",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-17T08:11:11.594Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01XqQEW36qWdGE3tomeogEVK`</summary>

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
  "parentUuid": "39c7901b-cfd3-4a08-ab50-c4559ee536d7",
  "isSidechain": false,
  "requestId": "req_011Cb7oWwvAQENJYEmi77QeC",
  "type": "assistant",
  "uuid": "34503024-2198-434a-8b7d-c25fa0871271",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/review_reviewer_1_772f066c",
  "sessionId": "fd7408d6-e7e0-4bb4-8dde-4202758b928d",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FsKVpsn4Uuii6KXkJoTn25",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2507,
      "cache_read_input_tokens": 27674,
      "output_tokens": 186,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2507,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 186,
          "cache_read_input_tokens": 27674,
          "cache_creation_input_tokens": 2507,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2507
          },
          "type": "message"
        }
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

_source line 13 · 2026-05-17T08:11:12.248Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images · `toolu_01SKLx8Sne3m5uZrwyFHQRKs`</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/main.pdf",
  "pages": "1-10",
  "dpi": 200
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "34503024-2198-434a-8b7d-c25fa0871271",
  "isSidechain": false,
  "requestId": "req_011Cb7oWwvAQENJYEmi77QeC",
  "type": "assistant",
  "uuid": "ceddb571-b06e-47dd-b246-9e4be6f3d8f4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/review_reviewer_1_772f066c",
  "sessionId": "fd7408d6-e7e0-4bb4-8dde-4202758b928d",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FsKVpsn4Uuii6KXkJoTn25",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2507,
      "cache_read_input_tokens": 27674,
      "output_tokens": 186,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2507,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 186,
          "cache_read_input_tokens": 27674,
          "cache_creation_input_tokens": 2507,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2507
          },
          "type": "message"
        }
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

_source line 14 · 2026-05-17T08:11:26.180Z_

<details><summary>↩ Tool result · `toolu_01XqQEW36qWdGE3tomeogEVK`</summary>

```text
Web search results for query: "ACL Rolling Review 2026 reviewer guidelines review form criteria"

Links: [{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"ACL Rolling Review | ACL Member Portal","url":"https://www.aclweb.org/portal/content/acl-rolling-review"}]

I've found comprehensive information about the ACL Rolling Review 2026 reviewer guidelines, review form, and criteria. Here are the key findings:

## Reviewer Guidelines

When you accept a reviewing request for an ARR cycle, you'll receive a kick-off email from OpenReview listing important dates, and you should block time for checking assignments, working on reviews, and submitting them on time.

To preserve the merits of double-blind review, reviewers for *ACL conferences should not actively try to discover the identity of authors and not let any suspicion of author identity affect their judgment, with reviewers asked to read the paper and get their first impression before searching for related work.

## Review Form Criteria

The review form includes several key evaluation dimensions:

- **Major Reasons to Publish**: Reviewers should identify major reasons to publish, which could include novel and useful methodology, insightful empirical results or theoretical analysis, clear organization of related literature, or other reasons why interested readers of *ACL papers may find the paper useful.

- **Concerns**: Reviewers should identify concerns about correctness of results or argumentation, limited perceived impact of methods or findings, lack of clarity in exposition, or other reasons why interested readers may gain less from this paper than other papers under consideration.

- **Excitement**: Reviewers assess how exciting the paper is subjectively, considering whether papers present conceptual breakthroughs, challenge common assumptions, have possible impact on communities, or are relevant and useful for the reviewer's own research.

- **Ethical Review**: Reviewers should review the ACL code of ethics and the ARR checklist submitted by authors, and describe any ethical issues and the extent to which they have been acknowledged or addressed.

- **Reproducibility**: Reviewers assess whether there is enough information in the paper for readers to reproduce the main results, use results in future work as a baseline, or build upon the work.

## 2026 Incentives and Policies

From this cycle, ARR intends to strictly monitor adherence to reviewing responsibilities, with papers whose authors have not registered as reviewers or completed their checklists by the designated deadline automatically desk-rejected.

Reviewers/ACs who remain unresponsive and do not submit their reviews or meta-reviews on time will be prevented from accessing reviews and/or meta-reviews for their own papers.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "34503024-2198-434a-8b7d-c25fa0871271",
  "isSidechain": false,
  "promptId": "e22b3aa5-f147-4b55-a02c-533b2c761d41",
  "type": "user",
  "uuid": "9a9c287b-e1cb-406c-bb9c-2ad8c526dfb4",
  "toolUseResult": {
    "query": "ACL Rolling Review 2026 reviewer guidelines review form criteria",
    "results": [
      {
        "tool_use_id": "srvtoolu_01PtY5C4WcGAmxNEQGom8fss",
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
            "title": "ACL Rolling Review – A peer review platform for the Association for Computational Linguistics",
            "url": "http://aclrollingreview.org/"
          },
          {
            "title": "How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics",
            "url": "http://aclrollingreview.org/reviewing"
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
            "title": "ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics",
            "url": "http://aclrollingreview.org/acguidelines"
          },
          {
            "title": "ACL Rolling Review | ACL Member Portal",
            "url": "https://www.aclweb.org/portal/content/acl-rolling-review"
          }
        ]
      },
      "I've found comprehensive information about the ACL Rolling Review 2026 reviewer guidelines, review form, and criteria. Here are the key findings:\n\n## Reviewer Guidelines\n\nWhen you accept a reviewing request for an ARR cycle, you'll receive a kick-off email from OpenReview listing important dates, and you should block time for checking assignments, working on reviews, and submitting them on time.\n\nTo preserve the merits of double-blind review, reviewers for *ACL conferences should not actively try to discover the identity of authors and not let any suspicion of author identity affect their judgment, with reviewers asked to read the paper and get their first impression before searching for related work.\n\n## Review Form Criteria\n\nThe review form includes several key evaluation dimensions:\n\n- **Major Reasons to Publish**: Reviewers should identify major reasons to publish, which could include novel and useful methodology, insightful empirical results or theoretical analysis, clear organization of related literature, or other reasons why interested readers of *ACL papers may find the paper useful.\n\n- **Concerns**: Reviewers should identify concerns about correctness of results or argumentation, limited perceived impact of methods or findings, lack of clarity in exposition, or other reasons why interested readers may gain less from this paper than other papers under consideration.\n\n- **Excitement**: Reviewers assess how exciting the paper is subjectively, considering whether papers present conceptual breakthroughs, challenge common assumptions, have possible impact on communities, or are relevant and useful for the reviewer's own research.\n\n- **Ethical Review**: Reviewers should review the ACL code of ethics and the ARR checklist submitted by authors, and describe any ethical issues and the extent to which they have been acknowledged or addressed.\n\n- **Reproducibility**: Reviewers assess whether there is enough information in the paper for readers to reproduce the main results, use results in future work as a baseline, or build upon the work.\n\n## 2026 Incentives and Policies\n\nFrom this cycle, ARR intends to strictly monitor adherence to reviewing responsibilities, with papers whose authors have not registered as reviewers or completed their checklists by the designated deadline automatically desk-rejected.\n\nReviewers/ACs who remain unresponsive and do not submit their reviews or meta-reviews on time will be prevented from accessing reviews and/or meta-reviews for their own papers."
    ],
    "durationSeconds": 14.581239088999999
  },
  "sourceToolAssistantUUID": "34503024-2198-434a-8b7d-c25fa0871271",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/review_reviewer_1_772f066c",
  "sessionId": "fd7408d6-e7e0-4bb4-8dde-4202758b928d",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-17T08:11:30.946Z_

<details><summary>↩ Tool result · `toolu_01SKLx8Sne3m5uZrwyFHQRKs`</summary>

```text
Error: result (9,085,867 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-14-projects-distill-sparse-swiglu--claude-sessions-review-reviewer-1-772f066c/fd7408d6-e7e0-4bb4-8dde-4202758b928d/tool-results/mcp-agent-ml-research-pdf_to_images-1779005490929.txt.
Format: JSON with schema: {result: string}
Use offset and limit parameters to read specific portions of the file, search within it for specific content, and jq to make structured queries.
REQUIREMENTS FOR SUMMARIZATION/ANALYSIS/REVIEW:
- You MUST read the content from the file at /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-14-projects-distill-sparse-swiglu--claude-sessions-review-reviewer-1-772f066c/fd7408d6-e7e0-4bb4-8dde-4202758b928d/tool-results/mcp-agent-ml-research-pdf_to_images-1779005490929.txt in sequential chunks until 100% of the content has been read.
- If you receive truncation warnings when reading the file, reduce the chunk size until you have read 100% of the content without truncation.
- Before producing ANY summary or analysis, you MUST explicitly describe what portion of the content you have read. ***If you did not read the entire content, you MUST explicitly state this.***

```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ceddb571-b06e-47dd-b246-9e4be6f3d8f4",
  "isSidechain": false,
  "promptId": "e22b3aa5-f147-4b55-a02c-533b2c761d41",
  "type": "user",
  "uuid": "d65d9bd3-ca2a-476c-98b4-8a3ede14553a",
  "toolUseResult": "Error: result (9,085,867 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-14-projects-distill-sparse-swiglu--claude-sessions-review-reviewer-1-772f066c/fd7408d6-e7e0-4bb4-8dde-4202758b928d/tool-results/mcp-agent-ml-research-pdf_to_images-1779005490929.txt.\nFormat: JSON with schema: {result: string}\nUse offset and limit parameters to read specific portions of the file, search within it for specific content, and jq to make structured queries.\nREQUIREMENTS FOR SUMMARIZATION/ANALYSIS/REVIEW:\n- You MUST read the content from the file at /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-14-projects-distill-sparse-swiglu--claude-sessions-review-reviewer-1-772f066c/fd7408d6-e7e0-4bb4-8dde-4202758b928d/tool-results/mcp-agent-ml-research-pdf_to_images-1779005490929.txt in sequential chunks until 100% of the content has been read.\n- If you receive truncation warnings when reading the file, reduce the chunk size until you have read 100% of the content without truncation.\n- Before producing ANY summary or analysis, you MUST explicitly describe what portion of the content you have read. ***If you did not read the entire content, you MUST explicitly state this.***\n",
  "mcpMeta": {
    "storage": "sanitized-trace-archive",
    "source_line": 15,
    "serialized_bytes": 9085904,
    "serialized_sha256": "b82d8a7925e2b823a787a0e0a1dbfbf072094d3a980dd570e5d7b11add2e4162",
    "note": "Complete sanitized source is retained in trace-files.tar.gz."
  },
  "sourceToolAssistantUUID": "ceddb571-b06e-47dd-b246-9e4be6f3d8f4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/review_reviewer_1_772f066c",
  "sessionId": "fd7408d6-e7e0-4bb4-8dde-4202758b928d",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Runtime record

_source line 16_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[Round 1 审稿请求]: 你负责**方法严谨性 + 实验有效性**的审查。  ## Venue 信息 - **目标会议**: EMNLP 2026 (via ACL Rolling Review, May cycle) - **截止日期**: 2026-05-25 - **页数限制**: Long paper ≤8 页正文 + unlimited references + appendix…",
  "leafUuid": "d65d9bd3-ca2a-476c-98b4-8a3ede14553a",
  "sessionId": "fd7408d6-e7e0-4bb4-8dde-4202758b928d"
}
```

---

### Runtime record

_source line 17_

```json
{
  "type": "ai-title",
  "aiTitle": "Review paper on sparse SwiGLU distillation methods",
  "sessionId": "fd7408d6-e7e0-4bb4-8dde-4202758b928d"
}
```

---

### Assistant

_source line 18 · 2026-05-17T08:11:34.325Z_

<details><summary>Logged reasoning block</summary>

```text
The PDF images were too large. Let me fetch the review form page and read the paper source files directly instead. Let me read the tex files to understand the paper content.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d65d9bd3-ca2a-476c-98b4-8a3ede14553a",
  "isSidechain": false,
  "requestId": "req_011Cb7oYbZrw5R7dxMKXAbxL",
  "type": "assistant",
  "uuid": "e9444177-43c7-4f6f-be46-95527c86d7ca",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/review_reviewer_1_772f066c",
  "sessionId": "fd7408d6-e7e0-4bb4-8dde-4202758b928d",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01A2zxzHYBsyvZtBLEqe5B4P",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1647,
      "cache_read_input_tokens": 30181,
      "output_tokens": 289,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1647,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 289,
          "cache_read_input_tokens": 30181,
          "cache_creation_input_tokens": 1647,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1647
          },
          "type": "message"
        }
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

_source line 19 · 2026-05-17T08:11:35.423Z_

PDF 图片太大，改为直接读取 LaTeX 源文件。同时获取 ARR review form 详细评分标准。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e9444177-43c7-4f6f-be46-95527c86d7ca",
  "isSidechain": false,
  "requestId": "req_011Cb7oYbZrw5R7dxMKXAbxL",
  "type": "assistant",
  "uuid": "40488497-6fd1-44fd-af6e-534ec160f12d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/review_reviewer_1_772f066c",
  "sessionId": "fd7408d6-e7e0-4bb4-8dde-4202758b928d",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01A2zxzHYBsyvZtBLEqe5B4P",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1647,
      "cache_read_input_tokens": 30181,
      "output_tokens": 289,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1647,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 289,
          "cache_read_input_tokens": 30181,
          "cache_creation_input_tokens": 1647,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1647
          },
          "type": "message"
        }
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

_source line 20 · 2026-05-17T08:11:36.780Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01W27p3cr41NubYBebsxs3g1`</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract the complete review form with all scoring dimensions, their scale (1-5 etc), and descriptions for each score level. Include all fields reviewers must fill in."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "40488497-6fd1-44fd-af6e-534ec160f12d",
  "isSidechain": false,
  "requestId": "req_011Cb7oYbZrw5R7dxMKXAbxL",
  "type": "assistant",
  "uuid": "ea081ad0-2484-4b69-8199-d4e2e720fe63",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/review_reviewer_1_772f066c",
  "sessionId": "fd7408d6-e7e0-4bb4-8dde-4202758b928d",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01A2zxzHYBsyvZtBLEqe5B4P",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1647,
      "cache_read_input_tokens": 30181,
      "output_tokens": 289,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1647,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 289,
          "cache_read_input_tokens": 30181,
          "cache_creation_input_tokens": 1647,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1647
          },
          "type": "message"
        }
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

_source line 21 · 2026-05-17T08:11:37.155Z_

<details><summary>↩ Tool result · `toolu_0127JLVcAN5N52q71xwU3hSE`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/limitations.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/main.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/introduction.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/abstract.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/conclusion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/related_work.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/method.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/appendix.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/experiments.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c3ea9b5e-9330-412c-981a-6f4a69e2d52b",
  "isSidechain": false,
  "promptId": "e22b3aa5-f147-4b55-a02c-533b2c761d41",
  "type": "user",
  "uuid": "043b3e07-6ab0-45fb-a0c0-a7a3c9cd7179",
  "toolUseResult": {
    "filenames": [
      "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/limitations.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/main.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/introduction.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/abstract.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/conclusion.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/related_work.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/method.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/appendix.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/experiments.tex"
    ],
    "durationMs": 13,
    "numFiles": 9,
    "truncated": false
  },
  "sourceToolAssistantUUID": "c3ea9b5e-9330-412c-981a-6f4a69e2d52b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/review_reviewer_1_772f066c",
  "sessionId": "fd7408d6-e7e0-4bb4-8dde-4202758b928d",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-17T08:11:37.123Z_

<details open><summary>🔧 Tool call — Glob · `toolu_0127JLVcAN5N52q71xwU3hSE`</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ea081ad0-2484-4b69-8199-d4e2e720fe63",
  "isSidechain": false,
  "requestId": "req_011Cb7oYbZrw5R7dxMKXAbxL",
  "type": "assistant",
  "uuid": "c3ea9b5e-9330-412c-981a-6f4a69e2d52b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/review_reviewer_1_772f066c",
  "sessionId": "fd7408d6-e7e0-4bb4-8dde-4202758b928d",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01A2zxzHYBsyvZtBLEqe5B4P",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1647,
      "cache_read_input_tokens": 30181,
      "output_tokens": 289,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1647,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 289,
          "cache_read_input_tokens": 30181,
          "cache_creation_input_tokens": 1647,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1647
          },
          "type": "message"
        }
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

_source line 23 · 2026-05-17T08:11:43.508Z_

<details><summary>↩ Tool result · `toolu_01W27p3cr41NubYBebsxs3g1`</summary>

```text
# ACL Rolling Review Form - Complete Scoring Dimensions

## Core Evaluation Dimensions

**Reviewer Confidence** (1-5 scale)
- 5: "Positive that my evaluation is correct. I read the paper very carefully"
- 4: Quite sure; unlikely to have missed important points
- 3: Pretty sure; may have missed some details
- 2: Willing to defend evaluation; fairly likely missed some details
- 1: "Not my area, or paper is very hard to understand"

**Soundness** (1-5 scale, with half-points)
- 5: "Excellent: This study is one of the most thorough I have seen"
- 4: Strong; sufficient support with minor additions optional
- 3: Acceptable; main claims supported with minor gaps
- 2: Poor; main claims lack sufficient support
- 1: "Major Issues: This study is not yet sufficiently thorough to warrant publication"

**Excitement** (1-5 scale, with half-points)
- 5: "Highly Exciting: I would recommend this paper to others"
- 4: Exciting; would mention to others or attend presentation
- 3: Interesting; might mention points or attend if time permits
- 2: Potentially interesting; doesn't resonate personally
- 1: "Not Exciting: this paper does not resonate with me"

**Overall Assessment** (1-5 scale, with half-points)
- 5: Consider for Award (top 2.5% papers)
- 4: Conference acceptance
- 3: Findings acceptance
- 2: Resubmit next cycle
- 1: Do not resubmit

## Additional Evaluation Dimensions

**Reproducibility** (1-5 scale): Assesses whether readers can reproduce results

**Datasets** (1-5 scale): Evaluates released dataset value to community

**Software** (1-5 scale): Assesses released software utility

**Author Identity Knowledge** (1-5 scale): Tracks blind review integrity

**Required Fields:**
- Paper Summary
- Summary of Strengths
- Summary of Weaknesses
- Comments/Suggestions/Typos
- Limitations and Societal Impact
- Ethical Concerns
- Ethics Review Recommendation
- Best Paper Justification (conditional)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ea081ad0-2484-4b69-8199-d4e2e720fe63",
  "isSidechain": false,
  "promptId": "e22b3aa5-f147-4b55-a02c-533b2c761d41",
  "type": "user",
  "uuid": "cd0c5076-0599-425a-992e-089edbcb5627",
  "toolUseResult": {
    "bytes": 25365,
    "code": 200,
    "codeText": "OK",
    "result": "# ACL Rolling Review Form - Complete Scoring Dimensions\n\n## Core Evaluation Dimensions\n\n**Reviewer Confidence** (1-5 scale)\n- 5: \"Positive that my evaluation is correct. I read the paper very carefully\"\n- 4: Quite sure; unlikely to have missed important points\n- 3: Pretty sure; may have missed some details\n- 2: Willing to defend evaluation; fairly likely missed some details\n- 1: \"Not my area, or paper is very hard to understand\"\n\n**Soundness** (1-5 scale, with half-points)\n- 5: \"Excellent: This study is one of the most thorough I have seen\"\n- 4: Strong; sufficient support with minor additions optional\n- 3: Acceptable; main claims supported with minor gaps\n- 2: Poor; main claims lack sufficient support\n- 1: \"Major Issues: This study is not yet sufficiently thorough to warrant publication\"\n\n**Excitement** (1-5 scale, with half-points)\n- 5: \"Highly Exciting: I would recommend this paper to others\"\n- 4: Exciting; would mention to others or attend presentation\n- 3: Interesting; might mention points or attend if time permits\n- 2: Potentially interesting; doesn't resonate personally\n- 1: \"Not Exciting: this paper does not resonate with me\"\n\n**Overall Assessment** (1-5 scale, with half-points)\n- 5: Consider for Award (top 2.5% papers)\n- 4: Conference acceptance\n- 3: Findings acceptance\n- 2: Resubmit next cycle\n- 1: Do not resubmit\n\n## Additional Evaluation Dimensions\n\n**Reproducibility** (1-5 scale): Assesses whether readers can reproduce results\n\n**Datasets** (1-5 scale): Evaluates released dataset value to community\n\n**Software** (1-5 scale): Assesses released software utility\n\n**Author Identity Knowledge** (1-5 scale): Tracks blind review integrity\n\n**Required Fields:**\n- Paper Summary\n- Summary of Strengths\n- Summary of Weaknesses\n- Comments/Suggestions/Typos\n- Limitations and Societal Impact\n- Ethical Concerns\n- Ethics Review Recommendation\n- Best Paper Justification (conditional)",
    "durationMs": 6722,
    "url": "https://aclrollingreview.org/reviewform"
  },
  "sourceToolAssistantUUID": "ea081ad0-2484-4b69-8199-d4e2e720fe63",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/review_reviewer_1_772f066c",
  "sessionId": "fd7408d6-e7e0-4bb4-8dde-4202758b928d",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 24 · 2026-05-17T08:11:46.777Z_

<details><summary>Logged reasoning block</summary>

```text
Good, I have the review form criteria. Now let me read all the tex files. Let me read them in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cd0c5076-0599-425a-992e-089edbcb5627",
  "isSidechain": false,
  "requestId": "req_011Cb7oZWy4fYiJASzD2k8VN",
  "type": "assistant",
  "uuid": "6a071869-f6f0-4328-bf9e-80c9c21cc577",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/review_reviewer_1_772f066c",
  "sessionId": "fd7408d6-e7e0-4bb4-8dde-4202758b928d",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014pujs8tdAWYSgd6nPAVexn",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 365,
      "cache_creation_input_tokens": 855,
      "cache_read_input_tokens": 31828,
      "output_tokens": 722,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 855,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 365,
          "output_tokens": 722,
          "cache_read_input_tokens": 31828,
          "cache_creation_input_tokens": 855,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 855
          },
          "type": "message"
        }
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

_source line 25 · 2026-05-17T08:11:47.281Z_

ARR review form 已获取。现在并行读取所有论文章节。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6a071869-f6f0-4328-bf9e-80c9c21cc577",
  "isSidechain": false,
  "requestId": "req_011Cb7oZWy4fYiJASzD2k8VN",
  "type": "assistant",
  "uuid": "95a1f67b-443b-44db-baeb-aed2029b498a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/review_reviewer_1_772f066c",
  "sessionId": "fd7408d6-e7e0-4bb4-8dde-4202758b928d",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014pujs8tdAWYSgd6nPAVexn",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 365,
      "cache_creation_input_tokens": 855,
      "cache_read_input_tokens": 31828,
      "output_tokens": 722,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 855,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 365,
          "output_tokens": 722,
          "cache_read_input_tokens": 31828,
          "cache_creation_input_tokens": 855,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 855
          },
          "type": "message"
        }
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

_source line 26 · 2026-05-17T08:11:47.830Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Tgt38YdpC3cbnpSU5goCRZ`</summary>

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
  "parentUuid": "95a1f67b-443b-44db-baeb-aed2029b498a",
  "isSidechain": false,
  "requestId": "req_011Cb7oZWy4fYiJASzD2k8VN",
  "type": "assistant",
  "uuid": "fc53a4b6-7c57-4a12-a6d1-12643d5ada57",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/review_reviewer_1_772f066c",
  "sessionId": "fd7408d6-e7e0-4bb4-8dde-4202758b928d",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014pujs8tdAWYSgd6nPAVexn",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 365,
      "cache_creation_input_tokens": 855,
      "cache_read_input_tokens": 31828,
      "output_tokens": 722,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 855,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 365,
          "output_tokens": 722,
          "cache_read_input_tokens": 31828,
          "cache_creation_input_tokens": 855,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 855
          },
          "type": "message"
        }
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

_source line 27 · 2026-05-17T08:11:51.702Z_

<details><summary>↩ Tool result · `toolu_01YUiLPF4YdW3wHeA7AGheQc`</summary>

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
110	\section{Adaptive Penalty Controller Dynamics}
111	\label{app:lagrangian}
112	
113	Table~\ref{tab:lagrangian} reports the convergence of the adaptive penalty controller across sparsity targets.
114	The geometric doubling pattern ($1 \to 2 \to 4 \to 8 \to \ldots$) enables $\lambda$ to reach steady state within $\sim$10 steps; the deadzone ($\epsilon = 0.02$) then stabilizes $\lambda$ once actual sparsity is within $\pm$2\% of the target.
115	
116	\begin{table}[h]
117	\centering
118	\caption{Penalty controller convergence across sparsity targets (multiplicative schedule, margin $\epsilon=0.02$, 1000 training steps). Deviation is $|$actual $-$ target$|$ / target.}
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
137	\begin{figure}[h]
138	\centering
139	\includegraphics[width=\columnwidth]{lagrangian_dynamics.pdf}
140	\caption{Adaptive penalty controller convergence across sparsity targets. Upper panel: penalty weight $\lambda$ (log scale) over training steps. The 30\% target requires extreme penalty ($\lambda \to 5000$) to suppress activations below their natural density, while 50\% needs only $\lambda \approx 8$ since SwiGLU gates already cluster near this sparsity. Lower panel: actual sparsity (solid) converges to the target (dashed) within $\sim$10 steps via geometric doubling.}
141	\label{fig:lagrangian_dynamics}
142	\end{figure}
143	
144	Temperature $\tau$ is annealed linearly from 1.0 to 0.1 over 1000 steps.
145	A mild loss increase in the final $\sim$100 steps is expected: as masks become more binary ($\tau \to 0$), discrete rounding noise slightly increases KL divergence, confirming the training is converging toward the hard-mask inference regime.
146	
147	The controller reliably drives actual sparsity to within 5\% of the target across all tested regimes, with $\lambda$ spanning three orders of magnitude (8 to 5000) via geometric doubling.
148	
149	
150	\section{Out-of-Distribution Evaluation}
151	\label{app:ood}
152	
153	To address concerns about data homogeneity between training (WikiText-103) and evaluation (WikiText-2), we evaluate on C4~\cite{raffel2020c4} validation set at 50\% sparsity under TEAL global allocation.
154	
155	\begin{table}[h]
156	\centering
157	\caption{Out-of-distribution evaluation on C4 validation (50\% sparsity, PPL$\downarrow$).}
158	\label{tab:ood}
159	\small
160	\begin{tabular}{lc}
161	\toprule
162	Method & C4 PPL$\downarrow$ \\
163	\midrule
164	Dense & 9.21 \\
165	KL predictor (Ours) & \textbf{18.40} \\ % exp_id: eval_c4_ood_kl50
166	TEAL vanilla & 38.75 \\
167	\bottomrule
168	\end{tabular}
169	\end{table}
170	
171	The KL-trained predictor achieves 52.5\% relative advantage over TEAL on out-of-domain data (18.40 vs.\ 38.75), comparable to or slightly exceeding the 49\% advantage observed on WikiText-2 (11.79 vs.\ 23.31), suggesting that KL-trained predictions generalize to held-out data when the evaluation distribution differs from training.
172	This confirms that the predictor learns generalizable neuron importance patterns rather than overfitting to the WikiText training distribution.
173	
174	
175	\section{Per-Layer Retention Analysis}
176	\label{app:retention}
177	
178	\begin{figure}[h]
179	\centering
180	\includegraphics[width=\columnwidth]{per_layer_retention_chart.pdf}
181	\caption{Per-layer neuron retention under global top-$k$ allocation at 30\%, 50\%, and 70\% sparsity. Dashed lines indicate uniform retention baselines. Late layers (L24--31) are consistently starved due to long-tailed activation distributions, with retention dropping to 28.4\% (L31) even at 30\% sparsity. At 70\%, starvation extends to mid-layers (L10--12: 16.7--20.1\%), explaining the transition to the capacity-limited regime.}
182	\label{fig:retention}
183	\end{figure}
184	
185	
186	\section{Training Stability}
187	\label{app:stability}
188	
189	Three-seed evaluation ($s \in \{42, 123, 456\}$) at 50\% sparsity under uniform allocation yields PPL $11.92 \pm 0.07$ (CV=0.6\%), confirming training stability across random initializations. % exp_id: multi_seed_kl50_uniform
190	Downstream metrics are similarly stable: ARC-c $33.8 \pm 1.2$\%, WinoGrande $62.9 \pm 0.1$\%, MMLU $28.0 \pm 0.6$\%, GSM8K $2.2 \pm 0.1$\%.
191	The low variance indicates that the KL training landscape is well-conditioned for this predictor architecture, with low sensitivity to initialization.
192	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5c5daa71-c898-40a8-a8fb-d2fcf9cc2da3",
  "isSidechain": false,
  "promptId": "e22b3aa5-f147-4b55-a02c-533b2c761d41",
  "type": "user",
  "uuid": "082bd6f6-4d53-4bfa-b8c4-3c8175a39c1f",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/appendix.tex",
      "content": "\\appendix\n\n\\section{Inference Efficiency}\n\\label{app:latency}\n\nTable~\\ref{tab:latency} reports inference throughput on a single NVIDIA RTX PRO 6000 Blackwell Server Edition GPU (batch size 1, sequence length 2048, fp16, averaged over 100 forward passes).\n\n\\begin{table}[h]\n\\centering\n\\caption{Inference latency on LLaMA-3.1-8B (RTX PRO 6000 Blackwell, batch=1, seq=2048, fp16, 100 forward passes). Overhead is relative to dense inference.}\n\\label{tab:latency}\n\\small\n\\begin{tabular}{llcccc}\n\\toprule\nMethod & Sparsity & ms/fwd & tok/s & Overhead \\\\\n\\midrule\nDense & 0\\% & 119.11$\\pm$0.57 & 17{,}195 & --- \\\\\n\\midrule\nKL predictor-only & 30\\% & 126.64$\\pm$0.70 & 16{,}172 & +6.3\\% \\\\ % exp_id: latency_bench\nKL predictor-only & 50\\% & 126.78$\\pm$0.31 & 16{,}154 & +6.4\\% \\\\ % exp_id: latency_bench\n\\midrule\nPredictor + compensation & 30\\% & 129.94$\\pm$0.75 & 15{,}761 & +9.1\\% \\\\ % exp_id: latency_bench\nPredictor + compensation & 50\\% & 129.71$\\pm$0.53 & 15{,}789 & +8.9\\% \\\\ % exp_id: latency_bench\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe full KL-sparse pipeline adds 6.4\\% overhead to dense inference (126.78 vs.\\ 119.11\\,ms/forward), of which the predictor's 32-layer forward pass contributes 3.17\\,ms (2.7\\%); the remainder arises from mask application and sparse FFN indexing.\nEliminating the compensation network saves an additional $\\sim$2.7\\% latency overhead and 67.2M parameters (the per-layer GEMV required for output rescaling), confirming that KL distillation provides both quality and efficiency advantages over BCE-based approaches.\nThe overhead is near-identical at 30\\% and 50\\% sparsity because the predictor runs the same computation regardless of target sparsity; only the top-$k$ threshold changes.\n\nNote that the current implementation uses unstructured element-wise masks, which do not translate to wall-clock speedup without sparse kernel support.\nThe pipeline adds $\\sim$6.4\\% overhead; net acceleration requires kernel-level sparse computation optimizations (e.g., Triton block-sparse, cuSPARSE) that are beyond the scope of this work.\nOur contribution is prediction quality and inference simplification (eliminating the compensation network), not end-to-end latency reduction.\n\n\n\\section{Predictor Bottleneck Sensitivity}\n\\label{app:db_sensitivity}\n\nTable~\\ref{tab:db_sensitivity} reports the effect of predictor bottleneck dimension $d_b$ on PPL at 50\\% sparsity under both TEAL global allocation (the paper's primary inference protocol) and per-token evaluation.\n\n\\begin{table}[h]\n\\centering\n\\caption{Predictor bottleneck sensitivity at 50\\% sparsity (WikiText-2 PPL$\\downarrow$). TEAL global is the primary inference protocol; per-token shown for reference.}\n\\label{tab:db_sensitivity}\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n$d_b$ & Params & TEAL global & $\\Delta$ & Per-token \\\\\n\\midrule\n64 & 38.2M (0.48\\%) & 12.076 & +0.9\\% & 10.16 \\\\ % exp_id: db_sensitivity_sweep\n128 & 75.9M (0.95\\%) & 11.963 & --- & 9.218 \\\\ % exp_id: db_sensitivity_sweep\n256 & 151.5M (1.89\\%) & 12.105 & +1.2\\% & 8.586 \\\\ % exp_id: db_sensitivity_sweep\n512 & 302.5M (3.77\\%) & 12.315 & +2.9\\% & 7.93 \\\\ % exp_id: db_sensitivity_sweep\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nUnder TEAL global allocation, increasing $d_b$ beyond 128 provides no benefit (PPL slightly worsens), while per-token evaluation shows monotonic improvement (10.16$\\to$7.93).\nThis divergence indicates that the global top-$k$ allocation mechanism, not predictor capacity, is the binding constraint: additional predictor capacity produces better per-neuron scores, but the global ranking and budget distribution cannot exploit them.\nThe $d_b{=}128$ configuration (75.9M params, $<$1\\% of base model) is therefore optimal for the TEAL inference protocol.\n\n\\subsection{Temperature Schedule Sensitivity}\n\\label{app:tau_sensitivity}\n\n\\begin{table}[h]\n\\centering\n\\caption{Temperature schedule sensitivity at 50\\% sparsity (WikiText-2 PPL$\\downarrow$, TEAL global).}\n\\label{tab:tau_sensitivity}\n\\small\n\\begin{tabular}{lc}\n\\toprule\n$\\tau$ Schedule & PPL$\\downarrow$ \\\\\n\\midrule\nFixed $\\tau{=}0.5$ & \\textbf{11.861} \\\\ % exp_id: tau_schedule_sweep\nLinear $1.0 \\to 0.1$ (default) & 11.963 \\\\ % exp_id: tau_schedule_sweep\nFixed $\\tau{=}0.1$ & 12.072 \\\\ % exp_id: tau_schedule_sweep\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTemperature schedule has minimal impact ($<$1.8\\% PPL variation).\nThe linear annealing default is a conservative choice; even removing annealing entirely (fixed $\\tau{=}0.5$) yields comparable performance.\n\n\\subsection{Training Convergence}\n\\label{app:training_convergence}\n\n\\begin{table}[h]\n\\centering\n\\caption{Training convergence at 50\\% sparsity (WikiText-2 PPL$\\downarrow$, TEAL global).}\n\\label{tab:training_convergence}\n\\small\n\\begin{tabular}{cc}\n\\toprule\nSteps & PPL$\\downarrow$ \\\\\n\\midrule\n200 & 15.158 \\\\ % exp_id: training_steps_sweep\n400 & 12.538 \\\\ % exp_id: training_steps_sweep\n600 & 12.046 \\\\ % exp_id: training_steps_sweep\n800 & 11.907 \\\\ % exp_id: training_steps_sweep\n1000 & \\textbf{11.906} \\\\ % exp_id: training_steps_sweep\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTraining converges rapidly: 95\\% of the quality gap closes by step 600, and performance saturates by step 800 ($\\Delta < 0.001$ between 800 and 1000 steps).\nOur default of 1000 steps provides a conservative margin.\n\n\n\\section{Adaptive Penalty Controller Dynamics}\n\\label{app:lagrangian}\n\nTable~\\ref{tab:lagrangian} reports the convergence of the adaptive penalty controller across sparsity targets.\nThe geometric doubling pattern ($1 \\to 2 \\to 4 \\to 8 \\to \\ldots$) enables $\\lambda$ to reach steady state within $\\sim$10 steps; the deadzone ($\\epsilon = 0.02$) then stabilizes $\\lambda$ once actual sparsity is within $\\pm$2\\% of the target.\n\n\\begin{table}[h]\n\\centering\n\\caption{Penalty controller convergence across sparsity targets (multiplicative schedule, margin $\\epsilon=0.02$, 1000 training steps). Deviation is $|$actual $-$ target$|$ / target.}\n\\label{tab:lagrangian}\n\\small\n\\begin{tabular}{lccccc}\n\\toprule\nTarget $\\rho$ & $\\lambda_{\\max}$ & Final $\\lambda$ & Actual sparsity & Deviation \\\\\n\\midrule\n30\\% & 5000 & 5000 (cap) & 0.285 & 5.0\\% \\\\ % exp_id: kl_30pct_s42\n40\\% & 5000 & 625 & 0.398 & 0.5\\% \\\\ % exp_id: kl_40pct_s42\n50\\% & 1000 & 8 & 0.504 & 0.8\\% \\\\ % exp_id: kl_50pct_s42\n70\\% & 1000 & 1000 (cap) & 0.688 & 1.7\\% \\\\ % exp_id: kl_70pct_s42\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nAt 50\\% sparsity, the SwiGLU gate distribution already clusters near the target, so $\\lambda$ remains low (8); the constraint is nearly satisfied by the initial predictor outputs.\nAt 30\\% and 70\\%, the gap between the gate prior and target is larger, driving $\\lambda$ to its respective caps.\nThe 40\\% target converges to $\\lambda = 625$ with only 0.5\\% deviation, illustrating the controller's precision when the target is reachable without saturating.\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=\\columnwidth]{lagrangian_dynamics.pdf}\n\\caption{Adaptive penalty controller convergence across sparsity targets. Upper panel: penalty weight $\\lambda$ (log scale) over training steps. The 30\\% target requires extreme penalty ($\\lambda \\to 5000$) to suppress activations below their natural density, while 50\\% needs only $\\lambda \\approx 8$ since SwiGLU gates already cluster near this sparsity. Lower panel: actual sparsity (solid) converges to the target (dashed) within $\\sim$10 steps via geometric doubling.}\n\\label{fig:lagrangian_dynamics}\n\\end{figure}\n\nTemperature $\\tau$ is annealed linearly from 1.0 to 0.1 over 1000 steps.\nA mild loss increase in the final $\\sim$100 steps is expected: as masks become more binary ($\\tau \\to 0$), discrete rounding noise slightly increases KL divergence, confirming the training is converging toward the hard-mask inference regime.\n\nThe controller reliably drives actual sparsity to within 5\\% of the target across all tested regimes, with $\\lambda$ spanning three orders of magnitude (8 to 5000) via geometric doubling.\n\n\n\\section{Out-of-Distribution Evaluation}\n\\label{app:ood}\n\nTo address concerns about data homogeneity between training (WikiText-103) and evaluation (WikiText-2), we evaluate on C4~\\cite{raffel2020c4} validation set at 50\\% sparsity under TEAL global allocation.\n\n\\begin{table}[h]\n\\centering\n\\caption{Out-of-distribution evaluation on C4 validation (50\\% sparsity, PPL$\\downarrow$).}\n\\label{tab:ood}\n\\small\n\\begin{tabular}{lc}\n\\toprule\nMethod & C4 PPL$\\downarrow$ \\\\\n\\midrule\nDense & 9.21 \\\\\nKL predictor (Ours) & \\textbf{18.40} \\\\ % exp_id: eval_c4_ood_kl50\nTEAL vanilla & 38.75 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe KL-trained predictor achieves 52.5\\% relative advantage over TEAL on out-of-domain data (18.40 vs.\\ 38.75), comparable to or slightly exceeding the 49\\% advantage observed on WikiText-2 (11.79 vs.\\ 23.31), suggesting that KL-trained predictions generalize to held-out data when the evaluation distribution differs from training.\nThis confirms that the predictor learns generalizable neuron importance patterns rather than overfitting to the WikiText training distribution.\n\n\n\\section{Per-Layer Retention Analysis}\n\\label{app:retention}\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=\\columnwidth]{per_layer_retention_chart.pdf}\n\\caption{Per-layer neuron retention under global top-$k$ allocation at 30\\%, 50\\%, and 70\\% sparsity. Dashed lines indicate uniform retention baselines. Late layers (L24--31) are consistently starved due to long-tailed activation distributions, with retention dropping to 28.4\\% (L31) even at 30\\% sparsity. At 70\\%, starvation extends to mid-layers (L10--12: 16.7--20.1\\%), explaining the transition to the capacity-limited regime.}\n\\label{fig:retention}\n\\end{figure}\n\n\n\\section{Training Stability}\n\\label{app:stability}\n\nThree-seed evaluation ($s \\in \\{42, 123, 456\\}$) at 50\\% sparsity under uniform allocation yields PPL $11.92 \\pm 0.07$ (CV=0.6\\%), confirming training stability across random initializations. % exp_id: multi_seed_kl50_uniform\nDownstream metrics are similarly stable: ARC-c $33.8 \\pm 1.2$\\%, WinoGrande $62.9 \\pm 0.1$\\%, MMLU $28.0 \\pm 0.6$\\%, GSM8K $2.2 \\pm 0.1$\\%.\nThe low variance indicates that the KL training landscape is well-conditioned for this predictor architecture, with low sensitivity to initialization.\n",
      "numLines": 192,
      "startLine": 1,
      "totalLines": 192
    }
  },
  "sourceToolAssistantUUID": "5c5daa71-c898-40a8-a8fb-d2fcf9cc2da3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/review_reviewer_1_772f066c",
  "sessionId": "fd7408d6-e7e0-4bb4-8dde-4202758b928d",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-17T08:11:47.848Z_

<details><summary>↩ Tool result · `toolu_01Tgt38YdpC3cbnpSU5goCRZ`</summary>

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
  "parentUuid": "fc53a4b6-7c57-4a12-a6d1-12643d5ada57",
  "isSidechain": false,
  "promptId": "e22b3aa5-f147-4b55-a02c-533b2c761d41",
  "type": "user",
  "uuid": "6d749949-97d8-427c-b122-13cd74b2d49c",
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
  "sourceToolAssistantUUID": "fc53a4b6-7c57-4a12-a6d1-12643d5ada57",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/review_reviewer_1_772f066c",
  "sessionId": "fd7408d6-e7e0-4bb4-8dde-4202758b928d",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-17T08:11:48.304Z_

<details open><summary>🔧 Tool call — Read · `toolu_01YK1Hivu89JVZ6L1jRwrUFS`</summary>

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
  "parentUuid": "6d749949-97d8-427c-b122-13cd74b2d49c",
  "isSidechain": false,
  "requestId": "req_011Cb7oZWy4fYiJASzD2k8VN",
  "type": "assistant",
  "uuid": "a6e56ac6-d183-4757-a21b-125b8b91d851",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/review_reviewer_1_772f066c",
  "sessionId": "fd7408d6-e7e0-4bb4-8dde-4202758b928d",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014pujs8tdAWYSgd6nPAVexn",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 365,
      "cache_creation_input_tokens": 855,
      "cache_read_input_tokens": 31828,
      "output_tokens": 722,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 855,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 365,
          "output_tokens": 722,
          "cache_read_input_tokens": 31828,
          "cache_creation_input_tokens": 855,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 855
          },
          "type": "message"
        }
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

_source line 30 · 2026-05-17T08:11:48.310Z_

<details><summary>↩ Tool result · `toolu_01YK1Hivu89JVZ6L1jRwrUFS`</summary>

```text
1	Activation sparsity reduces the effective computation in SwiGLU-based LLMs by pruning FFN neurons at inference, but existing learned predictors trained with binary cross-entropy (BCE) require error compensation networks due to a structural mismatch: BCE decomposes per neuron while inference uses global top-$k$ allocation across all layers.
2	We train lightweight predictors (2.37M parameters per layer, 75.9M total, $<$1\% of the base model) with KL divergence, which couples all neurons through the output distribution via Gumbel-Sigmoid relaxation, eliminating the need for compensation.
3	On LLaMA-3.1-8B (WikiText-2), our KL-trained predictor achieves perplexity 11.79 at 50\% sparsity without compensation, compared to 23.31 for vanilla TEAL and 27.97 for BCE trained at 2.71$\times$ the compute budget, whose loss saturates, confirming a structural rather than computational failure.
4	Three-seed evaluation confirms training stability (PPL $11.92 \pm 0.07$, CV${<}$1\% under uniform allocation).
5	The KL advantage grows disproportionately with sparsity: 18\% relative improvement at 30\%, 49\% at 50\%, and 82\% at 70\% (PPL 17.91 vs.\ 100.11); KL itself incurs $2.93\times$ the dense baseline, demonstrating substantial output fidelity even at extreme sparsity.
6	Cross-architecture evaluation on Mistral-7B-v0.3 confirms the advantage transfers across SwiGLU architectures at the 7--8B parameter scale, with consistent KL-over-TEAL ratios (within 7\% at $\leq$50\% sparsity).
7	SPON's static bias correction proves near-orthogonal to the predictor (cosine similarity 0.196), providing only 2.4\% relative PPL improvement (12.08$\to$11.79 under \texttt{evaluate.py}).
8	We propose a two-dimensional taxonomy over correction granularity $\times$ training signal coupling that unifies prior methods and identify three distinct sparsity regimes (budget-surplus, budget-constrained, and capacity-limited) that govern the quality-sparsity tradeoff.
9	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a6e56ac6-d183-4757-a21b-125b8b91d851",
  "isSidechain": false,
  "promptId": "e22b3aa5-f147-4b55-a02c-533b2c761d41",
  "type": "user",
  "uuid": "2033b14c-fb84-4453-8766-e551e8bed340",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/abstract.tex",
      "content": "Activation sparsity reduces the effective computation in SwiGLU-based LLMs by pruning FFN neurons at inference, but existing learned predictors trained with binary cross-entropy (BCE) require error compensation networks due to a structural mismatch: BCE decomposes per neuron while inference uses global top-$k$ allocation across all layers.\nWe train lightweight predictors (2.37M parameters per layer, 75.9M total, $<$1\\% of the base model) with KL divergence, which couples all neurons through the output distribution via Gumbel-Sigmoid relaxation, eliminating the need for compensation.\nOn LLaMA-3.1-8B (WikiText-2), our KL-trained predictor achieves perplexity 11.79 at 50\\% sparsity without compensation, compared to 23.31 for vanilla TEAL and 27.97 for BCE trained at 2.71$\\times$ the compute budget, whose loss saturates, confirming a structural rather than computational failure.\nThree-seed evaluation confirms training stability (PPL $11.92 \\pm 0.07$, CV${<}$1\\% under uniform allocation).\nThe KL advantage grows disproportionately with sparsity: 18\\% relative improvement at 30\\%, 49\\% at 50\\%, and 82\\% at 70\\% (PPL 17.91 vs.\\ 100.11); KL itself incurs $2.93\\times$ the dense baseline, demonstrating substantial output fidelity even at extreme sparsity.\nCross-architecture evaluation on Mistral-7B-v0.3 confirms the advantage transfers across SwiGLU architectures at the 7--8B parameter scale, with consistent KL-over-TEAL ratios (within 7\\% at $\\leq$50\\% sparsity).\nSPON's static bias correction proves near-orthogonal to the predictor (cosine similarity 0.196), providing only 2.4\\% relative PPL improvement (12.08$\\to$11.79 under \\texttt{evaluate.py}).\nWe propose a two-dimensional taxonomy over correction granularity $\\times$ training signal coupling that unifies prior methods and identify three distinct sparsity regimes (budget-surplus, budget-constrained, and capacity-limited) that govern the quality-sparsity tradeoff.\n",
      "numLines": 9,
      "startLine": 1,
      "totalLines": 9
    }
  },
  "sourceToolAssistantUUID": "a6e56ac6-d183-4757-a21b-125b8b91d851",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/review_reviewer_1_772f066c",
  "sessionId": "fd7408d6-e7e0-4bb4-8dde-4202758b928d",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-17T08:11:48.778Z_

<details open><summary>🔧 Tool call — Read · `toolu_01YFxFX2kgtYpBD4Ao8VkDY9`</summary>

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
  "parentUuid": "2033b14c-fb84-4453-8766-e551e8bed340",
  "isSidechain": false,
  "requestId": "req_011Cb7oZWy4fYiJASzD2k8VN",
  "type": "assistant",
  "uuid": "670a3f16-7c93-4065-b447-4358f2204e74",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/review_reviewer_1_772f066c",
  "sessionId": "fd7408d6-e7e0-4bb4-8dde-4202758b928d",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014pujs8tdAWYSgd6nPAVexn",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 365,
      "cache_creation_input_tokens": 855,
      "cache_read_input_tokens": 31828,
      "output_tokens": 722,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 855,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 365,
          "output_tokens": 722,
          "cache_read_input_tokens": 31828,
          "cache_creation_input_tokens": 855,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 855
          },
          "type": "message"
        }
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

_source line 32 · 2026-05-17T08:11:48.783Z_

<details><summary>↩ Tool result · `toolu_01YFxFX2kgtYpBD4Ao8VkDY9`</summary>

```text
1	\section{Introduction}
2	
3	SwiGLU feed-forward networks~\cite{shazeer2020glu} in modern LLMs exhibit high contextual sparsity: at any given token, a large fraction of FFN neurons contribute negligibly to the output.
4	Exploiting this sparsity can simplify inference by pruning 50\% of FFN neurons per token (without modifying the pretrained weights), eliminating the need for auxiliary compensation networks.
5	Yet the gap between potential and practice remains wide.
6	Training-free methods such as TEAL~\cite{liu2025teal} select neurons by activation magnitude alone, degrading perplexity from 6.12 (dense) to 23.31 at 50\% sparsity on LLaMA-3.1-8B~\cite{grattafiori2024llama3}, a 281\% increase.
7	Learned predictors~\cite{liu2023dejavu,gautam2026fastforward} close part of this gap by training small auxiliary networks to anticipate which neurons will be important, but they rely on error compensation modules (output rescaling networks or additive correction layers) that add 67.2M parameters and $\sim$2.7\% additional latency overhead at inference.
8	The question is whether a predictor can be trained so that compensation becomes unnecessary.
9	
10	The answer depends on the training objective.
11	Current learned predictors use binary cross-entropy (BCE) loss: each neuron is independently classified as ``keep'' or ``prune'' against an oracle mask derived from the dense model's activations.
12	The gradient of BCE with respect to neuron $j$'s score is $\partial \mathcal{L}_{\text{BCE}} / \partial s_j = \sigma(s_j) - m_j^*$, a function of neuron $j$ alone, independent of every other neuron in the network.
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
28	The predictor itself is a lightweight two-layer MLP (Linear $4096 \to 128$, GELU, Linear $128 \to 14336$) with 2.37M parameters per layer and 75.9M total (under 1\% of the base model), requiring no compensation network at inference.
29	
30	Empirically, the structural argument is borne out across sparsity levels, training budgets, and architectures.
31	At 50\% sparsity on LLaMA-3.1-8B, the KL-trained predictor achieves PPL 11.79 under TEAL's global allocation, compared to 23.31 for vanilla TEAL.
32	BCE trained for 2700 steps (2.71$\times$ our compute budget) reaches only 27.97, and its training loss saturates with $\Delta = -0.006$ over the final 2200 steps, confirming that the failure is structural, not computational.
33	The KL advantage grows disproportionately with sparsity: 18\% relative improvement at 30\%, 49\% at 50\%, and 82\% at 70\%.
34	Evaluation on Mistral-7B-v0.3~\cite{jiang2023mistral} across three sparsity levels confirms the advantage transfers across SwiGLU architectures at the 7--8B parameter scale, with KL-over-TEAL ratios consistent within 7\% at $\leq$50\% sparsity and the same regime boundary where magnitude-based methods catastrophically degrade.
35	We also analyze SPON's~\cite{xu2026spon} static bias correction and find it near-orthogonal to the predictor's effect (cosine similarity 0.196), providing only 2.4\% relative PPL improvement (12.08$\to$11.79); the KL predictor already captures most of the recoverable signal.
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
46	\item We identify three distinct sparsity regimes (budget-surplus at $\leq$30\%, budget-constrained at $\sim$40\%, and capacity-limited at $\geq$50\%) and confirm via SPON orthogonality analysis that static correction provides diminishing returns once a coupled predictor is present.
47	\end{itemize}
48	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "670a3f16-7c93-4065-b447-4358f2204e74",
  "isSidechain": false,
  "promptId": "e22b3aa5-f147-4b55-a02c-533b2c761d41",
  "type": "user",
  "uuid": "a23134c8-f455-4bf3-92ae-b9783183ff96",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/introduction.tex",
      "content": "\\section{Introduction}\n\nSwiGLU feed-forward networks~\\cite{shazeer2020glu} in modern LLMs exhibit high contextual sparsity: at any given token, a large fraction of FFN neurons contribute negligibly to the output.\nExploiting this sparsity can simplify inference by pruning 50\\% of FFN neurons per token (without modifying the pretrained weights), eliminating the need for auxiliary compensation networks.\nYet the gap between potential and practice remains wide.\nTraining-free methods such as TEAL~\\cite{liu2025teal} select neurons by activation magnitude alone, degrading perplexity from 6.12 (dense) to 23.31 at 50\\% sparsity on LLaMA-3.1-8B~\\cite{grattafiori2024llama3}, a 281\\% increase.\nLearned predictors~\\cite{liu2023dejavu,gautam2026fastforward} close part of this gap by training small auxiliary networks to anticipate which neurons will be important, but they rely on error compensation modules (output rescaling networks or additive correction layers) that add 67.2M parameters and $\\sim$2.7\\% additional latency overhead at inference.\nThe question is whether a predictor can be trained so that compensation becomes unnecessary.\n\nThe answer depends on the training objective.\nCurrent learned predictors use binary cross-entropy (BCE) loss: each neuron is independently classified as ``keep'' or ``prune'' against an oracle mask derived from the dense model's activations.\nThe gradient of BCE with respect to neuron $j$'s score is $\\partial \\mathcal{L}_{\\text{BCE}} / \\partial s_j = \\sigma(s_j) - m_j^*$, a function of neuron $j$ alone, independent of every other neuron in the network.\nBut at inference, no neuron is evaluated in isolation.\nTEAL's global top-$k$ mechanism~\\cite{liu2025teal} ranks all neurons across all layers and retains only those above a model-wide threshold.\nWhether neuron $j$ survives depends not on its own score but on how that score compares to the scores of all $L \\times d_{\\text{ff}}$ neurons.\nThis creates a structural mismatch: the training objective decomposes per neuron, while the inference allocation is a global combinatorial decision.\nBCE can achieve $>$90\\% per-neuron classification accuracy against oracle masks yet still produce poor output quality under global allocation, because it optimizes a proxy misaligned with the true objective.\n\nKL divergence resolves this mismatch by coupling all neurons through the output distribution.\nInstead of classifying individual neurons, we minimize $D_{\\text{KL}}(p_{\\text{dense}} \\| p_{\\text{sparse}})$ between the dense and sparse model outputs, training the predictor to preserve the full next-token distribution under pruning.\nThe gradient for neuron $j$ in layer $\\ell$ factors as:\n\\begin{equation*}\n\\frac{\\partial \\mathcal{L}_{\\text{KL}}}{\\partial s_j^{(\\ell)}} = \\frac{\\partial \\mathcal{L}_{\\text{KL}}}{\\partial \\mathbf{z}} \\cdot \\frac{\\partial \\mathbf{z}}{\\partial \\mathbf{h}^{(\\ell)}} \\cdot \\frac{\\partial \\mathbf{h}^{(\\ell)}}{\\partial \\tilde{m}_j^{(\\ell)}} \\cdot \\frac{\\partial \\tilde{m}_j^{(\\ell)}}{\\partial s_j^{(\\ell)}},\n\\end{equation*}\nwhere the Jacobian $\\partial \\mathbf{z} / \\partial \\mathbf{h}^{(\\ell)}$ propagates through all downstream layers, making each neuron's gradient dependent on every other neuron's mask state.\nChanging one neuron's mask affects all output logits; KL captures this because it measures distributional divergence over the entire vocabulary.\nA Gumbel-Sigmoid relaxation~\\cite{jang2017gumbel} provides differentiable mask sampling during training, bridging the gap between soft training masks and hard inference decisions.\nThe predictor itself is a lightweight two-layer MLP (Linear $4096 \\to 128$, GELU, Linear $128 \\to 14336$) with 2.37M parameters per layer and 75.9M total (under 1\\% of the base model), requiring no compensation network at inference.\n\nEmpirically, the structural argument is borne out across sparsity levels, training budgets, and architectures.\nAt 50\\% sparsity on LLaMA-3.1-8B, the KL-trained predictor achieves PPL 11.79 under TEAL's global allocation, compared to 23.31 for vanilla TEAL.\nBCE trained for 2700 steps (2.71$\\times$ our compute budget) reaches only 27.97, and its training loss saturates with $\\Delta = -0.006$ over the final 2200 steps, confirming that the failure is structural, not computational.\nThe KL advantage grows disproportionately with sparsity: 18\\% relative improvement at 30\\%, 49\\% at 50\\%, and 82\\% at 70\\%.\nEvaluation on Mistral-7B-v0.3~\\cite{jiang2023mistral} across three sparsity levels confirms the advantage transfers across SwiGLU architectures at the 7--8B parameter scale, with KL-over-TEAL ratios consistent within 7\\% at $\\leq$50\\% sparsity and the same regime boundary where magnitude-based methods catastrophically degrade.\nWe also analyze SPON's~\\cite{xu2026spon} static bias correction and find it near-orthogonal to the predictor's effect (cosine similarity 0.196), providing only 2.4\\% relative PPL improvement (12.08$\\to$11.79); the KL predictor already captures most of the recoverable signal.\n\nTo situate these findings, we propose a two-dimensional taxonomy (Figure~\\ref{fig:taxonomy}) that classifies sparsity prediction methods along \\emph{correction granularity} (static, per-layer, per-token) and \\emph{training signal coupling} (decomposed, intermediate, coupled).\nPrior methods occupy distinct cells: SPON~\\cite{xu2026spon} combines static correction with coupled KL training; ShadowLLM~\\cite{akhauri2024shadowllm} uses per-layer prediction with intermediate MSE; FastForward~\\cite{gautam2026fastforward} and DejaVu~\\cite{liu2023dejavu} achieve per-token granularity but with decomposed BCE objectives.\nNo prior work has combined per-token contextual prediction with a coupled training signal.\nOur method fills this cell, unifying input-dependent mask generation with an objective that reflects global neuron interactions through the output distribution.\n\nOur contributions are:\n\\begin{itemize}[nosep,leftmargin=*]\n\\item We show that a KL-trained contextual predictor eliminates the need for error compensation networks in activation sparsity, and provide a formal gradient analysis explaining the structural mismatch between per-neuron BCE training and global top-$k$ inference allocation.\n\\item We organize prior work via a 2D framework (correction granularity $\\times$ training signal coupling, Figure~\\ref{fig:taxonomy}) that situates our method in a previously unexplored cell: per-token prediction with coupled training signals.\n\\item We identify three distinct sparsity regimes (budget-surplus at $\\leq$30\\%, budget-constrained at $\\sim$40\\%, and capacity-limited at $\\geq$50\\%) and confirm via SPON orthogonality analysis that static correction provides diminishing returns once a coupled predictor is present.\n\\end{itemize}\n",
      "numLines": 48,
      "startLine": 1,
      "totalLines": 48
    }
  },
  "sourceToolAssistantUUID": "670a3f16-7c93-4065-b447-4358f2204e74",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/review_reviewer_1_772f066c",
  "sessionId": "fd7408d6-e7e0-4bb4-8dde-4202758b928d",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-17T08:11:49.209Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Uo84XSeQ94msgrYtSJ8a6A`</summary>

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
  "parentUuid": "a23134c8-f455-4bf3-92ae-b9783183ff96",
  "isSidechain": false,
  "requestId": "req_011Cb7oZWy4fYiJASzD2k8VN",
  "type": "assistant",
  "uuid": "038ccf17-a427-4419-9890-ab2ce47580df",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/review_reviewer_1_772f066c",
  "sessionId": "fd7408d6-e7e0-4bb4-8dde-4202758b928d",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014pujs8tdAWYSgd6nPAVexn",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 365,
      "cache_creation_input_tokens": 855,
      "cache_read_input_tokens": 31828,
      "output_tokens": 722,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 855,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 365,
          "output_tokens": 722,
          "cache_read_input_tokens": 31828,
          "cache_creation_input_tokens": 855,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 855
          },
          "type": "message"
        }
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

_source line 34 · 2026-05-17T08:11:49.214Z_

<details><summary>↩ Tool result · `toolu_01Uo84XSeQ94msgrYtSJ8a6A`</summary>

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
41	With 32 independent predictors (one per layer), the total overhead is 75.9M parameters, less than 1\% of the 8B base model.
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
63	In our setting, STE produces discontinuous gradient signals: small parameter changes can flip many neurons simultaneously, causing violent oscillations in the penalty weight and failure to converge to the target sparsity.
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
79	We use forward KL (mean-seeking) rather than reverse KL, as the goal is to preserve the dense model's primary predictions rather than explore alternative modes.
80	No temperature scaling ($T{=}1$) is applied~\cite{hinton2015distilling}.
81	
82	
83	\subsection{Adaptive Penalty Sparsity Controller}
84	\label{sec:method:lagrangian}
85	
86	We enforce a model-level sparsity target $\rho$ via constrained optimization.
87	Let $\bar{s} = \frac{1}{L} \sum_\ell \frac{1}{d_{\text{ff}}} \sum_j \tilde{m}_j^{(\ell)}$ denote the average fraction of retained neurons.
88	The constrained problem is:
89	\begin{align}
90	\min_\theta \; \mathcal{L}_{\text{KL}} \quad \text{s.t.} \quad \bar{s} \leq 1 - \rho.
91	\label{eq:constrained}
92	\end{align}
93	We relax this via an adaptive penalty controller:
94	\begin{align}
95	\mathcal{L} = \mathcal{L}_{\text{KL}} + \lambda \cdot \text{clamp}(|\bar{s} - (1 - \rho)| - \epsilon, \min{=}0)^2,
96	\label{eq:lagrangian}
97	\end{align}
98	where $\epsilon = 0.02$ is a deadzone margin that prevents $\lambda$ from responding to small constraint violations.
99	The penalty weight $\lambda$ is updated multiplicatively at each step:
100	\begin{align}
101	\lambda \leftarrow \begin{cases} \lambda \times 2 & \text{if } \bar{s} > (1-\rho) + \epsilon \\ \lambda \times 0.5 & \text{if } \bar{s} < (1-\rho) - \epsilon \\ \lambda & \text{otherwise} \end{cases}
102	\label{eq:dual_update}
103	\end{align}
104	with $\lambda$ clamped to $[\lambda_{\text{floor}}, \lambda_{\max}]$ where $\lambda_{\text{floor}} = 0.01$ and $\lambda_{\max} \in \{1000, 5000\}$ depending on the target.
105	The geometric doubling is parameter-free (no step-size tuning) and converges within 40--110 steps across all targets (Figure~\ref{fig:lagrangian_dynamics}); the deadzone prevents oscillation once sparsity is within $\pm$2\%.\footnote{Our update rule resembles the augmented Lagrangian method but replaces gradient-based dual updates with a multiplicative schedule for training stability. We term it an adaptive penalty controller to distinguish from formal dual methods that guarantee KKT satisfaction.}
106	
107	
108	\subsection{Gradient-Based Motivation: BCE vs.\ KL}
109	\label{sec:method:gradient}
110	
111	We analyze the structural difference between BCE and KL training signals to motivate why KL distillation is better suited to global top-$k$ inference.
112	
113	\paragraph{BCE gradient structure.}
114	The standard approach trains the predictor against oracle masks $m_j^* = \mathbf{1}[|g_j| \geq \text{top-}k\text{ threshold}]$ derived from the dense model's activation magnitudes.
115	The loss decomposes per neuron:
116	\begin{align}
117	\mathcal{L}_{\text{BCE}} = -\frac{1}{d_{\text{ff}}} \sum_{j=1}^{d_{\text{ff}}} \bigl[ m_j^* \log \sigma(s_j) + (1 - m_j^*) \log(1 - \sigma(s_j)) \bigr].
118	\label{eq:bce}
119	\end{align}
120	The gradient with respect to predictor logit $s_j$ is:
121	\begin{align}
122	\frac{\partial \mathcal{L}_{\text{BCE}}}{\partial s_j} = \sigma(s_j) - m_j^*.
123	\label{eq:bce_grad}
124	\end{align}
125	This gradient depends \emph{only} on neuron $j$'s own prediction and target.
126	Each neuron is trained independently; there is no inter-neuron coupling in the learning signal.
127	
128	\paragraph{KL gradient structure.}
129	Under KL distillation, the gradient for predictor logit $s_j^{(\ell)}$ in layer $\ell$ is:
130	\begin{align}
131	\frac{\partial \mathcal{L}_{\text{KL}}}{\partial s_j^{(\ell)}} = \underbrace{\frac{\partial \mathcal{L}_{\text{KL}}}{\partial \mathbf{z}_{\text{sparse}}}}_{\text{(a)}} \cdot \underbrace{\frac{\partial \mathbf{z}_{\text{sparse}}}{\partial \mathbf{h}^{(\ell)}}}_{\text{(b)}} \cdot \underbrace{\frac{\partial \mathbf{h}^{(\ell)}}{\partial \tilde{m}_j^{(\ell)}}}_{\text{(c)}} \cdot \underbrace{\frac{\partial \tilde{m}_j^{(\ell)}}{\partial s_j^{(\ell)}}}_{\text{(d)}},
132	\label{eq:kl_grad}
133	\end{align}
134	where each factor has a distinct role:
135	\begin{itemize}
136	\item[\textbf{(a)}] The KL gradient at the output, reflecting how each logit component deviates from the dense distribution.
137	\item[\textbf{(b)}] The Jacobian through all downstream layers from layer $\ell$'s output to the final logits. This factor couples neuron $j$'s gradient to the state of every other retained neuron in layers $\ell, \ell{+}1, \ldots, L$, because the sparse hidden state propagates through subsequent attention and FFN operations.
138	\item[\textbf{(c)}] The local mask effect: $\partial \mathbf{h}^{(\ell)} / \partial \tilde{m}_j^{(\ell)} = (g_j^{(\ell)} \cdot [\mathbf{x}^{(\ell)} \mathbf{W}_u^{(\ell)}]_j) \cdot \mathbf{W}_{d,j}^{(\ell)}$, projecting through the down-projection to affect the full $d$-dimensional hidden state.
139	\item[\textbf{(d)}] The Gumbel-Sigmoid derivative, providing the differentiable path from logit to mask.
140	\end{itemize}
141	
142	\paragraph{The structural mismatch.}
143	The key observation is that factor (b) makes the KL gradient for neuron $j$ depend on \emph{all} other neurons' mask values.
144	BCE's factorized gradient (Eq.~\ref{eq:bce_grad}) optimizes each neuron's prediction accuracy in isolation, but TEAL inference selects neurons via a global ranking across all layers.
145	Under global top-$k$, the decision to retain neuron $j$ depends on the scores of all other neurons, a combinatorial interaction that BCE cannot capture.
146	
147	Concretely, BCE achieves high per-neuron accuracy ($>$90\% oracle agreement) yet produces poor output under TEAL, because it optimizes a proxy misaligned with output preservation under global budget allocation.
148	KL directly optimizes the end-to-end objective, with gradients that reflect inter-neuron dependencies through the computation graph.
149	
150	\paragraph{Empirical verification.}
151	Measuring gradient signal-to-noise ratio\footnote{$\text{SNR}_\ell = \|\mathbb{E}[\nabla_{\theta_\ell} \mathcal{L}]\|_2^2 / \text{Var}[\nabla_{\theta_\ell} \mathcal{L}]$, expectation over mini-batches.} over 80 steps on LLaMA-3.1-8B (C4 data), KL achieves $5.76\times$ higher average SNR than BCE ($5.77{\times}10^{-5}$ vs.\ $1.00{\times}10^{-5}$).
152	The advantage concentrates in early layers (0--4: ratio $34$--$156\times$) where factor~(b)'s Jacobian chain traverses the full remaining network; late layers (27--31: $1.7$--$3.8\times$) show reduced advantage as the shorter chain limits factor~(b)'s contribution.
153	BCE's early-layer SNR collapses to ${\sim}10^{-8}$ after step~10, explaining why extended training cannot close the gap.
154	
155	\subsection{Two-Dimensional Taxonomy of Sparsity Prediction Methods}
156	\label{sec:method:taxonomy}
157	
158	We organize prior work along two axes: \emph{correction granularity} (how the mask adapts to input) and \emph{training signal coupling} (whether the objective captures inter-neuron dependencies).
159	
160	\begin{table}[t]
161	\centering
162	\caption{Taxonomy of learned sparsity prediction methods. Rows indicate correction granularity; columns indicate training signal coupling. Our method fills a previously unexplored cell.}
163	\label{tab:taxonomy}
164	\resizebox{\columnwidth}{!}{
165	\begin{tabular}{lccc}
166	\toprule
167	 & Decomposed (BCE) & Intermediate (MSE) & Coupled (KL) \\
168	\midrule
169	Static & --- & --- & SPON \\
170	Per-layer & --- & ShadowLLM & --- \\
171	Per-token & FastForward & --- & \textbf{Ours} \\
172	\bottomrule
173	\end{tabular}}
174	\end{table}
175	
176	\paragraph{Correction granularity.}
177	\emph{Static} methods~\cite{xu2026spon} learn a fixed bias vector per layer that does not depend on the input token.
178	\emph{Per-layer} methods~\cite{akhauri2024shadowllm} condition on a layer-level summary (e.g., the attention output) but share predictions across tokens within a layer.
179	\emph{Per-token} methods~\cite{gautam2026fastforward,liu2023dejavu} produce a unique mask for each input position.
180	
181	\paragraph{Training signal coupling.}
182	\emph{Decomposed} objectives (BCE) treat each neuron independently, optimizing per-element classification against an oracle mask.
183	\emph{Intermediate} objectives (MSE on hidden states) capture local coupling within a single layer but not end-to-end output effects.
184	\emph{Coupled} objectives (KL on output distribution) propagate gradients through the full forward pass, reflecting how all mask decisions jointly affect the final distribution.
185	
186	SPON~\cite{xu2026spon} operates at the intersection of static granularity and coupled training: it distills a per-layer bias correction via KL but cannot adapt to per-input neuron importance.
187	FastForward~\cite{gautam2026fastforward} achieves per-token granularity but uses BCE training, losing inter-neuron coupling.
188	Our method combines per-token contextual prediction with coupled KL training (Table~\ref{tab:taxonomy}), unifying the advantages of both axes: input-dependent mask generation trained with a signal that captures global neuron interactions through the output distribution.
189	
190	\begin{figure}[t]
191	\centering
192	\includegraphics[width=\columnwidth]{fig1_overview.pdf}
193	\caption{Method overview: a lightweight per-layer predictor produces importance scores trained via KL divergence with Gumbel-Sigmoid relaxation. At inference, scores feed TEAL's global top-$k$ allocation without compensation networks.}
194	\label{fig:taxonomy}
195	\end{figure}
196	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "038ccf17-a427-4419-9890-ab2ce47580df",
  "isSidechain": false,
  "promptId": "e22b3aa5-f147-4b55-a02c-533b2c761d41",
  "type": "user",
  "uuid": "5f3f3f22-e219-49b1-940f-f0d56bc485c7",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/method.tex",
      "content": "\\section{Method}\n\\label{sec:method}\n\nWe present a KL distillation framework for training contextual sparsity predictors in SwiGLU-based language models.\nThe method replaces per-neuron binary classification (BCE) with an output-distribution objective that couples all pruning decisions through the model's forward pass, eliminating the need for auxiliary error compensation networks at inference.\n\n\\subsection{Problem Formulation}\n\\label{sec:method:formulation}\n\nConsider a pretrained transformer with $L$ layers, each containing a SwiGLU feed-forward network~\\cite{shazeer2020glu}.\nFor layer $\\ell$, the FFN computes:\n\\begin{align}\n\\mathbf{y}^{(\\ell)} = \\bigl(\\sigma(\\mathbf{x}^{(\\ell)} \\mathbf{W}_g^{(\\ell)}) \\odot \\mathbf{x}^{(\\ell)} \\mathbf{W}_u^{(\\ell)}\\bigr) \\mathbf{W}_d^{(\\ell)},\n\\label{eq:swiglu}\n\\end{align}\nwhere $\\mathbf{x}^{(\\ell)} \\in \\mathbb{R}^{d}$ is the hidden state after attention ($d{=}4096$), $\\sigma$ denotes SiLU, $\\mathbf{W}_g^{(\\ell)}, \\mathbf{W}_u^{(\\ell)} \\in \\mathbb{R}^{d \\times d_{\\text{ff}}}$ and $\\mathbf{W}_d^{(\\ell)} \\in \\mathbb{R}^{d_{\\text{ff}} \\times d}$ are the gate, up-projection, and down-projection matrices, and $d_{\\text{ff}}{=}14{,}336$.\n\nDefine the gate activation $\\mathbf{g}^{(\\ell)} = \\sigma(\\mathbf{x}^{(\\ell)} \\mathbf{W}_g^{(\\ell)}) \\in \\mathbb{R}^{d_{\\text{ff}}}$.\nEach element $g_j^{(\\ell)}$ determines the contribution of neuron $j$ to the output.\nWe introduce a binary mask $\\mathbf{m}^{(\\ell)} \\in \\{0,1\\}^{d_{\\text{ff}}}$ that zeros out pruned neurons:\n\\begin{align}\n\\mathbf{y}_{\\text{sparse}}^{(\\ell)} = \\bigl(\\mathbf{m}^{(\\ell)} \\odot \\mathbf{g}^{(\\ell)} \\odot \\mathbf{x}^{(\\ell)} \\mathbf{W}_u^{(\\ell)}\\bigr) \\mathbf{W}_d^{(\\ell)}.\n\\label{eq:sparse_ffn}\n\\end{align}\nOur goal is to learn a mask predictor $f_\\theta^{(\\ell)}(\\mathbf{h}) \\to \\mathbf{s}^{(\\ell)} \\in (0,1)^{d_{\\text{ff}}}$ that produces per-neuron importance scores from the pre-FFN hidden state $\\mathbf{h}$.\nAt inference, the scores are fed to a global top-$k$ allocation mechanism~\\cite{liu2025teal} that distributes the sparsity budget across layers non-uniformly, retaining the $(1{-}\\rho) \\times L \\times d_{\\text{ff}}$ highest-scoring neurons model-wide for a target sparsity ratio $\\rho$.\n\n\n\\subsection{Predictor Architecture}\n\\label{sec:method:predictor}\n\nEach layer $\\ell$ has an independent two-layer MLP predictor:\n\\begin{align}\nf_\\theta^{(\\ell)}(\\mathbf{h}) = \\text{GELU}(\\mathbf{h} \\mathbf{W}_1^{(\\ell)}) \\, \\mathbf{W}_2^{(\\ell)},\n\\label{eq:predictor}\n\\end{align}\nwhere $\\mathbf{W}_1^{(\\ell)} \\in \\mathbb{R}^{d \\times d_b}$ and $\\mathbf{W}_2^{(\\ell)} \\in \\mathbb{R}^{d_b \\times d_{\\text{ff}}}$ with bottleneck dimension $d_b{=}128$.\nThe predictor takes the hidden state after attention (before the FFN) and outputs $d_{\\text{ff}}$-dimensional logits $\\mathbf{s}^{(\\ell)}$, from which the mask is derived.\n\nEach predictor has $(4096 \\times 128) + (128 \\times 14336) = 2.37\\text{M}$ parameters.\nWith 32 independent predictors (one per layer), the total overhead is 75.9M parameters, less than 1\\% of the 8B base model.\nThe predictors operate independently across layers, requiring no cross-layer communication at inference.\n\n\n\\subsection{Gumbel-Sigmoid Relaxation}\n\\label{sec:method:gumbel}\n\nThe hard mask $m_j = \\mathbf{1}[s_j > \\text{threshold}]$ is non-differentiable, preventing gradient flow from the KL objective through the mask to the predictor parameters.\nWe apply Gumbel-Sigmoid relaxation~\\cite{jang2017gumbel} to produce differentiable soft masks:\n\\begin{align}\n\\tilde{m}_j = \\sigma_\\tau\\!\\left(\\log \\frac{s_j}{1 - s_j} + g_1 - g_2\\right), \\quad g_1, g_2 \\sim \\text{Gumbel}(0,1),\n\\label{eq:gumbel}\n\\end{align}\nwhere $\\sigma_\\tau(x) = \\text{sigmoid}(x / \\tau)$ and $\\tau$ is a temperature parameter.\nThe Gumbel noise provides stochastic exploration of mask configurations during training, while the temperature controls sharpness: as $\\tau \\to 0$, $\\tilde{m}_j$ approaches a binary decision.\n\nWe anneal $\\tau$ linearly from 1.0 to 0.1 over training.\nAt high temperature, the soft mask permits gradient flow through all neurons, enabling broad exploration.\nAs temperature decreases, the mask concentrates on confident decisions, approximating the hard allocation used at inference.\n\n\\paragraph{Comparison with Straight-Through Estimation.}\nThe straight-through estimator (STE)~\\cite{bengio2013ste} applies a hard threshold in the forward pass and passes gradients through unchanged ($\\partial m / \\partial s = 1$).\nIn our setting, STE produces discontinuous gradient signals: small parameter changes can flip many neurons simultaneously, causing violent oscillations in the penalty weight and failure to converge to the target sparsity.\nGumbel relaxation eliminates this pathology, contributing a 34.5\\% improvement (PPL 15.77 $\\to$ 11.79 at 50\\% sparsity), as we verify empirically in \\S\\ref{sec:experiments}.\n\n\n\\subsection{KL Divergence Training Objective}\n\\label{sec:method:kl}\n\nLet $\\mathbf{z}_{\\text{dense}}$ denote the output logits from a full dense forward pass, and $\\mathbf{z}_{\\text{sparse}}$ the logits from a forward pass with predictor-generated soft masks $\\{\\tilde{\\mathbf{m}}^{(\\ell)}\\}_\\ell$ applied at every layer.\nWe minimize the forward KL divergence between the dense and sparse output distributions:\n\\begin{align}\n\\mathcal{L}_{\\text{KL}} = D_{\\text{KL}}(p_{\\text{dense}} \\,\\|\\, p_{\\text{sparse}}) = \\sum_{v} p_{\\text{dense}}^{(v)} \\log \\frac{p_{\\text{dense}}^{(v)}}{p_{\\text{sparse}}^{(v)}},\n\\label{eq:kl_loss}\n\\end{align}\nwhere $p_{\\text{dense}} = \\text{softmax}(\\mathbf{z}_{\\text{dense}})$ and $p_{\\text{sparse}} = \\text{softmax}(\\mathbf{z}_{\\text{sparse}})$, summed over the vocabulary $v$ and averaged over sequence positions.\nThe base model is frozen; only the predictor parameters receive gradients.\n\nWe use forward KL (mean-seeking) rather than reverse KL, as the goal is to preserve the dense model's primary predictions rather than explore alternative modes.\nNo temperature scaling ($T{=}1$) is applied~\\cite{hinton2015distilling}.\n\n\n\\subsection{Adaptive Penalty Sparsity Controller}\n\\label{sec:method:lagrangian}\n\nWe enforce a model-level sparsity target $\\rho$ via constrained optimization.\nLet $\\bar{s} = \\frac{1}{L} \\sum_\\ell \\frac{1}{d_{\\text{ff}}} \\sum_j \\tilde{m}_j^{(\\ell)}$ denote the average fraction of retained neurons.\nThe constrained problem is:\n\\begin{align}\n\\min_\\theta \\; \\mathcal{L}_{\\text{KL}} \\quad \\text{s.t.} \\quad \\bar{s} \\leq 1 - \\rho.\n\\label{eq:constrained}\n\\end{align}\nWe relax this via an adaptive penalty controller:\n\\begin{align}\n\\mathcal{L} = \\mathcal{L}_{\\text{KL}} + \\lambda \\cdot \\text{clamp}(|\\bar{s} - (1 - \\rho)| - \\epsilon, \\min{=}0)^2,\n\\label{eq:lagrangian}\n\\end{align}\nwhere $\\epsilon = 0.02$ is a deadzone margin that prevents $\\lambda$ from responding to small constraint violations.\nThe penalty weight $\\lambda$ is updated multiplicatively at each step:\n\\begin{align}\n\\lambda \\leftarrow \\begin{cases} \\lambda \\times 2 & \\text{if } \\bar{s} > (1-\\rho) + \\epsilon \\\\ \\lambda \\times 0.5 & \\text{if } \\bar{s} < (1-\\rho) - \\epsilon \\\\ \\lambda & \\text{otherwise} \\end{cases}\n\\label{eq:dual_update}\n\\end{align}\nwith $\\lambda$ clamped to $[\\lambda_{\\text{floor}}, \\lambda_{\\max}]$ where $\\lambda_{\\text{floor}} = 0.01$ and $\\lambda_{\\max} \\in \\{1000, 5000\\}$ depending on the target.\nThe geometric doubling is parameter-free (no step-size tuning) and converges within 40--110 steps across all targets (Figure~\\ref{fig:lagrangian_dynamics}); the deadzone prevents oscillation once sparsity is within $\\pm$2\\%.\\footnote{Our update rule resembles the augmented Lagrangian method but replaces gradient-based dual updates with a multiplicative schedule for training stability. We term it an adaptive penalty controller to distinguish from formal dual methods that guarantee KKT satisfaction.}\n\n\n\\subsection{Gradient-Based Motivation: BCE vs.\\ KL}\n\\label{sec:method:gradient}\n\nWe analyze the structural difference between BCE and KL training signals to motivate why KL distillation is better suited to global top-$k$ inference.\n\n\\paragraph{BCE gradient structure.}\nThe standard approach trains the predictor against oracle masks $m_j^* = \\mathbf{1}[|g_j| \\geq \\text{top-}k\\text{ threshold}]$ derived from the dense model's activation magnitudes.\nThe loss decomposes per neuron:\n\\begin{align}\n\\mathcal{L}_{\\text{BCE}} = -\\frac{1}{d_{\\text{ff}}} \\sum_{j=1}^{d_{\\text{ff}}} \\bigl[ m_j^* \\log \\sigma(s_j) + (1 - m_j^*) \\log(1 - \\sigma(s_j)) \\bigr].\n\\label{eq:bce}\n\\end{align}\nThe gradient with respect to predictor logit $s_j$ is:\n\\begin{align}\n\\frac{\\partial \\mathcal{L}_{\\text{BCE}}}{\\partial s_j} = \\sigma(s_j) - m_j^*.\n\\label{eq:bce_grad}\n\\end{align}\nThis gradient depends \\emph{only} on neuron $j$'s own prediction and target.\nEach neuron is trained independently; there is no inter-neuron coupling in the learning signal.\n\n\\paragraph{KL gradient structure.}\nUnder KL distillation, the gradient for predictor logit $s_j^{(\\ell)}$ in layer $\\ell$ is:\n\\begin{align}\n\\frac{\\partial \\mathcal{L}_{\\text{KL}}}{\\partial s_j^{(\\ell)}} = \\underbrace{\\frac{\\partial \\mathcal{L}_{\\text{KL}}}{\\partial \\mathbf{z}_{\\text{sparse}}}}_{\\text{(a)}} \\cdot \\underbrace{\\frac{\\partial \\mathbf{z}_{\\text{sparse}}}{\\partial \\mathbf{h}^{(\\ell)}}}_{\\text{(b)}} \\cdot \\underbrace{\\frac{\\partial \\mathbf{h}^{(\\ell)}}{\\partial \\tilde{m}_j^{(\\ell)}}}_{\\text{(c)}} \\cdot \\underbrace{\\frac{\\partial \\tilde{m}_j^{(\\ell)}}{\\partial s_j^{(\\ell)}}}_{\\text{(d)}},\n\\label{eq:kl_grad}\n\\end{align}\nwhere each factor has a distinct role:\n\\begin{itemize}\n\\item[\\textbf{(a)}] The KL gradient at the output, reflecting how each logit component deviates from the dense distribution.\n\\item[\\textbf{(b)}] The Jacobian through all downstream layers from layer $\\ell$'s output to the final logits. This factor couples neuron $j$'s gradient to the state of every other retained neuron in layers $\\ell, \\ell{+}1, \\ldots, L$, because the sparse hidden state propagates through subsequent attention and FFN operations.\n\\item[\\textbf{(c)}] The local mask effect: $\\partial \\mathbf{h}^{(\\ell)} / \\partial \\tilde{m}_j^{(\\ell)} = (g_j^{(\\ell)} \\cdot [\\mathbf{x}^{(\\ell)} \\mathbf{W}_u^{(\\ell)}]_j) \\cdot \\mathbf{W}_{d,j}^{(\\ell)}$, projecting through the down-projection to affect the full $d$-dimensional hidden state.\n\\item[\\textbf{(d)}] The Gumbel-Sigmoid derivative, providing the differentiable path from logit to mask.\n\\end{itemize}\n\n\\paragraph{The structural mismatch.}\nThe key observation is that factor (b) makes the KL gradient for neuron $j$ depend on \\emph{all} other neurons' mask values.\nBCE's factorized gradient (Eq.~\\ref{eq:bce_grad}) optimizes each neuron's prediction accuracy in isolation, but TEAL inference selects neurons via a global ranking across all layers.\nUnder global top-$k$, the decision to retain neuron $j$ depends on the scores of all other neurons, a combinatorial interaction that BCE cannot capture.\n\nConcretely, BCE achieves high per-neuron accuracy ($>$90\\% oracle agreement) yet produces poor output under TEAL, because it optimizes a proxy misaligned with output preservation under global budget allocation.\nKL directly optimizes the end-to-end objective, with gradients that reflect inter-neuron dependencies through the computation graph.\n\n\\paragraph{Empirical verification.}\nMeasuring gradient signal-to-noise ratio\\footnote{$\\text{SNR}_\\ell = \\|\\mathbb{E}[\\nabla_{\\theta_\\ell} \\mathcal{L}]\\|_2^2 / \\text{Var}[\\nabla_{\\theta_\\ell} \\mathcal{L}]$, expectation over mini-batches.} over 80 steps on LLaMA-3.1-8B (C4 data), KL achieves $5.76\\times$ higher average SNR than BCE ($5.77{\\times}10^{-5}$ vs.\\ $1.00{\\times}10^{-5}$).\nThe advantage concentrates in early layers (0--4: ratio $34$--$156\\times$) where factor~(b)'s Jacobian chain traverses the full remaining network; late layers (27--31: $1.7$--$3.8\\times$) show reduced advantage as the shorter chain limits factor~(b)'s contribution.\nBCE's early-layer SNR collapses to ${\\sim}10^{-8}$ after step~10, explaining why extended training cannot close the gap.\n\n\\subsection{Two-Dimensional Taxonomy of Sparsity Prediction Methods}\n\\label{sec:method:taxonomy}\n\nWe organize prior work along two axes: \\emph{correction granularity} (how the mask adapts to input) and \\emph{training signal coupling} (whether the objective captures inter-neuron dependencies).\n\n\\begin{table}[t]\n\\centering\n\\caption{Taxonomy of learned sparsity prediction methods. Rows indicate correction granularity; columns indicate training signal coupling. Our method fills a previously unexplored cell.}\n\\label{tab:taxonomy}\n\\resizebox{\\columnwidth}{!}{\n\\begin{tabular}{lccc}\n\\toprule\n & Decomposed (BCE) & Intermediate (MSE) & Coupled (KL) \\\\\n\\midrule\nStatic & --- & --- & SPON \\\\\nPer-layer & --- & ShadowLLM & --- \\\\\nPer-token & FastForward & --- & \\textbf{Ours} \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\n\\paragraph{Correction granularity.}\n\\emph{Static} methods~\\cite{xu2026spon} learn a fixed bias vector per layer that does not depend on the input token.\n\\emph{Per-layer} methods~\\cite{akhauri2024shadowllm} condition on a layer-level summary (e.g., the attention output) but share predictions across tokens within a layer.\n\\emph{Per-token} methods~\\cite{gautam2026fastforward,liu2023dejavu} produce a unique mask for each input position.\n\n\\paragraph{Training signal coupling.}\n\\emph{Decomposed} objectives (BCE) treat each neuron independently, optimizing per-element classification against an oracle mask.\n\\emph{Intermediate} objectives (MSE on hidden states) capture local coupling within a single layer but not end-to-end output effects.\n\\emph{Coupled} objectives (KL on output distribution) propagate gradients through the full forward pass, reflecting how all mask decisions jointly affect the final distribution.\n\nSPON~\\cite{xu2026spon} operates at the intersection of static granularity and coupled training: it distills a per-layer bias correction via KL but cannot adapt to per-input neuron importance.\nFastForward~\\cite{gautam2026fastforward} achieves per-token granularity but uses BCE training, losing inter-neuron coupling.\nOur method combines per-token contextual prediction with coupled KL training (Table~\\ref{tab:taxonomy}), unifying the advantages of both axes: input-dependent mask generation trained with a signal that captures global neuron interactions through the output distribution.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{fig1_overview.pdf}\n\\caption{Method overview: a lightweight per-layer predictor produces importance scores trained via KL divergence with Gumbel-Sigmoid relaxation. At inference, scores feed TEAL's global top-$k$ allocation without compensation networks.}\n\\label{fig:taxonomy}\n\\end{figure}\n",
      "numLines": 196,
      "startLine": 1,
      "totalLines": 196
    }
  },
  "sourceToolAssistantUUID": "038ccf17-a427-4419-9890-ab2ce47580df",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/review_reviewer_1_772f066c",
  "sessionId": "fd7408d6-e7e0-4bb4-8dde-4202758b928d",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-17T08:11:49.686Z_

<details open><summary>🔧 Tool call — Read · `toolu_01EJpUJf8vYioFf8NdjqS1Zu`</summary>

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
  "parentUuid": "5f3f3f22-e219-49b1-940f-f0d56bc485c7",
  "isSidechain": false,
  "requestId": "req_011Cb7oZWy4fYiJASzD2k8VN",
  "type": "assistant",
  "uuid": "858fb799-ef9a-44ba-b998-4153d3b67240",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/review_reviewer_1_772f066c",
  "sessionId": "fd7408d6-e7e0-4bb4-8dde-4202758b928d",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014pujs8tdAWYSgd6nPAVexn",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 365,
      "cache_creation_input_tokens": 855,
      "cache_read_input_tokens": 31828,
      "output_tokens": 722,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 855,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 365,
          "output_tokens": 722,
          "cache_read_input_tokens": 31828,
          "cache_creation_input_tokens": 855,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 855
          },
          "type": "message"
        }
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

_source line 36 · 2026-05-17T08:11:49.692Z_

<details><summary>↩ Tool result · `toolu_01EJpUJf8vYioFf8NdjqS1Zu`</summary>

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
11	All predictors are trained for 1000 steps on WikiText-103 with sequence length 2048 and batch size 4, using AdamW~\cite{loshchilov2019adamw} with learning rate $1 \times 10^{-3}$ and cosine decay.
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
29	Uniform allocation at 30\% recovers MMLU to 40.61\% (+15.3pp over KL-global's 25.27\%): global top-$k$ starves late layers (L31 retention 28.4\%) while uniform guarantees capacity in logit-forming layers (\S\ref{sec:scaling}). % exp_id: bench_kl30_uniform
30	
31	At 50\% sparsity, KL distillation over vanilla TEAL widens the PPL advantage: 11.79 vs.\ 23.31, a 49\% reduction. % exp_id: bench_kl50_global, bench_teal50
32	The predictor also generalizes to held-out data (C4 validation: 52.5\% advantage over TEAL; see Appendix~\ref{app:ood}).
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
66	The failure is structural: BCE achieves +13pp oracle F1 (0.613 vs.\ 0.540) yet 91\% worse PPL (22.51 vs.\ 11.79), and KL's near-random precision (0.51) confirms it learns a different mask optimized for distributional fidelity rather than magnitude matching. % exp_id: f1_oracle_analysis, bce_isocompute_s42
67	
68	
69	\subsection{Ablation Studies}
70	
71	Table~\ref{tab:ablation} isolates the contribution of each design choice at 50\% sparsity.
72	
73	\begin{table}[t]
74	\centering
75	\caption{Ablation at 50\% sparsity on LLaMA-3.1-8B (WikiText-2 PPL$\downarrow$, unified benchmark protocol).}
76	\label{tab:ablation}
77	\small
78	\begin{tabular}{lcc}
79	\toprule
80	Configuration & PPL$\downarrow$ & $\Delta$ from Ours \\
81	\midrule
82	\multicolumn{3}{l}{\textit{KL-based variants}} \\
83	Forward KL + Gumbel (Ours) & \textbf{11.79} & --- \\ % exp_id: bench_kl50_global
84	JSD (symmetric) + Gumbel & 12.54 & +0.75 \\ % exp_id: jsd_ablation_s42
85	Reverse KL + Gumbel & 12.80 & +1.01 \\ % exp_id: reverse_kl_ablation_s42
86	Forward KL + STE & 15.77 & +3.98 \\ % exp_id: ste_baseline_s42
87	\midrule
88	\multicolumn{3}{l}{\textit{BCE-based variants}} \\
89	BCE + Compensation (hard mask) & 25.44 & +13.65 \\ % exp_id: bce_comp_staged_s42
90	BCE (no compensation) & 27.97 & +16.18 \\ % exp_id: eval_bce_v3_s42
91	BCE + Gumbel + Penalty (no KL) & 38.02 & +26.23 \\ % exp_id: bce_gumbel_lagrangian_isolation
92	\bottomrule
93	\end{tabular}
94	\end{table}
95	
96	\paragraph{Gumbel vs.\ STE.}
97	Replacing Gumbel-Sigmoid with STE~\cite{bengio2013ste} degrades PPL from 11.79 to 15.77 (+3.98), accounting for 34.5\% of the improvement over vanilla TEAL. % exp_id: ste_baseline_s42
98	
99	\paragraph{Divergence Direction.}
100	Forward KL (mode-covering) outperforms JSD (+6.4\%) and reverse KL (+8.6\%), consistent with the SNR analysis in \S\ref{sec:method:gradient}: complete teacher supervision enables better global allocation learning. % exp_id: jsd_ablation_s42, reverse_kl_ablation_s42
101	
102	\paragraph{SPON Contribution.}
103	Adding SPON~\cite{xu2026spon} bias correction reduces PPL from 12.08 to 11.79 (2.4\% relative); see \S\ref{sec:spon} for decomposition.\footnote{SPON analysis uses \texttt{evaluate.py}; main results use the unified benchmark.} % exp_id: spon_2048_s42, mvp_kl_norm_v2_s42
104	
105	\paragraph{Loss Function Isolation.}
106	BCE with identical Gumbel-Sigmoid and penalty yields PPL 38.02, worse than vanilla BCE (27.97): the penalty interferes with per-neuron optimization without global coordination. % exp_id: bce_gumbel_lagrangian_isolation
107	The loss effect ($\Delta$PPL=26.23) is $6.6\times$ the relaxation effect ($\Delta$PPL=3.98).
108	
109	\paragraph{BCE + Compensation.}
110	Compensation improves BCE from 27.97 to 25.44 (9.0\%), still $2.16\times$ worse than KL. % exp_id: bce_comp_staged_s42
111	
112	\paragraph{Hyperparameter Robustness.}
113	Appendix~\ref{app:db_sensitivity} confirms robustness to predictor capacity ($d_b$, $<$3\%), temperature ($<$1.8\%), and training steps (saturated by 800). % exp_id: db_sensitivity_sweep, tau_schedule_sweep, training_steps_sweep
114	
115	
116	\subsection{Sparsity Scaling and Regime Analysis}
117	\label{sec:scaling}
118	
119	Table~\ref{tab:scaling} and Figure~\ref{fig:sparsity_sweep} show PPL as a function of sparsity for KL-predictor-TEAL and vanilla TEAL.
120	
121	\begin{figure}[t]
122	\centering
123	\includegraphics[width=\columnwidth]{fig2_sparsity_sweep.pdf}
124	\caption{Perplexity scaling with sparsity. The KL predictor's advantage grows disproportionately as more neurons are pruned.}
125	\label{fig:sparsity_sweep}
126	\end{figure}
127	
128	\begin{table}[t]
129	\centering
130	\caption{PPL scaling with sparsity (WikiText-2). KL advantage grows disproportionately with sparsity.}
131	\label{tab:scaling}
132	\small
133	\begin{tabular}{lccc}
134	\toprule
135	Sparsity & KL (Ours) & TEAL vanilla & Relative advantage \\
136	\midrule
137	30\% & \textbf{8.98} & 10.97 & 18\% \\ % exp_id: kl_30_global_teal
138	50\% & \textbf{11.79} & 23.31 & 49\% \\ % exp_id: bench_kl50_global
139	70\% & \textbf{17.91} & 100.11 & 82\% \\ % exp_id: kl_70_global_teal
140	\bottomrule
141	\end{tabular}
142	\end{table}
143	
144	The KL advantage grows from 18\% at 30\% to 82\% at 70\%, where TEAL collapses (PPL 100.11) while the learned predictor maintains coherent allocation.
145	In absolute terms, KL/Dense degradation is $1.47\times$ at 30\%, $1.93\times$ at 50\%, and $2.93\times$ at 70\%, compared to TEAL/Dense ratios of $1.79\times$, $3.81\times$, and $16.4\times$ respectively.
146	
147	\paragraph{Three Regimes: Allocation vs.\ Capacity.}
148	Table~\ref{tab:phase} presents global vs.\ uniform allocation at three sparsity levels, revealing qualitative regime shifts.
149	
150	\begin{table}[t]
151	\centering
152	\caption{Allocation analysis: global (TEAL) vs.\ uniform per-layer allocation across sparsity levels. \textbf{Bold}: best per column within each sparsity group (compensation-free). Each row uses a predictor trained at the respective sparsity target.}
153	\label{tab:phase}
154	\resizebox{\columnwidth}{!}{
155	\begin{tabular}{llccccc}
156	\toprule
157	Sparsity & Allocation & PPL$\downarrow$ & ARC-c & WG & MMLU & GSM8K \\
158	\midrule
159	0\% & Dense & 6.12 & 58.28 & 78.06 & 65.27 & 48.75 \\
160	\midrule
161	\multirow{3}{*}{30\%}
162	& TEAL vanilla & 10.97 & \textbf{42.32} & 66.06 & 38.61 & 7.88 \\ % exp_id: bench_teal30
163	& KL global & 8.98 & 39.68 & \textbf{70.17} & 25.27 & \textbf{8.79} \\ % exp_id: lm_eval_kl_30pct_s42
164	& KL uniform & \textbf{8.82} & 40.78 & 68.59 & \textbf{40.61} & 7.35 \\ % exp_id: bench_kl30_uniform
165	\midrule
166	\multirow{2}{*}{40\%}
167	& KL global & 10.12 & 40.96 & 65.35 & \textbf{38.06} & \textbf{5.00} \\ % exp_id: bench_kl40_global
168	& KL uniform & \textbf{8.36} & \textbf{41.81} & \textbf{67.17} & 30.68 & 3.94 \\ % exp_id: d030_kl40_uniform
169	\midrule
170	\multirow{3}{*}{50\%}
171	& TEAL vanilla & 23.31 & 28.41 & 53.04 & \textbf{28.32} & 1.97 \\ % exp_id: bench_teal50
172	& KL global & \textbf{11.79} & \textbf{32.85} & \textbf{63.46} & 27.89 & 1.29 \\ % exp_id: bench_kl50_global
173	& KL uniform & 11.96 & 32.76 & 62.90 & 27.77 & \textbf{2.12} \\ % exp_id: d030_kl50_uniform
174	\bottomrule
175	\end{tabular}}
176	\end{table}
177	
178	The allocation preference is \emph{non-monotonic}, revealing three regimes:
179	
180	\noindent\textbf{Budget-surplus ($\leq$30\%).}
181	Uniform allocation recovers MMLU from 25.27\% to 40.61\% (+15.3pp); global top-$k$ starves late layers (L31: 28.4\%, L30: 36.6\% retention) whose long-tailed activation distributions (std/mean$=$1.89 at L31) siphon budget from logit-forming layers. % exp_id: bench_kl30_uniform, lm_eval_kl_30pct_s42
182	
183	\noindent\textbf{Budget-constrained ($\sim$40\%).}
184	The preference reverses: global achieves MMLU 38.06\% vs.\ uniform's 30.68\% (+7.4pp). % exp_id: bench_kl40_global, d030_kl40_uniform
185	PPL remains low (8.36) but downstream accuracy degrades, confirming PPL is a poor proxy for reasoning.
186	
187	\noindent\textbf{Capacity-limited ($\geq$50\%).}
188	Global/uniform gap vanishes (MMLU 27.89\% vs.\ 27.77\%, both $\approx$ random). % exp_id: bench_kl50_global, d030_kl50_uniform
189	Late-layer starvation persists across levels (L24--31 mean retention: 50.1\% at 30\%, 34.2\% at 50\%, 22.6\% at 70\%; Figure~\ref{fig:retention}); this boundary is consistent on both 7--8B models (\S\ref{sec:cross_arch}).
190	
191	
192	\subsection{SPON Orthogonality Analysis}
193	\label{sec:spon}
194	
195	At 50\% sparsity, the predictor's hidden-state perturbation (L2=482.65) and SPON's additive correction (L2=76.2, cosine similarity 0.196) are near-orthogonal; SPON yields only 2.4\% PPL improvement (12.08$\to$11.79), confirming the KL predictor already captures most recoverable signal. % exp_id: spon_decomposition, spon_2048_s42, mvp_kl_norm_v2_s42
196	
197	\paragraph{Cross-Architecture Validation.}
198	\label{sec:cross_arch}
199	Table~\ref{tab:cross_arch} evaluates on Mistral-7B-v0.3~\cite{jiang2023mistral} (GQA + sliding window, dense PPL 5.52).
200	
201	\begin{table}[t]
202	\centering
203	\caption{Cross-architecture comparison (WikiText-2 PPL$\downarrow$). Adv = TEAL / KL.}
204	\label{tab:cross_arch}
205	\small
206	\begin{tabular}{l@{\hspace{4pt}}cc@{\hspace{3pt}}c@{\hspace{6pt}}|@{\hspace{6pt}}cc@{\hspace{3pt}}c}
207	\toprule
208	 & \multicolumn{3}{c}{Mistral-7B} & \multicolumn{3}{c}{LLaMA-8B} \\
209	 & KL & TEAL & Adv & KL & TEAL & Adv \\
210	\midrule
211	30\% & \textbf{6.77} & 8.38 & 1.24$\times$ & \textbf{8.98} & 10.97 & 1.22$\times$ \\ % exp_id: kl_30_mistral, teal_30_mistral
212	50\% & \textbf{8.65} & 18.31 & 2.12$\times$ & \textbf{11.79} & 23.31 & 1.98$\times$ \\ % exp_id: kl_50_mistral, teal_50_mistral
213	70\% & \textbf{13.33} & 61.72 & 4.63$\times$ & \textbf{17.91} & 100.11 & 5.59$\times$ \\ % exp_id: kl_70_mistral, teal_70_mistral
214	\bottomrule
215	\end{tabular}
216	\end{table}
217	
218	The KL advantage ratio is consistent across architectures (within 7\% at $\leq$50\% sparsity), with larger variance at 70\% (4.63$\times$ vs.\ 5.59$\times$) due to differential baseline collapse.
219	Mistral's TEAL baseline is uniformly stronger (its gate distribution favors magnitude pruning), yet consistent KL-over-TEAL ratios indicate the advantage stems from modeling inter-neuron dependencies, a structural property of SwiGLU at the 7--8B scale tested.
220	
221	
222	\paragraph{Inference Efficiency.}
223	The pipeline adds 6.4\% overhead to dense inference while eliminating the compensation network ($-$2.7\% latency, $-$67.2M params); see Appendix~\ref{app:latency}.
224	
225	\paragraph{Training Stability.}
226	Three-seed evaluation (50\% uniform): PPL $11.92 \pm 0.07$ (CV$<$1\%); see Appendix~\ref{app:stability}.
227	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "858fb799-ef9a-44ba-b998-4153d3b67240",
  "isSidechain": false,
  "promptId": "e22b3aa5-f147-4b55-a02c-533b2c761d41",
  "type": "user",
  "uuid": "dad5245d-cad7-48f1-b41b-756e725fe329",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/experiments.tex",
      "content": "\\section{Experiments}\n\\label{sec:experiments}\n\n\\subsection{Experimental Setup}\n\n\\paragraph{Model and Predictor.}\nWe evaluate on LLaMA-3.1-8B~\\cite{grattafiori2024llama3}, which uses SwiGLU FFN blocks~\\cite{shazeer2020glu} with $d_{\\text{model}}=4096$ and $d_{\\text{ff}}=14336$ across 32 layers.\nThe sparsity predictor is a two-layer MLP with 2.37M parameters per layer (75.9M total), implemented as Linear($4096 \\to 128$) + GELU + Linear($128 \\to 14336$), trained to produce per-neuron importance scores that minimize output-distribution divergence under sparsity.\n\n\\paragraph{Training.}\nAll predictors are trained for 1000 steps on WikiText-103 with sequence length 2048 and batch size 4, using AdamW~\\cite{loshchilov2019adamw} with learning rate $1 \\times 10^{-3}$ and cosine decay.\nThe KL predictor uses Gumbel-Sigmoid relaxation~\\cite{jang2017gumbel} with temperature $\\tau=1.0$ annealed to $0.1$ over training.\n\n\\paragraph{Evaluation.}\nWe report perplexity on WikiText-2~\\cite{merity2017pointer} (seq\\_len=2048) and downstream accuracy on ARC-Challenge (25-shot), WinoGrande (5-shot), MMLU (5-shot), and GSM8K (8-shot).\n\n\\paragraph{Inference Protocol.}\nAt inference, the predictor produces per-neuron scores that are passed to TEAL's global top-$k$ allocation mechanism~\\cite{liu2025teal}, which distributes the sparsity budget across layers non-uniformly.\nWe term this \\textit{predictor-TEAL}: the predictor replaces TEAL's magnitude-based scoring while retaining its allocation strategy.\n\n\\paragraph{Baselines.}\nWe compare against: (1) \\textbf{Vanilla TEAL}~\\cite{liu2025teal}, which uses activation magnitudes directly; (2) \\textbf{BCE predictor}, trained with per-neuron binary cross-entropy loss for 1000 and 2700 steps; (3) \\textbf{Uniform allocation}, which distributes the sparsity budget equally across layers; and (4) \\textbf{WINA}~\\cite{liu2025teal}, an importance-weighted variant.\n\n\n\\subsection{Main Results}\n\nTable~\\ref{tab:main} presents the primary comparison across sparsity levels.\nAt 30\\% sparsity, KL distillation with global TEAL allocation achieves PPL 8.98, reducing TEAL's degradation from dense (10.97 $\\to$ 8.98, an 18\\% improvement). % exp_id: kl_30_global_teal\nUniform allocation at 30\\% recovers MMLU to 40.61\\% (+15.3pp over KL-global's 25.27\\%): global top-$k$ starves late layers (L31 retention 28.4\\%) while uniform guarantees capacity in logit-forming layers (\\S\\ref{sec:scaling}). % exp_id: bench_kl30_uniform\n\nAt 50\\% sparsity, KL distillation over vanilla TEAL widens the PPL advantage: 11.79 vs.\\ 23.31, a 49\\% reduction. % exp_id: bench_kl50_global, bench_teal50\nThe predictor also generalizes to held-out data (C4 validation: 52.5\\% advantage over TEAL; see Appendix~\\ref{app:ood}).\nHowever, all methods exhibit downstream collapse on MMLU (27.89\\% vs.\\ 27.77\\% for global vs.\\ uniform, both $\\approx$ random) and GSM8K ($<$2.2\\%), indicating a capacity-limited regime where no allocation strategy can recover. % exp_id: bench_kl50_global, d030_kl50_uniform\n\n\\begin{table}[t]\n\\centering\n\\caption{Main results on LLaMA-3.1-8B. PPL$\\downarrow$ on WikiText-2; accuracy$\\uparrow$ on downstream tasks. \\textbf{Bold}: best among compensation-free methods per sparsity level. BCE uses a different inference protocol (hard mask + compensation network). Multi-seed variance (3 seeds, 50\\% uniform): PPL std=0.07; see Appendix~\\ref{app:stability}.}\n\\label{tab:main}\n\\resizebox{\\columnwidth}{!}{\n\\begin{tabular}{llccccc}\n\\toprule\nSparsity & Method & PPL$\\downarrow$ & ARC-c & WG & MMLU & GSM8K \\\\\n\\midrule\n0\\% & Dense & 6.12 & 58.28 & 78.06 & 65.27 & 48.75 \\\\\n\\midrule\n\\multirow{3}{*}{30\\%}\n& TEAL vanilla & 10.97 & \\textbf{42.32} & 66.06 & 38.61 & 7.88 \\\\ % exp_id: bench_teal30\n& KL global (Ours) & 8.98 & 39.68 & \\textbf{70.17} & 25.27 & \\textbf{8.79} \\\\ % exp_id: lm_eval_kl_30pct_s42\n& KL uniform & \\textbf{8.82} & 40.78 & 68.59 & \\textbf{40.61} & 7.35 \\\\ % exp_id: bench_kl30_uniform\n\\midrule\n\\multirow{4}{*}{50\\%}\n& TEAL vanilla & 23.31 & 28.41 & 53.04 & \\textbf{28.32} & 1.97 \\\\ % exp_id: bench_teal50\n& KL global (Ours) & \\textbf{11.79} & \\textbf{32.85} & \\textbf{63.46} & 27.89 & 1.29 \\\\ % exp_id: bench_kl50_global\n& KL uniform & 11.96 & 32.76 & 62.90 & 27.77 & \\textbf{2.12} \\\\ % exp_id: d030_kl50_uniform\n& BCE (2700 steps)$^\\ast$ & 27.97 & 23.98 & 50.59 & 30.02 & 4.85 \\\\ % exp_id: eval_bce_v3_s42\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\n\n\\subsection{Iso-Compute Analysis}\n\\label{sec:isocompute}\n\nTo test whether BCE simply requires more compute, we train it for 2700 steps (2.71$\\times$ the KL budget).\nThe BCE predictor achieves PPL 27.97, still 2.37$\\times$ worse than KL at 1000 steps (PPL 11.79). % exp_id: bce_isocompute_s42\nThe failure is structural: BCE achieves +13pp oracle F1 (0.613 vs.\\ 0.540) yet 91\\% worse PPL (22.51 vs.\\ 11.79), and KL's near-random precision (0.51) confirms it learns a different mask optimized for distributional fidelity rather than magnitude matching. % exp_id: f1_oracle_analysis, bce_isocompute_s42\n\n\n\\subsection{Ablation Studies}\n\nTable~\\ref{tab:ablation} isolates the contribution of each design choice at 50\\% sparsity.\n\n\\begin{table}[t]\n\\centering\n\\caption{Ablation at 50\\% sparsity on LLaMA-3.1-8B (WikiText-2 PPL$\\downarrow$, unified benchmark protocol).}\n\\label{tab:ablation}\n\\small\n\\begin{tabular}{lcc}\n\\toprule\nConfiguration & PPL$\\downarrow$ & $\\Delta$ from Ours \\\\\n\\midrule\n\\multicolumn{3}{l}{\\textit{KL-based variants}} \\\\\nForward KL + Gumbel (Ours) & \\textbf{11.79} & --- \\\\ % exp_id: bench_kl50_global\nJSD (symmetric) + Gumbel & 12.54 & +0.75 \\\\ % exp_id: jsd_ablation_s42\nReverse KL + Gumbel & 12.80 & +1.01 \\\\ % exp_id: reverse_kl_ablation_s42\nForward KL + STE & 15.77 & +3.98 \\\\ % exp_id: ste_baseline_s42\n\\midrule\n\\multicolumn{3}{l}{\\textit{BCE-based variants}} \\\\\nBCE + Compensation (hard mask) & 25.44 & +13.65 \\\\ % exp_id: bce_comp_staged_s42\nBCE (no compensation) & 27.97 & +16.18 \\\\ % exp_id: eval_bce_v3_s42\nBCE + Gumbel + Penalty (no KL) & 38.02 & +26.23 \\\\ % exp_id: bce_gumbel_lagrangian_isolation\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Gumbel vs.\\ STE.}\nReplacing Gumbel-Sigmoid with STE~\\cite{bengio2013ste} degrades PPL from 11.79 to 15.77 (+3.98), accounting for 34.5\\% of the improvement over vanilla TEAL. % exp_id: ste_baseline_s42\n\n\\paragraph{Divergence Direction.}\nForward KL (mode-covering) outperforms JSD (+6.4\\%) and reverse KL (+8.6\\%), consistent with the SNR analysis in \\S\\ref{sec:method:gradient}: complete teacher supervision enables better global allocation learning. % exp_id: jsd_ablation_s42, reverse_kl_ablation_s42\n\n\\paragraph{SPON Contribution.}\nAdding SPON~\\cite{xu2026spon} bias correction reduces PPL from 12.08 to 11.79 (2.4\\% relative); see \\S\\ref{sec:spon} for decomposition.\\footnote{SPON analysis uses \\texttt{evaluate.py}; main results use the unified benchmark.} % exp_id: spon_2048_s42, mvp_kl_norm_v2_s42\n\n\\paragraph{Loss Function Isolation.}\nBCE with identical Gumbel-Sigmoid and penalty yields PPL 38.02, worse than vanilla BCE (27.97): the penalty interferes with per-neuron optimization without global coordination. % exp_id: bce_gumbel_lagrangian_isolation\nThe loss effect ($\\Delta$PPL=26.23) is $6.6\\times$ the relaxation effect ($\\Delta$PPL=3.98).\n\n\\paragraph{BCE + Compensation.}\nCompensation improves BCE from 27.97 to 25.44 (9.0\\%), still $2.16\\times$ worse than KL. % exp_id: bce_comp_staged_s42\n\n\\paragraph{Hyperparameter Robustness.}\nAppendix~\\ref{app:db_sensitivity} confirms robustness to predictor capacity ($d_b$, $<$3\\%), temperature ($<$1.8\\%), and training steps (saturated by 800). % exp_id: db_sensitivity_sweep, tau_schedule_sweep, training_steps_sweep\n\n\n\\subsection{Sparsity Scaling and Regime Analysis}\n\\label{sec:scaling}\n\nTable~\\ref{tab:scaling} and Figure~\\ref{fig:sparsity_sweep} show PPL as a function of sparsity for KL-predictor-TEAL and vanilla TEAL.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{fig2_sparsity_sweep.pdf}\n\\caption{Perplexity scaling with sparsity. The KL predictor's advantage grows disproportionately as more neurons are pruned.}\n\\label{fig:sparsity_sweep}\n\\end{figure}\n\n\\begin{table}[t]\n\\centering\n\\caption{PPL scaling with sparsity (WikiText-2). KL advantage grows disproportionately with sparsity.}\n\\label{tab:scaling}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\nSparsity & KL (Ours) & TEAL vanilla & Relative advantage \\\\\n\\midrule\n30\\% & \\textbf{8.98} & 10.97 & 18\\% \\\\ % exp_id: kl_30_global_teal\n50\\% & \\textbf{11.79} & 23.31 & 49\\% \\\\ % exp_id: bench_kl50_global\n70\\% & \\textbf{17.91} & 100.11 & 82\\% \\\\ % exp_id: kl_70_global_teal\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe KL advantage grows from 18\\% at 30\\% to 82\\% at 70\\%, where TEAL collapses (PPL 100.11) while the learned predictor maintains coherent allocation.\nIn absolute terms, KL/Dense degradation is $1.47\\times$ at 30\\%, $1.93\\times$ at 50\\%, and $2.93\\times$ at 70\\%, compared to TEAL/Dense ratios of $1.79\\times$, $3.81\\times$, and $16.4\\times$ respectively.\n\n\\paragraph{Three Regimes: Allocation vs.\\ Capacity.}\nTable~\\ref{tab:phase} presents global vs.\\ uniform allocation at three sparsity levels, revealing qualitative regime shifts.\n\n\\begin{table}[t]\n\\centering\n\\caption{Allocation analysis: global (TEAL) vs.\\ uniform per-layer allocation across sparsity levels. \\textbf{Bold}: best per column within each sparsity group (compensation-free). Each row uses a predictor trained at the respective sparsity target.}\n\\label{tab:phase}\n\\resizebox{\\columnwidth}{!}{\n\\begin{tabular}{llccccc}\n\\toprule\nSparsity & Allocation & PPL$\\downarrow$ & ARC-c & WG & MMLU & GSM8K \\\\\n\\midrule\n0\\% & Dense & 6.12 & 58.28 & 78.06 & 65.27 & 48.75 \\\\\n\\midrule\n\\multirow{3}{*}{30\\%}\n& TEAL vanilla & 10.97 & \\textbf{42.32} & 66.06 & 38.61 & 7.88 \\\\ % exp_id: bench_teal30\n& KL global & 8.98 & 39.68 & \\textbf{70.17} & 25.27 & \\textbf{8.79} \\\\ % exp_id: lm_eval_kl_30pct_s42\n& KL uniform & \\textbf{8.82} & 40.78 & 68.59 & \\textbf{40.61} & 7.35 \\\\ % exp_id: bench_kl30_uniform\n\\midrule\n\\multirow{2}{*}{40\\%}\n& KL global & 10.12 & 40.96 & 65.35 & \\textbf{38.06} & \\textbf{5.00} \\\\ % exp_id: bench_kl40_global\n& KL uniform & \\textbf{8.36} & \\textbf{41.81} & \\textbf{67.17} & 30.68 & 3.94 \\\\ % exp_id: d030_kl40_uniform\n\\midrule\n\\multirow{3}{*}{50\\%}\n& TEAL vanilla & 23.31 & 28.41 & 53.04 & \\textbf{28.32} & 1.97 \\\\ % exp_id: bench_teal50\n& KL global & \\textbf{11.79} & \\textbf{32.85} & \\textbf{63.46} & 27.89 & 1.29 \\\\ % exp_id: bench_kl50_global\n& KL uniform & 11.96 & 32.76 & 62.90 & 27.77 & \\textbf{2.12} \\\\ % exp_id: d030_kl50_uniform\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\nThe allocation preference is \\emph{non-monotonic}, revealing three regimes:\n\n\\noindent\\textbf{Budget-surplus ($\\leq$30\\%).}\nUniform allocation recovers MMLU from 25.27\\% to 40.61\\% (+15.3pp); global top-$k$ starves late layers (L31: 28.4\\%, L30: 36.6\\% retention) whose long-tailed activation distributions (std/mean$=$1.89 at L31) siphon budget from logit-forming layers. % exp_id: bench_kl30_uniform, lm_eval_kl_30pct_s42\n\n\\noindent\\textbf{Budget-constrained ($\\sim$40\\%).}\nThe preference reverses: global achieves MMLU 38.06\\% vs.\\ uniform's 30.68\\% (+7.4pp). % exp_id: bench_kl40_global, d030_kl40_uniform\nPPL remains low (8.36) but downstream accuracy degrades, confirming PPL is a poor proxy for reasoning.\n\n\\noindent\\textbf{Capacity-limited ($\\geq$50\\%).}\nGlobal/uniform gap vanishes (MMLU 27.89\\% vs.\\ 27.77\\%, both $\\approx$ random). % exp_id: bench_kl50_global, d030_kl50_uniform\nLate-layer starvation persists across levels (L24--31 mean retention: 50.1\\% at 30\\%, 34.2\\% at 50\\%, 22.6\\% at 70\\%; Figure~\\ref{fig:retention}); this boundary is consistent on both 7--8B models (\\S\\ref{sec:cross_arch}).\n\n\n\\subsection{SPON Orthogonality Analysis}\n\\label{sec:spon}\n\nAt 50\\% sparsity, the predictor's hidden-state perturbation (L2=482.65) and SPON's additive correction (L2=76.2, cosine similarity 0.196) are near-orthogonal; SPON yields only 2.4\\% PPL improvement (12.08$\\to$11.79), confirming the KL predictor already captures most recoverable signal. % exp_id: spon_decomposition, spon_2048_s42, mvp_kl_norm_v2_s42\n\n\\paragraph{Cross-Architecture Validation.}\n\\label{sec:cross_arch}\nTable~\\ref{tab:cross_arch} evaluates on Mistral-7B-v0.3~\\cite{jiang2023mistral} (GQA + sliding window, dense PPL 5.52).\n\n\\begin{table}[t]\n\\centering\n\\caption{Cross-architecture comparison (WikiText-2 PPL$\\downarrow$). Adv = TEAL / KL.}\n\\label{tab:cross_arch}\n\\small\n\\begin{tabular}{l@{\\hspace{4pt}}cc@{\\hspace{3pt}}c@{\\hspace{6pt}}|@{\\hspace{6pt}}cc@{\\hspace{3pt}}c}\n\\toprule\n & \\multicolumn{3}{c}{Mistral-7B} & \\multicolumn{3}{c}{LLaMA-8B} \\\\\n & KL & TEAL & Adv & KL & TEAL & Adv \\\\\n\\midrule\n30\\% & \\textbf{6.77} & 8.38 & 1.24$\\times$ & \\textbf{8.98} & 10.97 & 1.22$\\times$ \\\\ % exp_id: kl_30_mistral, teal_30_mistral\n50\\% & \\textbf{8.65} & 18.31 & 2.12$\\times$ & \\textbf{11.79} & 23.31 & 1.98$\\times$ \\\\ % exp_id: kl_50_mistral, teal_50_mistral\n70\\% & \\textbf{13.33} & 61.72 & 4.63$\\times$ & \\textbf{17.91} & 100.11 & 5.59$\\times$ \\\\ % exp_id: kl_70_mistral, teal_70_mistral\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe KL advantage ratio is consistent across architectures (within 7\\% at $\\leq$50\\% sparsity), with larger variance at 70\\% (4.63$\\times$ vs.\\ 5.59$\\times$) due to differential baseline collapse.\nMistral's TEAL baseline is uniformly stronger (its gate distribution favors magnitude pruning), yet consistent KL-over-TEAL ratios indicate the advantage stems from modeling inter-neuron dependencies, a structural property of SwiGLU at the 7--8B scale tested.\n\n\n\\paragraph{Inference Efficiency.}\nThe pipeline adds 6.4\\% overhead to dense inference while eliminating the compensation network ($-$2.7\\% latency, $-$67.2M params); see Appendix~\\ref{app:latency}.\n\n\\paragraph{Training Stability.}\nThree-seed evaluation (50\\% uniform): PPL $11.92 \\pm 0.07$ (CV$<$1\\%); see Appendix~\\ref{app:stability}.\n",
      "numLines": 227,
      "startLine": 1,
      "totalLines": 227
    }
  },
  "sourceToolAssistantUUID": "858fb799-ef9a-44ba-b998-4153d3b67240",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/review_reviewer_1_772f066c",
  "sessionId": "fd7408d6-e7e0-4bb4-8dde-4202758b928d",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-17T08:11:50.112Z_

<details open><summary>🔧 Tool call — Read · `toolu_014V7LqrnK4Lu4vC8cFTFCPi`</summary>

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
  "parentUuid": "dad5245d-cad7-48f1-b41b-756e725fe329",
  "isSidechain": false,
  "requestId": "req_011Cb7oZWy4fYiJASzD2k8VN",
  "type": "assistant",
  "uuid": "c1590ac2-b6c3-42a4-8785-2434363a3469",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/review_reviewer_1_772f066c",
  "sessionId": "fd7408d6-e7e0-4bb4-8dde-4202758b928d",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014pujs8tdAWYSgd6nPAVexn",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 365,
      "cache_creation_input_tokens": 855,
      "cache_read_input_tokens": 31828,
      "output_tokens": 722,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 855,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 365,
          "output_tokens": 722,
          "cache_read_input_tokens": 31828,
          "cache_creation_input_tokens": 855,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 855
          },
          "type": "message"
        }
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

_source line 38 · 2026-05-17T08:11:50.117Z_

<details><summary>↩ Tool result · `toolu_014V7LqrnK4Lu4vC8cFTFCPi`</summary>

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
11	FastForward~\cite{gautam2026fastforward} adds a 67.2M-parameter compensation network using BCE for mask prediction, adding inference latency.
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
28	\paragraph{Weight Pruning and Routing.}
29	Wanda~\cite{sun2024wanda} and SparseGPT~\cite{frantar2023sparsegpt} produce static weight masks via magnitude or reconstruction criteria; Switch Transformers~\cite{fedus2022switch} achieve conditional computation through learned expert routing.
30	Our method differs in generating dynamic per-token activation masks on unmodified dense models.
31	Sequence-level distillation~\cite{kim2016sequencekd} and DistilBERT~\cite{sanh2019distilbert} apply distributional matching to train compact students; we apply the same KL principle to train a sparsity predictor rather than a smaller model.
32	Our Gumbel-Sigmoid sampling builds on the Concrete distribution~\cite{maddison2017concrete} and $L_0$ regularization~\cite{louizos2018l0} for differentiable discrete optimization, adapted here to per-token activation prediction with a coupled objective.
33	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c1590ac2-b6c3-42a4-8785-2434363a3469",
  "isSidechain": false,
  "promptId": "e22b3aa5-f147-4b55-a02c-533b2c761d41",
  "type": "user",
  "uuid": "944d6c18-801e-4819-abda-538bc1fab160",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/related_work.tex",
      "content": "\\section{Related Work}\n\n\\paragraph{Training-Free Activation Sparsity.}\nTEAL~\\cite{liu2025teal} applies global top-$k$ selection by activation magnitude, achieving 40--50\\% sparsity with no training cost.\nCATS~\\cite{lee2024cats} adapts per-layer thresholds for SiLU/SwiGLU activations; R-Sparse~\\cite{zhang2025rsparse} predicts sparsity from rank-aware SVD projections; DIP~\\cite{federici2025dip} combines dynamic input pruning with cache-aware masking.\nAll training-free methods determine masks from fixed statistics or input-independent criteria, while our predictor generates \\emph{input-dependent} masks trained to minimize output-distribution divergence.\n\n\\paragraph{Predictor-Based Contextual Sparsity.}\nDejaVu~\\cite{liu2023dejavu} introduced learned sparsity predictors trained via BCE to classify each neuron independently.\nShadowLLM~\\cite{akhauri2024shadowllm} uses attention-based routing with MSE supervision but retains per-neuron decomposition.\nFastForward~\\cite{gautam2026fastforward} adds a 67.2M-parameter compensation network using BCE for mask prediction, adding inference latency.\nPowerInfer~\\cite{song2024powerinfer} exploits power-law activation frequencies for GPU--CPU scheduling.\nMaskLLM~\\cite{fang2024maskllm} also employs learnable masks with Gumbel relaxation and frozen weights, but targets N:M semi-structured \\emph{weight} sparsity (2:4 patterns) via Gumbel-Softmax, producing fixed masks independent of input tokens.\nIn contrast, our method learns \\emph{activation} masks that are contextual (per-token), unstructured (budget-constrained global top-$k$), and trained with Gumbel-Sigmoid to minimize output-distribution divergence.\nAll prior predictor-based methods use decomposed (BCE) or intermediate (MSE) objectives where each neuron's gradient is independent of other mask states.\nOur \\emph{coupled} KL objective propagates gradients through all downstream layers, optimizing for global allocation quality without compensation.\n\n\\paragraph{Static Bias Correction.}\nSPON~\\cite{xu2026spon} learns input-independent bias vectors via closed-form KL minimization per layer, absorbed into weights at deployment.\nOur method is fundamentally different: a per-token contextual predictor trained end-to-end across all layers, producing input-dependent masks.\nSPON solves a static per-layer problem; we solve a global dynamic prediction problem. The two are near-orthogonal (cosine similarity 0.196; \\S\\ref{sec:experiments}).\n\n\\paragraph{Activation Function Engineering.}\nReLU Strikes Back~\\cite{mirzadeh2024relu} replaces SiLU with ReLU for $>$90\\% natural sparsity; TurboSparse~\\cite{song2024turbosparse} and ProSparse~\\cite{song2025prosparse} engineer extreme sparsity through activation modifications; the Sparsing Law~\\cite{luo2024sparsinglaw} formalizes how activation density increases with training compute.\nMiniTron~\\cite{muralidharan2024minitron} combines structured pruning with distillation but modifies architecture permanently.\nAll require retraining or weight modification; our method is a plug-in predictor on \\emph{unmodified} SwiGLU models.\n\n\\paragraph{Weight Pruning and Routing.}\nWanda~\\cite{sun2024wanda} and SparseGPT~\\cite{frantar2023sparsegpt} produce static weight masks via magnitude or reconstruction criteria; Switch Transformers~\\cite{fedus2022switch} achieve conditional computation through learned expert routing.\nOur method differs in generating dynamic per-token activation masks on unmodified dense models.\nSequence-level distillation~\\cite{kim2016sequencekd} and DistilBERT~\\cite{sanh2019distilbert} apply distributional matching to train compact students; we apply the same KL principle to train a sparsity predictor rather than a smaller model.\nOur Gumbel-Sigmoid sampling builds on the Concrete distribution~\\cite{maddison2017concrete} and $L_0$ regularization~\\cite{louizos2018l0} for differentiable discrete optimization, adapted here to per-token activation prediction with a coupled objective.\n",
      "numLines": 33,
      "startLine": 1,
      "totalLines": 33
    }
  },
  "sourceToolAssistantUUID": "c1590ac2-b6c3-42a4-8785-2434363a3469",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/review_reviewer_1_772f066c",
  "sessionId": "fd7408d6-e7e0-4bb4-8dde-4202758b928d",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-17T08:11:51.087Z_

<details open><summary>🔧 Tool call — Read · `toolu_01RUoeVMNEX18M9ez9cPTLab`</summary>

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
  "parentUuid": "944d6c18-801e-4819-abda-538bc1fab160",
  "isSidechain": false,
  "requestId": "req_011Cb7oZWy4fYiJASzD2k8VN",
  "type": "assistant",
  "uuid": "ed4d4d0c-8dce-451e-9ddc-3affb7445a65",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/review_reviewer_1_772f066c",
  "sessionId": "fd7408d6-e7e0-4bb4-8dde-4202758b928d",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014pujs8tdAWYSgd6nPAVexn",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 365,
      "cache_creation_input_tokens": 855,
      "cache_read_input_tokens": 31828,
      "output_tokens": 722,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 855,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 365,
          "output_tokens": 722,
          "cache_read_input_tokens": 31828,
          "cache_creation_input_tokens": 855,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 855
          },
          "type": "message"
        }
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

_source line 40 · 2026-05-17T08:11:51.093Z_

<details><summary>↩ Tool result · `toolu_01RUoeVMNEX18M9ez9cPTLab`</summary>

```text
1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	Training sparsity predictors with KL divergence eliminates error compensation networks by coupling all neurons through the output distribution, resolving BCE's structural mismatch with global top-$k$ allocation.
5	The resulting predictor (75.9M params, $<$1\% of base) achieves PPL 11.79 at 50\% sparsity vs.\ 23.31 for TEAL, transfers across SwiGLU architectures at the 7--8B parameter scale (within 7\% ratio consistency), and reveals three sparsity regimes governing the quality-allocation tradeoff.
6	
7	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ed4d4d0c-8dce-451e-9ddc-3affb7445a65",
  "isSidechain": false,
  "promptId": "e22b3aa5-f147-4b55-a02c-533b2c761d41",
  "type": "user",
  "uuid": "d21f9051-e766-4756-9e45-19add60cdf5d",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/conclusion.tex",
      "content": "\\section{Conclusion}\n\\label{sec:conclusion}\n\nTraining sparsity predictors with KL divergence eliminates error compensation networks by coupling all neurons through the output distribution, resolving BCE's structural mismatch with global top-$k$ allocation.\nThe resulting predictor (75.9M params, $<$1\\% of base) achieves PPL 11.79 at 50\\% sparsity vs.\\ 23.31 for TEAL, transfers across SwiGLU architectures at the 7--8B parameter scale (within 7\\% ratio consistency), and reveals three sparsity regimes governing the quality-allocation tradeoff.\n\n",
      "numLines": 7,
      "startLine": 1,
      "totalLines": 7
    }
  },
  "sourceToolAssistantUUID": "ed4d4d0c-8dce-451e-9ddc-3affb7445a65",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/review_reviewer_1_772f066c",
  "sessionId": "fd7408d6-e7e0-4bb4-8dde-4202758b928d",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-17T08:11:51.594Z_

<details open><summary>🔧 Tool call — Read · `toolu_01WVxoELYaaqp7wwXYpd6eKN`</summary>

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
  "parentUuid": "d21f9051-e766-4756-9e45-19add60cdf5d",
  "isSidechain": false,
  "requestId": "req_011Cb7oZWy4fYiJASzD2k8VN",
  "type": "assistant",
  "uuid": "8bfcf836-589b-4acf-a85a-ca8581714ccb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/review_reviewer_1_772f066c",
  "sessionId": "fd7408d6-e7e0-4bb4-8dde-4202758b928d",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014pujs8tdAWYSgd6nPAVexn",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 365,
      "cache_creation_input_tokens": 855,
      "cache_read_input_tokens": 31828,
      "output_tokens": 722,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 855,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 365,
          "output_tokens": 722,
          "cache_read_input_tokens": 31828,
          "cache_creation_input_tokens": 855,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 855
          },
          "type": "message"
        }
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

_source line 42 · 2026-05-17T08:11:51.600Z_

<details><summary>↩ Tool result · `toolu_01WVxoELYaaqp7wwXYpd6eKN`</summary>

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
  "parentUuid": "8bfcf836-589b-4acf-a85a-ca8581714ccb",
  "isSidechain": false,
  "promptId": "e22b3aa5-f147-4b55-a02c-533b2c761d41",
  "type": "user",
  "uuid": "ea8cd2b9-435d-4b00-9241-b8b457b47041",
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
  "sourceToolAssistantUUID": "8bfcf836-589b-4acf-a85a-ca8581714ccb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/review_reviewer_1_772f066c",
  "sessionId": "fd7408d6-e7e0-4bb4-8dde-4202758b928d",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-17T08:11:51.698Z_

<details open><summary>🔧 Tool call — Read · `toolu_01YUiLPF4YdW3wHeA7AGheQc`</summary>

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
  "parentUuid": "ea8cd2b9-435d-4b00-9241-b8b457b47041",
  "isSidechain": false,
  "requestId": "req_011Cb7oZWy4fYiJASzD2k8VN",
  "type": "assistant",
  "uuid": "5c5daa71-c898-40a8-a8fb-d2fcf9cc2da3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/review_reviewer_1_772f066c",
  "sessionId": "fd7408d6-e7e0-4bb4-8dde-4202758b928d",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014pujs8tdAWYSgd6nPAVexn",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 365,
      "cache_creation_input_tokens": 855,
      "cache_read_input_tokens": 31828,
      "output_tokens": 722,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 855,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 365,
          "output_tokens": 722,
          "cache_read_input_tokens": 31828,
          "cache_creation_input_tokens": 855,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 855
          },
          "type": "message"
        }
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

_source line 44 · 2026-05-17T08:11:51.765Z_

```json
{
  "parentUuid": "082bd6f6-4d53-4bfa-b8c4-3c8175a39c1f",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "cafcd47e-5f8a-404d-9a5a-b02496b0b466",
  "timestamp": "2026-05-17T08:11:51.765Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/review_reviewer_1_772f066c",
  "sessionId": "fd7408d6-e7e0-4bb4-8dde-4202758b928d",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

---

### Runtime record

_source line 45_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[Round 1 审稿请求]: 你负责**方法严谨性 + 实验有效性**的审查。  ## Venue 信息 - **目标会议**: EMNLP 2026 (via ACL Rolling Review, May cycle) - **截止日期**: 2026-05-25 - **页数限制**: Long paper ≤8 页正文 + unlimited references + appendix…",
  "leafUuid": "cafcd47e-5f8a-404d-9a5a-b02496b0b466",
  "sessionId": "fd7408d6-e7e0-4bb4-8dde-4202758b928d"
}
```

---

### Runtime record

_source line 46_

```json
{
  "type": "ai-title",
  "aiTitle": "Review paper on sparse SwiGLU distillation methods",
  "sessionId": "fd7408d6-e7e0-4bb4-8dde-4202758b928d"
}
```

---

### Assistant

_source line 47 · 2026-05-17T08:11:55.186Z_

<details><summary>Logged reasoning block</summary>

```text
Let me continue reading the appendix since it was cut off, and also read the bib file to check references.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cafcd47e-5f8a-404d-9a5a-b02496b0b466",
  "isSidechain": false,
  "requestId": "req_011Cb7oa8HasSuhyXXrDpeHo",
  "type": "assistant",
  "uuid": "2ead60d6-5f26-4f6a-a9d5-b05d6a5e5249",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/review_reviewer_1_772f066c",
  "sessionId": "fd7408d6-e7e0-4bb4-8dde-4202758b928d",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015zeFD5cwd75GcQumnYCJ82",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 21592,
      "cache_read_input_tokens": 32683,
      "output_tokens": 252,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 21592,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 252,
          "cache_read_input_tokens": 32683,
          "cache_creation_input_tokens": 21592,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 21592
          },
          "type": "message"
        }
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

_source line 48 · 2026-05-17T08:11:55.700Z_

继续读取 appendix 剩余部分和 references.bib。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2ead60d6-5f26-4f6a-a9d5-b05d6a5e5249",
  "isSidechain": false,
  "requestId": "req_011Cb7oa8HasSuhyXXrDpeHo",
  "type": "assistant",
  "uuid": "c61f3d72-5aef-4c36-9817-f160116eecfa",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/review_reviewer_1_772f066c",
  "sessionId": "fd7408d6-e7e0-4bb4-8dde-4202758b928d",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015zeFD5cwd75GcQumnYCJ82",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 21592,
      "cache_read_input_tokens": 32683,
      "output_tokens": 252,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 21592,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 252,
          "cache_read_input_tokens": 32683,
          "cache_creation_input_tokens": 21592,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 21592
          },
          "type": "message"
        }
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

_source line 49 · 2026-05-17T08:11:57.577Z_

<details open><summary>🔧 Tool call — Read · `toolu_01QSUKXw2oFim9jh6Z8y8BQD`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/appendix.tex",
  "offset": 192
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c61f3d72-5aef-4c36-9817-f160116eecfa",
  "isSidechain": false,
  "requestId": "req_011Cb7oa8HasSuhyXXrDpeHo",
  "type": "assistant",
  "uuid": "88692039-0562-4d80-9a57-1b99755caad3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/review_reviewer_1_772f066c",
  "sessionId": "fd7408d6-e7e0-4bb4-8dde-4202758b928d",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015zeFD5cwd75GcQumnYCJ82",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 21592,
      "cache_read_input_tokens": 32683,
      "output_tokens": 252,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 21592,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 252,
          "cache_read_input_tokens": 32683,
          "cache_creation_input_tokens": 21592,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 21592
          },
          "type": "message"
        }
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

_source line 50 · 2026-05-17T08:11:57.970Z_

<details><summary>↩ Tool result · `toolu_018QnLVdrJuHaSkLpKWNufoG`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/references.bib
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "68b5ea53-a139-454e-9d82-ec14ca5e2767",
  "isSidechain": false,
  "promptId": "e22b3aa5-f147-4b55-a02c-533b2c761d41",
  "type": "user",
  "uuid": "6373d8d2-4bed-42e0-a145-8da92365b000",
  "toolUseResult": {
    "filenames": [
      "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/references.bib"
    ],
    "durationMs": 12,
    "numFiles": 1,
    "truncated": false
  },
  "sourceToolAssistantUUID": "68b5ea53-a139-454e-9d82-ec14ca5e2767",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/review_reviewer_1_772f066c",
  "sessionId": "fd7408d6-e7e0-4bb4-8dde-4202758b928d",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool result

_source line 51 · 2026-05-17T08:11:57.585Z_

<details><summary>↩ Tool result · `toolu_01QSUKXw2oFim9jh6Z8y8BQD`</summary>

```text
&lt;system-reminder>Warning: the file exists but is shorter than the provided offset (192). The file has 192 lines.&lt;/system-reminder>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "88692039-0562-4d80-9a57-1b99755caad3",
  "isSidechain": false,
  "promptId": "e22b3aa5-f147-4b55-a02c-533b2c761d41",
  "type": "user",
  "uuid": "b78d1ed2-7c59-4178-ab98-23da5f81feb1",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/appendix.tex",
      "content": "",
      "numLines": 1,
      "startLine": 192,
      "totalLines": 192
    }
  },
  "sourceToolAssistantUUID": "88692039-0562-4d80-9a57-1b99755caad3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/review_reviewer_1_772f066c",
  "sessionId": "fd7408d6-e7e0-4bb4-8dde-4202758b928d",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 52 · 2026-05-17T08:11:57.948Z_

<details open><summary>🔧 Tool call — Glob · `toolu_018QnLVdrJuHaSkLpKWNufoG`</summary>

```json
{
  "pattern": "**/*.bib",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b78d1ed2-7c59-4178-ab98-23da5f81feb1",
  "isSidechain": false,
  "requestId": "req_011Cb7oa8HasSuhyXXrDpeHo",
  "type": "assistant",
  "uuid": "68b5ea53-a139-454e-9d82-ec14ca5e2767",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/review_reviewer_1_772f066c",
  "sessionId": "fd7408d6-e7e0-4bb4-8dde-4202758b928d",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015zeFD5cwd75GcQumnYCJ82",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 21592,
      "cache_read_input_tokens": 32683,
      "output_tokens": 252,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 21592,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 252,
          "cache_read_input_tokens": 32683,
          "cache_creation_input_tokens": 21592,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 21592
          },
          "type": "message"
        }
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

_source line 53 · 2026-05-17T08:12:01.047Z_

<details open><summary>🔧 Tool call — Read · `toolu_015g5m2ARkkzyJoD7hcZwShf`</summary>

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
  "parentUuid": "6373d8d2-4bed-42e0-a145-8da92365b000",
  "isSidechain": false,
  "requestId": "req_011Cb7oaaxxBggnNCsEm4i7c",
  "type": "assistant",
  "uuid": "65f6f5cb-ffe8-4e93-8e4e-205019e93ba8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/review_reviewer_1_772f066c",
  "sessionId": "fd7408d6-e7e0-4bb4-8dde-4202758b928d",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Kkb5YcnqHtLJjSdLxm3ybY",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 378,
      "cache_read_input_tokens": 54275,
      "output_tokens": 89,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 378,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 89,
          "cache_read_input_tokens": 54275,
          "cache_creation_input_tokens": 378,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 378
          },
          "type": "message"
        }
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

_source line 54 · 2026-05-17T08:12:01.055Z_

<details><summary>↩ Tool result · `toolu_015g5m2ARkkzyJoD7hcZwShf`</summary>

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
143	% KL distillation and knowledge distillation
144	% =============================================================================
145	
146	@inproceedings{kim2016sequencekd,
147	  title = {Sequence-Level Knowledge Distillation},
148	  author = {Yoon Kim and Alexander M. Rush},
149	  year = {2016},
150	  booktitle = {Proceedings of the Conference on Empirical Methods in Natural Language Processing (EMNLP)},
151	  url = {https://arxiv.org/abs/1606.07947},
152	}
153	
154	@article{sanh2019distilbert,
155	  title = {DistilBERT, a distilled version of BERT: smaller, faster, cheaper and lighter},
156	  author = {Victor Sanh and Lysandre Debut and Julien Chaumond and Thomas Wolf},
157	  year = {2019},
158	  journal = {arXiv preprint arXiv:1910.01108},
159	  url = {https://arxiv.org/abs/1910.01108},
160	}
161	
162	% =============================================================================
163	% Weight pruning methods
164	% =============================================================================
165	
166	@inproceedings{sun2024wanda,
167	  title = {A Simple and Effective Pruning Approach for Large Language Models},
168	  author = {Mingjie Sun and Zhuang Liu and Anna Bair and J. Zico Kolter},
169	  year = {2024},
170	  booktitle = {Proceedings of the International Conference on Learning Representations (ICLR)},
171	  url = {https://arxiv.org/abs/2306.11695},
172	}
173	
174	@inproceedings{frantar2023sparsegpt,
175	  title = {SparseGPT: Massive Language Models Can Be Accurately Pruned in One-Shot},
176	  author = {Elias Frantar and Dan Alistarh},
177	  year = {2023},
178	  booktitle = {Proceedings of the International Conference on Machine Learning (ICML)},
179	  url = {https://arxiv.org/abs/2301.00774},
180	}
181	
182	% =============================================================================
183	% Conditional computation and MoE
184	% =============================================================================
185	
186	@article{fedus2022switch,
187	  title = {Switch Transformers: Scaling to Trillion Parameter Models with Simple and Efficient Sparsity},
188	  author = {William Fedus and Barret Zoph and Noam Shazeer},
189	  year = {2022},
190	  journal = {Journal of Machine Learning Research},
191	  volume = {23},
192	  number = {120},
193	  pages = {1--40},
194	  url = {https://arxiv.org/abs/2101.03961},
195	}
196	
197	% =============================================================================
198	% Relaxation methods (Gumbel/Concrete)
199	% =============================================================================
200	
201	@inproceedings{louizos2018l0,
202	  title = {Learning Sparse Neural Networks through $L_0$ Regularization},
203	  author = {Christos Louizos and Max Welling and Diederik P. Kingma},
204	  year = {2018},
205	  booktitle = {Proceedings of the International Conference on Learning Representations (ICLR)},
206	  url = {https://arxiv.org/abs/1712.01312},
207	}
208	
209	@inproceedings{maddison2017concrete,
210	  title = {The Concrete Distribution: A Continuous Relaxation of Discrete Random Variables},
211	  author = {Chris J. Maddison and Andriy Mnih and Yee Whye Teh},
212	  year = {2017},
213	  booktitle = {Proceedings of the International Conference on Learning Representations (ICLR)},
214	  url = {https://arxiv.org/abs/1611.00712},
215	}
216	
217	% =============================================================================
218	% Foundational references
219	% =============================================================================
220	
221	@article{grattafiori2024llama3,
222	  title = {The Llama 3 Herd of Models},
223	  author = {Aaron Grattafiori and Abhimanyu Dubey and Abhinav Jauhri and Abhinav Pandey and Abhishek Kadian and Ahmad Al-Dahle and Aieleen Lakber and Aimin Chen and Ait Mokhtar Salma and Ajay Menon},
224	  year = {2024},
225	  journal = {arXiv preprint arXiv:2407.21783},
226	  url = {https://arxiv.org/abs/2407.21783},
227	}
228	
229	@article{jiang2023mistral,
230	  title = {Mistral 7B},
231	  author = {Albert Q. Jiang and Alexandre Sablayrolles and Arthur Mensch and Chris Bamford and Devendra Singh Chaplot and Diego de las Casas and Florian Bressand and Gianna Lengyel and Guillaume Lample and Lucile Saulnier},
232	  year = {2023},
233	  journal = {arXiv preprint arXiv:2310.06825},
234	  url = {https://arxiv.org/abs/2310.06825},
235	}
236	
237	@inproceedings{jang2017gumbel,
238	  title = {Categorical Reparameterization with Gumbel-Softmax},
239	  author = {Eric Jang and Shixiang Gu and Ben Poole},
240	  year = {2017},
241	  booktitle = {Proceedings of the International Conference on Learning Representations (ICLR)},
242	  url = {https://arxiv.org/abs/1611.01144},
243	}
244	
245	@article{shazeer2020glu,
246	  title = {GLU Variants Improve Transformer},
247	  author = {Noam Shazeer},
248	  year = {2020},
249	  journal = {arXiv preprint arXiv:2002.05202},
250	  url = {https://arxiv.org/abs/2002.05202},
251	}
252	
253	@inproceedings{merity2017pointer,
254	  title = {Pointer Sentinel Mixture Models},
255	  author = {Stephen Merity and Caiming Xiong and James Bradbury and Richard Socher},
256	  year = {2017},
257	  booktitle = {Proceedings of the International Conference on Learning Representations (ICLR)},
258	  url = {https://arxiv.org/abs/1609.07843},
259	}
260	
261	@inproceedings{hinton2015distilling,
262	  title = {Distilling the Knowledge in a Neural Network},
263	  author = {Geoffrey Hinton and Oriol Vinyals and Jeff Dean},
264	  year = {2015},
265	  booktitle = {NeurIPS 2014 Deep Learning Workshop},
266	  url = {https://arxiv.org/abs/1503.02531},
267	}
268	
269	@article{bengio2013ste,
270	  title = {Estimating or Propagating Gradients Through Stochastic Neurons for Conditional Computation},
271	  author = {Yoshua Bengio and Nicholas L\'{e}onard and Aaron Courville},
272	  year = {2013},
273	  journal = {arXiv preprint arXiv:1308.3432},
274	  url = {https://arxiv.org/abs/1308.3432},
275	}
276	
277	@inproceedings{loshchilov2019adamw,
278	  title = {Decoupled Weight Decay Regularization},
279	  author = {Ilya Loshchilov and Frank Hutter},
280	  year = {2019},
281	  booktitle = {Proceedings of the International Conference on Learning Representations (ICLR)},
282	  url = {https://arxiv.org/abs/1711.05101},
283	}
284	
285	@article{raffel2020c4,
286	  title = {Exploring the Limits of Transfer Learning with a Unified Text-to-Text Transformer},
287	  author = {Colin Raffel and Noam Shazeer and Adam Roberts and Katherine Lee and Sharan Narang and Michael Matena and Yanqi Zhou and Wei Li and Peter J. Liu},
288	  year = {2020},
289	  journal = {Journal of Machine Learning Research},
290	  volume = {21},
291	  number = {140},
292	  pages = {1--67},
293	  url = {https://arxiv.org/abs/1910.10683},
294	}
295	
296	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "65f6f5cb-ffe8-4e93-8e4e-205019e93ba8",
  "isSidechain": false,
  "promptId": "e22b3aa5-f147-4b55-a02c-533b2c761d41",
  "type": "user",
  "uuid": "ba7be404-db7e-400c-80b3-ad51b2b8f5e6",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/references.bib",
      "content": "% =============================================================================\n% Direction 1: KL distillation for structured/activation sparsity\n% =============================================================================\n\n@inproceedings{fang2024maskllm,\n  title = {MaskLLM: Learnable Semi-Structured Sparsity for Large Language Models},\n  author = {Gongfan Fang and Hongxu Yin and Saurav Muralidharan and Greg Heinrich and Jeff Pool and Jan Kautz and Pavlo Molchanov and Xinchao Wang},\n  year = {2024},\n  booktitle = {Advances in Neural Information Processing Systems (NeurIPS)},\n  url = {https://arxiv.org/abs/2409.17481},\n}\n\n@inproceedings{xu2026spon,\n  title = {Resting Neurons, Active Insights: Robustify Activation Sparsity for Large Language Models},\n  author = {Haotian Xu and Jiannan Yang and Tian Gao and Tsui-Wei Weng and Tengfei Ma},\n  year = {2026},\n  booktitle = {Proceedings of the International Conference on Machine Learning (ICML)},\n  url = {https://arxiv.org/abs/2512.12744},\n}\n\n@inproceedings{muralidharan2024minitron,\n  title = {Compact Language Models via Pruning and Knowledge Distillation},\n  author = {Saurav Muralidharan and Sharath Turuvekere Sreenivas and Raviraj Joshi and Marcin Chochowski and Mostofa Patwary and Mohammad Shoeybi and Bryan Catanzaro and Jan Kautz and Pavlo Molchanov},\n  year = {2024},\n  booktitle = {Advances in Neural Information Processing Systems (NeurIPS)},\n  url = {https://arxiv.org/abs/2407.14679},\n}\n\n\n% =============================================================================\n% Direction 3: SPON and learnable bias correction for sparsity\n% =============================================================================\n\n@article{gautam2026fastforward,\n  title = {Fast Forward: Accelerating LLM Prefill with Predictive FFN Sparsity},\n  author = {Aayush Gautam and Mukul Gagrani and Junyoung Park and Mingu Lee and Chiris Lott and Narasimha Reddy},\n  year = {2026},\n  journal = {arXiv preprint arXiv:2602.00397},\n  url = {https://arxiv.org/abs/2602.00397},\n}\n\n\n% =============================================================================\n% Direction 4: Predictor-based activation sparsity\n% =============================================================================\n\n@inproceedings{liu2025teal,\n  title = {Training-Free Activation Sparsity in Large Language Models},\n  author = {James Liu and Pragaash Ponnusamy and Tianle Cai and Han Guo and Yoon Kim and Ben Athiwaratkun},\n  year = {2025},\n  booktitle = {Proceedings of the International Conference on Learning Representations (ICLR)},\n  url = {https://arxiv.org/abs/2408.14690},\n}\n\n@inproceedings{liu2023dejavu,\n  title = {Deja Vu: Contextual Sparsity for Efficient LLMs at Inference Time},\n  author = {Zichang Liu and Jue Wang and Tri Dao and Tianyi Zhou and Binhang Yuan and Zhao Song and Anshumali Shrivastava and Ce Zhang and Yuandong Tian and Christopher Re and Beidi Chen},\n  year = {2023},\n  booktitle = {Proceedings of the International Conference on Machine Learning (ICML)},\n  url = {https://arxiv.org/abs/2310.17157},\n}\n\n@inproceedings{akhauri2024shadowllm,\n  title = {ShadowLLM: Predictor-based Contextual Sparsity for Large Language Models},\n  author = {Yash Akhauri and Ahmed F AbouElhamayed and Jordan Dotzel and Zhiru Zhang and Alexander M Rush and Safeen Huda and Mohamed S Abdelfattah},\n  year = {2024},\n  booktitle = {Proceedings of the Conference on Empirical Methods in Natural Language Processing (EMNLP)},\n  url = {https://arxiv.org/abs/2406.16635},\n}\n\n\n@article{lee2024cats,\n  title = {CATS: Contextually-Aware Thresholding for Sparsity in Large Language Models},\n  author = {Donghyun Lee and Je-Yong Lee and Genghan Zhang and Mo Tiwari and Azalia Mirhoseini},\n  year = {2024},\n  journal = {arXiv preprint arXiv:2404.08763},\n  url = {https://arxiv.org/abs/2404.08763},\n}\n\n@inproceedings{zhang2025rsparse,\n  title = {R-Sparse: Rank-Aware Activation Sparsity for Efficient LLM Inference},\n  author = {Zhenyu Zhang and Zechun Liu and Yuandong Tian and Harshit Khaitan and Zhangyang Wang and Steven Li},\n  year = {2025},\n  booktitle = {Proceedings of the International Conference on Learning Representations (ICLR)},\n  url = {https://arxiv.org/abs/2504.19449},\n}\n\n@inproceedings{federici2025dip,\n  title = {Efficient LLM Inference using Dynamic Input Pruning and Cache-Aware Masking},\n  author = {Marco Federici and Davide Belli and Mart van Baalen and Amir Jalalirad and Andrii Skliar and Bence Major and Markus Nagel and Paul Whatmough},\n  year = {2024},\n  booktitle = {Proceedings of Machine Learning and Systems (MLSys)},\n  url = {https://arxiv.org/abs/2412.01380},\n}\n\n% =============================================================================\n% Activation function replacement and sparsity enhancement\n% =============================================================================\n\n@inproceedings{mirzadeh2024relu,\n  title = {ReLU Strikes Back: Exploiting Activation Sparsity in Large Language Models},\n  author = {Iman Mirzadeh and Keivan Alizadeh and Sachin Mehta and Carlo C Del Mundo and Oncel Tuzel and Golnoosh Samei and Mohammad Rastegari and Mehrdad Farajtabar},\n  year = {2024},\n  booktitle = {Proceedings of the International Conference on Learning Representations (ICLR)},\n  url = {https://arxiv.org/abs/2310.04564},\n}\n\n@article{song2024turbosparse,\n  title = {Turbo Sparse: Achieving LLM SOTA Performance with Minimal Activated Parameters},\n  author = {Yixin Song and Haotong Xie and Zhengyan Zhang and Bo Wen and Li Ma and Zeyu Mi and Haibo Chen},\n  year = {2024},\n  journal = {arXiv preprint arXiv:2406.05955},\n  url = {https://arxiv.org/abs/2406.05955},\n}\n\n@inproceedings{song2025prosparse,\n  title = {ProSparse: Introducing and Enhancing Intrinsic Activation Sparsity within Large Language Models},\n  author = {Chenyang Song and Xu Han and Zhengyan Zhang and Shengding Hu and Xiyu Shi and Kuai Li and Chen Chen and Zhiyuan Liu and Guangli Li and Tao Yang and Maosong Sun},\n  year = {2025},\n  booktitle = {Proceedings of the International Conference on Computational Linguistics (COLING)},\n  url = {https://arxiv.org/abs/2402.13516},\n}\n\n@article{luo2024sparsinglaw,\n  title = {Sparsing Law: Towards Large Language Models with Greater Activation Sparsity},\n  author = {Yuqi Luo and Chenyang Song and Xu Han and Yingfa Chen and Chaojun Xiao and Xiaojun Meng and Liqun Deng and Jiansheng Wei and Zhiyuan Liu and Maosong Sun},\n  year = {2024},\n  journal = {arXiv preprint arXiv:2411.02335},\n  url = {https://arxiv.org/abs/2411.02335},\n}\n\n\n@inproceedings{song2024powerinfer,\n  title = {PowerInfer: Fast Large Language Model Serving with a Consumer-grade GPU},\n  author = {Yixin Song and Zeyu Mi and Haotong Xie and Haibo Chen},\n  year = {2024},\n  booktitle = {Proceedings of the ACM Symposium on Operating Systems Principles (SOSP)},\n  url = {https://arxiv.org/abs/2312.12456},\n}\n\n\n% =============================================================================\n% KL distillation and knowledge distillation\n% =============================================================================\n\n@inproceedings{kim2016sequencekd,\n  title = {Sequence-Level Knowledge Distillation},\n  author = {Yoon Kim and Alexander M. Rush},\n  year = {2016},\n  booktitle = {Proceedings of the Conference on Empirical Methods in Natural Language Processing (EMNLP)},\n  url = {https://arxiv.org/abs/1606.07947},\n}\n\n@article{sanh2019distilbert,\n  title = {DistilBERT, a distilled version of BERT: smaller, faster, cheaper and lighter},\n  author = {Victor Sanh and Lysandre Debut and Julien Chaumond and Thomas Wolf},\n  year = {2019},\n  journal = {arXiv preprint arXiv:1910.01108},\n  url = {https://arxiv.org/abs/1910.01108},\n}\n\n% =============================================================================\n% Weight pruning methods\n% =============================================================================\n\n@inproceedings{sun2024wanda,\n  title = {A Simple and Effective Pruning Approach for Large Language Models},\n  author = {Mingjie Sun and Zhuang Liu and Anna Bair and J. Zico Kolter},\n  year = {2024},\n  booktitle = {Proceedings of the International Conference on Learning Representations (ICLR)},\n  url = {https://arxiv.org/abs/2306.11695},\n}\n\n@inproceedings{frantar2023sparsegpt,\n  title = {SparseGPT: Massive Language Models Can Be Accurately Pruned in One-Shot},\n  author = {Elias Frantar and Dan Alistarh},\n  year = {2023},\n  booktitle = {Proceedings of the International Conference on Machine Learning (ICML)},\n  url = {https://arxiv.org/abs/2301.00774},\n}\n\n% =============================================================================\n% Conditional computation and MoE\n% =============================================================================\n\n@article{fedus2022switch,\n  title = {Switch Transformers: Scaling to Trillion Parameter Models with Simple and Efficient Sparsity},\n  author = {William Fedus and Barret Zoph and Noam Shazeer},\n  year = {2022},\n  journal = {Journal of Machine Learning Research},\n  volume = {23},\n  number = {120},\n  pages = {1--40},\n  url = {https://arxiv.org/abs/2101.03961},\n}\n\n% =============================================================================\n% Relaxation methods (Gumbel/Concrete)\n% =============================================================================\n\n@inproceedings{louizos2018l0,\n  title = {Learning Sparse Neural Networks through $L_0$ Regularization},\n  author = {Christos Louizos and Max Welling and Diederik P. Kingma},\n  year = {2018},\n  booktitle = {Proceedings of the International Conference on Learning Representations (ICLR)},\n  url = {https://arxiv.org/abs/1712.01312},\n}\n\n@inproceedings{maddison2017concrete,\n  title = {The Concrete Distribution: A Continuous Relaxation of Discrete Random Variables},\n  author = {Chris J. Maddison and Andriy Mnih and Yee Whye Teh},\n  year = {2017},\n  booktitle = {Proceedings of the International Conference on Learning Representations (ICLR)},\n  url = {https://arxiv.org/abs/1611.00712},\n}\n\n% =============================================================================\n% Foundational references\n% =============================================================================\n\n@article{grattafiori2024llama3,\n  title = {The Llama 3 Herd of Models},\n  author = {Aaron Grattafiori and Abhimanyu Dubey and Abhinav Jauhri and Abhinav Pandey and Abhishek Kadian and Ahmad Al-Dahle and Aieleen Lakber and Aimin Chen and Ait Mokhtar Salma and Ajay Menon},\n  year = {2024},\n  journal = {arXiv preprint arXiv:2407.21783},\n  url = {https://arxiv.org/abs/2407.21783},\n}\n\n@article{jiang2023mistral,\n  title = {Mistral 7B},\n  author = {Albert Q. Jiang and Alexandre Sablayrolles and Arthur Mensch and Chris Bamford and Devendra Singh Chaplot and Diego de las Casas and Florian Bressand and Gianna Lengyel and Guillaume Lample and Lucile Saulnier},\n  year = {2023},\n  journal = {arXiv preprint arXiv:2310.06825},\n  url = {https://arxiv.org/abs/2310.06825},\n}\n\n@inproceedings{jang2017gumbel,\n  title = {Categorical Reparameterization with Gumbel-Softmax},\n  author = {Eric Jang and Shixiang Gu and Ben Poole},\n  year = {2017},\n  booktitle = {Proceedings of the International Conference on Learning Representations (ICLR)},\n  url = {https://arxiv.org/abs/1611.01144},\n}\n\n@article{shazeer2020glu,\n  title = {GLU Variants Improve Transformer},\n  author = {Noam Shazeer},\n  year = {2020},\n  journal = {arXiv preprint arXiv:2002.05202},\n  url = {https://arxiv.org/abs/2002.05202},\n}\n\n@inproceedings{merity2017pointer,\n  title = {Pointer Sentinel Mixture Models},\n  author = {Stephen Merity and Caiming Xiong and James Bradbury and Richard Socher},\n  year = {2017},\n  booktitle = {Proceedings of the International Conference on Learning Representations (ICLR)},\n  url = {https://arxiv.org/abs/1609.07843},\n}\n\n@inproceedings{hinton2015distilling,\n  title = {Distilling the Knowledge in a Neural Network},\n  author = {Geoffrey Hinton and Oriol Vinyals and Jeff Dean},\n  year = {2015},\n  booktitle = {NeurIPS 2014 Deep Learning Workshop},\n  url = {https://arxiv.org/abs/1503.02531},\n}\n\n@article{bengio2013ste,\n  title = {Estimating or Propagating Gradients Through Stochastic Neurons for Conditional Computation},\n  author = {Yoshua Bengio and Nicholas L\\'{e}onard and Aaron Courville},\n  year = {2013},\n  journal = {arXiv preprint arXiv:1308.3432},\n  url = {https://arxiv.org/abs/1308.3432},\n}\n\n@inproceedings{loshchilov2019adamw,\n  title = {Decoupled Weight Decay Regularization},\n  author = {Ilya Loshchilov and Frank Hutter},\n  year = {2019},\n  booktitle = {Proceedings of the International Conference on Learning Representations (ICLR)},\n  url = {https://arxiv.org/abs/1711.05101},\n}\n\n@article{raffel2020c4,\n  title = {Exploring the Limits of Transfer Learning with a Unified Text-to-Text Transformer},\n  author = {Colin Raffel and Noam Shazeer and Adam Roberts and Katherine Lee and Sharan Narang and Michael Matena and Yanqi Zhou and Wei Li and Peter J. Liu},\n  year = {2020},\n  journal = {Journal of Machine Learning Research},\n  volume = {21},\n  number = {140},\n  pages = {1--67},\n  url = {https://arxiv.org/abs/1910.10683},\n}\n\n",
      "numLines": 296,
      "startLine": 1,
      "totalLines": 296
    }
  },
  "sourceToolAssistantUUID": "65f6f5cb-ffe8-4e93-8e4e-205019e93ba8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/review_reviewer_1_772f066c",
  "sessionId": "fd7408d6-e7e0-4bb4-8dde-4202758b928d",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Runtime record

_source line 55_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[Round 1 审稿请求]: 你负责**方法严谨性 + 实验有效性**的审查。  ## Venue 信息 - **目标会议**: EMNLP 2026 (via ACL Rolling Review, May cycle) - **截止日期**: 2026-05-25 - **页数限制**: Long paper ≤8 页正文 + unlimited references + appendix…",
  "leafUuid": "ba7be404-db7e-400c-80b3-ad51b2b8f5e6",
  "sessionId": "fd7408d6-e7e0-4bb4-8dde-4202758b928d"
}
```

---

### Runtime record

_source line 56_

```json
{
  "type": "ai-title",
  "aiTitle": "Review paper on sparse SwiGLU distillation methods",
  "sessionId": "fd7408d6-e7e0-4bb4-8dde-4202758b928d"
}
```

---

### Assistant

_source line 57 · 2026-05-17T08:14:14.586Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have read the complete paper. Let me now do a thorough review focusing on:

1. **Method correctness** (KL gradient analysis, Gumbel-Sigmoid, adaptive penalty controller, BCE vs KL mismatch argument)
2. **Experimental validity** (fairness of comparisons, ablation completeness, statistical power, generalization, data leakage, downstream collapse)
3. **Reproducibility** (hyperparameters, training details, inference protocol)
4. **Latency claim** (wall-clock speedup, net overhead)

Let me also verify references.


Now I'm checking the ARR reviewer guidelines and composing my review systematically. The paper proposes training lightweight sparsity predictors for SwiGLU-based LLMs using KL divergence instead of BCE, arguing that BCE has a structural mismatch with global top-k allocation since BCE gradients operate per-neuron while inference uses global allocation, whereas KL divergence couples all neurons through the output distribution via Gumbel-Sigmoid relaxation, achieving PPL 11.79 at 50% sparsity on LLaMA-3.1-8B compared to 23.31 for the baseline.

Looking at the method correctness, the gradient chain rule decomposition for the KL loss is mathematically sound and follows standard calculus.

The key insight is that factor (b)—the Jacobian through downstream layers—creates inter-neuron coupling, but this alone isn't what makes KL special. MSE on hidden states would also have some cross-layer effects, yet the crucial difference is that KL couples through the output distribution itself, not just intermediate computations. I initially thought MSE might avoid this coupling if computed independently at each layer, but that's the point—KL requires end-to-end differentiation through the full network, creating a fundamentally different gradient structure than layer-wise objectives.

Now I'm checking whether the factor decomposition is actually complete. The paper correctly applies the chain rule for a single neuron's gradient, and while it doesn't explicitly mention that gradients depend on mask values of other neurons in the same layer, this is implicitly handled through factor (c) and the sparse hidden state. Factor (c) captures the local effect of changing one mask on the hidden state, and the coupling between neurons in the same layer flows through factor (b) when the Jacobian propagates the effects of the full hidden state downstream. The masks in the same layer don't directly interact—they only couple through downstream computation, which makes sense for the element-wise masking in SwiGLU. Now I'm looking at how the paper relaxes the discrete masks using Gumbel-Sigmoid, which is the binary version of Gumbel-Softmax from Jang et al. (2017), allowing differentiable sampling with a temperature parameter.

There's a meaningful gap here though: the model trains with soft masks from the Gumbel-Sigmoid relaxation but evaluates with hard binary masks from TEAL's top-k selection. The paper acknowledges this train-test mismatch but doesn't formally quantify how much of the performance gap comes from this discrepancy, even though temperature annealing from 1.0 to 0.1 should help bridge it.

Looking at Table 5, the per-token evaluation shows 9.218 for d_b=128 while TEAL's global evaluation reaches 11.963—that's roughly a 30% difference, which suggests the mismatch between training and evaluation is more significant than the paper addresses.

For the adaptive penalty controller, the paper is transparent about using a multiplicative schedule rather than formal dual updates, which trades theoretical guarantees for training stability. The mechanism adjusts the penalty weight by doubling when sparsity exceeds the target, halving when it falls short, and holding steady otherwise.

The issue is that this heuristic lacks convergence guarantees, and more problematically, the penalty weight hits its ceiling at certain targets—like reaching 5000 at 30% sparsity while only achieving 28.5%, meaning the controller can't actually enforce the target once it maxes out. The paper also claims this is parameter-free, but λ_max varies across different sparsity targets, which undermines that claim.

Now looking at the BCE versus KL structural mismatch: the gradient structures are genuinely different—BCE only depends on individual neurons while KL couples through the full downstream Jacobian. The oracle F1 results do show something compelling: BCE hits 0.613 while KL gets 0.540, yet KL produces 91% better perplexity. But here's the catch—the oracle mask is just the dense model's top-k neurons by magnitude, which might not actually be optimal for preserving output quality. So BCE could be failing not because of the structural mismatch itself, but because the oracle target they're comparing against isn't the true ground truth.

The paper frames this as "BCE has structural mismatch with global top-k," but it's more nuanced: BCE is optimizing agreement with a magnitude-based oracle that doesn't correlate well with actual output distribution preservation. The gradient SNR analysis from Section 3.5 is interesting, though there's a methodological concern—they measured SNR on C4 data while training happened on WikiText-103, which could introduce a distribution mismatch.

Looking at the experimental setup, KL trains for 1000 steps while BCE gets compared at both 1000 and 2700 steps, which is fair. But the systems differ in more ways than just the loss function: KL uses Gumbel-Sigmoid with a penalty controller while BCE uses hard masking with compensation. The ablation showing "BCE + Gumbel + Penalty" performs worse (38.02 PPL vs 27.97) suggests the architectural choices interact with the objective in ways that make it hard to isolate the loss function's actual contribution.

Looking more carefully at the ablation results, KL with STE gets 15.77 versus BCE's 27.97 — a substantial gap that does support the loss function argument. However, KL+STE still benefits from the full end-to-end forward pass structure, which gives it an inherent advantage. A truly fair comparison would test something like MSE on output logits with STE to isolate just the loss function effect while controlling for the gradient mechanism, but that experiment isn't included.

Beyond the loss function, there are several confounding factors I'm noticing. The predictor architecture stays fixed across all experiments with no exploration of alternatives like attention-based routing. The paper also doesn't specify whether BCE received the same hyperparameter tuning as KL — learning rates and batch sizes could matter significantly. And there's no test of whether KL-trained predictors could benefit from FastForward's compensation approach, which would weaken the claim that KL eliminates the need for compensation entirely.

On the statistical side, three seeds give a tight confidence interval for PPL stability, but the evaluation is limited to just the 50% uniform allocation scenario.  Downstream metrics like ARC-c show more variance, while MMLU hovers near random chance, so the signal there is weak. Three seeds is acceptable by field standards but borderline for making strong statistical claims.

The cross-architecture evaluation is also narrow — only LLaMA-3.1-8B and Mistral-7B-v0.3, both in the 7-8B range with SwiGLU activations. There's no testing at larger scales or with different activation functions, though the method is inherently SwiGLU-specific.

For out-of-distribution evaluation, WikiText-103 and WikiText-2 share the same Wikipedia source, so there's distributional leakage. The C4 results show a meaningful gap (KL at 18.40 vs TEAL at 38.75), but that's just one sparsity level, and more comprehensive OOD testing would be valuable.

The bigger issue is downstream collapse at 50% sparsity — MMLU drops to random performance and GSM8K becomes essentially unusable across all methods. The paper frames this as a capacity-limited regime, but it's a serious practical limitation if the approach can't maintain reasoning ability at that sparsity level.

On latency, there's a critical disconnect: the pipeline adds 6.4% overhead to dense inference, and while eliminating compensation saves 2.7%, there's no actual wall-clock speedup because unstructured masks don't benefit from sparse kernel support. The paper acknowledges this limitation, but the latency claims need more careful framing.

For reproducibility, the training setup is clearly documented with specific model choices, data parameters, optimizer settings, and predictor architecture details that should enable replication.

However, several critical details are missing: the weight decay coefficient for AdamW, whether gradient clipping was applied, the actual training duration and hardware setup beyond the brief mention in limitations, and most importantly, the exact procedure for computing oracle masks from the dense model's activations—whether they use per-layer or global top-k selection. The evaluation batch size for perplexity measurements also isn't specified.

The predictor-TEAL inference pipeline itself is well-explained: the predictor generates sparsity scores that feed into TEAL's global top-k selection mechanism.

On the taxonomy issue, there's a classification problem where ShadowLLM is categorized as per-layer intermediate-level sparsity, but the paper's own description suggests it uses per-token attention-based routing, which doesn't align with that categorization.

The paper is generally well-written with a clear presentation of the structural mismatch argument and a useful 2D taxonomy framework. However, some relevant work is overlooked—particularly speculative decoding methods that leverage sparsity, dynamic inference and early-exit approaches, and other Gumbel-based differentiable pruning techniques beyond the cited L0 regularization.

Regarding the multiplicative schedule, the paper's connection to augmented Lagrangian methods is somewhat loose—it's actually using a penalty method with multiplicative updates rather than a true Lagrangian approach. While this lacks formal convergence guarantees, the empirical results demonstrate it works in practice. I also notice that at 30% sparsity the controller undershoots to 28.5%, a 5% deviation that's buried in Table 7 but deserves more discussion as a controller limitation.

Now I'm compiling the critical issues: the lack of wall-clock speedup is a major problem for an efficiency-focused paper, especially with the 6.4% overhead, so the framing needs substantial revision. The downstream task performance is concerning too—MMLU and GSM8K degrade severely at 50% sparsity and noticeably at 30%, which contradicts the perplexity improvements. The experimental evaluation is also quite narrow, limited to 7-8B models, WikiText-based training, and just two architectures. Beyond these critical gaps, there's the train-test mismatch between soft Gumbel masks during training and hard top-k at inference that creates roughly a 30% perplexity gap shown in Table 5, and I need to verify whether the BCE comparison is actually fair.

I'm also noting that three seeds at a single configuration provides limited statistical power, the "parameter-free" claim is misleading since λ_max varies across sparsity targets, and the penalty controller can't actually enforce all targets—the 30% target only achieves 28.5% because it hits the cap. There are also minor details missing like the weight decay value, oracle mask computation specifics, and some SNR measurement inconsistencies. Looking at the soundness score, the core method and gradient analysis are solid, but the experimental gaps around fairness and limited scale bring it to around 3.5/5—acceptable but with notable limitations.

The structural insight about the BCE versus KL mismatch is genuinely interesting, and the 2D taxonomy is a useful organizational contribution. But the lack of actual wall-clock speedup and the downstream collapse issues are serious practical concerns that limit how exciting this feels—maybe 2.5 to 3 out of 5. Reproducibility is decent with good hyperparameter reporting, though some details are missing, so that's around 3.5/5. Overall, the paper has a clear and interesting core idea with adequate experimental support, but those practical limitations and the writing quality suggest this lands somewhere between a Findings acceptance and a resubmit—probably 2.5 to 3 out of 5.

The main contributions really boil down to showing that KL outperforms BCE for training sparsity predictors with strong empirical evidence, providing a clean theoretical explanation through gradient analysis, and offering a useful 2D taxonomy for organizing the space.

The regime analysis adds an interesting empirical dimension to the findings. But stacked against the weaknesses—no practical speedup, downstream collapse at moderate sparsity levels, limited experimental scale at only 7-8B parameters, and some fairness concerns in the experimental setup—this feels borderline for a top venue like ACL or EMNLP. The theoretical insight is solid and the experiments back it up, but the practical impact just isn't there. I'm leaning toward a 3 out of 5, which could work as a Findings paper.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ba7be404-db7e-400c-80b3-ad51b2b8f5e6",
  "isSidechain": false,
  "requestId": "req_011Cb7oaozXrVyu8Pse6Ta64",
  "type": "assistant",
  "uuid": "bea9530c-bce2-4bdc-9582-6b265104ba46",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/review_reviewer_1_772f066c",
  "sessionId": "fd7408d6-e7e0-4bb4-8dde-4202758b928d",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KYmbmM4HBiFnhRcZ24sYgo",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5027,
      "cache_read_input_tokens": 54653,
      "output_tokens": 5565,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5027,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 5565,
          "cache_read_input_tokens": 54653,
          "cache_creation_input_tokens": 5027,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5027
          },
          "type": "message"
        }
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

_source line 58 · 2026-05-17T08:14:14.588Z_

论文通读完毕。现在验证引用并搜索 ARR reviewer guidelines 的更多细节。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bea9530c-bce2-4bdc-9582-6b265104ba46",
  "isSidechain": false,
  "requestId": "req_011Cb7oaozXrVyu8Pse6Ta64",
  "type": "assistant",
  "uuid": "e63180f4-89ab-4795-acfd-3291622500a9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/review_reviewer_1_772f066c",
  "sessionId": "fd7408d6-e7e0-4bb4-8dde-4202758b928d",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KYmbmM4HBiFnhRcZ24sYgo",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5027,
      "cache_read_input_tokens": 54653,
      "output_tokens": 5565,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5027,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 5565,
          "cache_read_input_tokens": 54653,
          "cache_creation_input_tokens": 5027,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5027
          },
          "type": "message"
        }
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

_source line 59 · 2026-05-17T08:14:15.998Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__verify_references · `toolu_01QajKP6bsuXGREdoudV7ru7`</summary>

```json
{
  "paper_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper",
  "project": "distill_sparse_swiglu"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e63180f4-89ab-4795-acfd-3291622500a9",
  "isSidechain": false,
  "requestId": "req_011Cb7oaozXrVyu8Pse6Ta64",
  "type": "assistant",
  "uuid": "a230e0b6-9b98-4a62-96aa-71199069e522",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/review_reviewer_1_772f066c",
  "sessionId": "fd7408d6-e7e0-4bb4-8dde-4202758b928d",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KYmbmM4HBiFnhRcZ24sYgo",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5027,
      "cache_read_input_tokens": 54653,
      "output_tokens": 5565,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5027,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 5565,
          "cache_read_input_tokens": 54653,
          "cache_creation_input_tokens": 5027,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5027
          },
          "type": "message"
        }
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

_source line 60 · 2026-05-17T08:14:18.449Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_019z7pVeXsedBMjCFFboA31r`</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewerguidelines",
  "prompt": "Extract the detailed reviewer guidelines: what should reviewers focus on, what dimensions matter most, any specific instructions about experimental evaluation, reproducibility, claims vs evidence. Include scoring rubric details if any."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a230e0b6-9b98-4a62-96aa-71199069e522",
  "isSidechain": false,
  "requestId": "req_011Cb7oaozXrVyu8Pse6Ta64",
  "type": "assistant",
  "uuid": "57990846-c63e-4031-9fc6-87df705f15eb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/review_reviewer_1_772f066c",
  "sessionId": "fd7408d6-e7e0-4bb4-8dde-4202758b928d",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KYmbmM4HBiFnhRcZ24sYgo",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5027,
      "cache_read_input_tokens": 54653,
      "output_tokens": 5565,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5027,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 5565,
          "cache_read_input_tokens": 54653,
          "cache_creation_input_tokens": 5027,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5027
          },
          "type": "message"
        }
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

_source line 61_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[Round 1 审稿请求]: 你负责**方法严谨性 + 实验有效性**的审查。  ## Venue 信息 - **目标会议**: EMNLP 2026 (via ACL Rolling Review, May cycle) - **截止日期**: 2026-05-25 - **页数限制**: Long paper ≤8 页正文 + unlimited references + appendix…",
  "leafUuid": "57990846-c63e-4031-9fc6-87df705f15eb",
  "sessionId": "fd7408d6-e7e0-4bb4-8dde-4202758b928d"
}
```

---

### Runtime record

_source line 62_

```json
{
  "type": "ai-title",
  "aiTitle": "Review paper on sparse SwiGLU distillation methods",
  "sessionId": "fd7408d6-e7e0-4bb4-8dde-4202758b928d"
}
```

---

### Tool result

_source line 63 · 2026-05-17T08:14:45.630Z_

<details><summary>↩ Tool result · `toolu_01QajKP6bsuXGREdoudV7ru7`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"summary\": {\"total_bib_entries\": 31, \"total_citations\": 58, \"unique_cited_keys\": 31, \"orphan_bib\": 0, \"missing_bib\": 0, \"duplicate_keys\": 0, \"online_verified\": 29, \"online_not_found\": 0, \"online_mismatch\": 2}, \"cross_check\": {\"orphan_bib\": [], \"missing_bib\": [], \"orphan_count\": 0, \"missing_count\": 0}, \"bib_entries\": [{\"key\": \"fang2024maskllm\", \"type\": \"inproceedings\", \"title\": \"MaskLLM: Learnable Semi-Structured Sparsity for Large Language Models\", \"authors\": \"Gongfan Fang and Hongxu Yin and Saurav Muralidharan and Greg Heinrich and Jeff P...\", \"year\": \"2024\", \"venue\": \"Advances in Neural Information Processing Systems (NeurIPS)\"}, {\"key\": \"xu2026spon\", \"type\": \"inproceedings\", \"title\": \"Resting Neurons, Active Insights: Robustify Activation Sparsity for Large Language Models\", \"authors\": \"Haotian Xu and Jiannan Yang and Tian Gao and Tsui-Wei Weng and Tengfei Ma\", \"year\": \"2026\", \"venue\": \"Proceedings of the International Conference on Machine Learning (ICML)\"}, {\"key\": \"muralidharan2024minitron\", \"type\": \"inproceedings\", \"title\": \"Compact Language Models via Pruning and Knowledge Distillation\", \"authors\": \"Saurav Muralidharan and Sharath Turuvekere Sreenivas and Raviraj Joshi and Marci...\", \"year\": \"2024\", \"venue\": \"Advances in Neural Information Processing Systems (NeurIPS)\"}, {\"key\": \"gautam2026fastforward\", \"type\": \"article\", \"title\": \"Fast Forward: Accelerating LLM Prefill with Predictive FFN Sparsity\", \"authors\": \"Aayush Gautam and Mukul Gagrani and Junyoung Park and Mingu Lee and Chiris Lott ...\", \"year\": \"2026\", \"venue\": \"arXiv preprint arXiv:2602.00397\"}, {\"key\": \"liu2025teal\", \"type\": \"inproceedings\", \"title\": \"Training-Free Activation Sparsity in Large Language Models\", \"authors\": \"James Liu and Pragaash Ponnusamy and Tianle Cai and Han Guo and Yoon Kim and Ben...\", \"year\": \"2025\", \"venue\": \"Proceedings of the International Conference on Learning Representations (ICLR)\"}, {\"key\": \"liu2023dejavu\", \"type\": \"inproceedings\", \"title\": \"Deja Vu: Contextual Sparsity for Efficient LLMs at Inference Time\", \"authors\": \"Zichang Liu and Jue Wang and Tri Dao and Tianyi Zhou and Binhang Yuan and Zhao S...\", \"year\": \"2023\", \"venue\": \"Proceedings of the International Conference on Machine Learning (ICML)\"}, {\"key\": \"akhauri2024shadowllm\", \"type\": \"inproceedings\", \"title\": \"ShadowLLM: Predictor-based Contextual Sparsity for Large Language Models\", \"authors\": \"Yash Akhauri and Ahmed F AbouElhamayed and Jordan Dotzel and Zhiru Zhang and Ale...\", \"year\": \"2024\", \"venue\": \"Proceedings of the Conference on Empirical Methods in Natural Language Processin...\"}, {\"key\": \"lee2024cats\", \"type\": \"article\", \"title\": \"CATS: Contextually-Aware Thresholding for Sparsity in Large Language Models\", \"authors\": \"Donghyun Lee and Je-Yong Lee and Genghan Zhang and Mo Tiwari and Azalia Mirhosei...\", \"year\": \"2024\", \"venue\": \"arXiv preprint arXiv:2404.08763\"}, {\"key\": \"zhang2025rsparse\", \"type\": \"inproceedings\", \"title\": \"R-Sparse: Rank-Aware Activation Sparsity for Efficient LLM Inference\", \"authors\": \"Zhenyu Zhang and Zechun Liu and Yuandong Tian and Harshit Khaitan and Zhangyang ...\", \"year\": \"2025\", \"venue\": \"Proceedings of the International Conference on Learning Representations (ICLR)\"}, {\"key\": \"federici2025dip\", \"type\": \"inproceedings\", \"title\": \"Efficient LLM Inference using Dynamic Input Pruning and Cache-Aware Masking\", \"authors\": \"Marco Federici and Davide Belli and Mart van Baalen and Amir Jalalirad and Andri...\", \"year\": \"2024\", \"venue\": \"Proceedings of Machine Learning and Systems (MLSys)\"}, {\"key\": \"mirzadeh2024relu\", \"type\": \"inproceedings\", \"title\": \"ReLU Strikes Back: Exploiting Activation Sparsity in Large Language Models\", \"authors\": \"Iman Mirzadeh and Keivan Alizadeh and Sachin Mehta and Carlo C Del Mundo and Onc...\", \"year\": \"2024\", \"venue\": \"Proceedings of the International Conference on Learning Representations (ICLR)\"}, {\"key\": \"song2024turbosparse\", \"type\": \"article\", \"title\": \"Turbo Sparse: Achieving LLM SOTA Performance with Minimal Activated Parameters\", \"authors\": \"Yixin Song and Haotong Xie and Zhengyan Zhang and Bo Wen and Li Ma and Zeyu Mi a...\", \"year\": \"2024\", \"venue\": \"arXiv preprint arXiv:2406.05955\"}, {\"key\": \"song2025prosparse\", \"type\": \"inproceedings\", \"title\": \"ProSparse: Introducing and Enhancing Intrinsic Activation Sparsity within Large Language Models\", \"authors\": \"Chenyang Song and Xu Han and Zhengyan Zhang and Shengding Hu and Xiyu Shi and Ku...\", \"year\": \"2025\", \"venue\": \"Proceedings of the International Conference on Computational Linguistics (COLING...\"}, {\"key\": \"luo2024sparsinglaw\", \"type\": \"article\", \"title\": \"Sparsing Law: Towards Large Language Models with Greater Activation Sparsity\", \"authors\": \"Yuqi Luo and Chenyang Song and Xu Han and Yingfa Chen and Chaojun Xiao and Xiaoj...\", \"year\": \"2024\", \"venue\": \"arXiv preprint arXiv:2411.02335\"}, {\"key\": \"song2024powerinfer\", \"type\": \"inproceedings\", \"title\": \"PowerInfer: Fast Large Language Model Serving with a Consumer-grade GPU\", \"authors\": \"Yixin Song and Zeyu Mi and Haotong Xie and Haibo Chen\", \"year\": \"2024\", \"venue\": \"Proceedings of the ACM Symposium on Operating Systems Principles (SOSP)\"}, {\"key\": \"kim2016sequencekd\", \"type\": \"inproceedings\", \"title\": \"Sequence-Level Knowledge Distillation\", \"authors\": \"Yoon Kim and Alexander M. Rush\", \"year\": \"2016\", \"venue\": \"Proceedings of the Conference on Empirical Methods in Natural Language Processin...\"}, {\"key\": \"sanh2019distilbert\", \"type\": \"article\", \"title\": \"DistilBERT, a distilled version of BERT: smaller, faster, cheaper and lighter\", \"authors\": \"Victor Sanh and Lysandre Debut and Julien Chaumond and Thomas Wolf\", \"year\": \"2019\", \"venue\": \"arXiv preprint arXiv:1910.01108\"}, {\"key\": \"sun2024wanda\", \"type\": \"inproceedings\", \"title\": \"A Simple and Effective Pruning Approach for Large Language Models\", \"authors\": \"Mingjie Sun and Zhuang Liu and Anna Bair and J. Zico Kolter\", \"year\": \"2024\", \"venue\": \"Proceedings of the International Conference on Learning Representations (ICLR)\"}, {\"key\": \"frantar2023sparsegpt\", \"type\": \"inproceedings\", \"title\": \"SparseGPT: Massive Language Models Can Be Accurately Pruned in One-Shot\", \"authors\": \"Elias Frantar and Dan Alistarh\", \"year\": \"2023\", \"venue\": \"Proceedings of the International Conference on Machine Learning (ICML)\"}, {\"key\": \"fedus2022switch\", \"type\": \"article\", \"title\": \"Switch Transformers: Scaling to Trillion Parameter Models with Simple and Efficient Sparsity\", \"authors\": \"William Fedus and Barret Zoph and Noam Shazeer\", \"year\": \"2022\", \"venue\": \"Journal of Machine Learning Research\"}, {\"key\": \"louizos2018l0\", \"type\": \"inproceedings\", \"title\": \"Learning Sparse Neural Networks through $L_0$ Regularization\", \"authors\": \"Christos Louizos and Max Welling and Diederik P. Kingma\", \"year\": \"2018\", \"venue\": \"Proceedings of the International Conference on Learning Representations (ICLR)\"}, {\"key\": \"maddison2017concrete\", \"type\": \"inproceedings\", \"title\": \"The Concrete Distribution: A Continuous Relaxation of Discrete Random Variables\", \"authors\": \"Chris J. Maddison and Andriy Mnih and Yee Whye Teh\", \"year\": \"2017\", \"venue\": \"Proceedings of the International Conference on Learning Representations (ICLR)\"}, {\"key\": \"grattafiori2024llama3\", \"type\": \"article\", \"title\": \"The Llama 3 Herd of Models\", \"authors\": \"Aaron Grattafiori and Abhimanyu Dubey and Abhinav Jauhri and Abhinav Pandey and ...\", \"year\": \"2024\", \"venue\": \"arXiv preprint arXiv:2407.21783\"}, {\"key\": \"jiang2023mistral\", \"type\": \"article\", \"title\": \"Mistral 7B\", \"authors\": \"Albert Q. Jiang and Alexandre Sablayrolles and Arthur Mensch and Chris Bamford a...\", \"year\": \"2023\", \"venue\": \"arXiv preprint arXiv:2310.06825\"}, {\"key\": \"jang2017gumbel\", \"type\": \"inproceedings\", \"title\": \"Categorical Reparameterization with Gumbel-Softmax\", \"authors\": \"Eric Jang and Shixiang Gu and Ben Poole\", \"year\": \"2017\", \"venue\": \"Proceedings of the International Conference on Learning Representations (ICLR)\"}, {\"key\": \"shazeer2020glu\", \"type\": \"article\", \"title\": \"GLU Variants Improve Transformer\", \"authors\": \"Noam Shazeer\", \"year\": \"2020\", \"venue\": \"arXiv preprint arXiv:2002.05202\"}, {\"key\": \"merity2017pointer\", \"type\": \"inproceedings\", \"title\": \"Pointer Sentinel Mixture Models\", \"authors\": \"Stephen Merity and Caiming Xiong and James Bradbury and Richard Socher\", \"year\": \"2017\", \"venue\": \"Proceedings of the International Conference on Learning Representations (ICLR)\"}, {\"key\": \"hinton2015distilling\", \"type\": \"inproceedings\", \"title\": \"Distilling the Knowledge in a Neural Network\", \"authors\": \"Geoffrey Hinton and Oriol Vinyals and Jeff Dean\", \"year\": \"2015\", \"venue\": \"NeurIPS 2014 Deep Learning Workshop\"}, {\"key\": \"bengio2013ste\", \"type\": \"article\", \"title\": \"Estimating or Propagating Gradients Through Stochastic Neurons for Conditional Computation\", \"authors\": \"Yoshua Bengio and Nicholas L\\\\'eonard and Aaron Courville\", \"year\": \"2013\", \"venue\": \"arXiv preprint arXiv:1308.3432\"}, {\"key\": \"loshchilov2019adamw\", \"type\": \"inproceedings\", \"title\": \"Decoupled Weight Decay Regularization\", \"authors\": \"Ilya Loshchilov and Frank Hutter\", \"year\": \"2019\", \"venue\": \"Proceedings of the International Conference on Learning Representations (ICLR)\"}, {\"key\": \"raffel2020c4\", \"type\": \"article\", \"title\": \"Exploring the Limits of Transfer Learning with a Unified Text-to-Text Transformer\", \"authors\": \"Colin Raffel and Noam Shazeer and Adam Roberts and Katherine Lee and Sharan Nara...\", \"year\": \"2020\", \"venue\": \"Journal of Machine Learning Research\"}], \"tex_citations\": [{\"key\": \"shazeer2020glu\", \"file\": \"introduction.tex\", \"line\": 3, \"command\": \"cite\"}, {\"key\": \"liu2025teal\", \"file\": \"introduction.tex\", \"line\": 6, \"command\": \"cite\"}, {\"key\": \"grattafiori2024llama3\", \"file\": \"introduction.tex\", \"line\": 6, \"command\": \"cite\"}, {\"key\": \"liu2023dejavu\", \"file\": \"introduction.tex\", \"line\": 7, \"command\": \"cite\"}, {\"key\": \"gautam2026fastforward\", \"file\": \"introduction.tex\", \"line\": 7, \"command\": \"cite\"}, {\"key\": \"liu2025teal\", \"file\": \"introduction.tex\", \"line\": 14, \"command\": \"cite\"}, {\"key\": \"jang2017gumbel\", \"file\": \"introduction.tex\", \"line\": 27, \"command\": \"cite\"}, {\"key\": \"jiang2023mistral\", \"file\": \"introduction.tex\", \"line\": 34, \"command\": \"cite\"}, {\"key\": \"xu2026spon\", \"file\": \"introduction.tex\", \"line\": 35, \"command\": \"cite\"}, {\"key\": \"xu2026spon\", \"file\": \"introduction.tex\", \"line\": 38, \"command\": \"cite\"}, {\"key\": \"akhauri2024shadowllm\", \"file\": \"introduction.tex\", \"line\": 38, \"command\": \"cite\"}, {\"key\": \"gautam2026fastforward\", \"file\": \"introduction.tex\", \"line\": 38, \"command\": \"cite\"}, {\"key\": \"liu2023dejavu\", \"file\": \"introduction.tex\", \"line\": 38, \"command\": \"cite\"}, {\"key\": \"liu2025teal\", \"file\": \"related_work.tex\", \"line\": 4, \"command\": \"cite\"}, {\"key\": \"lee2024cats\", \"file\": \"related_work.tex\", \"line\": 5, \"command\": \"cite\"}, {\"key\": \"zhang2025rsparse\", \"file\": \"related_work.tex\", \"line\": 5, \"command\": \"cite\"}, {\"key\": \"federici2025dip\", \"file\": \"related_work.tex\", \"line\": 5, \"command\": \"cite\"}, {\"key\": \"liu2023dejavu\", \"file\": \"related_work.tex\", \"line\": 9, \"command\": \"cite\"}, {\"key\": \"akhauri2024shadowllm\", \"file\": \"related_work.tex\", \"line\": 10, \"command\": \"cite\"}, {\"key\": \"gautam2026fastforward\", \"file\": \"related_work.tex\", \"line\": 11, \"command\": \"cite\"}, {\"key\": \"song2024powerinfer\", \"file\": \"related_work.tex\", \"line\": 12, \"command\": \"cite\"}, {\"key\": \"fang2024maskllm\", \"file\": \"related_work.tex\", \"line\": 13, \"command\": \"cite\"}, {\"key\": \"xu2026spon\", \"file\": \"related_work.tex\", \"line\": 19, \"command\": \"cite\"}, {\"key\": \"mirzadeh2024relu\", \"file\": \"related_work.tex\", \"line\": 24, \"command\": \"cite\"}, {\"key\": \"song2024turbosparse\", \"file\": \"related_work.tex\", \"line\": 24, \"command\": \"cite\"}, {\"key\": \"song2025prosparse\", \"file\": \"related_work.tex\", \"line\": 24, \"command\": \"cite\"}, {\"key\": \"luo2024sparsinglaw\", \"file\": \"related_work.tex\", \"line\": 24, \"command\": \"cite\"}, {\"key\": \"muralidharan2024minitron\", \"file\": \"related_work.tex\", \"line\": 25, \"command\": \"cite\"}, {\"key\": \"sun2024wanda\", \"file\": \"related_work.tex\", \"line\": 29, \"command\": \"cite\"}, {\"key\": \"frantar2023sparsegpt\", \"file\": \"related_work.tex\", \"line\": 29, \"command\": \"cite\"}, {\"key\": \"fedus2022switch\", \"file\": \"related_work.tex\", \"line\": 29, \"command\": \"cite\"}, {\"key\": \"kim2016sequencekd\", \"file\": \"related_work.tex\", \"line\": 31, \"command\": \"cite\"}, {\"key\": \"sanh2019distilbert\", \"file\": \"related_work.tex\", \"line\": 31, \"command\": \"cite\"}, {\"key\": \"maddison2017concrete\", \"file\": \"related_work.tex\", \"line\": 32, \"command\": \"cite\"}, {\"key\": \"louizos2018l0\", \"file\": \"related_work.tex\", \"line\": 32, \"command\": \"cite\"}, {\"key\": \"shazeer2020glu\", \"file\": \"method.tex\", \"line\": 10, \"command\": \"cite\"}, {\"key\": \"liu2025teal\", \"file\": \"method.tex\", \"line\": 26, \"command\": \"cite\"}, {\"key\": \"jang2017gumbel\", \"file\": \"method.tex\", \"line\": 49, \"command\": \"cite\"}, {\"key\": \"bengio2013ste\", \"file\": \"method.tex\", \"line\": 62, \"command\": \"cite\"}, {\"key\": \"hinton2015distilling\", \"file\": \"method.tex\", \"line\": 80, \"command\": \"cite\"}, {\"key\": \"xu2026spon\", \"file\": \"method.tex\", \"line\": 177, \"command\": \"cite\"}, {\"key\": \"akhauri2024shadowllm\", \"file\": \"method.tex\", \"line\": 178, \"command\": \"cite\"}, {\"key\": \"gautam2026fastforward\", \"file\": \"method.tex\", \"line\": 179, \"command\": \"cite\"}, {\"key\": \"liu2023dejavu\", \"file\": \"method.tex\", \"line\": 179, \"command\": \"cite\"}, {\"key\": \"xu2026spon\", \"file\": \"method.tex\", \"line\": 186, \"command\": \"cite\"}, {\"key\": \"gautam2026fastforward\", \"file\": \"method.tex\", \"line\": 187, \"command\": \"cite\"}, {\"key\": \"grattafiori2024llama3\", \"file\": \"experiments.tex\", \"line\": 7, \"command\": \"cite\"}, {\"key\": \"shazeer2020glu\", \"file\": \"experiments.tex\", \"line\": 7, \"command\": \"cite\"}, {\"key\": \"loshchilov2019adamw\", \"file\": \"experiments.tex\", \"line\": 11, \"command\": \"cite\"}, {\"key\": \"jang2017gumbel\", \"file\": \"experiments.tex\", \"line\": 12, \"command\": \"cite\"}, {\"key\": \"merity2017pointer\", \"file\": \"experiments.tex\", \"line\": 15, \"command\": \"cite\"}, {\"key\": \"liu2025teal\", \"file\": \"experiments.tex\", \"line\": 18, \"command\": \"cite\"}, {\"key\": \"liu2025teal\", \"file\": \"experiments.tex\", \"line\": 22, \"command\": \"cite\"}, {\"key\": \"liu2025teal\", \"file\": \"experiments.tex\", \"line\": 22, \"command\": \"cite\"}, {\"key\": \"bengio2013ste\", \"file\": \"experiments.tex\", \"line\": 97, \"command\": \"cite\"}, {\"key\": \"xu2026spon\", \"file\": \"experiments.tex\", \"line\": 103, \"command\": \"cite\"}, {\"key\": \"jiang2023mistral\", \"file\": \"experiments.tex\", \"line\": 199, \"command\": \"cite\"}, {\"key\": \"raffel2020c4\", \"file\": \"appendix.tex\", \"line\": 153, \"command\": \"cite\"}], \"online_verification\": [{\"key\": \"fang2024maskllm\", \"title\": \"MaskLLM: Learnable Semi-Structured Sparsity for Large Language Models\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"MaskLLM: Learnable Semi-Structured Sparsity for Large Language Models\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"xu2026spon\", \"title\": \"Resting Neurons, Active Insights: Robustify Activation Sparsity for Large Language Models\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Resting Neurons, Active Insights: Robustify Activation Sparsity for Large Language Models\", \"matched_year\": \"2025\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"muralidharan2024minitron\", \"title\": \"Compact Language Models via Pruning and Knowledge Distillation\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Compact Language Models via Pruning and Knowledge Distillation\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"gautam2026fastforward\", \"title\": \"Fast Forward: Accelerating LLM Prefill with Predictive FFN Sparsity\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Fast Forward: Accelerating LLM Prefill with Predictive FFN Sparsity\", \"matched_year\": \"2026\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"liu2025teal\", \"title\": \"Training-Free Activation Sparsity in Large Language Models\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Training-Free Activation Sparsity in Large Language Models\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"liu2023dejavu\", \"title\": \"Deja Vu: Contextual Sparsity for Efficient LLMs at Inference Time\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Deja Vu: Contextual Sparsity for Efficient LLMs at Inference Time\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"akhauri2024shadowllm\", \"title\": \"ShadowLLM: Predictor-based Contextual Sparsity for Large Language Models\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"ShadowLLM: Predictor-based Contextual Sparsity for Large Language Models\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"lee2024cats\", \"title\": \"CATS: Contextually-Aware Thresholding for Sparsity in Large Language Models\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"CATS: Contextually-Aware Thresholding for Sparsity in Large Language Models\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"zhang2025rsparse\", \"title\": \"R-Sparse: Rank-Aware Activation Sparsity for Efficient LLM Inference\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"R-Sparse: Rank-Aware Activation Sparsity for Efficient LLM Inference\", \"matched_year\": \"2025\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"federici2025dip\", \"title\": \"Efficient LLM Inference using Dynamic Input Pruning and Cache-Aware Masking\", \"status\": \"verified\", \"confidence\": 0.893, \"matched_title\": \"Code Artifact for Efficient LLM Inference using Dynamic Input Pruning and Cache-Aware Masking\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"mirzadeh2024relu\", \"title\": \"ReLU Strikes Back: Exploiting Activation Sparsity in Large Language Models\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"ReLU Strikes Back: Exploiting Activation Sparsity in Large Language Models\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"song2024turbosparse\", \"title\": \"Turbo Sparse: Achieving LLM SOTA Performance with Minimal Activated Parameters\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Turbo Sparse: Achieving LLM SOTA Performance with Minimal Activated Parameters\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"song2025prosparse\", \"title\": \"ProSparse: Introducing and Enhancing Intrinsic Activation Sparsity within Large Language Models\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"ProSparse: Introducing and Enhancing Intrinsic Activation Sparsity within Large Language Models\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"luo2024sparsinglaw\", \"title\": \"Sparsing Law: Towards Large Language Models with Greater Activation Sparsity\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Sparsing Law: Towards Large Language Models with Greater Activation Sparsity\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"song2024powerinfer\", \"title\": \"PowerInfer: Fast Large Language Model Serving with a Consumer-grade GPU\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"PowerInfer: Fast Large Language Model Serving with a Consumer-grade GPU\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"kim2016sequencekd\", \"title\": \"Sequence-Level Knowledge Distillation\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Sequence-Level Knowledge Distillation\", \"matched_year\": \"2016\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"sanh2019distilbert\", \"title\": \"DistilBERT, a distilled version of BERT: smaller, faster, cheaper and lighter\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"DistilBERT, a distilled version of BERT: smaller, faster, cheaper and lighter\", \"matched_year\": \"2019\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"sun2024wanda\", \"title\": \"A Simple and Effective Pruning Approach for Large Language Models\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"A Simple and Effective Pruning Approach for Large Language Models\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"frantar2023sparsegpt\", \"title\": \"SparseGPT: Massive Language Models Can Be Accurately Pruned in One-Shot\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"SparseGPT: Massive Language Models Can Be Accurately Pruned in One-Shot\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"fedus2022switch\", \"title\": \"Switch Transformers: Scaling to Trillion Parameter Models with Simple and Efficient Sparsity\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Switch Transformers: Scaling to Trillion Parameter Models with Simple and Efficient Sparsity\", \"matched_year\": \"2021\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"louizos2018l0\", \"title\": \"Learning Sparse Neural Networks through $L_0$ Regularization\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Learning Sparse Neural Networks through $L_0$ Regularization\", \"matched_year\": \"2017\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"maddison2017concrete\", \"title\": \"The Concrete Distribution: A Continuous Relaxation of Discrete Random Variables\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"The Concrete Distribution: A Continuous Relaxation of Discrete Random Variables\", \"matched_year\": \"2016\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"grattafiori2024llama3\", \"title\": \"The Llama 3 Herd of Models\", \"status\": \"mismatch\", \"confidence\": 1.0, \"matched_title\": \"The Llama 3 herd of models\", \"matched_year\": \"2025\", \"mismatch_fields\": [\"first_author: bib=grattafiori vs api=aaron\"], \"note\": \"\"}, {\"key\": \"jiang2023mistral\", \"title\": \"Mistral 7B\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Mistral 7B\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"jang2017gumbel\", \"title\": \"Categorical Reparameterization with Gumbel-Softmax\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Categorical Reparameterization with Gumbel-Softmax\", \"matched_year\": \"2016\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"shazeer2020glu\", \"title\": \"GLU Variants Improve Transformer\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"GLU Variants Improve Transformer\", \"matched_year\": \"2020\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"merity2017pointer\", \"title\": \"Pointer Sentinel Mixture Models\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Pointer Sentinel Mixture Models\", \"matched_year\": \"2016\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"hinton2015distilling\", \"title\": \"Distilling the Knowledge in a Neural Network\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Distilling the Knowledge in a Neural Network\", \"matched_year\": \"2015\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"bengio2013ste\", \"title\": \"Estimating or Propagating Gradients Through Stochastic Neurons for Conditional Computation\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Estimating or Propagating Gradients Through Stochastic Neurons for Conditional Computation\", \"matched_year\": \"2013\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"loshchilov2019adamw\", \"title\": \"Decoupled Weight Decay Regularization\", \"status\": \"mismatch\", \"confidence\": 1.0, \"matched_title\": \"Decoupled Weight Decay Regularization\", \"matched_year\": \"2017\", \"mismatch_fields\": [\"year: bib=2019 vs api=2017\"], \"note\": \"\"}, {\"key\": \"raffel2020c4\", \"title\": \"Exploring the Limits of Transfer Learning with a Unified Text-to-Text Transformer\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Exploring the Limits of Transfer Learning with a Unified Text-to-Text Transformer\", \"matched_year\": \"2019\", \"mismatch_fields\": [], \"note\": \"\"}]}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a230e0b6-9b98-4a62-96aa-71199069e522",
  "isSidechain": false,
  "promptId": "e22b3aa5-f147-4b55-a02c-533b2c761d41",
  "type": "user",
  "uuid": "638fe4c5-be94-4dfe-ad60-9d095396a7dd",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"summary\\\": {\\\"total_bib_entries\\\": 31, \\\"total_citations\\\": 58, \\\"unique_cited_keys\\\": 31, \\\"orphan_bib\\\": 0, \\\"missing_bib\\\": 0, \\\"duplicate_keys\\\": 0, \\\"online_verified\\\": 29, \\\"online_not_found\\\": 0, \\\"online_mismatch\\\": 2}, \\\"cross_check\\\": {\\\"orphan_bib\\\": [], \\\"missing_bib\\\": [], \\\"orphan_count\\\": 0, \\\"missing_count\\\": 0}, \\\"bib_entries\\\": [{\\\"key\\\": \\\"fang2024maskllm\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"MaskLLM: Learnable Semi-Structured Sparsity for Large Language Models\\\", \\\"authors\\\": \\\"Gongfan Fang and Hongxu Yin and Saurav Muralidharan and Greg Heinrich and Jeff P...\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"Advances in Neural Information Processing Systems (NeurIPS)\\\"}, {\\\"key\\\": \\\"xu2026spon\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Resting Neurons, Active Insights: Robustify Activation Sparsity for Large Language Models\\\", \\\"authors\\\": \\\"Haotian Xu and Jiannan Yang and Tian Gao and Tsui-Wei Weng and Tengfei Ma\\\", \\\"year\\\": \\\"2026\\\", \\\"venue\\\": \\\"Proceedings of the International Conference on Machine Learning (ICML)\\\"}, {\\\"key\\\": \\\"muralidharan2024minitron\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Compact Language Models via Pruning and Knowledge Distillation\\\", \\\"authors\\\": \\\"Saurav Muralidharan and Sharath Turuvekere Sreenivas and Raviraj Joshi and Marci...\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"Advances in Neural Information Processing Systems (NeurIPS)\\\"}, {\\\"key\\\": \\\"gautam2026fastforward\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Fast Forward: Accelerating LLM Prefill with Predictive FFN Sparsity\\\", \\\"authors\\\": \\\"Aayush Gautam and Mukul Gagrani and Junyoung Park and Mingu Lee and Chiris Lott ...\\\", \\\"year\\\": \\\"2026\\\", \\\"venue\\\": \\\"arXiv preprint arXiv:2602.00397\\\"}, {\\\"key\\\": \\\"liu2025teal\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Training-Free Activation Sparsity in Large Language Models\\\", \\\"authors\\\": \\\"James Liu and Pragaash Ponnusamy and Tianle Cai and Han Guo and Yoon Kim and Ben...\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"Proceedings of the International Conference on Learning Representations (ICLR)\\\"}, {\\\"key\\\": \\\"liu2023dejavu\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Deja Vu: Contextual Sparsity for Efficient LLMs at Inference Time\\\", \\\"authors\\\": \\\"Zichang Liu and Jue Wang and Tri Dao and Tianyi Zhou and Binhang Yuan and Zhao S...\\\", \\\"year\\\": \\\"2023\\\", \\\"venue\\\": \\\"Proceedings of the International Conference on Machine Learning (ICML)\\\"}, {\\\"key\\\": \\\"akhauri2024shadowllm\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"ShadowLLM: Predictor-based Contextual Sparsity for Large Language Models\\\", \\\"authors\\\": \\\"Yash Akhauri and Ahmed F AbouElhamayed and Jordan Dotzel and Zhiru Zhang and Ale...\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"Proceedings of the Conference on Empirical Methods in Natural Language Processin...\\\"}, {\\\"key\\\": \\\"lee2024cats\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"CATS: Contextually-Aware Thresholding for Sparsity in Large Language Models\\\", \\\"authors\\\": \\\"Donghyun Lee and Je-Yong Lee and Genghan Zhang and Mo Tiwari and Azalia Mirhosei...\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"arXiv preprint arXiv:2404.08763\\\"}, {\\\"key\\\": \\\"zhang2025rsparse\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"R-Sparse: Rank-Aware Activation Sparsity for Efficient LLM Inference\\\", \\\"authors\\\": \\\"Zhenyu Zhang and Zechun Liu and Yuandong Tian and Harshit Khaitan and Zhangyang ...\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"Proceedings of the International Conference on Learning Representations (ICLR)\\\"}, {\\\"key\\\": \\\"federici2025dip\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Efficient LLM Inference using Dynamic Input Pruning and Cache-Aware Masking\\\", \\\"authors\\\": \\\"Marco Federici and Davide Belli and Mart van Baalen and Amir Jalalirad and Andri...\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"Proceedings of Machine Learning and Systems (MLSys)\\\"}, {\\\"key\\\": \\\"mirzadeh2024relu\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"ReLU Strikes Back: Exploiting Activation Sparsity in Large Language Models\\\", \\\"authors\\\": \\\"Iman Mirzadeh and Keivan Alizadeh and Sachin Mehta and Carlo C Del Mundo and Onc...\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"Proceedings of the International Conference on Learning Representations (ICLR)\\\"}, {\\\"key\\\": \\\"song2024turbosparse\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Turbo Sparse: Achieving LLM SOTA Performance with Minimal Activated Parameters\\\", \\\"authors\\\": \\\"Yixin Song and Haotong Xie and Zhengyan Zhang and Bo Wen and Li Ma and Zeyu Mi a...\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"arXiv preprint arXiv:2406.05955\\\"}, {\\\"key\\\": \\\"song2025prosparse\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"ProSparse: Introducing and Enhancing Intrinsic Activation Sparsity within Large Language Models\\\", \\\"authors\\\": \\\"Chenyang Song and Xu Han and Zhengyan Zhang and Shengding Hu and Xiyu Shi and Ku...\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"Proceedings of the International Conference on Computational Linguistics (COLING...\\\"}, {\\\"key\\\": \\\"luo2024sparsinglaw\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Sparsing Law: Towards Large Language Models with Greater Activation Sparsity\\\", \\\"authors\\\": \\\"Yuqi Luo and Chenyang Song and Xu Han and Yingfa Chen and Chaojun Xiao and Xiaoj...\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"arXiv preprint arXiv:2411.02335\\\"}, {\\\"key\\\": \\\"song2024powerinfer\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"PowerInfer: Fast Large Language Model Serving with a Consumer-grade GPU\\\", \\\"authors\\\": \\\"Yixin Song and Zeyu Mi and Haotong Xie and Haibo Chen\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"Proceedings of the ACM Symposium on Operating Systems Principles (SOSP)\\\"}, {\\\"key\\\": \\\"kim2016sequencekd\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Sequence-Level Knowledge Distillation\\\", \\\"authors\\\": \\\"Yoon Kim and Alexander M. Rush\\\", \\\"year\\\": \\\"2016\\\", \\\"venue\\\": \\\"Proceedings of the Conference on Empirical Methods in Natural Language Processin...\\\"}, {\\\"key\\\": \\\"sanh2019distilbert\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"DistilBERT, a distilled version of BERT: smaller, faster, cheaper and lighter\\\", \\\"authors\\\": \\\"Victor Sanh and Lysandre Debut and Julien Chaumond and Thomas Wolf\\\", \\\"year\\\": \\\"2019\\\", \\\"venue\\\": \\\"arXiv preprint arXiv:1910.01108\\\"}, {\\\"key\\\": \\\"sun2024wanda\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"A Simple and Effective Pruning Approach for Large Language Models\\\", \\\"authors\\\": \\\"Mingjie Sun and Zhuang Liu and Anna Bair and J. Zico Kolter\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"Proceedings of the International Conference on Learning Representations (ICLR)\\\"}, {\\\"key\\\": \\\"frantar2023sparsegpt\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"SparseGPT: Massive Language Models Can Be Accurately Pruned in One-Shot\\\", \\\"authors\\\": \\\"Elias Frantar and Dan Alistarh\\\", \\\"year\\\": \\\"2023\\\", \\\"venue\\\": \\\"Proceedings of the International Conference on Machine Learning (ICML)\\\"}, {\\\"key\\\": \\\"fedus2022switch\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Switch Transformers: Scaling to Trillion Parameter Models with Simple and Efficient Sparsity\\\", \\\"authors\\\": \\\"William Fedus and Barret Zoph and Noam Shazeer\\\", \\\"year\\\": \\\"2022\\\", \\\"venue\\\": \\\"Journal of Machine Learning Research\\\"}, {\\\"key\\\": \\\"louizos2018l0\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Learning Sparse Neural Networks through $L_0$ Regularization\\\", \\\"authors\\\": \\\"Christos Louizos and Max Welling and Diederik P. Kingma\\\", \\\"year\\\": \\\"2018\\\", \\\"venue\\\": \\\"Proceedings of the International Conference on Learning Representations (ICLR)\\\"}, {\\\"key\\\": \\\"maddison2017concrete\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"The Concrete Distribution: A Continuous Relaxation of Discrete Random Variables\\\", \\\"authors\\\": \\\"Chris J. Maddison and Andriy Mnih and Yee Whye Teh\\\", \\\"year\\\": \\\"2017\\\", \\\"venue\\\": \\\"Proceedings of the International Conference on Learning Representations (ICLR)\\\"}, {\\\"key\\\": \\\"grattafiori2024llama3\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"The Llama 3 Herd of Models\\\", \\\"authors\\\": \\\"Aaron Grattafiori and Abhimanyu Dubey and Abhinav Jauhri and Abhinav Pandey and ...\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"arXiv preprint arXiv:2407.21783\\\"}, {\\\"key\\\": \\\"jiang2023mistral\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Mistral 7B\\\", \\\"authors\\\": \\\"Albert Q. Jiang and Alexandre Sablayrolles and Arthur Mensch and Chris Bamford a...\\\", \\\"year\\\": \\\"2023\\\", \\\"venue\\\": \\\"arXiv preprint arXiv:2310.06825\\\"}, {\\\"key\\\": \\\"jang2017gumbel\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Categorical Reparameterization with Gumbel-Softmax\\\", \\\"authors\\\": \\\"Eric Jang and Shixiang Gu and Ben Poole\\\", \\\"year\\\": \\\"2017\\\", \\\"venue\\\": \\\"Proceedings of the International Conference on Learning Representations (ICLR)\\\"}, {\\\"key\\\": \\\"shazeer2020glu\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"GLU Variants Improve Transformer\\\", \\\"authors\\\": \\\"Noam Shazeer\\\", \\\"year\\\": \\\"2020\\\", \\\"venue\\\": \\\"arXiv preprint arXiv:2002.05202\\\"}, {\\\"key\\\": \\\"merity2017pointer\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Pointer Sentinel Mixture Models\\\", \\\"authors\\\": \\\"Stephen Merity and Caiming Xiong and James Bradbury and Richard Socher\\\", \\\"year\\\": \\\"2017\\\", \\\"venue\\\": \\\"Proceedings of the International Conference on Learning Representations (ICLR)\\\"}, {\\\"key\\\": \\\"hinton2015distilling\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Distilling the Knowledge in a Neural Network\\\", \\\"authors\\\": \\\"Geoffrey Hinton and Oriol Vinyals and Jeff Dean\\\", \\\"year\\\": \\\"2015\\\", \\\"venue\\\": \\\"NeurIPS 2014 Deep Learning Workshop\\\"}, {\\\"key\\\": \\\"bengio2013ste\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Estimating or Propagating Gradients Through Stochastic Neurons for Conditional Computation\\\", \\\"authors\\\": \\\"Yoshua Bengio and Nicholas L\\\\\\\\'eonard and Aaron Courville\\\", \\\"year\\\": \\\"2013\\\", \\\"venue\\\": \\\"arXiv preprint arXiv:1308.3432\\\"}, {\\\"key\\\": \\\"loshchilov2019adamw\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Decoupled Weight Decay Regularization\\\", \\\"authors\\\": \\\"Ilya Loshchilov and Frank Hutter\\\", \\\"year\\\": \\\"2019\\\", \\\"venue\\\": \\\"Proceedings of the International Conference on Learning Representations (ICLR)\\\"}, {\\\"key\\\": \\\"raffel2020c4\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Exploring the Limits of Transfer Learning with a Unified Text-to-Text Transformer\\\", \\\"authors\\\": \\\"Colin Raffel and Noam Shazeer and Adam Roberts and Katherine Lee and Sharan Nara...\\\", \\\"year\\\": \\\"2020\\\", \\\"venue\\\": \\\"Journal of Machine Learning Research\\\"}], \\\"tex_citations\\\": [{\\\"key\\\": \\\"shazeer2020glu\\\", \\\"file\\\": \\\"introduction.tex\\\", \\\"line\\\": 3, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"liu2025teal\\\", \\\"file\\\": \\\"introduction.tex\\\", \\\"line\\\": 6, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"grattafiori2024llama3\\\", \\\"file\\\": \\\"introduction.tex\\\", \\\"line\\\": 6, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"liu2023dejavu\\\", \\\"file\\\": \\\"introduction.tex\\\", \\\"line\\\": 7, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"gautam2026fastforward\\\", \\\"file\\\": \\\"introduction.tex\\\", \\\"line\\\": 7, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"liu2025teal\\\", \\\"file\\\": \\\"introduction.tex\\\", \\\"line\\\": 14, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"jang2017gumbel\\\", \\\"file\\\": \\\"introduction.tex\\\", \\\"line\\\": 27, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"jiang2023mistral\\\", \\\"file\\\": \\\"introduction.tex\\\", \\\"line\\\": 34, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"xu2026spon\\\", \\\"file\\\": \\\"introduction.tex\\\", \\\"line\\\": 35, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"xu2026spon\\\", \\\"file\\\": \\\"introduction.tex\\\", \\\"line\\\": 38, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"akhauri2024shadowllm\\\", \\\"file\\\": \\\"introduction.tex\\\", \\\"line\\\": 38, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"gautam2026fastforward\\\", \\\"file\\\": \\\"introduction.tex\\\", \\\"line\\\": 38, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"liu2023dejavu\\\", \\\"file\\\": \\\"introduction.tex\\\", \\\"line\\\": 38, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"liu2025teal\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 4, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"lee2024cats\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 5, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"zhang2025rsparse\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 5, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"federici2025dip\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 5, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"liu2023dejavu\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 9, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"akhauri2024shadowllm\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 10, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"gautam2026fastforward\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 11, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"song2024powerinfer\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 12, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"fang2024maskllm\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 13, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"xu2026spon\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 19, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"mirzadeh2024relu\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 24, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"song2024turbosparse\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 24, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"song2025prosparse\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 24, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"luo2024sparsinglaw\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 24, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"muralidharan2024minitron\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 25, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"sun2024wanda\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 29, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"frantar2023sparsegpt\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 29, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"fedus2022switch\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 29, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"kim2016sequencekd\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 31, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"sanh2019distilbert\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 31, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"maddison2017concrete\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 32, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"louizos2018l0\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 32, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"shazeer2020glu\\\", \\\"file\\\": \\\"method.tex\\\", \\\"line\\\": 10, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"liu2025teal\\\", \\\"file\\\": \\\"method.tex\\\", \\\"line\\\": 26, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"jang2017gumbel\\\", \\\"file\\\": \\\"method.tex\\\", \\\"line\\\": 49, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"bengio2013ste\\\", \\\"file\\\": \\\"method.tex\\\", \\\"line\\\": 62, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"hinton2015distilling\\\", \\\"file\\\": \\\"method.tex\\\", \\\"line\\\": 80, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"xu2026spon\\\", \\\"file\\\": \\\"method.tex\\\", \\\"line\\\": 177, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"akhauri2024shadowllm\\\", \\\"file\\\": \\\"method.tex\\\", \\\"line\\\": 178, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"gautam2026fastforward\\\", \\\"file\\\": \\\"method.tex\\\", \\\"line\\\": 179, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"liu2023dejavu\\\", \\\"file\\\": \\\"method.tex\\\", \\\"line\\\": 179, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"xu2026spon\\\", \\\"file\\\": \\\"method.tex\\\", \\\"line\\\": 186, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"gautam2026fastforward\\\", \\\"file\\\": \\\"method.tex\\\", \\\"line\\\": 187, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"grattafiori2024llama3\\\", \\\"file\\\": \\\"experiments.tex\\\", \\\"line\\\": 7, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"shazeer2020glu\\\", \\\"file\\\": \\\"experiments.tex\\\", \\\"line\\\": 7, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"loshchilov2019adamw\\\", \\\"file\\\": \\\"experiments.tex\\\", \\\"line\\\": 11, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"jang2017gumbel\\\", \\\"file\\\": \\\"experiments.tex\\\", \\\"line\\\": 12, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"merity2017pointer\\\", \\\"file\\\": \\\"experiments.tex\\\", \\\"line\\\": 15, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"liu2025teal\\\", \\\"file\\\": \\\"experiments.tex\\\", \\\"line\\\": 18, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"liu2025teal\\\", \\\"file\\\": \\\"experiments.tex\\\", \\\"line\\\": 22, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"liu2025teal\\\", \\\"file\\\": \\\"experiments.tex\\\", \\\"line\\\": 22, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"bengio2013ste\\\", \\\"file\\\": \\\"experiments.tex\\\", \\\"line\\\": 97, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"xu2026spon\\\", \\\"file\\\": \\\"experiments.tex\\\", \\\"line\\\": 103, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"jiang2023mistral\\\", \\\"file\\\": \\\"experiments.tex\\\", \\\"line\\\": 199, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"raffel2020c4\\\", \\\"file\\\": \\\"appendix.tex\\\", \\\"line\\\": 153, \\\"command\\\": \\\"cite\\\"}], \\\"online_verification\\\": [{\\\"key\\\": \\\"fang2024maskllm\\\", \\\"title\\\": \\\"MaskLLM: Learnable Semi-Structured Sparsity for Large Language Models\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"MaskLLM: Learnable Semi-Structured Sparsity for Large Language Models\\\", \\\"matched_year\\\": \\\"2024\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"xu2026spon\\\", \\\"title\\\": \\\"Resting Neurons, Active Insights: Robustify Activation Sparsity for Large Language Models\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Resting Neurons, Active Insights: Robustify Activation Sparsity for Large Language Models\\\", \\\"matched_year\\\": \\\"2025\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"muralidharan2024minitron\\\", \\\"title\\\": \\\"Compact Language Models via Pruning and Knowledge Distillation\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Compact Language Models via Pruning and Knowledge Distillation\\\", \\\"matched_year\\\": \\\"2024\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"gautam2026fastforward\\\", \\\"title\\\": \\\"Fast Forward: Accelerating LLM Prefill with Predictive FFN Sparsity\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Fast Forward: Accelerating LLM Prefill with Predictive FFN Sparsity\\\", \\\"matched_year\\\": \\\"2026\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"liu2025teal\\\", \\\"title\\\": \\\"Training-Free Activation Sparsity in Large Language Models\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Training-Free Activation Sparsity in Large Language Models\\\", \\\"matched_year\\\": \\\"2024\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"liu2023dejavu\\\", \\\"title\\\": \\\"Deja Vu: Contextual Sparsity for Efficient LLMs at Inference Time\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Deja Vu: Contextual Sparsity for Efficient LLMs at Inference Time\\\", \\\"matched_year\\\": \\\"2023\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"akhauri2024shadowllm\\\", \\\"title\\\": \\\"ShadowLLM: Predictor-based Contextual Sparsity for Large Language Models\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"ShadowLLM: Predictor-based Contextual Sparsity for Large Language Models\\\", \\\"matched_year\\\": \\\"2024\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"lee2024cats\\\", \\\"title\\\": \\\"CATS: Contextually-Aware Thresholding for Sparsity in Large Language Models\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"CATS: Contextually-Aware Thresholding for Sparsity in Large Language Models\\\", \\\"matched_year\\\": \\\"2024\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"zhang2025rsparse\\\", \\\"title\\\": \\\"R-Sparse: Rank-Aware Activation Sparsity for Efficient LLM Inference\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"R-Sparse: Rank-Aware Activation Sparsity for Efficient LLM Inference\\\", \\\"matched_year\\\": \\\"2025\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"federici2025dip\\\", \\\"title\\\": \\\"Efficient LLM Inference using Dynamic Input Pruning and Cache-Aware Masking\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 0.893, \\\"matched_title\\\": \\\"Code Artifact for Efficient LLM Inference using Dynamic Input Pruning and Cache-Aware Masking\\\", \\\"matched_year\\\": \\\"2024\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"mirzadeh2024relu\\\", \\\"title\\\": \\\"ReLU Strikes Back: Exploiting Activation Sparsity in Large Language Models\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"ReLU Strikes Back: Exploiting Activation Sparsity in Large Language Models\\\", \\\"matched_year\\\": \\\"2023\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"song2024turbosparse\\\", \\\"title\\\": \\\"Turbo Sparse: Achieving LLM SOTA Performance with Minimal Activated Parameters\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Turbo Sparse: Achieving LLM SOTA Performance with Minimal Activated Parameters\\\", \\\"matched_year\\\": \\\"2024\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"song2025prosparse\\\", \\\"title\\\": \\\"ProSparse: Introducing and Enhancing Intrinsic Activation Sparsity within Large Language Models\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"ProSparse: Introducing and Enhancing Intrinsic Activation Sparsity within Large Language Models\\\", \\\"matched_year\\\": \\\"2024\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"luo2024sparsinglaw\\\", \\\"title\\\": \\\"Sparsing Law: Towards Large Language Models with Greater Activation Sparsity\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Sparsing Law: Towards Large Language Models with Greater Activation Sparsity\\\", \\\"matched_year\\\": \\\"2024\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"song2024powerinfer\\\", \\\"title\\\": \\\"PowerInfer: Fast Large Language Model Serving with a Consumer-grade GPU\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"PowerInfer: Fast Large Language Model Serving with a Consumer-grade GPU\\\", \\\"matched_year\\\": \\\"2024\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"kim2016sequencekd\\\", \\\"title\\\": \\\"Sequence-Level Knowledge Distillation\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Sequence-Level Knowledge Distillation\\\", \\\"matched_year\\\": \\\"2016\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"sanh2019distilbert\\\", \\\"title\\\": \\\"DistilBERT, a distilled version of BERT: smaller, faster, cheaper and lighter\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"DistilBERT, a distilled version of BERT: smaller, faster, cheaper and lighter\\\", \\\"matched_year\\\": \\\"2019\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"sun2024wanda\\\", \\\"title\\\": \\\"A Simple and Effective Pruning Approach for Large Language Models\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"A Simple and Effective Pruning Approach for Large Language Models\\\", \\\"matched_year\\\": \\\"2023\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"frantar2023sparsegpt\\\", \\\"title\\\": \\\"SparseGPT: Massive Language Models Can Be Accurately Pruned in One-Shot\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"SparseGPT: Massive Language Models Can Be Accurately Pruned in One-Shot\\\", \\\"matched_year\\\": \\\"2023\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"fedus2022switch\\\", \\\"title\\\": \\\"Switch Transformers: Scaling to Trillion Parameter Models with Simple and Efficient Sparsity\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Switch Transformers: Scaling to Trillion Parameter Models with Simple and Efficient Sparsity\\\", \\\"matched_year\\\": \\\"2021\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"louizos2018l0\\\", \\\"title\\\": \\\"Learning Sparse Neural Networks through $L_0$ Regularization\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Learning Sparse Neural Networks through $L_0$ Regularization\\\", \\\"matched_year\\\": \\\"2017\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"maddison2017concrete\\\", \\\"title\\\": \\\"The Concrete Distribution: A Continuous Relaxation of Discrete Random Variables\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"The Concrete Distribution: A Continuous Relaxation of Discrete Random Variables\\\", \\\"matched_year\\\": \\\"2016\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"grattafiori2024llama3\\\", \\\"title\\\": \\\"The Llama 3 Herd of Models\\\", \\\"status\\\": \\\"mismatch\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"The Llama 3 herd of models\\\", \\\"matched_year\\\": \\\"2025\\\", \\\"mismatch_fields\\\": [\\\"first_author: bib=grattafiori vs api=aaron\\\"], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"jiang2023mistral\\\", \\\"title\\\": \\\"Mistral 7B\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Mistral 7B\\\", \\\"matched_year\\\": \\\"2023\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"jang2017gumbel\\\", \\\"title\\\": \\\"Categorical Reparameterization with Gumbel-Softmax\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Categorical Reparameterization with Gumbel-Softmax\\\", \\\"matched_year\\\": \\\"2016\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"shazeer2020glu\\\", \\\"title\\\": \\\"GLU Variants Improve Transformer\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"GLU Variants Improve Transformer\\\", \\\"matched_year\\\": \\\"2020\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"merity2017pointer\\\", \\\"title\\\": \\\"Pointer Sentinel Mixture Models\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Pointer Sentinel Mixture Models\\\", \\\"matched_year\\\": \\\"2016\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"hinton2015distilling\\\", \\\"title\\\": \\\"Distilling the Knowledge in a Neural Network\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Distilling the Knowledge in a Neural Network\\\", \\\"matched_year\\\": \\\"2015\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"bengio2013ste\\\", \\\"title\\\": \\\"Estimating or Propagating Gradients Through Stochastic Neurons for Conditional Computation\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Estimating or Propagating Gradients Through Stochastic Neurons for Conditional Computation\\\", \\\"matched_year\\\": \\\"2013\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"loshchilov2019adamw\\\", \\\"title\\\": \\\"Decoupled Weight Decay Regularization\\\", \\\"status\\\": \\\"mismatch\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Decoupled Weight Decay Regularization\\\", \\\"matched_year\\\": \\\"2017\\\", \\\"mismatch_fields\\\": [\\\"year: bib=2019 vs api=2017\\\"], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"raffel2020c4\\\", \\\"title\\\": \\\"Exploring the Limits of Transfer Learning with a Unified Text-to-Text Transformer\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Exploring the Limits of Transfer Learning with a Unified Text-to-Text Transformer\\\", \\\"matched_year\\\": \\\"2019\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}]}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"summary\": {\"total_bib_entries\": 31, \"total_citations\": 58, \"unique_cited_keys\": 31, \"orphan_bib\": 0, \"missing_bib\": 0, \"duplicate_keys\": 0, \"online_verified\": 29, \"online_not_found\": 0, \"online_mismatch\": 2}, \"cross_check\": {\"orphan_bib\": [], \"missing_bib\": [], \"orphan_count\": 0, \"missing_count\": 0}, \"bib_entries\": [{\"key\": \"fang2024maskllm\", \"type\": \"inproceedings\", \"title\": \"MaskLLM: Learnable Semi-Structured Sparsity for Large Language Models\", \"authors\": \"Gongfan Fang and Hongxu Yin and Saurav Muralidharan and Greg Heinrich and Jeff P...\", \"year\": \"2024\", \"venue\": \"Advances in Neural Information Processing Systems (NeurIPS)\"}, {\"key\": \"xu2026spon\", \"type\": \"inproceedings\", \"title\": \"Resting Neurons, Active Insights: Robustify Activation Sparsity for Large Language Models\", \"authors\": \"Haotian Xu and Jiannan Yang and Tian Gao and Tsui-Wei Weng and Tengfei Ma\", \"year\": \"2026\", \"venue\": \"Proceedings of the International Conference on Machine Learning (ICML)\"}, {\"key\": \"muralidharan2024minitron\", \"type\": \"inproceedings\", \"title\": \"Compact Language Models via Pruning and Knowledge Distillation\", \"authors\": \"Saurav Muralidharan and Sharath Turuvekere Sreenivas and Raviraj Joshi and Marci...\", \"year\": \"2024\", \"venue\": \"Advances in Neural Information Processing Systems (NeurIPS)\"}, {\"key\": \"gautam2026fastforward\", \"type\": \"article\", \"title\": \"Fast Forward: Accelerating LLM Prefill with Predictive FFN Sparsity\", \"authors\": \"Aayush Gautam and Mukul Gagrani and Junyoung Park and Mingu Lee and Chiris Lott ...\", \"year\": \"2026\", \"venue\": \"arXiv preprint arXiv:2602.00397\"}, {\"key\": \"liu2025teal\", \"type\": \"inproceedings\", \"title\": \"Training-Free Activation Sparsity in Large Language Models\", \"authors\": \"James Liu and Pragaash Ponnusamy and Tianle Cai and Han Guo and Yoon Kim and Ben...\", \"year\": \"2025\", \"venue\": \"Proceedings of the International Conference on Learning Representations (ICLR)\"}, {\"key\": \"liu2023dejavu\", \"type\": \"inproceedings\", \"title\": \"Deja Vu: Contextual Sparsity for Efficient LLMs at Inference Time\", \"authors\": \"Zichang Liu and Jue Wang and Tri Dao and Tianyi Zhou and Binhang Yuan and Zhao S...\", \"year\": \"2023\", \"venue\": \"Proceedings of the International Conference on Machine Learning (ICML)\"}, {\"key\": \"akhauri2024shadowllm\", \"type\": \"inproceedings\", \"title\": \"ShadowLLM: Predictor-based Contextual Sparsity for Large Language Models\", \"authors\": \"Yash Akhauri and Ahmed F AbouElhamayed and Jordan Dotzel and Zhiru Zhang and Ale...\", \"year\": \"2024\", \"venue\": \"Proceedings of the Conference on Empirical Methods in Natural Language Processin...\"}, {\"key\": \"lee2024cats\", \"type\": \"article\", \"title\": \"CATS: Contextually-Aware Thresholding for Sparsity in Large Language Models\", \"authors\": \"Donghyun Lee and Je-Yong Lee and Genghan Zhang and Mo Tiwari and Azalia Mirhosei...\", \"year\": \"2024\", \"venue\": \"arXiv preprint arXiv:2404.08763\"}, {\"key\": \"zhang2025rsparse\", \"type\": \"inproceedings\", \"title\": \"R-Sparse: Rank-Aware Activation Sparsity for Efficient LLM Inference\", \"authors\": \"Zhenyu Zhang and Zechun Liu and Yuandong Tian and Harshit Khaitan and Zhangyang ...\", \"year\": \"2025\", \"venue\": \"Proceedings of the International Conference on Learning Representations (ICLR)\"}, {\"key\": \"federici2025dip\", \"type\": \"inproceedings\", \"title\": \"Efficient LLM Inference using Dynamic Input Pruning and Cache-Aware Masking\", \"authors\": \"Marco Federici and Davide Belli and Mart van Baalen and Amir Jalalirad and Andri...\", \"year\": \"2024\", \"venue\": \"Proceedings of Machine Learning and Systems (MLSys)\"}, {\"key\": \"mirzadeh2024relu\", \"type\": \"inproceedings\", \"title\": \"ReLU Strikes Back: Exploiting Activation Sparsity in Large Language Models\", \"authors\": \"Iman Mirzadeh and Keivan Alizadeh and Sachin Mehta and Carlo C Del Mundo and Onc...\", \"year\": \"2024\", \"venue\": \"Proceedings of the International Conference on Learning Representations (ICLR)\"}, {\"key\": \"song2024turbosparse\", \"type\": \"article\", \"title\": \"Turbo Sparse: Achieving LLM SOTA Performance with Minimal Activated Parameters\", \"authors\": \"Yixin Song and Haotong Xie and Zhengyan Zhang and Bo Wen and Li Ma and Zeyu Mi a...\", \"year\": \"2024\", \"venue\": \"arXiv preprint arXiv:2406.05955\"}, {\"key\": \"song2025prosparse\", \"type\": \"inproceedings\", \"title\": \"ProSparse: Introducing and Enhancing Intrinsic Activation Sparsity within Large Language Models\", \"authors\": \"Chenyang Song and Xu Han and Zhengyan Zhang and Shengding Hu and Xiyu Shi and Ku...\", \"year\": \"2025\", \"venue\": \"Proceedings of the International Conference on Computational Linguistics (COLING...\"}, {\"key\": \"luo2024sparsinglaw\", \"type\": \"article\", \"title\": \"Sparsing Law: Towards Large Language Models with Greater Activation Sparsity\", \"authors\": \"Yuqi Luo and Chenyang Song and Xu Han and Yingfa Chen and Chaojun Xiao and Xiaoj...\", \"year\": \"2024\", \"venue\": \"arXiv preprint arXiv:2411.02335\"}, {\"key\": \"song2024powerinfer\", \"type\": \"inproceedings\", \"title\": \"PowerInfer: Fast Large Language Model Serving with a Consumer-grade GPU\", \"authors\": \"Yixin Song and Zeyu Mi and Haotong Xie and Haibo Chen\", \"year\": \"2024\", \"venue\": \"Proceedings of the ACM Symposium on Operating Systems Principles (SOSP)\"}, {\"key\": \"kim2016sequencekd\", \"type\": \"inproceedings\", \"title\": \"Sequence-Level Knowledge Distillation\", \"authors\": \"Yoon Kim and Alexander M. Rush\", \"year\": \"2016\", \"venue\": \"Proceedings of the Conference on Empirical Methods in Natural Language Processin...\"}, {\"key\": \"sanh2019distilbert\", \"type\": \"article\", \"title\": \"DistilBERT, a distilled version of BERT: smaller, faster, cheaper and lighter\", \"authors\": \"Victor Sanh and Lysandre Debut and Julien Chaumond and Thomas Wolf\", \"year\": \"2019\", \"venue\": \"arXiv preprint arXiv:1910.01108\"}, {\"key\": \"sun2024wanda\", \"type\": \"inproceedings\", \"title\": \"A Simple and Effective Pruning Approach for Large Language Models\", \"authors\": \"Mingjie Sun and Zhuang Liu and Anna Bair and J. Zico Kolter\", \"year\": \"2024\", \"venue\": \"Proceedings of the International Conference on Learning Representations (ICLR)\"}, {\"key\": \"frantar2023sparsegpt\", \"type\": \"inproceedings\", \"title\": \"SparseGPT: Massive Language Models Can Be Accurately Pruned in One-Shot\", \"authors\": \"Elias Frantar and Dan Alistarh\", \"year\": \"2023\", \"venue\": \"Proceedings of the International Conference on Machine Learning (ICML)\"}, {\"key\": \"fedus2022switch\", \"type\": \"article\", \"title\": \"Switch Transformers: Scaling to Trillion Parameter Models with Simple and Efficient Sparsity\", \"authors\": \"William Fedus and Barret Zoph and Noam Shazeer\", \"year\": \"2022\", \"venue\": \"Journal of Machine Learning Research\"}, {\"key\": \"louizos2018l0\", \"type\": \"inproceedings\", \"title\": \"Learning Sparse Neural Networks through $L_0$ Regularization\", \"authors\": \"Christos Louizos and Max Welling and Diederik P. Kingma\", \"year\": \"2018\", \"venue\": \"Proceedings of the International Conference on Learning Representations (ICLR)\"}, {\"key\": \"maddison2017concrete\", \"type\": \"inproceedings\", \"title\": \"The Concrete Distribution: A Continuous Relaxation of Discrete Random Variables\", \"authors\": \"Chris J. Maddison and Andriy Mnih and Yee Whye Teh\", \"year\": \"2017\", \"venue\": \"Proceedings of the International Conference on Learning Representations (ICLR)\"}, {\"key\": \"grattafiori2024llama3\", \"type\": \"article\", \"title\": \"The Llama 3 Herd of Models\", \"authors\": \"Aaron Grattafiori and Abhimanyu Dubey and Abhinav Jauhri and Abhinav Pandey and ...\", \"year\": \"2024\", \"venue\": \"arXiv preprint arXiv:2407.21783\"}, {\"key\": \"jiang2023mistral\", \"type\": \"article\", \"title\": \"Mistral 7B\", \"authors\": \"Albert Q. Jiang and Alexandre Sablayrolles and Arthur Mensch and Chris Bamford a...\", \"year\": \"2023\", \"venue\": \"arXiv preprint arXiv:2310.06825\"}, {\"key\": \"jang2017gumbel\", \"type\": \"inproceedings\", \"title\": \"Categorical Reparameterization with Gumbel-Softmax\", \"authors\": \"Eric Jang and Shixiang Gu and Ben Poole\", \"year\": \"2017\", \"venue\": \"Proceedings of the International Conference on Learning Representations (ICLR)\"}, {\"key\": \"shazeer2020glu\", \"type\": \"article\", \"title\": \"GLU Variants Improve Transformer\", \"authors\": \"Noam Shazeer\", \"year\": \"2020\", \"venue\": \"arXiv preprint arXiv:2002.05202\"}, {\"key\": \"merity2017pointer\", \"type\": \"inproceedings\", \"title\": \"Pointer Sentinel Mixture Models\", \"authors\": \"Stephen Merity and Caiming Xiong and James Bradbury and Richard Socher\", \"year\": \"2017\", \"venue\": \"Proceedings of the International Conference on Learning Representations (ICLR)\"}, {\"key\": \"hinton2015distilling\", \"type\": \"inproceedings\", \"title\": \"Distilling the Knowledge in a Neural Network\", \"authors\": \"Geoffrey Hinton and Oriol Vinyals and Jeff Dean\", \"year\": \"2015\", \"venue\": \"NeurIPS 2014 Deep Learning Workshop\"}, {\"key\": \"bengio2013ste\", \"type\": \"article\", \"title\": \"Estimating or Propagating Gradients Through Stochastic Neurons for Conditional Computation\", \"authors\": \"Yoshua Bengio and Nicholas L\\\\'eonard and Aaron Courville\", \"year\": \"2013\", \"venue\": \"arXiv preprint arXiv:1308.3432\"}, {\"key\": \"loshchilov2019adamw\", \"type\": \"inproceedings\", \"title\": \"Decoupled Weight Decay Regularization\", \"authors\": \"Ilya Loshchilov and Frank Hutter\", \"year\": \"2019\", \"venue\": \"Proceedings of the International Conference on Learning Representations (ICLR)\"}, {\"key\": \"raffel2020c4\", \"type\": \"article\", \"title\": \"Exploring the Limits of Transfer Learning with a Unified Text-to-Text Transformer\", \"authors\": \"Colin Raffel and Noam Shazeer and Adam Roberts and Katherine Lee and Sharan Nara...\", \"year\": \"2020\", \"venue\": \"Journal of Machine Learning Research\"}], \"tex_citations\": [{\"key\": \"shazeer2020glu\", \"file\": \"introduction.tex\", \"line\": 3, \"command\": \"cite\"}, {\"key\": \"liu2025teal\", \"file\": \"introduction.tex\", \"line\": 6, \"command\": \"cite\"}, {\"key\": \"grattafiori2024llama3\", \"file\": \"introduction.tex\", \"line\": 6, \"command\": \"cite\"}, {\"key\": \"liu2023dejavu\", \"file\": \"introduction.tex\", \"line\": 7, \"command\": \"cite\"}, {\"key\": \"gautam2026fastforward\", \"file\": \"introduction.tex\", \"line\": 7, \"command\": \"cite\"}, {\"key\": \"liu2025teal\", \"file\": \"introduction.tex\", \"line\": 14, \"command\": \"cite\"}, {\"key\": \"jang2017gumbel\", \"file\": \"introduction.tex\", \"line\": 27, \"command\": \"cite\"}, {\"key\": \"jiang2023mistral\", \"file\": \"introduction.tex\", \"line\": 34, \"command\": \"cite\"}, {\"key\": \"xu2026spon\", \"file\": \"introduction.tex\", \"line\": 35, \"command\": \"cite\"}, {\"key\": \"xu2026spon\", \"file\": \"introduction.tex\", \"line\": 38, \"command\": \"cite\"}, {\"key\": \"akhauri2024shadowllm\", \"file\": \"introduction.tex\", \"line\": 38, \"command\": \"cite\"}, {\"key\": \"gautam2026fastforward\", \"file\": \"introduction.tex\", \"line\": 38, \"command\": \"cite\"}, {\"key\": \"liu2023dejavu\", \"file\": \"introduction.tex\", \"line\": 38, \"command\": \"cite\"}, {\"key\": \"liu2025teal\", \"file\": \"related_work.tex\", \"line\": 4, \"command\": \"cite\"}, {\"key\": \"lee2024cats\", \"file\": \"related_work.tex\", \"line\": 5, \"command\": \"cite\"}, {\"key\": \"zhang2025rsparse\", \"file\": \"related_work.tex\", \"line\": 5, \"command\": \"cite\"}, {\"key\": \"federici2025dip\", \"file\": \"related_work.tex\", \"line\": 5, \"command\": \"cite\"}, {\"key\": \"liu2023dejavu\", \"file\": \"related_work.tex\", \"line\": 9, \"command\": \"cite\"}, {\"key\": \"akhauri2024shadowllm\", \"file\": \"related_work.tex\", \"line\": 10, \"command\": \"cite\"}, {\"key\": \"gautam2026fastforward\", \"file\": \"related_work.tex\", \"line\": 11, \"command\": \"cite\"}, {\"key\": \"song2024powerinfer\", \"file\": \"related_work.tex\", \"line\": 12, \"command\": \"cite\"}, {\"key\": \"fang2024maskllm\", \"file\": \"related_work.tex\", \"line\": 13, \"command\": \"cite\"}, {\"key\": \"xu2026spon\", \"file\": \"related_work.tex\", \"line\": 19, \"command\": \"cite\"}, {\"key\": \"mirzadeh2024relu\", \"file\": \"related_work.tex\", \"line\": 24, \"command\": \"cite\"}, {\"key\": \"song2024turbosparse\", \"file\": \"related_work.tex\", \"line\": 24, \"command\": \"cite\"}, {\"key\": \"song2025prosparse\", \"file\": \"related_work.tex\", \"line\": 24, \"command\": \"cite\"}, {\"key\": \"luo2024sparsinglaw\", \"file\": \"related_work.tex\", \"line\": 24, \"command\": \"cite\"}, {\"key\": \"muralidharan2024minitron\", \"file\": \"related_work.tex\", \"line\": 25, \"command\": \"cite\"}, {\"key\": \"sun2024wanda\", \"file\": \"related_work.tex\", \"line\": 29, \"command\": \"cite\"}, {\"key\": \"frantar2023sparsegpt\", \"file\": \"related_work.tex\", \"line\": 29, \"command\": \"cite\"}, {\"key\": \"fedus2022switch\", \"file\": \"related_work.tex\", \"line\": 29, \"command\": \"cite\"}, {\"key\": \"kim2016sequencekd\", \"file\": \"related_work.tex\", \"line\": 31, \"command\": \"cite\"}, {\"key\": \"sanh2019distilbert\", \"file\": \"related_work.tex\", \"line\": 31, \"command\": \"cite\"}, {\"key\": \"maddison2017concrete\", \"file\": \"related_work.tex\", \"line\": 32, \"command\": \"cite\"}, {\"key\": \"louizos2018l0\", \"file\": \"related_work.tex\", \"line\": 32, \"command\": \"cite\"}, {\"key\": \"shazeer2020glu\", \"file\": \"method.tex\", \"line\": 10, \"command\": \"cite\"}, {\"key\": \"liu2025teal\", \"file\": \"method.tex\", \"line\": 26, \"command\": \"cite\"}, {\"key\": \"jang2017gumbel\", \"file\": \"method.tex\", \"line\": 49, \"command\": \"cite\"}, {\"key\": \"bengio2013ste\", \"file\": \"method.tex\", \"line\": 62, \"command\": \"cite\"}, {\"key\": \"hinton2015distilling\", \"file\": \"method.tex\", \"line\": 80, \"command\": \"cite\"}, {\"key\": \"xu2026spon\", \"file\": \"method.tex\", \"line\": 177, \"command\": \"cite\"}, {\"key\": \"akhauri2024shadowllm\", \"file\": \"method.tex\", \"line\": 178, \"command\": \"cite\"}, {\"key\": \"gautam2026fastforward\", \"file\": \"method.tex\", \"line\": 179, \"command\": \"cite\"}, {\"key\": \"liu2023dejavu\", \"file\": \"method.tex\", \"line\": 179, \"command\": \"cite\"}, {\"key\": \"xu2026spon\", \"file\": \"method.tex\", \"line\": 186, \"command\": \"cite\"}, {\"key\": \"gautam2026fastforward\", \"file\": \"method.tex\", \"line\": 187, \"command\": \"cite\"}, {\"key\": \"grattafiori2024llama3\", \"file\": \"experiments.tex\", \"line\": 7, \"command\": \"cite\"}, {\"key\": \"shazeer2020glu\", \"file\": \"experiments.tex\", \"line\": 7, \"command\": \"cite\"}, {\"key\": \"loshchilov2019adamw\", \"file\": \"experiments.tex\", \"line\": 11, \"command\": \"cite\"}, {\"key\": \"jang2017gumbel\", \"file\": \"experiments.tex\", \"line\": 12, \"command\": \"cite\"}, {\"key\": \"merity2017pointer\", \"file\": \"experiments.tex\", \"line\": 15, \"command\": \"cite\"}, {\"key\": \"liu2025teal\", \"file\": \"experiments.tex\", \"line\": 18, \"command\": \"cite\"}, {\"key\": \"liu2025teal\", \"file\": \"experiments.tex\", \"line\": 22, \"command\": \"cite\"}, {\"key\": \"liu2025teal\", \"file\": \"experiments.tex\", \"line\": 22, \"command\": \"cite\"}, {\"key\": \"bengio2013ste\", \"file\": \"experiments.tex\", \"line\": 97, \"command\": \"cite\"}, {\"key\": \"xu2026spon\", \"file\": \"experiments.tex\", \"line\": 103, \"command\": \"cite\"}, {\"key\": \"jiang2023mistral\", \"file\": \"experiments.tex\", \"line\": 199, \"command\": \"cite\"}, {\"key\": \"raffel2020c4\", \"file\": \"appendix.tex\", \"line\": 153, \"command\": \"cite\"}], \"online_verification\": [{\"key\": \"fang2024maskllm\", \"title\": \"MaskLLM: Learnable Semi-Structured Sparsity for Large Language Models\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"MaskLLM: Learnable Semi-Structured Sparsity for Large Language Models\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"xu2026spon\", \"title\": \"Resting Neurons, Active Insights: Robustify Activation Sparsity for Large Language Models\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Resting Neurons, Active Insights: Robustify Activation Sparsity for Large Language Models\", \"matched_year\": \"2025\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"muralidharan2024minitron\", \"title\": \"Compact Language Models via Pruning and Knowledge Distillation\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Compact Language Models via Pruning and Knowledge Distillation\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"gautam2026fastforward\", \"title\": \"Fast Forward: Accelerating LLM Prefill with Predictive FFN Sparsity\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Fast Forward: Accelerating LLM Prefill with Predictive FFN Sparsity\", \"matched_year\": \"2026\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"liu2025teal\", \"title\": \"Training-Free Activation Sparsity in Large Language Models\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Training-Free Activation Sparsity in Large Language Models\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"liu2023dejavu\", \"title\": \"Deja Vu: Contextual Sparsity for Efficient LLMs at Inference Time\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Deja Vu: Contextual Sparsity for Efficient LLMs at Inference Time\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"akhauri2024shadowllm\", \"title\": \"ShadowLLM: Predictor-based Contextual Sparsity for Large Language Models\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"ShadowLLM: Predictor-based Contextual Sparsity for Large Language Models\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"lee2024cats\", \"title\": \"CATS: Contextually-Aware Thresholding for Sparsity in Large Language Models\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"CATS: Contextually-Aware Thresholding for Sparsity in Large Language Models\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"zhang2025rsparse\", \"title\": \"R-Sparse: Rank-Aware Activation Sparsity for Efficient LLM Inference\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"R-Sparse: Rank-Aware Activation Sparsity for Efficient LLM Inference\", \"matched_year\": \"2025\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"federici2025dip\", \"title\": \"Efficient LLM Inference using Dynamic Input Pruning and Cache-Aware Masking\", \"status\": \"verified\", \"confidence\": 0.893, \"matched_title\": \"Code Artifact for Efficient LLM Inference using Dynamic Input Pruning and Cache-Aware Masking\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"mirzadeh2024relu\", \"title\": \"ReLU Strikes Back: Exploiting Activation Sparsity in Large Language Models\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"ReLU Strikes Back: Exploiting Activation Sparsity in Large Language Models\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"song2024turbosparse\", \"title\": \"Turbo Sparse: Achieving LLM SOTA Performance with Minimal Activated Parameters\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Turbo Sparse: Achieving LLM SOTA Performance with Minimal Activated Parameters\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"song2025prosparse\", \"title\": \"ProSparse: Introducing and Enhancing Intrinsic Activation Sparsity within Large Language Models\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"ProSparse: Introducing and Enhancing Intrinsic Activation Sparsity within Large Language Models\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"luo2024sparsinglaw\", \"title\": \"Sparsing Law: Towards Large Language Models with Greater Activation Sparsity\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Sparsing Law: Towards Large Language Models with Greater Activation Sparsity\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"song2024powerinfer\", \"title\": \"PowerInfer: Fast Large Language Model Serving with a Consumer-grade GPU\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"PowerInfer: Fast Large Language Model Serving with a Consumer-grade GPU\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"kim2016sequencekd\", \"title\": \"Sequence-Level Knowledge Distillation\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Sequence-Level Knowledge Distillation\", \"matched_year\": \"2016\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"sanh2019distilbert\", \"title\": \"DistilBERT, a distilled version of BERT: smaller, faster, cheaper and lighter\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"DistilBERT, a distilled version of BERT: smaller, faster, cheaper and lighter\", \"matched_year\": \"2019\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"sun2024wanda\", \"title\": \"A Simple and Effective Pruning Approach for Large Language Models\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"A Simple and Effective Pruning Approach for Large Language Models\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"frantar2023sparsegpt\", \"title\": \"SparseGPT: Massive Language Models Can Be Accurately Pruned in One-Shot\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"SparseGPT: Massive Language Models Can Be Accurately Pruned in One-Shot\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"fedus2022switch\", \"title\": \"Switch Transformers: Scaling to Trillion Parameter Models with Simple and Efficient Sparsity\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Switch Transformers: Scaling to Trillion Parameter Models with Simple and Efficient Sparsity\", \"matched_year\": \"2021\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"louizos2018l0\", \"title\": \"Learning Sparse Neural Networks through $L_0$ Regularization\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Learning Sparse Neural Networks through $L_0$ Regularization\", \"matched_year\": \"2017\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"maddison2017concrete\", \"title\": \"The Concrete Distribution: A Continuous Relaxation of Discrete Random Variables\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"The Concrete Distribution: A Continuous Relaxation of Discrete Random Variables\", \"matched_year\": \"2016\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"grattafiori2024llama3\", \"title\": \"The Llama 3 Herd of Models\", \"status\": \"mismatch\", \"confidence\": 1.0, \"matched_title\": \"The Llama 3 herd of models\", \"matched_year\": \"2025\", \"mismatch_fields\": [\"first_author: bib=grattafiori vs api=aaron\"], \"note\": \"\"}, {\"key\": \"jiang2023mistral\", \"title\": \"Mistral 7B\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Mistral 7B\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"jang2017gumbel\", \"title\": \"Categorical Reparameterization with Gumbel-Softmax\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Categorical Reparameterization with Gumbel-Softmax\", \"matched_year\": \"2016\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"shazeer2020glu\", \"title\": \"GLU Variants Improve Transformer\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"GLU Variants Improve Transformer\", \"matched_year\": \"2020\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"merity2017pointer\", \"title\": \"Pointer Sentinel Mixture Models\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Pointer Sentinel Mixture Models\", \"matched_year\": \"2016\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"hinton2015distilling\", \"title\": \"Distilling the Knowledge in a Neural Network\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Distilling the Knowledge in a Neural Network\", \"matched_year\": \"2015\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"bengio2013ste\", \"title\": \"Estimating or Propagating Gradients Through Stochastic Neurons for Conditional Computation\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Estimating or Propagating Gradients Through Stochastic Neurons for Conditional Computation\", \"matched_year\": \"2013\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"loshchilov2019adamw\", \"title\": \"Decoupled Weight Decay Regularization\", \"status\": \"mismatch\", \"confidence\": 1.0, \"matched_title\": \"Decoupled Weight Decay Regularization\", \"matched_year\": \"2017\", \"mismatch_fields\": [\"year: bib=2019 vs api=2017\"], \"note\": \"\"}, {\"key\": \"raffel2020c4\", \"title\": \"Exploring the Limits of Transfer Learning with a Unified Text-to-Text Transformer\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Exploring the Limits of Transfer Learning with a Unified Text-to-Text Transformer\", \"matched_year\": \"2019\", \"mismatch_fields\": [], \"note\": \"\"}]}, \"error\": null, \"metadata\": {}}"
    }
  },
  "sourceToolAssistantUUID": "a230e0b6-9b98-4a62-96aa-71199069e522",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/review_reviewer_1_772f066c",
  "sessionId": "fd7408d6-e7e0-4bb4-8dde-4202758b928d",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Runtime record

_source line 64_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[Round 1 审稿请求]: 你负责**方法严谨性 + 实验有效性**的审查。  ## Venue 信息 - **目标会议**: EMNLP 2026 (via ACL Rolling Review, May cycle) - **截止日期**: 2026-05-25 - **页数限制**: Long paper ≤8 页正文 + unlimited references + appendix…",
  "leafUuid": "638fe4c5-be94-4dfe-ad60-9d095396a7dd",
  "sessionId": "fd7408d6-e7e0-4bb4-8dde-4202758b928d"
}
```

---

### Runtime record

_source line 65_

```json
{
  "type": "ai-title",
  "aiTitle": "Review paper on sparse SwiGLU distillation methods",
  "sessionId": "fd7408d6-e7e0-4bb4-8dde-4202758b928d"
}
```

---

### Tool result

_source line 66 · 2026-05-17T08:15:00.769Z_

<details><summary>↩ Tool result · `toolu_019z7pVeXsedBMjCFFboA31r`</summary>

```text
# ARR Reviewer Guidelines: Key Focus Areas

## Core Reviewing Tasks

Reviewers should complete **four main tasks**:
1. Calendar allocation for reviewing and discussion periods
2. Assignment verification (expertise, conflicts of interest, desk-rejection criteria)
3. Writing substantive reviews
4. Updating assessments post-author response

## Primary Review Dimensions

**Soundness Assessment**: Technical validity must justify low scores. The guidance warns against scoring poorly without identifying specific faults, as this signals unconscious bias rather than legitimate concerns.

**Excitement Score**: Separate from soundness, this captures personal interest level—orthogonal to paper quality assessment.

**Overall Recommendation**: Composite judgment reflecting soundness, novelty, impact, and potential contribution to the field, regardless of personal enthusiasm.

## Critical Review Focus Areas

### Reading Strategy
Reviewers must read papers twice: initial skim-reading to adjust expectations without confirmation bias, then in-depth evaluation. The guidance emphasizes "postpone such searches until after they have read the paper completely" regarding related work verification.

### Specificity Requirement
Generic criticism is forbidden. Instead of stating "X is not clear," reviewers must specify "Y and Z are missing from X's description." Citations of missing references require exact identification.

### Common Problematic Heuristics to Avoid

The guidelines list 17 bias patterns (H1-H17), including:
- Dismissing findings as "obvious in retrospect"
- Requiring SOTA results when incremental progress suffices
- Penalizing negative results
- Criticizing methodological simplicity
- Demanding unnecessary additional experiments

## NLP-Specific Problem Areas

Reviewers should flag common issues with codes (M1-M5, T1-T2, R1-R5, G1-G5):

**Methodology issues** include LLM-only evaluation without validation, reproducibility gaps, undisclosed data quality problems, and incomplete proofs.

**Experimental results problems** span statistical rigor, overclaiming beyond evidence, and inappropriate claim scope relative to test populations.

## Reproducibility Expectations

Papers require "enough details to reproduce the experiments, including hyperparameter selection." Code/data availability should be clearly specified. Reviewers assess reproducibility without mandatory execution, focusing on whether sufficient information exists for replication.

## Tone and Professionalism

Reviews must maintain professional neutrality. The guidelines stress: "Write the review you would like to get yourself," noting that anonymous reviewing creates power asymmetries where sarcasm and dismissiveness can cause genuine harm.

## Post-Author Response Protocol

Reviewers must acknowledge author responses and update assessments accordingly. Ignoring rebuttals signals bad faith engagement. If unconvinced by responses, reviewers should explicitly explain why, providing actionable feedback rather than silence.

## Generative AI Restrictions

Reviewers cannot use AI to draft initial reviews or meta-reviews. Submitting manuscripts or reviews to non-privacy-preserving tools violates confidentiality and intellectual property obligations.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "57990846-c63e-4031-9fc6-87df705f15eb",
  "isSidechain": false,
  "promptId": "e22b3aa5-f147-4b55-a02c-533b2c761d41",
  "type": "user",
  "uuid": "3af3a0dd-c8ed-4a06-9f6a-1358ecb7b250",
  "toolUseResult": {
    "bytes": 100603,
    "code": 200,
    "codeText": "OK",
    "result": "# ARR Reviewer Guidelines: Key Focus Areas\n\n## Core Reviewing Tasks\n\nReviewers should complete **four main tasks**:\n1. Calendar allocation for reviewing and discussion periods\n2. Assignment verification (expertise, conflicts of interest, desk-rejection criteria)\n3. Writing substantive reviews\n4. Updating assessments post-author response\n\n## Primary Review Dimensions\n\n**Soundness Assessment**: Technical validity must justify low scores. The guidance warns against scoring poorly without identifying specific faults, as this signals unconscious bias rather than legitimate concerns.\n\n**Excitement Score**: Separate from soundness, this captures personal interest level—orthogonal to paper quality assessment.\n\n**Overall Recommendation**: Composite judgment reflecting soundness, novelty, impact, and potential contribution to the field, regardless of personal enthusiasm.\n\n## Critical Review Focus Areas\n\n### Reading Strategy\nReviewers must read papers twice: initial skim-reading to adjust expectations without confirmation bias, then in-depth evaluation. The guidance emphasizes \"postpone such searches until after they have read the paper completely\" regarding related work verification.\n\n### Specificity Requirement\nGeneric criticism is forbidden. Instead of stating \"X is not clear,\" reviewers must specify \"Y and Z are missing from X's description.\" Citations of missing references require exact identification.\n\n### Common Problematic Heuristics to Avoid\n\nThe guidelines list 17 bias patterns (H1-H17), including:\n- Dismissing findings as \"obvious in retrospect\"\n- Requiring SOTA results when incremental progress suffices\n- Penalizing negative results\n- Criticizing methodological simplicity\n- Demanding unnecessary additional experiments\n\n## NLP-Specific Problem Areas\n\nReviewers should flag common issues with codes (M1-M5, T1-T2, R1-R5, G1-G5):\n\n**Methodology issues** include LLM-only evaluation without validation, reproducibility gaps, undisclosed data quality problems, and incomplete proofs.\n\n**Experimental results problems** span statistical rigor, overclaiming beyond evidence, and inappropriate claim scope relative to test populations.\n\n## Reproducibility Expectations\n\nPapers require \"enough details to reproduce the experiments, including hyperparameter selection.\" Code/data availability should be clearly specified. Reviewers assess reproducibility without mandatory execution, focusing on whether sufficient information exists for replication.\n\n## Tone and Professionalism\n\nReviews must maintain professional neutrality. The guidelines stress: \"Write the review you would like to get yourself,\" noting that anonymous reviewing creates power asymmetries where sarcasm and dismissiveness can cause genuine harm.\n\n## Post-Author Response Protocol\n\nReviewers must acknowledge author responses and update assessments accordingly. Ignoring rebuttals signals bad faith engagement. If unconvinced by responses, reviewers should explicitly explain why, providing actionable feedback rather than silence.\n\n## Generative AI Restrictions\n\nReviewers cannot use AI to draft initial reviews or meta-reviews. Submitting manuscripts or reviews to non-privacy-preserving tools violates confidentiality and intellectual property obligations.",
    "durationMs": 15130,
    "url": "https://aclrollingreview.org/reviewerguidelines"
  },
  "sourceToolAssistantUUID": "57990846-c63e-4031-9fc6-87df705f15eb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/review_reviewer_1_772f066c",
  "sessionId": "fd7408d6-e7e0-4bb4-8dde-4202758b928d",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 67 · 2026-05-17T08:15:52.429Z_

<details><summary>Logged reasoning block</summary>

```text
I now have all the information I need. Let me compile a thorough review. Let me note:

Reference verification: 31 bib entries, all cited, no orphans, no missing. 29 verified, 0 not found, 2 mismatches (grattafiori2024llama3 has author format mismatch, loshchilov2019adamw has year mismatch with API showing 2017 instead of 2019). These are minor bibliographic issues.

Now let me write the complete review.

Key issues to structure:

**Must-Fix (Critical)**:

**N1**: The paper is framed as efficiency-motivated ("simplify inference," "eliminating compensation networks") but demonstrates NO wall-clock speedup. 

The pipeline actually adds 6.4% overhead, and while eliminating compensation saves 2.7%, this doesn't offset the predictor overhead, resulting in net +3.7% latency compared to compensation-based approaches. For a paper centered on efficiency gains, this is a critical disconnect between the stated motivation and actual performance.

**N2**: Downstream task collapse fundamentally limits practical value. At 50% sparsity (the primary evaluation point), MMLU drops to ~28% (random chance) and GSM8K falls below 2.2%. Even at 30% sparsity, MMLU plummets from 65.27% to 25.27% globally or 40.61% with uniform sparsity. The dramatic perplexity improvements don't translate to usable model capabilities.

**N3**: There's a significant mismatch between training with soft Gumbel-Sigmoid masks and evaluating with hard TEAL top-k selection. The appendix shows a ~30% gap in perplexity between the two approaches, but this discrepancy isn't formally analyzed. I need to understand how much of the performance degradation from dense to sparse models comes from this train-test mismatch versus the inherent information loss from sparsity itself.

**Should-Fix (Warning)**:

**W1**: The BCE comparison conflates multiple changes—KL uses Gumbel-Sigmoid with a penalty controller while BCE uses hard masks with compensation. When I look at the ablation combining BCE with Gumbel and penalty, it performs worse than vanilla BCE, showing the training setup matters significantly. The KL+STE comparison partially controls for this, but STE and hard masks are different gradient estimators, so the comparison isn't clean.

**W2**: The "parameter-free" penalty controller claim doesn't hold up—λ_max varies across targets (1000 to 5000), and at 30% sparsity the controller hits its cap with 5% deviation, meaning it can't enforce all targets.

**W3**: The evaluation is limited to 7-8B models, so the claim about SwiGLU architectures is only verified at a single scale.

**W4**: Variance estimates are missing for the primary result—only three seeds at one configuration (50% uniform), with no error bars on the main 50% global TEAL numbers.

**W5**: The gradient SNR measurement...

Now looking at the weaknesses more carefully. The gradient SNR uses C4 data while training happens on WikiText-103, which is an inconsistency. The paper frames the advantage as stemming from modeling inter-neuron dependencies specific to SwiGLU at this scale, but there's a simpler explanation: KL just provides a better training signal because it directly optimizes output quality, which any end-to-end objective would achieve. That framing overstates how specific the insight really is.

But stepping back, the paper does have genuine strengths. The theoretical decomposition is clean—showing how BCE gradients decompute per-neuron while KL couples through the downstream Jacobian is well-explained with the factor breakdown. The oracle F1 analysis is also compelling. BCE F1=0.613 > KL F1=0.540, yet KL has 91% better PPL. This directly demonstrates that per-neuron accuracy is the wrong proxy.
3. The 2D taxonomy (correction granularity × training signal coupling) is a useful organizational framework.
4. The three-regime analysis (budget-surplus, budget-constrained, capacity-limited) with non-monotonic allocation preference is an interesting empirical finding.
5. Good ablation coverage: loss function direction (Forward KL vs JSD vs Reverse KL), relaxation (Gumbel vs STE), compensation, hyperparameter sensitivity.
6. The SPON orthogonality analysis (cosine similarity 0.196) provides nice insight into the complementarity of static vs. learned correction.
7. Writing quality is generally good — clear exposition, well-structured.

Now I'm reconsidering my scoring more carefully. The core theoretical argument holds up and the gradient analysis is clean, though the experimental setup has some fairness issues around the BCE comparison and limited scale. The adaptive penalty controller works empirically without formal guarantees, so I'm settling on 3.5/5 for soundness. The KL versus BCE insight is genuinely interesting with a dramatic gap, and the 2D taxonomy is useful, but the lack of practical speedup, downstream collapse issues, and limited scale to 7-8B models significantly reduce the impact—I'd rate excitement at 2.5/5. Reproducibility is solid with good training descriptions, though a few details are missing like weight decay and gradient clipping specifics, and there's no mention of code release, so that's 3.5/5. Overall, this is a technically sound paper with a clear insight, but the practical limitations hold it back from being truly impactful. The theoretical contribution is solid and the experiments validate it clearly, so I think 3 (Findings acceptance) is the right call—the limitations are real but the paper is well-executed and honest about its scope. I'll settle on soundness 3.5, excitement 2.5, reproducibility 3.5, and overall 3, with high confidence in this assessment.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3af3a0dd-c8ed-4a06-9f6a-1358ecb7b250",
  "isSidechain": false,
  "requestId": "req_011Cb7op4L6xRF33AStTgnKi",
  "type": "assistant",
  "uuid": "182c9aca-0e0d-40af-a402-23ec1cd91229",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/review_reviewer_1_772f066c",
  "sessionId": "fd7408d6-e7e0-4bb4-8dde-4202758b928d",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FhnxYoRpfkxzZHRMuCDryb",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 15675,
      "cache_read_input_tokens": 59680,
      "output_tokens": 7618,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 15675,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 7618,
          "cache_read_input_tokens": 59680,
          "cache_creation_input_tokens": 15675,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 15675
          },
          "type": "message"
        }
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

_source line 68 · 2026-05-17T08:15:52.871Z_

全文通读完毕，引用验证完成，ARR 评审标准已获取。下面正式提交审稿意见。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "182c9aca-0e0d-40af-a402-23ec1cd91229",
  "isSidechain": false,
  "requestId": "req_011Cb7op4L6xRF33AStTgnKi",
  "type": "assistant",
  "uuid": "896c61d8-99ee-49ac-9781-2450330cd117",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/review_reviewer_1_772f066c",
  "sessionId": "fd7408d6-e7e0-4bb4-8dde-4202758b928d",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FhnxYoRpfkxzZHRMuCDryb",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 15675,
      "cache_read_input_tokens": 59680,
      "output_tokens": 7618,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 15675,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 7618,
          "cache_read_input_tokens": 59680,
          "cache_creation_input_tokens": 15675,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 15675
          },
          "type": "message"
        }
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

_source line 69 · 2026-05-17T08:17:57.722Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director · `toolu_01PSj2V5qMPDvVXKQjwMm5cU`</summary>

```json
{
  "text": "\n# Reviewer 1 审稿意见：Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs\n\n## Paper Summary\n\n本文提出用 KL divergence 替代 BCE 训练 SwiGLU LLM 的 activation sparsity predictor。核心论点是 BCE 梯度按 neuron 分解（Eq. 7: ∂L/∂s_j = σ(s_j) − m_j*），与推理时 TEAL 的 global top-k allocation 存在\"结构性不匹配\"；KL 梯度通过下游 Jacobian（factor (b)）耦合所有 neuron。方法使用 Gumbel-Sigmoid relaxation 实现可微训练，adaptive penalty controller 控制稀疏度。在 LLaMA-3.1-8B 上 50% sparsity 下 PPL 11.79 vs TEAL 的 23.31（无 compensation network）。跨架构验证于 Mistral-7B-v0.3。提出 correction granularity × training signal coupling 的 2D taxonomy，识别三种 sparsity regime。\n\n---\n\n## Summary of Strengths\n\n**S1. 清晰的理论洞察与形式化。** §3.5 的梯度分析是本文最强贡献。Factor (a)-(d) 分解清楚说明了 KL 和 BCE 的结构性差异：factor (b) 的 Jacobian ∂z/∂h^(ℓ) 使 KL 梯度依赖所有下游层的 mask 状态，而 BCE 的 Eq. 7 只依赖 neuron j 自身。这个观察数学上严格，且有直接的实证支撑。\n\n**S2. Oracle F1 分析揭示 proxy mismatch 的深度（§4.2）。** BCE 达到 F1=0.613（比 KL 的 0.540 高 +13pp）但 PPL 差 91%；KL 的 near-random precision (0.51) 表明它学到的 mask 与 magnitude oracle 完全不同，优化的是 distributional fidelity 而非 magnitude matching。这是全文最有说服力的实验证据，直接支撑了\"正确目标 > 高精度代理\"的核心论点。\n\n**S3. 消融设计覆盖关键设计选择。** Table 3 系统覆盖：loss direction（Forward KL vs JSD vs Reverse KL）、relaxation（Gumbel vs STE, Δ=3.98）、compensation 效果、以及关键的 isolation 实验（BCE + Gumbel + Penalty = 38.02，证明 penalty 框架本身不提供增益）。Loss effect (ΔPPL=26.23) 是 relaxation effect (ΔPPL=3.98) 的 6.6×，清晰分离了各组件贡献。\n\n**S4. 2D taxonomy 和 regime 分析有组织价值。** Table 1 的 correction granularity × training signal coupling 分类法简洁有效地定位了本文在文献中的位置。三 regime 分析（budget-surplus / budget-constrained / capacity-limited）发现 allocation preference 的非单调性（30% 偏好 uniform，40% 偏好 global，50% 无差异）是有意义的实证发现。\n\n**S5. SPON 正交性分析（§4.5）。** Cosine similarity 0.196 + 仅 2.4% PPL 改善的定量分解说明 KL predictor 已捕获大部分可恢复信号，static correction 与 learned prediction 接近正交，这对未来工作有指导意义。\n\n---\n\n## Summary of Weaknesses\n\n### Must-Fix 问题（影响接收决定）\n\n**N1 [critical] 论文以 efficiency 为动机，但实际无 wall-clock speedup，且 framing 产生误导。**\n- 具体位置：§1 (\"simplify inference by pruning 50% of FFN neurons\"), §4.6 (\"eliminates the compensation network, −2.7% latency\"), Appendix A (Table 6)\n- 问题：Table 6 (Appendix A) 显示 KL predictor-only 在 50% sparsity 下为 126.78ms（dense 119.11ms），overhead = +6.4%。消除 compensation 节省 2.7%，但 predictor 本身加 6.4%。与 compensation-based 方法相比净效果是 +6.4% vs +8.9%——仅节省 2.5pp overhead，且两者都比 dense 慢。更关键的是，unstructured element-wise mask 不产生任何 sparse computation speedup，论文自己在 Appendix A 和 Limitations 中承认 \"net acceleration requires kernel-level sparse computation optimizations\"。\n- 为什么影响接收：论文 Introduction 的 framing 暗示 \"simplify inference\" 和 \"eliminating compensation\" 带来效率增益。但实际效果是：(1) 比 dense 慢 6.4%；(2) 比有 compensation 的方案快 2.5pp 但仍然更慢。一篇以 sparsity prediction 为核心的论文，在没有任何实际加速的情况下，需要将 framing 从 \"efficiency\" 调整为 \"prediction quality / understanding\"。\n- 建议修改方向：重新定位论文贡献为\"理解 loss function 对 sparsity prediction 的影响\"和\"elimination of compensation as architectural simplification\"。在 Introduction 和 Abstract 中明确说明当前无 wall-clock speedup，将加速留作 future work with structured sparsity。\n\n**N2 [critical] 下游任务在实用稀疏度下崩溃，严重削弱 practical value。**\n- 具体位置：Table 2 (30% KL global: MMLU 25.27%, 50%: MMLU 27.89% ≈ random), Table 4\n- 问题：Dense MMLU = 65.27%。30% sparsity + global TEAL: MMLU = 25.27%（−40pp，接近 random 25%）；uniform 恢复到 40.61% 但仍损失 24.7pp。50% 时所有方法 MMLU ≈ 28%，GSM8K < 2.2%。PPL 的大幅改善（11.79 vs 23.31）未转化为 reasoning 能力保持。论文在 §4.3 提到 \"PPL is a poor proxy for reasoning\"，但这个结论在 Limitations 中才被充分讨论，而非贯穿全文。\n- 为什么影响接收：论文的核心评价指标（PPL）与实际应用关注的指标（downstream task performance）之间存在严重脱节。如果 50% sparsity 下模型在所有知识/推理任务上退化到 random，这意味着论文展示的\"最引人注目\"的改善点（49% PPL reduction at 50%）在实践中可能不相关。审稿人需要知道：在什么稀疏度下，该方法能同时保持合理的 PPL 和 downstream performance？\n- 建议修改方向：(1) 在主实验中更突出讨论 PPL-downstream disconnect；(2) 将 30% 的 downstream 结果提升到与 50% PPL 同等重要的位置；(3) 考虑补充 10-20% sparsity 下的 downstream 评估，找到 practical sweet spot。\n\n**N3 [critical] 训练-推理 mask 不匹配未被分析，且残差退化来源不明。**\n- 具体位置：§3.3 (Gumbel-Sigmoid, τ annealed to 0.1), §4.1 (predictor-TEAL inference), Appendix B Table 5\n- 问题：训练使用 soft Gumbel-Sigmoid mask（即使 τ=0.1 也非完全 binary），推理使用 TEAL 的 hard top-k allocation。Table 5 (Appendix B) 揭示了关键数据：d_b=128 在 per-token 评估下 PPL=9.218，在 TEAL global 下 PPL=11.963——差距约 30%。这意味着从 dense (6.12) 到 KL-TEAL (11.79) 的全部退化（Δ=5.67）中，有相当一部分可能来自 soft→hard mismatch 和 TEAL global allocation 的信息丢失，而非 sparsity 本身的 capacity loss。论文从未正式分析这一 gap 的来源。\n- 为什么影响接收：不分析这个 gap，读者无法判断剩余退化是方法可以改进的（通过 better allocation 或 better train-test alignment）还是 fundamental limit。这直接关系到方法的 ceiling 和 future improvement 空间。\n- 建议修改方向：添加分解分析，例如：(1) per-token hard mask evaluation（控制 allocation）；(2) per-token soft mask evaluation（Table 5 已有）；(3) global hard mask with oracle scores。分离 mask quality loss、discretization loss 和 allocation loss。\n\n---\n\n### Should-Fix 问题（影响评分但不一票否决）\n\n**W1 [warning] BCE 对比的公平性问题：系统差异超过 loss function。**\n- 具体位置：Table 3 ablation\n- 问题：KL 系统 = Forward KL + Gumbel-Sigmoid + penalty controller；BCE 系统 = BCE + hard mask + compensation。消融中 \"BCE + Gumbel + Penalty\" 达到 38.02（比 vanilla BCE 的 27.97 更差），说明 penalty 框架与 BCE 不兼容。这意味着 Table 2 中的 KL vs BCE 对比不仅是 loss function 的差异，而是整个 training pipeline 的差异。KL+STE (15.77) 提供了更接近的对比，但 STE 本身的 gradient bias 也是 confound。\n- 建议：明确说明 KL 的优势来自 loss function + compatible training infrastructure 的组合，而非单独的 loss function。或提供一个更直接的 fair comparison（例如 MSE on output logits + Gumbel，控制 training infrastructure 的同时对比 loss）。\n\n**W2 [warning] \"Parameter-free\" penalty controller 表述不准确。**\n- 具体位置：§3.4, footnote (\"parameter-free, no step-size tuning\"), Table 7\n- 问题：λ_max 在不同 sparsity target 下取不同值（30% 和 70% 用 5000，50% 用 1000），这本身就是 hyperparameter。Table 7 显示 30% target 时 λ 达到 cap (5000)，actual sparsity = 0.285（偏差 5%）。Controller 无法在所有 target 下精确收敛。\n- 建议：去掉 \"parameter-free\" 措辞；讨论 λ_max 选择对结果的影响；说明 30% 时 5% deviation 对 PPL 的影响。\n\n**W3 [warning] 统计效力不足。**\n- 具体位置：Appendix F (3 seeds, 50% uniform only)\n- 问题：(1) 3 seeds 的 95% CI（≈ [11.73, 12.11]，t-distribution）较宽，对 Table 3 中差异 <1 的 ablation 结果（如 Forward KL 11.79 vs JSD 12.54），无法判断统计显著性。(2) Multi-seed 仅在 50% uniform 下做，主结果（50% global TEAL, PPL 11.79）无方差估计。(3) Downstream metrics 更 noisy（ARC-c 33.8±1.2%），3 seeds 不足以支撑 downstream 的 regime 分析结论。\n- 建议：至少在 primary configuration (50% global TEAL) 也报告 multi-seed；考虑增加到 5 seeds。\n\n**W4 [warning] 实验规模受限。**\n- 具体位置：§4.1, §4.6, Limitations\n- 问题：仅 7-8B 模型（LLaMA-3.1-8B, Mistral-7B-v0.3），同一参数量级，同为 SwiGLU。论文多处使用 \"transfers across SwiGLU architectures\" 但实际上 (a) 仅测试了一个 scale，(b) 两个模型的 d_ff / d_model ratio 相同（14336/4096），(c) Mistral 的主要差异是 GQA + sliding window attention，这些差异与 FFN sparsity prediction 关系不大。\n- 建议：弱化 generalization claims，改为 \"verified on two 7-8B SwiGLU models\"。如果可能，增加 13B 或更大模型的验证。\n\n**W5 [warning] Gradient SNR 测量与训练设置不一致。**\n- 具体位置：§3.5 empirical verification\n- 问题：SNR 在 C4 数据上测量（\"80 steps on LLaMA-3.1-8B (C4 data)\"），但训练使用 WikiText-103。不同数据分布可能影响 SNR，使该测量不能直接代表训练过程中的实际 gradient quality。\n- 建议：在 WikiText-103 上重复 SNR 测量，或解释为何选择 C4 及其对结论的影响。\n\n**W6 [warning] 训练数据集过小且与评估数据同源。**\n- 具体位置：§4.1 (\"trained for 1000 steps on WikiText-103 with batch size 4\")\n- 问题：1000 steps × batch 4 × seq 2048 = ~8M tokens，仅为 WikiText-103 全集的一小部分。评估在 WikiText-2 上——与 WikiText-103 同源（都是 Wikipedia）。虽然 Appendix D 的 C4 OOD 评估有所缓解，但仅有一个 sparsity level (50%) 和一个 metric (PPL)。\n- 建议：在 C4 上补充 30% 和 70% 的评估；如果条件允许，考虑在非 Wikipedia 数据上训练一版 predictor 验证泛化性。\n\n---\n\n### 小问题（不影响接收）\n\n- **M1**: AdamW 的 weight decay 值未报告（§4.1）。\n- **M2**: BCE 的 oracle mask 生成方式（per-layer top-k 还是 global top-k？）未明确说明（§3.5 \"oracle masks m_j* = 1[|g_j| ≥ top-k threshold]\"，但 threshold 的作用域不清楚）。\n- **M3**: Table 1 将 ShadowLLM 归为 \"Per-layer\"，但 ShadowLLM 使用 attention-based routing，可能更接近 per-token。需核实分类准确性。\n- **M4**: loshchilov2019adamw 引用年份为 2019，OpenAlex 匹配到的原始 arXiv 年份为 2017。会议发表年份与 arXiv 年份不一致，建议统一。\n- **M5**: Appendix A 的 latency 测量在 RTX PRO 6000 Blackwell 上，但训练在 A6000 上（Limitations 提到 \"~17 minutes on A6000\"）。两个 GPU 架构差异较大，latency 数据的可迁移性不明。\n\n---\n\n## Questions to Authors\n\n**Q1.** Table 5 (Appendix B) 显示 d_b=128 per-token PPL = 9.218, TEAL global PPL = 11.963。这 ~30% 的 gap 中，有多少来自 soft→hard discretization，多少来自 TEAL global 的 budget allocation 策略？能否提供 per-token hard mask evaluation 来分离这两个因素？\n\n**Q2.** BCE 对比中，BCE 的 learning rate 和 optimizer 设置是否与 KL 完全一致？如果不一致，BCE 是否经过独立的 hyperparameter tuning？\n\n**Q3.** 论文称 \"KL's near-random precision (0.51)\"——这是否意味着 KL predictor 学到的 mask 与 magnitude-based oracle 几乎无相关性？如果是，KL predictor 到底保留了哪些 neuron——是否有 per-layer 的分析可以说明 KL mask 与 oracle mask 的差异模式？\n\n**Q4.** 30% sparsity 下 penalty controller 达到 λ cap (5000) 且 actual sparsity = 28.5%。如果 λ_max 设为更大的值（如 10000），sparsity 能否达到 30%？如果能，PPL 会如何变化？\n\n**Q5.** 是否尝试过在训练中使用 hard top-k (with STE) 替代 Gumbel-Sigmoid 来缩小 train-test gap？Table 3 已有 KL+STE 但未说明其是否使用 top-k selection。\n\n---\n\n## 官方维度打分（ACL Rolling Review form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5/5 | 核心梯度分析数学正确，factor (a)-(d) 分解完整。Gumbel-Sigmoid 使用正确。但 BCE 对比的公平性有 confound (W1)；train-test mask mismatch 未分析 (N3)；penalty controller 在边界情况下表现不佳 (W2)。 |\n| Excitement | 2.5/5 | \"正确 loss > 高精度 proxy\" 的洞察有价值，oracle F1 分析令人信服。2D taxonomy 有组织贡献。但无实际 speedup (N1) 和 downstream collapse (N2) 严重限制了实际影响力。 |\n| Reproducibility | 3.5/5 | 训练设置报告较全（model, data, steps, LR, optimizer, τ schedule）。缺少 weight decay、gradient clipping、evaluation batch size。未提及代码是否会开源。Appendix 的超参数 sensitivity 分析有利于复现。 |\n| Overall | 3/5 | Findings 边界。理论洞察清晰且有实证支撑，但 practical impact 受限于 (1) 无 wall-clock speedup, (2) downstream collapse, (3) limited scale。 |\n| Confidence | 4/5 | 对 activation sparsity 和 knowledge distillation 领域较熟悉，仔细阅读了全文和附录。 |\n\n---\n\n## 总体评分\n\n**Overall**: 3/5 (Findings acceptance)\n\n**一句话总结**: 论文提供了有价值的理论洞察（KL 梯度耦合解决 BCE 的结构性不匹配），实验设计合理但存在 BCE 对比公平性和 train-test mismatch 未分析的问题；无实际推理加速和下游任务崩溃严重限制了实用价值，适合 Findings 而非主会议。\n\n---\n\n## 主要优势\n\n- 梯度分析形式化清晰，factor (a)-(d) 分解为理解 loss function 设计提供了有用的分析框架\n- Oracle F1 分析（BCE F1=0.613 > KL F1=0.540，但 PPL 差 91%）是全文最有说服力的实验，直接 falsify 了 \"per-neuron accuracy = output quality\" 的隐含假设\n- 消融设计系统全面，loss isolation 实验（BCE + Gumbel + Penalty = 38.02）有效分离了 loss function 和 training infrastructure 的贡献\n- 三 regime 分析发现了 allocation preference 的非单调性，对部署决策有实用指导价值\n- 写作质量好，结构清晰，主线统一\n",
  "reviewer_id": "1",
  "project": "distill_sparse_swiglu"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "896c61d8-99ee-49ac-9781-2450330cd117",
  "isSidechain": false,
  "requestId": "req_011Cb7op4L6xRF33AStTgnKi",
  "type": "assistant",
  "uuid": "98b9bb72-7691-4746-928c-8b1645186b67",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/review_reviewer_1_772f066c",
  "sessionId": "fd7408d6-e7e0-4bb4-8dde-4202758b928d",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FhnxYoRpfkxzZHRMuCDryb",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 15675,
      "cache_read_input_tokens": 59680,
      "output_tokens": 7618,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 15675,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 7618,
          "cache_read_input_tokens": 59680,
          "cache_creation_input_tokens": 15675,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 15675
          },
          "type": "message"
        }
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

_source line 70_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[Round 1 审稿请求]: 你负责**方法严谨性 + 实验有效性**的审查。  ## Venue 信息 - **目标会议**: EMNLP 2026 (via ACL Rolling Review, May cycle) - **截止日期**: 2026-05-25 - **页数限制**: Long paper ≤8 页正文 + unlimited references + appendix…",
  "leafUuid": "98b9bb72-7691-4746-928c-8b1645186b67",
  "sessionId": "fd7408d6-e7e0-4bb4-8dde-4202758b928d"
}
```

---

### Runtime record

_source line 71_

```json
{
  "type": "ai-title",
  "aiTitle": "Review paper on sparse SwiGLU distillation methods",
  "sessionId": "fd7408d6-e7e0-4bb4-8dde-4202758b928d"
}
```

---

### Tool result

_source line 72 · 2026-05-17T08:18:01.776Z_

<details><summary>↩ Tool result · `toolu_01PSj2V5qMPDvVXKQjwMm5cU`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director\"}, \"error\": \"\"}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "98b9bb72-7691-4746-928c-8b1645186b67",
  "isSidechain": false,
  "promptId": "e22b3aa5-f147-4b55-a02c-533b2c761d41",
  "type": "user",
  "uuid": "5abda6e4-8972-46ac-a978-0e93b73db193",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"review_director_key\\\": \\\"feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director\\\"}, \\\"error\\\": \\\"\\\"}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director\"}, \"error\": \"\"}"
    }
  },
  "sourceToolAssistantUUID": "98b9bb72-7691-4746-928c-8b1645186b67",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/review_reviewer_1_772f066c",
  "sessionId": "fd7408d6-e7e0-4bb4-8dde-4202758b928d",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Runtime record

_source line 73_

```json
{
  "type": "ai-title",
  "aiTitle": "Review paper on sparse SwiGLU distillation methods",
  "sessionId": "fd7408d6-e7e0-4bb4-8dde-4202758b928d"
}
```

---

### Runtime record

_source line 74 · 2026-05-17T08:19:49.854Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-17T08:19:49.854Z",
  "sessionId": "fd7408d6-e7e0-4bb4-8dde-4202758b928d",
  "content": "[Round 1 审稿请求]:\n以下是 Reviewer 2 的完整审稿意见，请逐条回应：对每个 Must-Fix / Should-Fix / 小问题，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 2 — Round 1 审稿意见（新颖性 + 完整性）\n\n### 总体评分\n**Overall**: 3.0 / 5 (Findings)\n**一句话总结**: 核心方法是已有技术（KL distillation + Gumbel relaxation）在新场景（per-token activation sparsity）的组合应用，执行质量扎实但新颖性有限；downstream metrics 与 PPL 叙事存在系统性矛盾，削弱了核心 claim 的说服力。\n\n### Must-Fix 问题\n\n**N1** [critical] Responsible NLP Research Checklist 缺失，desk rejection 风险\n- ARR 自 2024-12 起强制要求此 checklist，缺失可直接 desk reject。论文无 checklist 也无 Ethics Statement。\n- 建议：参照 aclrollingreview.org/responsibleNLPresearch/ 逐项填写。\n\n**N2** [critical] Downstream metrics 与 PPL-centric 叙事系统性矛盾\n- Table 1: 30% sparsity KL global MMLU = 25.27%，比 TEAL vanilla (38.61%) 低 13.3pp。50% sparsity MMLU 全部 ≈28%（近随机），KL (27.89%) vs TEAL (28.32%) 无差异。GSM8K 50% KL (1.29%) 比 TEAL (1.97%) 更差。\n- 论文核心叙事围绕 PPL 改善（11.79 vs 23.31），但 downstream 讲了不同的故事。如果 PPL 改善不转化为 downstream 收益，\"eliminates compensation networks\" 的实际价值需重新评估。\n- Limitations 承认 PPL is poor proxy for reasoning，但 Abstract/Introduction 仍以 PPL 为核心 framing，自相矛盾。\n- 建议：Abstract/Introduction 诚实呈现 downstream mixed results；讨论 KL 训练为何恶化 MMLU（可能过度偏向 PPL-dominant layers）。\n\n**N3** [critical] 与 MaskLLM 核心技术重叠未充分辨析\n- MaskLLM (NeurIPS 2024) 同样用 frozen weights + learnable masks + Gumbel relaxation + KL divergence。Related Work 仅以 \"weight vs activation, static vs contextual\" 区分，但这是应用场景差异而非方法论差异。核心 pipeline（KL + Gumbel mask learning with frozen weights）相同。\n- 论文未讨论：(1) Gumbel-Softmax (MaskLLM) vs Gumbel-Sigmoid (本文) 的技术原因；(2) MaskLLM 是否已隐含解决 structural mismatch；(3) 如果 MaskLLM 的 mask 改为 input-dependent 是否等价于本文方法。\n- 建议：明确讨论方法论层面的区别和联系。\n\n### Should-Fix 问题\n\n**W1** [warning] 三 regime 分析证据不足以支撑 claim 强度\n- 三 regime 定义来自 2 个模型 × 3 个 sparsity levels = 6 数据点。具体边界阈值（≤30%, ~40%, ≥50%）的跨规模/跨架构泛化性完全未验证，但论文作为 Contribution 之一呈现。\n\n**W2** [warning] D2DMoE (NeurIPS 2024) 遗漏\n- Dense-to-Dynamic-k MoE 训练 router 用 ℓ2-norm regression 预测 expert 贡献，实现 per-token activation sparsity。其 training signal 既非 BCE 也非 KL，应位于 taxonomy 的 Per-token × Intermediate cell。遗漏使 taxonomy 不完整。\n\n**W3** [warning] Abstract 数据堆砌（18+ 个数字），审稿人 30 秒内无法消化\n\n**W4** [warning] 无实际 wall-clock speedup（+6.4% overhead），但 framing 暗示 efficiency gain\n\n**W5** [warning] Taxonomy 可能 post-hoc rationalization\n- 3×3 中仅 4 cell 填充，5 cell 空。两个轴恰好让本文独占一 cell。DejaVu 被归类为 Per-token × Decomposed 但 Table 2 中缺失。\n\n**W6** [warning] WAS (EMNLP 2025 main) 可能遗漏\n\n### 小问题\n- Abstract 中 \"-ing\" 分词短语有轻微 AI 写作痕迹\n- xu2026spon bib year=2026 vs OpenAlex=2025\n- Table 2 缺 DejaVu\n- Figure 1 label \"fig:taxonomy\" 但内容是 method overview\n- Conclusion 仅 3 行过短\n\n### 主要优势\n1. Gradient analysis 清晰有力，SNR 验证\n2. Ablation 系统全面，loss isolation 有力\n3. Cross-architecture Mistral 验证一致\n4. F1 oracle analysis 优雅\n5. 训练成本低"
}
```

---

### Runtime record

_source line 75 · 2026-05-17T08:19:49.855Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-17T08:19:49.855Z",
  "sessionId": "fd7408d6-e7e0-4bb4-8dde-4202758b928d"
}
```

---

## Round 2

2 recorded events

### User

_source line 76 · 2026-05-17T08:19:49.845Z_

Continue from where you left off.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5abda6e4-8972-46ac-a978-0e93b73db193",
  "isSidechain": false,
  "promptId": "e2bd2d71-d1a2-42f3-86c3-b3e33af96de1",
  "type": "user",
  "isMeta": true,
  "uuid": "0e2f15b1-1fdf-4a90-8023-879e5b486833",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/review_reviewer_1_772f066c",
  "sessionId": "fd7408d6-e7e0-4bb4-8dde-4202758b928d",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 77 · 2026-05-17T08:19:49.845Z_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0e2f15b1-1fdf-4a90-8023-879e5b486833",
  "isSidechain": false,
  "type": "assistant",
  "uuid": "2a312550-517d-4b2b-9d0b-fe4e536f6c3c",
  "isApiErrorMessage": false,
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/review_reviewer_1_772f066c",
  "sessionId": "fd7408d6-e7e0-4bb4-8dde-4202758b928d",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "id": "7f119a77-7d08-42ac-b565-06854650d4de",
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

14 recorded events

### User

_source line 78 · 2026-05-17T08:19:49.990Z_

[Round 1 审稿请求]:
以下是 Reviewer 2 的完整审稿意见，请逐条回应：对每个 Must-Fix / Should-Fix / 小问题，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。

---

## Reviewer 2 — Round 1 审稿意见（新颖性 + 完整性）

### 总体评分
**Overall**: 3.0 / 5 (Findings)
**一句话总结**: 核心方法是已有技术（KL distillation + Gumbel relaxation）在新场景（per-token activation sparsity）的组合应用，执行质量扎实但新颖性有限；downstream metrics 与 PPL 叙事存在系统性矛盾，削弱了核心 claim 的说服力。

### Must-Fix 问题

**N1** [critical] Responsible NLP Research Checklist 缺失，desk rejection 风险
- ARR 自 2024-12 起强制要求此 checklist，缺失可直接 desk reject。论文无 checklist 也无 Ethics Statement。
- 建议：参照 aclrollingreview.org/responsibleNLPresearch/ 逐项填写。

**N2** [critical] Downstream metrics 与 PPL-centric 叙事系统性矛盾
- Table 1: 30% sparsity KL global MMLU = 25.27%，比 TEAL vanilla (38.61%) 低 13.3pp。50% sparsity MMLU 全部 ≈28%（近随机），KL (27.89%) vs TEAL (28.32%) 无差异。GSM8K 50% KL (1.29%) 比 TEAL (1.97%) 更差。
- 论文核心叙事围绕 PPL 改善（11.79 vs 23.31），但 downstream 讲了不同的故事。如果 PPL 改善不转化为 downstream 收益，"eliminates compensation networks" 的实际价值需重新评估。
- Limitations 承认 PPL is poor proxy for reasoning，但 Abstract/Introduction 仍以 PPL 为核心 framing，自相矛盾。
- 建议：Abstract/Introduction 诚实呈现 downstream mixed results；讨论 KL 训练为何恶化 MMLU（可能过度偏向 PPL-dominant layers）。

**N3** [critical] 与 MaskLLM 核心技术重叠未充分辨析
- MaskLLM (NeurIPS 2024) 同样用 frozen weights + learnable masks + Gumbel relaxation + KL divergence。Related Work 仅以 "weight vs activation, static vs contextual" 区分，但这是应用场景差异而非方法论差异。核心 pipeline（KL + Gumbel mask learning with frozen weights）相同。
- 论文未讨论：(1) Gumbel-Softmax (MaskLLM) vs Gumbel-Sigmoid (本文) 的技术原因；(2) MaskLLM 是否已隐含解决 structural mismatch；(3) 如果 MaskLLM 的 mask 改为 input-dependent 是否等价于本文方法。
- 建议：明确讨论方法论层面的区别和联系。

### Should-Fix 问题

**W1** [warning] 三 regime 分析证据不足以支撑 claim 强度
- 三 regime 定义来自 2 个模型 × 3 个 sparsity levels = 6 数据点。具体边界阈值（≤30%, ~40%, ≥50%）的跨规模/跨架构泛化性完全未验证，但论文作为 Contribution 之一呈现。

**W2** [warning] D2DMoE (NeurIPS 2024) 遗漏
- Dense-to-Dynamic-k MoE 训练 router 用 ℓ2-norm regression 预测 expert 贡献，实现 per-token activation sparsity。其 training signal 既非 BCE 也非 KL，应位于 taxonomy 的 Per-token × Intermediate cell。遗漏使 taxonomy 不完整。

**W3** [warning] Abstract 数据堆砌（18+ 个数字），审稿人 30 秒内无法消化

**W4** [warning] 无实际 wall-clock speedup（+6.4% overhead），但 framing 暗示 efficiency gain

**W5** [warning] Taxonomy 可能 post-hoc rationalization
- 3×3 中仅 4 cell 填充，5 cell 空。两个轴恰好让本文独占一 cell。DejaVu 被归类为 Per-token × Decomposed 但 Table 2 中缺失。

**W6** [warning] WAS (EMNLP 2025 main) 可能遗漏

### 小问题
- Abstract 中 "-ing" 分词短语有轻微 AI 写作痕迹
- xu2026spon bib year=2026 vs OpenAlex=2025
- Table 2 缺 DejaVu
- Figure 1 label "fig:taxonomy" 但内容是 method overview
- Conclusion 仅 3 行过短

### 主要优势
1. Gradient analysis 清晰有力，SNR 验证
2. Ablation 系统全面，loss isolation 有力
3. Cross-architecture Mistral 验证一致
4. F1 oracle analysis 优雅
5. 训练成本低

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2a312550-517d-4b2b-9d0b-fe4e536f6c3c",
  "isSidechain": false,
  "promptId": "e2bd2d71-d1a2-42f3-86c3-b3e33af96de1",
  "type": "user",
  "uuid": "a4f405a5-bc63-492d-b377-6db373db3646",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/review_reviewer_1_772f066c",
  "sessionId": "fd7408d6-e7e0-4bb4-8dde-4202758b928d",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 79 · 2026-05-17T08:20:35.036Z_

<details><summary>Logged reasoning block</summary>

```text
The Review Director is asking me (Reviewer 1) to respond to Reviewer 2's complete review, going through each issue and marking [AGREE] or [REBUT] with evidence from the paper.

Let me go through each issue systematically.

### Must-Fix

**R2-N1**: Responsible NLP Research Checklist missing, desk rejection risk.
- I need to check if the paper has this. From my reading of main.tex, there's no checklist or ethics statement. This is a valid concern. I should [AGREE].

**R2-N2**: Downstream metrics vs PPL narrative contradiction.


- This aligns with my own N2. I should [AGREE] and reinforce with my own findings.

**R2-N3**: Overlap with MaskLLM not sufficiently discussed.
- Looking at the comparison more carefully, MaskLLM uses frozen weights with learnable masks and Gumbel relaxation to achieve N:M semi-structured sparsity patterns, while the paper's approach differs in its specific methodology. The Related Work section mentions MaskLLM but doesn't clearly delineate where the technical contributions diverge, so I think [AGREE] is warranted here.

The core distinction comes down to a few key points: this work targets activation sparsity with per-token contextual masks and global top-k selection, whereas MaskLLM focuses on weight sparsity with static input-independent masks over N:M patterns. The per-token prediction aspect is genuinely novel since it creates different gradient dynamics compared to MaskLLM's fixed masks. That said, Reviewer 2 has a point that the foundational pipeline—combining KL divergence, Gumbel relaxation, and frozen weights—borrows heavily from existing work, so the paper needs to articulate more clearly what the methodological innovation actually is beyond the application domain. the contextual prediction setting and (b) showing KL + Gumbel works for per-token masks. The per-token contextual nature does create a fundamentally different optimization landscape — the gradient analysis in §3.5 is specific to that setting — so I should acknowledge the overlap while clarifying what's genuinely novel versus adapted from MaskLLM.

On the regime analysis, six data points is admittedly thin for defining boundaries, but the non-monotonic allocation preference itself is an interesting finding worth noting. For D2DMoE, I need to verify whether it uses router training with ℓ2-norm regression and how that fits into the taxonomy.

Now I'm checking the abstract for the data overload concern. Counting the numbers: 2.37M parameters, 75.9M total, <1%, 11.79 PPL at 50%, 23.31 for vanilla TEAL, 27.97 for BCE at 2.71×. That's roughly 8 distinct metrics packed in, which does feel dense for an abstract.

Looking at the full list of numbers across the paper—11.92±0.07, CV<1%, percentages ranging from 7% to 100%, speedup multipliers like 2.93×, model sizes like 7-8B, and specific values like 0.196 and 12.08→11.79—there are easily 25+ data points scattered throughout. The reviewer's right that this reads more like a data dump than a coherent narrative. [AGREE].

The wall-clock speedup issue aligns with what I noted earlier. [AGREE].

On whether the taxonomy is post-hoc rationalization, I'm considering whether the framework was designed to fit the results rather than the results being evaluated against a pre-existing framework.  The concern that 5 out of 9 cells are empty and the axes were chosen to make this paper occupy a unique cell is worth taking seriously. That said, correction granularity and training signal coupling do feel like meaningful dimensions for understanding error correction approaches. The post-hoc concern isn't entirely dismissible, but I think there's enough substance here to partially agree rather than fully concede. [AGREE partially].

For WAS (EMNLP 2025), I'm not certain what this refers to—possibly Weight-Activation Sparsity or another acronym—and without more context I can't properly evaluate whether it's a genuine omission. I'll flag this as something I need clarification on.

On the abstract, I'm spotting several -ing phrases that could be tightened: "eliminating the need for compensation," "confirming training stability," and "demonstrating substantial output fidelity" all use this construction. These could be more direct.

The -ing phrases throughout are indeed a writing pattern worth addressing. [AGREE].

The bibliography year discrepancy is valid—if OpenAlex lists 2025 but the entry shows 2026, that's an error I should correct. I've noticed similar issues in my own review of the references.

Looking at the tables, DejaVu appears in the taxonomy but not in the main results table, which is a notable gap for a direct competitor baseline. [AGREE].

The figure labeling also seems off—the method overview figure is labeled as the taxonomy, but the actual taxonomy lives in Table 1. That's an inconsistency worth fixing. [AGREE].

The conclusion is quite brief at just three lines, which doesn't give enough space to synthesize the findings properly. [AGREE].

Now I'll draft the cross-review response.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a4f405a5-bc63-492d-b377-6db373db3646",
  "isSidechain": false,
  "requestId": "req_011Cb7pBNw8CPcG7LiVxFMWy",
  "type": "assistant",
  "uuid": "d6ec01ac-8aef-4555-8b04-77716776d0e1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/review_reviewer_1_772f066c",
  "sessionId": "fd7408d6-e7e0-4bb4-8dde-4202758b928d",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013bnKh968uPS2dUUmKsfeMx",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 61680,
      "cache_read_input_tokens": 11841,
      "output_tokens": 2041,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 61680,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 2041,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 61680,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 61680
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "messages_changed",
        "cache_missed_input_tokens": 47015
      }
    }
  }
}
```

</details>

---

### Assistant

_source line 80 · 2026-05-17T08:20:35.039Z_

逐条回应 Reviewer 2 的审稿意见。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d6ec01ac-8aef-4555-8b04-77716776d0e1",
  "isSidechain": false,
  "requestId": "req_011Cb7pBNw8CPcG7LiVxFMWy",
  "type": "assistant",
  "uuid": "e1758800-ce19-426d-97f4-3b67f93e510f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/review_reviewer_1_772f066c",
  "sessionId": "fd7408d6-e7e0-4bb4-8dde-4202758b928d",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013bnKh968uPS2dUUmKsfeMx",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 61680,
      "cache_read_input_tokens": 11841,
      "output_tokens": 2041,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 61680,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 2041,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 61680,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 61680
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "messages_changed",
        "cache_missed_input_tokens": 47015
      }
    }
  }
}
```

</details>

---

### Tool call

_source line 81 · 2026-05-17T08:20:35.046Z_

<details open><summary>🔧 Tool call — Read · `toolu_015zShvfH5yGg2xrhtv6qXsD`</summary>

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
  "parentUuid": "e1758800-ce19-426d-97f4-3b67f93e510f",
  "isSidechain": false,
  "requestId": "req_011Cb7pBNw8CPcG7LiVxFMWy",
  "type": "assistant",
  "uuid": "91c29ca2-3c1a-4952-a5a6-627f5c095632",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/review_reviewer_1_772f066c",
  "sessionId": "fd7408d6-e7e0-4bb4-8dde-4202758b928d",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013bnKh968uPS2dUUmKsfeMx",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 61680,
      "cache_read_input_tokens": 11841,
      "output_tokens": 2041,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 61680,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 2041,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 61680,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 61680
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "messages_changed",
        "cache_missed_input_tokens": 47015
      }
    }
  }
}
```

</details>

---

### Tool result

_source line 82 · 2026-05-17T08:20:35.372Z_

<details><summary>↩ Tool result · `toolu_014UWt3dTxFbSxrU6JEKtmdj`</summary>

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
11	FastForward~\cite{gautam2026fastforward} adds a 67.2M-parameter compensation network using BCE for mask prediction, adding inference latency.
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
28	\paragraph{Weight Pruning and Routing.}
29	Wanda~\cite{sun2024wanda} and SparseGPT~\cite{frantar2023sparsegpt} produce static weight masks via magnitude or reconstruction criteria; Switch Transformers~\cite{fedus2022switch} achieve conditional computation through learned expert routing.
30	Our method differs in generating dynamic per-token activation masks on unmodified dense models.
31	Sequence-level distillation~\cite{kim2016sequencekd} and DistilBERT~\cite{sanh2019distilbert} apply distributional matching to train compact students; we apply the same KL principle to train a sparsity predictor rather than a smaller model.
32	Our Gumbel-Sigmoid sampling builds on the Concrete distribution~\cite{maddison2017concrete} and $L_0$ regularization~\cite{louizos2018l0} for differentiable discrete optimization, adapted here to per-token activation prediction with a coupled objective.
33	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f38a1313-ec50-4af2-9d1c-07f059dea2a2",
  "isSidechain": false,
  "promptId": "e2bd2d71-d1a2-42f3-86c3-b3e33af96de1",
  "type": "user",
  "uuid": "bd704aaf-123c-4c34-b6f5-3122bc13ee7d",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/related_work.tex",
      "content": "\\section{Related Work}\n\n\\paragraph{Training-Free Activation Sparsity.}\nTEAL~\\cite{liu2025teal} applies global top-$k$ selection by activation magnitude, achieving 40--50\\% sparsity with no training cost.\nCATS~\\cite{lee2024cats} adapts per-layer thresholds for SiLU/SwiGLU activations; R-Sparse~\\cite{zhang2025rsparse} predicts sparsity from rank-aware SVD projections; DIP~\\cite{federici2025dip} combines dynamic input pruning with cache-aware masking.\nAll training-free methods determine masks from fixed statistics or input-independent criteria, while our predictor generates \\emph{input-dependent} masks trained to minimize output-distribution divergence.\n\n\\paragraph{Predictor-Based Contextual Sparsity.}\nDejaVu~\\cite{liu2023dejavu} introduced learned sparsity predictors trained via BCE to classify each neuron independently.\nShadowLLM~\\cite{akhauri2024shadowllm} uses attention-based routing with MSE supervision but retains per-neuron decomposition.\nFastForward~\\cite{gautam2026fastforward} adds a 67.2M-parameter compensation network using BCE for mask prediction, adding inference latency.\nPowerInfer~\\cite{song2024powerinfer} exploits power-law activation frequencies for GPU--CPU scheduling.\nMaskLLM~\\cite{fang2024maskllm} also employs learnable masks with Gumbel relaxation and frozen weights, but targets N:M semi-structured \\emph{weight} sparsity (2:4 patterns) via Gumbel-Softmax, producing fixed masks independent of input tokens.\nIn contrast, our method learns \\emph{activation} masks that are contextual (per-token), unstructured (budget-constrained global top-$k$), and trained with Gumbel-Sigmoid to minimize output-distribution divergence.\nAll prior predictor-based methods use decomposed (BCE) or intermediate (MSE) objectives where each neuron's gradient is independent of other mask states.\nOur \\emph{coupled} KL objective propagates gradients through all downstream layers, optimizing for global allocation quality without compensation.\n\n\\paragraph{Static Bias Correction.}\nSPON~\\cite{xu2026spon} learns input-independent bias vectors via closed-form KL minimization per layer, absorbed into weights at deployment.\nOur method is fundamentally different: a per-token contextual predictor trained end-to-end across all layers, producing input-dependent masks.\nSPON solves a static per-layer problem; we solve a global dynamic prediction problem. The two are near-orthogonal (cosine similarity 0.196; \\S\\ref{sec:experiments}).\n\n\\paragraph{Activation Function Engineering.}\nReLU Strikes Back~\\cite{mirzadeh2024relu} replaces SiLU with ReLU for $>$90\\% natural sparsity; TurboSparse~\\cite{song2024turbosparse} and ProSparse~\\cite{song2025prosparse} engineer extreme sparsity through activation modifications; the Sparsing Law~\\cite{luo2024sparsinglaw} formalizes how activation density increases with training compute.\nMiniTron~\\cite{muralidharan2024minitron} combines structured pruning with distillation but modifies architecture permanently.\nAll require retraining or weight modification; our method is a plug-in predictor on \\emph{unmodified} SwiGLU models.\n\n\\paragraph{Weight Pruning and Routing.}\nWanda~\\cite{sun2024wanda} and SparseGPT~\\cite{frantar2023sparsegpt} produce static weight masks via magnitude or reconstruction criteria; Switch Transformers~\\cite{fedus2022switch} achieve conditional computation through learned expert routing.\nOur method differs in generating dynamic per-token activation masks on unmodified dense models.\nSequence-level distillation~\\cite{kim2016sequencekd} and DistilBERT~\\cite{sanh2019distilbert} apply distributional matching to train compact students; we apply the same KL principle to train a sparsity predictor rather than a smaller model.\nOur Gumbel-Sigmoid sampling builds on the Concrete distribution~\\cite{maddison2017concrete} and $L_0$ regularization~\\cite{louizos2018l0} for differentiable discrete optimization, adapted here to per-token activation prediction with a coupled objective.\n",
      "numLines": 33,
      "startLine": 1,
      "totalLines": 33
    }
  },
  "sourceToolAssistantUUID": "f38a1313-ec50-4af2-9d1c-07f059dea2a2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/review_reviewer_1_772f066c",
  "sessionId": "fd7408d6-e7e0-4bb4-8dde-4202758b928d",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool result

_source line 83 · 2026-05-17T08:20:35.067Z_

<details><summary>↩ Tool result · `toolu_015zShvfH5yGg2xrhtv6qXsD`</summary>

```text
1	Activation sparsity reduces the effective computation in SwiGLU-based LLMs by pruning FFN neurons at inference, but existing learned predictors trained with binary cross-entropy (BCE) require error compensation networks due to a structural mismatch: BCE decomposes per neuron while inference uses global top-$k$ allocation across all layers.
2	We train lightweight predictors (2.37M parameters per layer, 75.9M total, $<$1\% of the base model) with KL divergence, which couples all neurons through the output distribution via Gumbel-Sigmoid relaxation, eliminating the need for compensation.
3	On LLaMA-3.1-8B (WikiText-2), our KL-trained predictor achieves perplexity 11.79 at 50\% sparsity without compensation, compared to 23.31 for vanilla TEAL and 27.97 for BCE trained at 2.71$\times$ the compute budget, whose loss saturates, confirming a structural rather than computational failure.
4	Three-seed evaluation confirms training stability (PPL $11.92 \pm 0.07$, CV${<}$1\% under uniform allocation).
5	The KL advantage grows disproportionately with sparsity: 18\% relative improvement at 30\%, 49\% at 50\%, and 82\% at 70\% (PPL 17.91 vs.\ 100.11); KL itself incurs $2.93\times$ the dense baseline, demonstrating substantial output fidelity even at extreme sparsity.
6	Cross-architecture evaluation on Mistral-7B-v0.3 confirms the advantage transfers across SwiGLU architectures at the 7--8B parameter scale, with consistent KL-over-TEAL ratios (within 7\% at $\leq$50\% sparsity).
7	SPON's static bias correction proves near-orthogonal to the predictor (cosine similarity 0.196), providing only 2.4\% relative PPL improvement (12.08$\to$11.79 under \texttt{evaluate.py}).
8	We propose a two-dimensional taxonomy over correction granularity $\times$ training signal coupling that unifies prior methods and identify three distinct sparsity regimes (budget-surplus, budget-constrained, and capacity-limited) that govern the quality-sparsity tradeoff.
9	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "91c29ca2-3c1a-4952-a5a6-627f5c095632",
  "isSidechain": false,
  "promptId": "e2bd2d71-d1a2-42f3-86c3-b3e33af96de1",
  "type": "user",
  "uuid": "734117d1-61ca-411f-81dc-b06ef8e71400",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/abstract.tex",
      "content": "Activation sparsity reduces the effective computation in SwiGLU-based LLMs by pruning FFN neurons at inference, but existing learned predictors trained with binary cross-entropy (BCE) require error compensation networks due to a structural mismatch: BCE decomposes per neuron while inference uses global top-$k$ allocation across all layers.\nWe train lightweight predictors (2.37M parameters per layer, 75.9M total, $<$1\\% of the base model) with KL divergence, which couples all neurons through the output distribution via Gumbel-Sigmoid relaxation, eliminating the need for compensation.\nOn LLaMA-3.1-8B (WikiText-2), our KL-trained predictor achieves perplexity 11.79 at 50\\% sparsity without compensation, compared to 23.31 for vanilla TEAL and 27.97 for BCE trained at 2.71$\\times$ the compute budget, whose loss saturates, confirming a structural rather than computational failure.\nThree-seed evaluation confirms training stability (PPL $11.92 \\pm 0.07$, CV${<}$1\\% under uniform allocation).\nThe KL advantage grows disproportionately with sparsity: 18\\% relative improvement at 30\\%, 49\\% at 50\\%, and 82\\% at 70\\% (PPL 17.91 vs.\\ 100.11); KL itself incurs $2.93\\times$ the dense baseline, demonstrating substantial output fidelity even at extreme sparsity.\nCross-architecture evaluation on Mistral-7B-v0.3 confirms the advantage transfers across SwiGLU architectures at the 7--8B parameter scale, with consistent KL-over-TEAL ratios (within 7\\% at $\\leq$50\\% sparsity).\nSPON's static bias correction proves near-orthogonal to the predictor (cosine similarity 0.196), providing only 2.4\\% relative PPL improvement (12.08$\\to$11.79 under \\texttt{evaluate.py}).\nWe propose a two-dimensional taxonomy over correction granularity $\\times$ training signal coupling that unifies prior methods and identify three distinct sparsity regimes (budget-surplus, budget-constrained, and capacity-limited) that govern the quality-sparsity tradeoff.\n",
      "numLines": 9,
      "startLine": 1,
      "totalLines": 9
    }
  },
  "sourceToolAssistantUUID": "91c29ca2-3c1a-4952-a5a6-627f5c095632",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/review_reviewer_1_772f066c",
  "sessionId": "fd7408d6-e7e0-4bb4-8dde-4202758b928d",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 84 · 2026-05-17T08:20:35.364Z_

<details open><summary>🔧 Tool call — Read · `toolu_014UWt3dTxFbSxrU6JEKtmdj`</summary>

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
  "parentUuid": "734117d1-61ca-411f-81dc-b06ef8e71400",
  "isSidechain": false,
  "requestId": "req_011Cb7pBNw8CPcG7LiVxFMWy",
  "type": "assistant",
  "uuid": "f38a1313-ec50-4af2-9d1c-07f059dea2a2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/review_reviewer_1_772f066c",
  "sessionId": "fd7408d6-e7e0-4bb4-8dde-4202758b928d",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013bnKh968uPS2dUUmKsfeMx",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 61680,
      "cache_read_input_tokens": 11841,
      "output_tokens": 2041,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 61680,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 2041,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 61680,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 61680
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "messages_changed",
        "cache_missed_input_tokens": 47015
      }
    }
  }
}
```

</details>

---

### Runtime record

_source line 85 · 2026-05-17T08:20:35.423Z_

```json
{
  "parentUuid": "bd704aaf-123c-4c34-b6f5-3122bc13ee7d",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "180c0e31-14a7-4467-8dbb-bc83a954bff8",
  "timestamp": "2026-05-17T08:20:35.423Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/review_reviewer_1_772f066c",
  "sessionId": "fd7408d6-e7e0-4bb4-8dde-4202758b928d",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

---

### Runtime record

_source line 86_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[Round 1 审稿请求]: 以下是 Reviewer 2 的完整审稿意见，请逐条回应：对每个 Must-Fix / Should-Fix / 小问题，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。  ---  ## Reviewer 2 — Round 1 审稿意见（新颖性 + 完整性）  ### 总体评分…",
  "leafUuid": "180c0e31-14a7-4467-8dbb-bc83a954bff8",
  "sessionId": "fd7408d6-e7e0-4bb4-8dde-4202758b928d"
}
```

---

### Runtime record

_source line 87_

```json
{
  "type": "ai-title",
  "aiTitle": "Review paper on sparse SwiGLU distillation methods",
  "sessionId": "fd7408d6-e7e0-4bb4-8dde-4202758b928d"
}
```

---

### Assistant

_source line 88 · 2026-05-17T08:21:15.900Z_

<details><summary>Logged reasoning block</summary>

```text
Now let me re-read the key tables and sections to prepare my response. I have all the information I need. Let me compose my cross-review.

Let me carefully go through each R2 issue:

**R2-N1: Responsible NLP Research Checklist missing**
I didn't check for this in my review. Looking at main.tex, there's no \input{checklist} or similar. ARR does require this since late 2024. This is a valid procedural concern that could lead to desk rejection. [AGREE].

**R2-N2: Downstream metrics vs PPL narrative**


This directly aligns with my own N2. The specific data point R2 raises is particularly striking—MMLU performs worse under KL global (25.27%) than TEAL vanilla (38.61%) at 30%—and I should have emphasized this discrepancy more strongly. [AGREE].

**R2-N3: MaskLLM overlap**
Looking at the technical details, both approaches use frozen weights with learnable Gumbel masks and KL divergence, but they differ in their sparsity targets—MaskLLM enforces static N:M weight sparsity while this paper takes a different approach.

R2 argues the core pipeline is essentially the same, just applied differently, which has some merit. However, the gradient analysis in §3.5 examining the structural mismatch between BCE and KL is novel to this contextual+global-top-k setting, something MaskLLM doesn't encounter since it doesn't face the same structural mismatch problem.

I should acknowledge R2's valid point about insufficient discussion of the methodology overlap, but push back on the claim of core technical equivalence. R2's specific questions about why Gumbel-Sigmoid over Gumbel-Softmax, whether MaskLLM implicitly solves the structural mismatch, and whether input-dependent masks in MaskLLM would be equivalent to this approach—these are fair and the paper should address them directly.

However, the fundamental differences are real: MaskLLM operates within fixed N:M groups while this approach uses global top-k allocation across all layers, and making MaskLLM's masks input-dependent wouldn't create equivalence because the allocation mechanism itself is different. The gradient analysis here is also specific to the end-to-end contextual setting.

On the regime analysis point, R2 has a valid concern—six data points across two models and three sparsity levels is thin evidence for claiming distinct regimes. The non-monotonic finding is interesting, but I should acknowledge the evidence doesn't fully support the strength of the claim being made.

D2DMoE is a legitimate omission from the taxonomy. It trains routers with ℓ2-norm regression to predict expert contribution and does per-token prediction with intermediate supervision, which fills a gap in the framework. The abstract is also overloaded with numbers—I count over 25 percentages and metrics crammed in, which reads more like a compressed results section than a coherent story. And the wall-clock speedup issue aligns with my earlier concern about practical efficiency gains.

On the taxonomy itself, the five empty cells out of nine are worth noting, but the axes capture meaningful distinctions. The concern about post-hoc rationalization has some merit, though the framework does organize the space in a useful way—though there's an inconsistency where DejaVu appears in the taxonomy table but isn't discussed in the main text.

I can't verify the WAS reference from EMNLP 2025, so I'll flag that as uncertain. The other minor issues check out: the abstract's -ing phrases, bibliography year inconsistencies, DejaVu's absence from the baseline comparisons, the figure label mismatch, and the conclusion being too brief all seem valid.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "180c0e31-14a7-4467-8dbb-bc83a954bff8",
  "isSidechain": false,
  "requestId": "req_011Cb7pEjGq4FWjfycbEcEWx",
  "type": "assistant",
  "uuid": "691b7374-0fa3-421b-b921-40bb7360555c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/review_reviewer_1_772f066c",
  "sessionId": "fd7408d6-e7e0-4bb4-8dde-4202758b928d",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RRBXef8EvFFBE6ufRrL53S",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3933,
      "cache_read_input_tokens": 73521,
      "output_tokens": 4658,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3933,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 4658,
          "cache_read_input_tokens": 73521,
          "cache_creation_input_tokens": 3933,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3933
          },
          "type": "message"
        }
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

_source line 89 · 2026-05-17T08:21:16.033Z_

已确认所有相关段落。下面提交交叉回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "691b7374-0fa3-421b-b921-40bb7360555c",
  "isSidechain": false,
  "requestId": "req_011Cb7pEjGq4FWjfycbEcEWx",
  "type": "assistant",
  "uuid": "f23f2f59-5186-40b5-be1d-fe0d30f0bf42",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/review_reviewer_1_772f066c",
  "sessionId": "fd7408d6-e7e0-4bb4-8dde-4202758b928d",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RRBXef8EvFFBE6ufRrL53S",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3933,
      "cache_read_input_tokens": 73521,
      "output_tokens": 4658,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3933,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 4658,
          "cache_read_input_tokens": 73521,
          "cache_creation_input_tokens": 3933,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3933
          },
          "type": "message"
        }
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

_source line 90 · 2026-05-17T08:22:21.835Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director · `toolu_018bmyxUDCgb7MV5iiAa4o1k`</summary>

```json
{
  "text": "\n# Reviewer 1 对 Reviewer 2 Round 1 意见的交叉回应\n\n---\n\n## Must-Fix 问题\n\n### [AGREE] R2-N1: Responsible NLP Research Checklist 缺失\n\n同意。我在 Round 1 审稿中遗漏了这一检查。main.tex 中确无 checklist 或 Ethics Statement。ARR 自 2024-12 起强制要求，缺失确实构成 desk rejection 风险。这是纯粹的格式合规问题，作者应立即补充。\n\n---\n\n### [AGREE] R2-N2: Downstream metrics 与 PPL-centric 叙事系统性矛盾\n\n强烈同意，这与我自己的 N2 一致。R2 进一步指出了一个我未充分强调的关键数据点：**30% sparsity 下 KL global 的 MMLU (25.27%) 比 TEAL vanilla (38.61%) 低 13.3pp**（Table 2）。这意味着 KL predictor 在 PPL 维度改善的同时，MMLU 反而显著恶化，KL 训练可能过度优化 token prediction 分布而牺牲了知识保留。\n\n补充我的观察：Table 4 (§4.4) 显示 KL uniform 在 30% 时恢复 MMLU 到 40.61%（+15.3pp over global），说明问题可能不在 KL 训练本身，而在 global top-k allocation 对 late layers（logit-forming layers）的 starvation 效应。§4.4 提到 \"L31 retention 28.4%\"，知识密集层被剥夺 budget 是 MMLU 崩溃的直接原因。但论文对此的讨论仅限于 regime analysis（§4.4），未反映到 Abstract/Introduction 的核心叙事中——R2 的 \"自相矛盾\" 判断准确。\n\n---\n\n### [REBUT] R2-N3: 与 MaskLLM 核心技术重叠\n\n**部分同意论文讨论不足，但不同意\"核心技术重叠\"的判断。**\n\nR2 正确指出 Related Work (§5 第2段) 对 MaskLLM 的区分过于简略——仅以 \"weight vs activation, static vs contextual\" 一笔带过。论文确实应更深入讨论方法论层面的联系。但 R2 将两者描述为 \"核心 pipeline 相同\" 忽略了关键的结构差异：\n\n1. **优化问题本质不同。** MaskLLM 学习 static masks（每个 N:M group 内选哪些 weight 保留），优化空间是 $\\binom{M}{N}$ 的 categorical distribution per group。本文学习 per-token contextual masks（每个 input position 独立决定哪些 neurons 保留），优化空间是 $\\{0,1\\}^{L \\times d_{ff}}$ 的 combinatorial space，受 global budget constraint。MaskLLM 没有 \"structural mismatch\" 问题——它的 masks 在训练和推理中都是 group-local 的，不存在 per-element 训练 vs. global allocation 推理的矛盾。\n\n2. **本文的核心贡献不是 \"KL + Gumbel\" pipeline 本身，而是 §3.5 的梯度分析。** Factor (a)-(d) 分解证明了 per-neuron BCE 和 end-to-end KL 在 contextual prediction + global top-k 设定下的结构性差异（factor (b) 的 downstream Jacobian 耦合）。这个分析对 MaskLLM 不适用——MaskLLM 的 masks 是 input-independent 的，不涉及 contextual prediction 的 gradient flow。\n\n3. **R2 的第三个问题 \"如果 MaskLLM 改为 input-dependent 是否等价\" 值得讨论**，但答案是否定的：(a) MaskLLM 用 Gumbel-Softmax 在 N:M group 内做 categorical selection，本文用 Gumbel-Sigmoid 做 binary per-neuron decisions + global budget constraint——relaxation 机制不同；(b) MaskLLM 的 allocation 是 per-group structured (2:4)，本文是 unstructured global top-k——inference protocol 不同；(c) 即使改为 input-dependent，MaskLLM 的 per-group 结构不产生 global coupling 问题。\n\n**结论：同意论文应更充分讨论 MaskLLM（especially 技术原因 for Gumbel-Softmax vs Sigmoid），但 \"核心技术重叠\" 的判断不成立。本文的核心新颖性在于 structural mismatch 的识别和梯度分析（§3.5），这在 MaskLLM 的设定中不存在。** 建议作者添加一段专门的 MaskLLM 技术对比。\n\n---\n\n## Should-Fix 问题\n\n### [AGREE] R2-W1: 三 regime 分析证据不足\n\n同意。2 models × 3 sparsity levels = 6 个数据点。具体 regime 边界（≤30%, ~40%, ≥50%）的泛化性完全未验证。这与我的 W4（实验规模受限）一致。作为 Contribution 之一呈现，claim 强度应降低为 \"empirical observation on 7-8B models\" 而非 general framework。补充：regime 边界可能与模型规模、架构、预训练数据量密切相关，论文未讨论这些 confounds。\n\n---\n\n### [AGREE] R2-W2: D2DMoE 遗漏\n\n同意。如果 D2DMoE (NeurIPS 2024) 使用 ℓ2-norm regression（intermediate objective）进行 per-token router training，它应填入 Table 1 的 Per-token × Intermediate cell（当前为空）。这不仅是引用遗漏，还影响 taxonomy 的完整性——本文 claim \"no prior work has combined per-token contextual prediction with a coupled training signal\"（§3.6 末段），但 taxonomy 中应先确认所有 cell 的 occupancy 状态。\n\n---\n\n### [AGREE] R2-W3: Abstract 数据堆砌\n\n同意。我统计 Abstract 中至少有 **25 个数字/百分比**（2.37M, 75.9M, <1%, 11.79, 50%, 23.31, 27.97, 2.71×, 11.92±0.07, CV<1%, 18%, 30%, 49%, 50%, 82%, 70%, 17.91, 100.11, 2.93×, 7-8B, 7%, ≤50%, 0.196, 2.4%, 12.08→11.79）。审稿人在 30 秒内无法从中提取核心信息。按照 ACL 论文写作规范，Abstract 应以叙事为主、最多引用 2-3 个关键数字。当前 Abstract 更像 Results 的压缩版，不是独立的故事。\n\n---\n\n### [AGREE] R2-W4: 无实际 wall-clock speedup\n\n同意，与我的 N1 一致。Appendix A Table 6 明确显示 +6.4% overhead。\n\n---\n\n### [AGREE] R2-W5: Taxonomy 可能 post-hoc rationalization\n\n部分同意。5/9 cells 空的确引发 post-hoc 质疑，尤其是两个轴恰好让本文独占一 cell。但我认为两个轴本身有独立的组织价值（correction granularity 和 training signal coupling 是文献中可辨认的真实维度），因此判断为 \"presentation concern\" 而非 \"validity concern\"。\n\n补充：R2 指出 DejaVu 在 Table 1 中被归类但 Table 2 中缺失——这确实是一个重要遗漏。如果 DejaVu 是 Per-token × Decomposed 的代表方法，它应该作为 baseline 出现在实验对比中。当前 Table 2 的 BCE baseline 未说明是否等同于 DejaVu 的实现。\n\n---\n\n### [REBUT] R2-W6: WAS (EMNLP 2025) 可能遗漏\n\n无法确认。R2 未提供 WAS 的完整标题、作者或链接。如果 R2 能提供具体引用信息，我可以评估其与本文的相关性。仅凭缩写无法判断是否确实是重要遗漏。\n\n---\n\n## 小问题\n\n**[AGREE]** Abstract -ing 分词短语。Abstract 确有多处 -ing 结尾：\"eliminating the need for compensation\", \"confirming a structural rather than computational failure\", \"confirming training stability\", \"demonstrating substantial output fidelity\"。这是典型的 AI 写作标志，应改写。\n\n**[AGREE]** xu2026spon bib year 不一致。references.bib 中 `year = {2026}`，如果 OpenAlex 显示 2025，应核实论文实际发表/接收年份。\n\n**[AGREE]** Table 2 缺 DejaVu。如 W5 中所述，taxonomy 中提到的方法应尽可能出现在实验对比中。\n\n**[AGREE]** Figure 1 label 为 `fig:taxonomy` 但内容是 method overview。§3.6 最后一段 \"Figure~\\ref{fig:taxonomy}\" 引用的是 Figure 1（method overview），但 taxonomy 实际在 Table 1。标签应改为 `fig:overview` 或类似。\n\n**[AGREE]** Conclusion 仅 3 行过短。§6 只有一段（conclusion.tex 仅 6 行 LaTeX），没有 future work discussion、没有 broader implications。对于一篇 long paper 这不符合预期。\n\n---\n\n## 对 R2 总体判断的评价\n\nR2 给出 Overall 3.0/5 (Findings)，与我的判断一致。R2 的新颖性质疑（R2-N3 MaskLLM overlap）是本次评审的核心分歧点。我的立场是：方法论工具确实不新（KL + Gumbel），但 structural mismatch 的识别和梯度分析（§3.5）是本文真正的贡献所在，这在 MaskLLM 的设定中不存在。论文应通过更充分的 MaskLLM 对比来突出这一点。\n\nR2 的 checklist 缺失（R2-N1）和 D2DMoE 遗漏（R2-W2）是我 Round 1 遗漏的有价值发现。Abstract 数据堆砌（R2-W3）的具体量化（18+ 数字）也比我更到位。\n\n两位 Reviewer 一致认为的核心问题：(1) downstream collapse vs PPL framing 矛盾，(2) 无 wall-clock speedup，(3) 实验规模有限。这三点是决定接收/拒绝的关键。\n",
  "reviewer_id": "1",
  "project": "distill_sparse_swiglu"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f23f2f59-5186-40b5-be1d-fe0d30f0bf42",
  "isSidechain": false,
  "requestId": "req_011Cb7pEjGq4FWjfycbEcEWx",
  "type": "assistant",
  "uuid": "7daf8354-5dec-41fd-b424-3537795c051e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/review_reviewer_1_772f066c",
  "sessionId": "fd7408d6-e7e0-4bb4-8dde-4202758b928d",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RRBXef8EvFFBE6ufRrL53S",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3933,
      "cache_read_input_tokens": 73521,
      "output_tokens": 4658,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3933,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 4658,
          "cache_read_input_tokens": 73521,
          "cache_creation_input_tokens": 3933,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3933
          },
          "type": "message"
        }
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

_source line 91 · 2026-05-17T08:22:25.687Z_

<details><summary>↩ Tool result · `toolu_018bmyxUDCgb7MV5iiAa4o1k`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director\"}, \"error\": \"\"}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7daf8354-5dec-41fd-b424-3537795c051e",
  "isSidechain": false,
  "promptId": "e2bd2d71-d1a2-42f3-86c3-b3e33af96de1",
  "type": "user",
  "uuid": "e5c0bb91-b894-4d68-9bea-4f95cb244f52",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"review_director_key\\\": \\\"feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director\\\"}, \\\"error\\\": \\\"\\\"}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director\"}, \"error\": \"\"}"
    }
  },
  "sourceToolAssistantUUID": "7daf8354-5dec-41fd-b424-3537795c051e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/review_reviewer_1_772f066c",
  "sessionId": "fd7408d6-e7e0-4bb4-8dde-4202758b928d",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---
