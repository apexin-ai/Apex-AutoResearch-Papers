# Research conversation: <project_context> # 项目: gen-depth-fingerprint ## 运行环境 - 服务器名: bjb2-18868 - SSH 连接命令: ssh connect.bjb2.seetacloud.com # 必

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 33
- **Recorded user turns:** 1
- **Tool calls:** 5
- **Original source:** `logs/chats/exported-trajectories/account-1/1d18d25d-25e1-4c57-94d9-a15ab4822c5c.jsonl`
- **Structured JSON:** [`08b56efcaf41b6cbf6c2.json`](../../sessions/08/08b56efcaf41b6cbf6c2.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-20T05:01:04.582Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-20T05:01:04.582Z",
  "sessionId": "1d18d25d-25e1-4c57-94d9-a15ab4822c5c",
  "content": "&lt;project_context>\n# 项目: gen-depth-fingerprint\n\n## 运行环境\n- 服务器名: bjb2-18868\n- SSH 连接命令: ssh connect.bjb2.seetacloud.com  # 必须用此命令，~/.ssh/config 自动应用密钥和跳板机，禁止用裸 IP\n- 项目代码根目录: /root/gen-depth-fingerprint\n\n## ⚠️ 活跃约束（必须遵守）\n\n- **C001**: 每次跑实验前确认当前可用的GPU卡数量（原因：用户(陈卓凡)要求添加的研究规则，防止在GPU不可用时启动实验）\n\n\n## 环境搭建\n连接服务器后先调 `detect_image` 检测是否为预置镜像。如果匹配，跳过基础环境搭建，只装项目特有依赖。已预装的包不要重复安装。\n\n## 输出风格\n回复简洁直接。只输出执行结果和必要信息，不要解释过程、不要客套、不要给未被要求的建议。\n&lt;/project_context>\n## 任务：实验数据利用审计\n\n### 目标\n检查 registry 中所有 conclusion=success 的实验，列出哪些实验的数据**未被论文正文或 appendix 引用**。\n\n### 步骤\n\n1. 用 `read_registry(project=\"gen-depth-fingerprint\")` 获取所有实验，筛选 conclusion=success 的实验（预计约 42 个）。\n\n2. 读取论文所有 tex 文件，搜索每个 exp_id 或其关键指标/实验名是否被引用。论文路径：\n   `/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/`\n   \n   关键 tex 文件：\n   - results.tex, introduction.tex, abstract.tex, conclusion.tex, discussion.tex\n   - appendix_*.tex（所有 appendix 文件）\n   - table*.tex（所有表格文件）\n\n   搜索方式：不仅搜 exp_id 字符串，也搜实验的关键数字（如特征性的 F1 值）、实验描述关键词（如 \"cross-model\"、\"temperature\"、\"prompt type\" 等）。\n\n3. 对每个未引用的成功实验，评估：\n   - 实验内容是什么（看 hypothesis 和 metrics）\n   - 能否补一个 appendix table/figure 增强论文\n   - 建议补充方式（新 appendix table、现有 appendix 扩展、或确认不需要引用的理由）\n\n4. 输出格式：\n```\n| exp_id | 实验名 | 当前引用状态 | 建议补充方式 |\n```\n\n### 注意\n- \"引用\"不要求出现 exp_id 字符串，实验结果的数字或描述出现在论文中即算引用\n- 一些实验是数据生成步骤（如 plan-002-* shard 生成），它们的数据被下游评估实验使用，算间接引用\n- 重点关注有独立分析价值但未被引用的实验"
}
````

---

### Runtime record

_source line 2 · 2026-05-20T05:01:04.585Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-20T05:01:04.585Z",
  "sessionId": "1d18d25d-25e1-4c57-94d9-a15ab4822c5c"
}
```

---

## Round 1

31 recorded events

### User

_source line 3 · 2026-05-20T05:01:04.614Z_

&lt;project_context>
# 项目: gen-depth-fingerprint

## 运行环境
- 服务器名: bjb2-18868
- SSH 连接命令: ssh connect.bjb2.seetacloud.com  # 必须用此命令，~/.ssh/config 自动应用密钥和跳板机，禁止用裸 IP
- 项目代码根目录: /root/gen-depth-fingerprint

## ⚠️ 活跃约束（必须遵守）

- **C001**: 每次跑实验前确认当前可用的GPU卡数量（原因：用户(陈卓凡)要求添加的研究规则，防止在GPU不可用时启动实验）


## 环境搭建
连接服务器后先调 `detect_image` 检测是否为预置镜像。如果匹配，跳过基础环境搭建，只装项目特有依赖。已预装的包不要重复安装。

## 输出风格
回复简洁直接。只输出执行结果和必要信息，不要解释过程、不要客套、不要给未被要求的建议。
&lt;/project_context>
## 任务：实验数据利用审计

### 目标
检查 registry 中所有 conclusion=success 的实验，列出哪些实验的数据**未被论文正文或 appendix 引用**。

### 步骤

1. 用 `read_registry(project="gen-depth-fingerprint")` 获取所有实验，筛选 conclusion=success 的实验（预计约 42 个）。

2. 读取论文所有 tex 文件，搜索每个 exp_id 或其关键指标/实验名是否被引用。论文路径：
   `/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/`
   
   关键 tex 文件：
   - results.tex, introduction.tex, abstract.tex, conclusion.tex, discussion.tex
   - appendix_*.tex（所有 appendix 文件）
   - table*.tex（所有表格文件）

   搜索方式：不仅搜 exp_id 字符串，也搜实验的关键数字（如特征性的 F1 值）、实验描述关键词（如 "cross-model"、"temperature"、"prompt type" 等）。

3. 对每个未引用的成功实验，评估：
   - 实验内容是什么（看 hypothesis 和 metrics）
   - 能否补一个 appendix table/figure 增强论文
   - 建议补充方式（新 appendix table、现有 appendix 扩展、或确认不需要引用的理由）

4. 输出格式：
```
| exp_id | 实验名 | 当前引用状态 | 建议补充方式 |
```

### 注意
- "引用"不要求出现 exp_id 字符串，实验结果的数字或描述出现在论文中即算引用
- 一些实验是数据生成步骤（如 plan-002-* shard 生成），它们的数据被下游评估实验使用，算间接引用
- 重点关注有独立分析价值但未被引用的实验

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "6504b37e-e710-425c-85a9-649cd3090508",
  "type": "user",
  "uuid": "03e1b0e6-f953-480a-b922-e9f15996e927",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "1d18d25d-25e1-4c57-94d9-a15ab4822c5c",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-20T05:01:04.614Z_

```json
{
  "parentUuid": "03e1b0e6-f953-480a-b922-e9f15996e927",
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
  "uuid": "58b24f87-dc15-4547-80ba-77321a767d79",
  "timestamp": "2026-05-20T05:01:04.614Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "1d18d25d-25e1-4c57-94d9-a15ab4822c5c",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

---

### Runtime record

_source line 5 · 2026-05-20T05:01:04.614Z_

```json
{
  "parentUuid": "58b24f87-dc15-4547-80ba-77321a767d79",
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
  "uuid": "fee717ec-65a5-4fd3-bd4d-39d8859dd579",
  "timestamp": "2026-05-20T05:01:04.614Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "1d18d25d-25e1-4c57-94d9-a15ab4822c5c",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

---

### Runtime record

_source line 6 · 2026-05-20T05:01:04.614Z_

```json
{
  "parentUuid": "fee717ec-65a5-4fd3-bd4d-39d8859dd579",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "4baf20ea-fc20-4222-9e46-0c5c0cb65637",
  "timestamp": "2026-05-20T05:01:04.614Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "1d18d25d-25e1-4c57-94d9-a15ab4822c5c",
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
  "aiTitle": "Audit unreferenced successful experiments in paper",
  "sessionId": "1d18d25d-25e1-4c57-94d9-a15ab4822c5c"
}
```

---

### Assistant

_source line 8 · 2026-05-20T05:01:07.713Z_

<details><summary>Logged reasoning block</summary>

```text
Let me start by reading the registry to get all experiments, then read the paper tex files to cross-reference.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4baf20ea-fc20-4222-9e46-0c5c0cb65637",
  "isSidechain": false,
  "requestId": "req_011CbDET47oEdSZHXvy1pocw",
  "type": "assistant",
  "uuid": "84d54e38-8a26-4628-89b1-d9bf2f404857",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "1d18d25d-25e1-4c57-94d9-a15ab4822c5c",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VPHEBjoZa1Ws52MKL4PXFx",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13117,
      "cache_read_input_tokens": 11841,
      "output_tokens": 149,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 13117,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 149,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 13117,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 13117
          },
          "type": "message"
        }
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

_source line 9 · 2026-05-20T05:01:08.177Z_

I'll先获取 registry 和论文文件列表，然后交叉比对。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "84d54e38-8a26-4628-89b1-d9bf2f404857",
  "isSidechain": false,
  "requestId": "req_011CbDET47oEdSZHXvy1pocw",
  "type": "assistant",
  "uuid": "3a3d0a18-d690-49d0-ae28-7f7a9b122ee7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "1d18d25d-25e1-4c57-94d9-a15ab4822c5c",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VPHEBjoZa1Ws52MKL4PXFx",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13117,
      "cache_read_input_tokens": 11841,
      "output_tokens": 149,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 13117,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 149,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 13117,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 13117
          },
          "type": "message"
        }
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

_source line 10 · 2026-05-20T05:01:08.828Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01XscBcKs1oHMXM5GEbrVfp3`</summary>

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
  "parentUuid": "3a3d0a18-d690-49d0-ae28-7f7a9b122ee7",
  "isSidechain": false,
  "requestId": "req_011CbDET47oEdSZHXvy1pocw",
  "type": "assistant",
  "uuid": "f7013314-94d5-4d7d-9434-1faa5b1b9a41",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "1d18d25d-25e1-4c57-94d9-a15ab4822c5c",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VPHEBjoZa1Ws52MKL4PXFx",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13117,
      "cache_read_input_tokens": 11841,
      "output_tokens": 149,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 13117,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 149,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 13117,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 13117
          },
          "type": "message"
        }
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

_source line 11 · 2026-05-20T05:01:08.834Z_

<details><summary>↩ Tool result · `toolu_01XscBcKs1oHMXM5GEbrVfp3`</summary>

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
  "parentUuid": "f7013314-94d5-4d7d-9434-1faa5b1b9a41",
  "isSidechain": false,
  "promptId": "6504b37e-e710-425c-85a9-649cd3090508",
  "type": "user",
  "uuid": "ff1d3ea8-bf61-4d95-af8d-7a553a8923ef",
  "toolUseResult": {
    "matches": [
      "mcp__agent-ml-research__read_registry"
    ],
    "query": "select:mcp__agent-ml-research__read_registry",
    "total_deferred_tools": 25
  },
  "sourceToolAssistantUUID": "f7013314-94d5-4d7d-9434-1faa5b1b9a41",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "1d18d25d-25e1-4c57-94d9-a15ab4822c5c",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-20T05:01:11.562Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_0138QMr6xqk8jS73kiBSRcVE`</summary>

