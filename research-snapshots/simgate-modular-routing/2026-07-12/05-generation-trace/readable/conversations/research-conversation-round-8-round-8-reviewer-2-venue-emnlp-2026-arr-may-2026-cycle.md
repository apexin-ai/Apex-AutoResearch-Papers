# Research conversation: [Round 8 审稿请求]: ## Round 8 审稿任务 — Reviewer 2（新颖性 + 完整性 + 写作质量） ### Venue 信息 - **会议**: EMNLP 2026 (通过 ARR May 2026 cycle 

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 63
- **Recorded user turns:** 3
- **Tool calls:** 15
- **Original source:** `logs/chats/exported-trajectories/account-2/5bc9ff02-4cf0-48f5-9df4-52d4a45b7804.jsonl`
- **Structured JSON:** [`e3f8e45fa5ecec47fd9b.json`](../../sessions/e3/e3f8e45fa5ecec47fd9b.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-16T12:22:32.505Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-16T12:22:32.505Z",
  "sessionId": "5bc9ff02-4cf0-48f5-9df4-52d4a45b7804",
  "content": "[Round 8 审稿请求]:\n## Round 8 审稿任务 — Reviewer 2（新颖性 + 完整性 + 写作质量）\n\n### Venue 信息\n- **会议**: EMNLP 2026 (通过 ARR May 2026 cycle 提交)\n- **截止日期**: 2026-05-25\n- **页数限制**: 正文 8 页 + 无限参考文献页\n- **模板**: ACL LaTeX (`\\usepackage[review]{acl}`)\n- **匿名**: Double-blind\n- **Limitations**: 必须有，不计入页数\n\n### 论文路径\n`projects/simgate-modular-routing/docs/paper/main.tex`（含 `\\input{abstract}`, `\\input{introduction}`, `\\input{method}`, `\\input{experiments}`, `\\input{related_work}`, `\\input{discussion}`, `\\input{conclusion}`）\n\n### 你的审查侧重\n1. **贡献新颖性**：episode-level counterfactual analysis 作为方法贡献是否足够 novel？DAF 指标本身是否有独立价值（vs 简单的 death rate comparison）？\"router 训练失败\"作为 negative result 是否有足够贡献？\n2. **Related Work 覆盖**：是否覆盖了 (a) RouteLLM, (b) tool-learning survey (Qu 2024), (c) Reflexion, (d) safe RL 近年工作（不仅是 Garcia 2015 survey）, (e) 2025-2026 concurrent routing 工作？\n3. **Cross-environment 叙事一致性**：MATH ($p=0.079$) 在 Abstract/Intro/Discussion/Conclusion 中的表述是否一致？是否有过度解读 non-significant result 的情况？ALFWorld 分析的方法论描述是否充分？\n4. **论文组织与写作**：Abstract 是否过长？信息密度是否恰当？Contributions 列表是否准确反映了实际完成的工作（特别是 cross-model generalization claim）？\n5. **格式与 Bib**：ACL template 合规性；bib entries 的 year/author 准确性；figure/table 引用完整性；匿名规则遵守\n\n### 上轮遗留 Issue（需验证是否已修复）\n\n**Critical (必须验证)**:\n- **R6-C1**: DAF=90.4% 是否仍作为 headline number？78.9% 是否被提升为同等重要的 penalty-independent metric？\n- **R7-N1**: ALFWorld (Table 3, N=135) — 是否添加了完整方法论描述（model, deterministic modality definition, labeling process, episode length）？\n\n**Warning (需验证)**:\n- **R6-W8**: Safe RL literature — 是否添加了 1-2 个 specific safety critic 引用（CPO, CRPO, safety Q-functions 等）来支持 §5 \"router = safety critic\" claim？\n- **R7-W1**: MATH p=0.079 — \"routing signal vanishes\" 是否改为了更审慎的措辞？\n- **R7-W2**: Llama pilot N=10 — 是否从 Contribution 列表中移除？是否降级为 directional observation？\n- **R7-W5**: Missing references — RouteLLM (Ong 2024), Reflexion (Shinn 2023), tool-learning survey (Qu 2024) 是否已添加？\n\n**Info (快速检查)**:\n- **R7-m1**: retool-2026 key/year 和 dynathink-2025 author 是否修正？\n- **R7-m2**: Abstract DAF 精度是否改为 ~90%？GPU 描述是否已泛化？\n- **R7-m3**: find-non-living-thing 40 episodes 是否有解释？code/data release plan 是否明确？\n\n### 输出格式\n请按以下结构输出审稿意见：\n1. Summary (2-3句)\n2. Strengths (逐条)\n3. Weaknesses (逐条，标明 severity: Must-Fix / Should-Fix / Minor)\n4. 上轮 Issue 验证结果（逐条：[RESOLVED] / [PARTIALLY FIXED] / [NOT FIXED] / [NEW ISSUE]）\n5. Missing References (如有)\n6. Questions for Authors\n7. Overall Assessment (strong reject / weak reject / borderline / weak accept / strong accept) + Confidence (1-5)"
}
```

---

### Runtime record

_source line 2 · 2026-05-16T12:22:32.509Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-16T12:22:32.509Z",
  "sessionId": "5bc9ff02-4cf0-48f5-9df4-52d4a45b7804"
}
```

---

## Round 1

54 recorded events

### User

_source line 3 · 2026-05-16T12:22:32.547Z_

[Round 8 审稿请求]:
## Round 8 审稿任务 — Reviewer 2（新颖性 + 完整性 + 写作质量）

### Venue 信息
- **会议**: EMNLP 2026 (通过 ARR May 2026 cycle 提交)
- **截止日期**: 2026-05-25
- **页数限制**: 正文 8 页 + 无限参考文献页
- **模板**: ACL LaTeX (`\usepackage[review]{acl}`)
- **匿名**: Double-blind
- **Limitations**: 必须有，不计入页数

### 论文路径
`projects/simgate-modular-routing/docs/paper/main.tex`（含 `\input{abstract}`, `\input{introduction}`, `\input{method}`, `\input{experiments}`, `\input{related_work}`, `\input{discussion}`, `\input{conclusion}`）

### 你的审查侧重
1. **贡献新颖性**：episode-level counterfactual analysis 作为方法贡献是否足够 novel？DAF 指标本身是否有独立价值（vs 简单的 death rate comparison）？"router 训练失败"作为 negative result 是否有足够贡献？
2. **Related Work 覆盖**：是否覆盖了 (a) RouteLLM, (b) tool-learning survey (Qu 2024), (c) Reflexion, (d) safe RL 近年工作（不仅是 Garcia 2015 survey）, (e) 2025-2026 concurrent routing 工作？
3. **Cross-environment 叙事一致性**：MATH ($p=0.079$) 在 Abstract/Intro/Discussion/Conclusion 中的表述是否一致？是否有过度解读 non-significant result 的情况？ALFWorld 分析的方法论描述是否充分？
4. **论文组织与写作**：Abstract 是否过长？信息密度是否恰当？Contributions 列表是否准确反映了实际完成的工作（特别是 cross-model generalization claim）？
5. **格式与 Bib**：ACL template 合规性；bib entries 的 year/author 准确性；figure/table 引用完整性；匿名规则遵守

### 上轮遗留 Issue（需验证是否已修复）

**Critical (必须验证)**:
- **R6-C1**: DAF=90.4% 是否仍作为 headline number？78.9% 是否被提升为同等重要的 penalty-independent metric？
- **R7-N1**: ALFWorld (Table 3, N=135) — 是否添加了完整方法论描述（model, deterministic modality definition, labeling process, episode length）？

**Warning (需验证)**:
- **R6-W8**: Safe RL literature — 是否添加了 1-2 个 specific safety critic 引用（CPO, CRPO, safety Q-functions 等）来支持 §5 "router = safety critic" claim？
- **R7-W1**: MATH p=0.079 — "routing signal vanishes" 是否改为了更审慎的措辞？
- **R7-W2**: Llama pilot N=10 — 是否从 Contribution 列表中移除？是否降级为 directional observation？
- **R7-W5**: Missing references — RouteLLM (Ong 2024), Reflexion (Shinn 2023), tool-learning survey (Qu 2024) 是否已添加？

**Info (快速检查)**:
- **R7-m1**: retool-2026 key/year 和 dynathink-2025 author 是否修正？
- **R7-m2**: Abstract DAF 精度是否改为 ~90%？GPU 描述是否已泛化？
- **R7-m3**: find-non-living-thing 40 episodes 是否有解释？code/data release plan 是否明确？

### 输出格式
请按以下结构输出审稿意见：
1. Summary (2-3句)
2. Strengths (逐条)
3. Weaknesses (逐条，标明 severity: Must-Fix / Should-Fix / Minor)
4. 上轮 Issue 验证结果（逐条：[RESOLVED] / [PARTIALLY FIXED] / [NOT FIXED] / [NEW ISSUE]）
5. Missing References (如有)
6. Questions for Authors
7. Overall Assessment (strong reject / weak reject / borderline / weak accept / strong accept) + Confidence (1-5)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "2cc35627-090b-4e8e-873a-80e6ce7d766f",
  "type": "user",
  "uuid": "2e539ece-c271-4171-8311-9df6c313377e",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/.claude/sessions/review_reviewer_2_ab9762a8",
  "sessionId": "5bc9ff02-4cf0-48f5-9df4-52d4a45b7804",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-16T12:22:32.546Z_

```json
{
  "parentUuid": "2e539ece-c271-4171-8311-9df6c313377e",
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
  "uuid": "a7033b91-2699-4b45-a4cd-23271bfb4bfe",
  "timestamp": "2026-05-16T12:22:32.546Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/.claude/sessions/review_reviewer_2_ab9762a8",
  "sessionId": "5bc9ff02-4cf0-48f5-9df4-52d4a45b7804",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-16T12:22:32.546Z_

```json
{
  "parentUuid": "a7033b91-2699-4b45-a4cd-23271bfb4bfe",
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
  "uuid": "88b7640a-8944-4ffc-9b6b-074269dfcf29",
  "timestamp": "2026-05-16T12:22:32.546Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/.claude/sessions/review_reviewer_2_ab9762a8",
  "sessionId": "5bc9ff02-4cf0-48f5-9df4-52d4a45b7804",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 6 · 2026-05-16T12:22:32.546Z_

```json
{
  "parentUuid": "88b7640a-8944-4ffc-9b6b-074269dfcf29",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "66652cfb-dace-4c66-ab1b-7700f6c2e6c8",
  "timestamp": "2026-05-16T12:22:32.546Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/.claude/sessions/review_reviewer_2_ab9762a8",
  "sessionId": "5bc9ff02-4cf0-48f5-9df4-52d4a45b7804",
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
  "aiTitle": "Review paper on modular routing with counterfactual analysis",
  "sessionId": "5bc9ff02-4cf0-48f5-9df4-52d4a45b7804"
}
```

---

### Assistant

_source line 8 · 2026-05-16T12:22:40.860Z_

<details><summary>Logged reasoning block</summary>

```text
The user is asking me to perform a review of a paper as Reviewer 2. Let me start by reading the paper materials and then conducting the review according to the instructions.

First, I need to:
1. Read the paper (main.tex and its input files)
2. Search for EMNLP 2026 / ACL ARR reviewer guidelines
3. Conduct the review according to the specified focus areas
4. Verify the issues from the previous round

Let me start by reading the paper and searching for reviewer guidelines in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "66652cfb-dace-4c66-ab1b-7700f6c2e6c8",
  "isSidechain": false,
  "requestId": "req_011Cb6EsvzbM7QrNauJdDcTT",
  "type": "assistant",
  "uuid": "5ac9cd15-bc41-41a4-8e22-d883128305cd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/.claude/sessions/review_reviewer_2_ab9762a8",
  "sessionId": "5bc9ff02-4cf0-48f5-9df4-52d4a45b7804",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01X2TaGzPq1tnfAqwpssREzZ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14266,
      "cache_read_input_tokens": 11841,
      "output_tokens": 287,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 14266,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 287,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 14266,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 14266
          },
          "type": "message"
        }
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

_source line 9 · 2026-05-16T12:22:42.330Z_

开始 Round 8 审稿。先并行读取论文各部分和搜索 reviewer guidelines。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5ac9cd15-bc41-41a4-8e22-d883128305cd",
  "isSidechain": false,
  "requestId": "req_011Cb6EsvzbM7QrNauJdDcTT",
  "type": "assistant",
  "uuid": "7532e367-fb0b-4b93-9aa0-5e97596b913d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/.claude/sessions/review_reviewer_2_ab9762a8",
  "sessionId": "5bc9ff02-4cf0-48f5-9df4-52d4a45b7804",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01X2TaGzPq1tnfAqwpssREzZ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14266,
      "cache_read_input_tokens": 11841,
      "output_tokens": 287,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 14266,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 287,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 14266,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 14266
          },
          "type": "message"
        }
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

_source line 10 · 2026-05-16T12:22:44.130Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01XGFEo8Z37H9ZuXXxb5mccP`</summary>

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
  "parentUuid": "7532e367-fb0b-4b93-9aa0-5e97596b913d",
  "isSidechain": false,
  "requestId": "req_011Cb6EsvzbM7QrNauJdDcTT",
  "type": "assistant",
  "uuid": "6ed9ad4a-b128-41b8-9815-533ad4d5876e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/.claude/sessions/review_reviewer_2_ab9762a8",
  "sessionId": "5bc9ff02-4cf0-48f5-9df4-52d4a45b7804",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01X2TaGzPq1tnfAqwpssREzZ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14266,
      "cache_read_input_tokens": 11841,
      "output_tokens": 287,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 14266,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 287,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 14266,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 14266
          },
          "type": "message"
        }
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

_source line 11 · 2026-05-16T12:22:44.147Z_

<details><summary>↩ Tool result · `toolu_01XGFEo8Z37H9ZuXXxb5mccP`</summary>

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
  "parentUuid": "6ed9ad4a-b128-41b8-9815-533ad4d5876e",
  "isSidechain": false,
  "promptId": "2cc35627-090b-4e8e-873a-80e6ce7d766f",
  "type": "user",
  "uuid": "dc4b83b9-2a0c-4745-aa46-ce66fa50dc90",
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
  "sourceToolAssistantUUID": "6ed9ad4a-b128-41b8-9815-533ad4d5876e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/.claude/sessions/review_reviewer_2_ab9762a8",
  "sessionId": "5bc9ff02-4cf0-48f5-9df4-52d4a45b7804",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 12 · 2026-05-16T12:22:47.072Z_

<details><summary>Logged reasoning block</summary>

