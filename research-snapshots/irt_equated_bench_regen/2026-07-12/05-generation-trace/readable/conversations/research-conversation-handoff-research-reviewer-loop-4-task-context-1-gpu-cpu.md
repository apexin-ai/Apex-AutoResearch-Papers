# Research conversation: [HANDOFF] 你是 Research Reviewer，这是 Loop #4。 ## 上一轮交接 (task_context) ### 1. 🔴 硬约束 / 红线 - 本项目无 GPU、无远程服务器——纯论文写作+本地 CPU 分析项

**Temporal Score Incomparability in LLM Benchmarks: A Large-Scale Psychometric Audit of 5,227 Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 21
- **Recorded user turns:** 3
- **Tool calls:** 2
- **Original source:** `logs/chats/exported-trajectories/account-2/ef30c0ef-29fb-4cb0-a309-7059c0bcd7c6.jsonl`
- **Structured JSON:** [`01db8eb6397af5a3c2b3.json`](../../sessions/01/01db8eb6397af5a3c2b3.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-25T06:11:02.441Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-25T06:11:02.441Z",
  "sessionId": "ef30c0ef-29fb-4cb0-a309-7059c0bcd7c6",
  "content": "[HANDOFF] 你是 Research Reviewer，这是 Loop #4。\n\n## 上一轮交接 (task_context)\n\n### 1. 🔴 硬约束 / 红线\n- 本项目无 GPU、无远程服务器——纯论文写作+本地 CPU 分析项目\n- 匿名仓库 `/tmp/anon_repo/` 的 git identity 必须是 `Anonymous &lt;anonymous@example.com>`，绝不能泄露真实身份\n- DDL 2026-05-25 AoE（EMNLP 2026 via ARR）——如果你醒来时已过 DDL，不要再建议修改论文\n- 正文严格 ≤8 页，当前 Conclusion 刚好卡在第 8 页底部，任何正文增加都会溢出——`\\enlargethispage{10\\baselineskip}` 已在 discussion.tex L1，不能再加\n- abstract ≤200 words（当前 161 words）\n\n### 2. 🖥️ 基础设施快照\n- 工作目录：`/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/`\n- 论文：`paper/main.pdf`（19 页，pdfTeX 编译），`paper/sections/*.tex`\n- 匿名仓库：`/tmp/anon_repo/`（11 commits，需用户手动设 Public）\n- 无服务器、无 GPU、无 wandb、无活跃进程\n- Registry：21 实验（14 success / 6 negative / 0 failed / 1 pending bifactor）\n\n### 3. 📊 当前状态\n**项目处于 Paper Final 阶段，等待用户提交。** 我（Loop #3 Reviewer）在本轮完成了：\n- 最终数据审计 worker 审查（PASS，2 个 info 级发现：AUC 0.93-0.94 应为 0.92-0.93、Table 5 rounding non-issue）\n- \\Cref 指针修复验证（4 个新 \\Cref 全部正确，但引发页面溢出→已修复）\n- 页面溢出修复后验证（PASS，Conclusion 在第 8 页内）\n- Desk-reject 风险终检（PDF metadata 匿名 ✅、Type 3=0 ✅、代码匿名 ✅、19 页 ✅）\n- Limitations + Claim 强度审查（6 阴性实验全部已反映，无过度 claim，\">21×\" 偏保守）\n- 模拟 ARR 审稿（C1 near-independence 证据链最薄弱，建议已被采纳：§4.3 \"Crucially\" 强化句 + §5.1 ρ→r 符号修复）\n- Figure 3（ρ degradation curves）提升正文后的完整性终检（PASS）\n\n**无 RUNNING 实验。无等待中的 Worker/Cron。** 唯一待办是用户操作：匿名仓库设 Public + ARR 提交。\n\n### 4. 📋 待办\n- DDL 过后且审稿返回 → 加载 `skills/global/rebuttal.skill.md`，准备 author response\n- 如果用户要求最后一轮修改 → **先检查页面是否仍在 8 页内**（当前零余量）\n- Camera-ready 阶段（如被录用）→ 修复 AUC 0.93-0.94→0.92-0.93（experiments.tex:10）、Table 2 caption 负面措辞、Intro \"massively redundant\"、plan_004 GSM1K 负相关主文引用\n\n### 5. 🎯 战略上下文\n- 论文核心论点：temporal DIF 广泛存在（17.9-31.3%）、与 web-overlap 近独立（Jaccard=0.206）、下游排名影响可控但非零（ρ=0.997, ±800 位移）\n- 审稿人最大攻击面：C1 near-independence 可能是 Li et al. proxy noise 的结果——防线是 base/instruct 反转（χ²=562.7），已在 §4.3 用 \"Crucially\" 句强化\n- 易错点 1：页面零余量——任何正文改动都可能把 Conclusion 推到第 9 页，改前必须编译+视觉验证\n- 易错点 2：§4.2（experiments.tex:16）是全文最密集段落（7 个统计论点挤在一段），审稿人可能跳读漏掉关键信息，但拆段有页面风险\n- 易错点 3：plan_017 的\"DIF items 更有区分力\"与\"audit protocol 建议审查/移除\"存在表面张力——正确理解是：高区分力+跨 cohort 功能差异=系统性偏移，强化而非削弱审计必要性\n- DEFF 范围 13.5-29.2% 很宽，weighted-mean 13.5% 被 cluster bootstrap CI [26.7%, 53.2%] 排除——论文立场是 simple-mean 29.2% 为 primary estimate\n\n## 可查的历史\n前 2 轮 handoff 在 `task_context/history/reviewer/loop_*.md`，如有疑问可 Read 回查。\n完整聊天归档可用 `recall_session_history(\"关键词\")` 搜索。\n\n## 第一个动作要求\n1. 用 `read_registry` 确认当前 RUNNING/PREPARING 实验状态（防止幻觉记忆过时状态）\n2. 回复一句话确认你看到了上面的硬约束 + 当前活跃实验，再开始任何工具调用"
}
```

---

### Runtime record

_source line 2 · 2026-05-25T06:11:02.445Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-25T06:11:02.445Z",
  "sessionId": "ef30c0ef-29fb-4cb0-a309-7059c0bcd7c6"
}
```

---

## Round 1

16 recorded events

### User

_source line 3 · 2026-05-25T06:11:02.487Z_

[HANDOFF] 你是 Research Reviewer，这是 Loop #4。

## 上一轮交接 (task_context)

### 1. 🔴 硬约束 / 红线
- 本项目无 GPU、无远程服务器——纯论文写作+本地 CPU 分析项目
- 匿名仓库 `/tmp/anon_repo/` 的 git identity 必须是 `Anonymous &lt;anonymous@example.com>`，绝不能泄露真实身份
- DDL 2026-05-25 AoE（EMNLP 2026 via ARR）——如果你醒来时已过 DDL，不要再建议修改论文
- 正文严格 ≤8 页，当前 Conclusion 刚好卡在第 8 页底部，任何正文增加都会溢出——`\enlargethispage{10\baselineskip}` 已在 discussion.tex L1，不能再加
- abstract ≤200 words（当前 161 words）

### 2. 🖥️ 基础设施快照
- 工作目录：`/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/`
- 论文：`paper/main.pdf`（19 页，pdfTeX 编译），`paper/sections/*.tex`
- 匿名仓库：`/tmp/anon_repo/`（11 commits，需用户手动设 Public）
- 无服务器、无 GPU、无 wandb、无活跃进程
- Registry：21 实验（14 success / 6 negative / 0 failed / 1 pending bifactor）

### 3. 📊 当前状态
**项目处于 Paper Final 阶段，等待用户提交。** 我（Loop #3 Reviewer）在本轮完成了：
- 最终数据审计 worker 审查（PASS，2 个 info 级发现：AUC 0.93-0.94 应为 0.92-0.93、Table 5 rounding non-issue）
- \Cref 指针修复验证（4 个新 \Cref 全部正确，但引发页面溢出→已修复）
- 页面溢出修复后验证（PASS，Conclusion 在第 8 页内）
- Desk-reject 风险终检（PDF metadata 匿名 ✅、Type 3=0 ✅、代码匿名 ✅、19 页 ✅）
- Limitations + Claim 强度审查（6 阴性实验全部已反映，无过度 claim，">21×" 偏保守）
- 模拟 ARR 审稿（C1 near-independence 证据链最薄弱，建议已被采纳：§4.3 "Crucially" 强化句 + §5.1 ρ→r 符号修复）
- Figure 3（ρ degradation curves）提升正文后的完整性终检（PASS）

**无 RUNNING 实验。无等待中的 Worker/Cron。** 唯一待办是用户操作：匿名仓库设 Public + ARR 提交。

### 4. 📋 待办
- DDL 过后且审稿返回 → 加载 `skills/global/rebuttal.skill.md`，准备 author response
- 如果用户要求最后一轮修改 → **先检查页面是否仍在 8 页内**（当前零余量）
- Camera-ready 阶段（如被录用）→ 修复 AUC 0.93-0.94→0.92-0.93（experiments.tex:10）、Table 2 caption 负面措辞、Intro "massively redundant"、plan_004 GSM1K 负相关主文引用

### 5. 🎯 战略上下文
- 论文核心论点：temporal DIF 广泛存在（17.9-31.3%）、与 web-overlap 近独立（Jaccard=0.206）、下游排名影响可控但非零（ρ=0.997, ±800 位移）
- 审稿人最大攻击面：C1 near-independence 可能是 Li et al. proxy noise 的结果——防线是 base/instruct 反转（χ²=562.7），已在 §4.3 用 "Crucially" 句强化
- 易错点 1：页面零余量——任何正文改动都可能把 Conclusion 推到第 9 页，改前必须编译+视觉验证
- 易错点 2：§4.2（experiments.tex:16）是全文最密集段落（7 个统计论点挤在一段），审稿人可能跳读漏掉关键信息，但拆段有页面风险
- 易错点 3：plan_017 的"DIF items 更有区分力"与"audit protocol 建议审查/移除"存在表面张力——正确理解是：高区分力+跨 cohort 功能差异=系统性偏移，强化而非削弱审计必要性
- DEFF 范围 13.5-29.2% 很宽，weighted-mean 13.5% 被 cluster bootstrap CI [26.7%, 53.2%] 排除——论文立场是 simple-mean 29.2% 为 primary estimate

## 可查的历史
前 2 轮 handoff 在 `task_context/history/reviewer/loop_*.md`，如有疑问可 Read 回查。
完整聊天归档可用 `recall_session_history("关键词")` 搜索。

## 第一个动作要求
1. 用 `read_registry` 确认当前 RUNNING/PREPARING 实验状态（防止幻觉记忆过时状态）
2. 回复一句话确认你看到了上面的硬约束 + 当前活跃实验，再开始任何工具调用

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "f4e13317-a93b-4dd7-b756-e44063b582f1",
  "type": "user",
  "uuid": "3238794f-a41e-4c77-8723-927987246c96",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/.claude/sessions/reviewer_430cd31d",
  "sessionId": "ef30c0ef-29fb-4cb0-a309-7059c0bcd7c6",
  "version": "2.1.126",
  "gitBranch": "rebuttal-b1-b7"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-25T06:11:02.486Z_

```json
{
  "parentUuid": "3238794f-a41e-4c77-8723-927987246c96",
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
      "mcp__agent-ml-research__check_figures_and_layout",
      "mcp__agent-ml-research__cleanup_pdf_images",
      "mcp__agent-ml-research__compute_coverage_matrix",
      "mcp__agent-ml-research__fetch_wandb_metrics",
      "mcp__agent-ml-research__get_gpu_health",
      "mcp__agent-ml-research__get_project_resource_usage",
      "mcp__agent-ml-research__list_constraints",
      "mcp__agent-ml-research__pdf_to_images",
      "mcp__agent-ml-research__read_experiment_plan_with_status",
      "mcp__agent-ml-research__read_matrix",
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__read_registry",
      "mcp__agent-ml-research__read_roadmap",
      "mcp__agent-ml-research__reviewer_post_to_director",
      "mcp__agent-ml-research__ssh_read_only",
      "mcp__agent-ml-research__tail_training_logs"
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
      "mcp__agent-ml-research__check_figures_and_layout",
      "mcp__agent-ml-research__cleanup_pdf_images",
      "mcp__agent-ml-research__compute_coverage_matrix",
      "mcp__agent-ml-research__fetch_wandb_metrics",
      "mcp__agent-ml-research__get_gpu_health",
      "mcp__agent-ml-research__get_project_resource_usage",
      "mcp__agent-ml-research__list_constraints",
      "mcp__agent-ml-research__pdf_to_images",
      "mcp__agent-ml-research__read_experiment_plan_with_status",
      "mcp__agent-ml-research__read_matrix",
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__read_registry",
      "mcp__agent-ml-research__read_roadmap",
      "mcp__agent-ml-research__reviewer_post_to_director",
      "mcp__agent-ml-research__ssh_read_only",
      "mcp__agent-ml-research__tail_training_logs"
    ],
    "removedNames": []
  },
  "type": "attachment",
  "uuid": "924199a1-ae98-462b-ae95-cbe5ecde9ffe",
  "timestamp": "2026-05-25T06:11:02.486Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/.claude/sessions/reviewer_430cd31d",
  "sessionId": "ef30c0ef-29fb-4cb0-a309-7059c0bcd7c6",
  "version": "2.1.126",
  "gitBranch": "rebuttal-b1-b7"
}
```

---

### Runtime record

_source line 5 · 2026-05-25T06:11:02.486Z_

```json
{
  "parentUuid": "924199a1-ae98-462b-ae95-cbe5ecde9ffe",
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
  "uuid": "71a251b5-3fdd-4fe4-9623-daad47854182",
  "timestamp": "2026-05-25T06:11:02.486Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/.claude/sessions/reviewer_430cd31d",
  "sessionId": "ef30c0ef-29fb-4cb0-a309-7059c0bcd7c6",
  "version": "2.1.126",
  "gitBranch": "rebuttal-b1-b7"
}
```

---

### Runtime record

_source line 6 · 2026-05-25T06:11:02.486Z_

```json
{
  "parentUuid": "71a251b5-3fdd-4fe4-9623-daad47854182",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "87d613ec-d92d-413b-ba64-5b0db2743256",
  "timestamp": "2026-05-25T06:11:02.486Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/.claude/sessions/reviewer_430cd31d",
  "sessionId": "ef30c0ef-29fb-4cb0-a309-7059c0bcd7c6",
  "version": "2.1.126",
  "gitBranch": "rebuttal-b1-b7"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Research Reviewer Loop #4 - Paper Final Validation",
  "sessionId": "ef30c0ef-29fb-4cb0-a309-7059c0bcd7c6"
}
```

---

### Assistant

_source line 8 · 2026-05-25T06:11:10.117Z_

<details><summary>Logged reasoning block</summary>

```text
我是 Research Reviewer Loop #4。收到交接信息，需要：
1. 确认硬约束
2. 用 read_registry 检查当前实验状态

先确认：项目处于 Paper Final 阶段，DDL 是 2026-05-25 AoE，今天就是 2026-05-25。无 GPU/服务器，纯论文项目。

让我先 read_registry 确认实验状态。
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "87d613ec-d92d-413b-ba64-5b0db2743256",
  "isSidechain": false,
  "requestId": "req_011CbNnq5ZEuUMpirbebtBrZ",
  "type": "assistant",
  "uuid": "504f5d13-8c58-435f-a625-cc751c11d7cb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/.claude/sessions/reviewer_430cd31d",
  "sessionId": "ef30c0ef-29fb-4cb0-a309-7059c0bcd7c6",
  "version": "2.1.126",
  "gitBranch": "rebuttal-b1-b7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Q8DSJXCsjYdteqWzwRQxhv",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 24068,
      "cache_read_input_tokens": 11841,
      "output_tokens": 295,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 24068,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 295,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 24068,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 24068
          },
          "type": "message"
        }
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

_source line 9 · 2026-05-25T06:11:11.734Z_

收到交接。硬约束确认：无 GPU/服务器、正文 ≤8 页零余量、abstract 161 words、DDL 今天 2026-05-25 AoE。正在查 registry 确认实验状态。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "504f5d13-8c58-435f-a625-cc751c11d7cb",
  "isSidechain": false,
  "requestId": "req_011CbNnq5ZEuUMpirbebtBrZ",
  "type": "assistant",
  "uuid": "035dd777-b407-42af-9889-61ac4e29a5e7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/.claude/sessions/reviewer_430cd31d",
  "sessionId": "ef30c0ef-29fb-4cb0-a309-7059c0bcd7c6",
  "version": "2.1.126",
  "gitBranch": "rebuttal-b1-b7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Q8DSJXCsjYdteqWzwRQxhv",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 24068,
      "cache_read_input_tokens": 11841,
      "output_tokens": 295,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 24068,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 295,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 24068,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 24068
          },
          "type": "message"
        }
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

_source line 10 · 2026-05-25T06:11:12.680Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01GwsPhWuk7iKyzKtHjKoMgB`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_registry",
  "max_results": 1
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "035dd777-b407-42af-9889-61ac4e29a5e7",
  "isSidechain": false,
  "requestId": "req_011CbNnq5ZEuUMpirbebtBrZ",
  "type": "assistant",
  "uuid": "71914b4a-ddac-4280-a3c5-abc916ac5a3e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/.claude/sessions/reviewer_430cd31d",
  "sessionId": "ef30c0ef-29fb-4cb0-a309-7059c0bcd7c6",
  "version": "2.1.126",
  "gitBranch": "rebuttal-b1-b7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Q8DSJXCsjYdteqWzwRQxhv",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 24068,
      "cache_read_input_tokens": 11841,
      "output_tokens": 295,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 24068,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 295,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 24068,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 24068
          },
          "type": "message"
        }
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

_source line 11 · 2026-05-25T06:11:12.687Z_

<details><summary>↩ Tool result · `toolu_01GwsPhWuk7iKyzKtHjKoMgB`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__read_registry"
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "71914b4a-ddac-4280-a3c5-abc916ac5a3e",
  "isSidechain": false,
  "promptId": "f4e13317-a93b-4dd7-b756-e44063b582f1",
  "type": "user",
  "uuid": "9d21f786-d9d9-4ce7-983b-6cf7a6530524",
  "toolUseResult": {
    "matches": [
      "mcp__agent-ml-research__read_registry"
    ],
    "query": "select:mcp__agent-ml-research__read_registry",
    "total_deferred_tools": 35
  },
  "sourceToolAssistantUUID": "71914b4a-ddac-4280-a3c5-abc916ac5a3e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/.claude/sessions/reviewer_430cd31d",
  "sessionId": "ef30c0ef-29fb-4cb0-a309-7059c0bcd7c6",
  "version": "2.1.126",
  "gitBranch": "rebuttal-b1-b7"
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-25T06:11:18.144Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_01MuTMJn3m9Viaa1TKVmLbM7`</summary>

```json
{
  "project": "irt_equated_bench_regen",
  "limit": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9d21f786-d9d9-4ce7-983b-6cf7a6530524",
  "isSidechain": false,
  "requestId": "req_011CbNnqqyCdnqgkc1TptkpF",
  "type": "assistant",
  "uuid": "e7cb72d4-d874-44b8-900e-3cbed253222b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/.claude/sessions/reviewer_430cd31d",
  "sessionId": "ef30c0ef-29fb-4cb0-a309-7059c0bcd7c6",
  "version": "2.1.126",
  "gitBranch": "rebuttal-b1-b7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012vxt9oDQXFJxUXd6Pz1vUr",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 657,
      "cache_read_input_tokens": 35909,
      "output_tokens": 89,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 657,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 89,
          "cache_read_input_tokens": 35909,
          "cache_creation_input_tokens": 657,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 657
          },
          "type": "message"
        }
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

_source line 13 · 2026-05-25T06:11:18.245Z_