```json
{
  "project": "gen-depth-fingerprint",
  "filters": {
    "conclusion": "success"
  },
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
  "parentUuid": "ff1d3ea8-bf61-4d95-af8d-7a553a8923ef",
  "isSidechain": false,
  "requestId": "req_011CbDETNHwb4DTpgPMzGich",
  "type": "assistant",
  "uuid": "5277fa8f-57e9-4f6f-bc5a-fb56e8b4b07a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "1d18d25d-25e1-4c57-94d9-a15ab4822c5c",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PF1w5x34vkDMWGNgnmu5Gf",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 511,
      "cache_read_input_tokens": 24958,
      "output_tokens": 213,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 511,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 213,
          "cache_read_input_tokens": 24958,
          "cache_creation_input_tokens": 511,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 511
          },
          "type": "message"
        }
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

_source line 13 · 2026-05-20T05:01:12.053Z_

<details><summary>↩ Tool result · `toolu_0138QMr6xqk8jS73kiBSRcVE`</summary>

```text
Error: result (61,189 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-3-projects-gen-depth-fingerprint/1d18d25d-25e1-4c57-94d9-a15ab4822c5c/tool-results/mcp-agent-ml-research-read_registry-1779253272038.txt.
Format: JSON with schema: {result: string}
Use offset and limit parameters to read specific portions of the file, search within it for specific content, and jq to make structured queries.
REQUIREMENTS FOR SUMMARIZATION/ANALYSIS/REVIEW:
- You MUST read the content from the file at /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-3-projects-gen-depth-fingerprint/1d18d25d-25e1-4c57-94d9-a15ab4822c5c/tool-results/mcp-agent-ml-research-read_registry-1779253272038.txt in sequential chunks until 100% of the content has been read.
- If you receive truncation warnings when reading the file, reduce the chunk size until you have read 100% of the content without truncation.
- Before producing ANY summary or analysis, you MUST explicitly describe what portion of the content you have read. ***If you did not read the entire content, you MUST explicitly state this.***

```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5277fa8f-57e9-4f6f-bc5a-fb56e8b4b07a",
  "isSidechain": false,
  "promptId": "6504b37e-e710-425c-85a9-649cd3090508",
  "type": "user",
  "uuid": "e4ef5f99-1ef2-41fc-9113-b0c7ebaf4131",
  "toolUseResult": "Error: result (61,189 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-3-projects-gen-depth-fingerprint/1d18d25d-25e1-4c57-94d9-a15ab4822c5c/tool-results/mcp-agent-ml-research-read_registry-1779253272038.txt.\nFormat: JSON with schema: {result: string}\nUse offset and limit parameters to read specific portions of the file, search within it for specific content, and jq to make structured queries.\nREQUIREMENTS FOR SUMMARIZATION/ANALYSIS/REVIEW:\n- You MUST read the content from the file at /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-3-projects-gen-depth-fingerprint/1d18d25d-25e1-4c57-94d9-a15ab4822c5c/tool-results/mcp-agent-ml-research-read_registry-1779253272038.txt in sequential chunks until 100% of the content has been read.\n- If you receive truncation warnings when reading the file, reduce the chunk size until you have read 100% of the content without truncation.\n- Before producing ANY summary or analysis, you MUST explicitly describe what portion of the content you have read. ***If you did not read the entire content, you MUST explicitly state this.***\n",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {\"exp_056b_qlora_qwen_base\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-19T07:53:19.069Z\", \"updated_at\": \"2026-05-19T09:51:15.712Z\", \"hypothesis\": \"Within-model QLoRA on Qwen3-1.7B base data establishes per-model baseline for instruct comparison; expected 3-class F1 comparable to pooled base QLoRA (0.905) with potential variance from smaller per-model dataset\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/bin/activate && python /root/gen-depth-fingerprint/qlora_instruct.py --generator qwen3-1.7b --data_path /root/gen-depth-fingerprint/data/qwen3-1.7b/generations_shard0.jsonl --backbone /root/autodl-tmp/models/qwen3-0.6b/Qwen/Qwen3-0___6B-Base/ --device cuda:0 --output /root/gen-depth-fingerprint/results/qlora_qwen3-1.7b.json 2>&1 | tee /root/gen-depth-fingerprint/results/qlora_qwen_base.log\\\"\", \"server\": \"bjb2-18868\", \"gpu\": [\"cuda:3\"], \"pid\": \"72489\", \"log_path\": \"~/runs/gen-depth-fingerprint/exp_056b_qlora_qwen_base.log\", \"submitted_at\": \"2026-05-19T09:02:41.726Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"conclusion\": \"success\", \"metrics\": {\"macro_f1_3class\": 0.904, \"macro_f1_3class_std\": 0.0094, \"macro_f1_5class\": 0.5544, \"macro_f1_5class_std\": 0.0068, \"binary_f1\": 0.8597, \"binary_f1_std\": 0.0123, \"n_samples\": 2291, \"runtime_seconds\": 880.9, \"note\": \"completed before kill signal\"}}, \"exp_055b_qlora_olmo_base\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-19T07:53:17.806Z\", \"updated_at\": \"2026-05-19T09:51:13.252Z\", \"hypothesis\": \"Within-model QLoRA on OLMo-2-1B base data establishes per-model baseline for instruct comparison; expected 3-class F1 comparable to pooled base QLoRA (0.905) with potential variance from smaller per-model dataset\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/bin/activate && python /root/gen-depth-fingerprint/qlora_instruct.py --generator olmo-2-1b --data_path /root/gen-depth-fingerprint/data/olmo-2-1b/generations_shard0.jsonl --backbone /root/autodl-tmp/models/qwen3-0.6b/Qwen/Qwen3-0___6B-Base/ --device cuda:0 --output /root/gen-depth-fingerprint/results/qlora_olmo-2-1b.json 2>&1 | tee /root/gen-depth-fingerprint/results/qlora_olmo_base.log\\\"\", \"server\": \"bjb2-18868\", \"gpu\": [\"cuda:2\"], \"pid\": \"72272\", \"log_path\": \"~/runs/gen-depth-fingerprint/exp_055b_qlora_olmo_base.log\", \"submitted_at\": \"2026-05-19T09:02:39.461Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"conclusion\": \"success\", \"metrics\": {\"macro_f1_3class\": 0.8588, \"macro_f1_3class_std\": 0.0036, \"macro_f1_5class\": 0.5398, \"macro_f1_5class_std\": 0.015, \"binary_f1\": 0.7925, \"binary_f1_std\": 0.0097, \"n_samples\": 2379, \"runtime_seconds\": 911.7, \"note\": \"completed before kill signal\"}}, \"exp_056_qlora_qwen_instruct\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-19T07:53:15.921Z\", \"updated_at\": \"2026-05-19T09:51:05.773Z\", \"hypothesis\": \"QLoRA end-to-end classifier on Qwen3-1.7B-Instruct generation data recovers depth signal partially: 3-class F1 lower than base QLoRA (0.905) due to instruct-tuning compressing depth features, but higher than XGBoost on instruct features (0.732)\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/bin/activate && python /root/gen-depth-fingerprint/qlora_instruct.py --generator qwen3-1.7b-instruct --data_path /root/gen-depth-fingerprint/data/qwen3-1.7b-instruct/generations_shard0.jsonl --backbone /root/autodl-tmp/models/qwen3-0.6b/Qwen/Qwen3-0___6B-Base/ --device cuda:0 --output /root/gen-depth-fingerprint/results/qlora_qwen3-1.7b-instruct.json 2>&1 | tee /root/gen-depth-fingerprint/results/qlora_qwen_instruct.log\\\"\", \"server\": \"bjb2-18868\", \"gpu\": [\"cuda:1\"], \"pid\": \"72065\", \"log_path\": \"~/runs/gen-depth-fingerprint/exp_056_qlora_qwen_instruct.log\", \"submitted_at\": \"2026-05-19T09:02:37.080Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"conclusion\": \"success\", \"metrics\": {\"macro_f1_3class\": 0.9066, \"macro_f1_3class_std\": 0.0082, \"macro_f1_5class\": 0.5514, \"macro_f1_5class_std\": 0.0031, \"binary_f1\": 0.8672, \"binary_f1_std\": 0.0137, \"n_samples\": 4963, \"runtime_seconds\": 1880.5}}, \"exp_055_qlora_olmo_instruct\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-19T07:53:14.526Z\", \"updated_at\": \"2026-05-19T09:51:03.509Z\", \"hypothesis\": \"QLoRA end-to-end classifier on OLMo-2-0425-1B-Instruct generation data recovers depth signal partially: 3-class F1 lower than base QLoRA (0.905) due to instruct-tuning compressing depth features, but higher than XGBoost on instruct features (0.575)\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/bin/activate && python /root/gen-depth-fingerprint/qlora_instruct.py --generator olmo-2-0425-1b-instruct --data_path /root/gen-depth-fingerprint/data/olmo-2-0425-1b-instruct/generations_shard0.jsonl --backbone /root/autodl-tmp/models/qwen3-0.6b/Qwen/Qwen3-0___6B-Base/ --device cuda:0 --output /root/gen-depth-fingerprint/results/qlora_olmo-2-0425-1b-instruct.json 2>&1 | tee /root/gen-depth-fingerprint/results/qlora_olmo_instruct.log\\\"\", \"server\": \"bjb2-18868\", \"gpu\": [\"cuda:0\"], \"pid\": \"71920\", \"log_path\": \"~/runs/gen-depth-fingerprint/exp_055_qlora_olmo_instruct.log\", \"submitted_at\": \"2026-05-19T09:02:34.465Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"conclusion\": \"success\", \"metrics\": {\"macro_f1_3class\": 0.8881, \"macro_f1_3class_std\": 0.0071, \"macro_f1_5class\": 0.5976, \"macro_f1_5class_std\": 0.0046, \"binary_f1\": 0.8363, \"binary_f1_std\": 0.0096, \"n_samples\": 4429, \"runtime_seconds\": 1689.7}}, \"exp_054_instruct_llama3_2_3b\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-18T03:06:07.150Z\", \"updated_at\": \"2026-05-18T07:58:31.553Z\", \"hypothesis\": \"Instruct-tuned Llama-3.2-3B-Instruct shows degraded depth signal vs base Llama-3.2-3B (F1=0.697), quantifying instruction-tuning's impact on DDR\", \"notes\": \"生成 59% (292/497 seeds) 后 Worker 与服务器断连。脚本有 resume 支持。模型已下载到 /root/autodl-tmp/models/Llama-3.2-3B-Instruct-ms/。Eval 脚本已准备: eval_exp054_instruct_llama.py\", \"conclusion\": \"success\", \"metrics\": {\"instruct_binary_f1\": 0.8381, \"instruct_binary_ci\": [0.828, 0.847], \"instruct_3class_f1\": 0.5437, \"instruct_3class_ci\": [0.53, 0.558], \"base_binary_f1\": 0.8488, \"base_3class_f1\": 0.7424, \"rho_instruct_entropy_mean\": 0.2299, \"rho_instruct_entropy_std\": 0.2623, \"rho_instruct_entropy_min\": -0.0027, \"rho_instruct_entropy_max\": 0.2036, \"rho_instruct_tail_decay\": 0.1198, \"rho_instruct_ttr\": -0.1411, \"rho_instruct_hapax_ratio\": -0.1157, \"rho_base_entropy_mean\": -0.627, \"rho_base_ttr\": -0.6856, \"rho_base_hapax_ratio\": -0.6975, \"direction_reversals\": 3, \"reversed_features\": [\"entropy_mean\", \"entropy_std\", \"tail_decay\"], \"data_count\": 4974}}, \"exp_049_temp_curve_t05\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T22:15:10.383Z\", \"updated_at\": \"2026-05-18T06:09:22.443Z\", \"hypothesis\": \"DDR signal at t=0.5 should be stronger than t=0.7 (less randomness preserves more distributional structure)\", \"spec\": {\"command\": \"python generate_chain.py --model-name pythia-2.8b-t05 --temperature 0.5 --top-p 0.9 --output-dir data/ --device cuda:0\", \"server\": \"autodl-5090\", \"data_path\": \"data/pythia-2.8b-t05\", \"data_count\": 995, \"model_name\": \"pythia-2.8b\", \"seed\": 0, \"note\": \"重跑：修复 top_p=0.9（之前错误使用 top_p=0.8）。串行 3 任务的第 1 个。\", \"checkpoint_path\": \"N/A (generation only)\", \"log_path\": \"/root/gen-depth-fingerprint/logs/tc_fix/\"}, \"failure_reason\": \"startup recovery: RUNNING with no cron and no server/pid info\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-18T02:11:23.228Z\", \"notes\": \"Registry 误标 failed（startup recovery 机制）。实际 tmux tc_fix 仍在运行中。Phase 1 (t=0.5 generation) 已完成 4708 records。等待 phase 2+3 完成后统一提取特征和评估。\", \"metrics\": {\"records\": 4708, \"skipped\": 113, \"seeds\": 995, \"model\": \"pythia-2.8b\", \"temperature\": 0.5, \"top_p\": 0.9, \"within_cv_binary_f1\": 0.8432, \"within_cv_binary_ci\": [0.8301, 0.8558], \"logo_binary_f1\": 0.8136, \"logo_binary_ci\": [0.7984, 0.8282], \"entropy_mean_rho\": -0.5844}}, \"exp_053_instruct_olmo2_1b\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-18T03:06:06.142Z\", \"updated_at\": \"2026-05-18T03:46:16.047Z\", \"hypothesis\": \"Instruct-tuned OLMo-2-1B-Instruct shows degraded depth signal vs base OLMo-2-1B (F1=0.695), quantifying instruction-tuning's impact on DDR\", \"spec\": {\"checkpoint_path\": \"N/A\", \"log_path\": \"/root/gen-depth-fingerprint/data/olmo-2-1b-instruct/\", \"model_name\": \"allenai/OLMo-2-0425-1B-Instruct\", \"note\": \"Used OLMo-2-0425-1B-Instruct (0725 version does not exist on HF)\"}, \"conclusion\": \"success\", \"metrics\": {\"within_binary_f1\": 0.8131, \"within_binary_ci\": [0.8012, 0.8251], \"within_3class_f1\": 0.5748, \"within_3class_ci\": [0.5605, 0.5897], \"base_binary_f1\": 0.8454, \"base_3class_f1\": 0.7538, \"gen1_f1_instruct\": 0.256, \"gen1_f1_base\": 0.523, \"delta_within_binary\": -0.032, \"delta_within_3class\": -0.179, \"spearman_instruct\": {\"entropy_mean\": 0.482, \"entropy_std\": 0.296, \"entropy_min\": 0.08, \"entropy_max\": 0.306, \"tail_decay\": 0.228, \"ttr\": 0.006, \"hapax_ratio\": 0.025}, \"spearman_base\": {\"entropy_mean\": -0.639, \"entropy_std\": -0.296, \"entropy_min\": -0.387, \"entropy_max\": 0.067, \"tail_decay\": -0.141, \"ttr\": -0.7, \"hapax_ratio\": -0.712}, \"features_reversed\": \"6/7\", \"model_used\": \"allenai/OLMo-2-0425-1B-Instruct\"}}, \"exp_052_instruct_qwen3_1_7b\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-18T03:06:04.788Z\", \"updated_at\": \"2026-05-18T03:26:14.267Z\", \"hypothesis\": \"Instruct-tuned Qwen3-1.7B (chat template, thinking=off) shows degraded depth signal vs base Qwen3-1.7B (F1=0.709), quantifying instruction-tuning's impact on DDR\", \"spec\": {\"checkpoint_path\": \"N/A\", \"log_path\": \"/root/gen-depth-fingerprint/data/qwen3-1.7b-instruct/\"}, \"conclusion\": \"success\", \"metrics\": {\"within_binary_f1\": 0.8753, \"within_binary_ci\": [0.8667, 0.8837], \"within_3class_f1\": 0.7324, \"within_3class_ci\": [0.7195, 0.745], \"base_binary_f1\": 0.8614, \"base_3class_f1\": 0.769, \"logo_instruct_binary\": 0.658, \"logo_instruct_3class\": 0.543, \"logo_base_binary\": 0.821, \"logo_base_3class\": 0.802, \"gen1_f1_instruct\": 0.438, \"gen1_f1_base\": 0.579, \"spearman_direction\": \"reversed (instruct ρ>0, base ρ<0)\", \"delta_within_binary\": 0.014, \"delta_within_3class\": -0.037, \"delta_logo_binary\": -0.163}}, \"exp_051_independent_seed\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T22:38:00.466Z\", \"updated_at\": \"2026-05-18T02:01:42.126Z\", \"hypothesis\": \"Cross-generator depth classification with non-overlapping seeds achieves comparable F1 to shared-seed LOGO, ruling out topic fingerprint leakage\", \"spec\": {\"command\": \"generate_chain.py + extract_features.py + eval_independent_seed.py\", \"server\": \"autodl-5090\", \"data_path\": \"data/independent_seed/\", \"data_count\": \"500 seeds per generator\", \"model_name\": \"pythia-2.8b, olmo-2-1b\", \"seed\": 42, \"device\": \"cuda:3\", \"checkpoint_path\": \"N/A (evaluation only)\", \"log_path\": \"/root/gen-depth-fingerprint/results/independent_seed_control/\", \"results_path\": \"/root/gen-depth-fingerprint/results/independent_seed_results.json\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-18T01:59:56.962Z\", \"metrics\": {\"pythia_to_olmo_binary_f1\": 0.6945, \"pythia_to_olmo_ci\": [0.6727, 0.7167], \"olmo_to_pythia_binary_f1\": 0.666, \"olmo_to_pythia_ci\": [0.6429, 0.6893], \"avg_binary_f1\": 0.6803, \"shared_seed_logo_ref\": 0.694, \"delta_vs_shared\": -0.014}}, \"exp_048_cross_temp_transfer\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T12:52:44.889Z\", \"updated_at\": \"2026-05-17T17:07:19.391Z\", \"hypothesis\": \"Cross-temperature transfer: XGBoost 7-feature classifier trained at one sampling temperature (t=0.7 or t=1.0) maintains depth discrimination when tested at a different temperature, demonstrating deployment robustness to unknown decoding parameters\", \"spec\": {\"command\": \"python cross_temp_transfer.py\", \"server\": \"autodl-5090\", \"data_path\": \"/root/gen-depth-fingerprint/data/features_all_models.csv + sampling_ablation features\", \"data_count\": \"~37000\", \"model_name\": \"XGBoost 7-feature (est200, md6)\", \"seed\": \"42\", \"checkpoint_path\": \"N/A (CPU-only eval)\", \"log_path\": \"/root/gen-depth-fingerprint/results/cross_temp_transfer.json\"}, \"conclusion\": \"success\", \"metrics\": {\"6gen_logo\": {\"within_0.7_binary\": 0.9471, \"within_0.7_3class\": 0.7888, \"cross_0.7to1.0_binary\": 0.9001, \"cross_0.7to1.0_3class\": 0.7225, \"within_1.0_binary\": 0.9107, \"within_1.0_3class\": 0.7257, \"cross_1.0to0.7_binary\": 0.9581, \"cross_1.0to0.7_3class\": 0.7913, \"caveat\": \"Only Qwen3-1.7B differs between conditions; 5/6 generators share data\"}, \"qwen_only\": {\"within_0.7_binary\": 0.9262, \"within_0.7_binary_ci\": [0.916, 0.935], \"within_0.7_3class\": 0.769, \"within_0.7_3class_ci\": [0.756, 0.781], \"cross_0.7to1.0_binary\": 0.7574, \"cross_0.7to1.0_binary_ci\": [0.745, 0.77], \"cross_0.7to1.0_3class\": 0.4581, \"cross_0.7to1.0_3class_ci\": [0.445, 0.472], \"within_1.0_binary\": 0.8248, \"within_1.0_binary_ci\": [0.81, 0.838], \"within_1.0_3class\": 0.5738, \"within_1.0_3class_ci\": [0.56, 0.588], \"cross_1.0to0.7_binary\": 0.9443, \"cross_1.0to0.7_binary_ci\": [0.936, 0.953], \"cross_1.0to0.7_3class\": 0.6014, \"cross_1.0to0.7_3class_ci\": [0.593, 0.611], \"delta_0.7train_binary_pp\": -16.9, \"delta_0.7train_3class_pp\": -31.1, \"delta_1.0train_binary_pp\": 12, \"delta_1.0train_3class_pp\": 2.8, \"asymmetric_transfer\": true}}, \"parent\": \"exp_047_multi_domain_t07\", \"completed_at\": \"2026-05-17T17:07:19.391Z\"}, \"exp_047_multi_domain_t07\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T05:51:25.881Z\", \"updated_at\": \"2026-05-17T07:22:04.483Z\", \"hypothesis\": \"Depth fingerprint generalizes across domains (News, Academic, Code) under standard decoding (t=0.7, top_p=0.9) matching main experiment params, eliminating the temperature confound from t=1.0 results and producing directly comparable domain generalization numbers\", \"parent\": \"exp_043_multi_domain_seeds\", \"spec\": {\"command\": \"python run_multi_domain_t07.py (3 generators x 3 domains parallel in tmux multi_domain_t07)\", \"server\": \"autodl-5090\", \"data_path\": \"/root/gen-depth-fingerprint/experiments/multi_domain/\", \"data_count\": \"200 seeds x 3 domains x 3 generators x 4 depths = 7200 samples\", \"model_name\": \"Pythia-1B, Qwen3-1.7B, Mistral-7B-v0.3 (gen) + Pythia-410M (ref)\", \"seed\": \"default\", \"gpu\": \"cuda:0,1,2\", \"checkpoint_source\": \"N/A (generation + evaluation pipeline, no pretrained checkpoint)\", \"eval_data\": \"News/Academic/Code seeds 200 per domain, generated chains depth 0-3\", \"checkpoint_path\": \"/root/gen-depth-fingerprint/experiments/multi_domain/multi_domain_results_t07.json\", \"log_path\": \"/root/gen-depth-fingerprint/experiments/multi_domain/run_t07.log\"}, \"metrics\": {\"news_binary_f1\": 0.7119, \"news_binary_ci\": [0.6898, 0.7332], \"news_3class_f1\": 0.7149, \"academic_binary_f1\": 0.6279, \"academic_binary_ci\": [0.6027, 0.6515], \"academic_3class_f1\": 0.6564, \"code_binary_f1\": 0.6872, \"code_binary_ci\": [0.6641, 0.71], \"code_3class_f1\": 0.6729, \"overall_binary_f1\": 0.6757, \"overall_3class_f1\": 0.6814, \"delta_vs_t10_news\": -0.034, \"delta_vs_t10_academic\": -0.1107, \"delta_vs_t10_code\": -0.0663}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-17T07:22:04.483Z\"}, \"multi-domain-seeds\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T03:38:54.349Z\", \"updated_at\": \"2026-05-17T05:05:40.584Z\", \"hypothesis\": \"Domain independence: depth fingerprint 的 differential depth response 不依赖 seed domain——在 News/Academic/Code 三个非 Wikipedia 域上，7-feature ensemble 的 binary F1 与 Wikipedia baseline 差异 <10pp，证明 DDR 是生成过程的固有特性而非特定域文本属性的 artifact\", \"spec\": {\"command\": \"python multi_domain_generation.py + eval\", \"server\": \"autodl-5090\", \"gpu\": \"cuda:0,1,2,3\", \"data_path\": \"/root/gen-depth-fingerprint/data/seeds_{news,academic,code}.jsonl\", \"data_count\": 600, \"model_name\": \"Pythia-1B + Qwen3-1.7B + Mistral-7B-v0.3\", \"seed\": 42}, \"metrics\": {\"news_binary_f1\": 0.7459, \"news_binary_ci\": [0.726, 0.764], \"news_multiclass_f1\": 0.6516, \"academic_binary_f1\": 0.7386, \"academic_binary_ci\": [0.72, 0.757], \"academic_multiclass_f1\": 0.6223, \"code_binary_f1\": 0.7535, \"code_binary_ci\": [0.737, 0.77], \"code_multiclass_f1\": 0.6344, \"wikipedia_baseline_binary_f1\": 0.8148, \"wikipedia_baseline_multiclass_f1\": 0.8632, \"max_gap_vs_wiki_pp\": 7.62, \"worst_domain\": \"academic\", \"best_domain\": \"code\", \"conclusion_label\": \"domain_independent\"}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/gen-depth-fingerprint/experiments/multi_domain/multi_domain_results.json\", \"log_path\": \"/root/gen-depth-fingerprint/experiments/multi_domain/multi_domain_results.json\", \"completed_at\": \"2026-05-17T05:05:40.584Z\"}, \"plan-008-seed-stratification\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T00:21:12.380Z\", \"updated_at\": \"2026-05-17T02:56:26.724Z\", \"hypothesis\": \"Seed complexity independence: depth fingerprint 的判别能力不依赖 seed 文本的词汇复杂度（按 gen-0 TTR terciles 分层验证）\", \"conclusion\": \"success\", \"metrics\": {\"low_complexity_binary\": 0.685, \"medium_binary\": 0.695, \"high_complexity_binary\": 0.695, \"low_complexity_multi\": 0.772, \"medium_multi\": 0.778, \"high_complexity_multi\": 0.779, \"max_diff_binary_pp\": 1.06, \"max_diff_multiclass_pp\": 0.68, \"conclusion_label\": \"seed_independent\"}, \"checkpoint_path\": \"/root/gen-depth-fingerprint/experiments/seed_stratification/seed_stratification_results.json\", \"log_path\": \"/root/gen-depth-fingerprint/experiments/seed_stratification/\", \"spec\": {\"command\": \"python seed_stratification.py\", \"server\": \"autodl-5090\", \"data_path\": \"/root/gen-depth-fingerprint/data/\", \"data_count\": 37058, \"model_name\": \"XGBoost 200/6\", \"seed\": 42}, \"completed_at\": \"2026-05-17T00:21:48.235Z\", \"parent\": \"plan-010-robustness\"}, \"plan-002-qwen06b-r2-s1\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T22:35:11.142Z\", \"updated_at\": \"2026-05-17T02:56:25.805Z\", \"hypothesis\": \"跨家族泛化数据生成（Qwen3-0.6B shard1）：Qwen3-0.6B continuation 链第二分片，补全 ~995 seeds 覆盖\", \"spec\": {\"command\": \"python generate_chain.py --model-name qwen3-0.6b --model-path /root/autodl-tmp/models/Qwen/Qwen3-0___6B-Base --input data/wiki_seed_1000.jsonl --shard-id 1 --num-shards 2 --device cuda:0\", \"server\": \"autodl-5090\", \"data_path\": \"/root/gen-depth-fingerprint/data/qwen3-0.6b/generations_shard1.jsonl\", \"data_count\": 2500, \"model_name\": \"Qwen3-0.6B\", \"seed\": \"500-999\", \"pid\": \"118126\", \"gpu\": [\"cuda:3\"]}, \"notes\": \"Orphan 进程 PID 118126 存活，shard1 进度 340/500 seeds (68%)，当前 1542 行，预计 ~23:00 UTC 完成。GPU cuda:3 利用率 33%。\", \"conclusion\": \"success\", \"checkpoint_path\": \"/root/gen-depth-fingerprint/data/qwen3-0.6b/generations_shard1.jsonl\", \"log_path\": \"/root/gen-depth-fingerprint/data/qwen3-0.6b/generations_shard1.jsonl\", \"completed_at\": \"2026-05-14T23:01:44.209Z\", \"metrics\": {\"records\": 2268, \"seeds\": 498, \"depth_dist\": {\"0\": 498, \"1\": 493, \"2\": 470, \"3\": 417, \"4\": 390}, \"file\": \"generations_shard1.jsonl\"}, \"parent\": \"plan-002\"}, \"plan-002-qwen06b-r2-s0\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T22:35:10.950Z\", \"updated_at\": \"2026-05-17T02:56:23.413Z\", \"hypothesis\": \"跨家族泛化数据生成（Qwen3-0.6B shard0）：最小参数量(0.6B) Qwen 模型的 continuation 链，验证 depth signal 在极小模型中是否仍存在（小模型可能因容量不足而无法维持深层生成的分布稳定性）\", \"spec\": {\"command\": \"python generate_chain.py --model-name qwen3-0.6b --model-path /root/autodl-tmp/models/Qwen/Qwen3-0___6B-Base --input data/wiki_seed_1000.jsonl --shard-id 0 --num-shards 2 --device cuda:0\", \"server\": \"autodl-5090\", \"data_path\": \"/root/gen-depth-fingerprint/data/qwen3-0.6b/generations_shard0.jsonl\", \"data_count\": 2500, \"model_name\": \"Qwen3-0.6B\", \"seed\": \"0-499\", \"pid\": \"117855\", \"gpu\": [\"cuda:2\"]}, \"notes\": \"Orphan 进程 PID 117855 存活，shard0 进度 350/500 seeds (70%)，当前 1593 行，预计 ~23:00 UTC 完成。GPU cuda:2 利用率 34%。\", \"conclusion\": \"success\", \"metrics\": {\"records\": 2270, \"seeds\": 498, \"depth_dist\": {\"0\": 498, \"1\": 493, \"2\": 468, \"3\": 423, \"4\": 388}, \"file\": \"generations_shard0.jsonl\"}, \"checkpoint_path\": \"/root/gen-depth-fingerprint/data/qwen3-0.6b/generations_shard0.jsonl\", \"log_path\": \"N/A\", \"completed_at\": \"2026-05-14T23:00:55.097Z\", \"parent\": \"plan-002\"}, \"review-exp-c-overall-ci\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T12:22:37.037Z\", \"updated_at\": \"2026-05-17T02:56:15.141Z\", \"hypothesis\": \"6-generator LOGO 的 overall bootstrap CI 窄且不跨越 chance level，entropy_max/entropy_min 的个体 Spearman ρ 验证其对 depth 的单调贡献方向（max 正相关因高 depth 分布更尖，min 负相关因低概率 tail 被压缩）\", \"spec\": {\"command\": \"python scripts/review_overall_ci.py\", \"server\": \"autodl-5090\", \"data_path\": \"data/features_all_models.csv\", \"data_count\": 27529, \"model_name\": \"xgboost\", \"seed\": 42, \"checkpoint_path\": \"n/a\", \"log_path\": \"results/review_overall_ci_results.json\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T12:27:02.426Z\", \"metrics\": {\"overall_logo_f1\": 0.7879, \"overall_ci95\": [0.783, 0.7929], \"spearman_entropy_max\": 0.0503, \"spearman_entropy_min\": -0.4061, \"spearman_hapax\": -0.6467, \"spearman_ttr\": -0.6302, \"spearman_entropy_mean\": -0.6098, \"spearman_entropy_std\": -0.1996, \"spearman_tail_decay\": -0.0403}}, \"review-exp-b-topic-drift\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T12:22:34.096Z\", \"updated_at\": \"2026-05-17T02:56:11.446Z\", \"hypothesis\": \"Depth fingerprint 不仅仅捕捉 topic shift：语义漂移(embedding cosine similarity)与 depth 相关性弱(|ρ|<0.3)，而 entropy/lexical features 与 depth 的相关性强(|ρ|>0.5)，证明 depth signal 来自生成过程的统计特性而非内容偏移\", \"spec\": {\"command\": \"python scripts/review_topic_drift.py\", \"server\": \"autodl-5090\", \"data_path\": \"/root/gen-depth-fingerprint/data/\", \"data_count\": 27529, \"model_name\": \"all-MiniLM-L6-v2\", \"seed\": 0}, \"conclusion\": \"success\", \"log_path\": \"/tmp/topic_drift.log\", \"checkpoint_path\": \"/root/gen-depth-fingerprint/results/review_topic_drift_results.json\", \"completed_at\": \"2026-05-15T12:28:11.624Z\", \"metrics\": {\"semantic_similarity_by_transition\": {\"0_to_1\": {\"mean\": 0.622, \"std\": 0.1647}, \"1_to_2\": {\"mean\": 0.6829, \"std\": 0.1837}, \"2_to_3\": {\"mean\": 0.801, \"std\": 0.2012}, \"3_to_4\": {\"mean\": 0.8587, \"std\": 0.1895}}, \"prompt_type_avg_sim\": {\"continuation\": 0.7168, \"elaboration\": 0.8093, \"inspired_rewriting\": 0.808}, \"shape_feature_correlations\": {\"entropy_std_rho\": -0.1639, \"tail_decay_rho\": 0.0675}, \"drifting_feature_correlations\": {\"hapax_ratio_rho\": -0.1242, \"ttr_rho\": -0.1784, \"entropy_mean_rho\": -0.2859}}}, \"plan-014\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T00:12:01.909Z\", \"updated_at\": \"2026-05-17T02:56:07.395Z\", \"hypothesis\": \"大模型规模泛化：Qwen3-8B (7B+参数) 的 continuation 链是否展现同样的 entropy 收敛和 lexical drift，验证 depth dynamics 不因模型容量增大而消失（更大模型可能有更强的分布记忆导致 depth signal 衰减）\", \"spec\": {\"command\": \"nohup /root/miniconda3/bin/python generate_chain.py --model-name qwen3-8b --model-path /root/autodl-tmp/models/Qwen/Qwen3-8B-Base/Qwen/Qwen3-8B-Base/ --input data/openwebtext_seeds.jsonl --shard-id 0 --num-shards 1 --device cuda:0 > /tmp/gen_large_model.log 2>&1 &\", \"server\": \"autodl-5090\", \"gpu\": \"cuda:0\", \"pid\": 134817, \"data_path\": \"data/wiki_seed_1000.jsonl\", \"data_count\": 996, \"model_name\": \"Qwen3-8B-Base\", \"seed\": \"all\", \"log_path\": \"/tmp/gen_large_model.log\", \"checkpoint_path\": \"/root/gen-depth-fingerprint/data/qwen3-8b/generations_shard0.jsonl\", \"output_path\": \"data/qwen3-8b/generations_shard0.jsonl\", \"estimated_duration_h\": 4, \"model_params\": \"8.2B\", \"fp16_vram_gb\": 16.1}, \"notes\": \"2026-05-15 04:25: ✅ 完整数据重算完成 (4409 records, 977 seeds)。与 82% 快照差异在统计噪声范围内：LOGO +0.0011, qwen8b held-out -0.0037。最终数字已确认，可用于论文。\", \"conclusion\": \"success\", \"metrics\": {\"total_records\": 4497, \"unique_seeds\": 995, \"depth_dist\": {\"0\": 995, \"1\": 979, \"2\": 937, \"3\": 831, \"4\": 755}, \"logo_6gen_avg_f1\": 0.7893, \"logo_per_generator\": {\"olmo-2-1b\": 0.7635, \"pythia-1b\": 0.8562, \"pythia-2.8b\": 0.8041, \"qwen3-0.6b\": 0.8243, \"qwen3-1.7b\": 0.8046, \"qwen3-8b\": 0.6832}, \"logo_qwen3_8b_held_out_f1\": 0.6832, \"logo_5gen_baseline_f1\": 0.8, \"spearman\": {\"hapax_ratio\": -0.5578, \"ttr\": -0.5419, \"entropy_mean\": -0.4754, \"entropy_min\": -0.3029, \"entropy_max\": 0.0946, \"tail_decay\": -0.0894, \"entropy_std\": -0.0755}, \"feature_importance\": {\"hapax_ratio\": 0.269, \"entropy_mean\": 0.1637, \"ttr\": 0.159, \"entropy_max\": 0.0634, \"entropy_std\": 0.0463, \"entropy_min\": 0.0153, \"tail_decay\": 0.0123}, \"revalidation_v2_vs_snapshot\": \"LOGO +0.0007 (0.7886→0.7893), qwen8b -0.0054 (0.6886→0.6832)\", \"revalidation_v2_conclusion\": \"complete_data_validates_snapshot_robustness\"}, \"completed_at\": \"2026-05-15T03:47:24.272Z\", \"parent\": \"plan-002\"}, \"plan-002-qwen17b-r2-s1\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T21:58:14.195Z\", \"updated_at\": \"2026-05-17T02:56:03.576Z\", \"spec\": {\"command\": \"python generate_chain.py --model-name qwen3-1.7b --model-path /root/autodl-tmp/models/Qwen/Qwen3-1___7B-Base --input data/wiki_seed_1000.jsonl --shard-id 1 --num-shards 2 --device cuda:0\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:1\"], \"pid\": \"120694\", \"log_path\": \"~/runs/gen-depth-fingerprint/plan-002-qwen17b-r2-s1.log\", \"submitted_at\": \"2026-05-14T21:58:14.157Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/gen-depth-fingerprint/data/qwen3-1.7b/generations_shard1.jsonl\", \"data_count\": 2500, \"model_name\": \"Qwen3-1.7B\", \"seed\": \"500-999\", \"wall_clock_seconds\": 4435.6, \"gpu_hours\": 1.23}, \"notes\": \"Orphan 进程 PID 120694 存活，shard1 进度 295/500 seeds (59%)，预计 ~22:55 UTC 完成。GPU cuda:1 利用率 44%。\", \"reproduce\": {\"finished_at\": \"2026-05-14T23:09:11.091Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T23:09:12.039773+00:00\"}]}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/gen-depth-fingerprint/data/qwen3-1.7b/generations_shard1.jsonl\", \"log_path\": \"~/runs/gen-depth-fingerprint/plan-002-qwen17b-r2-s1.log\", \"metrics\": {\"records\": 2326, \"seeds\": 498, \"depth_dist\": {\"0\": 498, \"1\": 491, \"2\": 473, \"3\": 440, \"4\": 424}, \"skipped\": 53, \"duration_s\": 4228, \"file\": \"generations_shard1.jsonl\"}, \"completed_at\": \"2026-05-14T23:12:09.724Z\", \"hypothesis\": \"跨家族泛化数据生成（Qwen3-1.7B shard1）：Qwen3-1.7B continuation 链第二分片，补全 ~995 seeds 覆盖\", \"parent\": \"plan-002\"}, \"plan-002-qwen17b-r2-s0\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T21:58:12.310Z\", \"updated_at\": \"2026-05-17T02:56:01.158Z\", \"spec\": {\"command\": \"python generate_chain.py --model-name qwen3-1.7b --model-path /root/autodl-tmp/models/Qwen/Qwen3-1___7B-Base --input data/wiki_seed_1000.jsonl --shard-id 0 --num-shards 2 --device cuda:0\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:0\"], \"pid\": \"120617\", \"log_path\": \"~/runs/gen-depth-fingerprint/plan-002-qwen17b-r2-s0.log\", \"submitted_at\": \"2026-05-14T21:58:12.274Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/gen-depth-fingerprint/data/qwen3-1.7b/generations_shard0.jsonl\", \"data_count\": 2500, \"model_name\": \"Qwen3-1.7B\", \"seed\": \"0-499\", \"wall_clock_seconds\": 7656.9, \"gpu_hours\": 2.13}, \"notes\": \"Orphan 进程 PID 120617 存活，shard0 进度 289/500 seeds (58%)，预计 ~22:55 UTC 完成。GPU cuda:0 利用率 40%。\", \"reproduce\": {\"finished_at\": \"2026-05-14T23:15:31.078Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T23:15:31.991817+00:00\"}]}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/gen-depth-fingerprint/data/qwen3-1.7b/generations_shard0.jsonl\", \"log_path\": \"~/runs/gen-depth-fingerprint/plan-002-qwen17b-r2-s0.log\", \"metrics\": {\"records\": 2291, \"seeds\": 498, \"depth_dist\": {\"0\": 498, \"1\": 492, \"2\": 468, \"3\": 435, \"4\": 398}, \"skipped\": 199, \"duration_s\": 4548.2, \"file_size_mb\": 2.5, \"file\": \"generations_shard0.jsonl\"}, \"completed_at\": \"2026-05-15T00:05:49.186Z\", \"hypothesis\": \"跨家族泛化数据生成（Qwen3-1.7B shard0）：Qwen 家族 1.7B 模型的 continuation 链 depth dynamics，验证中等规模非 Pythia 模型也产生可检测的 depth signal\", \"parent\": \"plan-002\"}, \"plan-002-olmo2-s1\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T20:09:46.880Z\", \"updated_at\": \"2026-05-17T02:55:54.134Z\", \"spec\": {\"command\": \"python generate_chain.py --model-name olmo-2-1b --shard-id 1 --num-shards 2\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:3\"], \"pid\": \"108452\", \"log_path\": \"~/runs/gen-depth-fingerprint/plan-002-olmo2-s1.log\", \"submitted_at\": \"2026-05-14T20:09:46.862Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/gen-depth-fingerprint/data/wiki_seed_1000.jsonl\", \"data_count\": 1000, \"model_name\": \"allenai/OLMo-2-0425-1B\", \"seed\": 42, \"wall_clock_seconds\": 4242.5, \"gpu_hours\": 1.18}, \"reproduce\": {\"finished_at\": \"2026-05-14T21:18:05.854Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T21:18:09.081771+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"records\": 2334, \"seeds\": 498, \"skipped\": 70, \"wall_time_s\": 4081.2, \"depth_dist\": {\"gen0\": 498, \"gen1\": 494, \"gen2\": 470, \"gen3\": 444, \"gen4\": 428}, \"file\": \"generations_shard1.jsonl\", \"file_size_mb\": 2.57}, \"checkpoint_path\": \"/root/gen-depth-fingerprint/data/olmo-2-1b/generations_shard1.jsonl\", \"completed_at\": \"2026-05-14T21:20:29.344Z\", \"hypothesis\": \"跨家族泛化数据生成（OLMo-2-1B shard1）：OLMo-2-1B continuation 链第二分片，补全 ~995 seeds 覆盖\", \"parent\": \"plan-002\"}, \"plan-002-olmo2-s0\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T20:09:45.173Z\", \"updated_at\": \"2026-05-17T02:55:52.145Z\", \"spec\": {\"command\": \"python generate_chain.py --model-name olmo-2-1b --shard-id 0 --num-shards 2\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:2\"], \"pid\": \"108242\", \"log_path\": \"~/runs/gen-depth-fingerprint/plan-002-olmo2-s0.log\", \"submitted_at\": \"2026-05-14T20:09:45.156Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/gen-depth-fingerprint/data/wiki_seed_1000.jsonl\", \"data_count\": 1000, \"model_name\": \"allenai/OLMo-2-0425-1B\", \"seed\": 42, \"wall_clock_seconds\": 4243.6, \"gpu_hours\": 1.18}, \"reproduce\": {\"finished_at\": \"2026-05-14T21:17:49.730Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T21:17:50.547144+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"records\": 2379, \"seeds\": 497, \"skipped\": 47, \"wall_time_s\": 3885.2, \"depth_dist\": {\"gen0\": 497, \"gen1\": 494, \"gen2\": 477, \"gen3\": 461, \"gen4\": 450}, \"file\": \"generations_shard0.jsonl\", \"file_size_mb\": 2.68}, \"checkpoint_path\": \"/root/gen-depth-fingerprint/data/olmo-2-1b/generations_shard0.jsonl\", \"completed_at\": \"2026-05-14T21:20:28.747Z\", \"hypothesis\": \"跨家族泛化数据生成（OLMo-2-1B shard0）：非 Pythia 架构(OLMo)的 continuation 链中 depth signal 是否存在，验证 depth dynamics 跨训练数据和架构的普遍性\", \"parent\": \"plan-002\"}, \"plan-002-pythia1b-s1\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T20:09:42.815Z\", \"updated_at\": \"2026-05-17T02:55:49.321Z\", \"spec\": {\"command\": \"python generate_chain.py --model-name pythia-1b --shard-id 1 --num-shards 2\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:1\"], \"pid\": \"108098\", \"log_path\": \"~/runs/gen-depth-fingerprint/plan-002-pythia1b-s1.log\", \"submitted_at\": \"2026-05-14T20:09:42.799Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/gen-depth-fingerprint/data/wiki_seed_1000.jsonl\", \"data_count\": 1000, \"model_name\": \"EleutherAI/pythia-1b\", \"seed\": 42, \"checkpoint_path\": \"/root/gen-depth-fingerprint/data/pythia-1b/generations_shard1.jsonl\", \"wall_clock_seconds\": 2862.4, \"gpu_hours\": 0.8}, \"reproduce\": {\"finished_at\": \"2026-05-14T20:50:17.333Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T20:50:18.063486+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"records\": 2269, \"seeds\": 498, \"skipped\": 100, \"wall_time_s\": 2247.6, \"depth_dist\": {\"gen0\": 498, \"gen1\": 496, \"gen2\": 455, \"gen3\": 422, \"gen4\": 398}, \"file\": \"data/pythia-1b/generations_shard1.jsonl\", \"file_size_mb\": 2.44}, \"completed_at\": \"2026-05-14T20:57:25.200Z\", \"hypothesis\": \"跨模型泛化数据生成（Pythia-1B shard1）：Pythia-1B continuation 链第二分片，与 shard0 合并后提供完整 ~995 seeds 的 depth 数据\", \"parent\": \"plan-002\"}, \"plan-002-pythia1b-s0\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T20:09:40.947Z\", \"updated_at\": \"2026-05-17T02:55:46.455Z\", \"spec\": {\"command\": \"python generate_chain.py --model-name pythia-1b --shard-id 0 --num-shards 2\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:0\"], \"pid\": \"108021\", \"log_path\": \"~/runs/gen-depth-fingerprint/plan-002-pythia1b-s0.log\", \"submitted_at\": \"2026-05-14T20:09:40.932Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/gen-depth-fingerprint/data/wiki_seed_1000.jsonl\", \"data_count\": 1000, \"model_name\": \"EleutherAI/pythia-1b\", \"seed\": 42, \"checkpoint_path\": \"/root/gen-depth-fingerprint/data/pythia-1b/generations_shard0.jsonl\", \"wall_clock_seconds\": 2862.8, \"gpu_hours\": 0.8}, \"reproduce\": {\"finished_at\": \"2026-05-14T20:50:12.706Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T20:50:13.422601+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"records\": 2286, \"seeds\": 497, \"skipped\": 91, \"wall_time_s\": 2296.7, \"depth_dist\": {\"gen0\": 497, \"gen1\": 497, \"gen2\": 457, \"gen3\": 429, \"gen4\": 406}, \"file\": \"data/pythia-1b/generations_shard0.jsonl\", \"file_size_mb\": 2.5}, \"completed_at\": \"2026-05-14T20:57:23.757Z\", \"hypothesis\": \"跨模型泛化数据生成（Pythia-1B shard0）：同家族更大模型 Pythia-1B 的 continuation 链是否展现与 Pythia-2.8B 相似的 depth dynamics，验证 depth signal 非特定参数量产物\", \"parent\": \"plan-002\"}, \"plan-002-eval\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T23:33:25.348Z\", \"updated_at\": \"2026-05-17T02:55:34.658Z\", \"hypothesis\": \"跨生成器泛化评估：Pythia-410M 深度特征在 leave-one-generator-out 设置下能否泛化到未见过的生成器\", \"conclusion\": \"success\", \"metrics\": {\"leave_one_out_avg_macro_f1\": 0.8037, \"best_held_out\": {\"model\": \"pythia-1b\", \"macro_f1\": 0.8507}, \"worst_held_out\": {\"model\": \"olmo-2-1b\", \"macro_f1\": 0.7519}, \"family_out_delta\": 0.0107, \"ablation_full_f1\": 0.8037, \"ablation_reference_only_f1\": 0.7543, \"ablation_surface_only_f1\": 0.7471, \"mcnemar_p\": 0, \"top_features\": [\"hapax_ratio_0.289\", \"ttr_0.168\", \"entropy_mean_0.160\"], \"entropy_std_drop\": 0.0049, \"entropy_std_drift\": 0.12, \"entropy_mean_drift\": 1.5}, \"spec\": {\"command\": \"python cross_generator_eval.py\", \"server\": \"autodl-5090\", \"data_path\": \"/root/gen-depth-fingerprint/data/features_all_models.csv\", \"data_count\": 23032, \"model_name\": \"XGBoost classifier\", \"seed\": 42, \"checkpoint_path\": \"/root/gen-depth-fingerprint/data/cross_generator_results.json\", \"log_path\": \"/root/gen-depth-fingerprint/data/cross_generator_report.md\"}, \"completed_at\": \"2026-05-14T23:40:47.236Z\", \"parent\": \"plan-002\"}, \"plan-010-llm-rephrase\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T22:26:58.107Z\", \"updated_at\": \"2026-05-17T02:55:34.090Z\", \"hypothesis\": \"LLM-simulated editing robustness: Qwen3-0.6B rephrasing (1-3 sentences) 比 random word replacement 更接近真实人类编辑，预期 depth fingerprint 退化更小\", \"spec\": {\"command\": \"python llm_rephrase_robustness.py\", \"server\": \"autodl-5090\", \"gpu\": \"cuda:0\", \"data_path\": \"/root/gen-depth-fingerprint/experiments/human_edit_robustness/\", \"data_count\": 5000, \"model_name\": \"Qwen3-0.6B-Base + Pythia-410M\", \"seed\": 42}, \"conclusion\": \"success\", \"notes\": \"v2 修复版：修正 binary task 定义(gen1-vs-gen2+)、3-class mapping、tail_decay 计算(rank 100-1000)。Original binary 0.6918 与 Table 3 (0.7014) 一致，确认修复正确。\", \"metrics\": {\"original_binary_f1\": 0.6918, \"original_binary_ci\": [0.6749, 0.7067], \"original_multiclass_f1\": 0.7385, \"original_multiclass_ci\": [0.7269, 0.7496], \"rephrased_binary_f1\": 0.6471, \"rephrased_binary_ci\": [0.6308, 0.6619], \"rephrased_multiclass_f1\": 0.6672, \"rephrased_multiclass_ci\": [0.6548, 0.6796], \"binary_drop\": -0.0447, \"multiclass_drop\": -0.0713, \"edit_distance_ratio\": 0.5071, \"avg_sentences_replaced\": 1.69, \"method\": \"7feature LOGO-CV, binary=gen1-vs-gen2+, 3class=gen0/gen1/gen2+\", \"bugs_fixed\": [\"binary_task_gen1_vs_gen2+\", \"3class_mapping\", \"tail_decay_rank100-1000\"]}, \"checkpoint_path\": \"/root/gen-depth-fingerprint/experiments/human_edit_robustness/llm_rephrase_results.json\", \"log_path\": \"/root/gen-depth-fingerprint/experiments/human_edit_robustness/llm_rephrase_results.json\", \"completed_at\": \"2026-05-17T01:04:28.657Z\", \"parent\": \"plan-010-robustness\"}, \"plan-015-v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T00:56:20.612Z\", \"updated_at\": \"2026-05-17T02:55:33.529Z\", \"spec\": {\"command\": \"PYTHONUNBUFFERED=1 HF_HUB_OFFLINE=1 CUDA_VISIBLE_DEVICES=2 python scripts/ordinal_baseline.py --device cuda:0\", \"server\": \"autodl-5090\", \"data_path\": \"/root/gen-depth-fingerprint/data/\", \"data_count\": 0, \"model_name\": \"pythia-410m+pythia-160m\", \"seed\": 42, \"checkpoint_path\": \"N/A (analysis task)\", \"log_path\": \"/tmp/ordinal_baseline_v2.log\"}, \"conclusion\": \"success\", \"hypothesis\": \"Ordinal baseline bugfix + bootstrap CI: 修复 Binoculars denominator bug，验证 7-feature ensemble 显著优于所有单一检测器\", \"metrics\": {\"seven_feature_logo_f1\": 0.798, \"seven_feature_ci95\": [0.786, 0.799], \"avg_logprob_logo_f1\": 0.7653, \"avg_logprob_ci95\": [0.616, 0.82], \"ld_score_logo_f1\": 0.7212, \"ld_score_ci95\": [0.588, 0.77], \"fastdetectgpt_logo_f1\": 0.6269, \"fastdetectgpt_ci95\": [0.511, 0.762], \"binoculars_logo_f1\": 0.579, \"binoculars_ci95\": [0.405, 0.664], \"binoculars_bug_fixed\": true, \"ld_score_corrected_cv_f1\": 0.7925, \"bootstrap_7feat_vs_avglogprob\": {\"delta\": 0.039, \"p\": 0, \"significant\": true}, \"bootstrap_7feat_vs_fastdetectgpt\": {\"delta\": 0.067, \"p\": 0, \"significant\": true}}, \"completed_at\": \"2026-05-15T01:26:40.380Z\", \"parent\": \"plan-015\"}, \"plan-003-olmo2ref\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T00:09:31.145Z\", \"updated_at\": \"2026-05-17T02:55:33.041Z\", \"spec\": {\"command\": \"python extract_features_crossref.py --reference-model /root/autodl-tmp/models/olmo-2-1b-hf/allenai/OLMo-2-0425-1B --output data/features_ref_olmo.csv --device cuda:0\", \"server\": \"autodl-5090\", \"data_path\": \"/root/gen-depth-fingerprint/data/\", \"data_count\": 23032, \"model_name\": \"OLMo-2-1B (reference)\", \"seed\": 42}, \"checkpoint_path\": \"/root/gen-depth-fingerprint/data/features_ref_olmo.csv\", \"log_path\": \"/root/gen-depth-fingerprint/data/features_ref_olmo.csv\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T00:10:00.971Z\", \"hypothesis\": \"跨家族参考模型验证（OLMo-2-1B）：用 OLMo-2-1B 作为参考模型提取 differential entropy 特征，验证 depth signal 的参考模型无关性——不同训练数据和架构的模型仍能检测相同的 depth dynamics\", \"parent\": \"plan-003\"}, \"plan-003-qwen06bref\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T00:09:31.649Z\", \"updated_at\": \"2026-05-17T02:55:27.742Z\", \"spec\": {\"command\": \"python extract_features_crossref.py --reference-model /root/autodl-tmp/models/Qwen/Qwen3-0___6B-Base --output data/features_ref_qwen.csv --device cuda:0\", \"server\": \"autodl-5090\", \"data_path\": \"/root/gen-depth-fingerprint/data/\", \"data_count\": 23032, \"model_name\": \"Qwen3-0.6B (reference)\", \"seed\": 42}, \"checkpoint_path\": \"/root/gen-depth-fingerprint/data/features_ref_qwen.csv\", \"log_path\": \"/root/gen-depth-fingerprint/data/features_ref_qwen.csv\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T00:10:01.383Z\", \"hypothesis\": \"跨家族参考模型验证（Qwen3-0.6B）：用非 Pythia 家族的 Qwen3-0.6B 作为参考模型提取 differential entropy 特征，验证 depth signal 不依赖于参考模型与生成器的家族匹配\", \"parent\": \"plan-003\"}, \"plan-005-rewrite\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T03:28:47.421Z\", \"updated_at\": \"2026-05-17T02:55:19.976Z\", \"spec\": {\"command\": \"python generate_chain_prompt.py --model-name pythia-2.8b --prompt-type inspired_rewriting --input data/wiki_seed_1000.jsonl --shard-id 0 --num-shards 1 --device cuda:0\", \"server\": \"autodl-5090\", \"gpu\": \"cuda:3\", \"pid\": 164881, \"log_path\": \"~/runs/gen-depth-fingerprint/plan-005-rewrite.log\", \"submitted_at\": \"2026-05-15T03:28:47.322Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/wiki_seed_1000.jsonl\", \"data_count\": 1000, \"model_name\": \"pythia-2.8b\", \"seed\": \"all\", \"prompt_type\": \"inspired_rewriting\", \"checkpoint_path\": \"/root/gen-depth-fingerprint/data/pythia-2.8b-inspired_rewriting/generations_shard0.jsonl\", \"wall_clock_seconds\": 8584, \"gpu_hours\": 2.38}, \"reproduce\": {\"finished_at\": \"2026-05-15T05:53:16.289Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T05:53:17.523804+00:00\"}]}, \"metrics\": {\"total_records\": 4827, \"unique_seeds\": 995, \"skipped\": 61, \"depth_distribution\": {\"0\": 995, \"1\": 995, \"2\": 959, \"3\": 944, \"4\": 934}, \"output_file\": \"/root/gen-depth-fingerprint/data/pythia-2.8b-inspired_rewriting/generations_shard0.jsonl\", \"file_size_mb\": 5.41, \"runtime_seconds\": 8584, \"speed_seeds_per_sec\": 0.12, \"depth_retention_d4_d0\": 0.939, \"vs_continuation\": \"retention 93.9% vs 83.1%, rewriting produces significantly more stable depth chains\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T06:00:25.058Z\", \"hypothesis\": \"Inspired rewriting 链数据生成：rewriting prompt 要求模型受启发重写而非逐字续写，预期 depth retention 介于 continuation 和 elaboration 之间，因为重写保留主题但改变表达\", \"parent\": \"plan-005\"}, \"plan-005-elab\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T03:28:45.680Z\", \"updated_at\": \"2026-05-17T02:55:17.294Z\", \"spec\": {\"command\": \"python generate_chain_prompt.py --model-name pythia-2.8b --prompt-type elaboration --input data/wiki_seed_1000.jsonl --shard-id 0 --num-shards 1 --device cuda:0\", \"server\": \"autodl-5090\", \"gpu\": \"cuda:2\", \"pid\": 164737, \"log_path\": \"/root/gen-depth-fingerprint/logs/plan-005-elab\", \"submitted_at\": \"2026-05-15T03:28:45.601Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/wiki_seed_1000.jsonl\", \"data_count\": 1000, \"model_name\": \"pythia-2.8b\", \"seed\": \"all\", \"prompt_type\": \"elaboration\", \"checkpoint_path\": \"/root/gen-depth-fingerprint/data/pythia-2.8b-elaboration/generations_shard0.jsonl\", \"wall_clock_seconds\": 19266.7, \"gpu_hours\": 5.35}, \"reproduce\": {\"finished_at\": \"2026-05-15T05:58:50.421Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T05:58:51.901208+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"total_records\": 4946, \"unique_seeds\": 995, \"skipped\": 14, \"depth_distribution\": {\"0\": 995, \"1\": 995, \"2\": 989, \"3\": 986, \"4\": 981}, \"output_file\": \"/root/gen-depth-fingerprint/data/pythia-2.8b-elaboration/generations_shard0.jsonl\", \"file_size_mb\": 5.53, \"runtime_seconds\": 8960.2, \"depth_retention_d4_d0\": 0.986, \"logo_cv_f1\": {\"mean\": 0.73, \"std\": 0.011}, \"lopto_f1\": 0.7622, \"feature_drift_entropy_mean\": -0.4705, \"feature_drift_ttr\": -0.6413, \"feature_drift_hapax\": -0.8284, \"vs_continuation\": \"retention 98.6% vs 83.1%; CV F1 0.730 vs 0.781 — elaboration chains more stable but depth signal weaker within-type\", \"vs_rewriting\": \"retention 98.6% vs 93.9%; CV F1 0.730 vs 0.737 — similar discriminability, elaboration slightly lower\"}, \"completed_at\": \"2026-05-15T08:49:52.315Z\", \"hypothesis\": \"Elaboration 链数据生成：elaboration prompt 要求模型展开而非续写，预期 depth signal 因语义锚定更强而衰减更慢（retention > continuation 的 83%）\", \"parent\": \"plan-005\"}, \"plan-005-cont\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T03:28:43.383Z\", \"updated_at\": \"2026-05-17T02:55:14.334Z\", \"spec\": {\"command\": \"python generate_chain_prompt.py --model-name pythia-2.8b --prompt-type continuation\", \"server\": \"autodl-5090\", \"gpu\": \"cuda:1\", \"pid\": 164658, \"log_path\": \"/root/runs/gen-depth-fingerprint/plan-005-cont.log\", \"submitted_at\": \"2026-05-15T03:28:43.303Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/gen-depth-fingerprint/data/wiki_seed_1000.jsonl\", \"data_count\": 995, \"model_name\": \"pythia-2.8b\", \"seed\": 0, \"prompt_type\": \"continuation\", \"checkpoint_path\": \"/root/gen-depth-fingerprint/data/pythia-2.8b-continuation/generations_shard0.jsonl\", \"wall_clock_seconds\": 8050.6, \"gpu_hours\": 2.24}, \"reproduce\": {\"finished_at\": \"2026-05-15T05:40:03.942Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T05:40:05.254414+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"total_records\": 4620, \"unique_seeds\": 995, \"skipped\": 168, \"depth_distribution\": {\"0\": 995, \"1\": 992, \"2\": 932, \"3\": 874, \"4\": 827}, \"output_file\": \"/root/gen-depth-fingerprint/data/pythia-2.8b-continuation/generations_shard0.jsonl\", \"file_size_mb\": 4.93, \"runtime_seconds\": 7760, \"speed_seeds_per_sec\": 0.13}, \"completed_at\": \"2026-05-15T05:42:53.944Z\", \"hypothesis\": \"Continuation 链数据生成：Pythia-2.8B 在 continuation prompt 下生成 depth 0-4 链，验证递归续写中 entropy/lexical 特征的单调漂移模式是否在 1000 seeds 规模下稳定复现\", \"parent\": \"plan-005\"}, \"plan-001-fix\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T18:50:14.620Z\", \"updated_at\": \"2026-05-17T02:55:10.600Z\", \"spec\": {\"command\": \"python ablation_analysis.py --parts A B C --device cuda:0\", \"server\": \"autodl-5090\", \"data_path\": \"data/features.csv + data/generations.jsonl\", \"data_count\": 4609, \"model_name\": \"pythia-410m\", \"seed\": 42, \"pid\": 101585, \"log_path\": \"/tmp/plan-001-fix.log\", \"checkpoint_path\": \"/root/gen-depth-fingerprint/results/ablation_results.json\"}, \"conclusion\": \"success\", \"metrics\": {\"full_macro_f1\": 0.8204, \"reference_only_f1\": 0.7187, \"surface_only_f1\": 0.7628, \"ref_vs_surf_bootstrap_ci\": \"[0.706,0.733] vs [0.747,0.774]\", \"h2_features\": \"entropy_mean, ttr, hapax_ratio\", \"h1_features\": \"tail_decay, entropy_std, entropy_max, entropy_min\", \"median_ppl_by_depth\": \"13.50, 4.96, 3.00, 2.07, 1.72\"}, \"completed_at\": \"2026-05-14T19:34:25.973Z\", \"hypothesis\": \"Feature ablation 修复验证：reference-only features (entropy系列+tail_decay) 独立于 surface features 仍能区分 depth，且两组特征的 bootstrap CI 不重叠，证明 differential response 和 lexical drift 是互补的独立信号源\", \"parent\": \"plan-001\"}, \"plan-010-robustness\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T22:09:57.049Z\", \"updated_at\": \"2026-05-16T22:11:48.657Z\", \"hypothesis\": \"Human edit robustness: depth fingerprint 在 5-20% random word replacement 下的 F1 退化测试，验证实际编辑场景（通常 < 5%）不影响检测\", \"conclusion\": \"success\", \"metrics\": {\"baseline_binary_f1\": 0.695, \"5pct_binary_f1\": 0.65, \"10pct_binary_f1\": 0.614, \"20pct_binary_f1\": 0.591, \"5pct_drop\": -0.046, \"10pct_drop\": -0.081, \"20pct_drop\": -0.104}, \"checkpoint_path\": \"/root/gen-depth-fingerprint/experiments/human_edit_robustness/robustness_results.json\", \"log_path\": \"/root/gen-depth-fingerprint/experiments/human_edit_robustness/\", \"spec\": {\"command\": \"python human_edit_robustness.py\", \"server\": \"autodl-5090\", \"gpu\": \"cuda:0\", \"data_path\": \"/root/gen-depth-fingerprint/data/detector_scores_8gen.csv\", \"data_count\": 5000, \"model_name\": \"Pythia-410M (reference)\", \"seed\": 42, \"perturbation_rates\": [0.05, 0.1, 0.2]}, \"completed_at\": \"2026-05-16T22:11:48.657Z\"}, \"plan-005\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T03:24:02.435Z\", \"updated_at\": \"2026-05-15T06:20:59.698Z\", \"hypothesis\": \"Prompt type comparison: continuation vs elaboration vs inspired_rewriting 链的 depth signal 强度差异。Pythia-2.8B, 1000 seeds, 3 prompt types × 5 depths = 15K texts\", \"spec\": {\"command\": \"python scripts/analyze_prompt_types.py\", \"server\": \"autodl-5090\", \"gpu\": \"cuda:1,cuda:2,cuda:3\", \"data_path\": \"data/pythia-2.8b-*/features.jsonl\", \"data_count\": 14393, \"model_name\": \"pythia-2.8b\", \"seed\": 42, \"log_path\": \"tmux: plan-005-cont, plan-005-elab, plan-005-rewrite\"}, \"notes\": \"plan-005 完成。3 种 prompt type 全部成功。关键发现：(1) depth signal 跨 prompt type 存在（CV F1 0.73-0.78）；(2) LOPTO 泛化良好（avg 0.7525）；(3) surface features (ttr, hapax) 最稳健；(4) shape features 在非 continuation 中信号消失；(5) continuation 衰减最大（16.9%），elaboration 几乎无衰减（1.4%）。\", \"failure_reason\": \"startup recovery: RUNNING with no cron and no server/pid info\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T05:30:39.849Z\", \"metrics\": {\"cv_f1\": {\"continuation\": 0.7806, \"inspired_rewriting\": 0.7368, \"elaboration\": 0.73}, \"lopto_f1\": {\"held_out_cont\": 0.762, \"held_out_elab\": 0.7622, \"held_out_rewrite\": 0.7334, \"avg\": 0.7525}, \"depth_retention_d4_d0\": {\"continuation\": 0.831, \"inspired_rewriting\": 0.939, \"elaboration\": 0.986}, \"drift_hapax_ratio\": {\"continuation\": -0.74, \"elaboration\": -0.828, \"rewriting\": -0.8}, \"drift_ttr\": {\"continuation\": -0.607, \"elaboration\": -0.641, \"rewriting\": -0.618}, \"drift_entropy_mean\": {\"continuation\": -0.557, \"elaboration\": -0.471, \"rewriting\": -0.477}, \"spearman_ttr\": {\"continuation\": -0.629, \"elaboration\": -0.666, \"rewriting\": -0.659}, \"spearman_hapax\": {\"continuation\": -0.651, \"elaboration\": -0.674, \"rewriting\": -0.67}, \"spearman_entropy_mean\": {\"continuation\": -0.665, \"elaboration\": -0.583, \"rewriting\": -0.564}}}, \"plan-015\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T23:58:41.890Z\", \"updated_at\": \"2026-05-15T01:25:59.552Z\", \"hypothesis\": \"现有检测器 ordinal baseline：FastDetectGPT/LD-Score 等检测器的连续分数是否已提供 ordinal depth signal\", \"spec\": {\"command\": \"python detector_baseline.py (log_likelihood + fast_detect_gpt + entropy_mean)\", \"server\": \"autodl-5090\", \"data_path\": \"/root/gen-depth-fingerprint/data/features_all_models.csv\", \"data_count\": 23032, \"model_name\": \"Pythia-410M (log_likelihood, FastDetectGPT, entropy_mean baselines)\", \"seed\": 42, \"checkpoint_path\": \"/root/gen-depth-fingerprint/data/detector_baseline_results.json\", \"log_path\": \"/root/gen-depth-fingerprint/data/\"}, \"conclusion\": \"success\", \"metrics\": {\"seven_feature_logo_f1\": 0.798, \"seven_feature_ci\": [0.786, 0.799], \"avg_logprob_logo_f1\": 0.7653, \"avg_logprob_ci\": [0.616, 0.82], \"avg_logprob_spearman\": 0.7876, \"ld_score_logo_f1\": 0.7212, \"ld_score_ci\": [0.588, 0.77], \"ld_score_spearman\": 0.7943, \"ld_score_pre_fix\": 0.6854, \"fast_detect_gpt_logo_f1\": 0.6269, \"fast_detect_gpt_ci\": [0.511, 0.762], \"fast_detect_gpt_spearman\": 0.4325, \"binoculars_logo_f1\": 0.579, \"binoculars_ci\": [0.405, 0.664], \"binoculars_spearman\": 0.1989, \"binoculars_bug_confirmed\": true, \"binoculars_bug_fix\": \"denominator changed from CE(performer, obs_argmax) to CE(performer, shifted_ids)\", \"bootstrap_n\": 1000, \"bootstrap_delta_7feat_vs_avglogprob\": {\"delta\": 0.039, \"p\": 0, \"significant\": true}, \"bootstrap_delta_7feat_vs_fdgpt\": {\"delta\": 0.067, \"p\": 0, \"significant\": true}, \"best_single_detector\": \"Avg-LogProb (0.7653)\", \"seven_feature_advantage_pp\": 3.3}, \"completed_at\": \"2026-05-15T00:26:12.709Z\"}, \"plan-004-prep\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-14T23:58:42.465Z\", \"updated_at\": \"2026-05-15T00:19:49.846Z\", \"hypothesis\": \"Downstream utility 准备：depth-stratified 数据集 + OLMo-1B fine-tuning 脚本（不开跑，等 Director 确认）\", \"conclusion\": \"success\", \"metrics\": {\"model\": \"OLMo-2-0425-1B (1485M)\", \"datasets\": {\"depth0_only\": {\"train\": 797, \"test\": 3138}, \"depth01\": {\"train\": 3951, \"test\": 3138}, \"all\": {\"train\": 12299, \"test\": 3138}, \"size_matched\": {\"train\": 3951, \"test\": 3138}, \"binary_filtered\": {\"train\": 3951, \"test\": 3138}}, \"dry_run_loss\": 2.18, \"script\": \"finetune_downstream.py\"}}, \"plan-003\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T23:58:40.949Z\", \"updated_at\": \"2026-05-15T00:09:28.999Z\", \"hypothesis\": \"跨家族参考模型伪证化：用 OLMo-2-1B 和 Qwen3-0.6B 作参考模型提取特征，验证 differential depth response 非 Pythia 特异\", \"conclusion\": \"success\", \"metrics\": {\"logo_f1_pythia_ref\": 0.8034, \"logo_f1_olmo_ref\": 0.8072, \"logo_f1_qwen_ref\": 0.8158, \"entropy_drift_all_refs_negative\": true, \"olmo_ref_drift_range\": [-0.608, -0.9089], \"qwen_ref_drift_range\": [-0.9557, -1.3458], \"pythia_ref_drift_range\": [-1.1872, -1.4017], \"dual_dynamics_is_pythia_artifact\": false}, \"spec\": {\"command\": \"python extract_features_crossref.py + cross_ref_analysis.py\", \"server\": \"autodl-5090\", \"data_path\": \"/root/gen-depth-fingerprint/data/features_all_models.csv\", \"data_count\": 23032, \"model_name\": \"OLMo-2-1B + Qwen3-0.6B as reference\", \"seed\": 42, \"checkpoint_path\": \"/root/gen-depth-fingerprint/data/cross_ref_results.json\", \"log_path\": \"/root/gen-depth-fingerprint/data/\"}, \"completed_at\": \"2026-05-15T00:09:28.999Z\"}, \"plan-013\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T23:33:25.590Z\", \"updated_at\": \"2026-05-14T23:53:38.901Z\", \"hypothesis\": \"文本长度混淆控制：深度特征的区分力是否独立于文本长度变化（长度归一化后趋势是否保持）\", \"conclusion\": \"success\", \"metrics\": {\"spearman_rho_range\": \"[-0.066, +0.134]\", \"length_depth_correlation\": \"weak (|ρ|<0.14)\", \"normalized_ttr_trend_preserved\": true, \"normalized_hapax_trend_preserved\": true, \"normalized_rho_stronger\": true, \"length_matched_f1_delta\": \"+0.041\", \"length_is_confound\": false, \"dropout_short_text_bias\": true}, \"spec\": {\"command\": \"python text_length_analysis.py\", \"server\": \"autodl-5090\", \"data_path\": \"/root/gen-depth-fingerprint/data/features_all_models.csv\", \"data_count\": 23032, \"model_name\": \"text length analysis\", \"seed\": 42, \"checkpoint_path\": \"/root/gen-depth-fingerprint/data/text_length_analysis.json\", \"log_path\": \"/root/gen-depth-fingerprint/data/text_length_boxplot.png\"}, \"completed_at\": \"2026-05-14T23:53:38.902Z\"}, \"plan-002\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T20:08:55.258Z\", \"updated_at\": \"2026-05-14T23:19:42.066Z\", \"hypothesis\": \"跨模型泛化：Pythia-410M 参考模型下的深度特征能否区分不同架构/规模生成器（Pythia-1B, OLMo-2-1B, Qwen3-1.7B, Qwen3-0.6B）的 continuation 链\", \"spec\": {\"command\": \"generate_chain.py --model-name {X} --model-path {path} --shard-id {0,1} --num-shards 2 --device cuda:0\", \"server\": \"autodl-5090\", \"data_path\": \"/root/gen-depth-fingerprint/data/wiki_seed_1000.jsonl\", \"data_count\": 1000, \"model_name\": \"pythia-1b, olmo-2-1b, qwen3-1.7b, qwen3-0.6b (+ pythia-2.8b from MVP)\", \"seed\": 42, \"temperature\": 0.7, \"top_p\": 0.9, \"max_new_tokens\": 256, \"reference_model\": \"EleutherAI/pythia-410m\", \"round1\": \"pythia-1b (cuda:0,1) + olmo-2-1b (cuda:2,3)\", \"round2\": \"qwen3-1.7b (cuda:0,1) + qwen3-0.6b (cuda:2,3)\", \"checkpoint_path\": \"/root/gen-depth-fingerprint/data/\", \"log_path\": \"/root/gen-depth-fingerprint/data/\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-14T23:19:36.270Z\", \"metrics\": {\"total_records\": 18423, \"models\": 4, \"pythia_1b\": {\"records\": 4555, \"seeds\": 995, \"file\": \"data/pythia-1b/generations.jsonl\"}, \"olmo_2_1b\": {\"records\": 4713, \"seeds\": 995, \"file\": \"data/olmo-2-1b/generations.jsonl\"}, \"qwen3_0_6b\": {\"records\": 4538, \"seeds\": 996, \"depth_dist\": {\"gen0\": 996, \"gen1\": 986, \"gen2\": 938, \"gen3\": 840, \"gen4\": 778}, \"file\": \"data/qwen3-0.6b/generations.jsonl\"}, \"qwen3_1_7b\": {\"records\": 4617, \"seeds\": 996, \"depth_dist\": {\"gen0\": 996, \"gen1\": 983, \"gen2\": 941, \"gen3\": 875, \"gen4\": 822}, \"file\": \"data/qwen3-1.7b/generations.jsonl\"}}}, \"plan-001\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T18:25:29.824Z\", \"updated_at\": \"2026-05-14T19:34:17.597Z\", \"hypothesis\": \"Feature ablation: 模型级特征（entropy系列+tail_decay）独立于表面特征仍能区分生成深度；H1/H2趋势分析确认特征随depth的变化模式；perplexity随depth显著变化\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/gen-depth-fingerprint && python ablation_analysis.py --parts A B C --device cuda:0\\\"\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:0\"], \"pid\": \"98324\", \"log_path\": \"/tmp/plan-001-fix.log\", \"submitted_at\": \"2026-05-14T18:25:56.326Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_path\": \"/root/gen-depth-fingerprint/results/ablation_results.json\", \"wall_clock_seconds\": 1685.0, \"gpu_hours\": 0.47}, \"reproduce\": {\"finished_at\": \"2026-05-14T18:51:40.563Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T18:51:41.308501+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"note\": \"initial_run_partial_issues_fixed_in_plan-001-fix\", \"ablation_full_macro_f1\": 0.82, \"ablation_surface_only_f1\": 0.76, \"ablation_reference_only_f1\": 0.72}, \"completed_at\": \"2026-05-14T18:54:01.340Z\"}, \"mvp-001\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T16:17:16.218Z\", \"updated_at\": \"2026-05-14T18:08:20.940Z\", \"hypothesis\": \"Pythia-410M 参考模型的分布特征（entropy stats, tail-decay, TTR, hapax）能区分 Pythia-2.8B continuation 链的 gen-0/gen-1/gen-2+，3-class macro-F1 ≥ 0.45\", \"spec\": {\"command\": \"python generate_chain.py --input data/wiki_seed_1000.jsonl --shard-id {0-3} --num-shards 4 --device cuda:0 (4 shards parallel)\", \"server\": \"autodl-5090\", \"data_path\": \"/root/gen-depth-fingerprint/data/wiki_seed_1000.jsonl\", \"data_count\": 1000, \"model_name\": \"EleutherAI/pythia-2.8b (FP16)\", \"seed\": 42, \"temperature\": 0.7, \"top_p\": 0.9, \"max_new_tokens\": 256, \"reference_model\": \"EleutherAI/pythia-410m\", \"script_path\": \"/root/gen-depth-fingerprint/generate_chain.py\", \"generation_type\": \"continuation\", \"depths\": \"gen-0 to gen-4\", \"checkpoint_path\": \"/root/gen-depth-fingerprint/results/mvp_results.json\", \"log_path\": \"/root/gen-depth-fingerprint/data/features.csv\"}, \"conclusion\": \"success\", \"metrics\": {\"macro_f1\": 0.8408, \"binary_f1_gen0_vs_gen2plus\": 0.8653, \"cv_macro_f1\": 0.806, \"cv_std\": 0.013, \"gen0_f1\": 0.9517, \"gen1_f1\": 0.7759, \"gen2plus_f1\": 0.7947, \"total_records\": 4609, \"seeds_used\": 995, \"skipped\": 173}, \"completed_at\": \"2026-05-14T18:08:20.940Z\"}}, \"count\": 42, \"total\": 42, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.1694}}"
    }
  },
  "sourceToolAssistantUUID": "5277fa8f-57e9-4f6f-bc5a-fb56e8b4b07a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "1d18d25d-25e1-4c57-94d9-a15ab4822c5c",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-20T05:01:12.205Z_

<details open><summary>🔧 Tool call — Glob · `toolu_019FyrqNvuq5MpVidmrQ4fJc`</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e4ef5f99-1ef2-41fc-9113-b0c7ebaf4131",
  "isSidechain": false,
  "requestId": "req_011CbDETNHwb4DTpgPMzGich",
  "type": "assistant",
  "uuid": "0169e1b0-533a-45f3-a510-5f024e24c9ad",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "1d18d25d-25e1-4c57-94d9-a15ab4822c5c",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PF1w5x34vkDMWGNgnmu5Gf",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 511,
      "cache_read_input_tokens": 24958,
      "output_tokens": 213,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 511,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 213,
          "cache_read_input_tokens": 24958,
          "cache_creation_input_tokens": 511,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 511
          },
          "type": "message"
        }
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

_source line 15 · 2026-05-20T05:01:12.223Z_

<details><summary>↩ Tool result · `toolu_019FyrqNvuq5MpVidmrQ4fJc`</summary>

```text
artifacts/_project/paper/table2.tex
artifacts/_project/paper/table1.tex
artifacts/_project/paper/table4.tex
artifacts/_project/paper/appendix_qlora.tex
artifacts/_project/paper/appendix_lofo.tex
artifacts/_project/paper/appendix_length.tex
artifacts/_project/paper/appendix_qualitative_examples.tex
artifacts/_project/paper/ethics.tex
artifacts/_project/paper/appendix_prompt_type.tex
artifacts/_project/paper/appendix_human_edit.tex
artifacts/_project/paper/appendix_error_analysis.tex
artifacts/_project/paper/appendix_domain.tex
artifacts/_project/paper/appendix_downstream.tex
artifacts/_project/paper/appendix_generator_subsets.tex
artifacts/_project/paper/appendix_tost.tex
artifacts/_project/paper/appendix_confusion_matrix.tex
artifacts/_project/paper/appendix_classifier.tex
artifacts/_project/paper/appendix_feature_distributions.tex
artifacts/_project/paper/appendix_cross_temp.tex
artifacts/_project/paper/appendix_ddr_validation.tex
artifacts/_project/paper/appendix_dataset_stats.tex
artifacts/_project/paper/appendix_finer_depth.tex
artifacts/_project/paper/appendix_transfer.tex
artifacts/_project/paper/appendix_temperature_stability.tex
artifacts/_project/paper/appendix_seed_control.tex
artifacts/_project/paper/appendix_instruct.tex
artifacts/_project/paper/discussion.tex
artifacts/_project/paper/appendix_ablation.tex
artifacts/_project/paper/appendix_feature_correlation.tex
artifacts/_project/paper/appendix_convergence.tex
artifacts/_project/paper/related_work.tex
artifacts/_project/paper/abstract.tex
artifacts/_project/paper/introduction.tex
artifacts/_project/paper/conclusion.tex
artifacts/_project/paper/main.tex
artifacts/_project/paper/limitations.tex
artifacts/_project/paper/results.tex
artifacts/_project/paper/appendix_cross_model_detail.tex
artifacts/_project/paper/method.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0169e1b0-533a-45f3-a510-5f024e24c9ad",
  "isSidechain": false,
  "promptId": "6504b37e-e710-425c-85a9-649cd3090508",
  "type": "user",
  "uuid": "f586d6ca-057b-41e1-b742-b7297b14e981",
  "toolUseResult": {
    "filenames": [
      "artifacts/_project/paper/table2.tex",
      "artifacts/_project/paper/table1.tex",
      "artifacts/_project/paper/table4.tex",
      "artifacts/_project/paper/appendix_qlora.tex",
      "artifacts/_project/paper/appendix_lofo.tex",
      "artifacts/_project/paper/appendix_length.tex",
      "artifacts/_project/paper/appendix_qualitative_examples.tex",
      "artifacts/_project/paper/ethics.tex",
      "artifacts/_project/paper/appendix_prompt_type.tex",
      "artifacts/_project/paper/appendix_human_edit.tex",
      "artifacts/_project/paper/appendix_error_analysis.tex",
      "artifacts/_project/paper/appendix_domain.tex",
      "artifacts/_project/paper/appendix_downstream.tex",
      "artifacts/_project/paper/appendix_generator_subsets.tex",
      "artifacts/_project/paper/appendix_tost.tex",
      "artifacts/_project/paper/appendix_confusion_matrix.tex",
      "artifacts/_project/paper/appendix_classifier.tex",
      "artifacts/_project/paper/appendix_feature_distributions.tex",
      "artifacts/_project/paper/appendix_cross_temp.tex",
      "artifacts/_project/paper/appendix_ddr_validation.tex",
      "artifacts/_project/paper/appendix_dataset_stats.tex",
      "artifacts/_project/paper/appendix_finer_depth.tex",
      "artifacts/_project/paper/appendix_transfer.tex",
      "artifacts/_project/paper/appendix_temperature_stability.tex",
      "artifacts/_project/paper/appendix_seed_control.tex",
      "artifacts/_project/paper/appendix_instruct.tex",
      "artifacts/_project/paper/discussion.tex",
      "artifacts/_project/paper/appendix_ablation.tex",
      "artifacts/_project/paper/appendix_feature_correlation.tex",
      "artifacts/_project/paper/appendix_convergence.tex",
      "artifacts/_project/paper/related_work.tex",
      "artifacts/_project/paper/abstract.tex",
      "artifacts/_project/paper/introduction.tex",
      "artifacts/_project/paper/conclusion.tex",
      "artifacts/_project/paper/main.tex",
      "artifacts/_project/paper/limitations.tex",
      "artifacts/_project/paper/results.tex",
      "artifacts/_project/paper/appendix_cross_model_detail.tex",
      "artifacts/_project/paper/method.tex"
    ],
    "durationMs": 13,
    "numFiles": 39,
    "truncated": false
  },
  "sourceToolAssistantUUID": "0169e1b0-533a-45f3-a510-5f024e24c9ad",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "1d18d25d-25e1-4c57-94d9-a15ab4822c5c",
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
  "leafUuid": "f586d6ca-057b-41e1-b742-b7297b14e981",
  "sessionId": "1d18d25d-25e1-4c57-94d9-a15ab4822c5c"
}
```

---

### Runtime record

_source line 17_

```json
{
  "type": "ai-title",
  "aiTitle": "Audit unreferenced successful experiments in paper",
  "sessionId": "1d18d25d-25e1-4c57-94d9-a15ab4822c5c"
}
```

---

### Assistant

_source line 18 · 2026-05-20T05:01:15.244Z_

<details><summary>Logged reasoning block</summary>

```text
The registry output is large - I need to read it in chunks. Let me also read all the tex files. I'll start reading the registry data and the tex files in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f586d6ca-057b-41e1-b742-b7297b14e981",
  "isSidechain": false,
  "requestId": "req_011CbDETcyjSZy5vbzdYzPdV",
  "type": "assistant",
  "uuid": "27a76de4-33a1-445f-8116-fa3f14fd95c3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "1d18d25d-25e1-4c57-94d9-a15ab4822c5c",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Q8eK9Mrp2LyNZxtJfwxrng",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1163,
      "cache_read_input_tokens": 25469,
      "output_tokens": 969,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1163,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 969,
          "cache_read_input_tokens": 25469,
          "cache_creation_input_tokens": 1163,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1163
          },
          "type": "message"
        }
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

