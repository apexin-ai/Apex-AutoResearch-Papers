# Research conversation: [Round 1 审稿请求]: ## 交叉分享：Reviewer 2 的完整 Round 1 审稿意见 请逐条回应 Reviewer 2 的每个问题：用 [AGREE] 表示同意并说明理由，或 [REBUT] 表示反驳并引用论文具体 Sec

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 58
- **Recorded user turns:** 1
- **Tool calls:** 17
- **Original source:** `logs/chats/exported-trajectories/account-3/cd3ac2da-cdcc-4c5b-9409-914107331cb2.jsonl`
- **Structured JSON:** [`b00c41ba95df15ca38e9.json`](../../sessions/b0/b00c41ba95df15ca38e9.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-15T01:58:14.466Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-15T01:58:14.466Z",
  "sessionId": "cd3ac2da-cdcc-4c5b-9409-914107331cb2",
  "content": "[Round 1 审稿请求]:\n## 交叉分享：Reviewer 2 的完整 Round 1 审稿意见\n\n请逐条回应 Reviewer 2 的每个问题：用 [AGREE] 表示同意并说明理由，或 [REBUT] 表示反驳并引用论文具体 Section/Table/Figure 作为证据。\n\n---\n\n以下是 Reviewer 2 的完整审稿原文：\n\n### 总体评分\n**Overall**: 3.0/5（Findings track acceptance）\n**Soundness**: 3.5/5 | **Excitement**: 2.5/5 | **Reproducibility**: 4.0/5\n**Confidence**: 4/5\n\n### 核心判断\n论文选择了有价值的研究问题，实验设计合理、统计检验到位。但作为 EMNLP 主会长文有三个核心不足：\n\n### Must-Fix 问题 (3 个)\n\n**N1** [critical] \"Correlation-selection gap\" 的解释力不足——4/5 个 signals 是 instance-level 的，它们不能做 per-sample selection 是定义上的必然结果，不是发现。真正需要深入分析的是唯一的 per-sample signal (logprob) 为何也失败（calibration? length bias? constrained decoding 干扰?），但论文对此几乎没有分析。\n\n**N2** [critical] Per-sample signal 探索严重不足——5 个 signals 中只有 logprob 1 个能做 per-sample selection，论文却声称 \"systematic comparison\"。LOO-SJ 已在 Appendix D 计算（Δρ=-0.014），但未测试其 selection 能力——这是一个自然的 per-sample structural signal。Consensus-proximity ranking 也未被分析。\n\n**N3** [critical] 对 Nedellec et al. (2026) 的增量贡献论证不足。三个区分点中：selection 结论是负面的、multi-domain 是标准做法、SJ 的优势不一致（CoNLL 上 EM > SJ，conditional filtering 后 EM > SJ）。\n\n### Should-Fix 问题 (5 个)\n- W1: \"first systematic evaluation\" claim 过强，需收窄 scope\n- W2: 遗漏 Singer et al. (2026) conformal prediction for NER（arXiv:2601.16999）和 ICLR 2025 conformal structured prediction\n- W3: 遗漏 \"Optimal Self-Consistency\" (arXiv:2511.12309) 和 \"Difficulty-Adaptive SC\" (NAACL 2025 Findings)\n- W4: 实验规模偏小（仅 8B 模型、1 个 RE benchmark、LoRA fine-tuned 非典型 generative IE 设置）\n- W5: ρ-AUROC dissociation 机制分析浅，主文应明确 EM=1 同时包含 all-correct 和 all-wrong 的压缩效应\n\n### 引用真实性\n46 篇中 43 篇验证通过。`nedellec2026consistency` 第一作者应为 Yao 而非 Nédellec，论文中 \"Nedellec et al.\" 引用有误。`lightman2024verify` 和 `hobelsberger2025systematic` 未匹配但属 API 问题，实质上是真实论文。\n\n### 遗漏重要引用\n1. Singer et al. (2026) \"UQ for NER via Conformal Prediction\"\n2. Conformal Structured Prediction (ICLR 2025)\n3. Optimal Self-Consistency (arXiv:2511.12309)\n4. Difficulty-Adaptive Self-Consistency (NAACL 2025 Findings)\n5. Generative Self-Aggregation (arXiv:2503.04104)\n\n### 审稿判断\n当前版本更适合 Findings track。如能深入分析 per-sample signal failure 原因、测试 LOO-SJ 等 per-sample structural signals、讨论 constrained decoding 影响，可提升至主会水准。"
}
```

---

### Runtime record

_source line 2 · 2026-05-15T01:58:14.469Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-15T01:58:14.469Z",
  "sessionId": "cd3ac2da-cdcc-4c5b-9409-914107331cb2"
}
```

---

## Round 1

56 recorded events

### User

_source line 3 · 2026-05-15T01:58:14.503Z_

[Round 1 审稿请求]:
## 交叉分享：Reviewer 2 的完整 Round 1 审稿意见

请逐条回应 Reviewer 2 的每个问题：用 [AGREE] 表示同意并说明理由，或 [REBUT] 表示反驳并引用论文具体 Section/Table/Figure 作为证据。

---

以下是 Reviewer 2 的完整审稿原文：

### 总体评分
**Overall**: 3.0/5（Findings track acceptance）
**Soundness**: 3.5/5 | **Excitement**: 2.5/5 | **Reproducibility**: 4.0/5
**Confidence**: 4/5

### 核心判断
论文选择了有价值的研究问题，实验设计合理、统计检验到位。但作为 EMNLP 主会长文有三个核心不足：

### Must-Fix 问题 (3 个)

**N1** [critical] "Correlation-selection gap" 的解释力不足——4/5 个 signals 是 instance-level 的，它们不能做 per-sample selection 是定义上的必然结果，不是发现。真正需要深入分析的是唯一的 per-sample signal (logprob) 为何也失败（calibration? length bias? constrained decoding 干扰?），但论文对此几乎没有分析。

**N2** [critical] Per-sample signal 探索严重不足——5 个 signals 中只有 logprob 1 个能做 per-sample selection，论文却声称 "systematic comparison"。LOO-SJ 已在 Appendix D 计算（Δρ=-0.014），但未测试其 selection 能力——这是一个自然的 per-sample structural signal。Consensus-proximity ranking 也未被分析。

**N3** [critical] 对 Nedellec et al. (2026) 的增量贡献论证不足。三个区分点中：selection 结论是负面的、multi-domain 是标准做法、SJ 的优势不一致（CoNLL 上 EM > SJ，conditional filtering 后 EM > SJ）。

### Should-Fix 问题 (5 个)
- W1: "first systematic evaluation" claim 过强，需收窄 scope
- W2: 遗漏 Singer et al. (2026) conformal prediction for NER（arXiv:2601.16999）和 ICLR 2025 conformal structured prediction
- W3: 遗漏 "Optimal Self-Consistency" (arXiv:2511.12309) 和 "Difficulty-Adaptive SC" (NAACL 2025 Findings)
- W4: 实验规模偏小（仅 8B 模型、1 个 RE benchmark、LoRA fine-tuned 非典型 generative IE 设置）
- W5: ρ-AUROC dissociation 机制分析浅，主文应明确 EM=1 同时包含 all-correct 和 all-wrong 的压缩效应

### 引用真实性
46 篇中 43 篇验证通过。`nedellec2026consistency` 第一作者应为 Yao 而非 Nédellec，论文中 "Nedellec et al." 引用有误。`lightman2024verify` 和 `hobelsberger2025systematic` 未匹配但属 API 问题，实质上是真实论文。

### 遗漏重要引用
1. Singer et al. (2026) "UQ for NER via Conformal Prediction"
2. Conformal Structured Prediction (ICLR 2025)
3. Optimal Self-Consistency (arXiv:2511.12309)
4. Difficulty-Adaptive Self-Consistency (NAACL 2025 Findings)
5. Generative Self-Aggregation (arXiv:2503.04104)

### 审稿判断
当前版本更适合 Findings track。如能深入分析 per-sample signal failure 原因、测试 LOO-SJ 等 per-sample structural signals、讨论 constrained decoding 影响，可提升至主会水准。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "e032b776-5e54-467c-9321-aeb2f2c75513",
  "type": "user",
  "uuid": "f614c187-ee95-44f4-877a-127a767b6747",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_1_68ddc296",
  "sessionId": "cd3ac2da-cdcc-4c5b-9409-914107331cb2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-15T01:58:14.503Z_

```json
{
  "parentUuid": "f614c187-ee95-44f4-877a-127a767b6747",
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
  "uuid": "508ed86c-89ac-4db5-a377-1972de95a642",
  "timestamp": "2026-05-15T01:58:14.503Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_1_68ddc296",
  "sessionId": "cd3ac2da-cdcc-4c5b-9409-914107331cb2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-15T01:58:14.503Z_

```json
{
  "parentUuid": "508ed86c-89ac-4db5-a377-1972de95a642",
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
  "uuid": "f5886272-3e49-475f-876e-6c9bb5c3b983",
  "timestamp": "2026-05-15T01:58:14.503Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_1_68ddc296",
  "sessionId": "cd3ac2da-cdcc-4c5b-9409-914107331cb2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 6 · 2026-05-15T01:58:14.503Z_

```json
{
  "parentUuid": "f5886272-3e49-475f-876e-6c9bb5c3b983",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "91cdfc7c-fa92-44ef-baad-63275c234f57",
  "timestamp": "2026-05-15T01:58:14.503Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_1_68ddc296",
  "sessionId": "cd3ac2da-cdcc-4c5b-9409-914107331cb2",
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
  "aiTitle": "Respond to EMNLP Reviewer 2 Round 1 comments",
  "sessionId": "cd3ac2da-cdcc-4c5b-9409-914107331cb2"
}
```

---

### Assistant

_source line 8 · 2026-05-15T01:58:19.845Z_

<details><summary>Logged reasoning block</summary>

```text
The user (acting as Review Director) is asking me (Reviewer 1) to respond to Reviewer 2's complete Round 1 review, point by point. I need to read the paper first to be able to provide informed responses.

Let me start by reading the paper PDF and understanding the content, then respond to each of Reviewer 2's points with [AGREE] or [REBUT] with evidence from the paper.

First, I need to load the necessary tools and read the paper.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "91cdfc7c-fa92-44ef-baad-63275c234f57",
  "isSidechain": false,
  "requestId": "req_011Cb3XTps3RY7HkRbfSMt4f",
  "type": "assistant",
  "uuid": "853d82b7-d319-4d61-a052-5f977c03f21b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_1_68ddc296",
  "sessionId": "cd3ac2da-cdcc-4c5b-9409-914107331cb2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RdDNuAJtBBVxjd2pT6xEWo",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14166,
      "cache_read_input_tokens": 11841,
      "output_tokens": 258,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 14166,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 258,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 14166,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 14166
          },
          "type": "message"
        }
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

_source line 9 · 2026-05-15T01:58:20.403Z_

我需要先阅读论文，然后逐条回应 Reviewer 2 的意见。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "853d82b7-d319-4d61-a052-5f977c03f21b",
  "isSidechain": false,
  "requestId": "req_011Cb3XTps3RY7HkRbfSMt4f",
  "type": "assistant",
  "uuid": "a5d43bae-c4a3-4ef1-92ba-b32fbec56f68",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_1_68ddc296",
  "sessionId": "cd3ac2da-cdcc-4c5b-9409-914107331cb2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RdDNuAJtBBVxjd2pT6xEWo",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14166,
      "cache_read_input_tokens": 11841,
      "output_tokens": 258,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 14166,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 258,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 14166,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 14166
          },
          "type": "message"
        }
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

_source line 10 · 2026-05-15T01:58:21.804Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01C4o4DY5MVgsZdjH1WgYp8e`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__review_reviewer_post_to_director",
  "max_results": 2
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a5d43bae-c4a3-4ef1-92ba-b32fbec56f68",
  "isSidechain": false,
  "requestId": "req_011Cb3XTps3RY7HkRbfSMt4f",
  "type": "assistant",
  "uuid": "0781ded9-4ce2-4bb7-8449-6674e77dc885",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_1_68ddc296",
  "sessionId": "cd3ac2da-cdcc-4c5b-9409-914107331cb2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RdDNuAJtBBVxjd2pT6xEWo",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14166,
      "cache_read_input_tokens": 11841,
      "output_tokens": 258,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 14166,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 258,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 14166,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 14166
          },
          "type": "message"
        }
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

_source line 11 · 2026-05-15T01:58:21.810Z_

<details><summary>↩ Tool result · `toolu_01C4o4DY5MVgsZdjH1WgYp8e`</summary>

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
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0781ded9-4ce2-4bb7-8449-6674e77dc885",
  "isSidechain": false,
  "promptId": "e032b776-5e54-467c-9321-aeb2f2c75513",
  "type": "user",
  "uuid": "db284800-0321-4ce1-ae44-f65c4ea2d7d8",
  "toolUseResult": {
    "matches": [
      "mcp__agent-ml-research__pdf_to_images",
      "mcp__agent-ml-research__review_reviewer_post_to_director"
    ],
    "query": "select:mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__review_reviewer_post_to_director",
    "total_deferred_tools": 23
  },
  "sourceToolAssistantUUID": "0781ded9-4ce2-4bb7-8449-6674e77dc885",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_1_68ddc296",
  "sessionId": "cd3ac2da-cdcc-4c5b-9409-914107331cb2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 12 · 2026-05-15T01:58:24.451Z_

正在读取论文，先查看论文源文件。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "db284800-0321-4ce1-ae44-f65c4ea2d7d8",
  "isSidechain": false,
  "requestId": "req_011Cb3XUMxpFEPte6aDFRimv",
  "type": "assistant",
  "uuid": "f8c54678-db8a-4fcd-b7df-103521ee721d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_1_68ddc296",
  "sessionId": "cd3ac2da-cdcc-4c5b-9409-914107331cb2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Fhe9hbwveD3e61twUWHFXQ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 921,
      "cache_read_input_tokens": 26007,
      "output_tokens": 205,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 921,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 205,
          "cache_read_input_tokens": 26007,
          "cache_creation_input_tokens": 921,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 921
          },
          "type": "message"
        }
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

_source line 13 · 2026-05-15T01:58:25.922Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01MoCBDfvzfwnUfHbh4wdaMk`</summary>

```json
{
  "pattern": "**/paper/main.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f8c54678-db8a-4fcd-b7df-103521ee721d",
  "isSidechain": false,
  "requestId": "req_011Cb3XUMxpFEPte6aDFRimv",
  "type": "assistant",
  "uuid": "7af54050-3265-4222-a8e2-8845af8c1b20",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_1_68ddc296",
  "sessionId": "cd3ac2da-cdcc-4c5b-9409-914107331cb2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Fhe9hbwveD3e61twUWHFXQ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 921,
      "cache_read_input_tokens": 26007,
      "output_tokens": 205,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 921,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 205,
          "cache_read_input_tokens": 26007,
          "cache_creation_input_tokens": 921,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 921
          },
          "type": "message"
        }
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

_source line 14 · 2026-05-15T01:58:25.958Z_

<details><summary>↩ Tool result · `toolu_01MoCBDfvzfwnUfHbh4wdaMk`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7af54050-3265-4222-a8e2-8845af8c1b20",
  "isSidechain": false,
  "promptId": "e032b776-5e54-467c-9321-aeb2f2c75513",
  "type": "user",
  "uuid": "f43dbcf7-d6a2-4089-a1fb-16e2182dde1c",
  "toolUseResult": {
    "filenames": [
      "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex"
    ],
    "durationMs": 24,
    "numFiles": 1,
    "truncated": false
  },
  "sourceToolAssistantUUID": "7af54050-3265-4222-a8e2-8845af8c1b20",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_1_68ddc296",
  "sessionId": "cd3ac2da-cdcc-4c5b-9409-914107331cb2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-15T01:58:26.545Z_

<details><summary>↩ Tool result · `toolu_01ToJ4HuAG7rbdLKCJbyzMwF`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/figures/paper/fig_overview.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/figures/paper/fig_selection_gap.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/exp010_selection_curves/figures/paper/fig_selection_curves.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/figures/paper/fig_signal_heatmap.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/figures/paper/fig_reliability.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/figures/paper/fig_selection_curves.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.pdf
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6f7d72a2-149b-4591-bc6c-7d329d088e1e",
  "isSidechain": false,
  "promptId": "e032b776-5e54-467c-9321-aeb2f2c75513",
  "type": "user",
  "uuid": "e41a0cc4-fc24-4a29-a48a-d1f155329182",
  "toolUseResult": {
    "filenames": [
      "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/figures/paper/fig_overview.pdf",
      "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/figures/paper/fig_selection_gap.pdf",
      "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/exp010_selection_curves/figures/paper/fig_selection_curves.pdf",
      "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/figures/paper/fig_signal_heatmap.pdf",
      "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/figures/paper/fig_reliability.pdf",
      "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/figures/paper/fig_selection_curves.pdf",
      "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.pdf"
    ],
    "durationMs": 31,
    "numFiles": 7,
    "truncated": false
  },
  "sourceToolAssistantUUID": "6f7d72a2-149b-4591-bc6c-7d329d088e1e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_1_68ddc296",
  "sessionId": "cd3ac2da-cdcc-4c5b-9409-914107331cb2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-15T01:58:26.505Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01ToJ4HuAG7rbdLKCJbyzMwF`</summary>

```json
{
  "pattern": "**/paper/*.pdf",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f43dbcf7-d6a2-4089-a1fb-16e2182dde1c",
  "isSidechain": false,
  "requestId": "req_011Cb3XUMxpFEPte6aDFRimv",
  "type": "assistant",
  "uuid": "6f7d72a2-149b-4591-bc6c-7d329d088e1e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_1_68ddc296",
  "sessionId": "cd3ac2da-cdcc-4c5b-9409-914107331cb2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Fhe9hbwveD3e61twUWHFXQ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 921,
      "cache_read_input_tokens": 26007,
      "output_tokens": 205,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 921,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 205,
          "cache_read_input_tokens": 26007,
          "cache_creation_input_tokens": 921,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 921
          },
          "type": "message"
        }
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

_source line 17 · 2026-05-15T01:58:28.955Z_

<details open><summary>🔧 Tool call — Read · `toolu_01AJWAKkQF6Umsqa4VALW2ZM`</summary>

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
  "parentUuid": "e41a0cc4-fc24-4a29-a48a-d1f155329182",
  "isSidechain": false,
  "requestId": "req_011Cb3XUiBF1zxPr13o4x3YU",
  "type": "assistant",
  "uuid": "7cb7ce01-6590-48cf-a6d8-b75d99265818",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_1_68ddc296",
  "sessionId": "cd3ac2da-cdcc-4c5b-9409-914107331cb2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019czngQwxVByPEmEtf8dQaR",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 599,
      "cache_read_input_tokens": 26928,
      "output_tokens": 89,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 599,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 89,
          "cache_read_input_tokens": 26928,
          "cache_creation_input_tokens": 599,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 599
          },
          "type": "message"
        }
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

_source line 18 · 2026-05-15T01:58:28.986Z_

<details><summary>↩ Tool result · `toolu_01AJWAKkQF6Umsqa4VALW2ZM`</summary>

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
  "parentUuid": "7cb7ce01-6590-48cf-a6d8-b75d99265818",
  "isSidechain": false,
  "promptId": "e032b776-5e54-467c-9321-aeb2f2c75513",
  "type": "user",
  "uuid": "73ac6186-f75b-41df-92b9-94ff38553c05",
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
  "sourceToolAssistantUUID": "7cb7ce01-6590-48cf-a6d8-b75d99265818",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_1_68ddc296",
  "sessionId": "cd3ac2da-cdcc-4c5b-9409-914107331cb2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-15T01:58:31.551Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01S4NdwK9ae8q91W1tX3teg8`</summary>

```json
{
  "pattern": "**/paper/sections/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "73ac6186-f75b-41df-92b9-94ff38553c05",
  "isSidechain": false,
  "requestId": "req_011Cb3XUtfmpM6pf3L738Dq4",
  "type": "assistant",
  "uuid": "4ee19b88-93bf-43c5-8681-207d664ecd88",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_1_68ddc296",
  "sessionId": "cd3ac2da-cdcc-4c5b-9409-914107331cb2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Bzfg37Fi8wydkLwZhKERTr",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 515,
      "cache_read_input_tokens": 27527,
      "output_tokens": 103,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 515,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 103,
          "cache_read_input_tokens": 27527,
          "cache_creation_input_tokens": 515,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 515
          },
          "type": "message"
        }
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

_source line 20 · 2026-05-15T01:58:31.577Z_

<details><summary>↩ Tool result · `toolu_01S4NdwK9ae8q91W1tX3teg8`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/abstract.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/conclusion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/limitations.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/method.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/introduction.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/related_work.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4ee19b88-93bf-43c5-8681-207d664ecd88",
  "isSidechain": false,
  "promptId": "e032b776-5e54-467c-9321-aeb2f2c75513",
  "type": "user",
  "uuid": "c4dffe6a-5ad6-421f-9b1d-13e85784082e",
  "toolUseResult": {
    "filenames": [
      "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/abstract.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/conclusion.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/limitations.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/method.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/introduction.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/related_work.tex"
    ],
    "durationMs": 17,
    "numFiles": 9,
    "truncated": false
  },
  "sourceToolAssistantUUID": "4ee19b88-93bf-43c5-8681-207d664ecd88",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_1_68ddc296",
  "sessionId": "cd3ac2da-cdcc-4c5b-9409-914107331cb2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 21_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[Round 1 审稿请求]: ## 交叉分享：Reviewer 2 的完整 Round 1 审稿意见  请逐条回应 Reviewer 2 的每个问题：用 [AGREE] 表示同意并说明理由，或 [REBUT] 表示反驳并引用论文具体 Section/Table/Figure 作为证据。  ---  以下是 Reviewer 2 的完整审稿原文：  ### 总体评分 **Overall**: 3.…",
  "leafUuid": "c4dffe6a-5ad6-421f-9b1d-13e85784082e",
  "sessionId": "cd3ac2da-cdcc-4c5b-9409-914107331cb2"
}
```

---

### Runtime record

_source line 22_

```json
{
  "type": "ai-title",
  "aiTitle": "Respond to EMNLP Reviewer 2 Round 1 comments",
  "sessionId": "cd3ac2da-cdcc-4c5b-9409-914107331cb2"
}
```

---

### Assistant

_source line 23 · 2026-05-15T01:58:34.098Z_

让我并行读取所有章节。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c4dffe6a-5ad6-421f-9b1d-13e85784082e",
  "isSidechain": false,
  "requestId": "req_011Cb3XV5nFmdPFxbozqtcYJ",
  "type": "assistant",
  "uuid": "30d7ffc4-0b69-49d3-ac1e-5c8fedab4c51",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_1_68ddc296",
  "sessionId": "cd3ac2da-cdcc-4c5b-9409-914107331cb2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011XmLzwn8kwEtrfPjAJSwkZ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 476,
      "cache_read_input_tokens": 28042,
      "output_tokens": 698,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 476,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 698,
          "cache_read_input_tokens": 28042,
          "cache_creation_input_tokens": 476,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 476
          },
          "type": "message"
        }
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