<details><summary>↩ Tool result · `toolu_01MuTMJn3m9Viaa1TKVmLbM7`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"experiments\": {\"plan_035_q3_inflation_sim\": {\"status\": \"DONE\", \"created_at\": \"2026-05-21T15:43:20.736Z\", \"updated_at\": \"2026-05-21T16:24:02.388Z\", \"hypothesis\": \"plan_013 发现 11.3% within-subject item pairs |Q3|>0.20，存在局部依赖(LD)。MH-DIF 假设局部独立，LD 可能膨胀 Type I error。通过 Monte Carlo 模拟或 within-subject permutation null（保持 Q3 结构），量化 LD 对 MH-DIF FPR 的实际膨胀程度。预测：校准 LD 后实际 FPR 膨胀 <3pp（从 nominal 5% 到 <8%），因为 LD 温和（mean Q3=0.009）且 MH 的 total-score stratification 部分吸收了 LD 效应。\", \"parent\": \"plan_013_q3_local_independence\", \"conclusion\": \"success\", \"metrics\": {\"n_subjects\": 8, \"n_permutations\": 1000, \"method\": \"permutation null + independence control, cross-subject matching\", \"ets_c_inflation\": {\"mean_pp\": 0.0004, \"max_pp\": 0.001, \"max_subject\": \"marketing\", \"verdict\": \"far below 3pp threshold\"}, \"p05_inflation\": {\"mean_pp\": -0.0019, \"direction\": \"slightly negative (no inflation)\", \"mean_fpr_with_ld\": 0.0412, \"mean_fpr_without_ld\": 0.0431}, \"subject_details\": {\"moral_scenarios\": {\"q3_pct\": 34.2, \"ets_c_delta_pp\": -1e-05}, \"human_aging\": {\"q3_pct\": 20.5, \"ets_c_delta_pp\": 0.0004}, \"world_religions\": {\"q3_pct\": 18.1, \"ets_c_delta_pp\": 0.0006}, \"marketing\": {\"q3_pct\": 17.5, \"ets_c_delta_pp\": 0.001}, \"professional_law\": {\"q3_pct\": 10.5, \"ets_c_delta_pp\": 0.0003}, \"college_medicine\": {\"q3_pct\": 4.6, \"ets_c_delta_pp\": 0.0005}}, \"q3_inflation_correlation\": {\"spearman_rho\": -0.238, \"p_value\": 0.57, \"significant\": false}, \"key_insight\": \"Cross-subject matching completely isolates within-subject LD from MH-DIF FPR\"}, \"notes\": \"LD inflation simulation 完成。核心发现：cross-subject matching 完全隔离了 within-subject LD 对 MH-DIF FPR 的影响。ETS-C 标准下 LD 膨胀仅 +0.0004pp（最大 +0.001pp），远低于 3pp 阈值。p<0.05 标准下甚至略为负（-0.0019pp，无膨胀）。即使 moral_scenarios 有 34.2% item pairs |Q3|>0.20，ETS-C 膨胀仍 <0.01pp。两个机制：(1) cross-subject matching 变量不含当前 subject items，LD 无法污染 matching；(2) ETS-C 的 |Δ|≥1.5 阈值本身极保守（actual FPR ~0.1%，远低于 nominal 5%）。Q3 与膨胀无显著相关（ρ=-0.24, p=0.57）。直接回应 Reviewer 对 LD violation 的担忧。\"}, \"plan_036_growing_pains_lookup\": {\"status\": \"DONE\", \"created_at\": \"2026-05-21T15:43:28.053Z\", \"updated_at\": \"2026-05-21T16:22:42.643Z\", \"hypothesis\": \"Growing Pains LLM benchmark paper 使用 FPC (Focal Point Contamination) anchor items 来检测污染。如果 FPC anchor item list 公开可得，与我们的 DIF C-flagged items 计算 Jaccard overlap 和 enrichment ratio。如果有显著 overlap (enrichment>2)，则 DIF 与 FPC 检测互补；如果无 overlap (enrichment≈1)，则证明 DIF 和 FPC 捕捉不同信号维度。\", \"parent\": \"plan_001_real_data_dif_mmlu\", \"conclusion\": \"success\", \"metrics\": {\"paper_found\": true, \"title\": \"Growing Pains: Extensible and Efficient LLM Benchmarking Via Fixed Parameter Calibration\", \"authors\": \"Habba et al.\", \"venue\": \"arXiv 2604.12843 (April 2026)\", \"fpc_meaning\": \"Fixed Parameter Calibration (NOT Focal Point Contamination)\", \"contamination_detection\": false, \"anchor_item_list_public\": false, \"overlap_analysis_possible\": false, \"relevance_to_our_work\": \"shared IRT foundation + contamination acknowledged as limitation\"}, \"notes\": \"Growing Pains (Habba et al., 2026) 的 FPC = Fixed Parameter Calibration，不是 Focal Point Contamination。论文用 IRT anchor items 做高效 benchmark 校准（100 anchor items per dataset, 395+ models, Spearman ρ≥0.9），不涉及污染检测。Anchor item IDs 动态计算、未公开持久化。无法执行 Jaccard overlap 分析。但论文在 Limitations 中承认 anchor items 可能随时间被污染，直接支持我们 DIF-based detection 的必要性论点。适合在 Related Work 中引用。\"}, \"plan_034_multi_subject_injection\": {\"status\": \"DONE\", \"created_at\": \"2026-05-21T15:43:12.118Z\", \"updated_at\": \"2026-05-21T16:02:54.334Z\", \"hypothesis\": \"Proposition 1 声称当污染局限于单一 subject 时 ΔFPR=0（cross-subject matching 不受污染）。当同时污染 k∈{1,2,3,5,10,20} 个 subject 时，matching variable 被逐步污染，ΔFPR(k) 将随 k 单调递增。具体预测：k≤3 时 ΔFPR<0.02（matching variable 被稀释），k≥10 时 ΔFPR>0.05（matching variable 严重受污）。ΔTPR(k) 在 k=1 与 k=20 之间保持稳定（>0.3 at p=0.5），因为 detection 对 target subject 内的 signal 而非 matching quality 更敏感。\", \"parent\": \"plan_016_within_subject_semi_synthetic\", \"conclusion\": \"success\", \"metrics\": {\"grid\": {\"k_values\": [1, 2, 3, 5, 10, 20], \"p_values\": [0.1, 0.3, 0.5], \"seeds_per_k\": 5, \"total_runs\": 90}, \"n_ref\": 1080, \"n_foc\": 807, \"n_foc_inject\": 787, \"proposition_1_boundary\": \"k≈5-10 subjects\", \"non_target_delta_fpr\": {\"k1_p05\": 0.002, \"k2_p05\": 0.002, \"k3_p05\": -0.001, \"k5_p05\": 0.007, \"k10_p03\": 0.026, \"k10_p05\": 0.069, \"k20_p03\": 0.072, \"k20_p05\": 0.167}, \"target_tpr\": {\"k1_p05\": 0.834, \"k5_p05\": 0.734, \"k10_p05\": 0.67, \"k20_p05\": 0.611}, \"key_findings\": {\"k_le_5_robust\": true, \"k_le_5_max_delta_fpr\": 0.007, \"k10_significant_at_p03\": true, \"k20_massive_inflation\": true, \"p01_robust_all_k\": true, \"tpr_dilution_with_k\": true, \"boundary_rule\": \"cross-subject DIF reliable when contaminated fraction <10%\"}}, \"notes\": \"Proposition 1 robustness boundary 实验完成。核心结论：cross-subject MH-DIF 在 k≤5 subjects (≤8.8%) 同时污染时 ΔFPR<0.007，Proposition 1 实际成立。k=10 (17.5%) 开始 p≥0.3 时 ΔFPR 显著（+0.026~+0.069）。k=20 (35.1%) 大规模膨胀（p=0.5 时 ΔFPR=+0.167）。低强度 p=0.1 在所有 k 值下都 robust。TPR 随 k 增大而下降（0.834→0.611 at p=0.5），因为 matching variable 吸收了部分 DIF 信号。实际意义：real-world 污染通常影响少数 subjects，cross-subject auditing 有足够 safety margin。\"}, \"plan_028_multi_bench_dif\": {\"status\": \"DONE\", \"created_at\": \"2026-05-21T10:45:20.123Z\", \"updated_at\": \"2026-05-21T14:04:56.321Z\", \"hypothesis\": \"Temporal DIF (2023 vs 2024 cohort) 在 METABENCH 的 ARC, HellaSwag, WinoGrande, TruthfulQA 上均展现与 MMLU 类似的显著 C% (>15%)，证明 temporal DIF 现象跨 benchmark 泛化，不是 MMLU 特有的 artifact。所有 benchmark 的 random-split control C% < 1%。\", \"parent\": \"plan_001_real_data_dif_mmlu\", \"metrics\": {\"mmlu\": {\"n_items\": 12508, \"n_ref\": 1080, \"n_foc\": 807, \"pct_c\": 31.3, \"random_pct_c\": 0.18, \"bootstrap_ci_95\": [29.38, 38.05], \"bootstrap_mean\": 33.14, \"bootstrap_sd\": 2.3, \"bootstrap_n\": 1000}, \"winogrande\": {\"n_items\": 1267, \"n_ref\": 1017, \"n_foc\": 803, \"pct_c\": 30.3, \"random_pct_c\": 0.32}, \"truthfulqa\": {\"n_items\": 817, \"n_ref\": 1080, \"n_foc\": 807, \"pct_c\": 29.7, \"random_pct_c\": 0.37}, \"arc\": {\"n_items\": 1172, \"n_ref\": 1080, \"n_foc\": 807, \"pct_c\": 26.9, \"random_pct_c\": 0.6}, \"gsm8k\": {\"n_items\": 1319, \"n_ref\": 1017, \"n_foc\": 804, \"pct_c\": 18.9, \"random_pct_c\": 0.3}, \"hellaswag\": {\"n_items\": 10042, \"n_ref\": 1080, \"n_foc\": 807, \"pct_c\": 17.9, \"random_pct_c\": 0.28}, \"cross_benchmark_range\": \"17.9-31.3%\", \"all_random_controls_below_1pct\": true, \"min_enrichment_ratio\": 45, \"n_benchmarks\": 6}, \"conclusion\": \"success\", \"notes\": \"All 6 METABENCH benchmarks show significant temporal DIF (17.9-31.3% ETS C), with all random controls <1%. Cross-benchmark consistency confirms temporal DIF is a universal phenomenon, not MMLU-specific. Knowledge/reasoning benchmarks (MMLU 31.3%, TruthfulQA 29.7%, ARC 26.9%, WinoGrande 30.3%) show higher C% than math/commonsense (GSM8K 18.9%, HellaSwag 17.9%). This directly addresses Dream #6 reviewer concern about single-benchmark generalizability. Worker failed 5× due to OOM on hellaswag.csv (2GB, 52M rows) — fixed with chunked loading.\"}, \"plan_032_dif_cleaned_mmlu\": {\"status\": \"DONE\", \"created_at\": \"2026-05-21T13:38:51.707Z\", \"updated_at\": \"2026-05-21T13:49:14.041Z\", \"hypothesis\": \"虽然 DIF-cleaned MMLU 的全局 rank correlation 很高 (ρ≈0.997)，但局部排名变化将揭示 DIF 的实际影响：特定模型家族（尤其是 2024 年新模型如 phi-3, llama-3）将在移除 C-flagged items 后排名显著下降，而 2023 年模型排名上升。这证明 DIF items 虽然不改变全局趋势，但系统性地偏向特定模型代际，构成 benchmark fairness 问题。\", \"parent\": \"plan_017_downstream_impact\", \"metrics\": {\"n_items_full\": 12508, \"n_items_cleaned\": 8590, \"n_items_removed\": 3918, \"pct_removed\": 31.3, \"spearman_rho\": 0.9965, \"rank_change_std\": 127.1, \"rank_change_min\": -589, \"rank_change_max\": 849, \"pct_change_ge5\": 89.5, \"pct_change_ge10\": 79.5, \"pct_change_ge20\": 66.4, \"pct_change_ge50\": 41.9, \"pct_change_ge100\": 24.8, \"top100_pct_ge10\": 18, \"top500_pct_ge10\": 47.2, \"cohort_2023_mean_change\": -22.56, \"cohort_2023_median_change\": -5, \"cohort_2024_mean_change\": 73.6, \"cohort_2024_median_change\": 11, \"systematic_bias\": \"DIF items favor 2024 models; cleaning hurts 2024 +73.6 avg, helps 2023 -22.6 avg\", \"top_hurt_families\": {\"phi-3\": 258.35, \"command-r\": 235, \"solar\": 149.15, \"llama-3\": 120.86}, \"top_benefit_families\": {\"mistral-0.1\": -60.32, \"mistral\": -53.27, \"zephyr\": -29.94, \"gemma-2\": -28.78}, \"removed_items_harder\": true, \"removed_mean_difficulty\": 0.409, \"cleaned_mean_difficulty\": 0.46, \"random_baseline_20trials\": {\"rank_change_std\": {\"mean\": 60.2, \"std\": 7.8}, \"mean_abs_rank_change\": {\"mean\": 36, \"std\": 3.6}, \"pct_change_ge100\": {\"mean\": 8.5, \"std\": 2}, \"cohort_2023_mean_change\": {\"mean\": 0.4, \"std\": 4.1}, \"cohort_2024_mean_change\": {\"mean\": 2.8, \"std\": 21.2}}, \"dif_vs_random_z_scores\": {\"rank_change_std_z\": 8.5, \"mean_abs_change_z\": 10.7, \"pct_ge100_z\": 8.2, \"cohort_2023_z\": -5.6, \"cohort_2024_z\": 3.3, \"cohort_asymmetry_gap_z\": 4.4}}, \"notes\": \"直接回应 Dream #7 \\\"ρ=0.997 is the paper's most damaging result\\\" 审稿意见。全局 ρ=0.9965 确实很高，但掩盖了剧烈的局部排名变化：89.5% 模型变化 ≥5 位，24.8% 变化 ≥100 位，最大变化 849 位。关键发现：系统性 cohort 偏差——2024 模型平均排名下降 73.6 位，2023 模型平均上升 22.6 位。Phi-3 下降 258 位, Llama-3 下降 121 位（DIF items 偏向这些新模型）。Mistral 系列上升 53 位。这证明 DIF 不仅是统计标记，更揭示了 benchmark 对不同模型代际的系统性偏差。\", \"conclusion\": \"success\"}, \"plan_033_subject_dif_concentration\": {\"status\": \"DONE\", \"created_at\": \"2026-05-21T13:41:16.628Z\", \"updated_at\": \"2026-05-21T13:42:06.450Z\", \"hypothesis\": \"DIF 在 MMLU 57 个 subject 间分布不均匀，且 STEM vs Humanities 存在系统性差异。控制 item difficulty 和 discrimination 后，特定 subject 的 content 本身预测 DIF 概率——这说明 DIF 不仅由 psychometric properties 驱动，还受知识领域内容特征影响。同时，DIF 的方向（favor 2023 vs 2024）可能在不同领域呈现不同模式。\", \"parent\": \"plan_001_real_data_dif_mmlu\", \"metrics\": {\"n_subjects\": 57, \"all_subjects_have_dif\": true, \"mean_pct_c\": 30.6, \"median_pct_c\": 29.7, \"sd_pct_c\": 5.5, \"range_pct_c\": [20.7, 48.4], \"top3_subjects\": {\"business_ethics\": 48.4, \"human_aging\": 41.9, \"formal_logic\": 40.4}, \"bottom3_subjects\": {\"computer_security\": 20.7, \"marketing\": 20.9, \"management\": 21.7}, \"domain_pct_c\": {\"STEM\": 30.9, \"Humanities\": 31.1, \"Social_Science\": 31.6}, \"stem_vs_humanities_p\": 0.611, \"kruskal_wallis_p\": 0.78, \"logistic_regression\": {\"difficulty_OR\": 0.086, \"discrimination_OR\": 57.2, \"pseudo_r2\": 0.042}, \"excess_dif_subjects\": [\"professional_law\", \"human_aging\", \"world_religions\", \"business_ethics\", \"professional_medicine\"], \"overall_pct_favor_2024\": 43.9, \"temporal_asymmetry\": {\"STEM_pct_favor_2024\": 55.4, \"Humanities_pct_favor_2024\": 35.6, \"Social_Science_pct_favor_2024\": 42}, \"unidirectional_subjects\": {\"world_religions\": {\"pct_favor_2024\": 16.9}, \"logical_fallacies\": {\"pct_favor_2024\": 20}}}, \"notes\": \"Hypothesis 部分验证：DIF rate 跨 domain 无显著差异 (STEM 30.9% vs Humanities 31.1%, p=0.61)，但 DIF direction 有强领域依赖——STEM 55.4% DIF items 偏向 2024 模型（能力提升），Humanities 仅 35.6%（64.4% 偏向 2023）。world_religions 和 logical_fallacies 呈近单向偏向 2023 (≥80%)。Logistic regression: discrimination OR=57.2, difficulty OR=0.086, 但 pseudo R²=0.042——item properties 仅解释 4% DIF variance，content 特征是主要驱动力。5 个 subject 控制 item props 后仍有 excess DIF (professional_law, human_aging, world_religions, business_ethics, professional_medicine)。\", \"conclusion\": \"success\"}, \"plan_031_temporal_granularity\": {\"status\": \"DONE\", \"created_at\": \"2026-05-21T12:46:39.820Z\", \"updated_at\": \"2026-05-21T12:49:28.194Z\", \"hypothesis\": \"如果 temporal DIF 随时间距离单调递增，则 half-year cohort (2023-H2 vs 2024-H1, 0.5yr) 的 C% 应显著低于 full-year (2023 vs 2024, 1.0yr) 的 C%。这检验 DIF 信号是否与 temporal distance 成正比，回应 Reviewer 对 binary temporal split 过于粗糙的批评。如果 half-year C% ≈ full-year C%，说明 DIF 信号在短至 6 个月的窗口内即已饱和。\", \"parent\": \"plan_001_real_data_dif_mmlu\", \"metrics\": {\"mmlu_full_year\": {\"comparison\": \"2023 vs 2024\", \"distance_yr\": 1, \"n_ref\": 1080, \"n_foc\": 807, \"pct_c\": 31.32, \"random_pct_c\": 0.02}, \"mmlu_half_year\": {\"comparison\": \"2023-H2 vs 2024-H1\", \"distance_yr\": 0.5, \"n_ref\": 1018, \"n_foc\": 807, \"pct_c\": 34.35, \"random_pct_c\": 0.19}, \"mmlu_within_2023\": {\"comparison\": \"2023-H1 vs 2023-H2\", \"distance_yr\": 0.5, \"n_ref\": 62, \"n_foc\": 1018, \"pct_c\": 22.62, \"random_pct_c\": 0.18, \"supplementary\": true}, \"cross_bench_half_year\": {\"arc_pct_c\": 29.27, \"hellaswag_pct_c\": 18.07, \"winogrande_pct_c\": 33.62, \"truthfulqa_pct_c\": 31.33}, \"cross_bench_full_year\": {\"arc_pct_c\": 26.88, \"hellaswag_pct_c\": 17.89, \"winogrande_pct_c\": 30.31, \"truthfulqa_pct_c\": 29.74}, \"half_year_gt_full_year_all_benchmarks\": true, \"dif_saturates_within_6mo\": true}, \"notes\": \"Reviewer 评定 partial success：MMLU 半年有效（34.35% vs 0.19%, 181× enrichment），但 cross-benchmark 半年 enrichment 不均——HellaSwag 仅 3.5× (18.07%/5.23%)，其余 ARC 12.2×, WinoGrande 12.2×, TruthfulQA 51.4×。DIF 在 6 个月内即饱和，cohort purity > temporal distance。2023-H1 vs 2023-H2 (supplementary, N=62 < 80): C%=22.62%。\", \"conclusion\": \"success\"}, \"plan_030_odds_ratio\": {\"status\": \"DONE\", \"created_at\": \"2026-05-21T10:17:26.316Z\", \"updated_at\": \"2026-05-21T10:18:26.271Z\", \"hypothesis\": \"Logistic regression 的 odds ratio + CI 量化 accuracy change 与 DIF C flag 的关联强度。Item-level accuracy change (Model 3) 比 domain-level delta (Model 1) 提供更精确的预测。控制 item properties (difficulty + discrimination) 后，accuracy change 的 OR 反转（Simpson's paradox），说明 DIF C 主要由 item 固有属性驱动而非 accuracy shift。\", \"parent\": \"plan_001_real_data_dif_mmlu\", \"metrics\": {\"model1_domain_delta\": {\"mcfadden_r2\": 0.0007, \"nagelkerke_r2\": 0.0012, \"aic\": 15545.2, \"subject_acc_delta_or\": 80.86, \"subject_acc_delta_or_per_010\": 1.55, \"subject_acc_delta_or_ci_per_010\": [1.19, 2.03]}, \"model2_domain_delta_plus_items\": {\"mcfadden_r2\": 0.0423, \"nagelkerke_r2\": 0.072, \"aic\": 14902.3, \"subject_acc_delta_or_per_010\": 0.73, \"ctt_difficulty_or_per_010\": 0.78, \"ctt_discrimination_or_per_010\": 1.51}, \"model3_item_delta\": {\"mcfadden_r2\": 0.0012, \"nagelkerke_r2\": 0.0021, \"aic\": 15536.9, \"item_acc_change_or\": 2.11, \"item_acc_change_or_per_010\": 1.08, \"item_acc_change_ci\": [1.51, 2.96]}, \"model4_item_delta_plus_items\": {\"mcfadden_r2\": 0.0434, \"nagelkerke_r2\": 0.0737, \"aic\": 14885.4, \"item_acc_change_or_per_010\": 0.92, \"ctt_difficulty_or_per_010\": 0.77, \"ctt_discrimination_or_per_010\": 1.54}, \"simpsons_paradox\": true, \"lr_test_m1_vs_m2_chi2\": 646.98, \"lr_test_m3_vs_m4_chi2\": 655.53, \"best_model\": \"Model 4 (item Δ + item props)\"}, \"conclusion\": \"success\"}, \"plan_027_temporal_overlap\": {\"status\": \"DONE\", \"created_at\": \"2026-05-21T08:34:47.232Z\", \"updated_at\": \"2026-05-21T08:38:52.937Z\", \"hypothesis\": \"Temporal cohort ability gap 很小 (d=-0.17)，ability-matched C% 接近 full 31.3%，确认 temporal DIF 非 ability confound 产物\", \"parent\": \"plan_001_real_data_dif_mmlu\", \"metrics\": {\"cohort_2023_n\": 1080, \"cohort_2023_mean\": 0.5814, \"cohort_2023_sd\": 0.1405, \"cohort_2024_n\": 807, \"cohort_2024_mean\": 0.6068, \"cohort_2024_sd\": 0.1556, \"cohens_d\": -0.173, \"overlap_coefficient\": 0.764, \"bhattacharyya\": 0.961, \"full_c_pct\": 31.3, \"score_range_overlap_c_pct\": 30.9, \"nn_matched_c_pct_mean\": 28.9, \"nn_matched_c_pct_sd\": 0.1, \"nn_matched_n_per_group\": 638, \"nn_matched_d\": -0.01, \"ability_confound_pp\": 2.4, \"ability_confound_pct_of_total\": 7.7, \"llama_comparison_d\": -0.99, \"llama_comparison_overlap\": 0.18, \"llama_matched_c_pct\": 28.3}, \"conclusion\": \"success\"}, \"plan_004_gsm8k_cross_benchmark\": {\"status\": \"DONE\", \"created_at\": \"2026-05-21T00:30:09.372Z\", \"updated_at\": \"2026-05-21T01:22:16.029Z\", \"hypothesis\": \"GSM8K 的 temporal DIF (2023 vs 2024) 将展示与 MMLU 类似的 30-40% ETS C%，证明 temporal DIF 现象跨 benchmark 泛化。使用 METABENCH 其他 benchmarks 总分做 external matching（GSM8K 无 subject 分层），预期 baseline FPR 更可控。如果 C% 在同一量级 → DIF 作为 benchmark health diagnostic 的泛化性得到验证。\", \"parent\": \"plan_001_real_data_dif_mmlu\", \"metrics\": {\"step1_gsm8k_temporal_dif\": {\"n_items\": 1319, \"n_ref\": 1017, \"n_foc\": 804, \"standard_c_pct\": 18.9, \"external_c_pct\": 47.4, \"sanity_c_pct\": 0.3, \"standard_external_spearman\": 0.926}, \"step2_semi_synthetic\": {\"standard_delta_tpr_p10\": 0.818, \"external_delta_tpr_p10\": 0.517}, \"step3_gsm1k_correlation\": {\"n_models\": 33, \"n_dif_c_items\": 249, \"pearson_r\": -0.478, \"pearson_p\": 0.005, \"spearman_rho\": -0.403, \"spearman_p\": 0.02, \"partial_r_controlling_accuracy\": -0.385, \"partial_p\": 0.027, \"permutation_p\": 0.014, \"dif_c_favor_2024\": 78, \"dif_c_favor_2023\": 171, \"direction\": \"NEGATIVE (opposite to contamination hypothesis)\", \"cook_d_max_model\": \"Deepseek-math-7b-rl\", \"leave_one_out_r_range\": \"-0.537 to -0.374\", \"robust\": true}}, \"notes\": \"Step 3 GSM1K correlation: r=-0.478 (p=0.005). |r|>0.3 threshold met but direction NEGATIVE — opposite to contamination hypothesis. DIF-C items disadvantage contaminated models, not advantage them. 171/249 DIF-C items favor older models. Partial r=-0.385 (p=0.027) controlling for overall accuracy. Permutation p=0.014. Robust to leave-one-out. Interpretation: DIF captures genuine measurement anomalies orthogonal to contamination. Contamination produces narrow boost on typical items, fails on atypical-difficulty items (DIF-C). Supports characterization narrative: DIF as benchmark health diagnostic, not contamination detector.\", \"conclusion\": \"negative\"}, \"plan_017_downstream_impact\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T23:44:12.194Z\", \"updated_at\": \"2026-05-21T00:05:41.991Z\", \"hypothesis\": \"移除 temporal DIF-flagged items (ETS C, ~31% of MMLU items) 后，模型跨代排名更稳定（Spearman ρ 提升），且稳定性提升显著优于随机移除相同数量 items 的 baseline。这证明 DIF 不只标记 noise，而是精确识别了 problematic items，为 DIF 作为 benchmark quality tool 提供 downstream evidence。\", \"parent\": \"plan_001_real_data_dif_mmlu\", \"metrics\": {\"n_dif_items\": 3918, \"n_stable_items\": 8590, \"dif_pct\": 31.3, \"rho_full_vs_stable_2023\": 0.998851, \"rho_full_vs_stable_2024\": 0.997014, \"rho_full_vs_stable_all\": 0.996451, \"shr_full\": 0.9934, \"shr_stable\": 0.9919, \"dif_vs_random_z_mean\": -14.91, \"dif_vs_random_all_21_conditions_significant\": true, \"dif_removal_MORE_disruptive_than_random\": true, \"cross_cohort_ratio_dif_vs_full\": 1.0919, \"cross_cohort_ratio_stable_vs_full\": 0.9581, \"top_beneficiaries\": \"phi-3, llama-3 derivatives\", \"top_hurt\": \"mistral merges, slerp models\", \"max_rank_change\": 851}, \"conclusion\": \"negative\", \"notes\": \"Hypothesis REJECTED but finding is richer. DIF removal causes MORE ranking disruption than random (z=-8 to -49σ, 21/21 conditions). DIF items are NOT noise — they carry concentrated differential information that systematically discriminates models. Key insight: DIF items capture temporal instability (1.09× cross-cohort accuracy swing vs 0.96× stable items). Rankings are very robust (ρ>0.996 even at 38% removal). Top beneficiaries of DIF items: phi-3 and llama-3 derivatives (+700-850 ranks). Top hurt: mistral merges/slerp models (-400 to -587 ranks). Paper narrative shift: DIF items are not \\\"bad items to remove\\\" but \\\"items that reveal differential model capabilities across generations\\\" — supports characterization narrative over cleaning narrative.\"}, \"plan_016_within_subject_semi_synthetic\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T22:30:50.476Z\", \"updated_at\": \"2026-05-20T22:49:02.342Z\", \"hypothesis\": \"在 subject 内部使用 within-subject total score 做 MH 分层的 semi-synthetic injection 中，DIF 仍能检测差异性污染（ΔTPR > 0.3 at p=0.5）。这证明 DIF 方法在 subject 级别也有效，plan_014 的 38% within-subject C% 反映的是真实代际能力差异而非方法失败。\", \"parent\": \"plan_014_within_subject_dif\", \"metrics\": {\"within_matching\": {\"subjects_passing_p05\": \"3/5 (human_aging, professional_medicine, formal_logic)\", \"business_ethics_baseline_fpr\": 0.563, \"business_ethics_delta_tpr_p05\": -0.078, \"human_aging_baseline_fpr\": 0.334, \"human_aging_delta_tpr_p05\": 0.385, \"professional_medicine_baseline_fpr\": 0.312, \"professional_medicine_delta_tpr_p05\": 0.327, \"formal_logic_baseline_fpr\": 0.409, \"formal_logic_delta_tpr_p05\": 0.457, \"high_school_statistics_baseline_fpr\": 0.407, \"high_school_statistics_delta_tpr_p05\": 0.194, \"fpr_inflates_with_injection\": true, \"avg_fpr_inflation_p10\": 0.186}, \"cross_matching\": {\"subjects_passing_p05\": \"4/5 (human_aging, professional_medicine, formal_logic, high_school_statistics)\", \"business_ethics_baseline_fpr\": 0.533, \"business_ethics_delta_tpr_p05\": 0.056, \"human_aging_baseline_fpr\": 0.431, \"human_aging_delta_tpr_p05\": 0.375, \"professional_medicine_baseline_fpr\": 0.38, \"professional_medicine_delta_tpr_p05\": 0.38, \"formal_logic_baseline_fpr\": 0.402, \"formal_logic_delta_tpr_p05\": 0.543, \"high_school_statistics_baseline_fpr\": 0.335, \"high_school_statistics_delta_tpr_p05\": 0.433, \"fpr_stable_across_injection\": true, \"delta_fpr_all_subjects\": 0}, \"success_criterion_met\": true}, \"conclusion\": \"success\", \"notes\": \"Revised per Director review. (1) Fixed comparison table FPR (0.048→0.314). (2) Added cross-subject matching: FPR completely stable (ΔFPR=0.000 all 5 subjects), better detection (4/5 ΔTPR>0.3 vs within 3/5). Within-subject FPR inflates +0.067 to +0.281 at p=1.0 due to matching variable contamination. (3) Added formal_logic (109 items, ΔTPR=+0.543 cross) and high_school_statistics (181 items, ΔTPR=+0.433 cross). Both 5 strata, clean detection. Cross-subject matching confirms plan_011's external MH finding at subject level.\"}, \"plan_013_q3_local_independence\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T21:58:11.134Z\", \"updated_at\": \"2026-05-20T22:36:16.364Z\", \"hypothesis\": \"MMLU 同一 subject 内的 items 存在显著局部依赖性（within-subject Q3 均值 > 0.20，显著高于 cross-subject Q3），这违反 2PL IRT 和 MH-DIF 的局部独立性假设，部分解释了 plan_011 中 temporal cohort baseline FPR=31% 的膨胀。如果确认，则动机化后续 bifactor/testlet 模型改进。\", \"parent\": \"plan_011_semi_synthetic_validation\", \"metrics\": {\"within_subject_mean_q3\": 0.0086, \"cross_subject_mean_q3\": 0.0031, \"within_subject_pct_above_020\": 11.3, \"cross_subject_pct_above_020\": 2.2, \"mann_whitney_p\": 2.29e-09, \"worst_subject\": \"moral_scenarios\", \"worst_subject_pct_above_020\": 34.2, \"n_items_retained\": 12251, \"n_items_filtered\": 257, \"subject_size_q3_corr\": 0.2064, \"subject_size_q3_p\": 0.123}, \"conclusion\": \"success\", \"notes\": \"Q3 诊断完成。Hypothesis 部分验证：within-subject 均值 Q3=0.0086（低于 0.20 阈值），但尾部显著——11.3% within-subject pairs |Q3|>0.20 vs 2.2% cross-subject（5x, Mann-Whitney p=2.3e-9）。局部依赖存在但温和，不太可能单独解释 31% FPR。最严重 subjects: moral_scenarios 34.2%, world_religions 18%, marketing 17.5%。结论：局部依赖是 FPR 的贡献因素之一，但主要 FPR 来源是 genuine temporal DIF（plan_014 确认 within-subject C%=38%）。\"}, \"plan_015_bifactor_irt\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-20T22:23:51.598Z\", \"updated_at\": \"2026-05-20T22:30:44.925Z\", \"hypothesis\": \"Bifactor IRT（1 general + 57 subject-specific factors）的 general θ 分层能将 temporal cohort baseline FPR 从 31% 降至 <15%，同时在 semi-synthetic 框架下保持 TPR>0.60 at p=0.5。Bifactor 通过分离学科特异性能力和通用能力，消除 subject-level 能力差异对 MH-DIF 的混淆。\", \"parent\": \"plan_012_irt_theta_conditioning\", \"conclusion\": \"killed\", \"notes\": \"D010: Director 取消。plan_014 前置检查结果 within-subject C%=38.1% (>25%)，证明 temporal DIF 渗透到 subject 内部，bifactor 无法解决。Between-subject variance 反而在压低 overall C%。\"}, \"plan_014_within_subject_dif\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T22:23:50.857Z\", \"updated_at\": \"2026-05-20T22:28:27.350Z\", \"hypothesis\": \"Within-subject temporal DIF（只用该 subject 内 items 和总分）在高 C% subjects 上的 C% 将 < 15%，表明 plan_001 的 31% FPR 主要来自 between-subject 能力差异而非 within-subject 因素。如果 within-subject C% > 25%，则 bifactor 模型也无法解决 FPR 问题。\", \"parent\": \"plan_012_irt_theta_conditioning\", \"metrics\": {\"business_ethics_within_c_pct\": 45.2, \"human_aging_within_c_pct\": 33, \"formal_logic_within_c_pct\": 39.5, \"professional_medicine_within_c_pct\": 31.1, \"high_school_statistics_within_c_pct\": 42, \"avg_within_subject_c_pct\": 38.1, \"avg_cross_subject_c_pct\": 40.5, \"avg_delta_within_vs_cross\": -2.4, \"sibtest_available\": false, \"r_available\": false, \"decision_zone\": \">25% HIGH\"}, \"conclusion\": \"negative\", \"notes\": \"Within-subject temporal DIF 前置检查 NEGATIVE。5 个高 C% subjects 平均 within-subject C%=38.1%（全部 >25%）：business_ethics 45.2%, human_aging 33.0%, formal_logic 39.5%, professional_medicine 31.1%, high_school_statistics 42.0%。Cross-subject matching C% 40.5%（Δ=-2.4pp）。结论：temporal DIF 渗透到每个 subject 内部，不是 between-subject 能力差异的伪影。Bifactor 模型大概率无法解决 FPR 问题。SIBTEST: R 不可用，Python 无实现。\"}, \"plan_012_irt_theta_conditioning\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T21:58:10.439Z\", \"updated_at\": \"2026-05-20T22:20:01.371Z\", \"hypothesis\": \"用 2PL IRT 估计的 θ 值（10-20 等距层）替代粗糙总分作为 MH 分层变量后，semi-synthetic 框架下 baseline FPR 将从 ~31%（temporal）/~49%（ability）降至 <10%，同时保持 TPR>0.70 at p=0.5。θ-conditioning 通过更精确的能力匹配消除 impact-vs-DIF 混淆残留。\", \"parent\": \"plan_011_semi_synthetic_validation\", \"metrics\": {\"temporal_theta_qt20_fpr\": 0.312, \"temporal_theta_qt20_tpr_p05\": 0.876, \"temporal_theta_qt20_tpr_p10\": 1, \"temporal_external5_fpr\": 0.314, \"temporal_external5_tpr_p05\": 0.834, \"ability_theta_qt10_fpr\": 0.093, \"ability_theta_qt10_tpr_p05\": 0.206, \"ability_theta_qt10_tpr_p10\": 0.544, \"ability_theta_qt20_fpr\": 0.079, \"ability_theta_qt20_tpr_p05\": 0.21, \"ability_theta_qt20_tpr_p10\": 0.544, \"ability_external5_fpr\": 0.493, \"ability_external5_tpr_p05\": 0.756, \"theta_total_score_corr\": 0.9986, \"enrichment_all_variants\": \"0.97-1.00\", \"success_criterion_met\": false}, \"conclusion\": \"negative\", \"notes\": \"θ-conditioning NEGATIVE. Temporal cohort: logit(p) θ corr=0.9986 with total score, all θ variants FPR=31-35% (no improvement over plan_011 external_5 FPR=31.4%). TPR well maintained (0.83-0.88 at p=0.5). Ability cohort: quantile θ bins (qt_10/qt_20) reduce FPR from 49% to 8-9%, but TPR collapses from 76% to 21% at p=0.5 — proving plan_011 ability cohort's high TPR was mainly ability confounding, not genuine DIF detection. Enrichment vs Li et al.: all variants 0.97-1.00 (unchanged from plan_001). Key conclusion: temporal cohort 31% baseline FPR is genuine DIF (real item-level differences between 2023 vs 2024 models), not an artifact of imprecise ability matching. Improving θ estimation won't fix it — need multidimensional or subject-level approaches.\"}, \"plan_011_semi_synthetic_validation\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T21:35:55.290Z\", \"updated_at\": \"2026-05-20T21:54:54.659Z\", \"hypothesis\": \"在 METABENCH 真实响应矩阵上注入已知差异性污染（focal group 指定 items 的 incorrect→correct 翻转）后，MH-DIF 的 ETS C 分类能在 ability-quintile cohort 上达到 TPR>0.5 (p=1.0) 且 FPR<0.05。如果成功，说明 plan_001/001b 的 enrichment≈1.0 是 Li et al. ground truth 不匹配（全局性 vs 差异性污染），而非 DIF 方法本身失败。\", \"parent\": \"plan_001b_matched_ability_dif\", \"metrics\": {\"temporal_external_tpr_p0\": 0.326, \"temporal_external_tpr_p03\": 0.548, \"temporal_external_tpr_p05\": 0.834, \"temporal_external_tpr_p07\": 0.99, \"temporal_external_tpr_p10\": 1, \"temporal_external_fpr\": 0.314, \"temporal_external_delta_tpr_p10\": 0.674, \"ability_external_tpr_p0\": 0.498, \"ability_external_tpr_p10\": 0.8, \"ability_external_fpr\": 0.493, \"ability_external_delta_tpr_p10\": 0.302, \"standard_mh_fpr_inflation\": \"temporal 0.298→0.616 at p=1.0\", \"matching_variable_contamination_confirmed\": true, \"bug_fix\": \"inf-delta classified as extreme DIF not class A\"}, \"conclusion\": \"success\", \"notes\": \"MH-DIF successfully detects injected differential contamination. Temporal+external: ΔTPR=+0.674 (0.326→1.000), FPR constant at 0.314. Clear dose-response across p={0.3,0.5,0.7,1.0}. Confirms plan_001/001b enrichment≈1.0 is ground truth mismatch (Li et al. = global contamination, DIF = differential contamination), NOT DIF method failure. Also discovered: (1) matching variable contamination when 20% items injected (standard MH FPR inflates 0.298→0.616, anchor/external variants immune), (2) inf-delta classification bug in plan_001 code fixed. Ability cohort has high baseline FPR (~49%) due to extreme Q1-2 vs Q4-5 ability gap — 5-strata insufficient.\"}, \"plan_001b_matched_ability_dif\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T21:35:08.552Z\", \"updated_at\": \"2026-05-20T21:35:51.089Z\", \"hypothesis\": \"在每个 accuracy quintile 内部做 temporal cohort MH-DIF（控制能力后），enrichment 将从 plan_001 的 0.96 提升到 >1.5，证明能力匹配能隔离出污染信号。\", \"parent\": \"plan_001_real_data_dif_mmlu\", \"conclusion\": \"negative\", \"notes\": \"D005: Matched-ability DIF 失败。所有 quintile enrichment 0.94-1.04。能力匹配未能隔离出污染信号。Reviewer 洞察：Li et al. web-overlap 是全局性污染标注（Common Crawl 对所有模型可用），不会产生 group-specific DIF。enrichment≈1.0 可能不是 DIF 方法失败，而是 ground truth 与 DIF 度量的东西根本不同——DIF 检测差异性训练数据包含，Li 检测存在性污染。\"}, \"plan_001_real_data_dif_mmlu\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T20:54:53.883Z\", \"updated_at\": \"2026-05-20T21:12:05.153Z\", \"hypothesis\": \"MH-DIF 在 METABENCH 真实 MMLU 数据（5227 模型 × 12508 items）上，用时间 cohort (2023 vs 2024) 和能力分位 cohort 分组时，ETS C 标记的 items 在 Li et al. clean items 中的 FPR ≤ 0.05，且 ETS C 标记在 contaminated items 中的比例显著高于 clean items。这验证 DIF 在真实数据上不会产生过多假阳性，且能捕捉到与 web-overlap 污染信号一致的差异性。\", \"parent\": \"mvp_dif_power_sim_phase2\", \"metrics\": {\"temporal_ets_c_pct\": 31.3, \"temporal_fpr_li_clean\": 0.318, \"temporal_enrichment\": 0.96, \"ability_ets_c_pct\": 2.9, \"ability_fpr_li_clean\": 0.027, \"ability_enrichment\": 1.19, \"within_family_llama2v3_c_pct\": 61.3, \"within_family_mistral_mixtral_c_pct\": 38.7, \"domain_spearman_rho\": 0.307, \"domain_spearman_p\": 0.02, \"sanity_random_split_c_pct\": 0.18, \"temporal_ability_jaccard\": 0.014}, \"conclusion\": \"negative\", \"notes\": \"Temporal cohort DIF (2023 vs 2024): 31.3% ETS C, enrichment=0.96 — DIF detects systematic capability improvement, NOT contamination (clean and contaminated items flagged at equal rates). Ability cohort: 2.9% C, enrichment=1.19 — weak positive signal, FPR=2.7% well controlled. Within-family (Llama-2 vs 3): 61.3% C confirms ability confound dominates. Domain ρ=0.307 (p=0.02) consistent with capability-driven DIF. Sanity check passed (random split 0.18% C). Core finding: naive MH-DIF cannot distinguish contamination from genuine capability improvement without ability matching or IRT equating.\"}, \"mvp_dif_power_sim_phase2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T18:52:34.145Z\", \"updated_at\": \"2026-05-20T19:30:16.477Z\", \"hypothesis\": \"ETS C 分类在 METABENCH 真实 MMLU 2PL IRT 参数（非理想化分布）下，仍能在 N≥80/group、δ≥1.4 时达到 TPR≥0.65、FPR≤0.10。Phase 1 用合成参数（a~LogNormal, b~N(0,1)）条件性通过，需验证真实参数分布（可能有偏态、聚集、极端值）不会降解检测功效。\", \"parent\": \"mvp_dif_power_sim\", \"metrics\": {\"ets_c_tpr_N80_d14\": 0.6823, \"ets_c_tpr_N80_d16\": 0.7223, \"ets_c_tpr_N100_d14\": 0.7582, \"ets_c_tpr_N100_d16\": 0.7966, \"ets_c_fpr_range\": \"0.036-0.042\", \"best_auc_mh\": 0.9254, \"best_auc_lr\": 0.9405, \"verdict\": \"PASS\", \"pass_plus_met\": true, \"real_param_a_mean\": 1.2, \"real_param_b_mean\": -0.84}, \"conclusion\": \"success\"}, \"mvp_dif_power_sim\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T17:16:29.354Z\", \"updated_at\": \"2026-05-20T18:52:23.378Z\", \"hypothesis\": \"DIF 跨模型批次分析（MH + Logistic Regression）在 N=50-80/group、污染效应量 δ≥1.0 logits 时，对 10% 污染 items 的检测功效 TPR≥0.70 且 FPR≤0.10。这是整个 pipeline 的前提假设——若 DIF 在理想合成数据上都 underpowered，则后续真实数据方案不成立。\", \"metrics\": {\"best_tpr_mh\": 0.6817, \"best_tpr_lr\": 0.6869, \"best_condition\": \"N=100_delta=1.6\", \"best_auc_mh\": 0.9393, \"best_auc_lr\": 0.9593, \"pass_criterion_tpr_mh\": 0.0416, \"pass_criterion_tpr_lr\": 0.0703, \"pass_criterion_condition\": \"N=50_delta=1.0\", \"verdict\": \"FAIL\", \"all_fpr_below_015\": true}, \"conclusion\": \"success\", \"notes\": \"Conditional pass (D001): ETS C classification as primary detector. ETS C TPR=0.72-0.85 at N≥80,δ≥1.4; FPR well controlled. BH-corrected p-value based detection failed (TPR 0.04-0.07 at pass criterion). Raw power also insufficient for p-value approach. AUC discriminability good (0.91-0.96). Decision: pivot to ETS C magnitude-based detection, Phase 2 validates with real IRT parameters.\"}}, \"count\": 21, \"total\": 21, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.0839}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e7cb72d4-d874-44b8-900e-3cbed253222b",
  "isSidechain": false,
  "promptId": "f4e13317-a93b-4dd7-b756-e44063b582f1",
  "type": "user",
  "uuid": "78c8376e-3046-4ba7-b246-d9fc715a7706",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"experiments\\\": {\\\"plan_035_q3_inflation_sim\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-21T15:43:20.736Z\\\", \\\"updated_at\\\": \\\"2026-05-21T16:24:02.388Z\\\", \\\"hypothesis\\\": \\\"plan_013 发现 11.3% within-subject item pairs |Q3|>0.20，存在局部依赖(LD)。MH-DIF 假设局部独立，LD 可能膨胀 Type I error。通过 Monte Carlo 模拟或 within-subject permutation null（保持 Q3 结构），量化 LD 对 MH-DIF FPR 的实际膨胀程度。预测：校准 LD 后实际 FPR 膨胀 <3pp（从 nominal 5% 到 <8%），因为 LD 温和（mean Q3=0.009）且 MH 的 total-score stratification 部分吸收了 LD 效应。\\\", \\\"parent\\\": \\\"plan_013_q3_local_independence\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"n_subjects\\\": 8, \\\"n_permutations\\\": 1000, \\\"method\\\": \\\"permutation null + independence control, cross-subject matching\\\", \\\"ets_c_inflation\\\": {\\\"mean_pp\\\": 0.0004, \\\"max_pp\\\": 0.001, \\\"max_subject\\\": \\\"marketing\\\", \\\"verdict\\\": \\\"far below 3pp threshold\\\"}, \\\"p05_inflation\\\": {\\\"mean_pp\\\": -0.0019, \\\"direction\\\": \\\"slightly negative (no inflation)\\\", \\\"mean_fpr_with_ld\\\": 0.0412, \\\"mean_fpr_without_ld\\\": 0.0431}, \\\"subject_details\\\": {\\\"moral_scenarios\\\": {\\\"q3_pct\\\": 34.2, \\\"ets_c_delta_pp\\\": -1e-05}, \\\"human_aging\\\": {\\\"q3_pct\\\": 20.5, \\\"ets_c_delta_pp\\\": 0.0004}, \\\"world_religions\\\": {\\\"q3_pct\\\": 18.1, \\\"ets_c_delta_pp\\\": 0.0006}, \\\"marketing\\\": {\\\"q3_pct\\\": 17.5, \\\"ets_c_delta_pp\\\": 0.001}, \\\"professional_law\\\": {\\\"q3_pct\\\": 10.5, \\\"ets_c_delta_pp\\\": 0.0003}, \\\"college_medicine\\\": {\\\"q3_pct\\\": 4.6, \\\"ets_c_delta_pp\\\": 0.0005}}, \\\"q3_inflation_correlation\\\": {\\\"spearman_rho\\\": -0.238, \\\"p_value\\\": 0.57, \\\"significant\\\": false}, \\\"key_insight\\\": \\\"Cross-subject matching completely isolates within-subject LD from MH-DIF FPR\\\"}, \\\"notes\\\": \\\"LD inflation simulation 完成。核心发现：cross-subject matching 完全隔离了 within-subject LD 对 MH-DIF FPR 的影响。ETS-C 标准下 LD 膨胀仅 +0.0004pp（最大 +0.001pp），远低于 3pp 阈值。p<0.05 标准下甚至略为负（-0.0019pp，无膨胀）。即使 moral_scenarios 有 34.2% item pairs |Q3|>0.20，ETS-C 膨胀仍 <0.01pp。两个机制：(1) cross-subject matching 变量不含当前 subject items，LD 无法污染 matching；(2) ETS-C 的 |Δ|≥1.5 阈值本身极保守（actual FPR ~0.1%，远低于 nominal 5%）。Q3 与膨胀无显著相关（ρ=-0.24, p=0.57）。直接回应 Reviewer 对 LD violation 的担忧。\\\"}, \\\"plan_036_growing_pains_lookup\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-21T15:43:28.053Z\\\", \\\"updated_at\\\": \\\"2026-05-21T16:22:42.643Z\\\", \\\"hypothesis\\\": \\\"Growing Pains LLM benchmark paper 使用 FPC (Focal Point Contamination) anchor items 来检测污染。如果 FPC anchor item list 公开可得，与我们的 DIF C-flagged items 计算 Jaccard overlap 和 enrichment ratio。如果有显著 overlap (enrichment>2)，则 DIF 与 FPC 检测互补；如果无 overlap (enrichment≈1)，则证明 DIF 和 FPC 捕捉不同信号维度。\\\", \\\"parent\\\": \\\"plan_001_real_data_dif_mmlu\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"paper_found\\\": true, \\\"title\\\": \\\"Growing Pains: Extensible and Efficient LLM Benchmarking Via Fixed Parameter Calibration\\\", \\\"authors\\\": \\\"Habba et al.\\\", \\\"venue\\\": \\\"arXiv 2604.12843 (April 2026)\\\", \\\"fpc_meaning\\\": \\\"Fixed Parameter Calibration (NOT Focal Point Contamination)\\\", \\\"contamination_detection\\\": false, \\\"anchor_item_list_public\\\": false, \\\"overlap_analysis_possible\\\": false, \\\"relevance_to_our_work\\\": \\\"shared IRT foundation + contamination acknowledged as limitation\\\"}, \\\"notes\\\": \\\"Growing Pains (Habba et al., 2026) 的 FPC = Fixed Parameter Calibration，不是 Focal Point Contamination。论文用 IRT anchor items 做高效 benchmark 校准（100 anchor items per dataset, 395+ models, Spearman ρ≥0.9），不涉及污染检测。Anchor item IDs 动态计算、未公开持久化。无法执行 Jaccard overlap 分析。但论文在 Limitations 中承认 anchor items 可能随时间被污染，直接支持我们 DIF-based detection 的必要性论点。适合在 Related Work 中引用。\\\"}, \\\"plan_034_multi_subject_injection\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-21T15:43:12.118Z\\\", \\\"updated_at\\\": \\\"2026-05-21T16:02:54.334Z\\\", \\\"hypothesis\\\": \\\"Proposition 1 声称当污染局限于单一 subject 时 ΔFPR=0（cross-subject matching 不受污染）。当同时污染 k∈{1,2,3,5,10,20} 个 subject 时，matching variable 被逐步污染，ΔFPR(k) 将随 k 单调递增。具体预测：k≤3 时 ΔFPR<0.02（matching variable 被稀释），k≥10 时 ΔFPR>0.05（matching variable 严重受污）。ΔTPR(k) 在 k=1 与 k=20 之间保持稳定（>0.3 at p=0.5），因为 detection 对 target subject 内的 signal 而非 matching quality 更敏感。\\\", \\\"parent\\\": \\\"plan_016_within_subject_semi_synthetic\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"grid\\\": {\\\"k_values\\\": [1, 2, 3, 5, 10, 20], \\\"p_values\\\": [0.1, 0.3, 0.5], \\\"seeds_per_k\\\": 5, \\\"total_runs\\\": 90}, \\\"n_ref\\\": 1080, \\\"n_foc\\\": 807, \\\"n_foc_inject\\\": 787, \\\"proposition_1_boundary\\\": \\\"k≈5-10 subjects\\\", \\\"non_target_delta_fpr\\\": {\\\"k1_p05\\\": 0.002, \\\"k2_p05\\\": 0.002, \\\"k3_p05\\\": -0.001, \\\"k5_p05\\\": 0.007, \\\"k10_p03\\\": 0.026, \\\"k10_p05\\\": 0.069, \\\"k20_p03\\\": 0.072, \\\"k20_p05\\\": 0.167}, \\\"target_tpr\\\": {\\\"k1_p05\\\": 0.834, \\\"k5_p05\\\": 0.734, \\\"k10_p05\\\": 0.67, \\\"k20_p05\\\": 0.611}, \\\"key_findings\\\": {\\\"k_le_5_robust\\\": true, \\\"k_le_5_max_delta_fpr\\\": 0.007, \\\"k10_significant_at_p03\\\": true, \\\"k20_massive_inflation\\\": true, \\\"p01_robust_all_k\\\": true, \\\"tpr_dilution_with_k\\\": true, \\\"boundary_rule\\\": \\\"cross-subject DIF reliable when contaminated fraction <10%\\\"}}, \\\"notes\\\": \\\"Proposition 1 robustness boundary 实验完成。核心结论：cross-subject MH-DIF 在 k≤5 subjects (≤8.8%) 同时污染时 ΔFPR<0.007，Proposition 1 实际成立。k=10 (17.5%) 开始 p≥0.3 时 ΔFPR 显著（+0.026~+0.069）。k=20 (35.1%) 大规模膨胀（p=0.5 时 ΔFPR=+0.167）。低强度 p=0.1 在所有 k 值下都 robust。TPR 随 k 增大而下降（0.834→0.611 at p=0.5），因为 matching variable 吸收了部分 DIF 信号。实际意义：real-world 污染通常影响少数 subjects，cross-subject auditing 有足够 safety margin。\\\"}, \\\"plan_028_multi_bench_dif\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-21T10:45:20.123Z\\\", \\\"updated_at\\\": \\\"2026-05-21T14:04:56.321Z\\\", \\\"hypothesis\\\": \\\"Temporal DIF (2023 vs 2024 cohort) 在 METABENCH 的 ARC, HellaSwag, WinoGrande, TruthfulQA 上均展现与 MMLU 类似的显著 C% (>15%)，证明 temporal DIF 现象跨 benchmark 泛化，不是 MMLU 特有的 artifact。所有 benchmark 的 random-split control C% < 1%。\\\", \\\"parent\\\": \\\"plan_001_real_data_dif_mmlu\\\", \\\"metrics\\\": {\\\"mmlu\\\": {\\\"n_items\\\": 12508, \\\"n_ref\\\": 1080, \\\"n_foc\\\": 807, \\\"pct_c\\\": 31.3, \\\"random_pct_c\\\": 0.18, \\\"bootstrap_ci_95\\\": [29.38, 38.05], \\\"bootstrap_mean\\\": 33.14, \\\"bootstrap_sd\\\": 2.3, \\\"bootstrap_n\\\": 1000}, \\\"winogrande\\\": {\\\"n_items\\\": 1267, \\\"n_ref\\\": 1017, \\\"n_foc\\\": 803, \\\"pct_c\\\": 30.3, \\\"random_pct_c\\\": 0.32}, \\\"truthfulqa\\\": {\\\"n_items\\\": 817, \\\"n_ref\\\": 1080, \\\"n_foc\\\": 807, \\\"pct_c\\\": 29.7, \\\"random_pct_c\\\": 0.37}, \\\"arc\\\": {\\\"n_items\\\": 1172, \\\"n_ref\\\": 1080, \\\"n_foc\\\": 807, \\\"pct_c\\\": 26.9, \\\"random_pct_c\\\": 0.6}, \\\"gsm8k\\\": {\\\"n_items\\\": 1319, \\\"n_ref\\\": 1017, \\\"n_foc\\\": 804, \\\"pct_c\\\": 18.9, \\\"random_pct_c\\\": 0.3}, \\\"hellaswag\\\": {\\\"n_items\\\": 10042, \\\"n_ref\\\": 1080, \\\"n_foc\\\": 807, \\\"pct_c\\\": 17.9, \\\"random_pct_c\\\": 0.28}, \\\"cross_benchmark_range\\\": \\\"17.9-31.3%\\\", \\\"all_random_controls_below_1pct\\\": true, \\\"min_enrichment_ratio\\\": 45, \\\"n_benchmarks\\\": 6}, \\\"conclusion\\\": \\\"success\\\", \\\"notes\\\": \\\"All 6 METABENCH benchmarks show significant temporal DIF (17.9-31.3% ETS C), with all random controls <1%. Cross-benchmark consistency confirms temporal DIF is a universal phenomenon, not MMLU-specific. Knowledge/reasoning benchmarks (MMLU 31.3%, TruthfulQA 29.7%, ARC 26.9%, WinoGrande 30.3%) show higher C% than math/commonsense (GSM8K 18.9%, HellaSwag 17.9%). This directly addresses Dream #6 reviewer concern about single-benchmark generalizability. Worker failed 5× due to OOM on hellaswag.csv (2GB, 52M rows) — fixed with chunked loading.\\\"}, \\\"plan_032_dif_cleaned_mmlu\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-21T13:38:51.707Z\\\", \\\"updated_at\\\": \\\"2026-05-21T13:49:14.041Z\\\", \\\"hypothesis\\\": \\\"虽然 DIF-cleaned MMLU 的全局 rank correlation 很高 (ρ≈0.997)，但局部排名变化将揭示 DIF 的实际影响：特定模型家族（尤其是 2024 年新模型如 phi-3, llama-3）将在移除 C-flagged items 后排名显著下降，而 2023 年模型排名上升。这证明 DIF items 虽然不改变全局趋势，但系统性地偏向特定模型代际，构成 benchmark fairness 问题。\\\", \\\"parent\\\": \\\"plan_017_downstream_impact\\\", \\\"metrics\\\": {\\\"n_items_full\\\": 12508, \\\"n_items_cleaned\\\": 8590, \\\"n_items_removed\\\": 3918, \\\"pct_removed\\\": 31.3, \\\"spearman_rho\\\": 0.9965, \\\"rank_change_std\\\": 127.1, \\\"rank_change_min\\\": -589, \\\"rank_change_max\\\": 849, \\\"pct_change_ge5\\\": 89.5, \\\"pct_change_ge10\\\": 79.5, \\\"pct_change_ge20\\\": 66.4, \\\"pct_change_ge50\\\": 41.9, \\\"pct_change_ge100\\\": 24.8, \\\"top100_pct_ge10\\\": 18, \\\"top500_pct_ge10\\\": 47.2, \\\"cohort_2023_mean_change\\\": -22.56, \\\"cohort_2023_median_change\\\": -5, \\\"cohort_2024_mean_change\\\": 73.6, \\\"cohort_2024_median_change\\\": 11, \\\"systematic_bias\\\": \\\"DIF items favor 2024 models; cleaning hurts 2024 +73.6 avg, helps 2023 -22.6 avg\\\", \\\"top_hurt_families\\\": {\\\"phi-3\\\": 258.35, \\\"command-r\\\": 235, \\\"solar\\\": 149.15, \\\"llama-3\\\": 120.86}, \\\"top_benefit_families\\\": {\\\"mistral-0.1\\\": -60.32, \\\"mistral\\\": -53.27, \\\"zephyr\\\": -29.94, \\\"gemma-2\\\": -28.78}, \\\"removed_items_harder\\\": true, \\\"removed_mean_difficulty\\\": 0.409, \\\"cleaned_mean_difficulty\\\": 0.46, \\\"random_baseline_20trials\\\": {\\\"rank_change_std\\\": {\\\"mean\\\": 60.2, \\\"std\\\": 7.8}, \\\"mean_abs_rank_change\\\": {\\\"mean\\\": 36, \\\"std\\\": 3.6}, \\\"pct_change_ge100\\\": {\\\"mean\\\": 8.5, \\\"std\\\": 2}, \\\"cohort_2023_mean_change\\\": {\\\"mean\\\": 0.4, \\\"std\\\": 4.1}, \\\"cohort_2024_mean_change\\\": {\\\"mean\\\": 2.8, \\\"std\\\": 21.2}}, \\\"dif_vs_random_z_scores\\\": {\\\"rank_change_std_z\\\": 8.5, \\\"mean_abs_change_z\\\": 10.7, \\\"pct_ge100_z\\\": 8.2, \\\"cohort_2023_z\\\": -5.6, \\\"cohort_2024_z\\\": 3.3, \\\"cohort_asymmetry_gap_z\\\": 4.4}}, \\\"notes\\\": \\\"直接回应 Dream #7 \\\\\\\"ρ=0.997 is the paper's most damaging result\\\\\\\" 审稿意见。全局 ρ=0.9965 确实很高，但掩盖了剧烈的局部排名变化：89.5% 模型变化 ≥5 位，24.8% 变化 ≥100 位，最大变化 849 位。关键发现：系统性 cohort 偏差——2024 模型平均排名下降 73.6 位，2023 模型平均上升 22.6 位。Phi-3 下降 258 位, Llama-3 下降 121 位（DIF items 偏向这些新模型）。Mistral 系列上升 53 位。这证明 DIF 不仅是统计标记，更揭示了 benchmark 对不同模型代际的系统性偏差。\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"plan_033_subject_dif_concentration\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-21T13:41:16.628Z\\\", \\\"updated_at\\\": \\\"2026-05-21T13:42:06.450Z\\\", \\\"hypothesis\\\": \\\"DIF 在 MMLU 57 个 subject 间分布不均匀，且 STEM vs Humanities 存在系统性差异。控制 item difficulty 和 discrimination 后，特定 subject 的 content 本身预测 DIF 概率——这说明 DIF 不仅由 psychometric properties 驱动，还受知识领域内容特征影响。同时，DIF 的方向（favor 2023 vs 2024）可能在不同领域呈现不同模式。\\\", \\\"parent\\\": \\\"plan_001_real_data_dif_mmlu\\\", \\\"metrics\\\": {\\\"n_subjects\\\": 57, \\\"all_subjects_have_dif\\\": true, \\\"mean_pct_c\\\": 30.6, \\\"median_pct_c\\\": 29.7, \\\"sd_pct_c\\\": 5.5, \\\"range_pct_c\\\": [20.7, 48.4], \\\"top3_subjects\\\": {\\\"business_ethics\\\": 48.4, \\\"human_aging\\\": 41.9, \\\"formal_logic\\\": 40.4}, \\\"bottom3_subjects\\\": {\\\"computer_security\\\": 20.7, \\\"marketing\\\": 20.9, \\\"management\\\": 21.7}, \\\"domain_pct_c\\\": {\\\"STEM\\\": 30.9, \\\"Humanities\\\": 31.1, \\\"Social_Science\\\": 31.6}, \\\"stem_vs_humanities_p\\\": 0.611, \\\"kruskal_wallis_p\\\": 0.78, \\\"logistic_regression\\\": {\\\"difficulty_OR\\\": 0.086, \\\"discrimination_OR\\\": 57.2, \\\"pseudo_r2\\\": 0.042}, \\\"excess_dif_subjects\\\": [\\\"professional_law\\\", \\\"human_aging\\\", \\\"world_religions\\\", \\\"business_ethics\\\", \\\"professional_medicine\\\"], \\\"overall_pct_favor_2024\\\": 43.9, \\\"temporal_asymmetry\\\": {\\\"STEM_pct_favor_2024\\\": 55.4, \\\"Humanities_pct_favor_2024\\\": 35.6, \\\"Social_Science_pct_favor_2024\\\": 42}, \\\"unidirectional_subjects\\\": {\\\"world_religions\\\": {\\\"pct_favor_2024\\\": 16.9}, \\\"logical_fallacies\\\": {\\\"pct_favor_2024\\\": 20}}}, \\\"notes\\\": \\\"Hypothesis 部分验证：DIF rate 跨 domain 无显著差异 (STEM 30.9% vs Humanities 31.1%, p=0.61)，但 DIF direction 有强领域依赖——STEM 55.4% DIF items 偏向 2024 模型（能力提升），Humanities 仅 35.6%（64.4% 偏向 2023）。world_religions 和 logical_fallacies 呈近单向偏向 2023 (≥80%)。Logistic regression: discrimination OR=57.2, difficulty OR=0.086, 但 pseudo R²=0.042——item properties 仅解释 4% DIF variance，content 特征是主要驱动力。5 个 subject 控制 item props 后仍有 excess DIF (professional_law, human_aging, world_religions, business_ethics, professional_medicine)。\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"plan_031_temporal_granularity\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-21T12:46:39.820Z\\\", \\\"updated_at\\\": \\\"2026-05-21T12:49:28.194Z\\\", \\\"hypothesis\\\": \\\"如果 temporal DIF 随时间距离单调递增，则 half-year cohort (2023-H2 vs 2024-H1, 0.5yr) 的 C% 应显著低于 full-year (2023 vs 2024, 1.0yr) 的 C%。这检验 DIF 信号是否与 temporal distance 成正比，回应 Reviewer 对 binary temporal split 过于粗糙的批评。如果 half-year C% ≈ full-year C%，说明 DIF 信号在短至 6 个月的窗口内即已饱和。\\\", \\\"parent\\\": \\\"plan_001_real_data_dif_mmlu\\\", \\\"metrics\\\": {\\\"mmlu_full_year\\\": {\\\"comparison\\\": \\\"2023 vs 2024\\\", \\\"distance_yr\\\": 1, \\\"n_ref\\\": 1080, \\\"n_foc\\\": 807, \\\"pct_c\\\": 31.32, \\\"random_pct_c\\\": 0.02}, \\\"mmlu_half_year\\\": {\\\"comparison\\\": \\\"2023-H2 vs 2024-H1\\\", \\\"distance_yr\\\": 0.5, \\\"n_ref\\\": 1018, \\\"n_foc\\\": 807, \\\"pct_c\\\": 34.35, \\\"random_pct_c\\\": 0.19}, \\\"mmlu_within_2023\\\": {\\\"comparison\\\": \\\"2023-H1 vs 2023-H2\\\", \\\"distance_yr\\\": 0.5, \\\"n_ref\\\": 62, \\\"n_foc\\\": 1018, \\\"pct_c\\\": 22.62, \\\"random_pct_c\\\": 0.18, \\\"supplementary\\\": true}, \\\"cross_bench_half_year\\\": {\\\"arc_pct_c\\\": 29.27, \\\"hellaswag_pct_c\\\": 18.07, \\\"winogrande_pct_c\\\": 33.62, \\\"truthfulqa_pct_c\\\": 31.33}, \\\"cross_bench_full_year\\\": {\\\"arc_pct_c\\\": 26.88, \\\"hellaswag_pct_c\\\": 17.89, \\\"winogrande_pct_c\\\": 30.31, \\\"truthfulqa_pct_c\\\": 29.74}, \\\"half_year_gt_full_year_all_benchmarks\\\": true, \\\"dif_saturates_within_6mo\\\": true}, \\\"notes\\\": \\\"Reviewer 评定 partial success：MMLU 半年有效（34.35% vs 0.19%, 181× enrichment），但 cross-benchmark 半年 enrichment 不均——HellaSwag 仅 3.5× (18.07%/5.23%)，其余 ARC 12.2×, WinoGrande 12.2×, TruthfulQA 51.4×。DIF 在 6 个月内即饱和，cohort purity > temporal distance。2023-H1 vs 2023-H2 (supplementary, N=62 < 80): C%=22.62%。\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"plan_030_odds_ratio\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-21T10:17:26.316Z\\\", \\\"updated_at\\\": \\\"2026-05-21T10:18:26.271Z\\\", \\\"hypothesis\\\": \\\"Logistic regression 的 odds ratio + CI 量化 accuracy change 与 DIF C flag 的关联强度。Item-level accuracy change (Model 3) 比 domain-level delta (Model 1) 提供更精确的预测。控制 item properties (difficulty + discrimination) 后，accuracy change 的 OR 反转（Simpson's paradox），说明 DIF C 主要由 item 固有属性驱动而非 accuracy shift。\\\", \\\"parent\\\": \\\"plan_001_real_data_dif_mmlu\\\", \\\"metrics\\\": {\\\"model1_domain_delta\\\": {\\\"mcfadden_r2\\\": 0.0007, \\\"nagelkerke_r2\\\": 0.0012, \\\"aic\\\": 15545.2, \\\"subject_acc_delta_or\\\": 80.86, \\\"subject_acc_delta_or_per_010\\\": 1.55, \\\"subject_acc_delta_or_ci_per_010\\\": [1.19, 2.03]}, \\\"model2_domain_delta_plus_items\\\": {\\\"mcfadden_r2\\\": 0.0423, \\\"nagelkerke_r2\\\": 0.072, \\\"aic\\\": 14902.3, \\\"subject_acc_delta_or_per_010\\\": 0.73, \\\"ctt_difficulty_or_per_010\\\": 0.78, \\\"ctt_discrimination_or_per_010\\\": 1.51}, \\\"model3_item_delta\\\": {\\\"mcfadden_r2\\\": 0.0012, \\\"nagelkerke_r2\\\": 0.0021, \\\"aic\\\": 15536.9, \\\"item_acc_change_or\\\": 2.11, \\\"item_acc_change_or_per_010\\\": 1.08, \\\"item_acc_change_ci\\\": [1.51, 2.96]}, \\\"model4_item_delta_plus_items\\\": {\\\"mcfadden_r2\\\": 0.0434, \\\"nagelkerke_r2\\\": 0.0737, \\\"aic\\\": 14885.4, \\\"item_acc_change_or_per_010\\\": 0.92, \\\"ctt_difficulty_or_per_010\\\": 0.77, \\\"ctt_discrimination_or_per_010\\\": 1.54}, \\\"simpsons_paradox\\\": true, \\\"lr_test_m1_vs_m2_chi2\\\": 646.98, \\\"lr_test_m3_vs_m4_chi2\\\": 655.53, \\\"best_model\\\": \\\"Model 4 (item Δ + item props)\\\"}, \\\"conclusion\\\": \\\"success\\\"}, \\\"plan_027_temporal_overlap\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-21T08:34:47.232Z\\\", \\\"updated_at\\\": \\\"2026-05-21T08:38:52.937Z\\\", \\\"hypothesis\\\": \\\"Temporal cohort ability gap 很小 (d=-0.17)，ability-matched C% 接近 full 31.3%，确认 temporal DIF 非 ability confound 产物\\\", \\\"parent\\\": \\\"plan_001_real_data_dif_mmlu\\\", \\\"metrics\\\": {\\\"cohort_2023_n\\\": 1080, \\\"cohort_2023_mean\\\": 0.5814, \\\"cohort_2023_sd\\\": 0.1405, \\\"cohort_2024_n\\\": 807, \\\"cohort_2024_mean\\\": 0.6068, \\\"cohort_2024_sd\\\": 0.1556, \\\"cohens_d\\\": -0.173, \\\"overlap_coefficient\\\": 0.764, \\\"bhattacharyya\\\": 0.961, \\\"full_c_pct\\\": 31.3, \\\"score_range_overlap_c_pct\\\": 30.9, \\\"nn_matched_c_pct_mean\\\": 28.9, \\\"nn_matched_c_pct_sd\\\": 0.1, \\\"nn_matched_n_per_group\\\": 638, \\\"nn_matched_d\\\": -0.01, \\\"ability_confound_pp\\\": 2.4, \\\"ability_confound_pct_of_total\\\": 7.7, \\\"llama_comparison_d\\\": -0.99, \\\"llama_comparison_overlap\\\": 0.18, \\\"llama_matched_c_pct\\\": 28.3}, \\\"conclusion\\\": \\\"success\\\"}, \\\"plan_004_gsm8k_cross_benchmark\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-21T00:30:09.372Z\\\", \\\"updated_at\\\": \\\"2026-05-21T01:22:16.029Z\\\", \\\"hypothesis\\\": \\\"GSM8K 的 temporal DIF (2023 vs 2024) 将展示与 MMLU 类似的 30-40% ETS C%，证明 temporal DIF 现象跨 benchmark 泛化。使用 METABENCH 其他 benchmarks 总分做 external matching（GSM8K 无 subject 分层），预期 baseline FPR 更可控。如果 C% 在同一量级 → DIF 作为 benchmark health diagnostic 的泛化性得到验证。\\\", \\\"parent\\\": \\\"plan_001_real_data_dif_mmlu\\\", \\\"metrics\\\": {\\\"step1_gsm8k_temporal_dif\\\": {\\\"n_items\\\": 1319, \\\"n_ref\\\": 1017, \\\"n_foc\\\": 804, \\\"standard_c_pct\\\": 18.9, \\\"external_c_pct\\\": 47.4, \\\"sanity_c_pct\\\": 0.3, \\\"standard_external_spearman\\\": 0.926}, \\\"step2_semi_synthetic\\\": {\\\"standard_delta_tpr_p10\\\": 0.818, \\\"external_delta_tpr_p10\\\": 0.517}, \\\"step3_gsm1k_correlation\\\": {\\\"n_models\\\": 33, \\\"n_dif_c_items\\\": 249, \\\"pearson_r\\\": -0.478, \\\"pearson_p\\\": 0.005, \\\"spearman_rho\\\": -0.403, \\\"spearman_p\\\": 0.02, \\\"partial_r_controlling_accuracy\\\": -0.385, \\\"partial_p\\\": 0.027, \\\"permutation_p\\\": 0.014, \\\"dif_c_favor_2024\\\": 78, \\\"dif_c_favor_2023\\\": 171, \\\"direction\\\": \\\"NEGATIVE (opposite to contamination hypothesis)\\\", \\\"cook_d_max_model\\\": \\\"Deepseek-math-7b-rl\\\", \\\"leave_one_out_r_range\\\": \\\"-0.537 to -0.374\\\", \\\"robust\\\": true}}, \\\"notes\\\": \\\"Step 3 GSM1K correlation: r=-0.478 (p=0.005). |r|>0.3 threshold met but direction NEGATIVE — opposite to contamination hypothesis. DIF-C items disadvantage contaminated models, not advantage them. 171/249 DIF-C items favor older models. Partial r=-0.385 (p=0.027) controlling for overall accuracy. Permutation p=0.014. Robust to leave-one-out. Interpretation: DIF captures genuine measurement anomalies orthogonal to contamination. Contamination produces narrow boost on typical items, fails on atypical-difficulty items (DIF-C). Supports characterization narrative: DIF as benchmark health diagnostic, not contamination detector.\\\", \\\"conclusion\\\": \\\"negative\\\"}, \\\"plan_017_downstream_impact\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-20T23:44:12.194Z\\\", \\\"updated_at\\\": \\\"2026-05-21T00:05:41.991Z\\\", \\\"hypothesis\\\": \\\"移除 temporal DIF-flagged items (ETS C, ~31% of MMLU items) 后，模型跨代排名更稳定（Spearman ρ 提升），且稳定性提升显著优于随机移除相同数量 items 的 baseline。这证明 DIF 不只标记 noise，而是精确识别了 problematic items，为 DIF 作为 benchmark quality tool 提供 downstream evidence。\\\", \\\"parent\\\": \\\"plan_001_real_data_dif_mmlu\\\", \\\"metrics\\\": {\\\"n_dif_items\\\": 3918, \\\"n_stable_items\\\": 8590, \\\"dif_pct\\\": 31.3, \\\"rho_full_vs_stable_2023\\\": 0.998851, \\\"rho_full_vs_stable_2024\\\": 0.997014, \\\"rho_full_vs_stable_all\\\": 0.996451, \\\"shr_full\\\": 0.9934, \\\"shr_stable\\\": 0.9919, \\\"dif_vs_random_z_mean\\\": -14.91, \\\"dif_vs_random_all_21_conditions_significant\\\": true, \\\"dif_removal_MORE_disruptive_than_random\\\": true, \\\"cross_cohort_ratio_dif_vs_full\\\": 1.0919, \\\"cross_cohort_ratio_stable_vs_full\\\": 0.9581, \\\"top_beneficiaries\\\": \\\"phi-3, llama-3 derivatives\\\", \\\"top_hurt\\\": \\\"mistral merges, slerp models\\\", \\\"max_rank_change\\\": 851}, \\\"conclusion\\\": \\\"negative\\\", \\\"notes\\\": \\\"Hypothesis REJECTED but finding is richer. DIF removal causes MORE ranking disruption than random (z=-8 to -49σ, 21/21 conditions). DIF items are NOT noise — they carry concentrated differential information that systematically discriminates models. Key insight: DIF items capture temporal instability (1.09× cross-cohort accuracy swing vs 0.96× stable items). Rankings are very robust (ρ>0.996 even at 38% removal). Top beneficiaries of DIF items: phi-3 and llama-3 derivatives (+700-850 ranks). Top hurt: mistral merges/slerp models (-400 to -587 ranks). Paper narrative shift: DIF items are not \\\\\\\"bad items to remove\\\\\\\" but \\\\\\\"items that reveal differential model capabilities across generations\\\\\\\" — supports characterization narrative over cleaning narrative.\\\"}, \\\"plan_016_within_subject_semi_synthetic\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-20T22:30:50.476Z\\\", \\\"updated_at\\\": \\\"2026-05-20T22:49:02.342Z\\\", \\\"hypothesis\\\": \\\"在 subject 内部使用 within-subject total score 做 MH 分层的 semi-synthetic injection 中，DIF 仍能检测差异性污染（ΔTPR > 0.3 at p=0.5）。这证明 DIF 方法在 subject 级别也有效，plan_014 的 38% within-subject C% 反映的是真实代际能力差异而非方法失败。\\\", \\\"parent\\\": \\\"plan_014_within_subject_dif\\\", \\\"metrics\\\": {\\\"within_matching\\\": {\\\"subjects_passing_p05\\\": \\\"3/5 (human_aging, professional_medicine, formal_logic)\\\", \\\"business_ethics_baseline_fpr\\\": 0.563, \\\"business_ethics_delta_tpr_p05\\\": -0.078, \\\"human_aging_baseline_fpr\\\": 0.334, \\\"human_aging_delta_tpr_p05\\\": 0.385, \\\"professional_medicine_baseline_fpr\\\": 0.312, \\\"professional_medicine_delta_tpr_p05\\\": 0.327, \\\"formal_logic_baseline_fpr\\\": 0.409, \\\"formal_logic_delta_tpr_p05\\\": 0.457, \\\"high_school_statistics_baseline_fpr\\\": 0.407, \\\"high_school_statistics_delta_tpr_p05\\\": 0.194, \\\"fpr_inflates_with_injection\\\": true, \\\"avg_fpr_inflation_p10\\\": 0.186}, \\\"cross_matching\\\": {\\\"subjects_passing_p05\\\": \\\"4/5 (human_aging, professional_medicine, formal_logic, high_school_statistics)\\\", \\\"business_ethics_baseline_fpr\\\": 0.533, \\\"business_ethics_delta_tpr_p05\\\": 0.056, \\\"human_aging_baseline_fpr\\\": 0.431, \\\"human_aging_delta_tpr_p05\\\": 0.375, \\\"professional_medicine_baseline_fpr\\\": 0.38, \\\"professional_medicine_delta_tpr_p05\\\": 0.38, \\\"formal_logic_baseline_fpr\\\": 0.402, \\\"formal_logic_delta_tpr_p05\\\": 0.543, \\\"high_school_statistics_baseline_fpr\\\": 0.335, \\\"high_school_statistics_delta_tpr_p05\\\": 0.433, \\\"fpr_stable_across_injection\\\": true, \\\"delta_fpr_all_subjects\\\": 0}, \\\"success_criterion_met\\\": true}, \\\"conclusion\\\": \\\"success\\\", \\\"notes\\\": \\\"Revised per Director review. (1) Fixed comparison table FPR (0.048→0.314). (2) Added cross-subject matching: FPR completely stable (ΔFPR=0.000 all 5 subjects), better detection (4/5 ΔTPR>0.3 vs within 3/5). Within-subject FPR inflates +0.067 to +0.281 at p=1.0 due to matching variable contamination. (3) Added formal_logic (109 items, ΔTPR=+0.543 cross) and high_school_statistics (181 items, ΔTPR=+0.433 cross). Both 5 strata, clean detection. Cross-subject matching confirms plan_011's external MH finding at subject level.\\\"}, \\\"plan_013_q3_local_independence\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-20T21:58:11.134Z\\\", \\\"updated_at\\\": \\\"2026-05-20T22:36:16.364Z\\\", \\\"hypothesis\\\": \\\"MMLU 同一 subject 内的 items 存在显著局部依赖性（within-subject Q3 均值 > 0.20，显著高于 cross-subject Q3），这违反 2PL IRT 和 MH-DIF 的局部独立性假设，部分解释了 plan_011 中 temporal cohort baseline FPR=31% 的膨胀。如果确认，则动机化后续 bifactor/testlet 模型改进。\\\", \\\"parent\\\": \\\"plan_011_semi_synthetic_validation\\\", \\\"metrics\\\": {\\\"within_subject_mean_q3\\\": 0.0086, \\\"cross_subject_mean_q3\\\": 0.0031, \\\"within_subject_pct_above_020\\\": 11.3, \\\"cross_subject_pct_above_020\\\": 2.2, \\\"mann_whitney_p\\\": 2.29e-09, \\\"worst_subject\\\": \\\"moral_scenarios\\\", \\\"worst_subject_pct_above_020\\\": 34.2, \\\"n_items_retained\\\": 12251, \\\"n_items_filtered\\\": 257, \\\"subject_size_q3_corr\\\": 0.2064, \\\"subject_size_q3_p\\\": 0.123}, \\\"conclusion\\\": \\\"success\\\", \\\"notes\\\": \\\"Q3 诊断完成。Hypothesis 部分验证：within-subject 均值 Q3=0.0086（低于 0.20 阈值），但尾部显著——11.3% within-subject pairs |Q3|>0.20 vs 2.2% cross-subject（5x, Mann-Whitney p=2.3e-9）。局部依赖存在但温和，不太可能单独解释 31% FPR。最严重 subjects: moral_scenarios 34.2%, world_religions 18%, marketing 17.5%。结论：局部依赖是 FPR 的贡献因素之一，但主要 FPR 来源是 genuine temporal DIF（plan_014 确认 within-subject C%=38%）。\\\"}, \\\"plan_015_bifactor_irt\\\": {\\\"status\\\": \\\"PREPARING\\\", \\\"created_at\\\": \\\"2026-05-20T22:23:51.598Z\\\", \\\"updated_at\\\": \\\"2026-05-20T22:30:44.925Z\\\", \\\"hypothesis\\\": \\\"Bifactor IRT（1 general + 57 subject-specific factors）的 general θ 分层能将 temporal cohort baseline FPR 从 31% 降至 <15%，同时在 semi-synthetic 框架下保持 TPR>0.60 at p=0.5。Bifactor 通过分离学科特异性能力和通用能力，消除 subject-level 能力差异对 MH-DIF 的混淆。\\\", \\\"parent\\\": \\\"plan_012_irt_theta_conditioning\\\", \\\"conclusion\\\": \\\"killed\\\", \\\"notes\\\": \\\"D010: Director 取消。plan_014 前置检查结果 within-subject C%=38.1% (>25%)，证明 temporal DIF 渗透到 subject 内部，bifactor 无法解决。Between-subject variance 反而在压低 overall C%。\\\"}, \\\"plan_014_within_subject_dif\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-20T22:23:50.857Z\\\", \\\"updated_at\\\": \\\"2026-05-20T22:28:27.350Z\\\", \\\"hypothesis\\\": \\\"Within-subject temporal DIF（只用该 subject 内 items 和总分）在高 C% subjects 上的 C% 将 < 15%，表明 plan_001 的 31% FPR 主要来自 between-subject 能力差异而非 within-subject 因素。如果 within-subject C% > 25%，则 bifactor 模型也无法解决 FPR 问题。\\\", \\\"parent\\\": \\\"plan_012_irt_theta_conditioning\\\", \\\"metrics\\\": {\\\"business_ethics_within_c_pct\\\": 45.2, \\\"human_aging_within_c_pct\\\": 33, \\\"formal_logic_within_c_pct\\\": 39.5, \\\"professional_medicine_within_c_pct\\\": 31.1, \\\"high_school_statistics_within_c_pct\\\": 42, \\\"avg_within_subject_c_pct\\\": 38.1, \\\"avg_cross_subject_c_pct\\\": 40.5, \\\"avg_delta_within_vs_cross\\\": -2.4, \\\"sibtest_available\\\": false, \\\"r_available\\\": false, \\\"decision_zone\\\": \\\">25% HIGH\\\"}, \\\"conclusion\\\": \\\"negative\\\", \\\"notes\\\": \\\"Within-subject temporal DIF 前置检查 NEGATIVE。5 个高 C% subjects 平均 within-subject C%=38.1%（全部 >25%）：business_ethics 45.2%, human_aging 33.0%, formal_logic 39.5%, professional_medicine 31.1%, high_school_statistics 42.0%。Cross-subject matching C% 40.5%（Δ=-2.4pp）。结论：temporal DIF 渗透到每个 subject 内部，不是 between-subject 能力差异的伪影。Bifactor 模型大概率无法解决 FPR 问题。SIBTEST: R 不可用，Python 无实现。\\\"}, \\\"plan_012_irt_theta_conditioning\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-20T21:58:10.439Z\\\", \\\"updated_at\\\": \\\"2026-05-20T22:20:01.371Z\\\", \\\"hypothesis\\\": \\\"用 2PL IRT 估计的 θ 值（10-20 等距层）替代粗糙总分作为 MH 分层变量后，semi-synthetic 框架下 baseline FPR 将从 ~31%（temporal）/~49%（ability）降至 <10%，同时保持 TPR>0.70 at p=0.5。θ-conditioning 通过更精确的能力匹配消除 impact-vs-DIF 混淆残留。\\\", \\\"parent\\\": \\\"plan_011_semi_synthetic_validation\\\", \\\"metrics\\\": {\\\"temporal_theta_qt20_fpr\\\": 0.312, \\\"temporal_theta_qt20_tpr_p05\\\": 0.876, \\\"temporal_theta_qt20_tpr_p10\\\": 1, \\\"temporal_external5_fpr\\\": 0.314, \\\"temporal_external5_tpr_p05\\\": 0.834, \\\"ability_theta_qt10_fpr\\\": 0.093, \\\"ability_theta_qt10_tpr_p05\\\": 0.206, \\\"ability_theta_qt10_tpr_p10\\\": 0.544, \\\"ability_theta_qt20_fpr\\\": 0.079, \\\"ability_theta_qt20_tpr_p05\\\": 0.21, \\\"ability_theta_qt20_tpr_p10\\\": 0.544, \\\"ability_external5_fpr\\\": 0.493, \\\"ability_external5_tpr_p05\\\": 0.756, \\\"theta_total_score_corr\\\": 0.9986, \\\"enrichment_all_variants\\\": \\\"0.97-1.00\\\", \\\"success_criterion_met\\\": false}, \\\"conclusion\\\": \\\"negative\\\", \\\"notes\\\": \\\"θ-conditioning NEGATIVE. Temporal cohort: logit(p) θ corr=0.9986 with total score, all θ variants FPR=31-35% (no improvement over plan_011 external_5 FPR=31.4%). TPR well maintained (0.83-0.88 at p=0.5). Ability cohort: quantile θ bins (qt_10/qt_20) reduce FPR from 49% to 8-9%, but TPR collapses from 76% to 21% at p=0.5 — proving plan_011 ability cohort's high TPR was mainly ability confounding, not genuine DIF detection. Enrichment vs Li et al.: all variants 0.97-1.00 (unchanged from plan_001). Key conclusion: temporal cohort 31% baseline FPR is genuine DIF (real item-level differences between 2023 vs 2024 models), not an artifact of imprecise ability matching. Improving θ estimation won't fix it — need multidimensional or subject-level approaches.\\\"}, \\\"plan_011_semi_synthetic_validation\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-20T21:35:55.290Z\\\", \\\"updated_at\\\": \\\"2026-05-20T21:54:54.659Z\\\", \\\"hypothesis\\\": \\\"在 METABENCH 真实响应矩阵上注入已知差异性污染（focal group 指定 items 的 incorrect→correct 翻转）后，MH-DIF 的 ETS C 分类能在 ability-quintile cohort 上达到 TPR>0.5 (p=1.0) 且 FPR<0.05。如果成功，说明 plan_001/001b 的 enrichment≈1.0 是 Li et al. ground truth 不匹配（全局性 vs 差异性污染），而非 DIF 方法本身失败。\\\", \\\"parent\\\": \\\"plan_001b_matched_ability_dif\\\", \\\"metrics\\\": {\\\"temporal_external_tpr_p0\\\": 0.326, \\\"temporal_external_tpr_p03\\\": 0.548, \\\"temporal_external_tpr_p05\\\": 0.834, \\\"temporal_external_tpr_p07\\\": 0.99, \\\"temporal_external_tpr_p10\\\": 1, \\\"temporal_external_fpr\\\": 0.314, \\\"temporal_external_delta_tpr_p10\\\": 0.674, \\\"ability_external_tpr_p0\\\": 0.498, \\\"ability_external_tpr_p10\\\": 0.8, \\\"ability_external_fpr\\\": 0.493, \\\"ability_external_delta_tpr_p10\\\": 0.302, \\\"standard_mh_fpr_inflation\\\": \\\"temporal 0.298→0.616 at p=1.0\\\", \\\"matching_variable_contamination_confirmed\\\": true, \\\"bug_fix\\\": \\\"inf-delta classified as extreme DIF not class A\\\"}, \\\"conclusion\\\": \\\"success\\\", \\\"notes\\\": \\\"MH-DIF successfully detects injected differential contamination. Temporal+external: ΔTPR=+0.674 (0.326→1.000), FPR constant at 0.314. Clear dose-response across p={0.3,0.5,0.7,1.0}. Confirms plan_001/001b enrichment≈1.0 is ground truth mismatch (Li et al. = global contamination, DIF = differential contamination), NOT DIF method failure. Also discovered: (1) matching variable contamination when 20% items injected (standard MH FPR inflates 0.298→0.616, anchor/external variants immune), (2) inf-delta classification bug in plan_001 code fixed. Ability cohort has high baseline FPR (~49%) due to extreme Q1-2 vs Q4-5 ability gap — 5-strata insufficient.\\\"}, \\\"plan_001b_matched_ability_dif\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-20T21:35:08.552Z\\\", \\\"updated_at\\\": \\\"2026-05-20T21:35:51.089Z\\\", \\\"hypothesis\\\": \\\"在每个 accuracy quintile 内部做 temporal cohort MH-DIF（控制能力后），enrichment 将从 plan_001 的 0.96 提升到 >1.5，证明能力匹配能隔离出污染信号。\\\", \\\"parent\\\": \\\"plan_001_real_data_dif_mmlu\\\", \\\"conclusion\\\": \\\"negative\\\", \\\"notes\\\": \\\"D005: Matched-ability DIF 失败。所有 quintile enrichment 0.94-1.04。能力匹配未能隔离出污染信号。Reviewer 洞察：Li et al. web-overlap 是全局性污染标注（Common Crawl 对所有模型可用），不会产生 group-specific DIF。enrichment≈1.0 可能不是 DIF 方法失败，而是 ground truth 与 DIF 度量的东西根本不同——DIF 检测差异性训练数据包含，Li 检测存在性污染。\\\"}, \\\"plan_001_real_data_dif_mmlu\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-20T20:54:53.883Z\\\", \\\"updated_at\\\": \\\"2026-05-20T21:12:05.153Z\\\", \\\"hypothesis\\\": \\\"MH-DIF 在 METABENCH 真实 MMLU 数据（5227 模型 × 12508 items）上，用时间 cohort (2023 vs 2024) 和能力分位 cohort 分组时，ETS C 标记的 items 在 Li et al. clean items 中的 FPR ≤ 0.05，且 ETS C 标记在 contaminated items 中的比例显著高于 clean items。这验证 DIF 在真实数据上不会产生过多假阳性，且能捕捉到与 web-overlap 污染信号一致的差异性。\\\", \\\"parent\\\": \\\"mvp_dif_power_sim_phase2\\\", \\\"metrics\\\": {\\\"temporal_ets_c_pct\\\": 31.3, \\\"temporal_fpr_li_clean\\\": 0.318, \\\"temporal_enrichment\\\": 0.96, \\\"ability_ets_c_pct\\\": 2.9, \\\"ability_fpr_li_clean\\\": 0.027, \\\"ability_enrichment\\\": 1.19, \\\"within_family_llama2v3_c_pct\\\": 61.3, \\\"within_family_mistral_mixtral_c_pct\\\": 38.7, \\\"domain_spearman_rho\\\": 0.307, \\\"domain_spearman_p\\\": 0.02, \\\"sanity_random_split_c_pct\\\": 0.18, \\\"temporal_ability_jaccard\\\": 0.014}, \\\"conclusion\\\": \\\"negative\\\", \\\"notes\\\": \\\"Temporal cohort DIF (2023 vs 2024): 31.3% ETS C, enrichment=0.96 — DIF detects systematic capability improvement, NOT contamination (clean and contaminated items flagged at equal rates). Ability cohort: 2.9% C, enrichment=1.19 — weak positive signal, FPR=2.7% well controlled. Within-family (Llama-2 vs 3): 61.3% C confirms ability confound dominates. Domain ρ=0.307 (p=0.02) consistent with capability-driven DIF. Sanity check passed (random split 0.18% C). Core finding: naive MH-DIF cannot distinguish contamination from genuine capability improvement without ability matching or IRT equating.\\\"}, \\\"mvp_dif_power_sim_phase2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-20T18:52:34.145Z\\\", \\\"updated_at\\\": \\\"2026-05-20T19:30:16.477Z\\\", \\\"hypothesis\\\": \\\"ETS C 分类在 METABENCH 真实 MMLU 2PL IRT 参数（非理想化分布）下，仍能在 N≥80/group、δ≥1.4 时达到 TPR≥0.65、FPR≤0.10。Phase 1 用合成参数（a~LogNormal, b~N(0,1)）条件性通过，需验证真实参数分布（可能有偏态、聚集、极端值）不会降解检测功效。\\\", \\\"parent\\\": \\\"mvp_dif_power_sim\\\", \\\"metrics\\\": {\\\"ets_c_tpr_N80_d14\\\": 0.6823, \\\"ets_c_tpr_N80_d16\\\": 0.7223, \\\"ets_c_tpr_N100_d14\\\": 0.7582, \\\"ets_c_tpr_N100_d16\\\": 0.7966, \\\"ets_c_fpr_range\\\": \\\"0.036-0.042\\\", \\\"best_auc_mh\\\": 0.9254, \\\"best_auc_lr\\\": 0.9405, \\\"verdict\\\": \\\"PASS\\\", \\\"pass_plus_met\\\": true, \\\"real_param_a_mean\\\": 1.2, \\\"real_param_b_mean\\\": -0.84}, \\\"conclusion\\\": \\\"success\\\"}, \\\"mvp_dif_power_sim\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-20T17:16:29.354Z\\\", \\\"updated_at\\\": \\\"2026-05-20T18:52:23.378Z\\\", \\\"hypothesis\\\": \\\"DIF 跨模型批次分析（MH + Logistic Regression）在 N=50-80/group、污染效应量 δ≥1.0 logits 时，对 10% 污染 items 的检测功效 TPR≥0.70 且 FPR≤0.10。这是整个 pipeline 的前提假设——若 DIF 在理想合成数据上都 underpowered，则后续真实数据方案不成立。\\\", \\\"metrics\\\": {\\\"best_tpr_mh\\\": 0.6817, \\\"best_tpr_lr\\\": 0.6869, \\\"best_condition\\\": \\\"N=100_delta=1.6\\\", \\\"best_auc_mh\\\": 0.9393, \\\"best_auc_lr\\\": 0.9593, \\\"pass_criterion_tpr_mh\\\": 0.0416, \\\"pass_criterion_tpr_lr\\\": 0.0703, \\\"pass_criterion_condition\\\": \\\"N=50_delta=1.0\\\", \\\"verdict\\\": \\\"FAIL\\\", \\\"all_fpr_below_015\\\": true}, \\\"conclusion\\\": \\\"success\\\", \\\"notes\\\": \\\"Conditional pass (D001): ETS C classification as primary detector. ETS C TPR=0.72-0.85 at N≥80,δ≥1.4; FPR well controlled. BH-corrected p-value based detection failed (TPR 0.04-0.07 at pass criterion). Raw power also insufficient for p-value approach. AUC discriminability good (0.91-0.96). Decision: pivot to ETS C magnitude-based detection, Phase 2 validates with real IRT parameters.\\\"}}, \\\"count\\\": 21, \\\"total\\\": 21, \\\"baseline\\\": null}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.0839}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {\"plan_035_q3_inflation_sim\": {\"status\": \"DONE\", \"created_at\": \"2026-05-21T15:43:20.736Z\", \"updated_at\": \"2026-05-21T16:24:02.388Z\", \"hypothesis\": \"plan_013 发现 11.3% within-subject item pairs |Q3|>0.20，存在局部依赖(LD)。MH-DIF 假设局部独立，LD 可能膨胀 Type I error。通过 Monte Carlo 模拟或 within-subject permutation null（保持 Q3 结构），量化 LD 对 MH-DIF FPR 的实际膨胀程度。预测：校准 LD 后实际 FPR 膨胀 <3pp（从 nominal 5% 到 <8%），因为 LD 温和（mean Q3=0.009）且 MH 的 total-score stratification 部分吸收了 LD 效应。\", \"parent\": \"plan_013_q3_local_independence\", \"conclusion\": \"success\", \"metrics\": {\"n_subjects\": 8, \"n_permutations\": 1000, \"method\": \"permutation null + independence control, cross-subject matching\", \"ets_c_inflation\": {\"mean_pp\": 0.0004, \"max_pp\": 0.001, \"max_subject\": \"marketing\", \"verdict\": \"far below 3pp threshold\"}, \"p05_inflation\": {\"mean_pp\": -0.0019, \"direction\": \"slightly negative (no inflation)\", \"mean_fpr_with_ld\": 0.0412, \"mean_fpr_without_ld\": 0.0431}, \"subject_details\": {\"moral_scenarios\": {\"q3_pct\": 34.2, \"ets_c_delta_pp\": -1e-05}, \"human_aging\": {\"q3_pct\": 20.5, \"ets_c_delta_pp\": 0.0004}, \"world_religions\": {\"q3_pct\": 18.1, \"ets_c_delta_pp\": 0.0006}, \"marketing\": {\"q3_pct\": 17.5, \"ets_c_delta_pp\": 0.001}, \"professional_law\": {\"q3_pct\": 10.5, \"ets_c_delta_pp\": 0.0003}, \"college_medicine\": {\"q3_pct\": 4.6, \"ets_c_delta_pp\": 0.0005}}, \"q3_inflation_correlation\": {\"spearman_rho\": -0.238, \"p_value\": 0.57, \"significant\": false}, \"key_insight\": \"Cross-subject matching completely isolates within-subject LD from MH-DIF FPR\"}, \"notes\": \"LD inflation simulation 完成。核心发现：cross-subject matching 完全隔离了 within-subject LD 对 MH-DIF FPR 的影响。ETS-C 标准下 LD 膨胀仅 +0.0004pp（最大 +0.001pp），远低于 3pp 阈值。p<0.05 标准下甚至略为负（-0.0019pp，无膨胀）。即使 moral_scenarios 有 34.2% item pairs |Q3|>0.20，ETS-C 膨胀仍 <0.01pp。两个机制：(1) cross-subject matching 变量不含当前 subject items，LD 无法污染 matching；(2) ETS-C 的 |Δ|≥1.5 阈值本身极保守（actual FPR ~0.1%，远低于 nominal 5%）。Q3 与膨胀无显著相关（ρ=-0.24, p=0.57）。直接回应 Reviewer 对 LD violation 的担忧。\"}, \"plan_036_growing_pains_lookup\": {\"status\": \"DONE\", \"created_at\": \"2026-05-21T15:43:28.053Z\", \"updated_at\": \"2026-05-21T16:22:42.643Z\", \"hypothesis\": \"Growing Pains LLM benchmark paper 使用 FPC (Focal Point Contamination) anchor items 来检测污染。如果 FPC anchor item list 公开可得，与我们的 DIF C-flagged items 计算 Jaccard overlap 和 enrichment ratio。如果有显著 overlap (enrichment>2)，则 DIF 与 FPC 检测互补；如果无 overlap (enrichment≈1)，则证明 DIF 和 FPC 捕捉不同信号维度。\", \"parent\": \"plan_001_real_data_dif_mmlu\", \"conclusion\": \"success\", \"metrics\": {\"paper_found\": true, \"title\": \"Growing Pains: Extensible and Efficient LLM Benchmarking Via Fixed Parameter Calibration\", \"authors\": \"Habba et al.\", \"venue\": \"arXiv 2604.12843 (April 2026)\", \"fpc_meaning\": \"Fixed Parameter Calibration (NOT Focal Point Contamination)\", \"contamination_detection\": false, \"anchor_item_list_public\": false, \"overlap_analysis_possible\": false, \"relevance_to_our_work\": \"shared IRT foundation + contamination acknowledged as limitation\"}, \"notes\": \"Growing Pains (Habba et al., 2026) 的 FPC = Fixed Parameter Calibration，不是 Focal Point Contamination。论文用 IRT anchor items 做高效 benchmark 校准（100 anchor items per dataset, 395+ models, Spearman ρ≥0.9），不涉及污染检测。Anchor item IDs 动态计算、未公开持久化。无法执行 Jaccard overlap 分析。但论文在 Limitations 中承认 anchor items 可能随时间被污染，直接支持我们 DIF-based detection 的必要性论点。适合在 Related Work 中引用。\"}, \"plan_034_multi_subject_injection\": {\"status\": \"DONE\", \"created_at\": \"2026-05-21T15:43:12.118Z\", \"updated_at\": \"2026-05-21T16:02:54.334Z\", \"hypothesis\": \"Proposition 1 声称当污染局限于单一 subject 时 ΔFPR=0（cross-subject matching 不受污染）。当同时污染 k∈{1,2,3,5,10,20} 个 subject 时，matching variable 被逐步污染，ΔFPR(k) 将随 k 单调递增。具体预测：k≤3 时 ΔFPR<0.02（matching variable 被稀释），k≥10 时 ΔFPR>0.05（matching variable 严重受污）。ΔTPR(k) 在 k=1 与 k=20 之间保持稳定（>0.3 at p=0.5），因为 detection 对 target subject 内的 signal 而非 matching quality 更敏感。\", \"parent\": \"plan_016_within_subject_semi_synthetic\", \"conclusion\": \"success\", \"metrics\": {\"grid\": {\"k_values\": [1, 2, 3, 5, 10, 20], \"p_values\": [0.1, 0.3, 0.5], \"seeds_per_k\": 5, \"total_runs\": 90}, \"n_ref\": 1080, \"n_foc\": 807, \"n_foc_inject\": 787, \"proposition_1_boundary\": \"k≈5-10 subjects\", \"non_target_delta_fpr\": {\"k1_p05\": 0.002, \"k2_p05\": 0.002, \"k3_p05\": -0.001, \"k5_p05\": 0.007, \"k10_p03\": 0.026, \"k10_p05\": 0.069, \"k20_p03\": 0.072, \"k20_p05\": 0.167}, \"target_tpr\": {\"k1_p05\": 0.834, \"k5_p05\": 0.734, \"k10_p05\": 0.67, \"k20_p05\": 0.611}, \"key_findings\": {\"k_le_5_robust\": true, \"k_le_5_max_delta_fpr\": 0.007, \"k10_significant_at_p03\": true, \"k20_massive_inflation\": true, \"p01_robust_all_k\": true, \"tpr_dilution_with_k\": true, \"boundary_rule\": \"cross-subject DIF reliable when contaminated fraction <10%\"}}, \"notes\": \"Proposition 1 robustness boundary 实验完成。核心结论：cross-subject MH-DIF 在 k≤5 subjects (≤8.8%) 同时污染时 ΔFPR<0.007，Proposition 1 实际成立。k=10 (17.5%) 开始 p≥0.3 时 ΔFPR 显著（+0.026~+0.069）。k=20 (35.1%) 大规模膨胀（p=0.5 时 ΔFPR=+0.167）。低强度 p=0.1 在所有 k 值下都 robust。TPR 随 k 增大而下降（0.834→0.611 at p=0.5），因为 matching variable 吸收了部分 DIF 信号。实际意义：real-world 污染通常影响少数 subjects，cross-subject auditing 有足够 safety margin。\"}, \"plan_028_multi_bench_dif\": {\"status\": \"DONE\", \"created_at\": \"2026-05-21T10:45:20.123Z\", \"updated_at\": \"2026-05-21T14:04:56.321Z\", \"hypothesis\": \"Temporal DIF (2023 vs 2024 cohort) 在 METABENCH 的 ARC, HellaSwag, WinoGrande, TruthfulQA 上均展现与 MMLU 类似的显著 C% (>15%)，证明 temporal DIF 现象跨 benchmark 泛化，不是 MMLU 特有的 artifact。所有 benchmark 的 random-split control C% < 1%。\", \"parent\": \"plan_001_real_data_dif_mmlu\", \"metrics\": {\"mmlu\": {\"n_items\": 12508, \"n_ref\": 1080, \"n_foc\": 807, \"pct_c\": 31.3, \"random_pct_c\": 0.18, \"bootstrap_ci_95\": [29.38, 38.05], \"bootstrap_mean\": 33.14, \"bootstrap_sd\": 2.3, \"bootstrap_n\": 1000}, \"winogrande\": {\"n_items\": 1267, \"n_ref\": 1017, \"n_foc\": 803, \"pct_c\": 30.3, \"random_pct_c\": 0.32}, \"truthfulqa\": {\"n_items\": 817, \"n_ref\": 1080, \"n_foc\": 807, \"pct_c\": 29.7, \"random_pct_c\": 0.37}, \"arc\": {\"n_items\": 1172, \"n_ref\": 1080, \"n_foc\": 807, \"pct_c\": 26.9, \"random_pct_c\": 0.6}, \"gsm8k\": {\"n_items\": 1319, \"n_ref\": 1017, \"n_foc\": 804, \"pct_c\": 18.9, \"random_pct_c\": 0.3}, \"hellaswag\": {\"n_items\": 10042, \"n_ref\": 1080, \"n_foc\": 807, \"pct_c\": 17.9, \"random_pct_c\": 0.28}, \"cross_benchmark_range\": \"17.9-31.3%\", \"all_random_controls_below_1pct\": true, \"min_enrichment_ratio\": 45, \"n_benchmarks\": 6}, \"conclusion\": \"success\", \"notes\": \"All 6 METABENCH benchmarks show significant temporal DIF (17.9-31.3% ETS C), with all random controls <1%. Cross-benchmark consistency confirms temporal DIF is a universal phenomenon, not MMLU-specific. Knowledge/reasoning benchmarks (MMLU 31.3%, TruthfulQA 29.7%, ARC 26.9%, WinoGrande 30.3%) show higher C% than math/commonsense (GSM8K 18.9%, HellaSwag 17.9%). This directly addresses Dream #6 reviewer concern about single-benchmark generalizability. Worker failed 5× due to OOM on hellaswag.csv (2GB, 52M rows) — fixed with chunked loading.\"}, \"plan_032_dif_cleaned_mmlu\": {\"status\": \"DONE\", \"created_at\": \"2026-05-21T13:38:51.707Z\", \"updated_at\": \"2026-05-21T13:49:14.041Z\", \"hypothesis\": \"虽然 DIF-cleaned MMLU 的全局 rank correlation 很高 (ρ≈0.997)，但局部排名变化将揭示 DIF 的实际影响：特定模型家族（尤其是 2024 年新模型如 phi-3, llama-3）将在移除 C-flagged items 后排名显著下降，而 2023 年模型排名上升。这证明 DIF items 虽然不改变全局趋势，但系统性地偏向特定模型代际，构成 benchmark fairness 问题。\", \"parent\": \"plan_017_downstream_impact\", \"metrics\": {\"n_items_full\": 12508, \"n_items_cleaned\": 8590, \"n_items_removed\": 3918, \"pct_removed\": 31.3, \"spearman_rho\": 0.9965, \"rank_change_std\": 127.1, \"rank_change_min\": -589, \"rank_change_max\": 849, \"pct_change_ge5\": 89.5, \"pct_change_ge10\": 79.5, \"pct_change_ge20\": 66.4, \"pct_change_ge50\": 41.9, \"pct_change_ge100\": 24.8, \"top100_pct_ge10\": 18, \"top500_pct_ge10\": 47.2, \"cohort_2023_mean_change\": -22.56, \"cohort_2023_median_change\": -5, \"cohort_2024_mean_change\": 73.6, \"cohort_2024_median_change\": 11, \"systematic_bias\": \"DIF items favor 2024 models; cleaning hurts 2024 +73.6 avg, helps 2023 -22.6 avg\", \"top_hurt_families\": {\"phi-3\": 258.35, \"command-r\": 235, \"solar\": 149.15, \"llama-3\": 120.86}, \"top_benefit_families\": {\"mistral-0.1\": -60.32, \"mistral\": -53.27, \"zephyr\": -29.94, \"gemma-2\": -28.78}, \"removed_items_harder\": true, \"removed_mean_difficulty\": 0.409, \"cleaned_mean_difficulty\": 0.46, \"random_baseline_20trials\": {\"rank_change_std\": {\"mean\": 60.2, \"std\": 7.8}, \"mean_abs_rank_change\": {\"mean\": 36, \"std\": 3.6}, \"pct_change_ge100\": {\"mean\": 8.5, \"std\": 2}, \"cohort_2023_mean_change\": {\"mean\": 0.4, \"std\": 4.1}, \"cohort_2024_mean_change\": {\"mean\": 2.8, \"std\": 21.2}}, \"dif_vs_random_z_scores\": {\"rank_change_std_z\": 8.5, \"mean_abs_change_z\": 10.7, \"pct_ge100_z\": 8.2, \"cohort_2023_z\": -5.6, \"cohort_2024_z\": 3.3, \"cohort_asymmetry_gap_z\": 4.4}}, \"notes\": \"直接回应 Dream #7 \\\"ρ=0.997 is the paper's most damaging result\\\" 审稿意见。全局 ρ=0.9965 确实很高，但掩盖了剧烈的局部排名变化：89.5% 模型变化 ≥5 位，24.8% 变化 ≥100 位，最大变化 849 位。关键发现：系统性 cohort 偏差——2024 模型平均排名下降 73.6 位，2023 模型平均上升 22.6 位。Phi-3 下降 258 位, Llama-3 下降 121 位（DIF items 偏向这些新模型）。Mistral 系列上升 53 位。这证明 DIF 不仅是统计标记，更揭示了 benchmark 对不同模型代际的系统性偏差。\", \"conclusion\": \"success\"}, \"plan_033_subject_dif_concentration\": {\"status\": \"DONE\", \"created_at\": \"2026-05-21T13:41:16.628Z\", \"updated_at\": \"2026-05-21T13:42:06.450Z\", \"hypothesis\": \"DIF 在 MMLU 57 个 subject 间分布不均匀，且 STEM vs Humanities 存在系统性差异。控制 item difficulty 和 discrimination 后，特定 subject 的 content 本身预测 DIF 概率——这说明 DIF 不仅由 psychometric properties 驱动，还受知识领域内容特征影响。同时，DIF 的方向（favor 2023 vs 2024）可能在不同领域呈现不同模式。\", \"parent\": \"plan_001_real_data_dif_mmlu\", \"metrics\": {\"n_subjects\": 57, \"all_subjects_have_dif\": true, \"mean_pct_c\": 30.6, \"median_pct_c\": 29.7, \"sd_pct_c\": 5.5, \"range_pct_c\": [20.7, 48.4], \"top3_subjects\": {\"business_ethics\": 48.4, \"human_aging\": 41.9, \"formal_logic\": 40.4}, \"bottom3_subjects\": {\"computer_security\": 20.7, \"marketing\": 20.9, \"management\": 21.7}, \"domain_pct_c\": {\"STEM\": 30.9, \"Humanities\": 31.1, \"Social_Science\": 31.6}, \"stem_vs_humanities_p\": 0.611, \"kruskal_wallis_p\": 0.78, \"logistic_regression\": {\"difficulty_OR\": 0.086, \"discrimination_OR\": 57.2, \"pseudo_r2\": 0.042}, \"excess_dif_subjects\": [\"professional_law\", \"human_aging\", \"world_religions\", \"business_ethics\", \"professional_medicine\"], \"overall_pct_favor_2024\": 43.9, \"temporal_asymmetry\": {\"STEM_pct_favor_2024\": 55.4, \"Humanities_pct_favor_2024\": 35.6, \"Social_Science_pct_favor_2024\": 42}, \"unidirectional_subjects\": {\"world_religions\": {\"pct_favor_2024\": 16.9}, \"logical_fallacies\": {\"pct_favor_2024\": 20}}}, \"notes\": \"Hypothesis 部分验证：DIF rate 跨 domain 无显著差异 (STEM 30.9% vs Humanities 31.1%, p=0.61)，但 DIF direction 有强领域依赖——STEM 55.4% DIF items 偏向 2024 模型（能力提升），Humanities 仅 35.6%（64.4% 偏向 2023）。world_religions 和 logical_fallacies 呈近单向偏向 2023 (≥80%)。Logistic regression: discrimination OR=57.2, difficulty OR=0.086, 但 pseudo R²=0.042——item properties 仅解释 4% DIF variance，content 特征是主要驱动力。5 个 subject 控制 item props 后仍有 excess DIF (professional_law, human_aging, world_religions, business_ethics, professional_medicine)。\", \"conclusion\": \"success\"}, \"plan_031_temporal_granularity\": {\"status\": \"DONE\", \"created_at\": \"2026-05-21T12:46:39.820Z\", \"updated_at\": \"2026-05-21T12:49:28.194Z\", \"hypothesis\": \"如果 temporal DIF 随时间距离单调递增，则 half-year cohort (2023-H2 vs 2024-H1, 0.5yr) 的 C% 应显著低于 full-year (2023 vs 2024, 1.0yr) 的 C%。这检验 DIF 信号是否与 temporal distance 成正比，回应 Reviewer 对 binary temporal split 过于粗糙的批评。如果 half-year C% ≈ full-year C%，说明 DIF 信号在短至 6 个月的窗口内即已饱和。\", \"parent\": \"plan_001_real_data_dif_mmlu\", \"metrics\": {\"mmlu_full_year\": {\"comparison\": \"2023 vs 2024\", \"distance_yr\": 1, \"n_ref\": 1080, \"n_foc\": 807, \"pct_c\": 31.32, \"random_pct_c\": 0.02}, \"mmlu_half_year\": {\"comparison\": \"2023-H2 vs 2024-H1\", \"distance_yr\": 0.5, \"n_ref\": 1018, \"n_foc\": 807, \"pct_c\": 34.35, \"random_pct_c\": 0.19}, \"mmlu_within_2023\": {\"comparison\": \"2023-H1 vs 2023-H2\", \"distance_yr\": 0.5, \"n_ref\": 62, \"n_foc\": 1018, \"pct_c\": 22.62, \"random_pct_c\": 0.18, \"supplementary\": true}, \"cross_bench_half_year\": {\"arc_pct_c\": 29.27, \"hellaswag_pct_c\": 18.07, \"winogrande_pct_c\": 33.62, \"truthfulqa_pct_c\": 31.33}, \"cross_bench_full_year\": {\"arc_pct_c\": 26.88, \"hellaswag_pct_c\": 17.89, \"winogrande_pct_c\": 30.31, \"truthfulqa_pct_c\": 29.74}, \"half_year_gt_full_year_all_benchmarks\": true, \"dif_saturates_within_6mo\": true}, \"notes\": \"Reviewer 评定 partial success：MMLU 半年有效（34.35% vs 0.19%, 181× enrichment），但 cross-benchmark 半年 enrichment 不均——HellaSwag 仅 3.5× (18.07%/5.23%)，其余 ARC 12.2×, WinoGrande 12.2×, TruthfulQA 51.4×。DIF 在 6 个月内即饱和，cohort purity > temporal distance。2023-H1 vs 2023-H2 (supplementary, N=62 < 80): C%=22.62%。\", \"conclusion\": \"success\"}, \"plan_030_odds_ratio\": {\"status\": \"DONE\", \"created_at\": \"2026-05-21T10:17:26.316Z\", \"updated_at\": \"2026-05-21T10:18:26.271Z\", \"hypothesis\": \"Logistic regression 的 odds ratio + CI 量化 accuracy change 与 DIF C flag 的关联强度。Item-level accuracy change (Model 3) 比 domain-level delta (Model 1) 提供更精确的预测。控制 item properties (difficulty + discrimination) 后，accuracy change 的 OR 反转（Simpson's paradox），说明 DIF C 主要由 item 固有属性驱动而非 accuracy shift。\", \"parent\": \"plan_001_real_data_dif_mmlu\", \"metrics\": {\"model1_domain_delta\": {\"mcfadden_r2\": 0.0007, \"nagelkerke_r2\": 0.0012, \"aic\": 15545.2, \"subject_acc_delta_or\": 80.86, \"subject_acc_delta_or_per_010\": 1.55, \"subject_acc_delta_or_ci_per_010\": [1.19, 2.03]}, \"model2_domain_delta_plus_items\": {\"mcfadden_r2\": 0.0423, \"nagelkerke_r2\": 0.072, \"aic\": 14902.3, \"subject_acc_delta_or_per_010\": 0.73, \"ctt_difficulty_or_per_010\": 0.78, \"ctt_discrimination_or_per_010\": 1.51}, \"model3_item_delta\": {\"mcfadden_r2\": 0.0012, \"nagelkerke_r2\": 0.0021, \"aic\": 15536.9, \"item_acc_change_or\": 2.11, \"item_acc_change_or_per_010\": 1.08, \"item_acc_change_ci\": [1.51, 2.96]}, \"model4_item_delta_plus_items\": {\"mcfadden_r2\": 0.0434, \"nagelkerke_r2\": 0.0737, \"aic\": 14885.4, \"item_acc_change_or_per_010\": 0.92, \"ctt_difficulty_or_per_010\": 0.77, \"ctt_discrimination_or_per_010\": 1.54}, \"simpsons_paradox\": true, \"lr_test_m1_vs_m2_chi2\": 646.98, \"lr_test_m3_vs_m4_chi2\": 655.53, \"best_model\": \"Model 4 (item Δ + item props)\"}, \"conclusion\": \"success\"}, \"plan_027_temporal_overlap\": {\"status\": \"DONE\", \"created_at\": \"2026-05-21T08:34:47.232Z\", \"updated_at\": \"2026-05-21T08:38:52.937Z\", \"hypothesis\": \"Temporal cohort ability gap 很小 (d=-0.17)，ability-matched C% 接近 full 31.3%，确认 temporal DIF 非 ability confound 产物\", \"parent\": \"plan_001_real_data_dif_mmlu\", \"metrics\": {\"cohort_2023_n\": 1080, \"cohort_2023_mean\": 0.5814, \"cohort_2023_sd\": 0.1405, \"cohort_2024_n\": 807, \"cohort_2024_mean\": 0.6068, \"cohort_2024_sd\": 0.1556, \"cohens_d\": -0.173, \"overlap_coefficient\": 0.764, \"bhattacharyya\": 0.961, \"full_c_pct\": 31.3, \"score_range_overlap_c_pct\": 30.9, \"nn_matched_c_pct_mean\": 28.9, \"nn_matched_c_pct_sd\": 0.1, \"nn_matched_n_per_group\": 638, \"nn_matched_d\": -0.01, \"ability_confound_pp\": 2.4, \"ability_confound_pct_of_total\": 7.7, \"llama_comparison_d\": -0.99, \"llama_comparison_overlap\": 0.18, \"llama_matched_c_pct\": 28.3}, \"conclusion\": \"success\"}, \"plan_004_gsm8k_cross_benchmark\": {\"status\": \"DONE\", \"created_at\": \"2026-05-21T00:30:09.372Z\", \"updated_at\": \"2026-05-21T01:22:16.029Z\", \"hypothesis\": \"GSM8K 的 temporal DIF (2023 vs 2024) 将展示与 MMLU 类似的 30-40% ETS C%，证明 temporal DIF 现象跨 benchmark 泛化。使用 METABENCH 其他 benchmarks 总分做 external matching（GSM8K 无 subject 分层），预期 baseline FPR 更可控。如果 C% 在同一量级 → DIF 作为 benchmark health diagnostic 的泛化性得到验证。\", \"parent\": \"plan_001_real_data_dif_mmlu\", \"metrics\": {\"step1_gsm8k_temporal_dif\": {\"n_items\": 1319, \"n_ref\": 1017, \"n_foc\": 804, \"standard_c_pct\": 18.9, \"external_c_pct\": 47.4, \"sanity_c_pct\": 0.3, \"standard_external_spearman\": 0.926}, \"step2_semi_synthetic\": {\"standard_delta_tpr_p10\": 0.818, \"external_delta_tpr_p10\": 0.517}, \"step3_gsm1k_correlation\": {\"n_models\": 33, \"n_dif_c_items\": 249, \"pearson_r\": -0.478, \"pearson_p\": 0.005, \"spearman_rho\": -0.403, \"spearman_p\": 0.02, \"partial_r_controlling_accuracy\": -0.385, \"partial_p\": 0.027, \"permutation_p\": 0.014, \"dif_c_favor_2024\": 78, \"dif_c_favor_2023\": 171, \"direction\": \"NEGATIVE (opposite to contamination hypothesis)\", \"cook_d_max_model\": \"Deepseek-math-7b-rl\", \"leave_one_out_r_range\": \"-0.537 to -0.374\", \"robust\": true}}, \"notes\": \"Step 3 GSM1K correlation: r=-0.478 (p=0.005). |r|>0.3 threshold met but direction NEGATIVE — opposite to contamination hypothesis. DIF-C items disadvantage contaminated models, not advantage them. 171/249 DIF-C items favor older models. Partial r=-0.385 (p=0.027) controlling for overall accuracy. Permutation p=0.014. Robust to leave-one-out. Interpretation: DIF captures genuine measurement anomalies orthogonal to contamination. Contamination produces narrow boost on typical items, fails on atypical-difficulty items (DIF-C). Supports characterization narrative: DIF as benchmark health diagnostic, not contamination detector.\", \"conclusion\": \"negative\"}, \"plan_017_downstream_impact\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T23:44:12.194Z\", \"updated_at\": \"2026-05-21T00:05:41.991Z\", \"hypothesis\": \"移除 temporal DIF-flagged items (ETS C, ~31% of MMLU items) 后，模型跨代排名更稳定（Spearman ρ 提升），且稳定性提升显著优于随机移除相同数量 items 的 baseline。这证明 DIF 不只标记 noise，而是精确识别了 problematic items，为 DIF 作为 benchmark quality tool 提供 downstream evidence。\", \"parent\": \"plan_001_real_data_dif_mmlu\", \"metrics\": {\"n_dif_items\": 3918, \"n_stable_items\": 8590, \"dif_pct\": 31.3, \"rho_full_vs_stable_2023\": 0.998851, \"rho_full_vs_stable_2024\": 0.997014, \"rho_full_vs_stable_all\": 0.996451, \"shr_full\": 0.9934, \"shr_stable\": 0.9919, \"dif_vs_random_z_mean\": -14.91, \"dif_vs_random_all_21_conditions_significant\": true, \"dif_removal_MORE_disruptive_than_random\": true, \"cross_cohort_ratio_dif_vs_full\": 1.0919, \"cross_cohort_ratio_stable_vs_full\": 0.9581, \"top_beneficiaries\": \"phi-3, llama-3 derivatives\", \"top_hurt\": \"mistral merges, slerp models\", \"max_rank_change\": 851}, \"conclusion\": \"negative\", \"notes\": \"Hypothesis REJECTED but finding is richer. DIF removal causes MORE ranking disruption than random (z=-8 to -49σ, 21/21 conditions). DIF items are NOT noise — they carry concentrated differential information that systematically discriminates models. Key insight: DIF items capture temporal instability (1.09× cross-cohort accuracy swing vs 0.96× stable items). Rankings are very robust (ρ>0.996 even at 38% removal). Top beneficiaries of DIF items: phi-3 and llama-3 derivatives (+700-850 ranks). Top hurt: mistral merges/slerp models (-400 to -587 ranks). Paper narrative shift: DIF items are not \\\"bad items to remove\\\" but \\\"items that reveal differential model capabilities across generations\\\" — supports characterization narrative over cleaning narrative.\"}, \"plan_016_within_subject_semi_synthetic\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T22:30:50.476Z\", \"updated_at\": \"2026-05-20T22:49:02.342Z\", \"hypothesis\": \"在 subject 内部使用 within-subject total score 做 MH 分层的 semi-synthetic injection 中，DIF 仍能检测差异性污染（ΔTPR > 0.3 at p=0.5）。这证明 DIF 方法在 subject 级别也有效，plan_014 的 38% within-subject C% 反映的是真实代际能力差异而非方法失败。\", \"parent\": \"plan_014_within_subject_dif\", \"metrics\": {\"within_matching\": {\"subjects_passing_p05\": \"3/5 (human_aging, professional_medicine, formal_logic)\", \"business_ethics_baseline_fpr\": 0.563, \"business_ethics_delta_tpr_p05\": -0.078, \"human_aging_baseline_fpr\": 0.334, \"human_aging_delta_tpr_p05\": 0.385, \"professional_medicine_baseline_fpr\": 0.312, \"professional_medicine_delta_tpr_p05\": 0.327, \"formal_logic_baseline_fpr\": 0.409, \"formal_logic_delta_tpr_p05\": 0.457, \"high_school_statistics_baseline_fpr\": 0.407, \"high_school_statistics_delta_tpr_p05\": 0.194, \"fpr_inflates_with_injection\": true, \"avg_fpr_inflation_p10\": 0.186}, \"cross_matching\": {\"subjects_passing_p05\": \"4/5 (human_aging, professional_medicine, formal_logic, high_school_statistics)\", \"business_ethics_baseline_fpr\": 0.533, \"business_ethics_delta_tpr_p05\": 0.056, \"human_aging_baseline_fpr\": 0.431, \"human_aging_delta_tpr_p05\": 0.375, \"professional_medicine_baseline_fpr\": 0.38, \"professional_medicine_delta_tpr_p05\": 0.38, \"formal_logic_baseline_fpr\": 0.402, \"formal_logic_delta_tpr_p05\": 0.543, \"high_school_statistics_baseline_fpr\": 0.335, \"high_school_statistics_delta_tpr_p05\": 0.433, \"fpr_stable_across_injection\": true, \"delta_fpr_all_subjects\": 0}, \"success_criterion_met\": true}, \"conclusion\": \"success\", \"notes\": \"Revised per Director review. (1) Fixed comparison table FPR (0.048→0.314). (2) Added cross-subject matching: FPR completely stable (ΔFPR=0.000 all 5 subjects), better detection (4/5 ΔTPR>0.3 vs within 3/5). Within-subject FPR inflates +0.067 to +0.281 at p=1.0 due to matching variable contamination. (3) Added formal_logic (109 items, ΔTPR=+0.543 cross) and high_school_statistics (181 items, ΔTPR=+0.433 cross). Both 5 strata, clean detection. Cross-subject matching confirms plan_011's external MH finding at subject level.\"}, \"plan_013_q3_local_independence\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T21:58:11.134Z\", \"updated_at\": \"2026-05-20T22:36:16.364Z\", \"hypothesis\": \"MMLU 同一 subject 内的 items 存在显著局部依赖性（within-subject Q3 均值 > 0.20，显著高于 cross-subject Q3），这违反 2PL IRT 和 MH-DIF 的局部独立性假设，部分解释了 plan_011 中 temporal cohort baseline FPR=31% 的膨胀。如果确认，则动机化后续 bifactor/testlet 模型改进。\", \"parent\": \"plan_011_semi_synthetic_validation\", \"metrics\": {\"within_subject_mean_q3\": 0.0086, \"cross_subject_mean_q3\": 0.0031, \"within_subject_pct_above_020\": 11.3, \"cross_subject_pct_above_020\": 2.2, \"mann_whitney_p\": 2.29e-09, \"worst_subject\": \"moral_scenarios\", \"worst_subject_pct_above_020\": 34.2, \"n_items_retained\": 12251, \"n_items_filtered\": 257, \"subject_size_q3_corr\": 0.2064, \"subject_size_q3_p\": 0.123}, \"conclusion\": \"success\", \"notes\": \"Q3 诊断完成。Hypothesis 部分验证：within-subject 均值 Q3=0.0086（低于 0.20 阈值），但尾部显著——11.3% within-subject pairs |Q3|>0.20 vs 2.2% cross-subject（5x, Mann-Whitney p=2.3e-9）。局部依赖存在但温和，不太可能单独解释 31% FPR。最严重 subjects: moral_scenarios 34.2%, world_religions 18%, marketing 17.5%。结论：局部依赖是 FPR 的贡献因素之一，但主要 FPR 来源是 genuine temporal DIF（plan_014 确认 within-subject C%=38%）。\"}, \"plan_015_bifactor_irt\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-20T22:23:51.598Z\", \"updated_at\": \"2026-05-20T22:30:44.925Z\", \"hypothesis\": \"Bifactor IRT（1 general + 57 subject-specific factors）的 general θ 分层能将 temporal cohort baseline FPR 从 31% 降至 <15%，同时在 semi-synthetic 框架下保持 TPR>0.60 at p=0.5。Bifactor 通过分离学科特异性能力和通用能力，消除 subject-level 能力差异对 MH-DIF 的混淆。\", \"parent\": \"plan_012_irt_theta_conditioning\", \"conclusion\": \"killed\", \"notes\": \"D010: Director 取消。plan_014 前置检查结果 within-subject C%=38.1% (>25%)，证明 temporal DIF 渗透到 subject 内部，bifactor 无法解决。Between-subject variance 反而在压低 overall C%。\"}, \"plan_014_within_subject_dif\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T22:23:50.857Z\", \"updated_at\": \"2026-05-20T22:28:27.350Z\", \"hypothesis\": \"Within-subject temporal DIF（只用该 subject 内 items 和总分）在高 C% subjects 上的 C% 将 < 15%，表明 plan_001 的 31% FPR 主要来自 between-subject 能力差异而非 within-subject 因素。如果 within-subject C% > 25%，则 bifactor 模型也无法解决 FPR 问题。\", \"parent\": \"plan_012_irt_theta_conditioning\", \"metrics\": {\"business_ethics_within_c_pct\": 45.2, \"human_aging_within_c_pct\": 33, \"formal_logic_within_c_pct\": 39.5, \"professional_medicine_within_c_pct\": 31.1, \"high_school_statistics_within_c_pct\": 42, \"avg_within_subject_c_pct\": 38.1, \"avg_cross_subject_c_pct\": 40.5, \"avg_delta_within_vs_cross\": -2.4, \"sibtest_available\": false, \"r_available\": false, \"decision_zone\": \">25% HIGH\"}, \"conclusion\": \"negative\", \"notes\": \"Within-subject temporal DIF 前置检查 NEGATIVE。5 个高 C% subjects 平均 within-subject C%=38.1%（全部 >25%）：business_ethics 45.2%, human_aging 33.0%, formal_logic 39.5%, professional_medicine 31.1%, high_school_statistics 42.0%。Cross-subject matching C% 40.5%（Δ=-2.4pp）。结论：temporal DIF 渗透到每个 subject 内部，不是 between-subject 能力差异的伪影。Bifactor 模型大概率无法解决 FPR 问题。SIBTEST: R 不可用，Python 无实现。\"}, \"plan_012_irt_theta_conditioning\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T21:58:10.439Z\", \"updated_at\": \"2026-05-20T22:20:01.371Z\", \"hypothesis\": \"用 2PL IRT 估计的 θ 值（10-20 等距层）替代粗糙总分作为 MH 分层变量后，semi-synthetic 框架下 baseline FPR 将从 ~31%（temporal）/~49%（ability）降至 <10%，同时保持 TPR>0.70 at p=0.5。θ-conditioning 通过更精确的能力匹配消除 impact-vs-DIF 混淆残留。\", \"parent\": \"plan_011_semi_synthetic_validation\", \"metrics\": {\"temporal_theta_qt20_fpr\": 0.312, \"temporal_theta_qt20_tpr_p05\": 0.876, \"temporal_theta_qt20_tpr_p10\": 1, \"temporal_external5_fpr\": 0.314, \"temporal_external5_tpr_p05\": 0.834, \"ability_theta_qt10_fpr\": 0.093, \"ability_theta_qt10_tpr_p05\": 0.206, \"ability_theta_qt10_tpr_p10\": 0.544, \"ability_theta_qt20_fpr\": 0.079, \"ability_theta_qt20_tpr_p05\": 0.21, \"ability_theta_qt20_tpr_p10\": 0.544, \"ability_external5_fpr\": 0.493, \"ability_external5_tpr_p05\": 0.756, \"theta_total_score_corr\": 0.9986, \"enrichment_all_variants\": \"0.97-1.00\", \"success_criterion_met\": false}, \"conclusion\": \"negative\", \"notes\": \"θ-conditioning NEGATIVE. Temporal cohort: logit(p) θ corr=0.9986 with total score, all θ variants FPR=31-35% (no improvement over plan_011 external_5 FPR=31.4%). TPR well maintained (0.83-0.88 at p=0.5). Ability cohort: quantile θ bins (qt_10/qt_20) reduce FPR from 49% to 8-9%, but TPR collapses from 76% to 21% at p=0.5 — proving plan_011 ability cohort's high TPR was mainly ability confounding, not genuine DIF detection. Enrichment vs Li et al.: all variants 0.97-1.00 (unchanged from plan_001). Key conclusion: temporal cohort 31% baseline FPR is genuine DIF (real item-level differences between 2023 vs 2024 models), not an artifact of imprecise ability matching. Improving θ estimation won't fix it — need multidimensional or subject-level approaches.\"}, \"plan_011_semi_synthetic_validation\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T21:35:55.290Z\", \"updated_at\": \"2026-05-20T21:54:54.659Z\", \"hypothesis\": \"在 METABENCH 真实响应矩阵上注入已知差异性污染（focal group 指定 items 的 incorrect→correct 翻转）后，MH-DIF 的 ETS C 分类能在 ability-quintile cohort 上达到 TPR>0.5 (p=1.0) 且 FPR<0.05。如果成功，说明 plan_001/001b 的 enrichment≈1.0 是 Li et al. ground truth 不匹配（全局性 vs 差异性污染），而非 DIF 方法本身失败。\", \"parent\": \"plan_001b_matched_ability_dif\", \"metrics\": {\"temporal_external_tpr_p0\": 0.326, \"temporal_external_tpr_p03\": 0.548, \"temporal_external_tpr_p05\": 0.834, \"temporal_external_tpr_p07\": 0.99, \"temporal_external_tpr_p10\": 1, \"temporal_external_fpr\": 0.314, \"temporal_external_delta_tpr_p10\": 0.674, \"ability_external_tpr_p0\": 0.498, \"ability_external_tpr_p10\": 0.8, \"ability_external_fpr\": 0.493, \"ability_external_delta_tpr_p10\": 0.302, \"standard_mh_fpr_inflation\": \"temporal 0.298→0.616 at p=1.0\", \"matching_variable_contamination_confirmed\": true, \"bug_fix\": \"inf-delta classified as extreme DIF not class A\"}, \"conclusion\": \"success\", \"notes\": \"MH-DIF successfully detects injected differential contamination. Temporal+external: ΔTPR=+0.674 (0.326→1.000), FPR constant at 0.314. Clear dose-response across p={0.3,0.5,0.7,1.0}. Confirms plan_001/001b enrichment≈1.0 is ground truth mismatch (Li et al. = global contamination, DIF = differential contamination), NOT DIF method failure. Also discovered: (1) matching variable contamination when 20% items injected (standard MH FPR inflates 0.298→0.616, anchor/external variants immune), (2) inf-delta classification bug in plan_001 code fixed. Ability cohort has high baseline FPR (~49%) due to extreme Q1-2 vs Q4-5 ability gap — 5-strata insufficient.\"}, \"plan_001b_matched_ability_dif\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T21:35:08.552Z\", \"updated_at\": \"2026-05-20T21:35:51.089Z\", \"hypothesis\": \"在每个 accuracy quintile 内部做 temporal cohort MH-DIF（控制能力后），enrichment 将从 plan_001 的 0.96 提升到 >1.5，证明能力匹配能隔离出污染信号。\", \"parent\": \"plan_001_real_data_dif_mmlu\", \"conclusion\": \"negative\", \"notes\": \"D005: Matched-ability DIF 失败。所有 quintile enrichment 0.94-1.04。能力匹配未能隔离出污染信号。Reviewer 洞察：Li et al. web-overlap 是全局性污染标注（Common Crawl 对所有模型可用），不会产生 group-specific DIF。enrichment≈1.0 可能不是 DIF 方法失败，而是 ground truth 与 DIF 度量的东西根本不同——DIF 检测差异性训练数据包含，Li 检测存在性污染。\"}, \"plan_001_real_data_dif_mmlu\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T20:54:53.883Z\", \"updated_at\": \"2026-05-20T21:12:05.153Z\", \"hypothesis\": \"MH-DIF 在 METABENCH 真实 MMLU 数据（5227 模型 × 12508 items）上，用时间 cohort (2023 vs 2024) 和能力分位 cohort 分组时，ETS C 标记的 items 在 Li et al. clean items 中的 FPR ≤ 0.05，且 ETS C 标记在 contaminated items 中的比例显著高于 clean items。这验证 DIF 在真实数据上不会产生过多假阳性，且能捕捉到与 web-overlap 污染信号一致的差异性。\", \"parent\": \"mvp_dif_power_sim_phase2\", \"metrics\": {\"temporal_ets_c_pct\": 31.3, \"temporal_fpr_li_clean\": 0.318, \"temporal_enrichment\": 0.96, \"ability_ets_c_pct\": 2.9, \"ability_fpr_li_clean\": 0.027, \"ability_enrichment\": 1.19, \"within_family_llama2v3_c_pct\": 61.3, \"within_family_mistral_mixtral_c_pct\": 38.7, \"domain_spearman_rho\": 0.307, \"domain_spearman_p\": 0.02, \"sanity_random_split_c_pct\": 0.18, \"temporal_ability_jaccard\": 0.014}, \"conclusion\": \"negative\", \"notes\": \"Temporal cohort DIF (2023 vs 2024): 31.3% ETS C, enrichment=0.96 — DIF detects systematic capability improvement, NOT contamination (clean and contaminated items flagged at equal rates). Ability cohort: 2.9% C, enrichment=1.19 — weak positive signal, FPR=2.7% well controlled. Within-family (Llama-2 vs 3): 61.3% C confirms ability confound dominates. Domain ρ=0.307 (p=0.02) consistent with capability-driven DIF. Sanity check passed (random split 0.18% C). Core finding: naive MH-DIF cannot distinguish contamination from genuine capability improvement without ability matching or IRT equating.\"}, \"mvp_dif_power_sim_phase2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T18:52:34.145Z\", \"updated_at\": \"2026-05-20T19:30:16.477Z\", \"hypothesis\": \"ETS C 分类在 METABENCH 真实 MMLU 2PL IRT 参数（非理想化分布）下，仍能在 N≥80/group、δ≥1.4 时达到 TPR≥0.65、FPR≤0.10。Phase 1 用合成参数（a~LogNormal, b~N(0,1)）条件性通过，需验证真实参数分布（可能有偏态、聚集、极端值）不会降解检测功效。\", \"parent\": \"mvp_dif_power_sim\", \"metrics\": {\"ets_c_tpr_N80_d14\": 0.6823, \"ets_c_tpr_N80_d16\": 0.7223, \"ets_c_tpr_N100_d14\": 0.7582, \"ets_c_tpr_N100_d16\": 0.7966, \"ets_c_fpr_range\": \"0.036-0.042\", \"best_auc_mh\": 0.9254, \"best_auc_lr\": 0.9405, \"verdict\": \"PASS\", \"pass_plus_met\": true, \"real_param_a_mean\": 1.2, \"real_param_b_mean\": -0.84}, \"conclusion\": \"success\"}, \"mvp_dif_power_sim\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T17:16:29.354Z\", \"updated_at\": \"2026-05-20T18:52:23.378Z\", \"hypothesis\": \"DIF 跨模型批次分析（MH + Logistic Regression）在 N=50-80/group、污染效应量 δ≥1.0 logits 时，对 10% 污染 items 的检测功效 TPR≥0.70 且 FPR≤0.10。这是整个 pipeline 的前提假设——若 DIF 在理想合成数据上都 underpowered，则后续真实数据方案不成立。\", \"metrics\": {\"best_tpr_mh\": 0.6817, \"best_tpr_lr\": 0.6869, \"best_condition\": \"N=100_delta=1.6\", \"best_auc_mh\": 0.9393, \"best_auc_lr\": 0.9593, \"pass_criterion_tpr_mh\": 0.0416, \"pass_criterion_tpr_lr\": 0.0703, \"pass_criterion_condition\": \"N=50_delta=1.0\", \"verdict\": \"FAIL\", \"all_fpr_below_015\": true}, \"conclusion\": \"success\", \"notes\": \"Conditional pass (D001): ETS C classification as primary detector. ETS C TPR=0.72-0.85 at N≥80,δ≥1.4; FPR well controlled. BH-corrected p-value based detection failed (TPR 0.04-0.07 at pass criterion). Raw power also insufficient for p-value approach. AUC discriminability good (0.91-0.96). Decision: pivot to ETS C magnitude-based detection, Phase 2 validates with real IRT parameters.\"}}, \"count\": 21, \"total\": 21, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.0839}}"
    }
  },
  "sourceToolAssistantUUID": "e7cb72d4-d874-44b8-900e-3cbed253222b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/.claude/sessions/reviewer_430cd31d",
  "sessionId": "ef30c0ef-29fb-4cb0-a309-7059c0bcd7c6",
  "version": "2.1.126",
  "gitBranch": "rebuttal-b1-b7"
}
```

</details>

---

### Runtime record

_source line 14_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[HANDOFF] 你是 Research Reviewer，这是 Loop #4。  ## 上一轮交接 (task_context)  ### 1. 🔴 硬约束 / 红线 - 本项目无 GPU、无远程服务器——纯论文写作+本地 CPU 分析项目 - 匿名仓库 `/tmp/anon_repo/` 的 git identity 必须是 `Anonymous <anonymous@example.c…",
  "leafUuid": "78c8376e-3046-4ba7-b246-d9fc715a7706",
  "sessionId": "ef30c0ef-29fb-4cb0-a309-7059c0bcd7c6"
}
```

---

### Runtime record

_source line 15_

```json
{
  "type": "ai-title",
  "aiTitle": "Research Reviewer Loop #4 - Paper Final Validation",
  "sessionId": "ef30c0ef-29fb-4cb0-a309-7059c0bcd7c6"
}
```

---

### Runtime record

_source line 16_

```json
{
  "type": "ai-title",
  "aiTitle": "Research Reviewer Loop #4 - Paper Final Validation",
  "sessionId": "ef30c0ef-29fb-4cb0-a309-7059c0bcd7c6"
}
```

---

### Runtime record

_source line 17 · 2026-05-25T14:12:19.538Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-25T14:12:19.538Z",
  "sessionId": "ef30c0ef-29fb-4cb0-a309-7059c0bcd7c6",
  "content": "[WRITE HANDOFF] 请立即写你的 handoff。\n\n**格式硬约束**:\n- 整条回复**只能**是 &lt;handoff>...&lt;/handoff> 标签包裹\n- 禁止在标签外写任何寒暄 / 说明 / 确认（\"好的\"/\"我开始写\"/\"写完了\"等）\n\n**必须覆盖以下 5 个 section（缺一不可，无内容写 N/A）**:\n\n### 1. 🔴 硬约束 / 红线\n  本项目特定的不可违反约束（GPU 设备号、服务器名、账号、路径限制等）。\n  写本项目特定的，不要抄 CLAUDE.md 通用 L1 红线。\n  下一个\"你\"第一眼看到的就是这里，写错了会被 Director CRITICAL。\n\n### 2. 🖥️ 基础设施快照\n  - 服务器名 + 工作目录 + Python 路径 + conda env\n  - 模型路径 / 数据集路径 / wandb config / HF cache\n  - 活跃进程：PID + tmux session + cron 任务 ID\n  写一次就稳定，下一个\"你\"不用再 SSH 探查。\n\n### 3. 📊 当前状态\n  - 你刚做完什么 / 正在做什么\n  - registry 里 RUNNING/PREPARING 的实验列表 + 一句话摘要\n  - 等待中的 Worker 回调 / Cron / Director 决策\n\n### 4. 📋 待办（条件触发式）\n  格式 \"条件 X 满足 → 动作 Y\"。例如:\n  - \"Falcon-H1R 下载完成 → sed 修 MODEL_PATH → dry-run → 提交\"\n  - \"pilot_011 出 GC4 结果 → ≥2pp 转架构 narrative，<2pp 写 null-result\"\n\n### 5. 🎯 战略上下文\n  - 项目核心结论 / 决策链（D001..）\n  - 下一个\"你\"最容易判断错的事 / 容易踩的坑\n\n**写作原则**：\n- 第 1 节必须是项目特定的（不是通用 L1 红线）\n- 第 2 节让下一轮 BOOT 后能立即开工，避免重新 SSH 探查\n- 简洁 > 完整：每节 5-10 行足够，长 handoff 不等于好 handoff\n\n示例格式:\n&lt;handoff>\n### 1. 🔴 硬约束 / 红线\n- 本项目只能用 cuda:4 / cuda:5（之前两次违规 cuda:0 被 Director CRITICAL）\n- submit_training_job 不支持 shell builtin（source/conda activate 全不行）\n\n### 2. 🖥️ 基础设施快照\n- 服务器：westd-8x6000，工作目录 /root/autodl-tmp/hybrid_reasoning_phases\n- Python：/root/miniconda3/bin/python（绝对路径，不走 conda activate）\n- 模型：/root/autodl-tmp/qwen35_4b_direct\n- 活跃：pilot_011 (PID 203221, tmux=pilot_011, cuda:4)\n\n### 3. 📊 当前状态\n我刚完成 pilot_010 分析，正在等 pilot_011 (Falcon-H1R) CoT 生成完成（6/50）。\nregistry: pilot_011 RUNNING；其他全 DONE。\n\n### 4. 📋 待办\n- pilot_011 cron 回调 → spawn worker 跑 probe + GC4 计算\n- GC4 ≥2pp → 转架构 narrative；<2pp → null-result paper outline 已就绪\n\n### 5. 🎯 战略上下文\nFalcon-H1R 是最后一个数据点。已知 4B/9B GC4 都 FAIL。\n易错：不要把 GC4-par (Falcon parallel) 和 GC4-seq (Qwen sequential) 直接对比。\n&lt;/handoff>"
}
```