```text
Now let me read the paper files and search for reviewer guidelines in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dc4b83b9-2a0c-4745-aa46-ce66fa50dc90",
  "isSidechain": false,
  "requestId": "req_011Cb6Etnf5AL2qXVpnfpuhT",
  "type": "assistant",
  "uuid": "99bc1321-08fd-40da-ae09-5fdab6ea2ad6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/.claude/sessions/review_reviewer_2_ab9762a8",
  "sessionId": "5bc9ff02-4cf0-48f5-9df4-52d4a45b7804",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JbYkbuqCasG2nxYFP3PH34",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1791,
      "cache_read_input_tokens": 26107,
      "output_tokens": 270,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1791,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 270,
          "cache_read_input_tokens": 26107,
          "cache_creation_input_tokens": 1791,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1791
          },
          "type": "message"
        }
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

_source line 13 · 2026-05-16T12:22:48.621Z_

<details open><summary>🔧 Tool call — Read · `toolu_01PTT12ANE6YVMM2BgLHXkam`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "99bc1321-08fd-40da-ae09-5fdab6ea2ad6",
  "isSidechain": false,
  "requestId": "req_011Cb6Etnf5AL2qXVpnfpuhT",
  "type": "assistant",
  "uuid": "586f0e27-a0c7-4373-b542-a2d00802d10a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/.claude/sessions/review_reviewer_2_ab9762a8",
  "sessionId": "5bc9ff02-4cf0-48f5-9df4-52d4a45b7804",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JbYkbuqCasG2nxYFP3PH34",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1791,
      "cache_read_input_tokens": 26107,
      "output_tokens": 270,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1791,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 270,
          "cache_read_input_tokens": 26107,
          "cache_creation_input_tokens": 1791,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1791
          },
          "type": "message"
        }
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

_source line 14 · 2026-05-16T12:22:48.633Z_

<details><summary>↩ Tool result · `toolu_01PTT12ANE6YVMM2BgLHXkam`</summary>

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
11	\graphicspath{{figures/}}
12	\usepackage{booktabs}
13	\usepackage{amsmath}
14	\usepackage{amssymb}
15	\usepackage{algorithm}
16	\usepackage{algorithmic}
17	
18	\title{Death Avoidance as the Dominant Routing Signal:\\A Counterfactual Analysis on ScienceWorld}
19	
20	\author{Anonymous}
21	
22	\begin{document}
23	\maketitle
24	
25	\input{abstract}
26	\input{introduction}
27	\input{method}
28	\input{experiments}
29	\input{related_work}
30	\input{discussion}
31	\input{conclusion}
32	
33	\section*{Limitations}
34	
35	Our primary analysis uses a single environment (ScienceWorld, 11 of 30 task types) with one backbone (Qwen2.5-7B-Instruct); generalization requires further validation. The $-100$ death penalty amplifies DAF; environments with softer penalties would exhibit lower DAF values (Appendix~\ref{app:penalty}). The 19 excluded task types (63\%) lack routing signal because both strategies typically time out within 30 steps; increasing the step budget could surface additional signal. Our internal-reasoning baseline uses single-pass ReAct~\citep{react-2023}; more sophisticated strategies (e.g., Reflexion~\citep{reflexion-2023}) may reduce internal death rates and lower DAF. Episode-level labels may assign suboptimal routing to individual steps, particularly those preceding death events, and training on pure-strategy trajectories introduces distribution shift at deployment~\citep{dagger-2011}. Cross-environment analyses on MATH and ALFWorld (\S\ref{sec:discussion}, Appendix~\ref{app:cross-env}) provide supporting evidence but do not conclusively establish generalization. A Llama-3.1-8B pilot ($N{=}10$; Appendix~\ref{app:cross-model}) shows directional consistency but is insufficient for statistical inference.
36	
37	\section*{Ethics Statement}
38	
39	This work uses ScienceWorld \cite{scienceworld-2022}, a publicly available text-based simulation environment, and does not involve human subjects or private data. All language models are accessed via standard APIs or publicly released weights. We report computational costs: approximately 40 GPU-hours on two consumer GPUs for data collection, router training, and evaluation. Code and data will be released upon acceptance.
40	
41	\bibliography{references}
42	
43	\appendix
44	
45	\section{Labeling Quality Audit}
46	\label{app:labeling}
47	
48	A potential concern is oracle circularity: whether episode-level labels reflect tie-breaking artifacts rather than genuine modality differences. We audit all 245 labels. Of the 150 \texttt{no\_preference} labels (61.2\%), 115 (46.9\%) are both-alive ties and 35 (14.3\%) are both-dead---all excluded from router training. The remaining 95 training labels are entirely genuine: 75 from death asymmetry (70 deterministic-preferred, 5 internal-preferred) and 20 from score comparison with both strategies surviving (16 deterministic-preferred, 4 internal-preferred). Zero labels depend on tie-breaking. Retraining the router using only death-asymmetry labels yields step-level balanced accuracy of 57.3\%, within 1$\sigma$ of the full-label retrain (57.6 $\pm$ 0.5\%, step-level Trainer evaluation), confirming that score-comparison labels contribute negligible additional signal. (Step-level metrics are used here for the relative comparison; as shown in \S\ref{sec:router-diagnostic}, absolute generalization to new episodes is near chance.) The 97.4\% step-level tie rate (\S\ref{sec:collection}) further motivates episode-level over step-level labeling.
49	
50	\section{Per-Task Decomposition}
51	\label{app:per-task}
52	We select 11 of ScienceWorld's 30 task types via prescreening: task types where both strategies complete at least one episode within the 30-step budget are retained; types where both strategies time out on all seed variations are excluded.\footnote{Prescreening ensures that the counterfactual comparison is meaningful---task types where neither strategy makes progress provide no routing signal.}
53	
54	\begin{table}[h]
55	\centering
56	\scriptsize
57	\setlength{\tabcolsep}{2.5pt}
58	\begin{tabular}{@{}lrrccc@{}}
59	\toprule
60	Task & $n$ & $\Delta_\text{full}$ & D\%\textsubscript{int} & D\%\textsubscript{det} & D / I / N \\
61	\midrule
62	id-life-stages-1       & 20  & $+47.50$ & 55   & 10   & 9 / 0 / 11  \\
63	lifespan-long          & 25  & $+44.00$ & 56   & 16   & 11 / 1 / 13 \\
64	lifespan-l-then-s      & 20  & $+40.80$ & 45   & 10   & 8 / 1 / 11  \\
65	inclined-plane         & 20  & $+36.00$ & 55   & 20   & 7 / 0 / 13  \\
66	freeze                 & 20  & $+30.50$ & 55   & 25   & 6 / 0 / 14  \\
67	meas-melt-point        & 20  & $+30.05$ & 55   & 25   & 6 / 0 / 14  \\
68	id-life-stages-2       & 20  & $+30.00$ & 50   & 20   & 6 / 0 / 14  \\
69	find-animal            & 20  & $+26.65$ & 50   & 25   & 5 / 0 / 15  \\
70	grow-fruit             & 20  & $+25.10$ & 45   & 20   & 6 / 1 / 13  \\
71	chem-mix               & 20  & $+21.80$ & 45   & 25   & 6 / 2 / 12  \\
72	\midrule
73	find-non-living$^\dagger$ & 40 & $+9.58$ & 0  & 0    & 16 / 4 / 20 \\
74	\midrule
75	\textbf{All (11 tasks)} & \textbf{245} & $\mathbf{+29.60}$ & \textbf{42.9} & \textbf{16.3} & \textbf{86 / 9 / 150} \\
76	\bottomrule
77	\end{tabular}
78	\caption{Per-task decomposition of the death avoidance effect. D\%: death rate for internal (int) and deterministic (det) strategies. D/I/N: episode labels (det-preferred / internal-preferred / no-preference). Sorted by $\Delta_{\text{full}}$ descending. $\dagger$\,Only task with zero deaths under both strategies; $n{=}40$ because data was collected in two batches, with the second batch adding 20 episodes to increase statistical power for this zero-death outlier.}
79	\label{tab:per-task}
80	\end{table}
81	
82	\paragraph{Task selection and anti-cherry-picking.}
83	The 11 included task types are those exhibiting meaningful routing signal in prescreening, not those with the highest death rates. The deterministic-strategy death rate is comparable between included (17.8\%) and excluded (14.9\%) task types, confirming that prescreening does not select for death-prone tasks. Rather, the key distinction is the \emph{presence} of routing signal: all 11 included tasks have $\Delta_{\text{nd}} \neq 0$ (non-zero performance gap on surviving episodes), while 53\% of excluded tasks show $\Delta_{\text{nd}} = 0$---neither strategy outperforms the other even when both survive, typically because both time out before making progress. \texttt{find-non-living-thing} serves as an internal counterexample: it has zero deaths under both strategies yet is included because it exhibits non-death routing signal ($\Delta_{\text{full}} = +9.58$ entirely from score differences), and deterministic is not always preferred (4 of 20 non-tie labels favor internal).
84	
85	\section{Correlation Robustness}
86	\label{app:correlation}
87	
88	The Pearson $r = 0.9698$ reported in \S\ref{sec:death-decomp} is robust across multiple diagnostics. Spearman rank correlation is $\rho = 0.986$ ($p = 2.4 \times 10^{-8}$), confirming that the relationship is not driven by outliers or non-linearity. A nonparametric bootstrap (10{,}000 resamples) yields 95\% CI $[0.952, 0.995]$.
89	
90	\begin{table}[h]
91	\centering
92	\small
93	\begin{tabular}{@{}lr@{}}
94	\toprule
95	Task removed & $r_{\text{LOO}}$ \\
96	\midrule
97	id-life-stages-1       & 0.963 \\
98	lifespan-long          & 0.969 \\
99	lifespan-l-then-s      & 0.976 \\
100	inclined-plane         & 0.969 \\
101	freeze                 & 0.971 \\
102	meas-melt-point        & 0.972 \\
103	id-life-stages-2       & 0.972 \\
104	find-animal            & 0.970 \\
105	grow-fruit             & 0.973 \\
106	chem-mix               & 0.969 \\
107	find-non-living        & 0.980 \\
108	\bottomrule
109	\end{tabular}
110	\caption{Leave-one-out Pearson $r$ for the death rate differential vs.\ $\Delta_{\text{full}}$ correlation. Full $r = 0.970$; LOO range $[0.963, 0.980]$. No single task type is a leverage point.}
111	\label{tab:loo}
112	\end{table}
113	
114	\section{Router Training Details}
115	\label{app:router-details}
116	
117	We use Qwen3-1.7B for the router to avoid circular dependency with the Qwen2.5-7B data-generating model.
118	
119	With gradient accumulation of 1 (effective batch size 4), routing performance is highly sensitive to the evaluation split, suggesting overfitting to specific train/validation partition boundaries. With gradient accumulation of 8 (effective batch size 32), step-level performance stabilizes across splits (${\sim}54\%$ balanced accuracy). All reported results use gradient accumulation 8.
120	
121	Under step-level evaluation with a fixed data split, cross-seed balanced accuracy ranges from 52.7\% to 58.1\%, but internal recall varies from 51.5\% to 81.8\%, reflecting threshold sensitivity. However, episode-level evaluation reveals that this apparent discrimination does not generalize: balanced accuracy drops to $47.1 \pm 2.2\%$ across 8 cross-split seeds (Appendix~\ref{app:seed-robustness}). Deployed end-to-end, the trained router allocates 97.0\% of episodes to deterministic computation with 17.6\% death rate, and misrouting cost (death from internally-routed episodes) exceeds the benefit of correctly routing rare internal-preferred cases.
122	
123	\paragraph{Evaluation methods.} All results use \emph{generation-based evaluation}: the model generates a routing label as text (\texttt{enable\_thinking=False}), parsed for classification. We evaluate at two granularities: \emph{step-level} (steps from the same episode may appear in both train and validation sets) and \emph{episode-level} (entire episodes held out). Step-level accuracy ($54.1 \pm 5.4\%$) exceeds chance, indicating the router captures some signal, but episode-level accuracy ($47.1 \pm 2.2\%$, below chance) shows this does not generalize to unseen episodes. A data scaling ablation (Appendix~\ref{app:seed-robustness}) rules out data scarcity, pointing instead to a structural limitation: always-deterministic is trivially near-optimal given DAF $= 90.4\%$. Both metrics are reported in the main text; the model-size ablation (Appendix~\ref{app:ablations}) uses step-level evaluation.
124	
125	\begin{table}[h]
126	\centering
127	\small
128	\resizebox{\columnwidth}{!}{%
129	\begin{tabular}{@{}lcc@{}}
130	\toprule
131	Hyperparameter & Classification Head & Implicit Router \\
132	\midrule
133	Base model & Qwen3-1.7B & Qwen3-1.7B \\
134	Architecture & Linear + LoRA & SFT + LoRA \\
135	LoRA $r$ / $\alpha$ & 16 / 32 & 16 / 32 \\
136	Learning rate & 2e-5 & 2e-4 \\
137	Optimizer & AdamW & AdamW \\
138	Epochs & 3 & 3 \\
139	Batch size (per device) & 4 & 4 \\
140	Gradient accumulation & 8 & 8 \\
141	Warmup ratio & 0.1 & 0.1 \\
142	Weight decay & 0.01 & 0.01 \\
143	Max sequence length & 512 & 512 \\
144	Seeds & \{42\} & \{42, 123, 456, 789\} \\
145	\bottomrule
146	\end{tabular}}
147	\caption{Router training hyperparameters. Both architectures use the same base model with LoRA adaptation. The classification head degenerates across all configurations; the implicit router results are reported as 4-seed mean$\pm$std.}
148	\label{tab:hyperparams}
149	\end{table}
150	
151	\section{Seed Robustness}
152	\label{app:seed-robustness}
153	
154	We assess router generalization at two evaluation granularities: \emph{step-level}, where steps from the same episode may appear in both train and validation sets, and \emph{episode-level}, where entire episodes are held out. Both use cross-split evaluation (seeds $\{42, \ldots, 49\}$, 8 seeds total), where the data partition and training seed both vary. Table~\ref{tab:seed-robustness} reports per-seed results.
155	
156	\begin{table}[h]
157	\centering
158	\small
159	\begin{tabular}{@{}llcc@{}}
160	\toprule
161	Eval.\ Granularity & Seed & Bal.\ Acc.\ (\%) \\
162	\midrule
163	Step-level & 42 & 57.06 \\
164	(same-episode & 43 & 63.99 \\
165	leakage) & 44 & 55.43 \\
166	 & 45 & 56.14 \\
167	 & 46 & 55.45 \\
168	 & 47 & 50.08 \\
169	 & 48 & 48.03 \\
170	 & 49 & 59.30 \\
171	\cmidrule{2-3}
172	 & Mean$\pm$std & $54.1 \pm 5.4$ \\
173	\midrule
174	Episode-level & 42 & 48.1 \\
175	(held-out & 43 & 47.9 \\
176	episodes) & 44 & 49.6 \\
177	 & 45 & 49.4 \\
178	 & 46 & 48.5 \\
179	 & 47 & 43.1 \\
180	 & 48 & 45.4 \\
181	 & 49 & 44.8 \\
182	\cmidrule{2-3}
183	 & Mean$\pm$std & $47.1 \pm 2.2$ \\
184	\midrule
185	\multicolumn{2}{@{}l}{Always-det (= majority-vote)} & 50.0 \\
186	\bottomrule
187	\end{tabular}
188	\caption{Per-seed router performance under cross-split evaluation (8 seeds, generation-based, \texttt{enable\_thinking=False}). Step-level evaluation allows steps from the same episode in both train and validation sets (same-episode leakage). Episode-level evaluation holds out entire episodes; the resulting $47.1 \pm 2.2\%$ is below the 50\% chance baseline. A data scaling ablation (Table~\ref{tab:data-scaling}) confirms this is structural rather than data-limited.}
189	\label{tab:seed-robustness}
190	\end{table}
191	
192	The contrast between step-level ($54.1 \pm 5.4\%$) and episode-level ($47.1 \pm 2.2\%$) evaluation reveals a generalization gap: the step-level signal likely reflects memorization of episode-specific context (enabled by same-episode leakage) rather than extraction of generalizable routing features. At episode level, the router performs below chance across all 8 seeds (range: 43.1\%--49.6\%). A data scaling ablation (Table~\ref{tab:data-scaling}) rules out data scarcity as the cause: scaling from 25\% to 800\% of the original training set ($32{\times}$ range) yields no improvement, converging to the always-deterministic baseline ($50\%$). The failure is structural: with DAF $= 90.4\%$ and all task types deterministic-majority (86:9 label ratio), always-deterministic trivially solves the episode-level routing problem, leaving no learnable signal for a step-level router.
193	
194	\paragraph{Data scaling ablation.} To test whether the episode-level generalization failure stems from data scarcity, we vary training set size from 25\% to 800\% of the original via paraphrase-based data augmentation (synonym substitution + template variation on step observations), holding the episode-level validation set fixed. Table~\ref{tab:data-scaling} reports the results.
195	
196	\begin{table}[h]
197	\centering
198	\small
199	\begin{tabular}{@{}rccc@{}}
200	\toprule
201	Scale & Train samples & Det\% & Ep.-level Bal.\ Acc.\ (\%) \\
202	\midrule
203	25\% & 433 & ${\sim}90$ & $49.5 \pm 0.3$ \\
204	50\% & 867 & ${\sim}90$ & $51.5$ \\
205	100\% & 1{,}735 & 89.6 & $49.9 \pm 0.1$ \\
206	200\% & 3{,}470 & 94.2 & $50.0 \pm 0.0$ \\
207	800\% & 13{,}880 & ${\sim}97.7$ & $51.0 \pm 1.1$ \\
208	\midrule
209	Always-det & --- & --- & 50.0 \\
210	\bottomrule
211	\end{tabular}
212	\caption{Data scaling ablation: episode-level balanced accuracy across training set sizes (25\%--800\% of original, $32{\times}$ range). Internal recall $= 0.0$ at all scales (complete majority-class collapse). Det\%: fraction of deterministic-preferred labels in training data. The 50\% scale is a single seed; all others report mean$\pm$std across seeds.}
213	\label{tab:data-scaling}
214	\end{table}
215	
216	All scales hover at ${\sim}50\%$ episode-level balanced accuracy---equivalent to the always-deterministic baseline---with no monotonic improvement as data increases. This rules out data scarcity as the explanation for the router's episode-level failure and points instead to a structural limitation: when DAF $= 90.4\%$ and all task types are deterministic-majority (86:9 label ratio), the episode-level routing problem is trivially solved by always choosing deterministic, leaving no learnable signal for a step-level router to exploit.
217	
218	Augmentation disproportionately increases the majority (deterministic) class: Det\% rises from 89.6\% at 100\% to 94.2\% at 200\% and ${\sim}97.7\%$ at 800\%. However, the complete collapse to majority-class prediction (internal recall $= 0.0$) occurs even at the smallest unaugmented scale (25\%, ${\sim}90\%$ det), confirming this is not an augmentation artifact. Balanced accuracy corrects for class imbalance by averaging per-class recall, so the metric itself is not biased by the skew.
219	
220	Decomposition metrics are stable under bootstrap resampling (1{,}000 resamples of the 245-episode dataset): DAF $= 90.6\% \pm 4.2\%$ (95\% CI $[81.6\%, 98.8\%]$); Pearson $r = 0.975 \pm 0.011$ (95\% CI $[0.952, 0.995]$). The death avoidance dominance finding is robust to both resampling and split perturbation.
221	
222	\paragraph{Per-task-type evaluation breakdown.} To test whether the router learns transferable routing strategies or merely task-type classification, we evaluate existing checkpoints (8 seeds) separately on each of the 11 task types. Of the 11 task types, 7 have \emph{all-deterministic} labels (no internal-preferred episodes exist), making balanced accuracy undefined---the router has nothing to learn beyond the trivial always-deterministic default. For the remaining 4 task types where both classes are present, balanced accuracy ranges from 50.0\% to 73.0\%, but this apparent signal does not indicate cross-task-type routing transfer: the router is effectively classifying task types (which correlate with death risk) rather than extracting a generalizable routing strategy. This complements the data scaling and capacity scaling ablations: routing signal does not transfer across task types because the signal \emph{is} the task type---whether a given task carries death risk.
223	
224	\section{Penalty Sensitivity Analysis}
225	\label{app:penalty}
226	
227	\begin{table}[h]
228	\centering
229	\small
230	\begin{tabular}{@{}rrr@{}}
231	\toprule
232	$P$ & DAF($P$) & 95\% CI \\
233	\midrule
234	0 & 7.5\% & [$-36.7$, $83.1$] \\
235	10 & 50.4\% & [$19.8$, $94.5$] \\
236	25 & 70.8\% & [$48.5$, $97.1$] \\
237	50 & 82.6\% & [$67.6$, $98.4$] \\
238	100\textsuperscript{*} & 90.4\% & [$81.5$, $99.1$] \\
239	200 & 95.0\% & [$90.0$, $99.5$] \\
240	500 & 97.9\% & [$95.8$, $99.8$] \\
241	\bottomrule
242	\end{tabular}
243	\caption{Sensitivity of DAF to death penalty magnitude $P$. DAF$(P) = 1 - \Delta_{\text{nd}} / \Delta_{\text{full}}(P)$, where $\Delta_{\text{full}}(P) \approx \delta \cdot P + \Delta_{\text{nd}}$, $\delta = 0.2653$ is the death-rate differential, and $\Delta_{\text{nd}} = 2.84$ (strict neither-died filtering). Bootstrap 95\% CIs from 1{,}000 resamples. \textsuperscript{*}Default setting.}
244	\label{tab:penalty-sensitivity}
245	\end{table}
246	
247	The non-death score gap $\Delta_{\text{nd}} = 2.84$ is invariant across penalty levels---it depends only on surviving-episode performance, not on $P$. As $P$ increases, $\Delta_{\text{full}}$ grows ($16.33$ at $P{=}50$, $29.60$ at $P{=}100$, $56.13$ at $P{=}200$) while $\Delta_{\text{nd}}$ remains fixed, mechanically increasing DAF.
248	
249	\paragraph{Mechanism boundary: death specificity.}
250	The $r = 0.97$ correlation between per-task death-rate differential and $\Delta_{\text{full}}$ is specific to catastrophic death (score $= -100$). Broader failure definitions dissolve the correlation entirely: defining ``failure'' as any non-positive score ($T{=}0$) yields $r = -0.13$ ($p = 0.70$), because non-death episodes show near-zero performance differential between strategies ($\Delta_{\text{nd}} = 2.84$). Table~\ref{tab:penalty-correlation} quantifies this specificity across penalty magnitudes.
251	
252	\begin{table}[h]
253	\centering
254	\small
255	\begin{tabular}{@{}rccl@{}}
256	\toprule
257	$P$ & $r$ & $p$ & Sig.\ ($\alpha{=}0.05$) \\
258	\midrule
259	10 & $-0.08$ & $0.813$ & No \\
260	25 & $0.51$ & $0.108$ & No \\
261	50 & $0.86$ & $0.0006$ & Yes \\
262	100\textsuperscript{*} & $0.97$ & $8 \times 10^{-7}$ & Yes \\
263	200 & $0.99$ & $1 \times 10^{-9}$ & Yes \\
264	\bottomrule
265	\end{tabular}
266	\caption{Pearson $r$ between per-task death-rate differential and $\Delta_{\text{full}}(P)$ across penalty magnitudes. The correlation is non-significant at low penalties and emerges at $P \geq 50$, reflecting the transition from non-death-dominated to death-dominated score gaps. \textsuperscript{*}Default ScienceWorld setting.}
267	\label{tab:penalty-correlation}
268	\end{table}
269	
270	This sharpens our central finding: death is not merely the dominant component of routing signal---it is effectively the \emph{only} component that generates differential routing signal in ScienceWorld. At low penalties, the death contribution is small and $\Delta_{\text{full}}$ reduces to $\Delta_{\text{nd}} \approx 2.84$, which is near-uniform across task types ($\text{mean non-death gap} = -1.19$ excluding the \texttt{find-non-living-thing} outlier); consequently, death-rate differential has no predictive power. As $P$ increases, the death term dominates $\Delta_{\text{full}}$, and the correlation sharpens because death rates \emph{are} the performance gap. The DAF values in Table~\ref{tab:penalty-sensitivity} increase monotonically with $P$, but this is a mathematical consequence of the decomposition ($\text{DAF} = \delta P / (\delta P + \Delta_{\text{nd}})$), not evidence of mechanism robustness.
271	
272	\section{Cross-Model Verification}
273	\label{app:cross-model}
274	
275	A preliminary pilot with Llama-3.1-8B-Instruct ($N{=}10$ episode pairs, 2 task types: \texttt{freeze} and \texttt{find-animal}) shows directionally consistent death patterns. The internal strategy dies in 50\% of episodes versus 20\% for deterministic (cf.\ 42.9\% vs.\ 16.3\% for Qwen2.5-7B). The sample is insufficient for statistical inference, but the direction is consistent with the Qwen results, suggesting the death-avoidance phenomenon is not model-specific.
276	
277	\section{Failure Mode Analysis}
278	\label{app:failure-modes}
279	
280	The most common failure mode for the internal strategy is state hallucination: the model predicts that an action succeeded (e.g., ``the water is now boiling'') when the environment state did not change, leading to cascading errors that trigger agent death. The deterministic strategy avoids this by receiving ground-truth observations, but still dies in 16.3\% of episodes---primarily from selecting inherently dangerous actions (e.g., eating toxic substances) rather than from state misestimation.
281	
282	\section{Ablation Studies}
283	\label{app:ablations}
284	
285	\paragraph{Capacity scaling.} We scale the implicit router from Qwen3-0.6B to Qwen3-4B. Step-level balanced accuracy shows no consistent improvement: 0.6B achieves $52.8\%$, 1.7B achieves $54.1\%$, and 4B achieves $53.5\%$. This confirms the router failure is structural rather than capacity-limited.
286	
287	\paragraph{Reasoning depth.} An ablation comparing chain-of-thought reasoning against direct-answer generation on 6 task types found no significant difference (Mann--Whitney $p > 0.26$, $|d| \leq 0.31$) and near-identical death rates (41.8\% vs.\ 42.5\%), confirming that reasoning depth does not meaningfully alter internal-mode outcomes.
288	
289	\section{Cross-Environment Analysis: ALFWorld}
290	\label{app:cross-env}
291	
292	We evaluate on ALFWorld~\citep{alfworld-2021}, a text-based household environment with 6 task types (json\_2.1.1 split, valid\_seen, 135 games, max 50 steps, binary success metric), using Qwen2.5-7B-Instruct. Unlike ScienceWorld, ALFWorld has no death penalty---failure means exhausting the step budget. The two modalities differ in \emph{information access}: the internal strategy receives only free-text observations, while the deterministic strategy additionally receives admissible actions at each step. This is an information asymmetry rather than a computation mode switch.
293	
294	The success rate gap is large: 27.4\% (deterministic) vs.\ 3.0\% (internal), reflecting the 7B model's near-inability to solve household tasks without admissible-action guidance. The label distribution (Table~\ref{tab:cross-env}) shows 35 deterministic-preferred (25.9\%), 2 internal-preferred (1.5\%), and 98 no-preference (72.6\%), of which 96 are both-fail. The deterministic advantage stems entirely from the information gap rather than death avoidance.
295	
296	\begin{figure}[h]
297	\centering
298	\includegraphics[width=\columnwidth]{figures/signal_reversal.pdf}
299	\caption{Label distribution reversal across environments. In ScienceWorld (with $-100$ death penalty), deterministic-preferred labels dominate (86:9). In MATH (no death penalty), the pattern inverts (17:30), with 84.3\% no preference.}
300	\label{fig:signal-reversal}
301	\end{figure}
302	
303	\begin{table}[h]
304	\centering
305	\small
306	\resizebox{\columnwidth}{!}{%
307	\begin{tabular}{@{}lccccc@{}}
308	\toprule
309	Environment & $N$ & Det\% & Int\% & NoPref\% & Death? \\
310	\midrule
311	ScienceWorld & 245 & 35.1 & 3.7 & 61.2 & Yes ($-100$) \\
312	MATH & 300 & 5.7 & 10.0 & 84.3 & No \\
313	ALFWorld & 135 & 25.9 & 1.5 & 72.6 & No\textsuperscript{$\dagger$} \\
314	\bottomrule
315	\end{tabular}}
316	\caption{Cross-environment label distribution. $\dagger$\,ALFWorld's deterministic advantage stems from action-space pruning, not death avoidance.}
317	\label{tab:cross-env}
318	\end{table}
319	
320	\end{document}
321	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "586f0e27-a0c7-4373-b542-a2d00802d10a",
  "isSidechain": false,
  "promptId": "2cc35627-090b-4e8e-873a-80e6ce7d766f",
  "type": "user",
  "uuid": "54462d74-d436-4385-8d47-fc0b49a7d340",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/main.tex",
      "content": "\\documentclass[11pt]{article}\n\n\\usepackage[review]{acl}\n\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage[T1]{fontenc}\n\\usepackage[utf8]{inputenc}\n\\usepackage{microtype}\n\\usepackage{graphicx}\n\\graphicspath{{figures/}}\n\\usepackage{booktabs}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{algorithm}\n\\usepackage{algorithmic}\n\n\\title{Death Avoidance as the Dominant Routing Signal:\\\\A Counterfactual Analysis on ScienceWorld}\n\n\\author{Anonymous}\n\n\\begin{document}\n\\maketitle\n\n\\input{abstract}\n\\input{introduction}\n\\input{method}\n\\input{experiments}\n\\input{related_work}\n\\input{discussion}\n\\input{conclusion}\n\n\\section*{Limitations}\n\nOur primary analysis uses a single environment (ScienceWorld, 11 of 30 task types) with one backbone (Qwen2.5-7B-Instruct); generalization requires further validation. The $-100$ death penalty amplifies DAF; environments with softer penalties would exhibit lower DAF values (Appendix~\\ref{app:penalty}). The 19 excluded task types (63\\%) lack routing signal because both strategies typically time out within 30 steps; increasing the step budget could surface additional signal. Our internal-reasoning baseline uses single-pass ReAct~\\citep{react-2023}; more sophisticated strategies (e.g., Reflexion~\\citep{reflexion-2023}) may reduce internal death rates and lower DAF. Episode-level labels may assign suboptimal routing to individual steps, particularly those preceding death events, and training on pure-strategy trajectories introduces distribution shift at deployment~\\citep{dagger-2011}. Cross-environment analyses on MATH and ALFWorld (\\S\\ref{sec:discussion}, Appendix~\\ref{app:cross-env}) provide supporting evidence but do not conclusively establish generalization. A Llama-3.1-8B pilot ($N{=}10$; Appendix~\\ref{app:cross-model}) shows directional consistency but is insufficient for statistical inference.\n\n\\section*{Ethics Statement}\n\nThis work uses ScienceWorld \\cite{scienceworld-2022}, a publicly available text-based simulation environment, and does not involve human subjects or private data. All language models are accessed via standard APIs or publicly released weights. We report computational costs: approximately 40 GPU-hours on two consumer GPUs for data collection, router training, and evaluation. Code and data will be released upon acceptance.\n\n\\bibliography{references}\n\n\\appendix\n\n\\section{Labeling Quality Audit}\n\\label{app:labeling}\n\nA potential concern is oracle circularity: whether episode-level labels reflect tie-breaking artifacts rather than genuine modality differences. We audit all 245 labels. Of the 150 \\texttt{no\\_preference} labels (61.2\\%), 115 (46.9\\%) are both-alive ties and 35 (14.3\\%) are both-dead---all excluded from router training. The remaining 95 training labels are entirely genuine: 75 from death asymmetry (70 deterministic-preferred, 5 internal-preferred) and 20 from score comparison with both strategies surviving (16 deterministic-preferred, 4 internal-preferred). Zero labels depend on tie-breaking. Retraining the router using only death-asymmetry labels yields step-level balanced accuracy of 57.3\\%, within 1$\\sigma$ of the full-label retrain (57.6 $\\pm$ 0.5\\%, step-level Trainer evaluation), confirming that score-comparison labels contribute negligible additional signal. (Step-level metrics are used here for the relative comparison; as shown in \\S\\ref{sec:router-diagnostic}, absolute generalization to new episodes is near chance.) The 97.4\\% step-level tie rate (\\S\\ref{sec:collection}) further motivates episode-level over step-level labeling.\n\n\\section{Per-Task Decomposition}\n\\label{app:per-task}\nWe select 11 of ScienceWorld's 30 task types via prescreening: task types where both strategies complete at least one episode within the 30-step budget are retained; types where both strategies time out on all seed variations are excluded.\\footnote{Prescreening ensures that the counterfactual comparison is meaningful---task types where neither strategy makes progress provide no routing signal.}\n\n\\begin{table}[h]\n\\centering\n\\scriptsize\n\\setlength{\\tabcolsep}{2.5pt}\n\\begin{tabular}{@{}lrrccc@{}}\n\\toprule\nTask & $n$ & $\\Delta_\\text{full}$ & D\\%\\textsubscript{int} & D\\%\\textsubscript{det} & D / I / N \\\\\n\\midrule\nid-life-stages-1       & 20  & $+47.50$ & 55   & 10   & 9 / 0 / 11  \\\\\nlifespan-long          & 25  & $+44.00$ & 56   & 16   & 11 / 1 / 13 \\\\\nlifespan-l-then-s      & 20  & $+40.80$ & 45   & 10   & 8 / 1 / 11  \\\\\ninclined-plane         & 20  & $+36.00$ & 55   & 20   & 7 / 0 / 13  \\\\\nfreeze                 & 20  & $+30.50$ & 55   & 25   & 6 / 0 / 14  \\\\\nmeas-melt-point        & 20  & $+30.05$ & 55   & 25   & 6 / 0 / 14  \\\\\nid-life-stages-2       & 20  & $+30.00$ & 50   & 20   & 6 / 0 / 14  \\\\\nfind-animal            & 20  & $+26.65$ & 50   & 25   & 5 / 0 / 15  \\\\\ngrow-fruit             & 20  & $+25.10$ & 45   & 20   & 6 / 1 / 13  \\\\\nchem-mix               & 20  & $+21.80$ & 45   & 25   & 6 / 2 / 12  \\\\\n\\midrule\nfind-non-living$^\\dagger$ & 40 & $+9.58$ & 0  & 0    & 16 / 4 / 20 \\\\\n\\midrule\n\\textbf{All (11 tasks)} & \\textbf{245} & $\\mathbf{+29.60}$ & \\textbf{42.9} & \\textbf{16.3} & \\textbf{86 / 9 / 150} \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Per-task decomposition of the death avoidance effect. D\\%: death rate for internal (int) and deterministic (det) strategies. D/I/N: episode labels (det-preferred / internal-preferred / no-preference). Sorted by $\\Delta_{\\text{full}}$ descending. $\\dagger$\\,Only task with zero deaths under both strategies; $n{=}40$ because data was collected in two batches, with the second batch adding 20 episodes to increase statistical power for this zero-death outlier.}\n\\label{tab:per-task}\n\\end{table}\n\n\\paragraph{Task selection and anti-cherry-picking.}\nThe 11 included task types are those exhibiting meaningful routing signal in prescreening, not those with the highest death rates. The deterministic-strategy death rate is comparable between included (17.8\\%) and excluded (14.9\\%) task types, confirming that prescreening does not select for death-prone tasks. Rather, the key distinction is the \\emph{presence} of routing signal: all 11 included tasks have $\\Delta_{\\text{nd}} \\neq 0$ (non-zero performance gap on surviving episodes), while 53\\% of excluded tasks show $\\Delta_{\\text{nd}} = 0$---neither strategy outperforms the other even when both survive, typically because both time out before making progress. \\texttt{find-non-living-thing} serves as an internal counterexample: it has zero deaths under both strategies yet is included because it exhibits non-death routing signal ($\\Delta_{\\text{full}} = +9.58$ entirely from score differences), and deterministic is not always preferred (4 of 20 non-tie labels favor internal).\n\n\\section{Correlation Robustness}\n\\label{app:correlation}\n\nThe Pearson $r = 0.9698$ reported in \\S\\ref{sec:death-decomp} is robust across multiple diagnostics. Spearman rank correlation is $\\rho = 0.986$ ($p = 2.4 \\times 10^{-8}$), confirming that the relationship is not driven by outliers or non-linearity. A nonparametric bootstrap (10{,}000 resamples) yields 95\\% CI $[0.952, 0.995]$.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{@{}lr@{}}\n\\toprule\nTask removed & $r_{\\text{LOO}}$ \\\\\n\\midrule\nid-life-stages-1       & 0.963 \\\\\nlifespan-long          & 0.969 \\\\\nlifespan-l-then-s      & 0.976 \\\\\ninclined-plane         & 0.969 \\\\\nfreeze                 & 0.971 \\\\\nmeas-melt-point        & 0.972 \\\\\nid-life-stages-2       & 0.972 \\\\\nfind-animal            & 0.970 \\\\\ngrow-fruit             & 0.973 \\\\\nchem-mix               & 0.969 \\\\\nfind-non-living        & 0.980 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Leave-one-out Pearson $r$ for the death rate differential vs.\\ $\\Delta_{\\text{full}}$ correlation. Full $r = 0.970$; LOO range $[0.963, 0.980]$. No single task type is a leverage point.}\n\\label{tab:loo}\n\\end{table}\n\n\\section{Router Training Details}\n\\label{app:router-details}\n\nWe use Qwen3-1.7B for the router to avoid circular dependency with the Qwen2.5-7B data-generating model.\n\nWith gradient accumulation of 1 (effective batch size 4), routing performance is highly sensitive to the evaluation split, suggesting overfitting to specific train/validation partition boundaries. With gradient accumulation of 8 (effective batch size 32), step-level performance stabilizes across splits (${\\sim}54\\%$ balanced accuracy). All reported results use gradient accumulation 8.\n\nUnder step-level evaluation with a fixed data split, cross-seed balanced accuracy ranges from 52.7\\% to 58.1\\%, but internal recall varies from 51.5\\% to 81.8\\%, reflecting threshold sensitivity. However, episode-level evaluation reveals that this apparent discrimination does not generalize: balanced accuracy drops to $47.1 \\pm 2.2\\%$ across 8 cross-split seeds (Appendix~\\ref{app:seed-robustness}). Deployed end-to-end, the trained router allocates 97.0\\% of episodes to deterministic computation with 17.6\\% death rate, and misrouting cost (death from internally-routed episodes) exceeds the benefit of correctly routing rare internal-preferred cases.\n\n\\paragraph{Evaluation methods.} All results use \\emph{generation-based evaluation}: the model generates a routing label as text (\\texttt{enable\\_thinking=False}), parsed for classification. We evaluate at two granularities: \\emph{step-level} (steps from the same episode may appear in both train and validation sets) and \\emph{episode-level} (entire episodes held out). Step-level accuracy ($54.1 \\pm 5.4\\%$) exceeds chance, indicating the router captures some signal, but episode-level accuracy ($47.1 \\pm 2.2\\%$, below chance) shows this does not generalize to unseen episodes. A data scaling ablation (Appendix~\\ref{app:seed-robustness}) rules out data scarcity, pointing instead to a structural limitation: always-deterministic is trivially near-optimal given DAF $= 90.4\\%$. Both metrics are reported in the main text; the model-size ablation (Appendix~\\ref{app:ablations}) uses step-level evaluation.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{@{}lcc@{}}\n\\toprule\nHyperparameter & Classification Head & Implicit Router \\\\\n\\midrule\nBase model & Qwen3-1.7B & Qwen3-1.7B \\\\\nArchitecture & Linear + LoRA & SFT + LoRA \\\\\nLoRA $r$ / $\\alpha$ & 16 / 32 & 16 / 32 \\\\\nLearning rate & 2e-5 & 2e-4 \\\\\nOptimizer & AdamW & AdamW \\\\\nEpochs & 3 & 3 \\\\\nBatch size (per device) & 4 & 4 \\\\\nGradient accumulation & 8 & 8 \\\\\nWarmup ratio & 0.1 & 0.1 \\\\\nWeight decay & 0.01 & 0.01 \\\\\nMax sequence length & 512 & 512 \\\\\nSeeds & \\{42\\} & \\{42, 123, 456, 789\\} \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Router training hyperparameters. Both architectures use the same base model with LoRA adaptation. The classification head degenerates across all configurations; the implicit router results are reported as 4-seed mean$\\pm$std.}\n\\label{tab:hyperparams}\n\\end{table}\n\n\\section{Seed Robustness}\n\\label{app:seed-robustness}\n\nWe assess router generalization at two evaluation granularities: \\emph{step-level}, where steps from the same episode may appear in both train and validation sets, and \\emph{episode-level}, where entire episodes are held out. Both use cross-split evaluation (seeds $\\{42, \\ldots, 49\\}$, 8 seeds total), where the data partition and training seed both vary. Table~\\ref{tab:seed-robustness} reports per-seed results.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{@{}llcc@{}}\n\\toprule\nEval.\\ Granularity & Seed & Bal.\\ Acc.\\ (\\%) \\\\\n\\midrule\nStep-level & 42 & 57.06 \\\\\n(same-episode & 43 & 63.99 \\\\\nleakage) & 44 & 55.43 \\\\\n & 45 & 56.14 \\\\\n & 46 & 55.45 \\\\\n & 47 & 50.08 \\\\\n & 48 & 48.03 \\\\\n & 49 & 59.30 \\\\\n\\cmidrule{2-3}\n & Mean$\\pm$std & $54.1 \\pm 5.4$ \\\\\n\\midrule\nEpisode-level & 42 & 48.1 \\\\\n(held-out & 43 & 47.9 \\\\\nepisodes) & 44 & 49.6 \\\\\n & 45 & 49.4 \\\\\n & 46 & 48.5 \\\\\n & 47 & 43.1 \\\\\n & 48 & 45.4 \\\\\n & 49 & 44.8 \\\\\n\\cmidrule{2-3}\n & Mean$\\pm$std & $47.1 \\pm 2.2$ \\\\\n\\midrule\n\\multicolumn{2}{@{}l}{Always-det (= majority-vote)} & 50.0 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Per-seed router performance under cross-split evaluation (8 seeds, generation-based, \\texttt{enable\\_thinking=False}). Step-level evaluation allows steps from the same episode in both train and validation sets (same-episode leakage). Episode-level evaluation holds out entire episodes; the resulting $47.1 \\pm 2.2\\%$ is below the 50\\% chance baseline. A data scaling ablation (Table~\\ref{tab:data-scaling}) confirms this is structural rather than data-limited.}\n\\label{tab:seed-robustness}\n\\end{table}\n\nThe contrast between step-level ($54.1 \\pm 5.4\\%$) and episode-level ($47.1 \\pm 2.2\\%$) evaluation reveals a generalization gap: the step-level signal likely reflects memorization of episode-specific context (enabled by same-episode leakage) rather than extraction of generalizable routing features. At episode level, the router performs below chance across all 8 seeds (range: 43.1\\%--49.6\\%). A data scaling ablation (Table~\\ref{tab:data-scaling}) rules out data scarcity as the cause: scaling from 25\\% to 800\\% of the original training set ($32{\\times}$ range) yields no improvement, converging to the always-deterministic baseline ($50\\%$). The failure is structural: with DAF $= 90.4\\%$ and all task types deterministic-majority (86:9 label ratio), always-deterministic trivially solves the episode-level routing problem, leaving no learnable signal for a step-level router.\n\n\\paragraph{Data scaling ablation.} To test whether the episode-level generalization failure stems from data scarcity, we vary training set size from 25\\% to 800\\% of the original via paraphrase-based data augmentation (synonym substitution + template variation on step observations), holding the episode-level validation set fixed. Table~\\ref{tab:data-scaling} reports the results.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{@{}rccc@{}}\n\\toprule\nScale & Train samples & Det\\% & Ep.-level Bal.\\ Acc.\\ (\\%) \\\\\n\\midrule\n25\\% & 433 & ${\\sim}90$ & $49.5 \\pm 0.3$ \\\\\n50\\% & 867 & ${\\sim}90$ & $51.5$ \\\\\n100\\% & 1{,}735 & 89.6 & $49.9 \\pm 0.1$ \\\\\n200\\% & 3{,}470 & 94.2 & $50.0 \\pm 0.0$ \\\\\n800\\% & 13{,}880 & ${\\sim}97.7$ & $51.0 \\pm 1.1$ \\\\\n\\midrule\nAlways-det & --- & --- & 50.0 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Data scaling ablation: episode-level balanced accuracy across training set sizes (25\\%--800\\% of original, $32{\\times}$ range). Internal recall $= 0.0$ at all scales (complete majority-class collapse). Det\\%: fraction of deterministic-preferred labels in training data. The 50\\% scale is a single seed; all others report mean$\\pm$std across seeds.}\n\\label{tab:data-scaling}\n\\end{table}\n\nAll scales hover at ${\\sim}50\\%$ episode-level balanced accuracy---equivalent to the always-deterministic baseline---with no monotonic improvement as data increases. This rules out data scarcity as the explanation for the router's episode-level failure and points instead to a structural limitation: when DAF $= 90.4\\%$ and all task types are deterministic-majority (86:9 label ratio), the episode-level routing problem is trivially solved by always choosing deterministic, leaving no learnable signal for a step-level router to exploit.\n\nAugmentation disproportionately increases the majority (deterministic) class: Det\\% rises from 89.6\\% at 100\\% to 94.2\\% at 200\\% and ${\\sim}97.7\\%$ at 800\\%. However, the complete collapse to majority-class prediction (internal recall $= 0.0$) occurs even at the smallest unaugmented scale (25\\%, ${\\sim}90\\%$ det), confirming this is not an augmentation artifact. Balanced accuracy corrects for class imbalance by averaging per-class recall, so the metric itself is not biased by the skew.\n\nDecomposition metrics are stable under bootstrap resampling (1{,}000 resamples of the 245-episode dataset): DAF $= 90.6\\% \\pm 4.2\\%$ (95\\% CI $[81.6\\%, 98.8\\%]$); Pearson $r = 0.975 \\pm 0.011$ (95\\% CI $[0.952, 0.995]$). The death avoidance dominance finding is robust to both resampling and split perturbation.\n\n\\paragraph{Per-task-type evaluation breakdown.} To test whether the router learns transferable routing strategies or merely task-type classification, we evaluate existing checkpoints (8 seeds) separately on each of the 11 task types. Of the 11 task types, 7 have \\emph{all-deterministic} labels (no internal-preferred episodes exist), making balanced accuracy undefined---the router has nothing to learn beyond the trivial always-deterministic default. For the remaining 4 task types where both classes are present, balanced accuracy ranges from 50.0\\% to 73.0\\%, but this apparent signal does not indicate cross-task-type routing transfer: the router is effectively classifying task types (which correlate with death risk) rather than extracting a generalizable routing strategy. This complements the data scaling and capacity scaling ablations: routing signal does not transfer across task types because the signal \\emph{is} the task type---whether a given task carries death risk.\n\n\\section{Penalty Sensitivity Analysis}\n\\label{app:penalty}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{@{}rrr@{}}\n\\toprule\n$P$ & DAF($P$) & 95\\% CI \\\\\n\\midrule\n0 & 7.5\\% & [$-36.7$, $83.1$] \\\\\n10 & 50.4\\% & [$19.8$, $94.5$] \\\\\n25 & 70.8\\% & [$48.5$, $97.1$] \\\\\n50 & 82.6\\% & [$67.6$, $98.4$] \\\\\n100\\textsuperscript{*} & 90.4\\% & [$81.5$, $99.1$] \\\\\n200 & 95.0\\% & [$90.0$, $99.5$] \\\\\n500 & 97.9\\% & [$95.8$, $99.8$] \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Sensitivity of DAF to death penalty magnitude $P$. DAF$(P) = 1 - \\Delta_{\\text{nd}} / \\Delta_{\\text{full}}(P)$, where $\\Delta_{\\text{full}}(P) \\approx \\delta \\cdot P + \\Delta_{\\text{nd}}$, $\\delta = 0.2653$ is the death-rate differential, and $\\Delta_{\\text{nd}} = 2.84$ (strict neither-died filtering). Bootstrap 95\\% CIs from 1{,}000 resamples. \\textsuperscript{*}Default setting.}\n\\label{tab:penalty-sensitivity}\n\\end{table}\n\nThe non-death score gap $\\Delta_{\\text{nd}} = 2.84$ is invariant across penalty levels---it depends only on surviving-episode performance, not on $P$. As $P$ increases, $\\Delta_{\\text{full}}$ grows ($16.33$ at $P{=}50$, $29.60$ at $P{=}100$, $56.13$ at $P{=}200$) while $\\Delta_{\\text{nd}}$ remains fixed, mechanically increasing DAF.\n\n\\paragraph{Mechanism boundary: death specificity.}\nThe $r = 0.97$ correlation between per-task death-rate differential and $\\Delta_{\\text{full}}$ is specific to catastrophic death (score $= -100$). Broader failure definitions dissolve the correlation entirely: defining ``failure'' as any non-positive score ($T{=}0$) yields $r = -0.13$ ($p = 0.70$), because non-death episodes show near-zero performance differential between strategies ($\\Delta_{\\text{nd}} = 2.84$). Table~\\ref{tab:penalty-correlation} quantifies this specificity across penalty magnitudes.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{@{}rccl@{}}\n\\toprule\n$P$ & $r$ & $p$ & Sig.\\ ($\\alpha{=}0.05$) \\\\\n\\midrule\n10 & $-0.08$ & $0.813$ & No \\\\\n25 & $0.51$ & $0.108$ & No \\\\\n50 & $0.86$ & $0.0006$ & Yes \\\\\n100\\textsuperscript{*} & $0.97$ & $8 \\times 10^{-7}$ & Yes \\\\\n200 & $0.99$ & $1 \\times 10^{-9}$ & Yes \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Pearson $r$ between per-task death-rate differential and $\\Delta_{\\text{full}}(P)$ across penalty magnitudes. The correlation is non-significant at low penalties and emerges at $P \\geq 50$, reflecting the transition from non-death-dominated to death-dominated score gaps. \\textsuperscript{*}Default ScienceWorld setting.}\n\\label{tab:penalty-correlation}\n\\end{table}\n\nThis sharpens our central finding: death is not merely the dominant component of routing signal---it is effectively the \\emph{only} component that generates differential routing signal in ScienceWorld. At low penalties, the death contribution is small and $\\Delta_{\\text{full}}$ reduces to $\\Delta_{\\text{nd}} \\approx 2.84$, which is near-uniform across task types ($\\text{mean non-death gap} = -1.19$ excluding the \\texttt{find-non-living-thing} outlier); consequently, death-rate differential has no predictive power. As $P$ increases, the death term dominates $\\Delta_{\\text{full}}$, and the correlation sharpens because death rates \\emph{are} the performance gap. The DAF values in Table~\\ref{tab:penalty-sensitivity} increase monotonically with $P$, but this is a mathematical consequence of the decomposition ($\\text{DAF} = \\delta P / (\\delta P + \\Delta_{\\text{nd}})$), not evidence of mechanism robustness.\n\n\\section{Cross-Model Verification}\n\\label{app:cross-model}\n\nA preliminary pilot with Llama-3.1-8B-Instruct ($N{=}10$ episode pairs, 2 task types: \\texttt{freeze} and \\texttt{find-animal}) shows directionally consistent death patterns. The internal strategy dies in 50\\% of episodes versus 20\\% for deterministic (cf.\\ 42.9\\% vs.\\ 16.3\\% for Qwen2.5-7B). The sample is insufficient for statistical inference, but the direction is consistent with the Qwen results, suggesting the death-avoidance phenomenon is not model-specific.\n\n\\section{Failure Mode Analysis}\n\\label{app:failure-modes}\n\nThe most common failure mode for the internal strategy is state hallucination: the model predicts that an action succeeded (e.g., ``the water is now boiling'') when the environment state did not change, leading to cascading errors that trigger agent death. The deterministic strategy avoids this by receiving ground-truth observations, but still dies in 16.3\\% of episodes---primarily from selecting inherently dangerous actions (e.g., eating toxic substances) rather than from state misestimation.\n\n\\section{Ablation Studies}\n\\label{app:ablations}\n\n\\paragraph{Capacity scaling.} We scale the implicit router from Qwen3-0.6B to Qwen3-4B. Step-level balanced accuracy shows no consistent improvement: 0.6B achieves $52.8\\%$, 1.7B achieves $54.1\\%$, and 4B achieves $53.5\\%$. This confirms the router failure is structural rather than capacity-limited.\n\n\\paragraph{Reasoning depth.} An ablation comparing chain-of-thought reasoning against direct-answer generation on 6 task types found no significant difference (Mann--Whitney $p > 0.26$, $|d| \\leq 0.31$) and near-identical death rates (41.8\\% vs.\\ 42.5\\%), confirming that reasoning depth does not meaningfully alter internal-mode outcomes.\n\n\\section{Cross-Environment Analysis: ALFWorld}\n\\label{app:cross-env}\n\nWe evaluate on ALFWorld~\\citep{alfworld-2021}, a text-based household environment with 6 task types (json\\_2.1.1 split, valid\\_seen, 135 games, max 50 steps, binary success metric), using Qwen2.5-7B-Instruct. Unlike ScienceWorld, ALFWorld has no death penalty---failure means exhausting the step budget. The two modalities differ in \\emph{information access}: the internal strategy receives only free-text observations, while the deterministic strategy additionally receives admissible actions at each step. This is an information asymmetry rather than a computation mode switch.\n\nThe success rate gap is large: 27.4\\% (deterministic) vs.\\ 3.0\\% (internal), reflecting the 7B model's near-inability to solve household tasks without admissible-action guidance. The label distribution (Table~\\ref{tab:cross-env}) shows 35 deterministic-preferred (25.9\\%), 2 internal-preferred (1.5\\%), and 98 no-preference (72.6\\%), of which 96 are both-fail. The deterministic advantage stems entirely from the information gap rather than death avoidance.\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/signal_reversal.pdf}\n\\caption{Label distribution reversal across environments. In ScienceWorld (with $-100$ death penalty), deterministic-preferred labels dominate (86:9). In MATH (no death penalty), the pattern inverts (17:30), with 84.3\\% no preference.}\n\\label{fig:signal-reversal}\n\\end{figure}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{@{}lccccc@{}}\n\\toprule\nEnvironment & $N$ & Det\\% & Int\\% & NoPref\\% & Death? \\\\\n\\midrule\nScienceWorld & 245 & 35.1 & 3.7 & 61.2 & Yes ($-100$) \\\\\nMATH & 300 & 5.7 & 10.0 & 84.3 & No \\\\\nALFWorld & 135 & 25.9 & 1.5 & 72.6 & No\\textsuperscript{$\\dagger$} \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Cross-environment label distribution. $\\dagger$\\,ALFWorld's deterministic advantage stems from action-space pruning, not death avoidance.}\n\\label{tab:cross-env}\n\\end{table}\n\n\\end{document}\n",
      "numLines": 321,
      "startLine": 1,
      "totalLines": 321
    }
  },
  "sourceToolAssistantUUID": "586f0e27-a0c7-4373-b542-a2d00802d10a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/.claude/sessions/review_reviewer_2_ab9762a8",
  "sessionId": "5bc9ff02-4cf0-48f5-9df4-52d4a45b7804",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-16T12:22:49.439Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01AKV2AyhFW9B6b3tcVi284N`</summary>

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
  "parentUuid": "54462d74-d436-4385-8d47-fc0b49a7d340",
  "isSidechain": false,
  "requestId": "req_011Cb6Etnf5AL2qXVpnfpuhT",
  "type": "assistant",
  "uuid": "aac80498-dfc0-456b-90dc-943824faab78",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/.claude/sessions/review_reviewer_2_ab9762a8",
  "sessionId": "5bc9ff02-4cf0-48f5-9df4-52d4a45b7804",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JbYkbuqCasG2nxYFP3PH34",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1791,
      "cache_read_input_tokens": 26107,
      "output_tokens": 270,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1791,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 270,
          "cache_read_input_tokens": 26107,
          "cache_creation_input_tokens": 1791,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1791
          },
          "type": "message"
        }
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

_source line 16 · 2026-05-16T12:22:50.107Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__verify_references · `toolu_01VRA6Jixnrc5HRQRLJymr9g`</summary>

```json
{
  "paper_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper",
  "project": "simgate-modular-routing"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "aac80498-dfc0-456b-90dc-943824faab78",
  "isSidechain": false,
  "requestId": "req_011Cb6Etnf5AL2qXVpnfpuhT",
  "type": "assistant",
  "uuid": "312bd8ba-a8f6-4efa-8668-182fbbce5f07",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/.claude/sessions/review_reviewer_2_ab9762a8",
  "sessionId": "5bc9ff02-4cf0-48f5-9df4-52d4a45b7804",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JbYkbuqCasG2nxYFP3PH34",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1791,
      "cache_read_input_tokens": 26107,
      "output_tokens": 270,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1791,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 270,
          "cache_read_input_tokens": 26107,
          "cache_creation_input_tokens": 1791,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1791
          },
          "type": "message"
        }
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

_source line 17_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[Round 8 审稿请求]: ## Round 8 审稿任务 — Reviewer 2（新颖性 + 完整性 + 写作质量）  ### Venue 信息 - **会议**: EMNLP 2026 (通过 ARR May 2026 cycle 提交) - **截止日期**: 2026-05-25 - **页数限制**: 正文 8 页 + 无限参考文献页 - **模板**: ACL LaTeX (`\\…",
  "leafUuid": "312bd8ba-a8f6-4efa-8668-182fbbce5f07",
  "sessionId": "5bc9ff02-4cf0-48f5-9df4-52d4a45b7804"
}
```

---

### Runtime record

_source line 18_

```json
{
  "type": "ai-title",
  "aiTitle": "Review paper on modular routing with counterfactual analysis",
  "sessionId": "5bc9ff02-4cf0-48f5-9df4-52d4a45b7804"
}
```

---

### Tool result

_source line 19 · 2026-05-16T12:22:55.960Z_

<details><summary>↩ Tool result · `toolu_01AKV2AyhFW9B6b3tcVi284N`</summary>

```text
Web search results for query: "ACL ARR 2026 reviewer guidelines review form criteria scoring"

