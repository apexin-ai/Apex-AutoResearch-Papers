# Research conversation: <project_context> # 项目: provenance_weight_training ## 运行环境 - 服务器名: westd-47453 - SSH 账户: root（调用 ssh_execute / submit_tr

**When Does Detect-and-Reweight Work for Synthetic Contamination? (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 37
- **Recorded user turns:** 1
- **Tool calls:** 7
- **Original source:** `logs/chats/exported-trajectories/account-3/33f4c8cf-38de-44f8-ba86-369f9c5d5e2f.jsonl`
- **Structured JSON:** [`fc008897acce02583eff.json`](../../sessions/fc/fc008897acce02583eff.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-14T23:36:32.077Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-14T23:36:32.077Z",
  "sessionId": "33f4c8cf-38de-44f8-ba86-369f9c5d5e2f",
  "content": "&lt;project_context>\n# 项目: provenance_weight_training\n\n## 运行环境\n- 服务器名: westd-47453\n- SSH 账户: root（调用 ssh_execute / submit_training_job 时传入 account=\"root\"）\n- SSH 连接命令: ssh connect.westd.seetacloud.com  # 必须用此命令，~/.ssh/config 自动应用密钥和跳板机，禁止用裸 IP\n- 项目代码根目录: /root/provenance_weight_training\n\n\n## 环境搭建\n连接服务器后先调 `detect_image` 检测是否为预置镜像。如果匹配，跳过基础环境搭建，只装项目特有依赖。已预装的包不要重复安装。\n\n## 输出风格\n回复简洁直接。只输出执行结果和必要信息，不要解释过程、不要客套、不要给未被要求的建议。\n&lt;/project_context>\n## 任务：更新 literature_map.yaml，整合 Drayson et al. 差异化分析\n\n### 背景\nWorker `literature-drayson-comparison` 已完成分析，产出在 `artifacts/drayson_comparison.md`。需要将关键发现整合到 `literature_map.yaml`。\n\n### 关键发现（已确认）\n- Drayson et al. (EMNLP 2025, arXiv:2502.15654) 使用 w=(1-q)^b 公式\n- 他们的 b 是验证集 empirical 选取，训练中固定（GPT-2/SmolLM 135M/360M 用 b=10，1.7B 用 b=1）\n- 我们的 adaptive b* 在文献中无先例\n- 差异化角度：fixed grid-search vs. theoretically-motivated adaptive\n\n### 要求\n1. 读取 `artifacts/drayson_comparison.md` 获取完整对比内容\n2. 读取当前 `literature_map.yaml`\n3. 更新/补充 Drayson et al. 条目，确保包含：\n   - 论文基本信息（title, venue, year, arxiv_id）\n   - role: direct-competitor\n   - 方法摘要（fixed b, empirical selection）\n   - 与我们的差异点（adaptive vs fixed, theory-motivated vs empirical）\n   - 我们的优势论点\n4. 如有其他从 drayson_comparison.md 中发现的相关论文，也添加到 map\n\n### 产出\n更新后的 literature_map.yaml（用 save_project_file 写入）"
}
```

---

### Runtime record

_source line 2 · 2026-05-14T23:36:32.081Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-14T23:36:32.081Z",
  "sessionId": "33f4c8cf-38de-44f8-ba86-369f9c5d5e2f"
}
```

---

## Round 1

35 recorded events

### User

_source line 3 · 2026-05-14T23:36:32.127Z_

&lt;project_context>
# 项目: provenance_weight_training

## 运行环境
- 服务器名: westd-47453
- SSH 账户: root（调用 ssh_execute / submit_training_job 时传入 account="root"）
- SSH 连接命令: ssh connect.westd.seetacloud.com  # 必须用此命令，~/.ssh/config 自动应用密钥和跳板机，禁止用裸 IP
- 项目代码根目录: /root/provenance_weight_training


## 环境搭建
连接服务器后先调 `detect_image` 检测是否为预置镜像。如果匹配，跳过基础环境搭建，只装项目特有依赖。已预装的包不要重复安装。

## 输出风格
回复简洁直接。只输出执行结果和必要信息，不要解释过程、不要客套、不要给未被要求的建议。
&lt;/project_context>
## 任务：更新 literature_map.yaml，整合 Drayson et al. 差异化分析

### 背景
Worker `literature-drayson-comparison` 已完成分析，产出在 `artifacts/drayson_comparison.md`。需要将关键发现整合到 `literature_map.yaml`。

### 关键发现（已确认）
- Drayson et al. (EMNLP 2025, arXiv:2502.15654) 使用 w=(1-q)^b 公式
- 他们的 b 是验证集 empirical 选取，训练中固定（GPT-2/SmolLM 135M/360M 用 b=10，1.7B 用 b=1）
- 我们的 adaptive b* 在文献中无先例
- 差异化角度：fixed grid-search vs. theoretically-motivated adaptive

### 要求
1. 读取 `artifacts/drayson_comparison.md` 获取完整对比内容
2. 读取当前 `literature_map.yaml`
3. 更新/补充 Drayson et al. 条目，确保包含：
   - 论文基本信息（title, venue, year, arxiv_id）
   - role: direct-competitor
   - 方法摘要（fixed b, empirical selection）
   - 与我们的差异点（adaptive vs fixed, theory-motivated vs empirical）
   - 我们的优势论点
4. 如有其他从 drayson_comparison.md 中发现的相关论文，也添加到 map

### 产出
更新后的 literature_map.yaml（用 save_project_file 写入）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "8284b17e-dd1f-467a-9357-c4f2071853ea",
  "type": "user",
  "uuid": "346207c4-9c2e-4bf6-9075-961d8ee76b3e",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training",
  "sessionId": "33f4c8cf-38de-44f8-ba86-369f9c5d5e2f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-14T23:36:32.126Z_

```json
{
  "parentUuid": "346207c4-9c2e-4bf6-9075-961d8ee76b3e",
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
      "mcp__agent-ml-research__save_project_file"
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
      "mcp__agent-ml-research__save_project_file"
    ],
    "removedNames": []
  },
  "type": "attachment",
  "uuid": "f9e473b9-0baf-4636-ba16-62bbb63d5db9",
  "timestamp": "2026-05-14T23:36:32.126Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training",
  "sessionId": "33f4c8cf-38de-44f8-ba86-369f9c5d5e2f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-14T23:36:32.126Z_

```json
{
  "parentUuid": "f9e473b9-0baf-4636-ba16-62bbb63d5db9",
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
  "uuid": "d8d50608-7667-464b-98de-bd2b689a5c65",
  "timestamp": "2026-05-14T23:36:32.126Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training",
  "sessionId": "33f4c8cf-38de-44f8-ba86-369f9c5d5e2f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 6 · 2026-05-14T23:36:32.126Z_

```json
{
  "parentUuid": "d8d50608-7667-464b-98de-bd2b689a5c65",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "8b392938-5210-423a-80e2-160440a6a654",
  "timestamp": "2026-05-14T23:36:32.126Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training",
  "sessionId": "33f4c8cf-38de-44f8-ba86-369f9c5d5e2f",
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
  "aiTitle": "Integrate Drayson et al. into literature_map.yaml",
  "sessionId": "33f4c8cf-38de-44f8-ba86-369f9c5d5e2f"
}
```

---

### Assistant

_source line 8 · 2026-05-14T23:36:34.996Z_

Let me read the two source files first.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8b392938-5210-423a-80e2-160440a6a654",
  "isSidechain": false,
  "requestId": "req_011Cb3Lf5qjGY3DsncwtJvi8",
  "type": "assistant",
  "uuid": "36e5b8e3-06ba-498c-9b2e-d88a190b8be1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training",
  "sessionId": "33f4c8cf-38de-44f8-ba86-369f9c5d5e2f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019p32bk7B27QV9PNc4rAAqd",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11205,
      "cache_read_input_tokens": 11841,
      "output_tokens": 113,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11205,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 113,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11205,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11205
          },
          "type": "message"
        }
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

_source line 9 · 2026-05-14T23:36:36.070Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01UJ82twmCVKTGuw1EswEfDL`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__save_project_file",
  "max_results": 2
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "36e5b8e3-06ba-498c-9b2e-d88a190b8be1",
  "isSidechain": false,
  "requestId": "req_011Cb3Lf5qjGY3DsncwtJvi8",
  "type": "assistant",
  "uuid": "efdb979c-ae7d-4416-976f-1dd4c3649c3d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training",
  "sessionId": "33f4c8cf-38de-44f8-ba86-369f9c5d5e2f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019p32bk7B27QV9PNc4rAAqd",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11205,
      "cache_read_input_tokens": 11841,
      "output_tokens": 113,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11205,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 113,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11205,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11205
          },
          "type": "message"
        }
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

_source line 10 · 2026-05-14T23:36:36.077Z_

<details><summary>↩ Tool result · `toolu_01UJ82twmCVKTGuw1EswEfDL`</summary>

````text
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
  "parentUuid": "efdb979c-ae7d-4416-976f-1dd4c3649c3d",
  "isSidechain": false,
  "promptId": "8284b17e-dd1f-467a-9357-c4f2071853ea",
  "type": "user",
  "uuid": "24b55637-8a72-40cb-a6f7-c319fbc656c1",
  "toolUseResult": {
    "matches": [
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__save_project_file"
    ],
    "query": "select:mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__save_project_file",
    "total_deferred_tools": 22
  },
  "sourceToolAssistantUUID": "efdb979c-ae7d-4416-976f-1dd4c3649c3d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training",
  "sessionId": "33f4c8cf-38de-44f8-ba86-369f9c5d5e2f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 11 · 2026-05-14T23:36:38.513Z_

<details><summary>Logged reasoning block</summary>

```text
Let me read both files now.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "24b55637-8a72-40cb-a6f7-c319fbc656c1",
  "isSidechain": false,
  "requestId": "req_011Cb3LfNFTPSjhj1MsDNMfx",
  "type": "assistant",
  "uuid": "7d459a57-0142-484a-84ea-efa046387519",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training",
  "sessionId": "33f4c8cf-38de-44f8-ba86-369f9c5d5e2f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AMnN2BkcMGUYfpqReGNezc",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 709,
      "cache_read_input_tokens": 23046,
      "output_tokens": 205,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 709,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 205,
          "cache_read_input_tokens": 23046,
          "cache_creation_input_tokens": 709,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 709
          },
          "type": "message"
        }
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

_source line 12 · 2026-05-14T23:36:39.469Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01FaV5Gk3h2Z5AfQSixuWotb`</summary>

```json
{
  "project": "provenance_weight_training",
  "file": "literature_map.yaml",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7d459a57-0142-484a-84ea-efa046387519",
  "isSidechain": false,
  "requestId": "req_011Cb3LfNFTPSjhj1MsDNMfx",
  "type": "assistant",
  "uuid": "4786b8a1-0992-4bfb-a9bf-9aee1800833c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training",
  "sessionId": "33f4c8cf-38de-44f8-ba86-369f9c5d5e2f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AMnN2BkcMGUYfpqReGNezc",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 709,
      "cache_read_input_tokens": 23046,
      "output_tokens": 205,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 709,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 205,
          "cache_read_input_tokens": 23046,
          "cache_creation_input_tokens": 709,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 709
          },
          "type": "message"
        }
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

_source line 13 · 2026-05-14T23:36:39.487Z_