---

### Runtime record

_source line 18 · 2026-05-25T14:12:19.539Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-25T14:12:19.539Z",
  "sessionId": "ef30c0ef-29fb-4cb0-a309-7059c0bcd7c6"
}
```

---

## Round 2

2 recorded events

### User

_source line 19 · 2026-05-25T14:12:19.530Z_

Continue from where you left off.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "78c8376e-3046-4ba7-b246-d9fc715a7706",
  "isSidechain": false,
  "promptId": "27428b93-6568-410c-adfd-d048d51b0ca7",
  "type": "user",
  "isMeta": true,
  "uuid": "b184b3d3-d1c0-4864-9489-c6872cc39738",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/.claude/sessions/reviewer_430cd31d",
  "sessionId": "ef30c0ef-29fb-4cb0-a309-7059c0bcd7c6",
  "version": "2.1.126",
  "gitBranch": "rebuttal-b1-b7"
}
```

</details>

---

### Assistant

_source line 20 · 2026-05-25T14:12:19.530Z_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b184b3d3-d1c0-4864-9489-c6872cc39738",
  "isSidechain": false,
  "type": "assistant",
  "uuid": "c4516662-dd37-48e1-907f-5646e84ccf23",
  "isApiErrorMessage": false,
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/.claude/sessions/reviewer_430cd31d",
  "sessionId": "ef30c0ef-29fb-4cb0-a309-7059c0bcd7c6",
  "version": "2.1.126",
  "gitBranch": "rebuttal-b1-b7",
  "message": {
    "id": "2890a3d0-5a5a-4344-ad1d-e8c206ab6c05",
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

_source line 21 · 2026-05-25T14:12:19.733Z_

[WRITE HANDOFF] 请立即写你的 handoff。

**格式硬约束**:
- 整条回复**只能**是 &lt;handoff>...&lt;/handoff> 标签包裹
- 禁止在标签外写任何寒暄 / 说明 / 确认（"好的"/"我开始写"/"写完了"等）

**必须覆盖以下 5 个 section（缺一不可，无内容写 N/A）**:

### 1. 🔴 硬约束 / 红线
  本项目特定的不可违反约束（GPU 设备号、服务器名、账号、路径限制等）。
  写本项目特定的，不要抄 CLAUDE.md 通用 L1 红线。
  下一个"你"第一眼看到的就是这里，写错了会被 Director CRITICAL。

### 2. 🖥️ 基础设施快照
  - 服务器名 + 工作目录 + Python 路径 + conda env
  - 模型路径 / 数据集路径 / wandb config / HF cache
  - 活跃进程：PID + tmux session + cron 任务 ID
  写一次就稳定，下一个"你"不用再 SSH 探查。

### 3. 📊 当前状态
  - 你刚做完什么 / 正在做什么
  - registry 里 RUNNING/PREPARING 的实验列表 + 一句话摘要
  - 等待中的 Worker 回调 / Cron / Director 决策

### 4. 📋 待办（条件触发式）
  格式 "条件 X 满足 → 动作 Y"。例如:
  - "Falcon-H1R 下载完成 → sed 修 MODEL_PATH → dry-run → 提交"
  - "pilot_011 出 GC4 结果 → ≥2pp 转架构 narrative，<2pp 写 null-result"

### 5. 🎯 战略上下文
  - 项目核心结论 / 决策链（D001..）
  - 下一个"你"最容易判断错的事 / 容易踩的坑

**写作原则**：
- 第 1 节必须是项目特定的（不是通用 L1 红线）
- 第 2 节让下一轮 BOOT 后能立即开工，避免重新 SSH 探查
- 简洁 > 完整：每节 5-10 行足够，长 handoff 不等于好 handoff

示例格式:
&lt;handoff>
### 1. 🔴 硬约束 / 红线
- 本项目只能用 cuda:4 / cuda:5（之前两次违规 cuda:0 被 Director CRITICAL）
- submit_training_job 不支持 shell builtin（source/conda activate 全不行）

### 2. 🖥️ 基础设施快照
- 服务器：westd-8x6000，工作目录 /root/autodl-tmp/hybrid_reasoning_phases
- Python：/root/miniconda3/bin/python（绝对路径，不走 conda activate）
- 模型：/root/autodl-tmp/qwen35_4b_direct
- 活跃：pilot_011 (PID 203221, tmux=pilot_011, cuda:4)

### 3. 📊 当前状态
我刚完成 pilot_010 分析，正在等 pilot_011 (Falcon-H1R) CoT 生成完成（6/50）。
registry: pilot_011 RUNNING；其他全 DONE。

### 4. 📋 待办
- pilot_011 cron 回调 → spawn worker 跑 probe + GC4 计算
- GC4 ≥2pp → 转架构 narrative；<2pp → null-result paper outline 已就绪

### 5. 🎯 战略上下文
Falcon-H1R 是最后一个数据点。已知 4B/9B GC4 都 FAIL。
易错：不要把 GC4-par (Falcon parallel) 和 GC4-seq (Qwen sequential) 直接对比。
&lt;/handoff>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c4516662-dd37-48e1-907f-5646e84ccf23",
  "isSidechain": false,
  "promptId": "27428b93-6568-410c-adfd-d048d51b0ca7",
  "type": "user",
  "uuid": "f33c7e53-ec45-4ab9-a32d-889995ba9a0b",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/.claude/sessions/reviewer_430cd31d",
  "sessionId": "ef30c0ef-29fb-4cb0-a309-7059c0bcd7c6",
  "version": "2.1.126",
  "gitBranch": "rebuttal-b1-b7"
}
```

</details>

---