Links: [{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"aclrollingreview/reviewing.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/reviewing.md"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"}]

I've found comprehensive information about ACL ARR 2026 reviewer guidelines and the review form. Here's what I found:

## Reviewer Scoring Criteria

Starting with February 2025, ARR reviewers are asked to provide three scores: soundness, excitement, and overall recommendation.

### Soundness Score
The soundness scores must be justified by the text of the review. If you give a low Soundness score without finding any major faults, this means that your review is not a faithful explanation of your recommendation, and you need to revise it.

### Excitement Score
Such preferences are more subjective and should be reflected in a separate excitement score, which is orthogonal to the assessment of the soundness of the paper. Excitement is subjective, and does not necessarily follow what is popular in the field.

### Overall Recommendation Score
The Overall assessment score is an explicit recommendation for the outcome of this paper, if it were committed to an *ACL venue. This is a composite score reflecting your assessment of soundness, excitement, and also other factors like novelty and impact.

## Review Form Criteria for Main vs Findings Papers

The main criteria for Findings are soundness and reproducibility. Conference recommendations may also consider novelty, impact and other factors.

The official review form and detailed guidelines are available at:
- Reviewer Guidelines: aclrollingreview.org/reviewerguidelines
- Review Form: aclrollingreview.org/reviewform


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "aac80498-dfc0-456b-90dc-943824faab78",
  "isSidechain": false,
  "promptId": "2cc35627-090b-4e8e-873a-80e6ce7d766f",
  "type": "user",
  "uuid": "f048bc3e-6090-4264-9e50-b1b518e69a5e",
  "toolUseResult": {
    "query": "ACL ARR 2026 reviewer guidelines review form criteria scoring",
    "results": [
      {
        "tool_use_id": "srvtoolu_017PUFRXMkMgRxQbQPbLmrUB",
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
      "I've found comprehensive information about ACL ARR 2026 reviewer guidelines and the review form. Here's what I found:\n\n## Reviewer Scoring Criteria\n\nStarting with February 2025, ARR reviewers are asked to provide three scores: soundness, excitement, and overall recommendation.\n\n### Soundness Score\nThe soundness scores must be justified by the text of the review. If you give a low Soundness score without finding any major faults, this means that your review is not a faithful explanation of your recommendation, and you need to revise it.\n\n### Excitement Score\nSuch preferences are more subjective and should be reflected in a separate excitement score, which is orthogonal to the assessment of the soundness of the paper. Excitement is subjective, and does not necessarily follow what is popular in the field.\n\n### Overall Recommendation Score\nThe Overall assessment score is an explicit recommendation for the outcome of this paper, if it were committed to an *ACL venue. This is a composite score reflecting your assessment of soundness, excitement, and also other factors like novelty and impact.\n\n## Review Form Criteria for Main vs Findings Papers\n\nThe main criteria for Findings are soundness and reproducibility. Conference recommendations may also consider novelty, impact and other factors.\n\nThe official review form and detailed guidelines are available at:\n- Reviewer Guidelines: aclrollingreview.org/reviewerguidelines\n- Review Form: aclrollingreview.org/reviewform"
    ],
    "durationSeconds": 6.515522266999997
  },
  "sourceToolAssistantUUID": "aac80498-dfc0-456b-90dc-943824faab78",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/.claude/sessions/review_reviewer_2_ab9762a8",
  "sessionId": "5bc9ff02-4cf0-48f5-9df4-52d4a45b7804",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-16T12:23:22.694Z_

<details><summary>↩ Tool result · `toolu_01VRA6Jixnrc5HRQRLJymr9g`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"summary\": {\"total_bib_entries\": 29, \"total_citations\": 44, \"unique_cited_keys\": 26, \"orphan_bib\": 3, \"missing_bib\": 0, \"duplicate_keys\": 0, \"online_verified\": 24, \"online_not_found\": 3, \"online_mismatch\": 2}, \"cross_check\": {\"orphan_bib\": [\"toolkengpt-2023\", \"tot-2023\", \"voyager-2023\"], \"missing_bib\": [], \"orphan_count\": 3, \"missing_count\": 0}, \"bib_entries\": [{\"key\": \"scienceworld-2022\", \"type\": \"inproceedings\", \"title\": \"ScienceWorld: Is Your Agent Smarter Than a 5th Grader?\", \"authors\": \"Wang, Ruoyao and Jansen, Peter and C\\\\^ot\\\\'e, Marc-Alexandre and Ammanabrolu, Pri...\", \"year\": \"2022\", \"venue\": \"Proceedings of the 2022 Conference on Empirical Methods in Natural Language Proc...\"}, {\"key\": \"react-2023\", \"type\": \"inproceedings\", \"title\": \"ReAct: Synergizing Reasoning and Acting in Language Models\", \"authors\": \"Yao, Shunyu and Zhao, Jeffrey and Yu, Dian and Du, Nan and Shafran, Izhak and Na...\", \"year\": \"2023\", \"venue\": \"International Conference on Learning Representations (ICLR)\"}, {\"key\": \"toolformer-2023\", \"type\": \"inproceedings\", \"title\": \"Toolformer: Language Models Can Teach Themselves to Use Tools\", \"authors\": \"Schick, Timo and Dwivedi-Yu, Jane and Dess\\\\`i, Roberto and Raileanu, Roberta and...\", \"year\": \"2023\", \"venue\": \"Advances in Neural Information Processing Systems (NeurIPS)\"}, {\"key\": \"art-2023\", \"type\": \"article\", \"title\": \"ART: Automatic Multi-step Reasoning and Tool-use for Large Language Models\", \"authors\": \"Paranjape, Bhargavi and Lundberg, Scott and Singh, Sameer and Hajishirzi, Hannan...\", \"year\": \"2023\", \"venue\": \"arXiv preprint arXiv:2303.09014\"}, {\"key\": \"chameleon-2023\", \"type\": \"inproceedings\", \"title\": \"Chameleon: Plug-and-Play Compositional Reasoning with Large Language Models\", \"authors\": \"Lu, Pan and Peng, Baolin and Cheng, Hao and Galley, Michel and Chang, Kai-Wei an...\", \"year\": \"2023\", \"venue\": \"Advances in Neural Information Processing Systems (NeurIPS)\"}, {\"key\": \"retool-2025\", \"type\": \"article\", \"title\": \"ReTool: Reinforcement Learning for Strategic Tool Use in LLMs\", \"authors\": \"Feng, Jiazhan and others\", \"year\": \"2025\", \"venue\": \"arXiv preprint arXiv:2504.11536\"}, {\"key\": \"cogrouter-2026\", \"type\": \"article\", \"title\": \"Think Fast and Slow: Step-Level Cognitive Depth Adaptation for LLM Agents\", \"authors\": \"Yang, Ruihan and others\", \"year\": \"2026\", \"venue\": \"arXiv preprint arXiv:2602.12662\"}, {\"key\": \"ares-2026\", \"type\": \"article\", \"title\": \"ARES: Adaptive Reasoning Effort Selection for Efficient LLM Agents\", \"authors\": \"Yang, Jingbo and others\", \"year\": \"2026\", \"venue\": \"arXiv preprint arXiv:2603.07915\"}, {\"key\": \"mixture-of-recursions-2025\", \"type\": \"inproceedings\", \"title\": \"Mixture-of-Recursions: Learning Dynamic Recursive Depths for Adaptive Token-Level Computation\", \"authors\": \"Bae, Sangmin and others\", \"year\": \"2025\", \"venue\": \"Advances in Neural Information Processing Systems (NeurIPS)\"}, {\"key\": \"mtrouter-2026\", \"type\": \"inproceedings\", \"title\": \"MTRouter: Cost-Aware Multi-Turn LLM Routing with History-Model Joint Embeddings\", \"authors\": \"Zhang, Yiqun and others\", \"year\": \"2026\", \"venue\": \"Proceedings of the Annual Meeting of the Association for Computational Linguisti...\"}, {\"key\": \"itp-2026\", \"type\": \"article\", \"title\": \"Imagine-then-Plan: Agent Learning from Adaptive Lookahead with World Models\", \"authors\": \"Liu, Youwei and others\", \"year\": \"2026\", \"venue\": \"arXiv preprint arXiv:2601.08955\"}, {\"key\": \"dynathink-2025\", \"type\": \"article\", \"title\": \"Dyna-Think: Synergizing Reasoning, Acting, and World Model Simulation in AI Agents\", \"authors\": \"Yu, Xiao and others\", \"year\": \"2025\", \"venue\": \"arXiv preprint arXiv:2506.00320\"}, {\"key\": \"tool-overuse-illusion-2026\", \"type\": \"article\", \"title\": \"The Tool-Overuse Illusion: Why Does LLM Prefer External Tools over Internal Knowledge?\", \"authors\": \"Zeng, Yirong and You, Shen and Liu, Yufei and Du, Qunyao and Ding, Xiao and Hou,...\", \"year\": \"2026\", \"venue\": \"arXiv preprint arXiv:2604.19749\"}, {\"key\": \"when2tool-2026\", \"type\": \"article\", \"title\": \"LLM Agents Already Know When to Call Tools -- Even Without Reasoning\", \"authors\": \"Sun, Chung-En and Liu, Linbo and Yan, Ge and Wang, Zimo and Weng, Tsui-Wei\", \"year\": \"2026\", \"venue\": \"arXiv preprint arXiv:2605.09252\"}, {\"key\": \"tool-use-tax-2026\", \"type\": \"article\", \"title\": \"Are Tools All We Need? Unveiling the Tool-Use Tax in LLM Agents\", \"authors\": \"Zhang, Kaituo and Xiong, Zhen and Zhong, Mingyu and Jiang, Zhimeng and Yuan, Zho...\", \"year\": \"2026\", \"venue\": \"arXiv preprint arXiv:2605.00136\"}, {\"key\": \"to-call-or-not-2026\", \"type\": \"article\", \"title\": \"To Call or Not to Call: A Framework to Assess and Optimize LLM Tool Calling\", \"authors\": \"Wu, Qinyuan and Das, Soumi and Amani, Mahsa and Nag, Arijit and Lee, Seungeon an...\", \"year\": \"2026\", \"venue\": \"arXiv preprint arXiv:2605.00737\"}, {\"key\": \"dagger-2011\", \"type\": \"inproceedings\", \"title\": \"A Reduction of Imitation Learning and Structured Prediction to No-Regret Online Learning\", \"authors\": \"Ross, St\\\\'ephane and Gordon, Geoffrey J and Bagnell, Drew\", \"year\": \"2011\", \"venue\": \"Proceedings of the International Conference on Artificial Intelligence and Stati...\"}, {\"key\": \"toolkengpt-2023\", \"type\": \"inproceedings\", \"title\": \"ToolkenGPT: Augmenting Frozen Language Models with Massive Tools via Tool Embeddings\", \"authors\": \"Hao, Shibo and Liu, Tianyang and Wang, Zhen and Hu, Zhiting\", \"year\": \"2023\", \"venue\": \"Advances in Neural Information Processing Systems (NeurIPS)\"}, {\"key\": \"alfworld-2021\", \"type\": \"inproceedings\", \"title\": \"ALFWorld: Aligning Text and Embodied Environments for Interactive Learning\", \"authors\": \"Shridhar, Mohit and Yuan, Xingdi and C\\\\^ot\\\\'e, Marc-Alexandre and Bisk, Yonatan ...\", \"year\": \"2021\", \"venue\": \"International Conference on Learning Representations (ICLR)\"}, {\"key\": \"garcia2015comprehensive\", \"type\": \"article\", \"title\": \"A Comprehensive Survey on Safe Reinforcement Learning\", \"authors\": \"Garc\\\\'ia, Javier and Fern\\\\'andez, Fernando\", \"year\": \"2015\", \"venue\": \"Journal of Machine Learning Research\"}, {\"key\": \"voyager-2023\", \"type\": \"article\", \"title\": \"Voyager: An Open-Ended Embodied Agent with Large Language Models\", \"authors\": \"Wang, Guanzhi and Xie, Yuqi and Jiang, Yunfan and Mandlekar, Ajay and Xiao, Chao...\", \"year\": \"2023\", \"venue\": \"arXiv preprint arXiv:2305.16291\"}, {\"key\": \"amitai2024explaining\", \"type\": \"inproceedings\", \"title\": \"Explaining Reinforcement Learning Agents through Counterfactual Action Outcomes\", \"authors\": \"Amitai, Yotam and Septon, Guy and Amir, Ofra\", \"year\": \"2024\", \"venue\": \"Proceedings of the AAAI Conference on Artificial Intelligence\"}, {\"key\": \"gajcin2023counterfactual\", \"type\": \"inproceedings\", \"title\": \"Counterfactual Explanations for Reinforcement Learning Agents\", \"authors\": \"Gajcin, Jasmina\", \"year\": \"2023\", \"venue\": \"Proceedings of the International Conference on Autonomous Agents and Multiagent ...\"}, {\"key\": \"olson2021counterfactual\", \"type\": \"article\", \"title\": \"Counterfactual State Explanations for Reinforcement Learning Agents via Generative Deep Learning\", \"authors\": \"Olson, Matthew L. and Khanna, Roli and Neal, Lawrence and Li, Fuxin and Wong, We...\", \"year\": \"2021\", \"venue\": \"Artificial Intelligence\"}, {\"key\": \"crpo-2021\", \"type\": \"inproceedings\", \"title\": \"CRPO: A New Approach for Safe Reinforcement Learning with Convergence Guarantee\", \"authors\": \"Xu, Tengyu and Liang, Yingbin and Lan, Guanghui\", \"year\": \"2021\", \"venue\": \"Proceedings of the 38th International Conference on Machine Learning (ICML)\"}, {\"key\": \"routellm-2024\", \"type\": \"article\", \"title\": \"RouteLLM: Learning to Route LLMs with Preference Data\", \"authors\": \"Ong, Isaac and Almahairi, Amjad and Wu, Vincent and Chiang, Wei-Lin and Wu, Tian...\", \"year\": \"2024\", \"venue\": \"arXiv preprint arXiv:2406.18665\"}, {\"key\": \"reflexion-2023\", \"type\": \"inproceedings\", \"title\": \"Reflexion: Language Agents with Verbal Reinforcement Learning\", \"authors\": \"Shinn, Noah and Cassano, Federico and Gopinath, Ashwin and Narasimhan, Karthik a...\", \"year\": \"2023\", \"venue\": \"Advances in Neural Information Processing Systems (NeurIPS)\"}, {\"key\": \"tool-learning-survey-2024\", \"type\": \"article\", \"title\": \"Tool Learning with Large Language Models: A Survey\", \"authors\": \"Qu, Changle and Dai, Sunhao and Wei, Xiaochi and Cai, Hengyi and Wang, Shuaiqian...\", \"year\": \"2024\", \"venue\": \"arXiv preprint arXiv:2405.17935\"}, {\"key\": \"tot-2023\", \"type\": \"inproceedings\", \"title\": \"Tree of Thoughts: Deliberate Problem Solving with Large Language Models\", \"authors\": \"Yao, Shunyu and Yu, Dian and Zhao, Jeffrey and Shafran, Izhak and Griffiths, Tho...\", \"year\": \"2023\", \"venue\": \"Advances in Neural Information Processing Systems (NeurIPS)\"}], \"tex_citations\": [{\"key\": \"scienceworld-2022\", \"file\": \"introduction.tex\", \"line\": 4, \"command\": \"cite\"}, {\"key\": \"toolformer-2023\", \"file\": \"introduction.tex\", \"line\": 7, \"command\": \"cite\"}, {\"key\": \"art-2023\", \"file\": \"introduction.tex\", \"line\": 7, \"command\": \"cite\"}, {\"key\": \"chameleon-2023\", \"file\": \"introduction.tex\", \"line\": 7, \"command\": \"cite\"}, {\"key\": \"cogrouter-2026\", \"file\": \"introduction.tex\", \"line\": 8, \"command\": \"cite\"}, {\"key\": \"ares-2026\", \"file\": \"introduction.tex\", \"line\": 8, \"command\": \"cite\"}, {\"key\": \"mtrouter-2026\", \"file\": \"introduction.tex\", \"line\": 8, \"command\": \"cite\"}, {\"key\": \"react-2023\", \"file\": \"introduction.tex\", \"line\": 20, \"command\": \"cite\"}, {\"key\": \"react-2023\", \"file\": \"method.tex\", \"line\": 11, \"command\": \"cite\"}, {\"key\": \"scienceworld-2022\", \"file\": \"method.tex\", \"line\": 22, \"command\": \"cite\"}, {\"key\": \"scienceworld-2022\", \"file\": \"method.tex\", \"line\": 37, \"command\": \"cite\"}, {\"key\": \"tool-learning-survey-2024\", \"file\": \"related_work.tex\", \"line\": 4, \"command\": \"citep\"}, {\"key\": \"toolformer-2023\", \"file\": \"related_work.tex\", \"line\": 5, \"command\": \"cite\"}, {\"key\": \"art-2023\", \"file\": \"related_work.tex\", \"line\": 5, \"command\": \"cite\"}, {\"key\": \"chameleon-2023\", \"file\": \"related_work.tex\", \"line\": 5, \"command\": \"cite\"}, {\"key\": \"retool-2025\", \"file\": \"related_work.tex\", \"line\": 5, \"command\": \"cite\"}, {\"key\": \"tool-overuse-illusion-2026\", \"file\": \"related_work.tex\", \"line\": 7, \"command\": \"citet\"}, {\"key\": \"when2tool-2026\", \"file\": \"related_work.tex\", \"line\": 7, \"command\": \"citet\"}, {\"key\": \"tool-use-tax-2026\", \"file\": \"related_work.tex\", \"line\": 7, \"command\": \"citet\"}, {\"key\": \"to-call-or-not-2026\", \"file\": \"related_work.tex\", \"line\": 7, \"command\": \"citet\"}, {\"key\": \"cogrouter-2026\", \"file\": \"related_work.tex\", \"line\": 11, \"command\": \"cite\"}, {\"key\": \"ares-2026\", \"file\": \"related_work.tex\", \"line\": 11, \"command\": \"cite\"}, {\"key\": \"mixture-of-recursions-2025\", \"file\": \"related_work.tex\", \"line\": 11, \"command\": \"cite\"}, {\"key\": \"mtrouter-2026\", \"file\": \"related_work.tex\", \"line\": 11, \"command\": \"cite\"}, {\"key\": \"routellm-2024\", \"file\": \"related_work.tex\", \"line\": 12, \"command\": \"citep\"}, {\"key\": \"olson2021counterfactual\", \"file\": \"related_work.tex\", \"line\": 16, \"command\": \"citep\"}, {\"key\": \"gajcin2023counterfactual\", \"file\": \"related_work.tex\", \"line\": 16, \"command\": \"citep\"}, {\"key\": \"amitai2024explaining\", \"file\": \"related_work.tex\", \"line\": 16, \"command\": \"citep\"}, {\"key\": \"garcia2015comprehensive\", \"file\": \"related_work.tex\", \"line\": 20, \"command\": \"citet\"}, {\"key\": \"crpo-2021\", \"file\": \"related_work.tex\", \"line\": 20, \"command\": \"citet\"}, {\"key\": \"scienceworld-2022\", \"file\": \"related_work.tex\", \"line\": 24, \"command\": \"cite\"}, {\"key\": \"alfworld-2021\", \"file\": \"related_work.tex\", \"line\": 24, \"command\": \"cite\"}, {\"key\": \"react-2023\", \"file\": \"related_work.tex\", \"line\": 25, \"command\": \"cite\"}, {\"key\": \"reflexion-2023\", \"file\": \"related_work.tex\", \"line\": 25, \"command\": \"cite\"}, {\"key\": \"itp-2026\", \"file\": \"related_work.tex\", \"line\": 26, \"command\": \"citep\"}, {\"key\": \"dynathink-2025\", \"file\": \"related_work.tex\", \"line\": 26, \"command\": \"citep\"}, {\"key\": \"garcia2015comprehensive\", \"file\": \"discussion.tex\", \"line\": 11, \"command\": \"citep\"}, {\"key\": \"cogrouter-2026\", \"file\": \"discussion.tex\", \"line\": 11, \"command\": \"citep\"}, {\"key\": \"ares-2026\", \"file\": \"discussion.tex\", \"line\": 11, \"command\": \"citep\"}, {\"key\": \"react-2023\", \"file\": \"main.tex\", \"line\": 35, \"command\": \"citep\"}, {\"key\": \"reflexion-2023\", \"file\": \"main.tex\", \"line\": 35, \"command\": \"citep\"}, {\"key\": \"dagger-2011\", \"file\": \"main.tex\", \"line\": 35, \"command\": \"citep\"}, {\"key\": \"scienceworld-2022\", \"file\": \"main.tex\", \"line\": 39, \"command\": \"cite\"}, {\"key\": \"alfworld-2021\", \"file\": \"main.tex\", \"line\": 292, \"command\": \"citep\"}], \"online_verification\": [{\"key\": \"scienceworld-2022\", \"title\": \"ScienceWorld: Is Your Agent Smarter Than a 5th Grader?\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"ScienceWorld: Is your Agent Smarter than a 5th Grader?\", \"matched_year\": \"2022\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"react-2023\", \"title\": \"ReAct: Synergizing Reasoning and Acting in Language Models\", \"status\": \"not_found\", \"confidence\": 0.45, \"matched_title\": \"Tree of Thoughts: Deliberate Problem Solving with Large Language Models\", \"matched_year\": \"\", \"mismatch_fields\": [], \"note\": \"best match similarity 0.45 below threshold 0.82\"}, {\"key\": \"toolformer-2023\", \"title\": \"Toolformer: Language Models Can Teach Themselves to Use Tools\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Toolformer: Language Models Can Teach Themselves to Use Tools\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"art-2023\", \"title\": \"ART: Automatic Multi-step Reasoning and Tool-use for Large Language Models\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"ART: Automatic multi-step reasoning and tool-use for large language models\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"chameleon-2023\", \"title\": \"Chameleon: Plug-and-Play Compositional Reasoning with Large Language Models\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Chameleon: Plug-and-Play Compositional Reasoning with Large Language Models\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"retool-2025\", \"title\": \"ReTool: Reinforcement Learning for Strategic Tool Use in LLMs\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"ReTool: Reinforcement Learning for Strategic Tool Use in LLMs\", \"matched_year\": \"2025\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"cogrouter-2026\", \"title\": \"Think Fast and Slow: Step-Level Cognitive Depth Adaptation for LLM Agents\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Think Fast and Slow: Step-Level Cognitive Depth Adaptation for LLM Agents\", \"matched_year\": \"2026\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"ares-2026\", \"title\": \"ARES: Adaptive Reasoning Effort Selection for Efficient LLM Agents\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Ares: Adaptive Reasoning Effort Selection for Efficient LLM Agents\", \"matched_year\": \"2026\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"mixture-of-recursions-2025\", \"title\": \"Mixture-of-Recursions: Learning Dynamic Recursive Depths for Adaptive Token-Level Computation\", \"status\": \"not_found\", \"confidence\": 0.327, \"matched_title\": \"Deep learning approaches to problems in speech recognition, computational chemistry, and natural language text processing\", \"matched_year\": \"\", \"mismatch_fields\": [], \"note\": \"best match similarity 0.33 below threshold 0.82\"}, {\"key\": \"mtrouter-2026\", \"title\": \"MTRouter: Cost-Aware Multi-Turn LLM Routing with History-Model Joint Embeddings\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"MTRouter: Cost-Aware Multi-Turn LLM Routing with History-Model Joint Embeddings\", \"matched_year\": \"2026\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"itp-2026\", \"title\": \"Imagine-then-Plan: Agent Learning from Adaptive Lookahead with World Models\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Imagine-then-Plan: Agent Learning from Adaptive Lookahead with World Models\", \"matched_year\": \"2026\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"dynathink-2025\", \"title\": \"Dyna-Think: Synergizing Reasoning, Acting, and World Model Simulation in AI Agents\", \"status\": \"mismatch\", \"confidence\": 1.0, \"matched_title\": \"Dyna-Think: Synergizing Reasoning, Acting, and World Model Simulation in AI Agents\", \"matched_year\": \"2025\", \"mismatch_fields\": [\"first_author: bib=yu vs api=xiao\"], \"note\": \"\"}, {\"key\": \"tool-overuse-illusion-2026\", \"title\": \"The Tool-Overuse Illusion: Why Does LLM Prefer External Tools over Internal Knowledge?\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"The Tool-Overuse Illusion: Why Does LLM Prefer External Tools over Internal Knowledge?\", \"matched_year\": \"2026\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"when2tool-2026\", \"title\": \"LLM Agents Already Know When to Call Tools -- Even Without Reasoning\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"LLM Agents Already Know When to Call Tools -- Even Without Reasoning\", \"matched_year\": \"2026\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"tool-use-tax-2026\", \"title\": \"Are Tools All We Need? Unveiling the Tool-Use Tax in LLM Agents\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Are Tools All We Need? Unveiling the Tool-Use Tax in LLM Agents\", \"matched_year\": \"2026\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"to-call-or-not-2026\", \"title\": \"To Call or Not to Call: A Framework to Assess and Optimize LLM Tool Calling\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"To Call or Not to Call: A Framework to Assess and Optimize LLM Tool Calling\", \"matched_year\": \"2026\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"dagger-2011\", \"title\": \"A Reduction of Imitation Learning and Structured Prediction to No-Regret Online Learning\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"A Reduction of Imitation Learning and Structured Prediction to No-Regret Online Learning\", \"matched_year\": \"2010\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"toolkengpt-2023\", \"title\": \"ToolkenGPT: Augmenting Frozen Language Models with Massive Tools via Tool Embeddings\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"ToolkenGPT: Augmenting Frozen Language Models with Massive Tools via Tool Embeddings\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"alfworld-2021\", \"title\": \"ALFWorld: Aligning Text and Embodied Environments for Interactive Learning\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"ALFWorld: Aligning Text and Embodied Environments for Interactive Learning\", \"matched_year\": \"2021\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"garcia2015comprehensive\", \"title\": \"A Comprehensive Survey on Safe Reinforcement Learning\", \"status\": \"mismatch\", \"confidence\": 1.0, \"matched_title\": \"A comprehensive survey on safe reinforcement learning\", \"matched_year\": \"2015\", \"mismatch_fields\": [\"first_author: bib=garc\\\\'ia vs api=garcía\"], \"note\": \"\"}, {\"key\": \"voyager-2023\", \"title\": \"Voyager: An Open-Ended Embodied Agent with Large Language Models\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Voyager: An Open-Ended Embodied Agent with Large Language Models\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"amitai2024explaining\", \"title\": \"Explaining Reinforcement Learning Agents through Counterfactual Action Outcomes\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Explaining Reinforcement Learning Agents through Counterfactual Action Outcomes\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"gajcin2023counterfactual\", \"title\": \"Counterfactual Explanations for Reinforcement Learning Agents\", \"status\": \"not_found\", \"confidence\": 0.777, \"matched_title\": \"Counterfactual state explanations for reinforcement learning agents via generative deep learning\", \"matched_year\": \"\", \"mismatch_fields\": [], \"note\": \"best match similarity 0.78 below threshold 0.82\"}, {\"key\": \"olson2021counterfactual\", \"title\": \"Counterfactual State Explanations for Reinforcement Learning Agents via Generative Deep Learning\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Counterfactual state explanations for reinforcement learning agents via generative deep learning\", \"matched_year\": \"2021\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"crpo-2021\", \"title\": \"CRPO: A New Approach for Safe Reinforcement Learning with Convergence Guarantee\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"CRPO: A New Approach for Safe Reinforcement Learning with Convergence Guarantee\", \"matched_year\": \"2020\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"routellm-2024\", \"title\": \"RouteLLM: Learning to Route LLMs with Preference Data\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"RouteLLM: Learning to Route LLMs with Preference Data\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"reflexion-2023\", \"title\": \"Reflexion: Language Agents with Verbal Reinforcement Learning\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Reflexion: Language Agents with Verbal Reinforcement Learning\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"tool-learning-survey-2024\", \"title\": \"Tool Learning with Large Language Models: A Survey\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Tool learning with large language models: a survey\", \"matched_year\": \"2025\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"tot-2023\", \"title\": \"Tree of Thoughts: Deliberate Problem Solving with Large Language Models\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Tree of Thoughts: Deliberate Problem Solving with Large Language Models\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}]}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "312bd8ba-a8f6-4efa-8668-182fbbce5f07",
  "isSidechain": false,
  "promptId": "2cc35627-090b-4e8e-873a-80e6ce7d766f",
  "type": "user",
  "uuid": "a6d50656-ab05-4fb3-87c0-ea18b91da937",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"summary\\\": {\\\"total_bib_entries\\\": 29, \\\"total_citations\\\": 44, \\\"unique_cited_keys\\\": 26, \\\"orphan_bib\\\": 3, \\\"missing_bib\\\": 0, \\\"duplicate_keys\\\": 0, \\\"online_verified\\\": 24, \\\"online_not_found\\\": 3, \\\"online_mismatch\\\": 2}, \\\"cross_check\\\": {\\\"orphan_bib\\\": [\\\"toolkengpt-2023\\\", \\\"tot-2023\\\", \\\"voyager-2023\\\"], \\\"missing_bib\\\": [], \\\"orphan_count\\\": 3, \\\"missing_count\\\": 0}, \\\"bib_entries\\\": [{\\\"key\\\": \\\"scienceworld-2022\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"ScienceWorld: Is Your Agent Smarter Than a 5th Grader?\\\", \\\"authors\\\": \\\"Wang, Ruoyao and Jansen, Peter and C\\\\\\\\^ot\\\\\\\\'e, Marc-Alexandre and Ammanabrolu, Pri...\\\", \\\"year\\\": \\\"2022\\\", \\\"venue\\\": \\\"Proceedings of the 2022 Conference on Empirical Methods in Natural Language Proc...\\\"}, {\\\"key\\\": \\\"react-2023\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"ReAct: Synergizing Reasoning and Acting in Language Models\\\", \\\"authors\\\": \\\"Yao, Shunyu and Zhao, Jeffrey and Yu, Dian and Du, Nan and Shafran, Izhak and Na...\\\", \\\"year\\\": \\\"2023\\\", \\\"venue\\\": \\\"International Conference on Learning Representations (ICLR)\\\"}, {\\\"key\\\": \\\"toolformer-2023\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Toolformer: Language Models Can Teach Themselves to Use Tools\\\", \\\"authors\\\": \\\"Schick, Timo and Dwivedi-Yu, Jane and Dess\\\\\\\\`i, Roberto and Raileanu, Roberta and...\\\", \\\"year\\\": \\\"2023\\\", \\\"venue\\\": \\\"Advances in Neural Information Processing Systems (NeurIPS)\\\"}, {\\\"key\\\": \\\"art-2023\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"ART: Automatic Multi-step Reasoning and Tool-use for Large Language Models\\\", \\\"authors\\\": \\\"Paranjape, Bhargavi and Lundberg, Scott and Singh, Sameer and Hajishirzi, Hannan...\\\", \\\"year\\\": \\\"2023\\\", \\\"venue\\\": \\\"arXiv preprint arXiv:2303.09014\\\"}, {\\\"key\\\": \\\"chameleon-2023\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Chameleon: Plug-and-Play Compositional Reasoning with Large Language Models\\\", \\\"authors\\\": \\\"Lu, Pan and Peng, Baolin and Cheng, Hao and Galley, Michel and Chang, Kai-Wei an...\\\", \\\"year\\\": \\\"2023\\\", \\\"venue\\\": \\\"Advances in Neural Information Processing Systems (NeurIPS)\\\"}, {\\\"key\\\": \\\"retool-2025\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"ReTool: Reinforcement Learning for Strategic Tool Use in LLMs\\\", \\\"authors\\\": \\\"Feng, Jiazhan and others\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"arXiv preprint arXiv:2504.11536\\\"}, {\\\"key\\\": \\\"cogrouter-2026\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Think Fast and Slow: Step-Level Cognitive Depth Adaptation for LLM Agents\\\", \\\"authors\\\": \\\"Yang, Ruihan and others\\\", \\\"year\\\": \\\"2026\\\", \\\"venue\\\": \\\"arXiv preprint arXiv:2602.12662\\\"}, {\\\"key\\\": \\\"ares-2026\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"ARES: Adaptive Reasoning Effort Selection for Efficient LLM Agents\\\", \\\"authors\\\": \\\"Yang, Jingbo and others\\\", \\\"year\\\": \\\"2026\\\", \\\"venue\\\": \\\"arXiv preprint arXiv:2603.07915\\\"}, {\\\"key\\\": \\\"mixture-of-recursions-2025\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Mixture-of-Recursions: Learning Dynamic Recursive Depths for Adaptive Token-Level Computation\\\", \\\"authors\\\": \\\"Bae, Sangmin and others\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"Advances in Neural Information Processing Systems (NeurIPS)\\\"}, {\\\"key\\\": \\\"mtrouter-2026\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"MTRouter: Cost-Aware Multi-Turn LLM Routing with History-Model Joint Embeddings\\\", \\\"authors\\\": \\\"Zhang, Yiqun and others\\\", \\\"year\\\": \\\"2026\\\", \\\"venue\\\": \\\"Proceedings of the Annual Meeting of the Association for Computational Linguisti...\\\"}, {\\\"key\\\": \\\"itp-2026\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Imagine-then-Plan: Agent Learning from Adaptive Lookahead with World Models\\\", \\\"authors\\\": \\\"Liu, Youwei and others\\\", \\\"year\\\": \\\"2026\\\", \\\"venue\\\": \\\"arXiv preprint arXiv:2601.08955\\\"}, {\\\"key\\\": \\\"dynathink-2025\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Dyna-Think: Synergizing Reasoning, Acting, and World Model Simulation in AI Agents\\\", \\\"authors\\\": \\\"Yu, Xiao and others\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"arXiv preprint arXiv:2506.00320\\\"}, {\\\"key\\\": \\\"tool-overuse-illusion-2026\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"The Tool-Overuse Illusion: Why Does LLM Prefer External Tools over Internal Knowledge?\\\", \\\"authors\\\": \\\"Zeng, Yirong and You, Shen and Liu, Yufei and Du, Qunyao and Ding, Xiao and Hou,...\\\", \\\"year\\\": \\\"2026\\\", \\\"venue\\\": \\\"arXiv preprint arXiv:2604.19749\\\"}, {\\\"key\\\": \\\"when2tool-2026\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"LLM Agents Already Know When to Call Tools -- Even Without Reasoning\\\", \\\"authors\\\": \\\"Sun, Chung-En and Liu, Linbo and Yan, Ge and Wang, Zimo and Weng, Tsui-Wei\\\", \\\"year\\\": \\\"2026\\\", \\\"venue\\\": \\\"arXiv preprint arXiv:2605.09252\\\"}, {\\\"key\\\": \\\"tool-use-tax-2026\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Are Tools All We Need? Unveiling the Tool-Use Tax in LLM Agents\\\", \\\"authors\\\": \\\"Zhang, Kaituo and Xiong, Zhen and Zhong, Mingyu and Jiang, Zhimeng and Yuan, Zho...\\\", \\\"year\\\": \\\"2026\\\", \\\"venue\\\": \\\"arXiv preprint arXiv:2605.00136\\\"}, {\\\"key\\\": \\\"to-call-or-not-2026\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"To Call or Not to Call: A Framework to Assess and Optimize LLM Tool Calling\\\", \\\"authors\\\": \\\"Wu, Qinyuan and Das, Soumi and Amani, Mahsa and Nag, Arijit and Lee, Seungeon an...\\\", \\\"year\\\": \\\"2026\\\", \\\"venue\\\": \\\"arXiv preprint arXiv:2605.00737\\\"}, {\\\"key\\\": \\\"dagger-2011\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"A Reduction of Imitation Learning and Structured Prediction to No-Regret Online Learning\\\", \\\"authors\\\": \\\"Ross, St\\\\\\\\'ephane and Gordon, Geoffrey J and Bagnell, Drew\\\", \\\"year\\\": \\\"2011\\\", \\\"venue\\\": \\\"Proceedings of the International Conference on Artificial Intelligence and Stati...\\\"}, {\\\"key\\\": \\\"toolkengpt-2023\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"ToolkenGPT: Augmenting Frozen Language Models with Massive Tools via Tool Embeddings\\\", \\\"authors\\\": \\\"Hao, Shibo and Liu, Tianyang and Wang, Zhen and Hu, Zhiting\\\", \\\"year\\\": \\\"2023\\\", \\\"venue\\\": \\\"Advances in Neural Information Processing Systems (NeurIPS)\\\"}, {\\\"key\\\": \\\"alfworld-2021\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"ALFWorld: Aligning Text and Embodied Environments for Interactive Learning\\\", \\\"authors\\\": \\\"Shridhar, Mohit and Yuan, Xingdi and C\\\\\\\\^ot\\\\\\\\'e, Marc-Alexandre and Bisk, Yonatan ...\\\", \\\"year\\\": \\\"2021\\\", \\\"venue\\\": \\\"International Conference on Learning Representations (ICLR)\\\"}, {\\\"key\\\": \\\"garcia2015comprehensive\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"A Comprehensive Survey on Safe Reinforcement Learning\\\", \\\"authors\\\": \\\"Garc\\\\\\\\'ia, Javier and Fern\\\\\\\\'andez, Fernando\\\", \\\"year\\\": \\\"2015\\\", \\\"venue\\\": \\\"Journal of Machine Learning Research\\\"}, {\\\"key\\\": \\\"voyager-2023\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Voyager: An Open-Ended Embodied Agent with Large Language Models\\\", \\\"authors\\\": \\\"Wang, Guanzhi and Xie, Yuqi and Jiang, Yunfan and Mandlekar, Ajay and Xiao, Chao...\\\", \\\"year\\\": \\\"2023\\\", \\\"venue\\\": \\\"arXiv preprint arXiv:2305.16291\\\"}, {\\\"key\\\": \\\"amitai2024explaining\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Explaining Reinforcement Learning Agents through Counterfactual Action Outcomes\\\", \\\"authors\\\": \\\"Amitai, Yotam and Septon, Guy and Amir, Ofra\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"Proceedings of the AAAI Conference on Artificial Intelligence\\\"}, {\\\"key\\\": \\\"gajcin2023counterfactual\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Counterfactual Explanations for Reinforcement Learning Agents\\\", \\\"authors\\\": \\\"Gajcin, Jasmina\\\", \\\"year\\\": \\\"2023\\\", \\\"venue\\\": \\\"Proceedings of the International Conference on Autonomous Agents and Multiagent ...\\\"}, {\\\"key\\\": \\\"olson2021counterfactual\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Counterfactual State Explanations for Reinforcement Learning Agents via Generative Deep Learning\\\", \\\"authors\\\": \\\"Olson, Matthew L. and Khanna, Roli and Neal, Lawrence and Li, Fuxin and Wong, We...\\\", \\\"year\\\": \\\"2021\\\", \\\"venue\\\": \\\"Artificial Intelligence\\\"}, {\\\"key\\\": \\\"crpo-2021\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"CRPO: A New Approach for Safe Reinforcement Learning with Convergence Guarantee\\\", \\\"authors\\\": \\\"Xu, Tengyu and Liang, Yingbin and Lan, Guanghui\\\", \\\"year\\\": \\\"2021\\\", \\\"venue\\\": \\\"Proceedings of the 38th International Conference on Machine Learning (ICML)\\\"}, {\\\"key\\\": \\\"routellm-2024\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"RouteLLM: Learning to Route LLMs with Preference Data\\\", \\\"authors\\\": \\\"Ong, Isaac and Almahairi, Amjad and Wu, Vincent and Chiang, Wei-Lin and Wu, Tian...\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"arXiv preprint arXiv:2406.18665\\\"}, {\\\"key\\\": \\\"reflexion-2023\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Reflexion: Language Agents with Verbal Reinforcement Learning\\\", \\\"authors\\\": \\\"Shinn, Noah and Cassano, Federico and Gopinath, Ashwin and Narasimhan, Karthik a...\\\", \\\"year\\\": \\\"2023\\\", \\\"venue\\\": \\\"Advances in Neural Information Processing Systems (NeurIPS)\\\"}, {\\\"key\\\": \\\"tool-learning-survey-2024\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Tool Learning with Large Language Models: A Survey\\\", \\\"authors\\\": \\\"Qu, Changle and Dai, Sunhao and Wei, Xiaochi and Cai, Hengyi and Wang, Shuaiqian...\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"arXiv preprint arXiv:2405.17935\\\"}, {\\\"key\\\": \\\"tot-2023\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Tree of Thoughts: Deliberate Problem Solving with Large Language Models\\\", \\\"authors\\\": \\\"Yao, Shunyu and Yu, Dian and Zhao, Jeffrey and Shafran, Izhak and Griffiths, Tho...\\\", \\\"year\\\": \\\"2023\\\", \\\"venue\\\": \\\"Advances in Neural Information Processing Systems (NeurIPS)\\\"}], \\\"tex_citations\\\": [{\\\"key\\\": \\\"scienceworld-2022\\\", \\\"file\\\": \\\"introduction.tex\\\", \\\"line\\\": 4, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"toolformer-2023\\\", \\\"file\\\": \\\"introduction.tex\\\", \\\"line\\\": 7, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"art-2023\\\", \\\"file\\\": \\\"introduction.tex\\\", \\\"line\\\": 7, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"chameleon-2023\\\", \\\"file\\\": \\\"introduction.tex\\\", \\\"line\\\": 7, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"cogrouter-2026\\\", \\\"file\\\": \\\"introduction.tex\\\", \\\"line\\\": 8, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"ares-2026\\\", \\\"file\\\": \\\"introduction.tex\\\", \\\"line\\\": 8, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"mtrouter-2026\\\", \\\"file\\\": \\\"introduction.tex\\\", \\\"line\\\": 8, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"react-2023\\\", \\\"file\\\": \\\"introduction.tex\\\", \\\"line\\\": 20, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"react-2023\\\", \\\"file\\\": \\\"method.tex\\\", \\\"line\\\": 11, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"scienceworld-2022\\\", \\\"file\\\": \\\"method.tex\\\", \\\"line\\\": 22, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"scienceworld-2022\\\", \\\"file\\\": \\\"method.tex\\\", \\\"line\\\": 37, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"tool-learning-survey-2024\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 4, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"toolformer-2023\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 5, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"art-2023\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 5, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"chameleon-2023\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 5, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"retool-2025\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 5, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"tool-overuse-illusion-2026\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 7, \\\"command\\\": \\\"citet\\\"}, {\\\"key\\\": \\\"when2tool-2026\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 7, \\\"command\\\": \\\"citet\\\"}, {\\\"key\\\": \\\"tool-use-tax-2026\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 7, \\\"command\\\": \\\"citet\\\"}, {\\\"key\\\": \\\"to-call-or-not-2026\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 7, \\\"command\\\": \\\"citet\\\"}, {\\\"key\\\": \\\"cogrouter-2026\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 11, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"ares-2026\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 11, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"mixture-of-recursions-2025\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 11, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"mtrouter-2026\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 11, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"routellm-2024\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 12, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"olson2021counterfactual\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 16, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"gajcin2023counterfactual\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 16, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"amitai2024explaining\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 16, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"garcia2015comprehensive\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 20, \\\"command\\\": \\\"citet\\\"}, {\\\"key\\\": \\\"crpo-2021\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 20, \\\"command\\\": \\\"citet\\\"}, {\\\"key\\\": \\\"scienceworld-2022\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 24, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"alfworld-2021\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 24, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"react-2023\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 25, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"reflexion-2023\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 25, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"itp-2026\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 26, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"dynathink-2025\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 26, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"garcia2015comprehensive\\\", \\\"file\\\": \\\"discussion.tex\\\", \\\"line\\\": 11, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"cogrouter-2026\\\", \\\"file\\\": \\\"discussion.tex\\\", \\\"line\\\": 11, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"ares-2026\\\", \\\"file\\\": \\\"discussion.tex\\\", \\\"line\\\": 11, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"react-2023\\\", \\\"file\\\": \\\"main.tex\\\", \\\"line\\\": 35, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"reflexion-2023\\\", \\\"file\\\": \\\"main.tex\\\", \\\"line\\\": 35, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"dagger-2011\\\", \\\"file\\\": \\\"main.tex\\\", \\\"line\\\": 35, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"scienceworld-2022\\\", \\\"file\\\": \\\"main.tex\\\", \\\"line\\\": 39, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"alfworld-2021\\\", \\\"file\\\": \\\"main.tex\\\", \\\"line\\\": 292, \\\"command\\\": \\\"citep\\\"}], \\\"online_verification\\\": [{\\\"key\\\": \\\"scienceworld-2022\\\", \\\"title\\\": \\\"ScienceWorld: Is Your Agent Smarter Than a 5th Grader?\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"ScienceWorld: Is your Agent Smarter than a 5th Grader?\\\", \\\"matched_year\\\": \\\"2022\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"react-2023\\\", \\\"title\\\": \\\"ReAct: Synergizing Reasoning and Acting in Language Models\\\", \\\"status\\\": \\\"not_found\\\", \\\"confidence\\\": 0.45, \\\"matched_title\\\": \\\"Tree of Thoughts: Deliberate Problem Solving with Large Language Models\\\", \\\"matched_year\\\": \\\"\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"best match similarity 0.45 below threshold 0.82\\\"}, {\\\"key\\\": \\\"toolformer-2023\\\", \\\"title\\\": \\\"Toolformer: Language Models Can Teach Themselves to Use Tools\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Toolformer: Language Models Can Teach Themselves to Use Tools\\\", \\\"matched_year\\\": \\\"2023\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"art-2023\\\", \\\"title\\\": \\\"ART: Automatic Multi-step Reasoning and Tool-use for Large Language Models\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"ART: Automatic multi-step reasoning and tool-use for large language models\\\", \\\"matched_year\\\": \\\"2023\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"chameleon-2023\\\", \\\"title\\\": \\\"Chameleon: Plug-and-Play Compositional Reasoning with Large Language Models\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Chameleon: Plug-and-Play Compositional Reasoning with Large Language Models\\\", \\\"matched_year\\\": \\\"2023\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"retool-2025\\\", \\\"title\\\": \\\"ReTool: Reinforcement Learning for Strategic Tool Use in LLMs\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"ReTool: Reinforcement Learning for Strategic Tool Use in LLMs\\\", \\\"matched_year\\\": \\\"2025\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"cogrouter-2026\\\", \\\"title\\\": \\\"Think Fast and Slow: Step-Level Cognitive Depth Adaptation for LLM Agents\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Think Fast and Slow: Step-Level Cognitive Depth Adaptation for LLM Agents\\\", \\\"matched_year\\\": \\\"2026\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"ares-2026\\\", \\\"title\\\": \\\"ARES: Adaptive Reasoning Effort Selection for Efficient LLM Agents\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Ares: Adaptive Reasoning Effort Selection for Efficient LLM Agents\\\", \\\"matched_year\\\": \\\"2026\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"mixture-of-recursions-2025\\\", \\\"title\\\": \\\"Mixture-of-Recursions: Learning Dynamic Recursive Depths for Adaptive Token-Level Computation\\\", \\\"status\\\": \\\"not_found\\\", \\\"confidence\\\": 0.327, \\\"matched_title\\\": \\\"Deep learning approaches to problems in speech recognition, computational chemistry, and natural language text processing\\\", \\\"matched_year\\\": \\\"\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"best match similarity 0.33 below threshold 0.82\\\"}, {\\\"key\\\": \\\"mtrouter-2026\\\", \\\"title\\\": \\\"MTRouter: Cost-Aware Multi-Turn LLM Routing with History-Model Joint Embeddings\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"MTRouter: Cost-Aware Multi-Turn LLM Routing with History-Model Joint Embeddings\\\", \\\"matched_year\\\": \\\"2026\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"itp-2026\\\", \\\"title\\\": \\\"Imagine-then-Plan: Agent Learning from Adaptive Lookahead with World Models\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Imagine-then-Plan: Agent Learning from Adaptive Lookahead with World Models\\\", \\\"matched_year\\\": \\\"2026\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"dynathink-2025\\\", \\\"title\\\": \\\"Dyna-Think: Synergizing Reasoning, Acting, and World Model Simulation in AI Agents\\\", \\\"status\\\": \\\"mismatch\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Dyna-Think: Synergizing Reasoning, Acting, and World Model Simulation in AI Agents\\\", \\\"matched_year\\\": \\\"2025\\\", \\\"mismatch_fields\\\": [\\\"first_author: bib=yu vs api=xiao\\\"], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"tool-overuse-illusion-2026\\\", \\\"title\\\": \\\"The Tool-Overuse Illusion: Why Does LLM Prefer External Tools over Internal Knowledge?\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"The Tool-Overuse Illusion: Why Does LLM Prefer External Tools over Internal Knowledge?\\\", \\\"matched_year\\\": \\\"2026\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"when2tool-2026\\\", \\\"title\\\": \\\"LLM Agents Already Know When to Call Tools -- Even Without Reasoning\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"LLM Agents Already Know When to Call Tools -- Even Without Reasoning\\\", \\\"matched_year\\\": \\\"2026\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"tool-use-tax-2026\\\", \\\"title\\\": \\\"Are Tools All We Need? Unveiling the Tool-Use Tax in LLM Agents\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Are Tools All We Need? Unveiling the Tool-Use Tax in LLM Agents\\\", \\\"matched_year\\\": \\\"2026\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"to-call-or-not-2026\\\", \\\"title\\\": \\\"To Call or Not to Call: A Framework to Assess and Optimize LLM Tool Calling\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"To Call or Not to Call: A Framework to Assess and Optimize LLM Tool Calling\\\", \\\"matched_year\\\": \\\"2026\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"dagger-2011\\\", \\\"title\\\": \\\"A Reduction of Imitation Learning and Structured Prediction to No-Regret Online Learning\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"A Reduction of Imitation Learning and Structured Prediction to No-Regret Online Learning\\\", \\\"matched_year\\\": \\\"2010\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"toolkengpt-2023\\\", \\\"title\\\": \\\"ToolkenGPT: Augmenting Frozen Language Models with Massive Tools via Tool Embeddings\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"ToolkenGPT: Augmenting Frozen Language Models with Massive Tools via Tool Embeddings\\\", \\\"matched_year\\\": \\\"2023\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"alfworld-2021\\\", \\\"title\\\": \\\"ALFWorld: Aligning Text and Embodied Environments for Interactive Learning\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"ALFWorld: Aligning Text and Embodied Environments for Interactive Learning\\\", \\\"matched_year\\\": \\\"2021\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"garcia2015comprehensive\\\", \\\"title\\\": \\\"A Comprehensive Survey on Safe Reinforcement Learning\\\", \\\"status\\\": \\\"mismatch\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"A comprehensive survey on safe reinforcement learning\\\", \\\"matched_year\\\": \\\"2015\\\", \\\"mismatch_fields\\\": [\\\"first_author: bib=garc\\\\\\\\'ia vs api=garcía\\\"], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"voyager-2023\\\", \\\"title\\\": \\\"Voyager: An Open-Ended Embodied Agent with Large Language Models\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Voyager: An Open-Ended Embodied Agent with Large Language Models\\\", \\\"matched_year\\\": \\\"2023\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"amitai2024explaining\\\", \\\"title\\\": \\\"Explaining Reinforcement Learning Agents through Counterfactual Action Outcomes\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Explaining Reinforcement Learning Agents through Counterfactual Action Outcomes\\\", \\\"matched_year\\\": \\\"2024\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"gajcin2023counterfactual\\\", \\\"title\\\": \\\"Counterfactual Explanations for Reinforcement Learning Agents\\\", \\\"status\\\": \\\"not_found\\\", \\\"confidence\\\": 0.777, \\\"matched_title\\\": \\\"Counterfactual state explanations for reinforcement learning agents via generative deep learning\\\", \\\"matched_year\\\": \\\"\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"best match similarity 0.78 below threshold 0.82\\\"}, {\\\"key\\\": \\\"olson2021counterfactual\\\", \\\"title\\\": \\\"Counterfactual State Explanations for Reinforcement Learning Agents via Generative Deep Learning\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Counterfactual state explanations for reinforcement learning agents via generative deep learning\\\", \\\"matched_year\\\": \\\"2021\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"crpo-2021\\\", \\\"title\\\": \\\"CRPO: A New Approach for Safe Reinforcement Learning with Convergence Guarantee\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"CRPO: A New Approach for Safe Reinforcement Learning with Convergence Guarantee\\\", \\\"matched_year\\\": \\\"2020\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"routellm-2024\\\", \\\"title\\\": \\\"RouteLLM: Learning to Route LLMs with Preference Data\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"RouteLLM: Learning to Route LLMs with Preference Data\\\", \\\"matched_year\\\": \\\"2024\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"reflexion-2023\\\", \\\"title\\\": \\\"Reflexion: Language Agents with Verbal Reinforcement Learning\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Reflexion: Language Agents with Verbal Reinforcement Learning\\\", \\\"matched_year\\\": \\\"2023\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"tool-learning-survey-2024\\\", \\\"title\\\": \\\"Tool Learning with Large Language Models: A Survey\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Tool learning with large language models: a survey\\\", \\\"matched_year\\\": \\\"2025\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"tot-2023\\\", \\\"title\\\": \\\"Tree of Thoughts: Deliberate Problem Solving with Large Language Models\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Tree of Thoughts: Deliberate Problem Solving with Large Language Models\\\", \\\"matched_year\\\": \\\"2023\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}]}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"summary\": {\"total_bib_entries\": 29, \"total_citations\": 44, \"unique_cited_keys\": 26, \"orphan_bib\": 3, \"missing_bib\": 0, \"duplicate_keys\": 0, \"online_verified\": 24, \"online_not_found\": 3, \"online_mismatch\": 2}, \"cross_check\": {\"orphan_bib\": [\"toolkengpt-2023\", \"tot-2023\", \"voyager-2023\"], \"missing_bib\": [], \"orphan_count\": 3, \"missing_count\": 0}, \"bib_entries\": [{\"key\": \"scienceworld-2022\", \"type\": \"inproceedings\", \"title\": \"ScienceWorld: Is Your Agent Smarter Than a 5th Grader?\", \"authors\": \"Wang, Ruoyao and Jansen, Peter and C\\\\^ot\\\\'e, Marc-Alexandre and Ammanabrolu, Pri...\", \"year\": \"2022\", \"venue\": \"Proceedings of the 2022 Conference on Empirical Methods in Natural Language Proc...\"}, {\"key\": \"react-2023\", \"type\": \"inproceedings\", \"title\": \"ReAct: Synergizing Reasoning and Acting in Language Models\", \"authors\": \"Yao, Shunyu and Zhao, Jeffrey and Yu, Dian and Du, Nan and Shafran, Izhak and Na...\", \"year\": \"2023\", \"venue\": \"International Conference on Learning Representations (ICLR)\"}, {\"key\": \"toolformer-2023\", \"type\": \"inproceedings\", \"title\": \"Toolformer: Language Models Can Teach Themselves to Use Tools\", \"authors\": \"Schick, Timo and Dwivedi-Yu, Jane and Dess\\\\`i, Roberto and Raileanu, Roberta and...\", \"year\": \"2023\", \"venue\": \"Advances in Neural Information Processing Systems (NeurIPS)\"}, {\"key\": \"art-2023\", \"type\": \"article\", \"title\": \"ART: Automatic Multi-step Reasoning and Tool-use for Large Language Models\", \"authors\": \"Paranjape, Bhargavi and Lundberg, Scott and Singh, Sameer and Hajishirzi, Hannan...\", \"year\": \"2023\", \"venue\": \"arXiv preprint arXiv:2303.09014\"}, {\"key\": \"chameleon-2023\", \"type\": \"inproceedings\", \"title\": \"Chameleon: Plug-and-Play Compositional Reasoning with Large Language Models\", \"authors\": \"Lu, Pan and Peng, Baolin and Cheng, Hao and Galley, Michel and Chang, Kai-Wei an...\", \"year\": \"2023\", \"venue\": \"Advances in Neural Information Processing Systems (NeurIPS)\"}, {\"key\": \"retool-2025\", \"type\": \"article\", \"title\": \"ReTool: Reinforcement Learning for Strategic Tool Use in LLMs\", \"authors\": \"Feng, Jiazhan and others\", \"year\": \"2025\", \"venue\": \"arXiv preprint arXiv:2504.11536\"}, {\"key\": \"cogrouter-2026\", \"type\": \"article\", \"title\": \"Think Fast and Slow: Step-Level Cognitive Depth Adaptation for LLM Agents\", \"authors\": \"Yang, Ruihan and others\", \"year\": \"2026\", \"venue\": \"arXiv preprint arXiv:2602.12662\"}, {\"key\": \"ares-2026\", \"type\": \"article\", \"title\": \"ARES: Adaptive Reasoning Effort Selection for Efficient LLM Agents\", \"authors\": \"Yang, Jingbo and others\", \"year\": \"2026\", \"venue\": \"arXiv preprint arXiv:2603.07915\"}, {\"key\": \"mixture-of-recursions-2025\", \"type\": \"inproceedings\", \"title\": \"Mixture-of-Recursions: Learning Dynamic Recursive Depths for Adaptive Token-Level Computation\", \"authors\": \"Bae, Sangmin and others\", \"year\": \"2025\", \"venue\": \"Advances in Neural Information Processing Systems (NeurIPS)\"}, {\"key\": \"mtrouter-2026\", \"type\": \"inproceedings\", \"title\": \"MTRouter: Cost-Aware Multi-Turn LLM Routing with History-Model Joint Embeddings\", \"authors\": \"Zhang, Yiqun and others\", \"year\": \"2026\", \"venue\": \"Proceedings of the Annual Meeting of the Association for Computational Linguisti...\"}, {\"key\": \"itp-2026\", \"type\": \"article\", \"title\": \"Imagine-then-Plan: Agent Learning from Adaptive Lookahead with World Models\", \"authors\": \"Liu, Youwei and others\", \"year\": \"2026\", \"venue\": \"arXiv preprint arXiv:2601.08955\"}, {\"key\": \"dynathink-2025\", \"type\": \"article\", \"title\": \"Dyna-Think: Synergizing Reasoning, Acting, and World Model Simulation in AI Agents\", \"authors\": \"Yu, Xiao and others\", \"year\": \"2025\", \"venue\": \"arXiv preprint arXiv:2506.00320\"}, {\"key\": \"tool-overuse-illusion-2026\", \"type\": \"article\", \"title\": \"The Tool-Overuse Illusion: Why Does LLM Prefer External Tools over Internal Knowledge?\", \"authors\": \"Zeng, Yirong and You, Shen and Liu, Yufei and Du, Qunyao and Ding, Xiao and Hou,...\", \"year\": \"2026\", \"venue\": \"arXiv preprint arXiv:2604.19749\"}, {\"key\": \"when2tool-2026\", \"type\": \"article\", \"title\": \"LLM Agents Already Know When to Call Tools -- Even Without Reasoning\", \"authors\": \"Sun, Chung-En and Liu, Linbo and Yan, Ge and Wang, Zimo and Weng, Tsui-Wei\", \"year\": \"2026\", \"venue\": \"arXiv preprint arXiv:2605.09252\"}, {\"key\": \"tool-use-tax-2026\", \"type\": \"article\", \"title\": \"Are Tools All We Need? Unveiling the Tool-Use Tax in LLM Agents\", \"authors\": \"Zhang, Kaituo and Xiong, Zhen and Zhong, Mingyu and Jiang, Zhimeng and Yuan, Zho...\", \"year\": \"2026\", \"venue\": \"arXiv preprint arXiv:2605.00136\"}, {\"key\": \"to-call-or-not-2026\", \"type\": \"article\", \"title\": \"To Call or Not to Call: A Framework to Assess and Optimize LLM Tool Calling\", \"authors\": \"Wu, Qinyuan and Das, Soumi and Amani, Mahsa and Nag, Arijit and Lee, Seungeon an...\", \"year\": \"2026\", \"venue\": \"arXiv preprint arXiv:2605.00737\"}, {\"key\": \"dagger-2011\", \"type\": \"inproceedings\", \"title\": \"A Reduction of Imitation Learning and Structured Prediction to No-Regret Online Learning\", \"authors\": \"Ross, St\\\\'ephane and Gordon, Geoffrey J and Bagnell, Drew\", \"year\": \"2011\", \"venue\": \"Proceedings of the International Conference on Artificial Intelligence and Stati...\"}, {\"key\": \"toolkengpt-2023\", \"type\": \"inproceedings\", \"title\": \"ToolkenGPT: Augmenting Frozen Language Models with Massive Tools via Tool Embeddings\", \"authors\": \"Hao, Shibo and Liu, Tianyang and Wang, Zhen and Hu, Zhiting\", \"year\": \"2023\", \"venue\": \"Advances in Neural Information Processing Systems (NeurIPS)\"}, {\"key\": \"alfworld-2021\", \"type\": \"inproceedings\", \"title\": \"ALFWorld: Aligning Text and Embodied Environments for Interactive Learning\", \"authors\": \"Shridhar, Mohit and Yuan, Xingdi and C\\\\^ot\\\\'e, Marc-Alexandre and Bisk, Yonatan ...\", \"year\": \"2021\", \"venue\": \"International Conference on Learning Representations (ICLR)\"}, {\"key\": \"garcia2015comprehensive\", \"type\": \"article\", \"title\": \"A Comprehensive Survey on Safe Reinforcement Learning\", \"authors\": \"Garc\\\\'ia, Javier and Fern\\\\'andez, Fernando\", \"year\": \"2015\", \"venue\": \"Journal of Machine Learning Research\"}, {\"key\": \"voyager-2023\", \"type\": \"article\", \"title\": \"Voyager: An Open-Ended Embodied Agent with Large Language Models\", \"authors\": \"Wang, Guanzhi and Xie, Yuqi and Jiang, Yunfan and Mandlekar, Ajay and Xiao, Chao...\", \"year\": \"2023\", \"venue\": \"arXiv preprint arXiv:2305.16291\"}, {\"key\": \"amitai2024explaining\", \"type\": \"inproceedings\", \"title\": \"Explaining Reinforcement Learning Agents through Counterfactual Action Outcomes\", \"authors\": \"Amitai, Yotam and Septon, Guy and Amir, Ofra\", \"year\": \"2024\", \"venue\": \"Proceedings of the AAAI Conference on Artificial Intelligence\"}, {\"key\": \"gajcin2023counterfactual\", \"type\": \"inproceedings\", \"title\": \"Counterfactual Explanations for Reinforcement Learning Agents\", \"authors\": \"Gajcin, Jasmina\", \"year\": \"2023\", \"venue\": \"Proceedings of the International Conference on Autonomous Agents and Multiagent ...\"}, {\"key\": \"olson2021counterfactual\", \"type\": \"article\", \"title\": \"Counterfactual State Explanations for Reinforcement Learning Agents via Generative Deep Learning\", \"authors\": \"Olson, Matthew L. and Khanna, Roli and Neal, Lawrence and Li, Fuxin and Wong, We...\", \"year\": \"2021\", \"venue\": \"Artificial Intelligence\"}, {\"key\": \"crpo-2021\", \"type\": \"inproceedings\", \"title\": \"CRPO: A New Approach for Safe Reinforcement Learning with Convergence Guarantee\", \"authors\": \"Xu, Tengyu and Liang, Yingbin and Lan, Guanghui\", \"year\": \"2021\", \"venue\": \"Proceedings of the 38th International Conference on Machine Learning (ICML)\"}, {\"key\": \"routellm-2024\", \"type\": \"article\", \"title\": \"RouteLLM: Learning to Route LLMs with Preference Data\", \"authors\": \"Ong, Isaac and Almahairi, Amjad and Wu, Vincent and Chiang, Wei-Lin and Wu, Tian...\", \"year\": \"2024\", \"venue\": \"arXiv preprint arXiv:2406.18665\"}, {\"key\": \"reflexion-2023\", \"type\": \"inproceedings\", \"title\": \"Reflexion: Language Agents with Verbal Reinforcement Learning\", \"authors\": \"Shinn, Noah and Cassano, Federico and Gopinath, Ashwin and Narasimhan, Karthik a...\", \"year\": \"2023\", \"venue\": \"Advances in Neural Information Processing Systems (NeurIPS)\"}, {\"key\": \"tool-learning-survey-2024\", \"type\": \"article\", \"title\": \"Tool Learning with Large Language Models: A Survey\", \"authors\": \"Qu, Changle and Dai, Sunhao and Wei, Xiaochi and Cai, Hengyi and Wang, Shuaiqian...\", \"year\": \"2024\", \"venue\": \"arXiv preprint arXiv:2405.17935\"}, {\"key\": \"tot-2023\", \"type\": \"inproceedings\", \"title\": \"Tree of Thoughts: Deliberate Problem Solving with Large Language Models\", \"authors\": \"Yao, Shunyu and Yu, Dian and Zhao, Jeffrey and Shafran, Izhak and Griffiths, Tho...\", \"year\": \"2023\", \"venue\": \"Advances in Neural Information Processing Systems (NeurIPS)\"}], \"tex_citations\": [{\"key\": \"scienceworld-2022\", \"file\": \"introduction.tex\", \"line\": 4, \"command\": \"cite\"}, {\"key\": \"toolformer-2023\", \"file\": \"introduction.tex\", \"line\": 7, \"command\": \"cite\"}, {\"key\": \"art-2023\", \"file\": \"introduction.tex\", \"line\": 7, \"command\": \"cite\"}, {\"key\": \"chameleon-2023\", \"file\": \"introduction.tex\", \"line\": 7, \"command\": \"cite\"}, {\"key\": \"cogrouter-2026\", \"file\": \"introduction.tex\", \"line\": 8, \"command\": \"cite\"}, {\"key\": \"ares-2026\", \"file\": \"introduction.tex\", \"line\": 8, \"command\": \"cite\"}, {\"key\": \"mtrouter-2026\", \"file\": \"introduction.tex\", \"line\": 8, \"command\": \"cite\"}, {\"key\": \"react-2023\", \"file\": \"introduction.tex\", \"line\": 20, \"command\": \"cite\"}, {\"key\": \"react-2023\", \"file\": \"method.tex\", \"line\": 11, \"command\": \"cite\"}, {\"key\": \"scienceworld-2022\", \"file\": \"method.tex\", \"line\": 22, \"command\": \"cite\"}, {\"key\": \"scienceworld-2022\", \"file\": \"method.tex\", \"line\": 37, \"command\": \"cite\"}, {\"key\": \"tool-learning-survey-2024\", \"file\": \"related_work.tex\", \"line\": 4, \"command\": \"citep\"}, {\"key\": \"toolformer-2023\", \"file\": \"related_work.tex\", \"line\": 5, \"command\": \"cite\"}, {\"key\": \"art-2023\", \"file\": \"related_work.tex\", \"line\": 5, \"command\": \"cite\"}, {\"key\": \"chameleon-2023\", \"file\": \"related_work.tex\", \"line\": 5, \"command\": \"cite\"}, {\"key\": \"retool-2025\", \"file\": \"related_work.tex\", \"line\": 5, \"command\": \"cite\"}, {\"key\": \"tool-overuse-illusion-2026\", \"file\": \"related_work.tex\", \"line\": 7, \"command\": \"citet\"}, {\"key\": \"when2tool-2026\", \"file\": \"related_work.tex\", \"line\": 7, \"command\": \"citet\"}, {\"key\": \"tool-use-tax-2026\", \"file\": \"related_work.tex\", \"line\": 7, \"command\": \"citet\"}, {\"key\": \"to-call-or-not-2026\", \"file\": \"related_work.tex\", \"line\": 7, \"command\": \"citet\"}, {\"key\": \"cogrouter-2026\", \"file\": \"related_work.tex\", \"line\": 11, \"command\": \"cite\"}, {\"key\": \"ares-2026\", \"file\": \"related_work.tex\", \"line\": 11, \"command\": \"cite\"}, {\"key\": \"mixture-of-recursions-2025\", \"file\": \"related_work.tex\", \"line\": 11, \"command\": \"cite\"}, {\"key\": \"mtrouter-2026\", \"file\": \"related_work.tex\", \"line\": 11, \"command\": \"cite\"}, {\"key\": \"routellm-2024\", \"file\": \"related_work.tex\", \"line\": 12, \"command\": \"citep\"}, {\"key\": \"olson2021counterfactual\", \"file\": \"related_work.tex\", \"line\": 16, \"command\": \"citep\"}, {\"key\": \"gajcin2023counterfactual\", \"file\": \"related_work.tex\", \"line\": 16, \"command\": \"citep\"}, {\"key\": \"amitai2024explaining\", \"file\": \"related_work.tex\", \"line\": 16, \"command\": \"citep\"}, {\"key\": \"garcia2015comprehensive\", \"file\": \"related_work.tex\", \"line\": 20, \"command\": \"citet\"}, {\"key\": \"crpo-2021\", \"file\": \"related_work.tex\", \"line\": 20, \"command\": \"citet\"}, {\"key\": \"scienceworld-2022\", \"file\": \"related_work.tex\", \"line\": 24, \"command\": \"cite\"}, {\"key\": \"alfworld-2021\", \"file\": \"related_work.tex\", \"line\": 24, \"command\": \"cite\"}, {\"key\": \"react-2023\", \"file\": \"related_work.tex\", \"line\": 25, \"command\": \"cite\"}, {\"key\": \"reflexion-2023\", \"file\": \"related_work.tex\", \"line\": 25, \"command\": \"cite\"}, {\"key\": \"itp-2026\", \"file\": \"related_work.tex\", \"line\": 26, \"command\": \"citep\"}, {\"key\": \"dynathink-2025\", \"file\": \"related_work.tex\", \"line\": 26, \"command\": \"citep\"}, {\"key\": \"garcia2015comprehensive\", \"file\": \"discussion.tex\", \"line\": 11, \"command\": \"citep\"}, {\"key\": \"cogrouter-2026\", \"file\": \"discussion.tex\", \"line\": 11, \"command\": \"citep\"}, {\"key\": \"ares-2026\", \"file\": \"discussion.tex\", \"line\": 11, \"command\": \"citep\"}, {\"key\": \"react-2023\", \"file\": \"main.tex\", \"line\": 35, \"command\": \"citep\"}, {\"key\": \"reflexion-2023\", \"file\": \"main.tex\", \"line\": 35, \"command\": \"citep\"}, {\"key\": \"dagger-2011\", \"file\": \"main.tex\", \"line\": 35, \"command\": \"citep\"}, {\"key\": \"scienceworld-2022\", \"file\": \"main.tex\", \"line\": 39, \"command\": \"cite\"}, {\"key\": \"alfworld-2021\", \"file\": \"main.tex\", \"line\": 292, \"command\": \"citep\"}], \"online_verification\": [{\"key\": \"scienceworld-2022\", \"title\": \"ScienceWorld: Is Your Agent Smarter Than a 5th Grader?\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"ScienceWorld: Is your Agent Smarter than a 5th Grader?\", \"matched_year\": \"2022\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"react-2023\", \"title\": \"ReAct: Synergizing Reasoning and Acting in Language Models\", \"status\": \"not_found\", \"confidence\": 0.45, \"matched_title\": \"Tree of Thoughts: Deliberate Problem Solving with Large Language Models\", \"matched_year\": \"\", \"mismatch_fields\": [], \"note\": \"best match similarity 0.45 below threshold 0.82\"}, {\"key\": \"toolformer-2023\", \"title\": \"Toolformer: Language Models Can Teach Themselves to Use Tools\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Toolformer: Language Models Can Teach Themselves to Use Tools\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"art-2023\", \"title\": \"ART: Automatic Multi-step Reasoning and Tool-use for Large Language Models\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"ART: Automatic multi-step reasoning and tool-use for large language models\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"chameleon-2023\", \"title\": \"Chameleon: Plug-and-Play Compositional Reasoning with Large Language Models\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Chameleon: Plug-and-Play Compositional Reasoning with Large Language Models\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"retool-2025\", \"title\": \"ReTool: Reinforcement Learning for Strategic Tool Use in LLMs\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"ReTool: Reinforcement Learning for Strategic Tool Use in LLMs\", \"matched_year\": \"2025\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"cogrouter-2026\", \"title\": \"Think Fast and Slow: Step-Level Cognitive Depth Adaptation for LLM Agents\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Think Fast and Slow: Step-Level Cognitive Depth Adaptation for LLM Agents\", \"matched_year\": \"2026\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"ares-2026\", \"title\": \"ARES: Adaptive Reasoning Effort Selection for Efficient LLM Agents\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Ares: Adaptive Reasoning Effort Selection for Efficient LLM Agents\", \"matched_year\": \"2026\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"mixture-of-recursions-2025\", \"title\": \"Mixture-of-Recursions: Learning Dynamic Recursive Depths for Adaptive Token-Level Computation\", \"status\": \"not_found\", \"confidence\": 0.327, \"matched_title\": \"Deep learning approaches to problems in speech recognition, computational chemistry, and natural language text processing\", \"matched_year\": \"\", \"mismatch_fields\": [], \"note\": \"best match similarity 0.33 below threshold 0.82\"}, {\"key\": \"mtrouter-2026\", \"title\": \"MTRouter: Cost-Aware Multi-Turn LLM Routing with History-Model Joint Embeddings\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"MTRouter: Cost-Aware Multi-Turn LLM Routing with History-Model Joint Embeddings\", \"matched_year\": \"2026\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"itp-2026\", \"title\": \"Imagine-then-Plan: Agent Learning from Adaptive Lookahead with World Models\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Imagine-then-Plan: Agent Learning from Adaptive Lookahead with World Models\", \"matched_year\": \"2026\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"dynathink-2025\", \"title\": \"Dyna-Think: Synergizing Reasoning, Acting, and World Model Simulation in AI Agents\", \"status\": \"mismatch\", \"confidence\": 1.0, \"matched_title\": \"Dyna-Think: Synergizing Reasoning, Acting, and World Model Simulation in AI Agents\", \"matched_year\": \"2025\", \"mismatch_fields\": [\"first_author: bib=yu vs api=xiao\"], \"note\": \"\"}, {\"key\": \"tool-overuse-illusion-2026\", \"title\": \"The Tool-Overuse Illusion: Why Does LLM Prefer External Tools over Internal Knowledge?\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"The Tool-Overuse Illusion: Why Does LLM Prefer External Tools over Internal Knowledge?\", \"matched_year\": \"2026\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"when2tool-2026\", \"title\": \"LLM Agents Already Know When to Call Tools -- Even Without Reasoning\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"LLM Agents Already Know When to Call Tools -- Even Without Reasoning\", \"matched_year\": \"2026\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"tool-use-tax-2026\", \"title\": \"Are Tools All We Need? Unveiling the Tool-Use Tax in LLM Agents\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Are Tools All We Need? Unveiling the Tool-Use Tax in LLM Agents\", \"matched_year\": \"2026\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"to-call-or-not-2026\", \"title\": \"To Call or Not to Call: A Framework to Assess and Optimize LLM Tool Calling\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"To Call or Not to Call: A Framework to Assess and Optimize LLM Tool Calling\", \"matched_year\": \"2026\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"dagger-2011\", \"title\": \"A Reduction of Imitation Learning and Structured Prediction to No-Regret Online Learning\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"A Reduction of Imitation Learning and Structured Prediction to No-Regret Online Learning\", \"matched_year\": \"2010\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"toolkengpt-2023\", \"title\": \"ToolkenGPT: Augmenting Frozen Language Models with Massive Tools via Tool Embeddings\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"ToolkenGPT: Augmenting Frozen Language Models with Massive Tools via Tool Embeddings\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"alfworld-2021\", \"title\": \"ALFWorld: Aligning Text and Embodied Environments for Interactive Learning\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"ALFWorld: Aligning Text and Embodied Environments for Interactive Learning\", \"matched_year\": \"2021\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"garcia2015comprehensive\", \"title\": \"A Comprehensive Survey on Safe Reinforcement Learning\", \"status\": \"mismatch\", \"confidence\": 1.0, \"matched_title\": \"A comprehensive survey on safe reinforcement learning\", \"matched_year\": \"2015\", \"mismatch_fields\": [\"first_author: bib=garc\\\\'ia vs api=garcía\"], \"note\": \"\"}, {\"key\": \"voyager-2023\", \"title\": \"Voyager: An Open-Ended Embodied Agent with Large Language Models\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Voyager: An Open-Ended Embodied Agent with Large Language Models\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"amitai2024explaining\", \"title\": \"Explaining Reinforcement Learning Agents through Counterfactual Action Outcomes\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Explaining Reinforcement Learning Agents through Counterfactual Action Outcomes\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"gajcin2023counterfactual\", \"title\": \"Counterfactual Explanations for Reinforcement Learning Agents\", \"status\": \"not_found\", \"confidence\": 0.777, \"matched_title\": \"Counterfactual state explanations for reinforcement learning agents via generative deep learning\", \"matched_year\": \"\", \"mismatch_fields\": [], \"note\": \"best match similarity 0.78 below threshold 0.82\"}, {\"key\": \"olson2021counterfactual\", \"title\": \"Counterfactual State Explanations for Reinforcement Learning Agents via Generative Deep Learning\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Counterfactual state explanations for reinforcement learning agents via generative deep learning\", \"matched_year\": \"2021\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"crpo-2021\", \"title\": \"CRPO: A New Approach for Safe Reinforcement Learning with Convergence Guarantee\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"CRPO: A New Approach for Safe Reinforcement Learning with Convergence Guarantee\", \"matched_year\": \"2020\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"routellm-2024\", \"title\": \"RouteLLM: Learning to Route LLMs with Preference Data\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"RouteLLM: Learning to Route LLMs with Preference Data\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"reflexion-2023\", \"title\": \"Reflexion: Language Agents with Verbal Reinforcement Learning\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Reflexion: Language Agents with Verbal Reinforcement Learning\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"tool-learning-survey-2024\", \"title\": \"Tool Learning with Large Language Models: A Survey\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Tool learning with large language models: a survey\", \"matched_year\": \"2025\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"tot-2023\", \"title\": \"Tree of Thoughts: Deliberate Problem Solving with Large Language Models\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Tree of Thoughts: Deliberate Problem Solving with Large Language Models\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}]}, \"error\": null, \"metadata\": {}}"
    }
  },
  "sourceToolAssistantUUID": "312bd8ba-a8f6-4efa-8668-182fbbce5f07",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/.claude/sessions/review_reviewer_2_ab9762a8",
  "sessionId": "5bc9ff02-4cf0-48f5-9df4-52d4a45b7804",
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
  "lastPrompt": "[Round 8 审稿请求]: ## Round 8 审稿任务 — Reviewer 2（新颖性 + 完整性 + 写作质量）  ### Venue 信息 - **会议**: EMNLP 2026 (通过 ARR May 2026 cycle 提交) - **截止日期**: 2026-05-25 - **页数限制**: 正文 8 页 + 无限参考文献页 - **模板**: ACL LaTeX (`\\…",
  "leafUuid": "a6d50656-ab05-4fb3-87c0-ea18b91da937",
  "sessionId": "5bc9ff02-4cf0-48f5-9df4-52d4a45b7804"
}
```

---

### Runtime record

_source line 22_

```json
{
  "type": "ai-title",
  "aiTitle": "Review paper on modular routing with counterfactual analysis",
  "sessionId": "5bc9ff02-4cf0-48f5-9df4-52d4a45b7804"
}
```

---

### Assistant

_source line 23 · 2026-05-16T12:23:26.494Z_

<details><summary>Logged reasoning block</summary>

```text
Good, I have the main.tex, web search results for reviewer guidelines, and reference verification. Now I need to read the individual sections of the paper. Let me also fetch the ARR review form to get the exact scoring criteria.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a6d50656-ab05-4fb3-87c0-ea18b91da937",
  "isSidechain": false,
  "requestId": "req_011Cb6EwdP3V6iL6L9WSvezK",
  "type": "assistant",
  "uuid": "7a200b20-3a76-48ff-b9f7-57005eb789a3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/.claude/sessions/review_reviewer_2_ab9762a8",
  "sessionId": "5bc9ff02-4cf0-48f5-9df4-52d4a45b7804",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Rf1F4jt7xRHnK7E1ybz6Dq",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 18386,
      "cache_read_input_tokens": 27898,
      "output_tokens": 672,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 18386,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 672,
          "cache_read_input_tokens": 27898,
          "cache_creation_input_tokens": 18386,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 18386
          },
          "type": "message"
        }
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