_source line 19 · 2026-05-20T05:01:16.222Z_

Registry 数据量大，需要分块读取。让我并行处理：读取 registry 数据和所有 tex 文件。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "27a76de4-33a1-445f-8116-fa3f14fd95c3",
  "isSidechain": false,
  "requestId": "req_011CbDETcyjSZy5vbzdYzPdV",
  "type": "assistant",
  "uuid": "73865ad3-b906-4870-8114-4c39806eefde",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "1d18d25d-25e1-4c57-94d9-a15ab4822c5c",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Q8eK9Mrp2LyNZxtJfwxrng",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1163,
      "cache_read_input_tokens": 25469,
      "output_tokens": 969,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1163,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 969,
          "cache_read_input_tokens": 25469,
          "cache_creation_input_tokens": 1163,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1163
          },
          "type": "message"
        }
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

_source line 20 · 2026-05-20T05:01:20.562Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01LEXH9vYx6E3Y9L6fRG8nLC`</summary>

```json
{
  "description": "Read registry data completely",
  "subagent_type": "general-purpose",
  "prompt": "Read the file at /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-3-projects-gen-depth-fingerprint/1d18d25d-25e1-4c57-94d9-a15ab4822c5c/tool-results/mcp-agent-ml-research-read_registry-1779253272038.txt in sequential chunks until you've read 100% of it.\n\nExtract ALL experiments with conclusion=success. For each, output a structured list with:\n- exp_id\n- name/title\n- hypothesis (brief)\n- key metrics (numbers)\n- any tags or keywords that describe what the experiment tested\n\nOutput the complete list as a clean table or structured format. Do not skip any experiments. Count the total number of success experiments at the end."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "73865ad3-b906-4870-8114-4c39806eefde",
  "isSidechain": false,
  "requestId": "req_011CbDETcyjSZy5vbzdYzPdV",
  "type": "assistant",
  "uuid": "5c6c5ac1-ee0a-4019-ae03-b7eeeac275d3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "1d18d25d-25e1-4c57-94d9-a15ab4822c5c",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Q8eK9Mrp2LyNZxtJfwxrng",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1163,
      "cache_read_input_tokens": 25469,
      "output_tokens": 969,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1163,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 969,
          "cache_read_input_tokens": 25469,
          "cache_creation_input_tokens": 1163,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1163
          },
          "type": "message"
        }
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

