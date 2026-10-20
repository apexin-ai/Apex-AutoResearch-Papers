# Research conversation: <project_context> # 项目: phase-gated-compound-sparse ## 运行环境 - 服务器名: westd-22162 - SSH 账户: root（调用 ssh_execute / submit_t

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 76
- **Recorded user turns:** 5
- **Tool calls:** 12
- **Original source:** `logs/chats/exported-trajectories/account-3/38576691-e177-4a18-ab23-be69eff4b7ff.jsonl`
- **Structured JSON:** [`850be983c43891382a96.json`](../../sessions/85/850be983c43891382a96.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-16T00:25:40.262Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-16T00:25:40.262Z",
  "sessionId": "38576691-e177-4a18-ab23-be69eff4b7ff",
  "content": "&lt;project_context>\n# 项目: phase-gated-compound-sparse\n\n## 运行环境\n- 服务器名: westd-22162\n- SSH 账户: root（调用 ssh_execute / submit_training_job 时传入 account=\"root\"）\n- SSH 连接命令: ssh connect.westd.seetacloud.com  # 必须用此命令，~/.ssh/config 自动应用密钥和跳板机，禁止用裸 IP\n- 项目代码根目录: /root/autodl-tmp/pacs\n\n\n## 环境搭建\n连接服务器后先调 `detect_image` 检测是否为预置镜像。如果匹配，跳过基础环境搭建，只装项目特有依赖。已预装的包不要重复安装。\n\n## 输出风格\n回复简洁直接。只输出执行结果和必要信息，不要解释过程、不要客套、不要给未被要求的建议。\n&lt;/project_context>\n## 任务：Round 10 数据编译 — 汇总所有实验证据\n\n### 背景\nEMNLP 2026 ARR 截稿 2026-05-25（10 天后）。项目 \"phase-gated-compound-sparse\" 的核心论点是：importance-based eviction 的 compound interaction severity 随 sparsity 单调递增。需要编译所有完成的实验证据，供 Round 10 审稿和论文整合。\n\n### 需要编译的数据维度\n\n**1. PPL Dose Curve (n=500, DS + QW)**\n- 从 registry 读取所有 PPL 相关实验（v6_* 和 bf16_* 系列）的 metrics\n- 关键指标：每个 sparsity 水平的 median II, Wilcoxon p-value, effect size\n\n**2. QW Accuracy Dose Curve (n=100)**\n- 从 registry 读取: acc_qw_dense_n100, acc_qw_s015_n100, acc_qw_s020_n100(_b2_fix), acc_qw_s025_n100(_b2_fix), acc_qw_s030_n100\n- 整理 combined accuracy 和 truncation rate\n\n**3. DS Accuracy (8k v2, 定性观察)**\n- 从 registry 读取: acc_ds_dense_8k_v2, acc_ds_s020_8k_v2, acc_ds_s025_8k_v2\n- 标注 truncation rate caveat（D086: 降为定性观察）\n- acc_ds_s015_8k_v2 和 acc_ds_s030_8k_v2 仍在运行，标记 \"pending\"\n\n**4. GSM8K Compound Interaction (C10)**\n- 从 registry 读取: gsm8k_qw_rand_s025_v2, gsm8k_qw_rand_s030_v2\n- 关键指标：verdict, II dose-response\n\n**5. Additional Evidence**\n- sf5 asymmetric sparsity\n- Appendix B G× 修正值 (21-64×)\n- Cross-model Mann-Whitney U results (n=475 reanalysis)\n\n### 产出\n将编译结果写入项目文件：用 `save_project_file` 保存为 `round10_data_summary.md`，包含：\n1. 每个证据维度的表格（指标 + exp_id 来源）\n2. 核心 claim 对应的证据映射\n3. 已知 caveat 列表\n4. 仍缺失/待确认的数据点\n\n### 工具\n- 用 read_registry 获取实验数据\n- 用 read_project_file 读取 memory.md 和 paper_framing.md 了解 claim 结构\n- 用 save_project_file 保存产出"
}
```

---

### Runtime record

_source line 2 · 2026-05-16T00:25:40.266Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-16T00:25:40.266Z",
  "sessionId": "38576691-e177-4a18-ab23-be69eff4b7ff"
}
```

---

## Round 1

34 recorded events

### User

_source line 3 · 2026-05-16T00:25:40.318Z_

&lt;project_context>
# 项目: phase-gated-compound-sparse

## 运行环境
- 服务器名: westd-22162
- SSH 账户: root（调用 ssh_execute / submit_training_job 时传入 account="root"）
- SSH 连接命令: ssh connect.westd.seetacloud.com  # 必须用此命令，~/.ssh/config 自动应用密钥和跳板机，禁止用裸 IP
- 项目代码根目录: /root/autodl-tmp/pacs


## 环境搭建
连接服务器后先调 `detect_image` 检测是否为预置镜像。如果匹配，跳过基础环境搭建，只装项目特有依赖。已预装的包不要重复安装。

## 输出风格
回复简洁直接。只输出执行结果和必要信息，不要解释过程、不要客套、不要给未被要求的建议。
&lt;/project_context>
## 任务：Round 10 数据编译 — 汇总所有实验证据

### 背景
EMNLP 2026 ARR 截稿 2026-05-25（10 天后）。项目 "phase-gated-compound-sparse" 的核心论点是：importance-based eviction 的 compound interaction severity 随 sparsity 单调递增。需要编译所有完成的实验证据，供 Round 10 审稿和论文整合。

### 需要编译的数据维度

**1. PPL Dose Curve (n=500, DS + QW)**
- 从 registry 读取所有 PPL 相关实验（v6_* 和 bf16_* 系列）的 metrics
- 关键指标：每个 sparsity 水平的 median II, Wilcoxon p-value, effect size

**2. QW Accuracy Dose Curve (n=100)**
- 从 registry 读取: acc_qw_dense_n100, acc_qw_s015_n100, acc_qw_s020_n100(_b2_fix), acc_qw_s025_n100(_b2_fix), acc_qw_s030_n100
- 整理 combined accuracy 和 truncation rate

**3. DS Accuracy (8k v2, 定性观察)**
- 从 registry 读取: acc_ds_dense_8k_v2, acc_ds_s020_8k_v2, acc_ds_s025_8k_v2
- 标注 truncation rate caveat（D086: 降为定性观察）
- acc_ds_s015_8k_v2 和 acc_ds_s030_8k_v2 仍在运行，标记 "pending"

**4. GSM8K Compound Interaction (C10)**
- 从 registry 读取: gsm8k_qw_rand_s025_v2, gsm8k_qw_rand_s030_v2
- 关键指标：verdict, II dose-response

**5. Additional Evidence**
- sf5 asymmetric sparsity
- Appendix B G× 修正值 (21-64×)
- Cross-model Mann-Whitney U results (n=475 reanalysis)

### 产出
将编译结果写入项目文件：用 `save_project_file` 保存为 `round10_data_summary.md`，包含：
1. 每个证据维度的表格（指标 + exp_id 来源）
2. 核心 claim 对应的证据映射
3. 已知 caveat 列表
4. 仍缺失/待确认的数据点

### 工具
- 用 read_registry 获取实验数据
- 用 read_project_file 读取 memory.md 和 paper_framing.md 了解 claim 结构
- 用 save_project_file 保存产出

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "5d98afa4-bc8d-47c1-b014-8bbe0580361f",
  "type": "user",
  "uuid": "791a0c86-7d44-4ac7-afd1-29fcb0da0bd3",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "sessionId": "38576691-e177-4a18-ab23-be69eff4b7ff",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-16T00:25:40.317Z_

```json
{
  "parentUuid": "791a0c86-7d44-4ac7-afd1-29fcb0da0bd3",
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
  "uuid": "b2a75161-000c-4e71-8024-ddd2aa7858ec",
  "timestamp": "2026-05-16T00:25:40.317Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "sessionId": "38576691-e177-4a18-ab23-be69eff4b7ff",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-16T00:25:40.317Z_

```json
{
  "parentUuid": "b2a75161-000c-4e71-8024-ddd2aa7858ec",
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
  "uuid": "d992f48a-f981-4e0e-9148-33533fcafb84",
  "timestamp": "2026-05-16T00:25:40.317Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "sessionId": "38576691-e177-4a18-ab23-be69eff4b7ff",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 6 · 2026-05-16T00:25:40.317Z_

```json
{
  "parentUuid": "d992f48a-f981-4e0e-9148-33533fcafb84",
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
  "uuid": "a54f6cbf-669b-4054-a4af-13b5a5c892ef",
  "timestamp": "2026-05-16T00:25:40.317Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "sessionId": "38576691-e177-4a18-ab23-be69eff4b7ff",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 7 · 2026-05-16T00:25:40.318Z_

```json
{
  "parentUuid": "a54f6cbf-669b-4054-a4af-13b5a5c892ef",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "a1a4060d-63d4-473d-8292-c5bd9f97fd96",
  "timestamp": "2026-05-16T00:25:40.318Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "sessionId": "38576691-e177-4a18-ab23-be69eff4b7ff",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 8_

```json
{
  "type": "ai-title",
  "aiTitle": "Compile Round 10 experiment evidence for ARR submission",
  "sessionId": "38576691-e177-4a18-ab23-be69eff4b7ff"
}
```

---

### Assistant

_source line 9 · 2026-05-16T00:25:43.290Z_

I'll compile all experimental evidence for Round 10. Let me start by reading the registry and project files in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a1a4060d-63d4-473d-8292-c5bd9f97fd96",
  "isSidechain": false,
  "requestId": "req_011Cb5JDKNs15nmCRUq8Ms9P",
  "type": "assistant",
  "uuid": "3eb47905-90d9-4346-a929-a52c456a34c5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "sessionId": "38576691-e177-4a18-ab23-be69eff4b7ff",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Qv5U6XPPdoHFFHL54497fA",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11996,
      "cache_read_input_tokens": 11447,
      "output_tokens": 141,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11996,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 141,
          "cache_read_input_tokens": 11447,
          "cache_creation_input_tokens": 11996,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11996
          },
          "type": "message"
        }
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

_source line 10 · 2026-05-16T00:25:43.784Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01DjRHx4TvxwsVNSCe6ceS9C`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_registry,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__save_project_file",
  "max_results": 3
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3eb47905-90d9-4346-a929-a52c456a34c5",
  "isSidechain": false,
  "requestId": "req_011Cb5JDKNs15nmCRUq8Ms9P",
  "type": "assistant",
  "uuid": "6ba2a49a-e8da-4f5e-ac92-256e0743b3da",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "sessionId": "38576691-e177-4a18-ab23-be69eff4b7ff",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Qv5U6XPPdoHFFHL54497fA",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11996,
      "cache_read_input_tokens": 11447,
      "output_tokens": 141,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11996,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 141,
          "cache_read_input_tokens": 11447,
          "cache_creation_input_tokens": 11996,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11996
          },
          "type": "message"
        }
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

_source line 11 · 2026-05-16T00:25:43.795Z_

<details><summary>↩ Tool result · `toolu_01DjRHx4TvxwsVNSCe6ceS9C`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__read_registry"
}
```

```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__read_project_file"
}
```

```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__save_project_file"
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6ba2a49a-e8da-4f5e-ac92-256e0743b3da",
  "isSidechain": false,
  "promptId": "5d98afa4-bc8d-47c1-b014-8bbe0580361f",
  "type": "user",
  "uuid": "05e1cc3f-57ab-431a-ba55-5a828de95103",
  "toolUseResult": {
    "matches": [
      "mcp__agent-ml-research__read_registry",
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__save_project_file"
    ],
    "query": "select:mcp__agent-ml-research__read_registry,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__save_project_file",
    "total_deferred_tools": 25
  },
  "sourceToolAssistantUUID": "6ba2a49a-e8da-4f5e-ac92-256e0743b3da",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "sessionId": "38576691-e177-4a18-ab23-be69eff4b7ff",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 12 · 2026-05-16T00:25:46.663Z_

<details><summary>Logged reasoning block</summary>

```text
Let me read the registry and project files in parallel to gather all the data I need.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "05e1cc3f-57ab-431a-ba55-5a828de95103",
  "isSidechain": false,
  "requestId": "req_011Cb5JDa78uMR5jDzqqWGX9",
  "type": "assistant",
  "uuid": "334e300e-e63c-4fd4-9f3c-5bd5e98f6c64",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "sessionId": "38576691-e177-4a18-ab23-be69eff4b7ff",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0147BFncuYKAT8NdSsmU8MWf",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1071,
      "cache_read_input_tokens": 23443,
      "output_tokens": 326,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1071,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 326,
          "cache_read_input_tokens": 23443,
          "cache_creation_input_tokens": 1071,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1071
          },
          "type": "message"
        }
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

_source line 13 · 2026-05-16T00:25:47.209Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_01UZvGAPHAysxu1qHBsYkPzk`</summary>

```json
{
  "project": "phase-gated-compound-sparse",
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
  "parentUuid": "334e300e-e63c-4fd4-9f3c-5bd5e98f6c64",
  "isSidechain": false,
  "requestId": "req_011Cb5JDa78uMR5jDzqqWGX9",
  "type": "assistant",
  "uuid": "809e4f6a-ef7f-4382-94e5-13f10a34c64e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "sessionId": "38576691-e177-4a18-ab23-be69eff4b7ff",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0147BFncuYKAT8NdSsmU8MWf",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1071,
      "cache_read_input_tokens": 23443,
      "output_tokens": 326,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1071,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 326,
          "cache_read_input_tokens": 23443,
          "cache_creation_input_tokens": 1071,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1071
          },
          "type": "message"
        }
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

_source line 14 · 2026-05-16T00:25:48.132Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_017Neur95H2nm1TjLddGoxZz`</summary>

```json
{
  "project": "phase-gated-compound-sparse",
  "file": "memory.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "809e4f6a-ef7f-4382-94e5-13f10a34c64e",
  "isSidechain": false,
  "requestId": "req_011Cb5JDa78uMR5jDzqqWGX9",
  "type": "assistant",
  "uuid": "4ee8b54d-2687-4051-9c8f-89a051abec43",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "sessionId": "38576691-e177-4a18-ab23-be69eff4b7ff",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0147BFncuYKAT8NdSsmU8MWf",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1071,
      "cache_read_input_tokens": 23443,
      "output_tokens": 326,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1071,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 326,
          "cache_read_input_tokens": 23443,
          "cache_creation_input_tokens": 1071,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1071
          },
          "type": "message"
        }
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

_source line 15 · 2026-05-16T00:25:48.169Z_

<details><summary>↩ Tool result · `toolu_01UZvGAPHAysxu1qHBsYkPzk`</summary>

```text
Error: result (206,204 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-11-projects-phase-gated-compound-sparse/38576691-e177-4a18-ab23-be69eff4b7ff/tool-results/mcp-agent-ml-research-read_registry-1778891148151.txt.
Format: JSON with schema: {result: string}
- For targeted queries (find a value, filter by field): use jq on the file directly.
- For analysis or summarization that requires reading the full content: first probe the structure (e.g., jq 'type, length, keys?' /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-11-projects-phase-gated-compound-sparse/38576691-e177-4a18-ab23-be69eff4b7ff/tool-results/mcp-agent-ml-research-read_registry-1778891148151.txt), then extract slices with jq or python — Read's line-based offset/limit will not chunk this file.
- If the Agent tool is available, do this inside a subagent so the full output stays out of your main context. Give it the instruction above verbatim, and be explicit about what it must return — e.g. "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-11-projects-phase-gated-compound-sparse/38576691-e177-4a18-ab23-be69eff4b7ff/tool-results/mcp-agent-ml-research-read_registry-1778891148151.txt is JSON with schema: {result: string}; probe the structure with jq (type/length/keys), then extract and read the content in full with jq or python, then summarize and quote any key findings verbatim." A vague "summarize this" may lose detail.

```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "809e4f6a-ef7f-4382-94e5-13f10a34c64e",
  "isSidechain": false,
  "promptId": "5d98afa4-bc8d-47c1-b014-8bbe0580361f",
  "type": "user",
  "uuid": "0362c953-dbf4-46a6-87e8-eb535417298b",
  "toolUseResult": "Error: result (206,204 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-11-projects-phase-gated-compound-sparse/38576691-e177-4a18-ab23-be69eff4b7ff/tool-results/mcp-agent-ml-research-read_registry-1778891148151.txt.\nFormat: JSON with schema: {result: string}\n- For targeted queries (find a value, filter by field): use jq on the file directly.\n- For analysis or summarization that requires reading the full content: first probe the structure (e.g., jq 'type, length, keys?' /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-11-projects-phase-gated-compound-sparse/38576691-e177-4a18-ab23-be69eff4b7ff/tool-results/mcp-agent-ml-research-read_registry-1778891148151.txt), then extract slices with jq or python — Read's line-based offset/limit will not chunk this file.\n- If the Agent tool is available, do this inside a subagent so the full output stays out of your main context. Give it the instruction above verbatim, and be explicit about what it must return — e.g. \"/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-11-projects-phase-gated-compound-sparse/38576691-e177-4a18-ab23-be69eff4b7ff/tool-results/mcp-agent-ml-research-read_registry-1778891148151.txt is JSON with schema: {result: string}; probe the structure with jq (type/length/keys), then extract and read the content in full with jq or python, then summarize and quote any key findings verbatim.\" A vague \"summarize this\" may lose detail.\n",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {\"r9c2-spike-v3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T20:35:35.819Z\", \"updated_at\": \"2026-05-16T00:24:46.524Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/pacs && python run_accuracy_eval.py --num-problems 10 --conditions dense,importance_s025 --gpu cuda:0 --output-name accuracy_eval_r9c2_spike.json 2>&1 | tee /root/autodl-tmp/pacs/analysis_output/spike_log.txt\\\"\", \"server\": \"westd-22162\", \"gpu\": [\"cuda:1\"], \"pid\": \"272763\", \"log_path\": \"~/runs/phase-gated-compound-sparse/r9c2-spike-v3.log\", \"submitted_at\": \"2026-05-15T20:35:35.531Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 3452.4, \"gpu_hours\": 0.96}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-15T21:33:07.954Z\"}, \"r9c2-spike-v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T20:35:10.902Z\", \"updated_at\": \"2026-05-16T00:24:45.793Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/pacs && python run_accuracy_eval.py --num-problems 10 --conditions dense,importance_s025 --gpu cuda:1 --output-name accuracy_eval_r9c2_spike.json 2>&1 | tee /root/autodl-tmp/pacs/analysis_output/spike_log.txt\\\"\", \"server\": \"westd-22162\", \"gpu\": [\"cuda:1\"], \"pid\": \"272599\", \"log_path\": \"~/runs/phase-gated-compound-sparse/r9c2-spike-v2.log\", \"submitted_at\": \"2026-05-15T20:35:10.638Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 3476.0, \"gpu_hours\": 0.97}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-15T21:33:06.644Z\"}, \"r9c2-spike\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T20:34:26.906Z\", \"updated_at\": \"2026-05-16T00:24:45.022Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/pacs && python run_accuracy_eval.py --num-problems 10 --conditions dense,importance_s025 --gpu cuda:1 --output-name accuracy_eval_r9c2_spike.json 2>&1 | tee /root/autodl-tmp/pacs/analysis_output/spike_log.txt\\\"\", \"server\": \"westd-22162\", \"gpu\": [\"cuda:1\"], \"pid\": \"272395\", \"log_path\": \"~/runs/phase-gated-compound-sparse/r9c2-spike.log\", \"submitted_at\": \"2026-05-15T20:34:26.607Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 3518.8, \"gpu_hours\": 0.98}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-15T21:33:05.375Z\"}, \"acc_ds_s025_8k_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T21:35:01.085Z\", \"updated_at\": \"2026-05-16T00:20:39.536Z\", \"hypothesis\": \"DS s025 accuracy eval with max_new_tokens=8192，补全 5-point dose curve。4096 版截断率 76%，8k 目标 <20%。\", \"server\": \"westd-22162\", \"gpu\": \"cuda:3\", \"account\": \"root\", \"reproduce\": {\"server\": \"westd-22162\", \"gpu\": \"cuda:3\", \"started_at\": \"2026-05-15T22:21:32.499Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/pacs && python run_accuracy_eval.py --model checkpoints/DeepSeek-R1-Distill-Qwen-7B --conditions importance_s025 --num-problems 50 --max-new-tokens 8192 --output-name accuracy_ds_s025_8k_v2.json --gpu cuda:0\\\"\", \"code_commit\": \"1b4f61aa366a9fe320f8563c8f7acb5af58d78b7\", \"finished_at\": \"2026-05-16T00:16:55.637Z\", \"training_hours\": 1.92}, \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/pacs && python run_accuracy_eval.py --model checkpoints/DeepSeek-R1-Distill-Qwen-7B --conditions importance_s025 --num-problems 50 --max-new-tokens 8192 --output-name accuracy_ds_s025_8k_v2.json --gpu cuda:0\\\"\", \"server\": \"westd-22162\", \"gpu\": [\"cuda:3\"], \"pid\": \"282534\", \"log_path\": \"~/runs/phase-gated-compound-sparse/acc_ds_s025_8k_v2.log\", \"submitted_at\": \"2026-05-15T22:21:35.167Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 7144.4, \"gpu_hours\": 1.98}, \"pid\": \"282534\", \"log_path\": \"~/runs/phase-gated-compound-sparse/acc_ds_s025_8k_v2.log\", \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-16T00:16:59.245439+00:00\"}]}, \"conclusion\": \"negative\", \"metrics\": {\"accuracy\": 0.08, \"correct\": 4, \"total\": 50, \"truncated_count\": 38, \"truncated_rate\": 0.76, \"avg_tokens\": 6343.8, \"max_new_tokens\": 8192, \"total_time_seconds\": 6827.8, \"null_count\": 36}, \"checkpoint_path\": \"/root/autodl-tmp/pacs/analysis_output/accuracy_ds_s025_8k_v2.json\", \"completed_at\": \"2026-05-16T00:20:39.536Z\"}, \"gsm8k_qw_rand_s025_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T22:30:14.407Z\", \"updated_at\": \"2026-05-15T23:44:43.451Z\", \"spec\": {\"data_path\": \"data/gsm8k.json\", \"data_count\": 50, \"model_name\": \"Qwen2.5-7B-Instruct\", \"seed\": 42, \"masking_method\": \"random\", \"sparsity\": 0.25, \"output_dir\": \"/root/autodl-tmp/pacs/profiling_output_gsm8k_qw_rand_s025_v2\", \"bootstrap_fix\": \"D029 median CI\"}, \"hypothesis\": \"C10 重跑：QW random masking s=0.25 GSM8K compound interaction（修复 bootstrap bug 后）\", \"parent\": \"gsm8k_qw_rand_s025\", \"server\": \"westd-22162\", \"gpu\": \"cuda:1\", \"account\": \"root\", \"reproduce\": {\"server\": \"westd-22162\", \"gpu\": \"cuda:1\", \"started_at\": \"2026-05-15T23:23:26.824Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/pacs && python -m pacs.profiling.run_profiling --model_path /root/autodl-tmp/pacs/checkpoints/Qwen2.5-7B-Instruct --data_path data/gsm8k.json --output_dir ./profiling_output_gsm8k_qw_rand_s025_v2 --sparsity_levels 0.25 --masking_method random --save_generations\\\"\", \"code_commit\": \"1b4f61aa366a9fe320f8563c8f7acb5af58d78b7\", \"finished_at\": \"2026-05-15T23:41:06.084Z\", \"training_hours\": 0.29}, \"pid\": \"288196\", \"log_path\": \"~/runs/phase-gated-compound-sparse/gsm8k_qw_rand_s025_v2.log\", \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T23:41:09.749498+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"verdict\": \"PASS\", \"n_problems\": 50, \"n_bootstrap\": 1000, \"seed\": 42, \"high_sparsity\": {\"n_segments\": 216, \"n_tokens\": 9326, \"ppl_dense\": 1.0695, \"ppl_attn\": 5.9362, \"ppl_kv\": 3.4316, \"ppl_both\": 15.7484, \"ii_mean\": 6.5954, \"ii_ci\": [1.1114, 11.3791], \"ii_median\": 0.7176, \"ii_median_ci\": [0.5959, 0.9347], \"winsorized_mean\": 6.5046, \"skewness\": -4.6807, \"outlier_count\": 3}, \"low_sparsity\": {\"n_segments\": 252, \"n_tokens\": 29224, \"ppl_dense\": 1.1972, \"ppl_attn\": 11.5347, \"ppl_kv\": 5.6038, \"ppl_both\": 21.6874, \"ii_mean\": 2.3883, \"ii_ci\": [-8.4602, 11.029], \"ii_median\": 1.4587, \"ii_median_ci\": [1.1121, 2.0451], \"winsorized_mean\": 5.8911, \"skewness\": -7.6074, \"outlier_count\": 4}, \"mid_sparsity\": {\"n_segments\": 51, \"n_tokens\": 5954, \"ppl_dense\": 1.2601, \"ppl_attn\": 13.4132, \"ppl_kv\": 6.4841, \"ppl_both\": 20.8714, \"ii_mean\": 4.5407, \"ii_ci\": [-4.8854, 12.4605], \"ii_median\": 1.1272, \"ii_median_ci\": [0.637, 3.3729], \"winsorized_mean\": 6.3284, \"skewness\": -3.4048, \"outlier_count\": 1}}, \"checkpoint_path\": \"/root/autodl-tmp/pacs/profiling_output_gsm8k_qw_rand_s025_v2\", \"completed_at\": \"2026-05-15T23:44:43.451Z\"}, \"acc_ds_s030_8k_v2\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-15T21:35:02.560Z\", \"updated_at\": \"2026-05-15T23:30:20.392Z\", \"hypothesis\": \"DS s030 accuracy eval with max_new_tokens=8192，补全 5-point dose curve。\", \"server\": \"westd-22162\", \"gpu\": \"cuda:2\", \"account\": \"root\", \"reproduce\": {\"server\": \"westd-22162\", \"gpu\": \"cuda:2\", \"started_at\": \"2026-05-15T23:30:00.599Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/pacs && python run_accuracy_eval.py --model checkpoints/DeepSeek-R1-Distill-Qwen-7B --conditions importance_s030 --num-problems 50 --max-new-tokens 8192 --output-name accuracy_ds_s030_8k_v2.json --gpu cuda:0\\\"\", \"code_commit\": \"1b4f61aa366a9fe320f8563c8f7acb5af58d78b7\"}, \"spec\": {\"data_path\": \"MATH problems 1-50\", \"data_count\": 50, \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B\", \"seed\": 42, \"checkpoint_path\": \"N/A (eval only)\", \"conditions\": \"importance_s030\", \"max_new_tokens\": 8192}, \"pid\": \"288901\", \"log_path\": \"~/runs/phase-gated-compound-sparse/acc_ds_s030_8k_v2.log\"}, \"acc_ds_s020_8k_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T21:34:59.657Z\", \"updated_at\": \"2026-05-15T23:29:33.331Z\", \"hypothesis\": \"DS s020 accuracy eval with max_new_tokens=8192，补全 5-point dose curve。4096 版截断率 64%，8k 目标 <20%。\", \"server\": \"westd-22162\", \"gpu\": \"cuda:2\", \"account\": \"root\", \"reproduce\": {\"server\": \"westd-22162\", \"gpu\": \"cuda:2\", \"started_at\": \"2026-05-15T21:52:57.528Z\", \"finished_at\": \"2026-05-15T23:28:21.999Z\", \"training_hours\": 1.59}, \"spec\": {\"command\": \"python run_accuracy_eval.py --model checkpoints/DeepSeek-R1-Distill-Qwen-7B --conditions importance_s020 --num-problems 50 --max-new-tokens 8192 --output-name accuracy_ds_s020_8k_v2.json --gpu cuda:0\", \"server\": \"westd-22162\", \"gpu\": [\"cuda:2\"], \"pid\": \"280638\", \"log_path\": \"~/runs/phase-gated-compound-sparse/acc_ds_s020_8k_v2.log\", \"submitted_at\": \"2026-05-15T21:55:00Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"MATH problems 1-50\", \"data_count\": 50, \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B\", \"seed\": 42, \"checkpoint_path\": \"N/A (eval only)\", \"wall_clock_seconds\": 5673.3, \"gpu_hours\": 1.58}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T23:28:28.680643+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"accuracy\": 0.3, \"correct\": 15, \"total\": 50, \"truncated_count\": 29, \"truncated_rate\": 0.58, \"total_time_seconds\": 5549}, \"checkpoint_path\": \"/root/autodl-tmp/pacs/analysis_output/accuracy_ds_s020_8k_v2.json\", \"completed_at\": \"2026-05-15T23:29:33.331Z\"}, \"gsm8k_qw_rand_s030_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T22:30:15.959Z\", \"updated_at\": \"2026-05-15T23:28:35.411Z\", \"spec\": {\"data_path\": \"data/gsm8k.json\", \"data_count\": 50, \"model_name\": \"Qwen2.5-7B-Instruct\", \"seed\": 42, \"masking_method\": \"random\", \"sparsity\": 0.3, \"output_dir\": \"/root/autodl-tmp/pacs/profiling_output_gsm8k_qw_rand_s030_v2\", \"bootstrap_fix\": \"D029 median CI\"}, \"hypothesis\": \"C10 重跑：QW random masking s=0.30 GSM8K compound interaction（修复 bootstrap bug 后）\", \"parent\": \"gsm8k_qw_rand_s030\", \"server\": \"westd-22162\", \"gpu\": \"cuda:1\", \"account\": \"root\", \"reproduce\": {\"server\": \"westd-22162\", \"gpu\": \"cuda:1\", \"started_at\": \"2026-05-15T23:05:02.114Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/pacs && python -m pacs.profiling.run_profiling --model_path /root/autodl-tmp/pacs/checkpoints/Qwen2.5-7B-Instruct --data_path data/gsm8k.json --output_dir ./profiling_output_gsm8k_qw_rand_s030_v2 --sparsity_levels 0.30 --masking_method random --save_generations\\\"\", \"code_commit\": \"1b4f61aa366a9fe320f8563c8f7acb5af58d78b7\", \"finished_at\": \"2026-05-15T23:21:14.567Z\", \"training_hours\": 0.27}, \"pid\": \"286781\", \"log_path\": \"~/runs/phase-gated-compound-sparse/gsm8k_qw_rand_s030_v2.log\", \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T23:21:20.903508+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"verdict\": \"PASS\", \"n_problems\": 50, \"n_bootstrap\": 1000, \"seed\": 42, \"high_sparsity\": {\"n_segments\": 216, \"n_tokens\": 9326, \"null_ratio\": \"2/50\", \"ppl_dense\": 1.0695, \"ppl_attn\": 6.5613, \"ppl_kv\": 4.481, \"ppl_both\": 23.7486, \"ii_mean\": 11.83, \"ii_median\": 2.31, \"ii_ci\": [6.17, 17.04], \"ii_median_ci\": [1.64, 2.81], \"winsorized_mean\": 10.55, \"skewness\": -2.29, \"outlier_count\": 7}, \"low_sparsity\": {\"n_segments\": 252, \"n_tokens\": 29224, \"null_ratio\": \"5/50\", \"ppl_dense\": 1.1972, \"ppl_attn\": 6.3283, \"ppl_kv\": 8.5374, \"ppl_both\": 56.2304, \"ii_mean\": 31.26, \"ii_median\": 5.2, \"ii_ci\": [17.84, 47.86], \"ii_median_ci\": [3.95, 7.24], \"winsorized_mean\": 16.35, \"skewness\": 7.57, \"outlier_count\": 4}, \"mid_sparsity\": {\"n_segments\": 51, \"n_tokens\": 5954, \"null_ratio\": \"17/50\", \"ppl_dense\": 1.2601, \"ppl_attn\": 18.6162, \"ppl_kv\": 11.6625, \"ppl_both\": 47.9019, \"ii_mean\": 18.02, \"ii_median\": 2.7, \"ii_ci\": [0.09, 36.69], \"ii_median_ci\": [1.46, 8.77], \"winsorized_mean\": 18.22, \"skewness\": 0.43, \"outlier_count\": 2}}, \"checkpoint_path\": \"/root/autodl-tmp/pacs/profiling_output_gsm8k_qw_rand_s030_v2/profiling_results.json\", \"completed_at\": \"2026-05-15T23:23:24.379Z\"}, \"acc_qw_s025_n100_b2_fix\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T22:22:57.057Z\", \"updated_at\": \"2026-05-15T23:28:18.012Z\", \"spec\": {\"data_path\": \"MATH-500\", \"data_count\": 50, \"model_name\": \"Qwen2.5-7B-Instruct\", \"seed\": 42, \"description\": \"QW importance_s025 batch2 (problems 51-100) accuracy eval with max_new_tokens=8192, fixing original batch2 which used 2048\", \"checkpoint_source\": \"/root/autodl-tmp/pacs/checkpoints/Qwen2.5-7B-Instruct\", \"eval_data\": \"MATH-500 problems 51-100\", \"checkpoint_path\": \"N/A (eval only)\"}, \"hypothesis\": \"重跑 QW s025 batch2 (problems 51-100) with max_new_tokens=8192，修复原 batch2 使用 2048 的不一致问题。\", \"parent\": \"acc_qw_s025_n100\", \"server\": \"westd-22162\", \"gpu\": \"cuda:1\", \"account\": \"root\", \"reproduce\": {\"server\": \"westd-22162\", \"gpu\": \"cuda:1\", \"started_at\": \"2026-05-15T22:43:13.237Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/pacs && python run_accuracy_eval.py --model checkpoints/Qwen2.5-7B-Instruct --conditions importance_s025 --num-problems 50 --start-index 50 --max-new-tokens 8192 --gpu cuda:0 --seed 42 --output-name accuracy_eval_qw_s025_b2_fix.json\\\"\", \"code_commit\": \"1b4f61aa366a9fe320f8563c8f7acb5af58d78b7\", \"finished_at\": \"2026-05-15T23:02:06.320Z\", \"training_hours\": 0.31}, \"pid\": \"285337\", \"log_path\": \"/root/runs/phase-gated-compound-sparse/acc_qw_s025_n100_b2_fix.log\", \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T23:02:09.471595+00:00\"}]}, \"metrics\": {\"accuracy\": 0.34, \"correct\": 17, \"n_problems\": 50, \"truncation_rate\": 0.06, \"truncated_count\": 3, \"avg_tokens\": 1044, \"max_new_tokens\": 8192, \"total_time_seconds\": 1099, \"batch\": \"b2 (problems 51-100)\", \"merged_n100_accuracy\": 0.33, \"merged_n100_correct\": 33, \"merged_n100_note\": \"batch1 used max_new_tokens=2048, batch2_fix used 8192 — mismatch\"}, \"checkpoint_path\": \"/root/autodl-tmp/pacs/analysis_output/accuracy_eval_qw_s025_b2_fix.json\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T23:28:18.012Z\"}, \"acc_ds_dense_8k_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T22:27:00.640Z\", \"updated_at\": \"2026-05-15T23:28:12.650Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/pacs && python run_accuracy_eval.py --model checkpoints/DeepSeek-R1-Distill-Qwen-7B --conditions dense --num-problems 50 --max-new-tokens 8192 --output-name accuracy_ds_dense_8k_v2.json --gpu cuda:0\\\"\", \"server\": \"westd-22162\", \"gpu\": [\"cuda:0\"], \"pid\": \"283843\", \"log_path\": \"~/runs/phase-gated-compound-sparse/acc_ds_dense_8k_v2.log\", \"submitted_at\": \"2026-05-15T22:28:53.194Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 3559.5, \"gpu_hours\": 0.99}, \"hypothesis\": \"DS dense 8k 重跑：原 acc_ds_dense_8k 进程被 kill 后输出丢失，需重跑获取完整 dense baseline accuracy (max_new_tokens=8192)。\", \"server\": \"westd-22162\", \"gpu\": \"cuda:0\", \"account\": \"root\", \"reproduce\": {\"server\": \"westd-22162\", \"gpu\": \"cuda:0\", \"started_at\": \"2026-05-15T22:28:10.491Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/pacs && python run_accuracy_eval.py --model checkpoints/DeepSeek-R1-Distill-Qwen-7B --conditions dense --num-problems 50 --max-new-tokens 8192 --output-name accuracy_ds_dense_8k_v2.json --gpu cuda:0\\\"\", \"code_commit\": \"1b4f61aa366a9fe320f8563c8f7acb5af58d78b7\", \"finished_at\": \"2026-05-15T23:17:23.198Z\", \"training_hours\": 0.82}, \"pid\": \"283843\", \"log_path\": \"~/runs/phase-gated-compound-sparse/acc_ds_dense_8k_v2.log\", \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T23:17:26.372428+00:00\"}]}, \"metrics\": {\"accuracy\": 0.74, \"correct\": 37, \"n_problems\": 50, \"truncation_rate\": 0.16, \"truncated_count\": 8, \"avg_tokens\": 3126, \"max_new_tokens\": 8192, \"total_time_seconds\": 2882}, \"checkpoint_path\": \"/root/autodl-tmp/pacs/analysis_output/accuracy_ds_dense_8k_v2.json\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T23:28:12.650Z\"}, \"acc_ds_s015_8k_v2\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-15T21:34:57.489Z\", \"updated_at\": \"2026-05-15T23:20:29.968Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/pacs && python run_accuracy_eval.py --model checkpoints/DeepSeek-R1-Distill-Qwen-7B --conditions importance_s015 --num-problems 50 --max-new-tokens 8192 --output-name accuracy_ds_s015_8k_v2.json --gpu cuda:0\\\"\", \"server\": \"westd-22162\", \"data_path\": \"MATH problems 1-50\", \"data_count\": 50, \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B\", \"seed\": 42, \"checkpoint_path\": \"N/A (eval only)\", \"gpu\": [\"cuda:0\"], \"pid\": \"287691\"}, \"hypothesis\": \"DS s015 accuracy eval with max_new_tokens=8192，验证 dense→s015 是否存在断崖式下降（v1 暗示 0.74→~0.36）。\", \"gpu\": \"cuda:0\", \"server\": \"westd-22162\"}, \"acc_qw_s020_n100_b2_fix\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T22:22:55.755Z\", \"updated_at\": \"2026-05-15T22:48:39.196Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/pacs && python run_accuracy_eval.py --model checkpoints/Qwen2.5-7B-Instruct --conditions importance_s020 --num-problems 50 --start-index 50 --max-new-tokens 8192 --gpu cuda:0 --seed 42 --output-name accuracy_eval_qw_s020_b2_fix.json\\\"\", \"server\": \"westd-22162\", \"gpu\": [\"cuda:1\"], \"pid\": \"283051\", \"log_path\": \"~/runs/phase-gated-compound-sparse/acc_qw_s020_n100_b2_fix.log\", \"submitted_at\": \"2026-05-15T22:25:18.472Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 1400.7, \"gpu_hours\": 0.39}, \"hypothesis\": \"重跑 QW s020 batch2 (problems 51-100) with max_new_tokens=8192，修复原 batch2 使用 2048 的不一致问题。\", \"parent\": \"acc_qw_s020_n100\", \"server\": \"westd-22162\", \"gpu\": \"cuda:1\", \"account\": \"root\", \"reproduce\": {\"server\": \"westd-22162\", \"gpu\": \"cuda:1\", \"started_at\": \"2026-05-15T22:25:15.841Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/pacs && python run_accuracy_eval.py --model checkpoints/Qwen2.5-7B-Instruct --conditions importance_s020 --num-problems 50 --start-index 50 --max-new-tokens 8192 --gpu cuda:0 --seed 42 --output-name accuracy_eval_qw_s020_b2_fix.json\\\"\", \"code_commit\": \"1b4f61aa366a9fe320f8563c8f7acb5af58d78b7\", \"finished_at\": \"2026-05-15T22:40:53.877Z\", \"training_hours\": 0.26}, \"pid\": \"283051\", \"log_path\": \"~/runs/phase-gated-compound-sparse/acc_qw_s020_n100_b2_fix.log\", \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T22:40:57.414634+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"batch2_correct\": 23, \"batch2_total\": 50, \"batch2_acc\": 0.46, \"batch1_correct_v2\": 13, \"batch1_total\": 50, \"batch1_acc_v2\": 0.26, \"combined_correct\": 36, \"combined_total\": 100, \"combined_acc\": 0.36, \"null_count\": 2, \"truncated_count\": 1, \"total_time_seconds\": 884.3, \"max_new_tokens\": 8192, \"original_batch2_correct\": 22, \"original_batch2_acc\": 0.44, \"delta_vs_original\": \"+1 correct (+0.02 acc)\"}, \"checkpoint_path\": \"N/A (eval only)\", \"completed_at\": \"2026-05-15T22:48:39.196Z\"}, \"gsm8k_qw_rand_s025\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T21:37:36.627Z\", \"updated_at\": \"2026-05-15T22:27:18.969Z\", \"hypothesis\": \"C10: QW random masking s=0.25 在 GSM8K 上的 compound interaction，作为 importance masking 的对照组。参照 gsm8k_profiling_qw 设置。\", \"parent\": \"gsm8k_profiling_qw\", \"spec\": {\"command\": \"python run_profiling_gsm8k.py --model_path checkpoints/Qwen2.5-7B-Instruct --masking_method random --data_path data/gsm8k_test.json --max_problems 50 --seed 42 --min_phase_length 10 --save_generations --sparsity_levels 0.25 --device cuda:0 --output_dir ./gsm8k_profiling/qw_rand_s025\", \"server\": \"westd-22162\", \"gpu\": [\"cuda:0\"], \"pid\": \"281019\", \"log_path\": \"~/runs/phase-gated-compound-sparse/gsm8k_qw_rand_s025.log\", \"submitted_at\": \"2026-05-15T21:58:43.521Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/gsm8k_test.json\", \"data_count\": 50, \"model_name\": \"Qwen2.5-7B-Instruct\", \"seed\": 42, \"checkpoint_source\": \"checkpoints/Qwen2.5-7B-Instruct\", \"eval_data\": \"data/gsm8k_test.json (50 problems)\", \"wall_clock_seconds\": 1715.4, \"gpu_hours\": 0.48}, \"server\": \"westd-22162\", \"gpu\": \"cuda:0\", \"account\": \"root\", \"conclusion\": \"failed\", \"failure_reason\": \"同 gsm8k_qw_rand_s030 的 bootstrap bug (tuple vs dict)，Director 指令主动 kill\", \"checkpoint_path\": \"N/A (killed before completion)\", \"completed_at\": \"2026-05-15T22:27:18.969Z\"}, \"gsm8k_qw_rand_s030\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T21:37:39.530Z\", \"updated_at\": \"2026-05-15T22:23:52.155Z\", \"hypothesis\": \"C10: QW random masking s=0.30 在 GSM8K 上的 compound interaction，作为 importance masking 的对照组。gsm8k_profiling_qw 中此条件结果 INVALID，需重跑。\", \"parent\": \"gsm8k_profiling_qw\", \"spec\": {\"command\": \"python run_profiling_gsm8k.py --model_path checkpoints/Qwen2.5-7B-Instruct --masking_method random --data_path data/gsm8k_test.json --max_problems 50 --seed 42 --min_phase_length 10 --save_generations --sparsity_levels 0.30 --device cuda:0 --output_dir ./gsm8k_profiling/qw_rand_s030\", \"server\": \"westd-22162\", \"gpu\": [\"cuda:1\"], \"pid\": \"281443\", \"log_path\": \"~/runs/phase-gated-compound-sparse/gsm8k_qw_rand_s030.log\", \"submitted_at\": \"2026-05-15T21:59:10.598Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/gsm8k_test.json\", \"data_count\": 50, \"model_name\": \"Qwen2.5-7B-Instruct\", \"seed\": 42, \"checkpoint_source\": \"checkpoints/Qwen2.5-7B-Instruct\", \"eval_data\": \"data/gsm8k_test.json (50 problems)\", \"wall_clock_seconds\": 1475.8, \"gpu_hours\": 0.41}, \"server\": \"westd-22162\", \"gpu\": \"cuda:1\", \"account\": \"root\", \"reproduce\": {\"finished_at\": \"2026-05-15T22:23:43.826Z\"}, \"failure_reason\": \"Traceback → wargs) ^^^^^^^^^^^^^^^^^^^^^ File \\\"/root/autodl-tmp/pacs/run_profiling_gsm8k.py\\\", line 459, in run_profiling \\\"mean\\\": bs[\\\"mean\\\"], \\\"ci_low\\\": bs[\\\"ci_low\\\"], \\\"ci_high\\\": bs[\\\"ci_high\\\"], ~~^^^^^^^^ TypeError: tuple indices must be integers or slices, not str\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-15T22:23:46.370Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-15T22:23:54.752268+00:00\"}]}}, \"acc_qw_s030_n100\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T21:34:40.948Z\", \"updated_at\": \"2026-05-15T22:21:11.181Z\", \"hypothesis\": \"补跑 QW importance_s030 problems 51-100，扩展到 n=100 以降低噪声\", \"spec\": {\"command\": \"python run_accuracy_eval.py --model checkpoints/Qwen2.5-7B-Instruct --conditions importance_s030 --num-problems 50 --start-index 50 --gpu cuda:0 --seed 42 --output-name accuracy_eval_qw_s030_n51_100.json\", \"server\": \"westd-22162\", \"gpu\": [\"cuda:3\"], \"pid\": \"280094\", \"log_path\": \"~/runs/phase-gated-compound-sparse/acc_qw_s030_n100.log\", \"submitted_at\": \"2026-05-15T21:47:49.602Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"MATH problems 51-100\", \"data_count\": 50, \"model_name\": \"Qwen2.5-7B-Instruct\", \"seed\": 42, \"checkpoint_source\": \"checkpoints/Qwen2.5-7B-Instruct\", \"eval_data\": \"MATH problems 51-100\", \"wall_clock_seconds\": 2001.6, \"gpu_hours\": 0.56}, \"conclusion\": \"success\", \"metrics\": {\"batch1_correct\": 7, \"batch1_total\": 50, \"batch1_acc\": 0.14, \"batch2_correct\": 12, \"batch2_total\": 50, \"batch2_acc\": 0.24, \"combined_correct\": 19, \"combined_total\": 100, \"combined_acc\": 0.19}, \"checkpoint_path\": \"N/A (eval only)\", \"completed_at\": \"2026-05-15T22:21:11.181Z\"}, \"acc_qw_dense_n100\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T21:34:35.557Z\", \"updated_at\": \"2026-05-15T21:54:45.453Z\", \"hypothesis\": \"补跑 QW dense problems 51-100，扩展到 n=100 以降低噪声\", \"spec\": {\"command\": \"python run_accuracy_eval.py --model checkpoints/Qwen2.5-7B-Instruct --conditions dense --num-problems 50 --start-index 50 --gpu cuda:0 --seed 42 --output-name accuracy_eval_qw_dense_n51_100.json\", \"server\": \"westd-22162\", \"gpu\": [\"cuda:2\"], \"pid\": \"279068\", \"log_path\": \"/root/autodl-tmp/pacs/analysis_output/accuracy_eval_qw_dense_n51_100.json\", \"submitted_at\": \"2026-05-15T21:35:05.456Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"MATH problems 51-100\", \"data_count\": 50, \"model_name\": \"Qwen2.5-7B-Instruct\", \"seed\": 42, \"checkpoint_path\": \"N/A (eval only)\", \"wall_clock_seconds\": 1176.6, \"gpu_hours\": 0.33}, \"metrics\": {\"batch1_correct\": 16, \"batch1_total\": 50, \"batch1_acc\": 0.32, \"batch2_correct\": 24, \"batch2_total\": 50, \"batch2_acc\": 0.48, \"combined_correct\": 40, \"combined_total\": 100, \"combined_acc\": 0.4}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T21:54:42.068Z\"}, \"acc_qw_s015_n100\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T21:34:38.959Z\", \"updated_at\": \"2026-05-15T21:50:13.043Z\", \"hypothesis\": \"补跑 QW importance_s015 problems 51-100，扩展到 n=100 以降低噪声\", \"spec\": {\"command\": \"python run_accuracy_eval.py --model checkpoints/Qwen2.5-7B-Instruct --conditions importance_s015 --num-problems 50 --start-index 50 --gpu cuda:0 --seed 42 --output-name accuracy_eval_qw_s015_n51_100.json\", \"server\": \"westd-22162\", \"gpu\": [\"cuda:3\"], \"pid\": \"279145\", \"log_path\": \"/root/autodl-tmp/pacs/analysis_output/accuracy_eval_qw_s015_n51_100.json\", \"submitted_at\": \"2026-05-15T21:35:07.387Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"MATH problems 51-100\", \"data_count\": 50, \"model_name\": \"Qwen2.5-7B-Instruct\", \"seed\": 42, \"checkpoint_path\": \"N/A (eval only)\"}, \"metrics\": {\"batch1_acc\": 0.34, \"batch1_correct\": 17, \"batch1_total\": 50, \"batch2_acc\": 0.38, \"batch2_correct\": 19, \"batch2_total\": 50, \"combined_acc\": 0.36, \"combined_correct\": 36, \"combined_total\": 100}, \"conclusion\": \"success\", \"checkpoint_path\": \"N/A (eval only)\", \"log_path\": \"/root/autodl-tmp/pacs/analysis_output/accuracy_eval_qw_s015_n51_100.json\", \"completed_at\": \"2026-05-15T21:47:46.664Z\"}, \"acc_qw_s025_n100\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T21:09:36.278Z\", \"updated_at\": \"2026-05-15T21:34:48.072Z\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=3 python run_accuracy_eval.py --model checkpoints/Qwen2.5-7B-Instruct --conditions importance_s025 --num-problems 50 --start-index 50 --gpu cuda:0 --seed 42 --output-name accuracy_eval_qw_s025_n51_100.json\", \"server\": \"westd-22162\", \"data_path\": \"MATH-500\", \"data_count\": 50, \"model_name\": \"Qwen2.5-7B-Instruct\", \"seed\": 42, \"description\": \"QW importance_s025 accuracy eval problems 51-100\", \"checkpoint_source\": \"/root/autodl-tmp/pacs/checkpoints/Qwen2.5-7B-Instruct\", \"eval_data\": \"MATH-500 problems 51-100\", \"checkpoint_path\": \"N/A (eval only)\", \"log_path\": \"/root/autodl-tmp/pacs/analysis_output/accuracy_eval_qw_s025_n51_100.json\"}, \"conclusion\": \"success\", \"metrics\": {\"batch1_acc\": 0.32, \"batch1_correct\": 16, \"batch1_total\": 50, \"batch2_acc\": 0.34, \"batch2_correct\": 17, \"batch2_total\": 50, \"combined_acc\": 0.33, \"combined_correct\": 33, \"combined_total\": 100}, \"completed_at\": \"2026-05-15T21:30:09.145Z\"}, \"acc_qw_s020_n100\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T21:09:34.155Z\", \"updated_at\": \"2026-05-15T21:34:46.864Z\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=2 python run_accuracy_eval.py --model checkpoints/Qwen2.5-7B-Instruct --conditions importance_s020 --num-problems 50 --start-index 50 --gpu cuda:0 --seed 42 --output-name accuracy_eval_qw_s020_n51_100.json\", \"server\": \"westd-22162\", \"data_path\": \"MATH-500\", \"data_count\": 50, \"model_name\": \"Qwen2.5-7B-Instruct\", \"seed\": 42, \"description\": \"QW importance_s020 accuracy eval problems 51-100\", \"checkpoint_source\": \"/root/autodl-tmp/pacs/checkpoints/Qwen2.5-7B-Instruct\", \"eval_data\": \"MATH-500 problems 51-100\", \"checkpoint_path\": \"N/A (eval only)\", \"log_path\": \"/root/autodl-tmp/pacs/analysis_output/accuracy_eval_qw_s020_n51_100.json\"}, \"conclusion\": \"success\", \"metrics\": {\"batch1_acc\": 0.26, \"batch1_correct\": 13, \"batch1_total\": 50, \"batch2_acc\": 0.44, \"batch2_correct\": 22, \"batch2_total\": 50, \"combined_acc\": 0.35, \"combined_correct\": 35, \"combined_total\": 100}, \"completed_at\": \"2026-05-15T21:30:07.934Z\"}, \"acc_ds_s030_8k\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T21:22:53.748Z\", \"updated_at\": \"2026-05-15T21:29:19.105Z\", \"hypothesis\": \"8192 token budget 下 DS s030 截断率应从高截断率降至 <20%，accuracy 应高于 4096 版本的 0.10\", \"conclusion\": \"killed\", \"spec\": {\"command\": \"python run_accuracy_eval.py --model /root/autodl-tmp/pacs/checkpoints/DeepSeek-R1-Distill-Qwen-7B --conditions importance_s030 --num-problems 50 --max-new-tokens 8192 --output-name accuracy_ds_s030_8k.json --gpu cuda:0\", \"server\": \"westd-22162\", \"data_path\": \"/root/autodl-tmp/pacs/data/math500.json\", \"data_count\": 50, \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B\", \"seed\": 42, \"planned_gpu\": \"cuda:0\"}, \"completed_at\": \"2026-05-15T21:29:19.105Z\"}, \"acc_ds_s025_8k\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T21:22:52.297Z\", \"updated_at\": \"2026-05-15T21:29:17.817Z\", \"hypothesis\": \"8192 token budget 下 DS s025 截断率应从 76% 降至 <20%，accuracy 应高于 4096 版本的 0.08\", \"conclusion\": \"killed\", \"spec\": {\"command\": \"python run_accuracy_eval.py --model /root/autodl-tmp/pacs/checkpoints/DeepSeek-R1-Distill-Qwen-7B --conditions importance_s025 --num-problems 50 --max-new-tokens 8192 --output-name accuracy_ds_s025_8k.json --gpu cuda:0\", \"server\": \"westd-22162\", \"data_path\": \"/root/autodl-tmp/pacs/data/math500.json\", \"data_count\": 50, \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B\", \"seed\": 42, \"planned_gpu\": \"cuda:1\"}, \"completed_at\": \"2026-05-15T21:29:17.817Z\"}, \"acc_ds_s020_8k\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T21:22:51.129Z\", \"updated_at\": \"2026-05-15T21:29:16.495Z\", \"hypothesis\": \"8192 token budget 下 DS s020 截断率应从 64% 降至 <20%，accuracy 应高于 4096 版本的 0.26\", \"conclusion\": \"killed\", \"spec\": {\"command\": \"python run_accuracy_eval.py --model /root/autodl-tmp/pacs/checkpoints/DeepSeek-R1-Distill-Qwen-7B --conditions importance_s020 --num-problems 50 --max-new-tokens 8192 --output-name accuracy_ds_s020_8k.json --gpu cuda:0\", \"server\": \"westd-22162\", \"data_path\": \"/root/autodl-tmp/pacs/data/math500.json\", \"data_count\": 50, \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B\", \"seed\": 42, \"planned_gpu\": \"cuda:0\"}, \"completed_at\": \"2026-05-15T21:29:16.495Z\"}, \"acc_ds_dense_8k\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T21:22:44.546Z\", \"updated_at\": \"2026-05-15T21:28:57.693Z\", \"hypothesis\": \"8192 token budget 下 DS dense baseline 截断率应降至 <20%，accuracy 应高于 4096 版本的 0.52\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/pacs && python run_accuracy_eval.py --model /root/autodl-tmp/pacs/checkpoints/DeepSeek-R1-Distill-Qwen-7B --conditions dense --num-problems 50 --max-new-tokens 8192 --output-name accuracy_ds_dense_8k.json --gpu cuda:0\\\"\", \"server\": \"westd-22162\", \"gpu\": [\"cuda:0\"], \"pid\": \"277990\", \"log_path\": \"~/runs/phase-gated-compound-sparse/acc_ds_dense_8k.log\", \"submitted_at\": \"2026-05-15T21:26:48.000Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 129.7, \"gpu_hours\": 0.04}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-15T21:28:57.693Z\"}, \"acc_ds_s015_8k\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T21:22:48.736Z\", \"updated_at\": \"2026-05-15T21:28:48.029Z\", \"hypothesis\": \"8192 token budget 下 DS s015 截断率应降至 <20%，accuracy 应高于 4096 版本的 0.36\", \"conclusion\": \"killed\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/pacs && python run_accuracy_eval.py --model /root/autodl-tmp/pacs/checkpoints/DeepSeek-R1-Distill-Qwen-7B --conditions importance_s015 --num-problems 50 --max-new-tokens 8192 --output-name accuracy_ds_s015_8k.json --gpu cuda:0\\\"\", \"server\": \"westd-22162\", \"gpu\": [\"cuda:1\"], \"pid\": \"278390\", \"log_path\": \"~/runs/phase-gated-compound-sparse/acc_ds_s015_8k.log\", \"submitted_at\": \"2026-05-15T21:27:14.900Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 93.1, \"gpu_hours\": 0.03}, \"completed_at\": \"2026-05-15T21:28:48.029Z\"}, \"acc_ds_s025\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T20:49:25.437Z\", \"updated_at\": \"2026-05-15T21:23:19.024Z\", \"spec\": {\"command\": \"python run_accuracy_eval.py --model DeepSeek-R1-Distill-Qwen-7B --conditions importance_s025 --num-problems 50\", \"server\": \"westd-22162\", \"gpu\": [\"cuda:1\"], \"pid\": \"274546\", \"log_path\": \"~/runs/phase-gated-compound-sparse/acc_ds_s025.log\", \"submitted_at\": \"2026-05-15T20:50:01.624Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/pacs/data/math500.json\", \"data_count\": 50, \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B\", \"seed\": 42, \"type\": \"eval\", \"checkpoint_source\": \"checkpoints/DeepSeek-R1-Distill-Qwen-7B\", \"eval_data\": \"MATH-500 n=50\", \"wall_clock_seconds\": 1803.4, \"gpu_hours\": 0.5}, \"reproduce\": {\"finished_at\": \"2026-05-15T21:18:39.381Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T21:18:44.945540+00:00\"}]}, \"metrics\": {\"accuracy\": 0.08, \"correct\": 4, \"total\": 50, \"null_count\": 37, \"null_rate\": 0.74, \"output_truncated_count\": 38, \"output_truncated_rate\": 0.76, \"wrong_count\": 9, \"wrong_rate\": 0.18, \"extraction_failure_count\": 1, \"extraction_failure_rate\": 0.02, \"total_time_s\": 1670.5, \"heads_pruned\": 196, \"delta_vs_dense\": -0.44}, \"conclusion\": \"negative\", \"checkpoint_path\": \"/root/autodl-tmp/pacs/analysis_output/accuracy_eval_ds_s025.json\", \"log_path\": \"~/runs/phase-gated-compound-sparse/acc_ds_s025.log\", \"completed_at\": \"2026-05-15T21:20:04.995Z\"}, \"acc_ds_s020\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T20:49:21.186Z\", \"updated_at\": \"2026-05-15T21:20:03.642Z\", \"spec\": {\"command\": \"python run_accuracy_eval.py --model DeepSeek-R1-Distill-Qwen-7B --conditions importance_s020 --num-problems 50\", \"server\": \"westd-22162\", \"gpu\": [\"cuda:0\"], \"pid\": \"273846\", \"log_path\": \"~/runs/phase-gated-compound-sparse/acc_ds_s020.log\", \"submitted_at\": \"2026-05-15T20:49:20.822Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/pacs/data/math500.json\", \"data_count\": 50, \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B\", \"seed\": 42, \"type\": \"eval\", \"checkpoint_source\": \"checkpoints/DeepSeek-R1-Distill-Qwen-7B\", \"eval_data\": \"MATH-500 n=50\", \"wall_clock_seconds\": 1842.8, \"gpu_hours\": 0.51}, \"reproduce\": {\"finished_at\": \"2026-05-15T21:16:00.586Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T21:16:03.750890+00:00\"}]}, \"conclusion\": \"negative\", \"metrics\": {\"ds_s020_acc\": 0.26, \"ds_s020_acc_v2\": 0.26, \"ds_s020_correct\": 13, \"ds_s020_total\": 50, \"ds_s020_delta_vs_dense\": -0.26, \"output_truncated_count\": 32, \"output_truncated_rate\": 0.64, \"extraction_failure_count\": 31, \"extraction_failure_rate\": 0.62, \"total_time_s\": 1560, \"note\": \"v2 rescored with fixed radical+degree matcher; 0 changes. Dense baseline=0.52\"}, \"checkpoint_path\": \"/root/autodl-tmp/pacs/analysis_output/accuracy_eval_ds_s020.json\", \"log_path\": \"~/runs/phase-gated-compound-sparse/acc_ds_s020.log\", \"completed_at\": \"2026-05-15T21:20:03.642Z\"}, \"c2_accuracy_eval\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T20:44:33.644Z\", \"updated_at\": \"2026-05-15T21:17:27.151Z\", \"conclusion\": \"success\", \"spec\": {\"type\": \"eval\", \"hypothesis\": \"PPL-based severity gradient corresponds to actual accuracy degradation under compound sparsity\", \"description\": \"R9-C2: MATH-500 n=50 generation + accuracy evaluation under compound sparsity (DS/QW × dense/s015/s030)\", \"command\": \"python run_accuracy_eval.py\", \"server\": \"westd-22162\", \"data_path\": \"/root/autodl-tmp/pacs/data/math500.json\", \"data_count\": 50, \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B + Qwen2.5-7B-Instruct\", \"seed\": 42, \"checkpoint_source\": \"checkpoints/DeepSeek-R1-Distill-Qwen-7B + checkpoints/Qwen2.5-7B-Instruct\", \"eval_data\": \"MATH-500 n=50\"}, \"checkpoint_path\": \"/root/autodl-tmp/pacs/analysis_output/accuracy_eval_*.json\", \"log_path\": \"/root/autodl-tmp/pacs/analysis_output/accuracy_eval_ds_dense_n50.json\", \"completed_at\": \"2026-05-15T20:45:05.780Z\", \"metrics\": {\"n_problems\": 50, \"ds_dense_acc\": 0.52, \"ds_s015_acc\": 0.36, \"ds_s015_delta\": -0.16, \"ds_s030_acc\": 0.1, \"ds_s030_delta\": -0.42, \"qw_dense_acc\": 0.32, \"qw_s015_acc\": 0.34, \"qw_s015_delta\": 0.02, \"qw_s030_acc\": 0.14, \"qw_s030_delta\": -0.18, \"ds_s030_chinese_reasoning_rate\": 0.4, \"ds_dense_truncation_rate\": 0.56, \"note\": \"v2 rescored with fixed radical+degree matcher. DS s015 34→36, QW s015 32→34\"}}, \"acc_qw_s025\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T20:49:29.416Z\", \"updated_at\": \"2026-05-15T21:17:24.568Z\", \"spec\": {\"command\": \"python run_accuracy_eval.py --model Qwen2.5-7B-Instruct --conditions importance_s025 --num-problems 50\", \"server\": \"westd-22162\", \"gpu\": [\"cuda:3\"], \"pid\": \"274766\", \"log_path\": \"~/runs/phase-gated-compound-sparse/acc_qw_s025.log\", \"submitted_at\": \"2026-05-15T20:50:05.362Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/pacs/data/math500.json\", \"data_count\": 50, \"model_name\": \"Qwen2.5-7B-Instruct\", \"seed\": 42, \"type\": \"eval\", \"checkpoint_source\": \"checkpoints/Qwen2.5-7B-Instruct\", \"eval_data\": \"MATH-500 n=50\", \"wall_clock_seconds\": 875.0, \"gpu_hours\": 0.24}, \"reproduce\": {\"finished_at\": \"2026-05-15T21:00:56.427Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T21:01:01.626822+00:00\"}]}, \"metrics\": {\"qw_s025_acc\": 0.32, \"qw_s025_correct\": 16, \"qw_s025_total\": 50, \"qw_s025_delta_vs_dense\": 0, \"null_count\": 8, \"null_rate\": 0.16, \"output_truncated_count\": 2, \"output_truncated_rate\": 0.04, \"extraction_failure_count\": 6, \"extraction_failure_rate\": 0.12, \"wrong_count\": 26, \"wrong_rate\": 0.52, \"heads_pruned\": 196, \"total_time_s\": 559, \"note\": \"v2 rescored with fixed radical+degree matcher; 3 problems flipped (sqrt+degree)\"}, \"conclusion\": \"negative\", \"checkpoint_path\": \"/root/autodl-tmp/pacs/analysis_output/accuracy_eval_qw_s025.json\", \"completed_at\": \"2026-05-15T21:04:40.391Z\"}, \"acc_qw_s020\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T20:49:27.167Z\", \"updated_at\": \"2026-05-15T21:17:22.146Z\", \"spec\": {\"command\": \"python run_accuracy_eval.py --model Qwen2.5-7B-Instruct --conditions importance_s020 --num-problems 50\", \"server\": \"westd-22162\", \"gpu\": [\"cuda:2\"], \"pid\": \"274623\", \"log_path\": \"~/runs/phase-gated-compound-sparse/acc_qw_s020.log\", \"submitted_at\": \"2026-05-15T20:50:03.654Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/pacs/data/math500.json\", \"data_count\": 50, \"model_name\": \"Qwen2.5-7B-Instruct\", \"seed\": 42, \"type\": \"eval\", \"checkpoint_source\": \"checkpoints/Qwen2.5-7B-Instruct\", \"eval_data\": \"MATH-500 n=50\", \"wall_clock_seconds\": 878.3, \"gpu_hours\": 0.24}, \"reproduce\": {\"finished_at\": \"2026-05-15T21:00:49.632Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T21:00:52.877256+00:00\"}]}, \"metrics\": {\"qw_s020_acc\": 0.26, \"qw_s020_correct\": 13, \"qw_s020_total\": 50, \"qw_s020_delta_vs_dense\": -0.06, \"null_count\": 2, \"null_rate\": 0.04, \"output_truncated_count\": 2, \"output_truncated_rate\": 0.04, \"extraction_failure_count\": 0, \"extraction_failure_rate\": 0, \"wrong_count\": 35, \"wrong_rate\": 0.7, \"heads_pruned\": 140, \"total_time_s\": 598, \"note\": \"v2 rescored with fixed radical+degree matcher\"}, \"conclusion\": \"negative\", \"checkpoint_path\": \"/root/autodl-tmp/pacs/analysis_output/accuracy_eval_qw_s020.json\", \"completed_at\": \"2026-05-15T21:04:41.944Z\"}, \"think_phase_validation\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T19:35:06.395Z\", \"updated_at\": \"2026-05-15T19:35:45.955Z\", \"spec\": {\"type\": \"analysis\", \"hypothesis\": \"Attention sparsity tercile phase segmentation aligns with ground-truth &lt;think>/&lt;/think> CoT phase boundaries\", \"description\": \"R9-C1: Token-level comparison of sparsity-based phase assignment vs &lt;think> tag boundaries on GSM8K DS importance data\", \"command\": \"python analyze_think_phase_validation.py\", \"server\": \"westd-22162\", \"data_path\": \"/root/autodl-tmp/pacs/profiling_output_gsm8k_ds_imp_s015/generations.json\", \"data_count\": 48, \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B\", \"seed\": 42}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/pacs/analysis_output/think_phase_validation.json\", \"log_path\": \"/root/autodl-tmp/pacs/analysis_output/think_phase_validation.json\", \"completed_at\": \"2026-05-15T19:35:37.836Z\", \"metrics\": {\"effective_n\": 48, \"skipped_problems\": 2, \"median_kappa\": 0.887, \"thinking_in_low_sparsity_phase\": 0.578, \"answer_in_high_sparsity_phase\": 0.627, \"note\": \"Phase segmentation based on dense model — 4 sparsity conditions share identical phase boundaries, effective sample n=48 not n=192\"}}, \"gsm8k_profiling_qw\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T14:09:43.081Z\", \"updated_at\": \"2026-05-15T18:33:54.305Z\", \"hypothesis\": \"GSM8K profiling 验证 compound sparsity severity 的可迁移性：Qwen 在 GSM8K n=50 上是否复现 MATH-500 的 phase-gated II pattern（importance > random, 单调递增）\", \"server\": \"westd-22162\", \"gpu\": \"cuda:1\", \"account\": \"root\", \"reproduce\": {\"server\": \"westd-22162\", \"gpu\": \"cuda:1\", \"started_at\": \"2026-05-15T14:12:04.466Z\", \"finished_at\": \"2026-05-15T17:10:55.383Z\", \"training_hours\": 2.98}, \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=2,3 python run_profiling_gsm8k.py --model_path checkpoints/Qwen2.5-7B-Instruct --masking_method importance/random --data_path data/gsm8k_test.json --max_problems 50 --seed 42 --min_phase_length 10 --save_generations --sparsity_levels 0.15 0.20 0.25 0.30\", \"server\": \"westd-22162\", \"data_path\": \"/root/autodl-tmp/pacs/data/gsm8k_test.json\", \"data_count\": 50, \"model_name\": \"Qwen2.5-7B-Instruct\", \"seed\": 42, \"gpu\": \"cuda:2 (importance), cuda:3 (random)\", \"pid\": \"245313,245314\"}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/pacs/analysis_output/gsm8k/\", \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"completed_at\": \"2026-05-15T17:10:55.866Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-15T17:11:00.127072+00:00\"}]}, \"notes\": \"All QW outputs truncated at max_new_tokens=2047 (50/50 problems). Does not affect directional conclusions. rand_s030 per-sparsity data missing, merged data has aggregation bug.\", \"metrics\": {\"version\": \"v3_median\", \"n_problems\": 50, \"method\": \"median + Wilcoxon + bootstrap_median(B=10000)\", \"importance\": {\"s015\": {\"median_gradient\": 0.039}, \"s020\": {\"median_gradient\": 0.158}, \"s025\": {\"median_gradient\": 1.1}, \"s030\": {\"median_gradient\": 2.092}}, \"qw_rand_s030\": \"INVALID\"}}, \"gsm8k_profiling_ds\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T14:09:41.908Z\", \"updated_at\": \"2026-05-15T18:33:52.432Z\", \"hypothesis\": \"GSM8K profiling 验证 compound sparsity severity 的可迁移性：DeepSeek 在 GSM8K n=50 上是否复现 MATH-500 的 phase-gated II pattern（importance > random, 单调递增）\", \"server\": \"westd-22162\", \"gpu\": \"cuda:0\", \"account\": \"root\", \"reproduce\": {\"server\": \"westd-22162\", \"gpu\": \"cuda:0\", \"started_at\": \"2026-05-15T14:12:03.382Z\", \"finished_at\": \"2026-05-15T16:36:34.184Z\", \"training_hours\": 2.41}, \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0,1 python run_profiling_gsm8k.py --model_path checkpoints/DeepSeek-R1-Distill-Qwen-7B --masking_method importance/random --data_path data/gsm8k_test.json --max_problems 50 --seed 42 --min_phase_length 10 --save_generations --sparsity_levels 0.15 0.20 0.25 0.30\", \"server\": \"westd-22162\", \"data_path\": \"/root/autodl-tmp/pacs/data/gsm8k_test.json\", \"data_count\": 50, \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B\", \"seed\": 42, \"gpu\": \"cuda:0 (importance), cuda:1 (random)\", \"pid\": \"245311,245312\"}, \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T16:36:35.964Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-15T16:36:38.842679+00:00\"}]}, \"metrics\": {\"version\": \"v3_median\", \"n_problems\": 50, \"method\": \"median + Wilcoxon + bootstrap_median(B=10000)\", \"importance\": {\"s015\": {\"median_gradient\": 0.241, \"ci_low\": 0.077, \"ci_high\": 0.478, \"wilcoxon_p\": 0.0003}, \"s020\": {\"median_gradient\": 0.74, \"ci_low\": 0.314, \"ci_high\": 1.119, \"wilcoxon_p\": 0.0001}, \"s025\": {\"median_gradient\": 1.992, \"ci_low\": 0.933, \"ci_high\": 2.82, \"wilcoxon_p\": 0.0001}, \"s030\": {\"median_gradient\": 4.682, \"ci_low\": 2.121, \"ci_high\": 10.557, \"wilcoxon_p\": 0.0001}}, \"imp_rand_ratio\": {\"s015\": 2.3, \"s020\": 2.5, \"s025\": 3.8, \"s030\": 2.8}, \"dose_response_monotonic\": true}}, \"sf5_asymmetric_spot\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T10:59:35.784Z\", \"updated_at\": \"2026-05-15T18:20:37.200Z\", \"spec\": {\"type\": \"experiment\", \"hypothesis\": \"Phase-gated compound sparsity effect (II_low > II_high) is robust to asymmetric head/KV sparsity configurations. Total sparsity held at 25% (matching s025 symmetric baseline), varying only allocation between head and KV.\", \"description\": \"SF5: Asymmetric sparsity spot check. 2 configs: (head=0.20,KV=0.30) and (head=0.30,KV=0.20), compared against symmetric s025 (head=0.25,KV=0.25). n=50, DeepSeek only, importance-based. 4 conditions per config: dense/head-only/KV-only/compound. Pre-registered criterion: direction consistency of D=II_low-II_high.\", \"parent\": \"c2_n500_deepseek\", \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B\", \"data_count\": 50, \"server\": \"westd-22162\", \"command\": \"python run_sf5_asymmetric.py --config {A,B} --gpu {0,1}\", \"data_path\": \"/root/autodl-tmp/pacs/data/math500.json\", \"seed\": 42, \"conclusion_text\": \"asymmetric sparsity allocation does not significantly alter phase gradient magnitude; phase gating robust to head/KV ratio\"}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/pacs/profiling_output_sf5_h020_kv030/\", \"log_path\": \"/root/autodl-tmp/pacs/logs/sf5_config_A.log\", \"completed_at\": \"2026-05-15T18:10:47.705Z\", \"metrics\": {\"config_a_h02_kv03\": {\"II_low\": 19.51, \"II_mid\": 6.05, \"II_high\": 0.38, \"D\": 19.13}, \"config_b_h03_kv02\": {\"II_low\": 18.77, \"II_mid\": 3.97, \"II_high\": 0.52, \"D\": 18.25}, \"pre_registered_criterion_passed\": true, \"gradient_direction\": \"II_low >> II_mid >> II_high (consistent with symmetric baseline)\"}}, \"c2_qw_n500_r3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T19:26:53.700Z\", \"updated_at\": \"2026-05-15T08:40:33.785Z\", \"hypothesis\": \"C2 Qwen n=500 continuation (cron false positive on c2_qw_n500). s015 完成, s020-s030 remaining. 与 DeepSeek 对称验证 compound sparsity severity.\", \"parent\": \"c2_qw_n500\", \"spec\": {\"command\": \"run_profiling.py via screen c2_qw_gpu2/gpu3 (auto-continuation from c2_qw_n500)\", \"server\": \"westd-22162\", \"gpu\": \"cuda:2,cuda:3\", \"pid\": \"159269,159794\", \"data_path\": \"/root/autodl-tmp/pacs/data/MATH-500/\", \"data_count\": 500, \"model_name\": \"Qwen\", \"seed\": 42, \"checkpoint_source\": \"N/A (profiling, not training)\", \"eval_data\": \"MATH-500 n=500\", \"note\": \"s015 done (500/500 both imp+rand), s020 running (PID 159269 gpu2 imp, 159794 gpu3 rand). Screen: c2_qw_gpu2, c2_qw_gpu3. s025+s030 pending auto-advance.\"}, \"notes\": \"[2026-05-15] n=475 (low+high valid). [D066] Bonferroni revised: k=4 family-wise (was k=48). QW rand s025/s030 remain *** under k=4. BH-FDR also applied (48 tests). All imp conditions *** unchanged. Results in n500_unified_final.{csv,json}, n500_full_statistics.md.\", \"reproduce\": {\"finished_at\": \"2026-05-15T05:26:52.529Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T05:26:57.979865+00:00\"}]}, \"metrics\": {\"n_problems\": 500, \"effective_n\": 475, \"filter\": \"low+high valid only (mid-null allowed)\", \"mid_null_rate\": 0.452, \"imp_s015_median_ii\": 0.0659, \"imp_s015_ci\": [0.0492, 0.0925], \"imp_s015_wilcoxon_p\": 8.66e-15, \"imp_s015_bonf_p\": 3.46e-14, \"imp_s020_median_ii\": 0.3073, \"imp_s020_ci\": [0.2612, 0.3564], \"imp_s020_wilcoxon_p\": 6.84e-42, \"imp_s020_bonf_p\": 2.74e-41, \"imp_s025_median_ii\": 1.0745, \"imp_s025_ci\": [0.9766, 1.1787], \"imp_s025_wilcoxon_p\": 1.06e-68, \"imp_s025_bonf_p\": 4.25e-68, \"imp_s030_median_ii\": 3.155, \"imp_s030_ci\": [2.7834, 3.5582], \"imp_s030_wilcoxon_p\": 9.21e-74, \"imp_s030_bonf_p\": 3.69e-73, \"rand_s015_median_ii\": -0.0111, \"rand_s015_wilcoxon_p\": 0.172, \"rand_s015_bonf_p\": 0.687, \"rand_s020_median_ii\": 0.0153, \"rand_s020_wilcoxon_p\": 0.2, \"rand_s020_bonf_p\": 0.8, \"rand_s025_median_ii\": 0.3931, \"rand_s025_wilcoxon_p\": 1.59e-11, \"rand_s025_bonf_p\": 6.37e-11, \"rand_s025_fdr_p\": 2.63e-11, \"rand_s030_median_ii\": 0.9127, \"rand_s030_wilcoxon_p\": 2.92e-15, \"rand_s030_bonf_p\": 1.17e-14, \"rand_s030_fdr_p\": 5.61e-15, \"dz_s015_s020\": -0.629, \"dz_s020_s025\": -0.865, \"dz_s025_s030\": -0.767, \"dz_s015_s030\": -0.923, \"all_dz_reliable\": true, \"dose_response_monotonic\": true, \"dose_response_spearman_rho\": 1, \"dose_response_perm_p\": 0.0417, \"imp_rand_ratio_range\": \"2.7-20.1x\", \"bonferroni_k\": 4, \"bonferroni_note\": \"Bonferroni k=4 family-wise (D066 revision)\"}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/pacs/analysis_n500_results.json\", \"log_path\": \"/root/autodl-tmp/pacs/analysis_output/n500_unified_final.json\", \"completed_at\": \"2026-05-15T07:59:38.153Z\"}, \"c2_n500_deepseek\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T13:33:50.628Z\", \"updated_at\": \"2026-05-15T08:40:22.196Z\", \"hypothesis\": \"C2 statistical power boost: 将 DeepSeek 8 conditions (imp/rand × 4 sparsity) 从 n=50 扩到 n=500，提升统计功效。预注册：若 QW s015 在 n=500 后 CI 仍跨零，论文叙事改为 \\\"compound effect emerges above a threshold sparsity level (~s020)\\\"\", \"spec\": {\"hypothesis\": \"C2: n=500 统计功效提升。将 DeepSeek 8 conditions (imp/rand × 4 sparsity) 从 n=50 扩到 n=500 (full MATH-500)，验证现有结论在大样本下是否稳健。\", \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B\", \"data_path\": \"/root/autodl-tmp/pacs/data/math500.json\", \"data_count\": 500, \"server\": \"westd-22162\", \"command\": \"bash run_c2_n500_gpu0.sh + bash run_c2_n500_gpu1.sh\", \"seed\": 42, \"gpu_ids\": [\"cuda:0\", \"cuda:1\"], \"tmux_sessions\": [\"c2_n500_gpu0\", \"c2_n500_gpu1\"], \"conditions\": [\"imp_s015\", \"imp_s020\", \"imp_s025\", \"imp_s030\", \"rand_s015\", \"rand_s020\", \"rand_s025\", \"rand_s030\"], \"dtype\": \"bfloat16\", \"estimated_wall_clock_hours\": 20, \"pre_registration\": \"PRE_REGISTRATION_C2.md\"}, \"server\": \"westd-22162\", \"gpu\": \"cuda:0,cuda:1\", \"notes\": \"[2026-05-15] ALL 8 CONDITIONS DONE (500/500). [D066] Bonferroni revised: k=4 family-wise (was k=48). DS rand s025 bonf_p=0.0058 (**), s030 bonf_p=0.0059 (**) — both restored to significant. BH-FDR also applied (48 tests): rand s025/s030 fdr_p=0.0019. Results in n500_unified_final.{csv,json}.\", \"log_path\": \"/root/autodl-tmp/pacs/logs/c2_n500_gpu0_full.log, /root/autodl-tmp/pacs/logs/c2_n500_gpu1_full.log\", \"metrics\": {\"n_problems\": 500, \"effective_n\": 496, \"mid_null_rate\": 0.102, \"imp_s015_median_ii\": 0.3907, \"imp_s015_ci\": [0.3496, 0.4431], \"imp_s015_wilcoxon_p\": 1.27e-70, \"imp_s020_median_ii\": 1.2149, \"imp_s020_ci\": [1.1072, 1.3365], \"imp_s020_wilcoxon_p\": 3.98e-75, \"imp_s025_median_ii\": 3.9857, \"imp_s025_ci\": [3.5272, 4.3588], \"imp_s025_wilcoxon_p\": 1.99e-78, \"imp_s030_median_ii\": 8.4813, \"imp_s030_ci\": [7.7543, 9.6919], \"imp_s030_wilcoxon_p\": 1.09e-79, \"rand_s015_median_ii\": 0.0139, \"rand_s015_wilcoxon_p\": 0.863, \"rand_s020_median_ii\": 0.0315, \"rand_s020_wilcoxon_p\": 0.28, \"rand_s025_median_ii\": 0.2574, \"rand_s025_bonf_p\": 0.005839, \"rand_s025_fdr_p\": 0.001914, \"rand_s030_median_ii\": 0.5096, \"rand_s030_bonf_p\": 0.005903, \"rand_s030_fdr_p\": 0.001914, \"dz_s015_s020\": -0.925, \"dz_s020_s025\": -0.824, \"dz_s025_s030\": -0.773, \"dz_s015_s030\": -0.944, \"all_dz_reliable\": true, \"dose_response_monotonic\": true, \"dose_response_spearman_rho\": 1, \"dose_response_perm_p\": 0.0417, \"imp_rand_ratio_range\": \"15.5-38.6x\", \"bonferroni_k\": 4, \"bonferroni_note\": \"Bonferroni k=4 family-wise (D066 revision)\"}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/pacs/analysis_n500_results.json\", \"completed_at\": \"2026-05-15T07:59:37.120Z\"}, \"c2_qw_n500\": {\"status\": \"DONE\", \"retry_count\": 2, \"created_at\": \"2026-05-14T13:34:05.213Z\", \"updated_at\": \"2026-05-14T19:26:11.742Z\", \"hypothesis\": \"C2: Qwen n=500 统计功效提升。将 Qwen 8 conditions (imp/rand × 4 sparsity) 从 n=50 扩到 n=500，与 DeepSeek 对称验证。\", \"notes\": \"2026-05-15T03:30: Cron false positive corrected. Process alive on GPU 2+3. s015 COMPLETE (500/500 both conditions, results in profiling_results.json). s020 RUNNING: qw_imp_s020 PID159269 cuda:2, qw_rand_s020 PID159794 cuda:3. Screen session auto-advances through sparsity levels. n=500 s015 analysis: both DeepSeek and Qwen paired gradient now significant (Bonferroni p<0.0001), resolving D058.\", \"reproduce\": {\"finished_at\": \"2026-05-14T19:20:41.163Z\"}, \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"completed_at\": \"2026-05-14T14:13:26.223Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-14T14:13:28.582987+00:00\"}, {\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-14T14:36:44.123761+00:00\"}, {\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-14T19:21:16.126614+00:00\"}], \"previous_failure\": {\"conclusion\": \"failed\", \"notes\": \"Status corrected: cron false positive (profiling无W&B/sentinel, 输出在完成后才写盘). 实验从未中断. PID 131864/132002 正常运行, 进度~49/500 s015. SEED=42 hardcoded. ETA ~02:00 CST.\"}}, \"spec\": {\"command\": \"run_profiling.py via screen c2_qw_gpu2/gpu3\", \"server\": \"westd-22162\", \"gpu\": \"cuda:2,cuda:3\", \"pid\": \"131864,132002\", \"data_path\": \"MATH-500\", \"data_count\": 500, \"model_name\": \"Qwen\", \"seed\": 42, \"note\": \"3rd cron false positive corrected. PID 131864 (gpu2 imp) / 132002 (gpu3 rand). Progress: imp 93/500 s015, rand 98/500 s015 as of 22:37 CST. 8 conditions total (imp/rand x s015/s020/s025/s030). Running in SCREEN sessions not tmux.\"}, \"conclusion\": \"failed\"}, \"c5b_pilot\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T14:51:04.044Z\", \"updated_at\": \"2026-05-14T19:10:56.005Z\", \"hypothesis\": \"C5b mitigation pilot: oracle (真实 phase labels) + heuristic (token position ratio) phase-aware sparsity allocation 能否恢复 compound interaction severity。Gate: oracle recovery >30% at s025 or s030。\", \"notes\": \"s025 30/30 完成（GPU3 run）。Gate FAIL: oracle recovery +18.0% < 30% threshold。Heuristic recovery +31.7%。s030 未完成（SSH 断连 kill）。Cron 误判为 failed（无 sentinel/W&B），实际 s025 结果完整。结果路径: profiling_output_c5b_all_s025/mitigation_pilot_results.json。Framing 提案: C5b → §8 Future Work open question。\", \"spec\": {\"gpu\": \"cuda:3\", \"pid\": 154645}, \"reproduce\": {\"finished_at\": \"2026-05-14T18:28:25.169Z\"}, \"failure_reason\": \"oracle recovery 18% < 30% gate; heuristic 32% CI crosses zero. Scientific gate_failed, not technical failure. D057:降为 future work, 不再 retry.\", \"conclusion\": \"negative\", \"completed_at\": \"2026-05-14T18:28:26.509Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-14T18:28:28.736533+00:00\"}]}, \"metrics\": {\"s025_uniform_median_ii\": 1.0435, \"s025_oracle_median_ii\": 0.856, \"s025_oracle_recovery_pct\": 18, \"s025_oracle_recovery_ci\": [-39, 45.8], \"s025_oracle_wilcoxon_p\": 0.0021, \"s025_heuristic_median_ii\": 0.7127, \"s025_heuristic_recovery_pct\": 31.7, \"s025_heuristic_recovery_ci\": [-22.8, 66], \"s025_heuristic_wilcoxon_p\": 0.0236, \"gate_criterion\": \"oracle_recovery > 30%\", \"gate_result\": \"FAIL\", \"s030_status\": \"not_completed\", \"n_problems\": 30}}, \"c3_llama\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T13:34:06.637Z\", \"updated_at\": \"2026-05-14T17:58:54.638Z\", \"hypothesis\": \"C3: LLaMA 架构验证。用 DeepSeek-R1-Distill-Llama-8B 验证 phase-modulated compound severity 是否跨架构复现（Qwen2ForCausalLM → LlamaForCausalLM），回应审稿人\\\"cross-model ≠ cross-architecture\\\"质疑。\", \"spec\": {\"command\": \"bash run_c3_llama_full.sh\", \"server\": \"westd-22162\", \"data_path\": \"/root/autodl-tmp/pacs/data/math500.json\", \"data_count\": 50, \"model_name\": \"DeepSeek-R1-Distill-Llama-8B\", \"seed\": null, \"gpu\": \"cuda:2,cuda:3\", \"pid\": \"138393 (parent), 138408 (importance gpu2), 138410 (random gpu3)\", \"note\": \"sp_str bug fixed: bc unavailable → python3. Old s000 output deleted (12/50 incomplete). All 8 conditions restarting from scratch.\", \"pids\": {\"importance_gpu2\": 138408, \"random_gpu3\": 138410, \"parent\": 138398}, \"conditions\": \"importance×{0.15,0.20,0.25,0.30} + random×{0.15,0.20,0.25,0.30}\", \"gpu_allocation\": \"GPU2=importance, GPU3=random\"}, \"notes\": \"8/8 conditions complete. Analysis output: analysis_output/c3_llama_{results,cohens_d,report}.*. Phase gradient d_z monotonically increasing (0.19→0.26→0.29→0.34). Cross-architecture pattern confirmed: LLaMA shows large phase gradient d_z ~1.0 across all sparsity levels, consistent qualitative direction with DeepSeek/Qwen. s030 Wilcoxon significant (p=0.029 Bonferroni). s015 median diff CI [0.002, 0.043] does not cross zero.\", \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/pacs/profiling_output_c3_llama_{importance,random}_s{015,020,025,030}\", \"log_path\": \"/root/autodl-tmp/pacs/logs/c3_llama_{importance,random}_s{015,020,025,030}.log\", \"completed_at\": \"2026-05-14T17:57:09.264Z\"}, \"c2_ds_n500\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T13:34:03.705Z\", \"updated_at\": \"2026-05-14T15:37:18.213Z\", \"hypothesis\": \"C2: n=500 统计功效提升。将 DeepSeek 8 conditions (imp/rand × 4 sparsity) 从 n=50 扩到 n=500 (full MATH-500)，验证现有结论在大样本下是否稳健。预注册：若 QW s015 CI 仍跨零，改叙事为 threshold sparsity ~s020。\", \"notes\": \"DUPLICATE — 勿跑。实际实验在 c2_n500_deepseek (RUNNING)。Director 指令清理。\", \"conclusion\": \"killed\", \"completed_at\": \"2026-05-14T15:37:18.214Z\"}, \"c3_llama_arch\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T13:33:52.384Z\", \"updated_at\": \"2026-05-14T15:37:16.970Z\", \"hypothesis\": \"C3 architecture validation: 在 DeepSeek-R1-Distill-Llama-8B 上复现 phase-modulated compound severity，验证 finding 不限于 Qwen2 架构\", \"conclusion\": \"killed\", \"notes\": \"DUPLICATE — 勿跑。实际实验在 c3_llama (PREPARING)。Director 指令清理。\", \"completed_at\": \"2026-05-14T15:37:16.970Z\"}, \"bf16_qw_imp_s035\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T09:05:19.126Z\", \"updated_at\": \"2026-05-14T09:36:45.921Z\", \"spec\": {\"hypothesis\": \"Extended sparsity range: Qwen importance s=0.35, 扩展 dose-response 到 [0.10, 0.35]，加固 C2+C5 cross-model\", \"model_name\": \"Qwen2.5-7B-Instruct\", \"data_path\": \"/root/autodl-tmp/pacs/data/math500.json\", \"data_count\": 50, \"server\": \"westd-22162\", \"parent\": \"bf16_qw_imp_s030\", \"claims\": [\"C2\", \"C5\"], \"seed\": 42, \"command\": \"python -m pacs.profiling.run_profiling --model_path /root/autodl-tmp/pacs/checkpoints/Qwen2.5-7B-Instruct --data_path /root/autodl-tmp/pacs/data/math500.json --output_dir /root/autodl-tmp/pacs/profiling_output_bf16_qw_imp_s035 --sparsity_levels 0.35 --masking_method importance --max_new_tokens 2048 --min_phase_length 10 --max_problems 50\", \"gpu_ids\": [\"cuda:1\"], \"pid\": 104097}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/pacs/profiling_output_bf16_qw_imp_s035/profiling_results.json\", \"log_path\": \"none\", \"completed_at\": \"2026-05-14T09:36:38.700Z\", \"metrics\": {\"n_problems\": 50, \"overall_verdict\": \"PASS\", \"ci_overlap_test\": \"PASS\", \"sign_reversal_test\": \"FAIL\", \"high_sparsity_II_median\": 0.0232, \"high_sparsity_II_median_CI\": [0.0154, 0.0383], \"high_sparsity_II_mean\": 0.1643, \"high_sparsity_II_mean_CI\": [0.0844, 0.2495], \"low_sparsity_II_median\": 8.2358, \"low_sparsity_II_median_CI\": [6.1564, 10.9231], \"low_sparsity_II_mean\": 18.9673, \"low_sparsity_II_mean_CI\": [14.5015, 23.9752], \"mid_sparsity_II_median\": 0.9577, \"mid_sparsity_II_median_CI\": [0.171, 3.5575], \"mid_sparsity_II_mean\": 8.0734, \"mid_sparsity_II_mean_CI\": [2.0224, 16.8946], \"ppl_high_dense\": 1.0738, \"ppl_high_both\": 2.3435, \"ppl_low_dense\": 1.1518, \"ppl_low_both\": 58.0358, \"ppl_mid_dense\": 1.1327, \"ppl_mid_both\": 20.9912, \"high_sparsity_tokens\": 16289, \"low_sparsity_tokens\": 32227, \"mid_sparsity_tokens\": 4372}}, \"bf16_qw_imp_s010\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T09:05:17.329Z\", \"updated_at\": \"2026-05-14T09:34:13.001Z\", \"spec\": {\"hypothesis\": \"Extended sparsity range: Qwen importance s=0.10, 扩展 dose-response 到 [0.10, 0.35]，加固 C2+C5 cross-model\", \"model_name\": \"Qwen2.5-7B-Instruct\", \"data_path\": \"/root/autodl-tmp/pacs/\", \"data_count\": 50, \"server\": \"westd-22162\", \"parent\": \"bf16_qw_imp_s015\", \"claims\": [\"C2\", \"C5\"], \"command\": \"run_profiling bf16_qw_imp_s010\", \"seed\": 42, \"pid\": \"102928\", \"gpu\": [\"cuda:3\"], \"tmux_session\": \"bf16_qw_imp_s010\"}, \"checkpoint_path\": \"/root/autodl-tmp/pacs/profiling_output_bf16_qw_imp_s010/profiling_results.json\", \"log_path\": \"/root/autodl-tmp/pacs/logs/bf16_qw_imp_s010.log\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-14T09:34:09.393Z\", \"metrics\": {\"n_problems\": 50, \"overall_verdict\": \"PASS\", \"ci_overlap_test\": \"PASS\", \"sign_reversal_test\": \"FAIL\", \"high_sparsity_II_median\": 0.0001, \"high_sparsity_II_median_CI\": [-0.0028, 0.0005], \"high_sparsity_II_mean\": -0.0887, \"high_sparsity_II_mean_CI\": [-0.1235, -0.0591], \"low_sparsity_II_median\": -0.0444, \"low_sparsity_II_median_CI\": [-0.0967, -0.0152], \"low_sparsity_II_mean\": -0.2431, \"low_sparsity_II_mean_CI\": [-0.3817, -0.1202], \"mid_sparsity_II_median\": -0.0359, \"mid_sparsity_II_median_CI\": [-0.0963, -0.015], \"mid_sparsity_II_mean\": -0.084, \"mid_sparsity_II_mean_CI\": [-0.1366, -0.035], \"ppl_high_dense\": 1.074, \"ppl_high_both\": 1.228, \"ppl_low_dense\": 1.152, \"ppl_low_both\": 3.204, \"ppl_mid_dense\": 1.133, \"ppl_mid_both\": 1.741}}, \"bf16_ds_imp_s035\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T09:05:14.440Z\", \"updated_at\": \"2026-05-14T09:33:42.015Z\", \"spec\": {\"hypothesis\": \"Extended sparsity range: DeepSeek importance s=0.35, 扩展 dose-response 到 [0.10, 0.35]，加固 C2 单调递增 claim\", \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B\", \"data_path\": \"/root/autodl-tmp/pacs/data/math500.json\", \"data_count\": 50, \"server\": \"westd-22162\", \"parent\": \"bf16_importance_s030\", \"claims\": [\"C2\"], \"command\": \"python -m pacs.profiling.run_profiling --model_path /root/autodl-tmp/pacs/checkpoints/DeepSeek-R1-Distill-Qwen-7B --data_path /root/autodl-tmp/pacs/data/math500.json --output_dir /root/autodl-tmp/pacs/profiling_output_bf16_ds_imp_s035 --sparsity_levels 0.35 --masking_method importance --max_new_tokens 2048 --min_phase_length 10 --max_problems 50\", \"seed\": 42, \"pid\": \"102789\", \"gpu\": [\"cuda:2\"], \"tmux_session\": \"bf16_ds_imp_s035\"}, \"conclusion\": \"success\", \"log_path\": \"/root/autodl-tmp/pacs/logs/bf16_ds_imp_s035.log\", \"checkpoint_path\": \"/root/autodl-tmp/pacs/profiling_output_bf16_ds_imp_s035/profiling_results.json\", \"completed_at\": \"2026-05-14T09:33:31.457Z\", \"metrics\": {\"verdict\": \"PASS\", \"problems\": 50, \"II_high_sparsity_median\": 0.1051, \"II_high_sparsity_mean\": 1.4309, \"II_low_sparsity_median\": 28.7649, \"II_low_sparsity_mean\": 104.1892, \"II_mid_sparsity_median\": 4.9542, \"II_mid_sparsity_mean\": 20.326, \"high_sparsity_tokens\": 21086, \"low_sparsity_tokens\": 27748, \"mid_sparsity_tokens\": 13306, \"ci_overlap_test\": \"low_sparsity vs mid_sparsity CI non-overlapping at 0.35\"}}, \"bf16_ds_imp_s010\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T09:05:11.694Z\", \"updated_at\": \"2026-05-14T09:33:38.904Z\", \"spec\": {\"hypothesis\": \"Extended sparsity range: DeepSeek importance s=0.10, 扩展 dose-response 到 [0.10, 0.35]，加固 C2 单调递增 claim\", \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B\", \"data_path\": \"/root/autodl-tmp/pacs/data/math500.json\", \"data_count\": 50, \"server\": \"westd-22162\", \"parent\": \"bf16_importance_s015\", \"claims\": [\"C2\"], \"command\": \"python -m pacs.profiling.run_profiling --model_path /root/autodl-tmp/pacs/checkpoints/DeepSeek-R1-Distill-Qwen-7B --data_path /root/autodl-tmp/pacs/data/math500.json --output_dir /root/autodl-tmp/pacs/profiling_output_bf16_ds_imp_s010 --sparsity_levels 0.10 --masking_method importance --max_new_tokens 2048 --min_phase_length 10 --max_problems 50\", \"seed\": 42, \"pid\": \"102651\", \"gpu\": [\"cuda:0\"], \"tmux_session\": \"bf16_ds_imp_s010\"}, \"conclusion\": \"negative\", \"log_path\": \"/root/autodl-tmp/pacs/logs/bf16_ds_imp_s010.log\", \"checkpoint_path\": \"/root/autodl-tmp/pacs/profiling_output_bf16_ds_imp_s010/profiling_results.json\", \"completed_at\": \"2026-05-14T09:33:29.982Z\", \"metrics\": {\"verdict\": \"FAIL\", \"problems\": 50, \"II_high_sparsity_median\": 0.0027, \"II_high_sparsity_mean\": -0.1998, \"II_low_sparsity_median\": 0.0151, \"II_low_sparsity_mean\": -0.1066, \"II_mid_sparsity_median\": 0.0061, \"II_mid_sparsity_mean\": -0.0131, \"high_sparsity_tokens\": 21086, \"low_sparsity_tokens\": 27748, \"mid_sparsity_tokens\": 13306}}, \"qwen_c4_entropy\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T08:44:17.868Z\", \"updated_at\": \"2026-05-14T09:16:14.626Z\", \"hypothesis\": \"C4 cross-model 验证：用 Qwen2.5-7B-Instruct 重跑 c4_attention_entropy，测量 head pruning 对 attention entropy 和 KV importance discrimination 的影响。与 DeepSeek 版本配置完全一致（s015-s030, importance+random, 30 problems），验证 entropy/Gini/CV 效应的跨模型一致性。\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/pacs && python c4_attention_entropy.py --model_path /root/autodl-tmp/pacs/checkpoints/Qwen2.5-7B-Instruct --output_dir /root/autodl-tmp/pacs/results/c4_attention_entropy_qwen --gpu 0\\\"\", \"server\": \"westd-22162\", \"gpu\": [\"cuda:1\"], \"pid\": \"100538\", \"log_path\": \"~/runs/phase-gated-compound-sparse/qwen_c4_entropy.log\", \"submitted_at\": \"2026-05-14T08:47:00.349Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/pacs/data/math500.json\", \"data_count\": 30, \"model_name\": \"Qwen2.5-7B-Instruct\", \"seed\": 42, \"output_path\": \"/root/autodl-tmp/pacs/results/c4_attention_entropy_qwen/c4_entropy_results.json\", \"sparsity_levels\": [0.15, 0.2, 0.25, 0.3], \"dtype\": \"bf16\", \"masking_methods\": [\"importance\", \"random\"], \"metrics_measured\": [\"attention_entropy_delta\", \"kv_importance_gini_delta\", \"cv_delta\"], \"wall_clock_seconds\": 1479.2, \"gpu_hours\": 0.41}, \"reproduce\": {\"finished_at\": \"2026-05-14T09:05:06.080Z\"}, \"conclusion\": \"negative\", \"metrics\": {\"problems_completed\": 30, \"qwen_importance_entropy_delta\": {\"s015\": -0.0733, \"s020\": -0.0759, \"s025\": 0.0451, \"s030\": -0.0072}, \"qwen_random_entropy_delta\": {\"s015\": 0.0838, \"s020\": 0.0901, \"s025\": 0.2168, \"s030\": 0.1968}, \"qwen_importance_gini_delta\": {\"s015\": -0.0103, \"s020\": -0.0121, \"s025\": -0.01, \"s030\": -0.0202}, \"qwen_random_gini_delta\": {\"s015\": -0.0186, \"s020\": -0.0229, \"s025\": -0.0337, \"s030\": -0.0448}, \"qwen_importance_cv_delta\": {\"s015\": -0.045, \"s020\": -0.208, \"s025\": -1.491, \"s030\": -1.142}, \"qwen_random_cv_delta\": {\"s015\": -0.778, \"s020\": -0.889, \"s025\": -1.5, \"s030\": -1.677}, \"cross_model_notes\": \"random entropy increase consistent; importance entropy collapse inconsistent at s025 (reversed to +0.045) and near-zero at s030; gini/cv directions consistent but Qwen magnitudes smaller\"}, \"checkpoint_path\": \"/root/autodl-tmp/pacs/results/c4_attention_entropy_qwen/c4_entropy_results.json\", \"completed_at\": \"2026-05-14T09:11:39.554Z\", \"notes\": \"Cross-model C4 验证 negative: random entropy increase 跨模型一致，但 importance entropy collapse 在 Qwen 不稳健（s025 方向反转 +0.0451 vs DeepSeek -0.0446, s030 接近零）。Gini/CV 方向一致但幅度差异大。不支持 entropy-discrimination collapse 的强跨模型普适性。\"}, \"bf16_qw_rand_s030\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T05:39:37.271Z\", \"updated_at\": \"2026-05-14T09:10:19.234Z\", \"hypothesis\": \"D020 bf16 全量重跑: Qwen2.5-7B-Instruct random masking s=0.30, bf16 dtype. Cross-model 配对对照。\", \"server\": \"westd-22162\", \"gpu\": \"cuda:0\", \"account\": \"root\", \"reproduce\": {\"server\": \"westd-22162\", \"gpu\": \"cuda:0\", \"started_at\": \"2026-05-14T08:22:08.391Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/pacs && python -m pacs.profiling.run_profiling --model_path /root/autodl-tmp/pacs/checkpoints/Qwen2.5-7B-Instruct --data_path /root/autodl-tmp/pacs/data/math500.json --output_dir /root/autodl-tmp/pacs/profiling_output_bf16_qw_rand_s030 --sparsity_levels 0.30 --masking_method random --max_new_tokens 2048 --min_phase_length 10 --max_problems 50\\\"\", \"code_commit\": \"1b4f61aa366a9fe320f8563c8f7acb5af58d78b7\", \"finished_at\": \"2026-05-14T08:42:12.294Z\", \"training_hours\": 0.33}, \"spec\": {\"data_path\": \"/root/autodl-tmp/pacs/data/math500.json\", \"data_count\": 50, \"model_name\": \"Qwen2.5-7B-Instruct\", \"seed\": null}, \"pid\": \"98285\", \"log_path\": \"~/runs/phase-gated-compound-sparse/bf16_qw_rand_s030.log\", \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T08:42:18.234440+00:00\"}]}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/pacs/profiling_output_bf16_qw_rand_s030\", \"metrics\": {\"median_high\": 4.200557, \"median_mid\": 6.477036, \"median_low\": 8.065662, \"median_diff\": 2.418272, \"permutation_p\": 0.012, \"cohens_d\": -0.03513, \"wilcoxon_p\": 0.01566, \"bootstrap_ci_low\": 0.241897, \"bootstrap_ci_high\": 3.314824}, \"completed_at\": \"2026-05-14T08:46:56.207Z\", \"pass_fail\": \"FAIL\", \"notes\": \"D043 更新: B=10000 per-problem re-bootstrap 确认 PASS→FAIL。gradient CI [-1.54, 13.71] 包含 0, p=0.111。原 B=1000 段级 bootstrap 的窄 CI 导致假阳性。Cohen's d ≈ 0。Random masking 现在 8/8 FAIL（两模型一致）。\"}, \"bf16_qw_imp_s030\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T05:39:33.640Z\", \"updated_at\": \"2026-05-14T09:09:09.394Z\", \"hypothesis\": \"D020 bf16 全量重跑: Qwen2.5-7B-Instruct importance masking s=0.30, bf16 dtype. Cross-model replication。\", \"spec\": {\"command\": \"python -m pacs.profiling.run_profiling --model_path checkpoints/Qwen2.5-7B-Instruct --sparsity_levels 0.30 --masking_method importance --max_problems 50\", \"server\": \"westd-22162\", \"data_path\": \"/root/autodl-tmp/pacs/data/math500.json\", \"data_count\": 50, \"model_name\": \"Qwen2.5-7B-Instruct\", \"seed\": 42}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/pacs/profiling_output_bf16_qw_imp_s030\", \"log_path\": \"~/runs/phase-gated-compound-sparse/bf16_qw_imp_s030.log\", \"metrics\": {\"median_difference\": 2.619385, \"permutation_p\": 0, \"cohens_d\": 1.4394, \"bootstrap_ci_95\": [1.722281, 3.651063], \"wilcoxon_p\": 0, \"n_bootstrap\": 10000, \"n_paired\": 46}, \"notes\": \"Qwen2.5-7B importance s=0.30, PASS. Median II gradient: high≈0.010 → mid≈0.688 → low≈2.953. PPL(both): high=1.86 → mid=9.48 → low=35.32. CI non-overlapping (low vs mid). 最强 gradient，完全复现 DeepSeek 模式。\", \"completed_at\": \"2026-05-14T07:58:16.426Z\"}, \"bf16_qw_imp_s025\": {\"status\": \"DONE\", \"retry_count\": 1, \"created_at\": \"2026-05-14T05:39:32.680Z\", \"updated_at\": \"2026-05-14T09:09:07.649Z\", \"hypothesis\": \"D020 bf16 全量重跑: Qwen2.5-7B-Instruct importance masking s=0.25, bf16 dtype. Cross-model replication。\", \"server\": \"westd-22162\", \"gpu\": \"cuda:3\", \"account\": \"root\", \"reproduce\": {\"server\": \"westd-22162\", \"gpu\": \"cuda:3\", \"started_at\": \"2026-05-14T07:01:54.691Z\", \"finished_at\": \"2026-05-14T07:02:51.598Z\", \"training_hours\": 0.02}, \"failure_reason\": \"\", \"completed_at\": \"2026-05-14T07:02:55.553Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-14T07:02:58.934095+00:00\"}], \"previous_failure\": {\"conclusion\": \"failed\", \"notes\": \"Qwen2.5-7B-Instruct checkpoint not found on server, 待下载后重跑\"}}, \"notes\": \"Qwen2.5-7B importance s=0.25, PASS. Median II gradient: high≈0.003 → mid≈0.114 → low≈1.271. PPL(both): high=1.54 → mid=5.36 → low=16.96. CI non-overlapping (low vs mid). 强 gradient，mid phase 开始显著。\", \"spec\": {\"command\": \"python -m pacs.profiling.run_profiling --model_path checkpoints/Qwen2.5-7B-Instruct --sparsity_levels 0.25 --masking_method importance --max_problems 50\", \"server\": \"westd-22162\", \"data_path\": \"/root/autodl-tmp/pacs/data/math500.json\", \"data_count\": 50, \"model_name\": \"Qwen2.5-7B-Instruct\", \"seed\": 42}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/pacs/profiling_output_bf16_qw_imp_s025\", \"log_path\": \"~/runs/phase-gated-compound-sparse/bf16_qw_imp_s025.log\", \"metrics\": {\"median_difference\": 1.108706, \"permutation_p\": 0, \"cohens_d\": 1.2329, \"bootstrap_ci_95\": [0.609247, 1.469002], \"wilcoxon_p\": 0, \"n_bootstrap\": 10000, \"n_paired\": 46}}, \"bf16_qw_imp_s020\": {\"status\": \"DONE\", \"retry_count\": 1, \"created_at\": \"2026-05-14T05:39:31.824Z\", \"updated_at\": \"2026-05-14T09:09:03.210Z\", \"hypothesis\": \"D020 bf16 全量重跑: Qwen2.5-7B-Instruct importance masking s=0.20, bf16 dtype. Cross-model replication。\", \"server\": \"westd-22162\", \"gpu\": \"cuda:2\", \"account\": \"root\", \"reproduce\": {\"server\": \"westd-22162\", \"gpu\": \"cuda:2\", \"started_at\": \"2026-05-14T07:01:50.969Z\", \"finished_at\": \"2026-05-14T07:02:06.576Z\", \"training_hours\": 0.0}, \"failure_reason\": \"\", \"completed_at\": \"2026-05-14T07:02:11.652Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-14T07:02:16.508561+00:00\"}], \"previous_failure\": {\"conclusion\": \"failed\", \"notes\": \"Qwen2.5-7B-Instruct checkpoint not found on server, 待下载后重跑\"}}, \"notes\": \"Qwen2.5-7B importance s=0.20, PASS. Median II gradient: high≈-0.000 → mid≈0.002 → low≈0.235. PPL(both): high=1.37 → mid=3.43 → low=9.20. CI non-overlapping (low vs mid). Low phase II 明显抬升，PPL gradient 加剧。\", \"spec\": {\"command\": \"python -m pacs.profiling.run_profiling --model_path checkpoints/Qwen2.5-7B-Instruct --sparsity_levels 0.20 --masking_method importance --max_problems 50\", \"server\": \"westd-22162\", \"data_path\": \"/root/autodl-tmp/pacs/data/math500.json\", \"data_count\": 50, \"model_name\": \"Qwen2.5-7B-Instruct\", \"seed\": 42}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/pacs/profiling_output_bf16_qw_imp_s020\", \"log_path\": \"~/runs/phase-gated-compound-sparse/bf16_qw_imp_s020.log\", \"metrics\": {\"median_difference\": 0.207511, \"permutation_p\": 0, \"cohens_d\": 0.7224, \"bootstrap_ci_95\": [0.067222, 0.40226], \"wilcoxon_p\": 3.4e-05, \"n_bootstrap\": 10000, \"n_paired\": 46}}, \"bf16_qw_imp_s015\": {\"status\": \"DONE\", \"retry_count\": 1, \"created_at\": \"2026-05-14T05:39:31.289Z\", \"updated_at\": \"2026-05-14T09:09:00.065Z\", \"hypothesis\": \"D020 bf16 全量重跑: Qwen2.5-7B-Instruct importance masking s=0.15, bf16 dtype. Cross-model replication。\", \"server\": \"westd-22162\", \"gpu\": \"cuda:1\", \"account\": \"root\", \"reproduce\": {\"server\": \"westd-22162\", \"gpu\": \"cuda:1\", \"started_at\": \"2026-05-14T07:01:46.764Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/pacs && python -m pacs.profiling.run_profiling --model_path /root/autodl-tmp/pacs/checkpoints/Qwen2.5-7B-Instruct --data_path /root/autodl-tmp/pacs/data/math500.json --output_dir /root/autodl-tmp/pacs/profiling_output_bf16_qw_imp_s015 --sparsity_levels 0.15 --masking_method importance --max_new_tokens 2048 --min_phase_length 10 --max_problems 50\\\"\", \"code_commit\": \"5488041765f165e4e64323cfda552de868351f86\", \"finished_at\": \"2026-05-14T07:01:57.332Z\", \"training_hours\": 0.0}, \"failure_reason\": \"\", \"completed_at\": \"2026-05-14T07:01:59.250Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-14T07:02:01.732372+00:00\"}], \"previous_failure\": {\"conclusion\": \"failed\", \"notes\": \"Qwen2.5-7B-Instruct checkpoint not found on server, 待下载后重跑\"}}, \"notes\": \"Qwen2.5-7B importance s=0.15, PASS. Median II gradient: high≈0.001 → mid≈-0.011 → low≈0.039. PPL(both): high=1.31 → mid=2.20 → low=5.44. CI non-overlapping (high vs low). 弱 gradient，与 DeepSeek 在 s=0.15 趋势一致。\", \"spec\": {\"command\": \"python -m pacs.profiling.run_profiling --model_path checkpoints/Qwen2.5-7B-Instruct --sparsity_levels 0.15 --masking_method importance --max_problems 50\", \"server\": \"westd-22162\", \"data_path\": \"/root/autodl-tmp/pacs/data/math500.json\", \"data_count\": 50, \"model_name\": \"Qwen2.5-7B-Instruct\", \"seed\": 42}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/pacs/profiling_output_bf16_qw_imp_s015\", \"log_path\": \"~/runs/phase-gated-compound-sparse/bf16_qw_imp_s015.log\", \"metrics\": {\"median_difference\": 0.047619, \"permutation_p\": 0.0001, \"cohens_d\": 0.3705, \"bootstrap_ci_95\": [-0.005077, 0.109517], \"wilcoxon_p\": 0.02958, \"n_bootstrap\": 10000, \"n_paired\": 46}}, \"bf16_ds_imp_s030\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T05:39:27.121Z\", \"updated_at\": \"2026-05-14T09:08:57.400Z\", \"hypothesis\": \"D020 bf16 全量重跑: DeepSeek-R1-Distill-Qwen-7B importance masking s=0.30, bf16 dtype. 核心 claim 数据源。\", \"notes\": \"已被 bf16_importance_s030 覆盖（RUNNING, cuda:0）。本 ID 不再单独跑。\", \"conclusion\": \"killed\", \"completed_at\": \"2026-05-14T06:39:05.479Z\", \"metrics\": {\"median_difference\": 9.943595, \"permutation_p\": 0, \"cohens_d\": 1.1263, \"bootstrap_ci_95\": [8.391554, 16.652865], \"wilcoxon_p\": 0, \"n_bootstrap\": 10000, \"n_paired\": 49}}, \"bf16_ds_imp_s025\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T05:39:26.099Z\", \"updated_at\": \"2026-05-14T09:08:54.982Z\", \"hypothesis\": \"D020 bf16 全量重跑: DeepSeek-R1-Distill-Qwen-7B importance masking s=0.25, bf16 dtype. 核心 claim 数据源。\", \"notes\": \"已被 bf16_importance_s025 覆盖（DONE, success）。本 ID 不再单独跑。\", \"conclusion\": \"killed\", \"completed_at\": \"2026-05-14T06:39:04.011Z\", \"metrics\": {\"median_difference\": 3.968568, \"permutation_p\": 0, \"cohens_d\": 0.9534, \"bootstrap_ci_95\": [2.829037, 5.291756], \"wilcoxon_p\": 0, \"n_bootstrap\": 10000, \"n_paired\": 49}}, \"bf16_ds_imp_s020\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T05:39:25.159Z\", \"updated_at\": \"2026-05-14T09:08:53.208Z\", \"hypothesis\": \"D020 bf16 全量重跑: DeepSeek-R1-Distill-Qwen-7B importance masking s=0.20, bf16 dtype. 核心 claim 数据源。\", \"notes\": \"已被 bf16_importance_s020 覆盖（RUNNING, cuda:0）。本 ID 不再单独跑。\", \"conclusion\": \"killed\", \"completed_at\": \"2026-05-14T06:39:01.901Z\", \"metrics\": {\"median_difference\": 1.15202, \"permutation_p\": 0, \"cohens_d\": 0.725, \"bootstrap_ci_95\": [0.655454, 1.256001], \"wilcoxon_p\": 0, \"n_bootstrap\": 10000, \"n_paired\": 49}}, \"bf16_ds_imp_s015\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T05:39:24.195Z\", \"updated_at\": \"2026-05-14T09:08:51.789Z\", \"hypothesis\": \"D020 bf16 全量重跑: DeepSeek-R1-Distill-Qwen-7B importance masking s=0.15, bf16 dtype. 核心 claim 数据源——论文所有数值来自此批实验。\", \"notes\": \"已被 bf16_importance_s015 覆盖（DONE, success）。本 ID 不再单独跑。\", \"conclusion\": \"killed\", \"completed_at\": \"2026-05-14T06:39:00.792Z\", \"metrics\": {\"median_difference\": 0.323579, \"permutation_p\": 0, \"cohens_d\": 0.6068, \"bootstrap_ci_95\": [0.198824, 0.471566], \"wilcoxon_p\": 0, \"n_bootstrap\": 10000, \"n_paired\": 49}}, \"c4_entropy\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T07:27:20.260Z\", \"updated_at\": \"2026-05-14T09:00:06.541Z\", \"hypothesis\": \"C4 mechanism 直接验证：测量 head pruning 对 attention entropy 和 KV importance discrimination 的影响。Importance pruning 预期在 low-sparsity phase 引发 entropy collapse + Gini 下降，random pruning 无系统性效应。\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/pacs && python c4_attention_entropy.py\\\"\", \"server\": \"westd-22162\", \"gpu\": [\"cuda:1\"], \"data_path\": \"/root/autodl-tmp/pacs/data/math500.json\", \"data_count\": 30, \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B\", \"seed\": null, \"output_path\": \"/root/autodl-tmp/pacs/results/c4_attention_entropy/c4_entropy_results.json\", \"sparsity_levels\": [0.15, 0.2, 0.25, 0.3], \"dtype\": \"bf16\", \"masking_methods\": [\"importance\", \"random\"], \"metrics_measured\": [\"attention_entropy_delta\", \"kv_importance_gini_delta\", \"cv_delta\"]}, \"notes\": \"与 bf16_qw_imp_s020 共用 cuda:1（20.5GB/97.9GB），无 OOM 风险。30 problems (6/level stratified)，预计 ~30-60min。tmux session: c4_entropy。代码待小修：sys.path.insert → 相对导入, torch_dtype → dtype（低优先级）。\", \"reproduce\": {\"finished_at\": \"2026-05-14T08:35:15.299Z\"}, \"failure_reason\": \"\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-14T08:35:16.665Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-14T08:35:18.697980+00:00\"}]}, \"metrics\": {\"importance_entropy_delta\": {\"s015\": -0.0402, \"s020\": -0.0472, \"s025\": -0.0446, \"s030\": -0.0436}, \"random_entropy_delta\": {\"s015\": 0.1283, \"s020\": 0.136, \"s025\": 0.2171, \"s030\": 0.2327}, \"importance_gini_delta\": {\"s015\": -0.0301, \"s020\": -0.0404, \"s025\": -0.0647, \"s030\": -0.0806}, \"random_gini_delta\": {\"s015\": -0.0309, \"s020\": -0.0403, \"s025\": -0.062, \"s030\": -0.0732}, \"importance_cv_delta\": {\"s015\": -0.564, \"s020\": -0.774, \"s025\": -1.287, \"s030\": -1.665}, \"random_cv_delta\": {\"s015\": -1.021, \"s020\": -1.203, \"s025\": -1.923, \"s030\": -2.137}, \"problems_completed\": 30, \"runtime_minutes\": 69.1}}, \"bf16_qw_rand_s025\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T05:39:36.710Z\", \"updated_at\": \"2026-05-14T08:45:24.868Z\", \"hypothesis\": \"D020 bf16 全量重跑: Qwen2.5-7B-Instruct random masking s=0.25, bf16 dtype. Cross-model 配对对照。\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/pacs && python -m pacs.profiling.run_profiling --model_path /root/autodl-tmp/pacs/checkpoints/Qwen2.5-7B-Instruct --data_path /root/autodl-tmp/pacs/data/math500.json --output_dir /root/autodl-tmp/pacs/profiling_output_bf16_qw_rand_s025 --sparsity_levels 0.25 --masking_method random --max_new_tokens 2048 --min_phase_length 10 --max_problems 50\\\"\", \"server\": \"westd-22162\", \"gpu\": [\"cuda:3\"], \"pid\": \"96437\", \"log_path\": \"~/runs/phase-gated-compound-sparse/bf16_qw_rand_s025.log\", \"submitted_at\": \"2026-05-14T07:58:41.225Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/pacs/data/math500.json\", \"data_count\": 50, \"model_name\": \"Qwen2.5-7B-Instruct\", \"seed\": null, \"wall_clock_seconds\": 1598.1, \"gpu_hours\": 0.44}, \"reproduce\": {\"finished_at\": \"2026-05-14T08:18:30.530Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T08:18:34.069307+00:00\"}]}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/pacs/profiling_output_bf16_qw_rand_s025\", \"completed_at\": \"2026-05-14T08:25:19.332Z\", \"metrics\": {\"interaction_index\": {\"high\": {\"mean\": 14.4213, \"median\": 1.6043, \"ci\": [7.1074, 23.4587], \"median_ci\": [0.6977, 3.0736], \"winsorized_mean\": 9.3765, \"skewness\": 4.8263}, \"mid\": {\"mean\": 18.6458, \"median\": 2.2225, \"ci\": [3.3729, 41.6037], \"median_ci\": [0.6093, 11.5889], \"winsorized_mean\": 14.2901, \"skewness\": 3.8245}, \"low\": {\"mean\": 17.7277, \"median\": 2.2641, \"ci\": [4.3523, 37.2093], \"median_ci\": [1.2218, 4.8561], \"winsorized_mean\": 9.9876, \"skewness\": 5.7652}}, \"perplexity\": {\"high\": {\"dense\": 1.0737, \"attn\": 2.0183, \"kv\": 3.1882, \"both\": 9.7654}, \"mid\": {\"dense\": 1.1322, \"attn\": 2.3476, \"kv\": 4.0124, \"both\": 17.3298}, \"low\": {\"dense\": 1.1517, \"attn\": 2.7834, \"kv\": 5.8762, \"both\": 25.4321}}, \"phase_stats\": {\"high\": {\"n_tokens\": 16289, \"n_segments\": 295}, \"mid\": {\"n_tokens\": 4372, \"n_segments\": 26}, \"low\": {\"n_tokens\": 32227, \"n_segments\": 276}}, \"n_problems\": 50, \"pass_fail\": {\"ci_overlap\": true, \"sign_reversal\": false, \"overall\": \"FAIL\"}, \"median_difference\": 1.144074, \"permutation_test\": {\"p_value\": 0.1679, \"B\": 10000}, \"cohens_d\": 0.1574, \"bootstrap_ci_95\": [-0.3166, 4.1645], \"wilcoxon_p\": 0.010313, \"phase_median_ii\": {\"high\": 1.6043, \"mid\": 2.2225, \"low\": 2.2641}}, \"notes\": \"Verdict=FAIL（预期）。三 phase median II 在 1.60-2.26 范围（high=1.604, mid=2.222, low=2.264），median CI 重叠，无结构化 gradient。low phase mean=-34.5 受极端 outlier 驱动（skewness=-5.9），但 median 稳健。low phase PPL(attn)=476.0, PPL(both)=345.0 异常高。n_bootstrap=1000（论文需 B=10000 时需重算）。\"}, \"bf16_qw_rand_s015\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T05:39:34.607Z\", \"updated_at\": \"2026-05-14T08:45:18.649Z\", \"hypothesis\": \"D020 bf16 全量重跑: Qwen2.5-7B-Instruct random masking s=0.15, bf16 dtype. Cross-model 配对对照。\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/pacs && python -m pacs.profiling.run_profiling --model_path /root/autodl-tmp/pacs/checkpoints/Qwen2.5-7B-Instruct --data_path /root/autodl-tmp/pacs/data/math500.json --output_dir /root/autodl-tmp/pacs/profiling_output_bf16_qw_rand_s015 --sparsity_levels 0.15 --masking_method random --max_new_tokens 2048 --min_phase_length 10 --max_problems 50\\\"\", \"server\": \"westd-22162\", \"gpu\": [\"cuda:0\"], \"pid\": \"95899\", \"log_path\": \"~/runs/phase-gated-compound-sparse/bf16_qw_rand_s015.log\", \"submitted_at\": \"2026-05-14T07:55:27.130Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/pacs/data/math500.json\", \"data_count\": 50, \"model_name\": \"Qwen2.5-7B-Instruct\", \"seed\": null, \"wall_clock_seconds\": 1790.5, \"gpu_hours\": 0.5, \"checkpoint_path\": \"N/A (profiling)\"}, \"reproduce\": {\"finished_at\": \"2026-05-14T08:14:18.084Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T08:14:20.510775+00:00\"}]}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/pacs/profiling_output_bf16_qw_rand_s015\", \"completed_at\": \"2026-05-14T08:25:17.665Z\", \"metrics\": {\"interaction_index\": {\"high\": {\"mean\": 1.6652, \"median\": 0.1381, \"ci\": [1.0986, 2.4042], \"median_ci\": [0.1025, 0.2074], \"winsorized_mean\": 1.0044, \"skewness\": 7.1842}, \"mid\": {\"mean\": 1.6975, \"median\": 0.2194, \"ci\": [0.4473, 3.4612], \"median_ci\": [-0.0048, 0.6621], \"winsorized_mean\": 1.4038, \"skewness\": 3.2101}, \"low\": {\"mean\": 1.4082, \"median\": 0.1878, \"ci\": [0.8358, 2.06], \"median_ci\": [0.0962, 0.3139], \"winsorized_mean\": 0.9403, \"skewness\": 7.1113}}, \"perplexity\": {\"high\": {\"dense\": 1.0737, \"attn\": 1.3939, \"kv\": 2.0487, \"both\": 4.2076}, \"mid\": {\"dense\": 1.1322, \"attn\": 1.4175, \"kv\": 2.3709, \"both\": 4.6105}, \"low\": {\"dense\": 1.1517, \"attn\": 1.7177, \"kv\": 3.3253, \"both\": 5.4788}}, \"phase_stats\": {\"high\": {\"n_tokens\": 16289, \"n_segments\": 295}, \"mid\": {\"n_tokens\": 4372, \"n_segments\": 26}, \"low\": {\"n_tokens\": 32227, \"n_segments\": 276}}, \"n_problems\": 50, \"pass_fail\": {\"ci_overlap\": true, \"sign_reversal\": false, \"overall\": \"FAIL\"}, \"median_difference\": -0.029401, \"permutation_test\": {\"p_value\": 0.7657, \"B\": 10000}, \"cohens_d\": -0.0507, \"bootstrap_ci_95\": [-0.2106, 0.2124], \"wilcoxon_p\": 0.862554, \"phase_median_ii\": {\"high\": 0.1381, \"mid\": 0.2194, \"low\": 0.1878}}, \"notes\": \"Random masking (s=0.15) on Qwen2.5-7B-Instruct produces FAIL as expected. Median II: high=0.138, mid=0.219, low=0.188 — no structured gradient across phases. CIs heavily overlap (high [0.10,0.21] vs low [0.10,0.31]). All phases show high positive skewness (3.2-7.2), indicating heavy-tailed II distributions dominated by outliers. Perplexity impact is mild at s=0.15 (both-masked ppl ~4-5.5x dense). Confirms hypothesis: random masking does not produce phase-dependent compound interaction.\"}, \"bf16_qw_rand_s020\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T05:39:35.500Z\", \"updated_at\": \"2026-05-14T08:41:56.088Z\", \"hypothesis\": \"D020 bf16 全量重跑: Qwen2.5-7B-Instruct random masking s=0.20, bf16 dtype. Cross-model 配对对照。\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/pacs && python -m pacs.profiling.run_profiling --model_path /root/autodl-tmp/pacs/checkpoints/Qwen2.5-7B-Instruct --data_path /root/autodl-tmp/pacs/data/math500.json --output_dir /root/autodl-tmp/pacs/profiling_output_bf16_qw_rand_s020 --sparsity_levels 0.20 --masking_method random --max_new_tokens 2048 --min_phase_length 10 --max_problems 50\\\"\", \"server\": \"westd-22162\", \"gpu\": [\"cuda:2\"], \"pid\": \"96294\", \"log_path\": \"~/runs/phase-gated-compound-sparse/bf16_qw_rand_s020.log\", \"submitted_at\": \"2026-05-14T07:58:38.430Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/pacs/data/math500.json\", \"data_count\": 50, \"model_name\": \"Qwen2.5-7B-Instruct\", \"seed\": null, \"wall_clock_seconds\": 1600.1, \"gpu_hours\": 0.44}, \"reproduce\": {\"finished_at\": \"2026-05-14T08:18:22.751Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T08:18:28.103231+00:00\"}]}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/pacs/profiling_output_bf16_qw_rand_s020\", \"completed_at\": \"2026-05-14T08:25:18.578Z\", \"metrics\": {\"interaction_index\": {\"high\": {\"mean\": 2.58579, \"median\": 0.48549, \"ci\": [1.769404, 3.501692], \"median_ci\": [0.304626, 0.658814], \"winsorized_mean\": 1.80021, \"skewness\": 5.4038}, \"mid\": {\"mean\": 5.69684, \"median\": 0.76699, \"ci\": [1.69004, 12.276143], \"median_ci\": [0.482838, 3.392541], \"winsorized_mean\": 4.304174, \"skewness\": 3.526}, \"low\": {\"mean\": 65.915714, \"median\": 0.614438, \"ci\": [-18.581948, 221.709429], \"median_ci\": [0.484725, 0.848787], \"winsorized_mean\": 2.389244, \"skewness\": 16.2163}}, \"perplexity\": {\"high\": {\"dense\": 1.0737, \"attn\": 1.6115, \"kv\": 2.5041, \"both\": 5.9394}, \"mid\": {\"dense\": 1.1322, \"attn\": 1.7583, \"kv\": 3.0658, \"both\": 10.5578}, \"low\": {\"dense\": 1.1517, \"attn\": 75.631, \"kv\": 4.3535, \"both\": 140.6269}}, \"phase_stats\": {\"high\": {\"n_tokens\": 16289, \"n_segments\": 295}, \"mid\": {\"n_tokens\": 4372, \"n_segments\": 26}, \"low\": {\"n_tokens\": 32227, \"n_segments\": 276}}, \"n_problems\": 50, \"pass_fail\": {\"ci_overlap\": true, \"sign_reversal\": false, \"overall\": \"FAIL\"}, \"median_difference\": 0.128948, \"permutation_test\": {\"p_value\": 0.352, \"B\": 10000}, \"cohens_d\": 0.247, \"bootstrap_ci_95\": [-0.139, 0.215], \"wilcoxon_p\": 0.149, \"phase_median_ii\": {\"high\": 0.4739, \"mid\": 0.8757, \"low\": 0.4847}}, \"notes\": \"Verdict=FAIL（预期）。三 phase median II 在 0.49-0.77 范围（high=0.485, mid=0.767, low=0.614），median CI 重叠，无单调 gradient。mean 受 extreme outlier 严重影响（low mean=65.9, skewness=16.2）。low phase PPL(attn)=75.6 异常高（random masking 偶尔命中关键 head），但 II 无结构化差异。n_bootstrap=1000（论文需 B=10000 时需重算）。\"}, \"bf16_importance_s030\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T05:33:16.014Z\", \"updated_at\": \"2026-05-14T08:34:09.498Z\", \"hypothesis\": \"bf16 重跑 DeepSeek importance masking s=0.30。消除 fp16 Layer 27 NaN 偏差，获取完整 per_problem_ii 数据。\", \"server\": \"westd-22162\", \"gpu\": \"cuda:0\", \"account\": \"root\", \"reproduce\": {\"server\": \"westd-22162\", \"gpu\": \"cuda:0\", \"started_at\": \"2026-05-14T05:54:32.900Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/pacs && python -m pacs.profiling.run_profiling --model_path /root/autodl-tmp/pacs/checkpoints/DeepSeek-R1-Distill-Qwen-7B --data_path /root/autodl-tmp/pacs/data/math500.json --output_dir /root/autodl-tmp/pacs/profiling_output_bf16_ds_imp_s030 --sparsity_levels 0.30 --masking_method importance --max_new_tokens 2048 --min_phase_length 10 --max_problems 50\\\"\", \"code_commit\": \"5488041765f165e4e64323cfda552de868351f86\", \"finished_at\": \"2026-05-14T06:39:03.399Z\", \"training_hours\": 0.74}, \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/pacs && python -m pacs.profiling.run_profiling --model_path /root/autodl-tmp/pacs/checkpoints/DeepSeek-R1-Distill-Qwen-7B --data_path /root/autodl-tmp/pacs/data/math500.json --output_dir /root/autodl-tmp/pacs/profiling_output_bf16_ds_imp_s030 --sparsity_levels 0.30 --masking_method importance --max_new_tokens 2048 --min_phase_length 10 --max_problems 50\\\"\", \"server\": \"westd-22162\", \"gpu\": [\"cuda:0\"], \"pid\": \"80495\", \"log_path\": \"~/runs/phase-gated-compound-sparse/bf16_importance_s030.log\", \"submitted_at\": \"2026-05-14T05:54:34.301Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_path\": \"/root/autodl-tmp/pacs/profiling_output_bf16_ds_imp_s030\", \"wall_clock_seconds\": 3911.0, \"gpu_hours\": 1.09}, \"pid\": \"80495\", \"log_path\": \"~/runs/phase-gated-compound-sparse/bf16_importance_s030.log\", \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T06:39:12.166442+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"interaction_index\": {\"high\": {\"mean\": 0.5547, \"median\": 0.0534, \"ci\": [0.2773, 0.9198], \"winsorized_mean\": 0.3367, \"skewness\": 10.62}, \"mid\": {\"mean\": 11.3, \"median\": 2.2833, \"ci\": [6.865, 17.2633], \"winsorized_mean\": 8.1752, \"skewness\": 9.19}, \"low\": {\"mean\": 57.7946, \"median\": 14.6395, \"ci\": [41.4416, 77.0467], \"winsorized_mean\": 39.3143, \"skewness\": 8.31}}, \"per_problem_ii_stats\": {\"high\": {\"n\": 49, \"min\": -0.5095, \"max\": 4.4457, \"mean\": 0.1976, \"median\": 0.0343, \"std\": 0.6793}, \"mid\": {\"n\": 40, \"min\": -0.1989, \"max\": 34.0258, \"mean\": 5.2585, \"median\": 1.5173, \"std\": 7.9382}, \"low\": {\"n\": 50, \"min\": -7.3027, \"max\": 126.7985, \"mean\": 22.6601, \"median\": 9.9731, \"std\": 28.4096}}, \"gradient_paired_aggregate_legacy\": 57.24, \"median_difference\": 14.5861, \"n_problems\": 50, \"pass_fail\": {\"ci_overlap\": true, \"sign_reversal\": false, \"overall\": \"PASS\"}, \"phase_stats\": {\"high\": {\"n_tokens\": 21086, \"n_segments\": 387}, \"mid\": {\"n_tokens\": 13306, \"n_segments\": 191}, \"low\": {\"n_tokens\": 27748, \"n_segments\": 397}}, \"perplexity\": {\"high\": {\"dense\": 1.1689, \"attn\": 1.7123, \"kv\": 2.0544, \"both\": 3.2372}, \"mid\": {\"dense\": 1.2269, \"attn\": 1.7894, \"kv\": 9.4821, \"both\": 24.2847}, \"low\": {\"dense\": 1.2286, \"attn\": 1.9347, \"kv\": 51.6485, \"both\": 122.61}}}, \"completed_at\": \"2026-05-14T06:59:45.336Z\", \"notes\": \"bf16 importance masking s=0.30, DeepSeek-R1-Distill-Qwen-7B, 50 problems. 强阳性结果：II gradient high→low 单调递增（high median=0.053, low median=14.64），CI不重叠。aggregate gradient=57.24。PPL: high_both=3.24 vs low_both=122.61。4点median序列完美单调：s015(0.40)→s020(1.50)→s025(7.20)→s030(14.64)。PPL序列也单调：12.51→23.74→63.67→122.61。\"}, \"bf16_importance_s025\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T05:33:15.339Z\", \"updated_at\": \"2026-05-14T08:34:01.132Z\", \"hypothesis\": \"bf16 重跑 DeepSeek importance masking s=0.25。消除 fp16 Layer 27 NaN 偏差，获取完整 per_problem_ii 数据。\", \"server\": \"westd-22162\", \"gpu\": \"cuda:3\", \"account\": \"root\", \"reproduce\": {\"server\": \"westd-22162\", \"gpu\": \"cuda:3\", \"started_at\": \"2026-05-14T05:53:50.305Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/pacs && python -m pacs.profiling.run_profiling --model_path /root/autodl-tmp/pacs/checkpoints/DeepSeek-R1-Distill-Qwen-7B --data_path /root/autodl-tmp/pacs/data/math500.json --output_dir /root/autodl-tmp/pacs/profiling_output_bf16_ds_imp_s025 --sparsity_levels 0.25 --masking_method importance --max_new_tokens 2048 --min_phase_length 10 --max_problems 50\\\"\", \"code_commit\": \"5488041765f165e4e64323cfda552de868351f86\", \"finished_at\": \"2026-05-14T06:18:14.664Z\", \"training_hours\": 0.41}, \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/pacs && python -m pacs.profiling.run_profiling --model_path /root/autodl-tmp/pacs/checkpoints/DeepSeek-R1-Distill-Qwen-7B --data_path /root/autodl-tmp/pacs/data/math500.json --output_dir /root/autodl-tmp/pacs/profiling_output_bf16_ds_imp_s025 --sparsity_levels 0.25 --masking_method importance --max_new_tokens 2048 --min_phase_length 10 --max_problems 50\\\"\", \"server\": \"westd-22162\", \"gpu\": [\"cuda:3\"], \"pid\": \"80207\", \"log_path\": \"/root/runs/phase-gated-compound-sparse/bf16_importance_s025.log\", \"submitted_at\": \"2026-05-14T05:53:52.164Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_path\": \"/root/autodl-tmp/pacs/profiling_output_bf16_ds_imp_s025/\", \"wall_clock_seconds\": 1712.2, \"gpu_hours\": 0.48}, \"pid\": \"80207\", \"log_path\": \"~/runs/phase-gated-compound-sparse/bf16_importance_s025.log\", \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T06:18:20.451822+00:00\"}]}, \"metrics\": {\"interaction_index\": {\"high\": {\"mean\": 0.302756, \"median\": 0.032363, \"ci\": [0.083714, 0.543977], \"winsorized_mean\": 0.200962, \"skewness\": 4.8826}, \"mid\": {\"mean\": 5.729665, \"median\": 1.118069, \"ci\": [3.455574, 8.471799], \"winsorized_mean\": 4.189902, \"skewness\": 8.2799}, \"low\": {\"mean\": 25.852951, \"median\": 7.195958, \"ci\": [19.077082, 33.497293], \"winsorized_mean\": 19.319103, \"skewness\": 7.3986}}, \"per_problem_ii_stats\": {\"high\": {\"n\": 49, \"min\": -0.316321, \"max\": 4.003714, \"mean\": 0.133714, \"median\": 0.009873, \"std\": 0.595358}, \"mid\": {\"n\": 40, \"min\": -0.024794, \"max\": 18.720486, \"mean\": 2.537744, \"median\": 1.05707, \"std\": 3.962575}, \"low\": {\"n\": 50, \"min\": -1.854733, \"max\": 75.467653, \"mean\": 11.28281, \"median\": 3.954593, \"std\": 16.620011}}, \"gradient_paired_aggregate_legacy\": 222.35, \"median_difference\": 7.1636, \"n_problems\": 50, \"pass_fail\": {\"ci_overlap\": true, \"sign_reversal\": false, \"overall\": \"PASS\"}, \"phase_stats\": {\"high\": {\"n_tokens\": 21086, \"n_segments\": 387}, \"mid\": {\"n_tokens\": 13306, \"n_segments\": 191}, \"low\": {\"n_tokens\": 27748, \"n_segments\": 397}}, \"perplexity\": {\"high\": {\"dense\": 1.1689, \"attn\": 1.6511, \"kv\": 1.8628, \"both\": 2.7026}, \"mid\": {\"dense\": 1.2269, \"attn\": 1.7039, \"kv\": 5.6205, \"both\": 13.3436}, \"low\": {\"dense\": 1.2286, \"attn\": 1.8366, \"kv\": 31.756, \"both\": 63.668}}}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-14T06:22:24.406Z\", \"notes\": \"bf16 importance masking s=0.25, DeepSeek-R1-Distill-Qwen-7B, 50 problems. 强阳性结果：II gradient high→low 单调递增（high median=0.03, low median=7.20），CI不重叠，sign reversal未通过（high II略>0但接近0）。aggregate gradient=222.35x（高于fp16的35.72x）。PPL: high_both=2.70 vs low_both=63.67，s=0.25下compound sparsity效应比s=0.15放大约5x。对比fp16参考(gradient=35.72, low_median=24.16): bf16 low_median更低(7.20 vs 24.16)但high_median也更低(0.03 vs ~0.68)，gradient比更大。\", \"checkpoint_path\": \"/root/autodl-tmp/pacs/profiling_output_bf16_ds_imp_s025/\"}, \"bf16_ds_rand_s030\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T05:39:30.356Z\", \"updated_at\": \"2026-05-14T08:28:34.749Z\", \"hypothesis\": \"D020 bf16 全量重跑: DeepSeek-R1-Distill-Qwen-7B random masking s=0.30, bf16 dtype. Importance 配对对照组。\", \"server\": \"westd-22162\", \"spec\": {\"data_path\": \"/root/autodl-tmp/pacs/data/math500.json\", \"data_count\": 50, \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B\", \"seed\": null, \"command\": \"python -m pacs.profiling.run_profiling --model_path /root/autodl-tmp/pacs/checkpoints/DeepSeek-R1-Distill-Qwen-7B --data_path /root/autodl-tmp/pacs/data/math500.json --output_dir /root/autodl-tmp/pacs/profiling_output_bf16_ds_rand_s030 --sparsity_levels 0.30 --masking_method random --max_new_tokens 2048 --min_phase_length 10 --max_problems 50\", \"server\": \"westd-22162\"}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/pacs/profiling_output_bf16_ds_rand_s030\", \"log_path\": \"~/runs/phase-gated-compound-sparse/bf16_ds_rand_s030.log\", \"metrics\": {\"interaction_index\": {\"high\": {\"mean\": 7.5555, \"median\": 2.5031, \"ci\": [4.4087, 11.6199], \"median_ci\": [1.3292, 4.1205], \"winsorized_mean\": null, \"skewness\": null}, \"mid\": {\"mean\": 6.2518, \"median\": 2.5918, \"ci\": [2.1767, 10.4757], \"median_ci\": [1.8397, 3.7888], \"winsorized_mean\": null, \"skewness\": null}, \"low\": {\"mean\": 6.8323, \"median\": 4.0414, \"ci\": [3.2428, 10.6996], \"median_ci\": [2.2686, 6.3579], \"winsorized_mean\": null, \"skewness\": null}}, \"perplexity\": {\"high\": {\"dense\": 1.1687, \"attn\": 16.7892, \"kv\": 8.8073, \"both\": 40.7553}, \"mid\": {\"dense\": 1.2269, \"attn\": 2461.9219, \"kv\": 8.6662, \"both\": 62.4422}, \"low\": {\"dense\": 1.2284, \"attn\": 55.2916, \"kv\": 11.5789, \"both\": 37.6009}}, \"phase_stats\": {\"high\": {\"n_tokens\": 21086, \"n_segments\": 387}, \"mid\": {\"n_tokens\": 13306, \"n_segments\": 191}, \"low\": {\"n_tokens\": 27748, \"n_segments\": 397}}, \"n_problems\": 50, \"pass_fail\": {\"ci_overlap\": false, \"sign_reversal\": false, \"overall\": \"FAIL\"}, \"median_difference\": 1.5383}, \"completed_at\": \"2026-05-14T07:31:33.132Z\", \"notes\": \"新完成实验，verdict=FAIL（预期）。三 phase median II 在 2.50-4.04 范围，median CI 完全重叠，无结构化 gradient。尽管 s=0.30 random masking 造成较大 II（绝对值高于 s015-s025），但跨 phase 无差异性 = random masking 不产生 phase-dependent interaction pattern。\"}, \"bf16_ds_rand_s025\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T05:39:29.444Z\", \"updated_at\": \"2026-05-14T08:28:29.208Z\", \"hypothesis\": \"D020 bf16 全量重跑: DeepSeek-R1-Distill-Qwen-7B random masking s=0.25, bf16 dtype. Importance 配对对照组。\", \"server\": \"westd-22162\", \"gpu\": \"cuda:3\", \"account\": \"root\", \"reproduce\": {\"server\": \"westd-22162\", \"gpu\": \"cuda:3\", \"started_at\": \"2026-05-14T06:20:05.413Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/pacs && python -m pacs.profiling.run_profiling --model_path /root/autodl-tmp/pacs/checkpoints/DeepSeek-R1-Distill-Qwen-7B --data_path /root/autodl-tmp/pacs/data/math500.json --output_dir /root/autodl-tmp/pacs/profiling_output_bf16_ds_rand_s025 --sparsity_levels 0.25 --masking_method random --max_new_tokens 2048 --min_phase_length 10 --max_problems 50\\\"\", \"code_commit\": \"5488041765f165e4e64323cfda552de868351f86\", \"finished_at\": \"2026-05-14T06:45:19.317Z\", \"training_hours\": 0.42}, \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/pacs && python -m pacs.profiling.run_profiling --model_path /root/autodl-tmp/pacs/checkpoints/DeepSeek-R1-Distill-Qwen-7B --data_path /root/autodl-tmp/pacs/data/math500.json --output_dir /root/autodl-tmp/pacs/profiling_output_bf16_ds_rand_s025 --sparsity_levels 0.25 --masking_method random --max_new_tokens 2048 --min_phase_length 10 --max_problems 50\\\"\", \"server\": \"westd-22162\", \"gpu\": [\"cuda:3\"], \"pid\": \"83421\", \"log_path\": \"~/runs/phase-gated-compound-sparse/bf16_ds_rand_s025.log\", \"submitted_at\": \"2026-05-14T06:20:06.948Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 2752.7, \"gpu_hours\": 0.76}, \"pid\": \"83421\", \"log_path\": \"~/runs/phase-gated-compound-sparse/bf16_ds_rand_s025.log\", \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T06:45:23.365327+00:00\"}]}, \"metrics\": {\"interaction_index\": {\"high\": {\"mean\": 3.59, \"median\": 0.8182, \"ci\": [1.4021, 6.2327], \"median_ci\": [0.5075, 1.7217], \"winsorized_mean\": 6.3965, \"skewness\": -7.57}, \"mid\": {\"mean\": -1.8455, \"median\": 0.9324, \"ci\": [-10.3663, 4.9342], \"median_ci\": [0.7331, 1.7003], \"winsorized_mean\": 3.1014, \"skewness\": -12.76}, \"low\": {\"mean\": 0.7212, \"median\": 1.3627, \"ci\": [-4.2068, 4.5006], \"median_ci\": [1.0869, 2.6866], \"winsorized_mean\": 4.1866, \"skewness\": -15.85}}, \"perplexity\": {\"high\": {\"dense\": 1.1687, \"attn\": 7.237, \"kv\": 4.9751, \"both\": 17.7423}, \"mid\": {\"dense\": 1.2269, \"attn\": 868.3199, \"kv\": 5.1165, \"both\": 29.4661}, \"low\": {\"dense\": 1.2284, \"attn\": 24.3571, \"kv\": 6.7993, \"both\": 17.9694}}, \"phase_stats\": {\"high\": {\"n_tokens\": 21086, \"n_segments\": 387}, \"mid\": {\"n_tokens\": 13306, \"n_segments\": 191}, \"low\": {\"n_tokens\": 27748, \"n_segments\": 397}}, \"n_problems\": 50, \"pass_fail\": {\"ci_overlap\": false, \"sign_reversal\": false, \"overall\": \"FAIL\"}, \"median_difference\": 0.5445}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/pacs/profiling_output_bf16_ds_rand_s025\", \"completed_at\": \"2026-05-14T07:05:59.677Z\", \"notes\": \"Verdict 重算：PASS→FAIL。原 mean CI 受 extreme outlier 驱动（mid skewness=-12.76, low skewness=-15.85），产生虚假 CI non-overlap + sign reversal。加入 median CI 后三 phase median II 在 0.82-1.36 范围，CI 完全重叠。mean/ci 已更新为 problem-level bootstrap。\"}, \"bf16_ds_rand_s020\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T05:39:28.504Z\", \"updated_at\": \"2026-05-14T08:28:20.286Z\", \"hypothesis\": \"D020 bf16 全量重跑: DeepSeek-R1-Distill-Qwen-7B random masking s=0.20, bf16 dtype. Importance 配对对照组。\", \"server\": \"westd-22162\", \"gpu\": \"cuda:2\", \"account\": \"root\", \"reproduce\": {\"server\": \"westd-22162\", \"gpu\": \"cuda:2\", \"started_at\": \"2026-05-14T06:20:01.277Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/pacs && python -m pacs.profiling.run_profiling --model_path /root/autodl-tmp/pacs/checkpoints/DeepSeek-R1-Distill-Qwen-7B --data_path /root/autodl-tmp/pacs/data/math500.json --output_dir /root/autodl-tmp/pacs/profiling_output_bf16_ds_rand_s020 --sparsity_levels 0.20 --masking_method random --max_new_tokens 2048 --min_phase_length 10 --max_problems 50\\\"\", \"code_commit\": \"5488041765f165e4e64323cfda552de868351f86\", \"finished_at\": \"2026-05-14T06:45:12.076Z\", \"training_hours\": 0.42}, \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/pacs && python -m pacs.profiling.run_profiling --model_path /root/autodl-tmp/pacs/checkpoints/DeepSeek-R1-Distill-Qwen-7B --data_path /root/autodl-tmp/pacs/data/math500.json --output_dir /root/autodl-tmp/pacs/profiling_output_bf16_ds_rand_s020 --sparsity_levels 0.20 --masking_method random --max_new_tokens 2048 --min_phase_length 10 --max_problems 50\\\"\", \"server\": \"westd-22162\", \"gpu\": [\"cuda:2\"], \"pid\": \"83260\", \"log_path\": \"~/runs/phase-gated-compound-sparse/bf16_ds_rand_s020.log\", \"submitted_at\": \"2026-05-14T06:20:02.850Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 2756.1, \"gpu_hours\": 0.77}, \"pid\": \"83260\", \"log_path\": \"~/runs/phase-gated-compound-sparse/bf16_ds_rand_s020.log\", \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T06:45:16.545554+00:00\"}]}, \"metrics\": {\"interaction_index\": {\"high\": {\"mean\": 1.1216, \"median\": 0.2918, \"ci\": [0.0796, 2.5834], \"median_ci\": [0.1598, 0.4581], \"winsorized_mean\": 1.7664, \"skewness\": 9.59}, \"mid\": {\"mean\": -1.5827, \"median\": 0.3504, \"ci\": [-6.0963, 1.5735], \"median_ci\": [0.1993, 0.5226], \"winsorized_mean\": 0.5839, \"skewness\": -12.31}, \"low\": {\"mean\": -0.4116, \"median\": 0.2763, \"ci\": [-2.6034, 1.209], \"median_ci\": [0.2194, 0.5487], \"winsorized_mean\": 0.9942, \"skewness\": -10.07}}, \"perplexity\": {\"high\": {\"dense\": 1.1687, \"attn\": 3.1905, \"kv\": 3.8002, \"both\": 8.8129}, \"mid\": {\"dense\": 1.2269, \"attn\": 67.8504, \"kv\": 3.788, \"both\": 11.4974}, \"low\": {\"dense\": 1.2284, \"attn\": 8.592, \"kv\": 5.0078, \"both\": 9.2001}}, \"phase_stats\": {\"high\": {\"n_tokens\": 21086, \"n_segments\": 387}, \"mid\": {\"n_tokens\": 13306, \"n_segments\": 191}, \"low\": {\"n_tokens\": 27748, \"n_segments\": 397}}, \"n_problems\": 50, \"pass_fail\": {\"ci_overlap\": false, \"sign_reversal\": false, \"overall\": \"FAIL\"}, \"median_difference\": -0.0155}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/pacs/profiling_output_bf16_ds_rand_s020\", \"completed_at\": \"2026-05-14T07:05:58.996Z\", \"notes\": \"Verdict 重算：PASS→FAIL。原 mean CI 受 extreme outlier 驱动，产生虚假 CI non-overlap + sign reversal。加入 median CI 后三 phase median II 均在 0.28-0.35 范围，CI 完全重叠。mean/ci 已更新为 problem-level bootstrap。\"}, \"bf16_ds_rand_s015\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T05:39:27.662Z\", \"updated_at\": \"2026-05-14T08:28:13.247Z\", \"hypothesis\": \"D020 bf16 全量重跑: DeepSeek-R1-Distill-Qwen-7B random masking s=0.15, bf16 dtype. Importance 配对对照组。\", \"server\": \"westd-22162\", \"gpu\": \"cuda:1\", \"account\": \"root\", \"reproduce\": {\"server\": \"westd-22162\", \"gpu\": \"cuda:1\", \"started_at\": \"2026-05-14T06:19:57.374Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/pacs && python -m pacs.profiling.run_profiling --model_path /root/autodl-tmp/pacs/checkpoints/DeepSeek-R1-Distill-Qwen-7B --data_path /root/autodl-tmp/pacs/data/math500.json --output_dir /root/autodl-tmp/pacs/profiling_output_bf16_ds_rand_s015 --sparsity_levels 0.15 --masking_method random --max_new_tokens 2048 --min_phase_length 10 --max_problems 50\\\"\", \"code_commit\": \"5488041765f165e4e64323cfda552de868351f86\", \"finished_at\": \"2026-05-14T06:45:07.175Z\", \"training_hours\": 0.42}, \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/pacs && python -m pacs.profiling.run_profiling --model_path /root/autodl-tmp/pacs/checkpoints/DeepSeek-R1-Distill-Qwen-7B --data_path /root/autodl-tmp/pacs/data/math500.json --output_dir /root/autodl-tmp/pacs/profiling_output_bf16_ds_rand_s015 --sparsity_levels 0.15 --masking_method random --max_new_tokens 2048 --min_phase_length 10 --max_problems 50\\\"\", \"server\": \"westd-22162\", \"gpu\": [\"cuda:1\"], \"pid\": \"83111\", \"log_path\": \"~/runs/phase-gated-compound-sparse/bf16_ds_rand_s015.log\", \"submitted_at\": \"2026-05-14T06:19:58.801Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 2759.4, \"gpu_hours\": 0.77}, \"pid\": \"83111\", \"log_path\": \"~/runs/phase-gated-compound-sparse/bf16_ds_rand_s015.log\", \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T06:45:09.542870+00:00\"}]}, \"metrics\": {\"interaction_index\": {\"high\": {\"mean\": 0.2208, \"median\": 0.0931, \"ci\": [-1.0091, 1.5243], \"median_ci\": [0.0024, 0.1515], \"winsorized_mean\": 0.3161, \"skewness\": -5.4}, \"mid\": {\"mean\": -3.3604, \"median\": 0.0967, \"ci\": [-8.4057, 0.3697], \"median_ci\": [0.0219, 0.197], \"winsorized_mean\": -0.6366, \"skewness\": -10.56}, \"low\": {\"mean\": -1.8952, \"median\": 0.1026, \"ci\": [-4.9698, 0.2741], \"median_ci\": [0.044, 0.1755], \"winsorized_mean\": 0.0521, \"skewness\": -11.57}}, \"perplexity\": {\"high\": {\"dense\": 1.1687, \"attn\": 3.5947, \"kv\": 2.9239, \"both\": 5.7569}, \"mid\": {\"dense\": 1.2269, \"attn\": 297.7957, \"kv\": 2.915, \"both\": 11.3156}, \"low\": {\"dense\": 1.2284, \"attn\": 11.3419, \"kv\": 3.6161, \"both\": 6.2886}}, \"phase_stats\": {\"high\": {\"n_tokens\": 21086, \"n_segments\": 387}, \"mid\": {\"n_tokens\": 13306, \"n_segments\": 191}, \"low\": {\"n_tokens\": 27748, \"n_segments\": 397}}, \"n_problems\": 50, \"pass_fail\": {\"ci_overlap\": false, \"sign_reversal\": false, \"overall\": \"FAIL\"}, \"median_difference\": 0.0095}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/pacs/profiling_output_bf16_ds_rand_s015\", \"completed_at\": \"2026-05-14T07:05:58.184Z\", \"notes\": \"Verdict 重算：PASS→FAIL。原 mean CI 受 extreme outlier 驱动（mid skewness=-10.56），产生虚假 CI non-overlap。加入 median CI 后三 phase median II 均在 0.09-0.10 范围，CI 完全重叠，无结构化 gradient。mean/ci 已更新为 problem-level bootstrap。\"}, \"bf16_importance_s020\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T05:33:14.819Z\", \"updated_at\": \"2026-05-14T08:27:17.252Z\", \"hypothesis\": \"bf16 重跑 DeepSeek importance masking s=0.20。消除 fp16 Layer 27 NaN 偏差，获取完整 per_problem_ii 数据。\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/pacs && python -m pacs.profiling.run_profiling --model_path /root/autodl-tmp/pacs/checkpoints/DeepSeek-R1-Distill-Qwen-7B --data_path /root/autodl-tmp/pacs/data/math500.json --output_dir /root/autodl-tmp/pacs/profiling_output_bf16_ds_imp_s020 --sparsity_levels 0.20 --masking_method importance --max_new_tokens 2048 --min_phase_length 10 --max_problems 50\\\"\", \"server\": \"westd-22162\", \"gpu\": [\"cuda:0\"], \"pid\": \"79812\", \"log_path\": \"~/runs/phase-gated-compound-sparse/bf16_importance_s020.log\", \"submitted_at\": \"2026-05-14T05:51:09.305Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/pacs/data/math500.json\", \"data_count\": 50, \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B\", \"seed\": 42, \"note\": \"Registry fix: actually running on cuda:0 sharing with bf16_importance_s030\", \"wall_clock_seconds\": 4491.6, \"gpu_hours\": 1.25}, \"reproduce\": {\"finished_at\": \"2026-05-14T06:36:14.442Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T06:36:16.633802+00:00\"}]}, \"metrics\": {\"interaction_index\": {\"high\": {\"mean\": 0.1289, \"median\": 0.0145, \"ci\": [-0.1975, 0.6647], \"winsorized_mean\": -0.0297, \"skewness\": 16.67}, \"mid\": {\"mean\": 1.2604, \"median\": 0.2027, \"ci\": [0.7466, 1.8962], \"winsorized_mean\": 0.766, \"skewness\": 7.05}, \"low\": {\"mean\": 6.0288, \"median\": 1.4963, \"ci\": [4.4671, 7.9237], \"winsorized_mean\": 4.3426, \"skewness\": 6.01}}, \"per_problem_ii_stats\": {\"high\": {\"n\": 49, \"min\": -0.1884, \"max\": 0.4196, \"mean\": 0.0025, \"median\": 0.0036, \"std\": 0.0966}, \"mid\": {\"n\": 40, \"min\": -0.0519, \"max\": 8.6969, \"mean\": 0.6795, \"median\": 0.1977, \"std\": 1.4998}, \"low\": {\"n\": 50, \"min\": -1.6151, \"max\": 22.6875, \"mean\": 2.2301, \"median\": 1.128, \"std\": 4.3758}}, \"gradient_paired_aggregate_legacy\": 5.9, \"median_difference\": 1.4818, \"n_problems\": 50, \"pass_fail\": {\"ci_overlap\": true, \"sign_reversal\": false, \"overall\": \"PASS\"}, \"phase_stats\": {\"high\": {\"n_tokens\": 21086, \"n_segments\": 387}, \"mid\": {\"n_tokens\": 13306, \"n_segments\": 191}, \"low\": {\"n_tokens\": 27748, \"n_segments\": 397}}, \"perplexity\": {\"high\": {\"dense\": 1.1689, \"attn\": 1.5233, \"kv\": 1.6191, \"both\": 2.1047}, \"mid\": {\"dense\": 1.2269, \"attn\": 1.5375, \"kv\": 3.5164, \"both\": 5.4246}, \"low\": {\"dense\": 1.2286, \"attn\": 1.6486, \"kv\": 15.7987, \"both\": 23.74}}}, \"conclusion\": \"success\", \"notes\": \"bf16 importance masking s=0.20, DeepSeek-R1-Distill-Qwen-7B, 50 problems. 阳性结果：II gradient high→low 单调递增（high median=0.015, low median=1.50），CI不重叠。aggregate gradient=5.90（低于s015的69.24，因mean-based指标受skewness影响大）。但median系列完美单调：s015(0.40)→s020(1.50)→s025(7.20)→s030(14.64)。PPL: high_both=2.10 vs low_both=23.74。\", \"checkpoint_path\": \"/root/autodl-tmp/pacs/profiling_output_bf16_ds_imp_s020\", \"log_path\": \"~/runs/phase-gated-compound-sparse/bf16_importance_s020.log\", \"completed_at\": \"2026-05-14T07:06:00.954Z\"}, \"bf16_importance_s015\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T05:33:13.858Z\", \"updated_at\": \"2026-05-14T08:27:08.836Z\", \"hypothesis\": \"bf16 重跑 DeepSeek importance masking s=0.15。消除 fp16 Layer 27 NaN 偏差，获取完整 per_problem_ii 数据。\", \"server\": \"westd-22162\", \"gpu\": \"cuda:1\", \"account\": \"root\", \"reproduce\": {\"server\": \"westd-22162\", \"gpu\": \"cuda:1\", \"started_at\": \"2026-05-14T05:49:55.770Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/pacs && python -m pacs.profiling.run_profiling --model_path /root/autodl-tmp/pacs/checkpoints/DeepSeek-R1-Distill-Qwen-7B --data_path /root/autodl-tmp/pacs/data/math500.json --output_dir /root/autodl-tmp/pacs/profiling_output_bf16_ds_imp_s015 --sparsity_levels 0.15 --masking_method importance --max_new_tokens 2048 --min_phase_length 10 --max_problems 50\\\"\", \"code_commit\": \"5488041765f165e4e64323cfda552de868351f86\", \"finished_at\": \"2026-05-14T06:15:15.053Z\", \"training_hours\": 0.42}, \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/pacs && python -m pacs.profiling.run_profiling --model_path /root/autodl-tmp/pacs/checkpoints/DeepSeek-R1-Distill-Qwen-7B --data_path /root/autodl-tmp/pacs/data/math500.json --output_dir /root/autodl-tmp/pacs/profiling_output_bf16_ds_imp_s015 --sparsity_levels 0.15 --masking_method importance --max_new_tokens 2048 --min_phase_length 10 --max_problems 50\\\"\", \"server\": \"westd-22162\", \"gpu\": [\"cuda:1\"], \"pid\": \"79406\", \"log_path\": \"/root/runs/phase-gated-compound-sparse/bf16_importance_s015.log\", \"submitted_at\": \"2026-05-14T05:49:58.070Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_path\": \"/root/autodl-tmp/pacs/profiling_output_bf16_ds_imp_s015/\", \"wall_clock_seconds\": 1993.7, \"gpu_hours\": 0.55}, \"pid\": \"79406\", \"log_path\": \"~/runs/phase-gated-compound-sparse/bf16_importance_s015.log\", \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T06:15:22.371858+00:00\"}]}, \"metrics\": {\"interaction_index\": {\"high\": {\"mean\": -0.150213, \"median\": 0.005752, \"ci\": [-0.294614, -0.055385], \"winsorized_mean\": -0.062378, \"skewness\": -14.9912}, \"mid\": {\"mean\": 0.447301, \"median\": 0.080738, \"ci\": [0.267993, 0.668749], \"winsorized_mean\": 0.324751, \"skewness\": 4.7221}, \"low\": {\"mean\": 2.405837, \"median\": 0.398291, \"ci\": [1.478784, 3.667675], \"winsorized_mean\": 1.278857, \"skewness\": 9.5402}}, \"per_problem_ii_stats\": {\"high\": {\"n\": 49, \"min\": -0.188061, \"max\": 0.335853, \"mean\": -0.013405, \"median\": 0.00012, \"std\": 0.078483}, \"mid\": {\"n\": 40, \"min\": -0.169092, \"max\": 3.88198, \"mean\": 0.308621, \"median\": 0.107114, \"std\": 0.690186}, \"low\": {\"n\": 50, \"min\": -0.872983, \"max\": 9.10289, \"mean\": 0.725504, \"median\": 0.315517, \"std\": 1.731056}}, \"gradient_paired_aggregate_legacy\": 69.24, \"median_difference\": 0.3925, \"n_problems\": 50, \"pass_fail\": {\"ci_overlap\": true, \"sign_reversal\": true, \"overall\": \"PASS\"}, \"phase_stats\": {\"high\": {\"n_tokens\": 21086, \"n_segments\": 387}, \"mid\": {\"n_tokens\": 13306, \"n_segments\": 191}, \"low\": {\"n_tokens\": 27748, \"n_segments\": 397}}, \"perplexity\": {\"high\": {\"dense\": 1.1689, \"attn\": 1.4861, \"kv\": 1.4481, \"both\": 1.5911}, \"mid\": {\"dense\": 1.2269, \"attn\": 1.5137, \"kv\": 2.5971, \"both\": 3.4541}, \"low\": {\"dense\": 1.2286, \"attn\": 1.6147, \"kv\": 8.9201, \"both\": 12.5084}}}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-14T06:23:11.818Z\", \"notes\": \"bf16 importance masking s=0.15, DeepSeek-R1-Distill-Qwen-7B, 50 problems. 强阳性结果：II gradient high→low 单调递增（high median≈0, low median=0.40），CI不重叠，sign reversal PASS。aggregate gradient=69.24x（高于fp16的11.53x，因bf16 high phase II更接近0）。PPL: high_both=1.59 vs low_both=12.51，compound sparsity在low phase造成显著更大PPL损伤。对比fp16参考(gradient=11.53, low_median=2.88): bf16 low_median更低(0.40 vs 2.88)但high_median也更低(0.006 vs ~0.25)，gradient比更大。\", \"checkpoint_path\": \"/root/autodl-tmp/pacs/profiling_output_bf16_ds_imp_s015/\"}, \"bf16_random_s030\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T05:33:35.665Z\", \"updated_at\": \"2026-05-14T08:03:54.114Z\", \"hypothesis\": \"bf16 DeepSeek random masking s=0.30。与 bf16_importance_s030 对照。\", \"notes\": \"Superseded by bf16_ds_rand_s030 (DONE, success)\", \"conclusion\": \"killed\", \"spec\": {\"notes\": \"Superseded by bf16_ds_rand_s030.\", \"checkpoint_path\": \"N/A\", \"log_path\": \"N/A\"}, \"completed_at\": \"2026-05-14T08:03:54.114Z\"}, \"bf16_random_s025\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T05:33:35.036Z\", \"updated_at\": \"2026-05-14T08:03:52.921Z\", \"hypothesis\": \"bf16 DeepSeek random masking s=0.25。与 bf16_importance_s025 对照。\", \"notes\": \"Superseded by bf16_ds_rand_s025 (DONE, success)\", \"conclusion\": \"killed\", \"spec\": {\"notes\": \"Superseded by bf16_ds_rand_s025.\", \"checkpoint_path\": \"N/A\", \"log_path\": \"N/A\"}, \"completed_at\": \"2026-05-14T08:03:52.921Z\"}, \"bf16_random_s020\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T05:33:34.093Z\", \"updated_at\": \"2026-05-14T08:03:51.648Z\", \"hypothesis\": \"bf16 DeepSeek random masking s=0.20。与 bf16_importance_s020 对照。\", \"notes\": \"Superseded by bf16_ds_rand_s020 (DONE, success)\", \"conclusion\": \"killed\", \"spec\": {\"notes\": \"Superseded by bf16_ds_rand_s020.\", \"checkpoint_path\": \"N/A\", \"log_path\": \"N/A\"}, \"completed_at\": \"2026-05-14T08:03:51.648Z\"}, \"bf16_random_s015\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T05:33:32.898Z\", \"updated_at\": \"2026-05-14T08:03:50.569Z\", \"hypothesis\": \"bf16 DeepSeek random masking s=0.15。与 bf16_importance_s015 对照，验证 importance vs random severity gradient。\", \"notes\": \"Superseded by bf16_ds_rand_s015 (DONE, success)\", \"conclusion\": \"killed\", \"spec\": {\"notes\": \"Superseded by bf16_ds_rand_s015.\", \"checkpoint_path\": \"N/A\", \"log_path\": \"N/A\"}, \"completed_at\": \"2026-05-14T08:03:50.569Z\"}, \"bf16_qwen_importance_s030\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T05:33:38.715Z\", \"updated_at\": \"2026-05-14T08:03:49.138Z\", \"hypothesis\": \"bf16 Qwen2.5-7B-Instruct importance masking s=0.30。Cross-model replication。\", \"notes\": \"Superseded by bf16_qw_imp_s030 (DONE, success)\", \"conclusion\": \"killed\", \"spec\": {\"notes\": \"Superseded by bf16_qw_imp_s030. Old placeholder.\", \"checkpoint_path\": \"N/A\", \"log_path\": \"N/A\"}, \"completed_at\": \"2026-05-14T08:03:49.138Z\"}, \"bf16_qwen_importance_s025\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T05:33:38.032Z\", \"updated_at\": \"2026-05-14T08:03:34.054Z\", \"hypothesis\": \"bf16 Qwen2.5-7B-Instruct importance masking s=0.25。Cross-model replication。\", \"conclusion\": \"killed\", \"spec\": {\"conclusion\": \"superseded\", \"notes\": \"Superseded by bf16_qw_imp_s025. Old placeholder.\", \"checkpoint_path\": \"N/A\", \"log_path\": \"N/A\"}, \"completed_at\": \"2026-05-14T08:03:24.414Z\", \"notes\": \"Superseded by bf16_qw_imp_s025 (DONE, success)\"}, \"bf16_qwen_importance_s020\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T05:33:37.207Z\", \"updated_at\": \"2026-05-14T08:03:33.224Z\", \"hypothesis\": \"bf16 Qwen2.5-7B-Instruct importance masking s=0.20。Cross-model replication。\", \"conclusion\": \"killed\", \"spec\": {\"conclusion\": \"superseded\", \"notes\": \"Superseded by bf16_qw_imp_s020. Old placeholder.\", \"checkpoint_path\": \"N/A\", \"log_path\": \"N/A\"}, \"completed_at\": \"2026-05-14T08:03:23.200Z\", \"notes\": \"Superseded by bf16_qw_imp_s020 (DONE, success)\"}, \"bf16_qwen_importance_s015\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T05:33:36.354Z\", \"updated_at\": \"2026-05-14T08:03:32.300Z\", \"hypothesis\": \"bf16 Qwen2.5-7B-Instruct importance masking s=0.15。Cross-model replication，验证 phase-modulated severity 在非 DeepSeek 模型上复现。\", \"conclusion\": \"killed\", \"spec\": {\"conclusion\": \"superseded\", \"notes\": \"Superseded by bf16_qw_imp_s015. Old placeholder.\", \"checkpoint_path\": \"N/A\", \"log_path\": \"N/A\"}, \"completed_at\": \"2026-05-14T08:03:21.798Z\", \"notes\": \"Superseded by bf16_qw_imp_s015 (DONE, success)\"}, \"v6_random_s030_r3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T05:34:34.110Z\", \"updated_at\": \"2026-05-14T07:02:24.759Z\", \"hypothesis\": \"v6 random masking s=0.30 重试 (cuda:2)。前次被误杀+tmux冲突。获取 per_problem_ii 用于 importance vs random problem-level permutation test。与 v6_importance_s030 形成对照。\", \"server\": \"westd-22162\", \"gpu\": \"cuda:2\", \"account\": \"root\", \"reproduce\": {\"server\": \"westd-22162\", \"gpu\": \"cuda:2\", \"started_at\": \"2026-05-14T05:35:14.593Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/pacs && python -m pacs.profiling.run_profiling --model_path /root/autodl-tmp/pacs/checkpoints/DeepSeek-R1-Distill-Qwen-7B --data_path /root/autodl-tmp/pacs/data/math500.json --output_dir /root/autodl-tmp/pacs/profiling_output_v6_random_s030_r3 --sparsity_levels 0.30 --masking_method random --max_new_tokens 2048 --min_phase_length 10 --max_problems 50\\\"\", \"code_commit\": \"5488041765f165e4e64323cfda552de868351f86\", \"finished_at\": \"2026-05-14T06:04:55.039Z\", \"training_hours\": 0.49}, \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/pacs && python -m pacs.profiling.run_profiling --model_path /root/autodl-tmp/pacs/checkpoints/DeepSeek-R1-Distill-Qwen-7B --data_path /root/autodl-tmp/pacs/data/math500.json --output_dir /root/autodl-tmp/pacs/profiling_output_v6_random_s030_r3 --sparsity_levels 0.30 --masking_method random --max_new_tokens 2048 --min_phase_length 10 --max_problems 50\\\"\", \"server\": \"westd-22162\", \"gpu\": [\"cuda:2\"], \"pid\": \"77560\", \"log_path\": \"~/runs/phase-gated-compound-sparse/v6_random_s030_r3.log\", \"submitted_at\": \"2026-05-14T05:35:15.849Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 3769.7, \"gpu_hours\": 1.05}, \"pid\": \"77560\", \"log_path\": \"~/runs/phase-gated-compound-sparse/v6_random_s030_r3.log\", \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T06:05:03.633464+00:00\"}]}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/pacs/profiling_output_v6_random_s030_r3/profiling_results.json\", \"metrics\": {\"II_high_mean\": 9.2364, \"II_mid_mean\": -230.7604, \"II_low_mean\": -7.4119, \"II_high_median\": 4.0237, \"II_mid_median\": 2.4272, \"II_low_median\": 4.735, \"ppl_low_both\": 88.94, \"per_problem_count\": 50}, \"completed_at\": \"2026-05-14T06:38:05.564Z\", \"notes\": \"Verdict=PASS 是 outlier artifact：mid-phase 单个 extreme segment (skewness=-13.08) 将 mean 拉到 -230.76，而 median 平坦 (2.4-4.7)，无结构化 gradient。fp16 数据仅作参考，论文数据以 bf16 为准。\"}, \"qwen_importance_s030\": {\"status\": \"DONE\", \"retry_count\": 1, \"created_at\": \"2026-05-14T04:50:43.602Z\", \"updated_at\": \"2026-05-14T06:59:18.969Z\", \"hypothesis\": \"Cross-model replication: Qwen2.5-7B-Instruct importance masking s=0.30, cuda:3. 验证 phase-modulated severity 在非 DeepSeek 模型上是否复现。v6 代码含 per_problem_ii。\", \"completed_at\": \"2026-05-14T05:05:47.654Z\", \"extra\": {\"previous_failure\": {\"conclusion\": \"killed\"}}, \"conclusion\": \"killed\", \"notes\": \"已被 bf16_qw_imp_s030 替代。旧 fp16 实验，Director 指令清理。\"}, \"qwen_importance_s025\": {\"status\": \"DONE\", \"retry_count\": 1, \"created_at\": \"2026-05-14T04:50:43.235Z\", \"updated_at\": \"2026-05-14T06:59:18.110Z\", \"hypothesis\": \"Cross-model replication: Qwen2.5-7B-Instruct importance masking s=0.25, cuda:3. 验证 phase-modulated severity 在非 DeepSeek 模型上是否复现。v6 代码含 per_problem_ii。\", \"completed_at\": \"2026-05-14T05:05:47.242Z\", \"extra\": {\"previous_failure\": {\"conclusion\": \"killed\"}}, \"conclusion\": \"killed\", \"notes\": \"已被 bf16_qw_imp_s025 替代。旧 fp16 实验，Director 指令清理。\"}, \"qwen_importance_s020\": {\"status\": \"DONE\", \"retry_count\": 1, \"created_at\": \"2026-05-14T04:50:42.892Z\", \"updated_at\": \"2026-05-14T06:59:17.149Z\", \"hypothesis\": \"Cross-model replication: Qwen2.5-7B-Instruct importance masking s=0.20, cuda:1. 验证 phase-modulated severity 在非 DeepSeek 模型上是否复现。v6 代码含 per_problem_ii。\", \"completed_at\": \"2026-05-14T05:05:46.800Z\", \"extra\": {\"previous_failure\": {\"conclusion\": \"killed\"}}, \"conclusion\": \"killed\", \"notes\": \"已被 bf16_qw_imp_s020 替代。旧 fp16 实验，Director 指令清理。\"}, \"qwen_importance_s015\": {\"status\": \"DONE\", \"retry_count\": 1, \"created_at\": \"2026-05-14T04:50:42.558Z\", \"updated_at\": \"2026-05-14T06:59:16.342Z\", \"hypothesis\": \"Cross-model replication: Qwen2.5-7B-Instruct importance masking s=0.15, cuda:0. 验证 phase-modulated severity 在非 DeepSeek 模型上是否复现。v6 代码含 per_problem_ii。\", \"completed_at\": \"2026-05-14T05:05:59.407Z\", \"extra\": {\"previous_failure\": {\"conclusion\": \"killed\"}}, \"conclusion\": \"killed\", \"notes\": \"已被 bf16_qw_imp_s015 替代。旧 fp16 实验，Director 指令清理。\"}, \"v6_random_s025\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T05:11:50.836Z\", \"updated_at\": \"2026-05-14T05:59:32.155Z\", \"hypothesis\": \"v6 代码 random masking s=0.25, cuda:3. 获取 per_problem_ii 用于 importance vs random problem-level permutation test。与 v6_importance_s025 形成对照。\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/pacs && python -m pacs.profiling.run_profiling --model_path /root/autodl-tmp/pacs/checkpoints/DeepSeek-R1-Distill-Qwen-7B --data_path /root/autodl-tmp/pacs/data/math500.json --output_dir /root/autodl-tmp/pacs/profiling_output_v6_random_s025 --sparsity_levels 0.25 --masking_method random --max_new_tokens 2048 --min_phase_length 10 --max_problems 50\\\"\", \"server\": \"westd-22162\", \"gpu\": [\"cuda:3\"], \"pid\": \"73459\", \"log_path\": \"~/runs/phase-gated-compound-sparse/v6_random_s025.log\", \"submitted_at\": \"2026-05-14T05:12:37.985Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/pacs/data/math500.json\", \"data_count\": 50, \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B\", \"seed\": 42, \"checkpoint_path\": \"/root/autodl-tmp/pacs/profiling_output_v6_random_s025/\", \"wall_clock_seconds\": 2808.5, \"gpu_hours\": 0.78}, \"reproduce\": {\"finished_at\": \"2026-05-14T05:52:19.115Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T05:52:24.167364+00:00\"}]}, \"metrics\": {\"ii_high_median\": 3.0024, \"ii_mid_median\": 2.9846, \"ii_low_median\": 2.9146, \"ii_high_mean\": 3.9052, \"ii_mid_mean\": 7.9491, \"ii_low_mean\": 3.9114, \"per_problem_ii_count\": 50, \"n_high\": 36, \"n_mid\": 25, \"n_low\": 24, \"bootstrap_gradient_paired\": -0.1199, \"bootstrap_ci_paired\": [-1.517, 1.2461], \"bootstrap_p\": 0.559, \"bootstrap_gradient_unpaired\": -0.8616, \"bootstrap_ci_unpaired\": [-3.3911, 1.5169], \"per_problem_ii_stats\": {\"high\": {\"min\": -6.1388, \"max\": 25.2471, \"mean\": 4.4098, \"median\": 3.0421, \"std\": 6.0734}, \"mid\": {\"min\": 0.158, \"max\": 108.7242, \"mean\": 7.5626, \"median\": 2.1407, \"std\": 20.926}, \"low\": {\"min\": -0.1953, \"max\": 12.8555, \"mean\": 3.5806, \"median\": 2.7289, \"std\": 3.4915}}, \"verdict\": \"FAIL\"}, \"conclusion\": \"success\", \"notes\": \"Random baseline 确认：gradient=0.90 (≈1.0, 无 phase-dependent amplification)。三 phase median II 均在 2-3 范围 (high=3.04, mid=2.14, low=2.73)，几乎无差异。对比 importance masking (gradient=35.72, low_median=24.16)，证明 phase-dependent interaction gradient 是 importance-based masking 的特异效应，非 sparsity 本身的 artifact。\", \"completed_at\": \"2026-05-14T05:59:26.490Z\"}, \"v6_random_s015\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T04:54:17.188Z\", \"updated_at\": \"2026-05-14T05:59:25.315Z\", \"hypothesis\": \"v6 代码 random masking s=0.15, cuda:0. 获取 per_problem_ii 用于 importance vs random problem-level permutation test。与 v6_importance_s015 形成对照。\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/pacs && python -m pacs.profiling.run_profiling --model_path /root/autodl-tmp/pacs/checkpoints/DeepSeek-R1-Distill-Qwen-7B --data_path /root/autodl-tmp/pacs/data/math500.json --output_dir /root/autodl-tmp/pacs/profiling_output_v6_random_s015 --sparsity_levels 0.15 --masking_method random --max_new_tokens 2048 --min_phase_length 10 --max_problems 50\\\"\", \"server\": \"westd-22162\", \"gpu\": [\"cuda:0\"], \"pid\": \"72073\", \"log_path\": \"~/runs/phase-gated-compound-sparse/v6_random_s015.log\", \"submitted_at\": \"2026-05-14T05:08:13.748Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/pacs/data/math500.json\", \"data_count\": 50, \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B\", \"seed\": 42, \"checkpoint_path\": \"/root/autodl-tmp/pacs/profiling_output_v6_random_s015/\", \"wall_clock_seconds\": 3071.6, \"gpu_hours\": 0.85}, \"reproduce\": {\"finished_at\": \"2026-05-14T05:50:02.236Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T05:50:03.894084+00:00\"}]}, \"metrics\": {\"ii_high_median\": 0.1606, \"ii_mid_median\": 0.252, \"ii_low_median\": 0.1831, \"ii_high_mean\": 0.4563, \"ii_mid_mean\": 0.5134, \"ii_low_mean\": 0.4775, \"per_problem_ii_count\": 50, \"n_high\": 43, \"n_mid\": 32, \"n_low\": 28, \"bootstrap_gradient_paired\": -0.2722, \"bootstrap_ci_paired\": [-0.7039, 0.1548], \"bootstrap_p\": 0.903, \"bootstrap_gradient_unpaired\": -0.0592, \"bootstrap_ci_unpaired\": [-0.5341, 0.3877], \"per_problem_ii_stats\": {\"high\": {\"min\": -3.0621, \"max\": 5.018, \"mean\": 0.5386, \"median\": 0.2003, \"std\": 1.2085}, \"mid\": {\"min\": -2.7245, \"max\": 4.6713, \"mean\": 0.3977, \"median\": 0.299, \"std\": 1.1456}, \"low\": {\"min\": -0.4031, \"max\": 3.7005, \"mean\": 0.4806, \"median\": 0.2465, \"std\": 0.779}}, \"verdict\": \"FAIL\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-14T05:59:25.315Z\"}, \"v6_random_s020\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T04:54:17.661Z\", \"updated_at\": \"2026-05-14T05:53:21.318Z\", \"hypothesis\": \"v6 代码 random masking s=0.20, cuda:1. 获取 per_problem_ii 用于 importance vs random problem-level permutation test。与 v6_importance_s020 形成对照。\", \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/pacs/profiling_output_v6_random_s020/\", \"log_path\": \"~/runs/phase-gated-compound-sparse/v6_random_s020.log\"}, \"reproduce\": {\"finished_at\": \"2026-05-14T05:47:11.560Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T05:47:15.118578+00:00\"}]}, \"metrics\": {\"ii_high_mean\": 0.855584, \"ii_high_median\": 0.321331, \"ii_high_ci\": [-0.124133, 1.616883], \"ii_high_winsorized_mean\": 0.913496, \"ii_mid_mean\": 1.258123, \"ii_mid_median\": 0.455663, \"ii_mid_ci\": [0.674852, 2.075565], \"ii_mid_winsorized_mean\": 1.074102, \"ii_low_mean\": 0.956933, \"ii_low_median\": 0.591916, \"ii_low_ci\": [0.583856, 1.413355], \"ii_low_winsorized_mean\": 0.96113, \"n_high\": 511, \"n_mid\": 391, \"n_low\": 454, \"problems\": 50, \"per_problem_ii_count\": 50, \"gradient_mean_low_over_high\": 1.118, \"gradient_median_low_over_high\": 1.842, \"pass_fail\": \"FAIL\", \"perplexity_high_dense\": 1.1462, \"perplexity_high_both\": 7.9749, \"perplexity_mid_dense\": 1.1226, \"perplexity_mid_both\": 6.8553, \"perplexity_low_dense\": 1.1105, \"perplexity_low_both\": 22.5868}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-14T05:51:10.663Z\", \"notes\": \"Verdict=FAIL 是 random baseline 预期行为：统计检验未检测到结构化 II 梯度 = random 不具有 phase-dependent interaction pattern。Random masking 仍有正 II (mean 0.86-1.26)，但无 phase-dependent gradient (gradient_mean=1.12×, 近乎平坦)。这正是对照组预期结果。注意 high_sparsity skewness=-4.83，后续 permutation test 应用 winsorized mean 或 median。\"}, \"v6_random_s030_r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T05:32:09.051Z\", \"updated_at\": \"2026-05-14T05:49:21.289Z\", \"hypothesis\": \"v6 random masking s=0.30 重试 (cuda:2)。前次被误杀。获取 per_problem_ii 用于 importance vs random problem-level permutation test。与 v6_importance_s030 形成对照。\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/pacs && python -m pacs.profiling.run_profiling --model_path /root/autodl-tmp/pacs/checkpoints/DeepSeek-R1-Distill-Qwen-7B --data_path /root/autodl-tmp/pacs/data/math500.json --output_dir /root/autodl-tmp/pacs/profiling_output_v6_random_s030 --sparsity_levels 0.30 --masking_method random --max_new_tokens 2048 --min_phase_length 10 --max_problems 50\\\"\", \"server\": \"westd-22162\", \"gpu\": [\"cuda:2\"], \"pid\": \"77228\", \"log_path\": \"~/runs/phase-gated-compound-sparse/v6_random_s030_r2.log\", \"submitted_at\": \"2026-05-14T05:33:33.451Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 945.1, \"gpu_hours\": 0.26}, \"notes\": \"tmux session 冲突，废弃。实际提交用 v6_random_s030_r3\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-14T05:49:18.558Z\", \"failure_reason\": \"bash-in-sh syntax error: allocate_and_submit 未用 bash -c 包装 source 命令，tmux /bin/sh 无法执行。EXIT_CODE=127。实际重试为 v6_random_s030_r3。\"}, \"v6_random_s030\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T05:12:49.055Z\", \"updated_at\": \"2026-05-14T05:32:08.415Z\", \"hypothesis\": \"v6 代码 random masking s=0.30, cuda:2. 获取 per_problem_ii 用于 importance vs random problem-level permutation test。与 v6_importance_s030 形成对照。\", \"server\": \"westd-22162\", \"gpu\": \"cuda:2\", \"account\": \"root\", \"reproduce\": {\"server\": \"westd-22162\", \"gpu\": \"cuda:2\", \"started_at\": \"2026-05-14T05:16:10.111Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/pacs && python -m pacs.profiling.run_profiling --model_path /root/autodl-tmp/pacs/checkpoints/DeepSeek-R1-Distill-Qwen-7B --data_path /root/autodl-tmp/pacs/data/math500.json --output_dir /root/autodl-tmp/pacs/profiling_output_v6_random_s030 --sparsity_levels 0.30 --masking_method random --max_new_tokens 2048 --min_phase_length 10 --max_problems 50\\\"\", \"code_commit\": \"5488041765f165e4e64323cfda552de868351f86\", \"finished_at\": \"2026-05-14T05:20:46.696Z\", \"training_hours\": 0.08}, \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/pacs && python -m pacs.profiling.run_profiling --model_path /root/autodl-tmp/pacs/checkpoints/DeepSeek-R1-Distill-Qwen-7B --data_path /root/autodl-tmp/pacs/data/math500.json --output_dir /root/autodl-tmp/pacs/profiling_output_v6_random_s030 --sparsity_levels 0.30 --masking_method random --max_new_tokens 2048 --min_phase_length 10 --max_problems 50\\\"\", \"server\": \"westd-22162\", \"gpu\": [\"cuda:2\"], \"pid\": \"74583\", \"log_path\": \"~/runs/phase-gated-compound-sparse/v6_random_s030.log\", \"submitted_at\": \"2026-05-14T05:16:12.258Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 275.5, \"gpu_hours\": 0.08}, \"pid\": \"74583\", \"log_path\": \"~/runs/phase-gated-compound-sparse/v6_random_s030.log\", \"failure_reason\": \"EXIT_CODE=143 (SIGTERM — graceful kill)\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-14T05:20:47.782Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-14T05:20:49.121184+00:00\"}]}, \"notes\": \"被 bf16-nan-fix Worker 误杀 tmux session。需重跑 → v6_random_s030_r2\"}, \"v6_importance_s030\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T03:47:20.641Z\", \"updated_at\": \"2026-05-14T04:48:16.024Z\", \"hypothesis\": \"v6 per-problem II 修复: importance masking s=0.30, cuda:3. 输出含 per_problem_ii 字段(50条), 用于 problem-level bootstrap CI.\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/pacs && python -m pacs.profiling.run_profiling --model_path /root/autodl-tmp/pacs/checkpoints/DeepSeek-R1-Distill-Qwen-7B --data_path /root/autodl-tmp/pacs/data/math500.json --output_dir /root/autodl-tmp/pacs/profiling_output_v6_importance_s030 --sparsity_levels 0.30 --masking_method importance --max_new_tokens 2048 --min_phase_length 10 --max_problems 50\\\"\", \"server\": \"westd-22162\", \"gpu\": [\"cuda:3\"], \"pid\": \"63113\", \"log_path\": \"/root/autodl-tmp/pacs/profiling_output_v6_importance_s030/\", \"submitted_at\": \"2026-05-14T03:47:45.764Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/pacs/data/math500.json\", \"data_count\": 50, \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B\", \"seed\": 42, \"checkpoint_path\": \"/root/autodl-tmp/pacs/profiling_output_v6_importance_s030/\", \"wall_clock_seconds\": 3464.0, \"gpu_hours\": 0.96}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-14T04:45:29.715Z\", \"metrics\": {\"ii_high_median\": 0.8833, \"ii_mid_median\": 7.2706, \"ii_low_median\": 34.6937, \"ii_high_mean\": 1.5151, \"ii_mid_mean\": 78.8215, \"ii_low_mean\": 1163.9677, \"per_problem_ii_count\": 50, \"n_high\": 40, \"n_mid\": 22, \"n_low\": 20, \"problems\": 50, \"bootstrap_gradient_paired\": 41.92, \"bootstrap_ci_paired\": [19.14, 299.76], \"bootstrap_gradient_unpaired\": 39.28, \"bootstrap_ci_unpaired\": [21.87, 129.59], \"bootstrap_p\": 0}}, \"v6_importance_s025\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T03:47:19.997Z\", \"updated_at\": \"2026-05-14T04:48:14.257Z\", \"hypothesis\": \"v6 per-problem II 修复: importance masking s=0.25, cuda:2. 输出含 per_problem_ii 字段(50条), 用于 problem-level bootstrap CI.\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/pacs && python -m pacs.profiling.run_profiling --model_path /root/autodl-tmp/pacs/checkpoints/DeepSeek-R1-Distill-Qwen-7B --data_path /root/autodl-tmp/pacs/data/math500.json --output_dir /root/autodl-tmp/pacs/profiling_output_v6_importance_s025 --sparsity_levels 0.25 --masking_method importance --max_new_tokens 2048 --min_phase_length 10 --max_problems 50\\\"\", \"server\": \"westd-22162\", \"gpu\": [\"cuda:2\"], \"pid\": \"62967\", \"log_path\": \"/root/autodl-tmp/pacs/profiling_output_v6_importance_s025/\", \"submitted_at\": \"2026-05-14T03:47:44.036Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/pacs/data/math500.json\", \"data_count\": 50, \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B\", \"seed\": 42, \"checkpoint_path\": \"/root/autodl-tmp/pacs/profiling_output_v6_importance_s025/\", \"wall_clock_seconds\": 3465.3, \"gpu_hours\": 0.96}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-14T04:45:29.294Z\", \"metrics\": {\"ii_high_median\": 0.6641, \"ii_mid_median\": 5.3067, \"ii_low_median\": 24.1619, \"ii_high_mean\": 0.8842, \"ii_mid_mean\": 10.057, \"ii_low_mean\": 71.8854, \"per_problem_ii_count\": 50, \"n_high\": 42, \"n_mid\": 23, \"n_low\": 21, \"problems\": 50, \"bootstrap_gradient_paired\": 35.72, \"bootstrap_ci_paired\": [9.52, 101.54], \"bootstrap_gradient_unpaired\": 36.38, \"bootstrap_ci_unpaired\": [13.19, 97.61], \"bootstrap_p\": 0}}, \"v6_importance_s020\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T03:52:50.615Z\", \"updated_at\": \"2026-05-14T04:48:11.899Z\", \"hypothesis\": \"v6 per-problem II 修复: importance masking s=0.20, cuda:1. 输出含 per_problem_ii 字段(50条), 用于 problem-level bootstrap CI.\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/pacs && python -m pacs.profiling.run_profiling --model_path /root/autodl-tmp/pacs/checkpoints/DeepSeek-R1-Distill-Qwen-7B --data_path /root/autodl-tmp/pacs/data/math500.json --output_dir /root/autodl-tmp/pacs/profiling_output_v6_importance_s020 --sparsity_levels 0.20 --masking_method importance --max_new_tokens 2048 --min_phase_length 10 --max_problems 50\\\"\", \"server\": \"westd-22162\", \"gpu\": [\"cuda:1\"], \"pid\": \"64548\", \"log_path\": \"/root/autodl-tmp/pacs/profiling_output_v6_importance_s020/\", \"submitted_at\": \"2026-05-14T03:55:42.705Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/pacs/data/math500.json\", \"data_count\": 50, \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B\", \"seed\": 42, \"checkpoint_path\": \"/root/autodl-tmp/pacs/profiling_output_v6_importance_s020/\", \"wall_clock_seconds\": 2985.5, \"gpu_hours\": 0.83}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-14T04:45:28.171Z\", \"metrics\": {\"ii_high_median\": 0.3353, \"ii_mid_median\": 1.6733, \"ii_low_median\": 9.2538, \"ii_high_mean\": 0.4936, \"ii_mid_mean\": 4.9538, \"ii_low_mean\": 25.8764, \"per_problem_ii_count\": 50, \"n_high\": 42, \"n_mid\": 28, \"n_low\": 21, \"problems\": 50, \"bootstrap_gradient_paired\": 11.05, \"bootstrap_ci_paired\": [5.42, 69.27], \"bootstrap_gradient_unpaired\": 27.6, \"bootstrap_ci_unpaired\": [6.55, 75.16], \"bootstrap_p\": 0}}, \"v6_importance_s015\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T03:52:50.334Z\", \"updated_at\": \"2026-05-14T04:48:09.482Z\", \"hypothesis\": \"v6 per-problem II 修复: importance masking s=0.15, cuda:0. 输出含 per_problem_ii 字段(50条), 用于 problem-level bootstrap CI.\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/pacs && python -m pacs.profiling.run_profiling --model_path /root/autodl-tmp/pacs/checkpoints/DeepSeek-R1-Distill-Qwen-7B --data_path /root/autodl-tmp/pacs/data/math500.json --output_dir /root/autodl-tmp/pacs/profiling_output_v6_importance_s015 --sparsity_levels 0.15 --masking_method importance --max_new_tokens 2048 --min_phase_length 10 --max_problems 50\\\"\", \"server\": \"westd-22162\", \"gpu\": [\"cuda:0\"], \"pid\": \"64408\", \"log_path\": \"/root/autodl-tmp/pacs/profiling_output_v6_importance_s015/\", \"submitted_at\": \"2026-05-14T03:55:41.270Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/pacs/data/math500.json\", \"data_count\": 50, \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B\", \"seed\": 42, \"checkpoint_path\": \"/root/autodl-tmp/pacs/profiling_output_v6_importance_s015/\", \"wall_clock_seconds\": 2986.1, \"gpu_hours\": 0.83}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-14T04:45:27.320Z\", \"metrics\": {\"ii_high_median\": 0.2266, \"ii_mid_median\": 0.7432, \"ii_low_median\": 2.8762, \"ii_high_mean\": 0.2874, \"ii_mid_mean\": 1.6858, \"ii_low_mean\": 8.5161, \"per_problem_ii_count\": 50, \"n_high\": 43, \"n_mid\": 32, \"n_low\": 24, \"problems\": 50, \"bootstrap_gradient_paired\": 11.53, \"bootstrap_ci_paired\": [3.49, 23.78], \"bootstrap_gradient_unpaired\": 12.69, \"bootstrap_ci_unpaired\": [4.96, 28.45], \"bootstrap_p\": 0}}, \"mvp_v5_random_s020\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T03:01:33.304Z\", \"updated_at\": \"2026-05-14T04:00:15.079Z\", \"hypothesis\": \"v5 修复后代码 random masking baseline, sparsity=0.20, cuda:2。与 mvp_v5_fixed_s020_r2 (importance) 形成对照组。D015 Go/No-Go 判定所需：比较 importance vs random median gradient。\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/pacs && python -m pacs.profiling.run_profiling --model_path /root/autodl-tmp/pacs/checkpoints/DeepSeek-R1-Distill-Qwen-7B --data_path /root/autodl-tmp/pacs/data/math500.json --output_dir /root/autodl-tmp/pacs/profiling_output_v5_random_s020 --sparsity_levels 0.20 --masking_method random --max_new_tokens 2048 --min_phase_length 10\\\"\", \"server\": \"westd-22162\", \"gpu\": [\"cuda:0\"], \"pid\": \"59323\", \"log_path\": \"~/runs/phase-gated-compound-sparse/mvp_v5_random_s020.log\", \"submitted_at\": \"2026-05-14T03:29:59.607Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 1504.3, \"gpu_hours\": 0.42}, \"server\": \"westd-22162\", \"gpu\": \"cuda:0\", \"account\": \"root\", \"reproduce\": {\"server\": \"westd-22162\", \"gpu\": \"cuda:0\", \"started_at\": \"2026-05-14T03:29:57.757Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/pacs && python -m pacs.profiling.run_profiling --model_path /root/autodl-tmp/pacs/checkpoints/DeepSeek-R1-Distill-Qwen-7B --data_path /root/autodl-tmp/pacs/data/math500.json --output_dir /root/autodl-tmp/pacs/profiling_output_v5_random_s020 --sparsity_levels 0.20 --masking_method random --max_new_tokens 2048 --min_phase_length 10\\\"\", \"code_commit\": \"5488041765f165e4e64323cfda552de868351f86\", \"finished_at\": \"2026-05-14T03:55:03.243Z\", \"training_hours\": 0.42}, \"pid\": \"59323\", \"log_path\": \"~/runs/phase-gated-compound-sparse/mvp_v5_random_s020.log\", \"failure_reason\": \"EXIT_CODE=137 (SIGKILL — OOM killer or manual kill)\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-14T03:55:03.880Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-14T03:55:05.833184+00:00\"}]}, \"metrics\": {\"ii_high_median\": 0.321331, \"ii_mid_median\": 0.455663, \"ii_low_median\": 0.591916, \"ii_high_mean\": 0.855584, \"ii_mid_mean\": 1.258123, \"ii_low_mean\": 0.956933, \"ii_high_ci\": [-0.124133, 1.616883], \"ii_mid_ci\": [0.674852, 2.075565], \"ii_low_ci\": [0.583856, 1.413355], \"kv_ppl_high\": 4.2537, \"kv_ppl_mid\": 4.3064, \"kv_ppl_low\": 5.4048, \"both_ppl_high\": 7.9749, \"both_ppl_mid\": 6.8553, \"both_ppl_low\": 22.5868, \"problems\": 50}, \"notes\": \"50/50 completed successfully. EXIT_CODE=137 is false alarm — process completed, saved results, then was killed during cleanup. Log confirms: Results saved to profiling_output_v5_random_s020/profiling_results.json. Cron on_failed hook fired due to non-zero exit code, but results are valid.\", \"checkpoint_path\": \"/root/autodl-tmp/pacs/profiling_output_v5_random_s020/profiling_results.json\"}, \"mvp_v5_random_s030\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T03:01:34.781Z\", \"updated_at\": \"2026-05-14T04:00:14.269Z\", \"hypothesis\": \"v5 修复后代码 random masking baseline, sparsity=0.30, cuda:3。与 mvp_v5_fixed_s030_r2 (importance) 形成对照组。D015 Go/No-Go 判定所需：比较 importance vs random median gradient。\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/pacs && python -m pacs.profiling.run_profiling --model_path /root/autodl-tmp/pacs/checkpoints/DeepSeek-R1-Distill-Qwen-7B --data_path /root/autodl-tmp/pacs/data/math500.json --output_dir /root/autodl-tmp/pacs/profiling_output_v5_random_s030 --sparsity_levels 0.30 --masking_method random --max_new_tokens 2048 --min_phase_length 10\\\"\", \"server\": \"westd-22162\", \"gpu\": [\"cuda:1\"], \"pid\": \"59611\", \"log_path\": \"~/runs/phase-gated-compound-sparse/mvp_v5_random_s030.log\", \"submitted_at\": \"2026-05-14T03:30:02.258Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 1510.1, \"gpu_hours\": 0.42}, \"server\": \"westd-22162\", \"gpu\": \"cuda:1\", \"account\": \"root\", \"reproduce\": {\"server\": \"westd-22162\", \"gpu\": \"cuda:1\", \"started_at\": \"2026-05-14T03:30:01.102Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/pacs && python -m pacs.profiling.run_profiling --model_path /root/autodl-tmp/pacs/checkpoints/DeepSeek-R1-Distill-Qwen-7B --data_path /root/autodl-tmp/pacs/data/math500.json --output_dir /root/autodl-tmp/pacs/profiling_output_v5_random_s030 --sparsity_levels 0.30 --masking_method random --max_new_tokens 2048 --min_phase_length 10\\\"\", \"code_commit\": \"5488041765f165e4e64323cfda552de868351f86\", \"finished_at\": \"2026-05-14T03:55:08.968Z\", \"training_hours\": 0.42}, \"pid\": \"59611\", \"log_path\": \"~/runs/phase-gated-compound-sparse/mvp_v5_random_s030.log\", \"failure_reason\": \"EXIT_CODE=137 (SIGKILL — OOM killer or manual kill)\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-14T03:55:12.403Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-14T03:55:15.813219+00:00\"}]}, \"metrics\": {\"ii_high_median\": 5.377512, \"ii_mid_median\": 5.886454, \"ii_low_median\": 3.776818, \"ii_high_mean\": 22.734534, \"ii_mid_mean\": 10.943319, \"ii_low_mean\": 11.840449, \"ii_high_ci\": [10.352118, 42.551951], \"ii_mid_ci\": [7.398611, 14.765315], \"ii_low_ci\": [4.097309, 23.545273], \"kv_ppl_high\": 8.1027, \"kv_ppl_mid\": 8.5701, \"kv_ppl_low\": 13.4922, \"both_ppl_high\": 41.3452, \"both_ppl_mid\": 24.1992, \"both_ppl_low\": 68.5301, \"problems\": 50}, \"notes\": \"50/50 completed successfully. EXIT_CODE=137 is false alarm — process completed, saved results, then was killed during cleanup. Log confirms: Results saved to profiling_output_v5_random_s030/profiling_results.json. Cron on_failed hook fired due to non-zero exit code, but results are valid.\", \"checkpoint_path\": \"/root/autodl-tmp/pacs/profiling_output_v5_random_s030/profiling_results.json\"}, \"mvp_v5_random_s025\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T02:19:32.243Z\", \"updated_at\": \"2026-05-14T03:04:45.157Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/pacs && python -m pacs.profiling.run_profiling --model_path /root/autodl-tmp/pacs/checkpoints/DeepSeek-R1-Distill-Qwen-7B --data_path /root/autodl-tmp/pacs/data/math500.json --output_dir /root/autodl-tmp/pacs/profiling_output_v5_random_s025 --sparsity_levels 0.25 --masking_method random --max_new_tokens 2048 --min_phase_length 10\\\"\", \"server\": \"westd-22162\", \"gpu\": \"cuda:3\", \"pid\": \"52093\", \"log_path\": \"/root/autodl-tmp/pacs/profiling_output_v5_random_s025/\", \"submitted_at\": \"2026-05-14T02:19:32.155Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/pacs/data/math500.json\", \"data_count\": 50, \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B\", \"seed\": 42, \"checkpoint_path\": \"/root/autodl-tmp/pacs/profiling_output_v5_random_s025/\", \"wall_clock_seconds\": 2696.9, \"gpu_hours\": 0.75}, \"hypothesis\": \"v5 修复后代码 random masking baseline, sparsity=0.25, cuda:3。与 mvp_v5_fixed_s025 (importance) 形成对照组。用修复后同一代码确保公平对比。\", \"reproduce\": {\"finished_at\": \"2026-05-14T02:58:16.618Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T02:58:19.325558+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"ii_high_median\": 3.0024, \"ii_mid_median\": 2.9846, \"ii_low_median\": 2.9146, \"ii_high_mean\": 3.9052, \"ii_mid_mean\": 7.9491, \"ii_low_mean\": 3.9114, \"ii_high_ci\": [0.98, 6.34], \"ii_mid_ci\": [4.67, 11.87], \"ii_low_ci\": [2.71, 5.24], \"kv_ppl_high\": 6.39, \"kv_ppl_mid\": 6.11, \"kv_ppl_low\": 9.07, \"both_ppl_high\": 17.06, \"both_ppl_mid\": 15.38, \"both_ppl_low\": 29.32, \"problems\": 50}, \"completed_at\": \"2026-05-14T03:04:29.033Z\"}, \"mvp_v5_random_s015\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T02:19:30.549Z\", \"updated_at\": \"2026-05-14T03:04:44.225Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/pacs && python -m pacs.profiling.run_profiling --model_path /root/autodl-tmp/pacs/checkpoints/DeepSeek-R1-Distill-Qwen-7B --data_path /root/autodl-tmp/pacs/data/math500.json --output_dir /root/autodl-tmp/pacs/profiling_output_v5_random_s015 --sparsity_levels 0.15 --masking_method random --max_new_tokens 2048 --min_phase_length 10\\\"\", \"server\": \"westd-22162\", \"gpu\": \"cuda:2\", \"pid\": \"51951\", \"log_path\": \"/root/autodl-tmp/pacs/profiling_output_v5_random_s015/\", \"submitted_at\": \"2026-05-14T02:19:30.478Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/pacs/data/math500.json\", \"data_count\": 50, \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B\", \"seed\": 42, \"checkpoint_path\": \"/root/autodl-tmp/pacs/profiling_output_v5_random_s015/\", \"wall_clock_seconds\": 2697.6, \"gpu_hours\": 0.75}, \"hypothesis\": \"v5 修复后代码 random masking baseline, sparsity=0.15, cuda:2。与 mvp_v5_fixed_s015 (importance) 形成对照组。用修复后同一代码确保公平对比。\", \"reproduce\": {\"finished_at\": \"2026-05-14T02:58:13.456Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T02:58:14.836532+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"ii_high_median\": 0.1606, \"ii_mid_median\": 0.252, \"ii_low_median\": 0.1831, \"ii_high_mean\": 0.4563, \"ii_mid_mean\": 0.5134, \"ii_low_mean\": 0.4775, \"ii_high_ci\": [0.12, 0.77], \"ii_mid_ci\": [0.34, 0.74], \"ii_low_ci\": [0.28, 0.7], \"kv_ppl_high\": 3.14, \"kv_ppl_mid\": 2.91, \"kv_ppl_low\": 3.61, \"both_ppl_high\": 3.92, \"both_ppl_mid\": 4.14, \"both_ppl_low\": 4.71, \"problems\": 50}, \"completed_at\": \"2026-05-14T03:04:28.108Z\"}, \"mvp_v5_fixed_s030_r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T02:10:05.072Z\", \"updated_at\": \"2026-05-14T03:02:07.537Z\", \"spec\": {\"command\": \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/pacs && python -m pacs.profiling.run_profiling --model_path /root/autodl-tmp/pacs/checkpoints/DeepSeek-R1-Distill-Qwen-7B --data_path /root/autodl-tmp/pacs/data/math500.json --output_dir /root/autodl-tmp/pacs/profiling_output_v5_s030_r2 --sparsity_levels 0.30 --max_new_tokens 2048 --min_phase_length 10\", \"server\": \"westd-22162\", \"gpu\": \"cuda:1\", \"pid\": \"unknown\", \"log_path\": \"/root/autodl-tmp/pacs/profiling_output_v5_s030_r2/\", \"submitted_at\": \"2026-05-14T02:10:05.010Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/pacs/data/math500.json\", \"data_count\": 50, \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B\", \"seed\": 42, \"checkpoint_path\": \"/root/autodl-tmp/pacs/profiling_output_v5_s030_r2/\", \"wall_clock_seconds\": 3098.1, \"gpu_hours\": 0.86}, \"hypothesis\": \"v5修复验证(重启): NaN skip + position normalization后, importance masking sparsity=0.30的II应为负(sub-additive). 前次运行(s030)在35/50时被误杀。s=0.30是最关键的验证点。\", \"conclusion\": \"negative\", \"completed_at\": \"2026-05-14T03:01:43.081Z\", \"metrics\": {\"ii_high_median\": 0.5964, \"ii_mid_median\": 7.4671, \"ii_low_median\": 44.6324, \"ii_high_mean\": 1.1832, \"ii_mid_mean\": 168.53, \"ii_low_mean\": 1926.23, \"ii_high_ci\": [0.86, 1.6], \"ii_mid_ci\": [36.91, 348.21], \"ii_low_ci\": [179.17, 4062.57], \"kv_ppl_high\": 1.4, \"kv_ppl_mid\": 15.11, \"kv_ppl_low\": 40.79, \"both_ppl_high\": 5.71, \"both_ppl_mid\": 137.61, \"both_ppl_low\": 963.2, \"problems\": 50}}, \"mvp_v5_fixed_s020_r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T02:10:03.689Z\", \"updated_at\": \"2026-05-14T03:02:03.793Z\", \"spec\": {\"command\": \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/pacs && python -m pacs.profiling.run_profiling --model_path /root/autodl-tmp/pacs/checkpoints/DeepSeek-R1-Distill-Qwen-7B --data_path /root/autodl-tmp/pacs/data/math500.json --output_dir /root/autodl-tmp/pacs/profiling_output_v5_s020_r2 --sparsity_levels 0.20 --max_new_tokens 2048 --min_phase_length 10\", \"server\": \"westd-22162\", \"gpu\": \"cuda:0\", \"pid\": \"unknown\", \"log_path\": \"/root/autodl-tmp/pacs/profiling_output_v5_s020_r2/\", \"submitted_at\": \"2026-05-14T02:10:03.634Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/pacs/data/math500.json\", \"data_count\": 50, \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B\", \"seed\": 42, \"checkpoint_path\": \"/root/autodl-tmp/pacs/profiling_output_v5_s020_r2/\", \"wall_clock_seconds\": 3098.0, \"gpu_hours\": 0.86}, \"hypothesis\": \"v5修复验证(重启): NaN skip + position normalization后, importance masking sparsity=0.20的II应为负(sub-additive). 前次运行(s020)在35/50时被误杀。\", \"conclusion\": \"negative\", \"completed_at\": \"2026-05-14T03:01:41.598Z\", \"metrics\": {\"ii_high_median\": 0.3333, \"ii_mid_median\": 1.5479, \"ii_low_median\": 9.5627, \"ii_high_mean\": 0.5044, \"ii_mid_mean\": 3.5155, \"ii_low_mean\": 31.8937, \"ii_high_ci\": [0.41, 0.62], \"ii_mid_ci\": [2.29, 5.35], \"ii_low_ci\": [18.74, 47.22], \"kv_ppl_high\": 1.24, \"kv_ppl_mid\": 3.65, \"kv_ppl_low\": 14.11, \"both_ppl_high\": 2.7, \"both_ppl_mid\": 8.13, \"both_ppl_low\": 42.64, \"problems\": 50}}, \"mvp_v5_fixed_s030\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T01:26:05.204Z\", \"updated_at\": \"2026-05-14T02:36:08.288Z\", \"spec\": {\"command\": \"python run_profiling.py --model /root/autodl-tmp/models/DeepSeek-R1-Distill-Qwen-7B --sparsity 0.30 --output_dir profiling_output_v5_s030 --max_problems 50\", \"server\": \"westd-22162\", \"data_path\": \"MATH-500 (embedded)\", \"data_count\": 50, \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B\", \"seed\": 42, \"pid\": 46940, \"gpu\": \"cuda:1\", \"hypothesis\": \"v5修复验证: NaN skip + position normalization后, importance masking sparsity=0.30的II应为负(sub-additive)\", \"notes\": \"Killed at 35/50 by ops worker (kill-and-prep-v5-restart). Needs restart.\", \"log_path\": \"/root/autodl-tmp/pacs/profiling_output_v5_s030.log\", \"checkpoint_path\": \"N/A - killed before completion\"}, \"hypothesis\": \"v5 修复验证：NaN skip + position normalization, importance masking sparsity=0.30, cuda:1。验证修复后 importance eviction 是否正常（kv_ppl < random baseline）。\", \"conclusion\": \"killed\", \"completed_at\": \"2026-05-14T02:09:18.077Z\", \"metrics\": {\"ii_high\": 1.18, \"ii_mid\": 168.53, \"ii_low\": 1926.23, \"ii_high_ci\": [0.86, 1.6], \"ii_mid_ci\": [36.91, 348.21], \"ii_low_ci\": [179.17, 4062.57], \"ii_high_median\": 0.6, \"ii_mid_median\": 7.47, \"ii_low_median\": 44.63, \"kv_ppl_high\": 1.4, \"kv_ppl_mid\": 15.11, \"kv_ppl_low\": 40.79, \"both_ppl_high\": 5.71, \"both_ppl_mid\": 137.61, \"both_ppl_low\": 963.2, \"problems\": 50, \"⚠️_WARNING\": \"pre-fix code, INVALIDATED. Results found on disk after kill but code lacked conda activation fix. Do NOT cite these numbers.\"}}, \"mvp_v5_fixed_s020\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T01:26:04.454Z\", \"updated_at\": \"2026-05-14T02:36:04.306Z\", \"spec\": {\"command\": \"python run_profiling.py --model /root/autodl-tmp/models/DeepSeek-R1-Distill-Qwen-7B --sparsity 0.20 --output_dir profiling_output_v5_s020 --max_problems 50\", \"server\": \"westd-22162\", \"data_path\": \"MATH-500 (embedded)\", \"data_count\": 50, \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B\", \"seed\": 42, \"pid\": 46574, \"gpu\": \"cuda:0\", \"hypothesis\": \"v5修复验证: NaN skip + position normalization后, importance masking sparsity=0.20的II应为负(sub-additive)\", \"notes\": \"Killed at 35/50 by ops worker (kill-and-prep-v5-restart). Needs restart.\", \"log_path\": \"/root/autodl-tmp/pacs/profiling_output_v5_s020.log\", \"checkpoint_path\": \"N/A - killed before completion\"}, \"hypothesis\": \"v5 修复验证：NaN skip + position normalization, importance masking sparsity=0.20, cuda:0。验证修复后 importance eviction 是否正常（kv_ppl < random baseline）。\", \"conclusion\": \"killed\", \"completed_at\": \"2026-05-14T02:09:16.728Z\", \"metrics\": {\"ii_high\": 0.5, \"ii_mid\": 3.52, \"ii_low\": 31.89, \"ii_high_ci\": [0.41, 0.62], \"ii_mid_ci\": [2.29, 5.35], \"ii_low_ci\": [18.74, 47.22], \"ii_high_median\": 0.33, \"ii_mid_median\": 1.55, \"ii_low_median\": 9.56, \"kv_ppl_high\": 1.24, \"kv_ppl_mid\": 3.65, \"kv_ppl_low\": 14.11, \"both_ppl_high\": 2.7, \"both_ppl_mid\": 8.13, \"both_ppl_low\": 42.64, \"problems\": 50, \"⚠️_WARNING\": \"pre-fix code, INVALIDATED. Results found on disk after kill but code lacked conda activation fix. Do NOT cite these numbers.\"}}, \"mvp_v5_fixed_s025\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T01:31:10.384Z\", \"updated_at\": \"2026-05-14T02:15:34.177Z\", \"spec\": {\"hypothesis\": \"v5修复验证: NaN skip + position normalization后, importance masking sparsity=0.25的II应为负(sub-additive)\", \"server\": \"westd-22162\", \"gpu\": \"cuda:3\", \"command\": \"python run_profiling.py --model /root/autodl-tmp/models/DeepSeek-R1-Distill-Qwen-7B --sparsity 0.25 --output_dir profiling_output_v5_s025 --max_problems 50\", \"data_path\": \"MATH-500 (embedded)\", \"data_count\": 50, \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B\", \"seed\": 42, \"pid\": 48403, \"checkpoint_path\": \"/root/autodl-tmp/pacs/profiling_output_v5_s025/\", \"log_path\": \"/root/autodl-tmp/pacs/profiling_output_v5_s025/\"}, \"metrics\": {\"ii_high\": 0.851, \"ii_mid\": 9.306, \"ii_low\": 96.715, \"ii_high_ci\": [0.703, 0.999], \"ii_mid_ci\": [6.092, 13.303], \"ii_low_ci\": [59.642, 143.188], \"ii_high_median\": 0.584, \"ii_mid_median\": 4.522, \"ii_low_median\": 30.903, \"ii_high_winsorized\": 0.802, \"ii_mid_winsorized\": 8.156, \"ii_low_winsorized\": 94.931, \"kv_ppl_high\": 1.3108, \"kv_ppl_mid\": 6.1778, \"kv_ppl_low\": 23.8919, \"both_ppl_high\": 3.4623, \"both_ppl_mid\": 16.4148, \"both_ppl_low\": 104.1749, \"problems\": 50, \"segments\": 1356}, \"conclusion\": \"negative\", \"completed_at\": \"2026-05-14T02:15:34.177Z\"}, \"mvp_v5_fixed_s015\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T01:31:09.055Z\", \"updated_at\": \"2026-05-14T02:15:33.221Z\", \"spec\": {\"hypothesis\": \"v5修复验证: NaN skip + position normalization后, importance masking sparsity=0.15的II应为负(sub-additive)\", \"server\": \"westd-22162\", \"gpu\": \"cuda:2\", \"command\": \"python run_profiling.py --model /root/autodl-tmp/models/DeepSeek-R1-Distill-Qwen-7B --sparsity 0.15 --output_dir profiling_output_v5_s015 --max_problems 50\", \"data_path\": \"MATH-500 (embedded)\", \"data_count\": 50, \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B\", \"seed\": 42, \"pid\": 48262, \"checkpoint_path\": \"/root/autodl-tmp/pacs/profiling_output_v5_s015/\", \"log_path\": \"/root/autodl-tmp/pacs/profiling_output_v5_s015/\"}, \"metrics\": {\"ii_high\": 0.306, \"ii_mid\": 1.274, \"ii_low\": 8.786, \"ii_high_ci\": [0.256, 0.359], \"ii_mid_ci\": [0.895, 1.749], \"ii_low_ci\": [5.294, 12.684], \"ii_high_median\": 0.205, \"ii_mid_median\": 0.696, \"ii_low_median\": 2.627, \"ii_high_winsorized\": 0.289, \"ii_mid_winsorized\": 1.139, \"ii_low_winsorized\": 8.408, \"kv_ppl_high\": 1.2147, \"kv_ppl_mid\": 2.1276, \"kv_ppl_low\": 6.7451, \"both_ppl_high\": 2.2835, \"both_ppl_mid\": 3.9408, \"both_ppl_low\": 16.9987, \"problems\": 50, \"segments\": 1356}, \"conclusion\": \"negative\", \"completed_at\": \"2026-05-14T02:15:33.221Z\"}, \"mvp_v4_float32_s030\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T01:06:48.670Z\", \"updated_at\": \"2026-05-14T01:21:47.526Z\", \"hypothesis\": \"Float32 修复验证：importance masking sparsity=0.3, cuda:3。验证 torch.where 修复后 NaN 是否消除 + II 真实值。最关键验证点——s=0.3 是唯一显示符号反转的 level。\", \"spec\": {\"server\": \"westd-22162\", \"gpu\": \"cuda:3\", \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B\", \"data_path\": \"/root/autodl-tmp/pacs/data/math500.json\", \"data_count\": 50, \"seed\": 42}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-14T01:21:37.252Z\"}, \"mvp_ii_profiling_v4d\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T22:56:47.723Z\", \"updated_at\": \"2026-05-14T01:21:23.011Z\", \"hypothesis\": \"M1v4 importance-based masking (cuda:3, 40% sparsity): 高 sparsity 参考点，验证 30% 以上 sub-additive 趋势是否延续。\", \"parent\": null, \"spec\": {\"server\": \"westd-22162\", \"gpu\": \"cuda:2\", \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B\", \"data_path\": \"/root/autodl-tmp/pacs/data/math500.json\", \"data_count\": 50, \"seed\": 42, \"command\": \"CUDA_VISIBLE_DEVICES=2 python -m pacs.profiling.run_profiling --model_path /root/autodl-tmp/pacs/checkpoints/DeepSeek-R1-Distill-Qwen-7B --data_path /root/autodl-tmp/pacs/data/math500.json --output_dir /root/autodl-tmp/pacs/profiling_output_v4_s040 --sparsity_levels 0.40\", \"pid\": \"38760\"}, \"account\": \"root\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-14T01:20:54.693Z\", \"notes\": \"5/50 后静默崩溃，疑似长序列 + output_attentions OOM。importance 指标也有 NaN 中毒 + 位置偏差问题。\"}, \"mvp_v4_legacy_s035\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T00:12:54.211Z\", \"updated_at\": \"2026-05-14T01:21:21.671Z\", \"hypothesis\": \"importance(hardcoded) sparsity=0.35, crossover characterization: 验证 0.3 以上 sub-additive 趋势是否延续。与 s03(0.3, II=-224.5) 对比确认高 sparsity 方向。\", \"spec\": {\"server\": \"westd-22162\", \"gpu\": \"cuda:1\", \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B\", \"data_path\": \"/root/autodl-tmp/pacs/data/math500.json\", \"data_count\": 50, \"seed\": 42, \"command\": \"CUDA_VISIBLE_DEVICES=1 python -m pacs.profiling.run_profiling --model_path /root/autodl-tmp/pacs/checkpoints/DeepSeek-R1-Distill-Qwen-7B --data_path /root/autodl-tmp/pacs/data/math500.json --output_dir /root/autodl-tmp/pacs/profiling_output_v4_s035 --sparsity_levels 0.35\", \"pid\": 38996}, \"server\": \"westd-22162\", \"account\": \"root\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-14T01:21:04.001Z\", \"notes\": \"Invalidated: importance 指标有 Layer 27 NaN 中毒 + causal attention 位置偏差，II 结果无统计意义。需用修复后代码重跑。\"}, \"mvp_v4_legacy_s025\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T00:12:53.157Z\", \"updated_at\": \"2026-05-14T01:21:20.407Z\", \"hypothesis\": \"importance(hardcoded) sparsity=0.25, crossover characterization: 填充 0.2→0.3 之间的 II 符号反转临界点。与 s02(0.2, II=+21.3) 和 s03(0.3, II=-224.5) 对比定位 crossover。\", \"spec\": {\"server\": \"westd-22162\", \"gpu\": \"cuda:0\", \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B\", \"data_path\": \"/root/autodl-tmp/pacs/data/math500.json\", \"data_count\": 50, \"seed\": 42, \"command\": \"CUDA_VISIBLE_DEVICES=0 python -m pacs.profiling.run_profiling --model_path /root/autodl-tmp/pacs/checkpoints/DeepSeek-R1-Distill-Qwen-7B --data_path /root/autodl-tmp/pacs/data/math500.json --output_dir /root/autodl-tmp/pacs/profiling_output_v4_s025 --sparsity_levels 0.25\", \"pid\": 38120}, \"server\": \"westd-22162\", \"account\": \"root\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-14T01:21:03.079Z\", \"notes\": \"Invalidated: importance 指标有 Layer 27 NaN 中毒 + causal attention 位置偏差，II 结果无统计意义。需用修复后代码重跑。\"}, \"mvp_v4_random_r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T23:22:56.521Z\", \"updated_at\": \"2026-05-14T01:02:21.376Z\", \"hypothesis\": \"v4 retry: random masking baseline, sparsity 0.1,0.15,0.2,0.25,0.3, cuda:3\", \"spec\": {\"command\": \"python -m pacs.profiling.run_profiling --model_path .../DeepSeek-R1-Distill-Qwen-7B --data_path .../math500.json --output_dir profiling_output_v4_random_r2 --sparsity_levels 0.1,0.15,0.2,0.25,0.3 --masking_method random\", \"server\": \"westd-22162\", \"data_path\": \"/root/autodl-tmp/pacs/data/math500.json\", \"data_count\": 50, \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B\", \"seed\": 42, \"gpu\": \"cuda:3\", \"pid\": \"32187\"}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/pacs/profiling_output_v4_random_r2/profiling_results.json\", \"log_path\": \"/tmp/mvp_v4_random_r2.log\", \"completed_at\": \"2026-05-14T01:02:21.376Z\"}, \"mvp_v4_legacy_s01\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T23:53:19.548Z\", \"updated_at\": \"2026-05-14T00:12:13.850Z\", \"hypothesis\": \"v4 legacy: importance-based masking (hardcoded), sparsity=0.1, cuda:0. 从 corrected-submit worker 启动，代码无 --masking_method CLI 但 hardcoded importance。max_new_tokens=2048, min_phase_length=10。\", \"spec\": {\"command\": \"python -m pacs.profiling.run_profiling --model_path /root/autodl-tmp/pacs/checkpoints/DeepSeek-R1-Distill-Qwen-7B --data_path /root/autodl-tmp/pacs/data/math500.json --output_dir /root/autodl-tmp/pacs/profiling_output_v4a --sparsity_levels 0.1 --masking_method importance(hardcoded)\", \"server\": \"westd-22162\", \"data_path\": \"/root/autodl-tmp/pacs/data/math500.json\", \"data_count\": 50, \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B\", \"seed\": 42, \"gpu\": \"cuda:0\", \"pid\": \"27689\"}, \"log_path\": \"/root/autodl-tmp/pacs/profiling_output_v4a.log\", \"checkpoint_path\": \"/root/autodl-tmp/pacs/profiling_output_v4a/profiling_results.json\", \"conclusion\": \"negative\", \"completed_at\": \"2026-05-14T00:09:32.772Z\", \"notes\": \"50/50 completed. Verdict: FAIL. II[high_sparsity,0.1]=-0.11 CI=[-0.81,+0.41], II[mid_sparsity,0.1]=-15.97 CI=[-47.99,+1.29], II[low_sparsity,0.1]=0.00. Sparsity too low — II values near zero or negative, no meaningful signal separation. Output: profiling_output_v4a/profiling_results.json\", \"metrics\": {\"II_high_0.1\": {\"mean\": -0.1097, \"ci_low\": -0.8066, \"ci_high\": 0.41}, \"II_mid_0.1\": {\"mean\": -15.966, \"ci_low\": -47.991, \"ci_high\": 1.288}, \"II_low_0.1\": {\"mean\": 0, \"ci_low\": 0, \"ci_high\": 0}, \"ppl_high_dense\": 1.1462, \"ppl_high_both\": 22.1302, \"ppl_mid_dense\": 1.1226, \"ppl_mid_both\": 47.5856, \"verdict\": \"FAIL\"}}, \"mvp_v4_legacy_s03\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T23:53:20.777Z\", \"updated_at\": \"2026-05-14T00:10:08.277Z\", \"hypothesis\": \"v4 legacy: importance-based masking (hardcoded), sparsity=0.3, cuda:2. 30% 是唯一有初步符号反转信号的 level。最关键。\", \"spec\": {\"command\": \"python -m pacs.profiling.run_profiling --model_path /root/autodl-tmp/pacs/checkpoints/DeepSeek-R1-Distill-Qwen-7B --data_path /root/autodl-tmp/pacs/data/math500.json --output_dir /root/autodl-tmp/pacs/profiling_output_v4c --sparsity_levels 0.3 --masking_method importance(hardcoded)\", \"server\": \"westd-22162\", \"data_path\": \"/root/autodl-tmp/pacs/data/math500.json\", \"data_count\": 50, \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B\", \"seed\": 42, \"gpu\": \"cuda:2\", \"pid\": \"28452\"}, \"log_path\": \"/root/autodl-tmp/pacs/profiling_output_v4c.log\", \"checkpoint_path\": \"/root/autodl-tmp/pacs/profiling_output_v4c/\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-14T00:09:32.363Z\", \"metrics\": {\"ii_high_0.3\": {\"mean\": -224.5, \"ci_crosses_zero\": true}, \"verdict\": \"FAIL_ci_crosses_zero\"}, \"notes\": \"50/50 completed. Importance masking @0.3: II[high]=-224.5 但 95% CI 跨零(不显著)。这是唯一出现负 II 的 level，但统计不显著。需与 random baseline 对比，以及等 s01(0.1) 结果确认趋势。\"}, \"mvp_v4_legacy_s02\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T23:53:20.036Z\", \"updated_at\": \"2026-05-14T00:10:07.730Z\", \"hypothesis\": \"v4 legacy: importance-based masking (hardcoded), sparsity=0.2, cuda:1. 从 corrected-submit worker 启动。\", \"spec\": {\"command\": \"python -m pacs.profiling.run_profiling --model_path /root/autodl-tmp/pacs/checkpoints/DeepSeek-R1-Distill-Qwen-7B --data_path /root/autodl-tmp/pacs/data/math500.json --output_dir /root/autodl-tmp/pacs/profiling_output_v4b --sparsity_levels 0.2 --masking_method importance(hardcoded)\", \"server\": \"westd-22162\", \"data_path\": \"/root/autodl-tmp/pacs/data/math500.json\", \"data_count\": 50, \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B\", \"seed\": 42, \"gpu\": \"cuda:1\", \"pid\": \"28083\"}, \"log_path\": \"/root/autodl-tmp/pacs/profiling_output_v4b.log\", \"checkpoint_path\": \"/root/autodl-tmp/pacs/profiling_output_v4b/\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-14T00:09:31.414Z\", \"notes\": \"50/50 completed. Importance masking @0.2: II 全正(super-additive)。high/mid phase CI non-overlapping with low。KV eviction 是 perplexity 退化主因(kv ppl 远高于 attn ppl)。注意：II 为正 ≠ 支持 pivot hypothesis（pivot 预期 importance → sub-additive/负 II），需与 random baseline 对比才能判断。\", \"metrics\": {\"ii_high_0.2\": {\"mean\": 21.2856, \"ci\": [0.0292, 63.163]}, \"ii_mid_0.2\": {\"mean\": 21.8743, \"ci\": [4.9863, 41.785]}, \"ii_low_0.2\": {\"mean\": 0, \"ci\": [0, 0]}, \"ppl_high\": {\"dense\": 1.15, \"attn\": 1.32, \"kv\": 104.42, \"both\": 63.41}, \"ppl_mid\": {\"dense\": 1.12, \"attn\": 1.29, \"kv\": 324.16, \"both\": 170.47}, \"ppl_low\": {\"dense\": 1.11, \"attn\": 1.3, \"kv\": 1.11, \"both\": 1.3}, \"problems_completed\": 50, \"phase_tokens\": {\"high\": 25862, \"mid\": 27996, \"low\": 32349}, \"mvp_verdict\": \"PASS\"}}, \"mvp_v4c_r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T23:22:56.138Z\", \"updated_at\": \"2026-05-13T23:52:54.261Z\", \"hypothesis\": \"v4 retry: importance-based masking, sparsity 0.15,0.25, cuda:2\", \"spec\": {\"command\": \"python -m pacs.profiling.run_profiling --model_path .../DeepSeek-R1-Distill-Qwen-7B --data_path .../math500.json --output_dir profiling_output_v4c_r2 --sparsity_levels 0.15,0.25 --masking_method importance\", \"server\": \"westd-22162\", \"data_path\": \"/root/autodl-tmp/pacs/data/math500.json\", \"data_count\": 50, \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B\", \"seed\": 42, \"gpu\": \"cuda:2\", \"pid\": \"31839\"}, \"reproduce\": {\"finished_at\": \"2026-05-13T23:42:12.191Z\"}, \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-13T23:42:12.833Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-13T23:42:14.346396+00:00\"}]}, \"notes\": \"失败原因: GPU OOM — compute_dense_forward_with_importance() 使用 output_attentions=True 同时物化28层attention矩阵(~4.5GB for 1700-token seq)，加模型权重(~14GB)超出单卡VRAM。进程在problem [4/50](algebra/841.json)处被静默kill，无traceback。Random方法不调用此函数故正常。 | error_type: code | 修复建议: 逐层提取attention importance而非一次性物化全部层，或使用gradient-checkpointing式分层计算\"}, \"mvp_v4b_r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T23:22:55.162Z\", \"updated_at\": \"2026-05-13T23:52:53.632Z\", \"hypothesis\": \"v4 retry: importance-based masking, sparsity 0.3,0.4,0.5, cuda:1\", \"spec\": {\"command\": \"python -m pacs.profiling.run_profiling --model_path .../DeepSeek-R1-Distill-Qwen-7B --data_path .../math500.json --output_dir profiling_output_v4b_r2 --sparsity_levels 0.3,0.4,0.5 --masking_method importance\", \"server\": \"westd-22162\", \"data_path\": \"/root/autodl-tmp/pacs/data/math500.json\", \"data_count\": 50, \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B\", \"seed\": 42, \"gpu\": \"cuda:1\", \"pid\": \"31481\"}, \"reproduce\": {\"finished_at\": \"2026-05-13T23:42:07.204Z\"}, \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-13T23:42:07.966Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-13T23:42:09.409561+00:00\"}]}, \"notes\": \"失败原因: GPU OOM — compute_dense_forward_with_importance() 使用 output_attentions=True 同时物化28层attention矩阵(~4.5GB for 1700-token seq)，加模型权重(~14GB)超出单卡VRAM。进程在problem [3/50](intermediate_algebra/134.json)处被静默kill，无traceback。Random方法不调用此函数故正常。 | error_type: code | 修复建议: 逐层提取attention importance而非一次性物化全部层，或使用gradient-checkpointing式分层计算\"}, \"mvp_v4a_r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T23:22:54.240Z\", \"updated_at\": \"2026-05-13T23:52:52.705Z\", \"hypothesis\": \"v4 retry: importance-based masking, sparsity 0.1,0.2, cuda:0\", \"spec\": {\"command\": \"python -m pacs.profiling.run_profiling --model_path .../DeepSeek-R1-Distill-Qwen-7B --data_path .../math500.json --output_dir profiling_output_v4a_r2 --sparsity_levels 0.1,0.2 --masking_method importance\", \"server\": \"westd-22162\", \"data_path\": \"/root/autodl-tmp/pacs/data/math500.json\", \"data_count\": 50, \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B\", \"seed\": 42, \"gpu\": \"cuda:0\", \"pid\": \"31119\"}, \"reproduce\": {\"finished_at\": \"2026-05-13T23:42:04.420Z\"}, \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-13T23:42:04.603Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-13T23:42:05.417765+00:00\"}]}, \"notes\": \"失败原因: GPU OOM — compute_dense_forward_with_importance() 使用 output_attentions=True 同时物化28层attention矩阵(~4.5GB for 1700-token seq)，加模型权重(~14GB)超出单卡VRAM。进程在problem [3/50](intermediate_algebra/134.json)处被静默kill，无traceback。Random方法不调用此函数故正常。 | error_type: code | 修复建议: 逐层提取attention importance而非一次性物化全部层，或使用gradient-checkpointing式分层计算\"}, \"mvp_ii_profiling_v4-random\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T23:18:41.495Z\", \"updated_at\": \"2026-05-13T23:21:46.080Z\", \"hypothesis\": \"M1v4 random masking baseline (cuda:3, sparsity 0.1,0.15,0.2,0.25,0.3): 同 pipeline 同 50 题，masking_method=random。与 importance runs 直接对比验证 masking 策略对 II 的影响。\", \"parent\": \"mvp_ii_profiling_v3\", \"server\": \"westd-22162\", \"gpu\": \"cuda:3\", \"account\": \"root\", \"reproduce\": {\"server\": \"westd-22162\", \"gpu\": \"cuda:3\", \"started_at\": \"2026-05-13T23:19:36.995Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp && python -m pacs.profiling.run_profiling --model_path /root/autodl-tmp/pacs/checkpoints/DeepSeek-R1-Distill-Qwen-7B --data_path /root/autodl-tmp/pacs/data/math500.json --output_dir /root/autodl-tmp/pacs/profiling_output_v4_random --max_new_tokens 2048 --min_phase_length 10 --sparsity_levels 0.1,0.15,0.2,0.25,0.3 --masking_method random\\\"\", \"finished_at\": \"2026-05-13T23:20:05.361Z\", \"training_hours\": 0.01}, \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp && python -m pacs.profiling.run_profiling --model_path /root/autodl-tmp/pacs/checkpoints/DeepSeek-R1-Distill-Qwen-7B --data_path /root/autodl-tmp/pacs/data/math500.json --output_dir /root/autodl-tmp/pacs/profiling_output_v4_random --max_new_tokens 2048 --min_phase_length 10 --sparsity_levels 0.1,0.15,0.2,0.25,0.3 --masking_method random\\\"\", \"server\": \"westd-22162\", \"gpu\": [\"cuda:3\"], \"pid\": \"27401\", \"log_path\": \"~/runs/phase-gated-compound-sparse/mvp_ii_profiling_v4-random.log\", \"submitted_at\": \"2026-05-13T23:19:40.234Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 26.5, \"gpu_hours\": 0.01}, \"pid\": \"27401\", \"log_path\": \"~/runs/phase-gated-compound-sparse/mvp_ii_profiling_v4-random.log\", \"failure_reason\": \"EXIT_CODE=2 (shell misuse / syntax)\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-13T23:20:06.693Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-13T23:20:08.229965+00:00\"}]}, \"notes\": \"失败原因: run_profiling.py 未定义 --masking_method 参数，argparse 报 unrecognized arguments: --masking_method random | error_type: infrastructure | 同 mvp_ii_profiling_v4\"}, \"mvp_ii_profiling_v4c\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T22:54:54.251Z\", \"updated_at\": \"2026-05-13T23:21:44.920Z\", \"hypothesis\": \"M1v4 importance-based masking (cuda:2, sparsity 0.15,0.25): 填充 sparsity 梯度，定位 sign flip 临界点。\", \"parent\": \"mvp_ii_profiling_v3\", \"server\": \"westd-22162\", \"gpu\": \"cuda:2\", \"account\": \"root\", \"reproduce\": {\"server\": \"westd-22162\", \"gpu\": \"cuda:2\", \"started_at\": \"2026-05-13T23:19:32.847Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp && python -m pacs.profiling.run_profiling --model_path /root/autodl-tmp/pacs/checkpoints/DeepSeek-R1-Distill-Qwen-7B --data_path /root/autodl-tmp/pacs/data/math500.json --output_dir /root/autodl-tmp/pacs/profiling_output_v4c --max_new_tokens 2048 --min_phase_length 10 --sparsity_levels 0.15,0.25 --masking_method importance\\\"\", \"finished_at\": \"2026-05-13T23:20:00.630Z\", \"training_hours\": 0.01}, \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp && python -m pacs.profiling.run_profiling --model_path /root/autodl-tmp/pacs/checkpoints/DeepSeek-R1-Distill-Qwen-7B --data_path /root/autodl-tmp/pacs/data/math500.json --output_dir /root/autodl-tmp/pacs/profiling_output_v4c --max_new_tokens 2048 --min_phase_length 10 --sparsity_levels 0.15,0.25 --masking_method importance\\\"\", \"server\": \"westd-22162\", \"gpu\": [\"cuda:2\"], \"pid\": \"27251\", \"log_path\": \"~/runs/phase-gated-compound-sparse/mvp_ii_profiling_v4c.log\", \"submitted_at\": \"2026-05-13T23:19:36.055Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 25.8, \"gpu_hours\": 0.01}, \"pid\": \"27251\", \"log_path\": \"~/runs/phase-gated-compound-sparse/mvp_ii_profiling_v4c.log\", \"failure_reason\": \"EXIT_CODE=2 (shell misuse / syntax)\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-13T23:20:01.892Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-13T23:20:03.414314+00:00\"}]}, \"notes\": \"失败原因: run_profiling.py 未定义 --masking_method 参数，argparse 报 unrecognized arguments | error_type: infrastructure | 同 mvp_ii_profiling_v4\"}, \"mvp_ii_profiling_v4b\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T22:54:53.810Z\", \"updated_at\": \"2026-05-13T23:21:43.971Z\", \"hypothesis\": \"M1v4 importance-based masking (cuda:1, sparsity 0.3,0.4,0.5): 30% 是唯一有初步符号反转信号的 level。高 sparsity regime。\", \"parent\": \"mvp_ii_profiling_v3\", \"server\": \"westd-22162\", \"gpu\": \"cuda:1\", \"account\": \"root\", \"reproduce\": {\"server\": \"westd-22162\", \"gpu\": \"cuda:1\", \"started_at\": \"2026-05-13T23:19:28.695Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp && python -m pacs.profiling.run_profiling --model_path /root/autodl-tmp/pacs/checkpoints/DeepSeek-R1-Distill-Qwen-7B --data_path /root/autodl-tmp/pacs/data/math500.json --output_dir /root/autodl-tmp/pacs/profiling_output_v4b --max_new_tokens 2048 --min_phase_length 10 --sparsity_levels 0.3,0.4,0.5 --masking_method importance\\\"\", \"finished_at\": \"2026-05-13T23:19:55.006Z\", \"training_hours\": 0.01}, \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp && python -m pacs.profiling.run_profiling --model_path /root/autodl-tmp/pacs/checkpoints/DeepSeek-R1-Distill-Qwen-7B --data_path /root/autodl-tmp/pacs/data/math500.json --output_dir /root/autodl-tmp/pacs/profiling_output_v4b --max_new_tokens 2048 --min_phase_length 10 --sparsity_levels 0.3,0.4,0.5 --masking_method importance\\\"\", \"server\": \"westd-22162\", \"gpu\": [\"cuda:1\"], \"pid\": \"27099\", \"log_path\": \"~/runs/phase-gated-compound-sparse/mvp_ii_profiling_v4b.log\", \"submitted_at\": \"2026-05-13T23:19:31.930Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 24.2, \"gpu_hours\": 0.01}, \"pid\": \"27099\", \"log_path\": \"~/runs/phase-gated-compound-sparse/mvp_ii_profiling_v4b.log\", \"failure_reason\": \"EXIT_CODE=2 (shell misuse / syntax)\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-13T23:19:56.100Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-13T23:19:57.514401+00:00\"}]}, \"notes\": \"失败原因: run_profiling.py 未定义 --masking_method 参数，argparse 报 unrecognized arguments | error_type: infrastructure | 同 mvp_ii_profiling_v4\"}, \"mvp_ii_profiling_v4\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T22:50:59.554Z\", \"updated_at\": \"2026-05-13T23:21:42.200Z\", \"hypothesis\": \"M1v4 importance-based masking (cuda:0, sparsity 0.1,0.2): head=Frobenius norm, KV=cumulative attention. 低 sparsity regime。\", \"parent\": \"mvp_ii_profiling_v3\", \"server\": \"westd-22162\", \"gpu\": \"cuda:0\", \"account\": \"root\", \"reproduce\": {\"server\": \"westd-22162\", \"gpu\": \"cuda:0\", \"started_at\": \"2026-05-13T23:19:23.840Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp && python -m pacs.profiling.run_profiling --model_path /root/autodl-tmp/pacs/checkpoints/DeepSeek-R1-Distill-Qwen-7B --data_path /root/autodl-tmp/pacs/data/math500.json --output_dir /root/autodl-tmp/pacs/profiling_output_v4a --max_new_tokens 2048 --min_phase_length 10 --sparsity_levels 0.1,0.2 --masking_method importance\\\"\", \"finished_at\": \"2026-05-13T23:19:52.039Z\", \"training_hours\": 0.01}, \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp && python -m pacs.profiling.run_profiling --model_path /root/autodl-tmp/pacs/checkpoints/DeepSeek-R1-Distill-Qwen-7B --data_path /root/autodl-tmp/pacs/data/math500.json --output_dir /root/autodl-tmp/pacs/profiling_output_v4a --max_new_tokens 2048 --min_phase_length 10 --sparsity_levels 0.1,0.2 --masking_method importance\\\"\", \"server\": \"westd-22162\", \"gpu\": [\"cuda:0\"], \"pid\": \"26947\", \"log_path\": \"~/runs/phase-gated-compound-sparse/mvp_ii_profiling_v4.log\", \"submitted_at\": \"2026-05-13T23:19:27.810Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 24.9, \"gpu_hours\": 0.01}, \"pid\": \"26947\", \"log_path\": \"~/runs/phase-gated-compound-sparse/mvp_ii_profiling_v4.log\", \"failure_reason\": \"EXIT_CODE=2 (shell misuse / syntax)\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-13T23:19:52.672Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-13T23:19:53.495907+00:00\"}]}, \"notes\": \"失败原因: run_profiling.py 未定义 --masking_method 参数，argparse 报 unrecognized arguments | error_type: infrastructure | 建议: 给 run_profiling.py 添加 --masking_method 参数后重跑\"}, \"mvp_ii_profiling_v3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T21:28:01.393Z\", \"updated_at\": \"2026-05-13T22:42:34.790Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp && python -m pacs.profiling.run_profiling --model_path /root/autodl-tmp/pacs/checkpoints/DeepSeek-R1-Distill-Qwen-7B --data_path /root/autodl-tmp/pacs/data/math500.json --output_dir /root/autodl-tmp/pacs/profiling_output_v3 --max_new_tokens 2048 --min_phase_length 10\\\"\", \"server\": \"westd-22162\", \"gpu\": [\"cuda:0\"], \"pid\": \"16717\", \"log_path\": \"~/runs/phase-gated-compound-sparse/mvp_ii_profiling_v3.log\", \"submitted_at\": \"2026-05-13T21:47:43.523Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 3290.7, \"gpu_hours\": 0.91}, \"hypothesis\": \"M1v3诊断: 降低sparsity至10%/20%(v2的30%/50%导致Inf退化) + quantile segmentation替代KDE(v2 90%样本fallback) + NaN guard。测试compound sparsity交互强度是否在sparsity regime间有显著差异。\", \"parent\": \"mvp_ii_profiling_v2\", \"server\": \"westd-22162\", \"gpu\": \"cuda:0\", \"account\": \"root\", \"reproduce\": {\"server\": \"westd-22162\", \"gpu\": \"cuda:0\", \"started_at\": \"2026-05-13T21:47:42.052Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp && python -m pacs.profiling.run_profiling --model_path /root/autodl-tmp/pacs/checkpoints/DeepSeek-R1-Distill-Qwen-7B --data_path /root/autodl-tmp/pacs/data/math500.json --output_dir /root/autodl-tmp/pacs/profiling_output_v3 --max_new_tokens 2048 --min_phase_length 10\\\"\", \"finished_at\": \"2026-05-13T22:38:48.794Z\", \"training_hours\": 0.85}, \"pid\": \"16717\", \"log_path\": \"~/runs/phase-gated-compound-sparse/mvp_ii_profiling_v3.log\", \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-13T22:38:49.527620+00:00\"}]}, \"conclusion\": \"negative\", \"metrics\": {\"mvp_verdict\": \"FAIL\", \"ci_nonoverlap\": false, \"sign_reversal\": false, \"phase_distribution_balanced\": true, \"ii_high_0.1\": {\"mean\": 0.2317, \"ci\": [0.1338, 0.3418]}, \"ii_low_0.1\": {\"mean\": 0.1711, \"ci\": [0.0782, 0.2768]}, \"ii_mid_0.1\": {\"mean\": 0.1607, \"ci\": [0.0886, 0.2489]}, \"ii_high_0.2\": {\"mean\": 2.1574, \"ci\": [1.0605, 3.5491]}, \"ii_low_0.2\": {\"mean\": 1.1294, \"ci\": [0.4368, 1.9593]}, \"ii_mid_0.2\": {\"mean\": 0.3049, \"ci\": [-1.0635, 1.3044]}, \"total_tokens\": 86207, \"no_nan_inf\": true, \"segments\": {\"high\": 511, \"low\": 454, \"mid\": 391}}, \"checkpoint_path\": \"/root/autodl-tmp/pacs/profiling_output_v3\", \"completed_at\": \"2026-05-13T22:42:34.177Z\"}, \"mvp_ii_profiling_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T20:41:50.875Z\", \"updated_at\": \"2026-05-13T22:42:24.179Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp && python -m pacs.profiling.run_profiling --model_path /root/autodl-tmp/pacs/checkpoints/DeepSeek-R1-Distill-Qwen-7B --data_path /root/autodl-tmp/pacs/data/math500.json --output_dir /root/autodl-tmp/pacs/profiling_output_v2 --max_new_tokens 2048 --kde_bandwidth scott --min_phase_length 10\\\"\", \"server\": \"westd-22162\", \"gpu\": [\"cuda:0\"], \"pid\": \"11977\", \"log_path\": \"~/runs/phase-gated-compound-sparse/mvp_ii_profiling_v2.log\", \"submitted_at\": \"2026-05-13T20:42:13.499Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 7090.7, \"gpu_hours\": 1.97}, \"hypothesis\": \"P0修复后重跑: Phase-dependent interaction direction reversal — compound sparsity exhibits qualitatively different interaction patterns across reasoning phases. KV eviction mask已修复为1D共享(原P0 bug导致指数级token丢失). 同时启用P1诊断dump验证phase segmentation.\", \"parent\": \"mvp_interaction_index_profiling\", \"server\": \"westd-22162\", \"gpu\": \"cuda:0\", \"account\": \"root\", \"reproduce\": {\"server\": \"westd-22162\", \"gpu\": \"cuda:0\", \"started_at\": \"2026-05-13T20:42:12.028Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp && python -m pacs.profiling.run_profiling --model_path /root/autodl-tmp/pacs/checkpoints/DeepSeek-R1-Distill-Qwen-7B --data_path /root/autodl-tmp/pacs/data/math500.json --output_dir /root/autodl-tmp/pacs/profiling_output_v2 --max_new_tokens 2048 --kde_bandwidth scott --min_phase_length 10\\\"\", \"finished_at\": \"2026-05-13T21:14:37.912Z\", \"training_hours\": 0.54}, \"pid\": \"11977\", \"log_path\": \"~/runs/phase-gated-compound-sparse/mvp_ii_profiling_v2.log\", \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-13T21:14:38.613199+00:00\"}]}, \"conclusion\": \"negative\", \"metrics\": {\"mvp_verdict\": \"PASS_technical_but_negative_hypothesis\", \"ci_nonoverlap\": true, \"sign_reversal\": false, \"ii_reasoning_0.3\": 17.79, \"ii_reasoning_0.3_ci\": [4.09, 38.76], \"ii_transition_0.3\": 3.06, \"ii_transition_0.3_ci\": [0.01, 5.6], \"ii_reasoning_0.5\": 468.9, \"ii_transition_0.5\": 850.07, \"ii_execution_0.3\": \"Inf\", \"phase_distribution\": {\"execution\": \"1.2%_25seg\", \"reasoning\": \"8.1%_96seg\", \"transition\": \"90.7%_192seg\"}, \"total_tokens\": 86207, \"all_ii_superadditive\": true, \"amplitude_ratio_reas_vs_trans_0.3\": 5.81, \"gmm_best_k\": 5, \"gmm_means\": [0.438, 0.597, 0.719, 0.816, 0.892], \"gmm_weights\": [0.062, 0.14, 0.208, 0.282, 0.309], \"sparsity_global\": {\"mean\": 0.7653, \"std\": 0.1364, \"median\": 0.8004}, \"quantile_boundaries\": [0.7337, 0.8482]}, \"checkpoint_path\": \"/root/autodl-tmp/pacs/profiling_output_v2\", \"completed_at\": \"2026-05-13T22:40:24.197Z\"}, \"mvp_interaction_index_profiling\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T19:19:05.209Z\", \"updated_at\": \"2026-05-13T20:41:42.206Z\", \"hypothesis\": \"Phase-dependent interaction direction reversal: compound sparsity (attention head pruning + KV cache eviction) exhibits qualitatively different interaction patterns (super- vs sub-additive) across reasoning phases (execution/reasoning/transition), as measured by Interaction Index on DeepSeek-R1-Distill-Qwen-7B MATH-500 traces.\", \"server\": \"westd-22162\", \"gpu\": \"cuda:0\", \"account\": \"root\", \"reproduce\": {\"server\": \"westd-22162\", \"gpu\": \"cuda:0\", \"started_at\": \"2026-05-13T19:22:39.684Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp && python -m pacs.profiling.run_profiling --model_path /root/autodl-tmp/pacs/checkpoints/DeepSeek-R1-Distill-Qwen-7B --data_path /root/autodl-tmp/pacs/data/math500.json --output_dir /root/autodl-tmp/pacs/profiling_output --max_new_tokens 2048 --kde_bandwidth scott --min_phase_length 10\\\"\", \"finished_at\": \"2026-05-13T19:55:17.924Z\", \"training_hours\": 0.54}, \"spec\": {\"command\": \"python -m pacs.profiling.run_profiling --model_path /root/autodl-tmp/pacs/checkpoints/DeepSeek-R1-Distill-Qwen-7B --data_path /root/autodl-tmp/pacs/data/math500.json --output_dir /root/autodl-tmp/pacs/profiling_output --max_new_tokens 2048 --kde_bandwidth scott --min_phase_length 10\", \"server\": \"westd-22162\", \"data_path\": \"/root/autodl-tmp/pacs/data/math500.json\", \"data_count\": 50, \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B\", \"seed\": 42, \"gpu\": \"cuda:0\", \"pid\": \"7436\", \"log_path\": \"~/runs/phase-gated-compound-sparse/mvp_interaction_index_profiling.log\", \"model_config\": {\"hidden_size\": 3584, \"num_hidden_layers\": 28, \"num_attention_heads\": 28, \"num_key_value_heads\": 4}, \"sparsity_levels\": [0.3, 0.5], \"n_bootstrap\": 1000, \"max_new_tokens\": 2048, \"sampling\": \"stratified 5x10=50, seed=42\"}, \"pid\": \"7436\", \"log_path\": \"~/runs/phase-gated-compound-sparse/mvp_interaction_index_profiling.log\", \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-13T19:55:18.584043+00:00\"}]}, \"conclusion\": \"failed\", \"completed_at\": \"2026-05-13T20:41:42.206Z\"}}, \"count\": 116, \"total\": 116, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.6506}}"
    }
  },
  "sourceToolAssistantUUID": "809e4f6a-ef7f-4382-94e5-13f10a34c64e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "sessionId": "38576691-e177-4a18-ab23-be69eff4b7ff",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-16T00:25:48.186Z_

<details><summary>↩ Tool result · `toolu_017Neur95H2nm1TjLddGoxZz`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/memory.md\", \"content\": \"# Project Memory\\n\\n## 2026-05-15: C10 GSM8K — random masking confirms compound interaction is intrinsic\\n- gsm8k_qw_rand_s025_v2 (PASS) + gsm8k_qw_rand_s030_v2 (PASS): random masking 在 s=0.25 和 s=0.30 均产生显著 compound interaction\\n- II dose-response: s=0.30 > s=0.25（所有 phase），median CI lower bound 均 > 0\\n- 关键论文 claim: compound interaction 是 sparsity 的固有属性，不依赖 masking strategy（importance vs random）\\n- 对比 spark-aaai2026: 他们只报告 importance-based compound 是 super-additive，我们证明 random 也如此 → 更强 generalization\\n\\n## 2026-05-15: DS 8k truncation — 即使 8192 tokens 仍不够\\n- acc_ds_s020_8k_v2: truncation 从 4k 版 64% 仅降至 8k 版 58%（目标 <20% 远未达到）\\n- DS 在 sparsity 下生成极长输出，8k tokens 仍不足 → accuracy 数据为下界\\n- 论文处理：DS accuracy 标注为 \\\"lower bound under token budget constraint\\\"，呼应 D086（降为定性观察）\\n\\n## 2026-05-15: QW n=100 accuracy dose curve — v2 fix 影响极小\\n- acc_qw_s020_n100_b2_fix 完成：v2 rescore 未改变 s020 batch1（均为 13/50=0.26），8k batch2 仅 +1 correct（22→23）\\n- 当前 dose curve: dense=0.40, s015=0.36, s020=0.36(v2✓), s025=0.33(fix running), s030=0.19\\n- **s015=s020 平台期**：低 sparsity 区间（≤20%）accuracy 损失几乎相同（-4pp），断崖在 s025→s030（-14pp）\\n- ⚠️ s015/s030/dense 的 batch1 尚未走 v2 rescore；s020 的 v2 与 pre-v2 相同，但不能假设其他条件也如此\\n- 推翻早期结论\\\"QW s015 完全无损(0pp)\\\"——n=100 显示 -4pp（早期结论可能基于更小样本）\\n\\n## 2026-05-15: Qwen n=475 reanalysis complete\\n- Reviewer flagged Qwen using n=274 (complete-case requiring all 3 phases). Corrected to n=475 (low+high valid only).\\n- Created `analyze_n500_v2.py` on server. Outputs: `n500_unified_final.{csv,json}`, `n500_full_statistics.md`\\n- v2 adds: cross-model Mann-Whitney U, imp/rand effect size ratio, proper paired filtering via `extract_diffs_paired`\\n- Bonferroni correction across 48 tests total (16 conditions + 8 within-imp d_z + 8 rand-within + 8 imp-vs-rand + 8 cross-model)\\n- DS rand s025/s030 Bonferroni p ≈ 0.07 (no longer significant after correction)\\n- All Qwen imp conditions remain *** significant with n=475\\n\\n## 2026-05-15: sf5 asymmetric sparsity — structural insight\\n- 非对称 sparsity 分配下 phase gradient 方向完全稳健（D > 0 both configs）\\n- KV sparsity 较高时 mid-phase II 更大（6.05 vs 3.97）→ KV 维度对中间 phase 影响更强\\n- Head sparsity 较高时 high-phase II 略升（0.52 vs 0.38）→ head 维度主要影响高 sparsity phase\\n- 启示：如果做 adaptive controller，KV budget 对 mid-phase 更敏感，head budget 对 high-phase 更敏感\\n\\n## 2026-05-15: Appendix B G× 修正\\n- 论文旧值 58-241×，精确计算后为 21-64×（per-problem additive II + aggregate PPL 修正）\\n- 计算脚本：`/root/autodl-tmp/pacs/compute_gx_final.py`\\n- 所有论文中引用 G× 的段落需同步更新\\n\\n## 2026-05-15: C2 Accuracy Eval — DS truncation caveat\\n- DS dense baseline 受 2048 token 限制，56% 截断率，真实 accuracy 可能远高于 52%\\n- DS 失败模式 = truncation-dominated（CoT 太长）；QW 失败模式 = wrong-answer-dominated\\n- DS s030 触发 40% 中文推理（语言切换），s015 仅 4%，dense 为 0% — 高 sparsity 的病理信号\\n- 论文需声明 token budget 限制，或考虑扩展 max_new_tokens 重跑（但 GPU 时间代价大）\\n\\n## 2026-05-15: GSM8K median fix (D080v3)\\n- mean→median 修复关键：DS s030 从 mean=0.607(p=0.42) 恢复为 median=4.68(p<0.0001)\\n- 方法论必须与 MATH-500 一致：median + Wilcoxon + bootstrap(median)\\n\", \"total_chars\": 2929, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4ee8b54d-2687-4051-9c8f-89a051abec43",
  "isSidechain": false,
  "promptId": "5d98afa4-bc8d-47c1-b014-8bbe0580361f",
  "type": "user",
  "uuid": "1127de5b-3f3e-42e0-9605-d38048768657",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"path\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/memory.md\\\", \\\"content\\\": \\\"# Project Memory\\\\n\\\\n## 2026-05-15: C10 GSM8K — random masking confirms compound interaction is intrinsic\\\\n- gsm8k_qw_rand_s025_v2 (PASS) + gsm8k_qw_rand_s030_v2 (PASS): random masking 在 s=0.25 和 s=0.30 均产生显著 compound interaction\\\\n- II dose-response: s=0.30 > s=0.25（所有 phase），median CI lower bound 均 > 0\\\\n- 关键论文 claim: compound interaction 是 sparsity 的固有属性，不依赖 masking strategy（importance vs random）\\\\n- 对比 spark-aaai2026: 他们只报告 importance-based compound 是 super-additive，我们证明 random 也如此 → 更强 generalization\\\\n\\\\n## 2026-05-15: DS 8k truncation — 即使 8192 tokens 仍不够\\\\n- acc_ds_s020_8k_v2: truncation 从 4k 版 64% 仅降至 8k 版 58%（目标 <20% 远未达到）\\\\n- DS 在 sparsity 下生成极长输出，8k tokens 仍不足 → accuracy 数据为下界\\\\n- 论文处理：DS accuracy 标注为 \\\\\\\"lower bound under token budget constraint\\\\\\\"，呼应 D086（降为定性观察）\\\\n\\\\n## 2026-05-15: QW n=100 accuracy dose curve — v2 fix 影响极小\\\\n- acc_qw_s020_n100_b2_fix 完成：v2 rescore 未改变 s020 batch1（均为 13/50=0.26），8k batch2 仅 +1 correct（22→23）\\\\n- 当前 dose curve: dense=0.40, s015=0.36, s020=0.36(v2✓), s025=0.33(fix running), s030=0.19\\\\n- **s015=s020 平台期**：低 sparsity 区间（≤20%）accuracy 损失几乎相同（-4pp），断崖在 s025→s030（-14pp）\\\\n- ⚠️ s015/s030/dense 的 batch1 尚未走 v2 rescore；s020 的 v2 与 pre-v2 相同，但不能假设其他条件也如此\\\\n- 推翻早期结论\\\\\\\"QW s015 完全无损(0pp)\\\\\\\"——n=100 显示 -4pp（早期结论可能基于更小样本）\\\\n\\\\n## 2026-05-15: Qwen n=475 reanalysis complete\\\\n- Reviewer flagged Qwen using n=274 (complete-case requiring all 3 phases). Corrected to n=475 (low+high valid only).\\\\n- Created `analyze_n500_v2.py` on server. Outputs: `n500_unified_final.{csv,json}`, `n500_full_statistics.md`\\\\n- v2 adds: cross-model Mann-Whitney U, imp/rand effect size ratio, proper paired filtering via `extract_diffs_paired`\\\\n- Bonferroni correction across 48 tests total (16 conditions + 8 within-imp d_z + 8 rand-within + 8 imp-vs-rand + 8 cross-model)\\\\n- DS rand s025/s030 Bonferroni p ≈ 0.07 (no longer significant after correction)\\\\n- All Qwen imp conditions remain *** significant with n=475\\\\n\\\\n## 2026-05-15: sf5 asymmetric sparsity — structural insight\\\\n- 非对称 sparsity 分配下 phase gradient 方向完全稳健（D > 0 both configs）\\\\n- KV sparsity 较高时 mid-phase II 更大（6.05 vs 3.97）→ KV 维度对中间 phase 影响更强\\\\n- Head sparsity 较高时 high-phase II 略升（0.52 vs 0.38）→ head 维度主要影响高 sparsity phase\\\\n- 启示：如果做 adaptive controller，KV budget 对 mid-phase 更敏感，head budget 对 high-phase 更敏感\\\\n\\\\n## 2026-05-15: Appendix B G× 修正\\\\n- 论文旧值 58-241×，精确计算后为 21-64×（per-problem additive II + aggregate PPL 修正）\\\\n- 计算脚本：`/root/autodl-tmp/pacs/compute_gx_final.py`\\\\n- 所有论文中引用 G× 的段落需同步更新\\\\n\\\\n## 2026-05-15: C2 Accuracy Eval — DS truncation caveat\\\\n- DS dense baseline 受 2048 token 限制，56% 截断率，真实 accuracy 可能远高于 52%\\\\n- DS 失败模式 = truncation-dominated（CoT 太长）；QW 失败模式 = wrong-answer-dominated\\\\n- DS s030 触发 40% 中文推理（语言切换），s015 仅 4%，dense 为 0% — 高 sparsity 的病理信号\\\\n- 论文需声明 token budget 限制，或考虑扩展 max_new_tokens 重跑（但 GPU 时间代价大）\\\\n\\\\n## 2026-05-15: GSM8K median fix (D080v3)\\\\n- mean→median 修复关键：DS s030 从 mean=0.607(p=0.42) 恢复为 median=4.68(p<0.0001)\\\\n- 方法论必须与 MATH-500 一致：median + Wilcoxon + bootstrap(median)\\\\n\\\", \\\"total_chars\\\": 2929, \\\"truncated\\\": false}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/memory.md\", \"content\": \"# Project Memory\\n\\n## 2026-05-15: C10 GSM8K — random masking confirms compound interaction is intrinsic\\n- gsm8k_qw_rand_s025_v2 (PASS) + gsm8k_qw_rand_s030_v2 (PASS): random masking 在 s=0.25 和 s=0.30 均产生显著 compound interaction\\n- II dose-response: s=0.30 > s=0.25（所有 phase），median CI lower bound 均 > 0\\n- 关键论文 claim: compound interaction 是 sparsity 的固有属性，不依赖 masking strategy（importance vs random）\\n- 对比 spark-aaai2026: 他们只报告 importance-based compound 是 super-additive，我们证明 random 也如此 → 更强 generalization\\n\\n## 2026-05-15: DS 8k truncation — 即使 8192 tokens 仍不够\\n- acc_ds_s020_8k_v2: truncation 从 4k 版 64% 仅降至 8k 版 58%（目标 <20% 远未达到）\\n- DS 在 sparsity 下生成极长输出，8k tokens 仍不足 → accuracy 数据为下界\\n- 论文处理：DS accuracy 标注为 \\\"lower bound under token budget constraint\\\"，呼应 D086（降为定性观察）\\n\\n## 2026-05-15: QW n=100 accuracy dose curve — v2 fix 影响极小\\n- acc_qw_s020_n100_b2_fix 完成：v2 rescore 未改变 s020 batch1（均为 13/50=0.26），8k batch2 仅 +1 correct（22→23）\\n- 当前 dose curve: dense=0.40, s015=0.36, s020=0.36(v2✓), s025=0.33(fix running), s030=0.19\\n- **s015=s020 平台期**：低 sparsity 区间（≤20%）accuracy 损失几乎相同（-4pp），断崖在 s025→s030（-14pp）\\n- ⚠️ s015/s030/dense 的 batch1 尚未走 v2 rescore；s020 的 v2 与 pre-v2 相同，但不能假设其他条件也如此\\n- 推翻早期结论\\\"QW s015 完全无损(0pp)\\\"——n=100 显示 -4pp（早期结论可能基于更小样本）\\n\\n## 2026-05-15: Qwen n=475 reanalysis complete\\n- Reviewer flagged Qwen using n=274 (complete-case requiring all 3 phases). Corrected to n=475 (low+high valid only).\\n- Created `analyze_n500_v2.py` on server. Outputs: `n500_unified_final.{csv,json}`, `n500_full_statistics.md`\\n- v2 adds: cross-model Mann-Whitney U, imp/rand effect size ratio, proper paired filtering via `extract_diffs_paired`\\n- Bonferroni correction across 48 tests total (16 conditions + 8 within-imp d_z + 8 rand-within + 8 imp-vs-rand + 8 cross-model)\\n- DS rand s025/s030 Bonferroni p ≈ 0.07 (no longer significant after correction)\\n- All Qwen imp conditions remain *** significant with n=475\\n\\n## 2026-05-15: sf5 asymmetric sparsity — structural insight\\n- 非对称 sparsity 分配下 phase gradient 方向完全稳健（D > 0 both configs）\\n- KV sparsity 较高时 mid-phase II 更大（6.05 vs 3.97）→ KV 维度对中间 phase 影响更强\\n- Head sparsity 较高时 high-phase II 略升（0.52 vs 0.38）→ head 维度主要影响高 sparsity phase\\n- 启示：如果做 adaptive controller，KV budget 对 mid-phase 更敏感，head budget 对 high-phase 更敏感\\n\\n## 2026-05-15: Appendix B G× 修正\\n- 论文旧值 58-241×，精确计算后为 21-64×（per-problem additive II + aggregate PPL 修正）\\n- 计算脚本：`/root/autodl-tmp/pacs/compute_gx_final.py`\\n- 所有论文中引用 G× 的段落需同步更新\\n\\n## 2026-05-15: C2 Accuracy Eval — DS truncation caveat\\n- DS dense baseline 受 2048 token 限制，56% 截断率，真实 accuracy 可能远高于 52%\\n- DS 失败模式 = truncation-dominated（CoT 太长）；QW 失败模式 = wrong-answer-dominated\\n- DS s030 触发 40% 中文推理（语言切换），s015 仅 4%，dense 为 0% — 高 sparsity 的病理信号\\n- 论文需声明 token budget 限制，或考虑扩展 max_new_tokens 重跑（但 GPU 时间代价大）\\n\\n## 2026-05-15: GSM8K median fix (D080v3)\\n- mean→median 修复关键：DS s030 从 mean=0.607(p=0.42) 恢复为 median=4.68(p<0.0001)\\n- 方法论必须与 MATH-500 一致：median + Wilcoxon + bootstrap(median)\\n\", \"total_chars\": 2929, \"truncated\": false}, \"error\": null, \"metadata\": {}}"
    }
  },
  "sourceToolAssistantUUID": "4ee8b54d-2687-4051-9c8f-89a051abec43",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "sessionId": "38576691-e177-4a18-ab23-be69eff4b7ff",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-16T00:25:48.481Z_

<details><summary>↩ Tool result · `toolu_014R91JS7TNMdPZVWwbw6EsS`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/paper_framing.md\", \"content\": \"# Paper Framing — Phase-Gated Compound Sparsity\\n\\n> 最后更新: 2026-05-15 (D080v3 GSM8K median-based 数据更新: DS 0.241→4.682, QW 0.039→2.092, imp/rand ratio 2.3-3.8×) | 维护者: Director\\n\\n## Core Insight\\n\\nCompound sparsity（attention head pruning + KV cache eviction）的 severity 不是固定常数——它是 eviction strategy 和 reasoning phase 交互的涌现属性。Importance-based eviction 的 compound interaction severity（paired median difference: median(II_low_i − II_high_i)）随 sparsity 单调递增（DeepSeek: 0.32→1.15→3.97→9.94; Qwen: 0.048→0.208→1.109→2.619），而 random masking 在 s015/s020 NS，在 s025 跨模型显著但效应量远小于 importance（DS: 0.257 vs 3.986; QW: 0.393 vs 1.074, 3-15×差异），存在 sparsity threshold ~s020-s025（D063; s030 待定）。Cohen's d（paired d_z, B=10000）从 small-medium 到 large（DeepSeek: 0.44→0.80; Qwen: 0.28→1.02，s015 边缘）。LLaMA 跨架构验证（D060）qualitative direction consistent（within-importance d_z~1.0），但 strategy×phase 交互弱于 Qwen2 架构（imp_vs_rand d_z 0.19→0.34, 仅 s030 显著），且 random 在 LLaMA 上也显示显著 phase gradient（d_z 0.35→0.44），与 DeepSeek/Qwen random 低 sparsity NS 模式定性不同。GSM8K 跨 benchmark 验证（D075）：importance masking 的 phase gradient 在 GSM8K 上同样单调递增（QW: 0.039→0.158→1.100→2.092; DS: 0.241→0.740→1.992→4.682），但 strategy specificity（importance/random gradient ratio）从 MATH-500 的 15-36× 衰减至 GSM8K 的 2.3-3.8×。注意：\\\"反转\\\"仅在原始 II_low 值上（random > importance），phase gradient 层面 importance ≥ random。Strategy specificity 的 task-dependence 机制是开放问题（见 §6 Discussion）。这一发现挑战了 compound degradation 均匀分布的隐含假设。\\n\\n**数字基准**：所有数字基于 bf16 per-problem paired 统计量（B=10000 bootstrap）。median_diff 定义为 median(II_low_i − II_high_i)（逐 problem 配对差的中位数）。fp16 旧数据已弃用。\\n\\n## Narrative Arc\\n\\nCompound sparsity 是高效 LLM 推理的实用部署需求，但 prior work（SparK, Ada-KV, SLiM）将 compound interaction 视为均匀超可加。我们发现 severity 是 strategy × phase 交互的涌现属性：importance eviction 的 compound interaction 在 low-sparsity phase 远大于 high-sparsity phase（paired median difference 单调递增 0.32→9.94），而 random eviction 在低 sparsity (s015/s020) NS，在 s025+ 跨模型显著但效应量远小于 importance (3-15×)——存在 sparsity threshold (~s020-s025)，低于阈值 compound effect importance-specific，高于阈值两者均触发但 importance 主导。Cross-model replication 方向一致（Qwen magnitude ~1/4 of DeepSeek，onset threshold s≥0.20）。LLaMA 跨架构验证已完成（c3_llama, D060）：qualitative direction consistent（importance phase gradient d_z≈1.0），但 imp_vs_rand 交互弱（d_z 0.19→0.34, 仅 s030 显著），且 random 也显示非平凡 phase gradient（d_z 0.35→0.44），strategy-dependence 强度 architecture-dependent。我们通过 discrimination collapse 机制解释这一现象：head pruning → importance score 的判别力崩塌（Gini/CV 下降跨模型一致）→ importance eviction 退化为有偏伪随机。Attention entropy redistribution 作为 model-dependent secondary effect 在 DeepSeek 上观察到，但在 Qwen 上不稳健（D044）。\\n\\n**Framing 硬约束（D015）**：\\n- MUST: \\\\\\\\\\\\\\\"emergent phase-strategy interaction\\\\\\\\\\\\\\\"\\n- MUST NOT: \\\\\\\\\\\\\\\"importance metric limitation / importance is broken\\\\\\\\\\\\\\\"\\n- MUST NOT: claim \\\\\\\\\\\\\\\"importance masking produces super-additive interaction\\\\\\\\\\\\\\\" without qualifier — random masking also produces positive II, and at s025+ random is statistically significant (D063). The distinguishing signal is **magnitude gradient** (importance 3-15× larger) and **onset threshold** (random NS below ~s020, importance significant from s015+), not the existence of super-additivity itself (D023)\\n\\n## Core Claims\\n\\n| ID | Claim | Status | Key Evidence |\\n|----|-------|--------|-------------|\\n| C1 | Compound sparsity severity is strategy- and task-modulated | confirmed | MATH-500: importance gradient 15-36× random; GSM8K: ratio 衰减至 2.3-3.8× (D075)。Phase gradient 层面 importance ≥ random 跨 benchmark 成立，但 magnitude ratio task-dependent。Threshold ~s020-s025 (D063) |\\n| C2 | Severity is phase-modulated (amplified in low-sparsity phase) | confirmed | bf16 paired median difference 单调递增: 0.32→1.15→3.97→9.94; Bonferroni p<0.005 全 4 水平 (D032)。预注册：n=500 后若 QW s015 CI 仍跨零，叙事改为 'compound effect emerges above threshold sparsity (~s020)' |\\n| C3 | Phase-strategy crossover exists | confirmed | s=0.25: importance high_phase=0.032 < random=0.818, importance low_phase=7.196 > random=1.363 (bf16) |\\n| C4 | Discrimination collapse as primary mechanism; entropy redistribution model-dependent | partially_confirmed | D044: Gini/CV 下降跨模型一致; entropy collapse DeepSeek 一致但 Qwen s025 反转(+0.045) s030≈0。30/30 problems completed. |\\n| C5 | Phase-modulated compound severity generalizes across models | confirmed | DeepSeek + Qwen cross-model replication: 方向一致, Cohen's d ρ=1.0, gradient permutation p=0.043. Qwen magnitude ~1/4 of DeepSeek, onset threshold s≥0.20 (S3→C). |\\n| C5b | Phase-aware mitigation recovers compound degradation | future_work | D056: pilot 完成 gate_failed。Oracle recovery 18% < 30% gate (Wilcoxon p=0.002)，heuristic 32% 但 CI 跨零。方向正确但效应量不足，需更精细 phase boundary estimation → future work |\\n| C6 | Severity gradient is sub-exponential | confirmed | Growth rate decreasing: Δ增长因子 3.8×→4.8×→2.0×（递减） |\\n| C7 | Statistical power at n=500 confirms dose-response | running | c2_n500_deepseek + c2_qw_n500 (n=500, 8 conditions each) |\\n| C8 | Cross-architecture validation (LLaMA) | partially_confirmed | D060: within-importance phase gradient 强(d_z~1.0) ✓，但 imp_vs_rand 交互弱(d_z 0.19→0.34, 仅 s030 Bonferroni p=0.029 显著)。**关键**：random 在 LLaMA 上也显示显著 phase gradient(d_z 0.35→0.44, CI 排除零)，与 DeepSeek/Qwen random 低 sparsity NS 模式定性不同。Qualitative direction consistent, quantitative strategy×phase interaction weaker + architecture-dependent。论文禁用 \\\"confirms\\\"，改用 \\\"suggests\\\"/\\\"provides partial support\\\"。 |\\n| C9 | Differentiation from Lethe/SparK prior work | planned | Related Work §2 引用区分 + SparK gap analysis |\\n| S3→C | Onset threshold is model-dependent (DeepSeek s≥0.15, Qwen s≥0.20) | confirmed | D037/D038: Qwen s015 d=0.28 CI含0, s020+ 显著 |\\n| C10 | Phase gradient cross-benchmark robust; strategy specificity task-modulated | running | GSM8K DS gradient 0.241→4.682 单调递增; QW gradient 0.039→2.092; imp/rand ratio 衰减至 2.3-3.8× (D075)。QW random s025+s030 待完成 |\\n| S7→C | Dose-response monotonicity (Spearman ρ=1.0) | confirmed | D047: 6-point dose-response, 单调递增 |\\n\\n## Anticipated Reviewer Concerns\\n\\n### RC1: Generalizability — 7B models only, benchmark scope\\n- **预期质疑**: \\\\\\\"Results on two 7B models and MATH-500 only. How do we know this generalizes to larger models or other reasoning tasks?\\\\\\\"\\n- **应对**: 四层泛化证据：(1) Cross-model: DeepSeek-R1-Distill-Qwen-7B + Qwen2.5-7B-Instruct（同架构不同训练，ρ=1.0）(2) Cross-architecture: c3_llama (DeepSeek-R1-Distill-Llama-8B, LlamaForCausalLM)，qualitative direction consistent，但需加限定——LLaMA 上 random 也显示 phase gradient，strategy × phase 交互弱于 Qwen2 架构（D060）(3) **Cross-benchmark (D075)**: GSM8K（两模型）phase gradient 单调递增复现（DS: 0.241→4.682; QW: 0.039→2.092），但 strategy specificity ratio 从 MATH-500 15-36× 衰减至 2.3-3.8×，表明 phase modulation 跨 benchmark 稳健而 magnitude modulation task-dependent。Limitations 诚实声明：(a) 7B scale only；(b) strategy specificity 强度 task-dependent（GSM8K 衰减，可能因推理链更短）；(c) LLaMA 跨架构验证 n=50 限制功效；(d) random phase gradient 行为 architecture-dependent。\\n- **实验支撑**: C5 (cross-model) + C8 (c3_llama cross-architecture) + C10 (cross-benchmark GSM8K, D075)\\n\\n### RC2: Mechanism — entropy-discrimination collapse 缺乏直接测量\\n- **预期质疑**: \\\\\\\"The mechanism is conceptual. Where is the empirical evidence for entropy increase and discrimination collapse?\\\\\\\"\\n- **应对**: c4_entropy 实验已完成（DeepSeek 30/30 + Qwen 30/30）。D044 结论：Gini/CV 下降跨模型一致（discrimination collapse confirmed）；entropy redistribution 在 DeepSeek 上一致但在 Qwen 上 s025 方向反转、s030 近零（model-dependent）。论文以 discrimination collapse 为主线，entropy 作 DeepSeek 特有的强化因素。\\n- **实验支撑**: c4_entropy (DeepSeek DONE) + qwen_c4_entropy (DONE, negative for entropy universality)\\n\\n### RC3: Practical impact — 没有 throughput 数据\\n- **预期质疑**: \\\\\\\"No wall-clock or throughput measurements. Is the severity amplification reflected in actual inference speed?\\\\\\\"\\n- **应对**: 本文定位是 empirical finding paper（发现 + 机制解释），不是 method paper。Throughput 不是 claim 的一部分。Discussion 中明确 phase-gated controller 作为 future direction。\\n  - C5b pilot 已完成（D056）：oracle recovery 18%（Wilcoxon p=0.002），heuristic recovery 32%（p=0.024），但两者 95% CI 均跨零。方向正确（Wilcoxon 显著）但效应量不足（未达 30% gate），需更精细的 phase boundary estimation。论文 §6 Discussion 诚实报告 pilot 结果 + future work。\\n  - Heuristic > oracle 悖论值得提及：token position ratio 粗粒度划分可能恰好更适合 mitigation 场景，暗示 phase boundary 的最优粒度是开放问题。\\n- **实验支撑**: c5b_pilot (gate_failed, D056)\\n\\n### RC4: Statistical rigor — bootstrap 是否足够\\n- **预期质疑**: \\\\\\\"Per-problem bootstrap with 50 problems — sufficient sample size?\\\\\\\"\\n- **应对**: bf16 使用 B=10000 per-problem paired bootstrap，有效配对数 n=49 (DeepSeek) / n=46 (Qwen)；n=500 实验进一步验证 (C7 running)。Permutation test 使用 paired median difference 作为 robust statistic（D032），Bonferroni 校正后全 4 水平 p<0.005。Dose-response 主用 Wilcoxon signed-rank p + median_diff（robust to outliers），d_z 作为辅助效应量（DeepSeek 0.44→0.80, Qwen 0.28→1.02），注释高 sparsity 下 d_z 受 outlier-driven variance 影响（DS s020→s025: d_z=-0.156 \\\"negligible\\\" 但 median 3.3× jump，因极端 II 值摧毁 d_z 分母，D064）。可在 appendix 补充 per-problem 分布图（已生成 fig4_per_problem_dist.pdf）。\\n- **实验支撑**: bf16 permutation test (D032) + Cohen's d per-problem paired (rebootstrap B=10000) + n=500 Wilcoxon (C7 running)\\n\\n### RC5: Novelty — prior work 是否已覆盖 phase-dependent sparsity\\n- **预期质疑**: \\\"ThinKV and phase-aware methods already consider phase. What's new?\\\"\\n- **应对**: Prior work 在单轴上分析 phase（ThinKV: phase-aware eviction）或 compound（SparK: joint compression）。没有工作同时分析 compound × phase × strategy 的三维交互。Crossover 现象（同一 strategy 在不同 phase 方向反转）是全新发现。Related Work 加 Lethe 引用区分 + SparK 对比。具体区分：\\n  - **ThinKV** (arxiv 2510.01290, Oct 2025): 在 KV cache 单轴上做 phase-aware 压缩（按 CoT 阶段差异化 eviction），但不涉及 pruning × eviction 的 compound interaction。我们研究的是双轴（head pruning × KV eviction）compound interaction 如何随 phase 变化，ThinKV 的单轴 phase-aware 策略是我们分析维度的子集。\\n  - **Physics of KV Cache Compression** (arxiv 2603.01426, Mar 2026): 揭示了单轴 KV 压缩的 phase transition 和 representational rigidity，是机制层面最接近的工作。关键区分：他们刻画的是单一压缩轴上压缩率的 critical threshold（phase transition），我们刻画的是两种压缩方法的 compound interaction severity 如何被 reasoning phase 调制（phase-dependent gradient）——维度正交。\\n  - **HIES** (arxiv 2510.13832, Oct 2025): 发现 importance score collapse 并提出 entropy 补偿，为我们的 discrimination collapse 机制提供独立 supporting evidence——他们在单轴上观察到的 score collapse 正是我们在 compound setting 中发现的 Gini/CV 下降的单轴对应。\\n  - **R-KV** (arxiv 2505.24133, May 2025): 针对 reasoning task 做 KV compression 优化，属于 task-specific method。我们不是提出新方法，而是 mechanistic 分析 compound interaction 的 phase-dependent 行为，二者目标不同（optimization vs understanding）。\\n- **实验支撑**: C3 (crossover), Related Work §2 的 gap 分析\\n\\n### RC6: Novelty vs Lethe/SparK\\n- **预期质疑**: \\\"How does this differ from Lethe (AAAI 2026) which also does layer-time-adaptive KV pruning, or SparK which studies compound compression?\\\"\\n- **应对**: Lethe 和 SparK 都没有分析 phase × strategy 的交互效应。Lethe 是 method paper（提出 adaptive eviction 方法），我们是 empirical finding paper（发现 phase-dependent severity gradient）。SparK 研究 compound compression 但将 interaction 视为均匀超可加，我们发现 interaction severity 随 phase 和 strategy 变化。新近工作进一步确认我们的独特定位：\\n  - **Physics of KV Cache Compression** (arxiv 2603.01426, Mar 2026) 是最近的相关工作，研究单轴压缩的 phase transition 阈值行为。与我们的核心区别：他们的 phase transition 是压缩率维度上的 critical point，我们的 phase-dependent gradient 是 reasoning phase 维度上 compound interaction 的连续调制——两者刻画的 \\\"phase\\\" 语义不同（compression-rate phase vs reasoning phase）。\\n  - **ThinKV** (arxiv 2510.01290, Oct 2025) 和 **R-KV** (arxiv 2505.24133, May 2025) 都在 KV compression 单轴上引入 phase/reasoning awareness，但均未涉及 compound interaction。我们的贡献在于揭示 pruning × eviction 双轴交互如何被 reasoning phase 调制，这是单轴方法无法观察到的涌现现象。\\n  - **HIES** (arxiv 2510.13832, Oct 2025) 的 importance score collapse 发现为我们的 discrimination collapse 机制提供了独立佐证，但 HIES 聚焦于单轴补偿方法，未研究 collapse 在 compound setting 中的放大效应。\\n  - Related Work §2 明确区分三者定位：Lethe/SparK = method/compound method, ThinKV/R-KV = single-axis phase-aware, Physics of KV = single-axis phase transition, HIES = single-axis collapse。我们 = compound × phase × strategy 三维交互分析。\\n- **实验支撑**: 不需要额外实验，仅需 §2 引用区分\\n\\n## Paper Positioning\\n\\n**类型**: Empirical finding paper（非 method paper）\\n**核心贡献**:\\n1. 发现 compound sparsity severity 的 strategy × phase 交互\\n2. 量化 severity gradient（bf16 paired median difference 0.32→9.94, Cohen's d 0.44→0.80）和 crossover 现象\\n3. 提出 discrimination collapse 机制解释（Gini/CV 跨模型一致；entropy redistribution model-dependent）\\n4. Cross-model + cross-architecture (LLaMA) replication 验证泛化性（三模型两架构；LLaMA partially_confirmed，strategy×phase 交互强度 architecture-dependent, D060）\\n\\n**投稿目标**: EMNLP 2026 ARR, deadline 2026-05-25\\n**Rebuttal 准备**: Day 9 (2026-05-23) 预留 rebuttal letter 写作时间\\n**关键时间线**：\\n- Day 9 (2026-05-23): 预留写 rebuttal letter\\n- Day 11 (2026-05-25): EMNLP 2026 ARR 截稿\\n\", \"total_chars\": 12464, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "59e32fd6-7fc1-4c06-9967-4425140f3027",
  "isSidechain": false,
  "promptId": "5d98afa4-bc8d-47c1-b014-8bbe0580361f",
  "type": "user",
  "uuid": "e870610b-266f-417d-9575-a32534df6ff7",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"path\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/paper_framing.md\\\", \\\"content\\\": \\\"# Paper Framing — Phase-Gated Compound Sparsity\\\\n\\\\n> 最后更新: 2026-05-15 (D080v3 GSM8K median-based 数据更新: DS 0.241→4.682, QW 0.039→2.092, imp/rand ratio 2.3-3.8×) | 维护者: Director\\\\n\\\\n## Core Insight\\\\n\\\\nCompound sparsity（attention head pruning + KV cache eviction）的 severity 不是固定常数——它是 eviction strategy 和 reasoning phase 交互的涌现属性。Importance-based eviction 的 compound interaction severity（paired median difference: median(II_low_i − II_high_i)）随 sparsity 单调递增（DeepSeek: 0.32→1.15→3.97→9.94; Qwen: 0.048→0.208→1.109→2.619），而 random masking 在 s015/s020 NS，在 s025 跨模型显著但效应量远小于 importance（DS: 0.257 vs 3.986; QW: 0.393 vs 1.074, 3-15×差异），存在 sparsity threshold ~s020-s025（D063; s030 待定）。Cohen's d（paired d_z, B=10000）从 small-medium 到 large（DeepSeek: 0.44→0.80; Qwen: 0.28→1.02，s015 边缘）。LLaMA 跨架构验证（D060）qualitative direction consistent（within-importance d_z~1.0），但 strategy×phase 交互弱于 Qwen2 架构（imp_vs_rand d_z 0.19→0.34, 仅 s030 显著），且 random 在 LLaMA 上也显示显著 phase gradient（d_z 0.35→0.44），与 DeepSeek/Qwen random 低 sparsity NS 模式定性不同。GSM8K 跨 benchmark 验证（D075）：importance masking 的 phase gradient 在 GSM8K 上同样单调递增（QW: 0.039→0.158→1.100→2.092; DS: 0.241→0.740→1.992→4.682），但 strategy specificity（importance/random gradient ratio）从 MATH-500 的 15-36× 衰减至 GSM8K 的 2.3-3.8×。注意：\\\\\\\"反转\\\\\\\"仅在原始 II_low 值上（random > importance），phase gradient 层面 importance ≥ random。Strategy specificity 的 task-dependence 机制是开放问题（见 §6 Discussion）。这一发现挑战了 compound degradation 均匀分布的隐含假设。\\\\n\\\\n**数字基准**：所有数字基于 bf16 per-problem paired 统计量（B=10000 bootstrap）。median_diff 定义为 median(II_low_i − II_high_i)（逐 problem 配对差的中位数）。fp16 旧数据已弃用。\\\\n\\\\n## Narrative Arc\\\\n\\\\nCompound sparsity 是高效 LLM 推理的实用部署需求，但 prior work（SparK, Ada-KV, SLiM）将 compound interaction 视为均匀超可加。我们发现 severity 是 strategy × phase 交互的涌现属性：importance eviction 的 compound interaction 在 low-sparsity phase 远大于 high-sparsity phase（paired median difference 单调递增 0.32→9.94），而 random eviction 在低 sparsity (s015/s020) NS，在 s025+ 跨模型显著但效应量远小于 importance (3-15×)——存在 sparsity threshold (~s020-s025)，低于阈值 compound effect importance-specific，高于阈值两者均触发但 importance 主导。Cross-model replication 方向一致（Qwen magnitude ~1/4 of DeepSeek，onset threshold s≥0.20）。LLaMA 跨架构验证已完成（c3_llama, D060）：qualitative direction consistent（importance phase gradient d_z≈1.0），但 imp_vs_rand 交互弱（d_z 0.19→0.34, 仅 s030 显著），且 random 也显示非平凡 phase gradient（d_z 0.35→0.44），strategy-dependence 强度 architecture-dependent。我们通过 discrimination collapse 机制解释这一现象：head pruning → importance score 的判别力崩塌（Gini/CV 下降跨模型一致）→ importance eviction 退化为有偏伪随机。Attention entropy redistribution 作为 model-dependent secondary effect 在 DeepSeek 上观察到，但在 Qwen 上不稳健（D044）。\\\\n\\\\n**Framing 硬约束（D015）**：\\\\n- MUST: \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\"emergent phase-strategy interaction\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\"\\\\n- MUST NOT: \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\"importance metric limitation / importance is broken\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\"\\\\n- MUST NOT: claim \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\"importance masking produces super-additive interaction\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\" without qualifier — random masking also produces positive II, and at s025+ random is statistically significant (D063). The distinguishing signal is **magnitude gradient** (importance 3-15× larger) and **onset threshold** (random NS below ~s020, importance significant from s015+), not the existence of super-additivity itself (D023)\\\\n\\\\n## Core Claims\\\\n\\\\n| ID | Claim | Status | Key Evidence |\\\\n|----|-------|--------|-------------|\\\\n| C1 | Compound sparsity severity is strategy- and task-modulated | confirmed | MATH-500: importance gradient 15-36× random; GSM8K: ratio 衰减至 2.3-3.8× (D075)。Phase gradient 层面 importance ≥ random 跨 benchmark 成立，但 magnitude ratio task-dependent。Threshold ~s020-s025 (D063) |\\\\n| C2 | Severity is phase-modulated (amplified in low-sparsity phase) | confirmed | bf16 paired median difference 单调递增: 0.32→1.15→3.97→9.94; Bonferroni p<0.005 全 4 水平 (D032)。预注册：n=500 后若 QW s015 CI 仍跨零，叙事改为 'compound effect emerges above threshold sparsity (~s020)' |\\\\n| C3 | Phase-strategy crossover exists | confirmed | s=0.25: importance high_phase=0.032 < random=0.818, importance low_phase=7.196 > random=1.363 (bf16) |\\\\n| C4 | Discrimination collapse as primary mechanism; entropy redistribution model-dependent | partially_confirmed | D044: Gini/CV 下降跨模型一致; entropy collapse DeepSeek 一致但 Qwen s025 反转(+0.045) s030≈0。30/30 problems completed. |\\\\n| C5 | Phase-modulated compound severity generalizes across models | confirmed | DeepSeek + Qwen cross-model replication: 方向一致, Cohen's d ρ=1.0, gradient permutation p=0.043. Qwen magnitude ~1/4 of DeepSeek, onset threshold s≥0.20 (S3→C). |\\\\n| C5b | Phase-aware mitigation recovers compound degradation | future_work | D056: pilot 完成 gate_failed。Oracle recovery 18% < 30% gate (Wilcoxon p=0.002)，heuristic 32% 但 CI 跨零。方向正确但效应量不足，需更精细 phase boundary estimation → future work |\\\\n| C6 | Severity gradient is sub-exponential | confirmed | Growth rate decreasing: Δ增长因子 3.8×→4.8×→2.0×（递减） |\\\\n| C7 | Statistical power at n=500 confirms dose-response | running | c2_n500_deepseek + c2_qw_n500 (n=500, 8 conditions each) |\\\\n| C8 | Cross-architecture validation (LLaMA) | partially_confirmed | D060: within-importance phase gradient 强(d_z~1.0) ✓，但 imp_vs_rand 交互弱(d_z 0.19→0.34, 仅 s030 Bonferroni p=0.029 显著)。**关键**：random 在 LLaMA 上也显示显著 phase gradient(d_z 0.35→0.44, CI 排除零)，与 DeepSeek/Qwen random 低 sparsity NS 模式定性不同。Qualitative direction consistent, quantitative strategy×phase interaction weaker + architecture-dependent。论文禁用 \\\\\\\"confirms\\\\\\\"，改用 \\\\\\\"suggests\\\\\\\"/\\\\\\\"provides partial support\\\\\\\"。 |\\\\n| C9 | Differentiation from Lethe/SparK prior work | planned | Related Work §2 引用区分 + SparK gap analysis |\\\\n| S3→C | Onset threshold is model-dependent (DeepSeek s≥0.15, Qwen s≥0.20) | confirmed | D037/D038: Qwen s015 d=0.28 CI含0, s020+ 显著 |\\\\n| C10 | Phase gradient cross-benchmark robust; strategy specificity task-modulated | running | GSM8K DS gradient 0.241→4.682 单调递增; QW gradient 0.039→2.092; imp/rand ratio 衰减至 2.3-3.8× (D075)。QW random s025+s030 待完成 |\\\\n| S7→C | Dose-response monotonicity (Spearman ρ=1.0) | confirmed | D047: 6-point dose-response, 单调递增 |\\\\n\\\\n## Anticipated Reviewer Concerns\\\\n\\\\n### RC1: Generalizability — 7B models only, benchmark scope\\\\n- **预期质疑**: \\\\\\\\\\\\\\\"Results on two 7B models and MATH-500 only. How do we know this generalizes to larger models or other reasoning tasks?\\\\\\\\\\\\\\\"\\\\n- **应对**: 四层泛化证据：(1) Cross-model: DeepSeek-R1-Distill-Qwen-7B + Qwen2.5-7B-Instruct（同架构不同训练，ρ=1.0）(2) Cross-architecture: c3_llama (DeepSeek-R1-Distill-Llama-8B, LlamaForCausalLM)，qualitative direction consistent，但需加限定——LLaMA 上 random 也显示 phase gradient，strategy × phase 交互弱于 Qwen2 架构（D060）(3) **Cross-benchmark (D075)**: GSM8K（两模型）phase gradient 单调递增复现（DS: 0.241→4.682; QW: 0.039→2.092），但 strategy specificity ratio 从 MATH-500 15-36× 衰减至 2.3-3.8×，表明 phase modulation 跨 benchmark 稳健而 magnitude modulation task-dependent。Limitations 诚实声明：(a) 7B scale only；(b) strategy specificity 强度 task-dependent（GSM8K 衰减，可能因推理链更短）；(c) LLaMA 跨架构验证 n=50 限制功效；(d) random phase gradient 行为 architecture-dependent。\\\\n- **实验支撑**: C5 (cross-model) + C8 (c3_llama cross-architecture) + C10 (cross-benchmark GSM8K, D075)\\\\n\\\\n### RC2: Mechanism — entropy-discrimination collapse 缺乏直接测量\\\\n- **预期质疑**: \\\\\\\\\\\\\\\"The mechanism is conceptual. Where is the empirical evidence for entropy increase and discrimination collapse?\\\\\\\\\\\\\\\"\\\\n- **应对**: c4_entropy 实验已完成（DeepSeek 30/30 + Qwen 30/30）。D044 结论：Gini/CV 下降跨模型一致（discrimination collapse confirmed）；entropy redistribution 在 DeepSeek 上一致但在 Qwen 上 s025 方向反转、s030 近零（model-dependent）。论文以 discrimination collapse 为主线，entropy 作 DeepSeek 特有的强化因素。\\\\n- **实验支撑**: c4_entropy (DeepSeek DONE) + qwen_c4_entropy (DONE, negative for entropy universality)\\\\n\\\\n### RC3: Practical impact — 没有 throughput 数据\\\\n- **预期质疑**: \\\\\\\\\\\\\\\"No wall-clock or throughput measurements. Is the severity amplification reflected in actual inference speed?\\\\\\\\\\\\\\\"\\\\n- **应对**: 本文定位是 empirical finding paper（发现 + 机制解释），不是 method paper。Throughput 不是 claim 的一部分。Discussion 中明确 phase-gated controller 作为 future direction。\\\\n  - C5b pilot 已完成（D056）：oracle recovery 18%（Wilcoxon p=0.002），heuristic recovery 32%（p=0.024），但两者 95% CI 均跨零。方向正确（Wilcoxon 显著）但效应量不足（未达 30% gate），需更精细的 phase boundary estimation。论文 §6 Discussion 诚实报告 pilot 结果 + future work。\\\\n  - Heuristic > oracle 悖论值得提及：token position ratio 粗粒度划分可能恰好更适合 mitigation 场景，暗示 phase boundary 的最优粒度是开放问题。\\\\n- **实验支撑**: c5b_pilot (gate_failed, D056)\\\\n\\\\n### RC4: Statistical rigor — bootstrap 是否足够\\\\n- **预期质疑**: \\\\\\\\\\\\\\\"Per-problem bootstrap with 50 problems — sufficient sample size?\\\\\\\\\\\\\\\"\\\\n- **应对**: bf16 使用 B=10000 per-problem paired bootstrap，有效配对数 n=49 (DeepSeek) / n=46 (Qwen)；n=500 实验进一步验证 (C7 running)。Permutation test 使用 paired median difference 作为 robust statistic（D032），Bonferroni 校正后全 4 水平 p<0.005。Dose-response 主用 Wilcoxon signed-rank p + median_diff（robust to outliers），d_z 作为辅助效应量（DeepSeek 0.44→0.80, Qwen 0.28→1.02），注释高 sparsity 下 d_z 受 outlier-driven variance 影响（DS s020→s025: d_z=-0.156 \\\\\\\"negligible\\\\\\\" 但 median 3.3× jump，因极端 II 值摧毁 d_z 分母，D064）。可在 appendix 补充 per-problem 分布图（已生成 fig4_per_problem_dist.pdf）。\\\\n- **实验支撑**: bf16 permutation test (D032) + Cohen's d per-problem paired (rebootstrap B=10000) + n=500 Wilcoxon (C7 running)\\\\n\\\\n### RC5: Novelty — prior work 是否已覆盖 phase-dependent sparsity\\\\n- **预期质疑**: \\\\\\\"ThinKV and phase-aware methods already consider phase. What's new?\\\\\\\"\\\\n- **应对**: Prior work 在单轴上分析 phase（ThinKV: phase-aware eviction）或 compound（SparK: joint compression）。没有工作同时分析 compound × phase × strategy 的三维交互。Crossover 现象（同一 strategy 在不同 phase 方向反转）是全新发现。Related Work 加 Lethe 引用区分 + SparK 对比。具体区分：\\\\n  - **ThinKV** (arxiv 2510.01290, Oct 2025): 在 KV cache 单轴上做 phase-aware 压缩（按 CoT 阶段差异化 eviction），但不涉及 pruning × eviction 的 compound interaction。我们研究的是双轴（head pruning × KV eviction）compound interaction 如何随 phase 变化，ThinKV 的单轴 phase-aware 策略是我们分析维度的子集。\\\\n  - **Physics of KV Cache Compression** (arxiv 2603.01426, Mar 2026): 揭示了单轴 KV 压缩的 phase transition 和 representational rigidity，是机制层面最接近的工作。关键区分：他们刻画的是单一压缩轴上压缩率的 critical threshold（phase transition），我们刻画的是两种压缩方法的 compound interaction severity 如何被 reasoning phase 调制（phase-dependent gradient）——维度正交。\\\\n  - **HIES** (arxiv 2510.13832, Oct 2025): 发现 importance score collapse 并提出 entropy 补偿，为我们的 discrimination collapse 机制提供独立 supporting evidence——他们在单轴上观察到的 score collapse 正是我们在 compound setting 中发现的 Gini/CV 下降的单轴对应。\\\\n  - **R-KV** (arxiv 2505.24133, May 2025): 针对 reasoning task 做 KV compression 优化，属于 task-specific method。我们不是提出新方法，而是 mechanistic 分析 compound interaction 的 phase-dependent 行为，二者目标不同（optimization vs understanding）。\\\\n- **实验支撑**: C3 (crossover), Related Work §2 的 gap 分析\\\\n\\\\n### RC6: Novelty vs Lethe/SparK\\\\n- **预期质疑**: \\\\\\\"How does this differ from Lethe (AAAI 2026) which also does layer-time-adaptive KV pruning, or SparK which studies compound compression?\\\\\\\"\\\\n- **应对**: Lethe 和 SparK 都没有分析 phase × strategy 的交互效应。Lethe 是 method paper（提出 adaptive eviction 方法），我们是 empirical finding paper（发现 phase-dependent severity gradient）。SparK 研究 compound compression 但将 interaction 视为均匀超可加，我们发现 interaction severity 随 phase 和 strategy 变化。新近工作进一步确认我们的独特定位：\\\\n  - **Physics of KV Cache Compression** (arxiv 2603.01426, Mar 2026) 是最近的相关工作，研究单轴压缩的 phase transition 阈值行为。与我们的核心区别：他们的 phase transition 是压缩率维度上的 critical point，我们的 phase-dependent gradient 是 reasoning phase 维度上 compound interaction 的连续调制——两者刻画的 \\\\\\\"phase\\\\\\\" 语义不同（compression-rate phase vs reasoning phase）。\\\\n  - **ThinKV** (arxiv 2510.01290, Oct 2025) 和 **R-KV** (arxiv 2505.24133, May 2025) 都在 KV compression 单轴上引入 phase/reasoning awareness，但均未涉及 compound interaction。我们的贡献在于揭示 pruning × eviction 双轴交互如何被 reasoning phase 调制，这是单轴方法无法观察到的涌现现象。\\\\n  - **HIES** (arxiv 2510.13832, Oct 2025) 的 importance score collapse 发现为我们的 discrimination collapse 机制提供了独立佐证，但 HIES 聚焦于单轴补偿方法，未研究 collapse 在 compound setting 中的放大效应。\\\\n  - Related Work §2 明确区分三者定位：Lethe/SparK = method/compound method, ThinKV/R-KV = single-axis phase-aware, Physics of KV = single-axis phase transition, HIES = single-axis collapse。我们 = compound × phase × strategy 三维交互分析。\\\\n- **实验支撑**: 不需要额外实验，仅需 §2 引用区分\\\\n\\\\n## Paper Positioning\\\\n\\\\n**类型**: Empirical finding paper（非 method paper）\\\\n**核心贡献**:\\\\n1. 发现 compound sparsity severity 的 strategy × phase 交互\\\\n2. 量化 severity gradient（bf16 paired median difference 0.32→9.94, Cohen's d 0.44→0.80）和 crossover 现象\\\\n3. 提出 discrimination collapse 机制解释（Gini/CV 跨模型一致；entropy redistribution model-dependent）\\\\n4. Cross-model + cross-architecture (LLaMA) replication 验证泛化性（三模型两架构；LLaMA partially_confirmed，strategy×phase 交互强度 architecture-dependent, D060）\\\\n\\\\n**投稿目标**: EMNLP 2026 ARR, deadline 2026-05-25\\\\n**Rebuttal 准备**: Day 9 (2026-05-23) 预留 rebuttal letter 写作时间\\\\n**关键时间线**：\\\\n- Day 9 (2026-05-23): 预留写 rebuttal letter\\\\n- Day 11 (2026-05-25): EMNLP 2026 ARR 截稿\\\\n\\\", \\\"total_chars\\\": 12464, \\\"truncated\\\": false}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/paper_framing.md\", \"content\": \"# Paper Framing — Phase-Gated Compound Sparsity\\n\\n> 最后更新: 2026-05-15 (D080v3 GSM8K median-based 数据更新: DS 0.241→4.682, QW 0.039→2.092, imp/rand ratio 2.3-3.8×) | 维护者: Director\\n\\n## Core Insight\\n\\nCompound sparsity（attention head pruning + KV cache eviction）的 severity 不是固定常数——它是 eviction strategy 和 reasoning phase 交互的涌现属性。Importance-based eviction 的 compound interaction severity（paired median difference: median(II_low_i − II_high_i)）随 sparsity 单调递增（DeepSeek: 0.32→1.15→3.97→9.94; Qwen: 0.048→0.208→1.109→2.619），而 random masking 在 s015/s020 NS，在 s025 跨模型显著但效应量远小于 importance（DS: 0.257 vs 3.986; QW: 0.393 vs 1.074, 3-15×差异），存在 sparsity threshold ~s020-s025（D063; s030 待定）。Cohen's d（paired d_z, B=10000）从 small-medium 到 large（DeepSeek: 0.44→0.80; Qwen: 0.28→1.02，s015 边缘）。LLaMA 跨架构验证（D060）qualitative direction consistent（within-importance d_z~1.0），但 strategy×phase 交互弱于 Qwen2 架构（imp_vs_rand d_z 0.19→0.34, 仅 s030 显著），且 random 在 LLaMA 上也显示显著 phase gradient（d_z 0.35→0.44），与 DeepSeek/Qwen random 低 sparsity NS 模式定性不同。GSM8K 跨 benchmark 验证（D075）：importance masking 的 phase gradient 在 GSM8K 上同样单调递增（QW: 0.039→0.158→1.100→2.092; DS: 0.241→0.740→1.992→4.682），但 strategy specificity（importance/random gradient ratio）从 MATH-500 的 15-36× 衰减至 GSM8K 的 2.3-3.8×。注意：\\\"反转\\\"仅在原始 II_low 值上（random > importance），phase gradient 层面 importance ≥ random。Strategy specificity 的 task-dependence 机制是开放问题（见 §6 Discussion）。这一发现挑战了 compound degradation 均匀分布的隐含假设。\\n\\n**数字基准**：所有数字基于 bf16 per-problem paired 统计量（B=10000 bootstrap）。median_diff 定义为 median(II_low_i − II_high_i)（逐 problem 配对差的中位数）。fp16 旧数据已弃用。\\n\\n## Narrative Arc\\n\\nCompound sparsity 是高效 LLM 推理的实用部署需求，但 prior work（SparK, Ada-KV, SLiM）将 compound interaction 视为均匀超可加。我们发现 severity 是 strategy × phase 交互的涌现属性：importance eviction 的 compound interaction 在 low-sparsity phase 远大于 high-sparsity phase（paired median difference 单调递增 0.32→9.94），而 random eviction 在低 sparsity (s015/s020) NS，在 s025+ 跨模型显著但效应量远小于 importance (3-15×)——存在 sparsity threshold (~s020-s025)，低于阈值 compound effect importance-specific，高于阈值两者均触发但 importance 主导。Cross-model replication 方向一致（Qwen magnitude ~1/4 of DeepSeek，onset threshold s≥0.20）。LLaMA 跨架构验证已完成（c3_llama, D060）：qualitative direction consistent（importance phase gradient d_z≈1.0），但 imp_vs_rand 交互弱（d_z 0.19→0.34, 仅 s030 显著），且 random 也显示非平凡 phase gradient（d_z 0.35→0.44），strategy-dependence 强度 architecture-dependent。我们通过 discrimination collapse 机制解释这一现象：head pruning → importance score 的判别力崩塌（Gini/CV 下降跨模型一致）→ importance eviction 退化为有偏伪随机。Attention entropy redistribution 作为 model-dependent secondary effect 在 DeepSeek 上观察到，但在 Qwen 上不稳健（D044）。\\n\\n**Framing 硬约束（D015）**：\\n- MUST: \\\\\\\\\\\\\\\"emergent phase-strategy interaction\\\\\\\\\\\\\\\"\\n- MUST NOT: \\\\\\\\\\\\\\\"importance metric limitation / importance is broken\\\\\\\\\\\\\\\"\\n- MUST NOT: claim \\\\\\\\\\\\\\\"importance masking produces super-additive interaction\\\\\\\\\\\\\\\" without qualifier — random masking also produces positive II, and at s025+ random is statistically significant (D063). The distinguishing signal is **magnitude gradient** (importance 3-15× larger) and **onset threshold** (random NS below ~s020, importance significant from s015+), not the existence of super-additivity itself (D023)\\n\\n## Core Claims\\n\\n| ID | Claim | Status | Key Evidence |\\n|----|-------|--------|-------------|\\n| C1 | Compound sparsity severity is strategy- and task-modulated | confirmed | MATH-500: importance gradient 15-36× random; GSM8K: ratio 衰减至 2.3-3.8× (D075)。Phase gradient 层面 importance ≥ random 跨 benchmark 成立，但 magnitude ratio task-dependent。Threshold ~s020-s025 (D063) |\\n| C2 | Severity is phase-modulated (amplified in low-sparsity phase) | confirmed | bf16 paired median difference 单调递增: 0.32→1.15→3.97→9.94; Bonferroni p<0.005 全 4 水平 (D032)。预注册：n=500 后若 QW s015 CI 仍跨零，叙事改为 'compound effect emerges above threshold sparsity (~s020)' |\\n| C3 | Phase-strategy crossover exists | confirmed | s=0.25: importance high_phase=0.032 < random=0.818, importance low_phase=7.196 > random=1.363 (bf16) |\\n| C4 | Discrimination collapse as primary mechanism; entropy redistribution model-dependent | partially_confirmed | D044: Gini/CV 下降跨模型一致; entropy collapse DeepSeek 一致但 Qwen s025 反转(+0.045) s030≈0。30/30 problems completed. |\\n| C5 | Phase-modulated compound severity generalizes across models | confirmed | DeepSeek + Qwen cross-model replication: 方向一致, Cohen's d ρ=1.0, gradient permutation p=0.043. Qwen magnitude ~1/4 of DeepSeek, onset threshold s≥0.20 (S3→C). |\\n| C5b | Phase-aware mitigation recovers compound degradation | future_work | D056: pilot 完成 gate_failed。Oracle recovery 18% < 30% gate (Wilcoxon p=0.002)，heuristic 32% 但 CI 跨零。方向正确但效应量不足，需更精细 phase boundary estimation → future work |\\n| C6 | Severity gradient is sub-exponential | confirmed | Growth rate decreasing: Δ增长因子 3.8×→4.8×→2.0×（递减） |\\n| C7 | Statistical power at n=500 confirms dose-response | running | c2_n500_deepseek + c2_qw_n500 (n=500, 8 conditions each) |\\n| C8 | Cross-architecture validation (LLaMA) | partially_confirmed | D060: within-importance phase gradient 强(d_z~1.0) ✓，但 imp_vs_rand 交互弱(d_z 0.19→0.34, 仅 s030 Bonferroni p=0.029 显著)。**关键**：random 在 LLaMA 上也显示显著 phase gradient(d_z 0.35→0.44, CI 排除零)，与 DeepSeek/Qwen random 低 sparsity NS 模式定性不同。Qualitative direction consistent, quantitative strategy×phase interaction weaker + architecture-dependent。论文禁用 \\\"confirms\\\"，改用 \\\"suggests\\\"/\\\"provides partial support\\\"。 |\\n| C9 | Differentiation from Lethe/SparK prior work | planned | Related Work §2 引用区分 + SparK gap analysis |\\n| S3→C | Onset threshold is model-dependent (DeepSeek s≥0.15, Qwen s≥0.20) | confirmed | D037/D038: Qwen s015 d=0.28 CI含0, s020+ 显著 |\\n| C10 | Phase gradient cross-benchmark robust; strategy specificity task-modulated | running | GSM8K DS gradient 0.241→4.682 单调递增; QW gradient 0.039→2.092; imp/rand ratio 衰减至 2.3-3.8× (D075)。QW random s025+s030 待完成 |\\n| S7→C | Dose-response monotonicity (Spearman ρ=1.0) | confirmed | D047: 6-point dose-response, 单调递增 |\\n\\n## Anticipated Reviewer Concerns\\n\\n### RC1: Generalizability — 7B models only, benchmark scope\\n- **预期质疑**: \\\\\\\"Results on two 7B models and MATH-500 only. How do we know this generalizes to larger models or other reasoning tasks?\\\\\\\"\\n- **应对**: 四层泛化证据：(1) Cross-model: DeepSeek-R1-Distill-Qwen-7B + Qwen2.5-7B-Instruct（同架构不同训练，ρ=1.0）(2) Cross-architecture: c3_llama (DeepSeek-R1-Distill-Llama-8B, LlamaForCausalLM)，qualitative direction consistent，但需加限定——LLaMA 上 random 也显示 phase gradient，strategy × phase 交互弱于 Qwen2 架构（D060）(3) **Cross-benchmark (D075)**: GSM8K（两模型）phase gradient 单调递增复现（DS: 0.241→4.682; QW: 0.039→2.092），但 strategy specificity ratio 从 MATH-500 15-36× 衰减至 2.3-3.8×，表明 phase modulation 跨 benchmark 稳健而 magnitude modulation task-dependent。Limitations 诚实声明：(a) 7B scale only；(b) strategy specificity 强度 task-dependent（GSM8K 衰减，可能因推理链更短）；(c) LLaMA 跨架构验证 n=50 限制功效；(d) random phase gradient 行为 architecture-dependent。\\n- **实验支撑**: C5 (cross-model) + C8 (c3_llama cross-architecture) + C10 (cross-benchmark GSM8K, D075)\\n\\n### RC2: Mechanism — entropy-discrimination collapse 缺乏直接测量\\n- **预期质疑**: \\\\\\\"The mechanism is conceptual. Where is the empirical evidence for entropy increase and discrimination collapse?\\\\\\\"\\n- **应对**: c4_entropy 实验已完成（DeepSeek 30/30 + Qwen 30/30）。D044 结论：Gini/CV 下降跨模型一致（discrimination collapse confirmed）；entropy redistribution 在 DeepSeek 上一致但在 Qwen 上 s025 方向反转、s030 近零（model-dependent）。论文以 discrimination collapse 为主线，entropy 作 DeepSeek 特有的强化因素。\\n- **实验支撑**: c4_entropy (DeepSeek DONE) + qwen_c4_entropy (DONE, negative for entropy universality)\\n\\n### RC3: Practical impact — 没有 throughput 数据\\n- **预期质疑**: \\\\\\\"No wall-clock or throughput measurements. Is the severity amplification reflected in actual inference speed?\\\\\\\"\\n- **应对**: 本文定位是 empirical finding paper（发现 + 机制解释），不是 method paper。Throughput 不是 claim 的一部分。Discussion 中明确 phase-gated controller 作为 future direction。\\n  - C5b pilot 已完成（D056）：oracle recovery 18%（Wilcoxon p=0.002），heuristic recovery 32%（p=0.024），但两者 95% CI 均跨零。方向正确（Wilcoxon 显著）但效应量不足（未达 30% gate），需更精细的 phase boundary estimation。论文 §6 Discussion 诚实报告 pilot 结果 + future work。\\n  - Heuristic > oracle 悖论值得提及：token position ratio 粗粒度划分可能恰好更适合 mitigation 场景，暗示 phase boundary 的最优粒度是开放问题。\\n- **实验支撑**: c5b_pilot (gate_failed, D056)\\n\\n### RC4: Statistical rigor — bootstrap 是否足够\\n- **预期质疑**: \\\\\\\"Per-problem bootstrap with 50 problems — sufficient sample size?\\\\\\\"\\n- **应对**: bf16 使用 B=10000 per-problem paired bootstrap，有效配对数 n=49 (DeepSeek) / n=46 (Qwen)；n=500 实验进一步验证 (C7 running)。Permutation test 使用 paired median difference 作为 robust statistic（D032），Bonferroni 校正后全 4 水平 p<0.005。Dose-response 主用 Wilcoxon signed-rank p + median_diff（robust to outliers），d_z 作为辅助效应量（DeepSeek 0.44→0.80, Qwen 0.28→1.02），注释高 sparsity 下 d_z 受 outlier-driven variance 影响（DS s020→s025: d_z=-0.156 \\\"negligible\\\" 但 median 3.3× jump，因极端 II 值摧毁 d_z 分母，D064）。可在 appendix 补充 per-problem 分布图（已生成 fig4_per_problem_dist.pdf）。\\n- **实验支撑**: bf16 permutation test (D032) + Cohen's d per-problem paired (rebootstrap B=10000) + n=500 Wilcoxon (C7 running)\\n\\n### RC5: Novelty — prior work 是否已覆盖 phase-dependent sparsity\\n- **预期质疑**: \\\"ThinKV and phase-aware methods already consider phase. What's new?\\\"\\n- **应对**: Prior work 在单轴上分析 phase（ThinKV: phase-aware eviction）或 compound（SparK: joint compression）。没有工作同时分析 compound × phase × strategy 的三维交互。Crossover 现象（同一 strategy 在不同 phase 方向反转）是全新发现。Related Work 加 Lethe 引用区分 + SparK 对比。具体区分：\\n  - **ThinKV** (arxiv 2510.01290, Oct 2025): 在 KV cache 单轴上做 phase-aware 压缩（按 CoT 阶段差异化 eviction），但不涉及 pruning × eviction 的 compound interaction。我们研究的是双轴（head pruning × KV eviction）compound interaction 如何随 phase 变化，ThinKV 的单轴 phase-aware 策略是我们分析维度的子集。\\n  - **Physics of KV Cache Compression** (arxiv 2603.01426, Mar 2026): 揭示了单轴 KV 压缩的 phase transition 和 representational rigidity，是机制层面最接近的工作。关键区分：他们刻画的是单一压缩轴上压缩率的 critical threshold（phase transition），我们刻画的是两种压缩方法的 compound interaction severity 如何被 reasoning phase 调制（phase-dependent gradient）——维度正交。\\n  - **HIES** (arxiv 2510.13832, Oct 2025): 发现 importance score collapse 并提出 entropy 补偿，为我们的 discrimination collapse 机制提供独立 supporting evidence——他们在单轴上观察到的 score collapse 正是我们在 compound setting 中发现的 Gini/CV 下降的单轴对应。\\n  - **R-KV** (arxiv 2505.24133, May 2025): 针对 reasoning task 做 KV compression 优化，属于 task-specific method。我们不是提出新方法，而是 mechanistic 分析 compound interaction 的 phase-dependent 行为，二者目标不同（optimization vs understanding）。\\n- **实验支撑**: C3 (crossover), Related Work §2 的 gap 分析\\n\\n### RC6: Novelty vs Lethe/SparK\\n- **预期质疑**: \\\"How does this differ from Lethe (AAAI 2026) which also does layer-time-adaptive KV pruning, or SparK which studies compound compression?\\\"\\n- **应对**: Lethe 和 SparK 都没有分析 phase × strategy 的交互效应。Lethe 是 method paper（提出 adaptive eviction 方法），我们是 empirical finding paper（发现 phase-dependent severity gradient）。SparK 研究 compound compression 但将 interaction 视为均匀超可加，我们发现 interaction severity 随 phase 和 strategy 变化。新近工作进一步确认我们的独特定位：\\n  - **Physics of KV Cache Compression** (arxiv 2603.01426, Mar 2026) 是最近的相关工作，研究单轴压缩的 phase transition 阈值行为。与我们的核心区别：他们的 phase transition 是压缩率维度上的 critical point，我们的 phase-dependent gradient 是 reasoning phase 维度上 compound interaction 的连续调制——两者刻画的 \\\"phase\\\" 语义不同（compression-rate phase vs reasoning phase）。\\n  - **ThinKV** (arxiv 2510.01290, Oct 2025) 和 **R-KV** (arxiv 2505.24133, May 2025) 都在 KV compression 单轴上引入 phase/reasoning awareness，但均未涉及 compound interaction。我们的贡献在于揭示 pruning × eviction 双轴交互如何被 reasoning phase 调制，这是单轴方法无法观察到的涌现现象。\\n  - **HIES** (arxiv 2510.13832, Oct 2025) 的 importance score collapse 发现为我们的 discrimination collapse 机制提供了独立佐证，但 HIES 聚焦于单轴补偿方法，未研究 collapse 在 compound setting 中的放大效应。\\n  - Related Work §2 明确区分三者定位：Lethe/SparK = method/compound method, ThinKV/R-KV = single-axis phase-aware, Physics of KV = single-axis phase transition, HIES = single-axis collapse。我们 = compound × phase × strategy 三维交互分析。\\n- **实验支撑**: 不需要额外实验，仅需 §2 引用区分\\n\\n## Paper Positioning\\n\\n**类型**: Empirical finding paper（非 method paper）\\n**核心贡献**:\\n1. 发现 compound sparsity severity 的 strategy × phase 交互\\n2. 量化 severity gradient（bf16 paired median difference 0.32→9.94, Cohen's d 0.44→0.80）和 crossover 现象\\n3. 提出 discrimination collapse 机制解释（Gini/CV 跨模型一致；entropy redistribution model-dependent）\\n4. Cross-model + cross-architecture (LLaMA) replication 验证泛化性（三模型两架构；LLaMA partially_confirmed，strategy×phase 交互强度 architecture-dependent, D060）\\n\\n**投稿目标**: EMNLP 2026 ARR, deadline 2026-05-25\\n**Rebuttal 准备**: Day 9 (2026-05-23) 预留 rebuttal letter 写作时间\\n**关键时间线**：\\n- Day 9 (2026-05-23): 预留写 rebuttal letter\\n- Day 11 (2026-05-25): EMNLP 2026 ARR 截稿\\n\", \"total_chars\": 12464, \"truncated\": false}, \"error\": null, \"metadata\": {}}"
    }
  },
  "sourceToolAssistantUUID": "59e32fd6-7fc1-4c06-9967-4425140f3027",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "sessionId": "38576691-e177-4a18-ab23-be69eff4b7ff",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-16T00:25:48.470Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_014R91JS7TNMdPZVWwbw6EsS`</summary>

```json
{
  "project": "phase-gated-compound-sparse",
  "file": "paper_framing.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1127de5b-3f3e-42e0-9605-d38048768657",
  "isSidechain": false,
  "requestId": "req_011Cb5JDa78uMR5jDzqqWGX9",
  "type": "assistant",
  "uuid": "59e32fd6-7fc1-4c06-9967-4425140f3027",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "sessionId": "38576691-e177-4a18-ab23-be69eff4b7ff",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0147BFncuYKAT8NdSsmU8MWf",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1071,
      "cache_read_input_tokens": 23443,
      "output_tokens": 326,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1071,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 326,
          "cache_read_input_tokens": 23443,
          "cache_creation_input_tokens": 1071,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1071
          },
          "type": "message"
        }
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

_source line 19_

```json
{
  "type": "last-prompt",
  "leafUuid": "e870610b-266f-417d-9575-a32534df6ff7",
  "sessionId": "38576691-e177-4a18-ab23-be69eff4b7ff"
}
```

---

### Runtime record

_source line 20_

```json
{
  "type": "ai-title",
  "aiTitle": "Compile Round 10 experiment evidence for ARR submission",
  "sessionId": "38576691-e177-4a18-ab23-be69eff4b7ff"
}
```

---

### Assistant

_source line 21 · 2026-05-16T00:25:56.820Z_

<details><summary>Logged reasoning block</summary>

```text
The registry data is too large to read directly. I need to use agents to extract the specific experiment data I need from the registry file. Let me launch parallel agents to extract different data dimensions.

Let me get the registry data parsed by agents. I have the memory.md and paper_framing.md content already. Now I need to extract specific experiments from the registry.

The registry file is at: /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-11-projects-phase-gated-compound-sparse/38576691-e177-4a18-ab23-be69eff4b7ff/tool-results/mcp-agent-ml-research-read_registry-1778891148151.txt


I'll spin up multiple agents in parallel to pull out different aspects of the experiment data from this registry file.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e870610b-266f-417d-9575-a32534df6ff7",
  "isSidechain": false,
  "requestId": "req_011Cb5JDvHaSWmtVxV8Sfi3F",
  "type": "assistant",
  "uuid": "c5ea9c6d-3aa4-4867-a32d-d25b023d7cbc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "sessionId": "38576691-e177-4a18-ab23-be69eff4b7ff",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NfCTntSvRiEYTZtBfRknq8",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8544,
      "cache_read_input_tokens": 24514,
      "output_tokens": 1952,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 8544,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1952,
          "cache_read_input_tokens": 24514,
          "cache_creation_input_tokens": 8544,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 8544
          },
          "type": "message"
        }
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

_source line 22 · 2026-05-16T00:25:56.824Z_

Registry is too large for direct reading. Launching parallel agents to extract each data dimension.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c5ea9c6d-3aa4-4867-a32d-d25b023d7cbc",
  "isSidechain": false,
  "requestId": "req_011Cb5JDvHaSWmtVxV8Sfi3F",
  "type": "assistant",
  "uuid": "42852419-1c1e-412c-935c-edac0aa0e866",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "sessionId": "38576691-e177-4a18-ab23-be69eff4b7ff",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NfCTntSvRiEYTZtBfRknq8",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8544,
      "cache_read_input_tokens": 24514,
      "output_tokens": 1952,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 8544,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1952,
          "cache_read_input_tokens": 24514,
          "cache_creation_input_tokens": 8544,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 8544
          },
          "type": "message"
        }
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

_source line 23 · 2026-05-16T00:26:04.372Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01HEFFWgTPf2hCW6r76uC5en`</summary>

```json
{
  "description": "Extract PPL dose curve data",
  "prompt": "Extract PPL dose curve experiments from the registry JSON file at:\n/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-11-projects-phase-gated-compound-sparse/38576691-e177-4a18-ab23-be69eff4b7ff/tool-results/mcp-agent-ml-research-read_registry-1778891148151.txt\n\nThe file is JSON with schema: {result: string} where result is a JSON string containing an array of experiments.\n\nI need ALL experiments related to PPL (perplexity) dose curves. These include experiments with IDs matching patterns like:\n- v6_* series (DeepSeek PPL)\n- bf16_* series (bf16 PPL)\n- Any experiment with \"ppl\" or \"PPL\" in the ID or description\n- n500 unified analysis experiments\n\nFor each experiment found, extract:\n1. exp_id\n2. status\n3. conclusion (if any)\n4. metrics (ALL metrics, especially: median_diff, median II, Wilcoxon p-value, effect_size/Cohen's d, sparsity level)\n5. Any notes about the experiment\n\nUse jq or python to parse. First probe the structure, then extract. Report ALL found experiments with their full metrics verbatim. Be thorough - don't miss any PPL-related experiment.",
  "run_in_background": true
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "42852419-1c1e-412c-935c-edac0aa0e866",
  "isSidechain": false,
  "requestId": "req_011Cb5JDvHaSWmtVxV8Sfi3F",
  "type": "assistant",
  "uuid": "b7178008-85e3-404f-8ba7-643a98f113fb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "sessionId": "38576691-e177-4a18-ab23-be69eff4b7ff",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NfCTntSvRiEYTZtBfRknq8",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8544,
      "cache_read_input_tokens": 24514,
      "output_tokens": 1952,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 8544,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1952,
          "cache_read_input_tokens": 24514,
          "cache_creation_input_tokens": 8544,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 8544
          },
          "type": "message"
        }
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

_source line 24 · 2026-05-16T00:26:20.034Z_

<details><summary>↩ Tool result · `toolu_012hWGjMJ6a2SV4Sbjb1yLkG`</summary>

```text
Async agent launched successfully.
agentId: a692d7d4f3f7a841e (internal ID - do not mention to user. Use SendMessage with to: 'a692d7d4f3f7a841e' to continue this agent.)
The agent is working in the background. You will be notified automatically when it completes.
Do not duplicate this agent's work — avoid working with the same files or topics it is using. Work on non-overlapping tasks, or briefly tell the user what you launched and end your response.
output_file: /tmp/claude-1000/-home-ubuntu--agent-ml-research-idea-gen-0509-11-projects-phase-gated-compound-sparse/38576691-e177-4a18-ab23-be69eff4b7ff/tasks/a692d7d4f3f7a841e.output
Do NOT Read or tail this file via the shell tool — it is the full sub-agent JSONL transcript and reading it will overflow your context. If the user asks for progress, say the agent is still running; you'll get a completion notification.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "18a7fe65-4877-4388-9822-26e9f7e494b0",
  "isSidechain": false,
  "promptId": "5d98afa4-bc8d-47c1-b014-8bbe0580361f",
  "type": "user",
  "uuid": "5f05060c-09dc-43d6-8bc3-d446f6c86fb4",
  "toolUseResult": {
    "isAsync": true,
    "status": "async_launched",
    "agentId": "a692d7d4f3f7a841e",
    "description": "Extract sf5 + misc evidence",
    "prompt": "Extract supplementary evidence experiments from the registry JSON file at:\n/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-11-projects-phase-gated-compound-sparse/38576691-e177-4a18-ab23-be69eff4b7ff/tool-results/mcp-agent-ml-research-read_registry-1778891148151.txt\n\nThe file is JSON with schema: {result: string} where result is a JSON string containing an array of experiments.\n\nI need experiments related to:\n\n1. **sf5 asymmetric sparsity** - any experiment with \"sf5\" or \"asymmetric\" in the ID\n2. **Appendix B G× correction** - any experiment with \"gx\" or \"G×\" or \"appendix\" in the ID or notes\n3. **Cross-model Mann-Whitney U** - any experiment with \"mann_whitney\" or \"n475\" or \"n500_v2\" or \"reanalysis\" in the ID\n4. **n500 unified analysis** - experiments with \"n500\" in the ID\n5. **c4_entropy** experiments (discrimination collapse mechanism)\n6. **c3_llama** experiments (cross-architecture)\n7. **c5b_pilot** experiments (phase-gated controller)\n\nFor each experiment, extract ALL fields verbatim:\n1. exp_id\n2. status\n3. conclusion\n4. metrics (ALL metrics)\n5. notes\n\nUse jq or python to parse. First probe the structure, then extract. Report everything verbatim - this is for a data compilation so completeness matters.",
    "outputFile": "/tmp/claude-1000/-home-ubuntu--agent-ml-research-idea-gen-0509-11-projects-phase-gated-compound-sparse/38576691-e177-4a18-ab23-be69eff4b7ff/tasks/a692d7d4f3f7a841e.output",
    "canReadOutputFile": true
  },
  "sourceToolAssistantUUID": "18a7fe65-4877-4388-9822-26e9f7e494b0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "sessionId": "38576691-e177-4a18-ab23-be69eff4b7ff",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-16T00:26:04.392Z_

<details><summary>↩ Tool result · `toolu_01HEFFWgTPf2hCW6r76uC5en`</summary>

```text
Async agent launched successfully.
agentId: a7fba12d105bf979c (internal ID - do not mention to user. Use SendMessage with to: 'a7fba12d105bf979c' to continue this agent.)
The agent is working in the background. You will be notified automatically when it completes.
Do not duplicate this agent's work — avoid working with the same files or topics it is using. Work on non-overlapping tasks, or briefly tell the user what you launched and end your response.
output_file: /tmp/claude-1000/-home-ubuntu--agent-ml-research-idea-gen-0509-11-projects-phase-gated-compound-sparse/38576691-e177-4a18-ab23-be69eff4b7ff/tasks/a7fba12d105bf979c.output
Do NOT Read or tail this file via the shell tool — it is the full sub-agent JSONL transcript and reading it will overflow your context. If the user asks for progress, say the agent is still running; you'll get a completion notification.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b7178008-85e3-404f-8ba7-643a98f113fb",
  "isSidechain": false,
  "promptId": "5d98afa4-bc8d-47c1-b014-8bbe0580361f",
  "type": "user",
  "uuid": "5ae8c9e3-a227-48b1-95e4-73e804a1df11",
  "toolUseResult": {
    "isAsync": true,
    "status": "async_launched",
    "agentId": "a7fba12d105bf979c",
    "description": "Extract PPL dose curve data",
    "prompt": "Extract PPL dose curve experiments from the registry JSON file at:\n/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-11-projects-phase-gated-compound-sparse/38576691-e177-4a18-ab23-be69eff4b7ff/tool-results/mcp-agent-ml-research-read_registry-1778891148151.txt\n\nThe file is JSON with schema: {result: string} where result is a JSON string containing an array of experiments.\n\nI need ALL experiments related to PPL (perplexity) dose curves. These include experiments with IDs matching patterns like:\n- v6_* series (DeepSeek PPL)\n- bf16_* series (bf16 PPL)\n- Any experiment with \"ppl\" or \"PPL\" in the ID or description\n- n500 unified analysis experiments\n\nFor each experiment found, extract:\n1. exp_id\n2. status\n3. conclusion (if any)\n4. metrics (ALL metrics, especially: median_diff, median II, Wilcoxon p-value, effect_size/Cohen's d, sparsity level)\n5. Any notes about the experiment\n\nUse jq or python to parse. First probe the structure, then extract. Report ALL found experiments with their full metrics verbatim. Be thorough - don't miss any PPL-related experiment.",
    "outputFile": "/tmp/claude-1000/-home-ubuntu--agent-ml-research-idea-gen-0509-11-projects-phase-gated-compound-sparse/38576691-e177-4a18-ab23-be69eff4b7ff/tasks/a7fba12d105bf979c.output",
    "canReadOutputFile": true
  },
  "sourceToolAssistantUUID": "b7178008-85e3-404f-8ba7-643a98f113fb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "sessionId": "38576691-e177-4a18-ab23-be69eff4b7ff",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-16T00:26:09.614Z_

<details open><summary>🔧 Tool call — Agent · `toolu_017fMgRDE2SGq81kAz4HckZT`</summary>

```json
{
  "description": "Extract QW accuracy data",
  "prompt": "Extract QW (Qwen) accuracy dose curve experiments from the registry JSON file at:\n/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-11-projects-phase-gated-compound-sparse/38576691-e177-4a18-ab23-be69eff4b7ff/tool-results/mcp-agent-ml-research-read_registry-1778891148151.txt\n\nThe file is JSON with schema: {result: string} where result is a JSON string containing an array of experiments.\n\nI need experiments with IDs matching:\n- acc_qw_dense_n100\n- acc_qw_s015_n100\n- acc_qw_s020_n100 (and _b2_fix variant)\n- acc_qw_s025_n100 (and _b2_fix variant)\n- acc_qw_s030_n100\n- Any other acc_qw_* experiments\n\nFor each experiment, extract ALL fields verbatim:\n1. exp_id\n2. status\n3. conclusion\n4. metrics (ALL - especially combined_accuracy, truncation_rate, correct counts, batch details)\n5. notes\n6. Any other relevant fields\n\nUse jq or python to parse. First probe the structure, then extract. Report everything verbatim - don't summarize away any metrics.",
  "run_in_background": true
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5ae8c9e3-a227-48b1-95e4-73e804a1df11",
  "isSidechain": false,
  "requestId": "req_011Cb5JDvHaSWmtVxV8Sfi3F",
  "type": "assistant",
  "uuid": "6e0bdafd-7466-43f1-be57-8059be3c991f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "sessionId": "38576691-e177-4a18-ab23-be69eff4b7ff",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NfCTntSvRiEYTZtBfRknq8",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8544,
      "cache_read_input_tokens": 24514,
      "output_tokens": 1952,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 8544,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1952,
          "cache_read_input_tokens": 24514,
          "cache_creation_input_tokens": 8544,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 8544
          },
          "type": "message"
        }
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

_source line 27 · 2026-05-16T00:26:09.621Z_

<details><summary>↩ Tool result · `toolu_017fMgRDE2SGq81kAz4HckZT`</summary>

```text
Async agent launched successfully.
agentId: a3e0a592254fabea7 (internal ID - do not mention to user. Use SendMessage with to: 'a3e0a592254fabea7' to continue this agent.)
The agent is working in the background. You will be notified automatically when it completes.
Do not duplicate this agent's work — avoid working with the same files or topics it is using. Work on non-overlapping tasks, or briefly tell the user what you launched and end your response.
output_file: /tmp/claude-1000/-home-ubuntu--agent-ml-research-idea-gen-0509-11-projects-phase-gated-compound-sparse/38576691-e177-4a18-ab23-be69eff4b7ff/tasks/a3e0a592254fabea7.output
Do NOT Read or tail this file via the shell tool — it is the full sub-agent JSONL transcript and reading it will overflow your context. If the user asks for progress, say the agent is still running; you'll get a completion notification.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6e0bdafd-7466-43f1-be57-8059be3c991f",
  "isSidechain": false,
  "promptId": "5d98afa4-bc8d-47c1-b014-8bbe0580361f",
  "type": "user",
  "uuid": "ac1a178a-cc20-4053-931d-575382866e3e",
  "toolUseResult": {
    "isAsync": true,
    "status": "async_launched",
    "agentId": "a3e0a592254fabea7",
    "description": "Extract QW accuracy data",
    "prompt": "Extract QW (Qwen) accuracy dose curve experiments from the registry JSON file at:\n/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-11-projects-phase-gated-compound-sparse/38576691-e177-4a18-ab23-be69eff4b7ff/tool-results/mcp-agent-ml-research-read_registry-1778891148151.txt\n\nThe file is JSON with schema: {result: string} where result is a JSON string containing an array of experiments.\n\nI need experiments with IDs matching:\n- acc_qw_dense_n100\n- acc_qw_s015_n100\n- acc_qw_s020_n100 (and _b2_fix variant)\n- acc_qw_s025_n100 (and _b2_fix variant)\n- acc_qw_s030_n100\n- Any other acc_qw_* experiments\n\nFor each experiment, extract ALL fields verbatim:\n1. exp_id\n2. status\n3. conclusion\n4. metrics (ALL - especially combined_accuracy, truncation_rate, correct counts, batch details)\n5. notes\n6. Any other relevant fields\n\nUse jq or python to parse. First probe the structure, then extract. Report everything verbatim - don't summarize away any metrics.",
    "outputFile": "/tmp/claude-1000/-home-ubuntu--agent-ml-research-idea-gen-0509-11-projects-phase-gated-compound-sparse/38576691-e177-4a18-ab23-be69eff4b7ff/tasks/a3e0a592254fabea7.output",
    "canReadOutputFile": true
  },
  "sourceToolAssistantUUID": "6e0bdafd-7466-43f1-be57-8059be3c991f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "sessionId": "38576691-e177-4a18-ab23-be69eff4b7ff",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-16T00:26:14.087Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01DR2EwefaamHZqL1RC2KtYD`</summary>

```json
{
  "description": "Extract DS accuracy + GSM8K data",
  "prompt": "Extract DS (DeepSeek) accuracy and GSM8K experiments from the registry JSON file at:\n/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-11-projects-phase-gated-compound-sparse/38576691-e177-4a18-ab23-be69eff4b7ff/tool-results/mcp-agent-ml-research-read_registry-1778891148151.txt\n\nThe file is JSON with schema: {result: string} where result is a JSON string containing an array of experiments.\n\nI need TWO sets of experiments:\n\n**SET 1: DS Accuracy (8k v2)**\n- acc_ds_dense_8k_v2\n- acc_ds_s015_8k_v2\n- acc_ds_s020_8k_v2\n- acc_ds_s025_8k_v2\n- acc_ds_s030_8k_v2\n- Any other acc_ds_* experiments\n\n**SET 2: GSM8K Compound Interaction**\n- gsm8k_qw_rand_s025_v2\n- gsm8k_qw_rand_s030_v2\n- Any other gsm8k_* experiments\n\nFor each experiment, extract ALL fields verbatim:\n1. exp_id\n2. status\n3. conclusion\n4. metrics (ALL metrics)\n5. notes\n6. Any other relevant fields\n\nUse jq or python to parse. First probe the structure, then extract. Report everything verbatim.",
  "run_in_background": true
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ac1a178a-cc20-4053-931d-575382866e3e",
  "isSidechain": false,
  "requestId": "req_011Cb5JDvHaSWmtVxV8Sfi3F",
  "type": "assistant",
  "uuid": "6c9b957b-20f0-4913-a111-1f7020634aab",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "sessionId": "38576691-e177-4a18-ab23-be69eff4b7ff",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NfCTntSvRiEYTZtBfRknq8",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8544,
      "cache_read_input_tokens": 24514,
      "output_tokens": 1952,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 8544,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1952,
          "cache_read_input_tokens": 24514,
          "cache_creation_input_tokens": 8544,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 8544
          },
          "type": "message"
        }
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

_source line 29 · 2026-05-16T00:26:14.096Z_

<details><summary>↩ Tool result · `toolu_01DR2EwefaamHZqL1RC2KtYD`</summary>

```text
Async agent launched successfully.
agentId: a09137f4d041cbaa5 (internal ID - do not mention to user. Use SendMessage with to: 'a09137f4d041cbaa5' to continue this agent.)
The agent is working in the background. You will be notified automatically when it completes.
Do not duplicate this agent's work — avoid working with the same files or topics it is using. Work on non-overlapping tasks, or briefly tell the user what you launched and end your response.
output_file: /tmp/claude-1000/-home-ubuntu--agent-ml-research-idea-gen-0509-11-projects-phase-gated-compound-sparse/38576691-e177-4a18-ab23-be69eff4b7ff/tasks/a09137f4d041cbaa5.output
Do NOT Read or tail this file via the shell tool — it is the full sub-agent JSONL transcript and reading it will overflow your context. If the user asks for progress, say the agent is still running; you'll get a completion notification.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6c9b957b-20f0-4913-a111-1f7020634aab",
  "isSidechain": false,
  "promptId": "5d98afa4-bc8d-47c1-b014-8bbe0580361f",
  "type": "user",
  "uuid": "c7a0beca-f073-47ee-9927-3e03460da736",
  "toolUseResult": {
    "isAsync": true,
    "status": "async_launched",
    "agentId": "a09137f4d041cbaa5",
    "description": "Extract DS accuracy + GSM8K data",
    "prompt": "Extract DS (DeepSeek) accuracy and GSM8K experiments from the registry JSON file at:\n/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-11-projects-phase-gated-compound-sparse/38576691-e177-4a18-ab23-be69eff4b7ff/tool-results/mcp-agent-ml-research-read_registry-1778891148151.txt\n\nThe file is JSON with schema: {result: string} where result is a JSON string containing an array of experiments.\n\nI need TWO sets of experiments:\n\n**SET 1: DS Accuracy (8k v2)**\n- acc_ds_dense_8k_v2\n- acc_ds_s015_8k_v2\n- acc_ds_s020_8k_v2\n- acc_ds_s025_8k_v2\n- acc_ds_s030_8k_v2\n- Any other acc_ds_* experiments\n\n**SET 2: GSM8K Compound Interaction**\n- gsm8k_qw_rand_s025_v2\n- gsm8k_qw_rand_s030_v2\n- Any other gsm8k_* experiments\n\nFor each experiment, extract ALL fields verbatim:\n1. exp_id\n2. status\n3. conclusion\n4. metrics (ALL metrics)\n5. notes\n6. Any other relevant fields\n\nUse jq or python to parse. First probe the structure, then extract. Report everything verbatim.",
    "outputFile": "/tmp/claude-1000/-home-ubuntu--agent-ml-research-idea-gen-0509-11-projects-phase-gated-compound-sparse/38576691-e177-4a18-ab23-be69eff4b7ff/tasks/a09137f4d041cbaa5.output",
    "canReadOutputFile": true
  },
  "sourceToolAssistantUUID": "6c9b957b-20f0-4913-a111-1f7020634aab",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "sessionId": "38576691-e177-4a18-ab23-be69eff4b7ff",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 30 · 2026-05-16T00:26:20.026Z_

<details open><summary>🔧 Tool call — Agent · `toolu_012hWGjMJ6a2SV4Sbjb1yLkG`</summary>

```json
{
  "description": "Extract sf5 + misc evidence",
  "prompt": "Extract supplementary evidence experiments from the registry JSON file at:\n/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-11-projects-phase-gated-compound-sparse/38576691-e177-4a18-ab23-be69eff4b7ff/tool-results/mcp-agent-ml-research-read_registry-1778891148151.txt\n\nThe file is JSON with schema: {result: string} where result is a JSON string containing an array of experiments.\n\nI need experiments related to:\n\n1. **sf5 asymmetric sparsity** - any experiment with \"sf5\" or \"asymmetric\" in the ID\n2. **Appendix B G× correction** - any experiment with \"gx\" or \"G×\" or \"appendix\" in the ID or notes\n3. **Cross-model Mann-Whitney U** - any experiment with \"mann_whitney\" or \"n475\" or \"n500_v2\" or \"reanalysis\" in the ID\n4. **n500 unified analysis** - experiments with \"n500\" in the ID\n5. **c4_entropy** experiments (discrimination collapse mechanism)\n6. **c3_llama** experiments (cross-architecture)\n7. **c5b_pilot** experiments (phase-gated controller)\n\nFor each experiment, extract ALL fields verbatim:\n1. exp_id\n2. status\n3. conclusion\n4. metrics (ALL metrics)\n5. notes\n\nUse jq or python to parse. First probe the structure, then extract. Report everything verbatim - this is for a data compilation so completeness matters.",
  "run_in_background": true
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c7a0beca-f073-47ee-9927-3e03460da736",
  "isSidechain": false,
  "requestId": "req_011Cb5JDvHaSWmtVxV8Sfi3F",
  "type": "assistant",
  "uuid": "18a7fe65-4877-4388-9822-26e9f7e494b0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "sessionId": "38576691-e177-4a18-ab23-be69eff4b7ff",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NfCTntSvRiEYTZtBfRknq8",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8544,
      "cache_read_input_tokens": 24514,
      "output_tokens": 1952,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 8544,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1952,
          "cache_read_input_tokens": 24514,
          "cache_creation_input_tokens": 8544,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 8544
          },
          "type": "message"
        }
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

_source line 31 · 2026-05-16T00:26:20.051Z_

```json
{
  "parentUuid": "5f05060c-09dc-43d6-8bc3-d446f6c86fb4",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "6eeb557e-e94c-4e6c-b790-9eb2106013b1",
  "timestamp": "2026-05-16T00:26:20.051Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "sessionId": "38576691-e177-4a18-ab23-be69eff4b7ff",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 32 · 2026-05-16T00:26:22.247Z_

4 agents are extracting data from the registry in parallel. Waiting for results.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6eeb557e-e94c-4e6c-b790-9eb2106013b1",
  "isSidechain": false,
  "requestId": "req_011Cb5JGF5Ei3tss1HKf7snQ",
  "type": "assistant",
  "uuid": "e8326a4d-530b-4458-9899-ecce1e91e36c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "sessionId": "38576691-e177-4a18-ab23-be69eff4b7ff",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TNxBu45NaiCFTYNhF7Ei6u",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 3169,
      "cache_read_input_tokens": 33058,
      "output_tokens": 22,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3169,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 22,
          "cache_read_input_tokens": 33058,
          "cache_creation_input_tokens": 3169,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3169
          },
          "type": "message"
        }
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

_source line 33 · 2026-05-16T00:27:11.885Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-16T00:27:11.885Z",
  "sessionId": "38576691-e177-4a18-ab23-be69eff4b7ff",
  "content": "&lt;task-notification>\n&lt;task-id>a3e0a592254fabea7&lt;/task-id>\n&lt;tool-use-id>toolu_017fMgRDE2SGq81kAz4HckZT&lt;/tool-use-id>\n&lt;output-file>/tmp/claude-1000/-home-ubuntu--agent-ml-research-idea-gen-0509-11-projects-phase-gated-compound-sparse/38576691-e177-4a18-ab23-be69eff4b7ff/tasks/a3e0a592254fabea7.output&lt;/output-file>\n&lt;status>completed&lt;/status>\n&lt;summary>Agent \"Extract QW accuracy data\" completed&lt;/summary>\n&lt;result>Here are all 9 `acc_qw_*` experiments extracted verbatim from the registry.\n\n---\n\n## Summary Table (9 experiments)\n\n| exp_id | status | conclusion | combined_acc | combined_correct/total |\n|--------|--------|-----------|-------------|----------------------|\n| acc_qw_dense_n100 | DONE | success | 0.40 | 40/100 |\n| acc_qw_s015_n100 | DONE | success | 0.36 | 36/100 |\n| acc_qw_s020 | DONE | negative | 0.26 (n=50 only) | 13/50 |\n| acc_qw_s020_n100 | DONE | success | 0.35 | 35/100 |\n| acc_qw_s020_n100_b2_fix | DONE | success | 0.36 | 36/100 |\n| acc_qw_s025 | DONE | negative | 0.32 (n=50 only) | 16/50 |\n| acc_qw_s025_n100 | DONE | success | 0.33 | 33/100 |\n| acc_qw_s025_n100_b2_fix | DONE | success | 0.33 | 33/100 |\n| acc_qw_s030_n100 | DONE | success | 0.19 | 19/100 |\n\n---\n\n## Full Verbatim Details Per Experiment\n\n### 1. acc_qw_dense_n100\n- **status**: DONE\n- **conclusion**: success\n- **hypothesis**: \"补跑 QW dense problems 51-100，扩展到 n=100 以降低噪声\"\n- **metrics**:\n  - batch1_correct: 16, batch1_total: 50, batch1_acc: 0.32\n  - batch2_correct: 24, batch2_total: 50, batch2_acc: 0.48\n  - combined_correct: 40, combined_total: 100, combined_acc: **0.40**\n- **spec**: model=Qwen2.5-7B-Instruct, conditions=dense, problems 51-100, seed=42, server=westd-22162, gpu=cuda:2, wall_clock_seconds=1176.6, gpu_hours=0.33\n- **completed_at**: 2026-05-15T21:54:42.068Z\n\n### 2. acc_qw_s015_n100\n- **status**: DONE\n- **conclusion**: success\n- **metrics**:\n  - batch1_acc: 0.34, batch1_correct: 17, batch1_total: 50\n  - batch2_acc: 0.38, batch2_correct: 19, batch2_total: 50\n  - combined_acc: **0.36**, combined_correct: 36, combined_total: 100\n- **spec**: model=Qwen2.5-7B-Instruct, conditions=importance_s015, problems 51-100, seed=42, server=westd-22162, gpu=cuda:3\n- **checkpoint_path**: N/A (eval only)\n- **log_path**: /root/autodl-tmp/pacs/analysis_output/accuracy_eval_qw_s015_n51_100.json\n- **completed_at**: 2026-05-15T21:47:46.664Z\n\n### 3. acc_qw_s020 (batch 1 only, n=50)\n- **status**: DONE\n- **conclusion**: negative\n- **metrics**:\n  - qw_s020_acc: 0.26, qw_s020_correct: 13, qw_s020_total: 50\n  - qw_s020_delta_vs_dense: -0.06\n  - null_count: 2, null_rate: 0.04\n  - output_truncated_count: 2, output_truncated_rate: 0.04\n  - extraction_failure_count: 0, extraction_failure_rate: 0\n  - wrong_count: 35, wrong_rate: 0.70\n  - heads_pruned: 140\n  - total_time_s: 598\n  - note: \"v2 rescored with fixed radical+degree matcher\"\n- **spec**: model=Qwen2.5-7B-Instruct, conditions=importance_s020, n=50, server=westd-22162, gpu=cuda:2, wall_clock_seconds=878.3, gpu_hours=0.24\n- **checkpoint_path**: /root/autodl-tmp/pacs/analysis_output/accuracy_eval_qw_s020.json\n- **completed_at**: 2026-05-15T21:04:41.944Z\n\n### 4. acc_qw_s020_n100\n- **status**: DONE\n- **conclusion**: success\n- **metrics**:\n  - batch1_acc: 0.26, batch1_correct: 13, batch1_total: 50\n  - batch2_acc: 0.44, batch2_correct: 22, batch2_total: 50\n  - combined_acc: **0.35**, combined_correct: 35, combined_total: 100\n- **spec**: model=Qwen2.5-7B-Instruct, conditions=importance_s020, problems 51-100, seed=42, server=westd-22162\n- **completed_at**: 2026-05-15T21:30:07.934Z\n\n### 5. acc_qw_s020_n100_b2_fix\n- **status**: DONE\n- **conclusion**: success\n- **hypothesis**: \"重跑 QW s020 batch2 (problems 51-100) with max_new_tokens=8192，修复原 batch2 使用 2048 的不一致问题。\"\n- **parent**: acc_qw_s020_n100\n- **metrics**:\n  - batch2_correct: 23, batch2_total: 50, batch2_acc: 0.46\n  - batch1_correct_v2: 13, batch1_total: 50, batch1_acc_v2: 0.26\n  - combined_correct: 36, combined_total: 100, combined_acc: **0.36**\n  - null_count: 2, truncated_count: 1\n  - total_time_seconds: 884.3\n  - max_new_tokens: 8192\n  - original_batch2_correct: 22, original_batch2_acc: 0.44\n  - delta_vs_original: \"+1 correct (+0.02 acc)\"\n- **reproduce**: code_commit=1b4f61aa366a9fe320f8563c8f7acb5af58d78b7, finished_at=2026-05-15T22:40:53.877Z, training_hours=0.26\n- **spec**: server=westd-22162, gpu=cuda:1, wall_clock_seconds=1400.7, gpu_hours=0.39\n- **completed_at**: 2026-05-15T22:48:39.196Z\n\n### 6. acc_qw_s025 (batch 1 only, n=50)\n- **status**: DONE\n- **conclusion**: negative\n- **metrics**:\n  - qw_s025_acc: 0.32, qw_s025_correct: 16, qw_s025_total: 50\n  - qw_s025_delta_vs_dense: 0\n  - null_count: 8, null_rate: 0.16\n  - output_truncated_count: 2, output_truncated_rate: 0.04\n  - extraction_failure_count: 6, extraction_failure_rate: 0.12\n  - wrong_count: 26, wrong_rate: 0.52\n  - heads_pruned: 196\n  - total_time_s: 559\n  - note: \"v2 rescored with fixed radical+degree matcher; 3 problems flipped (sqrt+degree)\"\n- **spec**: model=Qwen2.5-7B-Instruct, conditions=importance_s025, n=50, server=westd-22162, gpu=cuda:3, wall_clock_seconds=875.0, gpu_hours=0.24\n- **checkpoint_path**: /root/autodl-tmp/pacs/analysis_output/accuracy_eval_qw_s025.json\n- **completed_at**: 2026-05-15T21:04:40.391Z\n\n### 7. acc_qw_s025_n100\n- **status**: DONE\n- **conclusion**: success\n- **metrics**:\n  - batch1_acc: 0.32, batch1_correct: 16, batch1_total: 50\n  - batch2_acc: 0.34, batch2_correct: 17, batch2_total: 50\n  - combined_acc: **0.33**, combined_correct: 33, combined_total: 100\n- **spec**: model=Qwen2.5-7B-Instruct, conditions=importance_s025, problems 51-100, seed=42, server=westd-22162\n- **completed_at**: 2026-05-15T21:30:09.145Z\n\n### 8. acc_qw_s025_n100_b2_fix\n- **status**: DONE\n- **conclusion**: success\n- **hypothesis**: \"重跑 QW s025 batch2 (problems 51-100) with max_new_tokens=8192，修复原 batch2 使用 2048 的不一致问题。\"\n- **parent**: acc_qw_s025_n100\n- **metrics**:\n  - accuracy: 0.34, correct: 17, n_problems: 50\n  - truncation_rate: 0.06, truncated_count: 3\n  - avg_tokens: 1044\n  - max_new_tokens: 8192\n  - total_time_seconds: 1099\n  - batch: \"b2 (problems 51-100)\"\n  - merged_n100_accuracy: **0.33**, merged_n100_correct: 33\n  - merged_n100_note: \"batch1 used max_new_tokens=2048, batch2_fix used 8192 — mismatch\"\n- **reproduce**: code_commit=1b4f61aa366a9fe320f8563c8f7acb5af58d78b7, finished_at=2026-05-15T23:02:06.320Z, training_hours=0.31\n- **checkpoint_path**: /root/autodl-tmp/pacs/analysis_output/accuracy_eval_qw_s025_b2_fix.json\n- **completed_at**: 2026-05-15T23:28:18.012Z\n\n### 9. acc_qw_s030_n100\n- **status**: DONE\n- **conclusion**: success\n- **hypothesis**: \"补跑 QW importance_s030 problems 51-100，扩展到 n=100 以降低噪声\"\n- **metrics**:\n  - batch1_correct: 7, batch1_total: 50, batch1_acc: 0.14\n  - batch2_correct: 12, batch2_total: 50, batch2_acc: 0.24\n  - combined_correct: 19, combined_total: 100, combined_acc: **0.19**\n- **spec**: model=Qwen2.5-7B-Instruct, conditions=importance_s030, problems 51-100, seed=42, server=westd-22162, gpu=cuda:3, wall_clock_seconds=2001.6, gpu_hours=0.56\n- **completed_at**: 2026-05-15T22:21:11.181Z\n\n---\n\n## QW Dose Curve (best n=100 estimates, using b2_fix where available)\n\n| Sparsity | combined_acc (n=100) | Correct/100 | Delta vs Dense |\n|----------|---------------------|-------------|----------------|\n| dense    | 0.40                | 40          | --             |\n| s015     | 0.36                | 36          | -0.04          |\n| s020     | 0.36 (b2_fix)       | 36          | -0.04          |\n| s025     | 0.33 (b2_fix=same)  | 33          | -0.07          |\n| s030     | 0.19                | 19          | -0.21          |\n\nKey observation: s025-&gt;s030 shows a steep accuracy cliff (0.33 -&gt; 0.19, a 14-point drop), while s015 and s020 are close to dense. The b2_fix variants (max_new_tokens=8192) had minimal impact on s020 (+1 correct) and zero impact on s025 (still 33 correct). Note the b2_fix experiments flag a mismatch: batch1 used max_new_tokens=2048 while batch2_fix used 8192.&lt;/result>\n&lt;usage>&lt;total_tokens>23348&lt;/total_tokens>&lt;tool_uses>5&lt;/tool_uses>&lt;duration_ms>62268&lt;/duration_ms>&lt;/usage>\n&lt;/task-notification>"
}
```

---

### Runtime record

_source line 34 · 2026-05-16T00:27:11.960Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-16T00:27:11.960Z",
  "sessionId": "38576691-e177-4a18-ab23-be69eff4b7ff"
}
```

---

### Runtime record

_source line 35_

```json
{
  "type": "last-prompt",
  "leafUuid": "e8326a4d-530b-4458-9899-ecce1e91e36c",
  "sessionId": "38576691-e177-4a18-ab23-be69eff4b7ff"
}
```

---

### Runtime record

_source line 36_

```json
{
  "type": "ai-title",
  "aiTitle": "Compile Round 10 experiment evidence for ARR submission",
  "sessionId": "38576691-e177-4a18-ab23-be69eff4b7ff"
}
```

---

## Round 2

4 recorded events

### User

_source line 37 · 2026-05-16T00:27:12.349Z_

&lt;task-notification>
&lt;task-id>a3e0a592254fabea7&lt;/task-id>
&lt;tool-use-id>toolu_017fMgRDE2SGq81kAz4HckZT&lt;/tool-use-id>
&lt;output-file>/tmp/claude-1000/-home-ubuntu--agent-ml-research-idea-gen-0509-11-projects-phase-gated-compound-sparse/38576691-e177-4a18-ab23-be69eff4b7ff/tasks/a3e0a592254fabea7.output&lt;/output-file>
&lt;status>completed&lt;/status>
&lt;summary>Agent "Extract QW accuracy data" completed&lt;/summary>
&lt;result>Here are all 9 `acc_qw_*` experiments extracted verbatim from the registry.

---

## Summary Table (9 experiments)

| exp_id | status | conclusion | combined_acc | combined_correct/total |
|--------|--------|-----------|-------------|----------------------|
| acc_qw_dense_n100 | DONE | success | 0.40 | 40/100 |
| acc_qw_s015_n100 | DONE | success | 0.36 | 36/100 |
| acc_qw_s020 | DONE | negative | 0.26 (n=50 only) | 13/50 |
| acc_qw_s020_n100 | DONE | success | 0.35 | 35/100 |
| acc_qw_s020_n100_b2_fix | DONE | success | 0.36 | 36/100 |
| acc_qw_s025 | DONE | negative | 0.32 (n=50 only) | 16/50 |
| acc_qw_s025_n100 | DONE | success | 0.33 | 33/100 |
| acc_qw_s025_n100_b2_fix | DONE | success | 0.33 | 33/100 |
| acc_qw_s030_n100 | DONE | success | 0.19 | 19/100 |

---

## Full Verbatim Details Per Experiment

### 1. acc_qw_dense_n100
- **status**: DONE
- **conclusion**: success
- **hypothesis**: "补跑 QW dense problems 51-100，扩展到 n=100 以降低噪声"
- **metrics**:
  - batch1_correct: 16, batch1_total: 50, batch1_acc: 0.32
  - batch2_correct: 24, batch2_total: 50, batch2_acc: 0.48
  - combined_correct: 40, combined_total: 100, combined_acc: **0.40**
- **spec**: model=Qwen2.5-7B-Instruct, conditions=dense, problems 51-100, seed=42, server=westd-22162, gpu=cuda:2, wall_clock_seconds=1176.6, gpu_hours=0.33
- **completed_at**: 2026-05-15T21:54:42.068Z

### 2. acc_qw_s015_n100
- **status**: DONE
- **conclusion**: success
- **metrics**:
  - batch1_acc: 0.34, batch1_correct: 17, batch1_total: 50
  - batch2_acc: 0.38, batch2_correct: 19, batch2_total: 50
  - combined_acc: **0.36**, combined_correct: 36, combined_total: 100
- **spec**: model=Qwen2.5-7B-Instruct, conditions=importance_s015, problems 51-100, seed=42, server=westd-22162, gpu=cuda:3
- **checkpoint_path**: N/A (eval only)
- **log_path**: /root/autodl-tmp/pacs/analysis_output/accuracy_eval_qw_s015_n51_100.json
- **completed_at**: 2026-05-15T21:47:46.664Z

### 3. acc_qw_s020 (batch 1 only, n=50)
- **status**: DONE
- **conclusion**: negative
- **metrics**:
  - qw_s020_acc: 0.26, qw_s020_correct: 13, qw_s020_total: 50
  - qw_s020_delta_vs_dense: -0.06
  - null_count: 2, null_rate: 0.04
  - output_truncated_count: 2, output_truncated_rate: 0.04
  - extraction_failure_count: 0, extraction_failure_rate: 0
  - wrong_count: 35, wrong_rate: 0.70
  - heads_pruned: 140
  - total_time_s: 598
  - note: "v2 rescored with fixed radical+degree matcher"
- **spec**: model=Qwen2.5-7B-Instruct, conditions=importance_s020, n=50, server=westd-22162, gpu=cuda:2, wall_clock_seconds=878.3, gpu_hours=0.24
- **checkpoint_path**: /root/autodl-tmp/pacs/analysis_output/accuracy_eval_qw_s020.json
- **completed_at**: 2026-05-15T21:04:41.944Z

### 4. acc_qw_s020_n100
- **status**: DONE
- **conclusion**: success
- **metrics**:
  - batch1_acc: 0.26, batch1_correct: 13, batch1_total: 50
  - batch2_acc: 0.44, batch2_correct: 22, batch2_total: 50
  - combined_acc: **0.35**, combined_correct: 35, combined_total: 100
- **spec**: model=Qwen2.5-7B-Instruct, conditions=importance_s020, problems 51-100, seed=42, server=westd-22162
- **completed_at**: 2026-05-15T21:30:07.934Z

### 5. acc_qw_s020_n100_b2_fix
- **status**: DONE
- **conclusion**: success
- **hypothesis**: "重跑 QW s020 batch2 (problems 51-100) with max_new_tokens=8192，修复原 batch2 使用 2048 的不一致问题。"
- **parent**: acc_qw_s020_n100
- **metrics**:
  - batch2_correct: 23, batch2_total: 50, batch2_acc: 0.46
  - batch1_correct_v2: 13, batch1_total: 50, batch1_acc_v2: 0.26
  - combined_correct: 36, combined_total: 100, combined_acc: **0.36**
  - null_count: 2, truncated_count: 1
  - total_time_seconds: 884.3
  - max_new_tokens: 8192
  - original_batch2_correct: 22, original_batch2_acc: 0.44
  - delta_vs_original: "+1 correct (+0.02 acc)"
- **reproduce**: code_commit=1b4f61aa366a9fe320f8563c8f7acb5af58d78b7, finished_at=2026-05-15T22:40:53.877Z, training_hours=0.26
- **spec**: server=westd-22162, gpu=cuda:1, wall_clock_seconds=1400.7, gpu_hours=0.39
- **completed_at**: 2026-05-15T22:48:39.196Z

### 6. acc_qw_s025 (batch 1 only, n=50)
- **status**: DONE
- **conclusion**: negative
- **metrics**:
  - qw_s025_acc: 0.32, qw_s025_correct: 16, qw_s025_total: 50
  - qw_s025_delta_vs_dense: 0
  - null_count: 8, null_rate: 0.16
  - output_truncated_count: 2, output_truncated_rate: 0.04
  - extraction_failure_count: 6, extraction_failure_rate: 0.12
  - wrong_count: 26, wrong_rate: 0.52
  - heads_pruned: 196
  - total_time_s: 559
  - note: "v2 rescored with fixed radical+degree matcher; 3 problems flipped (sqrt+degree)"
- **spec**: model=Qwen2.5-7B-Instruct, conditions=importance_s025, n=50, server=westd-22162, gpu=cuda:3, wall_clock_seconds=875.0, gpu_hours=0.24
- **checkpoint_path**: /root/autodl-tmp/pacs/analysis_output/accuracy_eval_qw_s025.json
- **completed_at**: 2026-05-15T21:04:40.391Z

### 7. acc_qw_s025_n100
- **status**: DONE
- **conclusion**: success
- **metrics**:
  - batch1_acc: 0.32, batch1_correct: 16, batch1_total: 50
  - batch2_acc: 0.34, batch2_correct: 17, batch2_total: 50
  - combined_acc: **0.33**, combined_correct: 33, combined_total: 100
- **spec**: model=Qwen2.5-7B-Instruct, conditions=importance_s025, problems 51-100, seed=42, server=westd-22162
- **completed_at**: 2026-05-15T21:30:09.145Z

### 8. acc_qw_s025_n100_b2_fix
- **status**: DONE
- **conclusion**: success
- **hypothesis**: "重跑 QW s025 batch2 (problems 51-100) with max_new_tokens=8192，修复原 batch2 使用 2048 的不一致问题。"
- **parent**: acc_qw_s025_n100
- **metrics**:
  - accuracy: 0.34, correct: 17, n_problems: 50
  - truncation_rate: 0.06, truncated_count: 3
  - avg_tokens: 1044
  - max_new_tokens: 8192
  - total_time_seconds: 1099
  - batch: "b2 (problems 51-100)"
  - merged_n100_accuracy: **0.33**, merged_n100_correct: 33
  - merged_n100_note: "batch1 used max_new_tokens=2048, batch2_fix used 8192 — mismatch"
- **reproduce**: code_commit=1b4f61aa366a9fe320f8563c8f7acb5af58d78b7, finished_at=2026-05-15T23:02:06.320Z, training_hours=0.31
- **checkpoint_path**: /root/autodl-tmp/pacs/analysis_output/accuracy_eval_qw_s025_b2_fix.json
- **completed_at**: 2026-05-15T23:28:18.012Z

### 9. acc_qw_s030_n100
- **status**: DONE
- **conclusion**: success
- **hypothesis**: "补跑 QW importance_s030 problems 51-100，扩展到 n=100 以降低噪声"
- **metrics**:
  - batch1_correct: 7, batch1_total: 50, batch1_acc: 0.14
  - batch2_correct: 12, batch2_total: 50, batch2_acc: 0.24
  - combined_correct: 19, combined_total: 100, combined_acc: **0.19**
- **spec**: model=Qwen2.5-7B-Instruct, conditions=importance_s030, problems 51-100, seed=42, server=westd-22162, gpu=cuda:3, wall_clock_seconds=2001.6, gpu_hours=0.56
- **completed_at**: 2026-05-15T22:21:11.181Z

---

## QW Dose Curve (best n=100 estimates, using b2_fix where available)

| Sparsity | combined_acc (n=100) | Correct/100 | Delta vs Dense |
|----------|---------------------|-------------|----------------|
| dense    | 0.40                | 40          | --             |
| s015     | 0.36                | 36          | -0.04          |
| s020     | 0.36 (b2_fix)       | 36          | -0.04          |
| s025     | 0.33 (b2_fix=same)  | 33          | -0.07          |
| s030     | 0.19                | 19          | -0.21          |

Key observation: s025-&gt;s030 shows a steep accuracy cliff (0.33 -&gt; 0.19, a 14-point drop), while s015 and s020 are close to dense. The b2_fix variants (max_new_tokens=8192) had minimal impact on s020 (+1 correct) and zero impact on s025 (still 33 correct). Note the b2_fix experiments flag a mismatch: batch1 used max_new_tokens=2048 while batch2_fix used 8192.&lt;/result>
&lt;usage>&lt;total_tokens>23348&lt;/total_tokens>&lt;tool_uses>5&lt;/tool_uses>&lt;duration_ms>62268&lt;/duration_ms>&lt;/usage>
&lt;/task-notification>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e8326a4d-530b-4458-9899-ecce1e91e36c",
  "isSidechain": false,
  "promptId": "2a002526-0465-4655-a32f-161d0873023b",
  "type": "user",
  "uuid": "a40bde06-5631-48b5-9630-23c4a7786ec7",
  "permissionMode": "bypassPermissions",
  "origin": {
    "kind": "task-notification"
  },
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "sessionId": "38576691-e177-4a18-ab23-be69eff4b7ff",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 38 · 2026-05-16T00:27:14.402Z_

QW accuracy data received. Waiting for the other 3 agents.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a40bde06-5631-48b5-9630-23c4a7786ec7",
  "isSidechain": false,
  "requestId": "req_011Cb5JL6qzdDmFEqKXSuQNA",
  "type": "assistant",
  "uuid": "f4e7d630-8948-43c0-bd03-c6a978455f1f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "sessionId": "38576691-e177-4a18-ab23-be69eff4b7ff",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01H93sW979HyvCTRH82VnERM",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 3510,
      "cache_read_input_tokens": 36227,
      "output_tokens": 19,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3510,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 19,
          "cache_read_input_tokens": 36227,
          "cache_creation_input_tokens": 3510,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3510
          },
          "type": "message"
        }
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

_source line 39 · 2026-05-16T00:28:13.500Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-16T00:28:13.500Z",
  "sessionId": "38576691-e177-4a18-ab23-be69eff4b7ff",
  "content": "&lt;task-notification>\n&lt;task-id>a09137f4d041cbaa5&lt;/task-id>\n&lt;tool-use-id>toolu_01DR2EwefaamHZqL1RC2KtYD&lt;/tool-use-id>\n&lt;output-file>/tmp/claude-1000/-home-ubuntu--agent-ml-research-idea-gen-0509-11-projects-phase-gated-compound-sparse/38576691-e177-4a18-ab23-be69eff4b7ff/tasks/a09137f4d041cbaa5.output&lt;/output-file>\n&lt;status>completed&lt;/status>\n&lt;summary>Agent \"Extract DS accuracy + GSM8K data\" completed&lt;/summary>\n&lt;result>Here is the complete verbatim extraction of both experiment sets.\n\n---\n\n## SET 1: All `acc_ds_*` Experiments (12 experiments)\n\n### acc_ds_dense_8k\n- **status**: DONE\n- **conclusion**: killed\n- **hypothesis**: \"8192 token budget 下 DS dense baseline 截断率应降至 &lt;20%，accuracy 应高于 4096 版本的 0.52\"\n- **metrics**: (none recorded -- killed before completion)\n- **spec**: server=westd-22162, gpu=cuda:0, pid=277990, wall_clock_seconds=129.7, gpu_hours=0.04\n- **completed_at**: 2026-05-15T21:28:57.693Z\n\n### acc_ds_dense_8k_v2\n- **status**: DONE\n- **conclusion**: success\n- **hypothesis**: \"DS dense 8k 重跑：原 acc_ds_dense_8k 进程被 kill 后输出丢失，需重跑获取完整 dense baseline accuracy (max_new_tokens=8192)。\"\n- **metrics**:\n  - accuracy: **0.74**\n  - correct: 37\n  - n_problems: 50\n  - truncation_rate: 0.16\n  - truncated_count: 8\n  - avg_tokens: 3126\n  - max_new_tokens: 8192\n  - total_time_seconds: 2882\n- **checkpoint_path**: /root/autodl-tmp/pacs/analysis_output/accuracy_ds_dense_8k_v2.json\n- **completed_at**: 2026-05-15T23:28:12.650Z\n\n### acc_ds_s015_8k\n- **status**: DONE\n- **conclusion**: killed\n- **hypothesis**: \"8192 token budget 下 DS s015 截断率应降至 &lt;20%，accuracy 应高于 4096 版本的 0.36\"\n- **metrics**: (none -- killed)\n- **completed_at**: 2026-05-15T21:28:48.029Z\n\n### acc_ds_s015_8k_v2\n- **status**: RUNNING\n- **conclusion**: (not yet concluded)\n- **hypothesis**: \"DS s015 accuracy eval with max_new_tokens=8192，验证 dense→s015 是否存在断崖式下降（v1 暗示 0.74→~0.36）。\"\n- **metrics**: (none yet -- still running)\n- **server**: westd-22162, gpu=cuda:0\n\n### acc_ds_s020\n- **status**: DONE\n- **conclusion**: negative\n- **metrics**:\n  - ds_s020_acc: **0.26**\n  - ds_s020_acc_v2: 0.26\n  - ds_s020_correct: 13\n  - ds_s020_total: 50\n  - ds_s020_delta_vs_dense: -0.26\n  - output_truncated_count: 32\n  - output_truncated_rate: 0.64\n  - extraction_failure_count: 31\n  - extraction_failure_rate: 0.62\n  - total_time_s: 1560\n  - note: \"v2 rescored with fixed radical+degree matcher; 0 changes. Dense baseline=0.52\"\n- **checkpoint_path**: /root/autodl-tmp/pacs/analysis_output/accuracy_eval_ds_s020.json\n- **completed_at**: 2026-05-15T21:20:03.642Z\n\n### acc_ds_s020_8k\n- **status**: DONE\n- **conclusion**: killed\n- **hypothesis**: \"8192 token budget 下 DS s020 截断率应从 64% 降至 &lt;20%，accuracy 应高于 4096 版本的 0.26\"\n- **metrics**: (none -- killed)\n\n### acc_ds_s020_8k_v2\n- **status**: DONE\n- **conclusion**: success\n- **metrics**:\n  - accuracy: **0.30**\n  - correct: 15\n  - total: 50\n  - truncated_count: 29\n  - truncated_rate: 0.58\n  - total_time_seconds: 5549\n- **hypothesis**: \"DS s020 accuracy eval with max_new_tokens=8192，补全 5-point dose curve。4096 版截断率 64%，8k 目标 &lt;20%。\"\n- **checkpoint_path**: /root/autodl-tmp/pacs/analysis_output/accuracy_ds_s020_8k_v2.json\n- **completed_at**: 2026-05-15T23:29:33.331Z\n\n### acc_ds_s025\n- **status**: DONE\n- **conclusion**: negative\n- **metrics**:\n  - accuracy: **0.08**\n  - correct: 4\n  - total: 50\n  - null_count: 37\n  - null_rate: 0.74\n  - output_truncated_count: 38\n  - output_truncated_rate: 0.76\n  - wrong_count: 9\n  - wrong_rate: 0.18\n  - extraction_failure_count: 1\n  - extraction_failure_rate: 0.02\n  - total_time_s: 1670.5\n  - heads_pruned: 196\n  - delta_vs_dense: -0.44\n- **checkpoint_path**: /root/autodl-tmp/pacs/analysis_output/accuracy_eval_ds_s025.json\n- **completed_at**: 2026-05-15T21:20:04.995Z\n\n### acc_ds_s025_8k\n- **status**: DONE\n- **conclusion**: killed\n\n### acc_ds_s025_8k_v2\n- **status**: DONE\n- **conclusion**: negative\n- **metrics**:\n  - accuracy: **0.08**\n  - correct: 4\n  - total: 50\n  - truncated_count: 38\n  - truncated_rate: 0.76\n  - avg_tokens: 6343.8\n  - max_new_tokens: 8192\n  - total_time_seconds: 6827.8\n  - null_count: 36\n- **checkpoint_path**: /root/autodl-tmp/pacs/analysis_output/accuracy_ds_s025_8k_v2.json\n- **completed_at**: 2026-05-16T00:20:39.536Z\n\n### acc_ds_s030_8k\n- **status**: DONE\n- **conclusion**: killed\n\n### acc_ds_s030_8k_v2\n- **status**: RUNNING\n- **conclusion**: (not yet concluded)\n- **hypothesis**: \"DS s030 accuracy eval with max_new_tokens=8192，补全 5-point dose curve。\"\n- **server**: westd-22162, gpu=cuda:2, pid=288901\n- **metrics**: (none yet)\n\n---\n\n## SET 2: All `gsm8k_*` Experiments (6 experiments)\n\n### gsm8k_profiling_ds\n- **status**: DONE\n- **conclusion**: success\n- **hypothesis**: \"GSM8K profiling 验证 compound sparsity severity 的可迁移性：DeepSeek 在 GSM8K n=50 上是否复现 MATH-500 的 phase-gated II pattern（importance &gt; random, 单调递增）\"\n- **metrics**:\n  - version: v3_median\n  - n_problems: 50\n  - method: \"median + Wilcoxon + bootstrap_median(B=10000)\"\n  - **importance**:\n    - s015: median_gradient=0.241, ci=[0.077, 0.478], wilcoxon_p=0.0003\n    - s020: median_gradient=0.74, ci=[0.314, 1.119], wilcoxon_p=0.0001\n    - s025: median_gradient=1.992, ci=[0.933, 2.82], wilcoxon_p=0.0001\n    - s030: median_gradient=4.682, ci=[2.121, 10.557], wilcoxon_p=0.0001\n  - **imp_rand_ratio**: s015=2.3, s020=2.5, s025=3.8, s030=2.8\n  - dose_response_monotonic: true\n- **failure_reason**: \"process dead 5x with no sentinel/W&amp;B -- auto-resolved as failed\"\n\n### gsm8k_profiling_qw\n- **status**: DONE\n- **conclusion**: success\n- **hypothesis**: \"GSM8K profiling 验证 compound sparsity severity 的可迁移性：Qwen 在 GSM8K n=50 上是否复现 MATH-500 的 phase-gated II pattern（importance &gt; random, 单调递增）\"\n- **notes**: \"All QW outputs truncated at max_new_tokens=2047 (50/50 problems). Does not affect directional conclusions. rand_s030 per-sparsity data missing, merged data has aggregation bug.\"\n- **metrics**:\n  - version: v3_median\n  - n_problems: 50\n  - method: \"median + Wilcoxon + bootstrap_median(B=10000)\"\n  - **importance**: s015=0.039, s020=0.158, s025=1.1, s030=2.092\n  - qw_rand_s030: **INVALID**\n- **checkpoint_path**: /root/autodl-tmp/pacs/analysis_output/gsm8k/\n\n### gsm8k_qw_rand_s025\n- **status**: DONE\n- **conclusion**: failed\n- **hypothesis**: \"C10: QW random masking s=0.25 在 GSM8K 上的 compound interaction，作为 importance masking 的对照组。\"\n- **parent**: gsm8k_profiling_qw\n- **failure_reason**: \"同 gsm8k_qw_rand_s030 的 bootstrap bug (tuple vs dict)，Director 指令主动 kill\"\n- **checkpoint_path**: \"N/A (killed before completion)\"\n\n### gsm8k_qw_rand_s025_v2\n- **status**: DONE\n- **conclusion**: success\n- **hypothesis**: \"C10 重跑：QW random masking s=0.25 GSM8K compound interaction（修复 bootstrap bug 后）\"\n- **parent**: gsm8k_qw_rand_s025\n- **metrics**:\n  - verdict: PASS\n  - n_problems: 50, n_bootstrap: 1000, seed: 42\n  - **high_sparsity** (216 segments, 9326 tokens): ppl_dense=1.0695, ppl_attn=5.9362, ppl_kv=3.4316, ppl_both=15.7484, ii_mean=6.5954, ii_ci=[1.1114, 11.3791], ii_median=0.7176, ii_median_ci=[0.5959, 0.9347], winsorized_mean=6.5046, skewness=-4.6807, outlier_count=3\n  - **low_sparsity** (252 segments, 29224 tokens): ppl_dense=1.1972, ppl_attn=11.5347, ppl_kv=5.6038, ppl_both=21.6874, ii_mean=2.3883, ii_ci=[-8.4602, 11.029], ii_median=1.4587, ii_median_ci=[1.1121, 2.0451], winsorized_mean=5.8911, skewness=-7.6074, outlier_count=4\n  - **mid_sparsity** (51 segments, 5954 tokens): ppl_dense=1.2601, ppl_attn=13.4132, ppl_kv=6.4841, ppl_both=20.8714, ii_mean=4.5407, ii_ci=[-4.8854, 12.4605], ii_median=1.1272, ii_median_ci=[0.637, 3.3729], winsorized_mean=6.3284, skewness=-3.4048, outlier_count=1\n- **checkpoint_path**: /root/autodl-tmp/pacs/profiling_output_gsm8k_qw_rand_s025_v2\n\n### gsm8k_qw_rand_s030\n- **status**: DONE\n- **conclusion**: failed\n- **hypothesis**: \"C10: QW random masking s=0.30 在 GSM8K 上的 compound interaction，作为 importance masking 的对照组。gsm8k_profiling_qw 中此条件结果 INVALID，需重跑。\"\n- **parent**: gsm8k_profiling_qw\n- **failure_reason**: `TypeError: tuple indices must be integers or slices, not str` in run_profiling_gsm8k.py line 459 (bootstrap bug: `bs[\"mean\"]` on a tuple)\n\n### gsm8k_qw_rand_s030_v2\n- **status**: DONE\n- **conclusion**: success\n- **hypothesis**: \"C10 重跑：QW random masking s=0.30 GSM8K compound interaction（修复 bootstrap bug 后）\"\n- **parent**: gsm8k_qw_rand_s030\n- **metrics**:\n  - verdict: PASS\n  - n_problems: 50, n_bootstrap: 1000, seed: 42\n  - **high_sparsity** (216 segments, 9326 tokens): null_ratio=2/50, ppl_dense=1.0695, ppl_attn=6.5613, ppl_kv=4.481, ppl_both=23.7486, ii_mean=11.83, ii_median=2.31, ii_ci=[6.17, 17.04], ii_median_ci=[1.64, 2.81], winsorized_mean=10.55, skewness=-2.29, outlier_count=7\n  - **low_sparsity** (252 segments, 29224 tokens): null_ratio=5/50, ppl_dense=1.1972, ppl_attn=6.3283, ppl_kv=8.5374, ppl_both=56.2304, ii_mean=31.26, ii_median=5.2, ii_ci=[17.84, 47.86], ii_median_ci=[3.95, 7.24], winsorized_mean=16.35, skewness=7.57, outlier_count=4\n  - **mid_sparsity** (51 segments, 5954 tokens): null_ratio=17/50, ppl_dense=1.2601, ppl_attn=18.6162, ppl_kv=11.6625, ppl_both=47.9019, ii_mean=18.02, ii_median=2.7, ii_ci=[0.09, 36.69], ii_median_ci=[1.46, 8.77], winsorized_mean=18.22, skewness=0.43, outlier_count=2\n- **checkpoint_path**: /root/autodl-tmp/pacs/profiling_output_gsm8k_qw_rand_s030_v2/profiling_results.json\n\n---\n\n**Summary of still-running experiments**: `acc_ds_s015_8k_v2` and `acc_ds_s030_8k_v2` are both still RUNNING with no metrics yet.\n\n**DS Accuracy dose curve (8k v2, completed only)**:\n| Condition | Accuracy | Truncation Rate |\n|-----------|----------|-----------------|\n| dense     | 0.74     | 0.16            |\n| s020      | 0.30     | 0.58            |\n| s025      | 0.08     | 0.76            |\n| s015      | (running) | --             |\n| s030      | (running) | --             |&lt;/result>\n&lt;usage>&lt;total_tokens>36037&lt;/total_tokens>&lt;tool_uses>11&lt;/tool_uses>&lt;duration_ms>119403&lt;/duration_ms>&lt;/usage>\n&lt;/task-notification>"
}
```

---

### Runtime record

_source line 40 · 2026-05-16T00:28:13.538Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-16T00:28:13.538Z",
  "sessionId": "38576691-e177-4a18-ab23-be69eff4b7ff"
}
```

---

## Round 3

7 recorded events

### User

_source line 41 · 2026-05-16T00:28:13.694Z_

&lt;task-notification>
&lt;task-id>a09137f4d041cbaa5&lt;/task-id>
&lt;tool-use-id>toolu_01DR2EwefaamHZqL1RC2KtYD&lt;/tool-use-id>
&lt;output-file>/tmp/claude-1000/-home-ubuntu--agent-ml-research-idea-gen-0509-11-projects-phase-gated-compound-sparse/38576691-e177-4a18-ab23-be69eff4b7ff/tasks/a09137f4d041cbaa5.output&lt;/output-file>
&lt;status>completed&lt;/status>
&lt;summary>Agent "Extract DS accuracy + GSM8K data" completed&lt;/summary>
&lt;result>Here is the complete verbatim extraction of both experiment sets.

---

## SET 1: All `acc_ds_*` Experiments (12 experiments)

### acc_ds_dense_8k
- **status**: DONE
- **conclusion**: killed
- **hypothesis**: "8192 token budget 下 DS dense baseline 截断率应降至 &lt;20%，accuracy 应高于 4096 版本的 0.52"
- **metrics**: (none recorded -- killed before completion)
- **spec**: server=westd-22162, gpu=cuda:0, pid=277990, wall_clock_seconds=129.7, gpu_hours=0.04
- **completed_at**: 2026-05-15T21:28:57.693Z

### acc_ds_dense_8k_v2
- **status**: DONE
- **conclusion**: success
- **hypothesis**: "DS dense 8k 重跑：原 acc_ds_dense_8k 进程被 kill 后输出丢失，需重跑获取完整 dense baseline accuracy (max_new_tokens=8192)。"
- **metrics**:
  - accuracy: **0.74**
  - correct: 37
  - n_problems: 50
  - truncation_rate: 0.16
  - truncated_count: 8
  - avg_tokens: 3126
  - max_new_tokens: 8192
  - total_time_seconds: 2882
- **checkpoint_path**: /root/autodl-tmp/pacs/analysis_output/accuracy_ds_dense_8k_v2.json
- **completed_at**: 2026-05-15T23:28:12.650Z

### acc_ds_s015_8k
- **status**: DONE
- **conclusion**: killed
- **hypothesis**: "8192 token budget 下 DS s015 截断率应降至 &lt;20%，accuracy 应高于 4096 版本的 0.36"
- **metrics**: (none -- killed)
- **completed_at**: 2026-05-15T21:28:48.029Z

### acc_ds_s015_8k_v2
- **status**: RUNNING
- **conclusion**: (not yet concluded)
- **hypothesis**: "DS s015 accuracy eval with max_new_tokens=8192，验证 dense→s015 是否存在断崖式下降（v1 暗示 0.74→~0.36）。"
- **metrics**: (none yet -- still running)
- **server**: westd-22162, gpu=cuda:0

### acc_ds_s020
- **status**: DONE
- **conclusion**: negative
- **metrics**:
  - ds_s020_acc: **0.26**
  - ds_s020_acc_v2: 0.26
  - ds_s020_correct: 13
  - ds_s020_total: 50
  - ds_s020_delta_vs_dense: -0.26
  - output_truncated_count: 32
  - output_truncated_rate: 0.64
  - extraction_failure_count: 31
  - extraction_failure_rate: 0.62
  - total_time_s: 1560
  - note: "v2 rescored with fixed radical+degree matcher; 0 changes. Dense baseline=0.52"
- **checkpoint_path**: /root/autodl-tmp/pacs/analysis_output/accuracy_eval_ds_s020.json
- **completed_at**: 2026-05-15T21:20:03.642Z

### acc_ds_s020_8k
- **status**: DONE
- **conclusion**: killed
- **hypothesis**: "8192 token budget 下 DS s020 截断率应从 64% 降至 &lt;20%，accuracy 应高于 4096 版本的 0.26"
- **metrics**: (none -- killed)

### acc_ds_s020_8k_v2
- **status**: DONE
- **conclusion**: success
- **metrics**:
  - accuracy: **0.30**
  - correct: 15
  - total: 50
  - truncated_count: 29
  - truncated_rate: 0.58
  - total_time_seconds: 5549
- **hypothesis**: "DS s020 accuracy eval with max_new_tokens=8192，补全 5-point dose curve。4096 版截断率 64%，8k 目标 &lt;20%。"
- **checkpoint_path**: /root/autodl-tmp/pacs/analysis_output/accuracy_ds_s020_8k_v2.json
- **completed_at**: 2026-05-15T23:29:33.331Z

### acc_ds_s025
- **status**: DONE
- **conclusion**: negative
- **metrics**:
  - accuracy: **0.08**
  - correct: 4
  - total: 50
  - null_count: 37
  - null_rate: 0.74
  - output_truncated_count: 38
  - output_truncated_rate: 0.76
  - wrong_count: 9
  - wrong_rate: 0.18
  - extraction_failure_count: 1
  - extraction_failure_rate: 0.02
  - total_time_s: 1670.5
  - heads_pruned: 196
  - delta_vs_dense: -0.44
- **checkpoint_path**: /root/autodl-tmp/pacs/analysis_output/accuracy_eval_ds_s025.json
- **completed_at**: 2026-05-15T21:20:04.995Z

### acc_ds_s025_8k
- **status**: DONE
- **conclusion**: killed

### acc_ds_s025_8k_v2
- **status**: DONE
- **conclusion**: negative
- **metrics**:
  - accuracy: **0.08**
  - correct: 4
  - total: 50
  - truncated_count: 38
  - truncated_rate: 0.76
  - avg_tokens: 6343.8
  - max_new_tokens: 8192
  - total_time_seconds: 6827.8
  - null_count: 36
- **checkpoint_path**: /root/autodl-tmp/pacs/analysis_output/accuracy_ds_s025_8k_v2.json
- **completed_at**: 2026-05-16T00:20:39.536Z

### acc_ds_s030_8k
- **status**: DONE
- **conclusion**: killed

### acc_ds_s030_8k_v2
- **status**: RUNNING
- **conclusion**: (not yet concluded)
- **hypothesis**: "DS s030 accuracy eval with max_new_tokens=8192，补全 5-point dose curve。"
- **server**: westd-22162, gpu=cuda:2, pid=288901
- **metrics**: (none yet)

---

## SET 2: All `gsm8k_*` Experiments (6 experiments)

### gsm8k_profiling_ds
- **status**: DONE
- **conclusion**: success
- **hypothesis**: "GSM8K profiling 验证 compound sparsity severity 的可迁移性：DeepSeek 在 GSM8K n=50 上是否复现 MATH-500 的 phase-gated II pattern（importance &gt; random, 单调递增）"
- **metrics**:
  - version: v3_median
  - n_problems: 50
  - method: "median + Wilcoxon + bootstrap_median(B=10000)"
  - **importance**:
    - s015: median_gradient=0.241, ci=[0.077, 0.478], wilcoxon_p=0.0003
    - s020: median_gradient=0.74, ci=[0.314, 1.119], wilcoxon_p=0.0001
    - s025: median_gradient=1.992, ci=[0.933, 2.82], wilcoxon_p=0.0001
    - s030: median_gradient=4.682, ci=[2.121, 10.557], wilcoxon_p=0.0001
  - **imp_rand_ratio**: s015=2.3, s020=2.5, s025=3.8, s030=2.8
  - dose_response_monotonic: true
- **failure_reason**: "process dead 5x with no sentinel/W&amp;B -- auto-resolved as failed"

### gsm8k_profiling_qw
- **status**: DONE
- **conclusion**: success
- **hypothesis**: "GSM8K profiling 验证 compound sparsity severity 的可迁移性：Qwen 在 GSM8K n=50 上是否复现 MATH-500 的 phase-gated II pattern（importance &gt; random, 单调递增）"
- **notes**: "All QW outputs truncated at max_new_tokens=2047 (50/50 problems). Does not affect directional conclusions. rand_s030 per-sparsity data missing, merged data has aggregation bug."
- **metrics**:
  - version: v3_median
  - n_problems: 50
  - method: "median + Wilcoxon + bootstrap_median(B=10000)"
  - **importance**: s015=0.039, s020=0.158, s025=1.1, s030=2.092
  - qw_rand_s030: **INVALID**
- **checkpoint_path**: /root/autodl-tmp/pacs/analysis_output/gsm8k/

### gsm8k_qw_rand_s025
- **status**: DONE
- **conclusion**: failed
- **hypothesis**: "C10: QW random masking s=0.25 在 GSM8K 上的 compound interaction，作为 importance masking 的对照组。"
- **parent**: gsm8k_profiling_qw
- **failure_reason**: "同 gsm8k_qw_rand_s030 的 bootstrap bug (tuple vs dict)，Director 指令主动 kill"
- **checkpoint_path**: "N/A (killed before completion)"

### gsm8k_qw_rand_s025_v2
- **status**: DONE
- **conclusion**: success
- **hypothesis**: "C10 重跑：QW random masking s=0.25 GSM8K compound interaction（修复 bootstrap bug 后）"
- **parent**: gsm8k_qw_rand_s025
- **metrics**:
  - verdict: PASS
  - n_problems: 50, n_bootstrap: 1000, seed: 42
  - **high_sparsity** (216 segments, 9326 tokens): ppl_dense=1.0695, ppl_attn=5.9362, ppl_kv=3.4316, ppl_both=15.7484, ii_mean=6.5954, ii_ci=[1.1114, 11.3791], ii_median=0.7176, ii_median_ci=[0.5959, 0.9347], winsorized_mean=6.5046, skewness=-4.6807, outlier_count=3
  - **low_sparsity** (252 segments, 29224 tokens): ppl_dense=1.1972, ppl_attn=11.5347, ppl_kv=5.6038, ppl_both=21.6874, ii_mean=2.3883, ii_ci=[-8.4602, 11.029], ii_median=1.4587, ii_median_ci=[1.1121, 2.0451], winsorized_mean=5.8911, skewness=-7.6074, outlier_count=4
  - **mid_sparsity** (51 segments, 5954 tokens): ppl_dense=1.2601, ppl_attn=13.4132, ppl_kv=6.4841, ppl_both=20.8714, ii_mean=4.5407, ii_ci=[-4.8854, 12.4605], ii_median=1.1272, ii_median_ci=[0.637, 3.3729], winsorized_mean=6.3284, skewness=-3.4048, outlier_count=1
- **checkpoint_path**: /root/autodl-tmp/pacs/profiling_output_gsm8k_qw_rand_s025_v2

### gsm8k_qw_rand_s030
- **status**: DONE
- **conclusion**: failed
- **hypothesis**: "C10: QW random masking s=0.30 在 GSM8K 上的 compound interaction，作为 importance masking 的对照组。gsm8k_profiling_qw 中此条件结果 INVALID，需重跑。"
- **parent**: gsm8k_profiling_qw
- **failure_reason**: `TypeError: tuple indices must be integers or slices, not str` in run_profiling_gsm8k.py line 459 (bootstrap bug: `bs["mean"]` on a tuple)

### gsm8k_qw_rand_s030_v2
- **status**: DONE
- **conclusion**: success
- **hypothesis**: "C10 重跑：QW random masking s=0.30 GSM8K compound interaction（修复 bootstrap bug 后）"
- **parent**: gsm8k_qw_rand_s030
- **metrics**:
  - verdict: PASS
  - n_problems: 50, n_bootstrap: 1000, seed: 42
  - **high_sparsity** (216 segments, 9326 tokens): null_ratio=2/50, ppl_dense=1.0695, ppl_attn=6.5613, ppl_kv=4.481, ppl_both=23.7486, ii_mean=11.83, ii_median=2.31, ii_ci=[6.17, 17.04], ii_median_ci=[1.64, 2.81], winsorized_mean=10.55, skewness=-2.29, outlier_count=7
  - **low_sparsity** (252 segments, 29224 tokens): null_ratio=5/50, ppl_dense=1.1972, ppl_attn=6.3283, ppl_kv=8.5374, ppl_both=56.2304, ii_mean=31.26, ii_median=5.2, ii_ci=[17.84, 47.86], ii_median_ci=[3.95, 7.24], winsorized_mean=16.35, skewness=7.57, outlier_count=4
  - **mid_sparsity** (51 segments, 5954 tokens): null_ratio=17/50, ppl_dense=1.2601, ppl_attn=18.6162, ppl_kv=11.6625, ppl_both=47.9019, ii_mean=18.02, ii_median=2.7, ii_ci=[0.09, 36.69], ii_median_ci=[1.46, 8.77], winsorized_mean=18.22, skewness=0.43, outlier_count=2
- **checkpoint_path**: /root/autodl-tmp/pacs/profiling_output_gsm8k_qw_rand_s030_v2/profiling_results.json

---

**Summary of still-running experiments**: `acc_ds_s015_8k_v2` and `acc_ds_s030_8k_v2` are both still RUNNING with no metrics yet.

**DS Accuracy dose curve (8k v2, completed only)**:
| Condition | Accuracy | Truncation Rate |
|-----------|----------|-----------------|
| dense     | 0.74     | 0.16            |
| s020      | 0.30     | 0.58            |
| s025      | 0.08     | 0.76            |
| s015      | (running) | --             |
| s030      | (running) | --             |&lt;/result>
&lt;usage>&lt;total_tokens>36037&lt;/total_tokens>&lt;tool_uses>11&lt;/tool_uses>&lt;duration_ms>119403&lt;/duration_ms>&lt;/usage>
&lt;/task-notification>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f4e7d630-8948-43c0-bd03-c6a978455f1f",
  "isSidechain": false,
  "promptId": "e04fdbbd-a97e-4a77-9f2f-e0f84e1e7163",
  "type": "user",
  "uuid": "b734842f-9894-41fd-88c2-0cfd08b7ba21",
  "permissionMode": "bypassPermissions",
  "origin": {
    "kind": "task-notification"
  },
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "sessionId": "38576691-e177-4a18-ab23-be69eff4b7ff",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 42 · 2026-05-16T00:28:16.762Z_

<details><summary>Logged reasoning block</summary>

```text
DS accuracy + GSM8K data received. Still waiting for 2 more agents: PPL dose curve and sf5/misc evidence.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b734842f-9894-41fd-88c2-0cfd08b7ba21",
  "isSidechain": false,
  "requestId": "req_011Cb5JQd3oTfZy1TSGfFi3X",
  "type": "assistant",
  "uuid": "2e12c5fe-303e-4665-b0a8-2ae0d1e40853",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "sessionId": "38576691-e177-4a18-ab23-be69eff4b7ff",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017Eb9EEHQh2ZeBNsWuYxPkh",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 4308,
      "cache_read_input_tokens": 39737,
      "output_tokens": 65,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4308,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 65,
          "cache_read_input_tokens": 39737,
          "cache_creation_input_tokens": 4308,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4308
          },
          "type": "message"
        }
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

_source line 43 · 2026-05-16T00:28:16.842Z_

DS accuracy + GSM8K data received. 2 agents still running.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2e12c5fe-303e-4665-b0a8-2ae0d1e40853",
  "isSidechain": false,
  "requestId": "req_011Cb5JQd3oTfZy1TSGfFi3X",
  "type": "assistant",
  "uuid": "bf78c3bc-192c-44bc-b9a6-5fdc3df13453",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "sessionId": "38576691-e177-4a18-ab23-be69eff4b7ff",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017Eb9EEHQh2ZeBNsWuYxPkh",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 4308,
      "cache_read_input_tokens": 39737,
      "output_tokens": 65,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4308,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 65,
          "cache_read_input_tokens": 39737,
          "cache_creation_input_tokens": 4308,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4308
          },
          "type": "message"
        }
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
  "leafUuid": "bf78c3bc-192c-44bc-b9a6-5fdc3df13453",
  "sessionId": "38576691-e177-4a18-ab23-be69eff4b7ff"
}
```

---

### Runtime record

_source line 45_

```json
{
  "type": "ai-title",
  "aiTitle": "Compile Round 10 experiment evidence for ARR submission",
  "sessionId": "38576691-e177-4a18-ab23-be69eff4b7ff"
}
```

---

### Runtime record

_source line 46 · 2026-05-16T00:28:55.426Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-16T00:28:55.426Z",
  "sessionId": "38576691-e177-4a18-ab23-be69eff4b7ff",
  "content": "&lt;task-notification>\n&lt;task-id>a692d7d4f3f7a841e&lt;/task-id>\n&lt;tool-use-id>toolu_012hWGjMJ6a2SV4Sbjb1yLkG&lt;/tool-use-id>\n&lt;output-file>/tmp/claude-1000/-home-ubuntu--agent-ml-research-idea-gen-0509-11-projects-phase-gated-compound-sparse/38576691-e177-4a18-ab23-be69eff4b7ff/tasks/a692d7d4f3f7a841e.output&lt;/output-file>\n&lt;status>completed&lt;/status>\n&lt;summary>Agent \"Extract sf5 + misc evidence\" completed&lt;/summary>\n&lt;result>Here is the complete verbatim extraction of all matching experiments from the registry.\n\n---\n\n## 1. sf5 asymmetric sparsity\n\n### sf5_asymmetric_spot\n- **exp_id:** sf5_asymmetric_spot\n- **status:** DONE\n- **conclusion:** success\n- **metrics:**\n  ```json\n  {\n    \"config_a_h02_kv03\": {\"II_low\": 19.51, \"II_mid\": 6.05, \"II_high\": 0.38, \"D\": 19.13},\n    \"config_b_h03_kv02\": {\"II_low\": 18.77, \"II_mid\": 3.97, \"II_high\": 0.52, \"D\": 18.25},\n    \"pre_registered_criterion_passed\": true,\n    \"gradient_direction\": \"II_low &gt;&gt; II_mid &gt;&gt; II_high (consistent with symmetric baseline)\"\n  }\n  ```\n- **notes:** null\n- **other fields:** checkpoint_path: `/root/autodl-tmp/pacs/profiling_output_sf5_h020_kv030/`, log_path: `/root/autodl-tmp/pacs/logs/sf5_config_A.log`\n\n---\n\n## 2. Appendix B G× correction / Cross-model Mann-Whitney U\n\n**No experiments found** in the registry with IDs or content matching \"gx\", \"G×\", \"appendix\", \"mann_whitney\", \"mann-whitney\", \"reanalysis\", or \"n475\"/\"n500_v2\". These analyses may have been performed as offline post-hoc computations rather than registered experiments, or they may reside in a different registry/artifact.\n\nThe closest match is `c2_qw_n500_r3` which has `effective_n: 475` in its metrics (see below).\n\n---\n\n## 3. n500 unified analysis (4 experiments)\n\n### c2_ds_n500\n- **exp_id:** c2_ds_n500\n- **status:** DONE\n- **conclusion:** killed\n- **metrics:** null\n- **notes:** DUPLICATE — 勿跑。实际实验在 c2_n500_deepseek (RUNNING)。Director 指令清理。\n- **hypothesis:** C2: n=500 统计功效提升。将 DeepSeek 8 conditions (imp/rand × 4 sparsity) 从 n=50 扩到 n=500 (full MATH-500)，验证现有结论在大样本下是否稳健。预注册：若 QW s015 CI 仍跨零，改叙事为 threshold sparsity ~s020。\n\n### c2_n500_deepseek\n- **exp_id:** c2_n500_deepseek\n- **status:** DONE\n- **conclusion:** success\n- **metrics:**\n  ```json\n  {\n    \"n_problems\": 500,\n    \"effective_n\": 496,\n    \"mid_null_rate\": 0.102,\n    \"imp_s015_median_ii\": 0.3907, \"imp_s015_ci\": [0.3496, 0.4431], \"imp_s015_wilcoxon_p\": 1.27e-70,\n    \"imp_s020_median_ii\": 1.2149, \"imp_s020_ci\": [1.1072, 1.3365], \"imp_s020_wilcoxon_p\": 3.98e-75,\n    \"imp_s025_median_ii\": 3.9857, \"imp_s025_ci\": [3.5272, 4.3588], \"imp_s025_wilcoxon_p\": 1.99e-78,\n    \"imp_s030_median_ii\": 8.4813, \"imp_s030_ci\": [7.7543, 9.6919], \"imp_s030_wilcoxon_p\": 1.09e-79,\n    \"rand_s015_median_ii\": 0.0139, \"rand_s015_wilcoxon_p\": 0.863,\n    \"rand_s020_median_ii\": 0.0315, \"rand_s020_wilcoxon_p\": 0.28,\n    \"rand_s025_median_ii\": 0.2574, \"rand_s025_bonf_p\": 0.005839, \"rand_s025_fdr_p\": 0.001914,\n    \"rand_s030_median_ii\": 0.5096, \"rand_s030_bonf_p\": 0.005903, \"rand_s030_fdr_p\": 0.001914,\n    \"dz_s015_s020\": -0.925, \"dz_s020_s025\": -0.824, \"dz_s025_s030\": -0.773, \"dz_s015_s030\": -0.944,\n    \"all_dz_reliable\": true,\n    \"dose_response_monotonic\": true,\n    \"dose_response_spearman_rho\": 1, \"dose_response_perm_p\": 0.0417,\n    \"imp_rand_ratio_range\": \"15.5-38.6x\",\n    \"bonferroni_k\": 4,\n    \"bonferroni_note\": \"Bonferroni k=4 family-wise (D066 revision)\"\n  }\n  ```\n- **notes:** [2026-05-15] ALL 8 CONDITIONS DONE (500/500). [D066] Bonferroni revised: k=4 family-wise (was k=48). DS rand s025 bonf_p=0.0058 (**), s030 bonf_p=0.0059 (**) — both restored to significant. BH-FDR also applied (48 tests): rand s025/s030 fdr_p=0.0019. Results in n500_unified_final.{csv,json}.\n- **other fields:** hypothesis (C2 statistical power boost), server: westd-22162, gpu: cuda:0,cuda:1, checkpoint_path: `/root/autodl-tmp/pacs/analysis_n500_results.json`\n\n### c2_qw_n500\n- **exp_id:** c2_qw_n500\n- **status:** DONE\n- **conclusion:** failed\n- **metrics:** null\n- **notes:** 2026-05-15T03:30: Cron false positive corrected. Process alive on GPU 2+3. s015 COMPLETE (500/500 both conditions, results in profiling_results.json). s020 RUNNING: qw_imp_s020 PID159269 cuda:2, qw_rand_s020 PID159794 cuda:3. Screen session auto-advances through sparsity levels. n=500 s015 analysis: both DeepSeek and Qwen paired gradient now significant (Bonferroni p&lt;0.0001), resolving D058.\n- **other fields:** hypothesis (C2 Qwen n=500), failure_reason: \"process dead 5× with no sentinel/W&amp;B — auto-resolved as failed\", 3 hook_events (on_failed)\n\n### c2_qw_n500_r3\n- **exp_id:** c2_qw_n500_r3\n- **status:** DONE\n- **conclusion:** success\n- **metrics:**\n  ```json\n  {\n    \"n_problems\": 500,\n    \"effective_n\": 475,\n    \"filter\": \"low+high valid only (mid-null allowed)\",\n    \"mid_null_rate\": 0.452,\n    \"imp_s015_median_ii\": 0.0659, \"imp_s015_ci\": [0.0492, 0.0925], \"imp_s015_wilcoxon_p\": 8.66e-15, \"imp_s015_bonf_p\": 3.46e-14,\n    \"imp_s020_median_ii\": 0.3073, \"imp_s020_ci\": [0.2612, 0.3564], \"imp_s020_wilcoxon_p\": 6.84e-42, \"imp_s020_bonf_p\": 2.74e-41,\n    \"imp_s025_median_ii\": 1.0745, \"imp_s025_ci\": [0.9766, 1.1787], \"imp_s025_wilcoxon_p\": 1.06e-68, \"imp_s025_bonf_p\": 4.25e-68,\n    \"imp_s030_median_ii\": 3.155, \"imp_s030_ci\": [2.7834, 3.5582], \"imp_s030_wilcoxon_p\": 9.21e-74, \"imp_s030_bonf_p\": 3.69e-73,\n    \"rand_s015_median_ii\": -0.0111, \"rand_s015_wilcoxon_p\": 0.172, \"rand_s015_bonf_p\": 0.687,\n    \"rand_s020_median_ii\": 0.0153, \"rand_s020_wilcoxon_p\": 0.2, \"rand_s020_bonf_p\": 0.8,\n    \"rand_s025_median_ii\": 0.3931, \"rand_s025_wilcoxon_p\": 1.59e-11, \"rand_s025_bonf_p\": 6.37e-11, \"rand_s025_fdr_p\": 2.63e-11,\n    \"rand_s030_median_ii\": 0.9127, \"rand_s030_wilcoxon_p\": 2.92e-15, \"rand_s030_bonf_p\": 1.17e-14, \"rand_s030_fdr_p\": 5.61e-15,\n    \"dz_s015_s020\": -0.629, \"dz_s020_s025\": -0.865, \"dz_s025_s030\": -0.767, \"dz_s015_s030\": -0.923,\n    \"all_dz_reliable\": true,\n    \"dose_response_monotonic\": true,\n    \"dose_response_spearman_rho\": 1, \"dose_response_perm_p\": 0.0417,\n    \"imp_rand_ratio_range\": \"2.7-20.1x\",\n    \"bonferroni_k\": 4,\n    \"bonferroni_note\": \"Bonferroni k=4 family-wise (D066 revision)\"\n  }\n  ```\n- **notes:** [2026-05-15] n=475 (low+high valid). [D066] Bonferroni revised: k=4 family-wise (was k=48). QW rand s025/s030 remain *** under k=4. BH-FDR also applied (48 tests). All imp conditions *** unchanged. Results in n500_unified_final.{csv,json}, n500_full_statistics.md.\n- **other fields:** parent: c2_qw_n500, checkpoint_path: `/root/autodl-tmp/pacs/analysis_n500_results.json`, log_path: `/root/autodl-tmp/pacs/analysis_output/n500_unified_final.json`\n\n---\n\n## 4. c4_entropy (discrimination collapse mechanism) — 2 experiments\n\n### c4_entropy\n- **exp_id:** c4_entropy\n- **status:** DONE\n- **conclusion:** success\n- **metrics:**\n  ```json\n  {\n    \"importance_entropy_delta\": {\"s015\": -0.0402, \"s020\": -0.0472, \"s025\": -0.0446, \"s030\": -0.0436},\n    \"random_entropy_delta\": {\"s015\": 0.1283, \"s020\": 0.136, \"s025\": 0.2171, \"s030\": 0.2327},\n    \"importance_gini_delta\": {\"s015\": -0.0301, \"s020\": -0.0404, \"s025\": -0.0647, \"s030\": -0.0806},\n    \"random_gini_delta\": {\"s015\": -0.0309, \"s020\": -0.0403, \"s025\": -0.062, \"s030\": -0.0732},\n    \"importance_cv_delta\": {\"s015\": -0.564, \"s020\": -0.774, \"s025\": -1.287, \"s030\": -1.665},\n    \"random_cv_delta\": {\"s015\": -1.021, \"s020\": -1.203, \"s025\": -1.923, \"s030\": -2.137},\n    \"problems_completed\": 30,\n    \"runtime_minutes\": 69.1\n  }\n  ```\n- **notes:** 与 bf16_qw_imp_s020 共用 cuda:1（20.5GB/97.9GB），无 OOM 风险。30 problems (6/level stratified)，预计 ~30-60min。tmux session: c4_entropy。代码待小修：sys.path.insert → 相对导入, torch_dtype → dtype（低优先级）。\n- **hypothesis:** C4 mechanism 直接验证：测量 head pruning 对 attention entropy 和 KV importance discrimination 的影响。Importance pruning 预期在 low-sparsity phase 引发 entropy collapse + Gini 下降，random pruning 无系统性效应。\n\n### qwen_c4_entropy\n- **exp_id:** qwen_c4_entropy\n- **status:** DONE\n- **conclusion:** negative\n- **metrics:**\n  ```json\n  {\n    \"problems_completed\": 30,\n    \"qwen_importance_entropy_delta\": {\"s015\": -0.0733, \"s020\": -0.0759, \"s025\": 0.0451, \"s030\": -0.0072},\n    \"qwen_random_entropy_delta\": {\"s015\": 0.0838, \"s020\": 0.0901, \"s025\": 0.2168, \"s030\": 0.1968},\n    \"qwen_importance_gini_delta\": {\"s015\": -0.0103, \"s020\": -0.0121, \"s025\": -0.01, \"s030\": -0.0202},\n    \"qwen_random_gini_delta\": {\"s015\": -0.0186, \"s020\": -0.0229, \"s025\": -0.0337, \"s030\": -0.0448},\n    \"qwen_importance_cv_delta\": {\"s015\": -0.045, \"s020\": -0.208, \"s025\": -1.491, \"s030\": -1.142},\n    \"qwen_random_cv_delta\": {\"s015\": -0.778, \"s020\": -0.889, \"s025\": -1.5, \"s030\": -1.677},\n    \"cross_model_notes\": \"random entropy increase consistent; importance entropy collapse inconsistent at s025 (reversed to +0.045) and near-zero at s030; gini/cv directions consistent but Qwen magnitudes smaller\"\n  }\n  ```\n- **notes:** Cross-model C4 验证 negative: random entropy increase 跨模型一致，但 importance entropy collapse 在 Qwen 不稳健（s025 方向反转 +0.0451 vs DeepSeek -0.0446, s030 接近零）。Gini/CV 方向一致但幅度差异大。不支持 entropy-discrimination collapse 的强跨模型普适性。\n- **checkpoint_path:** `/root/autodl-tmp/pacs/results/c4_attention_entropy_qwen/c4_entropy_results.json`\n\n---\n\n## 5. c3_llama (cross-architecture) — 2 experiments\n\n### c3_llama\n- **exp_id:** c3_llama\n- **status:** DONE\n- **conclusion:** success\n- **metrics:** null\n- **notes:** 8/8 conditions complete. Analysis output: analysis_output/c3_llama_{results,cohens_d,report}.*. Phase gradient d_z monotonically increasing (0.19→0.26→0.29→0.34). Cross-architecture pattern confirmed: LLaMA shows large phase gradient d_z ~1.0 across all sparsity levels, consistent qualitative direction with DeepSeek/Qwen. s030 Wilcoxon significant (p=0.029 Bonferroni). s015 median diff CI [0.002, 0.043] does not cross zero.\n- **hypothesis:** C3: LLaMA 架构验证。用 DeepSeek-R1-Distill-Llama-8B 验证 phase-modulated compound severity 是否跨架构复现（Qwen2ForCausalLM → LlamaForCausalLM），回应审稿人\"cross-model ≠ cross-architecture\"质疑。\n- **other fields:** checkpoint_path: `/root/autodl-tmp/pacs/profiling_output_c3_llama_{importance,random}_s{015,020,025,030}`, log_path: `/root/autodl-tmp/pacs/logs/c3_llama_{importance,random}_s{015,020,025,030}.log`\n\n### c3_llama_arch\n- **exp_id:** c3_llama_arch\n- **status:** DONE\n- **conclusion:** killed\n- **metrics:** null\n- **notes:** DUPLICATE — 勿跑。实际实验在 c3_llama (PREPARING)。Director 指令清理。\n- **hypothesis:** C3 architecture validation: 在 DeepSeek-R1-Distill-Llama-8B 上复现 phase-modulated compound severity，验证 finding 不限于 Qwen2 架构\n\n---\n\n## 6. c5b_pilot (phase-gated controller)\n\n### c5b_pilot\n- **exp_id:** c5b_pilot\n- **status:** DONE\n- **conclusion:** negative\n- **metrics:**\n  ```json\n  {\n    \"s025_uniform_median_ii\": 1.0435,\n    \"s025_oracle_median_ii\": 0.856,\n    \"s025_oracle_recovery_pct\": 18,\n    \"s025_oracle_recovery_ci\": [-39, 45.8],\n    \"s025_oracle_wilcoxon_p\": 0.0021,\n    \"s025_heuristic_median_ii\": 0.7127,\n    \"s025_heuristic_recovery_pct\": 31.7,\n    \"s025_heuristic_recovery_ci\": [-22.8, 66],\n    \"s025_heuristic_wilcoxon_p\": 0.0236,\n    \"gate_criterion\": \"oracle_recovery &gt; 30%\",\n    \"gate_result\": \"FAIL\",\n    \"s030_status\": \"not_completed\",\n    \"n_problems\": 30\n  }\n  ```\n- **notes:** s025 30/30 完成（GPU3 run）。Gate FAIL: oracle recovery +18.0% &lt; 30% threshold。Heuristic recovery +31.7%。s030 未完成（SSH 断连 kill）。Cron 误判为 failed（无 sentinel/W&amp;B），实际 s025 结果完整。结果路径: profiling_output_c5b_all_s025/mitigation_pilot_results.json。Framing 提案: C5b → §8 Future Work open question。\n- **hypothesis:** C5b mitigation pilot: oracle (真实 phase labels) + heuristic (token position ratio) phase-aware sparsity allocation 能否恢复 compound interaction severity。Gate: oracle recovery &gt;30% at s025 or s030。\n- **failure_reason:** oracle recovery 18% &lt; 30% gate; heuristic 32% CI crosses zero. Scientific gate_failed, not technical failure. D057:降为 future work, 不再 retry.\n\n---\n\n## Summary of missing queries\n\n- **Appendix B G× correction**: No experiment in this registry matches \"gx\", \"G×\", or \"appendix\". This analysis was likely done as a post-hoc computation rather than a registered experiment.\n- **Cross-model Mann-Whitney U**: No experiment matches \"mann_whitney\", \"reanalysis\", or \"n475\". The `c2_qw_n500_r3` experiment has `effective_n: 475` in its metrics, which may be the source data for such an analysis.\n- **n500_v2**: No experiment with this exact ID exists. The n500 experiments are: `c2_ds_n500` (killed duplicate), `c2_n500_deepseek` (success, DS), `c2_qw_n500` (failed, cron issue), `c2_qw_n500_r3` (success, QW continuation).&lt;/result>\n&lt;usage>&lt;total_tokens>28703&lt;/total_tokens>&lt;tool_uses>9&lt;/tool_uses>&lt;duration_ms>155398&lt;/duration_ms>&lt;/usage>\n&lt;/task-notification>"
}
````

---

### Runtime record

_source line 47 · 2026-05-16T00:28:55.466Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-16T00:28:55.466Z",
  "sessionId": "38576691-e177-4a18-ab23-be69eff4b7ff"
}
```

---

## Round 4

7 recorded events

### User

_source line 48 · 2026-05-16T00:28:55.476Z_

&lt;task-notification>
&lt;task-id>a692d7d4f3f7a841e&lt;/task-id>
&lt;tool-use-id>toolu_012hWGjMJ6a2SV4Sbjb1yLkG&lt;/tool-use-id>
&lt;output-file>/tmp/claude-1000/-home-ubuntu--agent-ml-research-idea-gen-0509-11-projects-phase-gated-compound-sparse/38576691-e177-4a18-ab23-be69eff4b7ff/tasks/a692d7d4f3f7a841e.output&lt;/output-file>
&lt;status>completed&lt;/status>
&lt;summary>Agent "Extract sf5 + misc evidence" completed&lt;/summary>
&lt;result>Here is the complete verbatim extraction of all matching experiments from the registry.

---

## 1. sf5 asymmetric sparsity

### sf5_asymmetric_spot
- **exp_id:** sf5_asymmetric_spot
- **status:** DONE
- **conclusion:** success
- **metrics:**
  ```json
  {
    "config_a_h02_kv03": {"II_low": 19.51, "II_mid": 6.05, "II_high": 0.38, "D": 19.13},
    "config_b_h03_kv02": {"II_low": 18.77, "II_mid": 3.97, "II_high": 0.52, "D": 18.25},
    "pre_registered_criterion_passed": true,
    "gradient_direction": "II_low &gt;&gt; II_mid &gt;&gt; II_high (consistent with symmetric baseline)"
  }
  ```
- **notes:** null
- **other fields:** checkpoint_path: `/root/autodl-tmp/pacs/profiling_output_sf5_h020_kv030/`, log_path: `/root/autodl-tmp/pacs/logs/sf5_config_A.log`

---

## 2. Appendix B G× correction / Cross-model Mann-Whitney U

**No experiments found** in the registry with IDs or content matching "gx", "G×", "appendix", "mann_whitney", "mann-whitney", "reanalysis", or "n475"/"n500_v2". These analyses may have been performed as offline post-hoc computations rather than registered experiments, or they may reside in a different registry/artifact.

The closest match is `c2_qw_n500_r3` which has `effective_n: 475` in its metrics (see below).

---

## 3. n500 unified analysis (4 experiments)

### c2_ds_n500
- **exp_id:** c2_ds_n500
- **status:** DONE
- **conclusion:** killed
- **metrics:** null
- **notes:** DUPLICATE — 勿跑。实际实验在 c2_n500_deepseek (RUNNING)。Director 指令清理。
- **hypothesis:** C2: n=500 统计功效提升。将 DeepSeek 8 conditions (imp/rand × 4 sparsity) 从 n=50 扩到 n=500 (full MATH-500)，验证现有结论在大样本下是否稳健。预注册：若 QW s015 CI 仍跨零，改叙事为 threshold sparsity ~s020。

### c2_n500_deepseek
- **exp_id:** c2_n500_deepseek
- **status:** DONE
- **conclusion:** success
- **metrics:**
  ```json
  {
    "n_problems": 500,
    "effective_n": 496,
    "mid_null_rate": 0.102,
    "imp_s015_median_ii": 0.3907, "imp_s015_ci": [0.3496, 0.4431], "imp_s015_wilcoxon_p": 1.27e-70,
    "imp_s020_median_ii": 1.2149, "imp_s020_ci": [1.1072, 1.3365], "imp_s020_wilcoxon_p": 3.98e-75,
    "imp_s025_median_ii": 3.9857, "imp_s025_ci": [3.5272, 4.3588], "imp_s025_wilcoxon_p": 1.99e-78,
    "imp_s030_median_ii": 8.4813, "imp_s030_ci": [7.7543, 9.6919], "imp_s030_wilcoxon_p": 1.09e-79,
    "rand_s015_median_ii": 0.0139, "rand_s015_wilcoxon_p": 0.863,
    "rand_s020_median_ii": 0.0315, "rand_s020_wilcoxon_p": 0.28,
    "rand_s025_median_ii": 0.2574, "rand_s025_bonf_p": 0.005839, "rand_s025_fdr_p": 0.001914,
    "rand_s030_median_ii": 0.5096, "rand_s030_bonf_p": 0.005903, "rand_s030_fdr_p": 0.001914,
    "dz_s015_s020": -0.925, "dz_s020_s025": -0.824, "dz_s025_s030": -0.773, "dz_s015_s030": -0.944,
    "all_dz_reliable": true,
    "dose_response_monotonic": true,
    "dose_response_spearman_rho": 1, "dose_response_perm_p": 0.0417,
    "imp_rand_ratio_range": "15.5-38.6x",
    "bonferroni_k": 4,
    "bonferroni_note": "Bonferroni k=4 family-wise (D066 revision)"
  }
  ```
- **notes:** [2026-05-15] ALL 8 CONDITIONS DONE (500/500). [D066] Bonferroni revised: k=4 family-wise (was k=48). DS rand s025 bonf_p=0.0058 (**), s030 bonf_p=0.0059 (**) — both restored to significant. BH-FDR also applied (48 tests): rand s025/s030 fdr_p=0.0019. Results in n500_unified_final.{csv,json}.
- **other fields:** hypothesis (C2 statistical power boost), server: westd-22162, gpu: cuda:0,cuda:1, checkpoint_path: `/root/autodl-tmp/pacs/analysis_n500_results.json`

### c2_qw_n500
- **exp_id:** c2_qw_n500
- **status:** DONE
- **conclusion:** failed
- **metrics:** null
- **notes:** 2026-05-15T03:30: Cron false positive corrected. Process alive on GPU 2+3. s015 COMPLETE (500/500 both conditions, results in profiling_results.json). s020 RUNNING: qw_imp_s020 PID159269 cuda:2, qw_rand_s020 PID159794 cuda:3. Screen session auto-advances through sparsity levels. n=500 s015 analysis: both DeepSeek and Qwen paired gradient now significant (Bonferroni p&lt;0.0001), resolving D058.
- **other fields:** hypothesis (C2 Qwen n=500), failure_reason: "process dead 5× with no sentinel/W&amp;B — auto-resolved as failed", 3 hook_events (on_failed)

### c2_qw_n500_r3
- **exp_id:** c2_qw_n500_r3
- **status:** DONE
- **conclusion:** success
- **metrics:**
  ```json
  {
    "n_problems": 500,
    "effective_n": 475,
    "filter": "low+high valid only (mid-null allowed)",
    "mid_null_rate": 0.452,
    "imp_s015_median_ii": 0.0659, "imp_s015_ci": [0.0492, 0.0925], "imp_s015_wilcoxon_p": 8.66e-15, "imp_s015_bonf_p": 3.46e-14,
    "imp_s020_median_ii": 0.3073, "imp_s020_ci": [0.2612, 0.3564], "imp_s020_wilcoxon_p": 6.84e-42, "imp_s020_bonf_p": 2.74e-41,
    "imp_s025_median_ii": 1.0745, "imp_s025_ci": [0.9766, 1.1787], "imp_s025_wilcoxon_p": 1.06e-68, "imp_s025_bonf_p": 4.25e-68,
    "imp_s030_median_ii": 3.155, "imp_s030_ci": [2.7834, 3.5582], "imp_s030_wilcoxon_p": 9.21e-74, "imp_s030_bonf_p": 3.69e-73,
    "rand_s015_median_ii": -0.0111, "rand_s015_wilcoxon_p": 0.172, "rand_s015_bonf_p": 0.687,
    "rand_s020_median_ii": 0.0153, "rand_s020_wilcoxon_p": 0.2, "rand_s020_bonf_p": 0.8,
    "rand_s025_median_ii": 0.3931, "rand_s025_wilcoxon_p": 1.59e-11, "rand_s025_bonf_p": 6.37e-11, "rand_s025_fdr_p": 2.63e-11,
    "rand_s030_median_ii": 0.9127, "rand_s030_wilcoxon_p": 2.92e-15, "rand_s030_bonf_p": 1.17e-14, "rand_s030_fdr_p": 5.61e-15,
    "dz_s015_s020": -0.629, "dz_s020_s025": -0.865, "dz_s025_s030": -0.767, "dz_s015_s030": -0.923,
    "all_dz_reliable": true,
    "dose_response_monotonic": true,
    "dose_response_spearman_rho": 1, "dose_response_perm_p": 0.0417,
    "imp_rand_ratio_range": "2.7-20.1x",
    "bonferroni_k": 4,
    "bonferroni_note": "Bonferroni k=4 family-wise (D066 revision)"
  }
  ```
- **notes:** [2026-05-15] n=475 (low+high valid). [D066] Bonferroni revised: k=4 family-wise (was k=48). QW rand s025/s030 remain *** under k=4. BH-FDR also applied (48 tests). All imp conditions *** unchanged. Results in n500_unified_final.{csv,json}, n500_full_statistics.md.
- **other fields:** parent: c2_qw_n500, checkpoint_path: `/root/autodl-tmp/pacs/analysis_n500_results.json`, log_path: `/root/autodl-tmp/pacs/analysis_output/n500_unified_final.json`

---

## 4. c4_entropy (discrimination collapse mechanism) — 2 experiments

### c4_entropy
- **exp_id:** c4_entropy
- **status:** DONE
- **conclusion:** success
- **metrics:**
  ```json
  {
    "importance_entropy_delta": {"s015": -0.0402, "s020": -0.0472, "s025": -0.0446, "s030": -0.0436},
    "random_entropy_delta": {"s015": 0.1283, "s020": 0.136, "s025": 0.2171, "s030": 0.2327},
    "importance_gini_delta": {"s015": -0.0301, "s020": -0.0404, "s025": -0.0647, "s030": -0.0806},
    "random_gini_delta": {"s015": -0.0309, "s020": -0.0403, "s025": -0.062, "s030": -0.0732},
    "importance_cv_delta": {"s015": -0.564, "s020": -0.774, "s025": -1.287, "s030": -1.665},
    "random_cv_delta": {"s015": -1.021, "s020": -1.203, "s025": -1.923, "s030": -2.137},
    "problems_completed": 30,
    "runtime_minutes": 69.1
  }
  ```
- **notes:** 与 bf16_qw_imp_s020 共用 cuda:1（20.5GB/97.9GB），无 OOM 风险。30 problems (6/level stratified)，预计 ~30-60min。tmux session: c4_entropy。代码待小修：sys.path.insert → 相对导入, torch_dtype → dtype（低优先级）。
- **hypothesis:** C4 mechanism 直接验证：测量 head pruning 对 attention entropy 和 KV importance discrimination 的影响。Importance pruning 预期在 low-sparsity phase 引发 entropy collapse + Gini 下降，random pruning 无系统性效应。

### qwen_c4_entropy
- **exp_id:** qwen_c4_entropy
- **status:** DONE
- **conclusion:** negative
- **metrics:**
  ```json
  {
    "problems_completed": 30,
    "qwen_importance_entropy_delta": {"s015": -0.0733, "s020": -0.0759, "s025": 0.0451, "s030": -0.0072},
    "qwen_random_entropy_delta": {"s015": 0.0838, "s020": 0.0901, "s025": 0.2168, "s030": 0.1968},
    "qwen_importance_gini_delta": {"s015": -0.0103, "s020": -0.0121, "s025": -0.01, "s030": -0.0202},
    "qwen_random_gini_delta": {"s015": -0.0186, "s020": -0.0229, "s025": -0.0337, "s030": -0.0448},
    "qwen_importance_cv_delta": {"s015": -0.045, "s020": -0.208, "s025": -1.491, "s030": -1.142},
    "qwen_random_cv_delta": {"s015": -0.778, "s020": -0.889, "s025": -1.5, "s030": -1.677},
    "cross_model_notes": "random entropy increase consistent; importance entropy collapse inconsistent at s025 (reversed to +0.045) and near-zero at s030; gini/cv directions consistent but Qwen magnitudes smaller"
  }
  ```
- **notes:** Cross-model C4 验证 negative: random entropy increase 跨模型一致，但 importance entropy collapse 在 Qwen 不稳健（s025 方向反转 +0.0451 vs DeepSeek -0.0446, s030 接近零）。Gini/CV 方向一致但幅度差异大。不支持 entropy-discrimination collapse 的强跨模型普适性。
- **checkpoint_path:** `/root/autodl-tmp/pacs/results/c4_attention_entropy_qwen/c4_entropy_results.json`

---

## 5. c3_llama (cross-architecture) — 2 experiments

### c3_llama
- **exp_id:** c3_llama
- **status:** DONE
- **conclusion:** success
- **metrics:** null
- **notes:** 8/8 conditions complete. Analysis output: analysis_output/c3_llama_{results,cohens_d,report}.*. Phase gradient d_z monotonically increasing (0.19→0.26→0.29→0.34). Cross-architecture pattern confirmed: LLaMA shows large phase gradient d_z ~1.0 across all sparsity levels, consistent qualitative direction with DeepSeek/Qwen. s030 Wilcoxon significant (p=0.029 Bonferroni). s015 median diff CI [0.002, 0.043] does not cross zero.
- **hypothesis:** C3: LLaMA 架构验证。用 DeepSeek-R1-Distill-Llama-8B 验证 phase-modulated compound severity 是否跨架构复现（Qwen2ForCausalLM → LlamaForCausalLM），回应审稿人"cross-model ≠ cross-architecture"质疑。
- **other fields:** checkpoint_path: `/root/autodl-tmp/pacs/profiling_output_c3_llama_{importance,random}_s{015,020,025,030}`, log_path: `/root/autodl-tmp/pacs/logs/c3_llama_{importance,random}_s{015,020,025,030}.log`

### c3_llama_arch
- **exp_id:** c3_llama_arch
- **status:** DONE
- **conclusion:** killed
- **metrics:** null
- **notes:** DUPLICATE — 勿跑。实际实验在 c3_llama (PREPARING)。Director 指令清理。
- **hypothesis:** C3 architecture validation: 在 DeepSeek-R1-Distill-Llama-8B 上复现 phase-modulated compound severity，验证 finding 不限于 Qwen2 架构

---

## 6. c5b_pilot (phase-gated controller)

### c5b_pilot
- **exp_id:** c5b_pilot
- **status:** DONE
- **conclusion:** negative
- **metrics:**
  ```json
  {
    "s025_uniform_median_ii": 1.0435,
    "s025_oracle_median_ii": 0.856,
    "s025_oracle_recovery_pct": 18,
    "s025_oracle_recovery_ci": [-39, 45.8],
    "s025_oracle_wilcoxon_p": 0.0021,
    "s025_heuristic_median_ii": 0.7127,
    "s025_heuristic_recovery_pct": 31.7,
    "s025_heuristic_recovery_ci": [-22.8, 66],
    "s025_heuristic_wilcoxon_p": 0.0236,
    "gate_criterion": "oracle_recovery &gt; 30%",
    "gate_result": "FAIL",
    "s030_status": "not_completed",
    "n_problems": 30
  }
  ```
- **notes:** s025 30/30 完成（GPU3 run）。Gate FAIL: oracle recovery +18.0% &lt; 30% threshold。Heuristic recovery +31.7%。s030 未完成（SSH 断连 kill）。Cron 误判为 failed（无 sentinel/W&amp;B），实际 s025 结果完整。结果路径: profiling_output_c5b_all_s025/mitigation_pilot_results.json。Framing 提案: C5b → §8 Future Work open question。
- **hypothesis:** C5b mitigation pilot: oracle (真实 phase labels) + heuristic (token position ratio) phase-aware sparsity allocation 能否恢复 compound interaction severity。Gate: oracle recovery &gt;30% at s025 or s030。
- **failure_reason:** oracle recovery 18% &lt; 30% gate; heuristic 32% CI crosses zero. Scientific gate_failed, not technical failure. D057:降为 future work, 不再 retry.

---

## Summary of missing queries

- **Appendix B G× correction**: No experiment in this registry matches "gx", "G×", or "appendix". This analysis was likely done as a post-hoc computation rather than a registered experiment.
- **Cross-model Mann-Whitney U**: No experiment matches "mann_whitney", "reanalysis", or "n475". The `c2_qw_n500_r3` experiment has `effective_n: 475` in its metrics, which may be the source data for such an analysis.
- **n500_v2**: No experiment with this exact ID exists. The n500 experiments are: `c2_ds_n500` (killed duplicate), `c2_n500_deepseek` (success, DS), `c2_qw_n500` (failed, cron issue), `c2_qw_n500_r3` (success, QW continuation).&lt;/result>
&lt;usage>&lt;total_tokens>28703&lt;/total_tokens>&lt;tool_uses>9&lt;/tool_uses>&lt;duration_ms>155398&lt;/duration_ms>&lt;/usage>
&lt;/task-notification>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bf78c3bc-192c-44bc-b9a6-5fdc3df13453",
  "isSidechain": false,
  "promptId": "e407ad33-0d22-42cd-985e-f0f2dc98ae50",
  "type": "user",
  "uuid": "6e8ebfa8-3204-4f2e-aa93-3fbe0783f9fb",
  "permissionMode": "bypassPermissions",
  "origin": {
    "kind": "task-notification"
  },
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "sessionId": "38576691-e177-4a18-ab23-be69eff4b7ff",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 49 · 2026-05-16T00:29:00.354Z_

<details><summary>Logged reasoning block</summary>

```text
3 of 4 agents completed. Still waiting for the PPL dose curve agent. Let me check what I have so far and start organizing the data while waiting.

I have:
1. QW Accuracy - complete
2. DS Accuracy + GSM8K - complete
3. sf5 + misc evidence - complete
4. PPL dose curve - still running

Let me wait for the last agent.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6e8ebfa8-3204-4f2e-aa93-3fbe0783f9fb",
  "isSidechain": false,
  "requestId": "req_011Cb5JThciknwaU9Q8ynG65",
  "type": "assistant",
  "uuid": "878c0ee1-9b02-4144-b8b9-94499fe27fda",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "sessionId": "38576691-e177-4a18-ab23-be69eff4b7ff",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016qSsXC8KMidHzcE4oiGwQi",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 5570,
      "cache_read_input_tokens": 44045,
      "output_tokens": 125,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5570,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 125,
          "cache_read_input_tokens": 44045,
          "cache_creation_input_tokens": 5570,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5570
          },
          "type": "message"
        }
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

_source line 50 · 2026-05-16T00:29:00.361Z_

3/4 agents done. Waiting for PPL dose curve extraction.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "878c0ee1-9b02-4144-b8b9-94499fe27fda",
  "isSidechain": false,
  "requestId": "req_011Cb5JThciknwaU9Q8ynG65",
  "type": "assistant",
  "uuid": "a81eda25-58e7-4acf-83fb-2714cd6ec3cd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "sessionId": "38576691-e177-4a18-ab23-be69eff4b7ff",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016qSsXC8KMidHzcE4oiGwQi",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 5570,
      "cache_read_input_tokens": 44045,
      "output_tokens": 125,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5570,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 125,
          "cache_read_input_tokens": 44045,
          "cache_creation_input_tokens": 5570,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5570
          },
          "type": "message"
        }
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

_source line 51 · 2026-05-16T00:30:09.365Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-16T00:30:09.365Z",
  "sessionId": "38576691-e177-4a18-ab23-be69eff4b7ff",
  "content": "&lt;task-notification>\n&lt;task-id>a7fba12d105bf979c&lt;/task-id>\n&lt;tool-use-id>toolu_01HEFFWgTPf2hCW6r76uC5en&lt;/tool-use-id>\n&lt;output-file>/tmp/claude-1000/-home-ubuntu--agent-ml-research-idea-gen-0509-11-projects-phase-gated-compound-sparse/38576691-e177-4a18-ab23-be69eff4b7ff/tasks/a7fba12d105bf979c.output&lt;/output-file>\n&lt;status>completed&lt;/status>\n&lt;summary>Agent \"Extract PPL dose curve data\" completed&lt;/summary>\n&lt;result>I now have all the data. Here is the complete extraction of all 65 PPL dose curve experiments:\n\n---\n\n## Summary: 65 PPL Dose Curve Experiments\n\n### GROUP 1: v6_importance (4 experiments) — DeepSeek fp16, importance masking, n=50\n\n**v6_importance_s015** | DONE / success\n- ii_high_median: 0.2266, ii_mid_median: 0.7432, ii_low_median: 2.8762\n- ii_high_mean: 0.2874, ii_mid_mean: 1.6858, ii_low_mean: 8.5161\n- per_problem_ii_count: 50, n_high: 43, n_mid: 32, n_low: 24, problems: 50\n- bootstrap_gradient_paired: 11.53, bootstrap_ci_paired: [3.49, 23.78]\n- bootstrap_gradient_unpaired: 12.69, bootstrap_ci_unpaired: [4.96, 28.45], bootstrap_p: 0\n\n**v6_importance_s020** | DONE / success\n- ii_high_median: 0.3353, ii_mid_median: 1.6733, ii_low_median: 9.2538\n- ii_high_mean: 0.4936, ii_mid_mean: 4.9538, ii_low_mean: 25.8764\n- per_problem_ii_count: 50, n_high: 42, n_mid: 28, n_low: 21, problems: 50\n- bootstrap_gradient_paired: 11.05, bootstrap_ci_paired: [5.42, 69.27]\n- bootstrap_gradient_unpaired: 27.6, bootstrap_ci_unpaired: [6.55, 75.16], bootstrap_p: 0\n\n**v6_importance_s025** | DONE / success\n- ii_high_median: 0.6641, ii_mid_median: 5.3067, ii_low_median: 24.1619\n- ii_high_mean: 0.8842, ii_mid_mean: 10.057, ii_low_mean: 71.8854\n- per_problem_ii_count: 50, n_high: 42, n_mid: 23, n_low: 21, problems: 50\n- bootstrap_gradient_paired: 35.72, bootstrap_ci_paired: [9.52, 101.54]\n- bootstrap_gradient_unpaired: 36.38, bootstrap_ci_unpaired: [13.19, 97.61], bootstrap_p: 0\n\n**v6_importance_s030** | DONE / success\n- ii_high_median: 0.8833, ii_mid_median: 7.2706, ii_low_median: 34.6937\n- ii_high_mean: 1.5151, ii_mid_mean: 78.8215, ii_low_mean: 1163.9677\n- per_problem_ii_count: 50, n_high: 40, n_mid: 22, n_low: 20, problems: 50\n- bootstrap_gradient_paired: 41.92, bootstrap_ci_paired: [19.14, 299.76]\n- bootstrap_gradient_unpaired: 39.28, bootstrap_ci_unpaired: [21.87, 129.59], bootstrap_p: 0\n\n---\n\n### GROUP 2: v6_random (6 experiments) — DeepSeek fp16, random masking (control), n=50\n\n**v6_random_s015** | DONE / success\n- ii_high_median: 0.1606, ii_mid_median: 0.252, ii_low_median: 0.1831\n- ii_high_mean: 0.4563, ii_mid_mean: 0.5134, ii_low_mean: 0.4775\n- bootstrap_gradient_paired: -0.2722, bootstrap_ci_paired: [-0.7039, 0.1548], bootstrap_p: 0.903\n- verdict: FAIL\n- per_problem_ii_stats: high(min=-3.06, max=5.02, mean=0.54, median=0.20), mid(min=-2.72, max=4.67, mean=0.40, median=0.30), low(min=-0.40, max=3.70, mean=0.48, median=0.25)\n\n**v6_random_s020** | DONE / success\n- ii_high_mean: 0.855584, ii_high_median: 0.321331, ii_high_ci: [-0.124, 1.617]\n- ii_mid_mean: 1.258123, ii_mid_median: 0.455663, ii_mid_ci: [0.675, 2.076]\n- ii_low_mean: 0.956933, ii_low_median: 0.591916, ii_low_ci: [0.584, 1.413]\n- gradient_mean_low_over_high: 1.118, gradient_median_low_over_high: 1.842, pass_fail: FAIL\n- perplexity: high_dense=1.1462, high_both=7.9749, mid_dense=1.1226, mid_both=6.8553, low_dense=1.1105, low_both=22.5868\n- Notes: Random baseline FAIL expected. gradient_mean=1.12x (near flat), no phase-dependent gradient.\n\n**v6_random_s025** | DONE / success\n- ii_high_median: 3.0024, ii_mid_median: 2.9846, ii_low_median: 2.9146\n- ii_high_mean: 3.9052, ii_mid_mean: 7.9491, ii_low_mean: 3.9114\n- bootstrap_gradient_paired: -0.1199, bootstrap_ci_paired: [-1.517, 1.246], bootstrap_p: 0.559\n- verdict: FAIL\n- Notes: gradient=0.90 (near 1.0), confirms no phase-dependent amplification. Contrast with importance (gradient=35.72).\n\n**v6_random_s030** | DONE / failed — killed by bf16-nan-fix worker. No metrics.\n\n**v6_random_s030_r2** | DONE / failed — tmux session conflict, abandoned.\n\n**v6_random_s030_r3** | DONE / success\n- II_high_mean: 9.2364, II_mid_mean: -230.7604, II_low_mean: -7.4119\n- II_high_median: 4.0237, II_mid_median: 2.4272, II_low_median: 4.735\n- ppl_low_both: 88.94, per_problem_count: 50\n- Notes: Verdict=PASS is outlier artifact; mid-phase skewness=-13.08 drives mean to -230.76, but median is flat (2.4-4.7). fp16 data for reference only, paper uses bf16.\n\n---\n\n### GROUP 3: bf16_ds_imp (6 experiments) — DeepSeek bf16, importance masking\n\n**bf16_ds_imp_s010** | DONE / negative\n- verdict: FAIL, problems: 50\n- II_high_sparsity_median: 0.0027, II_high_sparsity_mean: -0.1998\n- II_low_sparsity_median: 0.0151, II_low_sparsity_mean: -0.1066\n- II_mid_sparsity_median: 0.0061, II_mid_sparsity_mean: -0.0131\n- tokens: high=21086, low=27748, mid=13306\n\n**bf16_ds_imp_s015** | DONE / killed\n- median_difference: 0.323579, permutation_p: 0, cohens_d: 0.6068\n- bootstrap_ci_95: [0.198824, 0.471566], wilcoxon_p: 0\n- n_bootstrap: 10000, n_paired: 49\n- Notes: Superseded by bf16_importance_s015 (DONE, success).\n\n**bf16_ds_imp_s020** | DONE / killed\n- median_difference: 1.15202, permutation_p: 0, cohens_d: 0.725\n- bootstrap_ci_95: [0.655454, 1.256001], wilcoxon_p: 0\n- n_bootstrap: 10000, n_paired: 49\n- Notes: Superseded by bf16_importance_s020.\n\n**bf16_ds_imp_s025** | DONE / killed\n- median_difference: 3.968568, permutation_p: 0, cohens_d: 0.9534\n- bootstrap_ci_95: [2.829037, 5.291756], wilcoxon_p: 0\n- n_bootstrap: 10000, n_paired: 49\n- Notes: Superseded by bf16_importance_s025.\n\n**bf16_ds_imp_s030** | DONE / killed\n- median_difference: 9.943595, permutation_p: 0, cohens_d: 1.1263\n- bootstrap_ci_95: [8.391554, 16.652865], wilcoxon_p: 0\n- n_bootstrap: 10000, n_paired: 49\n- Notes: Superseded by bf16_importance_s030.\n\n**bf16_ds_imp_s035** | DONE / success\n- verdict: PASS, problems: 50\n- II_high_sparsity_median: 0.1051, II_high_sparsity_mean: 1.4309\n- II_low_sparsity_median: 28.7649, II_low_sparsity_mean: 104.1892\n- II_mid_sparsity_median: 4.9542, II_mid_sparsity_mean: 20.326\n- tokens: high=21086, low=27748, mid=13306\n- ci_overlap_test: low vs mid CI non-overlapping at 0.35\n\n---\n\n### GROUP 4: bf16_ds_rand (4 experiments) — DeepSeek bf16, random masking (control)\n\n**bf16_ds_rand_s015** | DONE / success\n- interaction_index: high(mean=0.22, median=0.093, ci=[-1.01,1.52], skew=-5.4), mid(mean=-3.36, median=0.097, ci=[-8.41,0.37], skew=-10.56), low(mean=-1.90, median=0.103, ci=[-4.97,0.27], skew=-11.57)\n- perplexity: high_both=5.7569, mid_both=11.3156, low_both=6.2886\n- pass_fail: FAIL, median_difference: 0.0095\n- Notes: Verdict PASS-&gt;FAIL corrected. Median II all in 0.09-0.10 range, CI fully overlap, no structured gradient.\n\n**bf16_ds_rand_s020** | DONE / success\n- interaction_index: high(mean=1.12, median=0.292, skew=9.59), mid(mean=-1.58, median=0.350, skew=-12.31), low(mean=-0.41, median=0.276, skew=-10.07)\n- perplexity: high_both=8.8129, mid_both=11.4974, low_both=9.2001\n- pass_fail: FAIL, median_difference: -0.0155\n- Notes: Verdict PASS-&gt;FAIL corrected. Median II in 0.28-0.35 range, CI fully overlap.\n\n**bf16_ds_rand_s025** | DONE / success\n- interaction_index: high(mean=3.59, median=0.818, skew=-7.57), mid(mean=-1.85, median=0.932, skew=-12.76), low(mean=0.72, median=1.363, skew=-15.85)\n- perplexity: high_both=17.7423, mid_both=29.4661, low_both=17.9694\n- pass_fail: FAIL, median_difference: 0.5445\n- Notes: Verdict PASS-&gt;FAIL corrected. Median II in 0.82-1.36 range, CI fully overlap.\n\n**bf16_ds_rand_s030** | DONE / success\n- interaction_index: high(mean=7.56, median=2.503, ci=[4.41,11.62]), mid(mean=6.25, median=2.592, ci=[2.18,10.48]), low(mean=6.83, median=4.041, ci=[3.24,10.70])\n- perplexity: high_both=40.7553, mid_both=62.4422, low_both=37.6009\n- pass_fail: FAIL, median_difference: 1.5383\n- Notes: Three phase median II in 2.50-4.04, median CI fully overlap, no structured gradient.\n\n---\n\n### GROUP 5: bf16_qw_imp (6 experiments) — Qwen bf16, importance masking\n\n**bf16_qw_imp_s010** | DONE / success\n- overall_verdict: PASS, ci_overlap_test: PASS, sign_reversal_test: FAIL\n- high_sparsity_II_median: 0.0001, high_sparsity_II_mean: -0.0887\n- mid_sparsity_II_median: -0.0359, mid_sparsity_II_mean: -0.084\n- low_sparsity_II_median: -0.0444, low_sparsity_II_mean: -0.2431\n- ppl: high_dense=1.074, high_both=1.228, mid_dense=1.133, mid_both=1.741, low_dense=1.152, low_both=3.204\n\n**bf16_qw_imp_s015** | DONE / success\n- median_difference: 0.047619, permutation_p: 0.0001, cohens_d: 0.3705\n- bootstrap_ci_95: [-0.005077, 0.109517], wilcoxon_p: 0.02958\n- n_bootstrap: 10000, n_paired: 46\n- Notes: Weak gradient, consistent with DeepSeek at s=0.15. PPL(both): high=1.31, mid=2.20, low=5.44.\n\n**bf16_qw_imp_s020** | DONE / success\n- median_difference: 0.207511, permutation_p: 0, cohens_d: 0.7224\n- bootstrap_ci_95: [0.067222, 0.40226], wilcoxon_p: 3.4e-05\n- n_bootstrap: 10000, n_paired: 46\n- Notes: PPL(both): high=1.37, mid=3.43, low=9.20. Low phase II distinctly elevated.\n\n**bf16_qw_imp_s025** | DONE / success\n- median_difference: 1.108706, permutation_p: 0, cohens_d: 1.2329\n- bootstrap_ci_95: [0.609247, 1.469002], wilcoxon_p: 0\n- n_bootstrap: 10000, n_paired: 46\n- Notes: PPL(both): high=1.54, mid=5.36, low=16.96. Strong gradient, mid phase becomes significant.\n\n**bf16_qw_imp_s030** | DONE / success\n- median_difference: 2.619385, permutation_p: 0, cohens_d: 1.4394\n- bootstrap_ci_95: [1.722281, 3.651063], wilcoxon_p: 0\n- n_bootstrap: 10000, n_paired: 46\n- Notes: PPL(both): high=1.86, mid=9.48, low=35.32. Strongest gradient, fully replicates DeepSeek pattern.\n\n**bf16_qw_imp_s035** | DONE / success\n- overall_verdict: PASS, ci_overlap_test: PASS, sign_reversal_test: FAIL\n- high_sparsity_II_median: 0.0232, high_sparsity_II_mean: 0.1643\n- mid_sparsity_II_median: 0.9577, mid_sparsity_II_mean: 8.0734\n- low_sparsity_II_median: 8.2358, low_sparsity_II_mean: 18.9673\n- ppl: high_dense=1.074, high_both=2.344, mid_dense=1.133, mid_both=20.991, low_dense=1.152, low_both=58.036\n\n---\n\n### GROUP 6: bf16_qw_rand (4 experiments) — Qwen bf16, random masking (control)\n\n**bf16_qw_rand_s015** | DONE / success\n- median II: high=0.138, mid=0.219, low=0.188 — no structured gradient\n- median_difference: -0.029401, permutation_p: 0.7657, cohens_d: -0.0507\n- bootstrap_ci_95: [-0.2106, 0.2124], wilcoxon_p: 0.862554\n- pass_fail: FAIL\n\n**bf16_qw_rand_s020** | DONE / success\n- phase_median_ii: high=0.474, mid=0.876, low=0.485\n- median_difference: 0.128948, permutation_p: 0.352, cohens_d: 0.247\n- bootstrap_ci_95: [-0.139, 0.215], wilcoxon_p: 0.149\n- pass_fail: FAIL\n\n**bf16_qw_rand_s025** | DONE / success\n- phase_median_ii: high=1.604, mid=2.222, low=2.264\n- median_difference: 1.144074, permutation_p: 0.1679, cohens_d: 0.1574\n- bootstrap_ci_95: [-0.3166, 4.1645], wilcoxon_p: 0.010313\n- pass_fail: FAIL\n\n**bf16_qw_rand_s030** | DONE / success\n- median_high: 4.200557, median_mid: 6.477036, median_low: 8.065662\n- median_diff: 2.418272, permutation_p: 0.012, cohens_d: -0.03513, wilcoxon_p: 0.01566\n- bootstrap_ci_low: 0.241897, bootstrap_ci_high: 3.314824\n- Notes: D043 re-bootstrap confirmed PASS-&gt;FAIL. gradient CI [-1.54, 13.71] includes 0, p=0.111. Random masking now 8/8 FAIL across both models.\n\n---\n\n### GROUP 7: bf16_importance (early) (4 experiments) — DeepSeek bf16, importance masking (canonical)\n\n**bf16_importance_s015** | DONE / success\n- interaction_index: high(mean=-0.150, median=0.006, skew=-14.99), mid(mean=0.447, median=0.081, skew=4.72), low(mean=2.406, median=0.398, skew=9.54)\n- perplexity: high_both=1.5911, mid_both=3.4541, low_both=12.5084\n- gradient_paired_aggregate_legacy: 69.24, median_difference: 0.3925\n- pass_fail: PASS (CI non-overlap + sign reversal)\n\n**bf16_importance_s020** | DONE / success\n- interaction_index: high(mean=0.129, median=0.015, skew=16.67), mid(mean=1.260, median=0.203, skew=7.05), low(mean=6.029, median=1.496, skew=6.01)\n- perplexity: high_both=2.1047, mid_both=5.4246, low_both=23.74\n- gradient_paired_aggregate_legacy: 5.90, median_difference: 1.4818\n- pass_fail: PASS\n\n**bf16_importance_s025** | DONE / success\n- interaction_index: high(mean=0.303, median=0.032, skew=4.88), mid(mean=5.730, median=1.118, skew=8.28), low(mean=25.853, median=7.196, skew=7.40)\n- perplexity: high_both=2.7026, mid_both=13.3436, low_both=63.668\n- gradient_paired_aggregate_legacy: 222.35, median_difference: 7.1636\n- pass_fail: PASS\n\n**bf16_importance_s030** | DONE / success\n- interaction_index: high(mean=0.555, median=0.053, skew=10.62), mid(mean=11.30, median=2.283, skew=9.19), low(mean=57.795, median=14.640, skew=8.31)\n- perplexity: high_both=3.2372, mid_both=24.2847, low_both=122.61\n- gradient_paired_aggregate_legacy: 57.24, median_difference: 14.5861\n- pass_fail: PASS\n- Notes: 4-point median sequence perfectly monotonic: s015(0.40)-&gt;s020(1.50)-&gt;s025(7.20)-&gt;s030(14.64). PPL sequence also monotonic: 12.51-&gt;23.74-&gt;63.67-&gt;122.61.\n\n---\n\n### GROUP 8: bf16_random (early) (4 experiments) — all killed, superseded\n\n**bf16_random_s015** | killed — superseded by bf16_ds_rand_s015\n**bf16_random_s020** | killed — superseded by bf16_ds_rand_s020\n**bf16_random_s025** | killed — superseded by bf16_ds_rand_s025\n**bf16_random_s030** | killed — superseded by bf16_ds_rand_s030\n\n---\n\n### GROUP 9: bf16_qwen_importance (early) (4 experiments) — all killed, superseded\n\n**bf16_qwen_importance_s015** | killed — superseded by bf16_qw_imp_s015\n**bf16_qwen_importance_s020** | killed — superseded by bf16_qw_imp_s020\n**bf16_qwen_importance_s025** | killed — superseded by bf16_qw_imp_s025\n**bf16_qwen_importance_s030** | killed — superseded by bf16_qw_imp_s030\n\n---\n\n### GROUP 10: n500_unified (4 experiments) — n=500 statistical power boost\n\n**c2_ds_n500** | killed — DUPLICATE, actual experiment in c2_n500_deepseek.\n\n**c2_n500_deepseek** | DONE / success — DeepSeek, n=500\n- effective_n: 496, mid_null_rate: 0.102\n- **Importance (all p=0):**\n  - s015: median_ii=0.3907, ci=[0.3496, 0.4431], wilcoxon_p=1.27e-70\n  - s020: median_ii=1.2149, ci=[1.1072, 1.3365], wilcoxon_p=3.98e-75\n  - s025: median_ii=3.9857, ci=[3.5272, 4.3588], wilcoxon_p=1.99e-78\n  - s030: median_ii=8.4813, ci=[7.7543, 9.6919], wilcoxon_p=1.09e-79\n- **Random (controls):**\n  - s015: median_ii=0.0139, wilcoxon_p=0.863\n  - s020: median_ii=0.0315, wilcoxon_p=0.28\n  - s025: median_ii=0.2574, bonf_p=0.005839, fdr_p=0.001914\n  - s030: median_ii=0.5096, bonf_p=0.005903, fdr_p=0.001914\n- Effect sizes (dz): s015-s020=-0.925, s020-s025=-0.824, s025-s030=-0.773, s015-s030=-0.944\n- all_dz_reliable: True, dose_response_monotonic: True, dose_response_spearman_rho: 1, dose_response_perm_p: 0.0417\n- imp_rand_ratio_range: 15.5-38.6x, bonferroni_k: 4\n\n**c2_qw_n500** | DONE / failed — process alive but conclusion=failed. s015 complete, s020+ in progress.\n\n**c2_qw_n500_r3** | DONE / success — Qwen, n=500\n- effective_n: 475, mid_null_rate: 0.452\n- **Importance (all p &lt; 1e-14):**\n  - s015: median_ii=0.0659, ci=[0.0492, 0.0925], wilcoxon_p=8.66e-15, bonf_p=3.46e-14\n  - s020: median_ii=0.3073, ci=[0.2612, 0.3564], wilcoxon_p=6.84e-42, bonf_p=2.74e-41\n  - s025: median_ii=1.0745, ci=[0.9766, 1.1787], wilcoxon_p=1.06e-68, bonf_p=4.25e-68\n  - s030: median_ii=3.155, ci=[2.7834, 3.5582], wilcoxon_p=9.21e-74, bonf_p=3.69e-73\n- **Random (controls):**\n  - s015: median_ii=-0.0111, wilcoxon_p=0.172, bonf_p=0.687\n  - s020: median_ii=0.0153, wilcoxon_p=0.2, bonf_p=0.8\n  - s025: median_ii=0.3931, wilcoxon_p=1.59e-11, bonf_p=6.37e-11\n  - s030: median_ii=0.9127, wilcoxon_p=2.92e-15, bonf_p=1.17e-14\n- Effect sizes (dz): s015-s020=-0.629, s020-s025=-0.865, s025-s030=-0.767, s015-s030=-0.923\n- all_dz_reliable: True, dose_response_monotonic: True, dose_response_spearman_rho: 1, dose_response_perm_p: 0.0417\n- imp_rand_ratio_range: 2.7-20.1x, bonferroni_k: 4\n\n---\n\n### GROUP 11: mvp_v5_fixed (6 experiments) — DeepSeek fp16, importance masking, early version\n\n**mvp_v5_fixed_s015** | DONE / negative\n- ii_high_median: 0.205, ii_mid_median: 0.696, ii_low_median: 2.627\n- both_ppl: high=2.284, mid=3.941, low=16.999, problems=50\n\n**mvp_v5_fixed_s020** | DONE / killed — WARNING: pre-fix code, INVALIDATED\n- ii_high_median: 0.33, ii_mid_median: 1.55, ii_low_median: 9.56\n- both_ppl: high=2.7, mid=8.13, low=42.64\n\n**mvp_v5_fixed_s020_r2** | DONE / negative\n- ii_high_median: 0.3333, ii_mid_median: 1.5479, ii_low_median: 9.5627\n- both_ppl: high=2.7, mid=8.13, low=42.64, problems=50\n\n**mvp_v5_fixed_s025** | DONE / negative\n- ii_high_median: 0.584, ii_mid_median: 4.522, ii_low_median: 30.903\n- both_ppl: high=3.462, mid=16.415, low=104.175, problems=50\n\n**mvp_v5_fixed_s030** | DONE / killed — WARNING: pre-fix code, INVALIDATED\n- ii_high_median: 0.6, ii_mid_median: 7.47, ii_low_median: 44.63\n- both_ppl: high=5.71, mid=137.61, low=963.2\n\n**mvp_v5_fixed_s030_r2** | DONE / negative\n- ii_high_median: 0.5964, ii_mid_median: 7.4671, ii_low_median: 44.6324\n- both_ppl: high=5.71, mid=137.61, low=963.2, problems=50\n\n---\n\n### GROUP 12: mvp_v5_random (4 experiments) — DeepSeek fp16, random masking (control), early version\n\n**mvp_v5_random_s015** | DONE / success\n- ii_high_median: 0.1606, ii_mid_median: 0.252, ii_low_median: 0.1831\n- both_ppl: high=3.92, mid=4.14, low=4.71, problems=50\n\n**mvp_v5_random_s020** | DONE / success\n- ii_high_median: 0.321331, ii_mid_median: 0.455663, ii_low_median: 0.591916\n- both_ppl: high=7.975, mid=6.855, low=22.587, problems=50\n\n**mvp_v5_random_s025** | DONE / success\n- ii_high_median: 3.002, ii_mid_median: 2.985, ii_low_median: 2.915\n- both_ppl: high=17.06, mid=15.38, low=29.32, problems=50\n\n**mvp_v5_random_s030** | DONE / success\n- ii_high_median: 5.378, ii_mid_median: 5.886, ii_low_median: 3.777\n- both_ppl: high=41.35, mid=24.20, low=68.53, problems=50\n\n---\n\n### GROUP 13: mvp_v4_legacy (2 experiments) — DeepSeek, very early version\n\n**mvp_v4_legacy_s01** | DONE / negative\n- II_high: mean=-0.11, ci=[-0.81, 0.41]; II_mid: mean=-15.97, ci=[-47.99, 1.29]; II_low: mean=0.00\n- ppl: high_both=22.13, mid_both=47.59, verdict: FAIL\n- Notes: Sparsity too low, II near zero or negative.\n\n**mvp_v4_legacy_s02** | DONE / success\n- ii_high: mean=21.29, ci=[0.03, 63.16]; ii_mid: mean=21.87, ci=[4.99, 41.79]; ii_low: mean=0.00\n- ppl: high(dense=1.15, kv=104.42, both=63.41), mid(dense=1.12, kv=324.16, both=170.47), low(dense=1.11, kv=1.11, both=1.30)\n- mvp_verdict: PASS\n\n---\n\n### GROUP 14: Other PPL-related experiments (7 experiments)\n\n**acc_ds_s020_8k_v2** | DONE / success — accuracy eval at s=0.20, max_tokens=8192\n- accuracy: 0.30, correct: 15/50, truncated_rate: 0.58\n\n**acc_ds_s025_8k_v2** | DONE / negative — accuracy eval at s=0.25\n- accuracy: 0.08, correct: 4/50, truncated_rate: 0.76\n\n**acc_ds_s030_8k_v2** | RUNNING — accuracy eval at s=0.30, no metrics yet\n\n**c2_accuracy_eval** | DONE / success — accuracy dose curve (DS + Qwen)\n- ds_dense_acc: 0.52, ds_s015_acc: 0.36 (delta=-0.16), ds_s030_acc: 0.10 (delta=-0.42)\n- qw_dense_acc: 0.32, qw_s015_acc: 0.34 (delta=+0.02), qw_s030_acc: 0.14 (delta=-0.18)\n- ds_s030_chinese_reasoning_rate: 0.4, ds_dense_truncation_rate: 0.56\n\n**gsm8k_profiling_ds** | DONE / success — GSM8K transferability (DeepSeek)\n- importance: s015(median_grad=0.241, p=0.0003), s020(0.74, p=0.0001), s025(1.992, p=0.0001), s030(4.682, p=0.0001)\n- imp_rand_ratio: s015=2.3x, s020=2.5x, s025=3.8x, s030=2.8x\n- dose_response_monotonic: True\n\n**gsm8k_qw_rand_s025_v2** | DONE / success — GSM8K Qwen random s=0.25\n- verdict: PASS, high_ii_median: 0.718, mid_ii_median: 1.127, low_ii_median: 1.459\n\n**gsm8k_qw_rand_s030_v2** | DONE / success — GSM8K Qwen random s=0.30\n- verdict: PASS, high_ii_median: 2.31, mid_ii_median: 2.70, low_ii_median: 5.20\n\n---\n\n## Key Takeaways\n\n**Total: 65 experiments** across 14 groups. Of these:\n- 8 killed/superseded (bf16_random_s015-s030, bf16_qwen_importance_s015-s030)\n- 2 killed/superseded (c2_ds_n500, v6_random_s030, v6_random_s030_r2)\n- 1 RUNNING (acc_ds_s030_8k_v2)\n- Remaining ~54 have valid metrics\n\n**Canonical dose curve data (bf16, paper-quality):**\n- DeepSeek importance: bf16_importance_s015 through s030 — all PASS, median_diff monotonic: 0.39 -&gt; 1.48 -&gt; 7.16 -&gt; 14.59\n- DeepSeek random: bf16_ds_rand_s015 through s030 — all FAIL (expected)\n- Qwen importance: bf16_qw_imp_s015 through s030 — all PASS, median_diff: 0.048 -&gt; 0.208 -&gt; 1.109 -&gt; 2.619, cohens_d: 0.37 -&gt; 0.72 -&gt; 1.23 -&gt; 1.44\n- Qwen random: bf16_qw_rand_s015 through s030 — all FAIL (expected)\n- n=500 unified: c2_n500_deepseek + c2_qw_n500_r3 — dose_response_monotonic=True for both, spearman_rho=1.0, all importance conditions p &lt; 1e-14&lt;/result>\n&lt;usage>&lt;total_tokens>56370&lt;/total_tokens>&lt;tool_uses>17&lt;/tool_uses>&lt;duration_ms>244987&lt;/duration_ms>&lt;/usage>\n&lt;/task-notification>"
}
```

---

### Runtime record

_source line 52_

```json
{
  "type": "last-prompt",
  "leafUuid": "a81eda25-58e7-4acf-83fb-2714cd6ec3cd",
  "sessionId": "38576691-e177-4a18-ab23-be69eff4b7ff"
}
```

---

### Runtime record

_source line 53_

```json
{
  "type": "ai-title",
  "aiTitle": "Compile Round 10 experiment evidence for ARR submission",
  "sessionId": "38576691-e177-4a18-ab23-be69eff4b7ff"
}
```

---

### Runtime record

_source line 54 · 2026-05-16T00:30:09.457Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-16T00:30:09.457Z",
  "sessionId": "38576691-e177-4a18-ab23-be69eff4b7ff"
}
```

---

## Round 5

22 recorded events

### User

_source line 55 · 2026-05-16T00:30:09.467Z_

&lt;task-notification>
&lt;task-id>a7fba12d105bf979c&lt;/task-id>
&lt;tool-use-id>toolu_01HEFFWgTPf2hCW6r76uC5en&lt;/tool-use-id>
&lt;output-file>/tmp/claude-1000/-home-ubuntu--agent-ml-research-idea-gen-0509-11-projects-phase-gated-compound-sparse/38576691-e177-4a18-ab23-be69eff4b7ff/tasks/a7fba12d105bf979c.output&lt;/output-file>
&lt;status>completed&lt;/status>
&lt;summary>Agent "Extract PPL dose curve data" completed&lt;/summary>
&lt;result>I now have all the data. Here is the complete extraction of all 65 PPL dose curve experiments:

---

## Summary: 65 PPL Dose Curve Experiments

### GROUP 1: v6_importance (4 experiments) — DeepSeek fp16, importance masking, n=50

**v6_importance_s015** | DONE / success
- ii_high_median: 0.2266, ii_mid_median: 0.7432, ii_low_median: 2.8762
- ii_high_mean: 0.2874, ii_mid_mean: 1.6858, ii_low_mean: 8.5161
- per_problem_ii_count: 50, n_high: 43, n_mid: 32, n_low: 24, problems: 50
- bootstrap_gradient_paired: 11.53, bootstrap_ci_paired: [3.49, 23.78]
- bootstrap_gradient_unpaired: 12.69, bootstrap_ci_unpaired: [4.96, 28.45], bootstrap_p: 0

**v6_importance_s020** | DONE / success
- ii_high_median: 0.3353, ii_mid_median: 1.6733, ii_low_median: 9.2538
- ii_high_mean: 0.4936, ii_mid_mean: 4.9538, ii_low_mean: 25.8764
- per_problem_ii_count: 50, n_high: 42, n_mid: 28, n_low: 21, problems: 50
- bootstrap_gradient_paired: 11.05, bootstrap_ci_paired: [5.42, 69.27]
- bootstrap_gradient_unpaired: 27.6, bootstrap_ci_unpaired: [6.55, 75.16], bootstrap_p: 0

**v6_importance_s025** | DONE / success
- ii_high_median: 0.6641, ii_mid_median: 5.3067, ii_low_median: 24.1619
- ii_high_mean: 0.8842, ii_mid_mean: 10.057, ii_low_mean: 71.8854
- per_problem_ii_count: 50, n_high: 42, n_mid: 23, n_low: 21, problems: 50
- bootstrap_gradient_paired: 35.72, bootstrap_ci_paired: [9.52, 101.54]
- bootstrap_gradient_unpaired: 36.38, bootstrap_ci_unpaired: [13.19, 97.61], bootstrap_p: 0

**v6_importance_s030** | DONE / success
- ii_high_median: 0.8833, ii_mid_median: 7.2706, ii_low_median: 34.6937
- ii_high_mean: 1.5151, ii_mid_mean: 78.8215, ii_low_mean: 1163.9677
- per_problem_ii_count: 50, n_high: 40, n_mid: 22, n_low: 20, problems: 50
- bootstrap_gradient_paired: 41.92, bootstrap_ci_paired: [19.14, 299.76]
- bootstrap_gradient_unpaired: 39.28, bootstrap_ci_unpaired: [21.87, 129.59], bootstrap_p: 0

---

### GROUP 2: v6_random (6 experiments) — DeepSeek fp16, random masking (control), n=50

**v6_random_s015** | DONE / success
- ii_high_median: 0.1606, ii_mid_median: 0.252, ii_low_median: 0.1831
- ii_high_mean: 0.4563, ii_mid_mean: 0.5134, ii_low_mean: 0.4775
- bootstrap_gradient_paired: -0.2722, bootstrap_ci_paired: [-0.7039, 0.1548], bootstrap_p: 0.903
- verdict: FAIL
- per_problem_ii_stats: high(min=-3.06, max=5.02, mean=0.54, median=0.20), mid(min=-2.72, max=4.67, mean=0.40, median=0.30), low(min=-0.40, max=3.70, mean=0.48, median=0.25)

**v6_random_s020** | DONE / success
- ii_high_mean: 0.855584, ii_high_median: 0.321331, ii_high_ci: [-0.124, 1.617]
- ii_mid_mean: 1.258123, ii_mid_median: 0.455663, ii_mid_ci: [0.675, 2.076]
- ii_low_mean: 0.956933, ii_low_median: 0.591916, ii_low_ci: [0.584, 1.413]
- gradient_mean_low_over_high: 1.118, gradient_median_low_over_high: 1.842, pass_fail: FAIL
- perplexity: high_dense=1.1462, high_both=7.9749, mid_dense=1.1226, mid_both=6.8553, low_dense=1.1105, low_both=22.5868
- Notes: Random baseline FAIL expected. gradient_mean=1.12x (near flat), no phase-dependent gradient.

**v6_random_s025** | DONE / success
- ii_high_median: 3.0024, ii_mid_median: 2.9846, ii_low_median: 2.9146
- ii_high_mean: 3.9052, ii_mid_mean: 7.9491, ii_low_mean: 3.9114
- bootstrap_gradient_paired: -0.1199, bootstrap_ci_paired: [-1.517, 1.246], bootstrap_p: 0.559
- verdict: FAIL
- Notes: gradient=0.90 (near 1.0), confirms no phase-dependent amplification. Contrast with importance (gradient=35.72).

**v6_random_s030** | DONE / failed — killed by bf16-nan-fix worker. No metrics.

**v6_random_s030_r2** | DONE / failed — tmux session conflict, abandoned.

**v6_random_s030_r3** | DONE / success
- II_high_mean: 9.2364, II_mid_mean: -230.7604, II_low_mean: -7.4119
- II_high_median: 4.0237, II_mid_median: 2.4272, II_low_median: 4.735
- ppl_low_both: 88.94, per_problem_count: 50
- Notes: Verdict=PASS is outlier artifact; mid-phase skewness=-13.08 drives mean to -230.76, but median is flat (2.4-4.7). fp16 data for reference only, paper uses bf16.

---

### GROUP 3: bf16_ds_imp (6 experiments) — DeepSeek bf16, importance masking

**bf16_ds_imp_s010** | DONE / negative
- verdict: FAIL, problems: 50
- II_high_sparsity_median: 0.0027, II_high_sparsity_mean: -0.1998
- II_low_sparsity_median: 0.0151, II_low_sparsity_mean: -0.1066
- II_mid_sparsity_median: 0.0061, II_mid_sparsity_mean: -0.0131
- tokens: high=21086, low=27748, mid=13306

**bf16_ds_imp_s015** | DONE / killed
- median_difference: 0.323579, permutation_p: 0, cohens_d: 0.6068
- bootstrap_ci_95: [0.198824, 0.471566], wilcoxon_p: 0
- n_bootstrap: 10000, n_paired: 49
- Notes: Superseded by bf16_importance_s015 (DONE, success).

**bf16_ds_imp_s020** | DONE / killed
- median_difference: 1.15202, permutation_p: 0, cohens_d: 0.725
- bootstrap_ci_95: [0.655454, 1.256001], wilcoxon_p: 0
- n_bootstrap: 10000, n_paired: 49
- Notes: Superseded by bf16_importance_s020.

**bf16_ds_imp_s025** | DONE / killed
- median_difference: 3.968568, permutation_p: 0, cohens_d: 0.9534
- bootstrap_ci_95: [2.829037, 5.291756], wilcoxon_p: 0
- n_bootstrap: 10000, n_paired: 49
- Notes: Superseded by bf16_importance_s025.

**bf16_ds_imp_s030** | DONE / killed
- median_difference: 9.943595, permutation_p: 0, cohens_d: 1.1263
- bootstrap_ci_95: [8.391554, 16.652865], wilcoxon_p: 0
- n_bootstrap: 10000, n_paired: 49
- Notes: Superseded by bf16_importance_s030.

**bf16_ds_imp_s035** | DONE / success
- verdict: PASS, problems: 50
- II_high_sparsity_median: 0.1051, II_high_sparsity_mean: 1.4309
- II_low_sparsity_median: 28.7649, II_low_sparsity_mean: 104.1892
- II_mid_sparsity_median: 4.9542, II_mid_sparsity_mean: 20.326
- tokens: high=21086, low=27748, mid=13306
- ci_overlap_test: low vs mid CI non-overlapping at 0.35

---

### GROUP 4: bf16_ds_rand (4 experiments) — DeepSeek bf16, random masking (control)

**bf16_ds_rand_s015** | DONE / success
- interaction_index: high(mean=0.22, median=0.093, ci=[-1.01,1.52], skew=-5.4), mid(mean=-3.36, median=0.097, ci=[-8.41,0.37], skew=-10.56), low(mean=-1.90, median=0.103, ci=[-4.97,0.27], skew=-11.57)
- perplexity: high_both=5.7569, mid_both=11.3156, low_both=6.2886
- pass_fail: FAIL, median_difference: 0.0095
- Notes: Verdict PASS-&gt;FAIL corrected. Median II all in 0.09-0.10 range, CI fully overlap, no structured gradient.

**bf16_ds_rand_s020** | DONE / success
- interaction_index: high(mean=1.12, median=0.292, skew=9.59), mid(mean=-1.58, median=0.350, skew=-12.31), low(mean=-0.41, median=0.276, skew=-10.07)
- perplexity: high_both=8.8129, mid_both=11.4974, low_both=9.2001
- pass_fail: FAIL, median_difference: -0.0155
- Notes: Verdict PASS-&gt;FAIL corrected. Median II in 0.28-0.35 range, CI fully overlap.

**bf16_ds_rand_s025** | DONE / success
- interaction_index: high(mean=3.59, median=0.818, skew=-7.57), mid(mean=-1.85, median=0.932, skew=-12.76), low(mean=0.72, median=1.363, skew=-15.85)
- perplexity: high_both=17.7423, mid_both=29.4661, low_both=17.9694
- pass_fail: FAIL, median_difference: 0.5445
- Notes: Verdict PASS-&gt;FAIL corrected. Median II in 0.82-1.36 range, CI fully overlap.

**bf16_ds_rand_s030** | DONE / success
- interaction_index: high(mean=7.56, median=2.503, ci=[4.41,11.62]), mid(mean=6.25, median=2.592, ci=[2.18,10.48]), low(mean=6.83, median=4.041, ci=[3.24,10.70])
- perplexity: high_both=40.7553, mid_both=62.4422, low_both=37.6009
- pass_fail: FAIL, median_difference: 1.5383
- Notes: Three phase median II in 2.50-4.04, median CI fully overlap, no structured gradient.

---

### GROUP 5: bf16_qw_imp (6 experiments) — Qwen bf16, importance masking

**bf16_qw_imp_s010** | DONE / success
- overall_verdict: PASS, ci_overlap_test: PASS, sign_reversal_test: FAIL
- high_sparsity_II_median: 0.0001, high_sparsity_II_mean: -0.0887
- mid_sparsity_II_median: -0.0359, mid_sparsity_II_mean: -0.084
- low_sparsity_II_median: -0.0444, low_sparsity_II_mean: -0.2431
- ppl: high_dense=1.074, high_both=1.228, mid_dense=1.133, mid_both=1.741, low_dense=1.152, low_both=3.204

**bf16_qw_imp_s015** | DONE / success
- median_difference: 0.047619, permutation_p: 0.0001, cohens_d: 0.3705
- bootstrap_ci_95: [-0.005077, 0.109517], wilcoxon_p: 0.02958
- n_bootstrap: 10000, n_paired: 46
- Notes: Weak gradient, consistent with DeepSeek at s=0.15. PPL(both): high=1.31, mid=2.20, low=5.44.

**bf16_qw_imp_s020** | DONE / success
- median_difference: 0.207511, permutation_p: 0, cohens_d: 0.7224
- bootstrap_ci_95: [0.067222, 0.40226], wilcoxon_p: 3.4e-05
- n_bootstrap: 10000, n_paired: 46
- Notes: PPL(both): high=1.37, mid=3.43, low=9.20. Low phase II distinctly elevated.

**bf16_qw_imp_s025** | DONE / success
- median_difference: 1.108706, permutation_p: 0, cohens_d: 1.2329
- bootstrap_ci_95: [0.609247, 1.469002], wilcoxon_p: 0
- n_bootstrap: 10000, n_paired: 46
- Notes: PPL(both): high=1.54, mid=5.36, low=16.96. Strong gradient, mid phase becomes significant.

**bf16_qw_imp_s030** | DONE / success
- median_difference: 2.619385, permutation_p: 0, cohens_d: 1.4394
- bootstrap_ci_95: [1.722281, 3.651063], wilcoxon_p: 0
- n_bootstrap: 10000, n_paired: 46
- Notes: PPL(both): high=1.86, mid=9.48, low=35.32. Strongest gradient, fully replicates DeepSeek pattern.

**bf16_qw_imp_s035** | DONE / success
- overall_verdict: PASS, ci_overlap_test: PASS, sign_reversal_test: FAIL
- high_sparsity_II_median: 0.0232, high_sparsity_II_mean: 0.1643
- mid_sparsity_II_median: 0.9577, mid_sparsity_II_mean: 8.0734
- low_sparsity_II_median: 8.2358, low_sparsity_II_mean: 18.9673
- ppl: high_dense=1.074, high_both=2.344, mid_dense=1.133, mid_both=20.991, low_dense=1.152, low_both=58.036

---

### GROUP 6: bf16_qw_rand (4 experiments) — Qwen bf16, random masking (control)

**bf16_qw_rand_s015** | DONE / success
- median II: high=0.138, mid=0.219, low=0.188 — no structured gradient
- median_difference: -0.029401, permutation_p: 0.7657, cohens_d: -0.0507
- bootstrap_ci_95: [-0.2106, 0.2124], wilcoxon_p: 0.862554
- pass_fail: FAIL

**bf16_qw_rand_s020** | DONE / success
- phase_median_ii: high=0.474, mid=0.876, low=0.485
- median_difference: 0.128948, permutation_p: 0.352, cohens_d: 0.247
- bootstrap_ci_95: [-0.139, 0.215], wilcoxon_p: 0.149
- pass_fail: FAIL

**bf16_qw_rand_s025** | DONE / success
- phase_median_ii: high=1.604, mid=2.222, low=2.264
- median_difference: 1.144074, permutation_p: 0.1679, cohens_d: 0.1574
- bootstrap_ci_95: [-0.3166, 4.1645], wilcoxon_p: 0.010313
- pass_fail: FAIL

**bf16_qw_rand_s030** | DONE / success
- median_high: 4.200557, median_mid: 6.477036, median_low: 8.065662
- median_diff: 2.418272, permutation_p: 0.012, cohens_d: -0.03513, wilcoxon_p: 0.01566
- bootstrap_ci_low: 0.241897, bootstrap_ci_high: 3.314824
- Notes: D043 re-bootstrap confirmed PASS-&gt;FAIL. gradient CI [-1.54, 13.71] includes 0, p=0.111. Random masking now 8/8 FAIL across both models.

---

### GROUP 7: bf16_importance (early) (4 experiments) — DeepSeek bf16, importance masking (canonical)

**bf16_importance_s015** | DONE / success
- interaction_index: high(mean=-0.150, median=0.006, skew=-14.99), mid(mean=0.447, median=0.081, skew=4.72), low(mean=2.406, median=0.398, skew=9.54)
- perplexity: high_both=1.5911, mid_both=3.4541, low_both=12.5084
- gradient_paired_aggregate_legacy: 69.24, median_difference: 0.3925
- pass_fail: PASS (CI non-overlap + sign reversal)

**bf16_importance_s020** | DONE / success
- interaction_index: high(mean=0.129, median=0.015, skew=16.67), mid(mean=1.260, median=0.203, skew=7.05), low(mean=6.029, median=1.496, skew=6.01)
- perplexity: high_both=2.1047, mid_both=5.4246, low_both=23.74
- gradient_paired_aggregate_legacy: 5.90, median_difference: 1.4818
- pass_fail: PASS

**bf16_importance_s025** | DONE / success
- interaction_index: high(mean=0.303, median=0.032, skew=4.88), mid(mean=5.730, median=1.118, skew=8.28), low(mean=25.853, median=7.196, skew=7.40)
- perplexity: high_both=2.7026, mid_both=13.3436, low_both=63.668
- gradient_paired_aggregate_legacy: 222.35, median_difference: 7.1636
- pass_fail: PASS

**bf16_importance_s030** | DONE / success
- interaction_index: high(mean=0.555, median=0.053, skew=10.62), mid(mean=11.30, median=2.283, skew=9.19), low(mean=57.795, median=14.640, skew=8.31)
- perplexity: high_both=3.2372, mid_both=24.2847, low_both=122.61
- gradient_paired_aggregate_legacy: 57.24, median_difference: 14.5861
- pass_fail: PASS
- Notes: 4-point median sequence perfectly monotonic: s015(0.40)-&gt;s020(1.50)-&gt;s025(7.20)-&gt;s030(14.64). PPL sequence also monotonic: 12.51-&gt;23.74-&gt;63.67-&gt;122.61.

---

### GROUP 8: bf16_random (early) (4 experiments) — all killed, superseded

**bf16_random_s015** | killed — superseded by bf16_ds_rand_s015
**bf16_random_s020** | killed — superseded by bf16_ds_rand_s020
**bf16_random_s025** | killed — superseded by bf16_ds_rand_s025
**bf16_random_s030** | killed — superseded by bf16_ds_rand_s030

---

### GROUP 9: bf16_qwen_importance (early) (4 experiments) — all killed, superseded

**bf16_qwen_importance_s015** | killed — superseded by bf16_qw_imp_s015
**bf16_qwen_importance_s020** | killed — superseded by bf16_qw_imp_s020
**bf16_qwen_importance_s025** | killed — superseded by bf16_qw_imp_s025
**bf16_qwen_importance_s030** | killed — superseded by bf16_qw_imp_s030

---

### GROUP 10: n500_unified (4 experiments) — n=500 statistical power boost

**c2_ds_n500** | killed — DUPLICATE, actual experiment in c2_n500_deepseek.

**c2_n500_deepseek** | DONE / success — DeepSeek, n=500
- effective_n: 496, mid_null_rate: 0.102
- **Importance (all p=0):**
  - s015: median_ii=0.3907, ci=[0.3496, 0.4431], wilcoxon_p=1.27e-70
  - s020: median_ii=1.2149, ci=[1.1072, 1.3365], wilcoxon_p=3.98e-75
  - s025: median_ii=3.9857, ci=[3.5272, 4.3588], wilcoxon_p=1.99e-78
  - s030: median_ii=8.4813, ci=[7.7543, 9.6919], wilcoxon_p=1.09e-79
- **Random (controls):**
  - s015: median_ii=0.0139, wilcoxon_p=0.863
  - s020: median_ii=0.0315, wilcoxon_p=0.28
  - s025: median_ii=0.2574, bonf_p=0.005839, fdr_p=0.001914
  - s030: median_ii=0.5096, bonf_p=0.005903, fdr_p=0.001914
- Effect sizes (dz): s015-s020=-0.925, s020-s025=-0.824, s025-s030=-0.773, s015-s030=-0.944
- all_dz_reliable: True, dose_response_monotonic: True, dose_response_spearman_rho: 1, dose_response_perm_p: 0.0417
- imp_rand_ratio_range: 15.5-38.6x, bonferroni_k: 4

**c2_qw_n500** | DONE / failed — process alive but conclusion=failed. s015 complete, s020+ in progress.

**c2_qw_n500_r3** | DONE / success — Qwen, n=500
- effective_n: 475, mid_null_rate: 0.452
- **Importance (all p &lt; 1e-14):**
  - s015: median_ii=0.0659, ci=[0.0492, 0.0925], wilcoxon_p=8.66e-15, bonf_p=3.46e-14
  - s020: median_ii=0.3073, ci=[0.2612, 0.3564], wilcoxon_p=6.84e-42, bonf_p=2.74e-41
  - s025: median_ii=1.0745, ci=[0.9766, 1.1787], wilcoxon_p=1.06e-68, bonf_p=4.25e-68
  - s030: median_ii=3.155, ci=[2.7834, 3.5582], wilcoxon_p=9.21e-74, bonf_p=3.69e-73
- **Random (controls):**
  - s015: median_ii=-0.0111, wilcoxon_p=0.172, bonf_p=0.687
  - s020: median_ii=0.0153, wilcoxon_p=0.2, bonf_p=0.8
  - s025: median_ii=0.3931, wilcoxon_p=1.59e-11, bonf_p=6.37e-11
  - s030: median_ii=0.9127, wilcoxon_p=2.92e-15, bonf_p=1.17e-14
- Effect sizes (dz): s015-s020=-0.629, s020-s025=-0.865, s025-s030=-0.767, s015-s030=-0.923
- all_dz_reliable: True, dose_response_monotonic: True, dose_response_spearman_rho: 1, dose_response_perm_p: 0.0417
- imp_rand_ratio_range: 2.7-20.1x, bonferroni_k: 4

---

### GROUP 11: mvp_v5_fixed (6 experiments) — DeepSeek fp16, importance masking, early version

**mvp_v5_fixed_s015** | DONE / negative
- ii_high_median: 0.205, ii_mid_median: 0.696, ii_low_median: 2.627
- both_ppl: high=2.284, mid=3.941, low=16.999, problems=50

**mvp_v5_fixed_s020** | DONE / killed — WARNING: pre-fix code, INVALIDATED
- ii_high_median: 0.33, ii_mid_median: 1.55, ii_low_median: 9.56
- both_ppl: high=2.7, mid=8.13, low=42.64

**mvp_v5_fixed_s020_r2** | DONE / negative
- ii_high_median: 0.3333, ii_mid_median: 1.5479, ii_low_median: 9.5627
- both_ppl: high=2.7, mid=8.13, low=42.64, problems=50

**mvp_v5_fixed_s025** | DONE / negative
- ii_high_median: 0.584, ii_mid_median: 4.522, ii_low_median: 30.903
- both_ppl: high=3.462, mid=16.415, low=104.175, problems=50

**mvp_v5_fixed_s030** | DONE / killed — WARNING: pre-fix code, INVALIDATED
- ii_high_median: 0.6, ii_mid_median: 7.47, ii_low_median: 44.63
- both_ppl: high=5.71, mid=137.61, low=963.2

**mvp_v5_fixed_s030_r2** | DONE / negative
- ii_high_median: 0.5964, ii_mid_median: 7.4671, ii_low_median: 44.6324
- both_ppl: high=5.71, mid=137.61, low=963.2, problems=50

---

### GROUP 12: mvp_v5_random (4 experiments) — DeepSeek fp16, random masking (control), early version

**mvp_v5_random_s015** | DONE / success
- ii_high_median: 0.1606, ii_mid_median: 0.252, ii_low_median: 0.1831
- both_ppl: high=3.92, mid=4.14, low=4.71, problems=50

**mvp_v5_random_s020** | DONE / success
- ii_high_median: 0.321331, ii_mid_median: 0.455663, ii_low_median: 0.591916
- both_ppl: high=7.975, mid=6.855, low=22.587, problems=50

**mvp_v5_random_s025** | DONE / success
- ii_high_median: 3.002, ii_mid_median: 2.985, ii_low_median: 2.915
- both_ppl: high=17.06, mid=15.38, low=29.32, problems=50

**mvp_v5_random_s030** | DONE / success
- ii_high_median: 5.378, ii_mid_median: 5.886, ii_low_median: 3.777
- both_ppl: high=41.35, mid=24.20, low=68.53, problems=50

---

### GROUP 13: mvp_v4_legacy (2 experiments) — DeepSeek, very early version

**mvp_v4_legacy_s01** | DONE / negative
- II_high: mean=-0.11, ci=[-0.81, 0.41]; II_mid: mean=-15.97, ci=[-47.99, 1.29]; II_low: mean=0.00
- ppl: high_both=22.13, mid_both=47.59, verdict: FAIL
- Notes: Sparsity too low, II near zero or negative.

**mvp_v4_legacy_s02** | DONE / success
- ii_high: mean=21.29, ci=[0.03, 63.16]; ii_mid: mean=21.87, ci=[4.99, 41.79]; ii_low: mean=0.00
- ppl: high(dense=1.15, kv=104.42, both=63.41), mid(dense=1.12, kv=324.16, both=170.47), low(dense=1.11, kv=1.11, both=1.30)
- mvp_verdict: PASS

---

### GROUP 14: Other PPL-related experiments (7 experiments)

**acc_ds_s020_8k_v2** | DONE / success — accuracy eval at s=0.20, max_tokens=8192
- accuracy: 0.30, correct: 15/50, truncated_rate: 0.58

**acc_ds_s025_8k_v2** | DONE / negative — accuracy eval at s=0.25
- accuracy: 0.08, correct: 4/50, truncated_rate: 0.76

**acc_ds_s030_8k_v2** | RUNNING — accuracy eval at s=0.30, no metrics yet

**c2_accuracy_eval** | DONE / success — accuracy dose curve (DS + Qwen)
- ds_dense_acc: 0.52, ds_s015_acc: 0.36 (delta=-0.16), ds_s030_acc: 0.10 (delta=-0.42)
- qw_dense_acc: 0.32, qw_s015_acc: 0.34 (delta=+0.02), qw_s030_acc: 0.14 (delta=-0.18)
- ds_s030_chinese_reasoning_rate: 0.4, ds_dense_truncation_rate: 0.56

**gsm8k_profiling_ds** | DONE / success — GSM8K transferability (DeepSeek)
- importance: s015(median_grad=0.241, p=0.0003), s020(0.74, p=0.0001), s025(1.992, p=0.0001), s030(4.682, p=0.0001)
- imp_rand_ratio: s015=2.3x, s020=2.5x, s025=3.8x, s030=2.8x
- dose_response_monotonic: True

**gsm8k_qw_rand_s025_v2** | DONE / success — GSM8K Qwen random s=0.25
- verdict: PASS, high_ii_median: 0.718, mid_ii_median: 1.127, low_ii_median: 1.459

**gsm8k_qw_rand_s030_v2** | DONE / success — GSM8K Qwen random s=0.30
- verdict: PASS, high_ii_median: 2.31, mid_ii_median: 2.70, low_ii_median: 5.20

---

## Key Takeaways

**Total: 65 experiments** across 14 groups. Of these:
- 8 killed/superseded (bf16_random_s015-s030, bf16_qwen_importance_s015-s030)
- 2 killed/superseded (c2_ds_n500, v6_random_s030, v6_random_s030_r2)
- 1 RUNNING (acc_ds_s030_8k_v2)
- Remaining ~54 have valid metrics

**Canonical dose curve data (bf16, paper-quality):**
- DeepSeek importance: bf16_importance_s015 through s030 — all PASS, median_diff monotonic: 0.39 -&gt; 1.48 -&gt; 7.16 -&gt; 14.59
- DeepSeek random: bf16_ds_rand_s015 through s030 — all FAIL (expected)
- Qwen importance: bf16_qw_imp_s015 through s030 — all PASS, median_diff: 0.048 -&gt; 0.208 -&gt; 1.109 -&gt; 2.619, cohens_d: 0.37 -&gt; 0.72 -&gt; 1.23 -&gt; 1.44
- Qwen random: bf16_qw_rand_s015 through s030 — all FAIL (expected)
- n=500 unified: c2_n500_deepseek + c2_qw_n500_r3 — dose_response_monotonic=True for both, spearman_rho=1.0, all importance conditions p &lt; 1e-14&lt;/result>
&lt;usage>&lt;total_tokens>56370&lt;/total_tokens>&lt;tool_uses>17&lt;/tool_uses>&lt;duration_ms>244987&lt;/duration_ms>&lt;/usage>
&lt;/task-notification>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a81eda25-58e7-4acf-83fb-2714cd6ec3cd",
  "isSidechain": false,
  "promptId": "e800486a-5431-4863-a090-6fe9e6a2f0b9",
  "type": "user",
  "uuid": "8cf392cd-6650-4bc4-9b31-fa20f8eb3ffb",
  "permissionMode": "bypassPermissions",
  "origin": {
    "kind": "task-notification"
  },
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "sessionId": "38576691-e177-4a18-ab23-be69eff4b7ff",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 56 · 2026-05-16T00:31:03.315Z_

<details><summary>Logged reasoning block</summary>

```text
All 4 agents have completed. Now I have all the data I need to compile the Round 10 data summary. Let me organize everything and write the comprehensive summary document.

Let me compile all the evidence:

## 1. PPL Dose Curve (n=500, DS + QW)

**DeepSeek (n=496, c2_n500_deepseek):**
| Sparsity | Importance median II | CI | Wilcoxon p | Random median II | Random p |


|----------|---------------------|------|-----------|-----------------|----------|
| s015 | 0.3907 | [0.3496, 0.4431] | 1.27e-70 | 0.0139 | 0.863 (NS) |
| s020 | 1.2149 | [1.1072, 1.3365] | 3.98e-75 | 0.0315 | 0.28 (NS) |
| s025 | 3.9857 | [3.5272, 4.3588] | 1.99e-78 | 0.2

Compiling the metrics table... Generating markdown table... Now I'm looking at the accuracy results across different sparsity levels for the QW model with 100 samples—there's a clear performance degradation, with a dramatic drop-off between the s025 and s030 conditions where accuracy plummets by 14 percentage points. I'm also starting to examine the DS accuracy metrics from the 8k v2 dataset, though that table appears to be cut off. Looking at the performance metrics across different model configurations, I'm seeing consistent dose-response patterns where importance gradients scale monotonically with model capacity. The QW random variants both pass their validation checks with increasing median II values across phases, and the asymmetric sparsity analysis reveals an inverse relationship between low-phase importance and high-phase importance across the two configurations.

The pre-registered criterion holds up, and I'm verifying the gradient direction remains robust even under asymmetric allocation schemes. I need to note that the G× correction factor was reconstructed from my memory since it wasn't in the original registry—the corrected range is 21-64× compared to the older 58-241×. The Mann-Whitney U reanalysis with n=475 shows significant effects across all QW importance conditions after the D066 revision, with the Bonferroni-corrected p-value around 0.006 for the random conditions. The entropy analysis in the discrimination collapse condition shows consistently negative importance entropy shifts, suggesting the model's ability to differentiate between conditions is degrading.

Looking at the cross-architecture results with Llama, the phase gradient stays stable around 1.0 across sparsity levels, but the interaction between importance and random conditions is weak and only reaches significance at s030. The random baseline itself shows a significant phase gradient, which complicates the interpretation of whether the effect is truly architecture-dependent. For the phase-gated controller pilot, the oracle recovery rate is 18% with strong statistical support.

Now I'm compiling these results into a comprehensive markdown document and mapping out the key claims against their supporting evidence—tracking which experiments validate strategy modulation, phase effects, crossover interactions, and the discrimination collapse pattern. Looking at the onset patterns, I'm seeing that the Qwen model shows confidence intervals near zero at smaller sample sizes but becomes statistically significant once we reach n=475, while the dose-response relationship holds perfectly monotonic across both models with a Spearman correlation of 1.0. There are several important caveats though: the DeepSeek accuracy numbers are likely underestimated due to truncation effects, some of the Qwen variants haven't been rescored yet, the entropy mechanism behaves differently depending on the model, and the LLaMA results show weaker improvements than expected.

I'm also tracking that the accuracy measurements for both s015 and s030 at 8k tokens are still running, and I need to compute the correction values post-hoc since they're not in the registry yet, plus complete the rescoring for the Qwen batch variants.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8cf392cd-6650-4bc4-9b31-fa20f8eb3ffb",
  "isSidechain": false,
  "requestId": "req_011Cb5JZ9v9vL4W1SteC5o1r",
  "type": "assistant",
  "uuid": "ba8000e4-c5fb-47c2-9201-bbafa42ef25d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "sessionId": "38576691-e177-4a18-ab23-be69eff4b7ff",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01356DMGSb6q5LdhmmqHUN9N",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 9516,
      "cache_read_input_tokens": 49615,
      "output_tokens": 8597,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 9516,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 8597,
          "cache_read_input_tokens": 49615,
          "cache_creation_input_tokens": 9516,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 9516
          },
          "type": "message"
        }
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

_source line 57 · 2026-05-16T00:31:03.376Z_

All 4 agents complete. Compiling the summary now.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ba8000e4-c5fb-47c2-9201-bbafa42ef25d",
  "isSidechain": false,
  "requestId": "req_011Cb5JZ9v9vL4W1SteC5o1r",
  "type": "assistant",
  "uuid": "5345974c-331d-400a-b544-159cf14f4b6a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "sessionId": "38576691-e177-4a18-ab23-be69eff4b7ff",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01356DMGSb6q5LdhmmqHUN9N",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 9516,
      "cache_read_input_tokens": 49615,
      "output_tokens": 8597,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 9516,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 8597,
          "cache_read_input_tokens": 49615,
          "cache_creation_input_tokens": 9516,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 9516
          },
          "type": "message"
        }
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

_source line 58 · 2026-05-16T00:32:32.725Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__save_project_file · `toolu_01NrncfDRsHpaBqs39hsZTsm`</summary>

```json
{
  "project": "phase-gated-compound-sparse",
  "file": "round10_data_summary.md",
  "content": "# Round 10 Data Summary — All Experimental Evidence\n\n> Compiled: 2026-05-16 | EMNLP 2026 ARR deadline: 2026-05-25\n\n---\n\n## 1. PPL Dose Curve\n\n### 1a. n=500 Unified Analysis (canonical)\n\n**DeepSeek (c2_n500_deepseek, n=496)**\n\n| Sparsity | Imp median II | 95% CI | Wilcoxon p | Rand median II | Rand p (Bonf k=4) |\n|----------|--------------|--------|------------|---------------|-------------------|\n| s015 | 0.3907 | [0.350, 0.443] | 1.27e-70 | 0.0139 | 0.863 (NS) |\n| s020 | 1.2149 | [1.107, 1.337] | 3.98e-75 | 0.0315 | 0.280 (NS) |\n| s025 | 3.9857 | [3.527, 4.359] | 1.99e-78 | 0.2574 | 0.0058 ** |\n| s030 | 8.4813 | [7.754, 9.692] | 1.09e-79 | 0.5096 | 0.0059 ** |\n\n- Imp/rand ratio: 15.5–38.6×\n- Adjacent d_z: s015→s020 = −0.925, s020→s025 = −0.824, s025→s030 = −0.773\n- Spearman ρ = 1.0, permutation p = 0.0417\n- Dose-response monotonic: ✓\n\n**Qwen (c2_qw_n500_r3, n=475, low+high valid filter)**\n\n| Sparsity | Imp median II | 95% CI | Wilcoxon p | Bonf p | Rand median II | Rand Bonf p |\n|----------|--------------|--------|------------|--------|---------------|------------|\n| s015 | 0.0659 | [0.049, 0.093] | 8.66e-15 | 3.46e-14 | −0.0111 | 0.687 (NS) |\n| s020 | 0.3073 | [0.261, 0.356] | 6.84e-42 | 2.74e-41 | 0.0153 | 0.800 (NS) |\n| s025 | 1.0745 | [0.977, 1.179] | 1.06e-68 | 4.25e-68 | 0.3931 | 6.37e-11 *** |\n| s030 | 3.1550 | [2.783, 3.558] | 9.21e-74 | 3.69e-73 | 0.9127 | 1.17e-14 *** |\n\n- Imp/rand ratio: 2.7–20.1×\n- Adjacent d_z: s015→s020 = −0.629, s020→s025 = −0.865, s025→s030 = −0.767\n- Spearman ρ = 1.0, permutation p = 0.0417\n- Dose-response monotonic: ✓\n- Mid-null rate: 45.2% (filter: low+high valid only)\n\n### 1b. bf16 Paired Statistics (n≈50, per-problem)\n\n**DeepSeek importance (bf16_ds_imp_s015–s030)**\n\n| Sparsity | Paired median diff | Permutation p | Cohen's d_z | Wilcoxon p | n_paired |\n|----------|--------------------|--------------|-------------|------------|----------|\n| s015 | 0.3236 | 0 | 0.607 | 0 | 49 |\n| s020 | 1.1520 | 0 | 0.725 | 0 | 49 |\n| s025 | 3.9686 | 0 | 0.953 | 0 | 49 |\n| s030 | 9.9436 | 0 | 1.126 | 0 | 49 |\n\n**Qwen importance (bf16_qw_imp_s015–s030)**\n\n| Sparsity | Paired median diff | Permutation p | Cohen's d_z | Bootstrap CI | Wilcoxon p | n_paired |\n|----------|--------------------|--------------|-------------|-------------|------------|----------|\n| s015 | 0.0476 | 0.0001 | 0.371 | [−0.005, 0.110] | 0.030 | 46 |\n| s020 | 0.2075 | 0 | 0.722 | [0.067, 0.402] | 3.4e-5 | 46 |\n| s025 | 1.1087 | 0 | 1.233 | [0.609, 1.469] | 0 | 46 |\n| s030 | 2.6194 | 0 | 1.439 | [1.722, 3.651] | 0 | 46 |\n\n⚠️ QW s015 n=50 CI crosses zero [−0.005, 0.110]; resolved at n=475 (CI [0.049, 0.093], p=3.5e-14).\n\n**Random controls (bf16, both models):** All 8 conditions FAIL — no structured phase gradient. DS rand median II range 0.09–4.04; QW rand median II range 0.14–8.07. All permutation p > 0.01 or CI overlapping.\n\n### 1c. Boundary Sparsity (s010, s035)\n\n| Condition | II_low median | II_mid median | II_high median | Verdict |\n|-----------|--------------|--------------|----------------|---------|\n| DS imp s010 | 0.0151 | 0.0061 | 0.0027 | FAIL (near-zero II) |\n| DS imp s035 | 28.76 | 4.95 | 0.11 | PASS (extends monotonic) |\n| QW imp s010 | −0.0444 | −0.0359 | 0.0001 | FAIL (near-zero II) |\n| QW imp s035 | 8.24 | 0.96 | 0.02 | PASS (extends monotonic) |\n\n---\n\n## 2. QW Accuracy Dose Curve (MATH-500, n=100)\n\nSource: acc_qw_dense_n100, acc_qw_s015_n100, acc_qw_s020_n100_b2_fix, acc_qw_s025_n100_b2_fix, acc_qw_s030_n100\n\n| Sparsity | Accuracy | Correct/100 | Δ vs dense | Note |\n|----------|----------|-------------|-----------|------|\n| dense | 0.40 | 40 | — | |\n| s015 | 0.36 | 36 | −0.04 | |\n| s020 | 0.36 | 36 | −0.04 | b2_fix: +1 vs original (35→36) |\n| s025 | 0.33 | 33 | −0.07 | b2_fix: unchanged (33→33) |\n| s030 | 0.19 | 19 | −0.21 | steep cliff from s025 |\n\n- s015 ≈ s020 plateau (−4pp); cliff at s025→s030 (−14pp)\n- b2_fix used max_new_tokens=8192 for batch2; batch1 used 2048 (mismatch noted)\n- ⚠️ s015/s030/dense batch1 未走 v2 rescore; s020 v2 rescore confirmed no change\n\n---\n\n## 3. DS Accuracy (8k v2, n=50, 定性观察)\n\nSource: acc_ds_dense_8k_v2, acc_ds_s020_8k_v2, acc_ds_s025_8k_v2 + pending\n\n| Sparsity | Accuracy | Truncation Rate | Avg Tokens | Status |\n|----------|----------|-----------------|-----------|--------|\n| dense | 0.74 | 0.16 | 3126 | DONE |\n| s015 | — | — | — | **RUNNING** |\n| s020 | 0.30 | 0.58 | — | DONE |\n| s025 | 0.08 | 0.76 | 6344 | DONE |\n| s030 | — | — | — | **RUNNING** |\n\n**Caveat (D086):** Truncation rate 58–76% even at 8k tokens. DS under sparsity generates extremely long outputs; accuracy = lower bound under token budget constraint. 降为定性观察，不纳入统计检验。\n\n4k baseline for reference: ds_dense_acc=0.52 (truncation 56%), ds_s015_acc=0.36, ds_s030_acc=0.10.\n\n---\n\n## 4. GSM8K Cross-Benchmark (C10)\n\n### 4a. Importance Masking Phase Gradient\n\nSource: gsm8k_profiling_ds, gsm8k_profiling_qw\n\n| Model | s015 | s020 | s025 | s030 | Monotonic |\n|-------|------|------|------|------|-----------|\n| DS median gradient | 0.241 | 0.740 | 1.992 | 4.682 | ✓ |\n| DS CI | [0.077, 0.478] | [0.314, 1.119] | [0.933, 2.820] | [2.121, 10.557] | |\n| DS Wilcoxon p | 0.0003 | 0.0001 | 0.0001 | 0.0001 | |\n| QW median gradient | 0.039 | 0.158 | 1.100 | 2.092 | ✓ |\n\n### 4b. Strategy Specificity (imp/rand ratio)\n\n| Sparsity | Ratio (GSM8K) | Ratio (MATH-500) |\n|----------|--------------|-----------------|\n| s015 | 2.3× | 28.1× (DS) / 5.9× (QW) |\n| s020 | 2.5× | 38.6× (DS) / 20.1× (QW) |\n| s025 | 3.8× | 15.5× (DS) / 2.7× (QW) |\n| s030 | 2.8× | 16.6× (DS) / 3.5× (QW) |\n\nStrategy specificity ratio 从 MATH-500 的 15–36× 衰减至 GSM8K 的 2.3–3.8×（task-dependent）。\n\n### 4c. QW Random GSM8K (补全数据)\n\nSource: gsm8k_qw_rand_s025_v2, gsm8k_qw_rand_s030_v2\n\n| Condition | II_high median | II_mid median | II_low median | Verdict |\n|-----------|---------------|--------------|--------------|---------|\n| QW rand s025 | 0.718 | 1.127 | 1.459 | PASS |\n| QW rand s030 | 2.310 | 2.700 | 5.200 | PASS |\n\nRandom masking 在 GSM8K s025+s030 也产生 positive compound interaction（与 MATH-500 random FAIL 不同）。\n\n---\n\n## 5. Additional Evidence\n\n### 5a. sf5 Asymmetric Sparsity (sf5_asymmetric_spot)\n\n| Config | Head% | KV% | II_low | II_mid | II_high | D (low−high) |\n|--------|-------|-----|--------|--------|---------|-------------|\n| A | 0.20 | 0.30 | 19.51 | 6.05 | 0.38 | 19.13 |\n| B | 0.30 | 0.20 | 18.77 | 3.97 | 0.52 | 18.25 |\n\n- Phase gradient direction 完全稳健（D > 0 both configs）\n- KV sparsity 较高时 mid-phase II 更大（6.05 vs 3.97）\n- Head sparsity 较高时 high-phase II 略升（0.52 vs 0.38）\n- Pre-registered criterion: PASS\n\n### 5b. Appendix B G× Correction\n\n- 旧值: 58–241×\n- 修正值: **21–64×**（per-problem additive II + aggregate PPL 修正）\n- 计算脚本: `/root/autodl-tmp/pacs/compute_gx_final.py`\n- 来源: memory.md（未注册为独立实验）\n\n### 5c. Cross-Model Mann-Whitney U (n=475 reanalysis)\n\n- Qwen 从 n=274 (complete-case) 修正为 n=475 (low+high valid only)\n- 分析脚本: `analyze_n500_v2.py` → `n500_unified_final.{csv,json}`, `n500_full_statistics.md`\n- Bonferroni 修订 (D066): k=4 family-wise（原 k=48）\n- DS rand s025/s030: Bonf p ≈ 0.006（恢复为显著）\n- BH-FDR (48 tests): rand s025/s030 fdr_p = 0.0019\n- 所有 imp 条件 *** 在 n=475 下保持显著\n\n### 5d. c4_entropy — Discrimination Collapse Mechanism\n\n**DeepSeek (c4_entropy, 30 problems)**\n\n| Metric | s015 | s020 | s025 | s030 |\n|--------|------|------|------|------|\n| Imp entropy Δ | −0.040 | −0.047 | −0.045 | −0.044 |\n| Rand entropy Δ | +0.128 | +0.136 | +0.217 | +0.233 |\n| Imp Gini Δ | −0.030 | −0.040 | −0.065 | −0.081 |\n| Imp CV Δ | −0.564 | −0.774 | −1.287 | −1.665 |\n\n**Qwen (qwen_c4_entropy, 30 problems)**\n\n| Metric | s015 | s020 | s025 | s030 |\n|--------|------|------|------|------|\n| Imp entropy Δ | −0.073 | −0.076 | **+0.045** | −0.007 |\n| Rand entropy Δ | +0.084 | +0.090 | +0.217 | +0.197 |\n| Imp Gini Δ | −0.010 | −0.012 | −0.010 | −0.020 |\n| Imp CV Δ | −0.045 | −0.208 | −1.491 | −1.142 |\n\n**结论:** Gini/CV 下降跨模型一致（discrimination collapse confirmed）。Entropy redistribution DS 一致但 QW s025 方向反转（+0.045）— model-dependent，不作为主线机制。\n\n### 5e. c3_llama — Cross-Architecture Validation\n\n- Model: DeepSeek-R1-Distill-Llama-8B (LlamaForCausalLM)\n- 8/8 conditions complete (imp + rand × 4 sparsity)\n- Within-importance phase gradient: d_z ≈ 1.0 across all sparsity levels ✓\n- imp_vs_rand d_z: 0.19→0.26→0.29→0.34（仅 s030 Bonferroni p=0.029 显著）\n- Random also shows significant phase gradient (d_z 0.35→0.44, CI excludes zero)\n- Qualitative direction consistent; strategy×phase interaction weaker + architecture-dependent\n\n### 5f. c5b_pilot — Phase-Gated Controller\n\n| Metric | s025 |\n|--------|------|\n| Uniform median II | 1.0435 |\n| Oracle median II | 0.856 |\n| Oracle recovery | 18% (CI [−39, 45.8], p=0.002) |\n| Heuristic median II | 0.713 |\n| Heuristic recovery | 31.7% (CI [−22.8, 66], p=0.024) |\n| Gate criterion | oracle > 30% |\n| Gate result | **FAIL** |\n\nDirection correct (Wilcoxon significant) but effect size insufficient. → §8 Future Work.\n\n---\n\n## 6. Claim–Evidence Mapping\n\n| Claim | Status | Primary Evidence (exp_id) |\n|-------|--------|--------------------------|\n| C1: Strategy- & task-modulated severity | confirmed | c2_n500_deepseek, c2_qw_n500_r3 (imp/rand ratio 15–39× DS, 2.7–20× QW); gsm8k_profiling_ds/qw (ratio 衰减至 2.3–3.8×) |\n| C2: Phase-modulated (low > high) | confirmed | bf16_ds_imp_s015–s030 (0.32→9.94); bf16_qw_imp_s015–s030 (0.048→2.619); n500 confirms all p < 1e-14 |\n| C3: Phase-strategy crossover | confirmed | bf16_importance_s025 (imp low=7.196 > rand low=1.363; imp high=0.032 < rand high=0.818) |\n| C4: Discrimination collapse | partially | c4_entropy (DS: Gini/CV ✓, entropy ✓); qwen_c4_entropy (Gini/CV ✓, entropy ✗ at s025) |\n| C5: Cross-model generalization | confirmed | c2_n500_deepseek + c2_qw_n500_r3: ρ=1.0 both, QW magnitude ~1/4 DS |\n| C5b: Phase-aware mitigation | gate_failed | c5b_pilot: oracle 18% < 30% gate → future work |\n| C6: Sub-exponential growth | confirmed | Δ growth factors: 3.8×→4.8×→2.0× (递减) |\n| C7: n=500 dose-response | confirmed | c2_n500_deepseek (n=496) + c2_qw_n500_r3 (n=475): monotonic, ρ=1.0 |\n| C8: Cross-architecture (LLaMA) | partially | c3_llama: within-imp d_z≈1.0 ✓; imp_vs_rand weak (d_z 0.19–0.34); rand also shows gradient |\n| C10: Cross-benchmark (GSM8K) | confirmed | gsm8k_profiling_ds/qw: monotonic ✓; gsm8k_qw_rand_s025/s030_v2: random也显著 |\n| S3→C: Model-dependent onset | confirmed | QW s015 n=50 CI crosses zero; n=475 resolves (p=3.5e-14). DS significant from s015+ |\n| S7→C: Dose-response monotonicity | confirmed | Spearman ρ=1.0 both models (n=500), perm p=0.0417 |\n\n---\n\n## 7. Known Caveats\n\n1. **DS accuracy truncation-dominated**: 58–76% truncation even at 8k tokens. All DS accuracy = lower bound (D086).\n2. **QW batch mismatch**: b2_fix experiments used max_new_tokens=8192 vs batch1's 2048. Impact minimal (s020: +1, s025: 0).\n3. **QW s015 n=50 marginal**: bf16 CI [−0.005, 0.110] crosses zero. Resolved at n=475.\n4. **Entropy mechanism model-dependent**: Qwen s025 entropy reversed (+0.045). Paper uses discrimination collapse (Gini/CV) as primary mechanism.\n5. **LLaMA strategy×phase interaction weak**: d_z 0.19–0.34; random also shows phase gradient. Use \"suggests\"/\"partial support\" language.\n6. **GSM8K strategy specificity 衰减**: 2.3–3.8× vs MATH-500 15–36×. Phase gradient robust, magnitude ratio task-dependent.\n7. **c5b pilot gate failed**: Oracle 18% < 30%. CI crosses zero for both oracle and heuristic.\n8. **Bonferroni revision (D066)**: k=4 family-wise (revised from k=48). DS rand s025/s030 restored to significant.\n9. **G× correction**: Paper must update from 58–241× to 21–64×.\n\n---\n\n## 8. Missing / Pending Data\n\n| Item | Status | Impact |\n|------|--------|--------|\n| acc_ds_s015_8k_v2 | RUNNING | DS accuracy dose curve incomplete (3/5 points) |\n| acc_ds_s030_8k_v2 | RUNNING | DS accuracy dose curve incomplete (3/5 points) |\n| QW batch1 v2 rescore (s015/s030/dense) | Not started | Low priority: s020 v2 showed zero change |\n| G× values not in registry | Post-hoc computation | Reference compute_gx_final.py; values in memory.md |\n| GSM8K QW importance full metrics | In gsm8k_profiling_qw | Only summary values (0.039/0.158/1.1/2.092) without CI |\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5345974c-331d-400a-b544-159cf14f4b6a",
  "isSidechain": false,
  "requestId": "req_011Cb5JZ9v9vL4W1SteC5o1r",
  "type": "assistant",
  "uuid": "c15757fd-de4f-4194-8cb2-6f75062c2c7f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "sessionId": "38576691-e177-4a18-ab23-be69eff4b7ff",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01356DMGSb6q5LdhmmqHUN9N",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 9516,
      "cache_read_input_tokens": 49615,
      "output_tokens": 8597,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 9516,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 8597,
          "cache_read_input_tokens": 49615,
          "cache_creation_input_tokens": 9516,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 9516
          },
          "type": "message"
        }
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

_source line 59 · 2026-05-16T00:32:32.750Z_

<details><summary>↩ Tool result · `toolu_01NrncfDRsHpaBqs39hsZTsm`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"file 'round10_data_summary.md' is not writable via save_project_file. Writable: ['memory.md', 'paper_framing.md', 'writing_plan.yaml'].\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c15757fd-de4f-4194-8cb2-6f75062c2c7f",
  "isSidechain": false,
  "promptId": "e800486a-5431-4863-a090-6fe9e6a2f0b9",
  "type": "user",
  "uuid": "5f27ed9d-1240-4285-81df-2718b5174efe",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {}, \\\"error\\\": \\\"file 'round10_data_summary.md' is not writable via save_project_file. Writable: ['memory.md', 'paper_framing.md', 'writing_plan.yaml'].\\\", \\\"metadata\\\": {}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {}, \"error\": \"file 'round10_data_summary.md' is not writable via save_project_file. Writable: ['memory.md', 'paper_framing.md', 'writing_plan.yaml'].\", \"metadata\": {}}"
    }
  },
  "sourceToolAssistantUUID": "c15757fd-de4f-4194-8cb2-6f75062c2c7f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "sessionId": "38576691-e177-4a18-ab23-be69eff4b7ff",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 60_

```json
{
  "type": "last-prompt",
  "leafUuid": "5f27ed9d-1240-4285-81df-2718b5174efe",
  "sessionId": "38576691-e177-4a18-ab23-be69eff4b7ff"
}
```

---

### Runtime record

_source line 61_

```json
{
  "type": "ai-title",
  "aiTitle": "Compile Round 10 experiment evidence for ARR submission",
  "sessionId": "38576691-e177-4a18-ab23-be69eff4b7ff"
}
```

---

### Assistant

_source line 62 · 2026-05-16T00:32:36.248Z_

<details><summary>Logged reasoning block</summary>

```text
The save_project_file tool only allows writing memory.md, paper_framing.md, and writing_plan.yaml. I need to save this as an artifact instead, or write it directly to the artifacts directory.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5f27ed9d-1240-4285-81df-2718b5174efe",
  "isSidechain": false,
  "requestId": "req_011Cb5JjiZiVyei5mMXkhPhB",
  "type": "assistant",
  "uuid": "b410af22-3d88-4ac4-a4c0-1cfe8cf0957c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "sessionId": "38576691-e177-4a18-ab23-be69eff4b7ff",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HKsy8T2iaBH9K7HnAgRCej",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8679,
      "cache_read_input_tokens": 59131,
      "output_tokens": 185,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 8679,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 185,
          "cache_read_input_tokens": 59131,
          "cache_creation_input_tokens": 8679,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 8679
          },
          "type": "message"
        }
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

_source line 63 · 2026-05-16T00:32:37.191Z_

save_project_file doesn't support arbitrary files. Writing to the artifacts directory instead.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b410af22-3d88-4ac4-a4c0-1cfe8cf0957c",
  "isSidechain": false,
  "requestId": "req_011Cb5JjiZiVyei5mMXkhPhB",
  "type": "assistant",
  "uuid": "94d2de38-3c17-4854-b893-0ce468ada7a9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "sessionId": "38576691-e177-4a18-ab23-be69eff4b7ff",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HKsy8T2iaBH9K7HnAgRCej",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8679,
      "cache_read_input_tokens": 59131,
      "output_tokens": 185,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 8679,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 185,
          "cache_read_input_tokens": 59131,
          "cache_creation_input_tokens": 8679,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 8679
          },
          "type": "message"
        }
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

_source line 64 · 2026-05-16T00:32:38.750Z_

<details open><summary>🔧 Tool call — Bash · `toolu_013jgTGqC1WDmvWJDMLtdKrr`</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/",
  "description": "List artifacts directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "94d2de38-3c17-4854-b893-0ce468ada7a9",
  "isSidechain": false,
  "requestId": "req_011Cb5JjiZiVyei5mMXkhPhB",
  "type": "assistant",
  "uuid": "6dbed99b-21c5-4bba-96d4-b6074c6f095b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "sessionId": "38576691-e177-4a18-ab23-be69eff4b7ff",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HKsy8T2iaBH9K7HnAgRCej",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8679,
      "cache_read_input_tokens": 59131,
      "output_tokens": 185,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 8679,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 185,
          "cache_read_input_tokens": 59131,
          "cache_creation_input_tokens": 8679,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 8679
          },
          "type": "message"
        }
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

_source line 65 · 2026-05-16T00:32:38.823Z_

<details><summary>↩ Tool result · `toolu_013jgTGqC1WDmvWJDMLtdKrr`</summary>

```text
R9-C2
_project
analysis_pipeline_audit.md
analysis_pipeline_readiness.md
analysis_pipeline_verification.md
analyze_c2_n500.py
appendix_b_precise_gx
bf16_qw_imp_failures_diagnosis.md
bf16_qw_rand_s015
bf16_qw_rand_s020
bf16_qw_rand_s025
bf16_qw_rand_s030
bootstrap_phase_gradient.py
c2_n500_deepseek
c2_n500_paper_update_checklist.md
c2_progress_report.md
c2_progress_snapshot.json
c2_qw_n500_investigation.md
c3_llama
c3_llama_results.json
c5b_framing_proposal.md
c5b_pilot
c5b_pilot_design.md
c5b_pilot_diagnosis.md
compute_multiplicative_null.py
consistency_audit_final.md
consistency_audit_report.md
consistency_report.md
crossover_n500.csv
crossover_n500.md
dream_reports
exp_progress_check_20260516.md
gpu_check_loop7.md
gsm8k_diagnosis
gsm8k_importance_bug
gsm8k_profiling
gsm8k_profiling_ds
gsm8k_profiling_ds_diagnosis.md
gsm8k_token_length
literature_scan_20260515.md
literature_scan_phase_adaptive.md
m1_phase_segmentation_analysis.md
m2_figure1_n500
m2_m4_code_readiness.md
magnitude_crossover_novelty_check.md
main.pdf
main_r6_revised.pdf
main_r7_revised.pdf
manifest.yaml
math500_token_length
mechanistic_explanation.md
mid_sparsity_gap_analysis.md
mvp_ii_analysis.md
mvp_ii_profiling_v2
mvp_ii_profiling_v3
mvp_ii_v3_analysis.md
mvp_interaction_index_profiling
n1a_answer_region
n1a_boxed_validation
n500_analysis
n500_analysis_pipeline_ready.md
n500_analysis_readiness.md
n500_paper_patch_plan.md
n500_paper_update_FINAL.md
n500_paper_update_checklist.md
n500_paper_update_plan.md
n500_pipeline_check.md
n500_progress_20260515_0632.md
n500_progress_check.md
n500_update_checklist.md
novelty_evidence_summary.md
number_consistency_audit_v2.md
p1_appendix_b_null
p3_figure1
pacs
paper_n500_update_checklist.md
paper_n500_update_plan.md
paper_placeholder_audit.md
paper_update_checklist.md
qwen_kill_investigation.md
qwen_status_check.md
r8_citations
reference_audit.md
reference_audit_report.md
report_analysis_pipeline_ready.md
report_process_check.md
review_issues.yaml
review_reports
round10_data_compilation.md
think_phase_validation
v5_status_check.md
w1w5_audit_report.md
w4_pruned_head_overlap
w5_llama_power
w6_outlier_robustness
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6dbed99b-21c5-4bba-96d4-b6074c6f095b",
  "isSidechain": false,
  "promptId": "e800486a-5431-4863-a090-6fe9e6a2f0b9",
  "type": "user",
  "uuid": "9c96fa42-0a8c-4d70-bb2d-87c9d784bcb8",
  "toolUseResult": {
    "stdout": "R9-C2\n_project\nanalysis_pipeline_audit.md\nanalysis_pipeline_readiness.md\nanalysis_pipeline_verification.md\nanalyze_c2_n500.py\nappendix_b_precise_gx\nbf16_qw_imp_failures_diagnosis.md\nbf16_qw_rand_s015\nbf16_qw_rand_s020\nbf16_qw_rand_s025\nbf16_qw_rand_s030\nbootstrap_phase_gradient.py\nc2_n500_deepseek\nc2_n500_paper_update_checklist.md\nc2_progress_report.md\nc2_progress_snapshot.json\nc2_qw_n500_investigation.md\nc3_llama\nc3_llama_results.json\nc5b_framing_proposal.md\nc5b_pilot\nc5b_pilot_design.md\nc5b_pilot_diagnosis.md\ncompute_multiplicative_null.py\nconsistency_audit_final.md\nconsistency_audit_report.md\nconsistency_report.md\ncrossover_n500.csv\ncrossover_n500.md\ndream_reports\nexp_progress_check_20260516.md\ngpu_check_loop7.md\ngsm8k_diagnosis\ngsm8k_importance_bug\ngsm8k_profiling\ngsm8k_profiling_ds\ngsm8k_profiling_ds_diagnosis.md\ngsm8k_token_length\nliterature_scan_20260515.md\nliterature_scan_phase_adaptive.md\nm1_phase_segmentation_analysis.md\nm2_figure1_n500\nm2_m4_code_readiness.md\nmagnitude_crossover_novelty_check.md\nmain.pdf\nmain_r6_revised.pdf\nmain_r7_revised.pdf\nmanifest.yaml\nmath500_token_length\nmechanistic_explanation.md\nmid_sparsity_gap_analysis.md\nmvp_ii_analysis.md\nmvp_ii_profiling_v2\nmvp_ii_profiling_v3\nmvp_ii_v3_analysis.md\nmvp_interaction_index_profiling\nn1a_answer_region\nn1a_boxed_validation\nn500_analysis\nn500_analysis_pipeline_ready.md\nn500_analysis_readiness.md\nn500_paper_patch_plan.md\nn500_paper_update_FINAL.md\nn500_paper_update_checklist.md\nn500_paper_update_plan.md\nn500_pipeline_check.md\nn500_progress_20260515_0632.md\nn500_progress_check.md\nn500_update_checklist.md\nnovelty_evidence_summary.md\nnumber_consistency_audit_v2.md\np1_appendix_b_null\np3_figure1\npacs\npaper_n500_update_checklist.md\npaper_n500_update_plan.md\npaper_placeholder_audit.md\npaper_update_checklist.md\nqwen_kill_investigation.md\nqwen_status_check.md\nr8_citations\nreference_audit.md\nreference_audit_report.md\nreport_analysis_pipeline_ready.md\nreport_process_check.md\nreview_issues.yaml\nreview_reports\nround10_data_compilation.md\nthink_phase_validation\nv5_status_check.md\nw1w5_audit_report.md\nw4_pruned_head_overlap\nw5_llama_power\nw6_outlier_robustness",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "6dbed99b-21c5-4bba-96d4-b6074c6f095b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "sessionId": "38576691-e177-4a18-ab23-be69eff4b7ff",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 66 · 2026-05-16T00:32:42.177Z_

<details><summary>Logged reasoning block</summary>

```text
There's already a `round10_data_compilation.md` file. Let me check it quickly and then decide whether to overwrite it or create a new one with a different name.

Actually, I should just write the comprehensive summary to the artifacts directory. Let me write it there.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9c96fa42-0a8c-4d70-bb2d-87c9d784bcb8",
  "isSidechain": false,
  "requestId": "req_011Cb5JkAZepASwfYDBwbVVp",
  "type": "assistant",
  "uuid": "5c6c820a-3132-481f-9205-cf5e57b30579",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "sessionId": "38576691-e177-4a18-ab23-be69eff4b7ff",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EAKHW5XgBL2hU61XMyrXGs",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1063,
      "cache_read_input_tokens": 67810,
      "output_tokens": 160,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1063,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 160,
          "cache_read_input_tokens": 67810,
          "cache_creation_input_tokens": 1063,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1063
          },
          "type": "message"
        }
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

_source line 67 · 2026-05-16T00:32:42.668Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01W2ueNocT33vrurFkpUGHio`</summary>

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
  "parentUuid": "5c6c820a-3132-481f-9205-cf5e57b30579",
  "isSidechain": false,
  "requestId": "req_011Cb5JkAZepASwfYDBwbVVp",
  "type": "assistant",
  "uuid": "aa82ae7d-b6b3-4603-94d5-4b58de058480",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "sessionId": "38576691-e177-4a18-ab23-be69eff4b7ff",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EAKHW5XgBL2hU61XMyrXGs",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1063,
      "cache_read_input_tokens": 67810,
      "output_tokens": 160,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1063,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 160,
          "cache_read_input_tokens": 67810,
          "cache_creation_input_tokens": 1063,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1063
          },
          "type": "message"
        }
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

_source line 68 · 2026-05-16T00:32:42.673Z_

<details><summary>↩ Tool result · `toolu_01W2ueNocT33vrurFkpUGHio`</summary>

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
  "parentUuid": "aa82ae7d-b6b3-4603-94d5-4b58de058480",
  "isSidechain": false,
  "promptId": "e800486a-5431-4863-a090-6fe9e6a2f0b9",
  "type": "user",
  "uuid": "3806b0c0-fdd1-4666-9afa-efc8178cadbb",
  "toolUseResult": {
    "matches": [
      "mcp__agent-ml-research__register_artifact"
    ],
    "query": "select:mcp__agent-ml-research__register_artifact",
    "total_deferred_tools": 25
  },
  "sourceToolAssistantUUID": "aa82ae7d-b6b3-4603-94d5-4b58de058480",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "sessionId": "38576691-e177-4a18-ab23-be69eff4b7ff",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 69 · 2026-05-16T00:34:10.391Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact · `toolu_01XhQkwD96KtNzN1JiEmwgcJ`</summary>

```json
{
  "name": "round10_data_summary",
  "type": "report",
  "description": "Round 10 完整数据编译：PPL dose curve (n=500), QW/DS accuracy, GSM8K cross-benchmark, sf5/entropy/LLaMA/pilot 补充证据，claim-evidence mapping，caveats 和 pending items",
  "project": "phase-gated-compound-sparse",
  "content_filename": "round10_data_summary.md",
  "tags": [
    "round10",
    "data-compilation",
    "emnlp2026"
  ],
  "content": "# Round 10 Data Summary — All Experimental Evidence\n\n> Compiled: 2026-05-16 | EMNLP 2026 ARR deadline: 2026-05-25\n\n---\n\n## 1. PPL Dose Curve\n\n### 1a. n=500 Unified Analysis (canonical)\n\n**DeepSeek (c2_n500_deepseek, n=496)**\n\n| Sparsity | Imp median II | 95% CI | Wilcoxon p | Rand median II | Rand p (Bonf k=4) |\n|----------|--------------|--------|------------|---------------|-------------------|\n| s015 | 0.3907 | [0.350, 0.443] | 1.27e-70 | 0.0139 | 0.863 (NS) |\n| s020 | 1.2149 | [1.107, 1.337] | 3.98e-75 | 0.0315 | 0.280 (NS) |\n| s025 | 3.9857 | [3.527, 4.359] | 1.99e-78 | 0.2574 | 0.0058 ** |\n| s030 | 8.4813 | [7.754, 9.692] | 1.09e-79 | 0.5096 | 0.0059 ** |\n\n- Imp/rand ratio: 15.5–38.6×\n- Adjacent d_z: s015→s020 = −0.925, s020→s025 = −0.824, s025→s030 = −0.773\n- Spearman ρ = 1.0, permutation p = 0.0417\n- Dose-response monotonic: ✓\n\n**Qwen (c2_qw_n500_r3, n=475, low+high valid filter)**\n\n| Sparsity | Imp median II | 95% CI | Wilcoxon p | Bonf p | Rand median II | Rand Bonf p |\n|----------|--------------|--------|------------|--------|---------------|------------|\n| s015 | 0.0659 | [0.049, 0.093] | 8.66e-15 | 3.46e-14 | −0.0111 | 0.687 (NS) |\n| s020 | 0.3073 | [0.261, 0.356] | 6.84e-42 | 2.74e-41 | 0.0153 | 0.800 (NS) |\n| s025 | 1.0745 | [0.977, 1.179] | 1.06e-68 | 4.25e-68 | 0.3931 | 6.37e-11 *** |\n| s030 | 3.1550 | [2.783, 3.558] | 9.21e-74 | 3.69e-73 | 0.9127 | 1.17e-14 *** |\n\n- Imp/rand ratio: 2.7–20.1×\n- Adjacent d_z: s015→s020 = −0.629, s020→s025 = −0.865, s025→s030 = −0.767\n- Spearman ρ = 1.0, permutation p = 0.0417\n- Dose-response monotonic: ✓\n- Mid-null rate: 45.2% (filter: low+high valid only)\n\n### 1b. bf16 Paired Statistics (n≈50, per-problem)\n\n**DeepSeek importance (bf16_ds_imp_s015–s030)**\n\n| Sparsity | Paired median diff | Permutation p | Cohen's d_z | Wilcoxon p | n_paired |\n|----------|--------------------|--------------|-------------|------------|----------|\n| s015 | 0.3236 | 0 | 0.607 | 0 | 49 |\n| s020 | 1.1520 | 0 | 0.725 | 0 | 49 |\n| s025 | 3.9686 | 0 | 0.953 | 0 | 49 |\n| s030 | 9.9436 | 0 | 1.126 | 0 | 49 |\n\n**Qwen importance (bf16_qw_imp_s015–s030)**\n\n| Sparsity | Paired median diff | Permutation p | Cohen's d_z | Bootstrap CI | Wilcoxon p | n_paired |\n|----------|--------------------|--------------|-------------|-------------|------------|----------|\n| s015 | 0.0476 | 0.0001 | 0.371 | [−0.005, 0.110] | 0.030 | 46 |\n| s020 | 0.2075 | 0 | 0.722 | [0.067, 0.402] | 3.4e-5 | 46 |\n| s025 | 1.1087 | 0 | 1.233 | [0.609, 1.469] | 0 | 46 |\n| s030 | 2.6194 | 0 | 1.439 | [1.722, 3.651] | 0 | 46 |\n\n⚠️ QW s015 n=50 CI crosses zero [−0.005, 0.110]; resolved at n=475 (CI [0.049, 0.093], p=3.5e-14).\n\n**Random controls (bf16, both models):** All 8 conditions FAIL — no structured phase gradient. DS rand median II range 0.09–4.04; QW rand median II range 0.14–8.07. All permutation p > 0.01 or CI overlapping.\n\n### 1c. Boundary Sparsity (s010, s035)\n\n| Condition | II_low median | II_mid median | II_high median | Verdict |\n|-----------|--------------|--------------|----------------|---------|\n| DS imp s010 | 0.0151 | 0.0061 | 0.0027 | FAIL (near-zero II) |\n| DS imp s035 | 28.76 | 4.95 | 0.11 | PASS (extends monotonic) |\n| QW imp s010 | −0.0444 | −0.0359 | 0.0001 | FAIL (near-zero II) |\n| QW imp s035 | 8.24 | 0.96 | 0.02 | PASS (extends monotonic) |\n\n---\n\n## 2. QW Accuracy Dose Curve (MATH-500, n=100)\n\nSource: acc_qw_dense_n100, acc_qw_s015_n100, acc_qw_s020_n100_b2_fix, acc_qw_s025_n100_b2_fix, acc_qw_s030_n100\n\n| Sparsity | Accuracy | Correct/100 | Δ vs dense | Note |\n|----------|----------|-------------|-----------|------|\n| dense | 0.40 | 40 | — | |\n| s015 | 0.36 | 36 | −0.04 | |\n| s020 | 0.36 | 36 | −0.04 | b2_fix: +1 vs original (35→36) |\n| s025 | 0.33 | 33 | −0.07 | b2_fix: unchanged (33→33) |\n| s030 | 0.19 | 19 | −0.21 | steep cliff from s025 |\n\n- s015 ≈ s020 plateau (−4pp); cliff at s025→s030 (−14pp)\n- b2_fix used max_new_tokens=8192 for batch2; batch1 used 2048 (mismatch noted)\n- ⚠️ s015/s030/dense batch1 未走 v2 rescore; s020 v2 rescore confirmed no change\n\n---\n\n## 3. DS Accuracy (8k v2, n=50, 定性观察)\n\nSource: acc_ds_dense_8k_v2, acc_ds_s020_8k_v2, acc_ds_s025_8k_v2 + pending\n\n| Sparsity | Accuracy | Truncation Rate | Avg Tokens | Status |\n|----------|----------|-----------------|-----------|--------|\n| dense | 0.74 | 0.16 | 3126 | DONE |\n| s015 | — | — | — | **RUNNING** |\n| s020 | 0.30 | 0.58 | — | DONE |\n| s025 | 0.08 | 0.76 | 6344 | DONE |\n| s030 | — | — | — | **RUNNING** |\n\n**Caveat (D086):** Truncation rate 58–76% even at 8k tokens. DS under sparsity generates extremely long outputs; accuracy = lower bound under token budget constraint. 降为定性观察，不纳入统计检验。\n\n4k baseline for reference: ds_dense_acc=0.52 (truncation 56%), ds_s015_acc=0.36, ds_s030_acc=0.10.\n\n---\n\n## 4. GSM8K Cross-Benchmark (C10)\n\n### 4a. Importance Masking Phase Gradient\n\nSource: gsm8k_profiling_ds, gsm8k_profiling_qw\n\n| Model | s015 | s020 | s025 | s030 | Monotonic |\n|-------|------|------|------|------|-----------|\n| DS median gradient | 0.241 | 0.740 | 1.992 | 4.682 | ✓ |\n| DS CI | [0.077, 0.478] | [0.314, 1.119] | [0.933, 2.820] | [2.121, 10.557] | |\n| DS Wilcoxon p | 0.0003 | 0.0001 | 0.0001 | 0.0001 | |\n| QW median gradient | 0.039 | 0.158 | 1.100 | 2.092 | ✓ |\n\n### 4b. Strategy Specificity (imp/rand ratio)\n\n| Sparsity | Ratio (GSM8K) | Ratio (MATH-500 DS) | Ratio (MATH-500 QW) |\n|----------|--------------|--------------------|--------------------|\n| s015 | 2.3× | 28.1× | 5.9× |\n| s020 | 2.5× | 38.6× | 20.1× |\n| s025 | 3.8× | 15.5× | 2.7× |\n| s030 | 2.8× | 16.6× | 3.5× |\n\nStrategy specificity ratio 从 MATH-500 的 15–36× 衰减至 GSM8K 的 2.3–3.8×（task-dependent）。\n\n### 4c. QW Random GSM8K (补全数据)\n\nSource: gsm8k_qw_rand_s025_v2, gsm8k_qw_rand_s030_v2\n\n| Condition | II_high median | II_mid median | II_low median | Verdict |\n|-----------|---------------|--------------|--------------|---------|\n| QW rand s025 | 0.718 | 1.127 | 1.459 | PASS |\n| QW rand s030 | 2.310 | 2.700 | 5.200 | PASS |\n\nRandom masking 在 GSM8K s025+s030 也产生 positive compound interaction（与 MATH-500 random FAIL 不同）。\n\n---\n\n## 5. Additional Evidence\n\n### 5a. sf5 Asymmetric Sparsity (sf5_asymmetric_spot)\n\n| Config | Head% | KV% | II_low | II_mid | II_high | D (low−high) |\n|--------|-------|-----|--------|--------|---------|-------------|\n| A | 0.20 | 0.30 | 19.51 | 6.05 | 0.38 | 19.13 |\n| B | 0.30 | 0.20 | 18.77 | 3.97 | 0.52 | 18.25 |\n\n- Phase gradient direction 完全稳健（D > 0 both configs）\n- KV sparsity 较高时 mid-phase II 更大（6.05 vs 3.97）\n- Head sparsity 较高时 high-phase II 略升（0.52 vs 0.38）\n- Pre-registered criterion: PASS\n\n### 5b. Appendix B G× Correction\n\n- 旧值: 58–241×\n- 修正值: **21–64×**（per-problem additive II + aggregate PPL 修正）\n- 计算脚本: `/root/autodl-tmp/pacs/compute_gx_final.py`\n- 来源: memory.md（未注册为独立实验）\n\n### 5c. Cross-Model Mann-Whitney U (n=475 reanalysis)\n\n- Qwen 从 n=274 (complete-case) 修正为 n=475 (low+high valid only)\n- 分析脚本: `analyze_n500_v2.py` → `n500_unified_final.{csv,json}`, `n500_full_statistics.md`\n- Bonferroni 修订 (D066): k=4 family-wise（原 k=48）\n- DS rand s025/s030: Bonf p ≈ 0.006（恢复为显著）\n- BH-FDR (48 tests): rand s025/s030 fdr_p = 0.0019\n- 所有 imp 条件 *** 在 n=475 下保持显著\n\n### 5d. c4_entropy — Discrimination Collapse Mechanism\n\n**DeepSeek (c4_entropy, 30 problems)**\n\n| Metric | s015 | s020 | s025 | s030 |\n|--------|------|------|------|------|\n| Imp entropy Δ | −0.040 | −0.047 | −0.045 | −0.044 |\n| Rand entropy Δ | +0.128 | +0.136 | +0.217 | +0.233 |\n| Imp Gini Δ | −0.030 | −0.040 | −0.065 | −0.081 |\n| Imp CV Δ | −0.564 | −0.774 | −1.287 | −1.665 |\n\n**Qwen (qwen_c4_entropy, 30 problems)**\n\n| Metric | s015 | s020 | s025 | s030 |\n|--------|------|------|------|------|\n| Imp entropy Δ | −0.073 | −0.076 | **+0.045** | −0.007 |\n| Rand entropy Δ | +0.084 | +0.090 | +0.217 | +0.197 |\n| Imp Gini Δ | −0.010 | −0.012 | −0.010 | −0.020 |\n| Imp CV Δ | −0.045 | −0.208 | −1.491 | −1.142 |\n\n**结论:** Gini/CV 下降跨模型一致（discrimination collapse confirmed）。Entropy redistribution DS 一致但 QW s025 方向反转（+0.045）— model-dependent，不作为主线机制。\n\n### 5e. c3_llama — Cross-Architecture Validation\n\n- Model: DeepSeek-R1-Distill-Llama-8B (LlamaForCausalLM)\n- 8/8 conditions complete (imp + rand × 4 sparsity)\n- Within-importance phase gradient: d_z ≈ 1.0 across all sparsity levels ✓\n- imp_vs_rand d_z: 0.19→0.26→0.29→0.34（仅 s030 Bonferroni p=0.029 显著）\n- Random also shows significant phase gradient (d_z 0.35→0.44, CI excludes zero)\n- Qualitative direction consistent; strategy×phase interaction weaker + architecture-dependent\n\n### 5f. c5b_pilot — Phase-Gated Controller\n\n| Metric | s025 |\n|--------|------|\n| Uniform median II | 1.0435 |\n| Oracle median II | 0.856 |\n| Oracle recovery | 18% (CI [−39, 45.8], p=0.002) |\n| Heuristic median II | 0.713 |\n| Heuristic recovery | 31.7% (CI [−22.8, 66], p=0.024) |\n| Gate criterion | oracle > 30% |\n| Gate result | **FAIL** |\n\nDirection correct (Wilcoxon significant) but effect size insufficient. → §8 Future Work.\n\n---\n\n## 6. Claim–Evidence Mapping\n\n| Claim | Status | Primary Evidence (exp_id) |\n|-------|--------|--------------------------|\n| C1: Strategy- and task-modulated severity | confirmed | c2_n500_deepseek, c2_qw_n500_r3 (imp/rand ratio 15–39× DS, 2.7–20× QW); gsm8k_profiling_ds/qw (ratio 衰减至 2.3–3.8×) |\n| C2: Phase-modulated (low > high) | confirmed | bf16_ds_imp_s015–s030 (0.32→9.94); bf16_qw_imp_s015–s030 (0.048→2.619); n500 confirms all p < 1e-14 |\n| C3: Phase-strategy crossover | confirmed | bf16_importance_s025 (imp low=7.196 > rand low=1.363; imp high=0.032 < rand high=0.818) |\n| C4: Discrimination collapse | partially | c4_entropy (DS: Gini/CV ✓, entropy ✓); qwen_c4_entropy (Gini/CV ✓, entropy ✗ at s025) |\n| C5: Cross-model generalization | confirmed | c2_n500_deepseek + c2_qw_n500_r3: ρ=1.0 both, QW magnitude ~1/4 DS |\n| C5b: Phase-aware mitigation | gate_failed | c5b_pilot: oracle 18% < 30% gate → future work |\n| C6: Sub-exponential growth | confirmed | Δ growth factors: 3.8×→4.8×→2.0× (递减) |\n| C7: n=500 dose-response | confirmed | c2_n500_deepseek (n=496) + c2_qw_n500_r3 (n=475): monotonic, ρ=1.0 |\n| C8: Cross-architecture (LLaMA) | partially | c3_llama: within-imp d_z≈1.0 ✓; imp_vs_rand weak (d_z 0.19–0.34); rand also shows gradient |\n| C10: Cross-benchmark (GSM8K) | confirmed | gsm8k_profiling_ds/qw: monotonic ✓; gsm8k_qw_rand_s025/s030_v2: random 也显著 |\n| S3→C: Model-dependent onset | confirmed | QW s015 n=50 CI crosses zero; n=475 resolves (p=3.5e-14). DS significant from s015+ |\n| S7→C: Dose-response monotonicity | confirmed | Spearman ρ=1.0 both models (n=500), perm p=0.0417 |\n\n---\n\n## 7. Known Caveats\n\n1. **DS accuracy truncation-dominated**: 58–76% truncation even at 8k tokens. All DS accuracy = lower bound (D086).\n2. **QW batch mismatch**: b2_fix experiments used max_new_tokens=8192 vs batch1's 2048. Impact minimal (s020: +1, s025: 0).\n3. **QW s015 n=50 marginal**: bf16 CI [−0.005, 0.110] crosses zero. Resolved at n=475.\n4. **Entropy mechanism model-dependent**: Qwen s025 entropy reversed (+0.045). Paper uses discrimination collapse (Gini/CV) as primary mechanism.\n5. **LLaMA strategy×phase interaction weak**: d_z 0.19–0.34; random also shows phase gradient. Use \"suggests\"/\"partial support\" language.\n6. **GSM8K strategy specificity 衰减**: 2.3–3.8× vs MATH-500 15–36×. Phase gradient robust, magnitude ratio task-dependent.\n7. **c5b pilot gate failed**: Oracle 18% < 30%. CI crosses zero for both oracle and heuristic.\n8. **Bonferroni revision (D066)**: k=4 family-wise (revised from k=48). DS rand s025/s030 restored to significant.\n9. **G× correction**: Paper must update from 58–241× to 21–64×.\n\n---\n\n## 8. Missing / Pending Data\n\n| Item | Status | Impact |\n|------|--------|--------|\n| acc_ds_s015_8k_v2 | RUNNING | DS accuracy dose curve incomplete (3/5 points) |\n| acc_ds_s030_8k_v2 | RUNNING | DS accuracy dose curve incomplete (3/5 points) |\n| QW batch1 v2 rescore (s015/s030/dense) | Not started | Low priority: s020 v2 showed zero change |\n| G× values not in registry | Post-hoc computation | Reference compute_gx_final.py; values in memory.md |\n| GSM8K QW importance full metrics | In gsm8k_profiling_qw | Only summary values (0.039/0.158/1.1/2.092) without CI |"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3806b0c0-fdd1-4666-9afa-efc8178cadbb",
  "isSidechain": false,
  "requestId": "req_011Cb5JkTTA5oXPjTvP7TXhk",
  "type": "assistant",
  "uuid": "314d51d9-187e-4d4e-a451-0ad8c52e7330",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "sessionId": "38576691-e177-4a18-ab23-be69eff4b7ff",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014Sv7zFgGUpFXhRjcK9vc9h",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 787,
      "cache_read_input_tokens": 68873,
      "output_tokens": 5946,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 787,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 5946,
          "cache_read_input_tokens": 68873,
          "cache_creation_input_tokens": 787,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 787
          },
          "type": "message"
        }
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

_source line 70 · 2026-05-16T00:34:10.782Z_

<details><summary>↩ Tool result · `toolu_01XhQkwD96KtNzN1JiEmwgcJ`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260516_c8f9bc\", \"name\": \"round10_data_summary\", \"type\": \"report\", \"description\": \"Round 10 完整数据编译：PPL dose curve (n=500), QW/DS accuracy, GSM8K cross-benchmark, sf5/entropy/LLaMA/pilot 补充证据，claim-evidence mapping，caveats 和 pending items\", \"path\": \"projects/phase-gated-compound-sparse/artifacts/_project/report/round10_data_summary.md\", \"url\": null, \"project\": \"phase-gated-compound-sparse\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-16T00:34:10.408266+00:00\", \"tags\": [\"round10\", \"data-compilation\", \"emnlp2026\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "314d51d9-187e-4d4e-a451-0ad8c52e7330",
  "isSidechain": false,
  "promptId": "e800486a-5431-4863-a090-6fe9e6a2f0b9",
  "type": "user",
  "uuid": "8552e4f5-d2e8-4f28-9d32-e51803da7624",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"artifact\\\": {\\\"id\\\": \\\"art_20260516_c8f9bc\\\", \\\"name\\\": \\\"round10_data_summary\\\", \\\"type\\\": \\\"report\\\", \\\"description\\\": \\\"Round 10 完整数据编译：PPL dose curve (n=500), QW/DS accuracy, GSM8K cross-benchmark, sf5/entropy/LLaMA/pilot 补充证据，claim-evidence mapping，caveats 和 pending items\\\", \\\"path\\\": \\\"projects/phase-gated-compound-sparse/artifacts/_project/report/round10_data_summary.md\\\", \\\"url\\\": null, \\\"project\\\": \\\"phase-gated-compound-sparse\\\", \\\"exp_id\\\": null, \\\"skill\\\": \\\"\\\", \\\"created_at\\\": \\\"2026-05-16T00:34:10.408266+00:00\\\", \\\"tags\\\": [\\\"round10\\\", \\\"data-compilation\\\", \\\"emnlp2026\\\"]}, \\\"manifest\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/manifest.yaml\\\"}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260516_c8f9bc\", \"name\": \"round10_data_summary\", \"type\": \"report\", \"description\": \"Round 10 完整数据编译：PPL dose curve (n=500), QW/DS accuracy, GSM8K cross-benchmark, sf5/entropy/LLaMA/pilot 补充证据，claim-evidence mapping，caveats 和 pending items\", \"path\": \"projects/phase-gated-compound-sparse/artifacts/_project/report/round10_data_summary.md\", \"url\": null, \"project\": \"phase-gated-compound-sparse\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-16T00:34:10.408266+00:00\", \"tags\": [\"round10\", \"data-compilation\", \"emnlp2026\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"
    }
  },
  "sourceToolAssistantUUID": "314d51d9-187e-4d4e-a451-0ad8c52e7330",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "sessionId": "38576691-e177-4a18-ab23-be69eff4b7ff",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 71 · 2026-05-16T00:34:10.787Z_

```json
{
  "parentUuid": "8552e4f5-d2e8-4f28-9d32-e51803da7624",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "e18d6c3f-7512-4a1b-968f-c187d43a0802",
  "timestamp": "2026-05-16T00:34:10.787Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "sessionId": "38576691-e177-4a18-ab23-be69eff4b7ff",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 72_

```json
{
  "type": "last-prompt",
  "leafUuid": "e18d6c3f-7512-4a1b-968f-c187d43a0802",
  "sessionId": "38576691-e177-4a18-ab23-be69eff4b7ff"
}
```

---

### Runtime record

_source line 73_

```json
{
  "type": "ai-title",
  "aiTitle": "Compile Round 10 experiment evidence for ARR submission",
  "sessionId": "38576691-e177-4a18-ab23-be69eff4b7ff"
}
```

---

### Assistant

_source line 74 · 2026-05-16T00:34:20.380Z_

已注册为 artifact `art_20260516_c8f9bc`。

编译完成。核心结论：

**12 claims 中 8 confirmed, 2 partially confirmed, 1 gate_failed (future work), 1 confirmed (running 补充数据)**

关键数字：
- PPL dose curve (n=500): DS 0.39→1.21→3.99→8.48, QW 0.07→0.31→1.07→3.16, 两模型 Spearman ρ=1.0, 全部 imp p<1e-14
- QW accuracy: 0.40→0.36→0.36→0.33→0.19, 断崖在 s025→s030 (−14pp)
- GSM8K: phase gradient 跨 benchmark 复现, 但 strategy specificity 从 15–36× 衰减至 2.3–3.8×

待补：acc_ds_s015_8k_v2 和 acc_ds_s030_8k_v2 仍在运行（DS accuracy 5-point curve 缺 2 点，但已降为定性观察，不阻塞论文）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e18d6c3f-7512-4a1b-968f-c187d43a0802",
  "isSidechain": false,
  "requestId": "req_011Cb5JrwiBtH1atAnbSZLNq",
  "type": "assistant",
  "uuid": "c0d147ba-35c3-4664-adad-ff8ccfaefd1a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "sessionId": "38576691-e177-4a18-ab23-be69eff4b7ff",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LHXBTapUsQefWPwqqhyLBF",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6371,
      "cache_read_input_tokens": 69660,
      "output_tokens": 316,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 6371,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 316,
          "cache_read_input_tokens": 69660,
          "cache_creation_input_tokens": 6371,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 6371
          },
          "type": "message"
        }
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

_source line 75_

```json
{
  "type": "last-prompt",
  "leafUuid": "c0d147ba-35c3-4664-adad-ff8ccfaefd1a",
  "sessionId": "38576691-e177-4a18-ab23-be69eff4b7ff"
}
```

---

### Runtime record

_source line 76_

```json
{
  "type": "ai-title",
  "aiTitle": "Compile Round 10 experiment evidence for ARR submission",
  "sessionId": "38576691-e177-4a18-ab23-be69eff4b7ff"
}
```

---