_source line 24 · 2026-05-15T01:58:34.581Z_

<details open><summary>🔧 Tool call — Read · `toolu_01CSkTdMYgA2jZRimfcHbxKq`</summary>

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
  "parentUuid": "30d7ffc4-0b69-49d3-ac1e-5c8fedab4c51",
  "isSidechain": false,
  "requestId": "req_011Cb3XV5nFmdPFxbozqtcYJ",
  "type": "assistant",
  "uuid": "64d28c13-9337-474c-a437-510b0c82a810",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_1_68ddc296",
  "sessionId": "cd3ac2da-cdcc-4c5b-9409-914107331cb2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011XmLzwn8kwEtrfPjAJSwkZ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 476,
      "cache_read_input_tokens": 28042,
      "output_tokens": 698,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 476,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 698,
          "cache_read_input_tokens": 28042,
          "cache_creation_input_tokens": 476,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 476
          },
          "type": "message"
        }
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

_source line 25 · 2026-05-15T01:58:34.586Z_

<details><summary>↩ Tool result · `toolu_01CSkTdMYgA2jZRimfcHbxKq`</summary>

```text
1	\begin{abstract}
2	Test-time scaling through multi-sample generation promises quality improvements for LLM-based information extraction, but which confidence signals best serve quality estimation versus sample selection remains unclear.
3	We systematically compare five confidence signals from three families---structural (entity voting, Soft Jaccard), surface (exact match, Fleiss' $\kappa$), and model-internal (log-probability)---across NER and relation extraction on three datasets (SciERC, CoNLL-2003, WNUT-17) with two model families (Qwen3-8B, LLaMA-3.1-8B).
4	We find that the strongest signals achieve $\rho{=}0.38$ (entity voting) and AUROC${=}0.75$ (exact match) for quality estimation, with ranking and classification favoring different signals across task complexity; however, this strong quality estimation does not translate into selection gains---no signal reliably surpasses greedy decoding on either task ($p{>}0.39$, bootstrap) despite 13--18~pp of oracle headroom.
5	We term this disconnect the \textit{correlation-selection gap}: instance-level consistency signals predict which inputs the model handles reliably, not which output is best among $N$ candidates.
6	Signal rankings further depend on task difficulty---exact match dominates easy tasks, structural signals dominate hard tasks, and all signals converge when model capability is insufficient---establishing that signal choice should be guided by task difficulty and intended application.
7	These results reframe consistency signals as quality estimators rather than output selectors for structured IE.
8	\end{abstract}
9	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "64d28c13-9337-474c-a437-510b0c82a810",
  "isSidechain": false,
  "promptId": "e032b776-5e54-467c-9321-aeb2f2c75513",
  "type": "user",
  "uuid": "664ab25e-be60-400f-a670-1b552d480783",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/abstract.tex",
      "content": "\\begin{abstract}\nTest-time scaling through multi-sample generation promises quality improvements for LLM-based information extraction, but which confidence signals best serve quality estimation versus sample selection remains unclear.\nWe systematically compare five confidence signals from three families---structural (entity voting, Soft Jaccard), surface (exact match, Fleiss' $\\kappa$), and model-internal (log-probability)---across NER and relation extraction on three datasets (SciERC, CoNLL-2003, WNUT-17) with two model families (Qwen3-8B, LLaMA-3.1-8B).\nWe find that the strongest signals achieve $\\rho{=}0.38$ (entity voting) and AUROC${=}0.75$ (exact match) for quality estimation, with ranking and classification favoring different signals across task complexity; however, this strong quality estimation does not translate into selection gains---no signal reliably surpasses greedy decoding on either task ($p{>}0.39$, bootstrap) despite 13--18~pp of oracle headroom.\nWe term this disconnect the \\textit{correlation-selection gap}: instance-level consistency signals predict which inputs the model handles reliably, not which output is best among $N$ candidates.\nSignal rankings further depend on task difficulty---exact match dominates easy tasks, structural signals dominate hard tasks, and all signals converge when model capability is insufficient---establishing that signal choice should be guided by task difficulty and intended application.\nThese results reframe consistency signals as quality estimators rather than output selectors for structured IE.\n\\end{abstract}\n",
      "numLines": 9,
      "startLine": 1,
      "totalLines": 9
    }
  },
  "sourceToolAssistantUUID": "64d28c13-9337-474c-a437-510b0c82a810",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_1_68ddc296",
  "sessionId": "cd3ac2da-cdcc-4c5b-9409-914107331cb2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-15T01:58:38.818Z_

<details><summary>↩ Tool result · `toolu_011HWcg5nkDiLWnjvKyxvQCC`</summary>

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
115	\paragraph{Evaluation circularity.}
116	Leave-one-out SJ (LOO-SJ), which excludes the target sample when computing confidence, yields $\Delta\rho{=}{-}0.014$ relative to standard SJ, with a maximum per-instance $\Delta\rho$ of $3.1{\times}10^{-4}$.
117	Evaluation circularity is negligible.
118	
119	\paragraph{Conditional filtering details.}
120	On LLaMA conditional RE (non-zero F1 instances), SJ recovers to $\rho{=}0.405$ while FK drops to $\rho{=}0.259$, confirming that structural advantage is robust across both models and evaluation conditions.
121	At $N{=}16$, the divergence persists: SJ maintains $\rho{=}0.308$ on conditional RE while logprob drops to $\rho{=}{-}0.026$.
122	EM ranks first across all four tested conditional configurations---SciERC NER ($\rho{=}0.360$), CoNLL Qwen $N{=}16$ ($\rho{=}0.466$), CoNLL LLaMA 3-seed ($\rho{=}0.462$), and SciERC RE ($\rho{=}0.417$)---despite full-set rankings ranging from \#1 (CoNLL Qwen) to \#5 (SciERC RE).
123	On the full set, EM is diluted by trivial agreement: instances where all $N$ samples produce identical (possibly incorrect) outputs receive EM${=}1$ regardless of quality, compressing the signal's dynamic range.
124	On the conditional set---where the model demonstrably produces varied outputs---exact agreement becomes the strongest quality signal.
125	The margin over SJ is largest on RE ($\Delta\rho{=}{+}0.171$), where compound extraction decisions amplify output variability, and smallest on CoNLL LLaMA ($\Delta\rho{=}{+}0.002$), where all signals converge near $\rho{\approx}0.46$.
126	
127	\paragraph{Diminishing returns of $N$-scaling.}
128	Our $N{=}8$ and $N{=}16$ comparisons (Table~\ref{tab:robustness}) characterize the marginal value of additional samples for test-time scaling \cite{brown2024monkeys, snell2024scaling}.
129	For quality estimation, structural signals benefit consistently but sublinearly: SJ $\rho$ improves by $+0.052$ (Qwen SciERC, 3-seed mean) and $+0.032$ (LLaMA CoNLL, 3-seed mean) when doubling from $N{=}8$ to $N{=}16$, while log-probability is approximately $N$-invariant ($\Delta\rho{\leq}0.021$).
130	Structural signals leverage $\binom{N}{2}$ pairwise comparisons (28 pairs at $N{=}8$, 120 at $N{=}16$), but the $\rho$ improvement is far less than proportional, indicating diminishing information per additional comparison.
131	This asymmetry gives structural signals a relative advantage in the compute-constrained regime: at $N{=}8$, SJ already achieves $\rho{=}0.431$ on LLaMA CoNLL (vs.\ logprob $\rho{=}0.307$, $\Delta{=}{+}0.124$), and the gap \textit{widens} at $N{=}16$ ($\Delta{=}{+}0.153$) because structural signals continue to benefit from additional pairwise evidence while logprob does not.
132	For sample selection, additional samples increase the oracle upper bound---more draws raise the probability of a high-quality candidate---but signal-based selection remains flat because the selector's inability to identify the best candidate is a granularity limitation, not a sample size limitation.
133	The practical implication is that $N{=}8$ captures most of the achievable quality estimation benefit; further scaling widens rather than closes the correlation-selection gap absent stronger per-sample selectors.
134	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c8ca4a1d-0879-4c24-a137-5a49c59ed02a",
  "isSidechain": false,
  "promptId": "e032b776-5e54-467c-9321-aeb2f2c75513",
  "type": "user",
  "uuid": "7288de24-9ac3-466b-8bfa-2f5b83722508",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
      "content": "\\section{Notation}\\label{app:notation}\n\nTable~\\ref{tab:notation} summarizes the notation used throughout the paper.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{cl}\n\\toprule\nSymbol & Meaning \\\\\n\\midrule\n$\\mathcal{M}$ & Language model \\\\\n$x$ & Input instance \\\\\n$y_i$ & $i$-th stochastic sample \\\\\n$N$ & Number of samples \\\\\n$T$ & Sampling temperature \\\\\n$c(\\cdot)$ & Confidence signal \\\\\nSJ & Soft Jaccard similarity \\\\\nFK & Fleiss' $\\kappa$ \\\\\nEM & Exact-match voting rate \\\\\n$c_{\\text{vote}}$ & Entity voting confidence \\\\\n$c_{\\text{lp}}$ & Log-probability (mean token log-likelihood) \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Notation used throughout the paper.}\n\\label{tab:notation}\n\\end{table}\n\n\\section{Robustness Analysis}\\label{app:robustness}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Signal robustness across configurations (Spearman $\\rho$). Top: temperature on Qwen SciERC. Middle: sample size on Qwen SciERC. Bottom: cross-model transfer (LLaMA CoNLL $N{=}16$, 3-seed mean $\\pm\\sigma$). $^\\dagger$Mean over 3 seeds ($\\sigma{=}0.025$; individual: 0.428, 0.424, 0.384).}\n\\label{tab:robustness}\n\\begin{tabular}{llcc}\n\\toprule\n& & NER $\\rho$ & RE $\\rho$ \\\\\n\\midrule\n\\multicolumn{4}{l}{\\textit{Temperature} (Qwen SciERC, $N{=}8$)} \\\\\n\\quad SJ & $T{=}0.7$ & 0.388 & 0.234 \\\\\n\\quad SJ & $T{=}1.0$ & 0.360 & 0.250 \\\\\n\\quad FK & $T{=}0.7$ & 0.321 & 0.184 \\\\\n\\quad FK & $T{=}1.0$ & 0.267 & 0.275 \\\\\n\\midrule\n\\multicolumn{4}{l}{\\textit{Sample size} (Qwen SciERC, $T{=}1.0$)} \\\\\n\\quad SJ & $N{=}8$  & 0.360 & 0.250 \\\\\n\\quad SJ & $N{=}16$ & 0.412$^\\dagger$ & 0.281 \\\\\n\\quad FK & $N{=}8$  & 0.267 & 0.275 \\\\\n\\quad FK & $N{=}16$ & 0.280 & 0.279 \\\\\n\\midrule\n\\multicolumn{4}{l}{\\textit{Cross-model} (LLaMA CoNLL, $N{=}16$, 3 seeds)} \\\\\n\\quad SJ &  & $0.463{\\pm}0.007$ & --- \\\\\n\\quad FK &  & $0.455{\\pm}0.006$ & --- \\\\\n\\quad EM &  & $0.460{\\pm}0.008$ & --- \\\\\n\\quad Voting &  & $0.458{\\pm}0.003$ & --- \\\\\n\\quad Logprob &  & $0.310{\\pm}0.005$ & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{fig_temperature_robustness}\n\\caption{Temperature robustness on SciERC ($N{=}8$). Top: NER; bottom: RE. SJ maintains stable $\\rho$ across $T{=}0.7$ and $T{=}1.0$, while FK shows mixed sensitivity. Logprob $T{=}0.7$ data unavailable.}\n\\label{fig:temperature_robustness}\n\\end{figure}\n\n\\paragraph{Temperature sensitivity.}\nSJ NER $\\rho$ shifts from 0.388 ($T{=}0.7$) to 0.360 ($T{=}1.0$), a difference of 0.028 whose bootstrap confidence interval includes zero.\nFK shows mixed behavior: NER $\\rho$ drops by 0.054, while RE $\\rho$ increases by 0.091, likely reflecting reduced diversity at lower temperature interacting differently across tasks.\nAcross all comparisons, the SJ--FK relative ordering is preserved at both temperatures on NER (0.388 vs.\\ 0.321 at $T{=}0.7$; 0.360 vs.\\ 0.267 at $T{=}1.0$), indicating a stable signal hierarchy despite numerically small temperature effects.\n\n\\paragraph{Sample size scaling.}\nIncreasing from $N{=}8$ to $N{=}16$ improves SJ on Qwen SciERC NER: $\\rho$ rises from 0.360 to $0.412{\\pm}0.025$ (three seeds: 0.428, 0.424, 0.384), a gain of $+0.052$.\nThe magnitude of $N$-scaling gains is setting-dependent---LLaMA SciERC NER yields $+0.016$ and Qwen CoNLL NER $+0.014$---though the direction is consistently positive.\nLLaMA CoNLL exhibits the most uniform scaling: all four consistency signals gain $\\Delta\\rho{\\approx}{+}0.030$ (range: $+0.027$ to $+0.032$) while logprob gains only $+0.003$ (Table~\\ref{tab:quality_estimation}).\nFK $N$-scaling is inconsistent: degradation on SciERC ($-0.007$ to $-0.019$) but improvement on CoNLL with LLaMA ($+0.027$), suggesting sensitivity to both model and task characteristics.\nVoting confidence $N$-scaling is consistently positive ($+0.005$ on Qwen CoNLL, $+0.018$ on LLaMA SciERC, $+0.062$ on Qwen SciERC), while logprob is approximately $N$-invariant ($\\Delta{\\leq}0.021$).\nSJ, EM, and voting confidence scale consistently across all tested settings; only FK shows setting-dependent variation, suggesting that structural and binary-agreement signals are the most robust to $N$.\n\n\\paragraph{Cross-model transfer.}\nLLaMA-3.1-8B-Instruct replicates the structural-over-surface ordering on SciERC NER (SJ $\\rho{=}0.363$, FK $\\rho{=}0.327$).\nOn CoNLL, the cross-model gap is minimal (Table~\\ref{tab:quality_estimation}): SJ achieves $\\rho{=}0.431$ (LLaMA) vs.\\ 0.436 (Qwen), $\\Delta{=}0.005$.\nAt $N{=}16$, the structural-over-logprob advantage holds across all four tested settings: Qwen SciERC (Voting $\\rho{=}0.411$ vs.\\ logprob 0.259, $\\Delta{=}{+}0.152$), Qwen CoNLL (EM $\\rho{=}0.463$ vs.\\ logprob 0.328, $\\Delta{=}{+}0.135$), LLaMA SciERC (Voting $\\rho{=}0.452$ vs.\\ logprob 0.277, $\\Delta{=}{+}0.175$), and LLaMA CoNLL 3-seed (SJ $\\rho{=}0.463{\\pm}0.007$ vs.\\ logprob $0.310{\\pm}0.005$, $\\Delta{=}{+}0.153$).\n\n\\section{Calibration Analysis}\\label{app:calibration}\n\n\\begin{figure*}[t]\n\\centering\n\\includegraphics[width=\\textwidth]{fig_reliability}\n\\caption{Reliability diagrams on SciERC ($N{=}8$, $T{=}1.0$). Top: mean F1 vs.\\ binned confidence; bottom: instance counts per bin. Left: NER; right: RE. NER signals are reasonably well-calibrated (calibration ECE 0.069--0.096), while RE shows greater miscalibration (ECE 0.109--0.339), reflecting the difficulty of calibrating confidence for compound extraction tasks.}\n\\label{fig:reliability}\n\\end{figure*}\n\nNER signals are reasonably well-calibrated (calibration ECE 0.069--0.096), while RE exhibits greater miscalibration (ECE 0.109--0.339), indicating that translating consistency scores into calibrated confidence estimates is feasible for NER but remains challenging for compound extraction tasks.\n\n\\section{Additional Analyses}\\label{app:additional}\n\n\\paragraph{Per-relation diagnostic.}\nRE signal degradation is relation-specific.\n\\textsc{Feature-Of} has near-zero correlation ($\\rho{=}0.004$), while \\textsc{Hyponym-Of} achieves $\\rho{=}0.646$.\nThe primary bottleneck is entity span errors, which account for 55.5\\% of RE false negatives---a prerequisite failure that consistency signals cannot detect, as they measure agreement among equally incorrect extractions.\nWe note that RE analysis relies on a single dataset (SciERC); generalization to other RE benchmarks remains to be validated.\n\n\\paragraph{Capability stratification.}\nFor NER, SJ effectiveness scales with structural complexity: on SciERC instances with 6+ entities, $\\rho{=}0.547$, compared to $\\rho{=}0.415$ for 1--2 entities.\nThe SJ advantage over logprob remains stable across sentence-length quartiles ($\\Delta\\rho{\\approx}0.08$--$0.20$).\nFor RE, SJ $\\rho$ increases monotonically with sentence length (Q1: 0.110 $\\to$ Q4: 0.473; Fisher $z$-test $p{=}0.004$), indicating that longer, more relation-dense sentences provide richer structure for consistency-based estimation.\nBoth proxies are weakly correlated with F1 ($|r|{<}0.15$), confirming they capture input complexity rather than directly predicting output quality; however, entity count and sentence length are themselves moderately correlated ($\\rho{=}0.650$), so they reflect overlapping rather than independent complexity dimensions.\nFor RE, entity count and relation count are strongly correlated ($\\rho{=}0.769$) and thus reflect a single structural complexity dimension rather than independent axes.\nOn the high-complexity RE subset ($n{=}81$, high relation count), signals improve substantially: Voting reaches $\\rho{=}0.630$, logprob $\\rho{=}0.554$, and SJ $\\rho{=}0.502$---all far above the full-set levels.\nRicher relational structure provides more signal for consistency-based estimation, complementing the task-level boundary established by WNUT-17: structural signals are most effective within a ``sweet spot'' of sufficient model capability and sufficient output complexity.\n\n\\paragraph{Evaluation circularity.}\nLeave-one-out SJ (LOO-SJ), which excludes the target sample when computing confidence, yields $\\Delta\\rho{=}{-}0.014$ relative to standard SJ, with a maximum per-instance $\\Delta\\rho$ of $3.1{\\times}10^{-4}$.\nEvaluation circularity is negligible.\n\n\\paragraph{Conditional filtering details.}\nOn LLaMA conditional RE (non-zero F1 instances), SJ recovers to $\\rho{=}0.405$ while FK drops to $\\rho{=}0.259$, confirming that structural advantage is robust across both models and evaluation conditions.\nAt $N{=}16$, the divergence persists: SJ maintains $\\rho{=}0.308$ on conditional RE while logprob drops to $\\rho{=}{-}0.026$.\nEM ranks first across all four tested conditional configurations---SciERC NER ($\\rho{=}0.360$), CoNLL Qwen $N{=}16$ ($\\rho{=}0.466$), CoNLL LLaMA 3-seed ($\\rho{=}0.462$), and SciERC RE ($\\rho{=}0.417$)---despite full-set rankings ranging from \\#1 (CoNLL Qwen) to \\#5 (SciERC RE).\nOn the full set, EM is diluted by trivial agreement: instances where all $N$ samples produce identical (possibly incorrect) outputs receive EM${=}1$ regardless of quality, compressing the signal's dynamic range.\nOn the conditional set---where the model demonstrably produces varied outputs---exact agreement becomes the strongest quality signal.\nThe margin over SJ is largest on RE ($\\Delta\\rho{=}{+}0.171$), where compound extraction decisions amplify output variability, and smallest on CoNLL LLaMA ($\\Delta\\rho{=}{+}0.002$), where all signals converge near $\\rho{\\approx}0.46$.\n\n\\paragraph{Diminishing returns of $N$-scaling.}\nOur $N{=}8$ and $N{=}16$ comparisons (Table~\\ref{tab:robustness}) characterize the marginal value of additional samples for test-time scaling \\cite{brown2024monkeys, snell2024scaling}.\nFor quality estimation, structural signals benefit consistently but sublinearly: SJ $\\rho$ improves by $+0.052$ (Qwen SciERC, 3-seed mean) and $+0.032$ (LLaMA CoNLL, 3-seed mean) when doubling from $N{=}8$ to $N{=}16$, while log-probability is approximately $N$-invariant ($\\Delta\\rho{\\leq}0.021$).\nStructural signals leverage $\\binom{N}{2}$ pairwise comparisons (28 pairs at $N{=}8$, 120 at $N{=}16$), but the $\\rho$ improvement is far less than proportional, indicating diminishing information per additional comparison.\nThis asymmetry gives structural signals a relative advantage in the compute-constrained regime: at $N{=}8$, SJ already achieves $\\rho{=}0.431$ on LLaMA CoNLL (vs.\\ logprob $\\rho{=}0.307$, $\\Delta{=}{+}0.124$), and the gap \\textit{widens} at $N{=}16$ ($\\Delta{=}{+}0.153$) because structural signals continue to benefit from additional pairwise evidence while logprob does not.\nFor sample selection, additional samples increase the oracle upper bound---more draws raise the probability of a high-quality candidate---but signal-based selection remains flat because the selector's inability to identify the best candidate is a granularity limitation, not a sample size limitation.\nThe practical implication is that $N{=}8$ captures most of the achievable quality estimation benefit; further scaling widens rather than closes the correlation-selection gap absent stronger per-sample selectors.\n",
      "numLines": 134,
      "startLine": 1,
      "totalLines": 134
    }
  },
  "sourceToolAssistantUUID": "c8ca4a1d-0879-4c24-a137-5a49c59ed02a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_1_68ddc296",
  "sessionId": "cd3ac2da-cdcc-4c5b-9409-914107331cb2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-15T01:58:35.099Z_

<details open><summary>🔧 Tool call — Read · `toolu_01CfXL2h88YR1qeGBX6QMnvY`</summary>

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
  "parentUuid": "664ab25e-be60-400f-a670-1b552d480783",
  "isSidechain": false,
  "requestId": "req_011Cb3XV5nFmdPFxbozqtcYJ",
  "type": "assistant",
  "uuid": "17718c79-9581-4b2a-bf6c-f89342b73262",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_1_68ddc296",
  "sessionId": "cd3ac2da-cdcc-4c5b-9409-914107331cb2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011XmLzwn8kwEtrfPjAJSwkZ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 476,
      "cache_read_input_tokens": 28042,
      "output_tokens": 698,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 476,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 698,
          "cache_read_input_tokens": 28042,
          "cache_creation_input_tokens": 476,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 476
          },
          "type": "message"
        }
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

_source line 28 · 2026-05-15T01:58:35.104Z_

<details><summary>↩ Tool result · `toolu_01CfXL2h88YR1qeGBX6QMnvY`</summary>

```text
1	\section{Introduction}\label{sec:introduction}
2	
3	Self-consistency---sampling multiple outputs and aggregating them---has become a powerful strategy for improving language model reasoning.
4	On discrete-answer tasks such as arithmetic and commonsense QA, majority voting over chain-of-thought samples yields large gains: +18 percentage points on GSM8K \cite{wang2023selfconsistency}.
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
16	The most relevant study, \citet{nedellec2026consistency}, examines consistency--accuracy correlations for LLM-based IE but relies on surface-level matching, explicitly acknowledging it ``overlooks semantically consistent outputs.''
17	No existing work systematically compares confidence signals across structural, surface, and model-internal families for generative IE, nor disentangles quality estimation from sample selection.
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
35	    \item \textbf{First systematic comparison of confidence signals for generative IE.}
36	    We evaluate five signals from three families on quality estimation for NER and RE.
37	    Entity voting achieves the strongest $\rho{=}0.38$ while exact match leads AUROC${=}0.75$; signal rankings depend on both task complexity and evaluation metric, with structural signals leading rank correlation on complex schemas (SciERC) and surface signals leading on simpler tasks (CoNLL).
38	
39	    \item \textbf{Identification of the correlation-selection gap.}
40	    We demonstrate a fundamental disconnect between quality estimation and sample selection in structured IE.
41	    Despite strong instance-level correlations ($\rho$ up to 0.38), no signal reliably surpasses greedy on either task ($p{>}0.39$, bootstrap) despite 13--18~pp of oracle headroom.
42	    This gap reflects the instance-level nature of consistency signals, which predict input difficulty rather than discriminating among individual samples.
43	
44	    \item \textbf{Task-complexity boundary conditions.}
45	    Signal rankings depend on task difficulty: exact match leads on easy tasks (CoNLL), Soft Jaccard dominates on hard tasks (SciERC), and all signals converge when model capability is insufficient (WNUT-17, where 54\% of instances receive zero F1).
46	    This establishes practical guidance for signal selection based on expected task difficulty.
47	\end{enumerate}
48	
49	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "17718c79-9581-4b2a-bf6c-f89342b73262",
  "isSidechain": false,
  "promptId": "e032b776-5e54-467c-9321-aeb2f2c75513",
  "type": "user",
  "uuid": "4028aeff-eeef-4901-b146-643380a69aba",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/introduction.tex",
      "content": "\\section{Introduction}\\label{sec:introduction}\n\nSelf-consistency---sampling multiple outputs and aggregating them---has become a powerful strategy for improving language model reasoning.\nOn discrete-answer tasks such as arithmetic and commonsense QA, majority voting over chain-of-thought samples yields large gains: +18 percentage points on GSM8K \\cite{wang2023selfconsistency}.\nMore broadly, test-time compute scaling through repeated sampling and selection has emerged as a complementary axis to model scaling, offering substantial quality improvements at inference time \\cite{snell2024scaling, brown2024monkeys}.\nThese results rest on a shared assumption: that among $N$ stochastic samples, a selection mechanism can identify better outputs.\nFor tasks with a single correct answer, this assumption holds naturally---the majority vote is the selector.\nBut information extraction (IE) poses a fundamentally different challenge.\nThe output is not a single token or number; it is a \\textit{set} of entities or relations with internal dependencies, where two samples may extract overlapping but non-identical structures.\nThere is no obvious majority to vote on, partial agreement is the norm rather than the exception, and the space of valid outputs is combinatorially large.\nCan self-consistency still provide useful signal in this structured setting?\n\nPrior work on confidence estimation for LLM-based IE has conflated two distinct objectives: \\textit{quality estimation} (which inputs does the model handle reliably?) and \\textit{sample selection} (which of $N$ outputs is best?).\nThese require fundamentally different signal properties: the former benefits from instance-level aggregation, while the latter demands per-sample discrimination.\nSelf-consistency methods for discrete answers \\cite{wang2023selfconsistency, chen2024usc} and weighted variants \\cite{taubenfeld2025cisc, kang2025selfcertainty} assume outputs can be grouped by equivalence---an assumption that breaks for entity sets with partial overlap.\nThe most relevant study, \\citet{nedellec2026consistency}, examines consistency--accuracy correlations for LLM-based IE but relies on surface-level matching, explicitly acknowledging it ``overlooks semantically consistent outputs.''\nNo existing work systematically compares confidence signals across structural, surface, and model-internal families for generative IE, nor disentangles quality estimation from sample selection.\n\nOur central finding is that consistency-based signals are effective quality estimators but poor sample selectors for structured IE.\nEntity voting achieves $\\rho{=}0.38$ on SciERC NER and exact match leads AUROC${=}0.75$, both practically useful for quality-aware routing.\nYet no signal reliably surpasses greedy decoding on best-of-$N$ selection ($p{>}0.39$, bootstrap) despite 13--18~pp of oracle headroom.\nWe term this the \\textbf{correlation-selection gap} (Figure~\\ref{fig:overview}): instance-level signals predict \\textit{which inputs} are hard, not \\textit{which output} is best.\n\n\\begin{figure*}[t]\n\\centering\n\\includegraphics[width=\\textwidth]{fig_overview}\n\\caption{The correlation-selection gap. Left: consistency signals (here entity voting) predict instance-level quality---high agreement correlates with high F1 ($\\rho{\\approx}0.38$, AUROC${\\approx}0.69$). Right: the same instance-level signal assigns identical scores to all $N$ candidates from a given input, precluding sample selection. No signal reliably surpasses greedy on either task ($p{=}0.39$ for NER logprob).}\n\\label{fig:overview}\n\\end{figure*}\n\nWe systematically evaluate five confidence signals from three families---structural (entity voting, Soft Jaccard), surface (exact match, Fleiss' $\\kappa$), and model-internal (log-probability)---across NER and RE on SciERC \\cite{luan2018scierc}, CoNLL-2003 \\cite{tjongkimsang2003conll}, and WNUT-17 \\cite{derczynski2017wnut}, using Qwen3-8B and LLaMA-3.1-8B.\n\nOur contributions are as follows:\n\\begin{enumerate}\n    \\item \\textbf{First systematic comparison of confidence signals for generative IE.}\n    We evaluate five signals from three families on quality estimation for NER and RE.\n    Entity voting achieves the strongest $\\rho{=}0.38$ while exact match leads AUROC${=}0.75$; signal rankings depend on both task complexity and evaluation metric, with structural signals leading rank correlation on complex schemas (SciERC) and surface signals leading on simpler tasks (CoNLL).\n\n    \\item \\textbf{Identification of the correlation-selection gap.}\n    We demonstrate a fundamental disconnect between quality estimation and sample selection in structured IE.\n    Despite strong instance-level correlations ($\\rho$ up to 0.38), no signal reliably surpasses greedy on either task ($p{>}0.39$, bootstrap) despite 13--18~pp of oracle headroom.\n    This gap reflects the instance-level nature of consistency signals, which predict input difficulty rather than discriminating among individual samples.\n\n    \\item \\textbf{Task-complexity boundary conditions.}\n    Signal rankings depend on task difficulty: exact match leads on easy tasks (CoNLL), Soft Jaccard dominates on hard tasks (SciERC), and all signals converge when model capability is insufficient (WNUT-17, where 54\\% of instances receive zero F1).\n    This establishes practical guidance for signal selection based on expected task difficulty.\n\\end{enumerate}\n\n",
      "numLines": 49,
      "startLine": 1,
      "totalLines": 49
    }
  },
  "sourceToolAssistantUUID": "17718c79-9581-4b2a-bf6c-f89342b73262",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_1_68ddc296",
  "sessionId": "cd3ac2da-cdcc-4c5b-9409-914107331cb2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-15T01:58:35.523Z_