_source line 21 · 2026-05-20T05:01:27.767Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01XBbFuokrzNjN3eJmBxsC5H`</summary>

```json
{
  "description": "Read all tex files content",
  "subagent_type": "general-purpose",
  "prompt": "Read ALL .tex files in /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/ and extract all experiment-related content: exp IDs, metric numbers (F1 scores, accuracy values, p-values), experiment description keywords (like \"cross-model\", \"temperature\", \"prompt type\", \"human edit\", \"domain\", \"LoRA\", \"QLoRA\", \"seed\", \"transfer\", \"convergence\", \"ablation\", etc.), table data, and figure references.\n\nHere is the full list of tex files to read:\n- table2.tex, table1.tex, table4.tex\n- appendix_qlora.tex, appendix_lofo.tex, appendix_length.tex, appendix_qualitative_examples.tex\n- ethics.tex, appendix_prompt_type.tex, appendix_human_edit.tex, appendix_error_analysis.tex\n- appendix_domain.tex, appendix_downstream.tex, appendix_generator_subsets.tex, appendix_tost.tex\n- appendix_confusion_matrix.tex, appendix_classifier.tex, appendix_feature_distributions.tex\n- appendix_cross_temp.tex, appendix_ddr_validation.tex, appendix_dataset_stats.tex\n- appendix_finer_depth.tex, appendix_transfer.tex, appendix_temperature_stability.tex\n- appendix_seed_control.tex, appendix_instruct.tex, discussion.tex, appendix_ablation.tex\n- appendix_feature_correlation.tex, appendix_convergence.tex, related_work.tex, abstract.tex\n- introduction.tex, conclusion.tex, main.tex, limitations.tex, results.tex\n- appendix_cross_model_detail.tex, method.tex\n\nFor each file, output:\n1. File name\n2. Any exp_id strings found (like \"eval-xxx\", \"plan-xxx\", etc.)\n3. Key metric numbers mentioned\n4. Experiment-descriptive keywords/phrases used\n5. What tables/figures are defined\n\nBe thorough - read every file completely. This is for cross-referencing which experiments are cited in the paper."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5c6c5ac1-ee0a-4019-ae03-b7eeeac275d3",
  "isSidechain": false,
  "requestId": "req_011CbDETcyjSZy5vbzdYzPdV",
  "type": "assistant",
  "uuid": "9b1fccd1-844c-4f64-acf7-ff6e7f406daf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "1d18d25d-25e1-4c57-94d9-a15ab4822c5c",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Q8eK9Mrp2LyNZxtJfwxrng",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1163,
      "cache_read_input_tokens": 25469,
      "output_tokens": 969,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1163,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 969,
          "cache_read_input_tokens": 25469,
          "cache_creation_input_tokens": 1163,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1163
          },
          "type": "message"
        }
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

_source line 22 · 2026-05-20T05:04:00.992Z_

<details><summary>↩ Tool result · `toolu_01LEXH9vYx6E3Y9L6fRG8nLC`</summary>