_source line 24 · 2026-05-16T12:23:27.510Z_

现在并行读取各子文件和获取 ARR review form 详细评分标准。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7a200b20-3a76-48ff-b9f7-57005eb789a3",
  "isSidechain": false,
  "requestId": "req_011Cb6EwdP3V6iL6L9WSvezK",
  "type": "assistant",
  "uuid": "20b70fcd-28d3-4858-a580-ac0ea3b83167",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/.claude/sessions/review_reviewer_2_ab9762a8",
  "sessionId": "5bc9ff02-4cf0-48f5-9df4-52d4a45b7804",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Rf1F4jt7xRHnK7E1ybz6Dq",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 18386,
      "cache_read_input_tokens": 27898,
      "output_tokens": 672,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 18386,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 672,
          "cache_read_input_tokens": 27898,
          "cache_creation_input_tokens": 18386,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 18386
          },
          "type": "message"
        }
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

_source line 25 · 2026-05-16T12:23:29.479Z_

<details open><summary>🔧 Tool call — Read · `toolu_01PQdZg1ZoouRhXvinNZqmCQ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "20b70fcd-28d3-4858-a580-ac0ea3b83167",
  "isSidechain": false,
  "requestId": "req_011Cb6EwdP3V6iL6L9WSvezK",
  "type": "assistant",
  "uuid": "2c31c6fe-3011-4b0e-bc4c-159a4d5d4c69",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/.claude/sessions/review_reviewer_2_ab9762a8",
  "sessionId": "5bc9ff02-4cf0-48f5-9df4-52d4a45b7804",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Rf1F4jt7xRHnK7E1ybz6Dq",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 18386,
      "cache_read_input_tokens": 27898,
      "output_tokens": 672,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 18386,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 672,
          "cache_read_input_tokens": 27898,
          "cache_creation_input_tokens": 18386,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 18386
          },
          "type": "message"
        }
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

_source line 26 · 2026-05-16T12:23:33.937Z_

<details><summary>↩ Tool result · `toolu_01Rwwt3JSb7RL5UgsXXe2CPz`</summary>

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
  "parentUuid": "d5ee7d96-d480-4588-92a2-6bb7f8d21730",
  "isSidechain": false,
  "promptId": "2cc35627-090b-4e8e-873a-80e6ce7d766f",
  "type": "user",
  "uuid": "44f993dc-8497-4e41-95f9-2265c75d49de",
  "toolUseResult": {
    "matches": [
      "WebFetch"
    ],
    "query": "select:WebFetch",
    "total_deferred_tools": 23
  },
  "sourceToolAssistantUUID": "d5ee7d96-d480-4588-92a2-6bb7f8d21730",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/.claude/sessions/review_reviewer_2_ab9762a8",
  "sessionId": "5bc9ff02-4cf0-48f5-9df4-52d4a45b7804",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-16T12:23:29.488Z_

<details><summary>↩ Tool result · `toolu_01PQdZg1ZoouRhXvinNZqmCQ`</summary>

```text
1	\begin{abstract}
2	Modular LLM agents that route between neural reasoning and deterministic computation promise improved reliability, yet understanding \emph{what} drives the value of routing decisions remains unclear. We propose episode-level counterfactual analysis: running complete episodes under pure strategies and comparing final outcomes to decompose routing signal into death-avoidance and non-death components. Among task types exhibiting meaningful routing signal in prescreening (11 of 30 available ScienceWorld task types, 245 episodes, Qwen2.5-7B-Instruct), 78.9\% of non-tie routing labels (75 of 95) are driven by death asymmetry---a penalty-independent metric. Under the default penalty $P{=}100$, the Death Avoidance Factor (DAF) is $90.4\%$ (95\% CI: $[81.6\%, 98.8\%]$), though DAF varies from 50\% ($P{=}10$) to 98\% ($P{=}500$) across penalty settings (Appendix~\ref{app:penalty}). Per-task death rate correlates strongly with routing signal ($r{=}0.97$, though partly structural as death penalties contribute directly to score differences; \S\ref{sec:death-decomp}). An exploratory step-level router trained on these labels achieves $54.1 \pm 5.4\%$ step-level balanced accuracy (with same-episode leakage) but only $47.1 \pm 2.2\%$ on held-out episodes (below the always-deterministic baseline of 50\%); data scaling ($32{\times}$) and capacity scaling (0.6B--4B) confirm this is structural rather than data-limited. Cross-environment analysis on MATH ($N{=}300$) shows routing signal vanishes without a death penalty: the label distribution inverts from 86:9 (deterministic-preferred) to 30:17 (internal directionally favored), with a directional trend favoring internal reasoning ($+4.3$ percentage points, $p = 0.079$, not reaching $\alpha{=}0.05$). A Llama-3.1-8B pilot provides preliminary directional evidence that death-driven routing generalizes across model families. These findings indicate that in environments with catastrophic failure modes, routing value is dominated by safety---the router functions primarily as a safety critic rather than an efficiency optimizer.
3	\end{abstract}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2c31c6fe-3011-4b0e-bc4c-159a4d5d4c69",
  "isSidechain": false,
  "promptId": "2cc35627-090b-4e8e-873a-80e6ce7d766f",
  "type": "user",
  "uuid": "d73511f2-b31d-41d4-84ad-3ee53cdf978f",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/abstract.tex",
      "content": "\\begin{abstract}\nModular LLM agents that route between neural reasoning and deterministic computation promise improved reliability, yet understanding \\emph{what} drives the value of routing decisions remains unclear. We propose episode-level counterfactual analysis: running complete episodes under pure strategies and comparing final outcomes to decompose routing signal into death-avoidance and non-death components. Among task types exhibiting meaningful routing signal in prescreening (11 of 30 available ScienceWorld task types, 245 episodes, Qwen2.5-7B-Instruct), 78.9\\% of non-tie routing labels (75 of 95) are driven by death asymmetry---a penalty-independent metric. Under the default penalty $P{=}100$, the Death Avoidance Factor (DAF) is $90.4\\%$ (95\\% CI: $[81.6\\%, 98.8\\%]$), though DAF varies from 50\\% ($P{=}10$) to 98\\% ($P{=}500$) across penalty settings (Appendix~\\ref{app:penalty}). Per-task death rate correlates strongly with routing signal ($r{=}0.97$, though partly structural as death penalties contribute directly to score differences; \\S\\ref{sec:death-decomp}). An exploratory step-level router trained on these labels achieves $54.1 \\pm 5.4\\%$ step-level balanced accuracy (with same-episode leakage) but only $47.1 \\pm 2.2\\%$ on held-out episodes (below the always-deterministic baseline of 50\\%); data scaling ($32{\\times}$) and capacity scaling (0.6B--4B) confirm this is structural rather than data-limited. Cross-environment analysis on MATH ($N{=}300$) shows routing signal vanishes without a death penalty: the label distribution inverts from 86:9 (deterministic-preferred) to 30:17 (internal directionally favored), with a directional trend favoring internal reasoning ($+4.3$ percentage points, $p = 0.079$, not reaching $\\alpha{=}0.05$). A Llama-3.1-8B pilot provides preliminary directional evidence that death-driven routing generalizes across model families. These findings indicate that in environments with catastrophic failure modes, routing value is dominated by safety---the router functions primarily as a safety critic rather than an efficiency optimizer.\n\\end{abstract}",
      "numLines": 3,
      "startLine": 1,
      "totalLines": 3
    }
  },
  "sourceToolAssistantUUID": "2c31c6fe-3011-4b0e-bc4c-159a4d5d4c69",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/.claude/sessions/review_reviewer_2_ab9762a8",
  "sessionId": "5bc9ff02-4cf0-48f5-9df4-52d4a45b7804",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-16T12:23:30.355Z_