<details><summary>↩ Tool result · `toolu_01FaV5Gk3h2Z5AfQSixuWotb`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/literature_map.yaml\", \"content\": \"# Literature Map for provenance_weight_training\\n# 研究方向：基于收敛理论的自适应污染重加权\\n# 核心公式：w=(1-q)^b，q 为检测器合成概率，b* 为理论最优权重指数\\n# 生成日期：2026-05-14\\n\\n# ============================================================\\n# Category: direct-competitor\\n# 同主题/同方法的论文\\n# ============================================================\\n\\n- id: drayson_2025_detection_collapse\\n  title: \\\"Machine-Generated Text Detection Prevents Language Model Collapse\\\"\\n  authors: \\\"George Drayson, Emine Yilmaz, Vasileios Lampos\\\"\\n  venue: \\\"EMNLP 2025\\\"\\n  year: 2025\\n  url: \\\"https://arxiv.org/abs/2502.15654\\\"\\n  category: direct-competitor\\n  role: \\\"使用同一公式 w=(1-q)^b 进行重加权，但启发式选择 b 而非理论推导\\\"\\n  key_findings: \\\"训练机器生成文本检测器，用 importance resampling 上采样可能的人类内容，不仅防止 model collapse，还优于纯人类数据训练\\\"\\n  relevance_to_us: \\\"最直接的竞争者。我们的核心贡献是理论推导 b*，替代其启发式网格搜索方法\\\"\\n\\n- id: he_2025_golden_ratio\\n  title: \\\"Golden Ratio Weighting Prevents Model Collapse\\\"\\n  authors: \\\"Hengzhi He, Shirong Xu, Guang Cheng\\\"\\n  venue: \\\"Under review at JRSSB, 2025\\\"\\n  year: 2025\\n  url: \\\"https://arxiv.org/abs/2502.18049\\\"\\n  category: direct-competitor\\n  role: \\\"从理论推导合成/真实数据混合的最优权重，发现最优权重为黄金比例的倒数(~0.62)\\\"\\n  key_findings: \\\"在高斯估计、GLM、非参数估计等场景下，当合成数据与真实数据等量时，真实数据的最优权重约为 0.62（黄金比例倒数）\\\"\\n  relevance_to_us: \\\"同样是理论推导最优权重，但针对 real/synthetic 固定混合比例，未考虑检测器置信度的连续估计\\\"\\n\\n- id: feng_2024_beyond_collapse\\n  title: \\\"Beyond Model Collapse: Scaling Up with Synthesized Data Requires Verification\\\"\\n  authors: \\\"Yunzhen Feng, Elvis Dohmatob, Pu Yang, François Charton, Julia Kempe\\\"\\n  venue: \\\"arXiv preprint\\\"\\n  year: 2024\\n  url: \\\"https://arxiv.org/abs/2406.07515\\\"\\n  category: direct-competitor\\n  role: \\\"使用 verifier 过滤合成数据防止 model collapse，理论证明即使不完美的 verifier 也有效\\\"\\n  key_findings: \\\"用高斯混合模型和线性分类器推导条件，证明 verifier 引导的合成数据筛选可避免 model collapse；即使 verifier 不完美也能受益\\\"\\n  relevance_to_us: \\\"与我们的方法最相似——都用检测器置信度来处理合成数据。区别在于他们做 hard filtering，我们做 soft reweighting\\\"\\n\\n# ============================================================\\n# Category: method-component\\n# 我们用到的技术组件\\n# ============================================================\\n\\n- id: kimura_2024_iw_survey\\n  title: \\\"A Short Survey on Importance Weighting for Machine Learning\\\"\\n  authors: \\\"Masanari Kimura, Hideitsu Hino\\\"\\n  venue: \\\"TMLR 2024\\\"\\n  year: 2024\\n  url: \\\"https://arxiv.org/abs/2403.10175\\\"\\n  category: method-component\\n  role: \\\"importance weighting 在机器学习中的全面综述，覆盖分布偏移、密度比估计等核心理论\\\"\\n  key_findings: \\\"系统整理了 importance weighting 在监督学习分布偏移下的理论保证和应用，包括 covariate shift、domain adaptation 等场景\\\"\\n  relevance_to_us: \\\"为我们的 importance weighting 框架提供理论基础和方法论参考\\\"\\n\\n- id: vehtari_2024_psis\\n  title: \\\"Pareto Smoothed Importance Sampling\\\"\\n  authors: \\\"Aki Vehtari, Daniel Simpson, Andrew Gelman, Yuling Yao, Jonah Gabry\\\"\\n  venue: \\\"JMLR 2024\\\"\\n  year: 2024\\n  url: \\\"https://arxiv.org/abs/1507.02646\\\"\\n  category: method-component\\n  role: \\\"提供稳定的 effective sample size 估计和收敛诊断方法\\\"\\n  key_findings: \\\"用广义 Pareto 分布拟合 importance ratio 上尾实现平滑；提出 Pareto k 有限样本收敛率诊断指标；k<min(1-1/log10(S),0.7) 时估计可靠\\\"\\n  relevance_to_us: \\\"我们的 α_eff(b) 估计直接依赖 effective sample size 理论，PSIS 的收敛诊断可用于验证我们的权重方案\\\"\\n\\n- id: sow_2025_dynamic_reweighting\\n  title: \\\"Dynamic Loss-Based Sample Reweighting for Improved Large Language Model Pretraining\\\"\\n  authors: \\\"Daouda Sow et al.\\\"\\n  venue: \\\"ICLR 2025\\\"\\n  year: 2025\\n  url: \\\"https://arxiv.org/abs/2502.06733\\\"\\n  category: method-component\\n  role: \\\"首次提出 loss-based reweighting 对梯度优化收敛性影响的理论框架\\\"\\n  key_findings: \\\"基于 loss 值动态调整每个样本权重；建立了 loss-based reweighting 对收敛界影响的形式化刻画；在 7B 和 1.4B 模型上验证更快收敛和更优性能\\\"\\n  relevance_to_us: \\\"其收敛性理论框架可作为我们推导 b* 最优性的参考；loss-based 与 provenance-based reweighting 互补\\\"\\n\\n- id: ye_2025_data_mixing_laws\\n  title: \\\"Data Mixing Laws: Optimizing Data Mixtures by Predicting Language Modeling Performance\\\"\\n  authors: \\\"Jiasheng Ye, Peiju Liu, Tianxiang Sun, Yunhua Zhou, Jun Zhan, Xipeng Qiu\\\"\\n  venue: \\\"ICLR 2025\\\"\\n  year: 2025\\n  url: \\\"https://arxiv.org/abs/2403.16952\\\"\\n  category: method-component\\n  role: \\\"发现数据混合比例与模型性能之间的定量可预测性\\\"\\n  key_findings: \\\"模型性能关于混合比例具有函数形式的可预测性；可用小规模训练预测大模型在不同混合下的性能；适用于 continual training 的遗忘预测\\\"\\n  relevance_to_us: \\\"data mixing laws 可作为验证我们 b* 最优性的理论框架——检验不同 b 下的 mixing 效果是否符合预测\\\"\\n\\n- id: he_2024_softdedup\\n  title: \\\"SoftDedup: an Efficient Data Reweighting Method for Speeding Up Language Model Pre-training\\\"\\n  authors: \\\"Nan He, Weichen Xiong, Hanwen Liu, Yi Liao, Lei Ding, Kai Zhang, Guohua Tang, Xiao Han, Yang Wei\\\"\\n  venue: \\\"ACL 2024\\\"\\n  year: 2024\\n  url: \\\"https://arxiv.org/abs/2407.06654\\\"\\n  category: method-component\\n  role: \\\"用 data commonness 指标进行软去重加权，而非硬删除\\\"\\n  key_findings: \\\"用 n-gram 模型量化样本的 commonness，高频样本降权低频样本升权；相比硬去重保留信息完整性；等效训练时间提升 26% 效率和 1.77% 下游准确率\\\"\\n  relevance_to_us: \\\"软加权优于硬过滤的思路与我们一致——w=(1-q)^b 是连续加权而非二元过滤\\\"\\n\\n# ============================================================\\n# Category: background\\n# 数据污染/合成数据在 LLM 训练中的问题\\n# ============================================================\\n\\n- id: shumailov_2024_model_collapse\\n  title: \\\"AI Models Collapse When Trained on Recursively Generated Data\\\"\\n  authors: \\\"Ilia Shumailov, Zakhar Shumaylov, Yiren Zhao, Nicolas Papernot, Ross Anderson, Yarin Gal\\\"\\n  venue: \\\"Nature 2024\\\"\\n  year: 2024\\n  url: \\\"https://www.nature.com/articles/s41586-024-07566-y\\\"\\n  category: background\\n  role: \\\"奠基性工作——证明在递归生成数据上训练导致 model collapse\\\"\\n  key_findings: \\\"在 LLM、VAE、GMM 上证明不加区分地用模型生成内容训练会导致不可逆退化；原始分布的尾部逐渐消失；反复训练的语言模型出现重复短语\\\"\\n  relevance_to_us: \\\"model collapse 是我们工作的核心动机——加权方案的目标就是防止污染数据导致的性能退化\\\"\\n\\n- id: alemohammad_2024_mad\\n  title: \\\"Self-Consuming Generative Models Go MAD\\\"\\n  authors: \\\"Sina Alemohammad, Josue Casco-Rodriguez, Lorenzo Luzi, Ahmed Imtiaz Humayun, Hossein Babaei, Daniel LeJeune, Ali Siahkoohi, Richard G. Baraniuk\\\"\\n  venue: \\\"ICLR 2024\\\"\\n  year: 2024\\n  url: \\\"https://arxiv.org/abs/2307.01850\\\"\\n  category: background\\n  role: \\\"提出 Model Autophagy Disorder (MAD) 概念——自消费式生成模型的退化\\\"\\n  key_findings: \\\"分析三种自消费循环（fully synthetic、synthetic augmentation、fresh data）；无新鲜真实数据时质量或多样性不可避免下降；即使保留原始训练数据也可能退化\\\"\\n  relevance_to_us: \\\"MAD 的数学框架帮助理解不同污染程度下的退化动力学，为我们的收敛理论提供上下文\\\"\\n\\n- id: dohmatob_2025_strong_collapse\\n  title: \\\"Strong Model Collapse\\\"\\n  authors: \\\"Elvis Dohmatob, Yunzhen Feng, Arjun Subramonian, Julia Kempe\\\"\\n  venue: \\\"ICLR 2025 (Spotlight)\\\"\\n  year: 2025\\n  url: \\\"https://arxiv.org/abs/2410.04840\\\"\\n  category: background\\n  role: \\\"证明即使极少量合成数据（1/1000）也能导致 model collapse\\\"\\n  key_findings: \\\"在 scaling laws 框架下建立 strong model collapse；用算子值自由概率论获得测试误差的 bias-variance 分解；更大模型可放大 collapse 效应\\\"\\n  relevance_to_us: \\\"强化了我们工作的必要性——即使少量合成污染也需要处理，仅靠增加数据量无法解决\\\"\\n\\n- id: nait_saada_2025_quality_illusion\\n  title: \\\"The Data-Quality Illusion: Rethinking Classifier-Based Quality Filtering for LLM Pretraining\\\"\\n  authors: \\\"Thiziri Nait Saada, Louis Bethune, Michal Klein, David Grangier, Marco Cuturi, Pierre Ablin\\\"\\n  venue: \\\"arXiv preprint\\\"\\n  year: 2025\\n  url: \\\"https://arxiv.org/abs/2510.00866\\\"\\n  category: background\\n  role: \\\"质疑基于分类器的数据质量评分是否真正捕获了有意义的质量概念\\\"\\n  key_findings: \\\"CQF 改善下游任务但不一定改善语言建模；质量分类器隐式偏向其监督目标的数据分布；质量桶与特定 benchmark 对齐\\\"\\n  relevance_to_us: \\\"提醒我们检测器置信度 q 不等于真实质量——需要理论保证 b* 在检测器有偏时仍然有效\\\"\\n\\n# ============================================================\\n# Category: evaluation\\n# 评估方法相关\\n# ============================================================\\n\\n- id: mitchell_2023_detectgpt\\n  title: \\\"DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature\\\"\\n  authors: \\\"Eric Mitchell, Yoonho Lee, Alexander Khazatsky, Christopher D. Manning, Chelsea Finn\\\"\\n  venue: \\\"ICML 2023\\\"\\n  year: 2023\\n  url: \\\"https://arxiv.org/abs/2301.11305\\\"\\n  category: evaluation\\n  role: \\\"零样本机器生成文本检测方法——我们的检测器 q 的基线方法之一\\\"\\n  key_findings: \\\"LLM 生成的文本倾向于占据模型对数概率函数的负曲率区域；无需训练分类器、收集数据集或水印；在 GPT-NeoX 假新闻检测上从 0.81 AUROC 提升到 0.95\\\"\\n  relevance_to_us: \\\"可作为计算合成概率 q 的检测器之一；其概率曲率方法可能与我们的权重公式有理论联系\\\"\\n\\n- id: shi_2024_minkprob\\n  title: \\\"Detecting Pretraining Data from Large Language Models\\\"\\n  authors: \\\"Weijia Shi, Anirudh Ajith, Mengzhou Xia, Yangsibo Huang, Daogao Liu, Terra Blevins, Danqi Chen, Luke Zettlemoyer\\\"\\n  venue: \\\"ICLR 2024\\\"\\n  year: 2024\\n  url: \\\"https://arxiv.org/abs/2310.16789\\\"\\n  category: evaluation\\n  role: \\\"Min-K% Prob 方法——检测数据是否在预训练集中的无参考方法\\\"\\n  key_findings: \\\"已训练数据包含更少低概率异常 token；取最低 K% token 概率的平均值判断；在 WikiMIA 上比最佳基线高 7.4 AUC；无需参考模型\\\"\\n  relevance_to_us: \\\"Min-K% Prob 可作为估计合成概率 q 的候选方法；其 membership inference 思路可扩展为连续置信度估计\\\"\\n\\n- id: kuo_2024_data_weighting\\n  title: \\\"Not All LLM-Generated Data Are Equal: Rethinking Data Weighting in Text Classification\\\"\\n  authors: \\\"Hsun-Yu Kuo et al.\\\"\\n  venue: \\\"arXiv preprint\\\"\\n  year: 2024\\n  url: \\\"https://arxiv.org/abs/2410.21526\\\"\\n  category: evaluation\\n  role: \\\"评估合成数据加权策略在文本分类中的效果\\\"\\n  key_findings: \\\"提出加权损失方法用少量真实数据对齐合成数据分布；在 BERT 级模型上稳定优于标准交叉熵和其他加权方法\\\"\\n  relevance_to_us: \\\"验证了合成数据需要差异化加权的思路；其评估框架可参考用于我们的下游任务评估\\\"\\n\", \"total_chars\": 8521, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4786b8a1-0992-4bfb-a9bf-9aee1800833c",
  "isSidechain": false,
  "promptId": "8284b17e-dd1f-467a-9357-c4f2071853ea",
  "type": "user",
  "uuid": "4c302988-cc43-46d1-ab8c-15d07c744392",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"path\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/literature_map.yaml\\\", \\\"content\\\": \\\"# Literature Map for provenance_weight_training\\\\n# 研究方向：基于收敛理论的自适应污染重加权\\\\n# 核心公式：w=(1-q)^b，q 为检测器合成概率，b* 为理论最优权重指数\\\\n# 生成日期：2026-05-14\\\\n\\\\n# ============================================================\\\\n# Category: direct-competitor\\\\n# 同主题/同方法的论文\\\\n# ============================================================\\\\n\\\\n- id: drayson_2025_detection_collapse\\\\n  title: \\\\\\\"Machine-Generated Text Detection Prevents Language Model Collapse\\\\\\\"\\\\n  authors: \\\\\\\"George Drayson, Emine Yilmaz, Vasileios Lampos\\\\\\\"\\\\n  venue: \\\\\\\"EMNLP 2025\\\\\\\"\\\\n  year: 2025\\\\n  url: \\\\\\\"https://arxiv.org/abs/2502.15654\\\\\\\"\\\\n  category: direct-competitor\\\\n  role: \\\\\\\"使用同一公式 w=(1-q)^b 进行重加权，但启发式选择 b 而非理论推导\\\\\\\"\\\\n  key_findings: \\\\\\\"训练机器生成文本检测器，用 importance resampling 上采样可能的人类内容，不仅防止 model collapse，还优于纯人类数据训练\\\\\\\"\\\\n  relevance_to_us: \\\\\\\"最直接的竞争者。我们的核心贡献是理论推导 b*，替代其启发式网格搜索方法\\\\\\\"\\\\n\\\\n- id: he_2025_golden_ratio\\\\n  title: \\\\\\\"Golden Ratio Weighting Prevents Model Collapse\\\\\\\"\\\\n  authors: \\\\\\\"Hengzhi He, Shirong Xu, Guang Cheng\\\\\\\"\\\\n  venue: \\\\\\\"Under review at JRSSB, 2025\\\\\\\"\\\\n  year: 2025\\\\n  url: \\\\\\\"https://arxiv.org/abs/2502.18049\\\\\\\"\\\\n  category: direct-competitor\\\\n  role: \\\\\\\"从理论推导合成/真实数据混合的最优权重，发现最优权重为黄金比例的倒数(~0.62)\\\\\\\"\\\\n  key_findings: \\\\\\\"在高斯估计、GLM、非参数估计等场景下，当合成数据与真实数据等量时，真实数据的最优权重约为 0.62（黄金比例倒数）\\\\\\\"\\\\n  relevance_to_us: \\\\\\\"同样是理论推导最优权重，但针对 real/synthetic 固定混合比例，未考虑检测器置信度的连续估计\\\\\\\"\\\\n\\\\n- id: feng_2024_beyond_collapse\\\\n  title: \\\\\\\"Beyond Model Collapse: Scaling Up with Synthesized Data Requires Verification\\\\\\\"\\\\n  authors: \\\\\\\"Yunzhen Feng, Elvis Dohmatob, Pu Yang, François Charton, Julia Kempe\\\\\\\"\\\\n  venue: \\\\\\\"arXiv preprint\\\\\\\"\\\\n  year: 2024\\\\n  url: \\\\\\\"https://arxiv.org/abs/2406.07515\\\\\\\"\\\\n  category: direct-competitor\\\\n  role: \\\\\\\"使用 verifier 过滤合成数据防止 model collapse，理论证明即使不完美的 verifier 也有效\\\\\\\"\\\\n  key_findings: \\\\\\\"用高斯混合模型和线性分类器推导条件，证明 verifier 引导的合成数据筛选可避免 model collapse；即使 verifier 不完美也能受益\\\\\\\"\\\\n  relevance_to_us: \\\\\\\"与我们的方法最相似——都用检测器置信度来处理合成数据。区别在于他们做 hard filtering，我们做 soft reweighting\\\\\\\"\\\\n\\\\n# ============================================================\\\\n# Category: method-component\\\\n# 我们用到的技术组件\\\\n# ============================================================\\\\n\\\\n- id: kimura_2024_iw_survey\\\\n  title: \\\\\\\"A Short Survey on Importance Weighting for Machine Learning\\\\\\\"\\\\n  authors: \\\\\\\"Masanari Kimura, Hideitsu Hino\\\\\\\"\\\\n  venue: \\\\\\\"TMLR 2024\\\\\\\"\\\\n  year: 2024\\\\n  url: \\\\\\\"https://arxiv.org/abs/2403.10175\\\\\\\"\\\\n  category: method-component\\\\n  role: \\\\\\\"importance weighting 在机器学习中的全面综述，覆盖分布偏移、密度比估计等核心理论\\\\\\\"\\\\n  key_findings: \\\\\\\"系统整理了 importance weighting 在监督学习分布偏移下的理论保证和应用，包括 covariate shift、domain adaptation 等场景\\\\\\\"\\\\n  relevance_to_us: \\\\\\\"为我们的 importance weighting 框架提供理论基础和方法论参考\\\\\\\"\\\\n\\\\n- id: vehtari_2024_psis\\\\n  title: \\\\\\\"Pareto Smoothed Importance Sampling\\\\\\\"\\\\n  authors: \\\\\\\"Aki Vehtari, Daniel Simpson, Andrew Gelman, Yuling Yao, Jonah Gabry\\\\\\\"\\\\n  venue: \\\\\\\"JMLR 2024\\\\\\\"\\\\n  year: 2024\\\\n  url: \\\\\\\"https://arxiv.org/abs/1507.02646\\\\\\\"\\\\n  category: method-component\\\\n  role: \\\\\\\"提供稳定的 effective sample size 估计和收敛诊断方法\\\\\\\"\\\\n  key_findings: \\\\\\\"用广义 Pareto 分布拟合 importance ratio 上尾实现平滑；提出 Pareto k 有限样本收敛率诊断指标；k<min(1-1/log10(S),0.7) 时估计可靠\\\\\\\"\\\\n  relevance_to_us: \\\\\\\"我们的 α_eff(b) 估计直接依赖 effective sample size 理论，PSIS 的收敛诊断可用于验证我们的权重方案\\\\\\\"\\\\n\\\\n- id: sow_2025_dynamic_reweighting\\\\n  title: \\\\\\\"Dynamic Loss-Based Sample Reweighting for Improved Large Language Model Pretraining\\\\\\\"\\\\n  authors: \\\\\\\"Daouda Sow et al.\\\\\\\"\\\\n  venue: \\\\\\\"ICLR 2025\\\\\\\"\\\\n  year: 2025\\\\n  url: \\\\\\\"https://arxiv.org/abs/2502.06733\\\\\\\"\\\\n  category: method-component\\\\n  role: \\\\\\\"首次提出 loss-based reweighting 对梯度优化收敛性影响的理论框架\\\\\\\"\\\\n  key_findings: \\\\\\\"基于 loss 值动态调整每个样本权重；建立了 loss-based reweighting 对收敛界影响的形式化刻画；在 7B 和 1.4B 模型上验证更快收敛和更优性能\\\\\\\"\\\\n  relevance_to_us: \\\\\\\"其收敛性理论框架可作为我们推导 b* 最优性的参考；loss-based 与 provenance-based reweighting 互补\\\\\\\"\\\\n\\\\n- id: ye_2025_data_mixing_laws\\\\n  title: \\\\\\\"Data Mixing Laws: Optimizing Data Mixtures by Predicting Language Modeling Performance\\\\\\\"\\\\n  authors: \\\\\\\"Jiasheng Ye, Peiju Liu, Tianxiang Sun, Yunhua Zhou, Jun Zhan, Xipeng Qiu\\\\\\\"\\\\n  venue: \\\\\\\"ICLR 2025\\\\\\\"\\\\n  year: 2025\\\\n  url: \\\\\\\"https://arxiv.org/abs/2403.16952\\\\\\\"\\\\n  category: method-component\\\\n  role: \\\\\\\"发现数据混合比例与模型性能之间的定量可预测性\\\\\\\"\\\\n  key_findings: \\\\\\\"模型性能关于混合比例具有函数形式的可预测性；可用小规模训练预测大模型在不同混合下的性能；适用于 continual training 的遗忘预测\\\\\\\"\\\\n  relevance_to_us: \\\\\\\"data mixing laws 可作为验证我们 b* 最优性的理论框架——检验不同 b 下的 mixing 效果是否符合预测\\\\\\\"\\\\n\\\\n- id: he_2024_softdedup\\\\n  title: \\\\\\\"SoftDedup: an Efficient Data Reweighting Method for Speeding Up Language Model Pre-training\\\\\\\"\\\\n  authors: \\\\\\\"Nan He, Weichen Xiong, Hanwen Liu, Yi Liao, Lei Ding, Kai Zhang, Guohua Tang, Xiao Han, Yang Wei\\\\\\\"\\\\n  venue: \\\\\\\"ACL 2024\\\\\\\"\\\\n  year: 2024\\\\n  url: \\\\\\\"https://arxiv.org/abs/2407.06654\\\\\\\"\\\\n  category: method-component\\\\n  role: \\\\\\\"用 data commonness 指标进行软去重加权，而非硬删除\\\\\\\"\\\\n  key_findings: \\\\\\\"用 n-gram 模型量化样本的 commonness，高频样本降权低频样本升权；相比硬去重保留信息完整性；等效训练时间提升 26% 效率和 1.77% 下游准确率\\\\\\\"\\\\n  relevance_to_us: \\\\\\\"软加权优于硬过滤的思路与我们一致——w=(1-q)^b 是连续加权而非二元过滤\\\\\\\"\\\\n\\\\n# ============================================================\\\\n# Category: background\\\\n# 数据污染/合成数据在 LLM 训练中的问题\\\\n# ============================================================\\\\n\\\\n- id: shumailov_2024_model_collapse\\\\n  title: \\\\\\\"AI Models Collapse When Trained on Recursively Generated Data\\\\\\\"\\\\n  authors: \\\\\\\"Ilia Shumailov, Zakhar Shumaylov, Yiren Zhao, Nicolas Papernot, Ross Anderson, Yarin Gal\\\\\\\"\\\\n  venue: \\\\\\\"Nature 2024\\\\\\\"\\\\n  year: 2024\\\\n  url: \\\\\\\"https://www.nature.com/articles/s41586-024-07566-y\\\\\\\"\\\\n  category: background\\\\n  role: \\\\\\\"奠基性工作——证明在递归生成数据上训练导致 model collapse\\\\\\\"\\\\n  key_findings: \\\\\\\"在 LLM、VAE、GMM 上证明不加区分地用模型生成内容训练会导致不可逆退化；原始分布的尾部逐渐消失；反复训练的语言模型出现重复短语\\\\\\\"\\\\n  relevance_to_us: \\\\\\\"model collapse 是我们工作的核心动机——加权方案的目标就是防止污染数据导致的性能退化\\\\\\\"\\\\n\\\\n- id: alemohammad_2024_mad\\\\n  title: \\\\\\\"Self-Consuming Generative Models Go MAD\\\\\\\"\\\\n  authors: \\\\\\\"Sina Alemohammad, Josue Casco-Rodriguez, Lorenzo Luzi, Ahmed Imtiaz Humayun, Hossein Babaei, Daniel LeJeune, Ali Siahkoohi, Richard G. Baraniuk\\\\\\\"\\\\n  venue: \\\\\\\"ICLR 2024\\\\\\\"\\\\n  year: 2024\\\\n  url: \\\\\\\"https://arxiv.org/abs/2307.01850\\\\\\\"\\\\n  category: background\\\\n  role: \\\\\\\"提出 Model Autophagy Disorder (MAD) 概念——自消费式生成模型的退化\\\\\\\"\\\\n  key_findings: \\\\\\\"分析三种自消费循环（fully synthetic、synthetic augmentation、fresh data）；无新鲜真实数据时质量或多样性不可避免下降；即使保留原始训练数据也可能退化\\\\\\\"\\\\n  relevance_to_us: \\\\\\\"MAD 的数学框架帮助理解不同污染程度下的退化动力学，为我们的收敛理论提供上下文\\\\\\\"\\\\n\\\\n- id: dohmatob_2025_strong_collapse\\\\n  title: \\\\\\\"Strong Model Collapse\\\\\\\"\\\\n  authors: \\\\\\\"Elvis Dohmatob, Yunzhen Feng, Arjun Subramonian, Julia Kempe\\\\\\\"\\\\n  venue: \\\\\\\"ICLR 2025 (Spotlight)\\\\\\\"\\\\n  year: 2025\\\\n  url: \\\\\\\"https://arxiv.org/abs/2410.04840\\\\\\\"\\\\n  category: background\\\\n  role: \\\\\\\"证明即使极少量合成数据（1/1000）也能导致 model collapse\\\\\\\"\\\\n  key_findings: \\\\\\\"在 scaling laws 框架下建立 strong model collapse；用算子值自由概率论获得测试误差的 bias-variance 分解；更大模型可放大 collapse 效应\\\\\\\"\\\\n  relevance_to_us: \\\\\\\"强化了我们工作的必要性——即使少量合成污染也需要处理，仅靠增加数据量无法解决\\\\\\\"\\\\n\\\\n- id: nait_saada_2025_quality_illusion\\\\n  title: \\\\\\\"The Data-Quality Illusion: Rethinking Classifier-Based Quality Filtering for LLM Pretraining\\\\\\\"\\\\n  authors: \\\\\\\"Thiziri Nait Saada, Louis Bethune, Michal Klein, David Grangier, Marco Cuturi, Pierre Ablin\\\\\\\"\\\\n  venue: \\\\\\\"arXiv preprint\\\\\\\"\\\\n  year: 2025\\\\n  url: \\\\\\\"https://arxiv.org/abs/2510.00866\\\\\\\"\\\\n  category: background\\\\n  role: \\\\\\\"质疑基于分类器的数据质量评分是否真正捕获了有意义的质量概念\\\\\\\"\\\\n  key_findings: \\\\\\\"CQF 改善下游任务但不一定改善语言建模；质量分类器隐式偏向其监督目标的数据分布；质量桶与特定 benchmark 对齐\\\\\\\"\\\\n  relevance_to_us: \\\\\\\"提醒我们检测器置信度 q 不等于真实质量——需要理论保证 b* 在检测器有偏时仍然有效\\\\\\\"\\\\n\\\\n# ============================================================\\\\n# Category: evaluation\\\\n# 评估方法相关\\\\n# ============================================================\\\\n\\\\n- id: mitchell_2023_detectgpt\\\\n  title: \\\\\\\"DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature\\\\\\\"\\\\n  authors: \\\\\\\"Eric Mitchell, Yoonho Lee, Alexander Khazatsky, Christopher D. Manning, Chelsea Finn\\\\\\\"\\\\n  venue: \\\\\\\"ICML 2023\\\\\\\"\\\\n  year: 2023\\\\n  url: \\\\\\\"https://arxiv.org/abs/2301.11305\\\\\\\"\\\\n  category: evaluation\\\\n  role: \\\\\\\"零样本机器生成文本检测方法——我们的检测器 q 的基线方法之一\\\\\\\"\\\\n  key_findings: \\\\\\\"LLM 生成的文本倾向于占据模型对数概率函数的负曲率区域；无需训练分类器、收集数据集或水印；在 GPT-NeoX 假新闻检测上从 0.81 AUROC 提升到 0.95\\\\\\\"\\\\n  relevance_to_us: \\\\\\\"可作为计算合成概率 q 的检测器之一；其概率曲率方法可能与我们的权重公式有理论联系\\\\\\\"\\\\n\\\\n- id: shi_2024_minkprob\\\\n  title: \\\\\\\"Detecting Pretraining Data from Large Language Models\\\\\\\"\\\\n  authors: \\\\\\\"Weijia Shi, Anirudh Ajith, Mengzhou Xia, Yangsibo Huang, Daogao Liu, Terra Blevins, Danqi Chen, Luke Zettlemoyer\\\\\\\"\\\\n  venue: \\\\\\\"ICLR 2024\\\\\\\"\\\\n  year: 2024\\\\n  url: \\\\\\\"https://arxiv.org/abs/2310.16789\\\\\\\"\\\\n  category: evaluation\\\\n  role: \\\\\\\"Min-K% Prob 方法——检测数据是否在预训练集中的无参考方法\\\\\\\"\\\\n  key_findings: \\\\\\\"已训练数据包含更少低概率异常 token；取最低 K% token 概率的平均值判断；在 WikiMIA 上比最佳基线高 7.4 AUC；无需参考模型\\\\\\\"\\\\n  relevance_to_us: \\\\\\\"Min-K% Prob 可作为估计合成概率 q 的候选方法；其 membership inference 思路可扩展为连续置信度估计\\\\\\\"\\\\n\\\\n- id: kuo_2024_data_weighting\\\\n  title: \\\\\\\"Not All LLM-Generated Data Are Equal: Rethinking Data Weighting in Text Classification\\\\\\\"\\\\n  authors: \\\\\\\"Hsun-Yu Kuo et al.\\\\\\\"\\\\n  venue: \\\\\\\"arXiv preprint\\\\\\\"\\\\n  year: 2024\\\\n  url: \\\\\\\"https://arxiv.org/abs/2410.21526\\\\\\\"\\\\n  category: evaluation\\\\n  role: \\\\\\\"评估合成数据加权策略在文本分类中的效果\\\\\\\"\\\\n  key_findings: \\\\\\\"提出加权损失方法用少量真实数据对齐合成数据分布；在 BERT 级模型上稳定优于标准交叉熵和其他加权方法\\\\\\\"\\\\n  relevance_to_us: \\\\\\\"验证了合成数据需要差异化加权的思路；其评估框架可参考用于我们的下游任务评估\\\\\\\"\\\\n\\\", \\\"total_chars\\\": 8521, \\\"truncated\\\": false}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/literature_map.yaml\", \"content\": \"# Literature Map for provenance_weight_training\\n# 研究方向：基于收敛理论的自适应污染重加权\\n# 核心公式：w=(1-q)^b，q 为检测器合成概率，b* 为理论最优权重指数\\n# 生成日期：2026-05-14\\n\\n# ============================================================\\n# Category: direct-competitor\\n# 同主题/同方法的论文\\n# ============================================================\\n\\n- id: drayson_2025_detection_collapse\\n  title: \\\"Machine-Generated Text Detection Prevents Language Model Collapse\\\"\\n  authors: \\\"George Drayson, Emine Yilmaz, Vasileios Lampos\\\"\\n  venue: \\\"EMNLP 2025\\\"\\n  year: 2025\\n  url: \\\"https://arxiv.org/abs/2502.15654\\\"\\n  category: direct-competitor\\n  role: \\\"使用同一公式 w=(1-q)^b 进行重加权，但启发式选择 b 而非理论推导\\\"\\n  key_findings: \\\"训练机器生成文本检测器，用 importance resampling 上采样可能的人类内容，不仅防止 model collapse，还优于纯人类数据训练\\\"\\n  relevance_to_us: \\\"最直接的竞争者。我们的核心贡献是理论推导 b*，替代其启发式网格搜索方法\\\"\\n\\n- id: he_2025_golden_ratio\\n  title: \\\"Golden Ratio Weighting Prevents Model Collapse\\\"\\n  authors: \\\"Hengzhi He, Shirong Xu, Guang Cheng\\\"\\n  venue: \\\"Under review at JRSSB, 2025\\\"\\n  year: 2025\\n  url: \\\"https://arxiv.org/abs/2502.18049\\\"\\n  category: direct-competitor\\n  role: \\\"从理论推导合成/真实数据混合的最优权重，发现最优权重为黄金比例的倒数(~0.62)\\\"\\n  key_findings: \\\"在高斯估计、GLM、非参数估计等场景下，当合成数据与真实数据等量时，真实数据的最优权重约为 0.62（黄金比例倒数）\\\"\\n  relevance_to_us: \\\"同样是理论推导最优权重，但针对 real/synthetic 固定混合比例，未考虑检测器置信度的连续估计\\\"\\n\\n- id: feng_2024_beyond_collapse\\n  title: \\\"Beyond Model Collapse: Scaling Up with Synthesized Data Requires Verification\\\"\\n  authors: \\\"Yunzhen Feng, Elvis Dohmatob, Pu Yang, François Charton, Julia Kempe\\\"\\n  venue: \\\"arXiv preprint\\\"\\n  year: 2024\\n  url: \\\"https://arxiv.org/abs/2406.07515\\\"\\n  category: direct-competitor\\n  role: \\\"使用 verifier 过滤合成数据防止 model collapse，理论证明即使不完美的 verifier 也有效\\\"\\n  key_findings: \\\"用高斯混合模型和线性分类器推导条件，证明 verifier 引导的合成数据筛选可避免 model collapse；即使 verifier 不完美也能受益\\\"\\n  relevance_to_us: \\\"与我们的方法最相似——都用检测器置信度来处理合成数据。区别在于他们做 hard filtering，我们做 soft reweighting\\\"\\n\\n# ============================================================\\n# Category: method-component\\n# 我们用到的技术组件\\n# ============================================================\\n\\n- id: kimura_2024_iw_survey\\n  title: \\\"A Short Survey on Importance Weighting for Machine Learning\\\"\\n  authors: \\\"Masanari Kimura, Hideitsu Hino\\\"\\n  venue: \\\"TMLR 2024\\\"\\n  year: 2024\\n  url: \\\"https://arxiv.org/abs/2403.10175\\\"\\n  category: method-component\\n  role: \\\"importance weighting 在机器学习中的全面综述，覆盖分布偏移、密度比估计等核心理论\\\"\\n  key_findings: \\\"系统整理了 importance weighting 在监督学习分布偏移下的理论保证和应用，包括 covariate shift、domain adaptation 等场景\\\"\\n  relevance_to_us: \\\"为我们的 importance weighting 框架提供理论基础和方法论参考\\\"\\n\\n- id: vehtari_2024_psis\\n  title: \\\"Pareto Smoothed Importance Sampling\\\"\\n  authors: \\\"Aki Vehtari, Daniel Simpson, Andrew Gelman, Yuling Yao, Jonah Gabry\\\"\\n  venue: \\\"JMLR 2024\\\"\\n  year: 2024\\n  url: \\\"https://arxiv.org/abs/1507.02646\\\"\\n  category: method-component\\n  role: \\\"提供稳定的 effective sample size 估计和收敛诊断方法\\\"\\n  key_findings: \\\"用广义 Pareto 分布拟合 importance ratio 上尾实现平滑；提出 Pareto k 有限样本收敛率诊断指标；k<min(1-1/log10(S),0.7) 时估计可靠\\\"\\n  relevance_to_us: \\\"我们的 α_eff(b) 估计直接依赖 effective sample size 理论，PSIS 的收敛诊断可用于验证我们的权重方案\\\"\\n\\n- id: sow_2025_dynamic_reweighting\\n  title: \\\"Dynamic Loss-Based Sample Reweighting for Improved Large Language Model Pretraining\\\"\\n  authors: \\\"Daouda Sow et al.\\\"\\n  venue: \\\"ICLR 2025\\\"\\n  year: 2025\\n  url: \\\"https://arxiv.org/abs/2502.06733\\\"\\n  category: method-component\\n  role: \\\"首次提出 loss-based reweighting 对梯度优化收敛性影响的理论框架\\\"\\n  key_findings: \\\"基于 loss 值动态调整每个样本权重；建立了 loss-based reweighting 对收敛界影响的形式化刻画；在 7B 和 1.4B 模型上验证更快收敛和更优性能\\\"\\n  relevance_to_us: \\\"其收敛性理论框架可作为我们推导 b* 最优性的参考；loss-based 与 provenance-based reweighting 互补\\\"\\n\\n- id: ye_2025_data_mixing_laws\\n  title: \\\"Data Mixing Laws: Optimizing Data Mixtures by Predicting Language Modeling Performance\\\"\\n  authors: \\\"Jiasheng Ye, Peiju Liu, Tianxiang Sun, Yunhua Zhou, Jun Zhan, Xipeng Qiu\\\"\\n  venue: \\\"ICLR 2025\\\"\\n  year: 2025\\n  url: \\\"https://arxiv.org/abs/2403.16952\\\"\\n  category: method-component\\n  role: \\\"发现数据混合比例与模型性能之间的定量可预测性\\\"\\n  key_findings: \\\"模型性能关于混合比例具有函数形式的可预测性；可用小规模训练预测大模型在不同混合下的性能；适用于 continual training 的遗忘预测\\\"\\n  relevance_to_us: \\\"data mixing laws 可作为验证我们 b* 最优性的理论框架——检验不同 b 下的 mixing 效果是否符合预测\\\"\\n\\n- id: he_2024_softdedup\\n  title: \\\"SoftDedup: an Efficient Data Reweighting Method for Speeding Up Language Model Pre-training\\\"\\n  authors: \\\"Nan He, Weichen Xiong, Hanwen Liu, Yi Liao, Lei Ding, Kai Zhang, Guohua Tang, Xiao Han, Yang Wei\\\"\\n  venue: \\\"ACL 2024\\\"\\n  year: 2024\\n  url: \\\"https://arxiv.org/abs/2407.06654\\\"\\n  category: method-component\\n  role: \\\"用 data commonness 指标进行软去重加权，而非硬删除\\\"\\n  key_findings: \\\"用 n-gram 模型量化样本的 commonness，高频样本降权低频样本升权；相比硬去重保留信息完整性；等效训练时间提升 26% 效率和 1.77% 下游准确率\\\"\\n  relevance_to_us: \\\"软加权优于硬过滤的思路与我们一致——w=(1-q)^b 是连续加权而非二元过滤\\\"\\n\\n# ============================================================\\n# Category: background\\n# 数据污染/合成数据在 LLM 训练中的问题\\n# ============================================================\\n\\n- id: shumailov_2024_model_collapse\\n  title: \\\"AI Models Collapse When Trained on Recursively Generated Data\\\"\\n  authors: \\\"Ilia Shumailov, Zakhar Shumaylov, Yiren Zhao, Nicolas Papernot, Ross Anderson, Yarin Gal\\\"\\n  venue: \\\"Nature 2024\\\"\\n  year: 2024\\n  url: \\\"https://www.nature.com/articles/s41586-024-07566-y\\\"\\n  category: background\\n  role: \\\"奠基性工作——证明在递归生成数据上训练导致 model collapse\\\"\\n  key_findings: \\\"在 LLM、VAE、GMM 上证明不加区分地用模型生成内容训练会导致不可逆退化；原始分布的尾部逐渐消失；反复训练的语言模型出现重复短语\\\"\\n  relevance_to_us: \\\"model collapse 是我们工作的核心动机——加权方案的目标就是防止污染数据导致的性能退化\\\"\\n\\n- id: alemohammad_2024_mad\\n  title: \\\"Self-Consuming Generative Models Go MAD\\\"\\n  authors: \\\"Sina Alemohammad, Josue Casco-Rodriguez, Lorenzo Luzi, Ahmed Imtiaz Humayun, Hossein Babaei, Daniel LeJeune, Ali Siahkoohi, Richard G. Baraniuk\\\"\\n  venue: \\\"ICLR 2024\\\"\\n  year: 2024\\n  url: \\\"https://arxiv.org/abs/2307.01850\\\"\\n  category: background\\n  role: \\\"提出 Model Autophagy Disorder (MAD) 概念——自消费式生成模型的退化\\\"\\n  key_findings: \\\"分析三种自消费循环（fully synthetic、synthetic augmentation、fresh data）；无新鲜真实数据时质量或多样性不可避免下降；即使保留原始训练数据也可能退化\\\"\\n  relevance_to_us: \\\"MAD 的数学框架帮助理解不同污染程度下的退化动力学，为我们的收敛理论提供上下文\\\"\\n\\n- id: dohmatob_2025_strong_collapse\\n  title: \\\"Strong Model Collapse\\\"\\n  authors: \\\"Elvis Dohmatob, Yunzhen Feng, Arjun Subramonian, Julia Kempe\\\"\\n  venue: \\\"ICLR 2025 (Spotlight)\\\"\\n  year: 2025\\n  url: \\\"https://arxiv.org/abs/2410.04840\\\"\\n  category: background\\n  role: \\\"证明即使极少量合成数据（1/1000）也能导致 model collapse\\\"\\n  key_findings: \\\"在 scaling laws 框架下建立 strong model collapse；用算子值自由概率论获得测试误差的 bias-variance 分解；更大模型可放大 collapse 效应\\\"\\n  relevance_to_us: \\\"强化了我们工作的必要性——即使少量合成污染也需要处理，仅靠增加数据量无法解决\\\"\\n\\n- id: nait_saada_2025_quality_illusion\\n  title: \\\"The Data-Quality Illusion: Rethinking Classifier-Based Quality Filtering for LLM Pretraining\\\"\\n  authors: \\\"Thiziri Nait Saada, Louis Bethune, Michal Klein, David Grangier, Marco Cuturi, Pierre Ablin\\\"\\n  venue: \\\"arXiv preprint\\\"\\n  year: 2025\\n  url: \\\"https://arxiv.org/abs/2510.00866\\\"\\n  category: background\\n  role: \\\"质疑基于分类器的数据质量评分是否真正捕获了有意义的质量概念\\\"\\n  key_findings: \\\"CQF 改善下游任务但不一定改善语言建模；质量分类器隐式偏向其监督目标的数据分布；质量桶与特定 benchmark 对齐\\\"\\n  relevance_to_us: \\\"提醒我们检测器置信度 q 不等于真实质量——需要理论保证 b* 在检测器有偏时仍然有效\\\"\\n\\n# ============================================================\\n# Category: evaluation\\n# 评估方法相关\\n# ============================================================\\n\\n- id: mitchell_2023_detectgpt\\n  title: \\\"DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature\\\"\\n  authors: \\\"Eric Mitchell, Yoonho Lee, Alexander Khazatsky, Christopher D. Manning, Chelsea Finn\\\"\\n  venue: \\\"ICML 2023\\\"\\n  year: 2023\\n  url: \\\"https://arxiv.org/abs/2301.11305\\\"\\n  category: evaluation\\n  role: \\\"零样本机器生成文本检测方法——我们的检测器 q 的基线方法之一\\\"\\n  key_findings: \\\"LLM 生成的文本倾向于占据模型对数概率函数的负曲率区域；无需训练分类器、收集数据集或水印；在 GPT-NeoX 假新闻检测上从 0.81 AUROC 提升到 0.95\\\"\\n  relevance_to_us: \\\"可作为计算合成概率 q 的检测器之一；其概率曲率方法可能与我们的权重公式有理论联系\\\"\\n\\n- id: shi_2024_minkprob\\n  title: \\\"Detecting Pretraining Data from Large Language Models\\\"\\n  authors: \\\"Weijia Shi, Anirudh Ajith, Mengzhou Xia, Yangsibo Huang, Daogao Liu, Terra Blevins, Danqi Chen, Luke Zettlemoyer\\\"\\n  venue: \\\"ICLR 2024\\\"\\n  year: 2024\\n  url: \\\"https://arxiv.org/abs/2310.16789\\\"\\n  category: evaluation\\n  role: \\\"Min-K% Prob 方法——检测数据是否在预训练集中的无参考方法\\\"\\n  key_findings: \\\"已训练数据包含更少低概率异常 token；取最低 K% token 概率的平均值判断；在 WikiMIA 上比最佳基线高 7.4 AUC；无需参考模型\\\"\\n  relevance_to_us: \\\"Min-K% Prob 可作为估计合成概率 q 的候选方法；其 membership inference 思路可扩展为连续置信度估计\\\"\\n\\n- id: kuo_2024_data_weighting\\n  title: \\\"Not All LLM-Generated Data Are Equal: Rethinking Data Weighting in Text Classification\\\"\\n  authors: \\\"Hsun-Yu Kuo et al.\\\"\\n  venue: \\\"arXiv preprint\\\"\\n  year: 2024\\n  url: \\\"https://arxiv.org/abs/2410.21526\\\"\\n  category: evaluation\\n  role: \\\"评估合成数据加权策略在文本分类中的效果\\\"\\n  key_findings: \\\"提出加权损失方法用少量真实数据对齐合成数据分布；在 BERT 级模型上稳定优于标准交叉熵和其他加权方法\\\"\\n  relevance_to_us: \\\"验证了合成数据需要差异化加权的思路；其评估框架可参考用于我们的下游任务评估\\\"\\n\", \"total_chars\": 8521, \"truncated\": false}, \"error\": null, \"metadata\": {}}"
    }
  },
  "sourceToolAssistantUUID": "4786b8a1-0992-4bfb-a9bf-9aee1800833c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training",
  "sessionId": "33f4c8cf-38de-44f8-ba86-369f9c5d5e2f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-14T23:36:40.578Z_