<details open><summary>🔧 Tool call — Read · `toolu_0118TEUphV1mc9G6nioq45t5`</summary>

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
  "parentUuid": "4028aeff-eeef-4901-b146-643380a69aba",
  "isSidechain": false,
  "requestId": "req_011Cb3XV5nFmdPFxbozqtcYJ",
  "type": "assistant",
  "uuid": "f7e6e746-bdb5-4d79-9b0b-8f13a85f9689",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_1_68ddc296",
  "sessionId": "cd3ac2da-cdcc-4c5b-9409-914107331cb2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011XmLzwn8kwEtrfPjAJSwkZ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 476,
      "cache_read_input_tokens": 28042,
      "output_tokens": 698,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 476,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 698,
          "cache_read_input_tokens": 28042,
          "cache_creation_input_tokens": 476,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 476
          },
          "type": "message"
        }
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

_source line 30 · 2026-05-15T01:58:35.528Z_

<details><summary>↩ Tool result · `toolu_0118TEUphV1mc9G6nioq45t5`</summary>

```text
1	\section{Related Work}\label{sec:related}
2	
3	\paragraph{Self-consistency and test-time scaling.}
4	Self-consistency decoding \cite{wang2023selfconsistency} improves reasoning by majority voting over chain-of-thought samples, assuming a discrete answer space.
5	Extensions to free-form text use LLM-based comparison \cite{chen2024usc}, atomic sub-claim decomposition \cite{thirukovalluru2024atomic}, or cross-sample hallucination detection \cite{manakul2023selfcheckgpt}.
6	For test-time scaling, \citet{snell2024scaling} characterize compute scaling laws and \citet{brown2024monkeys} show best-of-$N$ gains across tasks.
7	Recent reward-free selectors include confidence-weighted voting \cite{taubenfeld2025cisc}, KL-based self-certainty \cite{kang2025selfcertainty}, adaptive sampling \cite{kim2026reasc}, ranked aggregation \cite{wang2025rankedvoting}, and latent-space consistency \cite{oh2025latentsc}.
8	All target reasoning/QA with discrete answers.
9	Our work extends self-consistency to set-valued structured outputs and identifies the correlation-selection gap: strong quality estimation ($\rho{=}0.38$) coexists with selection failure ($p{>}0.39$).
10	
11	\paragraph{Consistency for structured IE.}
12	\citet{nedellec2026consistency} study consistency--accuracy correlations for LLM-based NER/RE, corroborating our quality-estimation findings.
13	However, they rely on surface-level matching (explicitly acknowledging it ``overlooks semantically consistent outputs''), do not study best-of-$N$ selection, and evaluate a single domain with hard prompting.
14	Our Soft Jaccard signal addresses the matching limitation through type-aware bipartite matching with span overlap.
15	CoCoA \cite{vashurin2025cocoa} fuses model confidence with inter-sample consistency for QA/summarization but does not address structured extraction.
16	Our evaluation builds on generative IE work \cite{zhou2024uniner, sainz2024gollie, josifoski2022genie, li2023codeie, wadhwa2023revisiting, wang2023instructuie} and constrained decoding \cite{willard2023guided}.
17	
18	\paragraph{Uncertainty estimation and calibration.}
19	Several surveys cover confidence estimation \cite{geng2024confidence}, selective abstention \cite{wen2025know}, uncertainty quantification \cite{xia2025survey}, and their intersection with calibration \cite{hobelsberger2025systematic} for LLMs.
20	Semantic uncertainty \cite{kuhn2023semantic} clusters generations by meaning; \citet{kossen2024semantic} distill semantic entropy into lightweight probes; P(True) \cite{kadavath2022language} queries model confidence directly; our structural signals instead measure agreement over output \textit{structure}.
21	Modern neural networks are often miscalibrated \cite{guo2017calibration, desai2020calibration}; our reliability diagrams extend calibration analysis to structured prediction.
22	Deep ensembles \cite{lakshminarayanan2017ensembles} and MC-dropout \cite{gal2016dropout} obtain uncertainty from model variation; our approach requires no model modification.
23	Prior NER uncertainty work \cite{xiao2019uncertainty, shelmanov2021active, zhang2023ener} operates within discriminative paradigms, inapplicable to generative settings.
24	Conformal prediction \cite{fisch2021conformal, angelopoulos2021conformal} provides coverage guarantees; trained verifiers \cite{cobbe2021verifiers, lightman2024verify} and reward models \cite{wang2024mathshepherd} learn per-sample scoring from labeled data.
25	Selective prediction \cite{geifman2017selective} and confidence-based IE filtering \cite{culotta2004confidence} establish the broader framework; our contribution is characterizing which signals support quality estimation vs.\ sample selection for generative IE.
26	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f7e6e746-bdb5-4d79-9b0b-8f13a85f9689",
  "isSidechain": false,
  "promptId": "e032b776-5e54-467c-9321-aeb2f2c75513",
  "type": "user",
  "uuid": "fdb35c80-e7bf-439b-9508-5d931876c028",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/related_work.tex",
      "content": "\\section{Related Work}\\label{sec:related}\n\n\\paragraph{Self-consistency and test-time scaling.}\nSelf-consistency decoding \\cite{wang2023selfconsistency} improves reasoning by majority voting over chain-of-thought samples, assuming a discrete answer space.\nExtensions to free-form text use LLM-based comparison \\cite{chen2024usc}, atomic sub-claim decomposition \\cite{thirukovalluru2024atomic}, or cross-sample hallucination detection \\cite{manakul2023selfcheckgpt}.\nFor test-time scaling, \\citet{snell2024scaling} characterize compute scaling laws and \\citet{brown2024monkeys} show best-of-$N$ gains across tasks.\nRecent reward-free selectors include confidence-weighted voting \\cite{taubenfeld2025cisc}, KL-based self-certainty \\cite{kang2025selfcertainty}, adaptive sampling \\cite{kim2026reasc}, ranked aggregation \\cite{wang2025rankedvoting}, and latent-space consistency \\cite{oh2025latentsc}.\nAll target reasoning/QA with discrete answers.\nOur work extends self-consistency to set-valued structured outputs and identifies the correlation-selection gap: strong quality estimation ($\\rho{=}0.38$) coexists with selection failure ($p{>}0.39$).\n\n\\paragraph{Consistency for structured IE.}\n\\citet{nedellec2026consistency} study consistency--accuracy correlations for LLM-based NER/RE, corroborating our quality-estimation findings.\nHowever, they rely on surface-level matching (explicitly acknowledging it ``overlooks semantically consistent outputs''), do not study best-of-$N$ selection, and evaluate a single domain with hard prompting.\nOur Soft Jaccard signal addresses the matching limitation through type-aware bipartite matching with span overlap.\nCoCoA \\cite{vashurin2025cocoa} fuses model confidence with inter-sample consistency for QA/summarization but does not address structured extraction.\nOur evaluation builds on generative IE work \\cite{zhou2024uniner, sainz2024gollie, josifoski2022genie, li2023codeie, wadhwa2023revisiting, wang2023instructuie} and constrained decoding \\cite{willard2023guided}.\n\n\\paragraph{Uncertainty estimation and calibration.}\nSeveral surveys cover confidence estimation \\cite{geng2024confidence}, selective abstention \\cite{wen2025know}, uncertainty quantification \\cite{xia2025survey}, and their intersection with calibration \\cite{hobelsberger2025systematic} for LLMs.\nSemantic uncertainty \\cite{kuhn2023semantic} clusters generations by meaning; \\citet{kossen2024semantic} distill semantic entropy into lightweight probes; P(True) \\cite{kadavath2022language} queries model confidence directly; our structural signals instead measure agreement over output \\textit{structure}.\nModern neural networks are often miscalibrated \\cite{guo2017calibration, desai2020calibration}; our reliability diagrams extend calibration analysis to structured prediction.\nDeep ensembles \\cite{lakshminarayanan2017ensembles} and MC-dropout \\cite{gal2016dropout} obtain uncertainty from model variation; our approach requires no model modification.\nPrior NER uncertainty work \\cite{xiao2019uncertainty, shelmanov2021active, zhang2023ener} operates within discriminative paradigms, inapplicable to generative settings.\nConformal prediction \\cite{fisch2021conformal, angelopoulos2021conformal} provides coverage guarantees; trained verifiers \\cite{cobbe2021verifiers, lightman2024verify} and reward models \\cite{wang2024mathshepherd} learn per-sample scoring from labeled data.\nSelective prediction \\cite{geifman2017selective} and confidence-based IE filtering \\cite{culotta2004confidence} establish the broader framework; our contribution is characterizing which signals support quality estimation vs.\\ sample selection for generative IE.\n",
      "numLines": 26,
      "startLine": 1,
      "totalLines": 26
    }
  },
  "sourceToolAssistantUUID": "f7e6e746-bdb5-4d79-9b0b-8f13a85f9689",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_1_68ddc296",
  "sessionId": "cd3ac2da-cdcc-4c5b-9409-914107331cb2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-15T01:58:35.998Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Pgqb3rnR7uvAx1dfpiorCZ`</summary>

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
  "parentUuid": "fdb35c80-e7bf-439b-9508-5d931876c028",
  "isSidechain": false,
  "requestId": "req_011Cb3XV5nFmdPFxbozqtcYJ",
  "type": "assistant",
  "uuid": "80b6e462-2def-46b2-bffc-109f9f4d8dde",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_1_68ddc296",
  "sessionId": "cd3ac2da-cdcc-4c5b-9409-914107331cb2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011XmLzwn8kwEtrfPjAJSwkZ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 476,
      "cache_read_input_tokens": 28042,
      "output_tokens": 698,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 476,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 698,
          "cache_read_input_tokens": 28042,
          "cache_creation_input_tokens": 476,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 476
          },
          "type": "message"
        }
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

_source line 32 · 2026-05-15T01:58:36.003Z_

<details><summary>↩ Tool result · `toolu_01Pgqb3rnR7uvAx1dfpiorCZ`</summary>

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
37	Unlike structural signals, FK relies on exact string matching and does not tolerate surface variations.
38	
39	\paragraph{Soft Jaccard (structural, instance-level).}
40	Our core structural signal extends Jaccard similarity \cite{jaccard1901distribution} to extracted entity/relation sets.
41	For samples $y_i, y_j$, we group extractions by type, compute bipartite matching via the Hungarian algorithm with span overlap, and define:
42	\begin{equation}\label{eq:sj}
43	\text{SJ}(y_i, y_j) = \frac{\sum_{m \in M} \text{sim}(a_m, b_m)}{\sum_{g} \max(|g_i|, |g_j|)}
44	\end{equation}
45	where $M$ is the matched set, $\text{sim}$ is span-level Jaccard overlap, and $g_i, g_j$ index per-type extraction counts.
46	The instance-level signal averages over all pairs:
47	\begin{equation}\label{eq:sj_instance}
48	c_{\text{sj}}(x) = \frac{1}{\binom{N}{2}} \sum_{i<j} \text{SJ}(y_i, y_j)
49	\end{equation}
50	
51	\paragraph{Entity voting confidence (structural, instance-level).}
52	For each entity $e$ in the union $E_\cup$ of all samples, we compute frequency $\text{freq}(e) = |\{i : e \in y_i\}| / N$.
53	The instance-level confidence is the mean frequency:
54	\begin{equation}\label{eq:voting}
55	c_{\text{vote}}(x) = \frac{1}{|E_\cup|} \sum_{e \in E_\cup} \text{freq}(e)
56	\end{equation}
57	
58	\subsection{Evaluation Framework}\label{sec:evaluation}
59	
60	\paragraph{Quality estimation.}
61	We measure rank correlation (Spearman $\rho$) between the confidence signal and instance-level F1, and binary discrimination (AUROC) by classifying instances as above or below median F1.
62	
63	\paragraph{Sample selection.}
64	We report best-of-$N$ F1: for each instance, the signal selects one sample.
65	Per-sample signals (logprob) directly rank candidates; instance-level signals select the sample closest to the consensus output.
66	We compare against an \textit{oracle} (highest-F1 sample) and \textit{greedy} ($T{=}0$, $N{=}1$).
67	
68	\paragraph{Complementarity.}
69	High rank correlation does not guarantee effective sample selection: if per-sample variance is low, even a perfect quality estimator cannot distinguish among near-identical candidates (\S\ref{sec:selection_gap}).
70	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "80b6e462-2def-46b2-bffc-109f9f4d8dde",
  "isSidechain": false,
  "promptId": "e032b776-5e54-467c-9321-aeb2f2c75513",
  "type": "user",
  "uuid": "e30a10e7-e776-424d-97c8-d5f445c0aaa0",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/method.tex",
      "content": "\\section{Method}\\label{sec:method}\n\n\\subsection{Problem Formulation}\\label{sec:formulation}\n\nGiven a language model $\\mathcal{M}$ and input $x$, we sample $N$ structured outputs $\\{y_1, \\ldots, y_N\\}$ at temperature $T > 0$ via constrained decoding \\cite{willard2023guided}.\nEach $y_i$ is an entity set (NER) or relation set (RE).\nA confidence signal $c$ serves two purposes: (a) \\textit{quality estimation}---predicting which instances the model handles reliably, and (b) \\textit{sample selection}---identifying the best output among $N$ candidates.\n\nA \\textbf{per-sample signal} scores each $y_i$ independently, $c_{\\text{ps}}: (x, y_i) \\to \\mathbb{R}$, enabling direct candidate ranking.\nAn \\textbf{instance-level signal} aggregates over all $N$ samples, $c_{\\text{il}}: (x, \\{y_i\\}_{i=1}^N) \\to \\mathbb{R}$, producing a single score per input.\nThis asymmetry---between predicting \\textit{which inputs} are easy and selecting \\textit{which output} is best---is central to the correlation-selection gap we investigate.\nNotation is summarized in Appendix~\\ref{app:notation}.\n\n\\subsection{Confidence Signals}\\label{sec:signals}\n\nWe compare five signals from three families: \\textit{model-internal} (log-probability), \\textit{surface} (exact match, Fleiss' $\\kappa$), and \\textit{structural} (Soft Jaccard, entity voting).\n\n\\paragraph{Log-probability (model-internal, per-sample).}\nThe only per-sample signal.\nFor sample $y_i$ with tokens $t_1, \\ldots, t_{|y_i|}$:\n\\begin{equation}\\label{eq:logprob}\nc_{\\text{lp}}(y_i) = \\frac{1}{|y_i|} \\sum_{j=1}^{|y_i|} \\log p_{\\mathcal{M}}(t_j \\mid t_{<j}, x)\n\\end{equation}\n\n\\paragraph{Exact match voting (surface, instance-level).}\nThe majority fraction---the proportion of samples producing the most common output:\n\\begin{equation}\\label{eq:em}\nc_{\\text{em}}(x) = \\frac{1}{N} \\max_{y} \\big|\\{i : y_i = y\\}\\big|\n\\end{equation}\n\n\\paragraph{Fleiss' $\\kappa$ (surface, instance-level).}\nWe adapt \\citet{fleiss1971agreement} to entity sets: items are unique (text, type) tuples across all $N$ samples; each sample assigns binary present/absent labels, yielding a $|E_\\cup| \\times 2$ rating matrix:\n\\begin{equation}\\label{eq:fk}\n\\kappa = \\frac{\\bar{P} - \\bar{P}_e}{1 - \\bar{P}_e}\n\\end{equation}\nwhere $\\bar{P}$ is mean observed pairwise agreement and $\\bar{P}_e$ is expected agreement under random assignment.\nUnlike structural signals, FK relies on exact string matching and does not tolerate surface variations.\n\n\\paragraph{Soft Jaccard (structural, instance-level).}\nOur core structural signal extends Jaccard similarity \\cite{jaccard1901distribution} to extracted entity/relation sets.\nFor samples $y_i, y_j$, we group extractions by type, compute bipartite matching via the Hungarian algorithm with span overlap, and define:\n\\begin{equation}\\label{eq:sj}\n\\text{SJ}(y_i, y_j) = \\frac{\\sum_{m \\in M} \\text{sim}(a_m, b_m)}{\\sum_{g} \\max(|g_i|, |g_j|)}\n\\end{equation}\nwhere $M$ is the matched set, $\\text{sim}$ is span-level Jaccard overlap, and $g_i, g_j$ index per-type extraction counts.\nThe instance-level signal averages over all pairs:\n\\begin{equation}\\label{eq:sj_instance}\nc_{\\text{sj}}(x) = \\frac{1}{\\binom{N}{2}} \\sum_{i<j} \\text{SJ}(y_i, y_j)\n\\end{equation}\n\n\\paragraph{Entity voting confidence (structural, instance-level).}\nFor each entity $e$ in the union $E_\\cup$ of all samples, we compute frequency $\\text{freq}(e) = |\\{i : e \\in y_i\\}| / N$.\nThe instance-level confidence is the mean frequency:\n\\begin{equation}\\label{eq:voting}\nc_{\\text{vote}}(x) = \\frac{1}{|E_\\cup|} \\sum_{e \\in E_\\cup} \\text{freq}(e)\n\\end{equation}\n\n\\subsection{Evaluation Framework}\\label{sec:evaluation}\n\n\\paragraph{Quality estimation.}\nWe measure rank correlation (Spearman $\\rho$) between the confidence signal and instance-level F1, and binary discrimination (AUROC) by classifying instances as above or below median F1.\n\n\\paragraph{Sample selection.}\nWe report best-of-$N$ F1: for each instance, the signal selects one sample.\nPer-sample signals (logprob) directly rank candidates; instance-level signals select the sample closest to the consensus output.\nWe compare against an \\textit{oracle} (highest-F1 sample) and \\textit{greedy} ($T{=}0$, $N{=}1$).\n\n\\paragraph{Complementarity.}\nHigh rank correlation does not guarantee effective sample selection: if per-sample variance is low, even a perfect quality estimator cannot distinguish among near-identical candidates (\\S\\ref{sec:selection_gap}).\n",
      "numLines": 70,
      "startLine": 1,
      "totalLines": 70
    }
  },
  "sourceToolAssistantUUID": "80b6e462-2def-46b2-bffc-109f9f4d8dde",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_1_68ddc296",
  "sessionId": "cd3ac2da-cdcc-4c5b-9409-914107331cb2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-15T01:58:36.936Z_

