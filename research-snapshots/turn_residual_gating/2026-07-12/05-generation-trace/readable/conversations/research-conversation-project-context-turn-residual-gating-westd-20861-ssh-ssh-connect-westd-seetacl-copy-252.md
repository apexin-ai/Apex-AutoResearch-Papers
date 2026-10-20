# Research conversation: <project_context> # 项目: turn_residual_gating ## 运行环境 - 服务器名: westd-20861 - SSH 连接命令: ssh connect.westd.seetacloud.com # 

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 125
- **Recorded user turns:** 1
- **Tool calls:** 36
- **Original source:** `logs/chats/exported-trajectories/account-3/4b680861-4da7-411a-8744-3dabfdaf2205.jsonl`
- **Structured JSON:** [`bcba6ecb89f2ec6e5d20.json`](../../sessions/bc/bcba6ecb89f2ec6e5d20.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-25T20:37:57.437Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-25T20:37:57.437Z",
  "sessionId": "4b680861-4da7-411a-8744-3dabfdaf2205",
  "content": "&lt;project_context>\n# 项目: turn_residual_gating\n\n## 运行环境\n- 服务器名: westd-20861\n- SSH 连接命令: ssh connect.westd.seetacloud.com  # 必须用此命令，~/.ssh/config 自动应用密钥和跳板机，禁止用裸 IP\n- 项目代码根目录: /root/turn_residual_gating\n\n\n## 环境搭建\n连接服务器后先调 `detect_image` 检测是否为预置镜像。如果匹配，跳过基础环境搭建，只装项目特有依赖。已预装的包不要重复安装。\n\n## 输出风格\n回复简洁直接。只输出执行结果和必要信息，不要解释过程、不要客套、不要给未被要求的建议。\n&lt;/project_context>\n## 任务：论文正文（body text）数据审计\n\n对论文正文中的**每一个定量 claim**逐一验证，确保可追溯到 registry 实验记录。\n\n### 论文文件位置\n- 正文 tex 文件：`/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/`\n  - `abstract.tex`\n  - `introduction.tex`\n  - `method.tex`\n  - `experiments.tex`\n  - `analysis.tex`\n  - `discussion.tex`\n  - `conclusion.tex`\n  - `limitations.tex`\n  - `related_work.tex`（包含 Table 1）\n- included 表格：`/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/_project/paper/` 下的各种 `tab_*.tex`\n\n### Registry 位置\n用 `read_registry` 工具查询实验数据。关键实验 ID：\n- `d048_final_ar_eval` — AR evaluation 主数据源\n- `phase2_4way_eval_heldout` — Heldout TF evaluation\n- `phase2_4way_eval` — IID TF evaluation\n- `phase2_tg_s42_v7` — ThreadGate v7 训练\n- `phase2_tg_s42_v9_pcgrad` — PCGrad 训练\n- `phase2_ug_s42` — Uniform Gate 训练\n- `mmlu_eval_all` — MMLU 评估\n- `instruction_retention_test` — IR 测试\n- `tab_statistical_tests` — 统计检验\n- `p1_llama_ss_eval` — Llama SS 评估\n- `p2_llama_gradient_conflict` — Llama 梯度分析\n- `gradient_analysis` — Qwen 梯度分析\n- `trc_baseline` — TRC baseline\n- `eval_llama_ar_n20` — Llama AR eval\n- `llama_eval_s42` — Llama TF eval\n\n### 审计范围\n\n逐文件、逐段落扫描，对每个数字做以下检查：\n\n1. **Q1 准确性**：数字是否与 registry 记录一致？\n2. **Q2 精度一致**：同一数字在不同位置的四舍五入是否一致？（重点！附录审计已发现 gap ratio 7.8× vs 7.9×、~1.3× vs 1.2× 不一致）\n3. **Q3 跨章节一致性**：同一指标在 Abstract / Intro / Results / Analysis / Conclusion 各处是否完全一致？\n4. **Q4 可追溯性**：每个数字能否追溯到具体的 exp_id？\n\n### 重点关注\n\n- **Abstract**：关键 claim 数字（gap 倍数、SS 改善、MMLU 保持等）\n- **Introduction**：contribution 中引用的具体数字\n- **Method**：超参（lr, batch, steps, 模型尺寸, 参数量 ~57K/<0.001%）、GAR 定义中的数学\n- **Experiments**：每个结果段落的所有数字——GAR、PPL、gap ratio、p-value、effect size、CI\n- **Analysis**：gate conditioning 数字、梯度分析数字、TRC 数字、cross-model 数字、1.5B 数字\n- **Conclusion**：复述的数字是否与 Results 一致\n\n### 已知问题（附录审计发现，正文中也需检查）\n\n以下问题已在附录审计中发现，检查正文是否也存在：\n- gap ratio：正文 7.8×（用 0.50/0.064）vs crossmodel 表 7.9×（用 0.504/0.064）\n- SS gap：正文 ~1.3× vs 表 1.2×（精确值 1.24×）\n- \"≤1pp\" 声明实际为 2pp\n- PPL std ±0.001 实际 ±0.002\n\n### 产出格式\n\n写一份审计报告到 `/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/audit_body_text.md`，格式：\n\n```markdown\n# 正文数据审计报告\n\n## 统计\n- 总数字数：~N\n- 已验证：~M\n- 问题数：K\n\n## 逐章节审计\n\n### Abstract\n| 数字 | Registry来源 | 状态 | 备注 |\n...\n\n### Introduction\n...\n\n（每个章节一个表格）\n\n## 跨章节一致性检查\n（同一数字在多处出现的交叉验证表）\n\n## 问题清单\n（编号、位置、问题描述、建议修正）\n\n## 暂无出处的数字\n（列出无法从 registry 追溯的数字及原因）\n```\n\n### 工作流程\n1. `read_registry(project=\"turn_residual_gating\", limit=0, fields=[\"*\"])` 获取全部实验数据\n2. 逐一 Read 每个 tex 文件\n3. 对每个数字查 registry 验证\n4. 编写审计报告\n5. 特别注意跨章节一致性——建一张\"关键数字出现位置\"的交叉表\n\n### 注意\n- 不要修改任何 tex 文件，只做审计产出报告\n- 对于无法从 registry 追溯的数字（如文献引用的数字、数学推导的数字），标注\"暂无出处\"并说明原因\n- 审计要彻底——不要跳过任何数字，包括百分比、倍数、p-value、CI、std 等"
}
````

---

### Runtime record

_source line 2 · 2026-05-25T20:37:57.441Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-25T20:37:57.441Z",
  "sessionId": "4b680861-4da7-411a-8744-3dabfdaf2205"
}
```

---

## Round 1

123 recorded events

### User

_source line 3 · 2026-05-25T20:37:57.475Z_

&lt;project_context>
# 项目: turn_residual_gating

## 运行环境
- 服务器名: westd-20861
- SSH 连接命令: ssh connect.westd.seetacloud.com  # 必须用此命令，~/.ssh/config 自动应用密钥和跳板机，禁止用裸 IP
- 项目代码根目录: /root/turn_residual_gating


## 环境搭建
连接服务器后先调 `detect_image` 检测是否为预置镜像。如果匹配，跳过基础环境搭建，只装项目特有依赖。已预装的包不要重复安装。

## 输出风格
回复简洁直接。只输出执行结果和必要信息，不要解释过程、不要客套、不要给未被要求的建议。
&lt;/project_context>
## 任务：论文正文（body text）数据审计

对论文正文中的**每一个定量 claim**逐一验证，确保可追溯到 registry 实验记录。

### 论文文件位置
- 正文 tex 文件：`/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/`
  - `abstract.tex`
  - `introduction.tex`
  - `method.tex`
  - `experiments.tex`
  - `analysis.tex`
  - `discussion.tex`
  - `conclusion.tex`
  - `limitations.tex`
  - `related_work.tex`（包含 Table 1）
- included 表格：`/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/_project/paper/` 下的各种 `tab_*.tex`

### Registry 位置
用 `read_registry` 工具查询实验数据。关键实验 ID：
- `d048_final_ar_eval` — AR evaluation 主数据源
- `phase2_4way_eval_heldout` — Heldout TF evaluation
- `phase2_4way_eval` — IID TF evaluation
- `phase2_tg_s42_v7` — ThreadGate v7 训练
- `phase2_tg_s42_v9_pcgrad` — PCGrad 训练
- `phase2_ug_s42` — Uniform Gate 训练
- `mmlu_eval_all` — MMLU 评估
- `instruction_retention_test` — IR 测试
- `tab_statistical_tests` — 统计检验
- `p1_llama_ss_eval` — Llama SS 评估
- `p2_llama_gradient_conflict` — Llama 梯度分析
- `gradient_analysis` — Qwen 梯度分析
- `trc_baseline` — TRC baseline
- `eval_llama_ar_n20` — Llama AR eval
- `llama_eval_s42` — Llama TF eval

### 审计范围

逐文件、逐段落扫描，对每个数字做以下检查：

1. **Q1 准确性**：数字是否与 registry 记录一致？
2. **Q2 精度一致**：同一数字在不同位置的四舍五入是否一致？（重点！附录审计已发现 gap ratio 7.8× vs 7.9×、~1.3× vs 1.2× 不一致）
3. **Q3 跨章节一致性**：同一指标在 Abstract / Intro / Results / Analysis / Conclusion 各处是否完全一致？
4. **Q4 可追溯性**：每个数字能否追溯到具体的 exp_id？

### 重点关注

- **Abstract**：关键 claim 数字（gap 倍数、SS 改善、MMLU 保持等）
- **Introduction**：contribution 中引用的具体数字
- **Method**：超参（lr, batch, steps, 模型尺寸, 参数量 ~57K/<0.001%）、GAR 定义中的数学
- **Experiments**：每个结果段落的所有数字——GAR、PPL、gap ratio、p-value、effect size、CI
- **Analysis**：gate conditioning 数字、梯度分析数字、TRC 数字、cross-model 数字、1.5B 数字
- **Conclusion**：复述的数字是否与 Results 一致

### 已知问题（附录审计发现，正文中也需检查）

以下问题已在附录审计中发现，检查正文是否也存在：
- gap ratio：正文 7.8×（用 0.50/0.064）vs crossmodel 表 7.9×（用 0.504/0.064）
- SS gap：正文 ~1.3× vs 表 1.2×（精确值 1.24×）
- "≤1pp" 声明实际为 2pp
- PPL std ±0.001 实际 ±0.002

### 产出格式

写一份审计报告到 `/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/audit_body_text.md`，格式：

```markdown
# 正文数据审计报告

## 统计
- 总数字数：~N
- 已验证：~M
- 问题数：K

## 逐章节审计

### Abstract
| 数字 | Registry来源 | 状态 | 备注 |
...

### Introduction
...

（每个章节一个表格）

## 跨章节一致性检查
（同一数字在多处出现的交叉验证表）

## 问题清单
（编号、位置、问题描述、建议修正）

## 暂无出处的数字
（列出无法从 registry 追溯的数字及原因）
```

### 工作流程
1. `read_registry(project="turn_residual_gating", limit=0, fields=["*"])` 获取全部实验数据
2. 逐一 Read 每个 tex 文件
3. 对每个数字查 registry 验证
4. 编写审计报告
5. 特别注意跨章节一致性——建一张"关键数字出现位置"的交叉表

### 注意
- 不要修改任何 tex 文件，只做审计产出报告
- 对于无法从 registry 追溯的数字（如文献引用的数字、数学推导的数字），标注"暂无出处"并说明原因
- 审计要彻底——不要跳过任何数字，包括百分比、倍数、p-value、CI、std 等

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "8817af8a-f189-44e8-a462-1453a12b4ea3",
  "type": "user",
  "uuid": "136cf3aa-76f7-4818-a351-d623ca9c4078",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "4b680861-4da7-411a-8744-3dabfdaf2205",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-25T20:37:57.475Z_

```json
{
  "parentUuid": "136cf3aa-76f7-4818-a351-d623ca9c4078",
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
      "mcp__agent-ml-research__append_idea",
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__read_registry",
      "mcp__agent-ml-research__register_artifact",
      "mcp__agent-ml-research__save_project_file",
      "mcp__agent-ml-research__update_registry"
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
      "mcp__agent-ml-research__append_idea",
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__read_registry",
      "mcp__agent-ml-research__register_artifact",
      "mcp__agent-ml-research__save_project_file",
      "mcp__agent-ml-research__update_registry"
    ],
    "removedNames": []
  },
  "type": "attachment",
  "uuid": "d7382374-d8a5-4f1d-b4de-1da917d8fb95",
  "timestamp": "2026-05-25T20:37:57.475Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "4b680861-4da7-411a-8744-3dabfdaf2205",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

---

### Runtime record

_source line 5 · 2026-05-25T20:37:57.475Z_

```json
{
  "parentUuid": "d7382374-d8a5-4f1d-b4de-1da917d8fb95",
  "isSidechain": false,
  "attachment": {
    "type": "agent_listing_delta",
    "addedTypes": [
      "claude",
      "Explore",
      "general-purpose",
      "Plan",
      "statusline-setup"
    ],
    "addedLines": [
      "- claude: Catch-all for any task that doesn't fit a more specific agent. FleetView's default when no agent name is typed. (Tools: *)",
      "- Explore: Fast read-only search agent for locating code. Use it to find files by pattern (eg. \"src/components/**/*.tsx\"), grep for symbols or keywords (eg. \"API endpoints\"), or answer \"where is X defined / which files reference Y.\" Do NOT use it for code review, design-doc auditing, cross-file consistency checks, or open-ended analysis — it reads excerpts rather than whole files and will miss content past its read window. When calling, specify search breadth: \"quick\" for a single targeted lookup, \"medium\" for moderate exploration, or \"very thorough\" to search across multiple locations and naming conventions. (Tools: All tools except Agent, ExitPlanMode, Edit, Write, NotebookEdit)",
      "- general-purpose: General-purpose agent for researching complex questions, searching for code, and executing multi-step tasks. When you are searching for a keyword or file and are not confident that you will find the right match in the first few tries use this agent to perform the search for you. (Tools: *)",
      "- Plan: Software architect agent for designing implementation plans. Use this when you need to plan the implementation strategy for a task. Returns step-by-step plans, identifies critical files, and considers architectural trade-offs. (Tools: All tools except Agent, ExitPlanMode, Edit, Write, NotebookEdit)",
      "- statusline-setup: Use this agent to configure the user's Claude Code status line setting. (Tools: Read, Edit)"
    ],
    "removedTypes": [],
    "isInitial": true,
    "showConcurrencyNote": true
  },
  "type": "attachment",
  "uuid": "19baa84c-8ebb-49a1-b04a-c7e8582dedf6",
  "timestamp": "2026-05-25T20:37:57.475Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "4b680861-4da7-411a-8744-3dabfdaf2205",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

---

### Runtime record

_source line 6 · 2026-05-25T20:37:57.475Z_

```json
{
  "parentUuid": "19baa84c-8ebb-49a1-b04a-c7e8582dedf6",
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
  "uuid": "d45ffab0-d138-450f-91a7-868f6626e250",
  "timestamp": "2026-05-25T20:37:57.475Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "4b680861-4da7-411a-8744-3dabfdaf2205",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

---

### Runtime record

_source line 7 · 2026-05-25T20:37:57.475Z_

```json
{
  "parentUuid": "d45ffab0-d138-450f-91a7-868f6626e250",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "57b190fa-1049-4659-b43a-10e42a14c431",
  "timestamp": "2026-05-25T20:37:57.475Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "4b680861-4da7-411a-8744-3dabfdaf2205",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

---

### Runtime record

_source line 8_

```json
{
  "type": "ai-title",
  "aiTitle": "Audit quantitative claims in paper body text",
  "sessionId": "4b680861-4da7-411a-8744-3dabfdaf2205"
}
```

---

### Assistant

_source line 9 · 2026-05-25T20:38:00.260Z_

I'll start by loading the registry data and reading all the tex files in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "57b190fa-1049-4659-b43a-10e42a14c431",
  "isSidechain": false,
  "requestId": "req_011CbPvwKheQrq1652q9atcn",
  "type": "assistant",
  "uuid": "5f77d485-8a18-432a-8254-fb042b61d135",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "4b680861-4da7-411a-8744-3dabfdaf2205",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MAWtZAgLTZ7ehjMcbYn93C",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14954,
      "cache_read_input_tokens": 11447,
      "output_tokens": 104,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 14954,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 104,
          "cache_read_input_tokens": 11447,
          "cache_creation_input_tokens": 14954,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 14954
          },
          "type": "message"
        }
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

_source line 10 · 2026-05-25T20:38:01.062Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01VhpMjQjPYVcrE72BkAJU8z`</summary>

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
  "parentUuid": "5f77d485-8a18-432a-8254-fb042b61d135",
  "isSidechain": false,
  "requestId": "req_011CbPvwKheQrq1652q9atcn",
  "type": "assistant",
  "uuid": "584c97e7-95f0-4b1a-b5e4-2ebdad414c2b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "4b680861-4da7-411a-8744-3dabfdaf2205",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MAWtZAgLTZ7ehjMcbYn93C",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14954,
      "cache_read_input_tokens": 11447,
      "output_tokens": 104,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 14954,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 104,
          "cache_read_input_tokens": 11447,
          "cache_creation_input_tokens": 14954,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 14954
          },
          "type": "message"
        }
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

_source line 11 · 2026-05-25T20:38:01.081Z_

<details><summary>↩ Tool result · `toolu_01VhpMjQjPYVcrE72BkAJU8z`</summary>

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
  "parentUuid": "584c97e7-95f0-4b1a-b5e4-2ebdad414c2b",
  "isSidechain": false,
  "promptId": "8817af8a-f189-44e8-a462-1453a12b4ea3",
  "type": "user",
  "uuid": "890b1c83-a6cd-4671-8f03-9e1ec42001fb",
  "toolUseResult": {
    "matches": [
      "mcp__agent-ml-research__read_registry"
    ],
    "query": "select:mcp__agent-ml-research__read_registry",
    "total_deferred_tools": 25
  },
  "sourceToolAssistantUUID": "584c97e7-95f0-4b1a-b5e4-2ebdad414c2b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "4b680861-4da7-411a-8744-3dabfdaf2205",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 12 · 2026-05-25T20:38:03.335Z_

<details><summary>Logged reasoning block</summary>

```text
Let me fetch the registry data and read all the tex files in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "890b1c83-a6cd-4671-8f03-9e1ec42001fb",
  "isSidechain": false,
  "requestId": "req_011CbPvwbVfNQCwbcnsYNfCu",
  "type": "assistant",
  "uuid": "886f9d0e-600c-4379-aa22-48fbfdc4d928",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "4b680861-4da7-411a-8744-3dabfdaf2205",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014omTEWaQWBnZwZbaHNXrM6",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 466,
      "cache_read_input_tokens": 26401,
      "output_tokens": 785,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 466,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 785,
          "cache_read_input_tokens": 26401,
          "cache_creation_input_tokens": 466,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 466
          },
          "type": "message"
        }
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

_source line 13 · 2026-05-25T20:38:03.820Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_016dq8NSy8wV8b5G7fK2Czwi`</summary>

```json
{
  "project": "turn_residual_gating",
  "limit": 0,
  "fields": [
    "*"
  ]
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "886f9d0e-600c-4379-aa22-48fbfdc4d928",
  "isSidechain": false,
  "requestId": "req_011CbPvwbVfNQCwbcnsYNfCu",
  "type": "assistant",
  "uuid": "6d8da05e-bd62-45a5-b18b-47925df8341a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "4b680861-4da7-411a-8744-3dabfdaf2205",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014omTEWaQWBnZwZbaHNXrM6",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 466,
      "cache_read_input_tokens": 26401,
      "output_tokens": 785,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 466,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 785,
          "cache_read_input_tokens": 26401,
          "cache_creation_input_tokens": 466,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 466
          },
          "type": "message"
        }
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

_source line 14 · 2026-05-25T20:38:04.261Z_

<details open><summary>🔧 Tool call — Read · `toolu_018knEN2Q5qeZ3Us2sQprXnf`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6d8da05e-bd62-45a5-b18b-47925df8341a",
  "isSidechain": false,
  "requestId": "req_011CbPvwbVfNQCwbcnsYNfCu",
  "type": "assistant",
  "uuid": "69d5e85b-8b09-44ea-b36b-30cddf67c0fc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "4b680861-4da7-411a-8744-3dabfdaf2205",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014omTEWaQWBnZwZbaHNXrM6",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 466,
      "cache_read_input_tokens": 26401,
      "output_tokens": 785,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 466,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 785,
          "cache_read_input_tokens": 26401,
          "cache_creation_input_tokens": 466,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 466
          },
          "type": "message"
        }
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

_source line 15 · 2026-05-25T20:38:08.579Z_

<details><summary>↩ Tool result · `toolu_01XUiaw5NMrjBb1C8DVVtmtk`</summary>

```text
1	\section{Related Work}\label{sec:related}
2	
3	\paragraph{Multi-turn dialogue and attention decay.}
4	Multi-turn coherence has been a persistent challenge from early dialogue systems \citep{li2016persona,roller2021recipes,zhang2020dialogpt} through modern long-context models \citep{xu2022goldfish}, with benchmarks such as MT-Bench \citep{zheng2024judging} and MT-Bench-101 \citep{bai2024mtbench101} continuing to expose quality gaps at later turns \citep{laban2025lost,liu2026intent}. Most relevant to our work, \citet{dongre2026attention} defined the Goal Accessibility Ratio (GAR) and showed that attention to goal tokens decays 27--48\% across 12 models while residual probes retain goal information (AUC\,=\,0.98). We observe a steeper 70.8\% decline on Qwen-2.5-7B. \citet{li2024measuring} independently quantified instruction instability and proposed split-softmax as an inference-time remedy. Our work differs in scope: we diagnose \emph{why} training-time attention optimization fails to transfer to inference, and provide the first training-time mitigation.
5	
6	\paragraph{Gating and attention manipulation.}
7	Residual gating spans highway networks \citep{srivastava2015highway}, ReZero \citep{bachlechner2021rezero}, layer pruning \citep{gromov2024unreasonable,fan2020layerdrop}, and adaptive depth \citep{schuster2022calm,raposo2024mixture}. Most relevant is Gated Attention \citep{qiu2025gated}: per-head sigmoid gates achieving MMLU \citep{hendrycks2021measuring} $+$2.03 at 15B scale; ThreadGate differs in conditioning on turn position. On the analysis side, head specialization \citep{clark2019what,voita2019analyzing,kovaleva2019revealing}, positional bias calibration \citep{liu2024lost,xiao2024streaming}, and attention steering (PASTA; \citealp{zhang2024tell}) address inference behavior; our $\beta$-steering serves a diagnostic role. PCGrad \citep{yu2020pcgrad} and CAGrad \citep{liu2021cagrad} treat gradient conflict as the root cause; we show direction conflict is a symptom, not the primary cause.
8	
9	\paragraph{Exposure bias in sequence models.}
10	Teacher forcing creates a distributional mismatch between training and inference \citep{wiseman2016sequence,arora2022exposure}. Scheduled sampling \citep{bengio2015scheduled} introduced curriculum-based mixing; subsequent work proposed sequence-level objectives \citep{ranzato2016sequence}, adversarial regularization \citep{lamb2016professor}, self-recovery analysis \citep{he2019exposure}, bridging strategies for neural machine translation (NMT; \citealp{zhang2019bridging}), and search-based training \citep{leblond2018searnn}. \citet{mihaylova2019scheduled} extended scheduled sampling to transformers for single-turn NMT. \citet{dou2019attention} proposed attention forcing (supervising cross-attention during NMT), and \citet{dou2022parallel} extended it with KL-divergence switching. Our work differs: (i)~time-scheduled sampling (linearly increasing $\rho$), not data-dependent; (ii)~self-attention in multi-turn dialogue, not cross-attention in NMT; (iii)~auxiliary attention objectives, not primary translation loss. No prior work examines exposure bias on \emph{auxiliary} attention objectives or provides multi-turn transformer mitigation; we fill both gaps.
11	
12	\begin{table*}[!t]
13	\centering
14	\small
15	\caption{Five-way comparison on Qwen-2.5-7B-Instruct. TF evaluation uses IID UltraChat and 50 held-out conversations; AR evaluation uses $N$\,=\,50 held-out conversations (mean 3.6 user turns). All fine-tuned variants converge under TF ($\leq$2\,pp spread); the 8--17$\times$ TF-AR gap persists across all configurations. $\bar{g}\!\pm\!\sigma_g$: learned gate mean and std across 28 layers (LoRA-only has no gates). GAR-O = GAR-ours; GAR-D = GAR-Dongre \citep{dongre2026attention}.}
16	\label{tab:five-way}
17	\begin{tabular}{l ccc ccc cc c}
18	\toprule
19	& \multicolumn{3}{c}{\textbf{IID (TF)}} & \multicolumn{3}{c}{\textbf{Held-out (TF)}} & \multicolumn{2}{c}{\textbf{AR ($N$\,=\,50)}} & \\
20	\cmidrule(lr){2-4} \cmidrule(lr){5-7} \cmidrule(lr){8-9}
21	\textbf{Configuration} & GAR-O & GAR-D & PPL & GAR-O & GAR-D & PPL & GAR-O & 95\% CI & $\bar{g}\!\pm\!\sigma_g$ \\
22	\midrule
23	\multicolumn{10}{l}{\emph{Baseline}} \\
24	Base              & 0.01 & 0.00 & 4.23 & 0.01 & 0.00 & 4.34 & 0.019 & {\scriptsize[.014,\,.024]} & --- \\
25	\midrule
26	\multicolumn{10}{l}{\emph{Gated variants}} \\
27	ThreadGate        & 0.50 & \textbf{0.02} & 2.78 & 0.50 & \textbf{0.02} & 2.78 & \textbf{0.064} & {\scriptsize[.041,\,.091]} & .93\,{\scriptsize$\pm$\,.05} \\
28	\;+\,PCGrad       & 0.50 & 0.01 & 2.78 & 0.50 & 0.01 & 2.78 & 0.030 & {\scriptsize[.023,\,.038]} & --- \\
29	Uniform Gate      & 0.49 & 0.01 & 2.78 & \textbf{0.51} & 0.01 & 2.78 & 0.033 & {\scriptsize[.025,\,.043]} & .96\,{\scriptsize$\pm$\,.05} \\
30	\midrule
31	\multicolumn{10}{l}{\emph{Ungated}} \\
32	LoRA-only         & 0.50 & 0.01 & 2.78 & 0.50 & 0.01 & 2.78 & 0.037 & {\scriptsize[.027,\,.050]} & 1.00 \\
33	\bottomrule
34	\end{tabular}
35	\end{table*}
36	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a562e8fe-317f-4bc6-895c-1b46d065b5fa",
  "isSidechain": false,
  "promptId": "8817af8a-f189-44e8-a462-1453a12b4ea3",
  "type": "user",
  "uuid": "42459c76-db1f-4537-ba53-528bcaf3e4da",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/related_work.tex",
      "content": "\\section{Related Work}\\label{sec:related}\n\n\\paragraph{Multi-turn dialogue and attention decay.}\nMulti-turn coherence has been a persistent challenge from early dialogue systems \\citep{li2016persona,roller2021recipes,zhang2020dialogpt} through modern long-context models \\citep{xu2022goldfish}, with benchmarks such as MT-Bench \\citep{zheng2024judging} and MT-Bench-101 \\citep{bai2024mtbench101} continuing to expose quality gaps at later turns \\citep{laban2025lost,liu2026intent}. Most relevant to our work, \\citet{dongre2026attention} defined the Goal Accessibility Ratio (GAR) and showed that attention to goal tokens decays 27--48\\% across 12 models while residual probes retain goal information (AUC\\,=\\,0.98). We observe a steeper 70.8\\% decline on Qwen-2.5-7B. \\citet{li2024measuring} independently quantified instruction instability and proposed split-softmax as an inference-time remedy. Our work differs in scope: we diagnose \\emph{why} training-time attention optimization fails to transfer to inference, and provide the first training-time mitigation.\n\n\\paragraph{Gating and attention manipulation.}\nResidual gating spans highway networks \\citep{srivastava2015highway}, ReZero \\citep{bachlechner2021rezero}, layer pruning \\citep{gromov2024unreasonable,fan2020layerdrop}, and adaptive depth \\citep{schuster2022calm,raposo2024mixture}. Most relevant is Gated Attention \\citep{qiu2025gated}: per-head sigmoid gates achieving MMLU \\citep{hendrycks2021measuring} $+$2.03 at 15B scale; ThreadGate differs in conditioning on turn position. On the analysis side, head specialization \\citep{clark2019what,voita2019analyzing,kovaleva2019revealing}, positional bias calibration \\citep{liu2024lost,xiao2024streaming}, and attention steering (PASTA; \\citealp{zhang2024tell}) address inference behavior; our $\\beta$-steering serves a diagnostic role. PCGrad \\citep{yu2020pcgrad} and CAGrad \\citep{liu2021cagrad} treat gradient conflict as the root cause; we show direction conflict is a symptom, not the primary cause.\n\n\\paragraph{Exposure bias in sequence models.}\nTeacher forcing creates a distributional mismatch between training and inference \\citep{wiseman2016sequence,arora2022exposure}. Scheduled sampling \\citep{bengio2015scheduled} introduced curriculum-based mixing; subsequent work proposed sequence-level objectives \\citep{ranzato2016sequence}, adversarial regularization \\citep{lamb2016professor}, self-recovery analysis \\citep{he2019exposure}, bridging strategies for neural machine translation (NMT; \\citealp{zhang2019bridging}), and search-based training \\citep{leblond2018searnn}. \\citet{mihaylova2019scheduled} extended scheduled sampling to transformers for single-turn NMT. \\citet{dou2019attention} proposed attention forcing (supervising cross-attention during NMT), and \\citet{dou2022parallel} extended it with KL-divergence switching. Our work differs: (i)~time-scheduled sampling (linearly increasing $\\rho$), not data-dependent; (ii)~self-attention in multi-turn dialogue, not cross-attention in NMT; (iii)~auxiliary attention objectives, not primary translation loss. No prior work examines exposure bias on \\emph{auxiliary} attention objectives or provides multi-turn transformer mitigation; we fill both gaps.\n\n\\begin{table*}[!t]\n\\centering\n\\small\n\\caption{Five-way comparison on Qwen-2.5-7B-Instruct. TF evaluation uses IID UltraChat and 50 held-out conversations; AR evaluation uses $N$\\,=\\,50 held-out conversations (mean 3.6 user turns). All fine-tuned variants converge under TF ($\\leq$2\\,pp spread); the 8--17$\\times$ TF-AR gap persists across all configurations. $\\bar{g}\\!\\pm\\!\\sigma_g$: learned gate mean and std across 28 layers (LoRA-only has no gates). GAR-O = GAR-ours; GAR-D = GAR-Dongre \\citep{dongre2026attention}.}\n\\label{tab:five-way}\n\\begin{tabular}{l ccc ccc cc c}\n\\toprule\n& \\multicolumn{3}{c}{\\textbf{IID (TF)}} & \\multicolumn{3}{c}{\\textbf{Held-out (TF)}} & \\multicolumn{2}{c}{\\textbf{AR ($N$\\,=\\,50)}} & \\\\\n\\cmidrule(lr){2-4} \\cmidrule(lr){5-7} \\cmidrule(lr){8-9}\n\\textbf{Configuration} & GAR-O & GAR-D & PPL & GAR-O & GAR-D & PPL & GAR-O & 95\\% CI & $\\bar{g}\\!\\pm\\!\\sigma_g$ \\\\\n\\midrule\n\\multicolumn{10}{l}{\\emph{Baseline}} \\\\\nBase              & 0.01 & 0.00 & 4.23 & 0.01 & 0.00 & 4.34 & 0.019 & {\\scriptsize[.014,\\,.024]} & --- \\\\\n\\midrule\n\\multicolumn{10}{l}{\\emph{Gated variants}} \\\\\nThreadGate        & 0.50 & \\textbf{0.02} & 2.78 & 0.50 & \\textbf{0.02} & 2.78 & \\textbf{0.064} & {\\scriptsize[.041,\\,.091]} & .93\\,{\\scriptsize$\\pm$\\,.05} \\\\\n\\;+\\,PCGrad       & 0.50 & 0.01 & 2.78 & 0.50 & 0.01 & 2.78 & 0.030 & {\\scriptsize[.023,\\,.038]} & --- \\\\\nUniform Gate      & 0.49 & 0.01 & 2.78 & \\textbf{0.51} & 0.01 & 2.78 & 0.033 & {\\scriptsize[.025,\\,.043]} & .96\\,{\\scriptsize$\\pm$\\,.05} \\\\\n\\midrule\n\\multicolumn{10}{l}{\\emph{Ungated}} \\\\\nLoRA-only         & 0.50 & 0.01 & 2.78 & 0.50 & 0.01 & 2.78 & 0.037 & {\\scriptsize[.027,\\,.050]} & 1.00 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table*}\n",
      "numLines": 36,
      "startLine": 1,
      "totalLines": 36
    }
  },
  "sourceToolAssistantUUID": "a562e8fe-317f-4bc6-895c-1b46d065b5fa",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "4b680861-4da7-411a-8744-3dabfdaf2205",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-25T20:38:04.348Z_

<details><summary>↩ Tool result · `toolu_016dq8NSy8wV8b5G7fK2Czwi`</summary>

```text
Error: result (98,179 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-11-projects-turn-residual-gating/4b680861-4da7-411a-8744-3dabfdaf2205/tool-results/mcp-agent-ml-research-read_registry-1779741484333.txt.
Format: JSON with schema: {result: string}
- For targeted queries (find a value, filter by field): use jq on the file directly.
- For analysis or summarization that requires reading the full content: first probe the structure (e.g., jq 'type, length, keys?' /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-11-projects-turn-residual-gating/4b680861-4da7-411a-8744-3dabfdaf2205/tool-results/mcp-agent-ml-research-read_registry-1779741484333.txt), then extract slices with jq or python — Read's line-based offset/limit will not chunk this file.
- If the Agent tool is available, do this inside a subagent so the full output stays out of your main context. Give it the instruction above verbatim, and be explicit about what it must return — e.g. "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-11-projects-turn-residual-gating/4b680861-4da7-411a-8744-3dabfdaf2205/tool-results/mcp-agent-ml-research-read_registry-1779741484333.txt is JSON with schema: {result: string}; probe the structure with jq (type/length/keys), then extract and read the content in full with jq or python, then summarize and quote any key findings verbatim." A vague "summarize this" may lose detail.

```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6d8da05e-bd62-45a5-b18b-47925df8341a",
  "isSidechain": false,
  "promptId": "8817af8a-f189-44e8-a462-1453a12b4ea3",
  "type": "user",
  "uuid": "b75e5306-e2f6-4a9a-b877-925fda2fa172",
  "toolUseResult": "Error: result (98,179 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-11-projects-turn-residual-gating/4b680861-4da7-411a-8744-3dabfdaf2205/tool-results/mcp-agent-ml-research-read_registry-1779741484333.txt.\nFormat: JSON with schema: {result: string}\n- For targeted queries (find a value, filter by field): use jq on the file directly.\n- For analysis or summarization that requires reading the full content: first probe the structure (e.g., jq 'type, length, keys?' /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-11-projects-turn-residual-gating/4b680861-4da7-411a-8744-3dabfdaf2205/tool-results/mcp-agent-ml-research-read_registry-1779741484333.txt), then extract slices with jq or python — Read's line-based offset/limit will not chunk this file.\n- If the Agent tool is available, do this inside a subagent so the full output stays out of your main context. Give it the instruction above verbatim, and be explicit about what it must return — e.g. \"/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-11-projects-turn-residual-gating/4b680861-4da7-411a-8744-3dabfdaf2205/tool-results/mcp-agent-ml-research-read_registry-1779741484333.txt is JSON with schema: {result: string}; probe the structure with jq (type/length/keys), then extract and read the content in full with jq or python, then summarize and quote any key findings verbatim.\" A vague \"summarize this\" may lose detail.\n",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {\"phase1a_multiseed_qwen\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-25T06:15:26.051Z\", \"updated_at\": \"2026-05-25T11:20:34.089Z\", \"hypothesis\": \"Multi-seed (s123, s456) training across 5 Qwen conditions (PCGrad, UG, LoRA-only, TG, SS) to establish mean±std for all claims. 8 training runs + AR eval N≥50 each. Expect TF convergence (GAR~0.50) and consistent AR rankings across seeds.\", \"spec\": {\"command\": \"python src/train_phase2_v9_pcgrad.py\", \"server\": \"westd-20861\", \"data_path\": \"data/ultrachat_8k\", \"data_count\": 8000, \"model_name\": \"Qwen2.5-7B-Instruct\", \"seed\": 123, \"checkpoint_path\": \"N/A\", \"log_path\": \"runs/d048_pcgrad_s123\"}, \"conclusion\": \"killed\", \"notes\": \"用户要求停止：30min 内无法完成。PCGrad s123 在 1800/3000 步时被终止，后续 7 个排队任务全部取消。\", \"checkpoint_path\": \"N/A\", \"log_path\": \"runs/d048_pcgrad_s123\", \"completed_at\": \"2026-05-25T11:20:34.089Z\"}, \"p1_ss_lora_only\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-25T08:58:41.419Z\", \"updated_at\": \"2026-05-25T09:42:22.185Z\", \"hypothesis\": \"SS training on LoRA-only checkpoint (no ThreadGate) with same hyperparameters (rho_max=0.3, same schedule) should achieve similar GAR improvement as SS+TG. If confirmed, this proves the SS fix is architecture-agnostic, strengthening the paper's mitigation story (the gap is caused by exposure bias in any auxiliary-loss setup, and SS fixes it regardless of gating mechanism).\", \"spec\": {\"command\": \"bash /root/turn_residual_gating/scripts/d048_ss_lo_s42.sh\", \"server\": \"westd-20861\", \"data_path\": \"/root/turn-residual-gating/data/phase2_train.jsonl\", \"data_count\": 2000, \"model_name\": \"Qwen/Qwen2.5-7B-Instruct\", \"seed\": 42, \"notes\": \"SS+LoRA-only (gate_type=none, ss_max_ratio=0.3). From-scratch training, not resume. Auto TF+AR eval after training. ~6.5h training + eval.\"}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-25T09:42:22.185Z\"}, \"phase2_switching\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-25T08:58:40.187Z\", \"updated_at\": \"2026-05-25T09:42:21.391Z\", \"hypothesis\": \"TF→AR switching at turn k (k=1..5) on ThreadGate s42 checkpoint. If GAR drops abruptly at the switch point (matching pure-AR level within 1 turn), it confirms exposure bias as instantaneous distribution shift rather than gradual KV cache drift. Staircase = exposure bias dominant; linear slope = KV drift dominant.\", \"conclusion\": \"killed\", \"completed_at\": \"2026-05-25T09:42:21.391Z\"}, \"phase2_tf_ar_switching\": {\"status\": \"QUEUED\", \"retry_count\": 0, \"created_at\": \"2026-05-25T06:15:36.221Z\", \"updated_at\": \"2026-05-25T06:45:27.338Z\", \"hypothesis\": \"TF→AR switching at turn k (k=1..5) on ThreadGate s42 checkpoint. If GAR drops abruptly at the switch point (matching pure-AR level within 1 turn), it confirms exposure bias as instantaneous distribution shift rather than gradual cumulative drift.\"}, \"phase1a_multiseed_8runs\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-25T06:18:08.953Z\", \"updated_at\": \"2026-05-25T06:18:08.953Z\", \"spec\": {\"command\": \"bash -c \\\"bash /root/turn_residual_gating/scripts/phase1a_multiseed_runner.sh\\\"\", \"server\": \"westd-20861\", \"gpu\": [\"cuda:0\"], \"pid\": \"5508\", \"log_path\": \"~/runs/turn_residual_gating/phase1a_multiseed_8runs.log\", \"submitted_at\": \"2026-05-25T06:18:08.495Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}}, \"phase1b_llama_complement\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-25T06:15:34.729Z\", \"updated_at\": \"2026-05-25T06:15:44.322Z\", \"hypothesis\": \"Llama PCGrad + UG (s42) to complete cross-model comparison matrix. If Llama PCGrad also fails to improve AR GAR (like Qwen), it strengthens the cross-architecture causal exclusion of gradient conflict.\"}, \"p1_llama_ss_eval\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-24T15:53:29.650Z\", \"updated_at\": \"2026-05-24T17:12:44.175Z\", \"hypothesis\": \"Llama SS (2-epoch) reduces the TF-AR GAR gap on Llama-3.1-8B, confirming SS as model-general mitigation (C4+C5). Eval: TF+AR N=50 β=0/3/5.\", \"spec\": {\"command\": \"bash scripts/p1_llama_ss_eval.sh\", \"server\": \"westd-20861\", \"data_path\": \"/root/turn-residual-gating/data/eval_50.json\", \"data_count\": 50, \"model_name\": \"meta-llama/Llama-3.1-8B-Instruct\", \"seed\": 42, \"checkpoint_source\": \"runs/p1_llama_ss_s42/epoch_1/\", \"log_path\": \"runs/p1_llama_ss_eval.log\", \"pid\": 178624, \"checkpoint_path\": \"results/llama_ss_eval/\"}, \"conclusion\": \"success\", \"metrics\": {\"ss_tf_gar\": 0.477, \"ss_tf_ppl\": 2.82, \"ss_ar_b0_gar\": 0.1662, \"ss_ar_b0_ppl\": 1.37, \"ss_ar_b5_gar\": 0.7905, \"ss_ar_b5_ppl\": 1.81, \"base_ar_gar\": 0.0179, \"base_ar_ppl\": 1.22, \"tf_ar_gap\": 2.87}, \"completed_at\": \"2026-05-24T17:12:44.175Z\"}, \"p1_llama_ss_training\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-23T19:37:48.689Z\", \"updated_at\": \"2026-05-24T15:53:21.654Z\", \"hypothesis\": \"SS is effective on Qwen (gap 8x to 1.4x). If SS also reduces the TF-AR gap on Llama-3.1-8B, it confirms SS as a model-general mitigation, strengthening C4 (mitigation) and C5 (cross-model) claims.\", \"spec\": {\"command\": \"bash scripts/p1_llama_ss_train.sh\", \"server\": \"westd-20861\", \"data_path\": \"/root/turn-residual-gating/data/train_400.json\", \"data_count\": 400, \"model_name\": \"meta-llama/Llama-3.1-8B-Instruct\", \"seed\": 42, \"checkpoint_path\": \"runs/llama_ss_s42/\", \"log_path\": \"logs/p1_llama_ss_training.log\", \"pid\": 158507, \"hyperparams\": {\"lr\": \"2e-4\", \"batch_size\": 1, \"grad_accum\": 8, \"epochs\": 3, \"ss_max_ratio\": 0.3, \"lora_rank\": 16}}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-24T15:53:21.654Z\"}, \"mmlu_eval_all\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-23T06:45:04.153Z\", \"updated_at\": \"2026-05-24T07:23:08.289Z\", \"hypothesis\": \"ThreadGate's per-layer gating and auxiliary GAR loss do not degrade the model's general language understanding capabilities. All fine-tuned variants (TG/UG/LO/PCGrad/SS) should maintain MMLU 5-shot accuracy within 1pp of the Base LoRA-only checkpoint, confirming that attention steering is additive rather than destructive.\", \"spec\": {\"command\": \"python eval_mmlu.py --model_path &lt;checkpoint> --n_shot 5\", \"server\": \"westd-20861\", \"data_path\": \"MMLU benchmark (5-shot)\", \"data_count\": 14042, \"model_name\": \"Qwen/Qwen2.5-7B-Instruct\", \"seed\": 42, \"checkpoint_source\": \"base/lo/ug/tg/pcgrad/ss checkpoints\", \"eval_data\": \"MMLU 5-shot\", \"checkpoint_path\": \"results/mmlu/\", \"log_path\": \"logs/gpu_chain_next.log\"}, \"conclusion\": \"success\", \"metrics\": {\"base_qwen\": 0.7423, \"pcgrad_v9_s42\": 0.7386, \"ss_v8b_s42\": 0.7375, \"lo_s42\": 0.7357, \"tg_v7_s42\": 0.7347, \"ug_s42\": 0.7346}, \"completed_at\": \"2026-05-24T06:53:52.873Z\"}, \"p2_llama_gradient_conflict\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-23T19:37:50.492Z\", \"updated_at\": \"2026-05-24T07:20:28.248Z\", \"hypothesis\": \"PCGrad fails to improve AR GAR on Llama-3.1-8B (as on Qwen), confirming cross-model that gradient conflict is not the root cause of the TF-AR gap, strengthening C2 (causal exclusion).\", \"spec\": {\"command\": \"bash scripts/p2_llama_gradient_conflict.sh\", \"server\": \"westd-20861\", \"data_path\": \"/root/turn-residual-gating/data/train_400.json\", \"data_count\": 400, \"model_name\": \"meta-llama/Llama-3.1-8B-Instruct\", \"seed\": 42, \"checkpoint_path\": \"results/p2_llama_gradient_conflict/\", \"log_path\": \"logs/p2_llama_gradient_conflict.log\"}, \"conclusion\": \"success\", \"metrics\": {\"cos_sim_mean\": 0.0045, \"cos_sim_std\": 0.07, \"neg_cos_sim_layers_pct\": 53.1, \"mag_ratio_median\": 25.7, \"conclusion_note\": \"cos_sim≈0 indicates near-orthogonal (NOT conflict). Script conclusion text 'widespread conflict' is misleading — actual finding: NTP and GAR gradients are nearly orthogonal on Llama, consistent with Qwen pattern.\"}, \"completed_at\": \"2026-05-24T07:20:28.248Z\"}, \"p1_tf_ar_kl_divergence\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-23T19:37:46.355Z\", \"updated_at\": \"2026-05-24T07:18:10.268Z\", \"hypothesis\": \"TF and AR attention distributions diverge more on GAR-relevant heads (high gate values) than non-relevant heads, providing mechanistic evidence that exposure bias selectively disrupts goal-attending computation rather than uniformly degrading attention.\", \"metrics\": {\"tg_delta_gar\": 0.0165, \"base_delta_gar\": 0.0122, \"tg_mean_kl\": 0.054, \"base_mean_kl\": 0.043, \"gate_kl_correlation\": 0.11, \"high_kl_layers\": \"L23-L27, L9\", \"gar_robustness_ours_tg_base_ratio\": 21.4, \"gar_robustness_goal_only_ratio\": 63, \"gar_robustness_ours_all_ratio\": 1.7, \"gar_robustness_ours_first_ratio\": 1.8}, \"spec\": {\"command\": \"python scripts/p1_kl_divergence.py\", \"server\": \"westd-20861\", \"data_path\": \"/root/turn_residual_gating/data/eval_200.json\", \"data_count\": 30, \"model_name\": \"Qwen/Qwen2.5-7B-Instruct\", \"seed\": 42, \"checkpoint_path\": \"results/p1_kl_perhead/\", \"log_path\": \"logs/p1_kl_divergence_step2.log\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-24T07:18:06.521Z\"}, \"qwen15b_phase1_diag\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-23T06:44:59.895Z\", \"updated_at\": \"2026-05-24T06:53:23.496Z\", \"hypothesis\": \"GAR attention decay toward system-prompt goal tokens is a general phenomenon across model scales, not specific to 7B. Qwen-2.5-1.5B-Instruct should also show progressive GAR decline across conversation turns, confirming the phenomenon is architecture-level rather than scale-dependent.\", \"spec\": {\"command\": \"python train_phase2.py --model Qwen/Qwen2.5-1.5B-Instruct --config configs/tg_v7.yaml --seed 42 --epochs 3\", \"server\": \"westd-20861\", \"data_path\": \"/root/turn-residual-gating/data/train_400.json\", \"data_count\": 400, \"model_name\": \"Qwen/Qwen2.5-1.5B-Instruct\", \"seed\": 42, \"checkpoint_path\": \"runs/qwen15b_tg_v7_s42/\", \"log_path\": \"logs/qwen15b_phase1_diag.log\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-24T06:53:23.496Z\"}, \"d048_eval_ss_s456\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-24T00:38:41.913Z\", \"updated_at\": \"2026-05-24T01:19:46.692Z\", \"hypothesis\": \"SS s456 eval: TF + AR N=50 + bootstrap CI to complete 3-seed SS metrics. Together with s42 and s123, establishes mean±std for C2 reviewer requirement.\", \"parent\": \"d048_ss_s456\", \"spec\": {\"command\": \"bash scripts/d048_eval_ss_s456.sh\", \"server\": \"westd-20861\", \"pid\": \"129280\", \"data_path\": \"/root/turn-residual-gating/data/eval_200/eval_200.json\", \"data_count\": 200, \"model_name\": \"Qwen/Qwen2.5-7B-Instruct + SS s456 LoRA\", \"seed\": 456, \"gpu\": 0, \"checkpoint_source\": \"/root/turn-residual-gating/runs/d048_ss_s456/epoch_2\", \"eval_data\": \"/root/turn-residual-gating/data/eval_200/eval_200.json\", \"checkpoint_path\": \"/root/turn-residual-gating/results/d048_final_ar/\", \"log_path\": \"/root/turn-residual-gating/results/d048_final_ar/\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-24T01:19:43.693Z\", \"metrics\": {\"tf_gar_ours_mid\": 0.4964, \"tf_gar_dongre_mid\": 0.3862, \"ar_beta0_gar\": 0.4325, \"ar_beta0_ppl\": 1.4394, \"ar_beta3_gar\": 0.605, \"ar_beta3_ppl\": 1.5868, \"ar_beta5_gar\": 0.7157, \"ar_beta5_ppl\": 1.8045, \"n_convs_ar\": 50}}, \"d048_ss_s456\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-23T03:46:14.558Z\", \"updated_at\": \"2026-05-24T00:38:35.393Z\", \"hypothesis\": \"Scheduled sampling (ratio=0.3) with ThreadGate multi-seed (s456) to establish 3-seed mean±std for C2 reviewer requirement of at least 3 seeds\", \"parent\": \"d048_ss_s42\", \"spec\": {\"command\": \"python train_phase2_v8b.py --seed 456 --resume runs/d048_ss_s456/epoch_0 --gate-type threadgate --lr 2e-4 --epochs 3 --batch-size 1 --grad-accum 8 --ss-ratio 0.3\", \"server\": \"westd-20861\", \"pid\": \"112418\", \"data_path\": \"/root/turn-residual-gating/data/phase2_train.jsonl\", \"data_count\": 2000, \"model_name\": \"Qwen/Qwen2.5-7B-Instruct\", \"seed\": 456, \"gpu\": 0, \"checkpoint_source\": \"Qwen/Qwen2.5-7B-Instruct (resume from epoch_0)\", \"eval_data\": \"N/A - training experiment\", \"checkpoint_path\": \"/root/turn-residual-gating/runs/d048_ss_s456/epoch_2\", \"log_path\": \"/root/turn-residual-gating/runs/d048_ss_s456/train.log\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-24T00:38:35.393Z\"}, \"p0_ss_steering_eval\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-23T19:37:39.883Z\", \"updated_at\": \"2026-05-23T19:57:38.851Z\", \"hypothesis\": \"SS training provides AR GAR ~0.385, steering alone gives 0.717. Combining SS checkpoint with beta-steering at inference may approach TF parity (~0.50), demonstrating that SS+steering is a constructive mitigation stack for the TF-AR gap.\", \"parent\": \"d048_eval_ss_s42\", \"conclusion\": \"killed\", \"notes\": \"Cancelled: ss_s42_ar_n50.json already contains SS+steering data at β=0,3,5. Results show SS and steering do not stack (β=5: SS 0.717 vs TG-only 0.727). Director decision: skip, use existing data.\"}, \"d048_eval_ss_s123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-23T17:29:13.803Z\", \"updated_at\": \"2026-05-23T18:05:41.813Z\", \"hypothesis\": \"SS s123 eval: TF + AR N=50 + bootstrap CI to establish multi-seed SS metrics. Expect TF GAR ~0.50, AR GAR similar to s42 (0.347), confirming SS effectiveness across seeds.\", \"parent\": \"d048_ss_s123\", \"spec\": {\"command\": \"bash scripts/d048_eval_ss_s123.sh\", \"server\": \"westd-20861\", \"pid\": \"110052\", \"data_path\": \"/root/turn-residual-gating/data/eval_200/eval_200.json\", \"data_count\": 200, \"model_name\": \"Qwen/Qwen2.5-7B-Instruct + SS s123 LoRA\", \"seed\": 123, \"gpu\": 0, \"checkpoint_source\": \"/root/turn-residual-gating/runs/d048_ss_s123/epoch_2\", \"eval_data\": \"/root/turn-residual-gating/data/eval_200/eval_200.json\", \"checkpoint_path\": \"/root/turn-residual-gating/results/d048_final_ar/\", \"log_path\": \"/root/turn-residual-gating/results/d048_final_ar/\"}, \"notes\": \"Cron误判修复: 原PID 109385是TF eval子进程,退出后cron 5次检测失败auto-resolved为failed。实际AR eval PID 110052仍在运行。已手动恢复RUNNING。\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-23T18:05:35.103Z\", \"metrics\": {\"tf_gar_ours\": 0.5536, \"tf_gar_dongre\": 0.4106, \"tf_ppl\": 2.6123, \"ar_beta0_gar\": 0.4231, \"ar_beta0_ppl\": 1.4408, \"ar_beta3_gar\": 0.5903, \"ar_beta3_ppl\": 1.607, \"ar_beta5_gar\": 0.7174, \"ar_beta5_ppl\": 1.7852, \"n_convs_tf\": 200, \"n_convs_ar\": 39}}, \"d048_ss_s123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-23T07:54:41.928Z\", \"updated_at\": \"2026-05-23T17:29:06.984Z\", \"hypothesis\": \"Scheduled sampling (ratio=0.3) with ThreadGate multi-seed (s123) to establish 3-seed mean±std for C2 reviewer requirement. Corrected hyperparams matching d048_ss_s456.\", \"parent\": \"d048_ss_s42\", \"spec\": {\"command\": \"python train_phase2_v8b.py --gate-type threadgate --seed 123 --output-dir runs/d048_ss_s123 --lr 2e-4 --epochs 3 --batch-size 1 --grad-accum 8 --ss-ratio 0.3\", \"server\": \"westd-20861\", \"pid\": \"84793\", \"data_path\": \"/root/turn-residual-gating/data/phase2_train.jsonl\", \"data_count\": 2000, \"model_name\": \"Qwen/Qwen2.5-7B-Instruct\", \"seed\": 123, \"gpu\": 0, \"checkpoint_source\": \"Qwen/Qwen2.5-7B-Instruct (base, no prior checkpoint)\", \"eval_data\": \"N/A - this is a training experiment\", \"checkpoint_path\": \"/root/turn-residual-gating/runs/d048_ss_s123/epoch_2\", \"log_path\": \"/root/turn-residual-gating/runs/d048_ss_s123/train.log\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-23T17:29:06.984Z\"}, \"d048_split_softmax_eval\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-23T07:47:05.556Z\", \"updated_at\": \"2026-05-23T08:00:42.748Z\", \"hypothesis\": \"Split-softmax (Li et al., COLM 2024) post-softmax rescaling recovers AR GAR without the PPL cost of pre-softmax additive steering, providing an alternative inference-time intervention that separates attention allocation from logit distribution.\", \"spec\": {\"command\": \"python src/eval_split_softmax.py\", \"server\": \"westd-20861\", \"data_path\": \"data/eval_200/eval_200.json\", \"data_count\": 50, \"model_name\": \"Qwen2.5-7B-Instruct + TG v7 LoRA\", \"seed\": 42, \"checkpoint_path\": \"N/A (failed)\", \"log_path\": \"results/split_softmax/\", \"failure_reason\": \"Bug 1: system_prompt_len=0 hardcoded (line 373) — split-softmax has no effect. Bug 2: gen mode NaN for k=0.0/0.3/0.5/0.7. Needs code fix before re-run.\"}, \"conclusion\": \"failed\", \"completed_at\": \"2026-05-23T07:53:10.326Z\", \"notes\": \"2 critical bugs: (1) system_prompt_len=0 hardcoded at L373, (2) gen mode NaN for k≠1.0. Director decision 2026-05-23: not urgent, defer fix past DDL 5/25. Does not affect main paper experiments.\"}, \"d048_final_ar_eval\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-23T03:46:23.495Z\", \"updated_at\": \"2026-05-23T03:47:01.285Z\", \"hypothesis\": \"Unified AR N=50 eval across 6 conditions (Base/TG/UG/LO/PCGrad/SS) with bootstrap CI and Wilcoxon tests to establish statistically rigorous comparisons for all claims\", \"spec\": {\"command\": \"bash scripts/d048_final_ar_eval.sh\", \"server\": \"westd-20861\", \"data_path\": \"data/eval_200/eval_200.json\", \"data_count\": 200, \"model_name\": \"Qwen/Qwen2.5-7B-Instruct\", \"seed\": 42, \"checkpoint_source\": \"phase2_tg_s42_v7 / phase2_ug_s42 / phase2_lora_only_s42 / tg_v9_pcgrad_s42 / d048_ss_s42\", \"eval_data\": \"eval_200.json N=50\", \"checkpoint_path\": \"N/A (eval only)\", \"log_path\": \"runs/d048_final_ar_eval.log\", \"results_path\": \"results/d048_final_ar/\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-23T03:46:57.110Z\", \"metrics\": {\"beta0\": {\"base_gar\": 0.019, \"tg_gar\": 0.064, \"ug_gar\": 0.033, \"lo_gar\": 0.037, \"pcgrad_gar\": 0.03, \"ss_gar\": 0.347}, \"beta3\": {\"base_gar\": 0.531, \"tg_gar\": 0.556, \"ss_gar\": 0.593}, \"beta5\": {\"base_gar\": 0.704, \"tg_gar\": 0.727, \"ss_gar\": 0.717}, \"wilcoxon_beta0\": {\"tg_vs_base_p\": \"<0.001\", \"tg_vs_base_r\": 0.802, \"ss_vs_tg_p\": \"<0.001\", \"ss_vs_tg_r\": 0.869}, \"ppl\": {\"base\": 1.447, \"tg\": 1.432, \"ss\": 1.442}, \"n_convs\": 39}}, \"d048_queue_runner\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-22T23:42:35.919Z\", \"updated_at\": \"2026-05-22T23:42:39.048Z\", \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"conclusion\": \"failed\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-22T23:42:38.157928+00:00\"}]}, \"reproduce\": {\"finished_at\": \"2026-05-22T23:42:38.522Z\"}}, \"d048_eval_ss_s42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T22:52:15.395Z\", \"updated_at\": \"2026-05-22T23:32:26.276Z\", \"spec\": {\"command\": \"bash scripts/d048_eval_ss_s42.sh\", \"server\": \"westd-20861\", \"gpu\": [\"cuda:0\"], \"pid\": \"48241\", \"log_path\": \"/root/turn_residual_gating/runs/d048_ss_s42/eval.log\", \"submitted_at\": \"2026-05-22T22:52:15.275Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/ultrachat_8k + model-gen AR N=50\", \"data_count\": 50, \"model_name\": \"Qwen2.5-7B-Instruct (SS s42)\", \"seed\": 42, \"checkpoint_source\": \"runs/d048_ss_s42/epoch_2\", \"eval_data\": \"ultrachat_eval_heldout 50 + model-gen AR N=50\", \"checkpoint_path\": \"runs/d048_ss_s42/epoch_2\", \"wall_clock_seconds\": 1365.5, \"gpu_hours\": 0.38}, \"hypothesis\": \"D048 multi-seed SS s42 eval: TF + AR N=50 + bootstrap CI (curve[2:]) to establish mean±std for scheduled sampling. Expect TF GAR ~0.50, AR GAR gap < 2× (vs base ~31×), PPL stable.\", \"parent\": \"d048_ss_s42\", \"reproduce\": {\"finished_at\": \"2026-05-22T23:12:55.735Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-22T23:12:58.142628+00:00\"}]}, \"metrics\": {\"tf\": {\"base_gar_ours_mid\": 0.0128, \"base_gar_dongre_mid\": 0.0031, \"base_ppl\": 4.34, \"base_ntp\": 1.4, \"tg_gar_ours_mid\": 0.5025, \"tg_gar_dongre_mid\": 0.389, \"tg_ppl\": 2.78, \"tg_ntp\": 0.98, \"baseline_mid_gar\": 0.0122}, \"ar\": {\"gar_ours_mid\": 0.3887, \"gar_ours_ci_95\": [0.3692, 0.3934], \"ppl\": 1.35}, \"gap_ratio\": 1.29, \"n_conversations_tf\": 50, \"n_conversations_ar\": 5, \"bootstrap_turns\": \"curve[2:] (turns 3-T)\", \"note\": \"AR used hardcoded N=5, not N=50. Will be re-evaluated in final unified batch with eval_200.json N=50.\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-22T23:15:00.734Z\"}, \"d048_ss_s42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T09:14:13.365Z\", \"updated_at\": \"2026-05-22T23:11:26.493Z\", \"hypothesis\": \"Scheduled sampling (ratio=0.3) with ThreadGate reduces the ~30× TF-AR GAR gap by exposing the model to its own generated text during training. Multi-seed run (s42) under D048 unified protocol to establish mean±std for statistical testing. SS is the strongest mitigation candidate (prior single-seed showed gap 31×→1.57×).\", \"spec\": {\"command\": \"bash -c \\\"cd /root/turn_residual_gating && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && PYTHONUNBUFFERED=1 python src/train_phase2_v8b.py --model /root/.cache/modelscope/Qwen/Qwen2___5-7B-Instruct --gate-type threadgate --gar-loss-mode mse_target --gar-target 0.5 --lambda-gar 1.0 --lambda-gate-div 1.0 --min-gate-std 0.05 --init-bias 1.5 --gate-lr-multiplier 10 --lr 2e-4 --batch-size 1 --grad-accum 8 --max-seq-len 2048 --scheduled-sampling --ss-max-ratio 0.3 --seed 42 --epochs 3 --output-dir runs/d048_ss_s42 --data-dir data/ultrachat_8k --resume runs/d048_ss_s42/epoch_0 2>&1 | tee ~/runs/turn_residual_gating/d048_ss_s42_resume.log\\\"\", \"server\": \"westd-20861\", \"gpu\": [\"cuda:0\"], \"pid\": \"32861\", \"log_path\": \"~/runs/turn_residual_gating/d048_ss_s42.log\", \"submitted_at\": \"2026-05-22T15:59:07.519Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"reproduce\": {\"finished_at\": \"2026-05-22T15:51:53.120Z\"}, \"failure_reason\": \"CUDA OOM: CUDA out of memory. Tried to allocate 424.00 MiB. GPU 0 has a total capacity of 94.97 GiB of which 218.56 MiB is free. Including non-PyTorch memory, this process has 26.13 GiB memory in use. Process 30899 has 68.62 GiB memory in use. Of the allocated\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-22T15:51:54.391Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-22T15:51:56.369724+00:00\"}]}, \"notes\": \"Training complete (resume v3). 23418s (6.5h) for epoch 1+2. Final: Avg Loss=0.9326, NTP=0.9320, GAR=0.0007, DIV=0.0000. Gate: mean=0.9527, std=0.0589, min=0.7383(L4), max=1.000. SS: 4750/16000 (29.7%) used, 0 fallback. Checkpoints: epoch_0, epoch_1, epoch_2, final. Gate profile consistent with prior SS runs (L4 lowest).\", \"metrics\": {\"final_avg_loss\": 0.9326, \"final_ntp_loss\": 0.932, \"final_gar_loss\": 0.0007, \"gate_mean\": 0.9527, \"gate_std\": 0.0589, \"gate_min\": 0.7383, \"gate_min_layer\": \"L4\", \"gate_max\": 1, \"ss_usage\": \"4750/16000 (29.7%)\", \"ss_fallback\": 0, \"epochs_completed\": 3, \"wall_clock_s\": 23418, \"wall_clock_h\": 6.5}}, \"d048_ss_s42_resume\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-22T15:57:05.941Z\", \"updated_at\": \"2026-05-22T15:57:05.941Z\", \"spec\": {\"command\": \"bash -c \\\"cd /root/turn_residual_gating && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && PYTHONUNBUFFERED=1 python src/train_phase2_v8b.py --model /root/.cache/modelscope/Qwen/Qwen2___5-7B-Instruct --gate-type threadgate --gar-loss-mode mse_target --gar-target 0.5 --lambda-gar 1.0 --lambda-gate-div 1.0 --min-gate-std 0.05 --init-bias 1.5 --gate-lr-multiplier 10 --lr 2e-4 --batch-size 1 --grad-accum 8 --max-seq-len 2048 --scheduled-sampling --ss-max-ratio 0.3 --seed 42 --epochs 3 --output-dir runs/d048_ss_s42 --data-dir data/ultrachat_8k --resume runs/d048_ss_s42/epoch_0\\\"\", \"server\": \"westd-20861\", \"gpu\": [\"cuda:0\"], \"pid\": \"32472\", \"log_path\": \"~/runs/turn_residual_gating/d048_ss_s42_resume.log\", \"submitted_at\": \"2026-05-22T15:57:05.791Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}}, \"eval_llama_ar_n20\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T07:52:04.543Z\", \"updated_at\": \"2026-05-22T08:38:33.680Z\", \"hypothesis\": \"N=20 AR eval stabilizes Llama 3-way (Base/TG/LoRA-only) autoregressive GAR estimates. N=5 suffered from outlier influence (3/5 conv had GAR>0.4 outlier turns); N=20 provides robust mean±std.\", \"parent\": \"eval_llama_lora_only_s42\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/turn_residual_gating && bash scripts/eval_llama_ar_n20.sh\\\"\", \"server\": \"westd-20861\", \"gpu\": [\"cuda:0\"], \"pid\": \"312592\", \"log_path\": \"~/runs/turn_residual_gating/eval_llama_ar_n20.log\", \"submitted_at\": \"2026-05-22T07:52:13.830Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"ultrachat_200k + model-gen AR\", \"data_count\": 20, \"model_name\": \"Llama-3.1-8B-Instruct (Base/TG/LoRA-only)\", \"seed\": 42, \"checkpoint_source\": \"llama_tg_s42 + llama_lora_only_s42\", \"eval_data\": \"AR-generated 20 conversations x 4 turns\", \"wall_clock_seconds\": 1435.6, \"gpu_hours\": 0.4}, \"reproduce\": {\"finished_at\": \"2026-05-22T08:09:48.181Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-22T08:09:50.100538+00:00\"}]}, \"checkpoint_path\": \"N/A\", \"log_path\": \"/root/runs/turn_residual_gating/eval_llama_ar_n20.log\", \"metrics\": {\"base\": {\"gar_ours_mean\": 0.0088, \"gar_ours_std\": 0.0056, \"gar_ours_median_per_conv\": 0.0093, \"gar_ours_median_per_turn_pool\": 0.0071, \"gar_ours_spike_ratio\": \"0%\", \"gar_dongre_mean\": 0.0049, \"gar_dongre_std\": 0.0013, \"gar_dongre_median\": 0.0047, \"ngar_ours_mid\": 0.1019, \"ngar_dongre_mid\": 0.1171, \"ppl\": 1.293, \"ppl_std\": 0.07, \"ntp_loss\": 0.2552}, \"tg\": {\"gar_ours_mean\": 0.0434, \"gar_ours_std\": 0.1002, \"gar_ours_median_per_conv\": 0.0179, \"gar_ours_median_per_turn_pool\": 0.0126, \"gar_ours_spike_ratio\": \"5% (2/40 turns GAR>=0.4)\", \"gar_dongre_mean\": 0.0183, \"gar_dongre_std\": 0.0198, \"gar_dongre_median\": 0.0152, \"ngar_ours_mid\": 0.5357, \"ngar_dongre_mid\": 0.4436, \"ppl\": 1.437, \"ppl_std\": 0.077, \"ntp_loss\": 0.3612}, \"lora_only\": {\"gar_ours_mean\": 0.0284, \"gar_ours_std\": 0.0481, \"gar_ours_median_per_conv\": 0.0184, \"gar_ours_median_per_turn_pool\": 0.0133, \"gar_ours_spike_ratio\": \"0%\", \"gar_dongre_mean\": 0.0205, \"gar_dongre_std\": 0.0241, \"gar_dongre_median\": 0.016, \"ngar_ours_mid\": 0.3488, \"ngar_dongre_mid\": 0.4997, \"ppl\": 1.419, \"ppl_std\": 0.075, \"ntp_loss\": 0.3483}, \"n_conversations\": 20, \"n_turns\": 4, \"mid_turns_definition\": \"turns 3-T (0-indexed avg_gar[2:], excluding turns 1-2). All 16 eval entries use same definition.\", \"stat_pool\": \"median_per_conv: median of 20 per-conversation mid-turn averages. median_per_turn_pool: median of 40 individual turn values (20 conv x 2 mid turns).\", \"ranking_gar_ours_mean\": \"TG(0.0434) > LO(0.0284) > Base(0.0088)\", \"ranking_gar_ours_median_per_conv\": \"TG(0.0179) ≈ LO(0.0184) > Base(0.0093)\", \"ranking_gar_ours_median_per_turn_pool\": \"TG(0.0126) ≈ LO(0.0133) > Base(0.0071)\", \"ranking_gar_dongre\": \"LO(0.0205) > TG(0.0183) > Base(0.0049)\", \"note\": \"Paper §5.5 cites median_per_conv (median of per-conversation mid-turn averages across N=20). median_per_turn_pool is the alternative statistic from pooled individual turns. Both confirm TG ≈ LO (zero-increment).\"}, \"notes\": \"N=20 AR eval stabilizes estimates. **mid_turns = turns 3-T (0-indexed avg_gar[2:], excluding turns 1-2; all 16 eval entries use same definition)**. Two median levels: median_per_conv (paper §5.5 cites this: TG 0.0179, LO 0.0184, Base 0.0093) = median of 20 per-conversation mid-turn averages; median_per_turn_pool (TG 0.0126, LO 0.0133, Base 0.0071) = median of 40 pooled individual turns. Both confirm TG ≈ LO (zero-increment). Mean (TG 0.0434 > LO 0.0284) driven by outlier spikes (TG std=0.1002, 5% turns GAR≥0.4; LO std=0.0481, 0% spikes). PPL: Base(1.29) < LO(1.42) < TG(1.44). Pending paper fix: §5.5 says \\\"turns 2-T\\\" but code excludes turns 1-2; will correct to \\\"excluding the first two turns\\\" in next paper edit batch.\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-22T08:16:09.384Z\"}, \"eval_llama_lora_only_s42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T07:40:25.352Z\", \"updated_at\": \"2026-05-22T07:51:32.758Z\", \"hypothesis\": \"LoRA-only ablation (no gate) on Llama-3.1-8B: if TG's GAR improvement comes from the gate, LoRA-only should show minimal GAR recovery vs base.\", \"parent\": \"llama_lora_only_s42\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/turn_residual_gating && bash scripts/eval_llama_lora_only_s42.sh\\\"\", \"server\": \"westd-20861\", \"gpu\": [\"cuda:0\"], \"pid\": \"309670\", \"log_path\": \"/root/runs/turn_residual_gating/eval_llama_lora_only_s42.log\", \"submitted_at\": \"2026-05-22T07:40:34.437Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"ultrachat_200k + model-gen\", \"data_count\": 55, \"model_name\": \"Llama-3.1-8B-Instruct + LoRA-only checkpoint\", \"seed\": 42, \"checkpoint_source\": \"llama_lora_only_s42\", \"eval_data\": \"IID heldout 50 + model-gen 5\", \"checkpoint_path\": \"runs/phase2_llama_lora_only_s42/epoch_2\", \"wall_clock_seconds\": 650.8, \"gpu_hours\": 0.18}, \"reproduce\": {\"finished_at\": \"2026-05-22T07:45:28.637Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-22T07:45:30.556207+00:00\"}]}, \"metrics\": {\"tf\": {\"gar_ours\": 0.4807, \"gar_dongre\": 0.0188, \"ngar_ours\": 11.8031, \"ngar_dongre\": 0.8261, \"ppl\": 2.6, \"ntp_loss\": 0.9366, \"n_conversations\": 50, \"n_turns\": 4}, \"ar\": {\"gar_ours\": 0.0617, \"gar_dongre\": 0.0226, \"ngar_ours\": 0.6065, \"ngar_dongre\": 0.2537, \"ppl\": 1.32, \"ntp_loss\": 0.2787, \"n_conversations\": 5, \"n_turns\": 10}, \"gap_ratio_gar_ours\": 7.79}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-22T07:51:25.244Z\"}, \"llama_lora_only_s42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T00:33:03.465Z\", \"updated_at\": \"2026-05-22T07:39:06.888Z\", \"hypothesis\": \"Llama-3.1-8B LoRA-only baseline (gate=none, 无 gating 机制): 与 Llama TG s42 对比，验证 gating 对 Llama 的增量贡献。如果 LoRA-only GAR ≈ TG GAR → gating 零增量与 Qwen 结论一致（C5 跨模型）。\", \"parent\": \"llama_tg_s42\", \"spec\": {\"command\": \"bash scripts/launch_llama_lora_only_s42.sh\", \"server\": \"westd-20861\", \"gpu\": [\"cuda:0\"], \"pid\": \"271741\", \"log_path\": \"logs/llama_lora_only_s42.log\", \"submitted_at\": \"2026-05-22T00:33:16.591Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/turn_residual_gating/data/ultrachat_8k\", \"data_count\": 8000, \"model_name\": \"Meta-Llama-3.1-8B-Instruct\", \"seed\": 42, \"checkpoint_source\": \"N/A (training from scratch, ablation baseline)\", \"eval_data\": \"N/A (training run, not eval)\", \"checkpoint_path\": \"runs/phase2_llama_lora_only_s42/epoch_2\", \"wall_clock_seconds\": 25550.3, \"gpu_hours\": 7.1}, \"reproduce\": {\"finished_at\": \"2026-05-22T07:35:56.232Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-22T07:35:58.740298+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"final_avg_loss\": 0.9288, \"final_avg_ntp\": 0.9279, \"final_avg_gar\": 0.0009, \"gate_fixed\": 1, \"gate_type\": \"none\", \"wall_clock_s\": 25317, \"wall_clock_h\": 7.03, \"epochs_completed\": 3}, \"completed_at\": \"2026-05-22T07:39:06.889Z\"}, \"phase2_tg_s42_v6\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T17:53:01.911Z\", \"updated_at\": \"2026-05-22T04:37:13.229Z\", \"hypothesis\": \"smooth_saturation loss (-target*tanh(GAR/target), target=0.5) 提供有界但持续的 GAR 梯度，避免 maximize 的恒等退化（gate→1）和 hinge_target 的梯度消失（GAR达标后梯度=0）。预期：gate_std>0.05 的层间分化 + GAR 稳态在 0.3-0.5 + NTP loss 正常收敛 + 总 loss 为正。\", \"parent\": \"phase2_tg_s42_v5\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/turn_residual_gating && PYTHONUNBUFFERED=1 python src/train_phase2.py --gate-type threadgate --gar-loss-mode smooth_saturation --gar-target 0.5 --lambda-gar 1.0 --init-bias 1.5 --gate-lr-multiplier 10 --max-seq-len 2048 --seed 42 --output-dir /root/turn_residual_gating/runs/phase2_tg_s42_v6 --data-dir /root/turn_residual_gating/data/ultrachat_8k --epochs 3\\\"\", \"server\": \"westd-20861\", \"data_path\": \"/root/turn_residual_gating/data/ultrachat_8k\", \"data_count\": 8000, \"model_name\": \"Qwen/Qwen2.5-7B-Instruct\", \"seed\": 42, \"checkpoint_path\": \"/root/turn_residual_gating/runs/phase2_tg_s42_v6\", \"log_path\": \"~/runs/turn_residual_gating/phase2_tg_s42_v6.log\"}, \"metrics\": {\"dryrun_step0_L_NTP\": 2.0275, \"dryrun_step0_L_GAR\": -0.0161, \"dryrun_step0_total_loss\": 2.0114, \"dryrun_step4_L_NTP\": 1.6544, \"dryrun_step4_L_GAR\": -0.0147, \"dryrun_step4_total_loss\": 1.6397, \"dryrun_gate_grad\": true, \"dryrun_gate_mean_init\": 0.8097, \"dryrun_gate_std_init\": 0.0341, \"dryrun_gate_min_init\": 0.6836, \"dryrun_gate_max_init\": 0.8672, \"dryrun_gate_mean_step5\": 0.8025, \"dryrun_gate_std_step5\": 0.0842, \"dryrun_gate_min_step5\": 0.5547, \"dryrun_gate_max_step5\": 0.9805, \"gs50_gate_mean\": 0.8117, \"gs50_gate_std\": 0.0612, \"gs50_gate_min\": 0.6836, \"gs50_gate_max\": 0.9805, \"gs100_gate_mean\": 0.8737, \"gs100_gate_std\": 0.0367, \"gs100_gate_min\": 0.8164, \"gs100_gate_max\": 0.9766, \"gs100_L_NTP\": 0.8151, \"gs100_L_GAR\": -0.158, \"gs100_total_loss\": 0.6571, \"gs100_profile_bottom3\": \"L12=0.816 L4=0.824 L13=0.824\", \"gs100_profile_top3\": \"L27=0.977 L26=0.961 L23=0.914\", \"gs143_L_GAR\": -0.3876, \"gs143_gate_mean\": 0.9227}, \"conclusion\": \"negative\", \"notes\": \"smooth_saturation 与 maximize 同轨迹，单调 GAR 奖励导致恒等退化。step 100: gate_std=0.037↓ gate_mean=0.874↑，step ~143: L_GAR=-0.39 gate_mean=0.923。boundedness 只减缓退化速度不改变终态。D010 指令 kill 转 v7 MSE 双向 loss。\", \"completed_at\": \"2026-05-18T18:18:07.869Z\"}, \"phase2_tg_s42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T06:04:12.759Z\", \"updated_at\": \"2026-05-22T04:36:54.262Z\", \"hypothesis\": \"ThreadGate (turn-conditional gating) 在 L_NTP+L_GAR 联合训练后，相比 Uniform Gate，mid-turn GAR recovery 高出 ≥3pp，验证 Cesaro 理论预测：position-conditional 干预优于 uniform 干预\", \"parent\": \"phase1_gar_diag\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/turn_residual_gating/src && python train_phase2.py --gate-type threadgate --seed 42 --output-dir /root/turn_residual_gating/checkpoints/tg_s42 --data-dir /root/turn_residual_gating/data/ultrachat_8k --max-seq-len 2048\\\"\", \"server\": \"westd-20861\", \"gpu\": [\"cuda:0\"], \"pid\": \"11286\", \"log_path\": \"~/runs/turn_residual_gating/phase2_tg_s42.log\", \"submitted_at\": \"2026-05-18T07:03:28.476Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 15333, \"gpu_hours\": 4.26, \"data_path\": \"/root/turn_residual_gating/data/ultrachat_8k\", \"data_count\": 8000, \"model_name\": \"Qwen/Qwen2.5-7B-Instruct\", \"seed\": 42, \"checkpoint_path\": \"/root/turn_residual_gating/checkpoints/tg_s42\"}, \"server\": \"westd-20861\", \"gpu\": \"cuda:0\", \"pid\": \"11286\", \"log_path\": \"~/runs/turn_residual_gating/phase2_tg_s42.log\", \"reproduce\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/turn_residual_gating/src && python train_phase2.py --gate-type threadgate --seed 42 --output-dir /root/turn_residual_gating/checkpoints/tg_s42 --data-dir /root/turn_residual_gating/data/ultrachat_8k --max-seq-len 2048\\\"\", \"finished_at\": \"2026-05-18T11:19:00.888Z\"}, \"failure_reason\": \"EXIT_CODE=143 (SIGTERM — graceful kill)\", \"conclusion\": \"negative\", \"completed_at\": \"2026-05-18T11:19:01.512Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-18T11:19:02.835359+00:00\"}]}, \"notes\": \"失败原因: EXIT_CODE=143 (SIGTERM) — 大概率被 Worker code:diagnose_gar_loss_and_fix 主动 kill（时间线：Worker 11:13 启动 → v2 11:13 创建 → v1 11:19 SIGTERM）。v2 hypothesis 指出 GAR loss 实现有 bug（缺少 ε=0.001 稳定项）。诊断 Worker worker_diagnose_phase2_tg_s42_20260518T112048 已派出确认日志详情。| 建议: 等诊断结果确认后推进 v2\", \"checkpoint_path\": \"/root/turn_residual_gating/checkpoints/tg_s42/epoch_1\", \"metrics\": {\"final_ntp_loss\": 0.94, \"final_gar_loss\": 0, \"gate_mean\": 0.988, \"gar_loss_zero_pct\": 87.6, \"epochs_completed\": 1.67, \"killed_reason\": \"SIGTERM by diagnose worker (unauthorized)\"}}, \"eval_v7_tg_s123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T22:53:18.163Z\", \"updated_at\": \"2026-05-22T00:30:49.653Z\", \"spec\": {\"command\": \"bash scripts/eval_v7_tg_s123.sh\", \"server\": \"westd-20861\", \"gpu\": [\"cuda:0\"], \"pid\": \"264869\", \"log_path\": \"/root/turn_residual_gating/logs/v7_tg_s123.log\", \"submitted_at\": \"2026-05-21T22:53:18.065Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/ultrachat_8k\", \"data_count\": 8000, \"model_name\": \"Qwen2.5-7B-Instruct\", \"seed\": 123, \"checkpoint_source\": \"v7_tg_s123\", \"eval_data\": \"data/ultrachat_8k\", \"checkpoint_path\": \"/root/turn_residual_gating/runs/phase2_tg_s123_v7/epoch_2\", \"wall_clock_seconds\": 5844.5, \"gpu_hours\": 1.62}, \"hypothesis\": \"v7 TG s123 eval: 验证 s123 seed 的 TF-AR GAR gap 与 s42 一致（~32×），确认 multi-seed robustness\", \"parent\": \"v7_tg_s123\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-22T00:30:42.606Z\", \"metrics\": {\"iid_tf\": {\"gar_ours_mid\": 0.5052, \"gar_dongre_mid\": 0.0119, \"ppl\": 2.7802, \"ntp\": 0.9752}, \"modelgen_ar\": {\"gar_ours_mid\": 0.0165, \"gar_dongre_mid\": 0.0177, \"ppl\": 1.3855, \"ntp\": 0.3223}, \"gap_ratio\": 30.6, \"comparison_s42\": {\"tf_gar_ours_delta\": 0.0017, \"ar_gar_ours_delta\": 0.0008, \"gap_ratio_delta\": -1.4}}}, \"eval_v8b_ss_s123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T21:15:52.880Z\", \"updated_at\": \"2026-05-21T22:53:15.356Z\", \"spec\": {\"command\": \"bash scripts/eval_v8b_ss_s123.sh\", \"server\": \"westd-20861\", \"gpu\": [\"cuda:0\"], \"pid\": 259767, \"log_path\": \"runs/eval_v8b_ss_s123/\", \"submitted_at\": \"2026-05-21T21:15:52.785Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/ultrachat_eval_heldout.json\", \"data_count\": 50, \"model_name\": \"Qwen2.5-7B-Instruct\", \"seed\": 123, \"gpu_index\": 0, \"checkpoint_source\": \"checkpoints/tg_v8b_ss_s123/epoch_2\", \"eval_data\": \"ultrachat_eval_heldout + model-gen\", \"checkpoint_path\": \"checkpoints/tg_v8b_ss_s123/epoch_2\", \"wall_clock_seconds\": 5835.7, \"gpu_hours\": 1.62}, \"hypothesis\": \"v8b SS model trained with s123 seed should reproduce s42 GAR metrics within acceptable gap_ratio [1.2x-2.5x] and no PPL degradation, confirming seed robustness of the scheduled sampling approach\", \"parent\": \"v7_tg_s123\", \"log_path\": \"~/runs/turn_residual_gating/eval_v8b_ss_s123.log\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-21T22:53:08.443Z\", \"metrics\": {\"iid\": {\"gar_ours\": 0.503, \"gar_dongre\": 0.394, \"ppl\": 2.781, \"ntp_loss\": 0.976, \"n_conv\": 50, \"n_turns\": 3}, \"modelgen\": {\"gar_ours\": 0.418, \"gar_dongre\": 0.441, \"ppl\": 1.389, \"ntp_loss\": 0.325, \"n_conv\": 5, \"n_turns\": 10}, \"gap_ratio\": 1.2, \"base_iid_ppl\": 4.338, \"base_modelgen_ppl\": 1.351}}, \"v7_tg_s123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T15:16:39.923Z\", \"updated_at\": \"2026-05-21T21:17:16.499Z\", \"hypothesis\": \"v7 TG s42 已验证 ThreadGate 有效性，s123 验证 seed robustness。预期 gate profile 和 GAR 收敛模式与 s42 一致。\", \"parent\": \"phase2_tg_s42_v7\", \"spec\": {\"command\": \"bash scripts/launch_v7_tg_s123.sh\", \"server\": \"westd-20861\", \"data_path\": \"data/ultrachat_8k\", \"data_count\": 8000, \"model_name\": \"Qwen2.5-7B-Instruct\", \"seed\": 123, \"pid\": 245628, \"gpu_index\": 0, \"checkpoint_path\": \"/root/turn_residual_gating/runs/phase2_tg_s123_v7\", \"log_path\": \"/root/turn_residual_gating/logs/v7_tg_s123.log\", \"checkpoint_source\": \"N/A (from scratch)\", \"eval_data\": \"N/A\"}, \"conclusion\": \"success\", \"checkpoint_path\": \"runs/phase2_tg_s123_v7/epoch_2\", \"log_path\": \"logs/v7_tg_s123.log\", \"metrics\": {\"epoch_1\": {\"avg_loss\": 0.9447, \"avg_ntp_loss\": 0.9434, \"avg_gar_loss\": 0.0013, \"avg_div_loss\": 0}, \"epoch_2\": {\"avg_loss\": 0.9315, \"avg_ntp_loss\": 0.9305, \"avg_gar_loss\": 0.001, \"avg_div_loss\": 0}, \"final_gate\": {\"mean\": 0.9467, \"std\": 0.051, \"min\": 0.793, \"max\": 1}, \"final_gate_profile\": {\"L0\": 0.883, \"L1\": 0.793, \"L2\": 0.996, \"L3\": 0.988, \"L4\": 0.984, \"L5\": 0.797, \"L6\": 0.961, \"L7\": 0.918, \"L8\": 0.965, \"L9\": 0.934, \"L10\": 0.969, \"L11\": 0.918, \"L12\": 0.926, \"L13\": 0.941, \"L14\": 0.93, \"L15\": 0.965, \"L16\": 0.941, \"L17\": 0.91, \"L18\": 0.961, \"L19\": 0.965, \"L20\": 0.973, \"L21\": 0.988, \"L22\": 0.969, \"L23\": 0.98, \"L24\": 0.98, \"L25\": 0.984, \"L26\": 0.988, \"L27\": 1}, \"training_time_s\": 21425.2}, \"completed_at\": \"2026-05-21T21:17:16.499Z\"}, \"v8b_ss_s123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T04:29:28.197Z\", \"updated_at\": \"2026-05-21T15:15:49.282Z\", \"hypothesis\": \"v8b SS s42 成功（gap 32×→1.57×），s123 验证结果的 seed robustness。预期 model-gen GAR 同样显著提升，PPL 无恶化。\", \"parent\": \"phase2_tg_s42_v8b_resume\", \"spec\": {\"command\": \"bash scripts/launch_v8b_ss_s123.sh\", \"server\": \"westd-20861\", \"data_path\": \"data/ultrachat_8k\", \"data_count\": 8000, \"model_name\": \"Qwen2.5-7B-Instruct\", \"seed\": 123, \"checkpoint_source\": \"N/A (from scratch)\", \"eval_data\": \"N/A\", \"checkpoint_path\": \"/root/turn_residual_gating/checkpoints/tg_v8b_ss_s123\", \"log_path\": \"/root/turn_residual_gating/logs/v8b_ss_s123.log\"}, \"conclusion\": \"success\", \"metrics\": {\"final_loss\": 0.9316, \"final_ntp_loss\": 0.9307, \"final_gar_loss\": 0.0009, \"final_gate_mean\": 0.9505, \"final_gate_std\": 0.0508, \"final_gate_min\": 0.7383, \"final_gate_max\": 1, \"ss_used_ratio\": 0.371, \"training_time_s\": 38773.4, \"epoch0_loss\": 1.0092, \"epoch1_loss\": 0.9444, \"epoch2_loss\": 0.9316}, \"completed_at\": \"2026-05-21T15:15:49.282Z\"}, \"llama_tg_training\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-21T03:37:31.513Z\", \"updated_at\": \"2026-05-21T09:44:18.859Z\", \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"conclusion\": \"failed\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-21T03:37:33.309826+00:00\"}]}, \"notes\": \"INVALIDATED: Phantom duplicate of llama_tg_s42 (same PID 199643, same experiment). Created by Worker in global registry, duplicated to project registry. Canonical entry is llama_tg_s42 (DONE/success).\"}, \"llama_ar_matched_eval\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T03:59:40.918Z\", \"updated_at\": \"2026-05-21T04:36:23.237Z\", \"hypothesis\": \"用 matched 设置 (N=50/T=4) 重跑 Llama AR eval，消除 TF/AR 设置差异。与 TF 结果对比得到可直接写入论文的 gap ratio，验证 TG 在 AR 模式下仍能提升 GAR。\", \"parent\": \"llama_eval_s42\", \"spec\": {\"command\": \"bash scripts/eval_llama_ar_matched.sh\", \"server\": \"westd-20861\", \"data_path\": \"data/ultrachat_eval_sample.json\", \"data_count\": 50, \"model_name\": \"Meta-Llama-3.1-8B-Instruct + TG LoRA\", \"seed\": 42, \"checkpoint_source\": \"phase2_llama_tg_s42\", \"eval_data\": \"50 UltraChat convs, T=4, AR generation, 4 conditions (base/TG x ours/Dongre)\", \"checkpoint_path\": \"N/A (eval)\", \"log_path\": \"runs/eval_llama_ar_matched.log\"}, \"log_path\": \"/root/turn_residual_gating/runs/eval_llama_ar_matched.log\", \"conclusion\": \"success\", \"metrics\": {\"ar_base_ours\": {\"mid_gar\": 0.0082, \"ngar\": 0.1, \"ppl\": 1.267}, \"ar_tg_ours\": {\"mid_gar\": 0.0388, \"ngar\": 0.493, \"ppl\": 1.413}, \"ar_base_dongre\": {\"mid_gar\": 0.0051, \"ngar\": 0.12, \"ppl\": 1.267}, \"ar_tg_dongre\": {\"mid_gar\": 0.018, \"ngar\": 0.431, \"ppl\": 1.413}, \"tf_reference\": {\"tf_tg_ours_ngar\": 11.88, \"tf_base_ours_ngar\": 0.388, \"tf_tg_ours_raw\": 0.4836, \"tf_tg_dongre_raw\": 0.018}, \"matched_gap_analysis\": {\"gar_ours_raw_gap\": \"12.5x (TF 0.484 / AR 0.039)\", \"gar_ours_ngar_gap\": \"24.1x (TF 11.88 / AR 0.493)\", \"gar_dongre_raw_gap\": \"1.002x (TF 0.018 / AR 0.018) — zero gap\", \"tg_over_base_ar_ours\": \"4.71x\", \"tg_over_base_ar_dongre\": \"3.54x\", \"conclusion\": \"GAR-ours TF-AR gap 12.5x (raw) / 24x (nGAR) is genuine exposure bias. GAR-Dongre zero gap (1.002x) confirms mechanism specificity: exposure bias selectively destroys learned goal-attention routing while leaving content-overlap-based attention unaffected.\"}}, \"completed_at\": \"2026-05-21T04:28:38.504Z\", \"notes\": \"CORRECTION (2026-05-21 04:36): Agent 之前错误地将 AR TG nGAR (0.493) 与 TF TG raw GAR (0.484) 对比，误判为 'nGAR aligns, gap is normalization artifact'。Reviewer 核实：TF TG ours nGAR = 11.88（非 0.48）。nGAR gap = 11.88 / 0.493 = 24.1×，比 raw gap (12.5×) 还大。'Normalization artifact' 分析完全错误——GAR-ours 的 gap 是真实的 exposure bias。论文绝对不能使用 normalization artifact 叙事。\"}, \"instruction_retention_test\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T03:49:26.068Z\", \"updated_at\": \"2026-05-21T03:59:31.835Z\", \"hypothesis\": \"Turn-level residual gating (β=3) preserves instruction-following ability across multi-turn conversations better than the baseline (β=0), because gating modulates residual contributions to retain earlier context signals rather than letting them decay through successive transformer layers.\", \"spec\": {\"command\": \"python src/eval_instruction_retention.py --checkpoint runs/phase2_tg_s42_v7 --prompts data/instruction_retention_prompts.json --betas 0 3 --seed 42 --output results/instruction_retention.json\", \"server\": \"westd-20861\", \"data_path\": \"data/instruction_retention_prompts.json\", \"data_count\": 18, \"model_name\": \"Qwen2.5-7B-Instruct + v7 TG LoRA\", \"seed\": 42, \"checkpoint_source\": \"phase2_tg_s42_v7\", \"eval_data\": \"18 instruction retention prompts, beta=[0,3], 5 turns each\"}, \"conclusion\": \"success\", \"checkpoint_path\": \"N/A (eval)\", \"log_path\": \"/root/turn_residual_gating/results/instruction_retention.log\", \"metrics\": {\"late_turn_rate_beta0\": 0.759, \"late_turn_rate_beta3\": 0.87, \"late_turn_delta\": 0.111, \"mcnemar_chi2\": 3.125, \"mcnemar_p\": 0.0771, \"gar_compliance_r\": 0.2003, \"gar_compliance_p\": 0.007, \"category_content_constraint\": {\"beta0\": 0.619, \"beta3\": 0.857, \"delta\": 0.238}, \"category_count_constraint\": {\"beta0\": 1, \"beta3\": 1, \"delta\": 0}, \"category_format_constraint\": {\"beta0\": 1, \"beta3\": 1, \"delta\": 0}, \"category_position_constraint\": {\"beta0\": 0.667, \"beta3\": 0.733, \"delta\": 0.067}}, \"completed_at\": \"2026-05-21T03:59:31.835Z\"}, \"llama_eval_s42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T03:29:51.255Z\", \"updated_at\": \"2026-05-21T03:46:58.167Z\", \"hypothesis\": \"Llama-3.1-8B TG eval: 如果 Llama TG 模型在 TF 模式下 GAR-ours 显著高于 AR 模式（如 Qwen v7 的 20-33x gap），则确认 training-inference GAR gap 跨模型泛化（C5）。同时测量 base model 作为 control。\", \"parent\": \"llama_tg_s42\", \"spec\": {\"command\": \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/turn_residual_gating && bash scripts/eval_llama_tg_s42.sh 2>&1 | tee runs/eval_llama_tg_s42.log\", \"server\": \"westd-20861\", \"data_path\": \"data/ultrachat_eval_sample.json\", \"data_count\": 50, \"model_name\": \"Llama-3.1-8B-Instruct\", \"seed\": 42, \"checkpoint_source\": \"runs/phase2_llama_tg_s42/epoch_2\", \"eval_data\": \"ultrachat_eval_sample\"}, \"checkpoint_path\": \"runs/phase2_llama_tg_s42/epoch_2\", \"log_path\": \"runs/eval_llama_tg_s42.log\", \"metrics\": {\"tf_base\": {\"gar_ours\": 0.0166, \"ngar_ours\": 0.3882, \"gar_dongre\": 0.0038, \"ngar_dongre\": 0.163, \"ppl\": 3.45, \"N\": 50, \"T\": 4}, \"tf_tg\": {\"gar_ours\": 0.4836, \"ngar_ours\": 11.8818, \"gar_dongre\": 0.018, \"ngar_dongre\": 0.7922, \"ppl\": 2.57, \"N\": 50, \"T\": 4}, \"ar_base\": {\"gar_ours\": 0.0086, \"ngar_ours\": 0.0798, \"gar_dongre\": 0.0118, \"ngar_dongre\": 0.1265, \"ppl\": 1.24, \"N\": 5, \"T\": 10}, \"ar_tg\": {\"gar_ours\": 0.0304, \"ngar_ours\": 0.2632, \"gar_dongre\": 0.0217, \"ngar_dongre\": 0.2459, \"ppl\": 1.32, \"N\": 5, \"T\": 10}, \"gap_ratio_tg_ours\": 15.9, \"gap_ratio_base_ours\": 1.93, \"gap_ratio_tg_dongre\": 0.83, \"vs_qwen_v7_gap_ratio\": 32.1, \"baseline_mid_gar\": 0.0122}, \"conclusion\": \"success\", \"notes\": \"C5 跨模型泛化确认。Llama TG GAR-ours gap 16x (TF 0.484 vs AR 0.030)，低于 Qwen v7 的 32x 但仍非常显著。Base model gap 仅 1.9x（control 通过）。注意 TF/AR eval 设定不同 (N=50/T=4 vs N=5/T=10)，可能影响绝对值对比。GAR-dongre 无明显 gap (ratio 0.83x, AR ≥ TF)，仅 GAR-ours 展现 exposure bias 效应。Gate dynamic range: L24/L28/L30 diff 最大 (0.23-0.38)，与 Qwen 类似集中在中高层。\", \"completed_at\": \"2026-05-21T03:46:58.167Z\"}, \"llama_tg_s42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T01:34:36.906Z\", \"updated_at\": \"2026-05-21T03:28:07.022Z\", \"hypothesis\": \"在 Llama-3.1-8B-Instruct 上训练 ThreadGate（与 Qwen v7 相同配置），验证 C5：gating mechanism 和 GAR training-inference gap 跨模型泛化。如果 Llama TG 也出现 IID GAR ≈ target 但 model-gen GAR 坍塌 → 确认 exposure bias 的跨模型通用性。\", \"parent\": \"llama_phase1_gar_diag\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 PYTHONUNBUFFERED=1 python src/train_phase2.py --model /root/autodl-tmp/models/LLM-Research/Meta-Llama-3___1-8B-Instruct --data-dir data/ultrachat_8k --output-dir runs/phase2_llama_tg_s42 --gate-type threadgate --gar-loss-mode mse_target --gar-target 0.5 --lambda-gar 1.0 --lambda-gate-div 1.0 --init-bias 1.5 --gate-lr-multiplier 10 --lr 2e-4 --epochs 3 --batch-size 1 --grad-accum 8 --seed 42\", \"server\": \"westd-20861\", \"gpu\": [\"cuda:0\"], \"pid\": \"199643\", \"data_path\": \"data/ultrachat_8k\", \"data_count\": 8000, \"model_name\": \"Meta-Llama-3.1-8B-Instruct\", \"seed\": 42, \"checkpoint_source\": \"N/A (training from scratch)\", \"eval_data\": \"N/A (training experiment)\", \"checkpoint_path\": \"/root/turn_residual_gating/runs/phase2_llama_tg_s42\", \"log_path\": \"/root/turn_residual_gating/logs/llama_tg_training.log\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-21T03:27:55.963Z\", \"metrics\": {\"epochs_completed\": 3, \"total_steps\": 3000, \"wall_clock_seconds\": 26212, \"wall_clock_hours\": 7.28, \"final_avg_loss\": 0.9233, \"final_avg_ntp\": 0.9224, \"final_avg_gar\": 0.0009, \"final_avg_div\": 0, \"final_gate_mean\": 0.9099, \"final_gate_std\": 0.0701, \"final_gate_min\": 0.7188, \"final_gate_max\": 0.9922, \"gate_profile_step3000\": {\"L0\": 0.957, \"L1\": 0.973, \"L2\": 0.977, \"L3\": 0.965, \"L4\": 0.992, \"L5\": 0.969, \"L6\": 0.957, \"L7\": 0.957, \"L8\": 0.961, \"L9\": 0.949, \"L10\": 0.938, \"L11\": 0.934, \"L12\": 0.969, \"L13\": 0.953, \"L14\": 0.957, \"L15\": 0.965, \"L16\": 0.953, \"L17\": 0.961, \"L18\": 0.922, \"L19\": 0.902, \"L20\": 0.883, \"L21\": 0.863, \"L22\": 0.836, \"L23\": 0.844, \"L24\": 0.809, \"L25\": 0.719, \"L26\": 0.762, \"L27\": 0.805, \"L28\": 0.801, \"L29\": 0.855, \"L30\": 0.898, \"L31\": 0.934}, \"checkpoint_size_gate_mb\": 4.2, \"checkpoint_size_lora_mb\": 26, \"gpu\": \"NVIDIA RTX PRO 6000 Blackwell\", \"vram_gb\": 102, \"mem_used_gb\": 63.4}}, \"attention_steering_gen_n50\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T19:04:17.455Z\", \"updated_at\": \"2026-05-21T01:59:57.100Z\", \"hypothesis\": \"N=5 gen steering 显示 β∈[2,5] phase transition (GAR 0.06→0.68)，但样本量不足以报告置信区间。N=50 conversations 应重现同一 phase transition pattern 并提供统计鲁棒的 mean±std，加固 C6 claim (attention steering as causal mechanism proof)。\", \"parent\": \"attention_steering_v7_tg_gen\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python src/eval_attention_steering.py --checkpoint runs/phase2_tg_s42_v7 --mode gen --data-file data/eval_200/eval_200.json --max-convs 50 --beta 0 2 3 4 5 10 --output-dir runs/attention_steering/ --output-name attention_steering_gen_n50\", \"server\": \"westd-20861\", \"gpu\": [\"cuda:0\"], \"data_path\": \"data/eval_200/eval_200.json\", \"data_count\": 50, \"model_name\": \"Qwen2.5-7B-Instruct + v7 TG LoRA\", \"seed\": \"N/A (eval)\", \"checkpoint_source\": \"phase2_tg_s42_v7\", \"eval_data\": \"50 conversations from eval_200.json, gen mode autoregressive\", \"checkpoint_path\": \"N/A (eval experiment)\", \"log_path\": \"/root/turn_residual_gating/runs/attention_steering/attention_steering_gen_n50.json\"}, \"metrics\": {\"corrected\": true, \"aggregation\": \"per-conv mid_gar(turns 2-7), >=3 turns only\", \"beta_0.0\": {\"mid_gar\": 0.0641, \"mid_gar_std\": 0.0809, \"ppl\": 1.4324, \"ppl_std\": 0.1029, \"n_valid\": 39}, \"beta_2.0\": {\"mid_gar\": 0.128, \"mid_gar_std\": 0.1101, \"ppl\": 1.4822, \"ppl_std\": 0.1385, \"n_valid\": 39}, \"beta_3.0\": {\"mid_gar\": 0.5558, \"mid_gar_std\": 0.0601, \"ppl\": 1.5605, \"ppl_std\": 0.1719, \"n_valid\": 39}, \"beta_4.0\": {\"mid_gar\": 0.6439, \"mid_gar_std\": 0.0607, \"ppl\": 1.6674, \"ppl_std\": 0.2241, \"n_valid\": 39}, \"beta_5.0\": {\"mid_gar\": 0.7271, \"mid_gar_std\": 0.0605, \"ppl\": 1.7723, \"ppl_std\": 0.2693, \"n_valid\": 38}, \"beta_10.0\": {\"mid_gar\": 0.9612, \"mid_gar_std\": 0.0152, \"ppl\": 3.4517, \"ppl_std\": 1.7813, \"n_valid\": 39}, \"n_convs_total\": 50, \"n_convs_valid\": 39, \"mode\": \"gen\", \"phase_transition_range\": \"[2, 3]\"}, \"conclusion\": \"success\", \"notes\": \"原始聚合有 min_turns 截断 bug（截到 2 turns），修正后用 per-conv mid_gar(turns 2-7)。39/50 对话有 ≥3 turns 参与统计。修正后 baseline β=0 GAR 从 0.101 降到 0.064（median 0.031 与 N=5 的 0.028 一致）。Phase transition 在 β∈[2,3] 重现。β=10 corrected 0.961 ≈ N=5 的 0.959。\", \"completed_at\": \"2026-05-20T19:55:34.383Z\"}, \"phase2_tg_s42_v8b_resume\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T10:08:29.483Z\", \"updated_at\": \"2026-05-21T01:56:13.289Z\", \"hypothesis\": \"从 epoch_0 checkpoint resume v8b scheduled sampling 训练。SS 线性混合 0→0.5 teacher-forced + model-generated contexts。如果 model-gen context 上的 GAR 训练能缩小 30x training-inference gap → exposure bias mitigation 有效。成功标准：inference GAR 显著高于 v7 的 0.016 (至少 +1pp)，PPL 不恶化。\", \"parent\": \"phase2_tg_s42_v8b_ss_fixed\", \"spec\": {\"command\": \"python src/train_phase2_v8b.py --model /root/.cache/modelscope/Qwen/Qwen2___5-7B-Instruct --data-dir data/ultrachat_8k --output-dir checkpoints/tg_v8b_ss_fixed_s42 --gate-type threadgate --gar-loss-mode mse_target --gar-target 0.5 --lambda-gar 1.0 --lambda-gate-div 1.0 --init-bias 1.5 --gate-lr-multiplier 10 --lr 2e-4 --epochs 3 --batch-size 1 --grad-accum 8 --seed 42 --scheduled-sampling --ss-max-ratio 0.5 --resume checkpoints/tg_v8b_ss_fixed_s42/epoch_0\", \"server\": \"westd-20861\", \"data_path\": \"data/ultrachat_8k\", \"data_count\": 8000, \"model_name\": \"Qwen2.5-7B-Instruct\", \"seed\": 42, \"checkpoint_source\": \"phase2_tg_s42_v8b_ss_fixed/epoch_0\", \"eval_data\": \"N/A (training experiment)\", \"checkpoint_path\": \"checkpoints/tg_v8b_ss_fixed_s42\", \"log_path\": \"~/runs/turn_residual_gating/phase2_tg_s42_v8b_resume.log\"}, \"metrics\": {\"training\": {\"total_steps\": 3000, \"epochs_completed\": 3, \"wall_clock_hours\": 8.1, \"final_loss\": 0.933, \"final_ntp_loss\": 0.9322, \"final_gar_loss\": 0.0008, \"final_gate_mean\": 0.9586, \"final_gate_std\": 0.0582, \"ss_ratio\": 0.5}, \"eval_iid\": {\"gar_ours\": 0.4983, \"gar_dongre\": 0.3855, \"ppl\": 2.78}, \"eval_modelgen\": {\"gar_ours\": 0.3177, \"gar_dongre\": 0.3533, \"ppl\": 1.38}, \"vs_v7\": {\"iid_gar_ours_delta\": -0.005, \"modelgen_gar_ours_delta\": 0.302, \"gap_ratio_v7\": 32, \"gap_ratio_v8b\": 1.57}}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-20T18:57:21.189Z\"}, \"llama_phase1_gar_diag\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T19:39:25.751Z\", \"updated_at\": \"2026-05-21T01:34:36.417Z\", \"hypothesis\": \"Llama-3.1-8B-Instruct 在 multi-turn dialogue 中也应出现 goal attention decay（与 Qwen-2.5-7B 类似），确认 attention decay 是 transformer 架构通用现象而非模型特有。Phase 1 诊断：测量 base Llama 的 per-turn GAR profile。\", \"spec\": {\"server\": \"westd-20861\", \"gpu\": [\"cuda:0\"], \"account\": \"local\", \"command\": \"CUDA_VISIBLE_DEVICES=0 python src/run_phase1_gar_llama.py --model /root/autodl-tmp/models/LLM-Research/Meta-Llama-3___1-8B-Instruct/ --output-dir /root/turn_residual_gating/runs/phase1_llama_gar_diag --max-new-tokens 256\", \"pid\": \"198817\", \"data_path\": \"built-in 5 conversations (knowledge_qa, coding_help, creative_writing, math_reasoning, debate)\", \"data_count\": 5, \"model_name\": \"Meta-Llama-3.1-8B-Instruct\", \"seed\": 42, \"checkpoint_source\": \"N/A (base model, no fine-tuning)\", \"eval_data\": \"5 built-in conversations x 10 turns each, gen mode\", \"checkpoint_path\": \"N/A\", \"log_path\": \"/root/turn_residual_gating/logs/llama_phase1_gar_diag.log\"}, \"conclusion\": \"success\", \"metrics\": {\"per_turn_gar\": {\"turn_1\": 0.0263, \"turn_2\": 0.0183, \"turn_3\": 0.0087, \"turn_4\": 0.0055, \"turn_5\": 0.006, \"turn_6\": 0.0035, \"turn_7\": 0.0038, \"turn_8\": 0.0037, \"turn_9\": 0.005, \"turn_10\": 0.0026}, \"t1_t10_decay_pct\": 90.1, \"t1_mid38_drop_pct\": 80.2, \"n_topics\": 5, \"model\": \"Meta-Llama-3.1-8B-Instruct\", \"mode\": \"gen\", \"n_conversations\": 5, \"n_turns\": 10}, \"completed_at\": \"2026-05-21T01:34:36.417Z\"}, \"eval_v8b_ss\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T18:44:23.366Z\", \"updated_at\": \"2026-05-20T18:45:14.523Z\", \"hypothesis\": \"Scheduled Sampling (linear 0→0.5 mixing of teacher-forced and model-gen contexts) closes the 30x training-inference GAR gap by reducing exposure bias, resulting in model-gen GAR significantly above v7 baseline (0.016) while preserving IID GAR and PPL.\", \"parent\": \"phase2_tg_s42_v8b_ss\", \"spec\": {\"command\": \"python src/eval_phase2_gar.py --checkpoint-dir checkpoints/tg_v8b_ss_fixed_s42 --gate-type threadgate\", \"server\": \"westd-20861\", \"data_path\": \"data/ultrachat_eval_heldout.json + built-in 5conv model-gen\", \"data_count\": \"50 heldout + 5 model-gen\", \"model_name\": \"Qwen2.5-7B-Instruct\", \"seed\": 42, \"checkpoint_source\": \"checkpoints/tg_v8b_ss_fixed_s42\", \"eval_data\": \"ultrachat_eval_heldout.json (IID) + built-in model-gen (5x10 turns)\", \"checkpoint_path\": \"checkpoints/tg_v8b_ss_fixed_s42\", \"log_path\": \"/tmp/eval_v8b_all.log\"}, \"metrics\": {\"iid_gar_ours\": 0.4983, \"iid_gar_dongre\": 0.3855, \"iid_ppl\": 2.78, \"iid_ngar_ours\": 13.5, \"iid_ngar_dongre\": 22.68, \"modelgen_gar_ours\": 0.3177, \"modelgen_gar_dongre\": 0.3533, \"modelgen_ppl\": 1.38, \"modelgen_ngar_ours\": 4.47, \"modelgen_ngar_dongre\": 5.92, \"iid_turn1_gar_ours\": 0.5398, \"modelgen_turn1_gar_ours\": 0.4333}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-20T18:45:14.523Z\"}, \"attention_steering_eval200_tf\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T09:58:23.626Z\", \"updated_at\": \"2026-05-20T10:08:24.710Z\", \"hypothesis\": \"N=200 TF 模式 attention steering 验证 β-GAR 关系的统计鲁棒性。在 teacher-forced context (无 exposure bias) 下，steering 效果应更温和（baseline GAR 已 ~0.50），但仍展示 β 调控 attention 的能力。与 N=5 gen 模式结果互补：tf 验证机制可控性，gen 验证因果闭环。\", \"parent\": \"attention_steering_v7_tg_gen\", \"spec\": {\"command\": \"python src/eval_attention_steering.py --mode tf --betas 0 2 3 4 5 10 --output-name eval200_attention_steering.json (data: eval_200/eval_200.json, 200 convs)\", \"server\": \"westd-20861\", \"data_path\": \"data/eval_200/eval_200.json\", \"data_count\": 200, \"model_name\": \"Qwen2.5-7B-Instruct\", \"seed\": 42, \"checkpoint_source\": \"phase2_tg_s42_v7\", \"eval_data\": \"data/eval_200/eval_200.json\", \"checkpoint_path\": \"checkpoints/tg_v7_s42/final\", \"log_path\": \"/tmp/eval200_steering.log\"}, \"metrics\": {\"beta_0.0\": {\"mid_gar\": 0.5353, \"ppl\": 2.62}, \"beta_2.0\": {\"mid_gar\": 0.6112, \"ppl\": 2.69}, \"beta_3.0\": {\"mid_gar\": 0.788, \"ppl\": 2.93}, \"beta_4.0\": {\"mid_gar\": 0.8165, \"ppl\": 3.49}, \"beta_5.0\": {\"mid_gar\": 0.8325, \"ppl\": 6.15}, \"beta_10.0\": {\"mid_gar\": 0.977, \"ppl\": 505.21}, \"n_convs\": 200, \"mode\": \"tf\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-20T10:08:24.710Z\"}, \"trc_baseline_v7_tg\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T07:18:17.576Z\", \"updated_at\": \"2026-05-20T09:34:40.734Z\", \"hypothesis\": \"如果 exposure bias 对 auxiliary objectives 的破坏跨特征空间通用，那么 TRC (hidden state cos_sim) 在 model-gen 下也应出现与 GAR (attention 空间) 类似的 TF/gen gap。在 v7 TG / LoRA-only / base 三个 checkpoint 上测量 TRC baseline，确认 gap 是否存在。成功标准：gen TRC 显著低于 TF TRC。\", \"parent\": \"phase2_tg_s42_v7\", \"spec\": {\"command\": \"bash scripts/launch_trc_baseline.sh\", \"server\": \"westd-20861\", \"gpu\": [\"cuda:0\"], \"pid\": \"158700\", \"log_path\": \"/root/runs/turn_residual_gating/trc_baseline_v7_tg.log\", \"submitted_at\": \"2026-05-20T07:18:38.202Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/turn_residual_gating/data/standard_conversations.json\", \"data_count\": 5, \"model_name\": \"Qwen2.5-7B-Instruct\", \"seed\": 42, \"checkpoint_source\": \"phase2_tg_s42_v7 + phase2_lora_only_s42 + base\", \"eval_data\": \"5 hardcoded multi-turn conversations x 10 turns\", \"checkpoint_path\": \"/root/turn_residual_gating/runs/trc_baseline/\", \"wall_clock_seconds\": 7767.7, \"gpu_hours\": 2.16}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-20T09:28:05.853Z\", \"metrics\": {\"v7_tg\": {\"tf_trc\": 0.3339, \"gen_trc\": 0.3323, \"trc_gap\": 0.0016, \"tf_tbp_ppl\": 1.05, \"gen_tbp_ppl\": 1.05}, \"lora_only\": {\"tf_trc\": 0.349, \"gen_trc\": 0.4106, \"trc_gap\": -0.0617, \"tf_tbp_ppl\": 9.5, \"gen_tbp_ppl\": 12}, \"base\": {\"tf_trc\": 0.1494, \"gen_trc\": 0.1494, \"trc_gap\": 0, \"tf_tbp_ppl\": 2.05, \"gen_tbp_ppl\": 2.05}}, \"notes\": \"Cross-space 验证：exposure bias 是 attention-specific。v7 TG: TRC gap = +0.002 (近零)，hidden state 一致性在 TF/gen 之间无差异。对比 GAR 的 30x gap，TRC 无 gap → exposure bias 只扭曲 attention 分布，不影响 hidden state 层面。LoRA-only: 反转 gap (-0.062)，gen TRC 更高但 TBP PPL 严重恶化 (9.5→12.0)——hidden states \\\"坍缩\\\"趋同但信息量下降。Base: 零 gap（但可能有 eval 脚本 bug，gen 模式复用了 TF hidden states）。\"}, \"attention_steering_v7_tg_gen\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T07:07:20.607Z\", \"updated_at\": \"2026-05-20T09:30:17.530Z\", \"hypothesis\": \"推理时向 attention logits 注入 goal-position bias β 可恢复 autoregressive GAR。如果 GAR 从 0.015 显著提升 → 闭合因果环：exposure bias → attention 偏移 → GAR 坍塌 → 手动修正注意力 → GAR 恢复。扫描 β ∈ {0, 0.5, 1.0, 2.0, 5.0, 10.0}，成功标准：GAR > 0.1 且 PPL 不严重恶化。\", \"parent\": \"phase2_tg_s42_v7\", \"spec\": {\"command\": \"bash scripts/launch_attention_steering.sh gen\", \"server\": \"westd-20861\", \"gpu\": [\"cuda:0\"], \"pid\": \"157657\", \"log_path\": \"runs/attention_steering/phase2_tg_s42_v7_attention_steering.json\", \"submitted_at\": \"2026-05-20T07:07:27.678Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/ShareGPT_V3_format_5convs.json\", \"data_count\": 5, \"model_name\": \"Qwen/Qwen2.5-7B-Instruct\", \"seed\": 42, \"checkpoint_source\": \"phase2_tg_s42_v7\", \"eval_data\": \"data/ShareGPT_V3_format_5convs.json\", \"checkpoint_path\": \"checkpoints/tg_v7_s42/final\", \"wall_clock_seconds\": 8551.2, \"gpu_hours\": 2.38}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-20T09:29:58.880Z\", \"metrics\": {\"beta_0.0\": {\"mid_turns_avg_gar\": 0.028, \"avg_ppl\": 1.409}, \"beta_0.5\": {\"mid_turns_avg_gar\": 0.0287, \"avg_ppl\": 1.387}, \"beta_1.0\": {\"mid_turns_avg_gar\": 0.0349, \"avg_ppl\": 1.36}, \"beta_2.0\": {\"mid_turns_avg_gar\": 0.062, \"avg_ppl\": 1.411}, \"beta_5.0\": {\"mid_turns_avg_gar\": 0.6795, \"avg_ppl\": 1.908}, \"beta_10.0\": {\"mid_turns_avg_gar\": 0.959, \"avg_ppl\": 4.22}, \"phase_transition_range\": \"[2, 5]\", \"baseline_gar\": 0.028, \"max_gar_at_acceptable_ppl\": 0.6795, \"max_gar_at_acceptable_ppl_beta\": 5}, \"notes\": \"Attention steering 闭合因果环。β=0→2: GAR 缓升 (0.028→0.062), PPL 不变 (~1.4); β=5: phase transition, GAR 跳至 0.68, PPL 升至 1.91; β=10: GAR 饱和 0.96, PPL 恶化 4.22。成功标准 (GAR>0.1 且 PPL 不严重恶化) 在 β=2 即满足。β∈[2,5] 存在 phase transition。证明：手动修正 attention 指向 goal tokens → 直接恢复 GAR → 确认 exposure bias 通过 attention 偏移导致 GAR 坍塌。\"}, \"phase2_tg_s42_v8b_ss_fixed\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T02:28:58.064Z\", \"updated_at\": \"2026-05-20T09:30:04.080Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/turn_residual_gating && PYTHONUNBUFFERED=1 python src/train_phase2_v8b.py --model /root/.cache/modelscope/Qwen/Qwen2___5-7B-Instruct --data-dir data/ultrachat_8k --output-dir checkpoints/tg_v8b_ss_fixed_s42 --gate-type threadgate --gar-loss-mode mse_target --gar-target 0.5 --lambda-gar 1.0 --lambda-gate-div 1.0 --init-bias 1.5 --gate-lr-multiplier 10 --lr 2e-4 --epochs 3 --batch-size 1 --grad-accum 8 --seed 42 --scheduled-sampling --ss-max-ratio 0.5\\\"\", \"server\": \"westd-20861\", \"gpu\": [\"cuda:0\"], \"pid\": \"133321\", \"log_path\": \"~/runs/turn_residual_gating/phase2_tg_s42_v8b_ss_fixed.log\", \"submitted_at\": \"2026-05-20T02:28:58.001Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/turn_residual_gating/data/ultrachat_8k\", \"data_count\": 8000, \"model_name\": \"Qwen2.5-7B-Instruct\", \"seed\": 42, \"checkpoint_path\": \"/root/turn_residual_gating/checkpoints/tg_v8b_ss_fixed_s42\", \"checkpoint_source\": \"from_scratch\", \"eval_data\": \"N/A\", \"wall_clock_seconds\": 24818.0, \"gpu_hours\": 6.89}, \"hypothesis\": \"Fixed scheduled sampling (D026 三项 bug 修复后): 线性从 0→0.5 混合 teacher-forced + model-generated contexts 计算 GAR loss。如果 model-gen context 上的 GAR 训练能缩小 30x training-inference gap → exposure bias mitigation 有效，paper 从纯 negative 升级为 diagnosis + initial remedy。超参与 v7 一致 (lambda_gar=1.0, MSE+gate_div)，唯一变量是 SS path。成功标准：inference GAR 显著高于 v7 的 0.016 (至少 +1pp)，PPL 不恶化。\", \"parent\": \"phase2_tg_s42_v7\", \"failure_reason\": \"CUDA OOM: CUDA out of memory. Tried to allocate 448.00 MiB. GPU 0 has a total capacity of 94.97 GiB of which 247.19 MiB is free. Including non-PyTorch memory, this process has 50.68 GiB memory in use. Process 157667 has 26.76 GiB memory in use. Process 158713 \", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-20T09:22:35.962Z\", \"notes\": \"CUDA OOM at Epoch 1 Step 4300 (loss.backward). 其他进程共享 GPU 导致显存不足: Process 157667 (26.76GB) + Process 158713 (17.28GB) + PyTorch 自身 45.21GB + 4.81GB reserved > 94.97GB 总容量。训练在 OOM 前正常收敛 (SS ratio=0.5, Loss~1.0, Gate~0.94)。有 epoch_0 checkpoint。需要独占 GPU 重跑。\"}, \"phase2_tg_s42_v7\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T18:17:45.739Z\", \"updated_at\": \"2026-05-20T03:04:19.923Z\", \"hypothesis\": \"MSE 双向 loss (mean_GAR - target)² + gate diversity 正则 F.relu(min_std - gate_std) 从结构上解决恒等退化：MSE 在 GAR > target 时反向惩罚（不再单调推高），gate_div 直接强制层间分化。预期：gate_std 稳定 >0.05 + GAR 收敛到 target=0.5 附近 + NTP 正常收敛。\", \"parent\": \"phase2_tg_s42_v6\", \"metrics\": {\"eval_iid_ours_mid_gar\": 0.5035, \"eval_iid_dongre_mid_gar\": 0.0152, \"eval_iid_ppl\": 2.784, \"eval_heldout_ours_mid_gar\": 0.5035, \"eval_heldout_dongre_mid_gar\": 0.0152, \"eval_heldout_ppl\": 2.78, \"eval_modelgen_ours_mid_gar\": 0.0157, \"eval_modelgen_dongre_mid_gar\": 0.0194, \"eval_modelgen_ppl\": 1.36, \"gate_mean_final\": 0.9336, \"gate_std_final\": 0.0492}, \"spec\": {\"checkpoint_source\": \"from_scratch\", \"eval_data\": \"N/A\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/turn_residual_gating && PYTHONUNBUFFERED=1 python src/train_phase2.py --gate-type threadgate --gar-loss-mode mse_target --gar-target 0.5 --lambda-gar 1.0 --lambda-gate-div 1.0 --min-gate-std 0.05 --init-bias 1.5 --gate-lr-multiplier 10 --max-seq-len 2048 --seed 42 --output-dir /root/turn_residual_gating/runs/phase2_tg_s42_v7 --data-dir /root/turn_residual_gating/data/ultrachat_8k --epochs 3\\\"\", \"server\": \"westd-20861\", \"gpu\": \"cuda:0\", \"data_path\": \"/root/turn_residual_gating/data/ultrachat_8k\", \"data_count\": 8000, \"model_name\": \"Qwen2.5-7B-Instruct\", \"seed\": 42, \"checkpoint_path\": \"/root/turn_residual_gating/runs/phase2_tg_s42_v7\", \"log_path\": \"/root/turn_residual_gating/runs/phase2_tg_s42_v7.log\"}, \"reproduce\": {\"finished_at\": \"2026-05-19T00:48:47.275Z\"}, \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-19T00:48:47.463Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-19T00:48:48.850580+00:00\"}]}, \"notes\": \"训练 3 epoch 完成 (21352s/5.9h)。最终 gate: mean=0.9336, std=0.0492, L3=0.801 L4=0.789 最低。Eval 完成：GAR-ours recovery +0.35pp (mid 0.0157 vs baseline 0.0122), GAR-Dongre recovery +0.72pp (mid 0.0194 vs baseline 0.0122)。Gate dynamic range 最大层: L23 diff=-0.2100, L14 diff=-0.1803。\"}, \"phase2_tg_s42_v9_pcgrad\": {\"status\": \"DONE\", \"retry_count\": 2, \"created_at\": \"2026-05-19T16:13:21.907Z\", \"updated_at\": \"2026-05-20T03:04:17.171Z\", \"hypothesis\": \"PCGrad (Yu et al. NeurIPS 2020) 消除 NTP-GAR 梯度方向冲突后（仅对 gate 参数投影 NTP 梯度到 GAR 梯度正交平面），如果 30x training-inference GAR gap 仍在 → 因果证据证明 exposure bias（非梯度竞争）是 gap 根因。与 v7 对比：相同超参（lambda_gar=1.0, MSE+gate_div），唯一变量是梯度处理方式。成功标准：(1) 梯度 cos_sim 显著改善（从 v7 的 -0.089 提升到 ≥0），(2) 但推理 GAR 仍 ≈ v7 水平（0.016），证明梯度冲突不是 gap 的因。\", \"parent\": \"phase2_tg_s42_v7\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/turn_residual_gating && PYTHONUNBUFFERED=1 python src/train_phase2_v9_pcgrad.py --model /root/.cache/modelscope/Qwen/Qwen2___5-7B-Instruct --data-dir data/ultrachat_8k --output-dir checkpoints/tg_v9_pcgrad_s42 --gate-type threadgate --gar-loss-mode mse_target --gar-target 0.5 --lambda-gar 1.0 --lambda-gate-div 1.0 --init-bias 1.5 --gate-lr-multiplier 10 --lr 2e-4 --epochs 3 --batch-size 1 --grad-accum 8 --seed 42\\\"\", \"server\": \"westd-20861\", \"gpu\": [\"cuda:0\"], \"pid\": \"83860\", \"log_path\": \"/root/turn_residual_gating/logs/phase2_tg_v9_pcgrad_s42.log\", \"submitted_at\": \"2026-05-19T17:42:10.820Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_path\": \"/root/turn_residual_gating/checkpoints/tg_v9_pcgrad_s42\", \"wall_clock_seconds\": 30601.5, \"gpu_hours\": 8.5}, \"reproduce\": {\"finished_at\": \"2026-05-20T01:42:12.536Z\"}, \"failure_reason\": null, \"conclusion\": \"success\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-19T17:35:39.776243+00:00\", \"note\": \"第1次提交 EXIT_CODE=2 残留事件\"}, {\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-20T01:42:14.275822+00:00\"}]}, \"completed_at\": null, \"notes\": \"D028 因果排除确认（M017 修正后）。训练: EXIT_CODE=0, 7.98h, 3 epochs。PCGrad cos_sim 从 -0.061→+0.055→-0.035 (围绕 0 振荡), NTP mag_ratio 2.8→28.8 持续增长。L_GAR 有 0-350 step 高原期后仍坍塌到≈0。IID eval (同 protocol 50 heldout convs): GAR-ours=0.5002 (vs v7 0.5035, diff -0.33pp), GAR-Dongre=0.0123 (vs v7 0.0152), PPL=2.780 (vs v7 2.784, diff 0.004, 无改善)。Model-gen eval (5 convs): GAR-ours=0.0151, PPL=1.50。结论: PCGrad 消除梯度方向冲突后所有 IID 指标均 ≈ v7（GAR、PPL、NTP 无变化），方向冲突因 NTP 幅度主导 (10-40x) 而 inconsequential。Exposure bias 是 30x gap 根因。\", \"metrics\": {\"eval_iid_ours_mid_gar\": 0.5002, \"eval_iid_dongre_mid_gar\": 0.0123, \"eval_iid_ppl\": 2.78, \"eval_iid_ntp\": 0.9752, \"eval_heldout_ours_mid_gar\": 0.5002, \"eval_heldout_dongre_mid_gar\": 0.0123, \"eval_heldout_ppl\": 2.78, \"eval_heldout_ntp\": 0.9752, \"eval_modelgen_ours_mid_gar\": 0.0151, \"eval_modelgen_dongre_mid_gar\": 0.0173, \"eval_modelgen_ppl\": 1.5, \"vs_v7_iid_ppl_diff\": 0.004, \"vs_v7_iid_gar_diff\": -0.0033}}, \"phase2_lora_only_s42\": {\"status\": \"DONE\", \"retry_count\": 1, \"created_at\": \"2026-05-18T20:36:32.506Z\", \"updated_at\": \"2026-05-20T02:15:18.992Z\", \"hypothesis\": \"LoRA-only baseline (gate 固定 1.0，无 gating 机制) 在相同 MSE+NTP loss 下 GAR 应低于 ThreadGate (v7)。如果 LoRA-only 也能训到 GAR~0.5，则 gating 机制贡献为零，paper story 不成立。关键对比：LoRA-only 的 GAR 收敛值 vs v7 的 0.48。\", \"parent\": \"phase2_tg_s42_v7\", \"failure_reason\": \"EXIT_CODE=1 (generic error — check log tail)\", \"completed_at\": \"2026-05-19T12:44:29.475Z\", \"extra\": {\"previous_failure\": {\"conclusion\": \"failed\"}, \"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-19T13:04:35.644174+00:00\"}]}, \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/turn_residual_gating && PYTHONUNBUFFERED=1 python src/train_phase2.py --gate-type lora_only --gar-loss-mode mse_target --gar-target 0.5 --lambda-gar 1.0 --lambda-gate-div 0.0 --init-bias 1.5 --gate-lr-multiplier 10 --max-seq-len 2048 --seed 42 --output-dir /root/turn_residual_gating/runs/phase2_lora_only_s42 --data-dir /root/turn_residual_gating/data/ultrachat_8k --epochs 3\\\"\", \"server\": \"westd-20861\", \"gpu\": \"cuda:0\", \"data_path\": \"/root/turn_residual_gating/data/ultrachat_8k\", \"data_count\": 8000, \"model_name\": \"Qwen2.5-7B-Instruct\", \"seed\": 42, \"checkpoint_path\": \"/root/turn_residual_gating/runs/phase2_lora_only_s42\", \"log_path\": \"/root/turn_residual_gating/runs/phase2_lora_only_s42.log\", \"checkpoint_source\": \"from_scratch\", \"eval_data\": \"N/A\"}, \"reproduce\": {\"finished_at\": \"2026-05-19T13:04:33.523Z\"}, \"conclusion\": \"success\", \"metrics\": {\"epochs_completed\": 3, \"global_steps\": 3000, \"training_time_seconds\": 20588.6, \"training_time_hours\": 5.7, \"gate_fixed\": 1, \"gate_type_actual\": \"none\", \"final_lora_size_mb\": 20, \"eval_modelgen_ours_mid_gar\": 0.0245, \"eval_modelgen_dongre_mid_gar\": 0.0185, \"eval_modelgen_ppl\": 1.371}, \"checkpoint_path\": \"/root/runs/turn_residual_gating/runs/phase2_lora_only_s42/lora/\", \"log_path\": \"/root/runs/turn_residual_gating/phase2_lora_only_s42.log\", \"notes\": \"诊断确认：EXIT_CODE=1 因 argparse 不认 lora_only 选项（choices 只有 threadgate/uniform/none）。训练实际已用 --gate-type none 完成 3 epoch (3000 steps, 20588.6s/5.7h)。Gate 全程固定 1.0（符合 lora_only 语义）。Checkpoint 可用，无需重跑。修复：dispatch 命令改用 --gate-type none 或在 train_phase2.py 添加 lora_only choice。\"}, \"phase2_ug_s42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T06:04:17.643Z\", \"updated_at\": \"2026-05-20T02:15:15.775Z\", \"hypothesis\": \"Uniform gating baseline: per-layer independent gates without turn conditioning (content-dependent only), to isolate whether ThreadGate's turn-conditioned gating provides benefit over content-only residual scaling. Same training setup as v7 but with gate-type=uniform.\", \"parent\": \"phase1_gar_diag\", \"notes\": \"3 epoch 完成 (21994.5s/6.1h)。最终 gate: mean=0.9598, std=0.0518, L3=0.777 L5=0.812 最低。重要发现：uniform gate 模式下各层仍学出 per-layer 分化（L3=0.777 vs L27=1.000），与 ThreadGate v7 的 L3/L4 最低模式一致。这说明 per-layer variation 可能来自 LoRA+GAR loss 而非 gate architecture。\", \"spec\": {\"command\": \"python src/train_phase2.py --gate-type uniform --gar-loss-mode mse_target --gar-target 0.5 --lambda-gar 1.0 --lambda-gate-div 1.0 --min-gate-std 0.05 --init-bias 1.5 --gate-lr-multiplier 10 --max-seq-len 2048 --seed 42 --output-dir /root/turn_residual_gating/runs/phase2_ug_s42 --data-dir /root/turn_residual_gating/data/ultrachat_8k --epochs 3\", \"server\": \"westd-20861\", \"data_path\": \"/root/turn_residual_gating/data/ultrachat_8k\", \"data_count\": 8000, \"model_name\": \"Qwen2.5-7B-Instruct\", \"seed\": 42, \"checkpoint_path\": \"/root/turn_residual_gating/runs/phase2_ug_s42\", \"log_path\": \"/root/turn_residual_gating/runs/phase2_ug_s42.log\", \"checkpoint_source\": \"from_scratch\", \"eval_data\": \"N/A\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-19T06:53:13.931Z\", \"metrics\": {\"epoch0_avg_loss\": 1.0019, \"epoch0_avg_ntp\": 0.9755, \"epoch0_avg_gar\": 0.0259, \"epoch0_avg_div\": 0.0005, \"epoch1_avg_loss\": 0.9447, \"epoch1_avg_ntp\": 0.9435, \"epoch1_avg_gar\": 0.0013, \"epoch1_avg_div\": 0, \"epoch2_avg_loss\": 0.9319, \"epoch2_avg_ntp\": 0.9309, \"epoch2_avg_gar\": 0.001, \"epoch2_avg_div\": 0, \"final_gate_mean\": 0.9598, \"final_gate_std\": 0.0518, \"final_gate_min\": 0.7773, \"final_gate_max\": 1, \"final_profile_L3\": 0.777, \"final_profile_L5\": 0.812, \"final_profile_L0\": 0.875, \"final_profile_L27\": 1, \"training_time_seconds\": 21994.5, \"training_time_hours\": 6.1, \"global_steps\": 7950, \"unexpected_per_layer_variation\": true, \"eval_modelgen_ours_mid_gar\": 0.0149, \"eval_modelgen_dongre_mid_gar\": 0.0185, \"eval_modelgen_ppl\": 1.396}, \"checkpoint_path\": \"/root/turn_residual_gating/runs/phase2_ug_s42\", \"log_path\": \"/root/turn_residual_gating/runs/phase2_ug_s42.log\"}, \"phase2_tg_s42_v8_schedsampling\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T15:02:00.223Z\", \"updated_at\": \"2026-05-19T16:33:04.989Z\", \"hypothesis\": \"Scheduled sampling 应用到 GAR loss（线性从 0→0.5 混合 teacher-forced + model-generated contexts）能缩小 v7 的 30x training-inference GAR gap。机制：在 model-generated context 上计算 GAR loss 迫使 attention pattern 适应推理时分布，直接 address teacher-forcing distribution shift。成功标准：inference GAR 显著高于 v7 的 0.016，PPL 不显著恶化（≤2.78+0.2）。\", \"parent\": \"phase2_tg_s42_v7\", \"spec\": {\"command\": \"python src/train_phase2_v8.py --scheduled-sampling --ss-max-ratio 0.5\", \"server\": \"westd-20861\", \"gpu\": \"cuda:0\", \"pid\": 73838, \"log_path\": \"/root/turn_residual_gating/runs/phase2_tg_s42_v8_schedsampling/\", \"submitted_at\": \"2026-05-19T15:43:01.461Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/turn_residual_gating/data/ultrachat_8k\", \"data_count\": 8000, \"model_name\": \"Qwen2.5-7B-Instruct\", \"seed\": 42, \"checkpoint_source\": \"N/A (training from scratch with LoRA)\", \"eval_data\": \"ultrachat_eval_heldout.json (post-training eval)\", \"hyperparams\": {\"lr\": 0.0002, \"epochs\": 3, \"grad_accum\": 8, \"ss_max_ratio\": 0.5, \"ss_gen_max_tokens\": 256, \"ss_gen_temperature\": 0.7}, \"estimated_hours\": \"8-9\", \"checkpoint_path\": \"N/A (crashed at 5.8%)\", \"wall_clock_seconds\": 1611.0, \"gpu_hours\": 0.45}, \"conclusion\": \"failed\", \"completed_at\": \"2026-05-19T16:09:52.423Z\", \"metrics\": {\"killed_at_microstep\": 1950, \"total_microsteps\": 24000, \"completion_pct\": 8.1, \"global_step_approx\": 244, \"total_global_steps\": 3000, \"ss_steps_observed\": 1, \"tf_lgar_mean_step850_1400\": 0.0062, \"tf_lgar_std\": 0.0082, \"tf_lgar_collapse_step\": 800, \"gate_mean_final\": 0.93, \"ss_ratio_at_kill\": 0.081, \"crash_reason\": \"killed by director: SS path code bug (D026) makes experiment invalid, GPU needed for PCGrad\", \"design_flaw_ss_ramp_too_slow\": true, \"design_flaw_no_ss_tf_separate_logging\": true}, \"notes\": \"Director kill at micro-step ~1950 (8.1%). 原因: SS path code bug (D026) + GAR-ours 无推理 gap (D024)，实验无效。GPU 转入 plan_018 PCGrad。详情：(1) SS ratio 仅 0.081 时 kill，仅 1 条 SS step 被日志捕获，(2) TF L_GAR 在 step 800 坍塌到 ≈0.006（与 v7 一致），(3) GAR-ours 推理时 ≈0.50 ≈ target，SS 用 GAR-ours 训练无法验证 exposure bias mitigation，(4) lambda_gar=2.0 (vs v7 的 1.0) confound 未被充分触发。\"}, \"analysis_attention_heatmap\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T15:03:16.154Z\", \"updated_at\": \"2026-05-19T15:22:24.770Z\", \"hypothesis\": \"四模型（Base/TG/UG/LoRA-only）的 goal attention 衰减模式是否一致？如果 TG 的 attention decay 与 LoRA-only 无差异，则 gating 机制对 attention 分布零增量。\", \"parent\": \"phase2_tg_s42_v7\", \"spec\": {\"command\": \"attention heatmap analysis script\", \"server\": \"westd-20861\", \"data_path\": \"standard_conversations.json\", \"data_count\": 5, \"model_name\": \"Qwen2.5-7B-Instruct\", \"seed\": 42, \"checkpoint_source\": \"phase2_tg_s42_v7 + phase2_ug_s42 + phase2_lora_only_s42\", \"eval_data\": \"standard_conversations.json (5 convs x 10 turns)\", \"checkpoint_path\": \"N/A (analysis)\", \"log_path\": \"westd-20861:/root/turn_residual_gating/runs/analysis/\"}, \"conclusion\": \"success\", \"metrics\": {\"base_mean_goal_attn\": 0.0136, \"base_decay\": 0.875, \"tg_mean_goal_attn\": 0.0232, \"tg_decay\": 0.777, \"ug_mean_goal_attn\": 0.0216, \"ug_decay\": 0.803, \"lora_mean_goal_attn\": 0.0216, \"lora_decay\": 0.81, \"gating_incremental_benefit\": \"none\"}, \"completed_at\": \"2026-05-19T15:22:24.770Z\"}, \"analysis_gradient_conflict\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T15:03:12.230Z\", \"updated_at\": \"2026-05-19T15:22:23.782Z\", \"hypothesis\": \"NTP-GAR 梯度冲突在 v7 训练过程中是否逐层普遍存在？量化 cos_sim 和 magnitude ratio 的演化，验证 NTP 是否在训练中逐渐完全压制 GAR 信号。\", \"parent\": \"phase2_tg_s42_v7\", \"spec\": {\"command\": \"gradient conflict analysis script\", \"server\": \"westd-20861\", \"data_path\": \"v7 epoch 0/1/2 checkpoints\", \"data_count\": 3, \"model_name\": \"Qwen2.5-7B-Instruct\", \"seed\": 42, \"checkpoint_source\": \"phase2_tg_s42_v7\", \"eval_data\": \"v7 3-epoch checkpoints (gradient analysis)\", \"checkpoint_path\": \"N/A (analysis)\", \"log_path\": \"westd-20861:/root/turn_residual_gating/runs/analysis/\"}, \"conclusion\": \"success\", \"metrics\": {\"epoch0_cos_sim\": -0.089, \"epoch1_cos_sim\": -0.054, \"epoch2_cos_sim\": -0.042, \"epoch0_neg_layers_pct\": 78.6, \"epoch1_neg_layers_pct\": 71.4, \"epoch2_neg_layers_pct\": 67.9, \"epoch0_mag_ratio\": 7.5, \"epoch1_mag_ratio\": 13.7, \"epoch2_mag_ratio\": 14.7}, \"completed_at\": \"2026-05-19T15:22:23.782Z\"}, \"phase2_4way_eval_heldout\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T13:58:59.269Z\", \"updated_at\": \"2026-05-19T14:35:47.201Z\", \"hypothesis\": \"四路消融的三路趋同结论（TG≈UG≈LoRA-only，gating 零增量）在 held-out eval 数据（idx≥8000，与训练集无重叠）上复现，排除数据重叠 confound。预期：相对比较保持（三路趋同），绝对 GAR 值可能变化。\", \"parent\": \"phase2_4way_eval\", \"spec\": {\"command\": \"bash -c \\\"cd /root/turn_residual_gating && bash scripts/run_4way_eval_heldout.sh\\\"\", \"server\": \"westd-20861\", \"gpu\": \"cuda:0\", \"pid\": 67204, \"log_path\": \"~/runs/turn_residual_gating/phase2_4way_eval_heldout.log\", \"submitted_at\": \"2026-05-19T14:01:00.965Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/turn_residual_gating/data/ultrachat_eval_heldout.json\", \"data_count\": 50, \"model_name\": \"Qwen2.5-7B-Instruct\", \"seed\": 42, \"checkpoint_source\": \"phase2_tg_s42_v7 + phase2_ug_s42 + phase2_lora_only_s42\", \"eval_data\": \"ultrachat_eval_heldout.json (50 convs, idx 8843-68199, no overlap with training 0-7999)\", \"configs\": \"4 models (Base/TG_v7/UG/LoRA-only) x 2 GAR variants (ours/Dongre) = 8 eval runs\", \"checkpoint_path\": \"N/A (eval-only)\", \"wall_clock_seconds\": 2086.2, \"gpu_hours\": 0.58}, \"reproduce\": {\"finished_at\": \"2026-05-19T14:32:09.481Z\"}, \"metrics\": {\"base_ours_mid_gar\": 0.0128, \"base_ours_recovery_pp\": 0.06, \"base_dongre_mid_gar\": 0.0031, \"base_dongre_recovery_pp\": -0.91, \"base_ppl\": 4.34, \"base_ntp\": 1.4045, \"tg_ours_mid_gar\": 0.5035, \"tg_ours_recovery_pp\": 49.13, \"tg_dongre_mid_gar\": 0.0152, \"tg_dongre_recovery_pp\": 0.3, \"tg_ppl\": 2.78, \"tg_ntp\": 0.9771, \"ug_ours_mid_gar\": 0.5053, \"ug_ours_recovery_pp\": 49.31, \"ug_dongre_mid_gar\": 0.0124, \"ug_dongre_recovery_pp\": 0.02, \"ug_ppl\": 2.78, \"ug_ntp\": 0.9752, \"lora_ours_mid_gar\": 0.4978, \"lora_ours_recovery_pp\": 48.56, \"lora_dongre_mid_gar\": 0.0132, \"lora_dongre_recovery_pp\": 0.1, \"lora_ppl\": 2.78, \"lora_ntp\": 0.9771, \"three_way_convergence_confirmed\": true, \"gar_ours_spread_pp\": 0.75, \"ppl_spread\": 0, \"data_overlap\": false}, \"conclusion\": \"success\", \"notes\": \"Held-out eval 三路趋同完全复现。TG/UG/LoRA-only GAR-ours: 0.504/0.505/0.498 (spread 0.75pp), PPL 均为 2.78。与 overlap 数据相比绝对值略高（GAR +1-2pp, PPL +0.15），属正常泛化偏移，相对比较完全一致。数据完整性 confound 已排除。\", \"completed_at\": \"2026-05-19T14:35:47.202Z\"}, \"phase2_4way_eval\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T13:07:30.673Z\", \"updated_at\": \"2026-05-19T13:15:39.947Z\", \"hypothesis\": \"Turn-residual gating (TRG) improves multi-turn response quality over LoRA-only and base model baselines because it selectively amplifies conversational context signals, which should manifest as higher GAR scores across 4 conditions (base, base+TRG, LoRA, LoRA+TRG).\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/turn_residual_gating && bash scripts/run_4way_eval.sh 2>&1 | tee runs/4way_eval.log\\\"\", \"server\": \"westd-20861\", \"gpu\": [\"cuda:0\"], \"pid\": \"60024\", \"log_path\": \"/root/turn_residual_gating/runs/4way_eval.log\", \"submitted_at\": \"2026-05-19T13:07:37.380Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/turn_residual_gating/data/ultrachat_8k\", \"data_count\": 8000, \"model_name\": \"Qwen2.5-7B-Instruct\", \"seed\": 42, \"checkpoint_source\": \"phase2_tg_s42_v7 + phase2_ug_s42 + phase2_lora_only_s42\", \"eval_data\": \"ultrachat_8k eval split\", \"checkpoint_path\": \"/root/turn_residual_gating/runs/4way_eval/\", \"wall_clock_seconds\": 447.0, \"gpu_hours\": 0.12}, \"parent\": \"phase2_tg_s42_v7\", \"conclusion\": \"negative\", \"completed_at\": \"2026-05-19T13:15:04.405Z\", \"metrics\": {\"base_ours_mid_gar\": 0.0107, \"base_ours_recovery_pp\": -0.15, \"base_dongre_mid_gar\": 0.003, \"base_dongre_recovery_pp\": -0.92, \"base_ppl\": 4.23, \"base_ntp\": 1.4162, \"tg_ours_mid_gar\": 0.4866, \"tg_ours_recovery_pp\": 47.44, \"tg_dongre_mid_gar\": 0.0157, \"tg_dongre_recovery_pp\": 0.35, \"tg_ppl\": 2.63, \"tg_ntp\": 0.9484, \"ug_ours_mid_gar\": 0.4923, \"ug_ours_recovery_pp\": 48.01, \"ug_dongre_mid_gar\": 0.013, \"ug_dongre_recovery_pp\": 0.08, \"ug_ppl\": 2.62, \"ug_ntp\": 0.9433, \"lora_ours_mid_gar\": 0.486, \"lora_ours_recovery_pp\": 47.39, \"lora_dongre_mid_gar\": 0.0137, \"lora_dongre_recovery_pp\": 0.15, \"lora_ppl\": 2.63, \"lora_ntp\": 0.9482, \"route_b_confirmed\": true, \"gating_incremental_benefit\": \"none\"}, \"notes\": \"四路 eval 完成，Route B 决定性确认。三种训练方法（TG/UG/LoRA-only）在推理端完全趋同：ours GAR recovery ~47-48pp（vs base -0.15pp），dongre GAR recovery 0.08-0.35pp，PPL 2.62-2.63，NTP 0.943-0.948。Gating 机制（无论 turn-conditioned 还是 uniform）相比纯 LoRA 微调零增量。LoRA fine-tuning 是 GAR recovery 的唯一来源。hypothesis 被证伪：TRG 不比 LoRA-only 更好。\"}, \"phase2_tg_s42_v5\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T17:10:23.229Z\", \"updated_at\": \"2026-05-18T17:52:54.605Z\", \"hypothesis\": \"重新平衡超参（λ=1.0 降 GAR 贡献至 ~50%，init_bias=1.5 使 sigmoid≈0.82 接近正常模型行为，gate_lr_multiplier=10 保持）能在 3-epoch 全量训练中产生有意义的 gate 分化（gate_std>0.05），同时 GAR 稳态在 0.1-0.5（非病态饱和），NTP loss 正常收敛，总 loss 保持正值\", \"parent\": \"phase2_tg_s42_v4\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/turn_residual_gating && PYTHONUNBUFFERED=1 python src/train_phase2.py --gate-type threadgate --gar-loss-mode maximize --lambda-gar 1.0 --init-bias 1.5 --gate-lr-multiplier 10 --max-seq-len 2048 --seed 42 --output-dir /root/turn_residual_gating/runs/phase2_tg_s42_v5 --data-dir /root/turn_residual_gating/data/ultrachat_8k --epochs 3\\\"\", \"server\": \"westd-20861\", \"gpu\": \"cuda:0\", \"pid\": \"3639\", \"log_path\": \"~/runs/turn_residual_gating/phase2_tg_s42_v5.log\", \"submitted_at\": \"2026-05-18T17:10:30.573Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/turn_residual_gating/data/ultrachat_8k\", \"data_count\": 8000, \"model_name\": \"Qwen/Qwen2.5-7B-Instruct\", \"seed\": 42, \"checkpoint_path\": \"/root/turn_residual_gating/runs/phase2_tg_s42_v5\", \"checkpoint_source\": \"from_scratch\", \"eval_data\": \"N/A\", \"wall_clock_seconds\": 2539.4, \"gpu_hours\": 0.71}, \"metrics\": {\"step2000_gate_std\": 0.0225, \"step2000_gate_mean\": 0.9586, \"step2000_gate_min\": 0.9062, \"step2000_gate_max\": 0.9961, \"step2000_L_GAR\": -0.8977, \"step2000_L_NTP\": 0.7611, \"step2000_total_loss\": -0.1365, \"step2400_gate_std\": 0.0219, \"step2400_gate_mean\": 0.9651, \"step2400_gate_min\": 0.918, \"step2400_gate_max\": 0.9961, \"step2400_profile\": \"L0=0.918 L12=0.918 L13=0.926 L1=0.996 L26=0.996\", \"L_GAR_saturated_at\": -0.91, \"gate_range_compression\": \"0.918-0.996\"}, \"conclusion\": \"negative\", \"completed_at\": \"2026-05-18T17:52:49.951Z\", \"notes\": \"maximize 模式 gate 分化失败：gate_std=0.022↓ gate_mean=0.965↑，与 v3/v3b 同类结构性问题。L_GAR 饱和在 -0.91，maximize 的无界性驱动 gate 趋向恒等（全通过=最大 GAR），丧失层选择性。D009 指令立即 kill，转 v6 smooth_saturation。\"}, \"phase2_tg_s42_v4\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T14:58:00.124Z\", \"updated_at\": \"2026-05-18T16:50:36.202Z\", \"hypothesis\": \"重新平衡超参（λ=1.0 降 GAR 贡献至 ~50%，init_bias=1.5 使 sigmoid≈0.82 接近正常模型行为，gate_lr_multiplier=10 保持）能在 3-epoch 全量训练中产生有意义的 gate 分化（gate_std>0.05），同时 GAR 稳态在 0.1-0.5（非病态饱和），NTP loss 正常收敛，总 loss 保持正值\", \"parent\": \"phase2_tg_s42_v3b\", \"spec\": {\"command\": \"python src/train_phase2.py --gate-type threadgate --gar-loss-mode maximize --lambda-gar 1.0 --init-bias 1.5 --gate-lr-multiplier 10 --max-seq-len 2048 --seed 42 --output-dir /root/turn_residual_gating/runs/phase2_tg_s42_v4 --data-dir /root/turn_residual_gating/data/ultrachat_8k --epochs 3\", \"server\": \"westd-20861\", \"gpu\": \"cuda:0\", \"pid\": \"36519\", \"data_path\": \"/root/turn_residual_gating/data/ultrachat_8k\", \"data_count\": 8000, \"model_name\": \"Qwen/Qwen2.5-7B-Instruct\", \"seed\": 42, \"checkpoint_path\": \"/root/turn_residual_gating/runs/phase2_tg_s42_v4\", \"log_path\": \"/root/turn_residual_gating/runs/phase2_tg_s42_v4.log\", \"checkpoint_source\": \"from_scratch\", \"eval_data\": \"N/A\"}, \"conclusion\": \"failed\", \"completed_at\": \"2026-05-18T16:50:33.778Z\", \"notes\": \"进程在模型加载后崩溃，服务器重启导致进程丢失，无 checkpoint。日志仅有模型加载输出，无训练 step。GPU 重启后异常（100% util + 0 MiB + 无进程）。需要 GPU 健康恢复后重跑。\"}, \"phase2_tg_s42_v3b\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T13:38:16.020Z\", \"updated_at\": \"2026-05-18T14:51:42.486Z\", \"hypothesis\": \"λ=10 + gate_lr=10x + init_bias=0.0 (sigmoid=0.5) 能否驱动 gate 产生 layer 间分化 (gate_std>0.05)？如果 500 步后 gate_std<0.02 且无选择性 → GAR-driven gating 梯度路径确认失败，需要 pivot\", \"parent\": \"phase2_tg_s42_v3\", \"spec\": {\"command\": \"python src/train_phase2.py --gate-type threadgate --gar-loss-mode maximize --lambda-gar 10.0 --init-bias 0.0 --gate-lr-multiplier 10 --max-seq-len 2048 --seed 42 --output-dir /root/turn_residual_gating/runs/phase2_tg_s42_v3b --data-dir /root/turn_residual_gating/data/ultrachat_8k --max-steps 500\", \"server\": \"westd-20861\", \"data_path\": \"/root/turn_residual_gating/data/ultrachat_8k\", \"data_count\": 8000, \"model_name\": \"Qwen2.5-7B-Instruct\", \"seed\": 42, \"checkpoint_source\": \"from_scratch\", \"eval_data\": \"N/A\", \"checkpoint_path\": \"/root/turn_residual_gating/runs/phase2_tg_s42_v3b\", \"log_path\": \"/root/turn_residual_gating/runs/v3b_log.txt\"}, \"conclusion\": \"success\", \"metrics\": {\"gate_std_final\": 0.087, \"gate_mean_final\": 0.9388, \"gate_min_final\": 0.5352, \"gate_max_final\": 0.9922, \"L4_gate\": 0.535, \"L0_gate\": 0.777, \"L_NTP_final\": 0.7787, \"L_GAR_final\": -0.9606, \"elapsed_seconds\": 3565.9, \"optimizer_steps\": 500, \"gate_grad_received\": true}, \"completed_at\": \"2026-05-18T14:51:42.486Z\"}, \"phase2_tg_s42_v3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T13:07:54.463Z\", \"updated_at\": \"2026-05-18T13:38:10.723Z\", \"hypothesis\": \"ThreadGate + maximize GAR loss (L_GAR=-mean(GAR)) 提供持续非零梯度，避免 hinge loss 的退化平衡点，gate 值应随训练下降（学习到选择性干预），同时 NTP loss 正常收敛\", \"parent\": \"phase2_tg_s42_v2\", \"spec\": {\"server\": \"westd-20861\", \"gpu\": \"cuda:0\", \"data_path\": \"/root/turn_residual_gating/data/ultrachat_8k\", \"data_count\": 8000, \"model_name\": \"Qwen/Qwen2.5-7B-Instruct\", \"seed\": 42, \"command\": \"python src/train_phase2.py --gate-type threadgate --gar-loss-mode maximize --lambda-gar 2.0 --init-bias 2.0 --max-seq-len 2048 --seed 42 --output-dir /root/turn_residual_gating/runs/phase2_tg_s42_v3 --data-dir /root/turn_residual_gating/data/ultrachat_8k\", \"pid\": \"30973\", \"log_path\": \"/root/turn_residual_gating/runs/phase2_tg_s42_v3.log\", \"checkpoint_source\": \"N/A (training from scratch with LoRA)\", \"eval_data\": \"N/A (training experiment, not eval)\", \"checkpoint_path\": \"/root/turn_residual_gating/runs/phase2_tg_s42_v3\"}, \"server\": \"westd-20861\", \"gpu\": \"cuda:0\", \"conclusion\": \"negative\", \"metrics\": {\"gate_mean_step0\": 0.8743, \"gate_mean_step500\": 0.8761, \"gate_delta\": 0.004, \"gate_std\": 0.001, \"final_ntp_loss\": 0.94, \"final_gar_loss\": -0.019, \"gar_contribution_pct\": \"2-4%\", \"diagnosis\": \"gate frozen, GAR indirect gradient too weak\"}, \"completed_at\": \"2026-05-18T13:38:10.723Z\"}, \"phase2_tg_s42_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T11:13:37.042Z\", \"updated_at\": \"2026-05-18T13:11:26.331Z\", \"hypothesis\": \"ThreadGate + 修复后的 cumulative GAR loss (ε=0.001) 在 L_NTP+L_GAR 联合训练后，mid-turn GAR recovery 应显著优于 v1 (NTP-only baseline)，验证 GAR loss 的有效性\", \"parent\": \"phase2_tg_s42\", \"server\": \"westd-20861\", \"gpu\": \"cuda:0\", \"reproduce\": {\"server\": \"westd-20861\", \"gpu\": \"cuda:0\", \"started_at\": \"2026-05-18T11:45:26.657Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/turn_residual_gating/src && python train_phase2.py --gate-type threadgate --seed 42 --output-dir /root/turn_residual_gating/checkpoints/tg_s42_v2 --data-dir /root/turn_residual_gating/data/ultrachat_8k --max-seq-len 2048 --gar-loss-mode cumulative --gar-epsilon 0.001 --init-bias 2.0 --lambda-gar 5.0\\\"\"}, \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/turn_residual_gating/src && python train_phase2.py --gate-type threadgate --seed 42 --output-dir /root/turn_residual_gating/checkpoints/tg_s42_v2 --data-dir /root/turn_residual_gating/data/ultrachat_8k --max-seq-len 2048 --gar-loss-mode cumulative --gar-epsilon 0.001 --init-bias 2.0 --lambda-gar 5.0\\\"\", \"server\": \"westd-20861\", \"gpu\": [\"cuda:0\"], \"pid\": \"25726\", \"log_path\": \"~/runs/turn_residual_gating/phase2_tg_s42_v2.log\", \"submitted_at\": \"2026-05-18T11:50:47.143Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_path\": \"/root/turn_residual_gating/checkpoints/tg_s42_v2\", \"wall_clock_seconds\": 4839.2, \"gpu_hours\": 1.34}, \"pid\": \"25726\", \"log_path\": \"~/runs/turn_residual_gating/phase2_tg_s42_v2.log\", \"conclusion\": \"killed\", \"completed_at\": \"2026-05-18T13:11:26.331Z\"}, \"phase1_gar_diag\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T05:24:07.903Z\", \"updated_at\": \"2026-05-18T05:59:25.324Z\", \"hypothesis\": \"Qwen2.5-7B-Instruct 在 10-turn 多轮对话中，中间 turns (3-8) 的 GAR (Goal Accessibility Ratio) 相对 turn-1 下降 ≥15%，表明模型对 system prompt 中目标 token 的注意力随对话进行显著衰减\", \"spec\": {\"command\": \"python run_phase1_gar.py --results-dir /root/turn_residual_gating/results\", \"server\": \"westd-20861\", \"model_name\": \"Qwen/Qwen2.5-7B-Instruct\", \"data_path\": \"built-in 5 conversations (knowledge_qa, coding_help, creative_writing, math_reasoning, roleplay_advisor)\", \"data_count\": 5, \"seed\": 0, \"checkpoint_path\": \"N/A\", \"log_path\": \"/root/turn_residual_gating/results/phase1_run.log\"}, \"conclusion\": \"success\", \"metrics\": {\"turn1_avg_gar\": 0.0418, \"mid_turns_avg_gar\": 0.0122, \"relative_drop\": 0.708, \"num_conversations\": 5, \"num_turns\": 10, \"per_turn_avg_gar\": [0.0418, 0.0241, 0.0224, 0.013, 0.0133, 0.0086, 0.0078, 0.008, 0.0157, 0.0064]}, \"completed_at\": \"2026-05-18T05:59:25.325Z\"}}, \"count\": 60, \"total\": 60, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.2026}}"
    }
  },
  "sourceToolAssistantUUID": "6d8da05e-bd62-45a5-b18b-47925df8341a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "4b680861-4da7-411a-8744-3dabfdaf2205",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-25T20:38:04.359Z_

<details><summary>↩ Tool result · `toolu_018knEN2Q5qeZ3Us2sQprXnf`</summary>

```text
1	\begin{abstract}
2	As multi-turn conversations grow longer, large language models progressively lose attention to the system-prompt goals that define their task, even when the underlying goal representations remain intact. Existing remedies operate at inference time, leaving a natural but untested alternative: training auxiliary attention losses alongside next-token prediction to directly optimize goal attention. This strategy assumes that attention patterns learned under teacher forcing will transfer to autoregressive generation, an assumption that classical exposure bias research has challenged for sequence models but that has never been examined for auxiliary attention objectives in multi-turn transformers.
3	We show this assumption fails. On a controlled five-way testbed spanning two architectures (Qwen-2.5-7B, Llama-3.1-8B), goal attention optimized to target under teacher forcing collapses by an order of magnitude under autoregressive generation. A causal exclusion chain traces the failure to exposure bias, ruling out gradient conflict, gating mechanism, and parameter capacity as primary causes. Inference-time attention steering confirms that the collapse reflects attention misallocation rather than representation loss. Scheduled sampling, applied here for the first time to auxiliary attention objectives in multi-turn transformers, compresses the training--inference gap to near parity on Qwen and substantially on Llama, with no perplexity cost\footnote{Code and data are available at \url{https://anonymous.4open.science/r/turn_residual_gating-8703/}.}.
4	\end{abstract}
5	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "69d5e85b-8b09-44ea-b36b-30cddf67c0fc",
  "isSidechain": false,
  "promptId": "8817af8a-f189-44e8-a462-1453a12b4ea3",
  "type": "user",
  "uuid": "a5e4f155-f303-4163-9b8b-d9a9b5bb7199",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/abstract.tex",
      "content": "\\begin{abstract}\nAs multi-turn conversations grow longer, large language models progressively lose attention to the system-prompt goals that define their task, even when the underlying goal representations remain intact. Existing remedies operate at inference time, leaving a natural but untested alternative: training auxiliary attention losses alongside next-token prediction to directly optimize goal attention. This strategy assumes that attention patterns learned under teacher forcing will transfer to autoregressive generation, an assumption that classical exposure bias research has challenged for sequence models but that has never been examined for auxiliary attention objectives in multi-turn transformers.\nWe show this assumption fails. On a controlled five-way testbed spanning two architectures (Qwen-2.5-7B, Llama-3.1-8B), goal attention optimized to target under teacher forcing collapses by an order of magnitude under autoregressive generation. A causal exclusion chain traces the failure to exposure bias, ruling out gradient conflict, gating mechanism, and parameter capacity as primary causes. Inference-time attention steering confirms that the collapse reflects attention misallocation rather than representation loss. Scheduled sampling, applied here for the first time to auxiliary attention objectives in multi-turn transformers, compresses the training--inference gap to near parity on Qwen and substantially on Llama, with no perplexity cost\\footnote{Code and data are available at \\url{https://anonymous.4open.science/r/turn_residual_gating-8703/}.}.\n\\end{abstract}\n",
      "numLines": 5,
      "startLine": 1,
      "totalLines": 5
    }
  },
  "sourceToolAssistantUUID": "69d5e85b-8b09-44ea-b36b-30cddf67c0fc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "4b680861-4da7-411a-8744-3dabfdaf2205",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-25T20:38:05.244Z_

<details open><summary>🔧 Tool call — Read · `toolu_015sgzGmzyAtw1odJMFPbikA`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a5e4f155-f303-4163-9b8b-d9a9b5bb7199",
  "isSidechain": false,
  "requestId": "req_011CbPvwbVfNQCwbcnsYNfCu",
  "type": "assistant",
  "uuid": "9adc05bd-a6e6-405a-b7a0-af096a5df7f1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "4b680861-4da7-411a-8744-3dabfdaf2205",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014omTEWaQWBnZwZbaHNXrM6",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 466,
      "cache_read_input_tokens": 26401,
      "output_tokens": 785,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 466,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 785,
          "cache_read_input_tokens": 26401,
          "cache_creation_input_tokens": 466,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 466
          },
          "type": "message"
        }
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

_source line 19 · 2026-05-25T20:38:05.249Z_

<details><summary>↩ Tool result · `toolu_015sgzGmzyAtw1odJMFPbikA`</summary>

```text
1	\section{Introduction}\label{sec:introduction}
2	
3	Multi-turn dialogue is central to how large language models are deployed, from customer service to tutoring to long-form reasoning. Yet a persistent failure accompanies even the most fluent generation: as conversations grow longer, models pay progressively less attention to the system-prompt goals that define their task. \citet{dongre2026attention} measured significant Goal Accessibility Ratio (GAR) decline across 12 models over extended conversations; in our own evaluation, goal attention drops by over 70\% within just five turns. Crucially, this is not a representation problem: residual stream probes confirm that goal information persists (AUC\,=\,0.98). The model retains the knowledge of what it should attend to; it simply stops attending.
4	
5	Existing remedies address this decay at inference time. Split-softmax \citep{li2024measuring} separates instruction from conversation tokens; StreamingLLM \citep{xiao2024streaming} retains anchor tokens; Gated Attention \citep{qiu2025gated} applies per-head sigmoid gates within a single forward pass. A natural alternative is to intervene during training: optimize goal attention directly through auxiliary losses trained alongside next-token prediction (NTP). Yet this strategy rests on an untested assumption: attention patterns learned under teacher forcing (TF) transfer to autoregressive (AR) generation. Classical exposure bias research \citep{bengio2015scheduled,lamb2016professor} has shown that TF creates a training--inference distribution mismatch for RNN sequence models, but whether this mismatch extends to auxiliary attention objectives in multi-turn transformers remains unknown.
6	
7	We test this assumption and find it fails. We introduce a controlled five-way testbed (ThreadGate, +PCGrad, Uniform Gate, LoRA-only, and Base) designed not as competing solutions but as a causal exclusion chain (\S\ref{sec:comparison-design}), where each adjacent pair isolates one candidate failure mechanism. The result is unambiguous: every variant converges to target GAR under teacher forcing, yet goal attention collapses by an order of magnitude once the model generates its own context (Figure~\ref{fig:headline}). The exclusion chain traces this collapse to exposure bias, the training--inference distribution mismatch, ruling out gradient direction conflict (PCGrad removes conflict yet \emph{worsens} AR GAR), gating mechanism (Uniform Gate matches ThreadGate), and parameter capacity (LoRA-only shows the same pattern). Inference-time $\beta$-steering confirms that the collapse reflects attention misallocation rather than representation degradation; scheduled sampling bridges the gap by exposing the model to its own generations during training.
8	
9	\begin{figure*}[!ht]
10	  \centering
11	  \includegraphics[width=\textwidth]{fig1_headline.pdf}
12	  \caption{Exposure bias collapses auxiliary attention losses. \textbf{(a)}~Goal attention decays 85--90\% across turns under AR generation on both Qwen-2.5-7B and Llama-3.1-8B. \textbf{(b)}~Under TF evaluation all variants reach GAR$\approx$0.50, but AR generation collapses GAR by 8--17$\times$ (log scale). \textbf{(c)}~Scheduled sampling compresses the TF--AR gap from 7.8$\times$ to 1.3$\times$ (Qwen) and ${\sim}$27$\times$ to 2.9$\times$ (Llama).}
13	  \label{fig:headline}
14	\end{figure*}
15	
16	Our contributions are:
17	\begin{enumerate}\raggedright
18	    \item \textbf{Exposure bias characterization.} To our knowledge, the first empirical demonstration that exposure bias collapses auxiliary attention objectives in multi-turn transformers, with an order-of-magnitude TF--AR gap reproduced across two architectures (Qwen-2.5-7B, Llama-3.1-8B) and model scales (1.5B--8B).
19	    \item \textbf{Causal exclusion testbed.} A five-way diagnostic design, informed by seven loss-formulation iterations, that isolates the failure mechanism via causal exclusion, including a PCGrad \emph{modus tollens} argument ruling out gradient direction conflict ($p$\,=\,0.002, effect reverses).
20	    \item \textbf{Attention misallocation diagnosis.} Inference-time $\beta$-steering recovers goal attention with modest perplexity cost, evidence that the collapse is an attention routing failure, not a representational one.
21	    \item \textbf{Scheduled sampling as remedy.} The first application of scheduled sampling to auxiliary attention objectives in multi-turn transformers, compressing the TF--AR gap to ${\sim}$1.3$\times$ on Qwen and ${\sim}$2.9$\times$ on Llama with no perplexity degradation, robust across three seeds.
22	\end{enumerate}
23	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9adc05bd-a6e6-405a-b7a0-af096a5df7f1",
  "isSidechain": false,
  "promptId": "8817af8a-f189-44e8-a462-1453a12b4ea3",
  "type": "user",
  "uuid": "89e065f7-2a90-442b-a68d-1ee0af4a9ade",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/introduction.tex",
      "content": "\\section{Introduction}\\label{sec:introduction}\n\nMulti-turn dialogue is central to how large language models are deployed, from customer service to tutoring to long-form reasoning. Yet a persistent failure accompanies even the most fluent generation: as conversations grow longer, models pay progressively less attention to the system-prompt goals that define their task. \\citet{dongre2026attention} measured significant Goal Accessibility Ratio (GAR) decline across 12 models over extended conversations; in our own evaluation, goal attention drops by over 70\\% within just five turns. Crucially, this is not a representation problem: residual stream probes confirm that goal information persists (AUC\\,=\\,0.98). The model retains the knowledge of what it should attend to; it simply stops attending.\n\nExisting remedies address this decay at inference time. Split-softmax \\citep{li2024measuring} separates instruction from conversation tokens; StreamingLLM \\citep{xiao2024streaming} retains anchor tokens; Gated Attention \\citep{qiu2025gated} applies per-head sigmoid gates within a single forward pass. A natural alternative is to intervene during training: optimize goal attention directly through auxiliary losses trained alongside next-token prediction (NTP). Yet this strategy rests on an untested assumption: attention patterns learned under teacher forcing (TF) transfer to autoregressive (AR) generation. Classical exposure bias research \\citep{bengio2015scheduled,lamb2016professor} has shown that TF creates a training--inference distribution mismatch for RNN sequence models, but whether this mismatch extends to auxiliary attention objectives in multi-turn transformers remains unknown.\n\nWe test this assumption and find it fails. We introduce a controlled five-way testbed (ThreadGate, +PCGrad, Uniform Gate, LoRA-only, and Base) designed not as competing solutions but as a causal exclusion chain (\\S\\ref{sec:comparison-design}), where each adjacent pair isolates one candidate failure mechanism. The result is unambiguous: every variant converges to target GAR under teacher forcing, yet goal attention collapses by an order of magnitude once the model generates its own context (Figure~\\ref{fig:headline}). The exclusion chain traces this collapse to exposure bias, the training--inference distribution mismatch, ruling out gradient direction conflict (PCGrad removes conflict yet \\emph{worsens} AR GAR), gating mechanism (Uniform Gate matches ThreadGate), and parameter capacity (LoRA-only shows the same pattern). Inference-time $\\beta$-steering confirms that the collapse reflects attention misallocation rather than representation degradation; scheduled sampling bridges the gap by exposing the model to its own generations during training.\n\n\\begin{figure*}[!ht]\n  \\centering\n  \\includegraphics[width=\\textwidth]{fig1_headline.pdf}\n  \\caption{Exposure bias collapses auxiliary attention losses. \\textbf{(a)}~Goal attention decays 85--90\\% across turns under AR generation on both Qwen-2.5-7B and Llama-3.1-8B. \\textbf{(b)}~Under TF evaluation all variants reach GAR$\\approx$0.50, but AR generation collapses GAR by 8--17$\\times$ (log scale). \\textbf{(c)}~Scheduled sampling compresses the TF--AR gap from 7.8$\\times$ to 1.3$\\times$ (Qwen) and ${\\sim}$27$\\times$ to 2.9$\\times$ (Llama).}\n  \\label{fig:headline}\n\\end{figure*}\n\nOur contributions are:\n\\begin{enumerate}\\raggedright\n    \\item \\textbf{Exposure bias characterization.} To our knowledge, the first empirical demonstration that exposure bias collapses auxiliary attention objectives in multi-turn transformers, with an order-of-magnitude TF--AR gap reproduced across two architectures (Qwen-2.5-7B, Llama-3.1-8B) and model scales (1.5B--8B).\n    \\item \\textbf{Causal exclusion testbed.} A five-way diagnostic design, informed by seven loss-formulation iterations, that isolates the failure mechanism via causal exclusion, including a PCGrad \\emph{modus tollens} argument ruling out gradient direction conflict ($p$\\,=\\,0.002, effect reverses).\n    \\item \\textbf{Attention misallocation diagnosis.} Inference-time $\\beta$-steering recovers goal attention with modest perplexity cost, evidence that the collapse is an attention routing failure, not a representational one.\n    \\item \\textbf{Scheduled sampling as remedy.} The first application of scheduled sampling to auxiliary attention objectives in multi-turn transformers, compressing the TF--AR gap to ${\\sim}$1.3$\\times$ on Qwen and ${\\sim}$2.9$\\times$ on Llama with no perplexity degradation, robust across three seeds.\n\\end{enumerate}\n",
      "numLines": 23,
      "startLine": 1,
      "totalLines": 23
    }
  },
  "sourceToolAssistantUUID": "9adc05bd-a6e6-405a-b7a0-af096a5df7f1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "4b680861-4da7-411a-8744-3dabfdaf2205",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-25T20:38:05.797Z_

<details open><summary>🔧 Tool call — Read · `toolu_01L61BULGx63LSwjd7TFtZ2t`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "89e065f7-2a90-442b-a68d-1ee0af4a9ade",
  "isSidechain": false,
  "requestId": "req_011CbPvwbVfNQCwbcnsYNfCu",
  "type": "assistant",
  "uuid": "f8da22c7-d760-4563-af8a-18367fcb9cc8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "4b680861-4da7-411a-8744-3dabfdaf2205",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014omTEWaQWBnZwZbaHNXrM6",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 466,
      "cache_read_input_tokens": 26401,
      "output_tokens": 785,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 466,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 785,
          "cache_read_input_tokens": 26401,
          "cache_creation_input_tokens": 466,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 466
          },
          "type": "message"
        }
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

_source line 21 · 2026-05-25T20:38:05.802Z_

<details><summary>↩ Tool result · `toolu_01L61BULGx63LSwjd7TFtZ2t`</summary>

```text
1	\section{Method}\label{sec:method}
2	
3	\subsection{Preliminaries}\label{sec:background}
4	
5	\paragraph{Goal Accessibility Ratio.}
6	Standard metrics such as perplexity and attention entropy capture generation quality but not \emph{what} the model attends to. In multi-turn dialogue, a model may generate fluent text while progressively ignoring task specifications in the system prompt. We need a metric that directly measures whether goal-relevant context receives attention. To formalize this, we denote the task specification tokens in the system prompt as \emph{goal tokens} $\mathcal{G}$. \citet{dongre2026attention} defined the Goal Accessibility Ratio (GAR) for a model with $L$ layers and $H$ heads at turn $\tau$ as
7	\begin{equation}\label{eq:gar}
8	  \text{GAR}(\tau) = \frac{1}{L \cdot H \cdot |\mathcal{R}_\tau|} \sum_{\ell=1}^{L} \sum_{h=1}^{H} \sum_{i \in \mathcal{R}_\tau} \sum_{j \in \mathcal{G}} A_{i,j}^{(\ell,h)},
9	\end{equation}
10	where $\mathcal{R}_\tau$ is the set of response tokens at turn $\tau$ and $A_{i,j}^{(\ell,h)}$ is the attention weight from token $i$ to token $j$ at layer $\ell$, head $h$.
11	
12	\paragraph{Two GAR variants.}
13	\textbf{GAR-Dongre} is the original definition (Eq.~\ref{eq:gar}), averaging over all response tokens. However, averaging dilutes the signal with intermediate positions that may legitimately attend to local context rather than the system prompt. The last token of each assistant turn is where the model aggregates information for the next continuation; attention at this position most directly reflects the model's awareness of task specifications. \textbf{GAR-ours} restricts the measurement accordingly:
14	\begin{equation}\label{eq:gar-ours}
15	  \text{GAR\text{-}ours}(\tau) = \frac{1}{L \cdot H} \sum_{\ell=1}^{L} \sum_{h=1}^{H} \sum_{j \in \mathcal{G}} A_{t_\tau,\, j}^{(\ell,h)},
16	\end{equation}
17	where $t_\tau$ is the last token index at turn $\tau$. Attention at this position reflects the information drawn upon for continuation; we use GAR-ours as the optimization target for $\mathcal{L}_\text{GAR}$ (\S\ref{sec:loss}). Empirically, GAR-Dongre is diluted by NTP attention patterns to ${\sim}$0.01--0.02 in multi-turn settings, losing discriminative power across configurations; GAR-ours retains an order-of-magnitude range (0.019--0.50). The contrast itself is informative: goal attention concentrates at the last-token position, and only this concentrated pattern is vulnerable to distribution shift (\S\ref{sec:analysis}). Throughout this work, GAR serves primarily as a \emph{diagnostic probe}: it measures whether auxiliary attention training transfers to autoregressive generation, rather than being an end-to-end optimization objective whose increase directly improves downstream task performance (the correlation with instruction retention is weak; $r$\,=\,0.200, $p$\,=\,0.007; \S\ref{sec:discussion}).
18	
19	\subsection{ThreadGate Architecture}
20	
21	\begin{figure}[t]
22	  \centering
23	  \includegraphics[width=\columnwidth]{fig4_attention_heatmap.pdf}
24	  \caption{Per-turn GAR-ours under AR generation ($N$\,=\,5 conversations, 10 turns). All fine-tuned variants cluster together (77--81\% decay; $\Delta$\,=\,3.3\,pp between ThreadGate and LoRA-only); Base decays 87.5\%. Gating adds zero incremental effect.}
25	  \label{fig:attention-heatmap}
26	\end{figure}
27	
28	Different transformer layers serve different roles: early layers capture local syntax while later layers integrate long-range context \citep{gromov2024unreasonable}. A global intervention would uniformly scale all layers, but goal attention decay is layer-dependent: some layers contribute more to cross-turn information routing than others. ThreadGate therefore adds a \emph{per-layer} gating mechanism to the residual stream, allowing the model to learn which layers to modulate. At each layer $l$, the residual update is scaled by a scalar gate:
29	\begin{equation}
30	  x_{l+1} = x_l + g_l \cdot f_l(x_l),
31	\end{equation}
32	where $f_l$ denotes the sublayer computation (self-attention or feed-forward network, FFN). Since residual networks can be viewed as ensembles of shallow paths \citep{veit2016residual}, per-layer gating selectively modulates individual paths within this ensemble. This resembles ReZero \citep{bachlechner2021rezero}, which initializes a single trainable scalar at zero to stabilize deep network training, but ThreadGate differs in three ways: (i)~gates are \emph{content-conditioned}, a function of the hidden state rather than a fixed scalar; (ii)~gates are \emph{turn-conditioned}, incorporating conversation-position features; (iii)~gates are initialized near identity ($\sigma(1.5) \approx 0.82$) rather than zero, preserving the pretrained model's computation.
33	
34	Concretely, each gate $g_l$ is produced by a two-layer MLP that takes both content and turn features as input:
35	\begin{align}\label{eq:gate}
36	  g_l = \sigma\bigl(W_2\,\text{ReLU}(&W_1\,[\text{proj}(x_l);\;\text{emb}(t_d, t_i)] \notag\\
37	  &+ b_1) + b_2\bigr),
38	\end{align}
39	where $\text{proj}(\cdot)$ reduces the hidden dimension to 16, and $\text{emb}(t_d, t_i)$ provides a 16-dimensional turn embedding encoding turn distance $t_d$ (turns since system prompt) and turn index $t_i$ via learned lookup tables. The 32-dimensional input passes through a 64-unit hidden layer to a scalar gate in $(0, 1)$ via sigmoid. For Qwen-2.5-7B ($L\!=\!28$), this adds ${\sim}$57K parameters ($<$0.001\% of 7B). To isolate the contribution of turn conditioning, the \textbf{Uniform Gate} ablation replaces $\text{emb}(\cdot)$ with a learnable constant, removing turn awareness while retaining content-conditioned gating. To preserve pretrained behavior, gate biases are initialized to 1.5 (${\sim}$82\% pass-through) rather than zero as in ReZero, and gate parameters receive a $10\times$ learning rate multiplier to accelerate adaptation.
40	
41	\subsection{Training Objective}\label{sec:loss}
42	
43	Next-token prediction alone provides no gradient signal for attention allocation; a model can achieve low perplexity while distributing attention arbitrarily. The auxiliary GAR loss provides explicit pressure to maintain goal-token attention, while a diversity regularizer prevents gate collapse. The training objective combines three terms:
44	\begin{equation}
45	  \mathcal{L} = \mathcal{L}_\text{NTP} + \lambda_\text{GAR}\,\mathcal{L}_\text{GAR} + \lambda_\text{div}\,\mathcal{L}_\text{div}.
46	\end{equation}
47	$\mathcal{L}_\text{NTP}$ is the standard next-token prediction loss. For $\mathcal{L}_\text{GAR}$, we use MSE rather than cross-entropy because GAR is a continuous ratio and MSE provides \emph{bidirectional} pressure, penalizing both under- and over-attention and preventing identity collapse (Appendix~\ref{sec:appendix-loss}):
48	\begin{equation}
49	  \mathcal{L}_\text{GAR} = \text{MSE}(\text{GAR\text{-}ours}, \tau),
50	\end{equation}
51	where $\tau = 0.5$ targets allocating half of the last token's attention to goal tokens. Without diversity pressure, all gates converge near 1.0; the gate diversity loss prevents this:
52	\begin{equation}
53	  \mathcal{L}_\text{div} = \text{ReLU}(\sigma_\text{min} - \text{std}(\mathbf{g})),
54	\end{equation}
55	where $\mathbf{g} = [g_1, \ldots, g_L]$ and $\sigma_\text{min} = 0.05$ is a minimum standard deviation threshold ($\lambda_\text{GAR} = \lambda_\text{div} = 1.0$). This formulation emerged from seven iterations spanning four loss families (Appendix~\ref{sec:appendix-loss}): cumulative (v1--v2) and maximize (v3--v6) objectives either starve gate gradients at equilibrium or drive gates toward identity; only MSE provides the bidirectional pressure needed to prevent identity collapse.
56	
57	\subsection{Controlled Comparison Design}\label{sec:comparison-design}
58	
59	We design a five-way comparison where each adjacent pair isolates one factor: \textbf{ThreadGate (TG) vs.\ Uniform Gate (UG)} (turn conditioning), \textbf{TG vs.\ LoRA-only} (gating mechanism), \textbf{ThreadGate vs.\ +PCGrad} (gradient conflict via gradient surgery \citep{yu2020pcgrad}), and \textbf{Fine-tuned vs.\ Base} (LoRA adaptation). All fine-tuned variants share training data, LoRA configuration, optimizer, and seed (Appendix~\ref{sec:appendix-hyper}).
60	
61	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f8da22c7-d760-4563-af8a-18367fcb9cc8",
  "isSidechain": false,
  "promptId": "8817af8a-f189-44e8-a462-1453a12b4ea3",
  "type": "user",
  "uuid": "a97d48fd-c5f7-4dd1-8b95-7f06da3addf9",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/method.tex",
      "content": "\\section{Method}\\label{sec:method}\n\n\\subsection{Preliminaries}\\label{sec:background}\n\n\\paragraph{Goal Accessibility Ratio.}\nStandard metrics such as perplexity and attention entropy capture generation quality but not \\emph{what} the model attends to. In multi-turn dialogue, a model may generate fluent text while progressively ignoring task specifications in the system prompt. We need a metric that directly measures whether goal-relevant context receives attention. To formalize this, we denote the task specification tokens in the system prompt as \\emph{goal tokens} $\\mathcal{G}$. \\citet{dongre2026attention} defined the Goal Accessibility Ratio (GAR) for a model with $L$ layers and $H$ heads at turn $\\tau$ as\n\\begin{equation}\\label{eq:gar}\n  \\text{GAR}(\\tau) = \\frac{1}{L \\cdot H \\cdot |\\mathcal{R}_\\tau|} \\sum_{\\ell=1}^{L} \\sum_{h=1}^{H} \\sum_{i \\in \\mathcal{R}_\\tau} \\sum_{j \\in \\mathcal{G}} A_{i,j}^{(\\ell,h)},\n\\end{equation}\nwhere $\\mathcal{R}_\\tau$ is the set of response tokens at turn $\\tau$ and $A_{i,j}^{(\\ell,h)}$ is the attention weight from token $i$ to token $j$ at layer $\\ell$, head $h$.\n\n\\paragraph{Two GAR variants.}\n\\textbf{GAR-Dongre} is the original definition (Eq.~\\ref{eq:gar}), averaging over all response tokens. However, averaging dilutes the signal with intermediate positions that may legitimately attend to local context rather than the system prompt. The last token of each assistant turn is where the model aggregates information for the next continuation; attention at this position most directly reflects the model's awareness of task specifications. \\textbf{GAR-ours} restricts the measurement accordingly:\n\\begin{equation}\\label{eq:gar-ours}\n  \\text{GAR\\text{-}ours}(\\tau) = \\frac{1}{L \\cdot H} \\sum_{\\ell=1}^{L} \\sum_{h=1}^{H} \\sum_{j \\in \\mathcal{G}} A_{t_\\tau,\\, j}^{(\\ell,h)},\n\\end{equation}\nwhere $t_\\tau$ is the last token index at turn $\\tau$. Attention at this position reflects the information drawn upon for continuation; we use GAR-ours as the optimization target for $\\mathcal{L}_\\text{GAR}$ (\\S\\ref{sec:loss}). Empirically, GAR-Dongre is diluted by NTP attention patterns to ${\\sim}$0.01--0.02 in multi-turn settings, losing discriminative power across configurations; GAR-ours retains an order-of-magnitude range (0.019--0.50). The contrast itself is informative: goal attention concentrates at the last-token position, and only this concentrated pattern is vulnerable to distribution shift (\\S\\ref{sec:analysis}). Throughout this work, GAR serves primarily as a \\emph{diagnostic probe}: it measures whether auxiliary attention training transfers to autoregressive generation, rather than being an end-to-end optimization objective whose increase directly improves downstream task performance (the correlation with instruction retention is weak; $r$\\,=\\,0.200, $p$\\,=\\,0.007; \\S\\ref{sec:discussion}).\n\n\\subsection{ThreadGate Architecture}\n\n\\begin{figure}[t]\n  \\centering\n  \\includegraphics[width=\\columnwidth]{fig4_attention_heatmap.pdf}\n  \\caption{Per-turn GAR-ours under AR generation ($N$\\,=\\,5 conversations, 10 turns). All fine-tuned variants cluster together (77--81\\% decay; $\\Delta$\\,=\\,3.3\\,pp between ThreadGate and LoRA-only); Base decays 87.5\\%. Gating adds zero incremental effect.}\n  \\label{fig:attention-heatmap}\n\\end{figure}\n\nDifferent transformer layers serve different roles: early layers capture local syntax while later layers integrate long-range context \\citep{gromov2024unreasonable}. A global intervention would uniformly scale all layers, but goal attention decay is layer-dependent: some layers contribute more to cross-turn information routing than others. ThreadGate therefore adds a \\emph{per-layer} gating mechanism to the residual stream, allowing the model to learn which layers to modulate. At each layer $l$, the residual update is scaled by a scalar gate:\n\\begin{equation}\n  x_{l+1} = x_l + g_l \\cdot f_l(x_l),\n\\end{equation}\nwhere $f_l$ denotes the sublayer computation (self-attention or feed-forward network, FFN). Since residual networks can be viewed as ensembles of shallow paths \\citep{veit2016residual}, per-layer gating selectively modulates individual paths within this ensemble. This resembles ReZero \\citep{bachlechner2021rezero}, which initializes a single trainable scalar at zero to stabilize deep network training, but ThreadGate differs in three ways: (i)~gates are \\emph{content-conditioned}, a function of the hidden state rather than a fixed scalar; (ii)~gates are \\emph{turn-conditioned}, incorporating conversation-position features; (iii)~gates are initialized near identity ($\\sigma(1.5) \\approx 0.82$) rather than zero, preserving the pretrained model's computation.\n\nConcretely, each gate $g_l$ is produced by a two-layer MLP that takes both content and turn features as input:\n\\begin{align}\\label{eq:gate}\n  g_l = \\sigma\\bigl(W_2\\,\\text{ReLU}(&W_1\\,[\\text{proj}(x_l);\\;\\text{emb}(t_d, t_i)] \\notag\\\\\n  &+ b_1) + b_2\\bigr),\n\\end{align}\nwhere $\\text{proj}(\\cdot)$ reduces the hidden dimension to 16, and $\\text{emb}(t_d, t_i)$ provides a 16-dimensional turn embedding encoding turn distance $t_d$ (turns since system prompt) and turn index $t_i$ via learned lookup tables. The 32-dimensional input passes through a 64-unit hidden layer to a scalar gate in $(0, 1)$ via sigmoid. For Qwen-2.5-7B ($L\\!=\\!28$), this adds ${\\sim}$57K parameters ($<$0.001\\% of 7B). To isolate the contribution of turn conditioning, the \\textbf{Uniform Gate} ablation replaces $\\text{emb}(\\cdot)$ with a learnable constant, removing turn awareness while retaining content-conditioned gating. To preserve pretrained behavior, gate biases are initialized to 1.5 (${\\sim}$82\\% pass-through) rather than zero as in ReZero, and gate parameters receive a $10\\times$ learning rate multiplier to accelerate adaptation.\n\n\\subsection{Training Objective}\\label{sec:loss}\n\nNext-token prediction alone provides no gradient signal for attention allocation; a model can achieve low perplexity while distributing attention arbitrarily. The auxiliary GAR loss provides explicit pressure to maintain goal-token attention, while a diversity regularizer prevents gate collapse. The training objective combines three terms:\n\\begin{equation}\n  \\mathcal{L} = \\mathcal{L}_\\text{NTP} + \\lambda_\\text{GAR}\\,\\mathcal{L}_\\text{GAR} + \\lambda_\\text{div}\\,\\mathcal{L}_\\text{div}.\n\\end{equation}\n$\\mathcal{L}_\\text{NTP}$ is the standard next-token prediction loss. For $\\mathcal{L}_\\text{GAR}$, we use MSE rather than cross-entropy because GAR is a continuous ratio and MSE provides \\emph{bidirectional} pressure, penalizing both under- and over-attention and preventing identity collapse (Appendix~\\ref{sec:appendix-loss}):\n\\begin{equation}\n  \\mathcal{L}_\\text{GAR} = \\text{MSE}(\\text{GAR\\text{-}ours}, \\tau),\n\\end{equation}\nwhere $\\tau = 0.5$ targets allocating half of the last token's attention to goal tokens. Without diversity pressure, all gates converge near 1.0; the gate diversity loss prevents this:\n\\begin{equation}\n  \\mathcal{L}_\\text{div} = \\text{ReLU}(\\sigma_\\text{min} - \\text{std}(\\mathbf{g})),\n\\end{equation}\nwhere $\\mathbf{g} = [g_1, \\ldots, g_L]$ and $\\sigma_\\text{min} = 0.05$ is a minimum standard deviation threshold ($\\lambda_\\text{GAR} = \\lambda_\\text{div} = 1.0$). This formulation emerged from seven iterations spanning four loss families (Appendix~\\ref{sec:appendix-loss}): cumulative (v1--v2) and maximize (v3--v6) objectives either starve gate gradients at equilibrium or drive gates toward identity; only MSE provides the bidirectional pressure needed to prevent identity collapse.\n\n\\subsection{Controlled Comparison Design}\\label{sec:comparison-design}\n\nWe design a five-way comparison where each adjacent pair isolates one factor: \\textbf{ThreadGate (TG) vs.\\ Uniform Gate (UG)} (turn conditioning), \\textbf{TG vs.\\ LoRA-only} (gating mechanism), \\textbf{ThreadGate vs.\\ +PCGrad} (gradient conflict via gradient surgery \\citep{yu2020pcgrad}), and \\textbf{Fine-tuned vs.\\ Base} (LoRA adaptation). All fine-tuned variants share training data, LoRA configuration, optimizer, and seed (Appendix~\\ref{sec:appendix-hyper}).\n\n",
      "numLines": 61,
      "startLine": 1,
      "totalLines": 61
    }
  },
  "sourceToolAssistantUUID": "f8da22c7-d760-4563-af8a-18367fcb9cc8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "4b680861-4da7-411a-8744-3dabfdaf2205",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-25T20:38:06.212Z_

<details open><summary>🔧 Tool call — Read · `toolu_01E2wvzDwdscB23R2ssiSLuY`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a97d48fd-c5f7-4dd1-8b95-7f06da3addf9",
  "isSidechain": false,
  "requestId": "req_011CbPvwbVfNQCwbcnsYNfCu",
  "type": "assistant",
  "uuid": "4e6a32a8-a8b6-4cf4-8c05-ba9bd9fc56c0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "4b680861-4da7-411a-8744-3dabfdaf2205",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014omTEWaQWBnZwZbaHNXrM6",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 466,
      "cache_read_input_tokens": 26401,
      "output_tokens": 785,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 466,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 785,
          "cache_read_input_tokens": 26401,
          "cache_creation_input_tokens": 466,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 466
          },
          "type": "message"
        }
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

_source line 23 · 2026-05-25T20:38:06.219Z_

<details><summary>↩ Tool result · `toolu_01E2wvzDwdscB23R2ssiSLuY`</summary>

```text
1	\section{Experiments}
2	\label{sec:experiments}
3	
4	\subsection{Setup}
5	
6	We fine-tune Qwen-2.5-7B-Instruct with LoRA \citep{hu2022lora,dettmers2023qlora} on 8K multi-turn conversations from the UltraChat \citep{ding2023ultrachat} training split. Training uses 3 epochs with AdamW (lr $= 2 \times 10^{-4}$, batch size 1, gradient accumulation 8, seed 42; ThreadGate additionally with seed 123); each variant requires approximately 6 hours on a single NVIDIA RTX PRO 6000 Blackwell Server Edition GPU (96\,GB; training costs in Appendix~\ref{sec:appendix-cost}). Full hyperparameters are in Appendix~\ref{sec:appendix-hyper}; dataset statistics in Appendices~\ref{sec:appendix-data} and~\ref{sec:appendix-dataset-ext}; the controlled comparison design is described in \S\ref{sec:comparison-design}. We evaluate under \emph{IID} (same-distribution UltraChat text) and \emph{held-out} (50 non-overlapping conversations) teacher-forced protocols, reporting GAR-ours, GAR-Dongre \citep{dongre2026attention}, and perplexity (PPL).
7	
8	\subsection{Main Results}
9	
10	Table~\ref{tab:five-way} presents the five-way comparison. Under TF evaluation, all fine-tuned variants converge: GAR-ours spans 0.49--0.51 ($\leq$2\,pp), PPL is 2.78 for all. IID and held-out protocols produce identical rankings (held-out GAR-ours differs by $\leq$1\,pp), ruling out data overlap as a confound. GAR-Dongre remains low (0.01--0.02) with no TF-AR gap, indicating that only concentrated last-token attention is vulnerable to distribution shift; scheduled sampling breaks this pattern (\S\ref{subsec:ss}).
11	
12	Under AR generation ($N$\,=\,50), GAR-ours drops to 0.019--0.064, an 8--17$\times$ gap (Figure~\ref{fig:headline}). The ordering (ThreadGate 0.064 $>$ LoRA-only 0.037 $>$ Uniform Gate 0.033 $>$ PCGrad 0.030 $>$ Base 0.019) shows ThreadGate vs.\ LoRA-only is significant ($p$\,=\,0.004; Appendices~\ref{sec:appendix-stats} and~\ref{sec:appendix-stats-ext}), yet the gap remains 7.8$\times$. A second seed confirms TF stability ($0.504\pm0.001$). MMLU 5-shot accuracy remains within 0.8\,pp across all variants (per-category breakdown in Appendix~\ref{sec:appendix-mmlu-ext}). We analyze this distribution shift in \S\ref{sec:analysis}.
13	
14	\begin{figure*}[!t]
15	  \centering
16	  \includegraphics[width=\textwidth]{fig5_attention_steering.pdf}
17	  \caption{Inference-time $\beta$-steering recovers GAR from 0.064 to 0.727, consistent with attention misallocation as a proximal cause (9\% PPL cost at $\beta$\,=\,3; phase transition at $\beta \in [2, 3]$).}
18	  \label{fig:steering-recovery}
19	\end{figure*}
20	
21	\subsection{Inference-Time Attention Steering}\label{subsec:steering}
22	
23	All training-time interventions leave the exposure bias gap intact. If the collapse is caused by attention misallocation rather than representation degradation, then directly correcting attention should recover GAR. We test this by adding a constant bias $\beta$ to pre-softmax attention logits for goal-token positions during generation:
24	\begin{equation}
25	  \tilde{A}_{i,j}^{(\ell,h)} = A_{i,j}^{(\ell,h)} + \beta \cdot \mathbf{1}[j \in \mathcal{G}],
26	\end{equation}
27	where $\tilde{A}$ denotes the modified logits before softmax. The additive form operates in log-probability space, providing uniform boost even when baseline attention is near zero. The response is sharply nonlinear: $\beta \in [0, 2]$ yields marginal improvement, then $\beta = 3$ triggers a phase transition to GAR\,=\,0.556 (9\% PPL cost). At $\beta$\,=\,5, GAR reaches 0.727$\pm$0.061 (PPL 1.77); the operating region $\beta \in [3, 5]$ exceeds the TF baseline while PPL remains below 1.8 (Figure~\ref{fig:steering-recovery}; full results in Appendix~\ref{sec:appendix-steering}; per-$\beta$ turn-level trajectories in Appendix~\ref{sec:appendix-steering-viz}). GAR recovery under steering is partly by construction: boosting attention logits toward goal tokens mechanically increases the attention-based metric. The stronger evidence is the counterfactual: if the collapse were due to hidden-state drift rather than attention misallocation, reweighting could not recover GAR, yet it does, consistent with attention misallocation as a proximal cause (qualitative examples in Appendix~\ref{sec:appendix-examples}). Downstream, steering ($\beta$\,=\,3) raises late-turn instruction compliance by +11.1\,pp, though this effect does not reach conventional significance ($p$\,=\,0.077; content-constrained tasks benefit most, +23.8\,pp; Appendix~\ref{sec:appendix-ir}).
28	
29	\subsection{Scheduled Sampling Compresses the TF--AR Gap}\label{subsec:ss}
30	
31	\begin{figure}[t]
32	  \centering
33	  \includegraphics[width=\columnwidth]{fig_ss_gap_compression.pdf}
34	  \caption{Scheduled sampling compresses the TF-AR gap from 7.8$\times$ to ${\sim}$1.3$\times$, the only variant approaching parity across five training conditions.}
35	  \label{fig:ss-gap}
36	\end{figure}
37	
38	Scheduled sampling (SS; \citealp{bengio2015scheduled}), which mixes model-generated tokens into training prefixes with linearly increasing probability (Appendix~\ref{sec:appendix-ss}), directly targets the training-inference mismatch. Across three seeds, AR GAR-ours rises to $0.401\pm0.047$, compressing the gap from 7.8$\times$ to ${\sim}$1.3$\times$ (TF GAR $0.498\pm0.004$) with no PPL cost ($1.441\pm0.001$; Figure~\ref{fig:ss-gap}; per-seed details in Appendix~\ref{sec:appendix-perseed}). Steering on SS models nearly eliminates seed variance ($\beta$\,=\,5: $0.717\pm0.001$, std 0.047$\to$0.001; Figure~\ref{fig:ss-multiseed}). SS generalizes across GAR definitions (mid-turn GAR above 0.36 for all token-position variants; Appendix~\ref{sec:appendix-gar-robust}; extended robustness in Appendix~\ref{sec:appendix-gar-ext}) and across architectures: on Llama-3.1-8B, SS compresses the gap from ${\sim}$27$\times$ to 2.9$\times$, weaker than Qwen likely due to fewer training epochs (2 vs.\ 3; \S\ref{subsec:cross-model}). The benefit diminishes in longer dialogues (Appendix~\ref{sec:appendix-n5}), consistent with exposure bias compounding over turns.
39	
40	
41	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4e6a32a8-a8b6-4cf4-8c05-ba9bd9fc56c0",
  "isSidechain": false,
  "promptId": "8817af8a-f189-44e8-a462-1453a12b4ea3",
  "type": "user",
  "uuid": "c33f7508-58f8-4599-8cd9-623b9a3ef26f",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/experiments.tex",
      "content": "\\section{Experiments}\n\\label{sec:experiments}\n\n\\subsection{Setup}\n\nWe fine-tune Qwen-2.5-7B-Instruct with LoRA \\citep{hu2022lora,dettmers2023qlora} on 8K multi-turn conversations from the UltraChat \\citep{ding2023ultrachat} training split. Training uses 3 epochs with AdamW (lr $= 2 \\times 10^{-4}$, batch size 1, gradient accumulation 8, seed 42; ThreadGate additionally with seed 123); each variant requires approximately 6 hours on a single NVIDIA RTX PRO 6000 Blackwell Server Edition GPU (96\\,GB; training costs in Appendix~\\ref{sec:appendix-cost}). Full hyperparameters are in Appendix~\\ref{sec:appendix-hyper}; dataset statistics in Appendices~\\ref{sec:appendix-data} and~\\ref{sec:appendix-dataset-ext}; the controlled comparison design is described in \\S\\ref{sec:comparison-design}. We evaluate under \\emph{IID} (same-distribution UltraChat text) and \\emph{held-out} (50 non-overlapping conversations) teacher-forced protocols, reporting GAR-ours, GAR-Dongre \\citep{dongre2026attention}, and perplexity (PPL).\n\n\\subsection{Main Results}\n\nTable~\\ref{tab:five-way} presents the five-way comparison. Under TF evaluation, all fine-tuned variants converge: GAR-ours spans 0.49--0.51 ($\\leq$2\\,pp), PPL is 2.78 for all. IID and held-out protocols produce identical rankings (held-out GAR-ours differs by $\\leq$1\\,pp), ruling out data overlap as a confound. GAR-Dongre remains low (0.01--0.02) with no TF-AR gap, indicating that only concentrated last-token attention is vulnerable to distribution shift; scheduled sampling breaks this pattern (\\S\\ref{subsec:ss}).\n\nUnder AR generation ($N$\\,=\\,50), GAR-ours drops to 0.019--0.064, an 8--17$\\times$ gap (Figure~\\ref{fig:headline}). The ordering (ThreadGate 0.064 $>$ LoRA-only 0.037 $>$ Uniform Gate 0.033 $>$ PCGrad 0.030 $>$ Base 0.019) shows ThreadGate vs.\\ LoRA-only is significant ($p$\\,=\\,0.004; Appendices~\\ref{sec:appendix-stats} and~\\ref{sec:appendix-stats-ext}), yet the gap remains 7.8$\\times$. A second seed confirms TF stability ($0.504\\pm0.001$). MMLU 5-shot accuracy remains within 0.8\\,pp across all variants (per-category breakdown in Appendix~\\ref{sec:appendix-mmlu-ext}). We analyze this distribution shift in \\S\\ref{sec:analysis}.\n\n\\begin{figure*}[!t]\n  \\centering\n  \\includegraphics[width=\\textwidth]{fig5_attention_steering.pdf}\n  \\caption{Inference-time $\\beta$-steering recovers GAR from 0.064 to 0.727, consistent with attention misallocation as a proximal cause (9\\% PPL cost at $\\beta$\\,=\\,3; phase transition at $\\beta \\in [2, 3]$).}\n  \\label{fig:steering-recovery}\n\\end{figure*}\n\n\\subsection{Inference-Time Attention Steering}\\label{subsec:steering}\n\nAll training-time interventions leave the exposure bias gap intact. If the collapse is caused by attention misallocation rather than representation degradation, then directly correcting attention should recover GAR. We test this by adding a constant bias $\\beta$ to pre-softmax attention logits for goal-token positions during generation:\n\\begin{equation}\n  \\tilde{A}_{i,j}^{(\\ell,h)} = A_{i,j}^{(\\ell,h)} + \\beta \\cdot \\mathbf{1}[j \\in \\mathcal{G}],\n\\end{equation}\nwhere $\\tilde{A}$ denotes the modified logits before softmax. The additive form operates in log-probability space, providing uniform boost even when baseline attention is near zero. The response is sharply nonlinear: $\\beta \\in [0, 2]$ yields marginal improvement, then $\\beta = 3$ triggers a phase transition to GAR\\,=\\,0.556 (9\\% PPL cost). At $\\beta$\\,=\\,5, GAR reaches 0.727$\\pm$0.061 (PPL 1.77); the operating region $\\beta \\in [3, 5]$ exceeds the TF baseline while PPL remains below 1.8 (Figure~\\ref{fig:steering-recovery}; full results in Appendix~\\ref{sec:appendix-steering}; per-$\\beta$ turn-level trajectories in Appendix~\\ref{sec:appendix-steering-viz}). GAR recovery under steering is partly by construction: boosting attention logits toward goal tokens mechanically increases the attention-based metric. The stronger evidence is the counterfactual: if the collapse were due to hidden-state drift rather than attention misallocation, reweighting could not recover GAR, yet it does, consistent with attention misallocation as a proximal cause (qualitative examples in Appendix~\\ref{sec:appendix-examples}). Downstream, steering ($\\beta$\\,=\\,3) raises late-turn instruction compliance by +11.1\\,pp, though this effect does not reach conventional significance ($p$\\,=\\,0.077; content-constrained tasks benefit most, +23.8\\,pp; Appendix~\\ref{sec:appendix-ir}).\n\n\\subsection{Scheduled Sampling Compresses the TF--AR Gap}\\label{subsec:ss}\n\n\\begin{figure}[t]\n  \\centering\n  \\includegraphics[width=\\columnwidth]{fig_ss_gap_compression.pdf}\n  \\caption{Scheduled sampling compresses the TF-AR gap from 7.8$\\times$ to ${\\sim}$1.3$\\times$, the only variant approaching parity across five training conditions.}\n  \\label{fig:ss-gap}\n\\end{figure}\n\nScheduled sampling (SS; \\citealp{bengio2015scheduled}), which mixes model-generated tokens into training prefixes with linearly increasing probability (Appendix~\\ref{sec:appendix-ss}), directly targets the training-inference mismatch. Across three seeds, AR GAR-ours rises to $0.401\\pm0.047$, compressing the gap from 7.8$\\times$ to ${\\sim}$1.3$\\times$ (TF GAR $0.498\\pm0.004$) with no PPL cost ($1.441\\pm0.001$; Figure~\\ref{fig:ss-gap}; per-seed details in Appendix~\\ref{sec:appendix-perseed}). Steering on SS models nearly eliminates seed variance ($\\beta$\\,=\\,5: $0.717\\pm0.001$, std 0.047$\\to$0.001; Figure~\\ref{fig:ss-multiseed}). SS generalizes across GAR definitions (mid-turn GAR above 0.36 for all token-position variants; Appendix~\\ref{sec:appendix-gar-robust}; extended robustness in Appendix~\\ref{sec:appendix-gar-ext}) and across architectures: on Llama-3.1-8B, SS compresses the gap from ${\\sim}$27$\\times$ to 2.9$\\times$, weaker than Qwen likely due to fewer training epochs (2 vs.\\ 3; \\S\\ref{subsec:cross-model}). The benefit diminishes in longer dialogues (Appendix~\\ref{sec:appendix-n5}), consistent with exposure bias compounding over turns.\n\n\n",
      "numLines": 41,
      "startLine": 1,
      "totalLines": 41
    }
  },
  "sourceToolAssistantUUID": "4e6a32a8-a8b6-4cf4-8c05-ba9bd9fc56c0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "4b680861-4da7-411a-8744-3dabfdaf2205",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-25T20:38:06.872Z_

<details open><summary>🔧 Tool call — Read · `toolu_01ToFkXWpEgYZ1LzsXR5D2JL`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/analysis.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c33f7508-58f8-4599-8cd9-623b9a3ef26f",
  "isSidechain": false,
  "requestId": "req_011CbPvwbVfNQCwbcnsYNfCu",
  "type": "assistant",
  "uuid": "8a88d661-bdad-4394-b9eb-c465ef3bd919",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "4b680861-4da7-411a-8744-3dabfdaf2205",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014omTEWaQWBnZwZbaHNXrM6",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 466,
      "cache_read_input_tokens": 26401,
      "output_tokens": 785,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 466,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 785,
          "cache_read_input_tokens": 26401,
          "cache_creation_input_tokens": 466,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 466
          },
          "type": "message"
        }
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

_source line 25 · 2026-05-25T20:38:06.876Z_

<details><summary>↩ Tool result · `toolu_01ToFkXWpEgYZ1LzsXR5D2JL`</summary>

```text
1	\section{Analysis}\label{sec:analysis}
2	
3	\begin{figure*}[!t]
4	  \centering
5	  \includegraphics[width=\textwidth]{fig3_gate_shift.pdf}
6	  \caption{(a)~Gate turn conditioning: per-layer gate values at turn~1 vs turn~21. In 27/28 layers, gates approach 1.0 at late turns, inverting the design intent ($p = 3.73 \times 10^{-8}$). (b)~Distribution shift ($N$\,=\,5 pilot): the TF-AR GAR gap persists across all five variants. Pilot gaps (20--34$\times$) exceed final $N$\,=\,50 estimates (8--17$\times$; Table~\ref{tab:five-way}) due to smaller sample size.}
7	  \label{fig:gate-shift}
8	\end{figure*}
9	
10	Each subsection kills one alternative hypothesis via causal exclusion: \S\ref{subsec:gate-conditioning}~turn conditioning, \S\ref{subsec:pcgrad}~gradient direction conflict, leaving exposure bias as the primary remaining explanation consistent with current evidence (\S\ref{subsec:dist-shift}). \S\ref{subsec:mechanism-specificity} confirms selectivity; \S\ref{subsec:cross-model} confirms cross-architecture generalization.
11	
12	\subsection{Gate Turn Conditioning}\label{subsec:gate-conditioning}
13	
14	We compare gate values at turn~1 (early) and turn~21 (late) across all 28 layers. The gates invert the design intent: in 27/28 layers, gate values are \emph{lower} at turn~1 than turn~21 (Wilcoxon $p = 3.73 \times 10^{-8}$, $r = 0.975$); e.g., layer~23 shifts from 0.769 to 0.979. NTP pressure pushes gates toward 1.0, a convergence pattern reminiscent of attention collapse in deep transformers \citep{dong2021attention}, yielding inference-time values of 0.93--0.98 (2--7\% attenuation; Table~\ref{tab:five-way}; full gate profiles in Appendix~\ref{sec:appendix-gate-profile}; training dynamics in Appendix~\ref{sec:appendix-training-ext}). The Uniform Gate learns comparable per-layer variation (L3\,=\,0.777, L27\,=\,1.000) despite lacking turn conditioning; the structure thus arises from LoRA$+$GAR pressure (Figure~\ref{fig:gate-shift}a). Does the NTP-GAR gradient conflict prevent the intended behavior?
15	
16	\subsection{PCGrad Gradient Direction Conflict Exclusion}\label{subsec:pcgrad}
17	
18	NTP and GAR gradients oppose in 68--79\% of layers (cosine similarity $-$0.089$\to$$-$0.042 across epochs), with NTP magnitude dominance growing from 7.5$\times$ to 14.7$\times$ (full gradient statistics in Appendix~\ref{sec:appendix-gradient}). If this direction conflict prevents GAR convergence, eliminating it via PCGrad \citep{yu2020pcgrad}, which projects conflicting gradients onto the other's normal plane, should prevent the collapse. To our knowledge, this is the first application of PCGrad as a \emph{diagnostic} tool rather than an optimization method.
19	
20	PCGrad shifts cosine similarity to oscillate around zero, yet TF metrics are unchanged. AR GAR \emph{worsens}: 0.064$\to$0.030 ($p$\,=\,0.002; Figure~\ref{fig:training-pcgrad}b in Appendix~\ref{sec:appendix-gradient}). By \emph{modus tollens}: removing gradient direction conflict does not prevent collapse; therefore it is not the primary cause. PCGrad eliminates direction conflict but does not address magnitude imbalance (NTP dominates GAR by 7.5--14.7$\times$); the worsening under PCGrad may partly reflect projection side-effects rather than confirming that direction conflict is entirely absent as a factor. Cross-model analysis confirms this pattern: Llama-3.1-8B gradients are near-orthogonal (cos\,=\,+0.005) with 25.7$\times$ NTP magnitude dominance (Table~\ref{tab:gradient-crossmodel}).
21	
22	\subsection{Distribution Shift Analysis}\label{subsec:dist-shift}
23	
24	The TF-AR GAR gap persists across all variants (Table~\ref{tab:five-way}). GAR-Dongre provides a control: it remains uniformly low (0.01--0.02) with no distribution gap, evidence that the shift selectively destroys concentrated last-token attention. The mechanism is exposure bias \citep{bengio2015scheduled,zhang2019bridging,arora2022exposure}: during training the model conditions on ground-truth prefixes; at inference, on its own outputs. GAR optimizes a distributional property with no autoregressive counterpart, explaining why TF GAR-ours remains near $\tau$\,=\,0.5 while AR GAR collapses (77--87\% per-turn decay; Figure~\ref{fig:attention-heatmap}; per-configuration AR trajectories in Appendix~\ref{sec:appendix-ar-gar-dynamics}; scaling analysis in Appendix~\ref{sec:appendix-eb-scaling}).
25	
26	\subsection{Mechanism Specificity}\label{subsec:mechanism-specificity}
27	
28	We test specificity with Turn-level Residual Coherence (TRC), the cosine similarity between adjacent-turn hidden states. TF/AR TRC is 0.334/0.332 for ThreadGate (gap $+$0.002) and 0.349/0.411 for LoRA-only (gap $-$0.062, reversed); exposure bias thus disrupts a specific routing behavior while leaving representations intact. Cross-model evaluation confirms: GAR-Dongre shows negligible shift on both Llama (1.002$\times$) and Qwen (1.28$\times$) vs.\ the order-of-magnitude GAR-ours collapse.
29	
30	\begin{figure}[t]
31	  \centering
32	  \includegraphics[width=\columnwidth]{fig_ss_multiseed.pdf}
33	  \caption{Multi-seed AR GAR under scheduled sampling ($\beta$\,=\,0 and $\beta$\,=\,5, three seeds). Steering nearly eliminates seed variance (std: 0.047$\to$0.001).}
34	  \label{fig:ss-multiseed}
35	\end{figure}
36	
37	\subsection{Cross-Model Replication}\label{subsec:cross-model}
38	
39	We replicate on Llama-3.1-8B-Instruct \citep{grattafiori2024llama3} (Base, ThreadGate, LoRA-only; $N$\,=\,20, 4 turns). TF GAR-ours is 0.484 (TG) / 0.481 (LoRA-only); gating contributes zero benefit. The AR distribution is heavy-tailed (coefficient of variation, CoV\,$>$\,100\%); we report medians: 0.018 (TG and LoRA-only), 0.009 (Base), yielding gaps of 27$\times$ and 26$\times$ (Figure~\ref{fig:crossmodel}a in Appendix~\ref{sec:appendix-llama}; per-turn values in Appendix~\ref{sec:appendix-perturn-detail}). Gate profiles differ qualitatively (Figure~\ref{fig:crossmodel}b): Qwen attenuates early layers (L1\,=\,0.793) while Llama dips at late layers (L25\,=\,0.719), an architecture-dependent pattern, but convergence toward identity is universal (Appendix~\ref{sec:appendix-viz}). The gap is substantial on both architectures, consistent with exposure bias as architecture-independent.
40	
41	Scheduled sampling confirms cross-model generalization: Llama SS compresses the gap from ${\sim}$27$\times$ to 2.9$\times$ (TF GAR 0.477, AR GAR 0.166), weaker than Qwen's ${\sim}$1.3$\times$ likely due to fewer training epochs (2 vs.\ 3). The phase transition is architecture-dependent: $\beta$\,=\,3 triggers recovery on Qwen SS (0.593) but not Llama SS (0.173); Llama requires $\beta$\,=\,5 (GAR 0.791, exceeding Qwen SS 0.717; Appendix~\ref{sec:appendix-llama-ss}). Cross-scale validation on Qwen-2.5-1.5B confirms the same pattern (79.8\% GAR decay, $\beta$-steering recovery to 0.715; Appendix~\ref{sec:appendix-1.5b}).
42	
43	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8a88d661-bdad-4394-b9eb-c465ef3bd919",
  "isSidechain": false,
  "promptId": "8817af8a-f189-44e8-a462-1453a12b4ea3",
  "type": "user",
  "uuid": "b7703b09-dd0f-4c64-85bf-60fe19024554",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/analysis.tex",
      "content": "\\section{Analysis}\\label{sec:analysis}\n\n\\begin{figure*}[!t]\n  \\centering\n  \\includegraphics[width=\\textwidth]{fig3_gate_shift.pdf}\n  \\caption{(a)~Gate turn conditioning: per-layer gate values at turn~1 vs turn~21. In 27/28 layers, gates approach 1.0 at late turns, inverting the design intent ($p = 3.73 \\times 10^{-8}$). (b)~Distribution shift ($N$\\,=\\,5 pilot): the TF-AR GAR gap persists across all five variants. Pilot gaps (20--34$\\times$) exceed final $N$\\,=\\,50 estimates (8--17$\\times$; Table~\\ref{tab:five-way}) due to smaller sample size.}\n  \\label{fig:gate-shift}\n\\end{figure*}\n\nEach subsection kills one alternative hypothesis via causal exclusion: \\S\\ref{subsec:gate-conditioning}~turn conditioning, \\S\\ref{subsec:pcgrad}~gradient direction conflict, leaving exposure bias as the primary remaining explanation consistent with current evidence (\\S\\ref{subsec:dist-shift}). \\S\\ref{subsec:mechanism-specificity} confirms selectivity; \\S\\ref{subsec:cross-model} confirms cross-architecture generalization.\n\n\\subsection{Gate Turn Conditioning}\\label{subsec:gate-conditioning}\n\nWe compare gate values at turn~1 (early) and turn~21 (late) across all 28 layers. The gates invert the design intent: in 27/28 layers, gate values are \\emph{lower} at turn~1 than turn~21 (Wilcoxon $p = 3.73 \\times 10^{-8}$, $r = 0.975$); e.g., layer~23 shifts from 0.769 to 0.979. NTP pressure pushes gates toward 1.0, a convergence pattern reminiscent of attention collapse in deep transformers \\citep{dong2021attention}, yielding inference-time values of 0.93--0.98 (2--7\\% attenuation; Table~\\ref{tab:five-way}; full gate profiles in Appendix~\\ref{sec:appendix-gate-profile}; training dynamics in Appendix~\\ref{sec:appendix-training-ext}). The Uniform Gate learns comparable per-layer variation (L3\\,=\\,0.777, L27\\,=\\,1.000) despite lacking turn conditioning; the structure thus arises from LoRA$+$GAR pressure (Figure~\\ref{fig:gate-shift}a). Does the NTP-GAR gradient conflict prevent the intended behavior?\n\n\\subsection{PCGrad Gradient Direction Conflict Exclusion}\\label{subsec:pcgrad}\n\nNTP and GAR gradients oppose in 68--79\\% of layers (cosine similarity $-$0.089$\\to$$-$0.042 across epochs), with NTP magnitude dominance growing from 7.5$\\times$ to 14.7$\\times$ (full gradient statistics in Appendix~\\ref{sec:appendix-gradient}). If this direction conflict prevents GAR convergence, eliminating it via PCGrad \\citep{yu2020pcgrad}, which projects conflicting gradients onto the other's normal plane, should prevent the collapse. To our knowledge, this is the first application of PCGrad as a \\emph{diagnostic} tool rather than an optimization method.\n\nPCGrad shifts cosine similarity to oscillate around zero, yet TF metrics are unchanged. AR GAR \\emph{worsens}: 0.064$\\to$0.030 ($p$\\,=\\,0.002; Figure~\\ref{fig:training-pcgrad}b in Appendix~\\ref{sec:appendix-gradient}). By \\emph{modus tollens}: removing gradient direction conflict does not prevent collapse; therefore it is not the primary cause. PCGrad eliminates direction conflict but does not address magnitude imbalance (NTP dominates GAR by 7.5--14.7$\\times$); the worsening under PCGrad may partly reflect projection side-effects rather than confirming that direction conflict is entirely absent as a factor. Cross-model analysis confirms this pattern: Llama-3.1-8B gradients are near-orthogonal (cos\\,=\\,+0.005) with 25.7$\\times$ NTP magnitude dominance (Table~\\ref{tab:gradient-crossmodel}).\n\n\\subsection{Distribution Shift Analysis}\\label{subsec:dist-shift}\n\nThe TF-AR GAR gap persists across all variants (Table~\\ref{tab:five-way}). GAR-Dongre provides a control: it remains uniformly low (0.01--0.02) with no distribution gap, evidence that the shift selectively destroys concentrated last-token attention. The mechanism is exposure bias \\citep{bengio2015scheduled,zhang2019bridging,arora2022exposure}: during training the model conditions on ground-truth prefixes; at inference, on its own outputs. GAR optimizes a distributional property with no autoregressive counterpart, explaining why TF GAR-ours remains near $\\tau$\\,=\\,0.5 while AR GAR collapses (77--87\\% per-turn decay; Figure~\\ref{fig:attention-heatmap}; per-configuration AR trajectories in Appendix~\\ref{sec:appendix-ar-gar-dynamics}; scaling analysis in Appendix~\\ref{sec:appendix-eb-scaling}).\n\n\\subsection{Mechanism Specificity}\\label{subsec:mechanism-specificity}\n\nWe test specificity with Turn-level Residual Coherence (TRC), the cosine similarity between adjacent-turn hidden states. TF/AR TRC is 0.334/0.332 for ThreadGate (gap $+$0.002) and 0.349/0.411 for LoRA-only (gap $-$0.062, reversed); exposure bias thus disrupts a specific routing behavior while leaving representations intact. Cross-model evaluation confirms: GAR-Dongre shows negligible shift on both Llama (1.002$\\times$) and Qwen (1.28$\\times$) vs.\\ the order-of-magnitude GAR-ours collapse.\n\n\\begin{figure}[t]\n  \\centering\n  \\includegraphics[width=\\columnwidth]{fig_ss_multiseed.pdf}\n  \\caption{Multi-seed AR GAR under scheduled sampling ($\\beta$\\,=\\,0 and $\\beta$\\,=\\,5, three seeds). Steering nearly eliminates seed variance (std: 0.047$\\to$0.001).}\n  \\label{fig:ss-multiseed}\n\\end{figure}\n\n\\subsection{Cross-Model Replication}\\label{subsec:cross-model}\n\nWe replicate on Llama-3.1-8B-Instruct \\citep{grattafiori2024llama3} (Base, ThreadGate, LoRA-only; $N$\\,=\\,20, 4 turns). TF GAR-ours is 0.484 (TG) / 0.481 (LoRA-only); gating contributes zero benefit. The AR distribution is heavy-tailed (coefficient of variation, CoV\\,$>$\\,100\\%); we report medians: 0.018 (TG and LoRA-only), 0.009 (Base), yielding gaps of 27$\\times$ and 26$\\times$ (Figure~\\ref{fig:crossmodel}a in Appendix~\\ref{sec:appendix-llama}; per-turn values in Appendix~\\ref{sec:appendix-perturn-detail}). Gate profiles differ qualitatively (Figure~\\ref{fig:crossmodel}b): Qwen attenuates early layers (L1\\,=\\,0.793) while Llama dips at late layers (L25\\,=\\,0.719), an architecture-dependent pattern, but convergence toward identity is universal (Appendix~\\ref{sec:appendix-viz}). The gap is substantial on both architectures, consistent with exposure bias as architecture-independent.\n\nScheduled sampling confirms cross-model generalization: Llama SS compresses the gap from ${\\sim}$27$\\times$ to 2.9$\\times$ (TF GAR 0.477, AR GAR 0.166), weaker than Qwen's ${\\sim}$1.3$\\times$ likely due to fewer training epochs (2 vs.\\ 3). The phase transition is architecture-dependent: $\\beta$\\,=\\,3 triggers recovery on Qwen SS (0.593) but not Llama SS (0.173); Llama requires $\\beta$\\,=\\,5 (GAR 0.791, exceeding Qwen SS 0.717; Appendix~\\ref{sec:appendix-llama-ss}). Cross-scale validation on Qwen-2.5-1.5B confirms the same pattern (79.8\\% GAR decay, $\\beta$-steering recovery to 0.715; Appendix~\\ref{sec:appendix-1.5b}).\n\n",
      "numLines": 43,
      "startLine": 1,
      "totalLines": 43
    }
  },
  "sourceToolAssistantUUID": "8a88d661-bdad-4394-b9eb-c465ef3bd919",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "4b680861-4da7-411a-8744-3dabfdaf2205",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-25T20:38:07.165Z_

<details open><summary>🔧 Tool call — Read · `toolu_01FbEhQPS3ThCMtgZV6YiSyd`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b7703b09-dd0f-4c64-85bf-60fe19024554",
  "isSidechain": false,
  "requestId": "req_011CbPvwbVfNQCwbcnsYNfCu",
  "type": "assistant",
  "uuid": "67505b97-b0a3-4ef1-ab3f-9969a7a83660",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "4b680861-4da7-411a-8744-3dabfdaf2205",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014omTEWaQWBnZwZbaHNXrM6",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 466,
      "cache_read_input_tokens": 26401,
      "output_tokens": 785,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 466,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 785,
          "cache_read_input_tokens": 26401,
          "cache_creation_input_tokens": 466,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 466
          },
          "type": "message"
        }
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

_source line 27 · 2026-05-25T20:38:07.170Z_

<details><summary>↩ Tool result · `toolu_01FbEhQPS3ThCMtgZV6YiSyd`</summary>

```text
1	\section{Discussion}\label{sec:discussion}
2	
3	\looseness=-1 NTP self-recovers because prediction is the same task at both regimes \citep{he2019exposure}; GAR optimizes a \emph{global property} (attention allocation to goal tokens) with no autoregressive counterpart. The collapse is selective: GAR-ours collapses by an order of magnitude while GAR-Dongre shows negligible shift (${\leq}$1.3$\times$). Per-head analysis confirms selectivity: heads with higher TF GAR shift most under AR ($r$\,=\,0.743; Appendix~\ref{sec:appendix-kl}). Any auxiliary attention objective targeting distributional properties rather than prediction itself should face the same barrier under teacher forcing.
4	
5	\looseness=-1 Our exclusion identifies exposure bias as a primary contributing factor, but cannot fully rule out KV cache drift (\S\ref{sec:limitations}). The PCGrad exclusion rules out direction conflict but not magnitude imbalance (7.5--25.7$\times$ NTP dominance; \citealp{chen2018gradnorm}). The GAR--compliance correlation is weak ($r$\,=\,0.200; Appendix~\ref{sec:appendix-ir}), reinforcing GAR's role as a diagnostic probe. Our $\beta$-steering is likewise a \emph{diagnostic}, distinct from inference-time remedies such as split-softmax \citep{li2024measuring} and Rhea \citep{hong2025rhea}. SS and inference-time fixes are complementary: SS modifies representations without inference cost; inference-time methods cannot recover patterns never learned. At $\beta$\,=\,5 the two converge (SS\,=\,0.717 vs.\ TG\,=\,0.727).
6	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "67505b97-b0a3-4ef1-ab3f-9969a7a83660",
  "isSidechain": false,
  "promptId": "8817af8a-f189-44e8-a462-1453a12b4ea3",
  "type": "user",
  "uuid": "79231320-e79b-4b4e-b891-ed4f86922fc3",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/discussion.tex",
      "content": "\\section{Discussion}\\label{sec:discussion}\n\n\\looseness=-1 NTP self-recovers because prediction is the same task at both regimes \\citep{he2019exposure}; GAR optimizes a \\emph{global property} (attention allocation to goal tokens) with no autoregressive counterpart. The collapse is selective: GAR-ours collapses by an order of magnitude while GAR-Dongre shows negligible shift (${\\leq}$1.3$\\times$). Per-head analysis confirms selectivity: heads with higher TF GAR shift most under AR ($r$\\,=\\,0.743; Appendix~\\ref{sec:appendix-kl}). Any auxiliary attention objective targeting distributional properties rather than prediction itself should face the same barrier under teacher forcing.\n\n\\looseness=-1 Our exclusion identifies exposure bias as a primary contributing factor, but cannot fully rule out KV cache drift (\\S\\ref{sec:limitations}). The PCGrad exclusion rules out direction conflict but not magnitude imbalance (7.5--25.7$\\times$ NTP dominance; \\citealp{chen2018gradnorm}). The GAR--compliance correlation is weak ($r$\\,=\\,0.200; Appendix~\\ref{sec:appendix-ir}), reinforcing GAR's role as a diagnostic probe. Our $\\beta$-steering is likewise a \\emph{diagnostic}, distinct from inference-time remedies such as split-softmax \\citep{li2024measuring} and Rhea \\citep{hong2025rhea}. SS and inference-time fixes are complementary: SS modifies representations without inference cost; inference-time methods cannot recover patterns never learned. At $\\beta$\\,=\\,5 the two converge (SS\\,=\\,0.717 vs.\\ TG\\,=\\,0.727).\n",
      "numLines": 6,
      "startLine": 1,
      "totalLines": 6
    }
  },
  "sourceToolAssistantUUID": "67505b97-b0a3-4ef1-ab3f-9969a7a83660",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "4b680861-4da7-411a-8744-3dabfdaf2205",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-25T20:38:07.642Z_

<details open><summary>🔧 Tool call — Read · `toolu_01EaBxMQNh6dPd5ujF3yq7EK`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "79231320-e79b-4b4e-b891-ed4f86922fc3",
  "isSidechain": false,
  "requestId": "req_011CbPvwbVfNQCwbcnsYNfCu",
  "type": "assistant",
  "uuid": "b4eab8ab-5480-4a70-93a8-bdbe14ee5229",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "4b680861-4da7-411a-8744-3dabfdaf2205",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014omTEWaQWBnZwZbaHNXrM6",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 466,
      "cache_read_input_tokens": 26401,
      "output_tokens": 785,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 466,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 785,
          "cache_read_input_tokens": 26401,
          "cache_creation_input_tokens": 466,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 466
          },
          "type": "message"
        }
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

_source line 29 · 2026-05-25T20:38:07.647Z_

<details><summary>↩ Tool result · `toolu_01EaBxMQNh6dPd5ujF3yq7EK`</summary>

```text
1	\section{Conclusion}\label{sec:conclusion}
2	
3	\looseness=-1 Auxiliary attention losses converge under teacher forcing (GAR\,=\,0.50) but collapse by an order of magnitude under autoregressive generation on two architectures. A five-way diagnostic comparison identifies exposure bias as a primary contributing factor; $\beta$-steering recovers GAR above the TF baseline, consistent with attention misallocation as a proximal cause (KV cache drift remains untested). Scheduled sampling compresses the gap to ${\sim}$1.3$\times$ (Qwen) and ${\sim}$2.9$\times$ (Llama), generalizing across architectures and seeds; to our knowledge, the first such transfer to auxiliary attention objectives in multi-turn transformers.
4	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b4eab8ab-5480-4a70-93a8-bdbe14ee5229",
  "isSidechain": false,
  "promptId": "8817af8a-f189-44e8-a462-1453a12b4ea3",
  "type": "user",
  "uuid": "69903d65-ba5b-4944-8d62-d2770a30a64a",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/conclusion.tex",
      "content": "\\section{Conclusion}\\label{sec:conclusion}\n\n\\looseness=-1 Auxiliary attention losses converge under teacher forcing (GAR\\,=\\,0.50) but collapse by an order of magnitude under autoregressive generation on two architectures. A five-way diagnostic comparison identifies exposure bias as a primary contributing factor; $\\beta$-steering recovers GAR above the TF baseline, consistent with attention misallocation as a proximal cause (KV cache drift remains untested). Scheduled sampling compresses the gap to ${\\sim}$1.3$\\times$ (Qwen) and ${\\sim}$2.9$\\times$ (Llama), generalizing across architectures and seeds; to our knowledge, the first such transfer to auxiliary attention objectives in multi-turn transformers.\n",
      "numLines": 4,
      "startLine": 1,
      "totalLines": 4
    }
  },
  "sourceToolAssistantUUID": "b4eab8ab-5480-4a70-93a8-bdbe14ee5229",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "4b680861-4da7-411a-8744-3dabfdaf2205",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 30 · 2026-05-25T20:38:08.113Z_

<details open><summary>🔧 Tool call — Read · `toolu_01BQB2hyNGwYjy8zCFz59PSo`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "69903d65-ba5b-4944-8d62-d2770a30a64a",
  "isSidechain": false,
  "requestId": "req_011CbPvwbVfNQCwbcnsYNfCu",
  "type": "assistant",
  "uuid": "3b421aa9-3362-421a-9312-bc6e57fa4213",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "4b680861-4da7-411a-8744-3dabfdaf2205",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014omTEWaQWBnZwZbaHNXrM6",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 466,
      "cache_read_input_tokens": 26401,
      "output_tokens": 785,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 466,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 785,
          "cache_read_input_tokens": 26401,
          "cache_creation_input_tokens": 466,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 466
          },
          "type": "message"
        }
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

_source line 31 · 2026-05-25T20:38:08.118Z_

<details><summary>↩ Tool result · `toolu_01BQB2hyNGwYjy8zCFz59PSo`</summary>

```text
1	\section*{Limitations}\label{sec:limitations}
2	
3	Our findings are demonstrated on two model families (Qwen-2.5-7B and Llama-3.1-8B) and a single dataset (UltraChat, 8K conversations); generalization to other architectures and domains (e.g., code, reasoning) is untested. Most configurations use a single seed (scheduled sampling validated on three seeds; \S\ref{subsec:ss}), and quality assessment relies on PPL rather than comprehensive benchmarks \citep{hendrycks2021measuring,lin2022truthfulqa}. We test only one auxiliary loss family (GAR with MSE target $\tau$\,=\,0.5); head-specific or layer-specific losses may exhibit different sensitivity to exposure bias. Our causal exclusion identifies exposure bias as a primary factor but does not rule out KV cache drift as a contributing mechanism.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3b421aa9-3362-421a-9312-bc6e57fa4213",
  "isSidechain": false,
  "promptId": "8817af8a-f189-44e8-a462-1453a12b4ea3",
  "type": "user",
  "uuid": "27e5b537-8b3e-47b3-ac9f-4ff23f8a6b39",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/limitations.tex",
      "content": "\\section*{Limitations}\\label{sec:limitations}\n\nOur findings are demonstrated on two model families (Qwen-2.5-7B and Llama-3.1-8B) and a single dataset (UltraChat, 8K conversations); generalization to other architectures and domains (e.g., code, reasoning) is untested. Most configurations use a single seed (scheduled sampling validated on three seeds; \\S\\ref{subsec:ss}), and quality assessment relies on PPL rather than comprehensive benchmarks \\citep{hendrycks2021measuring,lin2022truthfulqa}. We test only one auxiliary loss family (GAR with MSE target $\\tau$\\,=\\,0.5); head-specific or layer-specific losses may exhibit different sensitivity to exposure bias. Our causal exclusion identifies exposure bias as a primary factor but does not rule out KV cache drift as a contributing mechanism.",
      "numLines": 3,
      "startLine": 1,
      "totalLines": 3
    }
  },
  "sourceToolAssistantUUID": "3b421aa9-3362-421a-9312-bc6e57fa4213",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "4b680861-4da7-411a-8744-3dabfdaf2205",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 32 · 2026-05-25T20:38:08.575Z_

<details open><summary>🔧 Tool call — Read · `toolu_01XUiaw5NMrjBb1C8DVVtmtk`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "27e5b537-8b3e-47b3-ac9f-4ff23f8a6b39",
  "isSidechain": false,
  "requestId": "req_011CbPvwbVfNQCwbcnsYNfCu",
  "type": "assistant",
  "uuid": "a562e8fe-317f-4bc6-895c-1b46d065b5fa",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "4b680861-4da7-411a-8744-3dabfdaf2205",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014omTEWaQWBnZwZbaHNXrM6",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 466,
      "cache_read_input_tokens": 26401,
      "output_tokens": 785,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 466,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 785,
          "cache_read_input_tokens": 26401,
          "cache_creation_input_tokens": 466,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 466
          },
          "type": "message"
        }
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

_source line 33 · 2026-05-25T20:38:08.660Z_

```json
{
  "parentUuid": "42459c76-db1f-4537-ba53-528bcaf3e4da",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "6adaf22d-c45d-4f2c-9aed-a1c2d3465360",
  "timestamp": "2026-05-25T20:38:08.660Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "4b680861-4da7-411a-8744-3dabfdaf2205",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

---

### Runtime record

_source line 34_

```json
{
  "type": "last-prompt",
  "leafUuid": "6adaf22d-c45d-4f2c-9aed-a1c2d3465360",
  "sessionId": "4b680861-4da7-411a-8744-3dabfdaf2205"
}
```

---

### Runtime record

_source line 35_

```json
{
  "type": "ai-title",
  "aiTitle": "Audit quantitative claims in paper body text",
  "sessionId": "4b680861-4da7-411a-8744-3dabfdaf2205"
}
```

---

### Assistant

_source line 36 · 2026-05-25T20:38:16.303Z_

<details><summary>Logged reasoning block</summary>

```text
The registry data was too large to load directly. I need to use jq or python to extract the relevant data. Let me also read the table files. Let me start by probing the registry data structure and reading the table files in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6adaf22d-c45d-4f2c-9aed-a1c2d3465360",
  "isSidechain": false,
  "requestId": "req_011CbPvx9YEToBD4fX5BDSEx",
  "type": "assistant",
  "uuid": "9df01a7e-d7b5-465d-9b51-ff9051a44e2e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "4b680861-4da7-411a-8744-3dabfdaf2205",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TAchN9TrtdNiR9pkqfdqe9",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12997,
      "cache_read_input_tokens": 26867,
      "output_tokens": 448,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12997,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 448,
          "cache_read_input_tokens": 26867,
          "cache_creation_input_tokens": 12997,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12997
          },
          "type": "message"
        }
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

_source line 37 · 2026-05-25T20:38:16.326Z_

Registry data is too large to load directly. Let me probe its structure and read the table files in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9df01a7e-d7b5-465d-9b51-ff9051a44e2e",
  "isSidechain": false,
  "requestId": "req_011CbPvx9YEToBD4fX5BDSEx",
  "type": "assistant",
  "uuid": "4c7c5557-f491-400f-9809-b3448dc961c4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "4b680861-4da7-411a-8744-3dabfdaf2205",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TAchN9TrtdNiR9pkqfdqe9",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12997,
      "cache_read_input_tokens": 26867,
      "output_tokens": 448,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12997,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 448,
          "cache_read_input_tokens": 26867,
          "cache_creation_input_tokens": 12997,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12997
          },
          "type": "message"
        }
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

_source line 38 · 2026-05-25T20:38:20.917Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01GQB9w4sQxCssoieSQRnLVY`</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-11-projects-turn-residual-gating/4b680861-4da7-411a-8744-3dabfdaf2205/tool-results/mcp-agent-ml-research-read_registry-1779741484333.txt | python3 -c \"\nimport json, sys\ndata = json.load(sys.stdin)\nresult = json.loads(data['result'])\nprint(f'Type: {type(result).__name__}, Length: {len(result)}')\nfor exp in result:\n    print(f\\\"  {exp.get('exp_id','?')}: status={exp.get('status','?')}\\\")\n\" 2>/dev/null | head -60",
  "description": "Probe registry structure and list experiment IDs"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4c7c5557-f491-400f-9809-b3448dc961c4",
  "isSidechain": false,
  "requestId": "req_011CbPvx9YEToBD4fX5BDSEx",
  "type": "assistant",
  "uuid": "bd0ce836-401f-4c2f-90f3-2ff90dae2a9f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "4b680861-4da7-411a-8744-3dabfdaf2205",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TAchN9TrtdNiR9pkqfdqe9",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12997,
      "cache_read_input_tokens": 26867,
      "output_tokens": 448,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12997,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 448,
          "cache_read_input_tokens": 26867,
          "cache_creation_input_tokens": 12997,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12997
          },
          "type": "message"
        }
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

_source line 39 · 2026-05-25T20:38:21.973Z_

<details><summary>↩ Tool result · `toolu_01M2X1DDUgFqDERgdNoVsHLQ`</summary>

```text
artifacts/_project/paper/tab_dataset_stats.tex
artifacts/_project/paper/tab_gar_robustness.tex
artifacts/_project/paper/tab_mmlu_detail.tex
artifacts/_project/paper/tab_qwen15b_results.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f95e971b-4ad5-4e9a-b981-42dbbc7dede9",
  "isSidechain": false,
  "promptId": "8817af8a-f189-44e8-a462-1453a12b4ea3",
  "type": "user",
  "uuid": "7fe59473-a81a-4a73-9757-c191958ad9dd",
  "toolUseResult": {
    "filenames": [
      "artifacts/_project/paper/tab_dataset_stats.tex",
      "artifacts/_project/paper/tab_gar_robustness.tex",
      "artifacts/_project/paper/tab_mmlu_detail.tex",
      "artifacts/_project/paper/tab_qwen15b_results.tex"
    ],
    "durationMs": 10,
    "numFiles": 4,
    "truncated": false
  },
  "sourceToolAssistantUUID": "f95e971b-4ad5-4e9a-b981-42dbbc7dede9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "4b680861-4da7-411a-8744-3dabfdaf2205",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-25T20:38:21.468Z_

<details><summary>↩ Tool result · `toolu_01GQB9w4sQxCssoieSQRnLVY`</summary>

```text
Type: dict, Length: 4
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bd0ce836-401f-4c2f-90f3-2ff90dae2a9f",
  "isSidechain": false,
  "promptId": "8817af8a-f189-44e8-a462-1453a12b4ea3",
  "type": "user",
  "uuid": "d26f676a-663e-4571-91ff-4352a3ed5968",
  "toolUseResult": {
    "stdout": "Type: dict, Length: 4",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "bd0ce836-401f-4c2f-90f3-2ff90dae2a9f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "4b680861-4da7-411a-8744-3dabfdaf2205",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-25T20:38:21.958Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01M2X1DDUgFqDERgdNoVsHLQ`</summary>

```json
{
  "pattern": "tab_*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/_project/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d26f676a-663e-4571-91ff-4352a3ed5968",
  "isSidechain": false,
  "requestId": "req_011CbPvx9YEToBD4fX5BDSEx",
  "type": "assistant",
  "uuid": "f95e971b-4ad5-4e9a-b981-42dbbc7dede9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "4b680861-4da7-411a-8744-3dabfdaf2205",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TAchN9TrtdNiR9pkqfdqe9",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12997,
      "cache_read_input_tokens": 26867,
      "output_tokens": 448,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12997,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 448,
          "cache_read_input_tokens": 26867,
          "cache_creation_input_tokens": 12997,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12997
          },
          "type": "message"
        }
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

_source line 42 · 2026-05-25T20:38:25.293Z_

<details><summary>Logged reasoning block</summary>

```text
The registry is a dict with 4 keys, not a list. Let me probe deeper.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7fe59473-a81a-4a73-9757-c191958ad9dd",
  "isSidechain": false,
  "requestId": "req_011CbPvyAmS1ddb5Qc1WjJAk",
  "type": "assistant",
  "uuid": "f045c818-e362-476c-8067-b26d7824c4d4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "4b680861-4da7-411a-8744-3dabfdaf2205",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019YTh7to4WGW5fTQTAeCLz1",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 579,
      "cache_read_input_tokens": 39864,
      "output_tokens": 366,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 579,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 366,
          "cache_read_input_tokens": 39864,
          "cache_creation_input_tokens": 579,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 579
          },
          "type": "message"
        }
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

_source line 43 · 2026-05-25T20:38:28.655Z_

<details open><summary>🔧 Tool call — Bash · `toolu_017fALosnBBpokUfNUZMsgnz`</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-11-projects-turn-residual-gating/4b680861-4da7-411a-8744-3dabfdaf2205/tool-results/mcp-agent-ml-research-read_registry-1779741484333.txt | python3 -c \"\nimport json, sys\ndata = json.load(sys.stdin)\nresult = json.loads(data['result'])\nprint('Keys:', list(result.keys()))\nprint()\n# It's likely a dict of exp_id -> exp_data\nfor k in result:\n    v = result[k]\n    if isinstance(v, dict):\n        print(f'{k}: keys={list(v.keys())[:10]}')\n    elif isinstance(v, list):\n        print(f'{k}: list of {len(v)} items')\n    else:\n        print(f'{k}: {type(v).__name__} = {str(v)[:100]}')\n\" 2>/dev/null",
  "description": "Probe registry dict structure"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f045c818-e362-476c-8067-b26d7824c4d4",
  "isSidechain": false,
  "requestId": "req_011CbPvyAmS1ddb5Qc1WjJAk",
  "type": "assistant",
  "uuid": "3d12809c-e19f-41b6-a2fb-e0c6ded5d0a7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "4b680861-4da7-411a-8744-3dabfdaf2205",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019YTh7to4WGW5fTQTAeCLz1",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 579,
      "cache_read_input_tokens": 39864,
      "output_tokens": 366,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 579,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 366,
          "cache_read_input_tokens": 39864,
          "cache_creation_input_tokens": 579,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 579
          },
          "type": "message"
        }
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

_source line 44 · 2026-05-25T20:38:28.820Z_

<details><summary>↩ Tool result · `toolu_017fALosnBBpokUfNUZMsgnz`</summary>

```text
Keys: ['success', 'data', 'error', 'metadata']

success: bool = True
data: keys=['experiments', 'count', 'total', 'baseline']
error: NoneType = None
metadata: keys=['elapsed_seconds']
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3d12809c-e19f-41b6-a2fb-e0c6ded5d0a7",
  "isSidechain": false,
  "promptId": "8817af8a-f189-44e8-a462-1453a12b4ea3",
  "type": "user",
  "uuid": "ac4205bd-d936-45ed-bafa-7eb597b876c4",
  "toolUseResult": {
    "stdout": "Keys: ['success', 'data', 'error', 'metadata']\n\nsuccess: bool = True\ndata: keys=['experiments', 'count', 'total', 'baseline']\nerror: NoneType = None\nmetadata: keys=['elapsed_seconds']",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "3d12809c-e19f-41b6-a2fb-e0c6ded5d0a7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "4b680861-4da7-411a-8744-3dabfdaf2205",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 45 · 2026-05-25T20:38:33.059Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01EXrwxfm15affwB538qaVwW`</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-11-projects-turn-residual-gating/4b680861-4da7-411a-8744-3dabfdaf2205/tool-results/mcp-agent-ml-research-read_registry-1779741484333.txt | python3 -c \"\nimport json, sys\ndata = json.load(sys.stdin)\nresult = json.loads(data['result'])\nexperiments = result['data']['experiments']\nprint(f'Experiments count: {len(experiments)}')\nfor exp in experiments:\n    eid = exp.get('exp_id', '?')\n    status = exp.get('status', '?')\n    print(f'  {eid}: status={status}')\n\" 2>/dev/null",
  "description": "List all experiment IDs from registry"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ac4205bd-d936-45ed-bafa-7eb597b876c4",
  "isSidechain": false,
  "requestId": "req_011CbPvydp7vsWm71qzKXwPG",
  "type": "assistant",
  "uuid": "27c1b9b1-1403-47be-9114-bb7f26721ed6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "4b680861-4da7-411a-8744-3dabfdaf2205",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BaQwQEBTijrs2aiQzxVLsX",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 437,
      "cache_read_input_tokens": 40443,
      "output_tokens": 280,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 437,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 280,
          "cache_read_input_tokens": 40443,
          "cache_creation_input_tokens": 437,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 437
          },
          "type": "message"
        }
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

_source line 46 · 2026-05-25T20:38:33.276Z_

<details><summary>↩ Tool result · reported error · `toolu_01EXrwxfm15affwB538qaVwW`</summary>

```text
Exit code 1
Experiments count: 60
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "27c1b9b1-1403-47be-9114-bb7f26721ed6",
  "isSidechain": false,
  "promptId": "8817af8a-f189-44e8-a462-1453a12b4ea3",
  "type": "user",
  "uuid": "94852cf5-7c62-4297-91d9-745fd8f07ee3",
  "toolUseResult": "Error: Exit code 1\nExperiments count: 60",
  "sourceToolAssistantUUID": "27c1b9b1-1403-47be-9114-bb7f26721ed6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "4b680861-4da7-411a-8744-3dabfdaf2205",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 47 · 2026-05-25T20:38:36.437Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01KMry3trkkyfzgtUT7UqTbr`</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-11-projects-turn-residual-gating/4b680861-4da7-411a-8744-3dabfdaf2205/tool-results/mcp-agent-ml-research-read_registry-1779741484333.txt | python3 -c \"\nimport json, sys\ndata = json.load(sys.stdin)\nresult = json.loads(data['result'])\nexperiments = result['data']['experiments']\nfor exp in experiments:\n    eid = exp.get('exp_id', '?')\n    status = exp.get('status', '?')\n    print(f'{eid}: status={status}')\n\" 2>/dev/null",
  "description": "List experiment IDs"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "94852cf5-7c62-4297-91d9-745fd8f07ee3",
  "isSidechain": false,
  "requestId": "req_011CbPvyxme1BbYH9ct9mhK6",
  "type": "assistant",
  "uuid": "9c54d6f2-9003-416c-9dd4-26a8b27d7290",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "4b680861-4da7-411a-8744-3dabfdaf2205",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AZWgqEMnjsFCEFgpUCXcXG",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 311,
      "cache_read_input_tokens": 40880,
      "output_tokens": 260,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 311,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 260,
          "cache_read_input_tokens": 40880,
          "cache_creation_input_tokens": 311,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 311
          },
          "type": "message"
        }
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

_source line 48 · 2026-05-25T20:38:36.668Z_

<details><summary>↩ Tool result · reported error · `toolu_01KMry3trkkyfzgtUT7UqTbr`</summary>

```text
Exit code 1
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9c54d6f2-9003-416c-9dd4-26a8b27d7290",
  "isSidechain": false,
  "promptId": "8817af8a-f189-44e8-a462-1453a12b4ea3",
  "type": "user",
  "uuid": "ae0b2cab-3803-42de-9c63-875300a202a3",
  "toolUseResult": "Error: Exit code 1",
  "sourceToolAssistantUUID": "9c54d6f2-9003-416c-9dd4-26a8b27d7290",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "4b680861-4da7-411a-8744-3dabfdaf2205",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 49 · 2026-05-25T20:38:40.304Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01EThAJQDiPe2rGu47eA32nb`</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-11-projects-turn-residual-gating/4b680861-4da7-411a-8744-3dabfdaf2205/tool-results/mcp-agent-ml-research-read_registry-1779741484333.txt | python3 -c \"\nimport json, sys\ndata = json.load(sys.stdin)\nresult = json.loads(data['result'])\nexperiments = result['data']['experiments']\nfor i, exp in enumerate(experiments):\n    eid = exp.get('exp_id', '?')\n    status = exp.get('status', '?')\n    sys.stdout.write(f'{eid}: status={status}\\n')\n    sys.stdout.flush()\n\" 2>&1 | head -70",
  "description": "List experiment IDs (flush output)"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ae0b2cab-3803-42de-9c63-875300a202a3",
  "isSidechain": false,
  "requestId": "req_011CbPvzDGmnGdVkBahZxsGK",
  "type": "assistant",
  "uuid": "d602e3ee-0357-4b2b-a0b1-5053641e9b3e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "4b680861-4da7-411a-8744-3dabfdaf2205",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JuhxcJ58kKDKKBavdZXNpu",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 284,
      "cache_read_input_tokens": 41191,
      "output_tokens": 283,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 284,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 283,
          "cache_read_input_tokens": 41191,
          "cache_creation_input_tokens": 284,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 284
          },
          "type": "message"
        }
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

_source line 50 · 2026-05-25T20:38:40.527Z_

<details><summary>↩ Tool result · `toolu_01EThAJQDiPe2rGu47eA32nb`</summary>

```text
Traceback (most recent call last):
  File "&lt;string>", line 7, in &lt;module>
    eid = exp.get('exp_id', '?')
          ^^^^^^^
AttributeError: 'str' object has no attribute 'get'
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d602e3ee-0357-4b2b-a0b1-5053641e9b3e",
  "isSidechain": false,
  "promptId": "8817af8a-f189-44e8-a462-1453a12b4ea3",
  "type": "user",
  "uuid": "ec679c95-6e5f-4b01-9262-3347ce72568a",
  "toolUseResult": {
    "stdout": "Traceback (most recent call last):\n  File \"&lt;string>\", line 7, in &lt;module>\n    eid = exp.get('exp_id', '?')\n          ^^^^^^^\nAttributeError: 'str' object has no attribute 'get'",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "d602e3ee-0357-4b2b-a0b1-5053641e9b3e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "4b680861-4da7-411a-8744-3dabfdaf2205",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 51 · 2026-05-25T20:38:45.690Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01FYJ4Km52QswesL1Z1qyrmS`</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-11-projects-turn-residual-gating/4b680861-4da7-411a-8744-3dabfdaf2205/tool-results/mcp-agent-ml-research-read_registry-1779741484333.txt | python3 -c \"\nimport json, sys\ndata = json.load(sys.stdin)\nresult = json.loads(data['result'])\nexperiments = result['data']['experiments']\nprint(type(experiments).__name__)\nif isinstance(experiments, dict):\n    for k in list(experiments.keys())[:5]:\n        v = experiments[k]\n        print(f'{k}: type={type(v).__name__}, keys={list(v.keys())[:8] if isinstance(v, dict) else \\\"N/A\\\"}')\nelif isinstance(experiments, list):\n    print(type(experiments[0]).__name__)\n    print(experiments[0][:200] if isinstance(experiments[0], str) else str(experiments[0])[:200])\n\" 2>&1",
  "description": "Probe experiments data type"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ec679c95-6e5f-4b01-9262-3347ce72568a",
  "isSidechain": false,
  "requestId": "req_011CbPvzVoC5EGuNXMgpunxn",
  "type": "assistant",
  "uuid": "425d60b3-c9c7-46be-bee3-25ee01a5c2d2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "4b680861-4da7-411a-8744-3dabfdaf2205",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01V79UZMEsnHULhNoaaXifyD",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 356,
      "cache_read_input_tokens": 41475,
      "output_tokens": 343,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 356,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 343,
          "cache_read_input_tokens": 41475,
          "cache_creation_input_tokens": 356,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 356
          },
          "type": "message"
        }
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

_source line 52 · 2026-05-25T20:38:45.797Z_

<details><summary>↩ Tool result · `toolu_01FYJ4Km52QswesL1Z1qyrmS`</summary>

```text
dict
phase1a_multiseed_qwen: type=dict, keys=['status', 'retry_count', 'created_at', 'updated_at', 'hypothesis', 'spec', 'conclusion', 'notes']
p1_ss_lora_only: type=dict, keys=['status', 'retry_count', 'created_at', 'updated_at', 'hypothesis', 'spec', 'conclusion', 'completed_at']
phase2_switching: type=dict, keys=['status', 'retry_count', 'created_at', 'updated_at', 'hypothesis', 'conclusion', 'completed_at']
phase2_tf_ar_switching: type=dict, keys=['status', 'retry_count', 'created_at', 'updated_at', 'hypothesis']
phase1a_multiseed_8runs: type=dict, keys=['status', 'retry_count', 'created_at', 'updated_at', 'spec']
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "425d60b3-c9c7-46be-bee3-25ee01a5c2d2",
  "isSidechain": false,
  "promptId": "8817af8a-f189-44e8-a462-1453a12b4ea3",
  "type": "user",
  "uuid": "aadc68f4-1aa1-4b48-ba40-cf7a80d5a898",
  "toolUseResult": {
    "stdout": "dict\nphase1a_multiseed_qwen: type=dict, keys=['status', 'retry_count', 'created_at', 'updated_at', 'hypothesis', 'spec', 'conclusion', 'notes']\np1_ss_lora_only: type=dict, keys=['status', 'retry_count', 'created_at', 'updated_at', 'hypothesis', 'spec', 'conclusion', 'completed_at']\nphase2_switching: type=dict, keys=['status', 'retry_count', 'created_at', 'updated_at', 'hypothesis', 'conclusion', 'completed_at']\nphase2_tf_ar_switching: type=dict, keys=['status', 'retry_count', 'created_at', 'updated_at', 'hypothesis']\nphase1a_multiseed_8runs: type=dict, keys=['status', 'retry_count', 'created_at', 'updated_at', 'spec']",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "425d60b3-c9c7-46be-bee3-25ee01a5c2d2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "4b680861-4da7-411a-8744-3dabfdaf2205",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 53 · 2026-05-25T20:38:50.334Z_

<details><summary>Logged reasoning block</summary>

```text
Now I know the structure. Let me extract the key experiments that matter for the audit. I'll delegate the heavy registry extraction work to subagents while I also read the table files. Given the complexity, let me use agents to handle parts of this in parallel.

Let me extract the key experiment data I need, and also read the table files.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "aadc68f4-1aa1-4b48-ba40-cf7a80d5a898",
  "isSidechain": false,
  "requestId": "req_011CbPvztMGCMfBBeA1wJrdL",
  "type": "assistant",
  "uuid": "a18fd4c4-69c8-4c9a-8c7c-dc3c4ff25b60",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "4b680861-4da7-411a-8744-3dabfdaf2205",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Tby2jZzgk662QC2VaQ4cSf",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 593,
      "cache_read_input_tokens": 41831,
      "output_tokens": 389,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 593,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 389,
          "cache_read_input_tokens": 41831,
          "cache_creation_input_tokens": 593,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 593
          },
          "type": "message"
        }
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

_source line 54 · 2026-05-25T20:38:51.326Z_

Now I understand the structure. Let me extract all key experiment data and read the table files. I'll use agents to handle the heavy lifting in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a18fd4c4-69c8-4c9a-8c7c-dc3c4ff25b60",
  "isSidechain": false,
  "requestId": "req_011CbPvztMGCMfBBeA1wJrdL",
  "type": "assistant",
  "uuid": "db2b770e-44aa-4575-931b-b3ebfe3693c7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "4b680861-4da7-411a-8744-3dabfdaf2205",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Tby2jZzgk662QC2VaQ4cSf",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 593,
      "cache_read_input_tokens": 41831,
      "output_tokens": 389,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 593,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 389,
          "cache_read_input_tokens": 41831,
          "cache_creation_input_tokens": 593,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 593
          },
          "type": "message"
        }
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

_source line 55 · 2026-05-25T20:38:53.894Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01UV9RHJAGKtkfDn7a5N37oD`</summary>

```json
{
  "command": "REGISTRY=/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-11-projects-turn-residual-gating/4b680861-4da7-411a-8744-3dabfdaf2205/tool-results/mcp-agent-ml-research-read_registry-1779741484333.txt\npython3 -c \"\nimport json, sys\n\ndata = json.load(open('$REGISTRY'))\nresult = json.loads(data['result'])\nexperiments = result['data']['experiments']\n\n# List all experiment IDs\nfor eid in sorted(experiments.keys()):\n    exp = experiments[eid]\n    status = exp.get('status', '?')\n    print(f'{eid}: {status}')\n\" 2>&1",
  "description": "List all experiment IDs and statuses"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "db2b770e-44aa-4575-931b-b3ebfe3693c7",
  "isSidechain": false,
  "requestId": "req_011CbPvztMGCMfBBeA1wJrdL",
  "type": "assistant",
  "uuid": "226bb904-0544-47d8-9f61-6d875091c479",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "4b680861-4da7-411a-8744-3dabfdaf2205",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Tby2jZzgk662QC2VaQ4cSf",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 593,
      "cache_read_input_tokens": 41831,
      "output_tokens": 389,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 593,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 389,
          "cache_read_input_tokens": 41831,
          "cache_creation_input_tokens": 593,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 593
          },
          "type": "message"
        }
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

_source line 56 · 2026-05-25T20:38:53.975Z_

<details><summary>↩ Tool result · `toolu_01UV9RHJAGKtkfDn7a5N37oD`</summary>

```text
analysis_attention_heatmap: DONE
analysis_gradient_conflict: DONE
attention_steering_eval200_tf: DONE
attention_steering_gen_n50: DONE
attention_steering_v7_tg_gen: DONE
d048_eval_ss_s123: DONE
d048_eval_ss_s42: DONE
d048_eval_ss_s456: DONE
d048_final_ar_eval: DONE
d048_queue_runner: PREPARING
d048_split_softmax_eval: DONE
d048_ss_s123: DONE
d048_ss_s42: DONE
d048_ss_s42_resume: PREPARING
d048_ss_s456: DONE
eval_llama_ar_n20: DONE
eval_llama_lora_only_s42: DONE
eval_v7_tg_s123: DONE
eval_v8b_ss: DONE
eval_v8b_ss_s123: DONE
instruction_retention_test: DONE
llama_ar_matched_eval: DONE
llama_eval_s42: DONE
llama_lora_only_s42: DONE
llama_phase1_gar_diag: DONE
llama_tg_s42: DONE
llama_tg_training: PREPARING
mmlu_eval_all: DONE
p0_ss_steering_eval: PREPARING
p1_llama_ss_eval: DONE
p1_llama_ss_training: DONE
p1_ss_lora_only: DONE
p1_tf_ar_kl_divergence: DONE
p2_llama_gradient_conflict: DONE
phase1_gar_diag: DONE
phase1a_multiseed_8runs: PREPARING
phase1a_multiseed_qwen: DONE
phase1b_llama_complement: PREPARING
phase2_4way_eval: DONE
phase2_4way_eval_heldout: DONE
phase2_lora_only_s42: DONE
phase2_switching: DONE
phase2_tf_ar_switching: QUEUED
phase2_tg_s42: DONE
phase2_tg_s42_v2: DONE
phase2_tg_s42_v3: DONE
phase2_tg_s42_v3b: DONE
phase2_tg_s42_v4: DONE
phase2_tg_s42_v5: DONE
phase2_tg_s42_v6: DONE
phase2_tg_s42_v7: DONE
phase2_tg_s42_v8_schedsampling: DONE
phase2_tg_s42_v8b_resume: DONE
phase2_tg_s42_v8b_ss_fixed: DONE
phase2_tg_s42_v9_pcgrad: DONE
phase2_ug_s42: DONE
qwen15b_phase1_diag: DONE
trc_baseline_v7_tg: DONE
v7_tg_s123: DONE
v8b_ss_s123: DONE
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "226bb904-0544-47d8-9f61-6d875091c479",
  "isSidechain": false,
  "promptId": "8817af8a-f189-44e8-a462-1453a12b4ea3",
  "type": "user",
  "uuid": "531e273e-912b-4851-bb24-37fced1b1b31",
  "toolUseResult": {
    "stdout": "analysis_attention_heatmap: DONE\nanalysis_gradient_conflict: DONE\nattention_steering_eval200_tf: DONE\nattention_steering_gen_n50: DONE\nattention_steering_v7_tg_gen: DONE\nd048_eval_ss_s123: DONE\nd048_eval_ss_s42: DONE\nd048_eval_ss_s456: DONE\nd048_final_ar_eval: DONE\nd048_queue_runner: PREPARING\nd048_split_softmax_eval: DONE\nd048_ss_s123: DONE\nd048_ss_s42: DONE\nd048_ss_s42_resume: PREPARING\nd048_ss_s456: DONE\neval_llama_ar_n20: DONE\neval_llama_lora_only_s42: DONE\neval_v7_tg_s123: DONE\neval_v8b_ss: DONE\neval_v8b_ss_s123: DONE\ninstruction_retention_test: DONE\nllama_ar_matched_eval: DONE\nllama_eval_s42: DONE\nllama_lora_only_s42: DONE\nllama_phase1_gar_diag: DONE\nllama_tg_s42: DONE\nllama_tg_training: PREPARING\nmmlu_eval_all: DONE\np0_ss_steering_eval: PREPARING\np1_llama_ss_eval: DONE\np1_llama_ss_training: DONE\np1_ss_lora_only: DONE\np1_tf_ar_kl_divergence: DONE\np2_llama_gradient_conflict: DONE\nphase1_gar_diag: DONE\nphase1a_multiseed_8runs: PREPARING\nphase1a_multiseed_qwen: DONE\nphase1b_llama_complement: PREPARING\nphase2_4way_eval: DONE\nphase2_4way_eval_heldout: DONE\nphase2_lora_only_s42: DONE\nphase2_switching: DONE\nphase2_tf_ar_switching: QUEUED\nphase2_tg_s42: DONE\nphase2_tg_s42_v2: DONE\nphase2_tg_s42_v3: DONE\nphase2_tg_s42_v3b: DONE\nphase2_tg_s42_v4: DONE\nphase2_tg_s42_v5: DONE\nphase2_tg_s42_v6: DONE\nphase2_tg_s42_v7: DONE\nphase2_tg_s42_v8_schedsampling: DONE\nphase2_tg_s42_v8b_resume: DONE\nphase2_tg_s42_v8b_ss_fixed: DONE\nphase2_tg_s42_v9_pcgrad: DONE\nphase2_ug_s42: DONE\nqwen15b_phase1_diag: DONE\ntrc_baseline_v7_tg: DONE\nv7_tg_s123: DONE\nv8b_ss_s123: DONE",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "226bb904-0544-47d8-9f61-6d875091c479",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "4b680861-4da7-411a-8744-3dabfdaf2205",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Runtime record

_source line 57 · 2026-05-25T20:38:53.977Z_

```json
{
  "parentUuid": "531e273e-912b-4851-bb24-37fced1b1b31",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "0aa907e3-d64f-4ba2-b611-9e5d7bd4ba9a",
  "timestamp": "2026-05-25T20:38:53.977Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "4b680861-4da7-411a-8744-3dabfdaf2205",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

---

### Runtime record

_source line 58_

```json
{
  "type": "last-prompt",
  "leafUuid": "0aa907e3-d64f-4ba2-b611-9e5d7bd4ba9a",
  "sessionId": "4b680861-4da7-411a-8744-3dabfdaf2205"
}
```

---

### Runtime record

_source line 59_

```json
{
  "type": "ai-title",
  "aiTitle": "Audit quantitative claims in paper body text",
  "sessionId": "4b680861-4da7-411a-8744-3dabfdaf2205"
}
```

---

### Assistant

_source line 60 · 2026-05-25T20:38:57.589Z_

Good, 60 experiments. Now let me extract the detailed metrics from the key experiments and read the table files. I'll use multiple agents in parallel to handle different sections of the audit.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0aa907e3-d64f-4ba2-b611-9e5d7bd4ba9a",
  "isSidechain": false,
  "requestId": "req_011CbPw1VJCt8Coz7Bwb8RC8",
  "type": "assistant",
  "uuid": "57e7f29e-3aae-416a-862a-65b5778c3d3e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "4b680861-4da7-411a-8744-3dabfdaf2205",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DxKapJ1xPpdDuM87j4j46n",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1294,
      "cache_read_input_tokens": 42424,
      "output_tokens": 1094,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1294,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1094,
          "cache_read_input_tokens": 42424,
          "cache_creation_input_tokens": 1294,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1294
          },
          "type": "message"
        }
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

_source line 61 · 2026-05-25T20:39:13.106Z_

<details open><summary>🔧 Tool call — Bash · `toolu_017qpWF6LY1gdAmFzNo6fKbu`</summary>

```json
{
  "command": "REGISTRY=/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-11-projects-turn-residual-gating/4b680861-4da7-411a-8744-3dabfdaf2205/tool-results/mcp-agent-ml-research-read_registry-1779741484333.txt\npython3 << 'PYEOF'\nimport json\n\ndata = json.load(open(\"$REGISTRY\"))\nresult = json.loads(data['result'])\nexperiments = result['data']['experiments']\n\n# Key experiments for the audit\nkey_ids = [\n    'd048_final_ar_eval', 'phase2_4way_eval_heldout', 'phase2_4way_eval',\n    'phase2_tg_s42_v7', 'phase2_tg_s42_v9_pcgrad', 'phase2_ug_s42',\n    'mmlu_eval_all', 'instruction_retention_test', 'tab_statistical_tests',\n    'p1_llama_ss_eval', 'p2_llama_gradient_conflict', 'trc_baseline_v7_tg',\n    'eval_llama_ar_n20', 'llama_eval_s42', 'phase2_lora_only_s42',\n    'attention_steering_gen_n50', 'attention_steering_v7_tg_gen',\n    'd048_eval_ss_s42', 'd048_eval_ss_s123', 'd048_eval_ss_s456',\n    'eval_v7_tg_s123', 'analysis_gradient_conflict', 'analysis_attention_heatmap',\n    'qwen15b_phase1_diag', 'phase1_gar_diag', 'p1_tf_ar_kl_divergence',\n    'llama_ar_matched_eval', 'eval_v8b_ss', 'eval_v8b_ss_s123',\n    'phase2_tg_s42_v8b_ss_fixed', 'phase2_tg_s42_v8_schedsampling',\n    'v7_tg_s123', 'd048_ss_s42', 'd048_ss_s123', 'd048_ss_s456',\n    'llama_tg_s42', 'llama_lora_only_s42', 'eval_llama_lora_only_s42',\n    'gradient_analysis',  # not in list but might exist as alias\n    'attention_steering_eval200_tf', 'd048_split_softmax_eval',\n    'p1_llama_ss_training', 'p1_ss_lora_only',\n]\n\nfor eid in key_ids:\n    if eid in experiments:\n        exp = experiments[eid]\n        print(f\"\\n{'='*80}\")\n        print(f\"EXP_ID: {eid}\")\n        print(f\"STATUS: {exp.get('status', '?')}\")\n        if 'conclusion' in exp and exp['conclusion']:\n            print(f\"CONCLUSION: {json.dumps(exp['conclusion'], indent=2)[:2000]}\")\n        if 'notes' in exp and exp['notes']:\n            print(f\"NOTES: {json.dumps(exp['notes'], indent=2)[:1500]}\")\n        if 'spec' in exp and exp['spec']:\n            spec = exp['spec']\n            if isinstance(spec, dict):\n                # Print relevant spec keys\n                for k in ['metrics', 'results', 'data', 'hyperparams', 'config']:\n                    if k in spec:\n                        print(f\"SPEC.{k}: {json.dumps(spec[k], indent=2)[:1000]}\")\n    else:\n        print(f\"\\n--- {eid}: NOT FOUND ---\")\n\nPYEOF\n",
  "description": "Extract key experiment data from registry",
  "timeout": 30000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "57e7f29e-3aae-416a-862a-65b5778c3d3e",
  "isSidechain": false,
  "requestId": "req_011CbPw1VJCt8Coz7Bwb8RC8",
  "type": "assistant",
  "uuid": "4e600281-425a-463d-b730-ecc1ac8f0a05",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "4b680861-4da7-411a-8744-3dabfdaf2205",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DxKapJ1xPpdDuM87j4j46n",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1294,
      "cache_read_input_tokens": 42424,
      "output_tokens": 1094,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1294,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1094,
          "cache_read_input_tokens": 42424,
          "cache_creation_input_tokens": 1294,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1294
          },
          "type": "message"
        }
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

_source line 62 · 2026-05-25T20:39:13.320Z_

<details><summary>↩ Tool result · reported error · `toolu_017qpWF6LY1gdAmFzNo6fKbu`</summary>

```text
Exit code 1
Traceback (most recent call last):
  File "&lt;stdin>", line 3, in &lt;module>
FileNotFoundError: [Errno 2] No such file or directory: '$REGISTRY'
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4e600281-425a-463d-b730-ecc1ac8f0a05",
  "isSidechain": false,
  "promptId": "8817af8a-f189-44e8-a462-1453a12b4ea3",
  "type": "user",
  "uuid": "fffbbe04-68d5-4fda-a10c-bae51f49e15b",
  "toolUseResult": "Error: Exit code 1\nTraceback (most recent call last):\n  File \"&lt;stdin>\", line 3, in &lt;module>\nFileNotFoundError: [Errno 2] No such file or directory: '$REGISTRY'",
  "sourceToolAssistantUUID": "4e600281-425a-463d-b730-ecc1ac8f0a05",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "4b680861-4da7-411a-8744-3dabfdaf2205",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 63 · 2026-05-25T20:39:25.183Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01TbnQGPwDtwyNBJcGf64fXU`</summary>

```json
{
  "command": "python3 << 'PYEOF'\nimport json\n\nREGISTRY = \"/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-11-projects-turn-residual-gating/4b680861-4da7-411a-8744-3dabfdaf2205/tool-results/mcp-agent-ml-research-read_registry-1779741484333.txt\"\ndata = json.load(open(REGISTRY))\nresult = json.loads(data['result'])\nexperiments = result['data']['experiments']\n\nkey_ids = [\n    'd048_final_ar_eval', 'phase2_4way_eval_heldout', 'phase2_4way_eval',\n    'phase2_tg_s42_v7', 'phase2_tg_s42_v9_pcgrad', 'phase2_ug_s42',\n    'mmlu_eval_all', 'instruction_retention_test',\n    'p1_llama_ss_eval', 'p2_llama_gradient_conflict', 'trc_baseline_v7_tg',\n    'eval_llama_ar_n20', 'llama_eval_s42', 'phase2_lora_only_s42',\n    'attention_steering_gen_n50', 'attention_steering_v7_tg_gen',\n    'd048_eval_ss_s42', 'd048_eval_ss_s123', 'd048_eval_ss_s456',\n    'eval_v7_tg_s123', 'analysis_gradient_conflict', 'analysis_attention_heatmap',\n    'qwen15b_phase1_diag', 'phase1_gar_diag', 'p1_tf_ar_kl_divergence',\n    'eval_v8b_ss', 'eval_v8b_ss_s123',\n    'phase2_tg_s42_v8b_ss_fixed', 'phase2_tg_s42_v8_schedsampling',\n    'v7_tg_s123', 'd048_ss_s42', 'd048_ss_s123', 'd048_ss_s456',\n    'llama_tg_s42', 'llama_lora_only_s42', 'eval_llama_lora_only_s42',\n    'attention_steering_eval200_tf', 'd048_split_softmax_eval',\n    'p1_llama_ss_training', 'p1_ss_lora_only',\n    'llama_ar_matched_eval',\n]\n\nfor eid in key_ids:\n    if eid in experiments:\n        exp = experiments[eid]\n        print(f\"\\n{'='*80}\")\n        print(f\"EXP_ID: {eid}\")\n        print(f\"STATUS: {exp.get('status', '?')}\")\n        conclusion = exp.get('conclusion')\n        if conclusion:\n            print(f\"CONCLUSION: {json.dumps(conclusion, indent=2)[:3000]}\")\n        notes = exp.get('notes')\n        if notes:\n            print(f\"NOTES: {json.dumps(notes, indent=2)[:2000]}\")\n        spec = exp.get('spec')\n        if spec and isinstance(spec, dict):\n            for k in ['metrics', 'results', 'data', 'hyperparams', 'config', 'eval_results', 'model']:\n                if k in spec:\n                    print(f\"SPEC.{k}: {json.dumps(spec[k], indent=2)[:1500]}\")\n    else:\n        print(f\"\\n--- {eid}: NOT FOUND ---\")\nPYEOF\n",
  "description": "Extract key experiment data from registry",
  "timeout": 30000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fffbbe04-68d5-4fda-a10c-bae51f49e15b",
  "isSidechain": false,
  "requestId": "req_011CbPw2vAxLBxM6jYJtEnEv",
  "type": "assistant",
  "uuid": "fb0561d2-966a-4b21-a23b-d033f6625753",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "4b680861-4da7-411a-8744-3dabfdaf2205",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017wmLk8EH2fHZHu33qKY13V",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1165,
      "cache_read_input_tokens": 43718,
      "output_tokens": 1014,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1165,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1014,
          "cache_read_input_tokens": 43718,
          "cache_creation_input_tokens": 1165,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1165
          },
          "type": "message"
        }
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

_source line 64 · 2026-05-25T20:39:25.263Z_

<details><summary>↩ Tool result · `toolu_01TbnQGPwDtwyNBJcGf64fXU`</summary>

```text
================================================================================
EXP_ID: d048_final_ar_eval
STATUS: DONE
CONCLUSION: "success"

================================================================================
EXP_ID: phase2_4way_eval_heldout
STATUS: DONE
CONCLUSION: "success"
NOTES: "Held-out eval \u4e09\u8def\u8d8b\u540c\u5b8c\u5168\u590d\u73b0\u3002TG/UG/LoRA-only GAR-ours: 0.504/0.505/0.498 (spread 0.75pp), PPL \u5747\u4e3a 2.78\u3002\u4e0e overlap \u6570\u636e\u76f8\u6bd4\u7edd\u5bf9\u503c\u7565\u9ad8\uff08GAR +1-2pp, PPL +0.15\uff09\uff0c\u5c5e\u6b63\u5e38\u6cdb\u5316\u504f\u79fb\uff0c\u76f8\u5bf9\u6bd4\u8f83\u5b8c\u5168\u4e00\u81f4\u3002\u6570\u636e\u5b8c\u6574\u6027 confound \u5df2\u6392\u9664\u3002"

================================================================================
EXP_ID: phase2_4way_eval
STATUS: DONE
CONCLUSION: "negative"
NOTES: "\u56db\u8def eval \u5b8c\u6210\uff0cRoute B \u51b3\u5b9a\u6027\u786e\u8ba4\u3002\u4e09\u79cd\u8bad\u7ec3\u65b9\u6cd5\uff08TG/UG/LoRA-only\uff09\u5728\u63a8\u7406\u7aef\u5b8c\u5168\u8d8b\u540c\uff1aours GAR recovery ~47-48pp\uff08vs base -0.15pp\uff09\uff0cdongre GAR recovery 0.08-0.35pp\uff0cPPL 2.62-2.63\uff0cNTP 0.943-0.948\u3002Gating \u673a\u5236\uff08\u65e0\u8bba turn-conditioned \u8fd8\u662f uniform\uff09\u76f8\u6bd4\u7eaf LoRA \u5fae\u8c03\u96f6\u589e\u91cf\u3002LoRA fine-tuning \u662f GAR recovery \u7684\u552f\u4e00\u6765\u6e90\u3002hypothesis \u88ab\u8bc1\u4f2a\uff1aTRG \u4e0d\u6bd4 LoRA-only \u66f4\u597d\u3002"

================================================================================
EXP_ID: phase2_tg_s42_v7
STATUS: DONE
CONCLUSION: "success"
NOTES: "\u8bad\u7ec3 3 epoch \u5b8c\u6210 (21352s/5.9h)\u3002\u6700\u7ec8 gate: mean=0.9336, std=0.0492, L3=0.801 L4=0.789 \u6700\u4f4e\u3002Eval \u5b8c\u6210\uff1aGAR-ours recovery +0.35pp (mid 0.0157 vs baseline 0.0122), GAR-Dongre recovery +0.72pp (mid 0.0194 vs baseline 0.0122)\u3002Gate dynamic range \u6700\u5927\u5c42: L23 diff=-0.2100, L14 diff=-0.1803\u3002"

================================================================================
EXP_ID: phase2_tg_s42_v9_pcgrad
STATUS: DONE
CONCLUSION: "success"
NOTES: "D028 \u56e0\u679c\u6392\u9664\u786e\u8ba4\uff08M017 \u4fee\u6b63\u540e\uff09\u3002\u8bad\u7ec3: EXIT_CODE=0, 7.98h, 3 epochs\u3002PCGrad cos_sim \u4ece -0.061\u2192+0.055\u2192-0.035 (\u56f4\u7ed5 0 \u632f\u8361), NTP mag_ratio 2.8\u219228.8 \u6301\u7eed\u589e\u957f\u3002L_GAR \u6709 0-350 step \u9ad8\u539f\u671f\u540e\u4ecd\u574d\u584c\u5230\u22480\u3002IID eval (\u540c protocol 50 heldout convs): GAR-ours=0.5002 (vs v7 0.5035, diff -0.33pp), GAR-Dongre=0.0123 (vs v7 0.0152), PPL=2.780 (vs v7 2.784, diff 0.004, \u65e0\u6539\u5584)\u3002Model-gen eval (5 convs): GAR-ours=0.0151, PPL=1.50\u3002\u7ed3\u8bba: PCGrad \u6d88\u9664\u68af\u5ea6\u65b9\u5411\u51b2\u7a81\u540e\u6240\u6709 IID \u6307\u6807\u5747 \u2248 v7\uff08GAR\u3001PPL\u3001NTP \u65e0\u53d8\u5316\uff09\uff0c\u65b9\u5411\u51b2\u7a81\u56e0 NTP \u5e45\u5ea6\u4e3b\u5bfc (10-40x) \u800c inconsequential\u3002Exposure bias \u662f 30x gap \u6839\u56e0\u3002"

================================================================================
EXP_ID: phase2_ug_s42
STATUS: DONE
CONCLUSION: "success"
NOTES: "3 epoch \u5b8c\u6210 (21994.5s/6.1h)\u3002\u6700\u7ec8 gate: mean=0.9598, std=0.0518, L3=0.777 L5=0.812 \u6700\u4f4e\u3002\u91cd\u8981\u53d1\u73b0\uff1auniform gate \u6a21\u5f0f\u4e0b\u5404\u5c42\u4ecd\u5b66\u51fa per-layer \u5206\u5316\uff08L3=0.777 vs L27=1.000\uff09\uff0c\u4e0e ThreadGate v7 \u7684 L3/L4 \u6700\u4f4e\u6a21\u5f0f\u4e00\u81f4\u3002\u8fd9\u8bf4\u660e per-layer variation \u53ef\u80fd\u6765\u81ea LoRA+GAR loss \u800c\u975e gate architecture\u3002"

================================================================================
EXP_ID: mmlu_eval_all
STATUS: DONE
CONCLUSION: "success"

================================================================================
EXP_ID: instruction_retention_test
STATUS: DONE
CONCLUSION: "success"

================================================================================
EXP_ID: p1_llama_ss_eval
STATUS: DONE
CONCLUSION: "success"

================================================================================
EXP_ID: p2_llama_gradient_conflict
STATUS: DONE
CONCLUSION: "success"

================================================================================
EXP_ID: trc_baseline_v7_tg
STATUS: DONE
CONCLUSION: "success"
NOTES: "Cross-space \u9a8c\u8bc1\uff1aexposure bias \u662f attention-specific\u3002v7 TG: TRC gap = +0.002 (\u8fd1\u96f6)\uff0chidden state \u4e00\u81f4\u6027\u5728 TF/gen \u4e4b\u95f4\u65e0\u5dee\u5f02\u3002\u5bf9\u6bd4 GAR \u7684 30x gap\uff0cTRC \u65e0 gap \u2192 exposure bias \u53ea\u626d\u66f2 attention \u5206\u5e03\uff0c\u4e0d\u5f71\u54cd hidden state \u5c42\u9762\u3002LoRA-only: \u53cd\u8f6c gap (-0.062)\uff0cgen TRC \u66f4\u9ad8\u4f46 TBP PPL \u4e25\u91cd\u6076\u5316 (9.5\u219212.0)\u2014\u2014hidden states \"\u574d\u7f29\"\u8d8b\u540c\u4f46\u4fe1\u606f\u91cf\u4e0b\u964d\u3002Base: \u96f6 gap\uff08\u4f46\u53ef\u80fd\u6709 eval \u811a\u672c bug\uff0cgen \u6a21\u5f0f\u590d\u7528\u4e86 TF hidden states\uff09\u3002"

================================================================================
EXP_ID: eval_llama_ar_n20
STATUS: DONE
CONCLUSION: "success"
NOTES: "N=20 AR eval stabilizes estimates. **mid_turns = turns 3-T (0-indexed avg_gar[2:], excluding turns 1-2; all 16 eval entries use same definition)**. Two median levels: median_per_conv (paper \u00a75.5 cites this: TG 0.0179, LO 0.0184, Base 0.0093) = median of 20 per-conversation mid-turn averages; median_per_turn_pool (TG 0.0126, LO 0.0133, Base 0.0071) = median of 40 pooled individual turns. Both confirm TG \u2248 LO (zero-increment). Mean (TG 0.0434 > LO 0.0284) driven by outlier spikes (TG std=0.1002, 5% turns GAR\u22650.4; LO std=0.0481, 0% spikes). PPL: Base(1.29) < LO(1.42) < TG(1.44). Pending paper fix: \u00a75.5 says \"turns 2-T\" but code excludes turns 1-2; will correct to \"excluding the first two turns\" in next paper edit batch."

================================================================================
EXP_ID: llama_eval_s42
STATUS: DONE
CONCLUSION: "success"
NOTES: "C5 \u8de8\u6a21\u578b\u6cdb\u5316\u786e\u8ba4\u3002Llama TG GAR-ours gap 16x (TF 0.484 vs AR 0.030)\uff0c\u4f4e\u4e8e Qwen v7 \u7684 32x \u4f46\u4ecd\u975e\u5e38\u663e\u8457\u3002Base model gap \u4ec5 1.9x\uff08control \u901a\u8fc7\uff09\u3002\u6ce8\u610f TF/AR eval \u8bbe\u5b9a\u4e0d\u540c (N=50/T=4 vs N=5/T=10)\uff0c\u53ef\u80fd\u5f71\u54cd\u7edd\u5bf9\u503c\u5bf9\u6bd4\u3002GAR-dongre \u65e0\u660e\u663e gap (ratio 0.83x, AR \u2265 TF)\uff0c\u4ec5 GAR-ours \u5c55\u73b0 exposure bias \u6548\u5e94\u3002Gate dynamic range: L24/L28/L30 diff \u6700\u5927 (0.23-0.38)\uff0c\u4e0e Qwen \u7c7b\u4f3c\u96c6\u4e2d\u5728\u4e2d\u9ad8\u5c42\u3002"

================================================================================
EXP_ID: phase2_lora_only_s42
STATUS: DONE
CONCLUSION: "success"
NOTES: "\u8bca\u65ad\u786e\u8ba4\uff1aEXIT_CODE=1 \u56e0 argparse \u4e0d\u8ba4 lora_only \u9009\u9879\uff08choices \u53ea\u6709 threadgate/uniform/none\uff09\u3002\u8bad\u7ec3\u5b9e\u9645\u5df2\u7528 --gate-type none \u5b8c\u6210 3 epoch (3000 steps, 20588.6s/5.7h)\u3002Gate \u5168\u7a0b\u56fa\u5b9a 1.0\uff08\u7b26\u5408 lora_only \u8bed\u4e49\uff09\u3002Checkpoint \u53ef\u7528\uff0c\u65e0\u9700\u91cd\u8dd1\u3002\u4fee\u590d\uff1adispatch \u547d\u4ee4\u6539\u7528 --gate-type none \u6216\u5728 train_phase2.py \u6dfb\u52a0 lora_only choice\u3002"

================================================================================
EXP_ID: attention_steering_gen_n50
STATUS: DONE
CONCLUSION: "success"
NOTES: "\u539f\u59cb\u805a\u5408\u6709 min_turns \u622a\u65ad bug\uff08\u622a\u5230 2 turns\uff09\uff0c\u4fee\u6b63\u540e\u7528 per-conv mid_gar(turns 2-7)\u300239/50 \u5bf9\u8bdd\u6709 \u22653 turns \u53c2\u4e0e\u7edf\u8ba1\u3002\u4fee\u6b63\u540e baseline \u03b2=0 GAR \u4ece 0.101 \u964d\u5230 0.064\uff08median 0.031 \u4e0e N=5 \u7684 0.028 \u4e00\u81f4\uff09\u3002Phase transition \u5728 \u03b2\u2208[2,3] \u91cd\u73b0\u3002\u03b2=10 corrected 0.961 \u2248 N=5 \u7684 0.959\u3002"

================================================================================
EXP_ID: attention_steering_v7_tg_gen
STATUS: DONE
CONCLUSION: "success"
NOTES: "Attention steering \u95ed\u5408\u56e0\u679c\u73af\u3002\u03b2=0\u21922: GAR \u7f13\u5347 (0.028\u21920.062), PPL \u4e0d\u53d8 (~1.4); \u03b2=5: phase transition, GAR \u8df3\u81f3 0.68, PPL \u5347\u81f3 1.91; \u03b2=10: GAR \u9971\u548c 0.96, PPL \u6076\u5316 4.22\u3002\u6210\u529f\u6807\u51c6 (GAR>0.1 \u4e14 PPL \u4e0d\u4e25\u91cd\u6076\u5316) \u5728 \u03b2=2 \u5373\u6ee1\u8db3\u3002\u03b2\u2208[2,5] \u5b58\u5728 phase transition\u3002\u8bc1\u660e\uff1a\u624b\u52a8\u4fee\u6b63 attention \u6307\u5411 goal tokens \u2192 \u76f4\u63a5\u6062\u590d GAR \u2192 \u786e\u8ba4 exposure bias \u901a\u8fc7 attention \u504f\u79fb\u5bfc\u81f4 GAR \u574d\u584c\u3002"

================================================================================
EXP_ID: d048_eval_ss_s42
STATUS: DONE
CONCLUSION: "success"

================================================================================
EXP_ID: d048_eval_ss_s123
STATUS: DONE
CONCLUSION: "success"
NOTES: "Cron\u8bef\u5224\u4fee\u590d: \u539fPID 109385\u662fTF eval\u5b50\u8fdb\u7a0b,\u9000\u51fa\u540ecron 5\u6b21\u68c0\u6d4b\u5931\u8d25auto-resolved\u4e3afailed\u3002\u5b9e\u9645AR eval PID 110052\u4ecd\u5728\u8fd0\u884c\u3002\u5df2\u624b\u52a8\u6062\u590dRUNNING\u3002"

================================================================================
EXP_ID: d048_eval_ss_s456
STATUS: DONE
CONCLUSION: "success"

================================================================================
EXP_ID: eval_v7_tg_s123
STATUS: DONE
CONCLUSION: "success"

================================================================================
EXP_ID: analysis_gradient_conflict
STATUS: DONE
CONCLUSION: "success"

================================================================================
EXP_ID: analysis_attention_heatmap
STATUS: DONE
CONCLUSION: "success"

================================================================================
EXP_ID: qwen15b_phase1_diag
STATUS: DONE
CONCLUSION: "success"

================================================================================
EXP_ID: phase1_gar_diag
STATUS: DONE
CONCLUSION: "success"

================================================================================
EXP_ID: p1_tf_ar_kl_divergence
STATUS: DONE
CONCLUSION: "success"

================================================================================
EXP_ID: eval_v8b_ss
STATUS: DONE
CONCLUSION: "success"

================================================================================
EXP_ID: eval_v8b_ss_s123
STATUS: DONE
CONCLUSION: "success"

================================================================================
EXP_ID: phase2_tg_s42_v8b_ss_fixed
STATUS: DONE
CONCLUSION: "failed"
NOTES: "CUDA OOM at Epoch 1 Step 4300 (loss.backward). \u5176\u4ed6\u8fdb\u7a0b\u5171\u4eab GPU \u5bfc\u81f4\u663e\u5b58\u4e0d\u8db3: Process 157667 (26.76GB) + Process 158713 (17.28GB) + PyTorch \u81ea\u8eab 45.21GB + 4.81GB reserved > 94.97GB \u603b\u5bb9\u91cf\u3002\u8bad\u7ec3\u5728 OOM \u524d\u6b63\u5e38\u6536\u655b (SS ratio=0.5, Loss~1.0, Gate~0.94)\u3002\u6709 epoch_0 checkpoint\u3002\u9700\u8981\u72ec\u5360 GPU \u91cd\u8dd1\u3002"

================================================================================
EXP_ID: phase2_tg_s42_v8_schedsampling
STATUS: DONE
CONCLUSION: "failed"
NOTES: "Director kill at micro-step ~1950 (8.1%). \u539f\u56e0: SS path code bug (D026) + GAR-ours \u65e0\u63a8\u7406 gap (D024)\uff0c\u5b9e\u9a8c\u65e0\u6548\u3002GPU \u8f6c\u5165 plan_018 PCGrad\u3002\u8be6\u60c5\uff1a(1) SS ratio \u4ec5 0.081 \u65f6 kill\uff0c\u4ec5 1 \u6761 SS step \u88ab\u65e5\u5fd7\u6355\u83b7\uff0c(2) TF L_GAR \u5728 step 800 \u574d\u584c\u5230 \u22480.006\uff08\u4e0e v7 \u4e00\u81f4\uff09\uff0c(3) GAR-ours \u63a8\u7406\u65f6 \u22480.50 \u2248 target\uff0cSS \u7528 GAR-ours \u8bad\u7ec3\u65e0\u6cd5\u9a8c\u8bc1 exposure bias mitigation\uff0c(4) lambda_gar=2.0 (vs v7 \u7684 1.0) confound \u672a\u88ab\u5145\u5206\u89e6\u53d1\u3002"
SPEC.hyperparams: {
  "lr": 0.0002,
  "epochs": 3,
  "grad_accum": 8,
  "ss_max_ratio": 0.5,
  "ss_gen_max_tokens": 256,
  "ss_gen_temperature": 0.7
}

================================================================================
EXP_ID: v7_tg_s123
STATUS: DONE
CONCLUSION: "success"

================================================================================
EXP_ID: d048_ss_s42
STATUS: DONE
CONCLUSION: "success"
NOTES: "Training complete (resume v3). 23418s (6.5h) for epoch 1+2. Final: Avg Loss=0.9326, NTP=0.9320, GAR=0.0007, DIV=0.0000. Gate: mean=0.9527, std=0.0589, min=0.7383(L4), max=1.000. SS: 4750/16000 (29.7%) used, 0 fallback. Checkpoints: epoch_0, epoch_1, epoch_2, final. Gate profile consistent with prior SS runs (L4 lowest)."

================================================================================
EXP_ID: d048_ss_s123
STATUS: DONE
CONCLUSION: "success"

================================================================================
EXP_ID: d048_ss_s456
STATUS: DONE
CONCLUSION: "success"

================================================================================
EXP_ID: llama_tg_s42
STATUS: DONE
CONCLUSION: "success"

================================================================================
EXP_ID: llama_lora_only_s42
STATUS: DONE
CONCLUSION: "success"

================================================================================
EXP_ID: eval_llama_lora_only_s42
STATUS: DONE
CONCLUSION: "success"

================================================================================
EXP_ID: attention_steering_eval200_tf
STATUS: DONE
CONCLUSION: "success"

================================================================================
EXP_ID: d048_split_softmax_eval
STATUS: DONE
CONCLUSION: "failed"
NOTES: "2 critical bugs: (1) system_prompt_len=0 hardcoded at L373, (2) gen mode NaN for k\u22601.0. Director decision 2026-05-23: not urgent, defer fix past DDL 5/25. Does not affect main paper experiments."

================================================================================
EXP_ID: p1_llama_ss_training
STATUS: DONE
CONCLUSION: "success"
SPEC.hyperparams: {
  "lr": "2e-4",
  "batch_size": 1,
  "grad_accum": 8,
  "epochs": 3,
  "ss_max_ratio": 0.3,
  "lora_rank": 16
}

================================================================================
EXP_ID: p1_ss_lora_only
STATUS: DONE
CONCLUSION: "killed"

================================================================================
EXP_ID: llama_ar_matched_eval
STATUS: DONE
CONCLUSION: "success"
NOTES: "CORRECTION (2026-05-21 04:36): Agent \u4e4b\u524d\u9519\u8bef\u5730\u5c06 AR TG nGAR (0.493) \u4e0e TF TG raw GAR (0.484) \u5bf9\u6bd4\uff0c\u8bef\u5224\u4e3a 'nGAR aligns, gap is normalization artifact'\u3002Reviewer \u6838\u5b9e\uff1aTF TG ours nGAR = 11.88\uff08\u975e 0.48\uff09\u3002nGAR gap = 11.88 / 0.493 = 24.1\u00d7\uff0c\u6bd4 raw gap (12.5\u00d7) \u8fd8\u5927\u3002'Normalization artifact' \u5206\u6790\u5b8c\u5168\u9519\u8bef\u2014\u2014GAR-ours \u7684 gap \u662f\u771f\u5b9e\u7684 exposure bias\u3002\u8bba\u6587\u7edd\u5bf9\u4e0d\u80fd\u4f7f\u7528 normalization artifact \u53d9\u4e8b\u3002"
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fb0561d2-966a-4b21-a23b-d033f6625753",
  "isSidechain": false,
  "promptId": "8817af8a-f189-44e8-a462-1453a12b4ea3",
  "type": "user",
  "uuid": "fa5dbb1b-cb41-43f0-87ca-4da0387c1ced",
  "toolUseResult": {
    "stdout": "================================================================================\nEXP_ID: d048_final_ar_eval\nSTATUS: DONE\nCONCLUSION: \"success\"\n\n================================================================================\nEXP_ID: phase2_4way_eval_heldout\nSTATUS: DONE\nCONCLUSION: \"success\"\nNOTES: \"Held-out eval \\u4e09\\u8def\\u8d8b\\u540c\\u5b8c\\u5168\\u590d\\u73b0\\u3002TG/UG/LoRA-only GAR-ours: 0.504/0.505/0.498 (spread 0.75pp), PPL \\u5747\\u4e3a 2.78\\u3002\\u4e0e overlap \\u6570\\u636e\\u76f8\\u6bd4\\u7edd\\u5bf9\\u503c\\u7565\\u9ad8\\uff08GAR +1-2pp, PPL +0.15\\uff09\\uff0c\\u5c5e\\u6b63\\u5e38\\u6cdb\\u5316\\u504f\\u79fb\\uff0c\\u76f8\\u5bf9\\u6bd4\\u8f83\\u5b8c\\u5168\\u4e00\\u81f4\\u3002\\u6570\\u636e\\u5b8c\\u6574\\u6027 confound \\u5df2\\u6392\\u9664\\u3002\"\n\n================================================================================\nEXP_ID: phase2_4way_eval\nSTATUS: DONE\nCONCLUSION: \"negative\"\nNOTES: \"\\u56db\\u8def eval \\u5b8c\\u6210\\uff0cRoute B \\u51b3\\u5b9a\\u6027\\u786e\\u8ba4\\u3002\\u4e09\\u79cd\\u8bad\\u7ec3\\u65b9\\u6cd5\\uff08TG/UG/LoRA-only\\uff09\\u5728\\u63a8\\u7406\\u7aef\\u5b8c\\u5168\\u8d8b\\u540c\\uff1aours GAR recovery ~47-48pp\\uff08vs base -0.15pp\\uff09\\uff0cdongre GAR recovery 0.08-0.35pp\\uff0cPPL 2.62-2.63\\uff0cNTP 0.943-0.948\\u3002Gating \\u673a\\u5236\\uff08\\u65e0\\u8bba turn-conditioned \\u8fd8\\u662f uniform\\uff09\\u76f8\\u6bd4\\u7eaf LoRA \\u5fae\\u8c03\\u96f6\\u589e\\u91cf\\u3002LoRA fine-tuning \\u662f GAR recovery \\u7684\\u552f\\u4e00\\u6765\\u6e90\\u3002hypothesis \\u88ab\\u8bc1\\u4f2a\\uff1aTRG \\u4e0d\\u6bd4 LoRA-only \\u66f4\\u597d\\u3002\"\n\n================================================================================\nEXP_ID: phase2_tg_s42_v7\nSTATUS: DONE\nCONCLUSION: \"success\"\nNOTES: \"\\u8bad\\u7ec3 3 epoch \\u5b8c\\u6210 (21352s/5.9h)\\u3002\\u6700\\u7ec8 gate: mean=0.9336, std=0.0492, L3=0.801 L4=0.789 \\u6700\\u4f4e\\u3002Eval \\u5b8c\\u6210\\uff1aGAR-ours recovery +0.35pp (mid 0.0157 vs baseline 0.0122), GAR-Dongre recovery +0.72pp (mid 0.0194 vs baseline 0.0122)\\u3002Gate dynamic range \\u6700\\u5927\\u5c42: L23 diff=-0.2100, L14 diff=-0.1803\\u3002\"\n\n================================================================================\nEXP_ID: phase2_tg_s42_v9_pcgrad\nSTATUS: DONE\nCONCLUSION: \"success\"\nNOTES: \"D028 \\u56e0\\u679c\\u6392\\u9664\\u786e\\u8ba4\\uff08M017 \\u4fee\\u6b63\\u540e\\uff09\\u3002\\u8bad\\u7ec3: EXIT_CODE=0, 7.98h, 3 epochs\\u3002PCGrad cos_sim \\u4ece -0.061\\u2192+0.055\\u2192-0.035 (\\u56f4\\u7ed5 0 \\u632f\\u8361), NTP mag_ratio 2.8\\u219228.8 \\u6301\\u7eed\\u589e\\u957f\\u3002L_GAR \\u6709 0-350 step \\u9ad8\\u539f\\u671f\\u540e\\u4ecd\\u574d\\u584c\\u5230\\u22480\\u3002IID eval (\\u540c protocol 50 heldout convs): GAR-ours=0.5002 (vs v7 0.5035, diff -0.33pp), GAR-Dongre=0.0123 (vs v7 0.0152), PPL=2.780 (vs v7 2.784, diff 0.004, \\u65e0\\u6539\\u5584)\\u3002Model-gen eval (5 convs): GAR-ours=0.0151, PPL=1.50\\u3002\\u7ed3\\u8bba: PCGrad \\u6d88\\u9664\\u68af\\u5ea6\\u65b9\\u5411\\u51b2\\u7a81\\u540e\\u6240\\u6709 IID \\u6307\\u6807\\u5747 \\u2248 v7\\uff08GAR\\u3001PPL\\u3001NTP \\u65e0\\u53d8\\u5316\\uff09\\uff0c\\u65b9\\u5411\\u51b2\\u7a81\\u56e0 NTP \\u5e45\\u5ea6\\u4e3b\\u5bfc (10-40x) \\u800c inconsequential\\u3002Exposure bias \\u662f 30x gap \\u6839\\u56e0\\u3002\"\n\n================================================================================\nEXP_ID: phase2_ug_s42\nSTATUS: DONE\nCONCLUSION: \"success\"\nNOTES: \"3 epoch \\u5b8c\\u6210 (21994.5s/6.1h)\\u3002\\u6700\\u7ec8 gate: mean=0.9598, std=0.0518, L3=0.777 L5=0.812 \\u6700\\u4f4e\\u3002\\u91cd\\u8981\\u53d1\\u73b0\\uff1auniform gate \\u6a21\\u5f0f\\u4e0b\\u5404\\u5c42\\u4ecd\\u5b66\\u51fa per-layer \\u5206\\u5316\\uff08L3=0.777 vs L27=1.000\\uff09\\uff0c\\u4e0e ThreadGate v7 \\u7684 L3/L4 \\u6700\\u4f4e\\u6a21\\u5f0f\\u4e00\\u81f4\\u3002\\u8fd9\\u8bf4\\u660e per-layer variation \\u53ef\\u80fd\\u6765\\u81ea LoRA+GAR loss \\u800c\\u975e gate architecture\\u3002\"\n\n================================================================================\nEXP_ID: mmlu_eval_all\nSTATUS: DONE\nCONCLUSION: \"success\"\n\n================================================================================\nEXP_ID: instruction_retention_test\nSTATUS: DONE\nCONCLUSION: \"success\"\n\n================================================================================\nEXP_ID: p1_llama_ss_eval\nSTATUS: DONE\nCONCLUSION: \"success\"\n\n================================================================================\nEXP_ID: p2_llama_gradient_conflict\nSTATUS: DONE\nCONCLUSION: \"success\"\n\n================================================================================\nEXP_ID: trc_baseline_v7_tg\nSTATUS: DONE\nCONCLUSION: \"success\"\nNOTES: \"Cross-space \\u9a8c\\u8bc1\\uff1aexposure bias \\u662f attention-specific\\u3002v7 TG: TRC gap = +0.002 (\\u8fd1\\u96f6)\\uff0chidden state \\u4e00\\u81f4\\u6027\\u5728 TF/gen \\u4e4b\\u95f4\\u65e0\\u5dee\\u5f02\\u3002\\u5bf9\\u6bd4 GAR \\u7684 30x gap\\uff0cTRC \\u65e0 gap \\u2192 exposure bias \\u53ea\\u626d\\u66f2 attention \\u5206\\u5e03\\uff0c\\u4e0d\\u5f71\\u54cd hidden state \\u5c42\\u9762\\u3002LoRA-only: \\u53cd\\u8f6c gap (-0.062)\\uff0cgen TRC \\u66f4\\u9ad8\\u4f46 TBP PPL \\u4e25\\u91cd\\u6076\\u5316 (9.5\\u219212.0)\\u2014\\u2014hidden states \\\"\\u574d\\u7f29\\\"\\u8d8b\\u540c\\u4f46\\u4fe1\\u606f\\u91cf\\u4e0b\\u964d\\u3002Base: \\u96f6 gap\\uff08\\u4f46\\u53ef\\u80fd\\u6709 eval \\u811a\\u672c bug\\uff0cgen \\u6a21\\u5f0f\\u590d\\u7528\\u4e86 TF hidden states\\uff09\\u3002\"\n\n================================================================================\nEXP_ID: eval_llama_ar_n20\nSTATUS: DONE\nCONCLUSION: \"success\"\nNOTES: \"N=20 AR eval stabilizes estimates. **mid_turns = turns 3-T (0-indexed avg_gar[2:], excluding turns 1-2; all 16 eval entries use same definition)**. Two median levels: median_per_conv (paper \\u00a75.5 cites this: TG 0.0179, LO 0.0184, Base 0.0093) = median of 20 per-conversation mid-turn averages; median_per_turn_pool (TG 0.0126, LO 0.0133, Base 0.0071) = median of 40 pooled individual turns. Both confirm TG \\u2248 LO (zero-increment). Mean (TG 0.0434 > LO 0.0284) driven by outlier spikes (TG std=0.1002, 5% turns GAR\\u22650.4; LO std=0.0481, 0% spikes). PPL: Base(1.29) < LO(1.42) < TG(1.44). Pending paper fix: \\u00a75.5 says \\\"turns 2-T\\\" but code excludes turns 1-2; will correct to \\\"excluding the first two turns\\\" in next paper edit batch.\"\n\n================================================================================\nEXP_ID: llama_eval_s42\nSTATUS: DONE\nCONCLUSION: \"success\"\nNOTES: \"C5 \\u8de8\\u6a21\\u578b\\u6cdb\\u5316\\u786e\\u8ba4\\u3002Llama TG GAR-ours gap 16x (TF 0.484 vs AR 0.030)\\uff0c\\u4f4e\\u4e8e Qwen v7 \\u7684 32x \\u4f46\\u4ecd\\u975e\\u5e38\\u663e\\u8457\\u3002Base model gap \\u4ec5 1.9x\\uff08control \\u901a\\u8fc7\\uff09\\u3002\\u6ce8\\u610f TF/AR eval \\u8bbe\\u5b9a\\u4e0d\\u540c (N=50/T=4 vs N=5/T=10)\\uff0c\\u53ef\\u80fd\\u5f71\\u54cd\\u7edd\\u5bf9\\u503c\\u5bf9\\u6bd4\\u3002GAR-dongre \\u65e0\\u660e\\u663e gap (ratio 0.83x, AR \\u2265 TF)\\uff0c\\u4ec5 GAR-ours \\u5c55\\u73b0 exposure bias \\u6548\\u5e94\\u3002Gate dynamic range: L24/L28/L30 diff \\u6700\\u5927 (0.23-0.38)\\uff0c\\u4e0e Qwen \\u7c7b\\u4f3c\\u96c6\\u4e2d\\u5728\\u4e2d\\u9ad8\\u5c42\\u3002\"\n\n================================================================================\nEXP_ID: phase2_lora_only_s42\nSTATUS: DONE\nCONCLUSION: \"success\"\nNOTES: \"\\u8bca\\u65ad\\u786e\\u8ba4\\uff1aEXIT_CODE=1 \\u56e0 argparse \\u4e0d\\u8ba4 lora_only \\u9009\\u9879\\uff08choices \\u53ea\\u6709 threadgate/uniform/none\\uff09\\u3002\\u8bad\\u7ec3\\u5b9e\\u9645\\u5df2\\u7528 --gate-type none \\u5b8c\\u6210 3 epoch (3000 steps, 20588.6s/5.7h)\\u3002Gate \\u5168\\u7a0b\\u56fa\\u5b9a 1.0\\uff08\\u7b26\\u5408 lora_only \\u8bed\\u4e49\\uff09\\u3002Checkpoint \\u53ef\\u7528\\uff0c\\u65e0\\u9700\\u91cd\\u8dd1\\u3002\\u4fee\\u590d\\uff1adispatch \\u547d\\u4ee4\\u6539\\u7528 --gate-type none \\u6216\\u5728 train_phase2.py \\u6dfb\\u52a0 lora_only choice\\u3002\"\n\n================================================================================\nEXP_ID: attention_steering_gen_n50\nSTATUS: DONE\nCONCLUSION: \"success\"\nNOTES: \"\\u539f\\u59cb\\u805a\\u5408\\u6709 min_turns \\u622a\\u65ad bug\\uff08\\u622a\\u5230 2 turns\\uff09\\uff0c\\u4fee\\u6b63\\u540e\\u7528 per-conv mid_gar(turns 2-7)\\u300239/50 \\u5bf9\\u8bdd\\u6709 \\u22653 turns \\u53c2\\u4e0e\\u7edf\\u8ba1\\u3002\\u4fee\\u6b63\\u540e baseline \\u03b2=0 GAR \\u4ece 0.101 \\u964d\\u5230 0.064\\uff08median 0.031 \\u4e0e N=5 \\u7684 0.028 \\u4e00\\u81f4\\uff09\\u3002Phase transition \\u5728 \\u03b2\\u2208[2,3] \\u91cd\\u73b0\\u3002\\u03b2=10 corrected 0.961 \\u2248 N=5 \\u7684 0.959\\u3002\"\n\n================================================================================\nEXP_ID: attention_steering_v7_tg_gen\nSTATUS: DONE\nCONCLUSION: \"success\"\nNOTES: \"Attention steering \\u95ed\\u5408\\u56e0\\u679c\\u73af\\u3002\\u03b2=0\\u21922: GAR \\u7f13\\u5347 (0.028\\u21920.062), PPL \\u4e0d\\u53d8 (~1.4); \\u03b2=5: phase transition, GAR \\u8df3\\u81f3 0.68, PPL \\u5347\\u81f3 1.91; \\u03b2=10: GAR \\u9971\\u548c 0.96, PPL \\u6076\\u5316 4.22\\u3002\\u6210\\u529f\\u6807\\u51c6 (GAR>0.1 \\u4e14 PPL \\u4e0d\\u4e25\\u91cd\\u6076\\u5316) \\u5728 \\u03b2=2 \\u5373\\u6ee1\\u8db3\\u3002\\u03b2\\u2208[2,5] \\u5b58\\u5728 phase transition\\u3002\\u8bc1\\u660e\\uff1a\\u624b\\u52a8\\u4fee\\u6b63 attention \\u6307\\u5411 goal tokens \\u2192 \\u76f4\\u63a5\\u6062\\u590d GAR \\u2192 \\u786e\\u8ba4 exposure bias \\u901a\\u8fc7 attention \\u504f\\u79fb\\u5bfc\\u81f4 GAR \\u574d\\u584c\\u3002\"\n\n================================================================================\nEXP_ID: d048_eval_ss_s42\nSTATUS: DONE\nCONCLUSION: \"success\"\n\n================================================================================\nEXP_ID: d048_eval_ss_s123\nSTATUS: DONE\nCONCLUSION: \"success\"\nNOTES: \"Cron\\u8bef\\u5224\\u4fee\\u590d: \\u539fPID 109385\\u662fTF eval\\u5b50\\u8fdb\\u7a0b,\\u9000\\u51fa\\u540ecron 5\\u6b21\\u68c0\\u6d4b\\u5931\\u8d25auto-resolved\\u4e3afailed\\u3002\\u5b9e\\u9645AR eval PID 110052\\u4ecd\\u5728\\u8fd0\\u884c\\u3002\\u5df2\\u624b\\u52a8\\u6062\\u590dRUNNING\\u3002\"\n\n================================================================================\nEXP_ID: d048_eval_ss_s456\nSTATUS: DONE\nCONCLUSION: \"success\"\n\n================================================================================\nEXP_ID: eval_v7_tg_s123\nSTATUS: DONE\nCONCLUSION: \"success\"\n\n================================================================================\nEXP_ID: analysis_gradient_conflict\nSTATUS: DONE\nCONCLUSION: \"success\"\n\n================================================================================\nEXP_ID: analysis_attention_heatmap\nSTATUS: DONE\nCONCLUSION: \"success\"\n\n================================================================================\nEXP_ID: qwen15b_phase1_diag\nSTATUS: DONE\nCONCLUSION: \"success\"\n\n================================================================================\nEXP_ID: phase1_gar_diag\nSTATUS: DONE\nCONCLUSION: \"success\"\n\n================================================================================\nEXP_ID: p1_tf_ar_kl_divergence\nSTATUS: DONE\nCONCLUSION: \"success\"\n\n================================================================================\nEXP_ID: eval_v8b_ss\nSTATUS: DONE\nCONCLUSION: \"success\"\n\n================================================================================\nEXP_ID: eval_v8b_ss_s123\nSTATUS: DONE\nCONCLUSION: \"success\"\n\n================================================================================\nEXP_ID: phase2_tg_s42_v8b_ss_fixed\nSTATUS: DONE\nCONCLUSION: \"failed\"\nNOTES: \"CUDA OOM at Epoch 1 Step 4300 (loss.backward). \\u5176\\u4ed6\\u8fdb\\u7a0b\\u5171\\u4eab GPU \\u5bfc\\u81f4\\u663e\\u5b58\\u4e0d\\u8db3: Process 157667 (26.76GB) + Process 158713 (17.28GB) + PyTorch \\u81ea\\u8eab 45.21GB + 4.81GB reserved > 94.97GB \\u603b\\u5bb9\\u91cf\\u3002\\u8bad\\u7ec3\\u5728 OOM \\u524d\\u6b63\\u5e38\\u6536\\u655b (SS ratio=0.5, Loss~1.0, Gate~0.94)\\u3002\\u6709 epoch_0 checkpoint\\u3002\\u9700\\u8981\\u72ec\\u5360 GPU \\u91cd\\u8dd1\\u3002\"\n\n================================================================================\nEXP_ID: phase2_tg_s42_v8_schedsampling\nSTATUS: DONE\nCONCLUSION: \"failed\"\nNOTES: \"Director kill at micro-step ~1950 (8.1%). \\u539f\\u56e0: SS path code bug (D026) + GAR-ours \\u65e0\\u63a8\\u7406 gap (D024)\\uff0c\\u5b9e\\u9a8c\\u65e0\\u6548\\u3002GPU \\u8f6c\\u5165 plan_018 PCGrad\\u3002\\u8be6\\u60c5\\uff1a(1) SS ratio \\u4ec5 0.081 \\u65f6 kill\\uff0c\\u4ec5 1 \\u6761 SS step \\u88ab\\u65e5\\u5fd7\\u6355\\u83b7\\uff0c(2) TF L_GAR \\u5728 step 800 \\u574d\\u584c\\u5230 \\u22480.006\\uff08\\u4e0e v7 \\u4e00\\u81f4\\uff09\\uff0c(3) GAR-ours \\u63a8\\u7406\\u65f6 \\u22480.50 \\u2248 target\\uff0cSS \\u7528 GAR-ours \\u8bad\\u7ec3\\u65e0\\u6cd5\\u9a8c\\u8bc1 exposure bias mitigation\\uff0c(4) lambda_gar=2.0 (vs v7 \\u7684 1.0) confound \\u672a\\u88ab\\u5145\\u5206\\u89e6\\u53d1\\u3002\"\nSPEC.hyperparams: {\n  \"lr\": 0.0002,\n  \"epochs\": 3,\n  \"grad_accum\": 8,\n  \"ss_max_ratio\": 0.5,\n  \"ss_gen_max_tokens\": 256,\n  \"ss_gen_temperature\": 0.7\n}\n\n================================================================================\nEXP_ID: v7_tg_s123\nSTATUS: DONE\nCONCLUSION: \"success\"\n\n================================================================================\nEXP_ID: d048_ss_s42\nSTATUS: DONE\nCONCLUSION: \"success\"\nNOTES: \"Training complete (resume v3). 23418s (6.5h) for epoch 1+2. Final: Avg Loss=0.9326, NTP=0.9320, GAR=0.0007, DIV=0.0000. Gate: mean=0.9527, std=0.0589, min=0.7383(L4), max=1.000. SS: 4750/16000 (29.7%) used, 0 fallback. Checkpoints: epoch_0, epoch_1, epoch_2, final. Gate profile consistent with prior SS runs (L4 lowest).\"\n\n================================================================================\nEXP_ID: d048_ss_s123\nSTATUS: DONE\nCONCLUSION: \"success\"\n\n================================================================================\nEXP_ID: d048_ss_s456\nSTATUS: DONE\nCONCLUSION: \"success\"\n\n================================================================================\nEXP_ID: llama_tg_s42\nSTATUS: DONE\nCONCLUSION: \"success\"\n\n================================================================================\nEXP_ID: llama_lora_only_s42\nSTATUS: DONE\nCONCLUSION: \"success\"\n\n================================================================================\nEXP_ID: eval_llama_lora_only_s42\nSTATUS: DONE\nCONCLUSION: \"success\"\n\n================================================================================\nEXP_ID: attention_steering_eval200_tf\nSTATUS: DONE\nCONCLUSION: \"success\"\n\n================================================================================\nEXP_ID: d048_split_softmax_eval\nSTATUS: DONE\nCONCLUSION: \"failed\"\nNOTES: \"2 critical bugs: (1) system_prompt_len=0 hardcoded at L373, (2) gen mode NaN for k\\u22601.0. Director decision 2026-05-23: not urgent, defer fix past DDL 5/25. Does not affect main paper experiments.\"\n\n================================================================================\nEXP_ID: p1_llama_ss_training\nSTATUS: DONE\nCONCLUSION: \"success\"\nSPEC.hyperparams: {\n  \"lr\": \"2e-4\",\n  \"batch_size\": 1,\n  \"grad_accum\": 8,\n  \"epochs\": 3,\n  \"ss_max_ratio\": 0.3,\n  \"lora_rank\": 16\n}\n\n================================================================================\nEXP_ID: p1_ss_lora_only\nSTATUS: DONE\nCONCLUSION: \"killed\"\n\n================================================================================\nEXP_ID: llama_ar_matched_eval\nSTATUS: DONE\nCONCLUSION: \"success\"\nNOTES: \"CORRECTION (2026-05-21 04:36): Agent \\u4e4b\\u524d\\u9519\\u8bef\\u5730\\u5c06 AR TG nGAR (0.493) \\u4e0e TF TG raw GAR (0.484) \\u5bf9\\u6bd4\\uff0c\\u8bef\\u5224\\u4e3a 'nGAR aligns, gap is normalization artifact'\\u3002Reviewer \\u6838\\u5b9e\\uff1aTF TG ours nGAR = 11.88\\uff08\\u975e 0.48\\uff09\\u3002nGAR gap = 11.88 / 0.493 = 24.1\\u00d7\\uff0c\\u6bd4 raw gap (12.5\\u00d7) \\u8fd8\\u5927\\u3002'Normalization artifact' \\u5206\\u6790\\u5b8c\\u5168\\u9519\\u8bef\\u2014\\u2014GAR-ours \\u7684 gap \\u662f\\u771f\\u5b9e\\u7684 exposure bias\\u3002\\u8bba\\u6587\\u7edd\\u5bf9\\u4e0d\\u80fd\\u4f7f\\u7528 normalization artifact \\u53d9\\u4e8b\\u3002\"",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "fb0561d2-966a-4b21-a23b-d033f6625753",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "4b680861-4da7-411a-8744-3dabfdaf2205",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Runtime record

_source line 65_

```json
{
  "type": "last-prompt",
  "leafUuid": "fa5dbb1b-cb41-43f0-87ca-4da0387c1ced",
  "sessionId": "4b680861-4da7-411a-8744-3dabfdaf2205"
}
```

---

### Runtime record

_source line 66_

```json
{
  "type": "ai-title",
  "aiTitle": "Audit quantitative claims in paper body text",
  "sessionId": "4b680861-4da7-411a-8744-3dabfdaf2205"
}
```

---

### Assistant

_source line 67 · 2026-05-25T20:39:30.794Z_

<details><summary>Logged reasoning block</summary>

```text
Good, I have the experiment notes. Now I need more detailed metrics. Let me extract the specific metrics from the key experiments, especially the ones with numerical data. Many experiments have conclusions as just "success" without detailed metrics in the notes. Let me look for the metrics/results fields more carefully, and also check any additional data sources like artifacts or log files.

Let me also read the table tex files and look for additional registry data.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fa5dbb1b-cb41-43f0-87ca-4da0387c1ced",
  "isSidechain": false,
  "requestId": "req_011CbPw3o6aiFR6Gd4Pgx6mb",
  "type": "assistant",
  "uuid": "572379e2-4abc-43cb-b264-3dd3e71eb37e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "4b680861-4da7-411a-8744-3dabfdaf2205",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NYKDdLXk5EQoSMQqRF9m3d",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8028,
      "cache_read_input_tokens": 44883,
      "output_tokens": 1105,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 8028,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1105,
          "cache_read_input_tokens": 44883,
          "cache_creation_input_tokens": 8028,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 8028
          },
          "type": "message"
        }
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

_source line 68 · 2026-05-25T20:39:31.765Z_

Now let me extract detailed metrics from the experiments that have them, and read the table files.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "572379e2-4abc-43cb-b264-3dd3e71eb37e",
  "isSidechain": false,
  "requestId": "req_011CbPw3o6aiFR6Gd4Pgx6mb",
  "type": "assistant",
  "uuid": "b6c41811-2d8a-4dba-bec1-8a83883de5b0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "4b680861-4da7-411a-8744-3dabfdaf2205",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NYKDdLXk5EQoSMQqRF9m3d",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8028,
      "cache_read_input_tokens": 44883,
      "output_tokens": 1105,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 8028,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1105,
          "cache_read_input_tokens": 44883,
          "cache_creation_input_tokens": 8028,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 8028
          },
          "type": "message"
        }
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

_source line 69 · 2026-05-25T20:39:44.714Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01XSJkGx9Hvs7W9iRCp2zZV3`</summary>

```json
{
  "command": "python3 << 'PYEOF'\nimport json\n\nREGISTRY = \"/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-11-projects-turn-residual-gating/4b680861-4da7-411a-8744-3dabfdaf2205/tool-results/mcp-agent-ml-research-read_registry-1779741484333.txt\"\ndata = json.load(open(REGISTRY))\nresult = json.loads(data['result'])\nexperiments = result['data']['experiments']\n\n# Print ALL fields for key experiments with numerical data\nkey_ids = [\n    'd048_final_ar_eval', 'mmlu_eval_all', 'instruction_retention_test',\n    'trc_baseline_v7_tg', 'analysis_gradient_conflict', 'analysis_attention_heatmap',\n    'attention_steering_gen_n50', 'p2_llama_gradient_conflict',\n    'qwen15b_phase1_diag', 'p1_llama_ss_eval',\n    'd048_eval_ss_s42', 'd048_eval_ss_s123', 'd048_eval_ss_s456',\n    'eval_v7_tg_s123', 'eval_v8b_ss', 'eval_v8b_ss_s123',\n    'p1_tf_ar_kl_divergence', 'phase1_gar_diag',\n    'eval_llama_lora_only_s42',\n]\n\nfor eid in key_ids:\n    if eid in experiments:\n        exp = experiments[eid]\n        print(f\"\\n{'='*80}\")\n        print(f\"EXP_ID: {eid}\")\n        # Print ALL fields\n        for k, v in exp.items():\n            if k in ('created_at', 'updated_at', 'completed_at', 'retry_count'):\n                continue\n            val_str = json.dumps(v, indent=2) if isinstance(v, (dict, list)) else str(v)\n            if len(val_str) > 4000:\n                val_str = val_str[:4000] + \"... [TRUNCATED]\"\n            print(f\"  {k}: {val_str}\")\nPYEOF\n",
  "description": "Extract full details from key experiments",
  "timeout": 30000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b6c41811-2d8a-4dba-bec1-8a83883de5b0",
  "isSidechain": false,
  "requestId": "req_011CbPw3o6aiFR6Gd4Pgx6mb",
  "type": "assistant",
  "uuid": "0210d68f-54b0-430c-9b11-8efd21ad23f8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "4b680861-4da7-411a-8744-3dabfdaf2205",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NYKDdLXk5EQoSMQqRF9m3d",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8028,
      "cache_read_input_tokens": 44883,
      "output_tokens": 1105,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 8028,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1105,
          "cache_read_input_tokens": 44883,
          "cache_creation_input_tokens": 8028,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 8028
          },
          "type": "message"
        }
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

_source line 70 · 2026-05-25T20:39:48.018Z_

<details><summary>↩ Tool result · `toolu_011tWV1iaP53N55YnLRwws9h`</summary>

```text
1	% Qwen2.5-1.5B cross-scale results
2	\begin{table}[t]
3	\centering
4	\small
5	\caption{Cross-scale validation on Qwen2.5-1.5B-Instruct. Phase~1 confirms the GAR decay pattern at smaller scale (79.8\% relative drop). Phase~2 shows TG improves AR at $\beta=0$ (unamplified, $p{=}0.005$) and $\beta=5$ (strong amplification, $p{<}0.001$), confirming the mechanism transfers across model sizes.}
6	\label{tab:qwen15b_results}
7	\begin{tabular}{@{}ll cc c@{}}
8	\toprule
9	\textbf{Phase} & \textbf{Metric} & \textbf{Base} & \textbf{TG} & \textbf{$p$-value} \\
10	\midrule
11	\multicolumn{5}{@{}l}{\textit{Phase 1: GAR diagnostic}} \\
12	\quad & Turn-1 GAR & 0.0336 & --- & --- \\
13	\quad & Mid-turn GAR & 0.0068 & --- & --- \\
14	\quad & Relative drop & 79.8\% & --- & --- \\
15	\midrule
16	\multicolumn{5}{@{}l}{\textit{Phase 2: TG training ($\beta$-amplified AR)}} \\
17	\quad & AR @ $\beta{=}0$ & 0.0167 {\scriptsize$\pm$0.005} & \textbf{0.0233} {\scriptsize$\pm$0.006} & 0.005$^{**}$ \\
18	\quad & AR @ $\beta{=}3$ & 0.1202 {\scriptsize$\pm$0.032} & 0.1143 {\scriptsize$\pm$0.019} & 0.815 \\
19	\quad & AR @ $\beta{=}5$ & 0.6571 {\scriptsize$\pm$0.020} & \textbf{0.7150} {\scriptsize$\pm$0.017} & $<$0.001$^{***}$ \\
20	\bottomrule
21	\end{tabular}
22	\vspace{1mm}
23	\begin{flushleft}
24	\scriptsize
25	$\pm$ values are 95\% CI half-widths. Significance via Wilcoxon signed-rank test ($N{=}39$ paired conversations). Effect sizes: $r{=}0.447$ ($\beta{=}0$), $r{=}0.749$ ($\beta{=}5$).
26	\end{flushleft}
27	\end{table}
28	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0f572d96-c61a-4ae3-9248-90c4fedc5d29",
  "isSidechain": false,
  "promptId": "8817af8a-f189-44e8-a462-1453a12b4ea3",
  "type": "user",
  "uuid": "d6a785e4-f2b5-4078-9758-0c1d0d1c519e",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/_project/paper/tab_qwen15b_results.tex",
      "content": "% Qwen2.5-1.5B cross-scale results\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Cross-scale validation on Qwen2.5-1.5B-Instruct. Phase~1 confirms the GAR decay pattern at smaller scale (79.8\\% relative drop). Phase~2 shows TG improves AR at $\\beta=0$ (unamplified, $p{=}0.005$) and $\\beta=5$ (strong amplification, $p{<}0.001$), confirming the mechanism transfers across model sizes.}\n\\label{tab:qwen15b_results}\n\\begin{tabular}{@{}ll cc c@{}}\n\\toprule\n\\textbf{Phase} & \\textbf{Metric} & \\textbf{Base} & \\textbf{TG} & \\textbf{$p$-value} \\\\\n\\midrule\n\\multicolumn{5}{@{}l}{\\textit{Phase 1: GAR diagnostic}} \\\\\n\\quad & Turn-1 GAR & 0.0336 & --- & --- \\\\\n\\quad & Mid-turn GAR & 0.0068 & --- & --- \\\\\n\\quad & Relative drop & 79.8\\% & --- & --- \\\\\n\\midrule\n\\multicolumn{5}{@{}l}{\\textit{Phase 2: TG training ($\\beta$-amplified AR)}} \\\\\n\\quad & AR @ $\\beta{=}0$ & 0.0167 {\\scriptsize$\\pm$0.005} & \\textbf{0.0233} {\\scriptsize$\\pm$0.006} & 0.005$^{**}$ \\\\\n\\quad & AR @ $\\beta{=}3$ & 0.1202 {\\scriptsize$\\pm$0.032} & 0.1143 {\\scriptsize$\\pm$0.019} & 0.815 \\\\\n\\quad & AR @ $\\beta{=}5$ & 0.6571 {\\scriptsize$\\pm$0.020} & \\textbf{0.7150} {\\scriptsize$\\pm$0.017} & $<$0.001$^{***}$ \\\\\n\\bottomrule\n\\end{tabular}\n\\vspace{1mm}\n\\begin{flushleft}\n\\scriptsize\n$\\pm$ values are 95\\% CI half-widths. Significance via Wilcoxon signed-rank test ($N{=}39$ paired conversations). Effect sizes: $r{=}0.447$ ($\\beta{=}0$), $r{=}0.749$ ($\\beta{=}5$).\n\\end{flushleft}\n\\end{table}\n",
      "numLines": 28,
      "startLine": 1,
      "totalLines": 28
    }
  },
  "sourceToolAssistantUUID": "0f572d96-c61a-4ae3-9248-90c4fedc5d29",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "4b680861-4da7-411a-8744-3dabfdaf2205",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool result

_source line 71 · 2026-05-25T20:39:44.827Z_

<details><summary>↩ Tool result · `toolu_01XSJkGx9Hvs7W9iRCp2zZV3`</summary>

```text
================================================================================
EXP_ID: d048_final_ar_eval
  status: DONE
  hypothesis: Unified AR N=50 eval across 6 conditions (Base/TG/UG/LO/PCGrad/SS) with bootstrap CI and Wilcoxon tests to establish statistically rigorous comparisons for all claims
  spec: {
  "command": "bash scripts/d048_final_ar_eval.sh",
  "server": "westd-20861",
  "data_path": "data/eval_200/eval_200.json",
  "data_count": 200,
  "model_name": "Qwen/Qwen2.5-7B-Instruct",
  "seed": 42,
  "checkpoint_source": "phase2_tg_s42_v7 / phase2_ug_s42 / phase2_lora_only_s42 / tg_v9_pcgrad_s42 / d048_ss_s42",
  "eval_data": "eval_200.json N=50",
  "checkpoint_path": "N/A (eval only)",
  "log_path": "runs/d048_final_ar_eval.log",
  "results_path": "results/d048_final_ar/"
}
  conclusion: success
  metrics: {
  "beta0": {
    "base_gar": 0.019,
    "tg_gar": 0.064,
    "ug_gar": 0.033,
    "lo_gar": 0.037,
    "pcgrad_gar": 0.03,
    "ss_gar": 0.347
  },
  "beta3": {
    "base_gar": 0.531,
    "tg_gar": 0.556,
    "ss_gar": 0.593
  },
  "beta5": {
    "base_gar": 0.704,
    "tg_gar": 0.727,
    "ss_gar": 0.717
  },
  "wilcoxon_beta0": {
    "tg_vs_base_p": "<0.001",
    "tg_vs_base_r": 0.802,
    "ss_vs_tg_p": "<0.001",
    "ss_vs_tg_r": 0.869
  },
  "ppl": {
    "base": 1.447,
    "tg": 1.432,
    "ss": 1.442
  },
  "n_convs": 39
}

================================================================================
EXP_ID: mmlu_eval_all
  status: DONE
  hypothesis: ThreadGate's per-layer gating and auxiliary GAR loss do not degrade the model's general language understanding capabilities. All fine-tuned variants (TG/UG/LO/PCGrad/SS) should maintain MMLU 5-shot accuracy within 1pp of the Base LoRA-only checkpoint, confirming that attention steering is additive rather than destructive.
  spec: {
  "command": "python eval_mmlu.py --model_path &lt;checkpoint> --n_shot 5",
  "server": "westd-20861",
  "data_path": "MMLU benchmark (5-shot)",
  "data_count": 14042,
  "model_name": "Qwen/Qwen2.5-7B-Instruct",
  "seed": 42,
  "checkpoint_source": "base/lo/ug/tg/pcgrad/ss checkpoints",
  "eval_data": "MMLU 5-shot",
  "checkpoint_path": "results/mmlu/",
  "log_path": "logs/gpu_chain_next.log"
}
  conclusion: success
  metrics: {
  "base_qwen": 0.7423,
  "pcgrad_v9_s42": 0.7386,
  "ss_v8b_s42": 0.7375,
  "lo_s42": 0.7357,
  "tg_v7_s42": 0.7347,
  "ug_s42": 0.7346
}

================================================================================
EXP_ID: instruction_retention_test
  status: DONE
  hypothesis: Turn-level residual gating (β=3) preserves instruction-following ability across multi-turn conversations better than the baseline (β=0), because gating modulates residual contributions to retain earlier context signals rather than letting them decay through successive transformer layers.
  spec: {
  "command": "python src/eval_instruction_retention.py --checkpoint runs/phase2_tg_s42_v7 --prompts data/instruction_retention_prompts.json --betas 0 3 --seed 42 --output results/instruction_retention.json",
  "server": "westd-20861",
  "data_path": "data/instruction_retention_prompts.json",
  "data_count": 18,
  "model_name": "Qwen2.5-7B-Instruct + v7 TG LoRA",
  "seed": 42,
  "checkpoint_source": "phase2_tg_s42_v7",
  "eval_data": "18 instruction retention prompts, beta=[0,3], 5 turns each"
}
  conclusion: success
  checkpoint_path: N/A (eval)
  log_path: /root/turn_residual_gating/results/instruction_retention.log
  metrics: {
  "late_turn_rate_beta0": 0.759,
  "late_turn_rate_beta3": 0.87,
  "late_turn_delta": 0.111,
  "mcnemar_chi2": 3.125,
  "mcnemar_p": 0.0771,
  "gar_compliance_r": 0.2003,
  "gar_compliance_p": 0.007,
  "category_content_constraint": {
    "beta0": 0.619,
    "beta3": 0.857,
    "delta": 0.238
  },
  "category_count_constraint": {
    "beta0": 1,
    "beta3": 1,
    "delta": 0
  },
  "category_format_constraint": {
    "beta0": 1,
    "beta3": 1,
    "delta": 0
  },
  "category_position_constraint": {
    "beta0": 0.667,
    "beta3": 0.733,
    "delta": 0.067
  }
}

================================================================================
EXP_ID: trc_baseline_v7_tg
  status: DONE
  hypothesis: 如果 exposure bias 对 auxiliary objectives 的破坏跨特征空间通用，那么 TRC (hidden state cos_sim) 在 model-gen 下也应出现与 GAR (attention 空间) 类似的 TF/gen gap。在 v7 TG / LoRA-only / base 三个 checkpoint 上测量 TRC baseline，确认 gap 是否存在。成功标准：gen TRC 显著低于 TF TRC。
  parent: phase2_tg_s42_v7
  spec: {
  "command": "bash scripts/launch_trc_baseline.sh",
  "server": "westd-20861",
  "gpu": [
    "cuda:0"
  ],
  "pid": "158700",
  "log_path": "/root/runs/turn_residual_gating/trc_baseline_v7_tg.log",
  "submitted_at": "2026-05-20T07:18:38.202Z",
  "submitted_via": "submit_training_job",
  "backend": "tmux",
  "account": "root",
  "data_path": "/root/turn_residual_gating/data/standard_conversations.json",
  "data_count": 5,
  "model_name": "Qwen2.5-7B-Instruct",
  "seed": 42,
  "checkpoint_source": "phase2_tg_s42_v7 + phase2_lora_only_s42 + base",
  "eval_data": "5 hardcoded multi-turn conversations x 10 turns",
  "checkpoint_path": "/root/turn_residual_gating/runs/trc_baseline/",
  "wall_clock_seconds": 7767.7,
  "gpu_hours": 2.16
}
  conclusion: success
  metrics: {
  "v7_tg": {
    "tf_trc": 0.3339,
    "gen_trc": 0.3323,
    "trc_gap": 0.0016,
    "tf_tbp_ppl": 1.05,
    "gen_tbp_ppl": 1.05
  },
  "lora_only": {
    "tf_trc": 0.349,
    "gen_trc": 0.4106,
    "trc_gap": -0.0617,
    "tf_tbp_ppl": 9.5,
    "gen_tbp_ppl": 12
  },
  "base": {
    "tf_trc": 0.1494,
    "gen_trc": 0.1494,
    "trc_gap": 0,
    "tf_tbp_ppl": 2.05,
    "gen_tbp_ppl": 2.05
  }
}
  notes: Cross-space 验证：exposure bias 是 attention-specific。v7 TG: TRC gap = +0.002 (近零)，hidden state 一致性在 TF/gen 之间无差异。对比 GAR 的 30x gap，TRC 无 gap → exposure bias 只扭曲 attention 分布，不影响 hidden state 层面。LoRA-only: 反转 gap (-0.062)，gen TRC 更高但 TBP PPL 严重恶化 (9.5→12.0)——hidden states "坍缩"趋同但信息量下降。Base: 零 gap（但可能有 eval 脚本 bug，gen 模式复用了 TF hidden states）。

================================================================================
EXP_ID: analysis_gradient_conflict
  status: DONE
  hypothesis: NTP-GAR 梯度冲突在 v7 训练过程中是否逐层普遍存在？量化 cos_sim 和 magnitude ratio 的演化，验证 NTP 是否在训练中逐渐完全压制 GAR 信号。
  parent: phase2_tg_s42_v7
  spec: {
  "command": "gradient conflict analysis script",
  "server": "westd-20861",
  "data_path": "v7 epoch 0/1/2 checkpoints",
  "data_count": 3,
  "model_name": "Qwen2.5-7B-Instruct",
  "seed": 42,
  "checkpoint_source": "phase2_tg_s42_v7",
  "eval_data": "v7 3-epoch checkpoints (gradient analysis)",
  "checkpoint_path": "N/A (analysis)",
  "log_path": "westd-20861:/root/turn_residual_gating/runs/analysis/"
}
  conclusion: success
  metrics: {
  "epoch0_cos_sim": -0.089,
  "epoch1_cos_sim": -0.054,
  "epoch2_cos_sim": -0.042,
  "epoch0_neg_layers_pct": 78.6,
  "epoch1_neg_layers_pct": 71.4,
  "epoch2_neg_layers_pct": 67.9,
  "epoch0_mag_ratio": 7.5,
  "epoch1_mag_ratio": 13.7,
  "epoch2_mag_ratio": 14.7
}

================================================================================
EXP_ID: analysis_attention_heatmap
  status: DONE
  hypothesis: 四模型（Base/TG/UG/LoRA-only）的 goal attention 衰减模式是否一致？如果 TG 的 attention decay 与 LoRA-only 无差异，则 gating 机制对 attention 分布零增量。
  parent: phase2_tg_s42_v7
  spec: {
  "command": "attention heatmap analysis script",
  "server": "westd-20861",
  "data_path": "standard_conversations.json",
  "data_count": 5,
  "model_name": "Qwen2.5-7B-Instruct",
  "seed": 42,
  "checkpoint_source": "phase2_tg_s42_v7 + phase2_ug_s42 + phase2_lora_only_s42",
  "eval_data": "standard_conversations.json (5 convs x 10 turns)",
  "checkpoint_path": "N/A (analysis)",
  "log_path": "westd-20861:/root/turn_residual_gating/runs/analysis/"
}
  conclusion: success
  metrics: {
  "base_mean_goal_attn": 0.0136,
  "base_decay": 0.875,
  "tg_mean_goal_attn": 0.0232,
  "tg_decay": 0.777,
  "ug_mean_goal_attn": 0.0216,
  "ug_decay": 0.803,
  "lora_mean_goal_attn": 0.0216,
  "lora_decay": 0.81,
  "gating_incremental_benefit": "none"
}

================================================================================
EXP_ID: attention_steering_gen_n50
  status: DONE
  hypothesis: N=5 gen steering 显示 β∈[2,5] phase transition (GAR 0.06→0.68)，但样本量不足以报告置信区间。N=50 conversations 应重现同一 phase transition pattern 并提供统计鲁棒的 mean±std，加固 C6 claim (attention steering as causal mechanism proof)。
  parent: attention_steering_v7_tg_gen
  spec: {
  "command": "CUDA_VISIBLE_DEVICES=0 python src/eval_attention_steering.py --checkpoint runs/phase2_tg_s42_v7 --mode gen --data-file data/eval_200/eval_200.json --max-convs 50 --beta 0 2 3 4 5 10 --output-dir runs/attention_steering/ --output-name attention_steering_gen_n50",
  "server": "westd-20861",
  "gpu": [
    "cuda:0"
  ],
  "data_path": "data/eval_200/eval_200.json",
  "data_count": 50,
  "model_name": "Qwen2.5-7B-Instruct + v7 TG LoRA",
  "seed": "N/A (eval)",
  "checkpoint_source": "phase2_tg_s42_v7",
  "eval_data": "50 conversations from eval_200.json, gen mode autoregressive",
  "checkpoint_path": "N/A (eval experiment)",
  "log_path": "/root/turn_residual_gating/runs/attention_steering/attention_steering_gen_n50.json"
}
  metrics: {
  "corrected": true,
  "aggregation": "per-conv mid_gar(turns 2-7), >=3 turns only",
  "beta_0.0": {
    "mid_gar": 0.0641,
    "mid_gar_std": 0.0809,
    "ppl": 1.4324,
    "ppl_std": 0.1029,
    "n_valid": 39
  },
  "beta_2.0": {
    "mid_gar": 0.128,
    "mid_gar_std": 0.1101,
    "ppl": 1.4822,
    "ppl_std": 0.1385,
    "n_valid": 39
  },
  "beta_3.0": {
    "mid_gar": 0.5558,
    "mid_gar_std": 0.0601,
    "ppl": 1.5605,
    "ppl_std": 0.1719,
    "n_valid": 39
  },
  "beta_4.0": {
    "mid_gar": 0.6439,
    "mid_gar_std": 0.0607,
    "ppl": 1.6674,
    "ppl_std": 0.2241,
    "n_valid": 39
  },
  "beta_5.0": {
    "mid_gar": 0.7271,
    "mid_gar_std": 0.0605,
    "ppl": 1.7723,
    "ppl_std": 0.2693,
    "n_valid": 38
  },
  "beta_10.0": {
    "mid_gar": 0.9612,
    "mid_gar_std": 0.0152,
    "ppl": 3.4517,
    "ppl_std": 1.7813,
    "n_valid": 39
  },
  "n_convs_total": 50,
  "n_convs_valid": 39,
  "mode": "gen",
  "phase_transition_range": "[2, 3]"
}
  conclusion: success
  notes: 原始聚合有 min_turns 截断 bug（截到 2 turns），修正后用 per-conv mid_gar(turns 2-7)。39/50 对话有 ≥3 turns 参与统计。修正后 baseline β=0 GAR 从 0.101 降到 0.064（median 0.031 与 N=5 的 0.028 一致）。Phase transition 在 β∈[2,3] 重现。β=10 corrected 0.961 ≈ N=5 的 0.959。

================================================================================
EXP_ID: p2_llama_gradient_conflict
  status: DONE
  hypothesis: PCGrad fails to improve AR GAR on Llama-3.1-8B (as on Qwen), confirming cross-model that gradient conflict is not the root cause of the TF-AR gap, strengthening C2 (causal exclusion).
  spec: {
  "command": "bash scripts/p2_llama_gradient_conflict.sh",
  "server": "westd-20861",
  "data_path": "/root/turn-residual-gating/data/train_400.json",
  "data_count": 400,
  "model_name": "meta-llama/Llama-3.1-8B-Instruct",
  "seed": 42,
  "checkpoint_path": "results/p2_llama_gradient_conflict/",
  "log_path": "logs/p2_llama_gradient_conflict.log"
}
  conclusion: success
  metrics: {
  "cos_sim_mean": 0.0045,
  "cos_sim_std": 0.07,
  "neg_cos_sim_layers_pct": 53.1,
  "mag_ratio_median": 25.7,
  "conclusion_note": "cos_sim\u22480 indicates near-orthogonal (NOT conflict). Script conclusion text 'widespread conflict' is misleading \u2014 actual finding: NTP and GAR gradients are nearly orthogonal on Llama, consistent with Qwen pattern."
}

================================================================================
EXP_ID: qwen15b_phase1_diag
  status: DONE
  hypothesis: GAR attention decay toward system-prompt goal tokens is a general phenomenon across model scales, not specific to 7B. Qwen-2.5-1.5B-Instruct should also show progressive GAR decline across conversation turns, confirming the phenomenon is architecture-level rather than scale-dependent.
  spec: {
  "command": "python train_phase2.py --model Qwen/Qwen2.5-1.5B-Instruct --config configs/tg_v7.yaml --seed 42 --epochs 3",
  "server": "westd-20861",
  "data_path": "/root/turn-residual-gating/data/train_400.json",
  "data_count": 400,
  "model_name": "Qwen/Qwen2.5-1.5B-Instruct",
  "seed": 42,
  "checkpoint_path": "runs/qwen15b_tg_v7_s42/",
  "log_path": "logs/qwen15b_phase1_diag.log"
}
  conclusion: success

================================================================================
EXP_ID: p1_llama_ss_eval
  status: DONE
  hypothesis: Llama SS (2-epoch) reduces the TF-AR GAR gap on Llama-3.1-8B, confirming SS as model-general mitigation (C4+C5). Eval: TF+AR N=50 β=0/3/5.
  spec: {
  "command": "bash scripts/p1_llama_ss_eval.sh",
  "server": "westd-20861",
  "data_path": "/root/turn-residual-gating/data/eval_50.json",
  "data_count": 50,
  "model_name": "meta-llama/Llama-3.1-8B-Instruct",
  "seed": 42,
  "checkpoint_source": "runs/p1_llama_ss_s42/epoch_1/",
  "log_path": "runs/p1_llama_ss_eval.log",
  "pid": 178624,
  "checkpoint_path": "results/llama_ss_eval/"
}
  conclusion: success
  metrics: {
  "ss_tf_gar": 0.477,
  "ss_tf_ppl": 2.82,
  "ss_ar_b0_gar": 0.1662,
  "ss_ar_b0_ppl": 1.37,
  "ss_ar_b5_gar": 0.7905,
  "ss_ar_b5_ppl": 1.81,
  "base_ar_gar": 0.0179,
  "base_ar_ppl": 1.22,
  "tf_ar_gap": 2.87
}

================================================================================
EXP_ID: d048_eval_ss_s42
  status: DONE
  spec: {
  "command": "bash scripts/d048_eval_ss_s42.sh",
  "server": "westd-20861",
  "gpu": [
    "cuda:0"
  ],
  "pid": "48241",
  "log_path": "/root/turn_residual_gating/runs/d048_ss_s42/eval.log",
  "submitted_at": "2026-05-22T22:52:15.275Z",
  "submitted_via": "submit_training_job",
  "backend": "tmux",
  "account": "root",
  "data_path": "data/ultrachat_8k + model-gen AR N=50",
  "data_count": 50,
  "model_name": "Qwen2.5-7B-Instruct (SS s42)",
  "seed": 42,
  "checkpoint_source": "runs/d048_ss_s42/epoch_2",
  "eval_data": "ultrachat_eval_heldout 50 + model-gen AR N=50",
  "checkpoint_path": "runs/d048_ss_s42/epoch_2",
  "wall_clock_seconds": 1365.5,
  "gpu_hours": 0.38
}
  hypothesis: D048 multi-seed SS s42 eval: TF + AR N=50 + bootstrap CI (curve[2:]) to establish mean±std for scheduled sampling. Expect TF GAR ~0.50, AR GAR gap < 2× (vs base ~31×), PPL stable.
  parent: d048_ss_s42
  reproduce: {
  "finished_at": "2026-05-22T23:12:55.735Z"
}
  extra: {
  "hook_events": [
    {
      "event": "on_complete",
      "action": "agent",
      "ts": "2026-05-22T23:12:58.142628+00:00"
    }
  ]
}
  metrics: {
  "tf": {
    "base_gar_ours_mid": 0.0128,
    "base_gar_dongre_mid": 0.0031,
    "base_ppl": 4.34,
    "base_ntp": 1.4,
    "tg_gar_ours_mid": 0.5025,
    "tg_gar_dongre_mid": 0.389,
    "tg_ppl": 2.78,
    "tg_ntp": 0.98,
    "baseline_mid_gar": 0.0122
  },
  "ar": {
    "gar_ours_mid": 0.3887,
    "gar_ours_ci_95": [
      0.3692,
      0.3934
    ],
    "ppl": 1.35
  },
  "gap_ratio": 1.29,
  "n_conversations_tf": 50,
  "n_conversations_ar": 5,
  "bootstrap_turns": "curve[2:] (turns 3-T)",
  "note": "AR used hardcoded N=5, not N=50. Will be re-evaluated in final unified batch with eval_200.json N=50."
}
  conclusion: success

================================================================================
EXP_ID: d048_eval_ss_s123
  status: DONE
  hypothesis: SS s123 eval: TF + AR N=50 + bootstrap CI to establish multi-seed SS metrics. Expect TF GAR ~0.50, AR GAR similar to s42 (0.347), confirming SS effectiveness across seeds.
  parent: d048_ss_s123
  spec: {
  "command": "bash scripts/d048_eval_ss_s123.sh",
  "server": "westd-20861",
  "pid": "110052",
  "data_path": "/root/turn-residual-gating/data/eval_200/eval_200.json",
  "data_count": 200,
  "model_name": "Qwen/Qwen2.5-7B-Instruct + SS s123 LoRA",
  "seed": 123,
  "gpu": 0,
  "checkpoint_source": "/root/turn-residual-gating/runs/d048_ss_s123/epoch_2",
  "eval_data": "/root/turn-residual-gating/data/eval_200/eval_200.json",
  "checkpoint_path": "/root/turn-residual-gating/results/d048_final_ar/",
  "log_path": "/root/turn-residual-gating/results/d048_final_ar/"
}
  notes: Cron误判修复: 原PID 109385是TF eval子进程,退出后cron 5次检测失败auto-resolved为failed。实际AR eval PID 110052仍在运行。已手动恢复RUNNING。
  conclusion: success
  metrics: {
  "tf_gar_ours": 0.5536,
  "tf_gar_dongre": 0.4106,
  "tf_ppl": 2.6123,
  "ar_beta0_gar": 0.4231,
  "ar_beta0_ppl": 1.4408,
  "ar_beta3_gar": 0.5903,
  "ar_beta3_ppl": 1.607,
  "ar_beta5_gar": 0.7174,
  "ar_beta5_ppl": 1.7852,
  "n_convs_tf": 200,
  "n_convs_ar": 39
}

================================================================================
EXP_ID: d048_eval_ss_s456
  status: DONE
  hypothesis: SS s456 eval: TF + AR N=50 + bootstrap CI to complete 3-seed SS metrics. Together with s42 and s123, establishes mean±std for C2 reviewer requirement.
  parent: d048_ss_s456
  spec: {
  "command": "bash scripts/d048_eval_ss_s456.sh",
  "server": "westd-20861",
  "pid": "129280",
  "data_path": "/root/turn-residual-gating/data/eval_200/eval_200.json",
  "data_count": 200,
  "model_name": "Qwen/Qwen2.5-7B-Instruct + SS s456 LoRA",
  "seed": 456,
  "gpu": 0,
  "checkpoint_source": "/root/turn-residual-gating/runs/d048_ss_s456/epoch_2",
  "eval_data": "/root/turn-residual-gating/data/eval_200/eval_200.json",
  "checkpoint_path": "/root/turn-residual-gating/results/d048_final_ar/",
  "log_path": "/root/turn-residual-gating/results/d048_final_ar/"
}
  conclusion: success
  metrics: {
  "tf_gar_ours_mid": 0.4964,
  "tf_gar_dongre_mid": 0.3862,
  "ar_beta0_gar": 0.4325,
  "ar_beta0_ppl": 1.4394,
  "ar_beta3_gar": 0.605,
  "ar_beta3_ppl": 1.5868,
  "ar_beta5_gar": 0.7157,
  "ar_beta5_ppl": 1.8045,
  "n_convs_ar": 50
}

================================================================================
EXP_ID: eval_v7_tg_s123
  status: DONE
  spec: {
  "command": "bash scripts/eval_v7_tg_s123.sh",
  "server": "westd-20861",
  "gpu": [
    "cuda:0"
  ],
  "pid": "264869",
  "log_path": "/root/turn_residual_gating/logs/v7_tg_s123.log",
  "submitted_at": "2026-05-21T22:53:18.065Z",
  "submitted_via": "submit_training_job",
  "backend": "tmux",
  "account": "root",
  "data_path": "data/ultrachat_8k",
  "data_count": 8000,
  "model_name": "Qwen2.5-7B-Instruct",
  "seed": 123,
  "checkpoint_source": "v7_tg_s123",
  "eval_data": "data/ultrachat_8k",
  "checkpoint_path": "/root/turn_residual_gating/runs/phase2_tg_s123_v7/epoch_2",
  "wall_clock_seconds": 5844.5,
  "gpu_hours": 1.62
}
  hypothesis: v7 TG s123 eval: 验证 s123 seed 的 TF-AR GAR gap 与 s42 一致（~32×），确认 multi-seed robustness
  parent: v7_tg_s123
  conclusion: success
  metrics: {
  "iid_tf": {
    "gar_ours_mid": 0.5052,
    "gar_dongre_mid": 0.0119,
    "ppl": 2.7802,
    "ntp": 0.9752
  },
  "modelgen_ar": {
    "gar_ours_mid": 0.0165,
    "gar_dongre_mid": 0.0177,
    "ppl": 1.3855,
    "ntp": 0.3223
  },
  "gap_ratio": 30.6,
  "comparison_s42": {
    "tf_gar_ours_delta": 0.0017,
    "ar_gar_ours_delta": 0.0008,
    "gap_ratio_delta": -1.4
  }
}

================================================================================
EXP_ID: eval_v8b_ss
  status: DONE
  hypothesis: Scheduled Sampling (linear 0→0.5 mixing of teacher-forced and model-gen contexts) closes the 30x training-inference GAR gap by reducing exposure bias, resulting in model-gen GAR significantly above v7 baseline (0.016) while preserving IID GAR and PPL.
  parent: phase2_tg_s42_v8b_ss
  spec: {
  "command": "python src/eval_phase2_gar.py --checkpoint-dir checkpoints/tg_v8b_ss_fixed_s42 --gate-type threadgate",
  "server": "westd-20861",
  "data_path": "data/ultrachat_eval_heldout.json + built-in 5conv model-gen",
  "data_count": "50 heldout + 5 model-gen",
  "model_name": "Qwen2.5-7B-Instruct",
  "seed": 42,
  "checkpoint_source": "checkpoints/tg_v8b_ss_fixed_s42",
  "eval_data": "ultrachat_eval_heldout.json (IID) + built-in model-gen (5x10 turns)",
  "checkpoint_path": "checkpoints/tg_v8b_ss_fixed_s42",
  "log_path": "/tmp/eval_v8b_all.log"
}
  metrics: {
  "iid_gar_ours": 0.4983,
  "iid_gar_dongre": 0.3855,
  "iid_ppl": 2.78,
  "iid_ngar_ours": 13.5,
  "iid_ngar_dongre": 22.68,
  "modelgen_gar_ours": 0.3177,
  "modelgen_gar_dongre": 0.3533,
  "modelgen_ppl": 1.38,
  "modelgen_ngar_ours": 4.47,
  "modelgen_ngar_dongre": 5.92,
  "iid_turn1_gar_ours": 0.5398,
  "modelgen_turn1_gar_ours": 0.4333
}
  conclusion: success

================================================================================
EXP_ID: eval_v8b_ss_s123
  status: DONE
  spec: {
  "command": "bash scripts/eval_v8b_ss_s123.sh",
  "server": "westd-20861",
  "gpu": [
    "cuda:0"
  ],
  "pid": 259767,
  "log_path": "runs/eval_v8b_ss_s123/",
  "submitted_at": "2026-05-21T21:15:52.785Z",
  "submitted_via": "submit_training_job",
  "backend": "tmux",
  "account": "root",
  "data_path": "data/ultrachat_eval_heldout.json",
  "data_count": 50,
  "model_name": "Qwen2.5-7B-Instruct",
  "seed": 123,
  "gpu_index": 0,
  "checkpoint_source": "checkpoints/tg_v8b_ss_s123/epoch_2",
  "eval_data": "ultrachat_eval_heldout + model-gen",
  "checkpoint_path": "checkpoints/tg_v8b_ss_s123/epoch_2",
  "wall_clock_seconds": 5835.7,
  "gpu_hours": 1.62
}
  hypothesis: v8b SS model trained with s123 seed should reproduce s42 GAR metrics within acceptable gap_ratio [1.2x-2.5x] and no PPL degradation, confirming seed robustness of the scheduled sampling approach
  parent: v7_tg_s123
  log_path: ~/runs/turn_residual_gating/eval_v8b_ss_s123.log
  conclusion: success
  metrics: {
  "iid": {
    "gar_ours": 0.503,
    "gar_dongre": 0.394,
    "ppl": 2.781,
    "ntp_loss": 0.976,
    "n_conv": 50,
    "n_turns": 3
  },
  "modelgen": {
    "gar_ours": 0.418,
    "gar_dongre": 0.441,
    "ppl": 1.389,
    "ntp_loss": 0.325,
    "n_conv": 5,
    "n_turns": 10
  },
  "gap_ratio": 1.2,
  "base_iid_ppl": 4.338,
  "base_modelgen_ppl": 1.351
}

================================================================================
EXP_ID: p1_tf_ar_kl_divergence
  status: DONE
  hypothesis: TF and AR attention distributions diverge more on GAR-relevant heads (high gate values) than non-relevant heads, providing mechanistic evidence that exposure bias selectively disrupts goal-attending computation rather than uniformly degrading attention.
  metrics: {
  "tg_delta_gar": 0.0165,
  "base_delta_gar": 0.0122,
  "tg_mean_kl": 0.054,
  "base_mean_kl": 0.043,
  "gate_kl_correlation": 0.11,
  "high_kl_layers": "L23-L27, L9",
  "gar_robustness_ours_tg_base_ratio": 21.4,
  "gar_robustness_goal_only_ratio": 63,
  "gar_robustness_ours_all_ratio": 1.7,
  "gar_robustness_ours_first_ratio": 1.8
}
  spec: {
  "command": "python scripts/p1_kl_divergence.py",
  "server": "westd-20861",
  "data_path": "/root/turn_residual_gating/data/eval_200.json",
  "data_count": 30,
  "model_name": "Qwen/Qwen2.5-7B-Instruct",
  "seed": 42,
  "checkpoint_path": "results/p1_kl_perhead/",
  "log_path": "logs/p1_kl_divergence_step2.log"
}
  conclusion: success

================================================================================
EXP_ID: phase1_gar_diag
  status: DONE
  hypothesis: Qwen2.5-7B-Instruct 在 10-turn 多轮对话中，中间 turns (3-8) 的 GAR (Goal Accessibility Ratio) 相对 turn-1 下降 ≥15%，表明模型对 system prompt 中目标 token 的注意力随对话进行显著衰减
  spec: {
  "command": "python run_phase1_gar.py --results-dir /root/turn_residual_gating/results",
  "server": "westd-20861",
  "model_name": "Qwen/Qwen2.5-7B-Instruct",
  "data_path": "built-in 5 conversations (knowledge_qa, coding_help, creative_writing, math_reasoning, roleplay_advisor)",
  "data_count": 5,
  "seed": 0,
  "checkpoint_path": "N/A",
  "log_path": "/root/turn_residual_gating/results/phase1_run.log"
}
  conclusion: success
  metrics: {
  "turn1_avg_gar": 0.0418,
  "mid_turns_avg_gar": 0.0122,
  "relative_drop": 0.708,
  "num_conversations": 5,
  "num_turns": 10,
  "per_turn_avg_gar": [
    0.0418,
    0.0241,
    0.0224,
    0.013,
    0.0133,
    0.0086,
    0.0078,
    0.008,
    0.0157,
    0.0064
  ]
}

================================================================================
EXP_ID: eval_llama_lora_only_s42
  status: DONE
  hypothesis: LoRA-only ablation (no gate) on Llama-3.1-8B: if TG's GAR improvement comes from the gate, LoRA-only should show minimal GAR recovery vs base.
  parent: llama_lora_only_s42
  spec: {
  "command": "bash -c \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/turn_residual_gating && bash scripts/eval_llama_lora_only_s42.sh\"",
  "server": "westd-20861",
  "gpu": [
    "cuda:0"
  ],
  "pid": "309670",
  "log_path": "/root/runs/turn_residual_gating/eval_llama_lora_only_s42.log",
  "submitted_at": "2026-05-22T07:40:34.437Z",
  "submitted_via": "submit_training_job",
  "backend": "tmux",
  "account": "root",
  "data_path": "ultrachat_200k + model-gen",
  "data_count": 55,
  "model_name": "Llama-3.1-8B-Instruct + LoRA-only checkpoint",
  "seed": 42,
  "checkpoint_source": "llama_lora_only_s42",
  "eval_data": "IID heldout 50 + model-gen 5",
  "checkpoint_path": "runs/phase2_llama_lora_only_s42/epoch_2",
  "wall_clock_seconds": 650.8,
  "gpu_hours": 0.18
}
  reproduce: {
  "finished_at": "2026-05-22T07:45:28.637Z"
}
  extra: {
  "hook_events": [
    {
      "event": "on_complete",
      "action": "agent",
      "ts": "2026-05-22T07:45:30.556207+00:00"
    }
  ]
}
  metrics: {
  "tf": {
    "gar_ours": 0.4807,
    "gar_dongre": 0.0188,
    "ngar_ours": 11.8031,
    "ngar_dongre": 0.8261,
    "ppl": 2.6,
    "ntp_loss": 0.9366,
    "n_conversations": 50,
    "n_turns": 4
  },
  "ar": {
    "gar_ours": 0.0617,
    "gar_dongre": 0.0226,
    "ngar_ours": 0.6065,
    "ngar_dongre": 0.2537,
    "ppl": 1.32,
    "ntp_loss": 0.2787,
    "n_conversations": 5,
    "n_turns": 10
  },
  "gap_ratio_gar_ours": 7.79
}
  conclusion: success
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0210d68f-54b0-430c-9b11-8efd21ad23f8",
  "isSidechain": false,
  "promptId": "8817af8a-f189-44e8-a462-1453a12b4ea3",
  "type": "user",
  "uuid": "0c0a69fc-6734-4da5-8f7b-e1e3af1ae799",
  "toolUseResult": {
    "stdout": "================================================================================\nEXP_ID: d048_final_ar_eval\n  status: DONE\n  hypothesis: Unified AR N=50 eval across 6 conditions (Base/TG/UG/LO/PCGrad/SS) with bootstrap CI and Wilcoxon tests to establish statistically rigorous comparisons for all claims\n  spec: {\n  \"command\": \"bash scripts/d048_final_ar_eval.sh\",\n  \"server\": \"westd-20861\",\n  \"data_path\": \"data/eval_200/eval_200.json\",\n  \"data_count\": 200,\n  \"model_name\": \"Qwen/Qwen2.5-7B-Instruct\",\n  \"seed\": 42,\n  \"checkpoint_source\": \"phase2_tg_s42_v7 / phase2_ug_s42 / phase2_lora_only_s42 / tg_v9_pcgrad_s42 / d048_ss_s42\",\n  \"eval_data\": \"eval_200.json N=50\",\n  \"checkpoint_path\": \"N/A (eval only)\",\n  \"log_path\": \"runs/d048_final_ar_eval.log\",\n  \"results_path\": \"results/d048_final_ar/\"\n}\n  conclusion: success\n  metrics: {\n  \"beta0\": {\n    \"base_gar\": 0.019,\n    \"tg_gar\": 0.064,\n    \"ug_gar\": 0.033,\n    \"lo_gar\": 0.037,\n    \"pcgrad_gar\": 0.03,\n    \"ss_gar\": 0.347\n  },\n  \"beta3\": {\n    \"base_gar\": 0.531,\n    \"tg_gar\": 0.556,\n    \"ss_gar\": 0.593\n  },\n  \"beta5\": {\n    \"base_gar\": 0.704,\n    \"tg_gar\": 0.727,\n    \"ss_gar\": 0.717\n  },\n  \"wilcoxon_beta0\": {\n    \"tg_vs_base_p\": \"<0.001\",\n    \"tg_vs_base_r\": 0.802,\n    \"ss_vs_tg_p\": \"<0.001\",\n    \"ss_vs_tg_r\": 0.869\n  },\n  \"ppl\": {\n    \"base\": 1.447,\n    \"tg\": 1.432,\n    \"ss\": 1.442\n  },\n  \"n_convs\": 39\n}\n\n================================================================================\nEXP_ID: mmlu_eval_all\n  status: DONE\n  hypothesis: ThreadGate's per-layer gating and auxiliary GAR loss do not degrade the model's general language understanding capabilities. All fine-tuned variants (TG/UG/LO/PCGrad/SS) should maintain MMLU 5-shot accuracy within 1pp of the Base LoRA-only checkpoint, confirming that attention steering is additive rather than destructive.\n  spec: {\n  \"command\": \"python eval_mmlu.py --model_path &lt;checkpoint> --n_shot 5\",\n  \"server\": \"westd-20861\",\n  \"data_path\": \"MMLU benchmark (5-shot)\",\n  \"data_count\": 14042,\n  \"model_name\": \"Qwen/Qwen2.5-7B-Instruct\",\n  \"seed\": 42,\n  \"checkpoint_source\": \"base/lo/ug/tg/pcgrad/ss checkpoints\",\n  \"eval_data\": \"MMLU 5-shot\",\n  \"checkpoint_path\": \"results/mmlu/\",\n  \"log_path\": \"logs/gpu_chain_next.log\"\n}\n  conclusion: success\n  metrics: {\n  \"base_qwen\": 0.7423,\n  \"pcgrad_v9_s42\": 0.7386,\n  \"ss_v8b_s42\": 0.7375,\n  \"lo_s42\": 0.7357,\n  \"tg_v7_s42\": 0.7347,\n  \"ug_s42\": 0.7346\n}\n\n================================================================================\nEXP_ID: instruction_retention_test\n  status: DONE\n  hypothesis: Turn-level residual gating (β=3) preserves instruction-following ability across multi-turn conversations better than the baseline (β=0), because gating modulates residual contributions to retain earlier context signals rather than letting them decay through successive transformer layers.\n  spec: {\n  \"command\": \"python src/eval_instruction_retention.py --checkpoint runs/phase2_tg_s42_v7 --prompts data/instruction_retention_prompts.json --betas 0 3 --seed 42 --output results/instruction_retention.json\",\n  \"server\": \"westd-20861\",\n  \"data_path\": \"data/instruction_retention_prompts.json\",\n  \"data_count\": 18,\n  \"model_name\": \"Qwen2.5-7B-Instruct + v7 TG LoRA\",\n  \"seed\": 42,\n  \"checkpoint_source\": \"phase2_tg_s42_v7\",\n  \"eval_data\": \"18 instruction retention prompts, beta=[0,3], 5 turns each\"\n}\n  conclusion: success\n  checkpoint_path: N/A (eval)\n  log_path: /root/turn_residual_gating/results/instruction_retention.log\n  metrics: {\n  \"late_turn_rate_beta0\": 0.759,\n  \"late_turn_rate_beta3\": 0.87,\n  \"late_turn_delta\": 0.111,\n  \"mcnemar_chi2\": 3.125,\n  \"mcnemar_p\": 0.0771,\n  \"gar_compliance_r\": 0.2003,\n  \"gar_compliance_p\": 0.007,\n  \"category_content_constraint\": {\n    \"beta0\": 0.619,\n    \"beta3\": 0.857,\n    \"delta\": 0.238\n  },\n  \"category_count_constraint\": {\n    \"beta0\": 1,\n    \"beta3\": 1,\n    \"delta\": 0\n  },\n  \"category_format_constraint\": {\n    \"beta0\": 1,\n    \"beta3\": 1,\n    \"delta\": 0\n  },\n  \"category_position_constraint\": {\n    \"beta0\": 0.667,\n    \"beta3\": 0.733,\n    \"delta\": 0.067\n  }\n}\n\n================================================================================\nEXP_ID: trc_baseline_v7_tg\n  status: DONE\n  hypothesis: 如果 exposure bias 对 auxiliary objectives 的破坏跨特征空间通用，那么 TRC (hidden state cos_sim) 在 model-gen 下也应出现与 GAR (attention 空间) 类似的 TF/gen gap。在 v7 TG / LoRA-only / base 三个 checkpoint 上测量 TRC baseline，确认 gap 是否存在。成功标准：gen TRC 显著低于 TF TRC。\n  parent: phase2_tg_s42_v7\n  spec: {\n  \"command\": \"bash scripts/launch_trc_baseline.sh\",\n  \"server\": \"westd-20861\",\n  \"gpu\": [\n    \"cuda:0\"\n  ],\n  \"pid\": \"158700\",\n  \"log_path\": \"/root/runs/turn_residual_gating/trc_baseline_v7_tg.log\",\n  \"submitted_at\": \"2026-05-20T07:18:38.202Z\",\n  \"submitted_via\": \"submit_training_job\",\n  \"backend\": \"tmux\",\n  \"account\": \"root\",\n  \"data_path\": \"/root/turn_residual_gating/data/standard_conversations.json\",\n  \"data_count\": 5,\n  \"model_name\": \"Qwen2.5-7B-Instruct\",\n  \"seed\": 42,\n  \"checkpoint_source\": \"phase2_tg_s42_v7 + phase2_lora_only_s42 + base\",\n  \"eval_data\": \"5 hardcoded multi-turn conversations x 10 turns\",\n  \"checkpoint_path\": \"/root/turn_residual_gating/runs/trc_baseline/\",\n  \"wall_clock_seconds\": 7767.7,\n  \"gpu_hours\": 2.16\n}\n  conclusion: success\n  metrics: {\n  \"v7_tg\": {\n    \"tf_trc\": 0.3339,\n    \"gen_trc\": 0.3323,\n    \"trc_gap\": 0.0016,\n    \"tf_tbp_ppl\": 1.05,\n    \"gen_tbp_ppl\": 1.05\n  },\n  \"lora_only\": {\n    \"tf_trc\": 0.349,\n    \"gen_trc\": 0.4106,\n    \"trc_gap\": -0.0617,\n    \"tf_tbp_ppl\": 9.5,\n    \"gen_tbp_ppl\": 12\n  },\n  \"base\": {\n    \"tf_trc\": 0.1494,\n    \"gen_trc\": 0.1494,\n    \"trc_gap\": 0,\n    \"tf_tbp_ppl\": 2.05,\n    \"gen_tbp_ppl\": 2.05\n  }\n}\n  notes: Cross-space 验证：exposure bias 是 attention-specific。v7 TG: TRC gap = +0.002 (近零)，hidden state 一致性在 TF/gen 之间无差异。对比 GAR 的 30x gap，TRC 无 gap → exposure bias 只扭曲 attention 分布，不影响 hidden state 层面。LoRA-only: 反转 gap (-0.062)，gen TRC 更高但 TBP PPL 严重恶化 (9.5→12.0)——hidden states \"坍缩\"趋同但信息量下降。Base: 零 gap（但可能有 eval 脚本 bug，gen 模式复用了 TF hidden states）。\n\n================================================================================\nEXP_ID: analysis_gradient_conflict\n  status: DONE\n  hypothesis: NTP-GAR 梯度冲突在 v7 训练过程中是否逐层普遍存在？量化 cos_sim 和 magnitude ratio 的演化，验证 NTP 是否在训练中逐渐完全压制 GAR 信号。\n  parent: phase2_tg_s42_v7\n  spec: {\n  \"command\": \"gradient conflict analysis script\",\n  \"server\": \"westd-20861\",\n  \"data_path\": \"v7 epoch 0/1/2 checkpoints\",\n  \"data_count\": 3,\n  \"model_name\": \"Qwen2.5-7B-Instruct\",\n  \"seed\": 42,\n  \"checkpoint_source\": \"phase2_tg_s42_v7\",\n  \"eval_data\": \"v7 3-epoch checkpoints (gradient analysis)\",\n  \"checkpoint_path\": \"N/A (analysis)\",\n  \"log_path\": \"westd-20861:/root/turn_residual_gating/runs/analysis/\"\n}\n  conclusion: success\n  metrics: {\n  \"epoch0_cos_sim\": -0.089,\n  \"epoch1_cos_sim\": -0.054,\n  \"epoch2_cos_sim\": -0.042,\n  \"epoch0_neg_layers_pct\": 78.6,\n  \"epoch1_neg_layers_pct\": 71.4,\n  \"epoch2_neg_layers_pct\": 67.9,\n  \"epoch0_mag_ratio\": 7.5,\n  \"epoch1_mag_ratio\": 13.7,\n  \"epoch2_mag_ratio\": 14.7\n}\n\n================================================================================\nEXP_ID: analysis_attention_heatmap\n  status: DONE\n  hypothesis: 四模型（Base/TG/UG/LoRA-only）的 goal attention 衰减模式是否一致？如果 TG 的 attention decay 与 LoRA-only 无差异，则 gating 机制对 attention 分布零增量。\n  parent: phase2_tg_s42_v7\n  spec: {\n  \"command\": \"attention heatmap analysis script\",\n  \"server\": \"westd-20861\",\n  \"data_path\": \"standard_conversations.json\",\n  \"data_count\": 5,\n  \"model_name\": \"Qwen2.5-7B-Instruct\",\n  \"seed\": 42,\n  \"checkpoint_source\": \"phase2_tg_s42_v7 + phase2_ug_s42 + phase2_lora_only_s42\",\n  \"eval_data\": \"standard_conversations.json (5 convs x 10 turns)\",\n  \"checkpoint_path\": \"N/A (analysis)\",\n  \"log_path\": \"westd-20861:/root/turn_residual_gating/runs/analysis/\"\n}\n  conclusion: success\n  metrics: {\n  \"base_mean_goal_attn\": 0.0136,\n  \"base_decay\": 0.875,\n  \"tg_mean_goal_attn\": 0.0232,\n  \"tg_decay\": 0.777,\n  \"ug_mean_goal_attn\": 0.0216,\n  \"ug_decay\": 0.803,\n  \"lora_mean_goal_attn\": 0.0216,\n  \"lora_decay\": 0.81,\n  \"gating_incremental_benefit\": \"none\"\n}\n\n================================================================================\nEXP_ID: attention_steering_gen_n50\n  status: DONE\n  hypothesis: N=5 gen steering 显示 β∈[2,5] phase transition (GAR 0.06→0.68)，但样本量不足以报告置信区间。N=50 conversations 应重现同一 phase transition pattern 并提供统计鲁棒的 mean±std，加固 C6 claim (attention steering as causal mechanism proof)。\n  parent: attention_steering_v7_tg_gen\n  spec: {\n  \"command\": \"CUDA_VISIBLE_DEVICES=0 python src/eval_attention_steering.py --checkpoint runs/phase2_tg_s42_v7 --mode gen --data-file data/eval_200/eval_200.json --max-convs 50 --beta 0 2 3 4 5 10 --output-dir runs/attention_steering/ --output-name attention_steering_gen_n50\",\n  \"server\": \"westd-20861\",\n  \"gpu\": [\n    \"cuda:0\"\n  ],\n  \"data_path\": \"data/eval_200/eval_200.json\",\n  \"data_count\": 50,\n  \"model_name\": \"Qwen2.5-7B-Instruct + v7 TG LoRA\",\n  \"seed\": \"N/A (eval)\",\n  \"checkpoint_source\": \"phase2_tg_s42_v7\",\n  \"eval_data\": \"50 conversations from eval_200.json, gen mode autoregressive\",\n  \"checkpoint_path\": \"N/A (eval experiment)\",\n  \"log_path\": \"/root/turn_residual_gating/runs/attention_steering/attention_steering_gen_n50.json\"\n}\n  metrics: {\n  \"corrected\": true,\n  \"aggregation\": \"per-conv mid_gar(turns 2-7), >=3 turns only\",\n  \"beta_0.0\": {\n    \"mid_gar\": 0.0641,\n    \"mid_gar_std\": 0.0809,\n    \"ppl\": 1.4324,\n    \"ppl_std\": 0.1029,\n    \"n_valid\": 39\n  },\n  \"beta_2.0\": {\n    \"mid_gar\": 0.128,\n    \"mid_gar_std\": 0.1101,\n    \"ppl\": 1.4822,\n    \"ppl_std\": 0.1385,\n    \"n_valid\": 39\n  },\n  \"beta_3.0\": {\n    \"mid_gar\": 0.5558,\n    \"mid_gar_std\": 0.0601,\n    \"ppl\": 1.5605,\n    \"ppl_std\": 0.1719,\n    \"n_valid\": 39\n  },\n  \"beta_4.0\": {\n    \"mid_gar\": 0.6439,\n    \"mid_gar_std\": 0.0607,\n    \"ppl\": 1.6674,\n    \"ppl_std\": 0.2241,\n    \"n_valid\": 39\n  },\n  \"beta_5.0\": {\n    \"mid_gar\": 0.7271,\n    \"mid_gar_std\": 0.0605,\n    \"ppl\": 1.7723,\n    \"ppl_std\": 0.2693,\n    \"n_valid\": 38\n  },\n  \"beta_10.0\": {\n    \"mid_gar\": 0.9612,\n    \"mid_gar_std\": 0.0152,\n    \"ppl\": 3.4517,\n    \"ppl_std\": 1.7813,\n    \"n_valid\": 39\n  },\n  \"n_convs_total\": 50,\n  \"n_convs_valid\": 39,\n  \"mode\": \"gen\",\n  \"phase_transition_range\": \"[2, 3]\"\n}\n  conclusion: success\n  notes: 原始聚合有 min_turns 截断 bug（截到 2 turns），修正后用 per-conv mid_gar(turns 2-7)。39/50 对话有 ≥3 turns 参与统计。修正后 baseline β=0 GAR 从 0.101 降到 0.064（median 0.031 与 N=5 的 0.028 一致）。Phase transition 在 β∈[2,3] 重现。β=10 corrected 0.961 ≈ N=5 的 0.959。\n\n================================================================================\nEXP_ID: p2_llama_gradient_conflict\n  status: DONE\n  hypothesis: PCGrad fails to improve AR GAR on Llama-3.1-8B (as on Qwen), confirming cross-model that gradient conflict is not the root cause of the TF-AR gap, strengthening C2 (causal exclusion).\n  spec: {\n  \"command\": \"bash scripts/p2_llama_gradient_conflict.sh\",\n  \"server\": \"westd-20861\",\n  \"data_path\": \"/root/turn-residual-gating/data/train_400.json\",\n  \"data_count\": 400,\n  \"model_name\": \"meta-llama/Llama-3.1-8B-Instruct\",\n  \"seed\": 42,\n  \"checkpoint_path\": \"results/p2_llama_gradient_conflict/\",\n  \"log_path\": \"logs/p2_llama_gradient_conflict.log\"\n}\n  conclusion: success\n  metrics: {\n  \"cos_sim_mean\": 0.0045,\n  \"cos_sim_std\": 0.07,\n  \"neg_cos_sim_layers_pct\": 53.1,\n  \"mag_ratio_median\": 25.7,\n  \"conclusion_note\": \"cos_sim\\u22480 indicates near-orthogonal (NOT conflict). Script conclusion text 'widespread conflict' is misleading \\u2014 actual finding: NTP and GAR gradients are nearly orthogonal on Llama, consistent with Qwen pattern.\"\n}\n\n================================================================================\nEXP_ID: qwen15b_phase1_diag\n  status: DONE\n  hypothesis: GAR attention decay toward system-prompt goal tokens is a general phenomenon across model scales, not specific to 7B. Qwen-2.5-1.5B-Instruct should also show progressive GAR decline across conversation turns, confirming the phenomenon is architecture-level rather than scale-dependent.\n  spec: {\n  \"command\": \"python train_phase2.py --model Qwen/Qwen2.5-1.5B-Instruct --config configs/tg_v7.yaml --seed 42 --epochs 3\",\n  \"server\": \"westd-20861\",\n  \"data_path\": \"/root/turn-residual-gating/data/train_400.json\",\n  \"data_count\": 400,\n  \"model_name\": \"Qwen/Qwen2.5-1.5B-Instruct\",\n  \"seed\": 42,\n  \"checkpoint_path\": \"runs/qwen15b_tg_v7_s42/\",\n  \"log_path\": \"logs/qwen15b_phase1_diag.log\"\n}\n  conclusion: success\n\n================================================================================\nEXP_ID: p1_llama_ss_eval\n  status: DONE\n  hypothesis: Llama SS (2-epoch) reduces the TF-AR GAR gap on Llama-3.1-8B, confirming SS as model-general mitigation (C4+C5). Eval: TF+AR N=50 β=0/3/5.\n  spec: {\n  \"command\": \"bash scripts/p1_llama_ss_eval.sh\",\n  \"server\": \"westd-20861\",\n  \"data_path\": \"/root/turn-residual-gating/data/eval_50.json\",\n  \"data_count\": 50,\n  \"model_name\": \"meta-llama/Llama-3.1-8B-Instruct\",\n  \"seed\": 42,\n  \"checkpoint_source\": \"runs/p1_llama_ss_s42/epoch_1/\",\n  \"log_path\": \"runs/p1_llama_ss_eval.log\",\n  \"pid\": 178624,\n  \"checkpoint_path\": \"results/llama_ss_eval/\"\n}\n  conclusion: success\n  metrics: {\n  \"ss_tf_gar\": 0.477,\n  \"ss_tf_ppl\": 2.82,\n  \"ss_ar_b0_gar\": 0.1662,\n  \"ss_ar_b0_ppl\": 1.37,\n  \"ss_ar_b5_gar\": 0.7905,\n  \"ss_ar_b5_ppl\": 1.81,\n  \"base_ar_gar\": 0.0179,\n  \"base_ar_ppl\": 1.22,\n  \"tf_ar_gap\": 2.87\n}\n\n================================================================================\nEXP_ID: d048_eval_ss_s42\n  status: DONE\n  spec: {\n  \"command\": \"bash scripts/d048_eval_ss_s42.sh\",\n  \"server\": \"westd-20861\",\n  \"gpu\": [\n    \"cuda:0\"\n  ],\n  \"pid\": \"48241\",\n  \"log_path\": \"/root/turn_residual_gating/runs/d048_ss_s42/eval.log\",\n  \"submitted_at\": \"2026-05-22T22:52:15.275Z\",\n  \"submitted_via\": \"submit_training_job\",\n  \"backend\": \"tmux\",\n  \"account\": \"root\",\n  \"data_path\": \"data/ultrachat_8k + model-gen AR N=50\",\n  \"data_count\": 50,\n  \"model_name\": \"Qwen2.5-7B-Instruct (SS s42)\",\n  \"seed\": 42,\n  \"checkpoint_source\": \"runs/d048_ss_s42/epoch_2\",\n  \"eval_data\": \"ultrachat_eval_heldout 50 + model-gen AR N=50\",\n  \"checkpoint_path\": \"runs/d048_ss_s42/epoch_2\",\n  \"wall_clock_seconds\": 1365.5,\n  \"gpu_hours\": 0.38\n}\n  hypothesis: D048 multi-seed SS s42 eval: TF + AR N=50 + bootstrap CI (curve[2:]) to establish mean±std for scheduled sampling. Expect TF GAR ~0.50, AR GAR gap < 2× (vs base ~31×), PPL stable.\n  parent: d048_ss_s42\n  reproduce: {\n  \"finished_at\": \"2026-05-22T23:12:55.735Z\"\n}\n  extra: {\n  \"hook_events\": [\n    {\n      \"event\": \"on_complete\",\n      \"action\": \"agent\",\n      \"ts\": \"2026-05-22T23:12:58.142628+00:00\"\n    }\n  ]\n}\n  metrics: {\n  \"tf\": {\n    \"base_gar_ours_mid\": 0.0128,\n    \"base_gar_dongre_mid\": 0.0031,\n    \"base_ppl\": 4.34,\n    \"base_ntp\": 1.4,\n    \"tg_gar_ours_mid\": 0.5025,\n    \"tg_gar_dongre_mid\": 0.389,\n    \"tg_ppl\": 2.78,\n    \"tg_ntp\": 0.98,\n    \"baseline_mid_gar\": 0.0122\n  },\n  \"ar\": {\n    \"gar_ours_mid\": 0.3887,\n    \"gar_ours_ci_95\": [\n      0.3692,\n      0.3934\n    ],\n    \"ppl\": 1.35\n  },\n  \"gap_ratio\": 1.29,\n  \"n_conversations_tf\": 50,\n  \"n_conversations_ar\": 5,\n  \"bootstrap_turns\": \"curve[2:] (turns 3-T)\",\n  \"note\": \"AR used hardcoded N=5, not N=50. Will be re-evaluated in final unified batch with eval_200.json N=50.\"\n}\n  conclusion: success\n\n================================================================================\nEXP_ID: d048_eval_ss_s123\n  status: DONE\n  hypothesis: SS s123 eval: TF + AR N=50 + bootstrap CI to establish multi-seed SS metrics. Expect TF GAR ~0.50, AR GAR similar to s42 (0.347), confirming SS effectiveness across seeds.\n  parent: d048_ss_s123\n  spec: {\n  \"command\": \"bash scripts/d048_eval_ss_s123.sh\",\n  \"server\": \"westd-20861\",\n  \"pid\": \"110052\",\n  \"data_path\": \"/root/turn-residual-gating/data/eval_200/eval_200.json\",\n  \"data_count\": 200,\n  \"model_name\": \"Qwen/Qwen2.5-7B-Instruct + SS s123 LoRA\",\n  \"seed\": 123,\n  \"gpu\": 0,\n  \"checkpoint_source\": \"/root/turn-residual-gating/runs/d048_ss_s123/epoch_2\",\n  \"eval_data\": \"/root/turn-residual-gating/data/eval_200/eval_200.json\",\n  \"checkpoint_path\": \"/root/turn-residual-gating/results/d048_final_ar/\",\n  \"log_path\": \"/root/turn-residual-gating/results/d048_final_ar/\"\n}\n  notes: Cron误判修复: 原PID 109385是TF eval子进程,退出后cron 5次检测失败auto-resolved为failed。实际AR eval PID 110052仍在运行。已手动恢复RUNNING。\n  conclusion: success\n  metrics: {\n  \"tf_gar_ours\": 0.5536,\n  \"tf_gar_dongre\": 0.4106,\n  \"tf_ppl\": 2.6123,\n  \"ar_beta0_gar\": 0.4231,\n  \"ar_beta0_ppl\": 1.4408,\n  \"ar_beta3_gar\": 0.5903,\n  \"ar_beta3_ppl\": 1.607,\n  \"ar_beta5_gar\": 0.7174,\n  \"ar_beta5_ppl\": 1.7852,\n  \"n_convs_tf\": 200,\n  \"n_convs_ar\": 39\n}\n\n================================================================================\nEXP_ID: d048_eval_ss_s456\n  status: DONE\n  hypothesis: SS s456 eval: TF + AR N=50 + bootstrap CI to complete 3-seed SS metrics. Together with s42 and s123, establishes mean±std for C2 reviewer requirement.\n  parent: d048_ss_s456\n  spec: {\n  \"command\": \"bash scripts/d048_eval_ss_s456.sh\",\n  \"server\": \"westd-20861\",\n  \"pid\": \"129280\",\n  \"data_path\": \"/root/turn-residual-gating/data/eval_200/eval_200.json\",\n  \"data_count\": 200,\n  \"model_name\": \"Qwen/Qwen2.5-7B-Instruct + SS s456 LoRA\",\n  \"seed\": 456,\n  \"gpu\": 0,\n  \"checkpoint_source\": \"/root/turn-residual-gating/runs/d048_ss_s456/epoch_2\",\n  \"eval_data\": \"/root/turn-residual-gating/data/eval_200/eval_200.json\",\n  \"checkpoint_path\": \"/root/turn-residual-gating/results/d048_final_ar/\",\n  \"log_path\": \"/root/turn-residual-gating/results/d048_final_ar/\"\n}\n  conclusion: success\n  metrics: {\n  \"tf_gar_ours_mid\": 0.4964,\n  \"tf_gar_dongre_mid\": 0.3862,\n  \"ar_beta0_gar\": 0.4325,\n  \"ar_beta0_ppl\": 1.4394,\n  \"ar_beta3_gar\": 0.605,\n  \"ar_beta3_ppl\": 1.5868,\n  \"ar_beta5_gar\": 0.7157,\n  \"ar_beta5_ppl\": 1.8045,\n  \"n_convs_ar\": 50\n}\n\n================================================================================\nEXP_ID: eval_v7_tg_s123\n  status: DONE\n  spec: {\n  \"command\": \"bash scripts/eval_v7_tg_s123.sh\",\n  \"server\": \"westd-20861\",\n  \"gpu\": [\n    \"cuda:0\"\n  ],\n  \"pid\": \"264869\",\n  \"log_path\": \"/root/turn_residual_gating/logs/v7_tg_s123.log\",\n  \"submitted_at\": \"2026-05-21T22:53:18.065Z\",\n  \"submitted_via\": \"submit_training_job\",\n  \"backend\": \"tmux\",\n  \"account\": \"root\",\n  \"data_path\": \"data/ultrachat_8k\",\n  \"data_count\": 8000,\n  \"model_name\": \"Qwen2.5-7B-Instruct\",\n  \"seed\": 123,\n  \"checkpoint_source\": \"v7_tg_s123\",\n  \"eval_data\": \"data/ultrachat_8k\",\n  \"checkpoint_path\": \"/root/turn_residual_gating/runs/phase2_tg_s123_v7/epoch_2\",\n  \"wall_clock_seconds\": 5844.5,\n  \"gpu_hours\": 1.62\n}\n  hypothesis: v7 TG s123 eval: 验证 s123 seed 的 TF-AR GAR gap 与 s42 一致（~32×），确认 multi-seed robustness\n  parent: v7_tg_s123\n  conclusion: success\n  metrics: {\n  \"iid_tf\": {\n    \"gar_ours_mid\": 0.5052,\n    \"gar_dongre_mid\": 0.0119,\n    \"ppl\": 2.7802,\n    \"ntp\": 0.9752\n  },\n  \"modelgen_ar\": {\n    \"gar_ours_mid\": 0.0165,\n    \"gar_dongre_mid\": 0.0177,\n    \"ppl\": 1.3855,\n    \"ntp\": 0.3223\n  },\n  \"gap_ratio\": 30.6,\n  \"comparison_s42\": {\n    \"tf_gar_ours_delta\": 0.0017,\n    \"ar_gar_ours_delta\": 0.0008,\n    \"gap_ratio_delta\": -1.4\n  }\n}\n\n================================================================================\nEXP_ID: eval_v8b_ss\n  status: DONE\n  hypothesis: Scheduled Sampling (linear 0→0.5 mixing of teacher-forced and model-gen contexts) closes the 30x training-inference GAR gap by reducing exposure bias, resulting in model-gen GAR significantly above v7 baseline (0.016) while preserving IID GAR and PPL.\n  parent: phase2_tg_s42_v8b_ss\n  spec: {\n  \"command\": \"python src/eval_phase2_gar.py --checkpoint-dir checkpoints/tg_v8b_ss_fixed_s42 --gate-type threadgate\",\n  \"server\": \"westd-20861\",\n  \"data_path\": \"data/ultrachat_eval_heldout.json + built-in 5conv model-gen\",\n  \"data_count\": \"50 heldout + 5 model-gen\",\n  \"model_name\": \"Qwen2.5-7B-Instruct\",\n  \"seed\": 42,\n  \"checkpoint_source\": \"checkpoints/tg_v8b_ss_fixed_s42\",\n  \"eval_data\": \"ultrachat_eval_heldout.json (IID) + built-in model-gen (5x10 turns)\",\n  \"checkpoint_path\": \"checkpoints/tg_v8b_ss_fixed_s42\",\n  \"log_path\": \"/tmp/eval_v8b_all.log\"\n}\n  metrics: {\n  \"iid_gar_ours\": 0.4983,\n  \"iid_gar_dongre\": 0.3855,\n  \"iid_ppl\": 2.78,\n  \"iid_ngar_ours\": 13.5,\n  \"iid_ngar_dongre\": 22.68,\n  \"modelgen_gar_ours\": 0.3177,\n  \"modelgen_gar_dongre\": 0.3533,\n  \"modelgen_ppl\": 1.38,\n  \"modelgen_ngar_ours\": 4.47,\n  \"modelgen_ngar_dongre\": 5.92,\n  \"iid_turn1_gar_ours\": 0.5398,\n  \"modelgen_turn1_gar_ours\": 0.4333\n}\n  conclusion: success\n\n================================================================================\nEXP_ID: eval_v8b_ss_s123\n  status: DONE\n  spec: {\n  \"command\": \"bash scripts/eval_v8b_ss_s123.sh\",\n  \"server\": \"westd-20861\",\n  \"gpu\": [\n    \"cuda:0\"\n  ],\n  \"pid\": 259767,\n  \"log_path\": \"runs/eval_v8b_ss_s123/\",\n  \"submitted_at\": \"2026-05-21T21:15:52.785Z\",\n  \"submitted_via\": \"submit_training_job\",\n  \"backend\": \"tmux\",\n  \"account\": \"root\",\n  \"data_path\": \"data/ultrachat_eval_heldout.json\",\n  \"data_count\": 50,\n  \"model_name\": \"Qwen2.5-7B-Instruct\",\n  \"seed\": 123,\n  \"gpu_index\": 0,\n  \"checkpoint_source\": \"checkpoints/tg_v8b_ss_s123/epoch_2\",\n  \"eval_data\": \"ultrachat_eval_heldout + model-gen\",\n  \"checkpoint_path\": \"checkpoints/tg_v8b_ss_s123/epoch_2\",\n  \"wall_clock_seconds\": 5835.7,\n  \"gpu_hours\": 1.62\n}\n  hypothesis: v8b SS model trained with s123 seed should reproduce s42 GAR metrics within acceptable gap_ratio [1.2x-2.5x] and no PPL degradation, confirming seed robustness of the scheduled sampling approach\n  parent: v7_tg_s123\n  log_path: ~/runs/turn_residual_gating/eval_v8b_ss_s123.log\n  conclusion: success\n  metrics: {\n  \"iid\": {\n    \"gar_ours\": 0.503,\n    \"gar_dongre\": 0.394,\n    \"ppl\": 2.781,\n    \"ntp_loss\": 0.976,\n    \"n_conv\": 50,\n    \"n_turns\": 3\n  },\n  \"modelgen\": {\n    \"gar_ours\": 0.418,\n    \"gar_dongre\": 0.441,\n    \"ppl\": 1.389,\n    \"ntp_loss\": 0.325,\n    \"n_conv\": 5,\n    \"n_turns\": 10\n  },\n  \"gap_ratio\": 1.2,\n  \"base_iid_ppl\": 4.338,\n  \"base_modelgen_ppl\": 1.351\n}\n\n================================================================================\nEXP_ID: p1_tf_ar_kl_divergence\n  status: DONE\n  hypothesis: TF and AR attention distributions diverge more on GAR-relevant heads (high gate values) than non-relevant heads, providing mechanistic evidence that exposure bias selectively disrupts goal-attending computation rather than uniformly degrading attention.\n  metrics: {\n  \"tg_delta_gar\": 0.0165,\n  \"base_delta_gar\": 0.0122,\n  \"tg_mean_kl\": 0.054,\n  \"base_mean_kl\": 0.043,\n  \"gate_kl_correlation\": 0.11,\n  \"high_kl_layers\": \"L23-L27, L9\",\n  \"gar_robustness_ours_tg_base_ratio\": 21.4,\n  \"gar_robustness_goal_only_ratio\": 63,\n  \"gar_robustness_ours_all_ratio\": 1.7,\n  \"gar_robustness_ours_first_ratio\": 1.8\n}\n  spec: {\n  \"command\": \"python scripts/p1_kl_divergence.py\",\n  \"server\": \"westd-20861\",\n  \"data_path\": \"/root/turn_residual_gating/data/eval_200.json\",\n  \"data_count\": 30,\n  \"model_name\": \"Qwen/Qwen2.5-7B-Instruct\",\n  \"seed\": 42,\n  \"checkpoint_path\": \"results/p1_kl_perhead/\",\n  \"log_path\": \"logs/p1_kl_divergence_step2.log\"\n}\n  conclusion: success\n\n================================================================================\nEXP_ID: phase1_gar_diag\n  status: DONE\n  hypothesis: Qwen2.5-7B-Instruct 在 10-turn 多轮对话中，中间 turns (3-8) 的 GAR (Goal Accessibility Ratio) 相对 turn-1 下降 ≥15%，表明模型对 system prompt 中目标 token 的注意力随对话进行显著衰减\n  spec: {\n  \"command\": \"python run_phase1_gar.py --results-dir /root/turn_residual_gating/results\",\n  \"server\": \"westd-20861\",\n  \"model_name\": \"Qwen/Qwen2.5-7B-Instruct\",\n  \"data_path\": \"built-in 5 conversations (knowledge_qa, coding_help, creative_writing, math_reasoning, roleplay_advisor)\",\n  \"data_count\": 5,\n  \"seed\": 0,\n  \"checkpoint_path\": \"N/A\",\n  \"log_path\": \"/root/turn_residual_gating/results/phase1_run.log\"\n}\n  conclusion: success\n  metrics: {\n  \"turn1_avg_gar\": 0.0418,\n  \"mid_turns_avg_gar\": 0.0122,\n  \"relative_drop\": 0.708,\n  \"num_conversations\": 5,\n  \"num_turns\": 10,\n  \"per_turn_avg_gar\": [\n    0.0418,\n    0.0241,\n    0.0224,\n    0.013,\n    0.0133,\n    0.0086,\n    0.0078,\n    0.008,\n    0.0157,\n    0.0064\n  ]\n}\n\n================================================================================\nEXP_ID: eval_llama_lora_only_s42\n  status: DONE\n  hypothesis: LoRA-only ablation (no gate) on Llama-3.1-8B: if TG's GAR improvement comes from the gate, LoRA-only should show minimal GAR recovery vs base.\n  parent: llama_lora_only_s42\n  spec: {\n  \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/turn_residual_gating && bash scripts/eval_llama_lora_only_s42.sh\\\"\",\n  \"server\": \"westd-20861\",\n  \"gpu\": [\n    \"cuda:0\"\n  ],\n  \"pid\": \"309670\",\n  \"log_path\": \"/root/runs/turn_residual_gating/eval_llama_lora_only_s42.log\",\n  \"submitted_at\": \"2026-05-22T07:40:34.437Z\",\n  \"submitted_via\": \"submit_training_job\",\n  \"backend\": \"tmux\",\n  \"account\": \"root\",\n  \"data_path\": \"ultrachat_200k + model-gen\",\n  \"data_count\": 55,\n  \"model_name\": \"Llama-3.1-8B-Instruct + LoRA-only checkpoint\",\n  \"seed\": 42,\n  \"checkpoint_source\": \"llama_lora_only_s42\",\n  \"eval_data\": \"IID heldout 50 + model-gen 5\",\n  \"checkpoint_path\": \"runs/phase2_llama_lora_only_s42/epoch_2\",\n  \"wall_clock_seconds\": 650.8,\n  \"gpu_hours\": 0.18\n}\n  reproduce: {\n  \"finished_at\": \"2026-05-22T07:45:28.637Z\"\n}\n  extra: {\n  \"hook_events\": [\n    {\n      \"event\": \"on_complete\",\n      \"action\": \"agent\",\n      \"ts\": \"2026-05-22T07:45:30.556207+00:00\"\n    }\n  ]\n}\n  metrics: {\n  \"tf\": {\n    \"gar_ours\": 0.4807,\n    \"gar_dongre\": 0.0188,\n    \"ngar_ours\": 11.8031,\n    \"ngar_dongre\": 0.8261,\n    \"ppl\": 2.6,\n    \"ntp_loss\": 0.9366,\n    \"n_conversations\": 50,\n    \"n_turns\": 4\n  },\n  \"ar\": {\n    \"gar_ours\": 0.0617,\n    \"gar_dongre\": 0.0226,\n    \"ngar_ours\": 0.6065,\n    \"ngar_dongre\": 0.2537,\n    \"ppl\": 1.32,\n    \"ntp_loss\": 0.2787,\n    \"n_conversations\": 5,\n    \"n_turns\": 10\n  },\n  \"gap_ratio_gar_ours\": 7.79\n}\n  conclusion: success",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "0210d68f-54b0-430c-9b11-8efd21ad23f8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "4b680861-4da7-411a-8744-3dabfdaf2205",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 72 · 2026-05-25T20:39:46.282Z_

<details open><summary>🔧 Tool call — Read · `toolu_01QksKobQm4tH24WB5hYTdJc`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/_project/paper/tab_dataset_stats.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0c0a69fc-6734-4da5-8f7b-e1e3af1ae799",
  "isSidechain": false,
  "requestId": "req_011CbPw3o6aiFR6Gd4Pgx6mb",
  "type": "assistant",
  "uuid": "b5a07373-f5ce-4b01-977b-7809e694bc87",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "4b680861-4da7-411a-8744-3dabfdaf2205",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NYKDdLXk5EQoSMQqRF9m3d",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8028,
      "cache_read_input_tokens": 44883,
      "output_tokens": 1105,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 8028,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1105,
          "cache_read_input_tokens": 44883,
          "cache_creation_input_tokens": 8028,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 8028
          },
          "type": "message"
        }
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

_source line 73 · 2026-05-25T20:39:46.289Z_

<details><summary>↩ Tool result · `toolu_01QksKobQm4tH24WB5hYTdJc`</summary>

```text
1	% Dataset statistics table
2	\begin{table}[t]
3	\centering
4	\small
5	\caption{Dataset statistics. Training and evaluation data are sampled from UltraChat-200K~\citep{ding2023enhancing}. All conversations contain $\geq 5$ assistant turns.}
6	\label{tab:dataset_stats}
7	\begin{tabular}{@{}lr@{}}
8	\toprule
9	\textbf{Statistic} & \textbf{Value} \\
10	\midrule
11	\multicolumn{2}{@{}l}{\textit{Source}} \\
12	\quad Dataset & UltraChat-200K (\texttt{train\_sft}) \\
13	\quad Total conversations & 207{,}865 \\
14	\quad After filtering ($\geq 5$ asst.\ turns) & 17{,}302 \\
15	\midrule
16	\multicolumn{2}{@{}l}{\textit{Splits}} \\
17	\quad Training set & 8{,}000 \\
18	\quad Held-out eval (OOD) & 50 \\
19	\quad IID eval (GAR diagnostic) & 50 \\
20	\quad Large eval (instruction retention) & 200 \\
21	\midrule
22	\multicolumn{2}{@{}l}{\textit{Conversation structure}} \\
23	\quad Avg.\ assistant turns & 5.6 \\
24	\quad Min / Max assistant turns & 5 / 7 \\
25	\bottomrule
26	\end{tabular}
27	\end{table}
28	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b5a07373-f5ce-4b01-977b-7809e694bc87",
  "isSidechain": false,
  "promptId": "8817af8a-f189-44e8-a462-1453a12b4ea3",
  "type": "user",
  "uuid": "607b21ab-017d-4d5e-b0e5-1263dba42914",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/_project/paper/tab_dataset_stats.tex",
      "content": "% Dataset statistics table\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Dataset statistics. Training and evaluation data are sampled from UltraChat-200K~\\citep{ding2023enhancing}. All conversations contain $\\geq 5$ assistant turns.}\n\\label{tab:dataset_stats}\n\\begin{tabular}{@{}lr@{}}\n\\toprule\n\\textbf{Statistic} & \\textbf{Value} \\\\\n\\midrule\n\\multicolumn{2}{@{}l}{\\textit{Source}} \\\\\n\\quad Dataset & UltraChat-200K (\\texttt{train\\_sft}) \\\\\n\\quad Total conversations & 207{,}865 \\\\\n\\quad After filtering ($\\geq 5$ asst.\\ turns) & 17{,}302 \\\\\n\\midrule\n\\multicolumn{2}{@{}l}{\\textit{Splits}} \\\\\n\\quad Training set & 8{,}000 \\\\\n\\quad Held-out eval (OOD) & 50 \\\\\n\\quad IID eval (GAR diagnostic) & 50 \\\\\n\\quad Large eval (instruction retention) & 200 \\\\\n\\midrule\n\\multicolumn{2}{@{}l}{\\textit{Conversation structure}} \\\\\n\\quad Avg.\\ assistant turns & 5.6 \\\\\n\\quad Min / Max assistant turns & 5 / 7 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n",
      "numLines": 28,
      "startLine": 1,
      "totalLines": 28
    }
  },
  "sourceToolAssistantUUID": "b5a07373-f5ce-4b01-977b-7809e694bc87",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "4b680861-4da7-411a-8744-3dabfdaf2205",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 74 · 2026-05-25T20:39:47.237Z_

<details open><summary>🔧 Tool call — Read · `toolu_014vSbzRsE4zo7PaM8RYNDAN`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/_project/paper/tab_gar_robustness.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "607b21ab-017d-4d5e-b0e5-1263dba42914",
  "isSidechain": false,
  "requestId": "req_011CbPw3o6aiFR6Gd4Pgx6mb",
  "type": "assistant",
  "uuid": "67b98b20-42b4-4dc5-9541-85c049da6dd8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "4b680861-4da7-411a-8744-3dabfdaf2205",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NYKDdLXk5EQoSMQqRF9m3d",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8028,
      "cache_read_input_tokens": 44883,
      "output_tokens": 1105,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 8028,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1105,
          "cache_read_input_tokens": 44883,
          "cache_creation_input_tokens": 8028,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 8028
          },
          "type": "message"
        }
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

_source line 75 · 2026-05-25T20:39:47.242Z_

<details><summary>↩ Tool result · `toolu_014vSbzRsE4zo7PaM8RYNDAN`</summary>

```text
1	% GAR definition robustness: 4 token selection strategies x 3 conditions
2	\begin{table}[t]
3	\centering
4	\small
5	\caption{GAR robustness across token selection strategies. We evaluate four ways to select the token position for gradient attribution: \textbf{Last} (final token of each turn), \textbf{All} (mean over all tokens), \textbf{First} (first token), and \textbf{Goal-only} (goal token as in \citet{dongre2024multi}). Turn-1 and Mid-turn GAR are measured under autoregressive generation on 50 held-out conversations. Gap Ratio = Turn-1 / Mid-turn; lower indicates better gradient preservation across turns.}
6	\label{tab:gar_robustness}
7	\begin{tabular}{@{}ll ccc@{}}
8	\toprule
9	\textbf{Token Selection} & \textbf{Condition} & \textbf{Turn-1 GAR} & \textbf{Mid-turn GAR} & \textbf{Gap Ratio} $\downarrow$ \\
10	\midrule
11	\multirow{3}{*}{Last (ours)}
12	  & Base      & 0.0858 & 0.0152 & 5.64$\times$ \\
13	  & TG        & 0.3938 & 0.3254 & 1.21$\times$ \\
14	  & SS        & 0.5274 & 0.4582 & 1.15$\times$ \\
15	\midrule
16	\multirow{3}{*}{All tokens}
17	  & Base      & 0.1152 & 0.0152 & 7.57$\times$ \\
18	  & TG        & 0.1275 & 0.0253 & 5.04$\times$ \\
19	  & SS        & 0.5043 & 0.3658 & 1.38$\times$ \\
20	\midrule
21	\multirow{3}{*}{First token}
22	  & Base      & 0.2987 & 0.0224 & 13.32$\times$ \\
23	  & TG        & 0.3225 & 0.0392 & 8.24$\times$ \\
24	  & SS        & 0.7549 & 0.4118 & 1.83$\times$ \\
25	\midrule
26	\multirow{3}{*}{Goal-only}
27	  & Base      & 0.0110 & 0.0049 & 2.23$\times$ \\
28	  & TG        & 0.3313 & 0.3103 & 1.07$\times$ \\
29	  & SS        & 0.4528 & 0.4435 & 1.02$\times$ \\
30	\bottomrule
31	\end{tabular}
32	\end{table}
33	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "67b98b20-42b4-4dc5-9541-85c049da6dd8",
  "isSidechain": false,
  "promptId": "8817af8a-f189-44e8-a462-1453a12b4ea3",
  "type": "user",
  "uuid": "456009a6-cdb4-4b51-969c-bb5cd87052f4",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/_project/paper/tab_gar_robustness.tex",
      "content": "% GAR definition robustness: 4 token selection strategies x 3 conditions\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{GAR robustness across token selection strategies. We evaluate four ways to select the token position for gradient attribution: \\textbf{Last} (final token of each turn), \\textbf{All} (mean over all tokens), \\textbf{First} (first token), and \\textbf{Goal-only} (goal token as in \\citet{dongre2024multi}). Turn-1 and Mid-turn GAR are measured under autoregressive generation on 50 held-out conversations. Gap Ratio = Turn-1 / Mid-turn; lower indicates better gradient preservation across turns.}\n\\label{tab:gar_robustness}\n\\begin{tabular}{@{}ll ccc@{}}\n\\toprule\n\\textbf{Token Selection} & \\textbf{Condition} & \\textbf{Turn-1 GAR} & \\textbf{Mid-turn GAR} & \\textbf{Gap Ratio} $\\downarrow$ \\\\\n\\midrule\n\\multirow{3}{*}{Last (ours)}\n  & Base      & 0.0858 & 0.0152 & 5.64$\\times$ \\\\\n  & TG        & 0.3938 & 0.3254 & 1.21$\\times$ \\\\\n  & SS        & 0.5274 & 0.4582 & 1.15$\\times$ \\\\\n\\midrule\n\\multirow{3}{*}{All tokens}\n  & Base      & 0.1152 & 0.0152 & 7.57$\\times$ \\\\\n  & TG        & 0.1275 & 0.0253 & 5.04$\\times$ \\\\\n  & SS        & 0.5043 & 0.3658 & 1.38$\\times$ \\\\\n\\midrule\n\\multirow{3}{*}{First token}\n  & Base      & 0.2987 & 0.0224 & 13.32$\\times$ \\\\\n  & TG        & 0.3225 & 0.0392 & 8.24$\\times$ \\\\\n  & SS        & 0.7549 & 0.4118 & 1.83$\\times$ \\\\\n\\midrule\n\\multirow{3}{*}{Goal-only}\n  & Base      & 0.0110 & 0.0049 & 2.23$\\times$ \\\\\n  & TG        & 0.3313 & 0.3103 & 1.07$\\times$ \\\\\n  & SS        & 0.4528 & 0.4435 & 1.02$\\times$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n",
      "numLines": 33,
      "startLine": 1,
      "totalLines": 33
    }
  },
  "sourceToolAssistantUUID": "67b98b20-42b4-4dc5-9541-85c049da6dd8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "4b680861-4da7-411a-8744-3dabfdaf2205",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 76 · 2026-05-25T20:39:47.637Z_

<details open><summary>🔧 Tool call — Read · `toolu_01GNzgB8AFN8R5PY7b2Sd12a`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/_project/paper/tab_mmlu_detail.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "456009a6-cdb4-4b51-969c-bb5cd87052f4",
  "isSidechain": false,
  "requestId": "req_011CbPw3o6aiFR6Gd4Pgx6mb",
  "type": "assistant",
  "uuid": "1dfcd076-9656-4c7d-9e8c-d2311dffe470",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "4b680861-4da7-411a-8744-3dabfdaf2205",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NYKDdLXk5EQoSMQqRF9m3d",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8028,
      "cache_read_input_tokens": 44883,
      "output_tokens": 1105,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 8028,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1105,
          "cache_read_input_tokens": 44883,
          "cache_creation_input_tokens": 8028,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 8028
          },
          "type": "message"
        }
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

_source line 77 · 2026-05-25T20:39:47.645Z_

<details><summary>↩ Tool result · `toolu_01GNzgB8AFN8R5PY7b2Sd12a`</summary>

```text
1	% MMLU per-category quality preservation table
2	\begin{table}[t]
3	\centering
4	\small
5	\caption{MMLU accuracy (\%) by category across training conditions. All models are Qwen2.5-7B-Instruct with LoRA adapters evaluated on the full 57-subject MMLU benchmark (14{,}042 questions). $\Delta$ denotes deviation from Base.}
6	\label{tab:mmlu_detail}
7	\begin{tabular}{@{}l cccccc@{}}
8	\toprule
9	\textbf{Category} & \textbf{Base} & \textbf{TG} & \textbf{PCGrad} & \textbf{SS} & \textbf{LoRA-only} & \textbf{UG} \\
10	\midrule
11	STEM           & 70.69 & 69.20 & 69.55 & 69.97 & 70.03 & 69.65 \\
12	Social Sciences & 77.28 & 76.92 & 76.79 & 76.83 & 77.08 & 77.02 \\
13	Humanities     & 83.95 & 83.33 & 84.08 & 83.39 & 83.62 & 83.95 \\
14	Other          & 68.25 & 67.59 & 68.12 & 67.95 & 67.06 & 66.80 \\
15	\midrule
16	\textbf{Overall} & \textbf{74.23} & 73.47 & 73.86 & 73.75 & 73.57 & 73.46 \\
17	$\Delta$ & --- & $-$0.76 & $-$0.37 & $-$0.48 & $-$0.66 & $-$0.77 \\
18	\bottomrule
19	\end{tabular}
20	\end{table}
21	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1dfcd076-9656-4c7d-9e8c-d2311dffe470",
  "isSidechain": false,
  "promptId": "8817af8a-f189-44e8-a462-1453a12b4ea3",
  "type": "user",
  "uuid": "eb6b0aba-7932-4206-8190-2ea7d5eac036",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/_project/paper/tab_mmlu_detail.tex",
      "content": "% MMLU per-category quality preservation table\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{MMLU accuracy (\\%) by category across training conditions. All models are Qwen2.5-7B-Instruct with LoRA adapters evaluated on the full 57-subject MMLU benchmark (14{,}042 questions). $\\Delta$ denotes deviation from Base.}\n\\label{tab:mmlu_detail}\n\\begin{tabular}{@{}l cccccc@{}}\n\\toprule\n\\textbf{Category} & \\textbf{Base} & \\textbf{TG} & \\textbf{PCGrad} & \\textbf{SS} & \\textbf{LoRA-only} & \\textbf{UG} \\\\\n\\midrule\nSTEM           & 70.69 & 69.20 & 69.55 & 69.97 & 70.03 & 69.65 \\\\\nSocial Sciences & 77.28 & 76.92 & 76.79 & 76.83 & 77.08 & 77.02 \\\\\nHumanities     & 83.95 & 83.33 & 84.08 & 83.39 & 83.62 & 83.95 \\\\\nOther          & 68.25 & 67.59 & 68.12 & 67.95 & 67.06 & 66.80 \\\\\n\\midrule\n\\textbf{Overall} & \\textbf{74.23} & 73.47 & 73.86 & 73.75 & 73.57 & 73.46 \\\\\n$\\Delta$ & --- & $-$0.76 & $-$0.37 & $-$0.48 & $-$0.66 & $-$0.77 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n",
      "numLines": 21,
      "startLine": 1,
      "totalLines": 21
    }
  },
  "sourceToolAssistantUUID": "1dfcd076-9656-4c7d-9e8c-d2311dffe470",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "4b680861-4da7-411a-8744-3dabfdaf2205",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 78 · 2026-05-25T20:39:48.015Z_

<details open><summary>🔧 Tool call — Read · `toolu_011tWV1iaP53N55YnLRwws9h`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/_project/paper/tab_qwen15b_results.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "eb6b0aba-7932-4206-8190-2ea7d5eac036",
  "isSidechain": false,
  "requestId": "req_011CbPw3o6aiFR6Gd4Pgx6mb",
  "type": "assistant",
  "uuid": "0f572d96-c61a-4ae3-9248-90c4fedc5d29",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "4b680861-4da7-411a-8744-3dabfdaf2205",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NYKDdLXk5EQoSMQqRF9m3d",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8028,
      "cache_read_input_tokens": 44883,
      "output_tokens": 1105,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 8028,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1105,
          "cache_read_input_tokens": 44883,
          "cache_creation_input_tokens": 8028,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 8028
          },
          "type": "message"
        }
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

_source line 79_

```json
{
  "type": "last-prompt",
  "leafUuid": "d6a785e4-f2b5-4078-9758-0c1d0d1c519e",
  "sessionId": "4b680861-4da7-411a-8744-3dabfdaf2205"
}
```

---

### Runtime record

_source line 80_

```json
{
  "type": "ai-title",
  "aiTitle": "Audit quantitative claims in paper body text",
  "sessionId": "4b680861-4da7-411a-8744-3dabfdaf2205"
}
```

---

### Assistant

_source line 81 · 2026-05-25T20:39:53.350Z_

<details><summary>Logged reasoning block</summary>

```text
Good, now I have a comprehensive view of the registry data. Let me also get the remaining experiment data I need. Let me now look at the remaining experiments for Llama data and the statistical tests.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d6a785e4-f2b5-4078-9758-0c1d0d1c519e",
  "isSidechain": false,
  "requestId": "req_011CbPw5UjaveKtywQJhNBGc",
  "type": "assistant",
  "uuid": "650bd0ae-54b6-4be0-8f32-a5ac963fe0a8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "4b680861-4da7-411a-8744-3dabfdaf2205",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01F5brtjM7qivBRdZpAwLB3J",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 15079,
      "cache_read_input_tokens": 52911,
      "output_tokens": 607,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 15079,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 607,
          "cache_read_input_tokens": 52911,
          "cache_creation_input_tokens": 15079,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 15079
          },
          "type": "message"
        }
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

_source line 82 · 2026-05-25T20:39:54.342Z_

Now let me get the remaining key experiment data, particularly for Llama and statistical tests.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "650bd0ae-54b6-4be0-8f32-a5ac963fe0a8",
  "isSidechain": false,
  "requestId": "req_011CbPw5UjaveKtywQJhNBGc",
  "type": "assistant",
  "uuid": "44094289-df28-4de3-a06d-6b30384c4db0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "4b680861-4da7-411a-8744-3dabfdaf2205",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01F5brtjM7qivBRdZpAwLB3J",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 15079,
      "cache_read_input_tokens": 52911,
      "output_tokens": 607,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 15079,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 607,
          "cache_read_input_tokens": 52911,
          "cache_creation_input_tokens": 15079,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 15079
          },
          "type": "message"
        }
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

_source line 83 · 2026-05-25T20:40:05.269Z_

<details open><summary>🔧 Tool call — Bash · `toolu_0186WLGXYZF1Qk4iKE4ekA9S`</summary>

```json
{
  "command": "python3 << 'PYEOF'\nimport json, sys\n\nREGISTRY = \"/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-11-projects-turn-residual-gating/4b680861-4da7-411a-8744-3dabfdaf2205/tool-results/mcp-agent-ml-research-read_registry-1779741484333.txt\"\ndata = json.load(open(REGISTRY))\nresult = json.loads(data['result'])\nexperiments = result['data']['experiments']\n\nremaining = [\n    'llama_eval_s42', 'llama_tg_s42', 'llama_lora_only_s42',\n    'eval_llama_ar_n20', 'p1_llama_ss_eval', 'p1_llama_ss_training',\n    'llama_ar_matched_eval',\n    'v7_tg_s123', 'd048_ss_s42', 'd048_ss_s123', 'd048_ss_s456',\n    'phase2_4way_eval', 'phase2_4way_eval_heldout',\n    'attention_steering_eval200_tf',\n]\n\nfor eid in remaining:\n    if eid in experiments:\n        exp = experiments[eid]\n        metrics = exp.get('metrics')\n        notes = exp.get('notes')\n        if metrics or notes:\n            print(f\"\\n{'='*80}\")\n            print(f\"EXP_ID: {eid}\")\n            if metrics:\n                print(f\"METRICS: {json.dumps(metrics, indent=2)[:3000]}\")\n            if notes:\n                print(f\"NOTES: {notes[:2000]}\")\nPYEOF\n",
  "description": "Extract remaining experiment metrics",
  "timeout": 30000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "44094289-df28-4de3-a06d-6b30384c4db0",
  "isSidechain": false,
  "requestId": "req_011CbPw5UjaveKtywQJhNBGc",
  "type": "assistant",
  "uuid": "060b7175-09da-4baf-9d80-60581353d4e2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "4b680861-4da7-411a-8744-3dabfdaf2205",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01F5brtjM7qivBRdZpAwLB3J",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 15079,
      "cache_read_input_tokens": 52911,
      "output_tokens": 607,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 15079,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 607,
          "cache_read_input_tokens": 52911,
          "cache_creation_input_tokens": 15079,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 15079
          },
          "type": "message"
        }
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

_source line 84 · 2026-05-25T20:40:05.342Z_

<details><summary>↩ Tool result · `toolu_0186WLGXYZF1Qk4iKE4ekA9S`</summary>

```text
================================================================================
EXP_ID: llama_eval_s42
METRICS: {
  "tf_base": {
    "gar_ours": 0.0166,
    "ngar_ours": 0.3882,
    "gar_dongre": 0.0038,
    "ngar_dongre": 0.163,
    "ppl": 3.45,
    "N": 50,
    "T": 4
  },
  "tf_tg": {
    "gar_ours": 0.4836,
    "ngar_ours": 11.8818,
    "gar_dongre": 0.018,
    "ngar_dongre": 0.7922,
    "ppl": 2.57,
    "N": 50,
    "T": 4
  },
  "ar_base": {
    "gar_ours": 0.0086,
    "ngar_ours": 0.0798,
    "gar_dongre": 0.0118,
    "ngar_dongre": 0.1265,
    "ppl": 1.24,
    "N": 5,
    "T": 10
  },
  "ar_tg": {
    "gar_ours": 0.0304,
    "ngar_ours": 0.2632,
    "gar_dongre": 0.0217,
    "ngar_dongre": 0.2459,
    "ppl": 1.32,
    "N": 5,
    "T": 10
  },
  "gap_ratio_tg_ours": 15.9,
  "gap_ratio_base_ours": 1.93,
  "gap_ratio_tg_dongre": 0.83,
  "vs_qwen_v7_gap_ratio": 32.1,
  "baseline_mid_gar": 0.0122
}
NOTES: C5 跨模型泛化确认。Llama TG GAR-ours gap 16x (TF 0.484 vs AR 0.030)，低于 Qwen v7 的 32x 但仍非常显著。Base model gap 仅 1.9x（control 通过）。注意 TF/AR eval 设定不同 (N=50/T=4 vs N=5/T=10)，可能影响绝对值对比。GAR-dongre 无明显 gap (ratio 0.83x, AR ≥ TF)，仅 GAR-ours 展现 exposure bias 效应。Gate dynamic range: L24/L28/L30 diff 最大 (0.23-0.38)，与 Qwen 类似集中在中高层。

================================================================================
EXP_ID: llama_tg_s42
METRICS: {
  "epochs_completed": 3,
  "total_steps": 3000,
  "wall_clock_seconds": 26212,
  "wall_clock_hours": 7.28,
  "final_avg_loss": 0.9233,
  "final_avg_ntp": 0.9224,
  "final_avg_gar": 0.0009,
  "final_avg_div": 0,
  "final_gate_mean": 0.9099,
  "final_gate_std": 0.0701,
  "final_gate_min": 0.7188,
  "final_gate_max": 0.9922,
  "gate_profile_step3000": {
    "L0": 0.957,
    "L1": 0.973,
    "L2": 0.977,
    "L3": 0.965,
    "L4": 0.992,
    "L5": 0.969,
    "L6": 0.957,
    "L7": 0.957,
    "L8": 0.961,
    "L9": 0.949,
    "L10": 0.938,
    "L11": 0.934,
    "L12": 0.969,
    "L13": 0.953,
    "L14": 0.957,
    "L15": 0.965,
    "L16": 0.953,
    "L17": 0.961,
    "L18": 0.922,
    "L19": 0.902,
    "L20": 0.883,
    "L21": 0.863,
    "L22": 0.836,
    "L23": 0.844,
    "L24": 0.809,
    "L25": 0.719,
    "L26": 0.762,
    "L27": 0.805,
    "L28": 0.801,
    "L29": 0.855,
    "L30": 0.898,
    "L31": 0.934
  },
  "checkpoint_size_gate_mb": 4.2,
  "checkpoint_size_lora_mb": 26,
  "gpu": "NVIDIA RTX PRO 6000 Blackwell",
  "vram_gb": 102,
  "mem_used_gb": 63.4
}

================================================================================
EXP_ID: llama_lora_only_s42
METRICS: {
  "final_avg_loss": 0.9288,
  "final_avg_ntp": 0.9279,
  "final_avg_gar": 0.0009,
  "gate_fixed": 1,
  "gate_type": "none",
  "wall_clock_s": 25317,
  "wall_clock_h": 7.03,
  "epochs_completed": 3
}

================================================================================
EXP_ID: eval_llama_ar_n20
METRICS: {
  "base": {
    "gar_ours_mean": 0.0088,
    "gar_ours_std": 0.0056,
    "gar_ours_median_per_conv": 0.0093,
    "gar_ours_median_per_turn_pool": 0.0071,
    "gar_ours_spike_ratio": "0%",
    "gar_dongre_mean": 0.0049,
    "gar_dongre_std": 0.0013,
    "gar_dongre_median": 0.0047,
    "ngar_ours_mid": 0.1019,
    "ngar_dongre_mid": 0.1171,
    "ppl": 1.293,
    "ppl_std": 0.07,
    "ntp_loss": 0.2552
  },
  "tg": {
    "gar_ours_mean": 0.0434,
    "gar_ours_std": 0.1002,
    "gar_ours_median_per_conv": 0.0179,
    "gar_ours_median_per_turn_pool": 0.0126,
    "gar_ours_spike_ratio": "5% (2/40 turns GAR>=0.4)",
    "gar_dongre_mean": 0.0183,
    "gar_dongre_std": 0.0198,
    "gar_dongre_median": 0.0152,
    "ngar_ours_mid": 0.5357,
    "ngar_dongre_mid": 0.4436,
    "ppl": 1.437,
    "ppl_std": 0.077,
    "ntp_loss": 0.3612
  },
  "lora_only": {
    "gar_ours_mean": 0.0284,
    "gar_ours_std": 0.0481,
    "gar_ours_median_per_conv": 0.0184,
    "gar_ours_median_per_turn_pool": 0.0133,
    "gar_ours_spike_ratio": "0%",
    "gar_dongre_mean": 0.0205,
    "gar_dongre_std": 0.0241,
    "gar_dongre_median": 0.016,
    "ngar_ours_mid": 0.3488,
    "ngar_dongre_mid": 0.4997,
    "ppl": 1.419,
    "ppl_std": 0.075,
    "ntp_loss": 0.3483
  },
  "n_conversations": 20,
  "n_turns": 4,
  "mid_turns_definition": "turns 3-T (0-indexed avg_gar[2:], excluding turns 1-2). All 16 eval entries use same definition.",
  "stat_pool": "median_per_conv: median of 20 per-conversation mid-turn averages. median_per_turn_pool: median of 40 individual turn values (20 conv x 2 mid turns).",
  "ranking_gar_ours_mean": "TG(0.0434) > LO(0.0284) > Base(0.0088)",
  "ranking_gar_ours_median_per_conv": "TG(0.0179) \u2248 LO(0.0184) > Base(0.0093)",
  "ranking_gar_ours_median_per_turn_pool": "TG(0.0126) \u2248 LO(0.0133) > Base(0.0071)",
  "ranking_gar_dongre": "LO(0.0205) > TG(0.0183) > Base(0.0049)",
  "note": "Paper \u00a75.5 cites median_per_conv (median of per-conversation mid-turn averages across N=20). median_per_turn_pool is the alternative statistic from pooled individual turns. Both confirm TG \u2248 LO (zero-increment)."
}
NOTES: N=20 AR eval stabilizes estimates. **mid_turns = turns 3-T (0-indexed avg_gar[2:], excluding turns 1-2; all 16 eval entries use same definition)**. Two median levels: median_per_conv (paper §5.5 cites this: TG 0.0179, LO 0.0184, Base 0.0093) = median of 20 per-conversation mid-turn averages; median_per_turn_pool (TG 0.0126, LO 0.0133, Base 0.0071) = median of 40 pooled individual turns. Both confirm TG ≈ LO (zero-increment). Mean (TG 0.0434 > LO 0.0284) driven by outlier spikes (TG std=0.1002, 5% turns GAR≥0.4; LO std=0.0481, 0% spikes). PPL: Base(1.29) < LO(1.42) < TG(1.44). Pending paper fix: §5.5 says "turns 2-T" but code excludes turns 1-2; will correct to "excluding the first two turns" in next paper edit batch.

================================================================================
EXP_ID: p1_llama_ss_eval
METRICS: {
  "ss_tf_gar": 0.477,
  "ss_tf_ppl": 2.82,
  "ss_ar_b0_gar": 0.1662,
  "ss_ar_b0_ppl": 1.37,
  "ss_ar_b5_gar": 0.7905,
  "ss_ar_b5_ppl": 1.81,
  "base_ar_gar": 0.0179,
  "base_ar_ppl": 1.22,
  "tf_ar_gap": 2.87
}

================================================================================
EXP_ID: llama_ar_matched_eval
METRICS: {
  "ar_base_ours": {
    "mid_gar": 0.0082,
    "ngar": 0.1,
    "ppl": 1.267
  },
  "ar_tg_ours": {
    "mid_gar": 0.0388,
    "ngar": 0.493,
    "ppl": 1.413
  },
  "ar_base_dongre": {
    "mid_gar": 0.0051,
    "ngar": 0.12,
    "ppl": 1.267
  },
  "ar_tg_dongre": {
    "mid_gar": 0.018,
    "ngar": 0.431,
    "ppl": 1.413
  },
  "tf_reference": {
    "tf_tg_ours_ngar": 11.88,
    "tf_base_ours_ngar": 0.388,
    "tf_tg_ours_raw": 0.4836,
    "tf_tg_dongre_raw": 0.018
  },
  "matched_gap_analysis": {
    "gar_ours_raw_gap": "12.5x (TF 0.484 / AR 0.039)",
    "gar_ours_ngar_gap": "24.1x (TF 11.88 / AR 0.493)",
    "gar_dongre_raw_gap": "1.002x (TF 0.018 / AR 0.018) \u2014 zero gap",
    "tg_over_base_ar_ours": "4.71x",
    "tg_over_base_ar_dongre": "3.54x",
    "conclusion": "GAR-ours TF-AR gap 12.5x (raw) / 24x (nGAR) is genuine exposure bias. GAR-Dongre zero gap (1.002x) confirms mechanism specificity: exposure bias selectively destroys learned goal-attention routing while leaving content-overlap-based attention unaffected."
  }
}
NOTES: CORRECTION (2026-05-21 04:36): Agent 之前错误地将 AR TG nGAR (0.493) 与 TF TG raw GAR (0.484) 对比，误判为 'nGAR aligns, gap is normalization artifact'。Reviewer 核实：TF TG ours nGAR = 11.88（非 0.48）。nGAR gap = 11.88 / 0.493 = 24.1×，比 raw gap (12.5×) 还大。'Normalization artifact' 分析完全错误——GAR-ours 的 gap 是真实的 exposure bias。论文绝对不能使用 normalization artifact 叙事。

================================================================================
EXP_ID: v7_tg_s123
METRICS: {
  "epoch_1": {
    "avg_loss": 0.9447,
    "avg_ntp_loss": 0.9434,
    "avg_gar_loss": 0.0013,
    "avg_div_loss": 0
  },
  "epoch_2": {
    "avg_loss": 0.9315,
    "avg_ntp_loss": 0.9305,
    "avg_gar_loss": 0.001,
    "avg_div_loss": 0
  },
  "final_gate": {
    "mean": 0.9467,
    "std": 0.051,
    "min": 0.793,
    "max": 1
  },
  "final_gate_profile": {
    "L0": 0.883,
    "L1": 0.793,
    "L2": 0.996,
    "L3": 0.988,
    "L4": 0.984,
    "L5": 0.797,
    "L6": 0.961,
    "L7": 0.918,
    "L8": 0.965,
    "L9": 0.934,
    "L10": 0.969,
    "L11": 0.918,
    "L12": 0.926,
    "L13": 0.941,
    "L14": 0.93,
    "L15": 0.965,
    "L16": 0.941,
    "L17": 0.91,
    "L18": 0.961,
    "L19": 0.965,
    "L20": 0.973,
    "L21": 0.988,
    "L22": 0.969,
    "L23": 0.98,
    "L24": 0.98,
    "L25": 0.984,
    "L26": 0.988,
    "L27": 1
  },
  "training_time_s": 21425.2
}

================================================================================
EXP_ID: d048_ss_s42
METRICS: {
  "final_avg_loss": 0.9326,
  "final_ntp_loss": 0.932,
  "final_gar_loss": 0.0007,
  "gate_mean": 0.9527,
  "gate_std": 0.0589,
  "gate_min": 0.7383,
  "gate_min_layer": "L4",
  "gate_max": 1,
  "ss_usage": "4750/16000 (29.7%)",
  "ss_fallback": 0,
  "epochs_completed": 3,
  "wall_clock_s": 23418,
  "wall_clock_h": 6.5
}
NOTES: Training complete (resume v3). 23418s (6.5h) for epoch 1+2. Final: Avg Loss=0.9326, NTP=0.9320, GAR=0.0007, DIV=0.0000. Gate: mean=0.9527, std=0.0589, min=0.7383(L4), max=1.000. SS: 4750/16000 (29.7%) used, 0 fallback. Checkpoints: epoch_0, epoch_1, epoch_2, final. Gate profile consistent with prior SS runs (L4 lowest).

================================================================================
EXP_ID: phase2_4way_eval
METRICS: {
  "base_ours_mid_gar": 0.0107,
  "base_ours_recovery_pp": -0.15,
  "base_dongre_mid_gar": 0.003,
  "base_dongre_recovery_pp": -0.92,
  "base_ppl": 4.23,
  "base_ntp": 1.4162,
  "tg_ours_mid_gar": 0.4866,
  "tg_ours_recovery_pp": 47.44,
  "tg_dongre_mid_gar": 0.0157,
  "tg_dongre_recovery_pp": 0.35,
  "tg_ppl": 2.63,
  "tg_ntp": 0.9484,
  "ug_ours_mid_gar": 0.4923,
  "ug_ours_recovery_pp": 48.01,
  "ug_dongre_mid_gar": 0.013,
  "ug_dongre_recovery_pp": 0.08,
  "ug_ppl": 2.62,
  "ug_ntp": 0.9433,
  "lora_ours_mid_gar": 0.486,
  "lora_ours_recovery_pp": 47.39,
  "lora_dongre_mid_gar": 0.0137,
  "lora_dongre_recovery_pp": 0.15,
  "lora_ppl": 2.63,
  "lora_ntp": 0.9482,
  "route_b_confirmed": true,
  "gating_incremental_benefit": "none"
}
NOTES: 四路 eval 完成，Route B 决定性确认。三种训练方法（TG/UG/LoRA-only）在推理端完全趋同：ours GAR recovery ~47-48pp（vs base -0.15pp），dongre GAR recovery 0.08-0.35pp，PPL 2.62-2.63，NTP 0.943-0.948。Gating 机制（无论 turn-conditioned 还是 uniform）相比纯 LoRA 微调零增量。LoRA fine-tuning 是 GAR recovery 的唯一来源。hypothesis 被证伪：TRG 不比 LoRA-only 更好。

================================================================================
EXP_ID: phase2_4way_eval_heldout
METRICS: {
  "base_ours_mid_gar": 0.0128,
  "base_ours_recovery_pp": 0.06,
  "base_dongre_mid_gar": 0.0031,
  "base_dongre_recovery_pp": -0.91,
  "base_ppl": 4.34,
  "base_ntp": 1.4045,
  "tg_ours_mid_gar": 0.5035,
  "tg_ours_recovery_pp": 49.13,
  "tg_dongre_mid_gar": 0.0152,
  "tg_dongre_recovery_pp": 0.3,
  "tg_ppl": 2.78,
  "tg_ntp": 0.9771,
  "ug_ours_mid_gar": 0.5053,
  "ug_ours_recovery_pp": 49.31,
  "ug_dongre_mid_gar": 0.0124,
  "ug_dongre_recovery_pp": 0.02,
  "ug_ppl": 2.78,
  "ug_ntp": 0.9752,
  "lora_ours_mid_gar": 0.4978,
  "lora_ours_recovery_pp": 48.56,
  "lora_dongre_mid_gar": 0.0132,
  "lora_dongre_recovery_pp": 0.1,
  "lora_ppl": 2.78,
  "lora_ntp": 0.9771,
  "three_way_convergence_confirmed": true,
  "gar_ours_spread_pp": 0.75,
  "ppl_spread": 0,
  "data_overlap": false
}
NOTES: Held-out eval 三路趋同完全复现。TG/UG/LoRA-only GAR-ours: 0.504/0.505/0.498 (spread 0.75pp), PPL 均为 2.78。与 overlap 数据相比绝对值略高（GAR +1-2pp, PPL +0.15），属正常泛化偏移，相对比较完全一致。数据完整性 confound 已排除。

================================================================================
EXP_ID: attention_steering_eval200_tf
METRICS: {
  "beta_0.0": {
    "mid_gar": 0.5353,
    "ppl": 2.62
  },
  "beta_2.0": {
    "mid_gar": 0.6112,
    "ppl": 2.69
  },
  "beta_3.0": {
    "mid_gar": 0.788,
    "ppl": 2.93
  },
  "beta_4.0": {
    "mid_gar": 0.8165,
    "ppl": 3.49
  },
  "beta_5.0": {
    "mid_gar": 0.8325,
    "ppl": 6.15
  },
  "beta_10.0": {
    "mid_gar": 0.977,
    "ppl": 505.21
  },
  "n_convs": 200,
  "mode": "tf"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "060b7175-09da-4baf-9d80-60581353d4e2",
  "isSidechain": false,
  "promptId": "8817af8a-f189-44e8-a462-1453a12b4ea3",
  "type": "user",
  "uuid": "6b86878a-ba61-4fad-be2c-a8c72a9e1f8b",
  "toolUseResult": {
    "stdout": "================================================================================\nEXP_ID: llama_eval_s42\nMETRICS: {\n  \"tf_base\": {\n    \"gar_ours\": 0.0166,\n    \"ngar_ours\": 0.3882,\n    \"gar_dongre\": 0.0038,\n    \"ngar_dongre\": 0.163,\n    \"ppl\": 3.45,\n    \"N\": 50,\n    \"T\": 4\n  },\n  \"tf_tg\": {\n    \"gar_ours\": 0.4836,\n    \"ngar_ours\": 11.8818,\n    \"gar_dongre\": 0.018,\n    \"ngar_dongre\": 0.7922,\n    \"ppl\": 2.57,\n    \"N\": 50,\n    \"T\": 4\n  },\n  \"ar_base\": {\n    \"gar_ours\": 0.0086,\n    \"ngar_ours\": 0.0798,\n    \"gar_dongre\": 0.0118,\n    \"ngar_dongre\": 0.1265,\n    \"ppl\": 1.24,\n    \"N\": 5,\n    \"T\": 10\n  },\n  \"ar_tg\": {\n    \"gar_ours\": 0.0304,\n    \"ngar_ours\": 0.2632,\n    \"gar_dongre\": 0.0217,\n    \"ngar_dongre\": 0.2459,\n    \"ppl\": 1.32,\n    \"N\": 5,\n    \"T\": 10\n  },\n  \"gap_ratio_tg_ours\": 15.9,\n  \"gap_ratio_base_ours\": 1.93,\n  \"gap_ratio_tg_dongre\": 0.83,\n  \"vs_qwen_v7_gap_ratio\": 32.1,\n  \"baseline_mid_gar\": 0.0122\n}\nNOTES: C5 跨模型泛化确认。Llama TG GAR-ours gap 16x (TF 0.484 vs AR 0.030)，低于 Qwen v7 的 32x 但仍非常显著。Base model gap 仅 1.9x（control 通过）。注意 TF/AR eval 设定不同 (N=50/T=4 vs N=5/T=10)，可能影响绝对值对比。GAR-dongre 无明显 gap (ratio 0.83x, AR ≥ TF)，仅 GAR-ours 展现 exposure bias 效应。Gate dynamic range: L24/L28/L30 diff 最大 (0.23-0.38)，与 Qwen 类似集中在中高层。\n\n================================================================================\nEXP_ID: llama_tg_s42\nMETRICS: {\n  \"epochs_completed\": 3,\n  \"total_steps\": 3000,\n  \"wall_clock_seconds\": 26212,\n  \"wall_clock_hours\": 7.28,\n  \"final_avg_loss\": 0.9233,\n  \"final_avg_ntp\": 0.9224,\n  \"final_avg_gar\": 0.0009,\n  \"final_avg_div\": 0,\n  \"final_gate_mean\": 0.9099,\n  \"final_gate_std\": 0.0701,\n  \"final_gate_min\": 0.7188,\n  \"final_gate_max\": 0.9922,\n  \"gate_profile_step3000\": {\n    \"L0\": 0.957,\n    \"L1\": 0.973,\n    \"L2\": 0.977,\n    \"L3\": 0.965,\n    \"L4\": 0.992,\n    \"L5\": 0.969,\n    \"L6\": 0.957,\n    \"L7\": 0.957,\n    \"L8\": 0.961,\n    \"L9\": 0.949,\n    \"L10\": 0.938,\n    \"L11\": 0.934,\n    \"L12\": 0.969,\n    \"L13\": 0.953,\n    \"L14\": 0.957,\n    \"L15\": 0.965,\n    \"L16\": 0.953,\n    \"L17\": 0.961,\n    \"L18\": 0.922,\n    \"L19\": 0.902,\n    \"L20\": 0.883,\n    \"L21\": 0.863,\n    \"L22\": 0.836,\n    \"L23\": 0.844,\n    \"L24\": 0.809,\n    \"L25\": 0.719,\n    \"L26\": 0.762,\n    \"L27\": 0.805,\n    \"L28\": 0.801,\n    \"L29\": 0.855,\n    \"L30\": 0.898,\n    \"L31\": 0.934\n  },\n  \"checkpoint_size_gate_mb\": 4.2,\n  \"checkpoint_size_lora_mb\": 26,\n  \"gpu\": \"NVIDIA RTX PRO 6000 Blackwell\",\n  \"vram_gb\": 102,\n  \"mem_used_gb\": 63.4\n}\n\n================================================================================\nEXP_ID: llama_lora_only_s42\nMETRICS: {\n  \"final_avg_loss\": 0.9288,\n  \"final_avg_ntp\": 0.9279,\n  \"final_avg_gar\": 0.0009,\n  \"gate_fixed\": 1,\n  \"gate_type\": \"none\",\n  \"wall_clock_s\": 25317,\n  \"wall_clock_h\": 7.03,\n  \"epochs_completed\": 3\n}\n\n================================================================================\nEXP_ID: eval_llama_ar_n20\nMETRICS: {\n  \"base\": {\n    \"gar_ours_mean\": 0.0088,\n    \"gar_ours_std\": 0.0056,\n    \"gar_ours_median_per_conv\": 0.0093,\n    \"gar_ours_median_per_turn_pool\": 0.0071,\n    \"gar_ours_spike_ratio\": \"0%\",\n    \"gar_dongre_mean\": 0.0049,\n    \"gar_dongre_std\": 0.0013,\n    \"gar_dongre_median\": 0.0047,\n    \"ngar_ours_mid\": 0.1019,\n    \"ngar_dongre_mid\": 0.1171,\n    \"ppl\": 1.293,\n    \"ppl_std\": 0.07,\n    \"ntp_loss\": 0.2552\n  },\n  \"tg\": {\n    \"gar_ours_mean\": 0.0434,\n    \"gar_ours_std\": 0.1002,\n    \"gar_ours_median_per_conv\": 0.0179,\n    \"gar_ours_median_per_turn_pool\": 0.0126,\n    \"gar_ours_spike_ratio\": \"5% (2/40 turns GAR>=0.4)\",\n    \"gar_dongre_mean\": 0.0183,\n    \"gar_dongre_std\": 0.0198,\n    \"gar_dongre_median\": 0.0152,\n    \"ngar_ours_mid\": 0.5357,\n    \"ngar_dongre_mid\": 0.4436,\n    \"ppl\": 1.437,\n    \"ppl_std\": 0.077,\n    \"ntp_loss\": 0.3612\n  },\n  \"lora_only\": {\n    \"gar_ours_mean\": 0.0284,\n    \"gar_ours_std\": 0.0481,\n    \"gar_ours_median_per_conv\": 0.0184,\n    \"gar_ours_median_per_turn_pool\": 0.0133,\n    \"gar_ours_spike_ratio\": \"0%\",\n    \"gar_dongre_mean\": 0.0205,\n    \"gar_dongre_std\": 0.0241,\n    \"gar_dongre_median\": 0.016,\n    \"ngar_ours_mid\": 0.3488,\n    \"ngar_dongre_mid\": 0.4997,\n    \"ppl\": 1.419,\n    \"ppl_std\": 0.075,\n    \"ntp_loss\": 0.3483\n  },\n  \"n_conversations\": 20,\n  \"n_turns\": 4,\n  \"mid_turns_definition\": \"turns 3-T (0-indexed avg_gar[2:], excluding turns 1-2). All 16 eval entries use same definition.\",\n  \"stat_pool\": \"median_per_conv: median of 20 per-conversation mid-turn averages. median_per_turn_pool: median of 40 individual turn values (20 conv x 2 mid turns).\",\n  \"ranking_gar_ours_mean\": \"TG(0.0434) > LO(0.0284) > Base(0.0088)\",\n  \"ranking_gar_ours_median_per_conv\": \"TG(0.0179) \\u2248 LO(0.0184) > Base(0.0093)\",\n  \"ranking_gar_ours_median_per_turn_pool\": \"TG(0.0126) \\u2248 LO(0.0133) > Base(0.0071)\",\n  \"ranking_gar_dongre\": \"LO(0.0205) > TG(0.0183) > Base(0.0049)\",\n  \"note\": \"Paper \\u00a75.5 cites median_per_conv (median of per-conversation mid-turn averages across N=20). median_per_turn_pool is the alternative statistic from pooled individual turns. Both confirm TG \\u2248 LO (zero-increment).\"\n}\nNOTES: N=20 AR eval stabilizes estimates. **mid_turns = turns 3-T (0-indexed avg_gar[2:], excluding turns 1-2; all 16 eval entries use same definition)**. Two median levels: median_per_conv (paper §5.5 cites this: TG 0.0179, LO 0.0184, Base 0.0093) = median of 20 per-conversation mid-turn averages; median_per_turn_pool (TG 0.0126, LO 0.0133, Base 0.0071) = median of 40 pooled individual turns. Both confirm TG ≈ LO (zero-increment). Mean (TG 0.0434 > LO 0.0284) driven by outlier spikes (TG std=0.1002, 5% turns GAR≥0.4; LO std=0.0481, 0% spikes). PPL: Base(1.29) < LO(1.42) < TG(1.44). Pending paper fix: §5.5 says \"turns 2-T\" but code excludes turns 1-2; will correct to \"excluding the first two turns\" in next paper edit batch.\n\n================================================================================\nEXP_ID: p1_llama_ss_eval\nMETRICS: {\n  \"ss_tf_gar\": 0.477,\n  \"ss_tf_ppl\": 2.82,\n  \"ss_ar_b0_gar\": 0.1662,\n  \"ss_ar_b0_ppl\": 1.37,\n  \"ss_ar_b5_gar\": 0.7905,\n  \"ss_ar_b5_ppl\": 1.81,\n  \"base_ar_gar\": 0.0179,\n  \"base_ar_ppl\": 1.22,\n  \"tf_ar_gap\": 2.87\n}\n\n================================================================================\nEXP_ID: llama_ar_matched_eval\nMETRICS: {\n  \"ar_base_ours\": {\n    \"mid_gar\": 0.0082,\n    \"ngar\": 0.1,\n    \"ppl\": 1.267\n  },\n  \"ar_tg_ours\": {\n    \"mid_gar\": 0.0388,\n    \"ngar\": 0.493,\n    \"ppl\": 1.413\n  },\n  \"ar_base_dongre\": {\n    \"mid_gar\": 0.0051,\n    \"ngar\": 0.12,\n    \"ppl\": 1.267\n  },\n  \"ar_tg_dongre\": {\n    \"mid_gar\": 0.018,\n    \"ngar\": 0.431,\n    \"ppl\": 1.413\n  },\n  \"tf_reference\": {\n    \"tf_tg_ours_ngar\": 11.88,\n    \"tf_base_ours_ngar\": 0.388,\n    \"tf_tg_ours_raw\": 0.4836,\n    \"tf_tg_dongre_raw\": 0.018\n  },\n  \"matched_gap_analysis\": {\n    \"gar_ours_raw_gap\": \"12.5x (TF 0.484 / AR 0.039)\",\n    \"gar_ours_ngar_gap\": \"24.1x (TF 11.88 / AR 0.493)\",\n    \"gar_dongre_raw_gap\": \"1.002x (TF 0.018 / AR 0.018) \\u2014 zero gap\",\n    \"tg_over_base_ar_ours\": \"4.71x\",\n    \"tg_over_base_ar_dongre\": \"3.54x\",\n    \"conclusion\": \"GAR-ours TF-AR gap 12.5x (raw) / 24x (nGAR) is genuine exposure bias. GAR-Dongre zero gap (1.002x) confirms mechanism specificity: exposure bias selectively destroys learned goal-attention routing while leaving content-overlap-based attention unaffected.\"\n  }\n}\nNOTES: CORRECTION (2026-05-21 04:36): Agent 之前错误地将 AR TG nGAR (0.493) 与 TF TG raw GAR (0.484) 对比，误判为 'nGAR aligns, gap is normalization artifact'。Reviewer 核实：TF TG ours nGAR = 11.88（非 0.48）。nGAR gap = 11.88 / 0.493 = 24.1×，比 raw gap (12.5×) 还大。'Normalization artifact' 分析完全错误——GAR-ours 的 gap 是真实的 exposure bias。论文绝对不能使用 normalization artifact 叙事。\n\n================================================================================\nEXP_ID: v7_tg_s123\nMETRICS: {\n  \"epoch_1\": {\n    \"avg_loss\": 0.9447,\n    \"avg_ntp_loss\": 0.9434,\n    \"avg_gar_loss\": 0.0013,\n    \"avg_div_loss\": 0\n  },\n  \"epoch_2\": {\n    \"avg_loss\": 0.9315,\n    \"avg_ntp_loss\": 0.9305,\n    \"avg_gar_loss\": 0.001,\n    \"avg_div_loss\": 0\n  },\n  \"final_gate\": {\n    \"mean\": 0.9467,\n    \"std\": 0.051,\n    \"min\": 0.793,\n    \"max\": 1\n  },\n  \"final_gate_profile\": {\n    \"L0\": 0.883,\n    \"L1\": 0.793,\n    \"L2\": 0.996,\n    \"L3\": 0.988,\n    \"L4\": 0.984,\n    \"L5\": 0.797,\n    \"L6\": 0.961,\n    \"L7\": 0.918,\n    \"L8\": 0.965,\n    \"L9\": 0.934,\n    \"L10\": 0.969,\n    \"L11\": 0.918,\n    \"L12\": 0.926,\n    \"L13\": 0.941,\n    \"L14\": 0.93,\n    \"L15\": 0.965,\n    \"L16\": 0.941,\n    \"L17\": 0.91,\n    \"L18\": 0.961,\n    \"L19\": 0.965,\n    \"L20\": 0.973,\n    \"L21\": 0.988,\n    \"L22\": 0.969,\n    \"L23\": 0.98,\n    \"L24\": 0.98,\n    \"L25\": 0.984,\n    \"L26\": 0.988,\n    \"L27\": 1\n  },\n  \"training_time_s\": 21425.2\n}\n\n================================================================================\nEXP_ID: d048_ss_s42\nMETRICS: {\n  \"final_avg_loss\": 0.9326,\n  \"final_ntp_loss\": 0.932,\n  \"final_gar_loss\": 0.0007,\n  \"gate_mean\": 0.9527,\n  \"gate_std\": 0.0589,\n  \"gate_min\": 0.7383,\n  \"gate_min_layer\": \"L4\",\n  \"gate_max\": 1,\n  \"ss_usage\": \"4750/16000 (29.7%)\",\n  \"ss_fallback\": 0,\n  \"epochs_completed\": 3,\n  \"wall_clock_s\": 23418,\n  \"wall_clock_h\": 6.5\n}\nNOTES: Training complete (resume v3). 23418s (6.5h) for epoch 1+2. Final: Avg Loss=0.9326, NTP=0.9320, GAR=0.0007, DIV=0.0000. Gate: mean=0.9527, std=0.0589, min=0.7383(L4), max=1.000. SS: 4750/16000 (29.7%) used, 0 fallback. Checkpoints: epoch_0, epoch_1, epoch_2, final. Gate profile consistent with prior SS runs (L4 lowest).\n\n================================================================================\nEXP_ID: phase2_4way_eval\nMETRICS: {\n  \"base_ours_mid_gar\": 0.0107,\n  \"base_ours_recovery_pp\": -0.15,\n  \"base_dongre_mid_gar\": 0.003,\n  \"base_dongre_recovery_pp\": -0.92,\n  \"base_ppl\": 4.23,\n  \"base_ntp\": 1.4162,\n  \"tg_ours_mid_gar\": 0.4866,\n  \"tg_ours_recovery_pp\": 47.44,\n  \"tg_dongre_mid_gar\": 0.0157,\n  \"tg_dongre_recovery_pp\": 0.35,\n  \"tg_ppl\": 2.63,\n  \"tg_ntp\": 0.9484,\n  \"ug_ours_mid_gar\": 0.4923,\n  \"ug_ours_recovery_pp\": 48.01,\n  \"ug_dongre_mid_gar\": 0.013,\n  \"ug_dongre_recovery_pp\": 0.08,\n  \"ug_ppl\": 2.62,\n  \"ug_ntp\": 0.9433,\n  \"lora_ours_mid_gar\": 0.486,\n  \"lora_ours_recovery_pp\": 47.39,\n  \"lora_dongre_mid_gar\": 0.0137,\n  \"lora_dongre_recovery_pp\": 0.15,\n  \"lora_ppl\": 2.63,\n  \"lora_ntp\": 0.9482,\n  \"route_b_confirmed\": true,\n  \"gating_incremental_benefit\": \"none\"\n}\nNOTES: 四路 eval 完成，Route B 决定性确认。三种训练方法（TG/UG/LoRA-only）在推理端完全趋同：ours GAR recovery ~47-48pp（vs base -0.15pp），dongre GAR recovery 0.08-0.35pp，PPL 2.62-2.63，NTP 0.943-0.948。Gating 机制（无论 turn-conditioned 还是 uniform）相比纯 LoRA 微调零增量。LoRA fine-tuning 是 GAR recovery 的唯一来源。hypothesis 被证伪：TRG 不比 LoRA-only 更好。\n\n================================================================================\nEXP_ID: phase2_4way_eval_heldout\nMETRICS: {\n  \"base_ours_mid_gar\": 0.0128,\n  \"base_ours_recovery_pp\": 0.06,\n  \"base_dongre_mid_gar\": 0.0031,\n  \"base_dongre_recovery_pp\": -0.91,\n  \"base_ppl\": 4.34,\n  \"base_ntp\": 1.4045,\n  \"tg_ours_mid_gar\": 0.5035,\n  \"tg_ours_recovery_pp\": 49.13,\n  \"tg_dongre_mid_gar\": 0.0152,\n  \"tg_dongre_recovery_pp\": 0.3,\n  \"tg_ppl\": 2.78,\n  \"tg_ntp\": 0.9771,\n  \"ug_ours_mid_gar\": 0.5053,\n  \"ug_ours_recovery_pp\": 49.31,\n  \"ug_dongre_mid_gar\": 0.0124,\n  \"ug_dongre_recovery_pp\": 0.02,\n  \"ug_ppl\": 2.78,\n  \"ug_ntp\": 0.9752,\n  \"lora_ours_mid_gar\": 0.4978,\n  \"lora_ours_recovery_pp\": 48.56,\n  \"lora_dongre_mid_gar\": 0.0132,\n  \"lora_dongre_recovery_pp\": 0.1,\n  \"lora_ppl\": 2.78,\n  \"lora_ntp\": 0.9771,\n  \"three_way_convergence_confirmed\": true,\n  \"gar_ours_spread_pp\": 0.75,\n  \"ppl_spread\": 0,\n  \"data_overlap\": false\n}\nNOTES: Held-out eval 三路趋同完全复现。TG/UG/LoRA-only GAR-ours: 0.504/0.505/0.498 (spread 0.75pp), PPL 均为 2.78。与 overlap 数据相比绝对值略高（GAR +1-2pp, PPL +0.15），属正常泛化偏移，相对比较完全一致。数据完整性 confound 已排除。\n\n================================================================================\nEXP_ID: attention_steering_eval200_tf\nMETRICS: {\n  \"beta_0.0\": {\n    \"mid_gar\": 0.5353,\n    \"ppl\": 2.62\n  },\n  \"beta_2.0\": {\n    \"mid_gar\": 0.6112,\n    \"ppl\": 2.69\n  },\n  \"beta_3.0\": {\n    \"mid_gar\": 0.788,\n    \"ppl\": 2.93\n  },\n  \"beta_4.0\": {\n    \"mid_gar\": 0.8165,\n    \"ppl\": 3.49\n  },\n  \"beta_5.0\": {\n    \"mid_gar\": 0.8325,\n    \"ppl\": 6.15\n  },\n  \"beta_10.0\": {\n    \"mid_gar\": 0.977,\n    \"ppl\": 505.21\n  },\n  \"n_convs\": 200,\n  \"mode\": \"tf\"\n}",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "060b7175-09da-4baf-9d80-60581353d4e2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "4b680861-4da7-411a-8744-3dabfdaf2205",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Runtime record

_source line 85 · 2026-05-25T20:40:05.360Z_

```json
{
  "parentUuid": "6b86878a-ba61-4fad-be2c-a8c72a9e1f8b",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "5587b706-47c7-4910-ad95-4442ef966631",
  "timestamp": "2026-05-25T20:40:05.360Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "4b680861-4da7-411a-8744-3dabfdaf2205",
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
  "leafUuid": "5587b706-47c7-4910-ad95-4442ef966631",
  "sessionId": "4b680861-4da7-411a-8744-3dabfdaf2205"
}
```

---

### Runtime record

_source line 87_

```json
{
  "type": "ai-title",
  "aiTitle": "Audit quantitative claims in paper body text",
  "sessionId": "4b680861-4da7-411a-8744-3dabfdaf2205"
}
```

---

### Assistant

_source line 88 · 2026-05-25T20:40:09.615Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have a very comprehensive dataset. Let me also check for a few things that are referenced in the paper but might not have dedicated experiments: the gradient analysis experiment, the `tab_statistical_tests` entry, and any remaining data I need.

Let me also check if there's a `gradient_analysis` experiment (not `analysis_gradient_conflict`), and the statistical tests entry.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5587b706-47c7-4910-ad95-4442ef966631",
  "isSidechain": false,
  "requestId": "req_011CbPw6kVedjQaBGWkgq3rL",
  "type": "assistant",
  "uuid": "805829dd-dbde-4c1e-ae20-fc57ed6419e6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "4b680861-4da7-411a-8744-3dabfdaf2205",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018sJSjFUrmMdaRhXaSxnL9i",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6925,
      "cache_read_input_tokens": 67990,
      "output_tokens": 528,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 6925,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 528,
          "cache_read_input_tokens": 67990,
          "cache_creation_input_tokens": 6925,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 6925
          },
          "type": "message"
        }
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

_source line 89 · 2026-05-25T20:40:10.577Z_

Good. Let me also check for the statistical tests experiment and the multi-seed SS data that the paper references.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "805829dd-dbde-4c1e-ae20-fc57ed6419e6",
  "isSidechain": false,
  "requestId": "req_011CbPw6kVedjQaBGWkgq3rL",
  "type": "assistant",
  "uuid": "e366f6fd-6604-44ae-99cf-4b51b74c638b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "4b680861-4da7-411a-8744-3dabfdaf2205",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018sJSjFUrmMdaRhXaSxnL9i",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6925,
      "cache_read_input_tokens": 67990,
      "output_tokens": 528,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 6925,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 528,
          "cache_read_input_tokens": 67990,
          "cache_creation_input_tokens": 6925,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 6925
          },
          "type": "message"
        }
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

_source line 90 · 2026-05-25T20:40:18.988Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01MKd9Kq8kpoaRGNc8oED4oh`</summary>

```json
{
  "command": "python3 << 'PYEOF'\nimport json\n\nREGISTRY = \"/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-11-projects-turn-residual-gating/4b680861-4da7-411a-8744-3dabfdaf2205/tool-results/mcp-agent-ml-research-read_registry-1779741484333.txt\"\ndata = json.load(open(REGISTRY))\nresult = json.loads(data['result'])\nexperiments = result['data']['experiments']\n\n# Check for tab_statistical_tests (not found earlier), and gradient_analysis\nfor eid in sorted(experiments.keys()):\n    if 'stat' in eid or 'gradient' in eid or 'pcgrad' in eid:\n        exp = experiments[eid]\n        metrics = exp.get('metrics')\n        notes = exp.get('notes')\n        if metrics or notes:\n            print(f\"\\n{'='*60}\")\n            print(f\"EXP_ID: {eid}\")\n            if metrics:\n                print(f\"METRICS: {json.dumps(metrics, indent=2)[:2000]}\")\n            if notes:\n                print(f\"NOTES: {notes[:1000]}\")\nPYEOF\n",
  "description": "Find statistical tests and gradient experiments",
  "timeout": 15000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e366f6fd-6604-44ae-99cf-4b51b74c638b",
  "isSidechain": false,
  "requestId": "req_011CbPw6kVedjQaBGWkgq3rL",
  "type": "assistant",
  "uuid": "885125fe-5a0d-44f8-a897-8eeb6932eb8f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "4b680861-4da7-411a-8744-3dabfdaf2205",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018sJSjFUrmMdaRhXaSxnL9i",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6925,
      "cache_read_input_tokens": 67990,
      "output_tokens": 528,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 6925,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 528,
          "cache_read_input_tokens": 67990,
          "cache_creation_input_tokens": 6925,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 6925
          },
          "type": "message"
        }
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

_source line 91 · 2026-05-25T20:40:19.070Z_

<details><summary>↩ Tool result · `toolu_01MKd9Kq8kpoaRGNc8oED4oh`</summary>

```text
============================================================
EXP_ID: analysis_gradient_conflict
METRICS: {
  "epoch0_cos_sim": -0.089,
  "epoch1_cos_sim": -0.054,
  "epoch2_cos_sim": -0.042,
  "epoch0_neg_layers_pct": 78.6,
  "epoch1_neg_layers_pct": 71.4,
  "epoch2_neg_layers_pct": 67.9,
  "epoch0_mag_ratio": 7.5,
  "epoch1_mag_ratio": 13.7,
  "epoch2_mag_ratio": 14.7
}

============================================================
EXP_ID: p2_llama_gradient_conflict
METRICS: {
  "cos_sim_mean": 0.0045,
  "cos_sim_std": 0.07,
  "neg_cos_sim_layers_pct": 53.1,
  "mag_ratio_median": 25.7,
  "conclusion_note": "cos_sim\u22480 indicates near-orthogonal (NOT conflict). Script conclusion text 'widespread conflict' is misleading \u2014 actual finding: NTP and GAR gradients are nearly orthogonal on Llama, consistent with Qwen pattern."
}

============================================================
EXP_ID: phase2_tg_s42_v9_pcgrad
METRICS: {
  "eval_iid_ours_mid_gar": 0.5002,
  "eval_iid_dongre_mid_gar": 0.0123,
  "eval_iid_ppl": 2.78,
  "eval_iid_ntp": 0.9752,
  "eval_heldout_ours_mid_gar": 0.5002,
  "eval_heldout_dongre_mid_gar": 0.0123,
  "eval_heldout_ppl": 2.78,
  "eval_heldout_ntp": 0.9752,
  "eval_modelgen_ours_mid_gar": 0.0151,
  "eval_modelgen_dongre_mid_gar": 0.0173,
  "eval_modelgen_ppl": 1.5,
  "vs_v7_iid_ppl_diff": 0.004,
  "vs_v7_iid_gar_diff": -0.0033
}
NOTES: D028 因果排除确认（M017 修正后）。训练: EXIT_CODE=0, 7.98h, 3 epochs。PCGrad cos_sim 从 -0.061→+0.055→-0.035 (围绕 0 振荡), NTP mag_ratio 2.8→28.8 持续增长。L_GAR 有 0-350 step 高原期后仍坍塌到≈0。IID eval (同 protocol 50 heldout convs): GAR-ours=0.5002 (vs v7 0.5035, diff -0.33pp), GAR-Dongre=0.0123 (vs v7 0.0152), PPL=2.780 (vs v7 2.784, diff 0.004, 无改善)。Model-gen eval (5 convs): GAR-ours=0.0151, PPL=1.50。结论: PCGrad 消除梯度方向冲突后所有 IID 指标均 ≈ v7（GAR、PPL、NTP 无变化），方向冲突因 NTP 幅度主导 (10-40x) 而 inconsequential。Exposure bias 是 30x gap 根因。
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "885125fe-5a0d-44f8-a897-8eeb6932eb8f",
  "isSidechain": false,
  "promptId": "8817af8a-f189-44e8-a462-1453a12b4ea3",
  "type": "user",
  "uuid": "5ca645a0-a0ec-44ac-90b5-e2ee19ababde",
  "toolUseResult": {
    "stdout": "============================================================\nEXP_ID: analysis_gradient_conflict\nMETRICS: {\n  \"epoch0_cos_sim\": -0.089,\n  \"epoch1_cos_sim\": -0.054,\n  \"epoch2_cos_sim\": -0.042,\n  \"epoch0_neg_layers_pct\": 78.6,\n  \"epoch1_neg_layers_pct\": 71.4,\n  \"epoch2_neg_layers_pct\": 67.9,\n  \"epoch0_mag_ratio\": 7.5,\n  \"epoch1_mag_ratio\": 13.7,\n  \"epoch2_mag_ratio\": 14.7\n}\n\n============================================================\nEXP_ID: p2_llama_gradient_conflict\nMETRICS: {\n  \"cos_sim_mean\": 0.0045,\n  \"cos_sim_std\": 0.07,\n  \"neg_cos_sim_layers_pct\": 53.1,\n  \"mag_ratio_median\": 25.7,\n  \"conclusion_note\": \"cos_sim\\u22480 indicates near-orthogonal (NOT conflict). Script conclusion text 'widespread conflict' is misleading \\u2014 actual finding: NTP and GAR gradients are nearly orthogonal on Llama, consistent with Qwen pattern.\"\n}\n\n============================================================\nEXP_ID: phase2_tg_s42_v9_pcgrad\nMETRICS: {\n  \"eval_iid_ours_mid_gar\": 0.5002,\n  \"eval_iid_dongre_mid_gar\": 0.0123,\n  \"eval_iid_ppl\": 2.78,\n  \"eval_iid_ntp\": 0.9752,\n  \"eval_heldout_ours_mid_gar\": 0.5002,\n  \"eval_heldout_dongre_mid_gar\": 0.0123,\n  \"eval_heldout_ppl\": 2.78,\n  \"eval_heldout_ntp\": 0.9752,\n  \"eval_modelgen_ours_mid_gar\": 0.0151,\n  \"eval_modelgen_dongre_mid_gar\": 0.0173,\n  \"eval_modelgen_ppl\": 1.5,\n  \"vs_v7_iid_ppl_diff\": 0.004,\n  \"vs_v7_iid_gar_diff\": -0.0033\n}\nNOTES: D028 因果排除确认（M017 修正后）。训练: EXIT_CODE=0, 7.98h, 3 epochs。PCGrad cos_sim 从 -0.061→+0.055→-0.035 (围绕 0 振荡), NTP mag_ratio 2.8→28.8 持续增长。L_GAR 有 0-350 step 高原期后仍坍塌到≈0。IID eval (同 protocol 50 heldout convs): GAR-ours=0.5002 (vs v7 0.5035, diff -0.33pp), GAR-Dongre=0.0123 (vs v7 0.0152), PPL=2.780 (vs v7 2.784, diff 0.004, 无改善)。Model-gen eval (5 convs): GAR-ours=0.0151, PPL=1.50。结论: PCGrad 消除梯度方向冲突后所有 IID 指标均 ≈ v7（GAR、PPL、NTP 无变化），方向冲突因 NTP 幅度主导 (10-40x) 而 inconsequential。Exposure bias 是 30x gap 根因。",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "885125fe-5a0d-44f8-a897-8eeb6932eb8f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "4b680861-4da7-411a-8744-3dabfdaf2205",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 92 · 2026-05-25T20:40:23.832Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have comprehensive registry data. Let me also check the d048_final_ar_eval for more detailed data, particularly the AR eval results that the paper's Table 1 is based on. And I should also look for the statistical tests data separately, as `tab_statistical_tests` might not exist as an experiment. Let me check.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5ca645a0-a0ec-44ac-90b5-e2ee19ababde",
  "isSidechain": false,
  "requestId": "req_011CbPw7mArgpqg2GgDjhQs4",
  "type": "assistant",
  "uuid": "bd75e54c-91ab-421b-a13d-e400941c80f4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "4b680861-4da7-411a-8744-3dabfdaf2205",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Qj8geJWAqKFmVBCkSvDQiH",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1488,
      "cache_read_input_tokens": 74915,
      "output_tokens": 434,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1488,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 434,
          "cache_read_input_tokens": 74915,
          "cache_creation_input_tokens": 1488,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1488
          },
          "type": "message"
        }
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

_source line 93 · 2026-05-25T20:40:24.883Z_

Now I have all the registry data I need. Let me also check for statistical test results and the Wilcoxon p-value data referenced in the paper.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bd75e54c-91ab-421b-a13d-e400941c80f4",
  "isSidechain": false,
  "requestId": "req_011CbPw7mArgpqg2GgDjhQs4",
  "type": "assistant",
  "uuid": "ee40fd85-cd61-477f-a71b-d8619ea55d9a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "4b680861-4da7-411a-8744-3dabfdaf2205",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Qj8geJWAqKFmVBCkSvDQiH",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1488,
      "cache_read_input_tokens": 74915,
      "output_tokens": 434,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1488,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 434,
          "cache_read_input_tokens": 74915,
          "cache_creation_input_tokens": 1488,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1488
          },
          "type": "message"
        }
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

_source line 94 · 2026-05-25T20:40:31.653Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01628TZ6cvTpRjsbWSz5fwsb`</summary>

```json
{
  "command": "python3 << 'PYEOF'\nimport json\n\nREGISTRY = \"/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-11-projects-turn-residual-gating/4b680861-4da7-411a-8744-3dabfdaf2205/tool-results/mcp-agent-ml-research-read_registry-1779741484333.txt\"\ndata = json.load(open(REGISTRY))\nresult = json.loads(data['result'])\nexperiments = result['data']['experiments']\n\n# Check if tab_statistical_tests exists\nprint(\"tab_statistical_tests\" in experiments)\n\n# Also check d048_final_ar_eval for more complete data - we got truncated earlier\nexp = experiments['d048_final_ar_eval']\nprint(json.dumps(exp, indent=2)[:5000])\nPYEOF\n",
  "description": "Check statistical tests and full AR eval data",
  "timeout": 15000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ee40fd85-cd61-477f-a71b-d8619ea55d9a",
  "isSidechain": false,
  "requestId": "req_011CbPw7mArgpqg2GgDjhQs4",
  "type": "assistant",
  "uuid": "c0723efc-c2ef-4b91-9204-dd15458e1e52",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "4b680861-4da7-411a-8744-3dabfdaf2205",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Qj8geJWAqKFmVBCkSvDQiH",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1488,
      "cache_read_input_tokens": 74915,
      "output_tokens": 434,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1488,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 434,
          "cache_read_input_tokens": 74915,
          "cache_creation_input_tokens": 1488,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1488
          },
          "type": "message"
        }
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

_source line 95 · 2026-05-25T20:40:31.783Z_

<details><summary>↩ Tool result · `toolu_01628TZ6cvTpRjsbWSz5fwsb`</summary>

```text
False
{
  "status": "DONE",
  "retry_count": 0,
  "created_at": "2026-05-23T03:46:23.495Z",
  "updated_at": "2026-05-23T03:47:01.285Z",
  "hypothesis": "Unified AR N=50 eval across 6 conditions (Base/TG/UG/LO/PCGrad/SS) with bootstrap CI and Wilcoxon tests to establish statistically rigorous comparisons for all claims",
  "spec": {
    "command": "bash scripts/d048_final_ar_eval.sh",
    "server": "westd-20861",
    "data_path": "data/eval_200/eval_200.json",
    "data_count": 200,
    "model_name": "Qwen/Qwen2.5-7B-Instruct",
    "seed": 42,
    "checkpoint_source": "phase2_tg_s42_v7 / phase2_ug_s42 / phase2_lora_only_s42 / tg_v9_pcgrad_s42 / d048_ss_s42",
    "eval_data": "eval_200.json N=50",
    "checkpoint_path": "N/A (eval only)",
    "log_path": "runs/d048_final_ar_eval.log",
    "results_path": "results/d048_final_ar/"
  },
  "conclusion": "success",
  "completed_at": "2026-05-23T03:46:57.110Z",
  "metrics": {
    "beta0": {
      "base_gar": 0.019,
      "tg_gar": 0.064,
      "ug_gar": 0.033,
      "lo_gar": 0.037,
      "pcgrad_gar": 0.03,
      "ss_gar": 0.347
    },
    "beta3": {
      "base_gar": 0.531,
      "tg_gar": 0.556,
      "ss_gar": 0.593
    },
    "beta5": {
      "base_gar": 0.704,
      "tg_gar": 0.727,
      "ss_gar": 0.717
    },
    "wilcoxon_beta0": {
      "tg_vs_base_p": "<0.001",
      "tg_vs_base_r": 0.802,
      "ss_vs_tg_p": "<0.001",
      "ss_vs_tg_r": 0.869
    },
    "ppl": {
      "base": 1.447,
      "tg": 1.432,
      "ss": 1.442
    },
    "n_convs": 39
  }
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c0723efc-c2ef-4b91-9204-dd15458e1e52",
  "isSidechain": false,
  "promptId": "8817af8a-f189-44e8-a462-1453a12b4ea3",
  "type": "user",
  "uuid": "80e4278d-a31e-4ea2-9d79-1cb2ce910f7f",
  "toolUseResult": {
    "stdout": "False\n{\n  \"status\": \"DONE\",\n  \"retry_count\": 0,\n  \"created_at\": \"2026-05-23T03:46:23.495Z\",\n  \"updated_at\": \"2026-05-23T03:47:01.285Z\",\n  \"hypothesis\": \"Unified AR N=50 eval across 6 conditions (Base/TG/UG/LO/PCGrad/SS) with bootstrap CI and Wilcoxon tests to establish statistically rigorous comparisons for all claims\",\n  \"spec\": {\n    \"command\": \"bash scripts/d048_final_ar_eval.sh\",\n    \"server\": \"westd-20861\",\n    \"data_path\": \"data/eval_200/eval_200.json\",\n    \"data_count\": 200,\n    \"model_name\": \"Qwen/Qwen2.5-7B-Instruct\",\n    \"seed\": 42,\n    \"checkpoint_source\": \"phase2_tg_s42_v7 / phase2_ug_s42 / phase2_lora_only_s42 / tg_v9_pcgrad_s42 / d048_ss_s42\",\n    \"eval_data\": \"eval_200.json N=50\",\n    \"checkpoint_path\": \"N/A (eval only)\",\n    \"log_path\": \"runs/d048_final_ar_eval.log\",\n    \"results_path\": \"results/d048_final_ar/\"\n  },\n  \"conclusion\": \"success\",\n  \"completed_at\": \"2026-05-23T03:46:57.110Z\",\n  \"metrics\": {\n    \"beta0\": {\n      \"base_gar\": 0.019,\n      \"tg_gar\": 0.064,\n      \"ug_gar\": 0.033,\n      \"lo_gar\": 0.037,\n      \"pcgrad_gar\": 0.03,\n      \"ss_gar\": 0.347\n    },\n    \"beta3\": {\n      \"base_gar\": 0.531,\n      \"tg_gar\": 0.556,\n      \"ss_gar\": 0.593\n    },\n    \"beta5\": {\n      \"base_gar\": 0.704,\n      \"tg_gar\": 0.727,\n      \"ss_gar\": 0.717\n    },\n    \"wilcoxon_beta0\": {\n      \"tg_vs_base_p\": \"<0.001\",\n      \"tg_vs_base_r\": 0.802,\n      \"ss_vs_tg_p\": \"<0.001\",\n      \"ss_vs_tg_r\": 0.869\n    },\n    \"ppl\": {\n      \"base\": 1.447,\n      \"tg\": 1.432,\n      \"ss\": 1.442\n    },\n    \"n_convs\": 39\n  }\n}",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "c0723efc-c2ef-4b91-9204-dd15458e1e52",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "4b680861-4da7-411a-8744-3dabfdaf2205",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 96 · 2026-05-25T20:48:59.774Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the data I need. Let me also check for the statistical test data and the specific p-values mentioned in the paper (e.g., p=0.004 for TG vs LO). Let me check if there are results files on disk.

Actually, let me also check if the paper mentions specific CI values and p-values that I need to verify. Looking at the paper text:

From experiments.tex:
- "ThreadGate vs. LoRA-only is significant (p=0.004)" - need to verify
- "A second seed confirms TF stability (0.504±0.001)" - need to verify


- MMLU 5-shot accuracy stays within 0.8 percentage points across variants
- "AR GAR-ours rises to 0.401±0.047" - need to verify
- The speedup improves from 7.8× to ~1.3×
- "TF GAR 0.498±0.004" and perplexity at 1.441±0.001 - need to verify
- β=5 shows 0.717±0.001 with standard deviation reducing from 0.047 to 0.001

From analysis.tex:
- 27 out of 28 layers show gate inversion
- Wilcoxon test p-value at 3.73 × 10^{-8} with correlation r = 0.975
- Layer 23 shifts from 0.769 to 0.979
- Inference-time values range 0.93--0.98 with 2--7% attenuation
- NTP and GAR gradients oppose in 68--79% of layers
- Cosine similarity shifts from −0.089 to −0.042 across epochs
- NTP magnitude dominance grows from 7.5× to 14.7×
- AR GAR worsens from 0.064 to 0.030 (p=0.002)
- GAR-Dongre shows minimal shift on Llama (1.002×) and Qwen (1.28×)
- TRC is 0.334/0.332 for ThreadGate with a +0.002 gap
- Additional TRC values at 0.349/0.411 for LoRA-only with a −0.062 gap in the opposite direction
- Llama TF GAR reaches 0.484 with ThreadGate and 0.481 with LoRA-only
- Median values are 0.018 for both ThreadGate and LoRA-only, 0.009 for Base
- Gap ratios of 27× and 26× compress to 2.9× when Llama SS is applied
- TF GAR at 0.477 and AR GAR at 0.166
- β=3 recovers performance on Qwen SS (0.593) but fails on Llama SS (0.173)
- Llama requires β=5 to reach GAR of 0.791, exceeding Qwen SS at 0.717
- 79.8% GA recovery with β-steering bringing performance to 0.715

Now I'm verifying the reported numbers against the actual experimental data and computing multi-seed averages for the SS results across different random seeds. The standard deviation calculation checks out to 0.047, confirming the paper's reported value of 0.401±0.047 across those three seed runs. But there's a discrepancy—d048_eval_ss_s42 shows a different AR GAR value of 0.3887 with only 5 samples, while d048_final_ar_eval reports 0.347 with 50 samples for the same seed.

Looking at the actual sample sizes for AR across the three seeds, s42 and s123 both have 39 valid conversions while s456 has the full 50, which explains some of the variation. I need to verify whether 0.347 is the correct rounded value from d048_final_ar_eval's n_convs=39 result.

The paper reports AR GAR-ours as 0.401±0.047, and averaging the three seed values (0.347, 0.4231, 0.4325) gives 0.4009, which matches perfectly. Now I'm checking the TF GAR values across seeds—0.5025, 0.5536, and 0.4964—where 0.5536 looks like an outlier, so I need to calculate the mean and standard deviation to see if they align with what the paper claims.

The mean comes to 0.5175, which doesn't match the reported 0.498±0.004, so I'm wondering if the paper is averaging different TF values—maybe IID or held-out values rather than the "mid" variants. Looking at the eval data more carefully, the s123 value of 0.5536 seems anomalously high compared to the others, and I need to figure out which specific TF GAR values the paper actually used for its reported mean. Looking at the d048 series results across the three seeds, the TF values are 0.5025, 0.5536, and 0.4964, which average to 0.5175 with a standard deviation of 0.031—but that doesn't match the paper's reported 0.498±0.004, so the TF data might be coming from a different evaluation source altogether. Looking at the SS model results across the three seeds, I'm getting a mean TF GAR of 0.5175 with a standard deviation of 0.031, which doesn't match the paper's reported 0.498±0.004 at all. I need to figure out whether the paper is using held-out evaluations instead of IID ones, since the eval logs don't always clearly distinguish between them.

I'm noticing some inconsistencies in how the metrics are labeled across seeds—s123 reports "tf_gar_ours" while s456 reports "tf_gar_ours_mid", which suggests they might be computing things differently, possibly with "mid" excluding early conversation turns. Rather than get stuck on this discrepancy, I'll document it and move forward with the audit. So the TF metrics in d048_eval_ss_s42 are actually evaluating the TG model, not the SS model—that's why I'm seeing TG-specific values like the 0.5025 GAR. The SS model's performance is captured in the AR metrics instead. I need to figure out if there's a separate TF evaluation for the SS model itself, or if the paper is only reporting AR results for that configuration.

Looking at the eval scripts, it seems eval_v8b_ss does have TF GAR values for the SS model across different seeds—I'm seeing 0.4983 for s42 and 0.503 for s123, which average to around 0.5007. But the paper reports 0.498±0.004, so I need to find the third seed's value, likely in the d048_eval_ss_s456 data where I can see tf_gar_ours_mid at 0.4964.

Computing the mean and standard deviation across all three seeds—0.4983, 0.503, and 0.4964—gives me approximately 0.499±0.001, which is close to the reported 0.498±0.004 but not quite matching. The discrepancy suggests the paper might be using a slightly different calculation or data source.

Looking at the d048 unified evaluation results, I notice there's a labeling issue: the s42 entry shows 0.5025 but is marked as a TG model rather than SS, so I'm not sure if that's the right value to use. The other two seeds (s123 at 0.5536 and s456 at 0.4964) seem consistent, but this inconsistency is worth flagging for verification rather than getting stuck on it.

Now I'm pulling together the key metrics across all three seeds to verify the averages. For the multi-seed SS results with AR and β=0, I'm extracting the GAR scores from each experiment (0.347, 0.4231, 0.4325) which average to about 0.401 with a standard deviation around 0.047. Similarly, the perplexity values (1.442, 1.4408, 1.4394) are clustering tightly around 1.4407. Completing the calculation for the mean, I get 0.717, which matches the paper's reported value. The standard deviation is indeed very small, around 0.001. The paper's notation "std 0.047→0.001" is clarifying that steering reduces the variance across seeds from 0.047 at β=0 down to 0.001 at β=5, which all checks out. Now I'm moving on to examine the gap ratio metrics.

The gap ratio calculation gives 0.50 / 0.064 = 7.8×, matching the paper's reported value. However, if I use the held-out measurement of 0.5035 instead, I get 7.87, which rounds to 7.9×. This discrepancy is the gap ratio inconsistency I noted earlier. For the base model, the numbers don't show a meaningful gap since the adversarial robustness (0.019) actually exceeds the task-free measurement (0.01), which is unexpected.

Looking at the full range across all fine-tuned variants—TG at 7.8×, UG at 14.8×, LoRA-only at 13.5×, and PCGrad at 16.7×—the actual span is approximately 7.8 to 16.7×. The paper rounds this to 8–17×, which is reasonable since 7.8 rounds up to 8 and 16.7 rounds to 17.

Now checking the SS gap compression claim: TF shows 0.498 and AR shows 0.401, giving a ratio of 1.24×. The paper states "~1.3×", which seems like an overstatement—1.24× is closer to 1.2× even with the wiggle room the tilde provides.

But looking at the seed-specific data, s42 alone yields 0.5025/0.3887 = 1.29×, which aligns better with the paper's claim. The discrepancy appears to hinge on whether we're averaging per-seed ratios or computing the ratio from averaged values, and the exact values used for each seed. Looking at the multi-seed average approach, the ratio comes out to around 1.24× when dividing the mean performance gap by mean AR—closer to 1.2× than the paper's claimed 1.3×. The per-seed calculation gets complicated since I only have the unified N=50 AR value for s42 while the others come from their individual evaluations, so I'll note this discrepancy and move forward.

For MMLU, the gap between base and the lowest performing variant is 0.77 percentage points, which fits within the stated 0.8 pp threshold. Now checking the Qwen GAR decay claim against the phase 1 diagnostic data. relative_drop = 0.708 = 70.8%
Paper says "over 70%" ✓
Also says "70.8%" in related work section ✓

**AUC = 0.98:**
This is from Dongre et al., not our experiment. Will mark as literature reference.

**~57K parameters, <0.001%:**
Qwen-2.5-7B has 7B parameters. 57K / 7B = 0.0000081 = 0.00081% ≈ 0.001%
Paper says "<0.001%" — let me check: 57000/7000000000 = 0.00000814 = 0.000814%
That's 0.000814%, which IS less than 0.001%. ✓

0.001% of 7B equals 70,000, and since 57K is less than that threshold, the parameter count checks out. ✓

**Per-turn decay 85-90% (caption of Figure 1):**
Looking at the attention heatmap analysis, I'm seeing decay rates of 77.7% for TG, 80.3% for UG, 81.0% for LoRA, and 87.5% for the base model. The caption claims 85-90%, but TG doesn't fall in that range. The caption might be describing a different measurement from Figure 1(a) than what the pilot AR evaluation analysis shows, so I need to figure out which metric the caption is actually referencing.

The caption specifically mentions "Goal attention decays 85--90% across turns under AR generation on both Qwen-2.5-7B and Llama-3.1-8B." The 85-90% range could be an average across both architectures, or it might apply to the base models specifically. The base Qwen shows 87.5%, which fits the range, and Llama might be similar. But the fine-tuned variants (77-81%) don't match. There's a potential inconsistency here—the analysis.tex mentions "77--87% per-turn decay" for Figure 4, while the Figure 1 caption says 85-90%. I need to determine if these are measuring different things or if there's a discrepancy in the reported numbers. Looking at the per-turn GAR values, I can see the decay from turn 1 to turn 10 is about 84.7%, which aligns with the 85-90% figure caption claim. The relative drop between mid-turns and turn 1 is lower at 70.8%, so the caption is specifically referring to the first-to-last turn comparison rather than the overall average decay.

Now checking the TF-AR gap claims in Figure 1 — the 8-17× range on the log scale checks out at 7.8-16.7×, though the lower bound rounds up slightly. For Qwen, the gap narrows from 7.8× to around 1.3×, and I need to verify that 1.3× figure more carefully.

For Llama, the initial gap of ~27× comes from dividing the TG TF performance (0.484) by the AR median (0.018), which gives 26.9×. The final gap of 2.9× comes from the SS configuration where TF is 0.477 and AR is 0.166, yielding 2.87×. The analysis.tex file mentions gaps of 27× and 26× for the TG and LoRA-only setups respectively. So the gap calculations check out: TG gives 27.0×, LoRA-only is 26.1×, and the paper's rounded medians of 0.018 and 0.009 match the actual registry values when rounded. ✓

Now I'm verifying the other key metrics from the paper against the registry. The McNemar p-value of 0.0771 rounds to 0.077, the late-turn performance delta is 11.1 percentage points, content-constrained shows a 23.8 pp improvement, and the GAR-compliance correlation of 0.2003 rounds to 0.200 with a p-value of 0.007. All these values align with what's reported. ✓

For the TRC values, I'm checking ThreadGate's numbers: the transfer and generation TRC values of 0.3339 and 0.3323 both round correctly to 0.334 and 0.332, with the gap of 0.0016 rounding to 0.002. The LoRA-only configuration shows 0.349 for transfer TRC and 0.4106 for generation TRC, matching the paper's reported 0.349 and 0.411, with a gap of −0.0617 rounding to −0.062.

Now I'm verifying the gradient analysis metrics: the layer percentages across epochs range from 67.9% to 78.6%, which fits the paper's 68–79% range, the cosine similarity values match exactly at −0.089 and −0.042, and the NTP magnitude dominance grows from 7.5× to 14.7× as reported.

For the PCGrad comparison, I see TG at 0.064 versus PCGrad at 0.030, but the p=0.002 significance claim isn't directly in the registry data I'm checking—same problem with the p=0.004 for TG versus LoRA-only, so I'm flagging both as needing verification.

On the gate values, the registry shows TG's mean gate at 0.9336 with standard deviation around 0.05, which matches Table 1's .93 ±.05 notation. The range 0.93–0.98 represents the inference-time span, translating to 2–7% attenuation (since 1 - 0.98 = 2% and 1 - 0.93 = 7%).

For Layer 23, the shift from 0.769 to 0.979 comes from the gate turn conditioning analysis comparing turn 1 versus turn 21, though this specific data point isn't directly in the registry—I'll note the traceability as unclear but the numbers themselves appear sound.

The Llama cosine similarity of +0.005 aligns with the registry's cos_sim_mean of 0.0045, and the 25.7× NTP magnitude dominance matches the registry's mag_ratio_median exactly.

Now checking the Qwen and Llama SS results where β=3 triggers recovery on Qwen SS (0.593) but not on Llama SS (0.173)...

For the Qwen SS β=3 value, I found it in d048_final_ar_eval at beta3.ss_gar = 0.593. But the Llama SS β=3 value of 0.173 isn't showing up in the p1_llama_ss_eval registry, which only has β=0 and β=5 entries—I'll flag this as missing source data. The Llama β=5 GAR of 0.791 matches the registry's ss_ar_b5_gar of 0.7905, which is close enough given rounding.

Now I'm checking the Qwen 1.5B GAR decay of 79.8% against the registry. The qwen15b_phase1_diag entry shows success but the metrics aren't displayed in the summary, though the tab_qwen15b_results table does show the 79.8% figure.

Looking at the actual numbers: the turn-1 GAR is 0.0336 and mid-turn GAR is 0.0068, which gives a relative drop of about 79.8% when I calculate it out. The β-steering recovery shows 0.715 at β=5, and I'm now cross-referencing the GAR-Dongre baseline values from Table 1 to verify the 0.01-0.02 range. The 1.28× shift for Qwen GAR-Dongre comes from the analysis—I need to find the actual AR value since the table only shows the TF result of 0.02. Looking at the held-out metrics, the TF value is around 0.0152, but I'm still tracking down where the AR GAR-Dongre measurement appears in the evaluation data. The gate_kl_correlation metric shows 0.11, which doesn't align with the paper's claim about heads with higher TF GAR shifting most under AR at r=0.743—this likely comes from a separate analysis I need to flag. The β=5 convergence point checks out with the experimental data showing SS at 0.717 and TG at 0.727. Now I'm verifying the PPL cost claims, starting with the 9% figure at β=3 against the baseline PPL values. I'm verifying the GAR and PPL values at β=5 against the experimental data. The GAR of 0.727±0.061 matches the results, where the standard deviation rounds to 0.061, and the PPL of 1.77 also checks out against the recorded measurements.

Looking at the operating region across β∈[3,5], both endpoints exceed the baseline GAR threshold of ~0.50 while keeping PPL below 1.8. Now I'm cross-referencing the perplexity claim from the experiments section—all fine-tuned variants show PPL of 2.78 in both evaluation protocols. Finally, checking the consistency between IID and held-out evaluation protocols: the method rankings remain stable across both, with GAR differences staying within 1 percentage point. I'm seeing the actual difference is 1.3 percentage points when I look at the precise values, but the table rounds to 0.49 and 0.51, which displays as a 2 pp gap. The paper claims "≤1 pp" but that's inaccurate—even the unrounded 1.3 pp exceeds that threshold. Let me dig into the raw registry data to verify these numbers across all variants. I'm realizing the "≤1 pp" claim might be referring to the spread among the fine-tuned variants in the held-out setting rather than the IID-versus-held-out difference. Looking at the held-out values across TG, UG, LO, and PCGrad, the spread is roughly 0.75 pp, which rounds to about 1 pp. Let me check what the paper actually says to clarify this interpretation. Looking at the reported table values more carefully, the IID-to-held-out differences are actually larger than claimed — UG shows a 2 pp swing from 0.49 to 0.51, which contradicts the "≤1 pp" statement, so the claim should probably be "≤2 pp" to match what the data actually shows. Looking at the full range across both IID and held-out evaluations, GAR-ours spans from 0.49 to 0.51, which checks out as 2 pp. For the second seed stability claim, I'm seeing TF values of 0.5035 and 0.5052 across the two seeds, which average to 0.5044—but the paper reports 0.504±0.001, and I need to verify if that uncertainty represents half the range between these two measurements.

Now checking the Llama results against the paper's reported figures, where TF GAR-ours is listed as 0.484 for TG and 0.481 for LoRA-only, and my evaluation shows 0.4836 for the TG variant, which rounds correctly to 0.484.

For the LoRA-only variant, I'm getting 0.4807, which also rounds to 0.481 as expected. The coefficient of variation for TG AR is quite high at 230%, well above the 100% threshold, confirming significant variability. I'm also verifying the gate values—Llama shows L25 at 0.719 and Qwen shows L1 at 0.793, though I notice the Qwen data is from s123 rather than s42, so I need to check if the s42 variant is available elsewhere.

Looking more carefully at the analysis, it references "Qwen attenuates early layers (L1=0.793)" from the s123 run, but the main experiments use s42 as the primary seed. I should verify whether s42 has its own L1 measurement or if I need to use different layer values from the s42 gate profile that shows L3=0.801 and L4=0.789 as the minimum points. The general pattern of early layer attenuation holds across both seeds, though the specific L1=0.793 value comes from s123 rather than s42, which uses L3 and L4 as its lowest gates. For Qwen 1.5B, the β-steering recovery to 0.715 checks out against the results table. Now I need to verify the gap ratio discrepancy—the paper consistently uses 7.8× in the body (0.50/0.064), but depending on which TF value is used, it could round to 7.9×, and the held-out TF in the table is 0.50.

For the SS gap, the per-seed value from s42 gives 1.29× while the multi-seed average is 1.24×, so the paper's "~1.3×" is accurate for s42 but slightly overstates the average. The "≤1pp" claim in experiments.tex also needs checking—the actual maximum difference across variants appears to be 1.3-1.7 pp, which exceeds that bound.

The PPL standard deviation claim checks out: across the three seeds I get values of 1.442, 1.4408, and 1.4394, which average to 1.4407 with a standard deviation of 0.0013, rounding to ±0.001 as stated.

Now I'm verifying the Figure 4 caption claims about attention decay rates. The ThreadGate decay is 77.7% and LoRA-only is 81.0%, giving a difference of 3.3 pp, which matches what's reported.

For the Figure 1 caption's "85-90% across turns" claim, this appears to measure a different metric than the attention heatmap analysis. Looking at the goal attention drop data, I can calculate the decay from turn 1 to turn 10 as roughly 84.7%, which aligns with the 85% lower bound. The base Qwen model shows 87.5% decay, so the range seems consistent across the models tested. Looking at the actual numbers, the 85-90% claim seems to apply only to base models—Qwen base hits 87.5% while the fine-tuned variants (TG, UG, LoRA) all fall in the 77-81% range. The caption's wording suggests it covers all variants, but that's inconsistent with what the data shows, so I should note this discrepancy. Looking at the base model decay rates, Qwen-2.5-7B's 87.5% falls within the 85-90% range mentioned, so that checks out. For Llama-3.1-8B, I'd need to verify the per-turn decay data, but the range seems plausible for base models. The fine-tuned variants showing 77-81% decay is a separate finding from Fig 4. Now I'm cross-referencing some numbers from the related work section—the 27-48% figure is from another paper's work, the 70.8% decline on Qwen-2.5-7B matches the phase1 GAR diagnostic data.

For the method section, GAR-Dongre dilutes down to 0.01-0.02 as expected, and our approach maintains a wider range from 0.019 to 0.50 across different settings—that's roughly 26× difference or about 1.4 orders of magnitude. The correlation test shows r=0.200 with p=0.007, which aligns with the instruction retention analysis. Now checking the layer-wise compliance metrics where L3 reaches 0.777 and L27 hits 1.000. I'm verifying the experimental parameters against the documented specs: the learning rate of 0.0002 with gradient accumulation of 8 checks out, the dataset contains 8,000 multi-turn conversations as stated, training ran for 3 epochs completing in approximately 6 hours, and the GPU used was an NVIDIA RTX PRO 6000 Black.

There's a discrepancy with the GPU memory though—the paper specifies 96 GB, but the registry shows 102 GB for the Llama run, while the Qwen runs don't list GPU specs. However, checking the phase2 notes shows the actual total GPU memory was around 94.97 GB, which aligns with the 96 GB nominal specification for the RTX PRO 6000.

Now I'm verifying the experimental details against the paper. The AR evaluation used 50 held-out conversations with a mean of 3.6 user turns per conversation. For Figure 2, I'm checking the attention steering results where β=3 produces a GAR of 0.556 with a 9% PPL cost—the registry confirms the GAR value rounds correctly, and I'm calculating the PPL cost differential.

Looking at cross-section consistency, the key numbers that recur throughout the paper are the order of magnitude gap between methods (8-17×), the GAR = 0.50 threshold for task feasibility, and the ~1.3× semantic similarity gap mentioned in both the introduction and experiments section. I'm verifying that the beta coefficients and standard error measurements are consistently cited across the experimental sections and discussion, and they all check out. The key metrics like the GAR decline percentages and the various accuracy and perplexity measurements are properly documented in their source sections. Now I'm looking at the known discrepancies flagged in the appendix audit, starting with the 7.8× versus 7.9× gap ratio issue.

The body text consistently uses 7.8× derived from the rounded table values of 0.50/0.064, though there's a secondary mention of TF stability at 0.504±0.001 which would compute to approximately 7.9×. This precision difference between how the table presents the value versus how it appears in the text creates a minor tension, but since the primary claim relies on the table values, it's defensible. Now I'm checking the second flagged inconsistency about the SS gap ratio. Looking at the held-out evaluation results, the spread between variants is at most 1 percentage point, which supports the "≤1 pp" claim. But the sentence structure is genuinely ambiguous—"differs" could mean either the spread among fine-tuned variants or the difference between IID and held-out protocols, and I need to determine which interpretation the authors intended. the held-out values differ from IID values by ≤1 pp.

In that case: max IID-held-out diff = 1.7 pp (for TG: 0.4866 vs 0.5035). So "≤1 pp" is wrong — should be "≤2 pp".

Wait, TG IID is 0.4866 which rounds to 0.49 in the table, and TG held-out is 0.5035 which rounds to 0.50. So the difference at table precision is 1 pp (0.50 - 0.49). For UG: IID 0.4923 → 0.49, held-out 0.5053 → 0.51, diff = 2 pp.

At table precision, the max difference is 2 pp for UG, while the raw precision shows 1.7 pp for TG. Either way, the claim of ≤1 pp doesn't hold up. I've tried other interpretations—looking at individual configurations, the differences still exceed 1 pp for most cases. This needs to be flagged as an error: the statement should say "≤2 pp" instead.

Now checking the PPL standard deviation claim where the paper reports 1.441±0.001 but my calculations show a different value. I'm verifying the GAR-Dongre comparison claim — the Qwen ratio of 1.28× matches the data, confirming that ≤1.3× is accurate. Now I need to track down the actual AR GAR-Dongre value for Qwen to complete this verification. I'm seeing a discrepancy between the two Llama evaluation datasets—the matched eval gives 1.002× while the other setup shows 0.83—which comes down to their different configurations (N=50 TF/N=5 AR versus N=20 AR matched). The paper uses the matched figure, which makes sense for a direct comparison. For Qwen's 1.28×, I can't find a clear source in the data, so I'll need to flag that as uncertain.

Now I'm organizing the main findings into confirmed issues and potential precision concerns. The key problems are the "≤1 pp" claim that should be "≤2 pp" based on the UG IID-held-out difference, the "~1.3×" SS gap being slightly high when the multi-seed average is 1.24×, and the Fig 1(a) caption overstating the range for fine-tuned variants. There's also a minor precision question about whether the gap ratio should be 7.8× or 7.9× depending on rounding choices in the TF value.

Several statistics and metrics lack clear registry sources—the p-values for PCGrad and TG comparisons, the per-head correlation coefficient, the layer 23 shift values, and the Llama SS β parameter—but these appear to come from analysis scripts rather than being outright errors. Most other numbers in the paper check out against the available data, so I'm ready to compile the full audit report.

Let me double-check the TF stability claim by looking at the two seed runs: v7_tg_s42 gives 0.5035 and v7_tg_s123 gives 0.5052. The mean works out to 0.5044 (which rounds to 0.504) and the half-range is 0.0009 (which rounds to ±0.001), so the paper's reported value of 0.504±0.001 is accurate.

Now I'm noticing that s42 uses held-out evaluation while s123 uses IID evaluation—different protocols entirely. The paper doesn't clarify whether these should be averaged together, but the difference is negligible enough that it doesn't affect the conclusion.

Moving forward with the full verification. I should also check a few other numbers I might have overlooked. The architecture details like projecting to 16 dimensions, the 32-dimensional input through a 64-unit hidden layer, and σmin = 0.05 are all design choices rather than empirical results to validate. The math on the input dimensions checks out: 32 comes from 16 (projected hidden) plus 16 (turn embedding).

Now I'm looking at the experimental specifications to verify the reported numbers. Gradient accumulation is set to 8 in the phase2 spec, and the ThreadGate variant with seed 123 does exist in the registry. For the GAR-ours performance range of 0.49–0.51, I'm cross-checking against both the IID and held-out results across different methods. I'm noticing a discrepancy between the raw values and what's shown in the table — 0.4866 should round to 0.49 at two decimal places, but the table displays 0.50 for TG IID. Let me check whether the table values are actually derived from the evaluation results or if they come from a different source. the table might be using a different data source or a more precise intermediate value that rounds to 0.50. Let me check the actual LaTeX in related_work.tex to see what's there. The IID value of 0.4866 should round to 0.49, so either there's a rounding discrepancy in the table or the eval results I'm looking at aren't the final source. The held-out perplexity of 2.78 matches the table, but the IID perplexity discrepancy (2.63 vs 2.78) suggests the table might be using held-out data for both columns, or the IID evaluation was recalculated. Looking at the evaluation protocol description, IID refers to same-distribution but different conversations, while held-out uses 50 non-overlapping conversations—both are teacher-forced evaluations. contain the correct IID data after all—the base PPL values match the registry entries, so the table's IID and held-out columns are genuinely different datasets, not duplicates.

But there's a rounding discrepancy with the TG IID GAR-O value: it shows 0.50 in the table, yet the raw value of 0.4866 should round to 0.49 at two decimal places, not 0.50. This appears to be an actual rounding error in the table itself. Looking at the table values more carefully, I'm seeing a pattern where TG shows 0.50 for both IID and held-out GAR-O, while UG shows 0.49 for IID but 0.51 for held-out. This discrepancy between the registry value of 0.4866 and the table's 0.50 for TG IID is worth flagging as a potential rounding inconsistency. The TG and LoRA-only IID values are clearly off—0.4866 and 0.4860 shouldn't round to 0.50. More importantly, the PPL values don't match the registry either: the registry shows 2.63 for TG IID but the table has 2.78. Since the base PPL of 4.23 matches, it seems like the fine-tuned models' IID evaluation might have been re-run with different data or a different source than what's currently in the registry.

Actually, I'm noticing something odd—the phase2_4way_eval_heldout data shows 2.78 for TG PPL, which exactly matches what's in the table's IID column. That's suspicious, like the table might be pulling held-out values instead of true IID values for the fine-tuned variants. Though to be fair, IID and held-out PPL being similar makes sense if they're just using different conversation data, so it could be coincidental.

But the bigger picture is that the base model's IID PPL of 4.23 in the table matches phase2_4way_eval, suggesting that experiment is the source. The fact that only the fine-tuned models show this discrepancy suggests maybe the IID eval was re-run later with different parameters or data subsets specifically for those variants. I'm noticing the fine-tuned models show identical PPL of 2.78 across both IID and held-out evaluations, which seems suspicious given that phase2_4way_eval reports 2.63 for IID. This discrepancy suggests either the table uses a different evaluation protocol or there's an inconsistency in the reported numbers that I should flag. I can't find another explicit IID evaluation for the fine-tuned models in the experiment list, though the data could be from training logs or an unregistered eval run. I'll note this discrepancy and move forward with the report. Now I'm checking the Abstract claims against the experimental results — the exposure bias and attention collapse findings are well-supported by the data, with the quantitative gaps matching the stated magnitudes. Now I'm tallying up all the quantitative claims across the paper—roughly three from the abstract, about a dozen from the introduction, fifteen or so from the methods section, and around forty from the experiments including all the table values and statistical tests.

The analysis section adds another thirty-five numbers covering gate values and gradient statistics, while the discussion, conclusion, and related work sections contribute another sixteen combined. I'm also accounting for numbers in figure captions and the tables in the related work file, bringing the total to approximately 160 quantitative claims throughout the paper.

Given this complexity, I'll need to use an agent to help write the report.

Actually, I realize I have all the data I need now—I should write this myself. Let me structure the report with summary statistics first, then per-section audit tables, a cross-section consistency check, an issue list, and finally a section for numbers without registry sources. Now I'll write the full report to the output path.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "80e4278d-a31e-4ea2-9d79-1cb2ce910f7f",
  "isSidechain": false,
  "requestId": "req_011CbPw8hWNVFKwb85eNq4q5",
  "type": "assistant",
  "uuid": "40e8a1df-bced-4d13-bbf9-b34c1656cdaf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "4b680861-4da7-411a-8744-3dabfdaf2205",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Go3osTGCp3zWh9UuGTgtH9",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1176,
      "cache_read_input_tokens": 76403,
      "output_tokens": 26718,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1176,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 26718,
          "cache_read_input_tokens": 76403,
          "cache_creation_input_tokens": 1176,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1176
          },
          "type": "message"
        }
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

_source line 97 · 2026-05-25T20:48:59.909Z_

I now have all the data needed for a comprehensive audit. Let me verify a few more specific numbers, particularly for the table data and some edge cases.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "40e8a1df-bced-4d13-bbf9-b34c1656cdaf",
  "isSidechain": false,
  "requestId": "req_011CbPw8hWNVFKwb85eNq4q5",
  "type": "assistant",
  "uuid": "075df58d-6e56-4003-841f-7a3711237576",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "4b680861-4da7-411a-8744-3dabfdaf2205",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Go3osTGCp3zWh9UuGTgtH9",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1176,
      "cache_read_input_tokens": 76403,
      "output_tokens": 26718,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1176,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 26718,
          "cache_read_input_tokens": 76403,
          "cache_creation_input_tokens": 1176,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1176
          },
          "type": "message"
        }
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

_source line 98 · 2026-05-25T20:49:23.957Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01Xx1GjS8cLSqMrsArpHyaaA`</summary>

```json
{
  "command": "python3 << 'PYEOF'\nimport json\n\nREGISTRY = \"/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-11-projects-turn-residual-gating/4b680861-4da7-411a-8744-3dabfdaf2205/tool-results/mcp-agent-ml-research-read_registry-1779741484333.txt\"\ndata = json.load(open(REGISTRY))\nresult = json.loads(data['result'])\nexperiments = result['data']['experiments']\n\n# Also check qwen15b full data\nexp = experiments.get('qwen15b_phase1_diag', {})\nprint(\"=== qwen15b_phase1_diag full ===\")\nfor k, v in exp.items():\n    if k not in ('created_at', 'updated_at', 'retry_count'):\n        val = json.dumps(v, indent=2) if isinstance(v, (dict, list)) else str(v)\n        print(f\"  {k}: {val[:1000]}\")\n\n# Also check phase1a_multiseed_qwen\nprint(\"\\n=== phase1a_multiseed_qwen ===\")\nexp2 = experiments.get('phase1a_multiseed_qwen', {})\nfor k, v in exp2.items():\n    if k not in ('created_at', 'updated_at', 'retry_count'):\n        val = json.dumps(v, indent=2) if isinstance(v, (dict, list)) else str(v)\n        print(f\"  {k}: {val[:1000]}\")\n\n# Check gradient_analysis (alias)\nprint(\"\\n=== looking for gradient_analysis ===\")\nfor eid in experiments:\n    if 'gradient' in eid.lower():\n        print(f\"  found: {eid}\")\n\n# Also get SS multi-seed computation\n# s42\nss_s42_ar = 0.347  # d048_final_ar_eval\nss_s123_ar = 0.4231  # d048_eval_ss_s123\nss_s456_ar = 0.4325  # d048_eval_ss_s456\n\nimport statistics\nvals = [ss_s42_ar, ss_s123_ar, ss_s456_ar]\nmean = statistics.mean(vals)\nstd = statistics.stdev(vals)\nprint(f\"\\nSS AR multi-seed: mean={mean:.4f}, std={std:.4f}\")\nprint(f\"  Paper claims: 0.401±0.047\")\nprint(f\"  Match: mean {'✓' if abs(mean - 0.401) < 0.001 else '✗'}, std {'✓' if abs(std - 0.047) < 0.002 else '✗'}\")\n\n# SS PPL multi-seed\nppl_vals = [1.442, 1.4408, 1.4394]\nppl_mean = statistics.mean(ppl_vals)\nppl_std = statistics.stdev(ppl_vals)\nprint(f\"\\nSS PPL multi-seed: mean={ppl_mean:.4f}, std={ppl_std:.4f}\")\nprint(f\"  Paper claims: 1.441±0.001\")\nprint(f\"  Match: mean {'✓' if abs(ppl_mean - 1.441) < 0.001 else '✗'}, std {'✓' if abs(ppl_std - 0.001) < 0.001 else '✗'}\")\n\n# SS β=5 GAR multi-seed\nb5_vals = [0.717, 0.7174, 0.7157]\nb5_mean = statistics.mean(b5_vals)\nb5_std = statistics.stdev(b5_vals)\nprint(f\"\\nSS β=5 multi-seed: mean={b5_mean:.4f}, std={b5_std:.4f}\")\nprint(f\"  Paper claims: 0.717±0.001\")\n\n# Gap ratio computation\nprint(f\"\\nGap ratios:\")\nprint(f\"  TG: 0.50/0.064 = {0.50/0.064:.2f}x (paper: 7.8x)\")\nprint(f\"  TG precise: 0.5035/0.064 = {0.5035/0.064:.2f}x\")\nprint(f\"  UG: 0.49/0.033 = {0.49/0.033:.1f}x\")\nprint(f\"  LO: 0.50/0.037 = {0.50/0.037:.1f}x\")\nprint(f\"  PC: 0.50/0.030 = {0.50/0.030:.1f}x\")\n\n# SS gap ratio\nprint(f\"\\nSS gap ratio:\")\nprint(f\"  Multi-seed: {mean}/{0.498:.3f} = ..., let me use TF values\")\n# We need SS TF values\n# eval_v8b_ss s42: 0.4983\n# eval_v8b_ss_s123: 0.503\n# d048_eval_ss_s456: tf_gar_ours_mid = 0.4964\nss_tf_vals = [0.4983, 0.503, 0.4964]\nss_tf_mean = statistics.mean(ss_tf_vals)\nss_tf_std = statistics.stdev(ss_tf_vals)\nprint(f\"  SS TF multi-seed: mean={ss_tf_mean:.4f}, std={ss_tf_std:.4f}\")\nprint(f\"  Paper claims TF: 0.498±0.004\")\nprint(f\"  Gap ratio = {ss_tf_mean/mean:.3f}\")\nprint(f\"  Paper claims gap: ~1.3x\")\nPYEOF\n",
  "description": "Compute multi-seed SS statistics and gap ratios",
  "timeout": 15000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "075df58d-6e56-4003-841f-7a3711237576",
  "isSidechain": false,
  "requestId": "req_011CbPw8hWNVFKwb85eNq4q5",
  "type": "assistant",
  "uuid": "755055e4-adac-4843-a14d-c24bb1451fc7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "4b680861-4da7-411a-8744-3dabfdaf2205",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Go3osTGCp3zWh9UuGTgtH9",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1176,
      "cache_read_input_tokens": 76403,
      "output_tokens": 26718,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1176,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 26718,
          "cache_read_input_tokens": 76403,
          "cache_creation_input_tokens": 1176,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1176
          },
          "type": "message"
        }
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

_source line 99 · 2026-05-25T20:49:24.061Z_

<details><summary>↩ Tool result · `toolu_01Xx1GjS8cLSqMrsArpHyaaA`</summary>

```text
=== qwen15b_phase1_diag full ===
  status: DONE
  hypothesis: GAR attention decay toward system-prompt goal tokens is a general phenomenon across model scales, not specific to 7B. Qwen-2.5-1.5B-Instruct should also show progressive GAR decline across conversation turns, confirming the phenomenon is architecture-level rather than scale-dependent.
  spec: {
  "command": "python train_phase2.py --model Qwen/Qwen2.5-1.5B-Instruct --config configs/tg_v7.yaml --seed 42 --epochs 3",
  "server": "westd-20861",
  "data_path": "/root/turn-residual-gating/data/train_400.json",
  "data_count": 400,
  "model_name": "Qwen/Qwen2.5-1.5B-Instruct",
  "seed": 42,
  "checkpoint_path": "runs/qwen15b_tg_v7_s42/",
  "log_path": "logs/qwen15b_phase1_diag.log"
}
  conclusion: success
  completed_at: 2026-05-24T06:53:23.496Z

=== phase1a_multiseed_qwen ===
  status: DONE
  hypothesis: Multi-seed (s123, s456) training across 5 Qwen conditions (PCGrad, UG, LoRA-only, TG, SS) to establish mean±std for all claims. 8 training runs + AR eval N≥50 each. Expect TF convergence (GAR~0.50) and consistent AR rankings across seeds.
  spec: {
  "command": "python src/train_phase2_v9_pcgrad.py",
  "server": "westd-20861",
  "data_path": "data/ultrachat_8k",
  "data_count": 8000,
  "model_name": "Qwen2.5-7B-Instruct",
  "seed": 123,
  "checkpoint_path": "N/A",
  "log_path": "runs/d048_pcgrad_s123"
}
  conclusion: killed
  notes: 用户要求停止：30min 内无法完成。PCGrad s123 在 1800/3000 步时被终止，后续 7 个排队任务全部取消。
  checkpoint_path: N/A
  log_path: runs/d048_pcgrad_s123
  completed_at: 2026-05-25T11:20:34.089Z

=== looking for gradient_analysis ===
  found: p2_llama_gradient_conflict
  found: analysis_gradient_conflict

SS AR multi-seed: mean=0.4009, std=0.0469
  Paper claims: 0.401±0.047
  Match: mean ✓, std ✓

SS PPL multi-seed: mean=1.4407, std=0.0013
  Paper claims: 1.441±0.001
  Match: mean ✓, std ✓

SS β=5 multi-seed: mean=0.7167, std=0.0009
  Paper claims: 0.717±0.001

Gap ratios:
  TG: 0.50/0.064 = 7.81x (paper: 7.8x)
  TG precise: 0.5035/0.064 = 7.87x
  UG: 0.49/0.033 = 14.8x
  LO: 0.50/0.037 = 13.5x
  PC: 0.50/0.030 = 16.7x

SS gap ratio:
  Multi-seed: 0.40086666666666665/0.498 = ..., let me use TF values
  SS TF multi-seed: mean=0.4992, std=0.0034
  Paper claims TF: 0.498±0.004
  Gap ratio = 1.245
  Paper claims gap: ~1.3x
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "755055e4-adac-4843-a14d-c24bb1451fc7",
  "isSidechain": false,
  "promptId": "8817af8a-f189-44e8-a462-1453a12b4ea3",
  "type": "user",
  "uuid": "d3475b86-2166-4680-a5bd-cfee6b3a97ae",
  "toolUseResult": {
    "stdout": "=== qwen15b_phase1_diag full ===\n  status: DONE\n  hypothesis: GAR attention decay toward system-prompt goal tokens is a general phenomenon across model scales, not specific to 7B. Qwen-2.5-1.5B-Instruct should also show progressive GAR decline across conversation turns, confirming the phenomenon is architecture-level rather than scale-dependent.\n  spec: {\n  \"command\": \"python train_phase2.py --model Qwen/Qwen2.5-1.5B-Instruct --config configs/tg_v7.yaml --seed 42 --epochs 3\",\n  \"server\": \"westd-20861\",\n  \"data_path\": \"/root/turn-residual-gating/data/train_400.json\",\n  \"data_count\": 400,\n  \"model_name\": \"Qwen/Qwen2.5-1.5B-Instruct\",\n  \"seed\": 42,\n  \"checkpoint_path\": \"runs/qwen15b_tg_v7_s42/\",\n  \"log_path\": \"logs/qwen15b_phase1_diag.log\"\n}\n  conclusion: success\n  completed_at: 2026-05-24T06:53:23.496Z\n\n=== phase1a_multiseed_qwen ===\n  status: DONE\n  hypothesis: Multi-seed (s123, s456) training across 5 Qwen conditions (PCGrad, UG, LoRA-only, TG, SS) to establish mean±std for all claims. 8 training runs + AR eval N≥50 each. Expect TF convergence (GAR~0.50) and consistent AR rankings across seeds.\n  spec: {\n  \"command\": \"python src/train_phase2_v9_pcgrad.py\",\n  \"server\": \"westd-20861\",\n  \"data_path\": \"data/ultrachat_8k\",\n  \"data_count\": 8000,\n  \"model_name\": \"Qwen2.5-7B-Instruct\",\n  \"seed\": 123,\n  \"checkpoint_path\": \"N/A\",\n  \"log_path\": \"runs/d048_pcgrad_s123\"\n}\n  conclusion: killed\n  notes: 用户要求停止：30min 内无法完成。PCGrad s123 在 1800/3000 步时被终止，后续 7 个排队任务全部取消。\n  checkpoint_path: N/A\n  log_path: runs/d048_pcgrad_s123\n  completed_at: 2026-05-25T11:20:34.089Z\n\n=== looking for gradient_analysis ===\n  found: p2_llama_gradient_conflict\n  found: analysis_gradient_conflict\n\nSS AR multi-seed: mean=0.4009, std=0.0469\n  Paper claims: 0.401±0.047\n  Match: mean ✓, std ✓\n\nSS PPL multi-seed: mean=1.4407, std=0.0013\n  Paper claims: 1.441±0.001\n  Match: mean ✓, std ✓\n\nSS β=5 multi-seed: mean=0.7167, std=0.0009\n  Paper claims: 0.717±0.001\n\nGap ratios:\n  TG: 0.50/0.064 = 7.81x (paper: 7.8x)\n  TG precise: 0.5035/0.064 = 7.87x\n  UG: 0.49/0.033 = 14.8x\n  LO: 0.50/0.037 = 13.5x\n  PC: 0.50/0.030 = 16.7x\n\nSS gap ratio:\n  Multi-seed: 0.40086666666666665/0.498 = ..., let me use TF values\n  SS TF multi-seed: mean=0.4992, std=0.0034\n  Paper claims TF: 0.498±0.004\n  Gap ratio = 1.245\n  Paper claims gap: ~1.3x",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "755055e4-adac-4843-a14d-c24bb1451fc7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "4b680861-4da7-411a-8744-3dabfdaf2205",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Runtime record

_source line 100_

```json
{
  "type": "last-prompt",
  "leafUuid": "d3475b86-2166-4680-a5bd-cfee6b3a97ae",
  "sessionId": "4b680861-4da7-411a-8744-3dabfdaf2205"
}
```

---

### Runtime record

_source line 101_

```json
{
  "type": "ai-title",
  "aiTitle": "Audit quantitative claims in paper body text",
  "sessionId": "4b680861-4da7-411a-8744-3dabfdaf2205"
}
```

---

### Assistant

_source line 102 · 2026-05-25T20:50:31.265Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the data needed. Let me note the key findings:

1. SS TF mean = 0.4992 (paper claims 0.498 — off by 0.001, not matching at 3dp)
   Wait, 0.4992 rounds to 0.499, not 0.498. But the paper says 0.498.
   This is a minor discrepancy. The TF values I used are:
   - eval_v8b_ss (s42): 0.4983
   - eval_v8b_ss_s123 (s123): 0.503
   - d048_eval_ss_s456 (s456): 0.4964
   Mean = 0.4992 → rounds to 0.499, not 0.498.
   
   The standard deviation I computed is 0.0034, which rounds to 0.003, whereas the paper reports ±0.004. So there's a slight mismatch between my calculation of 0.499±0.003 and the paper's reported 0.498±0.004 — likely due to different source data or rounding conventions.

The gap ratio of 1.245 is closer to 1.2× than the paper's claim of ~1.3×, and similarly the standard deviation rounds down to 0.003 rather than 0.004. Let me verify which model's TF values I should be using here, since I'm seeing some confusion between the SS model's performance and the TG model's metrics.

Looking at the actual SS model evaluations across the three seeds, I'm getting TF GAR values of 0.4983, 0.503, and 0.4964, which average to 0.4992 with a standard deviation of 0.0034. The d048 file also shows a TG model evaluation at 0.5025, which is labeled differently and shouldn't be conflated with the SS model's results. Looking at the metrics more carefully, the "tg_gar_ours_mid" label in the SS evaluation file is probably referring to the TG model itself rather than SS in TF mode. So I need to find where the actual SS model's TF values are stored—they're likely coming from a different evaluation file like eval_v8b_ss.

When I pull those values—s42 at 0.4983, s123 at 0.503, and s456 at 0.4964—the mean comes to roughly 0.499, which rounds down to 0.498 and matches the paper's reported value. The standard deviation of 0.0034 is close enough to the reported 0.004 that the small difference could come from different rounding or slightly different source data, so this isn't a major concern.

Now I'm checking whether the IID values in Table 1 are consistent with what's in the registry. The table shows TG, PCGrad, UG, and LO all with GAR-O at 0.50 and PPL at 2.78, but when I look at the phase2_4way_eval registry for the IID condition, I'm seeing different numbers—TG's GAR is 0.4866 and PPL is 2.63, UG's GAR is 0.4923 and PPL is 2.62. There's a discrepancy here that I need to investigate further. I'm noticing that PCGrad's IID and held-out PPL values are both 2.78, which is unusual, while TG shows different values between the two evaluation sets (2.63 vs 2.78). Let me verify whether all models were re-evaluated or if there's an inconsistency in how the results were recorded. give different PPLs for TG.

I think the issue might be that phase2_4way_eval is an older experiment using a different eval protocol, and the final table uses a newer eval protocol. The phase2_tg_s42_v9_pcgrad results show that when using the final protocol, IID PPL = 2.78. Maybe the other models were also re-evaluated with this protocol, but the results aren't in a separate registry entry.

In any case, I'll note the discrepancy between the registry and the table for IID values (PPL 2.63 vs 2.78 for TG/UG/LO) and flag that the IID GAR values for TG and LO round to 0.49, not 0.50 as shown in the table (based on phase2_4way_eval data).

But if the table is pulling from a different data source than phase2_4way_eval, these might not actually be errors — the table could be correct based on updated evaluations, so I should flag this as something needing verification rather than a definite issue.

Now I'm noticing something odd in the PCGrad results: the IID and held-out metrics are completely identical, which seems suspicious. I need to check whether the eval script might have accidentally used the same data for both protocols.

Let me organize all these findings into a comprehensive audit report. Now I'm verifying the remaining AR model results—the base model shows 0.019 with confidence intervals, and I'm checking that the task-guided, PCGrad, UG, and LO variants all match their expected values of 0.064, 0.030, 0.033, and 0.037 respectively.

The gate statistics are also checking out: task-guided at 0.93±0.05, UG at 0.96±0.05, and LO at 1.00, all matching the registry values. Everything's verified except for that lingering IID PPL and GAR discrepancy I need to address in the report, so I'm going to write this up now and make sure I'm clear about what I'm confident in versus what still needs investigation.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d3475b86-2166-4680-a5bd-cfee6b3a97ae",
  "isSidechain": false,
  "requestId": "req_011CbPwowDiEsGKCv44vK6sL",
  "type": "assistant",
  "uuid": "ccc39679-efcf-49e6-b152-baa7aa950399",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "4b680861-4da7-411a-8744-3dabfdaf2205",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015MURkebmR2ooHGzDLkCC9Q",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 27718,
      "cache_read_input_tokens": 77579,
      "output_tokens": 13476,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 27718,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 13476,
          "cache_read_input_tokens": 77579,
          "cache_creation_input_tokens": 27718,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 27718
          },
          "type": "message"
        }
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

_source line 103 · 2026-05-25T20:50:31.311Z_

Now I have all data needed. Let me write the comprehensive audit report.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ccc39679-efcf-49e6-b152-baa7aa950399",
  "isSidechain": false,
  "requestId": "req_011CbPwowDiEsGKCv44vK6sL",
  "type": "assistant",
  "uuid": "7a0eb24b-f89d-4435-b3ae-45f31bfbc51d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "4b680861-4da7-411a-8744-3dabfdaf2205",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015MURkebmR2ooHGzDLkCC9Q",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 27718,
      "cache_read_input_tokens": 77579,
      "output_tokens": 13476,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 27718,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 13476,
          "cache_read_input_tokens": 77579,
          "cache_creation_input_tokens": 27718,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 27718
          },
          "type": "message"
        }
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

_source line 104 · 2026-05-25T20:53:57.052Z_

<details open><summary>🔧 Tool call — Write · `toolu_01Gzpc3wfNWfkgiZen7GkTEb`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/audit_body_text.md",
  "content": "# 正文数据审计报告\n\n## 统计\n- 总定量声明数：~160\n- 已验证（与 Registry 一致）：~135\n- 问题数：6（含 2 个 major、4 个 minor）\n- 暂无出处/需独立验证：~19\n\n---\n\n## 逐章节审计\n\n### Abstract\n\n| 数字/声明 | Registry 来源 | 状态 | 备注 |\n|-----------|-------------|------|------|\n| \"order of magnitude\" TF-AR gap | d048_final_ar_eval: 8–17× | ✓ | 8–17× ≈ 1 order of magnitude |\n| \"collapses by an order of magnitude\" | 同上 | ✓ | |\n| \"near parity on Qwen\" (SS) | d048_final_ar_eval + d048_eval_ss_s123/s456: gap 1.24× | ⚠️ minor | 1.24× 称为 \"near parity\" 可接受 |\n| \"no perplexity cost\" (SS) | d048_final_ar_eval: TG PPL 1.432, SS PPL 1.442 (Δ=0.7%) | ✓ | |\n| Two architectures (Qwen-2.5-7B, Llama-3.1-8B) | 多个 Llama 实验确认 | ✓ | |\n\n### Introduction\n\n| 数字/声明 | Registry 来源 | 状态 | 备注 |\n|-----------|-------------|------|------|\n| \"goal attention drops by over 70% within just five turns\" | phase1_gar_diag: relative_drop=0.708=70.8% | ✓ | |\n| AUC = 0.98 | N/A | 文献引用 | 来自 Dongre et al. (2026) |\n| Fig 1 caption: \"85–90% decay\" | phase1_gar_diag: turn1→turn10 = 84.7%; analysis_attention_heatmap: base=87.5% | ⚠️ minor | 对 base 模型大致正确 (85–87.5%), 但 fine-tuned 仅 77–81%。Caption 表述暗示所有变体均 85–90%，实际仅 base 接近 |\n| Fig 1 caption: \"8–17×\" | d048_final_ar_eval: 7.81–16.7× | ✓ | 7.81→8 (rounded up), 16.7→17 |\n| Fig 1 caption: \"7.8× to 1.3× (Qwen)\" | d048_final_ar_eval + SS multi-seed | ⚠️ minor | 7.8× ✓; ~1.3× 实际为 1.24×（多种子均值），s42 单独 1.29× |\n| Fig 1 caption: \"~27× to 2.9× (Llama)\" | eval_llama_ar_n20 + p1_llama_ss_eval | ✓ | 27.0× ✓; 2.87× ≈ 2.9× ✓ |\n| Contribution 2: \"p = 0.002, effect reverses\" | 无 registry entry | ❓ | p=0.002 在正文出现但 registry 无此统计检验记录 |\n| Contribution 4: \"~1.3× on Qwen and ~2.9× on Llama\" | 同上 | ⚠️ | 同 Fig 1 caption 一致性 OK，但 ~1.3× 偏高 |\n\n### Method\n\n| 数字/声明 | Registry 来源 | 状态 | 备注 |\n|-----------|-------------|------|------|\n| GAR-Dongre ~0.01–0.02 in multi-turn | phase2_4way_eval_heldout: 0.0124–0.0152 | ✓ | |\n| GAR-ours range 0.019–0.50 | d048_final_ar_eval (AR Base=0.019) + table (TF=0.50) | ✓ | |\n| r = 0.200, p = 0.007 (GAR–compliance) | instruction_retention_test | ✓ | Registry: r=0.2003, p=0.007 |\n| ~57K parameters | 架构设计值 | ✓ | 28 layers × (32×64 + 64 + 64×1 + 1) ≈ 57K |\n| <0.001% of 7B | 57K/7B = 0.00081% < 0.001% | ✓ | |\n| σ(1.5) ≈ 0.82 | 数学计算 | ✓ | sigmoid(1.5)=0.8176≈0.82 |\n| proj reduces to 16; emb 16-dim | 架构设计值 | — | 设计选择，无需验证 |\n| 32-dim input → 64-unit hidden → scalar | 架构设计值 | — | 32=16+16 ✓ |\n| σ_min = 0.05; λ_GAR = λ_div = 1.0 | 超参设计值 | — | |\n| 10× learning rate multiplier | 超参设计值 | — | |\n| UG: L3=0.777, L27=1.000 | phase2_ug_s42 notes | ✓ | |\n| Seven iterations, four loss families | 项目历史 | — | v1–v7 训练记录 |\n\n### Experiments\n\n| 数字/声明 | Registry 来源 | 状态 | 备注 |\n|-----------|-------------|------|------|\n| lr = 2×10⁻⁴ | phase2_tg_s42_v8_schedsampling spec | ✓ | |\n| batch size 1, grad accum 8 | 同上 | ✓ | |\n| seed 42; TG additionally seed 123 | v7_tg_s123 存在 | ✓ | |\n| 8K conversations from UltraChat | tab_dataset_stats: Training set=8,000 | ✓ | |\n| 3 epochs | phase2_tg_s42_v7: 3 epoch | ✓ | |\n| ~6 hours | phase2_tg_s42_v7: 21352s=5.9h≈6h | ✓ | |\n| RTX PRO 6000 Blackwell, 96 GB | llama_tg_s42: GPU 名称匹配; 96GB 为官方规格 | ✓ | Registry 显示实测 102GB，96GB 为标称值 |\n| **Table 1 IID TF GAR-ours: TG=0.50** | phase2_4way_eval: TG=0.4866 → 应为 0.49 | ⚠️ major | Registry IID 值 0.4866 四舍五入应为 0.49 而非 0.50。Table 同时显示 IID PPL=2.78，但 registry IID PPL=2.63（held-out 为 2.78）。疑似 IID 列使用了 held-out 数据或已更新 eval 协议 |\n| Table 1 IID TF: UG=0.49 | phase2_4way_eval: UG=0.4923 → 0.49 | ✓ | |\n| Table 1 IID TF: LO=0.50 | phase2_4way_eval: LO=0.4860 → 应为 0.49 | ⚠️ major | 同 TG 问题，0.486 应舍入为 0.49 |\n| Table 1 IID TF: PCGrad=0.50 | phase2_tg_s42_v9_pcgrad: 0.5002 → 0.50 | ✓ | |\n| Table 1 IID PPL: 所有 fine-tuned = 2.78 | phase2_4way_eval: TG/UG/LO PPL=2.62–2.63 | ⚠️ major | Registry IID PPL 为 2.62–2.63，非 2.78。PCGrad IID PPL=2.78 ✓。TG/UG/LO 的 IID PPL 与 held-out PPL 不匹配 |\n| Table 1 Held-out TF: 全部值 | phase2_4way_eval_heldout | ✓ | 所有值匹配 |\n| Table 1 AR: 全部值 | d048_final_ar_eval | ✓ | Base=0.019, TG=0.064, UG=0.033, LO=0.037, PC=0.030 全部匹配 |\n| Table 1 CI: [.041,.091] 等 | d048_final_ar_eval (bootstrap) | ✓ | |\n| Table 1 gate stats: TG .93±.05, UG .96±.05 | phase2_tg_s42_v7, phase2_ug_s42 | ✓ | TG 0.9336→.93, std 0.0492→.05 ✓ |\n| \"GAR-ours spans 0.49–0.51 (≤2 pp)\" | 表中值 | ✓ | |\n| \"PPL is 2.78 for all\" | Table 1 | ✓ | 表中确实全为 2.78（但 IID 数据来源有疑问，见上） |\n| **\"held-out GAR-ours differs by ≤1 pp\"** | phase2_4way_eval vs _heldout | ⚠️ major | TG: IID 0.4866 vs held-out 0.5035 = 1.7pp; UG: 0.4923 vs 0.5053 = 1.3pp。应为 \"≤2 pp\" |\n| \"GAR-Dongre remains low (0.01–0.02)\" | Table 1 | ✓ | |\n| \"no TF-AR gap\" for GAR-Dongre | Table 1 + analysis | ✓ | |\n| \"8–17× gap\" | d048_final_ar_eval | ✓ | 7.81–16.7× 取整 |\n| \"ThreadGate 0.064 > LoRA-only 0.037 > ...\" | d048_final_ar_eval | ✓ | 排序一致 |\n| \"TG vs LO significant (p=0.004)\" | 无 registry entry | ❓ | p=0.004 无法从 registry 追溯 |\n| \"gap remains 7.8×\" | 0.50/0.064=7.81 | ✓ | |\n| \"A second seed confirms TF stability (0.504±0.001)\" | eval_v7_tg_s123: TF=0.5052; phase2_4way_eval_heldout: TG TF=0.5035 | ✓ | mean(0.5035, 0.5052)=0.504, half-range=0.0009≈0.001 |\n| \"MMLU 5-shot accuracy remains within 0.8 pp\" | mmlu_eval_all: max delta=0.77pp (Base 74.23% – UG 73.46%) | ✓ | |\n| **§4.3: \"β=3 triggers phase transition to GAR=0.556 (9% PPL cost)\"** | attention_steering_gen_n50: β=3 GAR=0.5558→0.556 ✓; PPL cost (1.5605-1.4324)/1.4324=8.9%≈9% | ✓ | |\n| \"β=5, GAR reaches 0.727±0.061 (PPL 1.77)\" | attention_steering_gen_n50: β=5 GAR=0.7271, std=0.0605; PPL=1.7723 | ✓ | |\n| \"+11.1 pp late-turn compliance\" | instruction_retention_test: delta=0.111=11.1pp | ✓ | |\n| \"p=0.077\" (McNemar) | instruction_retention_test: mcnemar_p=0.0771→0.077 | ✓ | |\n| \"+23.8 pp content-constrained\" | instruction_retention_test: content_constraint delta=0.238=23.8pp | ✓ | |\n| **§4.4: \"AR GAR-ours rises to 0.401±0.047\"** | SS multi-seed: mean=0.4009≈0.401, std=0.0469≈0.047 | ✓ | s42=0.347, s123=0.4231, s456=0.4325 |\n| **\"gap from 7.8× to ~1.3×\"** | gap=0.4992/0.4009=1.245 | ⚠️ minor | 多种子均值 gap 为 1.24×；s42 单独 1.29×。~1.3× 偏高但 ~ 给出余量 |\n| \"TF GAR 0.498±0.004\" | SS TF multi-seed: 0.4983, 0.503, 0.4964 → mean=0.4992, std=0.0034 | ⚠️ minor | mean 应为 0.499 而非 0.498; std 应为 0.003 而非 0.004 |\n| \"PPL (1.441±0.001)\" | SS PPL multi-seed: 1.442, 1.4408, 1.4394 → mean=1.4407, std=0.0013 | ✓ | |\n| \"β=5: 0.717±0.001, std 0.047→0.001\" | SS β=5 multi-seed: mean=0.7167≈0.717, std=0.0009≈0.001; β=0 std=0.047 | ✓ | |\n| \"SS gap from ~27× to 2.9× (Llama)\" | p1_llama_ss_eval: TF 0.477, AR 0.166, gap=2.87≈2.9× | ✓ | |\n| \"fewer training epochs (2 vs 3)\" | p1_llama_ss_training spec: epochs=3 但 conclusion=success | ⚠️ minor | Registry spec 写 epochs=3 但实际可能只训练 2 epoch（早停或 epoch 计数差异）。需确认实际 epoch 数 |\n\n### Analysis\n\n| 数字/声明 | Registry 来源 | 状态 | 备注 |\n|-----------|-------------|------|------|\n| Fig 4 caption: \"77–81% decay\" | analysis_attention_heatmap: TG=77.7%, UG=80.3%, LO=81.0% | ✓ | |\n| \"Δ=3.3 pp between TG and LO\" | 81.0–77.7=3.3pp | ✓ | |\n| \"Base decays 87.5%\" | analysis_attention_heatmap: base_decay=0.875 | ✓ | |\n| §5.1: \"27/28 layers gate values lower at turn 1\" | 无直接 registry entry | ❓ | 来自 gate 分析脚本，非 registry 指标 |\n| \"Wilcoxon p = 3.73×10⁻⁸, r = 0.975\" | 无直接 registry entry | ❓ | 同上 |\n| \"layer 23 shifts from 0.769 to 0.979\" | 无直接 registry entry | ❓ | gate turn conditioning 分析结果 |\n| \"inference-time values of 0.93–0.98 (2–7% attenuation)\" | phase2_tg_s42_v7: gate mean=0.93; 1-0.93=7%, 1-0.98=2% | ✓ | |\n| \"L3=0.777, L27=1.000\" (UG) | phase2_ug_s42 notes | ✓ | |\n| §5.2: \"68–79% of layers\" (gradient conflict) | analysis_gradient_conflict: epoch0=78.6%, epoch2=67.9% | ✓ | 67.9–78.6% ≈ 68–79% |\n| \"cosine similarity −0.089→−0.042\" | analysis_gradient_conflict: epoch0=-0.089, epoch2=-0.042 | ✓ | |\n| \"NTP magnitude 7.5× to 14.7×\" | analysis_gradient_conflict: epoch0=7.5, epoch2=14.7 | ✓ | |\n| \"AR GAR worsens: 0.064→0.030\" | d048_final_ar_eval: TG=0.064, PCGrad=0.030 | ✓ | |\n| \"(p=0.002)\" (TG vs PCGrad) | 无 registry entry | ❓ | 见 Intro 同一 p 值 |\n| \"cos sim oscillates around zero\" (PCGrad) | phase2_tg_s42_v9_pcgrad notes: cos_sim -0.061→+0.055→-0.035 | ✓ | |\n| \"Llama near-orthogonal (cos=+0.005)\" | p2_llama_gradient_conflict: cos_sim_mean=0.0045→0.005 | ✓ | |\n| \"25.7× NTP magnitude dominance\" (Llama) | p2_llama_gradient_conflict: mag_ratio_median=25.7 | ✓ | |\n| §5.3: \"77–87% per-turn decay\" | analysis_attention_heatmap: 77.7–87.5% | ✓ | |\n| §5.4: TRC 0.334/0.332 (TG, gap +0.002) | trc_baseline_v7_tg: tf=0.3339, gen=0.3323, gap=0.0016 | ✓ | 0.334/0.332/+0.002 rounded ✓ |\n| TRC 0.349/0.411 (LO, gap −0.062) | trc_baseline_v7_tg: tf=0.349, gen=0.4106, gap=-0.0617 | ✓ | |\n| \"GAR-Dongre: Llama 1.002×, Qwen 1.28×\" | llama_ar_matched_eval: dongre gap=1.002× ✓; Qwen 1.28× 来源不明 | ⚠️ | Qwen 1.28× 无明确 registry 来源 |\n| §5.5: \"TF GAR-ours 0.484 (TG) / 0.481 (LO)\" on Llama | llama_eval_s42: 0.4836→0.484 ✓; eval_llama_lora_only_s42: 0.4807→0.481 ✓ | ✓ | |\n| \"medians: 0.018 (TG and LO), 0.009 (Base)\" | eval_llama_ar_n20: TG=0.0179→0.018 ✓, LO=0.0184→0.018 ✓, Base=0.0093→0.009 ✓ | ✓ | |\n| \"gaps of 27× and 26×\" | 0.484/0.018=26.9≈27×; 0.481/0.018=26.7≈27× or 26× | ✓ | |\n| \"CoV > 100%\" | eval_llama_ar_n20: TG std=0.1002, mean=0.0434, CoV=231% | ✓ | |\n| \"Llama SS: gap from ~27× to 2.9×\" | p1_llama_ss_eval: tf_ar_gap=2.87≈2.9× | ✓ | |\n| \"TF GAR 0.477, AR GAR 0.166\" (Llama SS) | p1_llama_ss_eval: ss_tf_gar=0.477 ✓, ss_ar_b0_gar=0.1662→0.166 ✓ | ✓ | |\n| \"β=3: Qwen SS 0.593, Llama SS 0.173\" | d048_final_ar_eval: Qwen β3 ss=0.593 ✓; Llama SS β=3 | ❓ | Llama SS β=3 (0.173) 无 registry 来源 |\n| \"Llama β=5: 0.791\" | p1_llama_ss_eval: ss_ar_b5_gar=0.7905→0.791 | ✓ | |\n| \"exceeding Qwen SS 0.717\" | d048_final_ar_eval: beta5.ss_gar=0.717 | ✓ | |\n| \"Qwen attenuates early layers (L1=0.793)\" | v7_tg_s123 gate profile: L1=0.793 | ✓ | 来自 s123 非主 seed (s42)。s42 最低层为 L3/L4 |\n| \"Llama dips at late layers (L25=0.719)\" | llama_tg_s42 gate profile: L25=0.719 | ✓ | |\n| \"79.8% GAR decay\" (1.5B) | tab_qwen15b_results: (0.0336-0.0068)/0.0336=79.8% | ✓ | |\n| \"β-steering recovery to 0.715\" (1.5B) | tab_qwen15b_results: AR β=5 TG=0.7150→0.715 | ✓ | |\n\n### Discussion\n\n| 数字/声明 | Registry 来源 | 状态 | 备注 |\n|-----------|-------------|------|------|\n| \"≤1.3×\" (GAR-Dongre shift) | analysis.tex 引用 Qwen 1.28× | ✓ | 1.28× ≤ 1.3× |\n| \"r=0.743\" (per-head TF GAR vs AR shift) | 无直接 registry entry | ❓ | p1_tf_ar_kl_divergence gate_kl_correlation=0.11 不匹配；可能来自不同分析 |\n| \"r=0.200\" (GAR–compliance) | instruction_retention_test: 0.2003 | ✓ | |\n| \"7.5–25.7× NTP dominance\" | analysis_gradient_conflict + p2_llama_gradient_conflict | ✓ | Qwen 7.5–14.7×, Llama 25.7× |\n| \"At β=5: SS=0.717 vs TG=0.727\" | d048_final_ar_eval: beta5.ss_gar=0.717, beta5.tg_gar=0.727 | ✓ | |\n\n### Conclusion\n\n| 数字/声明 | Registry 来源 | 状态 | 备注 |\n|-----------|-------------|------|------|\n| \"GAR=0.50\" (TF) | 多处验证 | ✓ | |\n| \"order of magnitude\" collapse | 同 Abstract | ✓ | |\n| \"~1.3× (Qwen)\" | 同 §4.4 | ⚠️ | 同上：实际 1.24× |\n| \"~2.9× (Llama)\" | p1_llama_ss_eval: 2.87× | ✓ | |\n| \"two architectures\" | 实验确认 | ✓ | |\n\n### Related Work\n\n| 数字/声明 | Registry 来源 | 状态 | 备注 |\n|-----------|-------------|------|------|\n| \"27–48% across 12 models\" (Dongre) | N/A | 文献引用 | |\n| \"70.8% decline on Qwen-2.5-7B\" | phase1_gar_diag: relative_drop=0.708=70.8% | ✓ | |\n| \"MMLU +2.03 at 15B\" (Gated Attention) | N/A | 文献引用 | |\n\n### Limitations\n\n| 数字/声明 | Registry 来源 | 状态 | 备注 |\n|-----------|-------------|------|------|\n| \"8K conversations\" | tab_dataset_stats | ✓ | |\n| \"three seeds\" (SS) | d048_ss_s42/s123/s456 | ✓ | |\n| \"τ=0.5\" | method 定义 | ✓ | |\n\n---\n\n## 跨章节一致性检查\n\n| 关键数字 | Abstract | Intro | Method | Experiments | Analysis | Discussion | Conclusion | 一致? |\n|----------|----------|-------|--------|-------------|----------|------------|------------|------|\n| TF GAR ≈ 0.50 | ✓ (implicit) | — | τ=0.5 | Table: 0.49–0.51 | — | — | 0.50 | ✓ |\n| AR collapse ~order of magnitude | ✓ | ✓ (8–17×) | — | 8–17× | — | ✓ | ✓ | ✓ |\n| Gap ratio 7.8× (TG) | — | 7.8× (fig caption) | — | 7.8× | — | — | — | ✓ |\n| ~1.3× SS gap (Qwen) | \"near parity\" | ~1.3× | — | ~1.3× | ~1.3× | — | ~1.3× | ✓ (但实际 1.24×) |\n| ~2.9× SS gap (Llama) | — | — | — | 2.9× | 2.9× | — | ~2.9× | ✓ |\n| p=0.002 (PCGrad) | — | 0.002 | — | — | 0.002 | — | — | ✓ |\n| 0.064 (TG AR GAR) | — | — | — | 0.064 | 0.064 | — | — | ✓ |\n| 0.727 (TG β=5) | — | — | — | 0.727 | — | 0.727 | — | ✓ |\n| 0.717 (SS β=5) | — | — | — | 0.717 | — | 0.717 | — | ✓ |\n| 70%/70.8% GAR decline | — | \"over 70%\" | — | — | — | — | — | ✓ vs Related Work 70.8% |\n| r=0.200 (GAR–compliance) | — | — | 0.200 | — | — | 0.200 | — | ✓ |\n\n**所有跨章节出现的数字内部一致。**\n\n---\n\n## 问题清单\n\n### ISSUE-1 [MAJOR]: Table 1 IID 列数据疑似使用 held-out 协议\n- **位置**: related_work.tex Table 1, IID (TF) 列\n- **问题**: Table 1 显示 IID TF 值 TG=0.50, LO=0.50, PPL=2.78。但 Registry phase2_4way_eval（标记为 IID eval）记录 TG GAR=0.4866（应为 0.49）、LO GAR=0.4860（应为 0.49）、PPL=2.63（非 2.78）。Held-out eval (phase2_4way_eval_heldout) 给出 TG=0.5035→0.50, PPL=2.78，与表中 IID 值匹配。\n- **可能原因**: (a) IID eval 已用新协议重跑但 registry 未更新；(b) Table 错误使用了 held-out 数据。注意 Base IID PPL=4.23 与 registry 匹配，仅 fine-tuned 模型有差异。PCGrad IID 值 (0.5002, 2.78) 来自独立实验且匹配。\n- **建议**: 确认 Table IID 列的实际数据来源。若确系 held-out 数据，需修正为真实 IID 值（GAR ~0.49, PPL ~2.63）或删除 IID 列。\n\n### ISSUE-2 [MAJOR]: \"≤1 pp\" 声明与实际数据不符\n- **位置**: experiments.tex §4.2, \"held-out GAR-ours differs by ≤1 pp\"\n- **问题**: 各变体 IID→held-out 差异: TG 1.7pp, UG 1.3pp, LO 1.2pp, PCGrad 0pp。最大 1.7pp，超过 \"≤1 pp\"。若改为 held-out 内部 spread (0.498–0.505=0.75pp)，则 ≤1pp 成立，但句意不支持此解读。\n- **建议**: 改为 \"≤2 pp\" 或明确为 held-out 内部 spread。\n\n### ISSUE-3 [minor]: ~1.3× SS gap 偏高\n- **位置**: Intro (fig caption), Experiments §4.4, Analysis §5.5, Conclusion\n- **问题**: 多种子均值 gap = 0.499/0.401 = 1.245 ≈ 1.2×。s42 单独 = 1.29×。\"~1.3×\" 偏高于多种子均值。\n- **建议**: 改为 \"~1.2×\" 或保留 \"~1.3×\" 但说明基于 s42 单种子。\n\n### ISSUE-4 [minor]: TF GAR 0.498±0.004 精度偏差\n- **位置**: experiments.tex §4.4\n- **问题**: SS TF 三种子均值 0.4992≈0.499（非 0.498），std=0.0034≈0.003（非 0.004）。差异很小但精度上不匹配。\n- **建议**: 修正为 \"0.499±0.003\"。\n\n### ISSUE-5 [minor]: Fig 1(a) caption \"85–90%\" 涵盖范围模糊\n- **位置**: introduction.tex Fig 1 caption\n- **问题**: \"85–90% decay across turns\" 对 base 模型大致正确 (Qwen 84.7–87.5%)，但 fine-tuned 模型仅 77–81%（Fig 4 caption 已正确标注）。Caption 未区分 base vs fine-tuned。\n- **建议**: 改为 \"77–87% across turns\" 或明确标注为 base model decay。\n\n### ISSUE-6 [minor]: Llama SS training \"2 vs 3\" epoch 需确认\n- **位置**: experiments.tex §4.4, analysis.tex §5.5\n- **问题**: 论文称 Llama SS \"fewer training epochs (2 vs 3)\"，但 p1_llama_ss_training spec 显示 epochs=3。实际训练可能因早停只完成 2 epoch，但 registry 记录不一致。\n- **建议**: 确认 Llama SS 实际训练 epoch 数并与 spec 对齐。\n\n---\n\n## 暂无出处的数字\n\n| 数字 | 位置 | 原因 |\n|------|------|------|\n| p=0.002 (TG vs PCGrad) | Intro, Analysis §5.2 | 无 registry entry, 来自统计检验脚本 |\n| p=0.004 (TG vs LO) | Experiments §4.2 | 无 registry entry |\n| r=0.743 (per-head correlation) | Discussion | registry p1_tf_ar_kl_divergence 中 gate_kl_correlation=0.11 不匹配 |\n| 27/28 layers gate inversion | Analysis §5.1 | 来自 gate 分析脚本, 非 registry |\n| Wilcoxon p=3.73×10⁻⁸, r=0.975 | Analysis §5.1 | 同上 |\n| Layer 23: 0.769→0.979 | Analysis §5.1 | 同上 |\n| Llama SS β=3 GAR=0.173 | Analysis §5.5 | p1_llama_ss_eval 仅有 β=0 和 β=5 |\n| Qwen GAR-Dongre TF/AR ratio 1.28× | Analysis §5.4 | 无直接 registry 来源 |\n| \"mean 3.6 user turns\" (AR eval) | Table 1 caption | 来自 eval 数据统计 |\n| 95% CI 值 (Table 1) | Table 1 | 来自 bootstrap, 仅最终 CI 边界在表中 |\n| AUC=0.98 | Intro | 文献引用 (Dongre et al. 2026) |\n| \"27–48% across 12 models\" | Related Work | 文献引用 (Dongre et al. 2026) |\n| \"MMLU +2.03 at 15B\" | Related Work | 文献引用 (Qiu et al. 2025) |\n| Pilot gaps \"20–34×\" | Fig 3 caption | 来自 N=5 pilot eval, 非 registry |\n| \"0-350 step plateau\" (PCGrad) | 隐含于 notes | 训练日志 |\n| per-β turn-level trajectories | §4.3 reference | 附录中的可视化 |\n| \"mid-turn GAR above 0.36\" (SS robustness) | §4.4 | 可能来自 tab_gar_robustness |\n| β=0 AR baseline PPL 1.432 | §4.3 context | d048_final_ar_eval ppl.tg=1.432 ✓ (可追溯) |\n| \"NTP magnitude dominance 10-40×\" (PCGrad) | Analysis §5.2 notes | phase2_tg_s42_v9_pcgrad notes: NTP mag_ratio 2.8→28.8 |\n\n**注**: 多数\"暂无出处\"的数字来自分析脚本的直接输出（gate 分析、统计检验），未作为独立 registry 实验记录。这些数字可通过重跑对应脚本验证，但当前无法仅从 registry 追溯。p 值 (0.002, 0.004) 和相关系数 (r=0.743) 建议在 registry 中补充 `tab_statistical_tests` 条目以提高可追溯性。\n\n---\n\n## MMLU 详细验证 (tab_mmlu_detail.tex)\n\n| 指标 | 表中值 | Registry (mmlu_eval_all) | 匹配? |\n|------|--------|-------------------------|------|\n| Base Overall | 74.23% | 0.7423 | ✓ |\n| TG Overall | 73.47% | 0.7347 | ✓ |\n| PCGrad Overall | 73.86% | 0.7386 | ✓ |\n| SS Overall | 73.75% | 0.7375 | ✓ |\n| LoRA-only Overall | 73.57% | 0.7357 | ✓ |\n| UG Overall | 73.46% | 0.7346 | ✓ |\n| Max Δ | −0.77pp | 74.23−73.46=0.77 | ✓ |\n| \"within 0.8 pp\" claim | 0.77≤0.8 | | ✓ |\n\n## Qwen-1.5B 验证 (tab_qwen15b_results.tex)\n\n| 指标 | 表中值 | 验算 | 匹配? |\n|------|--------|------|------|\n| Turn-1 GAR | 0.0336 | — | ✓ (来自 qwen15b_phase1_diag) |\n| Mid-turn GAR | 0.0068 | — | ✓ |\n| Relative drop | 79.8% | (0.0336-0.0068)/0.0336=79.76%≈79.8% | ✓ |\n| AR β=0 Base | 0.0167±0.005 | — | 来自 eval 脚本 |\n| AR β=0 TG | 0.0233±0.006, p=0.005 | — | 来自 eval 脚本 |\n| AR β=5 TG | 0.7150±0.017, p<0.001 | — | 来自 eval 脚本 |\n\n## GAR Robustness 验证 (tab_gar_robustness.tex)\n\n表中数据来自 GAR robustness 分析脚本，部分可与 p1_tf_ar_kl_divergence 交叉验证：\n- SS mid-turn GAR 对所有 token selection 策略 >0.36 ✓ (Last: 0.4582, All: 0.3658, First: 0.4118, Goal-only: 0.4435)\n- 论文 §4.4 \"mid-turn GAR above 0.36 for all token-position variants\" 与表一致 ✓\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7a0eb24b-f89d-4435-b3ae-45f31bfbc51d",
  "isSidechain": false,
  "requestId": "req_011CbPwowDiEsGKCv44vK6sL",
  "type": "assistant",
  "uuid": "36f1f798-cf07-4654-a5da-33a1392dfdad",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "4b680861-4da7-411a-8744-3dabfdaf2205",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015MURkebmR2ooHGzDLkCC9Q",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 27718,
      "cache_read_input_tokens": 77579,
      "output_tokens": 13476,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 27718,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 13476,
          "cache_read_input_tokens": 77579,
          "cache_creation_input_tokens": 27718,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 27718
          },
          "type": "message"
        }
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

_source line 105 · 2026-05-25T20:53:57.060Z_

<details><summary>↩ Tool result · reported error · `toolu_01Gzpc3wfNWfkgiZen7GkTEb`</summary>

```text
&lt;tool_use_error>File has not been read yet. Read it first before writing to it.&lt;/tool_use_error>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "36f1f798-cf07-4654-a5da-33a1392dfdad",
  "isSidechain": false,
  "promptId": "8817af8a-f189-44e8-a462-1453a12b4ea3",
  "type": "user",
  "uuid": "ea440173-64ca-4def-974b-ee848cd440c6",
  "toolUseResult": "Error: File has not been read yet. Read it first before writing to it.",
  "sourceToolAssistantUUID": "36f1f798-cf07-4654-a5da-33a1392dfdad",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "4b680861-4da7-411a-8744-3dabfdaf2205",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Runtime record

_source line 106_

```json
{
  "type": "last-prompt",
  "leafUuid": "ea440173-64ca-4def-974b-ee848cd440c6",
  "sessionId": "4b680861-4da7-411a-8744-3dabfdaf2205"
}
```

---

### Runtime record

_source line 107_

```json
{
  "type": "ai-title",
  "aiTitle": "Audit quantitative claims in paper body text",
  "sessionId": "4b680861-4da7-411a-8744-3dabfdaf2205"
}
```

---

### Tool call

_source line 108 · 2026-05-25T20:54:01.664Z_

<details open><summary>🔧 Tool call — Bash · `toolu_016yD1yg5QErxVCGTP7TdxHA`</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/audit_body_text.md 2>/dev/null; echo \"---\"; ls /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/ | head -20",
  "description": "Check if audit file exists"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ea440173-64ca-4def-974b-ee848cd440c6",
  "isSidechain": false,
  "requestId": "req_011CbPxA4R7MSGJJfpzGMsQW",
  "type": "assistant",
  "uuid": "08e9bffa-e4be-4883-8128-ef23c879f7dd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "4b680861-4da7-411a-8744-3dabfdaf2205",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QG2tfxMiMS2NEDt1EjTBmb",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13516,
      "cache_read_input_tokens": 105297,
      "output_tokens": 160,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 13516,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 160,
          "cache_read_input_tokens": 105297,
          "cache_creation_input_tokens": 13516,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 13516
          },
          "type": "message"
        }
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

_source line 109 · 2026-05-25T20:54:01.736Z_

<details><summary>↩ Tool result · `toolu_016yD1yg5QErxVCGTP7TdxHA`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/audit_body_text.md
---
_project
analysis_attention_heatmap
anonymous_repo
appendix_expansion
attention_steering_results.json
attention_steering_v7_tg_gen
audit_appendix_tables.md
audit_body_text.md
cos_sim_trajectory
data_audit_report.md
dream_reports
eval_v8b_ss
fig1_overview_pb.pdf
fig1_overview_pb.png
fig1_overview_pb_v2.pdf
fig1_overview_pb_v2.png
fig1_overview_pb_v3.png
fig1_overview_pb_v4.pdf
fig1_overview_pb_v4.png
fig1_overview_v2.pdf
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "08e9bffa-e4be-4883-8128-ef23c879f7dd",
  "isSidechain": false,
  "promptId": "8817af8a-f189-44e8-a462-1453a12b4ea3",
  "type": "user",
  "uuid": "435454d3-ace3-4388-bfe0-cfcc4f23a0fb",
  "toolUseResult": {
    "stdout": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/audit_body_text.md\n---\n_project\nanalysis_attention_heatmap\nanonymous_repo\nappendix_expansion\nattention_steering_results.json\nattention_steering_v7_tg_gen\naudit_appendix_tables.md\naudit_body_text.md\ncos_sim_trajectory\ndata_audit_report.md\ndream_reports\neval_v8b_ss\nfig1_overview_pb.pdf\nfig1_overview_pb.png\nfig1_overview_pb_v2.pdf\nfig1_overview_pb_v2.png\nfig1_overview_pb_v3.png\nfig1_overview_pb_v4.pdf\nfig1_overview_pb_v4.png\nfig1_overview_v2.pdf",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "08e9bffa-e4be-4883-8128-ef23c879f7dd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "4b680861-4da7-411a-8744-3dabfdaf2205",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 110 · 2026-05-25T20:54:04.042Z_

<details open><summary>🔧 Tool call — Read · `toolu_01MZxKw49nnuPgxuWVL8TpDn`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/audit_body_text.md",
  "limit": 5
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "435454d3-ace3-4388-bfe0-cfcc4f23a0fb",
  "isSidechain": false,
  "requestId": "req_011CbPxAQRPRHrhhfX2kPNN3",
  "type": "assistant",
  "uuid": "1068773b-9e75-42a5-9517-f9dd76654023",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "4b680861-4da7-411a-8744-3dabfdaf2205",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JBmvvH9RLfTygFaK5hmnPG",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 383,
      "cache_read_input_tokens": 118813,
      "output_tokens": 108,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 383,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 108,
          "cache_read_input_tokens": 118813,
          "cache_creation_input_tokens": 383,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 383
          },
          "type": "message"
        }
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

_source line 111 · 2026-05-25T20:54:04.050Z_

<details><summary>↩ Tool result · `toolu_01MZxKw49nnuPgxuWVL8TpDn`</summary>

```text
1	# 主体文本数据审计报告
2	
3	**审计日期**: 2026-05-25
4	**审计范围**: abstract.tex, introduction.tex, method.tex, experiments.tex, analysis.tex, discussion.tex, conclusion.tex, limitations.tex
5	**数据源**: experiment registry (60 experiments), figure generation scripts (gen_fig*.py), appendix tables
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1068773b-9e75-42a5-9517-f9dd76654023",
  "isSidechain": false,
  "promptId": "8817af8a-f189-44e8-a462-1453a12b4ea3",
  "type": "user",
  "uuid": "832b70b1-a094-4b77-8b32-3f7742212148",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/audit_body_text.md",
      "content": "# 主体文本数据审计报告\n\n**审计日期**: 2026-05-25\n**审计范围**: abstract.tex, introduction.tex, method.tex, experiments.tex, analysis.tex, discussion.tex, conclusion.tex, limitations.tex\n**数据源**: experiment registry (60 experiments), figure generation scripts (gen_fig*.py), appendix tables",
      "numLines": 5,
      "startLine": 1,
      "totalLines": 343
    }
  },
  "sourceToolAssistantUUID": "1068773b-9e75-42a5-9517-f9dd76654023",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "4b680861-4da7-411a-8744-3dabfdaf2205",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Runtime record

_source line 112 · 2026-05-25T20:54:04.144Z_

```json
{
  "parentUuid": "832b70b1-a094-4b77-8b32-3f7742212148",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "d83ecaa3-19bd-4cee-84c0-45c2532d52f9",
  "timestamp": "2026-05-25T20:54:04.144Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "4b680861-4da7-411a-8744-3dabfdaf2205",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

---

### Assistant

_source line 113 · 2026-05-25T20:54:06.397Z_

The file already exists from a previous audit. Let me overwrite it with the comprehensive new audit.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d83ecaa3-19bd-4cee-84c0-45c2532d52f9",
  "isSidechain": false,
  "requestId": "req_011CbPxAahGZ1zhRQYeHeyJo",
  "type": "assistant",
  "uuid": "293e2cf4-7d09-4125-88b1-d610acbcd9e1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "4b680861-4da7-411a-8744-3dabfdaf2205",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0135MveS11edQ1aHVpGGVUJX",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 324,
      "cache_read_input_tokens": 119196,
      "output_tokens": 8579,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 324,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 8579,
          "cache_read_input_tokens": 119196,
          "cache_creation_input_tokens": 324,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 324
          },
          "type": "message"
        }
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

_source line 114 · 2026-05-25T20:56:54.846Z_

<details open><summary>🔧 Tool call — Write · `toolu_019ezhKRUYNWwCDUTXzeLV1v`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/audit_body_text.md",
  "content": "# 正文数据审计报告\n\n**审计日期**: 2026-05-25\n**审计范围**: abstract.tex, introduction.tex, method.tex, experiments.tex, analysis.tex, discussion.tex, conclusion.tex, limitations.tex, related_work.tex (含 Table 1)\n**数据源**: experiment registry (60 experiments), included tables (tab_*.tex)\n\n## 统计\n- 总定量声明数：~160\n- 已验证（与 Registry 一致）：~135\n- 问题数：6（含 2 个 major、4 个 minor）\n- 暂无出处/需独立验证：~19\n\n---\n\n## 逐章节审计\n\n### Abstract\n\n| 数字/声明 | Registry 来源 | 状态 | 备注 |\n|-----------|-------------|------|------|\n| \"order of magnitude\" TF-AR gap | d048_final_ar_eval: 8–17× | ✓ | 8–17× ≈ 1 order of magnitude |\n| \"collapses by an order of magnitude\" | 同上 | ✓ | |\n| \"near parity on Qwen\" (SS) | d048_final_ar_eval + d048_eval_ss_s123/s456: gap 1.24× | ⚠️ minor | 1.24× 称为 \"near parity\" 可接受 |\n| \"no perplexity cost\" (SS) | d048_final_ar_eval: TG PPL 1.432, SS PPL 1.442 (Δ=0.7%) | ✓ | |\n| Two architectures (Qwen-2.5-7B, Llama-3.1-8B) | 多个 Llama 实验确认 | ✓ | |\n\n### Introduction\n\n| 数字/声明 | Registry 来源 | 状态 | 备注 |\n|-----------|-------------|------|------|\n| \"goal attention drops by over 70% within just five turns\" | phase1_gar_diag: relative_drop=0.708=70.8% | ✓ | |\n| AUC = 0.98 | N/A | 文献引用 | 来自 Dongre et al. (2026) |\n| Fig 1 caption: \"85–90% decay\" | phase1_gar_diag: turn1→turn10 = 84.7%; analysis_attention_heatmap: base=87.5% | ⚠️ minor | 对 base 模型大致正确 (85–87.5%), 但 fine-tuned 仅 77–81%。Caption 未区分 |\n| Fig 1 caption: \"8–17×\" | d048_final_ar_eval: 7.81–16.7× | ✓ | 7.81→8, 16.7→17 |\n| Fig 1 caption: \"7.8× to 1.3× (Qwen)\" | d048_final_ar_eval + SS multi-seed | ⚠️ minor | 7.8× ✓; ~1.3× 实际为 1.24×（多种子均值） |\n| Fig 1 caption: \"~27× to 2.9× (Llama)\" | eval_llama_ar_n20 + p1_llama_ss_eval | ✓ | 27.0× ✓; 2.87× ≈ 2.9× ✓ |\n| Contribution 2: \"p = 0.002, effect reverses\" | 无 registry entry | ❓ | p=0.002 在正文引用但 registry 无统计检验记录 |\n| Contribution 4: \"~1.3× on Qwen and ~2.9× on Llama\" | 同上 | ⚠️ | ~1.3× 偏高，同 Fig 1 caption |\n\n### Method\n\n| 数字/声明 | Registry 来源 | 状态 | 备注 |\n|-----------|-------------|------|------|\n| GAR-Dongre ~0.01–0.02 in multi-turn | phase2_4way_eval_heldout: 0.0124–0.0152 | ✓ | |\n| GAR-ours range 0.019–0.50 | d048_final_ar_eval (AR Base=0.019) + table (TF=0.50) | ✓ | |\n| r = 0.200, p = 0.007 (GAR–compliance) | instruction_retention_test: r=0.2003, p=0.007 | ✓ | |\n| ~57K parameters | 架构设计值 | ✓ | 28 layers × ~2K params/layer ≈ 57K |\n| <0.001% of 7B | 57K/7B = 0.00081% < 0.001% | ✓ | |\n| σ(1.5) ≈ 0.82 | 数学计算 | ✓ | sigmoid(1.5)=0.8176≈0.82 |\n| proj to 16; emb 16-dim; 32→64→1 | 架构设计值 | — | 设计选择 |\n| σ_min = 0.05; λ_GAR = λ_div = 1.0 | 超参设计值 | — | |\n| 10× learning rate multiplier | 超参设计值 | — | |\n| UG: L3=0.777, L27=1.000 | phase2_ug_s42 notes | ✓ | |\n| Seven iterations, four loss families | 项目历史 (v1–v7) | — | |\n\n### Experiments\n\n| 数字/声明 | Registry 来源 | 状态 | 备注 |\n|-----------|-------------|------|------|\n| lr = 2×10⁻⁴, batch 1, accum 8, seed 42 | phase2_tg_s42_v8_schedsampling spec | ✓ | |\n| 8K conversations from UltraChat | tab_dataset_stats: Training=8,000 | ✓ | |\n| 3 epochs, ~6 hours | phase2_tg_s42_v7: 3 epoch, 21352s=5.9h | ✓ | |\n| RTX PRO 6000 Blackwell, 96 GB | llama_tg_s42 GPU; 96GB = nominal spec | ✓ | |\n| **Table 1 IID TG: GAR-O=0.50** | phase2_4way_eval: TG=0.4866 → 应为 0.49 | ⚠️ MAJOR | 见 ISSUE-1 |\n| Table 1 IID UG: GAR-O=0.49 | phase2_4way_eval: UG=0.4923 → 0.49 | ✓ | |\n| **Table 1 IID LO: GAR-O=0.50** | phase2_4way_eval: LO=0.4860 → 应为 0.49 | ⚠️ MAJOR | 见 ISSUE-1 |\n| Table 1 IID PCGrad: GAR-O=0.50 | phase2_tg_s42_v9_pcgrad: 0.5002 → 0.50 | ✓ | |\n| **Table 1 IID PPL: all fine-tuned = 2.78** | phase2_4way_eval: TG/UG/LO PPL=2.62–2.63 | ⚠️ MAJOR | 见 ISSUE-1 |\n| Table 1 Held-out: all values | phase2_4way_eval_heldout | ✓ | 全部匹配 |\n| Table 1 AR: all values | d048_final_ar_eval | ✓ | Base=0.019, TG=0.064, UG=0.033, LO=0.037, PC=0.030 |\n| Table 1 CI values | d048_final_ar_eval bootstrap | ✓ | |\n| Table 1 gate: TG .93±.05, UG .96±.05 | phase2_tg_s42_v7/phase2_ug_s42 | ✓ | |\n| \"GAR-ours spans 0.49–0.51 (≤2 pp)\" | Table 1 values | ✓ | |\n| \"PPL is 2.78 for all\" | Table 1 | ✓ | 表中如此，但 IID 数据来源存疑 |\n| **\"held-out GAR-ours differs by ≤1 pp\"** | 各变体 IID→held-out diff 最大 1.7pp | ⚠️ MAJOR | 见 ISSUE-2 |\n| \"GAR-Dongre remains low (0.01–0.02)\" | Table 1 | ✓ | |\n| \"8–17× gap\" | d048_final_ar_eval | ✓ | 7.81–16.7× → 8–17× |\n| \"TG 0.064 > LO 0.037 > UG 0.033 > PC 0.030 > Base 0.019\" | d048_final_ar_eval | ✓ | |\n| \"TG vs LO significant (p=0.004)\" | 无 registry entry | ❓ | 来自统计检验脚本 |\n| \"gap remains 7.8×\" | 0.50/0.064=7.81 | ✓ | |\n| \"second seed: 0.504±0.001\" | eval_v7_tg_s123: 0.5052; heldout s42: 0.5035 | ✓ | mean=0.504, ±0.001 |\n| \"MMLU within 0.8 pp\" | mmlu_eval_all: max Δ=0.77pp | ✓ | |\n| §4.3: \"β=3 → GAR=0.556 (9% PPL cost)\" | attention_steering_gen_n50: 0.5558, (1.56-1.43)/1.43=8.9% | ✓ | |\n| \"β=5: GAR 0.727±0.061 (PPL 1.77)\" | attention_steering_gen_n50: 0.7271±0.0605, PPL 1.7723 | ✓ | |\n| \"PPL below 1.8 in [3,5]\" | β=3: 1.56, β=5: 1.77 | ✓ | |\n| \"+11.1 pp late-turn compliance\" | instruction_retention_test: delta=0.111 | ✓ | |\n| \"p=0.077\" (McNemar) | instruction_retention_test: 0.0771 | ✓ | |\n| \"+23.8 pp content-constrained\" | instruction_retention_test: 0.238 | ✓ | |\n| §4.4: \"AR GAR 0.401±0.047\" (SS 3-seed) | mean(0.347,0.4231,0.4325)=0.4009, std=0.0469 | ✓ | |\n| **\"gap from 7.8× to ~1.3×\"** | 0.4992/0.4009=1.245 | ⚠️ minor | 见 ISSUE-3 |\n| **\"TF GAR 0.498±0.004\"** | mean(0.4983,0.503,0.4964)=0.4992, std=0.0034 | ⚠️ minor | 见 ISSUE-4 |\n| \"PPL 1.441±0.001\" | mean(1.442,1.4408,1.4394)=1.4407, std=0.0013 | ✓ | |\n| \"β=5: 0.717±0.001, std 0.047→0.001\" | mean(0.717,0.7174,0.7157)=0.7167, std=0.0009 | ✓ | |\n| \"Llama SS: ~27× to 2.9×\" | p1_llama_ss_eval: gap=2.87 | ✓ | |\n| \"fewer epochs (2 vs 3)\" | p1_llama_ss_training spec: epochs=3 | ⚠️ minor | 见 ISSUE-6 |\n\n### Analysis\n\n| 数字/声明 | Registry 来源 | 状态 | 备注 |\n|-----------|-------------|------|------|\n| Fig 4: \"77–81% decay\" | analysis_attention_heatmap: TG=77.7%, LO=81.0% | ✓ | |\n| \"Δ=3.3 pp TG vs LO\" | 81.0−77.7=3.3 | ✓ | |\n| \"Base decays 87.5%\" | analysis_attention_heatmap: 0.875 | ✓ | |\n| §5.1: \"27/28 layers\" gate inversion | 无 registry entry | ❓ | gate 分析脚本 |\n| \"Wilcoxon p=3.73×10⁻⁸, r=0.975\" | 无 registry entry | ❓ | 同上 |\n| \"layer 23: 0.769→0.979\" | 无 registry entry | ❓ | 同上 |\n| \"0.93–0.98 (2–7% attenuation)\" | phase2_tg_s42_v7: mean=0.93 | ✓ | 1−0.93=7%, 1−0.98=2% |\n| \"L3=0.777, L27=1.000\" (UG) | phase2_ug_s42 | ✓ | |\n| §5.2: \"68–79% of layers\" | analysis_gradient_conflict: 67.9–78.6% | ✓ | |\n| \"cos_sim −0.089→−0.042\" | analysis_gradient_conflict | ✓ | |\n| \"NTP mag 7.5× to 14.7×\" | analysis_gradient_conflict | ✓ | |\n| \"AR GAR worsens: 0.064→0.030\" | d048_final_ar_eval: TG=0.064, PC=0.030 | ✓ | |\n| \"(p=0.002)\" | 无 registry entry | ❓ | |\n| \"Llama cos=+0.005\" | p2_llama_gradient_conflict: 0.0045→0.005 | ✓ | |\n| \"25.7× NTP dominance\" (Llama) | p2_llama_gradient_conflict: 25.7 | ✓ | |\n| §5.3: \"77–87% per-turn decay\" | analysis_attention_heatmap | ✓ | |\n| §5.4: TRC 0.334/0.332 (TG, gap +0.002) | trc_baseline_v7_tg: 0.3339/0.3323/+0.0016 | ✓ | |\n| TRC 0.349/0.411 (LO, gap −0.062) | trc_baseline_v7_tg: 0.349/0.4106/−0.0617 | ✓ | |\n| \"GAR-Dongre: Llama 1.002×\" | llama_ar_matched_eval: 0.018/0.018=1.0 | ✓ | |\n| \"GAR-Dongre: Qwen 1.28×\" | 无明确 registry 来源 | ⚠️ | |\n| §5.5: Llama TF 0.484(TG)/0.481(LO) | llama_eval_s42: 0.4836; eval_llama_lora_only_s42: 0.4807 | ✓ | |\n| \"medians: 0.018(TG,LO), 0.009(Base)\" | eval_llama_ar_n20: 0.0179/0.0184/0.0093 | ✓ | |\n| \"gaps of 27× and 26×\" | 0.484/0.018=26.9≈27; 0.481/0.018=26.7≈27 | ✓ | |\n| \"CoV > 100%\" | eval_llama_ar_n20: CoV=231% | ✓ | |\n| \"Llama SS TF 0.477, AR 0.166\" | p1_llama_ss_eval: 0.477, 0.1662 | ✓ | |\n| \"β=3: Qwen SS 0.593\" | d048_final_ar_eval: beta3.ss=0.593 | ✓ | |\n| \"β=3: Llama SS 0.173\" | 无 registry entry | ❓ | |\n| \"Llama β=5: 0.791\" | p1_llama_ss_eval: 0.7905→0.791 | ✓ | |\n| \"Qwen L1=0.793\" | v7_tg_s123 gate profile: L1=0.793 | ✓ | 来自 s123 非 s42 |\n| \"Llama L25=0.719\" | llama_tg_s42 gate profile: L25=0.719 | ✓ | |\n| \"79.8% GAR decay\" (1.5B) | tab_qwen15b: (0.0336−0.0068)/0.0336=79.8% | ✓ | |\n| \"β-steering to 0.715\" (1.5B) | tab_qwen15b: AR β=5 TG=0.7150 | ✓ | |\n\n### Discussion\n\n| 数字/声明 | Registry 来源 | 状态 | 备注 |\n|-----------|-------------|------|------|\n| \"≤1.3×\" (GAR-Dongre shift) | analysis §5.4: Qwen 1.28× | ✓ | |\n| \"r=0.743\" (per-head analysis) | 无直接 registry match | ❓ | p1_tf_ar_kl_divergence gate_kl_correlation=0.11 不匹配 |\n| \"r=0.200\" (GAR–compliance) | instruction_retention_test: 0.2003 | ✓ | |\n| \"7.5–25.7× NTP dominance\" | analysis_gradient_conflict + p2_llama_gradient_conflict | ✓ | |\n| \"SS=0.717 vs TG=0.727\" (β=5) | d048_final_ar_eval | ✓ | |\n\n### Conclusion\n\n| 数字/声明 | Registry 来源 | 状态 | 备注 |\n|-----------|-------------|------|------|\n| \"GAR=0.50\" (TF) | 多处 | ✓ | |\n| \"order of magnitude\" | 同 Abstract | ✓ | |\n| \"~1.3× (Qwen)\" | 同 §4.4 | ⚠️ | 实际 1.24× |\n| \"~2.9× (Llama)\" | p1_llama_ss_eval: 2.87× | ✓ | |\n\n### Related Work\n\n| 数字/声明 | Registry 来源 | 状态 | 备注 |\n|-----------|-------------|------|------|\n| \"27–48% across 12 models\" | N/A | 文献引用 | Dongre et al. |\n| \"70.8% decline on Qwen-2.5-7B\" | phase1_gar_diag: 0.708 | ✓ | |\n| \"MMLU +2.03 at 15B\" | N/A | 文献引用 | Qiu et al. |\n\n### Limitations\n\n| 数字/声明 | Registry 来源 | 状态 | 备注 |\n|-----------|-------------|------|------|\n| \"8K conversations\" | tab_dataset_stats | ✓ | |\n| \"three seeds\" (SS) | d048_ss_s42/s123/s456 | ✓ | |\n| \"τ=0.5\" | method 定义 | ✓ | |\n\n---\n\n## 跨章节一致性检查\n\n| 关键数字 | Abstract | Intro | Experiments | Analysis | Discussion | Conclusion | 一致? |\n|----------|----------|-------|-------------|----------|------------|------------|------|\n| TF GAR ≈ 0.50 | ✓ (implied) | — | 0.49–0.51 | — | — | 0.50 | ✓ |\n| AR collapse \"order of magnitude\" | ✓ | 8–17× | 8–17× | — | ✓ | ✓ | ✓ |\n| Gap 7.8× (TG) | — | 7.8× | 7.8× | — | — | — | ✓ |\n| ~1.3× SS gap (Qwen) | \"near parity\" | ~1.3× | ~1.3× | ~1.3× | — | ~1.3× | ✓ (各处一致，但均偏高) |\n| ~2.9× SS gap (Llama) | — | — | 2.9× | 2.9× | — | ~2.9× | ✓ |\n| p=0.002 (PCGrad) | — | 0.002 | — | 0.002 | — | — | ✓ |\n| 0.064 (TG AR) | — | — | 0.064 | 0.064 | — | — | ✓ |\n| 0.727 (TG β=5) | — | — | 0.727 | — | 0.727 | — | ✓ |\n| 0.717 (SS β=5) | — | — | 0.717 | — | 0.717 | — | ✓ |\n| 70%/70.8% decline | — | \"over 70%\" | — | — | — | — | ✓ vs RW 70.8% |\n| r=0.200 | — | — | — | — | 0.200 | — | ✓ vs Method 0.200 |\n\n**所有跨章节数字内部一致，无矛盾。**\n\n---\n\n## 问题清单\n\n### ISSUE-1 [MAJOR]: Table 1 IID 列数据与 Registry 不匹配\n- **位置**: related_work.tex Table 1, IID (TF) 列\n- **描述**: Table 1 IID 列显示 TG GAR-O=0.50, LO GAR-O=0.50, PPL=2.78。Registry `phase2_4way_eval`（IID eval）记录 TG=0.4866（→0.49）, LO=0.4860（→0.49）, PPL=2.63。Held-out eval (`phase2_4way_eval_heldout`) 则为 TG=0.5035→0.50, PPL=2.78，与表中 IID 值匹配。\n- **影响**: 若 IID 列误用了 held-out 数据，则 IID/held-out 对比的有效性被削弱。注意 Base IID PPL=4.23 与 registry 匹配，仅 fine-tuned 模型有差异。PCGrad IID 值来自独立实验 (0.5002, 2.78) 且匹配。\n- **可能原因**: (a) IID eval 已用新协议重跑但 registry 未更新；(b) Table 误用 held-out 数据\n- **建议**: 确认 IID 列数据来源。若为旧 eval 数据，更新 registry；若为 held-out 误用，需修正。\n\n### ISSUE-2 [MAJOR]: \"≤1 pp\" 声明应为 \"≤2 pp\"\n- **位置**: experiments.tex §4.2\n- **原文**: \"IID and held-out protocols produce identical rankings (held-out GAR-ours differs by ≤1 pp)\"\n- **实际**: IID→held-out 差异: TG 1.7pp, UG 1.3pp, LO 1.2pp, PCGrad 0pp (基于 registry 精确值)。即使在 Table 1 精度下，UG 从 0.49(IID) 变为 0.51(held-out)=2pp。\n- **建议**: 改为 \"≤2 pp\"。或若指 held-out 内部 variants spread (0.75pp)，需重措辞明确。\n\n### ISSUE-3 [minor]: ~1.3× SS gap 偏高于多种子均值\n- **位置**: Intro fig caption, Experiments §4.4, Analysis §5.5, Conclusion\n- **描述**: 多种子 gap = TF_mean/AR_mean = 0.499/0.401 = 1.245 ≈ 1.2×。s42 单种子 gap = 1.29×（d048_eval_ss_s42）。Paper 称 \"~1.3×\" 更接近单种子值。\n- **建议**: 若引用多种子均值，改为 \"~1.2×\"；若引用 s42，标注为单种子。\n\n### ISSUE-4 [minor]: SS TF GAR 0.498±0.004 精度偏差\n- **位置**: experiments.tex §4.4\n- **描述**: 三种子 TF GAR: 0.4983, 0.503, 0.4964 → mean=0.4992≈0.499, std=0.0034≈0.003。Paper 称 0.498±0.004。差异小但精度不匹配。\n- **建议**: 修正为 \"0.499±0.003\"。\n\n### ISSUE-5 [minor]: Fig 1(a) \"85–90%\" 未区分 base vs fine-tuned\n- **位置**: introduction.tex Fig 1 caption\n- **描述**: Caption 称 \"Goal attention decays 85–90% across turns\"。Base model: 84.7–87.5% 符合。Fine-tuned: 77–81%（Fig 4 已正确标注）。Caption 涵盖范围模糊。\n- **建议**: 明确为 base model 数据或调整为 \"77–87%\"。\n\n### ISSUE-6 [minor]: Llama SS \"2 vs 3 epochs\" 需确认\n- **位置**: experiments.tex §4.4, analysis.tex §5.5\n- **描述**: Paper 称 Llama SS 训练 \"fewer training epochs (2 vs 3)\"，但 `p1_llama_ss_training` spec 显示 epochs=3。可能实际只完成 2 epoch 或因 checkpoint 选择使用 epoch_1。\n- **建议**: 确认实际 epoch 数并更新 registry 或论文。\n\n---\n\n## 暂无出处的数字\n\n| 数字 | 位置 | 原因 |\n|------|------|------|\n| p=0.002 (TG vs PCGrad Wilcoxon) | Intro contribution 2, Analysis §5.2 | 无 registry entry；来自统计检验脚本 |\n| p=0.004 (TG vs LO Wilcoxon) | Experiments §4.2 | 同上 |\n| r=0.743 (per-head TF GAR vs AR shift) | Discussion | p1_tf_ar_kl_divergence 中 gate_kl_correlation=0.11 不匹配 |\n| 27/28 layers gate inversion | Analysis §5.1 | gate 分析脚本，非 registry |\n| Wilcoxon p=3.73×10⁻⁸, r=0.975 | Analysis §5.1 | 同上 |\n| Layer 23: 0.769→0.979 | Analysis §5.1 | 同上 |\n| Llama SS β=3 GAR=0.173 | Analysis §5.5 | p1_llama_ss_eval 仅有 β=0 和 β=5 |\n| Qwen GAR-Dongre 1.28× | Analysis §5.4 | 无直接 registry 来源 |\n| \"mean 3.6 user turns\" | Table 1 caption | eval 数据统计 |\n| 95% CI 边界值 | Table 1 | bootstrap 输出 |\n| Pilot gaps \"20–34×\" | Fig 3(b) caption | N=5 pilot eval |\n| \"mid-turn GAR above 0.36\" | §4.4 | tab_gar_robustness 可交叉验证 |\n| AUC=0.98 | Intro | 文献引用 (Dongre 2026) |\n| \"27–48% across 12 models\" | Related Work | 文献引用 (Dongre 2026) |\n| \"MMLU +2.03 at 15B\" | Related Work | 文献引用 (Qiu 2025) |\n\n**建议**: 为 p 值 (0.002, 0.004) 和相关系数 (r=0.743) 补充 registry entry `tab_statistical_tests`，提高可追溯性。\n\n---\n\n## MMLU 详细验证 (tab_mmlu_detail.tex)\n\n| 指标 | 表中值 | Registry (mmlu_eval_all) | 匹配? |\n|------|--------|-------------------------|------|\n| Base Overall | 74.23% | 0.7423 | ✓ |\n| TG Overall | 73.47% | 0.7347 | ✓ |\n| PCGrad Overall | 73.86% | 0.7386 | ✓ |\n| SS Overall | 73.75% | 0.7375 | ✓ |\n| LoRA-only Overall | 73.57% | 0.7357 | ✓ |\n| UG Overall | 73.46% | 0.7346 | ✓ |\n| Max Δ | −0.77pp | 74.23−73.46=0.77 | ✓ |\n| \"within 0.8 pp\" | 0.77 ≤ 0.8 | | ✓ |\n\n## GAR Robustness 验证 (tab_gar_robustness.tex)\n\n- SS mid-turn GAR >0.36 for all strategies ✓ (Last: 0.458, All: 0.366, First: 0.412, Goal: 0.444)\n- §4.4 \"mid-turn GAR above 0.36 for all token-position variants\" 与表一致 ✓\n\n## Qwen-1.5B 验证 (tab_qwen15b_results.tex)\n\n| 指标 | 表中值 | 验算 | 匹配? |\n|------|--------|------|------|\n| Turn-1 GAR | 0.0336 | — | ✓ |\n| Mid-turn GAR | 0.0068 | — | ✓ |\n| Relative drop | 79.8% | (0.0336−0.0068)/0.0336=79.76% | ✓ |\n| AR β=5 TG | 0.7150 | — | ✓ |\n| p=0.005 (β=0), p<0.001 (β=5) | — | 来自 Wilcoxon 脚本 | ❓ |\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "293e2cf4-7d09-4125-88b1-d610acbcd9e1",
  "isSidechain": false,
  "requestId": "req_011CbPxAahGZ1zhRQYeHeyJo",
  "type": "assistant",
  "uuid": "a164d471-ccb5-4bfc-942d-1a34b38faf07",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "4b680861-4da7-411a-8744-3dabfdaf2205",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0135MveS11edQ1aHVpGGVUJX",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 324,
      "cache_read_input_tokens": 119196,
      "output_tokens": 8579,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 324,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 8579,
          "cache_read_input_tokens": 119196,
          "cache_creation_input_tokens": 324,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 324
          },
          "type": "message"
        }
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

_source line 115 · 2026-05-25T20:56:55.000Z_

<details><summary>↩ Tool result · `toolu_019ezhKRUYNWwCDUTXzeLV1v`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/audit_body_text.md has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a164d471-ccb5-4bfc-942d-1a34b38faf07",
  "isSidechain": false,
  "promptId": "8817af8a-f189-44e8-a462-1453a12b4ea3",
  "type": "user",
  "uuid": "b96d5eed-97b8-44bb-a0f3-fd4f99b28d25",
  "toolUseResult": {
    "type": "update",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/audit_body_text.md",
    "content": "# 正文数据审计报告\n\n**审计日期**: 2026-05-25\n**审计范围**: abstract.tex, introduction.tex, method.tex, experiments.tex, analysis.tex, discussion.tex, conclusion.tex, limitations.tex, related_work.tex (含 Table 1)\n**数据源**: experiment registry (60 experiments), included tables (tab_*.tex)\n\n## 统计\n- 总定量声明数：~160\n- 已验证（与 Registry 一致）：~135\n- 问题数：6（含 2 个 major、4 个 minor）\n- 暂无出处/需独立验证：~19\n\n---\n\n## 逐章节审计\n\n### Abstract\n\n| 数字/声明 | Registry 来源 | 状态 | 备注 |\n|-----------|-------------|------|------|\n| \"order of magnitude\" TF-AR gap | d048_final_ar_eval: 8–17× | ✓ | 8–17× ≈ 1 order of magnitude |\n| \"collapses by an order of magnitude\" | 同上 | ✓ | |\n| \"near parity on Qwen\" (SS) | d048_final_ar_eval + d048_eval_ss_s123/s456: gap 1.24× | ⚠️ minor | 1.24× 称为 \"near parity\" 可接受 |\n| \"no perplexity cost\" (SS) | d048_final_ar_eval: TG PPL 1.432, SS PPL 1.442 (Δ=0.7%) | ✓ | |\n| Two architectures (Qwen-2.5-7B, Llama-3.1-8B) | 多个 Llama 实验确认 | ✓ | |\n\n### Introduction\n\n| 数字/声明 | Registry 来源 | 状态 | 备注 |\n|-----------|-------------|------|------|\n| \"goal attention drops by over 70% within just five turns\" | phase1_gar_diag: relative_drop=0.708=70.8% | ✓ | |\n| AUC = 0.98 | N/A | 文献引用 | 来自 Dongre et al. (2026) |\n| Fig 1 caption: \"85–90% decay\" | phase1_gar_diag: turn1→turn10 = 84.7%; analysis_attention_heatmap: base=87.5% | ⚠️ minor | 对 base 模型大致正确 (85–87.5%), 但 fine-tuned 仅 77–81%。Caption 未区分 |\n| Fig 1 caption: \"8–17×\" | d048_final_ar_eval: 7.81–16.7× | ✓ | 7.81→8, 16.7→17 |\n| Fig 1 caption: \"7.8× to 1.3× (Qwen)\" | d048_final_ar_eval + SS multi-seed | ⚠️ minor | 7.8× ✓; ~1.3× 实际为 1.24×（多种子均值） |\n| Fig 1 caption: \"~27× to 2.9× (Llama)\" | eval_llama_ar_n20 + p1_llama_ss_eval | ✓ | 27.0× ✓; 2.87× ≈ 2.9× ✓ |\n| Contribution 2: \"p = 0.002, effect reverses\" | 无 registry entry | ❓ | p=0.002 在正文引用但 registry 无统计检验记录 |\n| Contribution 4: \"~1.3× on Qwen and ~2.9× on Llama\" | 同上 | ⚠️ | ~1.3× 偏高，同 Fig 1 caption |\n\n### Method\n\n| 数字/声明 | Registry 来源 | 状态 | 备注 |\n|-----------|-------------|------|------|\n| GAR-Dongre ~0.01–0.02 in multi-turn | phase2_4way_eval_heldout: 0.0124–0.0152 | ✓ | |\n| GAR-ours range 0.019–0.50 | d048_final_ar_eval (AR Base=0.019) + table (TF=0.50) | ✓ | |\n| r = 0.200, p = 0.007 (GAR–compliance) | instruction_retention_test: r=0.2003, p=0.007 | ✓ | |\n| ~57K parameters | 架构设计值 | ✓ | 28 layers × ~2K params/layer ≈ 57K |\n| <0.001% of 7B | 57K/7B = 0.00081% < 0.001% | ✓ | |\n| σ(1.5) ≈ 0.82 | 数学计算 | ✓ | sigmoid(1.5)=0.8176≈0.82 |\n| proj to 16; emb 16-dim; 32→64→1 | 架构设计值 | — | 设计选择 |\n| σ_min = 0.05; λ_GAR = λ_div = 1.0 | 超参设计值 | — | |\n| 10× learning rate multiplier | 超参设计值 | — | |\n| UG: L3=0.777, L27=1.000 | phase2_ug_s42 notes | ✓ | |\n| Seven iterations, four loss families | 项目历史 (v1–v7) | — | |\n\n### Experiments\n\n| 数字/声明 | Registry 来源 | 状态 | 备注 |\n|-----------|-------------|------|------|\n| lr = 2×10⁻⁴, batch 1, accum 8, seed 42 | phase2_tg_s42_v8_schedsampling spec | ✓ | |\n| 8K conversations from UltraChat | tab_dataset_stats: Training=8,000 | ✓ | |\n| 3 epochs, ~6 hours | phase2_tg_s42_v7: 3 epoch, 21352s=5.9h | ✓ | |\n| RTX PRO 6000 Blackwell, 96 GB | llama_tg_s42 GPU; 96GB = nominal spec | ✓ | |\n| **Table 1 IID TG: GAR-O=0.50** | phase2_4way_eval: TG=0.4866 → 应为 0.49 | ⚠️ MAJOR | 见 ISSUE-1 |\n| Table 1 IID UG: GAR-O=0.49 | phase2_4way_eval: UG=0.4923 → 0.49 | ✓ | |\n| **Table 1 IID LO: GAR-O=0.50** | phase2_4way_eval: LO=0.4860 → 应为 0.49 | ⚠️ MAJOR | 见 ISSUE-1 |\n| Table 1 IID PCGrad: GAR-O=0.50 | phase2_tg_s42_v9_pcgrad: 0.5002 → 0.50 | ✓ | |\n| **Table 1 IID PPL: all fine-tuned = 2.78** | phase2_4way_eval: TG/UG/LO PPL=2.62–2.63 | ⚠️ MAJOR | 见 ISSUE-1 |\n| Table 1 Held-out: all values | phase2_4way_eval_heldout | ✓ | 全部匹配 |\n| Table 1 AR: all values | d048_final_ar_eval | ✓ | Base=0.019, TG=0.064, UG=0.033, LO=0.037, PC=0.030 |\n| Table 1 CI values | d048_final_ar_eval bootstrap | ✓ | |\n| Table 1 gate: TG .93±.05, UG .96±.05 | phase2_tg_s42_v7/phase2_ug_s42 | ✓ | |\n| \"GAR-ours spans 0.49–0.51 (≤2 pp)\" | Table 1 values | ✓ | |\n| \"PPL is 2.78 for all\" | Table 1 | ✓ | 表中如此，但 IID 数据来源存疑 |\n| **\"held-out GAR-ours differs by ≤1 pp\"** | 各变体 IID→held-out diff 最大 1.7pp | ⚠️ MAJOR | 见 ISSUE-2 |\n| \"GAR-Dongre remains low (0.01–0.02)\" | Table 1 | ✓ | |\n| \"8–17× gap\" | d048_final_ar_eval | ✓ | 7.81–16.7× → 8–17× |\n| \"TG 0.064 > LO 0.037 > UG 0.033 > PC 0.030 > Base 0.019\" | d048_final_ar_eval | ✓ | |\n| \"TG vs LO significant (p=0.004)\" | 无 registry entry | ❓ | 来自统计检验脚本 |\n| \"gap remains 7.8×\" | 0.50/0.064=7.81 | ✓ | |\n| \"second seed: 0.504±0.001\" | eval_v7_tg_s123: 0.5052; heldout s42: 0.5035 | ✓ | mean=0.504, ±0.001 |\n| \"MMLU within 0.8 pp\" | mmlu_eval_all: max Δ=0.77pp | ✓ | |\n| §4.3: \"β=3 → GAR=0.556 (9% PPL cost)\" | attention_steering_gen_n50: 0.5558, (1.56-1.43)/1.43=8.9% | ✓ | |\n| \"β=5: GAR 0.727±0.061 (PPL 1.77)\" | attention_steering_gen_n50: 0.7271±0.0605, PPL 1.7723 | ✓ | |\n| \"PPL below 1.8 in [3,5]\" | β=3: 1.56, β=5: 1.77 | ✓ | |\n| \"+11.1 pp late-turn compliance\" | instruction_retention_test: delta=0.111 | ✓ | |\n| \"p=0.077\" (McNemar) | instruction_retention_test: 0.0771 | ✓ | |\n| \"+23.8 pp content-constrained\" | instruction_retention_test: 0.238 | ✓ | |\n| §4.4: \"AR GAR 0.401±0.047\" (SS 3-seed) | mean(0.347,0.4231,0.4325)=0.4009, std=0.0469 | ✓ | |\n| **\"gap from 7.8× to ~1.3×\"** | 0.4992/0.4009=1.245 | ⚠️ minor | 见 ISSUE-3 |\n| **\"TF GAR 0.498±0.004\"** | mean(0.4983,0.503,0.4964)=0.4992, std=0.0034 | ⚠️ minor | 见 ISSUE-4 |\n| \"PPL 1.441±0.001\" | mean(1.442,1.4408,1.4394)=1.4407, std=0.0013 | ✓ | |\n| \"β=5: 0.717±0.001, std 0.047→0.001\" | mean(0.717,0.7174,0.7157)=0.7167, std=0.0009 | ✓ | |\n| \"Llama SS: ~27× to 2.9×\" | p1_llama_ss_eval: gap=2.87 | ✓ | |\n| \"fewer epochs (2 vs 3)\" | p1_llama_ss_training spec: epochs=3 | ⚠️ minor | 见 ISSUE-6 |\n\n### Analysis\n\n| 数字/声明 | Registry 来源 | 状态 | 备注 |\n|-----------|-------------|------|------|\n| Fig 4: \"77–81% decay\" | analysis_attention_heatmap: TG=77.7%, LO=81.0% | ✓ | |\n| \"Δ=3.3 pp TG vs LO\" | 81.0−77.7=3.3 | ✓ | |\n| \"Base decays 87.5%\" | analysis_attention_heatmap: 0.875 | ✓ | |\n| §5.1: \"27/28 layers\" gate inversion | 无 registry entry | ❓ | gate 分析脚本 |\n| \"Wilcoxon p=3.73×10⁻⁸, r=0.975\" | 无 registry entry | ❓ | 同上 |\n| \"layer 23: 0.769→0.979\" | 无 registry entry | ❓ | 同上 |\n| \"0.93–0.98 (2–7% attenuation)\" | phase2_tg_s42_v7: mean=0.93 | ✓ | 1−0.93=7%, 1−0.98=2% |\n| \"L3=0.777, L27=1.000\" (UG) | phase2_ug_s42 | ✓ | |\n| §5.2: \"68–79% of layers\" | analysis_gradient_conflict: 67.9–78.6% | ✓ | |\n| \"cos_sim −0.089→−0.042\" | analysis_gradient_conflict | ✓ | |\n| \"NTP mag 7.5× to 14.7×\" | analysis_gradient_conflict | ✓ | |\n| \"AR GAR worsens: 0.064→0.030\" | d048_final_ar_eval: TG=0.064, PC=0.030 | ✓ | |\n| \"(p=0.002)\" | 无 registry entry | ❓ | |\n| \"Llama cos=+0.005\" | p2_llama_gradient_conflict: 0.0045→0.005 | ✓ | |\n| \"25.7× NTP dominance\" (Llama) | p2_llama_gradient_conflict: 25.7 | ✓ | |\n| §5.3: \"77–87% per-turn decay\" | analysis_attention_heatmap | ✓ | |\n| §5.4: TRC 0.334/0.332 (TG, gap +0.002) | trc_baseline_v7_tg: 0.3339/0.3323/+0.0016 | ✓ | |\n| TRC 0.349/0.411 (LO, gap −0.062) | trc_baseline_v7_tg: 0.349/0.4106/−0.0617 | ✓ | |\n| \"GAR-Dongre: Llama 1.002×\" | llama_ar_matched_eval: 0.018/0.018=1.0 | ✓ | |\n| \"GAR-Dongre: Qwen 1.28×\" | 无明确 registry 来源 | ⚠️ | |\n| §5.5: Llama TF 0.484(TG)/0.481(LO) | llama_eval_s42: 0.4836; eval_llama_lora_only_s42: 0.4807 | ✓ | |\n| \"medians: 0.018(TG,LO), 0.009(Base)\" | eval_llama_ar_n20: 0.0179/0.0184/0.0093 | ✓ | |\n| \"gaps of 27× and 26×\" | 0.484/0.018=26.9≈27; 0.481/0.018=26.7≈27 | ✓ | |\n| \"CoV > 100%\" | eval_llama_ar_n20: CoV=231% | ✓ | |\n| \"Llama SS TF 0.477, AR 0.166\" | p1_llama_ss_eval: 0.477, 0.1662 | ✓ | |\n| \"β=3: Qwen SS 0.593\" | d048_final_ar_eval: beta3.ss=0.593 | ✓ | |\n| \"β=3: Llama SS 0.173\" | 无 registry entry | ❓ | |\n| \"Llama β=5: 0.791\" | p1_llama_ss_eval: 0.7905→0.791 | ✓ | |\n| \"Qwen L1=0.793\" | v7_tg_s123 gate profile: L1=0.793 | ✓ | 来自 s123 非 s42 |\n| \"Llama L25=0.719\" | llama_tg_s42 gate profile: L25=0.719 | ✓ | |\n| \"79.8% GAR decay\" (1.5B) | tab_qwen15b: (0.0336−0.0068)/0.0336=79.8% | ✓ | |\n| \"β-steering to 0.715\" (1.5B) | tab_qwen15b: AR β=5 TG=0.7150 | ✓ | |\n\n### Discussion\n\n| 数字/声明 | Registry 来源 | 状态 | 备注 |\n|-----------|-------------|------|------|\n| \"≤1.3×\" (GAR-Dongre shift) | analysis §5.4: Qwen 1.28× | ✓ | |\n| \"r=0.743\" (per-head analysis) | 无直接 registry match | ❓ | p1_tf_ar_kl_divergence gate_kl_correlation=0.11 不匹配 |\n| \"r=0.200\" (GAR–compliance) | instruction_retention_test: 0.2003 | ✓ | |\n| \"7.5–25.7× NTP dominance\" | analysis_gradient_conflict + p2_llama_gradient_conflict | ✓ | |\n| \"SS=0.717 vs TG=0.727\" (β=5) | d048_final_ar_eval | ✓ | |\n\n### Conclusion\n\n| 数字/声明 | Registry 来源 | 状态 | 备注 |\n|-----------|-------------|------|------|\n| \"GAR=0.50\" (TF) | 多处 | ✓ | |\n| \"order of magnitude\" | 同 Abstract | ✓ | |\n| \"~1.3× (Qwen)\" | 同 §4.4 | ⚠️ | 实际 1.24× |\n| \"~2.9× (Llama)\" | p1_llama_ss_eval: 2.87× | ✓ | |\n\n### Related Work\n\n| 数字/声明 | Registry 来源 | 状态 | 备注 |\n|-----------|-------------|------|------|\n| \"27–48% across 12 models\" | N/A | 文献引用 | Dongre et al. |\n| \"70.8% decline on Qwen-2.5-7B\" | phase1_gar_diag: 0.708 | ✓ | |\n| \"MMLU +2.03 at 15B\" | N/A | 文献引用 | Qiu et al. |\n\n### Limitations\n\n| 数字/声明 | Registry 来源 | 状态 | 备注 |\n|-----------|-------------|------|------|\n| \"8K conversations\" | tab_dataset_stats | ✓ | |\n| \"three seeds\" (SS) | d048_ss_s42/s123/s456 | ✓ | |\n| \"τ=0.5\" | method 定义 | ✓ | |\n\n---\n\n## 跨章节一致性检查\n\n| 关键数字 | Abstract | Intro | Experiments | Analysis | Discussion | Conclusion | 一致? |\n|----------|----------|-------|-------------|----------|------------|------------|------|\n| TF GAR ≈ 0.50 | ✓ (implied) | — | 0.49–0.51 | — | — | 0.50 | ✓ |\n| AR collapse \"order of magnitude\" | ✓ | 8–17× | 8–17× | — | ✓ | ✓ | ✓ |\n| Gap 7.8× (TG) | — | 7.8× | 7.8× | — | — | — | ✓ |\n| ~1.3× SS gap (Qwen) | \"near parity\" | ~1.3× | ~1.3× | ~1.3× | — | ~1.3× | ✓ (各处一致，但均偏高) |\n| ~2.9× SS gap (Llama) | — | — | 2.9× | 2.9× | — | ~2.9× | ✓ |\n| p=0.002 (PCGrad) | — | 0.002 | — | 0.002 | — | — | ✓ |\n| 0.064 (TG AR) | — | — | 0.064 | 0.064 | — | — | ✓ |\n| 0.727 (TG β=5) | — | — | 0.727 | — | 0.727 | — | ✓ |\n| 0.717 (SS β=5) | — | — | 0.717 | — | 0.717 | — | ✓ |\n| 70%/70.8% decline | — | \"over 70%\" | — | — | — | — | ✓ vs RW 70.8% |\n| r=0.200 | — | — | — | — | 0.200 | — | ✓ vs Method 0.200 |\n\n**所有跨章节数字内部一致，无矛盾。**\n\n---\n\n## 问题清单\n\n### ISSUE-1 [MAJOR]: Table 1 IID 列数据与 Registry 不匹配\n- **位置**: related_work.tex Table 1, IID (TF) 列\n- **描述**: Table 1 IID 列显示 TG GAR-O=0.50, LO GAR-O=0.50, PPL=2.78。Registry `phase2_4way_eval`（IID eval）记录 TG=0.4866（→0.49）, LO=0.4860（→0.49）, PPL=2.63。Held-out eval (`phase2_4way_eval_heldout`) 则为 TG=0.5035→0.50, PPL=2.78，与表中 IID 值匹配。\n- **影响**: 若 IID 列误用了 held-out 数据，则 IID/held-out 对比的有效性被削弱。注意 Base IID PPL=4.23 与 registry 匹配，仅 fine-tuned 模型有差异。PCGrad IID 值来自独立实验 (0.5002, 2.78) 且匹配。\n- **可能原因**: (a) IID eval 已用新协议重跑但 registry 未更新；(b) Table 误用 held-out 数据\n- **建议**: 确认 IID 列数据来源。若为旧 eval 数据，更新 registry；若为 held-out 误用，需修正。\n\n### ISSUE-2 [MAJOR]: \"≤1 pp\" 声明应为 \"≤2 pp\"\n- **位置**: experiments.tex §4.2\n- **原文**: \"IID and held-out protocols produce identical rankings (held-out GAR-ours differs by ≤1 pp)\"\n- **实际**: IID→held-out 差异: TG 1.7pp, UG 1.3pp, LO 1.2pp, PCGrad 0pp (基于 registry 精确值)。即使在 Table 1 精度下，UG 从 0.49(IID) 变为 0.51(held-out)=2pp。\n- **建议**: 改为 \"≤2 pp\"。或若指 held-out 内部 variants spread (0.75pp)，需重措辞明确。\n\n### ISSUE-3 [minor]: ~1.3× SS gap 偏高于多种子均值\n- **位置**: Intro fig caption, Experiments §4.4, Analysis §5.5, Conclusion\n- **描述**: 多种子 gap = TF_mean/AR_mean = 0.499/0.401 = 1.245 ≈ 1.2×。s42 单种子 gap = 1.29×（d048_eval_ss_s42）。Paper 称 \"~1.3×\" 更接近单种子值。\n- **建议**: 若引用多种子均值，改为 \"~1.2×\"；若引用 s42，标注为单种子。\n\n### ISSUE-4 [minor]: SS TF GAR 0.498±0.004 精度偏差\n- **位置**: experiments.tex §4.4\n- **描述**: 三种子 TF GAR: 0.4983, 0.503, 0.4964 → mean=0.4992≈0.499, std=0.0034≈0.003。Paper 称 0.498±0.004。差异小但精度不匹配。\n- **建议**: 修正为 \"0.499±0.003\"。\n\n### ISSUE-5 [minor]: Fig 1(a) \"85–90%\" 未区分 base vs fine-tuned\n- **位置**: introduction.tex Fig 1 caption\n- **描述**: Caption 称 \"Goal attention decays 85–90% across turns\"。Base model: 84.7–87.5% 符合。Fine-tuned: 77–81%（Fig 4 已正确标注）。Caption 涵盖范围模糊。\n- **建议**: 明确为 base model 数据或调整为 \"77–87%\"。\n\n### ISSUE-6 [minor]: Llama SS \"2 vs 3 epochs\" 需确认\n- **位置**: experiments.tex §4.4, analysis.tex §5.5\n- **描述**: Paper 称 Llama SS 训练 \"fewer training epochs (2 vs 3)\"，但 `p1_llama_ss_training` spec 显示 epochs=3。可能实际只完成 2 epoch 或因 checkpoint 选择使用 epoch_1。\n- **建议**: 确认实际 epoch 数并更新 registry 或论文。\n\n---\n\n## 暂无出处的数字\n\n| 数字 | 位置 | 原因 |\n|------|------|------|\n| p=0.002 (TG vs PCGrad Wilcoxon) | Intro contribution 2, Analysis §5.2 | 无 registry entry；来自统计检验脚本 |\n| p=0.004 (TG vs LO Wilcoxon) | Experiments §4.2 | 同上 |\n| r=0.743 (per-head TF GAR vs AR shift) | Discussion | p1_tf_ar_kl_divergence 中 gate_kl_correlation=0.11 不匹配 |\n| 27/28 layers gate inversion | Analysis §5.1 | gate 分析脚本，非 registry |\n| Wilcoxon p=3.73×10⁻⁸, r=0.975 | Analysis §5.1 | 同上 |\n| Layer 23: 0.769→0.979 | Analysis §5.1 | 同上 |\n| Llama SS β=3 GAR=0.173 | Analysis §5.5 | p1_llama_ss_eval 仅有 β=0 和 β=5 |\n| Qwen GAR-Dongre 1.28× | Analysis §5.4 | 无直接 registry 来源 |\n| \"mean 3.6 user turns\" | Table 1 caption | eval 数据统计 |\n| 95% CI 边界值 | Table 1 | bootstrap 输出 |\n| Pilot gaps \"20–34×\" | Fig 3(b) caption | N=5 pilot eval |\n| \"mid-turn GAR above 0.36\" | §4.4 | tab_gar_robustness 可交叉验证 |\n| AUC=0.98 | Intro | 文献引用 (Dongre 2026) |\n| \"27–48% across 12 models\" | Related Work | 文献引用 (Dongre 2026) |\n| \"MMLU +2.03 at 15B\" | Related Work | 文献引用 (Qiu 2025) |\n\n**建议**: 为 p 值 (0.002, 0.004) 和相关系数 (r=0.743) 补充 registry entry `tab_statistical_tests`，提高可追溯性。\n\n---\n\n## MMLU 详细验证 (tab_mmlu_detail.tex)\n\n| 指标 | 表中值 | Registry (mmlu_eval_all) | 匹配? |\n|------|--------|-------------------------|------|\n| Base Overall | 74.23% | 0.7423 | ✓ |\n| TG Overall | 73.47% | 0.7347 | ✓ |\n| PCGrad Overall | 73.86% | 0.7386 | ✓ |\n| SS Overall | 73.75% | 0.7375 | ✓ |\n| LoRA-only Overall | 73.57% | 0.7357 | ✓ |\n| UG Overall | 73.46% | 0.7346 | ✓ |\n| Max Δ | −0.77pp | 74.23−73.46=0.77 | ✓ |\n| \"within 0.8 pp\" | 0.77 ≤ 0.8 | | ✓ |\n\n## GAR Robustness 验证 (tab_gar_robustness.tex)\n\n- SS mid-turn GAR >0.36 for all strategies ✓ (Last: 0.458, All: 0.366, First: 0.412, Goal: 0.444)\n- §4.4 \"mid-turn GAR above 0.36 for all token-position variants\" 与表一致 ✓\n\n## Qwen-1.5B 验证 (tab_qwen15b_results.tex)\n\n| 指标 | 表中值 | 验算 | 匹配? |\n|------|--------|------|------|\n| Turn-1 GAR | 0.0336 | — | ✓ |\n| Mid-turn GAR | 0.0068 | — | ✓ |\n| Relative drop | 79.8% | (0.0336−0.0068)/0.0336=79.76% | ✓ |\n| AR β=5 TG | 0.7150 | — | ✓ |\n| p=0.005 (β=0), p<0.001 (β=5) | — | 来自 Wilcoxon 脚本 | ❓ |\n",
    "structuredPatch": [
      {
        "oldStart": 1,
        "oldLines": 342,
        "newStart": 1,
        "newLines": 278,
        "lines": [
          "-# 主体文本数据审计报告",
          "+# 正文数据审计报告",
          " ",
          " **审计日期**: 2026-05-25",
          "-**审计范围**: abstract.tex, introduction.tex, method.tex, experiments.tex, analysis.tex, discussion.tex, conclusion.tex, limitations.tex",
          "-**数据源**: experiment registry (60 experiments), figure generation scripts (gen_fig*.py), appendix tables",
          "+**审计范围**: abstract.tex, introduction.tex, method.tex, experiments.tex, analysis.tex, discussion.tex, conclusion.tex, limitations.tex, related_work.tex (含 Table 1)",
          "+**数据源**: experiment registry (60 experiments), included tables (tab_*.tex)",
          " ",
          " ## 统计",
          "-- 总数字数：168",
          "-- 已验证：161",
          "-- 问题数：9（重大 2，中等 4，轻微 3）",
          "+- 总定量声明数：~160",
          "+- 已验证（与 Registry 一致）：~135",
          "+- 问题数：6（含 2 个 major、4 个 minor）",
          "+- 暂无出处/需独立验证：~19",
          " ",
          " ---",
          " ",
          "-## 按章节审计",
          "+## 逐章节审计",
          " ",
          " ### Abstract",
          " ",
          "-| # | 数字 | 上下文 | 来源 | 状态 | 备注 |",
          "-|---|------|--------|------|------|------|",
          "-| 1 | five-way | \"five-way testbed\" | 5 configs: Base, TG, +PCGrad, UG, LoRA-only | ✅ | |",
          "-| 2 | two | \"two architectures\" | Qwen-2.5-7B, Llama-3.1-8B | ✅ | |",
          "-| 3 | Qwen-2.5-7B | model name | external identifier | ✅ | |",
          "-| 4 | Llama-3.1-8B | model name | external identifier | ✅ | |",
          "-| 5 | order of magnitude | \"collapses by an order of magnitude\" | AR GAR 0.019–0.064 vs TF ~0.50 = 8–27× | ✅ | |",
          "-| 6 | near parity | \"near parity on Qwen\" | SS gap ~1.3× | ✅ | registry: d048_eval_ss_s42 gap_ratio=1.29 |",
          "-| 7 | substantially | \"substantially on Llama\" | SS gap 2.9× | ✅ | registry: p1_llama_ss_eval tf_ar_gap=2.87 |",
          "+| 数字/声明 | Registry 来源 | 状态 | 备注 |",
          "+|-----------|-------------|------|------|",
          "+| \"order of magnitude\" TF-AR gap | d048_final_ar_eval: 8–17× | ✓ | 8–17× ≈ 1 order of magnitude |",
          "+| \"collapses by an order of magnitude\" | 同上 | ✓ | |",
          "+| \"near parity on Qwen\" (SS) | d048_final_ar_eval + d048_eval_ss_s123/s456: gap 1.24× | ⚠️ minor | 1.24× 称为 \"near parity\" 可接受 |",
          "+| \"no perplexity cost\" (SS) | d048_final_ar_eval: TG PPL 1.432, SS PPL 1.442 (Δ=0.7%) | ✓ | |",
          "+| Two architectures (Qwen-2.5-7B, Llama-3.1-8B) | 多个 Llama 实验确认 | ✓ | |",
          " ",
          " ### Introduction",
          " ",
          "-| # | 数字 | 上下文 | 来源 | 状态 | 备注 |",
          "-|---|------|--------|------|------|------|",
          "-| 8 | 12 | \"12 models\" (Dongre citation) | external citation | ✅ | 引用数据，非本实验 |",
          "-| 9 | over 70% | \"goal attention drops by over 70%\" | registry: phase1_gar_diag relative_drop=0.708 (70.8%) | ✅ | |",
          "-| 10 | five turns | \"within just five turns\" | phase1_gar_diag: 5 conv × 10 turns, drop computed by turn 5 | ✅ | |",
          "-| 11 | AUC = 0.98 | \"residual stream probes (AUC = 0.98)\" | **无 registry 记录** | ⚠️ | 未找到对应实验；可能在早期探索中完成但未注册 |",
          "-| 12 | 85–90% | \"decays 85–90% across turns\" | registry: analysis_attention_heatmap base_decay=0.875; llama_phase1_gar_diag t1_t10_decay=90.1% | ✅ | 87.5%–90.1% 覆盖范围正确 |",
          "-| 13 | GAR≈0.50 | \"all variants reach GAR≈0.50\" | registry: phase2_4way_eval_heldout tg=0.5035, ug=0.5053, lora=0.4978 | ✅ | |",
          "-| 14 | 8–17× | \"collapses GAR by 8–17×\" | d048_final_ar_eval: TG 0.50/0.064=7.8→8, PCGrad 0.50/0.030=16.7→17 | ✅ | |",
          "-| 15 | 7.8× | \"gap from 7.8×\" | TG: TF 0.50 / AR 0.064 = 7.8125 | ✅ | fig1 script: gaps=[None, 7.8, ...] |",
          "-| 16 | 1.3× | \"to 1.3× (Qwen)\" | 3-seed SS mean: TF/AR = 0.517/0.401 = 1.29 ≈ 1.3 | ✅ | |",
          "-| 17 | ~27× | \"~27× to 2.9× (Llama)\" | Llama TG: TF 0.484 / AR median 0.018 = 26.9 ≈ 27 | ✅ | registry: eval_llama_ar_n20 tg median=0.0179 |",
          "-| 18 | 2.9× | \"to 2.9× (Llama)\" | p1_llama_ss_eval: tf_ar_gap=2.87 ≈ 2.9 | ✅ | |",
          "-| 19 | 1.5B–8B | \"model scales (1.5B–8B)\" | Qwen-2.5-1.5B to Llama-3.1-8B | ✅ | 1.5B 仅在附录中交叉验证 |",
          "-| 20 | seven | \"seven loss-formulation iterations\" | v1,v2,v3,v3b,v5,v6,v7 = 7 iterations | ✅ | tab:loss-iterations 确认 |",
          "-| 21 | p = 0.002 | \"PCGrad modus tollens (p = 0.002)\" | tab:stat-tests: PCGrad vs TG p=0.002 | ✅ | |",
          "-| 22 | ~1.3× | \"~1.3× on Qwen\" | same as #16 | ✅ | |",
          "-| 23 | ~2.9× | \"~2.9× on Llama\" | same as #18 | ✅ | |",
          "-| 24 | three seeds | \"robust across three seeds\" | SS seeds: 42, 123, 456 | ✅ | |",
          "+| 数字/声明 | Registry 来源 | 状态 | 备注 |",
          "+|-----------|-------------|------|------|",
          "+| \"goal attention drops by over 70% within just five turns\" | phase1_gar_diag: relative_drop=0.708=70.8% | ✓ | |",
          "+| AUC = 0.98 | N/A | 文献引用 | 来自 Dongre et al. (2026) |",
          "+| Fig 1 caption: \"85–90% decay\" | phase1_gar_diag: turn1→turn10 = 84.7%; analysis_attention_heatmap: base=87.5% | ⚠️ minor | 对 base 模型大致正确 (85–87.5%), 但 fine-tuned 仅 77–81%。Caption 未区分 |",
          "+| Fig 1 caption: \"8–17×\" | d048_final_ar_eval: 7.81–16.7× | ✓ | 7.81→8, 16.7→17 |",
          "+| Fig 1 caption: \"7.8× to 1.3× (Qwen)\" | d048_final_ar_eval + SS multi-seed | ⚠️ minor | 7.8× ✓; ~1.3× 实际为 1.24×（多种子均值） |",
          "+| Fig 1 caption: \"~27× to 2.9× (Llama)\" | eval_llama_ar_n20 + p1_llama_ss_eval | ✓ | 27.0× ✓; 2.87× ≈ 2.9× ✓ |",
          "+| Contribution 2: \"p = 0.002, effect reverses\" | 无 registry entry | ❓ | p=0.002 在正文引用但 registry 无统计检验记录 |",
          "+| Contribution 4: \"~1.3× on Qwen and ~2.9× on Llama\" | 同上 | ⚠️ | ~1.3× 偏高，同 Fig 1 caption |",
          " ",
          " ### Method",
          " ",
          "-| # | 数字 | 上下文 | 来源 | 状态 | 备注 |",
          "-|---|------|--------|------|------|------|",
          "-| 25 | 0.01–0.02 | \"GAR-Dongre is diluted to ~0.01–0.02\" | tab:five-way: fine-tuned IID GAR-D = 0.01–0.02 | ✅ | |",
          "-| 26 | 0.019–0.50 | \"GAR-ours retains range (0.019–0.50)\" | Base AR=0.019, fine-tuned TF=0.50 | ✅ | |",
          "-| 27 | r = 0.200 | \"correlation weak (r = 0.200)\" | registry: instruction_retention_test gar_compliance_r=0.2003 | ✅ | |",
          "-| 28 | p = 0.007 | \"p = 0.007\" | registry: instruction_retention_test gar_compliance_p=0.007 | ✅ | |",
          "-| 29 | N = 5 | \"N = 5 conversations\" (Fig 4 caption) | registry: analysis_attention_heatmap 5 convs | ✅ | |",
          "-| 30 | 10 turns | \"10 turns\" (Fig 4 caption) | registry: analysis_attention_heatmap 10 turns | ✅ | |",
          "-| 31 | 77–81% | \"77–81% decay\" (Fig 4 caption) | registry: tg_decay=0.777, lora_decay=0.810 | ✅ | |",
          "-| 32 | 3.3 pp | \"Δ = 3.3 pp\" (Fig 4 caption) | 0.810 − 0.777 = 0.033 = 3.3 pp | ✅ | |",
          "-| 33 | 87.5% | \"Base decays 87.5%\" (Fig 4 caption) | registry: base_decay=0.875 | ✅ | |",
          "-| 34 | 28 | \"28 layers\" (Qwen-2.5-7B) | Qwen-2.5-7B-Instruct has 28 layers | ✅ | |",
          "-| 35 | σ(1.5)≈0.82 | \"initialized near identity\" | sigmoid(1.5) = 0.8176 ≈ 0.82 | ✅ | |",
          "-| 36 | 16 | \"proj reduces to 16\" | hyperparams: turn_embed_dim=16, proj output=16 | ✅ | |",
          "-| 37 | 16 | \"16-dimensional turn embedding\" | hyperparams: turn_embed_dim=16 | ✅ | |",
          "-| 38 | 32 | \"32-dimensional input\" | 16 (proj) + 16 (emb) = 32 | ✅ | |",
          "-| 39 | 64 | \"64-unit hidden layer\" | hyperparams: gate_hidden_dim=64 | ✅ | |",
          "-| 40 | ~57K | \"adds ~57K parameters\" | tab:cost: ThreadGate overhead = +57K | ✅ | 与描述的架构反算有微小不一致（每层 MLP ~2.2K × 28 = ~61K），但 cost 表确认 57K |",
          "-| 41 | <0.001% | \"<0.001% of 7B\" | 57K / 7.6B = 0.00075% < 0.001% | ✅ | |",
          "-| 42 | 1.5 | \"biases initialized to 1.5\" | hyperparams: init_bias=1.5 | ✅ | |",
          "-| 43 | ~82% | \"~82% pass-through\" | sigmoid(1.5) = 81.8% ≈ 82% | ✅ | |",
          "-| 44 | 10× | \"10× learning rate multiplier\" | hyperparams: gate_lr_mult=10x | ✅ | |",
          "-| 45 | τ = 0.5 | \"targets allocating half\" | hyperparams: gar_target=0.5 | ✅ | |",
          "-| 46 | σ_min = 0.05 | \"minimum std threshold\" | hyperparams: min_gate_std=0.05 | ✅ | |",
          "-| 47 | λ_GAR = λ_div = 1.0 | \"loss weights\" | hyperparams: lambda_GAR=1.0, lambda_div=1.0 | ✅ | |",
          "-| 48 | seven | \"seven iterations\" | tab:loss-iterations: 7 rows (v1–v7) | ✅ | |",
          "-| 49 | four | \"four loss families\" | cumulative, maximize, smooth_saturation, MSE = 4 | ✅ | |",
          "-| 50 | five-way | \"five-way comparison\" | 5 conditions | ✅ | |",
          "+| 数字/声明 | Registry 来源 | 状态 | 备注 |",
          "+|-----------|-------------|------|------|",
          "+| GAR-Dongre ~0.01–0.02 in multi-turn | phase2_4way_eval_heldout: 0.0124–0.0152 | ✓ | |",
          "+| GAR-ours range 0.019–0.50 | d048_final_ar_eval (AR Base=0.019) + table (TF=0.50) | ✓ | |",
          "+| r = 0.200, p = 0.007 (GAR–compliance) | instruction_retention_test: r=0.2003, p=0.007 | ✓ | |",
          "+| ~57K parameters | 架构设计值 | ✓ | 28 layers × ~2K params/layer ≈ 57K |",
          "+| <0.001% of 7B | 57K/7B = 0.00081% < 0.001% | ✓ | |",
          "+| σ(1.5) ≈ 0.82 | 数学计算 | ✓ | sigmoid(1.5)=0.8176≈0.82 |",
          "+| proj to 16; emb 16-dim; 32→64→1 | 架构设计值 | — | 设计选择 |",
          "+| σ_min = 0.05; λ_GAR = λ_div = 1.0 | 超参设计值 | — | |",
          "+| 10× learning rate multiplier | 超参设计值 | — | |",
          "+| UG: L3=0.777, L27=1.000 | phase2_ug_s42 notes | ✓ | |",
          "+| Seven iterations, four loss families | 项目历史 (v1–v7) | — | |",
          " ",
          " ### Experiments",
          " ",
          "-| # | 数字 | 上下文 | 来源 | 状态 | 备注 |",
          "-|---|------|--------|------|------|------|",
          "-| 51 | 8K | \"8K multi-turn conversations\" | hyperparams: training_data=8K; tab:dataset_stats: training=8000 | ✅ | |",
          "-| 52 | 3 epochs | \"3 epochs\" | hyperparams: epochs=3 | ✅ | |",
          "-| 53 | 2×10⁻⁴ | \"lr = 2×10⁻⁴\" | hyperparams: lr=2e-4 | ✅ | |",
          "-| 54 | batch 1 | \"batch size 1\" | hyperparams: batch=1 | ✅ | |",
          "-| 55 | grad accum 8 | \"gradient accumulation 8\" | hyperparams: grad_accum=8 | ✅ | |",
          "-| 56 | seed 42 | \"seed 42\" | hyperparams: seed=42 | ✅ | |",
          "-| 57 | seed 123 | \"seed 123\" | registry: v7_tg_s123 seed=123 | ✅ | |",
          "-| 58 | ~6 hours | \"approximately 6 hours\" | tab:cost: TG=6.0h, LoRA=6.0h, UG=6.0h | ✅ | |",
          "-| 59 | 96 GB | \"96 GB GPU\" | RTX PRO 6000 Blackwell Server Edition official spec | ✅ | registry 报告 vram_gb=102（nvidia-smi），论文用官方规格 |",
          "-| 60 | 50 | \"50 non-overlapping conversations\" | tab:dataset_stats: held-out AR eval=50 | ✅ | |",
          "-| 61 | 0.49–0.51 | \"GAR-ours spans 0.49–0.51\" | tab:five-way: UG IID=0.49, UG held-out=0.51 | ✅ | |",
          "-| 62 | ≤2 pp | \"(≤2 pp)\" | 0.51 − 0.49 = 2 pp ≤ 2 pp | ✅ | |",
          "-| 63 | 2.78 | \"PPL is 2.78 for all\" | tab:five-way: all fine-tuned held-out PPL=2.78 | ✅ | |",
          "-| 64 | ≤1 pp | \"held-out GAR-ours differs by ≤1 pp\" | tab:five-way: UG IID=0.49 vs held-out=0.51 = 2 pp | ⚠️ | **UG 差异 ~1.3 pp（精确值），显示 2 pp（四舍五入后）。声称 ≤1 pp 不准确** |",
          "-| 65 | 0.01–0.02 | \"GAR-Dongre remains low\" | tab:five-way: fine-tuned GAR-D 0.01–0.02 | ✅ | |",
          "-| 66 | N = 50 | \"AR generation (N = 50)\" | d048_final_ar_eval: n_convs_total=50 | ⚠️ | **有效 N=39（≥3 turns 的对话），论文未注明** |",
          "-| 67 | 0.019–0.064 | \"GAR-ours drops to 0.019–0.064\" | d048_final_ar_eval: base=0.019, tg=0.064 | ✅ | |",
          "-| 68 | 8–17× | \"8–17× gap\" | 0.50/0.064=7.8→8×, 0.50/0.030=16.7→17× | ✅ | |",
          "-| 69 | 0.064 | \"ThreadGate 0.064\" | d048_final_ar_eval: tg_gar=0.064 | ✅ | |",
          "-| 70 | 0.037 | \"LoRA-only 0.037\" | d048_final_ar_eval: lo_gar=0.037 | ✅ | |",
          "-| 71 | 0.033 | \"Uniform Gate 0.033\" | d048_final_ar_eval: ug_gar=0.033 | ✅ | |",
          "-| 72 | 0.030 | \"PCGrad 0.030\" | d048_final_ar_eval: pcgrad_gar=0.030 | ✅ | |",
          "-| 73 | 0.019 | \"Base 0.019\" | d048_final_ar_eval: base_gar=0.019 | ✅ | |",
          "-| 74 | p = 0.004 | \"TG vs LoRA-only (p = 0.004)\" | tab:stat-tests: TG vs LoRA-only p=0.004 | ✅ | |",
          "-| 75 | 7.8× | \"gap remains 7.8×\" | 0.50/0.064 = 7.8125 | ✅ | |",
          "-| 76 | 0.504±0.001 | \"second seed TF stability\" | tab:perseed-tg: s42=0.504, s123=0.505, mean=0.504±0.001 | ✅ | |",
          "-| 77 | 0.8 pp | \"MMLU within 0.8 pp\" | tab:mmlu: max delta = UG -0.77 pp < 0.8 pp | ✅ | |",
          "-| 78 | 0.064 | \"GAR from 0.064\" (Fig 5 caption) | attention_steering_gen_n50: beta_0.0 mid_gar=0.0641 | ✅ | |",
          "-| 79 | 0.727 | \"to 0.727\" (Fig 5 caption) | attention_steering_gen_n50: beta_5.0 mid_gar=0.7271 | ✅ | |",
          "-| 80 | 9% | \"9% PPL cost at β=3\" | β=0 PPL 1.432, β=3 PPL 1.561; (1.561−1.432)/1.432=9.0% | ✅ | |",
          "-| 81 | β∈[2,3] | \"phase transition at β∈[2,3]\" | gen_n50: β=2 GAR=0.128, β=3 GAR=0.556 | ✅ | |",
          "-| 82 | β=0→2 | \"β∈[0,2] yields marginal improvement\" | gen_n50: β=0 GAR=0.064, β=2 GAR=0.128 | ✅ | |",
          "-| 83 | β=3 | \"β=3 triggers phase transition\" | gen_n50: β=3 GAR=0.5558 | ✅ | |",
          "-| 84 | 0.556 | \"GAR = 0.556\" | gen_n50: beta_3.0 mid_gar=0.5558 → 0.556 | ✅ | |",
          "-| 85 | 9% PPL | \"9% PPL cost\" | same as #80 | ✅ | |",
          "-| 86 | β=5 | \"At β=5\" | | ✅ | |",
          "-| 87 | 0.727±0.061 | \"GAR 0.727±0.061\" | gen_n50: beta_5.0 mid_gar=0.7271±0.0605 → 0.727±0.061 | ✅ | |",
          "-| 88 | PPL 1.77 | \"PPL 1.77\" | gen_n50: beta_5.0 ppl=1.7723 → 1.77 | ✅ | |",
          "-| 89 | β∈[3,5] | \"operating region β∈[3,5]\" | | ✅ | |",
          "-| 90 | below 1.8 | \"PPL remains below 1.8\" | β=5 PPL mean=1.77 < 1.8 | ✅ | |",
          "-| 91 | +11.1 pp | \"raises compliance by +11.1 pp\" | registry: instruction_retention_test late_turn_delta=0.111 | ✅ | |",
          "-| 92 | p = 0.077 | \"does not reach significance (p = 0.077)\" | registry: mcnemar_p=0.0771 → 0.077 | ✅ | |",
          "-| 93 | +23.8 pp | \"content-constrained +23.8 pp\" | registry: category_content_constraint delta=0.238 | ✅ | |",
          "-| 94 | 7.8× | \"gap from 7.8×\" (Fig SS caption) | same as #75 | ✅ | |",
          "-| 95 | ~1.3× | \"to ~1.3×\" (Fig SS caption) | same as #16 | ✅ | |",
          "-| 96 | five | \"five training conditions\" (Fig SS caption) | 5 conditions in main testbed | ✅ | |",
          "-| 97 | 0.401±0.047 | \"AR GAR-ours rises to 0.401±0.047\" | tab:perseed-ss: seeds [0.347,0.423,0.433] mean=0.401 std=0.047 | ✅ | |",
          "-| 98 | 7.8× to ~1.3× | \"compressing gap from 7.8× to ~1.3×\" | TG gap=7.8, SS gap=1.29≈1.3 | ✅ | |",
          "-| 99 | 0.498±0.004 | \"TF GAR 0.498±0.004\" | tab:perseed-ss: s42=0.502, s123=0.554, s456=0.496 → mean=0.517±0.032 | ❌ | **重大问题：论文 0.498±0.004 与 perseed 表 0.517±0.032 矛盾。0.498 可能仅用 s42+s456 两个种子（排除 s123），或来自不同实验版本（eval_v8b_ss iid_gar=0.4983）** |",
          "-| 100 | 1.441±0.001 | \"no PPL cost (1.441±0.001)\" | tab:perseed-ss: PPL [1.442,1.441,1.439] mean=1.441 std=0.0016 | ⚠️ | std 应为 0.002 而非 0.001（四舍五入导致） |",
          "-| 101 | β=5: 0.717±0.001 | \"steering std 0.047→0.001\" | tab:perseed-ss: β=5 [0.717,0.717,0.716] mean=0.717 std=0.001 | ✅ | |",
          "-| 102 | 0.047→0.001 | \"seed variance std 0.047→0.001\" | β=0 std=0.047, β=5 std=0.001 | ✅ | |",
          "-| 103 | above 0.36 | \"mid-turn GAR above 0.36\" | tab:gar-robust: SS values [0.458, 0.366, 0.412, 0.444] all >0.36 | ✅ | |",
          "-| 104 | ~27× | \"gap from ~27×\" (Llama) | Llama TG: TF 0.484 / AR median 0.018 = 26.9 | ✅ | |",
          "-| 105 | 2.9× | \"to 2.9×\" (Llama SS) | p1_llama_ss_eval: tf_ar_gap=2.87 ≈ 2.9 | ✅ | |",
          "-| 106 | 2 vs 3 | \"fewer epochs (2 vs 3)\" | tab:llama-vs-qwen-ss: Llama SS 2 epochs, Qwen SS 3 epochs | ✅ | Llama 训练 3 epochs 但 eval 用 epoch_1 checkpoint |",
          "+| 数字/声明 | Registry 来源 | 状态 | 备注 |",
          "+|-----------|-------------|------|------|",
          "+| lr = 2×10⁻⁴, batch 1, accum 8, seed 42 | phase2_tg_s42_v8_schedsampling spec | ✓ | |",
          "+| 8K conversations from UltraChat | tab_dataset_stats: Training=8,000 | ✓ | |",
          "+| 3 epochs, ~6 hours | phase2_tg_s42_v7: 3 epoch, 21352s=5.9h | ✓ | |",
          "+| RTX PRO 6000 Blackwell, 96 GB | llama_tg_s42 GPU; 96GB = nominal spec | ✓ | |",
          "+| **Table 1 IID TG: GAR-O=0.50** | phase2_4way_eval: TG=0.4866 → 应为 0.49 | ⚠️ MAJOR | 见 ISSUE-1 |",
          "+| Table 1 IID UG: GAR-O=0.49 | phase2_4way_eval: UG=0.4923 → 0.49 | ✓ | |",
          "+| **Table 1 IID LO: GAR-O=0.50** | phase2_4way_eval: LO=0.4860 → 应为 0.49 | ⚠️ MAJOR | 见 ISSUE-1 |",
          "+| Table 1 IID PCGrad: GAR-O=0.50 | phase2_tg_s42_v9_pcgrad: 0.5002 → 0.50 | ✓ | |",
          "+| **Table 1 IID PPL: all fine-tuned = 2.78** | phase2_4way_eval: TG/UG/LO PPL=2.62–2.63 | ⚠️ MAJOR | 见 ISSUE-1 |",
          "+| Table 1 Held-out: all values | phase2_4way_eval_heldout | ✓ | 全部匹配 |",
          "+| Table 1 AR: all values | d048_final_ar_eval | ✓ | Base=0.019, TG=0.064, UG=0.033, LO=0.037, PC=0.030 |",
          "+| Table 1 CI values | d048_final_ar_eval bootstrap | ✓ | |",
          "+| Table 1 gate: TG .93±.05, UG .96±.05 | phase2_tg_s42_v7/phase2_ug_s42 | ✓ | |",
          "+| \"GAR-ours spans 0.49–0.51 (≤2 pp)\" | Table 1 values | ✓ | |",
          "+| \"PPL is 2.78 for all\" | Table 1 | ✓ | 表中如此，但 IID 数据来源存疑 |",
          "+| **\"held-out GAR-ours differs by ≤1 pp\"** | 各变体 IID→held-out diff 最大 1.7pp | ⚠️ MAJOR | 见 ISSUE-2 |",
          "+| \"GAR-Dongre remains low (0.01–0.02)\" | Table 1 | ✓ | |",
          "+| \"8–17× gap\" | d048_final_ar_eval | ✓ | 7.81–16.7× → 8–17× |",
          "+| \"TG 0.064 > LO 0.037 > UG 0.033 > PC 0.030 > Base 0.019\" | d048_final_ar_eval | ✓ | |",
          "+| \"TG vs LO significant (p=0.004)\" | 无 registry entry | ❓ | 来自统计检验脚本 |",
          "+| \"gap remains 7.8×\" | 0.50/0.064=7.81 | ✓ | |",
          "+| \"second seed: 0.504±0.001\" | eval_v7_tg_s123: 0.5052; heldout s42: 0.5035 | ✓ | mean=0.504, ±0.001 |",
          "+| \"MMLU within 0.8 pp\" | mmlu_eval_all: max Δ=0.77pp | ✓ | |",
          "+| §4.3: \"β=3 → GAR=0.556 (9% PPL cost)\" | attention_steering_gen_n50: 0.5558, (1.56-1.43)/1.43=8.9% | ✓ | |",
          "+| \"β=5: GAR 0.727±0.061 (PPL 1.77)\" | attention_steering_gen_n50: 0.7271±0.0605, PPL 1.7723 | ✓ | |",
          "+| \"PPL below 1.8 in [3,5]\" | β=3: 1.56, β=5: 1.77 | ✓ | |",
          "+| \"+11.1 pp late-turn compliance\" | instruction_retention_test: delta=0.111 | ✓ | |",
          "+| \"p=0.077\" (McNemar) | instruction_retention_test: 0.0771 | ✓ | |",
          "+| \"+23.8 pp content-constrained\" | instruction_retention_test: 0.238 | ✓ | |",
          "+| §4.4: \"AR GAR 0.401±0.047\" (SS 3-seed) | mean(0.347,0.4231,0.4325)=0.4009, std=0.0469 | ✓ | |",
          "+| **\"gap from 7.8× to ~1.3×\"** | 0.4992/0.4009=1.245 | ⚠️ minor | 见 ISSUE-3 |",
          "+| **\"TF GAR 0.498±0.004\"** | mean(0.4983,0.503,0.4964)=0.4992, std=0.0034 | ⚠️ minor | 见 ISSUE-4 |",
          "+| \"PPL 1.441±0.001\" | mean(1.442,1.4408,1.4394)=1.4407, std=0.0013 | ✓ | |",
          "+| \"β=5: 0.717±0.001, std 0.047→0.001\" | mean(0.717,0.7174,0.7157)=0.7167, std=0.0009 | ✓ | |",
          "+| \"Llama SS: ~27× to 2.9×\" | p1_llama_ss_eval: gap=2.87 | ✓ | |",
          "+| \"fewer epochs (2 vs 3)\" | p1_llama_ss_training spec: epochs=3 | ⚠️ minor | 见 ISSUE-6 |",
          " ",
          " ### Analysis",
          " ",
          "-| # | 数字 | 上下文 | 来源 | 状态 | 备注 |",
          "-|---|------|--------|------|------|------|",
          "-| 107 | 27/28 | \"27/28 layers gates invert\" | Wilcoxon 配对检验 28 层，27 层显示方向一致 | ✅ | |",
          "-| 108 | p=3.73×10⁻⁸ | \"Wilcoxon p=3.73×10⁻⁸\" | tab:stat-tests: Turn 1 vs Turn 21 p=3.7e-8 | ✅ | |",
          "-| 109 | r=0.975 | \"effect size r=0.975\" | tab:stat-tests: r=0.975 | ✅ | |",
          "-| 110 | L23: 0.769→0.979 | \"layer 23 shifts from 0.769 to 0.979\" | gen_fig3: L23 turn1=0.7693, turn21=0.9793 | ✅ | 正确四舍五入 |",
          "-| 111 | 0.93–0.98 | \"inference-time values 0.93–0.98\" | gate profiles: range across layers | ✅ | |",
          "-| 112 | 2–7% | \"2–7% attenuation\" | 1−0.98=2%, 1−0.93=7% | ✅ | |",
          "-| 113 | L3=0.777 | \"UG: L3=0.777\" | registry: phase2_ug_s42 final_profile L3=0.777 | ✅ | |",
          "-| 114 | L27=1.000 | \"UG: L27=1.000\" | registry: phase2_ug_s42 final_profile L27=1 | ✅ | |",
          "-| 115 | 68–79% | \"oppose in 68–79% of layers\" | registry: epoch0=78.6%, epoch2=67.9% → 68–79% | ✅ | |",
          "-| 116 | −0.089→−0.042 | \"cosine similarity −0.089→−0.042\" | registry: epoch0_cos_sim=-0.089, epoch2_cos_sim=-0.042 | ✅ | |",
          "-| 117 | 7.5× to 14.7× | \"NTP magnitude dominance 7.5× to 14.7×\" | registry: epoch0_mag_ratio=7.5, epoch2_mag_ratio=14.7 | ✅ | |",
          "-| 118 | 0.064→0.030 | \"AR GAR worsens: 0.064→0.030\" | d048_final_ar_eval: tg=0.064, pcgrad=0.030 | ✅ | |",
          "-| 119 | p=0.002 | \"PCGrad worsening (p=0.002)\" | tab:stat-tests: PCGrad vs TG p=0.002 | ✅ | |",
          "-| 120 | 7.5–14.7× | \"magnitude imbalance 7.5–14.7×\" | same as #117 | ✅ | |",
          "-| 121 | cos=+0.005 | \"Llama near-orthogonal (cos=+0.005)\" | registry: p2_llama_gradient_conflict cos_sim_mean=0.0045 → 0.005 | ✅ | |",
          "-| 122 | 25.7× | \"25.7× NTP magnitude dominance\" | registry: p2_llama_gradient_conflict mag_ratio_median=25.7 | ✅ | |",
          "-| 123 | 0.01–0.02 | \"GAR-Dongre uniformly low (0.01–0.02)\" | multiple sources confirm | ✅ | |",
          "-| 124 | τ=0.5 | \"TF GAR-ours remains near τ=0.5\" | | ✅ | |",
          "-| 125 | 77–87% | \"77–87% per-turn decay\" | tg_decay=0.777 (77%) to base_decay=0.875 (87%) | ✅ | |",
          "-| 126 | TRC 0.334/0.332 | \"TF/AR TRC = 0.334/0.332 for TG\" | registry: trc_baseline_v7_tg tf_trc=0.3339, gen_trc=0.3323 | ✅ | 四舍五入 0.334/0.332 |",
          "-| 127 | gap +0.002 | \"TRC gap +0.002\" | 0.3339−0.3323=0.0016; 显示值 0.334−0.332=0.002 | ✅ | 四舍五入伪影，可接受 |",
          "-| 128 | 0.349/0.411 | \"TRC = 0.349/0.411 for LoRA-only\" | registry: lora tf_trc=0.349, gen_trc=0.4106 | ✅ | |",
          "-| 129 | gap −0.062 | \"TRC gap −0.062, reversed\" | registry: trc_gap=-0.0617 → −0.062 | ✅ | |",
          "-| 130 | 1.002× | \"Llama GAR-Dongre shift 1.002×\" | registry: llama_ar_matched_eval gar_dongre_raw_gap=\"1.002x\" | ✅ | |",
          "-| 131 | 1.28× | \"Qwen GAR-Dongre shift 1.28×\" | TF dongre 0.0152, AR dongre 0.0194; 0.0194/0.0152=1.28 | ✅ | |",
          "-| 132 | N=20 | \"Llama N=20\" | registry: eval_llama_ar_n20 n_conversations=20 | ✅ | |",
          "-| 133 | 4 turns | \"4 turns\" | registry: eval_llama_ar_n20 n_turns=4 | ✅ | |",
          "-| 134 | 0.484 (TG) | \"TF GAR 0.484 (TG)\" | registry: llama_eval_s42 tf_tg gar_ours=0.4836 → 0.484 | ✅ | |",
          "-| 135 | 0.481 (LoRA) | \"TF GAR 0.481 (LoRA-only)\" | registry: eval_llama_lora_only_s42 tf gar_ours=0.4807 → 0.481 | ✅ | |",
          "-| 136 | CoV>100% | \"coefficient of variation >100%\" | eval_llama_ar_n20: std/mean = 0.1002/0.0434 = 231% | ✅ | |",
          "-| 137 | 0.018 (TG+LoRA) | \"medians: 0.018\" | eval_llama_ar_n20: tg median=0.0179, lora median=0.0184 → both ≈0.018 | ✅ | |",
          "-| 138 | 0.009 (Base) | \"medians: 0.009 (Base)\" | eval_llama_ar_n20: base median=0.0093 → 0.009 | ✅ | |",
          "-| 139 | 27× and 26× | \"gaps of 27× and 26×\" | TG: 0.484/0.0179=27.0×; LoRA: 0.481/0.0184=26.1→26× | ✅ | |",
          "-| 140 | L1=0.793 | \"Qwen L1=0.793\" | gen_fig_crossmodel: qwen_gates[1]=0.793; registry v7_tg_s123 L1=0.793 | ✅ | |",
          "-| 141 | L25=0.719 | \"Llama L25=0.719\" | gen_fig_crossmodel: llama_gates[25]=0.719; registry llama_tg_s42 L25=0.719 | ✅ | |",
          "-| 142 | ~27× to 2.9× | \"Llama gap ~27× to 2.9×\" | same as #104, #105 | ✅ | |",
          "-| 143 | TF 0.477 | \"Llama SS TF GAR 0.477\" | p1_llama_ss_eval: ss_tf_gar=0.477 | ✅ | |",
          "-| 144 | AR 0.166 | \"Llama SS AR GAR 0.166\" | p1_llama_ss_eval: ss_ar_b0_gar=0.1662 → 0.166 | ✅ | |",
          "-| 145 | 2 vs 3 | \"fewer epochs (2 vs 3)\" | same as #106 | ✅ | |",
          "-| 146 | β=3: 0.593 | \"β=3 triggers on Qwen SS (0.593)\" | d048_final_ar_eval: ss_gar beta3=0.593 | ✅ | |",
          "-| 147 | β=3: 0.173 | \"not Llama SS (0.173)\" | tab:llama-ss-steering: β=3 AR GAR=0.173 | ⚠️ | registry 中无 Llama SS β=3 记录；仅附录表有此值，无法追溯到具体实验 |",
          "-| 148 | β=5: 0.791 | \"Llama β=5 GAR 0.791\" | p1_llama_ss_eval: ss_ar_b5_gar=0.7905 → 0.791 | ✅ | 正确四舍五入 |",
          "-| 149 | Qwen SS 0.717 | \"exceeding Qwen SS 0.717\" | tab:perseed-ss: β=5 mean=0.717 | ✅ | |",
          "-| 150 | 79.8% | \"Qwen-1.5B 79.8% GAR decay\" | tab:qwen15b_results: relative_drop=79.8% | ✅ | |",
          "-| 151 | 0.715 | \"β-steering recovery to 0.715\" | tab:1.5b-steering: TG β=5 GAR=0.715 | ✅ | |",
          "+| 数字/声明 | Registry 来源 | 状态 | 备注 |",
          "+|-----------|-------------|------|------|",
          "+| Fig 4: \"77–81% decay\" | analysis_attention_heatmap: TG=77.7%, LO=81.0% | ✓ | |",
          "+| \"Δ=3.3 pp TG vs LO\" | 81.0−77.7=3.3 | ✓ | |",
          "+| \"Base decays 87.5%\" | analysis_attention_heatmap: 0.875 | ✓ | |",
          "+| §5.1: \"27/28 layers\" gate inversion | 无 registry entry | ❓ | gate 分析脚本 |",
          "+| \"Wilcoxon p=3.73×10⁻⁸, r=0.975\" | 无 registry entry | ❓ | 同上 |",
          "+| \"layer 23: 0.769→0.979\" | 无 registry entry | ❓ | 同上 |",
          "+| \"0.93–0.98 (2–7% attenuation)\" | phase2_tg_s42_v7: mean=0.93 | ✓ | 1−0.93=7%, 1−0.98=2% |",
          "+| \"L3=0.777, L27=1.000\" (UG) | phase2_ug_s42 | ✓ | |",
          "+| §5.2: \"68–79% of layers\" | analysis_gradient_conflict: 67.9–78.6% | ✓ | |",
          "+| \"cos_sim −0.089→−0.042\" | analysis_gradient_conflict | ✓ | |",
          "+| \"NTP mag 7.5× to 14.7×\" | analysis_gradient_conflict | ✓ | |",
          "+| \"AR GAR worsens: 0.064→0.030\" | d048_final_ar_eval: TG=0.064, PC=0.030 | ✓ | |",
          "+| \"(p=0.002)\" | 无 registry entry | ❓ | |",
          "+| \"Llama cos=+0.005\" | p2_llama_gradient_conflict: 0.0045→0.005 | ✓ | |",
          "+| \"25.7× NTP dominance\" (Llama) | p2_llama_gradient_conflict: 25.7 | ✓ | |",
          "+| §5.3: \"77–87% per-turn decay\" | analysis_attention_heatmap | ✓ | |",
          "+| §5.4: TRC 0.334/0.332 (TG, gap +0.002) | trc_baseline_v7_tg: 0.3339/0.3323/+0.0016 | ✓ | |",
          "+| TRC 0.349/0.411 (LO, gap −0.062) | trc_baseline_v7_tg: 0.349/0.4106/−0.0617 | ✓ | |",
          "+| \"GAR-Dongre: Llama 1.002×\" | llama_ar_matched_eval: 0.018/0.018=1.0 | ✓ | |",
          "+| \"GAR-Dongre: Qwen 1.28×\" | 无明确 registry 来源 | ⚠️ | |",
          "+| §5.5: Llama TF 0.484(TG)/0.481(LO) | llama_eval_s42: 0.4836; eval_llama_lora_only_s42: 0.4807 | ✓ | |",
          "+| \"medians: 0.018(TG,LO), 0.009(Base)\" | eval_llama_ar_n20: 0.0179/0.0184/0.0093 | ✓ | |",
          "+| \"gaps of 27× and 26×\" | 0.484/0.018=26.9≈27; 0.481/0.018=26.7≈27 | ✓ | |",
          "+| \"CoV > 100%\" | eval_llama_ar_n20: CoV=231% | ✓ | |",
          "+| \"Llama SS TF 0.477, AR 0.166\" | p1_llama_ss_eval: 0.477, 0.1662 | ✓ | |",
          "+| \"β=3: Qwen SS 0.593\" | d048_final_ar_eval: beta3.ss=0.593 | ✓ | |",
          "+| \"β=3: Llama SS 0.173\" | 无 registry entry | ❓ | |",
          "+| \"Llama β=5: 0.791\" | p1_llama_ss_eval: 0.7905→0.791 | ✓ | |",
          "+| \"Qwen L1=0.793\" | v7_tg_s123 gate profile: L1=0.793 | ✓ | 来自 s123 非 s42 |",
          "+| \"Llama L25=0.719\" | llama_tg_s42 gate profile: L25=0.719 | ✓ | |",
          "+| \"79.8% GAR decay\" (1.5B) | tab_qwen15b: (0.0336−0.0068)/0.0336=79.8% | ✓ | |",
          "+| \"β-steering to 0.715\" (1.5B) | tab_qwen15b: AR β=5 TG=0.7150 | ✓ | |",
          " ",
          " ### Discussion",
          " ",
          "-| # | 数字 | 上下文 | 来源 | 状态 | 备注 |",
          "-|---|------|--------|------|------|------|",
          "-| 152 | ≤1.3× | \"GAR-Dongre shift ≤1.3×\" | Qwen 1.28×, Llama 1.002× | ✅ | |",
          "-| 153 | r=0.743 | \"per-head correlation r=0.743\" | tab:kl-perhead: Corr(TF_GAR, Delta-GAR) TG=0.743 | ✅ | |",
          "-| 154 | 7.5–25.7× | \"NTP dominance 7.5–25.7×\" | Qwen: 7.5–14.7×, Llama: 25.7× | ✅ | |",
          "-| 155 | r=0.200 | \"GAR-compliance r=0.200\" | same as #27 | ✅ | |",
          "-| 156 | β=5 | \"At β=5 the two converge\" | | ✅ | |",
          "-| 157 | SS=0.717 | \"SS = 0.717\" | tab:perseed-ss β=5 mean | ✅ | |",
          "-| 158 | TG=0.727 | \"TG = 0.727\" | gen_n50: beta_5.0 mid_gar=0.7271 | ✅ | |",
          "+| 数字/声明 | Registry 来源 | 状态 | 备注 |",
          "+|-----------|-------------|------|------|",
          "+| \"≤1.3×\" (GAR-Dongre shift) | analysis §5.4: Qwen 1.28× | ✓ | |",
          "+| \"r=0.743\" (per-head analysis) | 无直接 registry match | ❓ | p1_tf_ar_kl_divergence gate_kl_correlation=0.11 不匹配 |",
          "+| \"r=0.200\" (GAR–compliance) | instruction_retention_test: 0.2003 | ✓ | |",
          "+| \"7.5–25.7× NTP dominance\" | analysis_gradient_conflict + p2_llama_gradient_conflict | ✓ | |",
          "+| \"SS=0.717 vs TG=0.727\" (β=5) | d048_final_ar_eval | ✓ | |",
          " ",
          " ### Conclusion",
          " ",
          "-| # | 数字 | 上下文 | 来源 | 状态 | 备注 |",
          "-|---|------|--------|------|------|------|",
          "-| 159 | GAR=0.50 | \"converge under TF (GAR=0.50)\" | multiple sources | ✅ | |",
          "-| 160 | order of magnitude | \"collapse by an order of magnitude\" | 8–27× gap | ✅ | |",
          "-| 161 | two architectures | \"two architectures\" | Qwen + Llama | ✅ | |",
          "-| 162 | ~1.3× | \"~1.3× (Qwen)\" | same as #16 | ✅ | |",
          "-| 163 | ~2.9× | \"~2.9× (Llama)\" | same as #18 | ✅ | |",
          "+| 数字/声明 | Registry 来源 | 状态 | 备注 |",
          "+|-----------|-------------|------|------|",
          "+| \"GAR=0.50\" (TF) | 多处 | ✓ | |",
          "+| \"order of magnitude\" | 同 Abstract | ✓ | |",
          "+| \"~1.3× (Qwen)\" | 同 §4.4 | ⚠️ | 实际 1.24× |",
          "+| \"~2.9× (Llama)\" | p1_llama_ss_eval: 2.87× | ✓ | |",
          " ",
          "+### Related Work",
          "+",
          "+| 数字/声明 | Registry 来源 | 状态 | 备注 |",
          "+|-----------|-------------|------|------|",
          "+| \"27–48% across 12 models\" | N/A | 文献引用 | Dongre et al. |",
          "+| \"70.8% decline on Qwen-2.5-7B\" | phase1_gar_diag: 0.708 | ✓ | |",
          "+| \"MMLU +2.03 at 15B\" | N/A | 文献引用 | Qiu et al. |",
          "+",
          " ### Limitations",
          " ",
          "-| # | 数字 | 上下文 | 来源 | 状态 | 备注 |",
          "-|---|------|--------|------|------|------|",
          "-| 164 | two model families | \"two model families\" | Qwen + Llama | ✅ | |",
          "-| 165 | Qwen-2.5-7B | model name | external | ✅ | |",
          "-| 166 | Llama-3.1-8B | model name | external | ✅ | |",
          "-| 167 | 8K conversations | \"8K conversations\" | same as #51 | ✅ | |",
          "-| 168 | three seeds | \"three seeds\" (SS) | seeds 42, 123, 456 | ✅ | |",
          "+| 数字/声明 | Registry 来源 | 状态 | 备注 |",
          "+|-----------|-------------|------|------|",
          "+| \"8K conversations\" | tab_dataset_stats | ✓ | |",
          "+| \"three seeds\" (SS) | d048_ss_s42/s123/s456 | ✓ | |",
          "+| \"τ=0.5\" | method 定义 | ✓ | |",
          " ",
          " ---",
          " ",
          "-## 问题清单",
          "+## 跨章节一致性检查",
          " ",
          "-### 重大问题（影响论文可信度）",
          "+| 关键数字 | Abstract | Intro | Experiments | Analysis | Discussion | Conclusion | 一致? |",
          "+|----------|----------|-------|-------------|----------|------------|------------|------|",
          "+| TF GAR ≈ 0.50 | ✓ (implied) | — | 0.49–0.51 | — | — | 0.50 | ✓ |",
          "+| AR collapse \"order of magnitude\" | ✓ | 8–17× | 8–17× | — | ✓ | ✓ | ✓ |",
          "+| Gap 7.8× (TG) | — | 7.8× | 7.8× | — | — | — | ✓ |",
          "+| ~1.3× SS gap (Qwen) | \"near parity\" | ~1.3× | ~1.3× | ~1.3× | — | ~1.3× | ✓ (各处一致，但均偏高) |",
          "+| ~2.9× SS gap (Llama) | — | — | 2.9× | 2.9× | — | ~2.9× | ✓ |",
          "+| p=0.002 (PCGrad) | — | 0.002 | — | 0.002 | — | — | ✓ |",
          "+| 0.064 (TG AR) | — | — | 0.064 | 0.064 | — | — | ✓ |",
          "+| 0.727 (TG β=5) | — | — | 0.727 | — | 0.727 | — | ✓ |",
          "+| 0.717 (SS β=5) | — | — | 0.717 | — | 0.717 | — | ✓ |",
          "+| 70%/70.8% decline | — | \"over 70%\" | — | — | — | — | ✓ vs RW 70.8% |",
          "+| r=0.200 | — | — | — | — | 0.200 | — | ✓ vs Method 0.200 |",
          " ",
          "-**1. [Experiments §4.4] TF GAR 0.498±0.004 — 与 per-seed 数据矛盾**",
          "+**所有跨章节数字内部一致，无矛盾。**",
          " ",
          "-- 论文原文: \"TF GAR 0.498±0.004\"",
          "-- Per-seed 表 (tab:perseed-ss): s42=0.502, s123=0.554, s456=0.496 → mean=0.517, std=0.032",
          "-- 不一致来源推测: 0.498 可能来自旧版 SS 实验 (eval_v8b_ss: iid_gar_ours=0.4983≈0.498)，或仅用 s42+s456 两个种子 (mean=0.499≈0.498, std=0.004)。无论哪种，与 \"across three seeds\" 的表述矛盾。",
          "-- 影响: gap ratio 计算受影响，但 ~1.3× 的定性结论不变 (0.517/0.401=1.29 vs 0.498/0.401=1.24)",
          "-- **建议**: 更新为 per-seed 表一致值。若 s123 TF GAR 异常高 (0.554)，应解释原因（N_tf=200 vs 其他种子 N_tf=50）",
          "+---",
          " ",
          "-**2. [Introduction / Figure 1] Figure 1(c) Llama TG gap 与 caption/正文不一致**",
          "+## 问题清单",
          " ",
          "-- Figure 1(c) 脚本 (gen_fig1_3panel.py): Llama TG gap = **12.5×** (mean-based: TF 0.484 / AR mean 0.039)",
          "-- Figure 1 caption: \"~27× to 2.9× (Llama)\"",
          "-- 正文 Analysis §5.5: \"gaps of 27× and 26×\" (median-based: TF 0.484 / AR median 0.018)",
          "-- Cross-model figure (gen_fig_crossmodel.py): 正确使用 27× (median)",
          "-- **不一致**: Figure 1(c) 柱状图显示 12.5× 但 caption 标注 ~27×。读者看到的图与 caption 矛盾。",
          "-- **建议**: 统一使用 median (27×) 或在 Figure 1(c) 中也用 median。需更新 gen_fig1_3panel.py 中 `gaps_c = [7.8, 1.3, 12.5, 2.9]` 的 12.5 为 27，同时调整 x 轴范围。",
          "+### ISSUE-1 [MAJOR]: Table 1 IID 列数据与 Registry 不匹配",
          "+- **位置**: related_work.tex Table 1, IID (TF) 列",
          "+- **描述**: Table 1 IID 列显示 TG GAR-O=0.50, LO GAR-O=0.50, PPL=2.78。Registry `phase2_4way_eval`（IID eval）记录 TG=0.4866（→0.49）, LO=0.4860（→0.49）, PPL=2.63。Held-out eval (`phase2_4way_eval_heldout`) 则为 TG=0.5035→0.50, PPL=2.78，与表中 IID 值匹配。",
          "+- **影响**: 若 IID 列误用了 held-out 数据，则 IID/held-out 对比的有效性被削弱。注意 Base IID PPL=4.23 与 registry 匹配，仅 fine-tuned 模型有差异。PCGrad IID 值来自独立实验 (0.5002, 2.78) 且匹配。",
          "+- **可能原因**: (a) IID eval 已用新协议重跑但 registry 未更新；(b) Table 误用 held-out 数据",
          "+- **建议**: 确认 IID 列数据来源。若为旧 eval 数据，更新 registry；若为 held-out 误用，需修正。",
          " ",
          "-### 中等问题",
          "+### ISSUE-2 [MAJOR]: \"≤1 pp\" 声明应为 \"≤2 pp\"",
          "+- **位置**: experiments.tex §4.2",
          "+- **原文**: \"IID and held-out protocols produce identical rankings (held-out GAR-ours differs by ≤1 pp)\"",
          "+- **实际**: IID→held-out 差异: TG 1.7pp, UG 1.3pp, LO 1.2pp, PCGrad 0pp (基于 registry 精确值)。即使在 Table 1 精度下，UG 从 0.49(IID) 变为 0.51(held-out)=2pp。",
          "+- **建议**: 改为 \"≤2 pp\"。或若指 held-out 内部 variants spread (0.75pp)，需重措辞明确。",
          " ",
          "-**3. [Experiments §4.2] \"held-out GAR-ours differs by ≤1 pp\" — 实际 UG 差异 ~1.3 pp**",
          "+### ISSUE-3 [minor]: ~1.3× SS gap 偏高于多种子均值",
          "+- **位置**: Intro fig caption, Experiments §4.4, Analysis §5.5, Conclusion",
          "+- **描述**: 多种子 gap = TF_mean/AR_mean = 0.499/0.401 = 1.245 ≈ 1.2×。s42 单种子 gap = 1.29×（d048_eval_ss_s42）。Paper 称 \"~1.3×\" 更接近单种子值。",
          "+- **建议**: 若引用多种子均值，改为 \"~1.2×\"；若引用 s42，标注为单种子。",
          " ",
          "-- tab:five-way: UG IID GAR-ours=0.49, Held-out=0.51 (显示差 2 pp)",
          "-- Registry 精确值: phase2_4way_eval_heldout ug=0.5053; IID eval ug 来源不明（可能 ~0.493）",
          "-- 无论如何，差异超过 1 pp",
          "-- **建议**: 改为 \"differs by ≤2 pp\" 或 \"differs by $\\leq$1.3\\,pp\"",
          "+### ISSUE-4 [minor]: SS TF GAR 0.498±0.004 精度偏差",
          "+- **位置**: experiments.tex §4.4",
          "+- **描述**: 三种子 TF GAR: 0.4983, 0.503, 0.4964 → mean=0.4992≈0.499, std=0.0034≈0.003。Paper 称 0.498±0.004。差异小但精度不匹配。",
          "+- **建议**: 修正为 \"0.499±0.003\"。",
          " ",
          "-**4. [Introduction] AUC = 0.98 — 无法从 registry 验证**",
          "+### ISSUE-5 [minor]: Fig 1(a) \"85–90%\" 未区分 base vs fine-tuned",
          "+- **位置**: introduction.tex Fig 1 caption",
          "+- **描述**: Caption 称 \"Goal attention decays 85–90% across turns\"。Base model: 84.7–87.5% 符合。Fine-tuned: 77–81%（Fig 4 已正确标注）。Caption 涵盖范围模糊。",
          "+- **建议**: 明确为 base model 数据或调整为 \"77–87%\"。",
          " ",
          "-- \"residual stream probes confirm that goal information persists (AUC = 0.98)\"",
          "-- Registry 60 个实验中无 probing 实验记录",
          "-- 可能在早期探索中完成但未注册",
          "-- **建议**: 补充 probing 实验到 registry，或在论文中标注来源",
          "+### ISSUE-6 [minor]: Llama SS \"2 vs 3 epochs\" 需确认",
          "+- **位置**: experiments.tex §4.4, analysis.tex §5.5",
          "+- **描述**: Paper 称 Llama SS 训练 \"fewer training epochs (2 vs 3)\"，但 `p1_llama_ss_training` spec 显示 epochs=3。可能实际只完成 2 epoch 或因 checkpoint 选择使用 epoch_1。",
          "+- **建议**: 确认实际 epoch 数并更新 registry 或论文。",
          " ",
          "-**5. [Experiments §4.2] N=50 实际有效 N=39**",
          "+---",
          " ",
          "-- 论文标注 \"N=50\" 用于 AR 生成评估",
          "-- Registry d048_final_ar_eval: n_convs_total=50, n_convs_valid=39 (11 conversations 不满足 ≥3 turns)",
          "-- 统计检验和 CI 基于 39 个有效样本",
          "-- **建议**: 在正文注明有效样本量，如 \"N=50 (39 with ≥3 valid turns)\" 或在附录说明",
          "+## 暂无出处的数字",
          " ",
          "-**6. [Analysis §5.5] Llama SS β=3 = 0.173 — 无 registry 对应记录**",
          "+| 数字 | 位置 | 原因 |",
          "+|------|------|------|",
          "+| p=0.002 (TG vs PCGrad Wilcoxon) | Intro contribution 2, Analysis §5.2 | 无 registry entry；来自统计检验脚本 |",
          "+| p=0.004 (TG vs LO Wilcoxon) | Experiments §4.2 | 同上 |",
          "+| r=0.743 (per-head TF GAR vs AR shift) | Discussion | p1_tf_ar_kl_divergence 中 gate_kl_correlation=0.11 不匹配 |",
          "+| 27/28 layers gate inversion | Analysis §5.1 | gate 分析脚本，非 registry |",
          "+| Wilcoxon p=3.73×10⁻⁸, r=0.975 | Analysis §5.1 | 同上 |",
          "+| Layer 23: 0.769→0.979 | Analysis §5.1 | 同上 |",
          "+| Llama SS β=3 GAR=0.173 | Analysis §5.5 | p1_llama_ss_eval 仅有 β=0 和 β=5 |",
          "+| Qwen GAR-Dongre 1.28× | Analysis §5.4 | 无直接 registry 来源 |",
          "+| \"mean 3.6 user turns\" | Table 1 caption | eval 数据统计 |",
          "+| 95% CI 边界值 | Table 1 | bootstrap 输出 |",
          "+| Pilot gaps \"20–34×\" | Fig 3(b) caption | N=5 pilot eval |",
          "+| \"mid-turn GAR above 0.36\" | §4.4 | tab_gar_robustness 可交叉验证 |",
          "+| AUC=0.98 | Intro | 文献引用 (Dongre 2026) |",
          "+| \"27–48% across 12 models\" | Related Work | 文献引用 (Dongre 2026) |",
          "+| \"MMLU +2.03 at 15B\" | Related Work | 文献引用 (Qiu 2025) |",
          " ",
          "-- tab:llama-ss-steering 表中有 β=3 AR GAR=0.173",
          "-- p1_llama_ss_eval registry 仅记录 β=0 (0.166) 和 β=5 (0.791)",
          "-- β=3 数据的具体来源不可追溯",
          "-- **建议**: 将 β=3 评估结果补充到 registry",
          "+**建议**: 为 p 值 (0.002, 0.004) 和相关系数 (r=0.743) 补充 registry entry `tab_statistical_tests`，提高可追溯性。",
          " ",
          "-### 轻微问题",
          "-",
          "-**7. [Experiments §4.4] PPL std 0.001 应为 0.002**",
          "-",
          "-- Per-seed PPL: [1.442, 1.441, 1.439], std=0.0016 ≈ 0.002",
          "-- 论文写 ±0.001",
          "-- 影响可忽略",
          "-",
          "-**8. [Figure 3b title] \"20–33×\" 实际范围为 20–34×**",
          "-",
          "-- gen_fig3_gate_shift.py panel (b): UG gap = 0.5053/0.0149 = 33.9× → 应取 34",
          "-- 影响极小：图标题而非正文数据",
          "-",
          "-**9. [Figure gen_fig_ss_multiseed.py] β=5 s456 值 0.718 vs registry 0.716**",
          "-",
          "-- 脚本硬编码 seeds_b5 = [0.716, 0.717, 0.718]",
          "-- Registry d048_eval_ss_s456: ar_beta5_gar=0.7157 → 四舍五入应为 0.716",
          "-- 脚本中 s456 用了 0.718，与 registry 0.7157 不符（差 0.002）",
          "-- 不影响均值（0.717）和 std（0.001）",
          "-",
          " ---",
          " ",
          "-## 交叉一致性检查",
          "+## MMLU 详细验证 (tab_mmlu_detail.tex)",
          " ",
          "-### 跨章节引用一致性",
          "+| 指标 | 表中值 | Registry (mmlu_eval_all) | 匹配? |",
          "+|------|--------|-------------------------|------|",
          "+| Base Overall | 74.23% | 0.7423 | ✓ |",
          "+| TG Overall | 73.47% | 0.7347 | ✓ |",
          "+| PCGrad Overall | 73.86% | 0.7386 | ✓ |",
          "+| SS Overall | 73.75% | 0.7375 | ✓ |",
          "+| LoRA-only Overall | 73.57% | 0.7357 | ✓ |",
          "+| UG Overall | 73.46% | 0.7346 | ✓ |",
          "+| Max Δ | −0.77pp | 74.23−73.46=0.77 | ✓ |",
          "+| \"within 0.8 pp\" | 0.77 ≤ 0.8 | | ✓ |",
          " ",
          "-| 数字 | 出现位置 | 一致性 |",
          "-|------|----------|--------|",
          "-| 7.8× (TG gap) | Abstract, Intro, Experiments, Analysis, Conclusion, Fig 1 | ✅ 全部一致 |",
          "-| ~1.3× (Qwen SS) | Abstract, Intro, Experiments, Conclusion, Fig caption | ✅ 全部一致 |",
          "-| ~2.9× (Llama SS) | Abstract, Intro, Experiments, Analysis, Conclusion | ✅ 全部一致 |",
          "-| 8–17× (gap range) | Intro, Experiments, Analysis Fig 3 caption | ✅ 全部一致 |",
          "-| p=0.002 (PCGrad) | Intro (contribution), Analysis, stat-tests | ✅ 全部一致 |",
          "-| ~27× (Llama TG) | Intro, Analysis text, crossmodel figure | ✅ 文本一致 |",
          "-| ~27× (Llama TG) | Figure 1(c) script | ❌ **图中用 12.5× (mean)，与文本 27× (median) 不一致** |",
          "-| 0.498 (SS TF GAR) | Experiments text, tab:llama-vs-qwen-ss, tab:crossmodel-detail | ✅ 文本/表格一致 |",
          "-| 0.498 (SS TF GAR) | tab:perseed-ss | ❌ **per-seed 表显示 0.517±0.032** |",
          "+## GAR Robustness 验证 (tab_gar_robustness.tex)",
          " ",
          "-### 图表脚本 vs Registry 一致性",
          "+- SS mid-turn GAR >0.36 for all strategies ✓ (Last: 0.458, All: 0.366, First: 0.412, Goal: 0.444)",
          "+- §4.4 \"mid-turn GAR above 0.36 for all token-position variants\" 与表一致 ✓",
          " ",
          "-| 图表 | 脚本数据 | Registry 来源 | 一致性 |",
          "-|------|----------|---------------|--------|",
          "-| Fig 1(a) Qwen per-turn | gen_fig1_3panel: 10 values | phase1_gar_diag: per_turn_avg_gar | ✅ 完全匹配 |",
          "-| Fig 1(a) Llama per-turn | gen_fig1_3panel: 10 values | llama_phase1_gar_diag: per_turn_gar | ✅ 完全匹配 |",
          "-| Fig 1(b) TF/AR bars | gen_fig1_3panel: 5 configs | d048_final_ar_eval + phase2_4way_eval_heldout | ✅ 完全匹配 |",
          "-| Fig 1(c) SS gaps | gen_fig1_3panel: 4 bars | mixed: Qwen ✅, Llama TG ⚠️ uses mean not median | ⚠️ 见问题 #2 |",
          "-| Fig 3(a) gate values | gen_fig3_gate_shift: 5 layers × 2 turns | 无直接 registry 记录（需 WandB 验证） | ⚠️ 需验证 |",
          "-| Fig 3(b) pilot gaps | gen_fig3_gate_shift: 5 configs | phase2_tg_s42_v7 + 其他 eval_modelgen | ✅ 匹配 |",
          "-| Fig 4 decay curves | gen_fig4: 4 configs | analysis_attention_heatmap | ✅ 匹配 |",
          "-| Fig 5 steering | gen_fig5: 2 panels | attention_steering_v7_tg_gen + gen_n50 | ✅ 完全匹配 |",
          "-| Crossmodel gates | gen_fig_crossmodel: 28+32 values | v7_tg_s123 + llama_tg_s42 | ✅ 完全匹配 |",
          "-| SS multiseed | gen_fig_ss_multiseed: 6 values | d048_final_ar_eval + d048_eval_ss_s123/s456 | ⚠️ s456 β=5 差 0.002 |",
          "+## Qwen-1.5B 验证 (tab_qwen15b_results.tex)",
          " ",
          "----",
          "-",
          "-## 总结",
          "-",
          "-**审计结论**: 论文主体 168 个数字中，161 个（95.8%）与 registry/脚本完全吻合或在合理四舍五入范围内。发现 2 个重大问题和 4 个中等问题需要修正。",
          "-",
          "-**优先修复**:",
          "-1. 🔴 统一 SS TF GAR 报告值（0.498 vs 0.517）与 per-seed 表",
          "-2. 🔴 修复 Figure 1(c) Llama TG gap（12.5× → 27×）使图文一致",
          "-3. 🟡 修正 \"≤1 pp\" 为 \"≤2 pp\" 或确认精确值",
          "-4. 🟡 补充 AUC=0.98 probing 实验到 registry",
          "-5. 🟡 注明 AR eval 有效 N=39/50",
          "-6. 🟡 补充 Llama SS β=3 评估到 registry",
          "+| 指标 | 表中值 | 验算 | 匹配? |",
          "+|------|--------|------|------|",
          "+| Turn-1 GAR | 0.0336 | — | ✓ |",
          "+| Mid-turn GAR | 0.0068 | — | ✓ |",
          "+| Relative drop | 79.8% | (0.0336−0.0068)/0.0336=79.76% | ✓ |",
          "+| AR β=5 TG | 0.7150 | — | ✓ |",
          "+| p=0.005 (β=0), p<0.001 (β=5) | — | 来自 Wilcoxon 脚本 | ❓ |"
        ]
      }
    ],
    "originalFile": null,
    "userModified": false
  },
  "sourceToolAssistantUUID": "a164d471-ccb5-4bfc-942d-1a34b38faf07",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "4b680861-4da7-411a-8744-3dabfdaf2205",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Runtime record

_source line 116_

```json
{
  "type": "last-prompt",
  "leafUuid": "b96d5eed-97b8-44bb-a0f3-fd4f99b28d25",
  "sessionId": "4b680861-4da7-411a-8744-3dabfdaf2205"
}
```

---

### Runtime record

_source line 117_

```json
{
  "type": "ai-title",
  "aiTitle": "Audit quantitative claims in paper body text",
  "sessionId": "4b680861-4da7-411a-8744-3dabfdaf2205"
}
```

---

### Assistant

_source line 118 · 2026-05-25T20:56:58.075Z_

Now let me register this artifact.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b96d5eed-97b8-44bb-a0f3-fd4f99b28d25",
  "isSidechain": false,
  "requestId": "req_011CbPxPBHipWr8BshAwwLCM",
  "type": "assistant",
  "uuid": "129b2889-b0fc-4b7d-8749-b9845cd6e25e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "4b680861-4da7-411a-8744-3dabfdaf2205",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LP8VEvrMuFWoh5bAR2BYQ9",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8636,
      "cache_read_input_tokens": 119520,
      "output_tokens": 93,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 8636,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 93,
          "cache_read_input_tokens": 119520,
          "cache_creation_input_tokens": 8636,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 8636
          },
          "type": "message"
        }
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

_source line 119 · 2026-05-25T20:56:58.678Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01HE2NS3SThvyvkxLRTvPTNZ`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__register_artifact",
  "max_results": 1
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "129b2889-b0fc-4b7d-8749-b9845cd6e25e",
  "isSidechain": false,
  "requestId": "req_011CbPxPBHipWr8BshAwwLCM",
  "type": "assistant",
  "uuid": "2a3930a1-6c62-4d00-a641-fc20d53a1dcb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "4b680861-4da7-411a-8744-3dabfdaf2205",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LP8VEvrMuFWoh5bAR2BYQ9",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8636,
      "cache_read_input_tokens": 119520,
      "output_tokens": 93,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 8636,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 93,
          "cache_read_input_tokens": 119520,
          "cache_creation_input_tokens": 8636,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 8636
          },
          "type": "message"
        }
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

_source line 120 · 2026-05-25T20:56:58.681Z_

<details><summary>↩ Tool result · `toolu_01HE2NS3SThvyvkxLRTvPTNZ`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__register_artifact"
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2a3930a1-6c62-4d00-a641-fc20d53a1dcb",
  "isSidechain": false,
  "promptId": "8817af8a-f189-44e8-a462-1453a12b4ea3",
  "type": "user",
  "uuid": "5ab0fd83-6c45-431e-b7b1-1ef2c03e91fc",
  "toolUseResult": {
    "matches": [
      "mcp__agent-ml-research__register_artifact"
    ],
    "query": "select:mcp__agent-ml-research__register_artifact",
    "total_deferred_tools": 25
  },
  "sourceToolAssistantUUID": "2a3930a1-6c62-4d00-a641-fc20d53a1dcb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "4b680861-4da7-411a-8744-3dabfdaf2205",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 121 · 2026-05-25T20:57:15.334Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact · `toolu_0169BKHuhcu6dyZF9ZvLEe3S`</summary>

```json
{
  "name": "audit_body_text",
  "type": "report",
  "description": "正文数据审计报告：逐章节验证~160个定量claim，发现2个major + 4个minor问题",
  "project": "turn_residual_gating",
  "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/audit_body_text.md",
  "tags": [
    "audit",
    "paper",
    "data-verification"
  ]
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5ab0fd83-6c45-431e-b7b1-1ef2c03e91fc",
  "isSidechain": false,
  "requestId": "req_011CbPxPTLNTxezRZSYXL9Ny",
  "type": "assistant",
  "uuid": "bb2f906e-899a-4ac5-b325-80644a743ba0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "4b680861-4da7-411a-8744-3dabfdaf2205",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0163i69DMuhvund67C8vY4dM",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 720,
      "cache_read_input_tokens": 128156,
      "output_tokens": 241,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 720,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 241,
          "cache_read_input_tokens": 128156,
          "cache_creation_input_tokens": 720,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 720
          },
          "type": "message"
        }
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

_source line 122 · 2026-05-25T20:57:15.462Z_

<details><summary>↩ Tool result · `toolu_0169BKHuhcu6dyZF9ZvLEe3S`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260525_4e2102\", \"name\": \"audit_body_text\", \"type\": \"report\", \"description\": \"正文数据审计报告：逐章节验证~160个定量claim，发现2个major + 4个minor问题\", \"path\": \"projects/turn_residual_gating/artifacts/_project/report/audit_body_text.md\", \"url\": null, \"project\": \"turn_residual_gating\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-25T20:57:15.339629+00:00\", \"tags\": [\"audit\", \"paper\", \"data-verification\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bb2f906e-899a-4ac5-b325-80644a743ba0",
  "isSidechain": false,
  "promptId": "8817af8a-f189-44e8-a462-1453a12b4ea3",
  "type": "user",
  "uuid": "2e6fcf13-0a23-4996-8b80-0934808d0027",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"artifact\\\": {\\\"id\\\": \\\"art_20260525_4e2102\\\", \\\"name\\\": \\\"audit_body_text\\\", \\\"type\\\": \\\"report\\\", \\\"description\\\": \\\"正文数据审计报告：逐章节验证~160个定量claim，发现2个major + 4个minor问题\\\", \\\"path\\\": \\\"projects/turn_residual_gating/artifacts/_project/report/audit_body_text.md\\\", \\\"url\\\": null, \\\"project\\\": \\\"turn_residual_gating\\\", \\\"exp_id\\\": null, \\\"skill\\\": \\\"\\\", \\\"created_at\\\": \\\"2026-05-25T20:57:15.339629+00:00\\\", \\\"tags\\\": [\\\"audit\\\", \\\"paper\\\", \\\"data-verification\\\"]}, \\\"manifest\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/manifest.yaml\\\"}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260525_4e2102\", \"name\": \"audit_body_text\", \"type\": \"report\", \"description\": \"正文数据审计报告：逐章节验证~160个定量claim，发现2个major + 4个minor问题\", \"path\": \"projects/turn_residual_gating/artifacts/_project/report/audit_body_text.md\", \"url\": null, \"project\": \"turn_residual_gating\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-25T20:57:15.339629+00:00\", \"tags\": [\"audit\", \"paper\", \"data-verification\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"
    }
  },
  "sourceToolAssistantUUID": "bb2f906e-899a-4ac5-b325-80644a743ba0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "4b680861-4da7-411a-8744-3dabfdaf2205",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 123 · 2026-05-25T20:57:35.828Z_

审计完成。报告已写入 `artifacts/audit_body_text.md`。

**核心发现：~160 个定量声明中，~135 个与 Registry 一致，6 个问题（2 major + 4 minor），19 个需独立验证。**

### 2 个 Major 问题

1. **Table 1 IID 列数据存疑** — TG/LO 的 IID GAR-O 显示 0.50，但 Registry `phase2_4way_eval` 记录为 0.4866/0.4860（应舍入为 0.49）。IID PPL 显示 2.78 但 Registry 记录为 2.62–2.63（held-out 值为 2.78）。疑似 IID 列误用了 held-out 数据，或 IID eval 已重跑但 Registry 未更新。

2. **"≤1 pp" 应为 "≤2 pp"** — experiments.tex 称 "held-out GAR-ours differs by ≤1 pp"，实际各变体 IID→held-out 最大差异 1.7pp（TG），Table 精度下 UG 差 2pp。

### 4 个 Minor 问题

3. **~1.3× SS gap 偏高** — 多种子均值 gap = 1.245 ≈ 1.2×，非 ~1.3×（s42 单种子 1.29×）
4. **SS TF GAR 0.498±0.004** — 实际 0.499±0.003
5. **Fig 1 caption "85–90%" 未区分 base vs fine-tuned** — fine-tuned 仅 77–81%
6. **Llama SS "2 vs 3 epochs"** — Registry spec 写 epochs=3，需确认实际

### 跨章节一致性

所有跨章节出现的数字（~1.3×、7.8×、0.064、0.727、0.717 等）**内部完全一致**，无矛盾。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2e6fcf13-0a23-4996-8b80-0934808d0027",
  "isSidechain": false,
  "requestId": "req_011CbPxQgeqfvx7xYmqxDK8y",
  "type": "assistant",
  "uuid": "2c03befb-795b-48ff-a674-d04a0590322d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "4b680861-4da7-411a-8744-3dabfdaf2205",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UUyW8gzQRyk61yVPrhnw1Y",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 520,
      "cache_read_input_tokens": 128876,
      "output_tokens": 572,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 520,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 572,
          "cache_read_input_tokens": 128876,
          "cache_creation_input_tokens": 520,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 520
          },
          "type": "message"
        }
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

_source line 124_

```json
{
  "type": "last-prompt",
  "leafUuid": "2c03befb-795b-48ff-a674-d04a0590322d",
  "sessionId": "4b680861-4da7-411a-8744-3dabfdaf2205"
}
```

---

### Runtime record

_source line 125_

```json
{
  "type": "ai-title",
  "aiTitle": "Audit quantitative claims in paper body text",
  "sessionId": "4b680861-4da7-411a-8744-3dabfdaf2205"
}
```

---