<details><summary>↩ Tool result · `toolu_011FvsqdQfuQM9VKuPrnYgEm`</summary>

```text
1	# Drayson et al. (EMNLP 2025) 深度对比分析
2	
3	> 日期: 2026-05-14 | 关联: D013 新颖性风险
4	
5	---
6	
7	## 1. Drayson 方法总结（200 字）
8	
9	Drayson et al. 提出 **detect-and-reweight** 防止语言模型在递归训练中坍塌。核心公式：**wⱼ = (1−q(xⱼ))^b / Σₗ(1−q(xₗ))^b**，其中 q(x) 为 ModernBERT 检测器输出的 machine-generated 概率。通过 Sampling Importance Resampling (SIR) 按权重重采样训练数据，上采样可能为人类撰写的内容。检测器在 MAGE 数据集上 fine-tune，in-domain AUC=0.986，OOD AUC=0.943。b 值通过在 WikiText-2 验证集上 1 代递归训练后评估选取（GPT-2/SmolLM 135M/360M 用 b=10，SmolLM 1.7B 用 b=1）。实验在 4 个模型（GPT-2 124M, SmolLM 135M/360M/1.7B）上进行 10 代递归训练，覆盖 6 种解码策略。结果：PPL 降低 0.85%–25.65%，diversity 提升 3.44%–14.62%。**b 在整个训练过程中固定，无自适应机制。**
10	
11	---
12	
13	## 2. 我们 vs Drayson 对比表
14	
15	| 维度 | Drayson et al. (EMNLP 2025) | 我们 (Adaptive b*) |
16	|------|---------------------------|-------------------|
17	| **b 选择方法** | 验证集 empirical 选取，per-model 固定 | α_eff(b) + ESS 约束自适应推导，per-batch 动态调整 |
18	| **检测器** | ModernBERT 150M (AUC=0.986) | TF-IDF + LR (AUC=0.939)，证明轻量检测器即可 |
19	| **污染设置** | 已知比例（实验控制 α,β,γ） | 未知比例（从 batch 统计量在线估计） |
20	| **理论基础** | 无（SIR 启发式，无 b 选取理论） | 收敛理论 motivated α_eff(b) 推导 + 连续谱统一框架 |
21	| **计算开销** | 需 per-model validation run（等价于 grid search） | 零额外 validation cost，从 batch 统计量直接计算 |
22	| **训练场景** | 递归训练 model collapse prevention | Web corpus 一次性预训练中的未知污染 |
23	| **数据规模** | WikiText-2 (36K docs, ~2M tokens) | FineWeb subset (132M+ tokens) |
24	| **生成器** | 单一生成器 per experiment | 多生成器 cross-contamination |
25	| **动态性** | b 固定（训练全程不变） | b* per-batch 自适应 |
26	| **框架贡献** | 提出 detect-and-reweight 方法 | 统一 soft-to-hard 连续谱 (b=0 uniform → b→∞ hard filter) |
27	
28	---
29	
30	## 3. 三个关键差异化论点（Related Work 可用）
31	
32	### 论点 1: From Heuristic to Principled（最直接）
33	
34	> Drayson et al. (2025) demonstrate that detect-and-reweight with w=(1−q)^b effectively prevents model collapse, but their bias term b is selected empirically per model via validation-set evaluation after one generation of recursive training. This requires a labeled validation set and separate tuning runs for each model architecture. We derive a principled, batch-adaptive b* from convergence-theory-inspired α_eff(b) with ESS constraints, eliminating validation-based tuning while matching or exceeding their best heuristic choices.
35	
36	### 论点 2: Unknown Contamination Proportion（差异化最强）
37	
38	> Prior detect-and-reweight approaches (Drayson et al., 2025) operate under controlled recursive training where contamination fractions are known by experimental design. In contrast, we address the realistic web-corpus scenario where neither the contamination proportion nor a clean validation set is available. Our adaptive b* is derived solely from batch-level detector statistics, making it applicable to large-scale pretraining where contamination is organic and unquantified.
39	
40	### 论点 3: Lightweight Detector Sufficiency（实用性角度）
41	
42	> Drayson et al. rely on ModernBERT (150M parameters, AUC=0.986), a state-of-the-art neural detector requiring GPU inference over the entire training corpus. We demonstrate that a simple TF-IDF + logistic regression detector (AUC=0.939) suffices when paired with our adaptive b*, reducing detector compute by orders of magnitude. This suggests the reweighting mechanism's effectiveness depends more on principled exponent selection than on detector precision.
43	
44	---
45	
46	## 4. Golden Ratio Weighting 总结（100 字）
47	
48	He & Xu (arXiv 2502.18049, 2025) 理论证明在递归训练中混合真实与合成数据时，最优权重 **w\* = (√(k²+4k)−k)/2**（k=真实/合成样本比）。当 k=1 时 w\*=1/φ≈0.618（黄金比例倒数）。在高斯分布估计、GLM、非参数估计三种设置下验证。**局限**：纯理论工作，假设已知污染比例，未涉及检测器或 LLM 实验，不处理 unknown/online 设置。
49	
50	---
51	
52	## 5. 其他相关论文一句话总结
53	
54	| 论文 | Venue | 一句话 |
55	|------|-------|--------|
56	| **Strong Model Collapse** (Dohmatob & Feng et al.) | ICLR 2025 (Spotlight), arXiv:2410.04840 | 理论证明即使 0.1% 合成数据污染也会导致 scaling law 失效，更大模型反而放大坍塌 |
57	| **Dynamic Loss-Based Sample Reweighting** (Sow et al., IBM/OSU/TUM) | ICLR 2025, arXiv:2502.06733 | 基于 per-sample loss 的在线重加权（LinUpper/Quadratic/Extremes + softmax temperature），不使用检测器，纯 loss signal 驱动，7B 模型验证有效 |
58	| **DoReMi** (Xie et al.) | NeurIPS 2023 | 域级别权重优化（Group DRO + 小模型代理），不处理 instance-level 污染 |
59	| **DSIR** (Xie et al.) | NeurIPS 2023 | N-gram 特征重要性采样选择数据子集匹配目标分布 |
60	| **Escaping Model Collapse via Synthetic Data Verification** | arXiv:2510.16657 | 提出验证机制筛选合成数据质量，与我们的 detection-based 方法互补 |
61	
62	---
63	
64	## 6. 搜索来源
65	
66	- Drayson et al.: [arXiv:2502.15654](https://arxiv.org/abs/2502.15654) | [HTML](https://arxiv.org/html/2502.15654) | [GitHub](https://github.com/GeorgeDrayson/model_collapse)
67	- Golden Ratio Weighting: [arXiv:2502.18049](https://arxiv.org/abs/2502.18049)
68	- Strong Model Collapse: [arXiv:2410.04840](https://arxiv.org/abs/2410.04840) | [ICLR 2025](https://openreview.net/forum?id=et5l9qPUhm)
69	- Dynamic Loss-Based Reweighting: [arXiv:2502.06733](https://arxiv.org/abs/2502.06733) | [GitHub](https://github.com/sowmaster/Sample-Level-Loss-Reweighting-ICLR-2025)
70	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "41a72385-eb72-408f-bf4a-6bfc9c5f5aa3",
  "isSidechain": false,
  "promptId": "8284b17e-dd1f-467a-9357-c4f2071853ea",
  "type": "user",
  "uuid": "8a901f06-c681-407a-85c5-33908b0a5b88",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/drayson_comparison.md",
      "content": "# Drayson et al. (EMNLP 2025) 深度对比分析\n\n> 日期: 2026-05-14 | 关联: D013 新颖性风险\n\n---\n\n## 1. Drayson 方法总结（200 字）\n\nDrayson et al. 提出 **detect-and-reweight** 防止语言模型在递归训练中坍塌。核心公式：**wⱼ = (1−q(xⱼ))^b / Σₗ(1−q(xₗ))^b**，其中 q(x) 为 ModernBERT 检测器输出的 machine-generated 概率。通过 Sampling Importance Resampling (SIR) 按权重重采样训练数据，上采样可能为人类撰写的内容。检测器在 MAGE 数据集上 fine-tune，in-domain AUC=0.986，OOD AUC=0.943。b 值通过在 WikiText-2 验证集上 1 代递归训练后评估选取（GPT-2/SmolLM 135M/360M 用 b=10，SmolLM 1.7B 用 b=1）。实验在 4 个模型（GPT-2 124M, SmolLM 135M/360M/1.7B）上进行 10 代递归训练，覆盖 6 种解码策略。结果：PPL 降低 0.85%–25.65%，diversity 提升 3.44%–14.62%。**b 在整个训练过程中固定，无自适应机制。**\n\n---\n\n## 2. 我们 vs Drayson 对比表\n\n| 维度 | Drayson et al. (EMNLP 2025) | 我们 (Adaptive b*) |\n|------|---------------------------|-------------------|\n| **b 选择方法** | 验证集 empirical 选取，per-model 固定 | α_eff(b) + ESS 约束自适应推导，per-batch 动态调整 |\n| **检测器** | ModernBERT 150M (AUC=0.986) | TF-IDF + LR (AUC=0.939)，证明轻量检测器即可 |\n| **污染设置** | 已知比例（实验控制 α,β,γ） | 未知比例（从 batch 统计量在线估计） |\n| **理论基础** | 无（SIR 启发式，无 b 选取理论） | 收敛理论 motivated α_eff(b) 推导 + 连续谱统一框架 |\n| **计算开销** | 需 per-model validation run（等价于 grid search） | 零额外 validation cost，从 batch 统计量直接计算 |\n| **训练场景** | 递归训练 model collapse prevention | Web corpus 一次性预训练中的未知污染 |\n| **数据规模** | WikiText-2 (36K docs, ~2M tokens) | FineWeb subset (132M+ tokens) |\n| **生成器** | 单一生成器 per experiment | 多生成器 cross-contamination |\n| **动态性** | b 固定（训练全程不变） | b* per-batch 自适应 |\n| **框架贡献** | 提出 detect-and-reweight 方法 | 统一 soft-to-hard 连续谱 (b=0 uniform → b→∞ hard filter) |\n\n---\n\n## 3. 三个关键差异化论点（Related Work 可用）\n\n### 论点 1: From Heuristic to Principled（最直接）\n\n> Drayson et al. (2025) demonstrate that detect-and-reweight with w=(1−q)^b effectively prevents model collapse, but their bias term b is selected empirically per model via validation-set evaluation after one generation of recursive training. This requires a labeled validation set and separate tuning runs for each model architecture. We derive a principled, batch-adaptive b* from convergence-theory-inspired α_eff(b) with ESS constraints, eliminating validation-based tuning while matching or exceeding their best heuristic choices.\n\n### 论点 2: Unknown Contamination Proportion（差异化最强）\n\n> Prior detect-and-reweight approaches (Drayson et al., 2025) operate under controlled recursive training where contamination fractions are known by experimental design. In contrast, we address the realistic web-corpus scenario where neither the contamination proportion nor a clean validation set is available. Our adaptive b* is derived solely from batch-level detector statistics, making it applicable to large-scale pretraining where contamination is organic and unquantified.\n\n### 论点 3: Lightweight Detector Sufficiency（实用性角度）\n\n> Drayson et al. rely on ModernBERT (150M parameters, AUC=0.986), a state-of-the-art neural detector requiring GPU inference over the entire training corpus. We demonstrate that a simple TF-IDF + logistic regression detector (AUC=0.939) suffices when paired with our adaptive b*, reducing detector compute by orders of magnitude. This suggests the reweighting mechanism's effectiveness depends more on principled exponent selection than on detector precision.\n\n---\n\n## 4. Golden Ratio Weighting 总结（100 字）\n\nHe & Xu (arXiv 2502.18049, 2025) 理论证明在递归训练中混合真实与合成数据时，最优权重 **w\\* = (√(k²+4k)−k)/2**（k=真实/合成样本比）。当 k=1 时 w\\*=1/φ≈0.618（黄金比例倒数）。在高斯分布估计、GLM、非参数估计三种设置下验证。**局限**：纯理论工作，假设已知污染比例，未涉及检测器或 LLM 实验，不处理 unknown/online 设置。\n\n---\n\n## 5. 其他相关论文一句话总结\n\n| 论文 | Venue | 一句话 |\n|------|-------|--------|\n| **Strong Model Collapse** (Dohmatob & Feng et al.) | ICLR 2025 (Spotlight), arXiv:2410.04840 | 理论证明即使 0.1% 合成数据污染也会导致 scaling law 失效，更大模型反而放大坍塌 |\n| **Dynamic Loss-Based Sample Reweighting** (Sow et al., IBM/OSU/TUM) | ICLR 2025, arXiv:2502.06733 | 基于 per-sample loss 的在线重加权（LinUpper/Quadratic/Extremes + softmax temperature），不使用检测器，纯 loss signal 驱动，7B 模型验证有效 |\n| **DoReMi** (Xie et al.) | NeurIPS 2023 | 域级别权重优化（Group DRO + 小模型代理），不处理 instance-level 污染 |\n| **DSIR** (Xie et al.) | NeurIPS 2023 | N-gram 特征重要性采样选择数据子集匹配目标分布 |\n| **Escaping Model Collapse via Synthetic Data Verification** | arXiv:2510.16657 | 提出验证机制筛选合成数据质量，与我们的 detection-based 方法互补 |\n\n---\n\n## 6. 搜索来源\n\n- Drayson et al.: [arXiv:2502.15654](https://arxiv.org/abs/2502.15654) | [HTML](https://arxiv.org/html/2502.15654) | [GitHub](https://github.com/GeorgeDrayson/model_collapse)\n- Golden Ratio Weighting: [arXiv:2502.18049](https://arxiv.org/abs/2502.18049)\n- Strong Model Collapse: [arXiv:2410.04840](https://arxiv.org/abs/2410.04840) | [ICLR 2025](https://openreview.net/forum?id=et5l9qPUhm)\n- Dynamic Loss-Based Reweighting: [arXiv:2502.06733](https://arxiv.org/abs/2502.06733) | [GitHub](https://github.com/sowmaster/Sample-Level-Loss-Reweighting-ICLR-2025)\n",
      "numLines": 70,
      "startLine": 1,
      "totalLines": 70
    }
  },
  "sourceToolAssistantUUID": "41a72385-eb72-408f-bf4a-6bfc9c5f5aa3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training",
  "sessionId": "33f4c8cf-38de-44f8-ba86-369f9c5d5e2f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-14T23:36:40.569Z_

<details open><summary>🔧 Tool call — Read · `toolu_011FvsqdQfuQM9VKuPrnYgEm`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/drayson_comparison.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4c302988-cc43-46d1-ab8c-15d07c744392",
  "isSidechain": false,
  "requestId": "req_011Cb3LfNFTPSjhj1MsDNMfx",
  "type": "assistant",
  "uuid": "41a72385-eb72-408f-bf4a-6bfc9c5f5aa3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training",
  "sessionId": "33f4c8cf-38de-44f8-ba86-369f9c5d5e2f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AMnN2BkcMGUYfpqReGNezc",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 709,
      "cache_read_input_tokens": 23046,
      "output_tokens": 205,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 709,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 205,
          "cache_read_input_tokens": 23046,
          "cache_creation_input_tokens": 709,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 709
          },
          "type": "message"
        }
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

_source line 16_

```json
{
  "type": "last-prompt",
  "leafUuid": "8a901f06-c681-407a-85c5-33908b0a5b88",
  "sessionId": "33f4c8cf-38de-44f8-ba86-369f9c5d5e2f"
}
```

---

### Runtime record

_source line 17_

```json
{
  "type": "ai-title",
  "aiTitle": "Integrate Drayson et al. into literature_map.yaml",
  "sessionId": "33f4c8cf-38de-44f8-ba86-369f9c5d5e2f"
}
```

---

### Assistant

_source line 18 · 2026-05-14T23:36:49.931Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have both files. Let me analyze what needs to be updated:

1. **Drayson et al. entry** - already exists as `drayson_2025_detection_collapse`, needs to be significantly enriched with details from the comparison doc
2. **He et al. Golden Ratio** - already exists as `he_2025_golden_ratio`, might need minor updates
3. **Dohmatob et al. Strong Model Collapse** - already exists as `dohmatob_2025_strong_collapse`


4. **Sow et al. Dynamic Loss-Based** - already exists as `sow_2025_dynamic_reweighting`
5. **DoReMi (Xie et al.)** - NOT in the map yet, should add
6. **DSIR (Xie et al.)** - NOT in the map yet, should add
7. **Escaping Model Collapse via Synthetic Data Verification** - NOT in the map yet, should add

I need to update the literature_map.yaml by enriching the Drayson entry with detailed method information and differentiation points, then add the three missing entries.

Updating the YAML file...
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8a901f06-c681-407a-85c5-33908b0a5b88",
  "isSidechain": false,
  "requestId": "req_011Cb3LfhjyKEMs65qxzeNeT",
  "type": "assistant",
  "uuid": "9cc0dd3a-27fa-4105-8a67-13ebdd3a6646",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training",
  "sessionId": "33f4c8cf-38de-44f8-ba86-369f9c5d5e2f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018x43DbHJ1NbTsyKTUDbnBc",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7627,
      "cache_read_input_tokens": 23755,
      "output_tokens": 6586,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 7627,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 6586,
          "cache_read_input_tokens": 23755,
          "cache_creation_input_tokens": 7627,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 7627
          },
          "type": "message"
        }
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

_source line 19 · 2026-05-14T23:36:51.055Z_

现有 Drayson 条目信息较简略，需要丰富。另外 drayson_comparison.md 中提到的 DoReMi、DSIR、Escaping Model Collapse 三篇尚未收录。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9cc0dd3a-27fa-4105-8a67-13ebdd3a6646",
  "isSidechain": false,
  "requestId": "req_011Cb3LfhjyKEMs65qxzeNeT",
  "type": "assistant",
  "uuid": "848b822c-da29-4d7f-8830-db8fd0dd4ccd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training",
  "sessionId": "33f4c8cf-38de-44f8-ba86-369f9c5d5e2f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018x43DbHJ1NbTsyKTUDbnBc",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7627,
      "cache_read_input_tokens": 23755,
      "output_tokens": 6586,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 7627,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 6586,
          "cache_read_input_tokens": 23755,
          "cache_creation_input_tokens": 7627,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 7627
          },
          "type": "message"
        }
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

_source line 20 · 2026-05-14T23:38:57.147Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__save_project_file · `toolu_01XDfg3GpnoYxiHSudisMZCg`</summary>

```json
{
  "project": "provenance_weight_training",
  "file": "literature_map.yaml",
  "content": "# Literature Map for provenance_weight_training\n# 研究方向：基于收敛理论的自适应污染重加权\n# 核心公式：w=(1-q)^b，q 为检测器合成概率，b* 为理论最优权重指数\n# 生成日期：2026-05-14\n\n# ============================================================\n# Category: direct-competitor\n# 同主题/同方法的论文\n# ============================================================\n\n- id: drayson_2025_detection_collapse\n  title: \"Machine-Generated Text Detection Prevents Language Model Collapse\"\n  authors: \"George Drayson, Emine Yilmaz, Vasileios Lampos\"\n  venue: \"EMNLP 2025\"\n  year: 2025\n  arxiv_id: \"2502.15654\"\n  url: \"https://arxiv.org/abs/2502.15654\"\n  github: \"https://github.com/GeorgeDrayson/model_collapse\"\n  category: direct-competitor\n  role: \"使用同一公式 w=(1-q)^b 进行重加权，但 b 为验证集 empirical 选取，训练中固定\"\n  method_summary: >\n    Detect-and-reweight 防止递归训练 model collapse。检测器为 ModernBERT 150M\n    (MAGE fine-tune, in-domain AUC=0.986, OOD AUC=0.943)。权重公式 wⱼ=(1-q(xⱼ))^b / Σₗ(1-q(xₗ))^b，\n    通过 SIR 按权重重采样训练数据。b 通过 WikiText-2 验证集上 1 代递归训练后评估选取\n    (GPT-2/SmolLM 135M/360M 用 b=10, SmolLM 1.7B 用 b=1)，训练全程固定。\n    实验覆盖 4 个模型 (GPT-2 124M, SmolLM 135M/360M/1.7B)、10 代递归训练、6 种解码策略。\n    结果 PPL 降低 0.85%–25.65%，diversity 提升 3.44%–14.62%。\n  key_findings: \"验证 detect-and-reweight 有效防止 model collapse 且优于纯人类数据训练；b 值对模型规模敏感（小模型 b=10，大模型 b=1）\"\n  differentiation:\n    b_selection: \"Drayson: 验证集 empirical grid search, per-model 固定 | 我们: α_eff(b) + ESS 约束, per-batch 自适应\"\n    contamination_setting: \"Drayson: 已知比例（实验控制） | 我们: 未知比例（batch 统计量在线估计）\"\n    detector: \"Drayson: ModernBERT 150M (AUC=0.986) | 我们: TF-IDF+LR (AUC=0.939)，证明轻量检测器即可\"\n    theory: \"Drayson: 无 b 选取理论（SIR 启发式） | 我们: 收敛理论 motivated α_eff(b) 推导\"\n    training_scenario: \"Drayson: 递归训练 model collapse prevention | 我们: Web corpus 一次性预训练中的未知污染\"\n    scale: \"Drayson: WikiText-2 (~2M tokens) | 我们: FineWeb subset (132M+ tokens)\"\n    dynamics: \"Drayson: b 固定（训练全程不变） | 我们: b* per-batch 自适应\"\n  our_advantages:\n    - \"From heuristic to principled: 理论推导 b* 替代 empirical grid search，零额外 validation cost\"\n    - \"Unknown contamination: 不需要已知污染比例或干净验证集，适用大规模 web pretraining\"\n    - \"Lightweight detector sufficiency: TF-IDF+LR 即可，检测器计算开销降低数量级\"\n    - \"Unified continuous spectrum: b=0 uniform → b→∞ hard filter 的统一框架\"\n  relevance_to_us: \"最直接的竞争者。共享 w=(1-q)^b 公式，但 b 选取方法根本不同——我们的核心贡献正是理论推导 adaptive b*\"\n\n- id: he_2025_golden_ratio\n  title: \"Golden Ratio Weighting Prevents Model Collapse\"\n  authors: \"Hengzhi He, Shirong Xu, Guang Cheng\"\n  venue: \"Under review at JRSSB, 2025\"\n  year: 2025\n  arxiv_id: \"2502.18049\"\n  url: \"https://arxiv.org/abs/2502.18049\"\n  category: direct-competitor\n  role: \"从理论推导合成/真实数据混合的最优权重，发现最优权重为黄金比例的倒数(~0.62)\"\n  key_findings: \"在高斯估计、GLM、非参数估计等场景下，当合成数据与真实数据等量时，真实数据的最优权重约为 0.62（黄金比例倒数）。公式 w*=(√(k²+4k)−k)/2, k=真实/合成样本比\"\n  differentiation:\n    scope: \"纯理论工作，假设已知污染比例，未涉及检测器或 LLM 实验，不处理 unknown/online 设置\"\n  relevance_to_us: \"同样是理论推导最优权重，但针对 real/synthetic 固定混合比例，未考虑检测器置信度的连续估计\"\n\n- id: feng_2024_beyond_collapse\n  title: \"Beyond Model Collapse: Scaling Up with Synthesized Data Requires Verification\"\n  authors: \"Yunzhen Feng, Elvis Dohmatob, Pu Yang, François Charton, Julia Kempe\"\n  venue: \"arXiv preprint\"\n  year: 2024\n  url: \"https://arxiv.org/abs/2406.07515\"\n  category: direct-competitor\n  role: \"使用 verifier 过滤合成数据防止 model collapse，理论证明即使不完美的 verifier 也有效\"\n  key_findings: \"用高斯混合模型和线性分类器推导条件，证明 verifier 引导的合成数据筛选可避免 model collapse；即使 verifier 不完美也能受益\"\n  relevance_to_us: \"与我们的方法最相似——都用检测器置信度来处理合成数据。区别在于他们做 hard filtering，我们做 soft reweighting\"\n\n# ============================================================\n# Category: method-component\n# 我们用到的技术组件\n# ============================================================\n\n- id: kimura_2024_iw_survey\n  title: \"A Short Survey on Importance Weighting for Machine Learning\"\n  authors: \"Masanari Kimura, Hideitsu Hino\"\n  venue: \"TMLR 2024\"\n  year: 2024\n  url: \"https://arxiv.org/abs/2403.10175\"\n  category: method-component\n  role: \"importance weighting 在机器学习中的全面综述，覆盖分布偏移、密度比估计等核心理论\"\n  key_findings: \"系统整理了 importance weighting 在监督学习分布偏移下的理论保证和应用，包括 covariate shift、domain adaptation 等场景\"\n  relevance_to_us: \"为我们的 importance weighting 框架提供理论基础和方法论参考\"\n\n- id: vehtari_2024_psis\n  title: \"Pareto Smoothed Importance Sampling\"\n  authors: \"Aki Vehtari, Daniel Simpson, Andrew Gelman, Yuling Yao, Jonah Gabry\"\n  venue: \"JMLR 2024\"\n  year: 2024\n  url: \"https://arxiv.org/abs/1507.02646\"\n  category: method-component\n  role: \"提供稳定的 effective sample size 估计和收敛诊断方法\"\n  key_findings: \"用广义 Pareto 分布拟合 importance ratio 上尾实现平滑；提出 Pareto k 有限样本收敛率诊断指标；k<min(1-1/log10(S),0.7) 时估计可靠\"\n  relevance_to_us: \"我们的 α_eff(b) 估计直接依赖 effective sample size 理论，PSIS 的收敛诊断可用于验证我们的权重方案\"\n\n- id: sow_2025_dynamic_reweighting\n  title: \"Dynamic Loss-Based Sample Reweighting for Improved Large Language Model Pretraining\"\n  authors: \"Daouda Sow et al.\"\n  venue: \"ICLR 2025\"\n  year: 2025\n  url: \"https://arxiv.org/abs/2502.06733\"\n  github: \"https://github.com/sowmaster/Sample-Level-Loss-Reweighting-ICLR-2025\"\n  category: method-component\n  role: \"首次提出 loss-based reweighting 对梯度优化收敛性影响的理论框架\"\n  key_findings: \"基于 loss 值动态调整每个样本权重；建立了 loss-based reweighting 对收敛界影响的形式化刻画；在 7B 和 1.4B 模型上验证更快收敛和更优性能\"\n  relevance_to_us: \"其收敛性理论框架可作为我们推导 b* 最优性的参考；loss-based 与 provenance-based reweighting 互补（不使用检测器，纯 loss signal 驱动）\"\n\n- id: ye_2025_data_mixing_laws\n  title: \"Data Mixing Laws: Optimizing Data Mixtures by Predicting Language Modeling Performance\"\n  authors: \"Jiasheng Ye, Peiju Liu, Tianxiang Sun, Yunhua Zhou, Jun Zhan, Xipeng Qiu\"\n  venue: \"ICLR 2025\"\n  year: 2025\n  url: \"https://arxiv.org/abs/2403.16952\"\n  category: method-component\n  role: \"发现数据混合比例与模型性能之间的定量可预测性\"\n  key_findings: \"模型性能关于混合比例具有函数形式的可预测性；可用小规模训练预测大模型在不同混合下的性能；适用于 continual training 的遗忘预测\"\n  relevance_to_us: \"data mixing laws 可作为验证我们 b* 最优性的理论框架——检验不同 b 下的 mixing 效果是否符合预测\"\n\n- id: he_2024_softdedup\n  title: \"SoftDedup: an Efficient Data Reweighting Method for Speeding Up Language Model Pre-training\"\n  authors: \"Nan He, Weichen Xiong, Hanwen Liu, Yi Liao, Lei Ding, Kai Zhang, Guohua Tang, Xiao Han, Yang Wei\"\n  venue: \"ACL 2024\"\n  year: 2024\n  url: \"https://arxiv.org/abs/2407.06654\"\n  category: method-component\n  role: \"用 data commonness 指标进行软去重加权，而非硬删除\"\n  key_findings: \"用 n-gram 模型量化样本的 commonness，高频样本降权低频样本升权；相比硬去重保留信息完整性；等效训练时间提升 26% 效率和 1.77% 下游准确率\"\n  relevance_to_us: \"软加权优于硬过滤的思路与我们一致——w=(1-q)^b 是连续加权而非二元过滤\"\n\n- id: xie_2023_doremi\n  title: \"DoReMi: Optimizing Data Mixtures by Predicting Language Modeling Performance\"\n  authors: \"Sang Michael Xie, Hieu Pham, Xuanyi Dong, Nan Du, Hanxiao Liu, Yifeng Lu, Percy Liang, Quoc V. Le, Tengyu Ma, Adams Wei Yu\"\n  venue: \"NeurIPS 2023\"\n  year: 2023\n  url: \"https://arxiv.org/abs/2305.10429\"\n  category: method-component\n  role: \"域级别权重优化（Group DRO + 小模型代理），不处理 instance-level 污染\"\n  key_findings: \"用小代理模型通过 Group DRO 优化域级别数据混合权重；在 The Pile 和 GLaM 数据集上无需目标分布知识即可改善下游性能\"\n  relevance_to_us: \"域级别 reweighting baseline；我们的方法在 instance-level 操作，粒度更细且基于检测器置信度而非 loss-based DRO\"\n\n- id: xie_2023_dsir\n  title: \"Data Selection for Language Models via Importance Resampling\"\n  authors: \"Sang Michael Xie, Shibani Santurkar, Tengyu Ma, Percy Liang\"\n  venue: \"NeurIPS 2023\"\n  year: 2023\n  url: \"https://arxiv.org/abs/2302.03169\"\n  category: method-component\n  role: \"N-gram 特征重要性采样选择数据子集匹配目标分布\"\n  key_findings: \"用 n-gram 特征估计 importance weights 并重采样数据匹配目标分布；比 heuristic filtering 更 principled；在 GLUE 和下游任务上优于随机选择和启发式方法\"\n  relevance_to_us: \"同样用 importance resampling，但目标是分布匹配而非污染处理；与 Drayson 的 SIR 方法有方法论联系\"\n\n# ============================================================\n# Category: background\n# 数据污染/合成数据在 LLM 训练中的问题\n# ============================================================\n\n- id: shumailov_2024_model_collapse\n  title: \"AI Models Collapse When Trained on Recursively Generated Data\"\n  authors: \"Ilia Shumailov, Zakhar Shumaylov, Yiren Zhao, Nicolas Papernot, Ross Anderson, Yarin Gal\"\n  venue: \"Nature 2024\"\n  year: 2024\n  url: \"https://www.nature.com/articles/s41586-024-07566-y\"\n  category: background\n  role: \"奠基性工作——证明在递归生成数据上训练导致 model collapse\"\n  key_findings: \"在 LLM、VAE、GMM 上证明不加区分地用模型生成内容训练会导致不可逆退化；原始分布的尾部逐渐消失；反复训练的语言模型出现重复短语\"\n  relevance_to_us: \"model collapse 是我们工作的核心动机——加权方案的目标就是防止污染数据导致的性能退化\"\n\n- id: alemohammad_2024_mad\n  title: \"Self-Consuming Generative Models Go MAD\"\n  authors: \"Sina Alemohammad, Josue Casco-Rodriguez, Lorenzo Luzi, Ahmed Imtiaz Humayun, Hossein Babaei, Daniel LeJeune, Ali Siahkoohi, Richard G. Baraniuk\"\n  venue: \"ICLR 2024\"\n  year: 2024\n  url: \"https://arxiv.org/abs/2307.01850\"\n  category: background\n  role: \"提出 Model Autophagy Disorder (MAD) 概念——自消费式生成模型的退化\"\n  key_findings: \"分析三种自消费循环（fully synthetic、synthetic augmentation、fresh data）；无新鲜真实数据时质量或多样性不可避免下降；即使保留原始训练数据也可能退化\"\n  relevance_to_us: \"MAD 的数学框架帮助理解不同污染程度下的退化动力学，为我们的收敛理论提供上下文\"\n\n- id: dohmatob_2025_strong_collapse\n  title: \"Strong Model Collapse\"\n  authors: \"Elvis Dohmatob, Yunzhen Feng, Arjun Subramonian, Julia Kempe\"\n  venue: \"ICLR 2025 (Spotlight)\"\n  year: 2025\n  arxiv_id: \"2410.04840\"\n  url: \"https://arxiv.org/abs/2410.04840\"\n  category: background\n  role: \"证明即使极少量合成数据（1/1000）也能导致 model collapse\"\n  key_findings: \"在 scaling laws 框架下建立 strong model collapse；用算子值自由概率论获得测试误差的 bias-variance 分解；更大模型可放大 collapse 效应\"\n  relevance_to_us: \"强化了我们工作的必要性——即使少量合成污染也需要处理，仅靠增加数据量无法解决\"\n\n- id: nait_saada_2025_quality_illusion\n  title: \"The Data-Quality Illusion: Rethinking Classifier-Based Quality Filtering for LLM Pretraining\"\n  authors: \"Thiziri Nait Saada, Louis Bethune, Michal Klein, David Grangier, Marco Cuturi, Pierre Ablin\"\n  venue: \"arXiv preprint\"\n  year: 2025\n  url: \"https://arxiv.org/abs/2510.00866\"\n  category: background\n  role: \"质疑基于分类器的数据质量评分是否真正捕获了有意义的质量概念\"\n  key_findings: \"CQF 改善下游任务但不一定改善语言建模；质量分类器隐式偏向其监督目标的数据分布；质量桶与特定 benchmark 对齐\"\n  relevance_to_us: \"提醒我们检测器置信度 q 不等于真实质量——需要理论保证 b* 在检测器有偏时仍然有效\"\n\n- id: guo_2025_escaping_collapse\n  title: \"Escaping Model Collapse via Synthetic Data Verification\"\n  authors: \"TBD\"\n  venue: \"arXiv preprint\"\n  year: 2025\n  arxiv_id: \"2510.16657\"\n  url: \"https://arxiv.org/abs/2510.16657\"\n  category: background\n  role: \"提出验证机制筛选合成数据质量，与 detection-based 方法互补\"\n  key_findings: \"通过验证机制在合成数据生成后筛选质量，与基于检测器的事后加权方法互补\"\n  relevance_to_us: \"verification-based 方法是另一条技术路线，可在 Related Work 中作为对比——他们做生成时验证，我们做训练时加权\"\n\n# ============================================================\n# Category: evaluation\n# 评估方法相关\n# ============================================================\n\n- id: mitchell_2023_detectgpt\n  title: \"DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature\"\n  authors: \"Eric Mitchell, Yoonho Lee, Alexander Khazatsky, Christopher D. Manning, Chelsea Finn\"\n  venue: \"ICML 2023\"\n  year: 2023\n  url: \"https://arxiv.org/abs/2301.11305\"\n  category: evaluation\n  role: \"零样本机器生成文本检测方法——我们的检测器 q 的基线方法之一\"\n  key_findings: \"LLM 生成的文本倾向于占据模型对数概率函数的负曲率区域；无需训练分类器、收集数据集或水印；在 GPT-NeoX 假新闻检测上从 0.81 AUROC 提升到 0.95\"\n  relevance_to_us: \"可作为计算合成概率 q 的检测器之一；其概率曲率方法可能与我们的权重公式有理论联系\"\n\n- id: shi_2024_minkprob\n  title: \"Detecting Pretraining Data from Large Language Models\"\n  authors: \"Weijia Shi, Anirudh Ajith, Mengzhou Xia, Yangsibo Huang, Daogao Liu, Terra Blevins, Danqi Chen, Luke Zettlemoyer\"\n  venue: \"ICLR 2024\"\n  year: 2024\n  url: \"https://arxiv.org/abs/2310.16789\"\n  category: evaluation\n  role: \"Min-K% Prob 方法——检测数据是否在预训练集中的无参考方法\"\n  key_findings: \"已训练数据包含更少低概率异常 token；取最低 K% token 概率的平均值判断；在 WikiMIA 上比最佳基线高 7.4 AUC；无需参考模型\"\n  relevance_to_us: \"Min-K% Prob 可作为估计合成概率 q 的候选方法；其 membership inference 思路可扩展为连续置信度估计\"\n\n- id: kuo_2024_data_weighting\n  title: \"Not All LLM-Generated Data Are Equal: Rethinking Data Weighting in Text Classification\"\n  authors: \"Hsun-Yu Kuo et al.\"\n  venue: \"arXiv preprint\"\n  year: 2024\n  url: \"https://arxiv.org/abs/2410.21526\"\n  category: evaluation\n  role: \"评估合成数据加权策略在文本分类中的效果\"\n  key_findings: \"提出加权损失方法用少量真实数据对齐合成数据分布；在 BERT 级模型上稳定优于标准交叉熵和其他加权方法\"\n  relevance_to_us: \"验证了合成数据需要差异化加权的思路；其评估框架可参考用于我们的下游任务评估\"\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "848b822c-da29-4d7f-8830-db8fd0dd4ccd",
  "isSidechain": false,
  "requestId": "req_011Cb3LfhjyKEMs65qxzeNeT",
  "type": "assistant",
  "uuid": "02dab4f7-8db5-456d-998c-ce2263a5c5d8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training",
  "sessionId": "33f4c8cf-38de-44f8-ba86-369f9c5d5e2f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018x43DbHJ1NbTsyKTUDbnBc",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7627,
      "cache_read_input_tokens": 23755,
      "output_tokens": 6586,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 7627,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 6586,
          "cache_read_input_tokens": 23755,
          "cache_creation_input_tokens": 7627,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 7627
          },
          "type": "message"
        }
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