<details open><summary>🔧 Tool call — Read · `toolu_01CtS6V4pZBQvzJVBgPEZix7`</summary>

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
  "parentUuid": "e30a10e7-e776-424d-97c8-d5f445c0aaa0",
  "isSidechain": false,
  "requestId": "req_011Cb3XV5nFmdPFxbozqtcYJ",
  "type": "assistant",
  "uuid": "d20f261a-6c8c-4791-abcf-07e2c6037431",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_1_68ddc296",
  "sessionId": "cd3ac2da-cdcc-4c5b-9409-914107331cb2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011XmLzwn8kwEtrfPjAJSwkZ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 476,
      "cache_read_input_tokens": 28042,
      "output_tokens": 698,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 476,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 698,
          "cache_read_input_tokens": 28042,
          "cache_creation_input_tokens": 476,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 476
          },
          "type": "message"
        }
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

_source line 34 · 2026-05-15T01:58:36.941Z_

<details><summary>↩ Tool result · `toolu_01CtS6V4pZBQvzJVBgPEZix7`</summary>

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
10	\textbf{CoNLL-2003} \cite{tjongkimsang2003conll} provides 3{,}453 test sentences with 4 entity types, where models achieve ${>}$91\% micro F1.
11	\textbf{WNUT-17} \cite{derczynski2017wnut} consists of 1{,}287 social media instances with emerging entities, used to probe method boundaries (54\% zero F1).
12	
13	\paragraph{Models and sampling.}
14	Our primary model is \textbf{Qwen3-8B} (LoRA, $r{=}32$); for cross-model validation, we evaluate \textbf{LLaMA-3.1-8B-Instruct}.
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
26	\caption{Quality estimation across tasks and models (Spearman $\rho$ and AUROC). Best value per block and column in \textbf{bold}. SciERC evaluates joint NER (6 types) and RE (7 types); CoNLL evaluates NER (4 types). Primary results use $N{=}8$, $T{=}1.0$; $N{=}16$ block reports LLaMA CoNLL 3-seed mean${\pm}$std.}
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
63	
64	\paragraph{$\rho$--AUROC dissociation.}
65	On NER, EM leads AUROC (0.749) despite ranking third in $\rho$ (0.295); on RE, EM achieves the highest AUROC (0.706) while ranking last in $\rho$ (0.134).
66	Binary agreement provides clean separation between reliable and unreliable instances, while structural signals capture finer-grained quality variation.
67	On CoNLL with LLaMA, logprob achieves the highest AUROC (0.761) yet the lowest $\rho$ (0.307), confirming this dissociation across datasets.
68	
69	\paragraph{Signal rankings shift with task difficulty.}
70	On CoNLL (greedy F1${>}$0.91), EM leads ($\rho{=}0.451$, AUROC${=}0.816$), surpassing SJ and Voting.
71	When most samples are near-correct, binary agreement captures remaining variance more efficiently than set-level similarity.
72	This reversal---EM${>}$SJ on easy tasks vs.\ SJ${>}$EM on hard tasks---demonstrates that optimal signal choice depends on task difficulty.
73	Cross-model stability is strong: SJ achieves $\rho{=}0.436$ (Qwen) vs.\ $0.431$ (LLaMA) on CoNLL ($\Delta{=}0.005$).
74	On WNUT-17, SJ achieves only $\rho{=}0.082$ ($p{=}0.106$), establishing the capability boundary where all signals break down.
75	
76	\paragraph{Conditional filtering.}
77	Filtering to non-zero F1 instances reshuffles rankings (Figure~\ref{fig:signal_heatmap}, right).
78	EM emerges as the strongest conditional signal on both NER ($\rho{=}0.360$) and RE ($\rho{=}0.417$), while Voting and FK drop substantially (Voting NER: $0.379{\to}0.300$; FK NER: $0.267{\to}0.176$).
79	Logprob RE collapses to $\rho{=}0.011$, confirming its full-set correlation was driven by zero/non-zero separation.
80	This creates a natural complementarity: Voting and SJ are preferred on the full set, while EM provides the most precise ranking within the non-trivial subset (see Appendix~\ref{app:additional} for details).
81	
82	%% ============================================================
83	\subsection{The Correlation-Selection Gap}
84	\label{sec:selection_gap}
85	
86	\begin{figure*}[t]
87	\centering
88	\includegraphics[width=\textwidth]{fig_selection_gap}
89	\caption{The correlation-selection gap on SciERC ($N{=}8$, $T{=}1.0$). Left: NER; right: RE. Bars show best-of-$N$ selection F1; the line marks quality estimation $\rho$. Despite $\rho$ up to 0.38, no signal reliably surpasses greedy on either task ($p{=}0.39$ for NER logprob, the best signal). Dashed line indicates oracle upper bound.}
90	\label{fig:selection_gap}
91	\end{figure*}
92	
93	\begin{table}[t]
94	\centering
95	\small
96	\caption{Best-of-$N$ selection F1 on SciERC ($N{=}8$, $T{=}1.0$). Best non-oracle result per column in \textbf{bold}. EM produces binary agreement without sample ranking.}
97	\label{tab:selection}
98	\begin{tabular}{lcc}
99	\toprule
100	Method & NER F1 & RE F1 \\
101	\midrule
102	Oracle & 0.776 & 0.585 \\
103	\midrule
104	Log-prob           & \textbf{0.650} & 0.395 \\
105	Soft Jaccard       & 0.645 & 0.386 \\
106	Voting             & 0.634 & 0.359 \\
107	Exact Match        & ---   & ---   \\
108	\midrule
109	Greedy ($T{=}0$)   & 0.644 & \textbf{0.404} \\
110	Random             & 0.608 & 0.354 \\
111	\bottomrule
112	\end{tabular}
113	\end{table}
114	
115	Despite strong quality estimation, confidence signals yield limited gains when used for best-of-$N$ selection (Table~\ref{tab:selection}, Figure~\ref{fig:selection_gap}).
116	
117	\paragraph{No signal reliably surpasses greedy.}
118	On NER, the oracle (0.776) reveals 13.2~pp of headroom above greedy (0.644).
119	Logprob achieves the highest selection F1 (0.650, +0.6~pp), but this is not statistically significant ($p{=}0.39$, 3-seed bootstrap; Cohen's $d{=}0.038$).
120	On RE, the gap is complete: no signal exceeds greedy (0.404) despite 18.1~pp of oracle headroom.
121	Voting ($\rho{=}0.379$, the best quality estimator) selects to only 0.634 on NER---\textit{below} greedy.
122	
123	\paragraph{Quality estimation $\neq$ output selection.}
124	Instance-level confidence signals predict \textit{which inputs} the model handles reliably, not \textit{which output} among $N$ candidates is best.
125	When per-sample variance is low relative to instance-level difficulty, even perfect quality estimation cannot discriminate among near-identical candidates.
126	This gap has direct consequences for test-time scaling in IE \cite{brown2024monkeys, snell2024scaling}: closing it likely requires per-sample signals such as trained verifiers \cite{cobbe2021verifiers}.
127	
128	%% ============================================================
129	\subsection{Robustness}
130	\label{sec:robustness_main}
131	
132	Signal rankings are robust across temperatures, sample sizes, and model families (Table~\ref{tab:robustness}, Appendix~\ref{app:robustness}).
133	SJ NER $\rho$ shifts by only 0.028 between $T{=}0.7$ and $T{=}1.0$ (bootstrap CI includes zero).
134	Doubling from $N{=}8$ to $N{=}16$ yields sublinear gains: SJ improves by $+0.052$ on Qwen SciERC NER, while logprob is approximately $N$-invariant ($\Delta\rho{\leq}0.021$).
135	The structural-over-logprob advantage is model-agnostic, holding across all four $N{=}16$ settings ($\Delta\rho{=}{+}0.135$ to ${+}0.175$).
136	NER signals are reasonably well-calibrated (ECE 0.069--0.096; Appendix~\ref{app:calibration}), while RE exhibits greater miscalibration (ECE 0.109--0.339).
137	For RE at $N{=}16$, SJ, FK, and logprob all plateau at $\rho{\approx}0.28$, suggesting compound errors impose a ceiling.
138	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d20f261a-6c8c-4791-abcf-07e2c6037431",
  "isSidechain": false,
  "promptId": "e032b776-5e54-467c-9321-aeb2f2c75513",
  "type": "user",
  "uuid": "2a805466-ff60-479b-b68b-ab4e06554a3a",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex",
      "content": "\\section{Experiments}\n\\label{sec:experiments}\n\n\\subsection{Experimental Setup}\n\\label{sec:setup}\n\n\\paragraph{Datasets.}\nWe evaluate on three English IE benchmarks spanning a difficulty gradient.\n\\textbf{SciERC} \\cite{luan2018scierc} contains 551 test instances annotated for joint NER (6 types) and RE (7 types).\n\\textbf{CoNLL-2003} \\cite{tjongkimsang2003conll} provides 3{,}453 test sentences with 4 entity types, where models achieve ${>}$91\\% micro F1.\n\\textbf{WNUT-17} \\cite{derczynski2017wnut} consists of 1{,}287 social media instances with emerging entities, used to probe method boundaries (54\\% zero F1).\n\n\\paragraph{Models and sampling.}\nOur primary model is \\textbf{Qwen3-8B} (LoRA, $r{=}32$); for cross-model validation, we evaluate \\textbf{LLaMA-3.1-8B-Instruct}.\nWe draw $N{=}8$ samples at $T{=}1.0$ (primary), with $N{=}16$ for scaling experiments.\\footnote{$N{=}16$ results for CoNLL (Qwen) and SciERC (LLaMA) are in Table~\\ref{tab:robustness} (Appendix~\\ref{app:robustness}).}\nQuality estimation uses Spearman $\\rho$ and AUROC; downstream utility uses best-of-$N$ selection F1 with exact span matching (NER) and head-tail-label matching (RE).\nInference uses vLLM with constrained decoding \\cite{willard2023guided}.\n\n%% ============================================================\n\\subsection{Quality Estimation Results}\n\\label{sec:qe_results}\n\n\\begin{table*}[t]\n\\centering\n\\small\n\\caption{Quality estimation across tasks and models (Spearman $\\rho$ and AUROC). Best value per block and column in \\textbf{bold}. SciERC evaluates joint NER (6 types) and RE (7 types); CoNLL evaluates NER (4 types). Primary results use $N{=}8$, $T{=}1.0$; $N{=}16$ block reports LLaMA CoNLL 3-seed mean${\\pm}$std.}\n\\label{tab:quality_estimation}\n\\begin{tabular}{ll cc cc cc cc}\n\\toprule\n& & \\multicolumn{2}{c}{\\textbf{SciERC NER}} & \\multicolumn{2}{c}{\\textbf{SciERC RE}} & \\multicolumn{2}{c}{\\textbf{CoNLL (Qwen)}} & \\multicolumn{2}{c}{\\textbf{CoNLL (LLaMA)}} \\\\\n\\cmidrule(lr){3-4} \\cmidrule(lr){5-6} \\cmidrule(lr){7-8} \\cmidrule(lr){9-10}\nSignal & Family & $\\rho$ & AUC & $\\rho$ & AUC & $\\rho$ & AUC & $\\rho$ & AUC \\\\\n\\midrule\n\\multicolumn{10}{l}{\\textit{$N{=}8$}} \\\\\nVoting Conf. & Structural & \\textbf{.379} & .684 & \\textbf{.350} & .693 & .424 & .789 & .426 & .709 \\\\\nSoft Jaccard  & Structural & .360 & .692 & .250 & .670 & .436 & .801 & \\textbf{.431} & .704 \\\\\nFleiss' $\\kappa$ & Surface & .267 & .629 & .275 & .609 & .400 & .774 & .428 & .703 \\\\\nExact Match  & Surface    & .295 & \\textbf{.749} & .134 & \\textbf{.706} & \\textbf{.451} & \\textbf{.816} & \\textbf{.431} & .705 \\\\\nLog-prob     & Model      & .205 & .578 & .266 & .600 & .316 & .753 & .307 & \\textbf{.761} \\\\\n\\midrule\n\\multicolumn{10}{l}{\\textit{$N{=}16$ (3-seed)}} \\\\\nVoting Conf. & Structural & & & & & & & .458${\\pm}$.003 & \\\\\nSoft Jaccard  & Structural & & & & & & & \\textbf{.463${\\pm}$.007} & \\\\\nFleiss' $\\kappa$ & Surface & & & & & & & .455${\\pm}$.006 & \\\\\nExact Match  & Surface    & & & & & & & .460${\\pm}$.008 & \\\\\nLog-prob     & Model      & & & & & & & .310${\\pm}$.005 & \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table*}\n\n\\begin{figure*}[t]\n\\centering\n\\includegraphics[width=\\textwidth]{fig_signal_heatmap}\n\\caption{Quality estimation heatmap (Spearman $\\rho$) across five signals and four configurations. Left: full evaluation set; right: conditional set (non-zero F1 instances). On the full set, structural signals dominate on SciERC while all signals converge on CoNLL. On the conditional set, EM emerges as the strongest signal on both NER ($\\rho{=}0.360$) and RE ($\\rho{=}0.417$), while logprob RE collapses to near-zero ($\\rho{=}0.011$).}\n\\label{fig:signal_heatmap}\n\\end{figure*}\n\nTable~\\ref{tab:quality_estimation} presents rank correlation ($\\rho$) and AUROC for five confidence signals across tasks and models.\n\n\\paragraph{Structural signals dominate on complex schemas.}\nOn SciERC NER, Voting achieves $\\rho{=}0.379$ and SJ $\\rho{=}0.360$, both outperforming surface ($\\rho{\\leq}0.295$) and logprob ($\\rho{=}0.205$).\nThe structural advantage persists on RE (Voting $\\rho{=}0.350$), though all signals weaken due to the 44\\% zero-F1 floor effect.\n\n\\paragraph{$\\rho$--AUROC dissociation.}\nOn NER, EM leads AUROC (0.749) despite ranking third in $\\rho$ (0.295); on RE, EM achieves the highest AUROC (0.706) while ranking last in $\\rho$ (0.134).\nBinary agreement provides clean separation between reliable and unreliable instances, while structural signals capture finer-grained quality variation.\nOn CoNLL with LLaMA, logprob achieves the highest AUROC (0.761) yet the lowest $\\rho$ (0.307), confirming this dissociation across datasets.\n\n\\paragraph{Signal rankings shift with task difficulty.}\nOn CoNLL (greedy F1${>}$0.91), EM leads ($\\rho{=}0.451$, AUROC${=}0.816$), surpassing SJ and Voting.\nWhen most samples are near-correct, binary agreement captures remaining variance more efficiently than set-level similarity.\nThis reversal---EM${>}$SJ on easy tasks vs.\\ SJ${>}$EM on hard tasks---demonstrates that optimal signal choice depends on task difficulty.\nCross-model stability is strong: SJ achieves $\\rho{=}0.436$ (Qwen) vs.\\ $0.431$ (LLaMA) on CoNLL ($\\Delta{=}0.005$).\nOn WNUT-17, SJ achieves only $\\rho{=}0.082$ ($p{=}0.106$), establishing the capability boundary where all signals break down.\n\n\\paragraph{Conditional filtering.}\nFiltering to non-zero F1 instances reshuffles rankings (Figure~\\ref{fig:signal_heatmap}, right).\nEM emerges as the strongest conditional signal on both NER ($\\rho{=}0.360$) and RE ($\\rho{=}0.417$), while Voting and FK drop substantially (Voting NER: $0.379{\\to}0.300$; FK NER: $0.267{\\to}0.176$).\nLogprob RE collapses to $\\rho{=}0.011$, confirming its full-set correlation was driven by zero/non-zero separation.\nThis creates a natural complementarity: Voting and SJ are preferred on the full set, while EM provides the most precise ranking within the non-trivial subset (see Appendix~\\ref{app:additional} for details).\n\n%% ============================================================\n\\subsection{The Correlation-Selection Gap}\n\\label{sec:selection_gap}\n\n\\begin{figure*}[t]\n\\centering\n\\includegraphics[width=\\textwidth]{fig_selection_gap}\n\\caption{The correlation-selection gap on SciERC ($N{=}8$, $T{=}1.0$). Left: NER; right: RE. Bars show best-of-$N$ selection F1; the line marks quality estimation $\\rho$. Despite $\\rho$ up to 0.38, no signal reliably surpasses greedy on either task ($p{=}0.39$ for NER logprob, the best signal). Dashed line indicates oracle upper bound.}\n\\label{fig:selection_gap}\n\\end{figure*}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Best-of-$N$ selection F1 on SciERC ($N{=}8$, $T{=}1.0$). Best non-oracle result per column in \\textbf{bold}. EM produces binary agreement without sample ranking.}\n\\label{tab:selection}\n\\begin{tabular}{lcc}\n\\toprule\nMethod & NER F1 & RE F1 \\\\\n\\midrule\nOracle & 0.776 & 0.585 \\\\\n\\midrule\nLog-prob           & \\textbf{0.650} & 0.395 \\\\\nSoft Jaccard       & 0.645 & 0.386 \\\\\nVoting             & 0.634 & 0.359 \\\\\nExact Match        & ---   & ---   \\\\\n\\midrule\nGreedy ($T{=}0$)   & 0.644 & \\textbf{0.404} \\\\\nRandom             & 0.608 & 0.354 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nDespite strong quality estimation, confidence signals yield limited gains when used for best-of-$N$ selection (Table~\\ref{tab:selection}, Figure~\\ref{fig:selection_gap}).\n\n\\paragraph{No signal reliably surpasses greedy.}\nOn NER, the oracle (0.776) reveals 13.2~pp of headroom above greedy (0.644).\nLogprob achieves the highest selection F1 (0.650, +0.6~pp), but this is not statistically significant ($p{=}0.39$, 3-seed bootstrap; Cohen's $d{=}0.038$).\nOn RE, the gap is complete: no signal exceeds greedy (0.404) despite 18.1~pp of oracle headroom.\nVoting ($\\rho{=}0.379$, the best quality estimator) selects to only 0.634 on NER---\\textit{below} greedy.\n\n\\paragraph{Quality estimation $\\neq$ output selection.}\nInstance-level confidence signals predict \\textit{which inputs} the model handles reliably, not \\textit{which output} among $N$ candidates is best.\nWhen per-sample variance is low relative to instance-level difficulty, even perfect quality estimation cannot discriminate among near-identical candidates.\nThis gap has direct consequences for test-time scaling in IE \\cite{brown2024monkeys, snell2024scaling}: closing it likely requires per-sample signals such as trained verifiers \\cite{cobbe2021verifiers}.\n\n%% ============================================================\n\\subsection{Robustness}\n\\label{sec:robustness_main}\n\nSignal rankings are robust across temperatures, sample sizes, and model families (Table~\\ref{tab:robustness}, Appendix~\\ref{app:robustness}).\nSJ NER $\\rho$ shifts by only 0.028 between $T{=}0.7$ and $T{=}1.0$ (bootstrap CI includes zero).\nDoubling from $N{=}8$ to $N{=}16$ yields sublinear gains: SJ improves by $+0.052$ on Qwen SciERC NER, while logprob is approximately $N$-invariant ($\\Delta\\rho{\\leq}0.021$).\nThe structural-over-logprob advantage is model-agnostic, holding across all four $N{=}16$ settings ($\\Delta\\rho{=}{+}0.135$ to ${+}0.175$).\nNER signals are reasonably well-calibrated (ECE 0.069--0.096; Appendix~\\ref{app:calibration}), while RE exhibits greater miscalibration (ECE 0.109--0.339).\nFor RE at $N{=}16$, SJ, FK, and logprob all plateau at $\\rho{\\approx}0.28$, suggesting compound errors impose a ceiling.\n",
      "numLines": 138,
      "startLine": 1,
      "totalLines": 138
    }
  },
  "sourceToolAssistantUUID": "d20f261a-6c8c-4791-abcf-07e2c6037431",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_1_68ddc296",
  "sessionId": "cd3ac2da-cdcc-4c5b-9409-914107331cb2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-15T01:58:37.411Z_

<details open><summary>🔧 Tool call — Read · `toolu_01MqUDkuzG9wjW12BkGYLZrh`</summary>

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
  "parentUuid": "2a805466-ff60-479b-b68b-ab4e06554a3a",
  "isSidechain": false,
  "requestId": "req_011Cb3XV5nFmdPFxbozqtcYJ",
  "type": "assistant",
  "uuid": "d0cf761a-b7fb-4cbf-a786-20febb7cf74a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_1_68ddc296",
  "sessionId": "cd3ac2da-cdcc-4c5b-9409-914107331cb2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011XmLzwn8kwEtrfPjAJSwkZ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 476,
      "cache_read_input_tokens": 28042,
      "output_tokens": 698,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 476,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 698,
          "cache_read_input_tokens": 28042,
          "cache_creation_input_tokens": 476,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 476
          },
          "type": "message"
        }
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