<details open><summary>🔧 Tool call — Read · `toolu_018GqqA68C7AnHoK6fWZZXbL`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d73511f2-b31d-41d4-84ad-3ee53cdf978f",
  "isSidechain": false,
  "requestId": "req_011Cb6EwdP3V6iL6L9WSvezK",
  "type": "assistant",
  "uuid": "11be368d-5b54-4834-bed4-aafaceb7b6e6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/.claude/sessions/review_reviewer_2_ab9762a8",
  "sessionId": "5bc9ff02-4cf0-48f5-9df4-52d4a45b7804",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Rf1F4jt7xRHnK7E1ybz6Dq",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 18386,
      "cache_read_input_tokens": 27898,
      "output_tokens": 672,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 18386,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 672,
          "cache_read_input_tokens": 27898,
          "cache_creation_input_tokens": 18386,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 18386
          },
          "type": "message"
        }
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

_source line 29 · 2026-05-16T12:23:30.361Z_

<details><summary>↩ Tool result · `toolu_018GqqA68C7AnHoK6fWZZXbL`</summary>

```text
1	\section{Introduction}
2	
3	Large language models deployed as interactive agents must repeatedly decide \emph{how} to compute: reason internally, or delegate to an external tool.
4	A Qwen2.5-7B-Instruct agent navigating ScienceWorld \cite{scienceworld-2022}---a text-based science simulation with 30 task types---faces this choice at every step. Tracking temperature thresholds, container states, and multi-step procedures via internal reasoning is error-prone: the model may hallucinate that water has boiled when the stove was never activated, or that an object has been moved when the action was invalid. Deterministic external computation (environment simulators, code interpreters) eliminates such hallucinations via exact state transitions. The practical question for agent design is therefore: \emph{when should an agent route computation externally versus reasoning internally?}
5	
6	Existing routing approaches frame this as a capability or efficiency decision.
7	Toolformer \cite{toolformer-2023} teaches models to insert API calls when doing so reduces perplexity; ART \cite{art-2023} decomposes tasks into tool-augmented programs; Chameleon \cite{chameleon-2023} selects among heterogeneous modules (search, code, vision) per subtask.
8	More recent adaptive-computation methods route to different reasoning depths \cite{cogrouter-2026,ares-2026} or model tiers \cite{mtrouter-2026}.
9	The shared assumption is that routing signal stems from diverse sources---accuracy, latency, capability matching---and that a learned router can exploit this signal to improve over any fixed strategy.
10	But this assumption has never been systematically verified: \emph{what actually drives the value of routing decisions in interactive environments?}
11	
12	We find a surprisingly concentrated answer: \textbf{death avoidance accounts for 90.4\% of the routing signal} (DAF $= 90.4\%$, 95\% CI: $[81.6\%, 98.8\%]$; at default penalty $P{=}100$) in ScienceWorld.
13	The internal strategy's hallucination-induced failures trigger catastrophic agent death (a $-100$ penalty), while the deterministic strategy survives the same episodes.
14	Once death episodes are removed, the performance gap between strategies nearly vanishes.
15	
16	Reaching this conclusion requires a methodological contribution.
17	The standard approach to generating routing labels---per-step oracle comparison---degenerates under sparse rewards.
18	In ScienceWorld, non-zero reward arrives only at episode termination; 97.4\% of steps (across 11 prescreened task types) produce identical scores regardless of modality, leaving no step-level signal to learn from (\S\ref{sec:collection}).
19	Keyword-based heuristics also fail structurally, as ScienceWorld actions lack science-specific terminology (\S\ref{sec:baselines}).
20	We instead propose \emph{episode-level counterfactual analysis}: run complete episodes under pure-internal (ReAct \cite{react-2023}) and pure-deterministic strategies, then compare episode outcomes to generate routing labels (\S\ref{sec:collection}).
21	
22	Among task types exhibiting meaningful routing signal in prescreening (11 of 30 available ScienceWorld task types, 245 episode pairs), the full deterministic advantage is $\Delta_{\text{full}} = +29.60$ points.
23	Excluding death episodes, the gap collapses to $\Delta_{\text{nd}} = +2.84$; 78.9\% of non-tie labels (75 of 95) arise from death asymmetry---a penalty-independent measure.
24	The penalty-sensitive Death Avoidance Factor (DAF; \S\ref{sec:daf}) is $90.4\%$ (95\% CI: $[81.6\%, 98.8\%]$) at the default penalty $P{=}100$, ranging from 50\% ($P{=}10$) to 98\% ($P{=}500$).
25	The per-task correlation between death-rate differential and performance gap is $r = 0.97$ ($p < 10^{-6}$, $n = 11$), confirming that death avoidance is the dominant mechanism across task types (\S\ref{sec:death-decomp}).
26	
27	Two cross-context checks probe the specificity of this finding.
28	First, a MATH Level~4--5 evaluation (300 problems), using a code interpreter as the deterministic modality, shows a directional trend consistent with the absence of death-driven routing signal: internal reasoning outperforms code interpreter by $+4.3$~pp ($p = 0.079$, not reaching $\alpha{=}0.05$)---the opposite direction from ScienceWorld.
29	In the absence of death risk, the deterministic advantage vanishes.
30	Second, a preliminary cross-model pilot with Llama-3.1-8B-Instruct ($N{=}10$ episode pairs, 2 task types) shows directionally consistent death patterns within ScienceWorld (Appendix~\ref{app:cross-model}), suggesting the phenomenon is not specific to a single model, though full-scale multi-model validation remains future work.
31	An exploratory step-level router (Qwen3-1.7B with LoRA) trained on these counterfactual labels achieves $54.1 \pm 5.4\%$ step-level balanced accuracy but only $47.1 \pm 2.2\%$ on held-out episodes---below the always-deterministic baseline---a structural limitation confirmed by data scaling ($32{\times}$) and capacity scaling (0.6B--4B) ablations (\S\ref{sec:router-diagnostic}).
32	
33	Our contributions are:
34	\begin{enumerate}
35	    \item \textbf{Routing signal decomposition.}
36	    We identify step-level oracle degeneracy in sparse-reward environments and introduce episode-level counterfactual analysis with the DAF metric, a methodology for quantifying what fraction of routing signal derives from catastrophic-failure avoidance (\S\ref{sec:collection}--\ref{sec:daf}).
37	
38	    \item \textbf{Death avoidance dominance.}
39	    On ScienceWorld, 78.9\% of non-tie routing labels stem from death asymmetry. The penalty-dependent DAF metric reaches $90.4\%$ at $P{=}100$ but varies substantially across penalty settings. An exploratory router trained on these labels fails to outperform the trivial always-deterministic baseline on held-out episodes ($47.1 \pm 2.2\%$ vs.\ $50.0\%$); data scaling and capacity scaling ablations confirm this is structural---when DAF $= 90.4\%$, always-deterministic is trivially near-optimal (\S\ref{sec:death-decomp}--\ref{sec:router-diagnostic}).
40	
41	    \item \textbf{Cross-context validation.}
42	    On MATH ($N{=}300$), where no death penalty exists, internal reasoning directionally outperforms code interpretation ($+4.3$~pp, $p = 0.079$, not reaching $\alpha{=}0.05$), consistent with the absence of death-driven routing signal. On ALFWorld ($N{=}135$), deterministic success (27.4\%) far exceeds internal (3.0\%), but the mechanism is information asymmetry (access to admissible actions) rather than death avoidance (\S\ref{sec:discussion}). Both contrasts confirm that the ScienceWorld finding is driven by failure structure, not an inherent advantage of deterministic computation.
43	\end{enumerate}
44	
45	
46	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "11be368d-5b54-4834-bed4-aafaceb7b6e6",
  "isSidechain": false,
  "promptId": "2cc35627-090b-4e8e-873a-80e6ce7d766f",
  "type": "user",
  "uuid": "a8ea0eb3-824a-4322-9a58-2c3562b5b02e",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/introduction.tex",
      "content": "\\section{Introduction}\n\nLarge language models deployed as interactive agents must repeatedly decide \\emph{how} to compute: reason internally, or delegate to an external tool.\nA Qwen2.5-7B-Instruct agent navigating ScienceWorld \\cite{scienceworld-2022}---a text-based science simulation with 30 task types---faces this choice at every step. Tracking temperature thresholds, container states, and multi-step procedures via internal reasoning is error-prone: the model may hallucinate that water has boiled when the stove was never activated, or that an object has been moved when the action was invalid. Deterministic external computation (environment simulators, code interpreters) eliminates such hallucinations via exact state transitions. The practical question for agent design is therefore: \\emph{when should an agent route computation externally versus reasoning internally?}\n\nExisting routing approaches frame this as a capability or efficiency decision.\nToolformer \\cite{toolformer-2023} teaches models to insert API calls when doing so reduces perplexity; ART \\cite{art-2023} decomposes tasks into tool-augmented programs; Chameleon \\cite{chameleon-2023} selects among heterogeneous modules (search, code, vision) per subtask.\nMore recent adaptive-computation methods route to different reasoning depths \\cite{cogrouter-2026,ares-2026} or model tiers \\cite{mtrouter-2026}.\nThe shared assumption is that routing signal stems from diverse sources---accuracy, latency, capability matching---and that a learned router can exploit this signal to improve over any fixed strategy.\nBut this assumption has never been systematically verified: \\emph{what actually drives the value of routing decisions in interactive environments?}\n\nWe find a surprisingly concentrated answer: \\textbf{death avoidance accounts for 90.4\\% of the routing signal} (DAF $= 90.4\\%$, 95\\% CI: $[81.6\\%, 98.8\\%]$; at default penalty $P{=}100$) in ScienceWorld.\nThe internal strategy's hallucination-induced failures trigger catastrophic agent death (a $-100$ penalty), while the deterministic strategy survives the same episodes.\nOnce death episodes are removed, the performance gap between strategies nearly vanishes.\n\nReaching this conclusion requires a methodological contribution.\nThe standard approach to generating routing labels---per-step oracle comparison---degenerates under sparse rewards.\nIn ScienceWorld, non-zero reward arrives only at episode termination; 97.4\\% of steps (across 11 prescreened task types) produce identical scores regardless of modality, leaving no step-level signal to learn from (\\S\\ref{sec:collection}).\nKeyword-based heuristics also fail structurally, as ScienceWorld actions lack science-specific terminology (\\S\\ref{sec:baselines}).\nWe instead propose \\emph{episode-level counterfactual analysis}: run complete episodes under pure-internal (ReAct \\cite{react-2023}) and pure-deterministic strategies, then compare episode outcomes to generate routing labels (\\S\\ref{sec:collection}).\n\nAmong task types exhibiting meaningful routing signal in prescreening (11 of 30 available ScienceWorld task types, 245 episode pairs), the full deterministic advantage is $\\Delta_{\\text{full}} = +29.60$ points.\nExcluding death episodes, the gap collapses to $\\Delta_{\\text{nd}} = +2.84$; 78.9\\% of non-tie labels (75 of 95) arise from death asymmetry---a penalty-independent measure.\nThe penalty-sensitive Death Avoidance Factor (DAF; \\S\\ref{sec:daf}) is $90.4\\%$ (95\\% CI: $[81.6\\%, 98.8\\%]$) at the default penalty $P{=}100$, ranging from 50\\% ($P{=}10$) to 98\\% ($P{=}500$).\nThe per-task correlation between death-rate differential and performance gap is $r = 0.97$ ($p < 10^{-6}$, $n = 11$), confirming that death avoidance is the dominant mechanism across task types (\\S\\ref{sec:death-decomp}).\n\nTwo cross-context checks probe the specificity of this finding.\nFirst, a MATH Level~4--5 evaluation (300 problems), using a code interpreter as the deterministic modality, shows a directional trend consistent with the absence of death-driven routing signal: internal reasoning outperforms code interpreter by $+4.3$~pp ($p = 0.079$, not reaching $\\alpha{=}0.05$)---the opposite direction from ScienceWorld.\nIn the absence of death risk, the deterministic advantage vanishes.\nSecond, a preliminary cross-model pilot with Llama-3.1-8B-Instruct ($N{=}10$ episode pairs, 2 task types) shows directionally consistent death patterns within ScienceWorld (Appendix~\\ref{app:cross-model}), suggesting the phenomenon is not specific to a single model, though full-scale multi-model validation remains future work.\nAn exploratory step-level router (Qwen3-1.7B with LoRA) trained on these counterfactual labels achieves $54.1 \\pm 5.4\\%$ step-level balanced accuracy but only $47.1 \\pm 2.2\\%$ on held-out episodes---below the always-deterministic baseline---a structural limitation confirmed by data scaling ($32{\\times}$) and capacity scaling (0.6B--4B) ablations (\\S\\ref{sec:router-diagnostic}).\n\nOur contributions are:\n\\begin{enumerate}\n    \\item \\textbf{Routing signal decomposition.}\n    We identify step-level oracle degeneracy in sparse-reward environments and introduce episode-level counterfactual analysis with the DAF metric, a methodology for quantifying what fraction of routing signal derives from catastrophic-failure avoidance (\\S\\ref{sec:collection}--\\ref{sec:daf}).\n\n    \\item \\textbf{Death avoidance dominance.}\n    On ScienceWorld, 78.9\\% of non-tie routing labels stem from death asymmetry. The penalty-dependent DAF metric reaches $90.4\\%$ at $P{=}100$ but varies substantially across penalty settings. An exploratory router trained on these labels fails to outperform the trivial always-deterministic baseline on held-out episodes ($47.1 \\pm 2.2\\%$ vs.\\ $50.0\\%$); data scaling and capacity scaling ablations confirm this is structural---when DAF $= 90.4\\%$, always-deterministic is trivially near-optimal (\\S\\ref{sec:death-decomp}--\\ref{sec:router-diagnostic}).\n\n    \\item \\textbf{Cross-context validation.}\n    On MATH ($N{=}300$), where no death penalty exists, internal reasoning directionally outperforms code interpretation ($+4.3$~pp, $p = 0.079$, not reaching $\\alpha{=}0.05$), consistent with the absence of death-driven routing signal. On ALFWorld ($N{=}135$), deterministic success (27.4\\%) far exceeds internal (3.0\\%), but the mechanism is information asymmetry (access to admissible actions) rather than death avoidance (\\S\\ref{sec:discussion}). Both contrasts confirm that the ScienceWorld finding is driven by failure structure, not an inherent advantage of deterministic computation.\n\\end{enumerate}\n\n\n",
      "numLines": 46,
      "startLine": 1,
      "totalLines": 46
    }
  },
  "sourceToolAssistantUUID": "11be368d-5b54-4834-bed4-aafaceb7b6e6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/.claude/sessions/review_reviewer_2_ab9762a8",
  "sessionId": "5bc9ff02-4cf0-48f5-9df4-52d4a45b7804",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 30 · 2026-05-16T12:23:30.833Z_

<details open><summary>🔧 Tool call — Read · `toolu_01M5D79xuBWQ5n6SQxTZQaL7`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a8ea0eb3-824a-4322-9a58-2c3562b5b02e",
  "isSidechain": false,
  "requestId": "req_011Cb6EwdP3V6iL6L9WSvezK",
  "type": "assistant",
  "uuid": "73122927-d32d-410e-a035-de37b097af51",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/.claude/sessions/review_reviewer_2_ab9762a8",
  "sessionId": "5bc9ff02-4cf0-48f5-9df4-52d4a45b7804",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Rf1F4jt7xRHnK7E1ybz6Dq",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 18386,
      "cache_read_input_tokens": 27898,
      "output_tokens": 672,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 18386,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 672,
          "cache_read_input_tokens": 27898,
          "cache_creation_input_tokens": 18386,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 18386
          },
          "type": "message"
        }
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

_source line 31 · 2026-05-16T12:23:30.840Z_

<details><summary>↩ Tool result · `toolu_01M5D79xuBWQ5n6SQxTZQaL7`</summary>

```text
1	\section{Method}
2	\label{sec:method}
3	
4	\subsection{Problem Setup}
5	\label{sec:problem-setup}
6	
7	Consider an interactive environment $\mathcal{E}$ with state space $\mathcal{S}$, observation space $\mathcal{O}$, and action space $\mathcal{A}$. An agent follows a policy $\pi: \mathcal{O}^* \rightarrow \mathcal{A}$ that maps observation histories to actions. At each step $t$, the agent receives observation $o_t$, selects action $a_t = \pi(o_1, \ldots, o_t)$, and the environment transitions to state $s_{t+1}$.
8	
9	We define a modality set $\mathcal{M} = \{{\tt int}, {\tt det}\}$ governing how the agent processes state transitions:
10	\begin{itemize}
11	    \item \textbf{Internal} ($m = {\tt int}$): The agent uses its own generation to predict intermediate observations. The LLM interleaves chain-of-thought reasoning with environment actions following the ReAct paradigm \cite{react-2023}, but prediction errors compound across steps.
12	    \item \textbf{Deterministic} ($m = {\tt det}$): The agent receives ground-truth observations from the environment simulator at each step---equivalent to access to a perfect dynamics model. Action selection remains with the LLM; only the state-transition prediction is replaced.
13	\end{itemize}
14	
15	\noindent We restrict $\mathcal{M}$ to two modalities. An ablation comparing chain-of-thought reasoning (deep internal) against direct-answer generation (fast internal) on 6 overlapping task types found no significant difference on any task (Mann--Whitney $p > 0.26$, $|d| \leq 0.31$) and near-identical death rates (41.8\% vs.\ 42.5\%), confirming that reasoning depth does not meaningfully alter internal-mode outcomes in this setting.
16	
17	A \emph{routing policy} $\rho: \mathcal{O}^* \rightarrow \mathcal{M}$ selects which modality to use at each step. The goal of modality routing is to learn $\rho$ that maximizes expected episode return. Our analysis investigates what signal is available to learn such a router.
18	
19	\subsection{Counterfactual Episode Collection}
20	\label{sec:collection}
21	
22	Per-step oracle labeling assigns routing labels by comparing single-step outcomes under each computation modality. Under sparse terminal rewards, this approach degenerates: on ScienceWorld \cite{scienceworld-2022}, 97.4\% of steps (across 11 prescreened task types) produce identical intermediate scores regardless of modality, yielding no routing signal. We instead perform episode-level counterfactual analysis.
23	
24	\paragraph{Pure-strategy trajectories.}
25	For a task instance $t$ and modality $m \in \mathcal{M}$, a \emph{pure-strategy trajectory} is the complete episode obtained by applying modality $m$ at every step:
26	\begin{equation}
27	    \tau_m^{(t)} = (o_1, a_1, o_2, a_2, \ldots, o_T, a_T)
28	\end{equation}
29	where $T \leq T_{\max}$ is the episode length (capped at $T_{\max} = 30$ steps). Both trajectories $\tau_{\tt int}^{(t)}$ and $\tau_{\tt det}^{(t)}$ are executed under identical initial conditions (same random seed, same task variation), ensuring that performance differences arise solely from the modality.
30	
31	Each trajectory $\tau$ yields a terminal score $s(\tau) \in \mathbb{Z}$ and a death indicator $d(\tau) \in \{0, 1\}$. When the agent dies ($d = 1$), the environment imposes a penalty: $s(\tau) = -P$ where $P > 0$ ($P = 100$ in ScienceWorld). The episode pair produces a tuple:
32	\begin{multline}
33	    \bigl(s^{\tt int}, s^{\tt det}, d^{\tt int}, d^{\tt det}\bigr) \triangleq \\
34	    \bigl(s(\tau_{\tt int}),\, s(\tau_{\tt det}),\, d(\tau_{\tt int}),\, d(\tau_{\tt det})\bigr)
35	\end{multline}
36	
37	We use Qwen2.5-7B-Instruct (vLLM) on ScienceWorld \cite{scienceworld-2022}, a text-based environment spanning 30 task types with a $-100$ death penalty. After prescreening, we collect 245 episode pairs across 11 task types (20--40 per type). The framework is environment-agnostic: it requires only paired episode outcomes under two modalities, with no assumptions about score structure or failure mode. We apply it unchanged to ALFWorld and MATH in \S\ref{sec:discussion}.
38	
39	\subsection{Episode-Level Labeling}
40	\label{sec:labeling}
41	
42	We define a labeling function $L$ that maps a counterfactual pair to a routing preference:
43	\begin{multline}
44	    L\!\bigl(\tau_{\tt int}^{(t)}, \tau_{\tt det}^{(t)}\bigr) \;\rightarrow \\
45	    \ell \in \{{\tt det\text{-}pref},\; {\tt int\text{-}pref},\; {\tt no\text{-}pref}\}
46	\end{multline}
47	
48	The labeling function is \emph{death-aware}: it prioritizes survival over score, reflecting the asymmetric cost of catastrophic failure in interactive environments. ScienceWorld scores are integer-valued, so we use exact (in)equality with no threshold. The full procedure is given in Algorithm~\ref{alg:labeling}. Figure~\ref{fig:pipeline} illustrates the overall pipeline.
49	
50	\begin{figure}[t]
51	\centering
52	\includegraphics[width=\columnwidth]{figures/pipeline_overview.pdf}
53	\caption{Counterfactual episode collection and analysis pipeline. Each task instance is run under both pure strategies independently, producing episode-level labels via Algorithm~\ref{alg:labeling}.}
54	\label{fig:pipeline}
55	\end{figure}
56	
57	\begin{algorithm}[t]
58	\caption{Episode-Level Counterfactual Labeling}
59	\label{alg:labeling}
60	\begin{algorithmic}[1]
61	\REQUIRE Task instance $t$, modalities $\mathcal{M} = \{{\tt int}, {\tt det}\}$
62	\ENSURE Label $\ell \in \{{\tt det\text{-}pref}, {\tt int\text{-}pref}, {\tt no\text{-}pref}\}$
63	\FOR{each $m \in \mathcal{M}$}
64	    \STATE Run episode $\tau_m$ with pure-strategy $m$
65	    \STATE Record score $s_m$ and death indicator $d_m$
66	\ENDFOR
67	\IF{$d_{\tt int} = 1$ \AND $d_{\tt det} = 0$}
68	    \STATE $\ell \leftarrow {\tt det\text{-}pref}$ \COMMENT{death asymmetry}
69	\ELSIF{$d_{\tt int} = 0$ \AND $d_{\tt det} = 1$}
70	    \STATE $\ell \leftarrow {\tt int\text{-}pref}$ \COMMENT{death asymmetry}
71	\ELSIF{$d_{\tt int} = d_{\tt det} = 1$}
72	    \STATE $\ell \leftarrow {\tt no\text{-}pref}$ \COMMENT{both dead}
73	\ELSIF{$s_{\tt det} > s_{\tt int}$}
74	    \STATE $\ell \leftarrow {\tt det\text{-}pref}$ \COMMENT{score comparison}
75	\ELSIF{$s_{\tt int} > s_{\tt det}$}
76	    \STATE $\ell \leftarrow {\tt int\text{-}pref}$ \COMMENT{score comparison}
77	\ELSE
78	    \STATE $\ell \leftarrow {\tt no\text{-}pref}$ \COMMENT{tied alive}
79	\ENDIF
80	\RETURN $\ell$
81	\end{algorithmic}
82	\end{algorithm}
83	
84	The four mutually exclusive cases correspond to:
85	\begin{enumerate}
86	    \item \textbf{Death asymmetry} (lines 5--8): $d^{\tt int} \neq d^{\tt det}$ $\rightarrow$ the surviving strategy is preferred. This accounts for 78.9\% of all non-tie labels (75 of 95).
87	    \item \textbf{Both dead} (lines 9--10): $d^{\tt int} = d^{\tt det} = 1$ $\rightarrow$ ${\tt no\_preference}$.
88	    \item \textbf{Score comparison} (lines 11--14): both survive and $s^{\tt det} \neq s^{\tt int}$ $\rightarrow$ the higher-scoring strategy is preferred.
89	    \item \textbf{Tied alive} (lines 15--16): both survive and $s^{\tt det} = s^{\tt int}$ $\rightarrow$ ${\tt no\_preference}$.
90	\end{enumerate}
91	
92	Label distributions are reported in \S\ref{sec:death-decomp}.
93	
94	\subsection{Death Avoidance Factor}
95	\label{sec:daf}
96	
97	To quantify the contribution of death avoidance to routing signal, we decompose the mean score gap between strategies. Let $\delta = \mathbb{E}[d^{\tt int}] - \mathbb{E}[d^{\tt det}]$ denote the death-rate differential and $\Delta_{\text{nd}}$ the mean score gap restricted to episodes where neither strategy dies. The full gap decomposes as:
98	\begin{equation}
99	    \Delta_{\text{full}} \approx \underbrace{\delta \cdot P}_{\text{death contribution}} + \Delta_{\text{nd}}
100	\end{equation}
101	The approximation holds exactly when the surviving strategy scores zero in all death-asymmetry episodes; in our data, the residual is small ($29.60 - 29.37 = 0.23$, or $0.8\%$ of $\Delta_{\text{full}}$).
102	
103	We define the Death Avoidance Factor (DAF) as the fraction of the full score gap attributable to death avoidance:
104	\begin{equation}
105	    \text{DAF} = 1 - \frac{\Delta_{\text{nd}}}{\Delta_{\text{full}}} \approx \frac{\delta P}{\delta P + \Delta_{\text{nd}}}
106	\end{equation}%
107	\footnote{When $\Delta_{\text{nd}} < 0$ (deterministic strategy scores lower than internal on non-death episodes), DAF exceeds 1, indicating death avoidance overcompensates for a non-death disadvantage.}
108	
109	DAF is well-defined when $\Delta_{\text{full}} > 0$; in our data, the minimum per-task $\Delta_{\text{full}}$ is $+9.58$ (\texttt{find-non-living-thing}), ensuring numerical stability. Since DAF $= \delta P / (\delta P + \Delta_{\text{nd}})$, it increases monotonically with $P$---a mathematical consequence, not an empirical finding. We therefore report both DAF at the environment default ($P{=}100$) and the penalty-independent death-asymmetry label fraction.
110	
111	To assess sensitivity to penalty magnitude, we recalculate DAF under hypothetical death penalties (Appendix~\ref{app:penalty}): $P{=}10 \rightarrow$ DAF $= 50.4\%$, $P{=}50 \rightarrow 82.6\%$, $P{=}100 \rightarrow 90.4\%$, $P{=}200 \rightarrow 95.0\%$. Death avoidance remains the dominant component across all penalty magnitudes, though its relative contribution scales with penalty severity. As a penalty-independent companion metric, 78.9\% of non-tie routing labels (75 of 95) are driven by death asymmetry rather than score comparison (\S\ref{sec:labeling}), confirming that death avoidance dominates routing signal regardless of penalty magnitude.
112	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "73122927-d32d-410e-a035-de37b097af51",
  "isSidechain": false,
  "promptId": "2cc35627-090b-4e8e-873a-80e6ce7d766f",
  "type": "user",
  "uuid": "cfab251b-a838-4bc1-978e-2ef4e1726245",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/method.tex",
      "content": "\\section{Method}\n\\label{sec:method}\n\n\\subsection{Problem Setup}\n\\label{sec:problem-setup}\n\nConsider an interactive environment $\\mathcal{E}$ with state space $\\mathcal{S}$, observation space $\\mathcal{O}$, and action space $\\mathcal{A}$. An agent follows a policy $\\pi: \\mathcal{O}^* \\rightarrow \\mathcal{A}$ that maps observation histories to actions. At each step $t$, the agent receives observation $o_t$, selects action $a_t = \\pi(o_1, \\ldots, o_t)$, and the environment transitions to state $s_{t+1}$.\n\nWe define a modality set $\\mathcal{M} = \\{{\\tt int}, {\\tt det}\\}$ governing how the agent processes state transitions:\n\\begin{itemize}\n    \\item \\textbf{Internal} ($m = {\\tt int}$): The agent uses its own generation to predict intermediate observations. The LLM interleaves chain-of-thought reasoning with environment actions following the ReAct paradigm \\cite{react-2023}, but prediction errors compound across steps.\n    \\item \\textbf{Deterministic} ($m = {\\tt det}$): The agent receives ground-truth observations from the environment simulator at each step---equivalent to access to a perfect dynamics model. Action selection remains with the LLM; only the state-transition prediction is replaced.\n\\end{itemize}\n\n\\noindent We restrict $\\mathcal{M}$ to two modalities. An ablation comparing chain-of-thought reasoning (deep internal) against direct-answer generation (fast internal) on 6 overlapping task types found no significant difference on any task (Mann--Whitney $p > 0.26$, $|d| \\leq 0.31$) and near-identical death rates (41.8\\% vs.\\ 42.5\\%), confirming that reasoning depth does not meaningfully alter internal-mode outcomes in this setting.\n\nA \\emph{routing policy} $\\rho: \\mathcal{O}^* \\rightarrow \\mathcal{M}$ selects which modality to use at each step. The goal of modality routing is to learn $\\rho$ that maximizes expected episode return. Our analysis investigates what signal is available to learn such a router.\n\n\\subsection{Counterfactual Episode Collection}\n\\label{sec:collection}\n\nPer-step oracle labeling assigns routing labels by comparing single-step outcomes under each computation modality. Under sparse terminal rewards, this approach degenerates: on ScienceWorld \\cite{scienceworld-2022}, 97.4\\% of steps (across 11 prescreened task types) produce identical intermediate scores regardless of modality, yielding no routing signal. We instead perform episode-level counterfactual analysis.\n\n\\paragraph{Pure-strategy trajectories.}\nFor a task instance $t$ and modality $m \\in \\mathcal{M}$, a \\emph{pure-strategy trajectory} is the complete episode obtained by applying modality $m$ at every step:\n\\begin{equation}\n    \\tau_m^{(t)} = (o_1, a_1, o_2, a_2, \\ldots, o_T, a_T)\n\\end{equation}\nwhere $T \\leq T_{\\max}$ is the episode length (capped at $T_{\\max} = 30$ steps). Both trajectories $\\tau_{\\tt int}^{(t)}$ and $\\tau_{\\tt det}^{(t)}$ are executed under identical initial conditions (same random seed, same task variation), ensuring that performance differences arise solely from the modality.\n\nEach trajectory $\\tau$ yields a terminal score $s(\\tau) \\in \\mathbb{Z}$ and a death indicator $d(\\tau) \\in \\{0, 1\\}$. When the agent dies ($d = 1$), the environment imposes a penalty: $s(\\tau) = -P$ where $P > 0$ ($P = 100$ in ScienceWorld). The episode pair produces a tuple:\n\\begin{multline}\n    \\bigl(s^{\\tt int}, s^{\\tt det}, d^{\\tt int}, d^{\\tt det}\\bigr) \\triangleq \\\\\n    \\bigl(s(\\tau_{\\tt int}),\\, s(\\tau_{\\tt det}),\\, d(\\tau_{\\tt int}),\\, d(\\tau_{\\tt det})\\bigr)\n\\end{multline}\n\nWe use Qwen2.5-7B-Instruct (vLLM) on ScienceWorld \\cite{scienceworld-2022}, a text-based environment spanning 30 task types with a $-100$ death penalty. After prescreening, we collect 245 episode pairs across 11 task types (20--40 per type). The framework is environment-agnostic: it requires only paired episode outcomes under two modalities, with no assumptions about score structure or failure mode. We apply it unchanged to ALFWorld and MATH in \\S\\ref{sec:discussion}.\n\n\\subsection{Episode-Level Labeling}\n\\label{sec:labeling}\n\nWe define a labeling function $L$ that maps a counterfactual pair to a routing preference:\n\\begin{multline}\n    L\\!\\bigl(\\tau_{\\tt int}^{(t)}, \\tau_{\\tt det}^{(t)}\\bigr) \\;\\rightarrow \\\\\n    \\ell \\in \\{{\\tt det\\text{-}pref},\\; {\\tt int\\text{-}pref},\\; {\\tt no\\text{-}pref}\\}\n\\end{multline}\n\nThe labeling function is \\emph{death-aware}: it prioritizes survival over score, reflecting the asymmetric cost of catastrophic failure in interactive environments. ScienceWorld scores are integer-valued, so we use exact (in)equality with no threshold. The full procedure is given in Algorithm~\\ref{alg:labeling}. Figure~\\ref{fig:pipeline} illustrates the overall pipeline.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/pipeline_overview.pdf}\n\\caption{Counterfactual episode collection and analysis pipeline. Each task instance is run under both pure strategies independently, producing episode-level labels via Algorithm~\\ref{alg:labeling}.}\n\\label{fig:pipeline}\n\\end{figure}\n\n\\begin{algorithm}[t]\n\\caption{Episode-Level Counterfactual Labeling}\n\\label{alg:labeling}\n\\begin{algorithmic}[1]\n\\REQUIRE Task instance $t$, modalities $\\mathcal{M} = \\{{\\tt int}, {\\tt det}\\}$\n\\ENSURE Label $\\ell \\in \\{{\\tt det\\text{-}pref}, {\\tt int\\text{-}pref}, {\\tt no\\text{-}pref}\\}$\n\\FOR{each $m \\in \\mathcal{M}$}\n    \\STATE Run episode $\\tau_m$ with pure-strategy $m$\n    \\STATE Record score $s_m$ and death indicator $d_m$\n\\ENDFOR\n\\IF{$d_{\\tt int} = 1$ \\AND $d_{\\tt det} = 0$}\n    \\STATE $\\ell \\leftarrow {\\tt det\\text{-}pref}$ \\COMMENT{death asymmetry}\n\\ELSIF{$d_{\\tt int} = 0$ \\AND $d_{\\tt det} = 1$}\n    \\STATE $\\ell \\leftarrow {\\tt int\\text{-}pref}$ \\COMMENT{death asymmetry}\n\\ELSIF{$d_{\\tt int} = d_{\\tt det} = 1$}\n    \\STATE $\\ell \\leftarrow {\\tt no\\text{-}pref}$ \\COMMENT{both dead}\n\\ELSIF{$s_{\\tt det} > s_{\\tt int}$}\n    \\STATE $\\ell \\leftarrow {\\tt det\\text{-}pref}$ \\COMMENT{score comparison}\n\\ELSIF{$s_{\\tt int} > s_{\\tt det}$}\n    \\STATE $\\ell \\leftarrow {\\tt int\\text{-}pref}$ \\COMMENT{score comparison}\n\\ELSE\n    \\STATE $\\ell \\leftarrow {\\tt no\\text{-}pref}$ \\COMMENT{tied alive}\n\\ENDIF\n\\RETURN $\\ell$\n\\end{algorithmic}\n\\end{algorithm}\n\nThe four mutually exclusive cases correspond to:\n\\begin{enumerate}\n    \\item \\textbf{Death asymmetry} (lines 5--8): $d^{\\tt int} \\neq d^{\\tt det}$ $\\rightarrow$ the surviving strategy is preferred. This accounts for 78.9\\% of all non-tie labels (75 of 95).\n    \\item \\textbf{Both dead} (lines 9--10): $d^{\\tt int} = d^{\\tt det} = 1$ $\\rightarrow$ ${\\tt no\\_preference}$.\n    \\item \\textbf{Score comparison} (lines 11--14): both survive and $s^{\\tt det} \\neq s^{\\tt int}$ $\\rightarrow$ the higher-scoring strategy is preferred.\n    \\item \\textbf{Tied alive} (lines 15--16): both survive and $s^{\\tt det} = s^{\\tt int}$ $\\rightarrow$ ${\\tt no\\_preference}$.\n\\end{enumerate}\n\nLabel distributions are reported in \\S\\ref{sec:death-decomp}.\n\n\\subsection{Death Avoidance Factor}\n\\label{sec:daf}\n\nTo quantify the contribution of death avoidance to routing signal, we decompose the mean score gap between strategies. Let $\\delta = \\mathbb{E}[d^{\\tt int}] - \\mathbb{E}[d^{\\tt det}]$ denote the death-rate differential and $\\Delta_{\\text{nd}}$ the mean score gap restricted to episodes where neither strategy dies. The full gap decomposes as:\n\\begin{equation}\n    \\Delta_{\\text{full}} \\approx \\underbrace{\\delta \\cdot P}_{\\text{death contribution}} + \\Delta_{\\text{nd}}\n\\end{equation}\nThe approximation holds exactly when the surviving strategy scores zero in all death-asymmetry episodes; in our data, the residual is small ($29.60 - 29.37 = 0.23$, or $0.8\\%$ of $\\Delta_{\\text{full}}$).\n\nWe define the Death Avoidance Factor (DAF) as the fraction of the full score gap attributable to death avoidance:\n\\begin{equation}\n    \\text{DAF} = 1 - \\frac{\\Delta_{\\text{nd}}}{\\Delta_{\\text{full}}} \\approx \\frac{\\delta P}{\\delta P + \\Delta_{\\text{nd}}}\n\\end{equation}%\n\\footnote{When $\\Delta_{\\text{nd}} < 0$ (deterministic strategy scores lower than internal on non-death episodes), DAF exceeds 1, indicating death avoidance overcompensates for a non-death disadvantage.}\n\nDAF is well-defined when $\\Delta_{\\text{full}} > 0$; in our data, the minimum per-task $\\Delta_{\\text{full}}$ is $+9.58$ (\\texttt{find-non-living-thing}), ensuring numerical stability. Since DAF $= \\delta P / (\\delta P + \\Delta_{\\text{nd}})$, it increases monotonically with $P$---a mathematical consequence, not an empirical finding. We therefore report both DAF at the environment default ($P{=}100$) and the penalty-independent death-asymmetry label fraction.\n\nTo assess sensitivity to penalty magnitude, we recalculate DAF under hypothetical death penalties (Appendix~\\ref{app:penalty}): $P{=}10 \\rightarrow$ DAF $= 50.4\\%$, $P{=}50 \\rightarrow 82.6\\%$, $P{=}100 \\rightarrow 90.4\\%$, $P{=}200 \\rightarrow 95.0\\%$. Death avoidance remains the dominant component across all penalty magnitudes, though its relative contribution scales with penalty severity. As a penalty-independent companion metric, 78.9\\% of non-tie routing labels (75 of 95) are driven by death asymmetry rather than score comparison (\\S\\ref{sec:labeling}), confirming that death avoidance dominates routing signal regardless of penalty magnitude.\n",
      "numLines": 112,
      "startLine": 1,
      "totalLines": 112
    }
  },
  "sourceToolAssistantUUID": "73122927-d32d-410e-a035-de37b097af51",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/.claude/sessions/review_reviewer_2_ab9762a8",
  "sessionId": "5bc9ff02-4cf0-48f5-9df4-52d4a45b7804",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 32 · 2026-05-16T12:23:31.363Z_