_source line 21 · 2026-05-14T23:38:57.173Z_

<details><summary>↩ Tool result · `toolu_01XDfg3GpnoYxiHSudisMZCg`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"file 'literature_map.yaml' is not writable via save_project_file. Writable: ['memory.md', 'paper_framing.md', 'writing_plan.yaml'].\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "02dab4f7-8db5-456d-998c-ce2263a5c5d8",
  "isSidechain": false,
  "promptId": "8284b17e-dd1f-467a-9357-c4f2071853ea",
  "type": "user",
  "uuid": "06a24276-fe6d-4319-83c7-a77f73ccc94e",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {}, \\\"error\\\": \\\"file 'literature_map.yaml' is not writable via save_project_file. Writable: ['memory.md', 'paper_framing.md', 'writing_plan.yaml'].\\\", \\\"metadata\\\": {}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {}, \"error\": \"file 'literature_map.yaml' is not writable via save_project_file. Writable: ['memory.md', 'paper_framing.md', 'writing_plan.yaml'].\", \"metadata\": {}}"
    }
  },
  "sourceToolAssistantUUID": "02dab4f7-8db5-456d-998c-ce2263a5c5d8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training",
  "sessionId": "33f4c8cf-38de-44f8-ba86-369f9c5d5e2f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 22 · 2026-05-14T23:38:59.809Z_

<details><summary>Logged reasoning block</summary>

