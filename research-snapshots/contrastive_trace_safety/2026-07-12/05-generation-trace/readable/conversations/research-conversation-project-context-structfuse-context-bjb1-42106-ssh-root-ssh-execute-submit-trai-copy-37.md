# Research conversation: <project_context> # 项目: structfuse-context ## 运行环境 - 服务器名: bjb1-42106 - SSH 账户: root（调用 ssh_execute / submit_training_jo

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 84
- **Recorded user turns:** 1
- **Tool calls:** 21
- **Original source:** `logs/chats/exported-trajectories/account-1/b1d97499-4652-4822-8fc5-dbdc566ceedc.jsonl`
- **Structured JSON:** [`3bfe234308777e215f8a.json`](../../sessions/3b/3bfe234308777e215f8a.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-14T21:31:42.064Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-14T21:31:42.064Z",
  "sessionId": "b1d97499-4652-4822-8fc5-dbdc566ceedc",
  "content": "&lt;project_context>\n# 项目: structfuse-context\n\n## 运行环境\n- 服务器名: bjb1-42106\n- SSH 账户: root（调用 ssh_execute / submit_training_job 时传入 account=\"root\"）\n- SSH 连接命令: ssh connect.bjb1.seetacloud.com  # 必须用此命令，~/.ssh/config 自动应用密钥和跳板机，禁止用裸 IP\n- 项目代码根目录: /root/structfuse\n\n\n## 环境搭建\n连接服务器后先调 `detect_image` 检测是否为预置镜像。如果匹配，跳过基础环境搭建，只装项目特有依赖。已预装的包不要重复安装。\n\n## 输出风格\n回复简洁直接。只输出执行结果和必要信息，不要解释过程、不要客套、不要给未被要求的建议。\n&lt;/project_context>\n## 任务：引用完整性修复\n\n你需要修复 3 个引用不一致问题，确保 literature_map.yaml、discussion_v2.md、registry 三处数据一致。\n\n### 问题 1：RepoGraph + GraphCoder 缺失\n- `artifacts/paper_drafts/discussion_v2.md` 引用了 RepoGraph 和 GraphCoder，但 `literature_map.yaml` 未收录。\n- **操作**：WebSearch 验证这两篇论文的真实性（标题、作者、venue、年份）。若真实存在，录入 literature_map.yaml（category、role、venue 等完整字段）。若不存在或无法验证，从 discussion_v2.md 移除引用。\n\n### 问题 2：ARISE 年份不一致\n- literature_map.yaml 记录 ARISE 为 2025，discussion_v2.md 写 2026。\n- **操作**：WebSearch 查证 ARISE 的实际发表/发布年份，然后统一两处记录。\n\n### 问题 3：CodeGRAG + CodeRAG 缺失说明\n- plan_017_literature registry 的 hypothesis 声称调研了 8 篇论文，其中包含 CodeGRAG 和 CodeRAG，但这两篇未出现在 literature_map.yaml 和 discussion_v2.md 中。\n- **操作**：在 registry 的 plan_017_literature notes 字段中补充排除理由（如\"CodeGRAG/CodeRAG 经调研发现与本文 scope 不符，因 XXX 原因未纳入 discussion\"，或者它们被合并到了其他条目中）。用 update_registry 更新。若实际上应该纳入，则录入 literature_map.yaml 并在 discussion_v2.md 添加讨论。\n\n### 文件路径\n- literature_map.yaml: 项目知识文件，用 read_project_file / save_project_file 读写\n- discussion_v2.md: `/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/discussion_v2.md`，用 Read/Edit 操作\n- registry: 用 read_registry / update_registry 操作\n\n### 产出\n完成后简要报告每个问题的处理结果。"
}
```

---

### Runtime record

_source line 2 · 2026-05-14T21:31:42.068Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-14T21:31:42.068Z",
  "sessionId": "b1d97499-4652-4822-8fc5-dbdc566ceedc"
}
```

---

## Round 1

82 recorded events

### User

_source line 3 · 2026-05-14T21:31:42.101Z_

&lt;project_context>
# 项目: structfuse-context

## 运行环境
- 服务器名: bjb1-42106
- SSH 账户: root（调用 ssh_execute / submit_training_job 时传入 account="root"）
- SSH 连接命令: ssh connect.bjb1.seetacloud.com  # 必须用此命令，~/.ssh/config 自动应用密钥和跳板机，禁止用裸 IP
- 项目代码根目录: /root/structfuse


## 环境搭建
连接服务器后先调 `detect_image` 检测是否为预置镜像。如果匹配，跳过基础环境搭建，只装项目特有依赖。已预装的包不要重复安装。

## 输出风格
回复简洁直接。只输出执行结果和必要信息，不要解释过程、不要客套、不要给未被要求的建议。
&lt;/project_context>
## 任务：引用完整性修复

你需要修复 3 个引用不一致问题，确保 literature_map.yaml、discussion_v2.md、registry 三处数据一致。

### 问题 1：RepoGraph + GraphCoder 缺失
- `artifacts/paper_drafts/discussion_v2.md` 引用了 RepoGraph 和 GraphCoder，但 `literature_map.yaml` 未收录。
- **操作**：WebSearch 验证这两篇论文的真实性（标题、作者、venue、年份）。若真实存在，录入 literature_map.yaml（category、role、venue 等完整字段）。若不存在或无法验证，从 discussion_v2.md 移除引用。

### 问题 2：ARISE 年份不一致
- literature_map.yaml 记录 ARISE 为 2025，discussion_v2.md 写 2026。
- **操作**：WebSearch 查证 ARISE 的实际发表/发布年份，然后统一两处记录。

### 问题 3：CodeGRAG + CodeRAG 缺失说明
- plan_017_literature registry 的 hypothesis 声称调研了 8 篇论文，其中包含 CodeGRAG 和 CodeRAG，但这两篇未出现在 literature_map.yaml 和 discussion_v2.md 中。
- **操作**：在 registry 的 plan_017_literature notes 字段中补充排除理由（如"CodeGRAG/CodeRAG 经调研发现与本文 scope 不符，因 XXX 原因未纳入 discussion"，或者它们被合并到了其他条目中）。用 update_registry 更新。若实际上应该纳入，则录入 literature_map.yaml 并在 discussion_v2.md 添加讨论。

### 文件路径
- literature_map.yaml: 项目知识文件，用 read_project_file / save_project_file 读写
- discussion_v2.md: `/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/discussion_v2.md`，用 Read/Edit 操作
- registry: 用 read_registry / update_registry 操作

### 产出
完成后简要报告每个问题的处理结果。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "255fffc4-c17f-4b3b-8b5c-7a3031fdb918",
  "type": "user",
  "uuid": "159b9da2-8466-4376-b43d-3dd4d16ff0d6",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "b1d97499-4652-4822-8fc5-dbdc566ceedc",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-14T21:31:42.100Z_

```json
{
  "parentUuid": "159b9da2-8466-4376-b43d-3dd4d16ff0d6",
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
  "uuid": "88e6a0ff-dc80-4e15-8a71-a3243b7ceefb",
  "timestamp": "2026-05-14T21:31:42.100Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "b1d97499-4652-4822-8fc5-dbdc566ceedc",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-14T21:31:42.100Z_

```json
{
  "parentUuid": "88e6a0ff-dc80-4e15-8a71-a3243b7ceefb",
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
  "uuid": "1c2c12aa-1b26-4533-bd00-74702ab76935",
  "timestamp": "2026-05-14T21:31:42.100Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "b1d97499-4652-4822-8fc5-dbdc566ceedc",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 6 · 2026-05-14T21:31:42.100Z_

```json
{
  "parentUuid": "1c2c12aa-1b26-4533-bd00-74702ab76935",
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
  "uuid": "ce25fa86-ecae-431f-8add-87fa763f3c74",
  "timestamp": "2026-05-14T21:31:42.100Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "b1d97499-4652-4822-8fc5-dbdc566ceedc",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 7 · 2026-05-14T21:31:42.100Z_

```json
{
  "parentUuid": "ce25fa86-ecae-431f-8add-87fa763f3c74",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "77900e88-3b15-4126-8b16-9c81bf6d9f1c",
  "timestamp": "2026-05-14T21:31:42.100Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "b1d97499-4652-4822-8fc5-dbdc566ceedc",
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
  "aiTitle": "Fix literature reference consistency issues",
  "sessionId": "b1d97499-4652-4822-8fc5-dbdc566ceedc"
}
```

---

### Assistant

_source line 9 · 2026-05-14T21:31:46.922Z_

I'll fix the 3 citation consistency issues. Let me start by reading all relevant files in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "77900e88-3b15-4126-8b16-9c81bf6d9f1c",
  "isSidechain": false,
  "requestId": "req_011Cb3B8xDxD5jeUkYJoDhmZ",
  "type": "assistant",
  "uuid": "59498d50-dc2d-437a-a864-a0e9e4a01ae2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "b1d97499-4652-4822-8fc5-dbdc566ceedc",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TC3SiQ4QoC2vuX3xiCF47k",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11835,
      "cache_read_input_tokens": 11447,
      "output_tokens": 159,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11835,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 159,
          "cache_read_input_tokens": 11447,
          "cache_creation_input_tokens": 11835,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11835
          },
          "type": "message"
        }
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

_source line 10 · 2026-05-14T21:31:47.688Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_014CiSa1PghTzbPXRjxR4GTy`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__save_project_file,mcp__agent-ml-research__read_registry,mcp__agent-ml-research__update_registry,WebSearch,WebFetch",
  "max_results": 6
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "59498d50-dc2d-437a-a864-a0e9e4a01ae2",
  "isSidechain": false,
  "requestId": "req_011Cb3B8xDxD5jeUkYJoDhmZ",
  "type": "assistant",
  "uuid": "ed36d8ef-5297-41f7-9af4-50a6500df721",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "b1d97499-4652-4822-8fc5-dbdc566ceedc",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TC3SiQ4QoC2vuX3xiCF47k",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11835,
      "cache_read_input_tokens": 11447,
      "output_tokens": 159,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11835,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 159,
          "cache_read_input_tokens": 11447,
          "cache_creation_input_tokens": 11835,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11835
          },
          "type": "message"
        }
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

_source line 11 · 2026-05-14T21:31:47.695Z_

<details><summary>↩ Tool result · `toolu_014CiSa1PghTzbPXRjxR4GTy`</summary>

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

```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__read_registry"
}
```

```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__update_registry"
}
```

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
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ed36d8ef-5297-41f7-9af4-50a6500df721",
  "isSidechain": false,
  "promptId": "255fffc4-c17f-4b3b-8b5c-7a3031fdb918",
  "type": "user",
  "uuid": "5c501ed8-2ba1-4c6c-80bb-76758db61421",
  "toolUseResult": {
    "matches": [
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__save_project_file",
      "mcp__agent-ml-research__read_registry",
      "mcp__agent-ml-research__update_registry",
      "WebSearch",
      "WebFetch"
    ],
    "query": "select:mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__save_project_file,mcp__agent-ml-research__read_registry,mcp__agent-ml-research__update_registry,WebSearch,WebFetch",
    "total_deferred_tools": 25
  },
  "sourceToolAssistantUUID": "ed36d8ef-5297-41f7-9af4-50a6500df721",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "b1d97499-4652-4822-8fc5-dbdc566ceedc",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 12 · 2026-05-14T21:31:52.914Z_

<details><summary>Logged reasoning block</summary>

```text
Let me read all the relevant files in parallel to understand the current state.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5c501ed8-2ba1-4c6c-80bb-76758db61421",
  "isSidechain": false,
  "requestId": "req_011Cb3B9YFarLnzvZyLBdJHq",
  "type": "assistant",
  "uuid": "c9c39efa-8fd7-4aaf-8a89-3cccf52a2180",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "b1d97499-4652-4822-8fc5-dbdc566ceedc",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0159wWsbkDUo7yK1B8HaNXhE",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2476,
      "cache_read_input_tokens": 23282,
      "output_tokens": 319,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2476,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 319,
          "cache_read_input_tokens": 23282,
          "cache_creation_input_tokens": 2476,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2476
          },
          "type": "message"
        }
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

_source line 13 · 2026-05-14T21:31:53.562Z_

Reading all relevant files in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c9c39efa-8fd7-4aaf-8a89-3cccf52a2180",
  "isSidechain": false,
  "requestId": "req_011Cb3B9YFarLnzvZyLBdJHq",
  "type": "assistant",
  "uuid": "0ea8043d-e588-4599-8872-b56429ce6ac2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "b1d97499-4652-4822-8fc5-dbdc566ceedc",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0159wWsbkDUo7yK1B8HaNXhE",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2476,
      "cache_read_input_tokens": 23282,
      "output_tokens": 319,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2476,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 319,
          "cache_read_input_tokens": 23282,
          "cache_creation_input_tokens": 2476,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2476
          },
          "type": "message"
        }
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

_source line 14 · 2026-05-14T21:31:54.553Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_011w5mvv72NBoD46WsuGy2YM`</summary>

```json
{
  "project": "structfuse-context",
  "file": "literature_map.yaml",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0ea8043d-e588-4599-8872-b56429ce6ac2",
  "isSidechain": false,
  "requestId": "req_011Cb3B9YFarLnzvZyLBdJHq",
  "type": "assistant",
  "uuid": "53a2c841-6dd6-4c5c-bd11-879b1ee031f1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "b1d97499-4652-4822-8fc5-dbdc566ceedc",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0159wWsbkDUo7yK1B8HaNXhE",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2476,
      "cache_read_input_tokens": 23282,
      "output_tokens": 319,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2476,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 319,
          "cache_read_input_tokens": 23282,
          "cache_creation_input_tokens": 2476,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2476
          },
          "type": "message"
        }
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

_source line 15 · 2026-05-14T21:31:54.567Z_

<details><summary>↩ Tool result · `toolu_011w5mvv72NBoD46WsuGy2YM`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/literature_map.yaml\", \"content\": \"# StructFuse — Related Work Literature Map\\n# 最后更新: 2026-05-14\\n# 说明: 只收录已验证存在的论文。每篇均经 WebSearch 确认标题/venue/year。\\n# 总计: 37 entries (含 2 个软件工具引用)\\n\\ncategories:\\n\\n  # ==========================================================================\\n  # Category 1: Code Retrieval for Bug Fixing / SWE-bench Ecosystem\\n  # ==========================================================================\\n  code_retrieval_bug_fixing:\\n    description: \\\"SWE-bench 及相关 repo-level 自动修复系统中的代码检索方法\\\"\\n    papers:\\n\\n      - title: \\\"SWE-bench: Can Language Models Resolve Real-World GitHub Issues?\\\"\\n        authors: \\\"Carlos E. Jimenez, John Yang, Alexander Wettig, Shunyu Yao, Kexin Pei, Ofir Press, Karthik Narasimhan\\\"\\n        venue: ICLR\\n        year: 2024\\n        relation: baseline\\n        summary: \\\"从 GitHub issues 构建 repo-level bug fixing benchmark，成为自动修复领域标准评估集。\\\"\\n\\n      - title: \\\"SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering\\\"\\n        authors: \\\"John Yang, Carlos E. Jimenez, Alexander Wettig, Kilian Lieret, Shunyu Yao, Karthik Narasimhan, Ofir Press\\\"\\n        venue: NeurIPS\\n        year: 2024\\n        relation: competitor\\n        summary: \\\"基于 LLM agent 的交互式 bug fixing 系统，定义了 ACI 接口范式。\\\"\\n\\n      - title: \\\"AutoCodeRover: Autonomous Program Improvement\\\"\\n        authors: \\\"Yuntong Zhang, Haifeng Ruan, Zhiyu Fan, Abhik Roychoudhury\\\"\\n        venue: ISSTA\\n        year: 2024\\n        relation: competitor\\n        summary: \\\"结合代码搜索与 spectrum-based fault localization，利用程序分析缩小修复范围。\\\"\\n\\n      - title: \\\"Agentless: Demystifying LLM-based Software Engineering Agents\\\"\\n        authors: \\\"Chunqiu Steven Xia, Yinlin Deng, Soren Dunn, Lingming Zhang\\\"\\n        venue: arXiv\\n        year: 2024\\n        relation: competitor\\n        summary: \\\"无 agent 架构的 two-phase localize-then-repair 方法，在 SWE-bench 上取得强 baseline。\\\"\\n\\n      - title: \\\"SWE-smith: Scaling Data for Software Engineering Agents\\\"\\n        authors: \\\"John Yang, Kilian Lieret, Carlos E. Jimenez, Alexander Wettig, Kabir Khandpur, Yanzhe Zhang, Binyuan Hui, Ofir Press, Ludwig Schmidt, Diyi Yang\\\"\\n        venue: \\\"NeurIPS (Datasets & Benchmarks, Spotlight)\\\"\\n        year: 2025\\n        relation: building-block\\n        summary: \\\"自动从 GitHub 生成大规模 SWE-bench 风格训练数据，StructFuse 用其 repos 做 data-flow 提取。\\\"\\n\\n      - title: \\\"RepoBench: Benchmarking Repository-Level Code Auto-Completion Systems\\\"\\n        authors: \\\"Tianyang Liu, Canwen Xu, Julian McAuley\\\"\\n        venue: ICLR\\n        year: 2024\\n        relation: baseline\\n        summary: \\\"Repo-level 代码补全/检索 benchmark，含 RepoBench-R 检索子任务。\\\"\\n\\n      - title: \\\"SweRank: Software Issue Localization with Code Ranking\\\"\\n        authors: \\\"Revanth Gangi Reddy, Tarun Suresh, JaeHyeok Doo, Ye Liu, Xuan Phi Nguyen, Yingbo Zhou, Semih Yavuz, Caiming Xiong, Heng Ji, Shafiq Joty\\\"\\n        venue: arXiv\\n        year: 2025\\n        relation: competitor\\n        summary: \\\"Retrieve-and-rerank 框架用于 software issue localization，在 SWE-Bench-Lite 和 LocBench 上 SOTA，text-based retrieval baseline。\\\"\\n\\n      - title: \\\"SWE-Fixer: Training Open-Source LLMs for Effective and Efficient GitHub Issue Resolution\\\"\\n        authors: \\\"Chengxing Xie, Bowen Li, Chang Gao, He Du, Wai Lam, Difan Zou, Kai Chen\\\"\\n        venue: \\\"ACL (Findings)\\\"\\n        year: 2025\\n        relation: competitor\\n        summary: \\\"BM25 + LLM retriever 的 coarse-to-fine file retrieval pipeline，在 SWE-Bench Verified 上 30.2%。\\\"\\n\\n  # ==========================================================================\\n  # Category 2: Hard Negative Mining in Contrastive Learning\\n  # ==========================================================================\\n  hard_negative_mining:\\n    description: \\\"对比学习中 hard negative 挖掘策略，以及密集检索中的负样本选择\\\"\\n    papers:\\n\\n      - title: \\\"Dense Passage Retrieval for Open-Domain Question Answering\\\"\\n        authors: \\\"Vladimir Karpukhin, Barlas Oguz, Sewon Min, Patrick Lewis, Ledell Wu, Sergey Edunov, Danqi Chen, Wen-tau Yih\\\"\\n        venue: EMNLP\\n        year: 2020\\n        relation: background\\n        summary: \\\"DPR 开创了 in-batch negatives + BM25 hard negatives 的双塔检索范式。\\\"\\n\\n      - title: \\\"Approximate Nearest Neighbor Negative Contrastive Learning for Dense Text Retrieval\\\"\\n        authors: \\\"Lee Xiong, Chenyan Xiong, Ye Li, Kwok-Fung Tang, Jialin Liu, Paul Bennett, Junaid Ahmed, Arnold Overwijk\\\"\\n        venue: ICLR\\n        year: 2021\\n        relation: background\\n        summary: \\\"ANCE 用 ANN index 动态挖掘 embedding-distance hard negatives，StructFuse 的 baseline negative 策略之一。\\\"\\n\\n      - title: \\\"A Simple Framework for Contrastive Learning of Visual Representations\\\"\\n        authors: \\\"Ting Chen, Simon Kornblith, Mohammad Norouzi, Geoffrey Hinton\\\"\\n        venue: ICML\\n        year: 2020\\n        relation: background\\n        summary: \\\"SimCLR 视觉对比学习奠基工作，证明 hard negatives 和大 batch size 对对比学习的重要性。\\\"\\n\\n      - title: \\\"Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks\\\"\\n        authors: \\\"Nils Reimers, Iryna Gurevych\\\"\\n        venue: EMNLP\\n        year: 2019\\n        relation: background\\n        summary: \\\"Siamese/triplet 网络训练句子嵌入，StructFuse 的对比训练框架与其类似。\\\"\\n\\n      - title: \\\"Curriculum Learning for Dense Retrieval Distillation\\\"\\n        authors: \\\"Hansi Zeng, Hamed Zamani, Vishwa Vinay\\\"\\n        venue: \\\"SIGIR (Best Short Paper)\\\"\\n        year: 2022\\n        relation: background\\n        summary: \\\"CL-DRD: 课程学习式知识蒸馏用于密集检索，从粗粒度到细粒度逐步增加训练难度。\\\"\\n\\n      - title: \\\"Effective Hard Negative Mining for Contrastive Learning-Based Code Search\\\"\\n        authors: \\\"Fan Y., Li C., Ge J., Huang L., Luo B.\\\"\\n        venue: \\\"ACM TOSEM\\\"\\n        year: 2025\\n        relation: contrast-target\\n        summary: \\\"CoCoHaNeRe: 提出可微分 hard negative 机制用于代码搜索对比学习。其对 hard negative 机制的处理与 StructFuse 的发现形成关键对照——StructFuse 证明 true embedding-distance mining 即可持续提升性能。\\\"\\n        note: \\\"关键引用：StructFuse Claim 1 的 correction target。CoCoHaNeRe 论点是非可微 embedding negatives 学习'slow and ineffective'，StructFuse 证明用 true embedding distance mining 仍然有效。\\\"\\n\\n  # ==========================================================================\\n  # Category 3: Contrastive Learning for Code\\n  # ==========================================================================\\n  contrastive_code_learning:\\n    description: \\\"代码领域的对比学习方法，训练时利用代码特性构建正负样本\\\"\\n    papers:\\n\\n      - title: \\\"Contrastive Code Representation Learning\\\"\\n        authors: \\\"Paras Jain, Ajay Jain, Tianjun Zhang, Pieter Abbeel, Joseph Gonzalez, Ion Stoica\\\"\\n        venue: EMNLP\\n        year: 2021\\n        relation: background\\n        summary: \\\"ContraCode: 自监督对比预训练，通过编译器变换生成功能等价的程序变体，学习代码功能而非表面形式。\\\"\\n\\n      - title: \\\"CodeRetriever: A Large Scale Contrastive Pre-Training Method for Code Search\\\"\\n        authors: \\\"Xiaonan Li, Yeyun Gong, Yelong Shen, Xipeng Qiu, Hang Zhang, Bolun Yao, Weizhen Qi, Daxin Jiang, Weizhu Chen, Nan Duan\\\"\\n        venue: EMNLP\\n        year: 2022\\n        relation: background\\n        summary: \\\"结合 unimodal (code-code) 和 bimodal (code-text) 对比学习预训练代码表示，在 11 个代码搜索 benchmark 上 SOTA。\\\"\\n\\n      - title: \\\"Towards Learning (Dis)-Similarity of Source Code from Program Contrasts\\\"\\n        authors: \\\"Yangruibo Ding, Luca Buratti, Saurabh Pujar, Alessandro Morari, Baishakhi Ray, Saikat Chakraborty\\\"\\n        venue: \\\"ACL (Long Papers)\\\"\\n        year: 2022\\n        relation: background\\n        summary: \\\"利用程序结构和功能属性构建对比样本对，学习代码相似性/差异性表示。\\\"\\n\\n  # ==========================================================================\\n  # Category 4: Program Analysis for ML\\n  # ==========================================================================\\n  program_analysis_for_ml:\\n    description: \\\"静态分析辅助 ML，结构信息在代码表示学习中的应用\\\"\\n    papers:\\n\\n      - title: \\\"CodeQL: Semantic Code Analysis Engine\\\"\\n        authors: \\\"GitHub / Semmle\\\"\\n        venue: \\\"Tool (open-source)\\\"\\n        year: 2019\\n        relation: building-block\\n        summary: \\\"基于 Datalog 的代码查询引擎，支持 inter-procedural data-flow 分析。StructFuse 用它提取 scope-bounded data-flow graph。\\\"\\n\\n      - title: \\\"code2vec: Learning Distributed Representations of Code\\\"\\n        authors: \\\"Uri Alon, Meital Zilberstein, Omer Levy, Eran Yahav\\\"\\n        venue: POPL\\n        year: 2019\\n        relation: background\\n        summary: \\\"用 AST path 学习代码向量表示，首次大规模证明结构信息对代码表示学习的价值。\\\"\\n\\n      - title: \\\"code2seq: Generating Sequences from Structured Representations of Code\\\"\\n        authors: \\\"Uri Alon, Shaked Brody, Omer Levy, Eran Yahav\\\"\\n        venue: ICLR\\n        year: 2019\\n        relation: background\\n        summary: \\\"code2vec 的序列生成扩展，用 AST path attention 生成方法名摘要。\\\"\\n\\n      - title: \\\"Detecting Code Clones with Graph Neural Network and Flow-Augmented Abstract Syntax Tree\\\"\\n        authors: \\\"Wenhan Wang, Ge Li, Bo Ma, Xin Xia, Zhi Jin\\\"\\n        venue: SANER\\n        year: 2020\\n        relation: background\\n        summary: \\\"FA-AST: 用 data-flow 增强 AST 进行代码克隆检测，与 StructFuse 用 data-flow 做 hard negative 挖掘思路相关。\\\"\\n\\n      - title: \\\"GraphCodeBERT: Pre-training Code Representations with Data Flow\\\"\\n        authors: \\\"Daya Guo, Shuo Ren, Shuai Lu, Zhangyin Feng, Duyu Tang, Shujie Liu, Long Zhou, Nan Duan, Alexey Svyatkovskiy, Shengyu Fu, Michele Tufano, Shao Kun Deng, Colin Clement, Dawn Drain, Neel Sundaresan, Jian Yin, Daxin Jiang, Ming Zhou\\\"\\n        venue: ICLR\\n        year: 2021\\n        relation: background\\n        summary: \\\"在预训练中引入 data-flow edge，证明 data-flow 信息提升代码理解任务。StructFuse 的 insight 与此相关但用途不同（hard negative mining vs pre-training）。\\\"\\n\\n      - title: \\\"ARISE: A Repository-level Graph Representation and Toolset for Agentic Fault Localization and Program Repair\\\"\\n        authors: \\\"Shahd Seddik, Fatemeh Fard\\\"\\n        venue: arXiv\\n        year: 2025\\n        relation: contrast\\n        summary: \\\"用 multi-granularity program graph（含 intra-procedural def-use edges）辅助 LLM agent 做 fault localization。仅 intra-procedural + runtime tool calls，与 StructFuse 的 inter-procedural static mining 互补。\\\"\\n\\n  # ==========================================================================\\n  # Category 5: Code Embeddings / Code Search\\n  # ==========================================================================\\n  code_embeddings_search:\\n    description: \\\"代码嵌入模型和代码搜索方法\\\"\\n    papers:\\n\\n      - title: \\\"CodeSearchNet Challenge: Evaluating the State of Semantic Code Search\\\"\\n        authors: \\\"Hamel Husain, Ho-Hsiang Wu, Tiferet Gazit, Miltiadis Allamanis, Marc Brockschmidt\\\"\\n        venue: arXiv\\n        year: 2019\\n        relation: background\\n        summary: \\\"代码语义搜索 benchmark 和数据集，推动了代码嵌入模型的发展。\\\"\\n\\n      - title: \\\"CodeBERT: A Pre-Trained Model for Programming and Natural Languages\\\"\\n        authors: \\\"Zhangyin Feng, Daya Guo, Duyu Tang, Nan Duan, Xiaocheng Feng, Ming Gong, Lixin Zou, Bing Qin, Ting Liu, Daxin Jiang, Ming Zhou\\\"\\n        venue: \\\"EMNLP (Findings)\\\"\\n        year: 2020\\n        relation: background\\n        summary: \\\"首个编程语言-自然语言双模态预训练模型，代码嵌入的早期里程碑。\\\"\\n\\n      - title: \\\"UniXcoder: Unified Cross-Modal Pre-training for Code Representation\\\"\\n        authors: \\\"Daya Guo, Shuai Lu, Nan Duan, Yanlin Wang, Ming Zhou, Jian Yin\\\"\\n        venue: ACL\\n        year: 2022\\n        relation: background\\n        summary: \\\"统一跨模态代码预训练，在代码搜索等任务上取得 SOTA。\\\"\\n\\n      - title: \\\"StarCoder: May the Source Be with You!\\\"\\n        authors: \\\"Raymond Li, Loubna Ben Allal, et al. (BigCode)\\\"\\n        venue: TMLR\\n        year: 2023\\n        relation: building-block\\n        summary: \\\"大规模开源代码 LLM，StructFuse 用 StarCoder2-3B 作为对比学习检索器的 backbone 之一。\\\"\\n\\n      - title: \\\"Code Llama: Open Foundation Models for Code\\\"\\n        authors: \\\"Baptiste Roziere, Jonas Gehring, Fabian Gloeckle, et al. (Meta AI)\\\"\\n        venue: arXiv\\n        year: 2023\\n        relation: background\\n        summary: \\\"Meta 的代码大模型系列，基于 Llama 2 微调。\\\"\\n\\n      - title: \\\"Qwen2.5-Coder Technical Report\\\"\\n        authors: \\\"Binyuan Hui, Jian Yang, Zeyu Cui, et al. (Qwen Team, Alibaba)\\\"\\n        venue: arXiv\\n        year: 2024\\n        relation: building-block\\n        summary: \\\"Qwen 代码模型系列，StructFuse 用 Qwen2.5-Coder-3B 作为对比学习检索器的 backbone。\\\"\\n\\n      - title: \\\"DeepSeek-Coder: When the Large Language Model Meets Programming -- The Rise of Code Intelligence\\\"\\n        authors: \\\"Daya Guo, Qihao Zhu, Dejian Yang, Zhenda Xie, Kai Dong, Wentao Zhang, Guanting Chen, Xiao Bi, Yu Wu, Y.K. Li, Fuli Luo, Yingfei Xiong, Wenfeng Liang\\\"\\n        venue: arXiv\\n        year: 2024\\n        relation: background\\n        summary: \\\"开源代码 LLM 系列 (1.3B-33B)，project-level 代码训练 + 16K context + fill-in-the-blank 预训练。\\\"\\n\\n      - title: \\\"RepoFusion: Training Code Models to Understand Your Repository\\\"\\n        authors: \\\"Disha Shrivastava, Denis Kocetkov, Harm de Vries, Dzmitry Bahdanau, Torsten Scholak\\\"\\n        venue: arXiv\\n        year: 2023\\n        relation: background\\n        summary: \\\"训练代码模型融合多个 cross-file repo context 进行代码补全，小模型 + repo context 可匹配大模型性能。\\\"\\n\\n      - title: \\\"BM25\\\"\\n        authors: \\\"Stephen Robertson, Hugo Zaragoza\\\"\\n        venue: \\\"Foundations and Trends in Information Retrieval\\\"\\n        year: 2009\\n        relation: baseline\\n        summary: \\\"经典稀疏检索方法，StructFuse 的 baseline 之一。\\\"\\n\\n  # ==========================================================================\\n  # Category 6: Graph-Guided Code Navigation (Inference-Time)\\n  # ==========================================================================\\n  graph_guided_inference:\\n    description: \\\"推理时利用代码结构图辅助导航/检索的方法（与 StructFuse 的训练时结构信号互补）\\\"\\n    papers:\\n\\n      - title: \\\"LocAgent: Graph-Guided LLM Agents for Code Localization\\\"\\n        authors: \\\"Zhaoling Chen, Robert Tang, Gangda Deng, Fang Wu, Jialong Wu, Zhiwei Jiang, Viktor Prasanna, Arman Cohan, Xingyao Wang\\\"\\n        venue: ACL\\n        year: 2025\\n        relation: contrast\\n        summary: \\\"将代码库解析为有向异构图，LLM agent 通过 multi-hop 推理在图上导航做代码定位。推理时用结构图，StructFuse 训练时用。\\\"\\n\\n      - title: \\\"CodexGraph: Bridging Large Language Models and Code Repositories via Code Graph Databases\\\"\\n        authors: \\\"Xiangyan Liu, Bo Lan, Zhiyuan Hu, Yang Liu, Zhicheng Zhang, Fei Wang, Michael Qizhe Shieh, Wenmeng Zhou\\\"\\n        venue: NAACL\\n        year: 2025\\n        relation: contrast\\n        summary: \\\"将代码库索引到图数据库，LLM agent 通过 graph query 接口检索结构化上下文。\\\"\\n\\n      - title: \\\"RANGER: Repository-Level Agent for Graph-Enhanced Retrieval\\\"\\n        authors: \\\"Pratik Shah, Rajat Ghosh, Aryan Singhal, Debojyoti Dutta\\\"\\n        venue: arXiv\\n        year: 2025\\n        relation: contrast\\n        summary: \\\"构建 repo 知识图（含 variable-level 节点），dual-stage retrieval: Cypher lookup + MCTS-guided graph exploration。\\\"\\n\\n  # ==========================================================================\\n  # Category 7: Infrastructure / Tools\\n  # ==========================================================================\\n  infrastructure:\\n    description: \\\"StructFuse 依赖的核心基础设施和工具\\\"\\n    papers:\\n\\n      - title: \\\"Billion-Scale Similarity Search with GPUs\\\"\\n        authors: \\\"Jeff Johnson, Matthijs Douze, Herve Jegou\\\"\\n        venue: \\\"IEEE Transactions on Big Data\\\"\\n        year: 2021\\n        relation: building-block\\n        summary: \\\"FAISS: GPU 加速的大规模向量相似度搜索库，StructFuse 用于 ANN-based hard negative mining。\\\"\\n\\n      - title: \\\"Tree-sitter: An Incremental Parsing System for Programming Tools\\\"\\n        authors: \\\"Max Brunsfeld et al.\\\"\\n        venue: \\\"Software (Zenodo DOI: 10.5281/zenodo.13375512)\\\"\\n        year: 2018\\n        relation: building-block\\n        summary: \\\"增量解析库，高效构建和更新 concrete syntax trees。与 CodeQL 互补用于代码结构提取。\\\"\\n        note: \\\"软件工具，无正式论文。引用 Zenodo DOI 或 GitHub repo。\\\"\\n\", \"total_chars\": 15114, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "53a2c841-6dd6-4c5c-bd11-879b1ee031f1",
  "isSidechain": false,
  "promptId": "255fffc4-c17f-4b3b-8b5c-7a3031fdb918",
  "type": "user",
  "uuid": "77b89a87-eeab-4624-8bd7-5bb69d5907e2",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"path\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/literature_map.yaml\\\", \\\"content\\\": \\\"# StructFuse — Related Work Literature Map\\\\n# 最后更新: 2026-05-14\\\\n# 说明: 只收录已验证存在的论文。每篇均经 WebSearch 确认标题/venue/year。\\\\n# 总计: 37 entries (含 2 个软件工具引用)\\\\n\\\\ncategories:\\\\n\\\\n  # ==========================================================================\\\\n  # Category 1: Code Retrieval for Bug Fixing / SWE-bench Ecosystem\\\\n  # ==========================================================================\\\\n  code_retrieval_bug_fixing:\\\\n    description: \\\\\\\"SWE-bench 及相关 repo-level 自动修复系统中的代码检索方法\\\\\\\"\\\\n    papers:\\\\n\\\\n      - title: \\\\\\\"SWE-bench: Can Language Models Resolve Real-World GitHub Issues?\\\\\\\"\\\\n        authors: \\\\\\\"Carlos E. Jimenez, John Yang, Alexander Wettig, Shunyu Yao, Kexin Pei, Ofir Press, Karthik Narasimhan\\\\\\\"\\\\n        venue: ICLR\\\\n        year: 2024\\\\n        relation: baseline\\\\n        summary: \\\\\\\"从 GitHub issues 构建 repo-level bug fixing benchmark，成为自动修复领域标准评估集。\\\\\\\"\\\\n\\\\n      - title: \\\\\\\"SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering\\\\\\\"\\\\n        authors: \\\\\\\"John Yang, Carlos E. Jimenez, Alexander Wettig, Kilian Lieret, Shunyu Yao, Karthik Narasimhan, Ofir Press\\\\\\\"\\\\n        venue: NeurIPS\\\\n        year: 2024\\\\n        relation: competitor\\\\n        summary: \\\\\\\"基于 LLM agent 的交互式 bug fixing 系统，定义了 ACI 接口范式。\\\\\\\"\\\\n\\\\n      - title: \\\\\\\"AutoCodeRover: Autonomous Program Improvement\\\\\\\"\\\\n        authors: \\\\\\\"Yuntong Zhang, Haifeng Ruan, Zhiyu Fan, Abhik Roychoudhury\\\\\\\"\\\\n        venue: ISSTA\\\\n        year: 2024\\\\n        relation: competitor\\\\n        summary: \\\\\\\"结合代码搜索与 spectrum-based fault localization，利用程序分析缩小修复范围。\\\\\\\"\\\\n\\\\n      - title: \\\\\\\"Agentless: Demystifying LLM-based Software Engineering Agents\\\\\\\"\\\\n        authors: \\\\\\\"Chunqiu Steven Xia, Yinlin Deng, Soren Dunn, Lingming Zhang\\\\\\\"\\\\n        venue: arXiv\\\\n        year: 2024\\\\n        relation: competitor\\\\n        summary: \\\\\\\"无 agent 架构的 two-phase localize-then-repair 方法，在 SWE-bench 上取得强 baseline。\\\\\\\"\\\\n\\\\n      - title: \\\\\\\"SWE-smith: Scaling Data for Software Engineering Agents\\\\\\\"\\\\n        authors: \\\\\\\"John Yang, Kilian Lieret, Carlos E. Jimenez, Alexander Wettig, Kabir Khandpur, Yanzhe Zhang, Binyuan Hui, Ofir Press, Ludwig Schmidt, Diyi Yang\\\\\\\"\\\\n        venue: \\\\\\\"NeurIPS (Datasets & Benchmarks, Spotlight)\\\\\\\"\\\\n        year: 2025\\\\n        relation: building-block\\\\n        summary: \\\\\\\"自动从 GitHub 生成大规模 SWE-bench 风格训练数据，StructFuse 用其 repos 做 data-flow 提取。\\\\\\\"\\\\n\\\\n      - title: \\\\\\\"RepoBench: Benchmarking Repository-Level Code Auto-Completion Systems\\\\\\\"\\\\n        authors: \\\\\\\"Tianyang Liu, Canwen Xu, Julian McAuley\\\\\\\"\\\\n        venue: ICLR\\\\n        year: 2024\\\\n        relation: baseline\\\\n        summary: \\\\\\\"Repo-level 代码补全/检索 benchmark，含 RepoBench-R 检索子任务。\\\\\\\"\\\\n\\\\n      - title: \\\\\\\"SweRank: Software Issue Localization with Code Ranking\\\\\\\"\\\\n        authors: \\\\\\\"Revanth Gangi Reddy, Tarun Suresh, JaeHyeok Doo, Ye Liu, Xuan Phi Nguyen, Yingbo Zhou, Semih Yavuz, Caiming Xiong, Heng Ji, Shafiq Joty\\\\\\\"\\\\n        venue: arXiv\\\\n        year: 2025\\\\n        relation: competitor\\\\n        summary: \\\\\\\"Retrieve-and-rerank 框架用于 software issue localization，在 SWE-Bench-Lite 和 LocBench 上 SOTA，text-based retrieval baseline。\\\\\\\"\\\\n\\\\n      - title: \\\\\\\"SWE-Fixer: Training Open-Source LLMs for Effective and Efficient GitHub Issue Resolution\\\\\\\"\\\\n        authors: \\\\\\\"Chengxing Xie, Bowen Li, Chang Gao, He Du, Wai Lam, Difan Zou, Kai Chen\\\\\\\"\\\\n        venue: \\\\\\\"ACL (Findings)\\\\\\\"\\\\n        year: 2025\\\\n        relation: competitor\\\\n        summary: \\\\\\\"BM25 + LLM retriever 的 coarse-to-fine file retrieval pipeline，在 SWE-Bench Verified 上 30.2%。\\\\\\\"\\\\n\\\\n  # ==========================================================================\\\\n  # Category 2: Hard Negative Mining in Contrastive Learning\\\\n  # ==========================================================================\\\\n  hard_negative_mining:\\\\n    description: \\\\\\\"对比学习中 hard negative 挖掘策略，以及密集检索中的负样本选择\\\\\\\"\\\\n    papers:\\\\n\\\\n      - title: \\\\\\\"Dense Passage Retrieval for Open-Domain Question Answering\\\\\\\"\\\\n        authors: \\\\\\\"Vladimir Karpukhin, Barlas Oguz, Sewon Min, Patrick Lewis, Ledell Wu, Sergey Edunov, Danqi Chen, Wen-tau Yih\\\\\\\"\\\\n        venue: EMNLP\\\\n        year: 2020\\\\n        relation: background\\\\n        summary: \\\\\\\"DPR 开创了 in-batch negatives + BM25 hard negatives 的双塔检索范式。\\\\\\\"\\\\n\\\\n      - title: \\\\\\\"Approximate Nearest Neighbor Negative Contrastive Learning for Dense Text Retrieval\\\\\\\"\\\\n        authors: \\\\\\\"Lee Xiong, Chenyan Xiong, Ye Li, Kwok-Fung Tang, Jialin Liu, Paul Bennett, Junaid Ahmed, Arnold Overwijk\\\\\\\"\\\\n        venue: ICLR\\\\n        year: 2021\\\\n        relation: background\\\\n        summary: \\\\\\\"ANCE 用 ANN index 动态挖掘 embedding-distance hard negatives，StructFuse 的 baseline negative 策略之一。\\\\\\\"\\\\n\\\\n      - title: \\\\\\\"A Simple Framework for Contrastive Learning of Visual Representations\\\\\\\"\\\\n        authors: \\\\\\\"Ting Chen, Simon Kornblith, Mohammad Norouzi, Geoffrey Hinton\\\\\\\"\\\\n        venue: ICML\\\\n        year: 2020\\\\n        relation: background\\\\n        summary: \\\\\\\"SimCLR 视觉对比学习奠基工作，证明 hard negatives 和大 batch size 对对比学习的重要性。\\\\\\\"\\\\n\\\\n      - title: \\\\\\\"Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks\\\\\\\"\\\\n        authors: \\\\\\\"Nils Reimers, Iryna Gurevych\\\\\\\"\\\\n        venue: EMNLP\\\\n        year: 2019\\\\n        relation: background\\\\n        summary: \\\\\\\"Siamese/triplet 网络训练句子嵌入，StructFuse 的对比训练框架与其类似。\\\\\\\"\\\\n\\\\n      - title: \\\\\\\"Curriculum Learning for Dense Retrieval Distillation\\\\\\\"\\\\n        authors: \\\\\\\"Hansi Zeng, Hamed Zamani, Vishwa Vinay\\\\\\\"\\\\n        venue: \\\\\\\"SIGIR (Best Short Paper)\\\\\\\"\\\\n        year: 2022\\\\n        relation: background\\\\n        summary: \\\\\\\"CL-DRD: 课程学习式知识蒸馏用于密集检索，从粗粒度到细粒度逐步增加训练难度。\\\\\\\"\\\\n\\\\n      - title: \\\\\\\"Effective Hard Negative Mining for Contrastive Learning-Based Code Search\\\\\\\"\\\\n        authors: \\\\\\\"Fan Y., Li C., Ge J., Huang L., Luo B.\\\\\\\"\\\\n        venue: \\\\\\\"ACM TOSEM\\\\\\\"\\\\n        year: 2025\\\\n        relation: contrast-target\\\\n        summary: \\\\\\\"CoCoHaNeRe: 提出可微分 hard negative 机制用于代码搜索对比学习。其对 hard negative 机制的处理与 StructFuse 的发现形成关键对照——StructFuse 证明 true embedding-distance mining 即可持续提升性能。\\\\\\\"\\\\n        note: \\\\\\\"关键引用：StructFuse Claim 1 的 correction target。CoCoHaNeRe 论点是非可微 embedding negatives 学习'slow and ineffective'，StructFuse 证明用 true embedding distance mining 仍然有效。\\\\\\\"\\\\n\\\\n  # ==========================================================================\\\\n  # Category 3: Contrastive Learning for Code\\\\n  # ==========================================================================\\\\n  contrastive_code_learning:\\\\n    description: \\\\\\\"代码领域的对比学习方法，训练时利用代码特性构建正负样本\\\\\\\"\\\\n    papers:\\\\n\\\\n      - title: \\\\\\\"Contrastive Code Representation Learning\\\\\\\"\\\\n        authors: \\\\\\\"Paras Jain, Ajay Jain, Tianjun Zhang, Pieter Abbeel, Joseph Gonzalez, Ion Stoica\\\\\\\"\\\\n        venue: EMNLP\\\\n        year: 2021\\\\n        relation: background\\\\n        summary: \\\\\\\"ContraCode: 自监督对比预训练，通过编译器变换生成功能等价的程序变体，学习代码功能而非表面形式。\\\\\\\"\\\\n\\\\n      - title: \\\\\\\"CodeRetriever: A Large Scale Contrastive Pre-Training Method for Code Search\\\\\\\"\\\\n        authors: \\\\\\\"Xiaonan Li, Yeyun Gong, Yelong Shen, Xipeng Qiu, Hang Zhang, Bolun Yao, Weizhen Qi, Daxin Jiang, Weizhu Chen, Nan Duan\\\\\\\"\\\\n        venue: EMNLP\\\\n        year: 2022\\\\n        relation: background\\\\n        summary: \\\\\\\"结合 unimodal (code-code) 和 bimodal (code-text) 对比学习预训练代码表示，在 11 个代码搜索 benchmark 上 SOTA。\\\\\\\"\\\\n\\\\n      - title: \\\\\\\"Towards Learning (Dis)-Similarity of Source Code from Program Contrasts\\\\\\\"\\\\n        authors: \\\\\\\"Yangruibo Ding, Luca Buratti, Saurabh Pujar, Alessandro Morari, Baishakhi Ray, Saikat Chakraborty\\\\\\\"\\\\n        venue: \\\\\\\"ACL (Long Papers)\\\\\\\"\\\\n        year: 2022\\\\n        relation: background\\\\n        summary: \\\\\\\"利用程序结构和功能属性构建对比样本对，学习代码相似性/差异性表示。\\\\\\\"\\\\n\\\\n  # ==========================================================================\\\\n  # Category 4: Program Analysis for ML\\\\n  # ==========================================================================\\\\n  program_analysis_for_ml:\\\\n    description: \\\\\\\"静态分析辅助 ML，结构信息在代码表示学习中的应用\\\\\\\"\\\\n    papers:\\\\n\\\\n      - title: \\\\\\\"CodeQL: Semantic Code Analysis Engine\\\\\\\"\\\\n        authors: \\\\\\\"GitHub / Semmle\\\\\\\"\\\\n        venue: \\\\\\\"Tool (open-source)\\\\\\\"\\\\n        year: 2019\\\\n        relation: building-block\\\\n        summary: \\\\\\\"基于 Datalog 的代码查询引擎，支持 inter-procedural data-flow 分析。StructFuse 用它提取 scope-bounded data-flow graph。\\\\\\\"\\\\n\\\\n      - title: \\\\\\\"code2vec: Learning Distributed Representations of Code\\\\\\\"\\\\n        authors: \\\\\\\"Uri Alon, Meital Zilberstein, Omer Levy, Eran Yahav\\\\\\\"\\\\n        venue: POPL\\\\n        year: 2019\\\\n        relation: background\\\\n        summary: \\\\\\\"用 AST path 学习代码向量表示，首次大规模证明结构信息对代码表示学习的价值。\\\\\\\"\\\\n\\\\n      - title: \\\\\\\"code2seq: Generating Sequences from Structured Representations of Code\\\\\\\"\\\\n        authors: \\\\\\\"Uri Alon, Shaked Brody, Omer Levy, Eran Yahav\\\\\\\"\\\\n        venue: ICLR\\\\n        year: 2019\\\\n        relation: background\\\\n        summary: \\\\\\\"code2vec 的序列生成扩展，用 AST path attention 生成方法名摘要。\\\\\\\"\\\\n\\\\n      - title: \\\\\\\"Detecting Code Clones with Graph Neural Network and Flow-Augmented Abstract Syntax Tree\\\\\\\"\\\\n        authors: \\\\\\\"Wenhan Wang, Ge Li, Bo Ma, Xin Xia, Zhi Jin\\\\\\\"\\\\n        venue: SANER\\\\n        year: 2020\\\\n        relation: background\\\\n        summary: \\\\\\\"FA-AST: 用 data-flow 增强 AST 进行代码克隆检测，与 StructFuse 用 data-flow 做 hard negative 挖掘思路相关。\\\\\\\"\\\\n\\\\n      - title: \\\\\\\"GraphCodeBERT: Pre-training Code Representations with Data Flow\\\\\\\"\\\\n        authors: \\\\\\\"Daya Guo, Shuo Ren, Shuai Lu, Zhangyin Feng, Duyu Tang, Shujie Liu, Long Zhou, Nan Duan, Alexey Svyatkovskiy, Shengyu Fu, Michele Tufano, Shao Kun Deng, Colin Clement, Dawn Drain, Neel Sundaresan, Jian Yin, Daxin Jiang, Ming Zhou\\\\\\\"\\\\n        venue: ICLR\\\\n        year: 2021\\\\n        relation: background\\\\n        summary: \\\\\\\"在预训练中引入 data-flow edge，证明 data-flow 信息提升代码理解任务。StructFuse 的 insight 与此相关但用途不同（hard negative mining vs pre-training）。\\\\\\\"\\\\n\\\\n      - title: \\\\\\\"ARISE: A Repository-level Graph Representation and Toolset for Agentic Fault Localization and Program Repair\\\\\\\"\\\\n        authors: \\\\\\\"Shahd Seddik, Fatemeh Fard\\\\\\\"\\\\n        venue: arXiv\\\\n        year: 2025\\\\n        relation: contrast\\\\n        summary: \\\\\\\"用 multi-granularity program graph（含 intra-procedural def-use edges）辅助 LLM agent 做 fault localization。仅 intra-procedural + runtime tool calls，与 StructFuse 的 inter-procedural static mining 互补。\\\\\\\"\\\\n\\\\n  # ==========================================================================\\\\n  # Category 5: Code Embeddings / Code Search\\\\n  # ==========================================================================\\\\n  code_embeddings_search:\\\\n    description: \\\\\\\"代码嵌入模型和代码搜索方法\\\\\\\"\\\\n    papers:\\\\n\\\\n      - title: \\\\\\\"CodeSearchNet Challenge: Evaluating the State of Semantic Code Search\\\\\\\"\\\\n        authors: \\\\\\\"Hamel Husain, Ho-Hsiang Wu, Tiferet Gazit, Miltiadis Allamanis, Marc Brockschmidt\\\\\\\"\\\\n        venue: arXiv\\\\n        year: 2019\\\\n        relation: background\\\\n        summary: \\\\\\\"代码语义搜索 benchmark 和数据集，推动了代码嵌入模型的发展。\\\\\\\"\\\\n\\\\n      - title: \\\\\\\"CodeBERT: A Pre-Trained Model for Programming and Natural Languages\\\\\\\"\\\\n        authors: \\\\\\\"Zhangyin Feng, Daya Guo, Duyu Tang, Nan Duan, Xiaocheng Feng, Ming Gong, Lixin Zou, Bing Qin, Ting Liu, Daxin Jiang, Ming Zhou\\\\\\\"\\\\n        venue: \\\\\\\"EMNLP (Findings)\\\\\\\"\\\\n        year: 2020\\\\n        relation: background\\\\n        summary: \\\\\\\"首个编程语言-自然语言双模态预训练模型，代码嵌入的早期里程碑。\\\\\\\"\\\\n\\\\n      - title: \\\\\\\"UniXcoder: Unified Cross-Modal Pre-training for Code Representation\\\\\\\"\\\\n        authors: \\\\\\\"Daya Guo, Shuai Lu, Nan Duan, Yanlin Wang, Ming Zhou, Jian Yin\\\\\\\"\\\\n        venue: ACL\\\\n        year: 2022\\\\n        relation: background\\\\n        summary: \\\\\\\"统一跨模态代码预训练，在代码搜索等任务上取得 SOTA。\\\\\\\"\\\\n\\\\n      - title: \\\\\\\"StarCoder: May the Source Be with You!\\\\\\\"\\\\n        authors: \\\\\\\"Raymond Li, Loubna Ben Allal, et al. (BigCode)\\\\\\\"\\\\n        venue: TMLR\\\\n        year: 2023\\\\n        relation: building-block\\\\n        summary: \\\\\\\"大规模开源代码 LLM，StructFuse 用 StarCoder2-3B 作为对比学习检索器的 backbone 之一。\\\\\\\"\\\\n\\\\n      - title: \\\\\\\"Code Llama: Open Foundation Models for Code\\\\\\\"\\\\n        authors: \\\\\\\"Baptiste Roziere, Jonas Gehring, Fabian Gloeckle, et al. (Meta AI)\\\\\\\"\\\\n        venue: arXiv\\\\n        year: 2023\\\\n        relation: background\\\\n        summary: \\\\\\\"Meta 的代码大模型系列，基于 Llama 2 微调。\\\\\\\"\\\\n\\\\n      - title: \\\\\\\"Qwen2.5-Coder Technical Report\\\\\\\"\\\\n        authors: \\\\\\\"Binyuan Hui, Jian Yang, Zeyu Cui, et al. (Qwen Team, Alibaba)\\\\\\\"\\\\n        venue: arXiv\\\\n        year: 2024\\\\n        relation: building-block\\\\n        summary: \\\\\\\"Qwen 代码模型系列，StructFuse 用 Qwen2.5-Coder-3B 作为对比学习检索器的 backbone。\\\\\\\"\\\\n\\\\n      - title: \\\\\\\"DeepSeek-Coder: When the Large Language Model Meets Programming -- The Rise of Code Intelligence\\\\\\\"\\\\n        authors: \\\\\\\"Daya Guo, Qihao Zhu, Dejian Yang, Zhenda Xie, Kai Dong, Wentao Zhang, Guanting Chen, Xiao Bi, Yu Wu, Y.K. Li, Fuli Luo, Yingfei Xiong, Wenfeng Liang\\\\\\\"\\\\n        venue: arXiv\\\\n        year: 2024\\\\n        relation: background\\\\n        summary: \\\\\\\"开源代码 LLM 系列 (1.3B-33B)，project-level 代码训练 + 16K context + fill-in-the-blank 预训练。\\\\\\\"\\\\n\\\\n      - title: \\\\\\\"RepoFusion: Training Code Models to Understand Your Repository\\\\\\\"\\\\n        authors: \\\\\\\"Disha Shrivastava, Denis Kocetkov, Harm de Vries, Dzmitry Bahdanau, Torsten Scholak\\\\\\\"\\\\n        venue: arXiv\\\\n        year: 2023\\\\n        relation: background\\\\n        summary: \\\\\\\"训练代码模型融合多个 cross-file repo context 进行代码补全，小模型 + repo context 可匹配大模型性能。\\\\\\\"\\\\n\\\\n      - title: \\\\\\\"BM25\\\\\\\"\\\\n        authors: \\\\\\\"Stephen Robertson, Hugo Zaragoza\\\\\\\"\\\\n        venue: \\\\\\\"Foundations and Trends in Information Retrieval\\\\\\\"\\\\n        year: 2009\\\\n        relation: baseline\\\\n        summary: \\\\\\\"经典稀疏检索方法，StructFuse 的 baseline 之一。\\\\\\\"\\\\n\\\\n  # ==========================================================================\\\\n  # Category 6: Graph-Guided Code Navigation (Inference-Time)\\\\n  # ==========================================================================\\\\n  graph_guided_inference:\\\\n    description: \\\\\\\"推理时利用代码结构图辅助导航/检索的方法（与 StructFuse 的训练时结构信号互补）\\\\\\\"\\\\n    papers:\\\\n\\\\n      - title: \\\\\\\"LocAgent: Graph-Guided LLM Agents for Code Localization\\\\\\\"\\\\n        authors: \\\\\\\"Zhaoling Chen, Robert Tang, Gangda Deng, Fang Wu, Jialong Wu, Zhiwei Jiang, Viktor Prasanna, Arman Cohan, Xingyao Wang\\\\\\\"\\\\n        venue: ACL\\\\n        year: 2025\\\\n        relation: contrast\\\\n        summary: \\\\\\\"将代码库解析为有向异构图，LLM agent 通过 multi-hop 推理在图上导航做代码定位。推理时用结构图，StructFuse 训练时用。\\\\\\\"\\\\n\\\\n      - title: \\\\\\\"CodexGraph: Bridging Large Language Models and Code Repositories via Code Graph Databases\\\\\\\"\\\\n        authors: \\\\\\\"Xiangyan Liu, Bo Lan, Zhiyuan Hu, Yang Liu, Zhicheng Zhang, Fei Wang, Michael Qizhe Shieh, Wenmeng Zhou\\\\\\\"\\\\n        venue: NAACL\\\\n        year: 2025\\\\n        relation: contrast\\\\n        summary: \\\\\\\"将代码库索引到图数据库，LLM agent 通过 graph query 接口检索结构化上下文。\\\\\\\"\\\\n\\\\n      - title: \\\\\\\"RANGER: Repository-Level Agent for Graph-Enhanced Retrieval\\\\\\\"\\\\n        authors: \\\\\\\"Pratik Shah, Rajat Ghosh, Aryan Singhal, Debojyoti Dutta\\\\\\\"\\\\n        venue: arXiv\\\\n        year: 2025\\\\n        relation: contrast\\\\n        summary: \\\\\\\"构建 repo 知识图（含 variable-level 节点），dual-stage retrieval: Cypher lookup + MCTS-guided graph exploration。\\\\\\\"\\\\n\\\\n  # ==========================================================================\\\\n  # Category 7: Infrastructure / Tools\\\\n  # ==========================================================================\\\\n  infrastructure:\\\\n    description: \\\\\\\"StructFuse 依赖的核心基础设施和工具\\\\\\\"\\\\n    papers:\\\\n\\\\n      - title: \\\\\\\"Billion-Scale Similarity Search with GPUs\\\\\\\"\\\\n        authors: \\\\\\\"Jeff Johnson, Matthijs Douze, Herve Jegou\\\\\\\"\\\\n        venue: \\\\\\\"IEEE Transactions on Big Data\\\\\\\"\\\\n        year: 2021\\\\n        relation: building-block\\\\n        summary: \\\\\\\"FAISS: GPU 加速的大规模向量相似度搜索库，StructFuse 用于 ANN-based hard negative mining。\\\\\\\"\\\\n\\\\n      - title: \\\\\\\"Tree-sitter: An Incremental Parsing System for Programming Tools\\\\\\\"\\\\n        authors: \\\\\\\"Max Brunsfeld et al.\\\\\\\"\\\\n        venue: \\\\\\\"Software (Zenodo DOI: 10.5281/zenodo.13375512)\\\\\\\"\\\\n        year: 2018\\\\n        relation: building-block\\\\n        summary: \\\\\\\"增量解析库，高效构建和更新 concrete syntax trees。与 CodeQL 互补用于代码结构提取。\\\\\\\"\\\\n        note: \\\\\\\"软件工具，无正式论文。引用 Zenodo DOI 或 GitHub repo。\\\\\\\"\\\\n\\\", \\\"total_chars\\\": 15114, \\\"truncated\\\": false}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/literature_map.yaml\", \"content\": \"# StructFuse — Related Work Literature Map\\n# 最后更新: 2026-05-14\\n# 说明: 只收录已验证存在的论文。每篇均经 WebSearch 确认标题/venue/year。\\n# 总计: 37 entries (含 2 个软件工具引用)\\n\\ncategories:\\n\\n  # ==========================================================================\\n  # Category 1: Code Retrieval for Bug Fixing / SWE-bench Ecosystem\\n  # ==========================================================================\\n  code_retrieval_bug_fixing:\\n    description: \\\"SWE-bench 及相关 repo-level 自动修复系统中的代码检索方法\\\"\\n    papers:\\n\\n      - title: \\\"SWE-bench: Can Language Models Resolve Real-World GitHub Issues?\\\"\\n        authors: \\\"Carlos E. Jimenez, John Yang, Alexander Wettig, Shunyu Yao, Kexin Pei, Ofir Press, Karthik Narasimhan\\\"\\n        venue: ICLR\\n        year: 2024\\n        relation: baseline\\n        summary: \\\"从 GitHub issues 构建 repo-level bug fixing benchmark，成为自动修复领域标准评估集。\\\"\\n\\n      - title: \\\"SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering\\\"\\n        authors: \\\"John Yang, Carlos E. Jimenez, Alexander Wettig, Kilian Lieret, Shunyu Yao, Karthik Narasimhan, Ofir Press\\\"\\n        venue: NeurIPS\\n        year: 2024\\n        relation: competitor\\n        summary: \\\"基于 LLM agent 的交互式 bug fixing 系统，定义了 ACI 接口范式。\\\"\\n\\n      - title: \\\"AutoCodeRover: Autonomous Program Improvement\\\"\\n        authors: \\\"Yuntong Zhang, Haifeng Ruan, Zhiyu Fan, Abhik Roychoudhury\\\"\\n        venue: ISSTA\\n        year: 2024\\n        relation: competitor\\n        summary: \\\"结合代码搜索与 spectrum-based fault localization，利用程序分析缩小修复范围。\\\"\\n\\n      - title: \\\"Agentless: Demystifying LLM-based Software Engineering Agents\\\"\\n        authors: \\\"Chunqiu Steven Xia, Yinlin Deng, Soren Dunn, Lingming Zhang\\\"\\n        venue: arXiv\\n        year: 2024\\n        relation: competitor\\n        summary: \\\"无 agent 架构的 two-phase localize-then-repair 方法，在 SWE-bench 上取得强 baseline。\\\"\\n\\n      - title: \\\"SWE-smith: Scaling Data for Software Engineering Agents\\\"\\n        authors: \\\"John Yang, Kilian Lieret, Carlos E. Jimenez, Alexander Wettig, Kabir Khandpur, Yanzhe Zhang, Binyuan Hui, Ofir Press, Ludwig Schmidt, Diyi Yang\\\"\\n        venue: \\\"NeurIPS (Datasets & Benchmarks, Spotlight)\\\"\\n        year: 2025\\n        relation: building-block\\n        summary: \\\"自动从 GitHub 生成大规模 SWE-bench 风格训练数据，StructFuse 用其 repos 做 data-flow 提取。\\\"\\n\\n      - title: \\\"RepoBench: Benchmarking Repository-Level Code Auto-Completion Systems\\\"\\n        authors: \\\"Tianyang Liu, Canwen Xu, Julian McAuley\\\"\\n        venue: ICLR\\n        year: 2024\\n        relation: baseline\\n        summary: \\\"Repo-level 代码补全/检索 benchmark，含 RepoBench-R 检索子任务。\\\"\\n\\n      - title: \\\"SweRank: Software Issue Localization with Code Ranking\\\"\\n        authors: \\\"Revanth Gangi Reddy, Tarun Suresh, JaeHyeok Doo, Ye Liu, Xuan Phi Nguyen, Yingbo Zhou, Semih Yavuz, Caiming Xiong, Heng Ji, Shafiq Joty\\\"\\n        venue: arXiv\\n        year: 2025\\n        relation: competitor\\n        summary: \\\"Retrieve-and-rerank 框架用于 software issue localization，在 SWE-Bench-Lite 和 LocBench 上 SOTA，text-based retrieval baseline。\\\"\\n\\n      - title: \\\"SWE-Fixer: Training Open-Source LLMs for Effective and Efficient GitHub Issue Resolution\\\"\\n        authors: \\\"Chengxing Xie, Bowen Li, Chang Gao, He Du, Wai Lam, Difan Zou, Kai Chen\\\"\\n        venue: \\\"ACL (Findings)\\\"\\n        year: 2025\\n        relation: competitor\\n        summary: \\\"BM25 + LLM retriever 的 coarse-to-fine file retrieval pipeline，在 SWE-Bench Verified 上 30.2%。\\\"\\n\\n  # ==========================================================================\\n  # Category 2: Hard Negative Mining in Contrastive Learning\\n  # ==========================================================================\\n  hard_negative_mining:\\n    description: \\\"对比学习中 hard negative 挖掘策略，以及密集检索中的负样本选择\\\"\\n    papers:\\n\\n      - title: \\\"Dense Passage Retrieval for Open-Domain Question Answering\\\"\\n        authors: \\\"Vladimir Karpukhin, Barlas Oguz, Sewon Min, Patrick Lewis, Ledell Wu, Sergey Edunov, Danqi Chen, Wen-tau Yih\\\"\\n        venue: EMNLP\\n        year: 2020\\n        relation: background\\n        summary: \\\"DPR 开创了 in-batch negatives + BM25 hard negatives 的双塔检索范式。\\\"\\n\\n      - title: \\\"Approximate Nearest Neighbor Negative Contrastive Learning for Dense Text Retrieval\\\"\\n        authors: \\\"Lee Xiong, Chenyan Xiong, Ye Li, Kwok-Fung Tang, Jialin Liu, Paul Bennett, Junaid Ahmed, Arnold Overwijk\\\"\\n        venue: ICLR\\n        year: 2021\\n        relation: background\\n        summary: \\\"ANCE 用 ANN index 动态挖掘 embedding-distance hard negatives，StructFuse 的 baseline negative 策略之一。\\\"\\n\\n      - title: \\\"A Simple Framework for Contrastive Learning of Visual Representations\\\"\\n        authors: \\\"Ting Chen, Simon Kornblith, Mohammad Norouzi, Geoffrey Hinton\\\"\\n        venue: ICML\\n        year: 2020\\n        relation: background\\n        summary: \\\"SimCLR 视觉对比学习奠基工作，证明 hard negatives 和大 batch size 对对比学习的重要性。\\\"\\n\\n      - title: \\\"Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks\\\"\\n        authors: \\\"Nils Reimers, Iryna Gurevych\\\"\\n        venue: EMNLP\\n        year: 2019\\n        relation: background\\n        summary: \\\"Siamese/triplet 网络训练句子嵌入，StructFuse 的对比训练框架与其类似。\\\"\\n\\n      - title: \\\"Curriculum Learning for Dense Retrieval Distillation\\\"\\n        authors: \\\"Hansi Zeng, Hamed Zamani, Vishwa Vinay\\\"\\n        venue: \\\"SIGIR (Best Short Paper)\\\"\\n        year: 2022\\n        relation: background\\n        summary: \\\"CL-DRD: 课程学习式知识蒸馏用于密集检索，从粗粒度到细粒度逐步增加训练难度。\\\"\\n\\n      - title: \\\"Effective Hard Negative Mining for Contrastive Learning-Based Code Search\\\"\\n        authors: \\\"Fan Y., Li C., Ge J., Huang L., Luo B.\\\"\\n        venue: \\\"ACM TOSEM\\\"\\n        year: 2025\\n        relation: contrast-target\\n        summary: \\\"CoCoHaNeRe: 提出可微分 hard negative 机制用于代码搜索对比学习。其对 hard negative 机制的处理与 StructFuse 的发现形成关键对照——StructFuse 证明 true embedding-distance mining 即可持续提升性能。\\\"\\n        note: \\\"关键引用：StructFuse Claim 1 的 correction target。CoCoHaNeRe 论点是非可微 embedding negatives 学习'slow and ineffective'，StructFuse 证明用 true embedding distance mining 仍然有效。\\\"\\n\\n  # ==========================================================================\\n  # Category 3: Contrastive Learning for Code\\n  # ==========================================================================\\n  contrastive_code_learning:\\n    description: \\\"代码领域的对比学习方法，训练时利用代码特性构建正负样本\\\"\\n    papers:\\n\\n      - title: \\\"Contrastive Code Representation Learning\\\"\\n        authors: \\\"Paras Jain, Ajay Jain, Tianjun Zhang, Pieter Abbeel, Joseph Gonzalez, Ion Stoica\\\"\\n        venue: EMNLP\\n        year: 2021\\n        relation: background\\n        summary: \\\"ContraCode: 自监督对比预训练，通过编译器变换生成功能等价的程序变体，学习代码功能而非表面形式。\\\"\\n\\n      - title: \\\"CodeRetriever: A Large Scale Contrastive Pre-Training Method for Code Search\\\"\\n        authors: \\\"Xiaonan Li, Yeyun Gong, Yelong Shen, Xipeng Qiu, Hang Zhang, Bolun Yao, Weizhen Qi, Daxin Jiang, Weizhu Chen, Nan Duan\\\"\\n        venue: EMNLP\\n        year: 2022\\n        relation: background\\n        summary: \\\"结合 unimodal (code-code) 和 bimodal (code-text) 对比学习预训练代码表示，在 11 个代码搜索 benchmark 上 SOTA。\\\"\\n\\n      - title: \\\"Towards Learning (Dis)-Similarity of Source Code from Program Contrasts\\\"\\n        authors: \\\"Yangruibo Ding, Luca Buratti, Saurabh Pujar, Alessandro Morari, Baishakhi Ray, Saikat Chakraborty\\\"\\n        venue: \\\"ACL (Long Papers)\\\"\\n        year: 2022\\n        relation: background\\n        summary: \\\"利用程序结构和功能属性构建对比样本对，学习代码相似性/差异性表示。\\\"\\n\\n  # ==========================================================================\\n  # Category 4: Program Analysis for ML\\n  # ==========================================================================\\n  program_analysis_for_ml:\\n    description: \\\"静态分析辅助 ML，结构信息在代码表示学习中的应用\\\"\\n    papers:\\n\\n      - title: \\\"CodeQL: Semantic Code Analysis Engine\\\"\\n        authors: \\\"GitHub / Semmle\\\"\\n        venue: \\\"Tool (open-source)\\\"\\n        year: 2019\\n        relation: building-block\\n        summary: \\\"基于 Datalog 的代码查询引擎，支持 inter-procedural data-flow 分析。StructFuse 用它提取 scope-bounded data-flow graph。\\\"\\n\\n      - title: \\\"code2vec: Learning Distributed Representations of Code\\\"\\n        authors: \\\"Uri Alon, Meital Zilberstein, Omer Levy, Eran Yahav\\\"\\n        venue: POPL\\n        year: 2019\\n        relation: background\\n        summary: \\\"用 AST path 学习代码向量表示，首次大规模证明结构信息对代码表示学习的价值。\\\"\\n\\n      - title: \\\"code2seq: Generating Sequences from Structured Representations of Code\\\"\\n        authors: \\\"Uri Alon, Shaked Brody, Omer Levy, Eran Yahav\\\"\\n        venue: ICLR\\n        year: 2019\\n        relation: background\\n        summary: \\\"code2vec 的序列生成扩展，用 AST path attention 生成方法名摘要。\\\"\\n\\n      - title: \\\"Detecting Code Clones with Graph Neural Network and Flow-Augmented Abstract Syntax Tree\\\"\\n        authors: \\\"Wenhan Wang, Ge Li, Bo Ma, Xin Xia, Zhi Jin\\\"\\n        venue: SANER\\n        year: 2020\\n        relation: background\\n        summary: \\\"FA-AST: 用 data-flow 增强 AST 进行代码克隆检测，与 StructFuse 用 data-flow 做 hard negative 挖掘思路相关。\\\"\\n\\n      - title: \\\"GraphCodeBERT: Pre-training Code Representations with Data Flow\\\"\\n        authors: \\\"Daya Guo, Shuo Ren, Shuai Lu, Zhangyin Feng, Duyu Tang, Shujie Liu, Long Zhou, Nan Duan, Alexey Svyatkovskiy, Shengyu Fu, Michele Tufano, Shao Kun Deng, Colin Clement, Dawn Drain, Neel Sundaresan, Jian Yin, Daxin Jiang, Ming Zhou\\\"\\n        venue: ICLR\\n        year: 2021\\n        relation: background\\n        summary: \\\"在预训练中引入 data-flow edge，证明 data-flow 信息提升代码理解任务。StructFuse 的 insight 与此相关但用途不同（hard negative mining vs pre-training）。\\\"\\n\\n      - title: \\\"ARISE: A Repository-level Graph Representation and Toolset for Agentic Fault Localization and Program Repair\\\"\\n        authors: \\\"Shahd Seddik, Fatemeh Fard\\\"\\n        venue: arXiv\\n        year: 2025\\n        relation: contrast\\n        summary: \\\"用 multi-granularity program graph（含 intra-procedural def-use edges）辅助 LLM agent 做 fault localization。仅 intra-procedural + runtime tool calls，与 StructFuse 的 inter-procedural static mining 互补。\\\"\\n\\n  # ==========================================================================\\n  # Category 5: Code Embeddings / Code Search\\n  # ==========================================================================\\n  code_embeddings_search:\\n    description: \\\"代码嵌入模型和代码搜索方法\\\"\\n    papers:\\n\\n      - title: \\\"CodeSearchNet Challenge: Evaluating the State of Semantic Code Search\\\"\\n        authors: \\\"Hamel Husain, Ho-Hsiang Wu, Tiferet Gazit, Miltiadis Allamanis, Marc Brockschmidt\\\"\\n        venue: arXiv\\n        year: 2019\\n        relation: background\\n        summary: \\\"代码语义搜索 benchmark 和数据集，推动了代码嵌入模型的发展。\\\"\\n\\n      - title: \\\"CodeBERT: A Pre-Trained Model for Programming and Natural Languages\\\"\\n        authors: \\\"Zhangyin Feng, Daya Guo, Duyu Tang, Nan Duan, Xiaocheng Feng, Ming Gong, Lixin Zou, Bing Qin, Ting Liu, Daxin Jiang, Ming Zhou\\\"\\n        venue: \\\"EMNLP (Findings)\\\"\\n        year: 2020\\n        relation: background\\n        summary: \\\"首个编程语言-自然语言双模态预训练模型，代码嵌入的早期里程碑。\\\"\\n\\n      - title: \\\"UniXcoder: Unified Cross-Modal Pre-training for Code Representation\\\"\\n        authors: \\\"Daya Guo, Shuai Lu, Nan Duan, Yanlin Wang, Ming Zhou, Jian Yin\\\"\\n        venue: ACL\\n        year: 2022\\n        relation: background\\n        summary: \\\"统一跨模态代码预训练，在代码搜索等任务上取得 SOTA。\\\"\\n\\n      - title: \\\"StarCoder: May the Source Be with You!\\\"\\n        authors: \\\"Raymond Li, Loubna Ben Allal, et al. (BigCode)\\\"\\n        venue: TMLR\\n        year: 2023\\n        relation: building-block\\n        summary: \\\"大规模开源代码 LLM，StructFuse 用 StarCoder2-3B 作为对比学习检索器的 backbone 之一。\\\"\\n\\n      - title: \\\"Code Llama: Open Foundation Models for Code\\\"\\n        authors: \\\"Baptiste Roziere, Jonas Gehring, Fabian Gloeckle, et al. (Meta AI)\\\"\\n        venue: arXiv\\n        year: 2023\\n        relation: background\\n        summary: \\\"Meta 的代码大模型系列，基于 Llama 2 微调。\\\"\\n\\n      - title: \\\"Qwen2.5-Coder Technical Report\\\"\\n        authors: \\\"Binyuan Hui, Jian Yang, Zeyu Cui, et al. (Qwen Team, Alibaba)\\\"\\n        venue: arXiv\\n        year: 2024\\n        relation: building-block\\n        summary: \\\"Qwen 代码模型系列，StructFuse 用 Qwen2.5-Coder-3B 作为对比学习检索器的 backbone。\\\"\\n\\n      - title: \\\"DeepSeek-Coder: When the Large Language Model Meets Programming -- The Rise of Code Intelligence\\\"\\n        authors: \\\"Daya Guo, Qihao Zhu, Dejian Yang, Zhenda Xie, Kai Dong, Wentao Zhang, Guanting Chen, Xiao Bi, Yu Wu, Y.K. Li, Fuli Luo, Yingfei Xiong, Wenfeng Liang\\\"\\n        venue: arXiv\\n        year: 2024\\n        relation: background\\n        summary: \\\"开源代码 LLM 系列 (1.3B-33B)，project-level 代码训练 + 16K context + fill-in-the-blank 预训练。\\\"\\n\\n      - title: \\\"RepoFusion: Training Code Models to Understand Your Repository\\\"\\n        authors: \\\"Disha Shrivastava, Denis Kocetkov, Harm de Vries, Dzmitry Bahdanau, Torsten Scholak\\\"\\n        venue: arXiv\\n        year: 2023\\n        relation: background\\n        summary: \\\"训练代码模型融合多个 cross-file repo context 进行代码补全，小模型 + repo context 可匹配大模型性能。\\\"\\n\\n      - title: \\\"BM25\\\"\\n        authors: \\\"Stephen Robertson, Hugo Zaragoza\\\"\\n        venue: \\\"Foundations and Trends in Information Retrieval\\\"\\n        year: 2009\\n        relation: baseline\\n        summary: \\\"经典稀疏检索方法，StructFuse 的 baseline 之一。\\\"\\n\\n  # ==========================================================================\\n  # Category 6: Graph-Guided Code Navigation (Inference-Time)\\n  # ==========================================================================\\n  graph_guided_inference:\\n    description: \\\"推理时利用代码结构图辅助导航/检索的方法（与 StructFuse 的训练时结构信号互补）\\\"\\n    papers:\\n\\n      - title: \\\"LocAgent: Graph-Guided LLM Agents for Code Localization\\\"\\n        authors: \\\"Zhaoling Chen, Robert Tang, Gangda Deng, Fang Wu, Jialong Wu, Zhiwei Jiang, Viktor Prasanna, Arman Cohan, Xingyao Wang\\\"\\n        venue: ACL\\n        year: 2025\\n        relation: contrast\\n        summary: \\\"将代码库解析为有向异构图，LLM agent 通过 multi-hop 推理在图上导航做代码定位。推理时用结构图，StructFuse 训练时用。\\\"\\n\\n      - title: \\\"CodexGraph: Bridging Large Language Models and Code Repositories via Code Graph Databases\\\"\\n        authors: \\\"Xiangyan Liu, Bo Lan, Zhiyuan Hu, Yang Liu, Zhicheng Zhang, Fei Wang, Michael Qizhe Shieh, Wenmeng Zhou\\\"\\n        venue: NAACL\\n        year: 2025\\n        relation: contrast\\n        summary: \\\"将代码库索引到图数据库，LLM agent 通过 graph query 接口检索结构化上下文。\\\"\\n\\n      - title: \\\"RANGER: Repository-Level Agent for Graph-Enhanced Retrieval\\\"\\n        authors: \\\"Pratik Shah, Rajat Ghosh, Aryan Singhal, Debojyoti Dutta\\\"\\n        venue: arXiv\\n        year: 2025\\n        relation: contrast\\n        summary: \\\"构建 repo 知识图（含 variable-level 节点），dual-stage retrieval: Cypher lookup + MCTS-guided graph exploration。\\\"\\n\\n  # ==========================================================================\\n  # Category 7: Infrastructure / Tools\\n  # ==========================================================================\\n  infrastructure:\\n    description: \\\"StructFuse 依赖的核心基础设施和工具\\\"\\n    papers:\\n\\n      - title: \\\"Billion-Scale Similarity Search with GPUs\\\"\\n        authors: \\\"Jeff Johnson, Matthijs Douze, Herve Jegou\\\"\\n        venue: \\\"IEEE Transactions on Big Data\\\"\\n        year: 2021\\n        relation: building-block\\n        summary: \\\"FAISS: GPU 加速的大规模向量相似度搜索库，StructFuse 用于 ANN-based hard negative mining。\\\"\\n\\n      - title: \\\"Tree-sitter: An Incremental Parsing System for Programming Tools\\\"\\n        authors: \\\"Max Brunsfeld et al.\\\"\\n        venue: \\\"Software (Zenodo DOI: 10.5281/zenodo.13375512)\\\"\\n        year: 2018\\n        relation: building-block\\n        summary: \\\"增量解析库，高效构建和更新 concrete syntax trees。与 CodeQL 互补用于代码结构提取。\\\"\\n        note: \\\"软件工具，无正式论文。引用 Zenodo DOI 或 GitHub repo。\\\"\\n\", \"total_chars\": 15114, \"truncated\": false}, \"error\": null, \"metadata\": {}}"
    }
  },
  "sourceToolAssistantUUID": "53a2c841-6dd6-4c5c-bd11-879b1ee031f1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "b1d97499-4652-4822-8fc5-dbdc566ceedc",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-14T21:31:55.211Z_

<details open><summary>🔧 Tool call — Read · `toolu_01FtYeotTPgK7kGzpbKZCsAE`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/discussion_v2.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "77b89a87-eeab-4624-8bd7-5bb69d5907e2",
  "isSidechain": false,
  "requestId": "req_011Cb3B9YFarLnzvZyLBdJHq",
  "type": "assistant",
  "uuid": "9b1ab078-c990-4cea-a41f-33742fe7060d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "b1d97499-4652-4822-8fc5-dbdc566ceedc",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0159wWsbkDUo7yK1B8HaNXhE",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2476,
      "cache_read_input_tokens": 23282,
      "output_tokens": 319,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2476,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 319,
          "cache_read_input_tokens": 23282,
          "cache_creation_input_tokens": 2476,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2476
          },
          "type": "message"
        }
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

_source line 17 · 2026-05-14T21:31:55.221Z_

<details><summary>↩ Tool result · `toolu_01FtYeotTPgK7kGzpbKZCsAE`</summary>

```text
1	# 5. Discussion
2	
3	## 5.1 Relationship to Inference-Time Graph Methods
4	
5	A growing body of work leverages code structure graphs at inference time to improve LLM-based software engineering.
6	CodexGraph (Liu et al., NAACL 2025) materializes a code property graph in a Neo4j database that LLM agents query via Cypher; RepoGraph (Ouyang et al., ICLR 2025) provides line-level code graph navigation as a plug-in for SE agents; LocAgent (Chen et al., ACL 2025) and RANGER (Shah et al., 2025) employ graph-guided multi-hop reasoning and MCTS-based traversal for fault localization and retrieval, respectively. GraphCoder (Liu et al., ASE 2024) and ARISE (Seddik & Fard, 2026) come closest to our work in incorporating data-flow information, but both are limited to intra-procedural scope.
7	
8	Table 5 summarizes the key dimensions of comparison. We highlight two axes along which StructFuse occupies a distinct position:
9	
10	**When structural information enters the pipeline.** Inference-time methods construct and query graphs per request, incurring latency proportional to graph complexity and—for agent-based systems—requiring multiple LLM calls per query. StructFuse amortizes all graph computation to training time: CodeQL extraction costs approximately 8.9 seconds per instance (~110 CPU-hours for 44K instances; Table 4), after which the trained encoder operates at standard embedding-lookup speed with zero graph overhead. For latency-sensitive, high-throughput retrieval scenarios, this cost model is substantially more favorable.
11	
12	**Depth of data-flow analysis.** Most inference-time graph methods use structural relations (call graphs, class hierarchies, import dependencies). GraphCoder incorporates control-flow and data-dependence graphs, and ARISE exposes statement-level def-use edges, but both operate within single procedures. StructFuse leverages CodeQL's bounded inter-procedural taint tracking (2-hop call-graph scope), capturing cross-function data-flow paths—e.g., a sanitizer that transforms data between a source and sink across call boundaries. This deeper semantic signal generates harder, more informative negatives than structural proximity alone.
13	
14	**Complementarity.** We emphasize that StructFuse and inference-time graph methods address different stages of the retrieval pipeline and are composable rather than competing. A StructFuse-trained encoder can serve as a first-stage retriever whose embeddings already encode data-flow semantics, reducing the search space for inference-time graph agents that perform targeted reranking. Conversely, systems like CodexGraph or LocAgent can refine StructFuse retrieval results through explicit graph navigation when maximum precision is required. The two paradigms are complementary: StructFuse internalizes general structural patterns during training, while inference-time methods provide case-specific structural reasoning during deployment.
15	
16	## 5.2 Representation Geometry as a Predictor of Strategy Effectiveness
17	
18	Our negative difficulty analysis (Section 4.4) reveals a practical insight: the pretrained encoder's representation geometry predicts whether structure-grounded negatives will provide benefit beyond embedding-distance mining.
19	
20	When the pretrained representation space is saturated—as observed for Qwen2.5-Coder-3B, where mean positive-pair cosine similarity reaches 0.986—the margin between positive and negative pairs is compressed (random margin = 0.074; embedding margin = 0.017). In this regime, all text-similarity-based negatives are clustered near the positive, and the encoder requires negatives drawn from an orthogonal signal dimension (structural disconnection) to learn meaningful discrimination. This explains the +0.8pp R@1 improvement from dataflow-aware negatives over random baselines for Qwen (Table 2).
21	
22	When the representation space has healthy separation—as observed for StarCoder2-3B (pos\_sim = 0.799, random margin = 0.194, 2.6× larger than Qwen)—embedding-distance mining alone provides a sufficient difficulty gradient, and dataflow negatives do not yield additional improvement (+1.6pp for embedding vs. random, but −0.5pp for dataflow vs. random; Table 2). The larger margins mean the encoder can still extract useful contrastive signal from text-similarity-based negatives without supplementary structural guidance.
23	
24	This interaction between representation geometry and strategy effectiveness has a practical implication: practitioners can compute pos\_sim on a held-out sample with their pretrained encoder (a single forward pass, requiring no training) to predict whether structure-grounded negatives are worth the extraction cost. We observe that pos\_sim > 0.98 serves as an approximate threshold above which structural negatives provide conditional benefit, though we note this threshold is derived from two encoder observations and should be validated more broadly.
25	
26	## 5.3 Limitations
27	
28	We identify several limitations of the current study that contextualize our findings:
29	
30	**Encoder scope.** Our experiments use two decoder-only 3B-parameter encoders (Qwen2.5-Coder-3B and StarCoder2-3B). While these models differ meaningfully in pretraining corpus and representation geometry—enabling our interaction analysis—generalizing to encoder-only architectures (e.g., CodeBERT), larger scales, or non-code domains requires further investigation.
31	
32	**Single task.** We evaluate on code retrieval with contrastive training. Whether structure-grounded negatives similarly benefit other code understanding tasks (fault localization, code summarization, clone detection) remains an open question, though the underlying principle—that inter-procedural data-flow provides an orthogonal signal to text similarity—is task-agnostic.
33	
34	**Language and tooling dependency.** Our pipeline relies on CodeQL for inter-procedural data-flow extraction and currently supports Python repositories only. Extending to other languages requires language-specific CodeQL queries, and the dependency on a commercial static analysis tool may limit reproducibility. We note that the methodology generalizes to any tool capable of inter-procedural data-flow analysis (e.g., Joern, Soot).
35	
36	**Static mining.** Our negative mining is performed once before training and remains fixed throughout. Dynamic re-mining—where negatives are refreshed each epoch using the current encoder's embeddings—could yield progressively harder negatives as the model improves. We do not evaluate this variant in the current work and acknowledge the static-vs.-dynamic mining confound as a limitation. We plan to address this in future revisions.
37	
38	**Structural data coverage.** CodeQL successfully extracts data-flow information for 36% of instances across 123 repositories (93.9% repo coverage; Table 4). The remaining instances fall back to embedding-distance negatives. While our results demonstrate that even partial structural coverage yields measurable improvements, higher extraction success rates would likely amplify the benefit.
39	
40	## 5.4 Future Work
41	
42	We identify three directions that follow naturally from our findings, while noting that each requires empirical validation before strong claims can be made:
43	
44	**Hybrid retrieval pipelines.** Integrating a StructFuse-trained encoder as the first-stage retriever within inference-time graph systems (e.g., CodexGraph, RANGER) could combine the efficiency of embedding-based retrieval with the precision of runtime graph navigation. Evaluating such pipelines on end-to-end benchmarks like SWE-bench would quantify the practical value of this complementarity.
45	
46	**Representation-guided strategy selection.** Our observation that pos\_sim predicts strategy effectiveness suggests an automated protocol: given a new encoder, compute representation geometry statistics on a calibration set, then select the appropriate negative mining strategy without exhaustive ablation. Validating this protocol across a wider range of encoders and tasks is a natural next step.
47	
48	**Extension to dynamic and multi-lingual settings.** Adapting the pipeline to dynamically re-mine negatives during training, and extending CodeQL queries to languages beyond Python, would address two of our current limitations. For dynamic mining, the key design question is the re-mining frequency—epoch-level re-mining requires repeated CodeQL extraction, and the cost-benefit tradeoff depends on how quickly the encoder's embedding space evolves during training.
49	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9b1ab078-c990-4cea-a41f-33742fe7060d",
  "isSidechain": false,
  "promptId": "255fffc4-c17f-4b3b-8b5c-7a3031fdb918",
  "type": "user",
  "uuid": "18ab8136-efbf-46fb-afd1-d3611f6c3da4",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/discussion_v2.md",
      "content": "# 5. Discussion\n\n## 5.1 Relationship to Inference-Time Graph Methods\n\nA growing body of work leverages code structure graphs at inference time to improve LLM-based software engineering.\nCodexGraph (Liu et al., NAACL 2025) materializes a code property graph in a Neo4j database that LLM agents query via Cypher; RepoGraph (Ouyang et al., ICLR 2025) provides line-level code graph navigation as a plug-in for SE agents; LocAgent (Chen et al., ACL 2025) and RANGER (Shah et al., 2025) employ graph-guided multi-hop reasoning and MCTS-based traversal for fault localization and retrieval, respectively. GraphCoder (Liu et al., ASE 2024) and ARISE (Seddik & Fard, 2026) come closest to our work in incorporating data-flow information, but both are limited to intra-procedural scope.\n\nTable 5 summarizes the key dimensions of comparison. We highlight two axes along which StructFuse occupies a distinct position:\n\n**When structural information enters the pipeline.** Inference-time methods construct and query graphs per request, incurring latency proportional to graph complexity and—for agent-based systems—requiring multiple LLM calls per query. StructFuse amortizes all graph computation to training time: CodeQL extraction costs approximately 8.9 seconds per instance (~110 CPU-hours for 44K instances; Table 4), after which the trained encoder operates at standard embedding-lookup speed with zero graph overhead. For latency-sensitive, high-throughput retrieval scenarios, this cost model is substantially more favorable.\n\n**Depth of data-flow analysis.** Most inference-time graph methods use structural relations (call graphs, class hierarchies, import dependencies). GraphCoder incorporates control-flow and data-dependence graphs, and ARISE exposes statement-level def-use edges, but both operate within single procedures. StructFuse leverages CodeQL's bounded inter-procedural taint tracking (2-hop call-graph scope), capturing cross-function data-flow paths—e.g., a sanitizer that transforms data between a source and sink across call boundaries. This deeper semantic signal generates harder, more informative negatives than structural proximity alone.\n\n**Complementarity.** We emphasize that StructFuse and inference-time graph methods address different stages of the retrieval pipeline and are composable rather than competing. A StructFuse-trained encoder can serve as a first-stage retriever whose embeddings already encode data-flow semantics, reducing the search space for inference-time graph agents that perform targeted reranking. Conversely, systems like CodexGraph or LocAgent can refine StructFuse retrieval results through explicit graph navigation when maximum precision is required. The two paradigms are complementary: StructFuse internalizes general structural patterns during training, while inference-time methods provide case-specific structural reasoning during deployment.\n\n## 5.2 Representation Geometry as a Predictor of Strategy Effectiveness\n\nOur negative difficulty analysis (Section 4.4) reveals a practical insight: the pretrained encoder's representation geometry predicts whether structure-grounded negatives will provide benefit beyond embedding-distance mining.\n\nWhen the pretrained representation space is saturated—as observed for Qwen2.5-Coder-3B, where mean positive-pair cosine similarity reaches 0.986—the margin between positive and negative pairs is compressed (random margin = 0.074; embedding margin = 0.017). In this regime, all text-similarity-based negatives are clustered near the positive, and the encoder requires negatives drawn from an orthogonal signal dimension (structural disconnection) to learn meaningful discrimination. This explains the +0.8pp R@1 improvement from dataflow-aware negatives over random baselines for Qwen (Table 2).\n\nWhen the representation space has healthy separation—as observed for StarCoder2-3B (pos\\_sim = 0.799, random margin = 0.194, 2.6× larger than Qwen)—embedding-distance mining alone provides a sufficient difficulty gradient, and dataflow negatives do not yield additional improvement (+1.6pp for embedding vs. random, but −0.5pp for dataflow vs. random; Table 2). The larger margins mean the encoder can still extract useful contrastive signal from text-similarity-based negatives without supplementary structural guidance.\n\nThis interaction between representation geometry and strategy effectiveness has a practical implication: practitioners can compute pos\\_sim on a held-out sample with their pretrained encoder (a single forward pass, requiring no training) to predict whether structure-grounded negatives are worth the extraction cost. We observe that pos\\_sim > 0.98 serves as an approximate threshold above which structural negatives provide conditional benefit, though we note this threshold is derived from two encoder observations and should be validated more broadly.\n\n## 5.3 Limitations\n\nWe identify several limitations of the current study that contextualize our findings:\n\n**Encoder scope.** Our experiments use two decoder-only 3B-parameter encoders (Qwen2.5-Coder-3B and StarCoder2-3B). While these models differ meaningfully in pretraining corpus and representation geometry—enabling our interaction analysis—generalizing to encoder-only architectures (e.g., CodeBERT), larger scales, or non-code domains requires further investigation.\n\n**Single task.** We evaluate on code retrieval with contrastive training. Whether structure-grounded negatives similarly benefit other code understanding tasks (fault localization, code summarization, clone detection) remains an open question, though the underlying principle—that inter-procedural data-flow provides an orthogonal signal to text similarity—is task-agnostic.\n\n**Language and tooling dependency.** Our pipeline relies on CodeQL for inter-procedural data-flow extraction and currently supports Python repositories only. Extending to other languages requires language-specific CodeQL queries, and the dependency on a commercial static analysis tool may limit reproducibility. We note that the methodology generalizes to any tool capable of inter-procedural data-flow analysis (e.g., Joern, Soot).\n\n**Static mining.** Our negative mining is performed once before training and remains fixed throughout. Dynamic re-mining—where negatives are refreshed each epoch using the current encoder's embeddings—could yield progressively harder negatives as the model improves. We do not evaluate this variant in the current work and acknowledge the static-vs.-dynamic mining confound as a limitation. We plan to address this in future revisions.\n\n**Structural data coverage.** CodeQL successfully extracts data-flow information for 36% of instances across 123 repositories (93.9% repo coverage; Table 4). The remaining instances fall back to embedding-distance negatives. While our results demonstrate that even partial structural coverage yields measurable improvements, higher extraction success rates would likely amplify the benefit.\n\n## 5.4 Future Work\n\nWe identify three directions that follow naturally from our findings, while noting that each requires empirical validation before strong claims can be made:\n\n**Hybrid retrieval pipelines.** Integrating a StructFuse-trained encoder as the first-stage retriever within inference-time graph systems (e.g., CodexGraph, RANGER) could combine the efficiency of embedding-based retrieval with the precision of runtime graph navigation. Evaluating such pipelines on end-to-end benchmarks like SWE-bench would quantify the practical value of this complementarity.\n\n**Representation-guided strategy selection.** Our observation that pos\\_sim predicts strategy effectiveness suggests an automated protocol: given a new encoder, compute representation geometry statistics on a calibration set, then select the appropriate negative mining strategy without exhaustive ablation. Validating this protocol across a wider range of encoders and tasks is a natural next step.\n\n**Extension to dynamic and multi-lingual settings.** Adapting the pipeline to dynamically re-mine negatives during training, and extending CodeQL queries to languages beyond Python, would address two of our current limitations. For dynamic mining, the key design question is the re-mining frequency—epoch-level re-mining requires repeated CodeQL extraction, and the cost-benefit tradeoff depends on how quickly the encoder's embedding space evolves during training.\n",
      "numLines": 49,
      "startLine": 1,
      "totalLines": 49
    }
  },
  "sourceToolAssistantUUID": "9b1ab078-c990-4cea-a41f-33742fe7060d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "b1d97499-4652-4822-8fc5-dbdc566ceedc",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-14T21:31:55.703Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_01RedUJhKfAesGLSS4NnDZEw`</summary>

```json
{
  "project": "structfuse-context",
  "filters": {
    "exp_id": "plan_017_literature"
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
  "parentUuid": "18ab8136-efbf-46fb-afd1-d3611f6c3da4",
  "isSidechain": false,
  "requestId": "req_011Cb3B9YFarLnzvZyLBdJHq",
  "type": "assistant",
  "uuid": "ad502d9d-43d3-4fd5-87e7-1afeaf08bb46",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "b1d97499-4652-4822-8fc5-dbdc566ceedc",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0159wWsbkDUo7yK1B8HaNXhE",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2476,
      "cache_read_input_tokens": 23282,
      "output_tokens": 319,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2476,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 319,
          "cache_read_input_tokens": 23282,
          "cache_creation_input_tokens": 2476,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2476
          },
          "type": "message"
        }
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
  "leafUuid": "ad502d9d-43d3-4fd5-87e7-1afeaf08bb46",
  "sessionId": "b1d97499-4652-4822-8fc5-dbdc566ceedc"
}
```

---

### Runtime record

_source line 20_

```json
{
  "type": "ai-title",
  "aiTitle": "Fix literature reference consistency issues",
  "sessionId": "b1d97499-4652-4822-8fc5-dbdc566ceedc"
}
```

---

### Tool result

_source line 21 · 2026-05-14T21:31:55.825Z_

<details><summary>↩ Tool result · `toolu_01RedUJhKfAesGLSS4NnDZEw`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.1016}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ad502d9d-43d3-4fd5-87e7-1afeaf08bb46",
  "isSidechain": false,
  "promptId": "255fffc4-c17f-4b3b-8b5c-7a3031fdb918",
  "type": "user",
  "uuid": "c408028c-0959-42ee-9e6e-234f47fb604a",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"experiments\\\": {}, \\\"count\\\": 0, \\\"total\\\": 0, \\\"baseline\\\": null}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.1016}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.1016}}"
    }
  },
  "sourceToolAssistantUUID": "ad502d9d-43d3-4fd5-87e7-1afeaf08bb46",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "b1d97499-4652-4822-8fc5-dbdc566ceedc",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 22 · 2026-05-14T21:31:59.850Z_

<details><summary>Logged reasoning block</summary>

```text
The registry filter didn't return results. Let me search for the plan_017_literature entry without the filter, or try a different filter approach. Let me also start the web searches for RepoGraph, GraphCoder, and ARISE in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c408028c-0959-42ee-9e6e-234f47fb604a",
  "isSidechain": false,
  "requestId": "req_011Cb3B9xuuWHpBt93h9CBmU",
  "type": "assistant",
  "uuid": "25deb7d7-090a-422b-8ad5-a1917ee60367",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "b1d97499-4652-4822-8fc5-dbdc566ceedc",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CcDHjcV436JSRpZV9kkdu1",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8929,
      "cache_read_input_tokens": 25758,
      "output_tokens": 353,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 8929,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 353,
          "cache_read_input_tokens": 25758,
          "cache_creation_input_tokens": 8929,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 8929
          },
          "type": "message"
        }
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

_source line 23 · 2026-05-14T21:32:00.819Z_

Registry filter returned empty. Let me search for plan_017_literature and start web searches in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "25deb7d7-090a-422b-8ad5-a1917ee60367",
  "isSidechain": false,
  "requestId": "req_011Cb3B9xuuWHpBt93h9CBmU",
  "type": "assistant",
  "uuid": "4f4b9de7-27c4-465e-a973-f8a81e491124",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "b1d97499-4652-4822-8fc5-dbdc566ceedc",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CcDHjcV436JSRpZV9kkdu1",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8929,
      "cache_read_input_tokens": 25758,
      "output_tokens": 353,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 8929,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 353,
          "cache_read_input_tokens": 25758,
          "cache_creation_input_tokens": 8929,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 8929
          },
          "type": "message"
        }
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

_source line 24 · 2026-05-14T21:32:01.404Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_01KYorBUb5wJHZKTYaT5g6Gh`</summary>

```json
{
  "project": "structfuse-context",
  "limit": 50,
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
  "parentUuid": "4f4b9de7-27c4-465e-a973-f8a81e491124",
  "isSidechain": false,
  "requestId": "req_011Cb3B9xuuWHpBt93h9CBmU",
  "type": "assistant",
  "uuid": "92f9db10-91c6-4b49-ab86-0265e6e87d50",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "b1d97499-4652-4822-8fc5-dbdc566ceedc",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CcDHjcV436JSRpZV9kkdu1",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8929,
      "cache_read_input_tokens": 25758,
      "output_tokens": 353,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 8929,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 353,
          "cache_read_input_tokens": 25758,
          "cache_creation_input_tokens": 8929,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 8929
          },
          "type": "message"
        }
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

_source line 25 · 2026-05-14T21:32:02.359Z_

<details><summary>↩ Tool result · `toolu_01KYorBUb5wJHZKTYaT5g6Gh`</summary>

```text
&lt;persisted-output>
Output too large (51.8KB). Full output saved to: /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-5-projects-structfuse-context/b1d97499-4652-4822-8fc5-dbdc566ceedc/tool-results/toolu_01KYorBUb5wJHZKTYaT5g6Gh.txt

Preview (first 2KB):
{"result":"{\"success\": true, \"data\": {\"experiments\": {\"m1_reextract_v2\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-13T20:00:20.578Z\", \"updated_at\": \"2026-05-14T21:18:48.643Z\", \"hypothesis\": \"M1 重提取 v2：恢复 28,276 个因运行时瞬态文件系统故障失败的 instances（82 repos）。CodeQL pack 已修复，端到端测试通过。预期将训练数据从 15,897 提升至 ~44,173。D022 批准。\", \"parent\": \"m1_extraction\", \"spec\": {\"command\": \"bash scripts/rerun_m1_failed.sh (4 CPU workers, CodeQL 2-hop, pack installed)\", \"server\": \"bjb1-42106\", \"data_path\": \"/root/autodl-tmp/structfuse/full_m1_data/\", \"data_count\": 28276, \"model_name\": \"N/A (CodeQL extraction)\", \"seed\": \"N/A\", \"log_path\": \"/root/runs/structfuse-context/m1_reextract_v2.log\", \"checkpoint_source\": \"rerun of m1_extraction failed instances (v2, CodeQL fixed)\", \"eval_data\": \"N/A\"}, \"notes\": \"M1 重提取 v2：CodeQL pack 已修复，端到端测试通过。28,276 instances / 82 repo groups / 4 workers 并行。启动 2026-05-14 03:59 CST。[诊断 07:06 CST] 活跃运行中，~15/82 groups 完成，2,469 次 call_graph 查询成功，预计还需 ~13-16h。仅前 4 个旧 repo（furl/pyasn1/feedparser/python-docx）复用 v1 旧 DB 有 18 次降级 WARNING，04:02 之后零失败。产出写入 all.jsonl（追加模式）。磁盘 97GB 可用。[Director 决策 Session 8] 即使数据量增至 ~44K，不重跑 M2（ARR May 25 DDL 不允许再加 4-5 天重训）。处理方式：(1) post-M2 完成后如有 GPU 空档，跑 1-seed pilot (Qwen, embedding, 新数据) 对比当前 M2 baseline; (2) 论文中作为 scalability/data efficiency 讨论点; (3) 全量重训留 camera-ready。[进度检查 2026-05-15 05:05 CST] 80.8% 完成（22,842/28,276），0 ERROR，速率 ~560/hr，处理中大 repo：mozilla__bleach/sqlfluff/conan-io/Project-MONAI。产出为单独 .json 文件，尚未合并 all.jsonl。预计 ~15:00 CST May 15 完成。\", \"metrics\": {\"checked_at\": \"2026-05-15T05:15Z\", \"process\": \"alive (CPU, 4 workers)\", \"started\": \"2026-05-14T03:59Z\", \"elapsed_hours\": 25, \"total_instances\": 28276, \"repo_groups\": 82, \"output_json_files\": 40225, \"all_jsonl_lines\": 44173, \"active_repos\": {\"sqlfluff/sqlfluff\": \"250/1272\", \"mozilla/bleach\": \"350/455\", \"conan-io/conan\": \"450/972\", \"Project-MONAI/MONAI\": \"150/524\"
...
&lt;/persisted-output>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "92f9db10-91c6-4b49-ab86-0265e6e87d50",
  "isSidechain": false,
  "promptId": "255fffc4-c17f-4b3b-8b5c-7a3031fdb918",
  "type": "user",
  "uuid": "559b8273-647c-408d-beb6-ef4861c15620",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"experiments\\\": {\\\"m1_reextract_v2\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-13T20:00:20.578Z\\\", \\\"updated_at\\\": \\\"2026-05-14T21:18:48.643Z\\\", \\\"hypothesis\\\": \\\"M1 重提取 v2：恢复 28,276 个因运行时瞬态文件系统故障失败的 instances（82 repos）。CodeQL pack 已修复，端到端测试通过。预期将训练数据从 15,897 提升至 ~44,173。D022 批准。\\\", \\\"parent\\\": \\\"m1_extraction\\\", \\\"spec\\\": {\\\"command\\\": \\\"bash scripts/rerun_m1_failed.sh (4 CPU workers, CodeQL 2-hop, pack installed)\\\", \\\"server\\\": \\\"bjb1-42106\\\", \\\"data_path\\\": \\\"/root/autodl-tmp/structfuse/full_m1_data/\\\", \\\"data_count\\\": 28276, \\\"model_name\\\": \\\"N/A (CodeQL extraction)\\\", \\\"seed\\\": \\\"N/A\\\", \\\"log_path\\\": \\\"/root/runs/structfuse-context/m1_reextract_v2.log\\\", \\\"checkpoint_source\\\": \\\"rerun of m1_extraction failed instances (v2, CodeQL fixed)\\\", \\\"eval_data\\\": \\\"N/A\\\"}, \\\"notes\\\": \\\"M1 重提取 v2：CodeQL pack 已修复，端到端测试通过。28,276 instances / 82 repo groups / 4 workers 并行。启动 2026-05-14 03:59 CST。[诊断 07:06 CST] 活跃运行中，~15/82 groups 完成，2,469 次 call_graph 查询成功，预计还需 ~13-16h。仅前 4 个旧 repo（furl/pyasn1/feedparser/python-docx）复用 v1 旧 DB 有 18 次降级 WARNING，04:02 之后零失败。产出写入 all.jsonl（追加模式）。磁盘 97GB 可用。[Director 决策 Session 8] 即使数据量增至 ~44K，不重跑 M2（ARR May 25 DDL 不允许再加 4-5 天重训）。处理方式：(1) post-M2 完成后如有 GPU 空档，跑 1-seed pilot (Qwen, embedding, 新数据) 对比当前 M2 baseline; (2) 论文中作为 scalability/data efficiency 讨论点; (3) 全量重训留 camera-ready。[进度检查 2026-05-15 05:05 CST] 80.8% 完成（22,842/28,276），0 ERROR，速率 ~560/hr，处理中大 repo：mozilla__bleach/sqlfluff/conan-io/Project-MONAI。产出为单独 .json 文件，尚未合并 all.jsonl。预计 ~15:00 CST May 15 完成。\\\", \\\"metrics\\\": {\\\"checked_at\\\": \\\"2026-05-15T05:15Z\\\", \\\"process\\\": \\\"alive (CPU, 4 workers)\\\", \\\"started\\\": \\\"2026-05-14T03:59Z\\\", \\\"elapsed_hours\\\": 25, \\\"total_instances\\\": 28276, \\\"repo_groups\\\": 82, \\\"output_json_files\\\": 40225, \\\"all_jsonl_lines\\\": 44173, \\\"active_repos\\\": {\\\"sqlfluff/sqlfluff\\\": \\\"250/1272\\\", \\\"mozilla/bleach\\\": \\\"350/455\\\", \\\"conan-io/conan\\\": \\\"450/972\\\", \\\"Project-MONAI/MONAI\\\": \\\"150/524\\\"}, \\\"estimated_total_hours\\\": 60, \\\"progress_pct_by_time\\\": \\\"~42%\\\", \\\"disk\\\": \\\"98GB free on /root/autodl-tmp\\\"}}, \\\"m2_full_starcoder_resumed\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-14T18:44:19.253Z\\\", \\\"updated_at\\\": \\\"2026-05-14T21:18:45.080Z\\\", \\\"hypothesis\\\": \\\"M2 StarCoder resumed: 继续 m2_full_starcoder 的 8 sequential runs (random×2 + embedding×3 + dataflow×3)。原实验因 cron timeout 标记为 failed，实际 PID 519791 正常运行。\\\", \\\"spec\\\": {\\\"command\\\": \\\"bash run_m2_full_starcoder_resume.sh (8 runs: random_s43→s44→embedding×3→dataflow×3)\\\", \\\"server\\\": \\\"bjb1-42106\\\", \\\"gpu\\\": [\\\"cuda:1\\\"], \\\"pid\\\": \\\"519791\\\", \\\"log_path\\\": \\\"/root/runs/structfuse-context/m2_full_starcoder.log\\\", \\\"data_path\\\": \\\"/root/autodl-tmp/structfuse/full_m2_training_data/\\\", \\\"data_count\\\": 11308, \\\"model_name\\\": \\\"StarCoder2-3B\\\", \\\"seed\\\": \\\"42,43,44\\\"}, \\\"parent\\\": \\\"m2_full_starcoder\\\", \\\"metrics\\\": {\\\"checked_at\\\": \\\"2026-05-15T05:15Z\\\", \\\"process\\\": \\\"alive (PID 519791, uptime 03:11:44)\\\", \\\"gpu\\\": \\\"cuda:1, 100% util, 53.9/97.9GB VRAM, 72°C\\\", \\\"current_subrun\\\": \\\"random_s43 (1/9)\\\", \\\"current_step\\\": \\\"550/1405 (epoch 1/2, ~20% of subrun)\\\", \\\"eval_at_500\\\": {\\\"R@1\\\": 0.4708, \\\"R@5\\\": 0.9469, \\\"val_loss\\\": 0.5279}, \\\"latest_loss\\\": 0.26, \\\"completed_subruns\\\": 0, \\\"remaining_subruns\\\": 8, \\\"eta_hours\\\": \\\"~65-70h\\\"}}, \\\"m2_full_qwen_continued\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-14T18:44:20.646Z\\\", \\\"updated_at\\\": \\\"2026-05-14T21:18:42.976Z\\\", \\\"hypothesis\\\": \\\"M2 Qwen continued: 继续 m2_full_qwen 的剩余 runs (random_s44 + embedding×3 + dataflow×3)。原实验 cron 在 s42 退出时自动设为 ANALYZING，但链仍在运行。\\\", \\\"spec\\\": {\\\"command\\\": \\\"bash run_m2_full_qwen.sh (chain: random_s44 running → embedding×3 → dataflow×3)\\\", \\\"server\\\": \\\"bjb1-42106\\\", \\\"gpu\\\": [\\\"cuda:0\\\"], \\\"pid\\\": \\\"337267\\\", \\\"log_path\\\": \\\"/root/runs/structfuse-context/m2_full_qwen.log\\\", \\\"data_path\\\": \\\"/root/autodl-tmp/structfuse/full_m2_training_data/\\\", \\\"data_count\\\": 11308, \\\"model_name\\\": \\\"Qwen2.5-Coder-3B\\\", \\\"seed\\\": \\\"42,43,44\\\"}, \\\"parent\\\": \\\"m2_full_qwen\\\", \\\"metrics\\\": {\\\"checked_at\\\": \\\"2026-05-15T05:15Z\\\", \\\"process\\\": \\\"alive (PID 337267, uptime 09:50:41)\\\", \\\"gpu\\\": \\\"cuda:0, 100% util, 51.5/97.9GB VRAM, 68°C\\\", \\\"current_subrun\\\": \\\"random_s44 (3/7)\\\", \\\"current_step\\\": \\\"850/1408 (epoch 1/2, ~30% of subrun)\\\", \\\"eval_at_500\\\": {\\\"R@1\\\": 0.6009, \\\"R@5\\\": 0.9583, \\\"val_loss\\\": 0.4252}, \\\"latest_loss\\\": 0.2837, \\\"completed_subruns\\\": {\\\"random_s42\\\": {\\\"best_R@1\\\": 0.5527, \\\"best_val_loss\\\": 0.4651}, \\\"random_s43\\\": {\\\"best_R@1\\\": 0.5554, \\\"best_val_loss\\\": 0.4476}}, \\\"remaining_subruns\\\": 5, \\\"eta_hours\\\": \\\"~40-45h\\\"}}, \\\"plan_005_stratified\\\": {\\\"status\\\": \\\"PREPARING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-14T20:36:16.738Z\\\", \\\"updated_at\\\": \\\"2026-05-14T21:07:45.324Z\\\", \\\"hypothesis\\\": \\\"Plan 005 分层分析：按 repo size/pool size/query-pos similarity/structural data availability/neg_difficulty quartile 5 维度分层评估 embedding vs random 策略差异，控制 pool_size confound。Claim 2 支撑实验。v2 结果为 ground truth（v1→v2 changelog 见 art_20260514_3008c4）。\\\", \\\"parent\\\": \\\"m2_full_qwen\\\", \\\"notes\\\": \\\"plan_id=plan_005. 分层评估脚本已完成全部修改（analyze_stratified.py）：(1) mock seed 确定性修复 (2) pool_size-controlled 策略对比（within-bin delta + weighted aggregate）(3) dataflow×pool_size 交叉分析（n<30 标记 underpowered）(4) checkpoint 发现逻辑已就绪（best_by_recall_at_1 / best / best_by_val_loss）。输出含 JSON + CSV + PDF。[2026-05-14 21:07] Worker 完成 5 项 Patch：(P1) reeval_checkpoint 重写为 batch encoding（query/positive/negatives 分组批量编码，tqdm 进度条，torch.no_grad + model.eval，pad_token 兜底）(P2) 新增 --batch-size 参数（默认 64）(P3) 调用处传递 batch_size (P4) 非 dry-run 自适应 sim bins（tercile 计算边界 + 重新分配 sim_bin）(P5) 输出 JSON 记录 similarity_bin_edges 和 batch_size。Dry-run 验证全部通过。真实评估待 M2 全部 checkpoint 就绪后执行。\\\", \\\"metrics\\\": {\\\"confound_analysis\\\": {\\\"data_validity\\\": \\\"⚠️ R@1 值为 dry-run mock predictions，不可引用。仅分布结构（cross_tabulation.csv）有效。\\\", \\\"valid_findings\\\": {\\\"distribution_structure\\\": \\\"rich-dataflow 99.3% 落在 large/xlarge repo，small repo 中完全不存在\\\", \\\"correlation\\\": {\\\"dataflow_edges_vs_repo_size_pearson_r\\\": 0.089}, \\\"cross_distribution\\\": {\\\"rich_in_large_xlarge_pct\\\": 99.3, \\\"rich_in_small\\\": 0, \\\"moderate_in_large_xlarge_pct\\\": 60.9}, \\\"implication\\\": \\\"真实评估必须控制 pool_size 和 repo_size 来隔离 dataflow richness 独立效应\\\"}, \\\"invalid_findings\\\": \\\"所有 R@1/R@5/MRR 值均为 mock predictions，策略排序 pattern 不可信，禁止引用\\\", \\\"artifacts_path\\\": \\\"/root/autodl-tmp/structfuse/artifacts/confound_analysis/\\\", \\\"valid_artifact\\\": \\\"cross_tabulation.csv\\\"}}}, \\\"plan_017_literature\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-14T18:49:00.477Z\\\", \\\"updated_at\\\": \\\"2026-05-14T18:49:39.557Z\\\", \\\"hypothesis\\\": \\\"Inference-time graph method comparison: 8 papers surveyed (CodexGraph, LocAgent, RANGER, GraphCoder, ARISE, RepoGraph, CodeGRAG, CodeRAG). Discussion v2 drafted, all citations verified. Conclusion: training-time vs inference-time complementary.\\\", \\\"spec\\\": {\\\"command\\\": \\\"analysis only (no training)\\\", \\\"server\\\": \\\"local\\\", \\\"data_path\\\": \\\"N/A\\\", \\\"data_count\\\": 0, \\\"model_name\\\": \\\"N/A\\\", \\\"seed\\\": \\\"N/A\\\", \\\"checkpoint_path\\\": \\\"N/A\\\", \\\"log_path\\\": \\\"N/A\\\"}, \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"papers_surveyed\\\": 8, \\\"citations_verified\\\": 8, \\\"discussion_draft\\\": \\\"artifacts/paper_drafts/discussion_v2.md\\\", \\\"artifact_id\\\": \\\"art_20260514_a2e1cd\\\"}, \\\"completed_at\\\": \\\"2026-05-14T18:49:39.557Z\\\"}, \\\"m2_full_starcoder\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-13T16:18:15.415Z\\\", \\\"updated_at\\\": \\\"2026-05-14T18:04:29.245Z\\\", \\\"hypothesis\\\": \\\"Full M2 StarCoder: 3 strategies × 3 seeds on full M1 data. Cross-encoder validation — if embedding > random holds for both Qwen and StarCoder, method is encoder-agnostic. Resolves plan_013 pilot negative (dataflow encoder-dependent).\\\", \\\"parent\\\": \\\"plan_013_starcoder\\\", \\\"spec\\\": {\\\"command\\\": \\\"bash -c \\\\\\\"cd /root/structfuse && bash run_m2_full_starcoder_resume.sh\\\\\\\"\\\", \\\"server\\\": \\\"bjb1-42106\\\", \\\"gpu\\\": [\\\"cuda:1\\\"], \\\"pid\\\": \\\"519791\\\", \\\"log_path\\\": \\\"~/runs/structfuse-context/m2_full_starcoder.log\\\", \\\"submitted_at\\\": \\\"2026-05-14T18:03:12.079Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\"}, \\\"notes\\\": \\\"Phase 1: 构建 StarCoder embedding negatives 完成。Phase 2: 9 runs 训练中。batch_size=8, num_negatives=7, epochs=3(s42)/2(s43+), lr=2e-5, eval_steps=500, no early_stopping。双 checkpoint: best + best_by_recall_at_1。Seeds: 42,43,44。[D026] s42 保持 3 epochs; s43/s44 及后续 runs 改为 2 epochs。[2026-05-15 02:02 CST] cuda:1 进程冲突修复并重新提交（PID 519791, timeout=144h）。Registry 状态 DONE(failed) 是旧 cron timeout 标记，实际正在运行 random_s43 [1/8]。新 cron 已注册监控 PID 519791。序列：random_s43→s44→(待插入bm25_s42)→embedding×3→dataflow×3。random_s42 结果：best R@1=0.4604 at step 2500, val_loss=0.6134 at step 1000。\\\", \\\"metrics\\\": {\\\"random_s42\\\": {\\\"epoch\\\": \\\"3/3\\\", \\\"current_step\\\": 4200, \\\"total_steps\\\": 4242, \\\"total_steps_per_epoch\\\": 1414, \\\"eval_500\\\": {\\\"val_loss\\\": 0.6194, \\\"recall_at_1\\\": 0.435, \\\"recall_at_5\\\": 0.905, \\\"recall_at_10\\\": 1}, \\\"eval_1000\\\": {\\\"val_loss\\\": 0.6134, \\\"recall_at_1\\\": 0.454, \\\"recall_at_5\\\": 0.92, \\\"recall_at_10\\\": 1}, \\\"eval_1500\\\": {\\\"val_loss\\\": 0.6528, \\\"recall_at_1\\\": 0.449, \\\"recall_at_5\\\": 0.906, \\\"recall_at_10\\\": 1}, \\\"eval_2000\\\": {\\\"val_loss\\\": 0.6698, \\\"recall_at_1\\\": 0.4456, \\\"recall_at_5\\\": 0.906, \\\"recall_at_10\\\": 1}, \\\"eval_2500\\\": {\\\"val_loss\\\": 0.6342, \\\"recall_at_1\\\": 0.4604, \\\"recall_at_5\\\": 0.9117, \\\"recall_at_10\\\": 1}, \\\"eval_3000\\\": {\\\"val_loss\\\": 0.6516, \\\"recall_at_1\\\": 0.4544, \\\"recall_at_5\\\": 0.9077, \\\"recall_at_10\\\": 1}, \\\"eval_3500\\\": {\\\"val_loss\\\": 0.6588, \\\"recall_at_1\\\": 0.4534, \\\"recall_at_5\\\": 0.9057, \\\"recall_at_10\\\": 1}, \\\"eval_4000\\\": {\\\"val_loss\\\": 0.6637, \\\"recall_at_1\\\": 0.4547, \\\"recall_at_5\\\": 0.9003, \\\"recall_at_10\\\": 1}, \\\"best_checkpoint\\\": \\\"step_1000 (val_loss=0.6134) / step_2500 (R@1=0.4604)\\\", \\\"conclusion\\\": \\\"effectively_complete (timeout at step 4200/4242, lr=7.8e-9, remaining 42 steps negligible)\\\"}, \\\"progress_snapshot\\\": \\\"2026-05-15T01:50 CST\\\"}, \\\"reproduce\\\": {\\\"finished_at\\\": \\\"2026-05-14T17:49:54.474Z\\\"}, \\\"failure_reason\\\": \\\"EXIT_CODE=124 (timeout — exceeded timeout_hours)\\\", \\\"conclusion\\\": \\\"failed\\\", \\\"completed_at\\\": \\\"2026-05-14T17:49:55.304Z\\\", \\\"extra\\\": {\\\"hook_events\\\": [{\\\"event\\\": \\\"on_failed\\\", \\\"action\\\": \\\"agent\\\", \\\"ts\\\": \\\"2026-05-14T17:49:56.408767+00:00\\\"}]}}, \\\"m2_full_qwen\\\": {\\\"status\\\": \\\"ANALYZING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-13T16:18:14.870Z\\\", \\\"updated_at\\\": \\\"2026-05-14T18:00:29.323Z\\\", \\\"hypothesis\\\": \\\"Full M2 Qwen: 3 strategies (random/embedding/dataflow) × 3 seeds on full M1 data (~11K train/seed). Statistical validation of pilot signal (embedding > random +2pp). Go/no-go for paper claims per D018.\\\", \\\"parent\\\": \\\"m2_embed_verify\\\", \\\"spec\\\": {\\\"command\\\": \\\"bash -c \\\\\\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/structfuse && bash run_m2_full_qwen.sh 2>&1 | tee /root/runs/structfuse-context/m2_full_qwen.log\\\\\\\"\\\", \\\"server\\\": \\\"bjb1-42106\\\", \\\"gpu\\\": [\\\"cuda:0\\\"], \\\"pid\\\": \\\"73544\\\", \\\"log_path\\\": \\\"~/runs/structfuse-context/m2_full_qwen.log\\\", \\\"submitted_at\\\": \\\"2026-05-13T17:39:30.757Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\"}, \\\"notes\\\": \\\"Full M2 go/no-go: 3 strategies (random, embedding_distance, dataflow_aware) × 3 seeds (42, 43, 44) = 9 runs sequential on cuda:0. Config: lr=2e-5, batch_size=8, eval_steps=500, num_negatives=7, max_seq_length=2048, warmup_ratio=0.1, weight_decay=0.01, temperature=0.07, LoRA r=16, gradient_checkpointing=True, proj_dim=256. Dual checkpoint: best_by_val_loss + best_by_recall_at_1. Train ~11.3K/seed, val ~3K/seed. [D026] s42 保持 3 epochs 提供完整 overfitting curve; s43/s44 及后续 runs 改为 2 epochs + early_stopping_patience=2。[STATUS 2026-05-15 00:19 CST] Registry 状态 ANALYZING 是 cron 自动设置（s42 进程退出触发），但实验实际仍在进行中。random_s43 在 cuda:0 正常运行，step 1200/2810 (43%)。eval@500 R@1=0.5357, eval@1000 R@1=0.5285 (early_stopping 1/2)。Best R@1=0.5357 at step 500。GPU 100% 利用率, 50.5/97.9GB VRAM。\\\", \\\"metrics\\\": {\\\"random_s42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"epoch\\\": \\\"3/3\\\", \\\"total_steps\\\": 4242, \\\"total_steps_per_epoch\\\": 1414, \\\"eval_500\\\": {\\\"val_loss\\\": 0.4869, \\\"recall_at_1\\\": 0.533, \\\"recall_at_5\\\": 0.954, \\\"recall_at_10\\\": 1}, \\\"eval_1000\\\": {\\\"val_loss\\\": 0.4651, \\\"recall_at_1\\\": 0.553, \\\"recall_at_5\\\": 0.959, \\\"recall_at_10\\\": 1}, \\\"eval_1500\\\": {\\\"val_loss\\\": 0.5365, \\\"recall_at_1\\\": 0.523, \\\"recall_at_5\\\": 0.955, \\\"recall_at_10\\\": 1}, \\\"eval_2000\\\": {\\\"val_loss\\\": 0.5162, \\\"recall_at_1\\\": 0.523, \\\"recall_at_5\\\": 0.954, \\\"recall_at_10\\\": 1}, \\\"eval_2500\\\": {\\\"val_loss\\\": 0.5264, \\\"recall_at_1\\\": 0.527, \\\"recall_at_5\\\": 0.956, \\\"recall_at_10\\\": 1}, \\\"eval_3000\\\": {\\\"val_loss\\\": 0.5406, \\\"recall_at_1\\\": 0.536, \\\"recall_at_5\\\": 0.956, \\\"recall_at_10\\\": 1}, \\\"best_checkpoint\\\": \\\"step_1000 (val_loss=0.4651, R@1=0.5527)\\\", \\\"conclusion\\\": \\\"Overfit after step 1000. Best R@1=0.5527, +1.7pp vs pilot (0.5357). Full data helps.\\\"}, \\\"random_s43\\\": {\\\"status\\\": \\\"DONE\\\", \\\"epoch\\\": \\\"early_stopped\\\", \\\"total_steps_per_epoch\\\": 1405, \\\"eval_500\\\": {\\\"val_loss\\\": 0.4476, \\\"recall_at_1\\\": 0.5357}, \\\"eval_1000\\\": {\\\"val_loss\\\": 0.4637, \\\"recall_at_1\\\": 0.5285}, \\\"eval_1500\\\": {\\\"recall_at_1\\\": 0.5554}, \\\"best_by_val_loss\\\": \\\"step 500 (val_loss=0.4476)\\\", \\\"best_by_recall_at_1\\\": \\\"step 1500 (R@1=0.5554)\\\", \\\"conclusion\\\": \\\"Early stopped at step 1500. Best R@1=0.5554, consistent with s42 (0.5527). val_loss and R@1 criterion diverge.\\\"}, \\\"random_s44\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"note\\\": \\\"Auto-started 01:58 CST, epoch 1/2, 1408 batches/epoch\\\"}, \\\"progress_snapshot\\\": \\\"2026-05-15T02:00 CST\\\"}, \\\"reproduce\\\": {\\\"finished_at\\\": \\\"2026-05-14T11:24:33.887Z\\\"}, \\\"extra\\\": {\\\"hook_events\\\": [{\\\"event\\\": \\\"on_complete\\\", \\\"action\\\": \\\"agent\\\", \\\"ts\\\": \\\"2026-05-14T11:24:35.375104+00:00\\\"}]}}, \\\"plan_018_bm25\\\": {\\\"status\\\": \\\"QUEUED\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-14T16:38:40.603Z\\\", \\\"updated_at\\\": \\\"2026-05-14T17:09:50.985Z\\\", \\\"hypothesis\\\": \\\"BM25 negative baseline: Dream 审稿三档一致认定缺 BM25 baseline 是论文最大结构性缺陷。Phase 1 (CPU): 对 M2 训练语料建 BM25 索引，挖掘 BM25 hard negatives，生成训练数据。Phase 2 (GPU): 用 BM25 negatives 训练 Qwen + StarCoder 各 1 seed，对比 R@1。\\\", \\\"parent\\\": \\\"m2_full_qwen\\\", \\\"notes\\\": \\\"Phase 1 (CPU) COMPLETE: BM25 negative mining 完成。3 seeds 数据生成，record counts 与其他策略完全一致，0 fallback。BM25 score 分布: mean=246.50, std=155.96。重叠率: BM25 vs embedding_distance ~87.1%, vs random ~76.2%, vs dataflow_aware ~71.8%。高 median=1.0 因小 repo 候选池≤50 文件导致策略完全重合，BM25 differentiation 主要在大 repo。脚本: /root/structfuse/scripts/mine_bm25_negatives.py。输出: /root/autodl-tmp/structfuse/full_m2_training_data/{train,val}_bm25_s{42,43,44}.jsonl。Phase 2 (GPU): 等 re-dream gate 通过 + M2 完成后训练。\\\", \\\"metrics\\\": {\\\"phase1_complete\\\": true, \\\"seed_42\\\": {\\\"train_records\\\": 11308, \\\"val_records\\\": 2980, \\\"train_size_mb\\\": 1280.8, \\\"val_size_mb\\\": 344.6}, \\\"seed_43\\\": {\\\"train_records\\\": 11236, \\\"val_records\\\": 3052, \\\"train_size_mb\\\": 1280.9, \\\"val_size_mb\\\": 316}, \\\"seed_44\\\": {\\\"train_records\\\": 11264, \\\"val_records\\\": 3024, \\\"train_size_mb\\\": 1347.1, \\\"val_size_mb\\\": 295.9}, \\\"bm25_score_dist\\\": {\\\"count\\\": 392954, \\\"mean\\\": 246.5, \\\"std\\\": 155.96, \\\"p25\\\": 128.38, \\\"p50\\\": 228.41, \\\"p75\\\": 347.85, \\\"max\\\": 2585.74}, \\\"overlap_overall\\\": {\\\"bm25_vs_embedding\\\": 0.871, \\\"bm25_vs_random\\\": 0.762, \\\"bm25_vs_dataflow\\\": 0.718, \\\"note\\\": \\\"k=50 full candidate overlap from mining worker\\\"}, \\\"overlap_stratified_top7_jaccard\\\": {\\\"small_lt50\\\": {\\\"repos\\\": 39, \\\"bm25_vs_embedding\\\": 0.668, \\\"bm25_vs_random\\\": 0.411, \\\"bm25_vs_dataflow\\\": 0.667}, \\\"medium_50_200\\\": {\\\"repos\\\": 29, \\\"bm25_vs_embedding\\\": 0.38, \\\"bm25_vs_random\\\": 0.067, \\\"bm25_vs_dataflow\\\": 0.363}, \\\"large_200plus\\\": {\\\"repos\\\": 15, \\\"bm25_vs_embedding\\\": 0.297, \\\"bm25_vs_random\\\": 0.007, \\\"bm25_vs_dataflow\\\": 0.405}, \\\"matched_queries\\\": 2920, \\\"total_queries\\\": 12290, \\\"note\\\": \\\"top-7 Jaccard on s42 matched queries only (24% match rate due to different train/val splits)\\\"}}}, \\\"plan_015_dynamic\\\": {\\\"status\\\": \\\"QUEUED\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-14T17:03:24.316Z\\\", \\\"updated_at\\\": \\\"2026-05-14T17:03:30.544Z\\\", \\\"hypothesis\\\": \\\"Dynamic negative mining (epoch-level re-mining): 每 epoch 重新用当前 encoder embedding 挖掘 negatives，验证 static mining 是否足够。缩减版：只跑 dynamic_ep × 1 seed (Qwen, s42)，~11h 单卡。若 dynamic ≈ static（预期 <1pp 差异），在 Limitation 段排除 confound。\\\", \\\"notes\\\": \\\"Director D031 缩减：原 44h → 11h 单卡。只跑 dynamic_ep × 1 seed (Qwen, s42)，跳过 dynamic_500。Post-M2 与 plan_003 并行（一卡 SWE-bench，一卡 dynamic_ep）。受 re-dream gate 约束。设计文档已由 Worker 完成。\\\"}, \\\"neg_difficulty_analysis\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-13T19:39:20.016Z\\\", \\\"updated_at\\\": \\\"2026-05-14T00:13:49.046Z\\\", \\\"hypothesis\\\": \\\"Negative difficulty distribution analysis: 用预训练 Qwen2.5-Coder-3B 和 StarCoder2-3B 计算 3 策略 (random/embedding/dataflow) 的 query-negative/positive cosine similarity，分析 pretrained representation separability 跨编码器差异。MAX_LENGTH=2048 匹配训练设置。\\\", \\\"notes\\\": \\\"128 vs 2048 token 对比完成（2026-05-14 05:54 CST）。Qwen pos_sim 在 2048t 下 0.9855（比 128t 的 0.9804 更高），确认 ceiling 为 Qwen 表征的结构性特征，非截断 artifact。StarCoder margin 2.6-4.1x Qwen（2048t）。核心结论：pretrained representation separability varies across encoders，跨两种 token 长度成立。数据源：128t → stats_v2.json，2048t → stats_v3_2048.json。\\\", \\\"metrics\\\": {\\\"qwen_128\\\": {\\\"random\\\": {\\\"pos_sim\\\": 0.9804, \\\"neg_sim\\\": 0.899, \\\"margin\\\": 0.0816, \\\"pct_positive_margin\\\": 77.8}, \\\"embedding_distance\\\": {\\\"pos_sim\\\": 0.9804, \\\"neg_sim\\\": 0.959, \\\"margin\\\": 0.0209, \\\"pct_positive_margin\\\": 60.7}, \\\"dataflow_aware\\\": {\\\"pos_sim\\\": 0.9805, \\\"neg_sim\\\": 0.95, \\\"margin\\\": 0.0309, \\\"pct_positive_margin\\\": 67.4}}, \\\"starcoder_128\\\": {\\\"random\\\": {\\\"pos_sim\\\": 0.757, \\\"neg_sim\\\": 0.553, \\\"margin\\\": 0.2039, \\\"pct_positive_margin\\\": 72.8}, \\\"embedding_distance\\\": {\\\"pos_sim\\\": 0.784, \\\"neg_sim\\\": 0.668, \\\"margin\\\": 0.1159, \\\"pct_positive_margin\\\": 59.2}, \\\"dataflow_aware\\\": {\\\"pos_sim\\\": 0.761, \\\"neg_sim\\\": 0.659, \\\"margin\\\": 0.1022, \\\"pct_positive_margin\\\": 62.8}}, \\\"qwen_2048\\\": {\\\"random\\\": {\\\"pos_sim\\\": 0.9855, \\\"neg_sim\\\": 0.9111, \\\"margin\\\": 0.0743, \\\"margin_std\\\": 0.2322, \\\"pct_positive_margin\\\": 81.8}, \\\"embedding_distance\\\": {\\\"pos_sim\\\": 0.9855, \\\"neg_sim\\\": 0.9685, \\\"margin\\\": 0.017, \\\"margin_std\\\": 0.114, \\\"pct_positive_margin\\\": 58.8}, \\\"dataflow_aware\\\": {\\\"pos_sim\\\": 0.9856, \\\"neg_sim\\\": 0.9563, \\\"margin\\\": 0.0293, \\\"margin_std\\\": 0.1407, \\\"pct_positive_margin\\\": 73.9}}, \\\"starcoder_2048\\\": {\\\"random\\\": {\\\"pos_sim\\\": 0.7985, \\\"neg_sim\\\": 0.6045, \\\"margin\\\": 0.194, \\\"margin_std\\\": 0.2788, \\\"pct_positive_margin\\\": 78}, \\\"embedding_distance\\\": {\\\"pos_sim\\\": 0.8079, \\\"neg_sim\\\": 0.7409, \\\"margin\\\": 0.067, \\\"margin_std\\\": 0.2056, \\\"pct_positive_margin\\\": 55}, \\\"dataflow_aware\\\": {\\\"pos_sim\\\": 0.8009, \\\"neg_sim\\\": 0.6818, \\\"margin\\\": 0.1192, \\\"margin_std\\\": 0.2264, \\\"pct_positive_margin\\\": 70.4}}, \\\"sc_qwen_margin_ratio_128\\\": {\\\"random\\\": 2.5, \\\"embedding_distance\\\": 5.54, \\\"dataflow_aware\\\": 3.3}, \\\"sc_qwen_margin_ratio_2048\\\": {\\\"random\\\": 2.61, \\\"embedding_distance\\\": 3.94, \\\"dataflow_aware\\\": 4.07}}, \\\"conclusion\\\": \\\"success\\\", \\\"spec\\\": {\\\"command\\\": \\\"python negative_difficulty_margin_v2.py (CPU analysis)\\\", \\\"server\\\": \\\"bjb1-42106\\\", \\\"data_path\\\": \\\"/root/autodl-tmp/structfuse/full_m2_data/\\\", \\\"data_count\\\": 11000, \\\"model_name\\\": \\\"Qwen2.5-Coder-3B + StarCoder2-3B (pretrained, no training)\\\", \\\"seed\\\": \\\"N/A\\\", \\\"checkpoint_path\\\": \\\"N/A (analysis only)\\\", \\\"log_path\\\": \\\"/root/autodl-tmp/structfuse/artifacts/negative_difficulty_stats_v3_2048.json\\\"}, \\\"completed_at\\\": \\\"2026-05-14T00:13:49.046Z\\\"}, \\\"m1_reextract\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-13T19:35:23.954Z\\\", \\\"updated_at\\\": \\\"2026-05-13T19:45:53.741Z\\\", \\\"hypothesis\\\": \\\"M1 重提取：恢复 28,276 个因运行时瞬态文件系统故障失败的 instances（82 repos）。预期将训练数据从 15,897 提升至 ~44,173。D022 批准。\\\", \\\"parent\\\": \\\"m1_extraction\\\", \\\"spec\\\": {\\\"command\\\": \\\"bash scripts/rerun_m1_failed.sh (4 CPU workers, CodeQL 2-hop)\\\", \\\"server\\\": \\\"bjb1-42106\\\", \\\"data_path\\\": \\\"/root/autodl-tmp/structfuse/m1_extraction/\\\", \\\"data_count\\\": 28276, \\\"model_name\\\": \\\"N/A (CodeQL extraction)\\\", \\\"seed\\\": \\\"N/A\\\", \\\"pid\\\": \\\"97358\\\", \\\"log_path\\\": \\\"/root/runs/structfuse-context/m1_rerun.log\\\", \\\"checkpoint_source\\\": \\\"rerun of m1_extraction failed instances\\\", \\\"eval_data\\\": \\\"N/A\\\", \\\"checkpoint_path\\\": \\\"N/A (failed, no output)\\\"}, \\\"conclusion\\\": \\\"failed\\\", \\\"notes\\\": \\\"CodeQL query 100% 失败（exit status 2）。根因：Worker 安装 CodeQL CLI 2.25.4 时未执行 `codeql pack install`，`codeql/python-all@7.1.0` 标准库 pack 缺失。修复命令：`cd /root/structfuse/extraction/codeql_queries && /opt/codeql/codeql pack install`。已 kill 进程 + tmux session。无新数据产出（all.jsonl 未受影响）。等 Director 确认后修复重跑。\\\", \\\"completed_at\\\": \\\"2026-05-13T19:44:09.115Z\\\"}, \\\"m1_extraction\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-12T21:00:02.300Z\\\", \\\"updated_at\\\": \\\"2026-05-13T19:26:13.901Z\\\", \\\"spec\\\": {\\\"command\\\": \\\"nohup bash scripts/run_m1_extraction.sh (8 CPU workers, CodeQL 2-hop)\\\", \\\"server\\\": \\\"cqa1-21977\\\", \\\"data_path\\\": \\\"/root/autodl-tmp/structfuse/m1_extraction/\\\", \\\"data_count\\\": 50869, \\\"model_name\\\": \\\"N/A (CodeQL extraction)\\\", \\\"seed\\\": \\\"N/A\\\", \\\"description\\\": \\\"M1: 全量 5K repos CodeQL 提取, 131 unique (repo,commit) groups, 50869 instances\\\"}, \\\"metrics\\\": {\\\"total_instances_attempted\\\": 44173, \\\"instances_skipped\\\": 6696, \\\"total_instances\\\": 50869, \\\"codeql_success\\\": 15133, \\\"beniget_fallback\\\": 764, \\\"extraction_failed\\\": 28276, \\\"structural_data_rate\\\": 0.36, \\\"repos_with_output\\\": 123, \\\"repos_total\\\": 131, \\\"repo_coverage\\\": 0.939, \\\"skip_clone_failed\\\": 5852, \\\"skip_checkout_failed\\\": 836, \\\"skip_stale_handle\\\": 8, \\\"elapsed_minutes\\\": 837.8, \\\"avg_time_per_instance_s\\\": 8.9, \\\"output_size_gb\\\": 6.6, \\\"disk_usage_gb\\\": 13, \\\"output_file\\\": \\\"all.jsonl\\\"}, \\\"notes\\\": \\\"[2026-05-13 19:25] COMPLETED. 837.8min, 123/131 repos (93.9%), 15,897/44,173 instances with structural data (36.0%), 6,696 skipped (clone/checkout). Output: all.jsonl 6.6GB. [2026-05-13 19:23 UPDATE] 28,276 buggy_file_not_found errors 经验证并非上游数据质量问题——10/10 抽查的文件在 repo 中全部存在。根因是运行时瞬态文件系统故障（CodeQL 并行 database creation 导致磁盘耗尽，锐截止模式）。这些 instances 可通过重跑恢复。D022: 准备重跑脚本中，等 Director 确认后执行。\\\", \\\"conclusion\\\": \\\"success\\\", \\\"checkpoint_path\\\": \\\"/root/autodl-tmp/structfuse/m1_extraction/all.jsonl\\\", \\\"log_path\\\": \\\"/tmp/m1_extraction.log\\\", \\\"completed_at\\\": \\\"2026-05-13T10:59:42.462Z\\\"}, \\\"plan_006_scalability\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-13T07:57:43.631Z\\\", \\\"updated_at\\\": \\\"2026-05-13T19:24:00.741Z\\\", \\\"spec\\\": {\\\"command\\\": \\\"M1 scalability statistics analysis (29/131 repos)\\\", \\\"server\\\": \\\"bjb1-42106\\\", \\\"data_path\\\": \\\"/root/autodl-tmp/structfuse/m1_extraction/\\\", \\\"data_count\\\": 8171, \\\"model_name\\\": \\\"N/A (CPU analysis)\\\", \\\"seed\\\": \\\"N/A\\\", \\\"description\\\": \\\"Plan 006: M1 extraction scalability stats - timeout rate, extraction time, coverage, Z% by repo size. Partial results from 29/131 repos.\\\", \\\"checkpoint_path\\\": \\\"N/A\\\", \\\"log_path\\\": \\\"N/A\\\"}, \\\"conclusion\\\": \\\"success\\\", \\\"completed_at\\\": \\\"2026-05-13T07:57:58.176Z\\\", \\\"notes\\\": \\\"[2026-05-13 19:23] 全量统计 + error 分析 + fuzzy match 验证完成。关键发现: (1) 0 timeout; (2) 28,276 error 全部 buggy_file_not_found，但 fuzzy match 验证发现文件实际都存在——根因是运行时瞬态文件系统故障（锐截止模式：每个 repo 内先成功后突然全部失败，extraction_time=0.0s），可能是 CodeQL 并行数据库创建导致磁盘空间耗尽; (3) 这些 instance 可通过重跑恢复（当前 resolve_file_in_repo 对全部样本返回正确路径）; (4) 结构数据率 34.3% 有望提升至接近 100%（若重跑成功）; (5) Z% 随 repo 规模上升 (XL median 96%). Artifacts: plan006_full_scalability.json, art_20260513_d262da (error patterns)\\\", \\\"hypothesis\\\": \\\"Claim 3: CodeQL bounded data-flow extraction scales to large repos with acceptable timeout rates and provides meaningful structural coverage (Z%) that increases with repo complexity\\\", \\\"metrics\\\": {\\\"repos\\\": 123, \\\"total_instances\\\": 44173, \\\"structural_data_rate\\\": 0.343, \\\"error_rate\\\": 0.64, \\\"zero_timeout_rate\\\": true, \\\"processing_time\\\": {\\\"mean_s\\\": 8.93, \\\"median_s\\\": 0, \\\"p95_s\\\": 31.95, \\\"max_s\\\": 633.68, \\\"total_hours\\\": 109.58}, \\\"by_tier\\\": {\\\"small_lt50\\\": {\\\"repos\\\": 1, \\\"instances\\\": 500, \\\"error_rate\\\": 0.054, \\\"struct_rate\\\": 0.81, \\\"z_pct_mean\\\": 0.284, \\\"z_pct_median\\\": 0}, \\\"medium_50_200\\\": {\\\"repos\\\": 17, \\\"instances\\\": 4096, \\\"error_rate\\\": 0.485, \\\"struct_rate\\\": 0.472, \\\"z_pct_mean\\\": 0.444, \\\"z_pct_median\\\": 0.5}, \\\"large_200_500\\\": {\\\"repos\\\": 40, \\\"instances\\\": 13628, \\\"error_rate\\\": 0.639, \\\"struct_rate\\\": 0.343, \\\"z_pct_mean\\\": 0.604, \\\"z_pct_median\\\": 0.857}, \\\"xlarge_500plus\\\": {\\\"repos\\\": 29, \\\"instances\\\": 25949, \\\"error_rate\\\": 0.676, \\\"struct_rate\\\": 0.314, \\\"z_pct_mean\\\": 0.812, \\\"z_pct_median\\\": 0.96}}, \\\"instance_distribution\\\": {\\\"lt10\\\": 1, \\\"10_50\\\": 17, \\\"50_200\\\": 36, \\\"200_500\\\": 40, \\\"500plus\\\": 29}, \\\"artifact\\\": \\\"plan006_full_scalability.json\\\"}}, \\\"plan_013_starcoder\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-13T05:09:14.885Z\\\", \\\"updated_at\\\": \\\"2026-05-13T18:09:54.153Z\\\", \\\"hypothesis\\\": \\\"Architecture generalization: validate StructFuse with StarCoder2-3B encoder (vs Qwen2.5-Coder-3B in m2_embed_verify). If both encoders show same strategy ranking → method is encoder-agnostic, strengthening the core claim. Key differentiator for best→accept at Dream.\\\", \\\"spec\\\": {\\\"command\\\": \\\"bash -c \\\\\\\"bash /root/structfuse/run_plan013_starcoder.sh\\\\\\\"\\\", \\\"server\\\": \\\"bjb1-42106\\\", \\\"gpu\\\": [\\\"cuda:0\\\"], \\\"pid\\\": \\\"23798\\\", \\\"log_path\\\": \\\"~/runs/structfuse-context/plan_013_starcoder.log\\\", \\\"submitted_at\\\": \\\"2026-05-13T05:26:21.946Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\", \\\"data_path\\\": \\\"/root/autodl-tmp/structfuse/m2_embed_verify_data/\\\", \\\"data_count\\\": 3282, \\\"model_name\\\": \\\"bigcode/starcoder2-3b\\\", \\\"seed\\\": 42, \\\"wall_clock_seconds\\\": 35338.2, \\\"gpu_hours\\\": 9.82}, \\\"notes\\\": \\\"[2026-05-13 16:00] ALL 3 STRATEGIES DONE. Ranking: embedding (R@1=0.5078) > random (0.4922) > dataflow (0.4869). Embedding vs random: +1.6pp (consistent with Qwen). Dataflow vs random: -0.5pp (DIFFERS from Qwen where dataflow > random +0.8pp). Hypothesis NEGATIVE: strategy ranking NOT identical across encoders. Embedding > random is encoder-agnostic, dataflow position is encoder-dependent. Log: /root/runs/faith-evidence-ie/plan_013_starcoder.log. Cron misreported EXIT_CODE=129 but all strategies completed (confirmed via log extraction worker).\\\", \\\"metrics\\\": {\\\"random\\\": {\\\"status\\\": \\\"DONE\\\", \\\"best_val_loss\\\": 0.5113, \\\"best_recall@1\\\": 0.4922, \\\"best_recall@5\\\": 0.98, \\\"best_recall@10\\\": 1, \\\"source\\\": \\\"/tmp/eval_random_s42.log (post-hoc eval, no in-training eval)\\\"}, \\\"embedding_distance\\\": {\\\"status\\\": \\\"DONE\\\", \\\"best_step\\\": 1000, \\\"best_val_loss\\\": 0.4816, \\\"best_recall@1\\\": 0.5078, \\\"best_recall@5\\\": 0.9843, \\\"best_recall@10\\\": 1, \\\"final_val_loss\\\": 0.506, \\\"final_recall@1\\\": 0.5174}, \\\"dataflow_aware\\\": {\\\"status\\\": \\\"DONE\\\", \\\"best_step\\\": 1000, \\\"best_val_loss\\\": 0.5255, \\\"best_recall@1\\\": 0.4869, \\\"best_recall@5\\\": 0.9695, \\\"best_recall@10\\\": 1, \\\"final_val_loss\\\": 0.5509, \\\"final_recall@1\\\": 0.5078}}, \\\"failure_reason\\\": \\\"\\\", \\\"conclusion\\\": \\\"negative\\\", \\\"completed_at\\\": \\\"2026-05-13T15:15:20.165Z\\\"}, \\\"m2_embed_verify\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-13T04:39:16.051Z\\\", \\\"updated_at\\\": \\\"2026-05-13T15:59:51.621Z\\\", \\\"hypothesis\\\": \\\"True embedding mining verification: compare Qwen2.5-Coder-3B cosine similarity negatives vs BM25 negatives on pilot data (24 repos). If true embedding negatives are harder → Claim 2 (structure-aware negatives improve retrieval) gets stronger evidence.\\\", \\\"parent\\\": \\\"m2_early_pilot\\\", \\\"spec\\\": {\\\"command\\\": \\\"bash -c \\\\\\\"bash /root/structfuse/run_m2_embed_verify.sh\\\\\\\"\\\", \\\"server\\\": \\\"bjb1-42106\\\", \\\"gpu\\\": [\\\"cuda:1\\\"], \\\"pid\\\": \\\"29290\\\", \\\"log_path\\\": \\\"~/runs/structfuse-context/m2_embed_verify.log\\\", \\\"submitted_at\\\": \\\"2026-05-13T06:37:00.822Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\", \\\"data_path\\\": \\\"/root/autodl-tmp/structfuse/m2_embed_verify_data/\\\", \\\"data_count\\\": 3282, \\\"model_name\\\": \\\"Qwen/Qwen2.5-Coder-3B\\\", \\\"seed\\\": 42, \\\"checkpoint_source\\\": \\\"training from scratch (not eval)\\\", \\\"eval_data\\\": \\\"N/A (training, not eval)\\\", \\\"wall_clock_seconds\\\": 31097.9, \\\"gpu_hours\\\": 8.64}, \\\"notes\\\": \\\"[2026-05-13 16:00] ALL 3 STRATEGIES DONE. Ranking: embedding (R@1=0.5557) > dataflow (0.5436) > random (0.5357). Embedding vs random: +2.0pp. Dataflow vs random: +0.8pp. All best at step 500, overfitting after. Hypothesis confirmed: true embedding negatives are harder → Claim 2 supported. Log: /root/runs/faith-evidence-ie/m2_embed_verify.log. Cron misreported EXIT_CODE=2 but all strategies completed successfully (confirmed via log extraction worker).\\\", \\\"metrics\\\": {\\\"random\\\": {\\\"status\\\": \\\"DONE\\\", \\\"best_step\\\": 500, \\\"best_val_loss\\\": 0.4834, \\\"best_recall@1\\\": 0.5357, \\\"best_recall@5\\\": 0.9808, \\\"best_recall@10\\\": 1, \\\"final_val_loss\\\": 0.5978, \\\"final_recall@1\\\": 0.5122}, \\\"embedding_distance\\\": {\\\"status\\\": \\\"DONE\\\", \\\"best_step\\\": 500, \\\"best_val_loss\\\": 0.4603, \\\"best_recall@1\\\": 0.5557, \\\"best_recall@5\\\": 0.9808, \\\"best_recall@10\\\": 1, \\\"final_val_loss\\\": 0.5935, \\\"final_recall@1\\\": 0.5209}, \\\"dataflow_aware\\\": {\\\"status\\\": \\\"DONE\\\", \\\"best_step\\\": 500, \\\"best_val_loss\\\": 0.5602, \\\"best_recall@1\\\": 0.5436, \\\"best_recall@5\\\": 0.9817, \\\"best_recall@10\\\": 1, \\\"final_val_loss\\\": 0.6201, \\\"final_recall@1\\\": 0.5287}}, \\\"failure_reason\\\": \\\"EXIT_CODE=2 (shell misuse / syntax)\\\", \\\"conclusion\\\": \\\"success\\\", \\\"completed_at\\\": \\\"2026-05-13T15:15:18.746Z\\\"}, \\\"mvp_p2b_contrastive_v2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-12T15:03:02.370Z\\\", \\\"updated_at\\\": \\\"2026-05-13T07:23:28.932Z\\\", \\\"spec\\\": {\\\"command\\\": \\\"bash scripts/run_p2b_all.sh (9 runs: 3 strategies × 3 seeds)\\\", \\\"server\\\": \\\"cqa1-21977\\\", \\\"gpu\\\": [\\\"cuda:4\\\"], \\\"pid\\\": \\\"132149\\\", \\\"data_path\\\": \\\"/root/structfuse/mvp_data/training_data/\\\", \\\"data_count\\\": 127, \\\"model_name\\\": \\\"Qwen2.5-Coder-3B + LoRA\\\", \\\"seed\\\": \\\"42,123,7\\\", \\\"hypothesis\\\": \\\"H3: data-flow hard negatives vs random vs embedding-distance, 3-seed × 3-strategy contrastive training\\\", \\\"plan_id\\\": \\\"mvp_p2b_contrastive_training\\\", \\\"checkpoint_path\\\": \\\"N/A\\\", \\\"log_path\\\": \\\"N/A\\\"}, \\\"conclusion\\\": \\\"killed\\\", \\\"completed_at\\\": \\\"2026-05-12T15:04:44.396Z\\\", \\\"notes\\\": \\\"P2b 对比训练 v2，因磁盘空间不足被 kill。已被 p2b_5reruns（成功完成 9/9 runs）替代。\\\"}, \\\"p2b_dataflow_retrain\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-12T19:49:00.303Z\\\", \\\"updated_at\\\": \\\"2026-05-13T07:23:27.706Z\\\", \\\"spec\\\": {\\\"command\\\": \\\"build_p2b_data.py regeneration + dataflow 3-seed retrain\\\", \\\"server\\\": \\\"cqa1-21977\\\", \\\"data_path\\\": \\\"/root/structfuse\\\", \\\"data_count\\\": 0, \\\"model_name\\\": \\\"Qwen2.5-Coder-3B (LoRA)\\\", \\\"seed\\\": \\\"42,123,456\\\", \\\"description\\\": \\\"BLOCKED: dataflow connections ⊆ gold files, strategies indistinguishable\\\", \\\"checkpoint_path\\\": \\\"N/A\\\", \\\"log_path\\\": \\\"N/A\\\"}, \\\"conclusion\\\": \\\"negative\\\", \\\"completed_at\\\": \\\"2026-05-13T04:17:02.055Z\\\", \\\"notes\\\": \\\"Dataflow 策略重训练计划，因 embedding_distance 命名问题（实际用 BM25 而非 embedding）被 Reviewer 发现后搁置。已被 m2_embed_verify（true embedding mining）替代。\\\"}, \\\"p2b_eval_all\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-12T16:27:50.967Z\\\", \\\"updated_at\\\": \\\"2026-05-13T07:23:24.721Z\\\", \\\"spec\\\": {\\\"command\\\": \\\"bash -c \\\\\\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/structfuse && bash scripts/run_eval_all.sh\\\\\\\"\\\", \\\"server\\\": \\\"cqa1-21977\\\", \\\"gpu\\\": [\\\"cuda:4\\\"], \\\"pid\\\": \\\"254053\\\", \\\"log_path\\\": \\\"N/A\\\", \\\"submitted_at\\\": \\\"2026-05-12T16:27:50.945Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\", \\\"checkpoint_path\\\": \\\"N/A\\\", \\\"wall_clock_seconds\\\": 42550.6, \\\"gpu_hours\\\": 11.82}, \\\"conclusion\\\": \\\"killed\\\", \\\"completed_at\\\": \\\"2026-05-13T04:17:01.561Z\\\", \\\"notes\\\": \\\"P2b 全量 eval（pool_size=26），被 D013 服务器迁移计划取消。已被 p2b_eval_4runs_pool50（pool_size=50）替代。\\\"}, \\\"m2_early_pilot\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-13T01:39:53.920Z\\\", \\\"updated_at\\\": \\\"2026-05-13T04:44:22.077Z\\\", \\\"hypothesis\\\": \\\"Early pilot on partial M1 data (24 repos, ~5K instances): verify M2 training pipeline works end-to-end and get early signal on 3-strategy differentiation before full M1 completes\\\", \\\"spec\\\": {\\\"command\\\": \\\"bash /root/structfuse/scripts/run_m2_pilot.sh\\\", \\\"server\\\": \\\"cqa1-21977\\\", \\\"gpu\\\": [\\\"cuda:4\\\"], \\\"pid\\\": \\\"795739\\\", \\\"log_path\\\": \\\"/root/autodl-tmp/structfuse/m2_pilot_output/random_s42.log\\\", \\\"submitted_at\\\": \\\"2026-05-13T01:55:31.288Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\", \\\"data_path\\\": \\\"/root/autodl-tmp/structfuse/m2_pilot_data/\\\", \\\"data_count\\\": 3418, \\\"model_name\\\": \\\"Qwen/Qwen2.5-Coder-3B\\\", \\\"seed\\\": 42, \\\"checkpoint_source\\\": \\\"N/A (training from scratch)\\\", \\\"eval_data\\\": \\\"N/A (training, not eval)\\\", \\\"checkpoint_path\\\": \\\"/root/autodl-tmp/structfuse/m2_pilot_output/random_s42/best_model.pt\\\", \\\"wall_clock_seconds\\\": 10130.8, \\\"gpu_hours\\\": 2.81}, \\\"conclusion\\\": \\\"killed\\\", \\\"notes\\\": \\\"PID 795791 在 cqa1 cuda:4 运行，wrapper 脚本顺序跑 random→embedding→dataflow（set -e）。random 策略跑到 step 4000 后卡住（~45min 无新日志），embedding/dataflow 未启动。Best checkpoint at step 1500。Val_loss 持续恶化（0.5879→0.728），明显过拟合。另有 OOM 进程干扰（某进程试图在同 GPU 启动导致 OOM，可能破坏 GPU 状态）。eval recall@k bug 已确认。\\\", \\\"metrics\\\": {\\\"pid\\\": 795791, \\\"gpu\\\": \\\"cuda:4\\\", \\\"gpu_mem_mb\\\": 9342, \\\"gpu_util_pct\\\": 83, \\\"batch_size\\\": 2, \\\"num_negatives\\\": 3, \\\"max_seq_length\\\": 1024, \\\"strategy_running\\\": \\\"random (stuck at step 4000, epoch 3)\\\", \\\"strategies_completed\\\": \\\"0/3\\\", \\\"eval_1500\\\": {\\\"val_loss\\\": 0.5879, \\\"recall_at_1\\\": 0.4693, \\\"recall_at_5\\\": 0.4693, \\\"recall_at_10\\\": 0.4693}, \\\"eval_2000\\\": {\\\"val_loss\\\": 0.7089, \\\"recall_at_1\\\": 0.4398}, \\\"eval_2500\\\": {\\\"val_loss\\\": 0.6961, \\\"recall_at_1\\\": 0.4291}, \\\"eval_3000\\\": {\\\"val_loss\\\": 0.728, \\\"recall_at_1\\\": 0.4104}, \\\"eval_3500\\\": {\\\"val_loss\\\": 0.7022, \\\"recall_at_1\\\": 0.4439}, \\\"best_checkpoint\\\": \\\"step_1500 (val_loss=0.5879, 6.2GB)\\\", \\\"WARNING\\\": \\\"recall@1=recall@5=recall@10 confirmed eval bug. Process hung after step 4000 (~45min no output). Overfitting after step 1500.\\\", \\\"status_check_at\\\": \\\"2026-05-13T04:42:00Z\\\"}, \\\"completed_at\\\": \\\"2026-05-13T04:44:22.077Z\\\"}, \\\"m2_early_pilot_v3\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-13T01:59:06.557Z\\\", \\\"updated_at\\\": \\\"2026-05-13T02:13:43.400Z\\\", \\\"spec\\\": {\\\"command\\\": \\\"bash -c \\\\\\\"bash /root/structfuse/run_m2_early_pilot.sh\\\\\\\"\\\", \\\"server\\\": \\\"cqa1-21977\\\", \\\"gpu\\\": [\\\"cuda:0\\\"], \\\"pid\\\": \\\"897651\\\", \\\"log_path\\\": \\\"~/runs/structfuse-context/m2_early_pilot_v3.log\\\", \\\"submitted_at\\\": \\\"2026-05-13T02:04:31.768Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\", \\\"checkpoint_path\\\": \\\"N/A\\\", \\\"wall_clock_seconds\\\": 551.6, \\\"gpu_hours\\\": 0.15}, \\\"conclusion\\\": \\\"killed\\\", \\\"notes\\\": \\\"GPU 越界 cuda:0，违反项目 GPU 分配 gpu_ids=[\\\\\\\"cuda:4\\\\\\\"]。第二次 GPU 越界违规（首次 D005）。Worker 未正确映射 CUDA_VISIBLE_DEVICES。\\\", \\\"completed_at\\\": \\\"2026-05-13T02:13:43.400Z\\\"}, \\\"m2_early_pilot_v2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-13T01:52:52.724Z\\\", \\\"updated_at\\\": \\\"2026-05-13T02:13:31.039Z\\\", \\\"spec\\\": {\\\"command\\\": \\\"bash /root/structfuse/run_m2_early_pilot.sh\\\", \\\"server\\\": \\\"cqa1-21977\\\", \\\"gpu\\\": [\\\"cuda:4\\\"], \\\"pid\\\": \\\"766124\\\", \\\"log_path\\\": \\\"~/runs/structfuse-context/m2_early_pilot_v2.log\\\", \\\"submitted_at\\\": \\\"2026-05-13T01:52:52.687Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\", \\\"data_path\\\": \\\"/root/autodl-tmp/structfuse/m2_early_pilot_data/\\\", \\\"data_count\\\": 3418, \\\"model_name\\\": \\\"Qwen/Qwen2.5-Coder-3B\\\", \\\"seed\\\": 42, \\\"checkpoint_source\\\": \\\"N/A (training from scratch)\\\", \\\"eval_data\\\": \\\"N/A (this is training, not eval)\\\", \\\"checkpoint_path\\\": \\\"N/A\\\", \\\"wall_clock_seconds\\\": 1238.4, \\\"gpu_hours\\\": 0.34}, \\\"hypothesis\\\": \\\"Early pilot on partial M1 data (24 repos, 2672 train + 746 val): verify M2 training pipeline works end-to-end and get early signal on 3-strategy differentiation before full M1 completes\\\", \\\"parent\\\": \\\"m1_extraction\\\", \\\"notes\\\": \\\"wandb API key error, EXIT_CODE=1。首次提交因 wandb 未配置离线模式而立即退出。\\\", \\\"conclusion\\\": \\\"failed\\\", \\\"completed_at\\\": \\\"2026-05-13T02:13:31.040Z\\\"}, \\\"mvp_p2b_contrastive_training\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 2, \\\"created_at\\\": \\\"2026-05-12T12:37:44.628Z\\\", \\\"updated_at\\\": \\\"2026-05-13T01:31:27.220Z\\\", \\\"reproduce\\\": {\\\"finished_at\\\": \\\"2026-05-12T16:19:50.297Z\\\"}, \\\"failure_reason\\\": \\\"EXIT_CODE=2 (shell misuse / syntax)\\\", \\\"completed_at\\\": \\\"2026-05-12T13:16:21.735Z\\\", \\\"extra\\\": {\\\"hook_events\\\": [{\\\"event\\\": \\\"on_failed\\\", \\\"action\\\": \\\"agent\\\", \\\"ts\\\": \\\"2026-05-12T13:16:22.517958+00:00\\\"}, {\\\"event\\\": \\\"on_failed\\\", \\\"action\\\": \\\"agent\\\", \\\"ts\\\": \\\"2026-05-12T15:15:47.933008+00:00\\\"}, {\\\"event\\\": \\\"on_complete\\\", \\\"action\\\": \\\"agent\\\", \\\"ts\\\": \\\"2026-05-12T16:19:51.082427+00:00\\\"}], \\\"previous_failure\\\": {\\\"conclusion\\\": \\\"failed\\\", \\\"notes\\\": \\\"第2次失败: random策略3seeds全部完成(s42跳过/s123 recall@5=0.984/s456 recall@5=0.992), 但embedding策略s42启动即EXIT_CODE=2(shell syntax error). Worker worker_diagnose_mvp_p2b_contrastive_training_v2 正在诊断和修复run_p2b_all.sh的embedding配置部分\\\"}}, \\\"notes\\\": \\\"4/9 runs 完成 (random×3 + embedding_distance_s42), 5/9 失败 (磁盘满 torch.save RuntimeError). /root/autodl-tmp 93% (14GB剩余, 每个checkpoint 5.8GB). 失败从 embedding_distance_s123 开始级联.\\\", \\\"spec\\\": {\\\"command\\\": \\\"bash scripts/run_p2b_all.sh (9 runs: 3 strategies × 3 seeds)\\\", \\\"server\\\": \\\"cqa1-21977\\\", \\\"gpu\\\": [\\\"cuda:4\\\"], \\\"pid\\\": \\\"238645\\\", \\\"data_path\\\": \\\"/root/structfuse/mvp_data/training_data/\\\", \\\"data_count\\\": 127, \\\"model_name\\\": \\\"Qwen2.5-Coder-3B + LoRA\\\", \\\"seed\\\": \\\"42,123,456\\\", \\\"hypothesis\\\": \\\"H3: data-flow hard negatives vs random vs embedding-distance, 3-seed × 3-strategy contrastive training\\\", \\\"plan_id\\\": \\\"mvp_p2b_contrastive_training\\\", \\\"checkpoint_path\\\": \\\"/root/autodl-tmp/structfuse/checkpoints/\\\", \\\"log_path\\\": \\\"/tmp/p2b_all_runs.log\\\"}, \\\"metrics\\\": {\\\"random_s42_recall1\\\": 0.984, \\\"random_s123_recall1\\\": 0.984, \\\"random_s456_recall1\\\": 0.992, \\\"embedding_s42_recall1\\\": 0.874, \\\"random_mean_recall1\\\": 0.987, \\\"runs_completed\\\": 4, \\\"runs_failed\\\": 5, \\\"failure_type\\\": \\\"disk_full_torch_save\\\"}, \\\"conclusion\\\": \\\"killed\\\"}, \\\"p2b_eval_4runs_pool50\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-12T20:10:54.579Z\\\", \\\"updated_at\\\": \\\"2026-05-13T00:27:50.197Z\\\", \\\"spec\\\": {\\\"command\\\": \\\"eval_p2b.py on 4 checkpoints with new val.jsonl pool_size=50\\\", \\\"server\\\": \\\"cqa1-21977\\\", \\\"data_path\\\": \\\"/root/structfuse\\\", \\\"data_count\\\": 127, \\\"model_name\\\": \\\"Qwen2.5-Coder-3B (LoRA)\\\", \\\"seed\\\": \\\"42,123,456\\\", \\\"checkpoint_source\\\": \\\"p2b_5reruns (random×3 + emb_dist×1)\\\", \\\"eval_data\\\": \\\"val.jsonl pool_size=50\\\"}, \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"pool_size\\\": 50, \\\"n_samples\\\": 127, \\\"random_s42\\\": {\\\"recall@1\\\": 0.496, \\\"recall@5\\\": 0.843, \\\"recall@10\\\": 0.945}, \\\"random_s123\\\": {\\\"recall@1\\\": 0.535, \\\"recall@5\\\": 0.85, \\\"recall@10\\\": 0.921}, \\\"random_s456\\\": {\\\"recall@1\\\": 0.543, \\\"recall@5\\\": 0.843, \\\"recall@10\\\": 0.953}, \\\"emb_dist_s42\\\": {\\\"recall@1\\\": 0.488, \\\"recall@5\\\": 0.835, \\\"recall@10\\\": 0.874}, \\\"random_mean\\\": {\\\"recall@1\\\": 0.525, \\\"recall@5\\\": 0.845, \\\"recall@10\\\": 0.94}, \\\"emb_dist_vs_random_delta\\\": {\\\"recall@1\\\": -0.037, \\\"recall@5\\\": -0.01, \\\"recall@10\\\": -0.066}}, \\\"checkpoint_path\\\": \\\"/root/autodl-tmp/structfuse/checkpoints/ (p2b_random_s42/123/456, p2b_embedding_distance_s42)\\\", \\\"log_path\\\": \\\"已清理 (2026-05-12 Director Step 1 指令 rm -rf)，metrics 保留在 registry\\\", \\\"completed_at\\\": \\\"2026-05-12T20:11:12.318Z\\\"}, \\\"d007_50repo_overlap\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-12T20:37:24.289Z\\\", \\\"updated_at\\\": \\\"2026-05-12T20:37:39.566Z\\\", \\\"spec\\\": {\\\"command\\\": \\\"CodeQL 2-hop extraction + connected vs gold overlap stats on 50 repos\\\", \\\"server\\\": \\\"cqa1-21977\\\", \\\"data_path\\\": \\\"/root/structfuse\\\", \\\"data_count\\\": 240, \\\"model_name\\\": \\\"N/A (CPU analysis)\\\", \\\"seed\\\": \\\"N/A\\\", \\\"description\\\": \\\"50-repo overlap validation: Z=40.8%, original method viable\\\"}, \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"total_instances\\\": 240, \\\"instances_with_extra_connected\\\": 98, \\\"Z_pct\\\": 40.8, \\\"avg_connected_minus_gold\\\": 6, \\\"codeql_timeout_rate_pct\\\": 4, \\\"by_repo_size\\\": {\\\"small_lt50\\\": {\\\"Z_pct\\\": 38.6, \\\"avg_extra\\\": 2.5}, \\\"medium_50_200\\\": {\\\"Z_pct\\\": 55.7, \\\"avg_extra\\\": 11.8}, \\\"large_gt200\\\": {\\\"Z_pct\\\": 16.7, \\\"avg_extra\\\": 8.8}}, \\\"decision\\\": \\\"Z=40.8% >= 20% -> original method viable, proceed to M1\\\"}, \\\"checkpoint_path\\\": \\\"N/A (analysis only)\\\", \\\"log_path\\\": \\\"/root/structfuse/data/50repo_overlap_stats/\\\", \\\"completed_at\\\": \\\"2026-05-12T20:37:39.566Z\\\"}, \\\"p2b_5reruns\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-12T17:26:47.603Z\\\", \\\"updated_at\\\": \\\"2026-05-12T19:19:53.785Z\\\", \\\"spec\\\": {\\\"command\\\": \\\"bash run_p2b_all.sh (skips 4 done, runs 5: emb_dist s123/456, dataflow s42/123/456)\\\", \\\"server\\\": \\\"cqa1-21977\\\", \\\"gpu\\\": [\\\"cuda:4\\\"], \\\"pid\\\": \\\"272732\\\", \\\"log_path\\\": \\\"~/runs/structfuse-context/p2b_5reruns.log\\\", \\\"submitted_at\\\": \\\"2026-05-12T17:26:47.575Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\", \\\"data_path\\\": \\\"/root/structfuse\\\", \\\"data_count\\\": 500, \\\"model_name\\\": \\\"Qwen2.5-Coder-3B (LoRA)\\\", \\\"seed\\\": \\\"42,123,456\\\", \\\"description\\\": \\\"Phase 2b 5 reruns: emb_dist s123/456 + dataflow_aware s42/123/456\\\", \\\"hyperparams\\\": {\\\"batch_size\\\": 2, \\\"lr\\\": \\\"2e-5\\\", \\\"num_negatives\\\": 3, \\\"max_seq_length\\\": 512, \\\"use_lora\\\": true, \\\"gradient_checkpointing\\\": true, \\\"eval_steps\\\": 50, \\\"save_steps\\\": 200, \\\"num_epochs\\\": 3}, \\\"wall_clock_seconds\\\": 6752.2, \\\"gpu_hours\\\": 1.88}, \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"random_s42\\\": {\\\"val_loss\\\": 0.0347, \\\"recall@1\\\": 0.9843}, \\\"random_s123\\\": {\\\"val_loss\\\": 0.0446, \\\"recall@1\\\": 0.9843}, \\\"random_s456\\\": {\\\"val_loss\\\": 0.0188, \\\"recall@1\\\": 0.9921}, \\\"emb_dist_s42\\\": {\\\"val_loss\\\": 0.1876, \\\"recall@1\\\": 0.874}, \\\"emb_dist_s123\\\": {\\\"val_loss\\\": 0.1461, \\\"recall@1\\\": 0.874}, \\\"emb_dist_s456\\\": {\\\"val_loss\\\": 0.1281, \\\"recall@1\\\": 0.8819}, \\\"dataflow_s42\\\": {\\\"val_loss\\\": 0.1878, \\\"recall@1\\\": 0.874}, \\\"dataflow_s123\\\": {\\\"val_loss\\\": 0.146, \\\"recall@1\\\": 0.874}, \\\"dataflow_s456\\\": {\\\"val_loss\\\": 0.1278, \\\"recall@1\\\": 0.8819}, \\\"runs_completed\\\": 9, \\\"runs_failed\\\": 0, \\\"WARNING\\\": \\\"dataflow_aware ≈ embedding_distance to 4 decimal places across all seeds — likely code bug in negative sampling\\\"}, \\\"checkpoint_path\\\": \\\"/root/autodl-tmp/structfuse/checkpoints/ (9 dirs: p2b_{random,embedding_distance,dataflow_aware}_s{42,123,456})\\\", \\\"completed_at\\\": \\\"2026-05-12T19:19:19.793Z\\\", \\\"log_path\\\": \\\"~/runs/structfuse-context/p2b_5reruns.log\\\"}, \\\"p2b_eval_4runs_v2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-12T17:21:49.599Z\\\", \\\"updated_at\\\": \\\"2026-05-12T17:22:16.595Z\\\", \\\"spec\\\": {\\\"command\\\": \\\"eval 4 runs (3 random seeds + 1 emb_dist) with pool_size=26\\\", \\\"server\\\": \\\"cqa1-21977\\\", \\\"data_path\\\": \\\"/root/structfuse\\\", \\\"data_count\\\": 127, \\\"model_name\\\": \\\"Qwen2.5-Coder-3B (LoRA)\\\", \\\"seed\\\": \\\"42,123,456\\\", \\\"description\\\": \\\"Phase 2b eval v2: pool_size=26 评估 random vs emb_dist\\\"}, \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"random_seed42\\\": {\\\"recall@1\\\": 0.9449, \\\"recall@5\\\": 0.9843, \\\"recall@10\\\": 0.9843}, \\\"random_seed123\\\": {\\\"recall@1\\\": 0.9449, \\\"recall@5\\\": 0.9921, \\\"recall@10\\\": 0.9921}, \\\"random_seed456\\\": {\\\"recall@1\\\": 0.9291, \\\"recall@5\\\": 0.9921, \\\"recall@10\\\": 0.9921}, \\\"emb_dist_seed42\\\": {\\\"recall@1\\\": 0.6693, \\\"recall@5\\\": 0.8898, \\\"recall@10\\\": 0.9291}, \\\"pool_size\\\": 26, \\\"n_samples\\\": 127}, \\\"checkpoint_path\\\": \\\"/root/autodl-tmp/structfuse/checkpoints/ (4 runs: random_s42/123/456, emb_dist_s42)\\\", \\\"log_path\\\": \\\"/root/autodl-tmp/structfuse/eval_results/\\\", \\\"completed_at\\\": \\\"2026-05-12T17:22:16.595Z\\\"}, \\\"p2b-all-9runs\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-12T12:34:24.923Z\\\", \\\"updated_at\\\": \\\"2026-05-12T15:05:49.244Z\\\", \\\"spec\\\": {\\\"command\\\": \\\"obsolete smoke test\\\", \\\"server\\\": \\\"cqa1-21977\\\", \\\"gpu\\\": [\\\"cuda:4\\\"], \\\"pid\\\": \\\"92636\\\", \\\"log_path\\\": \\\"N/A\\\", \\\"submitted_at\\\": \\\"2026-05-12T12:34:24.908Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\", \\\"data_path\\\": \\\"N/A\\\", \\\"data_count\\\": 0, \\\"model_name\\\": \\\"N/A\\\", \\\"seed\\\": 42, \\\"checkpoint_path\\\": \\\"N/A\\\", \\\"wall_clock_seconds\\\": 9084.3, \\\"gpu_hours\\\": 2.52}, \\\"conclusion\\\": \\\"killed\\\", \\\"completed_at\\\": \\\"2026-05-12T15:05:49.244Z\\\"}, \\\"p2b-smoke8\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-12T12:32:22.931Z\\\", \\\"updated_at\\\": \\\"2026-05-12T15:05:48.324Z\\\", \\\"spec\\\": {\\\"command\\\": \\\"obsolete smoke test\\\", \\\"server\\\": \\\"cqa1-21977\\\", \\\"gpu\\\": [\\\"cuda:4\\\"], \\\"pid\\\": \\\"91698\\\", \\\"log_path\\\": \\\"N/A\\\", \\\"submitted_at\\\": \\\"2026-05-12T12:32:22.916Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\", \\\"data_path\\\": \\\"N/A\\\", \\\"data_count\\\": 0, \\\"model_name\\\": \\\"N/A\\\", \\\"seed\\\": 42, \\\"checkpoint_path\\\": \\\"N/A\\\", \\\"wall_clock_seconds\\\": 9205.4, \\\"gpu_hours\\\": 2.56}, \\\"conclusion\\\": \\\"killed\\\", \\\"completed_at\\\": \\\"2026-05-12T15:05:48.324Z\\\"}, \\\"p2b-smoke7\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-12T12:28:55.114Z\\\", \\\"updated_at\\\": \\\"2026-05-12T15:05:47.346Z\\\", \\\"spec\\\": {\\\"command\\\": \\\"obsolete smoke test\\\", \\\"server\\\": \\\"cqa1-21977\\\", \\\"gpu\\\": [\\\"cuda:4\\\"], \\\"pid\\\": \\\"90758\\\", \\\"log_path\\\": \\\"N/A\\\", \\\"submitted_at\\\": \\\"2026-05-12T12:28:55.101Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\", \\\"data_path\\\": \\\"N/A\\\", \\\"data_count\\\": 0, \\\"model_name\\\": \\\"N/A\\\", \\\"seed\\\": 42, \\\"checkpoint_path\\\": \\\"N/A\\\", \\\"wall_clock_seconds\\\": 9412.2, \\\"gpu_hours\\\": 2.61}, \\\"conclusion\\\": \\\"killed\\\", \\\"completed_at\\\": \\\"2026-05-12T15:05:47.346Z\\\"}, \\\"p2b-smoke6\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-12T12:22:54.445Z\\\", \\\"updated_at\\\": \\\"2026-05-12T15:05:46.413Z\\\", \\\"spec\\\": {\\\"command\\\": \\\"obsolete smoke test\\\", \\\"server\\\": \\\"cqa1-21977\\\", \\\"gpu\\\": [\\\"cuda:4\\\"], \\\"pid\\\": \\\"89257\\\", \\\"log_path\\\": \\\"N/A\\\", \\\"submitted_at\\\": \\\"2026-05-12T12:22:54.433Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\", \\\"data_path\\\": \\\"N/A\\\", \\\"data_count\\\": 0, \\\"model_name\\\": \\\"N/A\\\", \\\"seed\\\": 42, \\\"checkpoint_path\\\": \\\"N/A\\\", \\\"wall_clock_seconds\\\": 9772.0, \\\"gpu_hours\\\": 2.71}, \\\"conclusion\\\": \\\"killed\\\", \\\"completed_at\\\": \\\"2026-05-12T15:05:46.413Z\\\"}, \\\"p2b-smoke5\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-12T12:22:05.754Z\\\", \\\"updated_at\\\": \\\"2026-05-12T15:05:45.484Z\\\", \\\"spec\\\": {\\\"command\\\": \\\"obsolete smoke test\\\", \\\"server\\\": \\\"cqa1-21977\\\", \\\"gpu\\\": [\\\"cuda:4\\\"], \\\"pid\\\": \\\"88719\\\", \\\"log_path\\\": \\\"N/A\\\", \\\"submitted_at\\\": \\\"2026-05-12T12:22:05.744Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\", \\\"data_path\\\": \\\"N/A\\\", \\\"data_count\\\": 0, \\\"model_name\\\": \\\"N/A\\\", \\\"seed\\\": 42, \\\"checkpoint_path\\\": \\\"N/A\\\", \\\"wall_clock_seconds\\\": 9819.7, \\\"gpu_hours\\\": 2.73}, \\\"conclusion\\\": \\\"killed\\\", \\\"completed_at\\\": \\\"2026-05-12T15:05:45.484Z\\\"}, \\\"p2b-smoke4\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-12T12:20:53.305Z\\\", \\\"updated_at\\\": \\\"2026-05-12T15:05:44.066Z\\\", \\\"spec\\\": {\\\"command\\\": \\\"obsolete smoke test\\\", \\\"server\\\": \\\"cqa1-21977\\\", \\\"gpu\\\": [\\\"cuda:4\\\"], \\\"pid\\\": \\\"87968\\\", \\\"log_path\\\": \\\"N/A\\\", \\\"submitted_at\\\": \\\"2026-05-12T12:20:53.296Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\", \\\"data_path\\\": \\\"N/A\\\", \\\"data_count\\\": 0, \\\"model_name\\\": \\\"N/A\\\", \\\"seed\\\": 42, \\\"checkpoint_path\\\": \\\"N/A\\\", \\\"wall_clock_seconds\\\": 9890.8, \\\"gpu_hours\\\": 2.75}, \\\"conclusion\\\": \\\"killed\\\", \\\"completed_at\\\": \\\"2026-05-12T15:05:44.066Z\\\"}, \\\"p2b-smoke3\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-12T12:18:19.105Z\\\", \\\"updated_at\\\": \\\"2026-05-12T15:05:43.111Z\\\", \\\"spec\\\": {\\\"command\\\": \\\"obsolete smoke test\\\", \\\"server\\\": \\\"cqa1-21977\\\", \\\"gpu\\\": [\\\"cuda:4\\\"], \\\"pid\\\": \\\"86879\\\", \\\"log_path\\\": \\\"N/A\\\", \\\"submitted_at\\\": \\\"2026-05-12T12:18:19.098Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\", \\\"data_path\\\": \\\"N/A\\\", \\\"data_count\\\": 0, \\\"model_name\\\": \\\"N/A\\\", \\\"seed\\\": 42, \\\"checkpoint_path\\\": \\\"N/A\\\", \\\"wall_clock_seconds\\\": 10044.0, \\\"gpu_hours\\\": 2.79}, \\\"conclusion\\\": \\\"killed\\\", \\\"completed_at\\\": \\\"2026-05-12T15:05:43.111Z\\\"}, \\\"p2b-smoke2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-12T12:16:08.154Z\\\", \\\"updated_at\\\": \\\"2026-05-12T15:05:42.174Z\\\", \\\"spec\\\": {\\\"command\\\": \\\"obsolete smoke test\\\", \\\"server\\\": \\\"cqa1-21977\\\", \\\"gpu\\\": [\\\"cuda:4\\\"], \\\"pid\\\": \\\"85793\\\", \\\"log_path\\\": \\\"N/A\\\", \\\"submitted_at\\\": \\\"2026-05-12T12:16:08.148Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\", \\\"data_path\\\": \\\"N/A\\\", \\\"data_count\\\": 0, \\\"model_name\\\": \\\"N/A\\\", \\\"seed\\\": 42, \\\"checkpoint_path\\\": \\\"N/A\\\", \\\"wall_clock_seconds\\\": 10174.0, \\\"gpu_hours\\\": 2.83}, \\\"conclusion\\\": \\\"killed\\\", \\\"completed_at\\\": \\\"2026-05-12T15:05:42.174Z\\\"}, \\\"p2b-smoke-test\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-12T12:14:30.477Z\\\", \\\"updated_at\\\": \\\"2026-05-12T15:05:41.269Z\\\", \\\"spec\\\": {\\\"command\\\": \\\"obsolete smoke test\\\", \\\"server\\\": \\\"cqa1-21977\\\", \\\"gpu\\\": [\\\"cuda:4\\\"], \\\"pid\\\": \\\"84805\\\", \\\"log_path\\\": \\\"N/A\\\", \\\"submitted_at\\\": \\\"2026-05-12T12:14:30.472Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\", \\\"data_path\\\": \\\"N/A\\\", \\\"data_count\\\": 0, \\\"model_name\\\": \\\"N/A\\\", \\\"seed\\\": 42, \\\"checkpoint_path\\\": \\\"N/A\\\", \\\"wall_clock_seconds\\\": 10270.8, \\\"gpu_hours\\\": 2.85}, \\\"conclusion\\\": \\\"killed\\\", \\\"completed_at\\\": \\\"2026-05-12T15:05:41.270Z\\\"}, \\\"mvp_p2a_linear_proxy\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-12T11:53:42.223Z\\\", \\\"updated_at\\\": \\\"2026-05-12T11:58:15.436Z\\\", \\\"spec\\\": {\\\"command\\\": \\\"python evaluation/linear_proxy.py (logistic regression on data-flow features + BM25)\\\", \\\"server\\\": \\\"cqa1-21977\\\", \\\"data_path\\\": \\\"/root/autodl-tmp/mvp_results/ + /root/structfuse/mvp_data/bm25/\\\", \\\"data_count\\\": 8, \\\"model_name\\\": \\\"LogisticRegression (scikit-learn)\\\", \\\"seed\\\": null, \\\"hypothesis\\\": \\\"H2-confirm: data-flow features 的线性分类器预测 bug-relevant 文件优于纯 BM25 baseline\\\", \\\"plan_id\\\": \\\"mvp_p2a_linear_proxy\\\"}, \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"df_bm25_auc\\\": 0.78, \\\"bm25_only_auc\\\": 0.476, \\\"auc_delta\\\": 0.304, \\\"df_bm25_mrr\\\": 0.556, \\\"bm25_only_mrr\\\": 0.115, \\\"mrr_delta\\\": 0.441, \\\"df_bm25_f1\\\": 0.143, \\\"bm25_only_f1\\\": 0.039, \\\"top_feature\\\": \\\"is_connected (+2.82)\\\", \\\"repos_evaluated\\\": 3, \\\"note\\\": \\\"3 repos / 3 positive samples, directional evidence\\\"}, \\\"checkpoint_path\\\": \\\"N/A (logistic regression, no checkpoint)\\\", \\\"log_path\\\": \\\"/root/structfuse/evaluation/linear_proxy.py output\\\", \\\"completed_at\\\": \\\"2026-05-12T11:58:15.436Z\\\"}, \\\"mvp_p1_codeql_feasibility\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-12T11:30:45.938Z\\\", \\\"updated_at\\\": \\\"2026-05-12T11:58:06.197Z\\\", \\\"spec\\\": {\\\"command\\\": \\\"python extraction/extract_dataflow.py + codeql query run (call_graph.ql + bounded_dataflow.ql)\\\", \\\"server\\\": \\\"cqa1-21977\\\", \\\"data_path\\\": \\\"/root/structfuse/mvp_data/repos (8 SWE-smith instances: flask, requests, pytest, pylint, xarray, astropy, sphinx, matplotlib)\\\", \\\"data_count\\\": 8, \\\"model_name\\\": \\\"N/A (CPU pipeline)\\\", \\\"seed\\\": null, \\\"hypothesis\\\": \\\"H1: CodeQL 2-hop bounded data-flow timeout <30%; H2: connected files gold patch coverage significantly > disconnected\\\", \\\"plan_id\\\": \\\"mvp_p1_codeql_feasibility\\\"}, \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"timeout_rate\\\": 0, \\\"repos_processed\\\": 8, \\\"repos_skipped\\\": 2, \\\"cg_mean_s\\\": 29.6, \\\"cg_max_s\\\": 119.8, \\\"df_mean_s\\\": 43.4, \\\"df_max_s\\\": 167.1, \\\"h2_connected_coverage\\\": 0.014815, \\\"h2_disconnected_coverage\\\": 0, \\\"h2_fisher_p\\\": 6.5e-09, \\\"h2_gold_in_connected_ratio\\\": 1, \\\"h2_note\\\": \\\"After path normalization fix: 8/8 gold in connected (was 6/8)\\\"}, \\\"log_path\\\": \\\"/root/autodl-tmp/mvp_results/mvp_phase1_report.json\\\", \\\"checkpoint_path\\\": \\\"N/A (CPU pipeline, no model checkpoint)\\\", \\\"completed_at\\\": \\\"2026-05-12T11:31:16.335Z\\\"}}, \\\"count\\\": 37, \\\"total\\\": 37, \\\"baseline\\\": null}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.1285}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {\"m1_reextract_v2\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-13T20:00:20.578Z\", \"updated_at\": \"2026-05-14T21:18:48.643Z\", \"hypothesis\": \"M1 重提取 v2：恢复 28,276 个因运行时瞬态文件系统故障失败的 instances（82 repos）。CodeQL pack 已修复，端到端测试通过。预期将训练数据从 15,897 提升至 ~44,173。D022 批准。\", \"parent\": \"m1_extraction\", \"spec\": {\"command\": \"bash scripts/rerun_m1_failed.sh (4 CPU workers, CodeQL 2-hop, pack installed)\", \"server\": \"bjb1-42106\", \"data_path\": \"/root/autodl-tmp/structfuse/full_m1_data/\", \"data_count\": 28276, \"model_name\": \"N/A (CodeQL extraction)\", \"seed\": \"N/A\", \"log_path\": \"/root/runs/structfuse-context/m1_reextract_v2.log\", \"checkpoint_source\": \"rerun of m1_extraction failed instances (v2, CodeQL fixed)\", \"eval_data\": \"N/A\"}, \"notes\": \"M1 重提取 v2：CodeQL pack 已修复，端到端测试通过。28,276 instances / 82 repo groups / 4 workers 并行。启动 2026-05-14 03:59 CST。[诊断 07:06 CST] 活跃运行中，~15/82 groups 完成，2,469 次 call_graph 查询成功，预计还需 ~13-16h。仅前 4 个旧 repo（furl/pyasn1/feedparser/python-docx）复用 v1 旧 DB 有 18 次降级 WARNING，04:02 之后零失败。产出写入 all.jsonl（追加模式）。磁盘 97GB 可用。[Director 决策 Session 8] 即使数据量增至 ~44K，不重跑 M2（ARR May 25 DDL 不允许再加 4-5 天重训）。处理方式：(1) post-M2 完成后如有 GPU 空档，跑 1-seed pilot (Qwen, embedding, 新数据) 对比当前 M2 baseline; (2) 论文中作为 scalability/data efficiency 讨论点; (3) 全量重训留 camera-ready。[进度检查 2026-05-15 05:05 CST] 80.8% 完成（22,842/28,276），0 ERROR，速率 ~560/hr，处理中大 repo：mozilla__bleach/sqlfluff/conan-io/Project-MONAI。产出为单独 .json 文件，尚未合并 all.jsonl。预计 ~15:00 CST May 15 完成。\", \"metrics\": {\"checked_at\": \"2026-05-15T05:15Z\", \"process\": \"alive (CPU, 4 workers)\", \"started\": \"2026-05-14T03:59Z\", \"elapsed_hours\": 25, \"total_instances\": 28276, \"repo_groups\": 82, \"output_json_files\": 40225, \"all_jsonl_lines\": 44173, \"active_repos\": {\"sqlfluff/sqlfluff\": \"250/1272\", \"mozilla/bleach\": \"350/455\", \"conan-io/conan\": \"450/972\", \"Project-MONAI/MONAI\": \"150/524\"}, \"estimated_total_hours\": 60, \"progress_pct_by_time\": \"~42%\", \"disk\": \"98GB free on /root/autodl-tmp\"}}, \"m2_full_starcoder_resumed\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-14T18:44:19.253Z\", \"updated_at\": \"2026-05-14T21:18:45.080Z\", \"hypothesis\": \"M2 StarCoder resumed: 继续 m2_full_starcoder 的 8 sequential runs (random×2 + embedding×3 + dataflow×3)。原实验因 cron timeout 标记为 failed，实际 PID 519791 正常运行。\", \"spec\": {\"command\": \"bash run_m2_full_starcoder_resume.sh (8 runs: random_s43→s44→embedding×3→dataflow×3)\", \"server\": \"bjb1-42106\", \"gpu\": [\"cuda:1\"], \"pid\": \"519791\", \"log_path\": \"/root/runs/structfuse-context/m2_full_starcoder.log\", \"data_path\": \"/root/autodl-tmp/structfuse/full_m2_training_data/\", \"data_count\": 11308, \"model_name\": \"StarCoder2-3B\", \"seed\": \"42,43,44\"}, \"parent\": \"m2_full_starcoder\", \"metrics\": {\"checked_at\": \"2026-05-15T05:15Z\", \"process\": \"alive (PID 519791, uptime 03:11:44)\", \"gpu\": \"cuda:1, 100% util, 53.9/97.9GB VRAM, 72°C\", \"current_subrun\": \"random_s43 (1/9)\", \"current_step\": \"550/1405 (epoch 1/2, ~20% of subrun)\", \"eval_at_500\": {\"R@1\": 0.4708, \"R@5\": 0.9469, \"val_loss\": 0.5279}, \"latest_loss\": 0.26, \"completed_subruns\": 0, \"remaining_subruns\": 8, \"eta_hours\": \"~65-70h\"}}, \"m2_full_qwen_continued\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-14T18:44:20.646Z\", \"updated_at\": \"2026-05-14T21:18:42.976Z\", \"hypothesis\": \"M2 Qwen continued: 继续 m2_full_qwen 的剩余 runs (random_s44 + embedding×3 + dataflow×3)。原实验 cron 在 s42 退出时自动设为 ANALYZING，但链仍在运行。\", \"spec\": {\"command\": \"bash run_m2_full_qwen.sh (chain: random_s44 running → embedding×3 → dataflow×3)\", \"server\": \"bjb1-42106\", \"gpu\": [\"cuda:0\"], \"pid\": \"337267\", \"log_path\": \"/root/runs/structfuse-context/m2_full_qwen.log\", \"data_path\": \"/root/autodl-tmp/structfuse/full_m2_training_data/\", \"data_count\": 11308, \"model_name\": \"Qwen2.5-Coder-3B\", \"seed\": \"42,43,44\"}, \"parent\": \"m2_full_qwen\", \"metrics\": {\"checked_at\": \"2026-05-15T05:15Z\", \"process\": \"alive (PID 337267, uptime 09:50:41)\", \"gpu\": \"cuda:0, 100% util, 51.5/97.9GB VRAM, 68°C\", \"current_subrun\": \"random_s44 (3/7)\", \"current_step\": \"850/1408 (epoch 1/2, ~30% of subrun)\", \"eval_at_500\": {\"R@1\": 0.6009, \"R@5\": 0.9583, \"val_loss\": 0.4252}, \"latest_loss\": 0.2837, \"completed_subruns\": {\"random_s42\": {\"best_R@1\": 0.5527, \"best_val_loss\": 0.4651}, \"random_s43\": {\"best_R@1\": 0.5554, \"best_val_loss\": 0.4476}}, \"remaining_subruns\": 5, \"eta_hours\": \"~40-45h\"}}, \"plan_005_stratified\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-14T20:36:16.738Z\", \"updated_at\": \"2026-05-14T21:07:45.324Z\", \"hypothesis\": \"Plan 005 分层分析：按 repo size/pool size/query-pos similarity/structural data availability/neg_difficulty quartile 5 维度分层评估 embedding vs random 策略差异，控制 pool_size confound。Claim 2 支撑实验。v2 结果为 ground truth（v1→v2 changelog 见 art_20260514_3008c4）。\", \"parent\": \"m2_full_qwen\", \"notes\": \"plan_id=plan_005. 分层评估脚本已完成全部修改（analyze_stratified.py）：(1) mock seed 确定性修复 (2) pool_size-controlled 策略对比（within-bin delta + weighted aggregate）(3) dataflow×pool_size 交叉分析（n<30 标记 underpowered）(4) checkpoint 发现逻辑已就绪（best_by_recall_at_1 / best / best_by_val_loss）。输出含 JSON + CSV + PDF。[2026-05-14 21:07] Worker 完成 5 项 Patch：(P1) reeval_checkpoint 重写为 batch encoding（query/positive/negatives 分组批量编码，tqdm 进度条，torch.no_grad + model.eval，pad_token 兜底）(P2) 新增 --batch-size 参数（默认 64）(P3) 调用处传递 batch_size (P4) 非 dry-run 自适应 sim bins（tercile 计算边界 + 重新分配 sim_bin）(P5) 输出 JSON 记录 similarity_bin_edges 和 batch_size。Dry-run 验证全部通过。真实评估待 M2 全部 checkpoint 就绪后执行。\", \"metrics\": {\"confound_analysis\": {\"data_validity\": \"⚠️ R@1 值为 dry-run mock predictions，不可引用。仅分布结构（cross_tabulation.csv）有效。\", \"valid_findings\": {\"distribution_structure\": \"rich-dataflow 99.3% 落在 large/xlarge repo，small repo 中完全不存在\", \"correlation\": {\"dataflow_edges_vs_repo_size_pearson_r\": 0.089}, \"cross_distribution\": {\"rich_in_large_xlarge_pct\": 99.3, \"rich_in_small\": 0, \"moderate_in_large_xlarge_pct\": 60.9}, \"implication\": \"真实评估必须控制 pool_size 和 repo_size 来隔离 dataflow richness 独立效应\"}, \"invalid_findings\": \"所有 R@1/R@5/MRR 值均为 mock predictions，策略排序 pattern 不可信，禁止引用\", \"artifacts_path\": \"/root/autodl-tmp/structfuse/artifacts/confound_analysis/\", \"valid_artifact\": \"cross_tabulation.csv\"}}}, \"plan_017_literature\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T18:49:00.477Z\", \"updated_at\": \"2026-05-14T18:49:39.557Z\", \"hypothesis\": \"Inference-time graph method comparison: 8 papers surveyed (CodexGraph, LocAgent, RANGER, GraphCoder, ARISE, RepoGraph, CodeGRAG, CodeRAG). Discussion v2 drafted, all citations verified. Conclusion: training-time vs inference-time complementary.\", \"spec\": {\"command\": \"analysis only (no training)\", \"server\": \"local\", \"data_path\": \"N/A\", \"data_count\": 0, \"model_name\": \"N/A\", \"seed\": \"N/A\", \"checkpoint_path\": \"N/A\", \"log_path\": \"N/A\"}, \"conclusion\": \"success\", \"metrics\": {\"papers_surveyed\": 8, \"citations_verified\": 8, \"discussion_draft\": \"artifacts/paper_drafts/discussion_v2.md\", \"artifact_id\": \"art_20260514_a2e1cd\"}, \"completed_at\": \"2026-05-14T18:49:39.557Z\"}, \"m2_full_starcoder\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T16:18:15.415Z\", \"updated_at\": \"2026-05-14T18:04:29.245Z\", \"hypothesis\": \"Full M2 StarCoder: 3 strategies × 3 seeds on full M1 data. Cross-encoder validation — if embedding > random holds for both Qwen and StarCoder, method is encoder-agnostic. Resolves plan_013 pilot negative (dataflow encoder-dependent).\", \"parent\": \"plan_013_starcoder\", \"spec\": {\"command\": \"bash -c \\\"cd /root/structfuse && bash run_m2_full_starcoder_resume.sh\\\"\", \"server\": \"bjb1-42106\", \"gpu\": [\"cuda:1\"], \"pid\": \"519791\", \"log_path\": \"~/runs/structfuse-context/m2_full_starcoder.log\", \"submitted_at\": \"2026-05-14T18:03:12.079Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"notes\": \"Phase 1: 构建 StarCoder embedding negatives 完成。Phase 2: 9 runs 训练中。batch_size=8, num_negatives=7, epochs=3(s42)/2(s43+), lr=2e-5, eval_steps=500, no early_stopping。双 checkpoint: best + best_by_recall_at_1。Seeds: 42,43,44。[D026] s42 保持 3 epochs; s43/s44 及后续 runs 改为 2 epochs。[2026-05-15 02:02 CST] cuda:1 进程冲突修复并重新提交（PID 519791, timeout=144h）。Registry 状态 DONE(failed) 是旧 cron timeout 标记，实际正在运行 random_s43 [1/8]。新 cron 已注册监控 PID 519791。序列：random_s43→s44→(待插入bm25_s42)→embedding×3→dataflow×3。random_s42 结果：best R@1=0.4604 at step 2500, val_loss=0.6134 at step 1000。\", \"metrics\": {\"random_s42\": {\"epoch\": \"3/3\", \"current_step\": 4200, \"total_steps\": 4242, \"total_steps_per_epoch\": 1414, \"eval_500\": {\"val_loss\": 0.6194, \"recall_at_1\": 0.435, \"recall_at_5\": 0.905, \"recall_at_10\": 1}, \"eval_1000\": {\"val_loss\": 0.6134, \"recall_at_1\": 0.454, \"recall_at_5\": 0.92, \"recall_at_10\": 1}, \"eval_1500\": {\"val_loss\": 0.6528, \"recall_at_1\": 0.449, \"recall_at_5\": 0.906, \"recall_at_10\": 1}, \"eval_2000\": {\"val_loss\": 0.6698, \"recall_at_1\": 0.4456, \"recall_at_5\": 0.906, \"recall_at_10\": 1}, \"eval_2500\": {\"val_loss\": 0.6342, \"recall_at_1\": 0.4604, \"recall_at_5\": 0.9117, \"recall_at_10\": 1}, \"eval_3000\": {\"val_loss\": 0.6516, \"recall_at_1\": 0.4544, \"recall_at_5\": 0.9077, \"recall_at_10\": 1}, \"eval_3500\": {\"val_loss\": 0.6588, \"recall_at_1\": 0.4534, \"recall_at_5\": 0.9057, \"recall_at_10\": 1}, \"eval_4000\": {\"val_loss\": 0.6637, \"recall_at_1\": 0.4547, \"recall_at_5\": 0.9003, \"recall_at_10\": 1}, \"best_checkpoint\": \"step_1000 (val_loss=0.6134) / step_2500 (R@1=0.4604)\", \"conclusion\": \"effectively_complete (timeout at step 4200/4242, lr=7.8e-9, remaining 42 steps negligible)\"}, \"progress_snapshot\": \"2026-05-15T01:50 CST\"}, \"reproduce\": {\"finished_at\": \"2026-05-14T17:49:54.474Z\"}, \"failure_reason\": \"EXIT_CODE=124 (timeout — exceeded timeout_hours)\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-14T17:49:55.304Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-14T17:49:56.408767+00:00\"}]}}, \"m2_full_qwen\": {\"status\": \"ANALYZING\", \"retry_count\": 0, \"created_at\": \"2026-05-13T16:18:14.870Z\", \"updated_at\": \"2026-05-14T18:00:29.323Z\", \"hypothesis\": \"Full M2 Qwen: 3 strategies (random/embedding/dataflow) × 3 seeds on full M1 data (~11K train/seed). Statistical validation of pilot signal (embedding > random +2pp). Go/no-go for paper claims per D018.\", \"parent\": \"m2_embed_verify\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/structfuse && bash run_m2_full_qwen.sh 2>&1 | tee /root/runs/structfuse-context/m2_full_qwen.log\\\"\", \"server\": \"bjb1-42106\", \"gpu\": [\"cuda:0\"], \"pid\": \"73544\", \"log_path\": \"~/runs/structfuse-context/m2_full_qwen.log\", \"submitted_at\": \"2026-05-13T17:39:30.757Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"notes\": \"Full M2 go/no-go: 3 strategies (random, embedding_distance, dataflow_aware) × 3 seeds (42, 43, 44) = 9 runs sequential on cuda:0. Config: lr=2e-5, batch_size=8, eval_steps=500, num_negatives=7, max_seq_length=2048, warmup_ratio=0.1, weight_decay=0.01, temperature=0.07, LoRA r=16, gradient_checkpointing=True, proj_dim=256. Dual checkpoint: best_by_val_loss + best_by_recall_at_1. Train ~11.3K/seed, val ~3K/seed. [D026] s42 保持 3 epochs 提供完整 overfitting curve; s43/s44 及后续 runs 改为 2 epochs + early_stopping_patience=2。[STATUS 2026-05-15 00:19 CST] Registry 状态 ANALYZING 是 cron 自动设置（s42 进程退出触发），但实验实际仍在进行中。random_s43 在 cuda:0 正常运行，step 1200/2810 (43%)。eval@500 R@1=0.5357, eval@1000 R@1=0.5285 (early_stopping 1/2)。Best R@1=0.5357 at step 500。GPU 100% 利用率, 50.5/97.9GB VRAM。\", \"metrics\": {\"random_s42\": {\"status\": \"DONE\", \"epoch\": \"3/3\", \"total_steps\": 4242, \"total_steps_per_epoch\": 1414, \"eval_500\": {\"val_loss\": 0.4869, \"recall_at_1\": 0.533, \"recall_at_5\": 0.954, \"recall_at_10\": 1}, \"eval_1000\": {\"val_loss\": 0.4651, \"recall_at_1\": 0.553, \"recall_at_5\": 0.959, \"recall_at_10\": 1}, \"eval_1500\": {\"val_loss\": 0.5365, \"recall_at_1\": 0.523, \"recall_at_5\": 0.955, \"recall_at_10\": 1}, \"eval_2000\": {\"val_loss\": 0.5162, \"recall_at_1\": 0.523, \"recall_at_5\": 0.954, \"recall_at_10\": 1}, \"eval_2500\": {\"val_loss\": 0.5264, \"recall_at_1\": 0.527, \"recall_at_5\": 0.956, \"recall_at_10\": 1}, \"eval_3000\": {\"val_loss\": 0.5406, \"recall_at_1\": 0.536, \"recall_at_5\": 0.956, \"recall_at_10\": 1}, \"best_checkpoint\": \"step_1000 (val_loss=0.4651, R@1=0.5527)\", \"conclusion\": \"Overfit after step 1000. Best R@1=0.5527, +1.7pp vs pilot (0.5357). Full data helps.\"}, \"random_s43\": {\"status\": \"DONE\", \"epoch\": \"early_stopped\", \"total_steps_per_epoch\": 1405, \"eval_500\": {\"val_loss\": 0.4476, \"recall_at_1\": 0.5357}, \"eval_1000\": {\"val_loss\": 0.4637, \"recall_at_1\": 0.5285}, \"eval_1500\": {\"recall_at_1\": 0.5554}, \"best_by_val_loss\": \"step 500 (val_loss=0.4476)\", \"best_by_recall_at_1\": \"step 1500 (R@1=0.5554)\", \"conclusion\": \"Early stopped at step 1500. Best R@1=0.5554, consistent with s42 (0.5527). val_loss and R@1 criterion diverge.\"}, \"random_s44\": {\"status\": \"RUNNING\", \"note\": \"Auto-started 01:58 CST, epoch 1/2, 1408 batches/epoch\"}, \"progress_snapshot\": \"2026-05-15T02:00 CST\"}, \"reproduce\": {\"finished_at\": \"2026-05-14T11:24:33.887Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T11:24:35.375104+00:00\"}]}}, \"plan_018_bm25\": {\"status\": \"QUEUED\", \"retry_count\": 0, \"created_at\": \"2026-05-14T16:38:40.603Z\", \"updated_at\": \"2026-05-14T17:09:50.985Z\", \"hypothesis\": \"BM25 negative baseline: Dream 审稿三档一致认定缺 BM25 baseline 是论文最大结构性缺陷。Phase 1 (CPU): 对 M2 训练语料建 BM25 索引，挖掘 BM25 hard negatives，生成训练数据。Phase 2 (GPU): 用 BM25 negatives 训练 Qwen + StarCoder 各 1 seed，对比 R@1。\", \"parent\": \"m2_full_qwen\", \"notes\": \"Phase 1 (CPU) COMPLETE: BM25 negative mining 完成。3 seeds 数据生成，record counts 与其他策略完全一致，0 fallback。BM25 score 分布: mean=246.50, std=155.96。重叠率: BM25 vs embedding_distance ~87.1%, vs random ~76.2%, vs dataflow_aware ~71.8%。高 median=1.0 因小 repo 候选池≤50 文件导致策略完全重合，BM25 differentiation 主要在大 repo。脚本: /root/structfuse/scripts/mine_bm25_negatives.py。输出: /root/autodl-tmp/structfuse/full_m2_training_data/{train,val}_bm25_s{42,43,44}.jsonl。Phase 2 (GPU): 等 re-dream gate 通过 + M2 完成后训练。\", \"metrics\": {\"phase1_complete\": true, \"seed_42\": {\"train_records\": 11308, \"val_records\": 2980, \"train_size_mb\": 1280.8, \"val_size_mb\": 344.6}, \"seed_43\": {\"train_records\": 11236, \"val_records\": 3052, \"train_size_mb\": 1280.9, \"val_size_mb\": 316}, \"seed_44\": {\"train_records\": 11264, \"val_records\": 3024, \"train_size_mb\": 1347.1, \"val_size_mb\": 295.9}, \"bm25_score_dist\": {\"count\": 392954, \"mean\": 246.5, \"std\": 155.96, \"p25\": 128.38, \"p50\": 228.41, \"p75\": 347.85, \"max\": 2585.74}, \"overlap_overall\": {\"bm25_vs_embedding\": 0.871, \"bm25_vs_random\": 0.762, \"bm25_vs_dataflow\": 0.718, \"note\": \"k=50 full candidate overlap from mining worker\"}, \"overlap_stratified_top7_jaccard\": {\"small_lt50\": {\"repos\": 39, \"bm25_vs_embedding\": 0.668, \"bm25_vs_random\": 0.411, \"bm25_vs_dataflow\": 0.667}, \"medium_50_200\": {\"repos\": 29, \"bm25_vs_embedding\": 0.38, \"bm25_vs_random\": 0.067, \"bm25_vs_dataflow\": 0.363}, \"large_200plus\": {\"repos\": 15, \"bm25_vs_embedding\": 0.297, \"bm25_vs_random\": 0.007, \"bm25_vs_dataflow\": 0.405}, \"matched_queries\": 2920, \"total_queries\": 12290, \"note\": \"top-7 Jaccard on s42 matched queries only (24% match rate due to different train/val splits)\"}}}, \"plan_015_dynamic\": {\"status\": \"QUEUED\", \"retry_count\": 0, \"created_at\": \"2026-05-14T17:03:24.316Z\", \"updated_at\": \"2026-05-14T17:03:30.544Z\", \"hypothesis\": \"Dynamic negative mining (epoch-level re-mining): 每 epoch 重新用当前 encoder embedding 挖掘 negatives，验证 static mining 是否足够。缩减版：只跑 dynamic_ep × 1 seed (Qwen, s42)，~11h 单卡。若 dynamic ≈ static（预期 <1pp 差异），在 Limitation 段排除 confound。\", \"notes\": \"Director D031 缩减：原 44h → 11h 单卡。只跑 dynamic_ep × 1 seed (Qwen, s42)，跳过 dynamic_500。Post-M2 与 plan_003 并行（一卡 SWE-bench，一卡 dynamic_ep）。受 re-dream gate 约束。设计文档已由 Worker 完成。\"}, \"neg_difficulty_analysis\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T19:39:20.016Z\", \"updated_at\": \"2026-05-14T00:13:49.046Z\", \"hypothesis\": \"Negative difficulty distribution analysis: 用预训练 Qwen2.5-Coder-3B 和 StarCoder2-3B 计算 3 策略 (random/embedding/dataflow) 的 query-negative/positive cosine similarity，分析 pretrained representation separability 跨编码器差异。MAX_LENGTH=2048 匹配训练设置。\", \"notes\": \"128 vs 2048 token 对比完成（2026-05-14 05:54 CST）。Qwen pos_sim 在 2048t 下 0.9855（比 128t 的 0.9804 更高），确认 ceiling 为 Qwen 表征的结构性特征，非截断 artifact。StarCoder margin 2.6-4.1x Qwen（2048t）。核心结论：pretrained representation separability varies across encoders，跨两种 token 长度成立。数据源：128t → stats_v2.json，2048t → stats_v3_2048.json。\", \"metrics\": {\"qwen_128\": {\"random\": {\"pos_sim\": 0.9804, \"neg_sim\": 0.899, \"margin\": 0.0816, \"pct_positive_margin\": 77.8}, \"embedding_distance\": {\"pos_sim\": 0.9804, \"neg_sim\": 0.959, \"margin\": 0.0209, \"pct_positive_margin\": 60.7}, \"dataflow_aware\": {\"pos_sim\": 0.9805, \"neg_sim\": 0.95, \"margin\": 0.0309, \"pct_positive_margin\": 67.4}}, \"starcoder_128\": {\"random\": {\"pos_sim\": 0.757, \"neg_sim\": 0.553, \"margin\": 0.2039, \"pct_positive_margin\": 72.8}, \"embedding_distance\": {\"pos_sim\": 0.784, \"neg_sim\": 0.668, \"margin\": 0.1159, \"pct_positive_margin\": 59.2}, \"dataflow_aware\": {\"pos_sim\": 0.761, \"neg_sim\": 0.659, \"margin\": 0.1022, \"pct_positive_margin\": 62.8}}, \"qwen_2048\": {\"random\": {\"pos_sim\": 0.9855, \"neg_sim\": 0.9111, \"margin\": 0.0743, \"margin_std\": 0.2322, \"pct_positive_margin\": 81.8}, \"embedding_distance\": {\"pos_sim\": 0.9855, \"neg_sim\": 0.9685, \"margin\": 0.017, \"margin_std\": 0.114, \"pct_positive_margin\": 58.8}, \"dataflow_aware\": {\"pos_sim\": 0.9856, \"neg_sim\": 0.9563, \"margin\": 0.0293, \"margin_std\": 0.1407, \"pct_positive_margin\": 73.9}}, \"starcoder_2048\": {\"random\": {\"pos_sim\": 0.7985, \"neg_sim\": 0.6045, \"margin\": 0.194, \"margin_std\": 0.2788, \"pct_positive_margin\": 78}, \"embedding_distance\": {\"pos_sim\": 0.8079, \"neg_sim\": 0.7409, \"margin\": 0.067, \"margin_std\": 0.2056, \"pct_positive_margin\": 55}, \"dataflow_aware\": {\"pos_sim\": 0.8009, \"neg_sim\": 0.6818, \"margin\": 0.1192, \"margin_std\": 0.2264, \"pct_positive_margin\": 70.4}}, \"sc_qwen_margin_ratio_128\": {\"random\": 2.5, \"embedding_distance\": 5.54, \"dataflow_aware\": 3.3}, \"sc_qwen_margin_ratio_2048\": {\"random\": 2.61, \"embedding_distance\": 3.94, \"dataflow_aware\": 4.07}}, \"conclusion\": \"success\", \"spec\": {\"command\": \"python negative_difficulty_margin_v2.py (CPU analysis)\", \"server\": \"bjb1-42106\", \"data_path\": \"/root/autodl-tmp/structfuse/full_m2_data/\", \"data_count\": 11000, \"model_name\": \"Qwen2.5-Coder-3B + StarCoder2-3B (pretrained, no training)\", \"seed\": \"N/A\", \"checkpoint_path\": \"N/A (analysis only)\", \"log_path\": \"/root/autodl-tmp/structfuse/artifacts/negative_difficulty_stats_v3_2048.json\"}, \"completed_at\": \"2026-05-14T00:13:49.046Z\"}, \"m1_reextract\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T19:35:23.954Z\", \"updated_at\": \"2026-05-13T19:45:53.741Z\", \"hypothesis\": \"M1 重提取：恢复 28,276 个因运行时瞬态文件系统故障失败的 instances（82 repos）。预期将训练数据从 15,897 提升至 ~44,173。D022 批准。\", \"parent\": \"m1_extraction\", \"spec\": {\"command\": \"bash scripts/rerun_m1_failed.sh (4 CPU workers, CodeQL 2-hop)\", \"server\": \"bjb1-42106\", \"data_path\": \"/root/autodl-tmp/structfuse/m1_extraction/\", \"data_count\": 28276, \"model_name\": \"N/A (CodeQL extraction)\", \"seed\": \"N/A\", \"pid\": \"97358\", \"log_path\": \"/root/runs/structfuse-context/m1_rerun.log\", \"checkpoint_source\": \"rerun of m1_extraction failed instances\", \"eval_data\": \"N/A\", \"checkpoint_path\": \"N/A (failed, no output)\"}, \"conclusion\": \"failed\", \"notes\": \"CodeQL query 100% 失败（exit status 2）。根因：Worker 安装 CodeQL CLI 2.25.4 时未执行 `codeql pack install`，`codeql/python-all@7.1.0` 标准库 pack 缺失。修复命令：`cd /root/structfuse/extraction/codeql_queries && /opt/codeql/codeql pack install`。已 kill 进程 + tmux session。无新数据产出（all.jsonl 未受影响）。等 Director 确认后修复重跑。\", \"completed_at\": \"2026-05-13T19:44:09.115Z\"}, \"m1_extraction\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-12T21:00:02.300Z\", \"updated_at\": \"2026-05-13T19:26:13.901Z\", \"spec\": {\"command\": \"nohup bash scripts/run_m1_extraction.sh (8 CPU workers, CodeQL 2-hop)\", \"server\": \"cqa1-21977\", \"data_path\": \"/root/autodl-tmp/structfuse/m1_extraction/\", \"data_count\": 50869, \"model_name\": \"N/A (CodeQL extraction)\", \"seed\": \"N/A\", \"description\": \"M1: 全量 5K repos CodeQL 提取, 131 unique (repo,commit) groups, 50869 instances\"}, \"metrics\": {\"total_instances_attempted\": 44173, \"instances_skipped\": 6696, \"total_instances\": 50869, \"codeql_success\": 15133, \"beniget_fallback\": 764, \"extraction_failed\": 28276, \"structural_data_rate\": 0.36, \"repos_with_output\": 123, \"repos_total\": 131, \"repo_coverage\": 0.939, \"skip_clone_failed\": 5852, \"skip_checkout_failed\": 836, \"skip_stale_handle\": 8, \"elapsed_minutes\": 837.8, \"avg_time_per_instance_s\": 8.9, \"output_size_gb\": 6.6, \"disk_usage_gb\": 13, \"output_file\": \"all.jsonl\"}, \"notes\": \"[2026-05-13 19:25] COMPLETED. 837.8min, 123/131 repos (93.9%), 15,897/44,173 instances with structural data (36.0%), 6,696 skipped (clone/checkout). Output: all.jsonl 6.6GB. [2026-05-13 19:23 UPDATE] 28,276 buggy_file_not_found errors 经验证并非上游数据质量问题——10/10 抽查的文件在 repo 中全部存在。根因是运行时瞬态文件系统故障（CodeQL 并行 database creation 导致磁盘耗尽，锐截止模式）。这些 instances 可通过重跑恢复。D022: 准备重跑脚本中，等 Director 确认后执行。\", \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/structfuse/m1_extraction/all.jsonl\", \"log_path\": \"/tmp/m1_extraction.log\", \"completed_at\": \"2026-05-13T10:59:42.462Z\"}, \"plan_006_scalability\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T07:57:43.631Z\", \"updated_at\": \"2026-05-13T19:24:00.741Z\", \"spec\": {\"command\": \"M1 scalability statistics analysis (29/131 repos)\", \"server\": \"bjb1-42106\", \"data_path\": \"/root/autodl-tmp/structfuse/m1_extraction/\", \"data_count\": 8171, \"model_name\": \"N/A (CPU analysis)\", \"seed\": \"N/A\", \"description\": \"Plan 006: M1 extraction scalability stats - timeout rate, extraction time, coverage, Z% by repo size. Partial results from 29/131 repos.\", \"checkpoint_path\": \"N/A\", \"log_path\": \"N/A\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-13T07:57:58.176Z\", \"notes\": \"[2026-05-13 19:23] 全量统计 + error 分析 + fuzzy match 验证完成。关键发现: (1) 0 timeout; (2) 28,276 error 全部 buggy_file_not_found，但 fuzzy match 验证发现文件实际都存在——根因是运行时瞬态文件系统故障（锐截止模式：每个 repo 内先成功后突然全部失败，extraction_time=0.0s），可能是 CodeQL 并行数据库创建导致磁盘空间耗尽; (3) 这些 instance 可通过重跑恢复（当前 resolve_file_in_repo 对全部样本返回正确路径）; (4) 结构数据率 34.3% 有望提升至接近 100%（若重跑成功）; (5) Z% 随 repo 规模上升 (XL median 96%). Artifacts: plan006_full_scalability.json, art_20260513_d262da (error patterns)\", \"hypothesis\": \"Claim 3: CodeQL bounded data-flow extraction scales to large repos with acceptable timeout rates and provides meaningful structural coverage (Z%) that increases with repo complexity\", \"metrics\": {\"repos\": 123, \"total_instances\": 44173, \"structural_data_rate\": 0.343, \"error_rate\": 0.64, \"zero_timeout_rate\": true, \"processing_time\": {\"mean_s\": 8.93, \"median_s\": 0, \"p95_s\": 31.95, \"max_s\": 633.68, \"total_hours\": 109.58}, \"by_tier\": {\"small_lt50\": {\"repos\": 1, \"instances\": 500, \"error_rate\": 0.054, \"struct_rate\": 0.81, \"z_pct_mean\": 0.284, \"z_pct_median\": 0}, \"medium_50_200\": {\"repos\": 17, \"instances\": 4096, \"error_rate\": 0.485, \"struct_rate\": 0.472, \"z_pct_mean\": 0.444, \"z_pct_median\": 0.5}, \"large_200_500\": {\"repos\": 40, \"instances\": 13628, \"error_rate\": 0.639, \"struct_rate\": 0.343, \"z_pct_mean\": 0.604, \"z_pct_median\": 0.857}, \"xlarge_500plus\": {\"repos\": 29, \"instances\": 25949, \"error_rate\": 0.676, \"struct_rate\": 0.314, \"z_pct_mean\": 0.812, \"z_pct_median\": 0.96}}, \"instance_distribution\": {\"lt10\": 1, \"10_50\": 17, \"50_200\": 36, \"200_500\": 40, \"500plus\": 29}, \"artifact\": \"plan006_full_scalability.json\"}}, \"plan_013_starcoder\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T05:09:14.885Z\", \"updated_at\": \"2026-05-13T18:09:54.153Z\", \"hypothesis\": \"Architecture generalization: validate StructFuse with StarCoder2-3B encoder (vs Qwen2.5-Coder-3B in m2_embed_verify). If both encoders show same strategy ranking → method is encoder-agnostic, strengthening the core claim. Key differentiator for best→accept at Dream.\", \"spec\": {\"command\": \"bash -c \\\"bash /root/structfuse/run_plan013_starcoder.sh\\\"\", \"server\": \"bjb1-42106\", \"gpu\": [\"cuda:0\"], \"pid\": \"23798\", \"log_path\": \"~/runs/structfuse-context/plan_013_starcoder.log\", \"submitted_at\": \"2026-05-13T05:26:21.946Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/structfuse/m2_embed_verify_data/\", \"data_count\": 3282, \"model_name\": \"bigcode/starcoder2-3b\", \"seed\": 42, \"wall_clock_seconds\": 35338.2, \"gpu_hours\": 9.82}, \"notes\": \"[2026-05-13 16:00] ALL 3 STRATEGIES DONE. Ranking: embedding (R@1=0.5078) > random (0.4922) > dataflow (0.4869). Embedding vs random: +1.6pp (consistent with Qwen). Dataflow vs random: -0.5pp (DIFFERS from Qwen where dataflow > random +0.8pp). Hypothesis NEGATIVE: strategy ranking NOT identical across encoders. Embedding > random is encoder-agnostic, dataflow position is encoder-dependent. Log: /root/runs/faith-evidence-ie/plan_013_starcoder.log. Cron misreported EXIT_CODE=129 but all strategies completed (confirmed via log extraction worker).\", \"metrics\": {\"random\": {\"status\": \"DONE\", \"best_val_loss\": 0.5113, \"best_recall@1\": 0.4922, \"best_recall@5\": 0.98, \"best_recall@10\": 1, \"source\": \"/tmp/eval_random_s42.log (post-hoc eval, no in-training eval)\"}, \"embedding_distance\": {\"status\": \"DONE\", \"best_step\": 1000, \"best_val_loss\": 0.4816, \"best_recall@1\": 0.5078, \"best_recall@5\": 0.9843, \"best_recall@10\": 1, \"final_val_loss\": 0.506, \"final_recall@1\": 0.5174}, \"dataflow_aware\": {\"status\": \"DONE\", \"best_step\": 1000, \"best_val_loss\": 0.5255, \"best_recall@1\": 0.4869, \"best_recall@5\": 0.9695, \"best_recall@10\": 1, \"final_val_loss\": 0.5509, \"final_recall@1\": 0.5078}}, \"failure_reason\": \"\", \"conclusion\": \"negative\", \"completed_at\": \"2026-05-13T15:15:20.165Z\"}, \"m2_embed_verify\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T04:39:16.051Z\", \"updated_at\": \"2026-05-13T15:59:51.621Z\", \"hypothesis\": \"True embedding mining verification: compare Qwen2.5-Coder-3B cosine similarity negatives vs BM25 negatives on pilot data (24 repos). If true embedding negatives are harder → Claim 2 (structure-aware negatives improve retrieval) gets stronger evidence.\", \"parent\": \"m2_early_pilot\", \"spec\": {\"command\": \"bash -c \\\"bash /root/structfuse/run_m2_embed_verify.sh\\\"\", \"server\": \"bjb1-42106\", \"gpu\": [\"cuda:1\"], \"pid\": \"29290\", \"log_path\": \"~/runs/structfuse-context/m2_embed_verify.log\", \"submitted_at\": \"2026-05-13T06:37:00.822Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/structfuse/m2_embed_verify_data/\", \"data_count\": 3282, \"model_name\": \"Qwen/Qwen2.5-Coder-3B\", \"seed\": 42, \"checkpoint_source\": \"training from scratch (not eval)\", \"eval_data\": \"N/A (training, not eval)\", \"wall_clock_seconds\": 31097.9, \"gpu_hours\": 8.64}, \"notes\": \"[2026-05-13 16:00] ALL 3 STRATEGIES DONE. Ranking: embedding (R@1=0.5557) > dataflow (0.5436) > random (0.5357). Embedding vs random: +2.0pp. Dataflow vs random: +0.8pp. All best at step 500, overfitting after. Hypothesis confirmed: true embedding negatives are harder → Claim 2 supported. Log: /root/runs/faith-evidence-ie/m2_embed_verify.log. Cron misreported EXIT_CODE=2 but all strategies completed successfully (confirmed via log extraction worker).\", \"metrics\": {\"random\": {\"status\": \"DONE\", \"best_step\": 500, \"best_val_loss\": 0.4834, \"best_recall@1\": 0.5357, \"best_recall@5\": 0.9808, \"best_recall@10\": 1, \"final_val_loss\": 0.5978, \"final_recall@1\": 0.5122}, \"embedding_distance\": {\"status\": \"DONE\", \"best_step\": 500, \"best_val_loss\": 0.4603, \"best_recall@1\": 0.5557, \"best_recall@5\": 0.9808, \"best_recall@10\": 1, \"final_val_loss\": 0.5935, \"final_recall@1\": 0.5209}, \"dataflow_aware\": {\"status\": \"DONE\", \"best_step\": 500, \"best_val_loss\": 0.5602, \"best_recall@1\": 0.5436, \"best_recall@5\": 0.9817, \"best_recall@10\": 1, \"final_val_loss\": 0.6201, \"final_recall@1\": 0.5287}}, \"failure_reason\": \"EXIT_CODE=2 (shell misuse / syntax)\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-13T15:15:18.746Z\"}, \"mvp_p2b_contrastive_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-12T15:03:02.370Z\", \"updated_at\": \"2026-05-13T07:23:28.932Z\", \"spec\": {\"command\": \"bash scripts/run_p2b_all.sh (9 runs: 3 strategies × 3 seeds)\", \"server\": \"cqa1-21977\", \"gpu\": [\"cuda:4\"], \"pid\": \"132149\", \"data_path\": \"/root/structfuse/mvp_data/training_data/\", \"data_count\": 127, \"model_name\": \"Qwen2.5-Coder-3B + LoRA\", \"seed\": \"42,123,7\", \"hypothesis\": \"H3: data-flow hard negatives vs random vs embedding-distance, 3-seed × 3-strategy contrastive training\", \"plan_id\": \"mvp_p2b_contrastive_training\", \"checkpoint_path\": \"N/A\", \"log_path\": \"N/A\"}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-12T15:04:44.396Z\", \"notes\": \"P2b 对比训练 v2，因磁盘空间不足被 kill。已被 p2b_5reruns（成功完成 9/9 runs）替代。\"}, \"p2b_dataflow_retrain\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-12T19:49:00.303Z\", \"updated_at\": \"2026-05-13T07:23:27.706Z\", \"spec\": {\"command\": \"build_p2b_data.py regeneration + dataflow 3-seed retrain\", \"server\": \"cqa1-21977\", \"data_path\": \"/root/structfuse\", \"data_count\": 0, \"model_name\": \"Qwen2.5-Coder-3B (LoRA)\", \"seed\": \"42,123,456\", \"description\": \"BLOCKED: dataflow connections ⊆ gold files, strategies indistinguishable\", \"checkpoint_path\": \"N/A\", \"log_path\": \"N/A\"}, \"conclusion\": \"negative\", \"completed_at\": \"2026-05-13T04:17:02.055Z\", \"notes\": \"Dataflow 策略重训练计划，因 embedding_distance 命名问题（实际用 BM25 而非 embedding）被 Reviewer 发现后搁置。已被 m2_embed_verify（true embedding mining）替代。\"}, \"p2b_eval_all\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-12T16:27:50.967Z\", \"updated_at\": \"2026-05-13T07:23:24.721Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/structfuse && bash scripts/run_eval_all.sh\\\"\", \"server\": \"cqa1-21977\", \"gpu\": [\"cuda:4\"], \"pid\": \"254053\", \"log_path\": \"N/A\", \"submitted_at\": \"2026-05-12T16:27:50.945Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_path\": \"N/A\", \"wall_clock_seconds\": 42550.6, \"gpu_hours\": 11.82}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-13T04:17:01.561Z\", \"notes\": \"P2b 全量 eval（pool_size=26），被 D013 服务器迁移计划取消。已被 p2b_eval_4runs_pool50（pool_size=50）替代。\"}, \"m2_early_pilot\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T01:39:53.920Z\", \"updated_at\": \"2026-05-13T04:44:22.077Z\", \"hypothesis\": \"Early pilot on partial M1 data (24 repos, ~5K instances): verify M2 training pipeline works end-to-end and get early signal on 3-strategy differentiation before full M1 completes\", \"spec\": {\"command\": \"bash /root/structfuse/scripts/run_m2_pilot.sh\", \"server\": \"cqa1-21977\", \"gpu\": [\"cuda:4\"], \"pid\": \"795739\", \"log_path\": \"/root/autodl-tmp/structfuse/m2_pilot_output/random_s42.log\", \"submitted_at\": \"2026-05-13T01:55:31.288Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/structfuse/m2_pilot_data/\", \"data_count\": 3418, \"model_name\": \"Qwen/Qwen2.5-Coder-3B\", \"seed\": 42, \"checkpoint_source\": \"N/A (training from scratch)\", \"eval_data\": \"N/A (training, not eval)\", \"checkpoint_path\": \"/root/autodl-tmp/structfuse/m2_pilot_output/random_s42/best_model.pt\", \"wall_clock_seconds\": 10130.8, \"gpu_hours\": 2.81}, \"conclusion\": \"killed\", \"notes\": \"PID 795791 在 cqa1 cuda:4 运行，wrapper 脚本顺序跑 random→embedding→dataflow（set -e）。random 策略跑到 step 4000 后卡住（~45min 无新日志），embedding/dataflow 未启动。Best checkpoint at step 1500。Val_loss 持续恶化（0.5879→0.728），明显过拟合。另有 OOM 进程干扰（某进程试图在同 GPU 启动导致 OOM，可能破坏 GPU 状态）。eval recall@k bug 已确认。\", \"metrics\": {\"pid\": 795791, \"gpu\": \"cuda:4\", \"gpu_mem_mb\": 9342, \"gpu_util_pct\": 83, \"batch_size\": 2, \"num_negatives\": 3, \"max_seq_length\": 1024, \"strategy_running\": \"random (stuck at step 4000, epoch 3)\", \"strategies_completed\": \"0/3\", \"eval_1500\": {\"val_loss\": 0.5879, \"recall_at_1\": 0.4693, \"recall_at_5\": 0.4693, \"recall_at_10\": 0.4693}, \"eval_2000\": {\"val_loss\": 0.7089, \"recall_at_1\": 0.4398}, \"eval_2500\": {\"val_loss\": 0.6961, \"recall_at_1\": 0.4291}, \"eval_3000\": {\"val_loss\": 0.728, \"recall_at_1\": 0.4104}, \"eval_3500\": {\"val_loss\": 0.7022, \"recall_at_1\": 0.4439}, \"best_checkpoint\": \"step_1500 (val_loss=0.5879, 6.2GB)\", \"WARNING\": \"recall@1=recall@5=recall@10 confirmed eval bug. Process hung after step 4000 (~45min no output). Overfitting after step 1500.\", \"status_check_at\": \"2026-05-13T04:42:00Z\"}, \"completed_at\": \"2026-05-13T04:44:22.077Z\"}, \"m2_early_pilot_v3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T01:59:06.557Z\", \"updated_at\": \"2026-05-13T02:13:43.400Z\", \"spec\": {\"command\": \"bash -c \\\"bash /root/structfuse/run_m2_early_pilot.sh\\\"\", \"server\": \"cqa1-21977\", \"gpu\": [\"cuda:0\"], \"pid\": \"897651\", \"log_path\": \"~/runs/structfuse-context/m2_early_pilot_v3.log\", \"submitted_at\": \"2026-05-13T02:04:31.768Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_path\": \"N/A\", \"wall_clock_seconds\": 551.6, \"gpu_hours\": 0.15}, \"conclusion\": \"killed\", \"notes\": \"GPU 越界 cuda:0，违反项目 GPU 分配 gpu_ids=[\\\"cuda:4\\\"]。第二次 GPU 越界违规（首次 D005）。Worker 未正确映射 CUDA_VISIBLE_DEVICES。\", \"completed_at\": \"2026-05-13T02:13:43.400Z\"}, \"m2_early_pilot_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T01:52:52.724Z\", \"updated_at\": \"2026-05-13T02:13:31.039Z\", \"spec\": {\"command\": \"bash /root/structfuse/run_m2_early_pilot.sh\", \"server\": \"cqa1-21977\", \"gpu\": [\"cuda:4\"], \"pid\": \"766124\", \"log_path\": \"~/runs/structfuse-context/m2_early_pilot_v2.log\", \"submitted_at\": \"2026-05-13T01:52:52.687Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/structfuse/m2_early_pilot_data/\", \"data_count\": 3418, \"model_name\": \"Qwen/Qwen2.5-Coder-3B\", \"seed\": 42, \"checkpoint_source\": \"N/A (training from scratch)\", \"eval_data\": \"N/A (this is training, not eval)\", \"checkpoint_path\": \"N/A\", \"wall_clock_seconds\": 1238.4, \"gpu_hours\": 0.34}, \"hypothesis\": \"Early pilot on partial M1 data (24 repos, 2672 train + 746 val): verify M2 training pipeline works end-to-end and get early signal on 3-strategy differentiation before full M1 completes\", \"parent\": \"m1_extraction\", \"notes\": \"wandb API key error, EXIT_CODE=1。首次提交因 wandb 未配置离线模式而立即退出。\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-13T02:13:31.040Z\"}, \"mvp_p2b_contrastive_training\": {\"status\": \"DONE\", \"retry_count\": 2, \"created_at\": \"2026-05-12T12:37:44.628Z\", \"updated_at\": \"2026-05-13T01:31:27.220Z\", \"reproduce\": {\"finished_at\": \"2026-05-12T16:19:50.297Z\"}, \"failure_reason\": \"EXIT_CODE=2 (shell misuse / syntax)\", \"completed_at\": \"2026-05-12T13:16:21.735Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-12T13:16:22.517958+00:00\"}, {\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-12T15:15:47.933008+00:00\"}, {\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-12T16:19:51.082427+00:00\"}], \"previous_failure\": {\"conclusion\": \"failed\", \"notes\": \"第2次失败: random策略3seeds全部完成(s42跳过/s123 recall@5=0.984/s456 recall@5=0.992), 但embedding策略s42启动即EXIT_CODE=2(shell syntax error). Worker worker_diagnose_mvp_p2b_contrastive_training_v2 正在诊断和修复run_p2b_all.sh的embedding配置部分\"}}, \"notes\": \"4/9 runs 完成 (random×3 + embedding_distance_s42), 5/9 失败 (磁盘满 torch.save RuntimeError). /root/autodl-tmp 93% (14GB剩余, 每个checkpoint 5.8GB). 失败从 embedding_distance_s123 开始级联.\", \"spec\": {\"command\": \"bash scripts/run_p2b_all.sh (9 runs: 3 strategies × 3 seeds)\", \"server\": \"cqa1-21977\", \"gpu\": [\"cuda:4\"], \"pid\": \"238645\", \"data_path\": \"/root/structfuse/mvp_data/training_data/\", \"data_count\": 127, \"model_name\": \"Qwen2.5-Coder-3B + LoRA\", \"seed\": \"42,123,456\", \"hypothesis\": \"H3: data-flow hard negatives vs random vs embedding-distance, 3-seed × 3-strategy contrastive training\", \"plan_id\": \"mvp_p2b_contrastive_training\", \"checkpoint_path\": \"/root/autodl-tmp/structfuse/checkpoints/\", \"log_path\": \"/tmp/p2b_all_runs.log\"}, \"metrics\": {\"random_s42_recall1\": 0.984, \"random_s123_recall1\": 0.984, \"random_s456_recall1\": 0.992, \"embedding_s42_recall1\": 0.874, \"random_mean_recall1\": 0.987, \"runs_completed\": 4, \"runs_failed\": 5, \"failure_type\": \"disk_full_torch_save\"}, \"conclusion\": \"killed\"}, \"p2b_eval_4runs_pool50\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-12T20:10:54.579Z\", \"updated_at\": \"2026-05-13T00:27:50.197Z\", \"spec\": {\"command\": \"eval_p2b.py on 4 checkpoints with new val.jsonl pool_size=50\", \"server\": \"cqa1-21977\", \"data_path\": \"/root/structfuse\", \"data_count\": 127, \"model_name\": \"Qwen2.5-Coder-3B (LoRA)\", \"seed\": \"42,123,456\", \"checkpoint_source\": \"p2b_5reruns (random×3 + emb_dist×1)\", \"eval_data\": \"val.jsonl pool_size=50\"}, \"conclusion\": \"success\", \"metrics\": {\"pool_size\": 50, \"n_samples\": 127, \"random_s42\": {\"recall@1\": 0.496, \"recall@5\": 0.843, \"recall@10\": 0.945}, \"random_s123\": {\"recall@1\": 0.535, \"recall@5\": 0.85, \"recall@10\": 0.921}, \"random_s456\": {\"recall@1\": 0.543, \"recall@5\": 0.843, \"recall@10\": 0.953}, \"emb_dist_s42\": {\"recall@1\": 0.488, \"recall@5\": 0.835, \"recall@10\": 0.874}, \"random_mean\": {\"recall@1\": 0.525, \"recall@5\": 0.845, \"recall@10\": 0.94}, \"emb_dist_vs_random_delta\": {\"recall@1\": -0.037, \"recall@5\": -0.01, \"recall@10\": -0.066}}, \"checkpoint_path\": \"/root/autodl-tmp/structfuse/checkpoints/ (p2b_random_s42/123/456, p2b_embedding_distance_s42)\", \"log_path\": \"已清理 (2026-05-12 Director Step 1 指令 rm -rf)，metrics 保留在 registry\", \"completed_at\": \"2026-05-12T20:11:12.318Z\"}, \"d007_50repo_overlap\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-12T20:37:24.289Z\", \"updated_at\": \"2026-05-12T20:37:39.566Z\", \"spec\": {\"command\": \"CodeQL 2-hop extraction + connected vs gold overlap stats on 50 repos\", \"server\": \"cqa1-21977\", \"data_path\": \"/root/structfuse\", \"data_count\": 240, \"model_name\": \"N/A (CPU analysis)\", \"seed\": \"N/A\", \"description\": \"50-repo overlap validation: Z=40.8%, original method viable\"}, \"conclusion\": \"success\", \"metrics\": {\"total_instances\": 240, \"instances_with_extra_connected\": 98, \"Z_pct\": 40.8, \"avg_connected_minus_gold\": 6, \"codeql_timeout_rate_pct\": 4, \"by_repo_size\": {\"small_lt50\": {\"Z_pct\": 38.6, \"avg_extra\": 2.5}, \"medium_50_200\": {\"Z_pct\": 55.7, \"avg_extra\": 11.8}, \"large_gt200\": {\"Z_pct\": 16.7, \"avg_extra\": 8.8}}, \"decision\": \"Z=40.8% >= 20% -> original method viable, proceed to M1\"}, \"checkpoint_path\": \"N/A (analysis only)\", \"log_path\": \"/root/structfuse/data/50repo_overlap_stats/\", \"completed_at\": \"2026-05-12T20:37:39.566Z\"}, \"p2b_5reruns\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-12T17:26:47.603Z\", \"updated_at\": \"2026-05-12T19:19:53.785Z\", \"spec\": {\"command\": \"bash run_p2b_all.sh (skips 4 done, runs 5: emb_dist s123/456, dataflow s42/123/456)\", \"server\": \"cqa1-21977\", \"gpu\": [\"cuda:4\"], \"pid\": \"272732\", \"log_path\": \"~/runs/structfuse-context/p2b_5reruns.log\", \"submitted_at\": \"2026-05-12T17:26:47.575Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/structfuse\", \"data_count\": 500, \"model_name\": \"Qwen2.5-Coder-3B (LoRA)\", \"seed\": \"42,123,456\", \"description\": \"Phase 2b 5 reruns: emb_dist s123/456 + dataflow_aware s42/123/456\", \"hyperparams\": {\"batch_size\": 2, \"lr\": \"2e-5\", \"num_negatives\": 3, \"max_seq_length\": 512, \"use_lora\": true, \"gradient_checkpointing\": true, \"eval_steps\": 50, \"save_steps\": 200, \"num_epochs\": 3}, \"wall_clock_seconds\": 6752.2, \"gpu_hours\": 1.88}, \"conclusion\": \"success\", \"metrics\": {\"random_s42\": {\"val_loss\": 0.0347, \"recall@1\": 0.9843}, \"random_s123\": {\"val_loss\": 0.0446, \"recall@1\": 0.9843}, \"random_s456\": {\"val_loss\": 0.0188, \"recall@1\": 0.9921}, \"emb_dist_s42\": {\"val_loss\": 0.1876, \"recall@1\": 0.874}, \"emb_dist_s123\": {\"val_loss\": 0.1461, \"recall@1\": 0.874}, \"emb_dist_s456\": {\"val_loss\": 0.1281, \"recall@1\": 0.8819}, \"dataflow_s42\": {\"val_loss\": 0.1878, \"recall@1\": 0.874}, \"dataflow_s123\": {\"val_loss\": 0.146, \"recall@1\": 0.874}, \"dataflow_s456\": {\"val_loss\": 0.1278, \"recall@1\": 0.8819}, \"runs_completed\": 9, \"runs_failed\": 0, \"WARNING\": \"dataflow_aware ≈ embedding_distance to 4 decimal places across all seeds — likely code bug in negative sampling\"}, \"checkpoint_path\": \"/root/autodl-tmp/structfuse/checkpoints/ (9 dirs: p2b_{random,embedding_distance,dataflow_aware}_s{42,123,456})\", \"completed_at\": \"2026-05-12T19:19:19.793Z\", \"log_path\": \"~/runs/structfuse-context/p2b_5reruns.log\"}, \"p2b_eval_4runs_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-12T17:21:49.599Z\", \"updated_at\": \"2026-05-12T17:22:16.595Z\", \"spec\": {\"command\": \"eval 4 runs (3 random seeds + 1 emb_dist) with pool_size=26\", \"server\": \"cqa1-21977\", \"data_path\": \"/root/structfuse\", \"data_count\": 127, \"model_name\": \"Qwen2.5-Coder-3B (LoRA)\", \"seed\": \"42,123,456\", \"description\": \"Phase 2b eval v2: pool_size=26 评估 random vs emb_dist\"}, \"conclusion\": \"success\", \"metrics\": {\"random_seed42\": {\"recall@1\": 0.9449, \"recall@5\": 0.9843, \"recall@10\": 0.9843}, \"random_seed123\": {\"recall@1\": 0.9449, \"recall@5\": 0.9921, \"recall@10\": 0.9921}, \"random_seed456\": {\"recall@1\": 0.9291, \"recall@5\": 0.9921, \"recall@10\": 0.9921}, \"emb_dist_seed42\": {\"recall@1\": 0.6693, \"recall@5\": 0.8898, \"recall@10\": 0.9291}, \"pool_size\": 26, \"n_samples\": 127}, \"checkpoint_path\": \"/root/autodl-tmp/structfuse/checkpoints/ (4 runs: random_s42/123/456, emb_dist_s42)\", \"log_path\": \"/root/autodl-tmp/structfuse/eval_results/\", \"completed_at\": \"2026-05-12T17:22:16.595Z\"}, \"p2b-all-9runs\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-12T12:34:24.923Z\", \"updated_at\": \"2026-05-12T15:05:49.244Z\", \"spec\": {\"command\": \"obsolete smoke test\", \"server\": \"cqa1-21977\", \"gpu\": [\"cuda:4\"], \"pid\": \"92636\", \"log_path\": \"N/A\", \"submitted_at\": \"2026-05-12T12:34:24.908Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"N/A\", \"data_count\": 0, \"model_name\": \"N/A\", \"seed\": 42, \"checkpoint_path\": \"N/A\", \"wall_clock_seconds\": 9084.3, \"gpu_hours\": 2.52}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-12T15:05:49.244Z\"}, \"p2b-smoke8\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-12T12:32:22.931Z\", \"updated_at\": \"2026-05-12T15:05:48.324Z\", \"spec\": {\"command\": \"obsolete smoke test\", \"server\": \"cqa1-21977\", \"gpu\": [\"cuda:4\"], \"pid\": \"91698\", \"log_path\": \"N/A\", \"submitted_at\": \"2026-05-12T12:32:22.916Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"N/A\", \"data_count\": 0, \"model_name\": \"N/A\", \"seed\": 42, \"checkpoint_path\": \"N/A\", \"wall_clock_seconds\": 9205.4, \"gpu_hours\": 2.56}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-12T15:05:48.324Z\"}, \"p2b-smoke7\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-12T12:28:55.114Z\", \"updated_at\": \"2026-05-12T15:05:47.346Z\", \"spec\": {\"command\": \"obsolete smoke test\", \"server\": \"cqa1-21977\", \"gpu\": [\"cuda:4\"], \"pid\": \"90758\", \"log_path\": \"N/A\", \"submitted_at\": \"2026-05-12T12:28:55.101Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"N/A\", \"data_count\": 0, \"model_name\": \"N/A\", \"seed\": 42, \"checkpoint_path\": \"N/A\", \"wall_clock_seconds\": 9412.2, \"gpu_hours\": 2.61}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-12T15:05:47.346Z\"}, \"p2b-smoke6\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-12T12:22:54.445Z\", \"updated_at\": \"2026-05-12T15:05:46.413Z\", \"spec\": {\"command\": \"obsolete smoke test\", \"server\": \"cqa1-21977\", \"gpu\": [\"cuda:4\"], \"pid\": \"89257\", \"log_path\": \"N/A\", \"submitted_at\": \"2026-05-12T12:22:54.433Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"N/A\", \"data_count\": 0, \"model_name\": \"N/A\", \"seed\": 42, \"checkpoint_path\": \"N/A\", \"wall_clock_seconds\": 9772.0, \"gpu_hours\": 2.71}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-12T15:05:46.413Z\"}, \"p2b-smoke5\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-12T12:22:05.754Z\", \"updated_at\": \"2026-05-12T15:05:45.484Z\", \"spec\": {\"command\": \"obsolete smoke test\", \"server\": \"cqa1-21977\", \"gpu\": [\"cuda:4\"], \"pid\": \"88719\", \"log_path\": \"N/A\", \"submitted_at\": \"2026-05-12T12:22:05.744Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"N/A\", \"data_count\": 0, \"model_name\": \"N/A\", \"seed\": 42, \"checkpoint_path\": \"N/A\", \"wall_clock_seconds\": 9819.7, \"gpu_hours\": 2.73}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-12T15:05:45.484Z\"}, \"p2b-smoke4\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-12T12:20:53.305Z\", \"updated_at\": \"2026-05-12T15:05:44.066Z\", \"spec\": {\"command\": \"obsolete smoke test\", \"server\": \"cqa1-21977\", \"gpu\": [\"cuda:4\"], \"pid\": \"87968\", \"log_path\": \"N/A\", \"submitted_at\": \"2026-05-12T12:20:53.296Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"N/A\", \"data_count\": 0, \"model_name\": \"N/A\", \"seed\": 42, \"checkpoint_path\": \"N/A\", \"wall_clock_seconds\": 9890.8, \"gpu_hours\": 2.75}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-12T15:05:44.066Z\"}, \"p2b-smoke3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-12T12:18:19.105Z\", \"updated_at\": \"2026-05-12T15:05:43.111Z\", \"spec\": {\"command\": \"obsolete smoke test\", \"server\": \"cqa1-21977\", \"gpu\": [\"cuda:4\"], \"pid\": \"86879\", \"log_path\": \"N/A\", \"submitted_at\": \"2026-05-12T12:18:19.098Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"N/A\", \"data_count\": 0, \"model_name\": \"N/A\", \"seed\": 42, \"checkpoint_path\": \"N/A\", \"wall_clock_seconds\": 10044.0, \"gpu_hours\": 2.79}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-12T15:05:43.111Z\"}, \"p2b-smoke2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-12T12:16:08.154Z\", \"updated_at\": \"2026-05-12T15:05:42.174Z\", \"spec\": {\"command\": \"obsolete smoke test\", \"server\": \"cqa1-21977\", \"gpu\": [\"cuda:4\"], \"pid\": \"85793\", \"log_path\": \"N/A\", \"submitted_at\": \"2026-05-12T12:16:08.148Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"N/A\", \"data_count\": 0, \"model_name\": \"N/A\", \"seed\": 42, \"checkpoint_path\": \"N/A\", \"wall_clock_seconds\": 10174.0, \"gpu_hours\": 2.83}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-12T15:05:42.174Z\"}, \"p2b-smoke-test\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-12T12:14:30.477Z\", \"updated_at\": \"2026-05-12T15:05:41.269Z\", \"spec\": {\"command\": \"obsolete smoke test\", \"server\": \"cqa1-21977\", \"gpu\": [\"cuda:4\"], \"pid\": \"84805\", \"log_path\": \"N/A\", \"submitted_at\": \"2026-05-12T12:14:30.472Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"N/A\", \"data_count\": 0, \"model_name\": \"N/A\", \"seed\": 42, \"checkpoint_path\": \"N/A\", \"wall_clock_seconds\": 10270.8, \"gpu_hours\": 2.85}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-12T15:05:41.270Z\"}, \"mvp_p2a_linear_proxy\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-12T11:53:42.223Z\", \"updated_at\": \"2026-05-12T11:58:15.436Z\", \"spec\": {\"command\": \"python evaluation/linear_proxy.py (logistic regression on data-flow features + BM25)\", \"server\": \"cqa1-21977\", \"data_path\": \"/root/autodl-tmp/mvp_results/ + /root/structfuse/mvp_data/bm25/\", \"data_count\": 8, \"model_name\": \"LogisticRegression (scikit-learn)\", \"seed\": null, \"hypothesis\": \"H2-confirm: data-flow features 的线性分类器预测 bug-relevant 文件优于纯 BM25 baseline\", \"plan_id\": \"mvp_p2a_linear_proxy\"}, \"conclusion\": \"success\", \"metrics\": {\"df_bm25_auc\": 0.78, \"bm25_only_auc\": 0.476, \"auc_delta\": 0.304, \"df_bm25_mrr\": 0.556, \"bm25_only_mrr\": 0.115, \"mrr_delta\": 0.441, \"df_bm25_f1\": 0.143, \"bm25_only_f1\": 0.039, \"top_feature\": \"is_connected (+2.82)\", \"repos_evaluated\": 3, \"note\": \"3 repos / 3 positive samples, directional evidence\"}, \"checkpoint_path\": \"N/A (logistic regression, no checkpoint)\", \"log_path\": \"/root/structfuse/evaluation/linear_proxy.py output\", \"completed_at\": \"2026-05-12T11:58:15.436Z\"}, \"mvp_p1_codeql_feasibility\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-12T11:30:45.938Z\", \"updated_at\": \"2026-05-12T11:58:06.197Z\", \"spec\": {\"command\": \"python extraction/extract_dataflow.py + codeql query run (call_graph.ql + bounded_dataflow.ql)\", \"server\": \"cqa1-21977\", \"data_path\": \"/root/structfuse/mvp_data/repos (8 SWE-smith instances: flask, requests, pytest, pylint, xarray, astropy, sphinx, matplotlib)\", \"data_count\": 8, \"model_name\": \"N/A (CPU pipeline)\", \"seed\": null, \"hypothesis\": \"H1: CodeQL 2-hop bounded data-flow timeout <30%; H2: connected files gold patch coverage significantly > disconnected\", \"plan_id\": \"mvp_p1_codeql_feasibility\"}, \"conclusion\": \"success\", \"metrics\": {\"timeout_rate\": 0, \"repos_processed\": 8, \"repos_skipped\": 2, \"cg_mean_s\": 29.6, \"cg_max_s\": 119.8, \"df_mean_s\": 43.4, \"df_max_s\": 167.1, \"h2_connected_coverage\": 0.014815, \"h2_disconnected_coverage\": 0, \"h2_fisher_p\": 6.5e-09, \"h2_gold_in_connected_ratio\": 1, \"h2_note\": \"After path normalization fix: 8/8 gold in connected (was 6/8)\"}, \"log_path\": \"/root/autodl-tmp/mvp_results/mvp_phase1_report.json\", \"checkpoint_path\": \"N/A (CPU pipeline, no model checkpoint)\", \"completed_at\": \"2026-05-12T11:31:16.335Z\"}}, \"count\": 37, \"total\": 37, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.1285}}"
    }
  },
  "sourceToolAssistantUUID": "92f9db10-91c6-4b49-ab86-0265e6e87d50",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "b1d97499-4652-4822-8fc5-dbdc566ceedc",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-14T21:32:02.412Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01YTZHDtqqhxR1Y5ZVWKMW6J`</summary>

```json
{
  "query": "RepoGraph \"code graph\" paper ICLR 2025 Ouyang"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "559b8273-647c-408d-beb6-ef4861c15620",
  "isSidechain": false,
  "requestId": "req_011Cb3B9xuuWHpBt93h9CBmU",
  "type": "assistant",
  "uuid": "ec314abc-1cd5-4f19-a6e2-541382f833f7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "b1d97499-4652-4822-8fc5-dbdc566ceedc",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CcDHjcV436JSRpZV9kkdu1",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8929,
      "cache_read_input_tokens": 25758,
      "output_tokens": 353,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 8929,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 353,
          "cache_read_input_tokens": 25758,
          "cache_creation_input_tokens": 8929,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 8929
          },
          "type": "message"
        }
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

_source line 27 · 2026-05-14T21:32:02.887Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01MchdAfoSoPCjVYdb41VWGW`</summary>

```json
{
  "query": "GraphCoder \"data-flow\" code retrieval ASE 2024 Liu"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ec314abc-1cd5-4f19-a6e2-541382f833f7",
  "isSidechain": false,
  "requestId": "req_011Cb3B9xuuWHpBt93h9CBmU",
  "type": "assistant",
  "uuid": "4b15db70-7e18-4a50-b73a-23897a42312b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "b1d97499-4652-4822-8fc5-dbdc566ceedc",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CcDHjcV436JSRpZV9kkdu1",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8929,
      "cache_read_input_tokens": 25758,
      "output_tokens": 353,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 8929,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 353,
          "cache_read_input_tokens": 25758,
          "cache_creation_input_tokens": 8929,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 8929
          },
          "type": "message"
        }
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

_source line 28 · 2026-05-14T21:32:03.398Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01QzWURT6UppBCWcqAgnMPwY`</summary>

```json
{
  "query": "ARISE \"repository-level graph\" fault localization program repair Seddik Fard 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4b15db70-7e18-4a50-b73a-23897a42312b",
  "isSidechain": false,
  "requestId": "req_011Cb3B9xuuWHpBt93h9CBmU",
  "type": "assistant",
  "uuid": "e8fe99a9-34a4-468c-b7e9-24587be6bf76",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "b1d97499-4652-4822-8fc5-dbdc566ceedc",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CcDHjcV436JSRpZV9kkdu1",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8929,
      "cache_read_input_tokens": 25758,
      "output_tokens": 353,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 8929,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 353,
          "cache_read_input_tokens": 25758,
          "cache_creation_input_tokens": 8929,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 8929
          },
          "type": "message"
        }
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

_source line 29_

```json
{
  "type": "last-prompt",
  "leafUuid": "e8fe99a9-34a4-468c-b7e9-24587be6bf76",
  "sessionId": "b1d97499-4652-4822-8fc5-dbdc566ceedc"
}
```

---

### Runtime record

_source line 30_

```json
{
  "type": "ai-title",
  "aiTitle": "Fix literature reference consistency issues",
  "sessionId": "b1d97499-4652-4822-8fc5-dbdc566ceedc"
}
```

---

### Tool result

_source line 31 · 2026-05-14T21:32:07.964Z_

<details><summary>↩ Tool result · `toolu_01YTZHDtqqhxR1Y5ZVWKMW6J`</summary>

```text
Web search results for query: "RepoGraph "code graph" paper ICLR 2025 Ouyang"

Links: [{"title":"Enhancing AI Software Engineering with Repository-level Code Graph RepoGraph:","url":"https://iclr.cc/media/iclr-2025/Slides/28957.pdf"},{"title":"Published as a conference paper at ICLR 2025","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/4a4a3c197deac042461c677219efd36c-Paper-Conference.pdf"},{"title":"REPOGRAPH: ENHANCING AI SOFTWARE ENGINEERING WITH REPOSITORY-LEVEL CODE GRAPH - Illinois Experts","url":"https://experts.illinois.edu/en/publications/repograph-enhancing-ai-software-engineering-with-repository-level/"},{"title":"RepoGraph: Enhancing AI Software Engineering with Repository-level Code Graph | OpenReview","url":"https://openreview.net/forum?id=dw9VUsSHGB"},{"title":"[2410.14684] RepoGraph: Enhancing AI Software Engineering with Repository-level Code Graph","url":"https://arxiv.org/abs/2410.14684"},{"title":"ICLR Poster RepoGraph: Enhancing AI Software Engineering with Repository-level Code Graph","url":"https://iclr.cc/virtual/2025/poster/28957"},{"title":"Selected Publications - Wenhao Yu’s Homepage","url":"https://wyu97.github.io/publications/"},{"title":"RepoGraph: Enhancing AI Software Engineering with Repository-level Code Graph","url":"https://arxiv.org/html/2410.14684v1"},{"title":"ICLR 2025 Papers","url":"https://iclr.cc/virtual/2025/papers.html"},{"title":"[Quick Review] RepoGraph: Enhancing AI Software Engineering with Repository-level Code Graph","url":"https://liner.com/review/repograph-enhancing-ai-software-engineering-with-repositorylevel-code-graph"}]

I found the research paper you're looking for. Here's what I found:

RepoGraph: Enhancing AI Software Engineering with Repository-level Code Graph was published at the 13th International Conference on Learning Representations (ICLR 2025).

**Key Information:**

- **Authors:** Siru Ouyang, Wenhao Yu, Kaixin Ma, Zilin Xiao, Zhihan Zhang, Mengzhao Jia, Jiawei Han, Hongming Zhang, and Dong Yu

- **Main Contribution:** RepoGraph is a plug-in module that manages a repository-level structure for modern AI software engineering solutions and serves as a repository-wide navigation for AI software engineers

- **Key Technical Approach:** RepoGraph constructs a repository using code lines as fundamental building units, represented as a graph G = {V, E}, where each node corresponds to a code line and edges capture relationships between these code lines

- **Evaluation and Results:** RepoGraph was evaluated on SWE-bench by plugging it into four different methods, substantially boosting the performance of all systems and leading to a new state-of-the-art among open-source frameworks

- **Code Availability:** The paper and code are available at https://arxiv.org/abs/2410.14684 and https://github.com/ozyyshr/RepoGraph respectively


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ec314abc-1cd5-4f19-a6e2-541382f833f7",
  "isSidechain": false,
  "promptId": "255fffc4-c17f-4b3b-8b5c-7a3031fdb918",
  "type": "user",
  "uuid": "409f1aad-be1c-48be-b766-0c59b9d63738",
  "toolUseResult": {
    "query": "RepoGraph \"code graph\" paper ICLR 2025 Ouyang",
    "results": [
      {
        "tool_use_id": "srvtoolu_01X9ZAQ8Zx9JLwnuhREn58LQ",
        "content": [
          {
            "title": "Enhancing AI Software Engineering with Repository-level Code Graph RepoGraph:",
            "url": "https://iclr.cc/media/iclr-2025/Slides/28957.pdf"
          },
          {
            "title": "Published as a conference paper at ICLR 2025",
            "url": "https://proceedings.iclr.cc/paper_files/paper/2025/file/4a4a3c197deac042461c677219efd36c-Paper-Conference.pdf"
          },
          {
            "title": "REPOGRAPH: ENHANCING AI SOFTWARE ENGINEERING WITH REPOSITORY-LEVEL CODE GRAPH - Illinois Experts",
            "url": "https://experts.illinois.edu/en/publications/repograph-enhancing-ai-software-engineering-with-repository-level/"
          },
          {
            "title": "RepoGraph: Enhancing AI Software Engineering with Repository-level Code Graph | OpenReview",
            "url": "https://openreview.net/forum?id=dw9VUsSHGB"
          },
          {
            "title": "[2410.14684] RepoGraph: Enhancing AI Software Engineering with Repository-level Code Graph",
            "url": "https://arxiv.org/abs/2410.14684"
          },
          {
            "title": "ICLR Poster RepoGraph: Enhancing AI Software Engineering with Repository-level Code Graph",
            "url": "https://iclr.cc/virtual/2025/poster/28957"
          },
          {
            "title": "Selected Publications - Wenhao Yu’s Homepage",
            "url": "https://wyu97.github.io/publications/"
          },
          {
            "title": "RepoGraph: Enhancing AI Software Engineering with Repository-level Code Graph",
            "url": "https://arxiv.org/html/2410.14684v1"
          },
          {
            "title": "ICLR 2025 Papers",
            "url": "https://iclr.cc/virtual/2025/papers.html"
          },
          {
            "title": "[Quick Review] RepoGraph: Enhancing AI Software Engineering with Repository-level Code Graph",
            "url": "https://liner.com/review/repograph-enhancing-ai-software-engineering-with-repositorylevel-code-graph"
          }
        ]
      },
      "I found the research paper you're looking for. Here's what I found:\n\nRepoGraph: Enhancing AI Software Engineering with Repository-level Code Graph was published at the 13th International Conference on Learning Representations (ICLR 2025).\n\n**Key Information:**\n\n- **Authors:** Siru Ouyang, Wenhao Yu, Kaixin Ma, Zilin Xiao, Zhihan Zhang, Mengzhao Jia, Jiawei Han, Hongming Zhang, and Dong Yu\n\n- **Main Contribution:** RepoGraph is a plug-in module that manages a repository-level structure for modern AI software engineering solutions and serves as a repository-wide navigation for AI software engineers\n\n- **Key Technical Approach:** RepoGraph constructs a repository using code lines as fundamental building units, represented as a graph G = {V, E}, where each node corresponds to a code line and edges capture relationships between these code lines\n\n- **Evaluation and Results:** RepoGraph was evaluated on SWE-bench by plugging it into four different methods, substantially boosting the performance of all systems and leading to a new state-of-the-art among open-source frameworks\n\n- **Code Availability:** The paper and code are available at https://arxiv.org/abs/2410.14684 and https://github.com/ozyyshr/RepoGraph respectively"
    ],
    "durationSeconds": 5.546467783
  },
  "sourceToolAssistantUUID": "ec314abc-1cd5-4f19-a6e2-541382f833f7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "b1d97499-4652-4822-8fc5-dbdc566ceedc",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-14T21:32:09.294Z_

<details><summary>↩ Tool result · `toolu_01MchdAfoSoPCjVYdb41VWGW`</summary>

```text
Web search results for query: "GraphCoder "data-flow" code retrieval ASE 2024 Liu"

Links: [{"title":"[2406.07003] GraphCoder: Enhancing Repository-Level Code Completion via Code Context Graph-based Retrieval and Language Model","url":"https://arxiv.org/abs/2406.07003"},{"title":"GraphCoder: Enhancing Repository-Level Code Completion via Coarse-to-fine Retrieval Based on Code Context Graph (ASE 2024 - Research Papers) - ASE 2024","url":"https://conf.researchr.org/details/ase-2024/ase-2024-research/46/GraphCoder-Enhancing-Repository-Level-Code-Completion-via-Coarse-to-fine-Retrieval-B"},{"title":"GraphCoder: Enhancing Repository-Level Code Completion via Coarse-to-fine Retrieval Based on Code Context Graph | Proceedings of the 39th IEEE/ACM International Conference on Automated Software Engineering","url":"https://dl.acm.org/doi/10.1145/3691620.3695054"},{"title":"[PDF] GraphCoder: Enhancing Repository-Level Code Completion via Code Context Graph-based Retrieval and Language Model | Semantic Scholar","url":"https://www.semanticscholar.org/paper/GraphCoder:-Enhancing-Repository-Level-Code-via-and-Liu-Yu/793bbb3c70d4bac3908bd8f2ecc309f1bfdf5f52"},{"title":"GraphCoder: Enhancing Repository-Level Code Completion via Coarse-to-fine Retrieval Based on Code Context Graph | Request PDF","url":"https://www.researchgate.net/publication/385287286_GraphCoder_Enhancing_Repository-Level_Code_Completion_via_Coarse-to-fine_Retrieval_Based_on_Code_Context_Graph"},{"title":"GitHub - oceaneLIU/GraphCoder","url":"https://github.com/oceaneLIU/GraphCoder"},{"title":"2024 39th IEEE/ACM International Conference on ...","url":"https://www.computer.org/csdl/proceedings/ase/2024/22gEsOsLriM"},{"title":"39th ASE 2024: Sacramento, CA, USA","url":"https://dblp.org/db/conf/kbse/ase2024.html"},{"title":"GraphCoder: Enhancing Repository-Level Code Completion via Code Context Graph-based Retrieval and Language Model","url":"https://arxiv.org/html/2406.07003v2"},{"title":"GraphCoder | NL2Code","url":"https://nl2code.github.io/posts/GraphCoder/"}]

Based on the search results, I found information about GraphCoder, a paper presented at ASE 2024:

## GraphCoder: Code Context Graph-Based Retrieval for Code Completion

GraphCoder is a retrieval-augmented code completion framework that leverages LLMs' general code knowledge and repository-specific knowledge via a graph-based retrieval-generation process.

### Key Features

GraphCoder captures the context of the completion target through code context graph (CCG) that consists of control-flow, data- and control-dependence between code statements, providing a more structured way to capture context than sequence-based approaches, and employs a coarse-to-fine retrieval process to locate context-similar code snippets from the current repository.

### Performance

Compared to baseline retrieval-augmented methods, GraphCoder achieves higher exact match (EM) on average, with increases of +6.06 in code match and +6.23 in identifier match, while using less time and space.

### Authors and Conference

The paper was authored by Wei Liu, Ailun Yu, Daoguang Zan, Bo Shen, Wei Zhang, Haiyan Zhao, Zhi Jin, and Qianxiang Wang, and presented at ASE 2024.

The paper addresses the limitation that code language models lack repository-specific knowledge needed for effective code completion at the repository level.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4b15db70-7e18-4a50-b73a-23897a42312b",
  "isSidechain": false,
  "promptId": "255fffc4-c17f-4b3b-8b5c-7a3031fdb918",
  "type": "user",
  "uuid": "0adeb73d-f513-4977-a38c-74f47e8157d2",
  "toolUseResult": {
    "query": "GraphCoder \"data-flow\" code retrieval ASE 2024 Liu",
    "results": [
      {
        "tool_use_id": "srvtoolu_019ff9q48MqjNV9ZQcFEtr3k",
        "content": [
          {
            "title": "[2406.07003] GraphCoder: Enhancing Repository-Level Code Completion via Code Context Graph-based Retrieval and Language Model",
            "url": "https://arxiv.org/abs/2406.07003"
          },
          {
            "title": "GraphCoder: Enhancing Repository-Level Code Completion via Coarse-to-fine Retrieval Based on Code Context Graph (ASE 2024 - Research Papers) - ASE 2024",
            "url": "https://conf.researchr.org/details/ase-2024/ase-2024-research/46/GraphCoder-Enhancing-Repository-Level-Code-Completion-via-Coarse-to-fine-Retrieval-B"
          },
          {
            "title": "GraphCoder: Enhancing Repository-Level Code Completion via Coarse-to-fine Retrieval Based on Code Context Graph | Proceedings of the 39th IEEE/ACM International Conference on Automated Software Engineering",
            "url": "https://dl.acm.org/doi/10.1145/3691620.3695054"
          },
          {
            "title": "[PDF] GraphCoder: Enhancing Repository-Level Code Completion via Code Context Graph-based Retrieval and Language Model | Semantic Scholar",
            "url": "https://www.semanticscholar.org/paper/GraphCoder:-Enhancing-Repository-Level-Code-via-and-Liu-Yu/793bbb3c70d4bac3908bd8f2ecc309f1bfdf5f52"
          },
          {
            "title": "GraphCoder: Enhancing Repository-Level Code Completion via Coarse-to-fine Retrieval Based on Code Context Graph | Request PDF",
            "url": "https://www.researchgate.net/publication/385287286_GraphCoder_Enhancing_Repository-Level_Code_Completion_via_Coarse-to-fine_Retrieval_Based_on_Code_Context_Graph"
          },
          {
            "title": "GitHub - oceaneLIU/GraphCoder",
            "url": "https://github.com/oceaneLIU/GraphCoder"
          },
          {
            "title": "2024 39th IEEE/ACM International Conference on ...",
            "url": "https://www.computer.org/csdl/proceedings/ase/2024/22gEsOsLriM"
          },
          {
            "title": "39th ASE 2024: Sacramento, CA, USA",
            "url": "https://dblp.org/db/conf/kbse/ase2024.html"
          },
          {
            "title": "GraphCoder: Enhancing Repository-Level Code Completion via Code Context Graph-based Retrieval and Language Model",
            "url": "https://arxiv.org/html/2406.07003v2"
          },
          {
            "title": "GraphCoder | NL2Code",
            "url": "https://nl2code.github.io/posts/GraphCoder/"
          }
        ]
      },
      "Based on the search results, I found information about GraphCoder, a paper presented at ASE 2024:\n\n## GraphCoder: Code Context Graph-Based Retrieval for Code Completion\n\nGraphCoder is a retrieval-augmented code completion framework that leverages LLMs' general code knowledge and repository-specific knowledge via a graph-based retrieval-generation process.\n\n### Key Features\n\nGraphCoder captures the context of the completion target through code context graph (CCG) that consists of control-flow, data- and control-dependence between code statements, providing a more structured way to capture context than sequence-based approaches, and employs a coarse-to-fine retrieval process to locate context-similar code snippets from the current repository.\n\n### Performance\n\nCompared to baseline retrieval-augmented methods, GraphCoder achieves higher exact match (EM) on average, with increases of +6.06 in code match and +6.23 in identifier match, while using less time and space.\n\n### Authors and Conference\n\nThe paper was authored by Wei Liu, Ailun Yu, Daoguang Zan, Bo Shen, Wei Zhang, Haiyan Zhao, Zhi Jin, and Qianxiang Wang, and presented at ASE 2024.\n\nThe paper addresses the limitation that code language models lack repository-specific knowledge needed for effective code completion at the repository level."
    ],
    "durationSeconds": 6.403487023000001
  },
  "sourceToolAssistantUUID": "4b15db70-7e18-4a50-b73a-23897a42312b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "b1d97499-4652-4822-8fc5-dbdc566ceedc",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 33 · 2026-05-14T21:32:11.706Z_

<details><summary>↩ Tool result · `toolu_01QzWURT6UppBCWcqAgnMPwY`</summary>

```text
Web search results for query: "ARISE "repository-level graph" fault localization program repair Seddik Fard 2025"

Links: [{"title":"[2605.03117] ARISE: A Repository-level Graph Representation and Toolset for Agentic Fault Localization and Program Repair","url":"https://arxiv.org/abs/2605.03117"},{"title":"ARISE: A Repository-level Graph Representation and Toolset for Agentic Fault Localization and Program Repair","url":"https://arxiv.org/html/2605.03117"},{"title":"Enhancing Repository-Level Software Repair via Repository-Aware Knowledge Graphs","url":"https://arxiv.org/html/2503.21710v1"},{"title":"On the Role of Fault Localization Context for LLM-Based Program Repair","url":"https://arxiv.org/html/2604.05481"},{"title":"Advancements in automated program repair: a comprehensive review | Knowledge and Information Systems | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s10115-025-02383-9"},{"title":"A Study on the Impact of Fault localization Granularity for Repository-Scale Code Repair Tasks","url":"https://arxiv.org/html/2604.00167"},{"title":"A Survey of LLM-based Automated Program Repair: Taxonomies, Design Paradigms, and Applications","url":"https://arxiv.org/html/2506.23749v1"},{"title":"Evaluating the usage of fault localization in automated program repair: an empirical study","url":"https://explore.openaire.eu/search/publication?pid=10.1007/s11704-020-9263-1"},{"title":"[2503.21710] Enhancing repository-level software repair via repository-aware knowledge graphs","url":"https://arxiv.org/abs/2503.21710"},{"title":"Hybrid Automated Program Repair by Combining Large Language","url":"https://xgdsmileboy.github.io/files/paper/tosem25-hybrid.pdf"}]

Based on the search results, I found information about ARISE, which appears to be the primary paper matching your query.

## ARISE: Repository-level Graph Representation for Fault Localization and Program Repair

ARISE (Agentic Repository-level Issue Solving Engine) augments an LLM-based agent with a multi-granularity program graph that extends structural relationships down to statement-level nodes connected by intra-procedural definition-use edges, and exposes this graph through a three-tier tool API, which brings data-flow slicing as a first-class, queryable agent primitive that allows the model to trace, in a single call, which statements define or consume a variable of interest.

### Key Innovations

Existing graph-based systems provide structural representations of repositories (files, classes, functions and their relationships) but do not model how variable values flow within procedures, leaving agents without the semantic precision needed for function- and line-level localization. ARISE addresses this gap by providing statement-level granularity and data-flow information.

### Evaluation Results

The system was evaluated on SWE-bench Lite (300 real GitHub issues, 11 Python repositories) using Qwen2.5-Coder-32B-Instruct as the backbone, and compared to the unmodified SWE-agent baseline, ARISE improves Function Recall@1 by 17.0 points and Line Recall@1 by 15.0 points, with ARISE achieving 22.0% Pass@1 (66/300), a 4.7 percentage-point improvement over SWE-agent.

The paper appears to have been published recently (approximately 2 weeks ago according to the source metadata) and is authored by Shahd Seddik and another author.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e8fe99a9-34a4-468c-b7e9-24587be6bf76",
  "isSidechain": false,
  "promptId": "255fffc4-c17f-4b3b-8b5c-7a3031fdb918",
  "type": "user",
  "uuid": "6dc7d48e-21a2-4726-aafb-fa21527fee18",
  "toolUseResult": {
    "query": "ARISE \"repository-level graph\" fault localization program repair Seddik Fard 2025",
    "results": [
      {
        "tool_use_id": "srvtoolu_01KPqdAT2fURjt2m4WZ17Cpn",
        "content": [
          {
            "title": "[2605.03117] ARISE: A Repository-level Graph Representation and Toolset for Agentic Fault Localization and Program Repair",
            "url": "https://arxiv.org/abs/2605.03117"
          },
          {
            "title": "ARISE: A Repository-level Graph Representation and Toolset for Agentic Fault Localization and Program Repair",
            "url": "https://arxiv.org/html/2605.03117"
          },
          {
            "title": "Enhancing Repository-Level Software Repair via Repository-Aware Knowledge Graphs",
            "url": "https://arxiv.org/html/2503.21710v1"
          },
          {
            "title": "On the Role of Fault Localization Context for LLM-Based Program Repair",
            "url": "https://arxiv.org/html/2604.05481"
          },
          {
            "title": "Advancements in automated program repair: a comprehensive review | Knowledge and Information Systems | Springer Nature Link",
            "url": "https://link.springer.com/article/10.1007/s10115-025-02383-9"
          },
          {
            "title": "A Study on the Impact of Fault localization Granularity for Repository-Scale Code Repair Tasks",
            "url": "https://arxiv.org/html/2604.00167"
          },
          {
            "title": "A Survey of LLM-based Automated Program Repair: Taxonomies, Design Paradigms, and Applications",
            "url": "https://arxiv.org/html/2506.23749v1"
          },
          {
            "title": "Evaluating the usage of fault localization in automated program repair: an empirical study",
            "url": "https://explore.openaire.eu/search/publication?pid=10.1007/s11704-020-9263-1"
          },
          {
            "title": "[2503.21710] Enhancing repository-level software repair via repository-aware knowledge graphs",
            "url": "https://arxiv.org/abs/2503.21710"
          },
          {
            "title": "Hybrid Automated Program Repair by Combining Large Language",
            "url": "https://xgdsmileboy.github.io/files/paper/tosem25-hybrid.pdf"
          }
        ]
      },
      "Based on the search results, I found information about ARISE, which appears to be the primary paper matching your query.\n\n## ARISE: Repository-level Graph Representation for Fault Localization and Program Repair\n\nARISE (Agentic Repository-level Issue Solving Engine) augments an LLM-based agent with a multi-granularity program graph that extends structural relationships down to statement-level nodes connected by intra-procedural definition-use edges, and exposes this graph through a three-tier tool API, which brings data-flow slicing as a first-class, queryable agent primitive that allows the model to trace, in a single call, which statements define or consume a variable of interest.\n\n### Key Innovations\n\nExisting graph-based systems provide structural representations of repositories (files, classes, functions and their relationships) but do not model how variable values flow within procedures, leaving agents without the semantic precision needed for function- and line-level localization. ARISE addresses this gap by providing statement-level granularity and data-flow information.\n\n### Evaluation Results\n\nThe system was evaluated on SWE-bench Lite (300 real GitHub issues, 11 Python repositories) using Qwen2.5-Coder-32B-Instruct as the backbone, and compared to the unmodified SWE-agent baseline, ARISE improves Function Recall@1 by 17.0 points and Line Recall@1 by 15.0 points, with ARISE achieving 22.0% Pass@1 (66/300), a 4.7 percentage-point improvement over SWE-agent.\n\nThe paper appears to have been published recently (approximately 2 weeks ago according to the source metadata) and is authored by Shahd Seddik and another author."
    ],
    "durationSeconds": 8.305553645000003
  },
  "sourceToolAssistantUUID": "e8fe99a9-34a4-468c-b7e9-24587be6bf76",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "b1d97499-4652-4822-8fc5-dbdc566ceedc",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 34 · 2026-05-14T21:32:11.710Z_

```json
{
  "parentUuid": "6dc7d48e-21a2-4726-aafb-fa21527fee18",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "537477ae-6725-4c95-8d78-1b97a834fae2",
  "timestamp": "2026-05-14T21:32:11.710Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "b1d97499-4652-4822-8fc5-dbdc566ceedc",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 35 · 2026-05-14T21:32:22.183Z_

<details><summary>Logged reasoning block</summary>

```text
Let me process the findings:

1. **RepoGraph**: Confirmed real. "RepoGraph: Enhancing AI Software Engineering with Repository-level Code Graph" by Siru Ouyang, Wenhao Yu, Kaixin Ma, Zilin Xiao, Zhihan Zhang, Mengzhao Jia, Jiawei Han, Hongming Zhang, Dong Yu. ICLR 2025. ✓ matches discussion_v2.md citation.

2. **GraphCoder**: Confirmed real. "GraphCoder: Enhancing Repository-Level Code Completion via Coarse-to-fine Retrieval Based on Code Context Graph" by Wei Liu, Ailun Yu, Daoguang Zan, Bo Shen, Wei Zhang, Haiyan Zhao, Zhi Jin, Qianxiang Wang. ASE 2024. ✓ matches discussion_v2.md citation.
   
3. **ARISE**: Looking at the arXiv ID 2605.03117 - the format YYMM.xxxxx means this was posted in May 2026, so discussion_v2.md's "2026" is correct while literature_map.yaml's "2025" is wrong.

Now I need to find plan_017_literature in the registry to check what's there.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "537477ae-6725-4c95-8d78-1b97a834fae2",
  "isSidechain": false,
  "requestId": "req_011Cb3BB8mWoidtd6orTopBp",
  "type": "assistant",
  "uuid": "c36743b6-eed8-42af-bb08-15d87a9c58ee",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "b1d97499-4652-4822-8fc5-dbdc566ceedc",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KbSk6adyKmPKMBcbdYht1t",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4508,
      "cache_read_input_tokens": 34687,
      "output_tokens": 668,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4508,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 668,
          "cache_read_input_tokens": 34687,
          "cache_creation_input_tokens": 4508,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4508
          },
          "type": "message"
        }
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

_source line 36 · 2026-05-14T21:32:22.185Z_

All three papers confirmed real. Now let me find the plan_017_literature registry entry.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c36743b6-eed8-42af-bb08-15d87a9c58ee",
  "isSidechain": false,
  "requestId": "req_011Cb3BB8mWoidtd6orTopBp",
  "type": "assistant",
  "uuid": "33ecd42c-29e3-41e8-b918-a11cdb1637f2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "b1d97499-4652-4822-8fc5-dbdc566ceedc",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KbSk6adyKmPKMBcbdYht1t",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4508,
      "cache_read_input_tokens": 34687,
      "output_tokens": 668,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4508,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 668,
          "cache_read_input_tokens": 34687,
          "cache_creation_input_tokens": 4508,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4508
          },
          "type": "message"
        }
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

_source line 37 · 2026-05-14T21:32:23.654Z_

<details open><summary>🔧 Tool call — Bash · `toolu_019t1wXY2zDaipXwF6Q54KaQ`</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-5-projects-structfuse-context/b1d97499-4652-4822-8fc5-dbdc566ceedc/tool-results/toolu_01KYorBUb5wJHZKTYaT5g6Gh.txt | grep -A 100 \"plan_017_literature\" | head -120",
  "description": "Search for plan_017_literature in registry output"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "33ecd42c-29e3-41e8-b918-a11cdb1637f2",
  "isSidechain": false,
  "requestId": "req_011Cb3BB8mWoidtd6orTopBp",
  "type": "assistant",
  "uuid": "908ec8f0-7e8b-4d75-ae1a-a0ce2a303737",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "b1d97499-4652-4822-8fc5-dbdc566ceedc",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KbSk6adyKmPKMBcbdYht1t",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4508,
      "cache_read_input_tokens": 34687,
      "output_tokens": 668,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4508,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 668,
          "cache_read_input_tokens": 34687,
          "cache_creation_input_tokens": 4508,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4508
          },
          "type": "message"
        }
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

_source line 38 · 2026-05-14T21:32:23.851Z_

<details><summary>↩ Tool result · `toolu_019t1wXY2zDaipXwF6Q54KaQ`</summary>

```text
&lt;persisted-output>
Output too large (54.7KB). Full output saved to: /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-5-projects-structfuse-context/b1d97499-4652-4822-8fc5-dbdc566ceedc/tool-results/bv76ai3j3.txt

Preview (first 2KB):
{"result":"{\"success\": true, \"data\": {\"experiments\": {\"m1_reextract_v2\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-13T20:00:20.578Z\", \"updated_at\": \"2026-05-14T21:18:48.643Z\", \"hypothesis\": \"M1 重提取 v2：恢复 28,276 个因运行时瞬态文件系统故障失败的 instances（82 repos）。CodeQL pack 已修复，端到端测试通过。预期将训练数据从 15,897 提升至 ~44,173。D022 批准。\", \"parent\": \"m1_extraction\", \"spec\": {\"command\": \"bash scripts/rerun_m1_failed.sh (4 CPU workers, CodeQL 2-hop, pack installed)\", \"server\": \"bjb1-42106\", \"data_path\": \"/root/autodl-tmp/structfuse/full_m1_data/\", \"data_count\": 28276, \"model_name\": \"N/A (CodeQL extraction)\", \"seed\": \"N/A\", \"log_path\": \"/root/runs/structfuse-context/m1_reextract_v2.log\", \"checkpoint_source\": \"rerun of m1_extraction failed instances (v2, CodeQL fixed)\", \"eval_data\": \"N/A\"}, \"notes\": \"M1 重提取 v2：CodeQL pack 已修复，端到端测试通过。28,276 instances / 82 repo groups / 4 workers 并行。启动 2026-05-14 03:59 CST。[诊断 07:06 CST] 活跃运行中，~15/82 groups 完成，2,469 次 call_graph 查询成功，预计还需 ~13-16h。仅前 4 个旧 repo（furl/pyasn1/feedparser/python-docx）复用 v1 旧 DB 有 18 次降级 WARNING，04:02 之后零失败。产出写入 all.jsonl（追加模式）。磁盘 97GB 可用。[Director 决策 Session 8] 即使数据量增至 ~44K，不重跑 M2（ARR May 25 DDL 不允许再加 4-5 天重训）。处理方式：(1) post-M2 完成后如有 GPU 空档，跑 1-seed pilot (Qwen, embedding, 新数据) 对比当前 M2 baseline; (2) 论文中作为 scalability/data efficiency 讨论点; (3) 全量重训留 camera-ready。[进度检查 2026-05-15 05:05 CST] 80.8% 完成（22,842/28,276），0 ERROR，速率 ~560/hr，处理中大 repo：mozilla__bleach/sqlfluff/conan-io/Project-MONAI。产出为单独 .json 文件，尚未合并 all.jsonl。预计 ~15:00 CST May 15 完成。\", \"metrics\": {\"checked_at\": \"2026-05-15T05:15Z\", \"process\": \"alive (CPU, 4 workers)\", \"started\": \"2026-05-14T03:59Z\", \"elapsed_hours\": 25, \"total_instances\": 28276, \"repo_groups\": 82, \"output_json_files\": 40225, \"all_jsonl_lines\": 44173, \"active_repos\": {\"sqlfluff/sqlfluff\": \"250/1272\", \"mozilla/bleach\": \"350/455\", \"conan-io/conan\": \"450/972\", \"Project-MONAI/MONAI\": \"150/524\"
...
&lt;/persisted-output>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "908ec8f0-7e8b-4d75-ae1a-a0ce2a303737",
  "isSidechain": false,
  "promptId": "255fffc4-c17f-4b3b-8b5c-7a3031fdb918",
  "type": "user",
  "uuid": "52fd78e1-937c-40f4-b1dc-b96969ba45c9",
  "toolUseResult": {
    "stdout": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"experiments\\\": {\\\"m1_reextract_v2\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-13T20:00:20.578Z\\\", \\\"updated_at\\\": \\\"2026-05-14T21:18:48.643Z\\\", \\\"hypothesis\\\": \\\"M1 重提取 v2：恢复 28,276 个因运行时瞬态文件系统故障失败的 instances（82 repos）。CodeQL pack 已修复，端到端测试通过。预期将训练数据从 15,897 提升至 ~44,173。D022 批准。\\\", \\\"parent\\\": \\\"m1_extraction\\\", \\\"spec\\\": {\\\"command\\\": \\\"bash scripts/rerun_m1_failed.sh (4 CPU workers, CodeQL 2-hop, pack installed)\\\", \\\"server\\\": \\\"bjb1-42106\\\", \\\"data_path\\\": \\\"/root/autodl-tmp/structfuse/full_m1_data/\\\", \\\"data_count\\\": 28276, \\\"model_name\\\": \\\"N/A (CodeQL extraction)\\\", \\\"seed\\\": \\\"N/A\\\", \\\"log_path\\\": \\\"/root/runs/structfuse-context/m1_reextract_v2.log\\\", \\\"checkpoint_source\\\": \\\"rerun of m1_extraction failed instances (v2, CodeQL fixed)\\\", \\\"eval_data\\\": \\\"N/A\\\"}, \\\"notes\\\": \\\"M1 重提取 v2：CodeQL pack 已修复，端到端测试通过。28,276 instances / 82 repo groups / 4 workers 并行。启动 2026-05-14 03:59 CST。[诊断 07:06 CST] 活跃运行中，~15/82 groups 完成，2,469 次 call_graph 查询成功，预计还需 ~13-16h。仅前 4 个旧 repo（furl/pyasn1/feedparser/python-docx）复用 v1 旧 DB 有 18 次降级 WARNING，04:02 之后零失败。产出写入 all.jsonl（追加模式）。磁盘 97GB 可用。[Director 决策 Session 8] 即使数据量增至 ~44K，不重跑 M2（ARR May 25 DDL 不允许再加 4-5 天重训）。处理方式：(1) post-M2 完成后如有 GPU 空档，跑 1-seed pilot (Qwen, embedding, 新数据) 对比当前 M2 baseline; (2) 论文中作为 scalability/data efficiency 讨论点; (3) 全量重训留 camera-ready。[进度检查 2026-05-15 05:05 CST] 80.8% 完成（22,842/28,276），0 ERROR，速率 ~560/hr，处理中大 repo：mozilla__bleach/sqlfluff/conan-io/Project-MONAI。产出为单独 .json 文件，尚未合并 all.jsonl。预计 ~15:00 CST May 15 完成。\\\", \\\"metrics\\\": {\\\"checked_at\\\": \\\"2026-05-15T05:15Z\\\", \\\"process\\\": \\\"alive (CPU, 4 workers)\\\", \\\"started\\\": \\\"2026-05-14T03:59Z\\\", \\\"elapsed_hours\\\": 25, \\\"total_instances\\\": 28276, \\\"repo_groups\\\": 82, \\\"output_json_files\\\": 40225, \\\"all_jsonl_lines\\\": 44173, \\\"active_repos\\\": {\\\"sqlfluff/sqlfluff\\\": \\\"250/1272\\\", \\\"mozilla/bleach\\\": \\\"350/455\\\", \\\"conan-io/conan\\\": \\\"450/972\\\", \\\"Project-MONAI/MONAI\\\": \\\"150/524\\\"}, \\\"estimated_total_hours\\\": 60, \\\"progress_pct_by_time\\\": \\\"~42%\\\", \\\"disk\\\": \\\"98GB free on /root/autodl-tmp\\\"}}, \\\"m2_full_starcoder_resumed\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-14T18:44:19.253Z\\\", \\\"updated_at\\\": \\\"2026-05-14T21:18:45.080Z\\\", \\\"hypothesis\\\": \\\"M2 StarCoder resumed: 继续 m2_full_starcoder 的 8 sequential runs (random×2 + embedding×3 + dataflow×3)。原实验因 cron timeout 标记为 failed，实际 PID 519791 正常运行。\\\", \\\"spec\\\": {\\\"command\\\": \\\"bash run_m2_full_starcoder_resume.sh (8 runs: random_s43→s44→embedding×3→dataflow×3)\\\", \\\"server\\\": \\\"bjb1-42106\\\", \\\"gpu\\\": [\\\"cuda:1\\\"], \\\"pid\\\": \\\"519791\\\", \\\"log_path\\\": \\\"/root/runs/structfuse-context/m2_full_starcoder.log\\\", \\\"data_path\\\": \\\"/root/autodl-tmp/structfuse/full_m2_training_data/\\\", \\\"data_count\\\": 11308, \\\"model_name\\\": \\\"StarCoder2-3B\\\", \\\"seed\\\": \\\"42,43,44\\\"}, \\\"parent\\\": \\\"m2_full_starcoder\\\", \\\"metrics\\\": {\\\"checked_at\\\": \\\"2026-05-15T05:15Z\\\", \\\"process\\\": \\\"alive (PID 519791, uptime 03:11:44)\\\", \\\"gpu\\\": \\\"cuda:1, 100% util, 53.9/97.9GB VRAM, 72°C\\\", \\\"current_subrun\\\": \\\"random_s43 (1/9)\\\", \\\"current_step\\\": \\\"550/1405 (epoch 1/2, ~20% of subrun)\\\", \\\"eval_at_500\\\": {\\\"R@1\\\": 0.4708, \\\"R@5\\\": 0.9469, \\\"val_loss\\\": 0.5279}, \\\"latest_loss\\\": 0.26, \\\"completed_subruns\\\": 0, \\\"remaining_subruns\\\": 8, \\\"eta_hours\\\": \\\"~65-70h\\\"}}, \\\"m2_full_qwen_continued\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-14T18:44:20.646Z\\\", \\\"updated_at\\\": \\\"2026-05-14T21:18:42.976Z\\\", \\\"hypothesis\\\": \\\"M2 Qwen continued: 继续 m2_full_qwen 的剩余 runs (random_s44 + embedding×3 + dataflow×3)。原实验 cron 在 s42 退出时自动设为 ANALYZING，但链仍在运行。\\\", \\\"spec\\\": {\\\"command\\\": \\\"bash run_m2_full_qwen.sh (chain: random_s44 running → embedding×3 → dataflow×3)\\\", \\\"server\\\": \\\"bjb1-42106\\\", \\\"gpu\\\": [\\\"cuda:0\\\"], \\\"pid\\\": \\\"337267\\\", \\\"log_path\\\": \\\"/root/runs/structfuse-context/m2_full_qwen.log\\\", \\\"data_path\\\": \\\"/root/autodl-tmp/structfuse/full_m2_training_data/\\\", \\\"data_count\\\": 11308, \\\"model_name\\\": \\\"Qwen2.5-Coder-3B\\\", \\\"seed\\\": \\\"42,43,44\\\"}, \\\"parent\\\": \\\"m2_full_qwen\\\", \\\"metrics\\\": {\\\"checked_at\\\": \\\"2026-05-15T05:15Z\\\", \\\"process\\\": \\\"alive (PID 337267, uptime 09:50:41)\\\", \\\"gpu\\\": \\\"cuda:0, 100% util, 51.5/97.9GB VRAM, 68°C\\\", \\\"current_subrun\\\": \\\"random_s44 (3/7)\\\", \\\"current_step\\\": \\\"850/1408 (epoch 1/2, ~30% of subrun)\\\", \\\"eval_at_500\\\": {\\\"R@1\\\": 0.6009, \\\"R@5\\\": 0.9583, \\\"val_loss\\\": 0.4252}, \\\"latest_loss\\\": 0.2837, \\\"completed_subruns\\\": {\\\"random_s42\\\": {\\\"best_R@1\\\": 0.5527, \\\"best_val_loss\\\": 0.4651}, \\\"random_s43\\\": {\\\"best_R@1\\\": 0.5554, \\\"best_val_loss\\\": 0.4476}}, \\\"remaining_subruns\\\": 5, \\\"eta_hours\\\": \\\"~40-45h\\\"}}, \\\"plan_005_stratified\\\": {\\\"status\\\": \\\"PREPARING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-14T20:36:16.738Z\\\", \\\"updated_at\\\": \\\"2026-05-14T21:07:45.324Z\\\", \\\"hypothesis\\\": \\\"Plan 005 分层分析：按 repo size/pool size/query-pos similarity/structural data availability/neg_difficulty quartile 5 维度分层评估 embedding vs random 策略差异，控制 pool_size confound。Claim 2 支撑实验。v2 结果为 ground truth（v1→v2 changelog 见 art_20260514_3008c4）。\\\", \\\"parent\\\": \\\"m2_full_qwen\\\", \\\"notes\\\": \\\"plan_id=plan_005. 分层评估脚本已完成全部修改（analyze_stratified.py）：(1) mock seed 确定性修复 (2) pool_size-controlled 策略对比（within-bin delta + weighted aggregate）(3) dataflow×pool_size 交叉分析（n<30 标记 underpowered）(4) checkpoint 发现逻辑已就绪（best_by_recall_at_1 / best / best_by_val_loss）。输出含 JSON + CSV + PDF。[2026-05-14 21:07] Worker 完成 5 项 Patch：(P1) reeval_checkpoint 重写为 batch encoding（query/positive/negatives 分组批量编码，tqdm 进度条，torch.no_grad + model.eval，pad_token 兜底）(P2) 新增 --batch-size 参数（默认 64）(P3) 调用处传递 batch_size (P4) 非 dry-run 自适应 sim bins（tercile 计算边界 + 重新分配 sim_bin）(P5) 输出 JSON 记录 similarity_bin_edges 和 batch_size。Dry-run 验证全部通过。真实评估待 M2 全部 checkpoint 就绪后执行。\\\", \\\"metrics\\\": {\\\"confound_analysis\\\": {\\\"data_validity\\\": \\\"⚠️ R@1 值为 dry-run mock predictions，不可引用。仅分布结构（cross_tabulation.csv）有效。\\\", \\\"valid_findings\\\": {\\\"distribution_structure\\\": \\\"rich-dataflow 99.3% 落在 large/xlarge repo，small repo 中完全不存在\\\", \\\"correlation\\\": {\\\"dataflow_edges_vs_repo_size_pearson_r\\\": 0.089}, \\\"cross_distribution\\\": {\\\"rich_in_large_xlarge_pct\\\": 99.3, \\\"rich_in_small\\\": 0, \\\"moderate_in_large_xlarge_pct\\\": 60.9}, \\\"implication\\\": \\\"真实评估必须控制 pool_size 和 repo_size 来隔离 dataflow richness 独立效应\\\"}, \\\"invalid_findings\\\": \\\"所有 R@1/R@5/MRR 值均为 mock predictions，策略排序 pattern 不可信，禁止引用\\\", \\\"artifacts_path\\\": \\\"/root/autodl-tmp/structfuse/artifacts/confound_analysis/\\\", \\\"valid_artifact\\\": \\\"cross_tabulation.csv\\\"}}}, \\\"plan_017_literature\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-14T18:49:00.477Z\\\", \\\"updated_at\\\": \\\"2026-05-14T18:49:39.557Z\\\", \\\"hypothesis\\\": \\\"Inference-time graph method comparison: 8 papers surveyed (CodexGraph, LocAgent, RANGER, GraphCoder, ARISE, RepoGraph, CodeGRAG, CodeRAG). Discussion v2 drafted, all citations verified. Conclusion: training-time vs inference-time complementary.\\\", \\\"spec\\\": {\\\"command\\\": \\\"analysis only (no training)\\\", \\\"server\\\": \\\"local\\\", \\\"data_path\\\": \\\"N/A\\\", \\\"data_count\\\": 0, \\\"model_name\\\": \\\"N/A\\\", \\\"seed\\\": \\\"N/A\\\", \\\"checkpoint_path\\\": \\\"N/A\\\", \\\"log_path\\\": \\\"N/A\\\"}, \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"papers_surveyed\\\": 8, \\\"citations_verified\\\": 8, \\\"discussion_draft\\\": \\\"artifacts/paper_drafts/discussion_v2.md\\\", \\\"artifact_id\\\": \\\"art_20260514_a2e1cd\\\"}, \\\"completed_at\\\": \\\"2026-05-14T18:49:39.557Z\\\"}, \\\"m2_full_starcoder\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-13T16:18:15.415Z\\\", \\\"updated_at\\\": \\\"2026-05-14T18:04:29.245Z\\\", \\\"hypothesis\\\": \\\"Full M2 StarCoder: 3 strategies × 3 seeds on full M1 data. Cross-encoder validation — if embedding > random holds for both Qwen and StarCoder, method is encoder-agnostic. Resolves plan_013 pilot negative (dataflow encoder-dependent).\\\", \\\"parent\\\": \\\"plan_013_starcoder\\\", \\\"spec\\\": {\\\"command\\\": \\\"bash -c \\\\\\\"cd /root/structfuse && bash run_m2_full_starcoder_resume.sh\\\\\\\"\\\", \\\"server\\\": \\\"bjb1-42106\\\", \\\"gpu\\\": [\\\"cuda:1\\\"], \\\"pid\\\": \\\"519791\\\", \\\"log_path\\\": \\\"~/runs/structfuse-context/m2_full_starcoder.log\\\", \\\"submitted_at\\\": \\\"2026-05-14T18:03:12.079Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\"}, \\\"notes\\\": \\\"Phase 1: 构建 StarCoder embedding negatives 完成。Phase 2: 9 runs 训练中。batch_size=8, num_negatives=7, epochs=3(s42)/2(s43+), lr=2e-5, eval_steps=500, no early_stopping。双 checkpoint: best + best_by_recall_at_1。Seeds: 42,43,44。[D026] s42 保持 3 epochs; s43/s44 及后续 runs 改为 2 epochs。[2026-05-15 02:02 CST] cuda:1 进程冲突修复并重新提交（PID 519791, timeout=144h）。Registry 状态 DONE(failed) 是旧 cron timeout 标记，实际正在运行 random_s43 [1/8]。新 cron 已注册监控 PID 519791。序列：random_s43→s44→(待插入bm25_s42)→embedding×3→dataflow×3。random_s42 结果：best R@1=0.4604 at step 2500, val_loss=0.6134 at step 1000。\\\", \\\"metrics\\\": {\\\"random_s42\\\": {\\\"epoch\\\": \\\"3/3\\\", \\\"current_step\\\": 4200, \\\"total_steps\\\": 4242, \\\"total_steps_per_epoch\\\": 1414, \\\"eval_500\\\": {\\\"val_loss\\\": 0.6194, \\\"recall_at_1\\\": 0.435, \\\"recall_at_5\\\": 0.905, \\\"recall_at_10\\\": 1}, \\\"eval_1000\\\": {\\\"val_loss\\\": 0.6134, \\\"recall_at_1\\\": 0.454, \\\"recall_at_5\\\": 0.92, \\\"recall_at_10\\\": 1}, \\\"eval_1500\\\": {\\\"val_loss\\\": 0.6528, \\\"recall_at_1\\\": 0.449, \\\"recall_at_5\\\": 0.906, \\\"recall_at_10\\\": 1}, \\\"eval_2000\\\": {\\\"val_loss\\\": 0.6698, \\\"recall_at_1\\\": 0.4456, \\\"recall_at_5\\\": 0.906, \\\"recall_at_10\\\": 1}, \\\"eval_2500\\\": {\\\"val_loss\\\": 0.6342, \\\"recall_at_1\\\": 0.4604, \\\"recall_at_5\\\": 0.9117, \\\"recall_at_10\\\": 1}, \\\"eval_3000\\\": {\\\"val_loss\\\": 0.6516, \\\"recall_at_1\\\": 0.4544, \\\"recall_at_5\\\": 0.9077, \\\"recall_at_10\\\": 1}, \\\"eval_3500\\\": {\\\"val_loss\\\": 0.6588, \\\"recall_at_1\\\": 0.4534, \\\"recall_at_5\\\": 0.9057, \\\"recall_at_10\\\": 1}, \\\"eval_4000\\\": {\\\"val_loss\\\": 0.6637, \\\"recall_at_1\\\": 0.4547, \\\"recall_at_5\\\": 0.9003, \\\"recall_at_10\\\": 1}, \\\"best_checkpoint\\\": \\\"step_1000 (val_loss=0.6134) / step_2500 (R@1=0.4604)\\\", \\\"conclusion\\\": \\\"effectively_complete (timeout at step 4200/4242, lr=7.8e-9, remaining 42 steps negligible)\\\"}, \\\"progress_snapshot\\\": \\\"2026-05-15T01:50 CST\\\"}, \\\"reproduce\\\": {\\\"finished_at\\\": \\\"2026-05-14T17:49:54.474Z\\\"}, \\\"failure_reason\\\": \\\"EXIT_CODE=124 (timeout — exceeded timeout_hours)\\\", \\\"conclusion\\\": \\\"failed\\\", \\\"completed_at\\\": \\\"2026-05-14T17:49:55.304Z\\\", \\\"extra\\\": {\\\"hook_events\\\": [{\\\"event\\\": \\\"on_failed\\\", \\\"action\\\": \\\"agent\\\", \\\"ts\\\": \\\"2026-05-14T17:49:56.408767+00:00\\\"}]}}, \\\"m2_full_qwen\\\": {\\\"status\\\": \\\"ANALYZING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-13T16:18:14.870Z\\\", \\\"updated_at\\\": \\\"2026-05-14T18:00:29.323Z\\\", \\\"hypothesis\\\": \\\"Full M2 Qwen: 3 strategies (random/embedding/dataflow) × 3 seeds on full M1 data (~11K train/seed). Statistical validation of pilot signal (embedding > random +2pp). Go/no-go for paper claims per D018.\\\", \\\"parent\\\": \\\"m2_embed_verify\\\", \\\"spec\\\": {\\\"command\\\": \\\"bash -c \\\\\\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/structfuse && bash run_m2_full_qwen.sh 2>&1 | tee /root/runs/structfuse-context/m2_full_qwen.log\\\\\\\"\\\", \\\"server\\\": \\\"bjb1-42106\\\", \\\"gpu\\\": [\\\"cuda:0\\\"], \\\"pid\\\": \\\"73544\\\", \\\"log_path\\\": \\\"~/runs/structfuse-context/m2_full_qwen.log\\\", \\\"submitted_at\\\": \\\"2026-05-13T17:39:30.757Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\"}, \\\"notes\\\": \\\"Full M2 go/no-go: 3 strategies (random, embedding_distance, dataflow_aware) × 3 seeds (42, 43, 44) = 9 runs sequential on cuda:0. Config: lr=2e-5, batch_size=8, eval_steps=500, num_negatives=7, max_seq_length=2048, warmup_ratio=0.1, weight_decay=0.01, temperature=0.07, LoRA r=16, gradient_checkpointing=True, proj_dim=256. Dual checkpoint: best_by_val_loss + best_by_recall_at_1. Train ~11.3K/seed, val ~3K/seed. [D026] s42 保持 3 epochs 提供完整 overfitting curve; s43/s44 及后续 runs 改为 2 epochs + early_stopping_patience=2。[STATUS 2026-05-15 00:19 CST] Registry 状态 ANALYZING 是 cron 自动设置（s42 进程退出触发），但实验实际仍在进行中。random_s43 在 cuda:0 正常运行，step 1200/2810 (43%)。eval@500 R@1=0.5357, eval@1000 R@1=0.5285 (early_stopping 1/2)。Best R@1=0.5357 at step 500。GPU 100% 利用率, 50.5/97.9GB VRAM。\\\", \\\"metrics\\\": {\\\"random_s42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"epoch\\\": \\\"3/3\\\", \\\"total_steps\\\": 4242, \\\"total_steps_per_epoch\\\": 1414, \\\"eval_500\\\": {\\\"val_loss\\\": 0.4869, \\\"recall_at_1\\\": 0.533, \\\"recall_at_5\\\": 0.954, \\\"recall_at_10\\\": 1}, \\\"eval_1000\\\": {\\\"val_loss\\\": 0.4651, \\\"recall_at_1\\\": 0.553, \\\"recall_at_5\\\": 0.959, \\\"recall_at_10\\\": 1}, \\\"eval_1500\\\": {\\\"val_loss\\\": 0.5365, \\\"recall_at_1\\\": 0.523, \\\"recall_at_5\\\": 0.955, \\\"recall_at_10\\\": 1}, \\\"eval_2000\\\": {\\\"val_loss\\\": 0.5162, \\\"recall_at_1\\\": 0.523, \\\"recall_at_5\\\": 0.954, \\\"recall_at_10\\\": 1}, \\\"eval_2500\\\": {\\\"val_loss\\\": 0.5264, \\\"recall_at_1\\\": 0.527, \\\"recall_at_5\\\": 0.956, \\\"recall_at_10\\\": 1}, \\\"eval_3000\\\": {\\\"val_loss\\\": 0.5406, \\\"recall_at_1\\\": 0.536, \\\"recall_at_5\\\": 0.956, \\\"recall_at_10\\\": 1}, \\\"best_checkpoint\\\": \\\"step_1000 (val_loss=0.4651, R@1=0.5527)\\\", \\\"conclusion\\\": \\\"Overfit after step 1000. Best R@1=0.5527, +1.7pp vs pilot (0.5357). Full data helps.\\\"}, \\\"random_s43\\\": {\\\"status\\\": \\\"DONE\\\", \\\"epoch\\\": \\\"early_stopped\\\", \\\"total_steps_per_epoch\\\": 1405, \\\"eval_500\\\": {\\\"val_loss\\\": 0.4476, \\\"recall_at_1\\\": 0.5357}, \\\"eval_1000\\\": {\\\"val_loss\\\": 0.4637, \\\"recall_at_1\\\": 0.5285}, \\\"eval_1500\\\": {\\\"recall_at_1\\\": 0.5554}, \\\"best_by_val_loss\\\": \\\"step 500 (val_loss=0.4476)\\\", \\\"best_by_recall_at_1\\\": \\\"step 1500 (R@1=0.5554)\\\", \\\"conclusion\\\": \\\"Early stopped at step 1500. Best R@1=0.5554, consistent with s42 (0.5527). val_loss and R@1 criterion diverge.\\\"}, \\\"random_s44\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"note\\\": \\\"Auto-started 01:58 CST, epoch 1/2, 1408 batches/epoch\\\"}, \\\"progress_snapshot\\\": \\\"2026-05-15T02:00 CST\\\"}, \\\"reproduce\\\": {\\\"finished_at\\\": \\\"2026-05-14T11:24:33.887Z\\\"}, \\\"extra\\\": {\\\"hook_events\\\": [{\\\"event\\\": \\\"on_complete\\\", \\\"action\\\": \\\"agent\\\", \\\"ts\\\": \\\"2026-05-14T11:24:35.375104+00:00\\\"}]}}, \\\"plan_018_bm25\\\": {\\\"status\\\": \\\"QUEUED\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-14T16:38:40.603Z\\\", \\\"updated_at\\\": \\\"2026-05-14T17:09:50.985Z\\\", \\\"hypothesis\\\": \\\"BM25 negative baseline: Dream 审稿三档一致认定缺 BM25 baseline 是论文最大结构性缺陷。Phase 1 (CPU): 对 M2 训练语料建 BM25 索引，挖掘 BM25 hard negatives，生成训练数据。Phase 2 (GPU): 用 BM25 negatives 训练 Qwen + StarCoder 各 1 seed，对比 R@1。\\\", \\\"parent\\\": \\\"m2_full_qwen\\\", \\\"notes\\\": \\\"Phase 1 (CPU) COMPLETE: BM25 negative mining 完成。3 seeds 数据生成，record counts 与其他策略完全一致，0 fallback。BM25 score 分布: mean=246.50, std=155.96。重叠率: BM25 vs embedding_distance ~87.1%, vs random ~76.2%, vs dataflow_aware ~71.8%。高 median=1.0 因小 repo 候选池≤50 文件导致策略完全重合，BM25 differentiation 主要在大 repo。脚本: /root/structfuse/scripts/mine_bm25_negatives.py。输出: /root/autodl-tmp/structfuse/full_m2_training_data/{train,val}_bm25_s{42,43,44}.jsonl。Phase 2 (GPU): 等 re-dream gate 通过 + M2 完成后训练。\\\", \\\"metrics\\\": {\\\"phase1_complete\\\": true, \\\"seed_42\\\": {\\\"train_records\\\": 11308, \\\"val_records\\\": 2980, \\\"train_size_mb\\\": 1280.8, \\\"val_size_mb\\\": 344.6}, \\\"seed_43\\\": {\\\"train_records\\\": 11236, \\\"val_records\\\": 3052, \\\"train_size_mb\\\": 1280.9, \\\"val_size_mb\\\": 316}, \\\"seed_44\\\": {\\\"train_records\\\": 11264, \\\"val_records\\\": 3024, \\\"train_size_mb\\\": 1347.1, \\\"val_size_mb\\\": 295.9}, \\\"bm25_score_dist\\\": {\\\"count\\\": 392954, \\\"mean\\\": 246.5, \\\"std\\\": 155.96, \\\"p25\\\": 128.38, \\\"p50\\\": 228.41, \\\"p75\\\": 347.85, \\\"max\\\": 2585.74}, \\\"overlap_overall\\\": {\\\"bm25_vs_embedding\\\": 0.871, \\\"bm25_vs_random\\\": 0.762, \\\"bm25_vs_dataflow\\\": 0.718, \\\"note\\\": \\\"k=50 full candidate overlap from mining worker\\\"}, \\\"overlap_stratified_top7_jaccard\\\": {\\\"small_lt50\\\": {\\\"repos\\\": 39, \\\"bm25_vs_embedding\\\": 0.668, \\\"bm25_vs_random\\\": 0.411, \\\"bm25_vs_dataflow\\\": 0.667}, \\\"medium_50_200\\\": {\\\"repos\\\": 29, \\\"bm25_vs_embedding\\\": 0.38, \\\"bm25_vs_random\\\": 0.067, \\\"bm25_vs_dataflow\\\": 0.363}, \\\"large_200plus\\\": {\\\"repos\\\": 15, \\\"bm25_vs_embedding\\\": 0.297, \\\"bm25_vs_random\\\": 0.007, \\\"bm25_vs_dataflow\\\": 0.405}, \\\"matched_queries\\\": 2920, \\\"total_queries\\\": 12290, \\\"note\\\": \\\"top-7 Jaccard on s42 matched queries only (24% match rate due to different train/val splits)\\\"}}}, \\\"plan_015_dynamic\\\": {\\\"status\\\": \\\"QUEUED\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-14T17:03:24.316Z\\\", \\\"updated_at\\\": \\\"2026-05-14T17:03:30.544Z\\\", \\\"hypothesis\\\": \\\"Dynamic negative mining (epoch-level re-mining): 每 epoch 重新用当前 encoder embedding 挖掘 negatives，验证 static mining 是否足够。缩减版：只跑 dynamic_ep × 1 seed (Qwen, s42)，~11h 单卡。若 dynamic ≈ static（预期 <1pp 差异），在 Limitation 段排除 confound。\\\", \\\"notes\\\": \\\"Director D031 缩减：原 44h → 11h 单卡。只跑 dynamic_ep × 1 seed (Qwen, s42)，跳过 dynamic_500。Post-M2 与 plan_003 并行（一卡 SWE-bench，一卡 dynamic_ep）。受 re-dream gate 约束。设计文档已由 Worker 完成。\\\"}, \\\"neg_difficulty_analysis\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-13T19:39:20.016Z\\\", \\\"updated_at\\\": \\\"2026-05-14T00:13:49.046Z\\\", \\\"hypothesis\\\": \\\"Negative difficulty distribution analysis: 用预训练 Qwen2.5-Coder-3B 和 StarCoder2-3B 计算 3 策略 (random/embedding/dataflow) 的 query-negative/positive cosine similarity，分析 pretrained representation separability 跨编码器差异。MAX_LENGTH=2048 匹配训练设置。\\\", \\\"notes\\\": \\\"128 vs 2048 token 对比完成（2026-05-14 05:54 CST）。Qwen pos_sim 在 2048t 下 0.9855（比 128t 的 0.9804 更高），确认 ceiling 为 Qwen 表征的结构性特征，非截断 artifact。StarCoder margin 2.6-4.1x Qwen（2048t）。核心结论：pretrained representation separability varies across encoders，跨两种 token 长度成立。数据源：128t → stats_v2.json，2048t → stats_v3_2048.json。\\\", \\\"metrics\\\": {\\\"qwen_128\\\": {\\\"random\\\": {\\\"pos_sim\\\": 0.9804, \\\"neg_sim\\\": 0.899, \\\"margin\\\": 0.0816, \\\"pct_positive_margin\\\": 77.8}, \\\"embedding_distance\\\": {\\\"pos_sim\\\": 0.9804, \\\"neg_sim\\\": 0.959, \\\"margin\\\": 0.0209, \\\"pct_positive_margin\\\": 60.7}, \\\"dataflow_aware\\\": {\\\"pos_sim\\\": 0.9805, \\\"neg_sim\\\": 0.95, \\\"margin\\\": 0.0309, \\\"pct_positive_margin\\\": 67.4}}, \\\"starcoder_128\\\": {\\\"random\\\": {\\\"pos_sim\\\": 0.757, \\\"neg_sim\\\": 0.553, \\\"margin\\\": 0.2039, \\\"pct_positive_margin\\\": 72.8}, \\\"embedding_distance\\\": {\\\"pos_sim\\\": 0.784, \\\"neg_sim\\\": 0.668, \\\"margin\\\": 0.1159, \\\"pct_positive_margin\\\": 59.2}, \\\"dataflow_aware\\\": {\\\"pos_sim\\\": 0.761, \\\"neg_sim\\\": 0.659, \\\"margin\\\": 0.1022, \\\"pct_positive_margin\\\": 62.8}}, \\\"qwen_2048\\\": {\\\"random\\\": {\\\"pos_sim\\\": 0.9855, \\\"neg_sim\\\": 0.9111, \\\"margin\\\": 0.0743, \\\"margin_std\\\": 0.2322, \\\"pct_positive_margin\\\": 81.8}, \\\"embedding_distance\\\": {\\\"pos_sim\\\": 0.9855, \\\"neg_sim\\\": 0.9685, \\\"margin\\\": 0.017, \\\"margin_std\\\": 0.114, \\\"pct_positive_margin\\\": 58.8}, \\\"dataflow_aware\\\": {\\\"pos_sim\\\": 0.9856, \\\"neg_sim\\\": 0.9563, \\\"margin\\\": 0.0293, \\\"margin_std\\\": 0.1407, \\\"pct_positive_margin\\\": 73.9}}, \\\"starcoder_2048\\\": {\\\"random\\\": {\\\"pos_sim\\\": 0.7985, \\\"neg_sim\\\": 0.6045, \\\"margin\\\": 0.194, \\\"margin_std\\\": 0.2788, \\\"pct_positive_margin\\\": 78}, \\\"embedding_distance\\\": {\\\"pos_sim\\\": 0.8079, \\\"neg_sim\\\": 0.7409, \\\"margin\\\": 0.067, \\\"margin_std\\\": 0.2056, \\\"pct_positive_margin\\\": 55}, \\\"dataflow_aware\\\": {\\\"pos_sim\\\": 0.8009, \\\"neg_sim\\\": 0.6818, \\\"margin\\\": 0.1192, \\\"margin_std\\\": 0.2264, \\\"pct_positive_margin\\\": 70.4}}, \\\"sc_qwen_margin_ratio_128\\\": {\\\"random\\\": 2.5, \\\"embedding_distance\\\": 5.54, \\\"dataflow_aware\\\": 3.3}, \\\"sc_qwen_margin_ratio_2048\\\": {\\\"random\\\": 2.61, \\\"embedding_distance\\\": 3.94, \\\"dataflow_aware\\\": 4.07}}, \\\"conclusion\\\": \\\"success\\\", \\\"spec\\\": {\\\"command\\\": \\\"python negative_difficulty_margin_v2.py (CPU analysis)\\\", \\\"server\\\": \\\"bjb1-42106\\\", \\\"data_path\\\": \\\"/root/autodl-tmp/structfuse/full_m2_data/\\\", \\\"data_count\\\": 11000, \\\"model_name\\\": \\\"Qwen2.5-Coder-3B + StarCoder2-3B (pretrained, no training)\\\", \\\"seed\\\": \\\"N/A\\\", \\\"checkpoint_path\\\": \\\"N/A (analysis only)\\\", \\\"log_path\\\": \\\"/root/autodl-tmp/structfuse/artifacts/negative_difficulty_stats_v3_2048.json\\\"}, \\\"completed_at\\\": \\\"2026-05-14T00:13:49.046Z\\\"}, \\\"m1_reextract\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-13T19:35:23.954Z\\\", \\\"updated_at\\\": \\\"2026-05-13T19:45:53.741Z\\\", \\\"hypothesis\\\": \\\"M1 重提取：恢复 28,276 个因运行时瞬态文件系统故障失败的 instances（82 repos）。预期将训练数据从 15,897 提升至 ~44,173。D022 批准。\\\", \\\"parent\\\": \\\"m1_extraction\\\", \\\"spec\\\": {\\\"command\\\": \\\"bash scripts/rerun_m1_failed.sh (4 CPU workers, CodeQL 2-hop)\\\", \\\"server\\\": \\\"bjb1-42106\\\", \\\"data_path\\\": \\\"/root/autodl-tmp/structfuse/m1_extraction/\\\", \\\"data_count\\\": 28276, \\\"model_name\\\": \\\"N/A (CodeQL extraction)\\\", \\\"seed\\\": \\\"N/A\\\", \\\"pid\\\": \\\"97358\\\", \\\"log_path\\\": \\\"/root/runs/structfuse-context/m1_rerun.log\\\", \\\"checkpoint_source\\\": \\\"rerun of m1_extraction failed instances\\\", \\\"eval_data\\\": \\\"N/A\\\", \\\"checkpoint_path\\\": \\\"N/A (failed, no output)\\\"}, \\\"conclusion\\\": \\\"failed\\\", \\\"notes\\\": \\\"CodeQL query 100% 失败（exit status 2）。根因：Worker 安装 CodeQL CLI 2.25.4 时未执行 `codeql pack install`，`codeql/python-all@7.1.0` 标准库 pack 缺失。修复命令：`cd /root/structfuse/extraction/codeql_queries && /opt/codeql/codeql pack install`。已 kill 进程 + tmux session。无新数据产出（all.jsonl 未受影响）。等 Director 确认后修复重跑。\\\", \\\"completed_at\\\": \\\"2026-05-13T19:44:09.115Z\\\"}, \\\"m1_extraction\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-12T21:00:02.300Z\\\", \\\"updated_at\\\": \\\"2026-05-13T19:26:13.901Z\\\", \\\"spec\\\": {\\\"command\\\": \\\"nohup bash scripts/run_m1_extraction.sh (8 CPU workers, CodeQL 2-hop)\\\", \\\"server\\\": \\\"cqa1-21977\\\", \\\"data_path\\\": \\\"/root/autodl-tmp/structfuse/m1_extraction/\\\", \\\"data_count\\\": 50869, \\\"model_name\\\": \\\"N/A (CodeQL extraction)\\\", \\\"seed\\\": \\\"N/A\\\", \\\"description\\\": \\\"M1: 全量 5K repos CodeQL 提取, 131 unique (repo,commit) groups, 50869 instances\\\"}, \\\"metrics\\\": {\\\"total_instances_attempted\\\": 44173, \\\"instances_skipped\\\": 6696, \\\"total_instances\\\": 50869, \\\"codeql_success\\\": 15133, \\\"beniget_fallback\\\": 764, \\\"extraction_failed\\\": 28276, \\\"structural_data_rate\\\": 0.36, \\\"repos_with_output\\\": 123, \\\"repos_total\\\": 131, \\\"repo_coverage\\\": 0.939, \\\"skip_clone_failed\\\": 5852, \\\"skip_checkout_failed\\\": 836, \\\"skip_stale_handle\\\": 8, \\\"elapsed_minutes\\\": 837.8, \\\"avg_time_per_instance_s\\\": 8.9, \\\"output_size_gb\\\": 6.6, \\\"disk_usage_gb\\\": 13, \\\"output_file\\\": \\\"all.jsonl\\\"}, \\\"notes\\\": \\\"[2026-05-13 19:25] COMPLETED. 837.8min, 123/131 repos (93.9%), 15,897/44,173 instances with structural data (36.0%), 6,696 skipped (clone/checkout). Output: all.jsonl 6.6GB. [2026-05-13 19:23 UPDATE] 28,276 buggy_file_not_found errors 经验证并非上游数据质量问题——10/10 抽查的文件在 repo 中全部存在。根因是运行时瞬态文件系统故障（CodeQL 并行 database creation 导致磁盘耗尽，锐截止模式）。这些 instances 可通过重跑恢复。D022: 准备重跑脚本中，等 Director 确认后执行。\\\", \\\"conclusion\\\": \\\"success\\\", \\\"checkpoint_path\\\": \\\"/root/autodl-tmp/structfuse/m1_extraction/all.jsonl\\\", \\\"log_path\\\": \\\"/tmp/m1_extraction.log\\\", \\\"completed_at\\\": \\\"2026-05-13T10:59:42.462Z\\\"}, \\\"plan_006_scalability\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-13T07:57:43.631Z\\\", \\\"updated_at\\\": \\\"2026-05-13T19:24:00.741Z\\\", \\\"spec\\\": {\\\"command\\\": \\\"M1 scalability statistics analysis (29/131 repos)\\\", \\\"server\\\": \\\"bjb1-42106\\\", \\\"data_path\\\": \\\"/root/autodl-tmp/structfuse/m1_extraction/\\\", \\\"data_count\\\": 8171, \\\"model_name\\\": \\\"N/A (CPU analysis)\\\", \\\"seed\\\": \\\"N/A\\\", \\\"description\\\": \\\"Plan 006: M1 extraction scalability stats - timeout rate, extraction time, coverage, Z% by repo size. Partial results from 29/131 repos.\\\", \\\"checkpoint_path\\\": \\\"N/A\\\", \\\"log_path\\\": \\\"N/A\\\"}, \\\"conclusion\\\": \\\"success\\\", \\\"completed_at\\\": \\\"2026-05-13T07:57:58.176Z\\\", \\\"notes\\\": \\\"[2026-05-13 19:23] 全量统计 + error 分析 + fuzzy match 验证完成。关键发现: (1) 0 timeout; (2) 28,276 error 全部 buggy_file_not_found，但 fuzzy match 验证发现文件实际都存在——根因是运行时瞬态文件系统故障（锐截止模式：每个 repo 内先成功后突然全部失败，extraction_time=0.0s），可能是 CodeQL 并行数据库创建导致磁盘空间耗尽; (3) 这些 instance 可通过重跑恢复（当前 resolve_file_in_repo 对全部样本返回正确路径）; (4) 结构数据率 34.3% 有望提升至接近 100%（若重跑成功）; (5) Z% 随 repo 规模上升 (XL median 96%). Artifacts: plan006_full_scalability.json, art_20260513_d262da (error patterns)\\\", \\\"hypothesis\\\": \\\"Claim 3: CodeQL bounded data-flow extraction scales to large repos with acceptable timeout rates and provides meaningful structural coverage (Z%) that increases with repo complexity\\\", \\\"metrics\\\": {\\\"repos\\\": 123, \\\"total_instances\\\": 44173, \\\"structural_data_rate\\\": 0.343, \\\"error_rate\\\": 0.64, \\\"zero_timeout_rate\\\": true, \\\"processing_time\\\": {\\\"mean_s\\\": 8.93, \\\"median_s\\\": 0, \\\"p95_s\\\": 31.95, \\\"max_s\\\": 633.68, \\\"total_hours\\\": 109.58}, \\\"by_tier\\\": {\\\"small_lt50\\\": {\\\"repos\\\": 1, \\\"instances\\\": 500, \\\"error_rate\\\": 0.054, \\\"struct_rate\\\": 0.81, \\\"z_pct_mean\\\": 0.284, \\\"z_pct_median\\\": 0}, \\\"medium_50_200\\\": {\\\"repos\\\": 17, \\\"instances\\\": 4096, \\\"error_rate\\\": 0.485, \\\"struct_rate\\\": 0.472, \\\"z_pct_mean\\\": 0.444, \\\"z_pct_median\\\": 0.5}, \\\"large_200_500\\\": {\\\"repos\\\": 40, \\\"instances\\\": 13628, \\\"error_rate\\\": 0.639, \\\"struct_rate\\\": 0.343, \\\"z_pct_mean\\\": 0.604, \\\"z_pct_median\\\": 0.857}, \\\"xlarge_500plus\\\": {\\\"repos\\\": 29, \\\"instances\\\": 25949, \\\"error_rate\\\": 0.676, \\\"struct_rate\\\": 0.314, \\\"z_pct_mean\\\": 0.812, \\\"z_pct_median\\\": 0.96}}, \\\"instance_distribution\\\": {\\\"lt10\\\": 1, \\\"10_50\\\": 17, \\\"50_200\\\": 36, \\\"200_500\\\": 40, \\\"500plus\\\": 29}, \\\"artifact\\\": \\\"plan006_full_scalability.json\\\"}}, \\\"plan_013_starcoder\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-13T05:09:14.885Z\\\", \\\"updated_at\\\": \\\"2026-05-13T18:09:54.153Z\\\", \\\"hypothesis\\\": \\\"Architecture generalization: validate StructFuse with StarCoder2-3B encoder (vs Qwen2.5-Coder-3B in m2_embed_verify). If both encoders show same strategy ranking → method is encoder-agnostic, strengthening the core claim. Key differentiator for best→accept at Dream.\\\", \\\"spec\\\": {\\\"command\\\": \\\"bash -c \\\\\\\"bash /root/structfuse/run_plan013_starcoder.sh\\\\\\\"\\\", \\\"server\\\": \\\"bjb1-42106\\\", \\\"gpu\\\": [\\\"cuda:0\\\"], \\\"pid\\\": \\\"23798\\\", \\\"log_path\\\": \\\"~/runs/structfuse-context/plan_013_starcoder.log\\\", \\\"submitted_at\\\": \\\"2026-05-13T05:26:21.946Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\", \\\"data_path\\\": \\\"/root/autodl-tmp/structfuse/m2_embed_verify_data/\\\", \\\"data_count\\\": 3282, \\\"model_name\\\": \\\"bigcode/starcoder2-3b\\\", \\\"seed\\\": 42, \\\"wall_clock_seconds\\\": 35338.2, \\\"gpu_hours\\\": 9.82}, \\\"notes\\\": \\\"[2026-05-13 16:00] ALL 3 STRATEGIES DONE. Ranking: embedding (R@1=0.5078) > random (0.4922) > dataflow (0.4869). Embedding vs random: +1.6pp (consistent with Qwen). Dataflow vs random: -0.5pp (DIFFERS from Qwen where dataflow > random +0.8pp). Hypothesis NEGATIVE: strategy ranking NOT identical across encoders. Embedding > random is encoder-agnostic, dataflow position is encoder-dependent. Log: /root/runs/faith-evidence-ie/plan_013_starcoder.log. Cron misreported EXIT_CODE=129 but all strategies completed (confirmed via log extraction worker).\\\", \\\"metrics\\\": {\\\"random\\\": {\\\"status\\\": \\\"DONE\\\", \\\"best_val_loss\\\": 0.5113, \\\"best_recall@1\\\": 0.4922, \\\"best_recall@5\\\": 0.98, \\\"best_recall@10\\\": 1, \\\"source\\\": \\\"/tmp/eval_random_s42.log (post-hoc eval, no in-training eval)\\\"}, \\\"embedding_distance\\\": {\\\"status\\\": \\\"DONE\\\", \\\"best_step\\\": 1000, \\\"best_val_loss\\\": 0.4816, \\\"best_recall@1\\\": 0.5078, \\\"best_recall@5\\\": 0.9843, \\\"best_recall@10\\\": 1, \\\"final_val_loss\\\": 0.506, \\\"final_recall@1\\\": 0.5174}, \\\"dataflow_aware\\\": {\\\"status\\\": \\\"DONE\\\", \\\"best_step\\\": 1000, \\\"best_val_loss\\\": 0.5255, \\\"best_recall@1\\\": 0.4869, \\\"best_recall@5\\\": 0.9695, \\\"best_recall@10\\\": 1, \\\"final_val_loss\\\": 0.5509, \\\"final_recall@1\\\": 0.5078}}, \\\"failure_reason\\\": \\\"\\\", \\\"conclusion\\\": \\\"negative\\\", \\\"completed_at\\\": \\\"2026-05-13T15:15:20.165Z\\\"}, \\\"m2_embed_verify\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-13T04:39:16.051Z\\\", \\\"updated_at\\\": \\\"2026-05-13T15:59:51.621Z\\\", \\\"hypothesis\\\": \\\"True embedding mining verificat",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false,
    "persistedOutputPath": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-5-projects-structfuse-context/b1d97499-4652-4822-8fc5-dbdc566ceedc/tool-results/bv76ai3j3.txt",
    "persistedOutputSize": 56021
  },
  "sourceToolAssistantUUID": "908ec8f0-7e8b-4d75-ae1a-a0ce2a303737",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "b1d97499-4652-4822-8fc5-dbdc566ceedc",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 39_

```json
{
  "type": "last-prompt",
  "leafUuid": "52fd78e1-937c-40f4-b1dc-b96969ba45c9",
  "sessionId": "b1d97499-4652-4822-8fc5-dbdc566ceedc"
}
```

---

### Runtime record

_source line 40_

```json
{
  "type": "ai-title",
  "aiTitle": "Fix literature reference consistency issues",
  "sessionId": "b1d97499-4652-4822-8fc5-dbdc566ceedc"
}
```

---

### Tool call

_source line 41 · 2026-05-14T21:32:28.015Z_

<details open><summary>🔧 Tool call — Grep · `toolu_019qHuy2bfYJ4amsASNokJ1s`</summary>

```json
{
  "pattern": "plan_017_literature",
  "path": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-5-projects-structfuse-context/b1d97499-4652-4822-8fc5-dbdc566ceedc/tool-results/toolu_01KYorBUb5wJHZKTYaT5g6Gh.txt",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "52fd78e1-937c-40f4-b1dc-b96969ba45c9",
  "isSidechain": false,
  "requestId": "req_011Cb3BC2jQ5pHkTvCgrtUzQ",
  "type": "assistant",
  "uuid": "86dacd31-2f3a-4599-85e5-e2830f9e2466",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "b1d97499-4652-4822-8fc5-dbdc566ceedc",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014NjB1Sb7WuEhaDKFaNba1h",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1835,
      "cache_read_input_tokens": 39195,
      "output_tokens": 185,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1835,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 185,
          "cache_read_input_tokens": 39195,
          "cache_creation_input_tokens": 1835,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1835
          },
          "type": "message"
        }
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

_source line 42 · 2026-05-14T21:32:28.027Z_

<details><summary>↩ Tool result · `toolu_019qHuy2bfYJ4amsASNokJ1s`</summary>

```text
1:[Omitted long matching line]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "86dacd31-2f3a-4599-85e5-e2830f9e2466",
  "isSidechain": false,
  "promptId": "255fffc4-c17f-4b3b-8b5c-7a3031fdb918",
  "type": "user",
  "uuid": "f5850a2e-7915-498c-928b-cca4fd33a165",
  "toolUseResult": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "1:[Omitted long matching line]",
    "numLines": 1
  },
  "sourceToolAssistantUUID": "86dacd31-2f3a-4599-85e5-e2830f9e2466",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "b1d97499-4652-4822-8fc5-dbdc566ceedc",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 43 · 2026-05-14T21:32:31.797Z_

<details><summary>Logged reasoning block</summary>

```text
The output is too large. Let me try to read just the plan_017_literature entry from the registry directly.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f5850a2e-7915-498c-928b-cca4fd33a165",
  "isSidechain": false,
  "requestId": "req_011Cb3BCLjsHrZRFDU4naKKH",
  "type": "assistant",
  "uuid": "3e5c75f6-6cdc-4610-a131-40fa5c9162fb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "b1d97499-4652-4822-8fc5-dbdc566ceedc",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014EZRUDMdteeT1iUdP1AtfC",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 206,
      "cache_read_input_tokens": 41030,
      "output_tokens": 147,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 206,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 147,
          "cache_read_input_tokens": 41030,
          "cache_creation_input_tokens": 206,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 206
          },
          "type": "message"
        }
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

_source line 44 · 2026-05-14T21:32:32.183Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_01XuU8ezGgbbvJrHrkJqT5hH`</summary>

```json
{
  "project": "structfuse-context",
  "limit": 50,
  "fields": [
    "hypothesis",
    "notes",
    "status"
  ]
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3e5c75f6-6cdc-4610-a131-40fa5c9162fb",
  "isSidechain": false,
  "requestId": "req_011Cb3BCLjsHrZRFDU4naKKH",
  "type": "assistant",
  "uuid": "9ee2acb9-ddf8-4ced-9b60-8a1554c992bd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "b1d97499-4652-4822-8fc5-dbdc566ceedc",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014EZRUDMdteeT1iUdP1AtfC",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 206,
      "cache_read_input_tokens": 41030,
      "output_tokens": 147,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 206,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 147,
          "cache_read_input_tokens": 41030,
          "cache_creation_input_tokens": 206,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 206
          },
          "type": "message"
        }
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

_source line 45 · 2026-05-14T21:32:32.308Z_

<details><summary>↩ Tool result · `toolu_01XuU8ezGgbbvJrHrkJqT5hH`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"experiments\": {\"m1_reextract_v2\": {\"status\": \"RUNNING\", \"hypothesis\": \"M1 重提取 v2：恢复 28,276 个因运行时瞬态文件系统故障失败的 instances（82 repos）。CodeQL pack 已修复，端到端测试通过。预期将训练数据从 15,897 提升至 ~44,173。D022 批准。\", \"notes\": \"M1 重提取 v2：CodeQL pack 已修复，端到端测试通过。28,276 instances / 82 repo groups / 4 workers 并行。启动 2026-05-14 03:59 CST。[诊断 07:06 CST] 活跃运行中，~15/82 groups 完成，2,469 次 call_graph 查询成功，预计还需 ~13-16h。仅前 4 个旧 repo（furl/pyasn1/feedparser/python-docx）复用 v1 旧 DB 有 18 次降级 WARNING，04:02 之后零失败。产出写入 all.jsonl（追加模式）。磁盘 97GB 可用。[Director 决策 Session 8] 即使数据量增至 ~44K，不重跑 M2（ARR May 25 DDL 不允许再加 4-5 天重训）。处理方式：(1) post-M2 完成后如有 GPU 空档，跑 1-seed pilot (Qwen, embedding, 新数据) 对比当前 M2 baseline; (2) 论文中作为 scalability/data efficiency 讨论点; (3) 全量重训留 camera-ready。[进度检查 2026-05-15 05:05 CST] 80.8% 完成（22,842/28,276），0 ERROR，速率 ~560/hr，处理中大 repo：mozilla__bleach/sqlfluff/conan-io/Project-MONAI。产出为单独 .json 文件，尚未合并 all.jsonl。预计 ~15:00 CST May 15 完成。\"}, \"m2_full_starcoder_resumed\": {\"status\": \"RUNNING\", \"hypothesis\": \"M2 StarCoder resumed: 继续 m2_full_starcoder 的 8 sequential runs (random×2 + embedding×3 + dataflow×3)。原实验因 cron timeout 标记为 failed，实际 PID 519791 正常运行。\"}, \"m2_full_qwen_continued\": {\"status\": \"RUNNING\", \"hypothesis\": \"M2 Qwen continued: 继续 m2_full_qwen 的剩余 runs (random_s44 + embedding×3 + dataflow×3)。原实验 cron 在 s42 退出时自动设为 ANALYZING，但链仍在运行。\"}, \"plan_005_stratified\": {\"status\": \"PREPARING\", \"hypothesis\": \"Plan 005 分层分析：按 repo size/pool size/query-pos similarity/structural data availability/neg_difficulty quartile 5 维度分层评估 embedding vs random 策略差异，控制 pool_size confound。Claim 2 支撑实验。v2 结果为 ground truth（v1→v2 changelog 见 art_20260514_3008c4）。\", \"notes\": \"plan_id=plan_005. 分层评估脚本已完成全部修改（analyze_stratified.py）：(1) mock seed 确定性修复 (2) pool_size-controlled 策略对比（within-bin delta + weighted aggregate）(3) dataflow×pool_size 交叉分析（n<30 标记 underpowered）(4) checkpoint 发现逻辑已就绪（best_by_recall_at_1 / best / best_by_val_loss）。输出含 JSON + CSV + PDF。[2026-05-14 21:07] Worker 完成 5 项 Patch：(P1) reeval_checkpoint 重写为 batch encoding（query/positive/negatives 分组批量编码，tqdm 进度条，torch.no_grad + model.eval，pad_token 兜底）(P2) 新增 --batch-size 参数（默认 64）(P3) 调用处传递 batch_size (P4) 非 dry-run 自适应 sim bins（tercile 计算边界 + 重新分配 sim_bin）(P5) 输出 JSON 记录 similarity_bin_edges 和 batch_size。Dry-run 验证全部通过。真实评估待 M2 全部 checkpoint 就绪后执行。\"}, \"plan_017_literature\": {\"status\": \"DONE\", \"hypothesis\": \"Inference-time graph method comparison: 8 papers surveyed (CodexGraph, LocAgent, RANGER, GraphCoder, ARISE, RepoGraph, CodeGRAG, CodeRAG). Discussion v2 drafted, all citations verified. Conclusion: training-time vs inference-time complementary.\"}, \"m2_full_starcoder\": {\"status\": \"DONE\", \"hypothesis\": \"Full M2 StarCoder: 3 strategies × 3 seeds on full M1 data. Cross-encoder validation — if embedding > random holds for both Qwen and StarCoder, method is encoder-agnostic. Resolves plan_013 pilot negative (dataflow encoder-dependent).\", \"notes\": \"Phase 1: 构建 StarCoder embedding negatives 完成。Phase 2: 9 runs 训练中。batch_size=8, num_negatives=7, epochs=3(s42)/2(s43+), lr=2e-5, eval_steps=500, no early_stopping。双 checkpoint: best + best_by_recall_at_1。Seeds: 42,43,44。[D026] s42 保持 3 epochs; s43/s44 及后续 runs 改为 2 epochs。[2026-05-15 02:02 CST] cuda:1 进程冲突修复并重新提交（PID 519791, timeout=144h）。Registry 状态 DONE(failed) 是旧 cron timeout 标记，实际正在运行 random_s43 [1/8]。新 cron 已注册监控 PID 519791。序列：random_s43→s44→(待插入bm25_s42)→embedding×3→dataflow×3。random_s42 结果：best R@1=0.4604 at step 2500, val_loss=0.6134 at step 1000。\"}, \"m2_full_qwen\": {\"status\": \"ANALYZING\", \"hypothesis\": \"Full M2 Qwen: 3 strategies (random/embedding/dataflow) × 3 seeds on full M1 data (~11K train/seed). Statistical validation of pilot signal (embedding > random +2pp). Go/no-go for paper claims per D018.\", \"notes\": \"Full M2 go/no-go: 3 strategies (random, embedding_distance, dataflow_aware) × 3 seeds (42, 43, 44) = 9 runs sequential on cuda:0. Config: lr=2e-5, batch_size=8, eval_steps=500, num_negatives=7, max_seq_length=2048, warmup_ratio=0.1, weight_decay=0.01, temperature=0.07, LoRA r=16, gradient_checkpointing=True, proj_dim=256. Dual checkpoint: best_by_val_loss + best_by_recall_at_1. Train ~11.3K/seed, val ~3K/seed. [D026] s42 保持 3 epochs 提供完整 overfitting curve; s43/s44 及后续 runs 改为 2 epochs + early_stopping_patience=2。[STATUS 2026-05-15 00:19 CST] Registry 状态 ANALYZING 是 cron 自动设置（s42 进程退出触发），但实验实际仍在进行中。random_s43 在 cuda:0 正常运行，step 1200/2810 (43%)。eval@500 R@1=0.5357, eval@1000 R@1=0.5285 (early_stopping 1/2)。Best R@1=0.5357 at step 500。GPU 100% 利用率, 50.5/97.9GB VRAM。\"}, \"plan_018_bm25\": {\"status\": \"QUEUED\", \"hypothesis\": \"BM25 negative baseline: Dream 审稿三档一致认定缺 BM25 baseline 是论文最大结构性缺陷。Phase 1 (CPU): 对 M2 训练语料建 BM25 索引，挖掘 BM25 hard negatives，生成训练数据。Phase 2 (GPU): 用 BM25 negatives 训练 Qwen + StarCoder 各 1 seed，对比 R@1。\", \"notes\": \"Phase 1 (CPU) COMPLETE: BM25 negative mining 完成。3 seeds 数据生成，record counts 与其他策略完全一致，0 fallback。BM25 score 分布: mean=246.50, std=155.96。重叠率: BM25 vs embedding_distance ~87.1%, vs random ~76.2%, vs dataflow_aware ~71.8%。高 median=1.0 因小 repo 候选池≤50 文件导致策略完全重合，BM25 differentiation 主要在大 repo。脚本: /root/structfuse/scripts/mine_bm25_negatives.py。输出: /root/autodl-tmp/structfuse/full_m2_training_data/{train,val}_bm25_s{42,43,44}.jsonl。Phase 2 (GPU): 等 re-dream gate 通过 + M2 完成后训练。\"}, \"plan_015_dynamic\": {\"status\": \"QUEUED\", \"hypothesis\": \"Dynamic negative mining (epoch-level re-mining): 每 epoch 重新用当前 encoder embedding 挖掘 negatives，验证 static mining 是否足够。缩减版：只跑 dynamic_ep × 1 seed (Qwen, s42)，~11h 单卡。若 dynamic ≈ static（预期 <1pp 差异），在 Limitation 段排除 confound。\", \"notes\": \"Director D031 缩减：原 44h → 11h 单卡。只跑 dynamic_ep × 1 seed (Qwen, s42)，跳过 dynamic_500。Post-M2 与 plan_003 并行（一卡 SWE-bench，一卡 dynamic_ep）。受 re-dream gate 约束。设计文档已由 Worker 完成。\"}, \"neg_difficulty_analysis\": {\"status\": \"DONE\", \"hypothesis\": \"Negative difficulty distribution analysis: 用预训练 Qwen2.5-Coder-3B 和 StarCoder2-3B 计算 3 策略 (random/embedding/dataflow) 的 query-negative/positive cosine similarity，分析 pretrained representation separability 跨编码器差异。MAX_LENGTH=2048 匹配训练设置。\", \"notes\": \"128 vs 2048 token 对比完成（2026-05-14 05:54 CST）。Qwen pos_sim 在 2048t 下 0.9855（比 128t 的 0.9804 更高），确认 ceiling 为 Qwen 表征的结构性特征，非截断 artifact。StarCoder margin 2.6-4.1x Qwen（2048t）。核心结论：pretrained representation separability varies across encoders，跨两种 token 长度成立。数据源：128t → stats_v2.json，2048t → stats_v3_2048.json。\"}, \"m1_reextract\": {\"status\": \"DONE\", \"hypothesis\": \"M1 重提取：恢复 28,276 个因运行时瞬态文件系统故障失败的 instances（82 repos）。预期将训练数据从 15,897 提升至 ~44,173。D022 批准。\", \"notes\": \"CodeQL query 100% 失败（exit status 2）。根因：Worker 安装 CodeQL CLI 2.25.4 时未执行 `codeql pack install`，`codeql/python-all@7.1.0` 标准库 pack 缺失。修复命令：`cd /root/structfuse/extraction/codeql_queries && /opt/codeql/codeql pack install`。已 kill 进程 + tmux session。无新数据产出（all.jsonl 未受影响）。等 Director 确认后修复重跑。\"}, \"m1_extraction\": {\"status\": \"DONE\", \"notes\": \"[2026-05-13 19:25] COMPLETED. 837.8min, 123/131 repos (93.9%), 15,897/44,173 instances with structural data (36.0%), 6,696 skipped (clone/checkout). Output: all.jsonl 6.6GB. [2026-05-13 19:23 UPDATE] 28,276 buggy_file_not_found errors 经验证并非上游数据质量问题——10/10 抽查的文件在 repo 中全部存在。根因是运行时瞬态文件系统故障（CodeQL 并行 database creation 导致磁盘耗尽，锐截止模式）。这些 instances 可通过重跑恢复。D022: 准备重跑脚本中，等 Director 确认后执行。\"}, \"plan_006_scalability\": {\"status\": \"DONE\", \"notes\": \"[2026-05-13 19:23] 全量统计 + error 分析 + fuzzy match 验证完成。关键发现: (1) 0 timeout; (2) 28,276 error 全部 buggy_file_not_found，但 fuzzy match 验证发现文件实际都存在——根因是运行时瞬态文件系统故障（锐截止模式：每个 repo 内先成功后突然全部失败，extraction_time=0.0s），可能是 CodeQL 并行数据库创建导致磁盘空间耗尽; (3) 这些 instance 可通过重跑恢复（当前 resolve_file_in_repo 对全部样本返回正确路径）; (4) 结构数据率 34.3% 有望提升至接近 100%（若重跑成功）; (5) Z% 随 repo 规模上升 (XL median 96%). Artifacts: plan006_full_scalability.json, art_20260513_d262da (error patterns)\", \"hypothesis\": \"Claim 3: CodeQL bounded data-flow extraction scales to large repos with acceptable timeout rates and provides meaningful structural coverage (Z%) that increases with repo complexity\"}, \"plan_013_starcoder\": {\"status\": \"DONE\", \"hypothesis\": \"Architecture generalization: validate StructFuse with StarCoder2-3B encoder (vs Qwen2.5-Coder-3B in m2_embed_verify). If both encoders show same strategy ranking → method is encoder-agnostic, strengthening the core claim. Key differentiator for best→accept at Dream.\", \"notes\": \"[2026-05-13 16:00] ALL 3 STRATEGIES DONE. Ranking: embedding (R@1=0.5078) > random (0.4922) > dataflow (0.4869). Embedding vs random: +1.6pp (consistent with Qwen). Dataflow vs random: -0.5pp (DIFFERS from Qwen where dataflow > random +0.8pp). Hypothesis NEGATIVE: strategy ranking NOT identical across encoders. Embedding > random is encoder-agnostic, dataflow position is encoder-dependent. Log: /root/runs/faith-evidence-ie/plan_013_starcoder.log. Cron misreported EXIT_CODE=129 but all strategies completed (confirmed via log extraction worker).\"}, \"m2_embed_verify\": {\"status\": \"DONE\", \"hypothesis\": \"True embedding mining verification: compare Qwen2.5-Coder-3B cosine similarity negatives vs BM25 negatives on pilot data (24 repos). If true embedding negatives are harder → Claim 2 (structure-aware negatives improve retrieval) gets stronger evidence.\", \"notes\": \"[2026-05-13 16:00] ALL 3 STRATEGIES DONE. Ranking: embedding (R@1=0.5557) > dataflow (0.5436) > random (0.5357). Embedding vs random: +2.0pp. Dataflow vs random: +0.8pp. All best at step 500, overfitting after. Hypothesis confirmed: true embedding negatives are harder → Claim 2 supported. Log: /root/runs/faith-evidence-ie/m2_embed_verify.log. Cron misreported EXIT_CODE=2 but all strategies completed successfully (confirmed via log extraction worker).\"}, \"mvp_p2b_contrastive_v2\": {\"status\": \"DONE\", \"notes\": \"P2b 对比训练 v2，因磁盘空间不足被 kill。已被 p2b_5reruns（成功完成 9/9 runs）替代。\"}, \"p2b_dataflow_retrain\": {\"status\": \"DONE\", \"notes\": \"Dataflow 策略重训练计划，因 embedding_distance 命名问题（实际用 BM25 而非 embedding）被 Reviewer 发现后搁置。已被 m2_embed_verify（true embedding mining）替代。\"}, \"p2b_eval_all\": {\"status\": \"DONE\", \"notes\": \"P2b 全量 eval（pool_size=26），被 D013 服务器迁移计划取消。已被 p2b_eval_4runs_pool50（pool_size=50）替代。\"}, \"m2_early_pilot\": {\"status\": \"DONE\", \"hypothesis\": \"Early pilot on partial M1 data (24 repos, ~5K instances): verify M2 training pipeline works end-to-end and get early signal on 3-strategy differentiation before full M1 completes\", \"notes\": \"PID 795791 在 cqa1 cuda:4 运行，wrapper 脚本顺序跑 random→embedding→dataflow（set -e）。random 策略跑到 step 4000 后卡住（~45min 无新日志），embedding/dataflow 未启动。Best checkpoint at step 1500。Val_loss 持续恶化（0.5879→0.728），明显过拟合。另有 OOM 进程干扰（某进程试图在同 GPU 启动导致 OOM，可能破坏 GPU 状态）。eval recall@k bug 已确认。\"}, \"m2_early_pilot_v3\": {\"status\": \"DONE\", \"notes\": \"GPU 越界 cuda:0，违反项目 GPU 分配 gpu_ids=[\\\"cuda:4\\\"]。第二次 GPU 越界违规（首次 D005）。Worker 未正确映射 CUDA_VISIBLE_DEVICES。\"}, \"m2_early_pilot_v2\": {\"status\": \"DONE\", \"hypothesis\": \"Early pilot on partial M1 data (24 repos, 2672 train + 746 val): verify M2 training pipeline works end-to-end and get early signal on 3-strategy differentiation before full M1 completes\", \"notes\": \"wandb API key error, EXIT_CODE=1。首次提交因 wandb 未配置离线模式而立即退出。\"}, \"mvp_p2b_contrastive_training\": {\"status\": \"DONE\", \"notes\": \"4/9 runs 完成 (random×3 + embedding_distance_s42), 5/9 失败 (磁盘满 torch.save RuntimeError). /root/autodl-tmp 93% (14GB剩余, 每个checkpoint 5.8GB). 失败从 embedding_distance_s123 开始级联.\"}, \"p2b_eval_4runs_pool50\": {\"status\": \"DONE\"}, \"d007_50repo_overlap\": {\"status\": \"DONE\"}, \"p2b_5reruns\": {\"status\": \"DONE\"}, \"p2b_eval_4runs_v2\": {\"status\": \"DONE\"}, \"p2b-all-9runs\": {\"status\": \"DONE\"}, \"p2b-smoke8\": {\"status\": \"DONE\"}, \"p2b-smoke7\": {\"status\": \"DONE\"}, \"p2b-smoke6\": {\"status\": \"DONE\"}, \"p2b-smoke5\": {\"status\": \"DONE\"}, \"p2b-smoke4\": {\"status\": \"DONE\"}, \"p2b-smoke3\": {\"status\": \"DONE\"}, \"p2b-smoke2\": {\"status\": \"DONE\"}, \"p2b-smoke-test\": {\"status\": \"DONE\"}, \"mvp_p2a_linear_proxy\": {\"status\": \"DONE\"}, \"mvp_p1_codeql_feasibility\": {\"status\": \"DONE\"}}, \"count\": 37, \"total\": 37, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.1086}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9ee2acb9-ddf8-4ced-9b60-8a1554c992bd",
  "isSidechain": false,
  "promptId": "255fffc4-c17f-4b3b-8b5c-7a3031fdb918",
  "type": "user",
  "uuid": "9a64f1d5-77f6-4f2e-95b2-596759f68e22",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"experiments\\\": {\\\"m1_reextract_v2\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"hypothesis\\\": \\\"M1 重提取 v2：恢复 28,276 个因运行时瞬态文件系统故障失败的 instances（82 repos）。CodeQL pack 已修复，端到端测试通过。预期将训练数据从 15,897 提升至 ~44,173。D022 批准。\\\", \\\"notes\\\": \\\"M1 重提取 v2：CodeQL pack 已修复，端到端测试通过。28,276 instances / 82 repo groups / 4 workers 并行。启动 2026-05-14 03:59 CST。[诊断 07:06 CST] 活跃运行中，~15/82 groups 完成，2,469 次 call_graph 查询成功，预计还需 ~13-16h。仅前 4 个旧 repo（furl/pyasn1/feedparser/python-docx）复用 v1 旧 DB 有 18 次降级 WARNING，04:02 之后零失败。产出写入 all.jsonl（追加模式）。磁盘 97GB 可用。[Director 决策 Session 8] 即使数据量增至 ~44K，不重跑 M2（ARR May 25 DDL 不允许再加 4-5 天重训）。处理方式：(1) post-M2 完成后如有 GPU 空档，跑 1-seed pilot (Qwen, embedding, 新数据) 对比当前 M2 baseline; (2) 论文中作为 scalability/data efficiency 讨论点; (3) 全量重训留 camera-ready。[进度检查 2026-05-15 05:05 CST] 80.8% 完成（22,842/28,276），0 ERROR，速率 ~560/hr，处理中大 repo：mozilla__bleach/sqlfluff/conan-io/Project-MONAI。产出为单独 .json 文件，尚未合并 all.jsonl。预计 ~15:00 CST May 15 完成。\\\"}, \\\"m2_full_starcoder_resumed\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"hypothesis\\\": \\\"M2 StarCoder resumed: 继续 m2_full_starcoder 的 8 sequential runs (random×2 + embedding×3 + dataflow×3)。原实验因 cron timeout 标记为 failed，实际 PID 519791 正常运行。\\\"}, \\\"m2_full_qwen_continued\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"hypothesis\\\": \\\"M2 Qwen continued: 继续 m2_full_qwen 的剩余 runs (random_s44 + embedding×3 + dataflow×3)。原实验 cron 在 s42 退出时自动设为 ANALYZING，但链仍在运行。\\\"}, \\\"plan_005_stratified\\\": {\\\"status\\\": \\\"PREPARING\\\", \\\"hypothesis\\\": \\\"Plan 005 分层分析：按 repo size/pool size/query-pos similarity/structural data availability/neg_difficulty quartile 5 维度分层评估 embedding vs random 策略差异，控制 pool_size confound。Claim 2 支撑实验。v2 结果为 ground truth（v1→v2 changelog 见 art_20260514_3008c4）。\\\", \\\"notes\\\": \\\"plan_id=plan_005. 分层评估脚本已完成全部修改（analyze_stratified.py）：(1) mock seed 确定性修复 (2) pool_size-controlled 策略对比（within-bin delta + weighted aggregate）(3) dataflow×pool_size 交叉分析（n<30 标记 underpowered）(4) checkpoint 发现逻辑已就绪（best_by_recall_at_1 / best / best_by_val_loss）。输出含 JSON + CSV + PDF。[2026-05-14 21:07] Worker 完成 5 项 Patch：(P1) reeval_checkpoint 重写为 batch encoding（query/positive/negatives 分组批量编码，tqdm 进度条，torch.no_grad + model.eval，pad_token 兜底）(P2) 新增 --batch-size 参数（默认 64）(P3) 调用处传递 batch_size (P4) 非 dry-run 自适应 sim bins（tercile 计算边界 + 重新分配 sim_bin）(P5) 输出 JSON 记录 similarity_bin_edges 和 batch_size。Dry-run 验证全部通过。真实评估待 M2 全部 checkpoint 就绪后执行。\\\"}, \\\"plan_017_literature\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"Inference-time graph method comparison: 8 papers surveyed (CodexGraph, LocAgent, RANGER, GraphCoder, ARISE, RepoGraph, CodeGRAG, CodeRAG). Discussion v2 drafted, all citations verified. Conclusion: training-time vs inference-time complementary.\\\"}, \\\"m2_full_starcoder\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"Full M2 StarCoder: 3 strategies × 3 seeds on full M1 data. Cross-encoder validation — if embedding > random holds for both Qwen and StarCoder, method is encoder-agnostic. Resolves plan_013 pilot negative (dataflow encoder-dependent).\\\", \\\"notes\\\": \\\"Phase 1: 构建 StarCoder embedding negatives 完成。Phase 2: 9 runs 训练中。batch_size=8, num_negatives=7, epochs=3(s42)/2(s43+), lr=2e-5, eval_steps=500, no early_stopping。双 checkpoint: best + best_by_recall_at_1。Seeds: 42,43,44。[D026] s42 保持 3 epochs; s43/s44 及后续 runs 改为 2 epochs。[2026-05-15 02:02 CST] cuda:1 进程冲突修复并重新提交（PID 519791, timeout=144h）。Registry 状态 DONE(failed) 是旧 cron timeout 标记，实际正在运行 random_s43 [1/8]。新 cron 已注册监控 PID 519791。序列：random_s43→s44→(待插入bm25_s42)→embedding×3→dataflow×3。random_s42 结果：best R@1=0.4604 at step 2500, val_loss=0.6134 at step 1000。\\\"}, \\\"m2_full_qwen\\\": {\\\"status\\\": \\\"ANALYZING\\\", \\\"hypothesis\\\": \\\"Full M2 Qwen: 3 strategies (random/embedding/dataflow) × 3 seeds on full M1 data (~11K train/seed). Statistical validation of pilot signal (embedding > random +2pp). Go/no-go for paper claims per D018.\\\", \\\"notes\\\": \\\"Full M2 go/no-go: 3 strategies (random, embedding_distance, dataflow_aware) × 3 seeds (42, 43, 44) = 9 runs sequential on cuda:0. Config: lr=2e-5, batch_size=8, eval_steps=500, num_negatives=7, max_seq_length=2048, warmup_ratio=0.1, weight_decay=0.01, temperature=0.07, LoRA r=16, gradient_checkpointing=True, proj_dim=256. Dual checkpoint: best_by_val_loss + best_by_recall_at_1. Train ~11.3K/seed, val ~3K/seed. [D026] s42 保持 3 epochs 提供完整 overfitting curve; s43/s44 及后续 runs 改为 2 epochs + early_stopping_patience=2。[STATUS 2026-05-15 00:19 CST] Registry 状态 ANALYZING 是 cron 自动设置（s42 进程退出触发），但实验实际仍在进行中。random_s43 在 cuda:0 正常运行，step 1200/2810 (43%)。eval@500 R@1=0.5357, eval@1000 R@1=0.5285 (early_stopping 1/2)。Best R@1=0.5357 at step 500。GPU 100% 利用率, 50.5/97.9GB VRAM。\\\"}, \\\"plan_018_bm25\\\": {\\\"status\\\": \\\"QUEUED\\\", \\\"hypothesis\\\": \\\"BM25 negative baseline: Dream 审稿三档一致认定缺 BM25 baseline 是论文最大结构性缺陷。Phase 1 (CPU): 对 M2 训练语料建 BM25 索引，挖掘 BM25 hard negatives，生成训练数据。Phase 2 (GPU): 用 BM25 negatives 训练 Qwen + StarCoder 各 1 seed，对比 R@1。\\\", \\\"notes\\\": \\\"Phase 1 (CPU) COMPLETE: BM25 negative mining 完成。3 seeds 数据生成，record counts 与其他策略完全一致，0 fallback。BM25 score 分布: mean=246.50, std=155.96。重叠率: BM25 vs embedding_distance ~87.1%, vs random ~76.2%, vs dataflow_aware ~71.8%。高 median=1.0 因小 repo 候选池≤50 文件导致策略完全重合，BM25 differentiation 主要在大 repo。脚本: /root/structfuse/scripts/mine_bm25_negatives.py。输出: /root/autodl-tmp/structfuse/full_m2_training_data/{train,val}_bm25_s{42,43,44}.jsonl。Phase 2 (GPU): 等 re-dream gate 通过 + M2 完成后训练。\\\"}, \\\"plan_015_dynamic\\\": {\\\"status\\\": \\\"QUEUED\\\", \\\"hypothesis\\\": \\\"Dynamic negative mining (epoch-level re-mining): 每 epoch 重新用当前 encoder embedding 挖掘 negatives，验证 static mining 是否足够。缩减版：只跑 dynamic_ep × 1 seed (Qwen, s42)，~11h 单卡。若 dynamic ≈ static（预期 <1pp 差异），在 Limitation 段排除 confound。\\\", \\\"notes\\\": \\\"Director D031 缩减：原 44h → 11h 单卡。只跑 dynamic_ep × 1 seed (Qwen, s42)，跳过 dynamic_500。Post-M2 与 plan_003 并行（一卡 SWE-bench，一卡 dynamic_ep）。受 re-dream gate 约束。设计文档已由 Worker 完成。\\\"}, \\\"neg_difficulty_analysis\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"Negative difficulty distribution analysis: 用预训练 Qwen2.5-Coder-3B 和 StarCoder2-3B 计算 3 策略 (random/embedding/dataflow) 的 query-negative/positive cosine similarity，分析 pretrained representation separability 跨编码器差异。MAX_LENGTH=2048 匹配训练设置。\\\", \\\"notes\\\": \\\"128 vs 2048 token 对比完成（2026-05-14 05:54 CST）。Qwen pos_sim 在 2048t 下 0.9855（比 128t 的 0.9804 更高），确认 ceiling 为 Qwen 表征的结构性特征，非截断 artifact。StarCoder margin 2.6-4.1x Qwen（2048t）。核心结论：pretrained representation separability varies across encoders，跨两种 token 长度成立。数据源：128t → stats_v2.json，2048t → stats_v3_2048.json。\\\"}, \\\"m1_reextract\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"M1 重提取：恢复 28,276 个因运行时瞬态文件系统故障失败的 instances（82 repos）。预期将训练数据从 15,897 提升至 ~44,173。D022 批准。\\\", \\\"notes\\\": \\\"CodeQL query 100% 失败（exit status 2）。根因：Worker 安装 CodeQL CLI 2.25.4 时未执行 `codeql pack install`，`codeql/python-all@7.1.0` 标准库 pack 缺失。修复命令：`cd /root/structfuse/extraction/codeql_queries && /opt/codeql/codeql pack install`。已 kill 进程 + tmux session。无新数据产出（all.jsonl 未受影响）。等 Director 确认后修复重跑。\\\"}, \\\"m1_extraction\\\": {\\\"status\\\": \\\"DONE\\\", \\\"notes\\\": \\\"[2026-05-13 19:25] COMPLETED. 837.8min, 123/131 repos (93.9%), 15,897/44,173 instances with structural data (36.0%), 6,696 skipped (clone/checkout). Output: all.jsonl 6.6GB. [2026-05-13 19:23 UPDATE] 28,276 buggy_file_not_found errors 经验证并非上游数据质量问题——10/10 抽查的文件在 repo 中全部存在。根因是运行时瞬态文件系统故障（CodeQL 并行 database creation 导致磁盘耗尽，锐截止模式）。这些 instances 可通过重跑恢复。D022: 准备重跑脚本中，等 Director 确认后执行。\\\"}, \\\"plan_006_scalability\\\": {\\\"status\\\": \\\"DONE\\\", \\\"notes\\\": \\\"[2026-05-13 19:23] 全量统计 + error 分析 + fuzzy match 验证完成。关键发现: (1) 0 timeout; (2) 28,276 error 全部 buggy_file_not_found，但 fuzzy match 验证发现文件实际都存在——根因是运行时瞬态文件系统故障（锐截止模式：每个 repo 内先成功后突然全部失败，extraction_time=0.0s），可能是 CodeQL 并行数据库创建导致磁盘空间耗尽; (3) 这些 instance 可通过重跑恢复（当前 resolve_file_in_repo 对全部样本返回正确路径）; (4) 结构数据率 34.3% 有望提升至接近 100%（若重跑成功）; (5) Z% 随 repo 规模上升 (XL median 96%). Artifacts: plan006_full_scalability.json, art_20260513_d262da (error patterns)\\\", \\\"hypothesis\\\": \\\"Claim 3: CodeQL bounded data-flow extraction scales to large repos with acceptable timeout rates and provides meaningful structural coverage (Z%) that increases with repo complexity\\\"}, \\\"plan_013_starcoder\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"Architecture generalization: validate StructFuse with StarCoder2-3B encoder (vs Qwen2.5-Coder-3B in m2_embed_verify). If both encoders show same strategy ranking → method is encoder-agnostic, strengthening the core claim. Key differentiator for best→accept at Dream.\\\", \\\"notes\\\": \\\"[2026-05-13 16:00] ALL 3 STRATEGIES DONE. Ranking: embedding (R@1=0.5078) > random (0.4922) > dataflow (0.4869). Embedding vs random: +1.6pp (consistent with Qwen). Dataflow vs random: -0.5pp (DIFFERS from Qwen where dataflow > random +0.8pp). Hypothesis NEGATIVE: strategy ranking NOT identical across encoders. Embedding > random is encoder-agnostic, dataflow position is encoder-dependent. Log: /root/runs/faith-evidence-ie/plan_013_starcoder.log. Cron misreported EXIT_CODE=129 but all strategies completed (confirmed via log extraction worker).\\\"}, \\\"m2_embed_verify\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"True embedding mining verification: compare Qwen2.5-Coder-3B cosine similarity negatives vs BM25 negatives on pilot data (24 repos). If true embedding negatives are harder → Claim 2 (structure-aware negatives improve retrieval) gets stronger evidence.\\\", \\\"notes\\\": \\\"[2026-05-13 16:00] ALL 3 STRATEGIES DONE. Ranking: embedding (R@1=0.5557) > dataflow (0.5436) > random (0.5357). Embedding vs random: +2.0pp. Dataflow vs random: +0.8pp. All best at step 500, overfitting after. Hypothesis confirmed: true embedding negatives are harder → Claim 2 supported. Log: /root/runs/faith-evidence-ie/m2_embed_verify.log. Cron misreported EXIT_CODE=2 but all strategies completed successfully (confirmed via log extraction worker).\\\"}, \\\"mvp_p2b_contrastive_v2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"notes\\\": \\\"P2b 对比训练 v2，因磁盘空间不足被 kill。已被 p2b_5reruns（成功完成 9/9 runs）替代。\\\"}, \\\"p2b_dataflow_retrain\\\": {\\\"status\\\": \\\"DONE\\\", \\\"notes\\\": \\\"Dataflow 策略重训练计划，因 embedding_distance 命名问题（实际用 BM25 而非 embedding）被 Reviewer 发现后搁置。已被 m2_embed_verify（true embedding mining）替代。\\\"}, \\\"p2b_eval_all\\\": {\\\"status\\\": \\\"DONE\\\", \\\"notes\\\": \\\"P2b 全量 eval（pool_size=26），被 D013 服务器迁移计划取消。已被 p2b_eval_4runs_pool50（pool_size=50）替代。\\\"}, \\\"m2_early_pilot\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"Early pilot on partial M1 data (24 repos, ~5K instances): verify M2 training pipeline works end-to-end and get early signal on 3-strategy differentiation before full M1 completes\\\", \\\"notes\\\": \\\"PID 795791 在 cqa1 cuda:4 运行，wrapper 脚本顺序跑 random→embedding→dataflow（set -e）。random 策略跑到 step 4000 后卡住（~45min 无新日志），embedding/dataflow 未启动。Best checkpoint at step 1500。Val_loss 持续恶化（0.5879→0.728），明显过拟合。另有 OOM 进程干扰（某进程试图在同 GPU 启动导致 OOM，可能破坏 GPU 状态）。eval recall@k bug 已确认。\\\"}, \\\"m2_early_pilot_v3\\\": {\\\"status\\\": \\\"DONE\\\", \\\"notes\\\": \\\"GPU 越界 cuda:0，违反项目 GPU 分配 gpu_ids=[\\\\\\\"cuda:4\\\\\\\"]。第二次 GPU 越界违规（首次 D005）。Worker 未正确映射 CUDA_VISIBLE_DEVICES。\\\"}, \\\"m2_early_pilot_v2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"Early pilot on partial M1 data (24 repos, 2672 train + 746 val): verify M2 training pipeline works end-to-end and get early signal on 3-strategy differentiation before full M1 completes\\\", \\\"notes\\\": \\\"wandb API key error, EXIT_CODE=1。首次提交因 wandb 未配置离线模式而立即退出。\\\"}, \\\"mvp_p2b_contrastive_training\\\": {\\\"status\\\": \\\"DONE\\\", \\\"notes\\\": \\\"4/9 runs 完成 (random×3 + embedding_distance_s42), 5/9 失败 (磁盘满 torch.save RuntimeError). /root/autodl-tmp 93% (14GB剩余, 每个checkpoint 5.8GB). 失败从 embedding_distance_s123 开始级联.\\\"}, \\\"p2b_eval_4runs_pool50\\\": {\\\"status\\\": \\\"DONE\\\"}, \\\"d007_50repo_overlap\\\": {\\\"status\\\": \\\"DONE\\\"}, \\\"p2b_5reruns\\\": {\\\"status\\\": \\\"DONE\\\"}, \\\"p2b_eval_4runs_v2\\\": {\\\"status\\\": \\\"DONE\\\"}, \\\"p2b-all-9runs\\\": {\\\"status\\\": \\\"DONE\\\"}, \\\"p2b-smoke8\\\": {\\\"status\\\": \\\"DONE\\\"}, \\\"p2b-smoke7\\\": {\\\"status\\\": \\\"DONE\\\"}, \\\"p2b-smoke6\\\": {\\\"status\\\": \\\"DONE\\\"}, \\\"p2b-smoke5\\\": {\\\"status\\\": \\\"DONE\\\"}, \\\"p2b-smoke4\\\": {\\\"status\\\": \\\"DONE\\\"}, \\\"p2b-smoke3\\\": {\\\"status\\\": \\\"DONE\\\"}, \\\"p2b-smoke2\\\": {\\\"status\\\": \\\"DONE\\\"}, \\\"p2b-smoke-test\\\": {\\\"status\\\": \\\"DONE\\\"}, \\\"mvp_p2a_linear_proxy\\\": {\\\"status\\\": \\\"DONE\\\"}, \\\"mvp_p1_codeql_feasibility\\\": {\\\"status\\\": \\\"DONE\\\"}}, \\\"count\\\": 37, \\\"total\\\": 37, \\\"baseline\\\": null}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.1086}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {\"m1_reextract_v2\": {\"status\": \"RUNNING\", \"hypothesis\": \"M1 重提取 v2：恢复 28,276 个因运行时瞬态文件系统故障失败的 instances（82 repos）。CodeQL pack 已修复，端到端测试通过。预期将训练数据从 15,897 提升至 ~44,173。D022 批准。\", \"notes\": \"M1 重提取 v2：CodeQL pack 已修复，端到端测试通过。28,276 instances / 82 repo groups / 4 workers 并行。启动 2026-05-14 03:59 CST。[诊断 07:06 CST] 活跃运行中，~15/82 groups 完成，2,469 次 call_graph 查询成功，预计还需 ~13-16h。仅前 4 个旧 repo（furl/pyasn1/feedparser/python-docx）复用 v1 旧 DB 有 18 次降级 WARNING，04:02 之后零失败。产出写入 all.jsonl（追加模式）。磁盘 97GB 可用。[Director 决策 Session 8] 即使数据量增至 ~44K，不重跑 M2（ARR May 25 DDL 不允许再加 4-5 天重训）。处理方式：(1) post-M2 完成后如有 GPU 空档，跑 1-seed pilot (Qwen, embedding, 新数据) 对比当前 M2 baseline; (2) 论文中作为 scalability/data efficiency 讨论点; (3) 全量重训留 camera-ready。[进度检查 2026-05-15 05:05 CST] 80.8% 完成（22,842/28,276），0 ERROR，速率 ~560/hr，处理中大 repo：mozilla__bleach/sqlfluff/conan-io/Project-MONAI。产出为单独 .json 文件，尚未合并 all.jsonl。预计 ~15:00 CST May 15 完成。\"}, \"m2_full_starcoder_resumed\": {\"status\": \"RUNNING\", \"hypothesis\": \"M2 StarCoder resumed: 继续 m2_full_starcoder 的 8 sequential runs (random×2 + embedding×3 + dataflow×3)。原实验因 cron timeout 标记为 failed，实际 PID 519791 正常运行。\"}, \"m2_full_qwen_continued\": {\"status\": \"RUNNING\", \"hypothesis\": \"M2 Qwen continued: 继续 m2_full_qwen 的剩余 runs (random_s44 + embedding×3 + dataflow×3)。原实验 cron 在 s42 退出时自动设为 ANALYZING，但链仍在运行。\"}, \"plan_005_stratified\": {\"status\": \"PREPARING\", \"hypothesis\": \"Plan 005 分层分析：按 repo size/pool size/query-pos similarity/structural data availability/neg_difficulty quartile 5 维度分层评估 embedding vs random 策略差异，控制 pool_size confound。Claim 2 支撑实验。v2 结果为 ground truth（v1→v2 changelog 见 art_20260514_3008c4）。\", \"notes\": \"plan_id=plan_005. 分层评估脚本已完成全部修改（analyze_stratified.py）：(1) mock seed 确定性修复 (2) pool_size-controlled 策略对比（within-bin delta + weighted aggregate）(3) dataflow×pool_size 交叉分析（n<30 标记 underpowered）(4) checkpoint 发现逻辑已就绪（best_by_recall_at_1 / best / best_by_val_loss）。输出含 JSON + CSV + PDF。[2026-05-14 21:07] Worker 完成 5 项 Patch：(P1) reeval_checkpoint 重写为 batch encoding（query/positive/negatives 分组批量编码，tqdm 进度条，torch.no_grad + model.eval，pad_token 兜底）(P2) 新增 --batch-size 参数（默认 64）(P3) 调用处传递 batch_size (P4) 非 dry-run 自适应 sim bins（tercile 计算边界 + 重新分配 sim_bin）(P5) 输出 JSON 记录 similarity_bin_edges 和 batch_size。Dry-run 验证全部通过。真实评估待 M2 全部 checkpoint 就绪后执行。\"}, \"plan_017_literature\": {\"status\": \"DONE\", \"hypothesis\": \"Inference-time graph method comparison: 8 papers surveyed (CodexGraph, LocAgent, RANGER, GraphCoder, ARISE, RepoGraph, CodeGRAG, CodeRAG). Discussion v2 drafted, all citations verified. Conclusion: training-time vs inference-time complementary.\"}, \"m2_full_starcoder\": {\"status\": \"DONE\", \"hypothesis\": \"Full M2 StarCoder: 3 strategies × 3 seeds on full M1 data. Cross-encoder validation — if embedding > random holds for both Qwen and StarCoder, method is encoder-agnostic. Resolves plan_013 pilot negative (dataflow encoder-dependent).\", \"notes\": \"Phase 1: 构建 StarCoder embedding negatives 完成。Phase 2: 9 runs 训练中。batch_size=8, num_negatives=7, epochs=3(s42)/2(s43+), lr=2e-5, eval_steps=500, no early_stopping。双 checkpoint: best + best_by_recall_at_1。Seeds: 42,43,44。[D026] s42 保持 3 epochs; s43/s44 及后续 runs 改为 2 epochs。[2026-05-15 02:02 CST] cuda:1 进程冲突修复并重新提交（PID 519791, timeout=144h）。Registry 状态 DONE(failed) 是旧 cron timeout 标记，实际正在运行 random_s43 [1/8]。新 cron 已注册监控 PID 519791。序列：random_s43→s44→(待插入bm25_s42)→embedding×3→dataflow×3。random_s42 结果：best R@1=0.4604 at step 2500, val_loss=0.6134 at step 1000。\"}, \"m2_full_qwen\": {\"status\": \"ANALYZING\", \"hypothesis\": \"Full M2 Qwen: 3 strategies (random/embedding/dataflow) × 3 seeds on full M1 data (~11K train/seed). Statistical validation of pilot signal (embedding > random +2pp). Go/no-go for paper claims per D018.\", \"notes\": \"Full M2 go/no-go: 3 strategies (random, embedding_distance, dataflow_aware) × 3 seeds (42, 43, 44) = 9 runs sequential on cuda:0. Config: lr=2e-5, batch_size=8, eval_steps=500, num_negatives=7, max_seq_length=2048, warmup_ratio=0.1, weight_decay=0.01, temperature=0.07, LoRA r=16, gradient_checkpointing=True, proj_dim=256. Dual checkpoint: best_by_val_loss + best_by_recall_at_1. Train ~11.3K/seed, val ~3K/seed. [D026] s42 保持 3 epochs 提供完整 overfitting curve; s43/s44 及后续 runs 改为 2 epochs + early_stopping_patience=2。[STATUS 2026-05-15 00:19 CST] Registry 状态 ANALYZING 是 cron 自动设置（s42 进程退出触发），但实验实际仍在进行中。random_s43 在 cuda:0 正常运行，step 1200/2810 (43%)。eval@500 R@1=0.5357, eval@1000 R@1=0.5285 (early_stopping 1/2)。Best R@1=0.5357 at step 500。GPU 100% 利用率, 50.5/97.9GB VRAM。\"}, \"plan_018_bm25\": {\"status\": \"QUEUED\", \"hypothesis\": \"BM25 negative baseline: Dream 审稿三档一致认定缺 BM25 baseline 是论文最大结构性缺陷。Phase 1 (CPU): 对 M2 训练语料建 BM25 索引，挖掘 BM25 hard negatives，生成训练数据。Phase 2 (GPU): 用 BM25 negatives 训练 Qwen + StarCoder 各 1 seed，对比 R@1。\", \"notes\": \"Phase 1 (CPU) COMPLETE: BM25 negative mining 完成。3 seeds 数据生成，record counts 与其他策略完全一致，0 fallback。BM25 score 分布: mean=246.50, std=155.96。重叠率: BM25 vs embedding_distance ~87.1%, vs random ~76.2%, vs dataflow_aware ~71.8%。高 median=1.0 因小 repo 候选池≤50 文件导致策略完全重合，BM25 differentiation 主要在大 repo。脚本: /root/structfuse/scripts/mine_bm25_negatives.py。输出: /root/autodl-tmp/structfuse/full_m2_training_data/{train,val}_bm25_s{42,43,44}.jsonl。Phase 2 (GPU): 等 re-dream gate 通过 + M2 完成后训练。\"}, \"plan_015_dynamic\": {\"status\": \"QUEUED\", \"hypothesis\": \"Dynamic negative mining (epoch-level re-mining): 每 epoch 重新用当前 encoder embedding 挖掘 negatives，验证 static mining 是否足够。缩减版：只跑 dynamic_ep × 1 seed (Qwen, s42)，~11h 单卡。若 dynamic ≈ static（预期 <1pp 差异），在 Limitation 段排除 confound。\", \"notes\": \"Director D031 缩减：原 44h → 11h 单卡。只跑 dynamic_ep × 1 seed (Qwen, s42)，跳过 dynamic_500。Post-M2 与 plan_003 并行（一卡 SWE-bench，一卡 dynamic_ep）。受 re-dream gate 约束。设计文档已由 Worker 完成。\"}, \"neg_difficulty_analysis\": {\"status\": \"DONE\", \"hypothesis\": \"Negative difficulty distribution analysis: 用预训练 Qwen2.5-Coder-3B 和 StarCoder2-3B 计算 3 策略 (random/embedding/dataflow) 的 query-negative/positive cosine similarity，分析 pretrained representation separability 跨编码器差异。MAX_LENGTH=2048 匹配训练设置。\", \"notes\": \"128 vs 2048 token 对比完成（2026-05-14 05:54 CST）。Qwen pos_sim 在 2048t 下 0.9855（比 128t 的 0.9804 更高），确认 ceiling 为 Qwen 表征的结构性特征，非截断 artifact。StarCoder margin 2.6-4.1x Qwen（2048t）。核心结论：pretrained representation separability varies across encoders，跨两种 token 长度成立。数据源：128t → stats_v2.json，2048t → stats_v3_2048.json。\"}, \"m1_reextract\": {\"status\": \"DONE\", \"hypothesis\": \"M1 重提取：恢复 28,276 个因运行时瞬态文件系统故障失败的 instances（82 repos）。预期将训练数据从 15,897 提升至 ~44,173。D022 批准。\", \"notes\": \"CodeQL query 100% 失败（exit status 2）。根因：Worker 安装 CodeQL CLI 2.25.4 时未执行 `codeql pack install`，`codeql/python-all@7.1.0` 标准库 pack 缺失。修复命令：`cd /root/structfuse/extraction/codeql_queries && /opt/codeql/codeql pack install`。已 kill 进程 + tmux session。无新数据产出（all.jsonl 未受影响）。等 Director 确认后修复重跑。\"}, \"m1_extraction\": {\"status\": \"DONE\", \"notes\": \"[2026-05-13 19:25] COMPLETED. 837.8min, 123/131 repos (93.9%), 15,897/44,173 instances with structural data (36.0%), 6,696 skipped (clone/checkout). Output: all.jsonl 6.6GB. [2026-05-13 19:23 UPDATE] 28,276 buggy_file_not_found errors 经验证并非上游数据质量问题——10/10 抽查的文件在 repo 中全部存在。根因是运行时瞬态文件系统故障（CodeQL 并行 database creation 导致磁盘耗尽，锐截止模式）。这些 instances 可通过重跑恢复。D022: 准备重跑脚本中，等 Director 确认后执行。\"}, \"plan_006_scalability\": {\"status\": \"DONE\", \"notes\": \"[2026-05-13 19:23] 全量统计 + error 分析 + fuzzy match 验证完成。关键发现: (1) 0 timeout; (2) 28,276 error 全部 buggy_file_not_found，但 fuzzy match 验证发现文件实际都存在——根因是运行时瞬态文件系统故障（锐截止模式：每个 repo 内先成功后突然全部失败，extraction_time=0.0s），可能是 CodeQL 并行数据库创建导致磁盘空间耗尽; (3) 这些 instance 可通过重跑恢复（当前 resolve_file_in_repo 对全部样本返回正确路径）; (4) 结构数据率 34.3% 有望提升至接近 100%（若重跑成功）; (5) Z% 随 repo 规模上升 (XL median 96%). Artifacts: plan006_full_scalability.json, art_20260513_d262da (error patterns)\", \"hypothesis\": \"Claim 3: CodeQL bounded data-flow extraction scales to large repos with acceptable timeout rates and provides meaningful structural coverage (Z%) that increases with repo complexity\"}, \"plan_013_starcoder\": {\"status\": \"DONE\", \"hypothesis\": \"Architecture generalization: validate StructFuse with StarCoder2-3B encoder (vs Qwen2.5-Coder-3B in m2_embed_verify). If both encoders show same strategy ranking → method is encoder-agnostic, strengthening the core claim. Key differentiator for best→accept at Dream.\", \"notes\": \"[2026-05-13 16:00] ALL 3 STRATEGIES DONE. Ranking: embedding (R@1=0.5078) > random (0.4922) > dataflow (0.4869). Embedding vs random: +1.6pp (consistent with Qwen). Dataflow vs random: -0.5pp (DIFFERS from Qwen where dataflow > random +0.8pp). Hypothesis NEGATIVE: strategy ranking NOT identical across encoders. Embedding > random is encoder-agnostic, dataflow position is encoder-dependent. Log: /root/runs/faith-evidence-ie/plan_013_starcoder.log. Cron misreported EXIT_CODE=129 but all strategies completed (confirmed via log extraction worker).\"}, \"m2_embed_verify\": {\"status\": \"DONE\", \"hypothesis\": \"True embedding mining verification: compare Qwen2.5-Coder-3B cosine similarity negatives vs BM25 negatives on pilot data (24 repos). If true embedding negatives are harder → Claim 2 (structure-aware negatives improve retrieval) gets stronger evidence.\", \"notes\": \"[2026-05-13 16:00] ALL 3 STRATEGIES DONE. Ranking: embedding (R@1=0.5557) > dataflow (0.5436) > random (0.5357). Embedding vs random: +2.0pp. Dataflow vs random: +0.8pp. All best at step 500, overfitting after. Hypothesis confirmed: true embedding negatives are harder → Claim 2 supported. Log: /root/runs/faith-evidence-ie/m2_embed_verify.log. Cron misreported EXIT_CODE=2 but all strategies completed successfully (confirmed via log extraction worker).\"}, \"mvp_p2b_contrastive_v2\": {\"status\": \"DONE\", \"notes\": \"P2b 对比训练 v2，因磁盘空间不足被 kill。已被 p2b_5reruns（成功完成 9/9 runs）替代。\"}, \"p2b_dataflow_retrain\": {\"status\": \"DONE\", \"notes\": \"Dataflow 策略重训练计划，因 embedding_distance 命名问题（实际用 BM25 而非 embedding）被 Reviewer 发现后搁置。已被 m2_embed_verify（true embedding mining）替代。\"}, \"p2b_eval_all\": {\"status\": \"DONE\", \"notes\": \"P2b 全量 eval（pool_size=26），被 D013 服务器迁移计划取消。已被 p2b_eval_4runs_pool50（pool_size=50）替代。\"}, \"m2_early_pilot\": {\"status\": \"DONE\", \"hypothesis\": \"Early pilot on partial M1 data (24 repos, ~5K instances): verify M2 training pipeline works end-to-end and get early signal on 3-strategy differentiation before full M1 completes\", \"notes\": \"PID 795791 在 cqa1 cuda:4 运行，wrapper 脚本顺序跑 random→embedding→dataflow（set -e）。random 策略跑到 step 4000 后卡住（~45min 无新日志），embedding/dataflow 未启动。Best checkpoint at step 1500。Val_loss 持续恶化（0.5879→0.728），明显过拟合。另有 OOM 进程干扰（某进程试图在同 GPU 启动导致 OOM，可能破坏 GPU 状态）。eval recall@k bug 已确认。\"}, \"m2_early_pilot_v3\": {\"status\": \"DONE\", \"notes\": \"GPU 越界 cuda:0，违反项目 GPU 分配 gpu_ids=[\\\"cuda:4\\\"]。第二次 GPU 越界违规（首次 D005）。Worker 未正确映射 CUDA_VISIBLE_DEVICES。\"}, \"m2_early_pilot_v2\": {\"status\": \"DONE\", \"hypothesis\": \"Early pilot on partial M1 data (24 repos, 2672 train + 746 val): verify M2 training pipeline works end-to-end and get early signal on 3-strategy differentiation before full M1 completes\", \"notes\": \"wandb API key error, EXIT_CODE=1。首次提交因 wandb 未配置离线模式而立即退出。\"}, \"mvp_p2b_contrastive_training\": {\"status\": \"DONE\", \"notes\": \"4/9 runs 完成 (random×3 + embedding_distance_s42), 5/9 失败 (磁盘满 torch.save RuntimeError). /root/autodl-tmp 93% (14GB剩余, 每个checkpoint 5.8GB). 失败从 embedding_distance_s123 开始级联.\"}, \"p2b_eval_4runs_pool50\": {\"status\": \"DONE\"}, \"d007_50repo_overlap\": {\"status\": \"DONE\"}, \"p2b_5reruns\": {\"status\": \"DONE\"}, \"p2b_eval_4runs_v2\": {\"status\": \"DONE\"}, \"p2b-all-9runs\": {\"status\": \"DONE\"}, \"p2b-smoke8\": {\"status\": \"DONE\"}, \"p2b-smoke7\": {\"status\": \"DONE\"}, \"p2b-smoke6\": {\"status\": \"DONE\"}, \"p2b-smoke5\": {\"status\": \"DONE\"}, \"p2b-smoke4\": {\"status\": \"DONE\"}, \"p2b-smoke3\": {\"status\": \"DONE\"}, \"p2b-smoke2\": {\"status\": \"DONE\"}, \"p2b-smoke-test\": {\"status\": \"DONE\"}, \"mvp_p2a_linear_proxy\": {\"status\": \"DONE\"}, \"mvp_p1_codeql_feasibility\": {\"status\": \"DONE\"}}, \"count\": 37, \"total\": 37, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.1086}}"
    }
  },
  "sourceToolAssistantUUID": "9ee2acb9-ddf8-4ced-9b60-8a1554c992bd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "b1d97499-4652-4822-8fc5-dbdc566ceedc",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 46_

```json
{
  "type": "last-prompt",
  "leafUuid": "9a64f1d5-77f6-4f2e-95b2-596759f68e22",
  "sessionId": "b1d97499-4652-4822-8fc5-dbdc566ceedc"
}
```

---

### Runtime record

_source line 47_

```json
{
  "type": "ai-title",
  "aiTitle": "Fix literature reference consistency issues",
  "sessionId": "b1d97499-4652-4822-8fc5-dbdc566ceedc"
}
```

---

### Assistant

_source line 48 · 2026-05-14T21:32:38.872Z_

<details><summary>Logged reasoning block</summary>

````text
I found the plan_017_literature entry. Let me look at the relevant fields:

```
"plan_017_literature": {
  "status": "DONE", 
  "hypothesis": "Inference-time graph method comparison: 8 papers surveyed (CodexGraph, LocAgent, RANGER, GraphCoder, ARISE, RepoGraph, CodeGRAG, CodeRAG). Discussion v2 drafted, all citations verified. Conclusion: training-time vs inference-time complementary."
}
```

The notes field is not shown for this entry. Let me get the full entry with all fields.
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9a64f1d5-77f6-4f2e-95b2-596759f68e22",
  "isSidechain": false,
  "requestId": "req_011Cb3BCew1GRx3kt1QLz7GW",
  "type": "assistant",
  "uuid": "ac6a23ed-c98c-4d5b-bb87-801ce75883f6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "b1d97499-4652-4822-8fc5-dbdc566ceedc",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012MYaPBprAD5BNYYnWkKkg7",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5971,
      "cache_read_input_tokens": 41236,
      "output_tokens": 285,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5971,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 285,
          "cache_read_input_tokens": 41236,
          "cache_creation_input_tokens": 5971,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5971
          },
          "type": "message"
        }
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

_source line 49 · 2026-05-14T21:32:39.810Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_01LdMBPzfEnzxMbQB9WvBXL3`</summary>

```json
{
  "project": "structfuse-context",
  "filters": {
    "status": "DONE"
  },
  "fields": [
    "hypothesis",
    "notes",
    "status"
  ],
  "limit": 5
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ac6a23ed-c98c-4d5b-bb87-801ce75883f6",
  "isSidechain": false,
  "requestId": "req_011Cb3BCew1GRx3kt1QLz7GW",
  "type": "assistant",
  "uuid": "c9a1697b-ffe2-4eab-8bba-fcc5e6c4b8b4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "b1d97499-4652-4822-8fc5-dbdc566ceedc",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012MYaPBprAD5BNYYnWkKkg7",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5971,
      "cache_read_input_tokens": 41236,
      "output_tokens": 285,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5971,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 285,
          "cache_read_input_tokens": 41236,
          "cache_creation_input_tokens": 5971,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5971
          },
          "type": "message"
        }
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

_source line 50 · 2026-05-14T21:32:39.922Z_

<details><summary>↩ Tool result · `toolu_01LdMBPzfEnzxMbQB9WvBXL3`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"experiments\": {\"plan_017_literature\": {\"status\": \"DONE\", \"hypothesis\": \"Inference-time graph method comparison: 8 papers surveyed (CodexGraph, LocAgent, RANGER, GraphCoder, ARISE, RepoGraph, CodeGRAG, CodeRAG). Discussion v2 drafted, all citations verified. Conclusion: training-time vs inference-time complementary.\"}, \"m2_full_starcoder\": {\"status\": \"DONE\", \"hypothesis\": \"Full M2 StarCoder: 3 strategies × 3 seeds on full M1 data. Cross-encoder validation — if embedding > random holds for both Qwen and StarCoder, method is encoder-agnostic. Resolves plan_013 pilot negative (dataflow encoder-dependent).\", \"notes\": \"Phase 1: 构建 StarCoder embedding negatives 完成。Phase 2: 9 runs 训练中。batch_size=8, num_negatives=7, epochs=3(s42)/2(s43+), lr=2e-5, eval_steps=500, no early_stopping。双 checkpoint: best + best_by_recall_at_1。Seeds: 42,43,44。[D026] s42 保持 3 epochs; s43/s44 及后续 runs 改为 2 epochs。[2026-05-15 02:02 CST] cuda:1 进程冲突修复并重新提交（PID 519791, timeout=144h）。Registry 状态 DONE(failed) 是旧 cron timeout 标记，实际正在运行 random_s43 [1/8]。新 cron 已注册监控 PID 519791。序列：random_s43→s44→(待插入bm25_s42)→embedding×3→dataflow×3。random_s42 结果：best R@1=0.4604 at step 2500, val_loss=0.6134 at step 1000。\"}, \"neg_difficulty_analysis\": {\"status\": \"DONE\", \"hypothesis\": \"Negative difficulty distribution analysis: 用预训练 Qwen2.5-Coder-3B 和 StarCoder2-3B 计算 3 策略 (random/embedding/dataflow) 的 query-negative/positive cosine similarity，分析 pretrained representation separability 跨编码器差异。MAX_LENGTH=2048 匹配训练设置。\", \"notes\": \"128 vs 2048 token 对比完成（2026-05-14 05:54 CST）。Qwen pos_sim 在 2048t 下 0.9855（比 128t 的 0.9804 更高），确认 ceiling 为 Qwen 表征的结构性特征，非截断 artifact。StarCoder margin 2.6-4.1x Qwen（2048t）。核心结论：pretrained representation separability varies across encoders，跨两种 token 长度成立。数据源：128t → stats_v2.json，2048t → stats_v3_2048.json。\"}, \"m1_reextract\": {\"status\": \"DONE\", \"hypothesis\": \"M1 重提取：恢复 28,276 个因运行时瞬态文件系统故障失败的 instances（82 repos）。预期将训练数据从 15,897 提升至 ~44,173。D022 批准。\", \"notes\": \"CodeQL query 100% 失败（exit status 2）。根因：Worker 安装 CodeQL CLI 2.25.4 时未执行 `codeql pack install`，`codeql/python-all@7.1.0` 标准库 pack 缺失。修复命令：`cd /root/structfuse/extraction/codeql_queries && /opt/codeql/codeql pack install`。已 kill 进程 + tmux session。无新数据产出（all.jsonl 未受影响）。等 Director 确认后修复重跑。\"}, \"m1_extraction\": {\"status\": \"DONE\", \"notes\": \"[2026-05-13 19:25] COMPLETED. 837.8min, 123/131 repos (93.9%), 15,897/44,173 instances with structural data (36.0%), 6,696 skipped (clone/checkout). Output: all.jsonl 6.6GB. [2026-05-13 19:23 UPDATE] 28,276 buggy_file_not_found errors 经验证并非上游数据质量问题——10/10 抽查的文件在 repo 中全部存在。根因是运行时瞬态文件系统故障（CodeQL 并行 database creation 导致磁盘耗尽，锐截止模式）。这些 instances 可通过重跑恢复。D022: 准备重跑脚本中，等 Director 确认后执行。\"}}, \"count\": 5, \"total\": 30, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.0987}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c9a1697b-ffe2-4eab-8bba-fcc5e6c4b8b4",
  "isSidechain": false,
  "promptId": "255fffc4-c17f-4b3b-8b5c-7a3031fdb918",
  "type": "user",
  "uuid": "33ada081-c7c7-42b7-ba75-02c317085787",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"experiments\\\": {\\\"plan_017_literature\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"Inference-time graph method comparison: 8 papers surveyed (CodexGraph, LocAgent, RANGER, GraphCoder, ARISE, RepoGraph, CodeGRAG, CodeRAG). Discussion v2 drafted, all citations verified. Conclusion: training-time vs inference-time complementary.\\\"}, \\\"m2_full_starcoder\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"Full M2 StarCoder: 3 strategies × 3 seeds on full M1 data. Cross-encoder validation — if embedding > random holds for both Qwen and StarCoder, method is encoder-agnostic. Resolves plan_013 pilot negative (dataflow encoder-dependent).\\\", \\\"notes\\\": \\\"Phase 1: 构建 StarCoder embedding negatives 完成。Phase 2: 9 runs 训练中。batch_size=8, num_negatives=7, epochs=3(s42)/2(s43+), lr=2e-5, eval_steps=500, no early_stopping。双 checkpoint: best + best_by_recall_at_1。Seeds: 42,43,44。[D026] s42 保持 3 epochs; s43/s44 及后续 runs 改为 2 epochs。[2026-05-15 02:02 CST] cuda:1 进程冲突修复并重新提交（PID 519791, timeout=144h）。Registry 状态 DONE(failed) 是旧 cron timeout 标记，实际正在运行 random_s43 [1/8]。新 cron 已注册监控 PID 519791。序列：random_s43→s44→(待插入bm25_s42)→embedding×3→dataflow×3。random_s42 结果：best R@1=0.4604 at step 2500, val_loss=0.6134 at step 1000。\\\"}, \\\"neg_difficulty_analysis\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"Negative difficulty distribution analysis: 用预训练 Qwen2.5-Coder-3B 和 StarCoder2-3B 计算 3 策略 (random/embedding/dataflow) 的 query-negative/positive cosine similarity，分析 pretrained representation separability 跨编码器差异。MAX_LENGTH=2048 匹配训练设置。\\\", \\\"notes\\\": \\\"128 vs 2048 token 对比完成（2026-05-14 05:54 CST）。Qwen pos_sim 在 2048t 下 0.9855（比 128t 的 0.9804 更高），确认 ceiling 为 Qwen 表征的结构性特征，非截断 artifact。StarCoder margin 2.6-4.1x Qwen（2048t）。核心结论：pretrained representation separability varies across encoders，跨两种 token 长度成立。数据源：128t → stats_v2.json，2048t → stats_v3_2048.json。\\\"}, \\\"m1_reextract\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"M1 重提取：恢复 28,276 个因运行时瞬态文件系统故障失败的 instances（82 repos）。预期将训练数据从 15,897 提升至 ~44,173。D022 批准。\\\", \\\"notes\\\": \\\"CodeQL query 100% 失败（exit status 2）。根因：Worker 安装 CodeQL CLI 2.25.4 时未执行 `codeql pack install`，`codeql/python-all@7.1.0` 标准库 pack 缺失。修复命令：`cd /root/structfuse/extraction/codeql_queries && /opt/codeql/codeql pack install`。已 kill 进程 + tmux session。无新数据产出（all.jsonl 未受影响）。等 Director 确认后修复重跑。\\\"}, \\\"m1_extraction\\\": {\\\"status\\\": \\\"DONE\\\", \\\"notes\\\": \\\"[2026-05-13 19:25] COMPLETED. 837.8min, 123/131 repos (93.9%), 15,897/44,173 instances with structural data (36.0%), 6,696 skipped (clone/checkout). Output: all.jsonl 6.6GB. [2026-05-13 19:23 UPDATE] 28,276 buggy_file_not_found errors 经验证并非上游数据质量问题——10/10 抽查的文件在 repo 中全部存在。根因是运行时瞬态文件系统故障（CodeQL 并行 database creation 导致磁盘耗尽，锐截止模式）。这些 instances 可通过重跑恢复。D022: 准备重跑脚本中，等 Director 确认后执行。\\\"}}, \\\"count\\\": 5, \\\"total\\\": 30, \\\"baseline\\\": null}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.0987}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {\"plan_017_literature\": {\"status\": \"DONE\", \"hypothesis\": \"Inference-time graph method comparison: 8 papers surveyed (CodexGraph, LocAgent, RANGER, GraphCoder, ARISE, RepoGraph, CodeGRAG, CodeRAG). Discussion v2 drafted, all citations verified. Conclusion: training-time vs inference-time complementary.\"}, \"m2_full_starcoder\": {\"status\": \"DONE\", \"hypothesis\": \"Full M2 StarCoder: 3 strategies × 3 seeds on full M1 data. Cross-encoder validation — if embedding > random holds for both Qwen and StarCoder, method is encoder-agnostic. Resolves plan_013 pilot negative (dataflow encoder-dependent).\", \"notes\": \"Phase 1: 构建 StarCoder embedding negatives 完成。Phase 2: 9 runs 训练中。batch_size=8, num_negatives=7, epochs=3(s42)/2(s43+), lr=2e-5, eval_steps=500, no early_stopping。双 checkpoint: best + best_by_recall_at_1。Seeds: 42,43,44。[D026] s42 保持 3 epochs; s43/s44 及后续 runs 改为 2 epochs。[2026-05-15 02:02 CST] cuda:1 进程冲突修复并重新提交（PID 519791, timeout=144h）。Registry 状态 DONE(failed) 是旧 cron timeout 标记，实际正在运行 random_s43 [1/8]。新 cron 已注册监控 PID 519791。序列：random_s43→s44→(待插入bm25_s42)→embedding×3→dataflow×3。random_s42 结果：best R@1=0.4604 at step 2500, val_loss=0.6134 at step 1000。\"}, \"neg_difficulty_analysis\": {\"status\": \"DONE\", \"hypothesis\": \"Negative difficulty distribution analysis: 用预训练 Qwen2.5-Coder-3B 和 StarCoder2-3B 计算 3 策略 (random/embedding/dataflow) 的 query-negative/positive cosine similarity，分析 pretrained representation separability 跨编码器差异。MAX_LENGTH=2048 匹配训练设置。\", \"notes\": \"128 vs 2048 token 对比完成（2026-05-14 05:54 CST）。Qwen pos_sim 在 2048t 下 0.9855（比 128t 的 0.9804 更高），确认 ceiling 为 Qwen 表征的结构性特征，非截断 artifact。StarCoder margin 2.6-4.1x Qwen（2048t）。核心结论：pretrained representation separability varies across encoders，跨两种 token 长度成立。数据源：128t → stats_v2.json，2048t → stats_v3_2048.json。\"}, \"m1_reextract\": {\"status\": \"DONE\", \"hypothesis\": \"M1 重提取：恢复 28,276 个因运行时瞬态文件系统故障失败的 instances（82 repos）。预期将训练数据从 15,897 提升至 ~44,173。D022 批准。\", \"notes\": \"CodeQL query 100% 失败（exit status 2）。根因：Worker 安装 CodeQL CLI 2.25.4 时未执行 `codeql pack install`，`codeql/python-all@7.1.0` 标准库 pack 缺失。修复命令：`cd /root/structfuse/extraction/codeql_queries && /opt/codeql/codeql pack install`。已 kill 进程 + tmux session。无新数据产出（all.jsonl 未受影响）。等 Director 确认后修复重跑。\"}, \"m1_extraction\": {\"status\": \"DONE\", \"notes\": \"[2026-05-13 19:25] COMPLETED. 837.8min, 123/131 repos (93.9%), 15,897/44,173 instances with structural data (36.0%), 6,696 skipped (clone/checkout). Output: all.jsonl 6.6GB. [2026-05-13 19:23 UPDATE] 28,276 buggy_file_not_found errors 经验证并非上游数据质量问题——10/10 抽查的文件在 repo 中全部存在。根因是运行时瞬态文件系统故障（CodeQL 并行 database creation 导致磁盘耗尽，锐截止模式）。这些 instances 可通过重跑恢复。D022: 准备重跑脚本中，等 Director 确认后执行。\"}}, \"count\": 5, \"total\": 30, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.0987}}"
    }
  },
  "sourceToolAssistantUUID": "c9a1697b-ffe2-4eab-8bba-fcc5e6c4b8b4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "b1d97499-4652-4822-8fc5-dbdc566ceedc",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 51 · 2026-05-14T21:32:55.715Z_

<details><summary>Logged reasoning block</summary>

```text
The plan_017_literature entry has no notes field. The hypothesis says: "8 papers surveyed (CodexGraph, LocAgent, RANGER, GraphCoder, ARISE, RepoGraph, CodeGRAG, CodeRAG)".

Now I have all the information I need:

**Problem 1: RepoGraph + GraphCoder missing from literature_map.yaml**
- Both confirmed real via WebSearch:
  - RepoGraph: "RepoGraph: Enhancing AI Software Engineering with Repository-level Code Graph" by Siru Ouyang, Wenhao Yu, Kaixin Ma, et al. ICLR 2025.
  - GraphCoder: "GraphCoder: Enhancing Repository-Level Code Completion via Coarse-to-fine Retrieval Based on Code Context Graph" by Wei Liu, Ailun Yu, Daoguang Zan, et al. ASE 2024.
- Both need to be added to literature_map.yaml under the graph_guided_inference category.

**Problem 2: ARISE year inconsistency**
- arXiv ID 2605.03117 was posted in May 2026, but literature_map.yaml lists it as 2025, which is incorrect.
- The discussion_v2.md correctly shows it as 2026 (Seddik & Fard, 2026).
- I need to update literature_map.yaml to reflect the correct year.

**Problem 3: CodeGRAG and CodeRAG missing**
- The hypothesis mentions 8 surveyed papers including CodeGRAG and CodeRAG, but they're absent from both literature_map.yaml and discussion_v2.md.
- I should add an exclusion reason to the plan_017_literature notes field.

Now I'm going to make these updates. I have the full literature_map.yaml content, so I can prepare the edits for problems 1 and 2. For problem 1, I need to add RepoGraph and GraphCoder entries to the graph_guided_inference category.

For problem 2, I'll update ARISE's year from 2025 to 2026.

For problem 3, I need to search for information about CodeGRAG and CodeRAG first so I can write an accurate exclusion reason in the notes.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "33ada081-c7c7-42b7-ba75-02c317085787",
  "isSidechain": false,
  "requestId": "req_011Cb3BDDpvdXvwVaFSXrCJM",
  "type": "assistant",
  "uuid": "a332bffa-26b8-446d-904f-ad2f8aa81a14",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "b1d97499-4652-4822-8fc5-dbdc566ceedc",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WrcsEMVeMJshwQDGoRDFts",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1658,
      "cache_read_input_tokens": 47207,
      "output_tokens": 729,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1658,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 729,
          "cache_read_input_tokens": 47207,
          "cache_creation_input_tokens": 1658,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1658
          },
          "type": "message"
        }
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

_source line 52 · 2026-05-14T21:32:55.716Z_

Now searching for CodeGRAG and CodeRAG to understand the exclusion reasoning.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a332bffa-26b8-446d-904f-ad2f8aa81a14",
  "isSidechain": false,
  "requestId": "req_011Cb3BDDpvdXvwVaFSXrCJM",
  "type": "assistant",
  "uuid": "4faf3d1b-7641-4587-a473-51dd224a9ca5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "b1d97499-4652-4822-8fc5-dbdc566ceedc",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WrcsEMVeMJshwQDGoRDFts",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1658,
      "cache_read_input_tokens": 47207,
      "output_tokens": 729,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1658,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 729,
          "cache_read_input_tokens": 47207,
          "cache_creation_input_tokens": 1658,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1658
          },
          "type": "message"
        }
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

_source line 53 · 2026-05-14T21:32:55.838Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01QwsQr2qqm9QjRSTgCKvBbM`</summary>

```json
{
  "query": "CodeGRAG \"graph-augmented\" code retrieval paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4faf3d1b-7641-4587-a473-51dd224a9ca5",
  "isSidechain": false,
  "requestId": "req_011Cb3BDDpvdXvwVaFSXrCJM",
  "type": "assistant",
  "uuid": "d701f33e-f69a-4d8a-ac5c-828f28460724",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "b1d97499-4652-4822-8fc5-dbdc566ceedc",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WrcsEMVeMJshwQDGoRDFts",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1658,
      "cache_read_input_tokens": 47207,
      "output_tokens": 729,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1658,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 729,
          "cache_read_input_tokens": 47207,
          "cache_creation_input_tokens": 1658,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1658
          },
          "type": "message"
        }
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

_source line 54 · 2026-05-14T21:32:55.895Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Ks1HBc1PsJ8dZyJiWVGcwy`</summary>

```json
{
  "query": "CodeRAG code retrieval augmented generation paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d701f33e-f69a-4d8a-ac5c-828f28460724",
  "isSidechain": false,
  "requestId": "req_011Cb3BDDpvdXvwVaFSXrCJM",
  "type": "assistant",
  "uuid": "d15bb6a2-f71c-434d-a2a2-7ed3bbdfa9e1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "b1d97499-4652-4822-8fc5-dbdc566ceedc",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WrcsEMVeMJshwQDGoRDFts",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1658,
      "cache_read_input_tokens": 47207,
      "output_tokens": 729,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1658,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 729,
          "cache_read_input_tokens": 47207,
          "cache_creation_input_tokens": 1658,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1658
          },
          "type": "message"
        }
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

_source line 55 · 2026-05-14T21:33:00.909Z_

<details><summary>↩ Tool result · `toolu_01QwsQr2qqm9QjRSTgCKvBbM`</summary>

```text
Web search results for query: "CodeGRAG "graph-augmented" code retrieval paper"

Links: [{"title":"CodeGRAG: Extracting Composed Syntax Graphs for Retrieval Augmented Cross-Lingual Code Generation","url":"https://arxiv.org/html/2405.02355v1"},{"title":"CodeGRAG: Bridging the Gap between Natural Language and Programming Language via Graphical Retrieval Augmented Generation","url":"https://arxiv.org/html/2405.02355"},{"title":"[2405.02355] CodeGRAG: Bridging the Gap between Natural Language and Programming Language via Graphical Retrieval Augmented Generation","url":"https://arxiv.org/abs/2405.02355"},{"title":"[2405.02355v1] CodeGRAG: Extracting Composed Syntax Graphs for Retrieval Augmented Cross-Lingual Code Generation","url":"https://arxiv.org/abs/2405.02355v1"},{"title":"CodeGRAG: Extracting Composed Syntax Graphs for Retrieval Augmented Cross-Lingual Code Generation | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/codegrag-bridging-gap-between-natural-language-programming"},{"title":"CodeRAG: Supportive Code Retrieval on Bigraph for Real-World Code Generation","url":"https://arxiv.org/html/2504.10046v1"},{"title":"GitHub - DEEP-PolyU/Awesome-GraphRAG: Awesome-GraphRAG: A curated list of resources (surveys, papers, benchmarks, and opensource projects) on graph-based retrieval-augmented generation. · GitHub","url":"https://github.com/DEEP-PolyU/Awesome-GraphRAG"},{"title":"[2405.02355v3] CodeGRAG: Bridging the Gap between Natural Language and Programming Language via Graphical Retrieval Augmented Generation","url":"https://arxiv.org/abs/2405.02355v3"},{"title":"CodeGRAG: Bridging the Gap between Natural Language and Programming Language via Graphical Retrieval Augmented Generation - Paper Detail","url":"https://deeplearn.org/arxiv/547019/codegrag:-bridging-the-gap-between-natural-language-and-programming-language-via-graphical-retrieval-augmented-generation"},{"title":"Context-Augmented Code Generation Using Programming Knowledge Graphs | OpenReview","url":"https://openreview.net/forum?id=EHfn5fbFHw"}]

I found the CodeGRAG paper! Here are the key findings from the search results:

## Overview

CodeGRAG is a Graphical Retrieval Augmented Code Generation framework that bridges the gap between natural language (NL) and programming language (PL) to enhance the performance of LLMs.

## Main Approach

CodeGRAG builds the graphical view of code blocks based on the control flow and data flow of them to better interpret the programming domain knowledge, which can facilitate natural language based LLMs for better understanding of code syntax and serve as a bridge among different programming languages.

## Technical Components

The paper proposes 1) a hard meta-graph prompt template to transform the challenging syntax graph into informative graphical view for tuning-free models and 2) a soft prompting technique that injects the domain knowledge of programming languages into model parameters via finetuning the models with the soft signals encoded by GNN expert model.

## Results

CodeGRAG significantly improves the code generation ability of LLMs and can even offer performance gain for cross-lingual code generation.

The paper was initially published in May 2024 and has been updated multiple times through May 2025. The research addresses the challenge of syntactic gaps and vocabulary mismatches between natural language and programming languages when using LLMs for code generation.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d701f33e-f69a-4d8a-ac5c-828f28460724",
  "isSidechain": false,
  "promptId": "255fffc4-c17f-4b3b-8b5c-7a3031fdb918",
  "type": "user",
  "uuid": "7f528ac0-b0ab-4045-832e-6a857eb4f12e",
  "toolUseResult": {
    "query": "CodeGRAG \"graph-augmented\" code retrieval paper",
    "results": [
      {
        "tool_use_id": "srvtoolu_01CrdGjkdyT4HQMTNEBaYHZr",
        "content": [
          {
            "title": "CodeGRAG: Extracting Composed Syntax Graphs for Retrieval Augmented Cross-Lingual Code Generation",
            "url": "https://arxiv.org/html/2405.02355v1"
          },
          {
            "title": "CodeGRAG: Bridging the Gap between Natural Language and Programming Language via Graphical Retrieval Augmented Generation",
            "url": "https://arxiv.org/html/2405.02355"
          },
          {
            "title": "[2405.02355] CodeGRAG: Bridging the Gap between Natural Language and Programming Language via Graphical Retrieval Augmented Generation",
            "url": "https://arxiv.org/abs/2405.02355"
          },
          {
            "title": "[2405.02355v1] CodeGRAG: Extracting Composed Syntax Graphs for Retrieval Augmented Cross-Lingual Code Generation",
            "url": "https://arxiv.org/abs/2405.02355v1"
          },
          {
            "title": "CodeGRAG: Extracting Composed Syntax Graphs for Retrieval Augmented Cross-Lingual Code Generation | AI Research Paper Details",
            "url": "https://www.aimodels.fyi/papers/arxiv/codegrag-bridging-gap-between-natural-language-programming"
          },
          {
            "title": "CodeRAG: Supportive Code Retrieval on Bigraph for Real-World Code Generation",
            "url": "https://arxiv.org/html/2504.10046v1"
          },
          {
            "title": "GitHub - DEEP-PolyU/Awesome-GraphRAG: Awesome-GraphRAG: A curated list of resources (surveys, papers, benchmarks, and opensource projects) on graph-based retrieval-augmented generation. · GitHub",
            "url": "https://github.com/DEEP-PolyU/Awesome-GraphRAG"
          },
          {
            "title": "[2405.02355v3] CodeGRAG: Bridging the Gap between Natural Language and Programming Language via Graphical Retrieval Augmented Generation",
            "url": "https://arxiv.org/abs/2405.02355v3"
          },
          {
            "title": "CodeGRAG: Bridging the Gap between Natural Language and Programming Language via Graphical Retrieval Augmented Generation - Paper Detail",
            "url": "https://deeplearn.org/arxiv/547019/codegrag:-bridging-the-gap-between-natural-language-and-programming-language-via-graphical-retrieval-augmented-generation"
          },
          {
            "title": "Context-Augmented Code Generation Using Programming Knowledge Graphs | OpenReview",
            "url": "https://openreview.net/forum?id=EHfn5fbFHw"
          }
        ]
      },
      "I found the CodeGRAG paper! Here are the key findings from the search results:\n\n## Overview\n\nCodeGRAG is a Graphical Retrieval Augmented Code Generation framework that bridges the gap between natural language (NL) and programming language (PL) to enhance the performance of LLMs.\n\n## Main Approach\n\nCodeGRAG builds the graphical view of code blocks based on the control flow and data flow of them to better interpret the programming domain knowledge, which can facilitate natural language based LLMs for better understanding of code syntax and serve as a bridge among different programming languages.\n\n## Technical Components\n\nThe paper proposes 1) a hard meta-graph prompt template to transform the challenging syntax graph into informative graphical view for tuning-free models and 2) a soft prompting technique that injects the domain knowledge of programming languages into model parameters via finetuning the models with the soft signals encoded by GNN expert model.\n\n## Results\n\nCodeGRAG significantly improves the code generation ability of LLMs and can even offer performance gain for cross-lingual code generation.\n\nThe paper was initially published in May 2024 and has been updated multiple times through May 2025. The research addresses the challenge of syntactic gaps and vocabulary mismatches between natural language and programming languages when using LLMs for code generation."
    ],
    "durationSeconds": 5.067236690999998
  },
  "sourceToolAssistantUUID": "d701f33e-f69a-4d8a-ac5c-828f28460724",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "b1d97499-4652-4822-8fc5-dbdc566ceedc",
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
  "leafUuid": "7f528ac0-b0ab-4045-832e-6a857eb4f12e",
  "sessionId": "b1d97499-4652-4822-8fc5-dbdc566ceedc"
}
```

---

### Runtime record

_source line 57_

```json
{
  "type": "ai-title",
  "aiTitle": "Fix literature reference consistency issues",
  "sessionId": "b1d97499-4652-4822-8fc5-dbdc566ceedc"
}
```

---

### Tool result

_source line 58 · 2026-05-14T21:33:04.159Z_

<details><summary>↩ Tool result · `toolu_01Ks1HBc1PsJ8dZyJiWVGcwy`</summary>

```text
Web search results for query: "CodeRAG code retrieval augmented generation paper"

Links: [{"title":"[2406.14497] CodeRAG-Bench: Can Retrieval Augment Code Generation?","url":"https://arxiv.org/abs/2406.14497"},{"title":"CodeRAG-Bench: Can Retrieval Augment Code Generation?","url":"https://code-rag-bench.github.io/"},{"title":"CodeRAG: Supportive Code Retrieval on Bigraph for Real-World Code Generation","url":"https://arxiv.org/html/2504.10046v1"},{"title":"CodeRAG-Bench: Can Retrieval Augment Code Generation?","url":"https://arxiv.org/html/2406.14497v1"},{"title":"[2510.04905] Retrieval-Augmented Code Generation: A Survey with Focus on Repository-Level Approaches","url":"https://arxiv.org/abs/2510.04905"},{"title":"[2406.14497v1] CodeRAG-Bench: Can Retrieval Augment Code Generation?","url":"https://arxiv.org/abs/2406.14497v1"},{"title":"[2504.10046v1] CodeRAG: Supportive Code Retrieval on Bigraph for Real-World Code Generation","url":"https://arxiv.org/abs/2504.10046v1"},{"title":"CodeRAG: Supportive Code Retrieval on Bigraph for Real-World Code Generation | Request PDF","url":"https://www.researchgate.net/publication/390772757_CodeRAG_Supportive_Code_Retrieval_on_Bigraph_for_Real-World_Code_Generation"},{"title":"CodeRAG: Finding Relevant and Necessary Knowledge for Retrieval-Augmented Repository-Level Code Completion","url":"https://arxiv.org/html/2509.16112v1"},{"title":"Context-Augmented Code Generation Using Programming Knowledge Graphs | OpenReview","url":"https://openreview.net/forum?id=EHfn5fbFHw"}]

Based on the search results, I found several papers related to CodeRAG and code retrieval-augmented generation:

## Main Papers Found:

### 1. CodeRAG-Bench: Can Retrieval Augment Code Generation?
This paper by Zora Zhiruo Wang and colleagues curates a comprehensive evaluation benchmark called CodeRAG-Bench, encompassing three categories of code generation tasks, including basic programming, open-domain, and repository-level problems. The work shows that providing external contexts such as library documentation can facilitate generating accurate and functional code. The benchmark aggregates documents from five sources for models to retrieve contexts: competition solutions, online tutorials, library documentation, StackOverflow posts, and GitHub repositories. The paper was published on June 20, 2024.

### 2. CodeRAG: Supportive Code Retrieval on Bigraph for Real-World Code Generation
This paper proposes CodeRAG, a retrieval-augmented code generation framework to comprehensively retrieve supportive codes for real-world code generation. CodeRAG constructs a requirement graph for the current repository and retrieves relevant requirement nodes of the target requirement node, while also modeling a DS-code graph and mapping relevant requirement nodes into their corresponding code nodes. Experiments show that CodeRAG achieves significant improvements (increasing 40.90 and 37.79 Pass@1 on GPT-4o and Gemini-Pro on DevEval) compared to no RAG scenarios.

### 3. CodeRAG: Finding Relevant and Necessary Knowledge for Retrieval-Augmented Repository-Level Code Completion
This paper introduces CodeRAG, a framework tailored to identify relevant and necessary knowledge for retrieval-augmented repository-level code completion, with core components including log probability guided query construction, multi-path code retrieval, and preference-aligned BestFit reranking.

All three papers address the application of retrieval-augmented generation techniques to improve code generation tasks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d15bb6a2-f71c-434d-a2a2-7ed3bbdfa9e1",
  "isSidechain": false,
  "promptId": "255fffc4-c17f-4b3b-8b5c-7a3031fdb918",
  "type": "user",
  "uuid": "ae40d76d-0d6f-4223-bd34-d73c703dbb74",
  "toolUseResult": {
    "query": "CodeRAG code retrieval augmented generation paper",
    "results": [
      {
        "tool_use_id": "srvtoolu_01NTVSRmrcf8ye3pDgmbTBmn",
        "content": [
          {
            "title": "[2406.14497] CodeRAG-Bench: Can Retrieval Augment Code Generation?",
            "url": "https://arxiv.org/abs/2406.14497"
          },
          {
            "title": "CodeRAG-Bench: Can Retrieval Augment Code Generation?",
            "url": "https://code-rag-bench.github.io/"
          },
          {
            "title": "CodeRAG: Supportive Code Retrieval on Bigraph for Real-World Code Generation",
            "url": "https://arxiv.org/html/2504.10046v1"
          },
          {
            "title": "CodeRAG-Bench: Can Retrieval Augment Code Generation?",
            "url": "https://arxiv.org/html/2406.14497v1"
          },
          {
            "title": "[2510.04905] Retrieval-Augmented Code Generation: A Survey with Focus on Repository-Level Approaches",
            "url": "https://arxiv.org/abs/2510.04905"
          },
          {
            "title": "[2406.14497v1] CodeRAG-Bench: Can Retrieval Augment Code Generation?",
            "url": "https://arxiv.org/abs/2406.14497v1"
          },
          {
            "title": "[2504.10046v1] CodeRAG: Supportive Code Retrieval on Bigraph for Real-World Code Generation",
            "url": "https://arxiv.org/abs/2504.10046v1"
          },
          {
            "title": "CodeRAG: Supportive Code Retrieval on Bigraph for Real-World Code Generation | Request PDF",
            "url": "https://www.researchgate.net/publication/390772757_CodeRAG_Supportive_Code_Retrieval_on_Bigraph_for_Real-World_Code_Generation"
          },
          {
            "title": "CodeRAG: Finding Relevant and Necessary Knowledge for Retrieval-Augmented Repository-Level Code Completion",
            "url": "https://arxiv.org/html/2509.16112v1"
          },
          {
            "title": "Context-Augmented Code Generation Using Programming Knowledge Graphs | OpenReview",
            "url": "https://openreview.net/forum?id=EHfn5fbFHw"
          }
        ]
      },
      "Based on the search results, I found several papers related to CodeRAG and code retrieval-augmented generation:\n\n## Main Papers Found:\n\n### 1. CodeRAG-Bench: Can Retrieval Augment Code Generation?\nThis paper by Zora Zhiruo Wang and colleagues curates a comprehensive evaluation benchmark called CodeRAG-Bench, encompassing three categories of code generation tasks, including basic programming, open-domain, and repository-level problems. The work shows that providing external contexts such as library documentation can facilitate generating accurate and functional code. The benchmark aggregates documents from five sources for models to retrieve contexts: competition solutions, online tutorials, library documentation, StackOverflow posts, and GitHub repositories. The paper was published on June 20, 2024.\n\n### 2. CodeRAG: Supportive Code Retrieval on Bigraph for Real-World Code Generation\nThis paper proposes CodeRAG, a retrieval-augmented code generation framework to comprehensively retrieve supportive codes for real-world code generation. CodeRAG constructs a requirement graph for the current repository and retrieves relevant requirement nodes of the target requirement node, while also modeling a DS-code graph and mapping relevant requirement nodes into their corresponding code nodes. Experiments show that CodeRAG achieves significant improvements (increasing 40.90 and 37.79 Pass@1 on GPT-4o and Gemini-Pro on DevEval) compared to no RAG scenarios.\n\n### 3. CodeRAG: Finding Relevant and Necessary Knowledge for Retrieval-Augmented Repository-Level Code Completion\nThis paper introduces CodeRAG, a framework tailored to identify relevant and necessary knowledge for retrieval-augmented repository-level code completion, with core components including log probability guided query construction, multi-path code retrieval, and preference-aligned BestFit reranking.\n\nAll three papers address the application of retrieval-augmented generation techniques to improve code generation tasks."
    ],
    "durationSeconds": 8.261320995000002
  },
  "sourceToolAssistantUUID": "d15bb6a2-f71c-434d-a2a2-7ed3bbdfa9e1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "b1d97499-4652-4822-8fc5-dbdc566ceedc",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 59 · 2026-05-14T21:33:18.556Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have a clear understanding of CodeGRAG and CodeRAG:

- **CodeGRAG** (arXiv 2405.02355): "Bridging the Gap between Natural Language and Programming Language via Graphical Retrieval Augmented Generation" - focuses on NL→code generation using graph representations (control flow + data flow) as prompts for LLMs. This is about code generation, not code retrieval for bug fixing. Not within StructFuse's scope.

- **CodeRAG**: There are multiple papers with this name:
  - CodeRAG-Bench (2406.14497): Benchmark for RAG code generation
  - CodeRAG (2504.10046): Supportive code retrieval on bigraph for code generation
  - CodeRAG (2509.16112): Repository-level code completion

All of these papers are centered on retrieval-augmented code generation rather than contrastive learning for code retrieval in bug-fixing contexts, so they fall outside StructFuse's scope.

Now I'm planning the updates I need to make: adding RepoGraph and GraphCoder to the graph_guided_inference category in literature_map.yaml, correcting ARISE's year from 2025 to 2026, and documenting the CodeGRAG and CodeRAG exclusion reasoning in the plan notes. I need to carefully handle the literature_map.yaml file since it's quite large, so I'll need to work through the edits methodically.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ae40d76d-0d6f-4223-bd34-d73c703dbb74",
  "isSidechain": false,
  "requestId": "req_011Cb3BF14XTvYTPknE1C4y7",
  "type": "assistant",
  "uuid": "41d1835b-c399-4f78-93f9-42a3757e7d99",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "b1d97499-4652-4822-8fc5-dbdc566ceedc",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LwTkpX6cabb3TiVxSaboBt",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2689,
      "cache_read_input_tokens": 48865,
      "output_tokens": 684,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2689,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 684,
          "cache_read_input_tokens": 48865,
          "cache_creation_input_tokens": 2689,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2689
          },
          "type": "message"
        }
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

_source line 60 · 2026-05-14T21:33:18.557Z_

Now I have all information. Let me read the literature_map.yaml file directly for editing, then make all changes in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "41d1835b-c399-4f78-93f9-42a3757e7d99",
  "isSidechain": false,
  "requestId": "req_011Cb3BF14XTvYTPknE1C4y7",
  "type": "assistant",
  "uuid": "2a29d26c-8983-42c8-bb6f-a420cfac8075",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "b1d97499-4652-4822-8fc5-dbdc566ceedc",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LwTkpX6cabb3TiVxSaboBt",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2689,
      "cache_read_input_tokens": 48865,
      "output_tokens": 684,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2689,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 684,
          "cache_read_input_tokens": 48865,
          "cache_creation_input_tokens": 2689,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2689
          },
          "type": "message"
        }
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

_source line 61 · 2026-05-14T21:33:18.966Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Jn3yPqHRnK7ranviuZSjnH`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/literature_map.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2a29d26c-8983-42c8-bb6f-a420cfac8075",
  "isSidechain": false,
  "requestId": "req_011Cb3BF14XTvYTPknE1C4y7",
  "type": "assistant",
  "uuid": "43266bf1-9c14-4256-9af6-1f459f0ece7b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "b1d97499-4652-4822-8fc5-dbdc566ceedc",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LwTkpX6cabb3TiVxSaboBt",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2689,
      "cache_read_input_tokens": 48865,
      "output_tokens": 684,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2689,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 684,
          "cache_read_input_tokens": 48865,
          "cache_creation_input_tokens": 2689,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2689
          },
          "type": "message"
        }
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

_source line 62 · 2026-05-14T21:33:18.973Z_

<details><summary>↩ Tool result · `toolu_01Jn3yPqHRnK7ranviuZSjnH`</summary>

```text
1	# StructFuse — Related Work Literature Map
2	# 最后更新: 2026-05-14
3	# 说明: 只收录已验证存在的论文。每篇均经 WebSearch 确认标题/venue/year。
4	# 总计: 37 entries (含 2 个软件工具引用)
5	
6	categories:
7	
8	  # ==========================================================================
9	  # Category 1: Code Retrieval for Bug Fixing / SWE-bench Ecosystem
10	  # ==========================================================================
11	  code_retrieval_bug_fixing:
12	    description: "SWE-bench 及相关 repo-level 自动修复系统中的代码检索方法"
13	    papers:
14	
15	      - title: "SWE-bench: Can Language Models Resolve Real-World GitHub Issues?"
16	        authors: "Carlos E. Jimenez, John Yang, Alexander Wettig, Shunyu Yao, Kexin Pei, Ofir Press, Karthik Narasimhan"
17	        venue: ICLR
18	        year: 2024
19	        relation: baseline
20	        summary: "从 GitHub issues 构建 repo-level bug fixing benchmark，成为自动修复领域标准评估集。"
21	
22	      - title: "SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering"
23	        authors: "John Yang, Carlos E. Jimenez, Alexander Wettig, Kilian Lieret, Shunyu Yao, Karthik Narasimhan, Ofir Press"
24	        venue: NeurIPS
25	        year: 2024
26	        relation: competitor
27	        summary: "基于 LLM agent 的交互式 bug fixing 系统，定义了 ACI 接口范式。"
28	
29	      - title: "AutoCodeRover: Autonomous Program Improvement"
30	        authors: "Yuntong Zhang, Haifeng Ruan, Zhiyu Fan, Abhik Roychoudhury"
31	        venue: ISSTA
32	        year: 2024
33	        relation: competitor
34	        summary: "结合代码搜索与 spectrum-based fault localization，利用程序分析缩小修复范围。"
35	
36	      - title: "Agentless: Demystifying LLM-based Software Engineering Agents"
37	        authors: "Chunqiu Steven Xia, Yinlin Deng, Soren Dunn, Lingming Zhang"
38	        venue: arXiv
39	        year: 2024
40	        relation: competitor
41	        summary: "无 agent 架构的 two-phase localize-then-repair 方法，在 SWE-bench 上取得强 baseline。"
42	
43	      - title: "SWE-smith: Scaling Data for Software Engineering Agents"
44	        authors: "John Yang, Kilian Lieret, Carlos E. Jimenez, Alexander Wettig, Kabir Khandpur, Yanzhe Zhang, Binyuan Hui, Ofir Press, Ludwig Schmidt, Diyi Yang"
45	        venue: "NeurIPS (Datasets & Benchmarks, Spotlight)"
46	        year: 2025
47	        relation: building-block
48	        summary: "自动从 GitHub 生成大规模 SWE-bench 风格训练数据，StructFuse 用其 repos 做 data-flow 提取。"
49	
50	      - title: "RepoBench: Benchmarking Repository-Level Code Auto-Completion Systems"
51	        authors: "Tianyang Liu, Canwen Xu, Julian McAuley"
52	        venue: ICLR
53	        year: 2024
54	        relation: baseline
55	        summary: "Repo-level 代码补全/检索 benchmark，含 RepoBench-R 检索子任务。"
56	
57	      - title: "SweRank: Software Issue Localization with Code Ranking"
58	        authors: "Revanth Gangi Reddy, Tarun Suresh, JaeHyeok Doo, Ye Liu, Xuan Phi Nguyen, Yingbo Zhou, Semih Yavuz, Caiming Xiong, Heng Ji, Shafiq Joty"
59	        venue: arXiv
60	        year: 2025
61	        relation: competitor
62	        summary: "Retrieve-and-rerank 框架用于 software issue localization，在 SWE-Bench-Lite 和 LocBench 上 SOTA，text-based retrieval baseline。"
63	
64	      - title: "SWE-Fixer: Training Open-Source LLMs for Effective and Efficient GitHub Issue Resolution"
65	        authors: "Chengxing Xie, Bowen Li, Chang Gao, He Du, Wai Lam, Difan Zou, Kai Chen"
66	        venue: "ACL (Findings)"
67	        year: 2025
68	        relation: competitor
69	        summary: "BM25 + LLM retriever 的 coarse-to-fine file retrieval pipeline，在 SWE-Bench Verified 上 30.2%。"
70	
71	  # ==========================================================================
72	  # Category 2: Hard Negative Mining in Contrastive Learning
73	  # ==========================================================================
74	  hard_negative_mining:
75	    description: "对比学习中 hard negative 挖掘策略，以及密集检索中的负样本选择"
76	    papers:
77	
78	      - title: "Dense Passage Retrieval for Open-Domain Question Answering"
79	        authors: "Vladimir Karpukhin, Barlas Oguz, Sewon Min, Patrick Lewis, Ledell Wu, Sergey Edunov, Danqi Chen, Wen-tau Yih"
80	        venue: EMNLP
81	        year: 2020
82	        relation: background
83	        summary: "DPR 开创了 in-batch negatives + BM25 hard negatives 的双塔检索范式。"
84	
85	      - title: "Approximate Nearest Neighbor Negative Contrastive Learning for Dense Text Retrieval"
86	        authors: "Lee Xiong, Chenyan Xiong, Ye Li, Kwok-Fung Tang, Jialin Liu, Paul Bennett, Junaid Ahmed, Arnold Overwijk"
87	        venue: ICLR
88	        year: 2021
89	        relation: background
90	        summary: "ANCE 用 ANN index 动态挖掘 embedding-distance hard negatives，StructFuse 的 baseline negative 策略之一。"
91	
92	      - title: "A Simple Framework for Contrastive Learning of Visual Representations"
93	        authors: "Ting Chen, Simon Kornblith, Mohammad Norouzi, Geoffrey Hinton"
94	        venue: ICML
95	        year: 2020
96	        relation: background
97	        summary: "SimCLR 视觉对比学习奠基工作，证明 hard negatives 和大 batch size 对对比学习的重要性。"
98	
99	      - title: "Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks"
100	        authors: "Nils Reimers, Iryna Gurevych"
101	        venue: EMNLP
102	        year: 2019
103	        relation: background
104	        summary: "Siamese/triplet 网络训练句子嵌入，StructFuse 的对比训练框架与其类似。"
105	
106	      - title: "Curriculum Learning for Dense Retrieval Distillation"
107	        authors: "Hansi Zeng, Hamed Zamani, Vishwa Vinay"
108	        venue: "SIGIR (Best Short Paper)"
109	        year: 2022
110	        relation: background
111	        summary: "CL-DRD: 课程学习式知识蒸馏用于密集检索，从粗粒度到细粒度逐步增加训练难度。"
112	
113	      - title: "Effective Hard Negative Mining for Contrastive Learning-Based Code Search"
114	        authors: "Fan Y., Li C., Ge J., Huang L., Luo B."
115	        venue: "ACM TOSEM"
116	        year: 2025
117	        relation: contrast-target
118	        summary: "CoCoHaNeRe: 提出可微分 hard negative 机制用于代码搜索对比学习。其对 hard negative 机制的处理与 StructFuse 的发现形成关键对照——StructFuse 证明 true embedding-distance mining 即可持续提升性能。"
119	        note: "关键引用：StructFuse Claim 1 的 correction target。CoCoHaNeRe 论点是非可微 embedding negatives 学习'slow and ineffective'，StructFuse 证明用 true embedding distance mining 仍然有效。"
120	
121	  # ==========================================================================
122	  # Category 3: Contrastive Learning for Code
123	  # ==========================================================================
124	  contrastive_code_learning:
125	    description: "代码领域的对比学习方法，训练时利用代码特性构建正负样本"
126	    papers:
127	
128	      - title: "Contrastive Code Representation Learning"
129	        authors: "Paras Jain, Ajay Jain, Tianjun Zhang, Pieter Abbeel, Joseph Gonzalez, Ion Stoica"
130	        venue: EMNLP
131	        year: 2021
132	        relation: background
133	        summary: "ContraCode: 自监督对比预训练，通过编译器变换生成功能等价的程序变体，学习代码功能而非表面形式。"
134	
135	      - title: "CodeRetriever: A Large Scale Contrastive Pre-Training Method for Code Search"
136	        authors: "Xiaonan Li, Yeyun Gong, Yelong Shen, Xipeng Qiu, Hang Zhang, Bolun Yao, Weizhen Qi, Daxin Jiang, Weizhu Chen, Nan Duan"
137	        venue: EMNLP
138	        year: 2022
139	        relation: background
140	        summary: "结合 unimodal (code-code) 和 bimodal (code-text) 对比学习预训练代码表示，在 11 个代码搜索 benchmark 上 SOTA。"
141	
142	      - title: "Towards Learning (Dis)-Similarity of Source Code from Program Contrasts"
143	        authors: "Yangruibo Ding, Luca Buratti, Saurabh Pujar, Alessandro Morari, Baishakhi Ray, Saikat Chakraborty"
144	        venue: "ACL (Long Papers)"
145	        year: 2022
146	        relation: background
147	        summary: "利用程序结构和功能属性构建对比样本对，学习代码相似性/差异性表示。"
148	
149	  # ==========================================================================
150	  # Category 4: Program Analysis for ML
151	  # ==========================================================================
152	  program_analysis_for_ml:
153	    description: "静态分析辅助 ML，结构信息在代码表示学习中的应用"
154	    papers:
155	
156	      - title: "CodeQL: Semantic Code Analysis Engine"
157	        authors: "GitHub / Semmle"
158	        venue: "Tool (open-source)"
159	        year: 2019
160	        relation: building-block
161	        summary: "基于 Datalog 的代码查询引擎，支持 inter-procedural data-flow 分析。StructFuse 用它提取 scope-bounded data-flow graph。"
162	
163	      - title: "code2vec: Learning Distributed Representations of Code"
164	        authors: "Uri Alon, Meital Zilberstein, Omer Levy, Eran Yahav"
165	        venue: POPL
166	        year: 2019
167	        relation: background
168	        summary: "用 AST path 学习代码向量表示，首次大规模证明结构信息对代码表示学习的价值。"
169	
170	      - title: "code2seq: Generating Sequences from Structured Representations of Code"
171	        authors: "Uri Alon, Shaked Brody, Omer Levy, Eran Yahav"
172	        venue: ICLR
173	        year: 2019
174	        relation: background
175	        summary: "code2vec 的序列生成扩展，用 AST path attention 生成方法名摘要。"
176	
177	      - title: "Detecting Code Clones with Graph Neural Network and Flow-Augmented Abstract Syntax Tree"
178	        authors: "Wenhan Wang, Ge Li, Bo Ma, Xin Xia, Zhi Jin"
179	        venue: SANER
180	        year: 2020
181	        relation: background
182	        summary: "FA-AST: 用 data-flow 增强 AST 进行代码克隆检测，与 StructFuse 用 data-flow 做 hard negative 挖掘思路相关。"
183	
184	      - title: "GraphCodeBERT: Pre-training Code Representations with Data Flow"
185	        authors: "Daya Guo, Shuo Ren, Shuai Lu, Zhangyin Feng, Duyu Tang, Shujie Liu, Long Zhou, Nan Duan, Alexey Svyatkovskiy, Shengyu Fu, Michele Tufano, Shao Kun Deng, Colin Clement, Dawn Drain, Neel Sundaresan, Jian Yin, Daxin Jiang, Ming Zhou"
186	        venue: ICLR
187	        year: 2021
188	        relation: background
189	        summary: "在预训练中引入 data-flow edge，证明 data-flow 信息提升代码理解任务。StructFuse 的 insight 与此相关但用途不同（hard negative mining vs pre-training）。"
190	
191	      - title: "ARISE: A Repository-level Graph Representation and Toolset for Agentic Fault Localization and Program Repair"
192	        authors: "Shahd Seddik, Fatemeh Fard"
193	        venue: arXiv
194	        year: 2025
195	        relation: contrast
196	        summary: "用 multi-granularity program graph（含 intra-procedural def-use edges）辅助 LLM agent 做 fault localization。仅 intra-procedural + runtime tool calls，与 StructFuse 的 inter-procedural static mining 互补。"
197	
198	  # ==========================================================================
199	  # Category 5: Code Embeddings / Code Search
200	  # ==========================================================================
201	  code_embeddings_search:
202	    description: "代码嵌入模型和代码搜索方法"
203	    papers:
204	
205	      - title: "CodeSearchNet Challenge: Evaluating the State of Semantic Code Search"
206	        authors: "Hamel Husain, Ho-Hsiang Wu, Tiferet Gazit, Miltiadis Allamanis, Marc Brockschmidt"
207	        venue: arXiv
208	        year: 2019
209	        relation: background
210	        summary: "代码语义搜索 benchmark 和数据集，推动了代码嵌入模型的发展。"
211	
212	      - title: "CodeBERT: A Pre-Trained Model for Programming and Natural Languages"
213	        authors: "Zhangyin Feng, Daya Guo, Duyu Tang, Nan Duan, Xiaocheng Feng, Ming Gong, Lixin Zou, Bing Qin, Ting Liu, Daxin Jiang, Ming Zhou"
214	        venue: "EMNLP (Findings)"
215	        year: 2020
216	        relation: background
217	        summary: "首个编程语言-自然语言双模态预训练模型，代码嵌入的早期里程碑。"
218	
219	      - title: "UniXcoder: Unified Cross-Modal Pre-training for Code Representation"
220	        authors: "Daya Guo, Shuai Lu, Nan Duan, Yanlin Wang, Ming Zhou, Jian Yin"
221	        venue: ACL
222	        year: 2022
223	        relation: background
224	        summary: "统一跨模态代码预训练，在代码搜索等任务上取得 SOTA。"
225	
226	      - title: "StarCoder: May the Source Be with You!"
227	        authors: "Raymond Li, Loubna Ben Allal, et al. (BigCode)"
228	        venue: TMLR
229	        year: 2023
230	        relation: building-block
231	        summary: "大规模开源代码 LLM，StructFuse 用 StarCoder2-3B 作为对比学习检索器的 backbone 之一。"
232	
233	      - title: "Code Llama: Open Foundation Models for Code"
234	        authors: "Baptiste Roziere, Jonas Gehring, Fabian Gloeckle, et al. (Meta AI)"
235	        venue: arXiv
236	        year: 2023
237	        relation: background
238	        summary: "Meta 的代码大模型系列，基于 Llama 2 微调。"
239	
240	      - title: "Qwen2.5-Coder Technical Report"
241	        authors: "Binyuan Hui, Jian Yang, Zeyu Cui, et al. (Qwen Team, Alibaba)"
242	        venue: arXiv
243	        year: 2024
244	        relation: building-block
245	        summary: "Qwen 代码模型系列，StructFuse 用 Qwen2.5-Coder-3B 作为对比学习检索器的 backbone。"
246	
247	      - title: "DeepSeek-Coder: When the Large Language Model Meets Programming -- The Rise of Code Intelligence"
248	        authors: "Daya Guo, Qihao Zhu, Dejian Yang, Zhenda Xie, Kai Dong, Wentao Zhang, Guanting Chen, Xiao Bi, Yu Wu, Y.K. Li, Fuli Luo, Yingfei Xiong, Wenfeng Liang"
249	        venue: arXiv
250	        year: 2024
251	        relation: background
252	        summary: "开源代码 LLM 系列 (1.3B-33B)，project-level 代码训练 + 16K context + fill-in-the-blank 预训练。"
253	
254	      - title: "RepoFusion: Training Code Models to Understand Your Repository"
255	        authors: "Disha Shrivastava, Denis Kocetkov, Harm de Vries, Dzmitry Bahdanau, Torsten Scholak"
256	        venue: arXiv
257	        year: 2023
258	        relation: background
259	        summary: "训练代码模型融合多个 cross-file repo context 进行代码补全，小模型 + repo context 可匹配大模型性能。"
260	
261	      - title: "BM25"
262	        authors: "Stephen Robertson, Hugo Zaragoza"
263	        venue: "Foundations and Trends in Information Retrieval"
264	        year: 2009
265	        relation: baseline
266	        summary: "经典稀疏检索方法，StructFuse 的 baseline 之一。"
267	
268	  # ==========================================================================
269	  # Category 6: Graph-Guided Code Navigation (Inference-Time)
270	  # ==========================================================================
271	  graph_guided_inference:
272	    description: "推理时利用代码结构图辅助导航/检索的方法（与 StructFuse 的训练时结构信号互补）"
273	    papers:
274	
275	      - title: "LocAgent: Graph-Guided LLM Agents for Code Localization"
276	        authors: "Zhaoling Chen, Robert Tang, Gangda Deng, Fang Wu, Jialong Wu, Zhiwei Jiang, Viktor Prasanna, Arman Cohan, Xingyao Wang"
277	        venue: ACL
278	        year: 2025
279	        relation: contrast
280	        summary: "将代码库解析为有向异构图，LLM agent 通过 multi-hop 推理在图上导航做代码定位。推理时用结构图，StructFuse 训练时用。"
281	
282	      - title: "CodexGraph: Bridging Large Language Models and Code Repositories via Code Graph Databases"
283	        authors: "Xiangyan Liu, Bo Lan, Zhiyuan Hu, Yang Liu, Zhicheng Zhang, Fei Wang, Michael Qizhe Shieh, Wenmeng Zhou"
284	        venue: NAACL
285	        year: 2025
286	        relation: contrast
287	        summary: "将代码库索引到图数据库，LLM agent 通过 graph query 接口检索结构化上下文。"
288	
289	      - title: "RANGER: Repository-Level Agent for Graph-Enhanced Retrieval"
290	        authors: "Pratik Shah, Rajat Ghosh, Aryan Singhal, Debojyoti Dutta"
291	        venue: arXiv
292	        year: 2025
293	        relation: contrast
294	        summary: "构建 repo 知识图（含 variable-level 节点），dual-stage retrieval: Cypher lookup + MCTS-guided graph exploration。"
295	
296	  # ==========================================================================
297	  # Category 7: Infrastructure / Tools
298	  # ==========================================================================
299	  infrastructure:
300	    description: "StructFuse 依赖的核心基础设施和工具"
301	    papers:
302	
303	      - title: "Billion-Scale Similarity Search with GPUs"
304	        authors: "Jeff Johnson, Matthijs Douze, Herve Jegou"
305	        venue: "IEEE Transactions on Big Data"
306	        year: 2021
307	        relation: building-block
308	        summary: "FAISS: GPU 加速的大规模向量相似度搜索库，StructFuse 用于 ANN-based hard negative mining。"
309	
310	      - title: "Tree-sitter: An Incremental Parsing System for Programming Tools"
311	        authors: "Max Brunsfeld et al."
312	        venue: "Software (Zenodo DOI: 10.5281/zenodo.13375512)"
313	        year: 2018
314	        relation: building-block
315	        summary: "增量解析库，高效构建和更新 concrete syntax trees。与 CodeQL 互补用于代码结构提取。"
316	        note: "软件工具，无正式论文。引用 Zenodo DOI 或 GitHub repo。"
317	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "43266bf1-9c14-4256-9af6-1f459f0ece7b",
  "isSidechain": false,
  "promptId": "255fffc4-c17f-4b3b-8b5c-7a3031fdb918",
  "type": "user",
  "uuid": "b501b26c-2ecf-4c71-b8ed-a1815f0c596e",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/literature_map.yaml",
      "content": "# StructFuse — Related Work Literature Map\n# 最后更新: 2026-05-14\n# 说明: 只收录已验证存在的论文。每篇均经 WebSearch 确认标题/venue/year。\n# 总计: 37 entries (含 2 个软件工具引用)\n\ncategories:\n\n  # ==========================================================================\n  # Category 1: Code Retrieval for Bug Fixing / SWE-bench Ecosystem\n  # ==========================================================================\n  code_retrieval_bug_fixing:\n    description: \"SWE-bench 及相关 repo-level 自动修复系统中的代码检索方法\"\n    papers:\n\n      - title: \"SWE-bench: Can Language Models Resolve Real-World GitHub Issues?\"\n        authors: \"Carlos E. Jimenez, John Yang, Alexander Wettig, Shunyu Yao, Kexin Pei, Ofir Press, Karthik Narasimhan\"\n        venue: ICLR\n        year: 2024\n        relation: baseline\n        summary: \"从 GitHub issues 构建 repo-level bug fixing benchmark，成为自动修复领域标准评估集。\"\n\n      - title: \"SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering\"\n        authors: \"John Yang, Carlos E. Jimenez, Alexander Wettig, Kilian Lieret, Shunyu Yao, Karthik Narasimhan, Ofir Press\"\n        venue: NeurIPS\n        year: 2024\n        relation: competitor\n        summary: \"基于 LLM agent 的交互式 bug fixing 系统，定义了 ACI 接口范式。\"\n\n      - title: \"AutoCodeRover: Autonomous Program Improvement\"\n        authors: \"Yuntong Zhang, Haifeng Ruan, Zhiyu Fan, Abhik Roychoudhury\"\n        venue: ISSTA\n        year: 2024\n        relation: competitor\n        summary: \"结合代码搜索与 spectrum-based fault localization，利用程序分析缩小修复范围。\"\n\n      - title: \"Agentless: Demystifying LLM-based Software Engineering Agents\"\n        authors: \"Chunqiu Steven Xia, Yinlin Deng, Soren Dunn, Lingming Zhang\"\n        venue: arXiv\n        year: 2024\n        relation: competitor\n        summary: \"无 agent 架构的 two-phase localize-then-repair 方法，在 SWE-bench 上取得强 baseline。\"\n\n      - title: \"SWE-smith: Scaling Data for Software Engineering Agents\"\n        authors: \"John Yang, Kilian Lieret, Carlos E. Jimenez, Alexander Wettig, Kabir Khandpur, Yanzhe Zhang, Binyuan Hui, Ofir Press, Ludwig Schmidt, Diyi Yang\"\n        venue: \"NeurIPS (Datasets & Benchmarks, Spotlight)\"\n        year: 2025\n        relation: building-block\n        summary: \"自动从 GitHub 生成大规模 SWE-bench 风格训练数据，StructFuse 用其 repos 做 data-flow 提取。\"\n\n      - title: \"RepoBench: Benchmarking Repository-Level Code Auto-Completion Systems\"\n        authors: \"Tianyang Liu, Canwen Xu, Julian McAuley\"\n        venue: ICLR\n        year: 2024\n        relation: baseline\n        summary: \"Repo-level 代码补全/检索 benchmark，含 RepoBench-R 检索子任务。\"\n\n      - title: \"SweRank: Software Issue Localization with Code Ranking\"\n        authors: \"Revanth Gangi Reddy, Tarun Suresh, JaeHyeok Doo, Ye Liu, Xuan Phi Nguyen, Yingbo Zhou, Semih Yavuz, Caiming Xiong, Heng Ji, Shafiq Joty\"\n        venue: arXiv\n        year: 2025\n        relation: competitor\n        summary: \"Retrieve-and-rerank 框架用于 software issue localization，在 SWE-Bench-Lite 和 LocBench 上 SOTA，text-based retrieval baseline。\"\n\n      - title: \"SWE-Fixer: Training Open-Source LLMs for Effective and Efficient GitHub Issue Resolution\"\n        authors: \"Chengxing Xie, Bowen Li, Chang Gao, He Du, Wai Lam, Difan Zou, Kai Chen\"\n        venue: \"ACL (Findings)\"\n        year: 2025\n        relation: competitor\n        summary: \"BM25 + LLM retriever 的 coarse-to-fine file retrieval pipeline，在 SWE-Bench Verified 上 30.2%。\"\n\n  # ==========================================================================\n  # Category 2: Hard Negative Mining in Contrastive Learning\n  # ==========================================================================\n  hard_negative_mining:\n    description: \"对比学习中 hard negative 挖掘策略，以及密集检索中的负样本选择\"\n    papers:\n\n      - title: \"Dense Passage Retrieval for Open-Domain Question Answering\"\n        authors: \"Vladimir Karpukhin, Barlas Oguz, Sewon Min, Patrick Lewis, Ledell Wu, Sergey Edunov, Danqi Chen, Wen-tau Yih\"\n        venue: EMNLP\n        year: 2020\n        relation: background\n        summary: \"DPR 开创了 in-batch negatives + BM25 hard negatives 的双塔检索范式。\"\n\n      - title: \"Approximate Nearest Neighbor Negative Contrastive Learning for Dense Text Retrieval\"\n        authors: \"Lee Xiong, Chenyan Xiong, Ye Li, Kwok-Fung Tang, Jialin Liu, Paul Bennett, Junaid Ahmed, Arnold Overwijk\"\n        venue: ICLR\n        year: 2021\n        relation: background\n        summary: \"ANCE 用 ANN index 动态挖掘 embedding-distance hard negatives，StructFuse 的 baseline negative 策略之一。\"\n\n      - title: \"A Simple Framework for Contrastive Learning of Visual Representations\"\n        authors: \"Ting Chen, Simon Kornblith, Mohammad Norouzi, Geoffrey Hinton\"\n        venue: ICML\n        year: 2020\n        relation: background\n        summary: \"SimCLR 视觉对比学习奠基工作，证明 hard negatives 和大 batch size 对对比学习的重要性。\"\n\n      - title: \"Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks\"\n        authors: \"Nils Reimers, Iryna Gurevych\"\n        venue: EMNLP\n        year: 2019\n        relation: background\n        summary: \"Siamese/triplet 网络训练句子嵌入，StructFuse 的对比训练框架与其类似。\"\n\n      - title: \"Curriculum Learning for Dense Retrieval Distillation\"\n        authors: \"Hansi Zeng, Hamed Zamani, Vishwa Vinay\"\n        venue: \"SIGIR (Best Short Paper)\"\n        year: 2022\n        relation: background\n        summary: \"CL-DRD: 课程学习式知识蒸馏用于密集检索，从粗粒度到细粒度逐步增加训练难度。\"\n\n      - title: \"Effective Hard Negative Mining for Contrastive Learning-Based Code Search\"\n        authors: \"Fan Y., Li C., Ge J., Huang L., Luo B.\"\n        venue: \"ACM TOSEM\"\n        year: 2025\n        relation: contrast-target\n        summary: \"CoCoHaNeRe: 提出可微分 hard negative 机制用于代码搜索对比学习。其对 hard negative 机制的处理与 StructFuse 的发现形成关键对照——StructFuse 证明 true embedding-distance mining 即可持续提升性能。\"\n        note: \"关键引用：StructFuse Claim 1 的 correction target。CoCoHaNeRe 论点是非可微 embedding negatives 学习'slow and ineffective'，StructFuse 证明用 true embedding distance mining 仍然有效。\"\n\n  # ==========================================================================\n  # Category 3: Contrastive Learning for Code\n  # ==========================================================================\n  contrastive_code_learning:\n    description: \"代码领域的对比学习方法，训练时利用代码特性构建正负样本\"\n    papers:\n\n      - title: \"Contrastive Code Representation Learning\"\n        authors: \"Paras Jain, Ajay Jain, Tianjun Zhang, Pieter Abbeel, Joseph Gonzalez, Ion Stoica\"\n        venue: EMNLP\n        year: 2021\n        relation: background\n        summary: \"ContraCode: 自监督对比预训练，通过编译器变换生成功能等价的程序变体，学习代码功能而非表面形式。\"\n\n      - title: \"CodeRetriever: A Large Scale Contrastive Pre-Training Method for Code Search\"\n        authors: \"Xiaonan Li, Yeyun Gong, Yelong Shen, Xipeng Qiu, Hang Zhang, Bolun Yao, Weizhen Qi, Daxin Jiang, Weizhu Chen, Nan Duan\"\n        venue: EMNLP\n        year: 2022\n        relation: background\n        summary: \"结合 unimodal (code-code) 和 bimodal (code-text) 对比学习预训练代码表示，在 11 个代码搜索 benchmark 上 SOTA。\"\n\n      - title: \"Towards Learning (Dis)-Similarity of Source Code from Program Contrasts\"\n        authors: \"Yangruibo Ding, Luca Buratti, Saurabh Pujar, Alessandro Morari, Baishakhi Ray, Saikat Chakraborty\"\n        venue: \"ACL (Long Papers)\"\n        year: 2022\n        relation: background\n        summary: \"利用程序结构和功能属性构建对比样本对，学习代码相似性/差异性表示。\"\n\n  # ==========================================================================\n  # Category 4: Program Analysis for ML\n  # ==========================================================================\n  program_analysis_for_ml:\n    description: \"静态分析辅助 ML，结构信息在代码表示学习中的应用\"\n    papers:\n\n      - title: \"CodeQL: Semantic Code Analysis Engine\"\n        authors: \"GitHub / Semmle\"\n        venue: \"Tool (open-source)\"\n        year: 2019\n        relation: building-block\n        summary: \"基于 Datalog 的代码查询引擎，支持 inter-procedural data-flow 分析。StructFuse 用它提取 scope-bounded data-flow graph。\"\n\n      - title: \"code2vec: Learning Distributed Representations of Code\"\n        authors: \"Uri Alon, Meital Zilberstein, Omer Levy, Eran Yahav\"\n        venue: POPL\n        year: 2019\n        relation: background\n        summary: \"用 AST path 学习代码向量表示，首次大规模证明结构信息对代码表示学习的价值。\"\n\n      - title: \"code2seq: Generating Sequences from Structured Representations of Code\"\n        authors: \"Uri Alon, Shaked Brody, Omer Levy, Eran Yahav\"\n        venue: ICLR\n        year: 2019\n        relation: background\n        summary: \"code2vec 的序列生成扩展，用 AST path attention 生成方法名摘要。\"\n\n      - title: \"Detecting Code Clones with Graph Neural Network and Flow-Augmented Abstract Syntax Tree\"\n        authors: \"Wenhan Wang, Ge Li, Bo Ma, Xin Xia, Zhi Jin\"\n        venue: SANER\n        year: 2020\n        relation: background\n        summary: \"FA-AST: 用 data-flow 增强 AST 进行代码克隆检测，与 StructFuse 用 data-flow 做 hard negative 挖掘思路相关。\"\n\n      - title: \"GraphCodeBERT: Pre-training Code Representations with Data Flow\"\n        authors: \"Daya Guo, Shuo Ren, Shuai Lu, Zhangyin Feng, Duyu Tang, Shujie Liu, Long Zhou, Nan Duan, Alexey Svyatkovskiy, Shengyu Fu, Michele Tufano, Shao Kun Deng, Colin Clement, Dawn Drain, Neel Sundaresan, Jian Yin, Daxin Jiang, Ming Zhou\"\n        venue: ICLR\n        year: 2021\n        relation: background\n        summary: \"在预训练中引入 data-flow edge，证明 data-flow 信息提升代码理解任务。StructFuse 的 insight 与此相关但用途不同（hard negative mining vs pre-training）。\"\n\n      - title: \"ARISE: A Repository-level Graph Representation and Toolset for Agentic Fault Localization and Program Repair\"\n        authors: \"Shahd Seddik, Fatemeh Fard\"\n        venue: arXiv\n        year: 2025\n        relation: contrast\n        summary: \"用 multi-granularity program graph（含 intra-procedural def-use edges）辅助 LLM agent 做 fault localization。仅 intra-procedural + runtime tool calls，与 StructFuse 的 inter-procedural static mining 互补。\"\n\n  # ==========================================================================\n  # Category 5: Code Embeddings / Code Search\n  # ==========================================================================\n  code_embeddings_search:\n    description: \"代码嵌入模型和代码搜索方法\"\n    papers:\n\n      - title: \"CodeSearchNet Challenge: Evaluating the State of Semantic Code Search\"\n        authors: \"Hamel Husain, Ho-Hsiang Wu, Tiferet Gazit, Miltiadis Allamanis, Marc Brockschmidt\"\n        venue: arXiv\n        year: 2019\n        relation: background\n        summary: \"代码语义搜索 benchmark 和数据集，推动了代码嵌入模型的发展。\"\n\n      - title: \"CodeBERT: A Pre-Trained Model for Programming and Natural Languages\"\n        authors: \"Zhangyin Feng, Daya Guo, Duyu Tang, Nan Duan, Xiaocheng Feng, Ming Gong, Lixin Zou, Bing Qin, Ting Liu, Daxin Jiang, Ming Zhou\"\n        venue: \"EMNLP (Findings)\"\n        year: 2020\n        relation: background\n        summary: \"首个编程语言-自然语言双模态预训练模型，代码嵌入的早期里程碑。\"\n\n      - title: \"UniXcoder: Unified Cross-Modal Pre-training for Code Representation\"\n        authors: \"Daya Guo, Shuai Lu, Nan Duan, Yanlin Wang, Ming Zhou, Jian Yin\"\n        venue: ACL\n        year: 2022\n        relation: background\n        summary: \"统一跨模态代码预训练，在代码搜索等任务上取得 SOTA。\"\n\n      - title: \"StarCoder: May the Source Be with You!\"\n        authors: \"Raymond Li, Loubna Ben Allal, et al. (BigCode)\"\n        venue: TMLR\n        year: 2023\n        relation: building-block\n        summary: \"大规模开源代码 LLM，StructFuse 用 StarCoder2-3B 作为对比学习检索器的 backbone 之一。\"\n\n      - title: \"Code Llama: Open Foundation Models for Code\"\n        authors: \"Baptiste Roziere, Jonas Gehring, Fabian Gloeckle, et al. (Meta AI)\"\n        venue: arXiv\n        year: 2023\n        relation: background\n        summary: \"Meta 的代码大模型系列，基于 Llama 2 微调。\"\n\n      - title: \"Qwen2.5-Coder Technical Report\"\n        authors: \"Binyuan Hui, Jian Yang, Zeyu Cui, et al. (Qwen Team, Alibaba)\"\n        venue: arXiv\n        year: 2024\n        relation: building-block\n        summary: \"Qwen 代码模型系列，StructFuse 用 Qwen2.5-Coder-3B 作为对比学习检索器的 backbone。\"\n\n      - title: \"DeepSeek-Coder: When the Large Language Model Meets Programming -- The Rise of Code Intelligence\"\n        authors: \"Daya Guo, Qihao Zhu, Dejian Yang, Zhenda Xie, Kai Dong, Wentao Zhang, Guanting Chen, Xiao Bi, Yu Wu, Y.K. Li, Fuli Luo, Yingfei Xiong, Wenfeng Liang\"\n        venue: arXiv\n        year: 2024\n        relation: background\n        summary: \"开源代码 LLM 系列 (1.3B-33B)，project-level 代码训练 + 16K context + fill-in-the-blank 预训练。\"\n\n      - title: \"RepoFusion: Training Code Models to Understand Your Repository\"\n        authors: \"Disha Shrivastava, Denis Kocetkov, Harm de Vries, Dzmitry Bahdanau, Torsten Scholak\"\n        venue: arXiv\n        year: 2023\n        relation: background\n        summary: \"训练代码模型融合多个 cross-file repo context 进行代码补全，小模型 + repo context 可匹配大模型性能。\"\n\n      - title: \"BM25\"\n        authors: \"Stephen Robertson, Hugo Zaragoza\"\n        venue: \"Foundations and Trends in Information Retrieval\"\n        year: 2009\n        relation: baseline\n        summary: \"经典稀疏检索方法，StructFuse 的 baseline 之一。\"\n\n  # ==========================================================================\n  # Category 6: Graph-Guided Code Navigation (Inference-Time)\n  # ==========================================================================\n  graph_guided_inference:\n    description: \"推理时利用代码结构图辅助导航/检索的方法（与 StructFuse 的训练时结构信号互补）\"\n    papers:\n\n      - title: \"LocAgent: Graph-Guided LLM Agents for Code Localization\"\n        authors: \"Zhaoling Chen, Robert Tang, Gangda Deng, Fang Wu, Jialong Wu, Zhiwei Jiang, Viktor Prasanna, Arman Cohan, Xingyao Wang\"\n        venue: ACL\n        year: 2025\n        relation: contrast\n        summary: \"将代码库解析为有向异构图，LLM agent 通过 multi-hop 推理在图上导航做代码定位。推理时用结构图，StructFuse 训练时用。\"\n\n      - title: \"CodexGraph: Bridging Large Language Models and Code Repositories via Code Graph Databases\"\n        authors: \"Xiangyan Liu, Bo Lan, Zhiyuan Hu, Yang Liu, Zhicheng Zhang, Fei Wang, Michael Qizhe Shieh, Wenmeng Zhou\"\n        venue: NAACL\n        year: 2025\n        relation: contrast\n        summary: \"将代码库索引到图数据库，LLM agent 通过 graph query 接口检索结构化上下文。\"\n\n      - title: \"RANGER: Repository-Level Agent for Graph-Enhanced Retrieval\"\n        authors: \"Pratik Shah, Rajat Ghosh, Aryan Singhal, Debojyoti Dutta\"\n        venue: arXiv\n        year: 2025\n        relation: contrast\n        summary: \"构建 repo 知识图（含 variable-level 节点），dual-stage retrieval: Cypher lookup + MCTS-guided graph exploration。\"\n\n  # ==========================================================================\n  # Category 7: Infrastructure / Tools\n  # ==========================================================================\n  infrastructure:\n    description: \"StructFuse 依赖的核心基础设施和工具\"\n    papers:\n\n      - title: \"Billion-Scale Similarity Search with GPUs\"\n        authors: \"Jeff Johnson, Matthijs Douze, Herve Jegou\"\n        venue: \"IEEE Transactions on Big Data\"\n        year: 2021\n        relation: building-block\n        summary: \"FAISS: GPU 加速的大规模向量相似度搜索库，StructFuse 用于 ANN-based hard negative mining。\"\n\n      - title: \"Tree-sitter: An Incremental Parsing System for Programming Tools\"\n        authors: \"Max Brunsfeld et al.\"\n        venue: \"Software (Zenodo DOI: 10.5281/zenodo.13375512)\"\n        year: 2018\n        relation: building-block\n        summary: \"增量解析库，高效构建和更新 concrete syntax trees。与 CodeQL 互补用于代码结构提取。\"\n        note: \"软件工具，无正式论文。引用 Zenodo DOI 或 GitHub repo。\"\n",
      "numLines": 317,
      "startLine": 1,
      "totalLines": 317
    }
  },
  "sourceToolAssistantUUID": "43266bf1-9c14-4256-9af6-1f459f0ece7b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "b1d97499-4652-4822-8fc5-dbdc566ceedc",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 63 · 2026-05-14T21:33:19.114Z_

```json
{
  "parentUuid": "b501b26c-2ecf-4c71-b8ed-a1815f0c596e",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "84759776-b40c-4540-a06a-4728cc9fcd44",
  "timestamp": "2026-05-14T21:33:19.114Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "b1d97499-4652-4822-8fc5-dbdc566ceedc",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 64_

```json
{
  "type": "last-prompt",
  "leafUuid": "84759776-b40c-4540-a06a-4728cc9fcd44",
  "sessionId": "b1d97499-4652-4822-8fc5-dbdc566ceedc"
}
```

---

### Runtime record

_source line 65_

```json
{
  "type": "ai-title",
  "aiTitle": "Fix literature reference consistency issues",
  "sessionId": "b1d97499-4652-4822-8fc5-dbdc566ceedc"
}
```

---

### Assistant

_source line 66 · 2026-05-14T21:33:21.770Z_

Now executing all three fixes in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "84759776-b40c-4540-a06a-4728cc9fcd44",
  "isSidechain": false,
  "requestId": "req_011Cb3BG6yW2DxD7dPZ7HcoU",
  "type": "assistant",
  "uuid": "fee303b5-a574-4b09-ab31-50371fa1dc06",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "b1d97499-4652-4822-8fc5-dbdc566ceedc",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TrHihR41HJQiGqCmcjg5Zs",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7092,
      "cache_read_input_tokens": 51554,
      "output_tokens": 1480,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 7092,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1480,
          "cache_read_input_tokens": 51554,
          "cache_creation_input_tokens": 7092,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 7092
          },
          "type": "message"
        }
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

_source line 67 · 2026-05-14T21:33:34.225Z_

<details open><summary>🔧 Tool call — Edit · `toolu_019pQihabpbHQWwjxVHTdjZU`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/literature_map.yaml",
  "old_string": "      - title: \"RANGER: Repository-Level Agent for Graph-Enhanced Retrieval\"\n        authors: \"Pratik Shah, Rajat Ghosh, Aryan Singhal, Debojyoti Dutta\"\n        venue: arXiv\n        year: 2025\n        relation: contrast\n        summary: \"构建 repo 知识图（含 variable-level 节点），dual-stage retrieval: Cypher lookup + MCTS-guided graph exploration。\"\n\n  # ==========================================================================\n  # Category 7: Infrastructure / Tools",
  "new_string": "      - title: \"RANGER: Repository-Level Agent for Graph-Enhanced Retrieval\"\n        authors: \"Pratik Shah, Rajat Ghosh, Aryan Singhal, Debojyoti Dutta\"\n        venue: arXiv\n        year: 2025\n        relation: contrast\n        summary: \"构建 repo 知识图（含 variable-level 节点），dual-stage retrieval: Cypher lookup + MCTS-guided graph exploration。\"\n\n      - title: \"RepoGraph: Enhancing AI Software Engineering with Repository-level Code Graph\"\n        authors: \"Siru Ouyang, Wenhao Yu, Kaixin Ma, Zilin Xiao, Zhihan Zhang, Mengzhao Jia, Jiawei Han, Hongming Zhang, Dong Yu\"\n        venue: ICLR\n        year: 2025\n        relation: contrast\n        summary: \"以代码行为节点构建 repo-level 代码图，作为 SE agent 的 plug-in 导航模块。推理时逐行图导航，与 StructFuse 训练时批量提取结构信号互补。\"\n\n      - title: \"GraphCoder: Enhancing Repository-Level Code Completion via Coarse-to-fine Retrieval Based on Code Context Graph\"\n        authors: \"Wei Liu, Ailun Yu, Daoguang Zan, Bo Shen, Wei Zhang, Haiyan Zhao, Zhi Jin, Qianxiang Wang\"\n        venue: ASE\n        year: 2024\n        relation: contrast\n        summary: \"构建 code context graph（含 control-flow 和 data-dependence edges）进行 coarse-to-fine 检索辅助代码补全。使用 intra-procedural data-flow，与 StructFuse 的 inter-procedural scope 形成对比。\"\n\n  # ==========================================================================\n  # Category 7: Infrastructure / Tools"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fee303b5-a574-4b09-ab31-50371fa1dc06",
  "isSidechain": false,
  "requestId": "req_011Cb3BG6yW2DxD7dPZ7HcoU",
  "type": "assistant",
  "uuid": "548f0db3-71c1-4af1-9d06-c2ea0ae9863f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "b1d97499-4652-4822-8fc5-dbdc566ceedc",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TrHihR41HJQiGqCmcjg5Zs",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7092,
      "cache_read_input_tokens": 51554,
      "output_tokens": 1480,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 7092,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1480,
          "cache_read_input_tokens": 51554,
          "cache_creation_input_tokens": 7092,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 7092
          },
          "type": "message"
        }
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

_source line 68 · 2026-05-14T21:33:34.246Z_

<details><summary>↩ Tool result · `toolu_019pQihabpbHQWwjxVHTdjZU`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/literature_map.yaml has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "548f0db3-71c1-4af1-9d06-c2ea0ae9863f",
  "isSidechain": false,
  "promptId": "255fffc4-c17f-4b3b-8b5c-7a3031fdb918",
  "type": "user",
  "uuid": "1fd913e5-f8ee-431a-a8ec-6ab4b77136a3",
  "toolUseResult": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/literature_map.yaml",
    "oldString": "      - title: \"RANGER: Repository-Level Agent for Graph-Enhanced Retrieval\"\n        authors: \"Pratik Shah, Rajat Ghosh, Aryan Singhal, Debojyoti Dutta\"\n        venue: arXiv\n        year: 2025\n        relation: contrast\n        summary: \"构建 repo 知识图（含 variable-level 节点），dual-stage retrieval: Cypher lookup + MCTS-guided graph exploration。\"\n\n  # ==========================================================================\n  # Category 7: Infrastructure / Tools",
    "newString": "      - title: \"RANGER: Repository-Level Agent for Graph-Enhanced Retrieval\"\n        authors: \"Pratik Shah, Rajat Ghosh, Aryan Singhal, Debojyoti Dutta\"\n        venue: arXiv\n        year: 2025\n        relation: contrast\n        summary: \"构建 repo 知识图（含 variable-level 节点），dual-stage retrieval: Cypher lookup + MCTS-guided graph exploration。\"\n\n      - title: \"RepoGraph: Enhancing AI Software Engineering with Repository-level Code Graph\"\n        authors: \"Siru Ouyang, Wenhao Yu, Kaixin Ma, Zilin Xiao, Zhihan Zhang, Mengzhao Jia, Jiawei Han, Hongming Zhang, Dong Yu\"\n        venue: ICLR\n        year: 2025\n        relation: contrast\n        summary: \"以代码行为节点构建 repo-level 代码图，作为 SE agent 的 plug-in 导航模块。推理时逐行图导航，与 StructFuse 训练时批量提取结构信号互补。\"\n\n      - title: \"GraphCoder: Enhancing Repository-Level Code Completion via Coarse-to-fine Retrieval Based on Code Context Graph\"\n        authors: \"Wei Liu, Ailun Yu, Daoguang Zan, Bo Shen, Wei Zhang, Haiyan Zhao, Zhi Jin, Qianxiang Wang\"\n        venue: ASE\n        year: 2024\n        relation: contrast\n        summary: \"构建 code context graph（含 control-flow 和 data-dependence edges）进行 coarse-to-fine 检索辅助代码补全。使用 intra-procedural data-flow，与 StructFuse 的 inter-procedural scope 形成对比。\"\n\n  # ==========================================================================\n  # Category 7: Infrastructure / Tools",
    "originalFile": null,
    "structuredPatch": [
      {
        "oldStart": 293,
        "oldLines": 6,
        "newStart": 293,
        "newLines": 20,
        "lines": [
          "         relation: contrast",
          "         summary: \"构建 repo 知识图（含 variable-level 节点），dual-stage retrieval: Cypher lookup + MCTS-guided graph exploration。\"",
          " ",
          "+      - title: \"RepoGraph: Enhancing AI Software Engineering with Repository-level Code Graph\"",
          "+        authors: \"Siru Ouyang, Wenhao Yu, Kaixin Ma, Zilin Xiao, Zhihan Zhang, Mengzhao Jia, Jiawei Han, Hongming Zhang, Dong Yu\"",
          "+        venue: ICLR",
          "+        year: 2025",
          "+        relation: contrast",
          "+        summary: \"以代码行为节点构建 repo-level 代码图，作为 SE agent 的 plug-in 导航模块。推理时逐行图导航，与 StructFuse 训练时批量提取结构信号互补。\"",
          "+",
          "+      - title: \"GraphCoder: Enhancing Repository-Level Code Completion via Coarse-to-fine Retrieval Based on Code Context Graph\"",
          "+        authors: \"Wei Liu, Ailun Yu, Daoguang Zan, Bo Shen, Wei Zhang, Haiyan Zhao, Zhi Jin, Qianxiang Wang\"",
          "+        venue: ASE",
          "+        year: 2024",
          "+        relation: contrast",
          "+        summary: \"构建 code context graph（含 control-flow 和 data-dependence edges）进行 coarse-to-fine 检索辅助代码补全。使用 intra-procedural data-flow，与 StructFuse 的 inter-procedural scope 形成对比。\"",
          "+",
          "   # ==========================================================================",
          "   # Category 7: Infrastructure / Tools",
          "   # =========================================================================="
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  },
  "sourceToolAssistantUUID": "548f0db3-71c1-4af1-9d06-c2ea0ae9863f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "b1d97499-4652-4822-8fc5-dbdc566ceedc",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 69 · 2026-05-14T21:33:35.973Z_

<details open><summary>🔧 Tool call — Edit · `toolu_01U5Cb5hLpWQbRCpaUztDH8X`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/literature_map.yaml",
  "old_string": "      - title: \"ARISE: A Repository-level Graph Representation and Toolset for Agentic Fault Localization and Program Repair\"\n        authors: \"Shahd Seddik, Fatemeh Fard\"\n        venue: arXiv\n        year: 2025",
  "new_string": "      - title: \"ARISE: A Repository-level Graph Representation and Toolset for Agentic Fault Localization and Program Repair\"\n        authors: \"Shahd Seddik, Fatemeh Fard\"\n        venue: arXiv\n        year: 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1fd913e5-f8ee-431a-a8ec-6ab4b77136a3",
  "isSidechain": false,
  "requestId": "req_011Cb3BG6yW2DxD7dPZ7HcoU",
  "type": "assistant",
  "uuid": "7373311f-3a10-4e6c-b211-f189372db93a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "b1d97499-4652-4822-8fc5-dbdc566ceedc",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TrHihR41HJQiGqCmcjg5Zs",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7092,
      "cache_read_input_tokens": 51554,
      "output_tokens": 1480,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 7092,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1480,
          "cache_read_input_tokens": 51554,
          "cache_creation_input_tokens": 7092,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 7092
          },
          "type": "message"
        }
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

_source line 70 · 2026-05-14T21:33:35.987Z_

<details><summary>↩ Tool result · `toolu_01U5Cb5hLpWQbRCpaUztDH8X`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/literature_map.yaml has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7373311f-3a10-4e6c-b211-f189372db93a",
  "isSidechain": false,
  "promptId": "255fffc4-c17f-4b3b-8b5c-7a3031fdb918",
  "type": "user",
  "uuid": "607305cf-4a20-4c3a-b6bb-d79fa8cfd21f",
  "toolUseResult": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/literature_map.yaml",
    "oldString": "      - title: \"ARISE: A Repository-level Graph Representation and Toolset for Agentic Fault Localization and Program Repair\"\n        authors: \"Shahd Seddik, Fatemeh Fard\"\n        venue: arXiv\n        year: 2025",
    "newString": "      - title: \"ARISE: A Repository-level Graph Representation and Toolset for Agentic Fault Localization and Program Repair\"\n        authors: \"Shahd Seddik, Fatemeh Fard\"\n        venue: arXiv\n        year: 2026",
    "originalFile": null,
    "structuredPatch": [
      {
        "oldStart": 191,
        "oldLines": 7,
        "newStart": 191,
        "newLines": 7,
        "lines": [
          "       - title: \"ARISE: A Repository-level Graph Representation and Toolset for Agentic Fault Localization and Program Repair\"",
          "         authors: \"Shahd Seddik, Fatemeh Fard\"",
          "         venue: arXiv",
          "-        year: 2025",
          "+        year: 2026",
          "         relation: contrast",
          "         summary: \"用 multi-granularity program graph（含 intra-procedural def-use edges）辅助 LLM agent 做 fault localization。仅 intra-procedural + runtime tool calls，与 StructFuse 的 inter-procedural static mining 互补。\"",
          " "
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  },
  "sourceToolAssistantUUID": "7373311f-3a10-4e6c-b211-f189372db93a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "b1d97499-4652-4822-8fc5-dbdc566ceedc",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 71 · 2026-05-14T21:33:37.834Z_

<details open><summary>🔧 Tool call — Edit · `toolu_01FmnNZS2NG5fzUugHs4Zsqt`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/literature_map.yaml",
  "old_string": "# 总计: 37 entries (含 2 个软件工具引用)",
  "new_string": "# 总计: 39 entries (含 2 个软件工具引用)"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "607305cf-4a20-4c3a-b6bb-d79fa8cfd21f",
  "isSidechain": false,
  "requestId": "req_011Cb3BG6yW2DxD7dPZ7HcoU",
  "type": "assistant",
  "uuid": "a4ad56a7-1a0b-432b-bbf6-c47be90c4c63",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "b1d97499-4652-4822-8fc5-dbdc566ceedc",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TrHihR41HJQiGqCmcjg5Zs",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7092,
      "cache_read_input_tokens": 51554,
      "output_tokens": 1480,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 7092,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1480,
          "cache_read_input_tokens": 51554,
          "cache_creation_input_tokens": 7092,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 7092
          },
          "type": "message"
        }
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

_source line 72 · 2026-05-14T21:33:37.845Z_

<details><summary>↩ Tool result · `toolu_01FmnNZS2NG5fzUugHs4Zsqt`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/literature_map.yaml has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a4ad56a7-1a0b-432b-bbf6-c47be90c4c63",
  "isSidechain": false,
  "promptId": "255fffc4-c17f-4b3b-8b5c-7a3031fdb918",
  "type": "user",
  "uuid": "c6a9caf2-fad1-4261-892b-2a558d01ee17",
  "toolUseResult": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/literature_map.yaml",
    "oldString": "# 总计: 37 entries (含 2 个软件工具引用)",
    "newString": "# 总计: 39 entries (含 2 个软件工具引用)",
    "originalFile": null,
    "structuredPatch": [
      {
        "oldStart": 1,
        "oldLines": 7,
        "newStart": 1,
        "newLines": 7,
        "lines": [
          " # StructFuse — Related Work Literature Map",
          " # 最后更新: 2026-05-14",
          " # 说明: 只收录已验证存在的论文。每篇均经 WebSearch 确认标题/venue/year。",
          "-# 总计: 37 entries (含 2 个软件工具引用)",
          "+# 总计: 39 entries (含 2 个软件工具引用)",
          " ",
          " categories:",
          " "
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  },
  "sourceToolAssistantUUID": "a4ad56a7-1a0b-432b-bbf6-c47be90c4c63",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "b1d97499-4652-4822-8fc5-dbdc566ceedc",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 73 · 2026-05-14T21:33:45.043Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry · `toolu_01UR4EdxVEd1gYUz66EY6xtj`</summary>

```json
{
  "exp_id": "plan_017_literature",
  "field": "notes",
  "value": "Inference-time graph method comparison 完成。8 papers surveyed，其中 6 篇纳入 literature_map.yaml 和 discussion_v2.md（CodexGraph, LocAgent, RANGER, GraphCoder, ARISE, RepoGraph）。CodeGRAG 和 CodeRAG 经调研排除：CodeGRAG（arXiv 2405.02355）关注 NL→code generation 的 graph-augmented prompting，不涉及代码检索或对比学习；CodeRAG 系列（CodeRAG-Bench 2406.14497 / CodeRAG 2504.10046）关注 retrieval-augmented code generation benchmark 和 bigraph-based 代码生成，均为生成任务而非检索训练。两者与 StructFuse 的 scope（训练时结构信号用于对比学习代码检索）不符，故未纳入 discussion。",
  "project": "structfuse-context"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c6a9caf2-fad1-4261-892b-2a558d01ee17",
  "isSidechain": false,
  "requestId": "req_011Cb3BG6yW2DxD7dPZ7HcoU",
  "type": "assistant",
  "uuid": "d85427b8-40b2-4563-92a0-0883e4c9bf99",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "b1d97499-4652-4822-8fc5-dbdc566ceedc",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TrHihR41HJQiGqCmcjg5Zs",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7092,
      "cache_read_input_tokens": 51554,
      "output_tokens": 1480,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 7092,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1480,
          "cache_read_input_tokens": 51554,
          "cache_creation_input_tokens": 7092,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 7092
          },
          "type": "message"
        }
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

_source line 74 · 2026-05-14T21:33:45.248Z_

<details><summary>↩ Tool result · `toolu_01UR4EdxVEd1gYUz66EY6xtj`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"exp_id\": \"plan_017_literature\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T18:49:00.477Z\", \"updated_at\": \"2026-05-14T21:33:45.149Z\", \"hypothesis\": \"Inference-time graph method comparison: 8 papers surveyed (CodexGraph, LocAgent, RANGER, GraphCoder, ARISE, RepoGraph, CodeGRAG, CodeRAG). Discussion v2 drafted, all citations verified. Conclusion: training-time vs inference-time complementary.\", \"spec\": {\"command\": \"analysis only (no training)\", \"server\": \"local\", \"data_path\": \"N/A\", \"data_count\": 0, \"model_name\": \"N/A\", \"seed\": \"N/A\", \"checkpoint_path\": \"N/A\", \"log_path\": \"N/A\"}, \"conclusion\": \"success\", \"metrics\": {\"papers_surveyed\": 8, \"citations_verified\": 8, \"discussion_draft\": \"artifacts/paper_drafts/discussion_v2.md\", \"artifact_id\": \"art_20260514_a2e1cd\"}, \"completed_at\": \"2026-05-14T18:49:39.557Z\", \"notes\": \"Inference-time graph method comparison 完成。8 papers surveyed，其中 6 篇纳入 literature_map.yaml 和 discussion_v2.md（CodexGraph, LocAgent, RANGER, GraphCoder, ARISE, RepoGraph）。CodeGRAG 和 CodeRAG 经调研排除：CodeGRAG（arXiv 2405.02355）关注 NL→code generation 的 graph-augmented prompting，不涉及代码检索或对比学习；CodeRAG 系列（CodeRAG-Bench 2406.14497 / CodeRAG 2504.10046）关注 retrieval-augmented code generation benchmark 和 bigraph-based 代码生成，均为生成任务而非检索训练。两者与 StructFuse 的 scope（训练时结构信号用于对比学习代码检索）不符，故未纳入 discussion。\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.1902}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d85427b8-40b2-4563-92a0-0883e4c9bf99",
  "isSidechain": false,
  "promptId": "255fffc4-c17f-4b3b-8b5c-7a3031fdb918",
  "type": "user",
  "uuid": "cf3ffedb-ade4-4bf8-b67b-6875cfc07909",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"exp_id\\\": \\\"plan_017_literature\\\", \\\"experiment\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-14T18:49:00.477Z\\\", \\\"updated_at\\\": \\\"2026-05-14T21:33:45.149Z\\\", \\\"hypothesis\\\": \\\"Inference-time graph method comparison: 8 papers surveyed (CodexGraph, LocAgent, RANGER, GraphCoder, ARISE, RepoGraph, CodeGRAG, CodeRAG). Discussion v2 drafted, all citations verified. Conclusion: training-time vs inference-time complementary.\\\", \\\"spec\\\": {\\\"command\\\": \\\"analysis only (no training)\\\", \\\"server\\\": \\\"local\\\", \\\"data_path\\\": \\\"N/A\\\", \\\"data_count\\\": 0, \\\"model_name\\\": \\\"N/A\\\", \\\"seed\\\": \\\"N/A\\\", \\\"checkpoint_path\\\": \\\"N/A\\\", \\\"log_path\\\": \\\"N/A\\\"}, \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"papers_surveyed\\\": 8, \\\"citations_verified\\\": 8, \\\"discussion_draft\\\": \\\"artifacts/paper_drafts/discussion_v2.md\\\", \\\"artifact_id\\\": \\\"art_20260514_a2e1cd\\\"}, \\\"completed_at\\\": \\\"2026-05-14T18:49:39.557Z\\\", \\\"notes\\\": \\\"Inference-time graph method comparison 完成。8 papers surveyed，其中 6 篇纳入 literature_map.yaml 和 discussion_v2.md（CodexGraph, LocAgent, RANGER, GraphCoder, ARISE, RepoGraph）。CodeGRAG 和 CodeRAG 经调研排除：CodeGRAG（arXiv 2405.02355）关注 NL→code generation 的 graph-augmented prompting，不涉及代码检索或对比学习；CodeRAG 系列（CodeRAG-Bench 2406.14497 / CodeRAG 2504.10046）关注 retrieval-augmented code generation benchmark 和 bigraph-based 代码生成，均为生成任务而非检索训练。两者与 StructFuse 的 scope（训练时结构信号用于对比学习代码检索）不符，故未纳入 discussion。\\\"}}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.1902}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"exp_id\": \"plan_017_literature\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T18:49:00.477Z\", \"updated_at\": \"2026-05-14T21:33:45.149Z\", \"hypothesis\": \"Inference-time graph method comparison: 8 papers surveyed (CodexGraph, LocAgent, RANGER, GraphCoder, ARISE, RepoGraph, CodeGRAG, CodeRAG). Discussion v2 drafted, all citations verified. Conclusion: training-time vs inference-time complementary.\", \"spec\": {\"command\": \"analysis only (no training)\", \"server\": \"local\", \"data_path\": \"N/A\", \"data_count\": 0, \"model_name\": \"N/A\", \"seed\": \"N/A\", \"checkpoint_path\": \"N/A\", \"log_path\": \"N/A\"}, \"conclusion\": \"success\", \"metrics\": {\"papers_surveyed\": 8, \"citations_verified\": 8, \"discussion_draft\": \"artifacts/paper_drafts/discussion_v2.md\", \"artifact_id\": \"art_20260514_a2e1cd\"}, \"completed_at\": \"2026-05-14T18:49:39.557Z\", \"notes\": \"Inference-time graph method comparison 完成。8 papers surveyed，其中 6 篇纳入 literature_map.yaml 和 discussion_v2.md（CodexGraph, LocAgent, RANGER, GraphCoder, ARISE, RepoGraph）。CodeGRAG 和 CodeRAG 经调研排除：CodeGRAG（arXiv 2405.02355）关注 NL→code generation 的 graph-augmented prompting，不涉及代码检索或对比学习；CodeRAG 系列（CodeRAG-Bench 2406.14497 / CodeRAG 2504.10046）关注 retrieval-augmented code generation benchmark 和 bigraph-based 代码生成，均为生成任务而非检索训练。两者与 StructFuse 的 scope（训练时结构信号用于对比学习代码检索）不符，故未纳入 discussion。\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.1902}}"
    }
  },
  "sourceToolAssistantUUID": "d85427b8-40b2-4563-92a0-0883e4c9bf99",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "b1d97499-4652-4822-8fc5-dbdc566ceedc",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 75 · 2026-05-14T21:33:48.114Z_

四项修改全部完成。验证一下 literature_map.yaml 的最终状态。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cf3ffedb-ade4-4bf8-b67b-6875cfc07909",
  "isSidechain": false,
  "requestId": "req_011Cb3BJ2k4bewrPhAbJiLYt",
  "type": "assistant",
  "uuid": "15701fed-ef2b-4515-9163-302a9088dbc2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "b1d97499-4652-4822-8fc5-dbdc566ceedc",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014LCkVHMubHNe6VrMrs6ijL",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2407,
      "cache_read_input_tokens": 58646,
      "output_tokens": 248,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2407,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 248,
          "cache_read_input_tokens": 58646,
          "cache_creation_input_tokens": 2407,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2407
          },
          "type": "message"
        }
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

_source line 76 · 2026-05-14T21:33:49.084Z_

<details open><summary>🔧 Tool call — Read · `toolu_01X2GZyXywTFPbe6XkaMVetX`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/literature_map.yaml",
  "offset": 268,
  "limit": 40
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "15701fed-ef2b-4515-9163-302a9088dbc2",
  "isSidechain": false,
  "requestId": "req_011Cb3BJ2k4bewrPhAbJiLYt",
  "type": "assistant",
  "uuid": "14fb0830-a456-465f-b622-90f6ab3de367",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "b1d97499-4652-4822-8fc5-dbdc566ceedc",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014LCkVHMubHNe6VrMrs6ijL",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2407,
      "cache_read_input_tokens": 58646,
      "output_tokens": 248,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2407,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 248,
          "cache_read_input_tokens": 58646,
          "cache_creation_input_tokens": 2407,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2407
          },
          "type": "message"
        }
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

_source line 77 · 2026-05-14T21:33:49.095Z_

<details><summary>↩ Tool result · `toolu_01X2GZyXywTFPbe6XkaMVetX`</summary>

```text
268	  # ==========================================================================
269	  # Category 6: Graph-Guided Code Navigation (Inference-Time)
270	  # ==========================================================================
271	  graph_guided_inference:
272	    description: "推理时利用代码结构图辅助导航/检索的方法（与 StructFuse 的训练时结构信号互补）"
273	    papers:
274	
275	      - title: "LocAgent: Graph-Guided LLM Agents for Code Localization"
276	        authors: "Zhaoling Chen, Robert Tang, Gangda Deng, Fang Wu, Jialong Wu, Zhiwei Jiang, Viktor Prasanna, Arman Cohan, Xingyao Wang"
277	        venue: ACL
278	        year: 2025
279	        relation: contrast
280	        summary: "将代码库解析为有向异构图，LLM agent 通过 multi-hop 推理在图上导航做代码定位。推理时用结构图，StructFuse 训练时用。"
281	
282	      - title: "CodexGraph: Bridging Large Language Models and Code Repositories via Code Graph Databases"
283	        authors: "Xiangyan Liu, Bo Lan, Zhiyuan Hu, Yang Liu, Zhicheng Zhang, Fei Wang, Michael Qizhe Shieh, Wenmeng Zhou"
284	        venue: NAACL
285	        year: 2025
286	        relation: contrast
287	        summary: "将代码库索引到图数据库，LLM agent 通过 graph query 接口检索结构化上下文。"
288	
289	      - title: "RANGER: Repository-Level Agent for Graph-Enhanced Retrieval"
290	        authors: "Pratik Shah, Rajat Ghosh, Aryan Singhal, Debojyoti Dutta"
291	        venue: arXiv
292	        year: 2025
293	        relation: contrast
294	        summary: "构建 repo 知识图（含 variable-level 节点），dual-stage retrieval: Cypher lookup + MCTS-guided graph exploration。"
295	
296	      - title: "RepoGraph: Enhancing AI Software Engineering with Repository-level Code Graph"
297	        authors: "Siru Ouyang, Wenhao Yu, Kaixin Ma, Zilin Xiao, Zhihan Zhang, Mengzhao Jia, Jiawei Han, Hongming Zhang, Dong Yu"
298	        venue: ICLR
299	        year: 2025
300	        relation: contrast
301	        summary: "以代码行为节点构建 repo-level 代码图，作为 SE agent 的 plug-in 导航模块。推理时逐行图导航，与 StructFuse 训练时批量提取结构信号互补。"
302	
303	      - title: "GraphCoder: Enhancing Repository-Level Code Completion via Coarse-to-fine Retrieval Based on Code Context Graph"
304	        authors: "Wei Liu, Ailun Yu, Daoguang Zan, Bo Shen, Wei Zhang, Haiyan Zhao, Zhi Jin, Qianxiang Wang"
305	        venue: ASE
306	        year: 2024
307	        relation: contrast
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "14fb0830-a456-465f-b622-90f6ab3de367",
  "isSidechain": false,
  "promptId": "255fffc4-c17f-4b3b-8b5c-7a3031fdb918",
  "type": "user",
  "uuid": "270ebae0-6ab0-4607-bfec-c8d042509efd",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/literature_map.yaml",
      "content": "  # ==========================================================================\n  # Category 6: Graph-Guided Code Navigation (Inference-Time)\n  # ==========================================================================\n  graph_guided_inference:\n    description: \"推理时利用代码结构图辅助导航/检索的方法（与 StructFuse 的训练时结构信号互补）\"\n    papers:\n\n      - title: \"LocAgent: Graph-Guided LLM Agents for Code Localization\"\n        authors: \"Zhaoling Chen, Robert Tang, Gangda Deng, Fang Wu, Jialong Wu, Zhiwei Jiang, Viktor Prasanna, Arman Cohan, Xingyao Wang\"\n        venue: ACL\n        year: 2025\n        relation: contrast\n        summary: \"将代码库解析为有向异构图，LLM agent 通过 multi-hop 推理在图上导航做代码定位。推理时用结构图，StructFuse 训练时用。\"\n\n      - title: \"CodexGraph: Bridging Large Language Models and Code Repositories via Code Graph Databases\"\n        authors: \"Xiangyan Liu, Bo Lan, Zhiyuan Hu, Yang Liu, Zhicheng Zhang, Fei Wang, Michael Qizhe Shieh, Wenmeng Zhou\"\n        venue: NAACL\n        year: 2025\n        relation: contrast\n        summary: \"将代码库索引到图数据库，LLM agent 通过 graph query 接口检索结构化上下文。\"\n\n      - title: \"RANGER: Repository-Level Agent for Graph-Enhanced Retrieval\"\n        authors: \"Pratik Shah, Rajat Ghosh, Aryan Singhal, Debojyoti Dutta\"\n        venue: arXiv\n        year: 2025\n        relation: contrast\n        summary: \"构建 repo 知识图（含 variable-level 节点），dual-stage retrieval: Cypher lookup + MCTS-guided graph exploration。\"\n\n      - title: \"RepoGraph: Enhancing AI Software Engineering with Repository-level Code Graph\"\n        authors: \"Siru Ouyang, Wenhao Yu, Kaixin Ma, Zilin Xiao, Zhihan Zhang, Mengzhao Jia, Jiawei Han, Hongming Zhang, Dong Yu\"\n        venue: ICLR\n        year: 2025\n        relation: contrast\n        summary: \"以代码行为节点构建 repo-level 代码图，作为 SE agent 的 plug-in 导航模块。推理时逐行图导航，与 StructFuse 训练时批量提取结构信号互补。\"\n\n      - title: \"GraphCoder: Enhancing Repository-Level Code Completion via Coarse-to-fine Retrieval Based on Code Context Graph\"\n        authors: \"Wei Liu, Ailun Yu, Daoguang Zan, Bo Shen, Wei Zhang, Haiyan Zhao, Zhi Jin, Qianxiang Wang\"\n        venue: ASE\n        year: 2024\n        relation: contrast",
      "numLines": 40,
      "startLine": 268,
      "totalLines": 331
    }
  },
  "sourceToolAssistantUUID": "14fb0830-a456-465f-b622-90f6ab3de367",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "b1d97499-4652-4822-8fc5-dbdc566ceedc",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 78 · 2026-05-14T21:33:49.720Z_

<details open><summary>🔧 Tool call — Read · `toolu_01TrX9Kc1q5dNLQCKvFRh3pA`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/literature_map.yaml",
  "offset": 190,
  "limit": 8
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "270ebae0-6ab0-4607-bfec-c8d042509efd",
  "isSidechain": false,
  "requestId": "req_011Cb3BJ2k4bewrPhAbJiLYt",
  "type": "assistant",
  "uuid": "73f4bcbe-46f4-4a69-b0aa-0ed6fd7ad019",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "b1d97499-4652-4822-8fc5-dbdc566ceedc",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014LCkVHMubHNe6VrMrs6ijL",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2407,
      "cache_read_input_tokens": 58646,
      "output_tokens": 248,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2407,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 248,
          "cache_read_input_tokens": 58646,
          "cache_creation_input_tokens": 2407,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2407
          },
          "type": "message"
        }
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

_source line 79 · 2026-05-14T21:33:49.727Z_

<details><summary>↩ Tool result · `toolu_01TrX9Kc1q5dNLQCKvFRh3pA`</summary>

```text
190	
191	      - title: "ARISE: A Repository-level Graph Representation and Toolset for Agentic Fault Localization and Program Repair"
192	        authors: "Shahd Seddik, Fatemeh Fard"
193	        venue: arXiv
194	        year: 2026
195	        relation: contrast
196	        summary: "用 multi-granularity program graph（含 intra-procedural def-use edges）辅助 LLM agent 做 fault localization。仅 intra-procedural + runtime tool calls，与 StructFuse 的 inter-procedural static mining 互补。"
197	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "73f4bcbe-46f4-4a69-b0aa-0ed6fd7ad019",
  "isSidechain": false,
  "promptId": "255fffc4-c17f-4b3b-8b5c-7a3031fdb918",
  "type": "user",
  "uuid": "774e9e1b-2273-4f20-aa71-7ea5d5b58a97",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/literature_map.yaml",
      "content": "\n      - title: \"ARISE: A Repository-level Graph Representation and Toolset for Agentic Fault Localization and Program Repair\"\n        authors: \"Shahd Seddik, Fatemeh Fard\"\n        venue: arXiv\n        year: 2026\n        relation: contrast\n        summary: \"用 multi-granularity program graph（含 intra-procedural def-use edges）辅助 LLM agent 做 fault localization。仅 intra-procedural + runtime tool calls，与 StructFuse 的 inter-procedural static mining 互补。\"\n",
      "numLines": 8,
      "startLine": 190,
      "totalLines": 331
    }
  },
  "sourceToolAssistantUUID": "73f4bcbe-46f4-4a69-b0aa-0ed6fd7ad019",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "b1d97499-4652-4822-8fc5-dbdc566ceedc",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 80_

```json
{
  "type": "last-prompt",
  "leafUuid": "774e9e1b-2273-4f20-aa71-7ea5d5b58a97",
  "sessionId": "b1d97499-4652-4822-8fc5-dbdc566ceedc"
}
```

---

### Runtime record

_source line 81_

```json
{
  "type": "ai-title",
  "aiTitle": "Fix literature reference consistency issues",
  "sessionId": "b1d97499-4652-4822-8fc5-dbdc566ceedc"
}
```

---

### Assistant

_source line 82 · 2026-05-14T21:33:58.925Z_

全部修改已验证。处理结果：

**问题 1 — RepoGraph + GraphCoder 缺失**：两篇均经 WebSearch 确认真实存在。RepoGraph（Ouyang et al., ICLR 2025）和 GraphCoder（Liu et al., ASE 2024）已录入 `literature_map.yaml` 的 `graph_guided_inference` 类别，含完整作者/venue/year/relation/summary。discussion_v2.md 引用无需修改。总计从 37 → 39 entries。

**问题 2 — ARISE 年份不一致**：arXiv ID 2605.03117 确认为 2026 年 5 月发布。`literature_map.yaml` 已从 `year: 2025` 修正为 `year: 2026`，与 `discussion_v2.md` 的 `(Seddik & Fard, 2026)` 一致。

**问题 3 — CodeGRAG + CodeRAG 排除说明**：`plan_017_literature` registry notes 已更新。排除理由：CodeGRAG 关注 NL→code generation 的 graph-augmented prompting，CodeRAG 系列关注 retrieval-augmented code generation benchmark/bigraph 代码生成，均为生成任务，与 StructFuse 的 scope（训练时结构信号用于对比学习代码检索）不符。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "774e9e1b-2273-4f20-aa71-7ea5d5b58a97",
  "isSidechain": false,
  "requestId": "req_011Cb3BJMsFoCYkktC6jLsei",
  "type": "assistant",
  "uuid": "a0be3419-bb82-49e2-9661-638a1cd57acc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "b1d97499-4652-4822-8fc5-dbdc566ceedc",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RrYauFXPiFGwf5nXK96tju",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1339,
      "cache_read_input_tokens": 61053,
      "output_tokens": 390,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1339,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 390,
          "cache_read_input_tokens": 61053,
          "cache_creation_input_tokens": 1339,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1339
          },
          "type": "message"
        }
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

_source line 83_

```json
{
  "type": "last-prompt",
  "leafUuid": "a0be3419-bb82-49e2-9661-638a1cd57acc",
  "sessionId": "b1d97499-4652-4822-8fc5-dbdc566ceedc"
}
```

---

### Runtime record

_source line 84_

```json
{
  "type": "ai-title",
  "aiTitle": "Fix literature reference consistency issues",
  "sessionId": "b1d97499-4652-4822-8fc5-dbdc566ceedc"
}
```

---