```text
Here is the complete list of all 42 experiments with `conclusion=success`:

---

## All Successful Experiments (42/42)

| # | exp_id | Title / What it tested | Hypothesis (brief) | Key Metrics | Tags |
|---|--------|----------------------|---------------------|-------------|------|
| 1 | **mvp-001** | MVP: Pythia-2.8B depth classification | Pythia-410M reference features can distinguish gen-0/gen-1/gen-2+ in Pythia-2.8B continuation chains (target: 3-class F1 >= 0.45) | macro_f1=0.8408, binary_f1=0.8653, cv_macro_f1=0.806 | baseline, depth-classification, pythia |
| 2 | **plan-001** | Feature ablation (initial) | Model-level features (entropy+tail_decay) independently distinguish depth; perplexity changes significantly with depth | ablation_full_f1=0.82, surface_only=0.76, reference_only=0.72 | ablation, feature-importance |
| 3 | **plan-001-fix** | Feature ablation (bugfix) | Reference-only features independently distinguish depth; bootstrap CIs don't overlap between reference and surface features | full_f1=0.8204, reference_only=0.7187, surface_only=0.7628, median_ppl_by_depth: 13.50/4.96/3.00/2.07/1.72 | ablation, bootstrap-CI, dual-signal |
| 4 | **plan-002** | Cross-model generalization (data generation) | Depth features from Pythia-410M generalize across architectures (Pythia-1B, OLMo-2-1B, Qwen3-1.7B, Qwen3-0.6B) | total_records=18423, models=4 | cross-generator, data-generation |
| 5 | **plan-002-pythia1b-s0** | Pythia-1B shard0 generation | Same-family larger model shows similar depth dynamics as Pythia-2.8B | records=2286, seeds=497 | data-generation, pythia, scaling |
| 6 | **plan-002-pythia1b-s1** | Pythia-1B shard1 generation | Complete seed coverage for Pythia-1B | records=2269, seeds=498 | data-generation, pythia |
| 7 | **plan-002-olmo2-s0** | OLMo-2-1B shard0 generation | Non-Pythia architecture shows depth signal, verifying universality across training data and architecture | records=2379, seeds=497 | data-generation, olmo, cross-architecture |
| 8 | **plan-002-olmo2-s1** | OLMo-2-1B shard1 generation | Complete seed coverage for OLMo-2-1B | records=2334, seeds=498 | data-generation, olmo |
| 9 | **plan-002-qwen17b-r2-s0** | Qwen3-1.7B shard0 generation | Mid-size non-Pythia model produces detectable depth signal | records=2291, seeds=498 | data-generation, qwen |
| 10 | **plan-002-qwen17b-r2-s1** | Qwen3-1.7B shard1 generation | Complete seed coverage for Qwen3-1.7B | records=2326, seeds=498 | data-generation, qwen |
| 11 | **plan-002-qwen06b-r2-s0** | Qwen3-0.6B shard0 generation | Smallest model (0.6B) still exhibits depth signal despite limited capacity | records=2270, seeds=498 | data-generation, qwen, small-model |
| 12 | **plan-002-qwen06b-r2-s1** | Qwen3-0.6B shard1 generation | Complete seed coverage for Qwen3-0.6B | records=2268, seeds=498 | data-generation, qwen |
| 13 | **plan-002-eval** | Cross-generator LOGO evaluation | Leave-one-generator-out generalization across unseen generators | logo_avg_f1=0.8037, best=pythia-1b(0.8507), worst=olmo-2-1b(0.7519), family_out_delta=0.0107 | cross-generator, LOGO, evaluation |
| 14 | **plan-003** | Cross-family reference model falsification | DDR is not Pythia-specific: OLMo-2-1B and Qwen3-0.6B as reference models yield similar F1 | logo_f1_pythia=0.8034, logo_f1_olmo=0.8072, logo_f1_qwen=0.8158 | cross-reference, falsification |
| 15 | **plan-003-olmo2ref** | OLMo-2-1B as reference model | Depth signal persists with OLMo reference, proving reference-model independence | (feature extraction completed) | cross-reference, olmo |
| 16 | **plan-003-qwen06bref** | Qwen3-0.6B as reference model | Depth signal persists with Qwen reference, no family-matching needed | (feature extraction completed) | cross-reference, qwen |
| 17 | **plan-004-prep** | Downstream utility preparation | Depth-stratified dataset + OLMo-1B fine-tuning script prepared | model=OLMo-2-0425-1B, dry_run_loss=2.18 | downstream, preparation |
| 18 | **plan-005** | Prompt type comparison (aggregate) | Depth signal exists across continuation/elaboration/rewriting prompt types | cv_f1: continuation=0.7806, rewriting=0.7368, elaboration=0.73; LOPTO avg=0.7525; retention: cont=83.1%, rewrite=93.9%, elab=98.6% | prompt-type, cross-prompt |
| 19 | **plan-005-cont** | Continuation chain generation | Recursive continuation shows stable entropy/lexical drift at 1000-seed scale | records=4620, seeds=995, retention_d4/d0=83.1% | data-generation, continuation |
| 20 | **plan-005-elab** | Elaboration chain generation | Elaboration chains decay slower due to stronger semantic anchoring | records=4946, seeds=995, retention=98.6%, lopto_f1=0.7622 | data-generation, elaboration |
| 21 | **plan-005-rewrite** | Inspired rewriting chain generation | Rewriting preserves topic but changes expression; retention between continuation and elaboration | records=4827, seeds=995, retention=93.9% | data-generation, rewriting |
| 22 | **plan-008-seed-stratification** | Seed complexity independence | Depth fingerprint discrimination independent of seed text lexical complexity (TTR terciles) | low/med/high binary F1: 0.685/0.695/0.695; max_diff_binary=1.06pp | robustness, seed-complexity |
| 23 | **plan-010-robustness** | Human edit robustness (random word replacement) | Depth fingerprint degrades gracefully under 5-20% random word replacement | baseline=0.695, 5%=0.65(-4.6pp), 10%=0.614(-8.1pp), 20%=0.591(-10.4pp) | robustness, human-edit |
| 24 | **plan-010-llm-rephrase** | LLM-simulated editing robustness | Qwen3-0.6B rephrasing causes less degradation than random replacement | original_binary=0.6918, rephrased_binary=0.6471, drop=-4.5pp, edit_distance_ratio=0.507 | robustness, llm-rephrase |
| 25 | **plan-013** | Text length confound control | Depth features independent of text length variation; length-normalized trends preserved | length_depth_corr: weak (|rho|<0.14), length_matched_f1_delta=+0.041, length_is_confound=False | confound-control, length |
| 26 | **plan-014** | Large model scale generalization (Qwen3-8B) | 8B-parameter model shows same entropy convergence and lexical drift | records=4497, seeds=995, logo_6gen_avg_f1=0.7893, qwen8b_held_out_f1=0.6832 | scaling, large-model, qwen |
| 27 | **plan-015** | Ordinal baseline (existing detectors) | FastDetectGPT/LD-Score/Binoculars continuous scores as ordinal depth signals | 7-feature=0.798, avg_logprob=0.7653, ld_score=0.7212, fastdetectgpt=0.6269, binoculars=0.579 | baseline-comparison, detectors |
| 28 | **plan-015-v2** | Ordinal baseline bugfix + bootstrap CI | 7-feature ensemble significantly outperforms all single detectors after Binoculars bug fix | 7-feature=0.798, avg_logprob=0.7653, delta_vs_avglogprob=+3.9pp(p=0), delta_vs_fdgpt=+6.7pp(p=0) | baseline-comparison, bootstrap, bugfix |
| 29 | **review-exp-b-topic-drift** | Topic drift vs. depth signal disentanglement | Semantic drift correlates weakly with depth (|rho|<0.3) while entropy/lexical features correlate strongly (|rho|>0.5) | semantic_sim 0->1: 0.622, 3->4: 0.859; entropy_mean_rho=-0.286 | confound-control, topic-drift |
| 30 | **review-exp-c-overall-ci** | Overall LOGO bootstrap CI + feature Spearman | 6-generator LOGO CI is narrow and above chance; per-feature Spearman validates monotonic depth contributions | overall_logo_f1=0.7879, CI=[0.783,0.793], spearman_hapax=-0.647, spearman_ttr=-0.630 | statistical-validation, bootstrap-CI |
| 31 | **multi-domain-seeds** | Domain independence (t=1.0) | DDR generalizes to News/Academic/Code; gap vs Wikipedia <10pp | news=0.746, academic=0.739, code=0.754, wiki_baseline=0.815, max_gap=7.62pp | domain-generalization, robustness |
| 32 | **exp_047_multi_domain_t07** | Domain independence (t=0.7) | Same domain generalization under standard decoding (t=0.7), eliminating temperature confound | news=0.712, academic=0.628, code=0.687, overall=0.676 | domain-generalization, temperature |
| 33 | **exp_048_cross_temp_transfer** | Cross-temperature transfer | Classifier trained at one temperature maintains discrimination at another; asymmetric transfer observed | qwen_only: within_0.7_binary=0.926, cross_0.7to1.0=0.757, within_1.0=0.825, cross_1.0to0.7=0.944 | temperature-robustness, transfer |
| 34 | **exp_049_temp_curve_t05** | Temperature curve (t=0.5) | DDR signal at t=0.5 stronger than t=0.7 (less randomness preserves distributional structure) | within_cv_binary_f1=0.8432, logo_binary_f1=0.8136, entropy_mean_rho=-0.584 | temperature, sampling-ablation |
| 35 | **exp_051_independent_seed** | Independent seed control | Non-overlapping seeds achieve comparable F1 to shared-seed LOGO, ruling out topic leakage | avg_binary_f1=0.6803, shared_seed_ref=0.694, delta=-1.4pp | confound-control, seed-leakage |
| 36 | **exp_052_instruct_qwen3_1_7b** | Instruct-tuning impact (Qwen3-1.7B) | Instruct-tuned Qwen3-1.7B shows degraded depth signal vs base; Spearman direction reversed | within_binary: instruct=0.875, base=0.861; logo: instruct=0.658, base=0.821; direction=reversed | instruct-tuning, signal-degradation |
| 37 | **exp_053_instruct_olmo2_1b** | Instruct-tuning impact (OLMo-2-1B) | OLMo-2 instruct shows degraded depth signal; 6/7 features reversed direction | within_binary: instruct=0.813, base=0.845; gen1_f1: instruct=0.256, base=0.523; features_reversed=6/7 | instruct-tuning, signal-degradation |
| 38 | **exp_054_instruct_llama3_2_3b** | Instruct-tuning impact (Llama-3.2-3B) | Llama-3.2-3B-Instruct shows degraded 3-class depth signal and feature direction reversals | instruct_binary=0.838, instruct_3class=0.544; base_binary=0.849, base_3class=0.742; 3 features reversed | instruct-tuning, llama |
| 39 | **exp_055_qlora_olmo_instruct** | QLoRA on OLMo instruct data | QLoRA end-to-end classifier partially recovers depth signal on instruct data | macro_f1_3class=0.888, binary_f1=0.836, n_samples=4429 | qlora, instruct, end-to-end |
| 40 | **exp_055b_qlora_olmo_base** | QLoRA on OLMo base data (control) | Per-model QLoRA baseline for instruct comparison | macro_f1_3class=0.859, binary_f1=0.793, n_samples=2379 | qlora, base-model, control |
| 41 | **exp_056_qlora_qwen_instruct** | QLoRA on Qwen instruct data | QLoRA recovers depth signal on instruct data, F1 comparable to base | macro_f1_3class=0.907, binary_f1=0.867, n_samples=4963 | qlora, instruct, end-to-end |
| 42 | **exp_056b_qlora_qwen_base** | QLoRA on Qwen base data (control) | Per-model QLoRA baseline for instruct comparison | macro_f1_3class=0.904, binary_f1=0.860, n_samples=2291 | qlora, base-model, control |

---

**Total experiments in registry: 42**
**Total with conclusion=success: 42** (100% success rate)

The experiments cluster into these categories:
- **Data generation** (12 exps): Shard-level generation for Pythia-1B, OLMo-2-1B, Qwen3-0.6B/1.7B/8B, and prompt-type variants
- **Core evaluation** (4 exps): MVP, cross-generator LOGO, feature ablation
- **Cross-reference model** (3 exps): Verifying DDR is not Pythia-reference-specific
- **Robustness / confound controls** (8 exps): Seed complexity, text length, topic drift, human edit, LLM rephrase, independent seed
- **Domain generalization** (2 exps): News/Academic/Code at t=0.7 and t=1.0
- **Temperature / sampling** (3 exps): t=0.5 curve, cross-temperature transfer
- **Prompt type** (4 exps): Continuation vs elaboration vs rewriting
- **Instruct-tuning impact** (3 exps): Qwen3, OLMo-2, Llama-3.2
- **QLoRA end-to-end** (4 exps): Instruct/base paired comparisons for Qwen and OLMo
- **Baseline comparison** (2 exps): Existing detectors as ordinal baselines
- **Statistical validation** (1 exp): Overall bootstrap CI
- **Downstream prep** (1 exp): Fine-tuning script preparation

agentId: a78362b8c21c4112f (use SendMessage with to: 'a78362b8c21c4112f' to continue this agent)
&lt;usage>total_tokens: 60194
tool_uses: 20
duration_ms: 160426&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5c6c5ac1-ee0a-4019-ae03-b7eeeac275d3",
  "isSidechain": false,
  "promptId": "6504b37e-e710-425c-85a9-649cd3090508",
  "type": "user",
  "uuid": "8221be68-af49-4e6e-9fe0-84520254fcc8",
  "toolUseResult": {
    "status": "completed",
    "prompt": "Read the file at /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-3-projects-gen-depth-fingerprint/1d18d25d-25e1-4c57-94d9-a15ab4822c5c/tool-results/mcp-agent-ml-research-read_registry-1779253272038.txt in sequential chunks until you've read 100% of it.\n\nExtract ALL experiments with conclusion=success. For each, output a structured list with:\n- exp_id\n- name/title\n- hypothesis (brief)\n- key metrics (numbers)\n- any tags or keywords that describe what the experiment tested\n\nOutput the complete list as a clean table or structured format. Do not skip any experiments. Count the total number of success experiments at the end.",
    "agentId": "a78362b8c21c4112f",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Here is the complete list of all 42 experiments with `conclusion=success`:\n\n---\n\n## All Successful Experiments (42/42)\n\n| # | exp_id | Title / What it tested | Hypothesis (brief) | Key Metrics | Tags |\n|---|--------|----------------------|---------------------|-------------|------|\n| 1 | **mvp-001** | MVP: Pythia-2.8B depth classification | Pythia-410M reference features can distinguish gen-0/gen-1/gen-2+ in Pythia-2.8B continuation chains (target: 3-class F1 >= 0.45) | macro_f1=0.8408, binary_f1=0.8653, cv_macro_f1=0.806 | baseline, depth-classification, pythia |\n| 2 | **plan-001** | Feature ablation (initial) | Model-level features (entropy+tail_decay) independently distinguish depth; perplexity changes significantly with depth | ablation_full_f1=0.82, surface_only=0.76, reference_only=0.72 | ablation, feature-importance |\n| 3 | **plan-001-fix** | Feature ablation (bugfix) | Reference-only features independently distinguish depth; bootstrap CIs don't overlap between reference and surface features | full_f1=0.8204, reference_only=0.7187, surface_only=0.7628, median_ppl_by_depth: 13.50/4.96/3.00/2.07/1.72 | ablation, bootstrap-CI, dual-signal |\n| 4 | **plan-002** | Cross-model generalization (data generation) | Depth features from Pythia-410M generalize across architectures (Pythia-1B, OLMo-2-1B, Qwen3-1.7B, Qwen3-0.6B) | total_records=18423, models=4 | cross-generator, data-generation |\n| 5 | **plan-002-pythia1b-s0** | Pythia-1B shard0 generation | Same-family larger model shows similar depth dynamics as Pythia-2.8B | records=2286, seeds=497 | data-generation, pythia, scaling |\n| 6 | **plan-002-pythia1b-s1** | Pythia-1B shard1 generation | Complete seed coverage for Pythia-1B | records=2269, seeds=498 | data-generation, pythia |\n| 7 | **plan-002-olmo2-s0** | OLMo-2-1B shard0 generation | Non-Pythia architecture shows depth signal, verifying universality across training data and architecture | records=2379, seeds=497 | data-generation, olmo, cross-architecture |\n| 8 | **plan-002-olmo2-s1** | OLMo-2-1B shard1 generation | Complete seed coverage for OLMo-2-1B | records=2334, seeds=498 | data-generation, olmo |\n| 9 | **plan-002-qwen17b-r2-s0** | Qwen3-1.7B shard0 generation | Mid-size non-Pythia model produces detectable depth signal | records=2291, seeds=498 | data-generation, qwen |\n| 10 | **plan-002-qwen17b-r2-s1** | Qwen3-1.7B shard1 generation | Complete seed coverage for Qwen3-1.7B | records=2326, seeds=498 | data-generation, qwen |\n| 11 | **plan-002-qwen06b-r2-s0** | Qwen3-0.6B shard0 generation | Smallest model (0.6B) still exhibits depth signal despite limited capacity | records=2270, seeds=498 | data-generation, qwen, small-model |\n| 12 | **plan-002-qwen06b-r2-s1** | Qwen3-0.6B shard1 generation | Complete seed coverage for Qwen3-0.6B | records=2268, seeds=498 | data-generation, qwen |\n| 13 | **plan-002-eval** | Cross-generator LOGO evaluation | Leave-one-generator-out generalization across unseen generators | logo_avg_f1=0.8037, best=pythia-1b(0.8507), worst=olmo-2-1b(0.7519), family_out_delta=0.0107 | cross-generator, LOGO, evaluation |\n| 14 | **plan-003** | Cross-family reference model falsification | DDR is not Pythia-specific: OLMo-2-1B and Qwen3-0.6B as reference models yield similar F1 | logo_f1_pythia=0.8034, logo_f1_olmo=0.8072, logo_f1_qwen=0.8158 | cross-reference, falsification |\n| 15 | **plan-003-olmo2ref** | OLMo-2-1B as reference model | Depth signal persists with OLMo reference, proving reference-model independence | (feature extraction completed) | cross-reference, olmo |\n| 16 | **plan-003-qwen06bref** | Qwen3-0.6B as reference model | Depth signal persists with Qwen reference, no family-matching needed | (feature extraction completed) | cross-reference, qwen |\n| 17 | **plan-004-prep** | Downstream utility preparation | Depth-stratified dataset + OLMo-1B fine-tuning script prepared | model=OLMo-2-0425-1B, dry_run_loss=2.18 | downstream, preparation |\n| 18 | **plan-005** | Prompt type comparison (aggregate) | Depth signal exists across continuation/elaboration/rewriting prompt types | cv_f1: continuation=0.7806, rewriting=0.7368, elaboration=0.73; LOPTO avg=0.7525; retention: cont=83.1%, rewrite=93.9%, elab=98.6% | prompt-type, cross-prompt |\n| 19 | **plan-005-cont** | Continuation chain generation | Recursive continuation shows stable entropy/lexical drift at 1000-seed scale | records=4620, seeds=995, retention_d4/d0=83.1% | data-generation, continuation |\n| 20 | **plan-005-elab** | Elaboration chain generation | Elaboration chains decay slower due to stronger semantic anchoring | records=4946, seeds=995, retention=98.6%, lopto_f1=0.7622 | data-generation, elaboration |\n| 21 | **plan-005-rewrite** | Inspired rewriting chain generation | Rewriting preserves topic but changes expression; retention between continuation and elaboration | records=4827, seeds=995, retention=93.9% | data-generation, rewriting |\n| 22 | **plan-008-seed-stratification** | Seed complexity independence | Depth fingerprint discrimination independent of seed text lexical complexity (TTR terciles) | low/med/high binary F1: 0.685/0.695/0.695; max_diff_binary=1.06pp | robustness, seed-complexity |\n| 23 | **plan-010-robustness** | Human edit robustness (random word replacement) | Depth fingerprint degrades gracefully under 5-20% random word replacement | baseline=0.695, 5%=0.65(-4.6pp), 10%=0.614(-8.1pp), 20%=0.591(-10.4pp) | robustness, human-edit |\n| 24 | **plan-010-llm-rephrase** | LLM-simulated editing robustness | Qwen3-0.6B rephrasing causes less degradation than random replacement | original_binary=0.6918, rephrased_binary=0.6471, drop=-4.5pp, edit_distance_ratio=0.507 | robustness, llm-rephrase |\n| 25 | **plan-013** | Text length confound control | Depth features independent of text length variation; length-normalized trends preserved | length_depth_corr: weak (|rho|<0.14), length_matched_f1_delta=+0.041, length_is_confound=False | confound-control, length |\n| 26 | **plan-014** | Large model scale generalization (Qwen3-8B) | 8B-parameter model shows same entropy convergence and lexical drift | records=4497, seeds=995, logo_6gen_avg_f1=0.7893, qwen8b_held_out_f1=0.6832 | scaling, large-model, qwen |\n| 27 | **plan-015** | Ordinal baseline (existing detectors) | FastDetectGPT/LD-Score/Binoculars continuous scores as ordinal depth signals | 7-feature=0.798, avg_logprob=0.7653, ld_score=0.7212, fastdetectgpt=0.6269, binoculars=0.579 | baseline-comparison, detectors |\n| 28 | **plan-015-v2** | Ordinal baseline bugfix + bootstrap CI | 7-feature ensemble significantly outperforms all single detectors after Binoculars bug fix | 7-feature=0.798, avg_logprob=0.7653, delta_vs_avglogprob=+3.9pp(p=0), delta_vs_fdgpt=+6.7pp(p=0) | baseline-comparison, bootstrap, bugfix |\n| 29 | **review-exp-b-topic-drift** | Topic drift vs. depth signal disentanglement | Semantic drift correlates weakly with depth (|rho|<0.3) while entropy/lexical features correlate strongly (|rho|>0.5) | semantic_sim 0->1: 0.622, 3->4: 0.859; entropy_mean_rho=-0.286 | confound-control, topic-drift |\n| 30 | **review-exp-c-overall-ci** | Overall LOGO bootstrap CI + feature Spearman | 6-generator LOGO CI is narrow and above chance; per-feature Spearman validates monotonic depth contributions | overall_logo_f1=0.7879, CI=[0.783,0.793], spearman_hapax=-0.647, spearman_ttr=-0.630 | statistical-validation, bootstrap-CI |\n| 31 | **multi-domain-seeds** | Domain independence (t=1.0) | DDR generalizes to News/Academic/Code; gap vs Wikipedia <10pp | news=0.746, academic=0.739, code=0.754, wiki_baseline=0.815, max_gap=7.62pp | domain-generalization, robustness |\n| 32 | **exp_047_multi_domain_t07** | Domain independence (t=0.7) | Same domain generalization under standard decoding (t=0.7), eliminating temperature confound | news=0.712, academic=0.628, code=0.687, overall=0.676 | domain-generalization, temperature |\n| 33 | **exp_048_cross_temp_transfer** | Cross-temperature transfer | Classifier trained at one temperature maintains discrimination at another; asymmetric transfer observed | qwen_only: within_0.7_binary=0.926, cross_0.7to1.0=0.757, within_1.0=0.825, cross_1.0to0.7=0.944 | temperature-robustness, transfer |\n| 34 | **exp_049_temp_curve_t05** | Temperature curve (t=0.5) | DDR signal at t=0.5 stronger than t=0.7 (less randomness preserves distributional structure) | within_cv_binary_f1=0.8432, logo_binary_f1=0.8136, entropy_mean_rho=-0.584 | temperature, sampling-ablation |\n| 35 | **exp_051_independent_seed** | Independent seed control | Non-overlapping seeds achieve comparable F1 to shared-seed LOGO, ruling out topic leakage | avg_binary_f1=0.6803, shared_seed_ref=0.694, delta=-1.4pp | confound-control, seed-leakage |\n| 36 | **exp_052_instruct_qwen3_1_7b** | Instruct-tuning impact (Qwen3-1.7B) | Instruct-tuned Qwen3-1.7B shows degraded depth signal vs base; Spearman direction reversed | within_binary: instruct=0.875, base=0.861; logo: instruct=0.658, base=0.821; direction=reversed | instruct-tuning, signal-degradation |\n| 37 | **exp_053_instruct_olmo2_1b** | Instruct-tuning impact (OLMo-2-1B) | OLMo-2 instruct shows degraded depth signal; 6/7 features reversed direction | within_binary: instruct=0.813, base=0.845; gen1_f1: instruct=0.256, base=0.523; features_reversed=6/7 | instruct-tuning, signal-degradation |\n| 38 | **exp_054_instruct_llama3_2_3b** | Instruct-tuning impact (Llama-3.2-3B) | Llama-3.2-3B-Instruct shows degraded 3-class depth signal and feature direction reversals | instruct_binary=0.838, instruct_3class=0.544; base_binary=0.849, base_3class=0.742; 3 features reversed | instruct-tuning, llama |\n| 39 | **exp_055_qlora_olmo_instruct** | QLoRA on OLMo instruct data | QLoRA end-to-end classifier partially recovers depth signal on instruct data | macro_f1_3class=0.888, binary_f1=0.836, n_samples=4429 | qlora, instruct, end-to-end |\n| 40 | **exp_055b_qlora_olmo_base** | QLoRA on OLMo base data (control) | Per-model QLoRA baseline for instruct comparison | macro_f1_3class=0.859, binary_f1=0.793, n_samples=2379 | qlora, base-model, control |\n| 41 | **exp_056_qlora_qwen_instruct** | QLoRA on Qwen instruct data | QLoRA recovers depth signal on instruct data, F1 comparable to base | macro_f1_3class=0.907, binary_f1=0.867, n_samples=4963 | qlora, instruct, end-to-end |\n| 42 | **exp_056b_qlora_qwen_base** | QLoRA on Qwen base data (control) | Per-model QLoRA baseline for instruct comparison | macro_f1_3class=0.904, binary_f1=0.860, n_samples=2291 | qlora, base-model, control |\n\n---\n\n**Total experiments in registry: 42**\n**Total with conclusion=success: 42** (100% success rate)\n\nThe experiments cluster into these categories:\n- **Data generation** (12 exps): Shard-level generation for Pythia-1B, OLMo-2-1B, Qwen3-0.6B/1.7B/8B, and prompt-type variants\n- **Core evaluation** (4 exps): MVP, cross-generator LOGO, feature ablation\n- **Cross-reference model** (3 exps): Verifying DDR is not Pythia-reference-specific\n- **Robustness / confound controls** (8 exps): Seed complexity, text length, topic drift, human edit, LLM rephrase, independent seed\n- **Domain generalization** (2 exps): News/Academic/Code at t=0.7 and t=1.0\n- **Temperature / sampling** (3 exps): t=0.5 curve, cross-temperature transfer\n- **Prompt type** (4 exps): Continuation vs elaboration vs rewriting\n- **Instruct-tuning impact** (3 exps): Qwen3, OLMo-2, Llama-3.2\n- **QLoRA end-to-end** (4 exps): Instruct/base paired comparisons for Qwen and OLMo\n- **Baseline comparison** (2 exps): Existing detectors as ordinal baselines\n- **Statistical validation** (1 exp): Overall bootstrap CI\n- **Downstream prep** (1 exp): Fine-tuning script preparation"
      }
    ],
    "totalDurationMs": 160426,
    "totalTokens": 60194,
    "totalToolUseCount": 20,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7616,
      "cache_read_input_tokens": 48384,
      "output_tokens": 4193,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 7616
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 4193,
          "cache_read_input_tokens": 48384,
          "cache_creation_input_tokens": 7616,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 7616,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 4,
      "searchCount": 0,
      "bashCount": 16,
      "editFileCount": 0,
      "linesAdded": 0,
      "linesRemoved": 0,
      "otherToolCount": 0
    }
  },
  "sourceToolAssistantUUID": "5c6c5ac1-ee0a-4019-ae03-b7eeeac275d3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "1d18d25d-25e1-4c57-94d9-a15ab4822c5c",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Runtime record

_source line 23_

```json
{
  "type": "last-prompt",
  "leafUuid": "8221be68-af49-4e6e-9fe0-84520254fcc8",
  "sessionId": "1d18d25d-25e1-4c57-94d9-a15ab4822c5c"
}
```

---

### Runtime record

_source line 24_

```json
{
  "type": "ai-title",
  "aiTitle": "Audit unreferenced successful experiments in paper",
  "sessionId": "1d18d25d-25e1-4c57-94d9-a15ab4822c5c"
}
```

---

### Tool result

_source line 25 · 2026-05-20T05:05:57.997Z_

<details><summary>↩ Tool result · `toolu_01XBbFuokrzNjN3eJmBxsC5H`</summary>

```text
Here is the complete extraction from all 41 .tex files:

---

## 1. `table1.tex`
- **Exp IDs**: None
- **Key metrics**: LOGO Macro-F1 per generator: Pythia-1B 0.806, Mistral-7B 0.681; Average 8-gen 0.762, 95% CI [0.758, 0.766]
- **Keywords**: leave-one-generator-out (LOGO), 3-class depth classification, held-out generator
- **Tables/Figures**: `\label{tab:logo-results}` (Table: LOGO results, 8-gen, 3-class). NOTE: this standalone file is NOT \input'd by main.tex; the inline table in results.tex is authoritative.

## 2. `table2.tex`
- **Exp IDs**: None
- **Key metrics**: Full 7-feature LOGO F1 = 0.773; Surface only (2 features) = 0.688; Reference only (5 features) = 0.713; McNemar p < 0.001 for both subsets. Permutation importance: hapax_ratio 0.269, entropy_mean 0.164, ttr 0.159
- **Keywords**: feature group ablation, complementarity, 8-gen 10-fold CV, permutation importance, surface features, reference features
- **Tables/Figures**: `\label{tab:feature-ablation}` (Table: feature group ablation)

## 3. `table4.tex`
- **Exp IDs**: None
- **Key metrics**: Pythia-410M LOGO F1 = 0.803, Ent. Drift [-1.19, -1.40]; OLMo-2-1B LOGO F1 = 0.807, Ent. Drift [-0.61, -0.91]; Qwen3-0.6B LOGO F1 = 0.816, Ent. Drift [-0.96, -1.35]; F1 spread = 0.013
- **Keywords**: cross-family reference model validation, 5-gen LOGO subset, entropy drift, reference model choice
- **Tables/Figures**: `\label{tab:cross-ref}` (Table: cross-family reference models)

## 4. `appendix_qlora.tex`
- **Exp IDs**: None
- **Key metrics**: XGBoost 5-class F1 = 0.501 +/- 0.038, 3-class F1 = 0.789; QLoRA 5-class F1 = 0.583 +/- 0.010, 3-class F1 = 0.905 +/- 0.003; Per-class F1 (5-class): 0.999/0.796/0.413/0.259/0.447; Hyperparameter robustness: rank 32 seed 123 yields 5-class 0.587 +/- 0.005, 3-class 0.905 +/- 0.004
- **Keywords**: QLoRA, end-to-end depth classification, Qwen3-0.6B-Base, LoRA rank 16, learning rate 2e-4, 3 epochs, 5-class sequence classification, hyperparameter robustness, LoRA rank 32, seed 123, token-level patterns
- **Tables/Figures**: `\label{tab:qlora}` (Table: QLoRA vs XGBoost)

## 5. `appendix_lofo.tex`
- **Exp IDs**: None
- **Key metrics**: Full 7-feature LOGO F1 = 0.789 (6-gen); entropy_max dropped: 0.774 (-1.50 pp); entropy_mean: 0.783 (-0.63 pp); ttr: 0.784 (-0.55 pp); hapax_ratio: 0.785 (-0.42 pp); tail_decay: 0.786 (-0.33 pp); entropy_std: 0.786 (-0.29 pp); entropy_min: 0.789 (+0.01 pp)
- **Keywords**: leave-one-feature-out (LOFO), ablation, permutation importance, feature redundancy, 6-gen LOGO
- **Tables/Figures**: `\label{tab:lofo}` (Table: LOFO ablation)

## 6. `appendix_length.tex`
- **Exp IDs**: None
- **Key metrics**: Spearman |rho| < 0.14 (length-depth); tail_decay |rho| = 0.38, hapax_ratio |rho| = 0.30, TTR |rho| = 0.29 (length-feature); entropy_mean |rho| = 0.09, entropy_std |rho| = 0.18; Length-matched binary F1 = 0.724 (down from 0.770, delta = -0.046); Random-subsample control F1 = 0.767; Length accounts for ~6% of discriminative performance
- **Keywords**: length confound, Spearman correlation, length-matched classification, random-subsample control, deconfounding, 8-gen LOGO
- **Tables/Figures**: None (inline results only)

## 7. `appendix_qualitative_examples.tex`
- **Exp IDs**: seed 120
- **Key metrics**: Feature values per depth: entropy_mean 2.720/2.206/0.780; TTR 0.659/0.272/0.081; hapax ratio 0.561/0.183/0.005; entropy_max 7.000/7.016/6.926; tail_decay -0.00227/-0.00231/-0.00223
- **Keywords**: qualitative examples, generation chain, Pythia-2.8B, continuation prompt, monotonic drift, near-stationary shape features, seed 120
- **Tables/Figures**: `\label{tab:qualitative-text}` (Table: example text chain), `\label{tab:qualitative-features}` (Table: feature values)

## 8. `ethics.tex`
- **Exp IDs**: None
- **Key metrics**: 62 GPU-hours total; 4x NVIDIA RTX 5090 GPUs (32 GB each)
- **Keywords**: ethics, Wikipedia seeds, CC BY-SA 3.0, Apache 2.0, Qwen License, Llama Community License, compute budget, Python 3.12.3, PyTorch 2.10.0, CUDA 12.8, Transformers 4.57.6, XGBoost 3.2.0, scikit-learn 1.8.0
- **Tables/Figures**: None

## 9. `appendix_prompt_type.tex`
- **Exp IDs**: None
- **Key metrics**: Within-prompt-type 5-fold CV F1: continuation 0.78, rewriting 0.74, elaboration 0.73; Cross-prompt-type (LOPTO) avg F1 = 0.753; Feature decay rates: continuation 16.9%/step, rewriting 6.1%, elaboration 1.4%
- **Keywords**: prompt type, continuation, elaboration, inspired rewriting, LOPTO (leave-one-prompt-type-out), cross-prompt transfer, Pythia-2.8B, 995 seeds, 5 depths
- **Tables/Figures**: None (inline results)

## 10. `appendix_human_edit.tex`
- **Exp IDs**: None
- **Key metrics**: 
  - Perturbation robustness: 0% binary F1=0.695 [0.680,0.710], 3-class=0.737; 5% binary=0.650, 3-class=0.641; 10% binary=0.614, 3-class=0.492; 20% binary=0.591, 3-class=0.367
  - Feature subset: Ent-only 0% bin=0.833, 7-feat bin=0.695; at 20%: ent-only=0.569, 7-feat=0.591 (crossover)
  - Baseline robustness: 7-feat 0.695, LD-Score 0.677, Avg-LogProb 0.682, FastDetectGPT 0.571, Binoculars 0.500
  - LLM-simulated regen: binary drops 0.692->0.647 (-4.5 pp), 3-class 0.739->0.667 (-7.1 pp)
  - Seed complexity: max F1 variation 1.1 pp across TTR terciles
- **Keywords**: human edit, random word replacement, perturbation robustness, 8-gen LOGO, binary gen-1 vs gen-2+, feature subset degradation, entropy-only subset, baseline robustness, LD-Score, FastDetectGPT, Binoculars, Avg-LogProb, LLM-simulated sentence regeneration, Qwen3-0.6B-Base, seed complexity
- **Tables/Figures**: `\label{tab:human-edit}`, `\label{tab:feature-degrade}`, `\label{tab:baseline-robustness}`

## 11. `appendix_error_analysis.tex`
- **Exp IDs**: None
- **Key metrics**: N=29,095, overall error rate 28.08%; 86.2% false negatives, 13.8% false positives; Depth-2 error 48.42%, depth-3 29.17%, depth-4 20.32%, depth-1 FP 7.11%; Per-generator: Mistral-7B 45.00%, Qwen3-8B 34.18%, Llama-3.2-3B 30.18%, OLMo-2-1B 28.35%, Pythia-2.8B 23.96%, Qwen3-1.7B 22.48%, Qwen3-0.6B 21.03%, Pythia-1B 18.20%; Mann-Whitney: entropy_mean p<1e-300, TTR p<1e-300, hapax_ratio p<1e-300; entropy_max p=0.584, tail_decay p=0.653; Misclassified gen-2+ TTR 0.464 vs 0.302 correct; entropy_mean 2.26 vs 1.57
- **Keywords**: error analysis, binary classification, false negatives, false positives, error asymmetry, per-depth error rates, per-generator error rates, Mann-Whitney U test, model scale effect
- **Tables/Figures**: `\label{tab:error-by-gen}`