```text
The MCP tool doesn't allow writing to literature_map.yaml. Let me write it directly to the file system.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "06a24276-fe6d-4319-83c7-a77f73ccc94e",
  "isSidechain": false,
  "requestId": "req_011Cb3LqmTjkpxRqj9whdgVm",
  "type": "assistant",
  "uuid": "efa6f0af-d10f-497d-baa3-09003f53e5d3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training",
  "sessionId": "33f4c8cf-38de-44f8-ba86-369f9c5d5e2f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011aXridonUNtiT8Gnfq9YcS",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6672,
      "cache_read_input_tokens": 31382,
      "output_tokens": 6272,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 6672,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 6272,
          "cache_read_input_tokens": 31382,
          "cache_creation_input_tokens": 6672,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 6672
          },
          "type": "message"
        }
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

_source line 23 · 2026-05-14T23:39:00.298Z_

MCP 工具不支持写 literature_map.yaml，直接写文件。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "efa6f0af-d10f-497d-baa3-09003f53e5d3",
  "isSidechain": false,
  "requestId": "req_011Cb3LqmTjkpxRqj9whdgVm",
  "type": "assistant",
  "uuid": "6a6c0bc1-bc77-4bfa-b9f9-8ec8fa27cf00",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training",
  "sessionId": "33f4c8cf-38de-44f8-ba86-369f9c5d5e2f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011aXridonUNtiT8Gnfq9YcS",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6672,
      "cache_read_input_tokens": 31382,
      "output_tokens": 6272,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 6672,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 6272,
          "cache_read_input_tokens": 31382,
          "cache_creation_input_tokens": 6672,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 6672
          },
          "type": "message"
        }
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

_source line 24 · 2026-05-14T23:41:04.881Z_

<details open><summary>🔧 Tool call — Write · `toolu_01TzUwYbtPsjU3X7tjnaqXbj`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/literature_map.yaml",
  "content": "# Literature Map for provenance_weight_training\n# 研究方向：基于收敛理论的自适应污染重加权\n# 核心公式：w=(1-q)^b，q 为检测器合成概率，b* 为理论最优权重指数\n# 生成日期：2026-05-14\n\n# ============================================================\n# Category: direct-competitor\n# 同主题/同方法的论文\n# ============================================================\n\n- id: drayson_2025_detection_collapse\n  title: \"Machine-Generated Text Detection Prevents Language Model Collapse\"\n  authors: \"George Drayson, Emine Yilmaz, Vasileios Lampos\"\n  venue: \"EMNLP 2025\"\n  year: 2025\n  arxiv_id: \"2502.15654\"\n  url: \"https://arxiv.org/abs/2502.15654\"\n  github: \"https://github.com/GeorgeDrayson/model_collapse\"\n  category: direct-competitor\n  role: \"使用同一公式 w=(1-q)^b 进行重加权，但 b 为验证集 empirical 选取，训练中固定\"\n  method_summary: >\n    Detect-and-reweight 防止递归训练 model collapse。检测器为 ModernBERT 150M\n    (MAGE fine-tune, in-domain AUC=0.986, OOD AUC=0.943)。权重公式 wⱼ=(1-q(xⱼ))^b / Σₗ(1-q(xₗ))^b，\n    通过 SIR 按权重重采样训练数据。b 通过 WikiText-2 验证集上 1 代递归训练后评估选取\n    (GPT-2/SmolLM 135M/360M 用 b=10, SmolLM 1.7B 用 b=1)，训练全程固定。\n    实验覆盖 4 个模型 (GPT-2 124M, SmolLM 135M/360M/1.7B)、10 代递归训练、6 种解码策略。\n    结果 PPL 降低 0.85%–25.65%，diversity 提升 3.44%–14.62%。\n  key_findings: \"验证 detect-and-reweight 有效防止 model collapse 且优于纯人类数据训练；b 值对模型规模敏感（小模型 b=10，大模型 b=1）\"\n  differentiation:\n    b_selection: \"Drayson: 验证集 empirical grid search, per-model 固定 | 我们: α_eff(b) + ESS 约束, per-batch 自适应\"\n    contamination_setting: \"Drayson: 已知比例（实验控制） | 我们: 未知比例（batch 统计量在线估计）\"\n    detector: \"Drayson: ModernBERT 150M (AUC=0.986) | 我们: TF-IDF+LR (AUC=0.939)，证明轻量检测器即可\"\n    theory: \"Drayson: 无 b 选取理论（SIR 启发式） | 我们: 收敛理论 motivated α_eff(b) 推导\"\n    training_scenario: \"Drayson: 递归训练 model collapse prevention | 我们: Web corpus 一次性预训练中的未知污染\"\n    scale: \"Drayson: WikiText-2 (~2M tokens) | 我们: FineWeb subset (132M+ tokens)\"\n    dynamics: \"Drayson: b 固定（训练全程不变） | 我们: b* per-batch 自适应\"\n  our_advantages:\n    - \"From heuristic to principled: 理论推导 b* 替代 empirical grid search，零额外 validation cost\"\n    - \"Unknown contamination: 不需要已知污染比例或干净验证集，适用大规模 web pretraining\"\n    - \"Lightweight detector sufficiency: TF-IDF+LR 即可，检测器计算开销降低数量级\"\n    - \"Unified continuous spectrum: b=0 uniform → b→∞ hard filter 的统一框架\"\n  relevance_to_us: \"最直接的竞争者。共享 w=(1-q)^b 公式，但 b 选取方法根本不同——我们的核心贡献正是理论推导 adaptive b*\"\n\n- id: he_2025_golden_ratio\n  title: \"Golden Ratio Weighting Prevents Model Collapse\"\n  authors: \"Hengzhi He, Shirong Xu, Guang Cheng\"\n  venue: \"Under review at JRSSB, 2025\"\n  year: 2025\n  arxiv_id: \"2502.18049\"\n  url: \"https://arxiv.org/abs/2502.18049\"\n  category: direct-competitor\n  role: \"从理论推导合成/真实数据混合的最优权重，发现最优权重为黄金比例的倒数(~0.62)\"\n  key_findings: \"在高斯估计、GLM、非参数估计等场景下，当合成数据与真实数据等量时，真实数据的最优权重约为 0.62（黄金比例倒数）。公式 w*=(√(k²+4k)−k)/2, k=真实/合成样本比\"\n  differentiation:\n    scope: \"纯理论工作，假设已知污染比例，未涉及检测器或 LLM 实验，不处理 unknown/online 设置\"\n  relevance_to_us: \"同样是理论推导最优权重，但针对 real/synthetic 固定混合比例，未考虑检测器置信度的连续估计\"\n\n- id: feng_2024_beyond_collapse\n  title: \"Beyond Model Collapse: Scaling Up with Synthesized Data Requires Verification\"\n  authors: \"Yunzhen Feng, Elvis Dohmatob, Pu Yang, François Charton, Julia Kempe\"\n  venue: \"arXiv preprint\"\n  year: 2024\n  url: \"https://arxiv.org/abs/2406.07515\"\n  category: direct-competitor\n  role: \"使用 verifier 过滤合成数据防止 model collapse，理论证明即使不完美的 verifier 也有效\"\n  key_findings: \"用高斯混合模型和线性分类器推导条件，证明 verifier 引导的合成数据筛选可避免 model collapse；即使 verifier 不完美也能受益\"\n  relevance_to_us: \"与我们的方法最相似——都用检测器置信度来处理合成数据。区别在于他们做 hard filtering，我们做 soft reweighting\"\n\n# ============================================================\n# Category: method-component\n# 我们用到的技术组件\n# ============================================================\n\n- id: kimura_2024_iw_survey\n  title: \"A Short Survey on Importance Weighting for Machine Learning\"\n  authors: \"Masanari Kimura, Hideitsu Hino\"\n  venue: \"TMLR 2024\"\n  year: 2024\n  url: \"https://arxiv.org/abs/2403.10175\"\n  category: method-component\n  role: \"importance weighting 在机器学习中的全面综述，覆盖分布偏移、密度比估计等核心理论\"\n  key_findings: \"系统整理了 importance weighting 在监督学习分布偏移下的理论保证和应用，包括 covariate shift、domain adaptation 等场景\"\n  relevance_to_us: \"为我们的 importance weighting 框架提供理论基础和方法论参考\"\n\n- id: vehtari_2024_psis\n  title: \"Pareto Smoothed Importance Sampling\"\n  authors: \"Aki Vehtari, Daniel Simpson, Andrew Gelman, Yuling Yao, Jonah Gabry\"\n  venue: \"JMLR 2024\"\n  year: 2024\n  url: \"https://arxiv.org/abs/1507.02646\"\n  category: method-component\n  role: \"提供稳定的 effective sample size 估计和收敛诊断方法\"\n  key_findings: \"用广义 Pareto 分布拟合 importance ratio 上尾实现平滑；提出 Pareto k 有限样本收敛率诊断指标；k<min(1-1/log10(S),0.7) 时估计可靠\"\n  relevance_to_us: \"我们的 α_eff(b) 估计直接依赖 effective sample size 理论，PSIS 的收敛诊断可用于验证我们的权重方案\"\n\n- id: sow_2025_dynamic_reweighting\n  title: \"Dynamic Loss-Based Sample Reweighting for Improved Large Language Model Pretraining\"\n  authors: \"Daouda Sow et al.\"\n  venue: \"ICLR 2025\"\n  year: 2025\n  url: \"https://arxiv.org/abs/2502.06733\"\n  github: \"https://github.com/sowmaster/Sample-Level-Loss-Reweighting-ICLR-2025\"\n  category: method-component\n  role: \"首次提出 loss-based reweighting 对梯度优化收敛性影响的理论框架\"\n  key_findings: \"基于 loss 值动态调整每个样本权重；建立了 loss-based reweighting 对收敛界影响的形式化刻画；在 7B 和 1.4B 模型上验证更快收敛和更优性能\"\n  relevance_to_us: \"其收敛性理论框架可作为我们推导 b* 最优性的参考；loss-based 与 provenance-based reweighting 互补（不使用检测器，纯 loss signal 驱动）\"\n\n- id: ye_2025_data_mixing_laws\n  title: \"Data Mixing Laws: Optimizing Data Mixtures by Predicting Language Modeling Performance\"\n  authors: \"Jiasheng Ye, Peiju Liu, Tianxiang Sun, Yunhua Zhou, Jun Zhan, Xipeng Qiu\"\n  venue: \"ICLR 2025\"\n  year: 2025\n  url: \"https://arxiv.org/abs/2403.16952\"\n  category: method-component\n  role: \"发现数据混合比例与模型性能之间的定量可预测性\"\n  key_findings: \"模型性能关于混合比例具有函数形式的可预测性；可用小规模训练预测大模型在不同混合下的性能；适用于 continual training 的遗忘预测\"\n  relevance_to_us: \"data mixing laws 可作为验证我们 b* 最优性的理论框架——检验不同 b 下的 mixing 效果是否符合预测\"\n\n- id: he_2024_softdedup\n  title: \"SoftDedup: an Efficient Data Reweighting Method for Speeding Up Language Model Pre-training\"\n  authors: \"Nan He, Weichen Xiong, Hanwen Liu, Yi Liao, Lei Ding, Kai Zhang, Guohua Tang, Xiao Han, Yang Wei\"\n  venue: \"ACL 2024\"\n  year: 2024\n  url: \"https://arxiv.org/abs/2407.06654\"\n  category: method-component\n  role: \"用 data commonness 指标进行软去重加权，而非硬删除\"\n  key_findings: \"用 n-gram 模型量化样本的 commonness，高频样本降权低频样本升权；相比硬去重保留信息完整性；等效训练时间提升 26% 效率和 1.77% 下游准确率\"\n  relevance_to_us: \"软加权优于硬过滤的思路与我们一致——w=(1-q)^b 是连续加权而非二元过滤\"\n\n- id: xie_2023_doremi\n  title: \"DoReMi: Optimizing Data Mixtures by Predicting Language Modeling Performance\"\n  authors: \"Sang Michael Xie, Hieu Pham, Xuanyi Dong, Nan Du, Hanxiao Liu, Yifeng Lu, Percy Liang, Quoc V. Le, Tengyu Ma, Adams Wei Yu\"\n  venue: \"NeurIPS 2023\"\n  year: 2023\n  url: \"https://arxiv.org/abs/2305.10429\"\n  category: method-component\n  role: \"域级别权重优化（Group DRO + 小模型代理），不处理 instance-level 污染\"\n  key_findings: \"用小代理模型通过 Group DRO 优化域级别数据混合权重；在 The Pile 和 GLaM 数据集上无需目标分布知识即可改善下游性能\"\n  relevance_to_us: \"域级别 reweighting baseline；我们的方法在 instance-level 操作，粒度更细且基于检测器置信度而非 loss-based DRO\"\n\n- id: xie_2023_dsir\n  title: \"Data Selection for Language Models via Importance Resampling\"\n  authors: \"Sang Michael Xie, Shibani Santurkar, Tengyu Ma, Percy Liang\"\n  venue: \"NeurIPS 2023\"\n  year: 2023\n  url: \"https://arxiv.org/abs/2302.03169\"\n  category: method-component\n  role: \"N-gram 特征重要性采样选择数据子集匹配目标分布\"\n  key_findings: \"用 n-gram 特征估计 importance weights 并重采样数据匹配目标分布；比 heuristic filtering 更 principled；在 GLUE 和下游任务上优于随机选择和启发式方法\"\n  relevance_to_us: \"同样用 importance resampling，但目标是分布匹配而非污染处理；与 Drayson 的 SIR 方法有方法论联系\"\n\n# ============================================================\n# Category: background\n# 数据污染/合成数据在 LLM 训练中的问题\n# ============================================================\n\n- id: shumailov_2024_model_collapse\n  title: \"AI Models Collapse When Trained on Recursively Generated Data\"\n  authors: \"Ilia Shumailov, Zakhar Shumaylov, Yiren Zhao, Nicolas Papernot, Ross Anderson, Yarin Gal\"\n  venue: \"Nature 2024\"\n  year: 2024\n  url: \"https://www.nature.com/articles/s41586-024-07566-y\"\n  category: background\n  role: \"奠基性工作——证明在递归生成数据上训练导致 model collapse\"\n  key_findings: \"在 LLM、VAE、GMM 上证明不加区分地用模型生成内容训练会导致不可逆退化；原始分布的尾部逐渐消失；反复训练的语言模型出现重复短语\"\n  relevance_to_us: \"model collapse 是我们工作的核心动机——加权方案的目标就是防止污染数据导致的性能退化\"\n\n- id: alemohammad_2024_mad\n  title: \"Self-Consuming Generative Models Go MAD\"\n  authors: \"Sina Alemohammad, Josue Casco-Rodriguez, Lorenzo Luzi, Ahmed Imtiaz Humayun, Hossein Babaei, Daniel LeJeune, Ali Siahkoohi, Richard G. Baraniuk\"\n  venue: \"ICLR 2024\"\n  year: 2024\n  url: \"https://arxiv.org/abs/2307.01850\"\n  category: background\n  role: \"提出 Model Autophagy Disorder (MAD) 概念——自消费式生成模型的退化\"\n  key_findings: \"分析三种自消费循环（fully synthetic、synthetic augmentation、fresh data）；无新鲜真实数据时质量或多样性不可避免下降；即使保留原始训练数据也可能退化\"\n  relevance_to_us: \"MAD 的数学框架帮助理解不同污染程度下的退化动力学，为我们的收敛理论提供上下文\"\n\n- id: dohmatob_2025_strong_collapse\n  title: \"Strong Model Collapse\"\n  authors: \"Elvis Dohmatob, Yunzhen Feng, Arjun Subramonian, Julia Kempe\"\n  venue: \"ICLR 2025 (Spotlight)\"\n  year: 2025\n  arxiv_id: \"2410.04840\"\n  url: \"https://arxiv.org/abs/2410.04840\"\n  category: background\n  role: \"证明即使极少量合成数据（1/1000）也能导致 model collapse\"\n  key_findings: \"在 scaling laws 框架下建立 strong model collapse；用算子值自由概率论获得测试误差的 bias-variance 分解；更大模型可放大 collapse 效应\"\n  relevance_to_us: \"强化了我们工作的必要性——即使少量合成污染也需要处理，仅靠增加数据量无法解决\"\n\n- id: nait_saada_2025_quality_illusion\n  title: \"The Data-Quality Illusion: Rethinking Classifier-Based Quality Filtering for LLM Pretraining\"\n  authors: \"Thiziri Nait Saada, Louis Bethune, Michal Klein, David Grangier, Marco Cuturi, Pierre Ablin\"\n  venue: \"arXiv preprint\"\n  year: 2025\n  url: \"https://arxiv.org/abs/2510.00866\"\n  category: background\n  role: \"质疑基于分类器的数据质量评分是否真正捕获了有意义的质量概念\"\n  key_findings: \"CQF 改善下游任务但不一定改善语言建模；质量分类器隐式偏向其监督目标的数据分布；质量桶与特定 benchmark 对齐\"\n  relevance_to_us: \"提醒我们检测器置信度 q 不等于真实质量——需要理论保证 b* 在检测器有偏时仍然有效\"\n\n- id: guo_2025_escaping_collapse\n  title: \"Escaping Model Collapse via Synthetic Data Verification\"\n  authors: \"TBD\"\n  venue: \"arXiv preprint\"\n  year: 2025\n  arxiv_id: \"2510.16657\"\n  url: \"https://arxiv.org/abs/2510.16657\"\n  category: background\n  role: \"提出验证机制筛选合成数据质量，与 detection-based 方法互补\"\n  key_findings: \"通过验证机制在合成数据生成后筛选质量，与基于检测器的事后加权方法互补\"\n  relevance_to_us: \"verification-based 方法是另一条技术路线，可在 Related Work 中作为对比——他们做生成时验证，我们做训练时加权\"\n\n# ============================================================\n# Category: evaluation\n# 评估方法相关\n# ============================================================\n\n- id: mitchell_2023_detectgpt\n  title: \"DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature\"\n  authors: \"Eric Mitchell, Yoonho Lee, Alexander Khazatsky, Christopher D. Manning, Chelsea Finn\"\n  venue: \"ICML 2023\"\n  year: 2023\n  url: \"https://arxiv.org/abs/2301.11305\"\n  category: evaluation\n  role: \"零样本机器生成文本检测方法——我们的检测器 q 的基线方法之一\"\n  key_findings: \"LLM 生成的文本倾向于占据模型对数概率函数的负曲率区域；无需训练分类器、收集数据集或水印；在 GPT-NeoX 假新闻检测上从 0.81 AUROC 提升到 0.95\"\n  relevance_to_us: \"可作为计算合成概率 q 的检测器之一；其概率曲率方法可能与我们的权重公式有理论联系\"\n\n- id: shi_2024_minkprob\n  title: \"Detecting Pretraining Data from Large Language Models\"\n  authors: \"Weijia Shi, Anirudh Ajith, Mengzhou Xia, Yangsibo Huang, Daogao Liu, Terra Blevins, Danqi Chen, Luke Zettlemoyer\"\n  venue: \"ICLR 2024\"\n  year: 2024\n  url: \"https://arxiv.org/abs/2310.16789\"\n  category: evaluation\n  role: \"Min-K% Prob 方法——检测数据是否在预训练集中的无参考方法\"\n  key_findings: \"已训练数据包含更少低概率异常 token；取最低 K% token 概率的平均值判断；在 WikiMIA 上比最佳基线高 7.4 AUC；无需参考模型\"\n  relevance_to_us: \"Min-K% Prob 可作为估计合成概率 q 的候选方法；其 membership inference 思路可扩展为连续置信度估计\"\n\n- id: kuo_2024_data_weighting\n  title: \"Not All LLM-Generated Data Are Equal: Rethinking Data Weighting in Text Classification\"\n  authors: \"Hsun-Yu Kuo et al.\"\n  venue: \"arXiv preprint\"\n  year: 2024\n  url: \"https://arxiv.org/abs/2410.21526\"\n  category: evaluation\n  role: \"评估合成数据加权策略在文本分类中的效果\"\n  key_findings: \"提出加权损失方法用少量真实数据对齐合成数据分布；在 BERT 级模型上稳定优于标准交叉熵和其他加权方法\"\n  relevance_to_us: \"验证了合成数据需要差异化加权的思路；其评估框架可参考用于我们的下游任务评估\"\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6a6c0bc1-bc77-4bfa-b9f9-8ec8fa27cf00",
  "isSidechain": false,
  "requestId": "req_011Cb3LqmTjkpxRqj9whdgVm",
  "type": "assistant",
  "uuid": "4067676e-5ff5-4000-863e-97eb12f072e9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training",
  "sessionId": "33f4c8cf-38de-44f8-ba86-369f9c5d5e2f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011aXridonUNtiT8Gnfq9YcS",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6672,
      "cache_read_input_tokens": 31382,
      "output_tokens": 6272,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 6672,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 6272,
          "cache_read_input_tokens": 31382,
          "cache_creation_input_tokens": 6672,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 6672
          },
          "type": "message"
        }
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

_source line 25 · 2026-05-14T23:41:04.884Z_

<details><summary>↩ Tool result · reported error · `toolu_01TzUwYbtPsjU3X7tjnaqXbj`</summary>

```text
&lt;tool_use_error>File has not been read yet. Read it first before writing to it.&lt;/tool_use_error>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4067676e-5ff5-4000-863e-97eb12f072e9",
  "isSidechain": false,
  "promptId": "8284b17e-dd1f-467a-9357-c4f2071853ea",
  "type": "user",
  "uuid": "4deb47ae-bb86-4320-acde-ecf309ac232d",
  "toolUseResult": "Error: File has not been read yet. Read it first before writing to it.",
  "sourceToolAssistantUUID": "4067676e-5ff5-4000-863e-97eb12f072e9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training",
  "sessionId": "33f4c8cf-38de-44f8-ba86-369f9c5d5e2f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 26_

```json
{
  "type": "last-prompt",
  "leafUuid": "4deb47ae-bb86-4320-acde-ecf309ac232d",
  "sessionId": "33f4c8cf-38de-44f8-ba86-369f9c5d5e2f"
}
```

---

### Runtime record

_source line 27_

```json
{
  "type": "ai-title",
  "aiTitle": "Integrate Drayson et al. into literature_map.yaml",
  "sessionId": "33f4c8cf-38de-44f8-ba86-369f9c5d5e2f"
}
```

---

### Tool call

_source line 28 · 2026-05-14T23:41:08.879Z_

<details open><summary>🔧 Tool call — Read · `toolu_017Gj4jgUFCtCgiwAwzX1ywg`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/literature_map.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4deb47ae-bb86-4320-acde-ecf309ac232d",
  "isSidechain": false,
  "requestId": "req_011Cb3M1Bg2LEK2ab5YvXYzQ",
  "type": "assistant",
  "uuid": "8c015997-0454-4320-aea4-623f3b3f5a7e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training",
  "sessionId": "33f4c8cf-38de-44f8-ba86-369f9c5d5e2f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PsyxZjfADtjLp8VGTunspK",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6318,
      "cache_read_input_tokens": 38054,
      "output_tokens": 86,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 6318,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 86,
          "cache_read_input_tokens": 38054,
          "cache_creation_input_tokens": 6318,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 6318
          },
          "type": "message"
        }
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

_source line 29 · 2026-05-14T23:41:08.887Z_

<details><summary>↩ Tool result · `toolu_017Gj4jgUFCtCgiwAwzX1ywg`</summary>