_source line 36 · 2026-05-15T01:58:37.416Z_

<details><summary>↩ Tool result · `toolu_01MqUDkuzG9wjW12BkGYLZrh`</summary>

```text
1	\section{Discussion}\label{sec:discussion}
2	
3	\paragraph{Practical recommendations.}
4	For per-instance quality ranking, entity voting provides the strongest rank correlation ($\rho{=}0.38$, Table~\ref{tab:quality_estimation}), though exact match leads binary discrimination on SciERC (AUROC${=}0.749$).
5	When temperature or cross-condition robustness is required, SJ is preferable: its temperature sensitivity is small with bootstrap CIs including zero (Table~\ref{tab:robustness}).
6	Under conditional filtering, EM leads on both NER and RE ($\rho{=}0.360$, $0.417$), extending binary-agreement advantages to the within-capability regime.
7	Signal rankings depend on task difficulty: EM dominates on easy tasks (CoNLL, F1${>}$0.91), Voting and SJ dominate on hard tasks (SciERC, F1$\,{\approx}\,$0.66), and all signals converge when model capability is insufficient (WNUT-17).
8	This ordering is model-agnostic, suggesting the difficulty gradient determines which signal family is most informative.
9	Conditional filtering confirms this pattern: removing zero-F1 instances shifts effective difficulty toward the easy-task regime, and EM reclaims the lead while Voting and SJ drop substantially (Voting RE: $0.350{\to}0.241$).
10	
11	\paragraph{Why quality estimators fail as selectors.}
12	Quality estimation ranks \textit{instances} by expected output quality via output distribution entropy; sample selection ranks \textit{candidates within a single instance}, requiring per-sample quality information that instance-level aggregation discards.
13	On SciERC NER, the random baseline (0.608) falls 3.6~pp below greedy (0.644), confirming per-instance sample variance exists; yet the oracle gap of 13.2~pp shows substantially better candidates exist, and the best signal captures only +0.6~pp ($p{=}0.39$).
14	The $\rho$--AUROC dissociation illuminates the same asymmetry: on SciERC, EM achieves the highest AUROC (0.749 NER, 0.706 RE) yet ranks third or last in $\rho$; both metrics measure between-instance discrimination at different granularity, but neither captures within-instance variation.
15	The practical implication is that these signals are well-suited for routing and triage---flagging uncertain instances for human review---but not for fine-grained ranking within a difficulty tier.
16	
17	\paragraph{Methodological implications.}
18	The decoupling of quality estimation ($\rho$), binary discrimination (AUROC), and sample selection (best-of-$N$ F1) means that evaluating confidence signals on a single metric risks selecting the wrong signal for the intended use case.
19	Effective best-of-$N$ selection likely requires per-sample signals such as trained verifiers \cite{cobbe2021verifiers} that can evaluate individual outputs rather than distribution-level properties.
20	Further $N$-scaling analysis (Appendix~\ref{app:additional}) shows that $N{=}8$ captures most achievable quality estimation benefit; additional samples widen the correlation-selection gap absent stronger selectors.
21	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d0cf761a-b7fb-4cbf-a786-20febb7cf74a",
  "isSidechain": false,
  "promptId": "e032b776-5e54-467c-9321-aeb2f2c75513",
  "type": "user",
  "uuid": "15ca6366-44ab-4d96-b1a8-2da0999e189a",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex",
      "content": "\\section{Discussion}\\label{sec:discussion}\n\n\\paragraph{Practical recommendations.}\nFor per-instance quality ranking, entity voting provides the strongest rank correlation ($\\rho{=}0.38$, Table~\\ref{tab:quality_estimation}), though exact match leads binary discrimination on SciERC (AUROC${=}0.749$).\nWhen temperature or cross-condition robustness is required, SJ is preferable: its temperature sensitivity is small with bootstrap CIs including zero (Table~\\ref{tab:robustness}).\nUnder conditional filtering, EM leads on both NER and RE ($\\rho{=}0.360$, $0.417$), extending binary-agreement advantages to the within-capability regime.\nSignal rankings depend on task difficulty: EM dominates on easy tasks (CoNLL, F1${>}$0.91), Voting and SJ dominate on hard tasks (SciERC, F1$\\,{\\approx}\\,$0.66), and all signals converge when model capability is insufficient (WNUT-17).\nThis ordering is model-agnostic, suggesting the difficulty gradient determines which signal family is most informative.\nConditional filtering confirms this pattern: removing zero-F1 instances shifts effective difficulty toward the easy-task regime, and EM reclaims the lead while Voting and SJ drop substantially (Voting RE: $0.350{\\to}0.241$).\n\n\\paragraph{Why quality estimators fail as selectors.}\nQuality estimation ranks \\textit{instances} by expected output quality via output distribution entropy; sample selection ranks \\textit{candidates within a single instance}, requiring per-sample quality information that instance-level aggregation discards.\nOn SciERC NER, the random baseline (0.608) falls 3.6~pp below greedy (0.644), confirming per-instance sample variance exists; yet the oracle gap of 13.2~pp shows substantially better candidates exist, and the best signal captures only +0.6~pp ($p{=}0.39$).\nThe $\\rho$--AUROC dissociation illuminates the same asymmetry: on SciERC, EM achieves the highest AUROC (0.749 NER, 0.706 RE) yet ranks third or last in $\\rho$; both metrics measure between-instance discrimination at different granularity, but neither captures within-instance variation.\nThe practical implication is that these signals are well-suited for routing and triage---flagging uncertain instances for human review---but not for fine-grained ranking within a difficulty tier.\n\n\\paragraph{Methodological implications.}\nThe decoupling of quality estimation ($\\rho$), binary discrimination (AUROC), and sample selection (best-of-$N$ F1) means that evaluating confidence signals on a single metric risks selecting the wrong signal for the intended use case.\nEffective best-of-$N$ selection likely requires per-sample signals such as trained verifiers \\cite{cobbe2021verifiers} that can evaluate individual outputs rather than distribution-level properties.\nFurther $N$-scaling analysis (Appendix~\\ref{app:additional}) shows that $N{=}8$ captures most achievable quality estimation benefit; additional samples widen the correlation-selection gap absent stronger selectors.\n",
      "numLines": 21,
      "startLine": 1,
      "totalLines": 21
    }
  },
  "sourceToolAssistantUUID": "d0cf761a-b7fb-4cbf-a786-20febb7cf74a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_1_68ddc296",
  "sessionId": "cd3ac2da-cdcc-4c5b-9409-914107331cb2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-15T01:58:37.877Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Fg7zo1kazJQJv2mxmRmL7A`</summary>

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
  "parentUuid": "15ca6366-44ab-4d96-b1a8-2da0999e189a",
  "isSidechain": false,
  "requestId": "req_011Cb3XV5nFmdPFxbozqtcYJ",
  "type": "assistant",
  "uuid": "17552fe3-5e40-40de-ae8e-7b25b982bb6f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_1_68ddc296",
  "sessionId": "cd3ac2da-cdcc-4c5b-9409-914107331cb2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011XmLzwn8kwEtrfPjAJSwkZ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 476,
      "cache_read_input_tokens": 28042,
      "output_tokens": 698,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 476,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 698,
          "cache_read_input_tokens": 28042,
          "cache_creation_input_tokens": 476,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 476
          },
          "type": "message"
        }
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

_source line 38 · 2026-05-15T01:58:37.882Z_

<details><summary>↩ Tool result · `toolu_01Fg7zo1kazJQJv2mxmRmL7A`</summary>

```text
1	\section{Conclusion}\label{sec:conclusion}
2	
3	This work provides the first systematic evaluation of confidence signals for test-time scaling in generative information extraction.
4	By comparing five signals from three families---structural, surface, and model-internal---across NER and RE tasks of varying difficulty, we disentangle two objectives that prior work has conflated: quality estimation (ranking instances by expected performance) and sample selection (choosing the best output among $N$ candidates).
5	Our experiments on SciERC, CoNLL-2003, and WNUT-17 with Qwen3-8B and LLaMA-3.1-8B reveal that these objectives require fundamentally different signal properties.
6	
7	Three findings anchor our analysis.
8	First, consistency-based signals are effective quality estimators: entity voting achieves the strongest rank correlation ($\rho{=}0.38$) while exact match leads binary discrimination (AUROC${=}0.75$) on SciERC NER, with signal rankings depending on both task complexity and evaluation metric.
9	Second, the \textit{correlation-selection gap} shows that strong instance-level correlation does not yield substantial selection gains---no signal reliably surpasses greedy on either task (NER logprob: +0.6~pp, $p{=}0.39$; RE: $-$0.9~pp) despite 13--18~pp of oracle headroom---because instance-level signals cannot discriminate among candidates with similar consistency profiles.
10	Third, signal rankings depend on task difficulty: exact match leads on easy tasks, Soft Jaccard and voting lead on hard tasks, and all signals converge when model capability is insufficient, establishing practical guidance for signal choice.
11	
12	Several directions remain open.
13	Trained verifiers or reward models could close the selection gap by learning per-sample quality discrimination that unsupervised consistency signals lack.
14	Cross-task transfer of confidence signals beyond IE---to structured prediction tasks such as semantic parsing and code generation---would test the generality of our findings.
15	Integration with conformal prediction could convert continuous confidence scores into calibrated coverage guarantees.
16	Finally, scaling analysis with larger models (70B+) and more diverse IE tasks would clarify whether increased model capability narrows or widens the correlation-selection gap.
17	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "17552fe3-5e40-40de-ae8e-7b25b982bb6f",
  "isSidechain": false,
  "promptId": "e032b776-5e54-467c-9321-aeb2f2c75513",
  "type": "user",
  "uuid": "c944cc60-cef6-4bb1-83ae-83fbd66aefba",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/conclusion.tex",
      "content": "\\section{Conclusion}\\label{sec:conclusion}\n\nThis work provides the first systematic evaluation of confidence signals for test-time scaling in generative information extraction.\nBy comparing five signals from three families---structural, surface, and model-internal---across NER and RE tasks of varying difficulty, we disentangle two objectives that prior work has conflated: quality estimation (ranking instances by expected performance) and sample selection (choosing the best output among $N$ candidates).\nOur experiments on SciERC, CoNLL-2003, and WNUT-17 with Qwen3-8B and LLaMA-3.1-8B reveal that these objectives require fundamentally different signal properties.\n\nThree findings anchor our analysis.\nFirst, consistency-based signals are effective quality estimators: entity voting achieves the strongest rank correlation ($\\rho{=}0.38$) while exact match leads binary discrimination (AUROC${=}0.75$) on SciERC NER, with signal rankings depending on both task complexity and evaluation metric.\nSecond, the \\textit{correlation-selection gap} shows that strong instance-level correlation does not yield substantial selection gains---no signal reliably surpasses greedy on either task (NER logprob: +0.6~pp, $p{=}0.39$; RE: $-$0.9~pp) despite 13--18~pp of oracle headroom---because instance-level signals cannot discriminate among candidates with similar consistency profiles.\nThird, signal rankings depend on task difficulty: exact match leads on easy tasks, Soft Jaccard and voting lead on hard tasks, and all signals converge when model capability is insufficient, establishing practical guidance for signal choice.\n\nSeveral directions remain open.\nTrained verifiers or reward models could close the selection gap by learning per-sample quality discrimination that unsupervised consistency signals lack.\nCross-task transfer of confidence signals beyond IE---to structured prediction tasks such as semantic parsing and code generation---would test the generality of our findings.\nIntegration with conformal prediction could convert continuous confidence scores into calibrated coverage guarantees.\nFinally, scaling analysis with larger models (70B+) and more diverse IE tasks would clarify whether increased model capability narrows or widens the correlation-selection gap.\n",
      "numLines": 17,
      "startLine": 1,
      "totalLines": 17
    }
  },
  "sourceToolAssistantUUID": "17552fe3-5e40-40de-ae8e-7b25b982bb6f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_1_68ddc296",
  "sessionId": "cd3ac2da-cdcc-4c5b-9409-914107331cb2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-15T01:58:38.349Z_

<details open><summary>🔧 Tool call — Read · `toolu_01P1bDtZjmbro4URdrRYU5G5`</summary>

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
  "parentUuid": "c944cc60-cef6-4bb1-83ae-83fbd66aefba",
  "isSidechain": false,
  "requestId": "req_011Cb3XV5nFmdPFxbozqtcYJ",
  "type": "assistant",
  "uuid": "45d38038-068f-4485-b842-5ff01fa124da",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_1_68ddc296",
  "sessionId": "cd3ac2da-cdcc-4c5b-9409-914107331cb2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011XmLzwn8kwEtrfPjAJSwkZ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 476,
      "cache_read_input_tokens": 28042,
      "output_tokens": 698,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 476,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 698,
          "cache_read_input_tokens": 28042,
          "cache_creation_input_tokens": 476,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 476
          },
          "type": "message"
        }
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

_source line 40 · 2026-05-15T01:58:38.355Z_

<details><summary>↩ Tool result · `toolu_01P1bDtZjmbro4URdrRYU5G5`</summary>

```text
1	Our evaluation covers three datasets but only one RE benchmark (SciERC), where 44\% of instances receive zero F1, compressing the discriminable range and limiting signal differentiation for relation extraction.
2	WNUT-17 confirms the capability boundary of our approach, but our positive results on formal-domain text (CoNLL, SciERC) have not been validated on informal or noisy text where models achieve non-trivial performance.
3	
4	We evaluate two model families (Qwen3-8B and LLaMA-3.1-8B), both at 8B parameters.
5	Whether our findings---particularly the correlation-selection gap and the structural-over-surface signal ordering---hold for larger models (70B+) or closed-source APIs remains untested.
6	Larger models may produce higher-quality and more diverse samples, potentially altering the signal landscape.
7	
8	Our analysis of selection potential uses unsupervised signals and a logistic regression proxy as an upper bound.
9	We do not train a dedicated verifier or reward model, leaving unknown how much of the oracle headroom a supervised approach could recover.
10	
11	We evaluate at $N{=}8$ and $N{=}16$.
12	The behavior of confidence signals at larger sample sizes (e.g., $N{=}64$ or $N{=}128$) is unknown, and $N$-scaling gains are setting-dependent: SJ improves by $+0.052$ on Qwen SciERC NER but only $+0.016$ on LLaMA SciERC NER when doubling from $N{=}8$ to $N{=}16$.
13	
14	On CoNLL with LLaMA, the SJ--FK gap is only 0.003 ($\rho{=}0.431$ vs.\ $0.428$), so the structural advantage over surface signals may not generalize to all simple-schema datasets.
15	Finally, log-probability was excluded from the temperature comparison ($T{=}0.7$ vs.\ $T{=}1.0$) due to missing $T{=}0.7$ logprob data, leaving its temperature sensitivity uncharacterized.
16	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "45d38038-068f-4485-b842-5ff01fa124da",
  "isSidechain": false,
  "promptId": "e032b776-5e54-467c-9321-aeb2f2c75513",
  "type": "user",
  "uuid": "f226e3e4-51c1-4c0b-b046-58f37db0b0ce",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/limitations.tex",
      "content": "Our evaluation covers three datasets but only one RE benchmark (SciERC), where 44\\% of instances receive zero F1, compressing the discriminable range and limiting signal differentiation for relation extraction.\nWNUT-17 confirms the capability boundary of our approach, but our positive results on formal-domain text (CoNLL, SciERC) have not been validated on informal or noisy text where models achieve non-trivial performance.\n\nWe evaluate two model families (Qwen3-8B and LLaMA-3.1-8B), both at 8B parameters.\nWhether our findings---particularly the correlation-selection gap and the structural-over-surface signal ordering---hold for larger models (70B+) or closed-source APIs remains untested.\nLarger models may produce higher-quality and more diverse samples, potentially altering the signal landscape.\n\nOur analysis of selection potential uses unsupervised signals and a logistic regression proxy as an upper bound.\nWe do not train a dedicated verifier or reward model, leaving unknown how much of the oracle headroom a supervised approach could recover.\n\nWe evaluate at $N{=}8$ and $N{=}16$.\nThe behavior of confidence signals at larger sample sizes (e.g., $N{=}64$ or $N{=}128$) is unknown, and $N$-scaling gains are setting-dependent: SJ improves by $+0.052$ on Qwen SciERC NER but only $+0.016$ on LLaMA SciERC NER when doubling from $N{=}8$ to $N{=}16$.\n\nOn CoNLL with LLaMA, the SJ--FK gap is only 0.003 ($\\rho{=}0.431$ vs.\\ $0.428$), so the structural advantage over surface signals may not generalize to all simple-schema datasets.\nFinally, log-probability was excluded from the temperature comparison ($T{=}0.7$ vs.\\ $T{=}1.0$) due to missing $T{=}0.7$ logprob data, leaving its temperature sensitivity uncharacterized.\n",
      "numLines": 16,
      "startLine": 1,
      "totalLines": 16
    }
  },
  "sourceToolAssistantUUID": "45d38038-068f-4485-b842-5ff01fa124da",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_1_68ddc296",
  "sessionId": "cd3ac2da-cdcc-4c5b-9409-914107331cb2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-15T01:58:38.813Z_

<details open><summary>🔧 Tool call — Read · `toolu_011HWcg5nkDiLWnjvKyxvQCC`</summary>

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
  "parentUuid": "f226e3e4-51c1-4c0b-b046-58f37db0b0ce",
  "isSidechain": false,
  "requestId": "req_011Cb3XV5nFmdPFxbozqtcYJ",
  "type": "assistant",
  "uuid": "c8ca4a1d-0879-4c24-a137-5a49c59ed02a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_1_68ddc296",
  "sessionId": "cd3ac2da-cdcc-4c5b-9409-914107331cb2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011XmLzwn8kwEtrfPjAJSwkZ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 476,
      "cache_read_input_tokens": 28042,
      "output_tokens": 698,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 476,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 698,
          "cache_read_input_tokens": 28042,
          "cache_creation_input_tokens": 476,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 476
          },
          "type": "message"
        }
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

_source line 42 · 2026-05-15T01:58:38.873Z_

```json
{
  "parentUuid": "7288de24-9ac3-466b-8bfa-2f5b83722508",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "e8660e37-737a-40a2-adbc-e409eb02e22e",
  "timestamp": "2026-05-15T01:58:38.873Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_1_68ddc296",
  "sessionId": "cd3ac2da-cdcc-4c5b-9409-914107331cb2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 43_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[Round 1 审稿请求]: ## 交叉分享：Reviewer 2 的完整 Round 1 审稿意见  请逐条回应 Reviewer 2 的每个问题：用 [AGREE] 表示同意并说明理由，或 [REBUT] 表示反驳并引用论文具体 Section/Table/Figure 作为证据。  ---  以下是 Reviewer 2 的完整审稿原文：  ### 总体评分 **Overall**: 3.…",
  "leafUuid": "e8660e37-737a-40a2-adbc-e409eb02e22e",
  "sessionId": "cd3ac2da-cdcc-4c5b-9409-914107331cb2"
}
```

---

### Runtime record

_source line 44_

```json
{
  "type": "ai-title",
  "aiTitle": "Respond to EMNLP Reviewer 2 Round 1 comments",
  "sessionId": "cd3ac2da-cdcc-4c5b-9409-914107331cb2"
}
```

---

### Assistant

_source line 45 · 2026-05-15T01:58:42.171Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have a thorough understanding of the paper. Let me also check the references file to verify some claims by Reviewer 2.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e8660e37-737a-40a2-adbc-e409eb02e22e",
  "isSidechain": false,
  "requestId": "req_011Cb3XVct2Nv3kFHvem4nkg",
  "type": "assistant",
  "uuid": "1125232e-1a51-4050-8ad2-f0ca2977344f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_1_68ddc296",
  "sessionId": "cd3ac2da-cdcc-4c5b-9409-914107331cb2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011wAA4Sz18SwBmwtEzL5aGf",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 15252,
      "cache_read_input_tokens": 28518,
      "output_tokens": 167,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 15252,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 167,
          "cache_read_input_tokens": 28518,
          "cache_creation_input_tokens": 15252,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 15252
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

_source line 46 · 2026-05-15T01:58:43.137Z_

现在读取 references 文件，确认引用相关问题。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1125232e-1a51-4050-8ad2-f0ca2977344f",
  "isSidechain": false,
  "requestId": "req_011Cb3XVct2Nv3kFHvem4nkg",
  "type": "assistant",
  "uuid": "6e8e157f-56f2-4b44-a63f-4d5a5ad34fd3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_1_68ddc296",
  "sessionId": "cd3ac2da-cdcc-4c5b-9409-914107331cb2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011wAA4Sz18SwBmwtEzL5aGf",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 15252,
      "cache_read_input_tokens": 28518,
      "output_tokens": 167,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 15252,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 167,
          "cache_read_input_tokens": 28518,
          "cache_creation_input_tokens": 15252,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 15252
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

_source line 47 · 2026-05-15T01:58:45.078Z_

<details open><summary>🔧 Tool call — Glob · `toolu_018T8i8DdAMJQZ1TerKziAWB`</summary>