<details open><summary>🔧 Tool call — Read · `toolu_01XLvZqL2Xb8UJJECXCYmJJz`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cfab251b-a838-4bc1-978e-2ef4e1726245",
  "isSidechain": false,
  "requestId": "req_011Cb6EwdP3V6iL6L9WSvezK",
  "type": "assistant",
  "uuid": "e5a04ef1-29ea-4fc8-98fc-c448a64df716",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/.claude/sessions/review_reviewer_2_ab9762a8",
  "sessionId": "5bc9ff02-4cf0-48f5-9df4-52d4a45b7804",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Rf1F4jt7xRHnK7E1ybz6Dq",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 18386,
      "cache_read_input_tokens": 27898,
      "output_tokens": 672,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 18386,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 672,
          "cache_read_input_tokens": 27898,
          "cache_creation_input_tokens": 18386,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 18386
          },
          "type": "message"
        }
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

_source line 33 · 2026-05-16T12:23:31.369Z_

<details><summary>↩ Tool result · `toolu_01XLvZqL2Xb8UJJECXCYmJJz`</summary>

```text
1	\section{Experiments}
2	
3	\subsection{Death Avoidance Decomposition}
4	\label{sec:death-decomp}
5	
6	\begin{figure}[t]
7	\centering
8	\includegraphics[width=\columnwidth]{figures/fig1_daf_scatter.pdf}
9	\caption{Per-task scatter: death rate differential (internal $-$ deterministic) vs.\ performance gap ($\Delta_{\text{full}}$). $r = 0.97$, $p < 10^{-6}$, $n = 11$ task types.}
10	\label{fig:decomposition}
11	\end{figure}
12	
13	Across 245 episodes, $\Delta_{\text{full}} = +29.60$; excluding death episodes, $\Delta_{\text{nd}} = +2.84$, yielding DAF $= 90.4\%$ (95\% CI: $[81.6\%, 98.8\%]$; at default $P{=}100$). The penalty-independent death-asymmetry label fraction is 78.9\% (75 of 95 non-tie labels). The internal strategy dies in 42.9\% of episodes versus 16.3\% for deterministic (2.6$\times$). Per-task, death rate differential correlates strongly with $\Delta_{\text{full}}$ ($r = 0.97$, $p < 10^{-6}$; Figure~\ref{fig:decomposition}; robustness diagnostics in Appendix~\ref{app:correlation}). Of 245 episodes, 86 are \texttt{det\_preferred}, 9 \texttt{internal\_preferred}, and 150 \texttt{no\_preference}.
14	
15	One exception: \texttt{find-non-living-thing} ($n{=}40$, zero deaths) has DAF $= 0\%$ with $\Delta = +9.58$ entirely from non-death score differences; all 10 remaining types exceed DAF $> 85\%$. Bootstrap 95\% CIs confirm $\Delta > 0$ for 10 of 11 types; \texttt{chemistry-mix} ($N{=}20$, $\Delta = 21.8$, 95\% CI $[-5.0, 48.6]$) is the sole exception (Appendix~\ref{app:per-task}).
16	
17	\subsection{Baselines}
18	\label{sec:baselines}
19	
20	\begin{table}[t]
21	\centering
22	\small
23	\resizebox{\columnwidth}{!}{%
24	\begin{tabular}{@{}lccc@{}}
25	\toprule
26	Strategy & Score & 95\% CI & Death \% \\
27	\midrule
28	Always-Internal & $-39.07$ & [$-46.40$, $-32.27$] & 42.9 \\
29	Always-Deterministic & $-9.47$ & [$-14.71$, $-4.29$] & 16.3 \\
30	Random & $-22.38$ & [$-28.67$, $-15.75$] & 27.8 \\
31	Oracle & $-6.58$ & [$-11.54$, $-1.70$] & 14.3 \\
32	\midrule
33	Trained Router$^\dagger$ & $-10.70$ & [$-16.33$, $-5.27$] & 17.6 \\
34	\bottomrule
35	\end{tabular}}
36	\caption{Episode-weighted mean scores on ScienceWorld (11 tasks, 245 episodes). $\dagger$\,Single seed; see \S\ref{sec:router-diagnostic}.}
37	\label{tab:baselines}
38	\end{table}
39	
40	Always-deterministic ($-9.47$) outperforms always-internal ($-39.07$) by 29.60 points. The oracle improves only to $-6.58$, with 96.3\% of decisions matching always-deterministic---\emph{oracle degeneracy} indicating the optimal routing policy closely resembles unconditional deterministic computation.
41	
42	\subsection{Router Training as Diagnostic}
43	\label{sec:router-diagnostic}
44	
45	We probe whether counterfactual labels can train a step-level router, as a diagnostic of label informativeness. A classification head on LLM hidden states degenerates to always-deterministic across all configurations. An implicit router (Qwen3-1.7B fine-tuned; Appendix~\ref{app:router-details}) yields $54.1 \pm 5.4\%$ step-level balanced accuracy but $47.1 \pm 2.2\%$ on held-out episodes (8 seeds)---below always-deterministic (50\%). This is structural, not data-limited: $32{\times}$ data scaling, 0.6B--4B capacity scaling, majority-vote baseline, and per-task-type evaluation all confirm no learnable routing signal beyond always-deterministic (Appendix~\ref{app:seed-robustness}). Deployed end-to-end (Table~\ref{tab:baselines}), the router ($-10.70$) does not outperform always-deterministic ($-9.47$; overlapping CIs). We verify label quality in Appendix~\ref{app:labeling}.
46	
47	A Llama-3.1-8B pilot ($N{=}10$) shows directionally consistent death patterns (Appendix~\ref{app:cross-model}). Failure mode and ablation details in Appendices~\ref{app:failure-modes}--\ref{app:ablations}.
48	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e5a04ef1-29ea-4fc8-98fc-c448a64df716",
  "isSidechain": false,
  "promptId": "2cc35627-090b-4e8e-873a-80e6ce7d766f",
  "type": "user",
  "uuid": "dbef1c20-cf7b-4bd4-9d6f-fb7a058f8f0e",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/experiments.tex",
      "content": "\\section{Experiments}\n\n\\subsection{Death Avoidance Decomposition}\n\\label{sec:death-decomp}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig1_daf_scatter.pdf}\n\\caption{Per-task scatter: death rate differential (internal $-$ deterministic) vs.\\ performance gap ($\\Delta_{\\text{full}}$). $r = 0.97$, $p < 10^{-6}$, $n = 11$ task types.}\n\\label{fig:decomposition}\n\\end{figure}\n\nAcross 245 episodes, $\\Delta_{\\text{full}} = +29.60$; excluding death episodes, $\\Delta_{\\text{nd}} = +2.84$, yielding DAF $= 90.4\\%$ (95\\% CI: $[81.6\\%, 98.8\\%]$; at default $P{=}100$). The penalty-independent death-asymmetry label fraction is 78.9\\% (75 of 95 non-tie labels). The internal strategy dies in 42.9\\% of episodes versus 16.3\\% for deterministic (2.6$\\times$). Per-task, death rate differential correlates strongly with $\\Delta_{\\text{full}}$ ($r = 0.97$, $p < 10^{-6}$; Figure~\\ref{fig:decomposition}; robustness diagnostics in Appendix~\\ref{app:correlation}). Of 245 episodes, 86 are \\texttt{det\\_preferred}, 9 \\texttt{internal\\_preferred}, and 150 \\texttt{no\\_preference}.\n\nOne exception: \\texttt{find-non-living-thing} ($n{=}40$, zero deaths) has DAF $= 0\\%$ with $\\Delta = +9.58$ entirely from non-death score differences; all 10 remaining types exceed DAF $> 85\\%$. Bootstrap 95\\% CIs confirm $\\Delta > 0$ for 10 of 11 types; \\texttt{chemistry-mix} ($N{=}20$, $\\Delta = 21.8$, 95\\% CI $[-5.0, 48.6]$) is the sole exception (Appendix~\\ref{app:per-task}).\n\n\\subsection{Baselines}\n\\label{sec:baselines}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{@{}lccc@{}}\n\\toprule\nStrategy & Score & 95\\% CI & Death \\% \\\\\n\\midrule\nAlways-Internal & $-39.07$ & [$-46.40$, $-32.27$] & 42.9 \\\\\nAlways-Deterministic & $-9.47$ & [$-14.71$, $-4.29$] & 16.3 \\\\\nRandom & $-22.38$ & [$-28.67$, $-15.75$] & 27.8 \\\\\nOracle & $-6.58$ & [$-11.54$, $-1.70$] & 14.3 \\\\\n\\midrule\nTrained Router$^\\dagger$ & $-10.70$ & [$-16.33$, $-5.27$] & 17.6 \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Episode-weighted mean scores on ScienceWorld (11 tasks, 245 episodes). $\\dagger$\\,Single seed; see \\S\\ref{sec:router-diagnostic}.}\n\\label{tab:baselines}\n\\end{table}\n\nAlways-deterministic ($-9.47$) outperforms always-internal ($-39.07$) by 29.60 points. The oracle improves only to $-6.58$, with 96.3\\% of decisions matching always-deterministic---\\emph{oracle degeneracy} indicating the optimal routing policy closely resembles unconditional deterministic computation.\n\n\\subsection{Router Training as Diagnostic}\n\\label{sec:router-diagnostic}\n\nWe probe whether counterfactual labels can train a step-level router, as a diagnostic of label informativeness. A classification head on LLM hidden states degenerates to always-deterministic across all configurations. An implicit router (Qwen3-1.7B fine-tuned; Appendix~\\ref{app:router-details}) yields $54.1 \\pm 5.4\\%$ step-level balanced accuracy but $47.1 \\pm 2.2\\%$ on held-out episodes (8 seeds)---below always-deterministic (50\\%). This is structural, not data-limited: $32{\\times}$ data scaling, 0.6B--4B capacity scaling, majority-vote baseline, and per-task-type evaluation all confirm no learnable routing signal beyond always-deterministic (Appendix~\\ref{app:seed-robustness}). Deployed end-to-end (Table~\\ref{tab:baselines}), the router ($-10.70$) does not outperform always-deterministic ($-9.47$; overlapping CIs). We verify label quality in Appendix~\\ref{app:labeling}.\n\nA Llama-3.1-8B pilot ($N{=}10$) shows directionally consistent death patterns (Appendix~\\ref{app:cross-model}). Failure mode and ablation details in Appendices~\\ref{app:failure-modes}--\\ref{app:ablations}.\n",
      "numLines": 48,
      "startLine": 1,
      "totalLines": 48
    }
  },
  "sourceToolAssistantUUID": "e5a04ef1-29ea-4fc8-98fc-c448a64df716",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/.claude/sessions/review_reviewer_2_ab9762a8",
  "sessionId": "5bc9ff02-4cf0-48f5-9df4-52d4a45b7804",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 34 · 2026-05-16T12:23:31.814Z_

<details open><summary>🔧 Tool call — Read · `toolu_01ND5TfWtYdbwQHnvLuiu6zz`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dbef1c20-cf7b-4bd4-9d6f-fb7a058f8f0e",
  "isSidechain": false,
  "requestId": "req_011Cb6EwdP3V6iL6L9WSvezK",
  "type": "assistant",
  "uuid": "ecce4556-26de-4481-8d57-1ce7f7b9fe91",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/.claude/sessions/review_reviewer_2_ab9762a8",
  "sessionId": "5bc9ff02-4cf0-48f5-9df4-52d4a45b7804",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Rf1F4jt7xRHnK7E1ybz6Dq",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 18386,
      "cache_read_input_tokens": 27898,
      "output_tokens": 672,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 18386,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 672,
          "cache_read_input_tokens": 27898,
          "cache_creation_input_tokens": 18386,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 18386
          },
          "type": "message"
        }
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

_source line 35 · 2026-05-16T12:23:31.819Z_

<details><summary>↩ Tool result · `toolu_01ND5TfWtYdbwQHnvLuiu6zz`</summary>

```text
1	\section{Related Work}
2	
3	\paragraph{Tool Use and External Computation in LLMs.}
4	A growing body of work augments language models with external tools \citep{tool-learning-survey-2024}.
5	Toolformer \cite{toolformer-2023} teaches LLMs to insert API calls via self-supervised loss filtering; ART \cite{art-2023} decomposes tasks into tool-augmented programs; Chameleon \cite{chameleon-2023} composes heterogeneous modules per subtask; ReTool \cite{retool-2025} applies RL to discover when code execution is preferable to chain-of-thought.
6	These focus on \emph{learning to use tools}; we ask a prior question: \emph{what signal drives the routing decision?}
7	Recent concurrent work sharpens this question: \citet{tool-overuse-illusion-2026} identify a cognitive-illusion effect in LLM tool use, \citet{when2tool-2026} show tool-call decisions are encoded in hidden states before reasoning, \citet{tool-use-tax-2026} quantify a ``tool-use tax'' where tools degrade performance, and \citet{to-call-or-not-2026} propose a necessity--utility--affordability framework.
8	Our counterfactual decomposition provides environment-grounded evidence: in ScienceWorld, $90.4\%$ of routing signal at $P{=}100$ traces to catastrophic-failure prevention.
9	
10	\paragraph{Adaptive Computation and Routing.}
11	CogRouter \cite{cogrouter-2026} adapts reasoning depth per step, ARES \cite{ares-2026} selects among reasoning effort levels, Mixture-of-Recursions \cite{mixture-of-recursions-2025} learns token-level recursion depths, and MTRouter \cite{mtrouter-2026} addresses multi-turn routing across heterogeneous models.
12	RouteLLM \citep{routellm-2024} learns routers from preference data to select between strong and weak models.
13	These optimize \emph{how} to route; we reveal \emph{why} routing helps---in interactive environments, the dominant signal is catastrophic-failure avoidance.
14	
15	\paragraph{Counterfactual Evaluation in RL.}
16	Prior work generates counterfactual explanations for RL agents by perturbing individual actions within a fixed policy \citep{olson2021counterfactual, gajcin2023counterfactual, amitai2024explaining}.
17	Our approach differs in both purpose and granularity: we execute two complete episodes under different routing strategies, producing prospective paired comparisons that isolate routing signal \emph{before} any router is trained, sidestepping compounding perturbation artifacts.
18	
19	\paragraph{Safe RL and Catastrophic Failure.}
20	\citet{garcia2015comprehensive} survey safe RL methods that constrain policies to avoid catastrophic outcomes; \citet{crpo-2021} develop principled constrained optimization with formal convergence guarantees.
21	Our counterfactual decomposition reveals that death avoidance is the dominant component of routing signal, suggesting that modality routing functions primarily as a safety mechanism rather than a generic capability-matching problem.
22	
23	\paragraph{LLM Agents in Interactive Environments.}
24	ScienceWorld \cite{scienceworld-2022} serves as our primary testbed; ALFWorld \cite{alfworld-2021} provides a complementary household environment.
25	ReAct \cite{react-2023} interleaves reasoning with actions and serves as our internal baseline; Reflexion \cite{reflexion-2023} extends this with verbal self-reflection.
26	Recent agent architectures augment planning with world models \citep{itp-2026, dynathink-2025}, which inherit hallucination risks.
27	Our deterministic modality provides exact state transitions, and our analysis shows this exactness matters almost exclusively for death avoidance.
28	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ecce4556-26de-4481-8d57-1ce7f7b9fe91",
  "isSidechain": false,
  "promptId": "2cc35627-090b-4e8e-873a-80e6ce7d766f",
  "type": "user",
  "uuid": "1c1e056a-f6e0-477e-92a0-209d104a2307",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/related_work.tex",
      "content": "\\section{Related Work}\n\n\\paragraph{Tool Use and External Computation in LLMs.}\nA growing body of work augments language models with external tools \\citep{tool-learning-survey-2024}.\nToolformer \\cite{toolformer-2023} teaches LLMs to insert API calls via self-supervised loss filtering; ART \\cite{art-2023} decomposes tasks into tool-augmented programs; Chameleon \\cite{chameleon-2023} composes heterogeneous modules per subtask; ReTool \\cite{retool-2025} applies RL to discover when code execution is preferable to chain-of-thought.\nThese focus on \\emph{learning to use tools}; we ask a prior question: \\emph{what signal drives the routing decision?}\nRecent concurrent work sharpens this question: \\citet{tool-overuse-illusion-2026} identify a cognitive-illusion effect in LLM tool use, \\citet{when2tool-2026} show tool-call decisions are encoded in hidden states before reasoning, \\citet{tool-use-tax-2026} quantify a ``tool-use tax'' where tools degrade performance, and \\citet{to-call-or-not-2026} propose a necessity--utility--affordability framework.\nOur counterfactual decomposition provides environment-grounded evidence: in ScienceWorld, $90.4\\%$ of routing signal at $P{=}100$ traces to catastrophic-failure prevention.\n\n\\paragraph{Adaptive Computation and Routing.}\nCogRouter \\cite{cogrouter-2026} adapts reasoning depth per step, ARES \\cite{ares-2026} selects among reasoning effort levels, Mixture-of-Recursions \\cite{mixture-of-recursions-2025} learns token-level recursion depths, and MTRouter \\cite{mtrouter-2026} addresses multi-turn routing across heterogeneous models.\nRouteLLM \\citep{routellm-2024} learns routers from preference data to select between strong and weak models.\nThese optimize \\emph{how} to route; we reveal \\emph{why} routing helps---in interactive environments, the dominant signal is catastrophic-failure avoidance.\n\n\\paragraph{Counterfactual Evaluation in RL.}\nPrior work generates counterfactual explanations for RL agents by perturbing individual actions within a fixed policy \\citep{olson2021counterfactual, gajcin2023counterfactual, amitai2024explaining}.\nOur approach differs in both purpose and granularity: we execute two complete episodes under different routing strategies, producing prospective paired comparisons that isolate routing signal \\emph{before} any router is trained, sidestepping compounding perturbation artifacts.\n\n\\paragraph{Safe RL and Catastrophic Failure.}\n\\citet{garcia2015comprehensive} survey safe RL methods that constrain policies to avoid catastrophic outcomes; \\citet{crpo-2021} develop principled constrained optimization with formal convergence guarantees.\nOur counterfactual decomposition reveals that death avoidance is the dominant component of routing signal, suggesting that modality routing functions primarily as a safety mechanism rather than a generic capability-matching problem.\n\n\\paragraph{LLM Agents in Interactive Environments.}\nScienceWorld \\cite{scienceworld-2022} serves as our primary testbed; ALFWorld \\cite{alfworld-2021} provides a complementary household environment.\nReAct \\cite{react-2023} interleaves reasoning with actions and serves as our internal baseline; Reflexion \\cite{reflexion-2023} extends this with verbal self-reflection.\nRecent agent architectures augment planning with world models \\citep{itp-2026, dynathink-2025}, which inherit hallucination risks.\nOur deterministic modality provides exact state transitions, and our analysis shows this exactness matters almost exclusively for death avoidance.\n",
      "numLines": 28,
      "startLine": 1,
      "totalLines": 28
    }
  },
  "sourceToolAssistantUUID": "ecce4556-26de-4481-8d57-1ce7f7b9fe91",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/.claude/sessions/review_reviewer_2_ab9762a8",
  "sessionId": "5bc9ff02-4cf0-48f5-9df4-52d4a45b7804",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 36 · 2026-05-16T12:23:32.275Z_

<details open><summary>🔧 Tool call — Read · `toolu_01A8x1xE5V1iCwNHSRUpubtA`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1c1e056a-f6e0-477e-92a0-209d104a2307",
  "isSidechain": false,
  "requestId": "req_011Cb6EwdP3V6iL6L9WSvezK",
  "type": "assistant",
  "uuid": "0812bd2a-c966-4dec-bd65-a3381096a31c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/.claude/sessions/review_reviewer_2_ab9762a8",
  "sessionId": "5bc9ff02-4cf0-48f5-9df4-52d4a45b7804",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Rf1F4jt7xRHnK7E1ybz6Dq",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 18386,
      "cache_read_input_tokens": 27898,
      "output_tokens": 672,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 18386,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 672,
          "cache_read_input_tokens": 27898,
          "cache_creation_input_tokens": 18386,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 18386
          },
          "type": "message"
        }
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

_source line 37 · 2026-05-16T12:23:32.281Z_

<details><summary>↩ Tool result · `toolu_01A8x1xE5V1iCwNHSRUpubtA`</summary>

```text
1	\section{Discussion}
2	\label{sec:discussion}
3	
4	\paragraph{Cross-environment evidence.}
5	Does routing signal persist without catastrophic failure? On MATH Level~4--5 (300 problems), using a code interpreter as the deterministic modality, internal reasoning directionally outperforms: 81.0\% vs.\ 76.7\% accuracy ($+4.3$~pp, 95\% CI $[0.0, +8.7]$; McNemar $p = 0.079$, not reaching $\alpha{=}0.05$). The label distribution inverts: 30 internal-preferred vs.\ 17 deterministic-preferred (cf.\ 9:86 in ScienceWorld), with 84.3\% no-preference. In the absence of death risk, the deterministic advantage vanishes---consistent with death avoidance as the primary driver. A complementary evaluation on ALFWorld ($N{=}135$) confirms that the counterfactual framework identifies different routing mechanisms across environments: the deterministic advantage there stems from information asymmetry (access to admissible actions) rather than death avoidance (Appendix~\ref{app:cross-env}).
6	
7	\paragraph{Penalty sensitivity.}
8	The $r = 0.97$ correlation is specific to catastrophic death (score $= -100$); defining ``failure'' as any non-positive score yields $r = -0.13$ ($p = 0.70$). The correlation emerges only at $P \geq 50$ ($r = 0.86$) and reflects that non-death episodes show near-zero performance differential ($\Delta_{\text{nd}} = 2.84$; Appendix~\ref{app:penalty}). Death is effectively the \emph{only} component generating differential routing signal in ScienceWorld. These findings may be capability-dependent: the 42.9\% internal death rate reflects a 7B model's hallucination vulnerability; larger models with lower death rates would reduce DAF, potentially revealing non-death routing signal currently masked by catastrophic failures.
9	
10	\paragraph{Implications for router design.}
11	The dominance of death avoidance (DAF $= 90.4\%$ at $P{=}100$) reframes modality routing as primarily a \emph{safety} problem rather than an efficiency-quality tradeoff. The router functions as a safety critic---predicting which states lead to catastrophic failure under internal reasoning---aligning more closely with safe RL~\citep{garcia2015comprehensive} than with cost-quality optimization~\citep{cogrouter-2026, ares-2026}. The extreme label imbalance (86:9 deterministic-preferred, 150 no-preference) is not an artifact but a central result: among episodes where modality matters, deterministic is preferred at 9.6:1, explaining why always-deterministic is a strong baseline and why the trained router (\S\ref{sec:router-diagnostic}) adds no value. A lightweight death predictor may capture most routing benefit without full counterfactual labeling.
12	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0812bd2a-c966-4dec-bd65-a3381096a31c",
  "isSidechain": false,
  "promptId": "2cc35627-090b-4e8e-873a-80e6ce7d766f",
  "type": "user",
  "uuid": "f61cd32a-3dfa-46e8-8eaf-2d788ed2a384",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/discussion.tex",
      "content": "\\section{Discussion}\n\\label{sec:discussion}\n\n\\paragraph{Cross-environment evidence.}\nDoes routing signal persist without catastrophic failure? On MATH Level~4--5 (300 problems), using a code interpreter as the deterministic modality, internal reasoning directionally outperforms: 81.0\\% vs.\\ 76.7\\% accuracy ($+4.3$~pp, 95\\% CI $[0.0, +8.7]$; McNemar $p = 0.079$, not reaching $\\alpha{=}0.05$). The label distribution inverts: 30 internal-preferred vs.\\ 17 deterministic-preferred (cf.\\ 9:86 in ScienceWorld), with 84.3\\% no-preference. In the absence of death risk, the deterministic advantage vanishes---consistent with death avoidance as the primary driver. A complementary evaluation on ALFWorld ($N{=}135$) confirms that the counterfactual framework identifies different routing mechanisms across environments: the deterministic advantage there stems from information asymmetry (access to admissible actions) rather than death avoidance (Appendix~\\ref{app:cross-env}).\n\n\\paragraph{Penalty sensitivity.}\nThe $r = 0.97$ correlation is specific to catastrophic death (score $= -100$); defining ``failure'' as any non-positive score yields $r = -0.13$ ($p = 0.70$). The correlation emerges only at $P \\geq 50$ ($r = 0.86$) and reflects that non-death episodes show near-zero performance differential ($\\Delta_{\\text{nd}} = 2.84$; Appendix~\\ref{app:penalty}). Death is effectively the \\emph{only} component generating differential routing signal in ScienceWorld. These findings may be capability-dependent: the 42.9\\% internal death rate reflects a 7B model's hallucination vulnerability; larger models with lower death rates would reduce DAF, potentially revealing non-death routing signal currently masked by catastrophic failures.\n\n\\paragraph{Implications for router design.}\nThe dominance of death avoidance (DAF $= 90.4\\%$ at $P{=}100$) reframes modality routing as primarily a \\emph{safety} problem rather than an efficiency-quality tradeoff. The router functions as a safety critic---predicting which states lead to catastrophic failure under internal reasoning---aligning more closely with safe RL~\\citep{garcia2015comprehensive} than with cost-quality optimization~\\citep{cogrouter-2026, ares-2026}. The extreme label imbalance (86:9 deterministic-preferred, 150 no-preference) is not an artifact but a central result: among episodes where modality matters, deterministic is preferred at 9.6:1, explaining why always-deterministic is a strong baseline and why the trained router (\\S\\ref{sec:router-diagnostic}) adds no value. A lightweight death predictor may capture most routing benefit without full counterfactual labeling.\n",
      "numLines": 12,
      "startLine": 1,
      "totalLines": 12
    }
  },
  "sourceToolAssistantUUID": "0812bd2a-c966-4dec-bd65-a3381096a31c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/.claude/sessions/review_reviewer_2_ab9762a8",
  "sessionId": "5bc9ff02-4cf0-48f5-9df4-52d4a45b7804",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 38 · 2026-05-16T12:23:33.267Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Meu2R6PBKN7Jig6iaoR6oj`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f61cd32a-3dfa-46e8-8eaf-2d788ed2a384",
  "isSidechain": false,
  "requestId": "req_011Cb6EwdP3V6iL6L9WSvezK",
  "type": "assistant",
  "uuid": "29c274e0-0e77-4471-b31d-fe8683aa4f35",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/.claude/sessions/review_reviewer_2_ab9762a8",
  "sessionId": "5bc9ff02-4cf0-48f5-9df4-52d4a45b7804",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Rf1F4jt7xRHnK7E1ybz6Dq",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 18386,
      "cache_read_input_tokens": 27898,
      "output_tokens": 672,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 18386,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 672,
          "cache_read_input_tokens": 27898,
          "cache_creation_input_tokens": 18386,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 18386
          },
          "type": "message"
        }
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