## 12. `appendix_domain.tex`
- **Exp IDs**: None
- **Key metrics**: Code binary F1=0.754 [0.737,0.770], 3-class=0.634; News binary=0.746 [0.726,0.764], 3-class=0.652; Academic binary=0.739 [0.720,0.757], 3-class=0.622; Domain x temperature: News 0.746 vs 0.712 (t=1.0 vs 0.7), Academic 0.739 vs 0.628, Code 0.754 vs 0.687
- **Keywords**: cross-domain, News, Academic, Code documentation, Wikipedia, domain generalization, temperature interaction, 3 generators (Pythia-1B, Qwen3-1.7B, Mistral-7B), 200 seeds, t=1.0, top-p=1.0, reference model calibration, 3-class inversion, DDR evidence
- **Tables/Figures**: `\label{tab:domain}`

## 13. `appendix_downstream.tex`
- **Exp IDs**: None
- **Key metrics**: OLMo-2-0425-1B downstream PPL: All depths (12,299) 2.335+/-0.000; Size-matched random (3,951) 2.367+/-0.000; Depth 0-1 (3,951) 2.387+/-0.001; Binary-filtered (3,951) 2.389+/-0.000; Depth 0 only (797) 2.681+/-0.001; TOST p=1.1e-4 at +/-2% margin; Cohen's d: 86.0 (full vs random), 119.7 (full vs depth 0-1); Margin sensitivity: Full vs Random passes at +/-2% (p=1e-6), Full vs Depth 0-1 requires +/-3%
- **Keywords**: downstream, fine-tuning, perplexity, data curation, OLMo-2-0425-1B, depth-aware curation, TOST equivalence testing, null result, 3 seeds, size-matched, data quantity dominates, margin sensitivity
- **Tables/Figures**: `\label{tab:downstream}`, `\label{tab:tost-margins}`

## 14. `appendix_generator_subsets.tex`
- **Exp IDs**: None
- **Key metrics**: None (summary table only)
- **Keywords**: generator subsets, 8-gen main LOGO, 5-gen cross-model chains, 6-gen QLoRA, 4-gen temperature ablation, 1-gen prompt-type, 3-gen cross-domain, 3-gen instruct, 5-gen downstream, chronological expansion
- **Tables/Figures**: `\label{tab:gen-subsets}`

## 15. `appendix_tost.tex`
- **Exp IDs**: None
- **Key metrics**: Per-generator TOST (epsilon=|d|<0.20): entropy_min passes 8/8; entropy_max passes 6/8 (Pythia-1B |d|=0.21, Pythia-2.8B |d|=0.25); tail_decay passes 4/8; all drifting features 0/8; Per-generator |d| values: Pythia-2.8B entropy_mean=1.20, Pythia-1B=1.40, Qwen3-1.7B=1.12, etc.
- **Keywords**: TOST equivalence testing, per-generator, Cohen's d, epsilon=0.20, near-stationary, drifting, gen-1 vs gen-2+, alpha=0.05, DDR scatter
- **Tables/Figures**: `\label{tab:tost-per-gen}`, `\label{fig:ddr-scatter}` (fig_ddr_scatter.pdf)

## 16. `appendix_confusion_matrix.tex`
- **Exp IDs**: None
- **Key metrics**: N=27,529 (6-gen); gen-0 recall 99.4%; gen-1: 75.0% correct, 18.8% -> gen-2+, 6.2% -> gen-0; gen-2+: 73.7% correct, 23.3% -> gen-1, 3.0% -> gen-0
- **Keywords**: confusion matrix, 6-generator LOGO, 3-class, gen-0/gen-1/gen-2+, row-normalized, DDR predictions
- **Tables/Figures**: `\label{tab:confusion}`, `\label{fig:confusion-heatmap}` (fig_appendix_confusion.pdf)

## 17. `appendix_classifier.tex`
- **Exp IDs**: None
- **Key metrics**: 6-gen LOGO: XGBoost 0.789, Random Forest 0.790, Logistic Regression 0.725; Per-generator: Pythia-1B easiest (0.856/0.856/0.781), Qwen3-8B hardest (0.683/0.684/0.624); CORAL, Frank-Hall comparable with overlapping CIs; Temperature ablation (4-gen LOGO): Pythia-2.8B t=0.5 binary=0.814, t=0.7=0.740, t=0.9=0.480; OLMo t=0.5=0.783, t=0.7=0.695, t=0.9=0.453; Qwen3-1.7B t=0.5=0.751, t=0.7=0.751, t=0.9=0.566; Qwen3-0.6B t=0.5=0.711, t=0.7=0.691, t=0.9=0.598; rho(ent mean) ranges -0.72 to -0.26
- **Keywords**: classifier sensitivity, XGBoost, Random Forest, Logistic Regression, CORAL ordinal, Frank-Hall ordinal, sampling sensitivity, temperature ablation, t=0.5/0.7/0.9, nucleus p=0.9, per-generator performance, scale effect, OLMo-2-0425-1B (April 2025 release)
- **Tables/Figures**: `\label{tab:alt-classifier}`, `\label{tab:sampling-ablation}`, `\label{fig:per-gen}` (fig_appendix_per_gen.pdf)

## 18. `appendix_feature_distributions.tex`
- **Exp IDs**: None
- **Key metrics**: None (visualization appendix)
- **Keywords**: DDR trend lines, per-feature depth trends, Spearman rho, linear R^2, UMAP embedding, 7-feature space, N=7500, k=30, min_dist=0.3, StandardScaler, depth gradient, convergence
- **Tables/Figures**: `\label{fig:ddr-trends}` (fig_appendix_ddr_trends.pdf), `\label{fig:umap}` (fig_appendix_umap.pdf)

## 19. `appendix_cross_temp.tex`
- **Exp IDs**: None
- **Key metrics**: 6-gen LOGO cross-temperature: 0.7->0.7 3-class F1=0.789; 1.0->1.0=0.726; 1.0->0.7=0.791; 0.7->1.0=0.723 (-6.6 pp); Qwen3-1.7B drops to 0.418 under cross-temp; Binary: Qwen3-1.7B 0.948->0.713 (0.7->1.0), recovers 0.948 (1.0->0.7); Aggregate binary range 0.900-0.958
- **Keywords**: cross-temperature transfer, train/test temperature mismatch, Qwen3-1.7B, asymmetric transfer, generator-specific vulnerability, t=1.0, top-p=0.95
- **Tables/Figures**: `\label{fig:cross-temp}` (fig_appendix_cross_temp.pdf)

## 20. `appendix_ddr_validation.tex`
- **Exp IDs**: None
- **Key metrics**: 
  - k-means clustering: k=2 silhouette=0.632, k=3=0.499, k=4=0.571
  - TOST sensitivity: entropy_min passes 7/8 at eps=0.15, 8/8 at eps=0.20; tail_decay 4/8 at eps=0.20, 7/8 at eps=0.25; all drifting 0/8 at all eps
  - Holdout split validation: max delta|rho|=0.05, min gap between zones >0.15
  - Effect sizes: entropy_mean |d|=1.054, |Delta|=1.410, |delta|=0.587; TTR |d|=0.814, |Delta|=1.116, |delta|=0.510; hapax |d|=0.735, |Delta|=0.936, |delta|=0.528; ent_std |d|=0.457, |Delta|=0.605, |delta|=0.295; tail_decay |d|=0.087; ent_max |d|=0.062; ent_min |d|=0.016, Cliff's delta=0.354
  - Levene tests: p<1e-10, variance ratios 1.86-2.21
  - Minimum drifting-to-max-stationary gap: 9.5x under Glass's Delta
- **Keywords**: data-driven clustering, k-means, silhouette, TOST sensitivity, epsilon 0.15/0.20/0.25, holdout generator split validation, Split A, Split B, 4/4 partition, heteroscedasticity, Levene test, Glass's Delta, Cliff's delta, Cohen's d, DDR partition validation, gen-1 vs gen-2+ N=29,095
- **Tables/Figures**: `\label{tab:clustering}`, `\label{tab:tost-sensitivity}`, `\label{tab:holdout-split}`, `\label{fig:holdout-scatter}` (fig_ddr_holdout_split.pdf), `\label{tab:effect-sizes}`

## 21. `appendix_dataset_stats.tex`
- **Exp IDs**: None
- **Key metrics**: Total N=37,058; per-generator: Pythia-1B 4,555; Pythia-2.8B 4,609; OLMo-2-1B 4,713; Qwen3-0.6B 4,538; Qwen3-1.7B 4,617; Qwen3-8B 4,497; Llama-3.2-3B 4,680; Mistral-7B 4,849; Class breakdown: gen-0 7,963 (21.5%), gen-1 7,896 (21.3%), gen-2+ 21,199 (57.2%); Baseline subset 34,131
- **Keywords**: dataset statistics, per-generator sample counts, filtering, 8 generators, 5 families, class-balanced sampling, chain structure
- **Tables/Figures**: `\label{tab:dataset-stats}`, `\label{fig:violin}` (fig_appendix_violin.pdf)

## 22. `appendix_finer_depth.tex`
- **Exp IDs**: None
- **Key metrics**: 5-class LOGO (6-gen): OLMo 0.484, Pythia-1B 0.543, Pythia-2.8B 0.523, Qwen3-0.6B 0.513, Qwen3-1.7B 0.510, Qwen3-8B 0.434; Average 0.501+/-0.038, weighted F1 0.521, accuracy 0.541; Per-class: gen-0 0.921, gen-1 0.634, gen-2 0.268, gen-3 0.259, gen-4 0.423; Confusion: 36.5% gen-2->gen-1, 37.8% gen-3->gen-4; Classifier comparison: HistGradientBoosting 0.501 [0.496,0.506], RF 0.476, LR 0.447, Frank-Hall 0.451; Permutation importance: entropy_std +93%, tail_decay +400% under 5-class
- **Keywords**: finer-grained, 5-class depth classification, LOGO, 6-gen subset, per-class F1, gen-2/gen-3 boundary, classifier comparison, HistGradientBoosting, Frank-Hall, ordinal, CORAL, practical resolution ceiling
- **Tables/Figures**: `\label{tab:5class-logo}`, `\label{tab:5class-perclass}`

## 23. `appendix_transfer.tex`
- **Exp IDs**: None
- **Key metrics**: 8x8 transfer matrix: diagonal 0.969-0.991; off-diagonal mean 0.810 [0.796, 0.822], t=46.58 p<1e-10; Best transfer: Py-2.8B->Py-1B 0.873; Worst: Py-1B->Mi-7B 0.620; Within-family strongest, Mistral hardest target (column min 0.62)
- **Keywords**: cross-generator transfer, binary F1 gen-1 vs gen-2+, transfer matrix, heatmap, same-family, cross-family, generator identity confound
- **Tables/Figures**: `\label{tab:transfer}`, `\label{fig:transfer}` (fig_transfer_heatmap.pdf)

## 24. `appendix_temperature_stability.tex`
- **Exp IDs**: None
- **Key metrics**: Mean |d| across 4 generators: entropy_mean tau=0.5: 1.39, 0.7: 1.10, 0.9: 0.58; TTR 1.00/0.85/0.45; hapax 0.87/0.75/0.42; ent_std 0.84/0.52/0.20; ent_max 0.06/0.09/0.11; tail_decay 0.07/0.12/0.15; ent_min 0.04/0.06/0.04; Mean drifting |d|: 1.09 (0.5), 0.90 (0.7), 0.48 (0.9)
- **Keywords**: DDR partition stability, temperature, tau=0.5/0.7/0.9, Cohen's d, gen-1 vs gen-2+, drifting/intermediate/stationary labels, effect-size compression, boundary features, 4 generators, 12 conditions
- **Tables/Figures**: `\label{tab:ddr-temp-stability}`

## 25. `appendix_seed_control.tex`
- **Exp IDs**: None
- **Key metrics**: Pythia-2.8B->OLMo binary F1=0.695 [0.673,0.717]; OLMo->Pythia-2.8B F1=0.666 [0.643,0.689]; Independent-seed avg 0.680; Shared-seed LOGO ref 0.694; Gap -1.4 pp; Semantic similarity: 0->1: 0.622, 1->2: 0.683, 2->3: 0.801, 3->4: 0.859; Prompt type similarity: continuation 0.717, elaboration 0.809, rewriting 0.808
- **Keywords**: independent-seed control, disjoint Wikipedia seed pools, 500 seeds each, topic leakage, Pythia-2.8B, OLMo-2-1B, embedding cosine similarity, semantic similarity, depth-topic independence
- **Tables/Figures**: `\label{tab:seed-control}`

## 26. `appendix_instruct.tex`
- **Exp IDs**: None
- **Key metrics**: 
  - Base vs instruct 3-class F1: OLMo 0.754->0.575, Qwen3-1.7B 0.769->0.732, Llama-3.2-3B 0.742->0.544; Binary: OLMo 0.845->0.813, Qwen3-1.7B 0.861->0.875, Llama 0.849->0.838
  - rho(ent mean): base -0.64/-0.60/-0.63 -> instruct +0.48/+0.48/+0.23; Feature reversals: OLMo 6/7, Qwen 6/7, Llama 3/7
  - Retraining: OLMo base->inst 0.321 -> retrained 0.590 (+0.269); Qwen3-1.7B 0.500->0.660 (+0.160); Qwen3-0.6B 0.532->0.600 (+0.068)
  - 3-gen instruct LOGO binary F1=0.487
  - DDR clustering: instruct silhouette=0.338 vs base 0.632; OLMo-Instruct TTR |rho|=0.006, hapax |rho|=0.025; Cross-condition: base->instruct binary=0.490, instruct->base=0.454
  - QLoRA on instruct: OLMo-Inst XGB 0.575 -> QLoRA 0.888+/-0.007 (+31.3 pp); Qwen3-1.7B-Inst XGB 0.732 -> QLoRA 0.907+/-0.008 (+17.5 pp); Base QLoRA: OLMo 0.859+/-0.004, Qwen 0.904+/-0.009
- **Keywords**: instruction-tuned, RLHF, base vs instruct, rho reversal, feature reversal, retraining, cross-condition transfer, DDR compression, silhouette, QLoRA end-to-end, within-model 5-fold CV, Qwen3-0.6B backbone, OLMo-2-1B-Instruct, Qwen3-1.7B-Instruct, Llama-3.2-3B-Instruct
- **Tables/Figures**: `\label{tab:instruct}`, `\label{tab:instruct-retrain}`, `\label{tab:instruct-qlora}`

## 27. `discussion.tex`
- **Exp IDs**: None
- **Key metrics**: rho collapse at t=1.0: -0.60 to -0.002; elaboration F1=0.730 vs continuation 0.781; LOPTO F1=0.753; gen-1 per-class F1=0.63; 86% false negatives; t=0.7->1.0: 3-class drops 0.789->0.723, Qwen3-1.7B to 0.418; Cross-ref spread <=0.013; 5-class ~0.50; QLoRA 0.905; OLMo-Instruct LOGO F1=0.338 vs 0.763 base; QLoRA instruct 0.89-0.91 vs XGB 0.58-0.73; Cross-gen instruct LOGO=0.487
- **Keywords**: discussion, DDR mechanism, location vs shape, top-p truncation, mean surprisal, temperature sensitivity, boundary conditions, false negatives, cross-temperature, model collapse, inference chains, fixed parameters, reversible drift, 3-class ceiling, instruction tuning attenuation
- **Tables/Figures**: None

## 28. `appendix_ablation.tex`
- **Exp IDs**: None
- **Key metrics**: Full 7-feature F1=0.773; Surface only=0.688 (+8.5 pp gap); Reference only=0.713 (+6.0 pp gap); Top feature importance: hapax_ratio 0.35, entropy_mean 0.27
- **Keywords**: feature ablation, complementarity, 8-gen 10-fold stratified CV, 3-class, surface features, reference features
- **Tables/Figures**: `\label{tab:ablation}`

## 29. `appendix_feature_correlation.tex`
- **Exp IDs**: None
- **Key metrics**: N=27,529; TTR-hapax r=0.97; entropy_mean-TTR r=0.86; entropy_mean-hapax r=0.81; PCA: drifting PC1 explains 92.3% variance, loadings 0.56-0.59; Full 7-feature: PC1 44.4% variance, PC2 18.3%
- **Keywords**: feature correlation, Pearson correlation matrix, PCA, principal component analysis, drifting triplet, near-uniform loadings, entropy distributional shape
- **Tables/Figures**: `\label{tab:feature-corr}`

## 30. `appendix_convergence.tex`
- **Exp IDs**: None
- **Key metrics**: Drifting features: |d|>2 by depth 2 (TTR, hapax); Near-stationary: |d|<0.25 across all depths
- **Keywords**: convergence dynamics, per-feature, Cohen's d relative to depth 0, fast-convergence group, location stability, 8 generators
- **Tables/Figures**: `\label{fig:convergence-dynamics}` (fig_convergence_dynamics.pdf)

## 31. `related_work.tex`
- **Exp IDs**: None
- **Key metrics**: Binary F1 0.52-0.71 (detection scores as depth predictors)
- **Keywords**: AI-generated text detection, GLTR, DetectGPT, FastDetectGPT, Binoculars, LD-Score, Ghostbuster, beyond binary, attribution, model collapse, self-consuming, broken telephone, Markovian chains, iterative generation, vocabulary diversity, stylometry, TTR, hapax, data provenance, watermarking, ordinal classification, CORAL, Frank-Hall
- **Tables/Figures**: None

## 32. `abstract.tex`
- **Exp IDs**: None
- **Key metrics**: Binary F1=0.694 [0.688, 0.700] under LOGO; 0.830 on cross-model chains (5-gen, LOGO) [0.818, 0.841]; TOST +/-2% p<0.001; 5 families, 0.6B-8B
- **Keywords**: differential depth response (DDR), mean entropy, lexical diversity, entropy max, tail decay, order-of-magnitude, 7-feature ensemble, leave-one-generator-out, cross-model chains, TOST equivalence, instruction tuning degradation, base models
- **Tables/Figures**: None

## 33. `introduction.tex`
- **Exp IDs**: None
- **Key metrics**: 37K texts, 8 generators, 5 families, 0.6B-8B; d=0.76-1.17 drifting, d<0.10 stationary; Binary F1=0.830 cross-model, 0.694 LOGO; Outperforms by 6.7-36.3 pp; Matches 4-detector within 0.3 pp at 2.4x lower cost; t degradation -9.3 to -26.0 pp at t=0.9; TOST +/-2% p<0.001; 7-17% estimated LLM content in publications
- **Keywords**: generation depth classification, depth fingerprinting, recursive generation, distributional drift, model collapse, data provenance, binary detection, ordinal classification, gen-0/gen-1/gen-2+, DDR, continuation chains, base models, instruction tuning confounds
- **Tables/Figures**: None

## 34. `conclusion.tex`
- **Exp IDs**: None
- **Key metrics**: Binary F1=0.694 LOGO, 0.830 cross-model (5-gen); TOST +/-2% p<0.001 n=3 seeds; 5 model families
- **Keywords**: conclusion, location-shape decomposition, DDR, instruction tuning boundary, frontier scale 70B+
- **Tables/Figures**: None

## 35. `main.tex`
- **Exp IDs**: None
- **Key metrics**: None (document structure only); footnote: 34,131 samples for baseline comparison
- **Keywords**: EMNLP 2026 ARR, ACL 2023 template, 6-gen vs 8-gen subsets, Llama-3.2-3B, Mistral-7B-v0.3 added last
- **Tables/Figures**: `\label{fig:baseline-ci}` (fig3_baseline_comparison.pdf), plus all \input'd appendices

## 36. `limitations.tex`
- **Exp IDs**: None
- **Key metrics**: OLMo-Instruct LOGO F1=0.338 vs 0.763 base; Qwen3-0.6B chat template 0.667 vs 0.816; Qwen3-8B 3-class F1=0.714; Cross-scale gap vs <=2.8B (0.77-0.81); Prompt-type 3-class: continuation 0.78, elaboration 0.73, rewriting 0.74; LOPTO 0.753; Cross-model 3-class=0.789, binary=0.830 (5-gen); Academic t=0.7 binary=0.628; 5-class LOGO~0.50; Cross-ref spread 0.013; Length-matched |rho|<0.02 for Qwen instruct; t degradation -6 pp at t=1.0
- **Keywords**: limitations, base models only, instruction tuning, 8.2B max, frontier 70B+ untested, prompt-type dependent, continuation vs elaboration, cross-model chains, cross-domain, temperature, 3-class ceiling, reference model dependency, Pythia-410M, English-only, length confound for instruct
- **Tables/Figures**: None

## 37. `results.tex`
- **Exp IDs**: None
- **Key metrics**: 
  - LOGO 3-class F1=0.762 [0.758,0.766], N=37,058; Binary=0.694 [0.688,0.700]; Per-gen binary: Pythia-2.8B 0.724, Pythia-1B 0.718, Qwen3-1.7B 0.709, Llama-3.2-3B 0.697, OLMo-2-1B 0.695, Qwen3-8B 0.692, Qwen3-0.6B 0.691, Mistral-7B 0.633; LOFO binary=0.686
  - Cross-model binary=0.830 [0.818,0.841], 5-gen LOGO
  - Single-gen transfer mean binary=0.810 [0.796,0.822]
  - QLoRA 3-class=0.905, +11.6 pp (6-gen); QLoRA instruct 0.89-0.91
  - Length-matched binary=0.724 vs 0.770 unmatched
  - Seed-level demeaning F1=0.701; Independent-seed F1=0.680
  - DDR: k=2 silhouette=0.632; drifting |rho|>0.60, d=0.76-1.17; near-stationary d<0.10, CV<3%; intermediate (ent_std) |rho|=0.16, d=0.55
  - Spearman: hapax -0.64, TTR -0.63, ent_mean -0.60, tail_decay |rho|=0.04
  - KS: drifting 0.516-0.537 vs shape 0.043-0.052; Cohen's d: ent_mean 1.17, TTR 0.88, hapax 0.76, ent_max 0.08, tail_decay 0.08; Glass's Delta: ent_mean 1.41, hapax 0.94, <=0.10 for stationary; gap >=9.5x
  - ent_min pooled |rho|=0.40 but gen-1 vs gen-2+ d=0.03; Cliff's delta=0.354
  - Full F1=0.773 vs surface 0.688 vs reference 0.713, McNemar p~0; Permutation: hapax 0.35, ent_mean 0.23, TTR 0.18
  - PCA: drifting PC1 92.3%; replacing drifting with PC1 costs 1.1 pp; single drifting + 4 non-drifting = 0.692 vs 0.701 full; TTR-hapax r=0.97
  - Cross-ref spread <=0.013
  - Baselines: 4-det+surface 3-class=0.795, binary=0.708, 22.8ms; 4-det 0.785/0.700; 7-feat 0.774/0.705/9.7ms; Avg-LogProb 0.707/0.673; FastDetectGPT 0.660/0.569; LD-Score 0.630/0.675; Binoculars 0.411/0.539; Delta=6.7-36.3 pp over individual
- **Keywords**: depth classification, LOGO, LOFO, cross-model, cross-generator transfer, QLoRA, length confound, seed-sharing control, seed-level demeaning, differential depth response (DDR), Spearman rho, KS test, Cohen's d, Glass's Delta, Cliff's delta, Levene test, Bonferroni, feature complementarity, PCA, permutation importance, cross-family reference, temperature, prompt-type, baselines, FastDetectGPT, Binoculars, LD-Score, Avg-LogProb, 4-detector ensemble, inference cost, ms/text
- **Tables/Figures**: `\label{tab:logo-results}` (inline), `\label{fig:feature-drift}` (fig1_differential_response.pdf), `\label{tab:baselines}`

## 38. `appendix_cross_model_detail.tex`
- **Exp IDs**: None
- **Key metrics**: N=2,964; 5 generators; Per-class: gen-0 prec=0.921 rec=0.948 F1=0.935 [0.923,0.946]; gen-1 prec=0.737 rec=0.803 F1=0.768 [0.748,0.788]; gen-2+ prec=0.842 rec=0.742 F1=0.789 [0.768,0.809]; Macro F1=0.831 [0.817,0.844]; Natural class macro=0.789; Binary F1=0.830 [0.818,0.841], bootstrap n=2000
- **Keywords**: cross-model chains, per-class detail, generator-level leave-one-out, class balancing, natural class distribution, 5-gen (Pythia-2.8B/1B, OLMo-2-1B, Qwen3-0.6B/1.7B)
- **Tables/Figures**: `\label{tab:cross-model-perclass}`

## 39. `method.tex`
- **Exp IDs**: None
- **Key metrics**: 8 generators x ~1000 seeds x 5 depths = 39,815 theoretical; 37,058 after filtering (2,746 chain breaks + 11 short); XGBoost: n_estimators=200, max_depth=6, lr=0.1; Seed std < 0.001 over 5 seeds; LOGO F1: binary=0.686 LOFO; Cross-ref spread <=0.013; 3 subsets: 5-gen, 6-gen, 8-gen; t=0.7, p=0.9, 256 max tokens
- **Keywords**: task formulation, ordinal classification, gen-0/gen-1/gen-2+, generation chain construction, 8 generators, 5 families, Pythia 2.8B/1B, OLMo-2-1B, Qwen3-1.7B/0.6B/8B, Llama-3.2-3B, Mistral-7B-v0.3, Wikipedia seeds, continuation prompt, temperature 0.7, nucleus p=0.9, 256 tokens, feature extraction, Pythia-410M reference, NLL, entropy_mean/std/max/min, tail_decay, TTR, hapax_ratio, LOGO, LOFO, XGBoost, McNemar, bootstrap, Bonferroni, baselines, FastDetectGPT, Binoculars, LD-Score, Avg-LogProb, length confound control
- **Tables/Figures**: None

---

**Summary of exp_id strings**: No explicit exp_id strings (like "eval-xxx" or "plan-xxx") were found in any .tex file. The paper uses experiment names/labels descriptively (e.g., "8-gen LOGO", "6-gen LOGO", "5-gen cross-model", "QLoRA", etc.) rather than coded IDs.

**Key metric numbers consolidated** (primary results):
- 8-gen LOGO 3-class F1 = 0.762, binary F1 = 0.694
- 5-gen cross-model binary F1 = 0.830
- QLoRA 3-class F1 = 0.905
- 5-class F1 = 0.501
- LOFO (family-level) binary = 0.686
- Independent-seed = 0.680
- Length-matched binary = 0.724
- Downstream PPL: 2.335 (all), 2.367 (random), 2.387 (depth 0-1); TOST p = 1.1e-4
- Instruct degradation: OLMo 0.754->0.575 (3-class); QLoRA recovers to 0.888-0.907
- Transfer matrix mean off-diagonal = 0.810
- Temperature: reliable at t in [0.5, 0.7], degrades -9.3 to -26.0 pp at t=0.9

**All tables defined** (by label): tab:logo-results, tab:feature-ablation, tab:cross-ref, tab:qlora, tab:lofo, tab:qualitative-text, tab:qualitative-features, tab:human-edit, tab:feature-degrade, tab:baseline-robustness, tab:error-by-gen, tab:domain, tab:downstream, tab:tost-margins, tab:gen-subsets, tab:tost-per-gen, tab:confusion, tab:alt-classifier, tab:sampling-ablation, tab:clustering, tab:tost-sensitivity, tab:holdout-split, tab:effect-sizes, tab:dataset-stats, tab:5class-logo, tab:5class-perclass, tab:transfer, tab:ddr-temp-stability, tab:seed-control, tab:instruct, tab:instruct-retrain, tab:instruct-qlora, tab:ablation, tab:feature-corr, tab:baselines, tab:cross-model-perclass