```json
{
  "pattern": "**/paper/references.bib",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6e8e157f-56f2-4b44-a63f-4d5a5ad34fd3",
  "isSidechain": false,
  "requestId": "req_011Cb3XVct2Nv3kFHvem4nkg",
  "type": "assistant",
  "uuid": "4f5b7bf6-0b28-4c30-bfc9-5d11270d71d2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_1_68ddc296",
  "sessionId": "cd3ac2da-cdcc-4c5b-9409-914107331cb2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011wAA4Sz18SwBmwtEzL5aGf",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 15252,
      "cache_read_input_tokens": 28518,
      "output_tokens": 167,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 15252,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 167,
          "cache_read_input_tokens": 28518,
          "cache_creation_input_tokens": 15252,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 15252
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

_source line 48 · 2026-05-15T01:58:45.091Z_

<details><summary>↩ Tool result · `toolu_018T8i8DdAMJQZ1TerKziAWB`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/references.bib
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4f5b7bf6-0b28-4c30-bfc9-5d11270d71d2",
  "isSidechain": false,
  "promptId": "e032b776-5e54-467c-9321-aeb2f2c75513",
  "type": "user",
  "uuid": "095b6597-88ec-4a16-a5a5-03d5bed4e6fc",
  "toolUseResult": {
    "filenames": [
      "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/references.bib"
    ],
    "durationMs": 10,
    "numFiles": 1,
    "truncated": false
  },
  "sourceToolAssistantUUID": "4f5b7bf6-0b28-4c30-bfc9-5d11270d71d2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_1_68ddc296",
  "sessionId": "cd3ac2da-cdcc-4c5b-9409-914107331cb2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 49 · 2026-05-15T01:58:48.245Z_

<details open><summary>🔧 Tool call — Read · `toolu_01D4dg82TJiRKBk3hcGVe8xZ`</summary>

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
  "parentUuid": "095b6597-88ec-4a16-a5a5-03d5bed4e6fc",
  "isSidechain": false,
  "requestId": "req_011Cb3XW5e743o9kapS5jMVj",
  "type": "assistant",
  "uuid": "b95728d1-6b33-4f06-9f75-685435c69e36",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_1_68ddc296",
  "sessionId": "cd3ac2da-cdcc-4c5b-9409-914107331cb2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012UMVXerh5MtDu9zF5FuQmN",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 216,
      "cache_read_input_tokens": 43770,
      "output_tokens": 90,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 216,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 90,
          "cache_read_input_tokens": 43770,
          "cache_creation_input_tokens": 216,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 216
          },
          "type": "message"
        }
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

_source line 50 · 2026-05-15T01:58:48.258Z_

<details><summary>↩ Tool result · `toolu_01D4dg82TJiRKBk3hcGVe8xZ`</summary>

```text
1	% Auto-generated from literature_map.yaml — do not edit manually
2	
3	@inproceedings{angelopoulos2021conformal,
4	  title = {Uncertainty Sets for Image Classifiers using Conformal Prediction},
5	  author = {Angelopoulos, Anastasios N. and Bates, Stephen and Malik, Jitendra and Jordan, Michael I.},
6	  booktitle = {ICLR 2021},
7	  year = {2021},
8	  url = {https://arxiv.org/abs/2009.14193}
9	}
10	
11	@article{brown2024monkeys,
12	  title = {Large Language Monkeys: Scaling Inference Compute with Repeated Sampling},
13	  author = {Brown, Bradley and Juravsky, Jordan and Ehrlich, Ryan and Clark, Ronald and Le, Quoc V. and Ré, Christopher and Mirhoseini, Azalia},
14	  journal = {arXiv preprint arXiv:2407.21787},
15	  year = {2024},
16	  url = {https://arxiv.org/abs/2407.21787}
17	}
18	
19	@inproceedings{chen2024usc,
20	  title = {Universal Self-Consistency for Large Language Model Generation},
21	  author = {Chen, Xinyun and Aksitov, Renat and Alon, Uri and Ren, Jie and Xiao, Kefan and Yin, Pengcheng and Prakash, Sushant and Sutton, Charles and Wang, Xuezhi and Zhou, Denny},
22	  booktitle = {arXiv preprint (ICML 2024 Workshop ICL)},
23	  year = {2024},
24	  url = {https://arxiv.org/abs/2311.17311}
25	}
26	
27	@article{cobbe2021verifiers,
28	  title = {Training Verifiers to Solve Math Word Problems},
29	  author = {Cobbe, Karl and Kosaraju, Vineet and Bavarian, Mohammad and Chen, Mark and Jun, Heewoo and Kaiser, Lukasz and Plappert, Matthias and Tworek, Jerry and Hilton, Jacob and Nakano, Reiichiro and Hesse, Christopher and Schulman, John},
30	  journal = {arXiv preprint arXiv:2110.14168},
31	  year = {2021},
32	  url = {https://arxiv.org/abs/2110.14168}
33	}
34	
35	@inproceedings{culotta2004confidence,
36	  title = {Confidence Estimation for Information Extraction},
37	  author = {Culotta, Aron and McCallum, Andrew},
38	  booktitle = {HLT-NAACL 2004},
39	  year = {2004},
40	  url = {https://aclanthology.org/N04-4028/}
41	}
42	
43	@inproceedings{derczynski2017wnut,
44	  title = {Results of the WNUT2017 Shared Task on Novel and Emerging Entity Recognition},
45	  author = {Derczynski, Leon and Nichols, Eric and Erp, Marieke van and Limsopatham, Nut},
46	  booktitle = {W-NUT Workshop at EMNLP 2017},
47	  year = {2017},
48	  url = {https://aclanthology.org/W17-4418/}
49	}
50	
51	@inproceedings{desai2020calibration,
52	  title = {Calibration of Pre-trained Transformers},
53	  author = {Desai, Shrey and Durrett, Greg},
54	  booktitle = {Proceedings of the 2020 Conference on Empirical Methods in Natural Language Processing (EMNLP)},
55	  year = {2020},
56	  doi = {10.18653/v1/2020.emnlp-main.21},
57	  url = {http://dx.doi.org/10.18653/v1/2020.emnlp-main.21}
58	}
59	
60	@inproceedings{fisch2021conformal,
61	  title = {Few-Shot Conformal Prediction with Auxiliary Tasks},
62	  author = {Fisch, Adam and Schuster, Tal and Jaakkola, Tommi and Barzilay, Regina},
63	  booktitle = {ICML 2021},
64	  year = {2021},
65	  doi = {10.5555/3524938.3525234},
66	  url = {https://arxiv.org/abs/2102.08898}
67	}
68	
69	@article{fleiss1971agreement,
70	  title = {Measuring nominal scale agreement among many raters.},
71	  author = {Fleiss, Joseph L.},
72	  journal = {Psychological Bulletin},
73	  year = {1971},
74	  doi = {10.1037/h0031619},
75	  url = {http://dx.doi.org/10.1037/h0031619}
76	}
77	
78	@inproceedings{gal2016dropout,
79	  title = {Dropout as a Bayesian Approximation: Representing Model Uncertainty in Deep Learning},
80	  author = {Gal, Yarin and Ghahramani, Zoubin},
81	  booktitle = {ICML 2016},
82	  year = {2016},
83	  url = {https://arxiv.org/abs/1506.02142}
84	}
85	
86	@inproceedings{geifman2017selective,
87	  title = {Selective Classification for Deep Neural Networks},
88	  author = {Geifman, Yonatan and El-Yaniv, Ran},
89	  booktitle = {NeurIPS 2017},
90	  year = {2017},
91	  url = {https://arxiv.org/abs/1705.08500}
92	}
93	
94	@inproceedings{geng2024confidence,
95	  title = {A Survey of Confidence Estimation and Calibration in Large Language Models},
96	  author = {Geng, Jiahui and Cai, Fengyu and Wang, Yuxia and Koeppl, Heinz and Nakov, Preslav and Gurevych, Iryna},
97	  booktitle = {Proceedings of the 2024 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies (Volume 1: Long Papers)},
98	  year = {2024},
99	  doi = {10.18653/v1/2024.naacl-long.366},
100	  url = {http://dx.doi.org/10.18653/v1/2024.naacl-long.366}
101	}
102	
103	@inproceedings{guo2017calibration,
104	  title = {On Calibration of Modern Neural Networks},
105	  author = {Guo, Chuan and Pleiss, Geoff and Sun, Yu and Weinberger, Kilian Q.},
106	  booktitle = {ICML 2017},
107	  year = {2017},
108	  url = {https://arxiv.org/abs/1706.04599}
109	}
110	
111	@article{hobelsberger2025systematic,
112	  title = {Systematic Evaluation of Uncertainty Estimation Methods in Large Language Models},
113	  author = {Hobelsberger, Christian and Winner, Theresa and Nawroth, Andreas and Mitevski, Oliver and Haensch, Anna-Carolina},
114	  journal = {arXiv preprint arXiv:2510.20460},
115	  year = {2025},
116	  url = {https://arxiv.org/abs/2510.20460}
117	}
118	
119	@article{jaccard1901distribution,
120	  title = {Étude comparative de la distribution florale dans une portion des Alpes et du Jura},
121	  author = {Jaccard, Paul},
122	  journal = {Bulletin de la Société Vaudoise des Sciences Naturelles},
123	  year = {1901},
124	  url = {https://www.researchgate.net/publication/225035806}
125	}
126	
127	@inproceedings{josifoski2022genie,
128	  title = {{GenIE}: Generative Information Extraction},
129	  author = {Josifoski, Martin and De Cao, Nicola and Peyrard, Maxime and Petroni, Fabio and West, Robert},
130	  booktitle = {Proceedings of the 2022 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies (NAACL)},
131	  year = {2022},
132	  doi = {10.18653/v1/2022.naacl-main.342},
133	  url = {https://arxiv.org/abs/2112.08340}
134	}
135	
136	@article{kadavath2022language,
137	  title = {Language Models (Mostly) Know What They Know},
138	  author = {Kadavath, Saurav and Conerly, Tom and Askell, Amanda and Henighan, Tom and Drain, Dawn and Perez, Ethan and Schiefer, Nicholas and Hatfield-Dodds, Zac and DasSarma, Nova and Tran-Johnson, Eli and Johnston, Scott and El-Showk, Sheer and Jones, Andy and Elhage, Nelson and Hume, Tristan and Chen, Anna and Bai, Yuntao and Bowman, Sam and Fort, Stanislav and Ganguli, Deep and Hernandez, Danny and Jacobson, Josh and Kernion, Jackson and Kravec, Shauna and Lovitt, Liane and Ndousse, Kamal and Olsson, Catherine and Ringer, Sam and Amodei, Dario and Brown, Tom and Clark, Jack and Joseph, Nicholas and Mann, Ben and McCandlish, Sam and Olah, Chris and Kaplan, Jared},
139	  journal = {arXiv preprint arXiv:2207.05221},
140	  year = {2022},
141	  url = {https://arxiv.org/abs/2207.05221}
142	}
143	
144	@inproceedings{kang2025selfcertainty,
145	  title = {Scalable Best-of-N Selection for Large Language Models via Self-Certainty},
146	  author = {Kang, Zhewei and Zhao, Xuandong and Song, Dawn},
147	  booktitle = {NeurIPS 2025},
148	  year = {2025},
149	  url = {https://arxiv.org/abs/2502.18581}
150	}
151	
152	@inproceedings{kim2026reasc,
153	  title = {Reliability-Aware Adaptive Self-Consistency for Efficient Sampling in {LLM} Reasoning},
154	  author = {Kim, Junseok and Yang, Nakyeong and Min, Kyungmin and Jung, Kyomin},
155	  booktitle = {ACL 2026},
156	  year = {2026},
157	  url = {https://arxiv.org/abs/2601.02970}
158	}
159	
160	@article{kossen2024semantic,
161	  title = {Semantic Entropy Probes: Robust and Cheap Hallucination Detection in {LLMs}},
162	  author = {Kossen, Jannik and Han, Jiatong and Razzak, Muhammed and Schut, Lisa and Malik, Shreshth and Gal, Yarin},
163	  journal = {arXiv preprint arXiv:2406.15927},
164	  year = {2024},
165	  url = {https://arxiv.org/abs/2406.15927}
166	}
167	
168	@inproceedings{kuhn2023semantic,
169	  title = {Semantic Uncertainty: Linguistic Invariances for Uncertainty Estimation in Natural Language Generation},
170	  author = {Kuhn, Lorenz and Gal, Yarin and Farquhar, Sebastian},
171	  booktitle = {ICLR 2023},
172	  year = {2023},
173	  url = {https://arxiv.org/abs/2302.09664}
174	}
175	
176	@inproceedings{lakshminarayanan2017ensembles,
177	  title = {Simple and Scalable Predictive Uncertainty Estimation using Deep Ensembles},
178	  author = {Lakshminarayanan, Balaji and Pritzel, Alexander and Blundell, Charles},
179	  booktitle = {NeurIPS 2017},
180	  year = {2017},
181	  url = {https://arxiv.org/abs/1612.01474}
182	}
183	
184	@inproceedings{li2023codeie,
185	  title = {{CodeIE}: Large Code Generation Models are Better Few-Shot Information Extractors},
186	  author = {Li, Peng and Sun, Tianxiang and Tang, Qiong and Yan, Hang and Wu, Yuanbin and Huang, Xuanjing and Qiu, Xipeng},
187	  booktitle = {Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics (ACL)},
188	  year = {2023},
189	  doi = {10.18653/v1/2023.acl-long.855},
190	  url = {https://arxiv.org/abs/2305.05711}
191	}
192	
193	@inproceedings{lightman2024verify,
194	  title = {Let's Verify Step by Step},
195	  author = {Lightman, Hunter and Kosaraju, Vineet and Burda, Yura and Edwards, Harri and Baker, Bowen and Lee, Teddy and Leike, Jan and Schulman, John and Sutskever, Ilya and Cobbe, Karl},
196	  booktitle = {ICLR 2024},
197	  year = {2024},
198	  url = {https://arxiv.org/abs/2305.20050}
199	}
200	
201	@inproceedings{luan2018scierc,
202	  title = {Multi-Task Identification of Entities, Relations, and Coreference for Scientific Knowledge Graph Construction},
203	  author = {Luan, Yi and He, Luheng and Ostendorf, Mari and Hajishirzi, Hannaneh},
204	  booktitle = {Proceedings of the 2018 Conference on Empirical Methods in Natural Language Processing},
205	  year = {2018},
206	  doi = {10.18653/v1/D18-1360},
207	  url = {http://dx.doi.org/10.18653/v1/D18-1360}
208	}
209	
210	@inproceedings{manakul2023selfcheckgpt,
211	  title = {SelfCheckGPT: Zero-Resource Black-Box Hallucination Detection for Generative Large Language Models},
212	  author = {Manakul, Potsawee and Liusie, Adian and Gales, Mark},
213	  booktitle = {Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing},
214	  year = {2023},
215	  doi = {10.18653/v1/2023.emnlp-main.557},
216	  url = {http://dx.doi.org/10.18653/v1/2023.emnlp-main.557}
217	}
218	
219	@article{nedellec2026consistency,
220	  title = {Consistency–accuracy correlation in hard-prompted LLMs for entity and relation extraction: empirical findings from plant-health data},
221	  author = {Yao, Xinzhi and Nédellec, Claire and Xia, Jingbo and Bossy, Robert},
222	  journal = {Genomics \& Informatics},
223	  year = {2026},
224	  doi = {10.1186/s44342-025-00063-2},
225	  url = {http://dx.doi.org/10.1186/s44342-025-00063-2}
226	}
227	
228	@article{oh2025latentsc,
229	  title = {Latent Self-Consistency for Reliable Majority-Set Selection in Short- and Long-Answer Reasoning},
230	  author = {Oh, Jungsuk and Lee, Jay-Yoon},
231	  journal = {arXiv preprint arXiv:2508.18395},
232	  year = {2025},
233	  url = {https://arxiv.org/abs/2508.18395}
234	}
235	
236	@inproceedings{sainz2024gollie,
237	  title = {{GoLLIE}: Annotation Guidelines improve Zero-Shot Information-Extraction},
238	  author = {Sainz, Oscar and García-Ferrero, Iker and Agerri, Rodrigo and Lacalle, Oier Lopez de and Rigau, German and Agirre, Eneko},
239	  booktitle = {ICLR 2024},
240	  year = {2024},
241	  url = {https://arxiv.org/abs/2310.03668}
242	}
243	
244	@inproceedings{shelmanov2021active,
245	  title = {Active Learning for Sequence Tagging with Deep Pre-trained Models and Bayesian Uncertainty Estimates},
246	  author = {Shelmanov, Artem and Puzyrev, Dmitri and Kupriyanova, Lyubov and Belyakov, Denis and Larionov, Daniil and Khromov, Nikita and Kozlova, Olga and Artemova, Ekaterina and Dylov, Dmitry V. and Panchenko, Alexander},
247	  booktitle = {Proceedings of the 16th Conference of the European Chapter of the Association for Computational Linguistics: Main Volume},
248	  year = {2021},
249	  doi = {10.18653/v1/2021.eacl-main.145},
250	  url = {http://dx.doi.org/10.18653/v1/2021.eacl-main.145}
251	}
252	
253	@inproceedings{snell2024scaling,
254	  title = {Scaling {LLM} Test-Time Compute Optimally can be More Effective than Scaling Model Parameters},
255	  author = {Snell, Charlie and Lee, Jaehoon and Xu, Kelvin and Kumar, Aviral},
256	  booktitle = {ICLR 2025},
257	  year = {2024},
258	  url = {https://arxiv.org/abs/2408.03314}
259	}
260	
261	@inproceedings{taubenfeld2025cisc,
262	  title = {Confidence Improves Self-Consistency in LLMs},
263	  author = {Taubenfeld, Amir and Sheffer, Tom and Ofek, Eran and Feder, Amir and Goldstein, Ariel and Gekhman, Zorik and Yona, Gal},
264	  booktitle = {Findings of the Association for Computational Linguistics: ACL 2025},
265	  year = {2025},
266	  doi = {10.18653/v1/2025.findings-acl.1030},
267	  url = {http://dx.doi.org/10.18653/v1/2025.findings-acl.1030}
268	}
269	
270	@inproceedings{thirukovalluru2024atomic,
271	  title = {Atomic Self-Consistency for Better Long Form Generations},
272	  author = {Thirukovalluru, Raghuveer and Huang, Yukun and Dhingra, Bhuwan},
273	  booktitle = {Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing},
274	  year = {2024},
275	  doi = {10.18653/v1/2024.emnlp-main.706},
276	  url = {http://dx.doi.org/10.18653/v1/2024.emnlp-main.706}
277	}
278	
279	@inproceedings{tjongkimsang2003conll,
280	  title = {Introduction to the {CoNLL}-2003 Shared Task: Language-Independent Named Entity Recognition},
281	  author = {Sang, Erik F. Tjong Kim and Meulder, Fien De},
282	  booktitle = {CoNLL 2003},
283	  year = {2003},
284	  url = {https://aclanthology.org/W03-0419/}
285	}
286	
287	@inproceedings{vashurin2025cocoa,
288	  title = {Uncertainty Quantification for {LLMs} through Minimum Bayes Risk: Bridging Confidence and Consistency},
289	  author = {Vashurin, Roman and Goloburda, Maiya and Ilina, Albina and Rubashevskii, Aleksandr and Nakov, Preslav and Shelmanov, Artem and Panov, Maxim},
290	  booktitle = {NeurIPS 2025},
291	  year = {2025},
292	  url = {https://arxiv.org/abs/2502.04964}
293	}
294	
295	@inproceedings{wadhwa2023revisiting,
296	  title = {Revisiting Relation Extraction in the era of Large Language Models},
297	  author = {Wadhwa, Somin and Amir, Silvio and Wallace, Byron},
298	  booktitle = {Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)},
299	  year = {2023},
300	  doi = {10.18653/v1/2023.acl-long.868},
301	  url = {http://dx.doi.org/10.18653/v1/2023.acl-long.868}
302	}
303	
304	@article{wang2023instructuie,
305	  title = {{InstructUIE}: Multi-task Instruction Tuning for Unified Information Extraction},
306	  author = {Wang, Xiao and Zhou, Weikang and Zu, Can and Xia, Han and Chen, Tianze and Zhang, Yuansen and Zheng, Rui and Ye, Junjie and Zhang, Qi and Gui, Tao and Kang, Jihua and Yang, Jingsheng and Li, Siyuan and Du, Chunsai},
307	  journal = {arXiv preprint arXiv:2304.08085},
308	  year = {2023},
309	  url = {https://arxiv.org/abs/2304.08085}
310	}
311	
312	@inproceedings{wang2023selfconsistency,
313	  title = {Self-Consistency Improves Chain of Thought Reasoning in Language Models},
314	  author = {Wang, Xuezhi and Wei, Jason and Schuurmans, Dale and Le, Quoc and Chi, Ed and Narang, Sharan and Chowdhery, Aakanksha and Zhou, Denny},
315	  booktitle = {ICLR 2023},
316	  year = {2023},
317	  url = {https://arxiv.org/abs/2203.11171}
318	}
319	
320	@inproceedings{wang2024mathshepherd,
321	  title = {Math-Shepherd: Verify and Reinforce {LLMs} Step-by-step without Human Annotations},
322	  author = {Wang, Peiyi and Li, Lei and Shao, Zhihong and Xu, Runxin and Dai, Damai and Li, Yifei and Chen, Deli and Wu, Yu and Sui, Zhifang},
323	  booktitle = {ACL 2024},
324	  year = {2024},
325	  url = {https://arxiv.org/abs/2312.08935}
326	}
327	
328	@inproceedings{wang2025rankedvoting,
329	  title = {Ranked Voting based Self-Consistency of Large Language Models},
330	  author = {Wang, Weiqin and Wang, Yile and Huang, Hui},
331	  booktitle = {ACL Findings 2025},
332	  year = {2025},
333	  url = {https://arxiv.org/abs/2505.10772}
334	}
335	
336	@article{wen2025know,
337	  title = {Know Your Limits: A Survey of Abstention in Large Language Models},
338	  author = {Wen, Bingbing and Yao, Jihan and Feng, Shangbin and Xu, Chenjun and Tsvetkov, Yulia and Howe, Bill and Wang, Lucy Lu},
339	  journal = {Transactions of the Association for Computational Linguistics},
340	  year = {2025},
341	  doi = {10.1162/tacl_a_00754},
342	  url = {http://dx.doi.org/10.1162/tacl_a_00754}
343	}
344	
345	@article{willard2023guided,
346	  title = {Efficient Guided Generation for Large Language Models},
347	  author = {Willard, Brandon T. and Louf, Rémi},
348	  journal = {arXiv preprint arXiv:2307.09702},
349	  year = {2023},
350	  url = {https://arxiv.org/abs/2307.09702}
351	}
352	
353	@inproceedings{xia2025survey,
354	  title = {A Survey of Uncertainty Estimation Methods on Large Language Models},
355	  author = {Xia, Zhiqiu and Xu, Jinxuan and Zhang, Yuqian and Liu, Hang},
356	  booktitle = {ACL Findings 2025},
357	  year = {2025},
358	  url = {https://aclanthology.org/2025.findings-acl.1101/}
359	}
360	
361	@article{xiao2019uncertainty,
362	  title = {Quantifying Uncertainties in Natural Language Processing Tasks},
363	  author = {Xiao, Yijun and Wang, William Yang},
364	  journal = {Proceedings of the AAAI Conference on Artificial Intelligence},
365	  year = {2019},
366	  doi = {10.1609/aaai.v33i01.33017322},
367	  url = {http://dx.doi.org/10.1609/aaai.v33i01.33017322}
368	}
369	
370	@inproceedings{zhang2023ener,
371	  title = {E-NER: Evidential Deep Learning for Trustworthy Named Entity Recognition},
372	  author = {Zhang, Zhen and Hu, Mengting and Zhao, Shiwan and Huang, Minlie and Wang, Haotian and Liu, Lemao and Zhang, Zhirui and Liu, Zhe and Wu, Bingzhe},
373	  booktitle = {Findings of the Association for Computational Linguistics: ACL 2023},
374	  year = {2023},
375	  doi = {10.18653/v1/2023.findings-acl.103},
376	  url = {http://dx.doi.org/10.18653/v1/2023.findings-acl.103}
377	}
378	
379	@inproceedings{zhou2024uniner,
380	  title = {{UniversalNER}: Targeted Distillation from Large Language Models for Open Named Entity Recognition},
381	  author = {Zhou, Wenxuan and Zhang, Sheng and Gu, Yu and Chen, Muhao and Poon, Hoifung},
382	  booktitle = {Proceedings of the International Conference on Learning Representations (ICLR)},
383	  year = {2024},
384	  url = {https://arxiv.org/abs/2308.03279}
385	}
386	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b95728d1-6b33-4f06-9f75-685435c69e36",
  "isSidechain": false,
  "promptId": "e032b776-5e54-467c-9321-aeb2f2c75513",
  "type": "user",
  "uuid": "189e5f3c-7f0e-429b-b8f2-f27f0fdcbfcb",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/references.bib",
      "content": "% Auto-generated from literature_map.yaml — do not edit manually\n\n@inproceedings{angelopoulos2021conformal,\n  title = {Uncertainty Sets for Image Classifiers using Conformal Prediction},\n  author = {Angelopoulos, Anastasios N. and Bates, Stephen and Malik, Jitendra and Jordan, Michael I.},\n  booktitle = {ICLR 2021},\n  year = {2021},\n  url = {https://arxiv.org/abs/2009.14193}\n}\n\n@article{brown2024monkeys,\n  title = {Large Language Monkeys: Scaling Inference Compute with Repeated Sampling},\n  author = {Brown, Bradley and Juravsky, Jordan and Ehrlich, Ryan and Clark, Ronald and Le, Quoc V. and Ré, Christopher and Mirhoseini, Azalia},\n  journal = {arXiv preprint arXiv:2407.21787},\n  year = {2024},\n  url = {https://arxiv.org/abs/2407.21787}\n}\n\n@inproceedings{chen2024usc,\n  title = {Universal Self-Consistency for Large Language Model Generation},\n  author = {Chen, Xinyun and Aksitov, Renat and Alon, Uri and Ren, Jie and Xiao, Kefan and Yin, Pengcheng and Prakash, Sushant and Sutton, Charles and Wang, Xuezhi and Zhou, Denny},\n  booktitle = {arXiv preprint (ICML 2024 Workshop ICL)},\n  year = {2024},\n  url = {https://arxiv.org/abs/2311.17311}\n}\n\n@article{cobbe2021verifiers,\n  title = {Training Verifiers to Solve Math Word Problems},\n  author = {Cobbe, Karl and Kosaraju, Vineet and Bavarian, Mohammad and Chen, Mark and Jun, Heewoo and Kaiser, Lukasz and Plappert, Matthias and Tworek, Jerry and Hilton, Jacob and Nakano, Reiichiro and Hesse, Christopher and Schulman, John},\n  journal = {arXiv preprint arXiv:2110.14168},\n  year = {2021},\n  url = {https://arxiv.org/abs/2110.14168}\n}\n\n@inproceedings{culotta2004confidence,\n  title = {Confidence Estimation for Information Extraction},\n  author = {Culotta, Aron and McCallum, Andrew},\n  booktitle = {HLT-NAACL 2004},\n  year = {2004},\n  url = {https://aclanthology.org/N04-4028/}\n}\n\n@inproceedings{derczynski2017wnut,\n  title = {Results of the WNUT2017 Shared Task on Novel and Emerging Entity Recognition},\n  author = {Derczynski, Leon and Nichols, Eric and Erp, Marieke van and Limsopatham, Nut},\n  booktitle = {W-NUT Workshop at EMNLP 2017},\n  year = {2017},\n  url = {https://aclanthology.org/W17-4418/}\n}\n\n@inproceedings{desai2020calibration,\n  title = {Calibration of Pre-trained Transformers},\n  author = {Desai, Shrey and Durrett, Greg},\n  booktitle = {Proceedings of the 2020 Conference on Empirical Methods in Natural Language Processing (EMNLP)},\n  year = {2020},\n  doi = {10.18653/v1/2020.emnlp-main.21},\n  url = {http://dx.doi.org/10.18653/v1/2020.emnlp-main.21}\n}\n\n@inproceedings{fisch2021conformal,\n  title = {Few-Shot Conformal Prediction with Auxiliary Tasks},\n  author = {Fisch, Adam and Schuster, Tal and Jaakkola, Tommi and Barzilay, Regina},\n  booktitle = {ICML 2021},\n  year = {2021},\n  doi = {10.5555/3524938.3525234},\n  url = {https://arxiv.org/abs/2102.08898}\n}\n\n@article{fleiss1971agreement,\n  title = {Measuring nominal scale agreement among many raters.},\n  author = {Fleiss, Joseph L.},\n  journal = {Psychological Bulletin},\n  year = {1971},\n  doi = {10.1037/h0031619},\n  url = {http://dx.doi.org/10.1037/h0031619}\n}\n\n@inproceedings{gal2016dropout,\n  title = {Dropout as a Bayesian Approximation: Representing Model Uncertainty in Deep Learning},\n  author = {Gal, Yarin and Ghahramani, Zoubin},\n  booktitle = {ICML 2016},\n  year = {2016},\n  url = {https://arxiv.org/abs/1506.02142}\n}\n\n@inproceedings{geifman2017selective,\n  title = {Selective Classification for Deep Neural Networks},\n  author = {Geifman, Yonatan and El-Yaniv, Ran},\n  booktitle = {NeurIPS 2017},\n  year = {2017},\n  url = {https://arxiv.org/abs/1705.08500}\n}\n\n@inproceedings{geng2024confidence,\n  title = {A Survey of Confidence Estimation and Calibration in Large Language Models},\n  author = {Geng, Jiahui and Cai, Fengyu and Wang, Yuxia and Koeppl, Heinz and Nakov, Preslav and Gurevych, Iryna},\n  booktitle = {Proceedings of the 2024 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies (Volume 1: Long Papers)},\n  year = {2024},\n  doi = {10.18653/v1/2024.naacl-long.366},\n  url = {http://dx.doi.org/10.18653/v1/2024.naacl-long.366}\n}\n\n@inproceedings{guo2017calibration,\n  title = {On Calibration of Modern Neural Networks},\n  author = {Guo, Chuan and Pleiss, Geoff and Sun, Yu and Weinberger, Kilian Q.},\n  booktitle = {ICML 2017},\n  year = {2017},\n  url = {https://arxiv.org/abs/1706.04599}\n}\n\n@article{hobelsberger2025systematic,\n  title = {Systematic Evaluation of Uncertainty Estimation Methods in Large Language Models},\n  author = {Hobelsberger, Christian and Winner, Theresa and Nawroth, Andreas and Mitevski, Oliver and Haensch, Anna-Carolina},\n  journal = {arXiv preprint arXiv:2510.20460},\n  year = {2025},\n  url = {https://arxiv.org/abs/2510.20460}\n}\n\n@article{jaccard1901distribution,\n  title = {Étude comparative de la distribution florale dans une portion des Alpes et du Jura},\n  author = {Jaccard, Paul},\n  journal = {Bulletin de la Société Vaudoise des Sciences Naturelles},\n  year = {1901},\n  url = {https://www.researchgate.net/publication/225035806}\n}\n\n@inproceedings{josifoski2022genie,\n  title = {{GenIE}: Generative Information Extraction},\n  author = {Josifoski, Martin and De Cao, Nicola and Peyrard, Maxime and Petroni, Fabio and West, Robert},\n  booktitle = {Proceedings of the 2022 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies (NAACL)},\n  year = {2022},\n  doi = {10.18653/v1/2022.naacl-main.342},\n  url = {https://arxiv.org/abs/2112.08340}\n}\n\n@article{kadavath2022language,\n  title = {Language Models (Mostly) Know What They Know},\n  author = {Kadavath, Saurav and Conerly, Tom and Askell, Amanda and Henighan, Tom and Drain, Dawn and Perez, Ethan and Schiefer, Nicholas and Hatfield-Dodds, Zac and DasSarma, Nova and Tran-Johnson, Eli and Johnston, Scott and El-Showk, Sheer and Jones, Andy and Elhage, Nelson and Hume, Tristan and Chen, Anna and Bai, Yuntao and Bowman, Sam and Fort, Stanislav and Ganguli, Deep and Hernandez, Danny and Jacobson, Josh and Kernion, Jackson and Kravec, Shauna and Lovitt, Liane and Ndousse, Kamal and Olsson, Catherine and Ringer, Sam and Amodei, Dario and Brown, Tom and Clark, Jack and Joseph, Nicholas and Mann, Ben and McCandlish, Sam and Olah, Chris and Kaplan, Jared},\n  journal = {arXiv preprint arXiv:2207.05221},\n  year = {2022},\n  url = {https://arxiv.org/abs/2207.05221}\n}\n\n@inproceedings{kang2025selfcertainty,\n  title = {Scalable Best-of-N Selection for Large Language Models via Self-Certainty},\n  author = {Kang, Zhewei and Zhao, Xuandong and Song, Dawn},\n  booktitle = {NeurIPS 2025},\n  year = {2025},\n  url = {https://arxiv.org/abs/2502.18581}\n}\n\n@inproceedings{kim2026reasc,\n  title = {Reliability-Aware Adaptive Self-Consistency for Efficient Sampling in {LLM} Reasoning},\n  author = {Kim, Junseok and Yang, Nakyeong and Min, Kyungmin and Jung, Kyomin},\n  booktitle = {ACL 2026},\n  year = {2026},\n  url = {https://arxiv.org/abs/2601.02970}\n}\n\n@article{kossen2024semantic,\n  title = {Semantic Entropy Probes: Robust and Cheap Hallucination Detection in {LLMs}},\n  author = {Kossen, Jannik and Han, Jiatong and Razzak, Muhammed and Schut, Lisa and Malik, Shreshth and Gal, Yarin},\n  journal = {arXiv preprint arXiv:2406.15927},\n  year = {2024},\n  url = {https://arxiv.org/abs/2406.15927}\n}\n\n@inproceedings{kuhn2023semantic,\n  title = {Semantic Uncertainty: Linguistic Invariances for Uncertainty Estimation in Natural Language Generation},\n  author = {Kuhn, Lorenz and Gal, Yarin and Farquhar, Sebastian},\n  booktitle = {ICLR 2023},\n  year = {2023},\n  url = {https://arxiv.org/abs/2302.09664}\n}\n\n@inproceedings{lakshminarayanan2017ensembles,\n  title = {Simple and Scalable Predictive Uncertainty Estimation using Deep Ensembles},\n  author = {Lakshminarayanan, Balaji and Pritzel, Alexander and Blundell, Charles},\n  booktitle = {NeurIPS 2017},\n  year = {2017},\n  url = {https://arxiv.org/abs/1612.01474}\n}\n\n@inproceedings{li2023codeie,\n  title = {{CodeIE}: Large Code Generation Models are Better Few-Shot Information Extractors},\n  author = {Li, Peng and Sun, Tianxiang and Tang, Qiong and Yan, Hang and Wu, Yuanbin and Huang, Xuanjing and Qiu, Xipeng},\n  booktitle = {Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics (ACL)},\n  year = {2023},\n  doi = {10.18653/v1/2023.acl-long.855},\n  url = {https://arxiv.org/abs/2305.05711}\n}\n\n@inproceedings{lightman2024verify,\n  title = {Let's Verify Step by Step},\n  author = {Lightman, Hunter and Kosaraju, Vineet and Burda, Yura and Edwards, Harri and Baker, Bowen and Lee, Teddy and Leike, Jan and Schulman, John and Sutskever, Ilya and Cobbe, Karl},\n  booktitle = {ICLR 2024},\n  year = {2024},\n  url = {https://arxiv.org/abs/2305.20050}\n}\n\n@inproceedings{luan2018scierc,\n  title = {Multi-Task Identification of Entities, Relations, and Coreference for Scientific Knowledge Graph Construction},\n  author = {Luan, Yi and He, Luheng and Ostendorf, Mari and Hajishirzi, Hannaneh},\n  booktitle = {Proceedings of the 2018 Conference on Empirical Methods in Natural Language Processing},\n  year = {2018},\n  doi = {10.18653/v1/D18-1360},\n  url = {http://dx.doi.org/10.18653/v1/D18-1360}\n}\n\n@inproceedings{manakul2023selfcheckgpt,\n  title = {SelfCheckGPT: Zero-Resource Black-Box Hallucination Detection for Generative Large Language Models},\n  author = {Manakul, Potsawee and Liusie, Adian and Gales, Mark},\n  booktitle = {Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing},\n  year = {2023},\n  doi = {10.18653/v1/2023.emnlp-main.557},\n  url = {http://dx.doi.org/10.18653/v1/2023.emnlp-main.557}\n}\n\n@article{nedellec2026consistency,\n  title = {Consistency–accuracy correlation in hard-prompted LLMs for entity and relation extraction: empirical findings from plant-health data},\n  author = {Yao, Xinzhi and Nédellec, Claire and Xia, Jingbo and Bossy, Robert},\n  journal = {Genomics \\& Informatics},\n  year = {2026},\n  doi = {10.1186/s44342-025-00063-2},\n  url = {http://dx.doi.org/10.1186/s44342-025-00063-2}\n}\n\n@article{oh2025latentsc,\n  title = {Latent Self-Consistency for Reliable Majority-Set Selection in Short- and Long-Answer Reasoning},\n  author = {Oh, Jungsuk and Lee, Jay-Yoon},\n  journal = {arXiv preprint arXiv:2508.18395},\n  year = {2025},\n  url = {https://arxiv.org/abs/2508.18395}\n}\n\n@inproceedings{sainz2024gollie,\n  title = {{GoLLIE}: Annotation Guidelines improve Zero-Shot Information-Extraction},\n  author = {Sainz, Oscar and García-Ferrero, Iker and Agerri, Rodrigo and Lacalle, Oier Lopez de and Rigau, German and Agirre, Eneko},\n  booktitle = {ICLR 2024},\n  year = {2024},\n  url = {https://arxiv.org/abs/2310.03668}\n}\n\n@inproceedings{shelmanov2021active,\n  title = {Active Learning for Sequence Tagging with Deep Pre-trained Models and Bayesian Uncertainty Estimates},\n  author = {Shelmanov, Artem and Puzyrev, Dmitri and Kupriyanova, Lyubov and Belyakov, Denis and Larionov, Daniil and Khromov, Nikita and Kozlova, Olga and Artemova, Ekaterina and Dylov, Dmitry V. and Panchenko, Alexander},\n  booktitle = {Proceedings of the 16th Conference of the European Chapter of the Association for Computational Linguistics: Main Volume},\n  year = {2021},\n  doi = {10.18653/v1/2021.eacl-main.145},\n  url = {http://dx.doi.org/10.18653/v1/2021.eacl-main.145}\n}\n\n@inproceedings{snell2024scaling,\n  title = {Scaling {LLM} Test-Time Compute Optimally can be More Effective than Scaling Model Parameters},\n  author = {Snell, Charlie and Lee, Jaehoon and Xu, Kelvin and Kumar, Aviral},\n  booktitle = {ICLR 2025},\n  year = {2024},\n  url = {https://arxiv.org/abs/2408.03314}\n}\n\n@inproceedings{taubenfeld2025cisc,\n  title = {Confidence Improves Self-Consistency in LLMs},\n  author = {Taubenfeld, Amir and Sheffer, Tom and Ofek, Eran and Feder, Amir and Goldstein, Ariel and Gekhman, Zorik and Yona, Gal},\n  booktitle = {Findings of the Association for Computational Linguistics: ACL 2025},\n  year = {2025},\n  doi = {10.18653/v1/2025.findings-acl.1030},\n  url = {http://dx.doi.org/10.18653/v1/2025.findings-acl.1030}\n}\n\n@inproceedings{thirukovalluru2024atomic,\n  title = {Atomic Self-Consistency for Better Long Form Generations},\n  author = {Thirukovalluru, Raghuveer and Huang, Yukun and Dhingra, Bhuwan},\n  booktitle = {Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing},\n  year = {2024},\n  doi = {10.18653/v1/2024.emnlp-main.706},\n  url = {http://dx.doi.org/10.18653/v1/2024.emnlp-main.706}\n}\n\n@inproceedings{tjongkimsang2003conll,\n  title = {Introduction to the {CoNLL}-2003 Shared Task: Language-Independent Named Entity Recognition},\n  author = {Sang, Erik F. Tjong Kim and Meulder, Fien De},\n  booktitle = {CoNLL 2003},\n  year = {2003},\n  url = {https://aclanthology.org/W03-0419/}\n}\n\n@inproceedings{vashurin2025cocoa,\n  title = {Uncertainty Quantification for {LLMs} through Minimum Bayes Risk: Bridging Confidence and Consistency},\n  author = {Vashurin, Roman and Goloburda, Maiya and Ilina, Albina and Rubashevskii, Aleksandr and Nakov, Preslav and Shelmanov, Artem and Panov, Maxim},\n  booktitle = {NeurIPS 2025},\n  year = {2025},\n  url = {https://arxiv.org/abs/2502.04964}\n}\n\n@inproceedings{wadhwa2023revisiting,\n  title = {Revisiting Relation Extraction in the era of Large Language Models},\n  author = {Wadhwa, Somin and Amir, Silvio and Wallace, Byron},\n  booktitle = {Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)},\n  year = {2023},\n  doi = {10.18653/v1/2023.acl-long.868},\n  url = {http://dx.doi.org/10.18653/v1/2023.acl-long.868}\n}\n\n@article{wang2023instructuie,\n  title = {{InstructUIE}: Multi-task Instruction Tuning for Unified Information Extraction},\n  author = {Wang, Xiao and Zhou, Weikang and Zu, Can and Xia, Han and Chen, Tianze and Zhang, Yuansen and Zheng, Rui and Ye, Junjie and Zhang, Qi and Gui, Tao and Kang, Jihua and Yang, Jingsheng and Li, Siyuan and Du, Chunsai},\n  journal = {arXiv preprint arXiv:2304.08085},\n  year = {2023},\n  url = {https://arxiv.org/abs/2304.08085}\n}\n\n@inproceedings{wang2023selfconsistency,\n  title = {Self-Consistency Improves Chain of Thought Reasoning in Language Models},\n  author = {Wang, Xuezhi and Wei, Jason and Schuurmans, Dale and Le, Quoc and Chi, Ed and Narang, Sharan and Chowdhery, Aakanksha and Zhou, Denny},\n  booktitle = {ICLR 2023},\n  year = {2023},\n  url = {https://arxiv.org/abs/2203.11171}\n}\n\n@inproceedings{wang2024mathshepherd,\n  title = {Math-Shepherd: Verify and Reinforce {LLMs} Step-by-step without Human Annotations},\n  author = {Wang, Peiyi and Li, Lei and Shao, Zhihong and Xu, Runxin and Dai, Damai and Li, Yifei and Chen, Deli and Wu, Yu and Sui, Zhifang},\n  booktitle = {ACL 2024},\n  year = {2024},\n  url = {https://arxiv.org/abs/2312.08935}\n}\n\n@inproceedings{wang2025rankedvoting,\n  title = {Ranked Voting based Self-Consistency of Large Language Models},\n  author = {Wang, Weiqin and Wang, Yile and Huang, Hui},\n  booktitle = {ACL Findings 2025},\n  year = {2025},\n  url = {https://arxiv.org/abs/2505.10772}\n}\n\n@article{wen2025know,\n  title = {Know Your Limits: A Survey of Abstention in Large Language Models},\n  author = {Wen, Bingbing and Yao, Jihan and Feng, Shangbin and Xu, Chenjun and Tsvetkov, Yulia and Howe, Bill and Wang, Lucy Lu},\n  journal = {Transactions of the Association for Computational Linguistics},\n  year = {2025},\n  doi = {10.1162/tacl_a_00754},\n  url = {http://dx.doi.org/10.1162/tacl_a_00754}\n}\n\n@article{willard2023guided,\n  title = {Efficient Guided Generation for Large Language Models},\n  author = {Willard, Brandon T. and Louf, Rémi},\n  journal = {arXiv preprint arXiv:2307.09702},\n  year = {2023},\n  url = {https://arxiv.org/abs/2307.09702}\n}\n\n@inproceedings{xia2025survey,\n  title = {A Survey of Uncertainty Estimation Methods on Large Language Models},\n  author = {Xia, Zhiqiu and Xu, Jinxuan and Zhang, Yuqian and Liu, Hang},\n  booktitle = {ACL Findings 2025},\n  year = {2025},\n  url = {https://aclanthology.org/2025.findings-acl.1101/}\n}\n\n@article{xiao2019uncertainty,\n  title = {Quantifying Uncertainties in Natural Language Processing Tasks},\n  author = {Xiao, Yijun and Wang, William Yang},\n  journal = {Proceedings of the AAAI Conference on Artificial Intelligence},\n  year = {2019},\n  doi = {10.1609/aaai.v33i01.33017322},\n  url = {http://dx.doi.org/10.1609/aaai.v33i01.33017322}\n}\n\n@inproceedings{zhang2023ener,\n  title = {E-NER: Evidential Deep Learning for Trustworthy Named Entity Recognition},\n  author = {Zhang, Zhen and Hu, Mengting and Zhao, Shiwan and Huang, Minlie and Wang, Haotian and Liu, Lemao and Zhang, Zhirui and Liu, Zhe and Wu, Bingzhe},\n  booktitle = {Findings of the Association for Computational Linguistics: ACL 2023},\n  year = {2023},\n  doi = {10.18653/v1/2023.findings-acl.103},\n  url = {http://dx.doi.org/10.18653/v1/2023.findings-acl.103}\n}\n\n@inproceedings{zhou2024uniner,\n  title = {{UniversalNER}: Targeted Distillation from Large Language Models for Open Named Entity Recognition},\n  author = {Zhou, Wenxuan and Zhang, Sheng and Gu, Yu and Chen, Muhao and Poon, Hoifung},\n  booktitle = {Proceedings of the International Conference on Learning Representations (ICLR)},\n  year = {2024},\n  url = {https://arxiv.org/abs/2308.03279}\n}\n",
      "numLines": 386,
      "startLine": 1,
      "totalLines": 386
    }
  },
  "sourceToolAssistantUUID": "b95728d1-6b33-4f06-9f75-685435c69e36",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_1_68ddc296",
  "sessionId": "cd3ac2da-cdcc-4c5b-9409-914107331cb2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 51_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[Round 1 审稿请求]: ## 交叉分享：Reviewer 2 的完整 Round 1 审稿意见  请逐条回应 Reviewer 2 的每个问题：用 [AGREE] 表示同意并说明理由，或 [REBUT] 表示反驳并引用论文具体 Section/Table/Figure 作为证据。  ---  以下是 Reviewer 2 的完整审稿原文：  ### 总体评分 **Overall**: 3.…",
  "leafUuid": "189e5f3c-7f0e-429b-b8f2-f27f0fdcbfcb",
  "sessionId": "cd3ac2da-cdcc-4c5b-9409-914107331cb2"
}
```

---

### Runtime record

_source line 52_

```json
{
  "type": "ai-title",
  "aiTitle": "Respond to EMNLP Reviewer 2 Round 1 comments",
  "sessionId": "cd3ac2da-cdcc-4c5b-9409-914107331cb2"
}
```

---

### Assistant

_source line 53 · 2026-05-15T02:00:01.110Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have a thorough understanding of the paper. Let me compose my cross-review response to Reviewer 2's points.

Let me go through each issue:

**N1** [critical] "Correlation-selection gap" 的解释力不足——4/5 个 signals 是 instance-level 的，它们不能做 per-sample selection 是定义上的必然结果，不是发现。真正需要深入分析的是唯一的 per-sample signal (logprob) 为何也失败（calibration? length bias? constrained decoding 干扰?），但论文对此几乎没有分析。


The paper does acknowledge the instance-level limitation in Section 3.3 and the Discussion, but the reviewer has a point—they actually test instance-level signals by selecting the sample closest to consensus, so it's not purely definitional. The real gap is that logprob, the only true per-sample signal, also fails, and the paper doesn't adequately investigate why (whether it's calibration issues, length bias, or constrained decoding interference). proximity approach IS a per-sample selection mechanism derived from instance-level signals. But R2's point that the gap for 4/5 signals is somewhat expected by design is valid.

For logprob, the paper shows it achieves 0.650 vs greedy 0.644 (p=0.39) on NER. The paper doesn't deeply analyze WHY logprob fails. This is a fair criticism. 

However, I should note that the paper DOES provide some analysis: Section 5.1 conditional filtering shows "Logprob RE collapses to ρ=0.011", and Appendix D mentions that LOO-SJ has Δρ=-0.014. Also the reliability diagrams (Appendix B) show calibration analysis. But the specific analysis of logprob failure mechanisms is indeed thin.

The paper does define the gap clearly and consensus-proximity selection is a meaningful contribution, though the analysis of why logprob specifically underperforms remains shallow. R2 raises a valid point about per-sample signal exploration—LOO-SJ is computed in Appendix D but only for evaluation purposes, not tested as a selection mechanism itself, even though it's a natural structural signal that could be applied per-sample.

-sample signal for selection - for each sample y_i, compute its SJ against all other samples (leave-one-out), giving a per-sample score. This is actually a very natural idea.

Actually, re-reading the method section more carefully: the paper says "instance-level signals select the sample closest to the consensus output" (Section 3.3). This IS essentially consensus-proximity ranking. So the paper DOES use it but doesn't analyze it as a distinct signal? Let me re-check...

Table 5 shows selection results. For instance-level signals like SJ, Voting, they show selection F1. This means they ARE using some form of per-sample ranking derived from instance-level signals. The paper says they "select the sample closest to the consensus output." So consensus-proximity IS being used, but R2 wants it analyzed more explicitly.

For LOO-SJ as selection: each sample y_i gets a score based on its average structural similarity to all other samples. The paper does compute this in Appendix D but only for analyzing circularity, not for the actual selection experiments. R2 has a point that this is a missed opportunity.

Though I think there's a partial rebuttal here: the consensus-proximity ranking used for instance-level signals in Table 5 is essentially LOO-SJ selection under the hood. When selecting the sample closest to consensus via SJ, you're picking the one with the highest average pairwise SJ across all samples—which is exactly what LOO-SJ does. So it's being tested implicitly, just not made explicit. Looking at the results, SJ achieves 0.645 NER F1, Voting gets 0.634, and Logprob reaches 0.650, so the performance is competitive but the connection between the method and the signal isn't clearly articulated.

Now looking at the greedy baseline at 0.644, consensus-proximity (which is effectively LOO-SJ for SJ) barely outperforms it at 0.645. So the signal IS being tested in the selection experiments, contrary to R2's claim that it wasn't analyzed. The paper should make this LOO-SJ connection explicit and could explore more per-sample signals, but the criticism that consensus-proximity wasn't tested isn't entirely fair.

On the Nedellec comparison, R2 raises three concerns: the selection results are negative, multi-domain evaluation is standard practice, and SJ's advantage is inconsistent across tasks. I see merit in some of these points—the negative selection result is still a valid contribution if properly characterized, and R2 is right that multi-domain work is now standard. The SJ inconsistency is partially valid (EM outperforms SJ on CoNLL and with conditional filtering), though the paper frames this as a task-difficulty finding rather than claiming SJ universally wins. The incremental value over Nedellec is less clear than the paper suggests, but a well-characterized negative result still counts as a contribution.

I also notice R2 caught an authorship issue: the bibliography lists Yao as the first author of the Nedellec paper, not Nédellec, so citing it as "Nédellec et al." is technically incorrect. On the "first systematic evaluation" claim, the paper scopes it to confidence signals for generative IE, which seems appropriately bounded.

For the missing citations, the conformal prediction works (Singer et al., the ICLR 2025 paper) are relevant but perhaps not essential since the paper focuses on self-consistency signals rather than conformal methods. The self-consistency papers like "Optimal Self-Consistency" and "Difficulty-Adaptive SC" seem more directly related to the core contribution.

On the experimental scope, using two 8B model families across three datasets and two tasks is modest but not negligible—the limitation to 8B models is acknowledged, and the LoRA fine-tuning setup does diverge from typical generative IE approaches. The ρ-AUROC dissociation is addressed in the paper's discussion of quality estimation versus output selection.

I'm noticing the EM=1 compression effect where identical outputs receive perfect scores regardless of correctness is explained in the appendix, which weakens the critique since it's documented but buried. There's also a citation accuracy issue to flag—the Yao et al. reference is mislabeled as Nédellec in the bibliography.

Now I'm structuring my response by evaluating each weakness with either agreement or rebuttal based on textual evidence. For the first point about definitional circularity, I partially agree that the instance-level signals have a definitional component, but the consensus-proximity selection method in Section 3.3 does convert these into per-sample selectors, so it's not purely circular reasoning.

For the second point about LOO-SJ, the paper actually does test it as a per-sample selector through the consensus-proximity approach, and Table 5 shows it achieves 0.645, so this is more of a presentation gap than a missing experiment. The third weakness about negative selection results is valid—it's a genuine contribution, though the overall incremental argument is indeed overstated.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "189e5f3c-7f0e-429b-b8f2-f27f0fdcbfcb",
  "isSidechain": false,
  "requestId": "req_011Cb3XWK6EVYSu6Y8a3ehqa",
  "type": "assistant",
  "uuid": "ef658b58-c806-4563-9b71-093e29544374",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_1_68ddc296",
  "sessionId": "cd3ac2da-cdcc-4c5b-9409-914107331cb2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PVf2U5kNaajw1ZLzremMEy",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7548,
      "cache_read_input_tokens": 43986,
      "output_tokens": 7330,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 7548,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 7330,
          "cache_read_input_tokens": 43986,
          "cache_creation_input_tokens": 7548,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 7548
          },
          "type": "message"
        }
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

_source line 54 · 2026-05-15T02:01:03.397Z_

论文全文已读完。现在逐条回应 Reviewer 2 的意见。

---

## Reviewer 1 对 Reviewer 2 审稿意见的交叉回应

### Must-Fix 问题

**[AGREE with nuance] R2-N1: Correlation-selection gap 的解释力**

同意 R2 的核心判断：4/5 instance-level signals 无法做 per-sample selection 在定义上是预期的（Section 3.1 明确区分了 per-sample vs. instance-level，Eq. 5–8 只产出单一 score），这削弱了"发现"的新颖性。

但需补充两点：
1. 论文在 Section 3.3 中通过"select the sample closest to the consensus output"将 instance-level signals 转化为 per-sample 排序——这不是纯粹定义性的，是一个合理的 selection 策略，只不过效果不好（Table 5: SJ=0.645 vs. Greedy=0.644）。
2. R2 关于 logprob 失败原因分析不足的批评完全成立。论文仅在 Section 5.1 提到 conditional filtering 后"logprob RE collapses to ρ=0.011"（Figure 2 右），说明其 full-set correlation 来自 zero/non-zero 分离；Discussion 段简要提到 constrained decoding 可能的影响，但未做任何实验验证（calibration 干扰？length bias？constrained decoding 对 token logprob 的扭曲？）。作为唯一的 per-sample signal，logprob 值得至少一段深入分析。

**[REBUT] R2-N2: Per-sample signal 探索严重不足**

R2 认为 LOO-SJ 的 selection 能力"未被测试"，但这与论文实际实验不符。Section 3.3 明确说 instance-level signals 通过 consensus-proximity 选择候选样本。对于 SJ，consensus-proximity 就是：对每个 $y_i$ 计算其对所有其他样本的平均 SJ——这在数学上等价于 LOO-SJ 排序。Table 5 中 SJ 行（NER F1=0.645, RE F1=0.386）就是 LOO-SJ 的 selection 结果，只是论文没有显式使用"LOO-SJ selection"这个术语。

真正的问题是论文没有把这个等价关系说清楚，也没有把 Appendix D 的 LOO-SJ 分析（Δρ=−0.014）与 Table 5 的 selection 结果连起来讨论。这是一个表述不清的问题，不是实验缺失。

不过，R2 关于只有 1 个 per-sample signal 的批评仍然有效——论文声称"systematic comparison"但 per-sample 维度极度单薄。可以补充的 per-sample signals 包括：per-sample entropy、per-entity logprob（而非 sequence-level mean）、或 per-sample 与 consensus 的 SJ 距离（显式地写为 per-sample signal）。

**[AGREE] R2-N3: 对 Nedellec et al. (2026) 的增量贡献论证不足**

同意。进一步补充：
- **引用本身有错误**——bib 文件中 `nedellec2026consistency` 的 author 字段为 `{Yao, Xinzhi and Nédellec, Claire and Xia, Jingbo and Bossy, Robert}`，第一作者是 Yao 而非 Nédellec，但论文全文使用"Nédellec et al."，这是一个事实性错误，R2 的发现正确。
- SJ 优势的不一致性确实削弱了区分论证：CoNLL 上 EM > SJ（Table 3: EM ρ=0.451 vs. SJ ρ=0.436），conditional filtering 后 EM 在所有 4 个配置中领先（Appendix D）。论文将此解释为"task-difficulty dependent"（Discussion 段），但这恰恰说明 SJ 的核心优势仅在特定条件下成立。
- 不过，我认为 negative selection result 本身仍是有价值的贡献——R2 似乎低估了负面发现的学术价值。Nedellec et al. 未涉及 selection，论文首次在 IE 场景下系统验证了 best-of-N selection 的失败，这个结论对社区有指导意义。问题在于论文对此贡献的**论证方式**不够有力，而非贡献本身不存在。

### Should-Fix 问题

**[AGREE] R2-W1: "first systematic evaluation" claim**

同意需收窄。Abstract 第 1 行和 Contribution 1（Section 1）都用了"first systematic"。鉴于 Nedellec et al. (2026) 已经做了 consistency–accuracy correlation 分析（虽然 scope 更窄），"first" claim 应加限定语，如"first to compare signals from multiple families for both quality estimation and sample selection in generative IE"。

**[REBUT] R2-W2: 遗漏 conformal prediction 文献**

论文已在 Section 2 引用了 conformal prediction 的两篇代表性工作（Fisch et al. 2021, Angelopoulos et al. 2021），并在 Conclusion 明确提出"Integration with conformal prediction could convert continuous confidence scores into calibrated coverage guarantees"作为 future work。本文的核心问题是 unsupervised consistency signals 的质量估计 vs. selection 能力，不是 conformal coverage guarantee。Singer et al. (2026) 和 ICLR 2025 conformal structured prediction 属于相关但不同的研究路线（supervised conformal vs. unsupervised consistency），添加为 related work 引用是合理的，但称其为"critical omission"过重。

**[AGREE] R2-W3: 遗漏 self-consistency 改进文献**

同意。"Optimal Self-Consistency" 和 "Difficulty-Adaptive SC" 直接涉及 self-consistency 的选择策略优化，与论文的 correlation-selection gap 主题高度相关。尤其是 Difficulty-Adaptive SC——论文的核心发现之一就是 signal rankings depend on task difficulty（Section 5.1, Discussion），如果已有工作在这个方向上做了自适应选择，论文应该讨论。

**[AGREE with nuance] R2-W4: 实验规模偏小**

部分同意。论文覆盖 2 个模型族 × 3 个数据集 × 2 个任务，做了 temperature/N/cross-model robustness 分析（Appendix A），统计检验到位——这在 EMNLP 标准下不算小。但：
- 仅 8B 模型确实是限制，Limitations 已承认（lines 5-6）
- 仅 1 个 RE benchmark（SciERC, 44% zero-F1）导致 RE 结论受 floor effect 影响严重
- LoRA fine-tuned 设置不是主流 generative IE setting（多数工作用 hard prompting 或 instruction tuning），论文没有讨论 LoRA 可能引入的 distribution shift 对 consistency signals 的影响

R2 指出"非典型 generative IE 设置"这一点我补充同意——LoRA fine-tuning 可能导致模型输出分布比 hard-prompted 模型更集中，人为压低了 sample diversity，从而使 selection signals 更难区分候选样本。这是一个潜在的混淆变量。

**[AGREE] R2-W5: ρ-AUROC dissociation 机制分析浅**

同意。EM=1 的压缩效应（all-correct 和 all-wrong 都映射到 EM=1）在 Appendix D 有讨论（"instances where all N samples produce identical (possibly incorrect) outputs receive EM=1 regardless of quality, compressing the signal's dynamic range"），但仅在 appendix。这个机制是理解 ρ-AUROC 分离的关键，应在主文 Section 5.1 或 Discussion 中明确阐述。

### 引用真实性

**[AGREE] nedellec2026consistency 引用错误**

确认。Bib 文件显示 author = {Yao, Xinzhi and Nédellec, Claire and Xia, Jingbo and Bossy, Robert}。第一作者是 Yao，论文应引用为"Yao et al. (2026)"而非"Nédellec et al."。引用 key 命名为 `nedellec2026consistency` 也具有误导性。

### 遗漏引用

**[AGREE]** #3 Optimal Self-Consistency 和 #4 Difficulty-Adaptive SC 确实应该引用讨论（理由见 W3）。

**[REBUT]** #1 Singer et al. 和 #2 ICLR 2025 conformal 为不同研究路线，非 critical omission（理由见 W2）。

**[NEUTRAL]** #5 Generative Self-Aggregation (arXiv:2503.04104) 需要确认其内容再判断——如果涉及 structured output aggregation 则应引用。

### 审稿判断

**[AGREE with qualification]**

同意"当前版本更适合 Findings track"的判断方向。核心问题是：(1) correlation-selection gap 的理论贡献被其部分定义性质削弱（N1），(2) per-sample signal 维度过于单薄（N2），(3) logprob 失败的机制分析缺失。

但我对 R2 提出的修改路径（"深入分析 per-sample signal failure 原因、测试 LOO-SJ 等 per-sample structural signals、讨论 constrained decoding 影响"）补充建议：LOO-SJ 实际已隐式测试（Table 5 的 SJ 行），更有价值的方向是引入真正新的 per-sample signals（如 per-entity logprob、learned verifier probe）或分析 constrained decoding 对 logprob 信号的系统性扭曲。

---

汇报给 Director。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ef658b58-c806-4563-9b71-093e29544374",
  "isSidechain": false,
  "requestId": "req_011Cb3XWK6EVYSu6Y8a3ehqa",
  "type": "assistant",
  "uuid": "3d2689a5-9d90-48c1-b62e-1d7c2448d43c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_1_68ddc296",
  "sessionId": "cd3ac2da-cdcc-4c5b-9409-914107331cb2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PVf2U5kNaajw1ZLzremMEy",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7548,
      "cache_read_input_tokens": 43986,
      "output_tokens": 7330,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 7548,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 7330,
          "cache_read_input_tokens": 43986,
          "cache_creation_input_tokens": 7548,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 7548
          },
          "type": "message"
        }
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

_source line 55 · 2026-05-15T02:01:22.273Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director · `toolu_012fTTNyZNyyk8kcjEZXNXgS`</summary>

```json
{
  "text": "## Reviewer 1 对 Reviewer 2 审稿意见的交叉回应\n\n### Must-Fix 问题\n\n**[AGREE with nuance] R2-N1: Correlation-selection gap 的解释力**\n\n同意 R2 的核心判断：4/5 instance-level signals 无法做 per-sample selection 在定义上是预期的（Section 3.1 明确区分了 per-sample vs. instance-level，Eq. 5–8 只产出单一 score），这削弱了\"发现\"的新颖性。\n\n但需补充两点：\n1. 论文在 Section 3.3 中通过\"select the sample closest to the consensus output\"将 instance-level signals 转化为 per-sample 排序——这不是纯粹定义性的，是一个合理的 selection 策略，只不过效果不好（Table 5: SJ=0.645 vs. Greedy=0.644）。\n2. R2 关于 logprob 失败原因分析不足的批评完全成立。论文仅在 Section 5.1 提到 conditional filtering 后\"logprob RE collapses to ρ=0.011\"（Figure 2 右），说明其 full-set correlation 来自 zero/non-zero 分离；Discussion 段简要提到 constrained decoding 可能的影响，但未做任何实验验证。作为唯一的 per-sample signal，logprob 值得至少一段深入分析。\n\n**[REBUT] R2-N2: Per-sample signal 探索严重不足**\n\nR2 认为 LOO-SJ 的 selection 能力\"未被测试\"，但这与论文实际实验不符。Section 3.3 明确说 instance-level signals 通过 consensus-proximity 选择候选样本。对于 SJ，consensus-proximity 就是：对每个 y_i 计算其对所有其他样本的平均 SJ——这在数学上等价于 LOO-SJ 排序。Table 5 中 SJ 行（NER F1=0.645, RE F1=0.386）就是 LOO-SJ 的 selection 结果，只是论文没有显式使用\"LOO-SJ selection\"这个术语。\n\n真正的问题是论文没有把这个等价关系说清楚，是表述问题而非实验缺失。\n\n不过，R2 关于只有 1 个 per-sample signal 的批评仍然有效——\"systematic comparison\" 但 per-sample 维度极度单薄。\n\n**[AGREE] R2-N3: 对 Nedellec et al. (2026) 的增量贡献论证不足**\n\n同意。补充发现：bib 文件中 nedellec2026consistency 的 author 字段确认第一作者是 Yao，论文全文使用\"Nédellec et al.\"是事实性错误。SJ 优势不一致性确实削弱区分论证（CoNLL: EM ρ=0.451 > SJ ρ=0.436; conditional filtering 后 EM 在所有 4 个配置领先）。\n\n但 negative selection result 本身仍有学术价值——Nedellec et al. 未涉及 selection，论文首次系统验证了 best-of-N selection 在 IE 中的失败。问题在于论证方式不够有力，而非贡献不存在。\n\n### Should-Fix 问题\n\n**[AGREE] R2-W1**: \"first systematic\" claim 需收窄，加限定语如\"first to compare signals from multiple families for both quality estimation and sample selection in generative IE\"。\n\n**[REBUT] R2-W2**: 论文已引用 conformal prediction 代表性工作（Fisch 2021, Angelopoulos 2021）并在 Conclusion 讨论 future integration。Singer et al. 和 ICLR 2025 conformal 属不同研究路线（supervised conformal vs. unsupervised consistency），添加为 related work 合理，但非 critical omission。\n\n**[AGREE] R2-W3**: Optimal Self-Consistency 和 Difficulty-Adaptive SC 与论文核心主题高度相关，应引用讨论。尤其后者——论文的核心发现之一就是 signal rankings depend on task difficulty。\n\n**[AGREE with nuance] R2-W4**: 实验覆盖度在 EMNLP 标准下不算小（2 模型族 × 3 数据集 × robustness 分析）。但仅 8B 模型、1 个 RE benchmark、LoRA fine-tuned 设置确是限制。补充同意 R2 的\"非典型设置\"观点——LoRA fine-tuning 可能使模型输出分布比 hard-prompted 更集中，人为压低 sample diversity，使 selection signals 更难区分候选样本，这是潜在混淆变量。\n\n**[AGREE] R2-W5**: EM=1 压缩效应在 Appendix D 有讨论但仅在 appendix，应在主文明确阐述。\n\n### 引用真实性\n\n**[AGREE]** nedellec2026consistency 第一作者应为 Yao，论文\"Nédellec et al.\"引用有误，已从 bib 文件确认。\n\n### 遗漏引用\n\n- [AGREE] #3 Optimal SC, #4 Difficulty-Adaptive SC 应引用\n- [REBUT] #1 Singer et al., #2 ICLR 2025 conformal 非 critical omission\n- [NEUTRAL] #5 Generative Self-Aggregation 需确认内容再判断\n\n### 审稿判断\n\n[AGREE with qualification] 同意 Findings track 判断方向。核心问题：(1) gap 的理论贡献被部分定义性质削弱，(2) per-sample signal 维度单薄，(3) logprob 失败机制分析缺失。\n\n对 R2 修改路径的补充建议：LOO-SJ 实际已隐式测试（Table 5 SJ 行），更有价值的方向是引入真正新的 per-sample signals（per-entity logprob、learned verifier probe）或分析 constrained decoding 对 logprob 信号的系统性扭曲。",
  "reviewer_id": "1",
  "project": "struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3d2689a5-9d90-48c1-b62e-1d7c2448d43c",
  "isSidechain": false,
  "requestId": "req_011Cb3XWK6EVYSu6Y8a3ehqa",
  "type": "assistant",
  "uuid": "a9ea3126-01f7-4401-8d0d-981c8c9926d4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_1_68ddc296",
  "sessionId": "cd3ac2da-cdcc-4c5b-9409-914107331cb2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PVf2U5kNaajw1ZLzremMEy",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7548,
      "cache_read_input_tokens": 43986,
      "output_tokens": 7330,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 7548,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 7330,
          "cache_read_input_tokens": 43986,
          "cache_creation_input_tokens": 7548,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 7548
          },
          "type": "message"
        }
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

_source line 56_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[Round 1 审稿请求]: ## 交叉分享：Reviewer 2 的完整 Round 1 审稿意见  请逐条回应 Reviewer 2 的每个问题：用 [AGREE] 表示同意并说明理由，或 [REBUT] 表示反驳并引用论文具体 Section/Table/Figure 作为证据。  ---  以下是 Reviewer 2 的完整审稿原文：  ### 总体评分 **Overall**: 3.…",
  "leafUuid": "a9ea3126-01f7-4401-8d0d-981c8c9926d4",
  "sessionId": "cd3ac2da-cdcc-4c5b-9409-914107331cb2"
}
```

---

### Runtime record

_source line 57_

```json
{
  "type": "ai-title",
  "aiTitle": "Respond to EMNLP Reviewer 2 Round 1 comments",
  "sessionId": "cd3ac2da-cdcc-4c5b-9409-914107331cb2"
}
```

---

### Tool result

_source line 58 · 2026-05-15T02:01:26.896Z_

<details><summary>↩ Tool result · `toolu_012fTTNyZNyyk8kcjEZXNXgS`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_3897c2857f11615119e277e820eae311:director\"}, \"error\": \"\"}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a9ea3126-01f7-4401-8d0d-981c8c9926d4",
  "isSidechain": false,
  "promptId": "e032b776-5e54-467c-9321-aeb2f2c75513",
  "type": "user",
  "uuid": "1a7fe85f-2b08-42c2-8185-609443f015be",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"review_director_key\\\": \\\"feishu:group:oc_3897c2857f11615119e277e820eae311:director\\\"}, \\\"error\\\": \\\"\\\"}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_3897c2857f11615119e277e820eae311:director\"}, \"error\": \"\"}"
    }
  },
  "sourceToolAssistantUUID": "a9ea3126-01f7-4401-8d0d-981c8c9926d4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_1_68ddc296",
  "sessionId": "cd3ac2da-cdcc-4c5b-9409-914107331cb2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---