_source line 39 · 2026-05-16T12:23:33.272Z_

<details><summary>↩ Tool result · `toolu_01Meu2R6PBKN7Jig6iaoR6oj`</summary>

```text
1	\section{Conclusion}
2	
3	We introduced episode-level counterfactual analysis for decomposing routing signal in modular LLM agents. Applied to 245 ScienceWorld episodes (11 of 30 task types, Qwen2.5-7B-Instruct), 78.9\% of non-tie routing labels (75 of 95) arise from death asymmetry. The DAF reaches $90.4\%$ (95\% CI: $[81.6\%, 98.8\%]$) at $P{=}100$, with strong cross-task correlation ($r = 0.97$, $p < 10^{-6}$).
4	
5	Cross-environment evidence supports this finding: on MATH ($N{=}300$), routing signal vanishes without death penalty, with a directional trend favoring internal reasoning ($+4.3$~pp, $p = 0.079$). An exploratory router trained on counterfactual labels achieves only $47.1 \pm 2.2\%$ on held-out episodes---below always-deterministic---a structural limitation confirmed by data and capacity scaling ablations.
6	
7	In environments with catastrophic failure modes, routing value is dominated by safety: the router functions as a safety critic rather than an efficiency optimizer. Open directions include step-level counterfactual labeling, stronger backbones with lower intrinsic death rates, and environments with graded failure costs.
8	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "29c274e0-0e77-4471-b31d-fe8683aa4f35",
  "isSidechain": false,
  "promptId": "2cc35627-090b-4e8e-873a-80e6ce7d766f",
  "type": "user",
  "uuid": "186f6bce-f336-4345-a107-f271c8d64246",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/conclusion.tex",
      "content": "\\section{Conclusion}\n\nWe introduced episode-level counterfactual analysis for decomposing routing signal in modular LLM agents. Applied to 245 ScienceWorld episodes (11 of 30 task types, Qwen2.5-7B-Instruct), 78.9\\% of non-tie routing labels (75 of 95) arise from death asymmetry. The DAF reaches $90.4\\%$ (95\\% CI: $[81.6\\%, 98.8\\%]$) at $P{=}100$, with strong cross-task correlation ($r = 0.97$, $p < 10^{-6}$).\n\nCross-environment evidence supports this finding: on MATH ($N{=}300$), routing signal vanishes without death penalty, with a directional trend favoring internal reasoning ($+4.3$~pp, $p = 0.079$). An exploratory router trained on counterfactual labels achieves only $47.1 \\pm 2.2\\%$ on held-out episodes---below always-deterministic---a structural limitation confirmed by data and capacity scaling ablations.\n\nIn environments with catastrophic failure modes, routing value is dominated by safety: the router functions as a safety critic rather than an efficiency optimizer. Open directions include step-level counterfactual labeling, stronger backbones with lower intrinsic death rates, and environments with graded failure costs.\n",
      "numLines": 8,
      "startLine": 1,
      "totalLines": 8
    }
  },
  "sourceToolAssistantUUID": "29c274e0-0e77-4471-b31d-fe8683aa4f35",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/.claude/sessions/review_reviewer_2_ab9762a8",
  "sessionId": "5bc9ff02-4cf0-48f5-9df4-52d4a45b7804",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 40 · 2026-05-16T12:23:33.933Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01Rwwt3JSb7RL5UgsXXe2CPz`</summary>

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
  "parentUuid": "186f6bce-f336-4345-a107-f271c8d64246",
  "isSidechain": false,
  "requestId": "req_011Cb6EwdP3V6iL6L9WSvezK",
  "type": "assistant",
  "uuid": "d5ee7d96-d480-4588-92a2-6bb7f8d21730",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/.claude/sessions/review_reviewer_2_ab9762a8",
  "sessionId": "5bc9ff02-4cf0-48f5-9df4-52d4a45b7804",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Rf1F4jt7xRHnK7E1ybz6Dq",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 18386,
      "cache_read_input_tokens": 27898,
      "output_tokens": 672,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 18386,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 672,
          "cache_read_input_tokens": 27898,
          "cache_creation_input_tokens": 18386,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 18386
          },
          "type": "message"
        }
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

_source line 41 · 2026-05-16T12:23:34.046Z_

```json
{
  "parentUuid": "44f993dc-8497-4e41-95f9-2265c75d49de",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "63e4f497-915e-483d-ba52-6be6b67bd012",
  "timestamp": "2026-05-16T12:23:34.046Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/.claude/sessions/review_reviewer_2_ab9762a8",
  "sessionId": "5bc9ff02-4cf0-48f5-9df4-52d4a45b7804",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 42_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[Round 8 审稿请求]: ## Round 8 审稿任务 — Reviewer 2（新颖性 + 完整性 + 写作质量）  ### Venue 信息 - **会议**: EMNLP 2026 (通过 ARR May 2026 cycle 提交) - **截止日期**: 2026-05-25 - **页数限制**: 正文 8 页 + 无限参考文献页 - **模板**: ACL LaTeX (`\\…",
  "leafUuid": "63e4f497-915e-483d-ba52-6be6b67bd012",
  "sessionId": "5bc9ff02-4cf0-48f5-9df4-52d4a45b7804"
}
```

---

### Runtime record

_source line 43_

```json
{
  "type": "ai-title",
  "aiTitle": "Review paper on modular routing with counterfactual analysis",
  "sessionId": "5bc9ff02-4cf0-48f5-9df4-52d4a45b7804"
}
```

---

### Assistant

_source line 44 · 2026-05-16T12:23:37.887Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the paper sections. Let me also fetch the ARR review form to get exact scoring criteria.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "63e4f497-915e-483d-ba52-6be6b67bd012",
  "isSidechain": false,
  "requestId": "req_011Cb6ExTqLyqftbtYmPhcNc",
  "type": "assistant",
  "uuid": "347eb526-7557-4c3d-b648-b306235af650",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/.claude/sessions/review_reviewer_2_ab9762a8",
  "sessionId": "5bc9ff02-4cf0-48f5-9df4-52d4a45b7804",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017ebryjud7kkBZPqu7CakTs",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 10844,
      "cache_read_input_tokens": 46284,
      "output_tokens": 173,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 10844,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 173,
          "cache_read_input_tokens": 46284,
          "cache_creation_input_tokens": 10844,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 10844
          },
          "type": "message"
        }
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

_source line 45 · 2026-05-16T12:23:38.375Z_

获取 ARR review form 的详细评分标准。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "347eb526-7557-4c3d-b648-b306235af650",
  "isSidechain": false,
  "requestId": "req_011Cb6ExTqLyqftbtYmPhcNc",
  "type": "assistant",
  "uuid": "ecc781d6-8133-42f3-9821-2ad23a61e160",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/.claude/sessions/review_reviewer_2_ab9762a8",
  "sessionId": "5bc9ff02-4cf0-48f5-9df4-52d4a45b7804",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017ebryjud7kkBZPqu7CakTs",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 10844,
      "cache_read_input_tokens": 46284,
      "output_tokens": 173,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 10844,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 173,
          "cache_read_input_tokens": 46284,
          "cache_creation_input_tokens": 10844,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 10844
          },
          "type": "message"
        }
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

_source line 46 · 2026-05-16T12:23:41.981Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01EdtGcxsk17R2Kr8ai46BKk`</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract the complete review form criteria, scoring scales, and descriptions for each dimension (soundness, excitement, overall assessment, confidence, etc.). List each dimension with its scale and description."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ecc781d6-8133-42f3-9821-2ad23a61e160",
  "isSidechain": false,
  "requestId": "req_011Cb6ExTqLyqftbtYmPhcNc",
  "type": "assistant",
  "uuid": "48ccbac4-5835-4603-99c9-cbe881bf59bb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/.claude/sessions/review_reviewer_2_ab9762a8",
  "sessionId": "5bc9ff02-4cf0-48f5-9df4-52d4a45b7804",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017ebryjud7kkBZPqu7CakTs",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 10844,
      "cache_read_input_tokens": 46284,
      "output_tokens": 173,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 10844,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 173,
          "cache_read_input_tokens": 46284,
          "cache_creation_input_tokens": 10844,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 10844
          },
          "type": "message"
        }
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

_source line 47 · 2026-05-16T12:23:47.873Z_

<details><summary>↩ Tool result · `toolu_01EdtGcxsk17R2Kr8ai46BKk`</summary>

```text
# ACL Rolling Review Form - Evaluation Dimensions

## Reviewer Confidence
**Scale: 1-5**
- 5: "Positive that my evaluation is correct. I read the paper very carefully"
- 4: Quite sure with unlikely errors
- 3: Pretty sure but possible oversights
- 2: Defensible but likely missed details
- 1: Outside expertise or incomprehensible paper

## Soundness
**Scale: 1-5 (increments of 0.5)**
- 5: "Excellent: This study is one of the most thorough I have seen"
- 4: Strong support for claims; minor experiments optional
- 3: Acceptable support for main claims; minor details needed
- 2: Main claims lack sufficient support; major technical issues
- 1: "Major Issues: This study is not yet sufficiently thorough to warrant publication"

## Excitement
**Scale: 1-5 (increments of 0.5)**
- 5: Highly exciting; would recommend widely
- 4: Exciting; would mention to colleagues
- 3: Interesting; might attend presentation
- 2: Potentially interesting but limited personal resonance
- 1: No resonance; lacks relevance to computational linguistics

## Overall Assessment
**Scale: 1-5 (increments of 0.5)**
- 5: Consider for Award (top 2.5%)
- 4: Conference acceptance
- 3: Findings acceptance
- 2: Resubmit next cycle
- 1: Do not resubmit

## Additional Dimensions
- **Reproducibility** (1-5 scale)
- **Datasets** (1-5 scale)
- **Software** (1-5 scale)
- **Author Identity Knowledge** (1-5 scale)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "48ccbac4-5835-4603-99c9-cbe881bf59bb",
  "isSidechain": false,
  "promptId": "2cc35627-090b-4e8e-873a-80e6ce7d766f",
  "type": "user",
  "uuid": "7566b145-3ee9-49b4-a4ba-e9ae63da6d74",
  "toolUseResult": {
    "bytes": 25365,
    "code": 200,
    "codeText": "OK",
    "result": "# ACL Rolling Review Form - Evaluation Dimensions\n\n## Reviewer Confidence\n**Scale: 1-5**\n- 5: \"Positive that my evaluation is correct. I read the paper very carefully\"\n- 4: Quite sure with unlikely errors\n- 3: Pretty sure but possible oversights\n- 2: Defensible but likely missed details\n- 1: Outside expertise or incomprehensible paper\n\n## Soundness\n**Scale: 1-5 (increments of 0.5)**\n- 5: \"Excellent: This study is one of the most thorough I have seen\"\n- 4: Strong support for claims; minor experiments optional\n- 3: Acceptable support for main claims; minor details needed\n- 2: Main claims lack sufficient support; major technical issues\n- 1: \"Major Issues: This study is not yet sufficiently thorough to warrant publication\"\n\n## Excitement\n**Scale: 1-5 (increments of 0.5)**\n- 5: Highly exciting; would recommend widely\n- 4: Exciting; would mention to colleagues\n- 3: Interesting; might attend presentation\n- 2: Potentially interesting but limited personal resonance\n- 1: No resonance; lacks relevance to computational linguistics\n\n## Overall Assessment\n**Scale: 1-5 (increments of 0.5)**\n- 5: Consider for Award (top 2.5%)\n- 4: Conference acceptance\n- 3: Findings acceptance\n- 2: Resubmit next cycle\n- 1: Do not resubmit\n\n## Additional Dimensions\n- **Reproducibility** (1-5 scale)\n- **Datasets** (1-5 scale)\n- **Software** (1-5 scale)\n- **Author Identity Knowledge** (1-5 scale)",
    "durationMs": 5886,
    "url": "https://aclrollingreview.org/reviewform"
  },
  "sourceToolAssistantUUID": "48ccbac4-5835-4603-99c9-cbe881bf59bb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/.claude/sessions/review_reviewer_2_ab9762a8",
  "sessionId": "5bc9ff02-4cf0-48f5-9df4-52d4a45b7804",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 48 · 2026-05-16T12:27:38.165Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the paper content and the reviewer guidelines. Let me compile my review.

Let me check the key issues from the previous round:

**Critical (必须验证)**:
- **R6-C1**: DAF=90.4% 是否仍作为 headline number？78.9% 是否被提升为同等重要的 penalty-independent metric？
- **R7-N1**: ALFWorld (Table 3, N=135) — 是否添加了完整方法论描述（model, deterministic modality definition, labeling process, episode length）？


- **R6-W8**: Safe RL literature — 是否添加了 1-2 个 specific safety critic 引用（CPO, CRPO, safety Q-functions 等）来支持 §5 "router = safety critic" claim？
- **R7-W1**: MATH p=0.079 — "routing signal vanishes" 是否改为了更审慎的措辞？
- **R7-W2**: Llama pilot N=10 — 是否从 Contribution 列表中移除？是否降级为 directional observation？
- **R7-W5**: Missing references — RouteLLM (Ong 2024), Reflexion (Shinn 2023), tool-learning survey (Qu 2024) 是否已添加？

现在检查一些关键细节：**R7-m1** 中 retool-2026 和 dynathink-2025 的元数据是否修正了，**R7-m2** 中 Abstract 的 DAF 精度是否调整为 ~90%，GPU 描述是否泛化了，以及 **R7-m3** 中 find-non-living-thing 的 40 episodes 是否有合理解释，code/data release 计划是否明确。现在看一下 Abstract 中关于非平局路由标签的部分。

78.9% 的非平局标签现在被明确标记为"penalty-independent metric"，并与 DAF 90.4% 并列呈现。在引言和方法部分也都强调了这一点，确认死亡规避在不同惩罚幅度下都主导了路由信号。这个修改看起来已经完成了。现在检查 ALFWorld 在附录 A.9 中的内容。

他们在 json_2.1.1 split 上评估了 135 个游戏，使用 Qwen2.5-7B-Instruct，内部策略只接收自由文本观察，而确定性策略还能获得每一步的可行动作。ALFWorld 没有死亡惩罚——失败就是耗尽步数预算，所以标签会根据这个约束来应用通用的 Algorithm 1 框架。

在相关工作中，他们现在引用了 CRPO 作为具体的安全约束优化方法，补充了 Garcia 2015 的综述。

对于 MATH 数据集（300 个样本），他们发现没有死亡惩罚时路由信号消失，但内部推理有轻微的正向趋势（+4.3 个百分点，p = 0.079，未达到显著性水平）。

问题在于摘要和结论中仍然说"路由信号消失"，但 p 值为 0.079 是边界情况，95% 置信区间 [0.0, +8.7] 的下界为 0，表示几乎没有效应，这种表述方式有问题。

"消失"这个词对于非显著结果来说过于绝对，应该改为"确定性优势不存在"或"死亡驱动的路由信号未被观察到"。实际上，他们似乎是指"没有死亡惩罚时，死亡驱动的路由信号消失"，因为在 MATH 中没有死亡惩罚。路由信号并没有完全消失，而是反向了。所以措辞不够精确。再仔细看摘要，它说的是确定性路由信号消失了，标签分布从 86:9（偏好确定性）反转到 30:17（内部推理方向上更优）。

但"路由信号消失"具有误导性，因为确实存在信号，只是方向不同。问题在于框架：p=0.079 的结果没有达到显著性，所以说信号从 86:9"反转"到 30:17 也是过度解读。30:17 与噪声相容。

在结论中，他们写的是"没有死亡惩罚时路由信号消失，有利于内部推理的方向趋势（+4.3 pp，p = 0.079）"。这样更好——用"方向趋势"和 p 值进行了限定。但"消失"这个词对于可能仍存在路由信号（只是不显著）的结果来说仍然过强。所以 R7-W1 是部分修复的——他们添加了"方向趋势"和"未达到 α=0.05"的限定词，但"消失"这个词仍然被使用。

现在看 R7-W2：Llama 试点 N=10。检查贡献列表，第 3 项提到"跨上下文验证。在 MATH（N=300）...在 ALFWorld（N=135）..."，没有提到 Llama。好的。在实验部分，他们说"Llama-3.1-8B 试点（N=10）显示方向一致的死亡模式"，在引言中也提到了这个 N=10 的试点，暗示这种现象不仅限于特定模型。

现在措辞已经恰当地加了限定条件。

R7-W5 检查缺失的参考文献：RouteLLM、Reflexion 和工具学习综述都已在参考书目中并在相应位置引用。都解决了。

现在检查 R7-m1 关于 retool 的关键词/年份和 dynathink 作者的问题。

retool 的关键词是 `retool-2025`，年份是 2025，这看起来是对的。对于 dynathink，OpenAlex 验证显示作者解析可能存在差异——"Yu, Xiao" 中 Yu 是姓氏，Xiao 是名字，但 API 可能以不同方式解析了中文名字，这可能只是验证工具的误报。

对于 R7-m2 的摘要，他们保留了精确的 DAF 数值 90.4%，并包含了置信区间，这是可以接受的。GPU 描述提到大约 40 个 GPU 小时。

R7-m3 中关于 find-non-living-thing 任务的 40 个 episode，附录解释了这是因为数据分两批收集，第二批增加了 20 个 episode 来提高这个零死亡异常值的统计功效。代码和数据会在论文被接受后发布。

现在看一下论文的主要贡献，特别是 episode 级别的反事实分析方法。

这种方法本身相对直接——运行两种策略并比较结果——但应用到路由信号分解上有一定新颖性。DAF 指标本质上是一个比率分解（1 - Δ_nd/Δ_full），虽然有用但作为指标的新颖性有限。DAF 对惩罚参数的依赖性限制了它的独立价值，不过它通过量化对分数差距的贡献比例，相比简单的死亡率比较还是有优势的。路由器训练失败作为负面结果虽然有趣，但在负面结果文献中已经是公认的现象。

更有价值的贡献在于他们诊断了失败的原因——DAF 主导性表明总是确定性策略已接近最优——这比失败本身更有意义。

现在检查相关工作的覆盖范围，RouteLLM、工具学习综述、Reflexion 和安全强化学习的相关论文都已引用，但可能还需要补充一些更近期的工作。

CRPO 的加入是个改进，不过 CPO 仍然缺失。2025-2026 年的并发路由工作涵盖得很全面，包括 CogRouter、ARES、MoR 等多个相关研究，虽然 HybridLLM 和 FrugalGPT 这样的路由工作可能也值得考虑，但它们的直接相关性可能较低。

现在看 MATH 数据集上的结果，p 值为 0.079，抽象部分提到"没有死亡惩罚时路由信号消失"。

跨越摘要、引言、讨论和结论各部分，我看到一致的模式：内部推理相比代码解释器有 +4.3 个百分点的优势，但这个差异没有达到统计显著性水平（p = 0.079，未达到 α = 0.05），95% 置信区间是 [0.0, +8.7]。

我需要确保所有部分都准确反映这一点，特别是避免过度陈述"路由信号消失"——应该更精确地说是"死亡驱动的路由信号消失"或"确定性优势消失"。结论部分还需要补充"未达到 α = 0.05"这个重要的统计限定词，以与摘要和引言保持一致。

关于 95% 置信区间 [0.0, +8.7]，下界恰好为 0.0 这一点确实处于边界，需要谨慎解释。

在 ALFWorld 方法论中，虽然论文描述了环境设置和模型选择，但有两个细节需要澄清：首先，"确定性模态"实际上反映的是信息获取的不对称性而非计算模式的改变，这个重要的区别应该在讨论部分更加突出；其次，由于 ALFWorld 中不存在死亡机制，标签化过程会直接进行分数比较，这一点虽然隐含在文中但应该更明确地说明。

关于论文的整体组织，摘要部分篇幅较长，接近 200 字，已经达到 ACL 指南建议范围的上限。虽然信息密度很高，但试图涵盖的内容过多，可能需要进一步精简和重点突出。 The Llama pilot is framed as preliminary evidence in the introduction rather than a core contribution, which is the right call—it supports the generalizability claim without overstating the scope of the work.

Now checking the formatting and bibliography. The paper follows ACL template requirements with proper anonymization and a limitations section. There are a few bibliography quirks: three entries that are cited in the bib file but not referenced in the actual text, a potential author name parsing issue with one Chinese name, and a couple of well-known papers that didn't resolve through the API lookup—these are minor issues that don't substantially affect the submission.

For the year discrepancies, some are just the difference between preprint and publication dates, which is normal. The survey entry needs clarification on whether to use the 2024 arXiv date or the 2025 venue publication date. Now let me check the page count.

The paper structure suggests it's substantial — with an abstract, introduction, three-part method section, three-part experiments, related work, discussion, conclusion, limitations, and ethics statement. I can't verify the exact page count without compiling, but it appears to fit within the 8-page limit for the main body.

Checking for anonymity issues, the author field says "Anonymous" and I don't see any identifying information in the ethics statement or elsewhere — just generic details about GPU usage and a standard note about releasing code upon acceptance.

Now I'll start drafting the review, but first let me double-check my reference verification to make sure I have the orphan entries right.

Looking at the bibliography, there are three unused references: toolkengpt-2023, tot-2023, and voyager-2023. These are just sitting in the bib file without being cited anywhere, which is sloppy but not a submission problem. On the flip side, all the citations in the paper have corresponding entries, so there are no missing references.

For the novelty question, I need to think more carefully about what's actually new here. The core method is straightforward — run tasks under both strategies, compare outcomes, and break down the score difference into death versus non-death components. It's effective, but counterfactual evaluation in RL isn't new; they cite prior work on this. Their angle is doing this at the episode level rather than the action level, which is their distinction from earlier approaches.

But here's the thing: episode-level comparison of different policies is just policy comparison. The counterfactual aspect comes from both policies starting from the same initial state, which is standard practice in paired experiments. The real novelty seems to be in the application — using this to decompose the routing signal rather than in the method itself.

The DAF metric is essentially a variance decomposition or attribution formula. It's a natural statistical decomposition, nothing deeply novel there, but it cleanly answers a specific question about how much of the routing benefit comes from death avoidance. The router failure result is interesting as a negative finding — the trained router can't beat always-deterministic, which makes sense given that 90.4% of the signal comes from death avoidance alone.

Overall, this feels like an insight paper rather than a methods contribution. The empirical finding is solid and well-executed, but the limited scope — one environment, one model primarily — makes it borderline for a venue like EMNLP. The generalization question is the real weakness here.

The "router as safety critic" framing in the discussion is interesting but oversells the evidence. They're reinterpreting their findings through a safe RL lens without actually building a safety critic or empirically connecting to safe RL methods like CRPO. It's a reasonable discussion point but shouldn't be presented as a core claim.

Now I need to think through my scoring more systematically. The experimental design is solid — clean counterfactual setup, proper confidence intervals, multiple ablations — and the DAF decomposition is mathematically sound.

But there are real limitations. The findings rest heavily on ScienceWorld with its specific death penalty mechanic, and that r=0.97 correlation is partly just mechanical since death penalties directly affect scores. The MATH environment doesn't show significant results, and ALFWorld reveals a completely different mechanism at play, which actually undermines the generalizability of the death-avoidance story.

For soundness I'm settling on 3.5/5 — the work is technically competent but the scope is narrow and the key finding depends too much on one environment's particular structure.

On excitement, the insight is somewhat limited. Death avoidance as a routing signal is interesting in isolation, but it's specific to one environment with a particular failure mode. The practical takeaway — just use a death predictor instead of a full router — is sensible but never actually demonstrated. I'd rate that 2.5/5.

The paper itself is well-executed and honest about what it can and can't claim, which I appreciate. The analysis goes deep within its scope. The real question is whether that scope is broad enough to matter.

For a venue like EMNLP, this reads as borderline Findings material rather than main conference. The negative result about router failure is thoroughly analyzed but not particularly surprising given everything else in the paper. I'm thinking 3/5 overall.

Now I need to write up the full review. Actually, let me double-check the abstract length first — it looks quite long, probably 250-300 words, which is well above the typical 200-word guidance. I should note that in my review.

I'm also noticing some sloppiness in how the results are presented. The conclusion claims the routing signal "vanishes without death penalty," but the actual p-value is 0.079 — that's not statistically significant, so "vanishes" overstates it. The abstract and introduction are careful to note this doesn't reach α=0.05, but the conclusion drops that qualifier, which is inconsistent and misleading.

The paper does acknowledge the artificial nature of ScienceWorld's death penalty in the limitations and discussion sections, noting how the -100 point penalty amplifies the effect and that real environments with softer penalties would show lower values. That's good.

Now I'm checking the reference verification — there's a naming convention issue with the dynathink-2025 citation where the author field shows "Yu, Xiao and others" but OpenAlex parses it differently, likely because of how Chinese names are formatted in the bibliography. This is the same issue flagged before, and the bib format itself appears correct for that naming convention.

The tool-learning-survey-2024 has a year mismatch between the bib (2024) and OpenAlex (2025), which could be an arXiv versus official publication discrepancy. I also found three unused references that should be removed.

The retool citation was previously flagged as needing correction from 2026 to 2025, and I can confirm it's now properly set to 2025 and verified by OpenAlex, so that's been fixed.

For the ALFWorld methodology, I need to verify whether the paper provides complete descriptions of the model, deterministic modality definition, labeling process, and episode length as requested.

The model is clearly specified as Qwen2.5-7B-Instruct, the deterministic modality is well-defined with the information asymmetry explanation, and the episode length is capped at 50 steps. The labeling process for ALFWorld isn't explicitly detailed—it appears to follow Algorithm 1 but without the death condition, so it only compares scores, which is implied rather than stated outright.

Looking more carefully at the ALFWorld section, I see "binary success metric" mentioned, which clarifies that the labeling uses Algorithm 1's score comparison branch where success equals 1 and failure equals 0. This means if one strategy succeeds and the other fails, it's labeled as preferred; if both succeed or both fail, there's no preference. That resolves the ambiguity.

Now checking whether the paper explains why "find-non-living-thing" has 40 episodes—Appendix A.2 indicates the data came from two collection batches, with the second batch adding 20 episodes to boost statistical power for this particular task.

I should assess the writing quality before drafting the full review. The paper is generally clear and well-structured, moving logically from problem setup through methods and experiments. The authors are transparent about DAF's penalty-dependent limitations and present the penalty-independent alternative at 78.9%. Notation stays consistent throughout, though some sentences in the abstract are unnecessarily long and complex.

Before finalizing, I want to verify the cross-model generalization claim in the introduction—specifically contribution 3 about cross-context validation on MATH where no death penalty exists.

Looking at the evidence: on MATH, internal reasoning outperforms code by 4.3 percentage points but doesn't reach statistical significance (p = 0.079). On ALFWorld, deterministic success dominates at 27.4% versus 3.0% for internal reasoning, but this stems from information asymmetry rather than death avoidance. Both cases confirm the ScienceWorld effect is about failure structure, not inherent advantages of deterministic approaches. The introduction does mention a preliminary cross-model pilot with Llama-3.1-8B showing directionally consistent death patterns within ScienceWorld, though they acknowledge full-scale multi-model validation is future work.

Now I need to clarify what "routing signal vanishes" actually means in the abstract—specifically whether it refers to the death-driven routing signal disappearing when the penalty is removed.

The phrasing is genuinely problematic because it claims the routing signal vanishes while simultaneously reporting a directional trend favoring internal reasoning, which is contradictory. The most reasonable interpretation is that the deterministic routing advantage from ScienceWorld disappears in MATH, but the language obscures this and would rightfully draw scrutiny from a reviewer.

R7-W1 already flagged this issue, and while the revision added qualifiers about the directional trend and statistical significance, it left "vanishes" unchanged—so this is only partially addressed.

Now I'm noticing a more fundamental problem: the definition of "deterministic modality" shifts across environments. In ScienceWorld it means ground-truth observations, in MATH it's a code interpreter, and in ALFWorld it's admissible actions—three entirely different mechanisms. The paper acknowledges this distinction for ALFWorld but not for MATH, which undermines the validity of comparing routing patterns across these environments.

There's also the issue of task selection in ScienceWorld: excluding 63% of tasks because both strategies time out seems to contradict the anti-cherry-picking argument, even if death rates are comparable between included and excluded sets. And the high DAF values appear mechanically driven by the penalty structure—with P=100 and δ≈0.27, the formula naturally produces DAF around 90%, so the effect size is partly an artifact of how the metric is constructed.

The paper does acknowledge this through penalty sensitivity analysis and by reporting the penalty-independent label fraction (78.9%), which I'd count as a strength. But the statistical power is concerning: only 11 task types with roughly 8.6 non-tie labels each gives just 11 data points for correlation analysis, and the MATH results show underpowered detection (p=0.079) for the claimed effect size.

On the "safety critic" framing, the paper's own finding contradicts this—always-deterministic being optimal isn't a safety critic actively constraining behavior, it's just defaulting to the safer option. A true safety critic would selectively intervene when needed, which is what the failed router was supposed to do.

Looking at the full picture, this is a focused empirical contribution showing that death avoidance dominates routing in ScienceWorld, with thorough analysis and good presentation. But the scope is narrow—primarily one environment and one model—so the generalizability is questionable. The core insight about safety dominating routing signal may not hold in environments without such extreme penalty structures. I'd rate this around 3.0/5 for findings acceptance.

Actually, bumping that to 4/5. Now let me write out the full review.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7566b145-3ee9-49b4-a4ba-e9ae63da6d74",
  "isSidechain": false,
  "requestId": "req_011Cb6EyUzpfG5bsfvhgY1FR",
  "type": "assistant",
  "uuid": "edbfa1f3-9f2d-4fd1-96af-063ae919a950",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/.claude/sessions/review_reviewer_2_ab9762a8",
  "sessionId": "5bc9ff02-4cf0-48f5-9df4-52d4a45b7804",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01P3fAgKVSJfC5LL7vGeq7XE",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 605,
      "cache_read_input_tokens": 57128,
      "output_tokens": 15664,
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
          "output_tokens": 15664,
          "cache_read_input_tokens": 57128,
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

_source line 49 · 2026-05-16T12:28:54.032Z_

全部材料已读完。现在编写审稿意见。

---

## Round 8 审稿意见 — Reviewer 2

### 1. Summary

本文提出 episode-level counterfactual analysis 方法来分解模块化 LLM agent 中的 routing signal，发现在 ScienceWorld 环境中，78.9% 的非 tie routing label 源于 death asymmetry（penalty-independent），DAF 在 $P=100$ 下达到 90.4%。论文进一步展示 trained router 无法超越 always-deterministic baseline（47.1% vs 50.0% episode-level），并通过 MATH 和 ALFWorld 的 cross-environment 分析提供支撑证据。整体是一篇聚焦的 empirical insight paper，分析严谨但范围受限。

### 2. Strengths

- **S1**: 双指标设计（penalty-independent 的 78.9% label fraction + penalty-dependent DAF）比前版本显著改善了核心发现的可信度，读者可以自行判断 penalty 选择的影响。
- **S2**: Router failure 的诊断非常彻底——data scaling（32×）、capacity scaling（0.6B–4B）、per-task-type breakdown、classification head vs. SFT 对比——系统排除了简单假设，形成强力的 negative result。
- **S3**: Penalty sensitivity analysis（Appendix A.4, Table 5–6）和 mechanism boundary（threshold-specific correlation, $r=0.97$ at $P=100$ vs $r=-0.13$ at $T=0$）深化了 insight 的边界条件。
- **S4**: Related work 现在覆盖全面——RouteLLM、Reflexion、tool-learning survey、CRPO 均已纳入；2025–2026 concurrent routing 工作覆盖到位（6 篇）。
- **S5**: Limitations section 诚实且具体——19 个排除 task types、episode-level label 的局限性、DAgger distribution shift、Llama pilot 的统计不足都被明确承认。

### 3. Weaknesses

**W1 [Should-Fix]** "routing signal vanishes" 措辞仍然 overstate non-significant result

Abstract 和 Conclusion 均写 "routing signal vanishes without a death penalty"，但 MATH 结果是 $p=0.079$（未达 $\alpha=0.05$），95% CI $[0.0, +8.7]$。"vanishes" 暗示 signal 不存在，但 30:17 的 label distribution 和 +4.3 pp 的 directional trend 恰恰说明存在 signal——只是方向反转且未达显著。更准确的措辞应为 "the deterministic advantage disappears" 或 "death-driven routing signal is absent"。此外，Conclusion 中 "$p = 0.079$" 后缺少 "not reaching $\alpha=0.05$" 的 hedge（Abstract 和 Introduction 中有此限定），造成叙事不一致。

**W2 [Should-Fix]** "Deterministic modality" 定义跨环境不一致，削弱 cross-environment 比较的说服力

ScienceWorld 中 deterministic = ground-truth observations（perfect dynamics model）；MATH 中 = code interpreter；ALFWorld 中 = admissible actions access。论文对 ALFWorld 明确标注了 "information asymmetry rather than a computation mode switch"（Appendix A.9），但 MATH 的 code interpreter 同样不是 ScienceWorld 意义上的 "deterministic computation"——它引入了代码生成、执行、debugging 等额外变量。Discussion §5 第一段将三个环境并列作为 "cross-environment evidence"，却未讨论 modality 定义的异质性对结论可迁移性的影响。建议在 Method 或 Discussion 中增加一段明确 modality 在各环境中的操作化定义，并讨论这一差异如何影响 DAF 的跨环境可比性。

**W3 [Should-Fix]** 11/30 task types 选择的 generalizability concern 未充分回应

63% 的 ScienceWorld task types 被排除（"both strategies time out"）。Appendix A.2 论证了 included vs excluded 的 death rate 相似（17.8% vs 14.9%），但这仅说明 death rate 无 selection bias，不能说明 routing signal 的结构相似。排除的 task types 可能存在不同的 failure modes（如 timeout 而非 death），其 routing signal 结构可能完全不同。论文的 central claim "death avoidance accounts for X% of routing signal" 实际上只适用于 "有 routing signal 的 task types"，但这一限定在 Abstract 和 Conclusion 中的表述不够显著。

**W4 [Minor]** Abstract 信息过载

Abstract 约 250 词，包含 DAF、penalty sensitivity range、78.9%、router training 结果、MATH、Llama pilot——信息密度高到几乎是 extended abstract。建议删减 penalty sensitivity range 和 Llama pilot 的 mention，专注于核心发现和最重要的验证结果。

**W5 [Minor]** "Safety critic" 类比过度延伸

Discussion 将 router 比作 "safety critic"（safe RL 中的术语），但 safe RL 中的 safety critic 是主动学习的约束机制，而本文的发现是 always-deterministic 就是最优策略——这更像是 "default to safe modality"，而非 learned safety critic。CRPO 的引用确认了 safe RL 的相关性，但类比本身不够精确。

**W6 [Minor]** Bib 中有 3 个 orphan entries

`toolkengpt-2023`、`tot-2023`、`voyager-2023` 在 bib 中存在但未被引用。`tool-learning-survey-2024` 的 bib year 为 2024，但 OpenAlex 记录为 2025 出版——应核实并统一。

### 4. 上轮 Issue 验证结果

| Issue | 状态 | 说明 |
|-------|------|------|
| **R6-C1** DAF 90.4% headline + 78.9% 提升 | **[RESOLVED]** | 78.9% 现在在 Abstract/Intro/Method/Experiments 中均先于或与 DAF 并列出现，明确标注 "penalty-independent metric"。双指标设计是本轮最重要的改进。 |
| **R7-N1** ALFWorld 方法论描述 | **[RESOLVED]** | Appendix A.9 现包含 model (Qwen2.5-7B)、deterministic modality 定义（admissible actions）、episode count (135)、max steps (50)、success metric (binary)。labeling process 通过 Algorithm 1 隐式覆盖。 |
| **R6-W8** Safe RL specific citation | **[RESOLVED]** | CRPO (Xu et al., 2021) 已添加至 Related Work §Safe RL 段落，与 Garcia 2015 survey 互补。 |
| **R7-W1** MATH "routing signal vanishes" 措辞 | **[PARTIALLY FIXED]** | 已添加 "directional trend" 和 "not reaching α=0.05" 限定（Abstract/Intro/Discussion），但 "vanishes" 一词仍保留在 Abstract 和 Conclusion 中，且 Conclusion 缺少 "not reaching α=0.05" hedge。见 W1。 |
| **R7-W2** Llama pilot 从 Contribution 列表移除 | **[RESOLVED]** | Contribution 列表中无 Llama/cross-model claim。Introduction 中降级为 "preliminary pilot" + "directionally consistent" + "though full-scale multi-model validation remains future work"。 |
| **R7-W5** 缺失 references | **[RESOLVED]** | RouteLLM (routellm-2024)、Reflexion (reflexion-2023)、tool-learning survey (tool-learning-survey-2024) 均已添加并在 Related Work 中引用。 |
| **R7-m1** retool key/year, dynathink author | **[RESOLVED]** | `retool-2025` key 和 year 已修正（OpenAlex 验证通过）。`dynathink-2025` author "Yu, Xiao" 符合中文姓名格式（Yu 为姓），OpenAlex 的 "xiao" 匹配是 API 解析差异，非实际错误。 |
| **R7-m2** Abstract DAF 精度 + GPU 描述 | **[RESOLVED]** | DAF 90.4% 保留精确值但附 CI [81.6%, 98.8%]；Ethics Statement 改为 "two consumer GPUs"（已泛化）。 |
| **R7-m3** find-non-living-thing 40 eps 解释 + code/data release | **[RESOLVED]** | Table 4 脚注解释了 "data was collected in two batches"；Ethics Statement 明确 "Code and data will be released upon acceptance"。 |

### 5. Missing References

核心 references 已覆盖。可选改进：
- **FrugalGPT** (Chen et al., 2023) / **HybridLLM** (Ding et al., 2024)——cost-quality routing 的先驱工作，与 "routing as safety vs efficiency" 的 framing 直接相关，可加入 §Adaptive Computation and Routing 段落。
- Safe RL 部分现有 Garcia 2015 survey + CRPO 2021，已满足最低要求。若要加强 "safety critic" 类比，可考虑引用 safety Q-functions 或 CPO (Stooke et al., 2020) 等具体实现。

### 6. Questions for Authors

**Q1**: MATH 中 code interpreter 作为 "deterministic modality" 与 ScienceWorld 中 ground-truth observations 的类比是否成立？Code interpreter 本身有 failure modes（syntax error、runtime error），这如何影响 DAF 跨环境可比性？

**Q2**: 19 个被排除的 task types 中，有多少因 timeout 而非 death 失败？如果 timeout 也是一种 "catastrophic failure"（agent 完全无法完成任务），DAF 分析是否应将其纳入？

**Q3**: Discussion 中说 "larger models with lower death rates would reduce DAF, potentially revealing non-death routing signal currently masked by catastrophic failures"——这是否意味着本文的核心发现（death avoidance dominance）可能是 model capability 的 artifact 而非 environment structure 的 fundamental property？

### 7. Overall Assessment

**Overall**: 3.0/5 (Findings acceptance)

**Confidence**: 4/5

**Rationale**: 论文在其选定范围内做了扎实的实验分析——DAF 分解、router diagnostic、penalty sensitivity、cross-environment checks 构成了一套完整的 evidence chain。Round 6–7 的关键问题（DAF vs 78.9% 双指标、ALFWorld 方法论、missing references）已全部修复。

阻碍 main conference acceptance 的主要因素：(1) 核心发现绑定于 ScienceWorld 的特定 failure structure（$-100$ death penalty），generalizability 有限；(2) episode-level counterfactual analysis 方法论本身较为直接（paired comparison under two policies），方法创新性不足以单独支撑贡献；(3) MATH 的 cross-environment validation 未达统计显著性，且 "deterministic modality" 在三个环境中定义不一致，削弱了 cross-environment 叙事。作为 Findings paper，insight 的清晰度和分析的彻底性达到了 publishable 水平。

---

将审稿意见提交给 Review Director。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "edbfa1f3-9f2d-4fd1-96af-063ae919a950",
  "isSidechain": false,
  "requestId": "req_011Cb6EyUzpfG5bsfvhgY1FR",
  "type": "assistant",
  "uuid": "24ac1b19-c185-4df3-9d7b-ab9d7836d060",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/.claude/sessions/review_reviewer_2_ab9762a8",
  "sessionId": "5bc9ff02-4cf0-48f5-9df4-52d4a45b7804",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01P3fAgKVSJfC5LL7vGeq7XE",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 605,
      "cache_read_input_tokens": 57128,
      "output_tokens": 15664,
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
          "output_tokens": 15664,
          "cache_read_input_tokens": 57128,
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

_source line 50 · 2026-05-16T12:29:25.016Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director · `toolu_01XMvkCooQmMbqznm9aeRUuC`</summary>

```json
{
  "text": "## Round 8 审稿意见 — Reviewer 2（新颖性 + 完整性 + 写作质量）\n\n### 1. Summary\n\n本文提出 episode-level counterfactual analysis 方法来分解模块化 LLM agent 中的 routing signal，发现在 ScienceWorld 环境中，78.9% 的非 tie routing label 源于 death asymmetry（penalty-independent），DAF 在 P=100 下达到 90.4%。论文进一步展示 trained router 无法超越 always-deterministic baseline（47.1% vs 50.0% episode-level），并通过 MATH 和 ALFWorld 的 cross-environment 分析提供支撑证据。整体是一篇聚焦的 empirical insight paper，分析严谨但范围受限。\n\n### 2. Strengths\n\n- **S1**: 双指标设计（penalty-independent 的 78.9% label fraction + penalty-dependent DAF）比前版本显著改善了核心发现的可信度，读者可以自行判断 penalty 选择的影响。\n- **S2**: Router failure 的诊断非常彻底——data scaling（32×）、capacity scaling（0.6B–4B）、per-task-type breakdown、classification head vs. SFT 对比——系统排除了简单假设，形成强力的 negative result。\n- **S3**: Penalty sensitivity analysis（Appendix A.4, Table 5–6）和 mechanism boundary（threshold-specific correlation, r=0.97 at P=100 vs r=-0.13 at T=0）深化了 insight 的边界条件。\n- **S4**: Related work 现在覆盖全面——RouteLLM、Reflexion、tool-learning survey、CRPO 均已纳入；2025–2026 concurrent routing 工作覆盖到位（6篇）。\n- **S5**: Limitations section 诚实且具体——19 个排除 task types、episode-level label 的局限性、DAgger distribution shift、Llama pilot 的统计不足都被明确承认。\n\n### 3. Weaknesses\n\n**W1 [Should-Fix]** \"routing signal vanishes\" 措辞仍然 overstate non-significant result\n\nAbstract 和 Conclusion 均写 \"routing signal vanishes without a death penalty\"，但 MATH 结果是 p=0.079（未达 α=0.05），95% CI [0.0, +8.7]。\"vanishes\" 暗示 signal 不存在，但 30:17 的 label distribution 和 +4.3 pp 的 directional trend 恰恰说明存在 signal——只是方向反转且未达显著。更准确的措辞应为 \"the deterministic advantage disappears\" 或 \"death-driven routing signal is absent\"。此外，Conclusion 中 \"p = 0.079\" 后缺少 \"not reaching α=0.05\" 的 hedge（Abstract 和 Introduction 中有此限定），造成叙事不一致。\n\n**W2 [Should-Fix]** \"Deterministic modality\" 定义跨环境不一致，削弱 cross-environment 比较的说服力\n\nScienceWorld 中 deterministic = ground-truth observations（perfect dynamics model）；MATH 中 = code interpreter；ALFWorld 中 = admissible actions access。论文对 ALFWorld 明确标注了 \"information asymmetry rather than a computation mode switch\"（Appendix A.9），但 MATH 的 code interpreter 同样不是 ScienceWorld 意义上的 \"deterministic computation\"——它引入了代码生成、执行、debugging 等额外变量。Discussion §5 第一段将三个环境并列作为 \"cross-environment evidence\"，却未讨论 modality 定义的异质性对结论可迁移性的影响。建议在 Method 或 Discussion 中增加一段明确 modality 在各环境中的操作化定义，并讨论这一差异如何影响 DAF 的跨环境可比性。\n\n**W3 [Should-Fix]** 11/30 task types 选择的 generalizability concern 未充分回应\n\n63% 的 ScienceWorld task types 被排除（\"both strategies time out\"）。Appendix A.2 论证了 included vs excluded 的 death rate 相似（17.8% vs 14.9%），但这仅说明 death rate 无 selection bias，不能说明 routing signal 的结构相似。排除的 task types 可能存在不同的 failure modes（如 timeout 而非 death），其 routing signal 结构可能完全不同。论文的 central claim \"death avoidance accounts for X% of routing signal\" 实际上只适用于 \"有 routing signal 的 task types\"，但这一限定在 Abstract 和 Conclusion 中的表述不够显著。\n\n**W4 [Minor]** Abstract 信息过载\n\nAbstract 约 250 词，包含 DAF、penalty sensitivity range、78.9%、router training 结果、MATH、Llama pilot——信息密度高到几乎是 extended abstract。建议删减 penalty sensitivity range 和 Llama pilot 的 mention，专注于核心发现和最重要的验证结果。\n\n**W5 [Minor]** \"Safety critic\" 类比过度延伸\n\nDiscussion 将 router 比作 \"safety critic\"（safe RL 中的术语），但 safe RL 中的 safety critic 是主动学习的约束机制，而本文的发现是 always-deterministic 就是最优策略——这更像是 \"default to safe modality\"，而非 learned safety critic。CRPO 的引用确认了 safe RL 的相关性，但类比本身不够精确。\n\n**W6 [Minor]** Bib 中有 3 个 orphan entries\n\ntoolkengpt-2023、tot-2023、voyager-2023 在 bib 中存在但未被引用。tool-learning-survey-2024 的 bib year 为 2024，但 OpenAlex 记录为 2025 出版——应核实并统一。\n\n### 4. 上轮 Issue 验证结果\n\n| Issue | 状态 | 说明 |\n|-------|------|------|\n| **R6-C1** DAF 90.4% headline + 78.9% 提升 | [RESOLVED] | 78.9% 现在在 Abstract/Intro/Method/Experiments 中均先于或与 DAF 并列出现，明确标注 \"penalty-independent metric\"。双指标设计是本轮最重要的改进。 |\n| **R7-N1** ALFWorld 方法论描述 | [RESOLVED] | Appendix A.9 现包含 model (Qwen2.5-7B)、deterministic modality 定义（admissible actions）、episode count (135)、max steps (50)、success metric (binary)。 |\n| **R6-W8** Safe RL specific citation | [RESOLVED] | CRPO (Xu et al., 2021) 已添加至 Related Work §Safe RL 段落。 |\n| **R7-W1** MATH \"routing signal vanishes\" 措辞 | [PARTIALLY FIXED] | 已添加 \"directional trend\" 和 \"not reaching α=0.05\" 限定，但 \"vanishes\" 一词仍保留在 Abstract 和 Conclusion 中，且 Conclusion 缺少 \"not reaching α=0.05\" hedge。见 W1。 |\n| **R7-W2** Llama pilot 从 Contribution 列表移除 | [RESOLVED] | Contribution 列表中无 Llama/cross-model claim。降级为 \"preliminary pilot\" + \"directionally consistent\"。 |\n| **R7-W5** 缺失 references | [RESOLVED] | RouteLLM、Reflexion、tool-learning survey 均已添加并引用。 |\n| **R7-m1** retool key/year, dynathink author | [RESOLVED] | retool-2025 key/year 已修正（OpenAlex 验证通过）。dynathink-2025 author 格式正确。 |\n| **R7-m2** Abstract DAF 精度 + GPU 描述 | [RESOLVED] | DAF 90.4% 保留精确值但附 CI；GPU 改为 \"two consumer GPUs\"。 |\n| **R7-m3** find-non-living-thing 40 eps + code/data release | [RESOLVED] | Table 4 脚注解释了两批收集；Ethics Statement 明确 release plan。 |\n\n### 5. Missing References\n\n核心 references 已覆盖。可选改进：\n- FrugalGPT (Chen et al., 2023) / HybridLLM (Ding et al., 2024) — cost-quality routing 先驱，与 \"routing as safety vs efficiency\" framing 直接相关\n- 若要加强 \"safety critic\" 类比：CPO (Stooke et al., 2020) 或 safety Q-functions\n\n### 6. Questions for Authors\n\n**Q1**: MATH 中 code interpreter 作为 \"deterministic modality\" 与 ScienceWorld 中 ground-truth observations 的类比是否成立？Code interpreter 本身有 failure modes（syntax error、runtime error），这如何影响 DAF 跨环境可比性？\n\n**Q2**: 19 个被排除的 task types 中，有多少因 timeout 而非 death 失败？如果 timeout 也是一种 \"catastrophic failure\"，DAF 分析是否应将其纳入？\n\n**Q3**: Discussion 中说 \"larger models with lower death rates would reduce DAF, potentially revealing non-death routing signal currently masked by catastrophic failures\"——这是否意味着本文核心发现可能是 model capability 的 artifact 而非 environment structure 的 fundamental property？\n\n### 7. Overall Assessment\n\n**Overall**: 3.0/5 (Findings acceptance)\n**Confidence**: 4/5\n\n**Rationale**: 论文在选定范围内做了扎实的实验分析——DAF 分解、router diagnostic、penalty sensitivity、cross-environment checks 构成完整的 evidence chain。Round 6–7 的关键问题（DAF vs 78.9% 双指标、ALFWorld 方法论、missing references）已全部修复。\n\n阻碍 main conference acceptance 的主要因素：(1) 核心发现绑定于 ScienceWorld 的特定 failure structure（-100 death penalty），generalizability 有限；(2) episode-level counterfactual analysis 方法论本身较为直接（paired comparison under two policies），方法创新性不足以单独支撑贡献；(3) MATH cross-environment validation 未达统计显著性，且 \"deterministic modality\" 定义跨环境不一致，削弱了 cross-environment 叙事。作为 Findings paper，insight 的清晰度和分析的彻底性达到 publishable 水平。\n\n### 参考验证摘要（自动化工具）\n- 29 bib entries, 26 cited, 3 orphan (toolkengpt, tot, voyager)\n- 24/29 OpenAlex verified, 3 not found (react-2023/mixture-of-recursions-2025/gajcin2023 — likely API coverage gaps), 2 minor mismatches (dynathink author parsing, garcia accent)\n- 0 missing bib entries (all citations have corresponding bib entries)",
  "reviewer_id": "2",
  "project": "simgate-modular-routing"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "24ac1b19-c185-4df3-9d7b-ab9d7836d060",
  "isSidechain": false,
  "requestId": "req_011Cb6EyUzpfG5bsfvhgY1FR",
  "type": "assistant",
  "uuid": "73ce3966-a7c9-4751-aba8-a7c8d78c14a5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/.claude/sessions/review_reviewer_2_ab9762a8",
  "sessionId": "5bc9ff02-4cf0-48f5-9df4-52d4a45b7804",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01P3fAgKVSJfC5LL7vGeq7XE",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 605,
      "cache_read_input_tokens": 57128,
      "output_tokens": 15664,
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
          "output_tokens": 15664,
          "cache_read_input_tokens": 57128,
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

### Runtime record

_source line 51_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[Round 8 审稿请求]: ## Round 8 审稿任务 — Reviewer 2（新颖性 + 完整性 + 写作质量）  ### Venue 信息 - **会议**: EMNLP 2026 (通过 ARR May 2026 cycle 提交) - **截止日期**: 2026-05-25 - **页数限制**: 正文 8 页 + 无限参考文献页 - **模板**: ACL LaTeX (`\\…",
  "leafUuid": "73ce3966-a7c9-4751-aba8-a7c8d78c14a5",
  "sessionId": "5bc9ff02-4cf0-48f5-9df4-52d4a45b7804"
}
```

---

### Runtime record

_source line 52_

```json
{
  "type": "ai-title",
  "aiTitle": "Review paper on modular routing with counterfactual analysis",
  "sessionId": "5bc9ff02-4cf0-48f5-9df4-52d4a45b7804"
}
```

---

### Tool result

_source line 53 · 2026-05-16T12:29:28.636Z_

<details><summary>↩ Tool result · `toolu_01XMvkCooQmMbqznm9aeRUuC`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director\"}, \"error\": \"\"}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "73ce3966-a7c9-4751-aba8-a7c8d78c14a5",
  "isSidechain": false,
  "promptId": "2cc35627-090b-4e8e-873a-80e6ce7d766f",
  "type": "user",
  "uuid": "76577076-a684-4e6a-8496-27125467e109",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"review_director_key\\\": \\\"feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director\\\"}, \\\"error\\\": \\\"\\\"}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director\"}, \"error\": \"\"}"
    }
  },
  "sourceToolAssistantUUID": "73ce3966-a7c9-4751-aba8-a7c8d78c14a5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/.claude/sessions/review_reviewer_2_ab9762a8",
  "sessionId": "5bc9ff02-4cf0-48f5-9df4-52d4a45b7804",
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
  "type": "ai-title",
  "aiTitle": "Review paper on modular routing with counterfactual analysis",
  "sessionId": "5bc9ff02-4cf0-48f5-9df4-52d4a45b7804"
}
```

