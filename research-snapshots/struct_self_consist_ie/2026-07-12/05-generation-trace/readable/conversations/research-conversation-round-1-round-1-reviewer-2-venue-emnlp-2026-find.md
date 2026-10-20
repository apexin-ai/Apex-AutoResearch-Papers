# Research conversation: [Round 1 审稿请求]: ## Round 1 审稿任务 — Reviewer 2 **你的侧重**：新颖性 + 定位完整性 + 写作质量 + 格式合规 ### 投稿信息 - **目标 venue**: EMNLP 2026 Find

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 83
- **Recorded user turns:** 3
- **Tool calls:** 22
- **Original source:** `logs/chats/exported-trajectories/account-3/f49c1ccb-97a0-4961-857d-2db0aa0e0624.jsonl`
- **Structured JSON:** [`f651013fb73a3ef88fa5.json`](../../sessions/f6/f651013fb73a3ef88fa5.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-15T14:58:32.856Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-15T14:58:32.856Z",
  "sessionId": "f49c1ccb-97a0-4961-857d-2db0aa0e0624",
  "content": "[Round 1 审稿请求]:\n## Round 1 审稿任务 — Reviewer 2\n\n**你的侧重**：新颖性 + 定位完整性 + 写作质量 + 格式合规\n\n### 投稿信息\n- **目标 venue**: EMNLP 2026 Findings (ARR May cycle)\n- **Deadline**: 2026-05-25\n- **格式**: ACL template, 长文 8 页正文 + unlimited Limitations/Ethics/References/Appendix\n- **匿名**: Double-blind\n- **论文路径**: `projects/struct_self_consist_ie/docs/paper/main.tex`（多文件结构，sections 在 `sections/` 子目录）\n\n### 论文概要\n本文研究 LLM 结构化信息抽取（NER/RE）中，自一致性信号能否用于质量估计和样本选择。比较 5 个置信度信号（VC, SJ, FK, EM, LP），在 3 个 NER 数据集 + 1 个 RE 数据集、2 个 8B 模型上系统评估。核心发现：所有信号实现强质量估计（ρ 至 0.38, AUROC 至 0.75），但无一显著改善样本选择——\"correlation-selection gap\"。机制解释：LP score compression + MBR utility-quality misalignment。\n\n### 审查要点（不限于此）\n\n1. **新颖性与贡献评估**\n   - Correlation-selection gap 是否为真正的 empirical discovery？4/5 信号是 instance-level——无法 select 是定义必然。论文自承 \"Layer 1 (definitional)\"。核心贡献应聚焦 LP compression 诊断 + MBR failure，而非整个 gap\n   - 与 Nédellec et al. (2026) 的增量贡献：structural matching、selection analysis、difficulty gradient 三点增量是否足够\n   - Contribution 1（multi-metric evaluation）是 methodological contribution 还是 engineering benchmark？\n   - SJ 方法新颖性：Hungarian matching + token-level IoU 的组合是否属于标准技术应用\n\n2. **Related Work 覆盖与定位**\n   - 引用完整性检查：62 篇 bib entry 是否均被正文引用（orphan check）\n   - Eikema et al. (2025) structure-conditional MBR 是否应前移到 Related Work（当前仅在 Discussion）\n   - MBR decoding 在非 MT 任务中的应用引用是否充分\n   - Test-time scaling survey (Zhang et al. 2025) 引用位置是否合适\n   - 与 concurrent work 的差异化是否清晰（USC, CISC, Self-Certainty, RASC 等）\n\n3. **写作质量**\n   - Abstract 密度：是否过于拥挤（5 signal names, 3 datasets, 2 models, 4 metrics + gap 概念）——是否适合精简为问题-发现-意义三段式\n   - Claim scope：标题 \"8B-Scale\" 是否充分限定规模泛化；\"Do Not Select\" 是否过强（仅 2 个 8B 模型）\n   - 术语一致性：VC/SJ/FK/EM/LP 在全文表格和正文中是否统一\n   - RE 结论的 \"preliminary\" 标注是否全文一致（Abstract, Experiments, Discussion, Conclusion 各处）\n   - Figure/Table caption 信息量和准确性\n\n4. **格式合规（关键）**\n   - **页数检查**：论文正文（Abstract 至 Conclusion）是否 ≤ 8 页（初步估计约 11 页，严重超限）\n   - Limitations section 位置和内容\n   - Ethics Statement 是否独立且有实质内容\n   - 匿名合规：是否有身份泄露（代码链接、致谢、自引方式）\n   - ACL template 使用是否正确（`\\usepackage[review]{acl}`）\n   - References 格式（natbib + acl_natbib.bst）\n\n5. **Reproducibility checklist**\n   - 代码和数据是否承诺发布\n   - 实验配置是否完整\n   - 随机种子报告\n\n请按 EMNLP 标准进行严格审查，输出完整审稿报告。"
}
```

---

### Runtime record

_source line 2 · 2026-05-15T14:58:32.860Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-15T14:58:32.860Z",
  "sessionId": "f49c1ccb-97a0-4961-857d-2db0aa0e0624"
}
```

---

## Round 1

71 recorded events

### User

_source line 3 · 2026-05-15T14:58:32.896Z_

[Round 1 审稿请求]:
## Round 1 审稿任务 — Reviewer 2

**你的侧重**：新颖性 + 定位完整性 + 写作质量 + 格式合规

### 投稿信息
- **目标 venue**: EMNLP 2026 Findings (ARR May cycle)
- **Deadline**: 2026-05-25
- **格式**: ACL template, 长文 8 页正文 + unlimited Limitations/Ethics/References/Appendix
- **匿名**: Double-blind
- **论文路径**: `projects/struct_self_consist_ie/docs/paper/main.tex`（多文件结构，sections 在 `sections/` 子目录）

### 论文概要
本文研究 LLM 结构化信息抽取（NER/RE）中，自一致性信号能否用于质量估计和样本选择。比较 5 个置信度信号（VC, SJ, FK, EM, LP），在 3 个 NER 数据集 + 1 个 RE 数据集、2 个 8B 模型上系统评估。核心发现：所有信号实现强质量估计（ρ 至 0.38, AUROC 至 0.75），但无一显著改善样本选择——"correlation-selection gap"。机制解释：LP score compression + MBR utility-quality misalignment。

### 审查要点（不限于此）

1. **新颖性与贡献评估**
   - Correlation-selection gap 是否为真正的 empirical discovery？4/5 信号是 instance-level——无法 select 是定义必然。论文自承 "Layer 1 (definitional)"。核心贡献应聚焦 LP compression 诊断 + MBR failure，而非整个 gap
   - 与 Nédellec et al. (2026) 的增量贡献：structural matching、selection analysis、difficulty gradient 三点增量是否足够
   - Contribution 1（multi-metric evaluation）是 methodological contribution 还是 engineering benchmark？
   - SJ 方法新颖性：Hungarian matching + token-level IoU 的组合是否属于标准技术应用

2. **Related Work 覆盖与定位**
   - 引用完整性检查：62 篇 bib entry 是否均被正文引用（orphan check）
   - Eikema et al. (2025) structure-conditional MBR 是否应前移到 Related Work（当前仅在 Discussion）
   - MBR decoding 在非 MT 任务中的应用引用是否充分
   - Test-time scaling survey (Zhang et al. 2025) 引用位置是否合适
   - 与 concurrent work 的差异化是否清晰（USC, CISC, Self-Certainty, RASC 等）

3. **写作质量**
   - Abstract 密度：是否过于拥挤（5 signal names, 3 datasets, 2 models, 4 metrics + gap 概念）——是否适合精简为问题-发现-意义三段式
   - Claim scope：标题 "8B-Scale" 是否充分限定规模泛化；"Do Not Select" 是否过强（仅 2 个 8B 模型）
   - 术语一致性：VC/SJ/FK/EM/LP 在全文表格和正文中是否统一
   - RE 结论的 "preliminary" 标注是否全文一致（Abstract, Experiments, Discussion, Conclusion 各处）
   - Figure/Table caption 信息量和准确性

4. **格式合规（关键）**
   - **页数检查**：论文正文（Abstract 至 Conclusion）是否 ≤ 8 页（初步估计约 11 页，严重超限）
   - Limitations section 位置和内容
   - Ethics Statement 是否独立且有实质内容
   - 匿名合规：是否有身份泄露（代码链接、致谢、自引方式）
   - ACL template 使用是否正确（`\usepackage[review]{acl}`）
   - References 格式（natbib + acl_natbib.bst）

5. **Reproducibility checklist**
   - 代码和数据是否承诺发布
   - 实验配置是否完整
   - 随机种子报告

请按 EMNLP 标准进行严格审查，输出完整审稿报告。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "a8cee1eb-a5df-415d-8e30-c85446d1e0a7",
  "type": "user",
  "uuid": "4d171d94-968b-4b19-a111-075fabb015a1",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "f49c1ccb-97a0-4961-857d-2db0aa0e0624",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-15T14:58:32.895Z_

```json
{
  "parentUuid": "4d171d94-968b-4b19-a111-075fabb015a1",
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
  "uuid": "e406adb3-690d-418d-8cec-df5f7e0ba966",
  "timestamp": "2026-05-15T14:58:32.895Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "f49c1ccb-97a0-4961-857d-2db0aa0e0624",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-15T14:58:32.896Z_

```json
{
  "parentUuid": "e406adb3-690d-418d-8cec-df5f7e0ba966",
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
  "uuid": "b71f5321-4b8b-47a9-ac98-d01d35d8b2ab",
  "timestamp": "2026-05-15T14:58:32.896Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "f49c1ccb-97a0-4961-857d-2db0aa0e0624",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 6 · 2026-05-15T14:58:32.896Z_

```json
{
  "parentUuid": "b71f5321-4b8b-47a9-ac98-d01d35d8b2ab",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "6957be4f-d663-4216-9d0b-9510a0612081",
  "timestamp": "2026-05-15T14:58:32.896Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "f49c1ccb-97a0-4961-857d-2db0aa0e0624",
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
  "aiTitle": "Round 1 review for EMNLP 2026 structured IE paper",
  "sessionId": "f49c1ccb-97a0-4961-857d-2db0aa0e0624"
}
```

---

### Assistant

_source line 8 · 2026-05-15T14:58:37.335Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to perform a Round 1 review of a paper as Reviewer 2, focusing on novelty, related work completeness, writing quality, and format compliance. Let me start by:

1. First, loading the review-reviewer-session-start skill as instructed
2. Searching for EMNLP 2026 / ACL ARR reviewer guidelines
3. Reading the paper

Let me begin by reading the paper and searching for reviewer guidelines in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6957be4f-d663-4216-9d0b-9510a0612081",
  "isSidechain": false,
  "requestId": "req_011Cb4Yy1MWLQupr9o8ewdMs",
  "type": "assistant",
  "uuid": "6aef973d-4c03-47fb-b1b4-2d35dd79a716",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "f49c1ccb-97a0-4961-857d-2db0aa0e0624",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Pob25oeSUEDDyGm1KWpE34",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14261,
      "cache_read_input_tokens": 11841,
      "output_tokens": 442,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 14261,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 442,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 14261,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 14261
          },
          "type": "message"
        }
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

_source line 9 · 2026-05-15T14:58:37.839Z_

开始 Round 1 审稿。先并行执行：加载 session-start skill、搜索 ARR reviewer guidelines、读取论文主文件。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6aef973d-4c03-47fb-b1b4-2d35dd79a716",
  "isSidechain": false,
  "requestId": "req_011Cb4Yy1MWLQupr9o8ewdMs",
  "type": "assistant",
  "uuid": "3ba73ed9-904f-4ac5-b824-aa24238c0571",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "f49c1ccb-97a0-4961-857d-2db0aa0e0624",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Pob25oeSUEDDyGm1KWpE34",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14261,
      "cache_read_input_tokens": 11841,
      "output_tokens": 442,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 14261,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 442,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 14261,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 14261
          },
          "type": "message"
        }
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

_source line 10 · 2026-05-15T14:58:38.901Z_

<details open><summary>🔧 Tool call — Read · `toolu_01MJWuZpeGEMVrh4ZpvFM7ze`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/skills/review-reviewer-session-start.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3ba73ed9-904f-4ac5-b824-aa24238c0571",
  "isSidechain": false,
  "requestId": "req_011Cb4Yy1MWLQupr9o8ewdMs",
  "type": "assistant",
  "uuid": "6f0dbf2e-db90-444d-8f45-85dc980c8f84",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "f49c1ccb-97a0-4961-857d-2db0aa0e0624",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Pob25oeSUEDDyGm1KWpE34",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14261,
      "cache_read_input_tokens": 11841,
      "output_tokens": 442,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 14261,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 442,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 14261,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 14261
          },
          "type": "message"
        }
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

_source line 11 · 2026-05-15T14:58:40.562Z_

<details><summary>↩ Tool result · `toolu_01BRJHjenyTSHSUo4z9ZjWmS`</summary>

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
21	\title{Strong Predictors, Weak Selectors:\\ Confidence Signals Predict but Do Not Select in 8B-Scale Information Extraction}
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
40	All experiments use publicly available benchmarks (SciERC, CoNLL-2003, WNUT-17) and open-weight models (Qwen3-8B, LLaMA-3.1-8B).
41	CoNLL-2003 is derived from the Reuters RCV1 corpus, which is available for research purposes under a NIST agreement; we use the standard research distribution.
42	No new human data was collected or annotated for this study.
43	Our findings on signal limitations could inform more reliable deployment of IE systems by guiding practitioners toward appropriate confidence signals for their use case.
44	
45	\bibliography{references}
46	
47	\appendix
48	\input{sections/appendix}
49	
50	\end{document}
51	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d502479d-ce60-4199-b685-36f3efe0be66",
  "isSidechain": false,
  "promptId": "a8cee1eb-a5df-415d-8e30-c85446d1e0a7",
  "type": "user",
  "uuid": "51e20519-5cd6-40b8-aeab-470d0eb29d6d",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex",
      "content": "\\documentclass[11pt]{article}\n\n\\usepackage[review]{acl}\n\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage[T1]{fontenc}\n\\usepackage[utf8]{inputenc}\n\\usepackage{microtype}\n\\usepackage{inconsolata}\n\\usepackage{graphicx}\n\\usepackage{booktabs}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{multirow}\n\\usepackage{xcolor}\n\\usepackage{subcaption}\n\n\\graphicspath{{figures/}}\n\n\\title{Strong Predictors, Weak Selectors:\\\\ Confidence Signals Predict but Do Not Select in 8B-Scale Information Extraction}\n\n\\author{Anonymous}\n\n\\begin{document}\n\\maketitle\n\n\\input{sections/abstract}\n\\input{sections/introduction}\n\\input{sections/related_work}\n\\input{sections/method}\n\\input{sections/experiments}\n\\input{sections/discussion}\n\\input{sections/conclusion}\n\n\\section*{Limitations}\n\\input{sections/limitations}\n\n\\section*{Ethics Statement}\nAll experiments use publicly available benchmarks (SciERC, CoNLL-2003, WNUT-17) and open-weight models (Qwen3-8B, LLaMA-3.1-8B).\nCoNLL-2003 is derived from the Reuters RCV1 corpus, which is available for research purposes under a NIST agreement; we use the standard research distribution.\nNo new human data was collected or annotated for this study.\nOur findings on signal limitations could inform more reliable deployment of IE systems by guiding practitioners toward appropriate confidence signals for their use case.\n\n\\bibliography{references}\n\n\\appendix\n\\input{sections/appendix}\n\n\\end{document}\n",
      "numLines": 51,
      "startLine": 1,
      "totalLines": 51
    }
  },
  "sourceToolAssistantUUID": "d502479d-ce60-4199-b685-36f3efe0be66",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "f49c1ccb-97a0-4961-857d-2db0aa0e0624",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-15T14:58:38.915Z_

<details><summary>↩ Tool result · reported error · `toolu_01MJWuZpeGEMVrh4ZpvFM7ze`</summary>

```text
File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6f0dbf2e-db90-444d-8f45-85dc980c8f84",
  "isSidechain": false,
  "promptId": "a8cee1eb-a5df-415d-8e30-c85446d1e0a7",
  "type": "user",
  "uuid": "65310f3d-23d8-42e8-b015-e003eb410055",
  "toolUseResult": "Error: File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5.",
  "sourceToolAssistantUUID": "6f0dbf2e-db90-444d-8f45-85dc980c8f84",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "f49c1ccb-97a0-4961-857d-2db0aa0e0624",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-15T14:58:40.348Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01Uj9BMpxK96xVvQQajGeYAa`</summary>

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
  "parentUuid": "65310f3d-23d8-42e8-b015-e003eb410055",
  "isSidechain": false,
  "requestId": "req_011Cb4Yy1MWLQupr9o8ewdMs",
  "type": "assistant",
  "uuid": "724c9d33-d411-4d39-b382-13fa858f67b5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "f49c1ccb-97a0-4961-857d-2db0aa0e0624",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Pob25oeSUEDDyGm1KWpE34",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14261,
      "cache_read_input_tokens": 11841,
      "output_tokens": 442,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 14261,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 442,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 14261,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 14261
          },
          "type": "message"
        }
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

_source line 14 · 2026-05-15T14:58:40.353Z_

<details><summary>↩ Tool result · `toolu_01Uj9BMpxK96xVvQQajGeYAa`</summary>

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
  "parentUuid": "724c9d33-d411-4d39-b382-13fa858f67b5",
  "isSidechain": false,
  "promptId": "a8cee1eb-a5df-415d-8e30-c85446d1e0a7",
  "type": "user",
  "uuid": "fb046e71-0f8d-456a-b552-06e1c08f7788",
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
  "sourceToolAssistantUUID": "724c9d33-d411-4d39-b382-13fa858f67b5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "f49c1ccb-97a0-4961-857d-2db0aa0e0624",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-15T14:58:40.554Z_

<details open><summary>🔧 Tool call — Read · `toolu_01BRJHjenyTSHSUo4z9ZjWmS`</summary>

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
  "parentUuid": "fb046e71-0f8d-456a-b552-06e1c08f7788",
  "isSidechain": false,
  "requestId": "req_011Cb4Yy1MWLQupr9o8ewdMs",
  "type": "assistant",
  "uuid": "d502479d-ce60-4199-b685-36f3efe0be66",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "f49c1ccb-97a0-4961-857d-2db0aa0e0624",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Pob25oeSUEDDyGm1KWpE34",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14261,
      "cache_read_input_tokens": 11841,
      "output_tokens": 442,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 14261,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 442,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 14261,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 14261
          },
          "type": "message"
        }
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

_source line 16 · 2026-05-15T14:58:43.446Z_

<details><summary>Logged reasoning block</summary>

```text
Now I need to read the paper sections and search for reviewer guidelines. Let me read all the sections in parallel, and also search for ARR reviewer guidelines.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "51e20519-5cd6-40b8-aeab-470d0eb29d6d",
  "isSidechain": false,
  "requestId": "req_011Cb4YyaRqevxoksW4nB8Mt",
  "type": "assistant",
  "uuid": "f1eab0e0-e890-4e21-b78e-f06de2a4e9c1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "f49c1ccb-97a0-4961-857d-2db0aa0e0624",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01H8R78T7yXMjbMm2LN7ffsn",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 3128,
      "cache_read_input_tokens": 26102,
      "output_tokens": 322,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3128,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 322,
          "cache_read_input_tokens": 26102,
          "cache_creation_input_tokens": 3128,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3128
          },
          "type": "message"
        }
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

_source line 17 · 2026-05-15T14:58:44.571Z_

论文是多文件结构。并行读取所有 sections 和搜索 ARR reviewer guidelines。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f1eab0e0-e890-4e21-b78e-f06de2a4e9c1",
  "isSidechain": false,
  "requestId": "req_011Cb4YyaRqevxoksW4nB8Mt",
  "type": "assistant",
  "uuid": "72947d09-626f-4b9d-912b-ab9228644b48",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "f49c1ccb-97a0-4961-857d-2db0aa0e0624",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01H8R78T7yXMjbMm2LN7ffsn",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 3128,
      "cache_read_input_tokens": 26102,
      "output_tokens": 322,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3128,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 322,
          "cache_read_input_tokens": 26102,
          "cache_creation_input_tokens": 3128,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3128
          },
          "type": "message"
        }
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

_source line 18 · 2026-05-15T14:58:45.084Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01Juduaccz7p5WkxEBmimbPZ`</summary>

```json
{
  "pattern": "**/docs/paper/sections/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "72947d09-626f-4b9d-912b-ab9228644b48",
  "isSidechain": false,
  "requestId": "req_011Cb4YyaRqevxoksW4nB8Mt",
  "type": "assistant",
  "uuid": "6405d6a3-0bb4-420d-bbe4-8844fe748516",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "f49c1ccb-97a0-4961-857d-2db0aa0e0624",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01H8R78T7yXMjbMm2LN7ffsn",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 3128,
      "cache_read_input_tokens": 26102,
      "output_tokens": 322,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3128,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 322,
          "cache_read_input_tokens": 26102,
          "cache_creation_input_tokens": 3128,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3128
          },
          "type": "message"
        }
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

_source line 19 · 2026-05-15T14:58:45.122Z_

<details><summary>↩ Tool result · `toolu_01Juduaccz7p5WkxEBmimbPZ`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/related_work.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/conclusion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/abstract.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/introduction.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/limitations.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/method.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6405d6a3-0bb4-420d-bbe4-8844fe748516",
  "isSidechain": false,
  "promptId": "a8cee1eb-a5df-415d-8e30-c85446d1e0a7",
  "type": "user",
  "uuid": "c335bd99-6eb4-4c08-95b2-d6e3cb32c256",
  "toolUseResult": {
    "filenames": [
      "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/related_work.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/conclusion.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/abstract.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/introduction.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/limitations.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/method.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex"
    ],
    "durationMs": 29,
    "numFiles": 9,
    "truncated": false
  },
  "sourceToolAssistantUUID": "6405d6a3-0bb4-420d-bbe4-8844fe748516",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "f49c1ccb-97a0-4961-857d-2db0aa0e0624",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-15T14:58:46.050Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01TNEMMrA6ivma9waEPavDMi`</summary>

```json
{
  "pattern": "**/docs/paper/references.bib",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c335bd99-6eb4-4c08-95b2-d6e3cb32c256",
  "isSidechain": false,
  "requestId": "req_011Cb4YyaRqevxoksW4nB8Mt",
  "type": "assistant",
  "uuid": "1d6e0569-bc4b-4250-a429-57860e3bd4ce",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "f49c1ccb-97a0-4961-857d-2db0aa0e0624",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01H8R78T7yXMjbMm2LN7ffsn",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 3128,
      "cache_read_input_tokens": 26102,
      "output_tokens": 322,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3128,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 322,
          "cache_read_input_tokens": 26102,
          "cache_creation_input_tokens": 3128,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3128
          },
          "type": "message"
        }
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

_source line 21 · 2026-05-15T14:58:46.084Z_

<details><summary>↩ Tool result · `toolu_01TNEMMrA6ivma9waEPavDMi`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/references.bib
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1d6e0569-bc4b-4250-a429-57860e3bd4ce",
  "isSidechain": false,
  "promptId": "a8cee1eb-a5df-415d-8e30-c85446d1e0a7",
  "type": "user",
  "uuid": "4e20fc7e-ce87-43b6-9aed-ef517ba513c9",
  "toolUseResult": {
    "filenames": [
      "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/references.bib"
    ],
    "durationMs": 28,
    "numFiles": 1,
    "truncated": false
  },
  "sourceToolAssistantUUID": "1d6e0569-bc4b-4250-a429-57860e3bd4ce",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "f49c1ccb-97a0-4961-857d-2db0aa0e0624",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-15T14:58:46.340Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_011BNmUJweTgSwtN89L3z14q`</summary>

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
  "parentUuid": "4e20fc7e-ce87-43b6-9aed-ef517ba513c9",
  "isSidechain": false,
  "requestId": "req_011Cb4YyaRqevxoksW4nB8Mt",
  "type": "assistant",
  "uuid": "dd569837-ec96-4036-a752-700177e31a6b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "f49c1ccb-97a0-4961-857d-2db0aa0e0624",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01H8R78T7yXMjbMm2LN7ffsn",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 3128,
      "cache_read_input_tokens": 26102,
      "output_tokens": 322,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3128,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 322,
          "cache_read_input_tokens": 26102,
          "cache_creation_input_tokens": 3128,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3128
          },
          "type": "message"
        }
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

_source line 23_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[Round 1 审稿请求]: ## Round 1 审稿任务 — Reviewer 2  **你的侧重**：新颖性 + 定位完整性 + 写作质量 + 格式合规  ### 投稿信息 - **目标 venue**: EMNLP 2026 Findings (ARR May cycle) - **Deadline**: 2026-05-25 - **格式**: ACL template, 长文 8 页…",
  "leafUuid": "dd569837-ec96-4036-a752-700177e31a6b",
  "sessionId": "f49c1ccb-97a0-4961-857d-2db0aa0e0624"
}
```

---

### Runtime record

_source line 24_

```json
{
  "type": "ai-title",
  "aiTitle": "Round 1 review for EMNLP 2026 structured IE paper",
  "sessionId": "f49c1ccb-97a0-4961-857d-2db0aa0e0624"
}
```

---

### Tool result

_source line 25 · 2026-05-15T14:58:54.755Z_

<details><summary>↩ Tool result · `toolu_011BNmUJweTgSwtN89L3z14q`</summary>

```text
Web search results for query: "ACL ARR 2025 2026 reviewer guidelines review form criteria scoring"

Links: [{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"ACLRollingReview (@ReviewAcl) / X","url":"https://x.com/reviewacl"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"aclrollingreview/reviewing.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/reviewing.md"}]

I found comprehensive information about ACL ARR reviewer guidelines for 2025-2026. Here's a summary of the key information:

## Scoring System

Starting with February 2025, ARR reviewers are asked to provide three scores: soundness, excitement, and overall recommendation. The soundness scores must be justified by the text of the review.

## Overall Recommendation Criteria

The overall recommendation scores include:

- 5 = Consider for Award: Papers that could be considered for an outstanding paper award at an *ACL conference (up to top 2.5% papers)
- 2 = Resubmit next cycle: Papers needing substantial revisions that can be completed by the next ARR cycle
- 1.5 = Resubmit after next cycle: Papers needing substantial revisions that cannot be completed by the next ARR cycle
- 1 = Do not resubmit: Papers that have to be fully redone, or are not relevant to the *ACL community (not related to computational processing of language)

## Additional Guidelines

Reviewers are asked whether authors have adequately discussed limitations and potential positive and negative societal impacts, with constructive suggestions for improvement, though authors should be rewarded rather than punished for being upfront about limitations.

ARR reviewers are instructed to write a review as if the paper were being considered for the ACL conference, so low scores may indicate the submission is not a good fit for ACL, even if it may be suitable for other specialized venues.

You can find the full detailed guidelines at the official ARR Reviewer Guidelines page: http://aclrollingreview.org/reviewerguidelines


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "dd569837-ec96-4036-a752-700177e31a6b",
  "isSidechain": false,
  "promptId": "a8cee1eb-a5df-415d-8e30-c85446d1e0a7",
  "type": "user",
  "uuid": "e91f9661-bba5-4247-8351-3e7914fef3a4",
  "toolUseResult": {
    "query": "ACL ARR 2025 2026 reviewer guidelines review form criteria scoring",
    "results": [
      {
        "tool_use_id": "srvtoolu_01GUXEj2yVYnipNLWqcD6eaz",
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
            "title": "ACLRollingReview (@ReviewAcl) / X",
            "url": "https://x.com/reviewacl"
          },
          {
            "title": "Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics",
            "url": "http://aclrollingreview.org/authors"
          },
          {
            "title": "aclrollingreview/reviewing.md at main · acl-org/aclrollingreview",
            "url": "https://github.com/acl-org/aclrollingreview/blob/main/reviewing.md"
          }
        ]
      },
      "I found comprehensive information about ACL ARR reviewer guidelines for 2025-2026. Here's a summary of the key information:\n\n## Scoring System\n\nStarting with February 2025, ARR reviewers are asked to provide three scores: soundness, excitement, and overall recommendation. The soundness scores must be justified by the text of the review.\n\n## Overall Recommendation Criteria\n\nThe overall recommendation scores include:\n\n- 5 = Consider for Award: Papers that could be considered for an outstanding paper award at an *ACL conference (up to top 2.5% papers)\n- 2 = Resubmit next cycle: Papers needing substantial revisions that can be completed by the next ARR cycle\n- 1.5 = Resubmit after next cycle: Papers needing substantial revisions that cannot be completed by the next ARR cycle\n- 1 = Do not resubmit: Papers that have to be fully redone, or are not relevant to the *ACL community (not related to computational processing of language)\n\n## Additional Guidelines\n\nReviewers are asked whether authors have adequately discussed limitations and potential positive and negative societal impacts, with constructive suggestions for improvement, though authors should be rewarded rather than punished for being upfront about limitations.\n\nARR reviewers are instructed to write a review as if the paper were being considered for the ACL conference, so low scores may indicate the submission is not a good fit for ACL, even if it may be suitable for other specialized venues.\n\nYou can find the full detailed guidelines at the official ARR Reviewer Guidelines page: http://aclrollingreview.org/reviewerguidelines"
    ],
    "durationSeconds": 8.411422384999998
  },
  "sourceToolAssistantUUID": "dd569837-ec96-4036-a752-700177e31a6b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "f49c1ccb-97a0-4961-857d-2db0aa0e0624",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-15T14:58:58.895Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01StVeFknLwn3W9tyTMMz7jk`</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract the complete ARR review form: all scoring dimensions, their scales, descriptions, and any additional required fields. Include the exact scale descriptions for soundness, excitement, overall recommendation, and any other scored dimensions."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e91f9661-bba5-4247-8351-3e7914fef3a4",
  "isSidechain": false,
  "requestId": "req_011Cb4YzcoF1Lm3bkaDjnvnu",
  "type": "assistant",
  "uuid": "7d1f045d-0b04-4852-a2a7-7b3cd9efd6ee",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "f49c1ccb-97a0-4961-857d-2db0aa0e0624",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ACxtx1Mci3DLrexRzQuKmB",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1656,
      "cache_read_input_tokens": 29230,
      "output_tokens": 865,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1656,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 865,
          "cache_read_input_tokens": 29230,
          "cache_creation_input_tokens": 1656,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1656
          },
          "type": "message"
        }
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

_source line 27 · 2026-05-15T14:59:00.078Z_

<details open><summary>🔧 Tool call — Read · `toolu_01HJPGdNHzQo2z1R6ay7Mpx2`</summary>

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
  "parentUuid": "7d1f045d-0b04-4852-a2a7-7b3cd9efd6ee",
  "isSidechain": false,
  "requestId": "req_011Cb4YzcoF1Lm3bkaDjnvnu",
  "type": "assistant",
  "uuid": "1f5dda26-5ecc-4168-b201-215c9f7f8294",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "f49c1ccb-97a0-4961-857d-2db0aa0e0624",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ACxtx1Mci3DLrexRzQuKmB",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1656,
      "cache_read_input_tokens": 29230,
      "output_tokens": 865,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1656,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 865,
          "cache_read_input_tokens": 29230,
          "cache_creation_input_tokens": 1656,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1656
          },
          "type": "message"
        }
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

_source line 28 · 2026-05-15T14:59:00.095Z_

<details><summary>↩ Tool result · `toolu_01HJPGdNHzQo2z1R6ay7Mpx2`</summary>

```text
1	\begin{abstract}
2	Self-consistency---sampling multiple outputs and selecting via agreement---yields large gains on discrete-answer tasks, but information extraction (IE) produces \textit{sets} of entities and relations with partial overlap, where no majority vote exists.
3	Can consistency signals nonetheless select the best among $N$ candidates?
4	
5	Across three NER and one RE benchmark with two 8B-parameter models, all signals achieve strong quality estimation yet none significantly improves sample selection despite 12--18~pp of oracle headroom---the \textit{correlation-selection gap}.
6	Instance-level signals fail by construction; the two mechanisms that \textit{could} bridge the gap also fail: log-probability scores are compressed into effective ties (60\% of instances), and consensus-proximity selection (MBR decoding) correlates with quality across but not within instances.
7	Signal rankings are difficulty-dependent and collapse at the capability boundary.
8	
9	The gap widens with sample size; closing it likely requires per-sample scoring such as trained verifiers.
10	\end{abstract}
11	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1f5dda26-5ecc-4168-b201-215c9f7f8294",
  "isSidechain": false,
  "promptId": "a8cee1eb-a5df-415d-8e30-c85446d1e0a7",
  "type": "user",
  "uuid": "01f5e293-c62f-45f1-a2ff-ce3ff377ced6",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/abstract.tex",
      "content": "\\begin{abstract}\nSelf-consistency---sampling multiple outputs and selecting via agreement---yields large gains on discrete-answer tasks, but information extraction (IE) produces \\textit{sets} of entities and relations with partial overlap, where no majority vote exists.\nCan consistency signals nonetheless select the best among $N$ candidates?\n\nAcross three NER and one RE benchmark with two 8B-parameter models, all signals achieve strong quality estimation yet none significantly improves sample selection despite 12--18~pp of oracle headroom---the \\textit{correlation-selection gap}.\nInstance-level signals fail by construction; the two mechanisms that \\textit{could} bridge the gap also fail: log-probability scores are compressed into effective ties (60\\% of instances), and consensus-proximity selection (MBR decoding) correlates with quality across but not within instances.\nSignal rankings are difficulty-dependent and collapse at the capability boundary.\n\nThe gap widens with sample size; closing it likely requires per-sample scoring such as trained verifiers.\n\\end{abstract}\n",
      "numLines": 11,
      "startLine": 1,
      "totalLines": 11
    }
  },
  "sourceToolAssistantUUID": "1f5dda26-5ecc-4168-b201-215c9f7f8294",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "f49c1ccb-97a0-4961-857d-2db0aa0e0624",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 29 · 2026-05-15T14:59:04.342Z_

<details><summary>↩ Tool result · `toolu_01XQmYjFQsySadtNYNByVocX`</summary>

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
60	@inproceedings{eikema2022sampling,
61	  title = {Sampling-Based Approximations to Minimum {B}ayes Risk Decoding for Neural Machine Translation},
62	  author = {Eikema, Bryan and Aziz, Wilker},
63	  booktitle = {Proceedings of the 2022 Conference on Empirical Methods in Natural Language Processing},
64	  year = {2022},
65	  pages = {10978--10993},
66	  doi = {10.18653/v1/2022.emnlp-main.754}
67	}
68	
69	@inproceedings{fisch2021conformal,
70	  title = {Few-Shot Conformal Prediction with Auxiliary Tasks},
71	  author = {Fisch, Adam and Schuster, Tal and Jaakkola, Tommi and Barzilay, Regina},
72	  booktitle = {ICML 2021},
73	  year = {2021},
74	  doi = {10.5555/3524938.3525234},
75	  url = {https://arxiv.org/abs/2102.08898}
76	}
77	
78	@article{freitag2022high,
79	  title = {High Quality Rather than High Model Probability: Minimum {B}ayes Risk Decoding with Neural Metrics},
80	  author = {Freitag, Markus and Grangier, David and Tan, Qijun and Liang, Bowen},
81	  journal = {Transactions of the Association for Computational Linguistics},
82	  volume = {10},
83	  year = {2022},
84	  pages = {811--825},
85	  doi = {10.1162/tacl_a_00491}
86	}
87	
88	@inproceedings{he2024uncertainty,
89	  title = {Uncertainty Estimation on Sequential Labeling via Uncertainty Transmission},
90	  author = {He, Jianfeng and Yu, Linlin and Lei, Shuo and Lu, Chang-Tien and Chen, Feng},
91	  booktitle = {Findings of the Association for Computational Linguistics: NAACL 2024},
92	  year = {2024},
93	  pages = {2823--2835},
94	  doi = {10.18653/v1/2024.findings-naacl.180}
95	}
96	
97	@article{fleiss1971agreement,
98	  title = {Measuring nominal scale agreement among many raters.},
99	  author = {Fleiss, Joseph L.},
100	  journal = {Psychological Bulletin},
101	  year = {1971},
102	  doi = {10.1037/h0031619},
103	  url = {http://dx.doi.org/10.1037/h0031619}
104	}
105	
106	@inproceedings{gal2016dropout,
107	  title = {Dropout as a Bayesian Approximation: Representing Model Uncertainty in Deep Learning},
108	  author = {Gal, Yarin and Ghahramani, Zoubin},
109	  booktitle = {ICML 2016},
110	  year = {2016},
111	  url = {https://arxiv.org/abs/1506.02142}
112	}
113	
114	@inproceedings{geifman2017selective,
115	  title = {Selective Classification for Deep Neural Networks},
116	  author = {Geifman, Yonatan and El-Yaniv, Ran},
117	  booktitle = {NeurIPS 2017},
118	  year = {2017},
119	  url = {https://arxiv.org/abs/1705.08500}
120	}
121	
122	@article{feng2025optimal,
123	  title = {Optimal Self-Consistency for Efficient Reasoning with Large Language Models},
124	  author = {Feng, Austin and Alonso, Marius and Odonnat, Ambroise},
125	  journal = {arXiv preprint arXiv:2511.12309},
126	  year = {2025},
127	  url = {https://arxiv.org/abs/2511.12309}
128	}
129	
130	@inproceedings{geng2024confidence,
131	  title = {A Survey of Confidence Estimation and Calibration in Large Language Models},
132	  author = {Geng, Jiahui and Cai, Fengyu and Wang, Yuxia and Koeppl, Heinz and Nakov, Preslav and Gurevych, Iryna},
133	  booktitle = {Proceedings of the 2024 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies (Volume 1: Long Papers)},
134	  year = {2024},
135	  doi = {10.18653/v1/2024.naacl-long.366},
136	  url = {http://dx.doi.org/10.18653/v1/2024.naacl-long.366}
137	}
138	
139	@inproceedings{guo2017calibration,
140	  title = {On Calibration of Modern Neural Networks},
141	  author = {Guo, Chuan and Pleiss, Geoff and Sun, Yu and Weinberger, Kilian Q.},
142	  booktitle = {ICML 2017},
143	  year = {2017},
144	  url = {https://arxiv.org/abs/1706.04599}
145	}
146	
147	@article{hobelsberger2025systematic,
148	  title = {Systematic Evaluation of Uncertainty Estimation Methods in Large Language Models},
149	  author = {Hobelsberger, Christian and Winner, Theresa and Nawroth, Andreas and Mitevski, Oliver and Haensch, Anna-Carolina},
150	  journal = {arXiv preprint arXiv:2510.20460},
151	  year = {2025},
152	  url = {https://arxiv.org/abs/2510.20460}
153	}
154	
155	@article{jaccard1901distribution,
156	  title = {Étude comparative de la distribution florale dans une portion des Alpes et du Jura},
157	  author = {Jaccard, Paul},
158	  journal = {Bulletin de la Société Vaudoise des Sciences Naturelles},
159	  year = {1901},
160	  url = {https://www.researchgate.net/publication/225035806}
161	}
162	
163	@inproceedings{josifoski2022genie,
164	  title = {{GenIE}: Generative Information Extraction},
165	  author = {Josifoski, Martin and De Cao, Nicola and Peyrard, Maxime and Petroni, Fabio and West, Robert},
166	  booktitle = {Proceedings of the 2022 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies (NAACL)},
167	  year = {2022},
168	  doi = {10.18653/v1/2022.naacl-main.342},
169	  url = {https://arxiv.org/abs/2112.08340}
170	}
171	
172	@article{kadavath2022language,
173	  title = {Language Models (Mostly) Know What They Know},
174	  author = {Kadavath, Saurav and Conerly, Tom and Askell, Amanda and Henighan, Tom and Drain, Dawn and Perez, Ethan and Schiefer, Nicholas and Hatfield-Dodds, Zac and DasSarma, Nova and Tran-Johnson, Eli and Johnston, Scott and El-Showk, Sheer and Jones, Andy and Elhage, Nelson and Hume, Tristan and Chen, Anna and Bai, Yuntao and Bowman, Sam and Fort, Stanislav and Ganguli, Deep and Hernandez, Danny and Jacobson, Josh and Kernion, Jackson and Kravec, Shauna and Lovitt, Liane and Ndousse, Kamal and Olsson, Catherine and Ringer, Sam and Amodei, Dario and Brown, Tom and Clark, Jack and Joseph, Nicholas and Mann, Ben and McCandlish, Sam and Olah, Chris and Kaplan, Jared},
175	  journal = {arXiv preprint arXiv:2207.05221},
176	  year = {2022},
177	  url = {https://arxiv.org/abs/2207.05221}
178	}
179	
180	@inproceedings{kang2025selfcertainty,
181	  title = {Scalable Best-of-N Selection for Large Language Models via Self-Certainty},
182	  author = {Kang, Zhewei and Zhao, Xuandong and Song, Dawn},
183	  booktitle = {NeurIPS 2025},
184	  year = {2025},
185	  url = {https://arxiv.org/abs/2502.18581}
186	}
187	
188	@inproceedings{kim2024verifiner,
189	  title = {{V}erifi{NER}: Verification-augmented {NER} via Knowledge-grounded Reasoning with Large Language Models},
190	  author = {Kim, Seoyeon and Seo, Kwangwook and Chae, Hyungjoo and Yeo, Jinyoung and Lee, Dongha},
191	  booktitle = {Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)},
192	  year = {2024},
193	  pages = {2441--2461},
194	  doi = {10.18653/v1/2024.acl-long.134}
195	}
196	
197	@inproceedings{kim2026reasc,
198	  title = {Reliability-Aware Adaptive Self-Consistency for Efficient Sampling in {LLM} Reasoning},
199	  author = {Kim, Junseok and Yang, Nakyeong and Min, Kyungmin and Jung, Kyomin},
200	  booktitle = {ACL 2026},
201	  year = {2026},
202	  url = {https://arxiv.org/abs/2601.02970}
203	}
204	
205	@article{kossen2024semantic,
206	  title = {Semantic Entropy Probes: Robust and Cheap Hallucination Detection in {LLMs}},
207	  author = {Kossen, Jannik and Han, Jiatong and Razzak, Muhammed and Schut, Lisa and Malik, Shreshth and Gal, Yarin},
208	  journal = {arXiv preprint arXiv:2406.15927},
209	  year = {2024},
210	  url = {https://arxiv.org/abs/2406.15927}
211	}
212	
213	@article{li2025llms,
214	  title = {LLMs Can Generate a Better Answer by Aggregating Their Own Responses},
215	  author = {Li, Zichong and Feng, Xinyu and Cai, Yuheng and Zhang, Zixuan and Liu, Tianyi and Liang, Chen and Chen, Weizhu and Wang, Haoyu and Zhao, Tuo},
216	  journal = {arXiv preprint arXiv:2503.04104},
217	  year = {2025},
218	  url = {https://arxiv.org/abs/2503.04104}
219	}
220	
221	@inproceedings{kuhn2023semantic,
222	  title = {Semantic Uncertainty: Linguistic Invariances for Uncertainty Estimation in Natural Language Generation},
223	  author = {Kuhn, Lorenz and Gal, Yarin and Farquhar, Sebastian},
224	  booktitle = {ICLR 2023},
225	  year = {2023},
226	  url = {https://arxiv.org/abs/2302.09664}
227	}
228	
229	@inproceedings{malinin2021uncertainty,
230	  title = {Uncertainty Estimation in Autoregressive Structured Prediction},
231	  author = {Malinin, Andrey and Gales, Mark},
232	  booktitle = {International Conference on Learning Representations},
233	  year = {2021},
234	  url = {https://openreview.net/forum?id=jN5y-zb5Q7m}
235	}
236	
237	@inproceedings{lakshminarayanan2017ensembles,
238	  title = {Simple and Scalable Predictive Uncertainty Estimation using Deep Ensembles},
239	  author = {Lakshminarayanan, Balaji and Pritzel, Alexander and Blundell, Charles},
240	  booktitle = {NeurIPS 2017},
241	  year = {2017},
242	  url = {https://arxiv.org/abs/1612.01474}
243	}
244	
245	@inproceedings{li2023codeie,
246	  title = {{CodeIE}: Large Code Generation Models are Better Few-Shot Information Extractors},
247	  author = {Li, Peng and Sun, Tianxiang and Tang, Qiong and Yan, Hang and Wu, Yuanbin and Huang, Xuanjing and Qiu, Xipeng},
248	  booktitle = {Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics (ACL)},
249	  year = {2023},
250	  doi = {10.18653/v1/2023.acl-long.855},
251	  url = {https://arxiv.org/abs/2305.05711}
252	}
253	
254	@inproceedings{lightman2024verify,
255	  title = {Let's Verify Step by Step},
256	  author = {Lightman, Hunter and Kosaraju, Vineet and Burda, Yura and Edwards, Harri and Baker, Bowen and Lee, Teddy and Leike, Jan and Schulman, John and Sutskever, Ilya and Cobbe, Karl},
257	  booktitle = {ICLR 2024},
258	  year = {2024},
259	  url = {https://arxiv.org/abs/2305.20050}
260	}
261	
262	@inproceedings{luan2018scierc,
263	  title = {Multi-Task Identification of Entities, Relations, and Coreference for Scientific Knowledge Graph Construction},
264	  author = {Luan, Yi and He, Luheng and Ostendorf, Mari and Hajishirzi, Hannaneh},
265	  booktitle = {Proceedings of the 2018 Conference on Empirical Methods in Natural Language Processing},
266	  year = {2018},
267	  doi = {10.18653/v1/D18-1360},
268	  url = {http://dx.doi.org/10.18653/v1/D18-1360}
269	}
270	
271	@inproceedings{manakul2023selfcheckgpt,
272	  title = {SelfCheckGPT: Zero-Resource Black-Box Hallucination Detection for Generative Large Language Models},
273	  author = {Manakul, Potsawee and Liusie, Adian and Gales, Mark},
274	  booktitle = {Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing},
275	  year = {2023},
276	  doi = {10.18653/v1/2023.emnlp-main.557},
277	  url = {http://dx.doi.org/10.18653/v1/2023.emnlp-main.557}
278	}
279	
280	@article{nedellec2026consistency,
281	  title = {Consistency–accuracy correlation in hard-prompted LLMs for entity and relation extraction: empirical findings from plant-health data},
282	  author = {Yao, Xinzhi and Nédellec, Claire and Xia, Jingbo and Bossy, Robert},
283	  journal = {Genomics \& Informatics},
284	  year = {2026},
285	  doi = {10.1186/s44342-025-00063-2},
286	  url = {http://dx.doi.org/10.1186/s44342-025-00063-2}
287	}
288	
289	@article{oh2025latentsc,
290	  title = {Latent Self-Consistency for Reliable Majority-Set Selection in Short- and Long-Answer Reasoning},
291	  author = {Oh, Jungsuk and Lee, Jay-Yoon},
292	  journal = {arXiv preprint arXiv:2508.18395},
293	  year = {2025},
294	  url = {https://arxiv.org/abs/2508.18395}
295	}
296	
297	@inproceedings{sainz2024gollie,
298	  title = {{GoLLIE}: Annotation Guidelines improve Zero-Shot Information-Extraction},
299	  author = {Sainz, Oscar and García-Ferrero, Iker and Agerri, Rodrigo and Lacalle, Oier Lopez de and Rigau, German and Agirre, Eneko},
300	  booktitle = {ICLR 2024},
301	  year = {2024},
302	  url = {https://arxiv.org/abs/2310.03668}
303	}
304	
305	@inproceedings{shelmanov2021active,
306	  title = {Active Learning for Sequence Tagging with Deep Pre-trained Models and Bayesian Uncertainty Estimates},
307	  author = {Shelmanov, Artem and Puzyrev, Dmitri and Kupriyanova, Lyubov and Belyakov, Denis and Larionov, Daniil and Khromov, Nikita and Kozlova, Olga and Artemova, Ekaterina and Dylov, Dmitry V. and Panchenko, Alexander},
308	  booktitle = {Proceedings of the 16th Conference of the European Chapter of the Association for Computational Linguistics: Main Volume},
309	  year = {2021},
310	  doi = {10.18653/v1/2021.eacl-main.145},
311	  url = {http://dx.doi.org/10.18653/v1/2021.eacl-main.145}
312	}
313	
314	@inproceedings{snell2025scaling,
315	  title = {Scaling {LLM} Test-Time Compute Optimally can be More Effective than Scaling Model Parameters},
316	  author = {Snell, Charlie and Lee, Jaehoon and Xu, Kelvin and Kumar, Aviral},
317	  booktitle = {Proceedings of the International Conference on Learning Representations (ICLR)},
318	  year = {2025},
319	  url = {https://arxiv.org/abs/2408.03314}
320	}
321	
322	@inproceedings{taubenfeld2025cisc,
323	  title = {Confidence Improves Self-Consistency in LLMs},
324	  author = {Taubenfeld, Amir and Sheffer, Tom and Ofek, Eran and Feder, Amir and Goldstein, Ariel and Gekhman, Zorik and Yona, Gal},
325	  booktitle = {Findings of the Association for Computational Linguistics: ACL 2025},
326	  year = {2025},
327	  doi = {10.18653/v1/2025.findings-acl.1030},
328	  url = {http://dx.doi.org/10.18653/v1/2025.findings-acl.1030}
329	}
330	
331	@inproceedings{thirukovalluru2024atomic,
332	  title = {Atomic Self-Consistency for Better Long Form Generations},
333	  author = {Thirukovalluru, Raghuveer and Huang, Yukun and Dhingra, Bhuwan},
334	  booktitle = {Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing},
335	  year = {2024},
336	  doi = {10.18653/v1/2024.emnlp-main.706},
337	  url = {http://dx.doi.org/10.18653/v1/2024.emnlp-main.706}
338	}
339	
340	@inproceedings{tjongkimsang2003conll,
341	  title = {Introduction to the {CoNLL}-2003 Shared Task: Language-Independent Named Entity Recognition},
342	  author = {Sang, Erik F. Tjong Kim and Meulder, Fien De},
343	  booktitle = {CoNLL 2003},
344	  year = {2003},
345	  url = {https://aclanthology.org/W03-0419/}
346	}
347	
348	@inproceedings{vashurin2025cocoa,
349	  title = {Uncertainty Quantification for {LLMs} through Minimum Bayes Risk: Bridging Confidence and Consistency},
350	  author = {Vashurin, Roman and Goloburda, Maiya and Ilina, Albina and Rubashevskii, Aleksandr and Nakov, Preslav and Shelmanov, Artem and Panov, Maxim},
351	  booktitle = {NeurIPS 2025},
352	  year = {2025},
353	  url = {https://arxiv.org/abs/2502.04964}
354	}
355	
356	@inproceedings{wadhwa2023revisiting,
357	  title = {Revisiting Relation Extraction in the era of Large Language Models},
358	  author = {Wadhwa, Somin and Amir, Silvio and Wallace, Byron},
359	  booktitle = {Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)},
360	  year = {2023},
361	  doi = {10.18653/v1/2023.acl-long.868},
362	  url = {http://dx.doi.org/10.18653/v1/2023.acl-long.868}
363	}
364	
365	@article{wang2023instructuie,
366	  title = {{InstructUIE}: Multi-task Instruction Tuning for Unified Information Extraction},
367	  author = {Wang, Xiao and Zhou, Weikang and Zu, Can and Xia, Han and Chen, Tianze and Zhang, Yuansen and Zheng, Rui and Ye, Junjie and Zhang, Qi and Gui, Tao and Kang, Jihua and Yang, Jingsheng and Li, Siyuan and Du, Chunsai},
368	  journal = {arXiv preprint arXiv:2304.08085},
369	  year = {2023},
370	  url = {https://arxiv.org/abs/2304.08085}
371	}
372	
373	@inproceedings{wang2023selfconsistency,
374	  title = {Self-Consistency Improves Chain of Thought Reasoning in Language Models},
375	  author = {Wang, Xuezhi and Wei, Jason and Schuurmans, Dale and Le, Quoc and Chi, Ed and Narang, Sharan and Chowdhery, Aakanksha and Zhou, Denny},
376	  booktitle = {ICLR 2023},
377	  year = {2023},
378	  url = {https://arxiv.org/abs/2203.11171}
379	}
380	
381	@inproceedings{wang2025make,
382	  title = {Make Every Penny Count: Difficulty-Adaptive Self-Consistency for Cost-Efficient Reasoning},
383	  author = {Wang, Xinglin and Feng, Shaoxiong and Li, Yiwei and Yuan, Peiwen and Zhang, Yueqi and Tan, Chuyi and Pan, Boyuan and Hu, Yao and Li, Kan},
384	  booktitle = {Findings of the Association for Computational Linguistics: NAACL 2025},
385	  pages = {6919--6932},
386	  year = {2025}
387	}
388	
389	@inproceedings{wang2024mathshepherd,
390	  title = {Math-Shepherd: Verify and Reinforce {LLMs} Step-by-step without Human Annotations},
391	  author = {Wang, Peiyi and Li, Lei and Shao, Zhihong and Xu, Runxin and Dai, Damai and Li, Yifei and Chen, Deli and Wu, Yu and Sui, Zhifang},
392	  booktitle = {ACL 2024},
393	  year = {2024},
394	  url = {https://arxiv.org/abs/2312.08935}
395	}
396	
397	@inproceedings{wang2025rankedvoting,
398	  title = {Ranked Voting based Self-Consistency of Large Language Models},
399	  author = {Wang, Weiqin and Wang, Yile and Huang, Hui},
400	  booktitle = {ACL Findings 2025},
401	  year = {2025},
402	  url = {https://arxiv.org/abs/2505.10772}
403	}
404	
405	@article{wen2025know,
406	  title = {Know Your Limits: A Survey of Abstention in Large Language Models},
407	  author = {Wen, Bingbing and Yao, Jihan and Feng, Shangbin and Xu, Chenjun and Tsvetkov, Yulia and Howe, Bill and Wang, Lucy Lu},
408	  journal = {Transactions of the Association for Computational Linguistics},
409	  year = {2025},
410	  doi = {10.1162/tacl_a_00754},
411	  url = {http://dx.doi.org/10.1162/tacl_a_00754}
412	}
413	
414	@article{willard2023guided,
415	  title = {Efficient Guided Generation for Large Language Models},
416	  author = {Willard, Brandon T. and Louf, Rémi},
417	  journal = {arXiv preprint arXiv:2307.09702},
418	  year = {2023},
419	  url = {https://arxiv.org/abs/2307.09702}
420	}
421	
422	@inproceedings{xia2025survey,
423	  title = {A Survey of Uncertainty Estimation Methods on Large Language Models},
424	  author = {Xia, Zhiqiu and Xu, Jinxuan and Zhang, Yuqian and Liu, Hang},
425	  booktitle = {ACL Findings 2025},
426	  year = {2025},
427	  url = {https://aclanthology.org/2025.findings-acl.1101/}
428	}
429	
430	@article{xiao2019uncertainty,
431	  title = {Quantifying Uncertainties in Natural Language Processing Tasks},
432	  author = {Xiao, Yijun and Wang, William Yang},
433	  journal = {Proceedings of the AAAI Conference on Artificial Intelligence},
434	  year = {2019},
435	  doi = {10.1609/aaai.v33i01.33017322},
436	  url = {http://dx.doi.org/10.1609/aaai.v33i01.33017322}
437	}
438	
439	@inproceedings{zhang2023ener,
440	  title = {E-NER: Evidential Deep Learning for Trustworthy Named Entity Recognition},
441	  author = {Zhang, Zhen and Hu, Mengting and Zhao, Shiwan and Huang, Minlie and Wang, Haotian and Liu, Lemao and Zhang, Zhirui and Liu, Zhe and Wu, Bingzhe},
442	  booktitle = {Findings of the Association for Computational Linguistics: ACL 2023},
443	  year = {2023},
444	  doi = {10.18653/v1/2023.findings-acl.103},
445	  url = {http://dx.doi.org/10.18653/v1/2023.findings-acl.103}
446	}
447	
448	@inproceedings{zheng2024llamafactory,
449	  title = {{L}lama{F}actory: Unified Efficient Fine-Tuning of 100+ Language Models},
450	  author = {Zheng, Yaowei and Zhang, Richong and Zhang, Junhao and Ye, Yanhan and Luo, Zheyan},
451	  booktitle = {Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (Volume 3: System Demonstrations)},
452	  year = {2024},
453	  pages = {400--410},
454	  doi = {10.18653/v1/2024.acl-demos.38}
455	}
456	
457	@inproceedings{zhou2024uniner,
458	  title = {{UniversalNER}: Targeted Distillation from Large Language Models for Open Named Entity Recognition},
459	  author = {Zhou, Wenxuan and Zhang, Sheng and Gu, Yu and Chen, Muhao and Poon, Hoifung},
460	  booktitle = {Proceedings of the International Conference on Learning Representations (ICLR)},
461	  year = {2024},
462	  url = {https://arxiv.org/abs/2308.03279}
463	}
464	
465	@inproceedings{xiong2024llm,
466	  title = {Can {LLMs} Express Their Uncertainty? An Empirical Evaluation of Confidence Elicitation in {LLMs}},
467	  author = {Xiong, Miao and Hu, Zhiyuan and Lu, Xinyang and Li, Yifei and Fu, Jie and He, Junxian and Hooi, Bryan},
468	  booktitle = {Proceedings of the International Conference on Learning Representations (ICLR)},
469	  year = {2024},
470	  url = {https://arxiv.org/abs/2306.13063}
471	}
472	
473	@inproceedings{muller2021understanding,
474	  title = {Understanding the Properties of Minimum {Bayes} Risk Decoding in Neural Machine Translation},
475	  author = {M{\"u}ller, Mathias and Sennrich, Rico},
476	  booktitle = {Proceedings of the 59th Annual Meeting of the Association for Computational Linguistics (ACL)},
477	  year = {2021},
478	  url = {https://arxiv.org/abs/2105.08504}
479	}
480	
481	@inproceedings{heo2025uncertainty,
482	  title = {Do {LLMs} Estimate Uncertainty Well in Instruction Following?},
483	  author = {Heo, Juyeon and Xiong, Miao and Heinze-Deml, Christina and Narain, Jaya},
484	  booktitle = {Proceedings of the International Conference on Learning Representations (ICLR)},
485	  year = {2025},
486	  url = {https://arxiv.org/abs/2410.14582}
487	}
488	
489	@inproceedings{eikema2025structured,
490	  title = {Structure-Conditional Minimum {B}ayes Risk Decoding},
491	  author = {Eikema, Bryan and Rutkiewicz, Anna and Giulianelli, Mario},
492	  booktitle = {Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing},
493	  year = {2025},
494	  url = {https://arxiv.org/abs/2510.20700}
495	}
496	
497	@article{zhang2025tts,
498	  title = {A Survey on Test-Time Scaling in Large Language Models: What, How, Where, and How Well?},
499	  author = {Zhang, Qiyuan and Lyu, Fuyuan and Sun, Zexu and Wang, Lei and Zhang, Weixu and Guo, Zhihan and Wang, Yufei},
500	  journal = {arXiv preprint arXiv:2503.24235},
501	  year = {2025},
502	  url = {https://arxiv.org/abs/2503.24235}
503	}
504	
505	@article{venktesh2025trust,
506	  title = {Trust but Verify! A Survey on Verification Design for Test-time Scaling},
507	  author = {Venktesh, V and Rathee, Mandeep and Anand, Avishek},
508	  journal = {arXiv preprint arXiv:2508.16665},
509	  year = {2025},
510	  url = {https://arxiv.org/abs/2508.16665}
511	}
512	
513	@inproceedings{jinnai2024mbr,
514	  title = {Model-Based Minimum {B}ayes Risk Decoding for Text Generation},
515	  author = {Jinnai, Yuu and Morimura, Tetsuro and Honda, Ukyo and Ariu, Kaito and Abe, Kenshi},
516	  booktitle = {Proceedings of the 41st International Conference on Machine Learning (ICML)},
517	  year = {2024},
518	  url = {https://arxiv.org/abs/2311.05263}
519	}
520	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b3b04bb9-807e-43b6-bbc9-852751bfd6f4",
  "isSidechain": false,
  "promptId": "a8cee1eb-a5df-415d-8e30-c85446d1e0a7",
  "type": "user",
  "uuid": "943e98ae-b387-4e40-99e2-065741656508",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/references.bib",
      "content": "% Auto-generated from literature_map.yaml — do not edit manually\n\n@inproceedings{angelopoulos2021conformal,\n  title = {Uncertainty Sets for Image Classifiers using Conformal Prediction},\n  author = {Angelopoulos, Anastasios N. and Bates, Stephen and Malik, Jitendra and Jordan, Michael I.},\n  booktitle = {ICLR 2021},\n  year = {2021},\n  url = {https://arxiv.org/abs/2009.14193}\n}\n\n@article{brown2024monkeys,\n  title = {Large Language Monkeys: Scaling Inference Compute with Repeated Sampling},\n  author = {Brown, Bradley and Juravsky, Jordan and Ehrlich, Ryan and Clark, Ronald and Le, Quoc V. and Ré, Christopher and Mirhoseini, Azalia},\n  journal = {arXiv preprint arXiv:2407.21787},\n  year = {2024},\n  url = {https://arxiv.org/abs/2407.21787}\n}\n\n@inproceedings{chen2024usc,\n  title = {Universal Self-Consistency for Large Language Model Generation},\n  author = {Chen, Xinyun and Aksitov, Renat and Alon, Uri and Ren, Jie and Xiao, Kefan and Yin, Pengcheng and Prakash, Sushant and Sutton, Charles and Wang, Xuezhi and Zhou, Denny},\n  booktitle = {arXiv preprint (ICML 2024 Workshop ICL)},\n  year = {2024},\n  url = {https://arxiv.org/abs/2311.17311}\n}\n\n@article{cobbe2021verifiers,\n  title = {Training Verifiers to Solve Math Word Problems},\n  author = {Cobbe, Karl and Kosaraju, Vineet and Bavarian, Mohammad and Chen, Mark and Jun, Heewoo and Kaiser, Lukasz and Plappert, Matthias and Tworek, Jerry and Hilton, Jacob and Nakano, Reiichiro and Hesse, Christopher and Schulman, John},\n  journal = {arXiv preprint arXiv:2110.14168},\n  year = {2021},\n  url = {https://arxiv.org/abs/2110.14168}\n}\n\n@inproceedings{culotta2004confidence,\n  title = {Confidence Estimation for Information Extraction},\n  author = {Culotta, Aron and McCallum, Andrew},\n  booktitle = {HLT-NAACL 2004},\n  year = {2004},\n  url = {https://aclanthology.org/N04-4028/}\n}\n\n@inproceedings{derczynski2017wnut,\n  title = {Results of the WNUT2017 Shared Task on Novel and Emerging Entity Recognition},\n  author = {Derczynski, Leon and Nichols, Eric and Erp, Marieke van and Limsopatham, Nut},\n  booktitle = {W-NUT Workshop at EMNLP 2017},\n  year = {2017},\n  url = {https://aclanthology.org/W17-4418/}\n}\n\n@inproceedings{desai2020calibration,\n  title = {Calibration of Pre-trained Transformers},\n  author = {Desai, Shrey and Durrett, Greg},\n  booktitle = {Proceedings of the 2020 Conference on Empirical Methods in Natural Language Processing (EMNLP)},\n  year = {2020},\n  doi = {10.18653/v1/2020.emnlp-main.21},\n  url = {http://dx.doi.org/10.18653/v1/2020.emnlp-main.21}\n}\n\n@inproceedings{eikema2022sampling,\n  title = {Sampling-Based Approximations to Minimum {B}ayes Risk Decoding for Neural Machine Translation},\n  author = {Eikema, Bryan and Aziz, Wilker},\n  booktitle = {Proceedings of the 2022 Conference on Empirical Methods in Natural Language Processing},\n  year = {2022},\n  pages = {10978--10993},\n  doi = {10.18653/v1/2022.emnlp-main.754}\n}\n\n@inproceedings{fisch2021conformal,\n  title = {Few-Shot Conformal Prediction with Auxiliary Tasks},\n  author = {Fisch, Adam and Schuster, Tal and Jaakkola, Tommi and Barzilay, Regina},\n  booktitle = {ICML 2021},\n  year = {2021},\n  doi = {10.5555/3524938.3525234},\n  url = {https://arxiv.org/abs/2102.08898}\n}\n\n@article{freitag2022high,\n  title = {High Quality Rather than High Model Probability: Minimum {B}ayes Risk Decoding with Neural Metrics},\n  author = {Freitag, Markus and Grangier, David and Tan, Qijun and Liang, Bowen},\n  journal = {Transactions of the Association for Computational Linguistics},\n  volume = {10},\n  year = {2022},\n  pages = {811--825},\n  doi = {10.1162/tacl_a_00491}\n}\n\n@inproceedings{he2024uncertainty,\n  title = {Uncertainty Estimation on Sequential Labeling via Uncertainty Transmission},\n  author = {He, Jianfeng and Yu, Linlin and Lei, Shuo and Lu, Chang-Tien and Chen, Feng},\n  booktitle = {Findings of the Association for Computational Linguistics: NAACL 2024},\n  year = {2024},\n  pages = {2823--2835},\n  doi = {10.18653/v1/2024.findings-naacl.180}\n}\n\n@article{fleiss1971agreement,\n  title = {Measuring nominal scale agreement among many raters.},\n  author = {Fleiss, Joseph L.},\n  journal = {Psychological Bulletin},\n  year = {1971},\n  doi = {10.1037/h0031619},\n  url = {http://dx.doi.org/10.1037/h0031619}\n}\n\n@inproceedings{gal2016dropout,\n  title = {Dropout as a Bayesian Approximation: Representing Model Uncertainty in Deep Learning},\n  author = {Gal, Yarin and Ghahramani, Zoubin},\n  booktitle = {ICML 2016},\n  year = {2016},\n  url = {https://arxiv.org/abs/1506.02142}\n}\n\n@inproceedings{geifman2017selective,\n  title = {Selective Classification for Deep Neural Networks},\n  author = {Geifman, Yonatan and El-Yaniv, Ran},\n  booktitle = {NeurIPS 2017},\n  year = {2017},\n  url = {https://arxiv.org/abs/1705.08500}\n}\n\n@article{feng2025optimal,\n  title = {Optimal Self-Consistency for Efficient Reasoning with Large Language Models},\n  author = {Feng, Austin and Alonso, Marius and Odonnat, Ambroise},\n  journal = {arXiv preprint arXiv:2511.12309},\n  year = {2025},\n  url = {https://arxiv.org/abs/2511.12309}\n}\n\n@inproceedings{geng2024confidence,\n  title = {A Survey of Confidence Estimation and Calibration in Large Language Models},\n  author = {Geng, Jiahui and Cai, Fengyu and Wang, Yuxia and Koeppl, Heinz and Nakov, Preslav and Gurevych, Iryna},\n  booktitle = {Proceedings of the 2024 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies (Volume 1: Long Papers)},\n  year = {2024},\n  doi = {10.18653/v1/2024.naacl-long.366},\n  url = {http://dx.doi.org/10.18653/v1/2024.naacl-long.366}\n}\n\n@inproceedings{guo2017calibration,\n  title = {On Calibration of Modern Neural Networks},\n  author = {Guo, Chuan and Pleiss, Geoff and Sun, Yu and Weinberger, Kilian Q.},\n  booktitle = {ICML 2017},\n  year = {2017},\n  url = {https://arxiv.org/abs/1706.04599}\n}\n\n@article{hobelsberger2025systematic,\n  title = {Systematic Evaluation of Uncertainty Estimation Methods in Large Language Models},\n  author = {Hobelsberger, Christian and Winner, Theresa and Nawroth, Andreas and Mitevski, Oliver and Haensch, Anna-Carolina},\n  journal = {arXiv preprint arXiv:2510.20460},\n  year = {2025},\n  url = {https://arxiv.org/abs/2510.20460}\n}\n\n@article{jaccard1901distribution,\n  title = {Étude comparative de la distribution florale dans une portion des Alpes et du Jura},\n  author = {Jaccard, Paul},\n  journal = {Bulletin de la Société Vaudoise des Sciences Naturelles},\n  year = {1901},\n  url = {https://www.researchgate.net/publication/225035806}\n}\n\n@inproceedings{josifoski2022genie,\n  title = {{GenIE}: Generative Information Extraction},\n  author = {Josifoski, Martin and De Cao, Nicola and Peyrard, Maxime and Petroni, Fabio and West, Robert},\n  booktitle = {Proceedings of the 2022 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies (NAACL)},\n  year = {2022},\n  doi = {10.18653/v1/2022.naacl-main.342},\n  url = {https://arxiv.org/abs/2112.08340}\n}\n\n@article{kadavath2022language,\n  title = {Language Models (Mostly) Know What They Know},\n  author = {Kadavath, Saurav and Conerly, Tom and Askell, Amanda and Henighan, Tom and Drain, Dawn and Perez, Ethan and Schiefer, Nicholas and Hatfield-Dodds, Zac and DasSarma, Nova and Tran-Johnson, Eli and Johnston, Scott and El-Showk, Sheer and Jones, Andy and Elhage, Nelson and Hume, Tristan and Chen, Anna and Bai, Yuntao and Bowman, Sam and Fort, Stanislav and Ganguli, Deep and Hernandez, Danny and Jacobson, Josh and Kernion, Jackson and Kravec, Shauna and Lovitt, Liane and Ndousse, Kamal and Olsson, Catherine and Ringer, Sam and Amodei, Dario and Brown, Tom and Clark, Jack and Joseph, Nicholas and Mann, Ben and McCandlish, Sam and Olah, Chris and Kaplan, Jared},\n  journal = {arXiv preprint arXiv:2207.05221},\n  year = {2022},\n  url = {https://arxiv.org/abs/2207.05221}\n}\n\n@inproceedings{kang2025selfcertainty,\n  title = {Scalable Best-of-N Selection for Large Language Models via Self-Certainty},\n  author = {Kang, Zhewei and Zhao, Xuandong and Song, Dawn},\n  booktitle = {NeurIPS 2025},\n  year = {2025},\n  url = {https://arxiv.org/abs/2502.18581}\n}\n\n@inproceedings{kim2024verifiner,\n  title = {{V}erifi{NER}: Verification-augmented {NER} via Knowledge-grounded Reasoning with Large Language Models},\n  author = {Kim, Seoyeon and Seo, Kwangwook and Chae, Hyungjoo and Yeo, Jinyoung and Lee, Dongha},\n  booktitle = {Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)},\n  year = {2024},\n  pages = {2441--2461},\n  doi = {10.18653/v1/2024.acl-long.134}\n}\n\n@inproceedings{kim2026reasc,\n  title = {Reliability-Aware Adaptive Self-Consistency for Efficient Sampling in {LLM} Reasoning},\n  author = {Kim, Junseok and Yang, Nakyeong and Min, Kyungmin and Jung, Kyomin},\n  booktitle = {ACL 2026},\n  year = {2026},\n  url = {https://arxiv.org/abs/2601.02970}\n}\n\n@article{kossen2024semantic,\n  title = {Semantic Entropy Probes: Robust and Cheap Hallucination Detection in {LLMs}},\n  author = {Kossen, Jannik and Han, Jiatong and Razzak, Muhammed and Schut, Lisa and Malik, Shreshth and Gal, Yarin},\n  journal = {arXiv preprint arXiv:2406.15927},\n  year = {2024},\n  url = {https://arxiv.org/abs/2406.15927}\n}\n\n@article{li2025llms,\n  title = {LLMs Can Generate a Better Answer by Aggregating Their Own Responses},\n  author = {Li, Zichong and Feng, Xinyu and Cai, Yuheng and Zhang, Zixuan and Liu, Tianyi and Liang, Chen and Chen, Weizhu and Wang, Haoyu and Zhao, Tuo},\n  journal = {arXiv preprint arXiv:2503.04104},\n  year = {2025},\n  url = {https://arxiv.org/abs/2503.04104}\n}\n\n@inproceedings{kuhn2023semantic,\n  title = {Semantic Uncertainty: Linguistic Invariances for Uncertainty Estimation in Natural Language Generation},\n  author = {Kuhn, Lorenz and Gal, Yarin and Farquhar, Sebastian},\n  booktitle = {ICLR 2023},\n  year = {2023},\n  url = {https://arxiv.org/abs/2302.09664}\n}\n\n@inproceedings{malinin2021uncertainty,\n  title = {Uncertainty Estimation in Autoregressive Structured Prediction},\n  author = {Malinin, Andrey and Gales, Mark},\n  booktitle = {International Conference on Learning Representations},\n  year = {2021},\n  url = {https://openreview.net/forum?id=jN5y-zb5Q7m}\n}\n\n@inproceedings{lakshminarayanan2017ensembles,\n  title = {Simple and Scalable Predictive Uncertainty Estimation using Deep Ensembles},\n  author = {Lakshminarayanan, Balaji and Pritzel, Alexander and Blundell, Charles},\n  booktitle = {NeurIPS 2017},\n  year = {2017},\n  url = {https://arxiv.org/abs/1612.01474}\n}\n\n@inproceedings{li2023codeie,\n  title = {{CodeIE}: Large Code Generation Models are Better Few-Shot Information Extractors},\n  author = {Li, Peng and Sun, Tianxiang and Tang, Qiong and Yan, Hang and Wu, Yuanbin and Huang, Xuanjing and Qiu, Xipeng},\n  booktitle = {Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics (ACL)},\n  year = {2023},\n  doi = {10.18653/v1/2023.acl-long.855},\n  url = {https://arxiv.org/abs/2305.05711}\n}\n\n@inproceedings{lightman2024verify,\n  title = {Let's Verify Step by Step},\n  author = {Lightman, Hunter and Kosaraju, Vineet and Burda, Yura and Edwards, Harri and Baker, Bowen and Lee, Teddy and Leike, Jan and Schulman, John and Sutskever, Ilya and Cobbe, Karl},\n  booktitle = {ICLR 2024},\n  year = {2024},\n  url = {https://arxiv.org/abs/2305.20050}\n}\n\n@inproceedings{luan2018scierc,\n  title = {Multi-Task Identification of Entities, Relations, and Coreference for Scientific Knowledge Graph Construction},\n  author = {Luan, Yi and He, Luheng and Ostendorf, Mari and Hajishirzi, Hannaneh},\n  booktitle = {Proceedings of the 2018 Conference on Empirical Methods in Natural Language Processing},\n  year = {2018},\n  doi = {10.18653/v1/D18-1360},\n  url = {http://dx.doi.org/10.18653/v1/D18-1360}\n}\n\n@inproceedings{manakul2023selfcheckgpt,\n  title = {SelfCheckGPT: Zero-Resource Black-Box Hallucination Detection for Generative Large Language Models},\n  author = {Manakul, Potsawee and Liusie, Adian and Gales, Mark},\n  booktitle = {Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing},\n  year = {2023},\n  doi = {10.18653/v1/2023.emnlp-main.557},\n  url = {http://dx.doi.org/10.18653/v1/2023.emnlp-main.557}\n}\n\n@article{nedellec2026consistency,\n  title = {Consistency–accuracy correlation in hard-prompted LLMs for entity and relation extraction: empirical findings from plant-health data},\n  author = {Yao, Xinzhi and Nédellec, Claire and Xia, Jingbo and Bossy, Robert},\n  journal = {Genomics \\& Informatics},\n  year = {2026},\n  doi = {10.1186/s44342-025-00063-2},\n  url = {http://dx.doi.org/10.1186/s44342-025-00063-2}\n}\n\n@article{oh2025latentsc,\n  title = {Latent Self-Consistency for Reliable Majority-Set Selection in Short- and Long-Answer Reasoning},\n  author = {Oh, Jungsuk and Lee, Jay-Yoon},\n  journal = {arXiv preprint arXiv:2508.18395},\n  year = {2025},\n  url = {https://arxiv.org/abs/2508.18395}\n}\n\n@inproceedings{sainz2024gollie,\n  title = {{GoLLIE}: Annotation Guidelines improve Zero-Shot Information-Extraction},\n  author = {Sainz, Oscar and García-Ferrero, Iker and Agerri, Rodrigo and Lacalle, Oier Lopez de and Rigau, German and Agirre, Eneko},\n  booktitle = {ICLR 2024},\n  year = {2024},\n  url = {https://arxiv.org/abs/2310.03668}\n}\n\n@inproceedings{shelmanov2021active,\n  title = {Active Learning for Sequence Tagging with Deep Pre-trained Models and Bayesian Uncertainty Estimates},\n  author = {Shelmanov, Artem and Puzyrev, Dmitri and Kupriyanova, Lyubov and Belyakov, Denis and Larionov, Daniil and Khromov, Nikita and Kozlova, Olga and Artemova, Ekaterina and Dylov, Dmitry V. and Panchenko, Alexander},\n  booktitle = {Proceedings of the 16th Conference of the European Chapter of the Association for Computational Linguistics: Main Volume},\n  year = {2021},\n  doi = {10.18653/v1/2021.eacl-main.145},\n  url = {http://dx.doi.org/10.18653/v1/2021.eacl-main.145}\n}\n\n@inproceedings{snell2025scaling,\n  title = {Scaling {LLM} Test-Time Compute Optimally can be More Effective than Scaling Model Parameters},\n  author = {Snell, Charlie and Lee, Jaehoon and Xu, Kelvin and Kumar, Aviral},\n  booktitle = {Proceedings of the International Conference on Learning Representations (ICLR)},\n  year = {2025},\n  url = {https://arxiv.org/abs/2408.03314}\n}\n\n@inproceedings{taubenfeld2025cisc,\n  title = {Confidence Improves Self-Consistency in LLMs},\n  author = {Taubenfeld, Amir and Sheffer, Tom and Ofek, Eran and Feder, Amir and Goldstein, Ariel and Gekhman, Zorik and Yona, Gal},\n  booktitle = {Findings of the Association for Computational Linguistics: ACL 2025},\n  year = {2025},\n  doi = {10.18653/v1/2025.findings-acl.1030},\n  url = {http://dx.doi.org/10.18653/v1/2025.findings-acl.1030}\n}\n\n@inproceedings{thirukovalluru2024atomic,\n  title = {Atomic Self-Consistency for Better Long Form Generations},\n  author = {Thirukovalluru, Raghuveer and Huang, Yukun and Dhingra, Bhuwan},\n  booktitle = {Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing},\n  year = {2024},\n  doi = {10.18653/v1/2024.emnlp-main.706},\n  url = {http://dx.doi.org/10.18653/v1/2024.emnlp-main.706}\n}\n\n@inproceedings{tjongkimsang2003conll,\n  title = {Introduction to the {CoNLL}-2003 Shared Task: Language-Independent Named Entity Recognition},\n  author = {Sang, Erik F. Tjong Kim and Meulder, Fien De},\n  booktitle = {CoNLL 2003},\n  year = {2003},\n  url = {https://aclanthology.org/W03-0419/}\n}\n\n@inproceedings{vashurin2025cocoa,\n  title = {Uncertainty Quantification for {LLMs} through Minimum Bayes Risk: Bridging Confidence and Consistency},\n  author = {Vashurin, Roman and Goloburda, Maiya and Ilina, Albina and Rubashevskii, Aleksandr and Nakov, Preslav and Shelmanov, Artem and Panov, Maxim},\n  booktitle = {NeurIPS 2025},\n  year = {2025},\n  url = {https://arxiv.org/abs/2502.04964}\n}\n\n@inproceedings{wadhwa2023revisiting,\n  title = {Revisiting Relation Extraction in the era of Large Language Models},\n  author = {Wadhwa, Somin and Amir, Silvio and Wallace, Byron},\n  booktitle = {Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)},\n  year = {2023},\n  doi = {10.18653/v1/2023.acl-long.868},\n  url = {http://dx.doi.org/10.18653/v1/2023.acl-long.868}\n}\n\n@article{wang2023instructuie,\n  title = {{InstructUIE}: Multi-task Instruction Tuning for Unified Information Extraction},\n  author = {Wang, Xiao and Zhou, Weikang and Zu, Can and Xia, Han and Chen, Tianze and Zhang, Yuansen and Zheng, Rui and Ye, Junjie and Zhang, Qi and Gui, Tao and Kang, Jihua and Yang, Jingsheng and Li, Siyuan and Du, Chunsai},\n  journal = {arXiv preprint arXiv:2304.08085},\n  year = {2023},\n  url = {https://arxiv.org/abs/2304.08085}\n}\n\n@inproceedings{wang2023selfconsistency,\n  title = {Self-Consistency Improves Chain of Thought Reasoning in Language Models},\n  author = {Wang, Xuezhi and Wei, Jason and Schuurmans, Dale and Le, Quoc and Chi, Ed and Narang, Sharan and Chowdhery, Aakanksha and Zhou, Denny},\n  booktitle = {ICLR 2023},\n  year = {2023},\n  url = {https://arxiv.org/abs/2203.11171}\n}\n\n@inproceedings{wang2025make,\n  title = {Make Every Penny Count: Difficulty-Adaptive Self-Consistency for Cost-Efficient Reasoning},\n  author = {Wang, Xinglin and Feng, Shaoxiong and Li, Yiwei and Yuan, Peiwen and Zhang, Yueqi and Tan, Chuyi and Pan, Boyuan and Hu, Yao and Li, Kan},\n  booktitle = {Findings of the Association for Computational Linguistics: NAACL 2025},\n  pages = {6919--6932},\n  year = {2025}\n}\n\n@inproceedings{wang2024mathshepherd,\n  title = {Math-Shepherd: Verify and Reinforce {LLMs} Step-by-step without Human Annotations},\n  author = {Wang, Peiyi and Li, Lei and Shao, Zhihong and Xu, Runxin and Dai, Damai and Li, Yifei and Chen, Deli and Wu, Yu and Sui, Zhifang},\n  booktitle = {ACL 2024},\n  year = {2024},\n  url = {https://arxiv.org/abs/2312.08935}\n}\n\n@inproceedings{wang2025rankedvoting,\n  title = {Ranked Voting based Self-Consistency of Large Language Models},\n  author = {Wang, Weiqin and Wang, Yile and Huang, Hui},\n  booktitle = {ACL Findings 2025},\n  year = {2025},\n  url = {https://arxiv.org/abs/2505.10772}\n}\n\n@article{wen2025know,\n  title = {Know Your Limits: A Survey of Abstention in Large Language Models},\n  author = {Wen, Bingbing and Yao, Jihan and Feng, Shangbin and Xu, Chenjun and Tsvetkov, Yulia and Howe, Bill and Wang, Lucy Lu},\n  journal = {Transactions of the Association for Computational Linguistics},\n  year = {2025},\n  doi = {10.1162/tacl_a_00754},\n  url = {http://dx.doi.org/10.1162/tacl_a_00754}\n}\n\n@article{willard2023guided,\n  title = {Efficient Guided Generation for Large Language Models},\n  author = {Willard, Brandon T. and Louf, Rémi},\n  journal = {arXiv preprint arXiv:2307.09702},\n  year = {2023},\n  url = {https://arxiv.org/abs/2307.09702}\n}\n\n@inproceedings{xia2025survey,\n  title = {A Survey of Uncertainty Estimation Methods on Large Language Models},\n  author = {Xia, Zhiqiu and Xu, Jinxuan and Zhang, Yuqian and Liu, Hang},\n  booktitle = {ACL Findings 2025},\n  year = {2025},\n  url = {https://aclanthology.org/2025.findings-acl.1101/}\n}\n\n@article{xiao2019uncertainty,\n  title = {Quantifying Uncertainties in Natural Language Processing Tasks},\n  author = {Xiao, Yijun and Wang, William Yang},\n  journal = {Proceedings of the AAAI Conference on Artificial Intelligence},\n  year = {2019},\n  doi = {10.1609/aaai.v33i01.33017322},\n  url = {http://dx.doi.org/10.1609/aaai.v33i01.33017322}\n}\n\n@inproceedings{zhang2023ener,\n  title = {E-NER: Evidential Deep Learning for Trustworthy Named Entity Recognition},\n  author = {Zhang, Zhen and Hu, Mengting and Zhao, Shiwan and Huang, Minlie and Wang, Haotian and Liu, Lemao and Zhang, Zhirui and Liu, Zhe and Wu, Bingzhe},\n  booktitle = {Findings of the Association for Computational Linguistics: ACL 2023},\n  year = {2023},\n  doi = {10.18653/v1/2023.findings-acl.103},\n  url = {http://dx.doi.org/10.18653/v1/2023.findings-acl.103}\n}\n\n@inproceedings{zheng2024llamafactory,\n  title = {{L}lama{F}actory: Unified Efficient Fine-Tuning of 100+ Language Models},\n  author = {Zheng, Yaowei and Zhang, Richong and Zhang, Junhao and Ye, Yanhan and Luo, Zheyan},\n  booktitle = {Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (Volume 3: System Demonstrations)},\n  year = {2024},\n  pages = {400--410},\n  doi = {10.18653/v1/2024.acl-demos.38}\n}\n\n@inproceedings{zhou2024uniner,\n  title = {{UniversalNER}: Targeted Distillation from Large Language Models for Open Named Entity Recognition},\n  author = {Zhou, Wenxuan and Zhang, Sheng and Gu, Yu and Chen, Muhao and Poon, Hoifung},\n  booktitle = {Proceedings of the International Conference on Learning Representations (ICLR)},\n  year = {2024},\n  url = {https://arxiv.org/abs/2308.03279}\n}\n\n@inproceedings{xiong2024llm,\n  title = {Can {LLMs} Express Their Uncertainty? An Empirical Evaluation of Confidence Elicitation in {LLMs}},\n  author = {Xiong, Miao and Hu, Zhiyuan and Lu, Xinyang and Li, Yifei and Fu, Jie and He, Junxian and Hooi, Bryan},\n  booktitle = {Proceedings of the International Conference on Learning Representations (ICLR)},\n  year = {2024},\n  url = {https://arxiv.org/abs/2306.13063}\n}\n\n@inproceedings{muller2021understanding,\n  title = {Understanding the Properties of Minimum {Bayes} Risk Decoding in Neural Machine Translation},\n  author = {M{\\\"u}ller, Mathias and Sennrich, Rico},\n  booktitle = {Proceedings of the 59th Annual Meeting of the Association for Computational Linguistics (ACL)},\n  year = {2021},\n  url = {https://arxiv.org/abs/2105.08504}\n}\n\n@inproceedings{heo2025uncertainty,\n  title = {Do {LLMs} Estimate Uncertainty Well in Instruction Following?},\n  author = {Heo, Juyeon and Xiong, Miao and Heinze-Deml, Christina and Narain, Jaya},\n  booktitle = {Proceedings of the International Conference on Learning Representations (ICLR)},\n  year = {2025},\n  url = {https://arxiv.org/abs/2410.14582}\n}\n\n@inproceedings{eikema2025structured,\n  title = {Structure-Conditional Minimum {B}ayes Risk Decoding},\n  author = {Eikema, Bryan and Rutkiewicz, Anna and Giulianelli, Mario},\n  booktitle = {Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing},\n  year = {2025},\n  url = {https://arxiv.org/abs/2510.20700}\n}\n\n@article{zhang2025tts,\n  title = {A Survey on Test-Time Scaling in Large Language Models: What, How, Where, and How Well?},\n  author = {Zhang, Qiyuan and Lyu, Fuyuan and Sun, Zexu and Wang, Lei and Zhang, Weixu and Guo, Zhihan and Wang, Yufei},\n  journal = {arXiv preprint arXiv:2503.24235},\n  year = {2025},\n  url = {https://arxiv.org/abs/2503.24235}\n}\n\n@article{venktesh2025trust,\n  title = {Trust but Verify! A Survey on Verification Design for Test-time Scaling},\n  author = {Venktesh, V and Rathee, Mandeep and Anand, Avishek},\n  journal = {arXiv preprint arXiv:2508.16665},\n  year = {2025},\n  url = {https://arxiv.org/abs/2508.16665}\n}\n\n@inproceedings{jinnai2024mbr,\n  title = {Model-Based Minimum {B}ayes Risk Decoding for Text Generation},\n  author = {Jinnai, Yuu and Morimura, Tetsuro and Honda, Ukyo and Ariu, Kaito and Abe, Kenshi},\n  booktitle = {Proceedings of the 41st International Conference on Machine Learning (ICML)},\n  year = {2024},\n  url = {https://arxiv.org/abs/2311.05263}\n}\n",
      "numLines": 520,
      "startLine": 1,
      "totalLines": 520
    }
  },
  "sourceToolAssistantUUID": "b3b04bb9-807e-43b6-bbc9-852751bfd6f4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "f49c1ccb-97a0-4961-857d-2db0aa0e0624",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 30 · 2026-05-15T14:59:00.219Z_

<details open><summary>🔧 Tool call — Read · `toolu_01LQK4GrkAPHF2Fe2WKBLrCW`</summary>

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
  "parentUuid": "01f5e293-c62f-45f1-a2ff-ce3ff377ced6",
  "isSidechain": false,
  "requestId": "req_011Cb4YzcoF1Lm3bkaDjnvnu",
  "type": "assistant",
  "uuid": "63661983-aba6-44fb-ae63-3efbae275e32",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "f49c1ccb-97a0-4961-857d-2db0aa0e0624",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ACxtx1Mci3DLrexRzQuKmB",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1656,
      "cache_read_input_tokens": 29230,
      "output_tokens": 865,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1656,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 865,
          "cache_read_input_tokens": 29230,
          "cache_creation_input_tokens": 1656,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1656
          },
          "type": "message"
        }
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

_source line 31 · 2026-05-15T14:59:00.224Z_

<details><summary>↩ Tool result · `toolu_01LQK4GrkAPHF2Fe2WKBLrCW`</summary>

```text
1	\section{Introduction}\label{sec:introduction}
2	
3	Self-consistency---sampling multiple outputs and aggregating them---has become a powerful strategy for improving language model reasoning.
4	On discrete-answer tasks such as arithmetic and commonsense QA, majority voting over chain-of-thought samples yields large gains: +18 percentage points on GSM8K (PaLM-540B; \citealp{wang2023selfconsistency}).
5	More broadly, test-time compute scaling through repeated sampling and selection has emerged as a complementary axis to model scaling, offering substantial quality improvements at inference time \cite{snell2025scaling, brown2024monkeys}.
6	These results rest on a shared assumption: that among $N$ stochastic samples, a selection mechanism can identify better outputs.
7	For tasks with a single correct answer, this assumption holds naturally---the majority vote is the selector.
8	But information extraction (IE) poses a structurally different challenge.
9	The output is not a single token or number; it is a \textit{set} of entities or relations with internal dependencies, where two samples may extract overlapping but non-identical structures.
10	There is no obvious majority to vote on, partial agreement is the norm rather than the exception, and the space of valid outputs is combinatorially large.
11	Can self-consistency still provide useful signal in this structured setting?
12	
13	Prior work on confidence estimation for LLM-based IE has conflated two distinct objectives: \textit{quality estimation} (which inputs does the model handle reliably?) and \textit{sample selection} (which of $N$ outputs is best?).
14	These require different signal properties: the former benefits from instance-level aggregation, while the latter demands per-sample discrimination.
15	Self-consistency methods for discrete answers \cite{wang2023selfconsistency, chen2024usc} and weighted variants \cite{taubenfeld2025cisc, kang2025selfcertainty} assume outputs can be grouped by equivalence---an assumption that breaks for entity sets with partial overlap.
16	The most relevant study, \citet{nedellec2026consistency}, examines consistency--accuracy correlations for LLM-based IE, finding results that our quality-estimation analysis corroborates.
17	Our work complements theirs in three directions: (i)~structural matching beyond surface-level agreement, (ii)~testing whether quality estimation translates to best-of-$N$ selection (it does not), and (iii)~a difficulty gradient revealing non-obvious findings---WNUT-17 conditional correlations collapse to $\rho{=}0.038$ (n.s.) and LP exhibits strong \textit{negative} correlation ($\rho{=}{-}0.410$)---that would be invisible on a single dataset.
18	
19	Structured IE requires schema-compliant output, making constrained decoding \cite{willard2023guided} the standard inference strategy---without it, a substantial fraction of outputs from general-purpose models are unparseable.\footnote{Fine-tuned models may retain format compliance without grammar constraints: our free-form ablation achieves 99.95\% valid JSON rate (\S\ref{sec:ablation}).}
20	All experiments use constrained decoding, the regime under which structured IE is practically deployed.
21	
22	Our central finding is the \textbf{correlation-selection gap} (Figure~\ref{fig:overview}): consistency-based signals achieve strong quality estimation ($\rho$ up to 0.38, AUROC up to 0.75) but fail at sample selection despite 12--18~pp of oracle headroom.
23	Four of five signals are instance-level by construction---this is definitional, not empirical.
24	The non-trivial questions are whether (a)~consensus-proximity selection, instantiating MBR decoding \cite{eikema2022sampling, freitag2022high, muller2021understanding}, can recover per-sample discrimination, and (b)~whether log-probability, the only per-sample signal, can exploit the headroom.
25	Both fail: MBR utility correlates with F1 across instances but not within them (\S\ref{sec:discussion}); log-probability scores are severely compressed (60\% of instances effectively tied), though where compression is mitigated, LP becomes a significant selector ($+2.9$~pp, $p{=}0.01$).
26	A controlled free-form decoding ablation confirms that NER LP compression persists without constrained decoding; on RE, LP selection reverses direction (preliminary), revealing task-dependent interaction with decoding regime (\S\ref{sec:ablation}).
27	
28	\begin{figure*}[t]
29	\centering
30	\includegraphics[width=\textwidth]{fig_overview}
31	\caption{The correlation-selection gap. \textbf{Left}: high inter-sample agreement correlates with high F1 (quality estimation). \textbf{Right}: instance-level signals assign identical scores to all candidates, precluding sample selection.}
32	\label{fig:overview}
33	\end{figure*}
34	
35	We systematically compare five confidence signals from three families---structural (entity voting confidence [VC], Soft Jaccard [SJ]), surface (exact match [EM], Fleiss' $\kappa$ [FK]), and model-internal (log-probability [LP])---across NER and RE on SciERC \cite{luan2018scierc}, CoNLL-2003 \cite{tjongkimsang2003conll}, and WNUT-17 \cite{derczynski2017wnut}, using Qwen3-8B and LLaMA-3.1-8B.
36	Our contributions are:
37	\begin{enumerate}
38	    \item \textbf{Multi-metric evaluation revealing metric dissociation.}
39	    We compare five confidence signals from three families---structural, surface, and model-internal---across three distinct metrics: quality estimation ($\rho$), binary discrimination (AUROC), and sample selection (best-of-$N$ F1).
40	    These metrics decouple: EM leads AUROC (0.749) but ranks third in $\rho$ (0.295), so single-metric evaluation risks selecting the wrong signal for a given use case.
41	
42	    \item \textbf{LP score compression and MBR utility-quality misalignment.}
43	    All signals achieve strong quality estimation ($\rho$ up to 0.38, AUROC up to 0.75) yet none significantly improves selection despite 12--18~pp of oracle headroom.
44	    The failure of four instance-level signals is definitional---they assign a single score per input and cannot rank candidates by construction.
45	    The empirical contribution is diagnosing why the two per-sample mechanisms that \textit{could} bridge the gap both fail: log-probability scores are compressed into effective ties (60\% of instances within $\varepsilon{=}0.05$), and consensus-proximity selection (MBR decoding) correlates with quality across instances but not within them.
46	    Where compression is mitigated, LP becomes a significant selector ($+2.9$~pp, $p{=}0.01$), confirming score compression as the primary bottleneck.
47	    A controlled ablation confirms LP compression persists without constrained decoding on NER; on RE, LP selection reverses direction (preliminary), indicating task-dependent interaction with decoding regime.
48	
49	    \item \textbf{Task-complexity boundary conditions.}
50	    Signal rankings shift with task difficulty: EM leads on easy tasks, SJ on hard tasks---consistent across two model families at 8B scale, though with model-dependent magnitude.
51	    At the capability boundary (WNUT-17, 52\% zero F1), conditional correlations collapse to non-significance and LP exhibits strong negative correlation ($\rho{=}{-}0.410$)---phenomena invisible on a single dataset that extend \citet{nedellec2026consistency}'s quality-estimation analysis.
52	    NER findings span three datasets; RE conclusions rest on SciERC alone (preliminary).
53	\end{enumerate}
54	
55	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "63661983-aba6-44fb-ae63-3efbae275e32",
  "isSidechain": false,
  "promptId": "a8cee1eb-a5df-415d-8e30-c85446d1e0a7",
  "type": "user",
  "uuid": "76b11e0c-b8aa-439f-b01d-346fcb1932f6",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/introduction.tex",
      "content": "\\section{Introduction}\\label{sec:introduction}\n\nSelf-consistency---sampling multiple outputs and aggregating them---has become a powerful strategy for improving language model reasoning.\nOn discrete-answer tasks such as arithmetic and commonsense QA, majority voting over chain-of-thought samples yields large gains: +18 percentage points on GSM8K (PaLM-540B; \\citealp{wang2023selfconsistency}).\nMore broadly, test-time compute scaling through repeated sampling and selection has emerged as a complementary axis to model scaling, offering substantial quality improvements at inference time \\cite{snell2025scaling, brown2024monkeys}.\nThese results rest on a shared assumption: that among $N$ stochastic samples, a selection mechanism can identify better outputs.\nFor tasks with a single correct answer, this assumption holds naturally---the majority vote is the selector.\nBut information extraction (IE) poses a structurally different challenge.\nThe output is not a single token or number; it is a \\textit{set} of entities or relations with internal dependencies, where two samples may extract overlapping but non-identical structures.\nThere is no obvious majority to vote on, partial agreement is the norm rather than the exception, and the space of valid outputs is combinatorially large.\nCan self-consistency still provide useful signal in this structured setting?\n\nPrior work on confidence estimation for LLM-based IE has conflated two distinct objectives: \\textit{quality estimation} (which inputs does the model handle reliably?) and \\textit{sample selection} (which of $N$ outputs is best?).\nThese require different signal properties: the former benefits from instance-level aggregation, while the latter demands per-sample discrimination.\nSelf-consistency methods for discrete answers \\cite{wang2023selfconsistency, chen2024usc} and weighted variants \\cite{taubenfeld2025cisc, kang2025selfcertainty} assume outputs can be grouped by equivalence---an assumption that breaks for entity sets with partial overlap.\nThe most relevant study, \\citet{nedellec2026consistency}, examines consistency--accuracy correlations for LLM-based IE, finding results that our quality-estimation analysis corroborates.\nOur work complements theirs in three directions: (i)~structural matching beyond surface-level agreement, (ii)~testing whether quality estimation translates to best-of-$N$ selection (it does not), and (iii)~a difficulty gradient revealing non-obvious findings---WNUT-17 conditional correlations collapse to $\\rho{=}0.038$ (n.s.) and LP exhibits strong \\textit{negative} correlation ($\\rho{=}{-}0.410$)---that would be invisible on a single dataset.\n\nStructured IE requires schema-compliant output, making constrained decoding \\cite{willard2023guided} the standard inference strategy---without it, a substantial fraction of outputs from general-purpose models are unparseable.\\footnote{Fine-tuned models may retain format compliance without grammar constraints: our free-form ablation achieves 99.95\\% valid JSON rate (\\S\\ref{sec:ablation}).}\nAll experiments use constrained decoding, the regime under which structured IE is practically deployed.\n\nOur central finding is the \\textbf{correlation-selection gap} (Figure~\\ref{fig:overview}): consistency-based signals achieve strong quality estimation ($\\rho$ up to 0.38, AUROC up to 0.75) but fail at sample selection despite 12--18~pp of oracle headroom.\nFour of five signals are instance-level by construction---this is definitional, not empirical.\nThe non-trivial questions are whether (a)~consensus-proximity selection, instantiating MBR decoding \\cite{eikema2022sampling, freitag2022high, muller2021understanding}, can recover per-sample discrimination, and (b)~whether log-probability, the only per-sample signal, can exploit the headroom.\nBoth fail: MBR utility correlates with F1 across instances but not within them (\\S\\ref{sec:discussion}); log-probability scores are severely compressed (60\\% of instances effectively tied), though where compression is mitigated, LP becomes a significant selector ($+2.9$~pp, $p{=}0.01$).\nA controlled free-form decoding ablation confirms that NER LP compression persists without constrained decoding; on RE, LP selection reverses direction (preliminary), revealing task-dependent interaction with decoding regime (\\S\\ref{sec:ablation}).\n\n\\begin{figure*}[t]\n\\centering\n\\includegraphics[width=\\textwidth]{fig_overview}\n\\caption{The correlation-selection gap. \\textbf{Left}: high inter-sample agreement correlates with high F1 (quality estimation). \\textbf{Right}: instance-level signals assign identical scores to all candidates, precluding sample selection.}\n\\label{fig:overview}\n\\end{figure*}\n\nWe systematically compare five confidence signals from three families---structural (entity voting confidence [VC], Soft Jaccard [SJ]), surface (exact match [EM], Fleiss' $\\kappa$ [FK]), and model-internal (log-probability [LP])---across NER and RE on SciERC \\cite{luan2018scierc}, CoNLL-2003 \\cite{tjongkimsang2003conll}, and WNUT-17 \\cite{derczynski2017wnut}, using Qwen3-8B and LLaMA-3.1-8B.\nOur contributions are:\n\\begin{enumerate}\n    \\item \\textbf{Multi-metric evaluation revealing metric dissociation.}\n    We compare five confidence signals from three families---structural, surface, and model-internal---across three distinct metrics: quality estimation ($\\rho$), binary discrimination (AUROC), and sample selection (best-of-$N$ F1).\n    These metrics decouple: EM leads AUROC (0.749) but ranks third in $\\rho$ (0.295), so single-metric evaluation risks selecting the wrong signal for a given use case.\n\n    \\item \\textbf{LP score compression and MBR utility-quality misalignment.}\n    All signals achieve strong quality estimation ($\\rho$ up to 0.38, AUROC up to 0.75) yet none significantly improves selection despite 12--18~pp of oracle headroom.\n    The failure of four instance-level signals is definitional---they assign a single score per input and cannot rank candidates by construction.\n    The empirical contribution is diagnosing why the two per-sample mechanisms that \\textit{could} bridge the gap both fail: log-probability scores are compressed into effective ties (60\\% of instances within $\\varepsilon{=}0.05$), and consensus-proximity selection (MBR decoding) correlates with quality across instances but not within them.\n    Where compression is mitigated, LP becomes a significant selector ($+2.9$~pp, $p{=}0.01$), confirming score compression as the primary bottleneck.\n    A controlled ablation confirms LP compression persists without constrained decoding on NER; on RE, LP selection reverses direction (preliminary), indicating task-dependent interaction with decoding regime.\n\n    \\item \\textbf{Task-complexity boundary conditions.}\n    Signal rankings shift with task difficulty: EM leads on easy tasks, SJ on hard tasks---consistent across two model families at 8B scale, though with model-dependent magnitude.\n    At the capability boundary (WNUT-17, 52\\% zero F1), conditional correlations collapse to non-significance and LP exhibits strong negative correlation ($\\rho{=}{-}0.410$)---phenomena invisible on a single dataset that extend \\citet{nedellec2026consistency}'s quality-estimation analysis.\n    NER findings span three datasets; RE conclusions rest on SciERC alone (preliminary).\n\\end{enumerate}\n\n",
      "numLines": 55,
      "startLine": 1,
      "totalLines": 55
    }
  },
  "sourceToolAssistantUUID": "63661983-aba6-44fb-ae63-3efbae275e32",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "f49c1ccb-97a0-4961-857d-2db0aa0e0624",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 32 · 2026-05-15T14:59:00.676Z_

<details open><summary>🔧 Tool call — Read · `toolu_01FjqbApvmVU3dYJagPSczB2`</summary>

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
  "parentUuid": "76b11e0c-b8aa-439f-b01d-346fcb1932f6",
  "isSidechain": false,
  "requestId": "req_011Cb4YzcoF1Lm3bkaDjnvnu",
  "type": "assistant",
  "uuid": "ad2ccdec-583b-4d66-a35d-ecfd3c4f5372",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "f49c1ccb-97a0-4961-857d-2db0aa0e0624",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ACxtx1Mci3DLrexRzQuKmB",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1656,
      "cache_read_input_tokens": 29230,
      "output_tokens": 865,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1656,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 865,
          "cache_read_input_tokens": 29230,
          "cache_creation_input_tokens": 1656,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1656
          },
          "type": "message"
        }
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

_source line 33 · 2026-05-15T14:59:00.682Z_

<details><summary>↩ Tool result · `toolu_01FjqbApvmVU3dYJagPSczB2`</summary>

```text
1	\section{Related Work}\label{sec:related}
2	
3	\paragraph{Self-consistency and test-time scaling.}
4	Self-consistency decoding \cite{wang2023selfconsistency} improves reasoning by majority voting over chain-of-thought samples, assuming a discrete answer space.
5	Extensions to free-form text use LLM-based comparison \cite{chen2024usc}, atomic sub-claim decomposition \cite{thirukovalluru2024atomic}, or cross-sample hallucination detection \cite{manakul2023selfcheckgpt}.
6	For test-time scaling \cite{zhang2025tts}, \citet{snell2025scaling} characterize compute scaling laws and \citet{brown2024monkeys} show best-of-$N$ gains across tasks.
7	Recent reward-free selectors include confidence-weighted voting \cite{taubenfeld2025cisc}, KL-based self-certainty \cite{kang2025selfcertainty}, adaptive sampling \cite{kim2026reasc}, ranked aggregation \cite{wang2025rankedvoting}, and latent-space consistency \cite{oh2025latentsc}.
8	Concurrently, \citet{feng2025optimal} and \citet{wang2025make} adapt self-consistency to difficulty-aware settings, echoing our finding that signal rankings shift with task complexity; \citet{li2025llms} propose generative self-aggregation for IE but focus on output fusion rather than confidence-based selection.
9	All of the above target reasoning/QA with discrete answers or specific aggregation strategies.
10	Our work extends self-consistency to set-valued structured outputs and identifies the correlation-selection gap: strong quality estimation ($\rho{=}0.38$) coexists with selection failure ($p{>}0.39$).
11	
12	\paragraph{Consistency for structured IE.}
13	\citet{nedellec2026consistency} study consistency--accuracy correlations for LLM-based NER/RE, corroborating our quality-estimation findings.
14	Their work leaves open three questions we address: (i)~whether structural matching improves on surface-level agreement (which they acknowledge ``overlooks semantically consistent outputs''); (ii)~whether quality estimation translates to best-of-$N$ selection; and (iii)~whether findings generalize across a difficulty gradient.
15	Our Soft Jaccard signal addresses (i) through type-aware bipartite matching with token-level span overlap; our selection analysis (\S\ref{sec:selection_gap}) directly addresses (ii); and our three-dataset evaluation spanning easy (CoNLL) to hard (SciERC) tasks addresses (iii).
16	CoCoA \cite{vashurin2025cocoa} fuses model confidence with inter-sample consistency for QA/summarization but does not address structured extraction.
17	Our evaluation builds on generative IE work \cite{zhou2024uniner, sainz2024gollie, josifoski2022genie, li2023codeie, wadhwa2023revisiting, wang2023instructuie} and constrained decoding \cite{willard2023guided}.
18	
19	\paragraph{Uncertainty estimation and calibration.}
20	Surveys cover confidence estimation \cite{geng2024confidence}, selective abstention \cite{wen2025know}, uncertainty quantification \cite{xia2025survey}, and calibration \cite{hobelsberger2025systematic} for LLMs; \citet{xiong2024llm} find LLMs tend toward overconfidence, and \citet{heo2025uncertainty} show calibration degrades with task complexity.
21	Semantic uncertainty \cite{kuhn2023semantic} clusters generations by meaning; \citet{kossen2024semantic} distill this into probes; P(True) \cite{kadavath2022language} queries model confidence directly; \citet{malinin2021uncertainty} distinguish data and model uncertainty in autoregressive models.
22	Our structural signals instead measure agreement over output \textit{structure}.
23	Neural networks are often miscalibrated \cite{guo2017calibration, desai2020calibration}; deep ensembles \cite{lakshminarayanan2017ensembles} and MC-dropout \cite{gal2016dropout} obtain uncertainty from model variation, while our approach requires no model modification.
24	Prior NER uncertainty work spans Bayesian inference for sequence labeling \cite{xiao2019uncertainty}, active learning under uncertainty \cite{shelmanov2021active}, evidential deep learning \cite{zhang2023ener}, verification-augmented NER \cite{kim2024verifiner}, and uncertainty transmission across label sequences \cite{he2024uncertainty}---all within discriminative paradigms.
25	Conformal prediction \cite{fisch2021conformal, angelopoulos2021conformal} provides coverage guarantees; trained verifiers \cite{cobbe2021verifiers, lightman2024verify, venktesh2025trust} and reward models \cite{wang2024mathshepherd} learn per-sample scoring.
26	Our selection strategies instantiate MBR decoding \cite{eikema2022sampling} with structural utility functions; despite MBR's success in translation \cite{freitag2022high} and other generation tasks \cite{jinnai2024mbr}, we find utility-quality misalignment at the per-sample level for structured IE (\S\ref{sec:discussion}).
27	\citet{eikema2025structured} study structure-conditional MBR decoding and find that standard utility functions degrade on structured outputs, consistent with our finding.
28	Selective prediction \cite{geifman2017selective} and confidence-based IE filtering \cite{culotta2004confidence} establish the broader framework.
29	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ad2ccdec-583b-4d66-a35d-ecfd3c4f5372",
  "isSidechain": false,
  "promptId": "a8cee1eb-a5df-415d-8e30-c85446d1e0a7",
  "type": "user",
  "uuid": "76e70654-10db-4246-b2ab-915318feae5c",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/related_work.tex",
      "content": "\\section{Related Work}\\label{sec:related}\n\n\\paragraph{Self-consistency and test-time scaling.}\nSelf-consistency decoding \\cite{wang2023selfconsistency} improves reasoning by majority voting over chain-of-thought samples, assuming a discrete answer space.\nExtensions to free-form text use LLM-based comparison \\cite{chen2024usc}, atomic sub-claim decomposition \\cite{thirukovalluru2024atomic}, or cross-sample hallucination detection \\cite{manakul2023selfcheckgpt}.\nFor test-time scaling \\cite{zhang2025tts}, \\citet{snell2025scaling} characterize compute scaling laws and \\citet{brown2024monkeys} show best-of-$N$ gains across tasks.\nRecent reward-free selectors include confidence-weighted voting \\cite{taubenfeld2025cisc}, KL-based self-certainty \\cite{kang2025selfcertainty}, adaptive sampling \\cite{kim2026reasc}, ranked aggregation \\cite{wang2025rankedvoting}, and latent-space consistency \\cite{oh2025latentsc}.\nConcurrently, \\citet{feng2025optimal} and \\citet{wang2025make} adapt self-consistency to difficulty-aware settings, echoing our finding that signal rankings shift with task complexity; \\citet{li2025llms} propose generative self-aggregation for IE but focus on output fusion rather than confidence-based selection.\nAll of the above target reasoning/QA with discrete answers or specific aggregation strategies.\nOur work extends self-consistency to set-valued structured outputs and identifies the correlation-selection gap: strong quality estimation ($\\rho{=}0.38$) coexists with selection failure ($p{>}0.39$).\n\n\\paragraph{Consistency for structured IE.}\n\\citet{nedellec2026consistency} study consistency--accuracy correlations for LLM-based NER/RE, corroborating our quality-estimation findings.\nTheir work leaves open three questions we address: (i)~whether structural matching improves on surface-level agreement (which they acknowledge ``overlooks semantically consistent outputs''); (ii)~whether quality estimation translates to best-of-$N$ selection; and (iii)~whether findings generalize across a difficulty gradient.\nOur Soft Jaccard signal addresses (i) through type-aware bipartite matching with token-level span overlap; our selection analysis (\\S\\ref{sec:selection_gap}) directly addresses (ii); and our three-dataset evaluation spanning easy (CoNLL) to hard (SciERC) tasks addresses (iii).\nCoCoA \\cite{vashurin2025cocoa} fuses model confidence with inter-sample consistency for QA/summarization but does not address structured extraction.\nOur evaluation builds on generative IE work \\cite{zhou2024uniner, sainz2024gollie, josifoski2022genie, li2023codeie, wadhwa2023revisiting, wang2023instructuie} and constrained decoding \\cite{willard2023guided}.\n\n\\paragraph{Uncertainty estimation and calibration.}\nSurveys cover confidence estimation \\cite{geng2024confidence}, selective abstention \\cite{wen2025know}, uncertainty quantification \\cite{xia2025survey}, and calibration \\cite{hobelsberger2025systematic} for LLMs; \\citet{xiong2024llm} find LLMs tend toward overconfidence, and \\citet{heo2025uncertainty} show calibration degrades with task complexity.\nSemantic uncertainty \\cite{kuhn2023semantic} clusters generations by meaning; \\citet{kossen2024semantic} distill this into probes; P(True) \\cite{kadavath2022language} queries model confidence directly; \\citet{malinin2021uncertainty} distinguish data and model uncertainty in autoregressive models.\nOur structural signals instead measure agreement over output \\textit{structure}.\nNeural networks are often miscalibrated \\cite{guo2017calibration, desai2020calibration}; deep ensembles \\cite{lakshminarayanan2017ensembles} and MC-dropout \\cite{gal2016dropout} obtain uncertainty from model variation, while our approach requires no model modification.\nPrior NER uncertainty work spans Bayesian inference for sequence labeling \\cite{xiao2019uncertainty}, active learning under uncertainty \\cite{shelmanov2021active}, evidential deep learning \\cite{zhang2023ener}, verification-augmented NER \\cite{kim2024verifiner}, and uncertainty transmission across label sequences \\cite{he2024uncertainty}---all within discriminative paradigms.\nConformal prediction \\cite{fisch2021conformal, angelopoulos2021conformal} provides coverage guarantees; trained verifiers \\cite{cobbe2021verifiers, lightman2024verify, venktesh2025trust} and reward models \\cite{wang2024mathshepherd} learn per-sample scoring.\nOur selection strategies instantiate MBR decoding \\cite{eikema2022sampling} with structural utility functions; despite MBR's success in translation \\cite{freitag2022high} and other generation tasks \\cite{jinnai2024mbr}, we find utility-quality misalignment at the per-sample level for structured IE (\\S\\ref{sec:discussion}).\n\\citet{eikema2025structured} study structure-conditional MBR decoding and find that standard utility functions degrade on structured outputs, consistent with our finding.\nSelective prediction \\cite{geifman2017selective} and confidence-based IE filtering \\cite{culotta2004confidence} establish the broader framework.\n",
      "numLines": 29,
      "startLine": 1,
      "totalLines": 29
    }
  },
  "sourceToolAssistantUUID": "ad2ccdec-583b-4d66-a35d-ecfd3c4f5372",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "f49c1ccb-97a0-4961-857d-2db0aa0e0624",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 34 · 2026-05-15T14:59:01.155Z_

<details open><summary>🔧 Tool call — Read · `toolu_01YZLMxQhh79DymbpNwjQrX7`</summary>

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
  "parentUuid": "76e70654-10db-4246-b2ab-915318feae5c",
  "isSidechain": false,
  "requestId": "req_011Cb4YzcoF1Lm3bkaDjnvnu",
  "type": "assistant",
  "uuid": "79992da1-447b-414b-8ecd-5b81f809f6c0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "f49c1ccb-97a0-4961-857d-2db0aa0e0624",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ACxtx1Mci3DLrexRzQuKmB",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1656,
      "cache_read_input_tokens": 29230,
      "output_tokens": 865,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1656,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 865,
          "cache_read_input_tokens": 29230,
          "cache_creation_input_tokens": 1656,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1656
          },
          "type": "message"
        }
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

_source line 35 · 2026-05-15T14:59:01.164Z_

<details><summary>↩ Tool result · `toolu_01YZLMxQhh79DymbpNwjQrX7`</summary>

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
16	We use \textit{confidence signal} as the umbrella term for all five measures.
17	Four are \textit{consistency signals}---computed from inter-sample agreement---spanning two families: \textit{structural} (Soft Jaccard [SJ], entity voting confidence [VC]) and \textit{surface} (exact match [EM], Fleiss' $\kappa$ [FK]).
18	The fifth, log-probability, is the sole \textit{model-internal} signal and the only one that scores individual samples rather than the instance as a whole.
19	
20	\paragraph{Log-probability (model-internal, per-sample).}
21	The only per-sample signal.
22	For sample $y_i$ with tokens $t_1, \ldots, t_{|y_i|}$:
23	\begin{equation}\label{eq:logprob}
24	c_{\text{lp}}(y_i) = \frac{1}{|y_i|} \sum_{j=1}^{|y_i|} \log p_{\mathcal{M}}(t_j \mid t_{&lt;j}, x)
25	\end{equation}
26	
27	\paragraph{Exact match voting (surface, instance-level).}
28	The majority fraction---the proportion of samples producing the most common output:
29	\begin{equation}\label{eq:em}
30	c_{\text{em}}(x) = \frac{1}{N} \max_{y} \big|\{i : y_i = y\}\big|
31	\end{equation}
32	
33	\paragraph{Fleiss' $\kappa$ (surface, instance-level).}
34	We adapt \citet{fleiss1971agreement} to entity sets: items are unique (text, type) tuples across all $N$ samples; each sample assigns binary present/absent labels, yielding a $|E_\cup| \times 2$ rating matrix:
35	\begin{equation}\label{eq:fk}
36	\kappa = \frac{\bar{P} - \bar{P}_e}{1 - \bar{P}_e}
37	\end{equation}
38	where $\bar{P}$ is mean observed pairwise agreement and $\bar{P}_e$ is expected agreement under random assignment.
39	While FK assumes independent raters, temperature-based sampling yields mild negative dependence rather than positive correlation among samples.
40	Empirically, we measure excess agreement ($\bar{P} - \bar{P}_e$) across all configurations (SciERC NER/RE, CoNLL, WNUT-17; $N{=}8$, $T{=}1.0$) and find values between $-$0.4\% and $-$4.0\%, indicating mild \textit{negative} dependence---samples from the same model tend to err on different items---which confirms that FK is not inflated by inter-sample dependence.
41	(All excess agreement values are negative across 5 configurations; a one-sample $t$-test against zero yields $p{<}0.05$, though with $n{=}5$ the test has limited power and should be interpreted cautiously.)
42	Unlike structural signals, FK relies on exact string matching and does not tolerate surface variations.
43	
44	\paragraph{Soft Jaccard (structural, instance-level).}
45	Our primary structural signal extends Jaccard similarity \cite{jaccard1901distribution} to extracted entity/relation sets.
46	For samples $y_i, y_j$, we group extractions by type, compute max-weight bipartite matching via the Hungarian algorithm (maximizing total token-level IoU; zero-IoU pairs automatically receive zero weight), and define:
47	\begin{equation}\label{eq:sj}
48	\text{SJ}(y_i, y_j) = \frac{\sum_{m \in M} \text{sim}(a_m, b_m)}{\sum_{g} \max(|g_i|, |g_j|)}
49	\end{equation}
50	where $M$ is the matched set from the Hungarian algorithm (without minimum similarity threshold), $\text{sim}(a_m, b_m)$ is the token-level IoU (intersection of tokens divided by union of tokens) between matched entity spans $a_m$ and $b_m$, and $g_i, g_j$ index per-type extraction counts.
51	We use $\max(|g_i|, |g_j|)$ rather than $|g_i \cup g_j|$ as the normalizer to penalize length asymmetry between samples.
52	The instance-level signal averages over all pairs:
53	\begin{equation}\label{eq:sj_instance}
54	c_{\text{sj}}(x) = \frac{1}{\binom{N}{2}} \sum_{i&lt;j} \text{SJ}(y_i, y_j)
55	\end{equation}
56	
57	\paragraph{Entity voting confidence (structural, instance-level).}
58	For each entity $e$ in the union $E_\cup$ of all samples, we compute frequency $\text{freq}(e) = |\{i : e \in y_i\}| / N$.
59	The instance-level confidence is the mean frequency:
60	\begin{equation}\label{eq:voting}
61	c_{\text{vote}}(x) = \frac{1}{|E_\cup|} \sum_{e \in E_\cup} \text{freq}(e)
62	\end{equation}
63	When $E_\cup = \emptyset$ (no entity extracted by any sample), we set $c_{\mathrm{vc}}(x) = 0$.\footnote{This occurs in $<$1\% of instances in our experiments (WNUT-17 only). Equation~\ref{eq:voting} defines the continuous QE signal used throughout Table~\ref{tab:quality_estimation} and all correlation analyses. For voted-output \textit{selection} (Table~\ref{tab:selection}), we include only entities with frequency ${>}N/2$, following standard majority voting. The two computations serve different purposes: Eq.~\ref{eq:voting} assigns a continuous quality score per instance; the majority threshold constructs a discrete output for F1 evaluation. On NER, the threshold variant yields $\rho{=}0.252$ (vs.\ $0.379$ for Eq.~\ref{eq:voting}), reflecting information loss from binarization; on RE, the difference is negligible ($\Delta\rho{=}0.019$).}
64	
65	\subsection{Evaluation Framework}\label{sec:evaluation}
66	
67	\paragraph{Quality estimation.}
68	We measure rank correlation (Spearman $\rho$) between the confidence signal and instance-level F1, and binary discrimination (AUROC) by classifying instances as above or below median F1.
69	Correlation analyses exclude instances with empty gold annotations ($n{=}529$ on SciERC after filtering 22/551), where F1 is trivially zero and consistency signals reflect agreement on the empty set rather than extraction quality; selection analyses retain the full set ($n{=}551$) because empty-gold instances contribute $\Delta{=}0$ to all signals, introducing no bias in the greedy-vs-signal comparison.
70	
71	\paragraph{Sample selection.}
72	We report best-of-$N$ F1: for each instance, the signal selects one sample.
73	Per-sample signals (LP) directly rank candidates; instance-level signals select the sample closest to the consensus output (the consensus-proximity score for SJ is mathematically equivalent to leave-one-out SJ selection).
74	We compare against an \textit{oracle} (highest-F1 sample) and a \textit{greedy} baseline (a fixed sample from the $T{=}1.0$ candidate pool, providing a no-selection reference within the sampled distribution).
75	
76	\paragraph{Complementarity.}
77	High rank correlation does not guarantee effective sample selection: if per-sample variance is low, even a perfect quality estimator cannot distinguish among near-identical candidates (\S\ref{sec:selection_gap}).
78	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "79992da1-447b-414b-8ecd-5b81f809f6c0",
  "isSidechain": false,
  "promptId": "a8cee1eb-a5df-415d-8e30-c85446d1e0a7",
  "type": "user",
  "uuid": "9c112911-f278-470d-95de-2cc10cdc6ba0",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/method.tex",
      "content": "\\section{Method}\\label{sec:method}\n\n\\subsection{Problem Formulation}\\label{sec:formulation}\n\nGiven a language model $\\mathcal{M}$ and input $x$, we sample $N$ structured outputs $\\{y_1, \\ldots, y_N\\}$ at temperature $T > 0$ via constrained decoding \\cite{willard2023guided}.\nEach $y_i$ is an entity set (NER) or relation set (RE).\nA confidence signal $c$ serves two purposes: (a) \\textit{quality estimation}---predicting which instances the model handles reliably, and (b) \\textit{sample selection}---identifying the best output among $N$ candidates.\n\nA \\textbf{per-sample signal} scores each $y_i$ independently, $c_{\\text{ps}}: (x, y_i) \\to \\mathbb{R}$, enabling direct candidate ranking.\nAn \\textbf{instance-level signal} aggregates over all $N$ samples, $c_{\\text{il}}: (x, \\{y_i\\}_{i=1}^N) \\to \\mathbb{R}$, producing a single score per input.\nThis asymmetry---between predicting \\textit{which inputs} are easy and selecting \\textit{which output} is best---is central to the correlation-selection gap we investigate.\nNotation is summarized in Appendix~\\ref{app:notation}.\n\n\\subsection{Confidence Signals}\\label{sec:signals}\n\nWe use \\textit{confidence signal} as the umbrella term for all five measures.\nFour are \\textit{consistency signals}---computed from inter-sample agreement---spanning two families: \\textit{structural} (Soft Jaccard [SJ], entity voting confidence [VC]) and \\textit{surface} (exact match [EM], Fleiss' $\\kappa$ [FK]).\nThe fifth, log-probability, is the sole \\textit{model-internal} signal and the only one that scores individual samples rather than the instance as a whole.\n\n\\paragraph{Log-probability (model-internal, per-sample).}\nThe only per-sample signal.\nFor sample $y_i$ with tokens $t_1, \\ldots, t_{|y_i|}$:\n\\begin{equation}\\label{eq:logprob}\nc_{\\text{lp}}(y_i) = \\frac{1}{|y_i|} \\sum_{j=1}^{|y_i|} \\log p_{\\mathcal{M}}(t_j \\mid t_{&lt;j}, x)\n\\end{equation}\n\n\\paragraph{Exact match voting (surface, instance-level).}\nThe majority fraction---the proportion of samples producing the most common output:\n\\begin{equation}\\label{eq:em}\nc_{\\text{em}}(x) = \\frac{1}{N} \\max_{y} \\big|\\{i : y_i = y\\}\\big|\n\\end{equation}\n\n\\paragraph{Fleiss' $\\kappa$ (surface, instance-level).}\nWe adapt \\citet{fleiss1971agreement} to entity sets: items are unique (text, type) tuples across all $N$ samples; each sample assigns binary present/absent labels, yielding a $|E_\\cup| \\times 2$ rating matrix:\n\\begin{equation}\\label{eq:fk}\n\\kappa = \\frac{\\bar{P} - \\bar{P}_e}{1 - \\bar{P}_e}\n\\end{equation}\nwhere $\\bar{P}$ is mean observed pairwise agreement and $\\bar{P}_e$ is expected agreement under random assignment.\nWhile FK assumes independent raters, temperature-based sampling yields mild negative dependence rather than positive correlation among samples.\nEmpirically, we measure excess agreement ($\\bar{P} - \\bar{P}_e$) across all configurations (SciERC NER/RE, CoNLL, WNUT-17; $N{=}8$, $T{=}1.0$) and find values between $-$0.4\\% and $-$4.0\\%, indicating mild \\textit{negative} dependence---samples from the same model tend to err on different items---which confirms that FK is not inflated by inter-sample dependence.\n(All excess agreement values are negative across 5 configurations; a one-sample $t$-test against zero yields $p{<}0.05$, though with $n{=}5$ the test has limited power and should be interpreted cautiously.)\nUnlike structural signals, FK relies on exact string matching and does not tolerate surface variations.\n\n\\paragraph{Soft Jaccard (structural, instance-level).}\nOur primary structural signal extends Jaccard similarity \\cite{jaccard1901distribution} to extracted entity/relation sets.\nFor samples $y_i, y_j$, we group extractions by type, compute max-weight bipartite matching via the Hungarian algorithm (maximizing total token-level IoU; zero-IoU pairs automatically receive zero weight), and define:\n\\begin{equation}\\label{eq:sj}\n\\text{SJ}(y_i, y_j) = \\frac{\\sum_{m \\in M} \\text{sim}(a_m, b_m)}{\\sum_{g} \\max(|g_i|, |g_j|)}\n\\end{equation}\nwhere $M$ is the matched set from the Hungarian algorithm (without minimum similarity threshold), $\\text{sim}(a_m, b_m)$ is the token-level IoU (intersection of tokens divided by union of tokens) between matched entity spans $a_m$ and $b_m$, and $g_i, g_j$ index per-type extraction counts.\nWe use $\\max(|g_i|, |g_j|)$ rather than $|g_i \\cup g_j|$ as the normalizer to penalize length asymmetry between samples.\nThe instance-level signal averages over all pairs:\n\\begin{equation}\\label{eq:sj_instance}\nc_{\\text{sj}}(x) = \\frac{1}{\\binom{N}{2}} \\sum_{i&lt;j} \\text{SJ}(y_i, y_j)\n\\end{equation}\n\n\\paragraph{Entity voting confidence (structural, instance-level).}\nFor each entity $e$ in the union $E_\\cup$ of all samples, we compute frequency $\\text{freq}(e) = |\\{i : e \\in y_i\\}| / N$.\nThe instance-level confidence is the mean frequency:\n\\begin{equation}\\label{eq:voting}\nc_{\\text{vote}}(x) = \\frac{1}{|E_\\cup|} \\sum_{e \\in E_\\cup} \\text{freq}(e)\n\\end{equation}\nWhen $E_\\cup = \\emptyset$ (no entity extracted by any sample), we set $c_{\\mathrm{vc}}(x) = 0$.\\footnote{This occurs in $<$1\\% of instances in our experiments (WNUT-17 only). Equation~\\ref{eq:voting} defines the continuous QE signal used throughout Table~\\ref{tab:quality_estimation} and all correlation analyses. For voted-output \\textit{selection} (Table~\\ref{tab:selection}), we include only entities with frequency ${>}N/2$, following standard majority voting. The two computations serve different purposes: Eq.~\\ref{eq:voting} assigns a continuous quality score per instance; the majority threshold constructs a discrete output for F1 evaluation. On NER, the threshold variant yields $\\rho{=}0.252$ (vs.\\ $0.379$ for Eq.~\\ref{eq:voting}), reflecting information loss from binarization; on RE, the difference is negligible ($\\Delta\\rho{=}0.019$).}\n\n\\subsection{Evaluation Framework}\\label{sec:evaluation}\n\n\\paragraph{Quality estimation.}\nWe measure rank correlation (Spearman $\\rho$) between the confidence signal and instance-level F1, and binary discrimination (AUROC) by classifying instances as above or below median F1.\nCorrelation analyses exclude instances with empty gold annotations ($n{=}529$ on SciERC after filtering 22/551), where F1 is trivially zero and consistency signals reflect agreement on the empty set rather than extraction quality; selection analyses retain the full set ($n{=}551$) because empty-gold instances contribute $\\Delta{=}0$ to all signals, introducing no bias in the greedy-vs-signal comparison.\n\n\\paragraph{Sample selection.}\nWe report best-of-$N$ F1: for each instance, the signal selects one sample.\nPer-sample signals (LP) directly rank candidates; instance-level signals select the sample closest to the consensus output (the consensus-proximity score for SJ is mathematically equivalent to leave-one-out SJ selection).\nWe compare against an \\textit{oracle} (highest-F1 sample) and a \\textit{greedy} baseline (a fixed sample from the $T{=}1.0$ candidate pool, providing a no-selection reference within the sampled distribution).\n\n\\paragraph{Complementarity.}\nHigh rank correlation does not guarantee effective sample selection: if per-sample variance is low, even a perfect quality estimator cannot distinguish among near-identical candidates (\\S\\ref{sec:selection_gap}).\n",
      "numLines": 78,
      "startLine": 1,
      "totalLines": 78
    }
  },
  "sourceToolAssistantUUID": "79992da1-447b-414b-8ecd-5b81f809f6c0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "f49c1ccb-97a0-4961-857d-2db0aa0e0624",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 36 · 2026-05-15T14:59:01.582Z_

<details open><summary>🔧 Tool call — Read · `toolu_01HgeEtSnXE3LWcWTggKJ4VL`</summary>

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
  "parentUuid": "9c112911-f278-470d-95de-2cc10cdc6ba0",
  "isSidechain": false,
  "requestId": "req_011Cb4YzcoF1Lm3bkaDjnvnu",
  "type": "assistant",
  "uuid": "ab97f275-b9fe-4c02-a723-9fc481f6f35c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "f49c1ccb-97a0-4961-857d-2db0aa0e0624",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ACxtx1Mci3DLrexRzQuKmB",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1656,
      "cache_read_input_tokens": 29230,
      "output_tokens": 865,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1656,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 865,
          "cache_read_input_tokens": 29230,
          "cache_creation_input_tokens": 1656,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1656
          },
          "type": "message"
        }
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

_source line 37 · 2026-05-15T14:59:01.587Z_

<details><summary>↩ Tool result · `toolu_01HgeEtSnXE3LWcWTggKJ4VL`</summary>

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
14	Both \textbf{Qwen3-8B} and \textbf{LLaMA-3.1-8B-Instruct} are fine-tuned with LoRA (rank$=$32, $\alpha{=}64$) for 5 epochs using LLaMA Factory \cite{zheng2024llamafactory} under identical training procedures, ensuring comparisons across the two model families (both at 8B scale) reflect model differences rather than training confounds.
15	We note a training confound for SciERC: Qwen3-8B's SciERC checkpoint was trained with \texttt{enable\_thinking=True} (LLaMA Factory 0.9.4 default), which prepends empty \texttt{&lt;think>\textbackslash n&lt;/think>} blocks (4--5 tokens) to each training response and includes them in the loss computation; CoNLL-2003 and WNUT-17 checkpoints explicitly set \texttt{enable\_thinking=False}.
16	No reasoning content is present (the blocks are always empty), and constrained decoding at inference time enforces JSON-only output, so thinking tokens do not appear in generated samples.
17	This constitutes a minor train--test distribution mismatch for SciERC ($<$0.3\% of the 2048-token training window); CoNLL-2003 and WNUT-17 are unaffected.
18	We discuss implications in the Limitations section.
19	We draw $N{=}8$ samples at $T{=}1.0$ (primary; single seed, seed${=}42$), with $N{=}16$ for scaling experiments.\footnote{$N{=}16$ results for CoNLL (Qwen) and SciERC (LLaMA) are in Table~\ref{tab:robustness} (Appendix~\ref{app:robustness}); detailed $N$-scaling analysis in Appendix~\ref{app:n_scaling}. A 3-seed stability analysis ($\sigma{\leq}0.026$; Table~\ref{tab:multiseed}, Appendix~\ref{app:multiseed}) confirms that signal rankings are identical across seeds.}
20	Quality estimation uses Spearman $\rho$ and AUROC; downstream utility uses best-of-$N$ selection macro F1 (instance-averaged) with exact span matching (NER) and head-tail-label matching (RE).
21	Inference uses vLLM with constrained decoding \cite{willard2023guided}.
22	
23	%% ============================================================
24	\subsection{Quality Estimation Results}
25	\label{sec:qe_results}
26	
27	\begin{table*}[t]
28	\centering
29	\small
30	\caption{Quality estimation across tasks and models (Spearman $\rho$ and AUROC; $N{=}8$, seed${=}42$). Best value per column in \textbf{bold}. SciERC evaluates joint NER (6 types) and RE (7 types, single benchmark---preliminary); CoNLL evaluates NER (4 types). $N{=}16$ results appear in Table~\ref{tab:robustness} (Appendix~\ref{app:robustness}).}
31	\label{tab:quality_estimation}
32	\begin{tabular}{ll cc cc cc cc}
33	\toprule
34	& & \multicolumn{2}{c}{\textbf{SciERC NER}} & \multicolumn{2}{c}{\textbf{SciERC RE}} & \multicolumn{2}{c}{\textbf{CoNLL (Qwen)}} & \multicolumn{2}{c}{\textbf{CoNLL (LLaMA)}} \\
35	\cmidrule(lr){3-4} \cmidrule(lr){5-6} \cmidrule(lr){7-8} \cmidrule(lr){9-10}
36	Signal & Family & $\rho$ & AUC & $\rho$ & AUC & $\rho$ & AUC & $\rho$ & AUC \\
37	\midrule
38	VC & Structural & \textbf{.379} & .684 & \textbf{.350} & .694 & .424 & .789 & .426 & .709 \\
39	SJ  & Structural & .360 & .692 & .250 & .670 & .436 & .801 & \textbf{.431} & .704 \\
40	FK & Surface & .267 & .629 & .275 & .609 & .400 & .774 & .428 & .703 \\
41	EM  & Surface    & .295 & \textbf{.749} & .134 & \textbf{.706} & \textbf{.451} & \textbf{.816} & \textbf{.431} & .705 \\
42	LP     & Model      & .205 & .578 & .266 & .601 & .316 & .753 & .307 & \textbf{.761} \\
43	\bottomrule
44	\end{tabular}
45	\end{table*}
46	
47	\begin{figure*}[t]
48	\centering
49	\includegraphics[width=\textwidth]{fig_signal_heatmap}
50	\caption{Quality estimation heatmap (Spearman $\rho$) across five signals and four configurations. Left: full evaluation set; right: conditional set (non-zero F1 instances). On the full set, structural signals dominate on SciERC NER while all signals converge on CoNLL. On the conditional set, EM emerges as the strongest signal on both NER ($\rho{=}0.360$) and RE ($\rho{=}0.417$), while LP RE collapses to near-zero ($\rho{=}0.011$).}
51	\label{fig:signal_heatmap}
52	\end{figure*}
53	
54	Table~\ref{tab:quality_estimation} presents rank correlation ($\rho$) and AUROC for five confidence signals across tasks and models.
55	
56	\paragraph{Difficulty-dependent signal complementarity.}
57	On SciERC NER (complex schema, 6 types), structural signals lead: VC achieves $\rho{=}0.379$ and SJ $\rho{=}0.360$, both outperforming surface ($\rho{\leq}0.295$) and LP ($\rho{=}0.205$).
58	This advantage persists on RE (VC $\rho{=}0.350$; preliminary, single benchmark), though all signals weaken due to the 40\% zero-F1 floor effect.
59	VC and SJ show moderate instance-level correlation (NER: $\rho{=}0.659$; RE: $\rho{=}0.605$), indicating information overlap but not redundancy; their differential behavior across difficulty levels reflects the complementary granularity of entity-level frequency vs.\ span-level set overlap.
60	While the best $\rho{=}0.38$ (VC) explains approximately 14\% of F1 variance, the best AUROC reaches 0.749 (EM), indicating strong binary discriminative power for the quality/failure classification most relevant to practitioners in quality-aware routing.\footnote{Semantic entropy \cite{kuhn2023semantic} achieves comparable AUROC on discrete-answer QA; direct comparison is not meaningful due to different output spaces.}
61	Pairwise bootstrap CIs confirm the SJ advantage over LP ($\Delta\rho{=}{+}0.155$, CI excludes zero) but not over EM ($\Delta\rho{=}{+}0.065$, marginal under Bonferroni correction; Table~\ref{tab:bootstrap_signal_ci}, Appendix~\ref{app:bootstrap_signal}).
62	
63	\paragraph{$\rho$--AUROC dissociation.}
64	Signal choice depends on the intended use: on NER, EM leads AUROC (0.749) despite ranking third in $\rho$ (0.295), preferred for binary quality triage; structural signals ($\rho{\geq}0.36$) are better for fine-grained ranking.
65	On CoNLL with LLaMA, LP leads AUROC (0.761) yet trails in $\rho$ (0.307), confirming this pattern across datasets.
66	
67	\paragraph{Signal rankings shift with task difficulty.}
68	On CoNLL (greedy F1${\approx}$0.91), EM leads ($\rho{=}0.451$, AUROC${=}0.816$), surpassing SJ and VC.
69	When most samples are near-correct, binary agreement captures remaining variance more efficiently than set-level similarity.
70	This crossover---EM${>}$SJ on easy tasks vs.\ SJ${>}$EM on hard tasks---demonstrates difficulty-dependent complementarity rather than a uniform structural advantage, suggesting practitioners should match signal type to expected task difficulty.
71	Stability across the two model families (both 8B) is strong: SJ achieves $\rho{=}0.436$ (Qwen) vs.\ $0.431$ (LLaMA) on CoNLL ($\Delta{=}0.005$, within 3-seed $\sigma{\approx}0.007$).
72	On WNUT-17 ($N{=}16$), where 52\% of instances receive zero F1, full-set correlations are misleading: VC achieves $\rho{=}0.724$ (AUROC${=}0.913$), but this is entirely driven by the zero/non-zero boundary (conditional $\rho{=}0.038$, n.s.; Table~\ref{tab:wnut}).
73	LP exhibits strong \textit{negative} correlation ($\rho{=}{-}0.410$, AUROC${=}0.219$).
74	We hypothesize that this reversal reflects overconfidence on out-of-distribution inputs \citep{xiong2024llm}: the model assigns high log-probabilities to fluent but incorrect entity patterns (e.g., common noun phrases that resemble but do not match rare WNUT entity types), while producing lower scores for genuinely uncertain outputs where it correctly hedges.
75	On the conditional set, all signals collapse toward weak or non-significant correlations ($\rho{\leq}0.35$), with SJ achieving only $\rho{=}0.089$ ($p{=}0.020$) on the full set---suggesting a capability boundary beyond which consistency signals capture binary success/failure but not quality gradation.
76	
77	\paragraph{Conditional filtering.}
78	Filtering to non-zero F1 instances separates binary success detection (can the model extract \textit{anything}?) from quality gradation (among successful extractions, which are better?), but excludes the hardest instances where models fail completely---the conditional set is easier on average.
79	This reshuffles signal rankings (Figure~\ref{fig:signal_heatmap}, right).
80	EM emerges as the strongest conditional signal on both NER ($\rho{=}0.360$) and RE ($\rho{=}0.417$; preliminary), while VC and FK drop substantially (VC NER: $0.379{\to}0.300$; FK NER: $0.267{\to}0.176$).
81	LP RE collapses to $\rho{=}0.011$, confirming its full-set correlation was driven by zero/non-zero separation.
82	This creates a natural complementarity: VC and SJ are preferred on the full set, while EM provides the most precise ranking within the non-trivial subset (see Appendix~\ref{app:additional} for details).
83	A two-stage pipeline---using structural signals for quality-aware routing, then EM for within-batch ranking among non-trivial instances---could leverage each signal's regime of strength.
84	
85	%% ============================================================
86	\subsection{The Correlation-Selection Gap}
87	\label{sec:selection_gap}
88	
89	\begin{figure*}[t]
90	\centering
91	\includegraphics[width=\textwidth]{fig_selection_gap}
92	\caption{The correlation-selection gap on SciERC ($N{=}8$, $T{=}1.0$). Left: NER; right: RE. Bars show best-of-$N$ selection F1; the line marks quality estimation $\rho$. Despite $\rho$ up to 0.38, no signal significantly outperforms greedy on either task (Fisher $p{=}0.54$ for NER LP, the best signal; Table~\ref{tab:selection}). Dashed line indicates oracle upper bound.}
93	\label{fig:selection_gap}
94	\end{figure*}
95	
96	\begin{table}[t]
97	\centering
98	\small
99	\caption{Best-of-$N$ selection F1 on SciERC ($N{=}8$, $T{=}1.0$). F1 is macro (instance-averaged), the natural metric for per-instance selection. NER: 3-seed mean${\pm}\sigma$ ($n{=}551$) with Fisher combined $p$ vs.\ greedy; RE: single seed (seed${=}42$, preliminary). Best non-oracle signal in \textbf{bold}. VC uses majority-threshold voting ($>{N/2}$) for selection, distinct from continuous QE (Eq.~\ref{eq:voting}). $^\dagger$Greedy baseline: a fixed sample from the $T{=}1.0$ candidate pool (not $T{=}0$ deterministic decoding), serving as the no-selection reference within the sampled distribution.}
100	\label{tab:selection}
101	\begin{tabular}{lccc}
102	\toprule
103	Method & NER F1 & $p$ & RE F1 \\
104	\midrule
105	Oracle & $0.745 \pm 0.004$ & --- & 0.585 \\
106	\midrule
107	LP           & $\mathbf{0.620} \pm 0.003$ & .54 & 0.395 \\
108	SJ           & $0.616 \pm 0.008$ & .75 & 0.386 \\
109	EM           & $0.609 \pm 0.005$ & ${>}.99$ & 0.372 \\
110	VC           & $0.595 \pm 0.007$ & ${>}.99$ & 0.359 \\
111	\midrule
112	Greedy$^\dagger$ & $0.620 \pm 0.002$ & --- & \textbf{0.404} \\
113	Random           & $0.582 \pm 0.005$ & --- & 0.354 \\
114	\bottomrule
115	\end{tabular}
116	\end{table}
117	
118	Despite strong quality estimation, confidence signals yield limited gains when used for best-of-$N$ selection (Table~\ref{tab:selection}, Figure~\ref{fig:selection_gap}).
119	Four of five signals are instance-level aggregates that assign a single score per input regardless of which sample is evaluated; they cannot rank candidates by construction.
120	The non-trivial question is whether log-probability---the only per-sample signal---can exploit the oracle headroom.
121	We anchor this analysis on SciERC, where output diversity is substantial: only 11--18\% of instances produce identical outputs across all $N{=}8$ samples, with 39--43\% unique outputs per instance (mean 3.5 distinct outputs), per-sample F1 standard deviation of 0.11--0.14, and mean pairwise SJ of 0.703.
122	
123	\paragraph{No significant improvement over greedy.}
124	We evaluate significance via 3-seed instance-level paired bootstrap resampling ($B{=}10{,}000$, Fisher combination; $n{=}551$).
125	On NER, the oracle (0.745, 3-seed mean) reveals 12.5~pp of headroom above greedy (0.620).
126	LP achieves the highest mean selection F1 (0.620), indistinguishable from greedy ($\Delta{=}{+}0.0$~pp, Fisher $p{=}0.54$).
127	On RE, the best signal (LP, 0.395) falls below greedy (0.404, $-0.9$\,pp, $p{=}0.80$; single seed), while 18.1~pp of oracle headroom remains; cross-seed analysis confirms RE LP failures are partially systematic (Appendix~\ref{app:lp_failure_stability}).
128	TOST equivalence testing confirms most signals are indistinguishable from greedy at ${\pm}2$--$3$~pp on NER; on RE, EM and VC fail equivalence even at ${\pm}5$~pp (Table~\ref{tab:tost}, Appendix~\ref{app:diversity}).
129	VC ($\rho{=}0.379$, the best quality estimator) selects---via majority-threshold voting, distinct from the continuous QE score---to only 0.595 on NER (3-seed mean), \textit{significantly below} greedy ($\Delta{=}{-}2.5$~pp, Fisher $p{<}0.001$).
130	The gap extends to CoNLL at $N{=}8$ (ceiling effect, 57--88\% identical outputs) and WNUT-17 (capability boundary; Table~\ref{tab:cross_selection}).
131	
132	\paragraph{Seed variability.}
133	While the 3-seed mean confirms the gap direction, individual seeds exhibit notable variance.
134	Seed~456 produces uniformly negative selection deltas across all five signals (VC $-3.4$~pp, EM $-2.0$~pp, SJ $-1.6$~pp, FK $-1.5$~pp, LP $-0.3$~pp), whereas seeds~42 and~123 show mixed behavior with LP achieving modest positive deltas ($+0.6$ and $-0.2$~pp respectively).
135	This variability does not undermine the central finding: even the most favorable single seed (seed~42, LP $\Delta{=}{+}0.6$~pp) falls short of significance ($p{=}0.19$), and the gap direction is consistent across all seeds for instance-level signals.
136	The seed sensitivity underscores that single-seed selection evaluations---common in the literature---may overstate or understate signal utility by several percentage points, motivating our multi-seed design.
137	
138	\paragraph{Quality estimation $\neq$ output selection.}
139	Instance-level confidence signals predict \textit{which inputs} the model handles reliably, not \textit{which output} among $N$ candidates is best.
140	When per-sample variance is low relative to instance-level difficulty, even perfect quality estimation cannot discriminate among near-identical candidates.
141	This gap has direct consequences for test-time scaling in IE \cite{brown2024monkeys, snell2025scaling}: closing it likely requires per-sample signals such as trained verifiers \cite{cobbe2021verifiers}.
142	
143	%% ============================================================
144	\subsection{Robustness}
145	\label{sec:robustness_main}
146	
147	Consistency-based signals show robust performance across $T{\in}\{0.7, 1.0\}$ (SJ NER $\Delta\rho{=}0.028$, bootstrap CI includes zero) and sublinear gains from $N{=}8$ to $N{=}16$, with structural signals maintaining their advantage over LP across all NER settings ($\Delta\rho{=}{+}0.135$ to ${+}0.175$; Table~\ref{tab:robustness}, Appendix~\ref{app:robustness}).
148	On RE, only VC consistently outperforms LP ($\Delta\rho{=}{+}0.012$, preliminary).
149	NER signals are reasonably calibrated (ECE 0.069--0.096; Appendix~\ref{app:calibration}), while RE miscalibration (ECE 0.109--0.339) and compound errors impose a ceiling at $\rho{\approx}0.28$ for $N{=}16$.
150	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ab97f275-b9fe-4c02-a723-9fc481f6f35c",
  "isSidechain": false,
  "promptId": "a8cee1eb-a5df-415d-8e30-c85446d1e0a7",
  "type": "user",
  "uuid": "6fb4c171-3107-4529-a7b2-fdda2ae1f169",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex",
      "content": "\\section{Experiments}\n\\label{sec:experiments}\n\n\\subsection{Experimental Setup}\n\\label{sec:setup}\n\n\\paragraph{Datasets.}\nWe evaluate on three English IE benchmarks spanning a difficulty gradient.\n\\textbf{SciERC} \\cite{luan2018scierc} contains 551 test instances annotated for joint NER (6 types) and RE (7 types).\n\\textbf{CoNLL-2003} \\cite{tjongkimsang2003conll} provides 3{,}453 test sentences with 4 entity types, where models achieve ${\\approx}$91\\% micro F1.\n\\textbf{WNUT-17} \\cite{derczynski2017wnut} consists of 1{,}287 social media instances with emerging entities, used to probe method boundaries (52\\% zero F1).\n\n\\paragraph{Models and sampling.}\nBoth \\textbf{Qwen3-8B} and \\textbf{LLaMA-3.1-8B-Instruct} are fine-tuned with LoRA (rank$=$32, $\\alpha{=}64$) for 5 epochs using LLaMA Factory \\cite{zheng2024llamafactory} under identical training procedures, ensuring comparisons across the two model families (both at 8B scale) reflect model differences rather than training confounds.\nWe note a training confound for SciERC: Qwen3-8B's SciERC checkpoint was trained with \\texttt{enable\\_thinking=True} (LLaMA Factory 0.9.4 default), which prepends empty \\texttt{&lt;think>\\textbackslash n&lt;/think>} blocks (4--5 tokens) to each training response and includes them in the loss computation; CoNLL-2003 and WNUT-17 checkpoints explicitly set \\texttt{enable\\_thinking=False}.\nNo reasoning content is present (the blocks are always empty), and constrained decoding at inference time enforces JSON-only output, so thinking tokens do not appear in generated samples.\nThis constitutes a minor train--test distribution mismatch for SciERC ($<$0.3\\% of the 2048-token training window); CoNLL-2003 and WNUT-17 are unaffected.\nWe discuss implications in the Limitations section.\nWe draw $N{=}8$ samples at $T{=}1.0$ (primary; single seed, seed${=}42$), with $N{=}16$ for scaling experiments.\\footnote{$N{=}16$ results for CoNLL (Qwen) and SciERC (LLaMA) are in Table~\\ref{tab:robustness} (Appendix~\\ref{app:robustness}); detailed $N$-scaling analysis in Appendix~\\ref{app:n_scaling}. A 3-seed stability analysis ($\\sigma{\\leq}0.026$; Table~\\ref{tab:multiseed}, Appendix~\\ref{app:multiseed}) confirms that signal rankings are identical across seeds.}\nQuality estimation uses Spearman $\\rho$ and AUROC; downstream utility uses best-of-$N$ selection macro F1 (instance-averaged) with exact span matching (NER) and head-tail-label matching (RE).\nInference uses vLLM with constrained decoding \\cite{willard2023guided}.\n\n%% ============================================================\n\\subsection{Quality Estimation Results}\n\\label{sec:qe_results}\n\n\\begin{table*}[t]\n\\centering\n\\small\n\\caption{Quality estimation across tasks and models (Spearman $\\rho$ and AUROC; $N{=}8$, seed${=}42$). Best value per column in \\textbf{bold}. SciERC evaluates joint NER (6 types) and RE (7 types, single benchmark---preliminary); CoNLL evaluates NER (4 types). $N{=}16$ results appear in Table~\\ref{tab:robustness} (Appendix~\\ref{app:robustness}).}\n\\label{tab:quality_estimation}\n\\begin{tabular}{ll cc cc cc cc}\n\\toprule\n& & \\multicolumn{2}{c}{\\textbf{SciERC NER}} & \\multicolumn{2}{c}{\\textbf{SciERC RE}} & \\multicolumn{2}{c}{\\textbf{CoNLL (Qwen)}} & \\multicolumn{2}{c}{\\textbf{CoNLL (LLaMA)}} \\\\\n\\cmidrule(lr){3-4} \\cmidrule(lr){5-6} \\cmidrule(lr){7-8} \\cmidrule(lr){9-10}\nSignal & Family & $\\rho$ & AUC & $\\rho$ & AUC & $\\rho$ & AUC & $\\rho$ & AUC \\\\\n\\midrule\nVC & Structural & \\textbf{.379} & .684 & \\textbf{.350} & .694 & .424 & .789 & .426 & .709 \\\\\nSJ  & Structural & .360 & .692 & .250 & .670 & .436 & .801 & \\textbf{.431} & .704 \\\\\nFK & Surface & .267 & .629 & .275 & .609 & .400 & .774 & .428 & .703 \\\\\nEM  & Surface    & .295 & \\textbf{.749} & .134 & \\textbf{.706} & \\textbf{.451} & \\textbf{.816} & \\textbf{.431} & .705 \\\\\nLP     & Model      & .205 & .578 & .266 & .601 & .316 & .753 & .307 & \\textbf{.761} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table*}\n\n\\begin{figure*}[t]\n\\centering\n\\includegraphics[width=\\textwidth]{fig_signal_heatmap}\n\\caption{Quality estimation heatmap (Spearman $\\rho$) across five signals and four configurations. Left: full evaluation set; right: conditional set (non-zero F1 instances). On the full set, structural signals dominate on SciERC NER while all signals converge on CoNLL. On the conditional set, EM emerges as the strongest signal on both NER ($\\rho{=}0.360$) and RE ($\\rho{=}0.417$), while LP RE collapses to near-zero ($\\rho{=}0.011$).}\n\\label{fig:signal_heatmap}\n\\end{figure*}\n\nTable~\\ref{tab:quality_estimation} presents rank correlation ($\\rho$) and AUROC for five confidence signals across tasks and models.\n\n\\paragraph{Difficulty-dependent signal complementarity.}\nOn SciERC NER (complex schema, 6 types), structural signals lead: VC achieves $\\rho{=}0.379$ and SJ $\\rho{=}0.360$, both outperforming surface ($\\rho{\\leq}0.295$) and LP ($\\rho{=}0.205$).\nThis advantage persists on RE (VC $\\rho{=}0.350$; preliminary, single benchmark), though all signals weaken due to the 40\\% zero-F1 floor effect.\nVC and SJ show moderate instance-level correlation (NER: $\\rho{=}0.659$; RE: $\\rho{=}0.605$), indicating information overlap but not redundancy; their differential behavior across difficulty levels reflects the complementary granularity of entity-level frequency vs.\\ span-level set overlap.\nWhile the best $\\rho{=}0.38$ (VC) explains approximately 14\\% of F1 variance, the best AUROC reaches 0.749 (EM), indicating strong binary discriminative power for the quality/failure classification most relevant to practitioners in quality-aware routing.\\footnote{Semantic entropy \\cite{kuhn2023semantic} achieves comparable AUROC on discrete-answer QA; direct comparison is not meaningful due to different output spaces.}\nPairwise bootstrap CIs confirm the SJ advantage over LP ($\\Delta\\rho{=}{+}0.155$, CI excludes zero) but not over EM ($\\Delta\\rho{=}{+}0.065$, marginal under Bonferroni correction; Table~\\ref{tab:bootstrap_signal_ci}, Appendix~\\ref{app:bootstrap_signal}).\n\n\\paragraph{$\\rho$--AUROC dissociation.}\nSignal choice depends on the intended use: on NER, EM leads AUROC (0.749) despite ranking third in $\\rho$ (0.295), preferred for binary quality triage; structural signals ($\\rho{\\geq}0.36$) are better for fine-grained ranking.\nOn CoNLL with LLaMA, LP leads AUROC (0.761) yet trails in $\\rho$ (0.307), confirming this pattern across datasets.\n\n\\paragraph{Signal rankings shift with task difficulty.}\nOn CoNLL (greedy F1${\\approx}$0.91), EM leads ($\\rho{=}0.451$, AUROC${=}0.816$), surpassing SJ and VC.\nWhen most samples are near-correct, binary agreement captures remaining variance more efficiently than set-level similarity.\nThis crossover---EM${>}$SJ on easy tasks vs.\\ SJ${>}$EM on hard tasks---demonstrates difficulty-dependent complementarity rather than a uniform structural advantage, suggesting practitioners should match signal type to expected task difficulty.\nStability across the two model families (both 8B) is strong: SJ achieves $\\rho{=}0.436$ (Qwen) vs.\\ $0.431$ (LLaMA) on CoNLL ($\\Delta{=}0.005$, within 3-seed $\\sigma{\\approx}0.007$).\nOn WNUT-17 ($N{=}16$), where 52\\% of instances receive zero F1, full-set correlations are misleading: VC achieves $\\rho{=}0.724$ (AUROC${=}0.913$), but this is entirely driven by the zero/non-zero boundary (conditional $\\rho{=}0.038$, n.s.; Table~\\ref{tab:wnut}).\nLP exhibits strong \\textit{negative} correlation ($\\rho{=}{-}0.410$, AUROC${=}0.219$).\nWe hypothesize that this reversal reflects overconfidence on out-of-distribution inputs \\citep{xiong2024llm}: the model assigns high log-probabilities to fluent but incorrect entity patterns (e.g., common noun phrases that resemble but do not match rare WNUT entity types), while producing lower scores for genuinely uncertain outputs where it correctly hedges.\nOn the conditional set, all signals collapse toward weak or non-significant correlations ($\\rho{\\leq}0.35$), with SJ achieving only $\\rho{=}0.089$ ($p{=}0.020$) on the full set---suggesting a capability boundary beyond which consistency signals capture binary success/failure but not quality gradation.\n\n\\paragraph{Conditional filtering.}\nFiltering to non-zero F1 instances separates binary success detection (can the model extract \\textit{anything}?) from quality gradation (among successful extractions, which are better?), but excludes the hardest instances where models fail completely---the conditional set is easier on average.\nThis reshuffles signal rankings (Figure~\\ref{fig:signal_heatmap}, right).\nEM emerges as the strongest conditional signal on both NER ($\\rho{=}0.360$) and RE ($\\rho{=}0.417$; preliminary), while VC and FK drop substantially (VC NER: $0.379{\\to}0.300$; FK NER: $0.267{\\to}0.176$).\nLP RE collapses to $\\rho{=}0.011$, confirming its full-set correlation was driven by zero/non-zero separation.\nThis creates a natural complementarity: VC and SJ are preferred on the full set, while EM provides the most precise ranking within the non-trivial subset (see Appendix~\\ref{app:additional} for details).\nA two-stage pipeline---using structural signals for quality-aware routing, then EM for within-batch ranking among non-trivial instances---could leverage each signal's regime of strength.\n\n%% ============================================================\n\\subsection{The Correlation-Selection Gap}\n\\label{sec:selection_gap}\n\n\\begin{figure*}[t]\n\\centering\n\\includegraphics[width=\\textwidth]{fig_selection_gap}\n\\caption{The correlation-selection gap on SciERC ($N{=}8$, $T{=}1.0$). Left: NER; right: RE. Bars show best-of-$N$ selection F1; the line marks quality estimation $\\rho$. Despite $\\rho$ up to 0.38, no signal significantly outperforms greedy on either task (Fisher $p{=}0.54$ for NER LP, the best signal; Table~\\ref{tab:selection}). Dashed line indicates oracle upper bound.}\n\\label{fig:selection_gap}\n\\end{figure*}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Best-of-$N$ selection F1 on SciERC ($N{=}8$, $T{=}1.0$). F1 is macro (instance-averaged), the natural metric for per-instance selection. NER: 3-seed mean${\\pm}\\sigma$ ($n{=}551$) with Fisher combined $p$ vs.\\ greedy; RE: single seed (seed${=}42$, preliminary). Best non-oracle signal in \\textbf{bold}. VC uses majority-threshold voting ($>{N/2}$) for selection, distinct from continuous QE (Eq.~\\ref{eq:voting}). $^\\dagger$Greedy baseline: a fixed sample from the $T{=}1.0$ candidate pool (not $T{=}0$ deterministic decoding), serving as the no-selection reference within the sampled distribution.}\n\\label{tab:selection}\n\\begin{tabular}{lccc}\n\\toprule\nMethod & NER F1 & $p$ & RE F1 \\\\\n\\midrule\nOracle & $0.745 \\pm 0.004$ & --- & 0.585 \\\\\n\\midrule\nLP           & $\\mathbf{0.620} \\pm 0.003$ & .54 & 0.395 \\\\\nSJ           & $0.616 \\pm 0.008$ & .75 & 0.386 \\\\\nEM           & $0.609 \\pm 0.005$ & ${>}.99$ & 0.372 \\\\\nVC           & $0.595 \\pm 0.007$ & ${>}.99$ & 0.359 \\\\\n\\midrule\nGreedy$^\\dagger$ & $0.620 \\pm 0.002$ & --- & \\textbf{0.404} \\\\\nRandom           & $0.582 \\pm 0.005$ & --- & 0.354 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nDespite strong quality estimation, confidence signals yield limited gains when used for best-of-$N$ selection (Table~\\ref{tab:selection}, Figure~\\ref{fig:selection_gap}).\nFour of five signals are instance-level aggregates that assign a single score per input regardless of which sample is evaluated; they cannot rank candidates by construction.\nThe non-trivial question is whether log-probability---the only per-sample signal---can exploit the oracle headroom.\nWe anchor this analysis on SciERC, where output diversity is substantial: only 11--18\\% of instances produce identical outputs across all $N{=}8$ samples, with 39--43\\% unique outputs per instance (mean 3.5 distinct outputs), per-sample F1 standard deviation of 0.11--0.14, and mean pairwise SJ of 0.703.\n\n\\paragraph{No significant improvement over greedy.}\nWe evaluate significance via 3-seed instance-level paired bootstrap resampling ($B{=}10{,}000$, Fisher combination; $n{=}551$).\nOn NER, the oracle (0.745, 3-seed mean) reveals 12.5~pp of headroom above greedy (0.620).\nLP achieves the highest mean selection F1 (0.620), indistinguishable from greedy ($\\Delta{=}{+}0.0$~pp, Fisher $p{=}0.54$).\nOn RE, the best signal (LP, 0.395) falls below greedy (0.404, $-0.9$\\,pp, $p{=}0.80$; single seed), while 18.1~pp of oracle headroom remains; cross-seed analysis confirms RE LP failures are partially systematic (Appendix~\\ref{app:lp_failure_stability}).\nTOST equivalence testing confirms most signals are indistinguishable from greedy at ${\\pm}2$--$3$~pp on NER; on RE, EM and VC fail equivalence even at ${\\pm}5$~pp (Table~\\ref{tab:tost}, Appendix~\\ref{app:diversity}).\nVC ($\\rho{=}0.379$, the best quality estimator) selects---via majority-threshold voting, distinct from the continuous QE score---to only 0.595 on NER (3-seed mean), \\textit{significantly below} greedy ($\\Delta{=}{-}2.5$~pp, Fisher $p{<}0.001$).\nThe gap extends to CoNLL at $N{=}8$ (ceiling effect, 57--88\\% identical outputs) and WNUT-17 (capability boundary; Table~\\ref{tab:cross_selection}).\n\n\\paragraph{Seed variability.}\nWhile the 3-seed mean confirms the gap direction, individual seeds exhibit notable variance.\nSeed~456 produces uniformly negative selection deltas across all five signals (VC $-3.4$~pp, EM $-2.0$~pp, SJ $-1.6$~pp, FK $-1.5$~pp, LP $-0.3$~pp), whereas seeds~42 and~123 show mixed behavior with LP achieving modest positive deltas ($+0.6$ and $-0.2$~pp respectively).\nThis variability does not undermine the central finding: even the most favorable single seed (seed~42, LP $\\Delta{=}{+}0.6$~pp) falls short of significance ($p{=}0.19$), and the gap direction is consistent across all seeds for instance-level signals.\nThe seed sensitivity underscores that single-seed selection evaluations---common in the literature---may overstate or understate signal utility by several percentage points, motivating our multi-seed design.\n\n\\paragraph{Quality estimation $\\neq$ output selection.}\nInstance-level confidence signals predict \\textit{which inputs} the model handles reliably, not \\textit{which output} among $N$ candidates is best.\nWhen per-sample variance is low relative to instance-level difficulty, even perfect quality estimation cannot discriminate among near-identical candidates.\nThis gap has direct consequences for test-time scaling in IE \\cite{brown2024monkeys, snell2025scaling}: closing it likely requires per-sample signals such as trained verifiers \\cite{cobbe2021verifiers}.\n\n%% ============================================================\n\\subsection{Robustness}\n\\label{sec:robustness_main}\n\nConsistency-based signals show robust performance across $T{\\in}\\{0.7, 1.0\\}$ (SJ NER $\\Delta\\rho{=}0.028$, bootstrap CI includes zero) and sublinear gains from $N{=}8$ to $N{=}16$, with structural signals maintaining their advantage over LP across all NER settings ($\\Delta\\rho{=}{+}0.135$ to ${+}0.175$; Table~\\ref{tab:robustness}, Appendix~\\ref{app:robustness}).\nOn RE, only VC consistently outperforms LP ($\\Delta\\rho{=}{+}0.012$, preliminary).\nNER signals are reasonably calibrated (ECE 0.069--0.096; Appendix~\\ref{app:calibration}), while RE miscalibration (ECE 0.109--0.339) and compound errors impose a ceiling at $\\rho{\\approx}0.28$ for $N{=}16$.\n",
      "numLines": 150,
      "startLine": 1,
      "totalLines": 150
    }
  },
  "sourceToolAssistantUUID": "ab97f275-b9fe-4c02-a723-9fc481f6f35c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "f49c1ccb-97a0-4961-857d-2db0aa0e0624",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 38 · 2026-05-15T14:59:02.633Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Jv5oUnfiJKHD5KhqLc4vkd`</summary>

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
  "parentUuid": "6fb4c171-3107-4529-a7b2-fdda2ae1f169",
  "isSidechain": false,
  "requestId": "req_011Cb4YzcoF1Lm3bkaDjnvnu",
  "type": "assistant",
  "uuid": "d5ffa8c6-170b-4165-955e-3e5f3e64b806",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "f49c1ccb-97a0-4961-857d-2db0aa0e0624",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ACxtx1Mci3DLrexRzQuKmB",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1656,
      "cache_read_input_tokens": 29230,
      "output_tokens": 865,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1656,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 865,
          "cache_read_input_tokens": 29230,
          "cache_creation_input_tokens": 1656,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1656
          },
          "type": "message"
        }
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

_source line 39 · 2026-05-15T14:59:02.656Z_

<details><summary>↩ Tool result · `toolu_01Jv5oUnfiJKHD5KhqLc4vkd`</summary>

```text
1	\section{Discussion}\label{sec:discussion}
2	
3	\paragraph{Practical recommendations.}
4	For per-instance quality ranking, VC provides the strongest rank correlation ($\rho{=}0.38$), though EM leads binary discrimination (AUROC${=}0.749$); under conditional filtering, EM leads on both NER and RE ($\rho{=}0.360$, $0.417$; RE: preliminary, single benchmark).
5	Signal rankings depend on task difficulty---EM dominates easy tasks (CoNLL), VC and SJ dominate hard tasks (SciERC)---directionally consistent across two model families at 8B scale, though with model-dependent magnitude.
6	At higher sample sizes ($N{=}16$), SJ converges to comparable NER performance with VC ($\Delta{=}0.002$) with lower cross-seed variance ($\sigma{=}0.010$ vs.\ $0.026$); on RE, only VC consistently outperforms LP (preliminary).
7	When model capability is insufficient (WNUT-17), all signals converge toward non-significant conditional correlations (Table~\ref{tab:wnut}).
8	
9	\paragraph{Why the gap exists: two layers.}
10	\textit{Layer 1 (definitional):} Four of five signals are instance-level aggregates that assign a single score per input; they cannot rank candidates by construction.
11	Consensus-proximity selection (\S\ref{sec:evaluation}) does not recover per-sample discrimination (Table~\ref{tab:selection}).
12	\textit{Layer 2 (score compression):} Log-probability, the only per-sample signal, also fails to exploit the 12--18~pp oracle headroom.
13	LP scores are severely compressed: the median within-instance LP range is only 0.041 nats, below the $\varepsilon{=}0.05$ threshold at which 60\% of instances are effectively tied, and 75\% of pairwise comparisons fall within $|\Delta|{<}0.026$ (Appendix~\ref{app:logprob_ties}).
14	In the 40\% of instances where compression is mitigated (LP range ${\geq}0.05$, $n{=}210$), LP \textit{significantly} outperforms greedy ($+2.9$~pp, $p{=}0.01$; within-instance $\rho$: 0.08$\to$0.39).
15	This diagnostic confirms that LP carries useful per-sample quality information; score compression is the primary mechanistic bottleneck.
16	A controlled NER ablation (\S\ref{sec:ablation}) confirms that LP compression persists without constrained decoding; on RE, the interaction is task-dependent.
17	Diversity-stratified analysis confirms the gap persists even among high-diversity instances (Appendix~\ref{app:diversity}); RE miscalibration (ECE 0.109--0.339, preliminary; Appendix~\ref{app:calibration}) may compound this.
18	
19	\paragraph{The gap widens with $N$.}
20	Doubling from $N{=}8$ to $N{=}16$ expands oracle headroom from 12.5 to 16.9~pp ($+4.4$~pp), yet signal-based selection fails to capture this growth.
21	LP, the best signal, improves by only $+0.4$~pp ($\Delta$: $+0.0{\to}+0.5$~pp), leaving 16.4~pp of headroom unrealized---a 31\% expansion of the gap.
22	VC deteriorates further ($\Delta$: $-2.5{\to}{-}3.1$~pp), a counterintuitive result for majority voting: with more candidates, systematic errors in entity-level frequency counts dominate, amplifying selection bias rather than correcting it.
23	On RE at $N{=}16$ (3-seed), the pattern is even more severe: oracle headroom reaches 17.1~pp, yet all four consistency signals fall below greedy (best: VC $\Delta{=}{-}0.8$~pp; worst: EM $\Delta{=}{-}1.5$~pp; all Fisher $p{>}0.77$; Table~\ref{tab:re_n16_selection}).
24	LP is the sole exception ($\Delta{=}{+}0.7$~pp, Fisher $p{=}0.058$), the only positive selection delta on either task at $N{=}16$, but does not reach significance.
25	This scaling behavior confirms that the correlation-selection gap is not a small-$N$ artifact; unsupervised signals face a structural ceiling that widens as oracle headroom grows.
26	
27	\paragraph{Connection to MBR decoding.}
28	Our selection strategies instantiate minimum Bayes risk (MBR) decoding \cite{eikema2022sampling, muller2021understanding}: each selects $\hat{y} = \arg\max_{y_i} \sum_{j \neq i} U(y_i, y_j)$ with utility $U$ defined by SJ, EM, or entity overlap.
29	Despite MBR's success in machine translation \cite{freitag2022high} and its extension to summarization, code generation, and captioning \cite{jinnai2024mbr}, all variants fail here because the utility functions correlate with F1 at the instance level but not within a single instance---the mathematical essence of the correlation-selection gap.
30	\citet{eikema2025structured} study structure-conditional MBR decoding and find that standard utility functions degrade on structured outputs---consistent with our finding that consensus-proximity selection fails in IE despite its success in machine translation.
31	
32	\paragraph{Score compression under free-form decoding.}\label{sec:ablation}
33	A natural hypothesis is that LP compression is an artifact of constrained decoding's restricted token space.
34	We test this via controlled ablation on SciERC (Qwen3-8B, single dataset): generating free-form (unconstrained) outputs on the same instances with post-hoc JSON parsing (parse rate 99.95\%, 4406/4408; Table~\ref{tab:freeform_ablation}).
35	For NER, LP variance is essentially unchanged (within-instance std ratio $0.97{\times}$, tied fraction 59.7\%$\to$57.7\%) and selection gains remain negligible ($+0.18$~pp free-form vs.\ $+0.59$~pp constrained), establishing that NER LP compression persists independent of decoding regime in our setting.
36	However, the ablation reveals a task-dependent interaction: RE LP selection flips from $-0.68$~pp (constrained) to $+1.69$~pp (free-form; preliminary, single seed).
37	This reversal falls within the NER bootstrap 95\% CI [$-3.0$, $+4.2$]~pp and is based on a single seed, so we do not treat it as a confirmed finding; it suggests that constrained decoding may interact differently with RE but requires multi-seed replication.
38	The NER/RE divergence indicates that the relationship between decoding regime and selection is task-specific in our setting.
39	Notably, the fine-tuned model achieved 99.95\% parse rate without grammar constraints, suggesting that constrained decoding's format-compliance role may be redundant for sufficiently fine-tuned models.
40	
41	\paragraph{Task-specific decoding interactions.}
42	The free-form ablation reveals divergent behavior across tasks.
43	On RE, LP selection flips from $-0.68$~pp (constrained) to $+1.69$~pp (free-form; preliminary, single RE benchmark), a reversal that spans all 7 relation types and is driven by selective variance reallocation ($p{<}0.0001$).
44	The win/loss ratio shifts from 36:59 (constrained) to 45:45 (free-form), with the gains concentrated on relation-dense instances (mean 3.3 gold relations).
45	This interaction does not generalize to NER, where selection remains negligible under both regimes.
46	This ablation uses a single seed (seed${=}42$); whether the RE reversal replicates across seeds and generalizes to other RE benchmarks warrants further investigation.
47	Second, the non-tied subset ($n{=}210$) is partially reshuffled under free-form decoding: Jaccard similarity between the constrained and free-form non-tied sets is 0.472, indicating that 87 instances newly gain LP discrimination while others lose it, yielding a $3{\times}$ increase in within-instance LP range for the newly non-tied subset.
48	Despite this reshuffling, aggregate NER selection gains remain negligible---score compression is not a fixed property of specific instances but rather a pervasive regime that shifts across instances without producing net selection improvement.
49	Free-form decoding also slightly improves quality estimation (NER VC $\rho$: 0.379$\to$0.409), though this does not translate to selection gains.
50	
51	\paragraph{Methodological implications.}
52	The decoupling of quality estimation ($\rho$), binary discrimination (AUROC), and sample selection (best-of-$N$ F1) means evaluating on a single metric risks selecting the wrong signal for the intended use case.
53	Effective selection likely requires per-sample signals such as trained verifiers \cite{cobbe2021verifiers, venktesh2025trust}; $N$-scaling analysis (Appendix~\ref{app:n_scaling}) shows $N{=}8$ captures most quality estimation benefit.
54	Cross-dataset evaluation confirms that structural signals are robust to domain shift when the training schema subsumes the target (VC $\rho{=}0.469$ OOD vs.\ $0.379$ in-domain); the reverse direction fails due to catastrophic model failure, not signal failure (Appendix~\ref{app:ood}).
55	Our findings are established under constrained decoding at 8B scale; a single-dataset NER ablation suggests LP compression persists without constrained decoding, but RE shows task-dependent interaction with decoding regime.
56	Whether these patterns generalize across datasets, model scales, and decoding strategies warrants further investigation.
57	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d5ffa8c6-170b-4165-955e-3e5f3e64b806",
  "isSidechain": false,
  "promptId": "a8cee1eb-a5df-415d-8e30-c85446d1e0a7",
  "type": "user",
  "uuid": "b0d83d0e-0695-419a-9533-e4aa01ae84b6",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex",
      "content": "\\section{Discussion}\\label{sec:discussion}\n\n\\paragraph{Practical recommendations.}\nFor per-instance quality ranking, VC provides the strongest rank correlation ($\\rho{=}0.38$), though EM leads binary discrimination (AUROC${=}0.749$); under conditional filtering, EM leads on both NER and RE ($\\rho{=}0.360$, $0.417$; RE: preliminary, single benchmark).\nSignal rankings depend on task difficulty---EM dominates easy tasks (CoNLL), VC and SJ dominate hard tasks (SciERC)---directionally consistent across two model families at 8B scale, though with model-dependent magnitude.\nAt higher sample sizes ($N{=}16$), SJ converges to comparable NER performance with VC ($\\Delta{=}0.002$) with lower cross-seed variance ($\\sigma{=}0.010$ vs.\\ $0.026$); on RE, only VC consistently outperforms LP (preliminary).\nWhen model capability is insufficient (WNUT-17), all signals converge toward non-significant conditional correlations (Table~\\ref{tab:wnut}).\n\n\\paragraph{Why the gap exists: two layers.}\n\\textit{Layer 1 (definitional):} Four of five signals are instance-level aggregates that assign a single score per input; they cannot rank candidates by construction.\nConsensus-proximity selection (\\S\\ref{sec:evaluation}) does not recover per-sample discrimination (Table~\\ref{tab:selection}).\n\\textit{Layer 2 (score compression):} Log-probability, the only per-sample signal, also fails to exploit the 12--18~pp oracle headroom.\nLP scores are severely compressed: the median within-instance LP range is only 0.041 nats, below the $\\varepsilon{=}0.05$ threshold at which 60\\% of instances are effectively tied, and 75\\% of pairwise comparisons fall within $|\\Delta|{<}0.026$ (Appendix~\\ref{app:logprob_ties}).\nIn the 40\\% of instances where compression is mitigated (LP range ${\\geq}0.05$, $n{=}210$), LP \\textit{significantly} outperforms greedy ($+2.9$~pp, $p{=}0.01$; within-instance $\\rho$: 0.08$\\to$0.39).\nThis diagnostic confirms that LP carries useful per-sample quality information; score compression is the primary mechanistic bottleneck.\nA controlled NER ablation (\\S\\ref{sec:ablation}) confirms that LP compression persists without constrained decoding; on RE, the interaction is task-dependent.\nDiversity-stratified analysis confirms the gap persists even among high-diversity instances (Appendix~\\ref{app:diversity}); RE miscalibration (ECE 0.109--0.339, preliminary; Appendix~\\ref{app:calibration}) may compound this.\n\n\\paragraph{The gap widens with $N$.}\nDoubling from $N{=}8$ to $N{=}16$ expands oracle headroom from 12.5 to 16.9~pp ($+4.4$~pp), yet signal-based selection fails to capture this growth.\nLP, the best signal, improves by only $+0.4$~pp ($\\Delta$: $+0.0{\\to}+0.5$~pp), leaving 16.4~pp of headroom unrealized---a 31\\% expansion of the gap.\nVC deteriorates further ($\\Delta$: $-2.5{\\to}{-}3.1$~pp), a counterintuitive result for majority voting: with more candidates, systematic errors in entity-level frequency counts dominate, amplifying selection bias rather than correcting it.\nOn RE at $N{=}16$ (3-seed), the pattern is even more severe: oracle headroom reaches 17.1~pp, yet all four consistency signals fall below greedy (best: VC $\\Delta{=}{-}0.8$~pp; worst: EM $\\Delta{=}{-}1.5$~pp; all Fisher $p{>}0.77$; Table~\\ref{tab:re_n16_selection}).\nLP is the sole exception ($\\Delta{=}{+}0.7$~pp, Fisher $p{=}0.058$), the only positive selection delta on either task at $N{=}16$, but does not reach significance.\nThis scaling behavior confirms that the correlation-selection gap is not a small-$N$ artifact; unsupervised signals face a structural ceiling that widens as oracle headroom grows.\n\n\\paragraph{Connection to MBR decoding.}\nOur selection strategies instantiate minimum Bayes risk (MBR) decoding \\cite{eikema2022sampling, muller2021understanding}: each selects $\\hat{y} = \\arg\\max_{y_i} \\sum_{j \\neq i} U(y_i, y_j)$ with utility $U$ defined by SJ, EM, or entity overlap.\nDespite MBR's success in machine translation \\cite{freitag2022high} and its extension to summarization, code generation, and captioning \\cite{jinnai2024mbr}, all variants fail here because the utility functions correlate with F1 at the instance level but not within a single instance---the mathematical essence of the correlation-selection gap.\n\\citet{eikema2025structured} study structure-conditional MBR decoding and find that standard utility functions degrade on structured outputs---consistent with our finding that consensus-proximity selection fails in IE despite its success in machine translation.\n\n\\paragraph{Score compression under free-form decoding.}\\label{sec:ablation}\nA natural hypothesis is that LP compression is an artifact of constrained decoding's restricted token space.\nWe test this via controlled ablation on SciERC (Qwen3-8B, single dataset): generating free-form (unconstrained) outputs on the same instances with post-hoc JSON parsing (parse rate 99.95\\%, 4406/4408; Table~\\ref{tab:freeform_ablation}).\nFor NER, LP variance is essentially unchanged (within-instance std ratio $0.97{\\times}$, tied fraction 59.7\\%$\\to$57.7\\%) and selection gains remain negligible ($+0.18$~pp free-form vs.\\ $+0.59$~pp constrained), establishing that NER LP compression persists independent of decoding regime in our setting.\nHowever, the ablation reveals a task-dependent interaction: RE LP selection flips from $-0.68$~pp (constrained) to $+1.69$~pp (free-form; preliminary, single seed).\nThis reversal falls within the NER bootstrap 95\\% CI [$-3.0$, $+4.2$]~pp and is based on a single seed, so we do not treat it as a confirmed finding; it suggests that constrained decoding may interact differently with RE but requires multi-seed replication.\nThe NER/RE divergence indicates that the relationship between decoding regime and selection is task-specific in our setting.\nNotably, the fine-tuned model achieved 99.95\\% parse rate without grammar constraints, suggesting that constrained decoding's format-compliance role may be redundant for sufficiently fine-tuned models.\n\n\\paragraph{Task-specific decoding interactions.}\nThe free-form ablation reveals divergent behavior across tasks.\nOn RE, LP selection flips from $-0.68$~pp (constrained) to $+1.69$~pp (free-form; preliminary, single RE benchmark), a reversal that spans all 7 relation types and is driven by selective variance reallocation ($p{<}0.0001$).\nThe win/loss ratio shifts from 36:59 (constrained) to 45:45 (free-form), with the gains concentrated on relation-dense instances (mean 3.3 gold relations).\nThis interaction does not generalize to NER, where selection remains negligible under both regimes.\nThis ablation uses a single seed (seed${=}42$); whether the RE reversal replicates across seeds and generalizes to other RE benchmarks warrants further investigation.\nSecond, the non-tied subset ($n{=}210$) is partially reshuffled under free-form decoding: Jaccard similarity between the constrained and free-form non-tied sets is 0.472, indicating that 87 instances newly gain LP discrimination while others lose it, yielding a $3{\\times}$ increase in within-instance LP range for the newly non-tied subset.\nDespite this reshuffling, aggregate NER selection gains remain negligible---score compression is not a fixed property of specific instances but rather a pervasive regime that shifts across instances without producing net selection improvement.\nFree-form decoding also slightly improves quality estimation (NER VC $\\rho$: 0.379$\\to$0.409), though this does not translate to selection gains.\n\n\\paragraph{Methodological implications.}\nThe decoupling of quality estimation ($\\rho$), binary discrimination (AUROC), and sample selection (best-of-$N$ F1) means evaluating on a single metric risks selecting the wrong signal for the intended use case.\nEffective selection likely requires per-sample signals such as trained verifiers \\cite{cobbe2021verifiers, venktesh2025trust}; $N$-scaling analysis (Appendix~\\ref{app:n_scaling}) shows $N{=}8$ captures most quality estimation benefit.\nCross-dataset evaluation confirms that structural signals are robust to domain shift when the training schema subsumes the target (VC $\\rho{=}0.469$ OOD vs.\\ $0.379$ in-domain); the reverse direction fails due to catastrophic model failure, not signal failure (Appendix~\\ref{app:ood}).\nOur findings are established under constrained decoding at 8B scale; a single-dataset NER ablation suggests LP compression persists without constrained decoding, but RE shows task-dependent interaction with decoding regime.\nWhether these patterns generalize across datasets, model scales, and decoding strategies warrants further investigation.\n",
      "numLines": 57,
      "startLine": 1,
      "totalLines": 57
    }
  },
  "sourceToolAssistantUUID": "d5ffa8c6-170b-4165-955e-3e5f3e64b806",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "f49c1ccb-97a0-4961-857d-2db0aa0e0624",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 40 · 2026-05-15T14:59:03.044Z_

<details open><summary>🔧 Tool call — Read · `toolu_018dvvE4T8c4jCAsNozWZH4L`</summary>

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
  "parentUuid": "b0d83d0e-0695-419a-9533-e4aa01ae84b6",
  "isSidechain": false,
  "requestId": "req_011Cb4YzcoF1Lm3bkaDjnvnu",
  "type": "assistant",
  "uuid": "525e1f97-ca4e-4a99-a993-d9b355644de6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "f49c1ccb-97a0-4961-857d-2db0aa0e0624",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ACxtx1Mci3DLrexRzQuKmB",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1656,
      "cache_read_input_tokens": 29230,
      "output_tokens": 865,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1656,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 865,
          "cache_read_input_tokens": 29230,
          "cache_creation_input_tokens": 1656,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1656
          },
          "type": "message"
        }
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

_source line 41 · 2026-05-15T14:59:03.049Z_

<details><summary>↩ Tool result · `toolu_018dvvE4T8c4jCAsNozWZH4L`</summary>

```text
1	\section{Conclusion}\label{sec:conclusion}
2	
3	We systematically evaluate five confidence signals across quality estimation, binary discrimination, and sample selection for LLM-based structured IE, revealing that these metrics decouple---single-metric evaluation risks selecting the wrong signal for the intended use case.
4	All signals achieve strong quality estimation ($\rho$ up to 0.38, AUROC up to 0.75) yet none significantly improves sample selection on SciERC despite 12--18~pp oracle headroom---the \textit{correlation-selection gap}.
5	The instance-level failure of four signals is definitional; the empirical finding is that neither consensus-proximity selection (MBR decoding) nor log-probability bridges the gap.
6	MBR utility correlates with quality across instances but not within them; LP scores are compressed into effective ties (60\% of instances), though where compression is mitigated, LP becomes a significant selector ($+2.9$~pp, $p{=}0.01$).
7	A controlled free-form decoding ablation confirms that NER LP compression persists without constrained decoding; on RE, LP selection reverses direction (preliminary), indicating task-dependent interaction with decoding regime.
8	Signal rankings shift with task difficulty---EM leads on easy tasks, SJ on hard tasks---consistent across two model families at 8B scale, though with model-dependent magnitude; at the capability boundary (WNUT-17), all signals collapse to non-significance.
9	RE findings rest on SciERC alone (preliminary) and warrant multi-benchmark validation.
10	Trained verifiers, scaling to 70B+ models, and conformal prediction are promising directions for closing the gap.
11	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "525e1f97-ca4e-4a99-a993-d9b355644de6",
  "isSidechain": false,
  "promptId": "a8cee1eb-a5df-415d-8e30-c85446d1e0a7",
  "type": "user",
  "uuid": "5213ea18-02d0-40aa-8f16-ceb03c39bb0a",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/conclusion.tex",
      "content": "\\section{Conclusion}\\label{sec:conclusion}\n\nWe systematically evaluate five confidence signals across quality estimation, binary discrimination, and sample selection for LLM-based structured IE, revealing that these metrics decouple---single-metric evaluation risks selecting the wrong signal for the intended use case.\nAll signals achieve strong quality estimation ($\\rho$ up to 0.38, AUROC up to 0.75) yet none significantly improves sample selection on SciERC despite 12--18~pp oracle headroom---the \\textit{correlation-selection gap}.\nThe instance-level failure of four signals is definitional; the empirical finding is that neither consensus-proximity selection (MBR decoding) nor log-probability bridges the gap.\nMBR utility correlates with quality across instances but not within them; LP scores are compressed into effective ties (60\\% of instances), though where compression is mitigated, LP becomes a significant selector ($+2.9$~pp, $p{=}0.01$).\nA controlled free-form decoding ablation confirms that NER LP compression persists without constrained decoding; on RE, LP selection reverses direction (preliminary), indicating task-dependent interaction with decoding regime.\nSignal rankings shift with task difficulty---EM leads on easy tasks, SJ on hard tasks---consistent across two model families at 8B scale, though with model-dependent magnitude; at the capability boundary (WNUT-17), all signals collapse to non-significance.\nRE findings rest on SciERC alone (preliminary) and warrant multi-benchmark validation.\nTrained verifiers, scaling to 70B+ models, and conformal prediction are promising directions for closing the gap.\n",
      "numLines": 11,
      "startLine": 1,
      "totalLines": 11
    }
  },
  "sourceToolAssistantUUID": "525e1f97-ca4e-4a99-a993-d9b355644de6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "f49c1ccb-97a0-4961-857d-2db0aa0e0624",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 42 · 2026-05-15T14:59:03.511Z_

<details open><summary>🔧 Tool call — Read · `toolu_01GDZFsyyfWqymvXAPHcLFsP`</summary>

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
  "parentUuid": "5213ea18-02d0-40aa-8f16-ceb03c39bb0a",
  "isSidechain": false,
  "requestId": "req_011Cb4YzcoF1Lm3bkaDjnvnu",
  "type": "assistant",
  "uuid": "dba49edc-4c8d-4b1d-9384-85ddf3bf2545",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "f49c1ccb-97a0-4961-857d-2db0aa0e0624",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ACxtx1Mci3DLrexRzQuKmB",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1656,
      "cache_read_input_tokens": 29230,
      "output_tokens": 865,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1656,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 865,
          "cache_read_input_tokens": 29230,
          "cache_creation_input_tokens": 1656,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1656
          },
          "type": "message"
        }
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

_source line 43 · 2026-05-15T14:59:03.525Z_

<details><summary>↩ Tool result · `toolu_01GDZFsyyfWqymvXAPHcLFsP`</summary>

```text
1	Our evaluation covers three datasets but only one RE benchmark (SciERC), where 40\% of instances receive zero F1, compressing the discriminable range and limiting signal differentiation for relation extraction.
2	RE selection failure persists even when restricting to non-zero F1 instances (Appendix~\ref{app:re_conditional_selection}), ruling out floor effects as the sole explanation, but generalization to other RE benchmarks remains unvalidated.
3	WNUT-17 confirms the capability boundary of our approach, but our positive results on formal-domain text (CoNLL, SciERC) have not been validated on informal or noisy text where models achieve non-trivial performance.
4	
5	We evaluate two model families (Qwen3-8B and LLaMA-3.1-8B), both at 8B parameters.
6	A 3-seed robustness analysis confirms that signal rankings are stable across seeds ($\sigma{\leq}0.026$; Table~\ref{tab:multiseed}), but whether our findings---particularly the correlation-selection gap and the difficulty-dependent signal ordering---hold for larger models (70B+) or closed-source APIs remains untested.
7	Larger models may produce higher-quality and more diverse samples, potentially altering the signal landscape.
8	
9	Our analysis of selection potential uses only unsupervised signals.
10	We do not train a dedicated verifier or reward model, leaving unknown how much of the oracle headroom a supervised approach could recover.
11	
12	We evaluate at $N{=}8$ and $N{=}16$.
13	The behavior of confidence signals at larger sample sizes (e.g., $N{=}64$ or $N{=}128$) is unknown, and $N$-scaling gains are setting-dependent: SJ improves by $+0.047$ on Qwen SciERC NER but only $+0.016$ on LLaMA SciERC NER when doubling from $N{=}8$ to $N{=}16$.
14	
15	On CoNLL with LLaMA, the SJ--FK gap is only 0.003 ($\rho{=}0.431$ vs.\ $0.428$), so the structural advantage over surface signals may not generalize to all simple-schema datasets.
16	Our free-form ablation (\S\ref{sec:ablation}) confirms that LP score compression persists without constrained decoding, but was conducted on a single dataset (SciERC) with one model (Qwen3-8B); whether the compression finding generalizes to other datasets, model families, or model scales remains untested.
17	
18	Qwen3-8B's SciERC checkpoint was trained with \texttt{enable\_thinking} active, injecting empty \texttt{&lt;think>&lt;/think>} blocks (4--5 tokens, no reasoning chain) before each response; CoNLL and WNUT checkpoints disabled this feature.
19	At inference time, constrained decoding suppresses thinking tokens in all configurations, so they do not appear in generated samples.
20	The empty blocks may weakly affect first-token probability distributions during training, potentially shifting LP score calibration on SciERC; however, since LP selection fails across all datasets including CoNLL and WNUT-17 (which lack this confound), the thinking token inconsistency is unlikely to explain the correlation-selection gap.
21	The absence of any reasoning content further limits the representational impact.
22	
23	One of three seeds (seed${=}456$) was run with \texttt{--subtask joint} (joint NER+RE decoding) rather than \texttt{--subtask ner} used by the other two seeds; the resulting NER F1 difference is ${<}0.3$~pp and falls within normal seed variance, so we retain this seed in 3-seed analyses without correction.
24	
25	Finally, log-probability was excluded from the temperature comparison ($T{=}0.7$ vs.\ $T{=}1.0$) due to missing $T{=}0.7$ LP data; all LP compression analyses use $T{=}1.0$ exclusively, and whether compression behavior changes at lower temperatures remains unknown.
26	The free-form ablation (within-instance std ratio $0.97{\times}$) provides stronger evidence that compression is not an artifact of the decoding strategy, but does not address temperature as a variable.
27	Since practitioners commonly deploy at $T{<}1.0$ for reliability, this untested dependence represents a gap between our evaluation conditions ($T{=}1.0$) and typical deployment settings.
28	Lower temperatures concentrate probability mass on fewer tokens, which could either reduce LP compression (by widening score gaps between high- and low-probability sequences) or exacerbate it (by collapsing diversity so that all $N$ samples share near-identical token-level likelihoods).
29	The direction of this interaction is not predictable from first principles and depends on how the model's likelihood surface interacts with the structured output space.
30	Resolving this would require a controlled $T$-sweep with LP data at each temperature, which our experimental pipeline did not collect.
31	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "dba49edc-4c8d-4b1d-9384-85ddf3bf2545",
  "isSidechain": false,
  "promptId": "a8cee1eb-a5df-415d-8e30-c85446d1e0a7",
  "type": "user",
  "uuid": "1d5ffc5f-14bd-48f0-be63-e2ddcdf35045",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/limitations.tex",
      "content": "Our evaluation covers three datasets but only one RE benchmark (SciERC), where 40\\% of instances receive zero F1, compressing the discriminable range and limiting signal differentiation for relation extraction.\nRE selection failure persists even when restricting to non-zero F1 instances (Appendix~\\ref{app:re_conditional_selection}), ruling out floor effects as the sole explanation, but generalization to other RE benchmarks remains unvalidated.\nWNUT-17 confirms the capability boundary of our approach, but our positive results on formal-domain text (CoNLL, SciERC) have not been validated on informal or noisy text where models achieve non-trivial performance.\n\nWe evaluate two model families (Qwen3-8B and LLaMA-3.1-8B), both at 8B parameters.\nA 3-seed robustness analysis confirms that signal rankings are stable across seeds ($\\sigma{\\leq}0.026$; Table~\\ref{tab:multiseed}), but whether our findings---particularly the correlation-selection gap and the difficulty-dependent signal ordering---hold for larger models (70B+) or closed-source APIs remains untested.\nLarger models may produce higher-quality and more diverse samples, potentially altering the signal landscape.\n\nOur analysis of selection potential uses only unsupervised signals.\nWe do not train a dedicated verifier or reward model, leaving unknown how much of the oracle headroom a supervised approach could recover.\n\nWe evaluate at $N{=}8$ and $N{=}16$.\nThe behavior of confidence signals at larger sample sizes (e.g., $N{=}64$ or $N{=}128$) is unknown, and $N$-scaling gains are setting-dependent: SJ improves by $+0.047$ on Qwen SciERC NER but only $+0.016$ on LLaMA SciERC NER when doubling from $N{=}8$ to $N{=}16$.\n\nOn CoNLL with LLaMA, the SJ--FK gap is only 0.003 ($\\rho{=}0.431$ vs.\\ $0.428$), so the structural advantage over surface signals may not generalize to all simple-schema datasets.\nOur free-form ablation (\\S\\ref{sec:ablation}) confirms that LP score compression persists without constrained decoding, but was conducted on a single dataset (SciERC) with one model (Qwen3-8B); whether the compression finding generalizes to other datasets, model families, or model scales remains untested.\n\nQwen3-8B's SciERC checkpoint was trained with \\texttt{enable\\_thinking} active, injecting empty \\texttt{&lt;think>&lt;/think>} blocks (4--5 tokens, no reasoning chain) before each response; CoNLL and WNUT checkpoints disabled this feature.\nAt inference time, constrained decoding suppresses thinking tokens in all configurations, so they do not appear in generated samples.\nThe empty blocks may weakly affect first-token probability distributions during training, potentially shifting LP score calibration on SciERC; however, since LP selection fails across all datasets including CoNLL and WNUT-17 (which lack this confound), the thinking token inconsistency is unlikely to explain the correlation-selection gap.\nThe absence of any reasoning content further limits the representational impact.\n\nOne of three seeds (seed${=}456$) was run with \\texttt{--subtask joint} (joint NER+RE decoding) rather than \\texttt{--subtask ner} used by the other two seeds; the resulting NER F1 difference is ${<}0.3$~pp and falls within normal seed variance, so we retain this seed in 3-seed analyses without correction.\n\nFinally, log-probability was excluded from the temperature comparison ($T{=}0.7$ vs.\\ $T{=}1.0$) due to missing $T{=}0.7$ LP data; all LP compression analyses use $T{=}1.0$ exclusively, and whether compression behavior changes at lower temperatures remains unknown.\nThe free-form ablation (within-instance std ratio $0.97{\\times}$) provides stronger evidence that compression is not an artifact of the decoding strategy, but does not address temperature as a variable.\nSince practitioners commonly deploy at $T{<}1.0$ for reliability, this untested dependence represents a gap between our evaluation conditions ($T{=}1.0$) and typical deployment settings.\nLower temperatures concentrate probability mass on fewer tokens, which could either reduce LP compression (by widening score gaps between high- and low-probability sequences) or exacerbate it (by collapsing diversity so that all $N$ samples share near-identical token-level likelihoods).\nThe direction of this interaction is not predictable from first principles and depends on how the model's likelihood surface interacts with the structured output space.\nResolving this would require a controlled $T$-sweep with LP data at each temperature, which our experimental pipeline did not collect.\n",
      "numLines": 31,
      "startLine": 1,
      "totalLines": 31
    }
  },
  "sourceToolAssistantUUID": "dba49edc-4c8d-4b1d-9384-85ddf3bf2545",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "f49c1ccb-97a0-4961-857d-2db0aa0e0624",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 44 · 2026-05-15T14:59:03.985Z_

<details open><summary>🔧 Tool call — Read · `toolu_01REvHJLsfmcFEZAeSdVGRkV`</summary>

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
  "parentUuid": "1d5ffc5f-14bd-48f0-be63-e2ddcdf35045",
  "isSidechain": false,
  "requestId": "req_011Cb4YzcoF1Lm3bkaDjnvnu",
  "type": "assistant",
  "uuid": "7a28e12d-cb64-4809-851f-67f9a2ce023d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "f49c1ccb-97a0-4961-857d-2db0aa0e0624",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ACxtx1Mci3DLrexRzQuKmB",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1656,
      "cache_read_input_tokens": 29230,
      "output_tokens": 865,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1656,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 865,
          "cache_read_input_tokens": 29230,
          "cache_creation_input_tokens": 1656,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1656
          },
          "type": "message"
        }
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

_source line 45 · 2026-05-15T14:59:04.329Z_

<details open><summary>🔧 Tool call — Read · `toolu_01XQmYjFQsySadtNYNByVocX`</summary>

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
  "parentUuid": "7a28e12d-cb64-4809-851f-67f9a2ce023d",
  "isSidechain": false,
  "requestId": "req_011Cb4YzcoF1Lm3bkaDjnvnu",
  "type": "assistant",
  "uuid": "b3b04bb9-807e-43b6-bbc9-852751bfd6f4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "f49c1ccb-97a0-4961-857d-2db0aa0e0624",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ACxtx1Mci3DLrexRzQuKmB",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1656,
      "cache_read_input_tokens": 29230,
      "output_tokens": 865,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1656,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 865,
          "cache_read_input_tokens": 29230,
          "cache_creation_input_tokens": 1656,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1656
          },
          "type": "message"
        }
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

_source line 46 · 2026-05-15T14:59:04.477Z_

<details><summary>↩ Tool result · `toolu_01REvHJLsfmcFEZAeSdVGRkV`</summary>

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
44	\quad SJ & $T{=}0.7$ & 0.388 & 0.234 \\
45	\quad SJ & $T{=}1.0$ & 0.360 & 0.250 \\
46	\quad FK & $T{=}0.7$ & 0.321 & 0.184 \\
47	\quad FK & $T{=}1.0$ & 0.267 & 0.275 \\
48	\midrule
49	\multicolumn{4}{l}{\textit{Sample size} (Qwen SciERC, $T{=}1.0$)} \\
50	\quad SJ & $N{=}8$  & 0.360 & 0.250 \\
51	\quad SJ & $N{=}16$ & 0.411$^\dagger$ & 0.281 \\
52	\quad FK & $N{=}8$  & 0.267 & 0.275 \\
53	\quad FK & $N{=}16$ & 0.283 & 0.279 \\
54	\midrule
55	\multicolumn{4}{l}{\textit{Across model families} (LLaMA CoNLL, $N{=}16$, 3 seeds)} \\
56	\quad SJ &  & $0.474{\pm}0.009$ & --- \\
57	\quad FK &  & $0.467{\pm}0.009$ & --- \\
58	\quad EM &  & $0.473{\pm}0.010$ & --- \\
59	\quad VC &  & $0.470{\pm}0.006$ & --- \\
60	\quad LP &  & $0.311{\pm}0.003$ & --- \\
61	\bottomrule
62	\end{tabular}
63	\end{table}
64	
65	\begin{figure}[t]
66	\centering
67	\includegraphics[width=\columnwidth]{fig_temperature_robustness}
68	\caption{Temperature robustness on SciERC ($N{=}8$). Top: NER; bottom: RE. SJ maintains stable $\rho$ across $T{=}0.7$ and $T{=}1.0$, while FK shows mixed sensitivity. LP $T{=}0.7$ data unavailable.}
69	\label{fig:temperature_robustness}
70	\end{figure}
71	
72	\paragraph{Temperature sensitivity.}
73	SJ NER $\rho$ shifts from 0.388 ($T{=}0.7$) to 0.360 ($T{=}1.0$), a difference of 0.028 whose bootstrap confidence interval includes zero.
74	FK shows mixed behavior: NER $\rho$ drops by 0.054, while RE $\rho$ increases by 0.091, likely reflecting reduced diversity at lower temperature interacting differently across tasks.
75	Across all comparisons, the SJ--FK relative ordering is preserved at both temperatures on NER (0.388 vs.\ 0.321 at $T{=}0.7$; 0.360 vs.\ 0.267 at $T{=}1.0$), indicating a stable signal hierarchy despite numerically small temperature effects.
76	
77	\paragraph{Sample size scaling.}
78	Increasing from $N{=}8$ to $N{=}16$ improves SJ on Qwen SciERC NER: $\rho$ rises from 0.360 to $0.411{\pm}0.010$ (three seeds: 0.398, 0.423, 0.410), a gain of $+0.047$.
79	The magnitude of $N$-scaling gains is setting-dependent---LLaMA SciERC NER yields $+0.016$ and Qwen CoNLL NER $+0.014$---though the direction is consistently positive.
80	LLaMA CoNLL exhibits the most uniform scaling: all four consistency signals gain $\Delta\rho{\approx}{+}0.042$ (range: $+0.039$ to $+0.044$) while LP gains only $+0.004$ (Table~\ref{tab:quality_estimation}).
81	FK $N$-scaling is seed-dependent: Qwen SciERC gains range from $+0.005$ to $+0.023$ across seeds (mean $+0.016$), while LLaMA CoNLL yields $+0.039$ (3-seed mean); individual seed FK shifts vary substantially under the unified pipeline, so this should not be interpreted as a robust trend.
82	VC $N$-scaling is consistently positive ($+0.005$ on Qwen CoNLL, $+0.018$ on LLaMA SciERC, $+0.030$ on Qwen SciERC), while LP is approximately $N$-invariant ($\Delta{\leq}0.034$).
83	SJ, EM, and VC scale consistently across all tested settings; only FK shows seed-dependent variation that does not constitute a reliable trend, suggesting that structural and binary-agreement signals are the most robust to $N$.
84	At $N{=}16$, SJ converges to comparable NER performance with VC ($\Delta{=}0.002$) while exhibiting lower cross-seed variance ($\sigma{=}0.010$ vs.\ $0.026$), making it a more stable alternative at higher sample sizes.
85	
86	\paragraph{Transfer across model families.}
87	LLaMA-3.1-8B-Instruct shows a similar SJ--FK ordering on SciERC NER (SJ $\rho{=}0.325{\pm}0.021$, FK $\rho{=}0.256{\pm}0.024$, $\Delta\rho{=}0.069$; permutation $p{=}0.06$, borderline).
88	On CoNLL, the gap across model families is minimal (Table~\ref{tab:quality_estimation}): SJ achieves $\rho{=}0.431$ (LLaMA) vs.\ 0.436 (Qwen), $\Delta{=}0.005$.
89	At $N{=}16$, the structural-over-LP advantage holds across all four tested NER settings: Qwen SciERC (VC $\rho{=}0.409$ vs.\ LP 0.239, $\Delta{=}{+}0.170$), Qwen CoNLL (EM $\rho{=}0.463$ vs.\ LP 0.328, $\Delta{=}{+}0.135$),\footnote{Qwen CoNLL $N{=}16$ was not recomputed under the unified pipeline; LP $\rho{=}0.328$ may differ slightly from the registry value (0.315) due to instance filtering.} LLaMA SciERC (VC $\rho{=}0.452$ vs.\ LP 0.277, $\Delta{=}{+}0.175$), and LLaMA CoNLL 3-seed (SJ $\rho{=}0.474{\pm}0.009$ vs.\ LP $0.311{\pm}0.003$, $\Delta{=}{+}0.163$).
90	
91	\section{Calibration Analysis}\label{app:calibration}
92	
93	\begin{figure*}[t]
94	\centering
95	\includegraphics[width=\textwidth]{fig_reliability}
96	\caption{Reliability diagrams on SciERC ($N{=}8$, $T{=}1.0$). Top: mean F1 vs.\ binned confidence; bottom: instance counts per bin. Left: NER; right: RE. NER signals are reasonably well-calibrated (calibration ECE 0.069--0.096), while RE shows greater miscalibration (ECE 0.109--0.339), reflecting the difficulty of calibrating confidence for compound extraction tasks.}
97	\label{fig:reliability}
98	\end{figure*}
99	
100	Reliability diagrams use 10 equal-width bins.
101	NER signals are reasonably well-calibrated (calibration ECE 0.069--0.096), while RE exhibits greater miscalibration (ECE 0.109--0.339), indicating that translating consistency scores into calibrated confidence estimates is feasible for NER but remains challenging for compound extraction tasks.
102	
103	\section{Additional Analyses}\label{app:additional}
104	
105	\paragraph{Per-relation diagnostic.}
106	RE signal degradation is relation-specific.
107	\textsc{Feature-Of} has near-zero correlation ($\rho{=}0.004$), while \textsc{Hyponym-Of} achieves $\rho{=}0.646$.
108	The primary bottleneck is entity span errors, which account for 55.5\% of RE false negatives---a prerequisite failure that consistency signals cannot detect, as they measure agreement among equally incorrect extractions.
109	We note that RE analysis relies on a single dataset (SciERC); generalization to other RE benchmarks remains to be validated.
110	
111	\paragraph{Capability stratification.}
112	For NER, SJ effectiveness scales with structural complexity: on SciERC instances with 6+ entities, $\rho{=}0.547$, compared to $\rho{=}0.415$ for 1--2 entities.
113	The SJ advantage over LP remains stable across sentence-length quartiles ($\Delta\rho{\approx}0.08$--$0.20$).
114	For RE, SJ $\rho$ increases monotonically with sentence length (Q1: 0.110 $\to$ Q4: 0.473; Fisher $z$-test $p{=}0.004$), indicating that longer, more relation-dense sentences provide richer structure for consistency-based estimation.
115	Both proxies are weakly correlated with F1 ($|r|{<}0.15$), confirming they capture input complexity rather than directly predicting output quality; however, entity count and sentence length are themselves moderately correlated ($\rho{=}0.650$), so they reflect overlapping rather than independent complexity dimensions.
116	For RE, entity count and relation count are strongly correlated ($\rho{=}0.769$) and thus reflect a single structural complexity dimension rather than independent axes.
117	On the high-complexity RE subset ($n{=}81$, high relation count), signals improve substantially: VC reaches $\rho{=}0.630$, LP $\rho{=}0.554$, and SJ $\rho{=}0.502$---all far above the full-set levels.
118	Richer relational structure provides more signal for consistency-based estimation, complementing the task-level boundary established by WNUT-17: structural signals are most effective within a ``sweet spot'' of sufficient model capability and sufficient output complexity.
119	
120	\paragraph{Length vs.\ log-probability.}
121	Figure~\ref{fig:length_logprob_scatter} shows that mean log-probability is weakly positively correlated with output length (NER: $\rho{=}0.386$, $n{=}4{,}232$; RE: $\rho{=}0.326$, $n{=}3{,}176$), ruling out length-penalty confounding as an explanation for LP's selection failure: longer outputs receive \textit{higher}, not lower, token-averaged log-probability under constrained decoding.
122	
123	\begin{figure}[t]
124	\centering
125	\includegraphics[width=\columnwidth]{fig_length_logprob_scatter}
126	\caption{Output length vs.\ mean log-probability on SciERC ($N{=}8$, $T{=}1.0$). Positive correlations (NER: $\rho{=}0.386$; RE: $\rho{=}0.326$) rule out length-penalty confounding.}
127	\label{fig:length_logprob_scatter}
128	\end{figure}
129	
130	\paragraph{Evaluation circularity and LOO-SJ equivalence.}
131	Consensus-proximity selection chooses $\hat{y} = \arg\max_{y_i} \sum_{j \neq i} \text{SJ}(y_i, y_j)$.
132	Leave-one-out SJ (LOO-SJ) for sample $y_i$ is $\text{LOO-SJ}_i = \frac{1}{N-1}\sum_{j \neq i} \text{SJ}(y_i, y_j)$.
133	Since the $\frac{1}{N-1}$ constant is shared across all candidates within an instance, $\arg\max_{y_i} \text{LOO-SJ}_i = \arg\max_{y_i} \sum_{j \neq i} \text{SJ}(y_i, y_j)$, making the two selection rules equivalent.
134	Standard (non-LOO) SJ adds the self-comparison term $\text{SJ}(y_i, y_i) = 1$ to each candidate, which is constant and thus does not affect ranking.
135	Empirically, LOO-SJ yields $\Delta\rho{=}{-}0.014$ relative to standard SJ (a correlation-level difference), with a maximum per-instance score difference of $3.1{\times}10^{-4}$ (negligible at the individual prediction level).
136	Evaluation circularity is negligible.
137	
138	\paragraph{Conditional filtering details.}
139	On LLaMA conditional RE (non-zero F1 instances), SJ recovers to $\rho{=}0.405$ while FK drops to $\rho{=}0.259$, consistent with the NER structural advantage; on full-set RE, however, the SJ--FK difference is non-significant ($\Delta\rho{=}{-}0.005$, $p{=}0.53$; preliminary).
140	At $N{=}16$, the divergence persists: SJ maintains $\rho{=}0.308$ on conditional RE while LP drops to $\rho{=}{-}0.026$.
141	EM ranks first across all four tested conditional configurations---SciERC NER ($\rho{=}0.360$), CoNLL Qwen $N{=}16$ ($\rho{=}0.466$), CoNLL LLaMA 3-seed ($\rho{=}0.462$), and SciERC RE ($\rho{=}0.417$)---despite full-set rankings ranging from \#1 (CoNLL Qwen) to \#5 (SciERC RE).
142	On the full set, EM is diluted by trivial agreement: instances where all $N$ samples produce identical (possibly incorrect) outputs receive EM${=}1$ regardless of quality, compressing the signal's dynamic range.
143	On the conditional set---where the model demonstrably produces varied outputs---exact agreement becomes the strongest quality signal.
144	The margin over SJ is largest on RE ($\Delta\rho{=}{+}0.171$), where compound extraction decisions amplify output variability, and smallest on CoNLL LLaMA ($\Delta\rho{=}{+}0.002$), where all signals converge near $\rho{\approx}0.46$.
145	
146	\paragraph{WNUT-17 full signal analysis.}
147	Table~\ref{tab:wnut} reports all five signals on WNUT-17.
148	VC achieves $\rho{=}0.724$ (AUROC${=}0.913$) on the full set, but conditional analysis (non-zero F1 instances) reveals this is entirely driven by the zero/non-zero boundary: conditional $\rho{=}0.038$ ($p{=}0.49$).
149	LP shows the reverse pattern: full-set $\rho{=}{-}0.410$ but conditional $\rho{=}0.350$, the highest among all signals on the conditional set.
150	This inversion confirms that full-set correlations on high-failure-rate datasets conflate binary success prediction with quality gradation.
151	
152	\begin{table}[t]
153	\centering
154	\small
155	\caption{Quality estimation on WNUT-17 (Qwen, $N{=}16$, $T{=}1.0$, $n{=}689$ after filtering gold-empty instances). Cond: non-zero F1 instances ($n{=}334$). LP exhibits strong negative full-set $\rho$; its conditional $\rho$ reverses to the highest among all signals, confirming that full-set correlations on high-failure-rate datasets conflate binary success prediction with quality gradation.}
156	\label{tab:wnut}
157	\begin{tabular}{lccccc}
158	\toprule
159	Signal & $\rho$ & $p$ & AUROC & Cond.\ $\rho$ & Cond.\ $p$ \\
160	\midrule
161	VC      & .724 & ${<}$1e-112 & .913 & .038 & .487 \\
162	FK      & .125 & .001 & .555 & .169 & .002 \\
163	SJ      & .089 & .020 & .517 & .288 & ${<}$1e-7 \\
164	EM      & .050 & .194 & .487 & .333 & ${<}$1e-9 \\
165	LP & $-$.410 & ${<}$1e-28 & .219 & .350 & ${<}$1e-10 \\
166	\bottomrule
167	\end{tabular}
168	\end{table}
169	
170	\paragraph{Cross-configuration selection analysis.}
171	Table~\ref{tab:cross_selection} extends the selection analysis to four additional configurations.
172	On LLaMA SciERC, where output diversity remains substantial (18\% identical outputs, 39\% unique), LP achieves the highest selection F1 (0.652) at $N{=}8$ but still falls within bootstrap noise of greedy (0.646), replicating the gap observed on Qwen SciERC (Table~\ref{tab:selection}).
173	On CoNLL, 57--88\% of instances produce identical outputs across all $N$ samples, reflecting a ceiling effect (greedy F1 ${\approx}$0.91--0.92) rather than signal failure; selection analysis on these configurations is uninformative because there is little per-sample variance for any signal to exploit.
174	
175	\begin{table*}[t]
176	\centering
177	\small
178	\caption{Best-of-$N$ selection F1 (macro, instance-averaged) across configurations ($T{=}1.0$). Best non-oracle signal per row in \textbf{bold}. At $N{=}8$, no signal significantly outperforms greedy in any configuration. At $N{=}16$ on LLaMA CoNLL, VC achieves small but significant gains ($+0.28$~pp, $p{<}0.03$; see text below). CoNLL shows especially tight clustering where greedy already exceeds 0.90.}
179	\label{tab:cross_selection}
180	\begin{tabular}{llccccccc}
181	\toprule
182	Config & $n$ & Greedy & Oracle & SJ & FK & EM & LP & VC \\
183	\midrule
184	LLaMA/SciERC $N{=}8$ & 529 & .646 & .778 & .643 & .639 & .634 & \textbf{.652} & .633 \\
185	LLaMA/SciERC $N{=}16$ & 529 & .645 & .806 & \textbf{.649} & \textbf{.649} & .640 & .646 & .640 \\
186	Qwen/CoNLL $N{=}8$ & 2{,}756 & .908 & .948 & \textbf{.899} & .893 & .898 & .897 & .895 \\
187	LLaMA/CoNLL $N{=}8$ & 2{,}756 & .924 & .943 & .924 & \textbf{.925} & .924 & .924 & .923 \\
188	\bottomrule
189	\end{tabular}
190	\end{table*}
191	
192	\paragraph{Diminishing returns of $N$-scaling.}
193	Our $N{=}8$ and $N{=}16$ comparisons (Table~\ref{tab:robustness}) characterize the marginal value of additional samples for test-time scaling \cite{brown2024monkeys, snell2025scaling}.
194	For quality estimation, structural signals benefit consistently but sublinearly: SJ $\rho$ improves by $+0.047$ (Qwen SciERC, 3-seed mean) and $+0.032$ (LLaMA CoNLL, 3-seed mean) when doubling from $N{=}8$ to $N{=}16$, while log-probability is approximately $N$-invariant ($\Delta\rho{\leq}0.021$).
195	Structural signals leverage $\binom{N}{2}$ pairwise comparisons (28 pairs at $N{=}8$, 120 at $N{=}16$), but the $\rho$ improvement is far less than proportional, indicating diminishing information per additional comparison.
196	This asymmetry gives structural signals a relative advantage in the compute-constrained regime: at $N{=}8$, SJ already achieves $\rho{=}0.431$ on LLaMA CoNLL (vs.\ LP $\rho{=}0.307$, $\Delta{=}{+}0.124$), and the gap \textit{widens} at $N{=}16$ ($\Delta{=}{+}0.163$) because structural signals continue to benefit from additional pairwise evidence while LP does not.
197	For sample selection, additional samples increase the oracle upper bound---more draws raise the probability of a high-quality candidate---but signal-based selection remains flat because the selector's inability to identify the best candidate is a granularity limitation, not a sample size limitation.
198	The practical implication is that $N{=}8$ captures most of the achievable quality estimation benefit; further scaling widens rather than closes the correlation-selection gap absent stronger per-sample selectors.
199	
200	\paragraph{$N{=}16$ CoNLL selection: small but significant.}
201	While quality estimation benefits sublinearly from $N$-scaling, selection behavior at $N{=}16$ reveals a nuanced exception on LLaMA CoNLL.
202	VC achieves the largest gain over greedy ($+0.28$~pp, $p{=}0.003$--$0.027$ across 3 seeds, all significant), with SJ, FK, and EM at $+0.22$--$0.23$~pp and LP at $+0.12$~pp (2/3 seeds significant).
203	These gains are statistically significant but practically minimal: oracle headroom at $N{=}16$ is only 2.5~pp, so VC captures approximately 10\% of the available headroom.
204	This reinforces the primary finding: even under the most favorable conditions---high baseline performance, more candidates, and aggregated multi-seed evidence---signal-based selection recovers only a fraction of the oracle headroom available.
205	
206	\section{Bootstrap CI for Signal Comparisons}\label{app:bootstrap_signal}
207	
208	Table~\ref{tab:bootstrap_signal_ci} reports bootstrap confidence intervals for individual signal $\rho$ and pairwise $\Delta\rho$ on SciERC NER ($N{=}8$, $n{=}529$, $B{=}10{,}000$, seed${=}42$).
209	The SJ--LP gap ($\Delta\rho{=}{+}0.155$) is clearly significant, confirming the structural advantage reported in \S\ref{sec:qe_results}.
210	The VC--SJ gap ($\Delta\rho{=}{+}0.019$) is not significant, indicating that these two structural signals perform comparably.
211	The SJ--EM gap ($\Delta\rho{=}{+}0.065$) is borderline significant, with the CI lower bound at $+0.003$ and upper bound at $+0.130$.
212	
213	\begin{table}[t]
214	\centering
215	\small
216	\caption{Bootstrap 95\% CIs for signal $\rho$ on SciERC NER ($N{=}8$, $n{=}529$, $B{=}10{,}000$, seed${=}42$). Top: individual signals. Bottom: pairwise $\Delta\rho$; ``Sig.'' indicates whether the 95\% CI excludes zero.}
217	\label{tab:bootstrap_signal_ci}
218	\begin{tabular}{lcc}
219	\toprule
220	Signal & $\rho$ & 95\% CI \\
221	\midrule
222	VC & +0.379 & [+0.299, +0.456] \\
223	SJ & +0.360 & [+0.277, +0.437] \\
224	EM & +0.295 & [+0.212, +0.371] \\
225	FK & +0.267 & [+0.176, +0.354] \\
226	LP & +0.205 & [+0.119, +0.291] \\
227	\bottomrule
228	\end{tabular}
229	
230	\vspace{0.5em}
231	
232	\begin{tabular}{lccc}
233	\toprule
234	Comparison & $\Delta\rho$ & 95\% CI & Sig. \\
235	\midrule
236	SJ $-$ LP & +0.155 & [+0.074, +0.234] & Yes \\
237	VC $-$ SJ & +0.019 & [$-$0.033, +0.073] & No \\
238	SJ $-$ EM & +0.065 & [+0.003, +0.130] & Marginal$^\dagger$ \\
239	\bottomrule
240	\end{tabular}
241	
242	\smallskip
243	{\footnotesize $^\dagger$Marginally significant without multiple comparison correction; would not survive Bonferroni correction for 10 pairwise comparisons ($\alpha_{\text{adj}}{=}0.005$).}
244	\end{table}
245	
246	At $N{=}16$ ($B{=}10{,}000$, permutation test), the structural advantage extends to FK comparisons.
247	On SciERC NER ($n{=}529$), SJ--FK ($\Delta\rho{=}0.147$--$0.160$, all $p{\leq}0.002$) and VC--FK ($\Delta\rho{=}0.138$--$0.188$, all $p{\leq}0.003$) are clearly significant across all three seeds; EM--FK is seed-dependent ($\Delta\rho{=}0.054$--$0.093$, $p{=}0.048$--$0.15$).
248	On CoNLL ($n{=}2{,}756$), all signals significantly outperform FK: EM $\Delta\rho{=}0.071$ ($p{<}0.001$), SJ $\Delta\rho{=}0.056$ ($p{<}0.001$), VC $\Delta\rho{=}0.022$ ($p{=}0.040$).
249	
250	\section{Diversity and Selection Analysis}\label{app:diversity}
251	
252	\paragraph{Output diversity quantification.}
253	Table~\ref{tab:diversity} summarizes output diversity across configurations.
254	On SciERC, output diversity is substantial: Qwen produces 43\% unique outputs per instance (mean 3.5 distinct out of $N{=}8$), with per-sample F1 standard deviation of 0.144 and mean pairwise SJ of 0.703.
255	LLaMA shows similar diversity (39\% unique, F1 std 0.11).
256	On CoNLL, diversity collapses: 57\% (Qwen) to 88\% (LLaMA) of instances produce identical outputs across all $N$ samples, reflecting a ceiling effect where greedy F1 already exceeds 0.90.
257	WNUT-17 shows 55\% identical outputs, driven by the 52\% zero-F1 rate.
258	
259	\begin{table}[t]
260	\centering
261	\small
262	\caption{Output diversity across configurations ($N{=}8$, $T{=}1.0$). ``Identical'' = fraction of instances with all $N$ outputs identical. ``Unique'' = mean fraction of distinct outputs per instance.}
263	\label{tab:diversity}
264	\begin{tabular}{lcc}
265	\toprule
266	Config & Identical & Unique \\
267	\midrule
268	Qwen/SciERC & 11\% & 43\% \\
269	LLaMA/SciERC & 18\% & 39\% \\
270	Qwen/CoNLL & 57\% & --- \\
271	LLaMA/CoNLL & 88\% & --- \\
272	WNUT-17 & 55\% & --- \\
273	\bottomrule
274	\end{tabular}
275	\end{table}
276	
277	\paragraph{Oracle-improvable fraction.}
278	Across SciERC configurations, 39--42\% of instances contain at least one sample with F1 exceeding greedy\footnote{Oracle-improvable and diversity-stratified analyses use $n{=}529$ (excluding instances with empty gold annotations; see \S\ref{sec:evaluation}); the diversity quantification in Table~\ref{tab:diversity} uses the full test set.}: Qwen NER 42.0\% (222/529, mean headroom $+$31.9~pp among improvable instances), Qwen RE 41.3\% (164/397, $+$45.3~pp), LLaMA NER 39.3\% (208/529, $+$33.7~pp).
279	On CoNLL, only 4--9\% of instances are improvable, confirming the ceiling effect.
280	
281	\paragraph{Diversity-stratified selection gap.}
282	On the 44\% of Qwen SciERC instances with high diversity (${\geq}4$ unique outputs among 8 samples, $n{=}232$), oracle headroom reaches $+$16.3~pp, yet all consistency-based signals (SJ, FK, EM, VC) select at or below greedy, and LP---the only per-sample signal---achieves merely $+$0.8~pp.
283	LLaMA replicates this pattern: on its high-diversity subset ($n{=}186$), oracle headroom reaches $+$20.1~pp while consistency signals remain at or below greedy and LP captures only $+$2.0~pp.
284	This rules out insufficient diversity as an explanation for the correlation-selection gap.
285	
286	\paragraph{TOST equivalence testing.}
287	The primary evidence against selection gains comes from effect sizes and confidence intervals: Cohen's $d{=}0.038$ for the best signal (NER LP) and bootstrap 95\% CI [$-$3.0, $+$4.2]~pp spanning zero.
288	Table~\ref{tab:tost} supplements this with two one-sided tests (TOST), testing whether each signal's selection F1 is equivalent to greedy within a bound $\delta$.
289	The $\delta$ values are contextualized against oracle headroom (12--18~pp): $\delta{=}5$~pp corresponds to forgoing 28--38\% of the available headroom, $\delta{=}3$~pp forgoing 17--23\%, and $\delta{=}2$~pp less than 15\%.
290	These proportions use the same test data that defines the headroom and should be interpreted as context for practical relevance rather than independent calibration.
291	The breakpoint $\delta^*$---the minimum equivalence margin at which each signal passes TOST---ranges from approximately 1.3~pp (SJ, ${\sim}$10\% of oracle headroom) to 3.4~pp (FK, ${\sim}$26\%) on NER, and from approximately 2.9~pp (LP, ${\sim}$16\%) to 6.5~pp (VC, ${\sim}$36\%) on RE.
292	On NER ($n{=}529$), at $\delta{=}{\pm}2$~pp, SJ and LP are confirmed equivalent to greedy (TOST $p{<}0.05$); at $\delta{=}{\pm}3$~pp, four of five signals pass; at $\delta{=}{\pm}5$~pp, all five pass.
293	On RE ($n{=}397$, preliminary), EM and VC fail equivalence even at $\delta{=}{\pm}5$~pp due to systematic underperformance ($\Delta{=}{-}3.2$~pp and $-4.5$~pp respectively).
294	The effect sizes are negligible ($d{=}0.038$) and confidence intervals span zero, with TOST confirming equivalence at practically meaningful margins.
295	
296	\begin{table}[t]
297	\centering
298	\small
299	\caption{TOST equivalence testing: signals vs.\ greedy on SciERC ($N{=}8$, $T{=}1.0$). \checkmark: equivalent at $p{<}0.05$; \texttimes: not equivalent. $\Delta$: mean F1 difference (signal $-$ greedy).}
300	\label{tab:tost}
301	\begin{tabular}{l cccc cccc}
302	\toprule
303	& \multicolumn{4}{c}{\textbf{NER}} & \multicolumn{4}{c}{\textbf{RE}} \\
304	\cmidrule(lr){2-5} \cmidrule(lr){6-9}
305	Signal & $\Delta$ & $\pm$2 & $\pm$3 & $\pm$5 & $\Delta$ & $\pm$2 & $\pm$3 & $\pm$5 \\
306	\midrule
307	LP & +0.6 & \checkmark & \checkmark & \checkmark & $-$0.9 & \texttimes & \checkmark & \checkmark \\
308	SJ & +0.1 & \checkmark & \checkmark & \checkmark & $-$1.8 & \texttimes & \texttimes & \checkmark \\
309	FK & $-$0.5 & \texttimes & \checkmark & \checkmark & $-$1.6 & \texttimes & \texttimes & \checkmark \\
310	EM & $-$0.8 & \texttimes & \checkmark & \checkmark & $-$3.2 & \texttimes & \texttimes & \texttimes \\
311	VC & $-$1.0 & \texttimes & \texttimes & \checkmark & $-$4.5 & \texttimes & \texttimes & \texttimes \\
312	\bottomrule
313	\end{tabular}
314	\end{table}
315	
316	\section{Multi-Seed Stability}\label{app:multiseed}
317	
318	Table~\ref{tab:multiseed} reports quality estimation metrics across three random seeds for both model families on SciERC ($N{=}8$, $T{=}1.0$).
319	On NER, the signal ranking VC${>}$SJ${>}$EM${>}$FK${>}$LP is identical across all six model-seed combinations, with $\sigma{\leq}0.025$ for all signals.
320	On RE (Qwen only, preliminary), VC remains the top signal ($\rho{=}0.309{\pm}0.024$), but LP rises to \#2 ($\rho{=}0.297{\pm}0.022$), above FK, SJ, and EM---a reversal from the NER ranking that reflects RE's higher sensitivity to per-sample scoring.
321	LLaMA absolute values are systematically lower than Qwen on NER, consistent with the directionally-consistent-but-magnitude-dependent characterization in the main text.
322	
323	\begin{table}[t]
324	\centering
325	\small
326	\caption{Multi-seed quality estimation on SciERC ($N{=}8$, $T{=}1.0$, seeds: 42, 123, 456). NER: both models; RE: Qwen only (preliminary). Signal ranking is stable across seeds ($\sigma{\leq}0.025$). $\sigma$ is population standard deviation over 3 seeds.}
327	\label{tab:multiseed}
328	\begin{tabular}{lccccc}
329	\toprule
330	& LP & FK & SJ & VC & EM \\
331	\midrule
332	\multicolumn{6}{l}{\textit{NER Spearman $\rho$ (mean $\pm\sigma$)}} \\
333	Qwen & .217${\pm}$.013 & .254${\pm}$.016 & .364${\pm}$.018 & .386${\pm}$.019 & .307${\pm}$.008 \\
334	LLaMA & .162${\pm}$.025 & .256${\pm}$.024 & .325${\pm}$.021 & .384${\pm}$.014 & .279${\pm}$.011 \\
335	\midrule
336	\multicolumn{6}{l}{\textit{RE Spearman $\rho$ (mean $\pm\sigma$, Qwen)}} \\
337	Qwen & .297${\pm}$.022 & .290${\pm}$.012 & .249${\pm}$.002 & .309${\pm}$.024 & .135${\pm}$.016 \\
338	\midrule
339	\multicolumn{6}{l}{\textit{NER AUROC (mean $\pm\sigma$)}} \\
340	Qwen & .613${\pm}$.002 & .618${\pm}$.009 & .684${\pm}$.009 & .697${\pm}$.010 & .661${\pm}$.010 \\
341	LLaMA & .577${\pm}$.007 & .616${\pm}$.011 & .655${\pm}$.010 & .689${\pm}$.005 & .636${\pm}$.006 \\
342	\bottomrule
343	\end{tabular}
344	\end{table}
345	
346	\section{Training Configuration}\label{app:training}
347	
348	Both models are fine-tuned with identical hyperparameters (Table~\ref{tab:training}) to ensure comparisons across model families reflect model differences rather than training confounds.
349	
350	\begin{table}[t]
351	\centering
352	\small
353	\caption{Training configuration. Both Qwen3-8B and LLaMA-3.1-8B-Instruct use identical settings unless noted.}
354	\label{tab:training}
355	\begin{tabular}{ll}
356	\toprule
357	Parameter & Value \\
358	\midrule
359	LoRA rank / $\alpha$ & 32 / 64 \\
360	LoRA target & All linear modules \\
361	LoRA dropout & 0 \\
362	Optimizer & AdamW \\
363	Learning rate & 2e-4, cosine schedule \\
364	Warmup ratio & 0.1 \\
365	Effective batch size & 16 (2 $\times$ grad.\ accum.\ 8) \\
366	Epochs & 5 \\
367	Max sequence length & 2048 \\
368	Precision & bf16 \\
369	Gradient checkpointing & Enabled \\
370	Max gradient norm & 1.0 \\
371	Training seed & 42 \\
372	Framework & LLaMA Factory \\
373	\midrule
374	\multicolumn{2}{l}{\textit{Dataset-specific}} \\
375	SciERC split & 1861 / 275 / 551 \\
376	CoNLL / WNUT & +\,load\_best\_model\_at\_end, \\
377	& eval\_steps${=}$200, save\_limit${=}$5 \\
378	\bottomrule
379	\end{tabular}
380	\end{table}
381	
382	\paragraph{Prompt template.}
383	For NER, we use a structured prompt:
384	\begin{quote}
385	\small
386	\texttt{System:} You are an expert in Named Entity Recognition.\\
387	\texttt{User:} Extract all named entities from the following text. Output as JSON.\\
388	Text: \texttt{\{input\_text\}}\\
389	Entity types: \texttt{\{schema\_types\}}
390	\end{quote}
391	RE follows the same structure with ``Relation Extraction'' and relation type lists substituted accordingly.
392	
393	\paragraph{Constrained decoding.}
394	Inference uses vLLM with XGrammar-based JSON schema enforcement \cite{willard2023guided}, which constrains outputs to valid entity/relation structures matching the target schema.
395	This eliminates format errors but may compress per-sample diversity by restricting the output space.\footnote{SciERC training used \texttt{enable\_thinking=True} (LLaMA Factory 0.9.4 default), injecting empty \texttt{&lt;think>&lt;/think>} blocks (4--5 tokens) into each training response with loss computation; CoNLL and WNUT explicitly set \texttt{enable\_thinking=False}. Constrained decoding at inference time enforces JSON-only output, suppressing thinking tokens. See \S\ref{sec:setup} and Limitations for discussion of this confound.}
396	
397	\section{Log-Probability Score Compression}\label{app:logprob_ties}
398	
399	Under constrained decoding, log-probability scores are severely compressed within instances, limiting per-sample discrimination (Table~\ref{tab:logprob_ties}, Figure~\ref{fig:lp_range_cdf}).
400	The median within-instance LP range is only 0.041 nats---below the $\varepsilon{=}0.05$ threshold used throughout, providing data-driven justification for this cutoff rather than an arbitrary choice.
401	At $\varepsilon{=}0.05$, 60.3\% of instances ($n{=}529$, excluding empty gold annotations) have a within-sample range below the threshold, and 75\% of pairwise comparisons are effective ties ($|\Delta|{<}0.026$).
402	The CDF rises smoothly with no cliff or discontinuity (Figure~\ref{fig:lp_range_cdf}), confirming that compression is a pervasive regime rather than a bimodal split.
403	For comparison, SJ has only 12.5\% tied instances at the same threshold---SJ's advantage over LP for selection is one of score resolution, not information content.
404	
405	\begin{figure}[t]
406	\centering
407	\includegraphics[width=\columnwidth]{fig_lp_range_cdf}
408	\caption{CDF of within-instance LP range on SciERC NER ($N{=}8$, $n{=}529$). The median LP range is 0.041 nats (dashed line), below $\varepsilon{=}0.05$. The smooth CDF confirms compression is pervasive, not bimodal.}
409	\label{fig:lp_range_cdf}
410	\end{figure}
411	
412	\begin{table}[t]
413	\centering
414	\small
415	\caption{Log-probability score compression on SciERC NER ($N{=}8$, $n{=}529$). ``Tied'' = fraction of instances where within-instance LP range ${<}\varepsilon$.}
416	\label{tab:logprob_ties}
417	\begin{tabular}{lc}
418	\toprule
419	$\varepsilon$ threshold & Tied instances (\%) \\
420	\midrule
421	0.01 & 1.1\% \\
422	0.05 & 60.3\% \\
423	0.1  & ${\sim}$84\% \\
424	0.5  & ${\sim}$99\% \\
425	\bottomrule
426	\end{tabular}
427	\end{table}
428	
429	\paragraph{Non-tied subset.}
430	Among instances with LP range ${\geq}0.05$ ($n{=}210$, 40\% of total), log-probability selection \textit{significantly} outperforms greedy ($+2.9$~pp F1, $p{=}0.01$), and within-instance $\rho(\text{LP}, \text{F1})$ rises from 0.08 (tied subset) to 0.39 (non-tied subset).
431	As a continuous complement to the binary tied/non-tied analysis, pooled within-instance $\rho(\text{LP}, \text{F1}){=}0.248$ across all instances confirms weak but positive per-sample signal; however, only 21.6\% of instances achieve $p{<}0.05$ significance, and $\rho(\text{LP range}, \text{F1 range}){=}0.328$ shows that instances with more LP spread also exhibit more F1 variability---LP carries information but compression limits its exploitation.
432	A free-form NER decoding ablation (Appendix~\ref{app:freeform_ablation}) confirms this compression persists without constrained decoding.
433	
434	\section{RE Conditional Selection}\label{app:re_conditional_selection}
435	
436	Table~\ref{tab:re_cond_selection} extends the selection analysis to the RE non-zero F1 subset.
437	Of $n{=}397$ RE instances, 238 (60\%) have non-zero F1 and 159 (40\%) have zero F1.
438	All five signals underperform greedy on both subsets.
439	On the non-zero subset, selection performance is \textit{worse} than on the full set (e.g., VC: $-10.0$~pp on non-zero vs.\ $-4.5$~pp on full set), because greedy is already strong on non-zero instances (F1${=}0.674$) and signals actively select inferior samples.
440	Oracle headroom exists (0.757 vs.\ 0.674) but no signal exploits it, ruling out the 40\% zero-F1 floor effect as the explanation for RE selection failure.
441	
442	\begin{table}[t]
443	\centering
444	\small
445	\caption{RE selection F1 (macro, instance-averaged) on SciERC ($N{=}8$, $T{=}1.0$). Full set ($n{=}397$) and non-zero F1 subset ($n{=}238$). No signal outperforms greedy on either subset.}
446	\label{tab:re_cond_selection}
447	\begin{tabular}{lcc}
448	\toprule
449	Method & Full ($n{=}397$) & Non-zero ($n{=}238$) \\
450	\midrule
451	Oracle & 0.585 & 0.757 \\
452	\midrule
453	LP & 0.395 & 0.600 \\
454	SJ & 0.386 & 0.604 \\
455	EM & 0.372 & 0.583 \\
456	VC & 0.359 & 0.574 \\
457	\midrule
458	Greedy & 0.404 & 0.674 \\
459	\bottomrule
460	\end{tabular}
461	\end{table}
462	
463	\section{RE $N{=}16$ Selection Analysis}\label{app:re_n16_selection}
464	
465	Table~\ref{tab:re_n16_selection} extends the selection analysis to RE at $N{=}16$ with 3-seed statistics.
466	All four consistency signals underperform greedy, with EM showing the largest deficit ($\Delta{=}{-}1.5$~pp, Fisher $p{>}0.99$).
467	LP is the only positive signal ($\Delta{=}{+}0.7$~pp, Fisher $p{=}0.058$), driven primarily by seed~456 ($\Delta{=}{+}1.5$~pp, $p{=}0.026$); the remaining seeds show smaller effects ($+0.1$ and $+0.6$~pp, $p{>}0.20$).
468	Even the most favorable seed captures only ${\sim}9\%$ of the 17.1~pp oracle headroom.
469	This cross-task consistency---LP as the only viable selection signal on both NER and RE---reinforces the structural limitation of instance-level signals for candidate ranking.
470	
471	\begin{table}[t]
472	\centering
473	\small
474	\caption{RE best-of-$N$ selection F1 (macro, instance-averaged) on SciERC ($N{=}16$, $T{=}1.0$, 3-seed mean${\pm}\sigma$, $n{=}551$). Fisher combined $p$ vs.\ greedy. LP is the only signal with positive $\Delta$. $\sigma$ is population standard deviation over 3 seeds.}
475	\label{tab:re_n16_selection}
476	\begin{tabular}{lccc}
477	\toprule
478	Method & F1 & $\Delta$ (pp) & $p$(Fisher) \\
479	\midrule
480	Oracle & $.463{\pm}.006$ & $+$17.1 & --- \\
481	\midrule
482	LP & $\mathbf{.299}{\pm}.007$ & $+$0.7 & .058 \\
483	VC & $.284{\pm}.002$ & $-$0.8 & .973 \\
484	FK & $.283{\pm}.005$ & $-$0.9 & .985 \\
485	SJ & $.281{\pm}.005$ & $-$1.0 & .993 \\
486	EM & $.277{\pm}.007$ & $-$1.5 & .999 \\
487	\midrule
488	Greedy & $.291{\pm}.000$ & --- & --- \\
489	Random & $.262{\pm}.001$ & $-$2.9 & --- \\
490	\bottomrule
491	\end{tabular}
492	\end{table}
493	
494	\section{Free-Form Decoding Ablation}\label{app:freeform_ablation}
495	
496	Table~\ref{tab:freeform_ablation} compares constrained and free-form decoding across four dimensions on SciERC ($N{=}8$, $T{=}1.0$, Qwen3-8B).
497	Free-form decoding removes grammar constraints entirely; outputs are parsed post-hoc (parse rate 99.95\%, 4406/4408).
498	LP score distributions are nearly identical across regimes (Panel~A: within-instance std ratio $0.97{\times}$), and NER selection gains remain negligible under both regimes (Panel~B).
499	RE LP selection flips positive under free-form decoding ($+1.69$~pp vs.\ $-0.68$~pp constrained).
500	Quality estimation improves modestly for most signals under free-form decoding (Panel~C), with the largest gain for FK ($+0.053$ NER, $+0.039$ RE).
501	
502	\begin{table*}[t]
503	\centering
504	\caption{Comparison of constrained vs.\ free-form decoding on SciERC (Qwen3-8B, $N{=}8$, $T{=}1.0$, seed=42).}
505	\label{tab:freeform_ablation}
506	
507	\vspace{2pt}
508	{\small\textsc{Panel A: Logprob Distribution}}
509	\vspace{2pt}
510	
511	\begin{tabular}{lccc}
512	\toprule
513	Metric & Constrained & Free-form & $\Delta$ \\
514	\midrule
515	Mean LP std        & 0.0206 & 0.0199 & $-$0.0007 \\
516	Mean LP range      & 0.0623 & 0.0599 & $-$0.0024 \\
517	Tied fraction ($\varepsilon{=}0.05$) & 59.7\% & 57.7\% & $-$2.0\,pp \\
518	\bottomrule
519	\end{tabular}
520	
521	\vspace{8pt}
522	
523	{\small\textsc{Panel B: Selection F1}}
524	\vspace{2pt}
525	
526	\begin{tabular}{llccc}
527	\toprule
528	Task & Method & Constrained & Free-form & $\Delta$ \\
529	\midrule
530	\multirow{3}{*}{NER}
531	  & Greedy        & 0.6182 & 0.6204 & $+$0.0022 \\
532	  & LP-selected   & 0.6241 & 0.6222 & $-$0.0019 \\
533	  & Selection gap & $+$0.0059 & $+$0.0018 & $-$0.0041 \\
534	\midrule
535	\multirow{3}{*}{RE}
536	  & Greedy        & 0.2913 & 0.2880 & $-$0.0033 \\
537	  & LP-selected   & 0.2845 & 0.3050 & \textbf{$+$0.0205} \\
538	  & Selection gap & $-$0.0068 & $+$0.0169 & \textbf{$+$0.0237} \\
539	\bottomrule
540	\end{tabular}
541	
542	\vspace{8pt}
543	
544	{\small\textsc{Panel C: QE Signal Quality (Spearman $\rho$)}}
545	\vspace{2pt}
546	
547	\begin{tabular}{l ccc ccc}
548	\toprule
549	 & \multicolumn{3}{c}{NER ($n{=}529$)} & \multicolumn{3}{c}{RE ($n{=}397$)} \\
550	\cmidrule(lr){2-4} \cmidrule(lr){5-7}
551	Signal & Constr. & Free & $\Delta$ & Constr. & Free & $\Delta$ \\
552	\midrule
553	SJ & 0.360 & 0.377 & $+$0.018 & 0.250 & 0.273 & $+$0.023 \\
554	FK & 0.267 & 0.320 & $+$0.053 & 0.275 & 0.315 & $+$0.039 \\
555	LP & 0.205 & 0.213 & $+$0.008 & 0.266 & 0.304 & $+$0.038 \\
556	EM & 0.295 & 0.317 & $+$0.023 & 0.134 & 0.137 & $+$0.002 \\
557	VC & 0.379 & 0.409 & $+$0.030 & 0.350 & 0.323 & $-$0.026 \\
558	\bottomrule
559	\end{tabular}
560	
561	\vspace{8pt}
562	
563	{\small\textsc{Panel D: Parse Rate (Free-form)}}
564	\vspace{2pt}
565	
566	\begin{tabular}{lc}
567	\toprule
568	Metric & Value \\
569	\midrule
570	Total samples          & 4408 \\
571	Parse rate             & 99.95\% \\
572	Instances 8/8 valid    & 549\,/\,551 (99.6\%) \\
573	\bottomrule
574	\end{tabular}
575	
576	\end{table*}
577	
578	\section{LP Selection Failure Stability}\label{app:lp_failure_stability}
579	
580	We analyze RE LP selection failures across three random seeds (constrained decoding, $N{=}8$, $T{=}1.0$, Qwen3-8B) to assess whether failures are systematic or stochastic.
581	
582	\paragraph{Pairwise overlap.}
583	LP selection failures (instances where LP-selected F1 $<$ greedy F1) show moderate cross-seed stability: the average pairwise Jaccard similarity is 0.42 (range: 0.38--0.46), indicating that failures are partially systematic---driven by instance complexity---but not fully deterministic.
584	The 3-way intersection contains 34 instances (27.9\% of any-seed failures), confirming a stable failure core.
585	
586	\paragraph{Instance complexity drives failure.}
587	Table~\ref{tab:stable_failures} stratifies instances by failure stability.
588	Stable failures (all 3 seeds) involve more gold relations (2.12 vs.\ 1.62 for never-fail instances) and higher greedy F1 (0.688 vs.\ 0.429), indicating that LP mis-selects on instances where the model already performs well---precisely the instances where selection would be most valuable.
589	Failure rate increases monotonically with gold relation count: 4.3\% at 1 relation, 20.7\% at 3 relations, 26.2\% at 6 relations.
590	
591	\begin{table}[t]
592	\centering
593	\small
594	\caption{RE LP selection failure stability across 3 seeds (SciERC, $N{=}8$). Stable failures concentrate on relation-dense instances with high greedy F1.}
595	\label{tab:stable_failures}
596	\begin{tabular}{lcccc}
597	\toprule
598	Group & $n$ & Gold rels & Greedy F1 & LP $\Delta$F1 \\
599	\midrule
600	Stable fail (3 seeds) & 34 & 2.12 & 0.688 & $-$0.499 \\
601	Fail 2+ seeds & 26 & 2.46 & 0.774 & $-$0.450 \\
602	Fail 1 seed & 62 & 2.32 & 0.692 & $-$0.239 \\
603	Never fail & 429 & 1.62 & 0.429 & $+$0.041 \\
604	\bottomrule
605	\end{tabular}
606	\end{table}
607	
608	\paragraph{Flip instances.}
609	Only 5 RE instances with gold relations flip from LP failure (constrained) to LP success (free-form), with mean gold relation count 3.67 (well above the population mean of 1.86).
610	These instances show large constrained LP errors ($\Delta{=}{-}0.430$) that reverse under free-form decoding ($\Delta{=}{+}0.503$), but their rarity (5/397) confirms that the RE selection flip is driven by aggregate variance reallocation rather than systematic instance-level correction.
611	
612	\section{$N$-Scaling Detailed Analysis}\label{app:n_scaling}
613	
614	Tables~\ref{tab:n-scaling}--\ref{tab:sigma-comparison} provide detailed $N$-scaling analysis on Qwen3-8B SciERC with 3-seed statistics.
615	
616	\begin{table}[t]
617	\centering
618	\caption{Effect of sample pool size on signal quality (Qwen3-8B, SciERC, 3-seed mean Spearman $\rho$).}
619	\label{tab:n-scaling}
620	\small
621	\begin{tabular}{l ccc ccc}
622	\toprule
623	 & \multicolumn{3}{c}{\textbf{NER} $\rho$} & \multicolumn{3}{c}{\textbf{RE} $\rho$} \\
624	\cmidrule(lr){2-4} \cmidrule(lr){5-7}
625	Signal & $N\!=\!8$ & $N\!=\!16$ & $\Delta$ & $N\!=\!8$ & $N\!=\!16$ & $\Delta$ \\
626	\midrule
627	SJ & 0.3641 & 0.4105 & \textbf{+0.0464} & 0.2485 & 0.2758 & \textbf{+0.0273} \\
628	FK & 0.2536 & 0.2833 & \textbf{+0.0297} & 0.2903 & 0.2964 & \textbf{+0.0061} \\
629	VC & 0.3861 & 0.4092 & \textbf{+0.0231} & 0.3088 & 0.3738 & \textbf{+0.0650} \\
630	LP & 0.2167 & 0.2393 & \textbf{+0.0226} & 0.2970 & 0.3100 & \textbf{+0.0130} \\
631	EM & 0.3071 & 0.3395 & \textbf{+0.0324} & 0.1353 & 0.1506 & \textbf{+0.0153} \\
632	\midrule
633	Mean & 0.3055 & 0.3364 & \textbf{+0.0308} & 0.2560 & 0.2813 & \textbf{+0.0253} \\
634	\bottomrule
635	\end{tabular}
636	\end{table}
637	
638	\begin{table}[t]
639	\centering
640	\caption{Cross-seed signal ranking stability (Kendall's $W$, 3 seeds).}
641	\label{tab:ranking-stability}
642	\small
643	\begin{tabular}{ll cc l}
644	\toprule
645	Model & Task & $N$ & Kendall's $W$ & Consensus ranking \\
646	\midrule
647	Qwen  & NER & 8  & 1.000 & VC $>$ SJ $>$ EM $>$ FK $>$ LP \\
648	Qwen  & NER & 16 & 0.956 & SJ $\approx$ VC $>$ EM $>$ FK $>$ LP \\
649	Qwen  & RE  & 8  & 0.822 & VC $>$ LP $>$ FK $>$ SJ $>$ EM \\
650	Qwen  & RE  & 16 & 0.956 & VC $>$ LP $>$ FK $>$ SJ $>$ EM \\
651	LLaMA & NER & 8  & 1.000 & VC $>$ SJ $>$ EM $>$ FK $>$ LP \\
652	\bottomrule
653	\end{tabular}
654	\end{table}
655	
656	\begin{table}[t]
657	\centering
658	\caption{Cross-seed standard deviation ($\sigma$) of Spearman $\rho$ at $N\!=\!8$ vs.\ $N\!=\!16$ (Qwen3-8B, SciERC, 3 seeds). $\sigma$ is population standard deviation.}
659	\label{tab:sigma-comparison}
660	\small
661	\begin{tabular}{l cc cc}
662	\toprule
663	 & \multicolumn{2}{c}{\textbf{NER} $\sigma_\rho$} & \multicolumn{2}{c}{\textbf{RE} $\sigma_\rho$} \\
664	\cmidrule(lr){2-3} \cmidrule(lr){4-5}
665	Signal & $N\!=\!8$ & $N\!=\!16$ & $N\!=\!8$ & $N\!=\!16$ \\
666	\midrule
667	SJ & 0.0179 & 0.0102 & 0.0015 & 0.0067 \\
668	FK & 0.0157 & 0.0079 & 0.0121 & 0.0143 \\
669	VC & 0.0187 & 0.0260 & 0.0244 & 0.0158 \\
670	EM & 0.0076 & 0.0031 & 0.0157 & 0.0049 \\
671	LP & 0.0125 & 0.0017 & 0.0218 & 0.0152 \\
672	\midrule
673	Mean & 0.0145 & 0.0098 & 0.0151 & 0.0114 \\
674	\bottomrule
675	\end{tabular}
676	\end{table}
677	
678	Signal rankings are highly stable across seeds: Kendall's $W{=}1.000$ for NER at $N{=}8$ (both models), dropping only to $W{=}0.956$ at $N{=}16$ where SJ and VC converge (Table~\ref{tab:ranking-stability}).
679	Doubling $N$ reduces cross-seed $\sigma$ by 32\% on NER and 24\% on RE (Table~\ref{tab:sigma-comparison}), with the largest reductions for SJ ($-43\%$ NER) and EM ($-59\%$ NER), confirming that additional samples stabilize structural signals more than LP.
680	
681	\section{Cross-Dataset OOD Analysis}\label{app:ood}
682	
683	To test whether confidence signals generalize under domain shift, we evaluate models on out-of-distribution data: a SciERC-trained model applied to CoNLL instances (wider$\to$narrower schema) and vice versa (Table~\ref{tab:ood}).
684	
685	\begin{table}[t]
686	\centering
687	\small
688	\caption{Cross-dataset OOD quality estimation (Spearman $\rho$, Qwen3-8B, $N{=}8$, $T{=}1.0$, seed${=}42$). SciERC$\to$CoNLL: SciERC-trained model on CoNLL instances ($n{=}2756$). CoNLL$\to$SciERC: CoNLL-trained model on SciERC instances ($n{=}529$, excluded from conclusions due to catastrophic model failure). In-domain $\rho$ from Table~\ref{tab:quality_estimation} (same model, same seed). \textsuperscript{***}$p{<}0.001$, \textsuperscript{*}$p{<}0.05$.}
689	\label{tab:ood}
690	\begin{tabular}{l ccc ccc}
691	\toprule
692	 & \multicolumn{3}{c}{\textbf{SciERC$\to$CoNLL}} & \multicolumn{3}{c}{\textbf{CoNLL$\to$SciERC}} \\
693	\cmidrule(lr){2-4} \cmidrule(lr){5-7}
694	Signal & $\rho$ & In-dom. & $\Delta$ & $\rho$ & In-dom. & $\Delta$ \\
695	\midrule
696	VC & .469\textsuperscript{***} & .379 & +.090 & +.105\textsuperscript{*} & .379 & $-$.274 \\
697	SJ & .378\textsuperscript{***} & .360 & +.018 & $-$.186\textsuperscript{***} & .360 & $-$.546 \\
698	EM & .300\textsuperscript{***} & .295 & +.005 & $-$.202\textsuperscript{***} & .295 & $-$.497 \\
699	FK & .285\textsuperscript{***} & .267 & +.018 & $-$.070 & .267 & $-$.337 \\
700	LP & .246\textsuperscript{***} & .205 & +.041 & $-$.152\textsuperscript{***} & .205 & $-$.357 \\
701	\bottomrule
702	\end{tabular}
703	\end{table}
704	
705	\paragraph{Wider-to-narrower schema transfer.}
706	When the SciERC-trained model (6 NER types) is applied to CoNLL (4 types), all signals remain significant ($p{<}0.001$) and structural signals improve over their in-domain levels (same model, seed${=}42$, $N{=}8$; in-domain $\rho$ from Table~\ref{tab:quality_estimation}): VC reaches $\rho{=}0.469$ (in-domain $0.379$, $\Delta{=}{+}0.090$), SJ $\rho{=}0.378$ (in-domain $0.360$, $\Delta{=}{+}0.018$), and FK $\rho{=}0.285$ (in-domain $0.267$, $\Delta{=}{+}0.018$).
707	The wider training schema subsumes CoNLL's narrower schema, so the model produces reasonable outputs even out-of-domain (greedy F1${=}0.522$), and structural signals benefit from the simpler target schema's reduced output ambiguity.
708	
709	\paragraph{Narrower-to-wider schema transfer (excluded).}
710	The reverse direction is excluded from our conclusions due to catastrophic model failure, not signal failure.
711	The CoNLL-trained model recognizes only 4 news entity types (PER, ORG, LOC, MISC) and has no relation extraction capability; when applied to SciERC's 6 scientific entity types and 7 relation types, the model cannot produce meaningful structured outputs (greedy NER F1${=}0.009$, RE F1${=}0.001$).
712	Under this regime, most signals flip to negative or near-zero correlations (Table~\ref{tab:ood}); only VC retains weak positive correlation ($\rho{=}0.105$, $p{=}0.016$).
713	These negative correlations reflect the model systematically generating confident but incorrect outputs---a capability failure analogous to WNUT-17 (\S\ref{sec:qe_results}), not evidence against signal utility.
714	
715	\paragraph{Asymmetry interpretation.}
716	The directional asymmetry is driven by schema coverage: wider$\to$narrower preserves signal utility because the SciERC model's 6-type schema subsumes CoNLL's 4 types, while narrower$\to$wider fails because the CoNLL model lacks the entity and relation types required by SciERC.
717	This extends the capability boundary identified on WNUT-17 to the domain-shift setting: confidence signals require sufficient model capability as a prerequisite, and results from the CoNLL$\to$SciERC direction should not be interpreted as evidence of signal degradation under domain shift.
718	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7a28e12d-cb64-4809-851f-67f9a2ce023d",
  "isSidechain": false,
  "promptId": "a8cee1eb-a5df-415d-8e30-c85446d1e0a7",
  "type": "user",
  "uuid": "68e425f4-41f3-4f4d-a276-3bd5c8d830dd",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
      "content": "\\section{Notation}\\label{app:notation}\n\nTable~\\ref{tab:notation} summarizes the notation used throughout the paper.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{cl}\n\\toprule\nSymbol & Meaning \\\\\n\\midrule\n$\\mathcal{M}$ & Language model \\\\\n$x$ & Input instance \\\\\n$y_i$ & $i$-th stochastic sample \\\\\n$N$ & Number of samples \\\\\n$T$ & Sampling temperature \\\\\n$c(\\cdot)$ & Confidence signal \\\\\nSJ & Soft Jaccard similarity \\\\\nFK & Fleiss' $\\kappa$ \\\\\nEM & Exact-match voting rate \\\\\nVC ($c_{\\mathrm{vc}}$) & Entity voting confidence \\\\\nLP ($c_{\\mathrm{lp}}$) & Log-probability (mean token log-likelihood) \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Notation used throughout the paper.}\n\\label{tab:notation}\n\\end{table}\n\n\\section{Robustness Analysis}\\label{app:robustness}\n\nWe exclude instances with empty gold annotations from all correlation analyses (CoNLL: 697/3{,}453 instances, 20.2\\%; SciERC: 22/551, 4.0\\%).\nFor these instances, F1 is trivially zero regardless of prediction quality, and consistency signals reflect agreement on the empty set rather than extraction quality---including them inflates or deflates Spearman $\\rho$ depending on signal behavior at the boundary.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Signal robustness across configurations (Spearman $\\rho$). Top: temperature on Qwen SciERC. Middle: sample size on Qwen SciERC. Bottom: transfer across model families (both 8B) (LLaMA CoNLL $N{=}16$, 3-seed mean $\\pm\\sigma$). $^\\dagger$Mean over 3 seeds ($\\sigma{=}0.013$; individual: 0.398, 0.423, 0.410). $\\sigma$ computed as sample standard deviation.}\n\\label{tab:robustness}\n\\begin{tabular}{llcc}\n\\toprule\n& & NER $\\rho$ & RE $\\rho$ \\\\\n\\midrule\n\\multicolumn{4}{l}{\\textit{Temperature} (Qwen SciERC, $N{=}8$)} \\\\\n\\quad SJ & $T{=}0.7$ & 0.388 & 0.234 \\\\\n\\quad SJ & $T{=}1.0$ & 0.360 & 0.250 \\\\\n\\quad FK & $T{=}0.7$ & 0.321 & 0.184 \\\\\n\\quad FK & $T{=}1.0$ & 0.267 & 0.275 \\\\\n\\midrule\n\\multicolumn{4}{l}{\\textit{Sample size} (Qwen SciERC, $T{=}1.0$)} \\\\\n\\quad SJ & $N{=}8$  & 0.360 & 0.250 \\\\\n\\quad SJ & $N{=}16$ & 0.411$^\\dagger$ & 0.281 \\\\\n\\quad FK & $N{=}8$  & 0.267 & 0.275 \\\\\n\\quad FK & $N{=}16$ & 0.283 & 0.279 \\\\\n\\midrule\n\\multicolumn{4}{l}{\\textit{Across model families} (LLaMA CoNLL, $N{=}16$, 3 seeds)} \\\\\n\\quad SJ &  & $0.474{\\pm}0.009$ & --- \\\\\n\\quad FK &  & $0.467{\\pm}0.009$ & --- \\\\\n\\quad EM &  & $0.473{\\pm}0.010$ & --- \\\\\n\\quad VC &  & $0.470{\\pm}0.006$ & --- \\\\\n\\quad LP &  & $0.311{\\pm}0.003$ & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{fig_temperature_robustness}\n\\caption{Temperature robustness on SciERC ($N{=}8$). Top: NER; bottom: RE. SJ maintains stable $\\rho$ across $T{=}0.7$ and $T{=}1.0$, while FK shows mixed sensitivity. LP $T{=}0.7$ data unavailable.}\n\\label{fig:temperature_robustness}\n\\end{figure}\n\n\\paragraph{Temperature sensitivity.}\nSJ NER $\\rho$ shifts from 0.388 ($T{=}0.7$) to 0.360 ($T{=}1.0$), a difference of 0.028 whose bootstrap confidence interval includes zero.\nFK shows mixed behavior: NER $\\rho$ drops by 0.054, while RE $\\rho$ increases by 0.091, likely reflecting reduced diversity at lower temperature interacting differently across tasks.\nAcross all comparisons, the SJ--FK relative ordering is preserved at both temperatures on NER (0.388 vs.\\ 0.321 at $T{=}0.7$; 0.360 vs.\\ 0.267 at $T{=}1.0$), indicating a stable signal hierarchy despite numerically small temperature effects.\n\n\\paragraph{Sample size scaling.}\nIncreasing from $N{=}8$ to $N{=}16$ improves SJ on Qwen SciERC NER: $\\rho$ rises from 0.360 to $0.411{\\pm}0.010$ (three seeds: 0.398, 0.423, 0.410), a gain of $+0.047$.\nThe magnitude of $N$-scaling gains is setting-dependent---LLaMA SciERC NER yields $+0.016$ and Qwen CoNLL NER $+0.014$---though the direction is consistently positive.\nLLaMA CoNLL exhibits the most uniform scaling: all four consistency signals gain $\\Delta\\rho{\\approx}{+}0.042$ (range: $+0.039$ to $+0.044$) while LP gains only $+0.004$ (Table~\\ref{tab:quality_estimation}).\nFK $N$-scaling is seed-dependent: Qwen SciERC gains range from $+0.005$ to $+0.023$ across seeds (mean $+0.016$), while LLaMA CoNLL yields $+0.039$ (3-seed mean); individual seed FK shifts vary substantially under the unified pipeline, so this should not be interpreted as a robust trend.\nVC $N$-scaling is consistently positive ($+0.005$ on Qwen CoNLL, $+0.018$ on LLaMA SciERC, $+0.030$ on Qwen SciERC), while LP is approximately $N$-invariant ($\\Delta{\\leq}0.034$).\nSJ, EM, and VC scale consistently across all tested settings; only FK shows seed-dependent variation that does not constitute a reliable trend, suggesting that structural and binary-agreement signals are the most robust to $N$.\nAt $N{=}16$, SJ converges to comparable NER performance with VC ($\\Delta{=}0.002$) while exhibiting lower cross-seed variance ($\\sigma{=}0.010$ vs.\\ $0.026$), making it a more stable alternative at higher sample sizes.\n\n\\paragraph{Transfer across model families.}\nLLaMA-3.1-8B-Instruct shows a similar SJ--FK ordering on SciERC NER (SJ $\\rho{=}0.325{\\pm}0.021$, FK $\\rho{=}0.256{\\pm}0.024$, $\\Delta\\rho{=}0.069$; permutation $p{=}0.06$, borderline).\nOn CoNLL, the gap across model families is minimal (Table~\\ref{tab:quality_estimation}): SJ achieves $\\rho{=}0.431$ (LLaMA) vs.\\ 0.436 (Qwen), $\\Delta{=}0.005$.\nAt $N{=}16$, the structural-over-LP advantage holds across all four tested NER settings: Qwen SciERC (VC $\\rho{=}0.409$ vs.\\ LP 0.239, $\\Delta{=}{+}0.170$), Qwen CoNLL (EM $\\rho{=}0.463$ vs.\\ LP 0.328, $\\Delta{=}{+}0.135$),\\footnote{Qwen CoNLL $N{=}16$ was not recomputed under the unified pipeline; LP $\\rho{=}0.328$ may differ slightly from the registry value (0.315) due to instance filtering.} LLaMA SciERC (VC $\\rho{=}0.452$ vs.\\ LP 0.277, $\\Delta{=}{+}0.175$), and LLaMA CoNLL 3-seed (SJ $\\rho{=}0.474{\\pm}0.009$ vs.\\ LP $0.311{\\pm}0.003$, $\\Delta{=}{+}0.163$).\n\n\\section{Calibration Analysis}\\label{app:calibration}\n\n\\begin{figure*}[t]\n\\centering\n\\includegraphics[width=\\textwidth]{fig_reliability}\n\\caption{Reliability diagrams on SciERC ($N{=}8$, $T{=}1.0$). Top: mean F1 vs.\\ binned confidence; bottom: instance counts per bin. Left: NER; right: RE. NER signals are reasonably well-calibrated (calibration ECE 0.069--0.096), while RE shows greater miscalibration (ECE 0.109--0.339), reflecting the difficulty of calibrating confidence for compound extraction tasks.}\n\\label{fig:reliability}\n\\end{figure*}\n\nReliability diagrams use 10 equal-width bins.\nNER signals are reasonably well-calibrated (calibration ECE 0.069--0.096), while RE exhibits greater miscalibration (ECE 0.109--0.339), indicating that translating consistency scores into calibrated confidence estimates is feasible for NER but remains challenging for compound extraction tasks.\n\n\\section{Additional Analyses}\\label{app:additional}\n\n\\paragraph{Per-relation diagnostic.}\nRE signal degradation is relation-specific.\n\\textsc{Feature-Of} has near-zero correlation ($\\rho{=}0.004$), while \\textsc{Hyponym-Of} achieves $\\rho{=}0.646$.\nThe primary bottleneck is entity span errors, which account for 55.5\\% of RE false negatives---a prerequisite failure that consistency signals cannot detect, as they measure agreement among equally incorrect extractions.\nWe note that RE analysis relies on a single dataset (SciERC); generalization to other RE benchmarks remains to be validated.\n\n\\paragraph{Capability stratification.}\nFor NER, SJ effectiveness scales with structural complexity: on SciERC instances with 6+ entities, $\\rho{=}0.547$, compared to $\\rho{=}0.415$ for 1--2 entities.\nThe SJ advantage over LP remains stable across sentence-length quartiles ($\\Delta\\rho{\\approx}0.08$--$0.20$).\nFor RE, SJ $\\rho$ increases monotonically with sentence length (Q1: 0.110 $\\to$ Q4: 0.473; Fisher $z$-test $p{=}0.004$), indicating that longer, more relation-dense sentences provide richer structure for consistency-based estimation.\nBoth proxies are weakly correlated with F1 ($|r|{<}0.15$), confirming they capture input complexity rather than directly predicting output quality; however, entity count and sentence length are themselves moderately correlated ($\\rho{=}0.650$), so they reflect overlapping rather than independent complexity dimensions.\nFor RE, entity count and relation count are strongly correlated ($\\rho{=}0.769$) and thus reflect a single structural complexity dimension rather than independent axes.\nOn the high-complexity RE subset ($n{=}81$, high relation count), signals improve substantially: VC reaches $\\rho{=}0.630$, LP $\\rho{=}0.554$, and SJ $\\rho{=}0.502$---all far above the full-set levels.\nRicher relational structure provides more signal for consistency-based estimation, complementing the task-level boundary established by WNUT-17: structural signals are most effective within a ``sweet spot'' of sufficient model capability and sufficient output complexity.\n\n\\paragraph{Length vs.\\ log-probability.}\nFigure~\\ref{fig:length_logprob_scatter} shows that mean log-probability is weakly positively correlated with output length (NER: $\\rho{=}0.386$, $n{=}4{,}232$; RE: $\\rho{=}0.326$, $n{=}3{,}176$), ruling out length-penalty confounding as an explanation for LP's selection failure: longer outputs receive \\textit{higher}, not lower, token-averaged log-probability under constrained decoding.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{fig_length_logprob_scatter}\n\\caption{Output length vs.\\ mean log-probability on SciERC ($N{=}8$, $T{=}1.0$). Positive correlations (NER: $\\rho{=}0.386$; RE: $\\rho{=}0.326$) rule out length-penalty confounding.}\n\\label{fig:length_logprob_scatter}\n\\end{figure}\n\n\\paragraph{Evaluation circularity and LOO-SJ equivalence.}\nConsensus-proximity selection chooses $\\hat{y} = \\arg\\max_{y_i} \\sum_{j \\neq i} \\text{SJ}(y_i, y_j)$.\nLeave-one-out SJ (LOO-SJ) for sample $y_i$ is $\\text{LOO-SJ}_i = \\frac{1}{N-1}\\sum_{j \\neq i} \\text{SJ}(y_i, y_j)$.\nSince the $\\frac{1}{N-1}$ constant is shared across all candidates within an instance, $\\arg\\max_{y_i} \\text{LOO-SJ}_i = \\arg\\max_{y_i} \\sum_{j \\neq i} \\text{SJ}(y_i, y_j)$, making the two selection rules equivalent.\nStandard (non-LOO) SJ adds the self-comparison term $\\text{SJ}(y_i, y_i) = 1$ to each candidate, which is constant and thus does not affect ranking.\nEmpirically, LOO-SJ yields $\\Delta\\rho{=}{-}0.014$ relative to standard SJ (a correlation-level difference), with a maximum per-instance score difference of $3.1{\\times}10^{-4}$ (negligible at the individual prediction level).\nEvaluation circularity is negligible.\n\n\\paragraph{Conditional filtering details.}\nOn LLaMA conditional RE (non-zero F1 instances), SJ recovers to $\\rho{=}0.405$ while FK drops to $\\rho{=}0.259$, consistent with the NER structural advantage; on full-set RE, however, the SJ--FK difference is non-significant ($\\Delta\\rho{=}{-}0.005$, $p{=}0.53$; preliminary).\nAt $N{=}16$, the divergence persists: SJ maintains $\\rho{=}0.308$ on conditional RE while LP drops to $\\rho{=}{-}0.026$.\nEM ranks first across all four tested conditional configurations---SciERC NER ($\\rho{=}0.360$), CoNLL Qwen $N{=}16$ ($\\rho{=}0.466$), CoNLL LLaMA 3-seed ($\\rho{=}0.462$), and SciERC RE ($\\rho{=}0.417$)---despite full-set rankings ranging from \\#1 (CoNLL Qwen) to \\#5 (SciERC RE).\nOn the full set, EM is diluted by trivial agreement: instances where all $N$ samples produce identical (possibly incorrect) outputs receive EM${=}1$ regardless of quality, compressing the signal's dynamic range.\nOn the conditional set---where the model demonstrably produces varied outputs---exact agreement becomes the strongest quality signal.\nThe margin over SJ is largest on RE ($\\Delta\\rho{=}{+}0.171$), where compound extraction decisions amplify output variability, and smallest on CoNLL LLaMA ($\\Delta\\rho{=}{+}0.002$), where all signals converge near $\\rho{\\approx}0.46$.\n\n\\paragraph{WNUT-17 full signal analysis.}\nTable~\\ref{tab:wnut} reports all five signals on WNUT-17.\nVC achieves $\\rho{=}0.724$ (AUROC${=}0.913$) on the full set, but conditional analysis (non-zero F1 instances) reveals this is entirely driven by the zero/non-zero boundary: conditional $\\rho{=}0.038$ ($p{=}0.49$).\nLP shows the reverse pattern: full-set $\\rho{=}{-}0.410$ but conditional $\\rho{=}0.350$, the highest among all signals on the conditional set.\nThis inversion confirms that full-set correlations on high-failure-rate datasets conflate binary success prediction with quality gradation.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Quality estimation on WNUT-17 (Qwen, $N{=}16$, $T{=}1.0$, $n{=}689$ after filtering gold-empty instances). Cond: non-zero F1 instances ($n{=}334$). LP exhibits strong negative full-set $\\rho$; its conditional $\\rho$ reverses to the highest among all signals, confirming that full-set correlations on high-failure-rate datasets conflate binary success prediction with quality gradation.}\n\\label{tab:wnut}\n\\begin{tabular}{lccccc}\n\\toprule\nSignal & $\\rho$ & $p$ & AUROC & Cond.\\ $\\rho$ & Cond.\\ $p$ \\\\\n\\midrule\nVC      & .724 & ${<}$1e-112 & .913 & .038 & .487 \\\\\nFK      & .125 & .001 & .555 & .169 & .002 \\\\\nSJ      & .089 & .020 & .517 & .288 & ${<}$1e-7 \\\\\nEM      & .050 & .194 & .487 & .333 & ${<}$1e-9 \\\\\nLP & $-$.410 & ${<}$1e-28 & .219 & .350 & ${<}$1e-10 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Cross-configuration selection analysis.}\nTable~\\ref{tab:cross_selection} extends the selection analysis to four additional configurations.\nOn LLaMA SciERC, where output diversity remains substantial (18\\% identical outputs, 39\\% unique), LP achieves the highest selection F1 (0.652) at $N{=}8$ but still falls within bootstrap noise of greedy (0.646), replicating the gap observed on Qwen SciERC (Table~\\ref{tab:selection}).\nOn CoNLL, 57--88\\% of instances produce identical outputs across all $N$ samples, reflecting a ceiling effect (greedy F1 ${\\approx}$0.91--0.92) rather than signal failure; selection analysis on these configurations is uninformative because there is little per-sample variance for any signal to exploit.\n\n\\begin{table*}[t]\n\\centering\n\\small\n\\caption{Best-of-$N$ selection F1 (macro, instance-averaged) across configurations ($T{=}1.0$). Best non-oracle signal per row in \\textbf{bold}. At $N{=}8$, no signal significantly outperforms greedy in any configuration. At $N{=}16$ on LLaMA CoNLL, VC achieves small but significant gains ($+0.28$~pp, $p{<}0.03$; see text below). CoNLL shows especially tight clustering where greedy already exceeds 0.90.}\n\\label{tab:cross_selection}\n\\begin{tabular}{llccccccc}\n\\toprule\nConfig & $n$ & Greedy & Oracle & SJ & FK & EM & LP & VC \\\\\n\\midrule\nLLaMA/SciERC $N{=}8$ & 529 & .646 & .778 & .643 & .639 & .634 & \\textbf{.652} & .633 \\\\\nLLaMA/SciERC $N{=}16$ & 529 & .645 & .806 & \\textbf{.649} & \\textbf{.649} & .640 & .646 & .640 \\\\\nQwen/CoNLL $N{=}8$ & 2{,}756 & .908 & .948 & \\textbf{.899} & .893 & .898 & .897 & .895 \\\\\nLLaMA/CoNLL $N{=}8$ & 2{,}756 & .924 & .943 & .924 & \\textbf{.925} & .924 & .924 & .923 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table*}\n\n\\paragraph{Diminishing returns of $N$-scaling.}\nOur $N{=}8$ and $N{=}16$ comparisons (Table~\\ref{tab:robustness}) characterize the marginal value of additional samples for test-time scaling \\cite{brown2024monkeys, snell2025scaling}.\nFor quality estimation, structural signals benefit consistently but sublinearly: SJ $\\rho$ improves by $+0.047$ (Qwen SciERC, 3-seed mean) and $+0.032$ (LLaMA CoNLL, 3-seed mean) when doubling from $N{=}8$ to $N{=}16$, while log-probability is approximately $N$-invariant ($\\Delta\\rho{\\leq}0.021$).\nStructural signals leverage $\\binom{N}{2}$ pairwise comparisons (28 pairs at $N{=}8$, 120 at $N{=}16$), but the $\\rho$ improvement is far less than proportional, indicating diminishing information per additional comparison.\nThis asymmetry gives structural signals a relative advantage in the compute-constrained regime: at $N{=}8$, SJ already achieves $\\rho{=}0.431$ on LLaMA CoNLL (vs.\\ LP $\\rho{=}0.307$, $\\Delta{=}{+}0.124$), and the gap \\textit{widens} at $N{=}16$ ($\\Delta{=}{+}0.163$) because structural signals continue to benefit from additional pairwise evidence while LP does not.\nFor sample selection, additional samples increase the oracle upper bound---more draws raise the probability of a high-quality candidate---but signal-based selection remains flat because the selector's inability to identify the best candidate is a granularity limitation, not a sample size limitation.\nThe practical implication is that $N{=}8$ captures most of the achievable quality estimation benefit; further scaling widens rather than closes the correlation-selection gap absent stronger per-sample selectors.\n\n\\paragraph{$N{=}16$ CoNLL selection: small but significant.}\nWhile quality estimation benefits sublinearly from $N$-scaling, selection behavior at $N{=}16$ reveals a nuanced exception on LLaMA CoNLL.\nVC achieves the largest gain over greedy ($+0.28$~pp, $p{=}0.003$--$0.027$ across 3 seeds, all significant), with SJ, FK, and EM at $+0.22$--$0.23$~pp and LP at $+0.12$~pp (2/3 seeds significant).\nThese gains are statistically significant but practically minimal: oracle headroom at $N{=}16$ is only 2.5~pp, so VC captures approximately 10\\% of the available headroom.\nThis reinforces the primary finding: even under the most favorable conditions---high baseline performance, more candidates, and aggregated multi-seed evidence---signal-based selection recovers only a fraction of the oracle headroom available.\n\n\\section{Bootstrap CI for Signal Comparisons}\\label{app:bootstrap_signal}\n\nTable~\\ref{tab:bootstrap_signal_ci} reports bootstrap confidence intervals for individual signal $\\rho$ and pairwise $\\Delta\\rho$ on SciERC NER ($N{=}8$, $n{=}529$, $B{=}10{,}000$, seed${=}42$).\nThe SJ--LP gap ($\\Delta\\rho{=}{+}0.155$) is clearly significant, confirming the structural advantage reported in \\S\\ref{sec:qe_results}.\nThe VC--SJ gap ($\\Delta\\rho{=}{+}0.019$) is not significant, indicating that these two structural signals perform comparably.\nThe SJ--EM gap ($\\Delta\\rho{=}{+}0.065$) is borderline significant, with the CI lower bound at $+0.003$ and upper bound at $+0.130$.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Bootstrap 95\\% CIs for signal $\\rho$ on SciERC NER ($N{=}8$, $n{=}529$, $B{=}10{,}000$, seed${=}42$). Top: individual signals. Bottom: pairwise $\\Delta\\rho$; ``Sig.'' indicates whether the 95\\% CI excludes zero.}\n\\label{tab:bootstrap_signal_ci}\n\\begin{tabular}{lcc}\n\\toprule\nSignal & $\\rho$ & 95\\% CI \\\\\n\\midrule\nVC & +0.379 & [+0.299, +0.456] \\\\\nSJ & +0.360 & [+0.277, +0.437] \\\\\nEM & +0.295 & [+0.212, +0.371] \\\\\nFK & +0.267 & [+0.176, +0.354] \\\\\nLP & +0.205 & [+0.119, +0.291] \\\\\n\\bottomrule\n\\end{tabular}\n\n\\vspace{0.5em}\n\n\\begin{tabular}{lccc}\n\\toprule\nComparison & $\\Delta\\rho$ & 95\\% CI & Sig. \\\\\n\\midrule\nSJ $-$ LP & +0.155 & [+0.074, +0.234] & Yes \\\\\nVC $-$ SJ & +0.019 & [$-$0.033, +0.073] & No \\\\\nSJ $-$ EM & +0.065 & [+0.003, +0.130] & Marginal$^\\dagger$ \\\\\n\\bottomrule\n\\end{tabular}\n\n\\smallskip\n{\\footnotesize $^\\dagger$Marginally significant without multiple comparison correction; would not survive Bonferroni correction for 10 pairwise comparisons ($\\alpha_{\\text{adj}}{=}0.005$).}\n\\end{table}\n\nAt $N{=}16$ ($B{=}10{,}000$, permutation test), the structural advantage extends to FK comparisons.\nOn SciERC NER ($n{=}529$), SJ--FK ($\\Delta\\rho{=}0.147$--$0.160$, all $p{\\leq}0.002$) and VC--FK ($\\Delta\\rho{=}0.138$--$0.188$, all $p{\\leq}0.003$) are clearly significant across all three seeds; EM--FK is seed-dependent ($\\Delta\\rho{=}0.054$--$0.093$, $p{=}0.048$--$0.15$).\nOn CoNLL ($n{=}2{,}756$), all signals significantly outperform FK: EM $\\Delta\\rho{=}0.071$ ($p{<}0.001$), SJ $\\Delta\\rho{=}0.056$ ($p{<}0.001$), VC $\\Delta\\rho{=}0.022$ ($p{=}0.040$).\n\n\\section{Diversity and Selection Analysis}\\label{app:diversity}\n\n\\paragraph{Output diversity quantification.}\nTable~\\ref{tab:diversity} summarizes output diversity across configurations.\nOn SciERC, output diversity is substantial: Qwen produces 43\\% unique outputs per instance (mean 3.5 distinct out of $N{=}8$), with per-sample F1 standard deviation of 0.144 and mean pairwise SJ of 0.703.\nLLaMA shows similar diversity (39\\% unique, F1 std 0.11).\nOn CoNLL, diversity collapses: 57\\% (Qwen) to 88\\% (LLaMA) of instances produce identical outputs across all $N$ samples, reflecting a ceiling effect where greedy F1 already exceeds 0.90.\nWNUT-17 shows 55\\% identical outputs, driven by the 52\\% zero-F1 rate.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Output diversity across configurations ($N{=}8$, $T{=}1.0$). ``Identical'' = fraction of instances with all $N$ outputs identical. ``Unique'' = mean fraction of distinct outputs per instance.}\n\\label{tab:diversity}\n\\begin{tabular}{lcc}\n\\toprule\nConfig & Identical & Unique \\\\\n\\midrule\nQwen/SciERC & 11\\% & 43\\% \\\\\nLLaMA/SciERC & 18\\% & 39\\% \\\\\nQwen/CoNLL & 57\\% & --- \\\\\nLLaMA/CoNLL & 88\\% & --- \\\\\nWNUT-17 & 55\\% & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Oracle-improvable fraction.}\nAcross SciERC configurations, 39--42\\% of instances contain at least one sample with F1 exceeding greedy\\footnote{Oracle-improvable and diversity-stratified analyses use $n{=}529$ (excluding instances with empty gold annotations; see \\S\\ref{sec:evaluation}); the diversity quantification in Table~\\ref{tab:diversity} uses the full test set.}: Qwen NER 42.0\\% (222/529, mean headroom $+$31.9~pp among improvable instances), Qwen RE 41.3\\% (164/397, $+$45.3~pp), LLaMA NER 39.3\\% (208/529, $+$33.7~pp).\nOn CoNLL, only 4--9\\% of instances are improvable, confirming the ceiling effect.\n\n\\paragraph{Diversity-stratified selection gap.}\nOn the 44\\% of Qwen SciERC instances with high diversity (${\\geq}4$ unique outputs among 8 samples, $n{=}232$), oracle headroom reaches $+$16.3~pp, yet all consistency-based signals (SJ, FK, EM, VC) select at or below greedy, and LP---the only per-sample signal---achieves merely $+$0.8~pp.\nLLaMA replicates this pattern: on its high-diversity subset ($n{=}186$), oracle headroom reaches $+$20.1~pp while consistency signals remain at or below greedy and LP captures only $+$2.0~pp.\nThis rules out insufficient diversity as an explanation for the correlation-selection gap.\n\n\\paragraph{TOST equivalence testing.}\nThe primary evidence against selection gains comes from effect sizes and confidence intervals: Cohen's $d{=}0.038$ for the best signal (NER LP) and bootstrap 95\\% CI [$-$3.0, $+$4.2]~pp spanning zero.\nTable~\\ref{tab:tost} supplements this with two one-sided tests (TOST), testing whether each signal's selection F1 is equivalent to greedy within a bound $\\delta$.\nThe $\\delta$ values are contextualized against oracle headroom (12--18~pp): $\\delta{=}5$~pp corresponds to forgoing 28--38\\% of the available headroom, $\\delta{=}3$~pp forgoing 17--23\\%, and $\\delta{=}2$~pp less than 15\\%.\nThese proportions use the same test data that defines the headroom and should be interpreted as context for practical relevance rather than independent calibration.\nThe breakpoint $\\delta^*$---the minimum equivalence margin at which each signal passes TOST---ranges from approximately 1.3~pp (SJ, ${\\sim}$10\\% of oracle headroom) to 3.4~pp (FK, ${\\sim}$26\\%) on NER, and from approximately 2.9~pp (LP, ${\\sim}$16\\%) to 6.5~pp (VC, ${\\sim}$36\\%) on RE.\nOn NER ($n{=}529$), at $\\delta{=}{\\pm}2$~pp, SJ and LP are confirmed equivalent to greedy (TOST $p{<}0.05$); at $\\delta{=}{\\pm}3$~pp, four of five signals pass; at $\\delta{=}{\\pm}5$~pp, all five pass.\nOn RE ($n{=}397$, preliminary), EM and VC fail equivalence even at $\\delta{=}{\\pm}5$~pp due to systematic underperformance ($\\Delta{=}{-}3.2$~pp and $-4.5$~pp respectively).\nThe effect sizes are negligible ($d{=}0.038$) and confidence intervals span zero, with TOST confirming equivalence at practically meaningful margins.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{TOST equivalence testing: signals vs.\\ greedy on SciERC ($N{=}8$, $T{=}1.0$). \\checkmark: equivalent at $p{<}0.05$; \\texttimes: not equivalent. $\\Delta$: mean F1 difference (signal $-$ greedy).}\n\\label{tab:tost}\n\\begin{tabular}{l cccc cccc}\n\\toprule\n& \\multicolumn{4}{c}{\\textbf{NER}} & \\multicolumn{4}{c}{\\textbf{RE}} \\\\\n\\cmidrule(lr){2-5} \\cmidrule(lr){6-9}\nSignal & $\\Delta$ & $\\pm$2 & $\\pm$3 & $\\pm$5 & $\\Delta$ & $\\pm$2 & $\\pm$3 & $\\pm$5 \\\\\n\\midrule\nLP & +0.6 & \\checkmark & \\checkmark & \\checkmark & $-$0.9 & \\texttimes & \\checkmark & \\checkmark \\\\\nSJ & +0.1 & \\checkmark & \\checkmark & \\checkmark & $-$1.8 & \\texttimes & \\texttimes & \\checkmark \\\\\nFK & $-$0.5 & \\texttimes & \\checkmark & \\checkmark & $-$1.6 & \\texttimes & \\texttimes & \\checkmark \\\\\nEM & $-$0.8 & \\texttimes & \\checkmark & \\checkmark & $-$3.2 & \\texttimes & \\texttimes & \\texttimes \\\\\nVC & $-$1.0 & \\texttimes & \\texttimes & \\checkmark & $-$4.5 & \\texttimes & \\texttimes & \\texttimes \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{Multi-Seed Stability}\\label{app:multiseed}\n\nTable~\\ref{tab:multiseed} reports quality estimation metrics across three random seeds for both model families on SciERC ($N{=}8$, $T{=}1.0$).\nOn NER, the signal ranking VC${>}$SJ${>}$EM${>}$FK${>}$LP is identical across all six model-seed combinations, with $\\sigma{\\leq}0.025$ for all signals.\nOn RE (Qwen only, preliminary), VC remains the top signal ($\\rho{=}0.309{\\pm}0.024$), but LP rises to \\#2 ($\\rho{=}0.297{\\pm}0.022$), above FK, SJ, and EM---a reversal from the NER ranking that reflects RE's higher sensitivity to per-sample scoring.\nLLaMA absolute values are systematically lower than Qwen on NER, consistent with the directionally-consistent-but-magnitude-dependent characterization in the main text.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Multi-seed quality estimation on SciERC ($N{=}8$, $T{=}1.0$, seeds: 42, 123, 456). NER: both models; RE: Qwen only (preliminary). Signal ranking is stable across seeds ($\\sigma{\\leq}0.025$). $\\sigma$ is population standard deviation over 3 seeds.}\n\\label{tab:multiseed}\n\\begin{tabular}{lccccc}\n\\toprule\n& LP & FK & SJ & VC & EM \\\\\n\\midrule\n\\multicolumn{6}{l}{\\textit{NER Spearman $\\rho$ (mean $\\pm\\sigma$)}} \\\\\nQwen & .217${\\pm}$.013 & .254${\\pm}$.016 & .364${\\pm}$.018 & .386${\\pm}$.019 & .307${\\pm}$.008 \\\\\nLLaMA & .162${\\pm}$.025 & .256${\\pm}$.024 & .325${\\pm}$.021 & .384${\\pm}$.014 & .279${\\pm}$.011 \\\\\n\\midrule\n\\multicolumn{6}{l}{\\textit{RE Spearman $\\rho$ (mean $\\pm\\sigma$, Qwen)}} \\\\\nQwen & .297${\\pm}$.022 & .290${\\pm}$.012 & .249${\\pm}$.002 & .309${\\pm}$.024 & .135${\\pm}$.016 \\\\\n\\midrule\n\\multicolumn{6}{l}{\\textit{NER AUROC (mean $\\pm\\sigma$)}} \\\\\nQwen & .613${\\pm}$.002 & .618${\\pm}$.009 & .684${\\pm}$.009 & .697${\\pm}$.010 & .661${\\pm}$.010 \\\\\nLLaMA & .577${\\pm}$.007 & .616${\\pm}$.011 & .655${\\pm}$.010 & .689${\\pm}$.005 & .636${\\pm}$.006 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{Training Configuration}\\label{app:training}\n\nBoth models are fine-tuned with identical hyperparameters (Table~\\ref{tab:training}) to ensure comparisons across model families reflect model differences rather than training confounds.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Training configuration. Both Qwen3-8B and LLaMA-3.1-8B-Instruct use identical settings unless noted.}\n\\label{tab:training}\n\\begin{tabular}{ll}\n\\toprule\nParameter & Value \\\\\n\\midrule\nLoRA rank / $\\alpha$ & 32 / 64 \\\\\nLoRA target & All linear modules \\\\\nLoRA dropout & 0 \\\\\nOptimizer & AdamW \\\\\nLearning rate & 2e-4, cosine schedule \\\\\nWarmup ratio & 0.1 \\\\\nEffective batch size & 16 (2 $\\times$ grad.\\ accum.\\ 8) \\\\\nEpochs & 5 \\\\\nMax sequence length & 2048 \\\\\nPrecision & bf16 \\\\\nGradient checkpointing & Enabled \\\\\nMax gradient norm & 1.0 \\\\\nTraining seed & 42 \\\\\nFramework & LLaMA Factory \\\\\n\\midrule\n\\multicolumn{2}{l}{\\textit{Dataset-specific}} \\\\\nSciERC split & 1861 / 275 / 551 \\\\\nCoNLL / WNUT & +\\,load\\_best\\_model\\_at\\_end, \\\\\n& eval\\_steps${=}$200, save\\_limit${=}$5 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Prompt template.}\nFor NER, we use a structured prompt:\n\\begin{quote}\n\\small\n\\texttt{System:} You are an expert in Named Entity Recognition.\\\\\n\\texttt{User:} Extract all named entities from the following text. Output as JSON.\\\\\nText: \\texttt{\\{input\\_text\\}}\\\\\nEntity types: \\texttt{\\{schema\\_types\\}}\n\\end{quote}\nRE follows the same structure with ``Relation Extraction'' and relation type lists substituted accordingly.\n\n\\paragraph{Constrained decoding.}\nInference uses vLLM with XGrammar-based JSON schema enforcement \\cite{willard2023guided}, which constrains outputs to valid entity/relation structures matching the target schema.\nThis eliminates format errors but may compress per-sample diversity by restricting the output space.\\footnote{SciERC training used \\texttt{enable\\_thinking=True} (LLaMA Factory 0.9.4 default), injecting empty \\texttt{&lt;think>&lt;/think>} blocks (4--5 tokens) into each training response with loss computation; CoNLL and WNUT explicitly set \\texttt{enable\\_thinking=False}. Constrained decoding at inference time enforces JSON-only output, suppressing thinking tokens. See \\S\\ref{sec:setup} and Limitations for discussion of this confound.}\n\n\\section{Log-Probability Score Compression}\\label{app:logprob_ties}\n\nUnder constrained decoding, log-probability scores are severely compressed within instances, limiting per-sample discrimination (Table~\\ref{tab:logprob_ties}, Figure~\\ref{fig:lp_range_cdf}).\nThe median within-instance LP range is only 0.041 nats---below the $\\varepsilon{=}0.05$ threshold used throughout, providing data-driven justification for this cutoff rather than an arbitrary choice.\nAt $\\varepsilon{=}0.05$, 60.3\\% of instances ($n{=}529$, excluding empty gold annotations) have a within-sample range below the threshold, and 75\\% of pairwise comparisons are effective ties ($|\\Delta|{<}0.026$).\nThe CDF rises smoothly with no cliff or discontinuity (Figure~\\ref{fig:lp_range_cdf}), confirming that compression is a pervasive regime rather than a bimodal split.\nFor comparison, SJ has only 12.5\\% tied instances at the same threshold---SJ's advantage over LP for selection is one of score resolution, not information content.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{fig_lp_range_cdf}\n\\caption{CDF of within-instance LP range on SciERC NER ($N{=}8$, $n{=}529$). The median LP range is 0.041 nats (dashed line), below $\\varepsilon{=}0.05$. The smooth CDF confirms compression is pervasive, not bimodal.}\n\\label{fig:lp_range_cdf}\n\\end{figure}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Log-probability score compression on SciERC NER ($N{=}8$, $n{=}529$). ``Tied'' = fraction of instances where within-instance LP range ${<}\\varepsilon$.}\n\\label{tab:logprob_ties}\n\\begin{tabular}{lc}\n\\toprule\n$\\varepsilon$ threshold & Tied instances (\\%) \\\\\n\\midrule\n0.01 & 1.1\\% \\\\\n0.05 & 60.3\\% \\\\\n0.1  & ${\\sim}$84\\% \\\\\n0.5  & ${\\sim}$99\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Non-tied subset.}\nAmong instances with LP range ${\\geq}0.05$ ($n{=}210$, 40\\% of total), log-probability selection \\textit{significantly} outperforms greedy ($+2.9$~pp F1, $p{=}0.01$), and within-instance $\\rho(\\text{LP}, \\text{F1})$ rises from 0.08 (tied subset) to 0.39 (non-tied subset).\nAs a continuous complement to the binary tied/non-tied analysis, pooled within-instance $\\rho(\\text{LP}, \\text{F1}){=}0.248$ across all instances confirms weak but positive per-sample signal; however, only 21.6\\% of instances achieve $p{<}0.05$ significance, and $\\rho(\\text{LP range}, \\text{F1 range}){=}0.328$ shows that instances with more LP spread also exhibit more F1 variability---LP carries information but compression limits its exploitation.\nA free-form NER decoding ablation (Appendix~\\ref{app:freeform_ablation}) confirms this compression persists without constrained decoding.\n\n\\section{RE Conditional Selection}\\label{app:re_conditional_selection}\n\nTable~\\ref{tab:re_cond_selection} extends the selection analysis to the RE non-zero F1 subset.\nOf $n{=}397$ RE instances, 238 (60\\%) have non-zero F1 and 159 (40\\%) have zero F1.\nAll five signals underperform greedy on both subsets.\nOn the non-zero subset, selection performance is \\textit{worse} than on the full set (e.g., VC: $-10.0$~pp on non-zero vs.\\ $-4.5$~pp on full set), because greedy is already strong on non-zero instances (F1${=}0.674$) and signals actively select inferior samples.\nOracle headroom exists (0.757 vs.\\ 0.674) but no signal exploits it, ruling out the 40\\% zero-F1 floor effect as the explanation for RE selection failure.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{RE selection F1 (macro, instance-averaged) on SciERC ($N{=}8$, $T{=}1.0$). Full set ($n{=}397$) and non-zero F1 subset ($n{=}238$). No signal outperforms greedy on either subset.}\n\\label{tab:re_cond_selection}\n\\begin{tabular}{lcc}\n\\toprule\nMethod & Full ($n{=}397$) & Non-zero ($n{=}238$) \\\\\n\\midrule\nOracle & 0.585 & 0.757 \\\\\n\\midrule\nLP & 0.395 & 0.600 \\\\\nSJ & 0.386 & 0.604 \\\\\nEM & 0.372 & 0.583 \\\\\nVC & 0.359 & 0.574 \\\\\n\\midrule\nGreedy & 0.404 & 0.674 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{RE $N{=}16$ Selection Analysis}\\label{app:re_n16_selection}\n\nTable~\\ref{tab:re_n16_selection} extends the selection analysis to RE at $N{=}16$ with 3-seed statistics.\nAll four consistency signals underperform greedy, with EM showing the largest deficit ($\\Delta{=}{-}1.5$~pp, Fisher $p{>}0.99$).\nLP is the only positive signal ($\\Delta{=}{+}0.7$~pp, Fisher $p{=}0.058$), driven primarily by seed~456 ($\\Delta{=}{+}1.5$~pp, $p{=}0.026$); the remaining seeds show smaller effects ($+0.1$ and $+0.6$~pp, $p{>}0.20$).\nEven the most favorable seed captures only ${\\sim}9\\%$ of the 17.1~pp oracle headroom.\nThis cross-task consistency---LP as the only viable selection signal on both NER and RE---reinforces the structural limitation of instance-level signals for candidate ranking.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{RE best-of-$N$ selection F1 (macro, instance-averaged) on SciERC ($N{=}16$, $T{=}1.0$, 3-seed mean${\\pm}\\sigma$, $n{=}551$). Fisher combined $p$ vs.\\ greedy. LP is the only signal with positive $\\Delta$. $\\sigma$ is population standard deviation over 3 seeds.}\n\\label{tab:re_n16_selection}\n\\begin{tabular}{lccc}\n\\toprule\nMethod & F1 & $\\Delta$ (pp) & $p$(Fisher) \\\\\n\\midrule\nOracle & $.463{\\pm}.006$ & $+$17.1 & --- \\\\\n\\midrule\nLP & $\\mathbf{.299}{\\pm}.007$ & $+$0.7 & .058 \\\\\nVC & $.284{\\pm}.002$ & $-$0.8 & .973 \\\\\nFK & $.283{\\pm}.005$ & $-$0.9 & .985 \\\\\nSJ & $.281{\\pm}.005$ & $-$1.0 & .993 \\\\\nEM & $.277{\\pm}.007$ & $-$1.5 & .999 \\\\\n\\midrule\nGreedy & $.291{\\pm}.000$ & --- & --- \\\\\nRandom & $.262{\\pm}.001$ & $-$2.9 & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{Free-Form Decoding Ablation}\\label{app:freeform_ablation}\n\nTable~\\ref{tab:freeform_ablation} compares constrained and free-form decoding across four dimensions on SciERC ($N{=}8$, $T{=}1.0$, Qwen3-8B).\nFree-form decoding removes grammar constraints entirely; outputs are parsed post-hoc (parse rate 99.95\\%, 4406/4408).\nLP score distributions are nearly identical across regimes (Panel~A: within-instance std ratio $0.97{\\times}$), and NER selection gains remain negligible under both regimes (Panel~B).\nRE LP selection flips positive under free-form decoding ($+1.69$~pp vs.\\ $-0.68$~pp constrained).\nQuality estimation improves modestly for most signals under free-form decoding (Panel~C), with the largest gain for FK ($+0.053$ NER, $+0.039$ RE).\n\n\\begin{table*}[t]\n\\centering\n\\caption{Comparison of constrained vs.\\ free-form decoding on SciERC (Qwen3-8B, $N{=}8$, $T{=}1.0$, seed=42).}\n\\label{tab:freeform_ablation}\n\n\\vspace{2pt}\n{\\small\\textsc{Panel A: Logprob Distribution}}\n\\vspace{2pt}\n\n\\begin{tabular}{lccc}\n\\toprule\nMetric & Constrained & Free-form & $\\Delta$ \\\\\n\\midrule\nMean LP std        & 0.0206 & 0.0199 & $-$0.0007 \\\\\nMean LP range      & 0.0623 & 0.0599 & $-$0.0024 \\\\\nTied fraction ($\\varepsilon{=}0.05$) & 59.7\\% & 57.7\\% & $-$2.0\\,pp \\\\\n\\bottomrule\n\\end{tabular}\n\n\\vspace{8pt}\n\n{\\small\\textsc{Panel B: Selection F1}}\n\\vspace{2pt}\n\n\\begin{tabular}{llccc}\n\\toprule\nTask & Method & Constrained & Free-form & $\\Delta$ \\\\\n\\midrule\n\\multirow{3}{*}{NER}\n  & Greedy        & 0.6182 & 0.6204 & $+$0.0022 \\\\\n  & LP-selected   & 0.6241 & 0.6222 & $-$0.0019 \\\\\n  & Selection gap & $+$0.0059 & $+$0.0018 & $-$0.0041 \\\\\n\\midrule\n\\multirow{3}{*}{RE}\n  & Greedy        & 0.2913 & 0.2880 & $-$0.0033 \\\\\n  & LP-selected   & 0.2845 & 0.3050 & \\textbf{$+$0.0205} \\\\\n  & Selection gap & $-$0.0068 & $+$0.0169 & \\textbf{$+$0.0237} \\\\\n\\bottomrule\n\\end{tabular}\n\n\\vspace{8pt}\n\n{\\small\\textsc{Panel C: QE Signal Quality (Spearman $\\rho$)}}\n\\vspace{2pt}\n\n\\begin{tabular}{l ccc ccc}\n\\toprule\n & \\multicolumn{3}{c}{NER ($n{=}529$)} & \\multicolumn{3}{c}{RE ($n{=}397$)} \\\\\n\\cmidrule(lr){2-4} \\cmidrule(lr){5-7}\nSignal & Constr. & Free & $\\Delta$ & Constr. & Free & $\\Delta$ \\\\\n\\midrule\nSJ & 0.360 & 0.377 & $+$0.018 & 0.250 & 0.273 & $+$0.023 \\\\\nFK & 0.267 & 0.320 & $+$0.053 & 0.275 & 0.315 & $+$0.039 \\\\\nLP & 0.205 & 0.213 & $+$0.008 & 0.266 & 0.304 & $+$0.038 \\\\\nEM & 0.295 & 0.317 & $+$0.023 & 0.134 & 0.137 & $+$0.002 \\\\\nVC & 0.379 & 0.409 & $+$0.030 & 0.350 & 0.323 & $-$0.026 \\\\\n\\bottomrule\n\\end{tabular}\n\n\\vspace{8pt}\n\n{\\small\\textsc{Panel D: Parse Rate (Free-form)}}\n\\vspace{2pt}\n\n\\begin{tabular}{lc}\n\\toprule\nMetric & Value \\\\\n\\midrule\nTotal samples          & 4408 \\\\\nParse rate             & 99.95\\% \\\\\nInstances 8/8 valid    & 549\\,/\\,551 (99.6\\%) \\\\\n\\bottomrule\n\\end{tabular}\n\n\\end{table*}\n\n\\section{LP Selection Failure Stability}\\label{app:lp_failure_stability}\n\nWe analyze RE LP selection failures across three random seeds (constrained decoding, $N{=}8$, $T{=}1.0$, Qwen3-8B) to assess whether failures are systematic or stochastic.\n\n\\paragraph{Pairwise overlap.}\nLP selection failures (instances where LP-selected F1 $<$ greedy F1) show moderate cross-seed stability: the average pairwise Jaccard similarity is 0.42 (range: 0.38--0.46), indicating that failures are partially systematic---driven by instance complexity---but not fully deterministic.\nThe 3-way intersection contains 34 instances (27.9\\% of any-seed failures), confirming a stable failure core.\n\n\\paragraph{Instance complexity drives failure.}\nTable~\\ref{tab:stable_failures} stratifies instances by failure stability.\nStable failures (all 3 seeds) involve more gold relations (2.12 vs.\\ 1.62 for never-fail instances) and higher greedy F1 (0.688 vs.\\ 0.429), indicating that LP mis-selects on instances where the model already performs well---precisely the instances where selection would be most valuable.\nFailure rate increases monotonically with gold relation count: 4.3\\% at 1 relation, 20.7\\% at 3 relations, 26.2\\% at 6 relations.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{RE LP selection failure stability across 3 seeds (SciERC, $N{=}8$). Stable failures concentrate on relation-dense instances with high greedy F1.}\n\\label{tab:stable_failures}\n\\begin{tabular}{lcccc}\n\\toprule\nGroup & $n$ & Gold rels & Greedy F1 & LP $\\Delta$F1 \\\\\n\\midrule\nStable fail (3 seeds) & 34 & 2.12 & 0.688 & $-$0.499 \\\\\nFail 2+ seeds & 26 & 2.46 & 0.774 & $-$0.450 \\\\\nFail 1 seed & 62 & 2.32 & 0.692 & $-$0.239 \\\\\nNever fail & 429 & 1.62 & 0.429 & $+$0.041 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Flip instances.}\nOnly 5 RE instances with gold relations flip from LP failure (constrained) to LP success (free-form), with mean gold relation count 3.67 (well above the population mean of 1.86).\nThese instances show large constrained LP errors ($\\Delta{=}{-}0.430$) that reverse under free-form decoding ($\\Delta{=}{+}0.503$), but their rarity (5/397) confirms that the RE selection flip is driven by aggregate variance reallocation rather than systematic instance-level correction.\n\n\\section{$N$-Scaling Detailed Analysis}\\label{app:n_scaling}\n\nTables~\\ref{tab:n-scaling}--\\ref{tab:sigma-comparison} provide detailed $N$-scaling analysis on Qwen3-8B SciERC with 3-seed statistics.\n\n\\begin{table}[t]\n\\centering\n\\caption{Effect of sample pool size on signal quality (Qwen3-8B, SciERC, 3-seed mean Spearman $\\rho$).}\n\\label{tab:n-scaling}\n\\small\n\\begin{tabular}{l ccc ccc}\n\\toprule\n & \\multicolumn{3}{c}{\\textbf{NER} $\\rho$} & \\multicolumn{3}{c}{\\textbf{RE} $\\rho$} \\\\\n\\cmidrule(lr){2-4} \\cmidrule(lr){5-7}\nSignal & $N\\!=\\!8$ & $N\\!=\\!16$ & $\\Delta$ & $N\\!=\\!8$ & $N\\!=\\!16$ & $\\Delta$ \\\\\n\\midrule\nSJ & 0.3641 & 0.4105 & \\textbf{+0.0464} & 0.2485 & 0.2758 & \\textbf{+0.0273} \\\\\nFK & 0.2536 & 0.2833 & \\textbf{+0.0297} & 0.2903 & 0.2964 & \\textbf{+0.0061} \\\\\nVC & 0.3861 & 0.4092 & \\textbf{+0.0231} & 0.3088 & 0.3738 & \\textbf{+0.0650} \\\\\nLP & 0.2167 & 0.2393 & \\textbf{+0.0226} & 0.2970 & 0.3100 & \\textbf{+0.0130} \\\\\nEM & 0.3071 & 0.3395 & \\textbf{+0.0324} & 0.1353 & 0.1506 & \\textbf{+0.0153} \\\\\n\\midrule\nMean & 0.3055 & 0.3364 & \\textbf{+0.0308} & 0.2560 & 0.2813 & \\textbf{+0.0253} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[t]\n\\centering\n\\caption{Cross-seed signal ranking stability (Kendall's $W$, 3 seeds).}\n\\label{tab:ranking-stability}\n\\small\n\\begin{tabular}{ll cc l}\n\\toprule\nModel & Task & $N$ & Kendall's $W$ & Consensus ranking \\\\\n\\midrule\nQwen  & NER & 8  & 1.000 & VC $>$ SJ $>$ EM $>$ FK $>$ LP \\\\\nQwen  & NER & 16 & 0.956 & SJ $\\approx$ VC $>$ EM $>$ FK $>$ LP \\\\\nQwen  & RE  & 8  & 0.822 & VC $>$ LP $>$ FK $>$ SJ $>$ EM \\\\\nQwen  & RE  & 16 & 0.956 & VC $>$ LP $>$ FK $>$ SJ $>$ EM \\\\\nLLaMA & NER & 8  & 1.000 & VC $>$ SJ $>$ EM $>$ FK $>$ LP \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[t]\n\\centering\n\\caption{Cross-seed standard deviation ($\\sigma$) of Spearman $\\rho$ at $N\\!=\\!8$ vs.\\ $N\\!=\\!16$ (Qwen3-8B, SciERC, 3 seeds). $\\sigma$ is population standard deviation.}\n\\label{tab:sigma-comparison}\n\\small\n\\begin{tabular}{l cc cc}\n\\toprule\n & \\multicolumn{2}{c}{\\textbf{NER} $\\sigma_\\rho$} & \\multicolumn{2}{c}{\\textbf{RE} $\\sigma_\\rho$} \\\\\n\\cmidrule(lr){2-3} \\cmidrule(lr){4-5}\nSignal & $N\\!=\\!8$ & $N\\!=\\!16$ & $N\\!=\\!8$ & $N\\!=\\!16$ \\\\\n\\midrule\nSJ & 0.0179 & 0.0102 & 0.0015 & 0.0067 \\\\\nFK & 0.0157 & 0.0079 & 0.0121 & 0.0143 \\\\\nVC & 0.0187 & 0.0260 & 0.0244 & 0.0158 \\\\\nEM & 0.0076 & 0.0031 & 0.0157 & 0.0049 \\\\\nLP & 0.0125 & 0.0017 & 0.0218 & 0.0152 \\\\\n\\midrule\nMean & 0.0145 & 0.0098 & 0.0151 & 0.0114 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nSignal rankings are highly stable across seeds: Kendall's $W{=}1.000$ for NER at $N{=}8$ (both models), dropping only to $W{=}0.956$ at $N{=}16$ where SJ and VC converge (Table~\\ref{tab:ranking-stability}).\nDoubling $N$ reduces cross-seed $\\sigma$ by 32\\% on NER and 24\\% on RE (Table~\\ref{tab:sigma-comparison}), with the largest reductions for SJ ($-43\\%$ NER) and EM ($-59\\%$ NER), confirming that additional samples stabilize structural signals more than LP.\n\n\\section{Cross-Dataset OOD Analysis}\\label{app:ood}\n\nTo test whether confidence signals generalize under domain shift, we evaluate models on out-of-distribution data: a SciERC-trained model applied to CoNLL instances (wider$\\to$narrower schema) and vice versa (Table~\\ref{tab:ood}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Cross-dataset OOD quality estimation (Spearman $\\rho$, Qwen3-8B, $N{=}8$, $T{=}1.0$, seed${=}42$). SciERC$\\to$CoNLL: SciERC-trained model on CoNLL instances ($n{=}2756$). CoNLL$\\to$SciERC: CoNLL-trained model on SciERC instances ($n{=}529$, excluded from conclusions due to catastrophic model failure). In-domain $\\rho$ from Table~\\ref{tab:quality_estimation} (same model, same seed). \\textsuperscript{***}$p{<}0.001$, \\textsuperscript{*}$p{<}0.05$.}\n\\label{tab:ood}\n\\begin{tabular}{l ccc ccc}\n\\toprule\n & \\multicolumn{3}{c}{\\textbf{SciERC$\\to$CoNLL}} & \\multicolumn{3}{c}{\\textbf{CoNLL$\\to$SciERC}} \\\\\n\\cmidrule(lr){2-4} \\cmidrule(lr){5-7}\nSignal & $\\rho$ & In-dom. & $\\Delta$ & $\\rho$ & In-dom. & $\\Delta$ \\\\\n\\midrule\nVC & .469\\textsuperscript{***} & .379 & +.090 & +.105\\textsuperscript{*} & .379 & $-$.274 \\\\\nSJ & .378\\textsuperscript{***} & .360 & +.018 & $-$.186\\textsuperscript{***} & .360 & $-$.546 \\\\\nEM & .300\\textsuperscript{***} & .295 & +.005 & $-$.202\\textsuperscript{***} & .295 & $-$.497 \\\\\nFK & .285\\textsuperscript{***} & .267 & +.018 & $-$.070 & .267 & $-$.337 \\\\\nLP & .246\\textsuperscript{***} & .205 & +.041 & $-$.152\\textsuperscript{***} & .205 & $-$.357 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Wider-to-narrower schema transfer.}\nWhen the SciERC-trained model (6 NER types) is applied to CoNLL (4 types), all signals remain significant ($p{<}0.001$) and structural signals improve over their in-domain levels (same model, seed${=}42$, $N{=}8$; in-domain $\\rho$ from Table~\\ref{tab:quality_estimation}): VC reaches $\\rho{=}0.469$ (in-domain $0.379$, $\\Delta{=}{+}0.090$), SJ $\\rho{=}0.378$ (in-domain $0.360$, $\\Delta{=}{+}0.018$), and FK $\\rho{=}0.285$ (in-domain $0.267$, $\\Delta{=}{+}0.018$).\nThe wider training schema subsumes CoNLL's narrower schema, so the model produces reasonable outputs even out-of-domain (greedy F1${=}0.522$), and structural signals benefit from the simpler target schema's reduced output ambiguity.\n\n\\paragraph{Narrower-to-wider schema transfer (excluded).}\nThe reverse direction is excluded from our conclusions due to catastrophic model failure, not signal failure.\nThe CoNLL-trained model recognizes only 4 news entity types (PER, ORG, LOC, MISC) and has no relation extraction capability; when applied to SciERC's 6 scientific entity types and 7 relation types, the model cannot produce meaningful structured outputs (greedy NER F1${=}0.009$, RE F1${=}0.001$).\nUnder this regime, most signals flip to negative or near-zero correlations (Table~\\ref{tab:ood}); only VC retains weak positive correlation ($\\rho{=}0.105$, $p{=}0.016$).\nThese negative correlations reflect the model systematically generating confident but incorrect outputs---a capability failure analogous to WNUT-17 (\\S\\ref{sec:qe_results}), not evidence against signal utility.\n\n\\paragraph{Asymmetry interpretation.}\nThe directional asymmetry is driven by schema coverage: wider$\\to$narrower preserves signal utility because the SciERC model's 6-type schema subsumes CoNLL's 4 types, while narrower$\\to$wider fails because the CoNLL model lacks the entity and relation types required by SciERC.\nThis extends the capability boundary identified on WNUT-17 to the domain-shift setting: confidence signals require sufficient model capability as a prerequisite, and results from the CoNLL$\\to$SciERC direction should not be interpreted as evidence of signal degradation under domain shift.\n",
      "numLines": 718,
      "startLine": 1,
      "totalLines": 718
    }
  },
  "sourceToolAssistantUUID": "7a28e12d-cb64-4809-851f-67f9a2ce023d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "f49c1ccb-97a0-4961-857d-2db0aa0e0624",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 47_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[Round 1 审稿请求]: ## Round 1 审稿任务 — Reviewer 2  **你的侧重**：新颖性 + 定位完整性 + 写作质量 + 格式合规  ### 投稿信息 - **目标 venue**: EMNLP 2026 Findings (ARR May cycle) - **Deadline**: 2026-05-25 - **格式**: ACL template, 长文 8 页…",
  "leafUuid": "68e425f4-41f3-4f4d-a276-3bd5c8d830dd",
  "sessionId": "f49c1ccb-97a0-4961-857d-2db0aa0e0624"
}
```

---

### Runtime record

_source line 48_

```json
{
  "type": "ai-title",
  "aiTitle": "Round 1 review for EMNLP 2026 structured IE paper",
  "sessionId": "f49c1ccb-97a0-4961-857d-2db0aa0e0624"
}
```

---

### Tool result

_source line 49 · 2026-05-15T14:59:04.984Z_

<details><summary>↩ Tool result · `toolu_01StVeFknLwn3W9tyTMMz7jk`</summary>

```text
# ACL Rolling Review Form - Complete Scoring Dimensions

## Primary Scoring Dimensions

### 1. Reviewer Confidence
Scale: 1-5
- **5**: "Positive that my evaluation is correct. I read the paper very carefully and am familiar with related work."
- **4**: "Quite sure. I tried to check the important points carefully."
- **3**: "Pretty sure, but there's a chance I missed something."
- **2**: "Willing to defend my evaluation, but it is fairly likely that I missed some details."
- **1**: "Not my area, or paper is very hard to understand."

### 2. Soundness
Scale: 1-5 (with half-point options)
- **5**: "This study is one of the most thorough I have seen, given its type."
- **4**: "This study provides sufficient support for all claims."
- **3**: "This study provides sufficient support for its main claims."
- **2**: "Some of the main claims are not sufficiently supported."
- **1**: "Not yet sufficiently thorough to warrant publication."

### 3. Excitement
Scale: 1-5 (with half-point options)
- **5**: "I would recommend this paper to others and/or attend its presentation."
- **4**: "I would mention this paper to others and/or make an effort to attend."
- **3**: "I might mention some points and/or attend if there's time."
- **2**: "Does not resonate with me, but might with others."
- **1**: "Does not resonate; unlikely to interest the community."

### 4. Overall Assessment
Scale: 1-5 (with half-point options)
- **5**: "Consider for Award"
- **4**: "Conference acceptance"
- **3**: "Findings acceptance"
- **2**: "Resubmit next cycle"
- **1**: "Do not resubmit"

## Additional Evaluation Areas

**Reproducibility** (1-5 scale), **Datasets** (1-5 scale), **Software** (1-5 scale), and **Author Identity Knowledge** (1-5 scale) are also scored with descriptive rubrics provided.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7d1f045d-0b04-4852-a2a7-7b3cd9efd6ee",
  "isSidechain": false,
  "promptId": "a8cee1eb-a5df-415d-8e30-c85446d1e0a7",
  "type": "user",
  "uuid": "1ad311df-6dfe-44cf-a7ae-e57712d1658d",
  "toolUseResult": {
    "bytes": 25365,
    "code": 200,
    "codeText": "OK",
    "result": "# ACL Rolling Review Form - Complete Scoring Dimensions\n\n## Primary Scoring Dimensions\n\n### 1. Reviewer Confidence\nScale: 1-5\n- **5**: \"Positive that my evaluation is correct. I read the paper very carefully and am familiar with related work.\"\n- **4**: \"Quite sure. I tried to check the important points carefully.\"\n- **3**: \"Pretty sure, but there's a chance I missed something.\"\n- **2**: \"Willing to defend my evaluation, but it is fairly likely that I missed some details.\"\n- **1**: \"Not my area, or paper is very hard to understand.\"\n\n### 2. Soundness\nScale: 1-5 (with half-point options)\n- **5**: \"This study is one of the most thorough I have seen, given its type.\"\n- **4**: \"This study provides sufficient support for all claims.\"\n- **3**: \"This study provides sufficient support for its main claims.\"\n- **2**: \"Some of the main claims are not sufficiently supported.\"\n- **1**: \"Not yet sufficiently thorough to warrant publication.\"\n\n### 3. Excitement\nScale: 1-5 (with half-point options)\n- **5**: \"I would recommend this paper to others and/or attend its presentation.\"\n- **4**: \"I would mention this paper to others and/or make an effort to attend.\"\n- **3**: \"I might mention some points and/or attend if there's time.\"\n- **2**: \"Does not resonate with me, but might with others.\"\n- **1**: \"Does not resonate; unlikely to interest the community.\"\n\n### 4. Overall Assessment\nScale: 1-5 (with half-point options)\n- **5**: \"Consider for Award\"\n- **4**: \"Conference acceptance\"\n- **3**: \"Findings acceptance\"\n- **2**: \"Resubmit next cycle\"\n- **1**: \"Do not resubmit\"\n\n## Additional Evaluation Areas\n\n**Reproducibility** (1-5 scale), **Datasets** (1-5 scale), **Software** (1-5 scale), and **Author Identity Knowledge** (1-5 scale) are also scored with descriptive rubrics provided.",
    "durationMs": 6085,
    "url": "https://aclrollingreview.org/reviewform"
  },
  "sourceToolAssistantUUID": "7d1f045d-0b04-4852-a2a7-7b3cd9efd6ee",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "f49c1ccb-97a0-4961-857d-2db0aa0e0624",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 50 · 2026-05-15T14:59:04.988Z_

```json
{
  "parentUuid": "1ad311df-6dfe-44cf-a7ae-e57712d1658d",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "c6d51dce-00f5-4f23-bda3-fc641c9d26ce",
  "timestamp": "2026-05-15T14:59:04.988Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "f49c1ccb-97a0-4961-857d-2db0aa0e0624",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 51 · 2026-05-15T14:59:21.117Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the paper content. Let me also fetch the ARR review form to get the exact scoring criteria, and run the reference verification tool. Let me also count the approximate page length of the paper.

Let me now analyze everything systematically:

1. **ARR Review Form** - I got the scoring dimensions from the WebFetch:
   - Reviewer Confidence: 1-5
   - Soundness: 1-5 (half-point)
   - Excitement: 1-5 (half-point)
   - Overall Assessment: 1-5 (half-point) where 3 = Findings acceptance
   - Reproducibility, Datasets, Software also scored

2. **Page count estimation** - Looking at the LaTeX structure, the main sections span from abstract through conclusion, with the introduction running about 53 lines including a full-width figure, related work at 28 lines, and the method section at 77 lines with additional content. The paper appears to be around 11 pages based on the substantial volume across these core sections, plus the limitations and ethics statement before the appendix.

3. **Reference check** - Need to verify the references next
4. **Novelty assessment** - Should evaluate the core contributions
5. **Writing quality** - Need to assess

Let me run the reference verification and take another look at the review form.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c6d51dce-00f5-4f23-bda3-fc641c9d26ce",
  "isSidechain": false,
  "requestId": "req_011Cb4Z1NZGS3ZwMB164FodW",
  "type": "assistant",
  "uuid": "70e0a8e9-545d-4fc7-9841-5c4cf0faa82a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "f49c1ccb-97a0-4961-857d-2db0aa0e0624",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011xMrGHJxNcV6S4Ex6KwDbR",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 45131,
      "cache_creation_input_tokens": 1510,
      "cache_read_input_tokens": 30886,
      "output_tokens": 747,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1510,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 45131,
          "output_tokens": 747,
          "cache_read_input_tokens": 30886,
          "cache_creation_input_tokens": 1510,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1510
          },
          "type": "message"
        }
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

_source line 52 · 2026-05-15T14:59:21.705Z_

已读完全部论文内容。现在并行执行引用验证和获取完整的 ARR review form。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "70e0a8e9-545d-4fc7-9841-5c4cf0faa82a",
  "isSidechain": false,
  "requestId": "req_011Cb4Z1NZGS3ZwMB164FodW",
  "type": "assistant",
  "uuid": "9ada9898-d80e-4a34-b2b5-50cc09ead33c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "f49c1ccb-97a0-4961-857d-2db0aa0e0624",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011xMrGHJxNcV6S4Ex6KwDbR",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 45131,
      "cache_creation_input_tokens": 1510,
      "cache_read_input_tokens": 30886,
      "output_tokens": 747,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1510,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 45131,
          "output_tokens": 747,
          "cache_read_input_tokens": 30886,
          "cache_creation_input_tokens": 1510,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1510
          },
          "type": "message"
        }
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

_source line 53 · 2026-05-15T14:59:23.306Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__verify_references · `toolu_01EyB9T3fkAJQ5ufKg9cmgPX`</summary>

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
  "parentUuid": "9ada9898-d80e-4a34-b2b5-50cc09ead33c",
  "isSidechain": false,
  "requestId": "req_011Cb4Z1NZGS3ZwMB164FodW",
  "type": "assistant",
  "uuid": "aa8ec23c-6356-49c8-ab88-f0e2b2582083",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "f49c1ccb-97a0-4961-857d-2db0aa0e0624",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011xMrGHJxNcV6S4Ex6KwDbR",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 45131,
      "cache_creation_input_tokens": 1510,
      "cache_read_input_tokens": 30886,
      "output_tokens": 747,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1510,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 45131,
          "output_tokens": 747,
          "cache_read_input_tokens": 30886,
          "cache_creation_input_tokens": 1510,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1510
          },
          "type": "message"
        }
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

_source line 54 · 2026-05-15T14:59:25.385Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01EqJjxmBCfpbzezVriGWSsG`</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewerguidelines",
  "prompt": "Extract the complete reviewer guidelines including: what to evaluate, how to write a review, common pitfalls, what makes a good review, and any specific instructions about scoring soundness, excitement, and overall assessment. Include all detail about what counts as Findings-worthy vs conference-worthy."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "aa8ec23c-6356-49c8-ab88-f0e2b2582083",
  "isSidechain": false,
  "requestId": "req_011Cb4Z1NZGS3ZwMB164FodW",
  "type": "assistant",
  "uuid": "a3c25a5f-9db7-4d02-bc8a-65e864df685e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "f49c1ccb-97a0-4961-857d-2db0aa0e0624",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011xMrGHJxNcV6S4Ex6KwDbR",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 45131,
      "cache_creation_input_tokens": 1510,
      "cache_read_input_tokens": 30886,
      "output_tokens": 747,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1510,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 45131,
          "output_tokens": 747,
          "cache_read_input_tokens": 30886,
          "cache_creation_input_tokens": 1510,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1510
          },
          "type": "message"
        }
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

_source line 55 · 2026-05-15T15:01:06.066Z_

<details><summary>↩ Tool result · `toolu_01EyB9T3fkAJQ5ufKg9cmgPX`</summary>

```text
&lt;persisted-output>
Output too large (50.9KB). Full output saved to: /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie--claude-sessions-review-reviewer-2-a0c838f5/f49c1ccb-97a0-4961-857d-2db0aa0e0624/tool-results/toolu_01EyB9T3fkAJQ5ufKg9cmgPX.txt

Preview (first 2KB):
{"result":"{\"success\": true, \"data\": {\"summary\": {\"total_bib_entries\": 62, \"total_citations\": 94, \"unique_cited_keys\": 62, \"orphan_bib\": 0, \"missing_bib\": 0, \"duplicate_keys\": 0, \"online_verified\": 56, \"online_not_found\": 3, \"online_mismatch\": 3}, \"cross_check\": {\"orphan_bib\": [], \"missing_bib\": [], \"orphan_count\": 0, \"missing_count\": 0}, \"bib_entries\": [{\"key\": \"angelopoulos2021conformal\", \"type\": \"inproceedings\", \"title\": \"Uncertainty Sets for Image Classifiers using Conformal Prediction\", \"authors\": \"Angelopoulos, Anastasios N. and Bates, Stephen and Malik, Jitendra and Jordan, M...\", \"year\": \"2021\", \"venue\": \"ICLR 2021\"}, {\"key\": \"brown2024monkeys\", \"type\": \"article\", \"title\": \"Large Language Monkeys: Scaling Inference Compute with Repeated Sampling\", \"authors\": \"Brown, Bradley and Juravsky, Jordan and Ehrlich, Ryan and Clark, Ronald and Le, ...\", \"year\": \"2024\", \"venue\": \"arXiv preprint arXiv:2407.21787\"}, {\"key\": \"chen2024usc\", \"type\": \"inproceedings\", \"title\": \"Universal Self-Consistency for Large Language Model Generation\", \"authors\": \"Chen, Xinyun and Aksitov, Renat and Alon, Uri and Ren, Jie and Xiao, Kefan and Y...\", \"year\": \"2024\", \"venue\": \"arXiv preprint (ICML 2024 Workshop ICL)\"}, {\"key\": \"cobbe2021verifiers\", \"type\": \"article\", \"title\": \"Training Verifiers to Solve Math Word Problems\", \"authors\": \"Cobbe, Karl and Kosaraju, Vineet and Bavarian, Mohammad and Chen, Mark and Jun, ...\", \"year\": \"2021\", \"venue\": \"arXiv preprint arXiv:2110.14168\"}, {\"key\": \"culotta2004confidence\", \"type\": \"inproceedings\", \"title\": \"Confidence Estimation for Information Extraction\", \"authors\": \"Culotta, Aron and McCallum, Andrew\", \"year\": \"2004\", \"venue\": \"HLT-NAACL 2004\"}, {\"key\": \"derczynski2017wnut\", \"type\": \"inproceedings\", \"title\": \"Results of the WNUT2017 Shared Task on Novel and Emerging Entity Recogniti
...
&lt;/persisted-output>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "aa8ec23c-6356-49c8-ab88-f0e2b2582083",
  "isSidechain": false,
  "promptId": "a8cee1eb-a5df-415d-8e30-c85446d1e0a7",
  "type": "user",
  "uuid": "537f1b98-09b2-4241-842e-9bec3075f6f4",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"summary\\\": {\\\"total_bib_entries\\\": 62, \\\"total_citations\\\": 94, \\\"unique_cited_keys\\\": 62, \\\"orphan_bib\\\": 0, \\\"missing_bib\\\": 0, \\\"duplicate_keys\\\": 0, \\\"online_verified\\\": 56, \\\"online_not_found\\\": 3, \\\"online_mismatch\\\": 3}, \\\"cross_check\\\": {\\\"orphan_bib\\\": [], \\\"missing_bib\\\": [], \\\"orphan_count\\\": 0, \\\"missing_count\\\": 0}, \\\"bib_entries\\\": [{\\\"key\\\": \\\"angelopoulos2021conformal\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Uncertainty Sets for Image Classifiers using Conformal Prediction\\\", \\\"authors\\\": \\\"Angelopoulos, Anastasios N. and Bates, Stephen and Malik, Jitendra and Jordan, M...\\\", \\\"year\\\": \\\"2021\\\", \\\"venue\\\": \\\"ICLR 2021\\\"}, {\\\"key\\\": \\\"brown2024monkeys\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Large Language Monkeys: Scaling Inference Compute with Repeated Sampling\\\", \\\"authors\\\": \\\"Brown, Bradley and Juravsky, Jordan and Ehrlich, Ryan and Clark, Ronald and Le, ...\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"arXiv preprint arXiv:2407.21787\\\"}, {\\\"key\\\": \\\"chen2024usc\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Universal Self-Consistency for Large Language Model Generation\\\", \\\"authors\\\": \\\"Chen, Xinyun and Aksitov, Renat and Alon, Uri and Ren, Jie and Xiao, Kefan and Y...\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"arXiv preprint (ICML 2024 Workshop ICL)\\\"}, {\\\"key\\\": \\\"cobbe2021verifiers\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Training Verifiers to Solve Math Word Problems\\\", \\\"authors\\\": \\\"Cobbe, Karl and Kosaraju, Vineet and Bavarian, Mohammad and Chen, Mark and Jun, ...\\\", \\\"year\\\": \\\"2021\\\", \\\"venue\\\": \\\"arXiv preprint arXiv:2110.14168\\\"}, {\\\"key\\\": \\\"culotta2004confidence\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Confidence Estimation for Information Extraction\\\", \\\"authors\\\": \\\"Culotta, Aron and McCallum, Andrew\\\", \\\"year\\\": \\\"2004\\\", \\\"venue\\\": \\\"HLT-NAACL 2004\\\"}, {\\\"key\\\": \\\"derczynski2017wnut\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Results of the WNUT2017 Shared Task on Novel and Emerging Entity Recognition\\\", \\\"authors\\\": \\\"Derczynski, Leon and Nichols, Eric and Erp, Marieke van and Limsopatham, Nut\\\", \\\"year\\\": \\\"2017\\\", \\\"venue\\\": \\\"W-NUT Workshop at EMNLP 2017\\\"}, {\\\"key\\\": \\\"desai2020calibration\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Calibration of Pre-trained Transformers\\\", \\\"authors\\\": \\\"Desai, Shrey and Durrett, Greg\\\", \\\"year\\\": \\\"2020\\\", \\\"venue\\\": \\\"Proceedings of the 2020 Conference on Empirical Methods in Natural Language Proc...\\\"}, {\\\"key\\\": \\\"eikema2022sampling\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Sampling-Based Approximations to Minimum Bayes Risk Decoding for Neural Machine Translation\\\", \\\"authors\\\": \\\"Eikema, Bryan and Aziz, Wilker\\\", \\\"year\\\": \\\"2022\\\", \\\"venue\\\": \\\"Proceedings of the 2022 Conference on Empirical Methods in Natural Language Proc...\\\"}, {\\\"key\\\": \\\"fisch2021conformal\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Few-Shot Conformal Prediction with Auxiliary Tasks\\\", \\\"authors\\\": \\\"Fisch, Adam and Schuster, Tal and Jaakkola, Tommi and Barzilay, Regina\\\", \\\"year\\\": \\\"2021\\\", \\\"venue\\\": \\\"ICML 2021\\\"}, {\\\"key\\\": \\\"freitag2022high\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"High Quality Rather than High Model Probability: Minimum Bayes Risk Decoding with Neural Metrics\\\", \\\"authors\\\": \\\"Freitag, Markus and Grangier, David and Tan, Qijun and Liang, Bowen\\\", \\\"year\\\": \\\"2022\\\", \\\"venue\\\": \\\"Transactions of the Association for Computational Linguistics\\\"}, {\\\"key\\\": \\\"he2024uncertainty\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Uncertainty Estimation on Sequential Labeling via Uncertainty Transmission\\\", \\\"authors\\\": \\\"He, Jianfeng and Yu, Linlin and Lei, Shuo and Lu, Chang-Tien and Chen, Feng\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"Findings of the Association for Computational Linguistics: NAACL 2024\\\"}, {\\\"key\\\": \\\"fleiss1971agreement\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Measuring nominal scale agreement among many raters.\\\", \\\"authors\\\": \\\"Fleiss, Joseph L.\\\", \\\"year\\\": \\\"1971\\\", \\\"venue\\\": \\\"Psychological Bulletin\\\"}, {\\\"key\\\": \\\"gal2016dropout\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Dropout as a Bayesian Approximation: Representing Model Uncertainty in Deep Learning\\\", \\\"authors\\\": \\\"Gal, Yarin and Ghahramani, Zoubin\\\", \\\"year\\\": \\\"2016\\\", \\\"venue\\\": \\\"ICML 2016\\\"}, {\\\"key\\\": \\\"geifman2017selective\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Selective Classification for Deep Neural Networks\\\", \\\"authors\\\": \\\"Geifman, Yonatan and El-Yaniv, Ran\\\", \\\"year\\\": \\\"2017\\\", \\\"venue\\\": \\\"NeurIPS 2017\\\"}, {\\\"key\\\": \\\"feng2025optimal\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Optimal Self-Consistency for Efficient Reasoning with Large Language Models\\\", \\\"authors\\\": \\\"Feng, Austin and Alonso, Marius and Odonnat, Ambroise\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"arXiv preprint arXiv:2511.12309\\\"}, {\\\"key\\\": \\\"geng2024confidence\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"A Survey of Confidence Estimation and Calibration in Large Language Models\\\", \\\"authors\\\": \\\"Geng, Jiahui and Cai, Fengyu and Wang, Yuxia and Koeppl, Heinz and Nakov, Presla...\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"Proceedings of the 2024 Conference of the North American Chapter of the Associat...\\\"}, {\\\"key\\\": \\\"guo2017calibration\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"On Calibration of Modern Neural Networks\\\", \\\"authors\\\": \\\"Guo, Chuan and Pleiss, Geoff and Sun, Yu and Weinberger, Kilian Q.\\\", \\\"year\\\": \\\"2017\\\", \\\"venue\\\": \\\"ICML 2017\\\"}, {\\\"key\\\": \\\"hobelsberger2025systematic\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Systematic Evaluation of Uncertainty Estimation Methods in Large Language Models\\\", \\\"authors\\\": \\\"Hobelsberger, Christian and Winner, Theresa and Nawroth, Andreas and Mitevski, O...\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"arXiv preprint arXiv:2510.20460\\\"}, {\\\"key\\\": \\\"jaccard1901distribution\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Étude comparative de la distribution florale dans une portion des Alpes et du Jura\\\", \\\"authors\\\": \\\"Jaccard, Paul\\\", \\\"year\\\": \\\"1901\\\", \\\"venue\\\": \\\"Bulletin de la Société Vaudoise des Sciences Naturelles\\\"}, {\\\"key\\\": \\\"josifoski2022genie\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"GenIE: Generative Information Extraction\\\", \\\"authors\\\": \\\"Josifoski, Martin and De Cao, Nicola and Peyrard, Maxime and Petroni, Fabio and ...\\\", \\\"year\\\": \\\"2022\\\", \\\"venue\\\": \\\"Proceedings of the 2022 Conference of the North American Chapter of the Associat...\\\"}, {\\\"key\\\": \\\"kadavath2022language\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Language Models (Mostly) Know What They Know\\\", \\\"authors\\\": \\\"Kadavath, Saurav and Conerly, Tom and Askell, Amanda and Henighan, Tom and Drain...\\\", \\\"year\\\": \\\"2022\\\", \\\"venue\\\": \\\"arXiv preprint arXiv:2207.05221\\\"}, {\\\"key\\\": \\\"kang2025selfcertainty\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Scalable Best-of-N Selection for Large Language Models via Self-Certainty\\\", \\\"authors\\\": \\\"Kang, Zhewei and Zhao, Xuandong and Song, Dawn\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"NeurIPS 2025\\\"}, {\\\"key\\\": \\\"kim2024verifiner\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"VerifiNER: Verification-augmented NER via Knowledge-grounded Reasoning with Large Language Models\\\", \\\"authors\\\": \\\"Kim, Seoyeon and Seo, Kwangwook and Chae, Hyungjoo and Yeo, Jinyoung and Lee, Do...\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"Proceedings of the 62nd Annual Meeting of the Association for Computational Ling...\\\"}, {\\\"key\\\": \\\"kim2026reasc\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Reliability-Aware Adaptive Self-Consistency for Efficient Sampling in LLM Reasoning\\\", \\\"authors\\\": \\\"Kim, Junseok and Yang, Nakyeong and Min, Kyungmin and Jung, Kyomin\\\", \\\"year\\\": \\\"2026\\\", \\\"venue\\\": \\\"ACL 2026\\\"}, {\\\"key\\\": \\\"kossen2024semantic\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Semantic Entropy Probes: Robust and Cheap Hallucination Detection in LLMs\\\", \\\"authors\\\": \\\"Kossen, Jannik and Han, Jiatong and Razzak, Muhammed and Schut, Lisa and Malik, ...\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"arXiv preprint arXiv:2406.15927\\\"}, {\\\"key\\\": \\\"li2025llms\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"LLMs Can Generate a Better Answer by Aggregating Their Own Responses\\\", \\\"authors\\\": \\\"Li, Zichong and Feng, Xinyu and Cai, Yuheng and Zhang, Zixuan and Liu, Tianyi an...\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"arXiv preprint arXiv:2503.04104\\\"}, {\\\"key\\\": \\\"kuhn2023semantic\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Semantic Uncertainty: Linguistic Invariances for Uncertainty Estimation in Natural Language Generation\\\", \\\"authors\\\": \\\"Kuhn, Lorenz and Gal, Yarin and Farquhar, Sebastian\\\", \\\"year\\\": \\\"2023\\\", \\\"venue\\\": \\\"ICLR 2023\\\"}, {\\\"key\\\": \\\"malinin2021uncertainty\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Uncertainty Estimation in Autoregressive Structured Prediction\\\", \\\"authors\\\": \\\"Malinin, Andrey and Gales, Mark\\\", \\\"year\\\": \\\"2021\\\", \\\"venue\\\": \\\"International Conference on Learning Representations\\\"}, {\\\"key\\\": \\\"lakshminarayanan2017ensembles\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Simple and Scalable Predictive Uncertainty Estimation using Deep Ensembles\\\", \\\"authors\\\": \\\"Lakshminarayanan, Balaji and Pritzel, Alexander and Blundell, Charles\\\", \\\"year\\\": \\\"2017\\\", \\\"venue\\\": \\\"NeurIPS 2017\\\"}, {\\\"key\\\": \\\"li2023codeie\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"CodeIE: Large Code Generation Models are Better Few-Shot Information Extractors\\\", \\\"authors\\\": \\\"Li, Peng and Sun, Tianxiang and Tang, Qiong and Yan, Hang and Wu, Yuanbin and Hu...\\\", \\\"year\\\": \\\"2023\\\", \\\"venue\\\": \\\"Proceedings of the 61st Annual Meeting of the Association for Computational Ling...\\\"}, {\\\"key\\\": \\\"lightman2024verify\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Let's Verify Step by Step\\\", \\\"authors\\\": \\\"Lightman, Hunter and Kosaraju, Vineet and Burda, Yura and Edwards, Harri and Bak...\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"ICLR 2024\\\"}, {\\\"key\\\": \\\"luan2018scierc\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Multi-Task Identification of Entities, Relations, and Coreference for Scientific Knowledge Graph Construction\\\", \\\"authors\\\": \\\"Luan, Yi and He, Luheng and Ostendorf, Mari and Hajishirzi, Hannaneh\\\", \\\"year\\\": \\\"2018\\\", \\\"venue\\\": \\\"Proceedings of the 2018 Conference on Empirical Methods in Natural Language Proc...\\\"}, {\\\"key\\\": \\\"manakul2023selfcheckgpt\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"SelfCheckGPT: Zero-Resource Black-Box Hallucination Detection for Generative Large Language Models\\\", \\\"authors\\\": \\\"Manakul, Potsawee and Liusie, Adian and Gales, Mark\\\", \\\"year\\\": \\\"2023\\\", \\\"venue\\\": \\\"Proceedings of the 2023 Conference on Empirical Methods in Natural Language Proc...\\\"}, {\\\"key\\\": \\\"nedellec2026consistency\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Consistency–accuracy correlation in hard-prompted LLMs for entity and relation extraction: empirical findings from plant...\\\", \\\"authors\\\": \\\"Yao, Xinzhi and Nédellec, Claire and Xia, Jingbo and Bossy, Robert\\\", \\\"year\\\": \\\"2026\\\", \\\"venue\\\": \\\"Genomics \\\\\\\\& Informatics\\\"}, {\\\"key\\\": \\\"oh2025latentsc\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Latent Self-Consistency for Reliable Majority-Set Selection in Short- and Long-Answer Reasoning\\\", \\\"authors\\\": \\\"Oh, Jungsuk and Lee, Jay-Yoon\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"arXiv preprint arXiv:2508.18395\\\"}, {\\\"key\\\": \\\"sainz2024gollie\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"GoLLIE: Annotation Guidelines improve Zero-Shot Information-Extraction\\\", \\\"authors\\\": \\\"Sainz, Oscar and García-Ferrero, Iker and Agerri, Rodrigo and Lacalle, Oier Lope...\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"ICLR 2024\\\"}, {\\\"key\\\": \\\"shelmanov2021active\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Active Learning for Sequence Tagging with Deep Pre-trained Models and Bayesian Uncertainty Estimates\\\", \\\"authors\\\": \\\"Shelmanov, Artem and Puzyrev, Dmitri and Kupriyanova, Lyubov and Belyakov, Denis...\\\", \\\"year\\\": \\\"2021\\\", \\\"venue\\\": \\\"Proceedings of the 16th Conference of the European Chapter of the Association fo...\\\"}, {\\\"key\\\": \\\"snell2025scaling\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters\\\", \\\"authors\\\": \\\"Snell, Charlie and Lee, Jaehoon and Xu, Kelvin and Kumar, Aviral\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"Proceedings of the International Conference on Learning Representations (ICLR)\\\"}, {\\\"key\\\": \\\"taubenfeld2025cisc\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Confidence Improves Self-Consistency in LLMs\\\", \\\"authors\\\": \\\"Taubenfeld, Amir and Sheffer, Tom and Ofek, Eran and Feder, Amir and Goldstein, ...\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"Findings of the Association for Computational Linguistics: ACL 2025\\\"}, {\\\"key\\\": \\\"thirukovalluru2024atomic\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Atomic Self-Consistency for Better Long Form Generations\\\", \\\"authors\\\": \\\"Thirukovalluru, Raghuveer and Huang, Yukun and Dhingra, Bhuwan\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"Proceedings of the 2024 Conference on Empirical Methods in Natural Language Proc...\\\"}, {\\\"key\\\": \\\"tjongkimsang2003conll\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Introduction to the CoNLL-2003 Shared Task: Language-Independent Named Entity Recognition\\\", \\\"authors\\\": \\\"Sang, Erik F. Tjong Kim and Meulder, Fien De\\\", \\\"year\\\": \\\"2003\\\", \\\"venue\\\": \\\"CoNLL 2003\\\"}, {\\\"key\\\": \\\"vashurin2025cocoa\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Uncertainty Quantification for LLMs through Minimum Bayes Risk: Bridging Confidence and Consistency\\\", \\\"authors\\\": \\\"Vashurin, Roman and Goloburda, Maiya and Ilina, Albina and Rubashevskii, Aleksan...\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"NeurIPS 2025\\\"}, {\\\"key\\\": \\\"wadhwa2023revisiting\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Revisiting Relation Extraction in the era of Large Language Models\\\", \\\"authors\\\": \\\"Wadhwa, Somin and Amir, Silvio and Wallace, Byron\\\", \\\"year\\\": \\\"2023\\\", \\\"venue\\\": \\\"Proceedings of the 61st Annual Meeting of the Association for Computational Ling...\\\"}, {\\\"key\\\": \\\"wang2023instructuie\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"InstructUIE: Multi-task Instruction Tuning for Unified Information Extraction\\\", \\\"authors\\\": \\\"Wang, Xiao and Zhou, Weikang and Zu, Can and Xia, Han and Chen, Tianze and Zhang...\\\", \\\"year\\\": \\\"2023\\\", \\\"venue\\\": \\\"arXiv preprint arXiv:2304.08085\\\"}, {\\\"key\\\": \\\"wang2023selfconsistency\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Self-Consistency Improves Chain of Thought Reasoning in Language Models\\\", \\\"authors\\\": \\\"Wang, Xuezhi and Wei, Jason and Schuurmans, Dale and Le, Quoc and Chi, Ed and Na...\\\", \\\"year\\\": \\\"2023\\\", \\\"venue\\\": \\\"ICLR 2023\\\"}, {\\\"key\\\": \\\"wang2025make\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Make Every Penny Count: Difficulty-Adaptive Self-Consistency for Cost-Efficient Reasoning\\\", \\\"authors\\\": \\\"Wang, Xinglin and Feng, Shaoxiong and Li, Yiwei and Yuan, Peiwen and Zhang, Yueq...\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"Findings of the Association for Computational Linguistics: NAACL 2025\\\"}, {\\\"key\\\": \\\"wang2024mathshepherd\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Math-Shepherd: Verify and Reinforce LLMs Step-by-step without Human Annotations\\\", \\\"authors\\\": \\\"Wang, Peiyi and Li, Lei and Shao, Zhihong and Xu, Runxin and Dai, Damai and Li, ...\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"ACL 2024\\\"}, {\\\"key\\\": \\\"wang2025rankedvoting\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Ranked Voting based Self-Consistency of Large Language Models\\\", \\\"authors\\\": \\\"Wang, Weiqin and Wang, Yile and Huang, Hui\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"ACL Findings 2025\\\"}, {\\\"key\\\": \\\"wen2025know\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Know Your Limits: A Survey of Abstention in Large Language Models\\\", \\\"authors\\\": \\\"Wen, Bingbing and Yao, Jihan and Feng, Shangbin and Xu, Chenjun and Tsvetkov, Yu...\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"Transactions of the Association for Computational Linguistics\\\"}, {\\\"key\\\": \\\"willard2023guided\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Efficient Guided Generation for Large Language Models\\\", \\\"authors\\\": \\\"Willard, Brandon T. and Louf, Rémi\\\", \\\"year\\\": \\\"2023\\\", \\\"venue\\\": \\\"arXiv preprint arXiv:2307.09702\\\"}, {\\\"key\\\": \\\"xia2025survey\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"A Survey of Uncertainty Estimation Methods on Large Language Models\\\", \\\"authors\\\": \\\"Xia, Zhiqiu and Xu, Jinxuan and Zhang, Yuqian and Liu, Hang\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"ACL Findings 2025\\\"}, {\\\"key\\\": \\\"xiao2019uncertainty\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Quantifying Uncertainties in Natural Language Processing Tasks\\\", \\\"authors\\\": \\\"Xiao, Yijun and Wang, William Yang\\\", \\\"year\\\": \\\"2019\\\", \\\"venue\\\": \\\"Proceedings of the AAAI Conference on Artificial Intelligence\\\"}, {\\\"key\\\": \\\"zhang2023ener\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"E-NER: Evidential Deep Learning for Trustworthy Named Entity Recognition\\\", \\\"authors\\\": \\\"Zhang, Zhen and Hu, Mengting and Zhao, Shiwan and Huang, Minlie and Wang, Haotia...\\\", \\\"year\\\": \\\"2023\\\", \\\"venue\\\": \\\"Findings of the Association for Computational Linguistics: ACL 2023\\\"}, {\\\"key\\\": \\\"zheng2024llamafactory\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"LlamaFactory: Unified Efficient Fine-Tuning of 100+ Language Models\\\", \\\"authors\\\": \\\"Zheng, Yaowei and Zhang, Richong and Zhang, Junhao and Ye, Yanhan and Luo, Zheya...\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"Proceedings of the 62nd Annual Meeting of the Association for Computational Ling...\\\"}, {\\\"key\\\": \\\"zhou2024uniner\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"UniversalNER: Targeted Distillation from Large Language Models for Open Named Entity Recognition\\\", \\\"authors\\\": \\\"Zhou, Wenxuan and Zhang, Sheng and Gu, Yu and Chen, Muhao and Poon, Hoifung\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"Proceedings of the International Conference on Learning Representations (ICLR)\\\"}, {\\\"key\\\": \\\"xiong2024llm\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Can LLMs Express Their Uncertainty? An Empirical Evaluation of Confidence Elicitation in LLMs\\\", \\\"authors\\\": \\\"Xiong, Miao and Hu, Zhiyuan and Lu, Xinyang and Li, Yifei and Fu, Jie and He, Ju...\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"Proceedings of the International Conference on Learning Representations (ICLR)\\\"}, {\\\"key\\\": \\\"muller2021understanding\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Understanding the Properties of Minimum Bayes Risk Decoding in Neural Machine Translation\\\", \\\"authors\\\": \\\"M\\\\\\\\\\\\\\\"uller, Mathias and Sennrich, Rico\\\", \\\"year\\\": \\\"2021\\\", \\\"venue\\\": \\\"Proceedings of the 59th Annual Meeting of the Association for Computational Ling...\\\"}, {\\\"key\\\": \\\"heo2025uncertainty\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Do LLMs Estimate Uncertainty Well in Instruction Following?\\\", \\\"authors\\\": \\\"Heo, Juyeon and Xiong, Miao and Heinze-Deml, Christina and Narain, Jaya\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"Proceedings of the International Conference on Learning Representations (ICLR)\\\"}, {\\\"key\\\": \\\"eikema2025structured\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Structure-Conditional Minimum Bayes Risk Decoding\\\", \\\"authors\\\": \\\"Eikema, Bryan and Rutkiewicz, Anna and Giulianelli, Mario\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"Proceedings of the 2025 Conference on Empirical Methods in Natural Language Proc...\\\"}, {\\\"key\\\": \\\"zhang2025tts\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"A Survey on Test-Time Scaling in Large Language Models: What, How, Where, and How Well?\\\", \\\"authors\\\": \\\"Zhang, Qiyuan and Lyu, Fuyuan and Sun, Zexu and Wang, Lei and Zhang, Weixu and G...\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"arXiv preprint arXiv:2503.24235\\\"}, {\\\"key\\\": \\\"venktesh2025trust\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Trust but Verify! A Survey on Verification Design for Test-time Scaling\\\", \\\"authors\\\": \\\"Venktesh, V and Rathee, Mandeep and Anand, Avishek\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"arXiv preprint arXiv:2508.16665\\\"}, {\\\"key\\\": \\\"jinnai2024mbr\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Model-Based Minimum Bayes Risk Decoding for Text Generation\\\", \\\"authors\\\": \\\"Jinnai, Yuu and Morimura, Tetsuro and Honda, Ukyo and Ariu, Kaito and Abe, Kensh...\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"Proceedings of the 41st International Conference on Machine Learning (ICML)\\\"}], \\\"tex_citations\\\": [{\\\"key\\\": \\\"wang2023selfconsistency\\\", \\\"file\\\": \\\"sections/introduction.tex\\\", \\\"line\\\": 4, \\\"command\\\": \\\"citealp\\\"}, {\\\"key\\\": \\\"snell2025scaling\\\", \\\"file\\\": \\\"sections/introduction.tex\\\", \\\"line\\\": 5, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"brown2024monkeys\\\", \\\"file\\\": \\\"sections/introduction.tex\\\", \\\"line\\\": 5, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"wang2023selfconsistency\\\", \\\"file\\\": \\\"sections/introduction.tex\\\", \\\"line\\\": 15, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"chen2024usc\\\", \\\"file\\\": \\\"sections/introduction.tex\\\", \\\"line\\\": 15, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"taubenfeld2025cisc\\\", \\\"file\\\": \\\"sections/introduction.tex\\\", \\\"line\\\": 15, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"kang2025selfcertainty\\\", \\\"file\\\": \\\"sections/introduction.tex\\\", \\\"line\\\": 15, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"nedellec2026consistency\\\", \\\"file\\\": \\\"sections/introduction.tex\\\", \\\"line\\\": 16, \\\"command\\\": \\\"citet\\\"}, {\\\"key\\\": \\\"willard2023guided\\\", \\\"file\\\": \\\"sections/introduction.tex\\\", \\\"line\\\": 19, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"eikema2022sampling\\\", \\\"file\\\": \\\"sections/introduction.tex\\\", \\\"line\\\": 24, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"freitag2022high\\\", \\\"file\\\": \\\"sections/introduction.tex\\\", \\\"line\\\": 24, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"muller2021understanding\\\", \\\"file\\\": \\\"sections/introduction.tex\\\", \\\"line\\\": 24, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"luan2018scierc\\\", \\\"file\\\": \\\"sections/introduction.tex\\\", \\\"line\\\": 35, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"tjongkimsang2003conll\\\", \\\"file\\\": \\\"sections/introduction.tex\\\", \\\"line\\\": 35, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"derczynski2017wnut\\\", \\\"file\\\": \\\"sections/introduction.tex\\\", \\\"line\\\": 35, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"nedellec2026consistency\\\", \\\"file\\\": \\\"sections/introduction.tex\\\", \\\"line\\\": 51, \\\"command\\\": \\\"citet\\\"}, {\\\"key\\\": \\\"wang2023selfconsistency\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 4, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"chen2024usc\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 5, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"thirukovalluru2024atomic\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 5, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"manakul2023selfcheckgpt\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 5, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"zhang2025tts\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 6, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"snell2025scaling\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 6, \\\"command\\\": \\\"citet\\\"}, {\\\"key\\\": \\\"brown2024monkeys\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 6, \\\"command\\\": \\\"citet\\\"}, {\\\"key\\\": \\\"taubenfeld2025cisc\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 7, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"kang2025selfcertainty\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 7, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"kim2026reasc\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 7, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"wang2025rankedvoting\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 7, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"oh2025latentsc\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 7, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"feng2025optimal\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 8, \\\"command\\\": \\\"citet\\\"}, {\\\"key\\\": \\\"wang2025make\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 8, \\\"command\\\": \\\"citet\\\"}, {\\\"key\\\": \\\"li2025llms\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 8, \\\"command\\\": \\\"citet\\\"}, {\\\"key\\\": \\\"nedellec2026consistency\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 13, \\\"command\\\": \\\"citet\\\"}, {\\\"key\\\": \\\"vashurin2025cocoa\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 16, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"zhou2024uniner\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 17, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"sainz2024gollie\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 17, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"josifoski2022genie\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 17, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"li2023codeie\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 17, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"wadhwa2023revisiting\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 17, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"wang2023instructuie\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 17, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"willard2023guided\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 17, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"geng2024confidence\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 20, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"wen2025know\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 20, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"xia2025survey\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 20, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"hobelsberger2025systematic\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 20, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"xiong2024llm\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 20, \\\"command\\\": \\\"citet\\\"}, {\\\"key\\\": \\\"heo2025uncertainty\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 20, \\\"command\\\": \\\"citet\\\"}, {\\\"key\\\": \\\"kuhn2023semantic\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 21, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"kossen2024semantic\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 21, \\\"command\\\": \\\"citet\\\"}, {\\\"key\\\": \\\"kadavath2022language\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 21, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"malinin2021uncertainty\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 21, \\\"command\\\": \\\"citet\\\"}, {\\\"key\\\": \\\"guo2017calibration\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 23, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"desai2020calibration\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 23, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"lakshminarayanan2017ensembles\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 23, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"gal2016dropout\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 23, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"xiao2019uncertainty\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 24, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"shelmanov2021active\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 24, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"zhang2023ener\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 24, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"kim2024verifiner\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 24, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"he2024uncertainty\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 24, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"fisch2021conformal\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 25, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"angelopoulos2021conformal\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 25, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"cobbe2021verifiers\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 25, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"lightman2024verify\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 25, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"venktesh2025trust\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 25, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"wang2024mathshepherd\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 25, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"eikema2022sampling\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 26, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"freitag2022high\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 26, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"jinnai2024mbr\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 26, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"eikema2025structured\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 27, \\\"command\\\": \\\"citet\\\"}, {\\\"key\\\": \\\"geifman2017selective\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 28, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"culotta2004confidence\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 28, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"willard2023guided\\\", \\\"file\\\": \\\"sections/method.tex\\\", \\\"line\\\": 5, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"fleiss1971agreement\\\", \\\"file\\\": \\\"sections/method.tex\\\", \\\"line\\\": 34, \\\"command\\\": \\\"citet\\\"}, {\\\"key\\\": \\\"jaccard1901distribution\\\", \\\"file\\\": \\\"sections/method.tex\\\", \\\"line\\\": 45, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"luan2018scierc\\\", \\\"file\\\": \\\"sections/experiments.tex\\\", \\\"line\\\": 9, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"tjongkimsang2003conll\\\", \\\"file\\\": \\\"sections/experiments.tex\\\", \\\"line\\\": 10, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"derczynski2017wnut\\\", \\\"file\\\": \\\"sections/experiments.tex\\\", \\\"line\\\": 11, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"zheng2024llamafactory\\\", \\\"file\\\": \\\"sections/experiments.tex\\\", \\\"line\\\": 14, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"willard2023guided\\\", \\\"file\\\": \\\"sections/experiments.tex\\\", \\\"line\\\": 21, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"kuhn2023semantic\\\", \\\"file\\\": \\\"sections/experiments.tex\\\", \\\"line\\\": 60, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"xiong2024llm\\\", \\\"file\\\": \\\"sections/experiments.tex\\\", \\\"line\\\": 74, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"brown2024monkeys\\\", \\\"file\\\": \\\"sections/experiments.tex\\\", \\\"line\\\": 141, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"snell2025scaling\\\", \\\"file\\\": \\\"sections/experiments.tex\\\", \\\"line\\\": 141, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"cobbe2021verifiers\\\", \\\"file\\\": \\\"sections/experiments.tex\\\", \\\"line\\\": 141, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"eikema2022sampling\\\", \\\"file\\\": \\\"sections/discussion.tex\\\", \\\"line\\\": 28, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"muller2021understanding\\\", \\\"file\\\": \\\"sections/discussion.tex\\\", \\\"line\\\": 28, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"freitag2022high\\\", \\\"file\\\": \\\"sections/discussion.tex\\\", \\\"line\\\": 29, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"jinnai2024mbr\\\", \\\"file\\\": \\\"sections/discussion.tex\\\", \\\"line\\\": 29, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"eikema2025structured\\\", \\\"file\\\": \\\"sections/discussion.tex\\\", \\\"line\\\": 30, \\\"command\\\": \\\"citet\\\"}, {\\\"key\\\": \\\"cobbe2021verifiers\\\", \\\"file\\\": \\\"sections/discussion.tex\\\", \\\"line\\\": 53, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"venktesh2025trust\\\", \\\"file\\\": \\\"sections/discussion.tex\\\", \\\"line\\\": 53, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"brown2024monkeys\\\", \\\"file\\\": \\\"sections/appendix.tex\\\", \\\"line\\\": 193, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"snell2025scaling\\\", \\\"file\\\": \\\"sections/appendix.tex\\\", \\\"line\\\": 193, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"willard2023guided\\\", \\\"file\\\": \\\"sections/appendix.tex\\\", \\\"line\\\": 394, \\\"command\\\": \\\"cite\\\"}], \\\"online_verification\\\": [{\\\"key\\\": \\\"angelopoulos2021conformal\\\", \\\"title\\\": \\\"Uncertainty Sets for Image Classifiers using Conformal Prediction\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Uncertainty Sets for Image Classifiers using Conformal Prediction\\\", \\\"matched_year\\\": \\\"2020\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"brown2024monkeys\\\", \\\"title\\\": \\\"Large Language Monkeys: Scaling Inference Compute with Repeated Sampling\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Large Language Monkeys: Scaling Inference Compute with Repeated Sampling\\\", \\\"matched_year\\\": \\\"2024\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"chen2024usc\\\", \\\"title\\\": \\\"Universal Self-Consistency for Large Language Model Generation\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Universal Self-Consistency for Large Language Model Generation\\\", \\\"matched_year\\\": \\\"2023\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"cobbe2021verifiers\\\", \\\"title\\\": \\\"Training Verifiers to Solve Math Word Problems\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Training Verifiers to Solve Math Word Problems\\\", \\\"matched_year\\\": \\\"2021\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"culotta2004confidence\\\", \\\"title\\\": \\\"Confidence Estimation for Information Extraction\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Confidence estimation for information extraction\\\", \\\"matched_year\\\": \\\"2004\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"derczynski2017wnut\\\", \\\"title\\\": \\\"Results of the WNUT2017 Shared Task on Novel and Emerging Entity Recognition\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Results of the WNUT2017 Shared Task on Novel and Emerging Entity Recognition\\\", \\\"matched_year\\\": \\\"2017\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"desai2020calibration\\\", \\\"title\\\": \\\"Calibration of Pre-trained Transformers\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Calibration of Pre-trained Transformers\\\", \\\"matched_year\\\": \\\"2020\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"eikema2022sampling\\\", \\\"title\\\": \\\"Sampling-Based Approximations to Minimum Bayes Risk Decoding for Neural Machine Translation\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Sampling-Based Approximations to Minimum Bayes Risk Decoding for Neural Machine Translation\\\", \\\"matched_year\\\": \\\"2022\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"fisch2021conformal\\\", \\\"title\\\": \\\"Few-Shot Conformal Prediction with Auxiliary Tasks\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Few-shot Conformal Prediction with Auxiliary Tasks\\\", \\\"matched_year\\\": \\\"2021\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"freitag2022high\\\", \\\"title\\\": \\\"High Quality Rather than High Model Probability: Minimum Bayes Risk Decoding with Neural Metrics\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"High Quality Rather than High Model Probability: Minimum Bayes Risk Decoding with Neural Metrics\\\", \\\"matched_year\\\": \\\"2022\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"he2024uncertainty\\\", \\\"title\\\": \\\"Uncertainty Estimation on Sequential Labeling via Uncertainty Transmission\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Uncertainty Estimation on Sequential Labeling via Uncertainty Transmission\\\", \\\"matched_year\\\": \\\"2024\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"fleiss1971agreement\\\", \\\"title\\\": \\\"Measuring nominal scale agreement among many raters.\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Measuring nominal scale agreement among many raters.\\\", \\\"matched_year\\\": \\\"1971\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"gal2016dropout\\\", \\\"title\\\": \\\"Dropout as a Bayesian Approximation: Representing Model Uncertainty in Deep Learning\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Dropout as a Bayesian Approximation: Representing Model Uncertainty in Deep Learning\\\", \\\"matched_year\\\": \\\"2015\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"geifman2017selective\\\", \\\"title\\\": \\\"Selective Classification for Deep Neural Networks\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Selective Classification for Deep Neural Networks\\\", \\\"matched_year\\\": \\\"2017\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"feng2025optimal\\\", \\\"title\\\": \\\"Optimal Self-Consistency for Efficient Reasoning with Large Language Models\\\", \\\"status\\\": \\\"mismatch\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Optimal Self-Consistency for Efficient Reasoning with Large Language Models\\\", \\\"matched_year\\\": \\\"2025\\\", \\\"mismatch_fields\\\": [\\\"first_author: bib=feng vs api=austin\\\"], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"geng2024confidence\\\", \\\"title\\\": \\\"A Survey of Confidence Estimation and Calibration in Large Language Models\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"A Survey of Confidence Estimation and Calibration in Large Language Models\\\", \\\"matched_year\\\": \\\"2024\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"guo2017calibration\\\", \\\"title\\\": \\\"On Calibration of Modern Neural Networks\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"On Calibration of Modern Neural Networks\\\", \\\"matched_year\\\": \\\"2017\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"hobelsberger2025systematic\\\", \\\"title\\\": \\\"Systematic Evaluation of Uncertainty Estimation Methods in Large Language Models\\\", \\\"status\\\": \\\"not_found\\\", \\\"confidence\\\": 0.236, \\\"matched_title\\\": \\\"A new criterion for assessing discriminant validity in variance-based structural equation modeling\\\", \\\"matched_year\\\": \\\"\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"best match similarity 0.24 below threshold 0.82\\\"}, {\\\"key\\\": \\\"jaccard1901distribution\\\", \\\"title\\\": \\\"Étude comparative de la distribution florale dans une portion des Alpes et du Jura\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Étude comparative de la distribution florale dans une portion des Alpes et du Jura\\\", \\\"matched_year\\\": \\\"1901\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"josifoski2022genie\\\", \\\"title\\\": \\\"GenIE: Generative Information Extraction\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"GenIE: Generative Information Extraction\\\", \\\"matched_year\\\": \\\"2022\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"kadavath2022language\\\", \\\"title\\\": \\\"Language Models (Mostly) Know What They Know\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Language Models (Mostly) Know What They Know\\\", \\\"matched_year\\\": \\\"2022\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"kang2025selfcertainty\\\", \\\"title\\\": \\\"Scalable Best-of-N Selection for Large Language Models via Self-Certainty\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Scalable Best-of-N Selection for Large Language Models via Self-Certainty\\\", \\\"matched_year\\\": \\\"2025\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"kim2024verifiner\\\", \\\"title\\\": \\\"VerifiNER: Verification-augmented NER via Knowledge-grounded Reasoning with Large Language Models\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"VerifiNER: Verification-augmented NER via Knowledge-grounded Reasoning with Large Language Models\\\", \\\"matched_year\\\": \\\"2024\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"kim2026reasc\\\", \\\"title\\\": \\\"Reliability-Aware Adaptive Self-Consistency for Efficient Sampling in LLM Reasoning\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Reliability-Aware Adaptive Self-Consistency for Efficient Sampling in LLM Reasoning\\\", \\\"matched_year\\\": \\\"2026\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"kossen2024semantic\\\", \\\"title\\\": \\\"Semantic Entropy Probes: Robust and Cheap Hallucination Detection in LLMs\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Semantic Entropy Probes: Robust and Cheap Hallucination Detection in LLMs\\\", \\\"matched_year\\\": \\\"2024\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"li2025llms\\\", \\\"title\\\": \\\"LLMs Can Generate a Better Answer by Aggregating Their Own Responses\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"LLMs Can Generate a Better Answer by Aggregating Their Own Responses\\\", \\\"matched_year\\\": \\\"2025\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"kuhn2023semantic\\\", \\\"title\\\": \\\"Semantic Uncertainty: Linguistic Invariances for Uncertainty Estimation in Natural Language Generation\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Semantic Uncertainty: Linguistic Invariances for Uncertainty Estimation in Natural Language Generation\\\", \\\"matched_year\\\": \\\"2023\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"malinin2021uncertainty\\\", \\\"title\\\": \\\"Uncertainty Estimation in Autoregressive Structured Prediction\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Uncertainty Estimation in Autoregressive Structured Prediction\\\", \\\"matched_year\\\": \\\"2020\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"lakshminarayanan2017ensembles\\\", \\\"title\\\": \\\"Simple and Scalable Predictive Uncertainty Estimation using Deep Ensembles\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Simple and Scalable Predictive Uncertainty Estimation using Deep Ensembles\\\", \\\"matched_year\\\": \\\"2016\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"li2023codeie\\\", \\\"title\\\": \\\"CodeIE: Large Code Generation Models are Better Few-Shot Information Extractors\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"CodeIE: Large Code Generation Models are Better Few-Shot Information Extractors\\\", \\\"matched_year\\\": \\\"2023\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"lightman2024verify\\\", \\\"title\\\": \\\"Let's Verify Step by Step\\\", \\\"status\\\": \\\"not_found\\\", \\\"confidence\\\": 0.246, \\\"matched_title\\\": \\\"Development and dosimetric verification of static SHArc: Step‐and‐shoot carbon ion arc therapy for LET &lt;sub>d&lt;/sub> escalation in pancreatic tumors\\\", \\\"matched_year\\\": \\\"\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"best match similarity 0.25 below threshold 0.82\\\"}, {\\\"key\\\": \\\"luan2018scierc\\\", \\\"title\\\": \\\"Multi-Task Identification of Entities, Relations, and Coreference for Scientific Knowledge Graph Construction\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Multi-Task Identification of Entities, Relations, and Coreference for Scientific Knowledge Graph Construction\\\", \\\"matched_year\\\": \\\"2018\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"manakul2023selfcheckgpt\\\", \\\"title\\\": \\\"SelfCheckGPT: Zero-Resource Black-Box Hallucination Detection for Generative Large Language Models\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"SelfCheckGPT: Zero-Resource Black-Box Hallucination Detection for Generative Large Language Models\\\", \\\"matched_year\\\": \\\"2023\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"nedellec2026consistency\\\", \\\"title\\\": \\\"Consistency–accuracy correlation in hard-prompted LLMs for entity and relation extraction: empirical findings from plant-health data\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Consistency–accuracy correlation in hard-prompted LLMs for entity and relation extraction: empirical findings from plant-health data\\\", \\\"matched_year\\\": \\\"2026\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"oh2025latentsc\\\", \\\"title\\\": \\\"Latent Self-Consistency for Reliable Majority-Set Selection in Short- and Long-Answer Reasoning\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Latent Self-Consistency for Reliable Majority-Set Selection in Short- and Long-Answer Reasoning\\\", \\\"matched_year\\\": \\\"2026\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"sainz2024gollie\\\", \\\"title\\\": \\\"GoLLIE: Annotation Guidelines improve Zero-Shot Information-Extraction\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"GoLLIE: Annotation Guidelines improve Zero-Shot Information-Extraction\\\", \\\"matched_year\\\": \\\"2023\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"shelmanov2021active\\\", \\\"title\\\": \\\"Active Learning for Sequence Tagging with Deep Pre-trained Models and Bayesian Uncertainty Estimates\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Active Learning for Sequence Tagging with Deep Pre-trained Models and Bayesian Uncertainty Estimates\\\", \\\"matched_year\\\": \\\"2021\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"snell2025scaling\\\", \\\"title\\\": \\\"Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters\\\", \\\"status\\\": \\\"mismatch\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters\\\", \\\"matched_year\\\": \\\"2024\\\", \\\"mismatch_fields\\\": [\\\"first_author: bib=snell vs api=charlie\\\"], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"taubenfeld2025cisc\\\", \\\"title\\\": \\\"Confidence Improves Self-Consistency in LLMs\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Confidence Improves Self-Consistency in LLMs\\\", \\\"matched_year\\\": \\\"2025\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"thirukovalluru2024atomic\\\", \\\"title\\\": \\\"Atomic Self-Consistency for Better Long Form Generations\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Atomic Self-Consistency for Better Long Form Generations\\\", \\\"matched_year\\\": \\\"2024\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"tjongkimsang2003conll\\\", \\\"title\\\": \\\"Introduction to the CoNLL-2003 Shared Task: Language-Independent Named Entity Recognition\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Introduction to the CoNLL-2003 Shared Task: Language-Independent Named Entity Recognition\\\", \\\"matched_year\\\": \\\"2003\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"vashurin2025cocoa\\\", \\\"title\\\": \\\"Uncertainty Quantification for LLMs through Minimum Bayes Risk: Bridging Confidence and Consistency\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Uncertainty Quantification for LLMs through Minimum Bayes Risk: Bridging Confidence and Consistency\\\", \\\"matched_year\\\": \\\"2025\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"wadhwa2023revisiting\\\", \\\"title\\\": \\\"Revisiting Relation Extraction in the era of Large Language Models\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Revisiting Relation Extraction in the era of Large Language Models\\\", \\\"matched_year\\\": \\\"2023\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"wang2023instructuie\\\", \\\"title\\\": \\\"InstructUIE: Multi-task Instruction Tuning for Unified Information Extraction\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"InstructUIE: Multi-task Instruction Tuning for Unified Information Extraction\\\", \\\"matched_year\\\": \\\"2023\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"wang2023selfconsistency\\\", \\\"title\\\": \\\"Self-Consistency Improves Chain of Thought Reasoning in Language Models\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Self-Consistency Improves Chain of Thought Reasoning in Language Models\\\", \\\"matched_year\\\": \\\"2022\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"wang2025make\\\", \\\"title\\\": \\\"Make Every Penny Count: Difficulty-Adaptive Self-Consistency for Cost-Efficient Reasoning\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Make Every Penny Count: Difficulty-Adaptive Self-Consistency for Cost-Efficient Reasoning\\\", \\\"matched_year\\\": \\\"2025\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"wang2024mathshepherd\\\", \\\"title\\\": \\\"Math-Shepherd: Verify and Reinforce LLMs Step-by-step without Human Annotations\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Math-Shepherd: Verify and Reinforce LLMs Step-by-step without Human Annotations\\\", \\\"matched_year\\\": \\\"2024\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"wang2025rankedvoting\\\", \\\"title\\\": \\\"Ranked Voting based Self-Consistency of Large Language Models\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Ranked Voting based Self-Consistency of Large Language Models\\\", \\\"matched_year\\\": \\\"2025\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"wen2025know\\\", \\\"title\\\": \\\"Know Your Limits: A Survey of Abstention in Large Language Models\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Know Your Limits: A Survey of Abstention in Large Language Models\\\", \\\"matched_year\\\": \\\"2025\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"willard2023guided\\\", \\\"title\\\": \\\"Efficient Guided Generation for Large Language Models\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Efficient Guided Generation for Large Language Models\\\", \\\"matched_year\\\": \\\"2023\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"xia2025survey\\\", \\\"title\\\": \\\"A Survey of Uncertainty Estimation Methods on Large Language Models\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"A Survey of Uncertainty Estimation Methods on Large Language Models\\\", \\\"matched_year\\\": \\\"2025\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"xiao2019uncertainty\\\", \\\"title\\\": \\\"Quantifying Uncertainties in Natural Language Processing Tasks\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Quantifying Uncertainties in Natural Language Processing Tasks\\\", \\\"matched_year\\\": \\\"2019\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"zhang2023ener\\\", \\\"title\\\": \\\"E-NER: Evidential Deep Learning for Trustworthy Named Entity Recognition\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"E-NER: Evidential Deep Learning for Trustworthy Named Entity Recognition\\\", \\\"matched_year\\\": \\\"2023\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"zheng2024llamafactory\\\", \\\"title\\\": \\\"LlamaFactory: Unified Efficient Fine-Tuning of 100+ Language Models\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"LlamaFactory: Unified Efficient Fine-Tuning of 100+ Language Models\\\", \\\"matched_year\\\": \\\"2024\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"zhou2024uniner\\\", \\\"title\\\": \\\"UniversalNER: Targeted Distillation from Large Language Models for Open Named Entity Recognition\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"UniversalNER: Targeted Distillation from Large Language Models for Open Named Entity Recognition\\\", \\\"matched_year\\\": \\\"2023\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"xiong2024llm\\\", \\\"title\\\": \\\"Can LLMs Express Their Uncertainty? An Empirical Evaluation of Confidence Elicitation in LLMs\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Can LLMs Express Their Uncertainty? An Empirical Evaluation of Confidence Elicitation in LLMs\\\", \\\"matched_year\\\": \\\"2023\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"muller2021understanding\\\", \\\"title\\\": \\\"Understanding the Properties of Minimum Bayes Risk Decoding in Neural Machine Translation\\\", \\\"status\\\": \\\"mismatch\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Understanding the Properties of Minimum Bayes Risk Decoding in Neural Machine Translation\\\", \\\"matched_year\\\": \\\"2021\\\", \\\"mismatch_fields\\\": [\\\"first_author: bib=m\\\\\\\\\\\\\\\"uller vs api=müller\\\"], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"heo2025uncertainty\\\", \\\"title\\\": \\\"Do LLMs Estimate Uncertainty Well in Instruction Following?\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 0.983, \\\"matched_title\\\": \\\"Do LLMs estimate uncertainty well in instruction-following?\\\", \\\"matched_year\\\": \\\"2024\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"eikema2025structured\\\", \\\"title\\\": \\\"Structure-Conditional Minimum Bayes Risk Decoding\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Structure-Conditional Minimum Bayes Risk Decoding\\\", \\\"matched_year\\\": \\\"2025\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"zhang2025tts\\\", \\\"title\\\": \\\"A Survey on Test-Time Scaling in Large Language Models: What, How, Where, and How Well?\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"A Survey on Test-Time Scaling in Large Language Models: What, How, Where, and How Well?\\\", \\\"matched_year\\\": \\\"2025\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"venktesh2025trust\\\", \\\"title\\\": \\\"Trust but Verify! A Survey on Verification Design for Test-time Scaling\\\", \\\"status\\\": \\\"not_found\\\", \\\"confidence\\\": 0.252, \\\"matched_title\\\": \\\"The PRISMA Statement for Reporting Systematic Reviews and Meta-Analyses of Studies That Evaluate Health Care Interventions: Explanation and Elaboration\\\", \\\"matched_year\\\": \\\"\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"best match similarity 0.25 below threshold 0.82\\\"}, {\\\"key\\\": \\\"jinnai2024mbr\\\", \\\"title\\\": \\\"Model-Based Minimum Bayes Risk Decoding for Text Generation\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Model-Based Minimum Bayes Risk Decoding for Text Generation\\\", \\\"matched_year\\\": \\\"2023\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}]}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"summary\": {\"total_bib_entries\": 62, \"total_citations\": 94, \"unique_cited_keys\": 62, \"orphan_bib\": 0, \"missing_bib\": 0, \"duplicate_keys\": 0, \"online_verified\": 56, \"online_not_found\": 3, \"online_mismatch\": 3}, \"cross_check\": {\"orphan_bib\": [], \"missing_bib\": [], \"orphan_count\": 0, \"missing_count\": 0}, \"bib_entries\": [{\"key\": \"angelopoulos2021conformal\", \"type\": \"inproceedings\", \"title\": \"Uncertainty Sets for Image Classifiers using Conformal Prediction\", \"authors\": \"Angelopoulos, Anastasios N. and Bates, Stephen and Malik, Jitendra and Jordan, M...\", \"year\": \"2021\", \"venue\": \"ICLR 2021\"}, {\"key\": \"brown2024monkeys\", \"type\": \"article\", \"title\": \"Large Language Monkeys: Scaling Inference Compute with Repeated Sampling\", \"authors\": \"Brown, Bradley and Juravsky, Jordan and Ehrlich, Ryan and Clark, Ronald and Le, ...\", \"year\": \"2024\", \"venue\": \"arXiv preprint arXiv:2407.21787\"}, {\"key\": \"chen2024usc\", \"type\": \"inproceedings\", \"title\": \"Universal Self-Consistency for Large Language Model Generation\", \"authors\": \"Chen, Xinyun and Aksitov, Renat and Alon, Uri and Ren, Jie and Xiao, Kefan and Y...\", \"year\": \"2024\", \"venue\": \"arXiv preprint (ICML 2024 Workshop ICL)\"}, {\"key\": \"cobbe2021verifiers\", \"type\": \"article\", \"title\": \"Training Verifiers to Solve Math Word Problems\", \"authors\": \"Cobbe, Karl and Kosaraju, Vineet and Bavarian, Mohammad and Chen, Mark and Jun, ...\", \"year\": \"2021\", \"venue\": \"arXiv preprint arXiv:2110.14168\"}, {\"key\": \"culotta2004confidence\", \"type\": \"inproceedings\", \"title\": \"Confidence Estimation for Information Extraction\", \"authors\": \"Culotta, Aron and McCallum, Andrew\", \"year\": \"2004\", \"venue\": \"HLT-NAACL 2004\"}, {\"key\": \"derczynski2017wnut\", \"type\": \"inproceedings\", \"title\": \"Results of the WNUT2017 Shared Task on Novel and Emerging Entity Recognition\", \"authors\": \"Derczynski, Leon and Nichols, Eric and Erp, Marieke van and Limsopatham, Nut\", \"year\": \"2017\", \"venue\": \"W-NUT Workshop at EMNLP 2017\"}, {\"key\": \"desai2020calibration\", \"type\": \"inproceedings\", \"title\": \"Calibration of Pre-trained Transformers\", \"authors\": \"Desai, Shrey and Durrett, Greg\", \"year\": \"2020\", \"venue\": \"Proceedings of the 2020 Conference on Empirical Methods in Natural Language Proc...\"}, {\"key\": \"eikema2022sampling\", \"type\": \"inproceedings\", \"title\": \"Sampling-Based Approximations to Minimum Bayes Risk Decoding for Neural Machine Translation\", \"authors\": \"Eikema, Bryan and Aziz, Wilker\", \"year\": \"2022\", \"venue\": \"Proceedings of the 2022 Conference on Empirical Methods in Natural Language Proc...\"}, {\"key\": \"fisch2021conformal\", \"type\": \"inproceedings\", \"title\": \"Few-Shot Conformal Prediction with Auxiliary Tasks\", \"authors\": \"Fisch, Adam and Schuster, Tal and Jaakkola, Tommi and Barzilay, Regina\", \"year\": \"2021\", \"venue\": \"ICML 2021\"}, {\"key\": \"freitag2022high\", \"type\": \"article\", \"title\": \"High Quality Rather than High Model Probability: Minimum Bayes Risk Decoding with Neural Metrics\", \"authors\": \"Freitag, Markus and Grangier, David and Tan, Qijun and Liang, Bowen\", \"year\": \"2022\", \"venue\": \"Transactions of the Association for Computational Linguistics\"}, {\"key\": \"he2024uncertainty\", \"type\": \"inproceedings\", \"title\": \"Uncertainty Estimation on Sequential Labeling via Uncertainty Transmission\", \"authors\": \"He, Jianfeng and Yu, Linlin and Lei, Shuo and Lu, Chang-Tien and Chen, Feng\", \"year\": \"2024\", \"venue\": \"Findings of the Association for Computational Linguistics: NAACL 2024\"}, {\"key\": \"fleiss1971agreement\", \"type\": \"article\", \"title\": \"Measuring nominal scale agreement among many raters.\", \"authors\": \"Fleiss, Joseph L.\", \"year\": \"1971\", \"venue\": \"Psychological Bulletin\"}, {\"key\": \"gal2016dropout\", \"type\": \"inproceedings\", \"title\": \"Dropout as a Bayesian Approximation: Representing Model Uncertainty in Deep Learning\", \"authors\": \"Gal, Yarin and Ghahramani, Zoubin\", \"year\": \"2016\", \"venue\": \"ICML 2016\"}, {\"key\": \"geifman2017selective\", \"type\": \"inproceedings\", \"title\": \"Selective Classification for Deep Neural Networks\", \"authors\": \"Geifman, Yonatan and El-Yaniv, Ran\", \"year\": \"2017\", \"venue\": \"NeurIPS 2017\"}, {\"key\": \"feng2025optimal\", \"type\": \"article\", \"title\": \"Optimal Self-Consistency for Efficient Reasoning with Large Language Models\", \"authors\": \"Feng, Austin and Alonso, Marius and Odonnat, Ambroise\", \"year\": \"2025\", \"venue\": \"arXiv preprint arXiv:2511.12309\"}, {\"key\": \"geng2024confidence\", \"type\": \"inproceedings\", \"title\": \"A Survey of Confidence Estimation and Calibration in Large Language Models\", \"authors\": \"Geng, Jiahui and Cai, Fengyu and Wang, Yuxia and Koeppl, Heinz and Nakov, Presla...\", \"year\": \"2024\", \"venue\": \"Proceedings of the 2024 Conference of the North American Chapter of the Associat...\"}, {\"key\": \"guo2017calibration\", \"type\": \"inproceedings\", \"title\": \"On Calibration of Modern Neural Networks\", \"authors\": \"Guo, Chuan and Pleiss, Geoff and Sun, Yu and Weinberger, Kilian Q.\", \"year\": \"2017\", \"venue\": \"ICML 2017\"}, {\"key\": \"hobelsberger2025systematic\", \"type\": \"article\", \"title\": \"Systematic Evaluation of Uncertainty Estimation Methods in Large Language Models\", \"authors\": \"Hobelsberger, Christian and Winner, Theresa and Nawroth, Andreas and Mitevski, O...\", \"year\": \"2025\", \"venue\": \"arXiv preprint arXiv:2510.20460\"}, {\"key\": \"jaccard1901distribution\", \"type\": \"article\", \"title\": \"Étude comparative de la distribution florale dans une portion des Alpes et du Jura\", \"authors\": \"Jaccard, Paul\", \"year\": \"1901\", \"venue\": \"Bulletin de la Société Vaudoise des Sciences Naturelles\"}, {\"key\": \"josifoski2022genie\", \"type\": \"inproceedings\", \"title\": \"GenIE: Generative Information Extraction\", \"authors\": \"Josifoski, Martin and De Cao, Nicola and Peyrard, Maxime and Petroni, Fabio and ...\", \"year\": \"2022\", \"venue\": \"Proceedings of the 2022 Conference of the North American Chapter of the Associat...\"}, {\"key\": \"kadavath2022language\", \"type\": \"article\", \"title\": \"Language Models (Mostly) Know What They Know\", \"authors\": \"Kadavath, Saurav and Conerly, Tom and Askell, Amanda and Henighan, Tom and Drain...\", \"year\": \"2022\", \"venue\": \"arXiv preprint arXiv:2207.05221\"}, {\"key\": \"kang2025selfcertainty\", \"type\": \"inproceedings\", \"title\": \"Scalable Best-of-N Selection for Large Language Models via Self-Certainty\", \"authors\": \"Kang, Zhewei and Zhao, Xuandong and Song, Dawn\", \"year\": \"2025\", \"venue\": \"NeurIPS 2025\"}, {\"key\": \"kim2024verifiner\", \"type\": \"inproceedings\", \"title\": \"VerifiNER: Verification-augmented NER via Knowledge-grounded Reasoning with Large Language Models\", \"authors\": \"Kim, Seoyeon and Seo, Kwangwook and Chae, Hyungjoo and Yeo, Jinyoung and Lee, Do...\", \"year\": \"2024\", \"venue\": \"Proceedings of the 62nd Annual Meeting of the Association for Computational Ling...\"}, {\"key\": \"kim2026reasc\", \"type\": \"inproceedings\", \"title\": \"Reliability-Aware Adaptive Self-Consistency for Efficient Sampling in LLM Reasoning\", \"authors\": \"Kim, Junseok and Yang, Nakyeong and Min, Kyungmin and Jung, Kyomin\", \"year\": \"2026\", \"venue\": \"ACL 2026\"}, {\"key\": \"kossen2024semantic\", \"type\": \"article\", \"title\": \"Semantic Entropy Probes: Robust and Cheap Hallucination Detection in LLMs\", \"authors\": \"Kossen, Jannik and Han, Jiatong and Razzak, Muhammed and Schut, Lisa and Malik, ...\", \"year\": \"2024\", \"venue\": \"arXiv preprint arXiv:2406.15927\"}, {\"key\": \"li2025llms\", \"type\": \"article\", \"title\": \"LLMs Can Generate a Better Answer by Aggregating Their Own Responses\", \"authors\": \"Li, Zichong and Feng, Xinyu and Cai, Yuheng and Zhang, Zixuan and Liu, Tianyi an...\", \"year\": \"2025\", \"venue\": \"arXiv preprint arXiv:2503.04104\"}, {\"key\": \"kuhn2023semantic\", \"type\": \"inproceedings\", \"title\": \"Semantic Uncertainty: Linguistic Invariances for Uncertainty Estimation in Natural Language Generation\", \"authors\": \"Kuhn, Lorenz and Gal, Yarin and Farquhar, Sebastian\", \"year\": \"2023\", \"venue\": \"ICLR 2023\"}, {\"key\": \"malinin2021uncertainty\", \"type\": \"inproceedings\", \"title\": \"Uncertainty Estimation in Autoregressive Structured Prediction\", \"authors\": \"Malinin, Andrey and Gales, Mark\", \"year\": \"2021\", \"venue\": \"International Conference on Learning Representations\"}, {\"key\": \"lakshminarayanan2017ensembles\", \"type\": \"inproceedings\", \"title\": \"Simple and Scalable Predictive Uncertainty Estimation using Deep Ensembles\", \"authors\": \"Lakshminarayanan, Balaji and Pritzel, Alexander and Blundell, Charles\", \"year\": \"2017\", \"venue\": \"NeurIPS 2017\"}, {\"key\": \"li2023codeie\", \"type\": \"inproceedings\", \"title\": \"CodeIE: Large Code Generation Models are Better Few-Shot Information Extractors\", \"authors\": \"Li, Peng and Sun, Tianxiang and Tang, Qiong and Yan, Hang and Wu, Yuanbin and Hu...\", \"year\": \"2023\", \"venue\": \"Proceedings of the 61st Annual Meeting of the Association for Computational Ling...\"}, {\"key\": \"lightman2024verify\", \"type\": \"inproceedings\", \"title\": \"Let's Verify Step by Step\", \"authors\": \"Lightman, Hunter and Kosaraju, Vineet and Burda, Yura and Edwards, Harri and Bak...\", \"year\": \"2024\", \"venue\": \"ICLR 2024\"}, {\"key\": \"luan2018scierc\", \"type\": \"inproceedings\", \"title\": \"Multi-Task Identification of Entities, Relations, and Coreference for Scientific Knowledge Graph Construction\", \"authors\": \"Luan, Yi and He, Luheng and Ostendorf, Mari and Hajishirzi, Hannaneh\", \"year\": \"2018\", \"venue\": \"Proceedings of the 2018 Conference on Empirical Methods in Natural Language Proc...\"}, {\"key\": \"manakul2023selfcheckgpt\", \"type\": \"inproceedings\", \"title\": \"SelfCheckGPT: Zero-Resource Black-Box Hallucination Detection for Generative Large Language Models\", \"authors\": \"Manakul, Potsawee and Liusie, Adian and Gales, Mark\", \"year\": \"2023\", \"venue\": \"Proceedings of the 2023 Conference on Empirical Methods in Natural Language Proc...\"}, {\"key\": \"nedellec2026consistency\", \"type\": \"article\", \"title\": \"Consistency–accuracy correlation in hard-prompted LLMs for entity and relation extraction: empirical findings from plant...\", \"authors\": \"Yao, Xinzhi and Nédellec, Claire and Xia, Jingbo and Bossy, Robert\", \"year\": \"2026\", \"venue\": \"Genomics \\\\& Informatics\"}, {\"key\": \"oh2025latentsc\", \"type\": \"article\", \"title\": \"Latent Self-Consistency for Reliable Majority-Set Selection in Short- and Long-Answer Reasoning\", \"authors\": \"Oh, Jungsuk and Lee, Jay-Yoon\", \"year\": \"2025\", \"venue\": \"arXiv preprint arXiv:2508.18395\"}, {\"key\": \"sainz2024gollie\", \"type\": \"inproceedings\", \"title\": \"GoLLIE: Annotation Guidelines improve Zero-Shot Information-Extraction\", \"authors\": \"Sainz, Oscar and García-Ferrero, Iker and Agerri, Rodrigo and Lacalle, Oier Lope...\", \"year\": \"2024\", \"venue\": \"ICLR 2024\"}, {\"key\": \"shelmanov2021active\", \"type\": \"inproceedings\", \"title\": \"Active Learning for Sequence Tagging with Deep Pre-trained Models and Bayesian Uncertainty Estimates\", \"authors\": \"Shelmanov, Artem and Puzyrev, Dmitri and Kupriyanova, Lyubov and Belyakov, Denis...\", \"year\": \"2021\", \"venue\": \"Proceedings of the 16th Conference of the European Chapter of the Association fo...\"}, {\"key\": \"snell2025scaling\", \"type\": \"inproceedings\", \"title\": \"Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters\", \"authors\": \"Snell, Charlie and Lee, Jaehoon and Xu, Kelvin and Kumar, Aviral\", \"year\": \"2025\", \"venue\": \"Proceedings of the International Conference on Learning Representations (ICLR)\"}, {\"key\": \"taubenfeld2025cisc\", \"type\": \"inproceedings\", \"title\": \"Confidence Improves Self-Consistency in LLMs\", \"authors\": \"Taubenfeld, Amir and Sheffer, Tom and Ofek, Eran and Feder, Amir and Goldstein, ...\", \"year\": \"2025\", \"venue\": \"Findings of the Association for Computational Linguistics: ACL 2025\"}, {\"key\": \"thirukovalluru2024atomic\", \"type\": \"inproceedings\", \"title\": \"Atomic Self-Consistency for Better Long Form Generations\", \"authors\": \"Thirukovalluru, Raghuveer and Huang, Yukun and Dhingra, Bhuwan\", \"year\": \"2024\", \"venue\": \"Proceedings of the 2024 Conference on Empirical Methods in Natural Language Proc...\"}, {\"key\": \"tjongkimsang2003conll\", \"type\": \"inproceedings\", \"title\": \"Introduction to the CoNLL-2003 Shared Task: Language-Independent Named Entity Recognition\", \"authors\": \"Sang, Erik F. Tjong Kim and Meulder, Fien De\", \"year\": \"2003\", \"venue\": \"CoNLL 2003\"}, {\"key\": \"vashurin2025cocoa\", \"type\": \"inproceedings\", \"title\": \"Uncertainty Quantification for LLMs through Minimum Bayes Risk: Bridging Confidence and Consistency\", \"authors\": \"Vashurin, Roman and Goloburda, Maiya and Ilina, Albina and Rubashevskii, Aleksan...\", \"year\": \"2025\", \"venue\": \"NeurIPS 2025\"}, {\"key\": \"wadhwa2023revisiting\", \"type\": \"inproceedings\", \"title\": \"Revisiting Relation Extraction in the era of Large Language Models\", \"authors\": \"Wadhwa, Somin and Amir, Silvio and Wallace, Byron\", \"year\": \"2023\", \"venue\": \"Proceedings of the 61st Annual Meeting of the Association for Computational Ling...\"}, {\"key\": \"wang2023instructuie\", \"type\": \"article\", \"title\": \"InstructUIE: Multi-task Instruction Tuning for Unified Information Extraction\", \"authors\": \"Wang, Xiao and Zhou, Weikang and Zu, Can and Xia, Han and Chen, Tianze and Zhang...\", \"year\": \"2023\", \"venue\": \"arXiv preprint arXiv:2304.08085\"}, {\"key\": \"wang2023selfconsistency\", \"type\": \"inproceedings\", \"title\": \"Self-Consistency Improves Chain of Thought Reasoning in Language Models\", \"authors\": \"Wang, Xuezhi and Wei, Jason and Schuurmans, Dale and Le, Quoc and Chi, Ed and Na...\", \"year\": \"2023\", \"venue\": \"ICLR 2023\"}, {\"key\": \"wang2025make\", \"type\": \"inproceedings\", \"title\": \"Make Every Penny Count: Difficulty-Adaptive Self-Consistency for Cost-Efficient Reasoning\", \"authors\": \"Wang, Xinglin and Feng, Shaoxiong and Li, Yiwei and Yuan, Peiwen and Zhang, Yueq...\", \"year\": \"2025\", \"venue\": \"Findings of the Association for Computational Linguistics: NAACL 2025\"}, {\"key\": \"wang2024mathshepherd\", \"type\": \"inproceedings\", \"title\": \"Math-Shepherd: Verify and Reinforce LLMs Step-by-step without Human Annotations\", \"authors\": \"Wang, Peiyi and Li, Lei and Shao, Zhihong and Xu, Runxin and Dai, Damai and Li, ...\", \"year\": \"2024\", \"venue\": \"ACL 2024\"}, {\"key\": \"wang2025rankedvoting\", \"type\": \"inproceedings\", \"title\": \"Ranked Voting based Self-Consistency of Large Language Models\", \"authors\": \"Wang, Weiqin and Wang, Yile and Huang, Hui\", \"year\": \"2025\", \"venue\": \"ACL Findings 2025\"}, {\"key\": \"wen2025know\", \"type\": \"article\", \"title\": \"Know Your Limits: A Survey of Abstention in Large Language Models\", \"authors\": \"Wen, Bingbing and Yao, Jihan and Feng, Shangbin and Xu, Chenjun and Tsvetkov, Yu...\", \"year\": \"2025\", \"venue\": \"Transactions of the Association for Computational Linguistics\"}, {\"key\": \"willard2023guided\", \"type\": \"article\", \"title\": \"Efficient Guided Generation for Large Language Models\", \"authors\": \"Willard, Brandon T. and Louf, Rémi\", \"year\": \"2023\", \"venue\": \"arXiv preprint arXiv:2307.09702\"}, {\"key\": \"xia2025survey\", \"type\": \"inproceedings\", \"title\": \"A Survey of Uncertainty Estimation Methods on Large Language Models\", \"authors\": \"Xia, Zhiqiu and Xu, Jinxuan and Zhang, Yuqian and Liu, Hang\", \"year\": \"2025\", \"venue\": \"ACL Findings 2025\"}, {\"key\": \"xiao2019uncertainty\", \"type\": \"article\", \"title\": \"Quantifying Uncertainties in Natural Language Processing Tasks\", \"authors\": \"Xiao, Yijun and Wang, William Yang\", \"year\": \"2019\", \"venue\": \"Proceedings of the AAAI Conference on Artificial Intelligence\"}, {\"key\": \"zhang2023ener\", \"type\": \"inproceedings\", \"title\": \"E-NER: Evidential Deep Learning for Trustworthy Named Entity Recognition\", \"authors\": \"Zhang, Zhen and Hu, Mengting and Zhao, Shiwan and Huang, Minlie and Wang, Haotia...\", \"year\": \"2023\", \"venue\": \"Findings of the Association for Computational Linguistics: ACL 2023\"}, {\"key\": \"zheng2024llamafactory\", \"type\": \"inproceedings\", \"title\": \"LlamaFactory: Unified Efficient Fine-Tuning of 100+ Language Models\", \"authors\": \"Zheng, Yaowei and Zhang, Richong and Zhang, Junhao and Ye, Yanhan and Luo, Zheya...\", \"year\": \"2024\", \"venue\": \"Proceedings of the 62nd Annual Meeting of the Association for Computational Ling...\"}, {\"key\": \"zhou2024uniner\", \"type\": \"inproceedings\", \"title\": \"UniversalNER: Targeted Distillation from Large Language Models for Open Named Entity Recognition\", \"authors\": \"Zhou, Wenxuan and Zhang, Sheng and Gu, Yu and Chen, Muhao and Poon, Hoifung\", \"year\": \"2024\", \"venue\": \"Proceedings of the International Conference on Learning Representations (ICLR)\"}, {\"key\": \"xiong2024llm\", \"type\": \"inproceedings\", \"title\": \"Can LLMs Express Their Uncertainty? An Empirical Evaluation of Confidence Elicitation in LLMs\", \"authors\": \"Xiong, Miao and Hu, Zhiyuan and Lu, Xinyang and Li, Yifei and Fu, Jie and He, Ju...\", \"year\": \"2024\", \"venue\": \"Proceedings of the International Conference on Learning Representations (ICLR)\"}, {\"key\": \"muller2021understanding\", \"type\": \"inproceedings\", \"title\": \"Understanding the Properties of Minimum Bayes Risk Decoding in Neural Machine Translation\", \"authors\": \"M\\\\\\\"uller, Mathias and Sennrich, Rico\", \"year\": \"2021\", \"venue\": \"Proceedings of the 59th Annual Meeting of the Association for Computational Ling...\"}, {\"key\": \"heo2025uncertainty\", \"type\": \"inproceedings\", \"title\": \"Do LLMs Estimate Uncertainty Well in Instruction Following?\", \"authors\": \"Heo, Juyeon and Xiong, Miao and Heinze-Deml, Christina and Narain, Jaya\", \"year\": \"2025\", \"venue\": \"Proceedings of the International Conference on Learning Representations (ICLR)\"}, {\"key\": \"eikema2025structured\", \"type\": \"inproceedings\", \"title\": \"Structure-Conditional Minimum Bayes Risk Decoding\", \"authors\": \"Eikema, Bryan and Rutkiewicz, Anna and Giulianelli, Mario\", \"year\": \"2025\", \"venue\": \"Proceedings of the 2025 Conference on Empirical Methods in Natural Language Proc...\"}, {\"key\": \"zhang2025tts\", \"type\": \"article\", \"title\": \"A Survey on Test-Time Scaling in Large Language Models: What, How, Where, and How Well?\", \"authors\": \"Zhang, Qiyuan and Lyu, Fuyuan and Sun, Zexu and Wang, Lei and Zhang, Weixu and G...\", \"year\": \"2025\", \"venue\": \"arXiv preprint arXiv:2503.24235\"}, {\"key\": \"venktesh2025trust\", \"type\": \"article\", \"title\": \"Trust but Verify! A Survey on Verification Design for Test-time Scaling\", \"authors\": \"Venktesh, V and Rathee, Mandeep and Anand, Avishek\", \"year\": \"2025\", \"venue\": \"arXiv preprint arXiv:2508.16665\"}, {\"key\": \"jinnai2024mbr\", \"type\": \"inproceedings\", \"title\": \"Model-Based Minimum Bayes Risk Decoding for Text Generation\", \"authors\": \"Jinnai, Yuu and Morimura, Tetsuro and Honda, Ukyo and Ariu, Kaito and Abe, Kensh...\", \"year\": \"2024\", \"venue\": \"Proceedings of the 41st International Conference on Machine Learning (ICML)\"}], \"tex_citations\": [{\"key\": \"wang2023selfconsistency\", \"file\": \"sections/introduction.tex\", \"line\": 4, \"command\": \"citealp\"}, {\"key\": \"snell2025scaling\", \"file\": \"sections/introduction.tex\", \"line\": 5, \"command\": \"cite\"}, {\"key\": \"brown2024monkeys\", \"file\": \"sections/introduction.tex\", \"line\": 5, \"command\": \"cite\"}, {\"key\": \"wang2023selfconsistency\", \"file\": \"sections/introduction.tex\", \"line\": 15, \"command\": \"cite\"}, {\"key\": \"chen2024usc\", \"file\": \"sections/introduction.tex\", \"line\": 15, \"command\": \"cite\"}, {\"key\": \"taubenfeld2025cisc\", \"file\": \"sections/introduction.tex\", \"line\": 15, \"command\": \"cite\"}, {\"key\": \"kang2025selfcertainty\", \"file\": \"sections/introduction.tex\", \"line\": 15, \"command\": \"cite\"}, {\"key\": \"nedellec2026consistency\", \"file\": \"sections/introduction.tex\", \"line\": 16, \"command\": \"citet\"}, {\"key\": \"willard2023guided\", \"file\": \"sections/introduction.tex\", \"line\": 19, \"command\": \"cite\"}, {\"key\": \"eikema2022sampling\", \"file\": \"sections/introduction.tex\", \"line\": 24, \"command\": \"cite\"}, {\"key\": \"freitag2022high\", \"file\": \"sections/introduction.tex\", \"line\": 24, \"command\": \"cite\"}, {\"key\": \"muller2021understanding\", \"file\": \"sections/introduction.tex\", \"line\": 24, \"command\": \"cite\"}, {\"key\": \"luan2018scierc\", \"file\": \"sections/introduction.tex\", \"line\": 35, \"command\": \"cite\"}, {\"key\": \"tjongkimsang2003conll\", \"file\": \"sections/introduction.tex\", \"line\": 35, \"command\": \"cite\"}, {\"key\": \"derczynski2017wnut\", \"file\": \"sections/introduction.tex\", \"line\": 35, \"command\": \"cite\"}, {\"key\": \"nedellec2026consistency\", \"file\": \"sections/introduction.tex\", \"line\": 51, \"command\": \"citet\"}, {\"key\": \"wang2023selfconsistency\", \"file\": \"sections/related_work.tex\", \"line\": 4, \"command\": \"cite\"}, {\"key\": \"chen2024usc\", \"file\": \"sections/related_work.tex\", \"line\": 5, \"command\": \"cite\"}, {\"key\": \"thirukovalluru2024atomic\", \"file\": \"sections/related_work.tex\", \"line\": 5, \"command\": \"cite\"}, {\"key\": \"manakul2023selfcheckgpt\", \"file\": \"sections/related_work.tex\", \"line\": 5, \"command\": \"cite\"}, {\"key\": \"zhang2025tts\", \"file\": \"sections/related_work.tex\", \"line\": 6, \"command\": \"cite\"}, {\"key\": \"snell2025scaling\", \"file\": \"sections/related_work.tex\", \"line\": 6, \"command\": \"citet\"}, {\"key\": \"brown2024monkeys\", \"file\": \"sections/related_work.tex\", \"line\": 6, \"command\": \"citet\"}, {\"key\": \"taubenfeld2025cisc\", \"file\": \"sections/related_work.tex\", \"line\": 7, \"command\": \"cite\"}, {\"key\": \"kang2025selfcertainty\", \"file\": \"sections/related_work.tex\", \"line\": 7, \"command\": \"cite\"}, {\"key\": \"kim2026reasc\", \"file\": \"sections/related_work.tex\", \"line\": 7, \"command\": \"cite\"}, {\"key\": \"wang2025rankedvoting\", \"file\": \"sections/related_work.tex\", \"line\": 7, \"command\": \"cite\"}, {\"key\": \"oh2025latentsc\", \"file\": \"sections/related_work.tex\", \"line\": 7, \"command\": \"cite\"}, {\"key\": \"feng2025optimal\", \"file\": \"sections/related_work.tex\", \"line\": 8, \"command\": \"citet\"}, {\"key\": \"wang2025make\", \"file\": \"sections/related_work.tex\", \"line\": 8, \"command\": \"citet\"}, {\"key\": \"li2025llms\", \"file\": \"sections/related_work.tex\", \"line\": 8, \"command\": \"citet\"}, {\"key\": \"nedellec2026consistency\", \"file\": \"sections/related_work.tex\", \"line\": 13, \"command\": \"citet\"}, {\"key\": \"vashurin2025cocoa\", \"file\": \"sections/related_work.tex\", \"line\": 16, \"command\": \"cite\"}, {\"key\": \"zhou2024uniner\", \"file\": \"sections/related_work.tex\", \"line\": 17, \"command\": \"cite\"}, {\"key\": \"sainz2024gollie\", \"file\": \"sections/related_work.tex\", \"line\": 17, \"command\": \"cite\"}, {\"key\": \"josifoski2022genie\", \"file\": \"sections/related_work.tex\", \"line\": 17, \"command\": \"cite\"}, {\"key\": \"li2023codeie\", \"file\": \"sections/related_work.tex\", \"line\": 17, \"command\": \"cite\"}, {\"key\": \"wadhwa2023revisiting\", \"file\": \"sections/related_work.tex\", \"line\": 17, \"command\": \"cite\"}, {\"key\": \"wang2023instructuie\", \"file\": \"sections/related_work.tex\", \"line\": 17, \"command\": \"cite\"}, {\"key\": \"willard2023guided\", \"file\": \"sections/related_work.tex\", \"line\": 17, \"command\": \"cite\"}, {\"key\": \"geng2024confidence\", \"file\": \"sections/related_work.tex\", \"line\": 20, \"command\": \"cite\"}, {\"key\": \"wen2025know\", \"file\": \"sections/related_work.tex\", \"line\": 20, \"command\": \"cite\"}, {\"key\": \"xia2025survey\", \"file\": \"sections/related_work.tex\", \"line\": 20, \"command\": \"cite\"}, {\"key\": \"hobelsberger2025systematic\", \"file\": \"sections/related_work.tex\", \"line\": 20, \"command\": \"cite\"}, {\"key\": \"xiong2024llm\", \"file\": \"sections/related_work.tex\", \"line\": 20, \"command\": \"citet\"}, {\"key\": \"heo2025uncertainty\", \"file\": \"sections/related_work.tex\", \"line\": 20, \"command\": \"citet\"}, {\"key\": \"kuhn2023semantic\", \"file\": \"sections/related_work.tex\", \"line\": 21, \"command\": \"cite\"}, {\"key\": \"kossen2024semantic\", \"file\": \"sections/related_work.tex\", \"line\": 21, \"command\": \"citet\"}, {\"key\": \"kadavath2022language\", \"file\": \"sections/related_work.tex\", \"line\": 21, \"command\": \"cite\"}, {\"key\": \"malinin2021uncertainty\", \"file\": \"sections/related_work.tex\", \"line\": 21, \"command\": \"citet\"}, {\"key\": \"guo2017calibration\", \"file\": \"sections/related_work.tex\", \"line\": 23, \"command\": \"cite\"}, {\"key\": \"desai2020calibration\", \"file\": \"sections/related_work.tex\", \"line\": 23, \"command\": \"cite\"}, {\"key\": \"lakshminarayanan2017ensembles\", \"file\": \"sections/related_work.tex\", \"line\": 23, \"command\": \"cite\"}, {\"key\": \"gal2016dropout\", \"file\": \"sections/related_work.tex\", \"line\": 23, \"command\": \"cite\"}, {\"key\": \"xiao2019uncertainty\", \"file\": \"sections/related_work.tex\", \"line\": 24, \"command\": \"cite\"}, {\"key\": \"shelmanov2021active\", \"file\": \"sections/related_work.tex\", \"line\": 24, \"command\": \"cite\"}, {\"key\": \"zhang2023ener\", \"file\": \"sections/related_work.tex\", \"line\": 24, \"command\": \"cite\"}, {\"key\": \"kim2024verifiner\", \"file\": \"sections/related_work.tex\", \"line\": 24, \"command\": \"cite\"}, {\"key\": \"he2024uncertainty\", \"file\": \"sections/related_work.tex\", \"line\": 24, \"command\": \"cite\"}, {\"key\": \"fisch2021conformal\", \"file\": \"sections/related_work.tex\", \"line\": 25, \"command\": \"cite\"}, {\"key\": \"angelopoulos2021conformal\", \"file\": \"sections/related_work.tex\", \"line\": 25, \"command\": \"cite\"}, {\"key\": \"cobbe2021verifiers\", \"file\": \"sections/related_work.tex\", \"line\": 25, \"command\": \"cite\"}, {\"key\": \"lightman2024verify\", \"file\": \"sections/related_work.tex\", \"line\": 25, \"command\": \"cite\"}, {\"key\": \"venktesh2025trust\", \"file\": \"sections/related_work.tex\", \"line\": 25, \"command\": \"cite\"}, {\"key\": \"wang2024mathshepherd\", \"file\": \"sections/related_work.tex\", \"line\": 25, \"command\": \"cite\"}, {\"key\": \"eikema2022sampling\", \"file\": \"sections/related_work.tex\", \"line\": 26, \"command\": \"cite\"}, {\"key\": \"freitag2022high\", \"file\": \"sections/related_work.tex\", \"line\": 26, \"command\": \"cite\"}, {\"key\": \"jinnai2024mbr\", \"file\": \"sections/related_work.tex\", \"line\": 26, \"command\": \"cite\"}, {\"key\": \"eikema2025structured\", \"file\": \"sections/related_work.tex\", \"line\": 27, \"command\": \"citet\"}, {\"key\": \"geifman2017selective\", \"file\": \"sections/related_work.tex\", \"line\": 28, \"command\": \"cite\"}, {\"key\": \"culotta2004confidence\", \"file\": \"sections/related_work.tex\", \"line\": 28, \"command\": \"cite\"}, {\"key\": \"willard2023guided\", \"file\": \"sections/method.tex\", \"line\": 5, \"command\": \"cite\"}, {\"key\": \"fleiss1971agreement\", \"file\": \"sections/method.tex\", \"line\": 34, \"command\": \"citet\"}, {\"key\": \"jaccard1901distribution\", \"file\": \"sections/method.tex\", \"line\": 45, \"command\": \"cite\"}, {\"key\": \"luan2018scierc\", \"file\": \"sections/experiments.tex\", \"line\": 9, \"command\": \"cite\"}, {\"key\": \"tjongkimsang2003conll\", \"file\": \"sections/experiments.tex\", \"line\": 10, \"command\": \"cite\"}, {\"key\": \"derczynski2017wnut\", \"file\": \"sections/experiments.tex\", \"line\": 11, \"command\": \"cite\"}, {\"key\": \"zheng2024llamafactory\", \"file\": \"sections/experiments.tex\", \"line\": 14, \"command\": \"cite\"}, {\"key\": \"willard2023guided\", \"file\": \"sections/experiments.tex\", \"line\": 21, \"command\": \"cite\"}, {\"key\": \"kuhn2023semantic\", \"file\": \"sections/experiments.tex\", \"line\": 60, \"command\": \"cite\"}, {\"key\": \"xiong2024llm\", \"file\": \"sections/experiments.tex\", \"line\": 74, \"command\": \"citep\"}, {\"key\": \"brown2024monkeys\", \"file\": \"sections/experiments.tex\", \"line\": 141, \"command\": \"cite\"}, {\"key\": \"snell2025scaling\", \"file\": \"sections/experiments.tex\", \"line\": 141, \"command\": \"cite\"}, {\"key\": \"cobbe2021verifiers\", \"file\": \"sections/experiments.tex\", \"line\": 141, \"command\": \"cite\"}, {\"key\": \"eikema2022sampling\", \"file\": \"sections/discussion.tex\", \"line\": 28, \"command\": \"cite\"}, {\"key\": \"muller2021understanding\", \"file\": \"sections/discussion.tex\", \"line\": 28, \"command\": \"cite\"}, {\"key\": \"freitag2022high\", \"file\": \"sections/discussion.tex\", \"line\": 29, \"command\": \"cite\"}, {\"key\": \"jinnai2024mbr\", \"file\": \"sections/discussion.tex\", \"line\": 29, \"command\": \"cite\"}, {\"key\": \"eikema2025structured\", \"file\": \"sections/discussion.tex\", \"line\": 30, \"command\": \"citet\"}, {\"key\": \"cobbe2021verifiers\", \"file\": \"sections/discussion.tex\", \"line\": 53, \"command\": \"cite\"}, {\"key\": \"venktesh2025trust\", \"file\": \"sections/discussion.tex\", \"line\": 53, \"command\": \"cite\"}, {\"key\": \"brown2024monkeys\", \"file\": \"sections/appendix.tex\", \"line\": 193, \"command\": \"cite\"}, {\"key\": \"snell2025scaling\", \"file\": \"sections/appendix.tex\", \"line\": 193, \"command\": \"cite\"}, {\"key\": \"willard2023guided\", \"file\": \"sections/appendix.tex\", \"line\": 394, \"command\": \"cite\"}], \"online_verification\": [{\"key\": \"angelopoulos2021conformal\", \"title\": \"Uncertainty Sets for Image Classifiers using Conformal Prediction\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Uncertainty Sets for Image Classifiers using Conformal Prediction\", \"matched_year\": \"2020\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"brown2024monkeys\", \"title\": \"Large Language Monkeys: Scaling Inference Compute with Repeated Sampling\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Large Language Monkeys: Scaling Inference Compute with Repeated Sampling\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"chen2024usc\", \"title\": \"Universal Self-Consistency for Large Language Model Generation\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Universal Self-Consistency for Large Language Model Generation\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"cobbe2021verifiers\", \"title\": \"Training Verifiers to Solve Math Word Problems\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Training Verifiers to Solve Math Word Problems\", \"matched_year\": \"2021\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"culotta2004confidence\", \"title\": \"Confidence Estimation for Information Extraction\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Confidence estimation for information extraction\", \"matched_year\": \"2004\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"derczynski2017wnut\", \"title\": \"Results of the WNUT2017 Shared Task on Novel and Emerging Entity Recognition\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Results of the WNUT2017 Shared Task on Novel and Emerging Entity Recognition\", \"matched_year\": \"2017\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"desai2020calibration\", \"title\": \"Calibration of Pre-trained Transformers\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Calibration of Pre-trained Transformers\", \"matched_year\": \"2020\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"eikema2022sampling\", \"title\": \"Sampling-Based Approximations to Minimum Bayes Risk Decoding for Neural Machine Translation\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Sampling-Based Approximations to Minimum Bayes Risk Decoding for Neural Machine Translation\", \"matched_year\": \"2022\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"fisch2021conformal\", \"title\": \"Few-Shot Conformal Prediction with Auxiliary Tasks\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Few-shot Conformal Prediction with Auxiliary Tasks\", \"matched_year\": \"2021\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"freitag2022high\", \"title\": \"High Quality Rather than High Model Probability: Minimum Bayes Risk Decoding with Neural Metrics\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"High Quality Rather than High Model Probability: Minimum Bayes Risk Decoding with Neural Metrics\", \"matched_year\": \"2022\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"he2024uncertainty\", \"title\": \"Uncertainty Estimation on Sequential Labeling via Uncertainty Transmission\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Uncertainty Estimation on Sequential Labeling via Uncertainty Transmission\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"fleiss1971agreement\", \"title\": \"Measuring nominal scale agreement among many raters.\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Measuring nominal scale agreement among many raters.\", \"matched_year\": \"1971\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"gal2016dropout\", \"title\": \"Dropout as a Bayesian Approximation: Representing Model Uncertainty in Deep Learning\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Dropout as a Bayesian Approximation: Representing Model Uncertainty in Deep Learning\", \"matched_year\": \"2015\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"geifman2017selective\", \"title\": \"Selective Classification for Deep Neural Networks\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Selective Classification for Deep Neural Networks\", \"matched_year\": \"2017\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"feng2025optimal\", \"title\": \"Optimal Self-Consistency for Efficient Reasoning with Large Language Models\", \"status\": \"mismatch\", \"confidence\": 1.0, \"matched_title\": \"Optimal Self-Consistency for Efficient Reasoning with Large Language Models\", \"matched_year\": \"2025\", \"mismatch_fields\": [\"first_author: bib=feng vs api=austin\"], \"note\": \"\"}, {\"key\": \"geng2024confidence\", \"title\": \"A Survey of Confidence Estimation and Calibration in Large Language Models\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"A Survey of Confidence Estimation and Calibration in Large Language Models\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"guo2017calibration\", \"title\": \"On Calibration of Modern Neural Networks\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"On Calibration of Modern Neural Networks\", \"matched_year\": \"2017\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"hobelsberger2025systematic\", \"title\": \"Systematic Evaluation of Uncertainty Estimation Methods in Large Language Models\", \"status\": \"not_found\", \"confidence\": 0.236, \"matched_title\": \"A new criterion for assessing discriminant validity in variance-based structural equation modeling\", \"matched_year\": \"\", \"mismatch_fields\": [], \"note\": \"best match similarity 0.24 below threshold 0.82\"}, {\"key\": \"jaccard1901distribution\", \"title\": \"Étude comparative de la distribution florale dans une portion des Alpes et du Jura\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Étude comparative de la distribution florale dans une portion des Alpes et du Jura\", \"matched_year\": \"1901\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"josifoski2022genie\", \"title\": \"GenIE: Generative Information Extraction\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"GenIE: Generative Information Extraction\", \"matched_year\": \"2022\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"kadavath2022language\", \"title\": \"Language Models (Mostly) Know What They Know\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Language Models (Mostly) Know What They Know\", \"matched_year\": \"2022\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"kang2025selfcertainty\", \"title\": \"Scalable Best-of-N Selection for Large Language Models via Self-Certainty\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Scalable Best-of-N Selection for Large Language Models via Self-Certainty\", \"matched_year\": \"2025\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"kim2024verifiner\", \"title\": \"VerifiNER: Verification-augmented NER via Knowledge-grounded Reasoning with Large Language Models\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"VerifiNER: Verification-augmented NER via Knowledge-grounded Reasoning with Large Language Models\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"kim2026reasc\", \"title\": \"Reliability-Aware Adaptive Self-Consistency for Efficient Sampling in LLM Reasoning\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Reliability-Aware Adaptive Self-Consistency for Efficient Sampling in LLM Reasoning\", \"matched_year\": \"2026\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"kossen2024semantic\", \"title\": \"Semantic Entropy Probes: Robust and Cheap Hallucination Detection in LLMs\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Semantic Entropy Probes: Robust and Cheap Hallucination Detection in LLMs\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"li2025llms\", \"title\": \"LLMs Can Generate a Better Answer by Aggregating Their Own Responses\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"LLMs Can Generate a Better Answer by Aggregating Their Own Responses\", \"matched_year\": \"2025\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"kuhn2023semantic\", \"title\": \"Semantic Uncertainty: Linguistic Invariances for Uncertainty Estimation in Natural Language Generation\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Semantic Uncertainty: Linguistic Invariances for Uncertainty Estimation in Natural Language Generation\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"malinin2021uncertainty\", \"title\": \"Uncertainty Estimation in Autoregressive Structured Prediction\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Uncertainty Estimation in Autoregressive Structured Prediction\", \"matched_year\": \"2020\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"lakshminarayanan2017ensembles\", \"title\": \"Simple and Scalable Predictive Uncertainty Estimation using Deep Ensembles\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Simple and Scalable Predictive Uncertainty Estimation using Deep Ensembles\", \"matched_year\": \"2016\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"li2023codeie\", \"title\": \"CodeIE: Large Code Generation Models are Better Few-Shot Information Extractors\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"CodeIE: Large Code Generation Models are Better Few-Shot Information Extractors\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"lightman2024verify\", \"title\": \"Let's Verify Step by Step\", \"status\": \"not_found\", \"confidence\": 0.246, \"matched_title\": \"Development and dosimetric verification of static SHArc: Step‐and‐shoot carbon ion arc therapy for LET &lt;sub>d&lt;/sub> escalation in pancreatic tumors\", \"matched_year\": \"\", \"mismatch_fields\": [], \"note\": \"best match similarity 0.25 below threshold 0.82\"}, {\"key\": \"luan2018scierc\", \"title\": \"Multi-Task Identification of Entities, Relations, and Coreference for Scientific Knowledge Graph Construction\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Multi-Task Identification of Entities, Relations, and Coreference for Scientific Knowledge Graph Construction\", \"matched_year\": \"2018\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"manakul2023selfcheckgpt\", \"title\": \"SelfCheckGPT: Zero-Resource Black-Box Hallucination Detection for Generative Large Language Models\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"SelfCheckGPT: Zero-Resource Black-Box Hallucination Detection for Generative Large Language Models\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"nedellec2026consistency\", \"title\": \"Consistency–accuracy correlation in hard-prompted LLMs for entity and relation extraction: empirical findings from plant-health data\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Consistency–accuracy correlation in hard-prompted LLMs for entity and relation extraction: empirical findings from plant-health data\", \"matched_year\": \"2026\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"oh2025latentsc\", \"title\": \"Latent Self-Consistency for Reliable Majority-Set Selection in Short- and Long-Answer Reasoning\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Latent Self-Consistency for Reliable Majority-Set Selection in Short- and Long-Answer Reasoning\", \"matched_year\": \"2026\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"sainz2024gollie\", \"title\": \"GoLLIE: Annotation Guidelines improve Zero-Shot Information-Extraction\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"GoLLIE: Annotation Guidelines improve Zero-Shot Information-Extraction\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"shelmanov2021active\", \"title\": \"Active Learning for Sequence Tagging with Deep Pre-trained Models and Bayesian Uncertainty Estimates\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Active Learning for Sequence Tagging with Deep Pre-trained Models and Bayesian Uncertainty Estimates\", \"matched_year\": \"2021\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"snell2025scaling\", \"title\": \"Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters\", \"status\": \"mismatch\", \"confidence\": 1.0, \"matched_title\": \"Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters\", \"matched_year\": \"2024\", \"mismatch_fields\": [\"first_author: bib=snell vs api=charlie\"], \"note\": \"\"}, {\"key\": \"taubenfeld2025cisc\", \"title\": \"Confidence Improves Self-Consistency in LLMs\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Confidence Improves Self-Consistency in LLMs\", \"matched_year\": \"2025\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"thirukovalluru2024atomic\", \"title\": \"Atomic Self-Consistency for Better Long Form Generations\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Atomic Self-Consistency for Better Long Form Generations\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"tjongkimsang2003conll\", \"title\": \"Introduction to the CoNLL-2003 Shared Task: Language-Independent Named Entity Recognition\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Introduction to the CoNLL-2003 Shared Task: Language-Independent Named Entity Recognition\", \"matched_year\": \"2003\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"vashurin2025cocoa\", \"title\": \"Uncertainty Quantification for LLMs through Minimum Bayes Risk: Bridging Confidence and Consistency\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Uncertainty Quantification for LLMs through Minimum Bayes Risk: Bridging Confidence and Consistency\", \"matched_year\": \"2025\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"wadhwa2023revisiting\", \"title\": \"Revisiting Relation Extraction in the era of Large Language Models\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Revisiting Relation Extraction in the era of Large Language Models\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"wang2023instructuie\", \"title\": \"InstructUIE: Multi-task Instruction Tuning for Unified Information Extraction\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"InstructUIE: Multi-task Instruction Tuning for Unified Information Extraction\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"wang2023selfconsistency\", \"title\": \"Self-Consistency Improves Chain of Thought Reasoning in Language Models\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Self-Consistency Improves Chain of Thought Reasoning in Language Models\", \"matched_year\": \"2022\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"wang2025make\", \"title\": \"Make Every Penny Count: Difficulty-Adaptive Self-Consistency for Cost-Efficient Reasoning\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Make Every Penny Count: Difficulty-Adaptive Self-Consistency for Cost-Efficient Reasoning\", \"matched_year\": \"2025\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"wang2024mathshepherd\", \"title\": \"Math-Shepherd: Verify and Reinforce LLMs Step-by-step without Human Annotations\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Math-Shepherd: Verify and Reinforce LLMs Step-by-step without Human Annotations\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"wang2025rankedvoting\", \"title\": \"Ranked Voting based Self-Consistency of Large Language Models\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Ranked Voting based Self-Consistency of Large Language Models\", \"matched_year\": \"2025\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"wen2025know\", \"title\": \"Know Your Limits: A Survey of Abstention in Large Language Models\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Know Your Limits: A Survey of Abstention in Large Language Models\", \"matched_year\": \"2025\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"willard2023guided\", \"title\": \"Efficient Guided Generation for Large Language Models\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Efficient Guided Generation for Large Language Models\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"xia2025survey\", \"title\": \"A Survey of Uncertainty Estimation Methods on Large Language Models\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"A Survey of Uncertainty Estimation Methods on Large Language Models\", \"matched_year\": \"2025\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"xiao2019uncertainty\", \"title\": \"Quantifying Uncertainties in Natural Language Processing Tasks\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Quantifying Uncertainties in Natural Language Processing Tasks\", \"matched_year\": \"2019\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"zhang2023ener\", \"title\": \"E-NER: Evidential Deep Learning for Trustworthy Named Entity Recognition\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"E-NER: Evidential Deep Learning for Trustworthy Named Entity Recognition\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"zheng2024llamafactory\", \"title\": \"LlamaFactory: Unified Efficient Fine-Tuning of 100+ Language Models\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"LlamaFactory: Unified Efficient Fine-Tuning of 100+ Language Models\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"zhou2024uniner\", \"title\": \"UniversalNER: Targeted Distillation from Large Language Models for Open Named Entity Recognition\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"UniversalNER: Targeted Distillation from Large Language Models for Open Named Entity Recognition\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"xiong2024llm\", \"title\": \"Can LLMs Express Their Uncertainty? An Empirical Evaluation of Confidence Elicitation in LLMs\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Can LLMs Express Their Uncertainty? An Empirical Evaluation of Confidence Elicitation in LLMs\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"muller2021understanding\", \"title\": \"Understanding the Properties of Minimum Bayes Risk Decoding in Neural Machine Translation\", \"status\": \"mismatch\", \"confidence\": 1.0, \"matched_title\": \"Understanding the Properties of Minimum Bayes Risk Decoding in Neural Machine Translation\", \"matched_year\": \"2021\", \"mismatch_fields\": [\"first_author: bib=m\\\\\\\"uller vs api=müller\"], \"note\": \"\"}, {\"key\": \"heo2025uncertainty\", \"title\": \"Do LLMs Estimate Uncertainty Well in Instruction Following?\", \"status\": \"verified\", \"confidence\": 0.983, \"matched_title\": \"Do LLMs estimate uncertainty well in instruction-following?\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"eikema2025structured\", \"title\": \"Structure-Conditional Minimum Bayes Risk Decoding\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Structure-Conditional Minimum Bayes Risk Decoding\", \"matched_year\": \"2025\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"zhang2025tts\", \"title\": \"A Survey on Test-Time Scaling in Large Language Models: What, How, Where, and How Well?\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"A Survey on Test-Time Scaling in Large Language Models: What, How, Where, and How Well?\", \"matched_year\": \"2025\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"venktesh2025trust\", \"title\": \"Trust but Verify! A Survey on Verification Design for Test-time Scaling\", \"status\": \"not_found\", \"confidence\": 0.252, \"matched_title\": \"The PRISMA Statement for Reporting Systematic Reviews and Meta-Analyses of Studies That Evaluate Health Care Interventions: Explanation and Elaboration\", \"matched_year\": \"\", \"mismatch_fields\": [], \"note\": \"best match similarity 0.25 below threshold 0.82\"}, {\"key\": \"jinnai2024mbr\", \"title\": \"Model-Based Minimum Bayes Risk Decoding for Text Generation\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Model-Based Minimum Bayes Risk Decoding for Text Generation\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}]}, \"error\": null, \"metadata\": {}}"
    }
  },
  "sourceToolAssistantUUID": "aa8ec23c-6356-49c8-ab88-f0e2b2582083",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "f49c1ccb-97a0-4961-857d-2db0aa0e0624",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 56_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[Round 1 审稿请求]: ## Round 1 审稿任务 — Reviewer 2  **你的侧重**：新颖性 + 定位完整性 + 写作质量 + 格式合规  ### 投稿信息 - **目标 venue**: EMNLP 2026 Findings (ARR May cycle) - **Deadline**: 2026-05-25 - **格式**: ACL template, 长文 8 页…",
  "leafUuid": "537f1b98-09b2-4241-842e-9bec3075f6f4",
  "sessionId": "f49c1ccb-97a0-4961-857d-2db0aa0e0624"
}
```

---

### Runtime record

_source line 57_

```json
{
  "type": "ai-title",
  "aiTitle": "Round 1 review for EMNLP 2026 structured IE paper",
  "sessionId": "f49c1ccb-97a0-4961-857d-2db0aa0e0624"
}
```

---

### Tool result

_source line 58 · 2026-05-15T15:01:24.060Z_

<details><summary>↩ Tool result · `toolu_01EqJjxmBCfpbzezVriGWSsG`</summary>

```text
# ARR Reviewer Guidelines: Complete Summary

## Core Evaluation Framework

ARR reviewers assess papers across three dimensions:

**Soundness**: Technical rigor and validity of methodology, evidence, and arguments. As the guidelines state, "low soundness scores must be justified by the text of the review."

**Excitement**: Personal interest and engagement with the work, independent of soundness assessment. This reflects subjective taste rather than objective quality.

**Overall Assessment**: A composite recommendation balancing soundness, excitement, novelty, and potential impact. Papers recommended for both Findings and main conferences "are expected to be sufficiently sound and reproducible."

## What to Evaluate

### Required Tasks

1. **Assignment Check**: Verify expertise match and absence of conflicts of interest. Skim the paper to confirm qualification.

2. **Desk-Rejection Checklist**: Screen for appropriateness, hallucinated references, anonymity violations, format violations, missing limitations sections, ethics issues, and dual submissions.

3. **Two-Stage Reading**:
   - Skim reading: Understand research question and contribution scope *before* examining results
   - In-depth reading: Evaluate technical soundness, evidence quality, and novelty

4. **Related Work Review**: Search for prior work *after* forming initial impressions to avoid confirmation bias.

## How to Write Strong Reviews

### Specificity (I1)

Avoid vague criticisms. Instead of "missing relevant references," specify which ones: "missing references X, Y, Z." Replace generic statements like "unclear" with precise descriptions: "Y and Z missing from description of X."

### Common Review Pitfalls (I2, I10)

The guidelines identify 17 problematic heuristics to avoid:

- **H1**: Dismissing findings as "unsurprising" despite lacking prior empirical validation
- **H3**: Rejecting work as "not novel" without providing specific references
- **H5**: Penalizing papers lacking state-of-the-art results when SOTA isn't claimed
- **H6**: Bias against negative results despite their scientific value
- **H7**: Criticizing simplicity when elegance is preferable
- **H8**: Expecting deep learning in interdisciplinary NLP work
- **H9**: Dismissing niche topics in main track submissions
- **H13-H15**: Requesting experiments beyond the paper's core claims

### Common NLP Paper Problems (M, T, R, G codes)

**Methodology Issues (M)**:
- LLM evaluation without validation in context
- Insufficient reproducibility details
- Undisclosed data quality issues
- Unmotivated model/benchmark selection
- Incomplete proofs or assumptions

**Results Issues (R)**:
- Statistical errors or p-hacking
- Claims exceeding evaluated scope
- Speculation presented as conclusions
- Overclaiming or misleading framing
- Missing statistical significance assessment

**General Issues (G)**:
- Unclear research questions or contributions
- Reliance on unsound precedents
- Misrepresented or missing related work
- Poorly defined terminology
- Misleading citations

### Tone and Professionalism (I4)

Reviews must be professional and constructive. The guidelines emphasize: "Write the review you would like to get yourself." Sarcasm and dismissiveness harm authors' mental health and diminish peer review's collaborative spirit.

## Scoring Standards

### Soundness-Score Alignment

Soundness scores must correlate with specific identified flaws. Low scores without justification suggest unconscious bias or unexamined heuristics from the problematic list above.

### Excitement vs. Soundness

A paper can be technically sound yet personally uninteresting, or compelling but with limitations. These dimensions are orthogonal and should be scored independently.

### What Merits Acceptance

**Findings-worthy papers** demonstrate technical soundness and reproducibility. **Main conference papers** additionally require excitement and impact potential. Contributions like efficiency improvements or resources for underserved languages merit acceptance despite limited novelty if impact potential is significant.

## Post-Review Engagement

### Author Response Phase (I11)

Reviewers should acknowledge author responses and update assessments when concerns are addressed. If unconvinced, explain why: "the authors responded, but issue X remains unresolved because [reason]."

### Resubmission Reviewing

- **Repeat reviewers** assess whether revisions adequately addressed previous concerns; avoid raising new issues
- **Substitute reviewers** categorize new concerns as: (i) unaddressed prior weaknesses, (ii) critical soundness issues, or (iii) improvement suggestions
- **Fresh reviewers** form independent assessments, then check if revisions addressed previously identified problems

## Special Considerations

### Generative AI Use

Reviewers may not use AI to generate review drafts but may use it for language refinement (especially for non-native speakers) or proof-checking. Uploading manuscripts or reviews to non-privacy-preserving AI tools violates confidentiality.

### Anonymity

Reviewers should not actively search for author identity. If discovered, disclose this to area chairs via the review form. Postpone related-work searches until after forming initial impressions.

### Desk-Rejection Grounds

Papers require desk rejection for: format/length violations, missing limitations sections, egregious anonymity violations, hallucinated references, or severe responsible NLP checklist violations indicating disengagement.

## Recognition and Accountability

Starting May 2025, ARR recognizes "great reviewers" through public conference lists and potential free virtual registration. Conversely, "highly irresponsible" reviewers submitting terse reviews, unprofessional content, or LLM-generated work may face desk rejection of their own submissions and ineligibility for subsequent cycles.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a3c25a5f-9db7-4d02-bc8a-65e864df685e",
  "isSidechain": false,
  "promptId": "a8cee1eb-a5df-415d-8e30-c85446d1e0a7",
  "type": "user",
  "uuid": "33b6281f-03ed-4996-9655-21d0d142b699",
  "toolUseResult": {
    "bytes": 100603,
    "code": 200,
    "codeText": "OK",
    "result": "# ARR Reviewer Guidelines: Complete Summary\n\n## Core Evaluation Framework\n\nARR reviewers assess papers across three dimensions:\n\n**Soundness**: Technical rigor and validity of methodology, evidence, and arguments. As the guidelines state, \"low soundness scores must be justified by the text of the review.\"\n\n**Excitement**: Personal interest and engagement with the work, independent of soundness assessment. This reflects subjective taste rather than objective quality.\n\n**Overall Assessment**: A composite recommendation balancing soundness, excitement, novelty, and potential impact. Papers recommended for both Findings and main conferences \"are expected to be sufficiently sound and reproducible.\"\n\n## What to Evaluate\n\n### Required Tasks\n\n1. **Assignment Check**: Verify expertise match and absence of conflicts of interest. Skim the paper to confirm qualification.\n\n2. **Desk-Rejection Checklist**: Screen for appropriateness, hallucinated references, anonymity violations, format violations, missing limitations sections, ethics issues, and dual submissions.\n\n3. **Two-Stage Reading**:\n   - Skim reading: Understand research question and contribution scope *before* examining results\n   - In-depth reading: Evaluate technical soundness, evidence quality, and novelty\n\n4. **Related Work Review**: Search for prior work *after* forming initial impressions to avoid confirmation bias.\n\n## How to Write Strong Reviews\n\n### Specificity (I1)\n\nAvoid vague criticisms. Instead of \"missing relevant references,\" specify which ones: \"missing references X, Y, Z.\" Replace generic statements like \"unclear\" with precise descriptions: \"Y and Z missing from description of X.\"\n\n### Common Review Pitfalls (I2, I10)\n\nThe guidelines identify 17 problematic heuristics to avoid:\n\n- **H1**: Dismissing findings as \"unsurprising\" despite lacking prior empirical validation\n- **H3**: Rejecting work as \"not novel\" without providing specific references\n- **H5**: Penalizing papers lacking state-of-the-art results when SOTA isn't claimed\n- **H6**: Bias against negative results despite their scientific value\n- **H7**: Criticizing simplicity when elegance is preferable\n- **H8**: Expecting deep learning in interdisciplinary NLP work\n- **H9**: Dismissing niche topics in main track submissions\n- **H13-H15**: Requesting experiments beyond the paper's core claims\n\n### Common NLP Paper Problems (M, T, R, G codes)\n\n**Methodology Issues (M)**:\n- LLM evaluation without validation in context\n- Insufficient reproducibility details\n- Undisclosed data quality issues\n- Unmotivated model/benchmark selection\n- Incomplete proofs or assumptions\n\n**Results Issues (R)**:\n- Statistical errors or p-hacking\n- Claims exceeding evaluated scope\n- Speculation presented as conclusions\n- Overclaiming or misleading framing\n- Missing statistical significance assessment\n\n**General Issues (G)**:\n- Unclear research questions or contributions\n- Reliance on unsound precedents\n- Misrepresented or missing related work\n- Poorly defined terminology\n- Misleading citations\n\n### Tone and Professionalism (I4)\n\nReviews must be professional and constructive. The guidelines emphasize: \"Write the review you would like to get yourself.\" Sarcasm and dismissiveness harm authors' mental health and diminish peer review's collaborative spirit.\n\n## Scoring Standards\n\n### Soundness-Score Alignment\n\nSoundness scores must correlate with specific identified flaws. Low scores without justification suggest unconscious bias or unexamined heuristics from the problematic list above.\n\n### Excitement vs. Soundness\n\nA paper can be technically sound yet personally uninteresting, or compelling but with limitations. These dimensions are orthogonal and should be scored independently.\n\n### What Merits Acceptance\n\n**Findings-worthy papers** demonstrate technical soundness and reproducibility. **Main conference papers** additionally require excitement and impact potential. Contributions like efficiency improvements or resources for underserved languages merit acceptance despite limited novelty if impact potential is significant.\n\n## Post-Review Engagement\n\n### Author Response Phase (I11)\n\nReviewers should acknowledge author responses and update assessments when concerns are addressed. If unconvinced, explain why: \"the authors responded, but issue X remains unresolved because [reason].\"\n\n### Resubmission Reviewing\n\n- **Repeat reviewers** assess whether revisions adequately addressed previous concerns; avoid raising new issues\n- **Substitute reviewers** categorize new concerns as: (i) unaddressed prior weaknesses, (ii) critical soundness issues, or (iii) improvement suggestions\n- **Fresh reviewers** form independent assessments, then check if revisions addressed previously identified problems\n\n## Special Considerations\n\n### Generative AI Use\n\nReviewers may not use AI to generate review drafts but may use it for language refinement (especially for non-native speakers) or proof-checking. Uploading manuscripts or reviews to non-privacy-preserving AI tools violates confidentiality.\n\n### Anonymity\n\nReviewers should not actively search for author identity. If discovered, disclose this to area chairs via the review form. Postpone related-work searches until after forming initial impressions.\n\n### Desk-Rejection Grounds\n\nPapers require desk rejection for: format/length violations, missing limitations sections, egregious anonymity violations, hallucinated references, or severe responsible NLP checklist violations indicating disengagement.\n\n## Recognition and Accountability\n\nStarting May 2025, ARR recognizes \"great reviewers\" through public conference lists and potential free virtual registration. Conversely, \"highly irresponsible\" reviewers submitting terse reviews, unprofessional content, or LLM-generated work may face desk rejection of their own submissions and ineligibility for subsequent cycles.",
    "durationMs": 17989,
    "url": "https://aclrollingreview.org/reviewerguidelines"
  },
  "sourceToolAssistantUUID": "a3c25a5f-9db7-4d02-bc8a-65e864df685e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "f49c1ccb-97a0-4961-857d-2db0aa0e0624",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 59 · 2026-05-15T15:01:26.989Z_

<details><summary>Logged reasoning block</summary>

```text
Now let me read the full reference verification output to check for any issues.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "33b6281f-03ed-4996-9655-21d0d142b699",
  "isSidechain": false,
  "requestId": "req_011Cb4ZBdANmk8GWQ6YrfQCx",
  "type": "assistant",
  "uuid": "80a22531-6bd6-4295-ae0a-46d8dc991580",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "f49c1ccb-97a0-4961-857d-2db0aa0e0624",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AALqcpUZVdm32bCfdADTmN",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 48149,
      "cache_read_input_tokens": 32396,
      "output_tokens": 249,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 48149,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 249,
          "cache_read_input_tokens": 32396,
          "cache_creation_input_tokens": 48149,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 48149
          },
          "type": "message"
        }
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

_source line 60 · 2026-05-15T15:01:27.483Z_

引用验证完成。让我读取详细结果。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "80a22531-6bd6-4295-ae0a-46d8dc991580",
  "isSidechain": false,
  "requestId": "req_011Cb4ZBdANmk8GWQ6YrfQCx",
  "type": "assistant",
  "uuid": "003aae00-c8d8-4657-8b11-26a4b0b189fe",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "f49c1ccb-97a0-4961-857d-2db0aa0e0624",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AALqcpUZVdm32bCfdADTmN",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 48149,
      "cache_read_input_tokens": 32396,
      "output_tokens": 249,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 48149,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 249,
          "cache_read_input_tokens": 32396,
          "cache_creation_input_tokens": 48149,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 48149
          },
          "type": "message"
        }
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

_source line 61 · 2026-05-15T15:01:28.784Z_

<details open><summary>🔧 Tool call — Read · `toolu_01CEdSaBSA7tkKvv4nUjuNuk`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie--claude-sessions-review-reviewer-2-a0c838f5/f49c1ccb-97a0-4961-857d-2db0aa0e0624/tool-results/toolu_01EyB9T3fkAJQ5ufKg9cmgPX.txt",
  "offset": 0,
  "limit": 100
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "003aae00-c8d8-4657-8b11-26a4b0b189fe",
  "isSidechain": false,
  "requestId": "req_011Cb4ZBdANmk8GWQ6YrfQCx",
  "type": "assistant",
  "uuid": "c9cfc4f5-7d7c-4bfa-8311-9dd65f7496d0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "f49c1ccb-97a0-4961-857d-2db0aa0e0624",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AALqcpUZVdm32bCfdADTmN",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 48149,
      "cache_read_input_tokens": 32396,
      "output_tokens": 249,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 48149,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 249,
          "cache_read_input_tokens": 32396,
          "cache_creation_input_tokens": 48149,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 48149
          },
          "type": "message"
        }
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

_source line 62 · 2026-05-15T15:01:29.163Z_

<details><summary>↩ Tool result · `toolu_01CEdSaBSA7tkKvv4nUjuNuk`</summary>

```text
0	{"result":"{\"success\": true, \"data\": {\"summary\": {\"total_bib_entries\": 62, \"total_citations\": 94, \"unique_cited_keys\": 62, \"orphan_bib\": 0, \"missing_bib\": 0, \"duplicate_keys\": 0, \"online_verified\": 56, \"online_not_found\": 3, \"online_mismatch\": 3}, \"cross_check\": {\"orphan_bib\": [], \"missing_bib\": [], \"orphan_count\": 0, \"missing_count\": 0}, \"bib_entries\": [{\"key\": \"angelopoulos2021conformal\", \"type\": \"inproceedings\", \"title\": \"Uncertainty Sets for Image Classifiers using Conformal Prediction\", \"authors\": \"Angelopoulos, Anastasios N. and Bates, Stephen and Malik, Jitendra and Jordan, M...\", \"year\": \"2021\", \"venue\": \"ICLR 2021\"}, {\"key\": \"brown2024monkeys\", \"type\": \"article\", \"title\": \"Large Language Monkeys: Scaling Inference Compute with Repeated Sampling\", \"authors\": \"Brown, Bradley and Juravsky, Jordan and Ehrlich, Ryan and Clark, Ronald and Le, ...\", \"year\": \"2024\", \"venue\": \"arXiv preprint arXiv:2407.21787\"}, {\"key\": \"chen2024usc\", \"type\": \"inproceedings\", \"title\": \"Universal Self-Consistency for Large Language Model Generation\", \"authors\": \"Chen, Xinyun and Aksitov, Renat and Alon, Uri and Ren, Jie and Xiao, Kefan and Y...\", \"year\": \"2024\", \"venue\": \"arXiv preprint (ICML 2024 Workshop ICL)\"}, {\"key\": \"cobbe2021verifiers\", \"type\": \"article\", \"title\": \"Training Verifiers to Solve Math Word Problems\", \"authors\": \"Cobbe, Karl and Kosaraju, Vineet and Bavarian, Mohammad and Chen, Mark and Jun, ...\", \"year\": \"2021\", \"venue\": \"arXiv preprint arXiv:2110.14168\"}, {\"key\": \"culotta2004confidence\", \"type\": \"inproceedings\", \"title\": \"Confidence Estimation for Information Extraction\", \"authors\": \"Culotta, Aron and McCallum, Andrew\", \"year\": \"2004\", \"venue\": \"HLT-NAACL 2004\"}, {\"key\": \"derczynski2017wnut\", \"type\": \"inproceedings\", \"title\": \"Results of the WNUT2017 Shared Task on Novel and Emerging Entity Recognition\", \"authors\": \"Derczynski, Leon and Nichols, Eric and Erp, Marieke van and Limsopatham, Nut\", \"year\": \"2017\", \"venue\": \"W-NUT Workshop at EMNLP 2017\"}, {\"key\": \"desai2020calibration\", \"type\": \"inproceedings\", \"title\": \"Calibration of Pre-trained Transformers\", \"authors\": \"Desai, Shrey and Durrett, Greg\", \"year\": \"2020\", \"venue\": \"Proceedings of the 2020 Conference on Empirical Methods in Natural Language Proc...\"}, {\"key\": \"eikema2022sampling\", \"type\": \"inproceedings\", \"title\": \"Sampling-Based Approximations to Minimum Bayes Risk Decoding for Neural Machine Translation\", \"authors\": \"Eikema, Bryan and Aziz, Wilker\", \"year\": \"2022\", \"venue\": \"Proceedings of the 2022 Conference on Empirical Methods in Natural Language Proc...\"}, {\"key\": \"fisch2021conformal\", \"type\": \"inproceedings\", \"title\": \"Few-Shot Conformal Prediction with Auxiliary Tasks\", \"authors\": \"Fisch, Adam and Schuster, Tal and Jaakkola, Tommi and Barzilay, Regina\", \"year\": \"2021\", \"venue\": \"ICML 2021\"}, {\"key\": \"freitag2022high\", \"type\": \"article\", \"title\": \"High Quality Rather than High Model Probability: Minimum Bayes Risk Decoding with Neural Metrics\", \"authors\": \"Freitag, Markus and Grangier, David and Tan, Qijun and Liang, Bowen\", \"year\": \"2022\", \"venue\": \"Transactions of the Association for Computational Linguistics\"}, {\"key\": \"he2024uncertainty\", \"type\": \"inproceedings\", \"title\": \"Uncertainty Estimation on Sequential Labeling via Uncertainty Transmission\", \"authors\": \"He, Jianfeng and Yu, Linlin and Lei, Shuo and Lu, Chang-Tien and Chen, Feng\", \"year\": \"2024\", \"venue\": \"Findings of the Association for Computational Linguistics: NAACL 2024\"}, {\"key\": \"fleiss1971agreement\", \"type\": \"article\", \"title\": \"Measuring nominal scale agreement among many raters.\", \"authors\": \"Fleiss, Joseph L.\", \"year\": \"1971\", \"venue\": \"Psychological Bulletin\"}, {\"key\": \"gal2016dropout\", \"type\": \"inproceedings\", \"title\": \"Dropout as a Bayesian Approximation: Representing Model Uncertainty in Deep Learning\", \"authors\": \"Gal, Yarin and Ghahramani, Zoubin\", \"year\": \"2016\", \"venue\": \"ICML 2016\"}, {\"key\": \"geifman2017selective\", \"type\": \"inproceedings\", \"title\": \"Selective Classification for Deep Neural Networks\", \"authors\": \"Geifman, Yonatan and El-Yaniv, Ran\", \"year\": \"2017\", \"venue\": \"NeurIPS 2017\"}, {\"key\": \"feng2025optimal\", \"type\": \"article\", \"title\": \"Optimal Self-Consistency for Efficient Reasoning with Large Language Models\", \"authors\": \"Feng, Austin and Alonso, Marius and Odonnat, Ambroise\", \"year\": \"2025\", \"venue\": \"arXiv preprint arXiv:2511.12309\"}, {\"key\": \"geng2024confidence\", \"type\": \"inproceedings\", \"title\": \"A Survey of Confidence Estimation and Calibration in Large Language Models\", \"authors\": \"Geng, Jiahui and Cai, Fengyu and Wang, Yuxia and Koeppl, Heinz and Nakov, Presla...\", \"year\": \"2024\", \"venue\": \"Proceedings of the 2024 Conference of the North American Chapter of the Associat...\"}, {\"key\": \"guo2017calibration\", \"type\": \"inproceedings\", \"title\": \"On Calibration of Modern Neural Networks\", \"authors\": \"Guo, Chuan and Pleiss, Geoff and Sun, Yu and Weinberger, Kilian Q.\", \"year\": \"2017\", \"venue\": \"ICML 2017\"}, {\"key\": \"hobelsberger2025systematic\", \"type\": \"article\", \"title\": \"Systematic Evaluation of Uncertainty Estimation Methods in Large Language Models\", \"authors\": \"Hobelsberger, Christian and Winner, Theresa and Nawroth, Andreas and Mitevski, O...\", \"year\": \"2025\", \"venue\": \"arXiv preprint arXiv:2510.20460\"}, {\"key\": \"jaccard1901distribution\", \"type\": \"article\", \"title\": \"Étude comparative de la distribution florale dans une portion des Alpes et du Jura\", \"authors\": \"Jaccard, Paul\", \"year\": \"1901\", \"venue\": \"Bulletin de la Société Vaudoise des Sciences Naturelles\"}, {\"key\": \"josifoski2022genie\", \"type\": \"inproceedings\", \"title\": \"GenIE: Generative Information Extraction\", \"authors\": \"Josifoski, Martin and De Cao, Nicola and Peyrard, Maxime and Petroni, Fabio and ...\", \"year\": \"2022\", \"venue\": \"Proceedings of the 2022 Conference of the North American Chapter of the Associat...\"}, {\"key\": \"kadavath2022language\", \"type\": \"article\", \"title\": \"Language Models (Mostly) Know What They Know\", \"authors\": \"Kadavath, Saurav and Conerly, Tom and Askell, Amanda and Henighan, Tom and Drain...\", \"year\": \"2022\", \"venue\": \"arXiv preprint arXiv:2207.05221\"}, {\"key\": \"kang2025selfcertainty\", \"type\": \"inproceedings\", \"title\": \"Scalable Best-of-N Selection for Large Language Models via Self-Certainty\", \"authors\": \"Kang, Zhewei and Zhao, Xuandong and Song, Dawn\", \"year\": \"2025\", \"venue\": \"NeurIPS 2025\"}, {\"key\": \"kim2024verifiner\", \"type\": \"inproceedings\", \"title\": \"VerifiNER: Verification-augmented NER via Knowledge-grounded Reasoning with Large Language Models\", \"authors\": \"Kim, Seoyeon and Seo, Kwangwook and Chae, Hyungjoo and Yeo, Jinyoung and Lee, Do...\", \"year\": \"2024\", \"venue\": \"Proceedings of the 62nd Annual Meeting of the Association for Computational Ling...\"}, {\"key\": \"kim2026reasc\", \"type\": \"inproceedings\", \"title\": \"Reliability-Aware Adaptive Self-Consistency for Efficient Sampling in LLM Reasoning\", \"authors\": \"Kim, Junseok and Yang, Nakyeong and Min, Kyungmin and Jung, Kyomin\", \"year\": \"2026\", \"venue\": \"ACL 2026\"}, {\"key\": \"kossen2024semantic\", \"type\": \"article\", \"title\": \"Semantic Entropy Probes: Robust and Cheap Hallucination Detection in LLMs\", \"authors\": \"Kossen, Jannik and Han, Jiatong and Razzak, Muhammed and Schut, Lisa and Malik, ...\", \"year\": \"2024\", \"venue\": \"arXiv preprint arXiv:2406.15927\"}, {\"key\": \"li2025llms\", \"type\": \"article\", \"title\": \"LLMs Can Generate a Better Answer by Aggregating Their Own Responses\", \"authors\": \"Li, Zichong and Feng, Xinyu and Cai, Yuheng and Zhang, Zixuan and Liu, Tianyi an...\", \"year\": \"2025\", \"venue\": \"arXiv preprint arXiv:2503.04104\"}, {\"key\": \"kuhn2023semantic\", \"type\": \"inproceedings\", \"title\": \"Semantic Uncertainty: Linguistic Invariances for Uncertainty Estimation in Natural Language Generation\", \"authors\": \"Kuhn, Lorenz and Gal, Yarin and Farquhar, Sebastian\", \"year\": \"2023\", \"venue\": \"ICLR 2023\"}, {\"key\": \"malinin2021uncertainty\", \"type\": \"inproceedings\", \"title\": \"Uncertainty Estimation in Autoregressive Structured Prediction\", \"authors\": \"Malinin, Andrey and Gales, Mark\", \"year\": \"2021\", \"venue\": \"International Conference on Learning Representations\"}, {\"key\": \"lakshminarayanan2017ensembles\", \"type\": \"inproceedings\", \"title\": \"Simple and Scalable Predictive Uncertainty Estimation using Deep Ensembles\", \"authors\": \"Lakshminarayanan, Balaji and Pritzel, Alexander and Blundell, Charles\", \"year\": \"2017\", \"venue\": \"NeurIPS 2017\"}, {\"key\": \"li2023codeie\", \"type\": \"inproceedings\", \"title\": \"CodeIE: Large Code Generation Models are Better Few-Shot Information Extractors\", \"authors\": \"Li, Peng and Sun, Tianxiang and Tang, Qiong and Yan, Hang and Wu, Yuanbin and Hu...\", \"year\": \"2023\", \"venue\": \"Proceedings of the 61st Annual Meeting of the Association for Computational Ling...\"}, {\"key\": \"lightman2024verify\", \"type\": \"inproceedings\", \"title\": \"Let's Verify Step by Step\", \"authors\": \"Lightman, Hunter and Kosaraju, Vineet and Burda, Yura and Edwards, Harri and Bak...\", \"year\": \"2024\", \"venue\": \"ICLR 2024\"}, {\"key\": \"luan2018scierc\", \"type\": \"inproceedings\", \"title\": \"Multi-Task Identification of Entities, Relations, and Coreference for Scientific Knowledge Graph Construction\", \"authors\": \"Luan, Yi and He, Luheng and Ostendorf, Mari and Hajishirzi, Hannaneh\", \"year\": \"2018\", \"venue\": \"Proceedings of the 2018 Conference on Empirical Methods in Natural Language Proc...\"}, {\"key\": \"manakul2023selfcheckgpt\", \"type\": \"inproceedings\", \"title\": \"SelfCheckGPT: Zero-Resource Black-Box Hallucination Detection for Generative Large Language Models\", \"authors\": \"Manakul, Potsawee and Liusie, Adian and Gales, Mark\", \"year\": \"2023\", \"venue\": \"Proceedings of the 2023 Conference on Empirical Methods in Natural Language Proc...\"}, {\"key\": \"nedellec2026consistency\", \"type\": \"article\", \"title\": \"Consistency–accuracy correlation in hard-prompted LLMs for entity and relation extraction: empirical findings from plant...\", \"authors\": \"Yao, Xinzhi and Nédellec, Claire and Xia, Jingbo and Bossy, Robert\", \"year\": \"2026\", \"venue\": \"Genomics \\\\& Informatics\"}, {\"key\": \"oh2025latentsc\", \"type\": \"article\", \"title\": \"Latent Self-Consistency for Reliable Majority-Set Selection in Short- and Long-Answer Reasoning\", \"authors\": \"Oh, Jungsuk and Lee, Jay-Yoon\", \"year\": \"2025\", \"venue\": \"arXiv preprint arXiv:2508.18395\"}, {\"key\": \"sainz2024gollie\", \"type\": \"inproceedings\", \"title\": \"GoLLIE: Annotation Guidelines improve Zero-Shot Information-Extraction\", \"authors\": \"Sainz, Oscar and García-Ferrero, Iker and Agerri, Rodrigo and Lacalle, Oier Lope...\", \"year\": \"2024\", \"venue\": \"ICLR 2024\"}, {\"key\": \"shelmanov2021active\", \"type\": \"inproceedings\", \"title\": \"Active Learning for Sequence Tagging with Deep Pre-trained Models and Bayesian Uncertainty Estimates\", \"authors\": \"Shelmanov, Artem and Puzyrev, Dmitri and Kupriyanova, Lyubov and Belyakov, Denis...\", \"year\": \"2021\", \"venue\": \"Proceedings of the 16th Conference of the European Chapter of the Association fo...\"}, {\"key\": \"snell2025scaling\", \"type\": \"inproceedings\", \"title\": \"Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters\", \"authors\": \"Snell, Charlie and Lee, Jaehoon and Xu, Kelvin and Kumar, Aviral\", \"year\": \"2025\", \"venue\": \"Proceedings of the International Conference on Learning Representations (ICLR)\"}, {\"key\": \"taubenfeld2025cisc\", \"type\": \"inproceedings\", \"title\": \"Confidence Improves Self-Consistency in LLMs\", \"authors\": \"Taubenfeld, Amir and Sheffer, Tom and Ofek, Eran and Feder, Amir and Goldstein, ...\", \"year\": \"2025\", \"venue\": \"Findings of the Association for Computational Linguistics: ACL 2025\"}, {\"key\": \"thirukovalluru2024atomic\", \"type\": \"inproceedings\", \"title\": \"Atomic Self-Consistency for Better Long Form Generations\", \"authors\": \"Thirukovalluru, Raghuveer and Huang, Yukun and Dhingra, Bhuwan\", \"year\": \"2024\", \"venue\": \"Proceedings of the 2024 Conference on Empirical Methods in Natural Language Proc...\"}, {\"key\": \"tjongkimsang2003conll\", \"type\": \"inproceedings\", \"title\": \"Introduction to the CoNLL-2003 Shared Task: Language-Independent Named Entity Recognition\", \"authors\": \"Sang, Erik F. Tjong Kim and Meulder, Fien De\", \"year\": \"2003\", \"venue\": \"CoNLL 2003\"}, {\"key\": \"vashurin2025cocoa\", \"type\": \"inproceedings\", \"title\": \"Uncertainty Quantification for LLMs through Minimum Bayes Risk: Bridging Confidence and Consistency\", \"authors\": \"Vashurin, Roman and Goloburda, Maiya and Ilina, Albina and Rubashevskii, Aleksan...\", \"year\": \"2025\", \"venue\": \"NeurIPS 2025\"}, {\"key\": \"wadhwa2023revisiting\", \"type\": \"inproceedings\", \"title\": \"Revisiting Relation Extraction in the era of Large Language Models\", \"authors\": \"Wadhwa, Somin and Amir, Silvio and Wallace, Byron\", \"year\": \"2023\", \"venue\": \"Proceedings of the 61st Annual Meeting of the Association for Computational Ling...\"}, {\"key\": \"wang2023instructuie\", \"type\": \"article\", \"title\": \"InstructUIE: Multi-task Instruction Tuning for Unified Information Extraction\", \"authors\": \"Wang, Xiao and Zhou, Weikang and Zu, Can and Xia, Han and Chen, Tianze and Zhang...\", \"year\": \"2023\", \"venue\": \"arXiv preprint arXiv:2304.08085\"}, {\"key\": \"wang2023selfconsistency\", \"type\": \"inproceedings\", \"title\": \"Self-Consistency Improves Chain of Thought Reasoning in Language Models\", \"authors\": \"Wang, Xuezhi and Wei, Jason and Schuurmans, Dale and Le, Quoc and Chi, Ed and Na...\", \"year\": \"2023\", \"venue\": \"ICLR 2023\"}, {\"key\": \"wang2025make\", \"type\": \"inproceedings\", \"title\": \"Make Every Penny Count: Difficulty-Adaptive Self-Consistency for Cost-Efficient Reasoning\", \"authors\": \"Wang, Xinglin and Feng, Shaoxiong and Li, Yiwei and Yuan, Peiwen and Zhang, Yueq...\", \"year\": \"2025\", \"venue\": \"Findings of the Association for Computational Linguistics: NAACL 2025\"}, {\"key\": \"wang2024mathshepherd\", \"type\": \"inproceedings\", \"title\": \"Math-Shepherd: Verify and Reinforce LLMs Step-by-step without Human Annotations\", \"authors\": \"Wang, Peiyi and Li, Lei and Shao, Zhihong and Xu, Runxin and Dai, Damai and Li, ...\", \"year\": \"2024\", \"venue\": \"ACL 2024\"}, {\"key\": \"wang2025rankedvoting\", \"type\": \"inproceedings\", \"title\": \"Ranked Voting based Self-Consistency of Large Language Models\", \"authors\": \"Wang, Weiqin and Wang, Yile and Huang, Hui\", \"year\": \"2025\", \"venue\": \"ACL Findings 2025\"}, {\"key\": \"wen2025know\", \"type\": \"article\", \"title\": \"Know Your Limits: A Survey of Abstention in Large Language Models\", \"authors\": \"Wen, Bingbing and Yao, Jihan and Feng, Shangbin and Xu, Chenjun and Tsvetkov, Yu...\", \"year\": \"2025\", \"venue\": \"Transactions of the Association for Computational Linguistics\"}, {\"key\": \"willard2023guided\", \"type\": \"article\", \"title\": \"Efficient Guided Generation for Large Language Models\", \"authors\": \"Willard, Brandon T. and Louf, Rémi\", \"year\": \"2023\", \"venue\": \"arXiv preprint arXiv:2307.09702\"}, {\"key\": \"xia2025survey\", \"type\": \"inproceedings\", \"title\": \"A Survey of Uncertainty Estimation Methods on Large Language Models\", \"authors\": \"Xia, Zhiqiu and Xu, Jinxuan and Zhang, Yuqian and Liu, Hang\", \"year\": \"2025\", \"venue\": \"ACL Findings 2025\"}, {\"key\": \"xiao2019uncertainty\", \"type\": \"article\", \"title\": \"Quantifying Uncertainties in Natural Language Processing Tasks\", \"authors\": \"Xiao, Yijun and Wang, William Yang\", \"year\": \"2019\", \"venue\": \"Proceedings of the AAAI Conference on Artificial Intelligence\"}, {\"key\": \"zhang2023ener\", \"type\": \"inproceedings\", \"title\": \"E-NER: Evidential Deep Learning for Trustworthy Named Entity Recognition\", \"authors\": \"Zhang, Zhen and Hu, Mengting and Zhao, Shiwan and Huang, Minlie and Wang, Haotia...\", \"year\": \"2023\", \"venue\": \"Findings of the Association for Computational Linguistics: ACL 2023\"}, {\"key\": \"zheng2024llamafactory\", \"type\": \"inproceedings\", \"title\": \"LlamaFactory: Unified Efficient Fine-Tuning of 100+ Language Models\", \"authors\": \"Zheng, Yaowei and Zhang, Richong and Zhang, Junhao and Ye, Yanhan and Luo, Zheya...\", \"year\": \"2024\", \"venue\": \"Proceedings of the 62nd Annual Meeting of the Association for Computational Ling...\"}, {\"key\": \"zhou2024uniner\", \"type\": \"inproceedings\", \"title\": \"UniversalNER: Targeted Distillation from Large Language Models for Open Named Entity Recognition\", \"authors\": \"Zhou, Wenxuan and Zhang, Sheng and Gu, Yu and Chen, Muhao and Poon, Hoifung\", \"year\": \"2024\", \"venue\": \"Proceedings of the International Conference on Learning Representations (ICLR)\"}, {\"key\": \"xiong2024llm\", \"type\": \"inproceedings\", \"title\": \"Can LLMs Express Their Uncertainty? An Empirical Evaluation of Confidence Elicitation in LLMs\", \"authors\": \"Xiong, Miao and Hu, Zhiyuan and Lu, Xinyang and Li, Yifei and Fu, Jie and He, Ju...\", \"year\": \"2024\", \"venue\": \"Proceedings of the International Conference on Learning Representations (ICLR)\"}, {\"key\": \"muller2021understanding\", \"type\": \"inproceedings\", \"title\": \"Understanding the Properties of Minimum Bayes Risk Decoding in Neural Machine Translation\", \"authors\": \"M\\\\\\\"uller, Mathias and Sennrich, Rico\", \"year\": \"2021\", \"venue\": \"Proceedings of the 59th Annual Meeting of the Association for Computational Ling...\"}, {\"key\": \"heo2025uncertainty\", \"type\": \"inproceedings\", \"title\": \"Do LLMs Estimate Uncertainty Well in Instruction Following?\", \"authors\": \"Heo, Juyeon and Xiong, Miao and Heinze-Deml, Christina and Narain, Jaya\", \"year\": \"2025\", \"venue\": \"Proceedings of the International Conference on Learning Representations (ICLR)\"}, {\"key\": \"eikema2025structured\", \"type\": \"inproceedings\", \"title\": \"Structure-Conditional Minimum Bayes Risk Decoding\", \"authors\": \"Eikema, Bryan and Rutkiewicz, Anna and Giulianelli, Mario\", \"year\": \"2025\", \"venue\": \"Proceedings of the 2025 Conference on Empirical Methods in Natural Language Proc...\"}, {\"key\": \"zhang2025tts\", \"type\": \"article\", \"title\": \"A Survey on Test-Time Scaling in Large Language Models: What, How, Where, and How Well?\", \"authors\": \"Zhang, Qiyuan and Lyu, Fuyuan and Sun, Zexu and Wang, Lei and Zhang, Weixu and G...\", \"year\": \"2025\", \"venue\": \"arXiv preprint arXiv:2503.24235\"}, {\"key\": \"venktesh2025trust\", \"type\": \"article\", \"title\": \"Trust but Verify! A Survey on Verification Design for Test-time Scaling\", \"authors\": \"Venktesh, V and Rathee, Mandeep and Anand, Avishek\", \"year\": \"2025\", \"venue\": \"arXiv preprint arXiv:2508.16665\"}, {\"key\": \"jinnai2024mbr\", \"type\": \"inproceedings\", \"title\": \"Model-Based Minimum Bayes Risk Decoding for Text Generation\", \"authors\": \"Jinnai, Yuu and Morimura, Tetsuro and Honda, Ukyo and Ariu, Kaito and Abe, Kensh...\", \"year\": \"2024\", \"venue\": \"Proceedings of the 41st International Conference on Machine Learning (ICML)\"}], \"tex_citations\": [{\"key\": \"wang2023selfconsistency\", \"file\": \"sections/introduction.tex\", \"line\": 4, \"command\": \"citealp\"}, {\"key\": \"snell2025scaling\", \"file\": \"sections/introduction.tex\", \"line\": 5, \"command\": \"cite\"}, {\"key\": \"brown2024monkeys\", \"file\": \"sections/introduction.tex\", \"line\": 5, \"command\": \"cite\"}, {\"key\": \"wang2023selfconsistency\", \"file\": \"sections/introduction.tex\", \"line\": 15, \"command\": \"cite\"}, {\"key\": \"chen2024usc\", \"file\": \"sections/introduction.tex\", \"line\": 15, \"command\": \"cite\"}, {\"key\": \"taubenfeld2025cisc\", \"file\": \"sections/introduction.tex\", \"line\": 15, \"command\": \"cite\"}, {\"key\": \"kang2025selfcertainty\", \"file\": \"sections/introduction.tex\", \"line\": 15, \"command\": \"cite\"}, {\"key\": \"nedellec2026consistency\", \"file\": \"sections/introduction.tex\", \"line\": 16, \"command\": \"citet\"}, {\"key\": \"willard2023guided\", \"file\": \"sections/introduction.tex\", \"line\": 19, \"command\": \"cite\"}, {\"key\": \"eikema2022sampling\", \"file\": \"sections/introduction.tex\", \"line\": 24, \"command\": \"cite\"}, {\"key\": \"freitag2022high\", \"file\": \"sections/introduction.tex\", \"line\": 24, \"command\": \"cite\"}, {\"key\": \"muller2021understanding\", \"file\": \"sections/introduction.tex\", \"line\": 24, \"command\": \"cite\"}, {\"key\": \"luan2018scierc\", \"file\": \"sections/introduction.tex\", \"line\": 35, \"command\": \"cite\"}, {\"key\": \"tjongkimsang2003conll\", \"file\": \"sections/introduction.tex\", \"line\": 35, \"command\": \"cite\"}, {\"key\": \"derczynski2017wnut\", \"file\": \"sections/introduction.tex\", \"line\": 35, \"command\": \"cite\"}, {\"key\": \"nedellec2026consistency\", \"file\": \"sections/introduction.tex\", \"line\": 51, \"command\": \"citet\"}, {\"key\": \"wang2023selfconsistency\", \"file\": \"sections/related_work.tex\", \"line\": 4, \"command\": \"cite\"}, {\"key\": \"chen2024usc\", \"file\": \"sections/related_work.tex\", \"line\": 5, \"command\": \"cite\"}, {\"key\": \"thirukovalluru2024atomic\", \"file\": \"sections/related_work.tex\", \"line\": 5, \"command\": \"cite\"}, {\"key\": \"manakul2023selfcheckgpt\", \"file\": \"sections/related_work.tex\", \"line\": 5, \"command\": \"cite\"}, {\"key\": \"zhang2025tts\", \"file\": \"sections/related_work.tex\", \"line\": 6, \"command\": \"cite\"}, {\"key\": \"snell2025scaling\", \"file\": \"sections/related_work.tex\", \"line\": 6, \"command\": \"citet\"}, {\"key\": \"brown2024monkeys\", \"file\": \"sections/related_work.tex\", \"line\": 6, \"command\": \"citet\"}, {\"key\": \"taubenfeld2025cisc\", \"file\": \"sections/related_work.tex\", \"line\": 7, \"command\": \"cite\"}, {\"key\": \"kang2025selfcertainty\", \"file\": \"sections/related_work.tex\", \"line\": 7, \"command\": \"cite\"}, {\"key\": \"kim2026reasc\", \"file\": \"sections/related_work.tex\", \"line\": 7, \"command\": \"cite\"}, {\"key\": \"wang2025rankedvoting\", \"file\": \"sections/related_work.tex\", \"line\": 7, \"command\": \"cite\"}, {\"key\": \"oh2025latentsc\", \"file\": \"sections/related_work.tex\", \"line\": 7, \"command\": \"cite\"}, {\"key\": \"feng2025optimal\", \"file\": \"sections/related_work.tex\", \"line\": 8, \"command\": \"citet\"}, {\"key\": \"wang2025make\", \"file\": \"sections/related_work.tex\", \"line\": 8, \"command\": \"citet\"}, {\"key\": \"li2025llms\", \"file\": \"sections/related_work.tex\", \"line\": 8, \"command\": \"citet\"}, {\"key\": \"nedellec2026consistency\", \"file\": \"sections/related_work.tex\", \"line\": 13, \"command\": \"citet\"}, {\"key\": \"vashurin2025cocoa\", \"file\": \"sections/related_work.tex\", \"line\": 16, \"command\": \"cite\"}, {\"key\": \"zhou2024uniner\", \"file\": \"sections/related_work.tex\", \"line\": 17, \"command\": \"cite\"}, {\"key\": \"sainz2024gollie\", \"file\": \"sections/related_work.tex\", \"line\": 17, \"command\": \"cite\"}, {\"key\": \"josifoski2022genie\", \"file\": \"sections/related_work.tex\", \"line\": 17, \"command\": \"cite\"}, {\"key\": \"li2023codeie\", \"file\": \"sections/related_work.tex\", \"line\": 17, \"command\": \"cite\"}, {\"key\": \"wadhwa2023revisiting\", \"file\": \"sections/related_work.tex\", \"line\": 17, \"command\": \"cite\"}, {\"key\": \"wang2023instructuie\", \"file\": \"sections/related_work.tex\", \"line\": 17, \"command\": \"cite\"}, {\"key\": \"willard2023guided\", \"file\": \"sections/related_work.tex\", \"line\": 17, \"command\": \"cite\"}, {\"key\": \"geng2024confidence\", \"file\": \"sections/related_work.tex\", \"line\": 20, \"command\": \"cite\"}, {\"key\": \"wen2025know\", \"file\": \"sections/related_work.tex\", \"line\": 20, \"command\": \"cite\"}, {\"key\": \"xia2025survey\", \"file\": \"sections/related_work.tex\", \"line\": 20, \"command\": \"cite\"}, {\"key\": \"hobelsberger2025systematic\", \"file\": \"sections/related_work.tex\", \"line\": 20, \"command\": \"cite\"}, {\"key\": \"xiong2024llm\", \"file\": \"sections/related_work.tex\", \"line\": 20, \"command\": \"citet\"}, {\"key\": \"heo2025uncertainty\", \"file\": \"sections/related_work.tex\", \"line\": 20, \"command\": \"citet\"}, {\"key\": \"kuhn2023semantic\", \"file\": \"sections/related_work.tex\", \"line\": 21, \"command\": \"cite\"}, {\"key\": \"kossen2024semantic\", \"file\": \"sections/related_work.tex\", \"line\": 21, \"command\": \"citet\"}, {\"key\": \"kadavath2022language\", \"file\": \"sections/related_work.tex\", \"line\": 21, \"command\": \"cite\"}, {\"key\": \"malinin2021uncertainty\", \"file\": \"sections/related_work.tex\", \"line\": 21, \"command\": \"citet\"}, {\"key\": \"guo2017calibration\", \"file\": \"sections/related_work.tex\", \"line\": 23, \"command\": \"cite\"}, {\"key\": \"desai2020calibration\", \"file\": \"sections/related_work.tex\", \"line\": 23, \"command\": \"cite\"}, {\"key\": \"lakshminarayanan2017ensembles\", \"file\": \"sections/related_work.tex\", \"line\": 23, \"command\": \"cite\"}, {\"key\": \"gal2016dropout\", \"file\": \"sections/related_work.tex\", \"line\": 23, \"command\": \"cite\"}, {\"key\": \"xiao2019uncertainty\", \"file\": \"sections/related_work.tex\", \"line\": 24, \"command\": \"cite\"}, {\"key\": \"shelmanov2021active\", \"file\": \"sections/related_work.tex\", \"line\": 24, \"command\": \"cite\"}, {\"key\": \"zhang2023ener\", \"file\": \"sections/related_work.tex\", \"line\": 24, \"command\": \"cite\"}, {\"key\": \"kim2024verifiner\", \"file\": \"sections/related_work.tex\", \"line\": 24, \"command\": \"cite\"}, {\"key\": \"he2024uncertainty\", \"file\": \"sections/related_work.tex\", \"line\": 24, \"command\": \"cite\"}, {\"key\": \"fisch2021conformal\", \"file\": \"sections/related_work.tex\", \"line\": 25, \"command\": \"cite\"}, {\"key\": \"angelopoulos2021conformal\", \"file\": \"sections/related_work.tex\", \"line\": 25, \"command\": \"cite\"}, {\"key\": \"cobbe2021verifiers\", \"file\": \"sections/related_work.tex\", \"line\": 25, \"command\": \"cite\"}, {\"key\": \"lightman2024verify\", \"file\": \"sections/related_work.tex\", \"line\": 25, \"command\": \"cite\"}, {\"key\": \"venktesh2025trust\", \"file\": \"sections/related_work.tex\", \"line\": 25, \"command\": \"cite\"}, {\"key\": \"wang2024mathshepherd\", \"file\": \"sections/related_work.tex\", \"line\": 25, \"command\": \"cite\"}, {\"key\": \"eikema2022sampling\", \"file\": \"sections/related_work.tex\", \"line\": 26, \"command\": \"cite\"}, {\"key\": \"freitag2022high\", \"file\": \"sections/related_work.tex\", \"line\": 26, \"command\": \"cite\"}, {\"key\": \"jinnai2024mbr\", \"file\": \"sections/related_work.tex\", \"line\": 26, \"command\": \"cite\"}, {\"key\": \"eikema2025structured\", \"file\": \"sections/related_work.tex\", \"line\": 27, \"command\": \"citet\"}, {\"key\": \"geifman2017selective\", \"file\": \"sections/related_work.tex\", \"line\": 28, \"command\": \"cite\"}, {\"key\": \"culotta2004confidence\", \"file\": \"sections/related_work.tex\", \"line\": 28, \"command\": \"cite\"}, {\"key\": \"willard2023guided\", \"file\": \"sections/method.tex\", \"line\": 5, \"command\": \"cite\"}, {\"key\": \"fleiss1971agreement\", \"file\": \"sections/method.tex\", \"line\": 34, \"command\": \"citet\"}, {\"key\": \"jaccard1901distribution\", \"file\": \"sections/method.tex\", \"line\": 45, \"command\": \"cite\"}, {\"key\": \"luan2018scierc\", \"file\": \"sections/experiments.tex\", \"line\": 9, \"command\": \"cite\"}, {\"key\": \"tjongkimsang2003conll\", \"file\": \"sections/experiments.tex\", \"line\": 10, \"command\": \"cite\"}, {\"key\": \"derczynski2017wnut\", \"file\": \"sections/experiments.tex\", \"line\": 11, \"command\": \"cite\"}, {\"key\": \"zheng2024llamafactory\", \"file\": \"sections/experiments.tex\", \"line\": 14, \"command\": \"cite\"}, {\"key\": \"willard2023guided\", \"file\": \"sections/experiments.tex\", \"line\": 21, \"command\": \"cite\"}, {\"key\": \"kuhn2023semantic\", \"file\": \"sections/experiments.tex\", \"line\": 60, \"command\": \"cite\"}, {\"key\": \"xiong2024llm\", \"file\": \"sections/experiments.tex\", \"line\": 74, \"command\": \"citep\"}, {\"key\": \"brown2024monkeys\", \"file\": \"sections/experiments.tex\", \"line\": 141, \"command\": \"cite\"}, {\"key\": \"snell2025scaling\", \"file\": \"sections/experiments.tex\", \"line\": 141, \"command\": \"cite\"}, {\"key\": \"cobbe2021verifiers\", \"file\": \"sections/experiments.tex\", \"line\": 141, \"command\": \"cite\"}, {\"key\": \"eikema2022sampling\", \"file\": \"sections/discussion.tex\", \"line\": 28, \"command\": \"cite\"}, {\"key\": \"muller2021understanding\", \"file\": \"sections/discussion.tex\", \"line\": 28, \"command\": \"cite\"}, {\"key\": \"freitag2022high\", \"file\": \"sections/discussion.tex\", \"line\": 29, \"command\": \"cite\"}, {\"key\": \"jinnai2024mbr\", \"file\": \"sections/discussion.tex\", \"line\": 29, \"command\": \"cite\"}, {\"key\": \"eikema2025structured\", \"file\": \"sections/discussion.tex\", \"line\": 30, \"command\": \"citet\"}, {\"key\": \"cobbe2021verifiers\", \"file\": \"sections/discussion.tex\", \"line\": 53, \"command\": \"cite\"}, {\"key\": \"venktesh2025trust\", \"file\": \"sections/discussion.tex\", \"line\": 53, \"command\": \"cite\"}, {\"key\": \"brown2024monkeys\", \"file\": \"sections/appendix.tex\", \"line\": 193, \"command\": \"cite\"}, {\"key\": \"snell2025scaling\", \"file\": \"sections/appendix.tex\", \"line\": 193, \"command\": \"cite\"}, {\"key\": \"willard2023guided\", \"file\": \"sections/appendix.tex\", \"line\": 394, \"command\": \"cite\"}], \"online_verification\": [{\"key\": \"angelopoulos2021conformal\", \"title\": \"Uncertainty Sets for Image Classifiers using Conformal Prediction\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Uncertainty Sets for Image Classifiers using Conformal Prediction\", \"matched_year\": \"2020\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"brown2024monkeys\", \"title\": \"Large Language Monkeys: Scaling Inference Compute with Repeated Sampling\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Large Language Monkeys: Scaling Inference Compute with Repeated Sampling\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"chen2024usc\", \"title\": \"Universal Self-Consistency for Large Language Model Generation\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Universal Self-Consistency for Large Language Model Generation\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"cobbe2021verifiers\", \"title\": \"Training Verifiers to Solve Math Word Problems\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Training Verifiers to Solve Math Word Problems\", \"matched_year\": \"2021\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"culotta2004confidence\", \"title\": \"Confidence Estimation for Information Extraction\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Confidence estimation for information extraction\", \"matched_year\": \"2004\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"derczynski2017wnut\", \"title\": \"Results of the WNUT2017 Shared Task on Novel and Emerging Entity Recognition\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Results of the WNUT2017 Shared Task on Novel and Emerging Entity Recognition\", \"matched_year\": \"2017\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"desai2020calibration\", \"title\": \"Calibration of Pre-trained Transformers\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Calibration of Pre-trained Transformers\", \"matched_year\": \"2020\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"eikema2022sampling\", \"title\": \"Sampling-Based Approximations to Minimum Bayes Risk Decoding for Neural Machine Translation\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Sampling-Based Approximations to Minimum Bayes Risk Decoding for Neural Machine Translation\", \"matched_year\": \"2022\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"fisch2021conformal\", \"title\": \"Few-Shot Conformal Prediction with Auxiliary Tasks\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Few-shot Conformal Prediction with Auxiliary Tasks\", \"matched_year\": \"2021\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"freitag2022high\", \"title\": \"High Quality Rather than High Model Probability: Minimum Bayes Risk Decoding with Neural Metrics\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"High Quality Rather than High Model Probability: Minimum Bayes Risk Decoding with Neural Metrics\", \"matched_year\": \"2022\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"he2024uncertainty\", \"title\": \"Uncertainty Estimation on Sequential Labeling via Uncertainty Transmission\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Uncertainty Estimation on Sequential Labeling via Uncertainty Transmission\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"fleiss1971agreement\", \"title\": \"Measuring nominal scale agreement among many raters.\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Measuring nominal scale agreement among many raters.\", \"matched_year\": \"1971\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"gal2016dropout\", \"title\": \"Dropout as a Bayesian Approximation: Representing Model Uncertainty in Deep Learning\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Dropout as a Bayesian Approximation: Representing Model Uncertainty in Deep Learning\", \"matched_year\": \"2015\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"geifman2017selective\", \"title\": \"Selective Classification for Deep Neural Networks\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Selective Classification for Deep Neural Networks\", \"matched_year\": \"2017\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"feng2025optimal\", \"title\": \"Optimal Self-Consistency for Efficient Reasoning with Large Language Models\", \"status\": \"mismatch\", \"confidence\": 1.0, \"matched_title\": \"Optimal Self-Consistency for Efficient Reasoning with Large Language Models\", \"matched_year\": \"2025\", \"mismatch_fields\": [\"first_author: bib=feng vs api=austin\"], \"note\": \"\"}, {\"key\": \"geng2024confidence\", \"title\": \"A Survey of Confidence Estimation and Calibration in Large Language Models\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"A Survey of Confidence Estimation and Calibration in Large Language Models\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"guo2017calibration\", \"title\": \"On Calibration of Modern Neural Networks\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"On Calibration of Modern Neural Networks\", \"matched_year\": \"2017\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"hobelsberger2025systematic\", \"title\": \"Systematic Evaluation of Uncertainty Estimation Methods in Large Language Models\", \"status\": \"not_found\", \"confidence\": 0.236, \"matched_title\": \"A new criterion for assessing discriminant validity in variance-based structural equation modeling\", \"matched_year\": \"\", \"mismatch_fields\": [], \"note\": \"best match similarity 0.24 below threshold 0.82\"}, {\"key\": \"jaccard1901distribution\", \"title\": \"Étude comparative de la distribution florale dans une portion des Alpes et du Jura\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Étude comparative de la distribution florale dans une portion des Alpes et du Jura\", \"matched_year\": \"1901\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"josifoski2022genie\", \"title\": \"GenIE: Generative Information Extraction\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"GenIE: Generative Information Extraction\", \"matched_year\": \"2022\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"kadavath2022language\", \"title\": \"Language Models (Mostly) Know What They Know\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Language Models (Mostly) Know What They Know\", \"matched_year\": \"2022\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"kang2025selfcertainty\", \"title\": \"Scalable Best-of-N Selection for Large Language Models via Self-Certainty\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Scalable Best-of-N Selection for Large Language Models via Self-Certainty\", \"matched_year\": \"2025\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"kim2024verifiner\", \"title\": \"VerifiNER: Verification-augmented NER via Knowledge-grounded Reasoning with Large Language Models\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"VerifiNER: Verification-augmented NER via Knowledge-grounded Reasoning with Large Language Models\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"kim2026reasc\", \"title\": \"Reliability-Aware Adaptive Self-Consistency for Efficient Sampling in LLM Reasoning\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Reliability-Aware Adaptive Self-Consistency for Efficient Sampling in LLM Reasoning\", \"matched_year\": \"2026\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"kossen2024semantic\", \"title\": \"Semantic Entropy Probes: Robust and Cheap Hallucination Detection in LLMs\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Semantic Entropy Probes: Robust and Cheap Hallucination Detection in LLMs\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"li2025llms\", \"title\": \"LLMs Can Generate a Better Answer by Aggregating Their Own Responses\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"LLMs Can Generate a Better Answer by Aggregating Their Own Responses\", \"matched_year\": \"2025\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"kuhn2023semantic\", \"title\": \"Semantic Uncertainty: Linguistic Invariances for Uncertainty Estimation in Natural Language Generation\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Semantic Uncertainty: Linguistic Invariances for Uncertainty Estimation in Natural Language Generation\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"malinin2021uncertainty\", \"title\": \"Uncertainty Estimation in Autoregressive Structured Prediction\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Uncertainty Estimation in Autoregressive Structured Prediction\", \"matched_year\": \"2020\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"lakshminarayanan2017ensembles\", \"title\": \"Simple and Scalable Predictive Uncertainty Estimation using Deep Ensembles\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Simple and Scalable Predictive Uncertainty Estimation using Deep Ensembles\", \"matched_year\": \"2016\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"li2023codeie\", \"title\": \"CodeIE: Large Code Generation Models are Better Few-Shot Information Extractors\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"CodeIE: Large Code Generation Models are Better Few-Shot Information Extractors\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"lightman2024verify\", \"title\": \"Let's Verify Step by Step\", \"status\": \"not_found\", \"confidence\": 0.246, \"matched_title\": \"Development and dosimetric verification of static SHArc: Step‐and‐shoot carbon ion arc therapy for LET &lt;sub>d&lt;/sub> escalation in pancreatic tumors\", \"matched_year\": \"\", \"mismatch_fields\": [], \"note\": \"best match similarity 0.25 below threshold 0.82\"}, {\"key\": \"luan2018scierc\", \"title\": \"Multi-Task Identification of Entities, Relations, and Coreference for Scientific Knowledge Graph Construction\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Multi-Task Identification of Entities, Relations, and Coreference for Scientific Knowledge Graph Construction\", \"matched_year\": \"2018\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"manakul2023selfcheckgpt\", \"title\": \"SelfCheckGPT: Zero-Resource Black-Box Hallucination Detection for Generative Large Language Models\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"SelfCheckGPT: Zero-Resource Black-Box Hallucination Detection for Generative Large Language Models\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"nedellec2026consistency\", \"title\": \"Consistency–accuracy correlation in hard-prompted LLMs for entity and relation extraction: empirical findings from plant-health data\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Consistency–accuracy correlation in hard-prompted LLMs for entity and relation extraction: empirical findings from plant-health data\", \"matched_year\": \"2026\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"oh2025latentsc\", \"title\": \"Latent Self-Consistency for Reliable Majority-Set Selection in Short- and Long-Answer Reasoning\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Latent Self-Consistency for Reliable Majority-Set Selection in Short- and Long-Answer Reasoning\", \"matched_year\": \"2026\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"sainz2024gollie\", \"title\": \"GoLLIE: Annotation Guidelines improve Zero-Shot Information-Extraction\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"GoLLIE: Annotation Guidelines improve Zero-Shot Information-Extraction\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"shelmanov2021active\", \"title\": \"Active Learning for Sequence Tagging with Deep Pre-trained Models and Bayesian Uncertainty Estimates\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Active Learning for Sequence Tagging with Deep Pre-trained Models and Bayesian Uncertainty Estimates\", \"matched_year\": \"2021\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"snell2025scaling\", \"title\": \"Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters\", \"status\": \"mismatch\", \"confidence\": 1.0, \"matched_title\": \"Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters\", \"matched_year\": \"2024\", \"mismatch_fields\": [\"first_author: bib=snell vs api=charlie\"], \"note\": \"\"}, {\"key\": \"taubenfeld2025cisc\", \"title\": \"Confidence Improves Self-Consistency in LLMs\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Confidence Improves Self-Consistency in LLMs\", \"matched_year\": \"2025\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"thirukovalluru2024atomic\", \"title\": \"Atomic Self-Consistency for Better Long Form Generations\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Atomic Self-Consistency for Better Long Form Generations\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"tjongkimsang2003conll\", \"title\": \"Introduction to the CoNLL-2003 Shared Task: Language-Independent Named Entity Recognition\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Introduction to the CoNLL-2003 Shared Task: Language-Independent Named Entity Recognition\", \"matched_year\": \"2003\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"vashurin2025cocoa\", \"title\": \"Uncertainty Quantification for LLMs through Minimum Bayes Risk: Bridging Confidence and Consistency\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Uncertainty Quantification for LLMs through Minimum Bayes Risk: Bridging Confidence and Consistency\", \"matched_year\": \"2025\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"wadhwa2023revisiting\", \"title\": \"Revisiting Relation Extraction in the era of Large Language Models\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Revisiting Relation Extraction in the era of Large Language Models\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"wang2023instructuie\", \"title\": \"InstructUIE: Multi-task Instruction Tuning for Unified Information Extraction\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"InstructUIE: Multi-task Instruction Tuning for Unified Information Extraction\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"wang2023selfconsistency\", \"title\": \"Self-Consistency Improves Chain of Thought Reasoning in Language Models\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Self-Consistency Improves Chain of Thought Reasoning in Language Models\", \"matched_year\": \"2022\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"wang2025make\", \"title\": \"Make Every Penny Count: Difficulty-Adaptive Self-Consistency for Cost-Efficient Reasoning\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Make Every Penny Count: Difficulty-Adaptive Self-Consistency for Cost-Efficient Reasoning\", \"matched_year\": \"2025\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"wang2024mathshepherd\", \"title\": \"Math-Shepherd: Verify and Reinforce LLMs Step-by-step without Human Annotations\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Math-Shepherd: Verify and Reinforce LLMs Step-by-step without Human Annotations\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"wang2025rankedvoting\", \"title\": \"Ranked Voting based Self-Consistency of Large Language Models\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Ranked Voting based Self-Consistency of Large Language Models\", \"matched_year\": \"2025\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"wen2025know\", \"title\": \"Know Your Limits: A Survey of Abstention in Large Language Models\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Know Your Limits: A Survey of Abstention in Large Language Models\", \"matched_year\": \"2025\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"willard2023guided\", \"title\": \"Efficient Guided Generation for Large Language Models\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Efficient Guided Generation for Large Language Models\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"xia2025survey\", \"title\": \"A Survey of Uncertainty Estimation Methods on Large Language Models\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"A Survey of Uncertainty Estimation Methods on Large Language Models\", \"matched_year\": \"2025\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"xiao2019uncertainty\", \"title\": \"Quantifying Uncertainties in Natural Language Processing Tasks\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Quantifying Uncertainties in Natural Language Processing Tasks\", \"matched_year\": \"2019\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"zhang2023ener\", \"title\": \"E-NER: Evidential Deep Learning for Trustworthy Named Entity Recognition\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"E-NER: Evidential Deep Learning for Trustworthy Named Entity Recognition\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"zheng2024llamafactory\", \"title\": \"LlamaFactory: Unified Efficient Fine-Tuning of 100+ Language Models\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"LlamaFactory: Unified Efficient Fine-Tuning of 100+ Language Models\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"zhou2024uniner\", \"title\": \"UniversalNER: Targeted Distillation from Large Language Models for Open Named Entity Recognition\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"UniversalNER: Targeted Distillation from Large Language Models for Open Named Entity Recognition\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"xiong2024llm\", \"title\": \"Can LLMs Express Their Uncertainty? An Empirical Evaluation of Confidence Elicitation in LLMs\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Can LLMs Express Their Uncertainty? An Empirical Evaluation of Confidence Elicitation in LLMs\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"muller2021understanding\", \"title\": \"Understanding the Properties of Minimum Bayes Risk Decoding in Neural Machine Translation\", \"status\": \"mismatch\", \"confidence\": 1.0, \"matched_title\": \"Understanding the Properties of Minimum Bayes Risk Decoding in Neural Machine Translation\", \"matched_year\": \"2021\", \"mismatch_fields\": [\"first_author: bib=m\\\\\\\"uller vs api=müller\"], \"note\": \"\"}, {\"key\": \"heo2025uncertainty\", \"title\": \"Do LLMs Estimate Uncertainty Well in Instruction Following?\", \"status\": \"verified\", \"confidence\": 0.983, \"matched_title\": \"Do LLMs estimate uncertainty well in instruction-following?\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"eikema2025structured\", \"title\": \"Structure-Conditional Minimum Bayes Risk Decoding\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Structure-Conditional Minimum Bayes Risk Decoding\", \"matched_year\": \"2025\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"zhang2025tts\", \"title\": \"A Survey on Test-Time Scaling in Large Language Models: What, How, Where, and How Well?\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"A Survey on Test-Time Scaling in Large Language Models: What, How, Where, and How Well?\", \"matched_year\": \"2025\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"venktesh2025trust\", \"title\": \"Trust but Verify! A Survey on Verification Design for Test-time Scaling\", \"status\": \"not_found\", \"confidence\": 0.252, \"matched_title\": \"The PRISMA Statement for Reporting Systematic Reviews and Meta-Analyses of Studies That Evaluate Health Care Interventions: Explanation and Elaboration\", \"matched_year\": \"\", \"mismatch_fields\": [], \"note\": \"best match similarity 0.25 below threshold 0.82\"}, {\"key\": \"jinnai2024mbr\", \"title\": \"Model-Based Minimum Bayes Risk Decoding for Text Generation\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Model-Based Minimum Bayes Risk Decoding for Text Generation\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}]}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c9cfc4f5-7d7c-4bfa-8311-9dd65f7496d0",
  "isSidechain": false,
  "promptId": "a8cee1eb-a5df-415d-8e30-c85446d1e0a7",
  "type": "user",
  "uuid": "96fb538e-bfe1-4500-9b2c-223c81575766",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie--claude-sessions-review-reviewer-2-a0c838f5/f49c1ccb-97a0-4961-857d-2db0aa0e0624/tool-results/toolu_01EyB9T3fkAJQ5ufKg9cmgPX.txt",
      "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"summary\\\": {\\\"total_bib_entries\\\": 62, \\\"total_citations\\\": 94, \\\"unique_cited_keys\\\": 62, \\\"orphan_bib\\\": 0, \\\"missing_bib\\\": 0, \\\"duplicate_keys\\\": 0, \\\"online_verified\\\": 56, \\\"online_not_found\\\": 3, \\\"online_mismatch\\\": 3}, \\\"cross_check\\\": {\\\"orphan_bib\\\": [], \\\"missing_bib\\\": [], \\\"orphan_count\\\": 0, \\\"missing_count\\\": 0}, \\\"bib_entries\\\": [{\\\"key\\\": \\\"angelopoulos2021conformal\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Uncertainty Sets for Image Classifiers using Conformal Prediction\\\", \\\"authors\\\": \\\"Angelopoulos, Anastasios N. and Bates, Stephen and Malik, Jitendra and Jordan, M...\\\", \\\"year\\\": \\\"2021\\\", \\\"venue\\\": \\\"ICLR 2021\\\"}, {\\\"key\\\": \\\"brown2024monkeys\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Large Language Monkeys: Scaling Inference Compute with Repeated Sampling\\\", \\\"authors\\\": \\\"Brown, Bradley and Juravsky, Jordan and Ehrlich, Ryan and Clark, Ronald and Le, ...\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"arXiv preprint arXiv:2407.21787\\\"}, {\\\"key\\\": \\\"chen2024usc\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Universal Self-Consistency for Large Language Model Generation\\\", \\\"authors\\\": \\\"Chen, Xinyun and Aksitov, Renat and Alon, Uri and Ren, Jie and Xiao, Kefan and Y...\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"arXiv preprint (ICML 2024 Workshop ICL)\\\"}, {\\\"key\\\": \\\"cobbe2021verifiers\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Training Verifiers to Solve Math Word Problems\\\", \\\"authors\\\": \\\"Cobbe, Karl and Kosaraju, Vineet and Bavarian, Mohammad and Chen, Mark and Jun, ...\\\", \\\"year\\\": \\\"2021\\\", \\\"venue\\\": \\\"arXiv preprint arXiv:2110.14168\\\"}, {\\\"key\\\": \\\"culotta2004confidence\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Confidence Estimation for Information Extraction\\\", \\\"authors\\\": \\\"Culotta, Aron and McCallum, Andrew\\\", \\\"year\\\": \\\"2004\\\", \\\"venue\\\": \\\"HLT-NAACL 2004\\\"}, {\\\"key\\\": \\\"derczynski2017wnut\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Results of the WNUT2017 Shared Task on Novel and Emerging Entity Recognition\\\", \\\"authors\\\": \\\"Derczynski, Leon and Nichols, Eric and Erp, Marieke van and Limsopatham, Nut\\\", \\\"year\\\": \\\"2017\\\", \\\"venue\\\": \\\"W-NUT Workshop at EMNLP 2017\\\"}, {\\\"key\\\": \\\"desai2020calibration\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Calibration of Pre-trained Transformers\\\", \\\"authors\\\": \\\"Desai, Shrey and Durrett, Greg\\\", \\\"year\\\": \\\"2020\\\", \\\"venue\\\": \\\"Proceedings of the 2020 Conference on Empirical Methods in Natural Language Proc...\\\"}, {\\\"key\\\": \\\"eikema2022sampling\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Sampling-Based Approximations to Minimum Bayes Risk Decoding for Neural Machine Translation\\\", \\\"authors\\\": \\\"Eikema, Bryan and Aziz, Wilker\\\", \\\"year\\\": \\\"2022\\\", \\\"venue\\\": \\\"Proceedings of the 2022 Conference on Empirical Methods in Natural Language Proc...\\\"}, {\\\"key\\\": \\\"fisch2021conformal\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Few-Shot Conformal Prediction with Auxiliary Tasks\\\", \\\"authors\\\": \\\"Fisch, Adam and Schuster, Tal and Jaakkola, Tommi and Barzilay, Regina\\\", \\\"year\\\": \\\"2021\\\", \\\"venue\\\": \\\"ICML 2021\\\"}, {\\\"key\\\": \\\"freitag2022high\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"High Quality Rather than High Model Probability: Minimum Bayes Risk Decoding with Neural Metrics\\\", \\\"authors\\\": \\\"Freitag, Markus and Grangier, David and Tan, Qijun and Liang, Bowen\\\", \\\"year\\\": \\\"2022\\\", \\\"venue\\\": \\\"Transactions of the Association for Computational Linguistics\\\"}, {\\\"key\\\": \\\"he2024uncertainty\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Uncertainty Estimation on Sequential Labeling via Uncertainty Transmission\\\", \\\"authors\\\": \\\"He, Jianfeng and Yu, Linlin and Lei, Shuo and Lu, Chang-Tien and Chen, Feng\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"Findings of the Association for Computational Linguistics: NAACL 2024\\\"}, {\\\"key\\\": \\\"fleiss1971agreement\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Measuring nominal scale agreement among many raters.\\\", \\\"authors\\\": \\\"Fleiss, Joseph L.\\\", \\\"year\\\": \\\"1971\\\", \\\"venue\\\": \\\"Psychological Bulletin\\\"}, {\\\"key\\\": \\\"gal2016dropout\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Dropout as a Bayesian Approximation: Representing Model Uncertainty in Deep Learning\\\", \\\"authors\\\": \\\"Gal, Yarin and Ghahramani, Zoubin\\\", \\\"year\\\": \\\"2016\\\", \\\"venue\\\": \\\"ICML 2016\\\"}, {\\\"key\\\": \\\"geifman2017selective\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Selective Classification for Deep Neural Networks\\\", \\\"authors\\\": \\\"Geifman, Yonatan and El-Yaniv, Ran\\\", \\\"year\\\": \\\"2017\\\", \\\"venue\\\": \\\"NeurIPS 2017\\\"}, {\\\"key\\\": \\\"feng2025optimal\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Optimal Self-Consistency for Efficient Reasoning with Large Language Models\\\", \\\"authors\\\": \\\"Feng, Austin and Alonso, Marius and Odonnat, Ambroise\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"arXiv preprint arXiv:2511.12309\\\"}, {\\\"key\\\": \\\"geng2024confidence\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"A Survey of Confidence Estimation and Calibration in Large Language Models\\\", \\\"authors\\\": \\\"Geng, Jiahui and Cai, Fengyu and Wang, Yuxia and Koeppl, Heinz and Nakov, Presla...\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"Proceedings of the 2024 Conference of the North American Chapter of the Associat...\\\"}, {\\\"key\\\": \\\"guo2017calibration\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"On Calibration of Modern Neural Networks\\\", \\\"authors\\\": \\\"Guo, Chuan and Pleiss, Geoff and Sun, Yu and Weinberger, Kilian Q.\\\", \\\"year\\\": \\\"2017\\\", \\\"venue\\\": \\\"ICML 2017\\\"}, {\\\"key\\\": \\\"hobelsberger2025systematic\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Systematic Evaluation of Uncertainty Estimation Methods in Large Language Models\\\", \\\"authors\\\": \\\"Hobelsberger, Christian and Winner, Theresa and Nawroth, Andreas and Mitevski, O...\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"arXiv preprint arXiv:2510.20460\\\"}, {\\\"key\\\": \\\"jaccard1901distribution\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Étude comparative de la distribution florale dans une portion des Alpes et du Jura\\\", \\\"authors\\\": \\\"Jaccard, Paul\\\", \\\"year\\\": \\\"1901\\\", \\\"venue\\\": \\\"Bulletin de la Société Vaudoise des Sciences Naturelles\\\"}, {\\\"key\\\": \\\"josifoski2022genie\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"GenIE: Generative Information Extraction\\\", \\\"authors\\\": \\\"Josifoski, Martin and De Cao, Nicola and Peyrard, Maxime and Petroni, Fabio and ...\\\", \\\"year\\\": \\\"2022\\\", \\\"venue\\\": \\\"Proceedings of the 2022 Conference of the North American Chapter of the Associat...\\\"}, {\\\"key\\\": \\\"kadavath2022language\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Language Models (Mostly) Know What They Know\\\", \\\"authors\\\": \\\"Kadavath, Saurav and Conerly, Tom and Askell, Amanda and Henighan, Tom and Drain...\\\", \\\"year\\\": \\\"2022\\\", \\\"venue\\\": \\\"arXiv preprint arXiv:2207.05221\\\"}, {\\\"key\\\": \\\"kang2025selfcertainty\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Scalable Best-of-N Selection for Large Language Models via Self-Certainty\\\", \\\"authors\\\": \\\"Kang, Zhewei and Zhao, Xuandong and Song, Dawn\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"NeurIPS 2025\\\"}, {\\\"key\\\": \\\"kim2024verifiner\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"VerifiNER: Verification-augmented NER via Knowledge-grounded Reasoning with Large Language Models\\\", \\\"authors\\\": \\\"Kim, Seoyeon and Seo, Kwangwook and Chae, Hyungjoo and Yeo, Jinyoung and Lee, Do...\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"Proceedings of the 62nd Annual Meeting of the Association for Computational Ling...\\\"}, {\\\"key\\\": \\\"kim2026reasc\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Reliability-Aware Adaptive Self-Consistency for Efficient Sampling in LLM Reasoning\\\", \\\"authors\\\": \\\"Kim, Junseok and Yang, Nakyeong and Min, Kyungmin and Jung, Kyomin\\\", \\\"year\\\": \\\"2026\\\", \\\"venue\\\": \\\"ACL 2026\\\"}, {\\\"key\\\": \\\"kossen2024semantic\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Semantic Entropy Probes: Robust and Cheap Hallucination Detection in LLMs\\\", \\\"authors\\\": \\\"Kossen, Jannik and Han, Jiatong and Razzak, Muhammed and Schut, Lisa and Malik, ...\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"arXiv preprint arXiv:2406.15927\\\"}, {\\\"key\\\": \\\"li2025llms\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"LLMs Can Generate a Better Answer by Aggregating Their Own Responses\\\", \\\"authors\\\": \\\"Li, Zichong and Feng, Xinyu and Cai, Yuheng and Zhang, Zixuan and Liu, Tianyi an...\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"arXiv preprint arXiv:2503.04104\\\"}, {\\\"key\\\": \\\"kuhn2023semantic\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Semantic Uncertainty: Linguistic Invariances for Uncertainty Estimation in Natural Language Generation\\\", \\\"authors\\\": \\\"Kuhn, Lorenz and Gal, Yarin and Farquhar, Sebastian\\\", \\\"year\\\": \\\"2023\\\", \\\"venue\\\": \\\"ICLR 2023\\\"}, {\\\"key\\\": \\\"malinin2021uncertainty\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Uncertainty Estimation in Autoregressive Structured Prediction\\\", \\\"authors\\\": \\\"Malinin, Andrey and Gales, Mark\\\", \\\"year\\\": \\\"2021\\\", \\\"venue\\\": \\\"International Conference on Learning Representations\\\"}, {\\\"key\\\": \\\"lakshminarayanan2017ensembles\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Simple and Scalable Predictive Uncertainty Estimation using Deep Ensembles\\\", \\\"authors\\\": \\\"Lakshminarayanan, Balaji and Pritzel, Alexander and Blundell, Charles\\\", \\\"year\\\": \\\"2017\\\", \\\"venue\\\": \\\"NeurIPS 2017\\\"}, {\\\"key\\\": \\\"li2023codeie\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"CodeIE: Large Code Generation Models are Better Few-Shot Information Extractors\\\", \\\"authors\\\": \\\"Li, Peng and Sun, Tianxiang and Tang, Qiong and Yan, Hang and Wu, Yuanbin and Hu...\\\", \\\"year\\\": \\\"2023\\\", \\\"venue\\\": \\\"Proceedings of the 61st Annual Meeting of the Association for Computational Ling...\\\"}, {\\\"key\\\": \\\"lightman2024verify\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Let's Verify Step by Step\\\", \\\"authors\\\": \\\"Lightman, Hunter and Kosaraju, Vineet and Burda, Yura and Edwards, Harri and Bak...\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"ICLR 2024\\\"}, {\\\"key\\\": \\\"luan2018scierc\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Multi-Task Identification of Entities, Relations, and Coreference for Scientific Knowledge Graph Construction\\\", \\\"authors\\\": \\\"Luan, Yi and He, Luheng and Ostendorf, Mari and Hajishirzi, Hannaneh\\\", \\\"year\\\": \\\"2018\\\", \\\"venue\\\": \\\"Proceedings of the 2018 Conference on Empirical Methods in Natural Language Proc...\\\"}, {\\\"key\\\": \\\"manakul2023selfcheckgpt\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"SelfCheckGPT: Zero-Resource Black-Box Hallucination Detection for Generative Large Language Models\\\", \\\"authors\\\": \\\"Manakul, Potsawee and Liusie, Adian and Gales, Mark\\\", \\\"year\\\": \\\"2023\\\", \\\"venue\\\": \\\"Proceedings of the 2023 Conference on Empirical Methods in Natural Language Proc...\\\"}, {\\\"key\\\": \\\"nedellec2026consistency\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Consistency–accuracy correlation in hard-prompted LLMs for entity and relation extraction: empirical findings from plant...\\\", \\\"authors\\\": \\\"Yao, Xinzhi and Nédellec, Claire and Xia, Jingbo and Bossy, Robert\\\", \\\"year\\\": \\\"2026\\\", \\\"venue\\\": \\\"Genomics \\\\\\\\& Informatics\\\"}, {\\\"key\\\": \\\"oh2025latentsc\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Latent Self-Consistency for Reliable Majority-Set Selection in Short- and Long-Answer Reasoning\\\", \\\"authors\\\": \\\"Oh, Jungsuk and Lee, Jay-Yoon\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"arXiv preprint arXiv:2508.18395\\\"}, {\\\"key\\\": \\\"sainz2024gollie\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"GoLLIE: Annotation Guidelines improve Zero-Shot Information-Extraction\\\", \\\"authors\\\": \\\"Sainz, Oscar and García-Ferrero, Iker and Agerri, Rodrigo and Lacalle, Oier Lope...\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"ICLR 2024\\\"}, {\\\"key\\\": \\\"shelmanov2021active\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Active Learning for Sequence Tagging with Deep Pre-trained Models and Bayesian Uncertainty Estimates\\\", \\\"authors\\\": \\\"Shelmanov, Artem and Puzyrev, Dmitri and Kupriyanova, Lyubov and Belyakov, Denis...\\\", \\\"year\\\": \\\"2021\\\", \\\"venue\\\": \\\"Proceedings of the 16th Conference of the European Chapter of the Association fo...\\\"}, {\\\"key\\\": \\\"snell2025scaling\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters\\\", \\\"authors\\\": \\\"Snell, Charlie and Lee, Jaehoon and Xu, Kelvin and Kumar, Aviral\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"Proceedings of the International Conference on Learning Representations (ICLR)\\\"}, {\\\"key\\\": \\\"taubenfeld2025cisc\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Confidence Improves Self-Consistency in LLMs\\\", \\\"authors\\\": \\\"Taubenfeld, Amir and Sheffer, Tom and Ofek, Eran and Feder, Amir and Goldstein, ...\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"Findings of the Association for Computational Linguistics: ACL 2025\\\"}, {\\\"key\\\": \\\"thirukovalluru2024atomic\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Atomic Self-Consistency for Better Long Form Generations\\\", \\\"authors\\\": \\\"Thirukovalluru, Raghuveer and Huang, Yukun and Dhingra, Bhuwan\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"Proceedings of the 2024 Conference on Empirical Methods in Natural Language Proc...\\\"}, {\\\"key\\\": \\\"tjongkimsang2003conll\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Introduction to the CoNLL-2003 Shared Task: Language-Independent Named Entity Recognition\\\", \\\"authors\\\": \\\"Sang, Erik F. Tjong Kim and Meulder, Fien De\\\", \\\"year\\\": \\\"2003\\\", \\\"venue\\\": \\\"CoNLL 2003\\\"}, {\\\"key\\\": \\\"vashurin2025cocoa\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Uncertainty Quantification for LLMs through Minimum Bayes Risk: Bridging Confidence and Consistency\\\", \\\"authors\\\": \\\"Vashurin, Roman and Goloburda, Maiya and Ilina, Albina and Rubashevskii, Aleksan...\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"NeurIPS 2025\\\"}, {\\\"key\\\": \\\"wadhwa2023revisiting\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Revisiting Relation Extraction in the era of Large Language Models\\\", \\\"authors\\\": \\\"Wadhwa, Somin and Amir, Silvio and Wallace, Byron\\\", \\\"year\\\": \\\"2023\\\", \\\"venue\\\": \\\"Proceedings of the 61st Annual Meeting of the Association for Computational Ling...\\\"}, {\\\"key\\\": \\\"wang2023instructuie\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"InstructUIE: Multi-task Instruction Tuning for Unified Information Extraction\\\", \\\"authors\\\": \\\"Wang, Xiao and Zhou, Weikang and Zu, Can and Xia, Han and Chen, Tianze and Zhang...\\\", \\\"year\\\": \\\"2023\\\", \\\"venue\\\": \\\"arXiv preprint arXiv:2304.08085\\\"}, {\\\"key\\\": \\\"wang2023selfconsistency\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Self-Consistency Improves Chain of Thought Reasoning in Language Models\\\", \\\"authors\\\": \\\"Wang, Xuezhi and Wei, Jason and Schuurmans, Dale and Le, Quoc and Chi, Ed and Na...\\\", \\\"year\\\": \\\"2023\\\", \\\"venue\\\": \\\"ICLR 2023\\\"}, {\\\"key\\\": \\\"wang2025make\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Make Every Penny Count: Difficulty-Adaptive Self-Consistency for Cost-Efficient Reasoning\\\", \\\"authors\\\": \\\"Wang, Xinglin and Feng, Shaoxiong and Li, Yiwei and Yuan, Peiwen and Zhang, Yueq...\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"Findings of the Association for Computational Linguistics: NAACL 2025\\\"}, {\\\"key\\\": \\\"wang2024mathshepherd\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Math-Shepherd: Verify and Reinforce LLMs Step-by-step without Human Annotations\\\", \\\"authors\\\": \\\"Wang, Peiyi and Li, Lei and Shao, Zhihong and Xu, Runxin and Dai, Damai and Li, ...\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"ACL 2024\\\"}, {\\\"key\\\": \\\"wang2025rankedvoting\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Ranked Voting based Self-Consistency of Large Language Models\\\", \\\"authors\\\": \\\"Wang, Weiqin and Wang, Yile and Huang, Hui\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"ACL Findings 2025\\\"}, {\\\"key\\\": \\\"wen2025know\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Know Your Limits: A Survey of Abstention in Large Language Models\\\", \\\"authors\\\": \\\"Wen, Bingbing and Yao, Jihan and Feng, Shangbin and Xu, Chenjun and Tsvetkov, Yu...\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"Transactions of the Association for Computational Linguistics\\\"}, {\\\"key\\\": \\\"willard2023guided\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Efficient Guided Generation for Large Language Models\\\", \\\"authors\\\": \\\"Willard, Brandon T. and Louf, Rémi\\\", \\\"year\\\": \\\"2023\\\", \\\"venue\\\": \\\"arXiv preprint arXiv:2307.09702\\\"}, {\\\"key\\\": \\\"xia2025survey\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"A Survey of Uncertainty Estimation Methods on Large Language Models\\\", \\\"authors\\\": \\\"Xia, Zhiqiu and Xu, Jinxuan and Zhang, Yuqian and Liu, Hang\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"ACL Findings 2025\\\"}, {\\\"key\\\": \\\"xiao2019uncertainty\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Quantifying Uncertainties in Natural Language Processing Tasks\\\", \\\"authors\\\": \\\"Xiao, Yijun and Wang, William Yang\\\", \\\"year\\\": \\\"2019\\\", \\\"venue\\\": \\\"Proceedings of the AAAI Conference on Artificial Intelligence\\\"}, {\\\"key\\\": \\\"zhang2023ener\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"E-NER: Evidential Deep Learning for Trustworthy Named Entity Recognition\\\", \\\"authors\\\": \\\"Zhang, Zhen and Hu, Mengting and Zhao, Shiwan and Huang, Minlie and Wang, Haotia...\\\", \\\"year\\\": \\\"2023\\\", \\\"venue\\\": \\\"Findings of the Association for Computational Linguistics: ACL 2023\\\"}, {\\\"key\\\": \\\"zheng2024llamafactory\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"LlamaFactory: Unified Efficient Fine-Tuning of 100+ Language Models\\\", \\\"authors\\\": \\\"Zheng, Yaowei and Zhang, Richong and Zhang, Junhao and Ye, Yanhan and Luo, Zheya...\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"Proceedings of the 62nd Annual Meeting of the Association for Computational Ling...\\\"}, {\\\"key\\\": \\\"zhou2024uniner\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"UniversalNER: Targeted Distillation from Large Language Models for Open Named Entity Recognition\\\", \\\"authors\\\": \\\"Zhou, Wenxuan and Zhang, Sheng and Gu, Yu and Chen, Muhao and Poon, Hoifung\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"Proceedings of the International Conference on Learning Representations (ICLR)\\\"}, {\\\"key\\\": \\\"xiong2024llm\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Can LLMs Express Their Uncertainty? An Empirical Evaluation of Confidence Elicitation in LLMs\\\", \\\"authors\\\": \\\"Xiong, Miao and Hu, Zhiyuan and Lu, Xinyang and Li, Yifei and Fu, Jie and He, Ju...\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"Proceedings of the International Conference on Learning Representations (ICLR)\\\"}, {\\\"key\\\": \\\"muller2021understanding\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Understanding the Properties of Minimum Bayes Risk Decoding in Neural Machine Translation\\\", \\\"authors\\\": \\\"M\\\\\\\\\\\\\\\"uller, Mathias and Sennrich, Rico\\\", \\\"year\\\": \\\"2021\\\", \\\"venue\\\": \\\"Proceedings of the 59th Annual Meeting of the Association for Computational Ling...\\\"}, {\\\"key\\\": \\\"heo2025uncertainty\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Do LLMs Estimate Uncertainty Well in Instruction Following?\\\", \\\"authors\\\": \\\"Heo, Juyeon and Xiong, Miao and Heinze-Deml, Christina and Narain, Jaya\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"Proceedings of the International Conference on Learning Representations (ICLR)\\\"}, {\\\"key\\\": \\\"eikema2025structured\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Structure-Conditional Minimum Bayes Risk Decoding\\\", \\\"authors\\\": \\\"Eikema, Bryan and Rutkiewicz, Anna and Giulianelli, Mario\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"Proceedings of the 2025 Conference on Empirical Methods in Natural Language Proc...\\\"}, {\\\"key\\\": \\\"zhang2025tts\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"A Survey on Test-Time Scaling in Large Language Models: What, How, Where, and How Well?\\\", \\\"authors\\\": \\\"Zhang, Qiyuan and Lyu, Fuyuan and Sun, Zexu and Wang, Lei and Zhang, Weixu and G...\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"arXiv preprint arXiv:2503.24235\\\"}, {\\\"key\\\": \\\"venktesh2025trust\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Trust but Verify! A Survey on Verification Design for Test-time Scaling\\\", \\\"authors\\\": \\\"Venktesh, V and Rathee, Mandeep and Anand, Avishek\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"arXiv preprint arXiv:2508.16665\\\"}, {\\\"key\\\": \\\"jinnai2024mbr\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Model-Based Minimum Bayes Risk Decoding for Text Generation\\\", \\\"authors\\\": \\\"Jinnai, Yuu and Morimura, Tetsuro and Honda, Ukyo and Ariu, Kaito and Abe, Kensh...\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"Proceedings of the 41st International Conference on Machine Learning (ICML)\\\"}], \\\"tex_citations\\\": [{\\\"key\\\": \\\"wang2023selfconsistency\\\", \\\"file\\\": \\\"sections/introduction.tex\\\", \\\"line\\\": 4, \\\"command\\\": \\\"citealp\\\"}, {\\\"key\\\": \\\"snell2025scaling\\\", \\\"file\\\": \\\"sections/introduction.tex\\\", \\\"line\\\": 5, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"brown2024monkeys\\\", \\\"file\\\": \\\"sections/introduction.tex\\\", \\\"line\\\": 5, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"wang2023selfconsistency\\\", \\\"file\\\": \\\"sections/introduction.tex\\\", \\\"line\\\": 15, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"chen2024usc\\\", \\\"file\\\": \\\"sections/introduction.tex\\\", \\\"line\\\": 15, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"taubenfeld2025cisc\\\", \\\"file\\\": \\\"sections/introduction.tex\\\", \\\"line\\\": 15, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"kang2025selfcertainty\\\", \\\"file\\\": \\\"sections/introduction.tex\\\", \\\"line\\\": 15, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"nedellec2026consistency\\\", \\\"file\\\": \\\"sections/introduction.tex\\\", \\\"line\\\": 16, \\\"command\\\": \\\"citet\\\"}, {\\\"key\\\": \\\"willard2023guided\\\", \\\"file\\\": \\\"sections/introduction.tex\\\", \\\"line\\\": 19, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"eikema2022sampling\\\", \\\"file\\\": \\\"sections/introduction.tex\\\", \\\"line\\\": 24, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"freitag2022high\\\", \\\"file\\\": \\\"sections/introduction.tex\\\", \\\"line\\\": 24, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"muller2021understanding\\\", \\\"file\\\": \\\"sections/introduction.tex\\\", \\\"line\\\": 24, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"luan2018scierc\\\", \\\"file\\\": \\\"sections/introduction.tex\\\", \\\"line\\\": 35, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"tjongkimsang2003conll\\\", \\\"file\\\": \\\"sections/introduction.tex\\\", \\\"line\\\": 35, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"derczynski2017wnut\\\", \\\"file\\\": \\\"sections/introduction.tex\\\", \\\"line\\\": 35, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"nedellec2026consistency\\\", \\\"file\\\": \\\"sections/introduction.tex\\\", \\\"line\\\": 51, \\\"command\\\": \\\"citet\\\"}, {\\\"key\\\": \\\"wang2023selfconsistency\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 4, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"chen2024usc\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 5, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"thirukovalluru2024atomic\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 5, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"manakul2023selfcheckgpt\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 5, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"zhang2025tts\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 6, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"snell2025scaling\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 6, \\\"command\\\": \\\"citet\\\"}, {\\\"key\\\": \\\"brown2024monkeys\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 6, \\\"command\\\": \\\"citet\\\"}, {\\\"key\\\": \\\"taubenfeld2025cisc\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 7, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"kang2025selfcertainty\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 7, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"kim2026reasc\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 7, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"wang2025rankedvoting\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 7, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"oh2025latentsc\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 7, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"feng2025optimal\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 8, \\\"command\\\": \\\"citet\\\"}, {\\\"key\\\": \\\"wang2025make\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 8, \\\"command\\\": \\\"citet\\\"}, {\\\"key\\\": \\\"li2025llms\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 8, \\\"command\\\": \\\"citet\\\"}, {\\\"key\\\": \\\"nedellec2026consistency\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 13, \\\"command\\\": \\\"citet\\\"}, {\\\"key\\\": \\\"vashurin2025cocoa\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 16, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"zhou2024uniner\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 17, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"sainz2024gollie\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 17, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"josifoski2022genie\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 17, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"li2023codeie\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 17, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"wadhwa2023revisiting\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 17, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"wang2023instructuie\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 17, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"willard2023guided\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 17, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"geng2024confidence\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 20, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"wen2025know\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 20, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"xia2025survey\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 20, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"hobelsberger2025systematic\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 20, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"xiong2024llm\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 20, \\\"command\\\": \\\"citet\\\"}, {\\\"key\\\": \\\"heo2025uncertainty\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 20, \\\"command\\\": \\\"citet\\\"}, {\\\"key\\\": \\\"kuhn2023semantic\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 21, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"kossen2024semantic\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 21, \\\"command\\\": \\\"citet\\\"}, {\\\"key\\\": \\\"kadavath2022language\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 21, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"malinin2021uncertainty\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 21, \\\"command\\\": \\\"citet\\\"}, {\\\"key\\\": \\\"guo2017calibration\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 23, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"desai2020calibration\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 23, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"lakshminarayanan2017ensembles\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 23, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"gal2016dropout\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 23, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"xiao2019uncertainty\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 24, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"shelmanov2021active\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 24, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"zhang2023ener\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 24, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"kim2024verifiner\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 24, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"he2024uncertainty\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 24, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"fisch2021conformal\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 25, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"angelopoulos2021conformal\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 25, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"cobbe2021verifiers\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 25, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"lightman2024verify\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 25, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"venktesh2025trust\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 25, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"wang2024mathshepherd\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 25, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"eikema2022sampling\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 26, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"freitag2022high\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 26, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"jinnai2024mbr\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 26, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"eikema2025structured\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 27, \\\"command\\\": \\\"citet\\\"}, {\\\"key\\\": \\\"geifman2017selective\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 28, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"culotta2004confidence\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 28, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"willard2023guided\\\", \\\"file\\\": \\\"sections/method.tex\\\", \\\"line\\\": 5, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"fleiss1971agreement\\\", \\\"file\\\": \\\"sections/method.tex\\\", \\\"line\\\": 34, \\\"command\\\": \\\"citet\\\"}, {\\\"key\\\": \\\"jaccard1901distribution\\\", \\\"file\\\": \\\"sections/method.tex\\\", \\\"line\\\": 45, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"luan2018scierc\\\", \\\"file\\\": \\\"sections/experiments.tex\\\", \\\"line\\\": 9, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"tjongkimsang2003conll\\\", \\\"file\\\": \\\"sections/experiments.tex\\\", \\\"line\\\": 10, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"derczynski2017wnut\\\", \\\"file\\\": \\\"sections/experiments.tex\\\", \\\"line\\\": 11, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"zheng2024llamafactory\\\", \\\"file\\\": \\\"sections/experiments.tex\\\", \\\"line\\\": 14, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"willard2023guided\\\", \\\"file\\\": \\\"sections/experiments.tex\\\", \\\"line\\\": 21, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"kuhn2023semantic\\\", \\\"file\\\": \\\"sections/experiments.tex\\\", \\\"line\\\": 60, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"xiong2024llm\\\", \\\"file\\\": \\\"sections/experiments.tex\\\", \\\"line\\\": 74, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"brown2024monkeys\\\", \\\"file\\\": \\\"sections/experiments.tex\\\", \\\"line\\\": 141, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"snell2025scaling\\\", \\\"file\\\": \\\"sections/experiments.tex\\\", \\\"line\\\": 141, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"cobbe2021verifiers\\\", \\\"file\\\": \\\"sections/experiments.tex\\\", \\\"line\\\": 141, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"eikema2022sampling\\\", \\\"file\\\": \\\"sections/discussion.tex\\\", \\\"line\\\": 28, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"muller2021understanding\\\", \\\"file\\\": \\\"sections/discussion.tex\\\", \\\"line\\\": 28, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"freitag2022high\\\", \\\"file\\\": \\\"sections/discussion.tex\\\", \\\"line\\\": 29, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"jinnai2024mbr\\\", \\\"file\\\": \\\"sections/discussion.tex\\\", \\\"line\\\": 29, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"eikema2025structured\\\", \\\"file\\\": \\\"sections/discussion.tex\\\", \\\"line\\\": 30, \\\"command\\\": \\\"citet\\\"}, {\\\"key\\\": \\\"cobbe2021verifiers\\\", \\\"file\\\": \\\"sections/discussion.tex\\\", \\\"line\\\": 53, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"venktesh2025trust\\\", \\\"file\\\": \\\"sections/discussion.tex\\\", \\\"line\\\": 53, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"brown2024monkeys\\\", \\\"file\\\": \\\"sections/appendix.tex\\\", \\\"line\\\": 193, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"snell2025scaling\\\", \\\"file\\\": \\\"sections/appendix.tex\\\", \\\"line\\\": 193, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"willard2023guided\\\", \\\"file\\\": \\\"sections/appendix.tex\\\", \\\"line\\\": 394, \\\"command\\\": \\\"cite\\\"}], \\\"online_verification\\\": [{\\\"key\\\": \\\"angelopoulos2021conformal\\\", \\\"title\\\": \\\"Uncertainty Sets for Image Classifiers using Conformal Prediction\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Uncertainty Sets for Image Classifiers using Conformal Prediction\\\", \\\"matched_year\\\": \\\"2020\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"brown2024monkeys\\\", \\\"title\\\": \\\"Large Language Monkeys: Scaling Inference Compute with Repeated Sampling\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Large Language Monkeys: Scaling Inference Compute with Repeated Sampling\\\", \\\"matched_year\\\": \\\"2024\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"chen2024usc\\\", \\\"title\\\": \\\"Universal Self-Consistency for Large Language Model Generation\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Universal Self-Consistency for Large Language Model Generation\\\", \\\"matched_year\\\": \\\"2023\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"cobbe2021verifiers\\\", \\\"title\\\": \\\"Training Verifiers to Solve Math Word Problems\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Training Verifiers to Solve Math Word Problems\\\", \\\"matched_year\\\": \\\"2021\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"culotta2004confidence\\\", \\\"title\\\": \\\"Confidence Estimation for Information Extraction\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Confidence estimation for information extraction\\\", \\\"matched_year\\\": \\\"2004\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"derczynski2017wnut\\\", \\\"title\\\": \\\"Results of the WNUT2017 Shared Task on Novel and Emerging Entity Recognition\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Results of the WNUT2017 Shared Task on Novel and Emerging Entity Recognition\\\", \\\"matched_year\\\": \\\"2017\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"desai2020calibration\\\", \\\"title\\\": \\\"Calibration of Pre-trained Transformers\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Calibration of Pre-trained Transformers\\\", \\\"matched_year\\\": \\\"2020\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"eikema2022sampling\\\", \\\"title\\\": \\\"Sampling-Based Approximations to Minimum Bayes Risk Decoding for Neural Machine Translation\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Sampling-Based Approximations to Minimum Bayes Risk Decoding for Neural Machine Translation\\\", \\\"matched_year\\\": \\\"2022\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"fisch2021conformal\\\", \\\"title\\\": \\\"Few-Shot Conformal Prediction with Auxiliary Tasks\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Few-shot Conformal Prediction with Auxiliary Tasks\\\", \\\"matched_year\\\": \\\"2021\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"freitag2022high\\\", \\\"title\\\": \\\"High Quality Rather than High Model Probability: Minimum Bayes Risk Decoding with Neural Metrics\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"High Quality Rather than High Model Probability: Minimum Bayes Risk Decoding with Neural Metrics\\\", \\\"matched_year\\\": \\\"2022\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"he2024uncertainty\\\", \\\"title\\\": \\\"Uncertainty Estimation on Sequential Labeling via Uncertainty Transmission\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Uncertainty Estimation on Sequential Labeling via Uncertainty Transmission\\\", \\\"matched_year\\\": \\\"2024\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"fleiss1971agreement\\\", \\\"title\\\": \\\"Measuring nominal scale agreement among many raters.\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Measuring nominal scale agreement among many raters.\\\", \\\"matched_year\\\": \\\"1971\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"gal2016dropout\\\", \\\"title\\\": \\\"Dropout as a Bayesian Approximation: Representing Model Uncertainty in Deep Learning\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Dropout as a Bayesian Approximation: Representing Model Uncertainty in Deep Learning\\\", \\\"matched_year\\\": \\\"2015\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"geifman2017selective\\\", \\\"title\\\": \\\"Selective Classification for Deep Neural Networks\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Selective Classification for Deep Neural Networks\\\", \\\"matched_year\\\": \\\"2017\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"feng2025optimal\\\", \\\"title\\\": \\\"Optimal Self-Consistency for Efficient Reasoning with Large Language Models\\\", \\\"status\\\": \\\"mismatch\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Optimal Self-Consistency for Efficient Reasoning with Large Language Models\\\", \\\"matched_year\\\": \\\"2025\\\", \\\"mismatch_fields\\\": [\\\"first_author: bib=feng vs api=austin\\\"], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"geng2024confidence\\\", \\\"title\\\": \\\"A Survey of Confidence Estimation and Calibration in Large Language Models\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"A Survey of Confidence Estimation and Calibration in Large Language Models\\\", \\\"matched_year\\\": \\\"2024\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"guo2017calibration\\\", \\\"title\\\": \\\"On Calibration of Modern Neural Networks\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"On Calibration of Modern Neural Networks\\\", \\\"matched_year\\\": \\\"2017\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"hobelsberger2025systematic\\\", \\\"title\\\": \\\"Systematic Evaluation of Uncertainty Estimation Methods in Large Language Models\\\", \\\"status\\\": \\\"not_found\\\", \\\"confidence\\\": 0.236, \\\"matched_title\\\": \\\"A new criterion for assessing discriminant validity in variance-based structural equation modeling\\\", \\\"matched_year\\\": \\\"\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"best match similarity 0.24 below threshold 0.82\\\"}, {\\\"key\\\": \\\"jaccard1901distribution\\\", \\\"title\\\": \\\"Étude comparative de la distribution florale dans une portion des Alpes et du Jura\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Étude comparative de la distribution florale dans une portion des Alpes et du Jura\\\", \\\"matched_year\\\": \\\"1901\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"josifoski2022genie\\\", \\\"title\\\": \\\"GenIE: Generative Information Extraction\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"GenIE: Generative Information Extraction\\\", \\\"matched_year\\\": \\\"2022\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"kadavath2022language\\\", \\\"title\\\": \\\"Language Models (Mostly) Know What They Know\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Language Models (Mostly) Know What They Know\\\", \\\"matched_year\\\": \\\"2022\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"kang2025selfcertainty\\\", \\\"title\\\": \\\"Scalable Best-of-N Selection for Large Language Models via Self-Certainty\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Scalable Best-of-N Selection for Large Language Models via Self-Certainty\\\", \\\"matched_year\\\": \\\"2025\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"kim2024verifiner\\\", \\\"title\\\": \\\"VerifiNER: Verification-augmented NER via Knowledge-grounded Reasoning with Large Language Models\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"VerifiNER: Verification-augmented NER via Knowledge-grounded Reasoning with Large Language Models\\\", \\\"matched_year\\\": \\\"2024\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"kim2026reasc\\\", \\\"title\\\": \\\"Reliability-Aware Adaptive Self-Consistency for Efficient Sampling in LLM Reasoning\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Reliability-Aware Adaptive Self-Consistency for Efficient Sampling in LLM Reasoning\\\", \\\"matched_year\\\": \\\"2026\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"kossen2024semantic\\\", \\\"title\\\": \\\"Semantic Entropy Probes: Robust and Cheap Hallucination Detection in LLMs\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Semantic Entropy Probes: Robust and Cheap Hallucination Detection in LLMs\\\", \\\"matched_year\\\": \\\"2024\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"li2025llms\\\", \\\"title\\\": \\\"LLMs Can Generate a Better Answer by Aggregating Their Own Responses\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"LLMs Can Generate a Better Answer by Aggregating Their Own Responses\\\", \\\"matched_year\\\": \\\"2025\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"kuhn2023semantic\\\", \\\"title\\\": \\\"Semantic Uncertainty: Linguistic Invariances for Uncertainty Estimation in Natural Language Generation\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Semantic Uncertainty: Linguistic Invariances for Uncertainty Estimation in Natural Language Generation\\\", \\\"matched_year\\\": \\\"2023\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"malinin2021uncertainty\\\", \\\"title\\\": \\\"Uncertainty Estimation in Autoregressive Structured Prediction\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Uncertainty Estimation in Autoregressive Structured Prediction\\\", \\\"matched_year\\\": \\\"2020\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"lakshminarayanan2017ensembles\\\", \\\"title\\\": \\\"Simple and Scalable Predictive Uncertainty Estimation using Deep Ensembles\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Simple and Scalable Predictive Uncertainty Estimation using Deep Ensembles\\\", \\\"matched_year\\\": \\\"2016\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"li2023codeie\\\", \\\"title\\\": \\\"CodeIE: Large Code Generation Models are Better Few-Shot Information Extractors\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"CodeIE: Large Code Generation Models are Better Few-Shot Information Extractors\\\", \\\"matched_year\\\": \\\"2023\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"lightman2024verify\\\", \\\"title\\\": \\\"Let's Verify Step by Step\\\", \\\"status\\\": \\\"not_found\\\", \\\"confidence\\\": 0.246, \\\"matched_title\\\": \\\"Development and dosimetric verification of static SHArc: Step‐and‐shoot carbon ion arc therapy for LET &lt;sub>d&lt;/sub> escalation in pancreatic tumors\\\", \\\"matched_year\\\": \\\"\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"best match similarity 0.25 below threshold 0.82\\\"}, {\\\"key\\\": \\\"luan2018scierc\\\", \\\"title\\\": \\\"Multi-Task Identification of Entities, Relations, and Coreference for Scientific Knowledge Graph Construction\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Multi-Task Identification of Entities, Relations, and Coreference for Scientific Knowledge Graph Construction\\\", \\\"matched_year\\\": \\\"2018\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"manakul2023selfcheckgpt\\\", \\\"title\\\": \\\"SelfCheckGPT: Zero-Resource Black-Box Hallucination Detection for Generative Large Language Models\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"SelfCheckGPT: Zero-Resource Black-Box Hallucination Detection for Generative Large Language Models\\\", \\\"matched_year\\\": \\\"2023\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"nedellec2026consistency\\\", \\\"title\\\": \\\"Consistency–accuracy correlation in hard-prompted LLMs for entity and relation extraction: empirical findings from plant-health data\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Consistency–accuracy correlation in hard-prompted LLMs for entity and relation extraction: empirical findings from plant-health data\\\", \\\"matched_year\\\": \\\"2026\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"oh2025latentsc\\\", \\\"title\\\": \\\"Latent Self-Consistency for Reliable Majority-Set Selection in Short- and Long-Answer Reasoning\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Latent Self-Consistency for Reliable Majority-Set Selection in Short- and Long-Answer Reasoning\\\", \\\"matched_year\\\": \\\"2026\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"sainz2024gollie\\\", \\\"title\\\": \\\"GoLLIE: Annotation Guidelines improve Zero-Shot Information-Extraction\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"GoLLIE: Annotation Guidelines improve Zero-Shot Information-Extraction\\\", \\\"matched_year\\\": \\\"2023\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"shelmanov2021active\\\", \\\"title\\\": \\\"Active Learning for Sequence Tagging with Deep Pre-trained Models and Bayesian Uncertainty Estimates\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Active Learning for Sequence Tagging with Deep Pre-trained Models and Bayesian Uncertainty Estimates\\\", \\\"matched_year\\\": \\\"2021\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"snell2025scaling\\\", \\\"title\\\": \\\"Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters\\\", \\\"status\\\": \\\"mismatch\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters\\\", \\\"matched_year\\\": \\\"2024\\\", \\\"mismatch_fields\\\": [\\\"first_author: bib=snell vs api=charlie\\\"], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"taubenfeld2025cisc\\\", \\\"title\\\": \\\"Confidence Improves Self-Consistency in LLMs\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Confidence Improves Self-Consistency in LLMs\\\", \\\"matched_year\\\": \\\"2025\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"thirukovalluru2024atomic\\\", \\\"title\\\": \\\"Atomic Self-Consistency for Better Long Form Generations\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Atomic Self-Consistency for Better Long Form Generations\\\", \\\"matched_year\\\": \\\"2024\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"tjongkimsang2003conll\\\", \\\"title\\\": \\\"Introduction to the CoNLL-2003 Shared Task: Language-Independent Named Entity Recognition\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Introduction to the CoNLL-2003 Shared Task: Language-Independent Named Entity Recognition\\\", \\\"matched_year\\\": \\\"2003\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"vashurin2025cocoa\\\", \\\"title\\\": \\\"Uncertainty Quantification for LLMs through Minimum Bayes Risk: Bridging Confidence and Consistency\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Uncertainty Quantification for LLMs through Minimum Bayes Risk: Bridging Confidence and Consistency\\\", \\\"matched_year\\\": \\\"2025\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"wadhwa2023revisiting\\\", \\\"title\\\": \\\"Revisiting Relation Extraction in the era of Large Language Models\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Revisiting Relation Extraction in the era of Large Language Models\\\", \\\"matched_year\\\": \\\"2023\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"wang2023instructuie\\\", \\\"title\\\": \\\"InstructUIE: Multi-task Instruction Tuning for Unified Information Extraction\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"InstructUIE: Multi-task Instruction Tuning for Unified Information Extraction\\\", \\\"matched_year\\\": \\\"2023\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"wang2023selfconsistency\\\", \\\"title\\\": \\\"Self-Consistency Improves Chain of Thought Reasoning in Language Models\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Self-Consistency Improves Chain of Thought Reasoning in Language Models\\\", \\\"matched_year\\\": \\\"2022\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"wang2025make\\\", \\\"title\\\": \\\"Make Every Penny Count: Difficulty-Adaptive Self-Consistency for Cost-Efficient Reasoning\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Make Every Penny Count: Difficulty-Adaptive Self-Consistency for Cost-Efficient Reasoning\\\", \\\"matched_year\\\": \\\"2025\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"wang2024mathshepherd\\\", \\\"title\\\": \\\"Math-Shepherd: Verify and Reinforce LLMs Step-by-step without Human Annotations\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Math-Shepherd: Verify and Reinforce LLMs Step-by-step without Human Annotations\\\", \\\"matched_year\\\": \\\"2024\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"wang2025rankedvoting\\\", \\\"title\\\": \\\"Ranked Voting based Self-Consistency of Large Language Models\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Ranked Voting based Self-Consistency of Large Language Models\\\", \\\"matched_year\\\": \\\"2025\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"wen2025know\\\", \\\"title\\\": \\\"Know Your Limits: A Survey of Abstention in Large Language Models\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Know Your Limits: A Survey of Abstention in Large Language Models\\\", \\\"matched_year\\\": \\\"2025\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"willard2023guided\\\", \\\"title\\\": \\\"Efficient Guided Generation for Large Language Models\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Efficient Guided Generation for Large Language Models\\\", \\\"matched_year\\\": \\\"2023\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"xia2025survey\\\", \\\"title\\\": \\\"A Survey of Uncertainty Estimation Methods on Large Language Models\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"A Survey of Uncertainty Estimation Methods on Large Language Models\\\", \\\"matched_year\\\": \\\"2025\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"xiao2019uncertainty\\\", \\\"title\\\": \\\"Quantifying Uncertainties in Natural Language Processing Tasks\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Quantifying Uncertainties in Natural Language Processing Tasks\\\", \\\"matched_year\\\": \\\"2019\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"zhang2023ener\\\", \\\"title\\\": \\\"E-NER: Evidential Deep Learning for Trustworthy Named Entity Recognition\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"E-NER: Evidential Deep Learning for Trustworthy Named Entity Recognition\\\", \\\"matched_year\\\": \\\"2023\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"zheng2024llamafactory\\\", \\\"title\\\": \\\"LlamaFactory: Unified Efficient Fine-Tuning of 100+ Language Models\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"LlamaFactory: Unified Efficient Fine-Tuning of 100+ Language Models\\\", \\\"matched_year\\\": \\\"2024\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"zhou2024uniner\\\", \\\"title\\\": \\\"UniversalNER: Targeted Distillation from Large Language Models for Open Named Entity Recognition\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"UniversalNER: Targeted Distillation from Large Language Models for Open Named Entity Recognition\\\", \\\"matched_year\\\": \\\"2023\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"xiong2024llm\\\", \\\"title\\\": \\\"Can LLMs Express Their Uncertainty? An Empirical Evaluation of Confidence Elicitation in LLMs\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Can LLMs Express Their Uncertainty? An Empirical Evaluation of Confidence Elicitation in LLMs\\\", \\\"matched_year\\\": \\\"2023\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"muller2021understanding\\\", \\\"title\\\": \\\"Understanding the Properties of Minimum Bayes Risk Decoding in Neural Machine Translation\\\", \\\"status\\\": \\\"mismatch\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Understanding the Properties of Minimum Bayes Risk Decoding in Neural Machine Translation\\\", \\\"matched_year\\\": \\\"2021\\\", \\\"mismatch_fields\\\": [\\\"first_author: bib=m\\\\\\\\\\\\\\\"uller vs api=müller\\\"], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"heo2025uncertainty\\\", \\\"title\\\": \\\"Do LLMs Estimate Uncertainty Well in Instruction Following?\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 0.983, \\\"matched_title\\\": \\\"Do LLMs estimate uncertainty well in instruction-following?\\\", \\\"matched_year\\\": \\\"2024\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"eikema2025structured\\\", \\\"title\\\": \\\"Structure-Conditional Minimum Bayes Risk Decoding\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Structure-Conditional Minimum Bayes Risk Decoding\\\", \\\"matched_year\\\": \\\"2025\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"zhang2025tts\\\", \\\"title\\\": \\\"A Survey on Test-Time Scaling in Large Language Models: What, How, Where, and How Well?\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"A Survey on Test-Time Scaling in Large Language Models: What, How, Where, and How Well?\\\", \\\"matched_year\\\": \\\"2025\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"venktesh2025trust\\\", \\\"title\\\": \\\"Trust but Verify! A Survey on Verification Design for Test-time Scaling\\\", \\\"status\\\": \\\"not_found\\\", \\\"confidence\\\": 0.252, \\\"matched_title\\\": \\\"The PRISMA Statement for Reporting Systematic Reviews and Meta-Analyses of Studies That Evaluate Health Care Interventions: Explanation and Elaboration\\\", \\\"matched_year\\\": \\\"\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"best match similarity 0.25 below threshold 0.82\\\"}, {\\\"key\\\": \\\"jinnai2024mbr\\\", \\\"title\\\": \\\"Model-Based Minimum Bayes Risk Decoding for Text Generation\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Model-Based Minimum Bayes Risk Decoding for Text Generation\\\", \\\"matched_year\\\": \\\"2023\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}]}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
      "numLines": 1,
      "startLine": 0,
      "totalLines": 1
    }
  },
  "sourceToolAssistantUUID": "c9cfc4f5-7d7c-4bfa-8311-9dd65f7496d0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "f49c1ccb-97a0-4961-857d-2db0aa0e0624",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 63_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[Round 1 审稿请求]: ## Round 1 审稿任务 — Reviewer 2  **你的侧重**：新颖性 + 定位完整性 + 写作质量 + 格式合规  ### 投稿信息 - **目标 venue**: EMNLP 2026 Findings (ARR May cycle) - **Deadline**: 2026-05-25 - **格式**: ACL template, 长文 8 页…",
  "leafUuid": "96fb538e-bfe1-4500-9b2c-223c81575766",
  "sessionId": "f49c1ccb-97a0-4961-857d-2db0aa0e0624"
}
```

---

### Runtime record

_source line 64_

```json
{
  "type": "ai-title",
  "aiTitle": "Round 1 review for EMNLP 2026 structured IE paper",
  "sessionId": "f49c1ccb-97a0-4961-857d-2db0aa0e0624"
}
```

---

### Assistant

_source line 65 · 2026-05-15T15:02:13.822Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the information I need. Let me compile my review.

Key findings from reference verification:
- 62 bib entries, all 62 cited (0 orphan, 0 missing) - clean
- 56 verified online, 3 not found (hobelsberger2025systematic, lightman2024verify, venktesh2025trust), 3 mismatch (feng2025optimal - author name format, snell2025scaling - author name format, muller2021understanding - LaTeX encoding)
- The "not found" entries are likely just not indexed in OpenAlex yet (recent papers or specific venues)


- The "mismatches" are just author name format differences (first vs last name, LaTeX encoding) - not real issues

Now let me look at the page count issue. The main body sections break down to roughly 383 lines of content across the abstract, introduction with a full-width figure, related work, method with equations, experiments with tables and figures, discussion, and conclusion.

I'm trying to figure out the exact formatting implications here - the ACL review template with the `review` option affects how the document renders, and I need to account for whether that's single or two-column format, plus how the full-width figures and tables will impact the overall page count.

Looking at the content breakdown, I'm estimating around 9-11 pages of main body material, which the Director also flagged as exceeding the 8-page limit. This is a significant constraint I need to address.

Now I'm turning to assess the novelty - the key contribution appears to be identifying this correlation-selection gap, where consistency signals can predict quality but don't actually help identify the best outputs.

Breaking this down: instance-level signals inherently can't perform selection by design, so that's not really a discovery. The more substantive finding is how log-probability scores get compressed under constrained decoding, which prevents effective selection - the non-tied subset analysis showing a 2.9 percentage point improvement with p=0.01 gives solid mechanistic support for this. The MBR failure within instances is somewhat intuitive given structured outputs, but the observation that signal rankings shift based on task difficulty does provide practical value. Compared to Nédellec et al., the incremental contributions around structural matching, selection analysis, and difficulty gradients are defensible, though the structural matching component itself feels somewhat limited.

The real novelty centers on the LP compression diagnosis and discovering that MBR's utility-quality tradeoff breaks down for structured outputs. The "gap" framing combines a definitional constraint with an empirical observation, which feels somewhat constructed.

Looking at the writing itself, the paper is well-structured with rigorous statistical work - multiple seeds, bootstrap confidence intervals, equivalence testing - and appropriately cautious about limitations. But the abstract is packed too densely, the title makes a strong claim from limited evidence (just two 8B models), and the paper exceeds the page limit while hedging so heavily in places that the core message gets diluted.

Now checking format compliance and potential issues. The LaTeX setup looks correct with proper anonymization and required sections, but the page count is a real concern for desk rejection. The self-citation handling is fine, and there are no anonymity problems. Let me work through a detailed review.

For scoring, I'm weighing the solid statistical methodology against the limited novelty and mostly negative results. The LP compression diagnosis is genuinely useful, but the framing oversells the contribution since most signals are instance-level by definition. The soundness is around 3.5 given the methodology is solid but the definitional versus empirical distinction gets muddled. Excitement sits at 2.5 due to the negative result and limited novelty despite the good diagnostic work. Overall, this lands between a resubmit recommendation and findings acceptance, probably around 2.5 to 3.

The page limit violation is concerning—if it's significantly over the limit, that's a critical issue that ARR reviewers would flag, though they typically don't desk-reject on their own. I should note this prominently in my review.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "96fb538e-bfe1-4500-9b2c-223c81575766",
  "isSidechain": false,
  "requestId": "req_011Cb4ZBzznawEnFdiBJ8xhe",
  "type": "assistant",
  "uuid": "4a0ad4b8-34dc-4bbb-9e24-d831f0e17d3e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "f49c1ccb-97a0-4961-857d-2db0aa0e0624",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014WBX1yKtnWj44GeZCuBbJ1",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 18157,
      "cache_read_input_tokens": 80545,
      "output_tokens": 7108,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 18157,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 7108,
          "cache_read_input_tokens": 80545,
          "cache_creation_input_tokens": 18157,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 18157
          },
          "type": "message"
        }
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

_source line 66 · 2026-05-15T15:02:16.599Z_

全部材料已读完。引用验证结果：62 条 bib entry 全部被正文引用（0 orphan, 0 missing），56 条在线验证通过，3 条未在 OpenAlex 索引中找到（hobelsberger2025, lightman2024, venktesh2025 — 均为近期 preprint，属正常），3 条 mismatch 仅为作者姓名格式差异（LaTeX 编码问题），无实质性错误。

现在撰写完整审稿报告并汇报给 Director。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4a0ad4b8-34dc-4bbb-9e24-d831f0e17d3e",
  "isSidechain": false,
  "requestId": "req_011Cb4ZBzznawEnFdiBJ8xhe",
  "type": "assistant",
  "uuid": "37a78e25-efcd-4122-a68d-90bc73fe94fc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "f49c1ccb-97a0-4961-857d-2db0aa0e0624",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014WBX1yKtnWj44GeZCuBbJ1",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 18157,
      "cache_read_input_tokens": 80545,
      "output_tokens": 7108,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 18157,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 7108,
          "cache_read_input_tokens": 80545,
          "cache_creation_input_tokens": 18157,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 18157
          },
          "type": "message"
        }
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

_source line 67 · 2026-05-15T15:04:17.808Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director · `toolu_01TiZwYpWH3BBvL81PSExDD1`</summary>

```json
{
  "text": "## Reviewer 2 — Round 1 审稿报告\n\n**论文**: Strong Predictors, Weak Selectors: Confidence Signals Predict but Do Not Select in 8B-Scale Information Extraction\n**目标 venue**: EMNLP 2026 Findings (ARR May cycle)\n**审查侧重**: 新颖性 + 定位完整性 + 写作质量 + 格式合规\n\n---\n\n## 总体评分\n**Overall**: 2.5/5（介于 Resubmit next cycle 和 Findings acceptance 之间）\n**一句话总结**: 方法论扎实、统计分析严谨的负面结果论文，但核心 framing 存在问题——\"correlation-selection gap\" 中 4/5 信号的 selection 失败是定义必然而非经验发现，真正的经验贡献（LP compression 诊断 + MBR utility-quality misalignment）被过度包装的 gap 叙事稀释；加上正文极可能严重超过 8 页限制，当前版本不宜接收。\n\n## 官方维度打分（来自 ACL ARR review form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5/5 | 统计方法论优秀（3-seed, bootstrap CI, TOST, Fisher combination），但核心 framing 将定义性质的观察与经验发现混为一体，夸大了 empirical contribution 的范围 |\n| Excitement | 2.5/5 | LP compression 诊断和 MBR 在 structured IE 上的失败是有价值的负面结果，但 4/5 信号 definitionally 无法 select 的事实削弱了\"所有信号都失败\"这一叙事的冲击力；整体贡献对 NLP 社区的启发性有限 |\n| Overall | 2.5/5 | 页数严重超限是硬伤（可能触发 desk-reject），需要实质性压缩；即使页数合规，contribution framing 也需要重新聚焦 |\n| Reproducibility | 4/5 | 训练配置完整（Table 8），prompt 模板、超参数、随机种子均已报告；缺少代码/数据发布承诺 |\n| Confidence | 4/5 | 对 self-consistency、MBR decoding、IE 评估均有扎实了解 |\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] 正文页数极可能严重超过 8 页限制\n- 具体位置：main.tex（Abstract → Conclusion 的全部 sections）\n- 问题：正文包含 7 个 section（Abstract, Introduction, Related Work, Method, Experiments, Discussion, Conclusion），其中 Introduction 含 1 个 figure*（全宽），Experiments 含 2 个 figure*、1 个 table*（全宽）、1 个 table，Method 含 6 个 displayed equation，Discussion 含 1 个 ablation subsection。保守估计正文约 10-11 页，超限 2-3 页。\n- 为什么影响接收：ARR CFP 明确规定长文正文 ≤8 页，超页是 desk-rejection 理由（ARR reviewer guidelines 的 desk-rejection checklist 中列有 format/length violations）。\n- 建议修改方向：(1) Discussion §sec:ablation（free-form ablation 详述）可移至 Appendix，正文仅保留 1-2 句结论；(2) Robustness (§5.4) 的大部分数字可移至 Appendix；(3) Experiments 中 seed variability 和 conditional filtering 段落可精简；(4) 压缩 Introduction 的 3 个 contribution bullet——当前每个 contribution 包含过多实验细节（具体数字、p-value），这些应留在 Experiments 中。\n\n**N2** [critical] 核心 framing \"correlation-selection gap\" 混淆了定义性观察与经验发现\n- 具体位置：Abstract line 5-6, Introduction §1 Contributions, Section 5.2 标题, Discussion 全篇\n- 问题：论文框架暗示 \"5 个信号都在 selection 上失败\" 是一个统一的经验发现。但论文自身承认（Introduction line 23: \"Four of five signals are instance-level by construction—this is definitional, not empirical\"；Discussion Layer 1）4/5 信号是 instance-level aggregates，它们无法 select 是数学上的必然，与\"gap\"无关。将这 4 个信号纳入 selection table（Table 2）并展示它们\"失败\"，在方法论上是有效的（通过 consensus-proximity 转化为 per-sample），但在叙事上容易误导读者，因为读者的第一印象是\"所有 5 个信号都经验性地失败了\"。\n- 真正的经验贡献仅限于：(a) LP score compression 诊断（60% tied, 非 tied 子集 +2.9pp p=0.01），(b) MBR utility-quality misalignment 在 structured IE 上的首次证实。这两点足以构成一篇有价值的 Findings 论文，但当前 framing 让它们淹没在过度宏大的\"gap\"叙事中。\n- 为什么影响接收：Reviewer 和 AC 可能认为论文过度包装了一个部分 trivial 的发现（ARR guidelines H1 提到不应因 \"unsurprising\" 拒稿，但这里的问题不是 surprising 与否，而是定义性观察被包装为经验发现）。\n- 建议修改方向：重新聚焦 framing。标题和 abstract 应明确：核心问题是 \"为什么 LP（唯一的 per-sample 信号）和 MBR（将 instance-level 转化为 per-sample 的唯一机制）都无法 bridge quality estimation 到 selection\"。4 个 instance-level 信号的 definitional failure 可以作为 background/motivation，而非核心 finding。Contribution 1 (\"multi-metric evaluation\") 更像是 methodology/benchmark 而非 conceptual contribution。\n\n**N3** [critical] 标题 claim 过强：\"Do Not Select\" + \"8B-Scale\" 的泛化暗示\n- 具体位置：标题 \"Confidence Signals Predict but Do Not Select in 8B-Scale Information Extraction\"\n- 问题：\"Do Not Select\" 是一个绝对性否定，但论文实际发现 LP 在非 tied 子集上 significantly selects (+2.9pp, p=0.01, §Discussion)，RE 在 free-form decoding 下 LP 也翻转为正（+1.69pp, preliminary）。即在论文自身的实验中，selection 并非完全不可能——只是在 primary setting 下未达显著性。此外，仅基于 2 个 8B 模型，标题使用 \"8B-Scale\" 暗示了这一规模下的普遍性。Limitations section 正确指出了 70B+ 和 closed-source API 未测试，但标题未反映这一限定。\n- 为什么影响接收：标题 overclaim 是 ARR review form 中 Results issues (R5: \"Overclaiming or misleading framing\") 的评审要点。\n- 建议修改方向：\"Do Not Select\" → \"Struggle to Select\" 或 \"Fail to Select Under Score Compression\"；考虑移除 \"8B-Scale\" 或改为 \"Two 8B Models\"。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] Abstract 信息密度过高，关键 message 被淹没\n- 具体位置：Abstract (sections/abstract.tex)\n- 问题：10 行 abstract 中包含：5 个信号缩写（VC, SJ, FK, EM, LP）、3 个 NER 数据集 + 1 个 RE 数据集、2 个 8B 模型、4 个评估维度（ρ, AUROC, best-of-N F1, oracle headroom）、\"correlation-selection gap\" 概念、LP compression 机制（60%）、MBR utility-quality misalignment、difficulty-dependent collapse、trained verifiers 作为 future direction。一般 EMNLP 读者在 abstract 中无法消化这么多具体数字和缩写。\n- 建议：精简为\"问题—方法—核心发现—implications\"四段式。具体数字和信号缩写留给 Introduction。\n\n**W2** [warning] Contribution 1 (\"multi-metric evaluation revealing metric dissociation\") 的贡献性质模糊\n- 具体位置：Introduction, Contribution 1 (line 38-40)\n- 问题：该 contribution 声称\"EM leads AUROC (0.749) but ranks third in ρ (0.295), so single-metric evaluation risks selecting the wrong signal\"。这是有效的实验观察，但它更接近于 methodological recommendation（\"应该评估多个指标\"）而非 conceptual contribution。在 EMNLP/ARR 评审标准下，这类 benchmark-level 发现通常不被视为独立的核心贡献——除非伴随新方法或新 benchmark release。\n- 建议：将其降级为 experimental finding，而非与 Contribution 2/3 并列为核心贡献。\n\n**W3** [warning] SJ（Soft Jaccard）方法新颖性有限\n- 具体位置：Method §3.2, Eq. 4-5\n- 问题：SJ 的核心组件——Hungarian algorithm 做 bipartite matching + token-level IoU 作为 similarity——均为标准技术。Hungarian matching 在 NER/RE 评估中已有应用（如 entity alignment 文献），token-level IoU 也是常规 span overlap metric。论文将 SJ 作为 \"our primary structural signal\" 和 \"structural matching beyond surface-level agreement\"（Introduction line 17, (i)），但未明确说明这一组合相对于已有工作的技术新颖性。\n- 建议：明确 SJ 是已有技术的组合应用，而非方法论贡献；或 cite 相关 entity alignment 文献以定位 SJ 的增量。\n\n**W4** [warning] Eikema et al. (2025) structure-conditional MBR 应提前到 Related Work\n- 具体位置：Related Work §2 最后一句引用了 eikema2025structured，但主要讨论在 Discussion §6 (line 30)\n- 问题：Eikema et al. (2025) 的 structure-conditional MBR decoding 发现 \"standard utility functions degrade on structured outputs\" 与本文核心发现高度相关。当前仅在 Discussion 中用 1 句带过，在 Related Work 最后 1 句提及。这一工作应该在 Related Work 中被更充分地讨论，并明确本文与之的差异化定位（他们研究 MT structured outputs，本文研究 IE structured outputs；他们提出 structure-conditional 方案，本文诊断失败原因）。\n- 建议：在 Related Work 的 MBR 段落中增加 2-3 句讨论 Eikema et al. (2025)，明确两者的互补关系。\n\n**W5** [warning] RE 结论的 \"preliminary\" 标注在各 section 中不一致\n- 具体位置：Abstract 未标注 preliminary；Introduction Contribution 2 line 47 标注 \"preliminary\"；Introduction Contribution 3 line 52 标注 \"preliminary\"；Table 1 caption 标注；Discussion 多处标注；Conclusion line 9 标注\n- 问题：Abstract（论文最高可见度的部分）完全未提及 RE 结果是 preliminary（基于单一 RE benchmark）。读者如果只读 abstract，会误以为 RE 结论与 NER 同等稳健。考虑到 RE 只有 SciERC 一个数据集（40% zero F1），且 RE selection 在 free-form 下出现 direction reversal，RE 结论的 preliminary 性质应在 abstract 中有所体现。\n- 建议：Abstract 中增加一句类似 \"RE findings rest on a single benchmark and are preliminary\"。\n\n**W6** [warning] 缺少代码/数据发布承诺\n- 具体位置：全文（Ethics Statement, Limitations, 均未提及）\n- 问题：ARR reproducibility checklist 通常要求作者说明是否会发布代码和数据。论文报告了完整的训练配置和实验参数，但未承诺发布代码、训练好的模型、或实验 artifacts。对于一篇以 empirical benchmark 为核心的论文，缺少复现资源会显著降低实际影响力。\n- 建议：在 Ethics Statement 或 Limitations 后添加 \"Code and Data\" 段，说明发布计划。\n\n**W7** [warning] enable_thinking 训练 confound 的影响评估不充分\n- 具体位置：Experiments §5.1 line 15-18, Limitations line 18-21\n- 问题：Qwen3-8B 的 SciERC checkpoint 使用 enable_thinking=True 训练（注入空 `&lt;think>&lt;/think>` blocks），而 CoNLL 和 WNUT 未使用。论文辩称影响小（<0.3% of 2048-token window, no reasoning content, constrained decoding suppresses），但未提供任何定量证据对比 thinking vs non-thinking 训练的 LP 分布差异。论文的核心发现之一是 LP score compression——如果 thinking tokens 在训练时偏移了 first-token probability distributions（论文自身在 Limitations 中承认这一可能），这恰好可能影响 LP compression 行为。\n- 建议：提供 SciERC vs CoNLL/WNUT 的 LP variance 对比数据，或运行一个 ablation（同一数据集两种 thinking 设置）来排除 confound。\n\n---\n\n## 小问题（不影响接收）\n\n- **M1**: Table 1 caption 中 \"SciERC RE\" 列标注为 \"single benchmark—preliminary\"，但 SciERC NER 也是 single benchmark（尽管有 CoNLL + WNUT-17 作为补充）。建议统一 \"preliminary\" 标注标准或解释为何 NER 不标注。\n- **M2**: Eq. 4 中 $\\sum_{g} \\max(|g_i|, |g_j|)$ 的 normalizer 解释（\"penalize length asymmetry\"）与标准 Jaccard 的 union normalizer 不同，但论文未讨论这一选择对结果的影响。是否做过 sensitivity analysis？\n- **M3**: 引用格式小问题——feng2025optimal 的 bib entry 中 author 字段为 \"Feng, Austin\"，但 OpenAlex 匹配到的 first author 是 \"Austin\"（非姓氏），可能需要检查作者顺序。snell2025scaling 类似。\n- **M4**: Discussion 中 free-form ablation 段落（§sec:ablation）使用 `\\paragraph` 标签但实际是一个完整的 subsection（约 17 行），与 Discussion 其他 paragraph 的粒度不一致。\n- **M5**: Appendix 中 Table 3 (tab:robustness) 的 footnote $\\dagger$ 解释 \"$\\sigma=0.013$\"，但表格正文中未出现 $\\pm 0.013$（表格显示的是单点值 0.411$^\\dagger$），容易混淆。\n- **M6**: nedellec2026consistency 在 bib 中的 author 字段以 \"Yao, Xinzhi\" 开头，但 key 用了 \"nedellec2026\"；虽然不影响编译，但 key 与实际第一作者不一致可能造成混淆。\n\n---\n\n## 主要优势\n\n1. **统计严谨性**: 3-seed analysis, bootstrap CI, TOST equivalence testing, Fisher combined p-values — 远超 IE/NLP 领域的典型论文水准。这种 \"negative result done right\" 的方法论值得认可。\n2. **诚实的 hedging**: RE 结论在 Experiments/Discussion/Conclusion 中一致标注 \"preliminary\"，训练 confound 在 Limitations 中坦诚披露，seed 456 的 --subtask joint 不一致也被报告。这种透明度在投稿论文中罕见。\n3. **LP compression 诊断的机制清晰度**: 60% tied fraction → non-tied subset 显著 select (+2.9pp) → 确认 compression 是 bottleneck 而非 LP 本身无信息——这一逻辑链是论文最强的贡献。\n4. **Difficulty gradient 发现**: EM→SJ crossover 在 easy→hard 任务上的切换，以及 WNUT-17 capability boundary 的识别，对 practitioners 有直接指导意义。\n5. **引用完整**: 62 篇引用无 orphan 无 missing，覆盖 self-consistency、MBR、uncertainty estimation、IE 等全部相关方向；concurrent work（CISC, Self-Certainty, RASC, LatentSC, Ranked Voting 等）均已讨论。\n\n---\n\n## Reviewer 2 建议的 action items（优先级排序）\n\n1. **[必须]** 压缩正文至 ≤8 页（当前估计 10-11 页）\n2. **[必须]** 重新聚焦 contribution framing：核心问题是 LP compression + MBR misalignment，而非 \"5 个信号都在 selection 上失败\"\n3. **[必须]** 修改标题，softening \"Do Not Select\" claim\n4. **[建议]** 精简 abstract，移除大部分具体数字和缩写\n5. **[建议]** Abstract 中标注 RE preliminary\n6. **[建议]** 扩展 Eikema et al. (2025) 在 Related Work 中的讨论\n7. **[建议]** 添加代码/数据发布承诺",
  "reviewer_id": "2",
  "project": "struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "37a78e25-efcd-4122-a68d-90bc73fe94fc",
  "isSidechain": false,
  "requestId": "req_011Cb4ZBzznawEnFdiBJ8xhe",
  "type": "assistant",
  "uuid": "3c686dc6-25e1-4e50-89cc-6f389b286ffc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "f49c1ccb-97a0-4961-857d-2db0aa0e0624",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014WBX1yKtnWj44GeZCuBbJ1",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 18157,
      "cache_read_input_tokens": 80545,
      "output_tokens": 7108,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 18157,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 7108,
          "cache_read_input_tokens": 80545,
          "cache_creation_input_tokens": 18157,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 18157
          },
          "type": "message"
        }
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

_source line 68 · 2026-05-15T15:04:21.941Z_

<details><summary>↩ Tool result · `toolu_01TiZwYpWH3BBvL81PSExDD1`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_3897c2857f11615119e277e820eae311:director\"}, \"error\": \"\"}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3c686dc6-25e1-4e50-89cc-6f389b286ffc",
  "isSidechain": false,
  "promptId": "a8cee1eb-a5df-415d-8e30-c85446d1e0a7",
  "type": "user",
  "uuid": "2275f338-78f1-44e5-97b1-4f79b674fcab",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"review_director_key\\\": \\\"feishu:group:oc_3897c2857f11615119e277e820eae311:director\\\"}, \\\"error\\\": \\\"\\\"}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_3897c2857f11615119e277e820eae311:director\"}, \"error\": \"\"}"
    }
  },
  "sourceToolAssistantUUID": "3c686dc6-25e1-4e50-89cc-6f389b286ffc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "f49c1ccb-97a0-4961-857d-2db0aa0e0624",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 69_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[Round 1 审稿请求]: ## Round 1 审稿任务 — Reviewer 2  **你的侧重**：新颖性 + 定位完整性 + 写作质量 + 格式合规  ### 投稿信息 - **目标 venue**: EMNLP 2026 Findings (ARR May cycle) - **Deadline**: 2026-05-25 - **格式**: ACL template, 长文 8 页…",
  "leafUuid": "2275f338-78f1-44e5-97b1-4f79b674fcab",
  "sessionId": "f49c1ccb-97a0-4961-857d-2db0aa0e0624"
}
```

---

### Runtime record

_source line 70_

```json
{
  "type": "ai-title",
  "aiTitle": "Round 1 review for EMNLP 2026 structured IE paper",
  "sessionId": "f49c1ccb-97a0-4961-857d-2db0aa0e0624"
}
```

---

### Runtime record

_source line 71_

```json
{
  "type": "ai-title",
  "aiTitle": "Round 1 review for EMNLP 2026 structured IE paper",
  "sessionId": "f49c1ccb-97a0-4961-857d-2db0aa0e0624"
}
```

---

### Runtime record

_source line 72 · 2026-05-15T15:05:31.533Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-15T15:05:31.533Z",
  "sessionId": "f49c1ccb-97a0-4961-857d-2db0aa0e0624",
  "content": "[Round 1 审稿请求]:\n## Step 2 — 交叉分享：请回应 Reviewer 1 的审稿意见\n\n以下是 Reviewer 1 的完整审稿原文。请逐条回应：**[AGREE]** 同意并说明理由，或 **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n### Reviewer 1 总体评分\nOverall: 3.5/5, Soundness: 3.5/5, Excitement: 3/5, Reproducibility: 3/5\n\n### Must-Fix 问题\n\n**N1** [critical] ε=0.05 \"effectively tied\" 阈值论证循环性\n- Table 12 显示 ε=0.01→1.1%, ε=0.05→60.3%（59× 跳变），阈值处于 CDF 陡峭区域\n- ε=0.05 选在中位数附近（median LP range=0.041），保证≥50% tied 是 by construction\n- 建议报告完整 ε 梯度 + 提供外部基准（QA/MT 上同模型 LP range 作参照）\n\n**N2** [critical] LP 温度数据缺失\n- 核心诊断对象 LP 在 T=0.7 无数据（Appendix B 明确标注），但论文在 Section 4.4 声称 \"robust performance across T∈{0.7, 1.0}\" 易误读为包含 LP\n- T<1.0 是常用部署温度，LP compression 行为完全未知\n\n**N3** [critical] RE 结论基础薄弱\n- 仅 SciERC 单数据集；Table 3 RE 仅 seed=42 单种子\n- \"preliminary\" 标注不一致：Abstract 未标 preliminary\n- 建议补数据集或统一降级 RE 为 pilot study\n\n### Should-Fix 问题\n\n**W1** Free-form ablation 仅 1 dataset × 1 model × 1 seed，RE LP 翻转需 3-seed 验证\n**W2** FK 独立性检验 n=5 t-test 功效极低，应改用 instance-level 检验（n=529+）\n**W3** Seed 456 使用 --subtask joint 而非 --subtask ner，可能影响 LP 行为\n**W4** TOST δ 锚定于内部 oracle headroom，缺乏外部实际意义基准\n**W5** SJ max normalizer 非标准设计未 ablate\n**W6** N=8 QE 主表单种子 vs N=16 多种子，设计不对称\n\n### Reviewer 1 主要优势评价\n1. Correlation-selection gap 概念和两层机制解释逻辑自洽\n2. 统计分析远超同类工作\n3. 限制披露透明\n4. NER 跨模型一致性强（Kendall's W=1.000）\n5. 难度梯度设计揭示非显然现象\n\n### 引用核查\n62 条引用全部通过，无虚假引用。\n\n---\n\n请对以上每个 N/W 级别问题给出你的 [AGREE] 或 [REBUT] 判断，并说明理由。特别是：你是否同意 R1 关于 ε=0.05 循环论证的判断？LP 温度缺失的 severity 你如何评估？"
}
```

---

### Runtime record

_source line 73 · 2026-05-15T15:05:31.533Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-15T15:05:31.533Z",
  "sessionId": "f49c1ccb-97a0-4961-857d-2db0aa0e0624"
}
```

---

## Round 2

2 recorded events

### User

_source line 74 · 2026-05-15T15:05:31.523Z_

Continue from where you left off.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2275f338-78f1-44e5-97b1-4f79b674fcab",
  "isSidechain": false,
  "promptId": "1234cdc9-15b4-4f33-864e-75218cb32c14",
  "type": "user",
  "isMeta": true,
  "uuid": "ee6d7295-d7be-4953-be4f-53e919e82dd5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "f49c1ccb-97a0-4961-857d-2db0aa0e0624",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 75 · 2026-05-15T15:05:31.523Z_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ee6d7295-d7be-4953-be4f-53e919e82dd5",
  "isSidechain": false,
  "type": "assistant",
  "uuid": "54b7891d-4e3a-4b7d-aed9-b98c927dcfeb",
  "isApiErrorMessage": false,
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "f49c1ccb-97a0-4961-857d-2db0aa0e0624",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "id": "2465b02b-721d-447a-b80f-5e79b5d4fdfc",
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

8 recorded events

### User

_source line 76 · 2026-05-15T15:05:31.605Z_

[Round 1 审稿请求]:
## Step 2 — 交叉分享：请回应 Reviewer 1 的审稿意见

以下是 Reviewer 1 的完整审稿原文。请逐条回应：**[AGREE]** 同意并说明理由，或 **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）。

---

### Reviewer 1 总体评分
Overall: 3.5/5, Soundness: 3.5/5, Excitement: 3/5, Reproducibility: 3/5

### Must-Fix 问题

**N1** [critical] ε=0.05 "effectively tied" 阈值论证循环性
- Table 12 显示 ε=0.01→1.1%, ε=0.05→60.3%（59× 跳变），阈值处于 CDF 陡峭区域
- ε=0.05 选在中位数附近（median LP range=0.041），保证≥50% tied 是 by construction
- 建议报告完整 ε 梯度 + 提供外部基准（QA/MT 上同模型 LP range 作参照）

**N2** [critical] LP 温度数据缺失
- 核心诊断对象 LP 在 T=0.7 无数据（Appendix B 明确标注），但论文在 Section 4.4 声称 "robust performance across T∈{0.7, 1.0}" 易误读为包含 LP
- T<1.0 是常用部署温度，LP compression 行为完全未知

**N3** [critical] RE 结论基础薄弱
- 仅 SciERC 单数据集；Table 3 RE 仅 seed=42 单种子
- "preliminary" 标注不一致：Abstract 未标 preliminary
- 建议补数据集或统一降级 RE 为 pilot study

### Should-Fix 问题

**W1** Free-form ablation 仅 1 dataset × 1 model × 1 seed，RE LP 翻转需 3-seed 验证
**W2** FK 独立性检验 n=5 t-test 功效极低，应改用 instance-level 检验（n=529+）
**W3** Seed 456 使用 --subtask joint 而非 --subtask ner，可能影响 LP 行为
**W4** TOST δ 锚定于内部 oracle headroom，缺乏外部实际意义基准
**W5** SJ max normalizer 非标准设计未 ablate
**W6** N=8 QE 主表单种子 vs N=16 多种子，设计不对称

### Reviewer 1 主要优势评价
1. Correlation-selection gap 概念和两层机制解释逻辑自洽
2. 统计分析远超同类工作
3. 限制披露透明
4. NER 跨模型一致性强（Kendall's W=1.000）
5. 难度梯度设计揭示非显然现象

### 引用核查
62 条引用全部通过，无虚假引用。

---

请对以上每个 N/W 级别问题给出你的 [AGREE] 或 [REBUT] 判断，并说明理由。特别是：你是否同意 R1 关于 ε=0.05 循环论证的判断？LP 温度缺失的 severity 你如何评估？

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "54b7891d-4e3a-4b7d-aed9-b98c927dcfeb",
  "isSidechain": false,
  "promptId": "1234cdc9-15b4-4f33-864e-75218cb32c14",
  "type": "user",
  "uuid": "a662f9a9-b0de-4ed1-8fae-2ad2f38620eb",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "f49c1ccb-97a0-4961-857d-2db0aa0e0624",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 77 · 2026-05-15T15:06:17.851Z_

<details><summary>Logged reasoning block</summary>

```text
The Director is asking me to cross-review Reviewer 1's findings. I need to go through each issue and provide [AGREE] or [REBUT] with evidence from the paper. Let me carefully analyze each point.

Let me re-read the relevant sections to make sure I'm accurate in my responses.

Key points to address:

**N1**: ε=0.05 threshold circularity
- R1 claims the threshold is chosen at the median, guaranteeing ≥50% tied by construction
- Let me check: Appendix §app:logprob_ties says "The median within-instance LP range is only 0.041 nats—below the ε=0.05 threshold used throughout, providing data-driven justification for this cutoff rather than an arbitrary choice."


- R1 has a point that selecting ε near the median does create a high tied fraction, but the paper actually shows the full distribution across multiple thresholds in Figure 8 and Table 12, which reveals the LP values are tightly clustered—the jump from 1.1% to 60.3% tied reflects this concentration rather than arbitrary threshold placement. The choice isn't truly circular, though R1's concern about the threshold's proximity to the median deserves acknowledgment.
- The paper's core argument isn't really about defending the specific 60% figure, but rather that LP ranges are fundamentally small (median 0.041 nats), making fine-grained discrimination inherently unreliable. The non-tied subset analysis showing a +2.9pp difference is the actual diagnostic that matters, independent of where exactly the threshold lands.

For N2, the missing LP temperature data is a genuine limitation—LP is the most interesting signal with the most nuanced findings, yet we don't know how sensitive it is to temperature variation. That's worth acknowledging as a real gap.

On N3, the RE conclusions do rest on a single dataset with a single seed, which is exactly the kind of preliminary evidence that needs replication before claiming robustness.

W1 is also fair—the RE reversal is one of the most striking findings but it's unreplicated across seeds and other benchmarks, so calling it preliminary is appropriate.

For W2, the paper does acknowledge the low statistical power with n=5 in the FK independence test, though that caveat could be more prominent.

W3 is a partial agreement—the seed 456 disclosure is transparent and the NER impact is negligible, but the paper doesn't specifically analyze whether joint decoding affects LP token probabilities differently.

On W4, the paper anchors TOST δ values to oracle headroom percentages in the appendix, but R1 wants external validation for these thresholds.  I agree the analysis would be stronger with independent calibration rather than relying on internal metrics.

W5 flags the max normalizer choice in the SJ method—there's no ablation comparing it against the union normalizer, which I already noted as a concern.

W6 points to an asymmetry: the main results use N=8 with a single seed, while the robustness checks scale to N=16 across multiple seeds.

Looking at the actual data, though, the paper does include 3-seed analysis for N=8 in the appendix, and the NER selection table reports multi-seed means with error bars. So the asymmetry is really just in how the main QE table is presented—the multi-seed results exist but aren't prominently featured. I'd agree this is a presentation issue rather than a data collection problem, though the main table should probably reference the appendix results more explicitly.

On the Director's meta-questions: I partially agree with R1 about the circularity concern—the framing has some circular elements, but the non-tied subset analysis does provide some independent validation. As for the LP temperature gap, that's actually quite serious. LP compression is the paper's most interesting finding and the core diagnostic, so not knowing how it behaves at deployment temperatures is a meaningful limitation.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a662f9a9-b0de-4ed1-8fae-2ad2f38620eb",
  "isSidechain": false,
  "requestId": "req_011Cb4ZVsZoeZPfPbKFuSAQT",
  "type": "assistant",
  "uuid": "503d0851-5aad-4e8d-99ab-396b337453b1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "f49c1ccb-97a0-4961-857d-2db0aa0e0624",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GsLx2uJejbx4Sn7kQTjiTc",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 996,
      "cache_read_input_tokens": 105881,
      "output_tokens": 5865,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 996,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 5865,
          "cache_read_input_tokens": 105881,
          "cache_creation_input_tokens": 996,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 996
          },
          "type": "message"
        }
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

_source line 78 · 2026-05-15T15:07:30.909Z_

## Reviewer 2 交叉回应：逐条回应 Reviewer 1

---

### Must-Fix 问题

**[AGREE with nuance] R1-N1: ε=0.05 阈值循环性**

R1 的核心观察是准确的：median LP range = 0.041 (Appendix G, Table 12)，选择 ε=0.05 必然保证 ≥50% tied，因为 ε 在中位数之上。Table 12 中 ε=0.01→1.1% 到 ε=0.05→60.3% 的 59× 跳变确实说明 CDF 在此区间极其陡峭，ε 选择的微小变化导致叙事效果差异巨大。论文声称 "providing data-driven justification for this cutoff"（Appendix G），但"在中位数附近选阈值"本身就不构成独立的 justification。

但我要补充一点限定：**这一 circularity 不影响论文最强的诊断证据。** 非 tied 子集的分析（LP range ≥0.05, n=210, +2.9pp, p=0.01；within-instance ρ 从 0.08→0.39；Appendix G）是一个 **conditional diagnostic**，其结论（"compression 是 bottleneck"）不依赖于 tied fraction 的具体百分比，而是依赖于 tied vs non-tied 的性能对比。即使把 ε 改为 0.03 或 0.08，只要切分出的两组在 selection 表现上有显著差异，结论依然成立。

R1 建议报告完整 ε 梯度 + 外部基准（QA/MT LP range），我完全支持。这能把 "60% tied" 从一个可能 cherry-picked 的叙事锚点变成一个经过校准的定量 claim。

**[AGREE] R1-N2: LP 温度数据缺失**

严重程度评估：**高。** 理由如下：

1. LP 是论文唯一的 per-sample 信号，也是两层机制解释中 Layer 2 的唯一主体。论文的核心诊断——LP score compression——完全基于 T=1.0 的数据。
2. Figure 5 caption 明确标注 "LP T=0.7 data unavailable"，但 §5.4 的主题句 "Consistency-based signals show robust performance across T∈{0.7, 1.0}" 语法上未排除 LP，读者很容易误读为包含 LP。
3. Limitations section (lines 25-30) 对此有长篇讨论，承认 "practitioners commonly deploy at T<1.0" 并分析了两种可能的方向（lower T 可能 reduce 或 exacerbate compression），但这只是理论推测，无数据支撑。
4. 从机制角度看，lower T 集中 probability mass 到 fewer tokens，很可能进一步压缩 LP range（因为所有 N samples 更加相似），这意味着论文的核心发现可能在部署温度下更严重——但也可能因为 token-level score gap 变大而缓解。方向不可预测，恰好说明数据不可省略。

我认为这是仅次于页数超限的第二大方法论问题。论文如果要保留 LP compression 作为核心贡献，T=0.7（或 T=0.5）的 LP 数据是必要的。

**[AGREE] R1-N3: RE 结论基础薄弱**

完全同意。我在自己的审稿中也独立提出了同一问题（我的 W5）：Abstract 未标注 RE preliminary，而 Introduction Contribution 2/3 和 Table 1 caption 标注了。

补充 R1 未提到的一个额外证据：RE selection 结果在 Table 2 中仅报告 "seed=42"（无 ±σ，无 Fisher p），而 NER 报告了 3-seed mean±σ + Fisher combined p。这一不对称不仅是 "preliminary" 的问题，而且导致 RE selection 的统计推断完全缺失——读者无法判断 RE 中 LP (0.395) vs greedy (0.404) 的 Δ=-0.9pp 是否 within noise。

R1 建议"补数据集或统一降级为 pilot study"——我倾向后者更实际。补 RE 数据集（如 TACRED/DocRED）需要完整的训练+推理 pipeline，短期难以完成。将 RE 统一降级为 "pilot study / exploratory analysis" 并在 Abstract 中明确标注，是更现实的方案。

---

### Should-Fix 问题

**[AGREE] R1-W1: Free-form ablation 单设置**

论文自身在 Discussion (line 46) 承认 "whether the RE reversal replicates across seeds and generalizes to other RE benchmarks warrants further investigation"。RE LP selection 从 -0.68pp (constrained) 翻转到 +1.69pp (free-form) 是论文中最 intriguing 的发现之一，但基于单 seed 单 dataset 单 model，confidence 极低。如果这一发现可复现，它实际上会削弱标题中 "Do Not Select" 的 claim（我在 N3 中也提到了这一点）。3-seed 验证是必要的。

**[AGREE with caveat] R1-W2: FK n=5 t-test 功效**

R1 的统计批评正确：n=5 的 one-sample t-test power 极低。论文自身也承认 "should be interpreted cautiously"（Method §3.2 line 41）。R1 建议 instance-level 检验（n=529+）是可行的——计算每个 instance 的 excess agreement ($\bar{P}_i - \bar{P}_{e,i}$) 然后对 n=529 个 instance 做 t-test 或 sign test。

但我要指出一个 caveat：FK 的独立性假设对论文核心结论的影响很小。FK 在所有 NER configurations 上都排在第 4/5 位（Table 1, Table 7），不是论文推荐的信号。即使 FK 被证明 inflated by dependence，这只会加强 SJ/VC 的相对优势，不会改变任何核心结论。所以这是一个方法论 hygiene 问题，不是影响结论的问题。

**[AGREE partially] R1-W3: Seed 456 --subtask joint**

Limitations 中的 disclosure 是坦诚的（NER F1 差异 <0.3pp），但 R1 的 concern 有一个未被论文回应的层面：--subtask joint 意味着模型在 decoding 时同时生成 NER + RE 输出，而 --subtask ner 只生成 NER。这可能影响 LP score 的 absolute level（更长的 joint output → 不同的 mean token log-probability），从而影响 LP compression 的 within-instance range。论文仅报告了 NER F1 差异，未分析 LP distribution 差异。

但实际影响可能有限：seed 456 是 3 个 seed 之一，且 3-seed 分析（Table 2, Table 7）显示 σ 在正常范围内。如果 seed 456 的 LP 行为异常，它会表现为更大的 σ——但 LP 的 3-seed σ=0.013（Table 7）并不突出。

**[AGREE] R1-W4: TOST δ 锚定缺乏外部基准**

R1 的批评是方法论上正确的。TOST 的 equivalence margin δ 应基于 practical significance（"多大的 selection gain 才值得部署？"），而非 anchored to internal oracle headroom。论文用 oracle headroom 的百分比（28-38%, 17-23%, <15%）来 contextualize δ，但 Appendix D 自身承认 "these proportions use the same test data that defines the headroom and should be interpreted as context for practical relevance rather than independent calibration"。

一个外部基准可以是：在 best-of-N selection 文献中（如 Brown et al. 2024 的 Large Language Monkeys），typical selection gain 相对于 oracle headroom 的比例是多少？如果 QA/reasoning 任务上 typical signals 捕获 30-50% headroom，那 IE 上 <10% 就确实是 failure。

**[AGREE] R1-W5: SJ max normalizer 未 ablate**

我在自己的审稿中也独立提出了这一问题（我的 M2）。Eq. 4 使用 $\max(|g_i|, |g_j|)$ 而非标准 Jaccard 的 $|g_i \cup g_j|$，论文仅提供了 1 句 justification（"to penalize length asymmetry"）。鉴于 SJ 是论文的 primary structural signal 并被定位为对 Nédellec et al. (2026) 的增量贡献之一，normalizer 选择的影响应被量化。

**[AGREE partially] R1-W6: N=8 单种子 vs N=16 多种子设计不对称**

R1 的观察在 presentation 层面是正确的：Table 1（主 QE 表）报告 N=8, seed=42 单种子。但 Appendix E Table 7 已提供 N=8 的 3-seed means±σ，且 signal ranking 在 3 seed 间完全一致（Kendall's W=1.000 for NER）。所以问题不在数据缺失，而在主表呈现方式：读者如果不查 Appendix 就会误以为 QE 结论仅基于单种子。

建议：Table 1 改为 3-seed mean（±σ 放 footnote 或 Appendix），与 Table 2（NER 已是 3-seed）保持一致。

---

### R1 优势评价回应

R1 的 5 条优势评价我全部同意。特别是第 2 条（"统计分析远超同类工作"）和第 3 条（"限制披露透明"）——我在自己的审稿中也独立识别为主要优势。这说明论文的方法论品质是两位 reviewer 的共识。

---

### 总结：与 R1 的分歧和共识

| 维度 | 共识/分歧 | 说明 |
|------|----------|------|
| ε=0.05 circularity | 部分共识 | R1 的表面论证正确，但非 tied 子集的 conditional diagnostic 不受影响 |
| LP 温度缺失 severity | 完全共识 | 我评估为 high severity，与 R1 一致 |
| RE preliminary | 完全共识 | R1 和我独立提出了相同问题 |
| Free-form ablation | 完全共识 | 3-seed 验证必要 |
| FK t-test | 共识但降级 | 方法论正确但不影响核心结论 |
| Overall 评分 | 分歧 | R1 给 3.5/5, 我给 2.5/5——差异主要源于我对页数超限的严重性评估和 contribution framing 问题 |

我与 R1 的主要分歧在 overall 评分（3.5 vs 2.5）。R1 未提及页数超限问题（我的 N1），也未挑战 contribution framing（我的 N2, N3）。如果页数合规且 framing 重新聚焦，我的评分会上调至 3/5（Findings borderline）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "503d0851-5aad-4e8d-99ab-396b337453b1",
  "isSidechain": false,
  "requestId": "req_011Cb4ZVsZoeZPfPbKFuSAQT",
  "type": "assistant",
  "uuid": "38769c1e-3617-4065-bef4-7736dce086ea",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "f49c1ccb-97a0-4961-857d-2db0aa0e0624",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GsLx2uJejbx4Sn7kQTjiTc",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 996,
      "cache_read_input_tokens": 105881,
      "output_tokens": 5865,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 996,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 5865,
          "cache_read_input_tokens": 105881,
          "cache_creation_input_tokens": 996,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 996
          },
          "type": "message"
        }
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

_source line 79 · 2026-05-15T15:07:43.884Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director · `toolu_01SMiFaChctip3cqfvL7n3mm`</summary>

```json
{
  "text": "## Reviewer 2 交叉回应 — 回应 Reviewer 1 审稿意见\n\n### 概要\n\nR1 的 6 个 Must/Should-Fix 问题中，我 **AGREE** 5 个（N2, N3, W1, W4, W5），**AGREE with nuance** 3 个（N1, W2, W3, W6）。无 REBUT。\n\n### 关键判断\n\n**ε=0.05 circularity（R1-N1）**: 表面论证正确（中位数附近选阈值保证 ≥50% tied），但非 tied 子集的 conditional diagnostic (+2.9pp, p=0.01) 不依赖于具体 tied fraction 百分比。建议补充完整 ε 梯度和外部基准，但不影响 LP compression 核心诊断的有效性。\n\n**LP 温度缺失（R1-N2）**: 评估为 **high severity**，与 R1 一致。LP 是唯一 per-sample 信号，score compression 在部署温度下的行为完全未知。这是仅次于页数超限的第二大方法论问题。\n\n**RE preliminary（R1-N3）**: 完全同意。补充指出 Table 2 RE 列缺少 3-seed 统计（NER 有 mean±σ + Fisher p，RE 仅 seed=42 单点值），进一步削弱 RE 结论基础。\n\n### 与 R1 的主要分歧\n\nOverall 评分差异（R1: 3.5 vs R2: 2.5），原因：\n1. 我识别了 **页数严重超限**（估计 10-11 页，超限 2-3 页）——R1 未提及此问题\n2. 我认为 **contribution framing** 存在根本问题（4/5 信号的 selection 失败是定义必然，被包装为经验发现）——R1 虽在 N1 中触及了方法论层面，但未挑战 framing 本身\n3. 我认为标题 \"Do Not Select\" **overclaim**（论文自身发现 LP 在非 tied 子集上 significantly selects）\n\n如果页数合规 + framing 重新聚焦 + 标题 softened，我的评分可上调至 3/5。",
  "reviewer_id": "2",
  "project": "struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "38769c1e-3617-4065-bef4-7736dce086ea",
  "isSidechain": false,
  "requestId": "req_011Cb4ZVsZoeZPfPbKFuSAQT",
  "type": "assistant",
  "uuid": "1f5f6e82-cd70-4640-9a06-e9fbeb0aa817",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "f49c1ccb-97a0-4961-857d-2db0aa0e0624",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GsLx2uJejbx4Sn7kQTjiTc",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 996,
      "cache_read_input_tokens": 105881,
      "output_tokens": 5865,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 996,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 5865,
          "cache_read_input_tokens": 105881,
          "cache_creation_input_tokens": 996,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 996
          },
          "type": "message"
        }
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

_source line 80_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[Round 1 审稿请求]: ## Step 2 — 交叉分享：请回应 Reviewer 1 的审稿意见  以下是 Reviewer 1 的完整审稿原文。请逐条回应：**[AGREE]** 同意并说明理由，或 **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）。  ---  ### Reviewer 1 总体评分 Overall: 3.5/5, S…",
  "leafUuid": "1f5f6e82-cd70-4640-9a06-e9fbeb0aa817",
  "sessionId": "f49c1ccb-97a0-4961-857d-2db0aa0e0624"
}
```

---

### Runtime record

_source line 81_

```json
{
  "type": "ai-title",
  "aiTitle": "Round 1 review for EMNLP 2026 structured IE paper",
  "sessionId": "f49c1ccb-97a0-4961-857d-2db0aa0e0624"
}
```

---

### Tool result

_source line 82 · 2026-05-15T15:07:47.724Z_

<details><summary>↩ Tool result · `toolu_01SMiFaChctip3cqfvL7n3mm`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_3897c2857f11615119e277e820eae311:director\"}, \"error\": \"\"}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1f5f6e82-cd70-4640-9a06-e9fbeb0aa817",
  "isSidechain": false,
  "promptId": "1234cdc9-15b4-4f33-864e-75218cb32c14",
  "type": "user",
  "uuid": "2bc3507c-a2bb-4daa-b684-f0f2b572ac66",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"review_director_key\\\": \\\"feishu:group:oc_3897c2857f11615119e277e820eae311:director\\\"}, \\\"error\\\": \\\"\\\"}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_3897c2857f11615119e277e820eae311:director\"}, \"error\": \"\"}"
    }
  },
  "sourceToolAssistantUUID": "1f5f6e82-cd70-4640-9a06-e9fbeb0aa817",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "f49c1ccb-97a0-4961-857d-2db0aa0e0624",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 83 · 2026-05-15T15:07:47.730Z_

```json
{
  "parentUuid": "2bc3507c-a2bb-4daa-b684-f0f2b572ac66",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "b6f88f6a-a1b6-434b-8355-2ce88b71fd48",
  "timestamp": "2026-05-15T15:07:47.730Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "f49c1ccb-97a0-4961-857d-2db0aa0e0624",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---