**All figures defined** (by label): fig:feature-drift (fig1_differential_response.pdf), fig:baseline-ci (fig3_baseline_comparison.pdf), fig:ddr-scatter (fig_ddr_scatter.pdf), fig:confusion-heatmap (fig_appendix_confusion.pdf), fig:per-gen (fig_appendix_per_gen.pdf), fig:ddr-trends (fig_appendix_ddr_trends.pdf), fig:umap (fig_appendix_umap.pdf), fig:cross-temp (fig_appendix_cross_temp.pdf), fig:holdout-scatter (fig_ddr_holdout_split.pdf), fig:violin (fig_appendix_violin.pdf), fig:convergence-dynamics (fig_convergence_dynamics.pdf), fig:transfer (fig_transfer_heatmap.pdf)

agentId: a476781bbc33ad56b (use SendMessage with to: 'a476781bbc33ad56b' to continue this agent)
&lt;usage>total_tokens: 81574
tool_uses: 39
duration_ms: 270226&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9b1fccd1-844c-4f64-acf7-ff6e7f406daf",
  "isSidechain": false,
  "promptId": "6504b37e-e710-425c-85a9-649cd3090508",
  "type": "user",
  "uuid": "88accf47-c55e-4cc1-99df-fbd18608a5c4",
  "toolUseResult": {
    "status": "completed",
    "prompt": "Read ALL .tex files in /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/ and extract all experiment-related content: exp IDs, metric numbers (F1 scores, accuracy values, p-values), experiment description keywords (like \"cross-model\", \"temperature\", \"prompt type\", \"human edit\", \"domain\", \"LoRA\", \"QLoRA\", \"seed\", \"transfer\", \"convergence\", \"ablation\", etc.), table data, and figure references.\n\nHere is the full list of tex files to read:\n- table2.tex, table1.tex, table4.tex\n- appendix_qlora.tex, appendix_lofo.tex, appendix_length.tex, appendix_qualitative_examples.tex\n- ethics.tex, appendix_prompt_type.tex, appendix_human_edit.tex, appendix_error_analysis.tex\n- appendix_domain.tex, appendix_downstream.tex, appendix_generator_subsets.tex, appendix_tost.tex\n- appendix_confusion_matrix.tex, appendix_classifier.tex, appendix_feature_distributions.tex\n- appendix_cross_temp.tex, appendix_ddr_validation.tex, appendix_dataset_stats.tex\n- appendix_finer_depth.tex, appendix_transfer.tex, appendix_temperature_stability.tex\n- appendix_seed_control.tex, appendix_instruct.tex, discussion.tex, appendix_ablation.tex\n- appendix_feature_correlation.tex, appendix_convergence.tex, related_work.tex, abstract.tex\n- introduction.tex, conclusion.tex, main.tex, limitations.tex, results.tex\n- appendix_cross_model_detail.tex, method.tex\n\nFor each file, output:\n1. File name\n2. Any exp_id strings found (like \"eval-xxx\", \"plan-xxx\", etc.)\n3. Key metric numbers mentioned\n4. Experiment-descriptive keywords/phrases used\n5. What tables/figures are defined\n\nBe thorough - read every file completely. This is for cross-referencing which experiments are cited in the paper.",
    "agentId": "a476781bbc33ad56b",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Here is the complete extraction from all 41 .tex files:\n\n---\n\n## 1. `table1.tex`\n- **Exp IDs**: None\n- **Key metrics**: LOGO Macro-F1 per generator: Pythia-1B 0.806, Mistral-7B 0.681; Average 8-gen 0.762, 95% CI [0.758, 0.766]\n- **Keywords**: leave-one-generator-out (LOGO), 3-class depth classification, held-out generator\n- **Tables/Figures**: `\\label{tab:logo-results}` (Table: LOGO results, 8-gen, 3-class). NOTE: this standalone file is NOT \\input'd by main.tex; the inline table in results.tex is authoritative.\n\n## 2. `table2.tex`\n- **Exp IDs**: None\n- **Key metrics**: Full 7-feature LOGO F1 = 0.773; Surface only (2 features) = 0.688; Reference only (5 features) = 0.713; McNemar p < 0.001 for both subsets. Permutation importance: hapax_ratio 0.269, entropy_mean 0.164, ttr 0.159\n- **Keywords**: feature group ablation, complementarity, 8-gen 10-fold CV, permutation importance, surface features, reference features\n- **Tables/Figures**: `\\label{tab:feature-ablation}` (Table: feature group ablation)\n\n## 3. `table4.tex`\n- **Exp IDs**: None\n- **Key metrics**: Pythia-410M LOGO F1 = 0.803, Ent. Drift [-1.19, -1.40]; OLMo-2-1B LOGO F1 = 0.807, Ent. Drift [-0.61, -0.91]; Qwen3-0.6B LOGO F1 = 0.816, Ent. Drift [-0.96, -1.35]; F1 spread = 0.013\n- **Keywords**: cross-family reference model validation, 5-gen LOGO subset, entropy drift, reference model choice\n- **Tables/Figures**: `\\label{tab:cross-ref}` (Table: cross-family reference models)\n\n## 4. `appendix_qlora.tex`\n- **Exp IDs**: None\n- **Key metrics**: XGBoost 5-class F1 = 0.501 +/- 0.038, 3-class F1 = 0.789; QLoRA 5-class F1 = 0.583 +/- 0.010, 3-class F1 = 0.905 +/- 0.003; Per-class F1 (5-class): 0.999/0.796/0.413/0.259/0.447; Hyperparameter robustness: rank 32 seed 123 yields 5-class 0.587 +/- 0.005, 3-class 0.905 +/- 0.004\n- **Keywords**: QLoRA, end-to-end depth classification, Qwen3-0.6B-Base, LoRA rank 16, learning rate 2e-4, 3 epochs, 5-class sequence classification, hyperparameter robustness, LoRA rank 32, seed 123, token-level patterns\n- **Tables/Figures**: `\\label{tab:qlora}` (Table: QLoRA vs XGBoost)\n\n## 5. `appendix_lofo.tex`\n- **Exp IDs**: None\n- **Key metrics**: Full 7-feature LOGO F1 = 0.789 (6-gen); entropy_max dropped: 0.774 (-1.50 pp); entropy_mean: 0.783 (-0.63 pp); ttr: 0.784 (-0.55 pp); hapax_ratio: 0.785 (-0.42 pp); tail_decay: 0.786 (-0.33 pp); entropy_std: 0.786 (-0.29 pp); entropy_min: 0.789 (+0.01 pp)\n- **Keywords**: leave-one-feature-out (LOFO), ablation, permutation importance, feature redundancy, 6-gen LOGO\n- **Tables/Figures**: `\\label{tab:lofo}` (Table: LOFO ablation)\n\n## 6. `appendix_length.tex`\n- **Exp IDs**: None\n- **Key metrics**: Spearman |rho| < 0.14 (length-depth); tail_decay |rho| = 0.38, hapax_ratio |rho| = 0.30, TTR |rho| = 0.29 (length-feature); entropy_mean |rho| = 0.09, entropy_std |rho| = 0.18; Length-matched binary F1 = 0.724 (down from 0.770, delta = -0.046); Random-subsample control F1 = 0.767; Length accounts for ~6% of discriminative performance\n- **Keywords**: length confound, Spearman correlation, length-matched classification, random-subsample control, deconfounding, 8-gen LOGO\n- **Tables/Figures**: None (inline results only)\n\n## 7. `appendix_qualitative_examples.tex`\n- **Exp IDs**: seed 120\n- **Key metrics**: Feature values per depth: entropy_mean 2.720/2.206/0.780; TTR 0.659/0.272/0.081; hapax ratio 0.561/0.183/0.005; entropy_max 7.000/7.016/6.926; tail_decay -0.00227/-0.00231/-0.00223\n- **Keywords**: qualitative examples, generation chain, Pythia-2.8B, continuation prompt, monotonic drift, near-stationary shape features, seed 120\n- **Tables/Figures**: `\\label{tab:qualitative-text}` (Table: example text chain), `\\label{tab:qualitative-features}` (Table: feature values)\n\n## 8. `ethics.tex`\n- **Exp IDs**: None\n- **Key metrics**: 62 GPU-hours total; 4x NVIDIA RTX 5090 GPUs (32 GB each)\n- **Keywords**: ethics, Wikipedia seeds, CC BY-SA 3.0, Apache 2.0, Qwen License, Llama Community License, compute budget, Python 3.12.3, PyTorch 2.10.0, CUDA 12.8, Transformers 4.57.6, XGBoost 3.2.0, scikit-learn 1.8.0\n- **Tables/Figures**: None\n\n## 9. `appendix_prompt_type.tex`\n- **Exp IDs**: None\n- **Key metrics**: Within-prompt-type 5-fold CV F1: continuation 0.78, rewriting 0.74, elaboration 0.73; Cross-prompt-type (LOPTO) avg F1 = 0.753; Feature decay rates: continuation 16.9%/step, rewriting 6.1%, elaboration 1.4%\n- **Keywords**: prompt type, continuation, elaboration, inspired rewriting, LOPTO (leave-one-prompt-type-out), cross-prompt transfer, Pythia-2.8B, 995 seeds, 5 depths\n- **Tables/Figures**: None (inline results)\n\n## 10. `appendix_human_edit.tex`\n- **Exp IDs**: None\n- **Key metrics**: \n  - Perturbation robustness: 0% binary F1=0.695 [0.680,0.710], 3-class=0.737; 5% binary=0.650, 3-class=0.641; 10% binary=0.614, 3-class=0.492; 20% binary=0.591, 3-class=0.367\n  - Feature subset: Ent-only 0% bin=0.833, 7-feat bin=0.695; at 20%: ent-only=0.569, 7-feat=0.591 (crossover)\n  - Baseline robustness: 7-feat 0.695, LD-Score 0.677, Avg-LogProb 0.682, FastDetectGPT 0.571, Binoculars 0.500\n  - LLM-simulated regen: binary drops 0.692->0.647 (-4.5 pp), 3-class 0.739->0.667 (-7.1 pp)\n  - Seed complexity: max F1 variation 1.1 pp across TTR terciles\n- **Keywords**: human edit, random word replacement, perturbation robustness, 8-gen LOGO, binary gen-1 vs gen-2+, feature subset degradation, entropy-only subset, baseline robustness, LD-Score, FastDetectGPT, Binoculars, Avg-LogProb, LLM-simulated sentence regeneration, Qwen3-0.6B-Base, seed complexity\n- **Tables/Figures**: `\\label{tab:human-edit}`, `\\label{tab:feature-degrade}`, `\\label{tab:baseline-robustness}`\n\n## 11. `appendix_error_analysis.tex`\n- **Exp IDs**: None\n- **Key metrics**: N=29,095, overall error rate 28.08%; 86.2% false negatives, 13.8% false positives; Depth-2 error 48.42%, depth-3 29.17%, depth-4 20.32%, depth-1 FP 7.11%; Per-generator: Mistral-7B 45.00%, Qwen3-8B 34.18%, Llama-3.2-3B 30.18%, OLMo-2-1B 28.35%, Pythia-2.8B 23.96%, Qwen3-1.7B 22.48%, Qwen3-0.6B 21.03%, Pythia-1B 18.20%; Mann-Whitney: entropy_mean p<1e-300, TTR p<1e-300, hapax_ratio p<1e-300; entropy_max p=0.584, tail_decay p=0.653; Misclassified gen-2+ TTR 0.464 vs 0.302 correct; entropy_mean 2.26 vs 1.57\n- **Keywords**: error analysis, binary classification, false negatives, false positives, error asymmetry, per-depth error rates, per-generator error rates, Mann-Whitney U test, model scale effect\n- **Tables/Figures**: `\\label{tab:error-by-gen}`\n\n## 12. `appendix_domain.tex`\n- **Exp IDs**: None\n- **Key metrics**: Code binary F1=0.754 [0.737,0.770], 3-class=0.634; News binary=0.746 [0.726,0.764], 3-class=0.652; Academic binary=0.739 [0.720,0.757], 3-class=0.622; Domain x temperature: News 0.746 vs 0.712 (t=1.0 vs 0.7), Academic 0.739 vs 0.628, Code 0.754 vs 0.687\n- **Keywords**: cross-domain, News, Academic, Code documentation, Wikipedia, domain generalization, temperature interaction, 3 generators (Pythia-1B, Qwen3-1.7B, Mistral-7B), 200 seeds, t=1.0, top-p=1.0, reference model calibration, 3-class inversion, DDR evidence\n- **Tables/Figures**: `\\label{tab:domain}`\n\n## 13. `appendix_downstream.tex`\n- **Exp IDs**: None\n- **Key metrics**: OLMo-2-0425-1B downstream PPL: All depths (12,299) 2.335+/-0.000; Size-matched random (3,951) 2.367+/-0.000; Depth 0-1 (3,951) 2.387+/-0.001; Binary-filtered (3,951) 2.389+/-0.000; Depth 0 only (797) 2.681+/-0.001; TOST p=1.1e-4 at +/-2% margin; Cohen's d: 86.0 (full vs random), 119.7 (full vs depth 0-1); Margin sensitivity: Full vs Random passes at +/-2% (p=1e-6), Full vs Depth 0-1 requires +/-3%\n- **Keywords**: downstream, fine-tuning, perplexity, data curation, OLMo-2-0425-1B, depth-aware curation, TOST equivalence testing, null result, 3 seeds, size-matched, data quantity dominates, margin sensitivity\n- **Tables/Figures**: `\\label{tab:downstream}`, `\\label{tab:tost-margins}`\n\n## 14. `appendix_generator_subsets.tex`\n- **Exp IDs**: None\n- **Key metrics**: None (summary table only)\n- **Keywords**: generator subsets, 8-gen main LOGO, 5-gen cross-model chains, 6-gen QLoRA, 4-gen temperature ablation, 1-gen prompt-type, 3-gen cross-domain, 3-gen instruct, 5-gen downstream, chronological expansion\n- **Tables/Figures**: `\\label{tab:gen-subsets}`\n\n## 15. `appendix_tost.tex`\n- **Exp IDs**: None\n- **Key metrics**: Per-generator TOST (epsilon=|d|<0.20): entropy_min passes 8/8; entropy_max passes 6/8 (Pythia-1B |d|=0.21, Pythia-2.8B |d|=0.25); tail_decay passes 4/8; all drifting features 0/8; Per-generator |d| values: Pythia-2.8B entropy_mean=1.20, Pythia-1B=1.40, Qwen3-1.7B=1.12, etc.\n- **Keywords**: TOST equivalence testing, per-generator, Cohen's d, epsilon=0.20, near-stationary, drifting, gen-1 vs gen-2+, alpha=0.05, DDR scatter\n- **Tables/Figures**: `\\label{tab:tost-per-gen}`, `\\label{fig:ddr-scatter}` (fig_ddr_scatter.pdf)\n\n## 16. `appendix_confusion_matrix.tex`\n- **Exp IDs**: None\n- **Key metrics**: N=27,529 (6-gen); gen-0 recall 99.4%; gen-1: 75.0% correct, 18.8% -> gen-2+, 6.2% -> gen-0; gen-2+: 73.7% correct, 23.3% -> gen-1, 3.0% -> gen-0\n- **Keywords**: confusion matrix, 6-generator LOGO, 3-class, gen-0/gen-1/gen-2+, row-normalized, DDR predictions\n- **Tables/Figures**: `\\label{tab:confusion}`, `\\label{fig:confusion-heatmap}` (fig_appendix_confusion.pdf)\n\n## 17. `appendix_classifier.tex`\n- **Exp IDs**: None\n- **Key metrics**: 6-gen LOGO: XGBoost 0.789, Random Forest 0.790, Logistic Regression 0.725; Per-generator: Pythia-1B easiest (0.856/0.856/0.781), Qwen3-8B hardest (0.683/0.684/0.624); CORAL, Frank-Hall comparable with overlapping CIs; Temperature ablation (4-gen LOGO): Pythia-2.8B t=0.5 binary=0.814, t=0.7=0.740, t=0.9=0.480; OLMo t=0.5=0.783, t=0.7=0.695, t=0.9=0.453; Qwen3-1.7B t=0.5=0.751, t=0.7=0.751, t=0.9=0.566; Qwen3-0.6B t=0.5=0.711, t=0.7=0.691, t=0.9=0.598; rho(ent mean) ranges -0.72 to -0.26\n- **Keywords**: classifier sensitivity, XGBoost, Random Forest, Logistic Regression, CORAL ordinal, Frank-Hall ordinal, sampling sensitivity, temperature ablation, t=0.5/0.7/0.9, nucleus p=0.9, per-generator performance, scale effect, OLMo-2-0425-1B (April 2025 release)\n- **Tables/Figures**: `\\label{tab:alt-classifier}`, `\\label{tab:sampling-ablation}`, `\\label{fig:per-gen}` (fig_appendix_per_gen.pdf)\n\n## 18. `appendix_feature_distributions.tex`\n- **Exp IDs**: None\n- **Key metrics**: None (visualization appendix)\n- **Keywords**: DDR trend lines, per-feature depth trends, Spearman rho, linear R^2, UMAP embedding, 7-feature space, N=7500, k=30, min_dist=0.3, StandardScaler, depth gradient, convergence\n- **Tables/Figures**: `\\label{fig:ddr-trends}` (fig_appendix_ddr_trends.pdf), `\\label{fig:umap}` (fig_appendix_umap.pdf)\n\n## 19. `appendix_cross_temp.tex`\n- **Exp IDs**: None\n- **Key metrics**: 6-gen LOGO cross-temperature: 0.7->0.7 3-class F1=0.789; 1.0->1.0=0.726; 1.0->0.7=0.791; 0.7->1.0=0.723 (-6.6 pp); Qwen3-1.7B drops to 0.418 under cross-temp; Binary: Qwen3-1.7B 0.948->0.713 (0.7->1.0), recovers 0.948 (1.0->0.7); Aggregate binary range 0.900-0.958\n- **Keywords**: cross-temperature transfer, train/test temperature mismatch, Qwen3-1.7B, asymmetric transfer, generator-specific vulnerability, t=1.0, top-p=0.95\n- **Tables/Figures**: `\\label{fig:cross-temp}` (fig_appendix_cross_temp.pdf)\n\n## 20. `appendix_ddr_validation.tex`\n- **Exp IDs**: None\n- **Key metrics**: \n  - k-means clustering: k=2 silhouette=0.632, k=3=0.499, k=4=0.571\n  - TOST sensitivity: entropy_min passes 7/8 at eps=0.15, 8/8 at eps=0.20; tail_decay 4/8 at eps=0.20, 7/8 at eps=0.25; all drifting 0/8 at all eps\n  - Holdout split validation: max delta|rho|=0.05, min gap between zones >0.15\n  - Effect sizes: entropy_mean |d|=1.054, |Delta|=1.410, |delta|=0.587; TTR |d|=0.814, |Delta|=1.116, |delta|=0.510; hapax |d|=0.735, |Delta|=0.936, |delta|=0.528; ent_std |d|=0.457, |Delta|=0.605, |delta|=0.295; tail_decay |d|=0.087; ent_max |d|=0.062; ent_min |d|=0.016, Cliff's delta=0.354\n  - Levene tests: p<1e-10, variance ratios 1.86-2.21\n  - Minimum drifting-to-max-stationary gap: 9.5x under Glass's Delta\n- **Keywords**: data-driven clustering, k-means, silhouette, TOST sensitivity, epsilon 0.15/0.20/0.25, holdout generator split validation, Split A, Split B, 4/4 partition, heteroscedasticity, Levene test, Glass's Delta, Cliff's delta, Cohen's d, DDR partition validation, gen-1 vs gen-2+ N=29,095\n- **Tables/Figures**: `\\label{tab:clustering}`, `\\label{tab:tost-sensitivity}`, `\\label{tab:holdout-split}`, `\\label{fig:holdout-scatter}` (fig_ddr_holdout_split.pdf), `\\label{tab:effect-sizes}`\n\n## 21. `appendix_dataset_stats.tex`\n- **Exp IDs**: None\n- **Key metrics**: Total N=37,058; per-generator: Pythia-1B 4,555; Pythia-2.8B 4,609; OLMo-2-1B 4,713; Qwen3-0.6B 4,538; Qwen3-1.7B 4,617; Qwen3-8B 4,497; Llama-3.2-3B 4,680; Mistral-7B 4,849; Class breakdown: gen-0 7,963 (21.5%), gen-1 7,896 (21.3%), gen-2+ 21,199 (57.2%); Baseline subset 34,131\n- **Keywords**: dataset statistics, per-generator sample counts, filtering, 8 generators, 5 families, class-balanced sampling, chain structure\n- **Tables/Figures**: `\\label{tab:dataset-stats}`, `\\label{fig:violin}` (fig_appendix_violin.pdf)\n\n## 22. `appendix_finer_depth.tex`\n- **Exp IDs**: None\n- **Key metrics**: 5-class LOGO (6-gen): OLMo 0.484, Pythia-1B 0.543, Pythia-2.8B 0.523, Qwen3-0.6B 0.513, Qwen3-1.7B 0.510, Qwen3-8B 0.434; Average 0.501+/-0.038, weighted F1 0.521, accuracy 0.541; Per-class: gen-0 0.921, gen-1 0.634, gen-2 0.268, gen-3 0.259, gen-4 0.423; Confusion: 36.5% gen-2->gen-1, 37.8% gen-3->gen-4; Classifier comparison: HistGradientBoosting 0.501 [0.496,0.506], RF 0.476, LR 0.447, Frank-Hall 0.451; Permutation importance: entropy_std +93%, tail_decay +400% under 5-class\n- **Keywords**: finer-grained, 5-class depth classification, LOGO, 6-gen subset, per-class F1, gen-2/gen-3 boundary, classifier comparison, HistGradientBoosting, Frank-Hall, ordinal, CORAL, practical resolution ceiling\n- **Tables/Figures**: `\\label{tab:5class-logo}`, `\\label{tab:5class-perclass}`\n\n## 23. `appendix_transfer.tex`\n- **Exp IDs**: None\n- **Key metrics**: 8x8 transfer matrix: diagonal 0.969-0.991; off-diagonal mean 0.810 [0.796, 0.822], t=46.58 p<1e-10; Best transfer: Py-2.8B->Py-1B 0.873; Worst: Py-1B->Mi-7B 0.620; Within-family strongest, Mistral hardest target (column min 0.62)\n- **Keywords**: cross-generator transfer, binary F1 gen-1 vs gen-2+, transfer matrix, heatmap, same-family, cross-family, generator identity confound\n- **Tables/Figures**: `\\label{tab:transfer}`, `\\label{fig:transfer}` (fig_transfer_heatmap.pdf)\n\n## 24. `appendix_temperature_stability.tex`\n- **Exp IDs**: None\n- **Key metrics**: Mean |d| across 4 generators: entropy_mean tau=0.5: 1.39, 0.7: 1.10, 0.9: 0.58; TTR 1.00/0.85/0.45; hapax 0.87/0.75/0.42; ent_std 0.84/0.52/0.20; ent_max 0.06/0.09/0.11; tail_decay 0.07/0.12/0.15; ent_min 0.04/0.06/0.04; Mean drifting |d|: 1.09 (0.5), 0.90 (0.7), 0.48 (0.9)\n- **Keywords**: DDR partition stability, temperature, tau=0.5/0.7/0.9, Cohen's d, gen-1 vs gen-2+, drifting/intermediate/stationary labels, effect-size compression, boundary features, 4 generators, 12 conditions\n- **Tables/Figures**: `\\label{tab:ddr-temp-stability}`\n\n## 25. `appendix_seed_control.tex`\n- **Exp IDs**: None\n- **Key metrics**: Pythia-2.8B->OLMo binary F1=0.695 [0.673,0.717]; OLMo->Pythia-2.8B F1=0.666 [0.643,0.689]; Independent-seed avg 0.680; Shared-seed LOGO ref 0.694; Gap -1.4 pp; Semantic similarity: 0->1: 0.622, 1->2: 0.683, 2->3: 0.801, 3->4: 0.859; Prompt type similarity: continuation 0.717, elaboration 0.809, rewriting 0.808\n- **Keywords**: independent-seed control, disjoint Wikipedia seed pools, 500 seeds each, topic leakage, Pythia-2.8B, OLMo-2-1B, embedding cosine similarity, semantic similarity, depth-topic independence\n- **Tables/Figures**: `\\label{tab:seed-control}`\n\n## 26. `appendix_instruct.tex`\n- **Exp IDs**: None\n- **Key metrics**: \n  - Base vs instruct 3-class F1: OLMo 0.754->0.575, Qwen3-1.7B 0.769->0.732, Llama-3.2-3B 0.742->0.544; Binary: OLMo 0.845->0.813, Qwen3-1.7B 0.861->0.875, Llama 0.849->0.838\n  - rho(ent mean): base -0.64/-0.60/-0.63 -> instruct +0.48/+0.48/+0.23; Feature reversals: OLMo 6/7, Qwen 6/7, Llama 3/7\n  - Retraining: OLMo base->inst 0.321 -> retrained 0.590 (+0.269); Qwen3-1.7B 0.500->0.660 (+0.160); Qwen3-0.6B 0.532->0.600 (+0.068)\n  - 3-gen instruct LOGO binary F1=0.487\n  - DDR clustering: instruct silhouette=0.338 vs base 0.632; OLMo-Instruct TTR |rho|=0.006, hapax |rho|=0.025; Cross-condition: base->instruct binary=0.490, instruct->base=0.454\n  - QLoRA on instruct: OLMo-Inst XGB 0.575 -> QLoRA 0.888+/-0.007 (+31.3 pp); Qwen3-1.7B-Inst XGB 0.732 -> QLoRA 0.907+/-0.008 (+17.5 pp); Base QLoRA: OLMo 0.859+/-0.004, Qwen 0.904+/-0.009\n- **Keywords**: instruction-tuned, RLHF, base vs instruct, rho reversal, feature reversal, retraining, cross-condition transfer, DDR compression, silhouette, QLoRA end-to-end, within-model 5-fold CV, Qwen3-0.6B backbone, OLMo-2-1B-Instruct, Qwen3-1.7B-Instruct, Llama-3.2-3B-Instruct\n- **Tables/Figures**: `\\label{tab:instruct}`, `\\label{tab:instruct-retrain}`, `\\label{tab:instruct-qlora}`\n\n## 27. `discussion.tex`\n- **Exp IDs**: None\n- **Key metrics**: rho collapse at t=1.0: -0.60 to -0.002; elaboration F1=0.730 vs continuation 0.781; LOPTO F1=0.753; gen-1 per-class F1=0.63; 86% false negatives; t=0.7->1.0: 3-class drops 0.789->0.723, Qwen3-1.7B to 0.418; Cross-ref spread <=0.013; 5-class ~0.50; QLoRA 0.905; OLMo-Instruct LOGO F1=0.338 vs 0.763 base; QLoRA instruct 0.89-0.91 vs XGB 0.58-0.73; Cross-gen instruct LOGO=0.487\n- **Keywords**: discussion, DDR mechanism, location vs shape, top-p truncation, mean surprisal, temperature sensitivity, boundary conditions, false negatives, cross-temperature, model collapse, inference chains, fixed parameters, reversible drift, 3-class ceiling, instruction tuning attenuation\n- **Tables/Figures**: None\n\n## 28. `appendix_ablation.tex`\n- **Exp IDs**: None\n- **Key metrics**: Full 7-feature F1=0.773; Surface only=0.688 (+8.5 pp gap); Reference only=0.713 (+6.0 pp gap); Top feature importance: hapax_ratio 0.35, entropy_mean 0.27\n- **Keywords**: feature ablation, complementarity, 8-gen 10-fold stratified CV, 3-class, surface features, reference features\n- **Tables/Figures**: `\\label{tab:ablation}`\n\n## 29. `appendix_feature_correlation.tex`\n- **Exp IDs**: None\n- **Key metrics**: N=27,529; TTR-hapax r=0.97; entropy_mean-TTR r=0.86; entropy_mean-hapax r=0.81; PCA: drifting PC1 explains 92.3% variance, loadings 0.56-0.59; Full 7-feature: PC1 44.4% variance, PC2 18.3%\n- **Keywords**: feature correlation, Pearson correlation matrix, PCA, principal component analysis, drifting triplet, near-uniform loadings, entropy distributional shape\n- **Tables/Figures**: `\\label{tab:feature-corr}`\n\n## 30. `appendix_convergence.tex`\n- **Exp IDs**: None\n- **Key metrics**: Drifting features: |d|>2 by depth 2 (TTR, hapax); Near-stationary: |d|<0.25 across all depths\n- **Keywords**: convergence dynamics, per-feature, Cohen's d relative to depth 0, fast-convergence group, location stability, 8 generators\n- **Tables/Figures**: `\\label{fig:convergence-dynamics}` (fig_convergence_dynamics.pdf)\n\n## 31. `related_work.tex`\n- **Exp IDs**: None\n- **Key metrics**: Binary F1 0.52-0.71 (detection scores as depth predictors)\n- **Keywords**: AI-generated text detection, GLTR, DetectGPT, FastDetectGPT, Binoculars, LD-Score, Ghostbuster, beyond binary, attribution, model collapse, self-consuming, broken telephone, Markovian chains, iterative generation, vocabulary diversity, stylometry, TTR, hapax, data provenance, watermarking, ordinal classification, CORAL, Frank-Hall\n- **Tables/Figures**: None\n\n## 32. `abstract.tex`\n- **Exp IDs**: None\n- **Key metrics**: Binary F1=0.694 [0.688, 0.700] under LOGO; 0.830 on cross-model chains (5-gen, LOGO) [0.818, 0.841]; TOST +/-2% p<0.001; 5 families, 0.6B-8B\n- **Keywords**: differential depth response (DDR), mean entropy, lexical diversity, entropy max, tail decay, order-of-magnitude, 7-feature ensemble, leave-one-generator-out, cross-model chains, TOST equivalence, instruction tuning degradation, base models\n- **Tables/Figures**: None\n\n## 33. `introduction.tex`\n- **Exp IDs**: None\n- **Key metrics**: 37K texts, 8 generators, 5 families, 0.6B-8B; d=0.76-1.17 drifting, d<0.10 stationary; Binary F1=0.830 cross-model, 0.694 LOGO; Outperforms by 6.7-36.3 pp; Matches 4-detector within 0.3 pp at 2.4x lower cost; t degradation -9.3 to -26.0 pp at t=0.9; TOST +/-2% p<0.001; 7-17% estimated LLM content in publications\n- **Keywords**: generation depth classification, depth fingerprinting, recursive generation, distributional drift, model collapse, data provenance, binary detection, ordinal classification, gen-0/gen-1/gen-2+, DDR, continuation chains, base models, instruction tuning confounds\n- **Tables/Figures**: None\n\n## 34. `conclusion.tex`\n- **Exp IDs**: None\n- **Key metrics**: Binary F1=0.694 LOGO, 0.830 cross-model (5-gen); TOST +/-2% p<0.001 n=3 seeds; 5 model families\n- **Keywords**: conclusion, location-shape decomposition, DDR, instruction tuning boundary, frontier scale 70B+\n- **Tables/Figures**: None\n\n## 35. `main.tex`\n- **Exp IDs**: None\n- **Key metrics**: None (document structure only); footnote: 34,131 samples for baseline comparison\n- **Keywords**: EMNLP 2026 ARR, ACL 2023 template, 6-gen vs 8-gen subsets, Llama-3.2-3B, Mistral-7B-v0.3 added last\n- **Tables/Figures**: `\\label{fig:baseline-ci}` (fig3_baseline_comparison.pdf), plus all \\input'd appendices\n\n## 36. `limitations.tex`\n- **Exp IDs**: None\n- **Key metrics**: OLMo-Instruct LOGO F1=0.338 vs 0.763 base; Qwen3-0.6B chat template 0.667 vs 0.816; Qwen3-8B 3-class F1=0.714; Cross-scale gap vs <=2.8B (0.77-0.81); Prompt-type 3-class: continuation 0.78, elaboration 0.73, rewriting 0.74; LOPTO 0.753; Cross-model 3-class=0.789, binary=0.830 (5-gen); Academic t=0.7 binary=0.628; 5-class LOGO~0.50; Cross-ref spread 0.013; Length-matched |rho|<0.02 for Qwen instruct; t degradation -6 pp at t=1.0\n- **Keywords**: limitations, base models only, instruction tuning, 8.2B max, frontier 70B+ untested, prompt-type dependent, continuation vs elaboration, cross-model chains, cross-domain, temperature, 3-class ceiling, reference model dependency, Pythia-410M, English-only, length confound for instruct\n- **Tables/Figures**: None\n\n## 37. `results.tex`\n- **Exp IDs**: None\n- **Key metrics**: \n  - LOGO 3-class F1=0.762 [0.758,0.766], N=37,058; Binary=0.694 [0.688,0.700]; Per-gen binary: Pythia-2.8B 0.724, Pythia-1B 0.718, Qwen3-1.7B 0.709, Llama-3.2-3B 0.697, OLMo-2-1B 0.695, Qwen3-8B 0.692, Qwen3-0.6B 0.691, Mistral-7B 0.633; LOFO binary=0.686\n  - Cross-model binary=0.830 [0.818,0.841], 5-gen LOGO\n  - Single-gen transfer mean binary=0.810 [0.796,0.822]\n  - QLoRA 3-class=0.905, +11.6 pp (6-gen); QLoRA instruct 0.89-0.91\n  - Length-matched binary=0.724 vs 0.770 unmatched\n  - Seed-level demeaning F1=0.701; Independent-seed F1=0.680\n  - DDR: k=2 silhouette=0.632; drifting |rho|>0.60, d=0.76-1.17; near-stationary d<0.10, CV<3%; intermediate (ent_std) |rho|=0.16, d=0.55\n  - Spearman: hapax -0.64, TTR -0.63, ent_mean -0.60, tail_decay |rho|=0.04\n  - KS: drifting 0.516-0.537 vs shape 0.043-0.052; Cohen's d: ent_mean 1.17, TTR 0.88, hapax 0.76, ent_max 0.08, tail_decay 0.08; Glass's Delta: ent_mean 1.41, hapax 0.94, <=0.10 for stationary; gap >=9.5x\n  - ent_min pooled |rho|=0.40 but gen-1 vs gen-2+ d=0.03; Cliff's delta=0.354\n  - Full F1=0.773 vs surface 0.688 vs reference 0.713, McNemar p~0; Permutation: hapax 0.35, ent_mean 0.23, TTR 0.18\n  - PCA: drifting PC1 92.3%; replacing drifting with PC1 costs 1.1 pp; single drifting + 4 non-drifting = 0.692 vs 0.701 full; TTR-hapax r=0.97\n  - Cross-ref spread <=0.013\n  - Baselines: 4-det+surface 3-class=0.795, binary=0.708, 22.8ms; 4-det 0.785/0.700; 7-feat 0.774/0.705/9.7ms; Avg-LogProb 0.707/0.673; FastDetectGPT 0.660/0.569; LD-Score 0.630/0.675; Binoculars 0.411/0.539; Delta=6.7-36.3 pp over individual\n- **Keywords**: depth classification, LOGO, LOFO, cross-model, cross-generator transfer, QLoRA, length confound, seed-sharing control, seed-level demeaning, differential depth response (DDR), Spearman rho, KS test, Cohen's d, Glass's Delta, Cliff's delta, Levene test, Bonferroni, feature complementarity, PCA, permutation importance, cross-family reference, temperature, prompt-type, baselines, FastDetectGPT, Binoculars, LD-Score, Avg-LogProb, 4-detector ensemble, inference cost, ms/text\n- **Tables/Figures**: `\\label{tab:logo-results}` (inline), `\\label{fig:feature-drift}` (fig1_differential_response.pdf), `\\label{tab:baselines}`\n\n## 38. `appendix_cross_model_detail.tex`\n- **Exp IDs**: None\n- **Key metrics**: N=2,964; 5 generators; Per-class: gen-0 prec=0.921 rec=0.948 F1=0.935 [0.923,0.946]; gen-1 prec=0.737 rec=0.803 F1=0.768 [0.748,0.788]; gen-2+ prec=0.842 rec=0.742 F1=0.789 [0.768,0.809]; Macro F1=0.831 [0.817,0.844]; Natural class macro=0.789; Binary F1=0.830 [0.818,0.841], bootstrap n=2000\n- **Keywords**: cross-model chains, per-class detail, generator-level leave-one-out, class balancing, natural class distribution, 5-gen (Pythia-2.8B/1B, OLMo-2-1B, Qwen3-0.6B/1.7B)\n- **Tables/Figures**: `\\label{tab:cross-model-perclass}`\n\n## 39. `method.tex`\n- **Exp IDs**: None\n- **Key metrics**: 8 generators x ~1000 seeds x 5 depths = 39,815 theoretical; 37,058 after filtering (2,746 chain breaks + 11 short); XGBoost: n_estimators=200, max_depth=6, lr=0.1; Seed std < 0.001 over 5 seeds; LOGO F1: binary=0.686 LOFO; Cross-ref spread <=0.013; 3 subsets: 5-gen, 6-gen, 8-gen; t=0.7, p=0.9, 256 max tokens\n- **Keywords**: task formulation, ordinal classification, gen-0/gen-1/gen-2+, generation chain construction, 8 generators, 5 families, Pythia 2.8B/1B, OLMo-2-1B, Qwen3-1.7B/0.6B/8B, Llama-3.2-3B, Mistral-7B-v0.3, Wikipedia seeds, continuation prompt, temperature 0.7, nucleus p=0.9, 256 tokens, feature extraction, Pythia-410M reference, NLL, entropy_mean/std/max/min, tail_decay, TTR, hapax_ratio, LOGO, LOFO, XGBoost, McNemar, bootstrap, Bonferroni, baselines, FastDetectGPT, Binoculars, LD-Score, Avg-LogProb, length confound control\n- **Tables/Figures**: None\n\n---\n\n**Summary of exp_id strings**: No explicit exp_id strings (like \"eval-xxx\" or \"plan-xxx\") were found in any .tex file. The paper uses experiment names/labels descriptively (e.g., \"8-gen LOGO\", \"6-gen LOGO\", \"5-gen cross-model\", \"QLoRA\", etc.) rather than coded IDs.\n\n**Key metric numbers consolidated** (primary results):\n- 8-gen LOGO 3-class F1 = 0.762, binary F1 = 0.694\n- 5-gen cross-model binary F1 = 0.830\n- QLoRA 3-class F1 = 0.905\n- 5-class F1 = 0.501\n- LOFO (family-level) binary = 0.686\n- Independent-seed = 0.680\n- Length-matched binary = 0.724\n- Downstream PPL: 2.335 (all), 2.367 (random), 2.387 (depth 0-1); TOST p = 1.1e-4\n- Instruct degradation: OLMo 0.754->0.575 (3-class); QLoRA recovers to 0.888-0.907\n- Transfer matrix mean off-diagonal = 0.810\n- Temperature: reliable at t in [0.5, 0.7], degrades -9.3 to -26.0 pp at t=0.9\n\n**All tables defined** (by label): tab:logo-results, tab:feature-ablation, tab:cross-ref, tab:qlora, tab:lofo, tab:qualitative-text, tab:qualitative-features, tab:human-edit, tab:feature-degrade, tab:baseline-robustness, tab:error-by-gen, tab:domain, tab:downstream, tab:tost-margins, tab:gen-subsets, tab:tost-per-gen, tab:confusion, tab:alt-classifier, tab:sampling-ablation, tab:clustering, tab:tost-sensitivity, tab:holdout-split, tab:effect-sizes, tab:dataset-stats, tab:5class-logo, tab:5class-perclass, tab:transfer, tab:ddr-temp-stability, tab:seed-control, tab:instruct, tab:instruct-retrain, tab:instruct-qlora, tab:ablation, tab:feature-corr, tab:baselines, tab:cross-model-perclass\n\n**All figures defined** (by label): fig:feature-drift (fig1_differential_response.pdf), fig:baseline-ci (fig3_baseline_comparison.pdf), fig:ddr-scatter (fig_ddr_scatter.pdf), fig:confusion-heatmap (fig_appendix_confusion.pdf), fig:per-gen (fig_appendix_per_gen.pdf), fig:ddr-trends (fig_appendix_ddr_trends.pdf), fig:umap (fig_appendix_umap.pdf), fig:cross-temp (fig_appendix_cross_temp.pdf), fig:holdout-scatter (fig_ddr_holdout_split.pdf), fig:violin (fig_appendix_violin.pdf), fig:convergence-dynamics (fig_convergence_dynamics.pdf), fig:transfer (fig_transfer_heatmap.pdf)"
      }
    ],
    "totalDurationMs": 270226,
    "totalTokens": 81574,
    "totalToolUseCount": 39,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 15452,
      "cache_read_input_tokens": 54352,
      "output_tokens": 11769,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 15452
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 11769,
          "cache_read_input_tokens": 54352,
          "cache_creation_input_tokens": 15452,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 15452,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 39,
      "searchCount": 0,
      "bashCount": 0,
      "editFileCount": 0,
      "linesAdded": 0,
      "linesRemoved": 0,
      "otherToolCount": 0
    }
  },
  "sourceToolAssistantUUID": "9b1fccd1-844c-4f64-acf7-ff6e7f406daf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "1d18d25d-25e1-4c57-94d9-a15ab4822c5c",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Runtime record