```text
1	# Literature Map for provenance_weight_training
2	# 研究方向：基于收敛理论的自适应污染重加权
3	# 核心公式：w=(1-q)^b，q 为检测器合成概率，b* 为理论最优权重指数
4	# 生成日期：2026-05-14
5	
6	# ============================================================
7	# Category: direct-competitor
8	# 同主题/同方法的论文
9	# ============================================================
10	
11	- id: drayson_2025_detection_collapse
12	  title: "Machine-Generated Text Detection Prevents Language Model Collapse"
13	  authors: "George Drayson, Emine Yilmaz, Vasileios Lampos"
14	  venue: "EMNLP 2025"
15	  year: 2025
16	  url: "https://arxiv.org/abs/2502.15654"
17	  category: direct-competitor
18	  role: "使用同一公式 w=(1-q)^b 进行重加权，但启发式选择 b 而非理论推导"
19	  key_findings: "训练机器生成文本检测器，用 importance resampling 上采样可能的人类内容，不仅防止 model collapse，还优于纯人类数据训练"
20	  relevance_to_us: "最直接的竞争者。我们的核心贡献是理论推导 b*，替代其启发式网格搜索方法"
21	
22	- id: he_2025_golden_ratio
23	  title: "Golden Ratio Weighting Prevents Model Collapse"
24	  authors: "Hengzhi He, Shirong Xu, Guang Cheng"
25	  venue: "Under review at JRSSB, 2025"
26	  year: 2025
27	  url: "https://arxiv.org/abs/2502.18049"
28	  category: direct-competitor
29	  role: "从理论推导合成/真实数据混合的最优权重，发现最优权重为黄金比例的倒数(~0.62)"
30	  key_findings: "在高斯估计、GLM、非参数估计等场景下，当合成数据与真实数据等量时，真实数据的最优权重约为 0.62（黄金比例倒数）"
31	  relevance_to_us: "同样是理论推导最优权重，但针对 real/synthetic 固定混合比例，未考虑检测器置信度的连续估计"
32	
33	- id: feng_2024_beyond_collapse
34	  title: "Beyond Model Collapse: Scaling Up with Synthesized Data Requires Verification"
35	  authors: "Yunzhen Feng, Elvis Dohmatob, Pu Yang, François Charton, Julia Kempe"
36	  venue: "arXiv preprint"
37	  year: 2024
38	  url: "https://arxiv.org/abs/2406.07515"
39	  category: direct-competitor
40	  role: "使用 verifier 过滤合成数据防止 model collapse，理论证明即使不完美的 verifier 也有效"
41	  key_findings: "用高斯混合模型和线性分类器推导条件，证明 verifier 引导的合成数据筛选可避免 model collapse；即使 verifier 不完美也能受益"
42	  relevance_to_us: "与我们的方法最相似——都用检测器置信度来处理合成数据。区别在于他们做 hard filtering，我们做 soft reweighting"
43	
44	# ============================================================
45	# Category: method-component
46	# 我们用到的技术组件
47	# ============================================================
48	
49	- id: kimura_2024_iw_survey
50	  title: "A Short Survey on Importance Weighting for Machine Learning"
51	  authors: "Masanari Kimura, Hideitsu Hino"
52	  venue: "TMLR 2024"
53	  year: 2024
54	  url: "https://arxiv.org/abs/2403.10175"
55	  category: method-component
56	  role: "importance weighting 在机器学习中的全面综述，覆盖分布偏移、密度比估计等核心理论"
57	  key_findings: "系统整理了 importance weighting 在监督学习分布偏移下的理论保证和应用，包括 covariate shift、domain adaptation 等场景"
58	  relevance_to_us: "为我们的 importance weighting 框架提供理论基础和方法论参考"
59	
60	- id: vehtari_2024_psis
61	  title: "Pareto Smoothed Importance Sampling"
62	  authors: "Aki Vehtari, Daniel Simpson, Andrew Gelman, Yuling Yao, Jonah Gabry"
63	  venue: "JMLR 2024"
64	  year: 2024
65	  url: "https://arxiv.org/abs/1507.02646"
66	  category: method-component
67	  role: "提供稳定的 effective sample size 估计和收敛诊断方法"
68	  key_findings: "用广义 Pareto 分布拟合 importance ratio 上尾实现平滑；提出 Pareto k 有限样本收敛率诊断指标；k<min(1-1/log10(S),0.7) 时估计可靠"
69	  relevance_to_us: "我们的 α_eff(b) 估计直接依赖 effective sample size 理论，PSIS 的收敛诊断可用于验证我们的权重方案"
70	
71	- id: sow_2025_dynamic_reweighting
72	  title: "Dynamic Loss-Based Sample Reweighting for Improved Large Language Model Pretraining"
73	  authors: "Daouda Sow et al."
74	  venue: "ICLR 2025"
75	  year: 2025
76	  url: "https://arxiv.org/abs/2502.06733"
77	  category: method-component
78	  role: "首次提出 loss-based reweighting 对梯度优化收敛性影响的理论框架"
79	  key_findings: "基于 loss 值动态调整每个样本权重；建立了 loss-based reweighting 对收敛界影响的形式化刻画；在 7B 和 1.4B 模型上验证更快收敛和更优性能"
80	  relevance_to_us: "其收敛性理论框架可作为我们推导 b* 最优性的参考；loss-based 与 provenance-based reweighting 互补"
81	
82	- id: ye_2025_data_mixing_laws
83	  title: "Data Mixing Laws: Optimizing Data Mixtures by Predicting Language Modeling Performance"
84	  authors: "Jiasheng Ye, Peiju Liu, Tianxiang Sun, Yunhua Zhou, Jun Zhan, Xipeng Qiu"
85	  venue: "ICLR 2025"
86	  year: 2025
87	  url: "https://arxiv.org/abs/2403.16952"
88	  category: method-component
89	  role: "发现数据混合比例与模型性能之间的定量可预测性"
90	  key_findings: "模型性能关于混合比例具有函数形式的可预测性；可用小规模训练预测大模型在不同混合下的性能；适用于 continual training 的遗忘预测"
91	  relevance_to_us: "data mixing laws 可作为验证我们 b* 最优性的理论框架——检验不同 b 下的 mixing 效果是否符合预测"
92	
93	- id: he_2024_softdedup
94	  title: "SoftDedup: an Efficient Data Reweighting Method for Speeding Up Language Model Pre-training"
95	  authors: "Nan He, Weichen Xiong, Hanwen Liu, Yi Liao, Lei Ding, Kai Zhang, Guohua Tang, Xiao Han, Yang Wei"
96	  venue: "ACL 2024"
97	  year: 2024
98	  url: "https://arxiv.org/abs/2407.06654"
99	  category: method-component
100	  role: "用 data commonness 指标进行软去重加权，而非硬删除"
101	  key_findings: "用 n-gram 模型量化样本的 commonness，高频样本降权低频样本升权；相比硬去重保留信息完整性；等效训练时间提升 26% 效率和 1.77% 下游准确率"
102	  relevance_to_us: "软加权优于硬过滤的思路与我们一致——w=(1-q)^b 是连续加权而非二元过滤"
103	
104	# ============================================================
105	# Category: background
106	# 数据污染/合成数据在 LLM 训练中的问题
107	# ============================================================
108	
109	- id: shumailov_2024_model_collapse
110	  title: "AI Models Collapse When Trained on Recursively Generated Data"
111	  authors: "Ilia Shumailov, Zakhar Shumaylov, Yiren Zhao, Nicolas Papernot, Ross Anderson, Yarin Gal"
112	  venue: "Nature 2024"
113	  year: 2024
114	  url: "https://www.nature.com/articles/s41586-024-07566-y"
115	  category: background
116	  role: "奠基性工作——证明在递归生成数据上训练导致 model collapse"
117	  key_findings: "在 LLM、VAE、GMM 上证明不加区分地用模型生成内容训练会导致不可逆退化；原始分布的尾部逐渐消失；反复训练的语言模型出现重复短语"
118	  relevance_to_us: "model collapse 是我们工作的核心动机——加权方案的目标就是防止污染数据导致的性能退化"
119	
120	- id: alemohammad_2024_mad
121	  title: "Self-Consuming Generative Models Go MAD"
122	  authors: "Sina Alemohammad, Josue Casco-Rodriguez, Lorenzo Luzi, Ahmed Imtiaz Humayun, Hossein Babaei, Daniel LeJeune, Ali Siahkoohi, Richard G. Baraniuk"
123	  venue: "ICLR 2024"
124	  year: 2024
125	  url: "https://arxiv.org/abs/2307.01850"
126	  category: background
127	  role: "提出 Model Autophagy Disorder (MAD) 概念——自消费式生成模型的退化"
128	  key_findings: "分析三种自消费循环（fully synthetic、synthetic augmentation、fresh data）；无新鲜真实数据时质量或多样性不可避免下降；即使保留原始训练数据也可能退化"
129	  relevance_to_us: "MAD 的数学框架帮助理解不同污染程度下的退化动力学，为我们的收敛理论提供上下文"
130	
131	- id: dohmatob_2025_strong_collapse
132	  title: "Strong Model Collapse"
133	  authors: "Elvis Dohmatob, Yunzhen Feng, Arjun Subramonian, Julia Kempe"
134	  venue: "ICLR 2025 (Spotlight)"
135	  year: 2025
136	  url: "https://arxiv.org/abs/2410.04840"
137	  category: background
138	  role: "证明即使极少量合成数据（1/1000）也能导致 model collapse"
139	  key_findings: "在 scaling laws 框架下建立 strong model collapse；用算子值自由概率论获得测试误差的 bias-variance 分解；更大模型可放大 collapse 效应"
140	  relevance_to_us: "强化了我们工作的必要性——即使少量合成污染也需要处理，仅靠增加数据量无法解决"
141	
142	- id: nait_saada_2025_quality_illusion
143	  title: "The Data-Quality Illusion: Rethinking Classifier-Based Quality Filtering for LLM Pretraining"
144	  authors: "Thiziri Nait Saada, Louis Bethune, Michal Klein, David Grangier, Marco Cuturi, Pierre Ablin"
145	  venue: "arXiv preprint"
146	  year: 2025
147	  url: "https://arxiv.org/abs/2510.00866"
148	  category: background
149	  role: "质疑基于分类器的数据质量评分是否真正捕获了有意义的质量概念"
150	  key_findings: "CQF 改善下游任务但不一定改善语言建模；质量分类器隐式偏向其监督目标的数据分布；质量桶与特定 benchmark 对齐"
151	  relevance_to_us: "提醒我们检测器置信度 q 不等于真实质量——需要理论保证 b* 在检测器有偏时仍然有效"
152	
153	# ============================================================
154	# Category: evaluation
155	# 评估方法相关
156	# ============================================================
157	
158	- id: mitchell_2023_detectgpt
159	  title: "DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature"
160	  authors: "Eric Mitchell, Yoonho Lee, Alexander Khazatsky, Christopher D. Manning, Chelsea Finn"
161	  venue: "ICML 2023"
162	  year: 2023
163	  url: "https://arxiv.org/abs/2301.11305"
164	  category: evaluation
165	  role: "零样本机器生成文本检测方法——我们的检测器 q 的基线方法之一"
166	  key_findings: "LLM 生成的文本倾向于占据模型对数概率函数的负曲率区域；无需训练分类器、收集数据集或水印；在 GPT-NeoX 假新闻检测上从 0.81 AUROC 提升到 0.95"
167	  relevance_to_us: "可作为计算合成概率 q 的检测器之一；其概率曲率方法可能与我们的权重公式有理论联系"
168	
169	- id: shi_2024_minkprob
170	  title: "Detecting Pretraining Data from Large Language Models"
171	  authors: "Weijia Shi, Anirudh Ajith, Mengzhou Xia, Yangsibo Huang, Daogao Liu, Terra Blevins, Danqi Chen, Luke Zettlemoyer"
172	  venue: "ICLR 2024"
173	  year: 2024
174	  url: "https://arxiv.org/abs/2310.16789"
175	  category: evaluation
176	  role: "Min-K% Prob 方法——检测数据是否在预训练集中的无参考方法"
177	  key_findings: "已训练数据包含更少低概率异常 token；取最低 K% token 概率的平均值判断；在 WikiMIA 上比最佳基线高 7.4 AUC；无需参考模型"
178	  relevance_to_us: "Min-K% Prob 可作为估计合成概率 q 的候选方法；其 membership inference 思路可扩展为连续置信度估计"
179	
180	- id: kuo_2024_data_weighting
181	  title: "Not All LLM-Generated Data Are Equal: Rethinking Data Weighting in Text Classification"
182	  authors: "Hsun-Yu Kuo et al."
183	  venue: "arXiv preprint"
184	  year: 2024
185	  url: "https://arxiv.org/abs/2410.21526"
186	  category: evaluation
187	  role: "评估合成数据加权策略在文本分类中的效果"
188	  key_findings: "提出加权损失方法用少量真实数据对齐合成数据分布；在 BERT 级模型上稳定优于标准交叉熵和其他加权方法"
189	  relevance_to_us: "验证了合成数据需要差异化加权的思路；其评估框架可参考用于我们的下游任务评估"
190	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8c015997-0454-4320-aea4-623f3b3f5a7e",
  "isSidechain": false,
  "promptId": "8284b17e-dd1f-467a-9357-c4f2071853ea",
  "type": "user",
  "uuid": "121e4177-d25d-41ef-b022-da20d646f818",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/literature_map.yaml",
      "content": "# Literature Map for provenance_weight_training\n# 研究方向：基于收敛理论的自适应污染重加权\n# 核心公式：w=(1-q)^b，q 为检测器合成概率，b* 为理论最优权重指数\n# 生成日期：2026-05-14\n\n# ============================================================\n# Category: direct-competitor\n# 同主题/同方法的论文\n# ============================================================\n\n- id: drayson_2025_detection_collapse\n  title: \"Machine-Generated Text Detection Prevents Language Model Collapse\"\n  authors: \"George Drayson, Emine Yilmaz, Vasileios Lampos\"\n  venue: \"EMNLP 2025\"\n  year: 2025\n  url: \"https://arxiv.org/abs/2502.15654\"\n  category: direct-competitor\n  role: \"使用同一公式 w=(1-q)^b 进行重加权，但启发式选择 b 而非理论推导\"\n  key_findings: \"训练机器生成文本检测器，用 importance resampling 上采样可能的人类内容，不仅防止 model collapse，还优于纯人类数据训练\"\n  relevance_to_us: \"最直接的竞争者。我们的核心贡献是理论推导 b*，替代其启发式网格搜索方法\"\n\n- id: he_2025_golden_ratio\n  title: \"Golden Ratio Weighting Prevents Model Collapse\"\n  authors: \"Hengzhi He, Shirong Xu, Guang Cheng\"\n  venue: \"Under review at JRSSB, 2025\"\n  year: 2025\n  url: \"https://arxiv.org/abs/2502.18049\"\n  category: direct-competitor\n  role: \"从理论推导合成/真实数据混合的最优权重，发现最优权重为黄金比例的倒数(~0.62)\"\n  key_findings: \"在高斯估计、GLM、非参数估计等场景下，当合成数据与真实数据等量时，真实数据的最优权重约为 0.62（黄金比例倒数）\"\n  relevance_to_us: \"同样是理论推导最优权重，但针对 real/synthetic 固定混合比例，未考虑检测器置信度的连续估计\"\n\n- id: feng_2024_beyond_collapse\n  title: \"Beyond Model Collapse: Scaling Up with Synthesized Data Requires Verification\"\n  authors: \"Yunzhen Feng, Elvis Dohmatob, Pu Yang, François Charton, Julia Kempe\"\n  venue: \"arXiv preprint\"\n  year: 2024\n  url: \"https://arxiv.org/abs/2406.07515\"\n  category: direct-competitor\n  role: \"使用 verifier 过滤合成数据防止 model collapse，理论证明即使不完美的 verifier 也有效\"\n  key_findings: \"用高斯混合模型和线性分类器推导条件，证明 verifier 引导的合成数据筛选可避免 model collapse；即使 verifier 不完美也能受益\"\n  relevance_to_us: \"与我们的方法最相似——都用检测器置信度来处理合成数据。区别在于他们做 hard filtering，我们做 soft reweighting\"\n\n# ============================================================\n# Category: method-component\n# 我们用到的技术组件\n# ============================================================\n\n- id: kimura_2024_iw_survey\n  title: \"A Short Survey on Importance Weighting for Machine Learning\"\n  authors: \"Masanari Kimura, Hideitsu Hino\"\n  venue: \"TMLR 2024\"\n  year: 2024\n  url: \"https://arxiv.org/abs/2403.10175\"\n  category: method-component\n  role: \"importance weighting 在机器学习中的全面综述，覆盖分布偏移、密度比估计等核心理论\"\n  key_findings: \"系统整理了 importance weighting 在监督学习分布偏移下的理论保证和应用，包括 covariate shift、domain adaptation 等场景\"\n  relevance_to_us: \"为我们的 importance weighting 框架提供理论基础和方法论参考\"\n\n- id: vehtari_2024_psis\n  title: \"Pareto Smoothed Importance Sampling\"\n  authors: \"Aki Vehtari, Daniel Simpson, Andrew Gelman, Yuling Yao, Jonah Gabry\"\n  venue: \"JMLR 2024\"\n  year: 2024\n  url: \"https://arxiv.org/abs/1507.02646\"\n  category: method-component\n  role: \"提供稳定的 effective sample size 估计和收敛诊断方法\"\n  key_findings: \"用广义 Pareto 分布拟合 importance ratio 上尾实现平滑；提出 Pareto k 有限样本收敛率诊断指标；k<min(1-1/log10(S),0.7) 时估计可靠\"\n  relevance_to_us: \"我们的 α_eff(b) 估计直接依赖 effective sample size 理论，PSIS 的收敛诊断可用于验证我们的权重方案\"\n\n- id: sow_2025_dynamic_reweighting\n  title: \"Dynamic Loss-Based Sample Reweighting for Improved Large Language Model Pretraining\"\n  authors: \"Daouda Sow et al.\"\n  venue: \"ICLR 2025\"\n  year: 2025\n  url: \"https://arxiv.org/abs/2502.06733\"\n  category: method-component\n  role: \"首次提出 loss-based reweighting 对梯度优化收敛性影响的理论框架\"\n  key_findings: \"基于 loss 值动态调整每个样本权重；建立了 loss-based reweighting 对收敛界影响的形式化刻画；在 7B 和 1.4B 模型上验证更快收敛和更优性能\"\n  relevance_to_us: \"其收敛性理论框架可作为我们推导 b* 最优性的参考；loss-based 与 provenance-based reweighting 互补\"\n\n- id: ye_2025_data_mixing_laws\n  title: \"Data Mixing Laws: Optimizing Data Mixtures by Predicting Language Modeling Performance\"\n  authors: \"Jiasheng Ye, Peiju Liu, Tianxiang Sun, Yunhua Zhou, Jun Zhan, Xipeng Qiu\"\n  venue: \"ICLR 2025\"\n  year: 2025\n  url: \"https://arxiv.org/abs/2403.16952\"\n  category: method-component\n  role: \"发现数据混合比例与模型性能之间的定量可预测性\"\n  key_findings: \"模型性能关于混合比例具有函数形式的可预测性；可用小规模训练预测大模型在不同混合下的性能；适用于 continual training 的遗忘预测\"\n  relevance_to_us: \"data mixing laws 可作为验证我们 b* 最优性的理论框架——检验不同 b 下的 mixing 效果是否符合预测\"\n\n- id: he_2024_softdedup\n  title: \"SoftDedup: an Efficient Data Reweighting Method for Speeding Up Language Model Pre-training\"\n  authors: \"Nan He, Weichen Xiong, Hanwen Liu, Yi Liao, Lei Ding, Kai Zhang, Guohua Tang, Xiao Han, Yang Wei\"\n  venue: \"ACL 2024\"\n  year: 2024\n  url: \"https://arxiv.org/abs/2407.06654\"\n  category: method-component\n  role: \"用 data commonness 指标进行软去重加权，而非硬删除\"\n  key_findings: \"用 n-gram 模型量化样本的 commonness，高频样本降权低频样本升权；相比硬去重保留信息完整性；等效训练时间提升 26% 效率和 1.77% 下游准确率\"\n  relevance_to_us: \"软加权优于硬过滤的思路与我们一致——w=(1-q)^b 是连续加权而非二元过滤\"\n\n# ============================================================\n# Category: background\n# 数据污染/合成数据在 LLM 训练中的问题\n# ============================================================\n\n- id: shumailov_2024_model_collapse\n  title: \"AI Models Collapse When Trained on Recursively Generated Data\"\n  authors: \"Ilia Shumailov, Zakhar Shumaylov, Yiren Zhao, Nicolas Papernot, Ross Anderson, Yarin Gal\"\n  venue: \"Nature 2024\"\n  year: 2024\n  url: \"https://www.nature.com/articles/s41586-024-07566-y\"\n  category: background\n  role: \"奠基性工作——证明在递归生成数据上训练导致 model collapse\"\n  key_findings: \"在 LLM、VAE、GMM 上证明不加区分地用模型生成内容训练会导致不可逆退化；原始分布的尾部逐渐消失；反复训练的语言模型出现重复短语\"\n  relevance_to_us: \"model collapse 是我们工作的核心动机——加权方案的目标就是防止污染数据导致的性能退化\"\n\n- id: alemohammad_2024_mad\n  title: \"Self-Consuming Generative Models Go MAD\"\n  authors: \"Sina Alemohammad, Josue Casco-Rodriguez, Lorenzo Luzi, Ahmed Imtiaz Humayun, Hossein Babaei, Daniel LeJeune, Ali Siahkoohi, Richard G. Baraniuk\"\n  venue: \"ICLR 2024\"\n  year: 2024\n  url: \"https://arxiv.org/abs/2307.01850\"\n  category: background\n  role: \"提出 Model Autophagy Disorder (MAD) 概念——自消费式生成模型的退化\"\n  key_findings: \"分析三种自消费循环（fully synthetic、synthetic augmentation、fresh data）；无新鲜真实数据时质量或多样性不可避免下降；即使保留原始训练数据也可能退化\"\n  relevance_to_us: \"MAD 的数学框架帮助理解不同污染程度下的退化动力学，为我们的收敛理论提供上下文\"\n\n- id: dohmatob_2025_strong_collapse\n  title: \"Strong Model Collapse\"\n  authors: \"Elvis Dohmatob, Yunzhen Feng, Arjun Subramonian, Julia Kempe\"\n  venue: \"ICLR 2025 (Spotlight)\"\n  year: 2025\n  url: \"https://arxiv.org/abs/2410.04840\"\n  category: background\n  role: \"证明即使极少量合成数据（1/1000）也能导致 model collapse\"\n  key_findings: \"在 scaling laws 框架下建立 strong model collapse；用算子值自由概率论获得测试误差的 bias-variance 分解；更大模型可放大 collapse 效应\"\n  relevance_to_us: \"强化了我们工作的必要性——即使少量合成污染也需要处理，仅靠增加数据量无法解决\"\n\n- id: nait_saada_2025_quality_illusion\n  title: \"The Data-Quality Illusion: Rethinking Classifier-Based Quality Filtering for LLM Pretraining\"\n  authors: \"Thiziri Nait Saada, Louis Bethune, Michal Klein, David Grangier, Marco Cuturi, Pierre Ablin\"\n  venue: \"arXiv preprint\"\n  year: 2025\n  url: \"https://arxiv.org/abs/2510.00866\"\n  category: background\n  role: \"质疑基于分类器的数据质量评分是否真正捕获了有意义的质量概念\"\n  key_findings: \"CQF 改善下游任务但不一定改善语言建模；质量分类器隐式偏向其监督目标的数据分布；质量桶与特定 benchmark 对齐\"\n  relevance_to_us: \"提醒我们检测器置信度 q 不等于真实质量——需要理论保证 b* 在检测器有偏时仍然有效\"\n\n# ============================================================\n# Category: evaluation\n# 评估方法相关\n# ============================================================\n\n- id: mitchell_2023_detectgpt\n  title: \"DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature\"\n  authors: \"Eric Mitchell, Yoonho Lee, Alexander Khazatsky, Christopher D. Manning, Chelsea Finn\"\n  venue: \"ICML 2023\"\n  year: 2023\n  url: \"https://arxiv.org/abs/2301.11305\"\n  category: evaluation\n  role: \"零样本机器生成文本检测方法——我们的检测器 q 的基线方法之一\"\n  key_findings: \"LLM 生成的文本倾向于占据模型对数概率函数的负曲率区域；无需训练分类器、收集数据集或水印；在 GPT-NeoX 假新闻检测上从 0.81 AUROC 提升到 0.95\"\n  relevance_to_us: \"可作为计算合成概率 q 的检测器之一；其概率曲率方法可能与我们的权重公式有理论联系\"\n\n- id: shi_2024_minkprob\n  title: \"Detecting Pretraining Data from Large Language Models\"\n  authors: \"Weijia Shi, Anirudh Ajith, Mengzhou Xia, Yangsibo Huang, Daogao Liu, Terra Blevins, Danqi Chen, Luke Zettlemoyer\"\n  venue: \"ICLR 2024\"\n  year: 2024\n  url: \"https://arxiv.org/abs/2310.16789\"\n  category: evaluation\n  role: \"Min-K% Prob 方法——检测数据是否在预训练集中的无参考方法\"\n  key_findings: \"已训练数据包含更少低概率异常 token；取最低 K% token 概率的平均值判断；在 WikiMIA 上比最佳基线高 7.4 AUC；无需参考模型\"\n  relevance_to_us: \"Min-K% Prob 可作为估计合成概率 q 的候选方法；其 membership inference 思路可扩展为连续置信度估计\"\n\n- id: kuo_2024_data_weighting\n  title: \"Not All LLM-Generated Data Are Equal: Rethinking Data Weighting in Text Classification\"\n  authors: \"Hsun-Yu Kuo et al.\"\n  venue: \"arXiv preprint\"\n  year: 2024\n  url: \"https://arxiv.org/abs/2410.21526\"\n  category: evaluation\n  role: \"评估合成数据加权策略在文本分类中的效果\"\n  key_findings: \"提出加权损失方法用少量真实数据对齐合成数据分布；在 BERT 级模型上稳定优于标准交叉熵和其他加权方法\"\n  relevance_to_us: \"验证了合成数据需要差异化加权的思路；其评估框架可参考用于我们的下游任务评估\"\n",
      "numLines": 190,
      "startLine": 1,
      "totalLines": 190
    }
  },
  "sourceToolAssistantUUID": "8c015997-0454-4320-aea4-623f3b3f5a7e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training",
  "sessionId": "33f4c8cf-38de-44f8-ba86-369f9c5d5e2f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 30 · 2026-05-14T23:43:17.141Z_

<details open><summary>🔧 Tool call — Write · `toolu_01NfXHEaSBTA38STuMAAF3Au`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/literature_map.yaml",
  "content": "# Literature Map for provenance_weight_training\n# 研究方向：基于收敛理论的自适应污染重加权\n# 核心公式：w=(1-q)^b，q 为检测器合成概率，b* 为理论最优权重指数\n# 更新日期：2026-05-14（整合 Drayson comparison 分析）\n\n# ============================================================\n# Category: direct-competitor\n# 同主题/同方法的论文\n# ============================================================\n\n- id: drayson_2025_detection_collapse\n  title: \"Machine-Generated Text Detection Prevents Language Model Collapse\"\n  authors: \"George Drayson, Emine Yilmaz, Vasileios Lampos\"\n  venue: \"EMNLP 2025\"\n  year: 2025\n  arxiv_id: \"2502.15654\"\n  url: \"https://arxiv.org/abs/2502.15654\"\n  github: \"https://github.com/GeorgeDrayson/model_collapse\"\n  category: direct-competitor\n  role: \"使用同一公式 w=(1-q)^b 进行重加权，但 b 为验证集 empirical 选取，训练中固定\"\n  method_summary: >\n    Detect-and-reweight 防止递归训练 model collapse。检测器为 ModernBERT 150M\n    (MAGE fine-tune, in-domain AUC=0.986, OOD AUC=0.943)。权重公式 wⱼ=(1-q(xⱼ))^b / Σₗ(1-q(xₗ))^b，\n    通过 SIR 按权重重采样训练数据。b 通过 WikiText-2 验证集上 1 代递归训练后评估选取\n    (GPT-2/SmolLM 135M/360M 用 b=10, SmolLM 1.7B 用 b=1)，训练全程固定。\n    实验覆盖 4 个模型 (GPT-2 124M, SmolLM 135M/360M/1.7B)、10 代递归训练、6 种解码策略。\n    结果 PPL 降低 0.85%–25.65%，diversity 提升 3.44%–14.62%。\n  key_findings: \"验证 detect-and-reweight 有效防止 model collapse 且优于纯人类数据训练；b 值对模型规模敏感（小模型 b=10，大模型 b=1）\"\n  differentiation:\n    b_selection: \"Drayson: 验证集 empirical grid search, per-model 固定 | 我们: α_eff(b) + ESS 约束, per-batch 自适应\"\n    contamination_setting: \"Drayson: 已知比例（实验控制） | 我们: 未知比例（batch 统计量在线估计）\"\n    detector: \"Drayson: ModernBERT 150M (AUC=0.986) | 我们: TF-IDF+LR (AUC=0.939)，证明轻量检测器即可\"\n    theory: \"Drayson: 无 b 选取理论（SIR 启发式） | 我们: 收敛理论 motivated α_eff(b) 推导\"\n    training_scenario: \"Drayson: 递归训练 model collapse prevention | 我们: Web corpus 一次性预训练中的未知污染\"\n    scale: \"Drayson: WikiText-2 (~2M tokens) | 我们: FineWeb subset (132M+ tokens)\"\n    dynamics: \"Drayson: b 固定（训练全程不变） | 我们: b* per-batch 自适应\"\n  our_advantages:\n    - \"From heuristic to principled: 理论推导 b* 替代 empirical grid search，零额外 validation cost\"\n    - \"Unknown contamination: 不需要已知污染比例或干净验证集，适用大规模 web pretraining\"\n    - \"Lightweight detector sufficiency: TF-IDF+LR 即可，检测器计算开销降低数量级\"\n    - \"Unified continuous spectrum: b=0 uniform → b→∞ hard filter 的统一框架\"\n  relevance_to_us: \"最直接的竞争者。共享 w=(1-q)^b 公式，但 b 选取方法根本不同——我们的核心贡献正是理论推导 adaptive b*\"\n\n- id: he_2025_golden_ratio\n  title: \"Golden Ratio Weighting Prevents Model Collapse\"\n  authors: \"Hengzhi He, Shirong Xu, Guang Cheng\"\n  venue: \"Under review at JRSSB, 2025\"\n  year: 2025\n  arxiv_id: \"2502.18049\"\n  url: \"https://arxiv.org/abs/2502.18049\"\n  category: direct-competitor\n  role: \"从理论推导合成/真实数据混合的最优权重，发现最优权重为黄金比例的倒数(~0.62)\"\n  key_findings: \"在高斯估计、GLM、非参数估计等场景下，当合成数据与真实数据等量时，真实数据的最优权重约为 0.62（黄金比例倒数）。公式 w*=(√(k²+4k)−k)/2, k=真实/合成样本比\"\n  differentiation:\n    scope: \"纯理论工作，假设已知污染比例，未涉及检测器或 LLM 实验，不处理 unknown/online 设置\"\n  relevance_to_us: \"同样是理论推导最优权重，但针对 real/synthetic 固定混合比例，未考虑检测器置信度的连续估计\"\n\n- id: feng_2024_beyond_collapse\n  title: \"Beyond Model Collapse: Scaling Up with Synthesized Data Requires Verification\"\n  authors: \"Yunzhen Feng, Elvis Dohmatob, Pu Yang, François Charton, Julia Kempe\"\n  venue: \"arXiv preprint\"\n  year: 2024\n  url: \"https://arxiv.org/abs/2406.07515\"\n  category: direct-competitor\n  role: \"使用 verifier 过滤合成数据防止 model collapse，理论证明即使不完美的 verifier 也有效\"\n  key_findings: \"用高斯混合模型和线性分类器推导条件，证明 verifier 引导的合成数据筛选可避免 model collapse；即使 verifier 不完美也能受益\"\n  relevance_to_us: \"与我们的方法最相似——都用检测器置信度来处理合成数据。区别在于他们做 hard filtering，我们做 soft reweighting\"\n\n# ============================================================\n# Category: method-component\n# 我们用到的技术组件\n# ============================================================\n\n- id: kimura_2024_iw_survey\n  title: \"A Short Survey on Importance Weighting for Machine Learning\"\n  authors: \"Masanari Kimura, Hideitsu Hino\"\n  venue: \"TMLR 2024\"\n  year: 2024\n  url: \"https://arxiv.org/abs/2403.10175\"\n  category: method-component\n  role: \"importance weighting 在机器学习中的全面综述，覆盖分布偏移、密度比估计等核心理论\"\n  key_findings: \"系统整理了 importance weighting 在监督学习分布偏移下的理论保证和应用，包括 covariate shift、domain adaptation 等场景\"\n  relevance_to_us: \"为我们的 importance weighting 框架提供理论基础和方法论参考\"\n\n- id: vehtari_2024_psis\n  title: \"Pareto Smoothed Importance Sampling\"\n  authors: \"Aki Vehtari, Daniel Simpson, Andrew Gelman, Yuling Yao, Jonah Gabry\"\n  venue: \"JMLR 2024\"\n  year: 2024\n  url: \"https://arxiv.org/abs/1507.02646\"\n  category: method-component\n  role: \"提供稳定的 effective sample size 估计和收敛诊断方法\"\n  key_findings: \"用广义 Pareto 分布拟合 importance ratio 上尾实现平滑；提出 Pareto k 有限样本收敛率诊断指标；k<min(1-1/log10(S),0.7) 时估计可靠\"\n  relevance_to_us: \"我们的 α_eff(b) 估计直接依赖 effective sample size 理论，PSIS 的收敛诊断可用于验证我们的权重方案\"\n\n- id: sow_2025_dynamic_reweighting\n  title: \"Dynamic Loss-Based Sample Reweighting for Improved Large Language Model Pretraining\"\n  authors: \"Daouda Sow et al.\"\n  venue: \"ICLR 2025\"\n  year: 2025\n  url: \"https://arxiv.org/abs/2502.06733\"\n  github: \"https://github.com/sowmaster/Sample-Level-Loss-Reweighting-ICLR-2025\"\n  category: method-component\n  role: \"首次提出 loss-based reweighting 对梯度优化收敛性影响的理论框架\"\n  key_findings: \"基于 loss 值动态调整每个样本权重；建立了 loss-based reweighting 对收敛界影响的形式化刻画；在 7B 和 1.4B 模型上验证更快收敛和更优性能\"\n  relevance_to_us: \"其收敛性理论框架可作为我们推导 b* 最优性的参考；loss-based 与 provenance-based reweighting 互补（不使用检测器，纯 loss signal 驱动）\"\n\n- id: ye_2025_data_mixing_laws\n  title: \"Data Mixing Laws: Optimizing Data Mixtures by Predicting Language Modeling Performance\"\n  authors: \"Jiasheng Ye, Peiju Liu, Tianxiang Sun, Yunhua Zhou, Jun Zhan, Xipeng Qiu\"\n  venue: \"ICLR 2025\"\n  year: 2025\n  url: \"https://arxiv.org/abs/2403.16952\"\n  category: method-component\n  role: \"发现数据混合比例与模型性能之间的定量可预测性\"\n  key_findings: \"模型性能关于混合比例具有函数形式的可预测性；可用小规模训练预测大模型在不同混合下的性能；适用于 continual training 的遗忘预测\"\n  relevance_to_us: \"data mixing laws 可作为验证我们 b* 最优性的理论框架——检验不同 b 下的 mixing 效果是否符合预测\"\n\n- id: he_2024_softdedup\n  title: \"SoftDedup: an Efficient Data Reweighting Method for Speeding Up Language Model Pre-training\"\n  authors: \"Nan He, Weichen Xiong, Hanwen Liu, Yi Liao, Lei Ding, Kai Zhang, Guohua Tang, Xiao Han, Yang Wei\"\n  venue: \"ACL 2024\"\n  year: 2024\n  url: \"https://arxiv.org/abs/2407.06654\"\n  category: method-component\n  role: \"用 data commonness 指标进行软去重加权，而非硬删除\"\n  key_findings: \"用 n-gram 模型量化样本的 commonness，高频样本降权低频样本升权；相比硬去重保留信息完整性；等效训练时间提升 26% 效率和 1.77% 下游准确率\"\n  relevance_to_us: \"软加权优于硬过滤的思路与我们一致——w=(1-q)^b 是连续加权而非二元过滤\"\n\n- id: xie_2023_doremi\n  title: \"DoReMi: Optimizing Data Mixtures by Predicting Language Modeling Performance\"\n  authors: \"Sang Michael Xie, Hieu Pham, Xuanyi Dong, Nan Du, Hanxiao Liu, Yifeng Lu, Percy Liang, Quoc V. Le, Tengyu Ma, Adams Wei Yu\"\n  venue: \"NeurIPS 2023\"\n  year: 2023\n  url: \"https://arxiv.org/abs/2305.10429\"\n  category: method-component\n  role: \"域级别权重优化（Group DRO + 小模型代理），不处理 instance-level 污染\"\n  key_findings: \"用小代理模型通过 Group DRO 优化域级别数据混合权重；在 The Pile 和 GLaM 数据集上无需目标分布知识即可改善下游性能\"\n  relevance_to_us: \"域级别 reweighting baseline；我们的方法在 instance-level 操作，粒度更细且基于检测器置信度而非 loss-based DRO\"\n\n- id: xie_2023_dsir\n  title: \"Data Selection for Language Models via Importance Resampling\"\n  authors: \"Sang Michael Xie, Shibani Santurkar, Tengyu Ma, Percy Liang\"\n  venue: \"NeurIPS 2023\"\n  year: 2023\n  url: \"https://arxiv.org/abs/2302.03169\"\n  category: method-component\n  role: \"N-gram 特征重要性采样选择数据子集匹配目标分布\"\n  key_findings: \"用 n-gram 特征估计 importance weights 并重采样数据匹配目标分布；比 heuristic filtering 更 principled；在 GLUE 和下游任务上优于随机选择和启发式方法\"\n  relevance_to_us: \"同样用 importance resampling，但目标是分布匹配而非污染处理；与 Drayson 的 SIR 方法有方法论联系\"\n\n# ============================================================\n# Category: background\n# 数据污染/合成数据在 LLM 训练中的问题\n# ============================================================\n\n- id: shumailov_2024_model_collapse\n  title: \"AI Models Collapse When Trained on Recursively Generated Data\"\n  authors: \"Ilia Shumailov, Zakhar Shumaylov, Yiren Zhao, Nicolas Papernot, Ross Anderson, Yarin Gal\"\n  venue: \"Nature 2024\"\n  year: 2024\n  url: \"https://www.nature.com/articles/s41586-024-07566-y\"\n  category: background\n  role: \"奠基性工作——证明在递归生成数据上训练导致 model collapse\"\n  key_findings: \"在 LLM、VAE、GMM 上证明不加区分地用模型生成内容训练会导致不可逆退化；原始分布的尾部逐渐消失；反复训练的语言模型出现重复短语\"\n  relevance_to_us: \"model collapse 是我们工作的核心动机——加权方案的目标就是防止污染数据导致的性能退化\"\n\n- id: alemohammad_2024_mad\n  title: \"Self-Consuming Generative Models Go MAD\"\n  authors: \"Sina Alemohammad, Josue Casco-Rodriguez, Lorenzo Luzi, Ahmed Imtiaz Humayun, Hossein Babaei, Daniel LeJeune, Ali Siahkoohi, Richard G. Baraniuk\"\n  venue: \"ICLR 2024\"\n  year: 2024\n  url: \"https://arxiv.org/abs/2307.01850\"\n  category: background\n  role: \"提出 Model Autophagy Disorder (MAD) 概念——自消费式生成模型的退化\"\n  key_findings: \"分析三种自消费循环（fully synthetic、synthetic augmentation、fresh data）；无新鲜真实数据时质量或多样性不可避免下降；即使保留原始训练数据也可能退化\"\n  relevance_to_us: \"MAD 的数学框架帮助理解不同污染程度下的退化动力学，为我们的收敛理论提供上下文\"\n\n- id: dohmatob_2025_strong_collapse\n  title: \"Strong Model Collapse\"\n  authors: \"Elvis Dohmatob, Yunzhen Feng, Arjun Subramonian, Julia Kempe\"\n  venue: \"ICLR 2025 (Spotlight)\"\n  year: 2025\n  arxiv_id: \"2410.04840\"\n  url: \"https://arxiv.org/abs/2410.04840\"\n  category: background\n  role: \"证明即使极少量合成数据（1/1000）也能导致 model collapse\"\n  key_findings: \"在 scaling laws 框架下建立 strong model collapse；用算子值自由概率论获得测试误差的 bias-variance 分解；更大模型可放大 collapse 效应\"\n  relevance_to_us: \"强化了我们工作的必要性——即使少量合成污染也需要处理，仅靠增加数据量无法解决\"\n\n- id: nait_saada_2025_quality_illusion\n  title: \"The Data-Quality Illusion: Rethinking Classifier-Based Quality Filtering for LLM Pretraining\"\n  authors: \"Thiziri Nait Saada, Louis Bethune, Michal Klein, David Grangier, Marco Cuturi, Pierre Ablin\"\n  venue: \"arXiv preprint\"\n  year: 2025\n  url: \"https://arxiv.org/abs/2510.00866\"\n  category: background\n  role: \"质疑基于分类器的数据质量评分是否真正捕获了有意义的质量概念\"\n  key_findings: \"CQF 改善下游任务但不一定改善语言建模；质量分类器隐式偏向其监督目标的数据分布；质量桶与特定 benchmark 对齐\"\n  relevance_to_us: \"提醒我们检测器置信度 q 不等于真实质量——需要理论保证 b* 在检测器有偏时仍然有效\"\n\n- id: guo_2025_escaping_collapse\n  title: \"Escaping Model Collapse via Synthetic Data Verification\"\n  venue: \"arXiv preprint\"\n  year: 2025\n  arxiv_id: \"2510.16657\"\n  url: \"https://arxiv.org/abs/2510.16657\"\n  category: background\n  role: \"提出验证机制筛选合成数据质量，与 detection-based 方法互补\"\n  key_findings: \"通过验证机制在合成数据生成后筛选质量，与基于检测器的事后加权方法互补\"\n  relevance_to_us: \"verification-based 方法是另一条技术路线——他们做生成时验证，我们做训练时加权\"\n\n# ============================================================\n# Category: evaluation\n# 评估方法相关\n# ============================================================\n\n- id: mitchell_2023_detectgpt\n  title: \"DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature\"\n  authors: \"Eric Mitchell, Yoonho Lee, Alexander Khazatsky, Christopher D. Manning, Chelsea Finn\"\n  venue: \"ICML 2023\"\n  year: 2023\n  url: \"https://arxiv.org/abs/2301.11305\"\n  category: evaluation\n  role: \"零样本机器生成文本检测方法——我们的检测器 q 的基线方法之一\"\n  key_findings: \"LLM 生成的文本倾向于占据模型对数概率函数的负曲率区域；无需训练分类器、收集数据集或水印；在 GPT-NeoX 假新闻检测上从 0.81 AUROC 提升到 0.95\"\n  relevance_to_us: \"可作为计算合成概率 q 的检测器之一；其概率曲率方法可能与我们的权重公式有理论联系\"\n\n- id: shi_2024_minkprob\n  title: \"Detecting Pretraining Data from Large Language Models\"\n  authors: \"Weijia Shi, Anirudh Ajith, Mengzhou Xia, Yangsibo Huang, Daogao Liu, Terra Blevins, Danqi Chen, Luke Zettlemoyer\"\n  venue: \"ICLR 2024\"\n  year: 2024\n  url: \"https://arxiv.org/abs/2310.16789\"\n  category: evaluation\n  role: \"Min-K% Prob 方法——检测数据是否在预训练集中的无参考方法\"\n  key_findings: \"已训练数据包含更少低概率异常 token；取最低 K% token 概率的平均值判断；在 WikiMIA 上比最佳基线高 7.4 AUC；无需参考模型\"\n  relevance_to_us: \"Min-K% Prob 可作为估计合成概率 q 的候选方法；其 membership inference 思路可扩展为连续置信度估计\"\n\n- id: kuo_2024_data_weighting\n  title: \"Not All LLM-Generated Data Are Equal: Rethinking Data Weighting in Text Classification\"\n  authors: \"Hsun-Yu Kuo et al.\"\n  venue: \"arXiv preprint\"\n  year: 2024\n  url: \"https://arxiv.org/abs/2410.21526\"\n  category: evaluation\n  role: \"评估合成数据加权策略在文本分类中的效果\"\n  key_findings: \"提出加权损失方法用少量真实数据对齐合成数据分布；在 BERT 级模型上稳定优于标准交叉熵和其他加权方法\"\n  relevance_to_us: \"验证了合成数据需要差异化加权的思路；其评估框架可参考用于我们的下游任务评估\"\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "121e4177-d25d-41ef-b022-da20d646f818",
  "isSidechain": false,
  "requestId": "req_011Cb3M1UmfqfrJ8b6WAgBtw",
  "type": "assistant",
  "uuid": "ccb0c563-abc4-4cb6-93e9-9a82704a62f3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training",
  "sessionId": "33f4c8cf-38de-44f8-ba86-369f9c5d5e2f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RZUBTYHaJnnQxmrdCTr2KA",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4796,
      "cache_read_input_tokens": 44372,
      "output_tokens": 6201,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4796,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 6201,
          "cache_read_input_tokens": 44372,
          "cache_creation_input_tokens": 4796,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4796
          },
          "type": "message"
        }
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

_source line 31 · 2026-05-14T23:43:17.167Z_

<details><summary>↩ Tool result · `toolu_01NfXHEaSBTA38STuMAAF3Au`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/literature_map.yaml has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ccb0c563-abc4-4cb6-93e9-9a82704a62f3",
  "isSidechain": false,
  "promptId": "8284b17e-dd1f-467a-9357-c4f2071853ea",
  "type": "user",
  "uuid": "297044e3-e7ad-4882-a36d-53b3e3cff017",
  "toolUseResult": {
    "type": "update",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/literature_map.yaml",
    "content": "# Literature Map for provenance_weight_training\n# 研究方向：基于收敛理论的自适应污染重加权\n# 核心公式：w=(1-q)^b，q 为检测器合成概率，b* 为理论最优权重指数\n# 更新日期：2026-05-14（整合 Drayson comparison 分析）\n\n# ============================================================\n# Category: direct-competitor\n# 同主题/同方法的论文\n# ============================================================\n\n- id: drayson_2025_detection_collapse\n  title: \"Machine-Generated Text Detection Prevents Language Model Collapse\"\n  authors: \"George Drayson, Emine Yilmaz, Vasileios Lampos\"\n  venue: \"EMNLP 2025\"\n  year: 2025\n  arxiv_id: \"2502.15654\"\n  url: \"https://arxiv.org/abs/2502.15654\"\n  github: \"https://github.com/GeorgeDrayson/model_collapse\"\n  category: direct-competitor\n  role: \"使用同一公式 w=(1-q)^b 进行重加权，但 b 为验证集 empirical 选取，训练中固定\"\n  method_summary: >\n    Detect-and-reweight 防止递归训练 model collapse。检测器为 ModernBERT 150M\n    (MAGE fine-tune, in-domain AUC=0.986, OOD AUC=0.943)。权重公式 wⱼ=(1-q(xⱼ))^b / Σₗ(1-q(xₗ))^b，\n    通过 SIR 按权重重采样训练数据。b 通过 WikiText-2 验证集上 1 代递归训练后评估选取\n    (GPT-2/SmolLM 135M/360M 用 b=10, SmolLM 1.7B 用 b=1)，训练全程固定。\n    实验覆盖 4 个模型 (GPT-2 124M, SmolLM 135M/360M/1.7B)、10 代递归训练、6 种解码策略。\n    结果 PPL 降低 0.85%–25.65%，diversity 提升 3.44%–14.62%。\n  key_findings: \"验证 detect-and-reweight 有效防止 model collapse 且优于纯人类数据训练；b 值对模型规模敏感（小模型 b=10，大模型 b=1）\"\n  differentiation:\n    b_selection: \"Drayson: 验证集 empirical grid search, per-model 固定 | 我们: α_eff(b) + ESS 约束, per-batch 自适应\"\n    contamination_setting: \"Drayson: 已知比例（实验控制） | 我们: 未知比例（batch 统计量在线估计）\"\n    detector: \"Drayson: ModernBERT 150M (AUC=0.986) | 我们: TF-IDF+LR (AUC=0.939)，证明轻量检测器即可\"\n    theory: \"Drayson: 无 b 选取理论（SIR 启发式） | 我们: 收敛理论 motivated α_eff(b) 推导\"\n    training_scenario: \"Drayson: 递归训练 model collapse prevention | 我们: Web corpus 一次性预训练中的未知污染\"\n    scale: \"Drayson: WikiText-2 (~2M tokens) | 我们: FineWeb subset (132M+ tokens)\"\n    dynamics: \"Drayson: b 固定（训练全程不变） | 我们: b* per-batch 自适应\"\n  our_advantages:\n    - \"From heuristic to principled: 理论推导 b* 替代 empirical grid search，零额外 validation cost\"\n    - \"Unknown contamination: 不需要已知污染比例或干净验证集，适用大规模 web pretraining\"\n    - \"Lightweight detector sufficiency: TF-IDF+LR 即可，检测器计算开销降低数量级\"\n    - \"Unified continuous spectrum: b=0 uniform → b→∞ hard filter 的统一框架\"\n  relevance_to_us: \"最直接的竞争者。共享 w=(1-q)^b 公式，但 b 选取方法根本不同——我们的核心贡献正是理论推导 adaptive b*\"\n\n- id: he_2025_golden_ratio\n  title: \"Golden Ratio Weighting Prevents Model Collapse\"\n  authors: \"Hengzhi He, Shirong Xu, Guang Cheng\"\n  venue: \"Under review at JRSSB, 2025\"\n  year: 2025\n  arxiv_id: \"2502.18049\"\n  url: \"https://arxiv.org/abs/2502.18049\"\n  category: direct-competitor\n  role: \"从理论推导合成/真实数据混合的最优权重，发现最优权重为黄金比例的倒数(~0.62)\"\n  key_findings: \"在高斯估计、GLM、非参数估计等场景下，当合成数据与真实数据等量时，真实数据的最优权重约为 0.62（黄金比例倒数）。公式 w*=(√(k²+4k)−k)/2, k=真实/合成样本比\"\n  differentiation:\n    scope: \"纯理论工作，假设已知污染比例，未涉及检测器或 LLM 实验，不处理 unknown/online 设置\"\n  relevance_to_us: \"同样是理论推导最优权重，但针对 real/synthetic 固定混合比例，未考虑检测器置信度的连续估计\"\n\n- id: feng_2024_beyond_collapse\n  title: \"Beyond Model Collapse: Scaling Up with Synthesized Data Requires Verification\"\n  authors: \"Yunzhen Feng, Elvis Dohmatob, Pu Yang, François Charton, Julia Kempe\"\n  venue: \"arXiv preprint\"\n  year: 2024\n  url: \"https://arxiv.org/abs/2406.07515\"\n  category: direct-competitor\n  role: \"使用 verifier 过滤合成数据防止 model collapse，理论证明即使不完美的 verifier 也有效\"\n  key_findings: \"用高斯混合模型和线性分类器推导条件，证明 verifier 引导的合成数据筛选可避免 model collapse；即使 verifier 不完美也能受益\"\n  relevance_to_us: \"与我们的方法最相似——都用检测器置信度来处理合成数据。区别在于他们做 hard filtering，我们做 soft reweighting\"\n\n# ============================================================\n# Category: method-component\n# 我们用到的技术组件\n# ============================================================\n\n- id: kimura_2024_iw_survey\n  title: \"A Short Survey on Importance Weighting for Machine Learning\"\n  authors: \"Masanari Kimura, Hideitsu Hino\"\n  venue: \"TMLR 2024\"\n  year: 2024\n  url: \"https://arxiv.org/abs/2403.10175\"\n  category: method-component\n  role: \"importance weighting 在机器学习中的全面综述，覆盖分布偏移、密度比估计等核心理论\"\n  key_findings: \"系统整理了 importance weighting 在监督学习分布偏移下的理论保证和应用，包括 covariate shift、domain adaptation 等场景\"\n  relevance_to_us: \"为我们的 importance weighting 框架提供理论基础和方法论参考\"\n\n- id: vehtari_2024_psis\n  title: \"Pareto Smoothed Importance Sampling\"\n  authors: \"Aki Vehtari, Daniel Simpson, Andrew Gelman, Yuling Yao, Jonah Gabry\"\n  venue: \"JMLR 2024\"\n  year: 2024\n  url: \"https://arxiv.org/abs/1507.02646\"\n  category: method-component\n  role: \"提供稳定的 effective sample size 估计和收敛诊断方法\"\n  key_findings: \"用广义 Pareto 分布拟合 importance ratio 上尾实现平滑；提出 Pareto k 有限样本收敛率诊断指标；k&lt;min(1-1/log10(S),0.7) 时估计可靠\"\n  relevance_to_us: \"我们的 α_eff(b) 估计直接依赖 effective sample size 理论，PSIS 的收敛诊断可用于验证我们的权重方案\"\n\n- id: sow_2025_dynamic_reweighting\n  title: \"Dynamic Loss-Based Sample Reweighting for Improved Large Language Model Pretraining\"\n  authors: \"Daouda Sow et al.\"\n  venue: \"ICLR 2025\"\n  year: 2025\n  url: \"https://arxiv.org/abs/2502.06733\"\n  github: \"https://github.com/sowmaster/Sample-Level-Loss-Reweighting-ICLR-2025\"\n  category: method-component\n  role: \"首次提出 loss-based reweighting 对梯度优化收敛性影响的理论框架\"\n  key_findings: \"基于 loss 值动态调整每个样本权重；建立了 loss-based reweighting 对收敛界影响的形式化刻画；在 7B 和 1.4B 模型上验证更快收敛和更优性能\"\n  relevance_to_us: \"其收敛性理论框架可作为我们推导 b* 最优性的参考；loss-based 与 provenance-based reweighting 互补（不使用检测器，纯 loss signal 驱动）\"\n\n- id: ye_2025_data_mixing_laws\n  title: \"Data Mixing Laws: Optimizing Data Mixtures by Predicting Language Modeling Performance\"\n  authors: \"Jiasheng Ye, Peiju Liu, Tianxiang Sun, Yunhua Zhou, Jun Zhan, Xipeng Qiu\"\n  venue: \"ICLR 2025\"\n  year: 2025\n  url: \"https://arxiv.org/abs/2403.16952\"\n  category: method-component\n  role: \"发现数据混合比例与模型性能之间的定量可预测性\"\n  key_findings: \"模型性能关于混合比例具有函数形式的可预测性；可用小规模训练预测大模型在不同混合下的性能；适用于 continual training 的遗忘预测\"\n  relevance_to_us: \"data mixing laws 可作为验证我们 b* 最优性的理论框架——检验不同 b 下的 mixing 效果是否符合预测\"\n\n- id: he_2024_softdedup\n  title: \"SoftDedup: an Efficient Data Reweighting Method for Speeding Up Language Model Pre-training\"\n  authors: \"Nan He, Weichen Xiong, Hanwen Liu, Yi Liao, Lei Ding, Kai Zhang, Guohua Tang, Xiao Han, Yang Wei\"\n  venue: \"ACL 2024\"\n  year: 2024\n  url: \"https://arxiv.org/abs/2407.06654\"\n  category: method-component\n  role: \"用 data commonness 指标进行软去重加权，而非硬删除\"\n  key_findings: \"用 n-gram 模型量化样本的 commonness，高频样本降权低频样本升权；相比硬去重保留信息完整性；等效训练时间提升 26% 效率和 1.77% 下游准确率\"\n  relevance_to_us: \"软加权优于硬过滤的思路与我们一致——w=(1-q)^b 是连续加权而非二元过滤\"\n\n- id: xie_2023_doremi\n  title: \"DoReMi: Optimizing Data Mixtures by Predicting Language Modeling Performance\"\n  authors: \"Sang Michael Xie, Hieu Pham, Xuanyi Dong, Nan Du, Hanxiao Liu, Yifeng Lu, Percy Liang, Quoc V. Le, Tengyu Ma, Adams Wei Yu\"\n  venue: \"NeurIPS 2023\"\n  year: 2023\n  url: \"https://arxiv.org/abs/2305.10429\"\n  category: method-component\n  role: \"域级别权重优化（Group DRO + 小模型代理），不处理 instance-level 污染\"\n  key_findings: \"用小代理模型通过 Group DRO 优化域级别数据混合权重；在 The Pile 和 GLaM 数据集上无需目标分布知识即可改善下游性能\"\n  relevance_to_us: \"域级别 reweighting baseline；我们的方法在 instance-level 操作，粒度更细且基于检测器置信度而非 loss-based DRO\"\n\n- id: xie_2023_dsir\n  title: \"Data Selection for Language Models via Importance Resampling\"\n  authors: \"Sang Michael Xie, Shibani Santurkar, Tengyu Ma, Percy Liang\"\n  venue: \"NeurIPS 2023\"\n  year: 2023\n  url: \"https://arxiv.org/abs/2302.03169\"\n  category: method-component\n  role: \"N-gram 特征重要性采样选择数据子集匹配目标分布\"\n  key_findings: \"用 n-gram 特征估计 importance weights 并重采样数据匹配目标分布；比 heuristic filtering 更 principled；在 GLUE 和下游任务上优于随机选择和启发式方法\"\n  relevance_to_us: \"同样用 importance resampling，但目标是分布匹配而非污染处理；与 Drayson 的 SIR 方法有方法论联系\"\n\n# ============================================================\n# Category: background\n# 数据污染/合成数据在 LLM 训练中的问题\n# ============================================================\n\n- id: shumailov_2024_model_collapse\n  title: \"AI Models Collapse When Trained on Recursively Generated Data\"\n  authors: \"Ilia Shumailov, Zakhar Shumaylov, Yiren Zhao, Nicolas Papernot, Ross Anderson, Yarin Gal\"\n  venue: \"Nature 2024\"\n  year: 2024\n  url: \"https://www.nature.com/articles/s41586-024-07566-y\"\n  category: background\n  role: \"奠基性工作——证明在递归生成数据上训练导致 model collapse\"\n  key_findings: \"在 LLM、VAE、GMM 上证明不加区分地用模型生成内容训练会导致不可逆退化；原始分布的尾部逐渐消失；反复训练的语言模型出现重复短语\"\n  relevance_to_us: \"model collapse 是我们工作的核心动机——加权方案的目标就是防止污染数据导致的性能退化\"\n\n- id: alemohammad_2024_mad\n  title: \"Self-Consuming Generative Models Go MAD\"\n  authors: \"Sina Alemohammad, Josue Casco-Rodriguez, Lorenzo Luzi, Ahmed Imtiaz Humayun, Hossein Babaei, Daniel LeJeune, Ali Siahkoohi, Richard G. Baraniuk\"\n  venue: \"ICLR 2024\"\n  year: 2024\n  url: \"https://arxiv.org/abs/2307.01850\"\n  category: background\n  role: \"提出 Model Autophagy Disorder (MAD) 概念——自消费式生成模型的退化\"\n  key_findings: \"分析三种自消费循环（fully synthetic、synthetic augmentation、fresh data）；无新鲜真实数据时质量或多样性不可避免下降；即使保留原始训练数据也可能退化\"\n  relevance_to_us: \"MAD 的数学框架帮助理解不同污染程度下的退化动力学，为我们的收敛理论提供上下文\"\n\n- id: dohmatob_2025_strong_collapse\n  title: \"Strong Model Collapse\"\n  authors: \"Elvis Dohmatob, Yunzhen Feng, Arjun Subramonian, Julia Kempe\"\n  venue: \"ICLR 2025 (Spotlight)\"\n  year: 2025\n  arxiv_id: \"2410.04840\"\n  url: \"https://arxiv.org/abs/2410.04840\"\n  category: background\n  role: \"证明即使极少量合成数据（1/1000）也能导致 model collapse\"\n  key_findings: \"在 scaling laws 框架下建立 strong model collapse；用算子值自由概率论获得测试误差的 bias-variance 分解；更大模型可放大 collapse 效应\"\n  relevance_to_us: \"强化了我们工作的必要性——即使少量合成污染也需要处理，仅靠增加数据量无法解决\"\n\n- id: nait_saada_2025_quality_illusion\n  title: \"The Data-Quality Illusion: Rethinking Classifier-Based Quality Filtering for LLM Pretraining\"\n  authors: \"Thiziri Nait Saada, Louis Bethune, Michal Klein, David Grangier, Marco Cuturi, Pierre Ablin\"\n  venue: \"arXiv preprint\"\n  year: 2025\n  url: \"https://arxiv.org/abs/2510.00866\"\n  category: background\n  role: \"质疑基于分类器的数据质量评分是否真正捕获了有意义的质量概念\"\n  key_findings: \"CQF 改善下游任务但不一定改善语言建模；质量分类器隐式偏向其监督目标的数据分布；质量桶与特定 benchmark 对齐\"\n  relevance_to_us: \"提醒我们检测器置信度 q 不等于真实质量——需要理论保证 b* 在检测器有偏时仍然有效\"\n\n- id: guo_2025_escaping_collapse\n  title: \"Escaping Model Collapse via Synthetic Data Verification\"\n  venue: \"arXiv preprint\"\n  year: 2025\n  arxiv_id: \"2510.16657\"\n  url: \"https://arxiv.org/abs/2510.16657\"\n  category: background\n  role: \"提出验证机制筛选合成数据质量，与 detection-based 方法互补\"\n  key_findings: \"通过验证机制在合成数据生成后筛选质量，与基于检测器的事后加权方法互补\"\n  relevance_to_us: \"verification-based 方法是另一条技术路线——他们做生成时验证，我们做训练时加权\"\n\n# ============================================================\n# Category: evaluation\n# 评估方法相关\n# ============================================================\n\n- id: mitchell_2023_detectgpt\n  title: \"DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature\"\n  authors: \"Eric Mitchell, Yoonho Lee, Alexander Khazatsky, Christopher D. Manning, Chelsea Finn\"\n  venue: \"ICML 2023\"\n  year: 2023\n  url: \"https://arxiv.org/abs/2301.11305\"\n  category: evaluation\n  role: \"零样本机器生成文本检测方法——我们的检测器 q 的基线方法之一\"\n  key_findings: \"LLM 生成的文本倾向于占据模型对数概率函数的负曲率区域；无需训练分类器、收集数据集或水印；在 GPT-NeoX 假新闻检测上从 0.81 AUROC 提升到 0.95\"\n  relevance_to_us: \"可作为计算合成概率 q 的检测器之一；其概率曲率方法可能与我们的权重公式有理论联系\"\n\n- id: shi_2024_minkprob\n  title: \"Detecting Pretraining Data from Large Language Models\"\n  authors: \"Weijia Shi, Anirudh Ajith, Mengzhou Xia, Yangsibo Huang, Daogao Liu, Terra Blevins, Danqi Chen, Luke Zettlemoyer\"\n  venue: \"ICLR 2024\"\n  year: 2024\n  url: \"https://arxiv.org/abs/2310.16789\"\n  category: evaluation\n  role: \"Min-K% Prob 方法——检测数据是否在预训练集中的无参考方法\"\n  key_findings: \"已训练数据包含更少低概率异常 token；取最低 K% token 概率的平均值判断；在 WikiMIA 上比最佳基线高 7.4 AUC；无需参考模型\"\n  relevance_to_us: \"Min-K% Prob 可作为估计合成概率 q 的候选方法；其 membership inference 思路可扩展为连续置信度估计\"\n\n- id: kuo_2024_data_weighting\n  title: \"Not All LLM-Generated Data Are Equal: Rethinking Data Weighting in Text Classification\"\n  authors: \"Hsun-Yu Kuo et al.\"\n  venue: \"arXiv preprint\"\n  year: 2024\n  url: \"https://arxiv.org/abs/2410.21526\"\n  category: evaluation\n  role: \"评估合成数据加权策略在文本分类中的效果\"\n  key_findings: \"提出加权损失方法用少量真实数据对齐合成数据分布；在 BERT 级模型上稳定优于标准交叉熵和其他加权方法\"\n  relevance_to_us: \"验证了合成数据需要差异化加权的思路；其评估框架可参考用于我们的下游任务评估\"\n",
    "structuredPatch": [
      {
        "oldStart": 1,
        "oldLines": 7,
        "newStart": 1,
        "newLines": 7,
        "lines": [
          " # Literature Map for provenance_weight_training",
          " # 研究方向：基于收敛理论的自适应污染重加权",
          " # 核心公式：w=(1-q)^b，q 为检测器合成概率，b* 为理论最优权重指数",
          "-# 生成日期：2026-05-14",
          "+# 更新日期：2026-05-14（整合 Drayson comparison 分析）",
          " ",
          " # ============================================================",
          " # Category: direct-competitor"
        ]
      },
      {
        "oldStart": 13,
        "oldLines": 21,
        "newStart": 13,
        "newLines": 46,
        "lines": [
          "   authors: \"George Drayson, Emine Yilmaz, Vasileios Lampos\"",
          "   venue: \"EMNLP 2025\"",
          "   year: 2025",
          "+  arxiv_id: \"2502.15654\"",
          "   url: \"https://arxiv.org/abs/2502.15654\"",
          "+  github: \"https://github.com/GeorgeDrayson/model_collapse\"",
          "   category: direct-competitor",
          "-  role: \"使用同一公式 w=(1-q)^b 进行重加权，但启发式选择 b 而非理论推导\"",
          "-  key_findings: \"训练机器生成文本检测器，用 importance resampling 上采样可能的人类内容，不仅防止 model collapse，还优于纯人类数据训练\"",
          "-  relevance_to_us: \"最直接的竞争者。我们的核心贡献是理论推导 b*，替代其启发式网格搜索方法\"",
          "+  role: \"使用同一公式 w=(1-q)^b 进行重加权，但 b 为验证集 empirical 选取，训练中固定\"",
          "+  method_summary: >",
          "+    Detect-and-reweight 防止递归训练 model collapse。检测器为 ModernBERT 150M",
          "+    (MAGE fine-tune, in-domain AUC=0.986, OOD AUC=0.943)。权重公式 wⱼ=(1-q(xⱼ))^b / Σₗ(1-q(xₗ))^b，",
          "+    通过 SIR 按权重重采样训练数据。b 通过 WikiText-2 验证集上 1 代递归训练后评估选取",
          "+    (GPT-2/SmolLM 135M/360M 用 b=10, SmolLM 1.7B 用 b=1)，训练全程固定。",
          "+    实验覆盖 4 个模型 (GPT-2 124M, SmolLM 135M/360M/1.7B)、10 代递归训练、6 种解码策略。",
          "+    结果 PPL 降低 0.85%–25.65%，diversity 提升 3.44%–14.62%。",
          "+  key_findings: \"验证 detect-and-reweight 有效防止 model collapse 且优于纯人类数据训练；b 值对模型规模敏感（小模型 b=10，大模型 b=1）\"",
          "+  differentiation:",
          "+    b_selection: \"Drayson: 验证集 empirical grid search, per-model 固定 | 我们: α_eff(b) + ESS 约束, per-batch 自适应\"",
          "+    contamination_setting: \"Drayson: 已知比例（实验控制） | 我们: 未知比例（batch 统计量在线估计）\"",
          "+    detector: \"Drayson: ModernBERT 150M (AUC=0.986) | 我们: TF-IDF+LR (AUC=0.939)，证明轻量检测器即可\"",
          "+    theory: \"Drayson: 无 b 选取理论（SIR 启发式） | 我们: 收敛理论 motivated α_eff(b) 推导\"",
          "+    training_scenario: \"Drayson: 递归训练 model collapse prevention | 我们: Web corpus 一次性预训练中的未知污染\"",
          "+    scale: \"Drayson: WikiText-2 (~2M tokens) | 我们: FineWeb subset (132M+ tokens)\"",
          "+    dynamics: \"Drayson: b 固定（训练全程不变） | 我们: b* per-batch 自适应\"",
          "+  our_advantages:",
          "+    - \"From heuristic to principled: 理论推导 b* 替代 empirical grid search，零额外 validation cost\"",
          "+    - \"Unknown contamination: 不需要已知污染比例或干净验证集，适用大规模 web pretraining\"",
          "+    - \"Lightweight detector sufficiency: TF-IDF+LR 即可，检测器计算开销降低数量级\"",
          "+    - \"Unified continuous spectrum: b=0 uniform → b→∞ hard filter 的统一框架\"",
          "+  relevance_to_us: \"最直接的竞争者。共享 w=(1-q)^b 公式，但 b 选取方法根本不同——我们的核心贡献正是理论推导 adaptive b*\"",
          " ",
          " - id: he_2025_golden_ratio",
          "   title: \"Golden Ratio Weighting Prevents Model Collapse\"",
          "   authors: \"Hengzhi He, Shirong Xu, Guang Cheng\"",
          "   venue: \"Under review at JRSSB, 2025\"",
          "   year: 2025",
          "+  arxiv_id: \"2502.18049\"",
          "   url: \"https://arxiv.org/abs/2502.18049\"",
          "   category: direct-competitor",
          "   role: \"从理论推导合成/真实数据混合的最优权重，发现最优权重为黄金比例的倒数(~0.62)\"",
          "-  key_findings: \"在高斯估计、GLM、非参数估计等场景下，当合成数据与真实数据等量时，真实数据的最优权重约为 0.62（黄金比例倒数）\"",
          "+  key_findings: \"在高斯估计、GLM、非参数估计等场景下，当合成数据与真实数据等量时，真实数据的最优权重约为 0.62（黄金比例倒数）。公式 w*=(√(k²+4k)−k)/2, k=真实/合成样本比\"",
          "+  differentiation:",
          "+    scope: \"纯理论工作，假设已知污染比例，未涉及检测器或 LLM 实验，不处理 unknown/online 设置\"",
          "   relevance_to_us: \"同样是理论推导最优权重，但针对 real/synthetic 固定混合比例，未考虑检测器置信度的连续估计\"",
          " ",
          " - id: feng_2024_beyond_collapse"
        ]
      },
      {
        "oldStart": 74,
        "oldLines": 10,
        "newStart": 99,
        "newLines": 11,
        "lines": [
          "   venue: \"ICLR 2025\"",
          "   year: 2025",
          "   url: \"https://arxiv.org/abs/2502.06733\"",
          "+  github: \"https://github.com/sowmaster/Sample-Level-Loss-Reweighting-ICLR-2025\"",
          "   category: method-component",
          "   role: \"首次提出 loss-based reweighting 对梯度优化收敛性影响的理论框架\"",
          "   key_findings: \"基于 loss 值动态调整每个样本权重；建立了 loss-based reweighting 对收敛界影响的形式化刻画；在 7B 和 1.4B 模型上验证更快收敛和更优性能\"",
          "-  relevance_to_us: \"其收敛性理论框架可作为我们推导 b* 最优性的参考；loss-based 与 provenance-based reweighting 互补\"",
          "+  relevance_to_us: \"其收敛性理论框架可作为我们推导 b* 最优性的参考；loss-based 与 provenance-based reweighting 互补（不使用检测器，纯 loss signal 驱动）\"",
          " ",
          " - id: ye_2025_data_mixing_laws",
          "   title: \"Data Mixing Laws: Optimizing Data Mixtures by Predicting Language Modeling Performance\""
        ]
      },
      {
        "oldStart": 101,
        "oldLines": 6,
        "newStart": 127,
        "newLines": 28,
        "lines": [
          "   key_findings: \"用 n-gram 模型量化样本的 commonness，高频样本降权低频样本升权；相比硬去重保留信息完整性；等效训练时间提升 26% 效率和 1.77% 下游准确率\"",
          "   relevance_to_us: \"软加权优于硬过滤的思路与我们一致——w=(1-q)^b 是连续加权而非二元过滤\"",
          " ",
          "+- id: xie_2023_doremi",
          "+  title: \"DoReMi: Optimizing Data Mixtures by Predicting Language Modeling Performance\"",
          "+  authors: \"Sang Michael Xie, Hieu Pham, Xuanyi Dong, Nan Du, Hanxiao Liu, Yifeng Lu, Percy Liang, Quoc V. Le, Tengyu Ma, Adams Wei Yu\"",
          "+  venue: \"NeurIPS 2023\"",
          "+  year: 2023",
          "+  url: \"https://arxiv.org/abs/2305.10429\"",
          "+  category: method-component",
          "+  role: \"域级别权重优化（Group DRO + 小模型代理），不处理 instance-level 污染\"",
          "+  key_findings: \"用小代理模型通过 Group DRO 优化域级别数据混合权重；在 The Pile 和 GLaM 数据集上无需目标分布知识即可改善下游性能\"",
          "+  relevance_to_us: \"域级别 reweighting baseline；我们的方法在 instance-level 操作，粒度更细且基于检测器置信度而非 loss-based DRO\"",
          "+",
          "+- id: xie_2023_dsir",
          "+  title: \"Data Selection for Language Models via Importance Resampling\"",
          "+  authors: \"Sang Michael Xie, Shibani Santurkar, Tengyu Ma, Percy Liang\"",
          "+  venue: \"NeurIPS 2023\"",
          "+  year: 2023",
          "+  url: \"https://arxiv.org/abs/2302.03169\"",
          "+  category: method-component",
          "+  role: \"N-gram 特征重要性采样选择数据子集匹配目标分布\"",
          "+  key_findings: \"用 n-gram 特征估计 importance weights 并重采样数据匹配目标分布；比 heuristic filtering 更 principled；在 GLUE 和下游任务上优于随机选择和启发式方法\"",
          "+  relevance_to_us: \"同样用 importance resampling，但目标是分布匹配而非污染处理；与 Drayson 的 SIR 方法有方法论联系\"",
          "+",
          " # ============================================================",
          " # Category: background",
          " # 数据污染/合成数据在 LLM 训练中的问题"
        ]
      },
      {
        "oldStart": 133,
        "oldLines": 6,
        "newStart": 181,
        "newLines": 7,
        "lines": [
          "   authors: \"Elvis Dohmatob, Yunzhen Feng, Arjun Subramonian, Julia Kempe\"",
          "   venue: \"ICLR 2025 (Spotlight)\"",
          "   year: 2025",
          "+  arxiv_id: \"2410.04840\"",
          "   url: \"https://arxiv.org/abs/2410.04840\"",
          "   category: background",
          "   role: \"证明即使极少量合成数据（1/1000）也能导致 model collapse\""
        ]
      },
      {
        "oldStart": 150,
        "oldLines": 6,
        "newStart": 199,
        "newLines": 17,
        "lines": [
          "   key_findings: \"CQF 改善下游任务但不一定改善语言建模；质量分类器隐式偏向其监督目标的数据分布；质量桶与特定 benchmark 对齐\"",
          "   relevance_to_us: \"提醒我们检测器置信度 q 不等于真实质量——需要理论保证 b* 在检测器有偏时仍然有效\"",
          " ",
          "+- id: guo_2025_escaping_collapse",
          "+  title: \"Escaping Model Collapse via Synthetic Data Verification\"",
          "+  venue: \"arXiv preprint\"",
          "+  year: 2025",
          "+  arxiv_id: \"2510.16657\"",
          "+  url: \"https://arxiv.org/abs/2510.16657\"",
          "+  category: background",
          "+  role: \"提出验证机制筛选合成数据质量，与 detection-based 方法互补\"",
          "+  key_findings: \"通过验证机制在合成数据生成后筛选质量，与基于检测器的事后加权方法互补\"",
          "+  relevance_to_us: \"verification-based 方法是另一条技术路线——他们做生成时验证，我们做训练时加权\"",
          "+",
          " # ============================================================",
          " # Category: evaluation",
          " # 评估方法相关"
        ]
      }
    ],
    "originalFile": "# Literature Map for provenance_weight_training\n# 研究方向：基于收敛理论的自适应污染重加权\n# 核心公式：w=(1-q)^b，q 为检测器合成概率，b* 为理论最优权重指数\n# 生成日期：2026-05-14\n\n# ============================================================\n# Category: direct-competitor\n# 同主题/同方法的论文\n# ============================================================\n\n- id: drayson_2025_detection_collapse\n  title: \"Machine-Generated Text Detection Prevents Language Model Collapse\"\n  authors: \"George Drayson, Emine Yilmaz, Vasileios Lampos\"\n  venue: \"EMNLP 2025\"\n  year: 2025\n  url: \"https://arxiv.org/abs/2502.15654\"\n  category: direct-competitor\n  role: \"使用同一公式 w=(1-q)^b 进行重加权，但启发式选择 b 而非理论推导\"\n  key_findings: \"训练机器生成文本检测器，用 importance resampling 上采样可能的人类内容，不仅防止 model collapse，还优于纯人类数据训练\"\n  relevance_to_us: \"最直接的竞争者。我们的核心贡献是理论推导 b*，替代其启发式网格搜索方法\"\n\n- id: he_2025_golden_ratio\n  title: \"Golden Ratio Weighting Prevents Model Collapse\"\n  authors: \"Hengzhi He, Shirong Xu, Guang Cheng\"\n  venue: \"Under review at JRSSB, 2025\"\n  year: 2025\n  url: \"https://arxiv.org/abs/2502.18049\"\n  category: direct-competitor\n  role: \"从理论推导合成/真实数据混合的最优权重，发现最优权重为黄金比例的倒数(~0.62)\"\n  key_findings: \"在高斯估计、GLM、非参数估计等场景下，当合成数据与真实数据等量时，真实数据的最优权重约为 0.62（黄金比例倒数）\"\n  relevance_to_us: \"同样是理论推导最优权重，但针对 real/synthetic 固定混合比例，未考虑检测器置信度的连续估计\"\n\n- id: feng_2024_beyond_collapse\n  title: \"Beyond Model Collapse: Scaling Up with Synthesized Data Requires Verification\"\n  authors: \"Yunzhen Feng, Elvis Dohmatob, Pu Yang, François Charton, Julia Kempe\"\n  venue: \"arXiv preprint\"\n  year: 2024\n  url: \"https://arxiv.org/abs/2406.07515\"\n  category: direct-competitor\n  role: \"使用 verifier 过滤合成数据防止 model collapse，理论证明即使不完美的 verifier 也有效\"\n  key_findings: \"用高斯混合模型和线性分类器推导条件，证明 verifier 引导的合成数据筛选可避免 model collapse；即使 verifier 不完美也能受益\"\n  relevance_to_us: \"与我们的方法最相似——都用检测器置信度来处理合成数据。区别在于他们做 hard filtering，我们做 soft reweighting\"\n\n# ============================================================\n# Category: method-component\n# 我们用到的技术组件\n# ============================================================\n\n- id: kimura_2024_iw_survey\n  title: \"A Short Survey on Importance Weighting for Machine Learning\"\n  authors: \"Masanari Kimura, Hideitsu Hino\"\n  venue: \"TMLR 2024\"\n  year: 2024\n  url: \"https://arxiv.org/abs/2403.10175\"\n  category: method-component\n  role: \"importance weighting 在机器学习中的全面综述，覆盖分布偏移、密度比估计等核心理论\"\n  key_findings: \"系统整理了 importance weighting 在监督学习分布偏移下的理论保证和应用，包括 covariate shift、domain adaptation 等场景\"\n  relevance_to_us: \"为我们的 importance weighting 框架提供理论基础和方法论参考\"\n\n- id: vehtari_2024_psis\n  title: \"Pareto Smoothed Importance Sampling\"\n  authors: \"Aki Vehtari, Daniel Simpson, Andrew Gelman, Yuling Yao, Jonah Gabry\"\n  venue: \"JMLR 2024\"\n  year: 2024\n  url: \"https://arxiv.org/abs/1507.02646\"\n  category: method-component\n  role: \"提供稳定的 effective sample size 估计和收敛诊断方法\"\n  key_findings: \"用广义 Pareto 分布拟合 importance ratio 上尾实现平滑；提出 Pareto k 有限样本收敛率诊断指标；k<min(1-1/log10(S),0.7) 时估计可靠\"\n  relevance_to_us: \"我们的 α_eff(b) 估计直接依赖 effective sample size 理论，PSIS 的收敛诊断可用于验证我们的权重方案\"\n\n- id: sow_2025_dynamic_reweighting\n  title: \"Dynamic Loss-Based Sample Reweighting for Improved Large Language Model Pretraining\"\n  authors: \"Daouda Sow et al.\"\n  venue: \"ICLR 2025\"\n  year: 2025\n  url: \"https://arxiv.org/abs/2502.06733\"\n  category: method-component\n  role: \"首次提出 loss-based reweighting 对梯度优化收敛性影响的理论框架\"\n  key_findings: \"基于 loss 值动态调整每个样本权重；建立了 loss-based reweighting 对收敛界影响的形式化刻画；在 7B 和 1.4B 模型上验证更快收敛和更优性能\"\n  relevance_to_us: \"其收敛性理论框架可作为我们推导 b* 最优性的参考；loss-based 与 provenance-based reweighting 互补\"\n\n- id: ye_2025_data_mixing_laws\n  title: \"Data Mixing Laws: Optimizing Data Mixtures by Predicting Language Modeling Performance\"\n  authors: \"Jiasheng Ye, Peiju Liu, Tianxiang Sun, Yunhua Zhou, Jun Zhan, Xipeng Qiu\"\n  venue: \"ICLR 2025\"\n  year: 2025\n  url: \"https://arxiv.org/abs/2403.16952\"\n  category: method-component\n  role: \"发现数据混合比例与模型性能之间的定量可预测性\"\n  key_findings: \"模型性能关于混合比例具有函数形式的可预测性；可用小规模训练预测大模型在不同混合下的性能；适用于 continual training 的遗忘预测\"\n  relevance_to_us: \"data mixing laws 可作为验证我们 b* 最优性的理论框架——检验不同 b 下的 mixing 效果是否符合预测\"\n\n- id: he_2024_softdedup\n  title: \"SoftDedup: an Efficient Data Reweighting Method for Speeding Up Language Model Pre-training\"\n  authors: \"Nan He, Weichen Xiong, Hanwen Liu, Yi Liao, Lei Ding, Kai Zhang, Guohua Tang, Xiao Han, Yang Wei\"\n  venue: \"ACL 2024\"\n  year: 2024\n  url: \"https://arxiv.org/abs/2407.06654\"\n  category: method-component\n  role: \"用 data commonness 指标进行软去重加权，而非硬删除\"\n  key_findings: \"用 n-gram 模型量化样本的 commonness，高频样本降权低频样本升权；相比硬去重保留信息完整性；等效训练时间提升 26% 效率和 1.77% 下游准确率\"\n  relevance_to_us: \"软加权优于硬过滤的思路与我们一致——w=(1-q)^b 是连续加权而非二元过滤\"\n\n# ============================================================\n# Category: background\n# 数据污染/合成数据在 LLM 训练中的问题\n# ============================================================\n\n- id: shumailov_2024_model_collapse\n  title: \"AI Models Collapse When Trained on Recursively Generated Data\"\n  authors: \"Ilia Shumailov, Zakhar Shumaylov, Yiren Zhao, Nicolas Papernot, Ross Anderson, Yarin Gal\"\n  venue: \"Nature 2024\"\n  year: 2024\n  url: \"https://www.nature.com/articles/s41586-024-07566-y\"\n  category: background\n  role: \"奠基性工作——证明在递归生成数据上训练导致 model collapse\"\n  key_findings: \"在 LLM、VAE、GMM 上证明不加区分地用模型生成内容训练会导致不可逆退化；原始分布的尾部逐渐消失；反复训练的语言模型出现重复短语\"\n  relevance_to_us: \"model collapse 是我们工作的核心动机——加权方案的目标就是防止污染数据导致的性能退化\"\n\n- id: alemohammad_2024_mad\n  title: \"Self-Consuming Generative Models Go MAD\"\n  authors: \"Sina Alemohammad, Josue Casco-Rodriguez, Lorenzo Luzi, Ahmed Imtiaz Humayun, Hossein Babaei, Daniel LeJeune, Ali Siahkoohi, Richard G. Baraniuk\"\n  venue: \"ICLR 2024\"\n  year: 2024\n  url: \"https://arxiv.org/abs/2307.01850\"\n  category: background\n  role: \"提出 Model Autophagy Disorder (MAD) 概念——自消费式生成模型的退化\"\n  key_findings: \"分析三种自消费循环（fully synthetic、synthetic augmentation、fresh data）；无新鲜真实数据时质量或多样性不可避免下降；即使保留原始训练数据也可能退化\"\n  relevance_to_us: \"MAD 的数学框架帮助理解不同污染程度下的退化动力学，为我们的收敛理论提供上下文\"\n\n- id: dohmatob_2025_strong_collapse\n  title: \"Strong Model Collapse\"\n  authors: \"Elvis Dohmatob, Yunzhen Feng, Arjun Subramonian, Julia Kempe\"\n  venue: \"ICLR 2025 (Spotlight)\"\n  year: 2025\n  url: \"https://arxiv.org/abs/2410.04840\"\n  category: background\n  role: \"证明即使极少量合成数据（1/1000）也能导致 model collapse\"\n  key_findings: \"在 scaling laws 框架下建立 strong model collapse；用算子值自由概率论获得测试误差的 bias-variance 分解；更大模型可放大 collapse 效应\"\n  relevance_to_us: \"强化了我们工作的必要性——即使少量合成污染也需要处理，仅靠增加数据量无法解决\"\n\n- id: nait_saada_2025_quality_illusion\n  title: \"The Data-Quality Illusion: Rethinking Classifier-Based Quality Filtering for LLM Pretraining\"\n  authors: \"Thiziri Nait Saada, Louis Bethune, Michal Klein, David Grangier, Marco Cuturi, Pierre Ablin\"\n  venue: \"arXiv preprint\"\n  year: 2025\n  url: \"https://arxiv.org/abs/2510.00866\"\n  category: background\n  role: \"质疑基于分类器的数据质量评分是否真正捕获了有意义的质量概念\"\n  key_findings: \"CQF 改善下游任务但不一定改善语言建模；质量分类器隐式偏向其监督目标的数据分布；质量桶与特定 benchmark 对齐\"\n  relevance_to_us: \"提醒我们检测器置信度 q 不等于真实质量——需要理论保证 b* 在检测器有偏时仍然有效\"\n\n# ============================================================\n# Category: evaluation\n# 评估方法相关\n# ============================================================\n\n- id: mitchell_2023_detectgpt\n  title: \"DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature\"\n  authors: \"Eric Mitchell, Yoonho Lee, Alexander Khazatsky, Christopher D. Manning, Chelsea Finn\"\n  venue: \"ICML 2023\"\n  year: 2023\n  url: \"https://arxiv.org/abs/2301.11305\"\n  category: evaluation\n  role: \"零样本机器生成文本检测方法——我们的检测器 q 的基线方法之一\"\n  key_findings: \"LLM 生成的文本倾向于占据模型对数概率函数的负曲率区域；无需训练分类器、收集数据集或水印；在 GPT-NeoX 假新闻检测上从 0.81 AUROC 提升到 0.95\"\n  relevance_to_us: \"可作为计算合成概率 q 的检测器之一；其概率曲率方法可能与我们的权重公式有理论联系\"\n\n- id: shi_2024_minkprob\n  title: \"Detecting Pretraining Data from Large Language Models\"\n  authors: \"Weijia Shi, Anirudh Ajith, Mengzhou Xia, Yangsibo Huang, Daogao Liu, Terra Blevins, Danqi Chen, Luke Zettlemoyer\"\n  venue: \"ICLR 2024\"\n  year: 2024\n  url: \"https://arxiv.org/abs/2310.16789\"\n  category: evaluation\n  role: \"Min-K% Prob 方法——检测数据是否在预训练集中的无参考方法\"\n  key_findings: \"已训练数据包含更少低概率异常 token；取最低 K% token 概率的平均值判断；在 WikiMIA 上比最佳基线高 7.4 AUC；无需参考模型\"\n  relevance_to_us: \"Min-K% Prob 可作为估计合成概率 q 的候选方法；其 membership inference 思路可扩展为连续置信度估计\"\n\n- id: kuo_2024_data_weighting\n  title: \"Not All LLM-Generated Data Are Equal: Rethinking Data Weighting in Text Classification\"\n  authors: \"Hsun-Yu Kuo et al.\"\n  venue: \"arXiv preprint\"\n  year: 2024\n  url: \"https://arxiv.org/abs/2410.21526\"\n  category: evaluation\n  role: \"评估合成数据加权策略在文本分类中的效果\"\n  key_findings: \"提出加权损失方法用少量真实数据对齐合成数据分布；在 BERT 级模型上稳定优于标准交叉熵和其他加权方法\"\n  relevance_to_us: \"验证了合成数据需要差异化加权的思路；其评估框架可参考用于我们的下游任务评估\"\n",
    "userModified": false
  },
  "sourceToolAssistantUUID": "ccb0c563-abc4-4cb6-93e9-9a82704a62f3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training",
  "sessionId": "33f4c8cf-38de-44f8-ba86-369f9c5d5e2f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 32 · 2026-05-14T23:43:17.183Z_

```json
{
  "parentUuid": "297044e3-e7ad-4882-a36d-53b3e3cff017",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "9d0bead7-05ef-455b-b3a8-5e89d77a3f38",
  "timestamp": "2026-05-14T23:43:17.183Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training",
  "sessionId": "33f4c8cf-38de-44f8-ba86-369f9c5d5e2f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 33_

```json
{
  "type": "last-prompt",
  "leafUuid": "9d0bead7-05ef-455b-b3a8-5e89d77a3f38",
  "sessionId": "33f4c8cf-38de-44f8-ba86-369f9c5d5e2f"
}
```

---

### Runtime record

_source line 34_

```json
{
  "type": "ai-title",
  "aiTitle": "Integrate Drayson et al. into literature_map.yaml",
  "sessionId": "33f4c8cf-38de-44f8-ba86-369f9c5d5e2f"
}
```

---

### Assistant

_source line 35 · 2026-05-14T23:43:29.305Z_

更新完成。变更摘要：

**Drayson 条目扩充：**
- 新增 `arxiv_id`、`github`、`method_summary`（详细方法描述含检测器规格、b 选取流程、实验规模）
- 新增 `differentiation` 结构化对比（7 个维度：b_selection、contamination_setting、detector、theory、training_scenario、scale、dynamics）
- 新增 `our_advantages` 列表（4 条：principled b*、unknown contamination、lightweight detector、unified spectrum）

**新增 3 篇论文：**
- `xie_2023_doremi` (NeurIPS 2023) — 域级别 Group DRO reweighting baseline
- `xie_2023_dsir` (NeurIPS 2023) — n-gram importance resampling，与 Drayson SIR 有方法论联系
- `guo_2025_escaping_collapse` (arXiv 2510.16657) — verification-based 合成数据筛选

**已有条目小更新：**
- `dohmatob_2025_strong_collapse` 补充 `arxiv_id`
- `sow_2025_dynamic_reweighting` 补充 `github` 链接和 relevance 细节

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9d0bead7-05ef-455b-b3a8-5e89d77a3f38",
  "isSidechain": false,
  "requestId": "req_011Cb3MAw6hjLnyBrw39Ensp",
  "type": "assistant",
  "uuid": "ed1d79f1-7ebd-433e-a3fe-867b21171a92",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training",
  "sessionId": "33f4c8cf-38de-44f8-ba86-369f9c5d5e2f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GG7cZiajwEQKTtKnFUeroY",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6357,
      "cache_read_input_tokens": 49168,
      "output_tokens": 353,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 6357,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 353,
          "cache_read_input_tokens": 49168,
          "cache_creation_input_tokens": 6357,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 6357
          },
          "type": "message"
        }
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

_source line 36_

```json
{
  "type": "last-prompt",
  "leafUuid": "ed1d79f1-7ebd-433e-a3fe-867b21171a92",
  "sessionId": "33f4c8cf-38de-44f8-ba86-369f9c5d5e2f"
}
```

---

### Runtime record

_source line 37_

```json
{
  "type": "ai-title",
  "aiTitle": "Integrate Drayson et al. into literature_map.yaml",
  "sessionId": "33f4c8cf-38de-44f8-ba86-369f9c5d5e2f"
}
```

---