---

### Runtime record

_source line 55 · 2026-05-16T12:30:23.905Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-16T12:30:23.905Z",
  "sessionId": "5bc9ff02-4cf0-48f5-9df4-52d4a45b7804",
  "content": "[Round 8 审稿请求]:\n## 交叉分享 — Reviewer 1 的完整审稿意见\n\n请逐条回应 Reviewer 1 的 Weaknesses：对每条标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n以下是 Reviewer 1 的完整审稿意见：\n\n### Summary\n本文提出 episode-level counterfactual analysis 方法，分析模块化 LLM agent 中路由信号的来源。在 ScienceWorld 的 11/30 任务类型（245 episodes）上，发现 78.9% 的非平局路由标签源自 death asymmetry（penalty-independent），DAF 在 P=100 时达 90.4%。论文训练了一个探索性 step-level router，发现其在 held-out episodes 上低于 always-deterministic baseline，并通过 data/capacity scaling 确认这是结构性限制。跨环境对比（MATH/ALFWorld）提供方向性支持证据。\n\n### Strengths\n- S1: 方法论贡献清晰——episode-level counterfactual analysis 在 sparse-reward 环境中解决了 step-level oracle 退化问题。\n- S2: 透明度极高——DAF penalty-dependence、r=0.97 structural coupling、11/30 scope 均主动披露。\n- S3: 78.9% 作为 penalty-independent companion metric 与 DAF 并列呈现。\n- S4: Robustness diagnostics 丰富——LOO、bootstrap CI、Spearman ρ=0.986、anti-cherry-picking paragraph。\n- S5: Labeling quality audit 排除了 oracle circularity。\n- S6: Router failure 的诚实报告比隐藏负面结果更有科学价值。\n\n### Weaknesses\n\n**W1 [Should-Fix]** Data scaling ablation 的 minority-class confound\n- Augmentation 使用 \"synonym substitution + template variation\"，只增加 surface diversity 不增加 episode diversity。Majority class 比例从 89.6%（100%）上升到 97.7%（800%），internal-preferred episodes 始终只有 ~8-9 个 episode 的变体。25% unaugmented scale 已 collapse 的事实有力，但论文应区分 \"step-level data scarcity\" 和 \"episode-level minority-class scarcity\"——后者是真正瓶颈，32× scaling 没有解决它。\n- 建议：\"rules out data scarcity\" 应软化为 \"consistent with structural limitation, though cannot definitively rule out that more diverse minority-class episodes would help\"。\n\n**W2 [Should-Fix]** Capacity scaling 范围偏窄（0.6B-4B）\n- 三个点均为小模型。更关键的是：论文未在 episode-level 上报告 capacity scaling 结果——只有 step-level 数据。如果 episode-level 在所有 capacity 下都是 ~47-50%，这才是真正排除 capacity 限制的证据。\n\n**W3 [Minor]** Reasoning depth ablation 的 sample size 未报告\n- \"6 task types\"，Mann-Whitney p>0.26，|d|≤0.31，但未报告 episode 数量。\n\n**W4 [Minor]** Cross-environment evidence 的 claim 精度\n- Conclusion 中 \"routing signal vanishes\" 措辞略超出 p=0.079 所支持的结论。\n\n**W5 [Minor]** r=0.97 的 structural coupling 已被承认但需更显式量化\n- 由于 Δ_full ≈ δ·P + Δ_nd 且 Δ_nd 各 task 近似常数，r=0.97 在数学上几乎必然。它证明的是 Δ_nd 的近似均匀性，而非 death 的\"预测力\"。应加一句明确指出这一数学必然性。\n\n---\n\n### Overall Assessment\n**3.5/5** — Borderline to Weak Accept (Findings track)\n**Confidence**: 4/5\n\n---\n\n请逐条回应（[AGREE] / [REBUT]）。"
}
```

---

### Runtime record

_source line 56 · 2026-05-16T12:30:23.905Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-16T12:30:23.905Z",
  "sessionId": "5bc9ff02-4cf0-48f5-9df4-52d4a45b7804"
}
```

---

## Round 2

2 recorded events

### User

_source line 57 · 2026-05-16T12:30:23.894Z_

Continue from where you left off.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "76577076-a684-4e6a-8496-27125467e109",
  "isSidechain": false,
  "promptId": "161b111a-6738-46a5-981a-305c4a471755",
  "type": "user",
  "isMeta": true,
  "uuid": "d0f29ace-6423-45df-96fa-8ed99ef329bf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/.claude/sessions/review_reviewer_2_ab9762a8",
  "sessionId": "5bc9ff02-4cf0-48f5-9df4-52d4a45b7804",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 58 · 2026-05-16T12:30:23.894Z_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d0f29ace-6423-45df-96fa-8ed99ef329bf",
  "isSidechain": false,
  "type": "assistant",
  "uuid": "4bf19224-59db-4bff-a689-20300bfee0df",
  "isApiErrorMessage": false,
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/.claude/sessions/review_reviewer_2_ab9762a8",
  "sessionId": "5bc9ff02-4cf0-48f5-9df4-52d4a45b7804",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "id": "dc7bd51f-5082-4a9f-a870-567ae650e36c",
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

_source line 59 · 2026-05-16T12:30:23.982Z_

[Round 8 审稿请求]:
## 交叉分享 — Reviewer 1 的完整审稿意见

请逐条回应 Reviewer 1 的 Weaknesses：对每条标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。

---

以下是 Reviewer 1 的完整审稿意见：

### Summary
本文提出 episode-level counterfactual analysis 方法，分析模块化 LLM agent 中路由信号的来源。在 ScienceWorld 的 11/30 任务类型（245 episodes）上，发现 78.9% 的非平局路由标签源自 death asymmetry（penalty-independent），DAF 在 P=100 时达 90.4%。论文训练了一个探索性 step-level router，发现其在 held-out episodes 上低于 always-deterministic baseline，并通过 data/capacity scaling 确认这是结构性限制。跨环境对比（MATH/ALFWorld）提供方向性支持证据。

### Strengths
- S1: 方法论贡献清晰——episode-level counterfactual analysis 在 sparse-reward 环境中解决了 step-level oracle 退化问题。
- S2: 透明度极高——DAF penalty-dependence、r=0.97 structural coupling、11/30 scope 均主动披露。
- S3: 78.9% 作为 penalty-independent companion metric 与 DAF 并列呈现。
- S4: Robustness diagnostics 丰富——LOO、bootstrap CI、Spearman ρ=0.986、anti-cherry-picking paragraph。
- S5: Labeling quality audit 排除了 oracle circularity。
- S6: Router failure 的诚实报告比隐藏负面结果更有科学价值。

### Weaknesses

**W1 [Should-Fix]** Data scaling ablation 的 minority-class confound
- Augmentation 使用 "synonym substitution + template variation"，只增加 surface diversity 不增加 episode diversity。Majority class 比例从 89.6%（100%）上升到 97.7%（800%），internal-preferred episodes 始终只有 ~8-9 个 episode 的变体。25% unaugmented scale 已 collapse 的事实有力，但论文应区分 "step-level data scarcity" 和 "episode-level minority-class scarcity"——后者是真正瓶颈，32× scaling 没有解决它。
- 建议："rules out data scarcity" 应软化为 "consistent with structural limitation, though cannot definitively rule out that more diverse minority-class episodes would help"。

**W2 [Should-Fix]** Capacity scaling 范围偏窄（0.6B-4B）
- 三个点均为小模型。更关键的是：论文未在 episode-level 上报告 capacity scaling 结果——只有 step-level 数据。如果 episode-level 在所有 capacity 下都是 ~47-50%，这才是真正排除 capacity 限制的证据。

**W3 [Minor]** Reasoning depth ablation 的 sample size 未报告
- "6 task types"，Mann-Whitney p>0.26，|d|≤0.31，但未报告 episode 数量。

**W4 [Minor]** Cross-environment evidence 的 claim 精度
- Conclusion 中 "routing signal vanishes" 措辞略超出 p=0.079 所支持的结论。

**W5 [Minor]** r=0.97 的 structural coupling 已被承认但需更显式量化
- 由于 Δ_full ≈ δ·P + Δ_nd 且 Δ_nd 各 task 近似常数，r=0.97 在数学上几乎必然。它证明的是 Δ_nd 的近似均匀性，而非 death 的"预测力"。应加一句明确指出这一数学必然性。

---

### Overall Assessment
**3.5/5** — Borderline to Weak Accept (Findings track)
**Confidence**: 4/5

---

请逐条回应（[AGREE] / [REBUT]）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4bf19224-59db-4bff-a689-20300bfee0df",
  "isSidechain": false,
  "promptId": "161b111a-6738-46a5-981a-305c4a471755",
  "type": "user",
  "uuid": "32bb167e-e3df-41ba-bed4-9f6f2d955a6c",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/.claude/sessions/review_reviewer_2_ab9762a8",
  "sessionId": "5bc9ff02-4cf0-48f5-9df4-52d4a45b7804",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 60 · 2026-05-16T12:30:56.172Z_

<details><summary>Logged reasoning block</summary>

```text
Let me carefully review Reviewer 1's weaknesses and respond to each one based on what I found in my own review of the paper.

**R1-W1**: Data scaling ablation minority-class confound
- R1 argues that augmentation only adds surface diversity, not episode diversity, and that minority class scarcity (only ~8-9 unique internal-preferred episodes) is the real bottleneck.
- Looking at the paper: Table 7 shows data scaling from 25% to 800%. The paper says "Augmentation disproportionately increases the majority (deterministic) class: Det% rises from 89.6% at 100% to 94.2% at 200% and ~97.7% at 800%." And "the complete collapse to majority-class prediction (internal recall = 0.0) occurs even at the smallest unaugmented scale (25%, ~90% det), confirming this is not an augmentation artifact."


- R1 has a point here: 32× data scaling just paraphrases existing episodes rather than creating new ones. The paper's claim about ruling out data scarcity is really about step-level scarcity, not the fundamental problem of having only 9 internal-preferred episodes to learn from. This is a valid methodological concern I should acknowledge.

**R1-W2**: Capacity scaling range too narrow (0.6B-4B), only step-level
- The paper examines step-level balanced accuracy across model sizes in Appendix A.7, but this doesn't directly address whether larger models could learn better routing policies with more episode-level diversity.
- I should agree that the ablation is incomplete — they only report episode-level performance for the 1.7B model, not for the smaller and larger variants.

**R1-W3**: Reasoning depth ablation sample size not reported
- The ablation comparing chain-of-thought reasoning against direct answers across 6 task types found no significant difference, but the sample size for this comparison isn't clearly stated in the methods section.
- I should agree this is a minor reporting gap.

**R1-W4**: "routing signal vanishes" overstatement
- This matches my own concern, so I should agree and note that I independently raised the same issue.

**R1-W5**: r=0.97 structural coupling
- R1 makes a valid point that the high correlation is partly mathematical — since the score formula is Δ_full ≈ δ·P + Δ_nd and the non-death component stays relatively constant across tasks, the correlation is somewhat constrained by the structure itself.
- The paper does acknowledge this structural component in the abstract and figure captions, so this isn't a hidden limitation.
- Looking at Table 6, the penalty correlation analysis actually demonstrates this structural effect nicely — r climbs from -0.08 at P=10 to 0.97 at P=100 to 0.99 at P=200, which shows how the penalty magnitude directly drives the correlation strength.
- The paper does acknowledge the structural coupling more than R1 suggests (the abstract mentions "partly structural" and Appendix A.4 provides the full mechanism), but adding an explicit sentence in §4.1 would make this clearer and preempt the critique.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "32bb167e-e3df-41ba-bed4-9f6f2d955a6c",
  "isSidechain": false,
  "requestId": "req_011Cb6FUgdd2YHV4tv3oQnQr",
  "type": "assistant",
  "uuid": "ee4afe15-0224-420d-b56a-774505045547",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/.claude/sessions/review_reviewer_2_ab9762a8",
  "sessionId": "5bc9ff02-4cf0-48f5-9df4-52d4a45b7804",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011ktCPx18nYiTkcSDJp9Fqq",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1194,
      "cache_read_input_tokens": 73464,
      "output_tokens": 3181,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1194,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 3181,
          "cache_read_input_tokens": 73464,
          "cache_creation_input_tokens": 1194,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1194
          },
          "type": "message"
        }
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

_source line 61 · 2026-05-16T12:30:56.712Z_

逐条回应 Reviewer 1 的 Weaknesses。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ee4afe15-0224-420d-b56a-774505045547",
  "isSidechain": false,
  "requestId": "req_011Cb6FUgdd2YHV4tv3oQnQr",
  "type": "assistant",
  "uuid": "8b829489-0523-4931-be99-4fed4d80cd55",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/.claude/sessions/review_reviewer_2_ab9762a8",
  "sessionId": "5bc9ff02-4cf0-48f5-9df4-52d4a45b7804",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011ktCPx18nYiTkcSDJp9Fqq",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1194,
      "cache_read_input_tokens": 73464,
      "output_tokens": 3181,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1194,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 3181,
          "cache_read_input_tokens": 73464,
          "cache_creation_input_tokens": 1194,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1194
          },
          "type": "message"
        }
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

_source line 62 · 2026-05-16T12:31:42.223Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director · `toolu_01DGxCtcryfstgDqVSpbbEH6`</summary>

```json
{
  "text": "## Reviewer 2 对 Reviewer 1 Weaknesses 的逐条回应\n\n---\n\n**[AGREE] R1-W1: Data scaling ablation 的 minority-class confound**\n\n同意。这是本文 router diagnostic 中最值得补充说明的方法论漏洞。论文的 data scaling（Table 7）使用 \"synonym substitution + template variation\" 做 augmentation，仅增加 step-level surface diversity，不增加 episode-level diversity。核心问题是：internal-preferred episodes 始终只有 9 个 unique episode（来自 Table 4 的 86:9 label 分布），无论 augment 到多少倍，router 看到的都是同 9 个 episode 的 paraphrase 变体。\n\n论文确实部分预见了这个问题——Appendix A.5 说 \"the complete collapse to majority-class prediction (internal recall = 0.0) occurs even at the smallest unaugmented scale (25%, ~90% det)\"，试图论证这不是 augmentation artifact。但 R1 的区分是准确的：25% scale 的 collapse 说明的是 \"9 个 minority episode 的子集不够\"，不是 \"episode diversity 不重要\"。\n\n建议作者将 \"rules out data scarcity\" 软化为 \"rules out step-level data scarcity; episode-level minority-class diversity remains a potential confound\"。这不影响 structural limitation 的核心论点（DAF=90.4% 下 always-deterministic 确实 trivially near-optimal），但提高了 claim 精度。\n\n---\n\n**[AGREE] R1-W2: Capacity scaling 范围偏窄（0.6B–4B），缺 episode-level 报告**\n\n同意，且补充两点：\n\n(1) 0.6B → 1.7B → 4B 三个点均为小模型（<5B），在 LLM routing 文献中，更典型的 scaling 范围是 1B–70B。虽然论文旨在验证 \"router capacity 不是瓶颈\"，但 4B 仍可能不足以学习 episode-level generalization 所需的 abstract routing features。\n\n(2) 更关键的是 R1 指出的 evaluation granularity 问题：Appendix A.7 只报告了 step-level balanced accuracy（52.8% / 54.1% / 53.5%），而论文的核心发现是 step-level vs episode-level 的 generalization gap（§4.3, Table 3）。如果 0.6B 和 4B 的 episode-level 结果也在 ~47–50% 范围内，这会实质性地加强 \"structural limitation\" 论点；如果 4B 的 episode-level 有所改善，则 structural limitation claim 需要弱化。缺少这组数据使得 capacity scaling ablation 不完整。\n\n---\n\n**[AGREE] R1-W3: Reasoning depth ablation 的 sample size 未报告**\n\n同意。Method §2.1 报告了 \"6 task types\"、Mann-Whitney p > 0.26、|d| ≤ 0.31、death rates 41.8% vs 42.5%，但未说明每组的 episode 数量。在 effect size 较小（|d| ≤ 0.31）的情况下，sample size 决定了 power——如果每组只有 ~20 episodes，non-significant result 可能是 underpowered 而非 truly null。修复成本极低（加一个括号），应补充。\n\n---\n\n**[AGREE] R1-W4: \"routing signal vanishes\" 措辞**\n\n强烈同意。我在自己的审稿中独立提出了相同问题（R2-W1）。补充一个 R1 未明确指出的细节：Conclusion 中 \"routing signal vanishes without death penalty, with a directional trend favoring internal reasoning ($+4.3$~pp, $p = 0.079$)\" 缺少 \"not reaching α=0.05\" 的 hedge——而 Abstract 和 Introduction 均有此限定。这造成了 paper 内部的叙事不一致：同一个 p=0.079 result 在不同位置的审慎程度不同。\n\n建议统一修改为 \"the deterministic advantage disappears\" 或 \"death-driven routing signal is absent\"，并确保所有出现 p=0.079 的位置都附带 significance caveat。\n\n---\n\n**[AGREE with nuance] R1-W5: r=0.97 的 structural coupling 需更显式量化**\n\n同意 R1 的核心判断——Δ_full ≈ δ·P + Δ_nd 中，当 Δ_nd 跨 task 近似常数（mean non-death gap = -1.19 excluding find-non-living-thing, 见 Appendix A.4）且 P=100 使 death term 远大于 Δ_nd 时，r≈1 是数学必然。\n\n但需指出论文已在多处部分承认了这一点：\n- Abstract: \"r=0.97, though partly structural as death penalties contribute directly to score differences\"\n- Appendix A.4: Table 6 展示了 r 随 P 变化（P=10 → r=-0.08, P=25 → r=0.51, P=100 → r=0.97），并明确写道 \"this is a mathematical consequence of the decomposition (DAF = δP/(δP + Δ_nd)), not evidence of mechanism robustness\"\n- Discussion: \"death is effectively the only component generating differential routing signal\"\n\n所以问题不是 \"未承认\"，而是 §4.1 主文中首次报告 r=0.97 时没有足够 foreground 这个 structural coupling——读者可能在看到数字时形成过强的 \"predictive power\" 印象，到 Appendix 才看到 qualification。建议在 §4.1 报告 r=0.97 的位置加一句显式说明其数学近必然性，而非仅在 Abstract 用 \"partly structural\" 一笔带过。\n\n---\n\n### 总结\n\n5 条 Weakness 中我对 4 条完全同意（W1–W4），对 W5 部分同意（核心判断正确但论文已有部分 acknowledgment）。R1 和 R2 的审查具有高度互补性：R1 聚焦 router diagnostic 的方法论严密性（W1 minority-class confound, W2 capacity scaling granularity），R2 聚焦跨环境叙事一致性（W2 modality definition inconsistency, W3 task selection generalizability）。\n\n两位 Reviewer 独立收敛的共识问题：\n1. **\"routing signal vanishes\" 措辞**（R1-W4 = R2-W1）——Must-Fix 级别\n2. **Capacity/data scaling ablation 的局限性**（R1-W1 + R1-W2）——Should-Fix 级别\n3. **r=0.97 structural coupling 的 prominence**（R1-W5）——Minor but recommended\n\n整体评分维持 3.0/5 (Findings acceptance), Confidence 4/5。",
  "reviewer_id": "2",
  "project": "simgate-modular-routing"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8b829489-0523-4931-be99-4fed4d80cd55",
  "isSidechain": false,
  "requestId": "req_011Cb6FUgdd2YHV4tv3oQnQr",
  "type": "assistant",
  "uuid": "99284b5b-fdc2-46fb-9659-65f43e3d7dc1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/.claude/sessions/review_reviewer_2_ab9762a8",
  "sessionId": "5bc9ff02-4cf0-48f5-9df4-52d4a45b7804",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011ktCPx18nYiTkcSDJp9Fqq",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1194,
      "cache_read_input_tokens": 73464,
      "output_tokens": 3181,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1194,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 3181,
          "cache_read_input_tokens": 73464,
          "cache_creation_input_tokens": 1194,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1194
          },
          "type": "message"
        }
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

_source line 63 · 2026-05-16T12:31:46.085Z_

<details><summary>↩ Tool result · `toolu_01DGxCtcryfstgDqVSpbbEH6`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director\"}, \"error\": \"\"}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "99284b5b-fdc2-46fb-9659-65f43e3d7dc1",
  "isSidechain": false,
  "promptId": "161b111a-6738-46a5-981a-305c4a471755",
  "type": "user",
  "uuid": "8dea4467-865a-422b-97fc-0267dda3d961",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"review_director_key\\\": \\\"feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director\\\"}, \\\"error\\\": \\\"\\\"}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director\"}, \"error\": \"\"}"
    }
  },
  "sourceToolAssistantUUID": "99284b5b-fdc2-46fb-9659-65f43e3d7dc1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/.claude/sessions/review_reviewer_2_ab9762a8",
  "sessionId": "5bc9ff02-4cf0-48f5-9df4-52d4a45b7804",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---