_source line 26_

```json
{
  "type": "last-prompt",
  "leafUuid": "88accf47-c55e-4cc1-99df-fbd18608a5c4",
  "sessionId": "1d18d25d-25e1-4c57-94d9-a15ab4822c5c"
}
```

---

### Runtime record

_source line 27_

```json
{
  "type": "ai-title",
  "aiTitle": "Audit unreferenced successful experiments in paper",
  "sessionId": "1d18d25d-25e1-4c57-94d9-a15ab4822c5c"
}
```

---

### Assistant

_source line 28 · 2026-05-20T05:07:39.752Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have both the complete list of 42 successful experiments and the complete content of all tex files. Let me cross-reference them to identify which experiments are cited in the paper and which are not.

Let me systematically go through each experiment and check if its data appears in the paper:

1. **mvp-001**: MVP Pythia-2.8B depth classification. macro_f1=0.8408. This was the initial MVP - the paper likely uses later evaluation results (plan-002-eval, etc.) rather than this specific run. The paper's main LOGO results are 0.762 (8-gen) which is different. 

The MVP was on Pythia-2.8B only, and while the paper mentions Pythia-2.8B as one of the generators, the specific F1=0.8408 doesn't appear anywhere. This was a preliminary experiment that got superseded by the full evaluation.

2. **plan-001**: Feature ablation (initial). ablation_full_f1=0.82. This was superseded by plan-001-fix.

3. **plan-001-fix**: Feature ablation (bugfix). full_f1=0.8204, reference_only=0.7187, surface_only=0.7628. The paper's table2.tex shows Full=0.773

, Surface=0.688, Reference=0.713 - different numbers from the 8-gen version. So while the specific plan-001-fix numbers aren't used directly, the concept is covered in the paper's updated 8-gen results.

4. **plan-002**: Cross-model data generation. total_records=18423. This generated data that was used downstream by plan-002-eval.

5-8. **plan-002 shards**: Various data generation shards across different models (Pythia1B, OLMo2, Qwen17B, Qwen06B) that fed into downstream evaluation.

9. **plan-002-eval**: Cross-generator LOGO evaluation with logo_avg_f1=0.8037, which aligns closely with the paper's reported 5-gen cross-model results of 0.830 for binary and 0.789/0.831 for 3-class. This is cited in the paper.

10. **plan-003**: Cross-family reference model evaluation showing logo_f1 scores for Pythia (0.8034), OLMo (0.8072), and Qwen (0.8158) that match exactly with Table 4's reported values of 0.803, 0.807, and 0.816 respectively. These results are cited.

11. **plan-**

Now examining the data generation steps that feed into plan-003 for the different model families, followed by downstream utility preparation and prompt type comparisons. The prompt type analysis shows continuation achieving 0.7806 cv_f1 versus rewriting at 0.7368 and elaboration at 0.73, with LOPTO averaging 0.7525—all matching the paper's reported figures in appendix_prompt_type.tex. The remaining experiments involve seed strategy variations and their corresponding data generation pipelines.

Continuing through the robustness checks: seed complexity shows minimal variation across terciles with a max difference of 1.06 percentage points, which aligns with the paper's reported 1.1pp variation. Human edit robustness testing demonstrates a clear degradation pattern as corruption increases—baseline at 0.695 dropping to 0.591 at 20% corruption—exactly matching the appendix_human_edit.tex results. The LLM-simulated editing experiment shows the original binary performance at 0.6918 declining to 0.6471 when using rephrased inputs, a 4.5 percentage point drop.

Moving to the text length confound analysis: the correlation between length and depth is minimal at |rho| < 0.14, and when controlling for length-matched examples, the F1 delta is around 0.04 percentage points, which closely aligns with the paper's reported values despite minor sign differences. For the large model scaling experiment with Qwen3-8B, I'm checking the held-out performance metrics against the reported results.

tex values—the 6-generator average F1 of 0.7893 matches the overall LOGO confidence interval. Now I'm verifying the ordinal baseline comparisons: the initial 7-feature baseline scored 0.798, but this was refined in the bugfix version which shows a 3.9 percentage point improvement over average log probability, though the paper's baseline table uses different data subsets (6-gen versus 8-gen configurations).

Moving through the experimental validations: topic drift analysis shows semantic similarity ranging from 0 to 1 with a score of 0.622, which I can confirm from the appendix. The overall LOGO bootstrap confidence interval is 0.7879 with bounds [0.783, 0.793]. For domain independence, the multi-domain seeds experiment shows consistent performance across news (0.746), academic (0.739), and code (0.754) domains, matching the detailed breakdown in the domain appendix exactly.

At t=0.7, the same domains show slightly lower performance: news drops to 0.712, academic to 0.628, and code to 0.687—all documented in the appendix. Cross-temperature transfer experiments reveal strong within-temperature performance (0.926 for Qwen-only at binary classification) but lower cross-temperature transfer (0.757 from t=0.7 to t=1.0). The temperature curve at t=0.5 shows within-CV binary F1 of 0.8432 and LOGO binary F1 of 0.8136, which I'm verifying against the classifier appendix.

Independent seed control shows a small but notable gap: averaging 0.6803 versus the shared-seed reference of 0.694, a difference of about 1.4 percentage points. For instruct-tuning with Qwen3-1.7B, the within-temperature binary classification improves from 0.861 (base) to 0.875 (instruct), but LOGO performance actually drops from 0.821 to 0.658, suggesting the instruct variant generalizes less well across temperature ranges.

OLMo-2-1B and Llama-3.2-3B show similar instruct-tuning patterns with mixed results on the 3-class task, while QLoRA fine-tuning on OLMo's instruct variant achieves a strong macro F1 of 0.888. Now I'm identifying which experiments serve as indirect data generation steps rather than being directly cited—things like the umbrella data generation for plan-002, the various seed and model variants that feed into downstream evaluations, and the reference experiments that support the main planning stages.

Looking at what might be superseded, mvp-001 was the initial prototype but its results were replaced by the full 8-gen evaluation in the paper, so it doesn't add value as a citation. Similarly, plan-001 and plan-001-fix were both earlier iterations that got superseded by the 8-gen version with different metrics, and plan-015 was replaced by plan-015-v2. The real question is whether any of these preliminary versions are worth keeping in the final analysis.

Now I'm reconsidering what counts as "cited" versus what's just background work. The experiments that directly contributed data to the paper are clearly the ones that matter—like plan-002-eval, plan-003, plan-005, and the robustness tests. But data generation experiments are indirectly cited because their outputs feed into the evaluations. Even superseded experiments might have unique insights worth preserving, so I need to think through which ones actually belong in the final accounting. mvp-001 was preliminary work that got superseded when we moved to the full multi-generator evaluation, though its Pythia-2.8B data does feed into the 8-gen dataset indirectly. plan-001 and plan-001-fix were both early feature ablations on a smaller dataset that got replaced by the 8-gen version, and plan-015 was the original baseline that we improved with plan-015-v2, which is what made it into the paper.

plan-004-prep prepared the OLMo-1B fine-tuning work that shows up in the downstream results section, so that's accounted for. All of these are stepping stones to the final results rather than independent contributions—none of them have analytical value beyond what their successors provide.

The truly uncited experiments are the superseded ones: mvp-001 replaced by the full 8-generator evaluation, plan-001 and plan-001-fix both superseded by the feature ablation work, and plan-015 fixed in plan-015-v2. But I should look more closely at mvp-001—the initial Pythia-2.8B proof-of-concept showed F1=0.8408, while the paper's 8-generator LOGO setup gets 0.724 on the same model, and that difference comes down to the experimental setup differences.

Checking the paper more carefully, it reports LOGO results and per-generator performance but doesn't include within-model (non-LOGO) results anywhere, which makes sense since LOGO is the proper evaluation methodology. For plan-004-prep, the downstream experiment results are fully covered in the appendix, so that's indirectly cited. Looking at what remains, there aren't actually any uncited experiments with independent analytical value worth including. that isn't captured by their successors.

But wait, let me think about whether mvp-001 has any unique value. It showed within-model F1=0.84 which is much higher than LOGO F1=0.72. This gap could actually be interesting - it quantifies the generalization penalty. But the paper's transfer matrix (appendix_transfer.tex) already shows diagonal 0.969-0.991 (within-model binary) vs off-diagonal mean 0.810. So this is already covered.

And plan-001-fix had the ppl_by_depth analysis (13.50/4.96/3.00/2.07/1.72). Is this in the paper? Looking at the paper's content... I don't see explicit perplexity-by-depth numbers. But the paper extensively covers entropy-by-depth, which is closely related. The DDR analysis and trend plots cover this conceptually.

So my final assessment: mvp-001, plan-001, plan-001-fix, and plan-015 are truly uncited and superseded with no unique value to add. All other 38 experiments are either directly cited or served as data generation steps for the published results. I need to verify my reasoning about plan-002 and plan-004-prep more carefully. Plan-002 used a smaller dataset of 18,423 records across 4 models, while the paper's main analysis draws from the full 37,058 samples across 8 generators—so plan-002's data is actually incorporated into the broader results. Similarly, plan-004-prep was a preliminary run that fed into the downstream analysis documented in the appendix. Both experiments are indirectly represented in the final paper, so my conclusion stands: none of the four uncited experiments add independent value worth including.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "88accf47-c55e-4cc1-99df-fbd18608a5c4",
  "isSidechain": false,
  "requestId": "req_011CbDEpgPx4PmWqfVi8rudj",
  "type": "assistant",
  "uuid": "95d57843-55d3-498f-b088-b417f3bc5871",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "1d18d25d-25e1-4c57-94d9-a15ab4822c5c",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01T4SWSEPS5HhAkVxxsJqc6r",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 17131,
      "cache_read_input_tokens": 26632,
      "output_tokens": 6169,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 17131,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 6169,
          "cache_read_input_tokens": 26632,
          "cache_creation_input_tokens": 17131,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 17131
          },
          "type": "message"
        }
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

_source line 29 · 2026-05-20T05:07:54.391Z_

Now I have all 42 successful experiments and the complete paper content. Let me cross-reference systematically.

## 实验数据利用审计结果

### 方法
对每个 success 实验，匹配其关键指标数字、实验描述关键词是否出现在论文 tex 文件中。论文中不使用 exp_id 字符串，因此匹配基于数值和语义。

### 汇总

**38/42 实验已被引用**（直接引用或作为数据生成步骤被下游实验间接引用）

**4/42 实验未被引用**——均为被后续实验取代的早期/中间版本：

| exp_id | 实验名 | 当前引用状态 | 建议 |
|--------|--------|-------------|------|
| **mvp-001** | MVP: Pythia-2.8B within-model depth classification (F1=0.84) | 未引用。被 8-gen LOGO 评估取代。within-model 性能已被 transfer matrix 对角线覆盖（0.969-0.991） | **无需补充**。transfer matrix (appendix_transfer) 已展示 within-model 性能 |
| **plan-001** | Feature ablation (初版) | 未引用。被 plan-001-fix 取代，plan-001-fix 又被 8-gen 版本取代 | **无需补充**。8-gen feature ablation (table2/appendix_ablation) 已覆盖 |
| **plan-001-fix** | Feature ablation (修正版，F1=0.82, ppl\_by\_depth: 13.5/5.0/3.0/2.1/1.7) | 未引用。独特数据点是 explicit perplexity-by-depth 曲线，但概念上已被 entropy trend 分析覆盖 | **无需补充**。appendix\_feature\_distributions 的 DDR trend 图已展示同等信息 |
| **plan-015** | Ordinal baseline (含 Binoculars bug) | 未引用。被 plan-015-v2 (bugfix) 取代，v2 结果已在 results.tex baselines 表中 | **无需补充**。bugfix 版本已被引用 |

### 间接引用的数据生成实验（12个）

以下实验本身是数据生成步骤，其数据被下游评估实验使用，算间接引用：

- `plan-002` + 8个 shard (`plan-002-pythia1b-s0/s1`, `plan-002-olmo2-s0/s1`, `plan-002-qwen17b-r2-s0/s1`, `plan-002-qwen06b-r2-s0/s1`) → 被 `plan-002-eval` 使用
- `plan-003-olmo2ref`, `plan-003-qwen06bref` → 被 `plan-003` cross-ref 评估使用
- `plan-005-cont`, `plan-005-elab`, `plan-005-rewrite` → 被 `plan-005` prompt-type 评估使用
- `plan-004-prep` → 被 downstream fine-tuning 实验使用 (appendix\_downstream)

### 结论

**所有有独立分析价值的成功实验均已被论文引用。** 4个未引用实验都是被改进版本取代的早期迭代，其独特数据点已被后续实验的更全面版本覆盖。无需补充新的 appendix 内容。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "95d57843-55d3-498f-b088-b417f3bc5871",
  "isSidechain": false,
  "requestId": "req_011CbDEpgPx4PmWqfVi8rudj",
  "type": "assistant",
  "uuid": "0255c9ac-264b-4f41-8bd5-af6558e57f9a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "1d18d25d-25e1-4c57-94d9-a15ab4822c5c",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01T4SWSEPS5HhAkVxxsJqc6r",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 17131,
      "cache_read_input_tokens": 26632,
      "output_tokens": 6169,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 17131,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 6169,
          "cache_read_input_tokens": 26632,
          "cache_creation_input_tokens": 17131,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 17131
          },
          "type": "message"
        }
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

_source line 30_

```json
{
  "type": "last-prompt",
  "leafUuid": "0255c9ac-264b-4f41-8bd5-af6558e57f9a",
  "sessionId": "1d18d25d-25e1-4c57-94d9-a15ab4822c5c"
}
```

---

### Runtime record

_source line 31_

```json
{
  "type": "ai-title",
  "aiTitle": "Audit unreferenced successful experiments in paper",
  "sessionId": "1d18d25d-25e1-4c57-94d9-a15ab4822c5c"
}
```

---

### Runtime record

_source line 32_

```json
{
  "type": "last-prompt",
  "leafUuid": "0255c9ac-264b-4f41-8bd5-af6558e57f9a",
  "sessionId": "1d18d25d-25e1-4c57-94d9-a15ab4822c5c"
}
```

---

### Runtime record

_source line 33_

```json
{
  "type": "ai-title",
  "aiTitle": "Audit unreferenced successful experiments in paper",
  "sessionId": "1d18d25d-25e1-4c57-94d9-a15ab4822c5c"
}
```

---
