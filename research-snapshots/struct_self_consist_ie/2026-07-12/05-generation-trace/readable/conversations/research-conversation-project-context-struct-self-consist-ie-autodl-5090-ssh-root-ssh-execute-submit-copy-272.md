# Research conversation: <project_context> # 项目: struct_self_consist_ie ## 运行环境 - 服务器名: autodl-5090 - SSH 账户: root（调用 ssh_execute / submit_traini

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 111
- **Recorded user turns:** 1
- **Tool calls:** 30
- **Original source:** `logs/chats/exported-trajectories/account-3/a97de670-f9a7-4d30-affd-382982b8a334.jsonl`
- **Structured JSON:** [`87e231dc6b8248fec053.json`](../../sessions/87/87e231dc6b8248fec053.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-19T13:54:24.264Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-19T13:54:24.264Z",
  "sessionId": "a97de670-f9a7-4d30-affd-382982b8a334",
  "content": "&lt;project_context>\n# 项目: struct_self_consist_ie\n\n## 运行环境\n- 服务器名: autodl-5090\n- SSH 账户: root（调用 ssh_execute / submit_training_job 时传入 account=\"root\"）\n- SSH 连接命令: ssh autodl-5090  # 必须用此命令，~/.ssh/config 自动应用密钥和跳板机，禁止用裸 IP\n- 项目代码根目录: /root/autodl-tmp/struct_self_consist_ie\n\n## ⚠️ 活跃约束（必须遵守）\n\n- **C001**: 论文 tex 文件只能修改 docs/paper/sections/ 下的编译版本，禁止直接修改 artifacts/_project/paper/ 下的 tex 文件（原因：两次出现 Worker 修改 artifacts/ 旧版本而非 docs/ 编译版本的系统性错误（patch-narrative worker + patch-experiments worker）。artifacts/_project/paper/ 是旧版残留，不参与编译。）\n\n\n## 环境搭建\n连接服务器后先调 `detect_image` 检测是否为预置镜像。如果匹配，跳过基础环境搭建，只装项目特有依赖。已预装的包不要重复安装。\n\n## 输出风格\n回复简洁直接。只输出执行结果和必要信息，不要解释过程、不要客套、不要给未被要求的建议。\n&lt;/project_context>\n## 任务：P0/P1 数据源深度核查\n\nClaim audit 发现论文中 4 个需要深度调查的数据不一致。你需要追溯数据源，确认正确值，并记录发现。\n\n### 调查 1: SciERC AUROC Table 1 vs registry 系统性偏离（P0）\n\nPaper Table 1 SciERC AUROC 列与 registry (exp_012_rerun_1024) 有系统性偏差：\n- VC: paper .663 vs registry .684 (-2.1pp)\n- SJ: paper .650 vs registry .692 (-4.2pp)\n- FK: paper .602 vs registry .629 (-2.7pp)\n- EM: paper .614 vs registry .749 (-13.5pp !!!)\n- LP: paper .578 vs registry .578 (0pp，唯一匹配)\n\nρ 值完全匹配（确认是同一份数据），但 AUROC 不同。\n\n你需要：\n1. 读 registry 中 exp_012_rerun_1024 的完整 metrics（用 read_registry）\n2. SSH 到服务器查找 AUROC 计算脚本，看是否有不同的 binarization threshold 或计算方式\n3. 确定哪组 AUROC 是正确的\n4. 将发现写入 artifacts 目录\n\n### 调查 2: CoNLL LP selection Δ 不一致（P0）\n\nTable 3 (experiments.tex:122) 写 CoNLL LP Δ = -0.85pp\nAppendix cross-selection table (appendix.tex:248) 写 LP F1 = .897, Δ = -1.1pp (相对 greedy .908)\n\n两处都声称是 3-seed mean, Qwen/CoNLL N=8。需要：\n1. 查 registry 中 CoNLL LP selection 相关实验的具体数值\n2. 检查是否 seed 组合或 averaging 方法不同\n3. 确定正确值\n\n### 调查 3: FewNERD degeneracy 13.8% 来源不明（P1）\n\nPaper Table 3: FewNERD degen = 13.8%\nRegistry 各 seed：\n- Seed 42: 10.1%, Seed 123: 13.1%, Seed 456: 12.1%, Seed 789: 11.8%\n- 3-seed mean (42/123/456) = 11.8% ≠ 13.8%\n- 4-seed mean = 11.8% ≠ 13.8%\n\n需要：\n1. 用 read_registry 查 FewNERD 相关实验的 degen_rate 字段\n2. 找出 13.8% 的计算来源（可能是不同 epoch/checkpoint？）\n\n### 调查 4: CoNLL degeneracy 48.4% 是 N=8 还是 N=16（P1）\n\nTable 3 标题写 N=8，但 CoNLL degen 48.4% 与 registry exp_002_conll_n16 (N=16) 的 0.4844 完全匹配。\n需要确认：\n1. 是否有 N=8 的 CoNLL degeneracy 数据\n2. 如果没有，Table 3 可能混用了 N=16 的值\n\n### 产出\n\n将所有发现写入：\n`/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/p0_data_verification_report.md`\n\n格式：每个调查项列出 [发现] [正确值] [建议修复]。"
}
```

---

### Runtime record

_source line 2 · 2026-05-19T13:54:24.267Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-19T13:54:24.267Z",
  "sessionId": "a97de670-f9a7-4d30-affd-382982b8a334"
}
```

---

## Round 1

109 recorded events

### User

_source line 3 · 2026-05-19T13:54:24.299Z_

&lt;project_context>
# 项目: struct_self_consist_ie

## 运行环境
- 服务器名: autodl-5090
- SSH 账户: root（调用 ssh_execute / submit_training_job 时传入 account="root"）
- SSH 连接命令: ssh autodl-5090  # 必须用此命令，~/.ssh/config 自动应用密钥和跳板机，禁止用裸 IP
- 项目代码根目录: /root/autodl-tmp/struct_self_consist_ie

## ⚠️ 活跃约束（必须遵守）

- **C001**: 论文 tex 文件只能修改 docs/paper/sections/ 下的编译版本，禁止直接修改 artifacts/_project/paper/ 下的 tex 文件（原因：两次出现 Worker 修改 artifacts/ 旧版本而非 docs/ 编译版本的系统性错误（patch-narrative worker + patch-experiments worker）。artifacts/_project/paper/ 是旧版残留，不参与编译。）


## 环境搭建
连接服务器后先调 `detect_image` 检测是否为预置镜像。如果匹配，跳过基础环境搭建，只装项目特有依赖。已预装的包不要重复安装。

## 输出风格
回复简洁直接。只输出执行结果和必要信息，不要解释过程、不要客套、不要给未被要求的建议。
&lt;/project_context>
## 任务：P0/P1 数据源深度核查

Claim audit 发现论文中 4 个需要深度调查的数据不一致。你需要追溯数据源，确认正确值，并记录发现。

### 调查 1: SciERC AUROC Table 1 vs registry 系统性偏离（P0）

Paper Table 1 SciERC AUROC 列与 registry (exp_012_rerun_1024) 有系统性偏差：
- VC: paper .663 vs registry .684 (-2.1pp)
- SJ: paper .650 vs registry .692 (-4.2pp)
- FK: paper .602 vs registry .629 (-2.7pp)
- EM: paper .614 vs registry .749 (-13.5pp !!!)
- LP: paper .578 vs registry .578 (0pp，唯一匹配)

ρ 值完全匹配（确认是同一份数据），但 AUROC 不同。

你需要：
1. 读 registry 中 exp_012_rerun_1024 的完整 metrics（用 read_registry）
2. SSH 到服务器查找 AUROC 计算脚本，看是否有不同的 binarization threshold 或计算方式
3. 确定哪组 AUROC 是正确的
4. 将发现写入 artifacts 目录

### 调查 2: CoNLL LP selection Δ 不一致（P0）

Table 3 (experiments.tex:122) 写 CoNLL LP Δ = -0.85pp
Appendix cross-selection table (appendix.tex:248) 写 LP F1 = .897, Δ = -1.1pp (相对 greedy .908)

两处都声称是 3-seed mean, Qwen/CoNLL N=8。需要：
1. 查 registry 中 CoNLL LP selection 相关实验的具体数值
2. 检查是否 seed 组合或 averaging 方法不同
3. 确定正确值

### 调查 3: FewNERD degeneracy 13.8% 来源不明（P1）

Paper Table 3: FewNERD degen = 13.8%
Registry 各 seed：
- Seed 42: 10.1%, Seed 123: 13.1%, Seed 456: 12.1%, Seed 789: 11.8%
- 3-seed mean (42/123/456) = 11.8% ≠ 13.8%
- 4-seed mean = 11.8% ≠ 13.8%

需要：
1. 用 read_registry 查 FewNERD 相关实验的 degen_rate 字段
2. 找出 13.8% 的计算来源（可能是不同 epoch/checkpoint？）

### 调查 4: CoNLL degeneracy 48.4% 是 N=8 还是 N=16（P1）

Table 3 标题写 N=8，但 CoNLL degen 48.4% 与 registry exp_002_conll_n16 (N=16) 的 0.4844 完全匹配。
需要确认：
1. 是否有 N=8 的 CoNLL degeneracy 数据
2. 如果没有，Table 3 可能混用了 N=16 的值

### 产出

将所有发现写入：
`/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/p0_data_verification_report.md`

格式：每个调查项列出 [发现] [正确值] [建议修复]。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "0731b9be-f5e6-4a8a-9a3c-2edafe06629b",
  "type": "user",
  "uuid": "652207f2-cf18-42f9-a211-433ac9261dc4",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "a97de670-f9a7-4d30-affd-382982b8a334",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-19T13:54:24.298Z_

```json
{
  "parentUuid": "652207f2-cf18-42f9-a211-433ac9261dc4",
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
      "mcp__agent-ml-research__detect_image",
      "mcp__agent-ml-research__kill_job",
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__read_registry",
      "mcp__agent-ml-research__register_artifact",
      "mcp__agent-ml-research__save_project_file",
      "mcp__agent-ml-research__ssh_execute",
      "mcp__agent-ml-research__ssh_read_only",
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
      "mcp__agent-ml-research__detect_image",
      "mcp__agent-ml-research__kill_job",
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__read_registry",
      "mcp__agent-ml-research__register_artifact",
      "mcp__agent-ml-research__save_project_file",
      "mcp__agent-ml-research__ssh_execute",
      "mcp__agent-ml-research__ssh_read_only",
      "mcp__agent-ml-research__update_registry"
    ],
    "removedNames": []
  },
  "type": "attachment",
  "uuid": "0c9b68a7-dcc9-4c7f-95e0-696ed57161b1",
  "timestamp": "2026-05-19T13:54:24.298Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "a97de670-f9a7-4d30-affd-382982b8a334",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-19T13:54:24.298Z_

```json
{
  "parentUuid": "0c9b68a7-dcc9-4c7f-95e0-696ed57161b1",
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
  "uuid": "b55a6000-617e-473e-aaf8-5c77e31a80cc",
  "timestamp": "2026-05-19T13:54:24.298Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "a97de670-f9a7-4d30-affd-382982b8a334",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 6 · 2026-05-19T13:54:24.298Z_

```json
{
  "parentUuid": "b55a6000-617e-473e-aaf8-5c77e31a80cc",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "62276bad-898d-4991-93a5-d3550a3bb539",
  "timestamp": "2026-05-19T13:54:24.298Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "a97de670-f9a7-4d30-affd-382982b8a334",
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
  "aiTitle": "Audit data inconsistencies in paper tables",
  "sessionId": "a97de670-f9a7-4d30-affd-382982b8a334"
}
```

---

### Assistant

_source line 8 · 2026-05-19T13:54:27.684Z_

I'll start by loading the necessary MCP tools and reading the registry data for all four investigations in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "62276bad-898d-4991-93a5-d3550a3bb539",
  "isSidechain": false,
  "requestId": "req_011CbC3JyPHLTyqQ5d4mtgwa",
  "type": "assistant",
  "uuid": "2ced91ff-4dc1-42a2-a1ff-82ef2e1bb735",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "a97de670-f9a7-4d30-affd-382982b8a334",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0178XmZbVJM6qFmPudth5EVV",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12474,
      "cache_read_input_tokens": 11841,
      "output_tokens": 180,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12474,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 180,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 12474,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12474
          },
          "type": "message"
        }
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

_source line 9 · 2026-05-19T13:54:29.162Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01BhZgKFqup8YJv8sEEHkHHA`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_registry,mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__register_artifact,mcp__agent-ml-research__save_project_file",
  "max_results": 6
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2ced91ff-4dc1-42a2-a1ff-82ef2e1bb735",
  "isSidechain": false,
  "requestId": "req_011CbC3JyPHLTyqQ5d4mtgwa",
  "type": "assistant",
  "uuid": "d17079c6-6b69-4e3b-b108-fe1a3d9563a5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "a97de670-f9a7-4d30-affd-382982b8a334",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0178XmZbVJM6qFmPudth5EVV",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12474,
      "cache_read_input_tokens": 11841,
      "output_tokens": 180,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12474,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 180,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 12474,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12474
          },
          "type": "message"
        }
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

_source line 10 · 2026-05-19T13:54:29.172Z_

<details><summary>↩ Tool result · `toolu_01BhZgKFqup8YJv8sEEHkHHA`</summary>

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
  "tool_name": "mcp__agent-ml-research__ssh_read_only"
}
```

```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__ssh_execute"
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
  "tool_name": "mcp__agent-ml-research__register_artifact"
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
  "parentUuid": "d17079c6-6b69-4e3b-b108-fe1a3d9563a5",
  "isSidechain": false,
  "promptId": "0731b9be-f5e6-4a8a-9a3c-2edafe06629b",
  "type": "user",
  "uuid": "97d40cee-d37a-45ff-b048-bbe56c84e66a",
  "toolUseResult": {
    "matches": [
      "mcp__agent-ml-research__read_registry",
      "mcp__agent-ml-research__ssh_read_only",
      "mcp__agent-ml-research__ssh_execute",
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__register_artifact",
      "mcp__agent-ml-research__save_project_file"
    ],
    "query": "select:mcp__agent-ml-research__read_registry,mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__register_artifact,mcp__agent-ml-research__save_project_file",
    "total_deferred_tools": 29
  },
  "sourceToolAssistantUUID": "d17079c6-6b69-4e3b-b108-fe1a3d9563a5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "a97de670-f9a7-4d30-affd-382982b8a334",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 11 · 2026-05-19T13:54:32.688Z_

<details><summary>Logged reasoning block</summary>

```text
Now let me read the registry data for the relevant experiments, and also look at the paper tex files to understand the current claims. Let me do these in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "97d40cee-d37a-45ff-b048-bbe56c84e66a",
  "isSidechain": false,
  "requestId": "req_011CbC3KLXmDCphZ7BiR3dtb",
  "type": "assistant",
  "uuid": "f5ff606f-acd6-4afd-bf37-fb324e8593a4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "a97de670-f9a7-4d30-affd-382982b8a334",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01K9CMF8mt8fbLgVHFPzVjey",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2252,
      "cache_read_input_tokens": 24315,
      "output_tokens": 779,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2252,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 779,
          "cache_read_input_tokens": 24315,
          "cache_creation_input_tokens": 2252,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2252
          },
          "type": "message"
        }
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

_source line 12 · 2026-05-19T13:54:33.448Z_

Starting the investigation. Let me pull registry data and paper source files in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f5ff606f-acd6-4afd-bf37-fb324e8593a4",
  "isSidechain": false,
  "requestId": "req_011CbC3KLXmDCphZ7BiR3dtb",
  "type": "assistant",
  "uuid": "4e666752-0a4e-4a97-a008-86fb6b4a9360",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "a97de670-f9a7-4d30-affd-382982b8a334",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01K9CMF8mt8fbLgVHFPzVjey",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2252,
      "cache_read_input_tokens": 24315,
      "output_tokens": 779,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2252,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 779,
          "cache_read_input_tokens": 24315,
          "cache_creation_input_tokens": 2252,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2252
          },
          "type": "message"
        }
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

_source line 13 · 2026-05-19T13:54:34.455Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_01ByKVsx87AvnnoJpcdnDVco`</summary>

```json
{
  "project": "struct_self_consist_ie",
  "filters": {
    "exp_id": "exp_012_rerun_1024"
  },
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
  "parentUuid": "4e666752-0a4e-4a97-a008-86fb6b4a9360",
  "isSidechain": false,
  "requestId": "req_011CbC3KLXmDCphZ7BiR3dtb",
  "type": "assistant",
  "uuid": "6b6b0a3f-852d-4c22-811a-d9df0ce2f62a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "a97de670-f9a7-4d30-affd-382982b8a334",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01K9CMF8mt8fbLgVHFPzVjey",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2252,
      "cache_read_input_tokens": 24315,
      "output_tokens": 779,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2252,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 779,
          "cache_read_input_tokens": 24315,
          "cache_creation_input_tokens": 2252,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2252
          },
          "type": "message"
        }
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

_source line 14 · 2026-05-19T13:54:35.007Z_

<details><summary>↩ Tool result · `toolu_01ByKVsx87AvnnoJpcdnDVco`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.5344}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6b6b0a3f-852d-4c22-811a-d9df0ce2f62a",
  "isSidechain": false,
  "promptId": "0731b9be-f5e6-4a8a-9a3c-2edafe06629b",
  "type": "user",
  "uuid": "caa42b42-cbc7-4035-a3bc-be86aa70e611",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"experiments\\\": {}, \\\"count\\\": 0, \\\"total\\\": 0, \\\"baseline\\\": null}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.5344}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.5344}}"
    }
  },
  "sourceToolAssistantUUID": "6b6b0a3f-852d-4c22-811a-d9df0ce2f62a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "a97de670-f9a7-4d30-affd-382982b8a334",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-19T13:54:35.409Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_0163guufA6QCbKCbHoF9kyix`</summary>

```json
{
  "project": "struct_self_consist_ie",
  "limit": 0,
  "fields": [
    "exp_id",
    "status",
    "conclusion",
    "metrics",
    "config"
  ]
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "caa42b42-cbc7-4035-a3bc-be86aa70e611",
  "isSidechain": false,
  "requestId": "req_011CbC3KLXmDCphZ7BiR3dtb",
  "type": "assistant",
  "uuid": "498077fb-4abe-4603-9215-51d13cb29ee7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "a97de670-f9a7-4d30-affd-382982b8a334",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01K9CMF8mt8fbLgVHFPzVjey",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2252,
      "cache_read_input_tokens": 24315,
      "output_tokens": 779,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2252,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 779,
          "cache_read_input_tokens": 24315,
          "cache_creation_input_tokens": 2252,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2252
          },
          "type": "message"
        }
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

_source line 16 · 2026-05-19T13:54:36.378Z_

<details><summary>↩ Tool result · `toolu_0163guufA6QCbKCbHoF9kyix`</summary>

```text
Error: result (84,157 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie/a97de670-f9a7-4d30-affd-382982b8a334/tool-results/mcp-agent-ml-research-read_registry-1779198876363.txt.
Format: JSON with schema: {result: string}
- For targeted queries (find a value, filter by field): use jq on the file directly.
- For analysis or summarization that requires reading the full content: first probe the structure (e.g., jq 'type, length, keys?' /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie/a97de670-f9a7-4d30-affd-382982b8a334/tool-results/mcp-agent-ml-research-read_registry-1779198876363.txt), then extract slices with jq or python — Read's line-based offset/limit will not chunk this file.
- If the Agent tool is available, do this inside a subagent so the full output stays out of your main context. Give it the instruction above verbatim, and be explicit about what it must return — e.g. "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie/a97de670-f9a7-4d30-affd-382982b8a334/tool-results/mcp-agent-ml-research-read_registry-1779198876363.txt is JSON with schema: {result: string}; probe the structure with jq (type/length/keys), then extract and read the content in full with jq or python, then summarize and quote any key findings verbatim." A vague "summarize this" may lose detail.

```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "498077fb-4abe-4603-9215-51d13cb29ee7",
  "isSidechain": false,
  "promptId": "0731b9be-f5e6-4a8a-9a3c-2edafe06629b",
  "type": "user",
  "uuid": "4ed4ae10-5725-44ba-bbb5-6d7b090fa9d3",
  "toolUseResult": "Error: result (84,157 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie/a97de670-f9a7-4d30-affd-382982b8a334/tool-results/mcp-agent-ml-research-read_registry-1779198876363.txt.\nFormat: JSON with schema: {result: string}\n- For targeted queries (find a value, filter by field): use jq on the file directly.\n- For analysis or summarization that requires reading the full content: first probe the structure (e.g., jq 'type, length, keys?' /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie/a97de670-f9a7-4d30-affd-382982b8a334/tool-results/mcp-agent-ml-research-read_registry-1779198876363.txt), then extract slices with jq or python — Read's line-based offset/limit will not chunk this file.\n- If the Agent tool is available, do this inside a subagent so the full output stays out of your main context. Give it the instruction above verbatim, and be explicit about what it must return — e.g. \"/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie/a97de670-f9a7-4d30-affd-382982b8a334/tool-results/mcp-agent-ml-research-read_registry-1779198876363.txt is JSON with schema: {result: string}; probe the structure with jq (type/length/keys), then extract and read the content in full with jq or python, then summarize and quote any key findings verbatim.\" A vague \"summarize this\" may lose detail.\n",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {\"exp_qwen25_72b_zeroshot\": {\"status\": \"RUNNING\"}, \"exp_qwen25_14b_fewnerd\": {\"status\": \"RUNNING\"}, \"exp_qwen25_32b_fewnerd\": {\"status\": \"RUNNING\"}, \"exp_qwen25_7b_fewnerd\": {\"status\": \"RUNNING\"}, \"exp_wnut17_qwen25_7b\": {\"status\": \"DONE\", \"conclusion\": \"negative\", \"metrics\": {\"seed42\": {\"greedy_f1\": 0.4524, \"construction_f1\": 0.4439, \"construction_delta_pp\": -0.84, \"construction_p\": 0.95}, \"seed123\": {\"greedy_f1\": 0.4518, \"construction_f1\": 0.4579, \"construction_delta_pp\": 0.61, \"construction_p\": 0.08}, \"seed456\": {\"greedy_f1\": 0.4526, \"construction_f1\": 0.4583, \"construction_delta_pp\": 0.57, \"construction_p\": 0.12}, \"oracle_headroom_pp\": \"6.3-9.2\"}}, \"exp_llama_fewnerd_inference\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"3seed_mean\": {\"greedy_f1\": 0.7842, \"oracle_f1\": 0.8843, \"headroom_pp\": 10.01, \"degeneracy_pct\": 23.36, \"lp_delta_pp\": 0.36, \"dgs_delta_pp\": -0.35}, \"seed_42\": {\"greedy_f1\": 0.7841, \"oracle_f1\": 0.8854, \"degen\": 27.32}, \"seed_123\": {\"greedy_f1\": 0.784, \"oracle_f1\": 0.8839, \"degen\": 24.63}, \"seed_456\": {\"greedy_f1\": 0.7844, \"oracle_f1\": 0.8835, \"degen\": 18.13}, \"signal_ranking\": \"LP (+0.36pp) > SJ (-0.52) > FK (-0.53) > EM (-1.02) > VC (-2.39)\", \"lp_only_positive\": true, \"n_instances_gold_filtered\": 32565}}, \"exp_entity_construction\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"n16_fair_cv\": {\"scierc_ner\": {\"cv_uniform_delta\": \"+1.35pp\", \"p_value\": 0.018, \"significant\": true}, \"conll_ner\": {\"cv_uniform_delta\": \"+0.10pp\", \"p_value\": 0.303, \"significant\": false}, \"fewnerd_ner\": {\"cv_uniform_delta\": \"+1.32pp\", \"p_value\": 0, \"significant\": true}, \"scierc_re\": {\"cv_uniform_delta\": \"+1.69pp\", \"p_value\": 0.049, \"significant\": true}}, \"n8_fair_cv\": {\"scierc_ner\": {\"uniform_confirm\": \"+1.54pp (p=0.023, sig)\", \"lp_weighted_confirm\": \"+1.67pp (p=0.004, sig)\", \"cv_uniform\": \"+1.12pp (p=0.057, borderline)\"}, \"conll_ner\": {\"cv_uniform\": \"-0.39pp (p=0.963, not sig)\"}, \"fewnerd_ner\": {\"lp_weighted_cv\": \"+0.88pp (p=0.000, sig)\", \"uniform_cv\": \"+0.32pp (p=0.003, sig)\"}}, \"adaptive_combination\": \"INVALIDATED - gold label leakage confirmed\", \"note\": \"5-fold CV, bootstrap B=10000, paired one-sided\"}}, \"exp_lp_alignment_gating\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"adjusted_score\": \"mean_rho * valid_ratio\", \"threshold\": 0.3, \"accuracy\": \"3/3 datasets correct\", \"robust_range\": \"0.2-0.4\"}}, \"exp_selective_prediction\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"vc_best_signal\": true, \"f1_at_80pct_coverage\": {\"scierc\": \"+5.0pp\", \"conll\": \"+8.4pp\", \"fewnerd\": \"+6.2pp\"}, \"precision_coverage_curves\": \"output/prescriptive_analysis/fig_selective_prediction.pdf\"}}, \"exp_llama_fewnerd_lora\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"epoch\": 3, \"train_loss\": 0.0516, \"eval_loss\": 0.0323, \"train_runtime_hours\": 15.35, \"total_steps\": 24708, \"final_checkpoint\": \"checkpoint-24708\", \"adapter_size_mb\": 320}}, \"hidden_state_probe_conll_full\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"hidden_state_probe_conll_v2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"exp_031_fewnerd_t12\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"exp_030_conll_t12\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"mbr_pilot\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"dgs_pilot\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"exp_fewnerd_s789_n8\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"greedy_f1\": 0.7478, \"oracle_f1\": 0.8714, \"headroom_pp\": 12.37, \"degen_rate\": 0.1177, \"degen_rate_source\": \"unified_metrics_constant_f1_gold_filtered\", \"instance_count\": 37648, \"n_valid\": 32565, \"lp_sel_f1\": 0.7614, \"lp_delta_pp\": 1.36, \"lp_rho_global\": 0.1788, \"lp_rho_cond\": 0.176, \"dgs_f1\": 0.7621, \"dgs_delta_pp\": 1.43, \"dgs_vs_lp_pp\": 0.07, \"best_signal\": \"LP\", \"four_seed_mean_greedy\": 0.7481, \"four_seed_mean_lp_delta_pp\": 1.38, \"four_seed_lp_delta_ci95\": [1.32, 1.44]}}, \"exp_026_t12_seed456\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"ner_greedy_f1\": 0.6637, \"ner_oracle_f1\": 0.7821, \"rho_sj_ner\": 0.3995, \"sample_f1_pct_zero\": 14.08, \"instance_count\": 551, \"n_valid\": 529}}, \"exp_026_t12_seed123\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"ner_greedy_f1\": 0.6595, \"ner_oracle_f1\": 0.7895, \"rho_sj_ner\": 0.359, \"sample_f1_pct_zero\": 13.99, \"instance_count\": 551, \"n_valid\": 529}}, \"exp_026_t10_seed456\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"ner_greedy_f1\": 0.6621, \"ner_oracle_f1\": 0.7754, \"rho_sj_ner\": 0.3921, \"sample_f1_pct_zero\": 12.97, \"instance_count\": 551, \"n_valid\": 529}}, \"exp_026_t10_seed123\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"ner_greedy_f1\": 0.6633, \"ner_oracle_f1\": 0.7777, \"rho_sj_ner\": 0.3809, \"sample_f1_pct_zero\": 12.59, \"instance_count\": 551, \"n_valid\": 529}}, \"exp_026_t10_seed42\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"ner_greedy_f1\": 0.6617, \"ner_oracle_f1\": 0.7798, \"rho_sj_ner\": 0.3598, \"sample_f1_pct_zero\": 12.9, \"instance_count\": 551, \"n_valid\": 529}}, \"exp_026_t08_seed456\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"ner_greedy_f1\": 0.6641, \"ner_oracle_f1\": 0.7694, \"rho_sj_ner\": 0.3771, \"sample_f1_pct_zero\": 11.79, \"instance_count\": 551, \"n_valid\": 529}}, \"exp_026_t08_seed123\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"ner_greedy_f1\": 0.6607, \"ner_oracle_f1\": 0.7714, \"rho_sj_ner\": 0.3893, \"sample_f1_pct_zero\": 11.22, \"instance_count\": 551, \"n_valid\": 529}}, \"exp_026_t05_seed456\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"ner_greedy_f1\": 0.6639, \"ner_oracle_f1\": 0.7437, \"rho_sj_ner\": 0.3279, \"sample_f1_pct_zero\": 10.28, \"instance_count\": 551, \"n_valid\": 529}}, \"exp_026_t05_seed123\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"ner_greedy_f1\": 0.6611, \"ner_oracle_f1\": 0.7444, \"rho_sj_ner\": 0.3133, \"sample_f1_pct_zero\": 10.09, \"instance_count\": 551, \"n_valid\": 529}}, \"exp_029b\": {\"status\": \"DONE\", \"metrics\": {\"degen_rate\": 0.478, \"degen_rate_source\": \"unified_metrics_constant_f1_gold_filtered\"}, \"conclusion\": \"success\"}, \"exp_029a\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"degen_rate\": 0.064, \"degen_rate_source\": \"unified_metrics_constant_f1_gold_filtered\"}}, \"exp_021_fewnerd_n8_seed456\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"degen_rate\": 0.1212, \"degen_rate_source\": \"unified_metrics_constant_f1_gold_filtered\", \"instance_count\": 37648, \"n_valid\": 32565, \"n_gold_empty\": 5083, \"ner_greedy_f1\": 0.7888, \"ner_oracle_f1\": 0.881, \"rho_fk_ner\": 0.1632, \"rho_sj_ner\": 0.313, \"sample_f1_pct_zero\": 19.32}}, \"exp_021_fewnerd_n8_seed123\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"degen_rate\": 0.1312, \"degen_rate_source\": \"unified_metrics_constant_f1_gold_filtered\", \"instance_count\": 37648, \"n_valid\": 32565, \"n_gold_empty\": 5083, \"ner_greedy_f1\": 0.7885, \"ner_oracle_f1\": 0.8892, \"rho_fk_ner\": 0.1602, \"rho_sj_ner\": 0.3083, \"sample_f1_pct_zero\": 20.39}}, \"exp_002_conll_n16_seed456\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"degen_rate\": 0.5544, \"degen_rate_source\": \"unified_metrics_constant_f1_gold_filtered\", \"instance_count\": 3453, \"n_valid\": 2756, \"n_gold_empty\": 697, \"ner_greedy_f1\": 0.9074, \"ner_oracle_f1\": 0.9549, \"rho_fk_ner\": 0.4718, \"rho_sj_ner\": 0.4819, \"sample_f1_pct_zero\": 7.02}}, \"exp_002_conll_n16_seed123\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"degen_rate\": 0.471, \"degen_rate_source\": \"unified_metrics_constant_f1_gold_filtered\", \"instance_count\": 3453, \"n_valid\": 2756, \"n_gold_empty\": 697, \"ner_greedy_f1\": 0.9068, \"ner_oracle_f1\": 0.9633, \"rho_fk_ner\": 0.4524, \"rho_sj_ner\": 0.4621, \"sample_f1_pct_zero\": 7.54}}, \"exp_017_llama_conll_n16_s456_r1024\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"degen_rate\": 0.8672, \"degen_rate_source\": \"unified_metrics_constant_f1_gold_filtered\", \"instance_count\": 3453, \"n_valid\": 2756, \"n_gold_empty\": 697, \"parse_rate\": 1, \"ner_greedy_f1\": 0.9265, \"ner_oracle_f1\": 0.9499, \"rho_fk_ner\": 0.469, \"rho_sj_ner\": 0.4734, \"rho_vc_ner\": 0.4722, \"rho_em_ner\": 0.4752, \"rho_lp_ner\": 0.3099, \"auroc_fk_ner\": 0.7408, \"auroc_sj_ner\": 0.7428, \"auroc_vc_ner\": 0.7495, \"auroc_em_ner\": 0.7444, \"auroc_lp_ner\": 0.7628, \"auroc_note\": \"median F1=1.0, AUROC uses >=median threshold\", \"rho_note\": \"CORRECTED 2026-05-15: old values (rho_fk=0.8085,rho_sj=0.1895) were inflated/deflated by 697 gold-empty instances. Now uses gold-filtered pipeline (n=2756).\"}}, \"exp_017_llama_conll_n16_r1024\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"degen_rate\": 0.8647, \"degen_rate_source\": \"unified_metrics_constant_f1_gold_filtered\", \"instance_count\": 3453, \"n_valid\": 2756, \"n_gold_empty\": 697, \"parse_rate\": 1, \"ner_greedy_f1\": 0.9265, \"ner_oracle_f1\": 0.9499, \"rho_fk_ner\": 0.4752, \"rho_sj_ner\": 0.4836, \"rho_vc_ner\": 0.4746, \"rho_em_ner\": 0.4818, \"rho_lp_ner\": 0.3136, \"auroc_fk_ner\": 0.7467, \"auroc_sj_ner\": 0.7496, \"auroc_vc_ner\": 0.7529, \"auroc_em_ner\": 0.7508, \"auroc_lp_ner\": 0.7661, \"auroc_note\": \"median F1=1.0, AUROC uses >=median threshold\", \"rho_note\": \"CORRECTED 2026-05-15: old values (rho_fk=0.8095,rho_sj=0.1815) were inflated/deflated by 697 gold-empty instances. Now uses gold-filtered pipeline (n=2756).\"}}, \"exp_018_llama_scierc_seed456_r1024\": {\"status\": \"DONE\", \"metrics\": {\"degen_rate\": 0.2741, \"degen_rate_source\": \"unified_metrics_constant_f1_gold_filtered\", \"ner_greedy_f1\": 0.6597, \"ner_oracle_f1\": 0.7683, \"ner_oracle_headroom\": 0.1086, \"ner_cond_rho_fk\": 0.1472, \"ner_cond_rho_sj\": 0.2718, \"ner_cond_rho_logprob\": 0.083, \"ner_logprob_auroc_cond\": 0.5485, \"re_greedy_f1\": 0.4338, \"re_oracle_f1\": 0.5834, \"re_oracle_headroom\": 0.1496, \"re_cond_rho_fk\": 0.2107, \"re_cond_rho_sj\": 0.3898, \"re_cond_rho_logprob\": 0.1252, \"re_logprob_auroc_cond\": 0.6119, \"ner_structural_beats_logprob\": true, \"re_structural_beats_logprob\": true}, \"conclusion\": \"success\"}, \"exp_018_llama_scierc_seed42_r1024\": {\"status\": \"DONE\", \"metrics\": {\"degen_rate\": 0.2495, \"degen_rate_source\": \"unified_metrics_constant_f1_gold_filtered\", \"ner\": {\"full\": {\"SJ\": {\"rho\": 0.3096, \"tau\": 0.2288, \"auroc\": 0.6683}, \"FK\": {\"rho\": 0.2352, \"tau\": 0.1759, \"auroc\": 0.6069}, \"logprob\": {\"rho\": 0.1503, \"tau\": 0.1087, \"auroc\": 0.5318}, \"EM\": {\"rho\": 0.2587, \"tau\": 0.1966, \"auroc\": 0.7174}, \"voting_conf\": {\"rho\": 0.4053, \"tau\": 0.3042, \"auroc\": 0.6967}}, \"conditional\": {\"SJ\": {\"rho\": 0.2718, \"tau\": null, \"auroc\": 0.6565}, \"FK\": {\"rho\": 0.1472, \"tau\": null, \"auroc\": 0.5866}, \"logprob\": {\"rho\": 0.081, \"tau\": null, \"auroc\": 0.5129}, \"EM\": {\"rho\": 0.3165, \"tau\": null, \"auroc\": 0.7244}, \"voting_conf\": {\"rho\": 0.3078, \"tau\": null, \"auroc\": 0.6714}}, \"greedy_f1\": 0.6607, \"oracle_f1\": 0.7781, \"n_full\": 529, \"n_cond\": 478}, \"re\": {\"full\": {\"SJ\": {\"rho\": 0.2748, \"tau\": 0.2102, \"auroc\": 0.7244}, \"FK\": {\"rho\": 0.3027, \"tau\": 0.2337, \"auroc\": 0.691}, \"logprob\": {\"rho\": 0.3163, \"tau\": 0.233, \"auroc\": 0.6313}, \"EM\": {\"rho\": 0.1681, \"tau\": 0.1275, \"auroc\": 0.7697}, \"voting_conf\": {\"rho\": 0.384, \"tau\": 0.2965, \"auroc\": 0.7337}}, \"conditional\": {\"SJ\": {\"rho\": 0.3461, \"tau\": null, \"auroc\": 0.7233}, \"FK\": {\"rho\": 0.1969, \"tau\": null, \"auroc\": 0.6684}, \"logprob\": {\"rho\": 0.0888, \"tau\": null, \"auroc\": 0.5556}, \"EM\": {\"rho\": 0.4969, \"tau\": null, \"auroc\": 0.819}, \"voting_conf\": {\"rho\": 0.3433, \"tau\": null, \"auroc\": 0.7003}}, \"greedy_f1\": 0.4319, \"oracle_f1\": 0.5775, \"n_full\": 397, \"n_cond\": 251}}, \"conclusion\": \"success\"}, \"exp_002_conll_n16\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"degen_rate\": 0.4844, \"degen_rate_source\": \"unified_metrics_constant_f1_gold_filtered\", \"N\": 16, \"dataset\": \"conll2003\", \"subtask\": \"ner\", \"n_instances\": 3453, \"n_valid\": 2756, \"n_conditional\": 2614, \"greedy_f1\": 0.907, \"full\": {\"SJ_rho\": 0.4496, \"FK_rho\": 0.3928, \"logprob_rho\": 0.3146, \"EM_rho\": 0.4627, \"voting_conf_rho\": 0.4286, \"SJ_AUROC\": 0.8264, \"FK_AUROC\": 0.7821, \"logprob_AUROC\": 0.7531, \"EM_AUROC\": 0.8409, \"voting_conf_AUROC\": 0.8071, \"SJ_ECE\": 0.0747, \"FK_ECE\": 0.1786, \"logprob_ECE\": 0.2031, \"EM_ECE\": 0.0786, \"voting_conf_ECE\": 0.529}, \"conditional\": {\"SJ_rho\": 0.4208, \"FK_rho\": 0.3494, \"logprob_rho\": 0.3756, \"EM_rho\": 0.4658, \"voting_conf_rho\": 0.3654, \"SJ_AUROC\": 0.8405, \"FK_AUROC\": 0.7819, \"logprob_AUROC\": 0.8259, \"EM_AUROC\": 0.8781, \"voting_conf_AUROC\": 0.7951, \"SJ_ECE\": 0.0982, \"FK_ECE\": 0.1899, \"logprob_ECE\": 0.2504, \"EM_ECE\": 0.0997, \"voting_conf_ECE\": 0.6096}, \"n8_vs_n16_delta_rho_full\": {\"SJ\": 0.0139, \"FK\": -0.007, \"logprob\": -0.0011, \"EM\": 0.012, \"voting_conf\": 0.0049}}}, \"exp_012_rerun_1024\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"degen_rate\": 0.1777, \"degen_rate_source\": \"unified_metrics_constant_f1_gold_filtered\", \"ner_full\": {\"n\": 529, \"SJ\": {\"rho\": 0.3599, \"tau\": 0.2646, \"AUROC\": 0.6917, \"ECE\": 0.4531, \"rho_ci95\": [0.2732, 0.4389], \"AUROC_ci95\": [0.6304, 0.7406]}, \"FK\": {\"rho\": 0.2665, \"tau\": 0.1974, \"AUROC\": 0.629, \"ECE\": 0.4512, \"rho_ci95\": [0.1743, 0.3486], \"AUROC_ci95\": [0.5612, 0.6882]}, \"logprob\": {\"rho\": 0.2052, \"tau\": 0.1478, \"AUROC\": 0.5783, \"ECE\": 0.7064, \"rho_ci95\": [0.1171, 0.2904], \"AUROC_ci95\": [0.5179, 0.6387]}, \"EM\": {\"rho\": 0.2945, \"tau\": 0.2208, \"AUROC\": 0.7493, \"ECE\": 0.3526, \"rho_ci95\": [0.2094, 0.37], \"AUROC_ci95\": [0.7002, 0.7928]}, \"voting_conf\": {\"rho\": 0.3792, \"tau\": 0.2805, \"AUROC\": 0.6841, \"ECE\": 0.3807, \"rho_ci95\": [0.2972, 0.4486], \"AUROC_ci95\": [0.6249, 0.7366]}}, \"ner_cond\": {\"n\": 477, \"SJ\": {\"rho\": 0.3113, \"tau\": 0.2257, \"AUROC\": 0.6772, \"ECE\": 0.4416, \"rho_ci95\": [0.2353, 0.3959], \"AUROC_ci95\": [0.621, 0.7337]}, \"FK\": {\"rho\": 0.1761, \"tau\": 0.1284, \"AUROC\": 0.6078, \"ECE\": 0.4389, \"rho_ci95\": [0.0839, 0.2665], \"AUROC_ci95\": [0.5442, 0.6709]}, \"logprob\": {\"rho\": 0.1538, \"tau\": 0.1111, \"AUROC\": 0.5633, \"ECE\": 0.6803, \"rho_ci95\": [0.0637, 0.2424], \"AUROC_ci95\": [0.5032, 0.6232]}, \"EM\": {\"rho\": 0.3596, \"tau\": 0.2735, \"AUROC\": 0.7556, \"ECE\": 0.3257, \"rho_ci95\": [0.2819, 0.4408], \"AUROC_ci95\": [0.7011, 0.8107]}, \"voting_conf\": {\"rho\": 0.3, \"tau\": 0.2189, \"AUROC\": 0.6618, \"ECE\": 0.3746, \"rho_ci95\": [0.2168, 0.3836], \"AUROC_ci95\": [0.6004, 0.7201]}}, \"re_full\": {\"n\": 397, \"SJ\": {\"rho\": 0.2503, \"tau\": 0.1878, \"AUROC\": 0.6702, \"ECE\": 0.3865}, \"FK\": {\"rho\": 0.2752, \"tau\": 0.2117, \"AUROC\": 0.6089, \"ECE\": 0.4405}, \"logprob\": {\"rho\": 0.2662, \"tau\": 0.1951, \"AUROC\": 0.6005, \"ECE\": 0.7694}, \"EM\": {\"rho\": 0.1344, \"tau\": 0.1081, \"AUROC\": 0.7059, \"ECE\": 0.3548}, \"voting_conf\": {\"rho\": 0.3498, \"tau\": 0.2663, \"AUROC\": 0.6935, \"ECE\": 0.2724}}, \"re_cond\": {\"n\": 238, \"SJ\": {\"rho\": 0.2457, \"tau\": 0.1811, \"AUROC\": 0.6463, \"ECE\": 0.2941}, \"FK\": {\"rho\": 0.1139, \"tau\": 0.0876, \"AUROC\": 0.551, \"ECE\": 0.3424}, \"logprob\": {\"rho\": 0.0112, \"tau\": 0.0051, \"AUROC\": 0.5186, \"ECE\": 0.6464}, \"EM\": {\"rho\": 0.4165, \"tau\": 0.3256, \"AUROC\": 0.7515, \"ECE\": 0.2232}, \"voting_conf\": {\"rho\": 0.2409, \"tau\": 0.178, \"AUROC\": 0.642, \"ECE\": 0.207}}, \"delta_vs_512_ner_full_rho\": {\"SJ\": 0.0034, \"FK\": 0.0014, \"EM\": 0.0379, \"voting_conf\": -0.1226, \"logprob\": 0.0656}, \"provenance_note\": \"exp_015_v2 scierc_n8_logprob used exp_012_logprob (max_tokens=512 truncated data). voting_conf was inflated 0.502→0.379, logprob was suppressed 0.140→0.205.\"}}, \"exp_llama_scierc_seed456\": {\"status\": \"DONE\", \"metrics\": {\"greedy_f1\": 0.6457, \"oracle_f1\": 0.7574, \"headroom\": 0.1117, \"dgs_f1\": 0.6454, \"degen_rate\": 0.2741, \"degen_rate_source\": \"unified_metrics_constant_f1_gold_filtered\", \"rho_SJ_full\": 0.3663, \"rho_FK_full\": 0.3115, \"rho_logprob_full\": 0.1911, \"rho_EM_full\": 0.3088, \"rho_vc_full\": 0.4135, \"auroc_SJ_full\": 0.7061, \"auroc_EM_full\": 0.7538, \"n_valid\": 529, \"n_conditional\": 478}, \"conclusion\": \"success\"}, \"exp_007_llama_scierc_seed123\": {\"status\": \"DONE\", \"conclusion\": \"negative\", \"metrics\": {\"greedy_f1\": 0.6454, \"oracle_f1\": 0.7657, \"headroom\": 0.1204, \"degen_rate\": 0.2665, \"degen_rate_source\": \"unified_metrics_constant_f1_gold_filtered\", \"dgs_delta_pp\": -0.38, \"rho_SJ_full\": 0.3552, \"rho_voting_conf_full\": 0.4193, \"auroc_SJ_full\": 0.7092, \"auroc_EM_full\": 0.7468}}, \"exp_qwen3_4b_conll_scs_inference\": {\"status\": \"DONE\", \"metrics\": {\"greedy_f1\": 0.9251, \"oracle_f1\": 0.9408, \"oracle_headroom_pp\": 1.57, \"SJ_rho_full\": 0.4045, \"SJ_rho_cond\": 0.4306, \"FK_rho_full\": 0.3961, \"FK_rho_cond\": 0.42, \"LP_rho_full\": 0.3186, \"LP_rho_cond\": 0.3378, \"LP_auroc_full\": 0.7689, \"LP_auroc_cond\": 0.8153, \"fleiss_kappa_mean\": 0.9349, \"soft_jaccard_mean\": 0.9754, \"structural_beats_surface\": true, \"rho_advantage_pp\": 0.84, \"n_instances\": 3453, \"n_gold_empty_filtered\": 697, \"n_greedy_f1_zero_filtered\": 112, \"verdict\": \"MARGINAL\", \"degen_rate\": 0.9057, \"degen_rate_source\": \"unified_metrics_constant_f1_gold_filtered\"}, \"conclusion\": \"success\"}, \"exp_qwen3_4b_conll_scs_inference_v2\": {\"status\": \"DONE\", \"metrics\": {\"greedy_f1\": 0.9234, \"oracle_f1\": 0.9404, \"oracle_headroom_pp\": 1.7, \"SJ_rho_full\": 0.4217, \"SJ_rho_cond\": 0.459, \"FK_rho_full\": 0.4181, \"FK_rho_cond\": 0.4538, \"LP_rho_full\": 0.3313, \"LP_rho_cond\": 0.3487, \"LP_auroc_full\": 0.7761, \"LP_auroc_cond\": 0.8209, \"n_instances\": 3453, \"verdict\": \"MARGINAL\", \"degen_rate\": 0.9057, \"degen_rate_source\": \"unified_metrics_constant_f1_gold_filtered\"}, \"conclusion\": \"success\"}, \"exp_qwen3_4b_scierc_scs_inference\": {\"status\": \"DONE\", \"metrics\": {\"ner_greedy_f1\": 0.6612, \"ner_oracle_f1\": 0.7839, \"ner_headroom_pp\": 12.28, \"ner_SJ_rho\": 0.4221, \"ner_FK_rho\": 0.3258, \"ner_LP_rho\": 0.28, \"re_greedy_f1\": 0.4136, \"re_oracle_f1\": 0.5846, \"re_headroom_pp\": 17.1, \"re_SJ_rho\": 0.2673, \"re_FK_rho\": 0.3593, \"re_LP_rho\": 0.3512, \"re_sample_f1_pct_zero\": 0.476, \"re_LP_rho_cond\": 0.1135, \"re_LP_rho_cond_p\": 0.074, \"degen_rate\": 0.104, \"degen_rate_source\": \"unified_metrics_constant_f1_gold_filtered\"}, \"conclusion\": \"success\"}, \"exp_027_fewnerd_n16\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"LP_delta_pp\": 1.88, \"LP_delta_95CI\": [1.41, 2.37], \"degen_rate\": 0.0706, \"degen_rate_source\": \"unified_metrics_constant_f1_gold_filtered\", \"greedy_f1\": 0.7478, \"lp_sel_f1\": 0.7666, \"oracle_f1\": 0.902, \"headroom_pp\": 15.42, \"all_8_types_positive\": true, \"n_instances\": 5000, \"N_samples\": 16, \"bootstrap_p\": \"<0.001\"}}, \"exp_026_t12\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"temperature\": 1.2, \"task\": \"T-ablation\", \"degen_rate\": 0.1493, \"degen_rate_source\": \"unified_metrics_constant_f1_gold_filtered\"}}, \"exp_026_t08\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"temperature\": 0.8, \"task\": \"T-ablation\", \"degen_rate\": 0.2382, \"degen_rate_source\": \"unified_metrics_constant_f1_gold_filtered\"}}, \"exp_026_t05\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"temperature\": 0.5, \"task\": \"T-ablation\", \"degen_rate\": 0.414, \"degen_rate_source\": \"unified_metrics_constant_f1_gold_filtered\"}}, \"exp_026_T12\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"degen_rate\": 0.1493, \"degen_rate_source\": \"unified_metrics_constant_f1_gold_filtered\", \"lp_range_mean\": 0.075, \"lp_range_std\": 0.059, \"within_instance_rho_mean\": 0.2245, \"within_instance_rho_median\": 0.3152, \"within_instance_rho_valid_pct\": 0.875, \"greedy_f1\": 0.62, \"oracle_f1\": 0.758, \"lp_sel_f1\": 0.621, \"sj_sel_f1\": 0.597, \"em_sel_f1\": 0.596, \"vc_sel_f1\": 0.582, \"sj_rho\": 0.384, \"fk_rho\": 0.386, \"lp_rho\": 0.182, \"vc_rho\": 0.342, \"sj_auroc\": 0.683, \"lp_auroc\": 0.566}}, \"exp_026_T08\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"degen_rate\": 0.2382, \"degen_rate_source\": \"unified_metrics_constant_f1_gold_filtered\", \"lp_range_mean\": 0.043, \"lp_range_std\": 0.042, \"within_instance_rho_mean\": 0.1701, \"within_instance_rho_median\": 0.2635, \"within_instance_rho_valid_pct\": 0.728, \"greedy_f1\": 0.616, \"oracle_f1\": 0.737, \"lp_sel_f1\": 0.627, \"sj_sel_f1\": 0.619, \"em_sel_f1\": 0.611, \"vc_sel_f1\": 0.603, \"sj_rho\": 0.378, \"fk_rho\": 0.34, \"lp_rho\": 0.212, \"vc_rho\": 0.352, \"sj_auroc\": 0.662, \"lp_auroc\": 0.571}}, \"exp_026_T05\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"degen_rate\": 0.414, \"degen_rate_source\": \"unified_metrics_constant_f1_gold_filtered\", \"lp_range_mean\": 0.022, \"lp_range_std\": 0.021, \"within_instance_rho_mean\": 0.1306, \"within_instance_rho_median\": 0.2182, \"within_instance_rho_valid_pct\": 0.597, \"greedy_f1\": 0.617, \"oracle_f1\": 0.71, \"lp_sel_f1\": 0.622, \"sj_sel_f1\": 0.622, \"em_sel_f1\": 0.619, \"vc_sel_f1\": 0.61, \"sj_rho\": 0.333, \"fk_rho\": 0.341, \"lp_rho\": 0.208, \"vc_rho\": 0.353, \"sj_auroc\": 0.644, \"lp_auroc\": 0.577}}, \"exp_017_llama_conll_n16_s123_r1024\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"degen_rate\": 0.8636, \"degen_rate_source\": \"unified_metrics_constant_f1_gold_filtered\"}}, \"exp_018_llama_scierc_seed123\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"degen_rate\": 0.2665, \"degen_rate_source\": \"unified_metrics_constant_f1_gold_filtered\"}}, \"exp_018_qwen_scierc_seed456\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"degen_rate\": 0.2042, \"degen_rate_source\": \"unified_metrics_constant_f1_gold_filtered\"}}, \"exp_018_qwen_scierc_seed123\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"degen_rate\": 0.172, \"degen_rate_source\": \"unified_metrics_constant_f1_gold_filtered\"}}, \"exp_epoch_dgs_analysis\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"exp_diagnostic_calibration\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"exp_adaptive_temperature\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"exp_entity_consensus\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"exp_ccs_selection\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"exp_017_llama_conll\": {\"status\": \"DONE\", \"metrics\": {\"degeneracy_cf1_gold_filtered\": 0.894, \"n_constant_f1\": 2465, \"n_gold_filtered\": 2756, \"n_total\": 3453, \"greedy_f1\": 0.9239, \"oracle_f1\": 0.9451, \"random_f1\": 0.9207, \"headroom_pp\": 2.11, \"dgs_f1\": 0.9254, \"dgs_delta_pp\": 0.14, \"dgs_nondegen_lp_delta_pp\": 1.37, \"selection_f1\": {\"SJ\": {\"f1\": 0.9237, \"delta_pp\": -0.04}, \"FK\": {\"f1\": 0.924, \"delta_pp\": -0.02}, \"VC\": {\"f1\": 0.925, \"delta_pp\": 0.08}, \"EM\": {\"f1\": 0.9244, \"delta_pp\": 0.02}, \"LP\": {\"f1\": 0.9244, \"delta_pp\": 0.02}}, \"qe_rho_full_3seed\": {\"SJ\": {\"mean\": 0.4631, \"sd\": 0.0074}, \"FK\": {\"mean\": 0.4546, \"sd\": 0.0061}, \"EM\": {\"mean\": 0.4603, \"sd\": 0.0078}, \"VC\": {\"mean\": 0.4579, \"sd\": 0.003}, \"LP\": {\"mean\": 0.3099, \"sd\": 0.0055}}, \"qe_auroc_full_3seed\": {\"SJ\": {\"mean\": 0.736, \"sd\": 0.0064}, \"FK\": {\"mean\": 0.732, \"sd\": 0.0063}, \"EM\": {\"mean\": 0.7355, \"sd\": 0.0069}, \"VC\": {\"mean\": 0.7394, \"sd\": 0.0041}, \"LP\": {\"mean\": 0.7629, \"sd\": 0.0044}}, \"lp_range\": {\"mean\": 0.0198, \"std\": 0.0315, \"median\": 0.0002}}, \"conclusion\": \"success\"}, \"exp_017_llama_conll_finetune\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"degeneracy_rate\": 0.853, \"greedy_f1\": 0.928, \"oracle_f1\": 0.951, \"headroom\": 0.023, \"selection_f1\": 0.934, \"full_rho_SJ\": 0.45, \"full_rho_FK\": 0.443, \"full_rho_VC\": 0.437, \"full_rho_EM\": 0.448, \"full_rho_LP\": 0.273, \"full_AUROC_SJ\": 0.752, \"full_AUROC_EM\": 0.753, \"full_AUROC_LP\": 0.739, \"cond_rho_SJ\": 0.454, \"cond_rho_EM\": 0.458, \"cond_rho_LP\": 0.311, \"cond_AUROC_EM\": 0.783, \"cond_AUROC_LP\": 0.804}}, \"exp_028_entity_token_lp\": {\"status\": \"DONE\", \"conclusion\": \"negative\", \"metrics\": {\"greedy_f1\": 0.643, \"oracle_f1\": 0.7845, \"full_lp_global_rho\": 0.2971, \"entity_text_type_lp_global_rho\": 0.4401, \"full_lp_selection_f1\": 0.6465, \"entity_text_type_lp_selection_f1\": 0.6357, \"dilution_ratio\": 0.32, \"full_lp_within_range_median\": 0.0402, \"entity_text_type_within_range_median\": 0.1346, \"schema_only_within_range_median\": 0.0089}}, \"exp_026_t12_scierc\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"exp_026_t08_scierc\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"exp_026_t05_scierc\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"exp_027_mlp_verifier\": {\"status\": \"DONE\", \"metrics\": {\"lr_auroc\": 0.6522, \"mlp_auroc\": 0.6381, \"rf_auroc\": 0.5868, \"mlp_15feat_auroc\": 0.6341, \"lr_sel_f1\": 0.6406, \"mlp_sel_f1\": 0.6278, \"greedy_f1\": 0.6441, \"oracle_f1\": 0.8231, \"best_single_signal_auroc\": 0.6476, \"feature_bottleneck_confirmed\": true}, \"conclusion\": \"negative\"}, \"exp_028_fewnerd_5epoch\": {\"status\": \"DONE\", \"conclusion\": \"negative\", \"metrics\": {\"degeneracy_cf1_gold\": 0.3133, \"greedy_f1\": 0.7773, \"lp_sel_delta_pp\": 0.624, \"lp_sel_f1\": 0.7835, \"oracle_f1\": 0.8723, \"within_instance_rho_mean\": 0.4066, \"within_instance_rho_median\": 0.6151}}, \"exp_028\": {\"status\": \"DONE\", \"conclusion\": \"negative\", \"metrics\": {\"degeneracy_cf1_gold\": 0.313, \"greedy_f1\": 0.7773, \"lp_sel_f1\": 0.7835, \"lp_sel_delta_pp\": 0.62, \"oracle_f1\": 0.8723, \"within_instance_rho\": 0.4066, \"train_loss\": 0.0189, \"eval_loss\": 0.0311}}, \"exp_024_claim_audit\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"consistent\": 97, \"errors\": 1, \"warnings\": 5, \"old_residuals_found\": 0}}, \"exp_016_rerun_1024_bootstrap\": {\"status\": \"DONE\", \"conclusion\": \"negative\", \"metrics\": {\"bootstrap_ci_95\": [-0.03, 0.042], \"permutation_p\": 0.39, \"cohen_d\": 0.038, \"sign_test_win_rate\": 0.466, \"ner_logprob_vs_greedy_delta\": 0.006, \"conclusion_summary\": \"NER selection: no signal significantly outperforms greedy; RE: same conclusion\"}}, \"exp_verbalized_confidence\": {\"status\": \"DONE\", \"conclusion\": \"negative\", \"metrics\": {\"scierc\": {\"VerbConf_rho\": 0.2965, \"VerbConf_auroc\": 0.6811, \"VerbConf_sel_f1\": 0.6195, \"VerbConf_delta\": -0.0245, \"best_existing_rho\": 0.3792, \"VerbConf_mean\": 8.58, \"VerbConf_std\": 1.15, \"parse_fail_rate\": 0.0026}, \"conll\": {\"VerbConf_rho\": 0.3366, \"VerbConf_auroc\": 0.7469, \"VerbConf_sel_f1\": 0.8886, \"VerbConf_delta\": -0.0193, \"best_existing_rho\": 0.4507, \"VerbConf_mean\": 9.24, \"VerbConf_std\": 1.32, \"parse_fail_rate\": 0}}}, \"exp_entity_token_lp\": {\"status\": \"DONE\", \"conclusion\": \"negative\", \"metrics\": {\"scierc_ner\": {\"greedy_f1\": 0.643, \"full_lp_sel_f1\": 0.6465, \"entity_lp_sel_f1\": 0.6262, \"oracle_f1\": 0.7845, \"entity_lp_delta_vs_full_lp\": -0.0203}, \"conll_ner\": {\"greedy_f1\": 0.9065, \"full_lp_sel_f1\": 0.8989, \"entity_lp_sel_f1\": 0.8659, \"oracle_f1\": 0.948, \"entity_lp_delta_vs_full_lp\": -0.033}, \"finding\": \"entity-token LP strictly worse than full-sequence LP; CoNLL entity tokens saturated (79.4% tied), SciERC entity tokens too sparse (5.3% of total)\"}}, \"exp_freeform_ablation\": {\"status\": \"DONE\", \"conclusion\": \"negative\", \"metrics\": {\"lp_std_ratio_free_vs_constrained\": 0.97, \"lp_range_ratio\": 0.96, \"tied_fraction_constrained\": 0.597, \"tied_fraction_freeform\": 0.577, \"ner_selection_gap_constrained\": 0.0059, \"ner_selection_gap_freeform\": 0.0018, \"re_selection_gap_constrained\": -0.0068, \"re_selection_gap_freeform\": 0.0169, \"parse_rate\": 0.9995, \"ner_vc_rho_constrained\": 0.3792, \"ner_vc_rho_freeform\": 0.4089}}, \"exp_008_re_n16\": {\"status\": \"DONE\", \"metrics\": {\"ner\": {\"greedy_f1\": 0.6635, \"oracle_f1\": 0.8208, \"headroom\": 0.1572, \"rho_sj_full\": 0.377, \"rho_fk_full\": 0.2508, \"rho_logprob_full\": 0.3153, \"rho_sj_cond\": 0.3598, \"rho_fk_cond\": 0.2251, \"rho_logprob_cond\": 0.2927, \"sj_beats_fk\": true, \"rho_advantage\": 0.1262}, \"re\": {\"greedy_f1\": 0.4339, \"oracle_f1\": 0.6658, \"headroom\": 0.2319, \"rho_sj_full\": 0.2966, \"rho_fk_full\": 0.2871, \"rho_logprob_full\": 0.2986, \"rho_sj_cond\": 0.3975, \"rho_fk_cond\": 0.3774, \"rho_logprob_cond\": 0.2745, \"sj_beats_fk\": true, \"rho_advantage\": 0.0095}, \"verdict\": \"FAIL\"}, \"conclusion\": \"success\"}, \"exp_001_ner_n16_seed123\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"ner\": {\"greedy_f1\": 0.663, \"oracle_f1\": 0.809, \"headroom\": 0.146, \"rho_sj\": 0.423, \"rho_fk\": 0.29, \"rho_logprob\": 0.239, \"rho_sj_cond\": 0.423, \"rho_fk_cond\": 0.26}, \"re\": {\"greedy_f1\": 0.419, \"oracle_f1\": 0.625, \"headroom\": 0.206, \"rho_sj\": 0.267, \"rho_fk\": 0.315, \"rho_sj_cond\": 0.364, \"rho_fk_cond\": 0.331}, \"verdict\": \"FAIL\", \"verdict_note\": \"RE rho_sj=0.267 < 0.40; RE >30% samples F1=0\", \"n_instances\": 551, \"seed\": 123, \"N\": 16, \"T\": 1}}, \"exp_007_ner_multi_model\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"epoch\": 5, \"train_loss\": 0.0767, \"eval_loss\": 0.1049, \"train_runtime_sec\": 1494.5, \"train_samples_per_second\": 6.226, \"checkpoints\": [\"checkpoint-400\", \"checkpoint-500\", \"checkpoint-585\"], \"base_model\": \"Meta-Llama-3.1-8B-Instruct\", \"lora_r\": 32, \"lora_alpha\": 64, \"note\": \"EXIT_CODE=129 (SIGHUP) but training completed all 5 epochs before signal. Checkpoint fully intact.\"}}, \"exp_003_ner_wnut17\": {\"status\": \"DONE\", \"metrics\": {\"ner\": {\"greedy_f1\": 0.525, \"oracle_f1\": 0.664, \"headroom\": 0.139, \"rho_sj_full\": 0.082, \"rho_fk_full\": 0.124, \"rho_logprob_full\": -0.414, \"rho_sj_cond\": 0.275, \"rho_fk_cond\": 0.164, \"rho_logprob_cond\": 0.352, \"sj_beats_logprob_cond\": false}, \"n_instances\": 1287, \"n_gold_empty\": 598, \"sample_f1_mean\": 0.401, \"sample_f1_pct_zero\": 53.7, \"N\": 16, \"T\": 1, \"seed\": 42, \"verdict\": \"FAIL\", \"verdict_note\": \">30% samples F1=0; structural rho weak; logprob baseline stronger\"}, \"conclusion\": \"negative\"}, \"exp_001_seed456_t10_full\": {\"status\": \"DONE\", \"conclusion\": \"negative\", \"metrics\": {\"ner\": {\"rho_sj\": 0.414, \"rho_fk\": 0.298}, \"re\": {\"rho_sj\": 0.268, \"rho_fk\": 0.26}, \"n_instances\": 551, \"N\": 16, \"T\": 1, \"seed\": 456, \"source\": \"reviewer_verified_report_json\"}}, \"exp_001_seed123_t10_full\": {\"status\": \"DONE\", \"conclusion\": \"negative\", \"metrics\": {\"ner\": {\"rho_sj\": 0.417, \"rho_fk\": 0.283}, \"re\": {\"rho_sj\": 0.265, \"rho_fk\": 0.315}, \"n_instances\": 551, \"N\": 16, \"T\": 1, \"seed\": 123, \"source\": \"reviewer_verified_report_json\"}}, \"exp_008_re_n16_t10_full\": {\"status\": \"DONE\", \"conclusion\": \"negative\", \"metrics\": {\"ner\": {\"rho_sj\": 0.444}, \"re\": {\"rho_sj\": 0.248}, \"n_instances\": 551, \"N\": 16, \"T\": 1, \"seed\": 42, \"mode\": \"RE-only\", \"source\": \"director_corrected\"}}, \"exp_007_llama_inference\": {\"status\": \"DONE\", \"metrics\": {\"ner\": {\"greedy_f1\": 0.66, \"oracle_f1\": 0.781, \"headroom\": 0.121, \"rho_fk\": 0.327, \"rho_sj\": 0.363, \"rho_fk_cond\": 0.226, \"rho_sj_cond\": 0.311, \"rho_logprob\": 0.183, \"rho_logprob_cond\": 0.109, \"structural_beats_surface\": true, \"sample_f1_pct_zero\": 11.6}, \"re\": {\"greedy_f1\": 0.434, \"oracle_f1\": 0.568, \"headroom\": 0.135, \"rho_fk\": 0.305, \"rho_sj\": 0.299, \"rho_fk_cond\": 0.259, \"rho_sj_cond\": 0.405, \"rho_logprob\": 0.288, \"rho_logprob_cond\": 0.092, \"structural_beats_surface\": false, \"sample_f1_pct_zero\": 41.2}, \"n_instances\": 551, \"N\": 8, \"T\": 1, \"seed\": 42, \"model\": \"LLaMA-3.1-8B-Instruct\", \"verdict\": \"FAIL\", \"verdict_note\": \"RE rho_sj_full=0.299 < 0.40; >30% RE samples F1=0\"}, \"conclusion\": \"success\"}, \"exp_003_wnut17_eval\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"greedy_f1\": 0.523, \"oracle_f1\": 0.664, \"headroom\": 0.141, \"rho_fk\": 0.125, \"rho_sj\": 0.089, \"rho_fk_cond\": 0.169, \"rho_sj_cond\": 0.288, \"rho_logprob_full\": -0.409, \"rho_logprob_cond\": 0.35, \"structural_beats_surface\": false, \"sample_f1_pct_zero\": 53.7, \"n_instances\": 1287, \"N\": 16, \"T\": 1, \"seed\": 42, \"model\": \"Qwen3-8B\", \"n_gold_empty_filtered\": 598, \"verdict\": \"FAIL\", \"verdict_note\": \"structural_beats_surface=false; >50% samples F1=0\"}}, \"exp_010_selection_curves\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"scierc_ner\": {\"n_instances\": 551, \"greedy_f1\": 0.618, \"N16\": {\"oracle\": 0.787, \"SJ\": 0.62, \"FK\": 0.621, \"logprob\": 0.621, \"voting_conf\": 0.585, \"EM\": 0.606, \"random\": 0.595}, \"N8\": {\"oracle\": 0.752, \"SJ\": 0.614, \"FK\": 0.614, \"logprob\": 0.619, \"voting_conf\": 0.591, \"EM\": 0.603, \"random\": 0.589}, \"N4\": {\"oracle\": 0.714, \"SJ\": 0.607, \"FK\": 0.608, \"logprob\": 0.616, \"voting_conf\": 0.594, \"EM\": 0.6, \"random\": 0.587}}, \"scierc_re\": {\"n_instances\": 397, \"greedy_f1\": 0.403, \"N16\": {\"oracle\": 0.631, \"SJ\": 0.397, \"FK\": 0.396, \"logprob\": 0.41, \"voting_conf\": 0.408, \"EM\": 0.381, \"random\": 0.364}, \"N8\": {\"oracle\": 0.583, \"SJ\": 0.393, \"FK\": 0.394, \"logprob\": 0.413, \"voting_conf\": 0.398, \"EM\": 0.381, \"random\": 0.363}}, \"conll_ner\": {\"n_instances\": 3453, \"greedy_f1\": 0.725, \"N8\": {\"oracle\": 0.757, \"SJ\": 0.718, \"FK\": 0.717, \"logprob\": 0.716, \"voting_conf\": 0.714, \"EM\": 0.716, \"random\": 0.69}, \"N4\": {\"oracle\": 0.746, \"SJ\": 0.714, \"FK\": 0.714, \"logprob\": 0.715, \"voting_conf\": 0.714, \"EM\": 0.712, \"random\": 0.692}}}}, \"exp_007_llama_seed456\": {\"status\": \"DONE\", \"conclusion\": \"negative\", \"metrics\": {\"verdict\": \"FAIL\", \"ner\": {\"greedy_f1\": 0.6597, \"oracle_f1\": 0.7575, \"oracle_headroom\": 0.0978, \"fleiss_kappa\": 0.4543, \"soft_jaccard\": 0.7491, \"rho_kappa_f1\": 0.3115, \"rho_sj_f1\": 0.3663, \"structural_gt_surface\": true}, \"re\": {\"greedy_f1\": 0.4334, \"oracle_f1\": 0.5789, \"oracle_headroom\": 0.1455, \"fleiss_kappa\": 0.3791, \"soft_jaccard\": 0.6782, \"rho_kappa_f1\": 0.3013, \"rho_sj_f1\": 0.287, \"structural_gt_surface\": false}, \"logprob_ner\": {\"rho\": 0.1911, \"auroc\": 0.5989}, \"logprob_re\": {\"rho\": 0.3246, \"auroc\": 0.6678}, \"fail_reason\": \"RE rho_sj=0.2870 < 0.40 threshold; >30% samples F1=0\"}}, \"exp_007_llama_seed123\": {\"status\": \"DONE\", \"conclusion\": \"negative\", \"metrics\": {\"verdict\": \"FAIL\", \"ner\": {\"greedy_f1\": 0.6605, \"oracle_f1\": 0.7703, \"headroom\": 0.1098, \"fleiss_kappa\": 0.4553, \"soft_jaccard\": 0.7525, \"rho_kappa_f1\": 0.2143, \"rho_sj_f1\": 0.3371, \"structural_gt_surface\": true}, \"re\": {\"greedy_f1\": 0.433, \"oracle_f1\": 0.5719, \"headroom\": 0.1389, \"fleiss_kappa\": 0.3851, \"soft_jaccard\": 0.6911, \"rho_kappa_f1\": 0.2844, \"rho_sj_f1\": 0.268, \"structural_gt_surface\": false}, \"fail_reasons\": [\"RE rho_sj=0.2680 < 0.40 threshold\", \">30% samples F1=0 (RE: 41.0%)\", \"RE structural not > surface (delta=-0.0165)\"]}}, \"exp_008_re_seed123\": {\"status\": \"DONE\", \"conclusion\": \"negative\", \"metrics\": {\"greedy_f1\": 0.4229, \"oracle_f1\": 0.6244, \"oracle_headroom\": 0.2015, \"fleiss_kappa_mean\": 0.3455, \"soft_jaccard_mean\": 0.6126, \"sample_f1_mean\": 0.3594, \"sample_f1_std\": 0.3793, \"sample_f1_zero_pct\": 44.1, \"structural_gt_surface\": false, \"rho_kappa_f1_full\": 0.3174, \"rho_sj_f1_full\": 0.2835, \"rho_kappa_f1_cond\": 0.0766, \"rho_sj_f1_cond\": 0.2877, \"logprob_auroc_full\": 0.6499, \"logprob_auroc_cond\": 0.5265, \"verdict\": \"FAIL\"}}, \"exp_001_seed42_v2\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"sj_rho_full\": 0.428, \"sj_rho_cond\": 0.369, \"structural_minus_surface\": 0.147, \"conclusion_note\": \"NER seed42 robustness confirmed, structural>surface +0.147\"}}, \"exp_001_seed123_v2\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"sj_rho_full\": 0.424, \"sj_rho_cond\": 0.376, \"structural_minus_surface\": 0.149, \"conclusion_note\": \"NER seed123 robustness confirmed, structural>surface +0.149\"}}, \"exp_008_re_n16_v2\": {\"status\": \"DONE\", \"conclusion\": \"negative\", \"metrics\": {\"sj_rho_full\": 0.281, \"sj_rho_cond\": 0.308, \"f1_zero_pct\": 44.3, \"conclusion_note\": \"RE N=16 v2 negative: SJ weak, 44.3% F1=0\"}}, \"exp_005_v2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"exp_006_v2\": {\"status\": \"DONE\", \"conclusion\": \"negative\", \"metrics\": {\"NER_SciERC_s42\": {\"greedy\": 0.618, \"oracle\": 0.787, \"SJ\": 0.62, \"logprob\": 0.621, \"FK\": 0.621, \"EM\": 0.606, \"voting_conf\": 0.585, \"random\": 0.586}, \"NER_SciERC_s123\": {\"greedy\": 0.618, \"oracle\": 0.785, \"SJ\": 0.617, \"logprob\": 0.618, \"FK\": 0.621, \"EM\": 0.613, \"voting_conf\": 0.584, \"random\": 0.583}, \"NER_CoNLL\": {\"greedy\": 0.725, \"oracle\": 0.757, \"SJ\": 0.718, \"logprob\": 0.716, \"FK\": 0.717, \"EM\": 0.716, \"voting_conf\": 0.714, \"random\": 0.692}, \"RE_SciERC\": {\"greedy\": 0.403, \"oracle\": 0.631, \"SJ\": 0.397, \"logprob\": 0.41, \"FK\": 0.396, \"EM\": 0.381, \"voting_conf\": 0.408, \"random\": 0.364}}}, \"exp_004_v2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"exp_009_v2\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"ner_seed42_global\": {\"sj_rho\": 0.431, \"fk_rho\": 0.325, \"logprob_rho\": 0.203, \"voting_conf_rho\": 0.475, \"em_rho\": 0.292}, \"ner_seed123_global\": {\"sj_rho\": 0.422, \"fk_rho\": 0.315, \"logprob_rho\": 0.226, \"voting_conf_rho\": 0.438, \"em_rho\": 0.299}, \"re_seed42_global\": {\"sj_rho\": 0.063, \"fk_rho\": 0.226, \"logprob_rho\": 0.4, \"voting_conf_rho\": 0.22, \"em_rho\": -0.132}, \"ner_seed_stability_max_delta\": 0.037, \"independent_proxies\": [\"sent_len\", \"ent_count\", \"type_diversity\"], \"inverted_u_ner\": \"not confirmed (ρ stable across independent proxies)\", \"inverted_u_re\": \"monotonic increase with complexity, not inverted-U\"}}, \"exp_016_v2\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"ner_conditional\": {\"n\": 529, \"best_single_signal_rho\": {\"soft_jaccard\": 0.4412}, \"best_combo_rho\": {\"sj+vc_a0.55\": 0.4552}, \"ensemble_auroc\": 0.7141, \"best_single_auroc\": {\"soft_jaccard\": 0.7166}, \"selection_f1\": {\"greedy\": 0.6442, \"logprob_best\": 0.6505, \"ensemble_best\": 0.6475, \"sj_best\": 0.6471, \"oracle\": 0.8442}}, \"re_conditional\": {\"n\": 397, \"best_single_signal_rho\": {\"voting_confidence\": 0.3849}, \"best_combo_rho\": {\"logprob+vc_a0.25\": 0.3936}, \"ensemble_auroc\": 0.6916, \"best_single_auroc\": {\"voting_confidence\": 0.7023}, \"selection_f1\": {\"greedy\": 0.403, \"logprob_best\": 0.4097, \"ensemble_best\": 0.4227, \"oracle\": 0.6306}}, \"re_full\": {\"ensemble_auroc\": 0.8608, \"best_single_auroc\": {\"voting_confidence\": 0.8248}}}}, \"exp_001_seed456_v2\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"exp_017_llama_conll_infer\": {\"status\": \"DONE\", \"metrics\": {\"greedy_f1\": 0.9266, \"oracle_f1\": 0.9443, \"oracle_headroom\": 0.0177, \"n_instances\": 3453, \"n_valid\": 2756, \"n_conditional\": 2642, \"N\": 8, \"full\": {\"SJ_rho\": 0.4314, \"FK_rho\": 0.4277, \"logprob_rho\": 0.3072, \"EM_rho\": 0.4306, \"voting_conf_rho\": 0.4256, \"SJ_AUROC\": 0.7039, \"FK_AUROC\": 0.7026, \"logprob_AUROC\": 0.761, \"EM_AUROC\": 0.7046, \"voting_conf_AUROC\": 0.7088, \"SJ_ECE\": 0.1137, \"FK_ECE\": 0.1053, \"logprob_ECE\": 0.129, \"EM_ECE\": 0.1094, \"voting_conf_ECE\": 0.0949}, \"conditional\": {\"SJ_rho\": 0.4356, \"FK_rho\": 0.431, \"logprob_rho\": 0.3282, \"EM_rho\": 0.4403, \"voting_conf_rho\": 0.3743, \"SJ_AUROC\": 0.7225, \"FK_AUROC\": 0.7208, \"logprob_AUROC\": 0.8102, \"EM_AUROC\": 0.7257, \"voting_conf_AUROC\": 0.6989, \"SJ_ECE\": 0.0829, \"FK_ECE\": 0.0796, \"logprob_ECE\": 0.0922, \"EM_ECE\": 0.0754, \"voting_conf_ECE\": 0.0784}}, \"conclusion\": \"success\"}, \"exp_003_wnut17_v2\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"exp_001_seed456_v2_ner\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"full\": {\"SJ\": {\"rho\": 0.384, \"auroc\": 0.711}, \"FK\": {\"rho\": 0.223, \"auroc\": 0.577}, \"logprob\": {\"rho\": 0.232, \"auroc\": 0.594}, \"EM\": {\"rho\": 0.316, \"auroc\": 0.768}, \"voting_conf\": {\"rho\": 0.411, \"auroc\": 0.712}}, \"conditional\": {\"SJ\": {\"rho\": 0.349, \"auroc\": 0.699}, \"FK\": {\"rho\": 0.157, \"auroc\": 0.561}, \"logprob\": {\"rho\": 0.171, \"auroc\": 0.576}, \"EM\": {\"rho\": 0.406, \"auroc\": 0.78}, \"voting_conf\": {\"rho\": 0.346, \"auroc\": 0.694}}, \"3seed_mean_SJ_rho_full\": 0.412, \"3seed_sd_SJ_rho_full\": 0.025, \"structural_beats_surface\": true, \"verdict\": \"MARGINAL\"}}, \"exp_009_v2_re_rerun\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"exp_007_llama_n16\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"N\": 16, \"dataset\": \"scierc\", \"subtask\": \"ner\", \"n_instances\": 551, \"n_valid\": 529, \"n_conditional\": 478, \"greedy_f1\": 0.645, \"full\": {\"SJ_rho\": 0.3791, \"FK_rho\": 0.3081, \"logprob_rho\": 0.2041, \"EM_rho\": 0.3159, \"voting_conf_rho\": 0.4515, \"SJ_AUROC\": 0.717, \"FK_AUROC\": 0.6581, \"logprob_AUROC\": 0.5656, \"EM_AUROC\": 0.7686, \"voting_conf_AUROC\": 0.7266, \"SJ_ECE\": 0.1019, \"FK_ECE\": 0.1556, \"logprob_ECE\": 0.084, \"EM_ECE\": 0.1761, \"voting_conf_ECE\": 0.1365}, \"conditional\": {\"SJ_rho\": 0.3222, \"FK_rho\": 0.2182, \"logprob_rho\": 0.1286, \"EM_rho\": 0.3563, \"voting_conf_rho\": 0.3356, \"SJ_AUROC\": 0.7014, \"FK_AUROC\": 0.6392, \"logprob_AUROC\": 0.545, \"EM_AUROC\": 0.7708, \"voting_conf_AUROC\": 0.6988, \"SJ_ECE\": 0.1466, \"FK_ECE\": 0.1853, \"logprob_ECE\": 0.1141, \"EM_ECE\": 0.1887, \"voting_conf_ECE\": 0.2634}, \"n8_vs_n16_delta_rho_full\": {\"SJ\": 0.0161, \"FK\": -0.0185, \"logprob\": 0.0214, \"EM\": 0.0007, \"voting_conf\": 0.0184}}}, \"exp_017_llama_conll_n16\": {\"status\": \"DONE\", \"metrics\": {\"greedy_f1\": 0.9243, \"oracle_f1\": 0.9487, \"oracle_headroom\": 0.0244, \"n_instances\": 3453, \"n_valid\": 2756, \"n_conditional\": 2642, \"structural_beats_surface\": true, \"full\": {\"SJ_rho\": 0.4642, \"SJ_AUROC\": 0.7391, \"SJ_ECE\": 0.1131, \"FK_rho\": 0.4566, \"FK_AUROC\": 0.736, \"FK_ECE\": 0.1071, \"logprob_rho\": 0.3058, \"logprob_AUROC\": 0.7594, \"logprob_ECE\": 0.1288, \"EM_rho\": 0.4613, \"EM_AUROC\": 0.7391, \"EM_ECE\": 0.1084, \"voting_conf_rho\": 0.4554, \"voting_conf_AUROC\": 0.7406, \"voting_conf_ECE\": 0.0844}, \"conditional\": {\"SJ_rho\": 0.4597, \"SJ_AUROC\": 0.7565, \"SJ_ECE\": 0.0846, \"FK_rho\": 0.4515, \"FK_AUROC\": 0.753, \"FK_ECE\": 0.0813, \"logprob_rho\": 0.3193, \"logprob_AUROC\": 0.8023, \"logprob_ECE\": 0.0921, \"EM_rho\": 0.4618, \"EM_AUROC\": 0.7589, \"EM_ECE\": 0.0757, \"voting_conf_rho\": 0.3978, \"voting_conf_AUROC\": 0.7287, \"voting_conf_ECE\": 0.0742}, \"best_of_n\": {\"greedy\": 0.9243, \"random_avg\": 0.9213, \"sj_best\": 0.9259, \"logprob_best\": 0.925, \"voting_conf_best\": 0.9268, \"oracle\": 0.9487}, \"n8_vs_n16_delta\": {\"full_SJ_rho_delta\": 0.0328, \"full_FK_rho_delta\": 0.0289, \"full_logprob_rho_delta\": -0.0014, \"full_EM_rho_delta\": 0.0307, \"full_voting_conf_rho_delta\": 0.0298, \"cond_SJ_rho_delta\": 0.0241, \"cond_FK_rho_delta\": 0.0205, \"cond_logprob_rho_delta\": -0.0089, \"cond_EM_rho_delta\": 0.0215, \"cond_voting_conf_rho_delta\": 0.0235}}, \"conclusion\": \"success\"}, \"exp_015_v2\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"scierc_ner_avg\": {\"sj_auroc\": 0.7394, \"fk_auroc\": 0.6172, \"em_auroc\": 0.7873, \"voting_auroc\": 0.7367, \"logprob_auroc\": 0.5918}, \"scierc_re_avg\": {\"sj_auroc\": 0.6746, \"fk_auroc\": 0.5939, \"em_auroc\": 0.715, \"voting_auroc\": 0.7234, \"logprob_auroc\": 0.5849}}}, \"exp_001_n16_seed456\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"instance_count\": 551, \"n_valid\": 529, \"n_gold_empty\": 22, \"parse_rate\": 1, \"ner_greedy_f1\": 0.6617, \"ner_oracle_f1\": 0.8075, \"re_greedy_f1\": 0.4215, \"re_oracle_f1\": 0.4748, \"rho_sj_ner\": 0.4098, \"rho_fk_ner\": 0.2723, \"rho_vc_ner\": 0.4449, \"rho_em_ner\": 0.3363, \"rho_lp_ner\": 0.2415, \"rho_sj_re\": 0.2835, \"rho_fk_re\": 0.2929, \"auroc_sj_ner\": 0.6823, \"auroc_fk_ner\": 0.6179, \"auroc_vc_ner\": 0.6981, \"auroc_em_ner\": 0.649, \"auroc_lp_ner\": 0.5885, \"rho_note\": \"CORRECTED 2026-05-15: old values (rho_fk=0.3448,rho_sj=0.4134) included 22 gold-empty instances. Now uses gold-filtered pipeline (n=529).\"}}, \"exp_011_ood_scierc_to_conll\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"greedy_ner_f1\": 0.522, \"rho_vc\": 0.469, \"rho_sj\": 0.378, \"rho_em\": 0.3, \"rho_fk\": 0.285, \"rho_lp\": 0.246}}, \"exp_qwen3_4b_scierc_finetune_v4\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"total_steps\": 585, \"completed_steps\": 585, \"best_checkpoint\": \"checkpoint-400\", \"best_eval_loss\": 0.0898, \"epochs\": 5}}, \"exp_011_ood_conll_to_scierc\": {\"status\": \"DONE\", \"conclusion\": \"negative\", \"metrics\": {\"greedy_ner_f1\": 0.009, \"greedy_re_f1\": 0.001, \"avg_structural_rho\": -0.05, \"verdict\": \"FAIL\", \"reason\": \"schema_incompatibility\", \"direction\": \"CoNLL_model_to_SciERC_data\", \"sample_f1_pct_zero_ner\": 98.06, \"rho_sj_ner\": -0.186, \"rho_fk_ner\": -0.069, \"note\": \"Schema incompatibility (CoNLL PER/ORG/LOC/MISC vs SciERC Task/Method/Material) causes catastrophic failure. Cannot evaluate confidence signals.\"}}, \"exp_freeform_seed789_v3\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"n_instances\": 551, \"n_samples\": 8, \"parse_rate_pct\": 100, \"elapsed_seconds\": 229.7, \"freeform_ner_selection_gap\": 0.0028, \"freeform_re_selection_gap\": 0.0219, \"freeform_lp_std\": 0.0183, \"freeform_lp_range\": 0.054908, \"freeform_tied_pct\": 59, \"re_lp_flip_positive\": true, \"variance_ratio_std\": 0.89, \"variance_ratio_range\": 0.88}}, \"exp_freeform_seed789\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"inference\": {\"n_instances\": 551, \"n_samples\": 8, \"total_samples\": 4408, \"total_parsed\": 4408, \"parse_rate_pct\": 100, \"elapsed_seconds\": 227.5}, \"freeform\": {\"selection_ner\": {\"greedy\": 0.6205, \"selected\": 0.6232, \"gap\": 0.0027}, \"selection_re\": {\"greedy\": 0.2909, \"selected\": 0.31, \"gap\": 0.0191}, \"logprob_variance\": {\"mean_std\": 0.0183, \"mean_range\": 0.054908, \"tied_pct\": 59}, \"qe_ner\": {\"n\": 529, \"SJ\": {\"rho\": 0.393995, \"auroc\": 0.734474}, \"FK\": {\"rho\": 0.312292, \"auroc\": 0.794384}, \"LP\": {\"rho\": 0.247096, \"auroc\": 0.677824}, \"EM\": {\"rho\": 0.320383, \"auroc\": 0.527033}, \"VC\": {\"rho\": 0.420625, \"auroc\": 0.768111}}, \"qe_re\": {\"n\": 397, \"SJ\": {\"rho\": 0.201746, \"auroc\": 0.574388}, \"FK\": {\"rho\": 0.2202, \"auroc\": 0.633014}, \"LP\": {\"rho\": 0.295765, \"auroc\": 0.687067}, \"EM\": {\"rho\": 0.103633, \"auroc\": 0.474737}, \"VC\": {\"rho\": 0.306868, \"auroc\": 0.642197}}}, \"constrained_ref\": {\"selection_ner\": {\"greedy\": 0.6182, \"selected\": 0.6241, \"gap\": 0.0059}, \"selection_re\": {\"greedy\": 0.2913, \"selected\": 0.2845, \"gap\": -0.0068}, \"logprob_variance\": {\"mean_std\": 0.020589, \"mean_range\": 0.062305, \"tied_pct\": 59.7}}, \"comparison\": {\"variance_ratio_std\": 0.89, \"variance_ratio_range\": 0.88, \"tied_reduction_pp\": 0.7}}}, \"exp_freeform_seed456\": {\"status\": \"DONE\", \"metrics\": {\"inference\": {\"n_instances\": 551, \"n_samples\": 8, \"total_samples\": 4408, \"total_parsed\": 4407, \"parse_rate_pct\": 99.98, \"elapsed_seconds\": 232.4}, \"freeform\": {\"selection_ner\": {\"greedy\": 0.6198, \"selected\": 0.6205, \"gap\": 0.0007}, \"selection_re\": {\"greedy\": 0.2908, \"selected\": 0.3108, \"gap\": 0.02}, \"logprob_variance\": {\"mean_std\": 0.018631, \"mean_range\": 0.056792, \"tied_pct\": 58.4}, \"qe_ner\": {\"n\": 529, \"SJ\": {\"rho\": 0.378498, \"auroc\": 0.707769}, \"FK\": {\"rho\": 0.286163, \"auroc\": 0.754779}, \"LP\": {\"rho\": 0.227089, \"auroc\": 0.672081}, \"EM\": {\"rho\": 0.319997, \"auroc\": 0.47789}, \"VC\": {\"rho\": 0.416853, \"auroc\": 0.756543}}, \"qe_re\": {\"n\": 397, \"SJ\": {\"rho\": 0.211331, \"auroc\": 0.572335}, \"FK\": {\"rho\": 0.259074, \"auroc\": 0.652998}, \"LP\": {\"rho\": 0.306382, \"auroc\": 0.70134}, \"EM\": {\"rho\": 0.1043, \"auroc\": 0.461641}, \"VC\": {\"rho\": 0.301507, \"auroc\": 0.628873}}}, \"constrained_ref\": {\"selection_ner\": {\"greedy\": 0.6182, \"selected\": 0.6241, \"gap\": 0.0059}, \"selection_re\": {\"greedy\": 0.2913, \"selected\": 0.2845, \"gap\": -0.0068}, \"logprob_variance\": {\"mean_std\": 0.020589, \"mean_range\": 0.062305, \"tied_pct\": 59.7}}, \"comparison\": {\"variance_ratio_std\": 0.9, \"variance_ratio_range\": 0.91, \"tied_reduction_pp\": 1.3}}, \"conclusion\": \"success\"}, \"exp_freeform_seed123\": {\"status\": \"DONE\", \"metrics\": {\"inference\": {\"n_instances\": 551, \"n_samples\": 8, \"total_samples\": 4408, \"total_parsed\": 4406, \"parse_rate_pct\": 99.95, \"elapsed_seconds\": 228.1}, \"freeform\": {\"selection_ner\": {\"greedy\": 0.6194, \"selected\": 0.6222, \"gap\": 0.0028}, \"selection_re\": {\"greedy\": 0.2874, \"selected\": 0.305, \"gap\": 0.0176}, \"logprob_variance\": {\"mean_std\": 0.019881, \"mean_range\": 0.059864, \"tied_pct\": 57.7}, \"qe_ner\": {\"n\": 529, \"SJ\": {\"rho\": 0.384214, \"auroc\": 0.748728}, \"FK\": {\"rho\": 0.323956, \"auroc\": 0.766039}, \"logprob\": {\"rho\": 0.217297, \"auroc\": 0.701657}, \"EM\": {\"rho\": 0.326887, \"auroc\": 0.52533}, \"voting_conf\": {\"rho\": 0.407893, \"auroc\": 0.799676}}, \"qe_re\": {\"n\": 397, \"SJ\": {\"rho\": 0.272776, \"auroc\": 0.614056}, \"FK\": {\"rho\": 0.314429, \"auroc\": 0.678534}, \"logprob\": {\"rho\": 0.309673, \"auroc\": 0.70414}, \"EM\": {\"rho\": 0.137216, \"auroc\": 0.487342}, \"voting_conf\": {\"rho\": 0.316667, \"auroc\": 0.647442}}}, \"constrained_ref\": {\"selection_ner\": {\"greedy\": 0.6182, \"selected\": 0.6241, \"gap\": 0.0059}, \"selection_re\": {\"greedy\": 0.2913, \"selected\": 0.2845, \"gap\": -0.0068}}, \"comparison\": {\"variance_ratio_std\": 0.97, \"variance_ratio_range\": 0.96, \"tied_reduction_pp\": 2}}, \"conclusion\": \"success\"}, \"exp_009_capability_stratification\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"scierc_ner\": {\"n\": 551, \"sj_rho_overall\": 0.398, \"by_greedy_f1\": {\"hard_0_25_sj_rho\": 0.159, \"med_low_sj_rho\": 0.139, \"med_high_sj_rho\": 0.09, \"easy_sj_rho\": 0.23}, \"by_sent_len\": {\"Q1_sj_rho\": 0.461, \"Q2_sj_rho\": 0.401, \"Q3_sj_rho\": 0.296, \"Q4_sj_rho\": 0.382}, \"by_ent_count\": {\"0_sj_rho\": 0.689, \"1_2_sj_rho\": 0.415, \"3_5_sj_rho\": 0.353, \"6plus_sj_rho\": 0.547}}, \"scierc_re\": {\"n\": 551, \"by_greedy_f1\": {\"hard_0_25_sj_rho\": -0.043, \"easy_sj_rho\": 0.21}, \"by_sent_len\": {\"Q1_sj_rho\": 0.447, \"Q4_sj_rho\": 0.54}, \"by_rel_count\": {\"0_sj_rho\": 0.62, \"1_2_sj_rho\": 0.275, \"6plus_sj_rho\": 0.527}}, \"conll_ner\": {\"n\": 3453, \"by_sent_len\": {\"Q1_sj_rho\": 0.334, \"Q3_sj_rho\": 0.518}}, \"proxy_independence\": {\"scierc_ner_f1_vs_slen\": -0.021, \"scierc_ner_f1_vs_ecnt\": 0.007, \"scierc_re_f1_vs_slen\": -0.147}}}, \"exp_023_lora_rank8\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"train_loss\": 0.1018, \"eval_loss\": 0.0776, \"train_runtime\": \"28m45s\", \"ner_full\": {\"n\": 529, \"greedy_f1\": 0.6397, \"oracle_f1\": 0.7998, \"oracle_headroom\": 0.1601, \"degeneracy_rate\": 0.072, \"SJ_rho\": 0.3649, \"FK_rho\": 0.2838, \"VC_rho\": 0.394, \"EM_rho\": 0.2562, \"LP_rho\": 0.2105, \"SJ_auroc\": 0.689, \"FK_auroc\": 0.6002, \"VC_auroc\": 0.6886, \"EM_auroc\": 0.7265, \"LP_auroc\": 0.6054, \"sel_SJ\": 0.6306, \"sel_FK\": 0.6265, \"sel_VC\": 0.5919, \"sel_EM\": 0.6073, \"sel_LP\": 0.635}, \"ner_cond\": {\"n\": 477, \"SJ_rho\": 0.3056, \"FK_rho\": 0.1452, \"VC_rho\": 0.3191, \"EM_rho\": 0.3558, \"LP_rho\": 0.169}, \"re_full\": {\"n\": 397, \"greedy_f1\": 0.3712, \"oracle_f1\": 0.609, \"oracle_headroom\": 0.2378, \"degeneracy_rate\": 0.217, \"SJ_rho\": 0.2244, \"FK_rho\": 0.3448, \"VC_rho\": 0.3617, \"EM_rho\": 0.068, \"LP_rho\": 0.2737, \"SJ_auroc\": 0.7092, \"FK_auroc\": 0.6469, \"VC_auroc\": 0.7533, \"EM_auroc\": 0.7306, \"LP_auroc\": 0.6325, \"sel_SJ\": 0.3584, \"sel_FK\": 0.3498, \"sel_VC\": 0.3715, \"sel_EM\": 0.3291, \"sel_LP\": 0.3606}, \"re_cond\": {\"n\": 242, \"SJ_rho\": 0.3601, \"FK_rho\": 0.2343, \"VC_rho\": 0.3703, \"EM_rho\": 0.4613, \"LP_rho\": 0.1809}}}, \"exp_022_seed789\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"exp_025_n32\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"n_samples\": 32, \"degeneracy_pct\": 4, \"lp_range\": 0.0781, \"oracle_f1\": 0.8412, \"greedy_f1\": 0.6615, \"oracle_gap\": 0.1797, \"selection_f1_lp_delta\": 0.54, \"selection_f1_sj_delta\": 0.16, \"selection_f1_fk_delta\": 0.6, \"selection_f1_em_delta\": 0.68, \"selection_f1_vc_delta\": -5.21, \"best_signal\": \"EM\", \"best_delta\": 0.68, \"metric_space\": \"micro_f1_filtered_529inst\", \"note\": \"corrected via n_ablation_fixed.py, greedy from inst['greedy'] field\"}}, \"exp_021_fewnerd_full\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"total_steps\": 6177, \"train_loss\": 0.048, \"eval_loss\": 0.0275, \"train_runtime\": \"3h57m\", \"epochs\": 3, \"final_checkpoint\": \"output/exp_021_fewnerd_full/checkpoint-6177\", \"adapter_path\": \"output/exp_021_fewnerd_full/adapter_model.safetensors\", \"inference_instances\": 37648, \"inference_filtered\": 32565, \"inference_n_samples\": 8, \"greedy_macro_f1\": 0.7478, \"oracle_macro_f1\": 0.8719, \"headroom\": 0.124, \"zero_f1_rate\": 0.119, \"degeneracy_rate\": 0.101, \"lp_within_range_mean\": 0.0879, \"lp_within_range_median\": 0.0662, \"lp_global_rho\": 0.4215, \"lp_cond_rho\": 0.4225, \"sj_global_rho\": 0.3002, \"sj_cond_rho\": 0.2937, \"fk_global_rho\": 0.3132, \"fk_cond_rho\": 0.3093, \"em_global_rho\": 0.2871, \"em_cond_rho\": 0.271, \"vc_global_rho\": 0.3858, \"vc_cond_rho\": 0.3234, \"lp_selection_delta_pp\": 1.36, \"vc_selection_delta_pp\": -1.79, \"sj_selection_delta_pp\": -2.14, \"fk_selection_delta_pp\": -2.26, \"em_selection_delta_pp\": -3.85, \"lp_bootstrap_ci_95_pp\": [1.18, 1.53], \"lp_sample_auroc\": 0.5782, \"vc_sample_auroc\": 0.5354, \"fk_sample_auroc\": 0.521, \"sj_sample_auroc\": 0.5197, \"em_sample_auroc\": 0.5137, \"scenario\": \"A_partial\", \"note\": \"Full analysis (gold-filtered n=32565). Prior simplified analysis used unfiltered data with different metrics.\"}}, \"exp_015_metrics_expansion\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"data_source\": \"exp_012_logprob/samples_with_logprobs.jsonl\", \"config\": \"N=8, T=1.0, seed=42, model=qwen3-8b-scierc-merged-v2\", \"ner\": {\"n_valid\": 529, \"n_cond\": 501, \"voting_rho_full\": 0.5018, \"voting_rho_cond\": 0.4497, \"voting_auroc\": 0.7279, \"voting_tau\": 0.3766, \"sj_rho_full\": 0.3565, \"sj_rho_cond\": 0.412, \"sj_auroc\": 0.6656, \"sj_tau\": 0.2658, \"em_rho_full\": 0.2566, \"em_rho_cond\": 0.3427, \"em_auroc\": 0.623, \"em_tau\": 0.1924, \"fk_rho_full\": 0.2651, \"fk_rho_cond\": 0.306, \"fk_auroc\": 0.6243, \"fk_tau\": 0.2027, \"logprob_rho_full\": 0.1396, \"logprob_rho_cond\": 0.1627, \"logprob_auroc\": 0.5585, \"logprob_tau\": 0.1006}, \"re\": {\"n_valid\": 397, \"n_cond\": 296, \"voting_rho_full\": 0.4217, \"voting_rho_cond\": 0.463, \"voting_auroc\": 0.7162, \"voting_tau\": 0.327, \"sj_rho_full\": 0.2112, \"sj_rho_cond\": 0.3683, \"sj_auroc\": 0.5816, \"sj_tau\": 0.1619, \"em_rho_full\": 0.1002, \"em_rho_cond\": 0.3607, \"em_auroc\": 0.5036, \"em_tau\": 0.0839, \"fk_rho_full\": 0.2528, \"fk_rho_cond\": 0.3168, \"fk_auroc\": 0.6308, \"fk_tau\": 0.1967, \"logprob_rho_full\": 0.2467, \"logprob_rho_cond\": 0.1457, \"logprob_auroc\": 0.6354, \"logprob_tau\": 0.1808}, \"diagnosis\": \"Unified 5-signal evaluation on single data source. Voting leads NER full (ρ=0.502), SJ retains strength in NER cond (ρ=0.412). All structural signals beat logprob on NER. RE: voting leads both full and cond.\"}}, \"exp_020_fewnerd_smoke\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"final_loss\": 0.031, \"total_steps\": 8236, \"training_time\": \"5h54m\", \"pilot_greedy_f1\": 0.8037, \"pilot_instances\": 200, \"merged_model_path\": \"checkpoints/qwen3-8b-fewnerd-merged\"}}, \"exp_vc_lp_cascade_selection\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"exp_tacred_re_benchmark\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"exp_vc_quartile_analysis\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"scierc_ner\": {\"Q1_lp_delta\": 0.016, \"Q2_lp_delta\": -0.006, \"Q3_lp_delta\": 0.02, \"Q4_lp_delta\": -0.004, \"Q4_mean_vc\": 0.921, \"Q1_headroom\": 0.169, \"Q4_headroom\": 0.048, \"overall_lp_delta\": 0.006, \"n\": 529}, \"scierc_re\": {\"Q1_lp_delta\": -0.036, \"Q2_lp_delta\": -0.021, \"Q3_lp_delta\": -0.022, \"Q4_lp_delta\": 0.04, \"Q4_mean_vc\": 0.894, \"Q1_headroom\": 0.211, \"Q4_headroom\": 0.145, \"overall_lp_delta\": -0.009, \"n\": 397}, \"conll_ner\": {\"Q1_lp_delta\": -0.037, \"Q2_lp_delta\": -0.005, \"Q3_lp_delta\": 0, \"Q4_lp_delta\": 0, \"overall_lp_delta\": -0.01, \"n\": 2756, \"note\": \"Q3/Q4 degenerate (VC=1.0, all samples identical)\"}, \"conclusion\": \"VC stratification does not solve LP compression for NER. RE Q4 is only exception (+0.040).\"}}, \"exp_llama3b_scierc_ablation\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"ner_full\": {\"SJ_rho\": 0.3754, \"FK_rho\": 0.2676, \"LP_rho\": 0.2662, \"EM_rho\": 0.3341, \"VC_rho\": 0.4602, \"SJ_auroc\": 0.7383, \"FK_auroc\": 0.6714, \"LP_auroc\": 0.633, \"EM_auroc\": 0.7763, \"VC_auroc\": 0.7429, \"n\": 529}, \"ner_cond\": {\"SJ_rho\": 0.3445, \"FK_rho\": 0.2125, \"LP_rho\": 0.2099, \"EM_rho\": 0.3952, \"VC_rho\": 0.3815, \"SJ_auroc\": 0.7292, \"FK_auroc\": 0.66, \"LP_auroc\": 0.6156, \"EM_auroc\": 0.7822, \"VC_auroc\": 0.7222, \"n\": 476}, \"greedy_f1\": 0.6267, \"oracle_f1\": 0.763, \"oracle_headroom\": 0.1363, \"selection_f1_SJ\": 0.6328, \"selection_f1_VC\": 0.6113, \"selection_f1_FK\": 0.6295, \"selection_f1_EM\": 0.6174, \"selection_f1_LP\": 0.6279, \"n_gold_empty\": 22, \"structural_beats_surface\": true, \"rho_advantage_SJ_over_FK\": 0.1078}}, \"exp_freeform_conll_4seed\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"greedy_f1\": \"0.9035±0.0004\", \"oracle_f1\": \"0.9460±0.0023\", \"lp_range_median\": \"0.0581±0.0072\", \"rho_sj\": \"0.4606±0.0188\", \"rho_fk\": \"0.4372±0.0209\", \"rho_em\": \"0.4714±0.0168\", \"rho_vc\": \"0.4606±0.0138\", \"rho_lp\": \"0.3262±0.0120\", \"sel_f1_sj\": \"0.8994±0.0014\", \"sel_f1_vc\": \"0.9006±0.0026\", \"sel_f1_lp\": \"0.8958±0.0009\", \"seeds\": [42, 123, 456, 789], \"n_samples\": 8, \"temperature\": 1, \"instances\": 2756, \"gold_empty_filtered\": 697}}, \"exp_qwen3_4b_conll_merge_inference_v2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"exp_qwen3_4b_scierc_merge_inference\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"exp_qwen3_4b_scierc_finetune_v3\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"exp_qwen3_4b_conll_finetune_resume\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"train_loss\": 0.001136, \"eval_loss\": 0.0225, \"best_global_step\": 4200, \"best_metric_eval_loss\": 0.0225, \"total_steps\": 4390, \"epochs\": 5, \"train_runtime_sec\": 1185.8, \"train_samples_per_second\": 59.2, \"resumed_from_step\": 3800}}, \"exp_qwen3_4b_scierc_finetune_v2\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"exp_qwen3_4b_conll_finetune\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"final_loss\": 0.0086, \"total_steps_completed\": 3920, \"total_steps_target\": 4390, \"epochs_completed\": 4.46, \"epochs_target\": 5, \"best_checkpoint\": \"checkpoint-3800\", \"note\": \"Training stopped at 89.3% completion (no error log found). Using checkpoint-3800 (loss ~0.01) for merge.\"}}, \"exp_freeform_seed789_v2\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"exp_qwen3_4b_scierc_finetune\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"exp_lp_t07_scierc\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"exp_lp_scierc_t07\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"ner_greedy_f1\": 0.662, \"ner_oracle_f1\": 0.764, \"ner_headroom_pp\": 10.2, \"ner_rho_sj_full\": 0.365, \"ner_rho_sj_cond\": 0.363, \"ner_rho_fk_full\": 0.289, \"ner_rho_fk_cond\": 0.255, \"lp_rho_full\": 0.249, \"lp_rho_cond\": 0.185, \"ner_rho_advantage\": 0.076, \"zero_f1_pct\": 11, \"full_n\": 529, \"cond_n\": 477, \"verdict\": \"success_supports_LP_compression_claim\"}}, \"exp_re_scierc_seed456\": {\"status\": \"DONE\", \"conclusion\": \"negative\", \"metrics\": {\"ner_greedy_f1\": 0.664, \"ner_oracle_f1\": 0.775, \"ner_headroom_pp\": 11.1, \"ner_rho_sj_cond\": 0.283, \"ner_rho_fk_cond\": 0.145, \"re_greedy_f1\": 0.417, \"re_oracle_f1\": 0.581, \"re_headroom_pp\": 16.3, \"re_rho_sj_cond\": 0.315, \"re_rho_fk_cond\": 0.123, \"re_zero_f1_pct\": 45.3, \"verdict\": \"FAIL_re_rho_sj_below_040\"}}, \"exp_re_scierc_seed123\": {\"status\": \"DONE\", \"conclusion\": \"negative\", \"metrics\": {\"ner_greedy_f1\": 0.663, \"ner_oracle_f1\": 0.786, \"ner_headroom_pp\": 12.3, \"ner_rho_sj_cond\": 0.404, \"ner_rho_fk_cond\": 0.182, \"re_greedy_f1\": 0.42, \"re_oracle_f1\": 0.593, \"re_headroom_pp\": 17.3, \"re_rho_sj_cond\": 0.277, \"re_rho_fk_cond\": 0.063, \"re_zero_f1_pct\": 43.6, \"verdict\": \"FAIL_re_rho_sj_below_040\"}}, \"exp_017_llama_conll_n8_t07\": {\"status\": \"DONE\", \"metrics\": {\"n_valid\": 2756, \"greedy_f1\": 0.9242, \"oracle_f1\": 0.9391, \"lp_range_median\": 1.1e-05, \"lp_tied_fraction_005\": 0.9579, \"signals\": {\"SJ\": {\"rho\": 0.3934, \"auroc\": 0.6506}, \"FK\": {\"rho\": 0.3879, \"auroc\": 0.6488}, \"VC\": {\"rho\": 0.375, \"auroc\": 0.6551}, \"EM\": {\"rho\": 0.3888, \"auroc\": 0.6494}, \"LP\": {\"rho\": 0.2951, \"auroc\": 0.7509}}, \"selection_f1\": {\"SJ\": 0.9247, \"FK\": 0.9254, \"VC\": 0.9264, \"EM\": 0.9255, \"LP\": 0.9248}}, \"conclusion\": \"success\"}, \"exp008_re_n16\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"exp001_seed456\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"exp001_seed123\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"exp_001_n16_seed456_full\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"exp_001_n16_seed123_full\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"exp_007_ner_llama\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"exp_002_merge_conll2003\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"exp_019_supervised_verifier\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"exp_018_llama_scierc_seed456\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"exp_002_conll_n16_r1024\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"exp_007_llama_n16_r1024\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"exp_001_seed123_v2_r1024\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"exp_001_seed456_v2_ner_r1024\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"exp_001_seed42_v2_r1024\": {\"status\": \"DONE\", \"conclusion\": \"killed\", \"metrics\": {\"greedy_f1\": 0.6647, \"oracle_f1\": 0.8106, \"softjaccard_rho_full\": 0.3928, \"fleiss_rho_full\": 0.2489, \"logprob_rho_full\": 0.2136, \"softjaccard_rho_cond\": 0.3455, \"fleiss_rho_cond\": 0.163, \"logprob_rho_cond\": 0.1624, \"verdict\": \"MARGINAL\"}}, \"exp_017_llama_conll_n16_s456\": {\"status\": \"DONE\", \"metrics\": {\"greedy_f1\": 0.9243, \"oracle_f1\": 0.9488, \"oracle_headroom\": 0.0245, \"n_instances\": 3453, \"n_valid\": 2756, \"n_conditional\": 2642, \"structural_beats_surface\": true, \"full\": {\"SJ_rho\": 0.4552, \"SJ_AUROC\": 0.7288, \"SJ_ECE\": 0.1134, \"FK_rho\": 0.4478, \"FK_AUROC\": 0.7248, \"FK_ECE\": 0.109, \"logprob_rho\": 0.3078, \"logprob_AUROC\": 0.7612, \"logprob_ECE\": 0.1289, \"EM_rho\": 0.452, \"EM_AUROC\": 0.7275, \"EM_ECE\": 0.1082, \"voting_conf_rho\": 0.4571, \"voting_conf_AUROC\": 0.7348, \"voting_conf_ECE\": 0.0863}, \"conditional\": {\"SJ_rho\": 0.4505, \"SJ_AUROC\": 0.7449, \"SJ_ECE\": 0.0826, \"FK_rho\": 0.4422, \"FK_AUROC\": 0.7401, \"FK_ECE\": 0.0835, \"logprob_rho\": 0.3242, \"logprob_AUROC\": 0.8067, \"logprob_ECE\": 0.0921, \"EM_rho\": 0.451, \"EM_AUROC\": 0.745, \"EM_ECE\": 0.0756, \"voting_conf_rho\": 0.3962, \"voting_conf_AUROC\": 0.7202, \"voting_conf_ECE\": 0.0746}, \"best_of_n\": {\"greedy\": 0.9243, \"random_avg\": 0.9215, \"sj_best\": 0.9243, \"logprob_best\": 0.9243, \"voting_conf_best\": 0.9243, \"oracle\": 0.9488}, \"n8_vs_n16_delta\": {\"full_SJ_rho_delta\": 0.0238, \"full_FK_rho_delta\": 0.0201, \"full_logprob_rho_delta\": 0.0006, \"full_EM_rho_delta\": 0.0214, \"full_voting_conf_rho_delta\": 0.0315, \"cond_SJ_rho_delta\": 0.0149, \"cond_FK_rho_delta\": 0.0112, \"cond_logprob_rho_delta\": -0.004, \"cond_EM_rho_delta\": 0.0107, \"cond_voting_conf_rho_delta\": 0.0219}}, \"conclusion\": \"success\"}, \"exp_017_llama_conll_n16_s123\": {\"status\": \"DONE\", \"metrics\": {\"greedy_f1\": 0.9266, \"oracle_f1\": 0.9497, \"oracle_headroom\": 0.0231, \"n_instances\": 3453, \"n_valid\": 2756, \"n_conditional\": 2642, \"structural_beats_surface\": true, \"full\": {\"SJ_rho\": 0.4698, \"SJ_AUROC\": 0.7402, \"SJ_ECE\": 0.1135, \"FK_rho\": 0.4594, \"FK_AUROC\": 0.7351, \"FK_ECE\": 0.1114, \"logprob_rho\": 0.3161, \"logprob_AUROC\": 0.768, \"logprob_ECE\": 0.129, \"EM_rho\": 0.4676, \"EM_AUROC\": 0.7399, \"EM_ECE\": 0.1082, \"voting_conf_rho\": 0.4612, \"voting_conf_AUROC\": 0.7429, \"voting_conf_ECE\": 0.0832}, \"conditional\": {\"SJ_rho\": 0.4712, \"SJ_AUROC\": 0.7609, \"SJ_ECE\": 0.0828, \"FK_rho\": 0.4595, \"FK_AUROC\": 0.7547, \"FK_ECE\": 0.0858, \"logprob_rho\": 0.3314, \"logprob_AUROC\": 0.8134, \"logprob_ECE\": 0.0922, \"EM_rho\": 0.4732, \"EM_AUROC\": 0.7626, \"EM_ECE\": 0.075, \"voting_conf_rho\": 0.4086, \"voting_conf_AUROC\": 0.7338, \"voting_conf_ECE\": 0.0706}, \"best_of_n\": {\"greedy\": 0.9242, \"random_avg\": 0.9216, \"sj_best\": 0.9247, \"logprob_best\": 0.9253, \"voting_conf_best\": 0.9255, \"oracle\": 0.9486}, \"n8_vs_n16_delta\": {\"full_SJ_rho_delta\": 0.0384, \"full_FK_rho_delta\": 0.0317, \"full_logprob_rho_delta\": 0.0089, \"full_SJ_AUROC_delta\": 0.0363, \"full_FK_AUROC_delta\": 0.0325, \"full_logprob_AUROC_delta\": 0.007, \"cond_SJ_rho_delta\": 0.0356, \"cond_FK_rho_delta\": 0.0285, \"cond_logprob_rho_delta\": 0.0032}}, \"conclusion\": \"success\"}, \"exp_008_re_n16_full\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"exp_001_n16_seed123\": {\"status\": \"DONE\", \"metrics\": {\"ner\": {\"greedy_f1\": 0.655, \"oracle_f1\": 0.8028, \"headroom\": 0.1478, \"rho_sj_full\": 0.4076, \"rho_fk_full\": 0.2799, \"rho_logprob_full\": 0.3189, \"rho_sj_cond\": 0.4271, \"rho_fk_cond\": 0.2743, \"rho_logprob_cond\": 0.2835, \"sj_beats_fk\": true, \"rho_advantage\": 0.1277}, \"re\": {\"greedy_f1\": 0.4243, \"oracle_f1\": 0.6771, \"headroom\": 0.2528, \"rho_sj_full\": 0.2943, \"rho_fk_full\": 0.2657, \"rho_logprob_full\": 0.3005, \"rho_sj_cond\": 0.4003, \"rho_fk_cond\": 0.313, \"rho_logprob_cond\": 0.2317, \"sj_beats_fk\": true, \"rho_advantage\": 0.0286}, \"verdict\": \"FAIL\"}, \"conclusion\": \"success\"}, \"exp_016_signal_ensemble\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"sj_logprob_pearson_ner\": 0.57, \"sj_logprob_pearson_re\": 0.42, \"best_linear_ner\": {\"combo\": \"SJ+voting_conf\", \"alpha\": 0.3, \"rho\": 0.489}, \"best_linear_re\": {\"combo\": \"voting_conf+logprob\", \"alpha\": 0.6, \"rho\": 0.429}, \"ensemble_ner_auroc\": 0.735, \"ensemble_re_auroc\": 0.719, \"best_single_ner_auroc\": 0.7, \"best_single_re_auroc\": 0.721, \"ensemble_ner_delta\": 0.035, \"selection_f1_ner\": {\"greedy\": 0.609, \"logprob\": 0.609, \"sj\": 0.604, \"ensemble\": 0.604, \"voting\": 0.596, \"random\": 0.58, \"oracle\": 0.769}, \"selection_f1_re\": {\"logprob\": 0.397, \"greedy\": 0.374, \"sj\": 0.368, \"ensemble\": 0.367, \"voting\": 0.338, \"random\": 0.338, \"oracle\": 0.561}, \"diagnosis\": \"SJ+voting_conf linear combo boosts NER ρ to 0.489 (+23%). RE: logprob-best is ONLY method beating greedy (0.397 vs 0.374). Ensemble AUROC +0.035 on NER. Oracle gap still huge.\"}}, \"exp_001_ner_n16_scierc\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"n_instances\": 551, \"ner_n\": 529, \"re_n\": 397, \"N\": 16, \"T\": 1, \"seed\": 42, \"full_test_set\": true, \"ner_voting_conf_rho\": 0.399, \"ner_sj_rho\": 0.398, \"ner_em_rho\": 0.339, \"ner_fk_rho\": 0.288, \"ner_logprob_rho\": 0.237, \"ner_voting_conf_auroc\": 0.704, \"ner_sj_auroc\": 0.697, \"ner_cond_em_rho\": 0.414, \"ner_cond_sj_rho\": 0.349, \"ner_cond_vc_rho\": 0.34, \"re_voting_conf_rho\": 0.38, \"re_logprob_rho\": 0.293, \"re_fk_rho\": 0.281, \"re_sj_rho\": 0.277, \"re_em_rho\": 0.148, \"re_voting_conf_auroc\": 0.699, \"re_cond_em_rho\": 0.475, \"re_cond_sj_rho\": 0.318, \"re_cond_vc_rho\": 0.35, \"re_cond_em_auroc\": 0.742, \"diagnosis\": \"551 instances T=1.0: voting_conf best on full set (NER 0.399, RE 0.380). EM SURPRISE best on conditional set (NER cond 0.414, RE cond 0.475). RE full FAIL (SJ 0.277 < 0.40). Previous N-scaling 'breakthrough' was artifact of 200 instances + T=0.7.\"}}, \"exp_002\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"sj_rho_full\": 0.4357, \"sj_tau_full\": 0.3851, \"sj_auroc_full\": 0.8008, \"sj_rho_cond\": 0.4511, \"fk_rho_full\": 0.3998, \"fk_tau_full\": 0.3568, \"fk_auroc_full\": 0.7741, \"fk_rho_cond\": 0.4064, \"logprob_rho_full\": 0.3157, \"logprob_tau_full\": 0.2469, \"logprob_auroc_full\": 0.7532, \"logprob_rho_cond\": 0.3562, \"em_rho_full\": 0.4507, \"em_tau_full\": 0.4002, \"em_auroc_full\": 0.8156, \"em_rho_cond\": 0.4799, \"ev_rho_full\": 0.4237, \"ev_tau_full\": 0.3777, \"ev_auroc_full\": 0.7889, \"ev_rho_cond\": 0.4127, \"greedy_f1\": 0.9123, \"oracle_f1\": 0.9543, \"voting_f1\": 0.9141, \"oracle_headroom\": 0.042, \"sj_vs_logprob_delta_rho\": 0.12, \"sj_vs_logprob_ci_low\": 0.0881, \"sj_vs_logprob_ci_high\": 0.154, \"sj_vs_logprob_significant\": true, \"n_instances\": 3453, \"n_valid\": 2756, \"n_samples\": 8, \"temperature\": 1}}, \"exp_002_ner_conll2003\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"exp_004_re_diagnostic\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"per_relation_type\": {\"HYPONYM-OF\": {\"n\": 36, \"rho_sj\": 0.545, \"rho_fk\": 0.646, \"rho_vc\": 0.628, \"mean_f1\": 0.513}, \"CONJUNCTION\": {\"n\": 86, \"rho_sj\": 0.383, \"rho_fk\": 0.35, \"rho_vc\": 0.484, \"mean_f1\": 0.48}, \"USED-FOR\": {\"n\": 299, \"rho_sj\": 0.236, \"rho_fk\": 0.255, \"rho_vc\": 0.286, \"mean_f1\": 0.422}, \"PART-OF\": {\"n\": 44, \"rho_sj\": 0.239, \"rho_fk\": 0.348, \"rho_vc\": 0.283, \"mean_f1\": 0.297}, \"EVALUATE-FOR\": {\"n\": 62, \"rho_sj\": 0.172, \"rho_fk\": 0.255, \"rho_vc\": 0.226, \"mean_f1\": 0.365}, \"COMPARE\": {\"n\": 35, \"rho_sj\": 0.168, \"rho_fk\": 0.184, \"rho_vc\": 0.18, \"mean_f1\": 0.453}, \"FEATURE-OF\": {\"n\": 50, \"rho_sj\": 0.004, \"rho_fk\": 0.052, \"rho_vc\": 0.014, \"mean_f1\": 0.254}}, \"error_propagation\": {\"total_fn\": 553, \"tail_error_pct\": 21.9, \"full_error_pct\": 21.7, \"head_error_pct\": 17.7, \"head_tail_error_pct\": 15.9, \"type_error_pct\": 8.3, \"worst_consistency\": \"head_type_error (sj=0.411)\", \"best_consistency\": \"head_error (sj=0.613)\"}, \"threshold_sensitivity\": {\"thr_0.00_rho_sj\": 0.3161, \"thr_0.00_rho_vc\": 0.3841, \"thr_0.00_n\": 313, \"thr_0.05_rho_sj\": 0.2682, \"thr_0.05_rho_vc\": 0.2364, \"thr_0.05_n\": 239}, \"bootstrap_ci_95\": {\"ner_sj\": [0.2946, 0.4586], \"ner_voting_conf\": [0.3048, 0.4656], \"re_sj\": [0.1422, 0.3391], \"re_voting_conf\": [0.1818, 0.3721], \"re_cond_sj\": [0.2161, 0.4102], \"re_cond_voting_conf\": [0.2825, 0.474]}, \"fisher_z_ner_vs_re\": {\"sj_z\": 2.31, \"sj_p\": 0.0209, \"sj_significant\": true, \"fk_z\": -0.31, \"fk_p\": 0.756, \"fk_significant\": false, \"voting_z\": 1.914, \"voting_p\": 0.0556, \"voting_significant\": false}, \"diagnosis\": \"FEATURE-OF is near-zero rho across all signals (n=50, F1=0.254). HYPONYM-OF strongest (rho_fk=0.646). Entity span errors (head+tail) account for 55.5% of RE FN. NER rho_sj significantly > RE rho_sj (p=0.021). Voting_conf is best RE signal in conditional set (rho=0.384).\"}}, \"exp_005\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"exp_014_entity_majority_voting\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"ner_full_rho\": 0.3915, \"ner_full_p\": 8.1e-21, \"ner_full_tau\": 0.2906, \"ner_full_auroc\": 0.7039, \"re_full_rho\": 0.3403, \"re_full_p\": 3.21e-12, \"re_full_tau\": 0.256, \"re_full_auroc\": 0.6668, \"ner_voting_f1\": 0.6246, \"ner_greedy_f1\": 0.6483, \"ner_oracle_f1\": 0.7793, \"re_voting_f1\": 0.3577, \"re_greedy_f1\": 0.4022, \"re_oracle_f1\": 0.5886, \"diagnosis\": \"Voting confidence BEATS SJ on both NER (rho 0.392 vs 0.383) and RE (0.340 vs 0.244). But voting as selection strategy LOSES to greedy.\"}}, \"exp_013_exact_match_voting\": {\"status\": \"DONE\", \"conclusion\": \"negative\", \"metrics\": {\"ner_full_rho\": 0.2941, \"ner_full_p\": 5.12e-12, \"ner_full_tau\": 0.2181, \"ner_full_auroc\": 0.6398, \"re_full_rho\": 0.1562, \"re_full_p\": 0.0018, \"re_full_tau\": 0.1185, \"re_full_auroc\": 0.5863, \"diagnosis\": \"EM between SJ and FK on NER, weakest on RE. Too coarse-grained.\"}}, \"exp_012_logprob_baseline\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"ner_full_rho_sj\": 0.3565, \"ner_full_rho_fk\": 0.2651, \"ner_full_rho_logprob\": 0.1396, \"ner_full_rho_greedy_logprob\": 0.1615, \"ner_full_tau_sj\": 0.2658, \"ner_full_tau_logprob\": 0.1006, \"ner_full_auroc_sj\": 0.6892, \"ner_full_auroc_fk\": 0.6292, \"ner_full_auroc_logprob\": 0.5907, \"ner_full_n\": 529, \"ner_sj_vs_logprob_delta\": 0.2169, \"re_full_rho_sj\": 0.2112, \"re_full_rho_fk\": 0.2528, \"re_full_rho_logprob\": 0.2467, \"re_full_auroc_sj\": 0.5916, \"re_full_auroc_fk\": 0.6262, \"re_full_auroc_logprob\": 0.6186, \"re_full_n\": 397, \"re_cond_rho_sj\": 0.3683, \"re_cond_rho_fk\": 0.3168, \"re_cond_rho_logprob\": 0.1457, \"re_cond_auroc_sj\": 0.6839, \"re_cond_auroc_logprob\": 0.5487, \"re_cond_n\": 296, \"diagnosis\": \"NER: SJ crushes logprob (rho +0.217). RE full: logprob slightly ahead. RE cond: SJ crushes logprob (rho +0.223). SJ unique value CONFIRMED.\"}}, \"mvp_pilot_005\": {\"status\": \"DONE\", \"metrics\": {\"ner_greedy_f1\": 0.6619, \"ner_oracle_f1\": 0.7585, \"ner_headroom\": 0.0966, \"ner_fleiss_kappa_mean\": 0.4722, \"ner_soft_jaccard_mean\": 0.7757, \"ner_full_rho_sj\": 0.3875, \"ner_full_rho_fk\": 0.3211, \"ner_full_n\": 529, \"ner_cond_rho_sj\": 0.3868, \"ner_cond_rho_fk\": 0.305, \"ner_cond_n\": 504, \"ner_sj_beats_fk_full\": true, \"ner_sj_beats_fk_cond\": true, \"ner_rho_advantage\": 0.0664, \"ner_sample_f1_mean\": 0.6243, \"ner_sample_f1_std\": 0.3131, \"ner_sample_f1_pct_zero\": 11.2, \"ner_gold_empty_filtered\": 22, \"ner_all_zero_filtered\": 25, \"re_greedy_f1\": 0.4219, \"re_oracle_f1\": 0.5532, \"re_headroom\": 0.1313, \"re_fleiss_kappa_mean\": 0.3829, \"re_soft_jaccard_mean\": 0.687, \"re_full_rho_sj\": 0.2343, \"re_full_rho_fk\": 0.1835, \"re_full_n\": 397, \"re_cond_rho_sj\": 0.3716, \"re_cond_rho_fk\": 0.2533, \"re_cond_n\": 301, \"re_sj_beats_fk_full\": true, \"re_sj_beats_fk_cond\": true, \"re_rho_advantage\": 0.0508, \"re_sample_f1_mean\": 0.3782, \"re_sample_f1_std\": 0.3845, \"re_sample_f1_pct_zero\": 42.4, \"re_gold_empty_filtered\": 154, \"re_all_zero_filtered\": 96, \"parse_failures\": 0, \"verdict\": \"FAIL\", \"verdict_note\": \"RE full rho_sj=0.234 < 0.40; RE cond rho_sj=0.372 passes conditional but not full threshold\"}, \"conclusion\": \"negative\"}, \"e1_component_wise_re_sj\": {\"status\": \"DONE\", \"conclusion\": \"negative\", \"metrics\": {\"full_head_sj_rho\": 0.21, \"full_tail_sj_rho\": 0.201, \"full_type_match_rho\": 0.201, \"full_multiplicative_rho\": 0.244, \"full_additive_rho\": 0.243, \"full_fleiss_kappa_rho\": 0.278, \"cond_head_sj_rho\": 0.27, \"cond_tail_sj_rho\": 0.259, \"cond_type_match_rho\": 0.252, \"cond_multiplicative_rho\": 0.316, \"cond_additive_rho\": 0.306, \"cond_fleiss_kappa_rho\": 0.307, \"n_full\": 397, \"n_conditional\": 313, \"diagnosis\": \"head_sj rho=0.210 FAR from NER rho=0.383. Multiplicative penalty hypothesis REJECTED. Problem is fundamental: span-level SJ lacks discriminative power for RE.\"}}, \"mvp_pilot_004\": {\"status\": \"DONE\", \"metrics\": {\"ner_greedy_f1\": 0.6671, \"ner_oracle_f1\": 0.7756, \"ner_headroom\": 0.1085, \"ner_fleiss_kappa_mean\": 0.4048, \"ner_soft_jaccard_mean\": 0.7008, \"ner_full_rho_fk\": 0.259, \"ner_full_rho_sj\": 0.3825, \"ner_full_n\": 529, \"ner_cond_rho_fk\": 0.2352, \"ner_cond_rho_sj\": 0.3762, \"ner_cond_n\": 508, \"ner_sj_beats_fk_full\": true, \"ner_sj_beats_fk_cond\": true, \"ner_sample_f1_mean\": 0.6084, \"ner_sample_f1_std\": 0.3174, \"ner_sample_f1_pct_zero\": 12.19, \"ner_gold_empty_filtered\": 22, \"ner_all_zero_filtered\": 21, \"re_greedy_f1\": 0.4208, \"re_oracle_f1\": 0.5882, \"re_headroom\": 0.1674, \"re_fleiss_kappa_mean\": 0.2996, \"re_soft_jaccard_mean\": 0.6114, \"re_full_rho_fk\": 0.2782, \"re_full_rho_sj\": 0.2441, \"re_full_n\": 397, \"re_cond_rho_fk\": 0.3067, \"re_cond_rho_sj\": 0.3161, \"re_cond_n\": 313, \"re_sj_beats_fk_full\": false, \"re_sj_beats_fk_cond\": true, \"re_sample_f1_mean\": 0.3612, \"re_sample_f1_std\": 0.383, \"re_sample_f1_pct_zero\": 44.3, \"re_gold_empty_filtered\": 154, \"re_all_zero_filtered\": 84, \"parse_failures\": 0, \"verdict\": \"FAIL\"}, \"conclusion\": \"negative\"}, \"ft_002_v2\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"epoch\": 5, \"train_loss\": 0.0806, \"eval_loss\": 0.089, \"train_runtime\": \"28m41s\", \"train_samples_per_second\": 5.407, \"train_steps_per_second\": 0.34, \"total_steps\": 585, \"checkpoints\": [\"checkpoint-400\", \"checkpoint-500\", \"checkpoint-585\"], \"gate0_final_ner_f1\": 0.6615, \"gate0_final_re_f1\": 0.4177, \"gate0_final_parse_failures\": 0, \"gate0_final_ner_pass\": true, \"gate0_final_re_pass\": true, \"gate0_final_pass\": true, \"gate0_ckpt400_ner_f1\": 0.6475, \"gate0_ckpt400_re_f1\": 0.3793, \"gate0_ckpt400_parse_failures\": 0, \"gate0_ckpt400_verdict\": \"FAIL\", \"gate0_ckpt400_re_sample_f1_pct_zero\": 58.8, \"gate0_ckpt400_warning\": \">30% samples F1=0\"}}, \"mvp_pilot_002\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"ft_002\": {\"status\": \"DONE\", \"conclusion\": \"killed\", \"metrics\": {\"last_step\": 70, \"total_steps\": 585, \"progress_pct\": 11.97, \"last_loss\": 0.1134, \"last_lr\": 0.00019982, \"elapsed\": \"3m32s\", \"failure_reason\": \"OOM at step 73, batch_size=4 too large for 32GB RTX 5090\"}}, \"ft_001\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"train_loss\": 0.1099, \"eval_loss\": 0.0771, \"gate0_ner_f1_strict\": 0.1143, \"gate0_re_f1_strict\": 0.0125, \"gate0_ner_f1_text\": 0.606, \"gate0_re_f1_text\": 0.3392, \"gate0_offset_accuracy\": 0.1665, \"gate0_parse_failures\": 43, \"gate0_pass\": false, \"gate0_realigned_ner_f1\": 0.6045, \"gate0_realigned_re_f1\": 0.338, \"gate0_realigned_entity_offset_accuracy\": 1, \"gate0_realigned_relation_offset_accuracy\": 1, \"gate0_realigned_ner_pass\": true, \"gate0_realigned_re_pass\": false, \"gate0_realigned_pass\": false, \"gate0_ner_f1_delta_realign\": 0.4901, \"gate0_re_f1_delta_realign\": 0.3255, \"verdict_note\": \"partial: NER PASS (60.4%) / RE FAIL (33.8% < 40%)\"}}, \"mvp_pilot_003\": {\"status\": \"DONE\", \"conclusion\": \"negative\", \"metrics\": {\"ner_greedy_f1\": 0.6362, \"ner_oracle_f1\": 0.792, \"ner_headroom\": 0.1559, \"ner_fleiss_kappa_mean\": 0.2488, \"ner_soft_jaccard_mean\": 0.5066, \"ner_full_rho_sj\": 0.3808, \"ner_full_rho_fk\": 0.3362, \"ner_full_p_sj\": 1.07e-19, \"ner_full_p_fk\": 1.93e-15, \"ner_full_n\": 529, \"ner_cond_rho_sj\": 0.3836, \"ner_cond_rho_fk\": 0.3187, \"ner_cond_p_sj\": 1.83e-19, \"ner_cond_p_fk\": 1.33e-13, \"ner_cond_n\": 514, \"ner_sj_beats_fk_full\": true, \"ner_sj_beats_fk_cond\": true, \"ner_rho_advantage\": 0.0446, \"ner_sample_f1_mean\": 0.5153, \"ner_sample_f1_std\": 0.3334, \"ner_sample_f1_pct_zero\": 19.9, \"ner_gold_empty_filtered\": 22, \"ner_all_zero_filtered\": 15, \"re_greedy_f1\": 0.3774, \"re_oracle_f1\": 0.5939, \"re_headroom\": 0.2165, \"re_fleiss_kappa_mean\": 0.0879, \"re_soft_jaccard_mean\": 0.3958, \"re_full_rho_sj\": 0.2367, \"re_full_rho_fk\": 0.2221, \"re_full_p_sj\": 1.85e-06, \"re_full_p_fk\": 7.92e-06, \"re_full_n\": 397, \"re_cond_rho_sj\": 0.3004, \"re_cond_rho_fk\": 0.2374, \"re_cond_p_sj\": 2.25e-08, \"re_cond_p_fk\": 1.19e-05, \"re_cond_n\": 333, \"re_sj_beats_fk_full\": true, \"re_sj_beats_fk_cond\": true, \"re_rho_advantage\": 0.0146, \"re_sample_f1_mean\": 0.1977, \"re_sample_f1_std\": 0.3251, \"re_sample_f1_pct_zero\": 67.6, \"re_gold_empty_filtered\": 154, \"re_all_zero_filtered\": 64, \"parse_failures_stochastic\": 0, \"parse_failures_greedy\": 0, \"total_stochastic_samples\": 4408, \"total_greedy\": 551, \"verdict\": \"FAIL\", \"verdict_reason\": \"RE full rho_sj=0.2367 < 0.40 threshold; strong signal exists but below PASS bar\"}}, \"mvp_pilot_001\": {\"status\": \"DONE\", \"conclusion\": \"negative\", \"metrics\": {\"ner_greedy_f1\": 0.611, \"ner_oracle_f1\": 0.78, \"ner_headroom\": 0.169, \"ner_fleiss_kappa_mean\": 0.2449, \"ner_soft_jaccard_mean\": 0.5041, \"ner_full_rho_sj\": 0.3616, \"ner_full_rho_fk\": 0.3515, \"ner_full_n\": 529, \"ner_cond_rho_sj\": 0.3688, \"ner_cond_rho_fk\": 0.3569, \"ner_cond_n\": 510, \"ner_sj_beats_fk_full\": true, \"ner_sj_beats_fk_cond\": true, \"ner_sample_f1_pct_zero\": 20.4, \"ner_gold_empty_filtered\": 22, \"ner_all_zero_filtered\": 19, \"re_greedy_f1\": 0.355, \"re_oracle_f1\": 0.572, \"re_headroom\": 0.217, \"re_fleiss_kappa_mean\": 0.0681, \"re_soft_jaccard_mean\": 0.3635, \"re_full_rho_sj\": 0.2535, \"re_full_rho_fk\": 0.2885, \"re_full_n\": 397, \"re_cond_rho_sj\": 0.3515, \"re_cond_rho_fk\": 0.3107, \"re_cond_n\": 320, \"re_sj_beats_fk_full\": false, \"re_sj_beats_fk_cond\": true, \"re_sample_f1_pct_zero\": 58.3, \"re_gold_empty_filtered\": 154, \"re_all_zero_filtered\": 77, \"parse_failures_stochastic\": 164, \"parse_failures_greedy\": 29, \"total_stochastic_samples\": 4408, \"total_greedy\": 551, \"verdict\": \"FAIL\", \"verdict_reason\": \"RE full rho_sj=0.2535 < 0.40; SJ does not beat FK on RE full set\"}}}, \"count\": 171, \"total\": 171, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.5614}}"
    }
  },
  "sourceToolAssistantUUID": "498077fb-4abe-4603-9215-51d13cb29ee7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "a97de670-f9a7-4d30-affd-382982b8a334",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-19T13:54:36.630Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01AEqEmUYbekyYmbnfYSfTZF`</summary>

```json
{
  "project": "struct_self_consist_ie",
  "file": "paper_provenance.yaml",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4ed4ae10-5725-44ba-bbb5-6d7b090fa9d3",
  "isSidechain": false,
  "requestId": "req_011CbC3KLXmDCphZ7BiR3dtb",
  "type": "assistant",
  "uuid": "9e8ac923-9d33-4522-bfdd-ff21639b0c27",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "a97de670-f9a7-4d30-affd-382982b8a334",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01K9CMF8mt8fbLgVHFPzVjey",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2252,
      "cache_read_input_tokens": 24315,
      "output_tokens": 779,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2252,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 779,
          "cache_read_input_tokens": 24315,
          "cache_creation_input_tokens": 2252,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2252
          },
          "type": "message"
        }
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

_source line 18 · 2026-05-19T13:54:36.643Z_

<details><summary>↩ Tool result · `toolu_01AEqEmUYbekyYmbnfYSfTZF`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/paper_provenance.yaml\", \"content\": \"paper:\\n  title: 'Strong Predictors, Weak Selectors: A Systematic Comparison of Confidence\\n    Signals for Test-Time Scaling in Information Extraction'\\n  version: 169\\n  generated_at: '2026-05-18T15:39:48.035618+00:00'\\n  source: manual provenance build by Paper Agent\\nclaims:\\n- id: c001_voting_rho_scierc_ner\\n  text: Voting Confidence achieves ρ=0.379 on SciERC NER (corrected from 0.502 truncation\\n    artifact)\\n  sections:\\n  - abstract\\n  - introduction\\n  - experiments\\n  - conclusion\\n  - discussion\\n  - related_work\\n  tier: 1\\n  evidence:\\n  - exp_id: exp_012_rerun_1024\\n    metric: ner.voting_rho_full\\n    value: 0.379\\n  note: Old value 0.502 from exp_015 was inflated by max_tokens=512 truncation. Corrected\\n    via exp_012_rerun_1024 (max_tokens=1024).\\n- id: c002_auroc_dissociation_scierc\\n  text: ρ-AUROC dissociation on SciERC — EM leads AUROC (NER 0.749, RE 0.706) while\\n    Voting leads ρ (NER 0.379, RE 0.422)\\n  sections:\\n  - abstract\\n  - introduction\\n  - experiments\\n  - conclusion\\n  - discussion\\n  tier: 1\\n  evidence:\\n  - exp_id: exp_012_rerun_1024\\n    metric: ner.em_auroc\\n    value: 0.749\\n  - exp_id: exp_012_rerun_1024\\n    metric: re.em_auroc\\n    value: 0.706\\n  - exp_id: exp_012_rerun_1024\\n    metric: ner.voting_auroc\\n    value: 0.684\\n  note: Old Table 1 had Voting NER AUROC=.741 (from exp_015 truncated). Corrected\\n    to .684 via exp_012_rerun_1024. EM now leads AUROC on both NER and RE. Headline\\n    claim changed from \\\"entity voting achieves ρ=0.38 and AUROC=0.74\\\" to split ρ (Voting\\n    0.38) / AUROC (EM 0.75) claim.\\n- id: c003_sj_rho_scierc_ner\\n  text: SJ achieves ρ=0.360 on SciERC NER (corrected from 0.357)\\n  sections:\\n  - experiments\\n  tier: 1\\n  evidence:\\n  - exp_id: exp_012_rerun_1024\\n    metric: ner.sj_rho_full\\n    value: 0.36\\n  - exp_id: exp_004_re_diagnostic\\n    metric: bootstrap_ci_95.ner_sj\\n    value:\\n    - 0.2946\\n    - 0.4586\\n- id: c004_voting_leads_re\\n  text: Voting leads RE full set (ρ=0.350, corrected from 0.422)\\n  sections:\\n  - experiments\\n  tier: 1\\n  evidence:\\n  - exp_id: exp_012_rerun_1024\\n    metric: re.voting_rho_full\\n    value: 0.35\\n  note: Corrected from exp_015_metrics_expansion (0.4217) via exp_012_rerun_1024.\\n- id: c005_fk_beats_sj_re\\n  text: FK (ρ=0.275) exceeds SJ (ρ=0.250) on RE—a reversal from NER\\n  sections:\\n  - experiments\\n  tier: 1\\n  evidence:\\n  - exp_id: exp_012_rerun_1024\\n    metric: re.fk_rho_full\\n    value: 0.275\\n  - exp_id: exp_012_rerun_1024\\n    metric: re.sj_rho_full\\n    value: 0.25\\n  note: Corrected from exp_015 (FK 0.253, SJ 0.211) via exp_012_rerun_1024.\\n- id: c006_re_40pct_zero_f1\\n  text: 40% of RE instances receive zero F1 (N=8, seed=42; 159/397)\\n  sections:\\n  - experiments\\n  - discussion\\n  tier: 1\\n  evidence:\\n  - exp_id: mvp_pilot_004\\n    metric: re_sample_f1_pct_zero\\n    value: 44.3\\n    note: 44.3% from mvp_pilot_004; paper uses 40% from primary config (N=8, seed=42)\\n  - exp_id: exp_008_re_n16_v2\\n    metric: f1_zero_pct\\n    value: 44.3\\n    note: 44.3% at N=16; zero-F1 fraction varies with N and seed\\n- id: c007_em_leads_conll\\n  text: EM leads CoNLL with ρ=0.451 and AUROC=0.816\\n  sections:\\n  - experiments\\n  tier: 1\\n  evidence:\\n  - exp_id: exp_002\\n    metric: em_rho_full\\n    value: 0.4507\\n  - exp_id: exp_002\\n    metric: em_auroc_full\\n    value: 0.8156\\n  - exp_id: exp_015_v2\\n    metric: auroc_best.EM.conll_ner\\n    value: 0.8156\\n- id: c008_cross_model_sj_stability\\n  text: 'SJ cross-model gap: ρ=0.436 (Qwen) vs 0.431 (LLaMA), Δ=0.005'\\n  sections:\\n  - experiments\\n  tier: 1\\n  evidence:\\n  - exp_id: exp_002\\n    metric: sj_rho_full\\n    value: 0.4357\\n  - exp_id: exp_017_llama_conll_infer\\n    metric: full.SJ_rho\\n    value: 0.4314\\n- id: c009_logprob_paradox\\n  text: Logprob achieves highest AUROC (0.761) yet lowest ρ (0.307) on CoNLL LLaMA\\n  sections:\\n  - experiments\\n  - discussion\\n  tier: 1\\n  evidence:\\n  - exp_id: exp_017_llama_conll_infer\\n    metric: full.logprob_AUROC\\n    value: 0.761\\n  - exp_id: exp_017_llama_conll_infer\\n    metric: full.logprob_rho\\n    value: 0.3072\\n- id: c010_conll_oracle_headroom\\n  text: 'CoNLL oracle headroom: +4.2pp (Qwen), +1.8pp (LLaMA)'\\n  sections:\\n  - experiments\\n  tier: 1\\n  evidence:\\n  - exp_id: exp_002\\n    metric: oracle_headroom\\n    value: 0.042\\n  - exp_id: exp_017_llama_conll_infer\\n    metric: oracle_headroom\\n    value: 0.0177\\n- id: c011_ner_no_reliable_selection\\n  text: No signal reliably surpasses greedy on NER (logprob +0.6pp, p=0.39, 3-seed\\n    bootstrap)\\n  sections:\\n  - abstract\\n  - introduction\\n  - experiments\\n  - conclusion\\n  - discussion\\n  - related_work\\n  tier: 1\\n  evidence:\\n  - exp_id: exp_016_rerun_1024_bootstrap\\n    metric: selection_f1_ner\\n    value:\\n      greedy: 0.644\\n      logprob: 0.65\\n      sj: 0.645\\n      voting: 0.634\\n      random: 0.608\\n      oracle: 0.776\\n  - exp_id: exp_016_rerun_1024_bootstrap\\n    metric: bootstrap_selection_test\\n    value:\\n      logprob_vs_greedy_p: 0.39\\n      ci_95:\\n      - -0.03\\n      - 0.042\\n      cohens_d: 0.038\\n      sign_test: 61W/70L\\n  note: 3-seed bootstrap confirms +0.6pp is NOT statistically significant. Unified\\n    with c012 — no signal reliably helps on either task.\\n- id: c012_re_no_signal_beats_greedy\\n  text: No signal surpasses greedy on RE; logprob drops to −0.9pp\\n  sections:\\n  - abstract\\n  - introduction\\n  - experiments\\n  - conclusion\\n  - discussion\\n  tier: 1\\n  evidence:\\n  - exp_id: exp_016_rerun_1024_bootstrap\\n    metric: selection_f1_re\\n    value:\\n      greedy: 0.404\\n      logprob: 0.395\\n      sj: 0.386\\n      voting: 0.359\\n      random: 0.354\\n      oracle: 0.585\\n  note: CLAIM REVERSED from exp_016 (max_tokens=512). Old claim was \\\"only logprob\\n    helps on RE (+2.3pp)\\\". Corrected via exp_016_rerun_1024_bootstrap.\\n- id: c013_oracle_headroom_ner\\n  text: Oracle upper bound 0.776, 13.2pp above greedy 0.644 on NER\\n  sections:\\n  - experiments\\n  - discussion\\n  tier: 1\\n  evidence:\\n  - exp_id: exp_016_rerun_1024_bootstrap\\n    metric: selection_f1_ner.oracle\\n    value: 0.776\\n  - exp_id: exp_016_rerun_1024_bootstrap\\n    metric: selection_f1_ner.greedy\\n    value: 0.644\\n- id: c014_re_oracle_headroom\\n  text: 'RE oracle gap: 18.1pp (0.585 vs 0.404)'\\n  sections:\\n  - experiments\\n  - discussion\\n  tier: 1\\n  evidence:\\n  - exp_id: exp_016_rerun_1024_bootstrap\\n    metric: selection_f1_re.oracle\\n    value: 0.585\\n  - exp_id: exp_016_rerun_1024_bootstrap\\n    metric: selection_f1_re.greedy\\n    value: 0.404\\n- id: c015_ensemble_auroc\\n  text: SJ+Voting ensemble AUROC=0.666, below best individual signal EM (0.749)\\n  sections:\\n  - discussion\\n  tier: 1\\n  evidence:\\n  - exp_id: exp_016_rerun_1024_bootstrap\\n    metric: ensemble_ner_auroc\\n    value: 0.666\\n  note: Ensemble does NOT improve over best individual. Changed from positive to negative\\n    finding.\\n- id: c016_ece_calibration\\n  text: NER reasonably well-calibrated (calibration ECE 0.069-0.096), RE shows greater\\n    miscalibration (ECE 0.109-0.339)\\n  sections:\\n  - experiments\\n  tier: 1\\n  evidence:\\n  - exp_id: exp_016_rerun_1024_bootstrap\\n    metric: calibration_ece\\n    value:\\n      ner_range: 0.069-0.096\\n      re_range: 0.109-0.339\\n  note: Previous c016 used binary ECE (0.27-0.77) which was incorrect metric. Calibration\\n    ECE (signal confidence → mean F1 deviation) shows NER is well-calibrated, RE has\\n    moderate miscalibration. Consistent with fig_reliability_1024.\\n- id: c017_fisher_z_ner_vs_re\\n  text: 'Fisher''s z-test ρ_SJ NER vs RE: z=2.31, p=0.021'\\n  sections:\\n  - experiments\\n  tier: 1\\n  evidence:\\n  - exp_id: exp_004_re_diagnostic\\n    metric: fisher_z_ner_vs_re.sj_z\\n    value: 2.31\\n  - exp_id: exp_004_re_diagnostic\\n    metric: fisher_z_ner_vs_re.sj_p\\n    value: 0.0209\\n- id: c018_per_relation_diagnostic\\n  text: Feature-Of ρ≈0.004, Hyponym-Of ρ=0.646\\n  sections:\\n  - experiments\\n  tier: 1\\n  evidence:\\n  - exp_id: exp_004_re_diagnostic\\n    metric: per_relation_type.FEATURE-OF.rho_sj\\n    value: 0.004\\n  - exp_id: exp_004_re_diagnostic\\n    metric: per_relation_type.HYPONYM-OF.rho_fk\\n    value: 0.646\\n- id: c019_entity_span_errors\\n  text: Entity span errors account for 55.5% of RE false negatives\\n  sections:\\n  - experiments\\n  tier: 1\\n  evidence:\\n  - exp_id: exp_004_re_diagnostic\\n    metric: error_propagation\\n    value: head_error 17.7% + tail_error (derived) + head_tail_error 15.9% + full_error\\n      21.7% → entity span errors ~55.5%\\n  note: Computed from error_propagation breakdown in exp_004\\n- id: c020_capability_stratification_ner\\n  text: SJ ρ=0.547 on SciERC instances with 6+ entities, vs 0.415 for 1-2 entities\\n  sections:\\n  - experiments\\n  tier: 1\\n  evidence:\\n  - exp_id: exp_009_capability_stratification\\n    metric: scierc_ner.by_ent_count.6plus_sj_rho\\n    value: 0.547\\n  - exp_id: exp_009_capability_stratification\\n    metric: scierc_ner.by_ent_count.1_2_sj_rho\\n    value: 0.415\\n- id: c021_wnut_boundary\\n  text: 'WNUT-17: SJ ρ=0.089 (p=0.020), 54% zero F1'\\n  sections:\\n  - experiments\\n  - conclusion\\n  tier: 1\\n  evidence:\\n  - exp_id: exp_003_wnut17_eval\\n    metric: rho_sj\\n    value: 0.089\\n  - exp_id: exp_003_wnut17_eval\\n    metric: sample_f1_pct_zero\\n    value: 53.7\\n  note: 'Corrected 2026-05-16: paper uses ρ=0.089 from exp003_wnut17_eval (gold-filtered\\n    n=689, p=0.020). Old value 0.062 was untraceable — only in deprecated draft.'\\n- id: c022_wnut_logprob_negative\\n  text: WNUT logprob shows strong negative correlation\\n  sections:\\n  - experiments\\n  tier: 1\\n  evidence:\\n  - exp_id: exp_003_ner_wnut17\\n    metric: ner.rho_logprob_full\\n    value: -0.414\\n  - exp_id: exp_003_wnut17_eval\\n    metric: rho_logprob_full\\n    value: -0.409\\n- id: c023_re_sent_length_sj\\n  text: 'RE SJ ρ increases with sentence length: Q1 0.110 → Q4 0.473 (Fisher p=0.004)'\\n  sections:\\n  - experiments\\n  tier: 2\\n  evidence:\\n  - exp_id: exp_009_v2_re_rerun\\n    metric: by_sent_len_quartiles\\n    value:\\n      Q1_sj_rho: 0.11\\n      Q4_sj_rho: 0.473\\n      fisher_z_p: 0.004\\n  note: 'Corrected 2026-05-16: source is exp_009_v2_re_rerun (gold-filtered n=397).\\n    Old registry exp_009 values (Q1=0.447, Q4=0.540) used unfiltered n=551.'\\n- id: c024_high_complexity_re_subset\\n  text: 'High-complexity RE subset (n=81): Voting ρ=0.630, logprob ρ=0.554, SJ ρ=0.502'\\n  sections:\\n  - experiments\\n  tier: 2\\n  evidence:\\n  - exp_id: exp_009_capability_stratification\\n    metric: scierc_re.by_rel_count\\n    value:\\n      6plus_sj_rho: 0.527\\n  note: Registry has 6plus_sj_rho=0.527; paper may use exp_009_v2 data. Voting and\\n    logprob values not in registry summary.\\n- id: c025_temperature_sj_stable\\n  text: SJ NER ρ shifts from 0.388 (T=0.7) to 0.360 (T=1.0), Δ=0.028\\n  sections:\\n  - experiments\\n  tier: 1\\n  evidence:\\n  - exp_id: exp_005\\n    metric: sj_rho_t07_ner\\n    value: 0.388\\n  - exp_id: exp_012_rerun_1024\\n    metric: ner.sj_rho_full\\n    value: 0.36\\n  note: T=0.7 data from exp_005; T=1.0 from exp_015\\n- id: c026_n_scaling_sj\\n  text: SJ N=8→N=16 improves ρ from 0.360 to 0.412±0.025 (3-seed, +0.052) on Qwen\\n    SciERC NER\\n  sections:\\n  - experiments\\n  tier: 1\\n  evidence:\\n  - exp_id: exp_012_rerun_1024\\n    metric: ner.sj_rho_full\\n    value: 0.36\\n  - exp_id: exp_001_seed42_v2\\n    metric: sj_rho_full\\n    value: 0.428\\n  - exp_id: exp_001_seed123_v2\\n    metric: sj_rho_full\\n    value: 0.424\\n  - exp_id: exp_001_seed456_v2_ner\\n    metric: full.SJ.rho\\n    value: 0.384\\n  note: '3-seed mean: (0.428+0.424+0.384)/3 ≈ 0.412, σ=0.025'\\n- id: c027_llama_conll_3seed\\n  text: 'LLaMA CoNLL N=16 3-seed: SJ ρ=0.463±0.007, logprob ρ=0.310±0.005'\\n  sections:\\n  - experiments\\n  tier: 1\\n  evidence:\\n  - exp_id: exp_017_llama_conll_n16\\n    metric: full.SJ_rho\\n    value: 0.4642\\n  - exp_id: exp_017_llama_conll_n16_s123\\n    metric: full.SJ_rho\\n    value: 0.4698\\n  - exp_id: exp_017_llama_conll_n16_s456\\n    metric: full.SJ_rho\\n    value: 0.4552\\n  - exp_id: exp_017_llama_conll_n16\\n    metric: full.logprob_rho\\n    value: 0.3058\\n  - exp_id: exp_017_llama_conll_n16_s123\\n    metric: full.logprob_rho\\n    value: 0.3161\\n  - exp_id: exp_017_llama_conll_n16_s456\\n    metric: full.logprob_rho\\n    value: 0.3078\\n- id: c028_loo_sj_circularity\\n  text: LOO-SJ Δρ=-0.014, max per-instance Δρ=3.1×10⁻⁴—circularity negligible\\n  sections:\\n  - experiments\\n  tier: 1\\n  evidence:\\n  - exp_id: exp_015_v2\\n    metric: loo_sj.max_delta_rho\\n    value: 0.000305\\n  - exp_id: exp_015_v2\\n    metric: loo_sj.all_no_circularity\\n    value: true\\n- id: c029_llama_scierc_cross_model\\n  text: 'LLaMA replicates structural-over-surface on SciERC: NER SJ ρ=0.363 > FK ρ=0.327;\\n    conditional RE SJ ρ=0.405 > FK ρ=0.259'\\n  sections:\\n  - experiments\\n  tier: 1\\n  evidence:\\n  - exp_id: exp_007_llama_inference\\n    metric: ner.rho_sj\\n    value: 0.363\\n  - exp_id: exp_007_llama_inference\\n    metric: ner.rho_fk\\n    value: 0.327\\n  - exp_id: exp_007_llama_inference\\n    metric: re.sj_rho_cond\\n    value: 0.405\\n  - exp_id: exp_007_llama_inference\\n    metric: re.fk_rho_cond\\n    value: 0.259\\n- id: c030_em_conditional_dominance\\n  text: 'EM ranks #1 on conditional set across all 4 configurations'\\n  sections:\\n  - experiments\\n  tier: 1\\n  evidence:\\n  - exp_id: exp_015_metrics_expansion\\n    metric: ner.em_rho_cond\\n    value: 0.3427\\n  - exp_id: exp_015_metrics_expansion\\n    metric: re.em_rho_cond\\n    value: 0.3607\\n  - exp_id: exp_002_conll_n16\\n    metric: conditional.EM_rho\\n    value: 0.4658\\n  - exp_id: exp_017_llama_conll_n16_s123\\n    metric: conditional.EM_rho\\n    value: 0.4732\\n  note: 'Paper cites EM conditional: SciERC NER 0.408, RE 0.485, CoNLL Qwen N=16 0.466,\\n    CoNLL LLaMA 3-seed 0.462. Registry has slightly different values from different\\n    seed/N combinations.'\\n- id: c031_em_conditional_scierc\\n  text: 'EM conditional: NER ρ=0.408, RE ρ=0.485'\\n  sections:\\n  - experiments\\n  tier: 1\\n  evidence:\\n  - exp_id: exp_001_ner_n16_scierc\\n    metric: ner_cond_em_rho\\n    value: 0.414\\n  - exp_id: exp_001_ner_n16_scierc\\n    metric: re_cond_em_rho\\n    value: 0.475\\n  note: 'Paper rounds: 0.414→0.408, 0.475→0.485. May use different seed/N baseline.'\\n- id: c032_logprob_re_cond_collapse\\n  text: Logprob conditional RE collapses to ρ=0.011\\n  sections:\\n  - experiments\\n  tier: 1\\n  evidence:\\n  - exp_id: exp_012_rerun_1024\\n    metric: re_cond.logprob.rho\\n    value: 0.0112\\n  note: 'Corrected 2026-05-16: source is exp_012_rerun_1024 (greedy_f1>0 filter, n=238).\\n    Old exp_015 value 0.1457 used wrong filter (any sample F1>0, n=331). Old text\\n    0.002 was stale and untraceable.'\\n- id: c033_sj_n16_cond_re\\n  text: At N=16, SJ maintains ρ=0.308 on conditional RE while logprob drops to -0.026\\n  sections:\\n  - experiments\\n  - discussion\\n  tier: 1\\n  evidence:\\n  - exp_id: exp_008_re_n16_v2\\n    metric: sj_rho_cond\\n    value: 0.308\\n- id: c034_structural_over_logprob_n16\\n  text: Structural-over-logprob advantage holds across all 4 N=16 settings (Δ=+0.124\\n    to +0.175)\\n  sections:\\n  - experiments\\n  - discussion\\n  tier: 1\\n  evidence:\\n  - exp_id: exp_001_ner_n16_scierc\\n    metric: ner_voting_conf_rho\\n    value: 0.399\\n  - exp_id: exp_001_ner_n16_scierc\\n    metric: ner_logprob_rho\\n    value: 0.237\\n  - exp_id: exp_002_conll_n16\\n    metric: full.EM_rho\\n    value: 0.4627\\n  - exp_id: exp_002_conll_n16\\n    metric: full.logprob_rho\\n    value: 0.3146\\n  - exp_id: exp_007_llama_n16\\n    metric: full.voting_conf_rho\\n    value: 0.4515\\n  - exp_id: exp_007_llama_n16\\n    metric: full.logprob_rho\\n    value: 0.2041\\n  - exp_id: exp_017_llama_conll_n16\\n    metric: full.SJ_rho\\n    value: 0.4642\\n  - exp_id: exp_017_llama_conll_n16\\n    metric: full.logprob_rho\\n    value: 0.3058\\n- id: c035_n_scaling_diminishing\\n  text: 'SJ N-scaling gains are sublinear: +0.052 Qwen SciERC, +0.032 LLaMA CoNLL'\\n  sections:\\n  - discussion\\n  tier: 1\\n  evidence:\\n  - exp_id: exp_001_seed42_v2\\n    metric: sj_rho_full\\n    value: 0.428\\n  - exp_id: exp_015_metrics_expansion\\n    metric: ner.sj_rho_full\\n    value: 0.3565\\n  - exp_id: exp_017_llama_conll_n16\\n    metric: full.SJ_rho\\n    value: 0.4642\\n  - exp_id: exp_017_llama_conll_infer\\n    metric: full.SJ_rho\\n    value: 0.4314\\n  note: 'Qwen SciERC: 0.412 (3-seed mean) - 0.360 = +0.052. LLaMA CoNLL: 0.463 (3-seed)\\n    - 0.431 = +0.032'\\n- id: c036_sj_ece_calibration\\n  text: '[DEPRECATED] SJ achieves lowest calibration error (ECE=0.075-0.102 across\\n    settings)'\\n  sections: []\\n  tier: X\\n  evidence: []\\n  note: DEPRECATED — reversed by c016_ece_miscalibration. Old ECE values (0.075-0.102)\\n    were from exp_015 (max_tokens=512 truncation artifact). Corrected data shows all\\n    signals ECE 0.27-0.77.\\n- id: C001\\n  location:\\n    section: abstract\\n    paragraph: 0\\n    sentence: 0\\n  text: No signal significantly improves sample selection over greedy decoding despite\\n    13-18pp oracle headroom\\n  type: empirical\\n  evidence:\\n  - exp_012_rerun_1024\\n  decisions:\\n  - D070\\n  - D071\\n  deprecated: false\\n- id: C003\\n  location:\\n    section: abstract\\n    paragraph: 0\\n    sentence: 0\\n  text: LP scores compressed into effective ties for 60% of instances under constrained\\n    decoding\\n  type: empirical\\n  evidence:\\n  - exp_012_rerun_1024\\n  decisions: []\\n  deprecated: false\\n- id: C006\\n  location:\\n    section: abstract\\n    paragraph: 0\\n    sentence: 0\\n  text: Where LP compression is absent, selection recovers +2.9pp (p=0.01)\\n  type: empirical\\n  evidence:\\n  - exp_012_rerun_1024\\n  decisions: []\\n  deprecated: false\\n- id: C010\\n  location:\\n    section: abstract\\n    paragraph: 0\\n    sentence: 0\\n  text: Constrained-decoding score compression is the primary bottleneck\\n  type: empirical\\n  evidence:\\n  - exp_012_rerun_1024\\n  decisions: []\\n  deprecated: false\\n- id: C011\\n  location:\\n    section: discussion\\n    paragraph: 0\\n    sentence: 0\\n  text: LP carries useful per-sample quality information; score compression is the\\n    primary bottleneck\\n  type: empirical\\n  evidence:\\n  - exp_012_rerun_1024\\n  decisions:\\n  - D071\\n  deprecated: false\\n- id: C013\\n  location:\\n    section: discussion\\n    paragraph: 0\\n    sentence: 0\\n  text: MBR utility correlates with F1 across instances but not within\\n  type: empirical\\n  evidence:\\n  - exp_012_rerun_1024\\n  decisions: []\\n  deprecated: false\\n- id: C016\\n  location:\\n    section: discussion\\n    paragraph: 0\\n    sentence: 0\\n  text: Free-form ablation would test if bottleneck is decoding-regime-specific\\n  type: planned\\n  evidence: []\\n  decisions:\\n  - D071\\n  deprecated: false\\n- id: C017\\n  location:\\n    section: conclusion\\n    paragraph: 0\\n    sentence: 0\\n  text: Consistency signals effective QE (rho up to 0.38, AUROC up to 0.75) but fail\\n    at selection\\n  type: empirical\\n  evidence:\\n  - exp_012_rerun_1024\\n  decisions: []\\n  deprecated: false\\n- id: C019\\n  location:\\n    section: conclusion\\n    paragraph: 0\\n    sentence: 0\\n  text: LP fails due to constrained-decoding score compression\\n  type: empirical\\n  evidence:\\n  - exp_012_rerun_1024\\n  decisions: []\\n  deprecated: false\\n- id: C022\\n  location:\\n    section: conclusion\\n    paragraph: 0\\n    sentence: 0\\n  text: RE findings preliminary, single benchmark\\n  type: scope_limitation\\n  evidence:\\n  - exp_012_rerun_1024\\n  decisions: []\\n  deprecated: false\\n- id: C023\\n  location:\\n    section: sections/discussion\\n    paragraph: 0\\n    sentence: 0\\n  text: Entity-token LP exhibits 4x higher within-instance variance than full-sequence\\n    LP on SciERC, but selection performs worse (-2.0pp)\\n  type: quantitative\\n  evidence:\\n  - exp_id: exp_entity_token_lp\\n    metric: scierc_entity_lp_variance_ratio\\n    value: 4.0x\\n  - exp_id: exp_entity_token_lp\\n    metric: scierc_entity_lp_selection_delta\\n    value: -1.68\\n  decisions: []\\n  deprecated: false\\n- id: C024\\n  location:\\n    section: sections/discussion\\n    paragraph: 0\\n    sentence: 0\\n  text: On CoNLL, entity-token LP variance collapses to near-zero (median 2e-10) with\\n    79% tied\\n  type: quantitative\\n  evidence:\\n  - exp_id: exp_entity_token_lp\\n    metric: conll_entity_lp_variance_median\\n    value: 2e-10\\n  - exp_id: exp_entity_token_lp\\n    metric: conll_entity_lp_tied_fraction\\n    value: 0.794\\n  decisions: []\\n  deprecated: false\\n- id: C025\\n  location:\\n    section: sections/discussion\\n    paragraph: 0\\n    sentence: 0\\n  text: Entity-token LP rules out format-token dilution as primary cause; points to\\n    intrinsic model overconfidence on entity tokens\\n  type: interpretive\\n  evidence:\\n  - exp_id: exp_entity_token_lp\\n  decisions: []\\n  deprecated: false\\n- id: C026\\n  location:\\n    section: sections/limitations\\n    paragraph: 0\\n    sentence: 0\\n  text: Entity-token LP is the only tested remedy; LP×VC and calibration approaches\\n    are unexplored\\n  type: scope\\n  evidence:\\n  - exp_id: exp_entity_token_lp\\n  decisions: []\\n  deprecated: false\\n- id: C027\\n  location:\\n    section: sections/introduction\\n    paragraph: 0\\n    sentence: 0\\n  text: 'C1 reframe: instance-level nature is setup, LP compression + MBR within-instance\\n    failure are the findings'\\n  type: structural\\n  evidence: []\\n  decisions: []\\n  deprecated: false\\n- id: C028\\n  location:\\n    section: sections/introduction\\n    paragraph: 0\\n    sentence: 0\\n  text: 'SF4: 60% tied replaced with pooled within-instance ρ(LP,F1)=0.248 continuous\\n    characterization'\\n  type: structural\\n  evidence: []\\n  decisions: []\\n  deprecated: false\\n- id: C029\\n  location:\\n    section: sections/introduction\\n    paragraph: 0\\n    sentence: 0\\n  text: 'C2 reframe: entity-token LP added as diagnostic ablation contribution'\\n  type: structural\\n  evidence:\\n  - exp_id: exp_entity_token_lp\\n  decisions: []\\n  deprecated: false\\n- id: C030\\n  location:\\n    section: sections/abstract\\n    paragraph: 0\\n    sentence: 0\\n  text: 'SF3: RE removed from abstract; SF1: ρ=0.38 sourced to SciERC primary, up\\n    to 0.45 on ceiling control; MF2(a): benchmark roles explicit; M2: streamlined\\n    from 9 to 6 sentences'\\n  type: structural\\n  evidence: []\\n  decisions: []\\n  deprecated: false\\n- id: C031\\n  location:\\n    section: sections/discussion\\n    paragraph: 0\\n    sentence: 0\\n  text: 21% of SciERC instances produce identical F1 across all N samples\\n  type: quantitative\\n  evidence: Q1 within-instance analysis\\n  decisions: []\\n  deprecated: false\\n- id: C032\\n  location:\\n    section: sections/discussion\\n    paragraph: 0\\n    sentence: 0\\n  text: 58% of CoNLL instances produce identical F1 across all N samples\\n  type: quantitative\\n  evidence: Q1 within-instance analysis\\n  decisions: []\\n  deprecated: false\\n- id: C033\\n  location:\\n    section: sections/discussion\\n    paragraph: 0\\n    sentence: 0\\n  text: 13% of SciERC instances yield constant utility scores\\n  type: quantitative\\n  evidence: Q1 within-instance analysis\\n  decisions: []\\n  deprecated: false\\n- id: C034\\n  location:\\n    section: sections/discussion\\n    paragraph: 0\\n    sentence: 0\\n  text: 49% of CoNLL instances yield constant utility scores\\n  type: quantitative\\n  evidence: Q1 within-instance analysis\\n  decisions: []\\n  deprecated: false\\n- id: C035\\n  location:\\n    section: sections/discussion\\n    paragraph: 0\\n    sentence: 0\\n  text: SJ median within-instance rho = 0.524 on SciERC\\n  type: quantitative\\n  evidence: Q1 within-instance analysis\\n  decisions: []\\n  deprecated: false\\n- id: C036\\n  location:\\n    section: sections/discussion\\n    paragraph: 0\\n    sentence: 0\\n  text: SJ median within-instance rho = 0.994 on CoNLL\\n  type: quantitative\\n  evidence: Q1 within-instance analysis\\n  decisions: []\\n  deprecated: false\\n- id: C037\\n  location:\\n    section: sections/discussion\\n    paragraph: 0\\n    sentence: 0\\n  text: MBR closes 23% of oracle gap on non-degenerate SciERC instances\\n  type: quantitative\\n  evidence: Q1 within-instance analysis\\n  decisions: []\\n  deprecated: false\\n- id: C038\\n  location:\\n    section: sections/discussion\\n    paragraph: 0\\n    sentence: 0\\n  text: MBR closes 41% of oracle gap on non-degenerate CoNLL instances\\n  type: quantitative\\n  evidence: Q1 within-instance analysis\\n  decisions: []\\n  deprecated: false\\n- id: C039\\n  location:\\n    section: sections/discussion\\n    paragraph: 0\\n    sentence: 0\\n  text: Greedy T=0 achieves F1=0.663 on SciERC, surpassing all N=8 selection strategies\\n  type: quantitative\\n  evidence: SF4 greedy data\\n  decisions: []\\n  deprecated: false\\n- id: C040\\n  location:\\n    section: sections/discussion\\n    paragraph: 0\\n    sentence: 0\\n  text: SciERC 3-epoch rho=0.32 vs 5-epoch rho=0.28; LP delta -1.18 vs +0.62 pp\\n  type: quantitative\\n  evidence: tab:epoch_scierc\\n  decisions: []\\n  deprecated: false\\n- id: C041\\n  location:\\n    section: sections/discussion\\n    paragraph: 0\\n    sentence: 0\\n  text: Entity-level majority voting yields +0.76pp on SciERC (5.8% gap recovery)\\n  type: quantitative\\n  evidence: []\\n  decisions: []\\n  deprecated: false\\n- id: C042\\n  location:\\n    section: sections/discussion\\n    paragraph: 0\\n    sentence: 0\\n  text: Entity-level majority voting yields -0.64pp on CoNLL\\n  type: quantitative\\n  evidence: []\\n  decisions: []\\n  deprecated: false\\n- id: C043\\n  location:\\n    section: sections/discussion\\n    paragraph: 0\\n    sentence: 0\\n  text: Entity-level majority voting yields -3.21pp on Few-NERD\\n  type: quantitative\\n  evidence: []\\n  decisions: []\\n  deprecated: false\\n- id: C044\\n  location:\\n    section: sections/discussion\\n    paragraph: 0\\n    sentence: 0\\n  text: On degenerate subsets, merge is uniformly negative across all three datasets\\n  type: quantitative\\n  evidence: []\\n  decisions: []\\n  deprecated: false\\n- id: C045\\n  location:\\n    section: sections/appendix\\n    paragraph: 0\\n    sentence: 0\\n  text: Exact permutation p=0.005 for per-type degeneracy-headroom correlation\\n  type: quantitative\\n  evidence: []\\n  decisions: []\\n  deprecated: false\\n- id: C046\\n  location:\\n    section: sections/appendix\\n    paragraph: 0\\n    sentence: 0\\n  text: Under conservative df=4 adjustment, p=0.033\\n  type: quantitative\\n  evidence: []\\n  decisions: []\\n  deprecated: false\\n- id: C047\\n  location:\\n    section: sections/appendix\\n    paragraph: 0\\n    sentence: 0\\n  text: 3-epoch SciERC mean within-instance rho=0.273\\n  type: quantitative\\n  evidence: []\\n  decisions: []\\n  deprecated: false\\n- id: C048\\n  location:\\n    section: sections/appendix\\n    paragraph: 0\\n    sentence: 0\\n  text: 5-epoch SciERC mean within-instance rho=0.179\\n  type: quantitative\\n  evidence: []\\n  decisions: []\\n  deprecated: false\\n- id: C049\\n  location:\\n    section: sections/appendix\\n    paragraph: 0\\n    sentence: 0\\n  text: 76.4% of instances show positive LP-quality correlation at 3 epochs\\n  type: quantitative\\n  evidence: []\\n  decisions: []\\n  deprecated: false\\n- id: C050\\n  location:\\n    section: sections/appendix\\n    paragraph: 0\\n    sentence: 0\\n  text: 64.1% of instances show positive LP-quality correlation at 5 epochs\\n  type: quantitative\\n  evidence: []\\n  decisions: []\\n  deprecated: false\\n- id: C051\\n  location:\\n    section: sections/appendix\\n    paragraph: 0\\n    sentence: 0\\n  text: Epoch-to-epoch alignment variation is 0.057 median rho, small vs cross-dataset\\n    gap\\n  type: quantitative\\n  evidence: []\\n  decisions: []\\n  deprecated: false\\n- id: C052\\n  location:\\n    section: sections/appendix\\n    paragraph: 0\\n    sentence: 0\\n  text: 'Optimal DALS tau spans 2 orders of magnitude: FN 0.001, SciERC 0.05, CoNLL\\n    0.10'\\n  type: quantitative\\n  evidence: []\\n  decisions: []\\n  deprecated: false\\n- id: C053\\n  location:\\n    section: sections/appendix\\n    paragraph: 0\\n    sentence: 0\\n  text: LOO regret ranges from 0.51 to 1.21pp\\n  type: quantitative\\n  evidence: []\\n  decisions: []\\n  deprecated: false\\n- id: C054\\n  location:\\n    section: sections/appendix\\n    paragraph: 0\\n    sentence: 0\\n  text: Even with oracle tau, CoNLL remains at -0.31pp\\n  type: quantitative\\n  evidence: []\\n  decisions: []\\n  deprecated: false\\n- id: C055\\n  location:\\n    section: sections/appendix\\n    paragraph: 0\\n    sentence: 0\\n  text: 'SciERC entity merge best k=3: +1.57pp, 11.9% recovery'\\n  type: quantitative\\n  evidence: []\\n  decisions: []\\n  deprecated: false\\n- id: C056\\n  location:\\n    section: sections/appendix\\n    paragraph: 0\\n    sentence: 0\\n  text: 'CoNLL entity merge best k=3: -0.38pp, -9.0% recovery'\\n  type: quantitative\\n  evidence: []\\n  decisions: []\\n  deprecated: false\\n- id: C057\\n  location:\\n    section: sections/appendix\\n    paragraph: 0\\n    sentence: 0\\n  text: 'FewNERD entity merge best k=2: -0.43pp, -3.6% recovery'\\n  type: quantitative\\n  evidence: []\\n  decisions: []\\n  deprecated: false\\n- id: C058\\n  location:\\n    section: sections/experiments\\n    paragraph: 0\\n    sentence: 0\\n  text: 'Conditional decomp SciERC favorable: +2.47pp CI [+0.30, +4.70]'\\n  type: quantitative\\n  evidence: []\\n  decisions: []\\n  deprecated: false\\n- id: C059\\n  location:\\n    section: sections/experiments\\n    paragraph: 0\\n    sentence: 0\\n  text: 'Conditional decomp FewNERD favorable: +0.63pp CI [-0.02, +1.30], marginal'\\n  type: quantitative\\n  evidence: []\\n  decisions: []\\n  deprecated: false\\n- id: C060\\n  location:\\n    section: sections/experiments\\n    paragraph: 0\\n    sentence: 0\\n  text: 'Conditional decomp CoNLL favorable: -1.78pp CI [-2.83, -0.76], negative'\\n  type: quantitative\\n  evidence: []\\n  decisions: []\\n  deprecated: false\\n- id: C061\\n  location:\\n    section: sections/appendix\\n    paragraph: 0\\n    sentence: 0\\n  text: Entity-token LP has 4x higher within-instance variance (0.000644 vs 0.000161)\\n  type: quantitative\\n  evidence: []\\n  decisions: []\\n  deprecated: false\\n- id: C062\\n  location:\\n    section: sections/appendix\\n    paragraph: 0\\n    sentence: 0\\n  text: Entity-token LP rho=0.440 vs full-sequence 0.297\\n  type: quantitative\\n  evidence: []\\n  decisions: []\\n  deprecated: false\\n- id: C063\\n  location:\\n    section: sections/appendix\\n    paragraph: 0\\n    sentence: 0\\n  text: Entity-token LP selection -0.73pp vs full-sequence +0.35pp\\n  type: quantitative\\n  evidence: []\\n  decisions: []\\n  deprecated: false\\ntables:\\n- id: tab:notation\\n  section: method\\n  caption: Notation used throughout the paper\\n  evidence: []\\n  note: Notation table—no experimental data.\\n- id: tab:quality_estimation\\n  section: experiments\\n  caption: Quality estimation across tasks and models (Spearman ρ and AUROC)\\n  evidence:\\n  - exp_id: exp_012_rerun_1024\\n    role: SciERC NER ρ values (N=8, Qwen) — corrected from exp_015 (truncation artifact)\\n  - exp_id: exp_015_metrics_expansion\\n    role: SciERC RE ρ values (N=8, Qwen) — RE values unaffected by truncation fix\\n  - exp_id: exp_015_v2\\n    role: AUROC values across settings\\n  - exp_id: exp_002\\n    role: CoNLL Qwen N=8 ρ and AUROC\\n  - exp_id: exp_017_llama_conll_infer\\n    role: CoNLL LLaMA N=8 ρ and AUROC\\n  - exp_id: exp_017_llama_conll_n16\\n    role: LLaMA CoNLL N=16 3-seed (seed=42)\\n  - exp_id: exp_017_llama_conll_n16_s123\\n    role: LLaMA CoNLL N=16 3-seed (seed=123)\\n  - exp_id: exp_017_llama_conll_n16_s456\\n    role: LLaMA CoNLL N=16 3-seed (seed=456)\\n- id: tab:selection\\n  section: experiments\\n  caption: Best-of-N selection F1 on SciERC (N=8, T=1.0)\\n  evidence:\\n  - exp_id: exp_016_signal_ensemble\\n    role: All selection F1 values (NER and RE)\\n- id: tab:robustness\\n  section: experiments\\n  caption: Signal robustness across configurations (Spearman ρ)\\n  evidence:\\n  - exp_id: exp_005\\n    role: Temperature block (T=0.7 vs T=1.0, Qwen SciERC)\\n  - exp_id: exp_015_metrics_expansion\\n    role: N=8 baseline values\\n  - exp_id: exp_001_seed42_v2\\n    role: N=16 SJ ρ seed=42\\n  - exp_id: exp_001_seed123_v2\\n    role: N=16 SJ ρ seed=123\\n  - exp_id: exp_001_seed456_v2_ner\\n    role: N=16 SJ ρ seed=456\\n  - exp_id: exp_017_llama_conll_n16\\n    role: 'Cross-model block: LLaMA CoNLL N=16 seed=42'\\n  - exp_id: exp_017_llama_conll_n16_s123\\n    role: 'Cross-model block: LLaMA CoNLL N=16 seed=123'\\n  - exp_id: exp_017_llama_conll_n16_s456\\n    role: 'Cross-model block: LLaMA CoNLL N=16 seed=456'\\nfigures:\\n- id: fig:overview\\n  section: introduction\\n  caption: The correlation-selection gap conceptual diagram\\n  evidence:\\n  - exp_id: exp_015_metrics_expansion\\n    role: Quality estimation data (ρ, AUROC for left panel)\\n  - exp_id: exp_016_signal_ensemble\\n    role: Selection F1 data (right panel)\\n- id: fig:signal_heatmap\\n  section: experiments\\n  caption: Quality estimation heatmap (Spearman ρ) across five signals and four configurations\\n  evidence:\\n  - exp_id: exp_015_metrics_expansion\\n    role: Full set ρ values for SciERC NER/RE (Qwen, N=8)\\n  - exp_id: exp_002\\n    role: CoNLL Qwen full set ρ values\\n  - exp_id: exp_001_ner_n16_scierc\\n    role: Conditional set ρ values\\n- id: fig:selection_gap\\n  section: experiments\\n  caption: The correlation-selection gap on SciERC (N=8)\\n  evidence:\\n  - exp_id: exp_016_signal_ensemble\\n    role: Best-of-N selection F1 bars and quality estimation ρ line\\n- id: fig:temperature_robustness\\n  section: experiments\\n  caption: Temperature robustness on SciERC (N=8)\\n  evidence:\\n  - exp_id: exp_005\\n    role: SJ, FK ρ values at T=0.7 and T=1.0\\n- id: fig:reliability\\n  section: experiments\\n  caption: Reliability diagrams on SciERC (N=8, T=1.0)\\n  evidence:\\n  - exp_id: exp_015_metrics_expansion\\n    role: Calibration/ECE data for all signals\\n  - exp_id: exp_002\\n    role: ECE values across signals\\n_completeness:\\n  coverage: 59/92\\n  claims: 87\\n  tables: 4\\n  figures: 5\\n  tier_counts:\\n    tier1: 0\\n    tier2: 59\\n    tier3: 33\\n    tierX: 0\\n  last_checked: '2026-05-18T15:39:48.035668+00:00'\\n\", \"total_chars\": 32730, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9e8ac923-9d33-4522-bfdd-ff21639b0c27",
  "isSidechain": false,
  "promptId": "0731b9be-f5e6-4a8a-9a3c-2edafe06629b",
  "type": "user",
  "uuid": "e89a0b59-1557-477c-8ff1-b9669ff0f5dd",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"path\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/paper_provenance.yaml\\\", \\\"content\\\": \\\"paper:\\\\n  title: 'Strong Predictors, Weak Selectors: A Systematic Comparison of Confidence\\\\n    Signals for Test-Time Scaling in Information Extraction'\\\\n  version: 169\\\\n  generated_at: '2026-05-18T15:39:48.035618+00:00'\\\\n  source: manual provenance build by Paper Agent\\\\nclaims:\\\\n- id: c001_voting_rho_scierc_ner\\\\n  text: Voting Confidence achieves ρ=0.379 on SciERC NER (corrected from 0.502 truncation\\\\n    artifact)\\\\n  sections:\\\\n  - abstract\\\\n  - introduction\\\\n  - experiments\\\\n  - conclusion\\\\n  - discussion\\\\n  - related_work\\\\n  tier: 1\\\\n  evidence:\\\\n  - exp_id: exp_012_rerun_1024\\\\n    metric: ner.voting_rho_full\\\\n    value: 0.379\\\\n  note: Old value 0.502 from exp_015 was inflated by max_tokens=512 truncation. Corrected\\\\n    via exp_012_rerun_1024 (max_tokens=1024).\\\\n- id: c002_auroc_dissociation_scierc\\\\n  text: ρ-AUROC dissociation on SciERC — EM leads AUROC (NER 0.749, RE 0.706) while\\\\n    Voting leads ρ (NER 0.379, RE 0.422)\\\\n  sections:\\\\n  - abstract\\\\n  - introduction\\\\n  - experiments\\\\n  - conclusion\\\\n  - discussion\\\\n  tier: 1\\\\n  evidence:\\\\n  - exp_id: exp_012_rerun_1024\\\\n    metric: ner.em_auroc\\\\n    value: 0.749\\\\n  - exp_id: exp_012_rerun_1024\\\\n    metric: re.em_auroc\\\\n    value: 0.706\\\\n  - exp_id: exp_012_rerun_1024\\\\n    metric: ner.voting_auroc\\\\n    value: 0.684\\\\n  note: Old Table 1 had Voting NER AUROC=.741 (from exp_015 truncated). Corrected\\\\n    to .684 via exp_012_rerun_1024. EM now leads AUROC on both NER and RE. Headline\\\\n    claim changed from \\\\\\\"entity voting achieves ρ=0.38 and AUROC=0.74\\\\\\\" to split ρ (Voting\\\\n    0.38) / AUROC (EM 0.75) claim.\\\\n- id: c003_sj_rho_scierc_ner\\\\n  text: SJ achieves ρ=0.360 on SciERC NER (corrected from 0.357)\\\\n  sections:\\\\n  - experiments\\\\n  tier: 1\\\\n  evidence:\\\\n  - exp_id: exp_012_rerun_1024\\\\n    metric: ner.sj_rho_full\\\\n    value: 0.36\\\\n  - exp_id: exp_004_re_diagnostic\\\\n    metric: bootstrap_ci_95.ner_sj\\\\n    value:\\\\n    - 0.2946\\\\n    - 0.4586\\\\n- id: c004_voting_leads_re\\\\n  text: Voting leads RE full set (ρ=0.350, corrected from 0.422)\\\\n  sections:\\\\n  - experiments\\\\n  tier: 1\\\\n  evidence:\\\\n  - exp_id: exp_012_rerun_1024\\\\n    metric: re.voting_rho_full\\\\n    value: 0.35\\\\n  note: Corrected from exp_015_metrics_expansion (0.4217) via exp_012_rerun_1024.\\\\n- id: c005_fk_beats_sj_re\\\\n  text: FK (ρ=0.275) exceeds SJ (ρ=0.250) on RE—a reversal from NER\\\\n  sections:\\\\n  - experiments\\\\n  tier: 1\\\\n  evidence:\\\\n  - exp_id: exp_012_rerun_1024\\\\n    metric: re.fk_rho_full\\\\n    value: 0.275\\\\n  - exp_id: exp_012_rerun_1024\\\\n    metric: re.sj_rho_full\\\\n    value: 0.25\\\\n  note: Corrected from exp_015 (FK 0.253, SJ 0.211) via exp_012_rerun_1024.\\\\n- id: c006_re_40pct_zero_f1\\\\n  text: 40% of RE instances receive zero F1 (N=8, seed=42; 159/397)\\\\n  sections:\\\\n  - experiments\\\\n  - discussion\\\\n  tier: 1\\\\n  evidence:\\\\n  - exp_id: mvp_pilot_004\\\\n    metric: re_sample_f1_pct_zero\\\\n    value: 44.3\\\\n    note: 44.3% from mvp_pilot_004; paper uses 40% from primary config (N=8, seed=42)\\\\n  - exp_id: exp_008_re_n16_v2\\\\n    metric: f1_zero_pct\\\\n    value: 44.3\\\\n    note: 44.3% at N=16; zero-F1 fraction varies with N and seed\\\\n- id: c007_em_leads_conll\\\\n  text: EM leads CoNLL with ρ=0.451 and AUROC=0.816\\\\n  sections:\\\\n  - experiments\\\\n  tier: 1\\\\n  evidence:\\\\n  - exp_id: exp_002\\\\n    metric: em_rho_full\\\\n    value: 0.4507\\\\n  - exp_id: exp_002\\\\n    metric: em_auroc_full\\\\n    value: 0.8156\\\\n  - exp_id: exp_015_v2\\\\n    metric: auroc_best.EM.conll_ner\\\\n    value: 0.8156\\\\n- id: c008_cross_model_sj_stability\\\\n  text: 'SJ cross-model gap: ρ=0.436 (Qwen) vs 0.431 (LLaMA), Δ=0.005'\\\\n  sections:\\\\n  - experiments\\\\n  tier: 1\\\\n  evidence:\\\\n  - exp_id: exp_002\\\\n    metric: sj_rho_full\\\\n    value: 0.4357\\\\n  - exp_id: exp_017_llama_conll_infer\\\\n    metric: full.SJ_rho\\\\n    value: 0.4314\\\\n- id: c009_logprob_paradox\\\\n  text: Logprob achieves highest AUROC (0.761) yet lowest ρ (0.307) on CoNLL LLaMA\\\\n  sections:\\\\n  - experiments\\\\n  - discussion\\\\n  tier: 1\\\\n  evidence:\\\\n  - exp_id: exp_017_llama_conll_infer\\\\n    metric: full.logprob_AUROC\\\\n    value: 0.761\\\\n  - exp_id: exp_017_llama_conll_infer\\\\n    metric: full.logprob_rho\\\\n    value: 0.3072\\\\n- id: c010_conll_oracle_headroom\\\\n  text: 'CoNLL oracle headroom: +4.2pp (Qwen), +1.8pp (LLaMA)'\\\\n  sections:\\\\n  - experiments\\\\n  tier: 1\\\\n  evidence:\\\\n  - exp_id: exp_002\\\\n    metric: oracle_headroom\\\\n    value: 0.042\\\\n  - exp_id: exp_017_llama_conll_infer\\\\n    metric: oracle_headroom\\\\n    value: 0.0177\\\\n- id: c011_ner_no_reliable_selection\\\\n  text: No signal reliably surpasses greedy on NER (logprob +0.6pp, p=0.39, 3-seed\\\\n    bootstrap)\\\\n  sections:\\\\n  - abstract\\\\n  - introduction\\\\n  - experiments\\\\n  - conclusion\\\\n  - discussion\\\\n  - related_work\\\\n  tier: 1\\\\n  evidence:\\\\n  - exp_id: exp_016_rerun_1024_bootstrap\\\\n    metric: selection_f1_ner\\\\n    value:\\\\n      greedy: 0.644\\\\n      logprob: 0.65\\\\n      sj: 0.645\\\\n      voting: 0.634\\\\n      random: 0.608\\\\n      oracle: 0.776\\\\n  - exp_id: exp_016_rerun_1024_bootstrap\\\\n    metric: bootstrap_selection_test\\\\n    value:\\\\n      logprob_vs_greedy_p: 0.39\\\\n      ci_95:\\\\n      - -0.03\\\\n      - 0.042\\\\n      cohens_d: 0.038\\\\n      sign_test: 61W/70L\\\\n  note: 3-seed bootstrap confirms +0.6pp is NOT statistically significant. Unified\\\\n    with c012 — no signal reliably helps on either task.\\\\n- id: c012_re_no_signal_beats_greedy\\\\n  text: No signal surpasses greedy on RE; logprob drops to −0.9pp\\\\n  sections:\\\\n  - abstract\\\\n  - introduction\\\\n  - experiments\\\\n  - conclusion\\\\n  - discussion\\\\n  tier: 1\\\\n  evidence:\\\\n  - exp_id: exp_016_rerun_1024_bootstrap\\\\n    metric: selection_f1_re\\\\n    value:\\\\n      greedy: 0.404\\\\n      logprob: 0.395\\\\n      sj: 0.386\\\\n      voting: 0.359\\\\n      random: 0.354\\\\n      oracle: 0.585\\\\n  note: CLAIM REVERSED from exp_016 (max_tokens=512). Old claim was \\\\\\\"only logprob\\\\n    helps on RE (+2.3pp)\\\\\\\". Corrected via exp_016_rerun_1024_bootstrap.\\\\n- id: c013_oracle_headroom_ner\\\\n  text: Oracle upper bound 0.776, 13.2pp above greedy 0.644 on NER\\\\n  sections:\\\\n  - experiments\\\\n  - discussion\\\\n  tier: 1\\\\n  evidence:\\\\n  - exp_id: exp_016_rerun_1024_bootstrap\\\\n    metric: selection_f1_ner.oracle\\\\n    value: 0.776\\\\n  - exp_id: exp_016_rerun_1024_bootstrap\\\\n    metric: selection_f1_ner.greedy\\\\n    value: 0.644\\\\n- id: c014_re_oracle_headroom\\\\n  text: 'RE oracle gap: 18.1pp (0.585 vs 0.404)'\\\\n  sections:\\\\n  - experiments\\\\n  - discussion\\\\n  tier: 1\\\\n  evidence:\\\\n  - exp_id: exp_016_rerun_1024_bootstrap\\\\n    metric: selection_f1_re.oracle\\\\n    value: 0.585\\\\n  - exp_id: exp_016_rerun_1024_bootstrap\\\\n    metric: selection_f1_re.greedy\\\\n    value: 0.404\\\\n- id: c015_ensemble_auroc\\\\n  text: SJ+Voting ensemble AUROC=0.666, below best individual signal EM (0.749)\\\\n  sections:\\\\n  - discussion\\\\n  tier: 1\\\\n  evidence:\\\\n  - exp_id: exp_016_rerun_1024_bootstrap\\\\n    metric: ensemble_ner_auroc\\\\n    value: 0.666\\\\n  note: Ensemble does NOT improve over best individual. Changed from positive to negative\\\\n    finding.\\\\n- id: c016_ece_calibration\\\\n  text: NER reasonably well-calibrated (calibration ECE 0.069-0.096), RE shows greater\\\\n    miscalibration (ECE 0.109-0.339)\\\\n  sections:\\\\n  - experiments\\\\n  tier: 1\\\\n  evidence:\\\\n  - exp_id: exp_016_rerun_1024_bootstrap\\\\n    metric: calibration_ece\\\\n    value:\\\\n      ner_range: 0.069-0.096\\\\n      re_range: 0.109-0.339\\\\n  note: Previous c016 used binary ECE (0.27-0.77) which was incorrect metric. Calibration\\\\n    ECE (signal confidence → mean F1 deviation) shows NER is well-calibrated, RE has\\\\n    moderate miscalibration. Consistent with fig_reliability_1024.\\\\n- id: c017_fisher_z_ner_vs_re\\\\n  text: 'Fisher''s z-test ρ_SJ NER vs RE: z=2.31, p=0.021'\\\\n  sections:\\\\n  - experiments\\\\n  tier: 1\\\\n  evidence:\\\\n  - exp_id: exp_004_re_diagnostic\\\\n    metric: fisher_z_ner_vs_re.sj_z\\\\n    value: 2.31\\\\n  - exp_id: exp_004_re_diagnostic\\\\n    metric: fisher_z_ner_vs_re.sj_p\\\\n    value: 0.0209\\\\n- id: c018_per_relation_diagnostic\\\\n  text: Feature-Of ρ≈0.004, Hyponym-Of ρ=0.646\\\\n  sections:\\\\n  - experiments\\\\n  tier: 1\\\\n  evidence:\\\\n  - exp_id: exp_004_re_diagnostic\\\\n    metric: per_relation_type.FEATURE-OF.rho_sj\\\\n    value: 0.004\\\\n  - exp_id: exp_004_re_diagnostic\\\\n    metric: per_relation_type.HYPONYM-OF.rho_fk\\\\n    value: 0.646\\\\n- id: c019_entity_span_errors\\\\n  text: Entity span errors account for 55.5% of RE false negatives\\\\n  sections:\\\\n  - experiments\\\\n  tier: 1\\\\n  evidence:\\\\n  - exp_id: exp_004_re_diagnostic\\\\n    metric: error_propagation\\\\n    value: head_error 17.7% + tail_error (derived) + head_tail_error 15.9% + full_error\\\\n      21.7% → entity span errors ~55.5%\\\\n  note: Computed from error_propagation breakdown in exp_004\\\\n- id: c020_capability_stratification_ner\\\\n  text: SJ ρ=0.547 on SciERC instances with 6+ entities, vs 0.415 for 1-2 entities\\\\n  sections:\\\\n  - experiments\\\\n  tier: 1\\\\n  evidence:\\\\n  - exp_id: exp_009_capability_stratification\\\\n    metric: scierc_ner.by_ent_count.6plus_sj_rho\\\\n    value: 0.547\\\\n  - exp_id: exp_009_capability_stratification\\\\n    metric: scierc_ner.by_ent_count.1_2_sj_rho\\\\n    value: 0.415\\\\n- id: c021_wnut_boundary\\\\n  text: 'WNUT-17: SJ ρ=0.089 (p=0.020), 54% zero F1'\\\\n  sections:\\\\n  - experiments\\\\n  - conclusion\\\\n  tier: 1\\\\n  evidence:\\\\n  - exp_id: exp_003_wnut17_eval\\\\n    metric: rho_sj\\\\n    value: 0.089\\\\n  - exp_id: exp_003_wnut17_eval\\\\n    metric: sample_f1_pct_zero\\\\n    value: 53.7\\\\n  note: 'Corrected 2026-05-16: paper uses ρ=0.089 from exp003_wnut17_eval (gold-filtered\\\\n    n=689, p=0.020). Old value 0.062 was untraceable — only in deprecated draft.'\\\\n- id: c022_wnut_logprob_negative\\\\n  text: WNUT logprob shows strong negative correlation\\\\n  sections:\\\\n  - experiments\\\\n  tier: 1\\\\n  evidence:\\\\n  - exp_id: exp_003_ner_wnut17\\\\n    metric: ner.rho_logprob_full\\\\n    value: -0.414\\\\n  - exp_id: exp_003_wnut17_eval\\\\n    metric: rho_logprob_full\\\\n    value: -0.409\\\\n- id: c023_re_sent_length_sj\\\\n  text: 'RE SJ ρ increases with sentence length: Q1 0.110 → Q4 0.473 (Fisher p=0.004)'\\\\n  sections:\\\\n  - experiments\\\\n  tier: 2\\\\n  evidence:\\\\n  - exp_id: exp_009_v2_re_rerun\\\\n    metric: by_sent_len_quartiles\\\\n    value:\\\\n      Q1_sj_rho: 0.11\\\\n      Q4_sj_rho: 0.473\\\\n      fisher_z_p: 0.004\\\\n  note: 'Corrected 2026-05-16: source is exp_009_v2_re_rerun (gold-filtered n=397).\\\\n    Old registry exp_009 values (Q1=0.447, Q4=0.540) used unfiltered n=551.'\\\\n- id: c024_high_complexity_re_subset\\\\n  text: 'High-complexity RE subset (n=81): Voting ρ=0.630, logprob ρ=0.554, SJ ρ=0.502'\\\\n  sections:\\\\n  - experiments\\\\n  tier: 2\\\\n  evidence:\\\\n  - exp_id: exp_009_capability_stratification\\\\n    metric: scierc_re.by_rel_count\\\\n    value:\\\\n      6plus_sj_rho: 0.527\\\\n  note: Registry has 6plus_sj_rho=0.527; paper may use exp_009_v2 data. Voting and\\\\n    logprob values not in registry summary.\\\\n- id: c025_temperature_sj_stable\\\\n  text: SJ NER ρ shifts from 0.388 (T=0.7) to 0.360 (T=1.0), Δ=0.028\\\\n  sections:\\\\n  - experiments\\\\n  tier: 1\\\\n  evidence:\\\\n  - exp_id: exp_005\\\\n    metric: sj_rho_t07_ner\\\\n    value: 0.388\\\\n  - exp_id: exp_012_rerun_1024\\\\n    metric: ner.sj_rho_full\\\\n    value: 0.36\\\\n  note: T=0.7 data from exp_005; T=1.0 from exp_015\\\\n- id: c026_n_scaling_sj\\\\n  text: SJ N=8→N=16 improves ρ from 0.360 to 0.412±0.025 (3-seed, +0.052) on Qwen\\\\n    SciERC NER\\\\n  sections:\\\\n  - experiments\\\\n  tier: 1\\\\n  evidence:\\\\n  - exp_id: exp_012_rerun_1024\\\\n    metric: ner.sj_rho_full\\\\n    value: 0.36\\\\n  - exp_id: exp_001_seed42_v2\\\\n    metric: sj_rho_full\\\\n    value: 0.428\\\\n  - exp_id: exp_001_seed123_v2\\\\n    metric: sj_rho_full\\\\n    value: 0.424\\\\n  - exp_id: exp_001_seed456_v2_ner\\\\n    metric: full.SJ.rho\\\\n    value: 0.384\\\\n  note: '3-seed mean: (0.428+0.424+0.384)/3 ≈ 0.412, σ=0.025'\\\\n- id: c027_llama_conll_3seed\\\\n  text: 'LLaMA CoNLL N=16 3-seed: SJ ρ=0.463±0.007, logprob ρ=0.310±0.005'\\\\n  sections:\\\\n  - experiments\\\\n  tier: 1\\\\n  evidence:\\\\n  - exp_id: exp_017_llama_conll_n16\\\\n    metric: full.SJ_rho\\\\n    value: 0.4642\\\\n  - exp_id: exp_017_llama_conll_n16_s123\\\\n    metric: full.SJ_rho\\\\n    value: 0.4698\\\\n  - exp_id: exp_017_llama_conll_n16_s456\\\\n    metric: full.SJ_rho\\\\n    value: 0.4552\\\\n  - exp_id: exp_017_llama_conll_n16\\\\n    metric: full.logprob_rho\\\\n    value: 0.3058\\\\n  - exp_id: exp_017_llama_conll_n16_s123\\\\n    metric: full.logprob_rho\\\\n    value: 0.3161\\\\n  - exp_id: exp_017_llama_conll_n16_s456\\\\n    metric: full.logprob_rho\\\\n    value: 0.3078\\\\n- id: c028_loo_sj_circularity\\\\n  text: LOO-SJ Δρ=-0.014, max per-instance Δρ=3.1×10⁻⁴—circularity negligible\\\\n  sections:\\\\n  - experiments\\\\n  tier: 1\\\\n  evidence:\\\\n  - exp_id: exp_015_v2\\\\n    metric: loo_sj.max_delta_rho\\\\n    value: 0.000305\\\\n  - exp_id: exp_015_v2\\\\n    metric: loo_sj.all_no_circularity\\\\n    value: true\\\\n- id: c029_llama_scierc_cross_model\\\\n  text: 'LLaMA replicates structural-over-surface on SciERC: NER SJ ρ=0.363 > FK ρ=0.327;\\\\n    conditional RE SJ ρ=0.405 > FK ρ=0.259'\\\\n  sections:\\\\n  - experiments\\\\n  tier: 1\\\\n  evidence:\\\\n  - exp_id: exp_007_llama_inference\\\\n    metric: ner.rho_sj\\\\n    value: 0.363\\\\n  - exp_id: exp_007_llama_inference\\\\n    metric: ner.rho_fk\\\\n    value: 0.327\\\\n  - exp_id: exp_007_llama_inference\\\\n    metric: re.sj_rho_cond\\\\n    value: 0.405\\\\n  - exp_id: exp_007_llama_inference\\\\n    metric: re.fk_rho_cond\\\\n    value: 0.259\\\\n- id: c030_em_conditional_dominance\\\\n  text: 'EM ranks #1 on conditional set across all 4 configurations'\\\\n  sections:\\\\n  - experiments\\\\n  tier: 1\\\\n  evidence:\\\\n  - exp_id: exp_015_metrics_expansion\\\\n    metric: ner.em_rho_cond\\\\n    value: 0.3427\\\\n  - exp_id: exp_015_metrics_expansion\\\\n    metric: re.em_rho_cond\\\\n    value: 0.3607\\\\n  - exp_id: exp_002_conll_n16\\\\n    metric: conditional.EM_rho\\\\n    value: 0.4658\\\\n  - exp_id: exp_017_llama_conll_n16_s123\\\\n    metric: conditional.EM_rho\\\\n    value: 0.4732\\\\n  note: 'Paper cites EM conditional: SciERC NER 0.408, RE 0.485, CoNLL Qwen N=16 0.466,\\\\n    CoNLL LLaMA 3-seed 0.462. Registry has slightly different values from different\\\\n    seed/N combinations.'\\\\n- id: c031_em_conditional_scierc\\\\n  text: 'EM conditional: NER ρ=0.408, RE ρ=0.485'\\\\n  sections:\\\\n  - experiments\\\\n  tier: 1\\\\n  evidence:\\\\n  - exp_id: exp_001_ner_n16_scierc\\\\n    metric: ner_cond_em_rho\\\\n    value: 0.414\\\\n  - exp_id: exp_001_ner_n16_scierc\\\\n    metric: re_cond_em_rho\\\\n    value: 0.475\\\\n  note: 'Paper rounds: 0.414→0.408, 0.475→0.485. May use different seed/N baseline.'\\\\n- id: c032_logprob_re_cond_collapse\\\\n  text: Logprob conditional RE collapses to ρ=0.011\\\\n  sections:\\\\n  - experiments\\\\n  tier: 1\\\\n  evidence:\\\\n  - exp_id: exp_012_rerun_1024\\\\n    metric: re_cond.logprob.rho\\\\n    value: 0.0112\\\\n  note: 'Corrected 2026-05-16: source is exp_012_rerun_1024 (greedy_f1>0 filter, n=238).\\\\n    Old exp_015 value 0.1457 used wrong filter (any sample F1>0, n=331). Old text\\\\n    0.002 was stale and untraceable.'\\\\n- id: c033_sj_n16_cond_re\\\\n  text: At N=16, SJ maintains ρ=0.308 on conditional RE while logprob drops to -0.026\\\\n  sections:\\\\n  - experiments\\\\n  - discussion\\\\n  tier: 1\\\\n  evidence:\\\\n  - exp_id: exp_008_re_n16_v2\\\\n    metric: sj_rho_cond\\\\n    value: 0.308\\\\n- id: c034_structural_over_logprob_n16\\\\n  text: Structural-over-logprob advantage holds across all 4 N=16 settings (Δ=+0.124\\\\n    to +0.175)\\\\n  sections:\\\\n  - experiments\\\\n  - discussion\\\\n  tier: 1\\\\n  evidence:\\\\n  - exp_id: exp_001_ner_n16_scierc\\\\n    metric: ner_voting_conf_rho\\\\n    value: 0.399\\\\n  - exp_id: exp_001_ner_n16_scierc\\\\n    metric: ner_logprob_rho\\\\n    value: 0.237\\\\n  - exp_id: exp_002_conll_n16\\\\n    metric: full.EM_rho\\\\n    value: 0.4627\\\\n  - exp_id: exp_002_conll_n16\\\\n    metric: full.logprob_rho\\\\n    value: 0.3146\\\\n  - exp_id: exp_007_llama_n16\\\\n    metric: full.voting_conf_rho\\\\n    value: 0.4515\\\\n  - exp_id: exp_007_llama_n16\\\\n    metric: full.logprob_rho\\\\n    value: 0.2041\\\\n  - exp_id: exp_017_llama_conll_n16\\\\n    metric: full.SJ_rho\\\\n    value: 0.4642\\\\n  - exp_id: exp_017_llama_conll_n16\\\\n    metric: full.logprob_rho\\\\n    value: 0.3058\\\\n- id: c035_n_scaling_diminishing\\\\n  text: 'SJ N-scaling gains are sublinear: +0.052 Qwen SciERC, +0.032 LLaMA CoNLL'\\\\n  sections:\\\\n  - discussion\\\\n  tier: 1\\\\n  evidence:\\\\n  - exp_id: exp_001_seed42_v2\\\\n    metric: sj_rho_full\\\\n    value: 0.428\\\\n  - exp_id: exp_015_metrics_expansion\\\\n    metric: ner.sj_rho_full\\\\n    value: 0.3565\\\\n  - exp_id: exp_017_llama_conll_n16\\\\n    metric: full.SJ_rho\\\\n    value: 0.4642\\\\n  - exp_id: exp_017_llama_conll_infer\\\\n    metric: full.SJ_rho\\\\n    value: 0.4314\\\\n  note: 'Qwen SciERC: 0.412 (3-seed mean) - 0.360 = +0.052. LLaMA CoNLL: 0.463 (3-seed)\\\\n    - 0.431 = +0.032'\\\\n- id: c036_sj_ece_calibration\\\\n  text: '[DEPRECATED] SJ achieves lowest calibration error (ECE=0.075-0.102 across\\\\n    settings)'\\\\n  sections: []\\\\n  tier: X\\\\n  evidence: []\\\\n  note: DEPRECATED — reversed by c016_ece_miscalibration. Old ECE values (0.075-0.102)\\\\n    were from exp_015 (max_tokens=512 truncation artifact). Corrected data shows all\\\\n    signals ECE 0.27-0.77.\\\\n- id: C001\\\\n  location:\\\\n    section: abstract\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: No signal significantly improves sample selection over greedy decoding despite\\\\n    13-18pp oracle headroom\\\\n  type: empirical\\\\n  evidence:\\\\n  - exp_012_rerun_1024\\\\n  decisions:\\\\n  - D070\\\\n  - D071\\\\n  deprecated: false\\\\n- id: C003\\\\n  location:\\\\n    section: abstract\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: LP scores compressed into effective ties for 60% of instances under constrained\\\\n    decoding\\\\n  type: empirical\\\\n  evidence:\\\\n  - exp_012_rerun_1024\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C006\\\\n  location:\\\\n    section: abstract\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: Where LP compression is absent, selection recovers +2.9pp (p=0.01)\\\\n  type: empirical\\\\n  evidence:\\\\n  - exp_012_rerun_1024\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C010\\\\n  location:\\\\n    section: abstract\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: Constrained-decoding score compression is the primary bottleneck\\\\n  type: empirical\\\\n  evidence:\\\\n  - exp_012_rerun_1024\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C011\\\\n  location:\\\\n    section: discussion\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: LP carries useful per-sample quality information; score compression is the\\\\n    primary bottleneck\\\\n  type: empirical\\\\n  evidence:\\\\n  - exp_012_rerun_1024\\\\n  decisions:\\\\n  - D071\\\\n  deprecated: false\\\\n- id: C013\\\\n  location:\\\\n    section: discussion\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: MBR utility correlates with F1 across instances but not within\\\\n  type: empirical\\\\n  evidence:\\\\n  - exp_012_rerun_1024\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C016\\\\n  location:\\\\n    section: discussion\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: Free-form ablation would test if bottleneck is decoding-regime-specific\\\\n  type: planned\\\\n  evidence: []\\\\n  decisions:\\\\n  - D071\\\\n  deprecated: false\\\\n- id: C017\\\\n  location:\\\\n    section: conclusion\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: Consistency signals effective QE (rho up to 0.38, AUROC up to 0.75) but fail\\\\n    at selection\\\\n  type: empirical\\\\n  evidence:\\\\n  - exp_012_rerun_1024\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C019\\\\n  location:\\\\n    section: conclusion\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: LP fails due to constrained-decoding score compression\\\\n  type: empirical\\\\n  evidence:\\\\n  - exp_012_rerun_1024\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C022\\\\n  location:\\\\n    section: conclusion\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: RE findings preliminary, single benchmark\\\\n  type: scope_limitation\\\\n  evidence:\\\\n  - exp_012_rerun_1024\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C023\\\\n  location:\\\\n    section: sections/discussion\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: Entity-token LP exhibits 4x higher within-instance variance than full-sequence\\\\n    LP on SciERC, but selection performs worse (-2.0pp)\\\\n  type: quantitative\\\\n  evidence:\\\\n  - exp_id: exp_entity_token_lp\\\\n    metric: scierc_entity_lp_variance_ratio\\\\n    value: 4.0x\\\\n  - exp_id: exp_entity_token_lp\\\\n    metric: scierc_entity_lp_selection_delta\\\\n    value: -1.68\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C024\\\\n  location:\\\\n    section: sections/discussion\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: On CoNLL, entity-token LP variance collapses to near-zero (median 2e-10) with\\\\n    79% tied\\\\n  type: quantitative\\\\n  evidence:\\\\n  - exp_id: exp_entity_token_lp\\\\n    metric: conll_entity_lp_variance_median\\\\n    value: 2e-10\\\\n  - exp_id: exp_entity_token_lp\\\\n    metric: conll_entity_lp_tied_fraction\\\\n    value: 0.794\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C025\\\\n  location:\\\\n    section: sections/discussion\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: Entity-token LP rules out format-token dilution as primary cause; points to\\\\n    intrinsic model overconfidence on entity tokens\\\\n  type: interpretive\\\\n  evidence:\\\\n  - exp_id: exp_entity_token_lp\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C026\\\\n  location:\\\\n    section: sections/limitations\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: Entity-token LP is the only tested remedy; LP×VC and calibration approaches\\\\n    are unexplored\\\\n  type: scope\\\\n  evidence:\\\\n  - exp_id: exp_entity_token_lp\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C027\\\\n  location:\\\\n    section: sections/introduction\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: 'C1 reframe: instance-level nature is setup, LP compression + MBR within-instance\\\\n    failure are the findings'\\\\n  type: structural\\\\n  evidence: []\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C028\\\\n  location:\\\\n    section: sections/introduction\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: 'SF4: 60% tied replaced with pooled within-instance ρ(LP,F1)=0.248 continuous\\\\n    characterization'\\\\n  type: structural\\\\n  evidence: []\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C029\\\\n  location:\\\\n    section: sections/introduction\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: 'C2 reframe: entity-token LP added as diagnostic ablation contribution'\\\\n  type: structural\\\\n  evidence:\\\\n  - exp_id: exp_entity_token_lp\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C030\\\\n  location:\\\\n    section: sections/abstract\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: 'SF3: RE removed from abstract; SF1: ρ=0.38 sourced to SciERC primary, up\\\\n    to 0.45 on ceiling control; MF2(a): benchmark roles explicit; M2: streamlined\\\\n    from 9 to 6 sentences'\\\\n  type: structural\\\\n  evidence: []\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C031\\\\n  location:\\\\n    section: sections/discussion\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: 21% of SciERC instances produce identical F1 across all N samples\\\\n  type: quantitative\\\\n  evidence: Q1 within-instance analysis\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C032\\\\n  location:\\\\n    section: sections/discussion\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: 58% of CoNLL instances produce identical F1 across all N samples\\\\n  type: quantitative\\\\n  evidence: Q1 within-instance analysis\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C033\\\\n  location:\\\\n    section: sections/discussion\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: 13% of SciERC instances yield constant utility scores\\\\n  type: quantitative\\\\n  evidence: Q1 within-instance analysis\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C034\\\\n  location:\\\\n    section: sections/discussion\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: 49% of CoNLL instances yield constant utility scores\\\\n  type: quantitative\\\\n  evidence: Q1 within-instance analysis\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C035\\\\n  location:\\\\n    section: sections/discussion\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: SJ median within-instance rho = 0.524 on SciERC\\\\n  type: quantitative\\\\n  evidence: Q1 within-instance analysis\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C036\\\\n  location:\\\\n    section: sections/discussion\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: SJ median within-instance rho = 0.994 on CoNLL\\\\n  type: quantitative\\\\n  evidence: Q1 within-instance analysis\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C037\\\\n  location:\\\\n    section: sections/discussion\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: MBR closes 23% of oracle gap on non-degenerate SciERC instances\\\\n  type: quantitative\\\\n  evidence: Q1 within-instance analysis\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C038\\\\n  location:\\\\n    section: sections/discussion\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: MBR closes 41% of oracle gap on non-degenerate CoNLL instances\\\\n  type: quantitative\\\\n  evidence: Q1 within-instance analysis\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C039\\\\n  location:\\\\n    section: sections/discussion\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: Greedy T=0 achieves F1=0.663 on SciERC, surpassing all N=8 selection strategies\\\\n  type: quantitative\\\\n  evidence: SF4 greedy data\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C040\\\\n  location:\\\\n    section: sections/discussion\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: SciERC 3-epoch rho=0.32 vs 5-epoch rho=0.28; LP delta -1.18 vs +0.62 pp\\\\n  type: quantitative\\\\n  evidence: tab:epoch_scierc\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C041\\\\n  location:\\\\n    section: sections/discussion\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: Entity-level majority voting yields +0.76pp on SciERC (5.8% gap recovery)\\\\n  type: quantitative\\\\n  evidence: []\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C042\\\\n  location:\\\\n    section: sections/discussion\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: Entity-level majority voting yields -0.64pp on CoNLL\\\\n  type: quantitative\\\\n  evidence: []\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C043\\\\n  location:\\\\n    section: sections/discussion\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: Entity-level majority voting yields -3.21pp on Few-NERD\\\\n  type: quantitative\\\\n  evidence: []\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C044\\\\n  location:\\\\n    section: sections/discussion\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: On degenerate subsets, merge is uniformly negative across all three datasets\\\\n  type: quantitative\\\\n  evidence: []\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C045\\\\n  location:\\\\n    section: sections/appendix\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: Exact permutation p=0.005 for per-type degeneracy-headroom correlation\\\\n  type: quantitative\\\\n  evidence: []\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C046\\\\n  location:\\\\n    section: sections/appendix\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: Under conservative df=4 adjustment, p=0.033\\\\n  type: quantitative\\\\n  evidence: []\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C047\\\\n  location:\\\\n    section: sections/appendix\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: 3-epoch SciERC mean within-instance rho=0.273\\\\n  type: quantitative\\\\n  evidence: []\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C048\\\\n  location:\\\\n    section: sections/appendix\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: 5-epoch SciERC mean within-instance rho=0.179\\\\n  type: quantitative\\\\n  evidence: []\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C049\\\\n  location:\\\\n    section: sections/appendix\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: 76.4% of instances show positive LP-quality correlation at 3 epochs\\\\n  type: quantitative\\\\n  evidence: []\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C050\\\\n  location:\\\\n    section: sections/appendix\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: 64.1% of instances show positive LP-quality correlation at 5 epochs\\\\n  type: quantitative\\\\n  evidence: []\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C051\\\\n  location:\\\\n    section: sections/appendix\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: Epoch-to-epoch alignment variation is 0.057 median rho, small vs cross-dataset\\\\n    gap\\\\n  type: quantitative\\\\n  evidence: []\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C052\\\\n  location:\\\\n    section: sections/appendix\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: 'Optimal DALS tau spans 2 orders of magnitude: FN 0.001, SciERC 0.05, CoNLL\\\\n    0.10'\\\\n  type: quantitative\\\\n  evidence: []\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C053\\\\n  location:\\\\n    section: sections/appendix\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: LOO regret ranges from 0.51 to 1.21pp\\\\n  type: quantitative\\\\n  evidence: []\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C054\\\\n  location:\\\\n    section: sections/appendix\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: Even with oracle tau, CoNLL remains at -0.31pp\\\\n  type: quantitative\\\\n  evidence: []\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C055\\\\n  location:\\\\n    section: sections/appendix\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: 'SciERC entity merge best k=3: +1.57pp, 11.9% recovery'\\\\n  type: quantitative\\\\n  evidence: []\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C056\\\\n  location:\\\\n    section: sections/appendix\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: 'CoNLL entity merge best k=3: -0.38pp, -9.0% recovery'\\\\n  type: quantitative\\\\n  evidence: []\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C057\\\\n  location:\\\\n    section: sections/appendix\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: 'FewNERD entity merge best k=2: -0.43pp, -3.6% recovery'\\\\n  type: quantitative\\\\n  evidence: []\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C058\\\\n  location:\\\\n    section: sections/experiments\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: 'Conditional decomp SciERC favorable: +2.47pp CI [+0.30, +4.70]'\\\\n  type: quantitative\\\\n  evidence: []\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C059\\\\n  location:\\\\n    section: sections/experiments\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: 'Conditional decomp FewNERD favorable: +0.63pp CI [-0.02, +1.30], marginal'\\\\n  type: quantitative\\\\n  evidence: []\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C060\\\\n  location:\\\\n    section: sections/experiments\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: 'Conditional decomp CoNLL favorable: -1.78pp CI [-2.83, -0.76], negative'\\\\n  type: quantitative\\\\n  evidence: []\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C061\\\\n  location:\\\\n    section: sections/appendix\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: Entity-token LP has 4x higher within-instance variance (0.000644 vs 0.000161)\\\\n  type: quantitative\\\\n  evidence: []\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C062\\\\n  location:\\\\n    section: sections/appendix\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: Entity-token LP rho=0.440 vs full-sequence 0.297\\\\n  type: quantitative\\\\n  evidence: []\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C063\\\\n  location:\\\\n    section: sections/appendix\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: Entity-token LP selection -0.73pp vs full-sequence +0.35pp\\\\n  type: quantitative\\\\n  evidence: []\\\\n  decisions: []\\\\n  deprecated: false\\\\ntables:\\\\n- id: tab:notation\\\\n  section: method\\\\n  caption: Notation used throughout the paper\\\\n  evidence: []\\\\n  note: Notation table—no experimental data.\\\\n- id: tab:quality_estimation\\\\n  section: experiments\\\\n  caption: Quality estimation across tasks and models (Spearman ρ and AUROC)\\\\n  evidence:\\\\n  - exp_id: exp_012_rerun_1024\\\\n    role: SciERC NER ρ values (N=8, Qwen) — corrected from exp_015 (truncation artifact)\\\\n  - exp_id: exp_015_metrics_expansion\\\\n    role: SciERC RE ρ values (N=8, Qwen) — RE values unaffected by truncation fix\\\\n  - exp_id: exp_015_v2\\\\n    role: AUROC values across settings\\\\n  - exp_id: exp_002\\\\n    role: CoNLL Qwen N=8 ρ and AUROC\\\\n  - exp_id: exp_017_llama_conll_infer\\\\n    role: CoNLL LLaMA N=8 ρ and AUROC\\\\n  - exp_id: exp_017_llama_conll_n16\\\\n    role: LLaMA CoNLL N=16 3-seed (seed=42)\\\\n  - exp_id: exp_017_llama_conll_n16_s123\\\\n    role: LLaMA CoNLL N=16 3-seed (seed=123)\\\\n  - exp_id: exp_017_llama_conll_n16_s456\\\\n    role: LLaMA CoNLL N=16 3-seed (seed=456)\\\\n- id: tab:selection\\\\n  section: experiments\\\\n  caption: Best-of-N selection F1 on SciERC (N=8, T=1.0)\\\\n  evidence:\\\\n  - exp_id: exp_016_signal_ensemble\\\\n    role: All selection F1 values (NER and RE)\\\\n- id: tab:robustness\\\\n  section: experiments\\\\n  caption: Signal robustness across configurations (Spearman ρ)\\\\n  evidence:\\\\n  - exp_id: exp_005\\\\n    role: Temperature block (T=0.7 vs T=1.0, Qwen SciERC)\\\\n  - exp_id: exp_015_metrics_expansion\\\\n    role: N=8 baseline values\\\\n  - exp_id: exp_001_seed42_v2\\\\n    role: N=16 SJ ρ seed=42\\\\n  - exp_id: exp_001_seed123_v2\\\\n    role: N=16 SJ ρ seed=123\\\\n  - exp_id: exp_001_seed456_v2_ner\\\\n    role: N=16 SJ ρ seed=456\\\\n  - exp_id: exp_017_llama_conll_n16\\\\n    role: 'Cross-model block: LLaMA CoNLL N=16 seed=42'\\\\n  - exp_id: exp_017_llama_conll_n16_s123\\\\n    role: 'Cross-model block: LLaMA CoNLL N=16 seed=123'\\\\n  - exp_id: exp_017_llama_conll_n16_s456\\\\n    role: 'Cross-model block: LLaMA CoNLL N=16 seed=456'\\\\nfigures:\\\\n- id: fig:overview\\\\n  section: introduction\\\\n  caption: The correlation-selection gap conceptual diagram\\\\n  evidence:\\\\n  - exp_id: exp_015_metrics_expansion\\\\n    role: Quality estimation data (ρ, AUROC for left panel)\\\\n  - exp_id: exp_016_signal_ensemble\\\\n    role: Selection F1 data (right panel)\\\\n- id: fig:signal_heatmap\\\\n  section: experiments\\\\n  caption: Quality estimation heatmap (Spearman ρ) across five signals and four configurations\\\\n  evidence:\\\\n  - exp_id: exp_015_metrics_expansion\\\\n    role: Full set ρ values for SciERC NER/RE (Qwen, N=8)\\\\n  - exp_id: exp_002\\\\n    role: CoNLL Qwen full set ρ values\\\\n  - exp_id: exp_001_ner_n16_scierc\\\\n    role: Conditional set ρ values\\\\n- id: fig:selection_gap\\\\n  section: experiments\\\\n  caption: The correlation-selection gap on SciERC (N=8)\\\\n  evidence:\\\\n  - exp_id: exp_016_signal_ensemble\\\\n    role: Best-of-N selection F1 bars and quality estimation ρ line\\\\n- id: fig:temperature_robustness\\\\n  section: experiments\\\\n  caption: Temperature robustness on SciERC (N=8)\\\\n  evidence:\\\\n  - exp_id: exp_005\\\\n    role: SJ, FK ρ values at T=0.7 and T=1.0\\\\n- id: fig:reliability\\\\n  section: experiments\\\\n  caption: Reliability diagrams on SciERC (N=8, T=1.0)\\\\n  evidence:\\\\n  - exp_id: exp_015_metrics_expansion\\\\n    role: Calibration/ECE data for all signals\\\\n  - exp_id: exp_002\\\\n    role: ECE values across signals\\\\n_completeness:\\\\n  coverage: 59/92\\\\n  claims: 87\\\\n  tables: 4\\\\n  figures: 5\\\\n  tier_counts:\\\\n    tier1: 0\\\\n    tier2: 59\\\\n    tier3: 33\\\\n    tierX: 0\\\\n  last_checked: '2026-05-18T15:39:48.035668+00:00'\\\\n\\\", \\\"total_chars\\\": 32730, \\\"truncated\\\": false}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/paper_provenance.yaml\", \"content\": \"paper:\\n  title: 'Strong Predictors, Weak Selectors: A Systematic Comparison of Confidence\\n    Signals for Test-Time Scaling in Information Extraction'\\n  version: 169\\n  generated_at: '2026-05-18T15:39:48.035618+00:00'\\n  source: manual provenance build by Paper Agent\\nclaims:\\n- id: c001_voting_rho_scierc_ner\\n  text: Voting Confidence achieves ρ=0.379 on SciERC NER (corrected from 0.502 truncation\\n    artifact)\\n  sections:\\n  - abstract\\n  - introduction\\n  - experiments\\n  - conclusion\\n  - discussion\\n  - related_work\\n  tier: 1\\n  evidence:\\n  - exp_id: exp_012_rerun_1024\\n    metric: ner.voting_rho_full\\n    value: 0.379\\n  note: Old value 0.502 from exp_015 was inflated by max_tokens=512 truncation. Corrected\\n    via exp_012_rerun_1024 (max_tokens=1024).\\n- id: c002_auroc_dissociation_scierc\\n  text: ρ-AUROC dissociation on SciERC — EM leads AUROC (NER 0.749, RE 0.706) while\\n    Voting leads ρ (NER 0.379, RE 0.422)\\n  sections:\\n  - abstract\\n  - introduction\\n  - experiments\\n  - conclusion\\n  - discussion\\n  tier: 1\\n  evidence:\\n  - exp_id: exp_012_rerun_1024\\n    metric: ner.em_auroc\\n    value: 0.749\\n  - exp_id: exp_012_rerun_1024\\n    metric: re.em_auroc\\n    value: 0.706\\n  - exp_id: exp_012_rerun_1024\\n    metric: ner.voting_auroc\\n    value: 0.684\\n  note: Old Table 1 had Voting NER AUROC=.741 (from exp_015 truncated). Corrected\\n    to .684 via exp_012_rerun_1024. EM now leads AUROC on both NER and RE. Headline\\n    claim changed from \\\"entity voting achieves ρ=0.38 and AUROC=0.74\\\" to split ρ (Voting\\n    0.38) / AUROC (EM 0.75) claim.\\n- id: c003_sj_rho_scierc_ner\\n  text: SJ achieves ρ=0.360 on SciERC NER (corrected from 0.357)\\n  sections:\\n  - experiments\\n  tier: 1\\n  evidence:\\n  - exp_id: exp_012_rerun_1024\\n    metric: ner.sj_rho_full\\n    value: 0.36\\n  - exp_id: exp_004_re_diagnostic\\n    metric: bootstrap_ci_95.ner_sj\\n    value:\\n    - 0.2946\\n    - 0.4586\\n- id: c004_voting_leads_re\\n  text: Voting leads RE full set (ρ=0.350, corrected from 0.422)\\n  sections:\\n  - experiments\\n  tier: 1\\n  evidence:\\n  - exp_id: exp_012_rerun_1024\\n    metric: re.voting_rho_full\\n    value: 0.35\\n  note: Corrected from exp_015_metrics_expansion (0.4217) via exp_012_rerun_1024.\\n- id: c005_fk_beats_sj_re\\n  text: FK (ρ=0.275) exceeds SJ (ρ=0.250) on RE—a reversal from NER\\n  sections:\\n  - experiments\\n  tier: 1\\n  evidence:\\n  - exp_id: exp_012_rerun_1024\\n    metric: re.fk_rho_full\\n    value: 0.275\\n  - exp_id: exp_012_rerun_1024\\n    metric: re.sj_rho_full\\n    value: 0.25\\n  note: Corrected from exp_015 (FK 0.253, SJ 0.211) via exp_012_rerun_1024.\\n- id: c006_re_40pct_zero_f1\\n  text: 40% of RE instances receive zero F1 (N=8, seed=42; 159/397)\\n  sections:\\n  - experiments\\n  - discussion\\n  tier: 1\\n  evidence:\\n  - exp_id: mvp_pilot_004\\n    metric: re_sample_f1_pct_zero\\n    value: 44.3\\n    note: 44.3% from mvp_pilot_004; paper uses 40% from primary config (N=8, seed=42)\\n  - exp_id: exp_008_re_n16_v2\\n    metric: f1_zero_pct\\n    value: 44.3\\n    note: 44.3% at N=16; zero-F1 fraction varies with N and seed\\n- id: c007_em_leads_conll\\n  text: EM leads CoNLL with ρ=0.451 and AUROC=0.816\\n  sections:\\n  - experiments\\n  tier: 1\\n  evidence:\\n  - exp_id: exp_002\\n    metric: em_rho_full\\n    value: 0.4507\\n  - exp_id: exp_002\\n    metric: em_auroc_full\\n    value: 0.8156\\n  - exp_id: exp_015_v2\\n    metric: auroc_best.EM.conll_ner\\n    value: 0.8156\\n- id: c008_cross_model_sj_stability\\n  text: 'SJ cross-model gap: ρ=0.436 (Qwen) vs 0.431 (LLaMA), Δ=0.005'\\n  sections:\\n  - experiments\\n  tier: 1\\n  evidence:\\n  - exp_id: exp_002\\n    metric: sj_rho_full\\n    value: 0.4357\\n  - exp_id: exp_017_llama_conll_infer\\n    metric: full.SJ_rho\\n    value: 0.4314\\n- id: c009_logprob_paradox\\n  text: Logprob achieves highest AUROC (0.761) yet lowest ρ (0.307) on CoNLL LLaMA\\n  sections:\\n  - experiments\\n  - discussion\\n  tier: 1\\n  evidence:\\n  - exp_id: exp_017_llama_conll_infer\\n    metric: full.logprob_AUROC\\n    value: 0.761\\n  - exp_id: exp_017_llama_conll_infer\\n    metric: full.logprob_rho\\n    value: 0.3072\\n- id: c010_conll_oracle_headroom\\n  text: 'CoNLL oracle headroom: +4.2pp (Qwen), +1.8pp (LLaMA)'\\n  sections:\\n  - experiments\\n  tier: 1\\n  evidence:\\n  - exp_id: exp_002\\n    metric: oracle_headroom\\n    value: 0.042\\n  - exp_id: exp_017_llama_conll_infer\\n    metric: oracle_headroom\\n    value: 0.0177\\n- id: c011_ner_no_reliable_selection\\n  text: No signal reliably surpasses greedy on NER (logprob +0.6pp, p=0.39, 3-seed\\n    bootstrap)\\n  sections:\\n  - abstract\\n  - introduction\\n  - experiments\\n  - conclusion\\n  - discussion\\n  - related_work\\n  tier: 1\\n  evidence:\\n  - exp_id: exp_016_rerun_1024_bootstrap\\n    metric: selection_f1_ner\\n    value:\\n      greedy: 0.644\\n      logprob: 0.65\\n      sj: 0.645\\n      voting: 0.634\\n      random: 0.608\\n      oracle: 0.776\\n  - exp_id: exp_016_rerun_1024_bootstrap\\n    metric: bootstrap_selection_test\\n    value:\\n      logprob_vs_greedy_p: 0.39\\n      ci_95:\\n      - -0.03\\n      - 0.042\\n      cohens_d: 0.038\\n      sign_test: 61W/70L\\n  note: 3-seed bootstrap confirms +0.6pp is NOT statistically significant. Unified\\n    with c012 — no signal reliably helps on either task.\\n- id: c012_re_no_signal_beats_greedy\\n  text: No signal surpasses greedy on RE; logprob drops to −0.9pp\\n  sections:\\n  - abstract\\n  - introduction\\n  - experiments\\n  - conclusion\\n  - discussion\\n  tier: 1\\n  evidence:\\n  - exp_id: exp_016_rerun_1024_bootstrap\\n    metric: selection_f1_re\\n    value:\\n      greedy: 0.404\\n      logprob: 0.395\\n      sj: 0.386\\n      voting: 0.359\\n      random: 0.354\\n      oracle: 0.585\\n  note: CLAIM REVERSED from exp_016 (max_tokens=512). Old claim was \\\"only logprob\\n    helps on RE (+2.3pp)\\\". Corrected via exp_016_rerun_1024_bootstrap.\\n- id: c013_oracle_headroom_ner\\n  text: Oracle upper bound 0.776, 13.2pp above greedy 0.644 on NER\\n  sections:\\n  - experiments\\n  - discussion\\n  tier: 1\\n  evidence:\\n  - exp_id: exp_016_rerun_1024_bootstrap\\n    metric: selection_f1_ner.oracle\\n    value: 0.776\\n  - exp_id: exp_016_rerun_1024_bootstrap\\n    metric: selection_f1_ner.greedy\\n    value: 0.644\\n- id: c014_re_oracle_headroom\\n  text: 'RE oracle gap: 18.1pp (0.585 vs 0.404)'\\n  sections:\\n  - experiments\\n  - discussion\\n  tier: 1\\n  evidence:\\n  - exp_id: exp_016_rerun_1024_bootstrap\\n    metric: selection_f1_re.oracle\\n    value: 0.585\\n  - exp_id: exp_016_rerun_1024_bootstrap\\n    metric: selection_f1_re.greedy\\n    value: 0.404\\n- id: c015_ensemble_auroc\\n  text: SJ+Voting ensemble AUROC=0.666, below best individual signal EM (0.749)\\n  sections:\\n  - discussion\\n  tier: 1\\n  evidence:\\n  - exp_id: exp_016_rerun_1024_bootstrap\\n    metric: ensemble_ner_auroc\\n    value: 0.666\\n  note: Ensemble does NOT improve over best individual. Changed from positive to negative\\n    finding.\\n- id: c016_ece_calibration\\n  text: NER reasonably well-calibrated (calibration ECE 0.069-0.096), RE shows greater\\n    miscalibration (ECE 0.109-0.339)\\n  sections:\\n  - experiments\\n  tier: 1\\n  evidence:\\n  - exp_id: exp_016_rerun_1024_bootstrap\\n    metric: calibration_ece\\n    value:\\n      ner_range: 0.069-0.096\\n      re_range: 0.109-0.339\\n  note: Previous c016 used binary ECE (0.27-0.77) which was incorrect metric. Calibration\\n    ECE (signal confidence → mean F1 deviation) shows NER is well-calibrated, RE has\\n    moderate miscalibration. Consistent with fig_reliability_1024.\\n- id: c017_fisher_z_ner_vs_re\\n  text: 'Fisher''s z-test ρ_SJ NER vs RE: z=2.31, p=0.021'\\n  sections:\\n  - experiments\\n  tier: 1\\n  evidence:\\n  - exp_id: exp_004_re_diagnostic\\n    metric: fisher_z_ner_vs_re.sj_z\\n    value: 2.31\\n  - exp_id: exp_004_re_diagnostic\\n    metric: fisher_z_ner_vs_re.sj_p\\n    value: 0.0209\\n- id: c018_per_relation_diagnostic\\n  text: Feature-Of ρ≈0.004, Hyponym-Of ρ=0.646\\n  sections:\\n  - experiments\\n  tier: 1\\n  evidence:\\n  - exp_id: exp_004_re_diagnostic\\n    metric: per_relation_type.FEATURE-OF.rho_sj\\n    value: 0.004\\n  - exp_id: exp_004_re_diagnostic\\n    metric: per_relation_type.HYPONYM-OF.rho_fk\\n    value: 0.646\\n- id: c019_entity_span_errors\\n  text: Entity span errors account for 55.5% of RE false negatives\\n  sections:\\n  - experiments\\n  tier: 1\\n  evidence:\\n  - exp_id: exp_004_re_diagnostic\\n    metric: error_propagation\\n    value: head_error 17.7% + tail_error (derived) + head_tail_error 15.9% + full_error\\n      21.7% → entity span errors ~55.5%\\n  note: Computed from error_propagation breakdown in exp_004\\n- id: c020_capability_stratification_ner\\n  text: SJ ρ=0.547 on SciERC instances with 6+ entities, vs 0.415 for 1-2 entities\\n  sections:\\n  - experiments\\n  tier: 1\\n  evidence:\\n  - exp_id: exp_009_capability_stratification\\n    metric: scierc_ner.by_ent_count.6plus_sj_rho\\n    value: 0.547\\n  - exp_id: exp_009_capability_stratification\\n    metric: scierc_ner.by_ent_count.1_2_sj_rho\\n    value: 0.415\\n- id: c021_wnut_boundary\\n  text: 'WNUT-17: SJ ρ=0.089 (p=0.020), 54% zero F1'\\n  sections:\\n  - experiments\\n  - conclusion\\n  tier: 1\\n  evidence:\\n  - exp_id: exp_003_wnut17_eval\\n    metric: rho_sj\\n    value: 0.089\\n  - exp_id: exp_003_wnut17_eval\\n    metric: sample_f1_pct_zero\\n    value: 53.7\\n  note: 'Corrected 2026-05-16: paper uses ρ=0.089 from exp003_wnut17_eval (gold-filtered\\n    n=689, p=0.020). Old value 0.062 was untraceable — only in deprecated draft.'\\n- id: c022_wnut_logprob_negative\\n  text: WNUT logprob shows strong negative correlation\\n  sections:\\n  - experiments\\n  tier: 1\\n  evidence:\\n  - exp_id: exp_003_ner_wnut17\\n    metric: ner.rho_logprob_full\\n    value: -0.414\\n  - exp_id: exp_003_wnut17_eval\\n    metric: rho_logprob_full\\n    value: -0.409\\n- id: c023_re_sent_length_sj\\n  text: 'RE SJ ρ increases with sentence length: Q1 0.110 → Q4 0.473 (Fisher p=0.004)'\\n  sections:\\n  - experiments\\n  tier: 2\\n  evidence:\\n  - exp_id: exp_009_v2_re_rerun\\n    metric: by_sent_len_quartiles\\n    value:\\n      Q1_sj_rho: 0.11\\n      Q4_sj_rho: 0.473\\n      fisher_z_p: 0.004\\n  note: 'Corrected 2026-05-16: source is exp_009_v2_re_rerun (gold-filtered n=397).\\n    Old registry exp_009 values (Q1=0.447, Q4=0.540) used unfiltered n=551.'\\n- id: c024_high_complexity_re_subset\\n  text: 'High-complexity RE subset (n=81): Voting ρ=0.630, logprob ρ=0.554, SJ ρ=0.502'\\n  sections:\\n  - experiments\\n  tier: 2\\n  evidence:\\n  - exp_id: exp_009_capability_stratification\\n    metric: scierc_re.by_rel_count\\n    value:\\n      6plus_sj_rho: 0.527\\n  note: Registry has 6plus_sj_rho=0.527; paper may use exp_009_v2 data. Voting and\\n    logprob values not in registry summary.\\n- id: c025_temperature_sj_stable\\n  text: SJ NER ρ shifts from 0.388 (T=0.7) to 0.360 (T=1.0), Δ=0.028\\n  sections:\\n  - experiments\\n  tier: 1\\n  evidence:\\n  - exp_id: exp_005\\n    metric: sj_rho_t07_ner\\n    value: 0.388\\n  - exp_id: exp_012_rerun_1024\\n    metric: ner.sj_rho_full\\n    value: 0.36\\n  note: T=0.7 data from exp_005; T=1.0 from exp_015\\n- id: c026_n_scaling_sj\\n  text: SJ N=8→N=16 improves ρ from 0.360 to 0.412±0.025 (3-seed, +0.052) on Qwen\\n    SciERC NER\\n  sections:\\n  - experiments\\n  tier: 1\\n  evidence:\\n  - exp_id: exp_012_rerun_1024\\n    metric: ner.sj_rho_full\\n    value: 0.36\\n  - exp_id: exp_001_seed42_v2\\n    metric: sj_rho_full\\n    value: 0.428\\n  - exp_id: exp_001_seed123_v2\\n    metric: sj_rho_full\\n    value: 0.424\\n  - exp_id: exp_001_seed456_v2_ner\\n    metric: full.SJ.rho\\n    value: 0.384\\n  note: '3-seed mean: (0.428+0.424+0.384)/3 ≈ 0.412, σ=0.025'\\n- id: c027_llama_conll_3seed\\n  text: 'LLaMA CoNLL N=16 3-seed: SJ ρ=0.463±0.007, logprob ρ=0.310±0.005'\\n  sections:\\n  - experiments\\n  tier: 1\\n  evidence:\\n  - exp_id: exp_017_llama_conll_n16\\n    metric: full.SJ_rho\\n    value: 0.4642\\n  - exp_id: exp_017_llama_conll_n16_s123\\n    metric: full.SJ_rho\\n    value: 0.4698\\n  - exp_id: exp_017_llama_conll_n16_s456\\n    metric: full.SJ_rho\\n    value: 0.4552\\n  - exp_id: exp_017_llama_conll_n16\\n    metric: full.logprob_rho\\n    value: 0.3058\\n  - exp_id: exp_017_llama_conll_n16_s123\\n    metric: full.logprob_rho\\n    value: 0.3161\\n  - exp_id: exp_017_llama_conll_n16_s456\\n    metric: full.logprob_rho\\n    value: 0.3078\\n- id: c028_loo_sj_circularity\\n  text: LOO-SJ Δρ=-0.014, max per-instance Δρ=3.1×10⁻⁴—circularity negligible\\n  sections:\\n  - experiments\\n  tier: 1\\n  evidence:\\n  - exp_id: exp_015_v2\\n    metric: loo_sj.max_delta_rho\\n    value: 0.000305\\n  - exp_id: exp_015_v2\\n    metric: loo_sj.all_no_circularity\\n    value: true\\n- id: c029_llama_scierc_cross_model\\n  text: 'LLaMA replicates structural-over-surface on SciERC: NER SJ ρ=0.363 > FK ρ=0.327;\\n    conditional RE SJ ρ=0.405 > FK ρ=0.259'\\n  sections:\\n  - experiments\\n  tier: 1\\n  evidence:\\n  - exp_id: exp_007_llama_inference\\n    metric: ner.rho_sj\\n    value: 0.363\\n  - exp_id: exp_007_llama_inference\\n    metric: ner.rho_fk\\n    value: 0.327\\n  - exp_id: exp_007_llama_inference\\n    metric: re.sj_rho_cond\\n    value: 0.405\\n  - exp_id: exp_007_llama_inference\\n    metric: re.fk_rho_cond\\n    value: 0.259\\n- id: c030_em_conditional_dominance\\n  text: 'EM ranks #1 on conditional set across all 4 configurations'\\n  sections:\\n  - experiments\\n  tier: 1\\n  evidence:\\n  - exp_id: exp_015_metrics_expansion\\n    metric: ner.em_rho_cond\\n    value: 0.3427\\n  - exp_id: exp_015_metrics_expansion\\n    metric: re.em_rho_cond\\n    value: 0.3607\\n  - exp_id: exp_002_conll_n16\\n    metric: conditional.EM_rho\\n    value: 0.4658\\n  - exp_id: exp_017_llama_conll_n16_s123\\n    metric: conditional.EM_rho\\n    value: 0.4732\\n  note: 'Paper cites EM conditional: SciERC NER 0.408, RE 0.485, CoNLL Qwen N=16 0.466,\\n    CoNLL LLaMA 3-seed 0.462. Registry has slightly different values from different\\n    seed/N combinations.'\\n- id: c031_em_conditional_scierc\\n  text: 'EM conditional: NER ρ=0.408, RE ρ=0.485'\\n  sections:\\n  - experiments\\n  tier: 1\\n  evidence:\\n  - exp_id: exp_001_ner_n16_scierc\\n    metric: ner_cond_em_rho\\n    value: 0.414\\n  - exp_id: exp_001_ner_n16_scierc\\n    metric: re_cond_em_rho\\n    value: 0.475\\n  note: 'Paper rounds: 0.414→0.408, 0.475→0.485. May use different seed/N baseline.'\\n- id: c032_logprob_re_cond_collapse\\n  text: Logprob conditional RE collapses to ρ=0.011\\n  sections:\\n  - experiments\\n  tier: 1\\n  evidence:\\n  - exp_id: exp_012_rerun_1024\\n    metric: re_cond.logprob.rho\\n    value: 0.0112\\n  note: 'Corrected 2026-05-16: source is exp_012_rerun_1024 (greedy_f1>0 filter, n=238).\\n    Old exp_015 value 0.1457 used wrong filter (any sample F1>0, n=331). Old text\\n    0.002 was stale and untraceable.'\\n- id: c033_sj_n16_cond_re\\n  text: At N=16, SJ maintains ρ=0.308 on conditional RE while logprob drops to -0.026\\n  sections:\\n  - experiments\\n  - discussion\\n  tier: 1\\n  evidence:\\n  - exp_id: exp_008_re_n16_v2\\n    metric: sj_rho_cond\\n    value: 0.308\\n- id: c034_structural_over_logprob_n16\\n  text: Structural-over-logprob advantage holds across all 4 N=16 settings (Δ=+0.124\\n    to +0.175)\\n  sections:\\n  - experiments\\n  - discussion\\n  tier: 1\\n  evidence:\\n  - exp_id: exp_001_ner_n16_scierc\\n    metric: ner_voting_conf_rho\\n    value: 0.399\\n  - exp_id: exp_001_ner_n16_scierc\\n    metric: ner_logprob_rho\\n    value: 0.237\\n  - exp_id: exp_002_conll_n16\\n    metric: full.EM_rho\\n    value: 0.4627\\n  - exp_id: exp_002_conll_n16\\n    metric: full.logprob_rho\\n    value: 0.3146\\n  - exp_id: exp_007_llama_n16\\n    metric: full.voting_conf_rho\\n    value: 0.4515\\n  - exp_id: exp_007_llama_n16\\n    metric: full.logprob_rho\\n    value: 0.2041\\n  - exp_id: exp_017_llama_conll_n16\\n    metric: full.SJ_rho\\n    value: 0.4642\\n  - exp_id: exp_017_llama_conll_n16\\n    metric: full.logprob_rho\\n    value: 0.3058\\n- id: c035_n_scaling_diminishing\\n  text: 'SJ N-scaling gains are sublinear: +0.052 Qwen SciERC, +0.032 LLaMA CoNLL'\\n  sections:\\n  - discussion\\n  tier: 1\\n  evidence:\\n  - exp_id: exp_001_seed42_v2\\n    metric: sj_rho_full\\n    value: 0.428\\n  - exp_id: exp_015_metrics_expansion\\n    metric: ner.sj_rho_full\\n    value: 0.3565\\n  - exp_id: exp_017_llama_conll_n16\\n    metric: full.SJ_rho\\n    value: 0.4642\\n  - exp_id: exp_017_llama_conll_infer\\n    metric: full.SJ_rho\\n    value: 0.4314\\n  note: 'Qwen SciERC: 0.412 (3-seed mean) - 0.360 = +0.052. LLaMA CoNLL: 0.463 (3-seed)\\n    - 0.431 = +0.032'\\n- id: c036_sj_ece_calibration\\n  text: '[DEPRECATED] SJ achieves lowest calibration error (ECE=0.075-0.102 across\\n    settings)'\\n  sections: []\\n  tier: X\\n  evidence: []\\n  note: DEPRECATED — reversed by c016_ece_miscalibration. Old ECE values (0.075-0.102)\\n    were from exp_015 (max_tokens=512 truncation artifact). Corrected data shows all\\n    signals ECE 0.27-0.77.\\n- id: C001\\n  location:\\n    section: abstract\\n    paragraph: 0\\n    sentence: 0\\n  text: No signal significantly improves sample selection over greedy decoding despite\\n    13-18pp oracle headroom\\n  type: empirical\\n  evidence:\\n  - exp_012_rerun_1024\\n  decisions:\\n  - D070\\n  - D071\\n  deprecated: false\\n- id: C003\\n  location:\\n    section: abstract\\n    paragraph: 0\\n    sentence: 0\\n  text: LP scores compressed into effective ties for 60% of instances under constrained\\n    decoding\\n  type: empirical\\n  evidence:\\n  - exp_012_rerun_1024\\n  decisions: []\\n  deprecated: false\\n- id: C006\\n  location:\\n    section: abstract\\n    paragraph: 0\\n    sentence: 0\\n  text: Where LP compression is absent, selection recovers +2.9pp (p=0.01)\\n  type: empirical\\n  evidence:\\n  - exp_012_rerun_1024\\n  decisions: []\\n  deprecated: false\\n- id: C010\\n  location:\\n    section: abstract\\n    paragraph: 0\\n    sentence: 0\\n  text: Constrained-decoding score compression is the primary bottleneck\\n  type: empirical\\n  evidence:\\n  - exp_012_rerun_1024\\n  decisions: []\\n  deprecated: false\\n- id: C011\\n  location:\\n    section: discussion\\n    paragraph: 0\\n    sentence: 0\\n  text: LP carries useful per-sample quality information; score compression is the\\n    primary bottleneck\\n  type: empirical\\n  evidence:\\n  - exp_012_rerun_1024\\n  decisions:\\n  - D071\\n  deprecated: false\\n- id: C013\\n  location:\\n    section: discussion\\n    paragraph: 0\\n    sentence: 0\\n  text: MBR utility correlates with F1 across instances but not within\\n  type: empirical\\n  evidence:\\n  - exp_012_rerun_1024\\n  decisions: []\\n  deprecated: false\\n- id: C016\\n  location:\\n    section: discussion\\n    paragraph: 0\\n    sentence: 0\\n  text: Free-form ablation would test if bottleneck is decoding-regime-specific\\n  type: planned\\n  evidence: []\\n  decisions:\\n  - D071\\n  deprecated: false\\n- id: C017\\n  location:\\n    section: conclusion\\n    paragraph: 0\\n    sentence: 0\\n  text: Consistency signals effective QE (rho up to 0.38, AUROC up to 0.75) but fail\\n    at selection\\n  type: empirical\\n  evidence:\\n  - exp_012_rerun_1024\\n  decisions: []\\n  deprecated: false\\n- id: C019\\n  location:\\n    section: conclusion\\n    paragraph: 0\\n    sentence: 0\\n  text: LP fails due to constrained-decoding score compression\\n  type: empirical\\n  evidence:\\n  - exp_012_rerun_1024\\n  decisions: []\\n  deprecated: false\\n- id: C022\\n  location:\\n    section: conclusion\\n    paragraph: 0\\n    sentence: 0\\n  text: RE findings preliminary, single benchmark\\n  type: scope_limitation\\n  evidence:\\n  - exp_012_rerun_1024\\n  decisions: []\\n  deprecated: false\\n- id: C023\\n  location:\\n    section: sections/discussion\\n    paragraph: 0\\n    sentence: 0\\n  text: Entity-token LP exhibits 4x higher within-instance variance than full-sequence\\n    LP on SciERC, but selection performs worse (-2.0pp)\\n  type: quantitative\\n  evidence:\\n  - exp_id: exp_entity_token_lp\\n    metric: scierc_entity_lp_variance_ratio\\n    value: 4.0x\\n  - exp_id: exp_entity_token_lp\\n    metric: scierc_entity_lp_selection_delta\\n    value: -1.68\\n  decisions: []\\n  deprecated: false\\n- id: C024\\n  location:\\n    section: sections/discussion\\n    paragraph: 0\\n    sentence: 0\\n  text: On CoNLL, entity-token LP variance collapses to near-zero (median 2e-10) with\\n    79% tied\\n  type: quantitative\\n  evidence:\\n  - exp_id: exp_entity_token_lp\\n    metric: conll_entity_lp_variance_median\\n    value: 2e-10\\n  - exp_id: exp_entity_token_lp\\n    metric: conll_entity_lp_tied_fraction\\n    value: 0.794\\n  decisions: []\\n  deprecated: false\\n- id: C025\\n  location:\\n    section: sections/discussion\\n    paragraph: 0\\n    sentence: 0\\n  text: Entity-token LP rules out format-token dilution as primary cause; points to\\n    intrinsic model overconfidence on entity tokens\\n  type: interpretive\\n  evidence:\\n  - exp_id: exp_entity_token_lp\\n  decisions: []\\n  deprecated: false\\n- id: C026\\n  location:\\n    section: sections/limitations\\n    paragraph: 0\\n    sentence: 0\\n  text: Entity-token LP is the only tested remedy; LP×VC and calibration approaches\\n    are unexplored\\n  type: scope\\n  evidence:\\n  - exp_id: exp_entity_token_lp\\n  decisions: []\\n  deprecated: false\\n- id: C027\\n  location:\\n    section: sections/introduction\\n    paragraph: 0\\n    sentence: 0\\n  text: 'C1 reframe: instance-level nature is setup, LP compression + MBR within-instance\\n    failure are the findings'\\n  type: structural\\n  evidence: []\\n  decisions: []\\n  deprecated: false\\n- id: C028\\n  location:\\n    section: sections/introduction\\n    paragraph: 0\\n    sentence: 0\\n  text: 'SF4: 60% tied replaced with pooled within-instance ρ(LP,F1)=0.248 continuous\\n    characterization'\\n  type: structural\\n  evidence: []\\n  decisions: []\\n  deprecated: false\\n- id: C029\\n  location:\\n    section: sections/introduction\\n    paragraph: 0\\n    sentence: 0\\n  text: 'C2 reframe: entity-token LP added as diagnostic ablation contribution'\\n  type: structural\\n  evidence:\\n  - exp_id: exp_entity_token_lp\\n  decisions: []\\n  deprecated: false\\n- id: C030\\n  location:\\n    section: sections/abstract\\n    paragraph: 0\\n    sentence: 0\\n  text: 'SF3: RE removed from abstract; SF1: ρ=0.38 sourced to SciERC primary, up\\n    to 0.45 on ceiling control; MF2(a): benchmark roles explicit; M2: streamlined\\n    from 9 to 6 sentences'\\n  type: structural\\n  evidence: []\\n  decisions: []\\n  deprecated: false\\n- id: C031\\n  location:\\n    section: sections/discussion\\n    paragraph: 0\\n    sentence: 0\\n  text: 21% of SciERC instances produce identical F1 across all N samples\\n  type: quantitative\\n  evidence: Q1 within-instance analysis\\n  decisions: []\\n  deprecated: false\\n- id: C032\\n  location:\\n    section: sections/discussion\\n    paragraph: 0\\n    sentence: 0\\n  text: 58% of CoNLL instances produce identical F1 across all N samples\\n  type: quantitative\\n  evidence: Q1 within-instance analysis\\n  decisions: []\\n  deprecated: false\\n- id: C033\\n  location:\\n    section: sections/discussion\\n    paragraph: 0\\n    sentence: 0\\n  text: 13% of SciERC instances yield constant utility scores\\n  type: quantitative\\n  evidence: Q1 within-instance analysis\\n  decisions: []\\n  deprecated: false\\n- id: C034\\n  location:\\n    section: sections/discussion\\n    paragraph: 0\\n    sentence: 0\\n  text: 49% of CoNLL instances yield constant utility scores\\n  type: quantitative\\n  evidence: Q1 within-instance analysis\\n  decisions: []\\n  deprecated: false\\n- id: C035\\n  location:\\n    section: sections/discussion\\n    paragraph: 0\\n    sentence: 0\\n  text: SJ median within-instance rho = 0.524 on SciERC\\n  type: quantitative\\n  evidence: Q1 within-instance analysis\\n  decisions: []\\n  deprecated: false\\n- id: C036\\n  location:\\n    section: sections/discussion\\n    paragraph: 0\\n    sentence: 0\\n  text: SJ median within-instance rho = 0.994 on CoNLL\\n  type: quantitative\\n  evidence: Q1 within-instance analysis\\n  decisions: []\\n  deprecated: false\\n- id: C037\\n  location:\\n    section: sections/discussion\\n    paragraph: 0\\n    sentence: 0\\n  text: MBR closes 23% of oracle gap on non-degenerate SciERC instances\\n  type: quantitative\\n  evidence: Q1 within-instance analysis\\n  decisions: []\\n  deprecated: false\\n- id: C038\\n  location:\\n    section: sections/discussion\\n    paragraph: 0\\n    sentence: 0\\n  text: MBR closes 41% of oracle gap on non-degenerate CoNLL instances\\n  type: quantitative\\n  evidence: Q1 within-instance analysis\\n  decisions: []\\n  deprecated: false\\n- id: C039\\n  location:\\n    section: sections/discussion\\n    paragraph: 0\\n    sentence: 0\\n  text: Greedy T=0 achieves F1=0.663 on SciERC, surpassing all N=8 selection strategies\\n  type: quantitative\\n  evidence: SF4 greedy data\\n  decisions: []\\n  deprecated: false\\n- id: C040\\n  location:\\n    section: sections/discussion\\n    paragraph: 0\\n    sentence: 0\\n  text: SciERC 3-epoch rho=0.32 vs 5-epoch rho=0.28; LP delta -1.18 vs +0.62 pp\\n  type: quantitative\\n  evidence: tab:epoch_scierc\\n  decisions: []\\n  deprecated: false\\n- id: C041\\n  location:\\n    section: sections/discussion\\n    paragraph: 0\\n    sentence: 0\\n  text: Entity-level majority voting yields +0.76pp on SciERC (5.8% gap recovery)\\n  type: quantitative\\n  evidence: []\\n  decisions: []\\n  deprecated: false\\n- id: C042\\n  location:\\n    section: sections/discussion\\n    paragraph: 0\\n    sentence: 0\\n  text: Entity-level majority voting yields -0.64pp on CoNLL\\n  type: quantitative\\n  evidence: []\\n  decisions: []\\n  deprecated: false\\n- id: C043\\n  location:\\n    section: sections/discussion\\n    paragraph: 0\\n    sentence: 0\\n  text: Entity-level majority voting yields -3.21pp on Few-NERD\\n  type: quantitative\\n  evidence: []\\n  decisions: []\\n  deprecated: false\\n- id: C044\\n  location:\\n    section: sections/discussion\\n    paragraph: 0\\n    sentence: 0\\n  text: On degenerate subsets, merge is uniformly negative across all three datasets\\n  type: quantitative\\n  evidence: []\\n  decisions: []\\n  deprecated: false\\n- id: C045\\n  location:\\n    section: sections/appendix\\n    paragraph: 0\\n    sentence: 0\\n  text: Exact permutation p=0.005 for per-type degeneracy-headroom correlation\\n  type: quantitative\\n  evidence: []\\n  decisions: []\\n  deprecated: false\\n- id: C046\\n  location:\\n    section: sections/appendix\\n    paragraph: 0\\n    sentence: 0\\n  text: Under conservative df=4 adjustment, p=0.033\\n  type: quantitative\\n  evidence: []\\n  decisions: []\\n  deprecated: false\\n- id: C047\\n  location:\\n    section: sections/appendix\\n    paragraph: 0\\n    sentence: 0\\n  text: 3-epoch SciERC mean within-instance rho=0.273\\n  type: quantitative\\n  evidence: []\\n  decisions: []\\n  deprecated: false\\n- id: C048\\n  location:\\n    section: sections/appendix\\n    paragraph: 0\\n    sentence: 0\\n  text: 5-epoch SciERC mean within-instance rho=0.179\\n  type: quantitative\\n  evidence: []\\n  decisions: []\\n  deprecated: false\\n- id: C049\\n  location:\\n    section: sections/appendix\\n    paragraph: 0\\n    sentence: 0\\n  text: 76.4% of instances show positive LP-quality correlation at 3 epochs\\n  type: quantitative\\n  evidence: []\\n  decisions: []\\n  deprecated: false\\n- id: C050\\n  location:\\n    section: sections/appendix\\n    paragraph: 0\\n    sentence: 0\\n  text: 64.1% of instances show positive LP-quality correlation at 5 epochs\\n  type: quantitative\\n  evidence: []\\n  decisions: []\\n  deprecated: false\\n- id: C051\\n  location:\\n    section: sections/appendix\\n    paragraph: 0\\n    sentence: 0\\n  text: Epoch-to-epoch alignment variation is 0.057 median rho, small vs cross-dataset\\n    gap\\n  type: quantitative\\n  evidence: []\\n  decisions: []\\n  deprecated: false\\n- id: C052\\n  location:\\n    section: sections/appendix\\n    paragraph: 0\\n    sentence: 0\\n  text: 'Optimal DALS tau spans 2 orders of magnitude: FN 0.001, SciERC 0.05, CoNLL\\n    0.10'\\n  type: quantitative\\n  evidence: []\\n  decisions: []\\n  deprecated: false\\n- id: C053\\n  location:\\n    section: sections/appendix\\n    paragraph: 0\\n    sentence: 0\\n  text: LOO regret ranges from 0.51 to 1.21pp\\n  type: quantitative\\n  evidence: []\\n  decisions: []\\n  deprecated: false\\n- id: C054\\n  location:\\n    section: sections/appendix\\n    paragraph: 0\\n    sentence: 0\\n  text: Even with oracle tau, CoNLL remains at -0.31pp\\n  type: quantitative\\n  evidence: []\\n  decisions: []\\n  deprecated: false\\n- id: C055\\n  location:\\n    section: sections/appendix\\n    paragraph: 0\\n    sentence: 0\\n  text: 'SciERC entity merge best k=3: +1.57pp, 11.9% recovery'\\n  type: quantitative\\n  evidence: []\\n  decisions: []\\n  deprecated: false\\n- id: C056\\n  location:\\n    section: sections/appendix\\n    paragraph: 0\\n    sentence: 0\\n  text: 'CoNLL entity merge best k=3: -0.38pp, -9.0% recovery'\\n  type: quantitative\\n  evidence: []\\n  decisions: []\\n  deprecated: false\\n- id: C057\\n  location:\\n    section: sections/appendix\\n    paragraph: 0\\n    sentence: 0\\n  text: 'FewNERD entity merge best k=2: -0.43pp, -3.6% recovery'\\n  type: quantitative\\n  evidence: []\\n  decisions: []\\n  deprecated: false\\n- id: C058\\n  location:\\n    section: sections/experiments\\n    paragraph: 0\\n    sentence: 0\\n  text: 'Conditional decomp SciERC favorable: +2.47pp CI [+0.30, +4.70]'\\n  type: quantitative\\n  evidence: []\\n  decisions: []\\n  deprecated: false\\n- id: C059\\n  location:\\n    section: sections/experiments\\n    paragraph: 0\\n    sentence: 0\\n  text: 'Conditional decomp FewNERD favorable: +0.63pp CI [-0.02, +1.30], marginal'\\n  type: quantitative\\n  evidence: []\\n  decisions: []\\n  deprecated: false\\n- id: C060\\n  location:\\n    section: sections/experiments\\n    paragraph: 0\\n    sentence: 0\\n  text: 'Conditional decomp CoNLL favorable: -1.78pp CI [-2.83, -0.76], negative'\\n  type: quantitative\\n  evidence: []\\n  decisions: []\\n  deprecated: false\\n- id: C061\\n  location:\\n    section: sections/appendix\\n    paragraph: 0\\n    sentence: 0\\n  text: Entity-token LP has 4x higher within-instance variance (0.000644 vs 0.000161)\\n  type: quantitative\\n  evidence: []\\n  decisions: []\\n  deprecated: false\\n- id: C062\\n  location:\\n    section: sections/appendix\\n    paragraph: 0\\n    sentence: 0\\n  text: Entity-token LP rho=0.440 vs full-sequence 0.297\\n  type: quantitative\\n  evidence: []\\n  decisions: []\\n  deprecated: false\\n- id: C063\\n  location:\\n    section: sections/appendix\\n    paragraph: 0\\n    sentence: 0\\n  text: Entity-token LP selection -0.73pp vs full-sequence +0.35pp\\n  type: quantitative\\n  evidence: []\\n  decisions: []\\n  deprecated: false\\ntables:\\n- id: tab:notation\\n  section: method\\n  caption: Notation used throughout the paper\\n  evidence: []\\n  note: Notation table—no experimental data.\\n- id: tab:quality_estimation\\n  section: experiments\\n  caption: Quality estimation across tasks and models (Spearman ρ and AUROC)\\n  evidence:\\n  - exp_id: exp_012_rerun_1024\\n    role: SciERC NER ρ values (N=8, Qwen) — corrected from exp_015 (truncation artifact)\\n  - exp_id: exp_015_metrics_expansion\\n    role: SciERC RE ρ values (N=8, Qwen) — RE values unaffected by truncation fix\\n  - exp_id: exp_015_v2\\n    role: AUROC values across settings\\n  - exp_id: exp_002\\n    role: CoNLL Qwen N=8 ρ and AUROC\\n  - exp_id: exp_017_llama_conll_infer\\n    role: CoNLL LLaMA N=8 ρ and AUROC\\n  - exp_id: exp_017_llama_conll_n16\\n    role: LLaMA CoNLL N=16 3-seed (seed=42)\\n  - exp_id: exp_017_llama_conll_n16_s123\\n    role: LLaMA CoNLL N=16 3-seed (seed=123)\\n  - exp_id: exp_017_llama_conll_n16_s456\\n    role: LLaMA CoNLL N=16 3-seed (seed=456)\\n- id: tab:selection\\n  section: experiments\\n  caption: Best-of-N selection F1 on SciERC (N=8, T=1.0)\\n  evidence:\\n  - exp_id: exp_016_signal_ensemble\\n    role: All selection F1 values (NER and RE)\\n- id: tab:robustness\\n  section: experiments\\n  caption: Signal robustness across configurations (Spearman ρ)\\n  evidence:\\n  - exp_id: exp_005\\n    role: Temperature block (T=0.7 vs T=1.0, Qwen SciERC)\\n  - exp_id: exp_015_metrics_expansion\\n    role: N=8 baseline values\\n  - exp_id: exp_001_seed42_v2\\n    role: N=16 SJ ρ seed=42\\n  - exp_id: exp_001_seed123_v2\\n    role: N=16 SJ ρ seed=123\\n  - exp_id: exp_001_seed456_v2_ner\\n    role: N=16 SJ ρ seed=456\\n  - exp_id: exp_017_llama_conll_n16\\n    role: 'Cross-model block: LLaMA CoNLL N=16 seed=42'\\n  - exp_id: exp_017_llama_conll_n16_s123\\n    role: 'Cross-model block: LLaMA CoNLL N=16 seed=123'\\n  - exp_id: exp_017_llama_conll_n16_s456\\n    role: 'Cross-model block: LLaMA CoNLL N=16 seed=456'\\nfigures:\\n- id: fig:overview\\n  section: introduction\\n  caption: The correlation-selection gap conceptual diagram\\n  evidence:\\n  - exp_id: exp_015_metrics_expansion\\n    role: Quality estimation data (ρ, AUROC for left panel)\\n  - exp_id: exp_016_signal_ensemble\\n    role: Selection F1 data (right panel)\\n- id: fig:signal_heatmap\\n  section: experiments\\n  caption: Quality estimation heatmap (Spearman ρ) across five signals and four configurations\\n  evidence:\\n  - exp_id: exp_015_metrics_expansion\\n    role: Full set ρ values for SciERC NER/RE (Qwen, N=8)\\n  - exp_id: exp_002\\n    role: CoNLL Qwen full set ρ values\\n  - exp_id: exp_001_ner_n16_scierc\\n    role: Conditional set ρ values\\n- id: fig:selection_gap\\n  section: experiments\\n  caption: The correlation-selection gap on SciERC (N=8)\\n  evidence:\\n  - exp_id: exp_016_signal_ensemble\\n    role: Best-of-N selection F1 bars and quality estimation ρ line\\n- id: fig:temperature_robustness\\n  section: experiments\\n  caption: Temperature robustness on SciERC (N=8)\\n  evidence:\\n  - exp_id: exp_005\\n    role: SJ, FK ρ values at T=0.7 and T=1.0\\n- id: fig:reliability\\n  section: experiments\\n  caption: Reliability diagrams on SciERC (N=8, T=1.0)\\n  evidence:\\n  - exp_id: exp_015_metrics_expansion\\n    role: Calibration/ECE data for all signals\\n  - exp_id: exp_002\\n    role: ECE values across signals\\n_completeness:\\n  coverage: 59/92\\n  claims: 87\\n  tables: 4\\n  figures: 5\\n  tier_counts:\\n    tier1: 0\\n    tier2: 59\\n    tier3: 33\\n    tierX: 0\\n  last_checked: '2026-05-18T15:39:48.035668+00:00'\\n\", \"total_chars\": 32730, \"truncated\": false}, \"error\": null, \"metadata\": {}}"
    }
  },
  "sourceToolAssistantUUID": "9e8ac923-9d33-4522-bfdd-ff21639b0c27",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "a97de670-f9a7-4d30-affd-382982b8a334",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-19T13:54:37.844Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_013ZmCZJkNy1WieQVeoM8D64`</summary>

```json
{
  "server": "autodl-5090",
  "command": "find /root/autodl-tmp/struct_self_consist_ie -name \"*.py\" -path \"*auroc*\" -o -name \"*.py\" -path \"*eval*\" -o -name \"*.py\" -path \"*metric*\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e89a0b59-1557-477c-8ff1-b9669ff0f5dd",
  "isSidechain": false,
  "requestId": "req_011CbC3KLXmDCphZ7BiR3dtb",
  "type": "assistant",
  "uuid": "01c8990e-6f22-4960-9813-e1a8fb3a94e8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "a97de670-f9a7-4d30-affd-382982b8a334",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01K9CMF8mt8fbLgVHFPzVjey",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2252,
      "cache_read_input_tokens": 24315,
      "output_tokens": 779,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2252,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 779,
          "cache_read_input_tokens": 24315,
          "cache_creation_input_tokens": 2252,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2252
          },
          "type": "message"
        }
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

_source line 20 · 2026-05-19T13:54:38.723Z_

<details><summary>↩ Tool result · `toolu_013ZmCZJkNy1WieQVeoM8D64`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/struct_self_consist_ie/code/evaluation.py\\n/root/autodl-tmp/struct_self_consist_ie/code/gate0_eval.py\\n/root/autodl-tmp/struct_self_consist_ie/code/gate0_realign_eval.py\\n/root/autodl-tmp/struct_self_consist_ie/code/analyze_exp015_v2_metrics.py\\n/root/autodl-tmp/struct_self_consist_ie/code/eval_n16_5signal.py\\n/root/autodl-tmp/struct_self_consist_ie/code/eval_n8_5signal.py\\n/root/autodl-tmp/struct_self_consist_ie/code/eval_s456_5signal.py\\n/root/autodl-tmp/struct_self_consist_ie/code/eval_exp012_rerun_auroc.py\\n/root/autodl-tmp/struct_self_consist_ie/code/eval_seed42_r1024_5signal.py\\n/root/autodl-tmp/struct_self_consist_ie/code/compute_metrics.py\\n/root/autodl-tmp/struct_self_consist_ie/code/exp026_temp_ablation_metrics.py\\n/root/autodl-tmp/struct_self_consist_ie/code/recompute_table_metrics.py\\n/root/autodl-tmp/struct_self_consist_ie/code/unified_tab_fewnerd_metrics.py\\n/root/autodl-tmp/struct_self_consist_ie/code/dals_fixed_tau_evaluation.py\\n/root/autodl-tmp/struct_self_consist_ie/code/unified_metrics.py\\n/root/autodl-tmp/struct_self_consist_ie/code/regression_test_unified_metrics.py\\n/root/autodl-tmp/struct_self_consist_ie/code/fix_s789_auroc.py\\n/root/autodl-tmp/struct_self_consist_ie/evaluate_verifier.py\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.87}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "01c8990e-6f22-4960-9813-e1a8fb3a94e8",
  "isSidechain": false,
  "promptId": "0731b9be-f5e6-4a8a-9a3c-2edafe06629b",
  "type": "user",
  "uuid": "b0b2fcf2-370e-4f84-a4aa-6afbb21c2464",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"/root/autodl-tmp/struct_self_consist_ie/code/evaluation.py\\\\n/root/autodl-tmp/struct_self_consist_ie/code/gate0_eval.py\\\\n/root/autodl-tmp/struct_self_consist_ie/code/gate0_realign_eval.py\\\\n/root/autodl-tmp/struct_self_consist_ie/code/analyze_exp015_v2_metrics.py\\\\n/root/autodl-tmp/struct_self_consist_ie/code/eval_n16_5signal.py\\\\n/root/autodl-tmp/struct_self_consist_ie/code/eval_n8_5signal.py\\\\n/root/autodl-tmp/struct_self_consist_ie/code/eval_s456_5signal.py\\\\n/root/autodl-tmp/struct_self_consist_ie/code/eval_exp012_rerun_auroc.py\\\\n/root/autodl-tmp/struct_self_consist_ie/code/eval_seed42_r1024_5signal.py\\\\n/root/autodl-tmp/struct_self_consist_ie/code/compute_metrics.py\\\\n/root/autodl-tmp/struct_self_consist_ie/code/exp026_temp_ablation_metrics.py\\\\n/root/autodl-tmp/struct_self_consist_ie/code/recompute_table_metrics.py\\\\n/root/autodl-tmp/struct_self_consist_ie/code/unified_tab_fewnerd_metrics.py\\\\n/root/autodl-tmp/struct_self_consist_ie/code/dals_fixed_tau_evaluation.py\\\\n/root/autodl-tmp/struct_self_consist_ie/code/unified_metrics.py\\\\n/root/autodl-tmp/struct_self_consist_ie/code/regression_test_unified_metrics.py\\\\n/root/autodl-tmp/struct_self_consist_ie/code/fix_s789_auroc.py\\\\n/root/autodl-tmp/struct_self_consist_ie/evaluate_verifier.py\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.87}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/struct_self_consist_ie/code/evaluation.py\\n/root/autodl-tmp/struct_self_consist_ie/code/gate0_eval.py\\n/root/autodl-tmp/struct_self_consist_ie/code/gate0_realign_eval.py\\n/root/autodl-tmp/struct_self_consist_ie/code/analyze_exp015_v2_metrics.py\\n/root/autodl-tmp/struct_self_consist_ie/code/eval_n16_5signal.py\\n/root/autodl-tmp/struct_self_consist_ie/code/eval_n8_5signal.py\\n/root/autodl-tmp/struct_self_consist_ie/code/eval_s456_5signal.py\\n/root/autodl-tmp/struct_self_consist_ie/code/eval_exp012_rerun_auroc.py\\n/root/autodl-tmp/struct_self_consist_ie/code/eval_seed42_r1024_5signal.py\\n/root/autodl-tmp/struct_self_consist_ie/code/compute_metrics.py\\n/root/autodl-tmp/struct_self_consist_ie/code/exp026_temp_ablation_metrics.py\\n/root/autodl-tmp/struct_self_consist_ie/code/recompute_table_metrics.py\\n/root/autodl-tmp/struct_self_consist_ie/code/unified_tab_fewnerd_metrics.py\\n/root/autodl-tmp/struct_self_consist_ie/code/dals_fixed_tau_evaluation.py\\n/root/autodl-tmp/struct_self_consist_ie/code/unified_metrics.py\\n/root/autodl-tmp/struct_self_consist_ie/code/regression_test_unified_metrics.py\\n/root/autodl-tmp/struct_self_consist_ie/code/fix_s789_auroc.py\\n/root/autodl-tmp/struct_self_consist_ie/evaluate_verifier.py\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.87}}"
    }
  },
  "sourceToolAssistantUUID": "01c8990e-6f22-4960-9813-e1a8fb3a94e8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "a97de670-f9a7-4d30-affd-382982b8a334",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-19T13:54:41.863Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01Fq8AJBiRSqeKinq28HLSBi`</summary>

```json
{
  "subagent_type": "Explore",
  "description": "Read paper tex files",
  "prompt": "Read the following files in the project at /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/:\n\n1. Find all .tex files in docs/paper/sections/ directory\n2. Read experiments.tex fully - I need to see Table 1 (SciERC AUROC columns), Table 3 (degeneracy rates, selection Δ)\n3. Read appendix.tex fully - I need the cross-selection table with LP F1 and Δ values\n\nReport the exact numbers found in these tables. Be thorough - capture all numeric values in Table 1 AUROC column for SciERC, Table 3 degeneracy and Δ values, and appendix cross-selection table values."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b0b2fcf2-370e-4f84-a4aa-6afbb21c2464",
  "isSidechain": false,
  "requestId": "req_011CbC3KLXmDCphZ7BiR3dtb",
  "type": "assistant",
  "uuid": "01c033e2-93f4-486c-b27c-c343345c78e3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "a97de670-f9a7-4d30-affd-382982b8a334",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01K9CMF8mt8fbLgVHFPzVjey",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2252,
      "cache_read_input_tokens": 24315,
      "output_tokens": 779,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2252,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 779,
          "cache_read_input_tokens": 24315,
          "cache_creation_input_tokens": 2252,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2252
          },
          "type": "message"
        }
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

_source line 22_

```json
{
  "type": "last-prompt",
  "leafUuid": "01c033e2-93f4-486c-b27c-c343345c78e3",
  "sessionId": "a97de670-f9a7-4d30-affd-382982b8a334"
}
```

---

### Runtime record

_source line 23_

```json
{
  "type": "ai-title",
  "aiTitle": "Audit data inconsistencies in paper tables",
  "sessionId": "a97de670-f9a7-4d30-affd-382982b8a334"
}
```

---

### Tool result

_source line 24 · 2026-05-19T13:55:05.465Z_

<details><summary>↩ Tool result · `toolu_01Fq8AJBiRSqeKinq28HLSBi`</summary>

```text
Perfect! I have found all the key information. Let me now compile the exact numbers from the tables you requested.

## Summary of Exact Numbers from Tables

Based on the files I've read, here are the exact numeric values you requested:

### **TABLE 1: SciERC AUROC Column (tab:quality_estimation)**
Located in experiments.tex, lines 22-41:

| Signal | Family | SciERC AUROC |
|--------|--------|--------------|
| VC | Structural | **0.663** |
| SJ | Structural | 0.650 |
| FK | Surface | 0.602 |
| EM | Surface | 0.614 |
| LP | Model | 0.578 |

### **TABLE 3: LP Selection Across Datasets (tab:fewnerd)**
Located in experiments.tex, lines 111-127:

| Dataset | n | Greedy | Degen.% | LP ρ | LP Δ | p |
|---------|-------|--------|---------|-------|-----------|-------|
| WNUT-17 | 1,287 | .452 | **67.9%** | -.446 | **-0.45 pp** | .72 |
| CoNLL | 2,756 | .908 | **48.4%** | .302 | **-0.85 pp** | 1.0 |
| SciERC | 529 | .644 | **17.8%** | .205 | **+0.61 pp** | .193 |
| Few-NERD | 32,565 | .748 | **13.8%** | .220 | **+1.39 pp** | <.001 |

### **APPENDIX CROSS-SELECTION TABLE (tab:cross_selection)**
Located in appendix.tex, lines 234-250:

| Config | n | Greedy | Oracle | SJ | FK | EM | **LP** | VC |
|--------|-------|--------|--------|--------|--------|--------|-----------|--------|
| LLaMA/SciERC N=8 | 529 | .646 | .778 | .643 | .639 | .634 | **0.652** | .633 |
| LLaMA/SciERC N=16 | 529 | .645 | .806 | .649 | .649 | .640 | **0.646** | .640 |
| LLaMA/FewNERD N=8 | 32,565 | .784 | .884 | .779 | .779 | .774 | **0.788** | .760 |
| Qwen/CoNLL N=8 | 2,756 | .908 | .957 | .899 | .893 | .898 | **0.897** | .895 |
| LLaMA/CoNLL N=8 | 2,756 | .924 | .943 | .924 | .925 | .924 | **0.924** | .923 |

The cross-selection table shows F1 scores (macro, instance-averaged) for best-of-N selection with LP marked in bold as requested. The corresponding Δ values (improvements over greedy) and other metrics can be derived from the differences shown.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "01c033e2-93f4-486c-b27c-c343345c78e3",
  "isSidechain": false,
  "promptId": "0731b9be-f5e6-4a8a-9a3c-2edafe06629b",
  "type": "user",
  "uuid": "30e9b08a-f022-47a6-ad2e-62a4d09b1b42",
  "toolUseResult": {
    "status": "completed",
    "prompt": "Read the following files in the project at /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/:\n\n1. Find all .tex files in docs/paper/sections/ directory\n2. Read experiments.tex fully - I need to see Table 1 (SciERC AUROC columns), Table 3 (degeneracy rates, selection Δ)\n3. Read appendix.tex fully - I need the cross-selection table with LP F1 and Δ values\n\nReport the exact numbers found in these tables. Be thorough - capture all numeric values in Table 1 AUROC column for SciERC, Table 3 degeneracy and Δ values, and appendix cross-selection table values.",
    "agentId": "a6b9c6ef519ef00f3",
    "agentType": "Explore",
    "content": [
      {
        "type": "text",
        "text": "Perfect! I have found all the key information. Let me now compile the exact numbers from the tables you requested.\n\n## Summary of Exact Numbers from Tables\n\nBased on the files I've read, here are the exact numeric values you requested:\n\n### **TABLE 1: SciERC AUROC Column (tab:quality_estimation)**\nLocated in experiments.tex, lines 22-41:\n\n| Signal | Family | SciERC AUROC |\n|--------|--------|--------------|\n| VC | Structural | **0.663** |\n| SJ | Structural | 0.650 |\n| FK | Surface | 0.602 |\n| EM | Surface | 0.614 |\n| LP | Model | 0.578 |\n\n### **TABLE 3: LP Selection Across Datasets (tab:fewnerd)**\nLocated in experiments.tex, lines 111-127:\n\n| Dataset | n | Greedy | Degen.% | LP ρ | LP Δ | p |\n|---------|-------|--------|---------|-------|-----------|-------|\n| WNUT-17 | 1,287 | .452 | **67.9%** | -.446 | **-0.45 pp** | .72 |\n| CoNLL | 2,756 | .908 | **48.4%** | .302 | **-0.85 pp** | 1.0 |\n| SciERC | 529 | .644 | **17.8%** | .205 | **+0.61 pp** | .193 |\n| Few-NERD | 32,565 | .748 | **13.8%** | .220 | **+1.39 pp** | <.001 |\n\n### **APPENDIX CROSS-SELECTION TABLE (tab:cross_selection)**\nLocated in appendix.tex, lines 234-250:\n\n| Config | n | Greedy | Oracle | SJ | FK | EM | **LP** | VC |\n|--------|-------|--------|--------|--------|--------|--------|-----------|--------|\n| LLaMA/SciERC N=8 | 529 | .646 | .778 | .643 | .639 | .634 | **0.652** | .633 |\n| LLaMA/SciERC N=16 | 529 | .645 | .806 | .649 | .649 | .640 | **0.646** | .640 |\n| LLaMA/FewNERD N=8 | 32,565 | .784 | .884 | .779 | .779 | .774 | **0.788** | .760 |\n| Qwen/CoNLL N=8 | 2,756 | .908 | .957 | .899 | .893 | .898 | **0.897** | .895 |\n| LLaMA/CoNLL N=8 | 2,756 | .924 | .943 | .924 | .925 | .924 | **0.924** | .923 |\n\nThe cross-selection table shows F1 scores (macro, instance-averaged) for best-of-N selection with LP marked in bold as requested. The corresponding Δ values (improvements over greedy) and other metrics can be derived from the differences shown."
      }
    ],
    "totalDurationMs": 23598,
    "totalTokens": 39626,
    "totalToolUseCount": 7,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 5092,
      "cache_read_input_tokens": 33721,
      "output_tokens": 810,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 5092
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 810,
          "cache_read_input_tokens": 33721,
          "cache_creation_input_tokens": 5092,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 5092,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 2,
      "searchCount": 5,
      "bashCount": 0,
      "editFileCount": 0,
      "linesAdded": 0,
      "linesRemoved": 0,
      "otherToolCount": 0
    }
  },
  "sourceToolAssistantUUID": "01c033e2-93f4-486c-b27c-c343345c78e3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "a97de670-f9a7-4d30-affd-382982b8a334",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 25 · 2026-05-19T13:55:17.437Z_

<details><summary>Logged reasoning block</summary>

```text
Good, I now have:

1. The paper provenance file with detailed claim evidence
2. Paper table values from the Explore agent
3. List of evaluation scripts on the server
4. The registry query was too large - I need to extract specific experiments

Key findings so far:

**Investigation 1 (SciERC AUROC)**: The provenance file mentions `exp_012_rerun_1024` for AUROC values, and lists:
- VC (voting) AUROC: 0.684 (provenance c002)
- EM AUROC: 0.749 (provenance c002)


But the paper Table 1 shows different values: VC .663, SJ .650, FK .602, EM .614, LP .578. The provenance file indicates `exp_015_v2` as the actual source for Table 1's AUROC values, suggesting two separate experiment runs. I need to query the registry for both experiments, examine the AUROC computation script, and pull the full registry data for FewNERD and CoNLL to trace where these discrepancies come from.

The initial search for exp_012_rerun_1024 came up empty, so I'll try a different approach—extracting the relevant experiments directly from the registry JSON, reading the evaluation script, and checking the LaTeX files themselves to see what's actually documented there.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "30e9b08a-f022-47a6-ad2e-62a4d09b1b42",
  "isSidechain": false,
  "requestId": "req_011CbC3N1PuxsSpfbNHgNbyB",
  "type": "assistant",
  "uuid": "63cb6e6f-c9b7-419b-8d06-6993f789f1a2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "a97de670-f9a7-4d30-affd-382982b8a334",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LbqbHhdF9UVnjW51hjLJJh",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 16797,
      "cache_read_input_tokens": 26567,
      "output_tokens": 788,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 16797,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 788,
          "cache_read_input_tokens": 26567,
          "cache_creation_input_tokens": 16797,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 16797
          },
          "type": "message"
        }
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

_source line 26 · 2026-05-19T13:55:17.438Z_

The exp_012_rerun_1024 filter returned 0 results — probably a different ID format. Let me extract from the full registry dump and read key scripts.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "63cb6e6f-c9b7-419b-8d06-6993f789f1a2",
  "isSidechain": false,
  "requestId": "req_011CbC3N1PuxsSpfbNHgNbyB",
  "type": "assistant",
  "uuid": "761368bd-ef93-4c3a-a215-3815c83187f0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "a97de670-f9a7-4d30-affd-382982b8a334",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LbqbHhdF9UVnjW51hjLJJh",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 16797,
      "cache_read_input_tokens": 26567,
      "output_tokens": 788,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 16797,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 788,
          "cache_read_input_tokens": 26567,
          "cache_creation_input_tokens": 16797,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 16797
          },
          "type": "message"
        }
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

_source line 27 · 2026-05-19T13:55:21.508Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01HyTtEw8FWhEe98rGjNUJB9`</summary>

```json
{
  "command": "cd /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie/a97de670-f9a7-4d30-affd-382982b8a334/tool-results && cat mcp-agent-ml-research-read_registry-1779198876363.txt | python3 -c \"\nimport json, sys\ndata = json.loads(json.loads(sys.stdin.read())['result'])\nexps = data['data']['experiments']\n# List all exp_ids\nfor eid in sorted(exps.keys()):\n    print(eid)\n\"",
  "description": "List all experiment IDs in registry"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "761368bd-ef93-4c3a-a215-3815c83187f0",
  "isSidechain": false,
  "requestId": "req_011CbC3N1PuxsSpfbNHgNbyB",
  "type": "assistant",
  "uuid": "65d7f1c8-c9b7-49f6-93b4-695834fcff5b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "a97de670-f9a7-4d30-affd-382982b8a334",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LbqbHhdF9UVnjW51hjLJJh",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 16797,
      "cache_read_input_tokens": 26567,
      "output_tokens": 788,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 16797,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 788,
          "cache_read_input_tokens": 26567,
          "cache_creation_input_tokens": 16797,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 16797
          },
          "type": "message"
        }
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

_source line 28 · 2026-05-19T13:55:21.681Z_

<details><summary>↩ Tool result · `toolu_01HyTtEw8FWhEe98rGjNUJB9`</summary>

```text
dgs_pilot
e1_component_wise_re_sj
exp001_seed123
exp001_seed456
exp008_re_n16
exp_001_n16_seed123
exp_001_n16_seed123_full
exp_001_n16_seed456
exp_001_n16_seed456_full
exp_001_ner_n16_scierc
exp_001_ner_n16_seed123
exp_001_seed123_t10_full
exp_001_seed123_v2
exp_001_seed123_v2_r1024
exp_001_seed42_v2
exp_001_seed42_v2_r1024
exp_001_seed456_t10_full
exp_001_seed456_v2
exp_001_seed456_v2_ner
exp_001_seed456_v2_ner_r1024
exp_002
exp_002_conll_n16
exp_002_conll_n16_r1024
exp_002_conll_n16_seed123
exp_002_conll_n16_seed456
exp_002_merge_conll2003
exp_002_ner_conll2003
exp_003_ner_wnut17
exp_003_wnut17_eval
exp_003_wnut17_v2
exp_004_re_diagnostic
exp_004_v2
exp_005
exp_005_v2
exp_006_v2
exp_007_llama_inference
exp_007_llama_n16
exp_007_llama_n16_r1024
exp_007_llama_scierc_seed123
exp_007_llama_seed123
exp_007_llama_seed456
exp_007_ner_llama
exp_007_ner_multi_model
exp_008_re_n16
exp_008_re_n16_full
exp_008_re_n16_t10_full
exp_008_re_n16_v2
exp_008_re_seed123
exp_009_capability_stratification
exp_009_v2
exp_009_v2_re_rerun
exp_010_selection_curves
exp_011_ood_conll_to_scierc
exp_011_ood_scierc_to_conll
exp_012_logprob_baseline
exp_012_rerun_1024
exp_013_exact_match_voting
exp_014_entity_majority_voting
exp_015_metrics_expansion
exp_015_v2
exp_016_rerun_1024_bootstrap
exp_016_signal_ensemble
exp_016_v2
exp_017_llama_conll
exp_017_llama_conll_finetune
exp_017_llama_conll_infer
exp_017_llama_conll_n16
exp_017_llama_conll_n16_r1024
exp_017_llama_conll_n16_s123
exp_017_llama_conll_n16_s123_r1024
exp_017_llama_conll_n16_s456
exp_017_llama_conll_n16_s456_r1024
exp_017_llama_conll_n8_t07
exp_018_llama_scierc_seed123
exp_018_llama_scierc_seed42_r1024
exp_018_llama_scierc_seed456
exp_018_llama_scierc_seed456_r1024
exp_018_qwen_scierc_seed123
exp_018_qwen_scierc_seed456
exp_019_supervised_verifier
exp_020_fewnerd_smoke
exp_021_fewnerd_full
exp_021_fewnerd_n8_seed123
exp_021_fewnerd_n8_seed456
exp_022_seed789
exp_023_lora_rank8
exp_024_claim_audit
exp_025_n32
exp_026_T05
exp_026_T08
exp_026_T12
exp_026_t05
exp_026_t05_scierc
exp_026_t05_seed123
exp_026_t05_seed456
exp_026_t08
exp_026_t08_scierc
exp_026_t08_seed123
exp_026_t08_seed456
exp_026_t10_seed123
exp_026_t10_seed42
exp_026_t10_seed456
exp_026_t12
exp_026_t12_scierc
exp_026_t12_seed123
exp_026_t12_seed456
exp_027_fewnerd_n16
exp_027_mlp_verifier
exp_028
exp_028_entity_token_lp
exp_028_fewnerd_5epoch
exp_029a
exp_029b
exp_030_conll_t12
exp_031_fewnerd_t12
exp_adaptive_temperature
exp_ccs_selection
exp_diagnostic_calibration
exp_entity_consensus
exp_entity_construction
exp_entity_token_lp
exp_epoch_dgs_analysis
exp_fewnerd_s789_n8
exp_freeform_ablation
exp_freeform_conll_4seed
exp_freeform_seed123
exp_freeform_seed456
exp_freeform_seed789
exp_freeform_seed789_v2
exp_freeform_seed789_v3
exp_llama3b_scierc_ablation
exp_llama_fewnerd_inference
exp_llama_fewnerd_lora
exp_llama_scierc_seed456
exp_lp_alignment_gating
exp_lp_scierc_t07
exp_lp_t07_scierc
exp_qwen25_14b_fewnerd
exp_qwen25_32b_fewnerd
exp_qwen25_72b_zeroshot
exp_qwen25_7b_fewnerd
exp_qwen3_4b_conll_finetune
exp_qwen3_4b_conll_finetune_resume
exp_qwen3_4b_conll_merge_inference_v2
exp_qwen3_4b_conll_scs_inference
exp_qwen3_4b_conll_scs_inference_v2
exp_qwen3_4b_scierc_finetune
exp_qwen3_4b_scierc_finetune_v2
exp_qwen3_4b_scierc_finetune_v3
exp_qwen3_4b_scierc_finetune_v4
exp_qwen3_4b_scierc_merge_inference
exp_qwen3_4b_scierc_scs_inference
exp_re_scierc_seed123
exp_re_scierc_seed456
exp_selective_prediction
exp_tacred_re_benchmark
exp_vc_lp_cascade_selection
exp_vc_quartile_analysis
exp_verbalized_confidence
exp_wnut17_qwen25_7b
ft_001
ft_002
ft_002_v2
hidden_state_probe_conll_full
hidden_state_probe_conll_v2
mbr_pilot
mvp_pilot_001
mvp_pilot_002
mvp_pilot_003
mvp_pilot_004
mvp_pilot_005
Shell cwd was reset to /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "65d7f1c8-c9b7-49f6-93b4-695834fcff5b",
  "isSidechain": false,
  "promptId": "0731b9be-f5e6-4a8a-9a3c-2edafe06629b",
  "type": "user",
  "uuid": "50ec7c81-1941-4635-9607-857f7db3100c",
  "toolUseResult": {
    "stdout": "dgs_pilot\ne1_component_wise_re_sj\nexp001_seed123\nexp001_seed456\nexp008_re_n16\nexp_001_n16_seed123\nexp_001_n16_seed123_full\nexp_001_n16_seed456\nexp_001_n16_seed456_full\nexp_001_ner_n16_scierc\nexp_001_ner_n16_seed123\nexp_001_seed123_t10_full\nexp_001_seed123_v2\nexp_001_seed123_v2_r1024\nexp_001_seed42_v2\nexp_001_seed42_v2_r1024\nexp_001_seed456_t10_full\nexp_001_seed456_v2\nexp_001_seed456_v2_ner\nexp_001_seed456_v2_ner_r1024\nexp_002\nexp_002_conll_n16\nexp_002_conll_n16_r1024\nexp_002_conll_n16_seed123\nexp_002_conll_n16_seed456\nexp_002_merge_conll2003\nexp_002_ner_conll2003\nexp_003_ner_wnut17\nexp_003_wnut17_eval\nexp_003_wnut17_v2\nexp_004_re_diagnostic\nexp_004_v2\nexp_005\nexp_005_v2\nexp_006_v2\nexp_007_llama_inference\nexp_007_llama_n16\nexp_007_llama_n16_r1024\nexp_007_llama_scierc_seed123\nexp_007_llama_seed123\nexp_007_llama_seed456\nexp_007_ner_llama\nexp_007_ner_multi_model\nexp_008_re_n16\nexp_008_re_n16_full\nexp_008_re_n16_t10_full\nexp_008_re_n16_v2\nexp_008_re_seed123\nexp_009_capability_stratification\nexp_009_v2\nexp_009_v2_re_rerun\nexp_010_selection_curves\nexp_011_ood_conll_to_scierc\nexp_011_ood_scierc_to_conll\nexp_012_logprob_baseline\nexp_012_rerun_1024\nexp_013_exact_match_voting\nexp_014_entity_majority_voting\nexp_015_metrics_expansion\nexp_015_v2\nexp_016_rerun_1024_bootstrap\nexp_016_signal_ensemble\nexp_016_v2\nexp_017_llama_conll\nexp_017_llama_conll_finetune\nexp_017_llama_conll_infer\nexp_017_llama_conll_n16\nexp_017_llama_conll_n16_r1024\nexp_017_llama_conll_n16_s123\nexp_017_llama_conll_n16_s123_r1024\nexp_017_llama_conll_n16_s456\nexp_017_llama_conll_n16_s456_r1024\nexp_017_llama_conll_n8_t07\nexp_018_llama_scierc_seed123\nexp_018_llama_scierc_seed42_r1024\nexp_018_llama_scierc_seed456\nexp_018_llama_scierc_seed456_r1024\nexp_018_qwen_scierc_seed123\nexp_018_qwen_scierc_seed456\nexp_019_supervised_verifier\nexp_020_fewnerd_smoke\nexp_021_fewnerd_full\nexp_021_fewnerd_n8_seed123\nexp_021_fewnerd_n8_seed456\nexp_022_seed789\nexp_023_lora_rank8\nexp_024_claim_audit\nexp_025_n32\nexp_026_T05\nexp_026_T08\nexp_026_T12\nexp_026_t05\nexp_026_t05_scierc\nexp_026_t05_seed123\nexp_026_t05_seed456\nexp_026_t08\nexp_026_t08_scierc\nexp_026_t08_seed123\nexp_026_t08_seed456\nexp_026_t10_seed123\nexp_026_t10_seed42\nexp_026_t10_seed456\nexp_026_t12\nexp_026_t12_scierc\nexp_026_t12_seed123\nexp_026_t12_seed456\nexp_027_fewnerd_n16\nexp_027_mlp_verifier\nexp_028\nexp_028_entity_token_lp\nexp_028_fewnerd_5epoch\nexp_029a\nexp_029b\nexp_030_conll_t12\nexp_031_fewnerd_t12\nexp_adaptive_temperature\nexp_ccs_selection\nexp_diagnostic_calibration\nexp_entity_consensus\nexp_entity_construction\nexp_entity_token_lp\nexp_epoch_dgs_analysis\nexp_fewnerd_s789_n8\nexp_freeform_ablation\nexp_freeform_conll_4seed\nexp_freeform_seed123\nexp_freeform_seed456\nexp_freeform_seed789\nexp_freeform_seed789_v2\nexp_freeform_seed789_v3\nexp_llama3b_scierc_ablation\nexp_llama_fewnerd_inference\nexp_llama_fewnerd_lora\nexp_llama_scierc_seed456\nexp_lp_alignment_gating\nexp_lp_scierc_t07\nexp_lp_t07_scierc\nexp_qwen25_14b_fewnerd\nexp_qwen25_32b_fewnerd\nexp_qwen25_72b_zeroshot\nexp_qwen25_7b_fewnerd\nexp_qwen3_4b_conll_finetune\nexp_qwen3_4b_conll_finetune_resume\nexp_qwen3_4b_conll_merge_inference_v2\nexp_qwen3_4b_conll_scs_inference\nexp_qwen3_4b_conll_scs_inference_v2\nexp_qwen3_4b_scierc_finetune\nexp_qwen3_4b_scierc_finetune_v2\nexp_qwen3_4b_scierc_finetune_v3\nexp_qwen3_4b_scierc_finetune_v4\nexp_qwen3_4b_scierc_merge_inference\nexp_qwen3_4b_scierc_scs_inference\nexp_re_scierc_seed123\nexp_re_scierc_seed456\nexp_selective_prediction\nexp_tacred_re_benchmark\nexp_vc_lp_cascade_selection\nexp_vc_quartile_analysis\nexp_verbalized_confidence\nexp_wnut17_qwen25_7b\nft_001\nft_002\nft_002_v2\nhidden_state_probe_conll_full\nhidden_state_probe_conll_v2\nmbr_pilot\nmvp_pilot_001\nmvp_pilot_002\nmvp_pilot_003\nmvp_pilot_004\nmvp_pilot_005",
    "stderr": "\nShell cwd was reset to /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "65d7f1c8-c9b7-49f6-93b4-695834fcff5b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "a97de670-f9a7-4d30-affd-382982b8a334",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-19T13:55:22.537Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01Pq3UGi2SfJ5g5YH6v8uphq`</summary>

```json
{
  "server": "autodl-5090",
  "command": "cat /root/autodl-tmp/struct_self_consist_ie/code/eval_exp012_rerun_auroc.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "50ec7c81-1941-4635-9607-857f7db3100c",
  "isSidechain": false,
  "requestId": "req_011CbC3N1PuxsSpfbNHgNbyB",
  "type": "assistant",
  "uuid": "fbfc4a61-cd70-48b2-aa3e-a3083c35606d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "a97de670-f9a7-4d30-affd-382982b8a334",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LbqbHhdF9UVnjW51hjLJJh",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 16797,
      "cache_read_input_tokens": 26567,
      "output_tokens": 788,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 16797,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 788,
          "cache_read_input_tokens": 26567,
          "cache_creation_input_tokens": 16797,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 16797
          },
          "type": "message"
        }
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

_source line 30 · 2026-05-19T13:55:22.910Z_

<details><summary>↩ Tool result · `toolu_01Pq3UGi2SfJ5g5YH6v8uphq`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"#!/usr/bin/env python3\\n\\\"\\\"\\\"Compute 5-signal AUROC for exp_012_rerun_1024 (joint NER+RE).\\\"\\\"\\\"\\nimport json, sys\\nimport numpy as np\\nfrom scipy.stats import spearmanr, rankdata\\nfrom collections import Counter\\n\\nsys.path.insert(0, '/root/autodl-tmp/struct_self_consist_ie/code')\\nfrom consistency import compute_all_consistency_scores\\nfrom evaluation import per_instance_f1\\n\\nDATA_PATH = \\\"/root/autodl-tmp/struct_self_consist_ie/output/exp_012_rerun_1024/samples.jsonl\\\"\\n\\ndef load_data(path):\\n    with open(path) as f:\\n        return [json.loads(line) for line in f if line.strip()]\\n\\ndef compute_exact_match_rate(samples, subtask):\\n    if subtask == \\\"ner\\\":\\n        keys = [frozenset((e[\\\"text\\\"], e[\\\"type\\\"]) for e in s.get(\\\"entities\\\", [])) for s in samples]\\n    else:\\n        keys = [frozenset((r[\\\"head\\\"], r[\\\"tail\\\"], r[\\\"type\\\"]) for r in s.get(\\\"relations\\\", [])) for s in samples]\\n    if not keys: return 0.0\\n    c = Counter(keys)\\n    return c.most_common(1)[0][1] / len(samples)\\n\\ndef compute_voting_confidence(samples, subtask):\\n    N = len(samples)\\n    if N == 0: return 0.0\\n    counter = Counter()\\n    if subtask == \\\"ner\\\":\\n        for s in samples:\\n            for e in s.get(\\\"entities\\\", []):\\n                counter[(e[\\\"text\\\"], e[\\\"type\\\"])] += 1\\n    else:\\n        for s in samples:\\n            for r in s.get(\\\"relations\\\", []):\\n                counter[(r[\\\"head\\\"], r[\\\"tail\\\"], r[\\\"type\\\"])] += 1\\n    if not counter: return 0.0\\n    return float(np.mean([v / N for v in counter.values()]))\\n\\ndef compute_mean_logprob(samples):\\n    lps = [s.get(\\\"mean_logprob\\\") for s in samples if s.get(\\\"mean_logprob\\\") is not None]\\n    lps = [lp for lp in lps if np.isfinite(lp)]\\n    return float(np.mean(lps)) if lps else float(\\\"nan\\\")\\n\\ndef safe_auroc(scores, labels):\\n    scores, labels = np.asarray(scores, float), np.asarray(labels, int)\\n    mask = np.isfinite(scores)\\n    scores, labels = scores[mask], labels[mask]\\n    if len(np.unique(labels)) < 2: return float(\\\"nan\\\")\\n    n_pos, n_neg = (labels==1).sum(), (labels==0).sum()\\n    if n_pos == 0 or n_neg == 0: return float(\\\"nan\\\")\\n    ranks = rankdata(scores)\\n    u = ranks[labels==1].sum() - n_pos*(n_pos+1)/2\\n    return float(u / (n_pos * n_neg))\\n\\ndef analyze(instances, subtask):\\n    entity_key = \\\"entities\\\" if subtask == \\\"ner\\\" else \\\"relations\\\"\\n    valid = [inst for inst in instances if len(inst[\\\"gold\\\"].get(entity_key, [])) > 0]\\n\\n    greedy_f1s = []\\n    for inst in valid:\\n        greedy = inst.get(\\\"greedy\\\", inst[\\\"samples\\\"][0])\\n        greedy_f1s.append(per_instance_f1(greedy, inst[\\\"gold\\\"], subtask=subtask))\\n    \\n    conditional_pairs = [(inst, f1) for inst, f1 in zip(valid, greedy_f1s) if f1 > 0]\\n    conditional_insts = [p[0] for p in conditional_pairs]\\n    conditional_f1s = [p[1] for p in conditional_pairs]\\n\\n    results = {\\\"n_total\\\": len(instances), \\\"n_valid\\\": len(valid), \\\"n_conditional\\\": len(conditional_insts)}\\n\\n    for split_name, split_insts, split_f1s in [\\n        (\\\"full\\\", valid, greedy_f1s),\\n        (\\\"cond\\\", conditional_insts, conditional_f1s),\\n    ]:\\n        cons = compute_all_consistency_scores(split_insts, subtask=subtask)\\n        sj = cons[\\\"soft_jaccard\\\"]\\n        fk = cons[\\\"fleiss_kappa\\\"]\\n\\n        lp, em, vc = [], [], []\\n        for inst in split_insts:\\n            samples = inst[\\\"samples\\\"]\\n            lp.append(compute_mean_logprob(samples))\\n            em.append(compute_exact_match_rate(samples, subtask))\\n            vc.append(compute_voting_confidence(samples, subtask))\\n\\n        signals = {\\\"sj\\\": np.array(sj), \\\"fk\\\": np.array(fk), \\\"logprob\\\": np.array(lp),\\n                    \\\"em\\\": np.array(em), \\\"voting_conf\\\": np.array(vc)}\\n        f1_arr = np.array(split_f1s)\\n        binary = (f1_arr >= 1.0).astype(int)\\n\\n        split_res = {\\\"n\\\": len(split_insts), \\\"n_pos\\\": int(binary.sum()), \\\"n_neg\\\": int((1-binary).sum())}\\n        for name, vals in signals.items():\\n            auroc = safe_auroc(vals, binary)\\n            split_res[f\\\"auroc_{name}\\\"] = round(auroc, 6) if np.isfinite(auroc) else None\\n        results[split_name] = split_res\\n    return results\\n\\ninstances = load_data(DATA_PATH)\\nprint(f\\\"Loaded {len(instances)} instances\\\")\\n\\nall_results = {}\\nfor subtask in [\\\"ner\\\", \\\"re\\\"]:\\n    print(f\\\"\\\\nProcessing {subtask}...\\\")\\n    all_results[subtask] = analyze(instances, subtask)\\n    r = all_results[subtask]\\n    print(f\\\"  n_valid={r['n_valid']}, n_conditional={r['n_conditional']}\\\")\\n    for split in [\\\"full\\\", \\\"cond\\\"]:\\n        sr = r[split]\\n        print(f\\\"  {split} (n={sr['n']}, pos={sr['n_pos']}, neg={sr['n_neg']}):\\\")\\n        for sig in [\\\"sj\\\", \\\"fk\\\", \\\"em\\\", \\\"voting_conf\\\", \\\"logprob\\\"]:\\n            print(f\\\"    {sig}: {sr[f'auroc_{sig}']}\\\")\\n\\nout_path = \\\"/root/autodl-tmp/struct_self_consist_ie/output/exp_012_rerun_1024/auroc_5signal.json\\\"\\nwith open(out_path, \\\"w\\\") as f:\\n    json.dump(all_results, f, indent=2)\\nprint(f\\\"\\\\nSaved to {out_path}\\\")\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.36}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fbfc4a61-cd70-48b2-aa3e-a3083c35606d",
  "isSidechain": false,
  "promptId": "0731b9be-f5e6-4a8a-9a3c-2edafe06629b",
  "type": "user",
  "uuid": "891b6248-ece4-4a1a-bca3-05a025de93dc",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"#!/usr/bin/env python3\\\\n\\\\\\\"\\\\\\\"\\\\\\\"Compute 5-signal AUROC for exp_012_rerun_1024 (joint NER+RE).\\\\\\\"\\\\\\\"\\\\\\\"\\\\nimport json, sys\\\\nimport numpy as np\\\\nfrom scipy.stats import spearmanr, rankdata\\\\nfrom collections import Counter\\\\n\\\\nsys.path.insert(0, '/root/autodl-tmp/struct_self_consist_ie/code')\\\\nfrom consistency import compute_all_consistency_scores\\\\nfrom evaluation import per_instance_f1\\\\n\\\\nDATA_PATH = \\\\\\\"/root/autodl-tmp/struct_self_consist_ie/output/exp_012_rerun_1024/samples.jsonl\\\\\\\"\\\\n\\\\ndef load_data(path):\\\\n    with open(path) as f:\\\\n        return [json.loads(line) for line in f if line.strip()]\\\\n\\\\ndef compute_exact_match_rate(samples, subtask):\\\\n    if subtask == \\\\\\\"ner\\\\\\\":\\\\n        keys = [frozenset((e[\\\\\\\"text\\\\\\\"], e[\\\\\\\"type\\\\\\\"]) for e in s.get(\\\\\\\"entities\\\\\\\", [])) for s in samples]\\\\n    else:\\\\n        keys = [frozenset((r[\\\\\\\"head\\\\\\\"], r[\\\\\\\"tail\\\\\\\"], r[\\\\\\\"type\\\\\\\"]) for r in s.get(\\\\\\\"relations\\\\\\\", [])) for s in samples]\\\\n    if not keys: return 0.0\\\\n    c = Counter(keys)\\\\n    return c.most_common(1)[0][1] / len(samples)\\\\n\\\\ndef compute_voting_confidence(samples, subtask):\\\\n    N = len(samples)\\\\n    if N == 0: return 0.0\\\\n    counter = Counter()\\\\n    if subtask == \\\\\\\"ner\\\\\\\":\\\\n        for s in samples:\\\\n            for e in s.get(\\\\\\\"entities\\\\\\\", []):\\\\n                counter[(e[\\\\\\\"text\\\\\\\"], e[\\\\\\\"type\\\\\\\"])] += 1\\\\n    else:\\\\n        for s in samples:\\\\n            for r in s.get(\\\\\\\"relations\\\\\\\", []):\\\\n                counter[(r[\\\\\\\"head\\\\\\\"], r[\\\\\\\"tail\\\\\\\"], r[\\\\\\\"type\\\\\\\"])] += 1\\\\n    if not counter: return 0.0\\\\n    return float(np.mean([v / N for v in counter.values()]))\\\\n\\\\ndef compute_mean_logprob(samples):\\\\n    lps = [s.get(\\\\\\\"mean_logprob\\\\\\\") for s in samples if s.get(\\\\\\\"mean_logprob\\\\\\\") is not None]\\\\n    lps = [lp for lp in lps if np.isfinite(lp)]\\\\n    return float(np.mean(lps)) if lps else float(\\\\\\\"nan\\\\\\\")\\\\n\\\\ndef safe_auroc(scores, labels):\\\\n    scores, labels = np.asarray(scores, float), np.asarray(labels, int)\\\\n    mask = np.isfinite(scores)\\\\n    scores, labels = scores[mask], labels[mask]\\\\n    if len(np.unique(labels)) < 2: return float(\\\\\\\"nan\\\\\\\")\\\\n    n_pos, n_neg = (labels==1).sum(), (labels==0).sum()\\\\n    if n_pos == 0 or n_neg == 0: return float(\\\\\\\"nan\\\\\\\")\\\\n    ranks = rankdata(scores)\\\\n    u = ranks[labels==1].sum() - n_pos*(n_pos+1)/2\\\\n    return float(u / (n_pos * n_neg))\\\\n\\\\ndef analyze(instances, subtask):\\\\n    entity_key = \\\\\\\"entities\\\\\\\" if subtask == \\\\\\\"ner\\\\\\\" else \\\\\\\"relations\\\\\\\"\\\\n    valid = [inst for inst in instances if len(inst[\\\\\\\"gold\\\\\\\"].get(entity_key, [])) > 0]\\\\n\\\\n    greedy_f1s = []\\\\n    for inst in valid:\\\\n        greedy = inst.get(\\\\\\\"greedy\\\\\\\", inst[\\\\\\\"samples\\\\\\\"][0])\\\\n        greedy_f1s.append(per_instance_f1(greedy, inst[\\\\\\\"gold\\\\\\\"], subtask=subtask))\\\\n    \\\\n    conditional_pairs = [(inst, f1) for inst, f1 in zip(valid, greedy_f1s) if f1 > 0]\\\\n    conditional_insts = [p[0] for p in conditional_pairs]\\\\n    conditional_f1s = [p[1] for p in conditional_pairs]\\\\n\\\\n    results = {\\\\\\\"n_total\\\\\\\": len(instances), \\\\\\\"n_valid\\\\\\\": len(valid), \\\\\\\"n_conditional\\\\\\\": len(conditional_insts)}\\\\n\\\\n    for split_name, split_insts, split_f1s in [\\\\n        (\\\\\\\"full\\\\\\\", valid, greedy_f1s),\\\\n        (\\\\\\\"cond\\\\\\\", conditional_insts, conditional_f1s),\\\\n    ]:\\\\n        cons = compute_all_consistency_scores(split_insts, subtask=subtask)\\\\n        sj = cons[\\\\\\\"soft_jaccard\\\\\\\"]\\\\n        fk = cons[\\\\\\\"fleiss_kappa\\\\\\\"]\\\\n\\\\n        lp, em, vc = [], [], []\\\\n        for inst in split_insts:\\\\n            samples = inst[\\\\\\\"samples\\\\\\\"]\\\\n            lp.append(compute_mean_logprob(samples))\\\\n            em.append(compute_exact_match_rate(samples, subtask))\\\\n            vc.append(compute_voting_confidence(samples, subtask))\\\\n\\\\n        signals = {\\\\\\\"sj\\\\\\\": np.array(sj), \\\\\\\"fk\\\\\\\": np.array(fk), \\\\\\\"logprob\\\\\\\": np.array(lp),\\\\n                    \\\\\\\"em\\\\\\\": np.array(em), \\\\\\\"voting_conf\\\\\\\": np.array(vc)}\\\\n        f1_arr = np.array(split_f1s)\\\\n        binary = (f1_arr >= 1.0).astype(int)\\\\n\\\\n        split_res = {\\\\\\\"n\\\\\\\": len(split_insts), \\\\\\\"n_pos\\\\\\\": int(binary.sum()), \\\\\\\"n_neg\\\\\\\": int((1-binary).sum())}\\\\n        for name, vals in signals.items():\\\\n            auroc = safe_auroc(vals, binary)\\\\n            split_res[f\\\\\\\"auroc_{name}\\\\\\\"] = round(auroc, 6) if np.isfinite(auroc) else None\\\\n        results[split_name] = split_res\\\\n    return results\\\\n\\\\ninstances = load_data(DATA_PATH)\\\\nprint(f\\\\\\\"Loaded {len(instances)} instances\\\\\\\")\\\\n\\\\nall_results = {}\\\\nfor subtask in [\\\\\\\"ner\\\\\\\", \\\\\\\"re\\\\\\\"]:\\\\n    print(f\\\\\\\"\\\\\\\\nProcessing {subtask}...\\\\\\\")\\\\n    all_results[subtask] = analyze(instances, subtask)\\\\n    r = all_results[subtask]\\\\n    print(f\\\\\\\"  n_valid={r['n_valid']}, n_conditional={r['n_conditional']}\\\\\\\")\\\\n    for split in [\\\\\\\"full\\\\\\\", \\\\\\\"cond\\\\\\\"]:\\\\n        sr = r[split]\\\\n        print(f\\\\\\\"  {split} (n={sr['n']}, pos={sr['n_pos']}, neg={sr['n_neg']}):\\\\\\\")\\\\n        for sig in [\\\\\\\"sj\\\\\\\", \\\\\\\"fk\\\\\\\", \\\\\\\"em\\\\\\\", \\\\\\\"voting_conf\\\\\\\", \\\\\\\"logprob\\\\\\\"]:\\\\n            print(f\\\\\\\"    {sig}: {sr[f'auroc_{sig}']}\\\\\\\")\\\\n\\\\nout_path = \\\\\\\"/root/autodl-tmp/struct_self_consist_ie/output/exp_012_rerun_1024/auroc_5signal.json\\\\\\\"\\\\nwith open(out_path, \\\\\\\"w\\\\\\\") as f:\\\\n    json.dump(all_results, f, indent=2)\\\\nprint(f\\\\\\\"\\\\\\\\nSaved to {out_path}\\\\\\\")\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.36}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"#!/usr/bin/env python3\\n\\\"\\\"\\\"Compute 5-signal AUROC for exp_012_rerun_1024 (joint NER+RE).\\\"\\\"\\\"\\nimport json, sys\\nimport numpy as np\\nfrom scipy.stats import spearmanr, rankdata\\nfrom collections import Counter\\n\\nsys.path.insert(0, '/root/autodl-tmp/struct_self_consist_ie/code')\\nfrom consistency import compute_all_consistency_scores\\nfrom evaluation import per_instance_f1\\n\\nDATA_PATH = \\\"/root/autodl-tmp/struct_self_consist_ie/output/exp_012_rerun_1024/samples.jsonl\\\"\\n\\ndef load_data(path):\\n    with open(path) as f:\\n        return [json.loads(line) for line in f if line.strip()]\\n\\ndef compute_exact_match_rate(samples, subtask):\\n    if subtask == \\\"ner\\\":\\n        keys = [frozenset((e[\\\"text\\\"], e[\\\"type\\\"]) for e in s.get(\\\"entities\\\", [])) for s in samples]\\n    else:\\n        keys = [frozenset((r[\\\"head\\\"], r[\\\"tail\\\"], r[\\\"type\\\"]) for r in s.get(\\\"relations\\\", [])) for s in samples]\\n    if not keys: return 0.0\\n    c = Counter(keys)\\n    return c.most_common(1)[0][1] / len(samples)\\n\\ndef compute_voting_confidence(samples, subtask):\\n    N = len(samples)\\n    if N == 0: return 0.0\\n    counter = Counter()\\n    if subtask == \\\"ner\\\":\\n        for s in samples:\\n            for e in s.get(\\\"entities\\\", []):\\n                counter[(e[\\\"text\\\"], e[\\\"type\\\"])] += 1\\n    else:\\n        for s in samples:\\n            for r in s.get(\\\"relations\\\", []):\\n                counter[(r[\\\"head\\\"], r[\\\"tail\\\"], r[\\\"type\\\"])] += 1\\n    if not counter: return 0.0\\n    return float(np.mean([v / N for v in counter.values()]))\\n\\ndef compute_mean_logprob(samples):\\n    lps = [s.get(\\\"mean_logprob\\\") for s in samples if s.get(\\\"mean_logprob\\\") is not None]\\n    lps = [lp for lp in lps if np.isfinite(lp)]\\n    return float(np.mean(lps)) if lps else float(\\\"nan\\\")\\n\\ndef safe_auroc(scores, labels):\\n    scores, labels = np.asarray(scores, float), np.asarray(labels, int)\\n    mask = np.isfinite(scores)\\n    scores, labels = scores[mask], labels[mask]\\n    if len(np.unique(labels)) < 2: return float(\\\"nan\\\")\\n    n_pos, n_neg = (labels==1).sum(), (labels==0).sum()\\n    if n_pos == 0 or n_neg == 0: return float(\\\"nan\\\")\\n    ranks = rankdata(scores)\\n    u = ranks[labels==1].sum() - n_pos*(n_pos+1)/2\\n    return float(u / (n_pos * n_neg))\\n\\ndef analyze(instances, subtask):\\n    entity_key = \\\"entities\\\" if subtask == \\\"ner\\\" else \\\"relations\\\"\\n    valid = [inst for inst in instances if len(inst[\\\"gold\\\"].get(entity_key, [])) > 0]\\n\\n    greedy_f1s = []\\n    for inst in valid:\\n        greedy = inst.get(\\\"greedy\\\", inst[\\\"samples\\\"][0])\\n        greedy_f1s.append(per_instance_f1(greedy, inst[\\\"gold\\\"], subtask=subtask))\\n    \\n    conditional_pairs = [(inst, f1) for inst, f1 in zip(valid, greedy_f1s) if f1 > 0]\\n    conditional_insts = [p[0] for p in conditional_pairs]\\n    conditional_f1s = [p[1] for p in conditional_pairs]\\n\\n    results = {\\\"n_total\\\": len(instances), \\\"n_valid\\\": len(valid), \\\"n_conditional\\\": len(conditional_insts)}\\n\\n    for split_name, split_insts, split_f1s in [\\n        (\\\"full\\\", valid, greedy_f1s),\\n        (\\\"cond\\\", conditional_insts, conditional_f1s),\\n    ]:\\n        cons = compute_all_consistency_scores(split_insts, subtask=subtask)\\n        sj = cons[\\\"soft_jaccard\\\"]\\n        fk = cons[\\\"fleiss_kappa\\\"]\\n\\n        lp, em, vc = [], [], []\\n        for inst in split_insts:\\n            samples = inst[\\\"samples\\\"]\\n            lp.append(compute_mean_logprob(samples))\\n            em.append(compute_exact_match_rate(samples, subtask))\\n            vc.append(compute_voting_confidence(samples, subtask))\\n\\n        signals = {\\\"sj\\\": np.array(sj), \\\"fk\\\": np.array(fk), \\\"logprob\\\": np.array(lp),\\n                    \\\"em\\\": np.array(em), \\\"voting_conf\\\": np.array(vc)}\\n        f1_arr = np.array(split_f1s)\\n        binary = (f1_arr >= 1.0).astype(int)\\n\\n        split_res = {\\\"n\\\": len(split_insts), \\\"n_pos\\\": int(binary.sum()), \\\"n_neg\\\": int((1-binary).sum())}\\n        for name, vals in signals.items():\\n            auroc = safe_auroc(vals, binary)\\n            split_res[f\\\"auroc_{name}\\\"] = round(auroc, 6) if np.isfinite(auroc) else None\\n        results[split_name] = split_res\\n    return results\\n\\ninstances = load_data(DATA_PATH)\\nprint(f\\\"Loaded {len(instances)} instances\\\")\\n\\nall_results = {}\\nfor subtask in [\\\"ner\\\", \\\"re\\\"]:\\n    print(f\\\"\\\\nProcessing {subtask}...\\\")\\n    all_results[subtask] = analyze(instances, subtask)\\n    r = all_results[subtask]\\n    print(f\\\"  n_valid={r['n_valid']}, n_conditional={r['n_conditional']}\\\")\\n    for split in [\\\"full\\\", \\\"cond\\\"]:\\n        sr = r[split]\\n        print(f\\\"  {split} (n={sr['n']}, pos={sr['n_pos']}, neg={sr['n_neg']}):\\\")\\n        for sig in [\\\"sj\\\", \\\"fk\\\", \\\"em\\\", \\\"voting_conf\\\", \\\"logprob\\\"]:\\n            print(f\\\"    {sig}: {sr[f'auroc_{sig}']}\\\")\\n\\nout_path = \\\"/root/autodl-tmp/struct_self_consist_ie/output/exp_012_rerun_1024/auroc_5signal.json\\\"\\nwith open(out_path, \\\"w\\\") as f:\\n    json.dump(all_results, f, indent=2)\\nprint(f\\\"\\\\nSaved to {out_path}\\\")\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.36}}"
    }
  },
  "sourceToolAssistantUUID": "fbfc4a61-cd70-48b2-aa3e-a3083c35606d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "a97de670-f9a7-4d30-affd-382982b8a334",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 31 · 2026-05-19T13:55:22.914Z_

```json
{
  "parentUuid": "891b6248-ece4-4a1a-bca3-05a025de93dc",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "12887522-0af9-4d9b-aeb3-1b17f220fe3d",
  "timestamp": "2026-05-19T13:55:22.914Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "a97de670-f9a7-4d30-affd-382982b8a334",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 32_

```json
{
  "type": "last-prompt",
  "leafUuid": "12887522-0af9-4d9b-aeb3-1b17f220fe3d",
  "sessionId": "a97de670-f9a7-4d30-affd-382982b8a334"
}
```

---

### Runtime record

_source line 33_

```json
{
  "type": "ai-title",
  "aiTitle": "Audit data inconsistencies in paper tables",
  "sessionId": "a97de670-f9a7-4d30-affd-382982b8a334"
}
```

---

### Assistant

_source line 34 · 2026-05-19T13:55:31.289Z_

<details><summary>Logged reasoning block</summary>

```text
Key finding from the AUROC script: The binarization threshold is `f1_arr >= 1.0` — this means it's checking if an instance achieves a PERFECT F1 score of 1.0, not using a typical 0.5 threshold. This is actually the correct approach for AUROC in this context (can the signal distinguish perfect extractions from imperfect ones).

Now I need to:
1. Check if there are AUROC results saved from this script
2. Check exp_015_v2 for AUROC values (the provenance says Table 1 sources AUROC from exp_015_v2)


3. Pull the FewNERD and CoNLL selection experiment data from the registry JSON and check the AUROC output file on the server.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "12887522-0af9-4d9b-aeb3-1b17f220fe3d",
  "isSidechain": false,
  "requestId": "req_011CbC3PJSNPif73s235HQ8a",
  "type": "assistant",
  "uuid": "d74cfe39-fbd4-4e00-bbd3-d20a4a0fb765",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "a97de670-f9a7-4d30-affd-382982b8a334",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HS1cRDesWf8sqJWscz1wJh",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5011,
      "cache_read_input_tokens": 43364,
      "output_tokens": 1688,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5011,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1688,
          "cache_read_input_tokens": 43364,
          "cache_creation_input_tokens": 5011,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5011
          },
          "type": "message"
        }
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

_source line 35 · 2026-05-19T13:55:31.551Z_

Found the AUROC script — binarization at F1 >= 1.0 (perfect extraction). Now let me extract the specific experiments from the registry and check the actual AUROC output files on the server.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d74cfe39-fbd4-4e00-bbd3-d20a4a0fb765",
  "isSidechain": false,
  "requestId": "req_011CbC3PJSNPif73s235HQ8a",
  "type": "assistant",
  "uuid": "cf76f9b8-e5d9-465b-96cc-7f7fe5148a8b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "a97de670-f9a7-4d30-affd-382982b8a334",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HS1cRDesWf8sqJWscz1wJh",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5011,
      "cache_read_input_tokens": 43364,
      "output_tokens": 1688,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5011,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1688,
          "cache_read_input_tokens": 43364,
          "cache_creation_input_tokens": 5011,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5011
          },
          "type": "message"
        }
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

_source line 36 · 2026-05-19T13:55:37.226Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01XWUmEEo6fzNv3mVUMPURg4`</summary>

```json
{
  "command": "REGFILE=\"/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie/a97de670-f9a7-4d30-affd-382982b8a334/tool-results/mcp-agent-ml-research-read_registry-1779198876363.txt\"\npython3 -c \"\nimport json, sys\ndata = json.loads(json.loads(open('$REGFILE').read())['result'])\nexps = data['data']['experiments']\n\n# Extract exp_012_rerun_1024 metrics\nexp = exps.get('exp_012_rerun_1024', {})\nprint('=== exp_012_rerun_1024 ===')\nprint(json.dumps(exp.get('metrics', {}), indent=2)[:5000])\nprint()\n\n# Extract exp_015_v2 metrics (provenance says AUROC from here)\nexp2 = exps.get('exp_015_v2', {})\nprint('=== exp_015_v2 ===')\nprint(json.dumps(exp2.get('metrics', {}), indent=2)[:5000])\n\"\n",
  "description": "Extract exp_012 and exp_015_v2 metrics from registry"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cf76f9b8-e5d9-465b-96cc-7f7fe5148a8b",
  "isSidechain": false,
  "requestId": "req_011CbC3PJSNPif73s235HQ8a",
  "type": "assistant",
  "uuid": "2940749b-9140-421f-aedf-6ea7bffa9c33",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "a97de670-f9a7-4d30-affd-382982b8a334",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HS1cRDesWf8sqJWscz1wJh",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5011,
      "cache_read_input_tokens": 43364,
      "output_tokens": 1688,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5011,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1688,
          "cache_read_input_tokens": 43364,
          "cache_creation_input_tokens": 5011,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5011
          },
          "type": "message"
        }
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

_source line 37 · 2026-05-19T13:55:48.811Z_

<details><summary>↩ Tool result · `toolu_015wPJYd1cyoQo9fdMQfYSJR`</summary>

```text
exp_002:
  N=None
  {
  "logprob_rho_full": 0.3157,
  "logprob_tau_full": 0.2469,
  "logprob_auroc_full": 0.7532,
  "logprob_rho_cond": 0.3562,
  "sj_vs_logprob_delta_rho": 0.12,
  "sj_vs_logprob_ci_low": 0.0881,
  "sj_vs_logprob_ci_high": 0.154,
  "sj_vs_logprob_significant": true
}

exp_002_conll_n16:
  N=None
  {
  "degen_rate": 0.4844,
  "degen_rate_source": "unified_metrics_constant_f1_gold_filtered"
}

exp_002_conll_n16_seed123:
  N=None
  {
  "degen_rate": 0.471,
  "degen_rate_source": "unified_metrics_constant_f1_gold_filtered"
}

exp_002_conll_n16_seed456:
  N=None
  {
  "degen_rate": 0.5544,
  "degen_rate_source": "unified_metrics_constant_f1_gold_filtered"
}

exp_011_ood_scierc_to_conll:
  N=None
  {
  "rho_lp": 0.246
}

exp_017_llama_conll:
  N=None
  {
  "degeneracy_cf1_gold_filtered": 0.894,
  "dgs_nondegen_lp_delta_pp": 1.37,
  "selection_f1": {
    "SJ": {
      "f1": 0.9237,
      "delta_pp": -0.04
    },
    "FK": {
      "f1": 0.924,
      "delta_pp": -0.02
    },
    "VC": {
      "f1": 0.925,
      "delta_pp": 0.08
    },
    "EM": {
      "f1": 0.9244,
      "delta_pp": 0.02
    },
    "LP": {
      "f1": 0.9244,
      "delta_pp": 0.02
    }
  },
  "lp_range": {
    "mean": 0.0198,
    "std": 0.0315,
    "median": 0.0002
  }
}

exp_017_llama_conll_finetune:
  N=None
  {
  "degeneracy_rate": 0.853,
  "selection_f1": 0.934,
  "full_rho_LP": 0.273,
  "full_AUROC_LP": 0.739,
  "cond_rho_LP": 0.311,
  "cond_AUROC_LP": 0.804
}

exp_017_llama_conll_n16_r1024:
  N=None
  {
  "degen_rate": 0.8647,
  "degen_rate_source": "unified_metrics_constant_f1_gold_filtered",
  "rho_lp_ner": 0.3136,
  "auroc_lp_ner": 0.7661
}

exp_017_llama_conll_n16_s123_r1024:
  N=None
  {
  "degen_rate": 0.8636,
  "degen_rate_source": "unified_metrics_constant_f1_gold_filtered"
}

exp_017_llama_conll_n16_s456_r1024:
  N=None
  {
  "degen_rate": 0.8672,
  "degen_rate_source": "unified_metrics_constant_f1_gold_filtered",
  "rho_lp_ner": 0.3099,
  "auroc_lp_ner": 0.7628
}

exp_017_llama_conll_n8_t07:
  N=None
  {
  "lp_range_median": 1.1e-05,
  "lp_tied_fraction_005": 0.9579,
  "selection_f1": {
    "SJ": 0.9247,
    "FK": 0.9254,
    "VC": 0.9264,
    "EM": 0.9255,
    "LP": 0.9248
  }
}

exp_freeform_conll_4seed:
  N=None
  {
  "lp_range_median": "0.0581\u00b10.0072",
  "rho_lp": "0.3262\u00b10.0120",
  "sel_f1_lp": "0.8958\u00b10.0009"
}

exp_qwen3_4b_conll_scs_inference:
  N=None
  {
  "degen_rate": 0.9057,
  "degen_rate_source": "unified_metrics_constant_f1_gold_filtered",
  "LP_rho_full": 0.3186,
  "LP_rho_cond": 0.3378,
  "LP_auroc_full": 0.7689,
  "LP_auroc_cond": 0.8153
}

exp_qwen3_4b_conll_scs_inference_v2:
  N=None
  {
  "degen_rate": 0.9057,
  "degen_rate_source": "unified_metrics_constant_f1_gold_filtered",
  "LP_rho_full": 0.3313,
  "LP_rho_cond": 0.3487,
  "LP_auroc_full": 0.7761,
  "LP_auroc_cond": 0.8209
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9f2df859-97fe-4163-88ad-f6745b0109fc",
  "isSidechain": false,
  "promptId": "0731b9be-f5e6-4a8a-9a3c-2edafe06629b",
  "type": "user",
  "uuid": "c2e67c47-4a1f-46ad-89a5-4aa7a45d0735",
  "toolUseResult": {
    "stdout": "exp_002:\n  N=None\n  {\n  \"logprob_rho_full\": 0.3157,\n  \"logprob_tau_full\": 0.2469,\n  \"logprob_auroc_full\": 0.7532,\n  \"logprob_rho_cond\": 0.3562,\n  \"sj_vs_logprob_delta_rho\": 0.12,\n  \"sj_vs_logprob_ci_low\": 0.0881,\n  \"sj_vs_logprob_ci_high\": 0.154,\n  \"sj_vs_logprob_significant\": true\n}\n\nexp_002_conll_n16:\n  N=None\n  {\n  \"degen_rate\": 0.4844,\n  \"degen_rate_source\": \"unified_metrics_constant_f1_gold_filtered\"\n}\n\nexp_002_conll_n16_seed123:\n  N=None\n  {\n  \"degen_rate\": 0.471,\n  \"degen_rate_source\": \"unified_metrics_constant_f1_gold_filtered\"\n}\n\nexp_002_conll_n16_seed456:\n  N=None\n  {\n  \"degen_rate\": 0.5544,\n  \"degen_rate_source\": \"unified_metrics_constant_f1_gold_filtered\"\n}\n\nexp_011_ood_scierc_to_conll:\n  N=None\n  {\n  \"rho_lp\": 0.246\n}\n\nexp_017_llama_conll:\n  N=None\n  {\n  \"degeneracy_cf1_gold_filtered\": 0.894,\n  \"dgs_nondegen_lp_delta_pp\": 1.37,\n  \"selection_f1\": {\n    \"SJ\": {\n      \"f1\": 0.9237,\n      \"delta_pp\": -0.04\n    },\n    \"FK\": {\n      \"f1\": 0.924,\n      \"delta_pp\": -0.02\n    },\n    \"VC\": {\n      \"f1\": 0.925,\n      \"delta_pp\": 0.08\n    },\n    \"EM\": {\n      \"f1\": 0.9244,\n      \"delta_pp\": 0.02\n    },\n    \"LP\": {\n      \"f1\": 0.9244,\n      \"delta_pp\": 0.02\n    }\n  },\n  \"lp_range\": {\n    \"mean\": 0.0198,\n    \"std\": 0.0315,\n    \"median\": 0.0002\n  }\n}\n\nexp_017_llama_conll_finetune:\n  N=None\n  {\n  \"degeneracy_rate\": 0.853,\n  \"selection_f1\": 0.934,\n  \"full_rho_LP\": 0.273,\n  \"full_AUROC_LP\": 0.739,\n  \"cond_rho_LP\": 0.311,\n  \"cond_AUROC_LP\": 0.804\n}\n\nexp_017_llama_conll_n16_r1024:\n  N=None\n  {\n  \"degen_rate\": 0.8647,\n  \"degen_rate_source\": \"unified_metrics_constant_f1_gold_filtered\",\n  \"rho_lp_ner\": 0.3136,\n  \"auroc_lp_ner\": 0.7661\n}\n\nexp_017_llama_conll_n16_s123_r1024:\n  N=None\n  {\n  \"degen_rate\": 0.8636,\n  \"degen_rate_source\": \"unified_metrics_constant_f1_gold_filtered\"\n}\n\nexp_017_llama_conll_n16_s456_r1024:\n  N=None\n  {\n  \"degen_rate\": 0.8672,\n  \"degen_rate_source\": \"unified_metrics_constant_f1_gold_filtered\",\n  \"rho_lp_ner\": 0.3099,\n  \"auroc_lp_ner\": 0.7628\n}\n\nexp_017_llama_conll_n8_t07:\n  N=None\n  {\n  \"lp_range_median\": 1.1e-05,\n  \"lp_tied_fraction_005\": 0.9579,\n  \"selection_f1\": {\n    \"SJ\": 0.9247,\n    \"FK\": 0.9254,\n    \"VC\": 0.9264,\n    \"EM\": 0.9255,\n    \"LP\": 0.9248\n  }\n}\n\nexp_freeform_conll_4seed:\n  N=None\n  {\n  \"lp_range_median\": \"0.0581\\u00b10.0072\",\n  \"rho_lp\": \"0.3262\\u00b10.0120\",\n  \"sel_f1_lp\": \"0.8958\\u00b10.0009\"\n}\n\nexp_qwen3_4b_conll_scs_inference:\n  N=None\n  {\n  \"degen_rate\": 0.9057,\n  \"degen_rate_source\": \"unified_metrics_constant_f1_gold_filtered\",\n  \"LP_rho_full\": 0.3186,\n  \"LP_rho_cond\": 0.3378,\n  \"LP_auroc_full\": 0.7689,\n  \"LP_auroc_cond\": 0.8153\n}\n\nexp_qwen3_4b_conll_scs_inference_v2:\n  N=None\n  {\n  \"degen_rate\": 0.9057,\n  \"degen_rate_source\": \"unified_metrics_constant_f1_gold_filtered\",\n  \"LP_rho_full\": 0.3313,\n  \"LP_rho_cond\": 0.3487,\n  \"LP_auroc_full\": 0.7761,\n  \"LP_auroc_cond\": 0.8209\n}",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "9f2df859-97fe-4163-88ad-f6745b0109fc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "a97de670-f9a7-4d30-affd-382982b8a334",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-19T13:55:37.310Z_

<details><summary>↩ Tool result · `toolu_01XWUmEEo6fzNv3mVUMPURg4`</summary>

```text
=== exp_012_rerun_1024 ===
{
  "degen_rate": 0.1777,
  "degen_rate_source": "unified_metrics_constant_f1_gold_filtered",
  "ner_full": {
    "n": 529,
    "SJ": {
      "rho": 0.3599,
      "tau": 0.2646,
      "AUROC": 0.6917,
      "ECE": 0.4531,
      "rho_ci95": [
        0.2732,
        0.4389
      ],
      "AUROC_ci95": [
        0.6304,
        0.7406
      ]
    },
    "FK": {
      "rho": 0.2665,
      "tau": 0.1974,
      "AUROC": 0.629,
      "ECE": 0.4512,
      "rho_ci95": [
        0.1743,
        0.3486
      ],
      "AUROC_ci95": [
        0.5612,
        0.6882
      ]
    },
    "logprob": {
      "rho": 0.2052,
      "tau": 0.1478,
      "AUROC": 0.5783,
      "ECE": 0.7064,
      "rho_ci95": [
        0.1171,
        0.2904
      ],
      "AUROC_ci95": [
        0.5179,
        0.6387
      ]
    },
    "EM": {
      "rho": 0.2945,
      "tau": 0.2208,
      "AUROC": 0.7493,
      "ECE": 0.3526,
      "rho_ci95": [
        0.2094,
        0.37
      ],
      "AUROC_ci95": [
        0.7002,
        0.7928
      ]
    },
    "voting_conf": {
      "rho": 0.3792,
      "tau": 0.2805,
      "AUROC": 0.6841,
      "ECE": 0.3807,
      "rho_ci95": [
        0.2972,
        0.4486
      ],
      "AUROC_ci95": [
        0.6249,
        0.7366
      ]
    }
  },
  "ner_cond": {
    "n": 477,
    "SJ": {
      "rho": 0.3113,
      "tau": 0.2257,
      "AUROC": 0.6772,
      "ECE": 0.4416,
      "rho_ci95": [
        0.2353,
        0.3959
      ],
      "AUROC_ci95": [
        0.621,
        0.7337
      ]
    },
    "FK": {
      "rho": 0.1761,
      "tau": 0.1284,
      "AUROC": 0.6078,
      "ECE": 0.4389,
      "rho_ci95": [
        0.0839,
        0.2665
      ],
      "AUROC_ci95": [
        0.5442,
        0.6709
      ]
    },
    "logprob": {
      "rho": 0.1538,
      "tau": 0.1111,
      "AUROC": 0.5633,
      "ECE": 0.6803,
      "rho_ci95": [
        0.0637,
        0.2424
      ],
      "AUROC_ci95": [
        0.5032,
        0.6232
      ]
    },
    "EM": {
      "rho": 0.3596,
      "tau": 0.2735,
      "AUROC": 0.7556,
      "ECE": 0.3257,
      "rho_ci95": [
        0.2819,
        0.4408
      ],
      "AUROC_ci95": [
        0.7011,
        0.8107
      ]
    },
    "voting_conf": {
      "rho": 0.3,
      "tau": 0.2189,
      "AUROC": 0.6618,
      "ECE": 0.3746,
      "rho_ci95": [
        0.2168,
        0.3836
      ],
      "AUROC_ci95": [
        0.6004,
        0.7201
      ]
    }
  },
  "re_full": {
    "n": 397,
    "SJ": {
      "rho": 0.2503,
      "tau": 0.1878,
      "AUROC": 0.6702,
      "ECE": 0.3865
    },
    "FK": {
      "rho": 0.2752,
      "tau": 0.2117,
      "AUROC": 0.6089,
      "ECE": 0.4405
    },
    "logprob": {
      "rho": 0.2662,
      "tau": 0.1951,
      "AUROC": 0.6005,
      "ECE": 0.7694
    },
    "EM": {
      "rho": 0.1344,
      "tau": 0.1081,
      "AUROC": 0.7059,
      "ECE": 0.3548
    },
    "voting_conf": {
      "rho": 0.3498,
      "tau": 0.2663,
      "AUROC": 0.6935,
      "ECE": 0.2724
    }
  },
  "re_cond": {
    "n": 238,
    "SJ": {
      "rho": 0.2457,
      "tau": 0.1811,
      "AUROC": 0.6463,
      "ECE": 0.2941
    },
    "FK": {
      "rho": 0.1139,
      "tau": 0.0876,
      "AUROC": 0.551,
      "ECE": 0.3424
    },
    "logprob": {
      "rho": 0.0112,
      "tau": 0.0051,
      "AUROC": 0.5186,
      "ECE": 0.6464
    },
    "EM": {
      "rho": 0.4165,
      "tau": 0.3256,
      "AUROC": 0.7515,
      "ECE": 0.2232
    },
    "voting_conf": {
      "rho": 0.2409,
      "tau": 0.178,
      "AUROC": 0.642,
      "ECE": 0.207
    }
  },
  "delta_vs_512_ner_full_rho": {
    "SJ": 0.0034,
    "FK": 0.0014,
    "EM": 0.0379,
    "voting_conf": -0.1226,
    "logprob": 0.0656
  },
  "provenance_note": "exp_015_v2 scierc_n8_logprob used exp_012_logprob (max_tokens=512 truncated data). voting_conf was inflated 0.502\u21920.379, logprob was suppressed 0.140\u21920.205."
}

=== exp_015_v2 ===
{
  "scierc_ner_avg": {
    "sj_auroc": 0.7394,
    "fk_auroc": 0.6172,
    "em_auroc": 0.7873,
    "voting_auroc": 0.7367,
    "logprob_auroc": 0.5918
  },
  "scierc_re_avg": {
    "sj_auroc": 0.6746,
    "fk_auroc": 0.5939,
    "em_auroc": 0.715,
    "voting_auroc": 0.7234,
    "logprob_auroc": 0.5849
  }
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2940749b-9140-421f-aedf-6ea7bffa9c33",
  "isSidechain": false,
  "promptId": "0731b9be-f5e6-4a8a-9a3c-2edafe06629b",
  "type": "user",
  "uuid": "b3051ca5-16f7-4f09-8a99-aa219e9a29a1",
  "toolUseResult": {
    "stdout": "=== exp_012_rerun_1024 ===\n{\n  \"degen_rate\": 0.1777,\n  \"degen_rate_source\": \"unified_metrics_constant_f1_gold_filtered\",\n  \"ner_full\": {\n    \"n\": 529,\n    \"SJ\": {\n      \"rho\": 0.3599,\n      \"tau\": 0.2646,\n      \"AUROC\": 0.6917,\n      \"ECE\": 0.4531,\n      \"rho_ci95\": [\n        0.2732,\n        0.4389\n      ],\n      \"AUROC_ci95\": [\n        0.6304,\n        0.7406\n      ]\n    },\n    \"FK\": {\n      \"rho\": 0.2665,\n      \"tau\": 0.1974,\n      \"AUROC\": 0.629,\n      \"ECE\": 0.4512,\n      \"rho_ci95\": [\n        0.1743,\n        0.3486\n      ],\n      \"AUROC_ci95\": [\n        0.5612,\n        0.6882\n      ]\n    },\n    \"logprob\": {\n      \"rho\": 0.2052,\n      \"tau\": 0.1478,\n      \"AUROC\": 0.5783,\n      \"ECE\": 0.7064,\n      \"rho_ci95\": [\n        0.1171,\n        0.2904\n      ],\n      \"AUROC_ci95\": [\n        0.5179,\n        0.6387\n      ]\n    },\n    \"EM\": {\n      \"rho\": 0.2945,\n      \"tau\": 0.2208,\n      \"AUROC\": 0.7493,\n      \"ECE\": 0.3526,\n      \"rho_ci95\": [\n        0.2094,\n        0.37\n      ],\n      \"AUROC_ci95\": [\n        0.7002,\n        0.7928\n      ]\n    },\n    \"voting_conf\": {\n      \"rho\": 0.3792,\n      \"tau\": 0.2805,\n      \"AUROC\": 0.6841,\n      \"ECE\": 0.3807,\n      \"rho_ci95\": [\n        0.2972,\n        0.4486\n      ],\n      \"AUROC_ci95\": [\n        0.6249,\n        0.7366\n      ]\n    }\n  },\n  \"ner_cond\": {\n    \"n\": 477,\n    \"SJ\": {\n      \"rho\": 0.3113,\n      \"tau\": 0.2257,\n      \"AUROC\": 0.6772,\n      \"ECE\": 0.4416,\n      \"rho_ci95\": [\n        0.2353,\n        0.3959\n      ],\n      \"AUROC_ci95\": [\n        0.621,\n        0.7337\n      ]\n    },\n    \"FK\": {\n      \"rho\": 0.1761,\n      \"tau\": 0.1284,\n      \"AUROC\": 0.6078,\n      \"ECE\": 0.4389,\n      \"rho_ci95\": [\n        0.0839,\n        0.2665\n      ],\n      \"AUROC_ci95\": [\n        0.5442,\n        0.6709\n      ]\n    },\n    \"logprob\": {\n      \"rho\": 0.1538,\n      \"tau\": 0.1111,\n      \"AUROC\": 0.5633,\n      \"ECE\": 0.6803,\n      \"rho_ci95\": [\n        0.0637,\n        0.2424\n      ],\n      \"AUROC_ci95\": [\n        0.5032,\n        0.6232\n      ]\n    },\n    \"EM\": {\n      \"rho\": 0.3596,\n      \"tau\": 0.2735,\n      \"AUROC\": 0.7556,\n      \"ECE\": 0.3257,\n      \"rho_ci95\": [\n        0.2819,\n        0.4408\n      ],\n      \"AUROC_ci95\": [\n        0.7011,\n        0.8107\n      ]\n    },\n    \"voting_conf\": {\n      \"rho\": 0.3,\n      \"tau\": 0.2189,\n      \"AUROC\": 0.6618,\n      \"ECE\": 0.3746,\n      \"rho_ci95\": [\n        0.2168,\n        0.3836\n      ],\n      \"AUROC_ci95\": [\n        0.6004,\n        0.7201\n      ]\n    }\n  },\n  \"re_full\": {\n    \"n\": 397,\n    \"SJ\": {\n      \"rho\": 0.2503,\n      \"tau\": 0.1878,\n      \"AUROC\": 0.6702,\n      \"ECE\": 0.3865\n    },\n    \"FK\": {\n      \"rho\": 0.2752,\n      \"tau\": 0.2117,\n      \"AUROC\": 0.6089,\n      \"ECE\": 0.4405\n    },\n    \"logprob\": {\n      \"rho\": 0.2662,\n      \"tau\": 0.1951,\n      \"AUROC\": 0.6005,\n      \"ECE\": 0.7694\n    },\n    \"EM\": {\n      \"rho\": 0.1344,\n      \"tau\": 0.1081,\n      \"AUROC\": 0.7059,\n      \"ECE\": 0.3548\n    },\n    \"voting_conf\": {\n      \"rho\": 0.3498,\n      \"tau\": 0.2663,\n      \"AUROC\": 0.6935,\n      \"ECE\": 0.2724\n    }\n  },\n  \"re_cond\": {\n    \"n\": 238,\n    \"SJ\": {\n      \"rho\": 0.2457,\n      \"tau\": 0.1811,\n      \"AUROC\": 0.6463,\n      \"ECE\": 0.2941\n    },\n    \"FK\": {\n      \"rho\": 0.1139,\n      \"tau\": 0.0876,\n      \"AUROC\": 0.551,\n      \"ECE\": 0.3424\n    },\n    \"logprob\": {\n      \"rho\": 0.0112,\n      \"tau\": 0.0051,\n      \"AUROC\": 0.5186,\n      \"ECE\": 0.6464\n    },\n    \"EM\": {\n      \"rho\": 0.4165,\n      \"tau\": 0.3256,\n      \"AUROC\": 0.7515,\n      \"ECE\": 0.2232\n    },\n    \"voting_conf\": {\n      \"rho\": 0.2409,\n      \"tau\": 0.178,\n      \"AUROC\": 0.642,\n      \"ECE\": 0.207\n    }\n  },\n  \"delta_vs_512_ner_full_rho\": {\n    \"SJ\": 0.0034,\n    \"FK\": 0.0014,\n    \"EM\": 0.0379,\n    \"voting_conf\": -0.1226,\n    \"logprob\": 0.0656\n  },\n  \"provenance_note\": \"exp_015_v2 scierc_n8_logprob used exp_012_logprob (max_tokens=512 truncated data). voting_conf was inflated 0.502\\u21920.379, logprob was suppressed 0.140\\u21920.205.\"\n}\n\n=== exp_015_v2 ===\n{\n  \"scierc_ner_avg\": {\n    \"sj_auroc\": 0.7394,\n    \"fk_auroc\": 0.6172,\n    \"em_auroc\": 0.7873,\n    \"voting_auroc\": 0.7367,\n    \"logprob_auroc\": 0.5918\n  },\n  \"scierc_re_avg\": {\n    \"sj_auroc\": 0.6746,\n    \"fk_auroc\": 0.5939,\n    \"em_auroc\": 0.715,\n    \"voting_auroc\": 0.7234,\n    \"logprob_auroc\": 0.5849\n  }\n}",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "2940749b-9140-421f-aedf-6ea7bffa9c33",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "a97de670-f9a7-4d30-affd-382982b8a334",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-19T13:55:38.876Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01FgiTYxCQob4RRtPzSMWkag`</summary>

```json
{
  "server": "autodl-5090",
  "command": "cat /root/autodl-tmp/struct_self_consist_ie/output/exp_012_rerun_1024/auroc_5signal.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b3051ca5-16f7-4f09-8a99-aa219e9a29a1",
  "isSidechain": false,
  "requestId": "req_011CbC3PJSNPif73s235HQ8a",
  "type": "assistant",
  "uuid": "1fe5f098-f2c0-4af0-a7c8-e32b9ba16bdc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "a97de670-f9a7-4d30-affd-382982b8a334",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HS1cRDesWf8sqJWscz1wJh",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5011,
      "cache_read_input_tokens": 43364,
      "output_tokens": 1688,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5011,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1688,
          "cache_read_input_tokens": 43364,
          "cache_creation_input_tokens": 5011,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5011
          },
          "type": "message"
        }
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

_source line 40 · 2026-05-19T13:55:39.255Z_

<details><summary>↩ Tool result · `toolu_01FgiTYxCQob4RRtPzSMWkag`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"ner\\\": {\\n    \\\"n_total\\\": 551,\\n    \\\"n_valid\\\": 529,\\n    \\\"n_conditional\\\": 477,\\n    \\\"full\\\": {\\n      \\\"n\\\": 529,\\n      \\\"n_pos\\\": 132,\\n      \\\"n_neg\\\": 397,\\n      \\\"auroc_sj\\\": 0.691741,\\n      \\\"auroc_fk\\\": 0.628998,\\n      \\\"auroc_logprob\\\": 0.578334,\\n      \\\"auroc_em\\\": 0.749265,\\n      \\\"auroc_voting_conf\\\": 0.684099\\n    },\\n    \\\"cond\\\": {\\n      \\\"n\\\": 477,\\n      \\\"n_pos\\\": 132,\\n      \\\"n_neg\\\": 345,\\n      \\\"auroc_sj\\\": 0.677163,\\n      \\\"auroc_fk\\\": 0.607839,\\n      \\\"auroc_logprob\\\": 0.563329,\\n      \\\"auroc_em\\\": 0.755578,\\n      \\\"auroc_voting_conf\\\": 0.661814\\n    }\\n  },\\n  \\\"re\\\": {\\n    \\\"n_total\\\": 551,\\n    \\\"n_valid\\\": 397,\\n    \\\"n_conditional\\\": 238,\\n    \\\"full\\\": {\\n      \\\"n\\\": 397,\\n      \\\"n_pos\\\": 76,\\n      \\\"n_neg\\\": 321,\\n      \\\"auroc_sj\\\": 0.670233,\\n      \\\"auroc_fk\\\": 0.608932,\\n      \\\"auroc_logprob\\\": 0.600467,\\n      \\\"auroc_em\\\": 0.705853,\\n      \\\"auroc_voting_conf\\\": 0.693474\\n    },\\n    \\\"cond\\\": {\\n      \\\"n\\\": 238,\\n      \\\"n_pos\\\": 76,\\n      \\\"n_neg\\\": 162,\\n      \\\"auroc_sj\\\": 0.64628,\\n      \\\"auroc_fk\\\": 0.551048,\\n      \\\"auroc_logprob\\\": 0.5186,\\n      \\\"auroc_em\\\": 0.751462,\\n      \\\"auroc_voting_conf\\\": 0.641975\\n    }\\n  }\\n}\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.36}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1fe5f098-f2c0-4af0-a7c8-e32b9ba16bdc",
  "isSidechain": false,
  "promptId": "0731b9be-f5e6-4a8a-9a3c-2edafe06629b",
  "type": "user",
  "uuid": "ae2853f3-6857-4f12-ae15-313bad321da8",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"{\\\\n  \\\\\\\"ner\\\\\\\": {\\\\n    \\\\\\\"n_total\\\\\\\": 551,\\\\n    \\\\\\\"n_valid\\\\\\\": 529,\\\\n    \\\\\\\"n_conditional\\\\\\\": 477,\\\\n    \\\\\\\"full\\\\\\\": {\\\\n      \\\\\\\"n\\\\\\\": 529,\\\\n      \\\\\\\"n_pos\\\\\\\": 132,\\\\n      \\\\\\\"n_neg\\\\\\\": 397,\\\\n      \\\\\\\"auroc_sj\\\\\\\": 0.691741,\\\\n      \\\\\\\"auroc_fk\\\\\\\": 0.628998,\\\\n      \\\\\\\"auroc_logprob\\\\\\\": 0.578334,\\\\n      \\\\\\\"auroc_em\\\\\\\": 0.749265,\\\\n      \\\\\\\"auroc_voting_conf\\\\\\\": 0.684099\\\\n    },\\\\n    \\\\\\\"cond\\\\\\\": {\\\\n      \\\\\\\"n\\\\\\\": 477,\\\\n      \\\\\\\"n_pos\\\\\\\": 132,\\\\n      \\\\\\\"n_neg\\\\\\\": 345,\\\\n      \\\\\\\"auroc_sj\\\\\\\": 0.677163,\\\\n      \\\\\\\"auroc_fk\\\\\\\": 0.607839,\\\\n      \\\\\\\"auroc_logprob\\\\\\\": 0.563329,\\\\n      \\\\\\\"auroc_em\\\\\\\": 0.755578,\\\\n      \\\\\\\"auroc_voting_conf\\\\\\\": 0.661814\\\\n    }\\\\n  },\\\\n  \\\\\\\"re\\\\\\\": {\\\\n    \\\\\\\"n_total\\\\\\\": 551,\\\\n    \\\\\\\"n_valid\\\\\\\": 397,\\\\n    \\\\\\\"n_conditional\\\\\\\": 238,\\\\n    \\\\\\\"full\\\\\\\": {\\\\n      \\\\\\\"n\\\\\\\": 397,\\\\n      \\\\\\\"n_pos\\\\\\\": 76,\\\\n      \\\\\\\"n_neg\\\\\\\": 321,\\\\n      \\\\\\\"auroc_sj\\\\\\\": 0.670233,\\\\n      \\\\\\\"auroc_fk\\\\\\\": 0.608932,\\\\n      \\\\\\\"auroc_logprob\\\\\\\": 0.600467,\\\\n      \\\\\\\"auroc_em\\\\\\\": 0.705853,\\\\n      \\\\\\\"auroc_voting_conf\\\\\\\": 0.693474\\\\n    },\\\\n    \\\\\\\"cond\\\\\\\": {\\\\n      \\\\\\\"n\\\\\\\": 238,\\\\n      \\\\\\\"n_pos\\\\\\\": 76,\\\\n      \\\\\\\"n_neg\\\\\\\": 162,\\\\n      \\\\\\\"auroc_sj\\\\\\\": 0.64628,\\\\n      \\\\\\\"auroc_fk\\\\\\\": 0.551048,\\\\n      \\\\\\\"auroc_logprob\\\\\\\": 0.5186,\\\\n      \\\\\\\"auroc_em\\\\\\\": 0.751462,\\\\n      \\\\\\\"auroc_voting_conf\\\\\\\": 0.641975\\\\n    }\\\\n  }\\\\n}\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.36}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"ner\\\": {\\n    \\\"n_total\\\": 551,\\n    \\\"n_valid\\\": 529,\\n    \\\"n_conditional\\\": 477,\\n    \\\"full\\\": {\\n      \\\"n\\\": 529,\\n      \\\"n_pos\\\": 132,\\n      \\\"n_neg\\\": 397,\\n      \\\"auroc_sj\\\": 0.691741,\\n      \\\"auroc_fk\\\": 0.628998,\\n      \\\"auroc_logprob\\\": 0.578334,\\n      \\\"auroc_em\\\": 0.749265,\\n      \\\"auroc_voting_conf\\\": 0.684099\\n    },\\n    \\\"cond\\\": {\\n      \\\"n\\\": 477,\\n      \\\"n_pos\\\": 132,\\n      \\\"n_neg\\\": 345,\\n      \\\"auroc_sj\\\": 0.677163,\\n      \\\"auroc_fk\\\": 0.607839,\\n      \\\"auroc_logprob\\\": 0.563329,\\n      \\\"auroc_em\\\": 0.755578,\\n      \\\"auroc_voting_conf\\\": 0.661814\\n    }\\n  },\\n  \\\"re\\\": {\\n    \\\"n_total\\\": 551,\\n    \\\"n_valid\\\": 397,\\n    \\\"n_conditional\\\": 238,\\n    \\\"full\\\": {\\n      \\\"n\\\": 397,\\n      \\\"n_pos\\\": 76,\\n      \\\"n_neg\\\": 321,\\n      \\\"auroc_sj\\\": 0.670233,\\n      \\\"auroc_fk\\\": 0.608932,\\n      \\\"auroc_logprob\\\": 0.600467,\\n      \\\"auroc_em\\\": 0.705853,\\n      \\\"auroc_voting_conf\\\": 0.693474\\n    },\\n    \\\"cond\\\": {\\n      \\\"n\\\": 238,\\n      \\\"n_pos\\\": 76,\\n      \\\"n_neg\\\": 162,\\n      \\\"auroc_sj\\\": 0.64628,\\n      \\\"auroc_fk\\\": 0.551048,\\n      \\\"auroc_logprob\\\": 0.5186,\\n      \\\"auroc_em\\\": 0.751462,\\n      \\\"auroc_voting_conf\\\": 0.641975\\n    }\\n  }\\n}\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.36}}"
    }
  },
  "sourceToolAssistantUUID": "1fe5f098-f2c0-4af0-a7c8-e32b9ba16bdc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "a97de670-f9a7-4d30-affd-382982b8a334",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-19T13:55:43.939Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01ER2HkcHnDimsvEgfN5s6xJ`</summary>

```json
{
  "command": "REGFILE=\"/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie/a97de670-f9a7-4d30-affd-382982b8a334/tool-results/mcp-agent-ml-research-read_registry-1779198876363.txt\"\npython3 -c \"\nimport json\ndata = json.loads(json.loads(open('$REGFILE').read())['result'])\nexps = data['data']['experiments']\n\n# FewNERD experiments\nfor eid in sorted(exps.keys()):\n    if 'fewnerd' in eid.lower() or 'few_nerd' in eid.lower():\n        exp = exps[eid]\n        m = exp.get('metrics', {})\n        # Look for degen_rate or degeneracy\n        degen_keys = [k for k in m.keys() if 'degen' in k.lower()]\n        if degen_keys:\n            print(f'{eid}: {json.dumps({k: m[k] for k in degen_keys})}')\n        # Also check config for N value\n        c = exp.get('config', {})\n        n_val = c.get('N') or c.get('n_samples') or c.get('n')\n        status = exp.get('status', '')\n        print(f'  status={status}, N={n_val}, metrics_keys={list(m.keys())[:15]}')\n        print()\n\"\n",
  "description": "Extract FewNERD degeneracy data from registry"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ae2853f3-6857-4f12-ae15-313bad321da8",
  "isSidechain": false,
  "requestId": "req_011CbC3PJSNPif73s235HQ8a",
  "type": "assistant",
  "uuid": "257c54a5-8fbf-47d6-be4a-4d463b5d0101",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "a97de670-f9a7-4d30-affd-382982b8a334",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HS1cRDesWf8sqJWscz1wJh",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5011,
      "cache_read_input_tokens": 43364,
      "output_tokens": 1688,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5011,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1688,
          "cache_read_input_tokens": 43364,
          "cache_creation_input_tokens": 5011,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5011
          },
          "type": "message"
        }
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

_source line 42 · 2026-05-19T13:55:44.015Z_

<details><summary>↩ Tool result · `toolu_01ER2HkcHnDimsvEgfN5s6xJ`</summary>

```text
  status=DONE, N=None, metrics_keys=['final_loss', 'total_steps', 'training_time', 'pilot_greedy_f1', 'pilot_instances', 'merged_model_path']

exp_021_fewnerd_full: {"degeneracy_rate": 0.101}
  status=DONE, N=None, metrics_keys=['total_steps', 'train_loss', 'eval_loss', 'train_runtime', 'epochs', 'final_checkpoint', 'adapter_path', 'inference_instances', 'inference_filtered', 'inference_n_samples', 'greedy_macro_f1', 'oracle_macro_f1', 'headroom', 'zero_f1_rate', 'degeneracy_rate']

exp_021_fewnerd_n8_seed123: {"degen_rate": 0.1312, "degen_rate_source": "unified_metrics_constant_f1_gold_filtered"}
  status=DONE, N=None, metrics_keys=['degen_rate', 'degen_rate_source', 'instance_count', 'n_valid', 'n_gold_empty', 'ner_greedy_f1', 'ner_oracle_f1', 'rho_fk_ner', 'rho_sj_ner', 'sample_f1_pct_zero']

exp_021_fewnerd_n8_seed456: {"degen_rate": 0.1212, "degen_rate_source": "unified_metrics_constant_f1_gold_filtered"}
  status=DONE, N=None, metrics_keys=['degen_rate', 'degen_rate_source', 'instance_count', 'n_valid', 'n_gold_empty', 'ner_greedy_f1', 'ner_oracle_f1', 'rho_fk_ner', 'rho_sj_ner', 'sample_f1_pct_zero']

exp_027_fewnerd_n16: {"degen_rate": 0.0706, "degen_rate_source": "unified_metrics_constant_f1_gold_filtered"}
  status=DONE, N=None, metrics_keys=['LP_delta_pp', 'LP_delta_95CI', 'degen_rate', 'degen_rate_source', 'greedy_f1', 'lp_sel_f1', 'oracle_f1', 'headroom_pp', 'all_8_types_positive', 'n_instances', 'N_samples', 'bootstrap_p']

exp_028_fewnerd_5epoch: {"degeneracy_cf1_gold": 0.3133}
  status=DONE, N=None, metrics_keys=['degeneracy_cf1_gold', 'greedy_f1', 'lp_sel_delta_pp', 'lp_sel_f1', 'oracle_f1', 'within_instance_rho_mean', 'within_instance_rho_median']

  status=DONE, N=None, metrics_keys=[]

exp_fewnerd_s789_n8: {"degen_rate": 0.1177, "degen_rate_source": "unified_metrics_constant_f1_gold_filtered"}
  status=DONE, N=None, metrics_keys=['greedy_f1', 'oracle_f1', 'headroom_pp', 'degen_rate', 'degen_rate_source', 'instance_count', 'n_valid', 'lp_sel_f1', 'lp_delta_pp', 'lp_rho_global', 'lp_rho_cond', 'dgs_f1', 'dgs_delta_pp', 'dgs_vs_lp_pp', 'best_signal']

  status=DONE, N=None, metrics_keys=['3seed_mean', 'seed_42', 'seed_123', 'seed_456', 'signal_ranking', 'lp_only_positive', 'n_instances_gold_filtered']

  status=DONE, N=None, metrics_keys=['epoch', 'train_loss', 'eval_loss', 'train_runtime_hours', 'total_steps', 'final_checkpoint', 'adapter_size_mb']

  status=RUNNING, N=None, metrics_keys=[]

  status=RUNNING, N=None, metrics_keys=[]

  status=RUNNING, N=None, metrics_keys=[]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "257c54a5-8fbf-47d6-be4a-4d463b5d0101",
  "isSidechain": false,
  "promptId": "0731b9be-f5e6-4a8a-9a3c-2edafe06629b",
  "type": "user",
  "uuid": "dae1c3ed-ddcc-459b-982f-b0b42bbe861b",
  "toolUseResult": {
    "stdout": "  status=DONE, N=None, metrics_keys=['final_loss', 'total_steps', 'training_time', 'pilot_greedy_f1', 'pilot_instances', 'merged_model_path']\n\nexp_021_fewnerd_full: {\"degeneracy_rate\": 0.101}\n  status=DONE, N=None, metrics_keys=['total_steps', 'train_loss', 'eval_loss', 'train_runtime', 'epochs', 'final_checkpoint', 'adapter_path', 'inference_instances', 'inference_filtered', 'inference_n_samples', 'greedy_macro_f1', 'oracle_macro_f1', 'headroom', 'zero_f1_rate', 'degeneracy_rate']\n\nexp_021_fewnerd_n8_seed123: {\"degen_rate\": 0.1312, \"degen_rate_source\": \"unified_metrics_constant_f1_gold_filtered\"}\n  status=DONE, N=None, metrics_keys=['degen_rate', 'degen_rate_source', 'instance_count', 'n_valid', 'n_gold_empty', 'ner_greedy_f1', 'ner_oracle_f1', 'rho_fk_ner', 'rho_sj_ner', 'sample_f1_pct_zero']\n\nexp_021_fewnerd_n8_seed456: {\"degen_rate\": 0.1212, \"degen_rate_source\": \"unified_metrics_constant_f1_gold_filtered\"}\n  status=DONE, N=None, metrics_keys=['degen_rate', 'degen_rate_source', 'instance_count', 'n_valid', 'n_gold_empty', 'ner_greedy_f1', 'ner_oracle_f1', 'rho_fk_ner', 'rho_sj_ner', 'sample_f1_pct_zero']\n\nexp_027_fewnerd_n16: {\"degen_rate\": 0.0706, \"degen_rate_source\": \"unified_metrics_constant_f1_gold_filtered\"}\n  status=DONE, N=None, metrics_keys=['LP_delta_pp', 'LP_delta_95CI', 'degen_rate', 'degen_rate_source', 'greedy_f1', 'lp_sel_f1', 'oracle_f1', 'headroom_pp', 'all_8_types_positive', 'n_instances', 'N_samples', 'bootstrap_p']\n\nexp_028_fewnerd_5epoch: {\"degeneracy_cf1_gold\": 0.3133}\n  status=DONE, N=None, metrics_keys=['degeneracy_cf1_gold', 'greedy_f1', 'lp_sel_delta_pp', 'lp_sel_f1', 'oracle_f1', 'within_instance_rho_mean', 'within_instance_rho_median']\n\n  status=DONE, N=None, metrics_keys=[]\n\nexp_fewnerd_s789_n8: {\"degen_rate\": 0.1177, \"degen_rate_source\": \"unified_metrics_constant_f1_gold_filtered\"}\n  status=DONE, N=None, metrics_keys=['greedy_f1', 'oracle_f1', 'headroom_pp', 'degen_rate', 'degen_rate_source', 'instance_count', 'n_valid', 'lp_sel_f1', 'lp_delta_pp', 'lp_rho_global', 'lp_rho_cond', 'dgs_f1', 'dgs_delta_pp', 'dgs_vs_lp_pp', 'best_signal']\n\n  status=DONE, N=None, metrics_keys=['3seed_mean', 'seed_42', 'seed_123', 'seed_456', 'signal_ranking', 'lp_only_positive', 'n_instances_gold_filtered']\n\n  status=DONE, N=None, metrics_keys=['epoch', 'train_loss', 'eval_loss', 'train_runtime_hours', 'total_steps', 'final_checkpoint', 'adapter_size_mb']\n\n  status=RUNNING, N=None, metrics_keys=[]\n\n  status=RUNNING, N=None, metrics_keys=[]\n\n  status=RUNNING, N=None, metrics_keys=[]",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "257c54a5-8fbf-47d6-be4a-4d463b5d0101",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "a97de670-f9a7-4d30-affd-382982b8a334",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-19T13:55:48.739Z_

<details open><summary>🔧 Tool call — Bash · `toolu_015wPJYd1cyoQo9fdMQfYSJR`</summary>

```json
{
  "command": "REGFILE=\"/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie/a97de670-f9a7-4d30-affd-382982b8a334/tool-results/mcp-agent-ml-research-read_registry-1779198876363.txt\"\npython3 -c \"\nimport json\ndata = json.loads(json.loads(open('$REGFILE').read())['result'])\nexps = data['data']['experiments']\n\n# CoNLL experiments - look for degeneracy and LP selection data\nfor eid in sorted(exps.keys()):\n    if 'conll' in eid.lower() or '002' in eid:\n        exp = exps[eid]\n        m = exp.get('metrics', {})\n        degen_keys = [k for k in m.keys() if 'degen' in k.lower()]\n        lp_keys = [k for k in m.keys() if 'lp' in k.lower() or 'logprob' in k.lower() or 'selection' in k.lower()]\n        if degen_keys or lp_keys:\n            relevant = {}\n            for k in degen_keys + lp_keys:\n                relevant[k] = m[k]\n            print(f'{eid}:')\n            c = exp.get('config', {})\n            n_val = c.get('N') or c.get('n_samples') or c.get('n')\n            print(f'  N={n_val}')\n            print(f'  {json.dumps(relevant, indent=2)[:2000]}')\n            print()\n\"\n",
  "description": "Extract CoNLL degeneracy and LP selection data"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dae1c3ed-ddcc-459b-982f-b0b42bbe861b",
  "isSidechain": false,
  "requestId": "req_011CbC3PJSNPif73s235HQ8a",
  "type": "assistant",
  "uuid": "9f2df859-97fe-4163-88ad-f6745b0109fc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "a97de670-f9a7-4d30-affd-382982b8a334",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HS1cRDesWf8sqJWscz1wJh",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5011,
      "cache_read_input_tokens": 43364,
      "output_tokens": 1688,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5011,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1688,
          "cache_read_input_tokens": 43364,
          "cache_creation_input_tokens": 5011,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5011
          },
          "type": "message"
        }
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
  "leafUuid": "c2e67c47-4a1f-46ad-89a5-4aa7a45d0735",
  "sessionId": "a97de670-f9a7-4d30-affd-382982b8a334"
}
```

---

### Runtime record

_source line 45_

```json
{
  "type": "ai-title",
  "aiTitle": "Audit data inconsistencies in paper tables",
  "sessionId": "a97de670-f9a7-4d30-affd-382982b8a334"
}
```

---

### Assistant

_source line 46 · 2026-05-19T13:56:43.972Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have substantial data. Let me analyze each investigation:

## Investigation 1: SciERC AUROC Table 1 vs registry

From the AUROC output file on the server (`auroc_5signal.json` for exp_012_rerun_1024), NER full set:
- SJ: 0.691741
- FK: 0.628998
- LP: 0.578334
- EM: 0.749265
- VC: 0.684099

From the registry (exp_012_rerun_1024 metrics → ner_full):


- SJ: 0.6917
- FK: 0.629
- LP: 0.5783
- EM: 0.7493
- VC: 0.6841

These match perfectly when rounded. But the paper Table 1 shows notably different values:
- VC: 0.663
- SJ: 0.650
- FK: 0.602
- EM: 0.614
- LP: 0.578

Now looking at exp_015_v2, I'm seeing higher AUROC scores across the board:
- SJ: 0.7394
- FK: 0.6172
- EM: 0.7873
- VC: (checking the value)
- LP: 0.5918

Neither experiment matches the paper values. The paper claims Table 1 sources from exp_015_v2, but the numbers don't align at all. LP is the only metric that matches exp_012 exactly at 0.578, while the others diverge significantly across all three datasets.

Looking at the registry data more carefully, I'm seeing the AUROC values for ner_full: SJ at 0.6917, FK at 0.629, LP at 0.5783, and EM at 0.7493. These align much more closely with exp_012_rerun_1024 than with the paper's reported numbers.

The paper shows EM at 0.614, but the registry has it at 0.7493—that's a huge discrepancy. I'm wondering if the paper might be using AUROC from a different experiment entirely, or perhaps a different binarization threshold than the standard f1 >= 1.0 that's in the script. I'm wondering if the paper might be using a completely different AUROC definition or threshold than what I've been checking—maybe not the binary f1 >= 1.0 approach at all. Looking at how much lower these values are compared to typical AUROC scores (like EM's usual .749 versus the paper's .614), I'm starting to suspect these might not even be AUROC metrics, but something else entirely that got mislabeled or confused in the documentation. I need to track down the exact source of these AUROC values. There's a script on the server that recomputes table metrics, and I should check if there's a dedicated Table 1 generation script. The provenance is confusing because it claims exp_015_v2 for AUROC while the ρ values come from exp_012_rerun_1024, yet those ρ values match perfectly with the paper. So I'm trying to figure out which AUROC is actually correct by examining the evidence in the provenance claim.

The provenance itself lists specific AUROC values from exp_012_rerun_1024—EM AUROC at 0.749 and VC AUROC at 0.684—but Table 1 in the paper shows completely different numbers: EM at 0.614 and VC at 0.663. This is a significant discrepancy that suggests either a recomputation happened or there's an error in how the metrics were aggregated. I should look for that recompute script and also check exp_015_metrics_expansion as a potential original source.

For the CoNLL LP delta, there's another inconsistency: Table 3 reports a delta of -0.85pp, while the appendix cross-selection section shows LP F1 at 0.897 with a delta of -1.1pp relative to greedy's 0.908. The math checks out for the appendix (0.897 - 0.908 = -1.1pp), so the question is which one used the correct seed configuration. I need to track down the specific 3-seed means for CoNLL LP selection to resolve this.

Now looking at the FewNERD degeneracy rates across different seeds in the registry. The 3-seed mean of 11.78% doesn't match the reported 13.8%, and I'm checking whether a different seed combination or all four seeds might explain the discrepancy.

The exp_028_fewnerd_5epoch result shows a much higher degeneracy at 31.3%, which seems like an outlier. I'm trying to trace where the 13.8% figure actually comes from—it's closest to the seed123 value of 13.12%, but none of the individual seeds or their averages align exactly. I should look at the unified metrics script to understand if there's a different degeneracy calculation being used.

Moving on to check the CoNLL degeneracy results, where the N=16 experiment shows 48.4%, which matches what's reported in the paper.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c2e67c47-4a1f-46ad-89a5-4aa7a45d0735",
  "isSidechain": false,
  "requestId": "req_011CbC3RDABJMiChJYSpLPmC",
  "type": "assistant",
  "uuid": "faaa9c2e-8283-47ab-9259-8accfd739dd1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "a97de670-f9a7-4d30-affd-382982b8a334",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LQfhkgAiG133rvPDRKPq3A",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7465,
      "cache_read_input_tokens": 48375,
      "output_tokens": 3997,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 7465,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3997,
          "cache_read_input_tokens": 48375,
          "cache_creation_input_tokens": 7465,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 7465
          },
          "type": "message"
        }
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

_source line 47 · 2026-05-19T13:56:44.887Z_

Major finding on Investigation 1: exp_012_rerun_1024 AUROC (from server file) shows VC=.684, SJ=.692, EM=.749, but paper has .663, .650, .614. These are different sources. Let me now dig deeper into all four investigations.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "faaa9c2e-8283-47ab-9259-8accfd739dd1",
  "isSidechain": false,
  "requestId": "req_011CbC3RDABJMiChJYSpLPmC",
  "type": "assistant",
  "uuid": "178dd11a-bbec-4b52-aa6c-e9b6643fd13e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "a97de670-f9a7-4d30-affd-382982b8a334",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LQfhkgAiG133rvPDRKPq3A",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7465,
      "cache_read_input_tokens": 48375,
      "output_tokens": 3997,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 7465,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3997,
          "cache_read_input_tokens": 48375,
          "cache_creation_input_tokens": 7465,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 7465
          },
          "type": "message"
        }
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

_source line 48 · 2026-05-19T13:56:51.812Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01Nq4BT1Z7sRpsNXukvkYMK1`</summary>

```json
{
  "command": "REGFILE=\"/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie/a97de670-f9a7-4d30-affd-382982b8a334/tool-results/mcp-agent-ml-research-read_registry-1779198876363.txt\"\npython3 -c \"\nimport json\ndata = json.loads(json.loads(open('$REGFILE').read())['result'])\nexps = data['data']['experiments']\n\n# exp_015_metrics_expansion full metrics (possible original AUROC source)\nexp = exps.get('exp_015_metrics_expansion', {})\nprint('=== exp_015_metrics_expansion ===')\nm = exp.get('metrics', {})\n# Look for AUROC keys\nfor k in sorted(m.keys()):\n    if 'auroc' in k.lower() or 'AUROC' in str(m[k]):\n        print(f'  {k}: {m[k]}')\nprint()\nprint('All keys:', list(m.keys()))\nprint()\n# Print full metrics\nprint(json.dumps(m, indent=2)[:4000])\n\"\n",
  "description": "Extract exp_015_metrics_expansion AUROC values"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "178dd11a-bbec-4b52-aa6c-e9b6643fd13e",
  "isSidechain": false,
  "requestId": "req_011CbC3RDABJMiChJYSpLPmC",
  "type": "assistant",
  "uuid": "413b4689-430b-4ae5-b4ab-66a926745c14",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "a97de670-f9a7-4d30-affd-382982b8a334",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LQfhkgAiG133rvPDRKPq3A",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7465,
      "cache_read_input_tokens": 48375,
      "output_tokens": 3997,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 7465,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3997,
          "cache_read_input_tokens": 48375,
          "cache_creation_input_tokens": 7465,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 7465
          },
          "type": "message"
        }
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

_source line 49 · 2026-05-19T13:56:51.921Z_

<details><summary>↩ Tool result · `toolu_01Nq4BT1Z7sRpsNXukvkYMK1`</summary>

```text
=== exp_015_metrics_expansion ===

All keys: ['data_source', 'config', 'ner', 're', 'diagnosis']

{
  "data_source": "exp_012_logprob/samples_with_logprobs.jsonl",
  "config": "N=8, T=1.0, seed=42, model=qwen3-8b-scierc-merged-v2",
  "ner": {
    "n_valid": 529,
    "n_cond": 501,
    "voting_rho_full": 0.5018,
    "voting_rho_cond": 0.4497,
    "voting_auroc": 0.7279,
    "voting_tau": 0.3766,
    "sj_rho_full": 0.3565,
    "sj_rho_cond": 0.412,
    "sj_auroc": 0.6656,
    "sj_tau": 0.2658,
    "em_rho_full": 0.2566,
    "em_rho_cond": 0.3427,
    "em_auroc": 0.623,
    "em_tau": 0.1924,
    "fk_rho_full": 0.2651,
    "fk_rho_cond": 0.306,
    "fk_auroc": 0.6243,
    "fk_tau": 0.2027,
    "logprob_rho_full": 0.1396,
    "logprob_rho_cond": 0.1627,
    "logprob_auroc": 0.5585,
    "logprob_tau": 0.1006
  },
  "re": {
    "n_valid": 397,
    "n_cond": 296,
    "voting_rho_full": 0.4217,
    "voting_rho_cond": 0.463,
    "voting_auroc": 0.7162,
    "voting_tau": 0.327,
    "sj_rho_full": 0.2112,
    "sj_rho_cond": 0.3683,
    "sj_auroc": 0.5816,
    "sj_tau": 0.1619,
    "em_rho_full": 0.1002,
    "em_rho_cond": 0.3607,
    "em_auroc": 0.5036,
    "em_tau": 0.0839,
    "fk_rho_full": 0.2528,
    "fk_rho_cond": 0.3168,
    "fk_auroc": 0.6308,
    "fk_tau": 0.1967,
    "logprob_rho_full": 0.2467,
    "logprob_rho_cond": 0.1457,
    "logprob_auroc": 0.6354,
    "logprob_tau": 0.1808
  },
  "diagnosis": "Unified 5-signal evaluation on single data source. Voting leads NER full (\u03c1=0.502), SJ retains strength in NER cond (\u03c1=0.412). All structural signals beat logprob on NER. RE: voting leads both full and cond."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "413b4689-430b-4ae5-b4ab-66a926745c14",
  "isSidechain": false,
  "promptId": "0731b9be-f5e6-4a8a-9a3c-2edafe06629b",
  "type": "user",
  "uuid": "0422e250-75fe-4be5-b998-99f87909a502",
  "toolUseResult": {
    "stdout": "=== exp_015_metrics_expansion ===\n\nAll keys: ['data_source', 'config', 'ner', 're', 'diagnosis']\n\n{\n  \"data_source\": \"exp_012_logprob/samples_with_logprobs.jsonl\",\n  \"config\": \"N=8, T=1.0, seed=42, model=qwen3-8b-scierc-merged-v2\",\n  \"ner\": {\n    \"n_valid\": 529,\n    \"n_cond\": 501,\n    \"voting_rho_full\": 0.5018,\n    \"voting_rho_cond\": 0.4497,\n    \"voting_auroc\": 0.7279,\n    \"voting_tau\": 0.3766,\n    \"sj_rho_full\": 0.3565,\n    \"sj_rho_cond\": 0.412,\n    \"sj_auroc\": 0.6656,\n    \"sj_tau\": 0.2658,\n    \"em_rho_full\": 0.2566,\n    \"em_rho_cond\": 0.3427,\n    \"em_auroc\": 0.623,\n    \"em_tau\": 0.1924,\n    \"fk_rho_full\": 0.2651,\n    \"fk_rho_cond\": 0.306,\n    \"fk_auroc\": 0.6243,\n    \"fk_tau\": 0.2027,\n    \"logprob_rho_full\": 0.1396,\n    \"logprob_rho_cond\": 0.1627,\n    \"logprob_auroc\": 0.5585,\n    \"logprob_tau\": 0.1006\n  },\n  \"re\": {\n    \"n_valid\": 397,\n    \"n_cond\": 296,\n    \"voting_rho_full\": 0.4217,\n    \"voting_rho_cond\": 0.463,\n    \"voting_auroc\": 0.7162,\n    \"voting_tau\": 0.327,\n    \"sj_rho_full\": 0.2112,\n    \"sj_rho_cond\": 0.3683,\n    \"sj_auroc\": 0.5816,\n    \"sj_tau\": 0.1619,\n    \"em_rho_full\": 0.1002,\n    \"em_rho_cond\": 0.3607,\n    \"em_auroc\": 0.5036,\n    \"em_tau\": 0.0839,\n    \"fk_rho_full\": 0.2528,\n    \"fk_rho_cond\": 0.3168,\n    \"fk_auroc\": 0.6308,\n    \"fk_tau\": 0.1967,\n    \"logprob_rho_full\": 0.2467,\n    \"logprob_rho_cond\": 0.1457,\n    \"logprob_auroc\": 0.6354,\n    \"logprob_tau\": 0.1808\n  },\n  \"diagnosis\": \"Unified 5-signal evaluation on single data source. Voting leads NER full (\\u03c1=0.502), SJ retains strength in NER cond (\\u03c1=0.412). All structural signals beat logprob on NER. RE: voting leads both full and cond.\"\n}",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "413b4689-430b-4ae5-b4ab-66a926745c14",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "a97de670-f9a7-4d30-affd-382982b8a334",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 50 · 2026-05-19T13:56:56.910Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01RTupatHCL5YWzoxRuTjtb4`</summary>

```json
{
  "command": "REGFILE=\"/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie/a97de670-f9a7-4d30-affd-382982b8a334/tool-results/mcp-agent-ml-research-read_registry-1779198876363.txt\"\npython3 -c \"\nimport json\ndata = json.loads(json.loads(open('$REGFILE').read())['result'])\nexps = data['data']['experiments']\n\n# exp_002 full metrics - CoNLL N=8 degeneracy\nexp = exps.get('exp_002', {})\nm = exp.get('metrics', {})\nprint('=== exp_002 (CoNLL) all metrics ===')\nprint(json.dumps(m, indent=2)[:5000])\nprint()\n\n# Also check exp_002_ner_conll2003\nexp2 = exps.get('exp_002_ner_conll2003', {})\nm2 = exp2.get('metrics', {})\nprint('=== exp_002_ner_conll2003 ===')\nprint(json.dumps(m2, indent=2)[:3000])\nprint()\n\n# exp_002_conll_n16_r1024\nexp3 = exps.get('exp_002_conll_n16_r1024', {})\nm3 = exp3.get('metrics', {})\nprint('=== exp_002_conll_n16_r1024 ===')\nprint(json.dumps(m3, indent=2)[:3000])\n\"\n",
  "description": "Extract CoNLL exp_002 full metrics including degeneracy"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0422e250-75fe-4be5-b998-99f87909a502",
  "isSidechain": false,
  "requestId": "req_011CbC3RDABJMiChJYSpLPmC",
  "type": "assistant",
  "uuid": "6dcfda5d-46bc-4cee-8506-0049ee72b510",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "a97de670-f9a7-4d30-affd-382982b8a334",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LQfhkgAiG133rvPDRKPq3A",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7465,
      "cache_read_input_tokens": 48375,
      "output_tokens": 3997,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 7465,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3997,
          "cache_read_input_tokens": 48375,
          "cache_creation_input_tokens": 7465,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 7465
          },
          "type": "message"
        }
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

_source line 51 · 2026-05-19T13:56:56.982Z_

<details><summary>↩ Tool result · `toolu_01RTupatHCL5YWzoxRuTjtb4`</summary>

```text
=== exp_002 (CoNLL) all metrics ===
{
  "sj_rho_full": 0.4357,
  "sj_tau_full": 0.3851,
  "sj_auroc_full": 0.8008,
  "sj_rho_cond": 0.4511,
  "fk_rho_full": 0.3998,
  "fk_tau_full": 0.3568,
  "fk_auroc_full": 0.7741,
  "fk_rho_cond": 0.4064,
  "logprob_rho_full": 0.3157,
  "logprob_tau_full": 0.2469,
  "logprob_auroc_full": 0.7532,
  "logprob_rho_cond": 0.3562,
  "em_rho_full": 0.4507,
  "em_tau_full": 0.4002,
  "em_auroc_full": 0.8156,
  "em_rho_cond": 0.4799,
  "ev_rho_full": 0.4237,
  "ev_tau_full": 0.3777,
  "ev_auroc_full": 0.7889,
  "ev_rho_cond": 0.4127,
  "greedy_f1": 0.9123,
  "oracle_f1": 0.9543,
  "voting_f1": 0.9141,
  "oracle_headroom": 0.042,
  "sj_vs_logprob_delta_rho": 0.12,
  "sj_vs_logprob_ci_low": 0.0881,
  "sj_vs_logprob_ci_high": 0.154,
  "sj_vs_logprob_significant": true,
  "n_instances": 3453,
  "n_valid": 2756,
  "n_samples": 8,
  "temperature": 1
}

=== exp_002_ner_conll2003 ===
{}

=== exp_002_conll_n16_r1024 ===
{}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6dcfda5d-46bc-4cee-8506-0049ee72b510",
  "isSidechain": false,
  "promptId": "0731b9be-f5e6-4a8a-9a3c-2edafe06629b",
  "type": "user",
  "uuid": "fe50cbe6-d09d-4766-91e6-d0e0f130d318",
  "toolUseResult": {
    "stdout": "=== exp_002 (CoNLL) all metrics ===\n{\n  \"sj_rho_full\": 0.4357,\n  \"sj_tau_full\": 0.3851,\n  \"sj_auroc_full\": 0.8008,\n  \"sj_rho_cond\": 0.4511,\n  \"fk_rho_full\": 0.3998,\n  \"fk_tau_full\": 0.3568,\n  \"fk_auroc_full\": 0.7741,\n  \"fk_rho_cond\": 0.4064,\n  \"logprob_rho_full\": 0.3157,\n  \"logprob_tau_full\": 0.2469,\n  \"logprob_auroc_full\": 0.7532,\n  \"logprob_rho_cond\": 0.3562,\n  \"em_rho_full\": 0.4507,\n  \"em_tau_full\": 0.4002,\n  \"em_auroc_full\": 0.8156,\n  \"em_rho_cond\": 0.4799,\n  \"ev_rho_full\": 0.4237,\n  \"ev_tau_full\": 0.3777,\n  \"ev_auroc_full\": 0.7889,\n  \"ev_rho_cond\": 0.4127,\n  \"greedy_f1\": 0.9123,\n  \"oracle_f1\": 0.9543,\n  \"voting_f1\": 0.9141,\n  \"oracle_headroom\": 0.042,\n  \"sj_vs_logprob_delta_rho\": 0.12,\n  \"sj_vs_logprob_ci_low\": 0.0881,\n  \"sj_vs_logprob_ci_high\": 0.154,\n  \"sj_vs_logprob_significant\": true,\n  \"n_instances\": 3453,\n  \"n_valid\": 2756,\n  \"n_samples\": 8,\n  \"temperature\": 1\n}\n\n=== exp_002_ner_conll2003 ===\n{}\n\n=== exp_002_conll_n16_r1024 ===\n{}",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "6dcfda5d-46bc-4cee-8506-0049ee72b510",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "a97de670-f9a7-4d30-affd-382982b8a334",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 52 · 2026-05-19T13:56:57.862Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_013MoVBk7VWLjtvxkRq6h9CT`</summary>

```json
{
  "server": "autodl-5090",
  "command": "cat /root/autodl-tmp/struct_self_consist_ie/code/recompute_table_metrics.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fe50cbe6-d09d-4766-91e6-d0e0f130d318",
  "isSidechain": false,
  "requestId": "req_011CbC3RDABJMiChJYSpLPmC",
  "type": "assistant",
  "uuid": "3145f39a-e6ce-43a6-8b5c-19f7f29f9714",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "a97de670-f9a7-4d30-affd-382982b8a334",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LQfhkgAiG133rvPDRKPq3A",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7465,
      "cache_read_input_tokens": 48375,
      "output_tokens": 3997,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 7465,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3997,
          "cache_read_input_tokens": 48375,
          "cache_creation_input_tokens": 7465,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 7465
          },
          "type": "message"
        }
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

_source line 53 · 2026-05-19T13:56:58.233Z_

<details><summary>↩ Tool result · `toolu_013MoVBk7VWLjtvxkRq6h9CT`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"#!/usr/bin/env python3\\nimport json, numpy as np\\nfrom scipy import stats as scipy_stats\\n\\ndef load_data(path):\\n    with open(path) as f:\\n        return [json.loads(line) for line in f if line.strip()]\\n\\ndef entity_set(output):\\n    ents = output.get(\\\"entities\\\", [])\\n    return set((e[\\\"text\\\"], e[\\\"type\\\"]) for e in ents)\\n\\ndef compute_f1(pred_set, gold_set):\\n    if not pred_set and not gold_set:\\n        return 1.0\\n    if not pred_set or not gold_set:\\n        return 0.0\\n    tp = len(pred_set & gold_set)\\n    p = tp / len(pred_set)\\n    r = tp / len(gold_set)\\n    if p + r == 0:\\n        return 0.0\\n    return 2 * p * r / (p + r)\\n\\ndef analyze_dataset(data, label):\\n    total = len(data)\\n    filtered = [d for d in data if len(d[\\\"gold\\\"].get(\\\"entities\\\", [])) > 0]\\n    N = len(filtered)\\n    n_samples = len(filtered[0][\\\"samples\\\"]) if filtered else 0\\n    print(f\\\"\\\\n{'='*60}\\\")\\n    print(f\\\"{label}: total={total}, gold-filtered n={N}, N_samples={n_samples}\\\")\\n    print(f\\\"{'='*60}\\\")\\n    greedy_f1s, oracle_f1s, mean_lps, max_lps, lp_sel_f1s = [], [], [], [], []\\n    degen_count = 0\\n    for d in filtered:\\n        gold_set = entity_set(d[\\\"gold\\\"])\\n        greedy_set = entity_set(d[\\\"greedy\\\"])\\n        gf1 = compute_f1(greedy_set, gold_set)\\n        greedy_f1s.append(gf1)\\n        logprobs = d.get(\\\"logprobs\\\", [])\\n        if not logprobs:\\n            logprobs = [s.get(\\\"mean_logprob\\\", s.get(\\\"cumulative_logprob\\\", -999)/max(s.get(\\\"n_tokens\\\",1),1)) for s in d[\\\"samples\\\"]]\\n        sample_f1s = [compute_f1(entity_set(s), gold_set) for s in d[\\\"samples\\\"]]\\n        oracle_f1s.append(max(sample_f1s))\\n        mean_lps.append(float(np.mean(logprobs)))\\n        max_lps.append(float(np.max(logprobs)))\\n        lp_sel_f1s.append(sample_f1s[int(np.argmax(logprobs))])\\n        if len(set(sample_f1s)) == 1:\\n            degen_count += 1\\n    greedy_f1s = np.array(greedy_f1s)\\n    oracle_f1s = np.array(oracle_f1s)\\n    lp_sel_f1s = np.array(lp_sel_f1s)\\n    mean_lps = np.array(mean_lps)\\n    max_lps = np.array(max_lps)\\n    gm = float(greedy_f1s.mean())\\n    om = float(oracle_f1s.mean())\\n    hd = (om - gm) * 100\\n    dp = degen_count / N * 100\\n    lsm = float(lp_sel_f1s.mean())\\n    ld = (lsm - gm) * 100\\n    rm, pm = scipy_stats.spearmanr(mean_lps, greedy_f1s)\\n    rx, px = scipy_stats.spearmanr(max_lps, greedy_f1s)\\n    print(f\\\"  greedy_F1  = {gm:.6f}\\\")\\n    print(f\\\"  oracle_F1  = {om:.6f}\\\")\\n    print(f\\\"  headroom   = {hd:.2f}pp\\\")\\n    print(f\\\"  degen%     = {dp:.1f}% ({degen_count}/{N})\\\")\\n    print(f\\\"  mean_LP rho= {float(rm):.6f} (p={float(pm):.2e})\\\")\\n    print(f\\\"  max_LP rho = {float(rx):.6f} (p={float(px):.2e})\\\")\\n    print(f\\\"  LP_sel_F1  = {lsm:.6f}\\\")\\n    print(f\\\"  LP_delta   = {ld:+.2f}pp\\\")\\n    return {\\\"n\\\":N,\\\"greedy\\\":round(gm,6),\\\"oracle\\\":round(om,6),\\\"headroom\\\":round(hd,2),\\\"degen\\\":round(dp,1),\\\"mean_lp_rho\\\":round(float(rm),6),\\\"max_lp_rho\\\":round(float(rx),6),\\\"lp_sel\\\":round(lsm,6),\\\"lp_delta\\\":round(ld,2)}\\n\\nbase = \\\"/root/autodl-tmp/struct_self_consist_ie/output\\\"\\nfewnerd = load_data(f\\\"{base}/exp_021_inference/samples.jsonl\\\")\\nfr = analyze_dataset(fewnerd, \\\"Few-NERD\\\")\\nconll = load_data(f\\\"{base}/exp002_conll2003/samples.jsonl\\\")\\ncr = analyze_dataset(conll, \\\"CoNLL\\\")\\nprint(\\\"\\\\n\\\" + \\\"=\\\"*60)\\nprint(\\\"SUMMARY\\\")\\nprint(\\\"=\\\"*60)\\nprint(json.dumps({\\\"fewnerd\\\": fr, \\\"conll\\\": cr}, indent=2))\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.36}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3145f39a-e6ce-43a6-8b5c-19f7f29f9714",
  "isSidechain": false,
  "promptId": "0731b9be-f5e6-4a8a-9a3c-2edafe06629b",
  "type": "user",
  "uuid": "109940fd-67a5-4d74-9de2-4e8572e24a90",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"#!/usr/bin/env python3\\\\nimport json, numpy as np\\\\nfrom scipy import stats as scipy_stats\\\\n\\\\ndef load_data(path):\\\\n    with open(path) as f:\\\\n        return [json.loads(line) for line in f if line.strip()]\\\\n\\\\ndef entity_set(output):\\\\n    ents = output.get(\\\\\\\"entities\\\\\\\", [])\\\\n    return set((e[\\\\\\\"text\\\\\\\"], e[\\\\\\\"type\\\\\\\"]) for e in ents)\\\\n\\\\ndef compute_f1(pred_set, gold_set):\\\\n    if not pred_set and not gold_set:\\\\n        return 1.0\\\\n    if not pred_set or not gold_set:\\\\n        return 0.0\\\\n    tp = len(pred_set & gold_set)\\\\n    p = tp / len(pred_set)\\\\n    r = tp / len(gold_set)\\\\n    if p + r == 0:\\\\n        return 0.0\\\\n    return 2 * p * r / (p + r)\\\\n\\\\ndef analyze_dataset(data, label):\\\\n    total = len(data)\\\\n    filtered = [d for d in data if len(d[\\\\\\\"gold\\\\\\\"].get(\\\\\\\"entities\\\\\\\", [])) > 0]\\\\n    N = len(filtered)\\\\n    n_samples = len(filtered[0][\\\\\\\"samples\\\\\\\"]) if filtered else 0\\\\n    print(f\\\\\\\"\\\\\\\\n{'='*60}\\\\\\\")\\\\n    print(f\\\\\\\"{label}: total={total}, gold-filtered n={N}, N_samples={n_samples}\\\\\\\")\\\\n    print(f\\\\\\\"{'='*60}\\\\\\\")\\\\n    greedy_f1s, oracle_f1s, mean_lps, max_lps, lp_sel_f1s = [], [], [], [], []\\\\n    degen_count = 0\\\\n    for d in filtered:\\\\n        gold_set = entity_set(d[\\\\\\\"gold\\\\\\\"])\\\\n        greedy_set = entity_set(d[\\\\\\\"greedy\\\\\\\"])\\\\n        gf1 = compute_f1(greedy_set, gold_set)\\\\n        greedy_f1s.append(gf1)\\\\n        logprobs = d.get(\\\\\\\"logprobs\\\\\\\", [])\\\\n        if not logprobs:\\\\n            logprobs = [s.get(\\\\\\\"mean_logprob\\\\\\\", s.get(\\\\\\\"cumulative_logprob\\\\\\\", -999)/max(s.get(\\\\\\\"n_tokens\\\\\\\",1),1)) for s in d[\\\\\\\"samples\\\\\\\"]]\\\\n        sample_f1s = [compute_f1(entity_set(s), gold_set) for s in d[\\\\\\\"samples\\\\\\\"]]\\\\n        oracle_f1s.append(max(sample_f1s))\\\\n        mean_lps.append(float(np.mean(logprobs)))\\\\n        max_lps.append(float(np.max(logprobs)))\\\\n        lp_sel_f1s.append(sample_f1s[int(np.argmax(logprobs))])\\\\n        if len(set(sample_f1s)) == 1:\\\\n            degen_count += 1\\\\n    greedy_f1s = np.array(greedy_f1s)\\\\n    oracle_f1s = np.array(oracle_f1s)\\\\n    lp_sel_f1s = np.array(lp_sel_f1s)\\\\n    mean_lps = np.array(mean_lps)\\\\n    max_lps = np.array(max_lps)\\\\n    gm = float(greedy_f1s.mean())\\\\n    om = float(oracle_f1s.mean())\\\\n    hd = (om - gm) * 100\\\\n    dp = degen_count / N * 100\\\\n    lsm = float(lp_sel_f1s.mean())\\\\n    ld = (lsm - gm) * 100\\\\n    rm, pm = scipy_stats.spearmanr(mean_lps, greedy_f1s)\\\\n    rx, px = scipy_stats.spearmanr(max_lps, greedy_f1s)\\\\n    print(f\\\\\\\"  greedy_F1  = {gm:.6f}\\\\\\\")\\\\n    print(f\\\\\\\"  oracle_F1  = {om:.6f}\\\\\\\")\\\\n    print(f\\\\\\\"  headroom   = {hd:.2f}pp\\\\\\\")\\\\n    print(f\\\\\\\"  degen%     = {dp:.1f}% ({degen_count}/{N})\\\\\\\")\\\\n    print(f\\\\\\\"  mean_LP rho= {float(rm):.6f} (p={float(pm):.2e})\\\\\\\")\\\\n    print(f\\\\\\\"  max_LP rho = {float(rx):.6f} (p={float(px):.2e})\\\\\\\")\\\\n    print(f\\\\\\\"  LP_sel_F1  = {lsm:.6f}\\\\\\\")\\\\n    print(f\\\\\\\"  LP_delta   = {ld:+.2f}pp\\\\\\\")\\\\n    return {\\\\\\\"n\\\\\\\":N,\\\\\\\"greedy\\\\\\\":round(gm,6),\\\\\\\"oracle\\\\\\\":round(om,6),\\\\\\\"headroom\\\\\\\":round(hd,2),\\\\\\\"degen\\\\\\\":round(dp,1),\\\\\\\"mean_lp_rho\\\\\\\":round(float(rm),6),\\\\\\\"max_lp_rho\\\\\\\":round(float(rx),6),\\\\\\\"lp_sel\\\\\\\":round(lsm,6),\\\\\\\"lp_delta\\\\\\\":round(ld,2)}\\\\n\\\\nbase = \\\\\\\"/root/autodl-tmp/struct_self_consist_ie/output\\\\\\\"\\\\nfewnerd = load_data(f\\\\\\\"{base}/exp_021_inference/samples.jsonl\\\\\\\")\\\\nfr = analyze_dataset(fewnerd, \\\\\\\"Few-NERD\\\\\\\")\\\\nconll = load_data(f\\\\\\\"{base}/exp002_conll2003/samples.jsonl\\\\\\\")\\\\ncr = analyze_dataset(conll, \\\\\\\"CoNLL\\\\\\\")\\\\nprint(\\\\\\\"\\\\\\\\n\\\\\\\" + \\\\\\\"=\\\\\\\"*60)\\\\nprint(\\\\\\\"SUMMARY\\\\\\\")\\\\nprint(\\\\\\\"=\\\\\\\"*60)\\\\nprint(json.dumps({\\\\\\\"fewnerd\\\\\\\": fr, \\\\\\\"conll\\\\\\\": cr}, indent=2))\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.36}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"#!/usr/bin/env python3\\nimport json, numpy as np\\nfrom scipy import stats as scipy_stats\\n\\ndef load_data(path):\\n    with open(path) as f:\\n        return [json.loads(line) for line in f if line.strip()]\\n\\ndef entity_set(output):\\n    ents = output.get(\\\"entities\\\", [])\\n    return set((e[\\\"text\\\"], e[\\\"type\\\"]) for e in ents)\\n\\ndef compute_f1(pred_set, gold_set):\\n    if not pred_set and not gold_set:\\n        return 1.0\\n    if not pred_set or not gold_set:\\n        return 0.0\\n    tp = len(pred_set & gold_set)\\n    p = tp / len(pred_set)\\n    r = tp / len(gold_set)\\n    if p + r == 0:\\n        return 0.0\\n    return 2 * p * r / (p + r)\\n\\ndef analyze_dataset(data, label):\\n    total = len(data)\\n    filtered = [d for d in data if len(d[\\\"gold\\\"].get(\\\"entities\\\", [])) > 0]\\n    N = len(filtered)\\n    n_samples = len(filtered[0][\\\"samples\\\"]) if filtered else 0\\n    print(f\\\"\\\\n{'='*60}\\\")\\n    print(f\\\"{label}: total={total}, gold-filtered n={N}, N_samples={n_samples}\\\")\\n    print(f\\\"{'='*60}\\\")\\n    greedy_f1s, oracle_f1s, mean_lps, max_lps, lp_sel_f1s = [], [], [], [], []\\n    degen_count = 0\\n    for d in filtered:\\n        gold_set = entity_set(d[\\\"gold\\\"])\\n        greedy_set = entity_set(d[\\\"greedy\\\"])\\n        gf1 = compute_f1(greedy_set, gold_set)\\n        greedy_f1s.append(gf1)\\n        logprobs = d.get(\\\"logprobs\\\", [])\\n        if not logprobs:\\n            logprobs = [s.get(\\\"mean_logprob\\\", s.get(\\\"cumulative_logprob\\\", -999)/max(s.get(\\\"n_tokens\\\",1),1)) for s in d[\\\"samples\\\"]]\\n        sample_f1s = [compute_f1(entity_set(s), gold_set) for s in d[\\\"samples\\\"]]\\n        oracle_f1s.append(max(sample_f1s))\\n        mean_lps.append(float(np.mean(logprobs)))\\n        max_lps.append(float(np.max(logprobs)))\\n        lp_sel_f1s.append(sample_f1s[int(np.argmax(logprobs))])\\n        if len(set(sample_f1s)) == 1:\\n            degen_count += 1\\n    greedy_f1s = np.array(greedy_f1s)\\n    oracle_f1s = np.array(oracle_f1s)\\n    lp_sel_f1s = np.array(lp_sel_f1s)\\n    mean_lps = np.array(mean_lps)\\n    max_lps = np.array(max_lps)\\n    gm = float(greedy_f1s.mean())\\n    om = float(oracle_f1s.mean())\\n    hd = (om - gm) * 100\\n    dp = degen_count / N * 100\\n    lsm = float(lp_sel_f1s.mean())\\n    ld = (lsm - gm) * 100\\n    rm, pm = scipy_stats.spearmanr(mean_lps, greedy_f1s)\\n    rx, px = scipy_stats.spearmanr(max_lps, greedy_f1s)\\n    print(f\\\"  greedy_F1  = {gm:.6f}\\\")\\n    print(f\\\"  oracle_F1  = {om:.6f}\\\")\\n    print(f\\\"  headroom   = {hd:.2f}pp\\\")\\n    print(f\\\"  degen%     = {dp:.1f}% ({degen_count}/{N})\\\")\\n    print(f\\\"  mean_LP rho= {float(rm):.6f} (p={float(pm):.2e})\\\")\\n    print(f\\\"  max_LP rho = {float(rx):.6f} (p={float(px):.2e})\\\")\\n    print(f\\\"  LP_sel_F1  = {lsm:.6f}\\\")\\n    print(f\\\"  LP_delta   = {ld:+.2f}pp\\\")\\n    return {\\\"n\\\":N,\\\"greedy\\\":round(gm,6),\\\"oracle\\\":round(om,6),\\\"headroom\\\":round(hd,2),\\\"degen\\\":round(dp,1),\\\"mean_lp_rho\\\":round(float(rm),6),\\\"max_lp_rho\\\":round(float(rx),6),\\\"lp_sel\\\":round(lsm,6),\\\"lp_delta\\\":round(ld,2)}\\n\\nbase = \\\"/root/autodl-tmp/struct_self_consist_ie/output\\\"\\nfewnerd = load_data(f\\\"{base}/exp_021_inference/samples.jsonl\\\")\\nfr = analyze_dataset(fewnerd, \\\"Few-NERD\\\")\\nconll = load_data(f\\\"{base}/exp002_conll2003/samples.jsonl\\\")\\ncr = analyze_dataset(conll, \\\"CoNLL\\\")\\nprint(\\\"\\\\n\\\" + \\\"=\\\"*60)\\nprint(\\\"SUMMARY\\\")\\nprint(\\\"=\\\"*60)\\nprint(json.dumps({\\\"fewnerd\\\": fr, \\\"conll\\\": cr}, indent=2))\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.36}}"
    }
  },
  "sourceToolAssistantUUID": "3145f39a-e6ce-43a6-8b5c-19f7f29f9714",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "a97de670-f9a7-4d30-affd-382982b8a334",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 54 · 2026-05-19T13:56:58.478Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01PwhLoEzkSDxWmTDfPAkFMK`</summary>

```json
{
  "server": "autodl-5090",
  "command": "cat /root/autodl-tmp/struct_self_consist_ie/code/unified_tab_fewnerd_metrics.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "109940fd-67a5-4d74-9de2-4e8572e24a90",
  "isSidechain": false,
  "requestId": "req_011CbC3RDABJMiChJYSpLPmC",
  "type": "assistant",
  "uuid": "afd3c16f-90cb-4bd8-b261-43be2853cbf6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "a97de670-f9a7-4d30-affd-382982b8a334",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LQfhkgAiG133rvPDRKPq3A",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7465,
      "cache_read_input_tokens": 48375,
      "output_tokens": 3997,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 7465,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3997,
          "cache_read_input_tokens": 48375,
          "cache_creation_input_tokens": 7465,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 7465
          },
          "type": "message"
        }
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
  "leafUuid": "afd3c16f-90cb-4bd8-b261-43be2853cbf6",
  "sessionId": "a97de670-f9a7-4d30-affd-382982b8a334"
}
```

---

### Runtime record

_source line 56_

```json
{
  "type": "ai-title",
  "aiTitle": "Audit data inconsistencies in paper tables",
  "sessionId": "a97de670-f9a7-4d30-affd-382982b8a334"
}
```

---

### Tool result

_source line 57 · 2026-05-19T13:56:58.840Z_

<details><summary>↩ Tool result · `toolu_01PwhLoEzkSDxWmTDfPAkFMK`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"#!/usr/bin/env python3\\n\\\"\\\"\\\"Unified tab:fewnerd metrics: gold-filtered, max_LP inst-level rho.\\nUses EXACT same code path for all 3 datasets.\\\"\\\"\\\"\\n\\nimport json\\nimport sys\\nimport os\\nimport numpy as np\\nfrom scipy.stats import spearmanr\\n\\nsys.path.insert(0, '/root/autodl-tmp/struct_self_consist_ie/code')\\nfrom evaluation import per_instance_f1\\n\\nSUBTASK = \\\"ner\\\"\\n\\ndef load_data(path):\\n    with open(path) as f:\\n        return [json.loads(line) for line in f if line.strip()]\\n\\ndef compute_metrics(data, label=\\\"dataset\\\"):\\n    N = len(data)\\n    if N == 0:\\n        print(f\\\"  [{label}] No instances!\\\")\\n        return {}\\n\\n    n_samples = len(data[0][\\\"samples\\\"])\\n\\n    greedy_f1s = []\\n    oracle_f1s = []\\n    lp_sel_f1s = []\\n    degen_f1_flags = []\\n    max_lp_per_instance = []\\n    mean_lp_per_instance = []\\n\\n    for inst in data:\\n        gold = inst[\\\"gold\\\"]\\n        greedy = inst[\\\"greedy\\\"]\\n        samples = inst[\\\"samples\\\"]\\n\\n        g_f1 = per_instance_f1(greedy, gold, SUBTASK)\\n        greedy_f1s.append(g_f1)\\n\\n        sample_f1s = []\\n        sample_lps = []\\n        for s in samples:\\n            f1 = per_instance_f1(s, gold, SUBTASK)\\n            sample_f1s.append(f1)\\n            lp = s.get(\\\"mean_logprob\\\")\\n            if lp is None:\\n                lp = s.get(\\\"cumulative_logprob\\\", -999) / max(s.get(\\\"n_tokens\\\", 1), 1)\\n            sample_lps.append(lp)\\n\\n        oracle_f1s.append(max(sample_f1s))\\n\\n        lp_sel_idx = int(np.argmax(sample_lps))\\n        lp_sel_f1s.append(sample_f1s[lp_sel_idx])\\n\\n        degen_f1_flags.append(len(set(sample_f1s)) == 1)\\n\\n        max_lp_per_instance.append(max(sample_lps))\\n        mean_lp_per_instance.append(float(np.mean(sample_lps)))\\n\\n    greedy_f1s = np.array(greedy_f1s)\\n    oracle_f1s = np.array(oracle_f1s)\\n    lp_sel_f1s = np.array(lp_sel_f1s)\\n\\n    greedy_macro = float(greedy_f1s.mean())\\n    oracle_macro = float(oracle_f1s.mean())\\n    lp_sel_macro = float(lp_sel_f1s.mean())\\n    headroom_pp = (oracle_macro - greedy_macro) * 100\\n    lp_delta_pp = (lp_sel_macro - greedy_macro) * 100\\n    degen_rate = float(np.mean(degen_f1_flags)) * 100\\n\\n    rho_max, p_max = spearmanr(max_lp_per_instance, greedy_f1s)\\n    rho_mean, p_mean = spearmanr(mean_lp_per_instance, greedy_f1s)\\n\\n    return {\\n        \\\"n\\\": N,\\n        \\\"n_samples\\\": n_samples,\\n        \\\"greedy_f1\\\": greedy_macro,\\n        \\\"oracle_f1\\\": oracle_macro,\\n        \\\"lp_sel_f1\\\": lp_sel_macro,\\n        \\\"headroom_pp\\\": headroom_pp,\\n        \\\"lp_delta_pp\\\": lp_delta_pp,\\n        \\\"degen_f1_pct\\\": degen_rate,\\n        \\\"lp_rho_max\\\": float(rho_max),\\n        \\\"lp_rho_max_p\\\": float(p_max),\\n        \\\"lp_rho_mean\\\": float(rho_mean),\\n        \\\"lp_rho_mean_p\\\": float(p_mean),\\n    }\\n\\n\\nif __name__ == \\\"__main__\\\":\\n    base = \\\"/root/autodl-tmp/struct_self_consist_ie/output\\\"\\n\\n    datasets = {\\n        \\\"SciERC\\\": os.path.join(base, \\\"exp_012_rerun_1024/samples.jsonl\\\"),\\n        \\\"Few-NERD\\\": os.path.join(base, \\\"exp_021_inference/samples.jsonl\\\"),\\n        \\\"CoNLL_Qwen_N8\\\": os.path.join(base, \\\"exp002_conll2003/samples.jsonl\\\"),\\n    }\\n\\n    all_results = {}\\n    for name, path in datasets.items():\\n        print(f\\\"\\\\n{'='*70}\\\")\\n        print(f\\\"DATASET: {name}\\\")\\n        print(f\\\"Path: {path}\\\")\\n        print(f\\\"{'='*70}\\\")\\n\\n        if not os.path.exists(path):\\n            print(f\\\"  ERROR: File not found!\\\")\\n            continue\\n\\n        data = load_data(path)\\n        total = len(data)\\n        gold_filtered = [d for d in data if len(d[\\\"gold\\\"].get(\\\"entities\\\", [])) > 0]\\n        n_gf = len(gold_filtered)\\n        print(f\\\"  Total: {total}, Gold-filtered: {n_gf}\\\")\\n\\n        r = compute_metrics(gold_filtered, name)\\n        all_results[name] = r\\n\\n        print(f\\\"  greedy_f1:    {r['greedy_f1']:.6f} ({r['greedy_f1']:.3f})\\\")\\n        print(f\\\"  oracle_f1:    {r['oracle_f1']:.6f} ({r['oracle_f1']:.3f})\\\")\\n        print(f\\\"  headroom:     {r['headroom_pp']:.2f}pp\\\")\\n        print(f\\\"  degen%:       {r['degen_f1_pct']:.1f}%\\\")\\n        print(f\\\"  lp_rho_max:   {r['lp_rho_max']:.6f} (p={r['lp_rho_max_p']:.2e})\\\")\\n        print(f\\\"  lp_rho_mean:  {r['lp_rho_mean']:.6f} (p={r['lp_rho_mean_p']:.2e})\\\")\\n        print(f\\\"  lp_sel_f1:    {r['lp_sel_f1']:.6f} ({r['lp_sel_f1']:.3f})\\\")\\n        print(f\\\"  lp_delta:     {r['lp_delta_pp']:+.2f}pp\\\")\\n\\n    # Summary table\\n    print(f\\\"\\\\n\\\\n{'='*70}\\\")\\n    print(\\\"SUMMARY TABLE (gold-filtered)\\\")\\n    print(f\\\"{'='*70}\\\")\\n    print(f\\\"{'Dataset':<20} | {'n':>6} | {'N':>2} | {'greedy':>7} | {'oracle':>7} | {'hdroom':>7} | {'degen%':>6} | {'LP_rho_max':>10} | {'LP_rho_mean':>11} | {'LP_sel':>7} | {'LP_delta':>8}\\\")\\n    print(\\\"-\\\" * 120)\\n    for name, r in all_results.items():\\n        print(f\\\"{name:<20} | {r['n']:>6} | {r['n_samples']:>2} | {r['greedy_f1']:.4f} | {r['oracle_f1']:.4f} | {r['headroom_pp']:>6.2f}pp | {r['degen_f1_pct']:>5.1f}% | {r['lp_rho_max']:>10.4f} | {r['lp_rho_mean']:>11.4f} | {r['lp_sel_f1']:.4f} | {r['lp_delta_pp']:>+7.2f}pp\\\")\\n\\n    # Save\\n    out_path = os.path.join(os.path.dirname(base), \\\"output/unified_tab_fewnerd_maxlp.json\\\")\\n    with open(out_path, \\\"w\\\") as f:\\n        json.dump(all_results, f, indent=2)\\n    print(f\\\"\\\\nSaved to {out_path}\\\")\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "afd3c16f-90cb-4bd8-b261-43be2853cbf6",
  "isSidechain": false,
  "promptId": "0731b9be-f5e6-4a8a-9a3c-2edafe06629b",
  "type": "user",
  "uuid": "404a8bc5-90f5-42a9-bce0-4771c9ab9944",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"#!/usr/bin/env python3\\\\n\\\\\\\"\\\\\\\"\\\\\\\"Unified tab:fewnerd metrics: gold-filtered, max_LP inst-level rho.\\\\nUses EXACT same code path for all 3 datasets.\\\\\\\"\\\\\\\"\\\\\\\"\\\\n\\\\nimport json\\\\nimport sys\\\\nimport os\\\\nimport numpy as np\\\\nfrom scipy.stats import spearmanr\\\\n\\\\nsys.path.insert(0, '/root/autodl-tmp/struct_self_consist_ie/code')\\\\nfrom evaluation import per_instance_f1\\\\n\\\\nSUBTASK = \\\\\\\"ner\\\\\\\"\\\\n\\\\ndef load_data(path):\\\\n    with open(path) as f:\\\\n        return [json.loads(line) for line in f if line.strip()]\\\\n\\\\ndef compute_metrics(data, label=\\\\\\\"dataset\\\\\\\"):\\\\n    N = len(data)\\\\n    if N == 0:\\\\n        print(f\\\\\\\"  [{label}] No instances!\\\\\\\")\\\\n        return {}\\\\n\\\\n    n_samples = len(data[0][\\\\\\\"samples\\\\\\\"])\\\\n\\\\n    greedy_f1s = []\\\\n    oracle_f1s = []\\\\n    lp_sel_f1s = []\\\\n    degen_f1_flags = []\\\\n    max_lp_per_instance = []\\\\n    mean_lp_per_instance = []\\\\n\\\\n    for inst in data:\\\\n        gold = inst[\\\\\\\"gold\\\\\\\"]\\\\n        greedy = inst[\\\\\\\"greedy\\\\\\\"]\\\\n        samples = inst[\\\\\\\"samples\\\\\\\"]\\\\n\\\\n        g_f1 = per_instance_f1(greedy, gold, SUBTASK)\\\\n        greedy_f1s.append(g_f1)\\\\n\\\\n        sample_f1s = []\\\\n        sample_lps = []\\\\n        for s in samples:\\\\n            f1 = per_instance_f1(s, gold, SUBTASK)\\\\n            sample_f1s.append(f1)\\\\n            lp = s.get(\\\\\\\"mean_logprob\\\\\\\")\\\\n            if lp is None:\\\\n                lp = s.get(\\\\\\\"cumulative_logprob\\\\\\\", -999) / max(s.get(\\\\\\\"n_tokens\\\\\\\", 1), 1)\\\\n            sample_lps.append(lp)\\\\n\\\\n        oracle_f1s.append(max(sample_f1s))\\\\n\\\\n        lp_sel_idx = int(np.argmax(sample_lps))\\\\n        lp_sel_f1s.append(sample_f1s[lp_sel_idx])\\\\n\\\\n        degen_f1_flags.append(len(set(sample_f1s)) == 1)\\\\n\\\\n        max_lp_per_instance.append(max(sample_lps))\\\\n        mean_lp_per_instance.append(float(np.mean(sample_lps)))\\\\n\\\\n    greedy_f1s = np.array(greedy_f1s)\\\\n    oracle_f1s = np.array(oracle_f1s)\\\\n    lp_sel_f1s = np.array(lp_sel_f1s)\\\\n\\\\n    greedy_macro = float(greedy_f1s.mean())\\\\n    oracle_macro = float(oracle_f1s.mean())\\\\n    lp_sel_macro = float(lp_sel_f1s.mean())\\\\n    headroom_pp = (oracle_macro - greedy_macro) * 100\\\\n    lp_delta_pp = (lp_sel_macro - greedy_macro) * 100\\\\n    degen_rate = float(np.mean(degen_f1_flags)) * 100\\\\n\\\\n    rho_max, p_max = spearmanr(max_lp_per_instance, greedy_f1s)\\\\n    rho_mean, p_mean = spearmanr(mean_lp_per_instance, greedy_f1s)\\\\n\\\\n    return {\\\\n        \\\\\\\"n\\\\\\\": N,\\\\n        \\\\\\\"n_samples\\\\\\\": n_samples,\\\\n        \\\\\\\"greedy_f1\\\\\\\": greedy_macro,\\\\n        \\\\\\\"oracle_f1\\\\\\\": oracle_macro,\\\\n        \\\\\\\"lp_sel_f1\\\\\\\": lp_sel_macro,\\\\n        \\\\\\\"headroom_pp\\\\\\\": headroom_pp,\\\\n        \\\\\\\"lp_delta_pp\\\\\\\": lp_delta_pp,\\\\n        \\\\\\\"degen_f1_pct\\\\\\\": degen_rate,\\\\n        \\\\\\\"lp_rho_max\\\\\\\": float(rho_max),\\\\n        \\\\\\\"lp_rho_max_p\\\\\\\": float(p_max),\\\\n        \\\\\\\"lp_rho_mean\\\\\\\": float(rho_mean),\\\\n        \\\\\\\"lp_rho_mean_p\\\\\\\": float(p_mean),\\\\n    }\\\\n\\\\n\\\\nif __name__ == \\\\\\\"__main__\\\\\\\":\\\\n    base = \\\\\\\"/root/autodl-tmp/struct_self_consist_ie/output\\\\\\\"\\\\n\\\\n    datasets = {\\\\n        \\\\\\\"SciERC\\\\\\\": os.path.join(base, \\\\\\\"exp_012_rerun_1024/samples.jsonl\\\\\\\"),\\\\n        \\\\\\\"Few-NERD\\\\\\\": os.path.join(base, \\\\\\\"exp_021_inference/samples.jsonl\\\\\\\"),\\\\n        \\\\\\\"CoNLL_Qwen_N8\\\\\\\": os.path.join(base, \\\\\\\"exp002_conll2003/samples.jsonl\\\\\\\"),\\\\n    }\\\\n\\\\n    all_results = {}\\\\n    for name, path in datasets.items():\\\\n        print(f\\\\\\\"\\\\\\\\n{'='*70}\\\\\\\")\\\\n        print(f\\\\\\\"DATASET: {name}\\\\\\\")\\\\n        print(f\\\\\\\"Path: {path}\\\\\\\")\\\\n        print(f\\\\\\\"{'='*70}\\\\\\\")\\\\n\\\\n        if not os.path.exists(path):\\\\n            print(f\\\\\\\"  ERROR: File not found!\\\\\\\")\\\\n            continue\\\\n\\\\n        data = load_data(path)\\\\n        total = len(data)\\\\n        gold_filtered = [d for d in data if len(d[\\\\\\\"gold\\\\\\\"].get(\\\\\\\"entities\\\\\\\", [])) > 0]\\\\n        n_gf = len(gold_filtered)\\\\n        print(f\\\\\\\"  Total: {total}, Gold-filtered: {n_gf}\\\\\\\")\\\\n\\\\n        r = compute_metrics(gold_filtered, name)\\\\n        all_results[name] = r\\\\n\\\\n        print(f\\\\\\\"  greedy_f1:    {r['greedy_f1']:.6f} ({r['greedy_f1']:.3f})\\\\\\\")\\\\n        print(f\\\\\\\"  oracle_f1:    {r['oracle_f1']:.6f} ({r['oracle_f1']:.3f})\\\\\\\")\\\\n        print(f\\\\\\\"  headroom:     {r['headroom_pp']:.2f}pp\\\\\\\")\\\\n        print(f\\\\\\\"  degen%:       {r['degen_f1_pct']:.1f}%\\\\\\\")\\\\n        print(f\\\\\\\"  lp_rho_max:   {r['lp_rho_max']:.6f} (p={r['lp_rho_max_p']:.2e})\\\\\\\")\\\\n        print(f\\\\\\\"  lp_rho_mean:  {r['lp_rho_mean']:.6f} (p={r['lp_rho_mean_p']:.2e})\\\\\\\")\\\\n        print(f\\\\\\\"  lp_sel_f1:    {r['lp_sel_f1']:.6f} ({r['lp_sel_f1']:.3f})\\\\\\\")\\\\n        print(f\\\\\\\"  lp_delta:     {r['lp_delta_pp']:+.2f}pp\\\\\\\")\\\\n\\\\n    # Summary table\\\\n    print(f\\\\\\\"\\\\\\\\n\\\\\\\\n{'='*70}\\\\\\\")\\\\n    print(\\\\\\\"SUMMARY TABLE (gold-filtered)\\\\\\\")\\\\n    print(f\\\\\\\"{'='*70}\\\\\\\")\\\\n    print(f\\\\\\\"{'Dataset':<20} | {'n':>6} | {'N':>2} | {'greedy':>7} | {'oracle':>7} | {'hdroom':>7} | {'degen%':>6} | {'LP_rho_max':>10} | {'LP_rho_mean':>11} | {'LP_sel':>7} | {'LP_delta':>8}\\\\\\\")\\\\n    print(\\\\\\\"-\\\\\\\" * 120)\\\\n    for name, r in all_results.items():\\\\n        print(f\\\\\\\"{name:<20} | {r['n']:>6} | {r['n_samples']:>2} | {r['greedy_f1']:.4f} | {r['oracle_f1']:.4f} | {r['headroom_pp']:>6.2f}pp | {r['degen_f1_pct']:>5.1f}% | {r['lp_rho_max']:>10.4f} | {r['lp_rho_mean']:>11.4f} | {r['lp_sel_f1']:.4f} | {r['lp_delta_pp']:>+7.2f}pp\\\\\\\")\\\\n\\\\n    # Save\\\\n    out_path = os.path.join(os.path.dirname(base), \\\\\\\"output/unified_tab_fewnerd_maxlp.json\\\\\\\")\\\\n    with open(out_path, \\\\\\\"w\\\\\\\") as f:\\\\n        json.dump(all_results, f, indent=2)\\\\n    print(f\\\\\\\"\\\\\\\\nSaved to {out_path}\\\\\\\")\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.35}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"#!/usr/bin/env python3\\n\\\"\\\"\\\"Unified tab:fewnerd metrics: gold-filtered, max_LP inst-level rho.\\nUses EXACT same code path for all 3 datasets.\\\"\\\"\\\"\\n\\nimport json\\nimport sys\\nimport os\\nimport numpy as np\\nfrom scipy.stats import spearmanr\\n\\nsys.path.insert(0, '/root/autodl-tmp/struct_self_consist_ie/code')\\nfrom evaluation import per_instance_f1\\n\\nSUBTASK = \\\"ner\\\"\\n\\ndef load_data(path):\\n    with open(path) as f:\\n        return [json.loads(line) for line in f if line.strip()]\\n\\ndef compute_metrics(data, label=\\\"dataset\\\"):\\n    N = len(data)\\n    if N == 0:\\n        print(f\\\"  [{label}] No instances!\\\")\\n        return {}\\n\\n    n_samples = len(data[0][\\\"samples\\\"])\\n\\n    greedy_f1s = []\\n    oracle_f1s = []\\n    lp_sel_f1s = []\\n    degen_f1_flags = []\\n    max_lp_per_instance = []\\n    mean_lp_per_instance = []\\n\\n    for inst in data:\\n        gold = inst[\\\"gold\\\"]\\n        greedy = inst[\\\"greedy\\\"]\\n        samples = inst[\\\"samples\\\"]\\n\\n        g_f1 = per_instance_f1(greedy, gold, SUBTASK)\\n        greedy_f1s.append(g_f1)\\n\\n        sample_f1s = []\\n        sample_lps = []\\n        for s in samples:\\n            f1 = per_instance_f1(s, gold, SUBTASK)\\n            sample_f1s.append(f1)\\n            lp = s.get(\\\"mean_logprob\\\")\\n            if lp is None:\\n                lp = s.get(\\\"cumulative_logprob\\\", -999) / max(s.get(\\\"n_tokens\\\", 1), 1)\\n            sample_lps.append(lp)\\n\\n        oracle_f1s.append(max(sample_f1s))\\n\\n        lp_sel_idx = int(np.argmax(sample_lps))\\n        lp_sel_f1s.append(sample_f1s[lp_sel_idx])\\n\\n        degen_f1_flags.append(len(set(sample_f1s)) == 1)\\n\\n        max_lp_per_instance.append(max(sample_lps))\\n        mean_lp_per_instance.append(float(np.mean(sample_lps)))\\n\\n    greedy_f1s = np.array(greedy_f1s)\\n    oracle_f1s = np.array(oracle_f1s)\\n    lp_sel_f1s = np.array(lp_sel_f1s)\\n\\n    greedy_macro = float(greedy_f1s.mean())\\n    oracle_macro = float(oracle_f1s.mean())\\n    lp_sel_macro = float(lp_sel_f1s.mean())\\n    headroom_pp = (oracle_macro - greedy_macro) * 100\\n    lp_delta_pp = (lp_sel_macro - greedy_macro) * 100\\n    degen_rate = float(np.mean(degen_f1_flags)) * 100\\n\\n    rho_max, p_max = spearmanr(max_lp_per_instance, greedy_f1s)\\n    rho_mean, p_mean = spearmanr(mean_lp_per_instance, greedy_f1s)\\n\\n    return {\\n        \\\"n\\\": N,\\n        \\\"n_samples\\\": n_samples,\\n        \\\"greedy_f1\\\": greedy_macro,\\n        \\\"oracle_f1\\\": oracle_macro,\\n        \\\"lp_sel_f1\\\": lp_sel_macro,\\n        \\\"headroom_pp\\\": headroom_pp,\\n        \\\"lp_delta_pp\\\": lp_delta_pp,\\n        \\\"degen_f1_pct\\\": degen_rate,\\n        \\\"lp_rho_max\\\": float(rho_max),\\n        \\\"lp_rho_max_p\\\": float(p_max),\\n        \\\"lp_rho_mean\\\": float(rho_mean),\\n        \\\"lp_rho_mean_p\\\": float(p_mean),\\n    }\\n\\n\\nif __name__ == \\\"__main__\\\":\\n    base = \\\"/root/autodl-tmp/struct_self_consist_ie/output\\\"\\n\\n    datasets = {\\n        \\\"SciERC\\\": os.path.join(base, \\\"exp_012_rerun_1024/samples.jsonl\\\"),\\n        \\\"Few-NERD\\\": os.path.join(base, \\\"exp_021_inference/samples.jsonl\\\"),\\n        \\\"CoNLL_Qwen_N8\\\": os.path.join(base, \\\"exp002_conll2003/samples.jsonl\\\"),\\n    }\\n\\n    all_results = {}\\n    for name, path in datasets.items():\\n        print(f\\\"\\\\n{'='*70}\\\")\\n        print(f\\\"DATASET: {name}\\\")\\n        print(f\\\"Path: {path}\\\")\\n        print(f\\\"{'='*70}\\\")\\n\\n        if not os.path.exists(path):\\n            print(f\\\"  ERROR: File not found!\\\")\\n            continue\\n\\n        data = load_data(path)\\n        total = len(data)\\n        gold_filtered = [d for d in data if len(d[\\\"gold\\\"].get(\\\"entities\\\", [])) > 0]\\n        n_gf = len(gold_filtered)\\n        print(f\\\"  Total: {total}, Gold-filtered: {n_gf}\\\")\\n\\n        r = compute_metrics(gold_filtered, name)\\n        all_results[name] = r\\n\\n        print(f\\\"  greedy_f1:    {r['greedy_f1']:.6f} ({r['greedy_f1']:.3f})\\\")\\n        print(f\\\"  oracle_f1:    {r['oracle_f1']:.6f} ({r['oracle_f1']:.3f})\\\")\\n        print(f\\\"  headroom:     {r['headroom_pp']:.2f}pp\\\")\\n        print(f\\\"  degen%:       {r['degen_f1_pct']:.1f}%\\\")\\n        print(f\\\"  lp_rho_max:   {r['lp_rho_max']:.6f} (p={r['lp_rho_max_p']:.2e})\\\")\\n        print(f\\\"  lp_rho_mean:  {r['lp_rho_mean']:.6f} (p={r['lp_rho_mean_p']:.2e})\\\")\\n        print(f\\\"  lp_sel_f1:    {r['lp_sel_f1']:.6f} ({r['lp_sel_f1']:.3f})\\\")\\n        print(f\\\"  lp_delta:     {r['lp_delta_pp']:+.2f}pp\\\")\\n\\n    # Summary table\\n    print(f\\\"\\\\n\\\\n{'='*70}\\\")\\n    print(\\\"SUMMARY TABLE (gold-filtered)\\\")\\n    print(f\\\"{'='*70}\\\")\\n    print(f\\\"{'Dataset':<20} | {'n':>6} | {'N':>2} | {'greedy':>7} | {'oracle':>7} | {'hdroom':>7} | {'degen%':>6} | {'LP_rho_max':>10} | {'LP_rho_mean':>11} | {'LP_sel':>7} | {'LP_delta':>8}\\\")\\n    print(\\\"-\\\" * 120)\\n    for name, r in all_results.items():\\n        print(f\\\"{name:<20} | {r['n']:>6} | {r['n_samples']:>2} | {r['greedy_f1']:.4f} | {r['oracle_f1']:.4f} | {r['headroom_pp']:>6.2f}pp | {r['degen_f1_pct']:>5.1f}% | {r['lp_rho_max']:>10.4f} | {r['lp_rho_mean']:>11.4f} | {r['lp_sel_f1']:.4f} | {r['lp_delta_pp']:>+7.2f}pp\\\")\\n\\n    # Save\\n    out_path = os.path.join(os.path.dirname(base), \\\"output/unified_tab_fewnerd_maxlp.json\\\")\\n    with open(out_path, \\\"w\\\") as f:\\n        json.dump(all_results, f, indent=2)\\n    print(f\\\"\\\\nSaved to {out_path}\\\")\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"
    }
  },
  "sourceToolAssistantUUID": "afd3c16f-90cb-4bd8-b261-43be2853cbf6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "a97de670-f9a7-4d30-affd-382982b8a334",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 58 · 2026-05-19T13:56:58.844Z_

```json
{
  "parentUuid": "404a8bc5-90f5-42a9-bce0-4771c9ab9944",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "a9a0f732-3012-46e9-b5a9-b7ffb72602d0",
  "timestamp": "2026-05-19T13:56:58.844Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "a97de670-f9a7-4d30-affd-382982b8a334",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 59 · 2026-05-19T13:57:48.535Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have critical data. Let me connect the dots for each investigation:

## Investigation 1: SciERC AUROC Table 1 vs registry

The paper Table 1 SciERC AUROC:
- VC: .663
- SJ: .650
- FK: .602
- EM: .614
- LP: .578

exp_012_rerun_1024 (NER full, auroc_5signal.json):
- VC: .684
- SJ: .692


- FK: .629
- EM: .749
- LP: .578

exp_015_metrics_expansion (NER) shows another set of values with voting and individual signal AUROCs, while exp_015_v2 gives yet different numbers for the same signals. These variations across experiments suggest either different preprocessing, model configurations, or evaluation methodologies are being used.

Now I'm seeing exp_015_v2 continued with VC and LP AUROC values, and I'm realizing there are at least four distinct AUROC computations across different sources—the paper's Table 1, exp_012_rerun_1024, exp_015_metrics_expansion, and exp_015_v2—and none of them align perfectly. The paper's provenance indicates Table 1 should derive from exp_015_v2, but the actual values don't match up, which suggests either a transcription error or a mismatch in which experiment was actually used.

Looking more carefully at the ρ values, the paper's correlation coefficients do match exp_012_rerun_1024 exactly, so that experiment is definitely the source for those metrics. For AUROC though, exp_015_metrics_expansion used truncated data (max_tokens=512), while exp_012_rerun_1024 was the corrected full-token version, and the AUROC values from exp_015_metrics_expansion still don't align with what appears in the paper.

I'm wondering if the paper's AUROC values might have been computed differently or averaged across multiple runs in a way that's not matching any single experiment I can find. Let me check whether there's a different AUROC calculation method being used—the eval script uses F1 >= 1.0 as the binary threshold, but maybe exp_015_metrics_expansion applied something different. Also, I just realized that exp_015_metrics_expansion actually pulled from the original exp_012_logprob data with max_tokens=512, not from exp_012_rerun_1024, so that's another source of divergence.

Looking at the exp_015_v2 results, those "avg" values suggest some kind of averaging was happening. But when I try to work backwards from the paper's reported numbers—like averaging NER and RE scores together for each dataset—I'm not getting matches either. The paper values just don't seem to come from any straightforward combination of the experiments I'm seeing.

Now checking if these could be conditional AUROC values instead. The VC score of .662 from the conditional NER results is suspiciously close to the paper's .663, though not exact. And LP's .578 matches the full NER value perfectly. But the rest of the paper values don't cleanly align with either the full or conditional metrics—it's a mixed bag that doesn't follow a consistent pattern.

Let me reconsider whether the paper's Table 1 might be pulling ρ and AUROC from different experimental runs or conditions altogether. The ρ values clearly match exp_012_rerun_1024 NER full, but the AUROC values seem to come from somewhere else. I should look more carefully at the recompute_table_metrics.py script to see how it actually generates the table metrics.

Analyzing the script logic...

Actually, I'm realizing recompute_table_metrics.py focuses on greedy F1, oracle F1, and LP selection metrics for the fewnerd table rather than computing AUROC for the five signals. I need to check unified_metrics.py instead, which might be where the authoritative computations happen. Let me also consider whether the paper values could be multi-seed averages, or if the AUROC values in Table 1 might actually come from a completely different experiment than exp_015_v2, since the values I'm seeing there don't match the paper either.

Wait, I'm noticing something important—exp_015_v2 has much higher AUROC values than exp_012_rerun_1024, and that's because exp_015_v2 used truncated data with max_tokens=512, which inflated the metrics due to truncation artifacts. The paper's Table 1 appears to use ρ from the corrected exp_012_rerun_1024 run, but the AUROC values don't align with either experiment cleanly.

Looking at the actual numbers, the paper shows VC .663, SJ .650, FK .602, EM .614, LP .578, while exp_012_rerun_1024 gives VC .684, SJ .692, FK .629, EM .749, LP .578. The AUROC column in the paper seems to contain outdated values that weren't properly synced when the ρ values were corrected to use the newer experiment.

I'm wondering if the paper values might be a 3-seed average from exp_012_rerun_1024, but I need to verify whether those seed-specific experiments actually exist and have the necessary AUROC data. Let me search through the available seed variants and check if there are any cached outputs from the metrics scripts that could clarify this.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a9a0f732-3012-46e9-b5a9-b7ffb72602d0",
  "isSidechain": false,
  "requestId": "req_011CbC3WN6LBa7eJXMsfN9Ar",
  "type": "assistant",
  "uuid": "1769e961-aac7-4487-b120-08fec11dd3fb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "a97de670-f9a7-4d30-affd-382982b8a334",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015zDHJsPeTzXeopt96Bt3uF",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9924,
      "cache_read_input_tokens": 55840,
      "output_tokens": 3532,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 9924,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3532,
          "cache_read_input_tokens": 55840,
          "cache_creation_input_tokens": 9924,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 9924
          },
          "type": "message"
        }
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

_source line 60 · 2026-05-19T13:57:48.996Z_

Found key data. The paper Table 1 AUROC doesn't match exp_012_rerun_1024. Now let me check multi-seed sources and run more specific queries.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1769e961-aac7-4487-b120-08fec11dd3fb",
  "isSidechain": false,
  "requestId": "req_011CbC3WN6LBa7eJXMsfN9Ar",
  "type": "assistant",
  "uuid": "a541e495-4304-410e-b971-701b0ffc69ae",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "a97de670-f9a7-4d30-affd-382982b8a334",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015zDHJsPeTzXeopt96Bt3uF",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9924,
      "cache_read_input_tokens": 55840,
      "output_tokens": 3532,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 9924,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3532,
          "cache_read_input_tokens": 55840,
          "cache_creation_input_tokens": 9924,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 9924
          },
          "type": "message"
        }
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

_source line 61 · 2026-05-19T13:57:58.887Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01W1eKu87x3TXpWqgPztAw7m`</summary>

```json
{
  "command": "REGFILE=\"/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie/a97de670-f9a7-4d30-affd-382982b8a334/tool-results/mcp-agent-ml-research-read_registry-1779198876363.txt\"\npython3 -c \"\nimport json\ndata = json.loads(json.loads(open('$REGFILE').read())['result'])\nexps = data['data']['experiments']\n\n# Check r1024 seed variants for AUROC\nfor eid in ['exp_001_seed42_v2_r1024', 'exp_001_seed123_v2_r1024', 'exp_001_seed456_v2_ner_r1024']:\n    exp = exps.get(eid, {})\n    m = exp.get('metrics', {})\n    print(f'=== {eid} ===')\n    # Look for AUROC keys\n    auroc_data = {k: v for k, v in m.items() if 'auroc' in k.lower() or 'AUROC' in str(v)}\n    if auroc_data:\n        print(json.dumps(auroc_data, indent=2)[:2000])\n    else:\n        print(f'  No AUROC keys. All keys: {list(m.keys())[:20]}')\n    print()\n\n# Check exp_016_signal_ensemble for selection data\nexp = exps.get('exp_016_signal_ensemble', {})\nm = exp.get('metrics', {})\nprint('=== exp_016_signal_ensemble ===')\nprint(json.dumps(m, indent=2)[:3000])\nprint()\n\n# Check exp_016_rerun_1024_bootstrap for CoNLL LP\nexp = exps.get('exp_016_rerun_1024_bootstrap', {})\nm = exp.get('metrics', {})\nsel_keys = {k: v for k, v in m.items() if 'selection' in k.lower() or 'sel' in k.lower() or 'lp' in k.lower() or 'logprob' in k.lower()}\nprint('=== exp_016_rerun_1024_bootstrap (selection) ===')\nprint(json.dumps(sel_keys, indent=2)[:3000])\n\"\n",
  "description": "Check seed-variant AUROC and selection data"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a541e495-4304-410e-b971-701b0ffc69ae",
  "isSidechain": false,
  "requestId": "req_011CbC3WN6LBa7eJXMsfN9Ar",
  "type": "assistant",
  "uuid": "3cf84c92-bf69-4258-9f6c-af85a9d5057d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "a97de670-f9a7-4d30-affd-382982b8a334",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015zDHJsPeTzXeopt96Bt3uF",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9924,
      "cache_read_input_tokens": 55840,
      "output_tokens": 3532,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 9924,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3532,
          "cache_read_input_tokens": 55840,
          "cache_creation_input_tokens": 9924,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 9924
          },
          "type": "message"
        }
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

_source line 62 · 2026-05-19T13:57:58.969Z_

<details><summary>↩ Tool result · `toolu_01W1eKu87x3TXpWqgPztAw7m`</summary>

```text
=== exp_001_seed42_v2_r1024 ===
  No AUROC keys. All keys: ['greedy_f1', 'oracle_f1', 'softjaccard_rho_full', 'fleiss_rho_full', 'logprob_rho_full', 'softjaccard_rho_cond', 'fleiss_rho_cond', 'logprob_rho_cond', 'verdict']

=== exp_001_seed123_v2_r1024 ===
  No AUROC keys. All keys: []

=== exp_001_seed456_v2_ner_r1024 ===
  No AUROC keys. All keys: []

=== exp_016_signal_ensemble ===
{
  "sj_logprob_pearson_ner": 0.57,
  "sj_logprob_pearson_re": 0.42,
  "best_linear_ner": {
    "combo": "SJ+voting_conf",
    "alpha": 0.3,
    "rho": 0.489
  },
  "best_linear_re": {
    "combo": "voting_conf+logprob",
    "alpha": 0.6,
    "rho": 0.429
  },
  "ensemble_ner_auroc": 0.735,
  "ensemble_re_auroc": 0.719,
  "best_single_ner_auroc": 0.7,
  "best_single_re_auroc": 0.721,
  "ensemble_ner_delta": 0.035,
  "selection_f1_ner": {
    "greedy": 0.609,
    "logprob": 0.609,
    "sj": 0.604,
    "ensemble": 0.604,
    "voting": 0.596,
    "random": 0.58,
    "oracle": 0.769
  },
  "selection_f1_re": {
    "logprob": 0.397,
    "greedy": 0.374,
    "sj": 0.368,
    "ensemble": 0.367,
    "voting": 0.338,
    "random": 0.338,
    "oracle": 0.561
  },
  "diagnosis": "SJ+voting_conf linear combo boosts NER \u03c1 to 0.489 (+23%). RE: logprob-best is ONLY method beating greedy (0.397 vs 0.374). Ensemble AUROC +0.035 on NER. Oracle gap still huge."
}

=== exp_016_rerun_1024_bootstrap (selection) ===
{
  "ner_logprob_vs_greedy_delta": 0.006
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3cf84c92-bf69-4258-9f6c-af85a9d5057d",
  "isSidechain": false,
  "promptId": "0731b9be-f5e6-4a8a-9a3c-2edafe06629b",
  "type": "user",
  "uuid": "e694a994-c964-44c3-b3e3-952a9a569e93",
  "toolUseResult": {
    "stdout": "=== exp_001_seed42_v2_r1024 ===\n  No AUROC keys. All keys: ['greedy_f1', 'oracle_f1', 'softjaccard_rho_full', 'fleiss_rho_full', 'logprob_rho_full', 'softjaccard_rho_cond', 'fleiss_rho_cond', 'logprob_rho_cond', 'verdict']\n\n=== exp_001_seed123_v2_r1024 ===\n  No AUROC keys. All keys: []\n\n=== exp_001_seed456_v2_ner_r1024 ===\n  No AUROC keys. All keys: []\n\n=== exp_016_signal_ensemble ===\n{\n  \"sj_logprob_pearson_ner\": 0.57,\n  \"sj_logprob_pearson_re\": 0.42,\n  \"best_linear_ner\": {\n    \"combo\": \"SJ+voting_conf\",\n    \"alpha\": 0.3,\n    \"rho\": 0.489\n  },\n  \"best_linear_re\": {\n    \"combo\": \"voting_conf+logprob\",\n    \"alpha\": 0.6,\n    \"rho\": 0.429\n  },\n  \"ensemble_ner_auroc\": 0.735,\n  \"ensemble_re_auroc\": 0.719,\n  \"best_single_ner_auroc\": 0.7,\n  \"best_single_re_auroc\": 0.721,\n  \"ensemble_ner_delta\": 0.035,\n  \"selection_f1_ner\": {\n    \"greedy\": 0.609,\n    \"logprob\": 0.609,\n    \"sj\": 0.604,\n    \"ensemble\": 0.604,\n    \"voting\": 0.596,\n    \"random\": 0.58,\n    \"oracle\": 0.769\n  },\n  \"selection_f1_re\": {\n    \"logprob\": 0.397,\n    \"greedy\": 0.374,\n    \"sj\": 0.368,\n    \"ensemble\": 0.367,\n    \"voting\": 0.338,\n    \"random\": 0.338,\n    \"oracle\": 0.561\n  },\n  \"diagnosis\": \"SJ+voting_conf linear combo boosts NER \\u03c1 to 0.489 (+23%). RE: logprob-best is ONLY method beating greedy (0.397 vs 0.374). Ensemble AUROC +0.035 on NER. Oracle gap still huge.\"\n}\n\n=== exp_016_rerun_1024_bootstrap (selection) ===\n{\n  \"ner_logprob_vs_greedy_delta\": 0.006\n}",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "3cf84c92-bf69-4258-9f6c-af85a9d5057d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "a97de670-f9a7-4d30-affd-382982b8a334",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 63 · 2026-05-19T13:58:00.312Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_015KRvokU73UuH54szMJ9K5M`</summary>

```json
{
  "server": "autodl-5090",
  "command": "find /root/autodl-tmp/struct_self_consist_ie/output -name \"unified_tab*\" -o -name \"*table1*\" -o -name \"*tab_qe*\" -o -name \"*auroc*json\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e694a994-c964-44c3-b3e3-952a9a569e93",
  "isSidechain": false,
  "requestId": "req_011CbC3WN6LBa7eJXMsfN9Ar",
  "type": "assistant",
  "uuid": "2690d35d-fceb-42e9-8e85-4f7528066d8e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "a97de670-f9a7-4d30-affd-382982b8a334",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015zDHJsPeTzXeopt96Bt3uF",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9924,
      "cache_read_input_tokens": 55840,
      "output_tokens": 3532,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 9924,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3532,
          "cache_read_input_tokens": 55840,
          "cache_creation_input_tokens": 9924,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 9924
          },
          "type": "message"
        }
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

_source line 64 · 2026-05-19T13:58:00.687Z_

<details><summary>↩ Tool result · `toolu_015KRvokU73UuH54szMJ9K5M`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/struct_self_consist_ie/output/exp_012_rerun_1024/auroc_5signal.json\\n/root/autodl-tmp/struct_self_consist_ie/output/d114_auroc_investigation/unified_auroc.json\\n/root/autodl-tmp/struct_self_consist_ie/output/d114_auroc_investigation/table1_update.md\\n/root/autodl-tmp/struct_self_consist_ie/output/unified_tab_fewnerd_maxlp.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.36}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2690d35d-fceb-42e9-8e85-4f7528066d8e",
  "isSidechain": false,
  "promptId": "0731b9be-f5e6-4a8a-9a3c-2edafe06629b",
  "type": "user",
  "uuid": "6dc1e596-5b09-44c4-8e84-895040284906",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"/root/autodl-tmp/struct_self_consist_ie/output/exp_012_rerun_1024/auroc_5signal.json\\\\n/root/autodl-tmp/struct_self_consist_ie/output/d114_auroc_investigation/unified_auroc.json\\\\n/root/autodl-tmp/struct_self_consist_ie/output/d114_auroc_investigation/table1_update.md\\\\n/root/autodl-tmp/struct_self_consist_ie/output/unified_tab_fewnerd_maxlp.json\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.36}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/struct_self_consist_ie/output/exp_012_rerun_1024/auroc_5signal.json\\n/root/autodl-tmp/struct_self_consist_ie/output/d114_auroc_investigation/unified_auroc.json\\n/root/autodl-tmp/struct_self_consist_ie/output/d114_auroc_investigation/table1_update.md\\n/root/autodl-tmp/struct_self_consist_ie/output/unified_tab_fewnerd_maxlp.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.36}}"
    }
  },
  "sourceToolAssistantUUID": "2690d35d-fceb-42e9-8e85-4f7528066d8e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "a97de670-f9a7-4d30-affd-382982b8a334",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 65 · 2026-05-19T13:58:01.089Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01UrN8pQ3kfMQjkuuTSqb5y1`</summary>

```json
{
  "server": "autodl-5090",
  "command": "cat /root/autodl-tmp/struct_self_consist_ie/code/unified_metrics.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6dc1e596-5b09-44c4-8e84-895040284906",
  "isSidechain": false,
  "requestId": "req_011CbC3WN6LBa7eJXMsfN9Ar",
  "type": "assistant",
  "uuid": "676c397c-2a93-43ee-aad2-21c2ce46422d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "a97de670-f9a7-4d30-affd-382982b8a334",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015zDHJsPeTzXeopt96Bt3uF",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9924,
      "cache_read_input_tokens": 55840,
      "output_tokens": 3532,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 9924,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3532,
          "cache_read_input_tokens": 55840,
          "cache_creation_input_tokens": 9924,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 9924
          },
          "type": "message"
        }
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

_source line 66_

```json
{
  "type": "last-prompt",
  "leafUuid": "676c397c-2a93-43ee-aad2-21c2ce46422d",
  "sessionId": "a97de670-f9a7-4d30-affd-382982b8a334"
}
```

---

### Runtime record

_source line 67_

```json
{
  "type": "ai-title",
  "aiTitle": "Audit data inconsistencies in paper tables",
  "sessionId": "a97de670-f9a7-4d30-affd-382982b8a334"
}
```

---

### Tool result

_source line 68 · 2026-05-19T13:58:01.453Z_

<details><summary>↩ Tool result · `toolu_01UrN8pQ3kfMQjkuuTSqb5y1`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"Unified F1 / degeneracy / data-loading module.\\n\\nThis is the single source of truth for entity F1, degeneracy detection,\\nand data loading across all analysis scripts. All analysis scripts must\\nimport from this module instead of defining their own implementations.\\n\\nConventions:\\n  - Entity = (start, end, type) tuple, exact match\\n  - F1 = micro per-instance: 2*P*R/(P+R)\\n  - Degeneracy = constant-F1 gold-filtered (all N sample F1s identical)\\n  - gold_filter = skip instances where gold entities list is empty\\n\\\"\\\"\\\"\\n\\nimport json\\nimport numpy as np\\n\\n\\ndef compute_entity_f1(pred_entities, gold_entities):\\n    \\\"\\\"\\\"Span-based entity F1 for a single instance.\\n\\n    Args:\\n        pred_entities: list of dicts with keys start, end, type.\\n        gold_entities: list of dicts with keys start, end, type.\\n\\n    Returns:\\n        float F1 in [0, 1].\\n    \\\"\\\"\\\"\\n    pred_set = {(e[\\\"start\\\"], e[\\\"end\\\"], e[\\\"type\\\"]) for e in pred_entities}\\n    gold_set = {(e[\\\"start\\\"], e[\\\"end\\\"], e[\\\"type\\\"]) for e in gold_entities}\\n    if not gold_set and not pred_set:\\n        return 1.0\\n    if not gold_set or not pred_set:\\n        return 0.0\\n    tp = len(pred_set & gold_set)\\n    if tp == 0:\\n        return 0.0\\n    p = tp / len(pred_set)\\n    r = tp / len(gold_set)\\n    return 2 * p * r / (p + r)\\n\\n\\ndef compute_degeneracy(sample_f1_list):\\n    \\\"\\\"\\\"Check if an instance is degenerate (constant-F1 gold-filtered).\\n\\n    All N sample F1 values are identical (after rounding to 10 decimals\\n    to avoid float noise) -> degenerate.\\n\\n    Args:\\n        sample_f1_list: list of float F1 values, one per sample.\\n\\n    Returns:\\n        bool, True if degenerate.\\n    \\\"\\\"\\\"\\n    return len(set(round(f, 10) for f in sample_f1_list)) <= 1\\n\\n\\ndef load_and_filter(path, gold_filter=True):\\n    \\\"\\\"\\\"Load samples.jsonl and optionally filter out gold-empty instances.\\n\\n    Args:\\n        path: path to samples.jsonl\\n        gold_filter: if True, skip instances with empty gold entities.\\n\\n    Returns:\\n        list of instance dicts.\\n    \\\"\\\"\\\"\\n    instances = []\\n    with open(path) as f:\\n        for line in f:\\n            if not line.strip():\\n                continue\\n            obj = json.loads(line)\\n            if gold_filter and not obj[\\\"gold\\\"].get(\\\"entities\\\", []):\\n                continue\\n            instances.append(obj)\\n    return instances\\n\\n\\ndef compute_sample_f1s(inst, n_samples=None):\\n    \\\"\\\"\\\"Compute per-sample F1 list for an instance.\\n\\n    Args:\\n        inst: instance dict with keys gold, samples.\\n        n_samples: if set, only use first n_samples.\\n\\n    Returns:\\n        list of float F1 values.\\n    \\\"\\\"\\\"\\n    gold_ents = inst[\\\"gold\\\"][\\\"entities\\\"]\\n    samples = inst[\\\"samples\\\"][:n_samples] if n_samples else inst[\\\"samples\\\"]\\n    return [compute_entity_f1(s.get(\\\"entities\\\", []), gold_ents) for s in samples]\\n\\n\\ndef compute_greedy_f1(inst):\\n    \\\"\\\"\\\"Compute greedy F1 for an instance.\\\"\\\"\\\"\\n    gold_ents = inst[\\\"gold\\\"][\\\"entities\\\"]\\n    greedy = inst.get(\\\"greedy\\\", inst[\\\"samples\\\"][0])\\n    return compute_entity_f1(greedy.get(\\\"entities\\\", []), gold_ents)\\n\\n\\ndef get_lp_selection_idx(inst, n_samples=None):\\n    \\\"\\\"\\\"Get the index of the sample with highest mean_logprob.\\\"\\\"\\\"\\n    samples = inst[\\\"samples\\\"][:n_samples] if n_samples else inst[\\\"samples\\\"]\\n    best_idx = 0\\n    best_lp = -float(\\\"inf\\\")\\n    for i, s in enumerate(samples):\\n        lp = s.get(\\\"mean_logprob\\\", None)\\n        if lp is None and \\\"logprobs\\\" in inst and i < len(inst[\\\"logprobs\\\"]):\\n            lp = inst[\\\"logprobs\\\"][i]\\n        if lp is not None and np.isfinite(lp) and lp > best_lp:\\n            best_lp = lp\\n            best_idx = i\\n    return best_idx\\n\\n\\ndef bootstrap_ci(values, n_boot=2000, ci=0.95, seed=42):\\n    \\\"\\\"\\\"Bootstrap confidence interval for the mean.\\\"\\\"\\\"\\n    arr = np.array(values)\\n    n = len(arr)\\n    if n == 0:\\n        return {\\\"mean\\\": 0.0, \\\"ci_lo\\\": 0.0, \\\"ci_hi\\\": 0.0}\\n    rng = np.random.RandomState(seed)\\n    boot_means = np.array([arr[rng.randint(0, n, n)].mean() for _ in range(n_boot)])\\n    boot_means.sort()\\n    lo = boot_means[int((1 - ci) / 2 * n_boot)]\\n    hi = boot_means[int((1 + ci) / 2 * n_boot)]\\n    return {\\\"mean\\\": float(arr.mean()), \\\"ci_lo\\\": float(lo), \\\"ci_hi\\\": float(hi)}\\n\\n\\ndef bootstrap_delta_ci(a, b, n_boot=2000, ci=0.95, seed=42):\\n    \\\"\\\"\\\"Bootstrap CI for mean(a) - mean(b), paired.\\\"\\\"\\\"\\n    a_arr, b_arr = np.array(a), np.array(b)\\n    n = len(a_arr)\\n    if n == 0:\\n        return {\\\"delta\\\": 0.0, \\\"ci_lo\\\": 0.0, \\\"ci_hi\\\": 0.0}\\n    rng = np.random.RandomState(seed)\\n    deltas = []\\n    for _ in range(n_boot):\\n        idx = rng.randint(0, n, n)\\n        deltas.append(float(a_arr[idx].mean() - b_arr[idx].mean()))\\n    deltas.sort()\\n    lo = deltas[int((1 - ci) / 2 * n_boot)]\\n    hi = deltas[int((1 + ci) / 2 * n_boot)]\\n    return {\\\"delta\\\": float(a_arr.mean() - b_arr.mean()), \\\"ci_lo\\\": float(lo), \\\"ci_hi\\\": float(hi)}\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.36}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "676c397c-2a93-43ee-aad2-21c2ce46422d",
  "isSidechain": false,
  "promptId": "0731b9be-f5e6-4a8a-9a3c-2edafe06629b",
  "type": "user",
  "uuid": "be8a010d-fc93-4c54-8e5d-b6d3e99ff757",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"\\\\\\\"\\\\\\\"\\\\\\\"Unified F1 / degeneracy / data-loading module.\\\\n\\\\nThis is the single source of truth for entity F1, degeneracy detection,\\\\nand data loading across all analysis scripts. All analysis scripts must\\\\nimport from this module instead of defining their own implementations.\\\\n\\\\nConventions:\\\\n  - Entity = (start, end, type) tuple, exact match\\\\n  - F1 = micro per-instance: 2*P*R/(P+R)\\\\n  - Degeneracy = constant-F1 gold-filtered (all N sample F1s identical)\\\\n  - gold_filter = skip instances where gold entities list is empty\\\\n\\\\\\\"\\\\\\\"\\\\\\\"\\\\n\\\\nimport json\\\\nimport numpy as np\\\\n\\\\n\\\\ndef compute_entity_f1(pred_entities, gold_entities):\\\\n    \\\\\\\"\\\\\\\"\\\\\\\"Span-based entity F1 for a single instance.\\\\n\\\\n    Args:\\\\n        pred_entities: list of dicts with keys start, end, type.\\\\n        gold_entities: list of dicts with keys start, end, type.\\\\n\\\\n    Returns:\\\\n        float F1 in [0, 1].\\\\n    \\\\\\\"\\\\\\\"\\\\\\\"\\\\n    pred_set = {(e[\\\\\\\"start\\\\\\\"], e[\\\\\\\"end\\\\\\\"], e[\\\\\\\"type\\\\\\\"]) for e in pred_entities}\\\\n    gold_set = {(e[\\\\\\\"start\\\\\\\"], e[\\\\\\\"end\\\\\\\"], e[\\\\\\\"type\\\\\\\"]) for e in gold_entities}\\\\n    if not gold_set and not pred_set:\\\\n        return 1.0\\\\n    if not gold_set or not pred_set:\\\\n        return 0.0\\\\n    tp = len(pred_set & gold_set)\\\\n    if tp == 0:\\\\n        return 0.0\\\\n    p = tp / len(pred_set)\\\\n    r = tp / len(gold_set)\\\\n    return 2 * p * r / (p + r)\\\\n\\\\n\\\\ndef compute_degeneracy(sample_f1_list):\\\\n    \\\\\\\"\\\\\\\"\\\\\\\"Check if an instance is degenerate (constant-F1 gold-filtered).\\\\n\\\\n    All N sample F1 values are identical (after rounding to 10 decimals\\\\n    to avoid float noise) -> degenerate.\\\\n\\\\n    Args:\\\\n        sample_f1_list: list of float F1 values, one per sample.\\\\n\\\\n    Returns:\\\\n        bool, True if degenerate.\\\\n    \\\\\\\"\\\\\\\"\\\\\\\"\\\\n    return len(set(round(f, 10) for f in sample_f1_list)) <= 1\\\\n\\\\n\\\\ndef load_and_filter(path, gold_filter=True):\\\\n    \\\\\\\"\\\\\\\"\\\\\\\"Load samples.jsonl and optionally filter out gold-empty instances.\\\\n\\\\n    Args:\\\\n        path: path to samples.jsonl\\\\n        gold_filter: if True, skip instances with empty gold entities.\\\\n\\\\n    Returns:\\\\n        list of instance dicts.\\\\n    \\\\\\\"\\\\\\\"\\\\\\\"\\\\n    instances = []\\\\n    with open(path) as f:\\\\n        for line in f:\\\\n            if not line.strip():\\\\n                continue\\\\n            obj = json.loads(line)\\\\n            if gold_filter and not obj[\\\\\\\"gold\\\\\\\"].get(\\\\\\\"entities\\\\\\\", []):\\\\n                continue\\\\n            instances.append(obj)\\\\n    return instances\\\\n\\\\n\\\\ndef compute_sample_f1s(inst, n_samples=None):\\\\n    \\\\\\\"\\\\\\\"\\\\\\\"Compute per-sample F1 list for an instance.\\\\n\\\\n    Args:\\\\n        inst: instance dict with keys gold, samples.\\\\n        n_samples: if set, only use first n_samples.\\\\n\\\\n    Returns:\\\\n        list of float F1 values.\\\\n    \\\\\\\"\\\\\\\"\\\\\\\"\\\\n    gold_ents = inst[\\\\\\\"gold\\\\\\\"][\\\\\\\"entities\\\\\\\"]\\\\n    samples = inst[\\\\\\\"samples\\\\\\\"][:n_samples] if n_samples else inst[\\\\\\\"samples\\\\\\\"]\\\\n    return [compute_entity_f1(s.get(\\\\\\\"entities\\\\\\\", []), gold_ents) for s in samples]\\\\n\\\\n\\\\ndef compute_greedy_f1(inst):\\\\n    \\\\\\\"\\\\\\\"\\\\\\\"Compute greedy F1 for an instance.\\\\\\\"\\\\\\\"\\\\\\\"\\\\n    gold_ents = inst[\\\\\\\"gold\\\\\\\"][\\\\\\\"entities\\\\\\\"]\\\\n    greedy = inst.get(\\\\\\\"greedy\\\\\\\", inst[\\\\\\\"samples\\\\\\\"][0])\\\\n    return compute_entity_f1(greedy.get(\\\\\\\"entities\\\\\\\", []), gold_ents)\\\\n\\\\n\\\\ndef get_lp_selection_idx(inst, n_samples=None):\\\\n    \\\\\\\"\\\\\\\"\\\\\\\"Get the index of the sample with highest mean_logprob.\\\\\\\"\\\\\\\"\\\\\\\"\\\\n    samples = inst[\\\\\\\"samples\\\\\\\"][:n_samples] if n_samples else inst[\\\\\\\"samples\\\\\\\"]\\\\n    best_idx = 0\\\\n    best_lp = -float(\\\\\\\"inf\\\\\\\")\\\\n    for i, s in enumerate(samples):\\\\n        lp = s.get(\\\\\\\"mean_logprob\\\\\\\", None)\\\\n        if lp is None and \\\\\\\"logprobs\\\\\\\" in inst and i < len(inst[\\\\\\\"logprobs\\\\\\\"]):\\\\n            lp = inst[\\\\\\\"logprobs\\\\\\\"][i]\\\\n        if lp is not None and np.isfinite(lp) and lp > best_lp:\\\\n            best_lp = lp\\\\n            best_idx = i\\\\n    return best_idx\\\\n\\\\n\\\\ndef bootstrap_ci(values, n_boot=2000, ci=0.95, seed=42):\\\\n    \\\\\\\"\\\\\\\"\\\\\\\"Bootstrap confidence interval for the mean.\\\\\\\"\\\\\\\"\\\\\\\"\\\\n    arr = np.array(values)\\\\n    n = len(arr)\\\\n    if n == 0:\\\\n        return {\\\\\\\"mean\\\\\\\": 0.0, \\\\\\\"ci_lo\\\\\\\": 0.0, \\\\\\\"ci_hi\\\\\\\": 0.0}\\\\n    rng = np.random.RandomState(seed)\\\\n    boot_means = np.array([arr[rng.randint(0, n, n)].mean() for _ in range(n_boot)])\\\\n    boot_means.sort()\\\\n    lo = boot_means[int((1 - ci) / 2 * n_boot)]\\\\n    hi = boot_means[int((1 + ci) / 2 * n_boot)]\\\\n    return {\\\\\\\"mean\\\\\\\": float(arr.mean()), \\\\\\\"ci_lo\\\\\\\": float(lo), \\\\\\\"ci_hi\\\\\\\": float(hi)}\\\\n\\\\n\\\\ndef bootstrap_delta_ci(a, b, n_boot=2000, ci=0.95, seed=42):\\\\n    \\\\\\\"\\\\\\\"\\\\\\\"Bootstrap CI for mean(a) - mean(b), paired.\\\\\\\"\\\\\\\"\\\\\\\"\\\\n    a_arr, b_arr = np.array(a), np.array(b)\\\\n    n = len(a_arr)\\\\n    if n == 0:\\\\n        return {\\\\\\\"delta\\\\\\\": 0.0, \\\\\\\"ci_lo\\\\\\\": 0.0, \\\\\\\"ci_hi\\\\\\\": 0.0}\\\\n    rng = np.random.RandomState(seed)\\\\n    deltas = []\\\\n    for _ in range(n_boot):\\\\n        idx = rng.randint(0, n, n)\\\\n        deltas.append(float(a_arr[idx].mean() - b_arr[idx].mean()))\\\\n    deltas.sort()\\\\n    lo = deltas[int((1 - ci) / 2 * n_boot)]\\\\n    hi = deltas[int((1 + ci) / 2 * n_boot)]\\\\n    return {\\\\\\\"delta\\\\\\\": float(a_arr.mean() - b_arr.mean()), \\\\\\\"ci_lo\\\\\\\": float(lo), \\\\\\\"ci_hi\\\\\\\": float(hi)}\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.36}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"Unified F1 / degeneracy / data-loading module.\\n\\nThis is the single source of truth for entity F1, degeneracy detection,\\nand data loading across all analysis scripts. All analysis scripts must\\nimport from this module instead of defining their own implementations.\\n\\nConventions:\\n  - Entity = (start, end, type) tuple, exact match\\n  - F1 = micro per-instance: 2*P*R/(P+R)\\n  - Degeneracy = constant-F1 gold-filtered (all N sample F1s identical)\\n  - gold_filter = skip instances where gold entities list is empty\\n\\\"\\\"\\\"\\n\\nimport json\\nimport numpy as np\\n\\n\\ndef compute_entity_f1(pred_entities, gold_entities):\\n    \\\"\\\"\\\"Span-based entity F1 for a single instance.\\n\\n    Args:\\n        pred_entities: list of dicts with keys start, end, type.\\n        gold_entities: list of dicts with keys start, end, type.\\n\\n    Returns:\\n        float F1 in [0, 1].\\n    \\\"\\\"\\\"\\n    pred_set = {(e[\\\"start\\\"], e[\\\"end\\\"], e[\\\"type\\\"]) for e in pred_entities}\\n    gold_set = {(e[\\\"start\\\"], e[\\\"end\\\"], e[\\\"type\\\"]) for e in gold_entities}\\n    if not gold_set and not pred_set:\\n        return 1.0\\n    if not gold_set or not pred_set:\\n        return 0.0\\n    tp = len(pred_set & gold_set)\\n    if tp == 0:\\n        return 0.0\\n    p = tp / len(pred_set)\\n    r = tp / len(gold_set)\\n    return 2 * p * r / (p + r)\\n\\n\\ndef compute_degeneracy(sample_f1_list):\\n    \\\"\\\"\\\"Check if an instance is degenerate (constant-F1 gold-filtered).\\n\\n    All N sample F1 values are identical (after rounding to 10 decimals\\n    to avoid float noise) -> degenerate.\\n\\n    Args:\\n        sample_f1_list: list of float F1 values, one per sample.\\n\\n    Returns:\\n        bool, True if degenerate.\\n    \\\"\\\"\\\"\\n    return len(set(round(f, 10) for f in sample_f1_list)) <= 1\\n\\n\\ndef load_and_filter(path, gold_filter=True):\\n    \\\"\\\"\\\"Load samples.jsonl and optionally filter out gold-empty instances.\\n\\n    Args:\\n        path: path to samples.jsonl\\n        gold_filter: if True, skip instances with empty gold entities.\\n\\n    Returns:\\n        list of instance dicts.\\n    \\\"\\\"\\\"\\n    instances = []\\n    with open(path) as f:\\n        for line in f:\\n            if not line.strip():\\n                continue\\n            obj = json.loads(line)\\n            if gold_filter and not obj[\\\"gold\\\"].get(\\\"entities\\\", []):\\n                continue\\n            instances.append(obj)\\n    return instances\\n\\n\\ndef compute_sample_f1s(inst, n_samples=None):\\n    \\\"\\\"\\\"Compute per-sample F1 list for an instance.\\n\\n    Args:\\n        inst: instance dict with keys gold, samples.\\n        n_samples: if set, only use first n_samples.\\n\\n    Returns:\\n        list of float F1 values.\\n    \\\"\\\"\\\"\\n    gold_ents = inst[\\\"gold\\\"][\\\"entities\\\"]\\n    samples = inst[\\\"samples\\\"][:n_samples] if n_samples else inst[\\\"samples\\\"]\\n    return [compute_entity_f1(s.get(\\\"entities\\\", []), gold_ents) for s in samples]\\n\\n\\ndef compute_greedy_f1(inst):\\n    \\\"\\\"\\\"Compute greedy F1 for an instance.\\\"\\\"\\\"\\n    gold_ents = inst[\\\"gold\\\"][\\\"entities\\\"]\\n    greedy = inst.get(\\\"greedy\\\", inst[\\\"samples\\\"][0])\\n    return compute_entity_f1(greedy.get(\\\"entities\\\", []), gold_ents)\\n\\n\\ndef get_lp_selection_idx(inst, n_samples=None):\\n    \\\"\\\"\\\"Get the index of the sample with highest mean_logprob.\\\"\\\"\\\"\\n    samples = inst[\\\"samples\\\"][:n_samples] if n_samples else inst[\\\"samples\\\"]\\n    best_idx = 0\\n    best_lp = -float(\\\"inf\\\")\\n    for i, s in enumerate(samples):\\n        lp = s.get(\\\"mean_logprob\\\", None)\\n        if lp is None and \\\"logprobs\\\" in inst and i < len(inst[\\\"logprobs\\\"]):\\n            lp = inst[\\\"logprobs\\\"][i]\\n        if lp is not None and np.isfinite(lp) and lp > best_lp:\\n            best_lp = lp\\n            best_idx = i\\n    return best_idx\\n\\n\\ndef bootstrap_ci(values, n_boot=2000, ci=0.95, seed=42):\\n    \\\"\\\"\\\"Bootstrap confidence interval for the mean.\\\"\\\"\\\"\\n    arr = np.array(values)\\n    n = len(arr)\\n    if n == 0:\\n        return {\\\"mean\\\": 0.0, \\\"ci_lo\\\": 0.0, \\\"ci_hi\\\": 0.0}\\n    rng = np.random.RandomState(seed)\\n    boot_means = np.array([arr[rng.randint(0, n, n)].mean() for _ in range(n_boot)])\\n    boot_means.sort()\\n    lo = boot_means[int((1 - ci) / 2 * n_boot)]\\n    hi = boot_means[int((1 + ci) / 2 * n_boot)]\\n    return {\\\"mean\\\": float(arr.mean()), \\\"ci_lo\\\": float(lo), \\\"ci_hi\\\": float(hi)}\\n\\n\\ndef bootstrap_delta_ci(a, b, n_boot=2000, ci=0.95, seed=42):\\n    \\\"\\\"\\\"Bootstrap CI for mean(a) - mean(b), paired.\\\"\\\"\\\"\\n    a_arr, b_arr = np.array(a), np.array(b)\\n    n = len(a_arr)\\n    if n == 0:\\n        return {\\\"delta\\\": 0.0, \\\"ci_lo\\\": 0.0, \\\"ci_hi\\\": 0.0}\\n    rng = np.random.RandomState(seed)\\n    deltas = []\\n    for _ in range(n_boot):\\n        idx = rng.randint(0, n, n)\\n        deltas.append(float(a_arr[idx].mean() - b_arr[idx].mean()))\\n    deltas.sort()\\n    lo = deltas[int((1 - ci) / 2 * n_boot)]\\n    hi = deltas[int((1 + ci) / 2 * n_boot)]\\n    return {\\\"delta\\\": float(a_arr.mean() - b_arr.mean()), \\\"ci_lo\\\": float(lo), \\\"ci_hi\\\": float(hi)}\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.36}}"
    }
  },
  "sourceToolAssistantUUID": "676c397c-2a93-43ee-aad2-21c2ce46422d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "a97de670-f9a7-4d30-affd-382982b8a334",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 69 · 2026-05-19T13:58:05.035Z_

<details><summary>Logged reasoning block</summary>

```text
There's a `d114_auroc_investigation` directory on the server — this looks like someone already investigated the AUROC discrepancy. Let me check that, and also the `unified_tab_fewnerd_maxlp.json` which would have the Table 3 data I need.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "be8a010d-fc93-4c54-8e5d-b6d3e99ff757",
  "isSidechain": false,
  "requestId": "req_011CbC3ayzC2dwRbY65Y3nfi",
  "type": "assistant",
  "uuid": "30ab80ef-9d46-4f84-bba3-f39abd290758",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "a97de670-f9a7-4d30-affd-382982b8a334",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012d4zrbNFVFpS5kUrwS9aTP",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6648,
      "cache_read_input_tokens": 65764,
      "output_tokens": 481,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 6648,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 481,
          "cache_read_input_tokens": 65764,
          "cache_creation_input_tokens": 6648,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 6648
          },
          "type": "message"
        }
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

_source line 70 · 2026-05-19T13:58:05.995Z_

There's a `d114_auroc_investigation` directory — previous investigation. Let me check that along with the FewNERD unified metrics.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "30ab80ef-9d46-4f84-bba3-f39abd290758",
  "isSidechain": false,
  "requestId": "req_011CbC3ayzC2dwRbY65Y3nfi",
  "type": "assistant",
  "uuid": "28851635-41fe-41dd-be69-0bad3b19fd9a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "a97de670-f9a7-4d30-affd-382982b8a334",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012d4zrbNFVFpS5kUrwS9aTP",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6648,
      "cache_read_input_tokens": 65764,
      "output_tokens": 481,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 6648,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 481,
          "cache_read_input_tokens": 65764,
          "cache_creation_input_tokens": 6648,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 6648
          },
          "type": "message"
        }
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

_source line 71 · 2026-05-19T13:58:07.057Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01LJtWogxQdZkmtG9Rcttjyh`</summary>

```json
{
  "server": "autodl-5090",
  "command": "cat /root/autodl-tmp/struct_self_consist_ie/output/d114_auroc_investigation/table1_update.md",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "28851635-41fe-41dd-be69-0bad3b19fd9a",
  "isSidechain": false,
  "requestId": "req_011CbC3ayzC2dwRbY65Y3nfi",
  "type": "assistant",
  "uuid": "fa76f799-dfd8-47fe-855a-5f0c50fef7c2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "a97de670-f9a7-4d30-affd-382982b8a334",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012d4zrbNFVFpS5kUrwS9aTP",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6648,
      "cache_read_input_tokens": 65764,
      "output_tokens": 481,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 6648,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 481,
          "cache_read_input_tokens": 65764,
          "cache_creation_input_tokens": 6648,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 6648
          },
          "type": "message"
        }
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

_source line 72 · 2026-05-19T13:58:07.429Z_

<details><summary>↩ Tool result · `toolu_01LJtWogxQdZkmtG9Rcttjyh`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"# Table 1 Update Assessment\\n\\n## Conclusion: Table 1 does NOT need updating.\\n\\nPaper Table 1 was generated by `analyze_exp015_unified.py` which uses `labels = (y >= median_f1).astype(int)`. This is the correct definition and matches the method section description.\\n\\nAll 15 values (5 signals × 3 datasets) verified to within rounding error (<0.0005):\\n\\n| Signal | SciERC (paper/verified) | CoNLL Qwen (paper/verified) | CoNLL LLaMA (paper/verified) |\\n|--------|------------------------|----------------------------|------------------------------|\\n| VC | .663 / .6627 ✓ | .789 / .7889 ✓ | .709 / .7088 ✓ |\\n| SJ | .650 / .6500 ✓ | .801 / .8008 ✓ | .704 / .7039 ✓ |\\n| FK | .602 / .6019 ✓ | .774 / .7741 ✓ | .703 / .7026 ✓ |\\n| EM | .614 / .6138 ✓ | .816 / .8156 ✓ | .705 / .7046 ✓ |\\n| LP | .578 / .5778 ✓ | .753 / .7532 ✓ | .761 / .7610 ✓ |\\n\\n## What needs updating\\n\\n1. **`evaluation.py:compute_auroc`** — FIXED (changed `>` to `>=`)\\n2. **Multi-seed appendix table** (`\\\\ref{tab:multiseed}`, seeds 42/123/456) — needs regeneration with corrected `compute_auroc`. The corrected values will be ~0.013–0.033 **lower** than currently reported.\\n3. **`analyze_exp012_rerun_5signal.py`** — uses `F1 >= 1.0` threshold which is a *different* metric entirely (predicting perfect extraction, not quality estimation). This script's AUROC is not used in the paper. No action needed unless this script is reused elsewhere.\\n\\n## Note on exp012 script\\n\\nThe `analyze_exp012_rerun_5signal.py` script uses `binary_correct = (f1_arr >= 1.0)` which measures \\\"can the signal predict **perfect** extraction?\\\" This is semantically distinct from the paper's \\\"above/below median\\\" definition. For CoNLL (median F1 = 1.0), the two definitions coincide; for SciERC (median F1 = 0.667), they diverge substantially (EM: .614 vs .749). This script's values should not be cited as \\\"AUROC\\\" without qualification.\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.36}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fa76f799-dfd8-47fe-855a-5f0c50fef7c2",
  "isSidechain": false,
  "promptId": "0731b9be-f5e6-4a8a-9a3c-2edafe06629b",
  "type": "user",
  "uuid": "4403f51f-cd18-44bb-a3fe-8a8a32e520d0",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"# Table 1 Update Assessment\\\\n\\\\n## Conclusion: Table 1 does NOT need updating.\\\\n\\\\nPaper Table 1 was generated by `analyze_exp015_unified.py` which uses `labels = (y >= median_f1).astype(int)`. This is the correct definition and matches the method section description.\\\\n\\\\nAll 15 values (5 signals × 3 datasets) verified to within rounding error (<0.0005):\\\\n\\\\n| Signal | SciERC (paper/verified) | CoNLL Qwen (paper/verified) | CoNLL LLaMA (paper/verified) |\\\\n|--------|------------------------|----------------------------|------------------------------|\\\\n| VC | .663 / .6627 ✓ | .789 / .7889 ✓ | .709 / .7088 ✓ |\\\\n| SJ | .650 / .6500 ✓ | .801 / .8008 ✓ | .704 / .7039 ✓ |\\\\n| FK | .602 / .6019 ✓ | .774 / .7741 ✓ | .703 / .7026 ✓ |\\\\n| EM | .614 / .6138 ✓ | .816 / .8156 ✓ | .705 / .7046 ✓ |\\\\n| LP | .578 / .5778 ✓ | .753 / .7532 ✓ | .761 / .7610 ✓ |\\\\n\\\\n## What needs updating\\\\n\\\\n1. **`evaluation.py:compute_auroc`** — FIXED (changed `>` to `>=`)\\\\n2. **Multi-seed appendix table** (`\\\\\\\\ref{tab:multiseed}`, seeds 42/123/456) — needs regeneration with corrected `compute_auroc`. The corrected values will be ~0.013–0.033 **lower** than currently reported.\\\\n3. **`analyze_exp012_rerun_5signal.py`** — uses `F1 >= 1.0` threshold which is a *different* metric entirely (predicting perfect extraction, not quality estimation). This script's AUROC is not used in the paper. No action needed unless this script is reused elsewhere.\\\\n\\\\n## Note on exp012 script\\\\n\\\\nThe `analyze_exp012_rerun_5signal.py` script uses `binary_correct = (f1_arr >= 1.0)` which measures \\\\\\\"can the signal predict **perfect** extraction?\\\\\\\" This is semantically distinct from the paper's \\\\\\\"above/below median\\\\\\\" definition. For CoNLL (median F1 = 1.0), the two definitions coincide; for SciERC (median F1 = 0.667), they diverge substantially (EM: .614 vs .749). This script's values should not be cited as \\\\\\\"AUROC\\\\\\\" without qualification.\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.36}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"# Table 1 Update Assessment\\n\\n## Conclusion: Table 1 does NOT need updating.\\n\\nPaper Table 1 was generated by `analyze_exp015_unified.py` which uses `labels = (y >= median_f1).astype(int)`. This is the correct definition and matches the method section description.\\n\\nAll 15 values (5 signals × 3 datasets) verified to within rounding error (<0.0005):\\n\\n| Signal | SciERC (paper/verified) | CoNLL Qwen (paper/verified) | CoNLL LLaMA (paper/verified) |\\n|--------|------------------------|----------------------------|------------------------------|\\n| VC | .663 / .6627 ✓ | .789 / .7889 ✓ | .709 / .7088 ✓ |\\n| SJ | .650 / .6500 ✓ | .801 / .8008 ✓ | .704 / .7039 ✓ |\\n| FK | .602 / .6019 ✓ | .774 / .7741 ✓ | .703 / .7026 ✓ |\\n| EM | .614 / .6138 ✓ | .816 / .8156 ✓ | .705 / .7046 ✓ |\\n| LP | .578 / .5778 ✓ | .753 / .7532 ✓ | .761 / .7610 ✓ |\\n\\n## What needs updating\\n\\n1. **`evaluation.py:compute_auroc`** — FIXED (changed `>` to `>=`)\\n2. **Multi-seed appendix table** (`\\\\ref{tab:multiseed}`, seeds 42/123/456) — needs regeneration with corrected `compute_auroc`. The corrected values will be ~0.013–0.033 **lower** than currently reported.\\n3. **`analyze_exp012_rerun_5signal.py`** — uses `F1 >= 1.0` threshold which is a *different* metric entirely (predicting perfect extraction, not quality estimation). This script's AUROC is not used in the paper. No action needed unless this script is reused elsewhere.\\n\\n## Note on exp012 script\\n\\nThe `analyze_exp012_rerun_5signal.py` script uses `binary_correct = (f1_arr >= 1.0)` which measures \\\"can the signal predict **perfect** extraction?\\\" This is semantically distinct from the paper's \\\"above/below median\\\" definition. For CoNLL (median F1 = 1.0), the two definitions coincide; for SciERC (median F1 = 0.667), they diverge substantially (EM: .614 vs .749). This script's values should not be cited as \\\"AUROC\\\" without qualification.\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.36}}"
    }
  },
  "sourceToolAssistantUUID": "fa76f799-dfd8-47fe-855a-5f0c50fef7c2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "a97de670-f9a7-4d30-affd-382982b8a334",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 73 · 2026-05-19T13:58:07.911Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_019XRB7vfMByK2RoSzTBJWUi`</summary>

```json
{
  "server": "autodl-5090",
  "command": "cat /root/autodl-tmp/struct_self_consist_ie/output/d114_auroc_investigation/unified_auroc.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4403f51f-cd18-44bb-a3fe-8a8a32e520d0",
  "isSidechain": false,
  "requestId": "req_011CbC3ayzC2dwRbY65Y3nfi",
  "type": "assistant",
  "uuid": "78df7a04-ea4c-4986-9546-69e4887a2f4c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "a97de670-f9a7-4d30-affd-382982b8a334",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012d4zrbNFVFpS5kUrwS9aTP",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6648,
      "cache_read_input_tokens": 65764,
      "output_tokens": 481,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 6648,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 481,
          "cache_read_input_tokens": 65764,
          "cache_creation_input_tokens": 6648,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 6648
          },
          "type": "message"
        }
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

_source line 74 · 2026-05-19T13:58:08.281Z_

<details><summary>↩ Tool result · `toolu_019XRB7vfMByK2RoSzTBJWUi`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"scierc_ner_seed42\\\": {\\n    \\\"n\\\": 529,\\n    \\\"median_f1\\\": 0.6667,\\n    \\\"auroc\\\": {\\n      \\\"VC\\\": 0.6627,\\n      \\\"SJ\\\": 0.65,\\n      \\\"FK\\\": 0.6019,\\n      \\\"EM\\\": 0.6138,\\n      \\\"LP\\\": 0.5778\\n    },\\n    \\\"rho\\\": {\\n      \\\"VC\\\": 0.3792,\\n      \\\"SJ\\\": 0.3599,\\n      \\\"FK\\\": 0.2665,\\n      \\\"EM\\\": 0.2945,\\n      \\\"LP\\\": 0.2052\\n    }\\n  },\\n  \\\"scierc_ner_seed123\\\": {\\n    \\\"n\\\": 529,\\n    \\\"median_f1\\\": 0.6667,\\n    \\\"auroc\\\": {\\n      \\\"VC\\\": 0.6898,\\n      \\\"SJ\\\": 0.6813,\\n      \\\"FK\\\": 0.6183,\\n      \\\"EM\\\": 0.6439,\\n      \\\"LP\\\": 0.5898\\n    },\\n    \\\"rho\\\": {\\n      \\\"VC\\\": 0.4133,\\n      \\\"SJ\\\": 0.3878,\\n      \\\"FK\\\": 0.2628,\\n      \\\"EM\\\": 0.3135,\\n      \\\"LP\\\": 0.2341\\n    }\\n  },\\n  \\\"scierc_ner_seed789\\\": {\\n    \\\"n\\\": 529,\\n    \\\"median_f1\\\": 0.6667,\\n    \\\"auroc\\\": {\\n      \\\"VC\\\": 0.6938,\\n      \\\"SJ\\\": 0.6599,\\n      \\\"FK\\\": 0.5869,\\n      \\\"EM\\\": 0.627,\\n      \\\"LP\\\": 0.5701\\n    },\\n    \\\"rho\\\": {\\n      \\\"VC\\\": 0.4506,\\n      \\\"SJ\\\": 0.3838,\\n      \\\"FK\\\": 0.2342,\\n      \\\"EM\\\": 0.3036,\\n      \\\"LP\\\": 0.2073\\n    }\\n  },\\n  \\\"scierc_re_seed42\\\": {\\n    \\\"n\\\": 397,\\n    \\\"median_f1\\\": 0.4,\\n    \\\"auroc\\\": {\\n      \\\"VC\\\": 0.6726,\\n      \\\"SJ\\\": 0.6175,\\n      \\\"FK\\\": 0.6402,\\n      \\\"EM\\\": 0.5501,\\n      \\\"LP\\\": 0.6306\\n    },\\n    \\\"rho\\\": {\\n      \\\"VC\\\": 0.3498,\\n      \\\"SJ\\\": 0.2503,\\n      \\\"FK\\\": 0.2752,\\n      \\\"EM\\\": 0.1344,\\n      \\\"LP\\\": 0.2662\\n    }\\n  },\\n  \\\"conll_ner_qwen_n8\\\": {\\n    \\\"n\\\": 2756,\\n    \\\"median_f1\\\": 1.0,\\n    \\\"auroc\\\": {\\n      \\\"VC\\\": 0.7889,\\n      \\\"SJ\\\": 0.8008,\\n      \\\"FK\\\": 0.7741,\\n      \\\"EM\\\": 0.8156,\\n      \\\"LP\\\": 0.7532\\n    },\\n    \\\"rho\\\": {\\n      \\\"VC\\\": 0.4237,\\n      \\\"SJ\\\": 0.4357,\\n      \\\"FK\\\": 0.3998,\\n      \\\"EM\\\": 0.4507,\\n      \\\"LP\\\": 0.3157\\n    }\\n  },\\n  \\\"conll_ner_llama_n8\\\": {\\n    \\\"n\\\": 2756,\\n    \\\"median_f1\\\": 1.0,\\n    \\\"auroc\\\": {\\n      \\\"VC\\\": 0.7088,\\n      \\\"SJ\\\": 0.7039,\\n      \\\"FK\\\": 0.7026,\\n      \\\"EM\\\": 0.7046,\\n      \\\"LP\\\": 0.761\\n    },\\n    \\\"rho\\\": {\\n      \\\"VC\\\": 0.4256,\\n      \\\"SJ\\\": 0.4314,\\n      \\\"FK\\\": 0.4277,\\n      \\\"EM\\\": 0.4306,\\n      \\\"LP\\\": 0.3072\\n    }\\n  },\\n  \\\"scierc_ner_3seed_aggregated\\\": {\\n    \\\"seeds\\\": [\\n      42,\\n      123,\\n      789\\n    ],\\n    \\\"auroc_mean\\\": {\\n      \\\"VC\\\": 0.6821,\\n      \\\"SJ\\\": 0.6637,\\n      \\\"FK\\\": 0.6024,\\n      \\\"EM\\\": 0.6282,\\n      \\\"LP\\\": 0.5792\\n    },\\n    \\\"auroc_std\\\": {\\n      \\\"VC\\\": 0.0169,\\n      \\\"SJ\\\": 0.016,\\n      \\\"FK\\\": 0.0157,\\n      \\\"EM\\\": 0.0151,\\n      \\\"LP\\\": 0.0099\\n    },\\n    \\\"auroc_per_seed\\\": {\\n      \\\"VC\\\": [\\n        0.6627,\\n        0.6898,\\n        0.6938\\n      ],\\n      \\\"SJ\\\": [\\n        0.65,\\n        0.6813,\\n        0.6599\\n      ],\\n      \\\"FK\\\": [\\n        0.6019,\\n        0.6183,\\n        0.5869\\n      ],\\n      \\\"EM\\\": [\\n        0.6138,\\n        0.6439,\\n        0.627\\n      ],\\n      \\\"LP\\\": [\\n        0.5778,\\n        0.5898,\\n        0.5701\\n      ]\\n    }\\n  },\\n  \\\"comparison_old_vs_new\\\": {\\n    \\\"VC\\\": {\\n      \\\"old_method_gt_median\\\": [\\n        0.6879,\\n        0.7089,\\n        0.7223\\n      ],\\n      \\\"new_method_geq_median\\\": [\\n        0.6627,\\n        0.6898,\\n        0.6938\\n      ],\\n      \\\"diffs\\\": [\\n        -0.0252,\\n        -0.0191,\\n        -0.0285\\n      ],\\n      \\\"mean_diff\\\": -0.0243\\n    },\\n    \\\"SJ\\\": {\\n      \\\"old_method_gt_median\\\": [\\n        0.6715,\\n        0.6919,\\n        0.6893\\n      ],\\n      \\\"new_method_geq_median\\\": [\\n        0.65,\\n        0.6813,\\n        0.6599\\n      ],\\n      \\\"diffs\\\": [\\n        -0.0215,\\n        -0.0106,\\n        -0.0294\\n      ],\\n      \\\"mean_diff\\\": -0.0205\\n    },\\n    \\\"FK\\\": {\\n      \\\"old_method_gt_median\\\": [\\n        0.6154,\\n        0.63,\\n        0.602\\n      ],\\n      \\\"new_method_geq_median\\\": [\\n        0.6019,\\n        0.6183,\\n        0.5869\\n      ],\\n      \\\"diffs\\\": [\\n        -0.0135,\\n        -0.0117,\\n        -0.0151\\n      ],\\n      \\\"mean_diff\\\": -0.0134\\n    },\\n    \\\"EM\\\": {\\n      \\\"old_method_gt_median\\\": [\\n        0.6472,\\n        0.6596,\\n        0.6468\\n      ],\\n      \\\"new_method_geq_median\\\": [\\n        0.6138,\\n        0.6439,\\n        0.627\\n      ],\\n      \\\"diffs\\\": [\\n        -0.0334,\\n        -0.0157,\\n        -0.0198\\n      ],\\n      \\\"mean_diff\\\": -0.023\\n    },\\n    \\\"LP\\\": {\\n      \\\"old_method_gt_median\\\": [\\n        0.6116,\\n        0.6132,\\n        0.6124\\n      ],\\n      \\\"new_method_geq_median\\\": [\\n        0.5778,\\n        0.5898,\\n        0.5701\\n      ],\\n      \\\"diffs\\\": [\\n        -0.0338,\\n        -0.0234,\\n        -0.0423\\n      ],\\n      \\\"mean_diff\\\": -0.0332\\n    }\\n  },\\n  \\\"appendix_multiseed_corrected\\\": {\\n    \\\"description\\\": \\\"Corrected AUROC values for appendix Table multiseed (F1 >= median)\\\",\\n    \\\"seeds\\\": [\\n      42,\\n      123,\\n      456\\n    ],\\n    \\\"qwen_ner\\\": {\\n      \\\"per_seed\\\": {\\n        \\\"42\\\": {\\n          \\\"LP\\\": 0.5778,\\n          \\\"FK\\\": 0.6019,\\n          \\\"SJ\\\": 0.65,\\n          \\\"VC\\\": 0.6627,\\n          \\\"EM\\\": 0.6138\\n        },\\n        \\\"123\\\": {\\n          \\\"LP\\\": 0.5898,\\n          \\\"FK\\\": 0.6183,\\n          \\\"SJ\\\": 0.6813,\\n          \\\"VC\\\": 0.6898,\\n          \\\"EM\\\": 0.6439\\n        },\\n        \\\"456\\\": {\\n          \\\"LP\\\": 0.5699,\\n          \\\"FK\\\": 0.5792,\\n          \\\"SJ\\\": 0.646,\\n          \\\"VC\\\": 0.6795,\\n          \\\"EM\\\": 0.6349\\n        }\\n      },\\n      \\\"mean_std\\\": {\\n        \\\"LP\\\": {\\n          \\\"mean\\\": 0.579,\\n          \\\"std\\\": 0.008\\n        },\\n        \\\"FK\\\": {\\n          \\\"mean\\\": 0.6,\\n          \\\"std\\\": 0.016\\n        },\\n        \\\"SJ\\\": {\\n          \\\"mean\\\": 0.659,\\n          \\\"std\\\": 0.016\\n        },\\n        \\\"VC\\\": {\\n          \\\"mean\\\": 0.677,\\n          \\\"std\\\": 0.011\\n        },\\n        \\\"EM\\\": {\\n          \\\"mean\\\": 0.631,\\n          \\\"std\\\": 0.013\\n        }\\n      }\\n    },\\n    \\\"llama_ner\\\": {\\n      \\\"per_seed\\\": {\\n        \\\"42\\\": {\\n          \\\"LP\\\": 0.5695,\\n          \\\"FK\\\": 0.5976,\\n          \\\"SJ\\\": 0.6401,\\n          \\\"VC\\\": 0.6843,\\n          \\\"EM\\\": 0.6138\\n        },\\n        \\\"123\\\": {\\n          \\\"LP\\\": 0.5722,\\n          \\\"FK\\\": 0.5974,\\n          \\\"SJ\\\": 0.6399,\\n          \\\"VC\\\": 0.6715,\\n          \\\"EM\\\": 0.6027\\n        },\\n        \\\"456\\\": {\\n          \\\"LP\\\": 0.5544,\\n          \\\"FK\\\": 0.585,\\n          \\\"SJ\\\": 0.6154,\\n          \\\"VC\\\": 0.6622,\\n          \\\"EM\\\": 0.6017\\n        }\\n      },\\n      \\\"mean_std\\\": {\\n        \\\"LP\\\": {\\n          \\\"mean\\\": 0.565,\\n          \\\"std\\\": 0.008\\n        },\\n        \\\"FK\\\": {\\n          \\\"mean\\\": 0.593,\\n          \\\"std\\\": 0.006\\n        },\\n        \\\"SJ\\\": {\\n          \\\"mean\\\": 0.632,\\n          \\\"std\\\": 0.012\\n        },\\n        \\\"VC\\\": {\\n          \\\"mean\\\": 0.673,\\n          \\\"std\\\": 0.009\\n        },\\n        \\\"EM\\\": {\\n          \\\"mean\\\": 0.606,\\n          \\\"std\\\": 0.005\\n        }\\n      }\\n    }\\n  }\\n}\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.36}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "78df7a04-ea4c-4986-9546-69e4887a2f4c",
  "isSidechain": false,
  "promptId": "0731b9be-f5e6-4a8a-9a3c-2edafe06629b",
  "type": "user",
  "uuid": "a0b94540-4f5c-4550-ad39-be52e25dc05e",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"{\\\\n  \\\\\\\"scierc_ner_seed42\\\\\\\": {\\\\n    \\\\\\\"n\\\\\\\": 529,\\\\n    \\\\\\\"median_f1\\\\\\\": 0.6667,\\\\n    \\\\\\\"auroc\\\\\\\": {\\\\n      \\\\\\\"VC\\\\\\\": 0.6627,\\\\n      \\\\\\\"SJ\\\\\\\": 0.65,\\\\n      \\\\\\\"FK\\\\\\\": 0.6019,\\\\n      \\\\\\\"EM\\\\\\\": 0.6138,\\\\n      \\\\\\\"LP\\\\\\\": 0.5778\\\\n    },\\\\n    \\\\\\\"rho\\\\\\\": {\\\\n      \\\\\\\"VC\\\\\\\": 0.3792,\\\\n      \\\\\\\"SJ\\\\\\\": 0.3599,\\\\n      \\\\\\\"FK\\\\\\\": 0.2665,\\\\n      \\\\\\\"EM\\\\\\\": 0.2945,\\\\n      \\\\\\\"LP\\\\\\\": 0.2052\\\\n    }\\\\n  },\\\\n  \\\\\\\"scierc_ner_seed123\\\\\\\": {\\\\n    \\\\\\\"n\\\\\\\": 529,\\\\n    \\\\\\\"median_f1\\\\\\\": 0.6667,\\\\n    \\\\\\\"auroc\\\\\\\": {\\\\n      \\\\\\\"VC\\\\\\\": 0.6898,\\\\n      \\\\\\\"SJ\\\\\\\": 0.6813,\\\\n      \\\\\\\"FK\\\\\\\": 0.6183,\\\\n      \\\\\\\"EM\\\\\\\": 0.6439,\\\\n      \\\\\\\"LP\\\\\\\": 0.5898\\\\n    },\\\\n    \\\\\\\"rho\\\\\\\": {\\\\n      \\\\\\\"VC\\\\\\\": 0.4133,\\\\n      \\\\\\\"SJ\\\\\\\": 0.3878,\\\\n      \\\\\\\"FK\\\\\\\": 0.2628,\\\\n      \\\\\\\"EM\\\\\\\": 0.3135,\\\\n      \\\\\\\"LP\\\\\\\": 0.2341\\\\n    }\\\\n  },\\\\n  \\\\\\\"scierc_ner_seed789\\\\\\\": {\\\\n    \\\\\\\"n\\\\\\\": 529,\\\\n    \\\\\\\"median_f1\\\\\\\": 0.6667,\\\\n    \\\\\\\"auroc\\\\\\\": {\\\\n      \\\\\\\"VC\\\\\\\": 0.6938,\\\\n      \\\\\\\"SJ\\\\\\\": 0.6599,\\\\n      \\\\\\\"FK\\\\\\\": 0.5869,\\\\n      \\\\\\\"EM\\\\\\\": 0.627,\\\\n      \\\\\\\"LP\\\\\\\": 0.5701\\\\n    },\\\\n    \\\\\\\"rho\\\\\\\": {\\\\n      \\\\\\\"VC\\\\\\\": 0.4506,\\\\n      \\\\\\\"SJ\\\\\\\": 0.3838,\\\\n      \\\\\\\"FK\\\\\\\": 0.2342,\\\\n      \\\\\\\"EM\\\\\\\": 0.3036,\\\\n      \\\\\\\"LP\\\\\\\": 0.2073\\\\n    }\\\\n  },\\\\n  \\\\\\\"scierc_re_seed42\\\\\\\": {\\\\n    \\\\\\\"n\\\\\\\": 397,\\\\n    \\\\\\\"median_f1\\\\\\\": 0.4,\\\\n    \\\\\\\"auroc\\\\\\\": {\\\\n      \\\\\\\"VC\\\\\\\": 0.6726,\\\\n      \\\\\\\"SJ\\\\\\\": 0.6175,\\\\n      \\\\\\\"FK\\\\\\\": 0.6402,\\\\n      \\\\\\\"EM\\\\\\\": 0.5501,\\\\n      \\\\\\\"LP\\\\\\\": 0.6306\\\\n    },\\\\n    \\\\\\\"rho\\\\\\\": {\\\\n      \\\\\\\"VC\\\\\\\": 0.3498,\\\\n      \\\\\\\"SJ\\\\\\\": 0.2503,\\\\n      \\\\\\\"FK\\\\\\\": 0.2752,\\\\n      \\\\\\\"EM\\\\\\\": 0.1344,\\\\n      \\\\\\\"LP\\\\\\\": 0.2662\\\\n    }\\\\n  },\\\\n  \\\\\\\"conll_ner_qwen_n8\\\\\\\": {\\\\n    \\\\\\\"n\\\\\\\": 2756,\\\\n    \\\\\\\"median_f1\\\\\\\": 1.0,\\\\n    \\\\\\\"auroc\\\\\\\": {\\\\n      \\\\\\\"VC\\\\\\\": 0.7889,\\\\n      \\\\\\\"SJ\\\\\\\": 0.8008,\\\\n      \\\\\\\"FK\\\\\\\": 0.7741,\\\\n      \\\\\\\"EM\\\\\\\": 0.8156,\\\\n      \\\\\\\"LP\\\\\\\": 0.7532\\\\n    },\\\\n    \\\\\\\"rho\\\\\\\": {\\\\n      \\\\\\\"VC\\\\\\\": 0.4237,\\\\n      \\\\\\\"SJ\\\\\\\": 0.4357,\\\\n      \\\\\\\"FK\\\\\\\": 0.3998,\\\\n      \\\\\\\"EM\\\\\\\": 0.4507,\\\\n      \\\\\\\"LP\\\\\\\": 0.3157\\\\n    }\\\\n  },\\\\n  \\\\\\\"conll_ner_llama_n8\\\\\\\": {\\\\n    \\\\\\\"n\\\\\\\": 2756,\\\\n    \\\\\\\"median_f1\\\\\\\": 1.0,\\\\n    \\\\\\\"auroc\\\\\\\": {\\\\n      \\\\\\\"VC\\\\\\\": 0.7088,\\\\n      \\\\\\\"SJ\\\\\\\": 0.7039,\\\\n      \\\\\\\"FK\\\\\\\": 0.7026,\\\\n      \\\\\\\"EM\\\\\\\": 0.7046,\\\\n      \\\\\\\"LP\\\\\\\": 0.761\\\\n    },\\\\n    \\\\\\\"rho\\\\\\\": {\\\\n      \\\\\\\"VC\\\\\\\": 0.4256,\\\\n      \\\\\\\"SJ\\\\\\\": 0.4314,\\\\n      \\\\\\\"FK\\\\\\\": 0.4277,\\\\n      \\\\\\\"EM\\\\\\\": 0.4306,\\\\n      \\\\\\\"LP\\\\\\\": 0.3072\\\\n    }\\\\n  },\\\\n  \\\\\\\"scierc_ner_3seed_aggregated\\\\\\\": {\\\\n    \\\\\\\"seeds\\\\\\\": [\\\\n      42,\\\\n      123,\\\\n      789\\\\n    ],\\\\n    \\\\\\\"auroc_mean\\\\\\\": {\\\\n      \\\\\\\"VC\\\\\\\": 0.6821,\\\\n      \\\\\\\"SJ\\\\\\\": 0.6637,\\\\n      \\\\\\\"FK\\\\\\\": 0.6024,\\\\n      \\\\\\\"EM\\\\\\\": 0.6282,\\\\n      \\\\\\\"LP\\\\\\\": 0.5792\\\\n    },\\\\n    \\\\\\\"auroc_std\\\\\\\": {\\\\n      \\\\\\\"VC\\\\\\\": 0.0169,\\\\n      \\\\\\\"SJ\\\\\\\": 0.016,\\\\n      \\\\\\\"FK\\\\\\\": 0.0157,\\\\n      \\\\\\\"EM\\\\\\\": 0.0151,\\\\n      \\\\\\\"LP\\\\\\\": 0.0099\\\\n    },\\\\n    \\\\\\\"auroc_per_seed\\\\\\\": {\\\\n      \\\\\\\"VC\\\\\\\": [\\\\n        0.6627,\\\\n        0.6898,\\\\n        0.6938\\\\n      ],\\\\n      \\\\\\\"SJ\\\\\\\": [\\\\n        0.65,\\\\n        0.6813,\\\\n        0.6599\\\\n      ],\\\\n      \\\\\\\"FK\\\\\\\": [\\\\n        0.6019,\\\\n        0.6183,\\\\n        0.5869\\\\n      ],\\\\n      \\\\\\\"EM\\\\\\\": [\\\\n        0.6138,\\\\n        0.6439,\\\\n        0.627\\\\n      ],\\\\n      \\\\\\\"LP\\\\\\\": [\\\\n        0.5778,\\\\n        0.5898,\\\\n        0.5701\\\\n      ]\\\\n    }\\\\n  },\\\\n  \\\\\\\"comparison_old_vs_new\\\\\\\": {\\\\n    \\\\\\\"VC\\\\\\\": {\\\\n      \\\\\\\"old_method_gt_median\\\\\\\": [\\\\n        0.6879,\\\\n        0.7089,\\\\n        0.7223\\\\n      ],\\\\n      \\\\\\\"new_method_geq_median\\\\\\\": [\\\\n        0.6627,\\\\n        0.6898,\\\\n        0.6938\\\\n      ],\\\\n      \\\\\\\"diffs\\\\\\\": [\\\\n        -0.0252,\\\\n        -0.0191,\\\\n        -0.0285\\\\n      ],\\\\n      \\\\\\\"mean_diff\\\\\\\": -0.0243\\\\n    },\\\\n    \\\\\\\"SJ\\\\\\\": {\\\\n      \\\\\\\"old_method_gt_median\\\\\\\": [\\\\n        0.6715,\\\\n        0.6919,\\\\n        0.6893\\\\n      ],\\\\n      \\\\\\\"new_method_geq_median\\\\\\\": [\\\\n        0.65,\\\\n        0.6813,\\\\n        0.6599\\\\n      ],\\\\n      \\\\\\\"diffs\\\\\\\": [\\\\n        -0.0215,\\\\n        -0.0106,\\\\n        -0.0294\\\\n      ],\\\\n      \\\\\\\"mean_diff\\\\\\\": -0.0205\\\\n    },\\\\n    \\\\\\\"FK\\\\\\\": {\\\\n      \\\\\\\"old_method_gt_median\\\\\\\": [\\\\n        0.6154,\\\\n        0.63,\\\\n        0.602\\\\n      ],\\\\n      \\\\\\\"new_method_geq_median\\\\\\\": [\\\\n        0.6019,\\\\n        0.6183,\\\\n        0.5869\\\\n      ],\\\\n      \\\\\\\"diffs\\\\\\\": [\\\\n        -0.0135,\\\\n        -0.0117,\\\\n        -0.0151\\\\n      ],\\\\n      \\\\\\\"mean_diff\\\\\\\": -0.0134\\\\n    },\\\\n    \\\\\\\"EM\\\\\\\": {\\\\n      \\\\\\\"old_method_gt_median\\\\\\\": [\\\\n        0.6472,\\\\n        0.6596,\\\\n        0.6468\\\\n      ],\\\\n      \\\\\\\"new_method_geq_median\\\\\\\": [\\\\n        0.6138,\\\\n        0.6439,\\\\n        0.627\\\\n      ],\\\\n      \\\\\\\"diffs\\\\\\\": [\\\\n        -0.0334,\\\\n        -0.0157,\\\\n        -0.0198\\\\n      ],\\\\n      \\\\\\\"mean_diff\\\\\\\": -0.023\\\\n    },\\\\n    \\\\\\\"LP\\\\\\\": {\\\\n      \\\\\\\"old_method_gt_median\\\\\\\": [\\\\n        0.6116,\\\\n        0.6132,\\\\n        0.6124\\\\n      ],\\\\n      \\\\\\\"new_method_geq_median\\\\\\\": [\\\\n        0.5778,\\\\n        0.5898,\\\\n        0.5701\\\\n      ],\\\\n      \\\\\\\"diffs\\\\\\\": [\\\\n        -0.0338,\\\\n        -0.0234,\\\\n        -0.0423\\\\n      ],\\\\n      \\\\\\\"mean_diff\\\\\\\": -0.0332\\\\n    }\\\\n  },\\\\n  \\\\\\\"appendix_multiseed_corrected\\\\\\\": {\\\\n    \\\\\\\"description\\\\\\\": \\\\\\\"Corrected AUROC values for appendix Table multiseed (F1 >= median)\\\\\\\",\\\\n    \\\\\\\"seeds\\\\\\\": [\\\\n      42,\\\\n      123,\\\\n      456\\\\n    ],\\\\n    \\\\\\\"qwen_ner\\\\\\\": {\\\\n      \\\\\\\"per_seed\\\\\\\": {\\\\n        \\\\\\\"42\\\\\\\": {\\\\n          \\\\\\\"LP\\\\\\\": 0.5778,\\\\n          \\\\\\\"FK\\\\\\\": 0.6019,\\\\n          \\\\\\\"SJ\\\\\\\": 0.65,\\\\n          \\\\\\\"VC\\\\\\\": 0.6627,\\\\n          \\\\\\\"EM\\\\\\\": 0.6138\\\\n        },\\\\n        \\\\\\\"123\\\\\\\": {\\\\n          \\\\\\\"LP\\\\\\\": 0.5898,\\\\n          \\\\\\\"FK\\\\\\\": 0.6183,\\\\n          \\\\\\\"SJ\\\\\\\": 0.6813,\\\\n          \\\\\\\"VC\\\\\\\": 0.6898,\\\\n          \\\\\\\"EM\\\\\\\": 0.6439\\\\n        },\\\\n        \\\\\\\"456\\\\\\\": {\\\\n          \\\\\\\"LP\\\\\\\": 0.5699,\\\\n          \\\\\\\"FK\\\\\\\": 0.5792,\\\\n          \\\\\\\"SJ\\\\\\\": 0.646,\\\\n          \\\\\\\"VC\\\\\\\": 0.6795,\\\\n          \\\\\\\"EM\\\\\\\": 0.6349\\\\n        }\\\\n      },\\\\n      \\\\\\\"mean_std\\\\\\\": {\\\\n        \\\\\\\"LP\\\\\\\": {\\\\n          \\\\\\\"mean\\\\\\\": 0.579,\\\\n          \\\\\\\"std\\\\\\\": 0.008\\\\n        },\\\\n        \\\\\\\"FK\\\\\\\": {\\\\n          \\\\\\\"mean\\\\\\\": 0.6,\\\\n          \\\\\\\"std\\\\\\\": 0.016\\\\n        },\\\\n        \\\\\\\"SJ\\\\\\\": {\\\\n          \\\\\\\"mean\\\\\\\": 0.659,\\\\n          \\\\\\\"std\\\\\\\": 0.016\\\\n        },\\\\n        \\\\\\\"VC\\\\\\\": {\\\\n          \\\\\\\"mean\\\\\\\": 0.677,\\\\n          \\\\\\\"std\\\\\\\": 0.011\\\\n        },\\\\n        \\\\\\\"EM\\\\\\\": {\\\\n          \\\\\\\"mean\\\\\\\": 0.631,\\\\n          \\\\\\\"std\\\\\\\": 0.013\\\\n        }\\\\n      }\\\\n    },\\\\n    \\\\\\\"llama_ner\\\\\\\": {\\\\n      \\\\\\\"per_seed\\\\\\\": {\\\\n        \\\\\\\"42\\\\\\\": {\\\\n          \\\\\\\"LP\\\\\\\": 0.5695,\\\\n          \\\\\\\"FK\\\\\\\": 0.5976,\\\\n          \\\\\\\"SJ\\\\\\\": 0.6401,\\\\n          \\\\\\\"VC\\\\\\\": 0.6843,\\\\n          \\\\\\\"EM\\\\\\\": 0.6138\\\\n        },\\\\n        \\\\\\\"123\\\\\\\": {\\\\n          \\\\\\\"LP\\\\\\\": 0.5722,\\\\n          \\\\\\\"FK\\\\\\\": 0.5974,\\\\n          \\\\\\\"SJ\\\\\\\": 0.6399,\\\\n          \\\\\\\"VC\\\\\\\": 0.6715,\\\\n          \\\\\\\"EM\\\\\\\": 0.6027\\\\n        },\\\\n        \\\\\\\"456\\\\\\\": {\\\\n          \\\\\\\"LP\\\\\\\": 0.5544,\\\\n          \\\\\\\"FK\\\\\\\": 0.585,\\\\n          \\\\\\\"SJ\\\\\\\": 0.6154,\\\\n          \\\\\\\"VC\\\\\\\": 0.6622,\\\\n          \\\\\\\"EM\\\\\\\": 0.6017\\\\n        }\\\\n      },\\\\n      \\\\\\\"mean_std\\\\\\\": {\\\\n        \\\\\\\"LP\\\\\\\": {\\\\n          \\\\\\\"mean\\\\\\\": 0.565,\\\\n          \\\\\\\"std\\\\\\\": 0.008\\\\n        },\\\\n        \\\\\\\"FK\\\\\\\": {\\\\n          \\\\\\\"mean\\\\\\\": 0.593,\\\\n          \\\\\\\"std\\\\\\\": 0.006\\\\n        },\\\\n        \\\\\\\"SJ\\\\\\\": {\\\\n          \\\\\\\"mean\\\\\\\": 0.632,\\\\n          \\\\\\\"std\\\\\\\": 0.012\\\\n        },\\\\n        \\\\\\\"VC\\\\\\\": {\\\\n          \\\\\\\"mean\\\\\\\": 0.673,\\\\n          \\\\\\\"std\\\\\\\": 0.009\\\\n        },\\\\n        \\\\\\\"EM\\\\\\\": {\\\\n          \\\\\\\"mean\\\\\\\": 0.606,\\\\n          \\\\\\\"std\\\\\\\": 0.005\\\\n        }\\\\n      }\\\\n    }\\\\n  }\\\\n}\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.36}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"scierc_ner_seed42\\\": {\\n    \\\"n\\\": 529,\\n    \\\"median_f1\\\": 0.6667,\\n    \\\"auroc\\\": {\\n      \\\"VC\\\": 0.6627,\\n      \\\"SJ\\\": 0.65,\\n      \\\"FK\\\": 0.6019,\\n      \\\"EM\\\": 0.6138,\\n      \\\"LP\\\": 0.5778\\n    },\\n    \\\"rho\\\": {\\n      \\\"VC\\\": 0.3792,\\n      \\\"SJ\\\": 0.3599,\\n      \\\"FK\\\": 0.2665,\\n      \\\"EM\\\": 0.2945,\\n      \\\"LP\\\": 0.2052\\n    }\\n  },\\n  \\\"scierc_ner_seed123\\\": {\\n    \\\"n\\\": 529,\\n    \\\"median_f1\\\": 0.6667,\\n    \\\"auroc\\\": {\\n      \\\"VC\\\": 0.6898,\\n      \\\"SJ\\\": 0.6813,\\n      \\\"FK\\\": 0.6183,\\n      \\\"EM\\\": 0.6439,\\n      \\\"LP\\\": 0.5898\\n    },\\n    \\\"rho\\\": {\\n      \\\"VC\\\": 0.4133,\\n      \\\"SJ\\\": 0.3878,\\n      \\\"FK\\\": 0.2628,\\n      \\\"EM\\\": 0.3135,\\n      \\\"LP\\\": 0.2341\\n    }\\n  },\\n  \\\"scierc_ner_seed789\\\": {\\n    \\\"n\\\": 529,\\n    \\\"median_f1\\\": 0.6667,\\n    \\\"auroc\\\": {\\n      \\\"VC\\\": 0.6938,\\n      \\\"SJ\\\": 0.6599,\\n      \\\"FK\\\": 0.5869,\\n      \\\"EM\\\": 0.627,\\n      \\\"LP\\\": 0.5701\\n    },\\n    \\\"rho\\\": {\\n      \\\"VC\\\": 0.4506,\\n      \\\"SJ\\\": 0.3838,\\n      \\\"FK\\\": 0.2342,\\n      \\\"EM\\\": 0.3036,\\n      \\\"LP\\\": 0.2073\\n    }\\n  },\\n  \\\"scierc_re_seed42\\\": {\\n    \\\"n\\\": 397,\\n    \\\"median_f1\\\": 0.4,\\n    \\\"auroc\\\": {\\n      \\\"VC\\\": 0.6726,\\n      \\\"SJ\\\": 0.6175,\\n      \\\"FK\\\": 0.6402,\\n      \\\"EM\\\": 0.5501,\\n      \\\"LP\\\": 0.6306\\n    },\\n    \\\"rho\\\": {\\n      \\\"VC\\\": 0.3498,\\n      \\\"SJ\\\": 0.2503,\\n      \\\"FK\\\": 0.2752,\\n      \\\"EM\\\": 0.1344,\\n      \\\"LP\\\": 0.2662\\n    }\\n  },\\n  \\\"conll_ner_qwen_n8\\\": {\\n    \\\"n\\\": 2756,\\n    \\\"median_f1\\\": 1.0,\\n    \\\"auroc\\\": {\\n      \\\"VC\\\": 0.7889,\\n      \\\"SJ\\\": 0.8008,\\n      \\\"FK\\\": 0.7741,\\n      \\\"EM\\\": 0.8156,\\n      \\\"LP\\\": 0.7532\\n    },\\n    \\\"rho\\\": {\\n      \\\"VC\\\": 0.4237,\\n      \\\"SJ\\\": 0.4357,\\n      \\\"FK\\\": 0.3998,\\n      \\\"EM\\\": 0.4507,\\n      \\\"LP\\\": 0.3157\\n    }\\n  },\\n  \\\"conll_ner_llama_n8\\\": {\\n    \\\"n\\\": 2756,\\n    \\\"median_f1\\\": 1.0,\\n    \\\"auroc\\\": {\\n      \\\"VC\\\": 0.7088,\\n      \\\"SJ\\\": 0.7039,\\n      \\\"FK\\\": 0.7026,\\n      \\\"EM\\\": 0.7046,\\n      \\\"LP\\\": 0.761\\n    },\\n    \\\"rho\\\": {\\n      \\\"VC\\\": 0.4256,\\n      \\\"SJ\\\": 0.4314,\\n      \\\"FK\\\": 0.4277,\\n      \\\"EM\\\": 0.4306,\\n      \\\"LP\\\": 0.3072\\n    }\\n  },\\n  \\\"scierc_ner_3seed_aggregated\\\": {\\n    \\\"seeds\\\": [\\n      42,\\n      123,\\n      789\\n    ],\\n    \\\"auroc_mean\\\": {\\n      \\\"VC\\\": 0.6821,\\n      \\\"SJ\\\": 0.6637,\\n      \\\"FK\\\": 0.6024,\\n      \\\"EM\\\": 0.6282,\\n      \\\"LP\\\": 0.5792\\n    },\\n    \\\"auroc_std\\\": {\\n      \\\"VC\\\": 0.0169,\\n      \\\"SJ\\\": 0.016,\\n      \\\"FK\\\": 0.0157,\\n      \\\"EM\\\": 0.0151,\\n      \\\"LP\\\": 0.0099\\n    },\\n    \\\"auroc_per_seed\\\": {\\n      \\\"VC\\\": [\\n        0.6627,\\n        0.6898,\\n        0.6938\\n      ],\\n      \\\"SJ\\\": [\\n        0.65,\\n        0.6813,\\n        0.6599\\n      ],\\n      \\\"FK\\\": [\\n        0.6019,\\n        0.6183,\\n        0.5869\\n      ],\\n      \\\"EM\\\": [\\n        0.6138,\\n        0.6439,\\n        0.627\\n      ],\\n      \\\"LP\\\": [\\n        0.5778,\\n        0.5898,\\n        0.5701\\n      ]\\n    }\\n  },\\n  \\\"comparison_old_vs_new\\\": {\\n    \\\"VC\\\": {\\n      \\\"old_method_gt_median\\\": [\\n        0.6879,\\n        0.7089,\\n        0.7223\\n      ],\\n      \\\"new_method_geq_median\\\": [\\n        0.6627,\\n        0.6898,\\n        0.6938\\n      ],\\n      \\\"diffs\\\": [\\n        -0.0252,\\n        -0.0191,\\n        -0.0285\\n      ],\\n      \\\"mean_diff\\\": -0.0243\\n    },\\n    \\\"SJ\\\": {\\n      \\\"old_method_gt_median\\\": [\\n        0.6715,\\n        0.6919,\\n        0.6893\\n      ],\\n      \\\"new_method_geq_median\\\": [\\n        0.65,\\n        0.6813,\\n        0.6599\\n      ],\\n      \\\"diffs\\\": [\\n        -0.0215,\\n        -0.0106,\\n        -0.0294\\n      ],\\n      \\\"mean_diff\\\": -0.0205\\n    },\\n    \\\"FK\\\": {\\n      \\\"old_method_gt_median\\\": [\\n        0.6154,\\n        0.63,\\n        0.602\\n      ],\\n      \\\"new_method_geq_median\\\": [\\n        0.6019,\\n        0.6183,\\n        0.5869\\n      ],\\n      \\\"diffs\\\": [\\n        -0.0135,\\n        -0.0117,\\n        -0.0151\\n      ],\\n      \\\"mean_diff\\\": -0.0134\\n    },\\n    \\\"EM\\\": {\\n      \\\"old_method_gt_median\\\": [\\n        0.6472,\\n        0.6596,\\n        0.6468\\n      ],\\n      \\\"new_method_geq_median\\\": [\\n        0.6138,\\n        0.6439,\\n        0.627\\n      ],\\n      \\\"diffs\\\": [\\n        -0.0334,\\n        -0.0157,\\n        -0.0198\\n      ],\\n      \\\"mean_diff\\\": -0.023\\n    },\\n    \\\"LP\\\": {\\n      \\\"old_method_gt_median\\\": [\\n        0.6116,\\n        0.6132,\\n        0.6124\\n      ],\\n      \\\"new_method_geq_median\\\": [\\n        0.5778,\\n        0.5898,\\n        0.5701\\n      ],\\n      \\\"diffs\\\": [\\n        -0.0338,\\n        -0.0234,\\n        -0.0423\\n      ],\\n      \\\"mean_diff\\\": -0.0332\\n    }\\n  },\\n  \\\"appendix_multiseed_corrected\\\": {\\n    \\\"description\\\": \\\"Corrected AUROC values for appendix Table multiseed (F1 >= median)\\\",\\n    \\\"seeds\\\": [\\n      42,\\n      123,\\n      456\\n    ],\\n    \\\"qwen_ner\\\": {\\n      \\\"per_seed\\\": {\\n        \\\"42\\\": {\\n          \\\"LP\\\": 0.5778,\\n          \\\"FK\\\": 0.6019,\\n          \\\"SJ\\\": 0.65,\\n          \\\"VC\\\": 0.6627,\\n          \\\"EM\\\": 0.6138\\n        },\\n        \\\"123\\\": {\\n          \\\"LP\\\": 0.5898,\\n          \\\"FK\\\": 0.6183,\\n          \\\"SJ\\\": 0.6813,\\n          \\\"VC\\\": 0.6898,\\n          \\\"EM\\\": 0.6439\\n        },\\n        \\\"456\\\": {\\n          \\\"LP\\\": 0.5699,\\n          \\\"FK\\\": 0.5792,\\n          \\\"SJ\\\": 0.646,\\n          \\\"VC\\\": 0.6795,\\n          \\\"EM\\\": 0.6349\\n        }\\n      },\\n      \\\"mean_std\\\": {\\n        \\\"LP\\\": {\\n          \\\"mean\\\": 0.579,\\n          \\\"std\\\": 0.008\\n        },\\n        \\\"FK\\\": {\\n          \\\"mean\\\": 0.6,\\n          \\\"std\\\": 0.016\\n        },\\n        \\\"SJ\\\": {\\n          \\\"mean\\\": 0.659,\\n          \\\"std\\\": 0.016\\n        },\\n        \\\"VC\\\": {\\n          \\\"mean\\\": 0.677,\\n          \\\"std\\\": 0.011\\n        },\\n        \\\"EM\\\": {\\n          \\\"mean\\\": 0.631,\\n          \\\"std\\\": 0.013\\n        }\\n      }\\n    },\\n    \\\"llama_ner\\\": {\\n      \\\"per_seed\\\": {\\n        \\\"42\\\": {\\n          \\\"LP\\\": 0.5695,\\n          \\\"FK\\\": 0.5976,\\n          \\\"SJ\\\": 0.6401,\\n          \\\"VC\\\": 0.6843,\\n          \\\"EM\\\": 0.6138\\n        },\\n        \\\"123\\\": {\\n          \\\"LP\\\": 0.5722,\\n          \\\"FK\\\": 0.5974,\\n          \\\"SJ\\\": 0.6399,\\n          \\\"VC\\\": 0.6715,\\n          \\\"EM\\\": 0.6027\\n        },\\n        \\\"456\\\": {\\n          \\\"LP\\\": 0.5544,\\n          \\\"FK\\\": 0.585,\\n          \\\"SJ\\\": 0.6154,\\n          \\\"VC\\\": 0.6622,\\n          \\\"EM\\\": 0.6017\\n        }\\n      },\\n      \\\"mean_std\\\": {\\n        \\\"LP\\\": {\\n          \\\"mean\\\": 0.565,\\n          \\\"std\\\": 0.008\\n        },\\n        \\\"FK\\\": {\\n          \\\"mean\\\": 0.593,\\n          \\\"std\\\": 0.006\\n        },\\n        \\\"SJ\\\": {\\n          \\\"mean\\\": 0.632,\\n          \\\"std\\\": 0.012\\n        },\\n        \\\"VC\\\": {\\n          \\\"mean\\\": 0.673,\\n          \\\"std\\\": 0.009\\n        },\\n        \\\"EM\\\": {\\n          \\\"mean\\\": 0.606,\\n          \\\"std\\\": 0.005\\n        }\\n      }\\n    }\\n  }\\n}\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.36}}"
    }
  },
  "sourceToolAssistantUUID": "78df7a04-ea4c-4986-9546-69e4887a2f4c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "a97de670-f9a7-4d30-affd-382982b8a334",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 75 · 2026-05-19T13:58:08.312Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_016Uxzptyd7VgcZD1ToSimjv`</summary>

```json
{
  "server": "autodl-5090",
  "command": "cat /root/autodl-tmp/struct_self_consist_ie/output/unified_tab_fewnerd_maxlp.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a0b94540-4f5c-4550-ad39-be52e25dc05e",
  "isSidechain": false,
  "requestId": "req_011CbC3ayzC2dwRbY65Y3nfi",
  "type": "assistant",
  "uuid": "ee678a31-b3b7-47a3-81fb-08456820873f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "a97de670-f9a7-4d30-affd-382982b8a334",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012d4zrbNFVFpS5kUrwS9aTP",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6648,
      "cache_read_input_tokens": 65764,
      "output_tokens": 481,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 6648,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 481,
          "cache_read_input_tokens": 65764,
          "cache_creation_input_tokens": 6648,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 6648
          },
          "type": "message"
        }
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

_source line 76_

```json
{
  "type": "last-prompt",
  "leafUuid": "ee678a31-b3b7-47a3-81fb-08456820873f",
  "sessionId": "a97de670-f9a7-4d30-affd-382982b8a334"
}
```

---

### Runtime record

_source line 77_

```json
{
  "type": "ai-title",
  "aiTitle": "Audit data inconsistencies in paper tables",
  "sessionId": "a97de670-f9a7-4d30-affd-382982b8a334"
}
```

---

### Tool result

_source line 78 · 2026-05-19T13:58:08.709Z_

<details><summary>↩ Tool result · `toolu_016Uxzptyd7VgcZD1ToSimjv`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"SciERC\\\": {\\n    \\\"n\\\": 529,\\n    \\\"n_samples\\\": 8,\\n    \\\"greedy_f1\\\": 0.6439219990259687,\\n    \\\"oracle_f1\\\": 0.7758023559647044,\\n    \\\"lp_sel_f1\\\": 0.6500718843902431,\\n    \\\"headroom_pp\\\": 13.188035693873568,\\n    \\\"lp_delta_pp\\\": 0.614988536427441,\\n    \\\"degen_f1_pct\\\": 17.76937618147448,\\n    \\\"lp_rho_max\\\": 0.21488770073659605,\\n    \\\"lp_rho_max_p\\\": 6.065313768450742e-07,\\n    \\\"lp_rho_mean\\\": 0.20517413101613924,\\n    \\\"lp_rho_mean_p\\\": 1.9498006196855416e-06\\n  },\\n  \\\"Few-NERD\\\": {\\n    \\\"n\\\": 32565,\\n    \\\"n_samples\\\": 8,\\n    \\\"greedy_f1\\\": 0.7478465965854552,\\n    \\\"oracle_f1\\\": 0.8718523412957434,\\n    \\\"lp_sel_f1\\\": 0.7613975687723666,\\n    \\\"headroom_pp\\\": 12.400574471028825,\\n    \\\"lp_delta_pp\\\": 1.355097218691148,\\n    \\\"degen_f1_pct\\\": 13.754030400736989,\\n    \\\"lp_rho_max\\\": 0.42151629185166933,\\n    \\\"lp_rho_max_p\\\": 0.0,\\n    \\\"lp_rho_mean\\\": 0.22172877738233274,\\n    \\\"lp_rho_mean_p\\\": 0.0\\n  },\\n  \\\"CoNLL_Qwen_N8\\\": {\\n    \\\"n\\\": 2756,\\n    \\\"n_samples\\\": 8,\\n    \\\"greedy_f1\\\": 0.9078871741063325,\\n    \\\"oracle_f1\\\": 0.948271330346802,\\n    \\\"lp_sel_f1\\\": 0.8974051146077575,\\n    \\\"headroom_pp\\\": 4.038415624046953,\\n    \\\"lp_delta_pp\\\": -1.0482059498574947,\\n    \\\"degen_f1_pct\\\": 59.143686502177076,\\n    \\\"lp_rho_max\\\": 0.3017192331559146,\\n    \\\"lp_rho_max_p\\\": 4.173770842291669e-59,\\n    \\\"lp_rho_mean\\\": 0.3156601023930858,\\n    \\\"lp_rho_mean_p\\\": 8.156803289565863e-65\\n  }\\n}\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.39}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ee678a31-b3b7-47a3-81fb-08456820873f",
  "isSidechain": false,
  "promptId": "0731b9be-f5e6-4a8a-9a3c-2edafe06629b",
  "type": "user",
  "uuid": "233e2f2d-6c31-40dc-80e3-a1ce3dfd3d2b",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"{\\\\n  \\\\\\\"SciERC\\\\\\\": {\\\\n    \\\\\\\"n\\\\\\\": 529,\\\\n    \\\\\\\"n_samples\\\\\\\": 8,\\\\n    \\\\\\\"greedy_f1\\\\\\\": 0.6439219990259687,\\\\n    \\\\\\\"oracle_f1\\\\\\\": 0.7758023559647044,\\\\n    \\\\\\\"lp_sel_f1\\\\\\\": 0.6500718843902431,\\\\n    \\\\\\\"headroom_pp\\\\\\\": 13.188035693873568,\\\\n    \\\\\\\"lp_delta_pp\\\\\\\": 0.614988536427441,\\\\n    \\\\\\\"degen_f1_pct\\\\\\\": 17.76937618147448,\\\\n    \\\\\\\"lp_rho_max\\\\\\\": 0.21488770073659605,\\\\n    \\\\\\\"lp_rho_max_p\\\\\\\": 6.065313768450742e-07,\\\\n    \\\\\\\"lp_rho_mean\\\\\\\": 0.20517413101613924,\\\\n    \\\\\\\"lp_rho_mean_p\\\\\\\": 1.9498006196855416e-06\\\\n  },\\\\n  \\\\\\\"Few-NERD\\\\\\\": {\\\\n    \\\\\\\"n\\\\\\\": 32565,\\\\n    \\\\\\\"n_samples\\\\\\\": 8,\\\\n    \\\\\\\"greedy_f1\\\\\\\": 0.7478465965854552,\\\\n    \\\\\\\"oracle_f1\\\\\\\": 0.8718523412957434,\\\\n    \\\\\\\"lp_sel_f1\\\\\\\": 0.7613975687723666,\\\\n    \\\\\\\"headroom_pp\\\\\\\": 12.400574471028825,\\\\n    \\\\\\\"lp_delta_pp\\\\\\\": 1.355097218691148,\\\\n    \\\\\\\"degen_f1_pct\\\\\\\": 13.754030400736989,\\\\n    \\\\\\\"lp_rho_max\\\\\\\": 0.42151629185166933,\\\\n    \\\\\\\"lp_rho_max_p\\\\\\\": 0.0,\\\\n    \\\\\\\"lp_rho_mean\\\\\\\": 0.22172877738233274,\\\\n    \\\\\\\"lp_rho_mean_p\\\\\\\": 0.0\\\\n  },\\\\n  \\\\\\\"CoNLL_Qwen_N8\\\\\\\": {\\\\n    \\\\\\\"n\\\\\\\": 2756,\\\\n    \\\\\\\"n_samples\\\\\\\": 8,\\\\n    \\\\\\\"greedy_f1\\\\\\\": 0.9078871741063325,\\\\n    \\\\\\\"oracle_f1\\\\\\\": 0.948271330346802,\\\\n    \\\\\\\"lp_sel_f1\\\\\\\": 0.8974051146077575,\\\\n    \\\\\\\"headroom_pp\\\\\\\": 4.038415624046953,\\\\n    \\\\\\\"lp_delta_pp\\\\\\\": -1.0482059498574947,\\\\n    \\\\\\\"degen_f1_pct\\\\\\\": 59.143686502177076,\\\\n    \\\\\\\"lp_rho_max\\\\\\\": 0.3017192331559146,\\\\n    \\\\\\\"lp_rho_max_p\\\\\\\": 4.173770842291669e-59,\\\\n    \\\\\\\"lp_rho_mean\\\\\\\": 0.3156601023930858,\\\\n    \\\\\\\"lp_rho_mean_p\\\\\\\": 8.156803289565863e-65\\\\n  }\\\\n}\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.39}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"SciERC\\\": {\\n    \\\"n\\\": 529,\\n    \\\"n_samples\\\": 8,\\n    \\\"greedy_f1\\\": 0.6439219990259687,\\n    \\\"oracle_f1\\\": 0.7758023559647044,\\n    \\\"lp_sel_f1\\\": 0.6500718843902431,\\n    \\\"headroom_pp\\\": 13.188035693873568,\\n    \\\"lp_delta_pp\\\": 0.614988536427441,\\n    \\\"degen_f1_pct\\\": 17.76937618147448,\\n    \\\"lp_rho_max\\\": 0.21488770073659605,\\n    \\\"lp_rho_max_p\\\": 6.065313768450742e-07,\\n    \\\"lp_rho_mean\\\": 0.20517413101613924,\\n    \\\"lp_rho_mean_p\\\": 1.9498006196855416e-06\\n  },\\n  \\\"Few-NERD\\\": {\\n    \\\"n\\\": 32565,\\n    \\\"n_samples\\\": 8,\\n    \\\"greedy_f1\\\": 0.7478465965854552,\\n    \\\"oracle_f1\\\": 0.8718523412957434,\\n    \\\"lp_sel_f1\\\": 0.7613975687723666,\\n    \\\"headroom_pp\\\": 12.400574471028825,\\n    \\\"lp_delta_pp\\\": 1.355097218691148,\\n    \\\"degen_f1_pct\\\": 13.754030400736989,\\n    \\\"lp_rho_max\\\": 0.42151629185166933,\\n    \\\"lp_rho_max_p\\\": 0.0,\\n    \\\"lp_rho_mean\\\": 0.22172877738233274,\\n    \\\"lp_rho_mean_p\\\": 0.0\\n  },\\n  \\\"CoNLL_Qwen_N8\\\": {\\n    \\\"n\\\": 2756,\\n    \\\"n_samples\\\": 8,\\n    \\\"greedy_f1\\\": 0.9078871741063325,\\n    \\\"oracle_f1\\\": 0.948271330346802,\\n    \\\"lp_sel_f1\\\": 0.8974051146077575,\\n    \\\"headroom_pp\\\": 4.038415624046953,\\n    \\\"lp_delta_pp\\\": -1.0482059498574947,\\n    \\\"degen_f1_pct\\\": 59.143686502177076,\\n    \\\"lp_rho_max\\\": 0.3017192331559146,\\n    \\\"lp_rho_max_p\\\": 4.173770842291669e-59,\\n    \\\"lp_rho_mean\\\": 0.3156601023930858,\\n    \\\"lp_rho_mean_p\\\": 8.156803289565863e-65\\n  }\\n}\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.39}}"
    }
  },
  "sourceToolAssistantUUID": "ee678a31-b3b7-47a3-81fb-08456820873f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "a97de670-f9a7-4d30-affd-382982b8a334",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 79 · 2026-05-19T13:59:32.903Z_

<details><summary>Logged reasoning block</summary>

```text
Excellent! Now I have all the data I need. Let me compile findings for each investigation:

## Investigation 1: SciERC AUROC Table 1 vs registry

**Resolution found!** The `d114_auroc_investigation/table1_update.md` explains everything:

1. Paper Table 1 uses **median-split AUROC** (binary = F1 >= median), computed by `analyze_exp015_unified.py`
2. The registry's `exp_012_rerun_1024` AUROC uses **perfect-extraction AUROC** (binary = F1 >= 1.0), computed by `eval_exp012_rerun_auroc.py`


3. These are fundamentally different metrics, and the paper's approach is the correct one.

I've verified all the paper values against the unified AUROC data—they match within rounding error across all domains: VC, SJ, FK, EM, and LP. For CoNLL where the median F1 equals 1.0, both definitions produce the same result.

Now looking at SciERC with its median F1 of 0.667, the two binarization approaches diverge significantly—that's what explains the large discrepancy for EM (.614 versus .749). So the paper is correct, and the registry values are using a different threshold definition. The real issue is that the registry needs clearer documentation about which AUROC variant it's reporting.

Moving to the next investigation, I'm checking the CoNLL LP selection inconsistency. The data shows that for the single-seed run with seed 42, greedy F1 was 0.9079 while the LP-selected F1 dropped to 0.8974, giving a delta of -1.05 percentage points.

But here's where it gets confusing: Table 3 in the paper reports -0.85pp for CoNLL LP delta, while the appendix cross-selection shows -1.1pp (calculated as .897 - .908). The appendix value is close enough to my computed -1.05pp that it's likely just rounding differences from different precision levels. However, Table 3's -0.85pp doesn't match either of these. If Table 3 is supposed to be averaging across three seeds, I need to find those other seed results in the registry to understand where this discrepancy comes from.

Looking through the registry, I can see exp_002_conll_n16 variants for seeds 123 and 456, but these are N=16 experiments, not N=8 like Table 3 claims. The appendix explicitly states Qwen/CoNLL N=8 with LP F1 = .897 and delta = -1.1pp relative to greedy .908, but when I check the unified_tab data, greedy shows as .9079 instead. I need to figure out which baseline value is actually being used here. I'm noticing Table 3 reports -0.85pp while both the appendix and my direct computation from seed 42 converge on around -1.05 to -1.1pp, so there's a clear discrepancy. I should check whether Table 3 uses a different selection criterion like max_lp instead of mean_lp, which could explain the gap.

Looking at the selection logic across both scripts, they both use argmax on logprobs to pick the sample, so the selection method is consistent. The difference must come from somewhere else in how the metrics are computed or aggregated.

Now I'm trying to trace where the -0.85pp in Table 3 comes from. The appendix might have a comprehensive cross-config table while Table 3 could be reporting a specific 3-seed result, so they might not be directly comparable. I need to check what experiments.tex actually references for Table 3 and whether I have multi-seed CoNLL N=8 data with LP selection in the registry.

My current findings are that the seed 42 computation gives -1.05pp, the appendix shows -1.1pp which aligns with that, but the -0.85pp in Table 3 remains unverified with no matching source I can locate.

For FewNERD, the 13.8% degeneracy value checks out—it's the seed 42 single-seed result from the gold-filtered constant-F1 definition in the inference samples.

But now I'm seeing a discrepancy in the registry data. The unified_tab script computes 13.75% for seed 42, yet the registry's exp_021_fewnerd_full entry shows 10.1% for the same seed. These don't match, and the likely explanation is that the registry entry is using a different n_instances baseline for its calculation.

Looking more closely at the source tags, I notice that exp_021_fewnerd_n8_seed123 explicitly references "unified_metrics_constant_f1_gold_filtered" as its source, but exp_021_fewnerd_full has no source tag at all. This suggests they might be using different degeneracy definitions entirely.

The unified_tab computation for seed 42 gives 13.75% using gold-filtered instances with the constant F1 criterion, which matches the paper's 13.8%. But the registry's 10.1% for the full experiment likely uses a different denominator or definition altogether—possibly counting all outputs as identical rather than just F1 scores, or applying different filtering logic.

The seed-specific experiments (123, 456, 789) show 13.1%, 12.1%, and 11.8% using the unified metrics definition, but seed 42 wasn't run with that same setup initially. When I recalculate the 3-seed mean using the correct unified value for seed 42 (13.75% instead of the old 10.1%), I get (13.75 + 13.12 + 12.12) / 3 = 13.0%, which actually aligns much better with the paper's reported 13.8%.

Wait, but the paper reports 13.8% and claims it's a 3-seed mean in Table 3's caption. If it's truly a 3-seed mean with uniform definitions, it should be around 13.0%, not 13.8%. This suggests the 13.8% might actually be the single-seed value for seed 42 alone, which would be correct, but that creates an inconsistency with what the table caption says it represents.

Now I'm moving on to check the CoNLL degeneracy value of 48.4% — looking at the registry to see what experiments were actually run and whether the degen_rate metric was even computed for those runs.

I'm finding that the 48.4% comes from an N=16 experiment, but the table claims N=8 with 48.4% degeneracy. The actual N=8 degeneracy from the unified table is 59.1%, so the paper appears to have mixed up the results from different experimental configurations. The mismatch continues — Table 3 shows 48.4% degeneracy with a greedy F1 of .908, but the unified data has .9079 greedy with 59.1% degeneracy, and the registry shows .9123 greedy. The n=2,756 sample count matches the N=8 experiments, but these different greedy scores suggest they might be pulling from different data sources or experimental runs.

The 48.4% degeneracy actually aligns with the N=16 data, not N=8, which is telling. I should dig into the actual tex files to pin down the exact values and check whether the -0.85pp LP selection difference comes from multi-seed computations in exp_002.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "233e2f2d-6c31-40dc-80e3-a1ce3dfd3d2b",
  "isSidechain": false,
  "requestId": "req_011CbC3bWqaQwXbUJ4hVS9aL",
  "type": "assistant",
  "uuid": "b3eda6e2-a871-4a7c-92f2-d87dbe0bfec1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "a97de670-f9a7-4d30-affd-382982b8a334",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YR9BTrPw62jwNBevjEuP1A",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6441,
      "cache_read_input_tokens": 72412,
      "output_tokens": 5116,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 6441,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 5116,
          "cache_read_input_tokens": 72412,
          "cache_creation_input_tokens": 6441,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 6441
          },
          "type": "message"
        }
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

_source line 80 · 2026-05-19T13:59:33.962Z_

Investigation 1 is resolved — previous audit confirms paper uses median-split AUROC, registry uses F1>=1.0 AUROC. Different metrics, paper is correct.

Now let me verify the remaining investigations. Need to read the experiments.tex directly and check CoNLL LP selection multi-seed data.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b3eda6e2-a871-4a7c-92f2-d87dbe0bfec1",
  "isSidechain": false,
  "requestId": "req_011CbC3bWqaQwXbUJ4hVS9aL",
  "type": "assistant",
  "uuid": "e2c89cb9-2639-406b-8945-446c2eee74f8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "a97de670-f9a7-4d30-affd-382982b8a334",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YR9BTrPw62jwNBevjEuP1A",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6441,
      "cache_read_input_tokens": 72412,
      "output_tokens": 5116,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 6441,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 5116,
          "cache_read_input_tokens": 72412,
          "cache_creation_input_tokens": 6441,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 6441
          },
          "type": "message"
        }
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

_source line 81 · 2026-05-19T13:59:40.848Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01MieHXuoBqohFJCCDBSLzD5`</summary>

```json
{
  "subagent_type": "Explore",
  "description": "Read experiments.tex Table 3",
  "prompt": "Read the file /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex lines 100-140, focusing on Table 3 (tab:fewnerd). I need:\n1. The exact table caption — does it specify N=8, 3-seed mean, or single seed?\n2. All CoNLL values in the table (n, greedy, degen%, LP ρ, LP Δ, p-value)\n3. All FewNERD values in the table\n4. Any footnotes or annotations about how values were computed\n\nAlso read /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex lines 230-270 for the cross-selection table (tab:cross_selection). I need:\n1. The exact table caption\n2. The Qwen/CoNLL N=8 row — all values including LP F1 and how Δ is computed\n3. Whether the appendix specifies seed or 3-seed mean"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e2c89cb9-2639-406b-8945-446c2eee74f8",
  "isSidechain": false,
  "requestId": "req_011CbC3bWqaQwXbUJ4hVS9aL",
  "type": "assistant",
  "uuid": "f989c8cf-b773-411e-87fc-82f42ffface5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "a97de670-f9a7-4d30-affd-382982b8a334",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YR9BTrPw62jwNBevjEuP1A",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6441,
      "cache_read_input_tokens": 72412,
      "output_tokens": 5116,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 6441,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 5116,
          "cache_read_input_tokens": 72412,
          "cache_creation_input_tokens": 6441,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 6441
          },
          "type": "message"
        }
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

_source line 82 · 2026-05-19T13:59:47.281Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01WsjGxjhKvqHYJwqNS3qmsH`</summary>

```json
{
  "command": "REGFILE=\"/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie/a97de670-f9a7-4d30-affd-382982b8a334/tool-results/mcp-agent-ml-research-read_registry-1779198876363.txt\"\npython3 -c \"\nimport json\ndata = json.loads(json.loads(open('$REGFILE').read())['result'])\nexps = data['data']['experiments']\n\n# Look for any CoNLL LP selection / cross-selection experiments\nfor eid in sorted(exps.keys()):\n    if 'ccs' in eid.lower() or 'cross' in eid.lower() or 'selective' in eid.lower() or 'selection' in eid.lower() or 'cascade' in eid.lower() or 'dals' in eid.lower():\n        exp = exps[eid]\n        m = exp.get('metrics', {})\n        print(f'{eid}: status={exp.get(\\\"status\\\")}, keys={list(m.keys())[:15]}')\n        # Show full metrics if small\n        ms = json.dumps(m, indent=2)\n        if len(ms) < 2000:\n            print(ms)\n        print()\n\"\n",
  "description": "Find CoNLL LP selection cross-dataset experiments"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f989c8cf-b773-411e-87fc-82f42ffface5",
  "isSidechain": false,
  "requestId": "req_011CbC3bWqaQwXbUJ4hVS9aL",
  "type": "assistant",
  "uuid": "19b484fd-a2c4-4096-adf9-62ea813dbbdc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "a97de670-f9a7-4d30-affd-382982b8a334",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YR9BTrPw62jwNBevjEuP1A",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6441,
      "cache_read_input_tokens": 72412,
      "output_tokens": 5116,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 6441,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 5116,
          "cache_read_input_tokens": 72412,
          "cache_creation_input_tokens": 6441,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 6441
          },
          "type": "message"
        }
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

_source line 83 · 2026-05-19T13:59:49.364Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01R3CAhzhuXjdYLURzCwqJiA`</summary>

```json
{
  "server": "autodl-5090",
  "command": "find /root/autodl-tmp/struct_self_consist_ie/output -name \"*dals*\" -o -name \"*cross_sel*\" -o -name \"*lp_selection*\" -o -name \"*tab3*\" -o -name \"*table3*\" -o -name \"*fewnerd_table*\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "19b484fd-a2c4-4096-adf9-62ea813dbbdc",
  "isSidechain": false,
  "requestId": "req_011CbC3bWqaQwXbUJ4hVS9aL",
  "type": "assistant",
  "uuid": "0423d483-00d4-4242-9f15-e340fd649e93",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "a97de670-f9a7-4d30-affd-382982b8a334",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YR9BTrPw62jwNBevjEuP1A",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6441,
      "cache_read_input_tokens": 72412,
      "output_tokens": 5116,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 6441,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 5116,
          "cache_read_input_tokens": 72412,
          "cache_creation_input_tokens": 6441,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 6441
          },
          "type": "message"
        }
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

_source line 84_

```json
{
  "type": "last-prompt",
  "leafUuid": "0423d483-00d4-4242-9f15-e340fd649e93",
  "sessionId": "a97de670-f9a7-4d30-affd-382982b8a334"
}
```

---

### Runtime record

_source line 85_

```json
{
  "type": "ai-title",
  "aiTitle": "Audit data inconsistencies in paper tables",
  "sessionId": "a97de670-f9a7-4d30-affd-382982b8a334"
}
```

---

### Tool result

_source line 86 · 2026-05-19T13:59:52.905Z_

<details><summary>↩ Tool result · `toolu_01MieHXuoBqohFJCCDBSLzD5`</summary>

```text
Perfect! I found both tables. Let me extract the exact information you need:

## Table 3 (tab:fewnerd) from experiments.tex

**Exact table caption (line 114):**
"LP selection across datasets (Qwen3-8B, $N{=}8$, $T{=}1.0$, gold-filtered). Few-NERD/CoNLL: 3-seed means; SciERC: single-seed (3-seed in Table~\ref{tab:multiseed}). $p$: paired bootstrap."

**CoNLL values (row on line 122):**
- n: 2,756
- Greedy: .908
- Degen.%: 48.4%
- LP ρ: .302
- LP Δ: −0.85 pp
- p: 1.0

**Few-NERD values (row on line 124):**
- n: 32,565
- Greedy: .748
- Degen.%: 13.8%
- LP ρ: .220
- LP Δ: **+1.39** pp (bolded in original)
- p: <.001

**Key specification from caption:** The table specifies **3-seed means for both Few-NERD and CoNLL**. The caption explicitly states this covers N=8.

---

## Cross-selection table (tab:cross_selection) from appendix.tex

**Exact table caption (lines 237-238):**
"Best-of-$N$ selection F1 (macro, instance-averaged) across configurations ($T{=}1.0$, 3-seed mean). Best non-oracle signal per row in \textbf{bold}. LP is the only signal with positive selection on both FewNERD configurations (Qwen $+1.39$~pp, Table~\ref{tab:fewnerd}; LLaMA $+0.36$~pp). At $N{=}16$ on LLaMA CoNLL, VC achieves small but significant gains ($+0.28$~pp, $p{<}0.03$; see text below). CoNLL shows especially tight clustering where greedy already exceeds 0.90."

**Qwen/CoNLL N=8 row (line 248):**
- Config: Qwen/CoNLL N=8
- n: 2,756
- Greedy: .908
- Oracle: .957
- SJ: .899
- FK: .893
- EM: .898
- LP: .897
- VC: .895

Note: The table does not show a separate "LP Δ" column; instead it shows absolute F1 values. The Δ (delta) is computed implicitly as the difference from Greedy (e.g., LP .897 − Greedy .908 = −0.011 or −1.1 pp).

**Seed specification:** The caption states "3-seed mean" explicitly for this table.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f989c8cf-b773-411e-87fc-82f42ffface5",
  "isSidechain": false,
  "promptId": "0731b9be-f5e6-4a8a-9a3c-2edafe06629b",
  "type": "user",
  "uuid": "731ba5f4-5c19-45b4-af1c-7862e81d49f2",
  "toolUseResult": {
    "status": "completed",
    "prompt": "Read the file /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex lines 100-140, focusing on Table 3 (tab:fewnerd). I need:\n1. The exact table caption — does it specify N=8, 3-seed mean, or single seed?\n2. All CoNLL values in the table (n, greedy, degen%, LP ρ, LP Δ, p-value)\n3. All FewNERD values in the table\n4. Any footnotes or annotations about how values were computed\n\nAlso read /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex lines 230-270 for the cross-selection table (tab:cross_selection). I need:\n1. The exact table caption\n2. The Qwen/CoNLL N=8 row — all values including LP F1 and how Δ is computed\n3. Whether the appendix specifies seed or 3-seed mean",
    "agentId": "a67b644301d2976ef",
    "agentType": "Explore",
    "content": [
      {
        "type": "text",
        "text": "Perfect! I found both tables. Let me extract the exact information you need:\n\n## Table 3 (tab:fewnerd) from experiments.tex\n\n**Exact table caption (line 114):**\n\"LP selection across datasets (Qwen3-8B, $N{=}8$, $T{=}1.0$, gold-filtered). Few-NERD/CoNLL: 3-seed means; SciERC: single-seed (3-seed in Table~\\ref{tab:multiseed}). $p$: paired bootstrap.\"\n\n**CoNLL values (row on line 122):**\n- n: 2,756\n- Greedy: .908\n- Degen.%: 48.4%\n- LP ρ: .302\n- LP Δ: −0.85 pp\n- p: 1.0\n\n**Few-NERD values (row on line 124):**\n- n: 32,565\n- Greedy: .748\n- Degen.%: 13.8%\n- LP ρ: .220\n- LP Δ: **+1.39** pp (bolded in original)\n- p: <.001\n\n**Key specification from caption:** The table specifies **3-seed means for both Few-NERD and CoNLL**. The caption explicitly states this covers N=8.\n\n---\n\n## Cross-selection table (tab:cross_selection) from appendix.tex\n\n**Exact table caption (lines 237-238):**\n\"Best-of-$N$ selection F1 (macro, instance-averaged) across configurations ($T{=}1.0$, 3-seed mean). Best non-oracle signal per row in \\textbf{bold}. LP is the only signal with positive selection on both FewNERD configurations (Qwen $+1.39$~pp, Table~\\ref{tab:fewnerd}; LLaMA $+0.36$~pp). At $N{=}16$ on LLaMA CoNLL, VC achieves small but significant gains ($+0.28$~pp, $p{<}0.03$; see text below). CoNLL shows especially tight clustering where greedy already exceeds 0.90.\"\n\n**Qwen/CoNLL N=8 row (line 248):**\n- Config: Qwen/CoNLL N=8\n- n: 2,756\n- Greedy: .908\n- Oracle: .957\n- SJ: .899\n- FK: .893\n- EM: .898\n- LP: .897\n- VC: .895\n\nNote: The table does not show a separate \"LP Δ\" column; instead it shows absolute F1 values. The Δ (delta) is computed implicitly as the difference from Greedy (e.g., LP .897 − Greedy .908 = −0.011 or −1.1 pp).\n\n**Seed specification:** The caption states \"3-seed mean\" explicitly for this table."
      }
    ],
    "totalDurationMs": 12052,
    "totalTokens": 25682,
    "totalToolUseCount": 2,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 4548,
      "cache_read_input_tokens": 20409,
      "output_tokens": 718,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4548
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7,
          "output_tokens": 718,
          "cache_read_input_tokens": 20409,
          "cache_creation_input_tokens": 4548,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4548,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 2,
      "searchCount": 0,
      "bashCount": 0,
      "editFileCount": 0,
      "linesAdded": 0,
      "linesRemoved": 0,
      "otherToolCount": 0
    }
  },
  "sourceToolAssistantUUID": "f989c8cf-b773-411e-87fc-82f42ffface5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "a97de670-f9a7-4d30-affd-382982b8a334",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 87 · 2026-05-19T13:59:52.984Z_

<details><summary>↩ Tool result · `toolu_01WsjGxjhKvqHYJwqNS3qmsH`</summary>

```text
exp_010_selection_curves: status=DONE, keys=['scierc_ner', 'scierc_re', 'conll_ner']
{
  "scierc_ner": {
    "n_instances": 551,
    "greedy_f1": 0.618,
    "N16": {
      "oracle": 0.787,
      "SJ": 0.62,
      "FK": 0.621,
      "logprob": 0.621,
      "voting_conf": 0.585,
      "EM": 0.606,
      "random": 0.595
    },
    "N8": {
      "oracle": 0.752,
      "SJ": 0.614,
      "FK": 0.614,
      "logprob": 0.619,
      "voting_conf": 0.591,
      "EM": 0.603,
      "random": 0.589
    },
    "N4": {
      "oracle": 0.714,
      "SJ": 0.607,
      "FK": 0.608,
      "logprob": 0.616,
      "voting_conf": 0.594,
      "EM": 0.6,
      "random": 0.587
    }
  },
  "scierc_re": {
    "n_instances": 397,
    "greedy_f1": 0.403,
    "N16": {
      "oracle": 0.631,
      "SJ": 0.397,
      "FK": 0.396,
      "logprob": 0.41,
      "voting_conf": 0.408,
      "EM": 0.381,
      "random": 0.364
    },
    "N8": {
      "oracle": 0.583,
      "SJ": 0.393,
      "FK": 0.394,
      "logprob": 0.413,
      "voting_conf": 0.398,
      "EM": 0.381,
      "random": 0.363
    }
  },
  "conll_ner": {
    "n_instances": 3453,
    "greedy_f1": 0.725,
    "N8": {
      "oracle": 0.757,
      "SJ": 0.718,
      "FK": 0.717,
      "logprob": 0.716,
      "voting_conf": 0.714,
      "EM": 0.716,
      "random": 0.69
    },
    "N4": {
      "oracle": 0.746,
      "SJ": 0.714,
      "FK": 0.714,
      "logprob": 0.715,
      "voting_conf": 0.714,
      "EM": 0.712,
      "random": 0.692
    }
  }
}

exp_ccs_selection: status=DONE, keys=[]
{}

exp_selective_prediction: status=DONE, keys=['vc_best_signal', 'f1_at_80pct_coverage', 'precision_coverage_curves']
{
  "vc_best_signal": true,
  "f1_at_80pct_coverage": {
    "scierc": "+5.0pp",
    "conll": "+8.4pp",
    "fewnerd": "+6.2pp"
  },
  "precision_coverage_curves": "output/prescriptive_analysis/fig_selective_prediction.pdf"
}

exp_vc_lp_cascade_selection: status=DONE, keys=[]
{}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "19b484fd-a2c4-4096-adf9-62ea813dbbdc",
  "isSidechain": false,
  "promptId": "0731b9be-f5e6-4a8a-9a3c-2edafe06629b",
  "type": "user",
  "uuid": "754aeb17-b11f-4be7-bfe2-d6c68b942d5c",
  "toolUseResult": {
    "stdout": "exp_010_selection_curves: status=DONE, keys=['scierc_ner', 'scierc_re', 'conll_ner']\n{\n  \"scierc_ner\": {\n    \"n_instances\": 551,\n    \"greedy_f1\": 0.618,\n    \"N16\": {\n      \"oracle\": 0.787,\n      \"SJ\": 0.62,\n      \"FK\": 0.621,\n      \"logprob\": 0.621,\n      \"voting_conf\": 0.585,\n      \"EM\": 0.606,\n      \"random\": 0.595\n    },\n    \"N8\": {\n      \"oracle\": 0.752,\n      \"SJ\": 0.614,\n      \"FK\": 0.614,\n      \"logprob\": 0.619,\n      \"voting_conf\": 0.591,\n      \"EM\": 0.603,\n      \"random\": 0.589\n    },\n    \"N4\": {\n      \"oracle\": 0.714,\n      \"SJ\": 0.607,\n      \"FK\": 0.608,\n      \"logprob\": 0.616,\n      \"voting_conf\": 0.594,\n      \"EM\": 0.6,\n      \"random\": 0.587\n    }\n  },\n  \"scierc_re\": {\n    \"n_instances\": 397,\n    \"greedy_f1\": 0.403,\n    \"N16\": {\n      \"oracle\": 0.631,\n      \"SJ\": 0.397,\n      \"FK\": 0.396,\n      \"logprob\": 0.41,\n      \"voting_conf\": 0.408,\n      \"EM\": 0.381,\n      \"random\": 0.364\n    },\n    \"N8\": {\n      \"oracle\": 0.583,\n      \"SJ\": 0.393,\n      \"FK\": 0.394,\n      \"logprob\": 0.413,\n      \"voting_conf\": 0.398,\n      \"EM\": 0.381,\n      \"random\": 0.363\n    }\n  },\n  \"conll_ner\": {\n    \"n_instances\": 3453,\n    \"greedy_f1\": 0.725,\n    \"N8\": {\n      \"oracle\": 0.757,\n      \"SJ\": 0.718,\n      \"FK\": 0.717,\n      \"logprob\": 0.716,\n      \"voting_conf\": 0.714,\n      \"EM\": 0.716,\n      \"random\": 0.69\n    },\n    \"N4\": {\n      \"oracle\": 0.746,\n      \"SJ\": 0.714,\n      \"FK\": 0.714,\n      \"logprob\": 0.715,\n      \"voting_conf\": 0.714,\n      \"EM\": 0.712,\n      \"random\": 0.692\n    }\n  }\n}\n\nexp_ccs_selection: status=DONE, keys=[]\n{}\n\nexp_selective_prediction: status=DONE, keys=['vc_best_signal', 'f1_at_80pct_coverage', 'precision_coverage_curves']\n{\n  \"vc_best_signal\": true,\n  \"f1_at_80pct_coverage\": {\n    \"scierc\": \"+5.0pp\",\n    \"conll\": \"+8.4pp\",\n    \"fewnerd\": \"+6.2pp\"\n  },\n  \"precision_coverage_curves\": \"output/prescriptive_analysis/fig_selective_prediction.pdf\"\n}\n\nexp_vc_lp_cascade_selection: status=DONE, keys=[]\n{}",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "19b484fd-a2c4-4096-adf9-62ea813dbbdc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "a97de670-f9a7-4d30-affd-382982b8a334",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 88 · 2026-05-19T13:59:53.361Z_

<details><summary>↩ Tool result · `toolu_01R3CAhzhuXjdYLURzCwqJiA`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/struct_self_consist_ie/output/dals_analysis.json\\n/root/autodl-tmp/struct_self_consist_ie/output/dals_hardening_results.json\\n/root/autodl-tmp/struct_self_consist_ie/output/statistical_hardening/w1_table3_multiseed.json\\n/root/autodl-tmp/struct_self_consist_ie/output/fewnerd_dals_multiseed_results.json\\n/root/autodl-tmp/struct_self_consist_ie/output/task2_dals_cross_model.py\\n/root/autodl-tmp/struct_self_consist_ie/output/dals_cross_model.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.37}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0423d483-00d4-4242-9f15-e340fd649e93",
  "isSidechain": false,
  "promptId": "0731b9be-f5e6-4a8a-9a3c-2edafe06629b",
  "type": "user",
  "uuid": "967c2f39-b384-4451-bf18-6292193b498d",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"/root/autodl-tmp/struct_self_consist_ie/output/dals_analysis.json\\\\n/root/autodl-tmp/struct_self_consist_ie/output/dals_hardening_results.json\\\\n/root/autodl-tmp/struct_self_consist_ie/output/statistical_hardening/w1_table3_multiseed.json\\\\n/root/autodl-tmp/struct_self_consist_ie/output/fewnerd_dals_multiseed_results.json\\\\n/root/autodl-tmp/struct_self_consist_ie/output/task2_dals_cross_model.py\\\\n/root/autodl-tmp/struct_self_consist_ie/output/dals_cross_model.json\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.37}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/struct_self_consist_ie/output/dals_analysis.json\\n/root/autodl-tmp/struct_self_consist_ie/output/dals_hardening_results.json\\n/root/autodl-tmp/struct_self_consist_ie/output/statistical_hardening/w1_table3_multiseed.json\\n/root/autodl-tmp/struct_self_consist_ie/output/fewnerd_dals_multiseed_results.json\\n/root/autodl-tmp/struct_self_consist_ie/output/task2_dals_cross_model.py\\n/root/autodl-tmp/struct_self_consist_ie/output/dals_cross_model.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.37}}"
    }
  },
  "sourceToolAssistantUUID": "0423d483-00d4-4242-9f15-e340fd649e93",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "a97de670-f9a7-4d30-affd-382982b8a334",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 89 · 2026-05-19T13:59:53.366Z_

```json
{
  "parentUuid": "967c2f39-b384-4451-bf18-6292193b498d",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "86acb395-3729-4e77-8df8-d5ad98c58dea",
  "timestamp": "2026-05-19T13:59:53.366Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "a97de670-f9a7-4d30-affd-382982b8a334",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 90 · 2026-05-19T13:59:58.372Z_

<details><summary>Logged reasoning block</summary>

```text
There's a `w1_table3_multiseed.json` file! That's exactly what I need for the Table 3 multi-seed data. Let me read that, along with the dals files.

Now I have confirmation:
- Table 3 caption says "3-seed means" for Few-NERD and CoNLL
- But Table 3 shows CoNLL degen=48.4%, which matches N=16 data (exp_002_conll_n16) 
- N=8 single-seed degeneracy is 59.1%

Let me get the multi-seed table data.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "86acb395-3729-4e77-8df8-d5ad98c58dea",
  "isSidechain": false,
  "requestId": "req_011CbC3jEGeXBQpkJKgAX2Bf",
  "type": "assistant",
  "uuid": "bfe90c92-d2f3-496e-bdc8-3e4ca1b107cd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "a97de670-f9a7-4d30-affd-382982b8a334",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PPxFpcGmj4KzTAdFU7uPrK",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7198,
      "cache_read_input_tokens": 78853,
      "output_tokens": 557,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 7198,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 557,
          "cache_read_input_tokens": 78853,
          "cache_creation_input_tokens": 7198,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 7198
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

_source line 91 · 2026-05-19T13:59:59.328Z_

Found `w1_table3_multiseed.json` — the authoritative multi-seed source for Table 3. Let me read it along with related files.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bfe90c92-d2f3-496e-bdc8-3e4ca1b107cd",
  "isSidechain": false,
  "requestId": "req_011CbC3jEGeXBQpkJKgAX2Bf",
  "type": "assistant",
  "uuid": "c8443ea5-2cd5-4b86-88ce-36f4fc4de322",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "a97de670-f9a7-4d30-affd-382982b8a334",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PPxFpcGmj4KzTAdFU7uPrK",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7198,
      "cache_read_input_tokens": 78853,
      "output_tokens": 557,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 7198,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 557,
          "cache_read_input_tokens": 78853,
          "cache_creation_input_tokens": 7198,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 7198
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

_source line 92 · 2026-05-19T14:00:00.282Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01LGNjgwm3PJynX39rEUYgzC`</summary>

```json
{
  "server": "autodl-5090",
  "command": "cat /root/autodl-tmp/struct_self_consist_ie/output/statistical_hardening/w1_table3_multiseed.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c8443ea5-2cd5-4b86-88ce-36f4fc4de322",
  "isSidechain": false,
  "requestId": "req_011CbC3jEGeXBQpkJKgAX2Bf",
  "type": "assistant",
  "uuid": "45266182-d014-47de-88e9-8caac2417c75",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "a97de670-f9a7-4d30-affd-382982b8a334",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PPxFpcGmj4KzTAdFU7uPrK",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7198,
      "cache_read_input_tokens": 78853,
      "output_tokens": 557,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 7198,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 557,
          "cache_read_input_tokens": 78853,
          "cache_creation_input_tokens": 7198,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 7198
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

_source line 93 · 2026-05-19T14:00:00.661Z_

<details><summary>↩ Tool result · `toolu_01LGNjgwm3PJynX39rEUYgzC`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"scierc_n8\\\": {\\n    \\\"seeds\\\": [\\n      42,\\n      123,\\n      456\\n    ],\\n    \\\"n_seeds\\\": 3,\\n    \\\"greedy_f1\\\": {\\n      \\\"mean\\\": 0.6458309540762559,\\n      \\\"std\\\": 0.0019530701379806984,\\n      \\\"per_seed\\\": {\\n        \\\"42\\\": 0.6439219990259687,\\n        \\\"123\\\": 0.6457455273145254,\\n        \\\"456\\\": 0.6478253358882736\\n      }\\n    },\\n    \\\"oracle_f1\\\": {\\n      \\\"mean\\\": 0.7763733508441953,\\n      \\\"std\\\": 0.003870215946919221,\\n      \\\"per_seed\\\": {\\n        \\\"42\\\": 0.7758023559647044,\\n        \\\"123\\\": 0.7804973434463037,\\n        \\\"456\\\": 0.7728203531215777\\n      }\\n    },\\n    \\\"headroom_pp\\\": {\\n      \\\"mean\\\": 13.054239676793935,\\n      \\\"std\\\": 0.5014118491848302,\\n      \\\"per_seed\\\": {\\n        \\\"42\\\": 13.188035693873568,\\n        \\\"123\\\": 13.475181613177833,\\n        \\\"456\\\": 12.499501723330408\\n      }\\n    },\\n    \\\"lp_sel_f1\\\": {\\n      \\\"mean\\\": 0.6462262034846267,\\n      \\\"std\\\": 0.0034002376795566574,\\n      \\\"per_seed\\\": {\\n        \\\"42\\\": 0.6500718843902431,\\n        \\\"123\\\": 0.6436180382499742,\\n        \\\"456\\\": 0.6449886878136628\\n      }\\n    },\\n    \\\"lp_delta_pp\\\": {\\n      \\\"mean\\\": 0.039524940837080504,\\n      \\\"std\\\": 0.49962588868193314,\\n      \\\"per_seed\\\": {\\n        \\\"42\\\": 0.614988536427441,\\n        \\\"123\\\": -0.21274890645511801,\\n        \\\"456\\\": -0.28366480746108147\\n      }\\n    },\\n    \\\"sj_sel_f1\\\": {\\n      \\\"mean\\\": 0.641316270203835,\\n      \\\"std\\\": 0.008619368987879657,\\n      \\\"per_seed\\\": {\\n        \\\"42\\\": 0.6450050009215592,\\n        \\\"123\\\": 0.6474774323740186,\\n        \\\"456\\\": 0.631466377315927\\n      }\\n    },\\n    \\\"em_sel_f1\\\": {\\n      \\\"mean\\\": 0.6339031229999631,\\n      \\\"std\\\": 0.005686848220610245,\\n      \\\"per_seed\\\": {\\n        \\\"42\\\": 0.636232670839558,\\n        \\\"123\\\": 0.6380553169972719,\\n        \\\"456\\\": 0.6274213811630595\\n      }\\n    },\\n    \\\"sj_delta_pp\\\": {\\n      \\\"mean\\\": -0.451468387242097,\\n      \\\"std\\\": 1.0262572835527375,\\n      \\\"per_seed\\\": {\\n        \\\"42\\\": 0.10830018955905185,\\n        \\\"123\\\": 0.17319050594931662,\\n        \\\"456\\\": -1.6358958572346594\\n      }\\n    },\\n    \\\"em_delta_pp\\\": {\\n      \\\"mean\\\": -1.1927831076292768,\\n      \\\"std\\\": 0.7340538418834969,\\n      \\\"per_seed\\\": {\\n        \\\"42\\\": -0.768932818641066,\\n        \\\"123\\\": -0.7690210317253476,\\n        \\\"456\\\": -2.040395472521417\\n      }\\n    },\\n    \\\"n_instances\\\": {\\n      \\\"42\\\": 529,\\n      \\\"123\\\": 529,\\n      \\\"456\\\": 529\\n    }\\n  },\\n  \\\"scierc_n16\\\": {\\n    \\\"seeds\\\": [\\n      42,\\n      123,\\n      456\\n    ],\\n    \\\"n_seeds\\\": 3,\\n    \\\"greedy_f1\\\": {\\n      \\\"mean\\\": 0.6440954527966648,\\n      \\\"std\\\": 0.00015021537180503046,\\n      \\\"per_seed\\\": {\\n        \\\"42\\\": 0.6441821796820129,\\n        \\\"123\\\": 0.6441821796820129,\\n        \\\"456\\\": 0.6439219990259687\\n      }\\n    },\\n    \\\"oracle_f1\\\": {\\n      \\\"mean\\\": 0.8198342597680971,\\n      \\\"std\\\": 0.002876403003560939,\\n      \\\"per_seed\\\": {\\n        \\\"42\\\": 0.8193707573669766,\\n        \\\"123\\\": 0.8172177538907217,\\n        \\\"456\\\": 0.8229142680465932\\n      }\\n    },\\n    \\\"headroom_pp\\\": {\\n      \\\"mean\\\": 17.573880697143238,\\n      \\\"std\\\": 0.3016225699668626,\\n      \\\"per_seed\\\": {\\n        \\\"42\\\": 17.518857768496375,\\n        \\\"123\\\": 17.303557420870884,\\n        \\\"456\\\": 17.89922690206245\\n      }\\n    },\\n    \\\"lp_sel_f1\\\": {\\n      \\\"mean\\\": 0.648785240888163,\\n      \\\"std\\\": 0.00695257791298551,\\n      \\\"per_seed\\\": {\\n        \\\"42\\\": 0.6465303389349577,\\n        \\\"123\\\": 0.6432399935708064,\\n        \\\"456\\\": 0.656585390158725\\n      }\\n    },\\n    \\\"lp_delta_pp\\\": {\\n      \\\"mean\\\": 0.4689788091498226,\\n      \\\"std\\\": 0.709861622068116,\\n      \\\"per_seed\\\": {\\n        \\\"42\\\": 0.2348159252944848,\\n        \\\"123\\\": -0.09421861112064445,\\n        \\\"456\\\": 1.2663391132756274\\n      }\\n    },\\n    \\\"sj_sel_f1\\\": {\\n      \\\"mean\\\": 0.6435605589002676,\\n      \\\"std\\\": 0.0023779841874772938,\\n      \\\"per_seed\\\": {\\n        \\\"42\\\": 0.646212731570788,\\n        \\\"123\\\": 0.6428503409683216,\\n        \\\"456\\\": 0.6416186041616933\\n      }\\n    },\\n    \\\"em_sel_f1\\\": {\\n      \\\"mean\\\": 0.6350290375615629,\\n      \\\"std\\\": 0.0038887249387768116,\\n      \\\"per_seed\\\": {\\n        \\\"42\\\": 0.6312245086541762,\\n        \\\"123\\\": 0.6389968168406954,\\n        \\\"456\\\": 0.6348657871898169\\n      }\\n    },\\n    \\\"sj_delta_pp\\\": {\\n      \\\"mean\\\": -0.053489389639719644,\\n      \\\"std\\\": 0.22742283077844724,\\n      \\\"per_seed\\\": {\\n        \\\"42\\\": 0.20305518887751006,\\n        \\\"123\\\": -0.13318387136912468,\\n        \\\"456\\\": -0.23033948642754432\\n      }\\n    },\\n    \\\"em_delta_pp\\\": {\\n      \\\"mean\\\": -0.9066415235101951,\\n      \\\"std\\\": 0.3886164139427325,\\n      \\\"per_seed\\\": {\\n        \\\"42\\\": -1.2957671027836626,\\n        \\\"123\\\": -0.5185362841317431,\\n        \\\"456\\\": -0.9056211836151795\\n      }\\n    },\\n    \\\"n_instances\\\": {\\n      \\\"42\\\": 529,\\n      \\\"123\\\": 529,\\n      \\\"456\\\": 529\\n    }\\n  },\\n  \\\"conll_n8\\\": {\\n    \\\"seeds\\\": [\\n      42\\n    ],\\n    \\\"n_seeds\\\": 1,\\n    \\\"greedy_f1\\\": {\\n      \\\"mean\\\": 0.9078871741063325,\\n      \\\"std\\\": 0.0,\\n      \\\"per_seed\\\": {\\n        \\\"42\\\": 0.9078871741063325\\n      }\\n    },\\n    \\\"oracle_f1\\\": {\\n      \\\"mean\\\": 0.948271330346802,\\n      \\\"std\\\": 0.0,\\n      \\\"per_seed\\\": {\\n        \\\"42\\\": 0.948271330346802\\n      }\\n    },\\n    \\\"headroom_pp\\\": {\\n      \\\"mean\\\": 4.038415624046953,\\n      \\\"std\\\": 0.0,\\n      \\\"per_seed\\\": {\\n        \\\"42\\\": 4.038415624046953\\n      }\\n    },\\n    \\\"lp_sel_f1\\\": {\\n      \\\"mean\\\": 0.8974051146077575,\\n      \\\"std\\\": 0.0,\\n      \\\"per_seed\\\": {\\n        \\\"42\\\": 0.8974051146077575\\n      }\\n    },\\n    \\\"lp_delta_pp\\\": {\\n      \\\"mean\\\": -1.0482059498574947,\\n      \\\"std\\\": 0.0,\\n      \\\"per_seed\\\": {\\n        \\\"42\\\": -1.0482059498574947\\n      }\\n    },\\n    \\\"sj_sel_f1\\\": {\\n      \\\"mean\\\": 0.8989733506696497,\\n      \\\"std\\\": 0.0,\\n      \\\"per_seed\\\": {\\n        \\\"42\\\": 0.8989733506696497\\n      }\\n    },\\n    \\\"em_sel_f1\\\": {\\n      \\\"mean\\\": 0.8971423200650341,\\n      \\\"std\\\": 0.0,\\n      \\\"per_seed\\\": {\\n        \\\"42\\\": 0.8971423200650341\\n      }\\n    },\\n    \\\"sj_delta_pp\\\": {\\n      \\\"mean\\\": -0.8913823436682788,\\n      \\\"std\\\": 0.0,\\n      \\\"per_seed\\\": {\\n        \\\"42\\\": -0.8913823436682788\\n      }\\n    },\\n    \\\"em_delta_pp\\\": {\\n      \\\"mean\\\": -1.0744854041298324,\\n      \\\"std\\\": 0.0,\\n      \\\"per_seed\\\": {\\n        \\\"42\\\": -1.0744854041298324\\n      }\\n    },\\n    \\\"n_instances\\\": {\\n      \\\"42\\\": 2756\\n    }\\n  },\\n  \\\"fewnerd_n8\\\": {\\n    \\\"seeds\\\": [\\n      42\\n    ],\\n    \\\"n_seeds\\\": 1,\\n    \\\"n_instances\\\": {\\n      \\\"42\\\": 32565\\n    },\\n    \\\"greedy_f1\\\": {\\n      \\\"mean\\\": 0.7478465965854552,\\n      \\\"std\\\": 0.0,\\n      \\\"per_seed\\\": {\\n        \\\"42\\\": 0.7478465965854552\\n      }\\n    },\\n    \\\"oracle_f1\\\": {\\n      \\\"mean\\\": 0.8718523412957434,\\n      \\\"std\\\": 0.0,\\n      \\\"per_seed\\\": {\\n        \\\"42\\\": 0.8718523412957434\\n      }\\n    },\\n    \\\"headroom_pp\\\": {\\n      \\\"mean\\\": 12.400574471028825,\\n      \\\"std\\\": 0.0,\\n      \\\"per_seed\\\": {\\n        \\\"42\\\": 12.400574471028825\\n      }\\n    },\\n    \\\"lp_sel_f1\\\": {\\n      \\\"mean\\\": 0.7613975687723666,\\n      \\\"std\\\": 0.0,\\n      \\\"per_seed\\\": {\\n        \\\"42\\\": 0.7613975687723666\\n      }\\n    },\\n    \\\"lp_delta_pp\\\": {\\n      \\\"mean\\\": 1.355097218691148,\\n      \\\"std\\\": 0.0,\\n      \\\"per_seed\\\": {\\n        \\\"42\\\": 1.355097218691148\\n      }\\n    }\\n  }\\n}\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.37}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "45266182-d014-47de-88e9-8caac2417c75",
  "isSidechain": false,
  "promptId": "0731b9be-f5e6-4a8a-9a3c-2edafe06629b",
  "type": "user",
  "uuid": "0eea851c-99aa-4bd0-9dfa-6c9b999b951b",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"{\\\\n  \\\\\\\"scierc_n8\\\\\\\": {\\\\n    \\\\\\\"seeds\\\\\\\": [\\\\n      42,\\\\n      123,\\\\n      456\\\\n    ],\\\\n    \\\\\\\"n_seeds\\\\\\\": 3,\\\\n    \\\\\\\"greedy_f1\\\\\\\": {\\\\n      \\\\\\\"mean\\\\\\\": 0.6458309540762559,\\\\n      \\\\\\\"std\\\\\\\": 0.0019530701379806984,\\\\n      \\\\\\\"per_seed\\\\\\\": {\\\\n        \\\\\\\"42\\\\\\\": 0.6439219990259687,\\\\n        \\\\\\\"123\\\\\\\": 0.6457455273145254,\\\\n        \\\\\\\"456\\\\\\\": 0.6478253358882736\\\\n      }\\\\n    },\\\\n    \\\\\\\"oracle_f1\\\\\\\": {\\\\n      \\\\\\\"mean\\\\\\\": 0.7763733508441953,\\\\n      \\\\\\\"std\\\\\\\": 0.003870215946919221,\\\\n      \\\\\\\"per_seed\\\\\\\": {\\\\n        \\\\\\\"42\\\\\\\": 0.7758023559647044,\\\\n        \\\\\\\"123\\\\\\\": 0.7804973434463037,\\\\n        \\\\\\\"456\\\\\\\": 0.7728203531215777\\\\n      }\\\\n    },\\\\n    \\\\\\\"headroom_pp\\\\\\\": {\\\\n      \\\\\\\"mean\\\\\\\": 13.054239676793935,\\\\n      \\\\\\\"std\\\\\\\": 0.5014118491848302,\\\\n      \\\\\\\"per_seed\\\\\\\": {\\\\n        \\\\\\\"42\\\\\\\": 13.188035693873568,\\\\n        \\\\\\\"123\\\\\\\": 13.475181613177833,\\\\n        \\\\\\\"456\\\\\\\": 12.499501723330408\\\\n      }\\\\n    },\\\\n    \\\\\\\"lp_sel_f1\\\\\\\": {\\\\n      \\\\\\\"mean\\\\\\\": 0.6462262034846267,\\\\n      \\\\\\\"std\\\\\\\": 0.0034002376795566574,\\\\n      \\\\\\\"per_seed\\\\\\\": {\\\\n        \\\\\\\"42\\\\\\\": 0.6500718843902431,\\\\n        \\\\\\\"123\\\\\\\": 0.6436180382499742,\\\\n        \\\\\\\"456\\\\\\\": 0.6449886878136628\\\\n      }\\\\n    },\\\\n    \\\\\\\"lp_delta_pp\\\\\\\": {\\\\n      \\\\\\\"mean\\\\\\\": 0.039524940837080504,\\\\n      \\\\\\\"std\\\\\\\": 0.49962588868193314,\\\\n      \\\\\\\"per_seed\\\\\\\": {\\\\n        \\\\\\\"42\\\\\\\": 0.614988536427441,\\\\n        \\\\\\\"123\\\\\\\": -0.21274890645511801,\\\\n        \\\\\\\"456\\\\\\\": -0.28366480746108147\\\\n      }\\\\n    },\\\\n    \\\\\\\"sj_sel_f1\\\\\\\": {\\\\n      \\\\\\\"mean\\\\\\\": 0.641316270203835,\\\\n      \\\\\\\"std\\\\\\\": 0.008619368987879657,\\\\n      \\\\\\\"per_seed\\\\\\\": {\\\\n        \\\\\\\"42\\\\\\\": 0.6450050009215592,\\\\n        \\\\\\\"123\\\\\\\": 0.6474774323740186,\\\\n        \\\\\\\"456\\\\\\\": 0.631466377315927\\\\n      }\\\\n    },\\\\n    \\\\\\\"em_sel_f1\\\\\\\": {\\\\n      \\\\\\\"mean\\\\\\\": 0.6339031229999631,\\\\n      \\\\\\\"std\\\\\\\": 0.005686848220610245,\\\\n      \\\\\\\"per_seed\\\\\\\": {\\\\n        \\\\\\\"42\\\\\\\": 0.636232670839558,\\\\n        \\\\\\\"123\\\\\\\": 0.6380553169972719,\\\\n        \\\\\\\"456\\\\\\\": 0.6274213811630595\\\\n      }\\\\n    },\\\\n    \\\\\\\"sj_delta_pp\\\\\\\": {\\\\n      \\\\\\\"mean\\\\\\\": -0.451468387242097,\\\\n      \\\\\\\"std\\\\\\\": 1.0262572835527375,\\\\n      \\\\\\\"per_seed\\\\\\\": {\\\\n        \\\\\\\"42\\\\\\\": 0.10830018955905185,\\\\n        \\\\\\\"123\\\\\\\": 0.17319050594931662,\\\\n        \\\\\\\"456\\\\\\\": -1.6358958572346594\\\\n      }\\\\n    },\\\\n    \\\\\\\"em_delta_pp\\\\\\\": {\\\\n      \\\\\\\"mean\\\\\\\": -1.1927831076292768,\\\\n      \\\\\\\"std\\\\\\\": 0.7340538418834969,\\\\n      \\\\\\\"per_seed\\\\\\\": {\\\\n        \\\\\\\"42\\\\\\\": -0.768932818641066,\\\\n        \\\\\\\"123\\\\\\\": -0.7690210317253476,\\\\n        \\\\\\\"456\\\\\\\": -2.040395472521417\\\\n      }\\\\n    },\\\\n    \\\\\\\"n_instances\\\\\\\": {\\\\n      \\\\\\\"42\\\\\\\": 529,\\\\n      \\\\\\\"123\\\\\\\": 529,\\\\n      \\\\\\\"456\\\\\\\": 529\\\\n    }\\\\n  },\\\\n  \\\\\\\"scierc_n16\\\\\\\": {\\\\n    \\\\\\\"seeds\\\\\\\": [\\\\n      42,\\\\n      123,\\\\n      456\\\\n    ],\\\\n    \\\\\\\"n_seeds\\\\\\\": 3,\\\\n    \\\\\\\"greedy_f1\\\\\\\": {\\\\n      \\\\\\\"mean\\\\\\\": 0.6440954527966648,\\\\n      \\\\\\\"std\\\\\\\": 0.00015021537180503046,\\\\n      \\\\\\\"per_seed\\\\\\\": {\\\\n        \\\\\\\"42\\\\\\\": 0.6441821796820129,\\\\n        \\\\\\\"123\\\\\\\": 0.6441821796820129,\\\\n        \\\\\\\"456\\\\\\\": 0.6439219990259687\\\\n      }\\\\n    },\\\\n    \\\\\\\"oracle_f1\\\\\\\": {\\\\n      \\\\\\\"mean\\\\\\\": 0.8198342597680971,\\\\n      \\\\\\\"std\\\\\\\": 0.002876403003560939,\\\\n      \\\\\\\"per_seed\\\\\\\": {\\\\n        \\\\\\\"42\\\\\\\": 0.8193707573669766,\\\\n        \\\\\\\"123\\\\\\\": 0.8172177538907217,\\\\n        \\\\\\\"456\\\\\\\": 0.8229142680465932\\\\n      }\\\\n    },\\\\n    \\\\\\\"headroom_pp\\\\\\\": {\\\\n      \\\\\\\"mean\\\\\\\": 17.573880697143238,\\\\n      \\\\\\\"std\\\\\\\": 0.3016225699668626,\\\\n      \\\\\\\"per_seed\\\\\\\": {\\\\n        \\\\\\\"42\\\\\\\": 17.518857768496375,\\\\n        \\\\\\\"123\\\\\\\": 17.303557420870884,\\\\n        \\\\\\\"456\\\\\\\": 17.89922690206245\\\\n      }\\\\n    },\\\\n    \\\\\\\"lp_sel_f1\\\\\\\": {\\\\n      \\\\\\\"mean\\\\\\\": 0.648785240888163,\\\\n      \\\\\\\"std\\\\\\\": 0.00695257791298551,\\\\n      \\\\\\\"per_seed\\\\\\\": {\\\\n        \\\\\\\"42\\\\\\\": 0.6465303389349577,\\\\n        \\\\\\\"123\\\\\\\": 0.6432399935708064,\\\\n        \\\\\\\"456\\\\\\\": 0.656585390158725\\\\n      }\\\\n    },\\\\n    \\\\\\\"lp_delta_pp\\\\\\\": {\\\\n      \\\\\\\"mean\\\\\\\": 0.4689788091498226,\\\\n      \\\\\\\"std\\\\\\\": 0.709861622068116,\\\\n      \\\\\\\"per_seed\\\\\\\": {\\\\n        \\\\\\\"42\\\\\\\": 0.2348159252944848,\\\\n        \\\\\\\"123\\\\\\\": -0.09421861112064445,\\\\n        \\\\\\\"456\\\\\\\": 1.2663391132756274\\\\n      }\\\\n    },\\\\n    \\\\\\\"sj_sel_f1\\\\\\\": {\\\\n      \\\\\\\"mean\\\\\\\": 0.6435605589002676,\\\\n      \\\\\\\"std\\\\\\\": 0.0023779841874772938,\\\\n      \\\\\\\"per_seed\\\\\\\": {\\\\n        \\\\\\\"42\\\\\\\": 0.646212731570788,\\\\n        \\\\\\\"123\\\\\\\": 0.6428503409683216,\\\\n        \\\\\\\"456\\\\\\\": 0.6416186041616933\\\\n      }\\\\n    },\\\\n    \\\\\\\"em_sel_f1\\\\\\\": {\\\\n      \\\\\\\"mean\\\\\\\": 0.6350290375615629,\\\\n      \\\\\\\"std\\\\\\\": 0.0038887249387768116,\\\\n      \\\\\\\"per_seed\\\\\\\": {\\\\n        \\\\\\\"42\\\\\\\": 0.6312245086541762,\\\\n        \\\\\\\"123\\\\\\\": 0.6389968168406954,\\\\n        \\\\\\\"456\\\\\\\": 0.6348657871898169\\\\n      }\\\\n    },\\\\n    \\\\\\\"sj_delta_pp\\\\\\\": {\\\\n      \\\\\\\"mean\\\\\\\": -0.053489389639719644,\\\\n      \\\\\\\"std\\\\\\\": 0.22742283077844724,\\\\n      \\\\\\\"per_seed\\\\\\\": {\\\\n        \\\\\\\"42\\\\\\\": 0.20305518887751006,\\\\n        \\\\\\\"123\\\\\\\": -0.13318387136912468,\\\\n        \\\\\\\"456\\\\\\\": -0.23033948642754432\\\\n      }\\\\n    },\\\\n    \\\\\\\"em_delta_pp\\\\\\\": {\\\\n      \\\\\\\"mean\\\\\\\": -0.9066415235101951,\\\\n      \\\\\\\"std\\\\\\\": 0.3886164139427325,\\\\n      \\\\\\\"per_seed\\\\\\\": {\\\\n        \\\\\\\"42\\\\\\\": -1.2957671027836626,\\\\n        \\\\\\\"123\\\\\\\": -0.5185362841317431,\\\\n        \\\\\\\"456\\\\\\\": -0.9056211836151795\\\\n      }\\\\n    },\\\\n    \\\\\\\"n_instances\\\\\\\": {\\\\n      \\\\\\\"42\\\\\\\": 529,\\\\n      \\\\\\\"123\\\\\\\": 529,\\\\n      \\\\\\\"456\\\\\\\": 529\\\\n    }\\\\n  },\\\\n  \\\\\\\"conll_n8\\\\\\\": {\\\\n    \\\\\\\"seeds\\\\\\\": [\\\\n      42\\\\n    ],\\\\n    \\\\\\\"n_seeds\\\\\\\": 1,\\\\n    \\\\\\\"greedy_f1\\\\\\\": {\\\\n      \\\\\\\"mean\\\\\\\": 0.9078871741063325,\\\\n      \\\\\\\"std\\\\\\\": 0.0,\\\\n      \\\\\\\"per_seed\\\\\\\": {\\\\n        \\\\\\\"42\\\\\\\": 0.9078871741063325\\\\n      }\\\\n    },\\\\n    \\\\\\\"oracle_f1\\\\\\\": {\\\\n      \\\\\\\"mean\\\\\\\": 0.948271330346802,\\\\n      \\\\\\\"std\\\\\\\": 0.0,\\\\n      \\\\\\\"per_seed\\\\\\\": {\\\\n        \\\\\\\"42\\\\\\\": 0.948271330346802\\\\n      }\\\\n    },\\\\n    \\\\\\\"headroom_pp\\\\\\\": {\\\\n      \\\\\\\"mean\\\\\\\": 4.038415624046953,\\\\n      \\\\\\\"std\\\\\\\": 0.0,\\\\n      \\\\\\\"per_seed\\\\\\\": {\\\\n        \\\\\\\"42\\\\\\\": 4.038415624046953\\\\n      }\\\\n    },\\\\n    \\\\\\\"lp_sel_f1\\\\\\\": {\\\\n      \\\\\\\"mean\\\\\\\": 0.8974051146077575,\\\\n      \\\\\\\"std\\\\\\\": 0.0,\\\\n      \\\\\\\"per_seed\\\\\\\": {\\\\n        \\\\\\\"42\\\\\\\": 0.8974051146077575\\\\n      }\\\\n    },\\\\n    \\\\\\\"lp_delta_pp\\\\\\\": {\\\\n      \\\\\\\"mean\\\\\\\": -1.0482059498574947,\\\\n      \\\\\\\"std\\\\\\\": 0.0,\\\\n      \\\\\\\"per_seed\\\\\\\": {\\\\n        \\\\\\\"42\\\\\\\": -1.0482059498574947\\\\n      }\\\\n    },\\\\n    \\\\\\\"sj_sel_f1\\\\\\\": {\\\\n      \\\\\\\"mean\\\\\\\": 0.8989733506696497,\\\\n      \\\\\\\"std\\\\\\\": 0.0,\\\\n      \\\\\\\"per_seed\\\\\\\": {\\\\n        \\\\\\\"42\\\\\\\": 0.8989733506696497\\\\n      }\\\\n    },\\\\n    \\\\\\\"em_sel_f1\\\\\\\": {\\\\n      \\\\\\\"mean\\\\\\\": 0.8971423200650341,\\\\n      \\\\\\\"std\\\\\\\": 0.0,\\\\n      \\\\\\\"per_seed\\\\\\\": {\\\\n        \\\\\\\"42\\\\\\\": 0.8971423200650341\\\\n      }\\\\n    },\\\\n    \\\\\\\"sj_delta_pp\\\\\\\": {\\\\n      \\\\\\\"mean\\\\\\\": -0.8913823436682788,\\\\n      \\\\\\\"std\\\\\\\": 0.0,\\\\n      \\\\\\\"per_seed\\\\\\\": {\\\\n        \\\\\\\"42\\\\\\\": -0.8913823436682788\\\\n      }\\\\n    },\\\\n    \\\\\\\"em_delta_pp\\\\\\\": {\\\\n      \\\\\\\"mean\\\\\\\": -1.0744854041298324,\\\\n      \\\\\\\"std\\\\\\\": 0.0,\\\\n      \\\\\\\"per_seed\\\\\\\": {\\\\n        \\\\\\\"42\\\\\\\": -1.0744854041298324\\\\n      }\\\\n    },\\\\n    \\\\\\\"n_instances\\\\\\\": {\\\\n      \\\\\\\"42\\\\\\\": 2756\\\\n    }\\\\n  },\\\\n  \\\\\\\"fewnerd_n8\\\\\\\": {\\\\n    \\\\\\\"seeds\\\\\\\": [\\\\n      42\\\\n    ],\\\\n    \\\\\\\"n_seeds\\\\\\\": 1,\\\\n    \\\\\\\"n_instances\\\\\\\": {\\\\n      \\\\\\\"42\\\\\\\": 32565\\\\n    },\\\\n    \\\\\\\"greedy_f1\\\\\\\": {\\\\n      \\\\\\\"mean\\\\\\\": 0.7478465965854552,\\\\n      \\\\\\\"std\\\\\\\": 0.0,\\\\n      \\\\\\\"per_seed\\\\\\\": {\\\\n        \\\\\\\"42\\\\\\\": 0.7478465965854552\\\\n      }\\\\n    },\\\\n    \\\\\\\"oracle_f1\\\\\\\": {\\\\n      \\\\\\\"mean\\\\\\\": 0.8718523412957434,\\\\n      \\\\\\\"std\\\\\\\": 0.0,\\\\n      \\\\\\\"per_seed\\\\\\\": {\\\\n        \\\\\\\"42\\\\\\\": 0.8718523412957434\\\\n      }\\\\n    },\\\\n    \\\\\\\"headroom_pp\\\\\\\": {\\\\n      \\\\\\\"mean\\\\\\\": 12.400574471028825,\\\\n      \\\\\\\"std\\\\\\\": 0.0,\\\\n      \\\\\\\"per_seed\\\\\\\": {\\\\n        \\\\\\\"42\\\\\\\": 12.400574471028825\\\\n      }\\\\n    },\\\\n    \\\\\\\"lp_sel_f1\\\\\\\": {\\\\n      \\\\\\\"mean\\\\\\\": 0.7613975687723666,\\\\n      \\\\\\\"std\\\\\\\": 0.0,\\\\n      \\\\\\\"per_seed\\\\\\\": {\\\\n        \\\\\\\"42\\\\\\\": 0.7613975687723666\\\\n      }\\\\n    },\\\\n    \\\\\\\"lp_delta_pp\\\\\\\": {\\\\n      \\\\\\\"mean\\\\\\\": 1.355097218691148,\\\\n      \\\\\\\"std\\\\\\\": 0.0,\\\\n      \\\\\\\"per_seed\\\\\\\": {\\\\n        \\\\\\\"42\\\\\\\": 1.355097218691148\\\\n      }\\\\n    }\\\\n  }\\\\n}\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.37}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"scierc_n8\\\": {\\n    \\\"seeds\\\": [\\n      42,\\n      123,\\n      456\\n    ],\\n    \\\"n_seeds\\\": 3,\\n    \\\"greedy_f1\\\": {\\n      \\\"mean\\\": 0.6458309540762559,\\n      \\\"std\\\": 0.0019530701379806984,\\n      \\\"per_seed\\\": {\\n        \\\"42\\\": 0.6439219990259687,\\n        \\\"123\\\": 0.6457455273145254,\\n        \\\"456\\\": 0.6478253358882736\\n      }\\n    },\\n    \\\"oracle_f1\\\": {\\n      \\\"mean\\\": 0.7763733508441953,\\n      \\\"std\\\": 0.003870215946919221,\\n      \\\"per_seed\\\": {\\n        \\\"42\\\": 0.7758023559647044,\\n        \\\"123\\\": 0.7804973434463037,\\n        \\\"456\\\": 0.7728203531215777\\n      }\\n    },\\n    \\\"headroom_pp\\\": {\\n      \\\"mean\\\": 13.054239676793935,\\n      \\\"std\\\": 0.5014118491848302,\\n      \\\"per_seed\\\": {\\n        \\\"42\\\": 13.188035693873568,\\n        \\\"123\\\": 13.475181613177833,\\n        \\\"456\\\": 12.499501723330408\\n      }\\n    },\\n    \\\"lp_sel_f1\\\": {\\n      \\\"mean\\\": 0.6462262034846267,\\n      \\\"std\\\": 0.0034002376795566574,\\n      \\\"per_seed\\\": {\\n        \\\"42\\\": 0.6500718843902431,\\n        \\\"123\\\": 0.6436180382499742,\\n        \\\"456\\\": 0.6449886878136628\\n      }\\n    },\\n    \\\"lp_delta_pp\\\": {\\n      \\\"mean\\\": 0.039524940837080504,\\n      \\\"std\\\": 0.49962588868193314,\\n      \\\"per_seed\\\": {\\n        \\\"42\\\": 0.614988536427441,\\n        \\\"123\\\": -0.21274890645511801,\\n        \\\"456\\\": -0.28366480746108147\\n      }\\n    },\\n    \\\"sj_sel_f1\\\": {\\n      \\\"mean\\\": 0.641316270203835,\\n      \\\"std\\\": 0.008619368987879657,\\n      \\\"per_seed\\\": {\\n        \\\"42\\\": 0.6450050009215592,\\n        \\\"123\\\": 0.6474774323740186,\\n        \\\"456\\\": 0.631466377315927\\n      }\\n    },\\n    \\\"em_sel_f1\\\": {\\n      \\\"mean\\\": 0.6339031229999631,\\n      \\\"std\\\": 0.005686848220610245,\\n      \\\"per_seed\\\": {\\n        \\\"42\\\": 0.636232670839558,\\n        \\\"123\\\": 0.6380553169972719,\\n        \\\"456\\\": 0.6274213811630595\\n      }\\n    },\\n    \\\"sj_delta_pp\\\": {\\n      \\\"mean\\\": -0.451468387242097,\\n      \\\"std\\\": 1.0262572835527375,\\n      \\\"per_seed\\\": {\\n        \\\"42\\\": 0.10830018955905185,\\n        \\\"123\\\": 0.17319050594931662,\\n        \\\"456\\\": -1.6358958572346594\\n      }\\n    },\\n    \\\"em_delta_pp\\\": {\\n      \\\"mean\\\": -1.1927831076292768,\\n      \\\"std\\\": 0.7340538418834969,\\n      \\\"per_seed\\\": {\\n        \\\"42\\\": -0.768932818641066,\\n        \\\"123\\\": -0.7690210317253476,\\n        \\\"456\\\": -2.040395472521417\\n      }\\n    },\\n    \\\"n_instances\\\": {\\n      \\\"42\\\": 529,\\n      \\\"123\\\": 529,\\n      \\\"456\\\": 529\\n    }\\n  },\\n  \\\"scierc_n16\\\": {\\n    \\\"seeds\\\": [\\n      42,\\n      123,\\n      456\\n    ],\\n    \\\"n_seeds\\\": 3,\\n    \\\"greedy_f1\\\": {\\n      \\\"mean\\\": 0.6440954527966648,\\n      \\\"std\\\": 0.00015021537180503046,\\n      \\\"per_seed\\\": {\\n        \\\"42\\\": 0.6441821796820129,\\n        \\\"123\\\": 0.6441821796820129,\\n        \\\"456\\\": 0.6439219990259687\\n      }\\n    },\\n    \\\"oracle_f1\\\": {\\n      \\\"mean\\\": 0.8198342597680971,\\n      \\\"std\\\": 0.002876403003560939,\\n      \\\"per_seed\\\": {\\n        \\\"42\\\": 0.8193707573669766,\\n        \\\"123\\\": 0.8172177538907217,\\n        \\\"456\\\": 0.8229142680465932\\n      }\\n    },\\n    \\\"headroom_pp\\\": {\\n      \\\"mean\\\": 17.573880697143238,\\n      \\\"std\\\": 0.3016225699668626,\\n      \\\"per_seed\\\": {\\n        \\\"42\\\": 17.518857768496375,\\n        \\\"123\\\": 17.303557420870884,\\n        \\\"456\\\": 17.89922690206245\\n      }\\n    },\\n    \\\"lp_sel_f1\\\": {\\n      \\\"mean\\\": 0.648785240888163,\\n      \\\"std\\\": 0.00695257791298551,\\n      \\\"per_seed\\\": {\\n        \\\"42\\\": 0.6465303389349577,\\n        \\\"123\\\": 0.6432399935708064,\\n        \\\"456\\\": 0.656585390158725\\n      }\\n    },\\n    \\\"lp_delta_pp\\\": {\\n      \\\"mean\\\": 0.4689788091498226,\\n      \\\"std\\\": 0.709861622068116,\\n      \\\"per_seed\\\": {\\n        \\\"42\\\": 0.2348159252944848,\\n        \\\"123\\\": -0.09421861112064445,\\n        \\\"456\\\": 1.2663391132756274\\n      }\\n    },\\n    \\\"sj_sel_f1\\\": {\\n      \\\"mean\\\": 0.6435605589002676,\\n      \\\"std\\\": 0.0023779841874772938,\\n      \\\"per_seed\\\": {\\n        \\\"42\\\": 0.646212731570788,\\n        \\\"123\\\": 0.6428503409683216,\\n        \\\"456\\\": 0.6416186041616933\\n      }\\n    },\\n    \\\"em_sel_f1\\\": {\\n      \\\"mean\\\": 0.6350290375615629,\\n      \\\"std\\\": 0.0038887249387768116,\\n      \\\"per_seed\\\": {\\n        \\\"42\\\": 0.6312245086541762,\\n        \\\"123\\\": 0.6389968168406954,\\n        \\\"456\\\": 0.6348657871898169\\n      }\\n    },\\n    \\\"sj_delta_pp\\\": {\\n      \\\"mean\\\": -0.053489389639719644,\\n      \\\"std\\\": 0.22742283077844724,\\n      \\\"per_seed\\\": {\\n        \\\"42\\\": 0.20305518887751006,\\n        \\\"123\\\": -0.13318387136912468,\\n        \\\"456\\\": -0.23033948642754432\\n      }\\n    },\\n    \\\"em_delta_pp\\\": {\\n      \\\"mean\\\": -0.9066415235101951,\\n      \\\"std\\\": 0.3886164139427325,\\n      \\\"per_seed\\\": {\\n        \\\"42\\\": -1.2957671027836626,\\n        \\\"123\\\": -0.5185362841317431,\\n        \\\"456\\\": -0.9056211836151795\\n      }\\n    },\\n    \\\"n_instances\\\": {\\n      \\\"42\\\": 529,\\n      \\\"123\\\": 529,\\n      \\\"456\\\": 529\\n    }\\n  },\\n  \\\"conll_n8\\\": {\\n    \\\"seeds\\\": [\\n      42\\n    ],\\n    \\\"n_seeds\\\": 1,\\n    \\\"greedy_f1\\\": {\\n      \\\"mean\\\": 0.9078871741063325,\\n      \\\"std\\\": 0.0,\\n      \\\"per_seed\\\": {\\n        \\\"42\\\": 0.9078871741063325\\n      }\\n    },\\n    \\\"oracle_f1\\\": {\\n      \\\"mean\\\": 0.948271330346802,\\n      \\\"std\\\": 0.0,\\n      \\\"per_seed\\\": {\\n        \\\"42\\\": 0.948271330346802\\n      }\\n    },\\n    \\\"headroom_pp\\\": {\\n      \\\"mean\\\": 4.038415624046953,\\n      \\\"std\\\": 0.0,\\n      \\\"per_seed\\\": {\\n        \\\"42\\\": 4.038415624046953\\n      }\\n    },\\n    \\\"lp_sel_f1\\\": {\\n      \\\"mean\\\": 0.8974051146077575,\\n      \\\"std\\\": 0.0,\\n      \\\"per_seed\\\": {\\n        \\\"42\\\": 0.8974051146077575\\n      }\\n    },\\n    \\\"lp_delta_pp\\\": {\\n      \\\"mean\\\": -1.0482059498574947,\\n      \\\"std\\\": 0.0,\\n      \\\"per_seed\\\": {\\n        \\\"42\\\": -1.0482059498574947\\n      }\\n    },\\n    \\\"sj_sel_f1\\\": {\\n      \\\"mean\\\": 0.8989733506696497,\\n      \\\"std\\\": 0.0,\\n      \\\"per_seed\\\": {\\n        \\\"42\\\": 0.8989733506696497\\n      }\\n    },\\n    \\\"em_sel_f1\\\": {\\n      \\\"mean\\\": 0.8971423200650341,\\n      \\\"std\\\": 0.0,\\n      \\\"per_seed\\\": {\\n        \\\"42\\\": 0.8971423200650341\\n      }\\n    },\\n    \\\"sj_delta_pp\\\": {\\n      \\\"mean\\\": -0.8913823436682788,\\n      \\\"std\\\": 0.0,\\n      \\\"per_seed\\\": {\\n        \\\"42\\\": -0.8913823436682788\\n      }\\n    },\\n    \\\"em_delta_pp\\\": {\\n      \\\"mean\\\": -1.0744854041298324,\\n      \\\"std\\\": 0.0,\\n      \\\"per_seed\\\": {\\n        \\\"42\\\": -1.0744854041298324\\n      }\\n    },\\n    \\\"n_instances\\\": {\\n      \\\"42\\\": 2756\\n    }\\n  },\\n  \\\"fewnerd_n8\\\": {\\n    \\\"seeds\\\": [\\n      42\\n    ],\\n    \\\"n_seeds\\\": 1,\\n    \\\"n_instances\\\": {\\n      \\\"42\\\": 32565\\n    },\\n    \\\"greedy_f1\\\": {\\n      \\\"mean\\\": 0.7478465965854552,\\n      \\\"std\\\": 0.0,\\n      \\\"per_seed\\\": {\\n        \\\"42\\\": 0.7478465965854552\\n      }\\n    },\\n    \\\"oracle_f1\\\": {\\n      \\\"mean\\\": 0.8718523412957434,\\n      \\\"std\\\": 0.0,\\n      \\\"per_seed\\\": {\\n        \\\"42\\\": 0.8718523412957434\\n      }\\n    },\\n    \\\"headroom_pp\\\": {\\n      \\\"mean\\\": 12.400574471028825,\\n      \\\"std\\\": 0.0,\\n      \\\"per_seed\\\": {\\n        \\\"42\\\": 12.400574471028825\\n      }\\n    },\\n    \\\"lp_sel_f1\\\": {\\n      \\\"mean\\\": 0.7613975687723666,\\n      \\\"std\\\": 0.0,\\n      \\\"per_seed\\\": {\\n        \\\"42\\\": 0.7613975687723666\\n      }\\n    },\\n    \\\"lp_delta_pp\\\": {\\n      \\\"mean\\\": 1.355097218691148,\\n      \\\"std\\\": 0.0,\\n      \\\"per_seed\\\": {\\n        \\\"42\\\": 1.355097218691148\\n      }\\n    }\\n  }\\n}\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.37}}"
    }
  },
  "sourceToolAssistantUUID": "45266182-d014-47de-88e9-8caac2417c75",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "a97de670-f9a7-4d30-affd-382982b8a334",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 94 · 2026-05-19T14:00:00.760Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_017idBE9KkSxPSRbLyc9NY1V`</summary>

```json
{
  "server": "autodl-5090",
  "command": "cat /root/autodl-tmp/struct_self_consist_ie/output/fewnerd_dals_multiseed_results.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0eea851c-99aa-4bd0-9dfa-6c9b999b951b",
  "isSidechain": false,
  "requestId": "req_011CbC3jEGeXBQpkJKgAX2Bf",
  "type": "assistant",
  "uuid": "265ece85-0b72-4eda-b4c2-819f7dfde14b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "a97de670-f9a7-4d30-affd-382982b8a334",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PPxFpcGmj4KzTAdFU7uPrK",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7198,
      "cache_read_input_tokens": 78853,
      "output_tokens": 557,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 7198,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 557,
          "cache_read_input_tokens": 78853,
          "cache_creation_input_tokens": 7198,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 7198
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

_source line 95 · 2026-05-19T14:00:01.147Z_

<details><summary>↩ Tool result · `toolu_017idBE9KkSxPSRbLyc9NY1V`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"task1_multiseed\\\": {\\n    \\\"dataset\\\": \\\"Few-NERD\\\",\\n    \\\"source\\\": \\\"exp_027_fewnerd_n16\\\",\\n    \\\"tau\\\": 0.05,\\n    \\\"n_instances_gold_filtered\\\": 4351,\\n    \\\"greedy_f1\\\": 74.9278,\\n    \\\"lp_sel_f1\\\": 76.7793,\\n    \\\"dals_f1\\\": 76.012,\\n    \\\"n_lp_selected\\\": 3498,\\n    \\\"pct_lp_selected\\\": 80.4,\\n    \\\"seeds\\\": {\\n      \\\"42\\\": {\\n        \\\"dals_gain_pp\\\": 1.0842,\\n        \\\"ci_95\\\": [\\n          0.6984,\\n          1.4709\\n        ],\\n        \\\"p_value\\\": 0.0,\\n        \\\"dals_f1\\\": 76.012\\n      },\\n      \\\"123\\\": {\\n        \\\"dals_gain_pp\\\": 1.0842,\\n        \\\"ci_95\\\": [\\n          0.7049,\\n          1.4794\\n        ],\\n        \\\"p_value\\\": 0.0,\\n        \\\"dals_f1\\\": 76.012\\n      },\\n      \\\"456\\\": {\\n        \\\"dals_gain_pp\\\": 1.0842,\\n        \\\"ci_95\\\": [\\n          0.709,\\n          1.4803\\n        ],\\n        \\\"p_value\\\": 0.0,\\n        \\\"dals_f1\\\": 76.012\\n      }\\n    },\\n    \\\"mean_gain_pp\\\": 1.0842,\\n    \\\"std_gain_pp\\\": 0.0\\n  },\\n  \\\"task2_tau_sensitivity\\\": {\\n    \\\"dataset\\\": \\\"Few-NERD\\\",\\n    \\\"source\\\": \\\"exp_027_fewnerd_n16\\\",\\n    \\\"greedy_f1\\\": 74.9278,\\n    \\\"lp_sel_f1\\\": 76.7793,\\n    \\\"results\\\": [\\n      {\\n        \\\"tau\\\": 0.01,\\n        \\\"dals_f1\\\": 76.6622,\\n        \\\"gain_vs_greedy_pp\\\": 1.7343,\\n        \\\"gain_vs_lp_pp\\\": -0.1171,\\n        \\\"pct_lp_selected\\\": 96.23,\\n        \\\"n_lp_selected\\\": 4187,\\n        \\\"n_total\\\": 4351\\n      },\\n      {\\n        \\\"tau\\\": 0.03,\\n        \\\"dals_f1\\\": 76.2194,\\n        \\\"gain_vs_greedy_pp\\\": 1.2916,\\n        \\\"gain_vs_lp_pp\\\": -0.5599,\\n        \\\"pct_lp_selected\\\": 91.4,\\n        \\\"n_lp_selected\\\": 3977,\\n        \\\"n_total\\\": 4351\\n      },\\n      {\\n        \\\"tau\\\": 0.05,\\n        \\\"dals_f1\\\": 76.012,\\n        \\\"gain_vs_greedy_pp\\\": 1.0842,\\n        \\\"gain_vs_lp_pp\\\": -0.7672,\\n        \\\"pct_lp_selected\\\": 80.4,\\n        \\\"n_lp_selected\\\": 3498,\\n        \\\"n_total\\\": 4351\\n      },\\n      {\\n        \\\"tau\\\": 0.1,\\n        \\\"dals_f1\\\": 75.496,\\n        \\\"gain_vs_greedy_pp\\\": 0.5682,\\n        \\\"gain_vs_lp_pp\\\": -1.2832,\\n        \\\"pct_lp_selected\\\": 50.31,\\n        \\\"n_lp_selected\\\": 2189,\\n        \\\"n_total\\\": 4351\\n      },\\n      {\\n        \\\"tau\\\": 0.15,\\n        \\\"dals_f1\\\": 75.0103,\\n        \\\"gain_vs_greedy_pp\\\": 0.0825,\\n        \\\"gain_vs_lp_pp\\\": -1.769,\\n        \\\"pct_lp_selected\\\": 31.97,\\n        \\\"n_lp_selected\\\": 1391,\\n        \\\"n_total\\\": 4351\\n      },\\n      {\\n        \\\"tau\\\": 0.2,\\n        \\\"dals_f1\\\": 74.9199,\\n        \\\"gain_vs_greedy_pp\\\": -0.0079,\\n        \\\"gain_vs_lp_pp\\\": -1.8594,\\n        \\\"pct_lp_selected\\\": 18.27,\\n        \\\"n_lp_selected\\\": 795,\\n        \\\"n_total\\\": 4351\\n      }\\n    ]\\n  }\\n}\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.38}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "265ece85-0b72-4eda-b4c2-819f7dfde14b",
  "isSidechain": false,
  "promptId": "0731b9be-f5e6-4a8a-9a3c-2edafe06629b",
  "type": "user",
  "uuid": "8b368690-ed0d-4ec2-a27f-c5eca5a2bd4b",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"{\\\\n  \\\\\\\"task1_multiseed\\\\\\\": {\\\\n    \\\\\\\"dataset\\\\\\\": \\\\\\\"Few-NERD\\\\\\\",\\\\n    \\\\\\\"source\\\\\\\": \\\\\\\"exp_027_fewnerd_n16\\\\\\\",\\\\n    \\\\\\\"tau\\\\\\\": 0.05,\\\\n    \\\\\\\"n_instances_gold_filtered\\\\\\\": 4351,\\\\n    \\\\\\\"greedy_f1\\\\\\\": 74.9278,\\\\n    \\\\\\\"lp_sel_f1\\\\\\\": 76.7793,\\\\n    \\\\\\\"dals_f1\\\\\\\": 76.012,\\\\n    \\\\\\\"n_lp_selected\\\\\\\": 3498,\\\\n    \\\\\\\"pct_lp_selected\\\\\\\": 80.4,\\\\n    \\\\\\\"seeds\\\\\\\": {\\\\n      \\\\\\\"42\\\\\\\": {\\\\n        \\\\\\\"dals_gain_pp\\\\\\\": 1.0842,\\\\n        \\\\\\\"ci_95\\\\\\\": [\\\\n          0.6984,\\\\n          1.4709\\\\n        ],\\\\n        \\\\\\\"p_value\\\\\\\": 0.0,\\\\n        \\\\\\\"dals_f1\\\\\\\": 76.012\\\\n      },\\\\n      \\\\\\\"123\\\\\\\": {\\\\n        \\\\\\\"dals_gain_pp\\\\\\\": 1.0842,\\\\n        \\\\\\\"ci_95\\\\\\\": [\\\\n          0.7049,\\\\n          1.4794\\\\n        ],\\\\n        \\\\\\\"p_value\\\\\\\": 0.0,\\\\n        \\\\\\\"dals_f1\\\\\\\": 76.012\\\\n      },\\\\n      \\\\\\\"456\\\\\\\": {\\\\n        \\\\\\\"dals_gain_pp\\\\\\\": 1.0842,\\\\n        \\\\\\\"ci_95\\\\\\\": [\\\\n          0.709,\\\\n          1.4803\\\\n        ],\\\\n        \\\\\\\"p_value\\\\\\\": 0.0,\\\\n        \\\\\\\"dals_f1\\\\\\\": 76.012\\\\n      }\\\\n    },\\\\n    \\\\\\\"mean_gain_pp\\\\\\\": 1.0842,\\\\n    \\\\\\\"std_gain_pp\\\\\\\": 0.0\\\\n  },\\\\n  \\\\\\\"task2_tau_sensitivity\\\\\\\": {\\\\n    \\\\\\\"dataset\\\\\\\": \\\\\\\"Few-NERD\\\\\\\",\\\\n    \\\\\\\"source\\\\\\\": \\\\\\\"exp_027_fewnerd_n16\\\\\\\",\\\\n    \\\\\\\"greedy_f1\\\\\\\": 74.9278,\\\\n    \\\\\\\"lp_sel_f1\\\\\\\": 76.7793,\\\\n    \\\\\\\"results\\\\\\\": [\\\\n      {\\\\n        \\\\\\\"tau\\\\\\\": 0.01,\\\\n        \\\\\\\"dals_f1\\\\\\\": 76.6622,\\\\n        \\\\\\\"gain_vs_greedy_pp\\\\\\\": 1.7343,\\\\n        \\\\\\\"gain_vs_lp_pp\\\\\\\": -0.1171,\\\\n        \\\\\\\"pct_lp_selected\\\\\\\": 96.23,\\\\n        \\\\\\\"n_lp_selected\\\\\\\": 4187,\\\\n        \\\\\\\"n_total\\\\\\\": 4351\\\\n      },\\\\n      {\\\\n        \\\\\\\"tau\\\\\\\": 0.03,\\\\n        \\\\\\\"dals_f1\\\\\\\": 76.2194,\\\\n        \\\\\\\"gain_vs_greedy_pp\\\\\\\": 1.2916,\\\\n        \\\\\\\"gain_vs_lp_pp\\\\\\\": -0.5599,\\\\n        \\\\\\\"pct_lp_selected\\\\\\\": 91.4,\\\\n        \\\\\\\"n_lp_selected\\\\\\\": 3977,\\\\n        \\\\\\\"n_total\\\\\\\": 4351\\\\n      },\\\\n      {\\\\n        \\\\\\\"tau\\\\\\\": 0.05,\\\\n        \\\\\\\"dals_f1\\\\\\\": 76.012,\\\\n        \\\\\\\"gain_vs_greedy_pp\\\\\\\": 1.0842,\\\\n        \\\\\\\"gain_vs_lp_pp\\\\\\\": -0.7672,\\\\n        \\\\\\\"pct_lp_selected\\\\\\\": 80.4,\\\\n        \\\\\\\"n_lp_selected\\\\\\\": 3498,\\\\n        \\\\\\\"n_total\\\\\\\": 4351\\\\n      },\\\\n      {\\\\n        \\\\\\\"tau\\\\\\\": 0.1,\\\\n        \\\\\\\"dals_f1\\\\\\\": 75.496,\\\\n        \\\\\\\"gain_vs_greedy_pp\\\\\\\": 0.5682,\\\\n        \\\\\\\"gain_vs_lp_pp\\\\\\\": -1.2832,\\\\n        \\\\\\\"pct_lp_selected\\\\\\\": 50.31,\\\\n        \\\\\\\"n_lp_selected\\\\\\\": 2189,\\\\n        \\\\\\\"n_total\\\\\\\": 4351\\\\n      },\\\\n      {\\\\n        \\\\\\\"tau\\\\\\\": 0.15,\\\\n        \\\\\\\"dals_f1\\\\\\\": 75.0103,\\\\n        \\\\\\\"gain_vs_greedy_pp\\\\\\\": 0.0825,\\\\n        \\\\\\\"gain_vs_lp_pp\\\\\\\": -1.769,\\\\n        \\\\\\\"pct_lp_selected\\\\\\\": 31.97,\\\\n        \\\\\\\"n_lp_selected\\\\\\\": 1391,\\\\n        \\\\\\\"n_total\\\\\\\": 4351\\\\n      },\\\\n      {\\\\n        \\\\\\\"tau\\\\\\\": 0.2,\\\\n        \\\\\\\"dals_f1\\\\\\\": 74.9199,\\\\n        \\\\\\\"gain_vs_greedy_pp\\\\\\\": -0.0079,\\\\n        \\\\\\\"gain_vs_lp_pp\\\\\\\": -1.8594,\\\\n        \\\\\\\"pct_lp_selected\\\\\\\": 18.27,\\\\n        \\\\\\\"n_lp_selected\\\\\\\": 795,\\\\n        \\\\\\\"n_total\\\\\\\": 4351\\\\n      }\\\\n    ]\\\\n  }\\\\n}\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.38}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"task1_multiseed\\\": {\\n    \\\"dataset\\\": \\\"Few-NERD\\\",\\n    \\\"source\\\": \\\"exp_027_fewnerd_n16\\\",\\n    \\\"tau\\\": 0.05,\\n    \\\"n_instances_gold_filtered\\\": 4351,\\n    \\\"greedy_f1\\\": 74.9278,\\n    \\\"lp_sel_f1\\\": 76.7793,\\n    \\\"dals_f1\\\": 76.012,\\n    \\\"n_lp_selected\\\": 3498,\\n    \\\"pct_lp_selected\\\": 80.4,\\n    \\\"seeds\\\": {\\n      \\\"42\\\": {\\n        \\\"dals_gain_pp\\\": 1.0842,\\n        \\\"ci_95\\\": [\\n          0.6984,\\n          1.4709\\n        ],\\n        \\\"p_value\\\": 0.0,\\n        \\\"dals_f1\\\": 76.012\\n      },\\n      \\\"123\\\": {\\n        \\\"dals_gain_pp\\\": 1.0842,\\n        \\\"ci_95\\\": [\\n          0.7049,\\n          1.4794\\n        ],\\n        \\\"p_value\\\": 0.0,\\n        \\\"dals_f1\\\": 76.012\\n      },\\n      \\\"456\\\": {\\n        \\\"dals_gain_pp\\\": 1.0842,\\n        \\\"ci_95\\\": [\\n          0.709,\\n          1.4803\\n        ],\\n        \\\"p_value\\\": 0.0,\\n        \\\"dals_f1\\\": 76.012\\n      }\\n    },\\n    \\\"mean_gain_pp\\\": 1.0842,\\n    \\\"std_gain_pp\\\": 0.0\\n  },\\n  \\\"task2_tau_sensitivity\\\": {\\n    \\\"dataset\\\": \\\"Few-NERD\\\",\\n    \\\"source\\\": \\\"exp_027_fewnerd_n16\\\",\\n    \\\"greedy_f1\\\": 74.9278,\\n    \\\"lp_sel_f1\\\": 76.7793,\\n    \\\"results\\\": [\\n      {\\n        \\\"tau\\\": 0.01,\\n        \\\"dals_f1\\\": 76.6622,\\n        \\\"gain_vs_greedy_pp\\\": 1.7343,\\n        \\\"gain_vs_lp_pp\\\": -0.1171,\\n        \\\"pct_lp_selected\\\": 96.23,\\n        \\\"n_lp_selected\\\": 4187,\\n        \\\"n_total\\\": 4351\\n      },\\n      {\\n        \\\"tau\\\": 0.03,\\n        \\\"dals_f1\\\": 76.2194,\\n        \\\"gain_vs_greedy_pp\\\": 1.2916,\\n        \\\"gain_vs_lp_pp\\\": -0.5599,\\n        \\\"pct_lp_selected\\\": 91.4,\\n        \\\"n_lp_selected\\\": 3977,\\n        \\\"n_total\\\": 4351\\n      },\\n      {\\n        \\\"tau\\\": 0.05,\\n        \\\"dals_f1\\\": 76.012,\\n        \\\"gain_vs_greedy_pp\\\": 1.0842,\\n        \\\"gain_vs_lp_pp\\\": -0.7672,\\n        \\\"pct_lp_selected\\\": 80.4,\\n        \\\"n_lp_selected\\\": 3498,\\n        \\\"n_total\\\": 4351\\n      },\\n      {\\n        \\\"tau\\\": 0.1,\\n        \\\"dals_f1\\\": 75.496,\\n        \\\"gain_vs_greedy_pp\\\": 0.5682,\\n        \\\"gain_vs_lp_pp\\\": -1.2832,\\n        \\\"pct_lp_selected\\\": 50.31,\\n        \\\"n_lp_selected\\\": 2189,\\n        \\\"n_total\\\": 4351\\n      },\\n      {\\n        \\\"tau\\\": 0.15,\\n        \\\"dals_f1\\\": 75.0103,\\n        \\\"gain_vs_greedy_pp\\\": 0.0825,\\n        \\\"gain_vs_lp_pp\\\": -1.769,\\n        \\\"pct_lp_selected\\\": 31.97,\\n        \\\"n_lp_selected\\\": 1391,\\n        \\\"n_total\\\": 4351\\n      },\\n      {\\n        \\\"tau\\\": 0.2,\\n        \\\"dals_f1\\\": 74.9199,\\n        \\\"gain_vs_greedy_pp\\\": -0.0079,\\n        \\\"gain_vs_lp_pp\\\": -1.8594,\\n        \\\"pct_lp_selected\\\": 18.27,\\n        \\\"n_lp_selected\\\": 795,\\n        \\\"n_total\\\": 4351\\n      }\\n    ]\\n  }\\n}\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.38}}"
    }
  },
  "sourceToolAssistantUUID": "265ece85-0b72-4eda-b4c2-819f7dfde14b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "a97de670-f9a7-4d30-affd-382982b8a334",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 96 · 2026-05-19T14:00:01.444Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01XuVPV9TXCResVCsoX8C2LU`</summary>

```json
{
  "server": "autodl-5090",
  "command": "cat /root/autodl-tmp/struct_self_consist_ie/output/dals_analysis.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8b368690-ed0d-4ec2-a27f-c5eca5a2bd4b",
  "isSidechain": false,
  "requestId": "req_011CbC3jEGeXBQpkJKgAX2Bf",
  "type": "assistant",
  "uuid": "6017bf7e-4dda-4465-8356-f413fab12a3a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "a97de670-f9a7-4d30-affd-382982b8a334",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PPxFpcGmj4KzTAdFU7uPrK",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7198,
      "cache_read_input_tokens": 78853,
      "output_tokens": 557,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 7198,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 557,
          "cache_read_input_tokens": 78853,
          "cache_creation_input_tokens": 7198,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 7198
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

_source line 97 · 2026-05-19T14:00:01.852Z_

<details><summary>↩ Tool result · `toolu_01XuVPV9TXCResVCsoX8C2LU`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"scierc\\\": {\\n    \\\"dataset\\\": \\\"scierc\\\",\\n    \\\"n_instances\\\": 529,\\n    \\\"lp_range_stats\\\": {\\n      \\\"mean\\\": 0.06218863264816551,\\n      \\\"median\\\": 0.040121078648161536,\\n      \\\"std\\\": 0.06908752812874064,\\n      \\\"P10\\\": 0.01858445776923011,\\n      \\\"P25\\\": 0.026459537324479056,\\n      \\\"P50\\\": 0.040121078648161536,\\n      \\\"P75\\\": 0.068535793140826,\\n      \\\"P90\\\": 0.12211430813918056,\\n      \\\"zero_pct\\\": 0.0,\\n      \\\"n_instances\\\": 529\\n    },\\n    \\\"lp_range_sweep\\\": {\\n      \\\"proxy\\\": \\\"lp_range\\\",\\n      \\\"sweep\\\": [\\n        {\\n          \\\"threshold\\\": 0.001,\\n          \\\"gated_pct\\\": 99.62,\\n          \\\"gated_lp_delta_pp\\\": 0.639,\\n          \\\"overall_dals_f1\\\": 65.0481,\\n          \\\"overall_greedy_f1\\\": 64.4115,\\n          \\\"overall_lp_f1\\\": 65.0481,\\n          \\\"dals_delta_vs_greedy_pp\\\": 0.6366,\\n          \\\"dals_delta_vs_lp_pp\\\": 0.0\\n        },\\n        {\\n          \\\"threshold\\\": 0.005,\\n          \\\"gated_pct\\\": 99.43,\\n          \\\"gated_lp_delta_pp\\\": 0.6403,\\n          \\\"overall_dals_f1\\\": 65.0481,\\n          \\\"overall_greedy_f1\\\": 64.4115,\\n          \\\"overall_lp_f1\\\": 65.0481,\\n          \\\"dals_delta_vs_greedy_pp\\\": 0.6366,\\n          \\\"dals_delta_vs_lp_pp\\\": 0.0\\n        },\\n        {\\n          \\\"threshold\\\": 0.01,\\n          \\\"gated_pct\\\": 98.87,\\n          \\\"gated_lp_delta_pp\\\": 0.6025,\\n          \\\"overall_dals_f1\\\": 65.0072,\\n          \\\"overall_greedy_f1\\\": 64.4115,\\n          \\\"overall_lp_f1\\\": 65.0481,\\n          \\\"dals_delta_vs_greedy_pp\\\": 0.5957,\\n          \\\"dals_delta_vs_lp_pp\\\": -0.041\\n        },\\n        {\\n          \\\"threshold\\\": 0.02,\\n          \\\"gated_pct\\\": 86.39,\\n          \\\"gated_lp_delta_pp\\\": 0.8595,\\n          \\\"overall_dals_f1\\\": 65.154,\\n          \\\"overall_greedy_f1\\\": 64.4115,\\n          \\\"overall_lp_f1\\\": 65.0481,\\n          \\\"dals_delta_vs_greedy_pp\\\": 0.7425,\\n          \\\"dals_delta_vs_lp_pp\\\": 0.1059\\n        },\\n        {\\n          \\\"threshold\\\": 0.03,\\n          \\\"gated_pct\\\": 68.24,\\n          \\\"gated_lp_delta_pp\\\": 1.2756,\\n          \\\"overall_dals_f1\\\": 65.282,\\n          \\\"overall_greedy_f1\\\": 64.4115,\\n          \\\"overall_lp_f1\\\": 65.0481,\\n          \\\"dals_delta_vs_greedy_pp\\\": 0.8705,\\n          \\\"dals_delta_vs_lp_pp\\\": 0.2339\\n        },\\n        {\\n          \\\"threshold\\\": 0.04,\\n          \\\"gated_pct\\\": 50.09,\\n          \\\"gated_lp_delta_pp\\\": 1.8618,\\n          \\\"overall_dals_f1\\\": 65.3441,\\n          \\\"overall_greedy_f1\\\": 64.4115,\\n          \\\"overall_lp_f1\\\": 65.0481,\\n          \\\"dals_delta_vs_greedy_pp\\\": 0.9326,\\n          \\\"dals_delta_vs_lp_pp\\\": 0.296\\n        },\\n        {\\n          \\\"threshold\\\": 0.05,\\n          \\\"gated_pct\\\": 39.7,\\n          \\\"gated_lp_delta_pp\\\": 2.8761,\\n          \\\"overall_dals_f1\\\": 65.5532,\\n          \\\"overall_greedy_f1\\\": 64.4115,\\n          \\\"overall_lp_f1\\\": 65.0481,\\n          \\\"dals_delta_vs_greedy_pp\\\": 1.1417,\\n          \\\"dals_delta_vs_lp_pp\\\": 0.5051\\n        },\\n        {\\n          \\\"threshold\\\": 0.07,\\n          \\\"gated_pct\\\": 23.63,\\n          \\\"gated_lp_delta_pp\\\": 3.2859,\\n          \\\"overall_dals_f1\\\": 65.1879,\\n          \\\"overall_greedy_f1\\\": 64.4115,\\n          \\\"overall_lp_f1\\\": 65.0481,\\n          \\\"dals_delta_vs_greedy_pp\\\": 0.7764,\\n          \\\"dals_delta_vs_lp_pp\\\": 0.1398\\n        },\\n        {\\n          \\\"threshold\\\": 0.1,\\n          \\\"gated_pct\\\": 16.07,\\n          \\\"gated_lp_delta_pp\\\": 3.6863,\\n          \\\"overall_dals_f1\\\": 65.0038,\\n          \\\"overall_greedy_f1\\\": 64.4115,\\n          \\\"overall_lp_f1\\\": 65.0481,\\n          \\\"dals_delta_vs_greedy_pp\\\": 0.5923,\\n          \\\"dals_delta_vs_lp_pp\\\": -0.0443\\n        }\\n      ],\\n      \\\"best_threshold\\\": 0.05,\\n      \\\"best_dals_f1\\\": 65.5532,\\n      \\\"best_dals_delta_vs_greedy_pp\\\": 1.1417,\\n      \\\"best_dals_delta_vs_lp_pp\\\": 0.5051,\\n      \\\"overall_greedy_f1\\\": 64.4115,\\n      \\\"overall_lp_f1\\\": 65.0481\\n    },\\n    \\\"sj_diversity_sweep\\\": {\\n      \\\"proxy\\\": \\\"sj_diversity\\\",\\n      \\\"sweep\\\": [\\n        {\\n          \\\"threshold\\\": 0.001,\\n          \\\"gated_pct\\\": 88.66,\\n          \\\"gated_lp_delta_pp\\\": 0.7181,\\n          \\\"overall_dals_f1\\\": 65.0481,\\n          \\\"overall_greedy_f1\\\": 64.4115,\\n          \\\"overall_lp_f1\\\": 65.0481,\\n          \\\"dals_delta_vs_greedy_pp\\\": 0.6366,\\n          \\\"dals_delta_vs_lp_pp\\\": 0.0\\n        },\\n        {\\n          \\\"threshold\\\": 0.\\n\\n... [截断: 输出过长，省略 23273 字符] ...\\n\\n47,\\n          \\\"dals_delta_vs_greedy_pp\\\": -0.7978,\\n          \\\"dals_delta_vs_lp_pp\\\": 0.268\\n        }\\n      ],\\n      \\\"best_threshold\\\": 0.3,\\n      \\\"best_dals_f1\\\": 90.0828,\\n      \\\"best_dals_delta_vs_greedy_pp\\\": -0.7978,\\n      \\\"best_dals_delta_vs_lp_pp\\\": 0.268,\\n      \\\"overall_greedy_f1\\\": 90.8806,\\n      \\\"overall_lp_f1\\\": 89.8147\\n    },\\n    \\\"em_diversity_sweep\\\": {\\n      \\\"proxy\\\": \\\"em_diversity\\\",\\n      \\\"sweep\\\": [\\n        {\\n          \\\"threshold\\\": 0.001,\\n          \\\"gated_pct\\\": 43.07,\\n          \\\"gated_lp_delta_pp\\\": -2.4747,\\n          \\\"overall_dals_f1\\\": 89.8147,\\n          \\\"overall_greedy_f1\\\": 90.8806,\\n          \\\"overall_lp_f1\\\": 89.8147,\\n          \\\"dals_delta_vs_greedy_pp\\\": -1.0658,\\n          \\\"dals_delta_vs_lp_pp\\\": 0.0\\n        },\\n        {\\n          \\\"threshold\\\": 0.01,\\n          \\\"gated_pct\\\": 43.07,\\n          \\\"gated_lp_delta_pp\\\": -2.4747,\\n          \\\"overall_dals_f1\\\": 89.8147,\\n          \\\"overall_greedy_f1\\\": 90.8806,\\n          \\\"overall_lp_f1\\\": 89.8147,\\n          \\\"dals_delta_vs_greedy_pp\\\": -1.0658,\\n          \\\"dals_delta_vs_lp_pp\\\": 0.0\\n        },\\n        {\\n          \\\"threshold\\\": 0.05,\\n          \\\"gated_pct\\\": 43.07,\\n          \\\"gated_lp_delta_pp\\\": -2.4747,\\n          \\\"overall_dals_f1\\\": 89.8147,\\n          \\\"overall_greedy_f1\\\": 90.8806,\\n          \\\"overall_lp_f1\\\": 89.8147,\\n          \\\"dals_delta_vs_greedy_pp\\\": -1.0658,\\n          \\\"dals_delta_vs_lp_pp\\\": 0.0\\n        },\\n        {\\n          \\\"threshold\\\": 0.1,\\n          \\\"gated_pct\\\": 43.07,\\n          \\\"gated_lp_delta_pp\\\": -2.4747,\\n          \\\"overall_dals_f1\\\": 89.8147,\\n          \\\"overall_greedy_f1\\\": 90.8806,\\n          \\\"overall_lp_f1\\\": 89.8147,\\n          \\\"dals_delta_vs_greedy_pp\\\": -1.0658,\\n          \\\"dals_delta_vs_lp_pp\\\": 0.0\\n        },\\n        {\\n          \\\"threshold\\\": 0.15,\\n          \\\"gated_pct\\\": 43.07,\\n          \\\"gated_lp_delta_pp\\\": -2.4747,\\n          \\\"overall_dals_f1\\\": 89.8147,\\n          \\\"overall_greedy_f1\\\": 90.8806,\\n          \\\"overall_lp_f1\\\": 89.8147,\\n          \\\"dals_delta_vs_greedy_pp\\\": -1.0658,\\n          \\\"dals_delta_vs_lp_pp\\\": 0.0\\n        },\\n        {\\n          \\\"threshold\\\": 0.2,\\n          \\\"gated_pct\\\": 43.07,\\n          \\\"gated_lp_delta_pp\\\": -2.4747,\\n          \\\"overall_dals_f1\\\": 89.8147,\\n          \\\"overall_greedy_f1\\\": 90.8806,\\n          \\\"overall_lp_f1\\\": 89.8147,\\n          \\\"dals_delta_vs_greedy_pp\\\": -1.0658,\\n          \\\"dals_delta_vs_lp_pp\\\": 0.0\\n        },\\n        {\\n          \\\"threshold\\\": 0.3,\\n          \\\"gated_pct\\\": 27.07,\\n          \\\"gated_lp_delta_pp\\\": -3.6655,\\n          \\\"overall_dals_f1\\\": 89.8884,\\n          \\\"overall_greedy_f1\\\": 90.8806,\\n          \\\"overall_lp_f1\\\": 89.8147,\\n          \\\"dals_delta_vs_greedy_pp\\\": -0.9922,\\n          \\\"dals_delta_vs_lp_pp\\\": 0.0737\\n        },\\n        {\\n          \\\"threshold\\\": 0.5,\\n          \\\"gated_pct\\\": 18.9,\\n          \\\"gated_lp_delta_pp\\\": -4.382,\\n          \\\"overall_dals_f1\\\": 90.0522,\\n          \\\"overall_greedy_f1\\\": 90.8806,\\n          \\\"overall_lp_f1\\\": 89.8147,\\n          \\\"dals_delta_vs_greedy_pp\\\": -0.8284,\\n          \\\"dals_delta_vs_lp_pp\\\": 0.2375\\n        },\\n        {\\n          \\\"threshold\\\": 0.7,\\n          \\\"gated_pct\\\": 9.87,\\n          \\\"gated_lp_delta_pp\\\": -4.1469,\\n          \\\"overall_dals_f1\\\": 90.4713,\\n          \\\"overall_greedy_f1\\\": 90.8806,\\n          \\\"overall_lp_f1\\\": 89.8147,\\n          \\\"dals_delta_vs_greedy_pp\\\": -0.4093,\\n          \\\"dals_delta_vs_lp_pp\\\": 0.6566\\n        }\\n      ],\\n      \\\"best_threshold\\\": 0.7,\\n      \\\"best_dals_f1\\\": 90.4713,\\n      \\\"best_dals_delta_vs_greedy_pp\\\": -0.4093,\\n      \\\"best_dals_delta_vs_lp_pp\\\": 0.6566,\\n      \\\"overall_greedy_f1\\\": 90.8806,\\n      \\\"overall_lp_f1\\\": 89.8147\\n    },\\n    \\\"oracle\\\": {\\n      \\\"oracle_f1\\\": 91.3907,\\n      \\\"lp_better_count\\\": 43,\\n      \\\"greedy_better_count\\\": 117,\\n      \\\"tied_count\\\": 2596,\\n      \\\"n\\\": 2756\\n    },\\n    \\\"baseline_comparison\\\": {\\n      \\\"pure_greedy_f1\\\": 90.8806,\\n      \\\"pure_lp_f1\\\": 89.8147,\\n      \\\"dals_best_lp_range_f1\\\": 90.5737,\\n      \\\"dals_best_lp_range_tau\\\": 0.1,\\n      \\\"dals_best_sj_div_f1\\\": 90.0828,\\n      \\\"dals_best_sj_div_tau\\\": 0.3,\\n      \\\"dals_best_em_div_f1\\\": 90.4713,\\n      \\\"dals_best_em_div_tau\\\": 0.7,\\n      \\\"oracle_f1\\\": 91.3907\\n    }\\n  }\\n}\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.4}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6017bf7e-4dda-4465-8356-f413fab12a3a",
  "isSidechain": false,
  "promptId": "0731b9be-f5e6-4a8a-9a3c-2edafe06629b",
  "type": "user",
  "uuid": "8483e788-b82a-40e8-9b5a-94fea0d0cedd",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"{\\\\n  \\\\\\\"scierc\\\\\\\": {\\\\n    \\\\\\\"dataset\\\\\\\": \\\\\\\"scierc\\\\\\\",\\\\n    \\\\\\\"n_instances\\\\\\\": 529,\\\\n    \\\\\\\"lp_range_stats\\\\\\\": {\\\\n      \\\\\\\"mean\\\\\\\": 0.06218863264816551,\\\\n      \\\\\\\"median\\\\\\\": 0.040121078648161536,\\\\n      \\\\\\\"std\\\\\\\": 0.06908752812874064,\\\\n      \\\\\\\"P10\\\\\\\": 0.01858445776923011,\\\\n      \\\\\\\"P25\\\\\\\": 0.026459537324479056,\\\\n      \\\\\\\"P50\\\\\\\": 0.040121078648161536,\\\\n      \\\\\\\"P75\\\\\\\": 0.068535793140826,\\\\n      \\\\\\\"P90\\\\\\\": 0.12211430813918056,\\\\n      \\\\\\\"zero_pct\\\\\\\": 0.0,\\\\n      \\\\\\\"n_instances\\\\\\\": 529\\\\n    },\\\\n    \\\\\\\"lp_range_sweep\\\\\\\": {\\\\n      \\\\\\\"proxy\\\\\\\": \\\\\\\"lp_range\\\\\\\",\\\\n      \\\\\\\"sweep\\\\\\\": [\\\\n        {\\\\n          \\\\\\\"threshold\\\\\\\": 0.001,\\\\n          \\\\\\\"gated_pct\\\\\\\": 99.62,\\\\n          \\\\\\\"gated_lp_delta_pp\\\\\\\": 0.639,\\\\n          \\\\\\\"overall_dals_f1\\\\\\\": 65.0481,\\\\n          \\\\\\\"overall_greedy_f1\\\\\\\": 64.4115,\\\\n          \\\\\\\"overall_lp_f1\\\\\\\": 65.0481,\\\\n          \\\\\\\"dals_delta_vs_greedy_pp\\\\\\\": 0.6366,\\\\n          \\\\\\\"dals_delta_vs_lp_pp\\\\\\\": 0.0\\\\n        },\\\\n        {\\\\n          \\\\\\\"threshold\\\\\\\": 0.005,\\\\n          \\\\\\\"gated_pct\\\\\\\": 99.43,\\\\n          \\\\\\\"gated_lp_delta_pp\\\\\\\": 0.6403,\\\\n          \\\\\\\"overall_dals_f1\\\\\\\": 65.0481,\\\\n          \\\\\\\"overall_greedy_f1\\\\\\\": 64.4115,\\\\n          \\\\\\\"overall_lp_f1\\\\\\\": 65.0481,\\\\n          \\\\\\\"dals_delta_vs_greedy_pp\\\\\\\": 0.6366,\\\\n          \\\\\\\"dals_delta_vs_lp_pp\\\\\\\": 0.0\\\\n        },\\\\n        {\\\\n          \\\\\\\"threshold\\\\\\\": 0.01,\\\\n          \\\\\\\"gated_pct\\\\\\\": 98.87,\\\\n          \\\\\\\"gated_lp_delta_pp\\\\\\\": 0.6025,\\\\n          \\\\\\\"overall_dals_f1\\\\\\\": 65.0072,\\\\n          \\\\\\\"overall_greedy_f1\\\\\\\": 64.4115,\\\\n          \\\\\\\"overall_lp_f1\\\\\\\": 65.0481,\\\\n          \\\\\\\"dals_delta_vs_greedy_pp\\\\\\\": 0.5957,\\\\n          \\\\\\\"dals_delta_vs_lp_pp\\\\\\\": -0.041\\\\n        },\\\\n        {\\\\n          \\\\\\\"threshold\\\\\\\": 0.02,\\\\n          \\\\\\\"gated_pct\\\\\\\": 86.39,\\\\n          \\\\\\\"gated_lp_delta_pp\\\\\\\": 0.8595,\\\\n          \\\\\\\"overall_dals_f1\\\\\\\": 65.154,\\\\n          \\\\\\\"overall_greedy_f1\\\\\\\": 64.4115,\\\\n          \\\\\\\"overall_lp_f1\\\\\\\": 65.0481,\\\\n          \\\\\\\"dals_delta_vs_greedy_pp\\\\\\\": 0.7425,\\\\n          \\\\\\\"dals_delta_vs_lp_pp\\\\\\\": 0.1059\\\\n        },\\\\n        {\\\\n          \\\\\\\"threshold\\\\\\\": 0.03,\\\\n          \\\\\\\"gated_pct\\\\\\\": 68.24,\\\\n          \\\\\\\"gated_lp_delta_pp\\\\\\\": 1.2756,\\\\n          \\\\\\\"overall_dals_f1\\\\\\\": 65.282,\\\\n          \\\\\\\"overall_greedy_f1\\\\\\\": 64.4115,\\\\n          \\\\\\\"overall_lp_f1\\\\\\\": 65.0481,\\\\n          \\\\\\\"dals_delta_vs_greedy_pp\\\\\\\": 0.8705,\\\\n          \\\\\\\"dals_delta_vs_lp_pp\\\\\\\": 0.2339\\\\n        },\\\\n        {\\\\n          \\\\\\\"threshold\\\\\\\": 0.04,\\\\n          \\\\\\\"gated_pct\\\\\\\": 50.09,\\\\n          \\\\\\\"gated_lp_delta_pp\\\\\\\": 1.8618,\\\\n          \\\\\\\"overall_dals_f1\\\\\\\": 65.3441,\\\\n          \\\\\\\"overall_greedy_f1\\\\\\\": 64.4115,\\\\n          \\\\\\\"overall_lp_f1\\\\\\\": 65.0481,\\\\n          \\\\\\\"dals_delta_vs_greedy_pp\\\\\\\": 0.9326,\\\\n          \\\\\\\"dals_delta_vs_lp_pp\\\\\\\": 0.296\\\\n        },\\\\n        {\\\\n          \\\\\\\"threshold\\\\\\\": 0.05,\\\\n          \\\\\\\"gated_pct\\\\\\\": 39.7,\\\\n          \\\\\\\"gated_lp_delta_pp\\\\\\\": 2.8761,\\\\n          \\\\\\\"overall_dals_f1\\\\\\\": 65.5532,\\\\n          \\\\\\\"overall_greedy_f1\\\\\\\": 64.4115,\\\\n          \\\\\\\"overall_lp_f1\\\\\\\": 65.0481,\\\\n          \\\\\\\"dals_delta_vs_greedy_pp\\\\\\\": 1.1417,\\\\n          \\\\\\\"dals_delta_vs_lp_pp\\\\\\\": 0.5051\\\\n        },\\\\n        {\\\\n          \\\\\\\"threshold\\\\\\\": 0.07,\\\\n          \\\\\\\"gated_pct\\\\\\\": 23.63,\\\\n          \\\\\\\"gated_lp_delta_pp\\\\\\\": 3.2859,\\\\n          \\\\\\\"overall_dals_f1\\\\\\\": 65.1879,\\\\n          \\\\\\\"overall_greedy_f1\\\\\\\": 64.4115,\\\\n          \\\\\\\"overall_lp_f1\\\\\\\": 65.0481,\\\\n          \\\\\\\"dals_delta_vs_greedy_pp\\\\\\\": 0.7764,\\\\n          \\\\\\\"dals_delta_vs_lp_pp\\\\\\\": 0.1398\\\\n        },\\\\n        {\\\\n          \\\\\\\"threshold\\\\\\\": 0.1,\\\\n          \\\\\\\"gated_pct\\\\\\\": 16.07,\\\\n          \\\\\\\"gated_lp_delta_pp\\\\\\\": 3.6863,\\\\n          \\\\\\\"overall_dals_f1\\\\\\\": 65.0038,\\\\n          \\\\\\\"overall_greedy_f1\\\\\\\": 64.4115,\\\\n          \\\\\\\"overall_lp_f1\\\\\\\": 65.0481,\\\\n          \\\\\\\"dals_delta_vs_greedy_pp\\\\\\\": 0.5923,\\\\n          \\\\\\\"dals_delta_vs_lp_pp\\\\\\\": -0.0443\\\\n        }\\\\n      ],\\\\n      \\\\\\\"best_threshold\\\\\\\": 0.05,\\\\n      \\\\\\\"best_dals_f1\\\\\\\": 65.5532,\\\\n      \\\\\\\"best_dals_delta_vs_greedy_pp\\\\\\\": 1.1417,\\\\n      \\\\\\\"best_dals_delta_vs_lp_pp\\\\\\\": 0.5051,\\\\n      \\\\\\\"overall_greedy_f1\\\\\\\": 64.4115,\\\\n      \\\\\\\"overall_lp_f1\\\\\\\": 65.0481\\\\n    },\\\\n    \\\\\\\"sj_diversity_sweep\\\\\\\": {\\\\n      \\\\\\\"proxy\\\\\\\": \\\\\\\"sj_diversity\\\\\\\",\\\\n      \\\\\\\"sweep\\\\\\\": [\\\\n        {\\\\n          \\\\\\\"threshold\\\\\\\": 0.001,\\\\n          \\\\\\\"gated_pct\\\\\\\": 88.66,\\\\n          \\\\\\\"gated_lp_delta_pp\\\\\\\": 0.7181,\\\\n          \\\\\\\"overall_dals_f1\\\\\\\": 65.0481,\\\\n          \\\\\\\"overall_greedy_f1\\\\\\\": 64.4115,\\\\n          \\\\\\\"overall_lp_f1\\\\\\\": 65.0481,\\\\n          \\\\\\\"dals_delta_vs_greedy_pp\\\\\\\": 0.6366,\\\\n          \\\\\\\"dals_delta_vs_lp_pp\\\\\\\": 0.0\\\\n        },\\\\n        {\\\\n          \\\\\\\"threshold\\\\\\\": 0.\\\\n\\\\n... [截断: 输出过长，省略 23273 字符] ...\\\\n\\\\n47,\\\\n          \\\\\\\"dals_delta_vs_greedy_pp\\\\\\\": -0.7978,\\\\n          \\\\\\\"dals_delta_vs_lp_pp\\\\\\\": 0.268\\\\n        }\\\\n      ],\\\\n      \\\\\\\"best_threshold\\\\\\\": 0.3,\\\\n      \\\\\\\"best_dals_f1\\\\\\\": 90.0828,\\\\n      \\\\\\\"best_dals_delta_vs_greedy_pp\\\\\\\": -0.7978,\\\\n      \\\\\\\"best_dals_delta_vs_lp_pp\\\\\\\": 0.268,\\\\n      \\\\\\\"overall_greedy_f1\\\\\\\": 90.8806,\\\\n      \\\\\\\"overall_lp_f1\\\\\\\": 89.8147\\\\n    },\\\\n    \\\\\\\"em_diversity_sweep\\\\\\\": {\\\\n      \\\\\\\"proxy\\\\\\\": \\\\\\\"em_diversity\\\\\\\",\\\\n      \\\\\\\"sweep\\\\\\\": [\\\\n        {\\\\n          \\\\\\\"threshold\\\\\\\": 0.001,\\\\n          \\\\\\\"gated_pct\\\\\\\": 43.07,\\\\n          \\\\\\\"gated_lp_delta_pp\\\\\\\": -2.4747,\\\\n          \\\\\\\"overall_dals_f1\\\\\\\": 89.8147,\\\\n          \\\\\\\"overall_greedy_f1\\\\\\\": 90.8806,\\\\n          \\\\\\\"overall_lp_f1\\\\\\\": 89.8147,\\\\n          \\\\\\\"dals_delta_vs_greedy_pp\\\\\\\": -1.0658,\\\\n          \\\\\\\"dals_delta_vs_lp_pp\\\\\\\": 0.0\\\\n        },\\\\n        {\\\\n          \\\\\\\"threshold\\\\\\\": 0.01,\\\\n          \\\\\\\"gated_pct\\\\\\\": 43.07,\\\\n          \\\\\\\"gated_lp_delta_pp\\\\\\\": -2.4747,\\\\n          \\\\\\\"overall_dals_f1\\\\\\\": 89.8147,\\\\n          \\\\\\\"overall_greedy_f1\\\\\\\": 90.8806,\\\\n          \\\\\\\"overall_lp_f1\\\\\\\": 89.8147,\\\\n          \\\\\\\"dals_delta_vs_greedy_pp\\\\\\\": -1.0658,\\\\n          \\\\\\\"dals_delta_vs_lp_pp\\\\\\\": 0.0\\\\n        },\\\\n        {\\\\n          \\\\\\\"threshold\\\\\\\": 0.05,\\\\n          \\\\\\\"gated_pct\\\\\\\": 43.07,\\\\n          \\\\\\\"gated_lp_delta_pp\\\\\\\": -2.4747,\\\\n          \\\\\\\"overall_dals_f1\\\\\\\": 89.8147,\\\\n          \\\\\\\"overall_greedy_f1\\\\\\\": 90.8806,\\\\n          \\\\\\\"overall_lp_f1\\\\\\\": 89.8147,\\\\n          \\\\\\\"dals_delta_vs_greedy_pp\\\\\\\": -1.0658,\\\\n          \\\\\\\"dals_delta_vs_lp_pp\\\\\\\": 0.0\\\\n        },\\\\n        {\\\\n          \\\\\\\"threshold\\\\\\\": 0.1,\\\\n          \\\\\\\"gated_pct\\\\\\\": 43.07,\\\\n          \\\\\\\"gated_lp_delta_pp\\\\\\\": -2.4747,\\\\n          \\\\\\\"overall_dals_f1\\\\\\\": 89.8147,\\\\n          \\\\\\\"overall_greedy_f1\\\\\\\": 90.8806,\\\\n          \\\\\\\"overall_lp_f1\\\\\\\": 89.8147,\\\\n          \\\\\\\"dals_delta_vs_greedy_pp\\\\\\\": -1.0658,\\\\n          \\\\\\\"dals_delta_vs_lp_pp\\\\\\\": 0.0\\\\n        },\\\\n        {\\\\n          \\\\\\\"threshold\\\\\\\": 0.15,\\\\n          \\\\\\\"gated_pct\\\\\\\": 43.07,\\\\n          \\\\\\\"gated_lp_delta_pp\\\\\\\": -2.4747,\\\\n          \\\\\\\"overall_dals_f1\\\\\\\": 89.8147,\\\\n          \\\\\\\"overall_greedy_f1\\\\\\\": 90.8806,\\\\n          \\\\\\\"overall_lp_f1\\\\\\\": 89.8147,\\\\n          \\\\\\\"dals_delta_vs_greedy_pp\\\\\\\": -1.0658,\\\\n          \\\\\\\"dals_delta_vs_lp_pp\\\\\\\": 0.0\\\\n        },\\\\n        {\\\\n          \\\\\\\"threshold\\\\\\\": 0.2,\\\\n          \\\\\\\"gated_pct\\\\\\\": 43.07,\\\\n          \\\\\\\"gated_lp_delta_pp\\\\\\\": -2.4747,\\\\n          \\\\\\\"overall_dals_f1\\\\\\\": 89.8147,\\\\n          \\\\\\\"overall_greedy_f1\\\\\\\": 90.8806,\\\\n          \\\\\\\"overall_lp_f1\\\\\\\": 89.8147,\\\\n          \\\\\\\"dals_delta_vs_greedy_pp\\\\\\\": -1.0658,\\\\n          \\\\\\\"dals_delta_vs_lp_pp\\\\\\\": 0.0\\\\n        },\\\\n        {\\\\n          \\\\\\\"threshold\\\\\\\": 0.3,\\\\n          \\\\\\\"gated_pct\\\\\\\": 27.07,\\\\n          \\\\\\\"gated_lp_delta_pp\\\\\\\": -3.6655,\\\\n          \\\\\\\"overall_dals_f1\\\\\\\": 89.8884,\\\\n          \\\\\\\"overall_greedy_f1\\\\\\\": 90.8806,\\\\n          \\\\\\\"overall_lp_f1\\\\\\\": 89.8147,\\\\n          \\\\\\\"dals_delta_vs_greedy_pp\\\\\\\": -0.9922,\\\\n          \\\\\\\"dals_delta_vs_lp_pp\\\\\\\": 0.0737\\\\n        },\\\\n        {\\\\n          \\\\\\\"threshold\\\\\\\": 0.5,\\\\n          \\\\\\\"gated_pct\\\\\\\": 18.9,\\\\n          \\\\\\\"gated_lp_delta_pp\\\\\\\": -4.382,\\\\n          \\\\\\\"overall_dals_f1\\\\\\\": 90.0522,\\\\n          \\\\\\\"overall_greedy_f1\\\\\\\": 90.8806,\\\\n          \\\\\\\"overall_lp_f1\\\\\\\": 89.8147,\\\\n          \\\\\\\"dals_delta_vs_greedy_pp\\\\\\\": -0.8284,\\\\n          \\\\\\\"dals_delta_vs_lp_pp\\\\\\\": 0.2375\\\\n        },\\\\n        {\\\\n          \\\\\\\"threshold\\\\\\\": 0.7,\\\\n          \\\\\\\"gated_pct\\\\\\\": 9.87,\\\\n          \\\\\\\"gated_lp_delta_pp\\\\\\\": -4.1469,\\\\n          \\\\\\\"overall_dals_f1\\\\\\\": 90.4713,\\\\n          \\\\\\\"overall_greedy_f1\\\\\\\": 90.8806,\\\\n          \\\\\\\"overall_lp_f1\\\\\\\": 89.8147,\\\\n          \\\\\\\"dals_delta_vs_greedy_pp\\\\\\\": -0.4093,\\\\n          \\\\\\\"dals_delta_vs_lp_pp\\\\\\\": 0.6566\\\\n        }\\\\n      ],\\\\n      \\\\\\\"best_threshold\\\\\\\": 0.7,\\\\n      \\\\\\\"best_dals_f1\\\\\\\": 90.4713,\\\\n      \\\\\\\"best_dals_delta_vs_greedy_pp\\\\\\\": -0.4093,\\\\n      \\\\\\\"best_dals_delta_vs_lp_pp\\\\\\\": 0.6566,\\\\n      \\\\\\\"overall_greedy_f1\\\\\\\": 90.8806,\\\\n      \\\\\\\"overall_lp_f1\\\\\\\": 89.8147\\\\n    },\\\\n    \\\\\\\"oracle\\\\\\\": {\\\\n      \\\\\\\"oracle_f1\\\\\\\": 91.3907,\\\\n      \\\\\\\"lp_better_count\\\\\\\": 43,\\\\n      \\\\\\\"greedy_better_count\\\\\\\": 117,\\\\n      \\\\\\\"tied_count\\\\\\\": 2596,\\\\n      \\\\\\\"n\\\\\\\": 2756\\\\n    },\\\\n    \\\\\\\"baseline_comparison\\\\\\\": {\\\\n      \\\\\\\"pure_greedy_f1\\\\\\\": 90.8806,\\\\n      \\\\\\\"pure_lp_f1\\\\\\\": 89.8147,\\\\n      \\\\\\\"dals_best_lp_range_f1\\\\\\\": 90.5737,\\\\n      \\\\\\\"dals_best_lp_range_tau\\\\\\\": 0.1,\\\\n      \\\\\\\"dals_best_sj_div_f1\\\\\\\": 90.0828,\\\\n      \\\\\\\"dals_best_sj_div_tau\\\\\\\": 0.3,\\\\n      \\\\\\\"dals_best_em_div_f1\\\\\\\": 90.4713,\\\\n      \\\\\\\"dals_best_em_div_tau\\\\\\\": 0.7,\\\\n      \\\\\\\"oracle_f1\\\\\\\": 91.3907\\\\n    }\\\\n  }\\\\n}\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.4}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"scierc\\\": {\\n    \\\"dataset\\\": \\\"scierc\\\",\\n    \\\"n_instances\\\": 529,\\n    \\\"lp_range_stats\\\": {\\n      \\\"mean\\\": 0.06218863264816551,\\n      \\\"median\\\": 0.040121078648161536,\\n      \\\"std\\\": 0.06908752812874064,\\n      \\\"P10\\\": 0.01858445776923011,\\n      \\\"P25\\\": 0.026459537324479056,\\n      \\\"P50\\\": 0.040121078648161536,\\n      \\\"P75\\\": 0.068535793140826,\\n      \\\"P90\\\": 0.12211430813918056,\\n      \\\"zero_pct\\\": 0.0,\\n      \\\"n_instances\\\": 529\\n    },\\n    \\\"lp_range_sweep\\\": {\\n      \\\"proxy\\\": \\\"lp_range\\\",\\n      \\\"sweep\\\": [\\n        {\\n          \\\"threshold\\\": 0.001,\\n          \\\"gated_pct\\\": 99.62,\\n          \\\"gated_lp_delta_pp\\\": 0.639,\\n          \\\"overall_dals_f1\\\": 65.0481,\\n          \\\"overall_greedy_f1\\\": 64.4115,\\n          \\\"overall_lp_f1\\\": 65.0481,\\n          \\\"dals_delta_vs_greedy_pp\\\": 0.6366,\\n          \\\"dals_delta_vs_lp_pp\\\": 0.0\\n        },\\n        {\\n          \\\"threshold\\\": 0.005,\\n          \\\"gated_pct\\\": 99.43,\\n          \\\"gated_lp_delta_pp\\\": 0.6403,\\n          \\\"overall_dals_f1\\\": 65.0481,\\n          \\\"overall_greedy_f1\\\": 64.4115,\\n          \\\"overall_lp_f1\\\": 65.0481,\\n          \\\"dals_delta_vs_greedy_pp\\\": 0.6366,\\n          \\\"dals_delta_vs_lp_pp\\\": 0.0\\n        },\\n        {\\n          \\\"threshold\\\": 0.01,\\n          \\\"gated_pct\\\": 98.87,\\n          \\\"gated_lp_delta_pp\\\": 0.6025,\\n          \\\"overall_dals_f1\\\": 65.0072,\\n          \\\"overall_greedy_f1\\\": 64.4115,\\n          \\\"overall_lp_f1\\\": 65.0481,\\n          \\\"dals_delta_vs_greedy_pp\\\": 0.5957,\\n          \\\"dals_delta_vs_lp_pp\\\": -0.041\\n        },\\n        {\\n          \\\"threshold\\\": 0.02,\\n          \\\"gated_pct\\\": 86.39,\\n          \\\"gated_lp_delta_pp\\\": 0.8595,\\n          \\\"overall_dals_f1\\\": 65.154,\\n          \\\"overall_greedy_f1\\\": 64.4115,\\n          \\\"overall_lp_f1\\\": 65.0481,\\n          \\\"dals_delta_vs_greedy_pp\\\": 0.7425,\\n          \\\"dals_delta_vs_lp_pp\\\": 0.1059\\n        },\\n        {\\n          \\\"threshold\\\": 0.03,\\n          \\\"gated_pct\\\": 68.24,\\n          \\\"gated_lp_delta_pp\\\": 1.2756,\\n          \\\"overall_dals_f1\\\": 65.282,\\n          \\\"overall_greedy_f1\\\": 64.4115,\\n          \\\"overall_lp_f1\\\": 65.0481,\\n          \\\"dals_delta_vs_greedy_pp\\\": 0.8705,\\n          \\\"dals_delta_vs_lp_pp\\\": 0.2339\\n        },\\n        {\\n          \\\"threshold\\\": 0.04,\\n          \\\"gated_pct\\\": 50.09,\\n          \\\"gated_lp_delta_pp\\\": 1.8618,\\n          \\\"overall_dals_f1\\\": 65.3441,\\n          \\\"overall_greedy_f1\\\": 64.4115,\\n          \\\"overall_lp_f1\\\": 65.0481,\\n          \\\"dals_delta_vs_greedy_pp\\\": 0.9326,\\n          \\\"dals_delta_vs_lp_pp\\\": 0.296\\n        },\\n        {\\n          \\\"threshold\\\": 0.05,\\n          \\\"gated_pct\\\": 39.7,\\n          \\\"gated_lp_delta_pp\\\": 2.8761,\\n          \\\"overall_dals_f1\\\": 65.5532,\\n          \\\"overall_greedy_f1\\\": 64.4115,\\n          \\\"overall_lp_f1\\\": 65.0481,\\n          \\\"dals_delta_vs_greedy_pp\\\": 1.1417,\\n          \\\"dals_delta_vs_lp_pp\\\": 0.5051\\n        },\\n        {\\n          \\\"threshold\\\": 0.07,\\n          \\\"gated_pct\\\": 23.63,\\n          \\\"gated_lp_delta_pp\\\": 3.2859,\\n          \\\"overall_dals_f1\\\": 65.1879,\\n          \\\"overall_greedy_f1\\\": 64.4115,\\n          \\\"overall_lp_f1\\\": 65.0481,\\n          \\\"dals_delta_vs_greedy_pp\\\": 0.7764,\\n          \\\"dals_delta_vs_lp_pp\\\": 0.1398\\n        },\\n        {\\n          \\\"threshold\\\": 0.1,\\n          \\\"gated_pct\\\": 16.07,\\n          \\\"gated_lp_delta_pp\\\": 3.6863,\\n          \\\"overall_dals_f1\\\": 65.0038,\\n          \\\"overall_greedy_f1\\\": 64.4115,\\n          \\\"overall_lp_f1\\\": 65.0481,\\n          \\\"dals_delta_vs_greedy_pp\\\": 0.5923,\\n          \\\"dals_delta_vs_lp_pp\\\": -0.0443\\n        }\\n      ],\\n      \\\"best_threshold\\\": 0.05,\\n      \\\"best_dals_f1\\\": 65.5532,\\n      \\\"best_dals_delta_vs_greedy_pp\\\": 1.1417,\\n      \\\"best_dals_delta_vs_lp_pp\\\": 0.5051,\\n      \\\"overall_greedy_f1\\\": 64.4115,\\n      \\\"overall_lp_f1\\\": 65.0481\\n    },\\n    \\\"sj_diversity_sweep\\\": {\\n      \\\"proxy\\\": \\\"sj_diversity\\\",\\n      \\\"sweep\\\": [\\n        {\\n          \\\"threshold\\\": 0.001,\\n          \\\"gated_pct\\\": 88.66,\\n          \\\"gated_lp_delta_pp\\\": 0.7181,\\n          \\\"overall_dals_f1\\\": 65.0481,\\n          \\\"overall_greedy_f1\\\": 64.4115,\\n          \\\"overall_lp_f1\\\": 65.0481,\\n          \\\"dals_delta_vs_greedy_pp\\\": 0.6366,\\n          \\\"dals_delta_vs_lp_pp\\\": 0.0\\n        },\\n        {\\n          \\\"threshold\\\": 0.\\n\\n... [截断: 输出过长，省略 23273 字符] ...\\n\\n47,\\n          \\\"dals_delta_vs_greedy_pp\\\": -0.7978,\\n          \\\"dals_delta_vs_lp_pp\\\": 0.268\\n        }\\n      ],\\n      \\\"best_threshold\\\": 0.3,\\n      \\\"best_dals_f1\\\": 90.0828,\\n      \\\"best_dals_delta_vs_greedy_pp\\\": -0.7978,\\n      \\\"best_dals_delta_vs_lp_pp\\\": 0.268,\\n      \\\"overall_greedy_f1\\\": 90.8806,\\n      \\\"overall_lp_f1\\\": 89.8147\\n    },\\n    \\\"em_diversity_sweep\\\": {\\n      \\\"proxy\\\": \\\"em_diversity\\\",\\n      \\\"sweep\\\": [\\n        {\\n          \\\"threshold\\\": 0.001,\\n          \\\"gated_pct\\\": 43.07,\\n          \\\"gated_lp_delta_pp\\\": -2.4747,\\n          \\\"overall_dals_f1\\\": 89.8147,\\n          \\\"overall_greedy_f1\\\": 90.8806,\\n          \\\"overall_lp_f1\\\": 89.8147,\\n          \\\"dals_delta_vs_greedy_pp\\\": -1.0658,\\n          \\\"dals_delta_vs_lp_pp\\\": 0.0\\n        },\\n        {\\n          \\\"threshold\\\": 0.01,\\n          \\\"gated_pct\\\": 43.07,\\n          \\\"gated_lp_delta_pp\\\": -2.4747,\\n          \\\"overall_dals_f1\\\": 89.8147,\\n          \\\"overall_greedy_f1\\\": 90.8806,\\n          \\\"overall_lp_f1\\\": 89.8147,\\n          \\\"dals_delta_vs_greedy_pp\\\": -1.0658,\\n          \\\"dals_delta_vs_lp_pp\\\": 0.0\\n        },\\n        {\\n          \\\"threshold\\\": 0.05,\\n          \\\"gated_pct\\\": 43.07,\\n          \\\"gated_lp_delta_pp\\\": -2.4747,\\n          \\\"overall_dals_f1\\\": 89.8147,\\n          \\\"overall_greedy_f1\\\": 90.8806,\\n          \\\"overall_lp_f1\\\": 89.8147,\\n          \\\"dals_delta_vs_greedy_pp\\\": -1.0658,\\n          \\\"dals_delta_vs_lp_pp\\\": 0.0\\n        },\\n        {\\n          \\\"threshold\\\": 0.1,\\n          \\\"gated_pct\\\": 43.07,\\n          \\\"gated_lp_delta_pp\\\": -2.4747,\\n          \\\"overall_dals_f1\\\": 89.8147,\\n          \\\"overall_greedy_f1\\\": 90.8806,\\n          \\\"overall_lp_f1\\\": 89.8147,\\n          \\\"dals_delta_vs_greedy_pp\\\": -1.0658,\\n          \\\"dals_delta_vs_lp_pp\\\": 0.0\\n        },\\n        {\\n          \\\"threshold\\\": 0.15,\\n          \\\"gated_pct\\\": 43.07,\\n          \\\"gated_lp_delta_pp\\\": -2.4747,\\n          \\\"overall_dals_f1\\\": 89.8147,\\n          \\\"overall_greedy_f1\\\": 90.8806,\\n          \\\"overall_lp_f1\\\": 89.8147,\\n          \\\"dals_delta_vs_greedy_pp\\\": -1.0658,\\n          \\\"dals_delta_vs_lp_pp\\\": 0.0\\n        },\\n        {\\n          \\\"threshold\\\": 0.2,\\n          \\\"gated_pct\\\": 43.07,\\n          \\\"gated_lp_delta_pp\\\": -2.4747,\\n          \\\"overall_dals_f1\\\": 89.8147,\\n          \\\"overall_greedy_f1\\\": 90.8806,\\n          \\\"overall_lp_f1\\\": 89.8147,\\n          \\\"dals_delta_vs_greedy_pp\\\": -1.0658,\\n          \\\"dals_delta_vs_lp_pp\\\": 0.0\\n        },\\n        {\\n          \\\"threshold\\\": 0.3,\\n          \\\"gated_pct\\\": 27.07,\\n          \\\"gated_lp_delta_pp\\\": -3.6655,\\n          \\\"overall_dals_f1\\\": 89.8884,\\n          \\\"overall_greedy_f1\\\": 90.8806,\\n          \\\"overall_lp_f1\\\": 89.8147,\\n          \\\"dals_delta_vs_greedy_pp\\\": -0.9922,\\n          \\\"dals_delta_vs_lp_pp\\\": 0.0737\\n        },\\n        {\\n          \\\"threshold\\\": 0.5,\\n          \\\"gated_pct\\\": 18.9,\\n          \\\"gated_lp_delta_pp\\\": -4.382,\\n          \\\"overall_dals_f1\\\": 90.0522,\\n          \\\"overall_greedy_f1\\\": 90.8806,\\n          \\\"overall_lp_f1\\\": 89.8147,\\n          \\\"dals_delta_vs_greedy_pp\\\": -0.8284,\\n          \\\"dals_delta_vs_lp_pp\\\": 0.2375\\n        },\\n        {\\n          \\\"threshold\\\": 0.7,\\n          \\\"gated_pct\\\": 9.87,\\n          \\\"gated_lp_delta_pp\\\": -4.1469,\\n          \\\"overall_dals_f1\\\": 90.4713,\\n          \\\"overall_greedy_f1\\\": 90.8806,\\n          \\\"overall_lp_f1\\\": 89.8147,\\n          \\\"dals_delta_vs_greedy_pp\\\": -0.4093,\\n          \\\"dals_delta_vs_lp_pp\\\": 0.6566\\n        }\\n      ],\\n      \\\"best_threshold\\\": 0.7,\\n      \\\"best_dals_f1\\\": 90.4713,\\n      \\\"best_dals_delta_vs_greedy_pp\\\": -0.4093,\\n      \\\"best_dals_delta_vs_lp_pp\\\": 0.6566,\\n      \\\"overall_greedy_f1\\\": 90.8806,\\n      \\\"overall_lp_f1\\\": 89.8147\\n    },\\n    \\\"oracle\\\": {\\n      \\\"oracle_f1\\\": 91.3907,\\n      \\\"lp_better_count\\\": 43,\\n      \\\"greedy_better_count\\\": 117,\\n      \\\"tied_count\\\": 2596,\\n      \\\"n\\\": 2756\\n    },\\n    \\\"baseline_comparison\\\": {\\n      \\\"pure_greedy_f1\\\": 90.8806,\\n      \\\"pure_lp_f1\\\": 89.8147,\\n      \\\"dals_best_lp_range_f1\\\": 90.5737,\\n      \\\"dals_best_lp_range_tau\\\": 0.1,\\n      \\\"dals_best_sj_div_f1\\\": 90.0828,\\n      \\\"dals_best_sj_div_tau\\\": 0.3,\\n      \\\"dals_best_em_div_f1\\\": 90.4713,\\n      \\\"dals_best_em_div_tau\\\": 0.7,\\n      \\\"oracle_f1\\\": 91.3907\\n    }\\n  }\\n}\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.4}}"
    }
  },
  "sourceToolAssistantUUID": "6017bf7e-4dda-4465-8356-f413fab12a3a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "a97de670-f9a7-4d30-affd-382982b8a334",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 98_

```json
{
  "type": "last-prompt",
  "leafUuid": "8483e788-b82a-40e8-9b5a-94fea0d0cedd",
  "sessionId": "a97de670-f9a7-4d30-affd-382982b8a334"
}
```

---

### Runtime record

_source line 99_

```json
{
  "type": "ai-title",
  "aiTitle": "Audit data inconsistencies in paper tables",
  "sessionId": "a97de670-f9a7-4d30-affd-382982b8a334"
}
```

---

### Assistant

_source line 100 · 2026-05-19T14:01:35.525Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the critical data. Let me compile the definitive findings:

## Investigation 1: SciERC AUROC — RESOLVED

The `d114_auroc_investigation/table1_update.md` confirms:
- Paper Table 1 uses **median-split AUROC** (`labels = (y >= median_f1).astype(int)`)
- Registry `exp_012_rerun_1024` uses **perfect-extraction AUROC** (`binary = (F1 >= 1.0)`)
- These are DIFFERENT metrics. Paper is CORRECT.
- All 15 values verified within rounding error.


- SciERC's median F1 of 0.6667 creates a significant divergence between the two approaches, whereas CoNLL's median F1 of 1.0 makes them align. This explains why the EM metric shows such a large gap (.614 vs .749) on SciERC — predicting above-median performance is fundamentally easier than predicting perfect extraction.

**Conclusion**: NOT an error. The registry AUROC uses a different binarization threshold. Paper is correct.

## Investigation 2: CoNLL LP selection Δ — CONFIRMED INCONSISTENCY

From `w1_table3_multiseed.json`, `conll_n8` has only a single seed run.

The computed LP delta for seed 42 is -1.0482pp, but this doesn't match the paper's reported values: Table 3 claims -0.85pp, while the appendix cross-selection shows -1.1pp. The appendix value is close enough when accounting for rounding (F1 rounded to 3 decimals), but the -0.85pp discrepancy remains unexplained. Let me trace where that figure originates by checking the underlying data. Looking at the SJ selection metrics, I'm seeing a delta of -0.89pp, which is much closer to the -0.85pp mentioned in the paper. This makes me wonder if there's been a mix-up—could the paper have reported the SJ delta in the LP column, or is -0.85pp coming from a different LP selection variant like max or sum instead of mean? The greedy-to-LP difference I'm calculating consistently comes out to around -1.0 to -1.1pp, not -0.85pp, so something doesn't quite align.

I'm noticing the correlation coefficient in Table 3 is ρ = .302, but my computed mean_logprob correlation is 0.3157. However, when I check the max_logprob correlation, it's 0.3017—which rounds to exactly .302. This suggests Table 3 might be using max_logprob selection rather than mean_logprob, which could explain the discrepancy in the delta values. , since the selection always uses the sample with the highest mean_logprob. So the -0.85pp gap still doesn't make sense. The actual selection delta is -1.05pp.

Let me look at `recompute_table_metrics.py` to see if Table 3 is computing things differently. That script extracts logprobs from the data, using either stored logprobs or reconstructing them from cumulative values and token counts, then collects the max logprob and the F1 scores for the selected samples.

Computing correlations...

It calculates both mean and max logprob correlations with greedy F1, and for selection it picks the sample with the highest logprob value. This should match the mean_logprob selection approach. I think the -0.85pp figure is just incorrect, and the real value for seed 42 is closer to -1.05pp.

Looking at the appendix cross-selection results, LP achieves .897 while greedy gets .908, which gives -1.1pp. But when I check the actual w1_table3 data with full precision, LP_sel is 0.8974 and greedy is 0.9079, yielding -1.05pp. The -1.1pp in the appendix comes from rounding the values to three decimals before computing the difference. So the correct delta for CoNLL N=8 seed 42 is -1.05pp.

Table 3 reports -0.85pp, which doesn't match either calculation. I'm wondering if this could be a 3-seed mean that somehow produced that value, but the metadata explicitly says only 1 seed exists for conll_n8, and the table caption claims 3-seed means. This is a clear inconsistency—either the caption is wrong or the data is incomplete.

So for this investigation: Table 3's -0.85pp doesn't align with the seed 42 data I found (-1.05pp), the appendix value (-1.1pp) rounds correctly from that same seed, and I can't verify where -0.85pp comes from at all.

For FewNERD, the 13.8% degeneracy rate checks out against the gold-filtered data with constant F1. The confusion came from a different experiment in the registry using a different definition or denominator that shows 10.1% instead.

Now I'm noticing the table caption claims 3-seed means for FewNERD, but the actual data file only has seed 42. If it's supposed to be a 3-seed average using the unified definition across seeds 42, 123, and 456, I'd need to compute that mean rather than just report the single seed value.

The metadata confirms `"n_seeds": 1` for FewNERD, so the caption is misleading — both FewNERD and CoNLL are actually single-seed results, not 3-seed means as claimed. The 13.8% is correct for seed 42 alone, but the labeling is wrong.

Now I'm moving to investigate the CoNLL degeneracy issue at 48.4%, which appears to be a confirmed error based on the unified metrics data. The metrics show n=2,756 for the CoNLL N=8 data, but the degeneracy value of 48.4% actually comes from N=16 experiments. Since both N values use the same instances, the sample count alone doesn't clarify which N was used—I need to look at the degeneracy rates to distinguish them, where N=8 gives 59.1% and N=16 gives 48.4%.

There's also a small discrepancy in the greedy F1 score: the JSON file shows 0.9088 (rounding to .909), while Table 3 lists .908, which matches the unified table's 0.9079. The key issue is that Table 3 claims N=8 for CoNLL, but the 48.4% degeneracy clearly indicates N=16 data was used instead.

For the LP ρ value, Table 3's .302 aligns with the max LP ρ of 0.3017 from the unified table, whereas the mean is 0.3157—so the table is reporting the maximum rather than the mean, which is fine as long as it's specified.

Now I'm checking the dals_analysis file directly for the CoNLL degeneracy calculation to see if it's computed there, and I'm looking at the oracle metrics which show the breakdown of cases where LP performs better versus greedy.

I have what I need to write up the report. Let me structure the findings: the SciERC AUROC discrepancy is a false alarm since the paper and registry use different binarization methods (median-split versus perfect extraction), and the previous audit confirmed all 15 values match. For the CoNLL LP delta, Table 3 reports -0.85pp, which I need to verify against the actual data.

Looking at the seed 42 computation, I'm getting -1.05pp, and the appendix cross-selection shows -1.1pp which aligns with that when rounded. The caption claims 3-seed means but only seed 42 exists for CoNLL, so the correct value should be -1.05pp or -1.0pp with a note clarifying the single-seed situation. For FewNERD's 13.8% degeneracy rate, that matches the seed 42 unified_metrics calculation (13.754% rounded), though the registry's 10.1% for the same seed uses an older definition. The caption again claims 3-seed means but only one seed is available.

Now I'm seeing the CoNLL degeneracy issue is a P0 error—the table header says N=8 but the 48.4% value comes from N=16 data. The actual N=8 degeneracy should be 59.1%, so I need to either correct the value or update the header to match the data source.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8483e788-b82a-40e8-9b5a-94fea0d0cedd",
  "isSidechain": false,
  "requestId": "req_011CbC3jrfR1875JjJxXRKZg",
  "type": "assistant",
  "uuid": "9f7c46da-45bb-4754-9f12-c0831ec85b97",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "a97de670-f9a7-4d30-affd-382982b8a334",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01L3YkokWbMsC5A4Z1UNq1kt",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 18444,
      "cache_read_input_tokens": 78853,
      "output_tokens": 7305,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 18444,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 7305,
          "cache_read_input_tokens": 78853,
          "cache_creation_input_tokens": 18444,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 18444
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

_source line 101 · 2026-05-19T14:01:35.538Z_

Now I have complete data for all four investigations. Let me compile the verification report.

Key findings:
1. **Investigation 1**: d114 audit already resolved — paper uses median-split AUROC, registry uses F1>=1.0 AUROC. Different metrics, paper correct.
2. **Investigation 2**: Table 3 LP Δ = -0.85pp, but computed value is -1.05pp; also only 1 seed exists despite "3-seed" caption.
3. **Investigation 3**: 13.8% is correct for seed 42 (13.754%), but Table 3 claims "3-seed means" when only 1 seed used.
4. **Investigation 4**: 48.4% matches N=16 (exp_002_conll_n16), not N=8. N=8 degeneracy = 59.1%.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9f7c46da-45bb-4754-9f12-c0831ec85b97",
  "isSidechain": false,
  "requestId": "req_011CbC3jrfR1875JjJxXRKZg",
  "type": "assistant",
  "uuid": "fa4c31a7-5683-42f1-9bb7-1c5f80caeb69",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "a97de670-f9a7-4d30-affd-382982b8a334",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01L3YkokWbMsC5A4Z1UNq1kt",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 18444,
      "cache_read_input_tokens": 78853,
      "output_tokens": 7305,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 18444,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 7305,
          "cache_read_input_tokens": 78853,
          "cache_creation_input_tokens": 18444,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 18444
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

_source line 102 · 2026-05-19T14:02:19.398Z_

<details open><summary>🔧 Tool call — Write · `toolu_01LHHd9NrXAwDe3s8MwQX3Wa`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/p0_data_verification_report.md",
  "content": "# P0/P1 Data Verification Report\n\n**Date**: 2026-05-19\n**Scope**: Four claim-audit flagged inconsistencies in paper vs registry data\n\n---\n\n## Investigation 1: SciERC AUROC Table 1 vs Registry (P0) → FALSE ALARM\n\n### Discrepancy reported\n\n| Signal | Paper Table 1 | Registry exp_012_rerun_1024 | Δ |\n|--------|--------------|---------------------------|------|\n| VC | .663 | .684 | -2.1pp |\n| SJ | .650 | .692 | -4.2pp |\n| FK | .602 | .629 | -2.7pp |\n| EM | .614 | .749 | -13.5pp |\n| LP | .578 | .578 | 0pp |\n\n### Finding\n\n**Not an error.** The paper and registry use different AUROC binarization thresholds:\n\n- **Paper Table 1**: median-split AUROC (`binary = (F1 >= median_F1)`), computed by `analyze_exp015_unified.py`. SciERC NER median F1 = 0.6667.\n- **Registry exp_012_rerun_1024**: perfect-extraction AUROC (`binary = (F1 >= 1.0)`), computed by `eval_exp012_rerun_auroc.py`.\n\nFor CoNLL (median F1 = 1.0), both definitions coincide → LP matches. For SciERC (median F1 = 0.667), they diverge substantially.\n\nPrevious investigation (`d114_auroc_investigation/table1_update.md`) verified all 15 Table 1 values match within rounding error (<0.0005).\n\n### Verification source\n- `output/d114_auroc_investigation/unified_auroc.json` — per-seed and aggregated verified AUROC\n- `output/d114_auroc_investigation/table1_update.md` — full verification report\n\n### Correct value\nPaper Table 1 values are **correct**. No fix needed.\n\n### Recommendation\nRegistry `exp_012_rerun_1024` AUROC fields should be annotated as \"perfect-extraction AUROC (F1>=1.0 threshold)\" to prevent future confusion with the paper's median-split AUROC.\n\n---\n\n## Investigation 2: CoNLL LP Selection Δ Inconsistency (P0) → CONFIRMED ERROR\n\n### Discrepancy reported\n- Table 3 (experiments.tex:122): CoNLL LP Δ = **-0.85pp**\n- Appendix cross-selection (appendix.tex:248): LP F1 = .897, Greedy = .908 → Δ = **-1.1pp**\n\n### Finding\n\n**Table 3's -0.85pp is incorrect.** Two sub-issues:\n\n**Issue A: Wrong LP Δ value.** From `w1_table3_multiseed.json`, CoNLL N=8 seed 42:\n- `greedy_f1 = 0.9079`, `lp_sel_f1 = 0.8974`\n- `lp_delta_pp = -1.0482`\n\nThe appendix cross-selection's -1.1pp = (.897 - .908) is the same computation rounded to 3 decimal places. Both are consistent: **Δ ≈ -1.05pp**.\n\nNo known data source produces -0.85pp. The closest match is the SJ selection delta (-0.89pp from `sj_delta_pp = -0.8914`), suggesting a possible column-swap error during table composition.\n\n**Issue B: \"3-seed means\" claim is false for CoNLL.** The `w1_table3_multiseed.json` file shows `\"n_seeds\": 1` for `conll_n8` — only seed 42 data exists. The Table 3 caption states \"Few-NERD/CoNLL: 3-seed means\" which is incorrect.\n\n### Correct value\n- LP Δ = **-1.05pp** (seed 42 single-seed, rounded to -1.0pp or -1.1pp)\n- Caption should either say \"CoNLL: single-seed\" or 3-seed data must be generated\n\n### Suggested fix\n1. Update Table 3 CoNLL LP Δ from -0.85pp to -1.05pp (or -1.0pp)\n2. Update caption to clarify CoNLL and FewNERD are single-seed (seed 42)\n3. Or generate seeds 123/456 CoNLL N=8 data and report true 3-seed mean\n\n---\n\n## Investigation 3: FewNERD Degeneracy 13.8% Source (P1) → CORRECT VALUE, WRONG CAPTION\n\n### Discrepancy reported\nPaper Table 3: FewNERD degen = 13.8%. Registry per-seed values:\n- Seed 42 (exp_021_fewnerd_full): 10.1%\n- Seed 123: 13.1%, Seed 456: 12.1%, Seed 789: 11.8%\n- 3-seed mean (42/123/456) = 11.8% ≠ 13.8%\n\n### Finding\n\n**13.8% is correct for seed 42** using the unified_metrics definition:\n\n| Source | Definition | Seed 42 value |\n|--------|-----------|---------------|\n| Registry exp_021_fewnerd_full | `degeneracy_rate` (old, no source tag) | 10.1% |\n| `unified_tab_fewnerd_maxlp.json` | constant-F1 gold-filtered | **13.754% → 13.8%** |\n| Registry exp_021_fewnerd_n8_seed123 | unified_metrics_constant_f1_gold_filtered | 13.12% |\n\nThe registry's 10.1% for seed 42 uses an older/different degeneracy definition (possibly different denominator — total vs gold-filtered, or different F1 comparison logic). The seed-specific experiments (123/456/789) use the unified definition and produce different values.\n\nThe `w1_table3_multiseed.json` confirms FewNERD also has `\"n_seeds\": 1` (seed 42 only).\n\n### Correct value\n- **13.8%** is correct for seed 42, unified_metrics constant-F1 gold-filtered\n- True 3-seed mean (42/123/456) under unified definition ≈ **13.0%** = (13.75 + 13.12 + 12.12) / 3\n\n### Suggested fix\n1. Update Table 3 caption to say \"single-seed (seed 42)\" for FewNERD (same as CoNLL fix)\n2. Or compute unified-definition degen for seeds 123/456 and report 3-seed mean (~13.0%)\n3. Update registry exp_021_fewnerd_full to include `degen_rate_source` tag and reconcile with unified definition\n\n---\n\n## Investigation 4: CoNLL Degeneracy 48.4% N=8 vs N=16 (P1) → CONFIRMED ERROR\n\n### Discrepancy reported\nTable 3 header says N=8, CoNLL degen = 48.4%. Registry exp_002_conll_n16 (N=16) has degen_rate = 0.4844.\n\n### Finding\n\n**Confirmed: 48.4% is N=16 data, not N=8.**\n\n| Source | N | Degen rate |\n|--------|---|-----------|\n| `unified_tab_fewnerd_maxlp.json` (seed 42) | 8 | **59.14%** |\n| Registry exp_002_conll_n16 (seed 42) | 16 | **48.44%** |\n| Registry exp_002_conll_n16_seed123 | 16 | 47.10% |\n| Registry exp_002_conll_n16_seed456 | 16 | 55.44% |\n| N=16 3-seed mean | 16 | 50.3% |\n\nN=8 produces higher degeneracy (59.1%) because fewer samples → less chance of F1 variation. Table 3 claims N=8 but reports the N=16 value (48.4%).\n\nOther Table 3 CoNLL values (n=2,756, greedy=.908, LP ρ=.302) are consistent with N=8 seed 42 data. Only the degeneracy column was pulled from N=16.\n\n### Correct value\n- N=8 CoNLL degeneracy (seed 42) = **59.1%**\n- N=16 CoNLL degeneracy (seed 42) = 48.4%\n\n### Suggested fix\nUpdate Table 3 CoNLL degen from 48.4% to 59.1%\n\n---\n\n## Summary\n\n| # | Issue | Severity | Status | Fix needed |\n|---|-------|----------|--------|-----------|\n| 1 | SciERC AUROC Table 1 vs registry | P0 | **False alarm** | Annotate registry AUROC definition |\n| 2 | CoNLL LP Δ inconsistency | P0 | **Confirmed error** | Table 3: -0.85pp → -1.05pp; fix \"3-seed\" caption |\n| 3 | FewNERD degen 13.8% source | P1 | **Value correct, caption wrong** | Fix \"3-seed\" caption or generate multi-seed data |\n| 4 | CoNLL degen 48.4% N mismatch | P1 | **Confirmed error** | Table 3: 48.4% → 59.1% (N=8 value) |\n\n### Cross-cutting issue: Table 3 \"3-seed means\" caption\nTable 3 caption claims \"Few-NERD/CoNLL: 3-seed means\" but both datasets have only seed 42 data in `w1_table3_multiseed.json`. Either:\n- (a) Generate seeds 123/456 for CoNLL N=8 and FewNERD N=8, then report true 3-seed means\n- (b) Correct the caption to \"single-seed (seed 42)\" for these datasets\n\nOption (b) is simpler but weakens statistical credibility. Option (a) requires new inference runs.\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fa4c31a7-5683-42f1-9bb7-1c5f80caeb69",
  "isSidechain": false,
  "requestId": "req_011CbC3jrfR1875JjJxXRKZg",
  "type": "assistant",
  "uuid": "32882ea2-1ecf-4076-8433-42992577c51e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "a97de670-f9a7-4d30-affd-382982b8a334",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01L3YkokWbMsC5A4Z1UNq1kt",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 18444,
      "cache_read_input_tokens": 78853,
      "output_tokens": 7305,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 18444,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 7305,
          "cache_read_input_tokens": 78853,
          "cache_creation_input_tokens": 18444,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 18444
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

_source line 103 · 2026-05-19T14:02:19.429Z_

<details><summary>↩ Tool result · `toolu_01LHHd9NrXAwDe3s8MwQX3Wa`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/p0_data_verification_report.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "32882ea2-1ecf-4076-8433-42992577c51e",
  "isSidechain": false,
  "promptId": "0731b9be-f5e6-4a8a-9a3c-2edafe06629b",
  "type": "user",
  "uuid": "9b8e47ff-9354-4b27-812b-c18e0257c6e8",
  "toolUseResult": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/p0_data_verification_report.md",
    "content": "# P0/P1 Data Verification Report\n\n**Date**: 2026-05-19\n**Scope**: Four claim-audit flagged inconsistencies in paper vs registry data\n\n---\n\n## Investigation 1: SciERC AUROC Table 1 vs Registry (P0) → FALSE ALARM\n\n### Discrepancy reported\n\n| Signal | Paper Table 1 | Registry exp_012_rerun_1024 | Δ |\n|--------|--------------|---------------------------|------|\n| VC | .663 | .684 | -2.1pp |\n| SJ | .650 | .692 | -4.2pp |\n| FK | .602 | .629 | -2.7pp |\n| EM | .614 | .749 | -13.5pp |\n| LP | .578 | .578 | 0pp |\n\n### Finding\n\n**Not an error.** The paper and registry use different AUROC binarization thresholds:\n\n- **Paper Table 1**: median-split AUROC (`binary = (F1 >= median_F1)`), computed by `analyze_exp015_unified.py`. SciERC NER median F1 = 0.6667.\n- **Registry exp_012_rerun_1024**: perfect-extraction AUROC (`binary = (F1 >= 1.0)`), computed by `eval_exp012_rerun_auroc.py`.\n\nFor CoNLL (median F1 = 1.0), both definitions coincide → LP matches. For SciERC (median F1 = 0.667), they diverge substantially.\n\nPrevious investigation (`d114_auroc_investigation/table1_update.md`) verified all 15 Table 1 values match within rounding error (<0.0005).\n\n### Verification source\n- `output/d114_auroc_investigation/unified_auroc.json` — per-seed and aggregated verified AUROC\n- `output/d114_auroc_investigation/table1_update.md` — full verification report\n\n### Correct value\nPaper Table 1 values are **correct**. No fix needed.\n\n### Recommendation\nRegistry `exp_012_rerun_1024` AUROC fields should be annotated as \"perfect-extraction AUROC (F1>=1.0 threshold)\" to prevent future confusion with the paper's median-split AUROC.\n\n---\n\n## Investigation 2: CoNLL LP Selection Δ Inconsistency (P0) → CONFIRMED ERROR\n\n### Discrepancy reported\n- Table 3 (experiments.tex:122): CoNLL LP Δ = **-0.85pp**\n- Appendix cross-selection (appendix.tex:248): LP F1 = .897, Greedy = .908 → Δ = **-1.1pp**\n\n### Finding\n\n**Table 3's -0.85pp is incorrect.** Two sub-issues:\n\n**Issue A: Wrong LP Δ value.** From `w1_table3_multiseed.json`, CoNLL N=8 seed 42:\n- `greedy_f1 = 0.9079`, `lp_sel_f1 = 0.8974`\n- `lp_delta_pp = -1.0482`\n\nThe appendix cross-selection's -1.1pp = (.897 - .908) is the same computation rounded to 3 decimal places. Both are consistent: **Δ ≈ -1.05pp**.\n\nNo known data source produces -0.85pp. The closest match is the SJ selection delta (-0.89pp from `sj_delta_pp = -0.8914`), suggesting a possible column-swap error during table composition.\n\n**Issue B: \"3-seed means\" claim is false for CoNLL.** The `w1_table3_multiseed.json` file shows `\"n_seeds\": 1` for `conll_n8` — only seed 42 data exists. The Table 3 caption states \"Few-NERD/CoNLL: 3-seed means\" which is incorrect.\n\n### Correct value\n- LP Δ = **-1.05pp** (seed 42 single-seed, rounded to -1.0pp or -1.1pp)\n- Caption should either say \"CoNLL: single-seed\" or 3-seed data must be generated\n\n### Suggested fix\n1. Update Table 3 CoNLL LP Δ from -0.85pp to -1.05pp (or -1.0pp)\n2. Update caption to clarify CoNLL and FewNERD are single-seed (seed 42)\n3. Or generate seeds 123/456 CoNLL N=8 data and report true 3-seed mean\n\n---\n\n## Investigation 3: FewNERD Degeneracy 13.8% Source (P1) → CORRECT VALUE, WRONG CAPTION\n\n### Discrepancy reported\nPaper Table 3: FewNERD degen = 13.8%. Registry per-seed values:\n- Seed 42 (exp_021_fewnerd_full): 10.1%\n- Seed 123: 13.1%, Seed 456: 12.1%, Seed 789: 11.8%\n- 3-seed mean (42/123/456) = 11.8% ≠ 13.8%\n\n### Finding\n\n**13.8% is correct for seed 42** using the unified_metrics definition:\n\n| Source | Definition | Seed 42 value |\n|--------|-----------|---------------|\n| Registry exp_021_fewnerd_full | `degeneracy_rate` (old, no source tag) | 10.1% |\n| `unified_tab_fewnerd_maxlp.json` | constant-F1 gold-filtered | **13.754% → 13.8%** |\n| Registry exp_021_fewnerd_n8_seed123 | unified_metrics_constant_f1_gold_filtered | 13.12% |\n\nThe registry's 10.1% for seed 42 uses an older/different degeneracy definition (possibly different denominator — total vs gold-filtered, or different F1 comparison logic). The seed-specific experiments (123/456/789) use the unified definition and produce different values.\n\nThe `w1_table3_multiseed.json` confirms FewNERD also has `\"n_seeds\": 1` (seed 42 only).\n\n### Correct value\n- **13.8%** is correct for seed 42, unified_metrics constant-F1 gold-filtered\n- True 3-seed mean (42/123/456) under unified definition ≈ **13.0%** = (13.75 + 13.12 + 12.12) / 3\n\n### Suggested fix\n1. Update Table 3 caption to say \"single-seed (seed 42)\" for FewNERD (same as CoNLL fix)\n2. Or compute unified-definition degen for seeds 123/456 and report 3-seed mean (~13.0%)\n3. Update registry exp_021_fewnerd_full to include `degen_rate_source` tag and reconcile with unified definition\n\n---\n\n## Investigation 4: CoNLL Degeneracy 48.4% N=8 vs N=16 (P1) → CONFIRMED ERROR\n\n### Discrepancy reported\nTable 3 header says N=8, CoNLL degen = 48.4%. Registry exp_002_conll_n16 (N=16) has degen_rate = 0.4844.\n\n### Finding\n\n**Confirmed: 48.4% is N=16 data, not N=8.**\n\n| Source | N | Degen rate |\n|--------|---|-----------|\n| `unified_tab_fewnerd_maxlp.json` (seed 42) | 8 | **59.14%** |\n| Registry exp_002_conll_n16 (seed 42) | 16 | **48.44%** |\n| Registry exp_002_conll_n16_seed123 | 16 | 47.10% |\n| Registry exp_002_conll_n16_seed456 | 16 | 55.44% |\n| N=16 3-seed mean | 16 | 50.3% |\n\nN=8 produces higher degeneracy (59.1%) because fewer samples → less chance of F1 variation. Table 3 claims N=8 but reports the N=16 value (48.4%).\n\nOther Table 3 CoNLL values (n=2,756, greedy=.908, LP ρ=.302) are consistent with N=8 seed 42 data. Only the degeneracy column was pulled from N=16.\n\n### Correct value\n- N=8 CoNLL degeneracy (seed 42) = **59.1%**\n- N=16 CoNLL degeneracy (seed 42) = 48.4%\n\n### Suggested fix\nUpdate Table 3 CoNLL degen from 48.4% to 59.1%\n\n---\n\n## Summary\n\n| # | Issue | Severity | Status | Fix needed |\n|---|-------|----------|--------|-----------|\n| 1 | SciERC AUROC Table 1 vs registry | P0 | **False alarm** | Annotate registry AUROC definition |\n| 2 | CoNLL LP Δ inconsistency | P0 | **Confirmed error** | Table 3: -0.85pp → -1.05pp; fix \"3-seed\" caption |\n| 3 | FewNERD degen 13.8% source | P1 | **Value correct, caption wrong** | Fix \"3-seed\" caption or generate multi-seed data |\n| 4 | CoNLL degen 48.4% N mismatch | P1 | **Confirmed error** | Table 3: 48.4% → 59.1% (N=8 value) |\n\n### Cross-cutting issue: Table 3 \"3-seed means\" caption\nTable 3 caption claims \"Few-NERD/CoNLL: 3-seed means\" but both datasets have only seed 42 data in `w1_table3_multiseed.json`. Either:\n- (a) Generate seeds 123/456 for CoNLL N=8 and FewNERD N=8, then report true 3-seed means\n- (b) Correct the caption to \"single-seed (seed 42)\" for these datasets\n\nOption (b) is simpler but weakens statistical credibility. Option (a) requires new inference runs.\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  },
  "sourceToolAssistantUUID": "32882ea2-1ecf-4076-8433-42992577c51e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "a97de670-f9a7-4d30-affd-382982b8a334",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 104_

```json
{
  "type": "last-prompt",
  "leafUuid": "9b8e47ff-9354-4b27-812b-c18e0257c6e8",
  "sessionId": "a97de670-f9a7-4d30-affd-382982b8a334"
}
```

---

### Runtime record

_source line 105_

```json
{
  "type": "ai-title",
  "aiTitle": "Audit data inconsistencies in paper tables",
  "sessionId": "a97de670-f9a7-4d30-affd-382982b8a334"
}
```

---

### Assistant

_source line 106 · 2026-05-19T14:02:22.836Z_

Now let me register the artifact.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9b8e47ff-9354-4b27-812b-c18e0257c6e8",
  "isSidechain": false,
  "requestId": "req_011CbC3uzkcV71vuFDpDBgBa",
  "type": "assistant",
  "uuid": "d33dc196-dedf-410c-89db-d36b3bb2b811",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "a97de670-f9a7-4d30-affd-382982b8a334",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HrR9AEFoc5bzoM12n4EhRy",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 18605,
      "cache_read_input_tokens": 86051,
      "output_tokens": 336,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 18605,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 336,
          "cache_read_input_tokens": 86051,
          "cache_creation_input_tokens": 18605,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 18605
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "previous_message_not_found"
      }
    }
  }
}
```

</details>

---

### Tool call

_source line 107 · 2026-05-19T14:02:26.209Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact · `toolu_014S6iFbMbxhzzMxwn51QDc9`</summary>

```json
{
  "name": "P0/P1 Data Verification Report",
  "type": "report",
  "description": "Deep audit of 4 data inconsistencies flagged by claim audit: SciERC AUROC (false alarm — different metrics), CoNLL LP Δ (confirmed error: -0.85pp should be -1.05pp), FewNERD degen 13.8% (correct value, wrong 3-seed caption), CoNLL degen 48.4% (confirmed error: N=16 value used in N=8 table)",
  "project": "struct_self_consist_ie",
  "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/p0_data_verification_report.md",
  "tags": [
    "claim-audit",
    "data-verification",
    "table3",
    "table1",
    "P0"
  ]
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d33dc196-dedf-410c-89db-d36b3bb2b811",
  "isSidechain": false,
  "requestId": "req_011CbC3uzkcV71vuFDpDBgBa",
  "type": "assistant",
  "uuid": "cad2b81c-4707-4040-a28b-ec32f4c332cf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "a97de670-f9a7-4d30-affd-382982b8a334",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HrR9AEFoc5bzoM12n4EhRy",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 18605,
      "cache_read_input_tokens": 86051,
      "output_tokens": 336,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 18605,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 336,
          "cache_read_input_tokens": 86051,
          "cache_creation_input_tokens": 18605,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 18605
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "previous_message_not_found"
      }
    }
  }
}
```

</details>

---

### Tool result

_source line 108 · 2026-05-19T14:02:26.672Z_

<details><summary>↩ Tool result · `toolu_014S6iFbMbxhzzMxwn51QDc9`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260519_f35393\", \"name\": \"P0/P1 Data Verification Report\", \"type\": \"report\", \"description\": \"Deep audit of 4 data inconsistencies flagged by claim audit: SciERC AUROC (false alarm — different metrics), CoNLL LP Δ (confirmed error: -0.85pp should be -1.05pp), FewNERD degen 13.8% (correct value, wrong 3-seed caption), CoNLL degen 48.4% (confirmed error: N=16 value used in N=8 table)\", \"path\": \"projects/struct_self_consist_ie/artifacts/_project/report/p0_data_verification_report.md\", \"url\": null, \"project\": \"struct_self_consist_ie\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-19T14:02:26.215584+00:00\", \"tags\": [\"claim-audit\", \"data-verification\", \"table3\", \"table1\", \"P0\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cad2b81c-4707-4040-a28b-ec32f4c332cf",
  "isSidechain": false,
  "promptId": "0731b9be-f5e6-4a8a-9a3c-2edafe06629b",
  "type": "user",
  "uuid": "0d570b2a-baf4-444d-913b-4aa819704e5d",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"artifact\\\": {\\\"id\\\": \\\"art_20260519_f35393\\\", \\\"name\\\": \\\"P0/P1 Data Verification Report\\\", \\\"type\\\": \\\"report\\\", \\\"description\\\": \\\"Deep audit of 4 data inconsistencies flagged by claim audit: SciERC AUROC (false alarm — different metrics), CoNLL LP Δ (confirmed error: -0.85pp should be -1.05pp), FewNERD degen 13.8% (correct value, wrong 3-seed caption), CoNLL degen 48.4% (confirmed error: N=16 value used in N=8 table)\\\", \\\"path\\\": \\\"projects/struct_self_consist_ie/artifacts/_project/report/p0_data_verification_report.md\\\", \\\"url\\\": null, \\\"project\\\": \\\"struct_self_consist_ie\\\", \\\"exp_id\\\": null, \\\"skill\\\": \\\"\\\", \\\"created_at\\\": \\\"2026-05-19T14:02:26.215584+00:00\\\", \\\"tags\\\": [\\\"claim-audit\\\", \\\"data-verification\\\", \\\"table3\\\", \\\"table1\\\", \\\"P0\\\"]}, \\\"manifest\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/manifest.yaml\\\"}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260519_f35393\", \"name\": \"P0/P1 Data Verification Report\", \"type\": \"report\", \"description\": \"Deep audit of 4 data inconsistencies flagged by claim audit: SciERC AUROC (false alarm — different metrics), CoNLL LP Δ (confirmed error: -0.85pp should be -1.05pp), FewNERD degen 13.8% (correct value, wrong 3-seed caption), CoNLL degen 48.4% (confirmed error: N=16 value used in N=8 table)\", \"path\": \"projects/struct_self_consist_ie/artifacts/_project/report/p0_data_verification_report.md\", \"url\": null, \"project\": \"struct_self_consist_ie\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-19T14:02:26.215584+00:00\", \"tags\": [\"claim-audit\", \"data-verification\", \"table3\", \"table1\", \"P0\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"
    }
  },
  "sourceToolAssistantUUID": "cad2b81c-4707-4040-a28b-ec32f4c332cf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "a97de670-f9a7-4d30-affd-382982b8a334",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 109 · 2026-05-19T14:02:35.196Z_

四项调查结果：

| # | 问题 | 结论 |
|---|------|------|
| 1 | SciERC AUROC Table 1 vs registry | **误报** — paper 用 median-split AUROC，registry 用 F1≥1.0 AUROC，是两个不同指标，paper 正确 |
| 2 | CoNLL LP Δ 不一致 | **确认错误** — Table 3 写 -0.85pp，实际计算为 -1.05pp（seed 42）；且标题声称 3-seed mean 但只有 1 个 seed |
| 3 | FewNERD degen 13.8% | **值正确，标题错** — 13.8% 是 seed 42 单 seed 的 unified_metrics 结果（13.754%），但 Table 3 标题谎称 3-seed mean |
| 4 | CoNLL degen 48.4% | **确认错误** — 48.4% 来自 N=16 (exp_002_conll_n16)，N=8 实际是 59.1% |

**跨问题共性**：Table 3 标题声称 "Few-NERD/CoNLL: 3-seed means"，但 `w1_table3_multiseed.json` 显示两者都只有 seed 42。需要补跑 seed 或修正标题。

报告已写入 `artifacts/p0_data_verification_report.md` 并注册。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0d570b2a-baf4-444d-913b-4aa819704e5d",
  "isSidechain": false,
  "requestId": "req_011CbC3vXiCKeVZYcELmF9xs",
  "type": "assistant",
  "uuid": "e226e4e6-4926-4f29-965b-e24814fb7651",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "a97de670-f9a7-4d30-affd-382982b8a334",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015wUWzKxy6EBiUrjgnF8T4E",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 702,
      "cache_read_input_tokens": 104656,
      "output_tokens": 416,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 702,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 416,
          "cache_read_input_tokens": 104656,
          "cache_creation_input_tokens": 702,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 702
          },
          "type": "message"
        }
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

_source line 110_

```json
{
  "type": "last-prompt",
  "leafUuid": "e226e4e6-4926-4f29-965b-e24814fb7651",
  "sessionId": "a97de670-f9a7-4d30-affd-382982b8a334"
}
```

---

### Runtime record

_source line 111_

```json
{
  "type": "ai-title",
  "aiTitle": "Audit data inconsistencies in paper tables",
  "sessionId": "a97de670-f9a7-4d30-affd-382982b8a334"
}
```

---
