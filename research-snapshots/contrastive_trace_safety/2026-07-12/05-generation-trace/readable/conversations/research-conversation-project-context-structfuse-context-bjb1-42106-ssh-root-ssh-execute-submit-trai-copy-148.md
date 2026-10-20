# Research conversation: <project_context> # 项目: structfuse-context ## 运行环境 - 服务器名: bjb1-42106 - SSH 账户: root（调用 ssh_execute / submit_training_jo

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 54
- **Recorded user turns:** 1
- **Tool calls:** 13
- **Original source:** `logs/chats/exported-trajectories/account-1/999f865e-f544-467f-b7e8-732fb33862f3.jsonl`
- **Structured JSON:** [`88590e7cb1cbcedee148.json`](../../sessions/88/88590e7cb1cbcedee148.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-15T01:58:22.472Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-15T01:58:22.472Z",
  "sessionId": "999f865e-f544-467f-b7e8-732fb33862f3",
  "content": "&lt;project_context>\n# 项目: structfuse-context\n\n## 运行环境\n- 服务器名: bjb1-42106\n- SSH 账户: root（调用 ssh_execute / submit_training_job 时传入 account=\"root\"）\n- SSH 连接命令: ssh connect.bjb1.seetacloud.com  # 必须用此命令，~/.ssh/config 自动应用密钥和跳板机，禁止用裸 IP\n- 项目代码根目录: /root/structfuse\n\n\n## 环境搭建\n连接服务器后先调 `detect_image` 检测是否为预置镜像。如果匹配，跳过基础环境搭建，只装项目特有依赖。已预装的包不要重复安装。\n\n## 输出风格\n回复简洁直接。只输出执行结果和必要信息，不要解释过程、不要客套、不要给未被要求的建议。\n&lt;/project_context>\n## 任务：审视 Claim 2 Exploratory 措辞\n\n读取 paper_framing.md，检查 Claim 2（dataflow-aware filtering）的 \"exploratory observation\" 措辞是否准确、一致、防守性足够。\n\n### 背景\n- D035 决策：Claim 2 从 \"conditional benefit beyond embedding\" 降级为 \"exploratory observation with testable prediction\"\n- 原因：dataflow 效果 encoder-dependent (Qwen dataflow > random +0.8pp, StarCoder dataflow < random -0.5pp)，n=2 encoders 不足以做强 claim\n- 这是 Reviewer 重点攻击面\n\n### 你的任务\n\n1. 用 read_project_file 读取：\n   - `paper_framing.md`\n   - `memory.md`\n\n2. 检查以下方面：\n   - Claim 2 的措辞是否在所有出现位置一致（abstract、intro、experiments、discussion、conclusion）\n   - 是否有地方不小心用了过强的措辞（如 \"demonstrates\", \"shows\", \"proves\" 用于 Claim 2）\n   - \"exploratory observation\" 的 hedge 是否充分（应包含：n=2 的限制、encoder-dependent 的 caveat、testable prediction 的前向声明）\n   - 是否明确区分了 Claim 1 (strong, confirmed) 和 Claim 2 (exploratory)\n\n3. 读取已有的论文草稿（如果存在）：\n   - `/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/` 下的所有 .md 文件\n\n4. 输出一份审查报告，写到：\n   `/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/claim2_wording_review.md`\n\n   包含：\n   - 所有出现 Claim 2 的位置及当前措辞\n   - 每处的强度评级（✅ 合适 / ⚠️ 偏强 / ❌ 过强）\n   - 建议修改（如有）\n   - 审稿人可能的攻击角度和预备 rebuttal 要点\n"
}
```

---

### Runtime record

_source line 2 · 2026-05-15T01:58:22.476Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-15T01:58:22.476Z",
  "sessionId": "999f865e-f544-467f-b7e8-732fb33862f3"
}
```

---

## Round 1

52 recorded events

### User

_source line 3 · 2026-05-15T01:58:22.510Z_

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
## 任务：审视 Claim 2 Exploratory 措辞

读取 paper_framing.md，检查 Claim 2（dataflow-aware filtering）的 "exploratory observation" 措辞是否准确、一致、防守性足够。

### 背景
- D035 决策：Claim 2 从 "conditional benefit beyond embedding" 降级为 "exploratory observation with testable prediction"
- 原因：dataflow 效果 encoder-dependent (Qwen dataflow > random +0.8pp, StarCoder dataflow < random -0.5pp)，n=2 encoders 不足以做强 claim
- 这是 Reviewer 重点攻击面

### 你的任务

1. 用 read_project_file 读取：
   - `paper_framing.md`
   - `memory.md`

2. 检查以下方面：
   - Claim 2 的措辞是否在所有出现位置一致（abstract、intro、experiments、discussion、conclusion）
   - 是否有地方不小心用了过强的措辞（如 "demonstrates", "shows", "proves" 用于 Claim 2）
   - "exploratory observation" 的 hedge 是否充分（应包含：n=2 的限制、encoder-dependent 的 caveat、testable prediction 的前向声明）
   - 是否明确区分了 Claim 1 (strong, confirmed) 和 Claim 2 (exploratory)

3. 读取已有的论文草稿（如果存在）：
   - `/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/` 下的所有 .md 文件

4. 输出一份审查报告，写到：
   `/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/claim2_wording_review.md`

   包含：
   - 所有出现 Claim 2 的位置及当前措辞
   - 每处的强度评级（✅ 合适 / ⚠️ 偏强 / ❌ 过强）
   - 建议修改（如有）
   - 审稿人可能的攻击角度和预备 rebuttal 要点


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "82620338-1cd7-4c43-9283-e5cb821c1607",
  "type": "user",
  "uuid": "ede489ff-b027-469a-b482-b9f33ca71fcb",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "999f865e-f544-467f-b7e8-732fb33862f3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-15T01:58:22.509Z_

```json
{
  "parentUuid": "ede489ff-b027-469a-b482-b9f33ca71fcb",
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
  "uuid": "4e00c71e-9c91-45b5-b141-bc13aaf894d6",
  "timestamp": "2026-05-15T01:58:22.509Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "999f865e-f544-467f-b7e8-732fb33862f3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-15T01:58:22.509Z_

```json
{
  "parentUuid": "4e00c71e-9c91-45b5-b141-bc13aaf894d6",
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
  "uuid": "129cd16e-82dc-4399-9b6c-bba7493601bc",
  "timestamp": "2026-05-15T01:58:22.509Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "999f865e-f544-467f-b7e8-732fb33862f3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 6 · 2026-05-15T01:58:22.509Z_

```json
{
  "parentUuid": "129cd16e-82dc-4399-9b6c-bba7493601bc",
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
  "uuid": "7fef89c9-1da6-4884-bf79-9e80f8e9cc29",
  "timestamp": "2026-05-15T01:58:22.509Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "999f865e-f544-467f-b7e8-732fb33862f3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 7 · 2026-05-15T01:58:22.509Z_

```json
{
  "parentUuid": "7fef89c9-1da6-4884-bf79-9e80f8e9cc29",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "7e2a7d40-0582-419f-9df7-0e75274166f7",
  "timestamp": "2026-05-15T01:58:22.509Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "999f865e-f544-467f-b7e8-732fb33862f3",
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
  "aiTitle": "Review Claim 2 wording defensiveness",
  "sessionId": "999f865e-f544-467f-b7e8-732fb33862f3"
}
```

---

### Assistant

_source line 9 · 2026-05-15T01:58:25.649Z_

I'll start by reading the required project files and checking for paper drafts.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7e2a7d40-0582-419f-9df7-0e75274166f7",
  "isSidechain": false,
  "requestId": "req_011Cb3XUR3rGTZKaZkRiZAFW",
  "type": "assistant",
  "uuid": "47883ea3-d8b6-47dc-9cab-a5b3648abfb5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "999f865e-f544-467f-b7e8-732fb33862f3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FS2MqcqTZLDRvYnHB1h91M",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 11778,
      "cache_read_input_tokens": 11447,
      "output_tokens": 105,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11778,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 105,
          "cache_read_input_tokens": 11447,
          "cache_creation_input_tokens": 11778,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11778
          },
          "type": "message"
        }
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

_source line 10 · 2026-05-15T01:58:26.408Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01RER9m1p9VpxkaWmoFqDTMQ`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_project_file",
  "max_results": 1
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "47883ea3-d8b6-47dc-9cab-a5b3648abfb5",
  "isSidechain": false,
  "requestId": "req_011Cb3XUR3rGTZKaZkRiZAFW",
  "type": "assistant",
  "uuid": "95668e43-43cc-440f-a99e-57d776300614",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "999f865e-f544-467f-b7e8-732fb33862f3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FS2MqcqTZLDRvYnHB1h91M",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 11778,
      "cache_read_input_tokens": 11447,
      "output_tokens": 105,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11778,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 105,
          "cache_read_input_tokens": 11447,
          "cache_creation_input_tokens": 11778,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11778
          },
          "type": "message"
        }
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

_source line 11 · 2026-05-15T01:58:26.415Z_

<details><summary>↩ Tool result · `toolu_01RER9m1p9VpxkaWmoFqDTMQ`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__read_project_file"
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "95668e43-43cc-440f-a99e-57d776300614",
  "isSidechain": false,
  "promptId": "82620338-1cd7-4c43-9283-e5cb821c1607",
  "type": "user",
  "uuid": "aa417dfd-2731-4fa4-9d1f-8fc930966d35",
  "toolUseResult": {
    "matches": [
      "mcp__agent-ml-research__read_project_file"
    ],
    "query": "select:mcp__agent-ml-research__read_project_file",
    "total_deferred_tools": 22
  },
  "sourceToolAssistantUUID": "95668e43-43cc-440f-a99e-57d776300614",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "999f865e-f544-467f-b7e8-732fb33862f3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 12 · 2026-05-15T01:58:29.180Z_

<details><summary>Logged reasoning block</summary>

```text
Let me read the required files in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "aa417dfd-2731-4fa4-9d1f-8fc930966d35",
  "isSidechain": false,
  "requestId": "req_011Cb3XUhYYRP14fAkJQ69vq",
  "type": "assistant",
  "uuid": "3839f3fb-9f17-4a85-bf23-7905e7dc0ad1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "999f865e-f544-467f-b7e8-732fb33862f3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CUfZNRE2BoQZoU1vFgpc6x",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 451,
      "cache_read_input_tokens": 23225,
      "output_tokens": 309,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 451,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 309,
          "cache_read_input_tokens": 23225,
          "cache_creation_input_tokens": 451,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 451
          },
          "type": "message"
        }
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

_source line 13 · 2026-05-15T01:58:30.041Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01WGYmUy3JZDMHu3ovBx6xHJ`</summary>

```json
{
  "project": "structfuse-context",
  "file": "paper_framing.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3839f3fb-9f17-4a85-bf23-7905e7dc0ad1",
  "isSidechain": false,
  "requestId": "req_011Cb3XUhYYRP14fAkJQ69vq",
  "type": "assistant",
  "uuid": "1cc9e485-4247-4028-8da6-f6a72531e4b9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "999f865e-f544-467f-b7e8-732fb33862f3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CUfZNRE2BoQZoU1vFgpc6x",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 451,
      "cache_read_input_tokens": 23225,
      "output_tokens": 309,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 451,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 309,
          "cache_read_input_tokens": 23225,
          "cache_creation_input_tokens": 451,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 451
          },
          "type": "message"
        }
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

_source line 14 · 2026-05-15T01:58:30.057Z_

<details><summary>↩ Tool result · `toolu_01WGYmUy3JZDMHu3ovBx6xHJ`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/paper_framing.md\", \"content\": \"# Paper Framing — StructFuse\\n\\n## Target Venue\\n- Primary: EMNLP 2026 Main\\n- Deadline: ARR May 25, 2026\\n\\n## Core Claims (3)\\n\\n1. **Simple static embedding-distance mining suffices for contrastive code retrieval, challenging the assumption that expensive gradient-based hard negative methods are necessary.** CoCoHaNeRe (ACM TOSEM 2025) argues non-differentiable embedding negatives are \\\"slow and ineffective\\\" compared to gradient-based methods — our results show that in structural code retrieval, simple embedding-distance mining yields +1.6–2.0pp R@1 over random baselines across two decoder-only encoders with distinct pretraining corpora and representation geometries (Qwen2.5-Coder-3B, StarCoder2-3B), without requiring gradient-based mechanisms.\\n\\n2. **[Exploratory observation] Structure-grounded (dataflow) negatives interact with encoder representation geometry, but do not consistently outperform embedding mining.** Pilot data shows dataflow < embedding on both encoders (Qwen: -1.2pp, StarCoder: -1.0pp R@1 vs embedding). The interaction pattern — Qwen (saturated, pos_sim > 0.98) shows smaller gap than StarCoder (healthy, pos_sim ~ 0.80) — suggests representation geometry mediates strategy effectiveness. neg_difficulty margin analysis (+17% Qwen, +28% StarCoder) provides mechanistic evidence for this interaction. Pending: multi-seed confirmation + plan_005 stratified analysis + plan_015 dynamic mining control. This is reported as an observation with mechanistic hypothesis, not an established finding.\\n\\n3. **Scope-bounded inter-procedural data-flow analysis via CodeQL provides a practical pipeline for computing structural connectivity at scale.** 0% timeout, 78% connected-not-gold rate (Z%), 123/131 repos with output at full scale. [Dream [M][W] flag: this is supporting methodology, not a primary research contribution. Drop speculative generalization claims (molecular networks, etc.) — no evidence. Frame as practical tool that enables the study, not a standalone contribution.]\\n\\n## Story Spine\\n\\n- **Problem**: Repo-level code repair requires selecting relevant files from large codebases. Current retrievers rely on text similarity alone, but lexical similarity ≠ structural relevance. Hard negative mining is the standard approach to improve contrastive retrievers, yet the field lacks systematic understanding of what negative selection strategies work for code and why.\\n\\n- **Existing approaches & gaps**:\\n  - Text-based retrieval (SweRank, SWE-Fixer): blind to structural dependencies\\n  - Graph-guided at inference (LocAgent, RANGER, CodexGraph): structural graphs at inference only, no training signal\\n  - ARISE: data-flow but intra-procedural only (no call boundary crossing), runtime tool calls only\\n  - CoCoHaNeRe (ACM TOSEM 2025): argues gradient-based hard negative methods outperform non-differentiable embedding negatives — but does not test simple static embedding-distance mining in structural code retrieval settings\\n  - Gap: no systematic study comparing negative mining strategies with proper controls, and no mechanistic explanation for when/why each strategy works\\n\\n- **Our contribution**: A systematic analysis of hard negative mining strategies for contrastive code retrieval. We (1) show that simple static embedding-distance mining suffices, challenging the assumption that expensive gradient-based methods are necessary (CoCoHaNeRe's premise), (2) observe that structure-grounded (dataflow) negatives interact with encoder representation geometry and provide mechanistic analysis of when/why different strategies yield different outcomes, and (3) validate findings on downstream SWE-bench task evaluation.\\n\\n- **Headline result template**: \\\"Simple static embedding-distance mining consistently improves code retrieval (+1.6–2.0pp R@1, 2 encoders), challenging the need for expensive gradient-based hard negative methods. Structure-grounded (dataflow) negatives show encoder-dependent interaction patterns — representation geometry analysis via negative difficulty provides mechanistic explanation for when different mining strategies are effective.\\\"\\n\\n## Core Insight\\n\\nThe effectiveness of hard negative mining strategies depends on the encoder's representation geometry. When the pretrained space is saturated (high pos_sim → low margin between positive and negative), the encoder needs harder negatives from an orthogonal signal dimension (structure). When the space has healthy separation, embedding-distance mining alone captures sufficient difficulty gradient. This encoder-strategy interaction explains contradictory findings in prior work.\\n\\n## Dual-Pillar Motivation\\n\\n1. **Primary — Systematic analysis challenging gradient-based assumptions**: Prior work (CoCoHaNeRe, ACM TOSEM 2025) assumes expensive gradient-based hard negative methods are necessary for effective code search. Our controlled comparison shows simple static embedding-distance mining suffices in structural code retrieval, isolating the effect of each strategy.\\n2. **Secondary — Mechanistic explanation via representation geometry**: neg_difficulty analysis (margin distribution × strategy × encoder) provides explanatory depth beyond empirical comparison, enabling practitioners to predict which strategy suits their encoder without exhaustive experiments.\\n\\n## Formal Definition\\n\\nGiven retrieval domain D, structural graph G, similarity function s, query q:\\n**structure-grounded hard negative** = argmax_{x ∈ D : s(x,q) > τ ∧ ¬reachable_G(x,q)} s(x,q)\\n\\nThe structural graph is externally fixed and does not update with the encoder (drift-immune).\\n\\n## Title Options\\n\\n- Primary: \\\"What Makes Hard Negatives Work for Code Retrieval? A Systematic Study of Mining Strategies and Representation Geometry\\\"\\n- Alternative: \\\"Beyond Gradient-Based Mining: Static Embedding Negatives Suffice for Contrastive Code Retrieval\\\" [contingent: activate only if M2 dataflow conditional benefit confirmed across encoders]\\n- Backup: \\\"Simple Embedding Mining Suffices: Challenging Gradient-Based Assumptions in Hard Negative Mining for Code\\\"\\n\\n## Venue Fit\\n\\n1. **EMNLP Main fit**: Empirical analysis + mechanistic insight papers are a strong EMNLP archetype (cf. \\\"Do Language Models...\\\" papers). Contribution is understanding, not just a new method.\\n2. **NLP audience**: Frame as contrastive learning methodology with code as instantiation. Representation geometry analysis generalizes beyond code.\\n3. **Against \\\"incremental\\\" criticism**: Paper challenges a prevalent assumption + provides mechanistic explanation for strategy × encoder interaction + validates on downstream task. Three contributions, not one marginal improvement.\\n\\n## Anticipated Reviewer Concerns\\n\\n| Concern | Response | Evidence |\\n|---------|----------|----------|\\n| Only 2 encoders — can you generalize? | n=2 is minimum for interaction claim; we frame as observation with mechanism, not universal law; two decoder-only encoders with distinct pretraining (Fill vs FIM) and representation geometry (pos_sim 0.99 vs 0.80) provide meaningful variation | plan_013 (done), m2_full runs |\\n| BM25 vs true embedding negatives? | Run BM25 negatives to empirically compare with embedding-distance mining, grounding the comparison against CoCoHaNeRe's gradient-based premise | plan_018 |\\n| Pool size sensitivity? | Evaluate at pool {50, 100, 200, 500} to confirm strategy rankings hold at realistic sizes | plan_019 |\\n| Stratified by structural data availability? | Report per-stratum R@1 for 34% with structural data vs 66% fallback | plan_005 (extended) |\\n| Temperature regime specificity | Ablate τ ∈ {0.05, 0.1, 0.2} | plan_014 |\\n| No downstream task evaluation | SWE-bench Lite end-to-end with LLM agent | plan_003 |\\n| Static vs dynamic mining confound | Clarify mining is static; add dynamic baseline | plan_015 |\\n| CodeQL scalability at larger scale | 0% timeout, 78% Z%, 123 repos; m1_reextract_v2 adds more | plan_006 (done) |\\n| Why not compare inference-time graph methods? | Complementary: they navigate at inference, we mine at training. Discuss relationship. | plan_017 |\\n| Single benchmark | Add RepoBench-R cross-file retrieval | plan_004 |\\n| Statistical significance | Bootstrap 95% CI for all comparisons; full M2 = 9 seeds × 3 strategies × 2 encoders | plan_016, m2_full |\\n| \\\"Complementary signal\\\" overstatement | Temper: \\\"conditionally beneficial\\\" not \\\"always complementary\\\" | Writing discipline |\\n| Missing related work | RepoFusion, GRACE, GraphCodeBERT, ANCE, curriculum HN mining | Writing task |\\n\\n## Evidence Status\\n\\n### Confirmed findings (basis for claims):\\n- D017: True embedding mining helps (+2.0pp Qwen, +1.6pp StarCoder) — challenges gradient-based necessity assumption\\n- D021/neg_difficulty: Qwen pos_sim=0.9855 (saturated), StarCoder pos_sim=0.7985 (healthy); margin differential explains strategy interaction\\n- m2_embed_verify (pilot): 3-strategy comparison confirms ranking (embedding > random, dataflow conditional)\\n- plan_013 (StarCoder pilot): Confirms cross-encoder pattern — embedding helps both, dataflow helps Qwen only\\n- plan_006: CodeQL scalability confirmed at 123-repo scale\\n\\n### In progress:\\n- m2_full_qwen: random s42 DONE (R@1=0.5527), s43 DONE (R@1=0.5554), s44 RUNNING (eval@500 R@1=0.6009). 2/10 runs complete, ~50h remaining.\\n- m2_full_starcoder: random s42 DONE (R@1=0.4604, from parent), s43 RUNNING (eval@500 R@1=0.4708). 1/9+ runs complete, ~65-70h remaining.\\n- m1_reextract_v2: 80.8% complete (22,842/28,276), 0 ERROR, ETA ~15:00 CST May 15\\n\\n### Planned (priority order):\\n- plan_018: BM25 negative baseline (Dream #1 consensus gap — grounds comparison against CoCoHaNeRe's premise)\\n- plan_003: SWE-bench Lite eval (biggest lever for paper strength)\\n- plan_019: Pool size sensitivity (Dream consensus — external validity)\\n- plan_014: Temperature ablation (Dream reviewer concern)\\n- plan_004: RepoBench-R second benchmark (with multi-seed CIs)\\n- plan_015: Dynamic mining baseline\\n- plan_005: Stratified analysis (extended: structural-available vs fallback stratum)\\n- plan_007/008/009: Additional ablations\\n\\n## Contingency (if full M2 results weaken claims)\\n\\n### All 18 runs confirm pilot pattern: Best case\\n- Full statistical power, paper as framed above\\n- Target: EMNLP Main\\n\\n### Dataflow benefit disappears even for Qwen at full scale: Pivot to 2-claim paper\\n- Drop Claim 2 to analysis observation\\n- Paper becomes: \\\"Simple embedding mining suffices (challenging gradient-based assumption) + CodeQL extraction is practical + representation geometry analysis explains prior contradictions\\\"\\n- Still publishable: challenging gradient-based assumption + mechanistic analysis is sufficient for EMNLP Main\\n\\n### BM25 negatives ≈ random (not harmful): Narrative pivot needed [D030 contingency]\\n- If plan_018 shows BM25 negatives perform ≈ random (not << random), the \\\"challenging gradient-based assumption\\\" narrative needs adjustment\\n- Pivot: \\\"systematic comparison reveals embedding-distance mining is the only strategy that consistently helps; gradient-based methods may not be necessary even when BM25 provides no signal\\\"\\n- Paper remains valid as systematic analysis — the core finding (simple embedding mining suffices) stands regardless of BM25 outcome\\n- Claim 1 core preserved: \\\"Simple static embedding-distance mining consistently improves code retrieval without gradient-based mechanisms\\\"\\n- Impact: BM25 result determines narrative nuance, not core contribution\\n\\n### Embedding mining also loses advantage at full scale: Major reassessment needed\\n- Recheck data pipeline for bugs (full-scale data may have distribution differences)\\n- If confirmed: negative result paper — \\\"Why Hard Negative Mining Doesn't Scale for Code Retrieval\\\"\\n- Discuss with user before committing direction\\n\\n## Deprecated Claims (with reason)\\n\\n- ~~\\\"Embedding-distance hard negatives actively harm code retrieval\\\"~~ — FALSIFIED by D017. Original evidence (-27pp R@1) was from BM25-proxy negatives incorrectly labeled as embedding_distance in MVP. True embedding mining shows consistent improvement. Preserved here to prevent regression.\\n\", \"total_chars\": 12022, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1cc9e485-4247-4028-8da6-f6a72531e4b9",
  "isSidechain": false,
  "promptId": "82620338-1cd7-4c43-9283-e5cb821c1607",
  "type": "user",
  "uuid": "874ca8da-36fd-48c5-8ed7-96186291e181",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"path\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/paper_framing.md\\\", \\\"content\\\": \\\"# Paper Framing — StructFuse\\\\n\\\\n## Target Venue\\\\n- Primary: EMNLP 2026 Main\\\\n- Deadline: ARR May 25, 2026\\\\n\\\\n## Core Claims (3)\\\\n\\\\n1. **Simple static embedding-distance mining suffices for contrastive code retrieval, challenging the assumption that expensive gradient-based hard negative methods are necessary.** CoCoHaNeRe (ACM TOSEM 2025) argues non-differentiable embedding negatives are \\\\\\\"slow and ineffective\\\\\\\" compared to gradient-based methods — our results show that in structural code retrieval, simple embedding-distance mining yields +1.6–2.0pp R@1 over random baselines across two decoder-only encoders with distinct pretraining corpora and representation geometries (Qwen2.5-Coder-3B, StarCoder2-3B), without requiring gradient-based mechanisms.\\\\n\\\\n2. **[Exploratory observation] Structure-grounded (dataflow) negatives interact with encoder representation geometry, but do not consistently outperform embedding mining.** Pilot data shows dataflow < embedding on both encoders (Qwen: -1.2pp, StarCoder: -1.0pp R@1 vs embedding). The interaction pattern — Qwen (saturated, pos_sim > 0.98) shows smaller gap than StarCoder (healthy, pos_sim ~ 0.80) — suggests representation geometry mediates strategy effectiveness. neg_difficulty margin analysis (+17% Qwen, +28% StarCoder) provides mechanistic evidence for this interaction. Pending: multi-seed confirmation + plan_005 stratified analysis + plan_015 dynamic mining control. This is reported as an observation with mechanistic hypothesis, not an established finding.\\\\n\\\\n3. **Scope-bounded inter-procedural data-flow analysis via CodeQL provides a practical pipeline for computing structural connectivity at scale.** 0% timeout, 78% connected-not-gold rate (Z%), 123/131 repos with output at full scale. [Dream [M][W] flag: this is supporting methodology, not a primary research contribution. Drop speculative generalization claims (molecular networks, etc.) — no evidence. Frame as practical tool that enables the study, not a standalone contribution.]\\\\n\\\\n## Story Spine\\\\n\\\\n- **Problem**: Repo-level code repair requires selecting relevant files from large codebases. Current retrievers rely on text similarity alone, but lexical similarity ≠ structural relevance. Hard negative mining is the standard approach to improve contrastive retrievers, yet the field lacks systematic understanding of what negative selection strategies work for code and why.\\\\n\\\\n- **Existing approaches & gaps**:\\\\n  - Text-based retrieval (SweRank, SWE-Fixer): blind to structural dependencies\\\\n  - Graph-guided at inference (LocAgent, RANGER, CodexGraph): structural graphs at inference only, no training signal\\\\n  - ARISE: data-flow but intra-procedural only (no call boundary crossing), runtime tool calls only\\\\n  - CoCoHaNeRe (ACM TOSEM 2025): argues gradient-based hard negative methods outperform non-differentiable embedding negatives — but does not test simple static embedding-distance mining in structural code retrieval settings\\\\n  - Gap: no systematic study comparing negative mining strategies with proper controls, and no mechanistic explanation for when/why each strategy works\\\\n\\\\n- **Our contribution**: A systematic analysis of hard negative mining strategies for contrastive code retrieval. We (1) show that simple static embedding-distance mining suffices, challenging the assumption that expensive gradient-based methods are necessary (CoCoHaNeRe's premise), (2) observe that structure-grounded (dataflow) negatives interact with encoder representation geometry and provide mechanistic analysis of when/why different strategies yield different outcomes, and (3) validate findings on downstream SWE-bench task evaluation.\\\\n\\\\n- **Headline result template**: \\\\\\\"Simple static embedding-distance mining consistently improves code retrieval (+1.6–2.0pp R@1, 2 encoders), challenging the need for expensive gradient-based hard negative methods. Structure-grounded (dataflow) negatives show encoder-dependent interaction patterns — representation geometry analysis via negative difficulty provides mechanistic explanation for when different mining strategies are effective.\\\\\\\"\\\\n\\\\n## Core Insight\\\\n\\\\nThe effectiveness of hard negative mining strategies depends on the encoder's representation geometry. When the pretrained space is saturated (high pos_sim → low margin between positive and negative), the encoder needs harder negatives from an orthogonal signal dimension (structure). When the space has healthy separation, embedding-distance mining alone captures sufficient difficulty gradient. This encoder-strategy interaction explains contradictory findings in prior work.\\\\n\\\\n## Dual-Pillar Motivation\\\\n\\\\n1. **Primary — Systematic analysis challenging gradient-based assumptions**: Prior work (CoCoHaNeRe, ACM TOSEM 2025) assumes expensive gradient-based hard negative methods are necessary for effective code search. Our controlled comparison shows simple static embedding-distance mining suffices in structural code retrieval, isolating the effect of each strategy.\\\\n2. **Secondary — Mechanistic explanation via representation geometry**: neg_difficulty analysis (margin distribution × strategy × encoder) provides explanatory depth beyond empirical comparison, enabling practitioners to predict which strategy suits their encoder without exhaustive experiments.\\\\n\\\\n## Formal Definition\\\\n\\\\nGiven retrieval domain D, structural graph G, similarity function s, query q:\\\\n**structure-grounded hard negative** = argmax_{x ∈ D : s(x,q) > τ ∧ ¬reachable_G(x,q)} s(x,q)\\\\n\\\\nThe structural graph is externally fixed and does not update with the encoder (drift-immune).\\\\n\\\\n## Title Options\\\\n\\\\n- Primary: \\\\\\\"What Makes Hard Negatives Work for Code Retrieval? A Systematic Study of Mining Strategies and Representation Geometry\\\\\\\"\\\\n- Alternative: \\\\\\\"Beyond Gradient-Based Mining: Static Embedding Negatives Suffice for Contrastive Code Retrieval\\\\\\\" [contingent: activate only if M2 dataflow conditional benefit confirmed across encoders]\\\\n- Backup: \\\\\\\"Simple Embedding Mining Suffices: Challenging Gradient-Based Assumptions in Hard Negative Mining for Code\\\\\\\"\\\\n\\\\n## Venue Fit\\\\n\\\\n1. **EMNLP Main fit**: Empirical analysis + mechanistic insight papers are a strong EMNLP archetype (cf. \\\\\\\"Do Language Models...\\\\\\\" papers). Contribution is understanding, not just a new method.\\\\n2. **NLP audience**: Frame as contrastive learning methodology with code as instantiation. Representation geometry analysis generalizes beyond code.\\\\n3. **Against \\\\\\\"incremental\\\\\\\" criticism**: Paper challenges a prevalent assumption + provides mechanistic explanation for strategy × encoder interaction + validates on downstream task. Three contributions, not one marginal improvement.\\\\n\\\\n## Anticipated Reviewer Concerns\\\\n\\\\n| Concern | Response | Evidence |\\\\n|---------|----------|----------|\\\\n| Only 2 encoders — can you generalize? | n=2 is minimum for interaction claim; we frame as observation with mechanism, not universal law; two decoder-only encoders with distinct pretraining (Fill vs FIM) and representation geometry (pos_sim 0.99 vs 0.80) provide meaningful variation | plan_013 (done), m2_full runs |\\\\n| BM25 vs true embedding negatives? | Run BM25 negatives to empirically compare with embedding-distance mining, grounding the comparison against CoCoHaNeRe's gradient-based premise | plan_018 |\\\\n| Pool size sensitivity? | Evaluate at pool {50, 100, 200, 500} to confirm strategy rankings hold at realistic sizes | plan_019 |\\\\n| Stratified by structural data availability? | Report per-stratum R@1 for 34% with structural data vs 66% fallback | plan_005 (extended) |\\\\n| Temperature regime specificity | Ablate τ ∈ {0.05, 0.1, 0.2} | plan_014 |\\\\n| No downstream task evaluation | SWE-bench Lite end-to-end with LLM agent | plan_003 |\\\\n| Static vs dynamic mining confound | Clarify mining is static; add dynamic baseline | plan_015 |\\\\n| CodeQL scalability at larger scale | 0% timeout, 78% Z%, 123 repos; m1_reextract_v2 adds more | plan_006 (done) |\\\\n| Why not compare inference-time graph methods? | Complementary: they navigate at inference, we mine at training. Discuss relationship. | plan_017 |\\\\n| Single benchmark | Add RepoBench-R cross-file retrieval | plan_004 |\\\\n| Statistical significance | Bootstrap 95% CI for all comparisons; full M2 = 9 seeds × 3 strategies × 2 encoders | plan_016, m2_full |\\\\n| \\\\\\\"Complementary signal\\\\\\\" overstatement | Temper: \\\\\\\"conditionally beneficial\\\\\\\" not \\\\\\\"always complementary\\\\\\\" | Writing discipline |\\\\n| Missing related work | RepoFusion, GRACE, GraphCodeBERT, ANCE, curriculum HN mining | Writing task |\\\\n\\\\n## Evidence Status\\\\n\\\\n### Confirmed findings (basis for claims):\\\\n- D017: True embedding mining helps (+2.0pp Qwen, +1.6pp StarCoder) — challenges gradient-based necessity assumption\\\\n- D021/neg_difficulty: Qwen pos_sim=0.9855 (saturated), StarCoder pos_sim=0.7985 (healthy); margin differential explains strategy interaction\\\\n- m2_embed_verify (pilot): 3-strategy comparison confirms ranking (embedding > random, dataflow conditional)\\\\n- plan_013 (StarCoder pilot): Confirms cross-encoder pattern — embedding helps both, dataflow helps Qwen only\\\\n- plan_006: CodeQL scalability confirmed at 123-repo scale\\\\n\\\\n### In progress:\\\\n- m2_full_qwen: random s42 DONE (R@1=0.5527), s43 DONE (R@1=0.5554), s44 RUNNING (eval@500 R@1=0.6009). 2/10 runs complete, ~50h remaining.\\\\n- m2_full_starcoder: random s42 DONE (R@1=0.4604, from parent), s43 RUNNING (eval@500 R@1=0.4708). 1/9+ runs complete, ~65-70h remaining.\\\\n- m1_reextract_v2: 80.8% complete (22,842/28,276), 0 ERROR, ETA ~15:00 CST May 15\\\\n\\\\n### Planned (priority order):\\\\n- plan_018: BM25 negative baseline (Dream #1 consensus gap — grounds comparison against CoCoHaNeRe's premise)\\\\n- plan_003: SWE-bench Lite eval (biggest lever for paper strength)\\\\n- plan_019: Pool size sensitivity (Dream consensus — external validity)\\\\n- plan_014: Temperature ablation (Dream reviewer concern)\\\\n- plan_004: RepoBench-R second benchmark (with multi-seed CIs)\\\\n- plan_015: Dynamic mining baseline\\\\n- plan_005: Stratified analysis (extended: structural-available vs fallback stratum)\\\\n- plan_007/008/009: Additional ablations\\\\n\\\\n## Contingency (if full M2 results weaken claims)\\\\n\\\\n### All 18 runs confirm pilot pattern: Best case\\\\n- Full statistical power, paper as framed above\\\\n- Target: EMNLP Main\\\\n\\\\n### Dataflow benefit disappears even for Qwen at full scale: Pivot to 2-claim paper\\\\n- Drop Claim 2 to analysis observation\\\\n- Paper becomes: \\\\\\\"Simple embedding mining suffices (challenging gradient-based assumption) + CodeQL extraction is practical + representation geometry analysis explains prior contradictions\\\\\\\"\\\\n- Still publishable: challenging gradient-based assumption + mechanistic analysis is sufficient for EMNLP Main\\\\n\\\\n### BM25 negatives ≈ random (not harmful): Narrative pivot needed [D030 contingency]\\\\n- If plan_018 shows BM25 negatives perform ≈ random (not << random), the \\\\\\\"challenging gradient-based assumption\\\\\\\" narrative needs adjustment\\\\n- Pivot: \\\\\\\"systematic comparison reveals embedding-distance mining is the only strategy that consistently helps; gradient-based methods may not be necessary even when BM25 provides no signal\\\\\\\"\\\\n- Paper remains valid as systematic analysis — the core finding (simple embedding mining suffices) stands regardless of BM25 outcome\\\\n- Claim 1 core preserved: \\\\\\\"Simple static embedding-distance mining consistently improves code retrieval without gradient-based mechanisms\\\\\\\"\\\\n- Impact: BM25 result determines narrative nuance, not core contribution\\\\n\\\\n### Embedding mining also loses advantage at full scale: Major reassessment needed\\\\n- Recheck data pipeline for bugs (full-scale data may have distribution differences)\\\\n- If confirmed: negative result paper — \\\\\\\"Why Hard Negative Mining Doesn't Scale for Code Retrieval\\\\\\\"\\\\n- Discuss with user before committing direction\\\\n\\\\n## Deprecated Claims (with reason)\\\\n\\\\n- ~~\\\\\\\"Embedding-distance hard negatives actively harm code retrieval\\\\\\\"~~ — FALSIFIED by D017. Original evidence (-27pp R@1) was from BM25-proxy negatives incorrectly labeled as embedding_distance in MVP. True embedding mining shows consistent improvement. Preserved here to prevent regression.\\\\n\\\", \\\"total_chars\\\": 12022, \\\"truncated\\\": false}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/paper_framing.md\", \"content\": \"# Paper Framing — StructFuse\\n\\n## Target Venue\\n- Primary: EMNLP 2026 Main\\n- Deadline: ARR May 25, 2026\\n\\n## Core Claims (3)\\n\\n1. **Simple static embedding-distance mining suffices for contrastive code retrieval, challenging the assumption that expensive gradient-based hard negative methods are necessary.** CoCoHaNeRe (ACM TOSEM 2025) argues non-differentiable embedding negatives are \\\"slow and ineffective\\\" compared to gradient-based methods — our results show that in structural code retrieval, simple embedding-distance mining yields +1.6–2.0pp R@1 over random baselines across two decoder-only encoders with distinct pretraining corpora and representation geometries (Qwen2.5-Coder-3B, StarCoder2-3B), without requiring gradient-based mechanisms.\\n\\n2. **[Exploratory observation] Structure-grounded (dataflow) negatives interact with encoder representation geometry, but do not consistently outperform embedding mining.** Pilot data shows dataflow < embedding on both encoders (Qwen: -1.2pp, StarCoder: -1.0pp R@1 vs embedding). The interaction pattern — Qwen (saturated, pos_sim > 0.98) shows smaller gap than StarCoder (healthy, pos_sim ~ 0.80) — suggests representation geometry mediates strategy effectiveness. neg_difficulty margin analysis (+17% Qwen, +28% StarCoder) provides mechanistic evidence for this interaction. Pending: multi-seed confirmation + plan_005 stratified analysis + plan_015 dynamic mining control. This is reported as an observation with mechanistic hypothesis, not an established finding.\\n\\n3. **Scope-bounded inter-procedural data-flow analysis via CodeQL provides a practical pipeline for computing structural connectivity at scale.** 0% timeout, 78% connected-not-gold rate (Z%), 123/131 repos with output at full scale. [Dream [M][W] flag: this is supporting methodology, not a primary research contribution. Drop speculative generalization claims (molecular networks, etc.) — no evidence. Frame as practical tool that enables the study, not a standalone contribution.]\\n\\n## Story Spine\\n\\n- **Problem**: Repo-level code repair requires selecting relevant files from large codebases. Current retrievers rely on text similarity alone, but lexical similarity ≠ structural relevance. Hard negative mining is the standard approach to improve contrastive retrievers, yet the field lacks systematic understanding of what negative selection strategies work for code and why.\\n\\n- **Existing approaches & gaps**:\\n  - Text-based retrieval (SweRank, SWE-Fixer): blind to structural dependencies\\n  - Graph-guided at inference (LocAgent, RANGER, CodexGraph): structural graphs at inference only, no training signal\\n  - ARISE: data-flow but intra-procedural only (no call boundary crossing), runtime tool calls only\\n  - CoCoHaNeRe (ACM TOSEM 2025): argues gradient-based hard negative methods outperform non-differentiable embedding negatives — but does not test simple static embedding-distance mining in structural code retrieval settings\\n  - Gap: no systematic study comparing negative mining strategies with proper controls, and no mechanistic explanation for when/why each strategy works\\n\\n- **Our contribution**: A systematic analysis of hard negative mining strategies for contrastive code retrieval. We (1) show that simple static embedding-distance mining suffices, challenging the assumption that expensive gradient-based methods are necessary (CoCoHaNeRe's premise), (2) observe that structure-grounded (dataflow) negatives interact with encoder representation geometry and provide mechanistic analysis of when/why different strategies yield different outcomes, and (3) validate findings on downstream SWE-bench task evaluation.\\n\\n- **Headline result template**: \\\"Simple static embedding-distance mining consistently improves code retrieval (+1.6–2.0pp R@1, 2 encoders), challenging the need for expensive gradient-based hard negative methods. Structure-grounded (dataflow) negatives show encoder-dependent interaction patterns — representation geometry analysis via negative difficulty provides mechanistic explanation for when different mining strategies are effective.\\\"\\n\\n## Core Insight\\n\\nThe effectiveness of hard negative mining strategies depends on the encoder's representation geometry. When the pretrained space is saturated (high pos_sim → low margin between positive and negative), the encoder needs harder negatives from an orthogonal signal dimension (structure). When the space has healthy separation, embedding-distance mining alone captures sufficient difficulty gradient. This encoder-strategy interaction explains contradictory findings in prior work.\\n\\n## Dual-Pillar Motivation\\n\\n1. **Primary — Systematic analysis challenging gradient-based assumptions**: Prior work (CoCoHaNeRe, ACM TOSEM 2025) assumes expensive gradient-based hard negative methods are necessary for effective code search. Our controlled comparison shows simple static embedding-distance mining suffices in structural code retrieval, isolating the effect of each strategy.\\n2. **Secondary — Mechanistic explanation via representation geometry**: neg_difficulty analysis (margin distribution × strategy × encoder) provides explanatory depth beyond empirical comparison, enabling practitioners to predict which strategy suits their encoder without exhaustive experiments.\\n\\n## Formal Definition\\n\\nGiven retrieval domain D, structural graph G, similarity function s, query q:\\n**structure-grounded hard negative** = argmax_{x ∈ D : s(x,q) > τ ∧ ¬reachable_G(x,q)} s(x,q)\\n\\nThe structural graph is externally fixed and does not update with the encoder (drift-immune).\\n\\n## Title Options\\n\\n- Primary: \\\"What Makes Hard Negatives Work for Code Retrieval? A Systematic Study of Mining Strategies and Representation Geometry\\\"\\n- Alternative: \\\"Beyond Gradient-Based Mining: Static Embedding Negatives Suffice for Contrastive Code Retrieval\\\" [contingent: activate only if M2 dataflow conditional benefit confirmed across encoders]\\n- Backup: \\\"Simple Embedding Mining Suffices: Challenging Gradient-Based Assumptions in Hard Negative Mining for Code\\\"\\n\\n## Venue Fit\\n\\n1. **EMNLP Main fit**: Empirical analysis + mechanistic insight papers are a strong EMNLP archetype (cf. \\\"Do Language Models...\\\" papers). Contribution is understanding, not just a new method.\\n2. **NLP audience**: Frame as contrastive learning methodology with code as instantiation. Representation geometry analysis generalizes beyond code.\\n3. **Against \\\"incremental\\\" criticism**: Paper challenges a prevalent assumption + provides mechanistic explanation for strategy × encoder interaction + validates on downstream task. Three contributions, not one marginal improvement.\\n\\n## Anticipated Reviewer Concerns\\n\\n| Concern | Response | Evidence |\\n|---------|----------|----------|\\n| Only 2 encoders — can you generalize? | n=2 is minimum for interaction claim; we frame as observation with mechanism, not universal law; two decoder-only encoders with distinct pretraining (Fill vs FIM) and representation geometry (pos_sim 0.99 vs 0.80) provide meaningful variation | plan_013 (done), m2_full runs |\\n| BM25 vs true embedding negatives? | Run BM25 negatives to empirically compare with embedding-distance mining, grounding the comparison against CoCoHaNeRe's gradient-based premise | plan_018 |\\n| Pool size sensitivity? | Evaluate at pool {50, 100, 200, 500} to confirm strategy rankings hold at realistic sizes | plan_019 |\\n| Stratified by structural data availability? | Report per-stratum R@1 for 34% with structural data vs 66% fallback | plan_005 (extended) |\\n| Temperature regime specificity | Ablate τ ∈ {0.05, 0.1, 0.2} | plan_014 |\\n| No downstream task evaluation | SWE-bench Lite end-to-end with LLM agent | plan_003 |\\n| Static vs dynamic mining confound | Clarify mining is static; add dynamic baseline | plan_015 |\\n| CodeQL scalability at larger scale | 0% timeout, 78% Z%, 123 repos; m1_reextract_v2 adds more | plan_006 (done) |\\n| Why not compare inference-time graph methods? | Complementary: they navigate at inference, we mine at training. Discuss relationship. | plan_017 |\\n| Single benchmark | Add RepoBench-R cross-file retrieval | plan_004 |\\n| Statistical significance | Bootstrap 95% CI for all comparisons; full M2 = 9 seeds × 3 strategies × 2 encoders | plan_016, m2_full |\\n| \\\"Complementary signal\\\" overstatement | Temper: \\\"conditionally beneficial\\\" not \\\"always complementary\\\" | Writing discipline |\\n| Missing related work | RepoFusion, GRACE, GraphCodeBERT, ANCE, curriculum HN mining | Writing task |\\n\\n## Evidence Status\\n\\n### Confirmed findings (basis for claims):\\n- D017: True embedding mining helps (+2.0pp Qwen, +1.6pp StarCoder) — challenges gradient-based necessity assumption\\n- D021/neg_difficulty: Qwen pos_sim=0.9855 (saturated), StarCoder pos_sim=0.7985 (healthy); margin differential explains strategy interaction\\n- m2_embed_verify (pilot): 3-strategy comparison confirms ranking (embedding > random, dataflow conditional)\\n- plan_013 (StarCoder pilot): Confirms cross-encoder pattern — embedding helps both, dataflow helps Qwen only\\n- plan_006: CodeQL scalability confirmed at 123-repo scale\\n\\n### In progress:\\n- m2_full_qwen: random s42 DONE (R@1=0.5527), s43 DONE (R@1=0.5554), s44 RUNNING (eval@500 R@1=0.6009). 2/10 runs complete, ~50h remaining.\\n- m2_full_starcoder: random s42 DONE (R@1=0.4604, from parent), s43 RUNNING (eval@500 R@1=0.4708). 1/9+ runs complete, ~65-70h remaining.\\n- m1_reextract_v2: 80.8% complete (22,842/28,276), 0 ERROR, ETA ~15:00 CST May 15\\n\\n### Planned (priority order):\\n- plan_018: BM25 negative baseline (Dream #1 consensus gap — grounds comparison against CoCoHaNeRe's premise)\\n- plan_003: SWE-bench Lite eval (biggest lever for paper strength)\\n- plan_019: Pool size sensitivity (Dream consensus — external validity)\\n- plan_014: Temperature ablation (Dream reviewer concern)\\n- plan_004: RepoBench-R second benchmark (with multi-seed CIs)\\n- plan_015: Dynamic mining baseline\\n- plan_005: Stratified analysis (extended: structural-available vs fallback stratum)\\n- plan_007/008/009: Additional ablations\\n\\n## Contingency (if full M2 results weaken claims)\\n\\n### All 18 runs confirm pilot pattern: Best case\\n- Full statistical power, paper as framed above\\n- Target: EMNLP Main\\n\\n### Dataflow benefit disappears even for Qwen at full scale: Pivot to 2-claim paper\\n- Drop Claim 2 to analysis observation\\n- Paper becomes: \\\"Simple embedding mining suffices (challenging gradient-based assumption) + CodeQL extraction is practical + representation geometry analysis explains prior contradictions\\\"\\n- Still publishable: challenging gradient-based assumption + mechanistic analysis is sufficient for EMNLP Main\\n\\n### BM25 negatives ≈ random (not harmful): Narrative pivot needed [D030 contingency]\\n- If plan_018 shows BM25 negatives perform ≈ random (not << random), the \\\"challenging gradient-based assumption\\\" narrative needs adjustment\\n- Pivot: \\\"systematic comparison reveals embedding-distance mining is the only strategy that consistently helps; gradient-based methods may not be necessary even when BM25 provides no signal\\\"\\n- Paper remains valid as systematic analysis — the core finding (simple embedding mining suffices) stands regardless of BM25 outcome\\n- Claim 1 core preserved: \\\"Simple static embedding-distance mining consistently improves code retrieval without gradient-based mechanisms\\\"\\n- Impact: BM25 result determines narrative nuance, not core contribution\\n\\n### Embedding mining also loses advantage at full scale: Major reassessment needed\\n- Recheck data pipeline for bugs (full-scale data may have distribution differences)\\n- If confirmed: negative result paper — \\\"Why Hard Negative Mining Doesn't Scale for Code Retrieval\\\"\\n- Discuss with user before committing direction\\n\\n## Deprecated Claims (with reason)\\n\\n- ~~\\\"Embedding-distance hard negatives actively harm code retrieval\\\"~~ — FALSIFIED by D017. Original evidence (-27pp R@1) was from BM25-proxy negatives incorrectly labeled as embedding_distance in MVP. True embedding mining shows consistent improvement. Preserved here to prevent regression.\\n\", \"total_chars\": 12022, \"truncated\": false}, \"error\": null, \"metadata\": {}}"
    }
  },
  "sourceToolAssistantUUID": "1cc9e485-4247-4028-8da6-f6a72531e4b9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "999f865e-f544-467f-b7e8-732fb33862f3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-15T01:58:30.995Z_

<details><summary>↩ Tool result · `toolu_01EKxcu8t4nd7bs4gVDcGFUU`</summary>

```text
artifacts/paper_drafts/discussion_v2.md
artifacts/paper_drafts/experimental_setup_k_checkpoint.md
artifacts/paper_drafts/related_work_v1.md
artifacts/paper_drafts/introduction_v1.md
artifacts/paper_drafts/figure_design_v1.md
artifacts/paper_drafts/method_v1.md
artifacts/paper_drafts/experiments_v1.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "748e6dd3-cdc6-41bf-ad22-cd35b6e92e7a",
  "isSidechain": false,
  "promptId": "82620338-1cd7-4c43-9283-e5cb821c1607",
  "type": "user",
  "uuid": "c4f55428-4dec-446d-95a8-01d698d65e81",
  "toolUseResult": {
    "filenames": [
      "artifacts/paper_drafts/discussion_v2.md",
      "artifacts/paper_drafts/experimental_setup_k_checkpoint.md",
      "artifacts/paper_drafts/related_work_v1.md",
      "artifacts/paper_drafts/introduction_v1.md",
      "artifacts/paper_drafts/figure_design_v1.md",
      "artifacts/paper_drafts/method_v1.md",
      "artifacts/paper_drafts/experiments_v1.md"
    ],
    "durationMs": 11,
    "numFiles": 7,
    "truncated": false
  },
  "sourceToolAssistantUUID": "748e6dd3-cdc6-41bf-ad22-cd35b6e92e7a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "999f865e-f544-467f-b7e8-732fb33862f3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-15T01:58:30.569Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01FrrjrwMv9RJ7embtb7Pya3`</summary>

```json
{
  "project": "structfuse-context",
  "file": "memory.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "874ca8da-36fd-48c5-8ed7-96186291e181",
  "isSidechain": false,
  "requestId": "req_011Cb3XUhYYRP14fAkJQ69vq",
  "type": "assistant",
  "uuid": "ff51c1f9-78bd-4345-8eb3-e66b1e4ffae9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "999f865e-f544-467f-b7e8-732fb33862f3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CUfZNRE2BoQZoU1vFgpc6x",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 451,
      "cache_read_input_tokens": 23225,
      "output_tokens": 309,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 451,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 309,
          "cache_read_input_tokens": 23225,
          "cache_creation_input_tokens": 451,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 451
          },
          "type": "message"
        }
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

_source line 17 · 2026-05-15T01:58:30.582Z_

<details><summary>↩ Tool result · `toolu_01FrrjrwMv9RJ7embtb7Pya3`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/memory.md\", \"content\": \"# Inference-Time Graph Methods 文献对比\\n\\n## 对比表\\n\\n| Method | Paper | Venue | Graph Type | Usage Stage | Inter-proc Data-Flow | Task | Scalability | Key Diff from StructFuse |\\n|--------|-------|-------|-----------|-------------|---------------------|------|-------------|--------------------------|\\n| **CodexGraph** | Bridging LLMs and Code Repositories via Code Graph Databases | NAACL 2025 (arXiv:2408.03910) | Code graph DB (MODULE/CLASS/FUNCTION nodes; CONTAINS/INHERITS/USES edges) | Inference-time | No. Static analysis for symbol relations only | General repo-level coding (completion, issue resolution) | CrossCodeEval, SWE-bench, EvoCodeBench | Agent queries graph DB at inference; task-agnostic schema but no data-flow semantics |\\n| **LocAgent** | Graph-Guided LLM Agents for Code Localization | ACL 2025 (arXiv:2503.09089) | Directed heterogeneous graph (code entities + dependency edges) | Inference-time | No. Dependency edges, not data-flow | Fault localization | 92.7% file-level accuracy; SWE-bench +12% Pass@10 | Agent multi-hop graph reasoning at inference; needs fine-tuned 32B model |\\n| **RANGER** | RANGER — Repository-Level Agent for Graph-Enhanced Retrieval | arXiv:2509.25257 (Sep 2025) | Knowledge graph + MCTS traversal | Inference-time | No | Code search, QA, cross-file retrieval, completion | CodeSearchNet, RepoQA, RepoBench, CrossCodeEval | MCTS-guided graph exploration; dual-stage (Cypher + MCTS); higher inference cost due to cross-encoder scoring |\\n| **RepoGraph** | Enhancing AI SE with Repository-level Code Graph | ICLR 2025 (arXiv:2410.14684) | Repo-level code graph (class hierarchy, call graph, file structure) | Inference-time | No. Structural relations only | Software engineering / issue resolution | SWE-bench (+32.8% relative); CrossCodeEval | Plug-in module for existing agents; repo-wide navigation; no semantic analysis |\\n| **GraphCoder** | Enhancing Repo-Level Code Completion via Code Context Graph | ASE 2024 (arXiv:2406.07003) | Code Context Graph (CFG + CDG + DDG) | Inference-time | Partial. Data dependence graph but **intra-procedural** only | Code completion | Repository-level benchmarks | Coarse-to-fine retrieval with CCG; closest to StructFuse in using data/control flow, but intra-proc and at inference-time |\\n| **CodeRAG** | Supportive Code Retrieval on Bigraph for Real-World Code Generation | arXiv:2504.10046 (Apr 2025) | Bigraph (requirement graph + DS-code graph) | Inference-time | No. Dependency + semantic edges | Repo-level code generation | DevEval (+40.90 Pass@1 w/ GPT-4o) | Dual-graph (requirements + code); agentic reasoning; high inference overhead |\\n| **ARISE** | ARISE: A Repository-level Graph Representation and Toolset for Agentic Fault Localization and Program Repair | arXiv:2605.03117 (May 2026), Seddik & Fard | Multi-granularity program graph (statement nodes + def-use edges) | Inference-time | Partial. **Intra-procedural** def-use edges + data-flow slicing tool | Fault localization + repair | SWE-bench Lite (300 issues); +17.0 Function Recall@1 | Closest to StructFuse in data-flow usage; but intra-proc only, agent queries at inference |\\n| **CodeGRAG** | Bridging NL and PL via Graphical RAG | arXiv:2405.02355 (2024) | Composed syntax graph (AST + DFG + CFG) | Both (GNN training + graph prompt at inference) | Partial. DFG extraction but function-level | Code generation (cross-lingual) | Multiple PLs | Only method with training-time component (GNN soft prompts); but graph also used at inference |\\n| **StructFuse** (Ours) | Structure-Grounded Hard Negatives via CodeQL Data-Flow | — | Inter-procedural data-flow graph (CodeQL taint tracking) | **Training-time only** | **Yes. Full inter-procedural** (source→sink across call boundaries) | Code retrieval (contrastive training) | Large-scale repos with CodeQL | Zero inference overhead; graph used offline for negative mining; inter-proc data-flow |\\n\\n## Discussion 要点\\n\\n### StructFuse vs Inference-Time Graph Methods: 互补性与差异性\\n\\n1. **Cost-accuracy tradeoff**: Inference-time methods (CodexGraph, RANGER, RepoGraph) achieve high precision by constructing and querying graphs per request, but incur significant latency (graph construction + traversal + LLM calls). StructFuse amortizes all graph computation to training time—once the encoder is trained with structure-grounded negatives, inference is a single embedding lookup with zero graph overhead. This makes StructFuse suitable for latency-sensitive production retrieval where inference-time graph methods are impractical.\\n\\n2. **Data-flow depth**: Most inference-time methods use structural graphs (call graphs, class hierarchies, file dependencies). Only GraphCoder and ARISE incorporate data/control flow, but limited to **intra-procedural** scope. StructFuse uniquely leverages **inter-procedural** data-flow via CodeQL's taint tracking, capturing cross-function semantic relationships (e.g., a sanitizer function that transforms data between source and sink across call boundaries). This deeper semantic signal generates harder, more informative negatives.\\n\\n3. **Complementarity**: StructFuse and inference-time methods are orthogonal and composable. A StructFuse-trained encoder can serve as the embedding backbone for systems like RANGER or CodexGraph, providing better initial retrieval that reduces the graph agent's search space. Conversely, inference-time graph methods can provide reranking on top of StructFuse retrieval for tasks requiring maximum precision.\\n\\n4. **Scalability model**: Inference-time methods scale linearly with query volume (each query triggers graph operations). StructFuse's cost is front-loaded: CodeQL analysis runs once per repository update, and the resulting negatives improve the encoder permanently. For high-QPS code search services, this one-time investment yields compounding returns.\\n\\n5. **Task generality vs specialization**: Inference-time graph agents (CodexGraph, RepoGraph) are task-agnostic but require powerful LLMs as backends. StructFuse produces a specialized retrieval encoder that excels at the code search task without LLM inference, making it deployable as a lightweight, efficient first-stage retriever in multi-stage pipelines.\\n\\n## Related Work 段落草稿 (~200 words)\\n\\n**Graph-Based Methods for Code Understanding.**\\nRecent work has explored leveraging code graphs to enhance LLM-based software engineering. Inference-time approaches construct and query graphs during each interaction: CodexGraph (Liu et al., NAACL 2025) builds a code graph database that LLM agents query via structured interfaces; RepoGraph (Ouyang et al., ICLR 2025) provides repository-level navigation as a plug-in module for SE agents; LocAgent (ACL 2025) and RANGER (Shah et al., 2025) employ graph-guided multi-hop reasoning and MCTS-based traversal for code localization and retrieval, respectively. GraphCoder (ASE 2024) incorporates intra-procedural control-flow and data-dependence graphs for code completion retrieval, while ARISE (Seddik & Fard, 2026) extends this with statement-level def-use edges for fault localization. CodeGRAG (2024) bridges training and inference by using GNN-encoded graph prompts.\\n\\nThese methods achieve strong results but impose substantial inference-time costs—graph construction, traversal, and often multiple LLM calls per query. Moreover, their data-flow analysis remains intra-procedural. StructFuse takes a fundamentally different approach: we leverage CodeQL's inter-procedural taint tracking to generate structure-grounded hard negatives at **training time**, producing an encoder that captures cross-function data-flow semantics without any graph overhead at inference. This positions StructFuse as complementary to inference-time graph methods—it can serve as an efficient first-stage retriever whose embeddings already encode deep structural relationships that other methods must compute on-the-fly.\\n\\n---\\n\\n## 参考文献（全部已验证 2026-05-14）\\n\\n- CodexGraph: arXiv:2408.03910, Liu et al., NAACL 2025\\n- LocAgent: arXiv:2503.09089, Chen et al., ACL 2025\\n- RANGER: arXiv:2509.25257, Shah et al., 2025 ✅ verified\\n- RepoGraph: arXiv:2410.14684, Ouyang et al., ICLR 2025\\n- GraphCoder: arXiv:2406.07003, Liu et al., ASE 2024\\n- CodeRAG: arXiv:2504.10046, 2025\\n- ARISE: arXiv:2605.03117, Seddik & Fard, 2026 ✅ verified (full title: \\\"ARISE: A Repository-level Graph Representation and Toolset for Agentic Fault Localization and Program Repair\\\")\\n- CodeGRAG: arXiv:2405.02355, 2024\\n\\n---\\n\\n## BM25 Negative Mining 策略洞察 (2026-05-14, updated)\\n\\n**两层重叠率数据（注意区分）**：\\n- **k=50 全候选重叠**（mining worker 报告）：BM25 vs embedding 87.1%, vs random 76.2%, vs dataflow 71.8%\\n- **top-7 Jaccard**（训练实际用的 num_negatives=7，分层分析）：差异远大于全候选\\n\\n**分层 top-7 Jaccard 重叠率**（seed 42, 2920 matched queries / 12290 total）：\\n| 层级 | BM25 vs Embedding | BM25 vs Random | BM25 vs Dataflow |\\n|------|-------------------|----------------|------------------|\\n| Small (<50 files, 39 repos) | 0.668 | 0.411 | 0.667 |\\n| Medium (50-200, 29 repos) | 0.380 | 0.067 | 0.363 |\\n| Large (200+, 15 repos) | 0.297 | 0.007 | 0.405 |\\n\\n**核心修正**：之前基于 87% 预测\\\"Phase 2 中 BM25 R@1 很可能接近 embedding\\\"——这个预测可能不成立。在中大 repo（训练数据主体）上 top-7 Jaccard 仅 30-38%，BM25 和 embedding 选出的训练 negatives 大部分不同。Phase 2 训练结果将真正区分两种策略。\\n\\n**意外发现**：BM25 vs dataflow 在大 repo 上重叠率（0.405）高于 vs embedding（0.297）。词汇相似性信号与数据流依赖有部分对齐，而纯 embedding 距离选择了不同维度的 hard negatives。\\n\\n---\\n\\n## 运维经验 (2026-05-14)\\n\\n**Registry 状态机 workaround**：当长链训练（多 run 串行）中途因 cron timeout 或子进程退出导致 registry 状态误标（DONE/failed 或 ANALYZING），而实际训练仍在跑时，不可回退状态。解决方案：创建 `{exp_id}_resumed` / `{exp_id}_continued` 新 entry，步进 PREPARING→QUEUED→ALLOCATED→RUNNING，注册 cron 监控实际 PID。原 entry 保留历史 metrics。\\n\\n**Bash 预读陷阱**：运行中的 bash 脚本已将循环体/数组预读到内存，磁盘上修改脚本文件不影响执行。需要在链外设置独立 tmux watcher 监控链 PID 退出后手动触发后续任务。\\n\\n**BM25 Phase 2 触发机制**：两个 tmux watcher（`bm25_starcoder_watcher`, `bm25_qwen_watcher`）每 5 分钟检查链 PID 存活，退出后自动启动 BM25 脚本。watcher 启动的训练不经过 submit_training_job，需在链完成回调中补注册 cron。\\n\\n---\\n\\n## 关键决策记录\\n\\n**m1_reextract_v2 数据使用决策 (2026-05-14, Director Session 8)**：即使 reextract 将数据从 ~16K 增至 ~44K，不重跑 M2。原因：ARR May 25 DDL 不允许再加 4-5 天重训。处理方式：(1) post-M2 完成后若有 GPU 空档，跑 1-seed pilot (Qwen, embedding, 新数据) 对比当前 M2 baseline；(2) 论文中作为 scalability/data efficiency 讨论点；(3) 全量重训留 camera-ready。\", \"total_chars\": 10174, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ff51c1f9-78bd-4345-8eb3-e66b1e4ffae9",
  "isSidechain": false,
  "promptId": "82620338-1cd7-4c43-9283-e5cb821c1607",
  "type": "user",
  "uuid": "bd4d72df-2168-4cf7-aa27-85087f34aa8b",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"path\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/memory.md\\\", \\\"content\\\": \\\"# Inference-Time Graph Methods 文献对比\\\\n\\\\n## 对比表\\\\n\\\\n| Method | Paper | Venue | Graph Type | Usage Stage | Inter-proc Data-Flow | Task | Scalability | Key Diff from StructFuse |\\\\n|--------|-------|-------|-----------|-------------|---------------------|------|-------------|--------------------------|\\\\n| **CodexGraph** | Bridging LLMs and Code Repositories via Code Graph Databases | NAACL 2025 (arXiv:2408.03910) | Code graph DB (MODULE/CLASS/FUNCTION nodes; CONTAINS/INHERITS/USES edges) | Inference-time | No. Static analysis for symbol relations only | General repo-level coding (completion, issue resolution) | CrossCodeEval, SWE-bench, EvoCodeBench | Agent queries graph DB at inference; task-agnostic schema but no data-flow semantics |\\\\n| **LocAgent** | Graph-Guided LLM Agents for Code Localization | ACL 2025 (arXiv:2503.09089) | Directed heterogeneous graph (code entities + dependency edges) | Inference-time | No. Dependency edges, not data-flow | Fault localization | 92.7% file-level accuracy; SWE-bench +12% Pass@10 | Agent multi-hop graph reasoning at inference; needs fine-tuned 32B model |\\\\n| **RANGER** | RANGER — Repository-Level Agent for Graph-Enhanced Retrieval | arXiv:2509.25257 (Sep 2025) | Knowledge graph + MCTS traversal | Inference-time | No | Code search, QA, cross-file retrieval, completion | CodeSearchNet, RepoQA, RepoBench, CrossCodeEval | MCTS-guided graph exploration; dual-stage (Cypher + MCTS); higher inference cost due to cross-encoder scoring |\\\\n| **RepoGraph** | Enhancing AI SE with Repository-level Code Graph | ICLR 2025 (arXiv:2410.14684) | Repo-level code graph (class hierarchy, call graph, file structure) | Inference-time | No. Structural relations only | Software engineering / issue resolution | SWE-bench (+32.8% relative); CrossCodeEval | Plug-in module for existing agents; repo-wide navigation; no semantic analysis |\\\\n| **GraphCoder** | Enhancing Repo-Level Code Completion via Code Context Graph | ASE 2024 (arXiv:2406.07003) | Code Context Graph (CFG + CDG + DDG) | Inference-time | Partial. Data dependence graph but **intra-procedural** only | Code completion | Repository-level benchmarks | Coarse-to-fine retrieval with CCG; closest to StructFuse in using data/control flow, but intra-proc and at inference-time |\\\\n| **CodeRAG** | Supportive Code Retrieval on Bigraph for Real-World Code Generation | arXiv:2504.10046 (Apr 2025) | Bigraph (requirement graph + DS-code graph) | Inference-time | No. Dependency + semantic edges | Repo-level code generation | DevEval (+40.90 Pass@1 w/ GPT-4o) | Dual-graph (requirements + code); agentic reasoning; high inference overhead |\\\\n| **ARISE** | ARISE: A Repository-level Graph Representation and Toolset for Agentic Fault Localization and Program Repair | arXiv:2605.03117 (May 2026), Seddik & Fard | Multi-granularity program graph (statement nodes + def-use edges) | Inference-time | Partial. **Intra-procedural** def-use edges + data-flow slicing tool | Fault localization + repair | SWE-bench Lite (300 issues); +17.0 Function Recall@1 | Closest to StructFuse in data-flow usage; but intra-proc only, agent queries at inference |\\\\n| **CodeGRAG** | Bridging NL and PL via Graphical RAG | arXiv:2405.02355 (2024) | Composed syntax graph (AST + DFG + CFG) | Both (GNN training + graph prompt at inference) | Partial. DFG extraction but function-level | Code generation (cross-lingual) | Multiple PLs | Only method with training-time component (GNN soft prompts); but graph also used at inference |\\\\n| **StructFuse** (Ours) | Structure-Grounded Hard Negatives via CodeQL Data-Flow | — | Inter-procedural data-flow graph (CodeQL taint tracking) | **Training-time only** | **Yes. Full inter-procedural** (source→sink across call boundaries) | Code retrieval (contrastive training) | Large-scale repos with CodeQL | Zero inference overhead; graph used offline for negative mining; inter-proc data-flow |\\\\n\\\\n## Discussion 要点\\\\n\\\\n### StructFuse vs Inference-Time Graph Methods: 互补性与差异性\\\\n\\\\n1. **Cost-accuracy tradeoff**: Inference-time methods (CodexGraph, RANGER, RepoGraph) achieve high precision by constructing and querying graphs per request, but incur significant latency (graph construction + traversal + LLM calls). StructFuse amortizes all graph computation to training time—once the encoder is trained with structure-grounded negatives, inference is a single embedding lookup with zero graph overhead. This makes StructFuse suitable for latency-sensitive production retrieval where inference-time graph methods are impractical.\\\\n\\\\n2. **Data-flow depth**: Most inference-time methods use structural graphs (call graphs, class hierarchies, file dependencies). Only GraphCoder and ARISE incorporate data/control flow, but limited to **intra-procedural** scope. StructFuse uniquely leverages **inter-procedural** data-flow via CodeQL's taint tracking, capturing cross-function semantic relationships (e.g., a sanitizer function that transforms data between source and sink across call boundaries). This deeper semantic signal generates harder, more informative negatives.\\\\n\\\\n3. **Complementarity**: StructFuse and inference-time methods are orthogonal and composable. A StructFuse-trained encoder can serve as the embedding backbone for systems like RANGER or CodexGraph, providing better initial retrieval that reduces the graph agent's search space. Conversely, inference-time graph methods can provide reranking on top of StructFuse retrieval for tasks requiring maximum precision.\\\\n\\\\n4. **Scalability model**: Inference-time methods scale linearly with query volume (each query triggers graph operations). StructFuse's cost is front-loaded: CodeQL analysis runs once per repository update, and the resulting negatives improve the encoder permanently. For high-QPS code search services, this one-time investment yields compounding returns.\\\\n\\\\n5. **Task generality vs specialization**: Inference-time graph agents (CodexGraph, RepoGraph) are task-agnostic but require powerful LLMs as backends. StructFuse produces a specialized retrieval encoder that excels at the code search task without LLM inference, making it deployable as a lightweight, efficient first-stage retriever in multi-stage pipelines.\\\\n\\\\n## Related Work 段落草稿 (~200 words)\\\\n\\\\n**Graph-Based Methods for Code Understanding.**\\\\nRecent work has explored leveraging code graphs to enhance LLM-based software engineering. Inference-time approaches construct and query graphs during each interaction: CodexGraph (Liu et al., NAACL 2025) builds a code graph database that LLM agents query via structured interfaces; RepoGraph (Ouyang et al., ICLR 2025) provides repository-level navigation as a plug-in module for SE agents; LocAgent (ACL 2025) and RANGER (Shah et al., 2025) employ graph-guided multi-hop reasoning and MCTS-based traversal for code localization and retrieval, respectively. GraphCoder (ASE 2024) incorporates intra-procedural control-flow and data-dependence graphs for code completion retrieval, while ARISE (Seddik & Fard, 2026) extends this with statement-level def-use edges for fault localization. CodeGRAG (2024) bridges training and inference by using GNN-encoded graph prompts.\\\\n\\\\nThese methods achieve strong results but impose substantial inference-time costs—graph construction, traversal, and often multiple LLM calls per query. Moreover, their data-flow analysis remains intra-procedural. StructFuse takes a fundamentally different approach: we leverage CodeQL's inter-procedural taint tracking to generate structure-grounded hard negatives at **training time**, producing an encoder that captures cross-function data-flow semantics without any graph overhead at inference. This positions StructFuse as complementary to inference-time graph methods—it can serve as an efficient first-stage retriever whose embeddings already encode deep structural relationships that other methods must compute on-the-fly.\\\\n\\\\n---\\\\n\\\\n## 参考文献（全部已验证 2026-05-14）\\\\n\\\\n- CodexGraph: arXiv:2408.03910, Liu et al., NAACL 2025\\\\n- LocAgent: arXiv:2503.09089, Chen et al., ACL 2025\\\\n- RANGER: arXiv:2509.25257, Shah et al., 2025 ✅ verified\\\\n- RepoGraph: arXiv:2410.14684, Ouyang et al., ICLR 2025\\\\n- GraphCoder: arXiv:2406.07003, Liu et al., ASE 2024\\\\n- CodeRAG: arXiv:2504.10046, 2025\\\\n- ARISE: arXiv:2605.03117, Seddik & Fard, 2026 ✅ verified (full title: \\\\\\\"ARISE: A Repository-level Graph Representation and Toolset for Agentic Fault Localization and Program Repair\\\\\\\")\\\\n- CodeGRAG: arXiv:2405.02355, 2024\\\\n\\\\n---\\\\n\\\\n## BM25 Negative Mining 策略洞察 (2026-05-14, updated)\\\\n\\\\n**两层重叠率数据（注意区分）**：\\\\n- **k=50 全候选重叠**（mining worker 报告）：BM25 vs embedding 87.1%, vs random 76.2%, vs dataflow 71.8%\\\\n- **top-7 Jaccard**（训练实际用的 num_negatives=7，分层分析）：差异远大于全候选\\\\n\\\\n**分层 top-7 Jaccard 重叠率**（seed 42, 2920 matched queries / 12290 total）：\\\\n| 层级 | BM25 vs Embedding | BM25 vs Random | BM25 vs Dataflow |\\\\n|------|-------------------|----------------|------------------|\\\\n| Small (<50 files, 39 repos) | 0.668 | 0.411 | 0.667 |\\\\n| Medium (50-200, 29 repos) | 0.380 | 0.067 | 0.363 |\\\\n| Large (200+, 15 repos) | 0.297 | 0.007 | 0.405 |\\\\n\\\\n**核心修正**：之前基于 87% 预测\\\\\\\"Phase 2 中 BM25 R@1 很可能接近 embedding\\\\\\\"——这个预测可能不成立。在中大 repo（训练数据主体）上 top-7 Jaccard 仅 30-38%，BM25 和 embedding 选出的训练 negatives 大部分不同。Phase 2 训练结果将真正区分两种策略。\\\\n\\\\n**意外发现**：BM25 vs dataflow 在大 repo 上重叠率（0.405）高于 vs embedding（0.297）。词汇相似性信号与数据流依赖有部分对齐，而纯 embedding 距离选择了不同维度的 hard negatives。\\\\n\\\\n---\\\\n\\\\n## 运维经验 (2026-05-14)\\\\n\\\\n**Registry 状态机 workaround**：当长链训练（多 run 串行）中途因 cron timeout 或子进程退出导致 registry 状态误标（DONE/failed 或 ANALYZING），而实际训练仍在跑时，不可回退状态。解决方案：创建 `{exp_id}_resumed` / `{exp_id}_continued` 新 entry，步进 PREPARING→QUEUED→ALLOCATED→RUNNING，注册 cron 监控实际 PID。原 entry 保留历史 metrics。\\\\n\\\\n**Bash 预读陷阱**：运行中的 bash 脚本已将循环体/数组预读到内存，磁盘上修改脚本文件不影响执行。需要在链外设置独立 tmux watcher 监控链 PID 退出后手动触发后续任务。\\\\n\\\\n**BM25 Phase 2 触发机制**：两个 tmux watcher（`bm25_starcoder_watcher`, `bm25_qwen_watcher`）每 5 分钟检查链 PID 存活，退出后自动启动 BM25 脚本。watcher 启动的训练不经过 submit_training_job，需在链完成回调中补注册 cron。\\\\n\\\\n---\\\\n\\\\n## 关键决策记录\\\\n\\\\n**m1_reextract_v2 数据使用决策 (2026-05-14, Director Session 8)**：即使 reextract 将数据从 ~16K 增至 ~44K，不重跑 M2。原因：ARR May 25 DDL 不允许再加 4-5 天重训。处理方式：(1) post-M2 完成后若有 GPU 空档，跑 1-seed pilot (Qwen, embedding, 新数据) 对比当前 M2 baseline；(2) 论文中作为 scalability/data efficiency 讨论点；(3) 全量重训留 camera-ready。\\\", \\\"total_chars\\\": 10174, \\\"truncated\\\": false}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/memory.md\", \"content\": \"# Inference-Time Graph Methods 文献对比\\n\\n## 对比表\\n\\n| Method | Paper | Venue | Graph Type | Usage Stage | Inter-proc Data-Flow | Task | Scalability | Key Diff from StructFuse |\\n|--------|-------|-------|-----------|-------------|---------------------|------|-------------|--------------------------|\\n| **CodexGraph** | Bridging LLMs and Code Repositories via Code Graph Databases | NAACL 2025 (arXiv:2408.03910) | Code graph DB (MODULE/CLASS/FUNCTION nodes; CONTAINS/INHERITS/USES edges) | Inference-time | No. Static analysis for symbol relations only | General repo-level coding (completion, issue resolution) | CrossCodeEval, SWE-bench, EvoCodeBench | Agent queries graph DB at inference; task-agnostic schema but no data-flow semantics |\\n| **LocAgent** | Graph-Guided LLM Agents for Code Localization | ACL 2025 (arXiv:2503.09089) | Directed heterogeneous graph (code entities + dependency edges) | Inference-time | No. Dependency edges, not data-flow | Fault localization | 92.7% file-level accuracy; SWE-bench +12% Pass@10 | Agent multi-hop graph reasoning at inference; needs fine-tuned 32B model |\\n| **RANGER** | RANGER — Repository-Level Agent for Graph-Enhanced Retrieval | arXiv:2509.25257 (Sep 2025) | Knowledge graph + MCTS traversal | Inference-time | No | Code search, QA, cross-file retrieval, completion | CodeSearchNet, RepoQA, RepoBench, CrossCodeEval | MCTS-guided graph exploration; dual-stage (Cypher + MCTS); higher inference cost due to cross-encoder scoring |\\n| **RepoGraph** | Enhancing AI SE with Repository-level Code Graph | ICLR 2025 (arXiv:2410.14684) | Repo-level code graph (class hierarchy, call graph, file structure) | Inference-time | No. Structural relations only | Software engineering / issue resolution | SWE-bench (+32.8% relative); CrossCodeEval | Plug-in module for existing agents; repo-wide navigation; no semantic analysis |\\n| **GraphCoder** | Enhancing Repo-Level Code Completion via Code Context Graph | ASE 2024 (arXiv:2406.07003) | Code Context Graph (CFG + CDG + DDG) | Inference-time | Partial. Data dependence graph but **intra-procedural** only | Code completion | Repository-level benchmarks | Coarse-to-fine retrieval with CCG; closest to StructFuse in using data/control flow, but intra-proc and at inference-time |\\n| **CodeRAG** | Supportive Code Retrieval on Bigraph for Real-World Code Generation | arXiv:2504.10046 (Apr 2025) | Bigraph (requirement graph + DS-code graph) | Inference-time | No. Dependency + semantic edges | Repo-level code generation | DevEval (+40.90 Pass@1 w/ GPT-4o) | Dual-graph (requirements + code); agentic reasoning; high inference overhead |\\n| **ARISE** | ARISE: A Repository-level Graph Representation and Toolset for Agentic Fault Localization and Program Repair | arXiv:2605.03117 (May 2026), Seddik & Fard | Multi-granularity program graph (statement nodes + def-use edges) | Inference-time | Partial. **Intra-procedural** def-use edges + data-flow slicing tool | Fault localization + repair | SWE-bench Lite (300 issues); +17.0 Function Recall@1 | Closest to StructFuse in data-flow usage; but intra-proc only, agent queries at inference |\\n| **CodeGRAG** | Bridging NL and PL via Graphical RAG | arXiv:2405.02355 (2024) | Composed syntax graph (AST + DFG + CFG) | Both (GNN training + graph prompt at inference) | Partial. DFG extraction but function-level | Code generation (cross-lingual) | Multiple PLs | Only method with training-time component (GNN soft prompts); but graph also used at inference |\\n| **StructFuse** (Ours) | Structure-Grounded Hard Negatives via CodeQL Data-Flow | — | Inter-procedural data-flow graph (CodeQL taint tracking) | **Training-time only** | **Yes. Full inter-procedural** (source→sink across call boundaries) | Code retrieval (contrastive training) | Large-scale repos with CodeQL | Zero inference overhead; graph used offline for negative mining; inter-proc data-flow |\\n\\n## Discussion 要点\\n\\n### StructFuse vs Inference-Time Graph Methods: 互补性与差异性\\n\\n1. **Cost-accuracy tradeoff**: Inference-time methods (CodexGraph, RANGER, RepoGraph) achieve high precision by constructing and querying graphs per request, but incur significant latency (graph construction + traversal + LLM calls). StructFuse amortizes all graph computation to training time—once the encoder is trained with structure-grounded negatives, inference is a single embedding lookup with zero graph overhead. This makes StructFuse suitable for latency-sensitive production retrieval where inference-time graph methods are impractical.\\n\\n2. **Data-flow depth**: Most inference-time methods use structural graphs (call graphs, class hierarchies, file dependencies). Only GraphCoder and ARISE incorporate data/control flow, but limited to **intra-procedural** scope. StructFuse uniquely leverages **inter-procedural** data-flow via CodeQL's taint tracking, capturing cross-function semantic relationships (e.g., a sanitizer function that transforms data between source and sink across call boundaries). This deeper semantic signal generates harder, more informative negatives.\\n\\n3. **Complementarity**: StructFuse and inference-time methods are orthogonal and composable. A StructFuse-trained encoder can serve as the embedding backbone for systems like RANGER or CodexGraph, providing better initial retrieval that reduces the graph agent's search space. Conversely, inference-time graph methods can provide reranking on top of StructFuse retrieval for tasks requiring maximum precision.\\n\\n4. **Scalability model**: Inference-time methods scale linearly with query volume (each query triggers graph operations). StructFuse's cost is front-loaded: CodeQL analysis runs once per repository update, and the resulting negatives improve the encoder permanently. For high-QPS code search services, this one-time investment yields compounding returns.\\n\\n5. **Task generality vs specialization**: Inference-time graph agents (CodexGraph, RepoGraph) are task-agnostic but require powerful LLMs as backends. StructFuse produces a specialized retrieval encoder that excels at the code search task without LLM inference, making it deployable as a lightweight, efficient first-stage retriever in multi-stage pipelines.\\n\\n## Related Work 段落草稿 (~200 words)\\n\\n**Graph-Based Methods for Code Understanding.**\\nRecent work has explored leveraging code graphs to enhance LLM-based software engineering. Inference-time approaches construct and query graphs during each interaction: CodexGraph (Liu et al., NAACL 2025) builds a code graph database that LLM agents query via structured interfaces; RepoGraph (Ouyang et al., ICLR 2025) provides repository-level navigation as a plug-in module for SE agents; LocAgent (ACL 2025) and RANGER (Shah et al., 2025) employ graph-guided multi-hop reasoning and MCTS-based traversal for code localization and retrieval, respectively. GraphCoder (ASE 2024) incorporates intra-procedural control-flow and data-dependence graphs for code completion retrieval, while ARISE (Seddik & Fard, 2026) extends this with statement-level def-use edges for fault localization. CodeGRAG (2024) bridges training and inference by using GNN-encoded graph prompts.\\n\\nThese methods achieve strong results but impose substantial inference-time costs—graph construction, traversal, and often multiple LLM calls per query. Moreover, their data-flow analysis remains intra-procedural. StructFuse takes a fundamentally different approach: we leverage CodeQL's inter-procedural taint tracking to generate structure-grounded hard negatives at **training time**, producing an encoder that captures cross-function data-flow semantics without any graph overhead at inference. This positions StructFuse as complementary to inference-time graph methods—it can serve as an efficient first-stage retriever whose embeddings already encode deep structural relationships that other methods must compute on-the-fly.\\n\\n---\\n\\n## 参考文献（全部已验证 2026-05-14）\\n\\n- CodexGraph: arXiv:2408.03910, Liu et al., NAACL 2025\\n- LocAgent: arXiv:2503.09089, Chen et al., ACL 2025\\n- RANGER: arXiv:2509.25257, Shah et al., 2025 ✅ verified\\n- RepoGraph: arXiv:2410.14684, Ouyang et al., ICLR 2025\\n- GraphCoder: arXiv:2406.07003, Liu et al., ASE 2024\\n- CodeRAG: arXiv:2504.10046, 2025\\n- ARISE: arXiv:2605.03117, Seddik & Fard, 2026 ✅ verified (full title: \\\"ARISE: A Repository-level Graph Representation and Toolset for Agentic Fault Localization and Program Repair\\\")\\n- CodeGRAG: arXiv:2405.02355, 2024\\n\\n---\\n\\n## BM25 Negative Mining 策略洞察 (2026-05-14, updated)\\n\\n**两层重叠率数据（注意区分）**：\\n- **k=50 全候选重叠**（mining worker 报告）：BM25 vs embedding 87.1%, vs random 76.2%, vs dataflow 71.8%\\n- **top-7 Jaccard**（训练实际用的 num_negatives=7，分层分析）：差异远大于全候选\\n\\n**分层 top-7 Jaccard 重叠率**（seed 42, 2920 matched queries / 12290 total）：\\n| 层级 | BM25 vs Embedding | BM25 vs Random | BM25 vs Dataflow |\\n|------|-------------------|----------------|------------------|\\n| Small (<50 files, 39 repos) | 0.668 | 0.411 | 0.667 |\\n| Medium (50-200, 29 repos) | 0.380 | 0.067 | 0.363 |\\n| Large (200+, 15 repos) | 0.297 | 0.007 | 0.405 |\\n\\n**核心修正**：之前基于 87% 预测\\\"Phase 2 中 BM25 R@1 很可能接近 embedding\\\"——这个预测可能不成立。在中大 repo（训练数据主体）上 top-7 Jaccard 仅 30-38%，BM25 和 embedding 选出的训练 negatives 大部分不同。Phase 2 训练结果将真正区分两种策略。\\n\\n**意外发现**：BM25 vs dataflow 在大 repo 上重叠率（0.405）高于 vs embedding（0.297）。词汇相似性信号与数据流依赖有部分对齐，而纯 embedding 距离选择了不同维度的 hard negatives。\\n\\n---\\n\\n## 运维经验 (2026-05-14)\\n\\n**Registry 状态机 workaround**：当长链训练（多 run 串行）中途因 cron timeout 或子进程退出导致 registry 状态误标（DONE/failed 或 ANALYZING），而实际训练仍在跑时，不可回退状态。解决方案：创建 `{exp_id}_resumed` / `{exp_id}_continued` 新 entry，步进 PREPARING→QUEUED→ALLOCATED→RUNNING，注册 cron 监控实际 PID。原 entry 保留历史 metrics。\\n\\n**Bash 预读陷阱**：运行中的 bash 脚本已将循环体/数组预读到内存，磁盘上修改脚本文件不影响执行。需要在链外设置独立 tmux watcher 监控链 PID 退出后手动触发后续任务。\\n\\n**BM25 Phase 2 触发机制**：两个 tmux watcher（`bm25_starcoder_watcher`, `bm25_qwen_watcher`）每 5 分钟检查链 PID 存活，退出后自动启动 BM25 脚本。watcher 启动的训练不经过 submit_training_job，需在链完成回调中补注册 cron。\\n\\n---\\n\\n## 关键决策记录\\n\\n**m1_reextract_v2 数据使用决策 (2026-05-14, Director Session 8)**：即使 reextract 将数据从 ~16K 增至 ~44K，不重跑 M2。原因：ARR May 25 DDL 不允许再加 4-5 天重训。处理方式：(1) post-M2 完成后若有 GPU 空档，跑 1-seed pilot (Qwen, embedding, 新数据) 对比当前 M2 baseline；(2) 论文中作为 scalability/data efficiency 讨论点；(3) 全量重训留 camera-ready。\", \"total_chars\": 10174, \"truncated\": false}, \"error\": null, \"metadata\": {}}"
    }
  },
  "sourceToolAssistantUUID": "ff51c1f9-78bd-4345-8eb3-e66b1e4ffae9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "999f865e-f544-467f-b7e8-732fb33862f3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-15T01:58:30.979Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01EKxcu8t4nd7bs4gVDcGFUU`</summary>

```json
{
  "pattern": "*.md",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bd4d72df-2168-4cf7-aa27-85087f34aa8b",
  "isSidechain": false,
  "requestId": "req_011Cb3XUhYYRP14fAkJQ69vq",
  "type": "assistant",
  "uuid": "748e6dd3-cdc6-41bf-ad22-cd35b6e92e7a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "999f865e-f544-467f-b7e8-732fb33862f3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CUfZNRE2BoQZoU1vFgpc6x",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 451,
      "cache_read_input_tokens": 23225,
      "output_tokens": 309,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 451,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 309,
          "cache_read_input_tokens": 23225,
          "cache_creation_input_tokens": 451,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 451
          },
          "type": "message"
        }
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
  "leafUuid": "c4f55428-4dec-446d-95a8-01d698d65e81",
  "sessionId": "999f865e-f544-467f-b7e8-732fb33862f3"
}
```

---

### Runtime record

_source line 20_

```json
{
  "type": "ai-title",
  "aiTitle": "Review Claim 2 wording defensiveness",
  "sessionId": "999f865e-f544-467f-b7e8-732fb33862f3"
}
```

---

### Assistant

_source line 21 · 2026-05-15T01:58:34.956Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have the paper_framing.md and memory.md content. Let me also read the paper draft files to check Claim 2 wording across all sections. Let me read all the draft files in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c4f55428-4dec-446d-95a8-01d698d65e81",
  "isSidechain": false,
  "requestId": "req_011Cb3XV3RNgjKXqkRNHfAAo",
  "type": "assistant",
  "uuid": "4b06d98a-4876-419e-8611-7b3fdafe6e9d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "999f865e-f544-467f-b7e8-732fb33862f3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RmtrSWnaQ6G4HTR38aWSQJ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7521,
      "cache_read_input_tokens": 23676,
      "output_tokens": 640,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 7521,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 640,
          "cache_read_input_tokens": 23676,
          "cache_creation_input_tokens": 7521,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 7521
          },
          "type": "message"
        }
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

_source line 22 · 2026-05-15T01:58:35.958Z_

Now let me read all the paper draft files to check Claim 2 wording across sections.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4b06d98a-4876-419e-8611-7b3fdafe6e9d",
  "isSidechain": false,
  "requestId": "req_011Cb3XV3RNgjKXqkRNHfAAo",
  "type": "assistant",
  "uuid": "f9006e5f-a8dd-41d7-9aac-cc4b2f0c8b97",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "999f865e-f544-467f-b7e8-732fb33862f3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RmtrSWnaQ6G4HTR38aWSQJ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7521,
      "cache_read_input_tokens": 23676,
      "output_tokens": 640,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 7521,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 640,
          "cache_read_input_tokens": 23676,
          "cache_creation_input_tokens": 7521,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 7521
          },
          "type": "message"
        }
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

_source line 23 · 2026-05-15T01:58:37.890Z_

<details open><summary>🔧 Tool call — Read · `toolu_017XN4g1kXuA6hTtA3HeMWm7`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/introduction_v1.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f9006e5f-a8dd-41d7-9aac-cc4b2f0c8b97",
  "isSidechain": false,
  "requestId": "req_011Cb3XV3RNgjKXqkRNHfAAo",
  "type": "assistant",
  "uuid": "12ebccb5-720e-4c17-a3ae-dbedc11b724d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "999f865e-f544-467f-b7e8-732fb33862f3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RmtrSWnaQ6G4HTR38aWSQJ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7521,
      "cache_read_input_tokens": 23676,
      "output_tokens": 640,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 7521,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 640,
          "cache_read_input_tokens": 23676,
          "cache_creation_input_tokens": 7521,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 7521
          },
          "type": "message"
        }
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

_source line 24 · 2026-05-15T01:58:41.000Z_

<details><summary>↩ Tool result · `toolu_01KxtWDfdZbYmpMhUnS8cdK2`</summary>

```text
1	# Experimental Setup: Negatives per Query (K) and Checkpoint Selection
2	
3	## Registry Analysis
4	
5	### K (negatives per query)
6	**K = 7** (`num_negatives=7`) for all main experiments: m2_full_qwen, m2_full_starcoder, m2_embed_verify, plan_013_starcoder. Earlier MVP experiments (p2b series) used K=3 but are superseded.
7	
8	### Dual Checkpoint Comparison
9	
10	| Run | Encoder | Strategy | Best by val_loss | Best by R@1 | Same? |
11	|-----|---------|----------|-----------------|-------------|-------|
12	| m2_full_qwen / random_s42 | Qwen | random | step 1000 (0.4651) | step 1000 (0.553) | Yes |
13	| m2_full_qwen / random_s43 | Qwen | random | step 500 | step 1500 (0.5501) | **No** (Δ=1000) |
14	| m2_embed_verify / random | Qwen | random | step 500 (0.4834) | step 500 (0.5357) | Yes |
15	| m2_embed_verify / embedding | Qwen | embedding | step 500 (0.4603) | step 500 (0.5557) | Yes |
16	| m2_embed_verify / dataflow | Qwen | dataflow | step 500 (0.5602) | step 500 (0.5436) | Yes |
17	| m2_full_starcoder / random_s42 | StarCoder | random | step 1000 (0.6134) | step 2500 (0.4604) | **No** (Δ=1500) |
18	| plan_013_starcoder / embedding | StarCoder | embedding | step 1000 (0.4816) | final (0.5174 > 0.5078@1000) | **No** |
19	| plan_013_starcoder / dataflow | StarCoder | dataflow | step 1000 (0.5255) | final (0.5078 > 0.4869@1000) | **No** |
20	
21	- plan_013_starcoder / random: data not available (post-hoc eval, no per-step tracking)
22	- Remaining m2_full runs (7 Qwen + 8 StarCoder): not yet completed
23	
24	**Pattern**: 4 of 5 Qwen runs agree (both criteria select same checkpoint); 1 Qwen run (random_s43) diverges (Δ=1000 steps). All 3 evaluable StarCoder runs disagree (R@1 improves after val_loss overfits). This is consistent with StarCoder's flatter loss landscape and weaker pretrained separability (neg_difficulty_analysis: StarCoder margin 2.6-4.1x Qwen).
25	
26	**Totals**: 8 evaluable runs — 4/8 (50%) same, 4/8 (50%) different. By encoder: Qwen 4/5 same, StarCoder 0/3 same.
27	
28	---
29	
30	## Paper Paragraph (Experimental Setup)
31	
32	**Training and Evaluation Protocol.**
33	For contrastive training, each query is paired with K=7 negative candidates sampled according to the respective strategy (random, embedding-distance, or dataflow-aware), consistent across all strategies and encoder architectures. We adopt a dual checkpoint selection protocol: during training, we independently track the best checkpoint by validation loss and the best by Recall@1 on a held-out validation set (evaluated every 500 steps). When reporting retrieval metrics, we select the checkpoint that maximizes Recall@1 directly, as validation loss and retrieval performance do not always agree—particularly for StarCoder2, where Recall@1 continues to improve after validation loss begins to overfit. Across 8 completed training runs spanning two encoders and three strategies, both criteria selected the same checkpoint in 4 runs; in the remaining 4 runs (1 Qwen2.5-Coder, 3 StarCoder2), the best-by-Recall@1 checkpoint was selected 500–1500 steps later than the best-by-loss checkpoint. Checkpoint divergence is more prevalent for StarCoder2 (0/3 agreement) than Qwen2.5-Coder (4/5 agreement), consistent with StarCoder2's flatter loss landscape. This dual protocol ensures that reported results reflect the model's best retrieval capability rather than a proxy metric.
34	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bbf8bf43-20ac-4342-a56f-39ee809fcaf5",
  "isSidechain": false,
  "promptId": "82620338-1cd7-4c43-9283-e5cb821c1607",
  "type": "user",
  "uuid": "4df6b46e-758d-413d-a00c-90e4d76eb904",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/experimental_setup_k_checkpoint.md",
      "content": "# Experimental Setup: Negatives per Query (K) and Checkpoint Selection\n\n## Registry Analysis\n\n### K (negatives per query)\n**K = 7** (`num_negatives=7`) for all main experiments: m2_full_qwen, m2_full_starcoder, m2_embed_verify, plan_013_starcoder. Earlier MVP experiments (p2b series) used K=3 but are superseded.\n\n### Dual Checkpoint Comparison\n\n| Run | Encoder | Strategy | Best by val_loss | Best by R@1 | Same? |\n|-----|---------|----------|-----------------|-------------|-------|\n| m2_full_qwen / random_s42 | Qwen | random | step 1000 (0.4651) | step 1000 (0.553) | Yes |\n| m2_full_qwen / random_s43 | Qwen | random | step 500 | step 1500 (0.5501) | **No** (Δ=1000) |\n| m2_embed_verify / random | Qwen | random | step 500 (0.4834) | step 500 (0.5357) | Yes |\n| m2_embed_verify / embedding | Qwen | embedding | step 500 (0.4603) | step 500 (0.5557) | Yes |\n| m2_embed_verify / dataflow | Qwen | dataflow | step 500 (0.5602) | step 500 (0.5436) | Yes |\n| m2_full_starcoder / random_s42 | StarCoder | random | step 1000 (0.6134) | step 2500 (0.4604) | **No** (Δ=1500) |\n| plan_013_starcoder / embedding | StarCoder | embedding | step 1000 (0.4816) | final (0.5174 > 0.5078@1000) | **No** |\n| plan_013_starcoder / dataflow | StarCoder | dataflow | step 1000 (0.5255) | final (0.5078 > 0.4869@1000) | **No** |\n\n- plan_013_starcoder / random: data not available (post-hoc eval, no per-step tracking)\n- Remaining m2_full runs (7 Qwen + 8 StarCoder): not yet completed\n\n**Pattern**: 4 of 5 Qwen runs agree (both criteria select same checkpoint); 1 Qwen run (random_s43) diverges (Δ=1000 steps). All 3 evaluable StarCoder runs disagree (R@1 improves after val_loss overfits). This is consistent with StarCoder's flatter loss landscape and weaker pretrained separability (neg_difficulty_analysis: StarCoder margin 2.6-4.1x Qwen).\n\n**Totals**: 8 evaluable runs — 4/8 (50%) same, 4/8 (50%) different. By encoder: Qwen 4/5 same, StarCoder 0/3 same.\n\n---\n\n## Paper Paragraph (Experimental Setup)\n\n**Training and Evaluation Protocol.**\nFor contrastive training, each query is paired with K=7 negative candidates sampled according to the respective strategy (random, embedding-distance, or dataflow-aware), consistent across all strategies and encoder architectures. We adopt a dual checkpoint selection protocol: during training, we independently track the best checkpoint by validation loss and the best by Recall@1 on a held-out validation set (evaluated every 500 steps). When reporting retrieval metrics, we select the checkpoint that maximizes Recall@1 directly, as validation loss and retrieval performance do not always agree—particularly for StarCoder2, where Recall@1 continues to improve after validation loss begins to overfit. Across 8 completed training runs spanning two encoders and three strategies, both criteria selected the same checkpoint in 4 runs; in the remaining 4 runs (1 Qwen2.5-Coder, 3 StarCoder2), the best-by-Recall@1 checkpoint was selected 500–1500 steps later than the best-by-loss checkpoint. Checkpoint divergence is more prevalent for StarCoder2 (0/3 agreement) than Qwen2.5-Coder (4/5 agreement), consistent with StarCoder2's flatter loss landscape. This dual protocol ensures that reported results reflect the model's best retrieval capability rather than a proxy metric.\n",
      "numLines": 34,
      "startLine": 1,
      "totalLines": 34
    }
  },
  "sourceToolAssistantUUID": "bbf8bf43-20ac-4342-a56f-39ee809fcaf5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "999f865e-f544-467f-b7e8-732fb33862f3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-15T01:58:37.899Z_

<details><summary>↩ Tool result · `toolu_017XN4g1kXuA6hTtA3HeMWm7`</summary>

```text
1	# 1. Introduction
2	
3	Large-scale software maintenance increasingly depends on automatically identifying which source files require modification given a bug report or issue description.
4	Benchmarks such as SWE-bench \cite{jimenez2024swebench} formalize this as a retrieval problem over repositories containing hundreds or thousands of files, and recent systems tackle it through text-based retrieval \cite{reddy2025swerank,xie2025swefixer}, agent-based interactive localization \cite{yang2024sweagent,xia2024agentless}, or combinations thereof.
5	A common assumption underlying these approaches is that textual similarity between an issue description and a source file signals relevance.
6	In practice, however, lexical similarity is an unreliable proxy for structural relevance: two files may share terminology yet have no functional relationship, while structurally coupled files—connected through data-flow or call dependencies—may use entirely different vocabulary.
7	This mismatch is particularly acute in large repositories where naming conventions are reused across unrelated modules, making retrieval that relies solely on text vulnerable to systematic false positives.
8	
9	Two largely independent lines of work have sought to address this limitation, each with a significant gap.
10	First, a growing body of methods leverages code structure graphs at inference time.
11	LocAgent \cite{chen2025locagent} and RANGER \cite{shah2025ranger} employ LLM agents to navigate repository-level graphs during fault localization; CodexGraph \cite{liu2025codexgraph} and RepoGraph \cite{ouyang2025repograph} provide graph database interfaces for structural code navigation; GraphCoder \cite{liu2024graphcoder} and ARISE \cite{seddik2026arise} incorporate control-flow or data-dependence edges—though both remain intra-procedural in scope.
12	These methods demonstrate the value of structural information, yet they apply it exclusively at inference time: the underlying retrieval encoder is trained without structural signal, and its embedding space is shaped solely by textual similarity.
13	Second, hard negative mining—selecting challenging negative examples for contrastive training—is known to substantially impact dense retrieval quality \cite{karpukhin2020dpr,xiong2021ance}, yet has received limited systematic study in the code domain.
14	CoCoHaNeRe \cite{fan2025cocohanere} proposes a gradient-based differentiable hard negative mechanism for code search contrastive learning, arguing that non-differentiable embedding-based negatives are ``slow and ineffective'' compared to gradient-based alternatives.
15	However, CoCoHaNeRe's comparison does not evaluate simple static embedding-distance mining—selecting negatives by nearest-neighbor lookup in a frozen embedding space—in structural code retrieval settings.
16	This leaves open whether the complexity of gradient-based methods is truly necessary, and more broadly, how different negative mining strategies interact with the properties of the encoder being trained.
17	
18	We present a systematic study of hard negative mining strategies for contrastive code retrieval, comparing random sampling, static embedding-distance mining, and structure-grounded negatives derived from inter-procedural data-flow analysis.
19	Our central finding challenges the prevailing assumption that expensive gradient-based methods are required: simple static embedding-distance mining consistently improves retrieval (pilot evidence; pending M2 full confirmation), yielding +1.6--2.0 percentage points in Recall@1 over random baselines across two decoder-only encoders with distinct pretraining paradigms and representation geometries—Qwen2.5-Coder-3B \cite{hui2024qwen25coder} and StarCoder2-3B \cite{li2023starcoder}.
20	These gains are achieved without gradient-based mechanisms, providing a direct counter-example to CoCoHaNeRe's premise in the structural code retrieval setting we study.
21	We note that CoCoHaNeRe's original argument targets the comparison between gradient-based and non-differentiable embedding negatives broadly; our counter-evidence is specific to structural code retrieval, where static embedding-distance mining proves sufficient.
22	Beyond this primary result, we observe that structure-grounded (dataflow) negatives do not consistently outperform embedding mining but exhibit encoder-dependent interaction patterns: analysis of negative difficulty margins reveals that the encoder's pretrained representation geometry—specifically, the degree of embedding space saturation—mediates which strategy is most effective, providing a mechanistic explanation for when and why different mining strategies yield different outcomes.
23	
24	Our contributions are as follows:
25	
26	1. We demonstrate that simple static embedding-distance hard negative mining consistently improves (pilot evidence; pending M2 full confirmation) contrastive code retrieval across two decoder-only encoders with distinct representation geometries, challenging the assumption that gradient-based hard negative methods \cite{fan2025cocohanere} are necessary for effective code search.
27	
28	2. **[Exploratory observation]** We report that structure-grounded (dataflow) negatives interact with encoder representation geometry: negative difficulty margin analysis (+17% for Qwen2.5-Coder-3B, +28% for StarCoder2-3B) provides mechanistic evidence that the pretrained embedding space's degree of saturation mediates strategy effectiveness. Pilot data shows dataflow negatives underperform embedding mining on both encoders, with the gap modulated by representation geometry. This is reported as an observation with mechanistic hypothesis, pending multi-seed confirmation.
29	
30	3. We develop and validate a scope-bounded inter-procedural data-flow extraction pipeline using CodeQL \cite{github2019codeql} that operates at scale (123 repositories, 0% timeout rate, 78% structurally connected non-gold rate), enabling structure-grounded negative mining for contrastive training of code retrievers.
31	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "12ebccb5-720e-4c17-a3ae-dbedc11b724d",
  "isSidechain": false,
  "promptId": "82620338-1cd7-4c43-9283-e5cb821c1607",
  "type": "user",
  "uuid": "faad4bd2-d2e2-40c2-b240-4339c68885c2",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/introduction_v1.md",
      "content": "# 1. Introduction\n\nLarge-scale software maintenance increasingly depends on automatically identifying which source files require modification given a bug report or issue description.\nBenchmarks such as SWE-bench \\cite{jimenez2024swebench} formalize this as a retrieval problem over repositories containing hundreds or thousands of files, and recent systems tackle it through text-based retrieval \\cite{reddy2025swerank,xie2025swefixer}, agent-based interactive localization \\cite{yang2024sweagent,xia2024agentless}, or combinations thereof.\nA common assumption underlying these approaches is that textual similarity between an issue description and a source file signals relevance.\nIn practice, however, lexical similarity is an unreliable proxy for structural relevance: two files may share terminology yet have no functional relationship, while structurally coupled files—connected through data-flow or call dependencies—may use entirely different vocabulary.\nThis mismatch is particularly acute in large repositories where naming conventions are reused across unrelated modules, making retrieval that relies solely on text vulnerable to systematic false positives.\n\nTwo largely independent lines of work have sought to address this limitation, each with a significant gap.\nFirst, a growing body of methods leverages code structure graphs at inference time.\nLocAgent \\cite{chen2025locagent} and RANGER \\cite{shah2025ranger} employ LLM agents to navigate repository-level graphs during fault localization; CodexGraph \\cite{liu2025codexgraph} and RepoGraph \\cite{ouyang2025repograph} provide graph database interfaces for structural code navigation; GraphCoder \\cite{liu2024graphcoder} and ARISE \\cite{seddik2026arise} incorporate control-flow or data-dependence edges—though both remain intra-procedural in scope.\nThese methods demonstrate the value of structural information, yet they apply it exclusively at inference time: the underlying retrieval encoder is trained without structural signal, and its embedding space is shaped solely by textual similarity.\nSecond, hard negative mining—selecting challenging negative examples for contrastive training—is known to substantially impact dense retrieval quality \\cite{karpukhin2020dpr,xiong2021ance}, yet has received limited systematic study in the code domain.\nCoCoHaNeRe \\cite{fan2025cocohanere} proposes a gradient-based differentiable hard negative mechanism for code search contrastive learning, arguing that non-differentiable embedding-based negatives are ``slow and ineffective'' compared to gradient-based alternatives.\nHowever, CoCoHaNeRe's comparison does not evaluate simple static embedding-distance mining—selecting negatives by nearest-neighbor lookup in a frozen embedding space—in structural code retrieval settings.\nThis leaves open whether the complexity of gradient-based methods is truly necessary, and more broadly, how different negative mining strategies interact with the properties of the encoder being trained.\n\nWe present a systematic study of hard negative mining strategies for contrastive code retrieval, comparing random sampling, static embedding-distance mining, and structure-grounded negatives derived from inter-procedural data-flow analysis.\nOur central finding challenges the prevailing assumption that expensive gradient-based methods are required: simple static embedding-distance mining consistently improves retrieval (pilot evidence; pending M2 full confirmation), yielding +1.6--2.0 percentage points in Recall@1 over random baselines across two decoder-only encoders with distinct pretraining paradigms and representation geometries—Qwen2.5-Coder-3B \\cite{hui2024qwen25coder} and StarCoder2-3B \\cite{li2023starcoder}.\nThese gains are achieved without gradient-based mechanisms, providing a direct counter-example to CoCoHaNeRe's premise in the structural code retrieval setting we study.\nWe note that CoCoHaNeRe's original argument targets the comparison between gradient-based and non-differentiable embedding negatives broadly; our counter-evidence is specific to structural code retrieval, where static embedding-distance mining proves sufficient.\nBeyond this primary result, we observe that structure-grounded (dataflow) negatives do not consistently outperform embedding mining but exhibit encoder-dependent interaction patterns: analysis of negative difficulty margins reveals that the encoder's pretrained representation geometry—specifically, the degree of embedding space saturation—mediates which strategy is most effective, providing a mechanistic explanation for when and why different mining strategies yield different outcomes.\n\nOur contributions are as follows:\n\n1. We demonstrate that simple static embedding-distance hard negative mining consistently improves (pilot evidence; pending M2 full confirmation) contrastive code retrieval across two decoder-only encoders with distinct representation geometries, challenging the assumption that gradient-based hard negative methods \\cite{fan2025cocohanere} are necessary for effective code search.\n\n2. **[Exploratory observation]** We report that structure-grounded (dataflow) negatives interact with encoder representation geometry: negative difficulty margin analysis (+17% for Qwen2.5-Coder-3B, +28% for StarCoder2-3B) provides mechanistic evidence that the pretrained embedding space's degree of saturation mediates strategy effectiveness. Pilot data shows dataflow negatives underperform embedding mining on both encoders, with the gap modulated by representation geometry. This is reported as an observation with mechanistic hypothesis, pending multi-seed confirmation.\n\n3. We develop and validate a scope-bounded inter-procedural data-flow extraction pipeline using CodeQL \\cite{github2019codeql} that operates at scale (123 repositories, 0% timeout rate, 78% structurally connected non-gold rate), enabling structure-grounded negative mining for contrastive training of code retrievers.\n",
      "numLines": 31,
      "startLine": 1,
      "totalLines": 31
    }
  },
  "sourceToolAssistantUUID": "12ebccb5-720e-4c17-a3ae-dbedc11b724d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "999f865e-f544-467f-b7e8-732fb33862f3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-15T01:58:38.400Z_

<details open><summary>🔧 Tool call — Read · `toolu_01X6F9kEqyVZNTcNnHWvHip2`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/experiments_v1.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "faad4bd2-d2e2-40c2-b240-4339c68885c2",
  "isSidechain": false,
  "requestId": "req_011Cb3XV3RNgjKXqkRNHfAAo",
  "type": "assistant",
  "uuid": "8bcf9f5e-9265-4e47-8de4-f9e53ab2dab7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "999f865e-f544-467f-b7e8-732fb33862f3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RmtrSWnaQ6G4HTR38aWSQJ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7521,
      "cache_read_input_tokens": 23676,
      "output_tokens": 640,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 7521,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 640,
          "cache_read_input_tokens": 23676,
          "cache_creation_input_tokens": 7521,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 7521
          },
          "type": "message"
        }
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

_source line 27 · 2026-05-15T01:58:38.406Z_

<details><summary>↩ Tool result · `toolu_01X6F9kEqyVZNTcNnHWvHip2`</summary>

```text
1	# §4 Experiments
2	
3	## §4.1 Experimental Setup
4	
5	**Dataset.** We construct our training corpus from SWE-smith \cite{yang2025swesmith}, a large-scale dataset of real-world GitHub bug-fix commits. Starting from 5,029 task instances spanning 131 unique (repository, commit) pairs, each task corresponds to a single bug-fix commit; we expand each task by treating every gold file as a separate training instance, yielding 44,173 training instances total (since many tasks involve multiple gold files). We run the StructFuse extraction pipeline (§3.2) to obtain inter-procedural data-flow graphs via CodeQL. After filtering for clone/checkout failures and extraction errors, we retain \placeholder{15,133} [pending recalc] instances with structural data across 123 repositories, yielding a structural coverage rate of \placeholder{34.3%} [pending recalc]. The remaining \placeholder{65.7%} [pending recalc] of instances lack structural connectivity data due to transient filesystem failures during batch extraction; a re-extraction pass (in progress) is expected to recover the majority of these instances, and we discuss data efficiency implications in §6.
6	
7	For each random seed, we perform a per-repository stratified split to produce approximately 11,300 training and 3,000 validation instances. Each instance consists of an issue description (query), one or more gold files (positives), and strategy-specific negatives (§3.4). The per-seed split ensures that no repository appears exclusively in one partition, preserving the distribution of repository sizes and structural properties.
8	
9	**Evaluation Protocol.** We evaluate retrieval performance using Recall@$k$ ($k \in \{1, 5, 10\}$) and Mean Reciprocal Rank (MRR), computed over a candidate pool of size 50 (1 positive + 49 negatives sampled per query). During training, $K = 7$ negatives are used per query. We report results as mean $\pm$ standard deviation across three random seeds (42, 43, 44). For all comparisons, we use the checkpoint selected by best validation Recall@1 ($\theta^*_{\text{R@1}}$), as discussed in §3.3.
10	
11	**Baselines.** Our core experiment compares three contrastive negative mining strategies—random, embedding-distance, and dataflow-aware (§3.4)—across two encoders and three seeds (3 × 3 × 2 = 18 runs). We additionally include two BM25-based comparisons reported separately from the core matrix: (1) a BM25 retrieval baseline using Okapi BM25 \cite{robertson2009bm25} to rank candidate files by lexical overlap with the query, providing a non-neural reference point; and (2) BM25-mined negatives as a supplementary contrastive training strategy to ground our comparison against the gradient-based premise of CoCoHaNeRe \cite{fan2025cocohanere}.
12	
13	## §4.2 Implementation Details
14	
15	**Encoders.** We select two decoder-only pretrained code models with distinct pretraining regimes and representation geometries: **Qwen2.5-Coder-3B** \cite{hui2024qwen25coder} and **StarCoder2-3B** \cite{li2023starcoder}. Qwen2.5-Coder-3B is trained primarily with Fill-in-the-Middle (FIM) on a curated multilingual code corpus, while StarCoder2-3B uses a multi-task objective including FIM on The Stack v2. As we show in §4.4, these models exhibit markedly different pretrained representation geometries: Qwen operates in a near-saturated similarity regime (mean positive cosine similarity 0.986), while StarCoder maintains healthy separation (mean positive cosine similarity 0.798). This divergence enables us to study how representation geometry mediates the effectiveness of different negative mining strategies.
16	
17	**Fine-Tuning Configuration.** Both encoders are fine-tuned with LoRA \cite{hu2022lora} applied to the query and value projection matrices ($W_q$, $W_v$) of every attention layer, with rank $r = 16$, scaling factor $\alpha = 32$, and dropout 0.05. We apply mean pooling over non-padding positions of the last hidden layer, followed by L2 normalization. A two-layer MLP projection head (Linear→GELU→Linear) maps the pooled representation to a 256-dimensional embedding. Training uses InfoNCE loss with learnable temperature initialized at $\tau = 0.07$, AdamW optimizer with learning rate $2 \times 10^{-5}$, weight decay 0.01, cosine annealing schedule with 10% linear warmup, and gradient clipping at max norm 1.0. Input sequences are truncated to 2,048 tokens. Batch size is 8 with gradient checkpointing enabled.
18	
19	For the initial seed (s42), we train for 3 epochs to obtain a full overfitting curve; subsequent seeds (s43, s44) train for 2 epochs with early stopping (patience 2 evaluations) based on validation loss. Evaluation is performed every 500 steps. We maintain dual checkpoints: $\theta^*_{\text{loss}}$ (minimum validation loss) and $\theta^*_{\text{R@1}}$ (maximum validation Recall@1).
20	
21	**Negative Mining.** Embedding-distance negatives are mined using FAISS \cite{johnson2021faiss} over frozen pretrained embeddings. BM25 negatives are mined by indexing all repository files with Okapi BM25 and selecting the top-$K$ highest-scoring non-gold files per query. Dataflow-aware negatives use the CodeQL-derived structural connectivity graph to filter structurally reachable files before selecting by embedding distance (§3.4). All mining is **static**—performed once before training and not refreshed.
22	
23	**Hardware.** All experiments are conducted on a single node with 2$\times$ NVIDIA RTX PRO 6000 (96 GB VRAM each). Qwen and StarCoder training chains run on separate GPUs in parallel. Each run (single strategy, single seed, single encoder) requires approximately 5–7 hours; the core experiment matrix (3 strategies $\times$ 3 seeds $\times$ 2 encoders = 18 runs) completes in approximately 120 GPU-hours. BM25-mined negative runs are conducted separately and reported as a supplementary comparison.
24	
25	## §4.3 Results
26	
27	### Main Results
28	
29	Table 1 presents the main retrieval results across three negative mining strategies and two encoders. Each cell reports mean $\pm$ standard deviation over three seeds.
30	
31	**Table 1: Retrieval performance by negative mining strategy and encoder.** Pool size = 50. Best per-encoder results in **bold**.
32	
33	| Strategy | Qwen2.5-Coder-3B | | | StarCoder2-3B | | |
34	|---|---|---|---|---|---|---|
35	| | R@1 | R@5 | MRR | R@1 | R@5 | MRR |
36	| BM25 (no training) | \placeholder{X.XX} | \placeholder{X.XX} | \placeholder{X.XX} | \placeholder{X.XX} | \placeholder{X.XX} | \placeholder{X.XX} |
37	| Random | \placeholder{X.XX±X.XX} | \placeholder{X.XX±X.XX} | \placeholder{X.XX±X.XX} | \placeholder{X.XX±X.XX} | \placeholder{X.XX±X.XX} | \placeholder{X.XX±X.XX} |
38	| BM25-mined | \placeholder{X.XX±X.XX} | \placeholder{X.XX±X.XX} | \placeholder{X.XX±X.XX} | \placeholder{X.XX±X.XX} | \placeholder{X.XX±X.XX} | \placeholder{X.XX±X.XX} |
39	| Embedding-distance | \placeholder{X.XX±X.XX} | \placeholder{X.XX±X.XX} | \placeholder{X.XX±X.XX} | \placeholder{X.XX±X.XX} | \placeholder{X.XX±X.XX} | \placeholder{X.XX±X.XX} |
40	| Dataflow-aware | \placeholder{X.XX±X.XX} | \placeholder{X.XX±X.XX} | \placeholder{X.XX±X.XX} | \placeholder{X.XX±X.XX} | \placeholder{X.XX±X.XX} | \placeholder{X.XX±X.XX} |
41	
42	**Key observations.** (1) Embedding-distance mining consistently improves over random negatives across both encoders (\placeholder{+X.X}pp and \placeholder{+X.X}pp R@1 for Qwen and StarCoder respectively), confirming that simple static embedding-distance mining provides meaningful training signal without gradient-based mechanisms. (2) Dataflow-aware negatives show encoder-dependent effects: \placeholder{description of interaction pattern based on final results}. (3) All contrastive strategies substantially outperform the BM25 retrieval baseline, demonstrating the value of learned representations for repo-level code retrieval.
43	
44	### Pilot Validation
45	
46	Prior to the full multi-seed experiment, we conducted single-seed pilot runs on a 24-repository subset (~3,300 instances) to validate the pipeline and obtain early signal on strategy differentiation. Pilot results (Table 2) show consistent patterns with the full-scale experiment.
47	
48	**Table 2: Pilot results (single seed, 24-repo subset, R@1 checkpoint).** Pool size = 50.
49	
50	| Strategy | Qwen R@1 | StarCoder R@1 |
51	|---|---|---|
52	| Random | 0.5357 | 0.4922 |
53	| Embedding-distance | 0.5557 (+2.0pp) | 0.5078 (+1.6pp) |
54	| Dataflow-aware | 0.5436 (+0.8pp) | 0.4869 (−0.5pp) |
55	
56	The pilot established two findings, with patterns expected to be confirmed at full scale (pending M2 full results): (i) embedding-distance mining yields consistent improvement across both encoders, and (ii) the dataflow-aware strategy's effectiveness is encoder-dependent—beneficial for Qwen but neutral-to-negative for StarCoder.
57	
58	### Ablations
59	
60	**Pool Size Sensitivity.** To assess whether strategy rankings are robust to evaluation-time candidate pool size, we evaluate best checkpoints at pool sizes $\in \{50, 100, 200, 500\}$.
61	
62	**Table 3: R@1 by pool size.**
63	
64	| Pool Size | Qwen Emb. | Qwen Rand. | Qwen $\Delta$ | SC Emb. | SC Rand. | SC $\Delta$ |
65	|---|---|---|---|---|---|---|
66	| 50 | \placeholder{X.XX} | \placeholder{X.XX} | \placeholder{+X.X} | \placeholder{X.XX} | \placeholder{X.XX} | \placeholder{+X.X} |
67	| 100 | \placeholder{X.XX} | \placeholder{X.XX} | \placeholder{+X.X} | \placeholder{X.XX} | \placeholder{X.XX} | \placeholder{+X.X} |
68	| 200 | \placeholder{X.XX} | \placeholder{X.XX} | \placeholder{+X.X} | \placeholder{X.XX} | \placeholder{X.XX} | \placeholder{+X.X} |
69	| 500 | \placeholder{X.XX} | \placeholder{X.XX} | \placeholder{+X.X} | \placeholder{X.XX} | \placeholder{X.XX} | \placeholder{+X.X} |
70	
71	**Dynamic Mining Control.** To isolate the effect of static vs. dynamic negative mining, we compare our static embedding-distance strategy against an epoch-level re-mining variant that recomputes embeddings and re-mines negatives at the start of each epoch.
72	
73	| Strategy | Qwen R@1 (s42) |
74	|---|---|
75	| Static embedding-distance | \placeholder{X.XX} |
76	| Dynamic (epoch re-mining) | \placeholder{X.XX} |
77	
78	### Downstream Evaluation
79	
80	**SWE-bench Lite.** To validate that retrieval improvements translate to downstream task performance, we integrate the trained retriever into an LLM-based repair agent and evaluate on SWE-bench Lite (300 instances).
81	
82	| Retriever | Resolve Rate |
83	|---|---|
84	| BM25 | \placeholder{X.X%} |
85	| Random-trained | \placeholder{X.X%} |
86	| Embedding-trained (Qwen) | \placeholder{X.X%} |
87	
88	## §4.4 Analysis
89	
90	### Representation Geometry and Negative Difficulty
91	
92	A central question is *why* embedding-distance mining helps while dataflow-aware mining shows encoder-dependent effects. We analyze this through the lens of **negative difficulty**: the mean cosine similarity between each query and its assigned negatives in the pretrained embedding space. Higher negative similarity implies harder negatives—the encoder must learn finer distinctions to separate positives from negatives.
93	
94	**Table 4: Negative difficulty analysis (pretrained encoders, 2048-token context).** Margin = pos\_sim − neg\_sim.
95	
96	| Strategy | Qwen2.5-Coder-3B | | | StarCoder2-3B | | |
97	|---|---|---|---|---|---|---|
98	| | pos\_sim | neg\_sim | margin | pos\_sim | neg\_sim | margin |
99	| Random | 0.986 | 0.911 | 0.074 | 0.799 | 0.605 | 0.194 |
100	| Embedding-distance | 0.986 | 0.969 | 0.017 | 0.808 | 0.741 | 0.067 |
101	| Dataflow-aware | 0.986 | 0.956 | 0.029 | 0.801 | 0.682 | 0.119 |
102	
103	Several patterns emerge from Table 4:
104	
105	**Saturation asymmetry.** Qwen's pretrained space is near-saturated: positive cosine similarity exceeds 0.98 regardless of strategy, leaving a maximum margin of only 0.074. StarCoder maintains 2.6–4.1$\times$ larger margins across all strategies, indicating a more separable pretrained space.
106	
107	**Difficulty gradient.** Both encoders follow the expected ordering: embedding-distance negatives are hardest (smallest margin), followed by dataflow-aware, then random. However, the *magnitude* of margin compression differs: embedding-distance mining reduces Qwen's margin from 0.074 to 0.017 (77% reduction), while StarCoder's margin drops from 0.194 to 0.067 (65% reduction). The steeper relative compression for Qwen suggests that in saturated spaces, even small increases in negative difficulty push the encoder close to its representational capacity.
108	
109	**Mechanistic hypothesis.** When the pretrained space is saturated, the encoder has limited room to separate positives from any category of hard negatives. Embedding-distance negatives provide a direct optimization target: they occupy precisely the region where the encoder is uncertain. Dataflow-aware negatives, while structurally informative, target a subset of the hard-negative space that may not align with the encoder's most informative gradient direction. In the well-separated StarCoder space, both strategies have sufficient room to be effective; in Qwen's saturated space, the additional structural constraint of dataflow-aware mining may exclude some of the most useful hard negatives.
110	
111	### Stratified Analysis
112	
113	We stratify results by structural data availability to assess whether the dataflow-aware strategy's effectiveness depends on the richness of the underlying CodeQL graph.
114	
115	**Table 5: R@1 stratified by structural data availability.**
116	
117	| Stratum | Instances | Qwen (Emb.) | Qwen (DF) | $\Delta$ | SC (Emb.) | SC (DF) | $\Delta$ |
118	|---|---|---|---|---|---|---|---|
119	| Rich dataflow ($\geq$5 edges) | \placeholder{N} | \placeholder{X.XX} | \placeholder{X.XX} | \placeholder{±X.X} | \placeholder{X.XX} | \placeholder{X.XX} | \placeholder{±X.X} |
120	| Sparse dataflow (1–4 edges) | \placeholder{N} | \placeholder{X.XX} | \placeholder{X.XX} | \placeholder{±X.X} | \placeholder{X.XX} | \placeholder{X.XX} | \placeholder{±X.X} |
121	| No structural data (fallback) | \placeholder{N} | \placeholder{X.XX} | \placeholder{X.XX} | \placeholder{±X.X} | \placeholder{X.XX} | \placeholder{X.XX} | \placeholder{±X.X} |
122	
123	Confound analysis reveals that rich-dataflow instances are heavily concentrated in large repositories (99.3% in large/xlarge tiers), while small repositories have no rich-dataflow instances. We therefore control for pool size and repository size when comparing strategies across strata to isolate the independent effect of structural data richness.
124	
125	### CodeQL Scalability
126	
127	We report extraction-time statistics to support the practicality of the pipeline at scale (Claim 3).
128	
129	&lt;!-- PENDING: Table 6 所有数值将在 m1_reextract_v2 完成后从实际数据一次性重算。不再手动调数字。 -->
130	**Table 6: CodeQL extraction scalability by repository tier [PENDING RECALC].** Repositories are tiered by their instance count in the expanded dataset.
131	
132	| Tier | Repos | Instances | Timeout Rate | Structural Coverage | Z% (median) |
133	|---|---|---|---|---|---|
134	| Small (<50 inst.) | 18 | 500 | 0% | \placeholder{81.0%} [pending recalc] | 0.0% |
135	| Medium (50–200) | 36 | 4,096 | 0% | \placeholder{47.2%} [pending recalc] | 50.0% |
136	| Large (200–500) | 40 | 13,628 | 0% | \placeholder{34.3%} [pending recalc] | 85.7% |
137	| XLarge (500+) | 29 | 25,949 | 0% | \placeholder{31.4%} [pending recalc] | 96.0% |
138	| **Total** | **123** | **44,173** | **0%** | **\placeholder{34.3%} [pending recalc]** | — |
139	
140	The pipeline achieves 0% timeout rate across all repository tiers. Structural coverage [pending recalc] (proportion of instances with CodeQL data-flow output) decreases with repository size, reflecting the combinatorial complexity of inter-procedural analysis in large codebases. Conversely, the connected-not-gold rate (Z%)—the proportion of structurally connected files that are non-gold—increases with repository size, reaching a median of 96% for repositories with 500+ instances. This indicates that larger repositories provide richer pools for structure-grounded negative mining. Of the 123 repositories, \placeholder{104} [pending recalc] produce at least one training pair with inter-file structural connectivity; the remaining \placeholder{19} [pending recalc] contribute instances to training but lack cross-file dataflow edges (their dataflow-aware negatives fall back to embedding-distance selection). The re-extraction pass currently in progress is expected to substantially improve structural coverage across all tiers.
141	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8bcf9f5e-9265-4e47-8de4-f9e53ab2dab7",
  "isSidechain": false,
  "promptId": "82620338-1cd7-4c43-9283-e5cb821c1607",
  "type": "user",
  "uuid": "d65ca5e3-493a-4d16-8633-fc8fc5a5d194",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/experiments_v1.md",
      "content": "# §4 Experiments\n\n## §4.1 Experimental Setup\n\n**Dataset.** We construct our training corpus from SWE-smith \\cite{yang2025swesmith}, a large-scale dataset of real-world GitHub bug-fix commits. Starting from 5,029 task instances spanning 131 unique (repository, commit) pairs, each task corresponds to a single bug-fix commit; we expand each task by treating every gold file as a separate training instance, yielding 44,173 training instances total (since many tasks involve multiple gold files). We run the StructFuse extraction pipeline (§3.2) to obtain inter-procedural data-flow graphs via CodeQL. After filtering for clone/checkout failures and extraction errors, we retain \\placeholder{15,133} [pending recalc] instances with structural data across 123 repositories, yielding a structural coverage rate of \\placeholder{34.3%} [pending recalc]. The remaining \\placeholder{65.7%} [pending recalc] of instances lack structural connectivity data due to transient filesystem failures during batch extraction; a re-extraction pass (in progress) is expected to recover the majority of these instances, and we discuss data efficiency implications in §6.\n\nFor each random seed, we perform a per-repository stratified split to produce approximately 11,300 training and 3,000 validation instances. Each instance consists of an issue description (query), one or more gold files (positives), and strategy-specific negatives (§3.4). The per-seed split ensures that no repository appears exclusively in one partition, preserving the distribution of repository sizes and structural properties.\n\n**Evaluation Protocol.** We evaluate retrieval performance using Recall@$k$ ($k \\in \\{1, 5, 10\\}$) and Mean Reciprocal Rank (MRR), computed over a candidate pool of size 50 (1 positive + 49 negatives sampled per query). During training, $K = 7$ negatives are used per query. We report results as mean $\\pm$ standard deviation across three random seeds (42, 43, 44). For all comparisons, we use the checkpoint selected by best validation Recall@1 ($\\theta^*_{\\text{R@1}}$), as discussed in §3.3.\n\n**Baselines.** Our core experiment compares three contrastive negative mining strategies—random, embedding-distance, and dataflow-aware (§3.4)—across two encoders and three seeds (3 × 3 × 2 = 18 runs). We additionally include two BM25-based comparisons reported separately from the core matrix: (1) a BM25 retrieval baseline using Okapi BM25 \\cite{robertson2009bm25} to rank candidate files by lexical overlap with the query, providing a non-neural reference point; and (2) BM25-mined negatives as a supplementary contrastive training strategy to ground our comparison against the gradient-based premise of CoCoHaNeRe \\cite{fan2025cocohanere}.\n\n## §4.2 Implementation Details\n\n**Encoders.** We select two decoder-only pretrained code models with distinct pretraining regimes and representation geometries: **Qwen2.5-Coder-3B** \\cite{hui2024qwen25coder} and **StarCoder2-3B** \\cite{li2023starcoder}. Qwen2.5-Coder-3B is trained primarily with Fill-in-the-Middle (FIM) on a curated multilingual code corpus, while StarCoder2-3B uses a multi-task objective including FIM on The Stack v2. As we show in §4.4, these models exhibit markedly different pretrained representation geometries: Qwen operates in a near-saturated similarity regime (mean positive cosine similarity 0.986), while StarCoder maintains healthy separation (mean positive cosine similarity 0.798). This divergence enables us to study how representation geometry mediates the effectiveness of different negative mining strategies.\n\n**Fine-Tuning Configuration.** Both encoders are fine-tuned with LoRA \\cite{hu2022lora} applied to the query and value projection matrices ($W_q$, $W_v$) of every attention layer, with rank $r = 16$, scaling factor $\\alpha = 32$, and dropout 0.05. We apply mean pooling over non-padding positions of the last hidden layer, followed by L2 normalization. A two-layer MLP projection head (Linear→GELU→Linear) maps the pooled representation to a 256-dimensional embedding. Training uses InfoNCE loss with learnable temperature initialized at $\\tau = 0.07$, AdamW optimizer with learning rate $2 \\times 10^{-5}$, weight decay 0.01, cosine annealing schedule with 10% linear warmup, and gradient clipping at max norm 1.0. Input sequences are truncated to 2,048 tokens. Batch size is 8 with gradient checkpointing enabled.\n\nFor the initial seed (s42), we train for 3 epochs to obtain a full overfitting curve; subsequent seeds (s43, s44) train for 2 epochs with early stopping (patience 2 evaluations) based on validation loss. Evaluation is performed every 500 steps. We maintain dual checkpoints: $\\theta^*_{\\text{loss}}$ (minimum validation loss) and $\\theta^*_{\\text{R@1}}$ (maximum validation Recall@1).\n\n**Negative Mining.** Embedding-distance negatives are mined using FAISS \\cite{johnson2021faiss} over frozen pretrained embeddings. BM25 negatives are mined by indexing all repository files with Okapi BM25 and selecting the top-$K$ highest-scoring non-gold files per query. Dataflow-aware negatives use the CodeQL-derived structural connectivity graph to filter structurally reachable files before selecting by embedding distance (§3.4). All mining is **static**—performed once before training and not refreshed.\n\n**Hardware.** All experiments are conducted on a single node with 2$\\times$ NVIDIA RTX PRO 6000 (96 GB VRAM each). Qwen and StarCoder training chains run on separate GPUs in parallel. Each run (single strategy, single seed, single encoder) requires approximately 5–7 hours; the core experiment matrix (3 strategies $\\times$ 3 seeds $\\times$ 2 encoders = 18 runs) completes in approximately 120 GPU-hours. BM25-mined negative runs are conducted separately and reported as a supplementary comparison.\n\n## §4.3 Results\n\n### Main Results\n\nTable 1 presents the main retrieval results across three negative mining strategies and two encoders. Each cell reports mean $\\pm$ standard deviation over three seeds.\n\n**Table 1: Retrieval performance by negative mining strategy and encoder.** Pool size = 50. Best per-encoder results in **bold**.\n\n| Strategy | Qwen2.5-Coder-3B | | | StarCoder2-3B | | |\n|---|---|---|---|---|---|---|\n| | R@1 | R@5 | MRR | R@1 | R@5 | MRR |\n| BM25 (no training) | \\placeholder{X.XX} | \\placeholder{X.XX} | \\placeholder{X.XX} | \\placeholder{X.XX} | \\placeholder{X.XX} | \\placeholder{X.XX} |\n| Random | \\placeholder{X.XX±X.XX} | \\placeholder{X.XX±X.XX} | \\placeholder{X.XX±X.XX} | \\placeholder{X.XX±X.XX} | \\placeholder{X.XX±X.XX} | \\placeholder{X.XX±X.XX} |\n| BM25-mined | \\placeholder{X.XX±X.XX} | \\placeholder{X.XX±X.XX} | \\placeholder{X.XX±X.XX} | \\placeholder{X.XX±X.XX} | \\placeholder{X.XX±X.XX} | \\placeholder{X.XX±X.XX} |\n| Embedding-distance | \\placeholder{X.XX±X.XX} | \\placeholder{X.XX±X.XX} | \\placeholder{X.XX±X.XX} | \\placeholder{X.XX±X.XX} | \\placeholder{X.XX±X.XX} | \\placeholder{X.XX±X.XX} |\n| Dataflow-aware | \\placeholder{X.XX±X.XX} | \\placeholder{X.XX±X.XX} | \\placeholder{X.XX±X.XX} | \\placeholder{X.XX±X.XX} | \\placeholder{X.XX±X.XX} | \\placeholder{X.XX±X.XX} |\n\n**Key observations.** (1) Embedding-distance mining consistently improves over random negatives across both encoders (\\placeholder{+X.X}pp and \\placeholder{+X.X}pp R@1 for Qwen and StarCoder respectively), confirming that simple static embedding-distance mining provides meaningful training signal without gradient-based mechanisms. (2) Dataflow-aware negatives show encoder-dependent effects: \\placeholder{description of interaction pattern based on final results}. (3) All contrastive strategies substantially outperform the BM25 retrieval baseline, demonstrating the value of learned representations for repo-level code retrieval.\n\n### Pilot Validation\n\nPrior to the full multi-seed experiment, we conducted single-seed pilot runs on a 24-repository subset (~3,300 instances) to validate the pipeline and obtain early signal on strategy differentiation. Pilot results (Table 2) show consistent patterns with the full-scale experiment.\n\n**Table 2: Pilot results (single seed, 24-repo subset, R@1 checkpoint).** Pool size = 50.\n\n| Strategy | Qwen R@1 | StarCoder R@1 |\n|---|---|---|\n| Random | 0.5357 | 0.4922 |\n| Embedding-distance | 0.5557 (+2.0pp) | 0.5078 (+1.6pp) |\n| Dataflow-aware | 0.5436 (+0.8pp) | 0.4869 (−0.5pp) |\n\nThe pilot established two findings, with patterns expected to be confirmed at full scale (pending M2 full results): (i) embedding-distance mining yields consistent improvement across both encoders, and (ii) the dataflow-aware strategy's effectiveness is encoder-dependent—beneficial for Qwen but neutral-to-negative for StarCoder.\n\n### Ablations\n\n**Pool Size Sensitivity.** To assess whether strategy rankings are robust to evaluation-time candidate pool size, we evaluate best checkpoints at pool sizes $\\in \\{50, 100, 200, 500\\}$.\n\n**Table 3: R@1 by pool size.**\n\n| Pool Size | Qwen Emb. | Qwen Rand. | Qwen $\\Delta$ | SC Emb. | SC Rand. | SC $\\Delta$ |\n|---|---|---|---|---|---|---|\n| 50 | \\placeholder{X.XX} | \\placeholder{X.XX} | \\placeholder{+X.X} | \\placeholder{X.XX} | \\placeholder{X.XX} | \\placeholder{+X.X} |\n| 100 | \\placeholder{X.XX} | \\placeholder{X.XX} | \\placeholder{+X.X} | \\placeholder{X.XX} | \\placeholder{X.XX} | \\placeholder{+X.X} |\n| 200 | \\placeholder{X.XX} | \\placeholder{X.XX} | \\placeholder{+X.X} | \\placeholder{X.XX} | \\placeholder{X.XX} | \\placeholder{+X.X} |\n| 500 | \\placeholder{X.XX} | \\placeholder{X.XX} | \\placeholder{+X.X} | \\placeholder{X.XX} | \\placeholder{X.XX} | \\placeholder{+X.X} |\n\n**Dynamic Mining Control.** To isolate the effect of static vs. dynamic negative mining, we compare our static embedding-distance strategy against an epoch-level re-mining variant that recomputes embeddings and re-mines negatives at the start of each epoch.\n\n| Strategy | Qwen R@1 (s42) |\n|---|---|\n| Static embedding-distance | \\placeholder{X.XX} |\n| Dynamic (epoch re-mining) | \\placeholder{X.XX} |\n\n### Downstream Evaluation\n\n**SWE-bench Lite.** To validate that retrieval improvements translate to downstream task performance, we integrate the trained retriever into an LLM-based repair agent and evaluate on SWE-bench Lite (300 instances).\n\n| Retriever | Resolve Rate |\n|---|---|\n| BM25 | \\placeholder{X.X%} |\n| Random-trained | \\placeholder{X.X%} |\n| Embedding-trained (Qwen) | \\placeholder{X.X%} |\n\n## §4.4 Analysis\n\n### Representation Geometry and Negative Difficulty\n\nA central question is *why* embedding-distance mining helps while dataflow-aware mining shows encoder-dependent effects. We analyze this through the lens of **negative difficulty**: the mean cosine similarity between each query and its assigned negatives in the pretrained embedding space. Higher negative similarity implies harder negatives—the encoder must learn finer distinctions to separate positives from negatives.\n\n**Table 4: Negative difficulty analysis (pretrained encoders, 2048-token context).** Margin = pos\\_sim − neg\\_sim.\n\n| Strategy | Qwen2.5-Coder-3B | | | StarCoder2-3B | | |\n|---|---|---|---|---|---|---|\n| | pos\\_sim | neg\\_sim | margin | pos\\_sim | neg\\_sim | margin |\n| Random | 0.986 | 0.911 | 0.074 | 0.799 | 0.605 | 0.194 |\n| Embedding-distance | 0.986 | 0.969 | 0.017 | 0.808 | 0.741 | 0.067 |\n| Dataflow-aware | 0.986 | 0.956 | 0.029 | 0.801 | 0.682 | 0.119 |\n\nSeveral patterns emerge from Table 4:\n\n**Saturation asymmetry.** Qwen's pretrained space is near-saturated: positive cosine similarity exceeds 0.98 regardless of strategy, leaving a maximum margin of only 0.074. StarCoder maintains 2.6–4.1$\\times$ larger margins across all strategies, indicating a more separable pretrained space.\n\n**Difficulty gradient.** Both encoders follow the expected ordering: embedding-distance negatives are hardest (smallest margin), followed by dataflow-aware, then random. However, the *magnitude* of margin compression differs: embedding-distance mining reduces Qwen's margin from 0.074 to 0.017 (77% reduction), while StarCoder's margin drops from 0.194 to 0.067 (65% reduction). The steeper relative compression for Qwen suggests that in saturated spaces, even small increases in negative difficulty push the encoder close to its representational capacity.\n\n**Mechanistic hypothesis.** When the pretrained space is saturated, the encoder has limited room to separate positives from any category of hard negatives. Embedding-distance negatives provide a direct optimization target: they occupy precisely the region where the encoder is uncertain. Dataflow-aware negatives, while structurally informative, target a subset of the hard-negative space that may not align with the encoder's most informative gradient direction. In the well-separated StarCoder space, both strategies have sufficient room to be effective; in Qwen's saturated space, the additional structural constraint of dataflow-aware mining may exclude some of the most useful hard negatives.\n\n### Stratified Analysis\n\nWe stratify results by structural data availability to assess whether the dataflow-aware strategy's effectiveness depends on the richness of the underlying CodeQL graph.\n\n**Table 5: R@1 stratified by structural data availability.**\n\n| Stratum | Instances | Qwen (Emb.) | Qwen (DF) | $\\Delta$ | SC (Emb.) | SC (DF) | $\\Delta$ |\n|---|---|---|---|---|---|---|---|\n| Rich dataflow ($\\geq$5 edges) | \\placeholder{N} | \\placeholder{X.XX} | \\placeholder{X.XX} | \\placeholder{±X.X} | \\placeholder{X.XX} | \\placeholder{X.XX} | \\placeholder{±X.X} |\n| Sparse dataflow (1–4 edges) | \\placeholder{N} | \\placeholder{X.XX} | \\placeholder{X.XX} | \\placeholder{±X.X} | \\placeholder{X.XX} | \\placeholder{X.XX} | \\placeholder{±X.X} |\n| No structural data (fallback) | \\placeholder{N} | \\placeholder{X.XX} | \\placeholder{X.XX} | \\placeholder{±X.X} | \\placeholder{X.XX} | \\placeholder{X.XX} | \\placeholder{±X.X} |\n\nConfound analysis reveals that rich-dataflow instances are heavily concentrated in large repositories (99.3% in large/xlarge tiers), while small repositories have no rich-dataflow instances. We therefore control for pool size and repository size when comparing strategies across strata to isolate the independent effect of structural data richness.\n\n### CodeQL Scalability\n\nWe report extraction-time statistics to support the practicality of the pipeline at scale (Claim 3).\n\n&lt;!-- PENDING: Table 6 所有数值将在 m1_reextract_v2 完成后从实际数据一次性重算。不再手动调数字。 -->\n**Table 6: CodeQL extraction scalability by repository tier [PENDING RECALC].** Repositories are tiered by their instance count in the expanded dataset.\n\n| Tier | Repos | Instances | Timeout Rate | Structural Coverage | Z% (median) |\n|---|---|---|---|---|---|\n| Small (<50 inst.) | 18 | 500 | 0% | \\placeholder{81.0%} [pending recalc] | 0.0% |\n| Medium (50–200) | 36 | 4,096 | 0% | \\placeholder{47.2%} [pending recalc] | 50.0% |\n| Large (200–500) | 40 | 13,628 | 0% | \\placeholder{34.3%} [pending recalc] | 85.7% |\n| XLarge (500+) | 29 | 25,949 | 0% | \\placeholder{31.4%} [pending recalc] | 96.0% |\n| **Total** | **123** | **44,173** | **0%** | **\\placeholder{34.3%} [pending recalc]** | — |\n\nThe pipeline achieves 0% timeout rate across all repository tiers. Structural coverage [pending recalc] (proportion of instances with CodeQL data-flow output) decreases with repository size, reflecting the combinatorial complexity of inter-procedural analysis in large codebases. Conversely, the connected-not-gold rate (Z%)—the proportion of structurally connected files that are non-gold—increases with repository size, reaching a median of 96% for repositories with 500+ instances. This indicates that larger repositories provide richer pools for structure-grounded negative mining. Of the 123 repositories, \\placeholder{104} [pending recalc] produce at least one training pair with inter-file structural connectivity; the remaining \\placeholder{19} [pending recalc] contribute instances to training but lack cross-file dataflow edges (their dataflow-aware negatives fall back to embedding-distance selection). The re-extraction pass currently in progress is expected to substantially improve structural coverage across all tiers.\n",
      "numLines": 141,
      "startLine": 1,
      "totalLines": 141
    }
  },
  "sourceToolAssistantUUID": "8bcf9f5e-9265-4e47-8de4-f9e53ab2dab7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "999f865e-f544-467f-b7e8-732fb33862f3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-15T01:58:38.857Z_

<details open><summary>🔧 Tool call — Read · `toolu_01PL6mmnEgEdeZeneNm4jih9`</summary>

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
  "parentUuid": "d65ca5e3-493a-4d16-8633-fc8fc5a5d194",
  "isSidechain": false,
  "requestId": "req_011Cb3XV3RNgjKXqkRNHfAAo",
  "type": "assistant",
  "uuid": "105d56f5-0166-483a-92d2-2e7c93de9569",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "999f865e-f544-467f-b7e8-732fb33862f3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RmtrSWnaQ6G4HTR38aWSQJ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7521,
      "cache_read_input_tokens": 23676,
      "output_tokens": 640,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 7521,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 640,
          "cache_read_input_tokens": 23676,
          "cache_creation_input_tokens": 7521,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 7521
          },
          "type": "message"
        }
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

_source line 29 · 2026-05-15T01:58:38.884Z_

<details><summary>↩ Tool result · `toolu_01PL6mmnEgEdeZeneNm4jih9`</summary>

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
  "parentUuid": "105d56f5-0166-483a-92d2-2e7c93de9569",
  "isSidechain": false,
  "promptId": "82620338-1cd7-4c43-9283-e5cb821c1607",
  "type": "user",
  "uuid": "5a1c5868-efc6-467b-a3b7-9a1721f875c8",
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
  "sourceToolAssistantUUID": "105d56f5-0166-483a-92d2-2e7c93de9569",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "999f865e-f544-467f-b7e8-732fb33862f3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 30 · 2026-05-15T01:58:39.337Z_

<details open><summary>🔧 Tool call — Read · `toolu_01H177KCahMu7Zf2nAQjukMs`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/related_work_v1.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5a1c5868-efc6-467b-a3b7-9a1721f875c8",
  "isSidechain": false,
  "requestId": "req_011Cb3XV3RNgjKXqkRNHfAAo",
  "type": "assistant",
  "uuid": "3b534dc5-f714-4901-8141-72063636a7db",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "999f865e-f544-467f-b7e8-732fb33862f3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RmtrSWnaQ6G4HTR38aWSQJ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7521,
      "cache_read_input_tokens": 23676,
      "output_tokens": 640,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 7521,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 640,
          "cache_read_input_tokens": 23676,
          "cache_creation_input_tokens": 7521,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 7521
          },
          "type": "message"
        }
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

_source line 31 · 2026-05-15T01:58:39.341Z_

<details><summary>↩ Tool result · `toolu_01H177KCahMu7Zf2nAQjukMs`</summary>

```text
1	# 2. Related Work
2	
3	## 2.1 Code Retrieval Methods
4	
5	Repo-level code retrieval aims to identify relevant files or code spans from large codebases given a bug report or issue description. Classical sparse retrieval via BM25 \cite{robertson2009bm25} remains a competitive baseline in this setting. The dense retrieval paradigm, pioneered by DPR \cite{karpukhin2020dpr} for open-domain question answering, has been increasingly adopted for code. SweRank \cite{reddy2025swerank} trains a retrieve-and-rerank pipeline for software issue localization, achieving state-of-the-art results on SWE-Bench-Lite and LocBench through text-based retrieval. SWE-Fixer \cite{xie2025swefixer} combines BM25 with a learned retriever in a coarse-to-fine file retrieval pipeline, demonstrating that sparse and dense retrieval are complementary. Both systems, however, treat code files as flat text and do not exploit structural relationships between files during training.
6	
7	A parallel line of work leverages code structure graphs at inference time to guide code navigation. LocAgent \cite{chen2025locagent} parses codebases into directed heterogeneous graphs and employs LLM agents for multi-hop graph reasoning during fault localization. RANGER \cite{shah2025ranger} constructs repository knowledge graphs with variable-level nodes and applies MCTS-guided graph exploration for retrieval. CodexGraph \cite{liu2025codexgraph} indexes codebases into graph databases queried via Cypher, while RepoGraph \cite{ouyang2025repograph} provides line-level code graph navigation as a plug-in module for software engineering agents. GraphCoder \cite{liu2024graphcoder} incorporates control-flow and data-dependence edges into code context graphs for coarse-to-fine retrieval, and ARISE \cite{seddik2026arise} exposes statement-level def-use edges for agentic fault localization—though both are limited to intra-procedural scope. These methods demonstrate the value of structural information for code retrieval, yet they incur per-query computational costs and, for agent-based systems, require multiple LLM calls per retrieval step.
8	
9	Critically, these graph-guided methods apply structural information exclusively at inference time; the underlying retrieval encoder is trained without structural signal. The encoder's embedding space is therefore optimized solely on textual similarity, potentially conflating lexically similar but structurally unrelated code. Our work addresses this gap by incorporating inter-procedural data-flow information into the training process through structure-grounded hard negative mining.
10	
11	## 2.2 Contrastive Learning for Code
12	
13	Building on the success of Sentence-BERT \cite{reimers2019sentencebert} in learning dense sentence representations via siamese contrastive objectives, contrastive learning has proven effective for learning code representations that capture functional semantics beyond surface-level patterns. ContraCode \cite{jain2021contracode} applies compiler-driven transformations to generate functionally equivalent program variants as positive pairs, training the encoder to be invariant to syntactic variation. CodeRetriever \cite{li2022coderetriever} combines unimodal (code-code) and bimodal (code-text) contrastive objectives, achieving strong results across eleven code search benchmarks. \citet{ding2022programcontrasts} leverage program structure and functional attributes to construct contrastive pairs for learning code (dis)similarity representations.
14	
15	Complementary efforts have explored encoding structural information directly into code representations. code2vec \cite{alon2019code2vec} demonstrates that AST path-based representations capture meaningful program properties at scale. GraphCodeBERT \cite{guo2021graphcodebert} incorporates data-flow edges into pre-training, showing that data-flow information improves downstream code understanding tasks. However, GraphCodeBERT uses data-flow as an auxiliary pre-training signal over individual functions, whereas our work uses inter-procedural data-flow to construct hard negatives for contrastive fine-tuning—a fundamentally different application of structural information that operates at the repository level rather than the function level.
16	
17	Despite the progress in contrastive code representation learning, these methods share a common dependency on negative sampling strategy yet few systematically investigate which negatives yield the best representations for code retrieval. Most approaches rely on in-batch negatives \cite{karpukhin2020dpr} or random sampling, leaving the interaction between negative selection strategy and encoder representation geometry unexplored. Our work addresses this gap with a controlled comparison across negative mining strategies on modern decoder-only code encoders.
18	
19	## 2.3 Hard Negative Mining
20	
21	Hard negative mining—selecting negative examples that are challenging for the current model—is well established for improving contrastive learning. In visual representation learning, SimCLR \cite{chen2020simclr} demonstrates the importance of large batch sizes and hard negatives for learning discriminative features. In dense text retrieval, DPR \cite{karpukhin2020dpr} shows that BM25-retrieved passages serve as effective hard negatives beyond in-batch sampling. ANCE \cite{xiong2021ance} advances this by mining negatives from the model's own embedding space via approximate nearest neighbor search, achieving substantial gains over static BM25 negatives. Curriculum-based approaches such as CL-DRD \cite{zeng2022cldrd} progressively increase negative difficulty during training through knowledge distillation.
22	
23	In the code domain, hard negative mining has received comparatively less systematic attention. CoCoHaNeRe \cite{fan2025cocohanere} proposes a differentiable hard negative mechanism for code search contrastive learning, arguing that gradient-based methods yield faster and more effective training than non-differentiable embedding-based negative selection. While CoCoHaNeRe demonstrates the advantages of its gradient-based approach within its experimental setting, it does not evaluate simple static embedding-distance mining—the strategy of selecting hard negatives by nearest-neighbor lookup in the encoder's frozen embedding space—in structural code retrieval settings.
24	
25	Our work provides a systematic comparison that challenges the assumption that expensive gradient-based hard negative methods are necessary for effective code retrieval. We show that simple static embedding-distance mining consistently improves (pilot evidence; pending M2 full confirmation) retrieval performance across two decoder-only encoders with distinct representation geometries, without requiring differentiable negative generation mechanisms. Furthermore, we introduce structure-grounded negatives derived from inter-procedural data-flow analysis and show that the relative effectiveness of mining strategies depends on the encoder's pretrained representation geometry—an interaction that existing work does not examine. Together, these findings address a gap at the intersection of graph-guided code methods, which exploit structure only at inference time, and contrastive training methods, which have not systematically leveraged structural signals for negative selection.
26	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3b534dc5-f714-4901-8141-72063636a7db",
  "isSidechain": false,
  "promptId": "82620338-1cd7-4c43-9283-e5cb821c1607",
  "type": "user",
  "uuid": "8df08a59-73fa-449a-ab74-97a08b17a7db",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/related_work_v1.md",
      "content": "# 2. Related Work\n\n## 2.1 Code Retrieval Methods\n\nRepo-level code retrieval aims to identify relevant files or code spans from large codebases given a bug report or issue description. Classical sparse retrieval via BM25 \\cite{robertson2009bm25} remains a competitive baseline in this setting. The dense retrieval paradigm, pioneered by DPR \\cite{karpukhin2020dpr} for open-domain question answering, has been increasingly adopted for code. SweRank \\cite{reddy2025swerank} trains a retrieve-and-rerank pipeline for software issue localization, achieving state-of-the-art results on SWE-Bench-Lite and LocBench through text-based retrieval. SWE-Fixer \\cite{xie2025swefixer} combines BM25 with a learned retriever in a coarse-to-fine file retrieval pipeline, demonstrating that sparse and dense retrieval are complementary. Both systems, however, treat code files as flat text and do not exploit structural relationships between files during training.\n\nA parallel line of work leverages code structure graphs at inference time to guide code navigation. LocAgent \\cite{chen2025locagent} parses codebases into directed heterogeneous graphs and employs LLM agents for multi-hop graph reasoning during fault localization. RANGER \\cite{shah2025ranger} constructs repository knowledge graphs with variable-level nodes and applies MCTS-guided graph exploration for retrieval. CodexGraph \\cite{liu2025codexgraph} indexes codebases into graph databases queried via Cypher, while RepoGraph \\cite{ouyang2025repograph} provides line-level code graph navigation as a plug-in module for software engineering agents. GraphCoder \\cite{liu2024graphcoder} incorporates control-flow and data-dependence edges into code context graphs for coarse-to-fine retrieval, and ARISE \\cite{seddik2026arise} exposes statement-level def-use edges for agentic fault localization—though both are limited to intra-procedural scope. These methods demonstrate the value of structural information for code retrieval, yet they incur per-query computational costs and, for agent-based systems, require multiple LLM calls per retrieval step.\n\nCritically, these graph-guided methods apply structural information exclusively at inference time; the underlying retrieval encoder is trained without structural signal. The encoder's embedding space is therefore optimized solely on textual similarity, potentially conflating lexically similar but structurally unrelated code. Our work addresses this gap by incorporating inter-procedural data-flow information into the training process through structure-grounded hard negative mining.\n\n## 2.2 Contrastive Learning for Code\n\nBuilding on the success of Sentence-BERT \\cite{reimers2019sentencebert} in learning dense sentence representations via siamese contrastive objectives, contrastive learning has proven effective for learning code representations that capture functional semantics beyond surface-level patterns. ContraCode \\cite{jain2021contracode} applies compiler-driven transformations to generate functionally equivalent program variants as positive pairs, training the encoder to be invariant to syntactic variation. CodeRetriever \\cite{li2022coderetriever} combines unimodal (code-code) and bimodal (code-text) contrastive objectives, achieving strong results across eleven code search benchmarks. \\citet{ding2022programcontrasts} leverage program structure and functional attributes to construct contrastive pairs for learning code (dis)similarity representations.\n\nComplementary efforts have explored encoding structural information directly into code representations. code2vec \\cite{alon2019code2vec} demonstrates that AST path-based representations capture meaningful program properties at scale. GraphCodeBERT \\cite{guo2021graphcodebert} incorporates data-flow edges into pre-training, showing that data-flow information improves downstream code understanding tasks. However, GraphCodeBERT uses data-flow as an auxiliary pre-training signal over individual functions, whereas our work uses inter-procedural data-flow to construct hard negatives for contrastive fine-tuning—a fundamentally different application of structural information that operates at the repository level rather than the function level.\n\nDespite the progress in contrastive code representation learning, these methods share a common dependency on negative sampling strategy yet few systematically investigate which negatives yield the best representations for code retrieval. Most approaches rely on in-batch negatives \\cite{karpukhin2020dpr} or random sampling, leaving the interaction between negative selection strategy and encoder representation geometry unexplored. Our work addresses this gap with a controlled comparison across negative mining strategies on modern decoder-only code encoders.\n\n## 2.3 Hard Negative Mining\n\nHard negative mining—selecting negative examples that are challenging for the current model—is well established for improving contrastive learning. In visual representation learning, SimCLR \\cite{chen2020simclr} demonstrates the importance of large batch sizes and hard negatives for learning discriminative features. In dense text retrieval, DPR \\cite{karpukhin2020dpr} shows that BM25-retrieved passages serve as effective hard negatives beyond in-batch sampling. ANCE \\cite{xiong2021ance} advances this by mining negatives from the model's own embedding space via approximate nearest neighbor search, achieving substantial gains over static BM25 negatives. Curriculum-based approaches such as CL-DRD \\cite{zeng2022cldrd} progressively increase negative difficulty during training through knowledge distillation.\n\nIn the code domain, hard negative mining has received comparatively less systematic attention. CoCoHaNeRe \\cite{fan2025cocohanere} proposes a differentiable hard negative mechanism for code search contrastive learning, arguing that gradient-based methods yield faster and more effective training than non-differentiable embedding-based negative selection. While CoCoHaNeRe demonstrates the advantages of its gradient-based approach within its experimental setting, it does not evaluate simple static embedding-distance mining—the strategy of selecting hard negatives by nearest-neighbor lookup in the encoder's frozen embedding space—in structural code retrieval settings.\n\nOur work provides a systematic comparison that challenges the assumption that expensive gradient-based hard negative methods are necessary for effective code retrieval. We show that simple static embedding-distance mining consistently improves (pilot evidence; pending M2 full confirmation) retrieval performance across two decoder-only encoders with distinct representation geometries, without requiring differentiable negative generation mechanisms. Furthermore, we introduce structure-grounded negatives derived from inter-procedural data-flow analysis and show that the relative effectiveness of mining strategies depends on the encoder's pretrained representation geometry—an interaction that existing work does not examine. Together, these findings address a gap at the intersection of graph-guided code methods, which exploit structure only at inference time, and contrastive training methods, which have not systematically leveraged structural signals for negative selection.\n",
      "numLines": 26,
      "startLine": 1,
      "totalLines": 26
    }
  },
  "sourceToolAssistantUUID": "3b534dc5-f714-4901-8141-72063636a7db",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "999f865e-f544-467f-b7e8-732fb33862f3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 32 · 2026-05-15T01:58:39.816Z_

<details open><summary>🔧 Tool call — Read · `toolu_0184djvvssfqH5wLQh7qFDyx`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/method_v1.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8df08a59-73fa-449a-ab74-97a08b17a7db",
  "isSidechain": false,
  "requestId": "req_011Cb3XV3RNgjKXqkRNHfAAo",
  "type": "assistant",
  "uuid": "92fe1df7-8f0b-4d4f-b016-8c5ea6a598d3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "999f865e-f544-467f-b7e8-732fb33862f3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RmtrSWnaQ6G4HTR38aWSQJ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7521,
      "cache_read_input_tokens": 23676,
      "output_tokens": 640,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 7521,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 640,
          "cache_read_input_tokens": 23676,
          "cache_creation_input_tokens": 7521,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 7521
          },
          "type": "message"
        }
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

_source line 33 · 2026-05-15T01:58:39.821Z_

<details><summary>↩ Tool result · `toolu_0184djvvssfqH5wLQh7qFDyx`</summary>

```text
1	# §3 Method
2	
3	## §3.1 Problem Formulation
4	
5	We address the task of **repo-level code retrieval for bug fixing**: given a natural-language bug report or issue description $q$, retrieve the top-$k$ most relevant source files from a repository's file set $\mathcal{F} = \{f_1, f_2, \ldots, f_N\}$. The gold set $\mathcal{F}^+_q \subset \mathcal{F}$ denotes the files modified in the ground-truth patch.
6	
7	We formulate this as a contrastive learning problem. Let $E_\theta$ be a pretrained encoder parameterized by $\theta$. We learn an embedding space where the similarity between a query $q$ and its gold files exceeds the similarity to non-gold files. Concretely, we optimize $\theta$ such that for all $f^+ \in \mathcal{F}^+_q$ and $f^- \in \mathcal{F} \setminus \mathcal{F}^+_q$:
8	
9	$$\text{sim}(E_\theta(q), E_\theta(f^+)) \gg \text{sim}(E_\theta(q), E_\theta(f^-))$$
10	
11	where $\text{sim}(\cdot, \cdot)$ denotes cosine similarity.
12	
13	The quality of the learned embedding space depends critically on the selection of negative files $f^-$ during training. Random negatives are often too easy, providing weak gradient signal \cite{chen2020simclr}. We systematically compare three negative mining strategies—random, embedding-distance, and dataflow-aware—and analyze how their effectiveness interacts with the encoder's pretrained representation geometry.
14	
15	## §3.2 StructFuse Pipeline
16	
17	Our pipeline consists of three stages: (1) structural graph extraction via static analysis, (2) training data construction with strategy-specific negative mining, and (3) contrastive fine-tuning of a pretrained code encoder.
18	
19	**CodeQL Extraction.** We use CodeQL \cite{codeql2019} to perform scope-bounded inter-procedural data-flow analysis on each repository. Specifically, we define taint-tracking queries that trace data flow from designated sources to sinks, crossing function call boundaries. This yields a set of data-flow paths $\mathcal{P} = \{(v_{\text{src}}, v_1, \ldots, v_{\text{sink}})\}$, where each node $v_i$ is annotated with its enclosing file.
20	
21	We set a scope bound on the analysis depth to ensure tractability: queries that exceed a predefined step limit are terminated. In practice, this achieves 0\% timeout rate across 123 out of 131 repositories in our dataset.
22	
23	**Structural Connectivity Graph.** From the extracted data-flow paths, we construct a file-level structural connectivity graph $G = (V, E)$, where $V = \mathcal{F}$ and an edge $(f_i, f_j) \in E$ exists if and only if at least one data-flow path in $\mathcal{P}$ traverses both $f_i$ and $f_j$. This graph captures inter-procedural structural relationships between files—two files are connected if data flows between them across function call boundaries.
24	
25	A key design property is that $G$ is **externally fixed**: it is computed once from the repository's static structure and does not update during encoder training. This makes the structural signal immune to representation drift \cite{xiong2021ance}, a known issue in dynamic negative mining where the mining distribution shifts as the encoder updates.
26	
27	**Structural Coverage.** At full scale, 78\% of files connected in $G$ are non-gold files (i.e., structurally related but not in the patch), providing a rich pool for structure-grounded negative mining. The remaining files either lack data-flow connections or belong to isolated modules.
28	
29	## §3.3 Training Objective
30	
31	**Contrastive Loss.** We train with InfoNCE loss \cite{karpukhin2020dpr}. For a query $q$ with positive file $f^+$ and a set of $K$ negatives $\{f^-_1, \ldots, f^-_K\}$, the loss is:
32	
33	$$\mathcal{L} = -\log \frac{\exp(\text{sim}(E_\theta(q), E_\theta(f^+)) / \tau)}{\exp(\text{sim}(E_\theta(q), E_\theta(f^+)) / \tau) + \sum_{k=1}^{K} \exp(\text{sim}(E_\theta(q), E_\theta(f^-_k)) / \tau)}$$
34	
35	where $\tau$ is a learnable temperature parameter initialized to 0.07 and $K = 7$ negatives per query. Our framework supports distance-weighted positive scores via per-sample weights $w_i = \exp(-\alpha \cdot d_i)$, where $d_i$ is the data-flow path distance from query to positive and $\alpha = 1.0$. In practice, the training data assigns a uniform distance of $d = 1$ to all positives, yielding a constant weight $w = e^{-1}$ across all samples. Since this scales all per-sample losses equally, the optimization is equivalent to standard unweighted InfoNCE.
36	
37	**Encoder Architecture.** We fine-tune two decoder-only pretrained code models—Qwen2.5-Coder-3B \cite{hui2024qwen25coder} and StarCoder2-3B \cite{li2023starcoder}—which differ in pretraining objectives (Fill-in-the-Middle vs. multi-task including Fill-in-the-Middle) and exhibit distinct representation geometries (§5). We apply mean pooling over non-padding positions of the last hidden layer to obtain fixed-dimensional representations, followed by L2 normalization. Each encoder is augmented with a two-layer MLP projection head (Linear→GELU→Linear) that maps the pooled hidden state to a 256-dimensional embedding space.
38	
39	**Parameter-Efficient Fine-Tuning.** We apply LoRA \cite{hu2022lora} to the query and value projection matrices ($W_q$, $W_v$) of each attention layer with rank $r = 16$, scaling factor $\alpha = 32$, and dropout 0.05. The base model weights remain frozen; only the LoRA adapters and projection head are updated. We use AdamW with learning rate $2 \times 10^{-5}$, weight decay 0.01, cosine annealing with 10\% linear warmup, and gradient clipping at max norm 1.0. Input sequences are truncated to 2048 tokens. We train for 2 epochs with early stopping (patience=2). An initial exploratory seed ($s_{42}$) uses 3 epochs to provide a complete overfitting curve; subsequent seeds use 2 epochs based on observed overfitting after epoch 1 (see §4). Evaluation is performed every 500 steps.
40	
41	**Dual Checkpoint Selection.** We observe that validation loss and retrieval metrics (Recall@1) do not always select the same checkpoint, particularly for StarCoder2-3B. We therefore maintain two checkpoints throughout training: $\theta^*_{\text{loss}}$ (minimum validation loss) and $\theta^*_{\text{R@1}}$ (maximum validation Recall@1). Final evaluation uses $\theta^*_{\text{R@1}}$, and we report both to enable analysis of the loss–metric disagreement.
42	
43	## §3.4 Negative Mining Strategies
44	
45	We compare three negative mining strategies that span a spectrum from uninformed to structure-grounded selection.
46	
47	**Random Mining.** For each query $q$, we sample $K$ negatives uniformly at random from $\mathcal{F} \setminus \mathcal{F}^+_q$. This serves as the baseline: negatives are unbiased but typically easy, as randomly chosen files are unlikely to share topical or structural similarity with the query.
48	
49	**Embedding-Distance Mining.** We compute embeddings for all files and queries using the frozen pretrained encoder $E_{\theta_0}$ (before fine-tuning) and build a FAISS index \cite{johnson2021faiss} over file embeddings. For each query $q$, we retrieve the $K$ non-gold files with highest cosine similarity to $q$ in the pretrained embedding space:
50	
51	$$f^-_{\text{embed}} = \underset{f \in \mathcal{F} \setminus \mathcal{F}^+_q}{\text{argtop-}K}\ \text{sim}(E_{\theta_0}(q), E_{\theta_0}(f))$$
52	
53	This selects files that the pretrained encoder already considers similar to the query—hard negatives that force the fine-tuned encoder to learn finer distinctions. Critically, this mining is **static**: embeddings are computed once from $E_{\theta_0}$ and not refreshed during training, avoiding the computational overhead and instability of online re-mining \cite{xiong2021ance}.
54	
55	**Dataflow-Aware Mining.** This strategy leverages the structural connectivity graph $G$ from §3.2 to select negatives that are textually similar but structurally disconnected from the query context. Formally, for query $q$ with associated gold files $\mathcal{F}^+_q$, we define the reachability set $\mathcal{R}_G(q) = \{f \in \mathcal{F} : \exists f^+ \in \mathcal{F}^+_q,\ (f^+, f) \in E^*\}$, where $E^*$ denotes the transitive closure of $G$. The dataflow-aware negatives are:
56	
57	$$f^-_{\text{df}} = \underset{f \in \mathcal{F} \setminus \mathcal{F}^+_q :\ f \notin \mathcal{R}_G(q)}{\text{argtop-}K}\ \text{sim}(E_{\theta_0}(q), E_{\theta_0}(f))$$
58	
59	That is, we select the most similar non-gold files that are also **structurally unreachable** from the gold files in the data-flow graph. The intuition is that these files represent a category of particularly informative negatives: they appear relevant based on surface-level textual features (variable names, API patterns, shared imports) yet lack the inter-procedural data-flow connections that characterize true functional relatedness. By training the encoder to distinguish these cases, we aim to push the embedding space toward capturing structural semantics beyond lexical overlap.
60	
61	**Difficulty Gradient.** The three strategies impose an expected difficulty ordering. Random negatives are easiest (low similarity, no structural constraint). Embedding-distance negatives are harder (high pretrained similarity, no structural constraint). Dataflow-aware negatives add a structural filter on top of embedding distance, selecting a subset that is simultaneously similar in text and disconnected in structure. We quantify this ordering empirically via the *negative difficulty* metric: the mean cosine similarity between each query and its assigned negatives (§5).
62	
63	For repositories where the structural graph $G$ has insufficient coverage (fewer than $K$ structurally disconnected candidates above a similarity threshold), the dataflow-aware strategy falls back to embedding-distance mining. This fallback applies to approximately 66\% of training instances, which lack structural connectivity data and therefore cannot supply structurally disconnected candidates. We analyze the fallback stratum separately in stratified evaluation (§5).
64	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "92fe1df7-8f0b-4d4f-b016-8c5ea6a598d3",
  "isSidechain": false,
  "promptId": "82620338-1cd7-4c43-9283-e5cb821c1607",
  "type": "user",
  "uuid": "5c48d629-f44e-47b4-b6f0-b5d61c52af9b",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/method_v1.md",
      "content": "# §3 Method\n\n## §3.1 Problem Formulation\n\nWe address the task of **repo-level code retrieval for bug fixing**: given a natural-language bug report or issue description $q$, retrieve the top-$k$ most relevant source files from a repository's file set $\\mathcal{F} = \\{f_1, f_2, \\ldots, f_N\\}$. The gold set $\\mathcal{F}^+_q \\subset \\mathcal{F}$ denotes the files modified in the ground-truth patch.\n\nWe formulate this as a contrastive learning problem. Let $E_\\theta$ be a pretrained encoder parameterized by $\\theta$. We learn an embedding space where the similarity between a query $q$ and its gold files exceeds the similarity to non-gold files. Concretely, we optimize $\\theta$ such that for all $f^+ \\in \\mathcal{F}^+_q$ and $f^- \\in \\mathcal{F} \\setminus \\mathcal{F}^+_q$:\n\n$$\\text{sim}(E_\\theta(q), E_\\theta(f^+)) \\gg \\text{sim}(E_\\theta(q), E_\\theta(f^-))$$\n\nwhere $\\text{sim}(\\cdot, \\cdot)$ denotes cosine similarity.\n\nThe quality of the learned embedding space depends critically on the selection of negative files $f^-$ during training. Random negatives are often too easy, providing weak gradient signal \\cite{chen2020simclr}. We systematically compare three negative mining strategies—random, embedding-distance, and dataflow-aware—and analyze how their effectiveness interacts with the encoder's pretrained representation geometry.\n\n## §3.2 StructFuse Pipeline\n\nOur pipeline consists of three stages: (1) structural graph extraction via static analysis, (2) training data construction with strategy-specific negative mining, and (3) contrastive fine-tuning of a pretrained code encoder.\n\n**CodeQL Extraction.** We use CodeQL \\cite{codeql2019} to perform scope-bounded inter-procedural data-flow analysis on each repository. Specifically, we define taint-tracking queries that trace data flow from designated sources to sinks, crossing function call boundaries. This yields a set of data-flow paths $\\mathcal{P} = \\{(v_{\\text{src}}, v_1, \\ldots, v_{\\text{sink}})\\}$, where each node $v_i$ is annotated with its enclosing file.\n\nWe set a scope bound on the analysis depth to ensure tractability: queries that exceed a predefined step limit are terminated. In practice, this achieves 0\\% timeout rate across 123 out of 131 repositories in our dataset.\n\n**Structural Connectivity Graph.** From the extracted data-flow paths, we construct a file-level structural connectivity graph $G = (V, E)$, where $V = \\mathcal{F}$ and an edge $(f_i, f_j) \\in E$ exists if and only if at least one data-flow path in $\\mathcal{P}$ traverses both $f_i$ and $f_j$. This graph captures inter-procedural structural relationships between files—two files are connected if data flows between them across function call boundaries.\n\nA key design property is that $G$ is **externally fixed**: it is computed once from the repository's static structure and does not update during encoder training. This makes the structural signal immune to representation drift \\cite{xiong2021ance}, a known issue in dynamic negative mining where the mining distribution shifts as the encoder updates.\n\n**Structural Coverage.** At full scale, 78\\% of files connected in $G$ are non-gold files (i.e., structurally related but not in the patch), providing a rich pool for structure-grounded negative mining. The remaining files either lack data-flow connections or belong to isolated modules.\n\n## §3.3 Training Objective\n\n**Contrastive Loss.** We train with InfoNCE loss \\cite{karpukhin2020dpr}. For a query $q$ with positive file $f^+$ and a set of $K$ negatives $\\{f^-_1, \\ldots, f^-_K\\}$, the loss is:\n\n$$\\mathcal{L} = -\\log \\frac{\\exp(\\text{sim}(E_\\theta(q), E_\\theta(f^+)) / \\tau)}{\\exp(\\text{sim}(E_\\theta(q), E_\\theta(f^+)) / \\tau) + \\sum_{k=1}^{K} \\exp(\\text{sim}(E_\\theta(q), E_\\theta(f^-_k)) / \\tau)}$$\n\nwhere $\\tau$ is a learnable temperature parameter initialized to 0.07 and $K = 7$ negatives per query. Our framework supports distance-weighted positive scores via per-sample weights $w_i = \\exp(-\\alpha \\cdot d_i)$, where $d_i$ is the data-flow path distance from query to positive and $\\alpha = 1.0$. In practice, the training data assigns a uniform distance of $d = 1$ to all positives, yielding a constant weight $w = e^{-1}$ across all samples. Since this scales all per-sample losses equally, the optimization is equivalent to standard unweighted InfoNCE.\n\n**Encoder Architecture.** We fine-tune two decoder-only pretrained code models—Qwen2.5-Coder-3B \\cite{hui2024qwen25coder} and StarCoder2-3B \\cite{li2023starcoder}—which differ in pretraining objectives (Fill-in-the-Middle vs. multi-task including Fill-in-the-Middle) and exhibit distinct representation geometries (§5). We apply mean pooling over non-padding positions of the last hidden layer to obtain fixed-dimensional representations, followed by L2 normalization. Each encoder is augmented with a two-layer MLP projection head (Linear→GELU→Linear) that maps the pooled hidden state to a 256-dimensional embedding space.\n\n**Parameter-Efficient Fine-Tuning.** We apply LoRA \\cite{hu2022lora} to the query and value projection matrices ($W_q$, $W_v$) of each attention layer with rank $r = 16$, scaling factor $\\alpha = 32$, and dropout 0.05. The base model weights remain frozen; only the LoRA adapters and projection head are updated. We use AdamW with learning rate $2 \\times 10^{-5}$, weight decay 0.01, cosine annealing with 10\\% linear warmup, and gradient clipping at max norm 1.0. Input sequences are truncated to 2048 tokens. We train for 2 epochs with early stopping (patience=2). An initial exploratory seed ($s_{42}$) uses 3 epochs to provide a complete overfitting curve; subsequent seeds use 2 epochs based on observed overfitting after epoch 1 (see §4). Evaluation is performed every 500 steps.\n\n**Dual Checkpoint Selection.** We observe that validation loss and retrieval metrics (Recall@1) do not always select the same checkpoint, particularly for StarCoder2-3B. We therefore maintain two checkpoints throughout training: $\\theta^*_{\\text{loss}}$ (minimum validation loss) and $\\theta^*_{\\text{R@1}}$ (maximum validation Recall@1). Final evaluation uses $\\theta^*_{\\text{R@1}}$, and we report both to enable analysis of the loss–metric disagreement.\n\n## §3.4 Negative Mining Strategies\n\nWe compare three negative mining strategies that span a spectrum from uninformed to structure-grounded selection.\n\n**Random Mining.** For each query $q$, we sample $K$ negatives uniformly at random from $\\mathcal{F} \\setminus \\mathcal{F}^+_q$. This serves as the baseline: negatives are unbiased but typically easy, as randomly chosen files are unlikely to share topical or structural similarity with the query.\n\n**Embedding-Distance Mining.** We compute embeddings for all files and queries using the frozen pretrained encoder $E_{\\theta_0}$ (before fine-tuning) and build a FAISS index \\cite{johnson2021faiss} over file embeddings. For each query $q$, we retrieve the $K$ non-gold files with highest cosine similarity to $q$ in the pretrained embedding space:\n\n$$f^-_{\\text{embed}} = \\underset{f \\in \\mathcal{F} \\setminus \\mathcal{F}^+_q}{\\text{argtop-}K}\\ \\text{sim}(E_{\\theta_0}(q), E_{\\theta_0}(f))$$\n\nThis selects files that the pretrained encoder already considers similar to the query—hard negatives that force the fine-tuned encoder to learn finer distinctions. Critically, this mining is **static**: embeddings are computed once from $E_{\\theta_0}$ and not refreshed during training, avoiding the computational overhead and instability of online re-mining \\cite{xiong2021ance}.\n\n**Dataflow-Aware Mining.** This strategy leverages the structural connectivity graph $G$ from §3.2 to select negatives that are textually similar but structurally disconnected from the query context. Formally, for query $q$ with associated gold files $\\mathcal{F}^+_q$, we define the reachability set $\\mathcal{R}_G(q) = \\{f \\in \\mathcal{F} : \\exists f^+ \\in \\mathcal{F}^+_q,\\ (f^+, f) \\in E^*\\}$, where $E^*$ denotes the transitive closure of $G$. The dataflow-aware negatives are:\n\n$$f^-_{\\text{df}} = \\underset{f \\in \\mathcal{F} \\setminus \\mathcal{F}^+_q :\\ f \\notin \\mathcal{R}_G(q)}{\\text{argtop-}K}\\ \\text{sim}(E_{\\theta_0}(q), E_{\\theta_0}(f))$$\n\nThat is, we select the most similar non-gold files that are also **structurally unreachable** from the gold files in the data-flow graph. The intuition is that these files represent a category of particularly informative negatives: they appear relevant based on surface-level textual features (variable names, API patterns, shared imports) yet lack the inter-procedural data-flow connections that characterize true functional relatedness. By training the encoder to distinguish these cases, we aim to push the embedding space toward capturing structural semantics beyond lexical overlap.\n\n**Difficulty Gradient.** The three strategies impose an expected difficulty ordering. Random negatives are easiest (low similarity, no structural constraint). Embedding-distance negatives are harder (high pretrained similarity, no structural constraint). Dataflow-aware negatives add a structural filter on top of embedding distance, selecting a subset that is simultaneously similar in text and disconnected in structure. We quantify this ordering empirically via the *negative difficulty* metric: the mean cosine similarity between each query and its assigned negatives (§5).\n\nFor repositories where the structural graph $G$ has insufficient coverage (fewer than $K$ structurally disconnected candidates above a similarity threshold), the dataflow-aware strategy falls back to embedding-distance mining. This fallback applies to approximately 66\\% of training instances, which lack structural connectivity data and therefore cannot supply structurally disconnected candidates. We analyze the fallback stratum separately in stratified evaluation (§5).\n",
      "numLines": 64,
      "startLine": 1,
      "totalLines": 64
    }
  },
  "sourceToolAssistantUUID": "92fe1df7-8f0b-4d4f-b016-8c5ea6a598d3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "999f865e-f544-467f-b7e8-732fb33862f3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 34 · 2026-05-15T01:58:40.769Z_

<details open><summary>🔧 Tool call — Read · `toolu_012cuzGJjUqs2U4NjUTHPSUZ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/figure_design_v1.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5c48d629-f44e-47b4-b6f0-b5d61c52af9b",
  "isSidechain": false,
  "requestId": "req_011Cb3XV3RNgjKXqkRNHfAAo",
  "type": "assistant",
  "uuid": "8c0467d3-93bf-442f-81bb-2862d2e0e8a6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "999f865e-f544-467f-b7e8-732fb33862f3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RmtrSWnaQ6G4HTR38aWSQJ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7521,
      "cache_read_input_tokens": 23676,
      "output_tokens": 640,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 7521,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 640,
          "cache_read_input_tokens": 23676,
          "cache_creation_input_tokens": 7521,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 7521
          },
          "type": "message"
        }
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

_source line 35 · 2026-05-15T01:58:40.775Z_

<details><summary>↩ Tool result · `toolu_012cuzGJjUqs2U4NjUTHPSUZ`</summary>

````text
1	# Figure Design — StructFuse Paper
2	
3	Target: EMNLP 2026 Main (ARR May 25 deadline)
4	Style: Two-column ACL format, max width ~3.25in (single col) or ~6.75in (full width)
5	
6	---
7	
8	## Figure 1: StructFuse Pipeline Overview
9	
10	**Purpose**: Establish the full method at a glance. Supports Claim 3 (CodeQL pipeline practicality) and orients the reader for §3.
11	
12	**Layout**: Full-width (2-column span). Left-to-right flow diagram with 4 major blocks:
13	
14	```
15	[Input]              [Extraction]           [Mining]              [Training]
16	┌──────────┐      ┌──────────────┐      ┌──────────────┐      ┌──────────────┐
17	│ Repo +   │ ──→  │ CodeQL       │ ──→  │ Negative     │ ──→  │ Contrastive  │
18	│ Bug      │      │ Data-flow    │      │ Mining       │      │ Fine-tuning  │
19	│ Report   │      │ Analysis     │      │ (3 strats)   │      │ (InfoNCE)    │
20	└──────────┘      └──────────────┘      └──────────────┘      └──────────────┘
21	                        │                      │
22	                   Structural            ┌─────┴─────┐
23	                   Graph G               │ Random    │
24	                                         │ Embedding │
25	                                         │ Dataflow  │
26	                                         └───────────┘
27	```
28	
29	- Input block: repo file tree icon + issue/bug report text snippet
30	- Extraction block: CodeQL logo/icon, arrows showing inter-procedural data-flow paths crossing file boundaries, output = Graph G (nodes=files, edges=data-flow)
31	- Mining block: 3 parallel branches for the 3 strategies, each with a mini-icon (dice for random, cosine curve for embedding, graph for dataflow). Show query → candidate selection for each
32	- Training block: encoder icon (Qwen/StarCoder), InfoNCE loss formula snippet, output = trained retriever
33	- Bottom annotation: "Static mining — computed once, no re-mining during training"
34	
35	**Data source**: No empirical data needed. Schematic only.
36	
37	**Design notes**:
38	- Color: 3 distinct colors for the 3 strategies — use Okabe-Ito palette consistently across all figures (orange=#E69F00 for random, blue=#0072B2 for embedding, green=#009E73 for dataflow)
39	- Rounded rectangles, thin arrows, sans-serif labels
40	- Reference style: similar to ANCE (Xiong et al. 2021) Fig 1, or DPR (Karpukhin et al. 2020) pipeline diagrams
41	- Tools: TikZ or draw.io → PDF export
42	
43	**Priority**: **必须** — every methods paper needs a pipeline figure
44	
45	---
46	
47	## Figure 2: Negative Mining Strategies Illustration
48	
49	**Purpose**: Make the 3 strategies intuitive. Directly supports §3.4 and helps readers understand what "structurally disconnected but textually similar" means concretely.
50	
51	**Layout**: Full-width. 3 panels side by side, each showing the same mini-repo graph with different negative selections highlighted.
52	
53	Panel structure (each ~2.2in wide):
54	```
55	(a) Random               (b) Embedding-distance      (c) Dataflow-aware
56	┌─────────────────┐      ┌─────────────────┐         ┌─────────────────┐
57	│  ○ ○ ○ ○ ○      │      │  ○ ○ ○ ○ ○      │         │  ○ ○ ○ ○ ○      │
58	│   /  \           │      │   /  \           │         │   /  \           │
59	│  ○────○          │      │  ○────○          │         │  ○────○          │
60	│  query  pos      │      │  query  pos      │         │  query  pos      │
61	│                  │      │                  │         │                  │
62	│  neg₁ neg₂ neg₃ │      │  neg₁ neg₂ neg₃ │         │  neg₁ neg₂ neg₃ │
63	│  (scattered)     │      │  (close to query)│         │  (close but      │
64	│                  │      │                  │         │   disconnected)  │
65	└─────────────────┘      └─────────────────┘         └─────────────────┘
66	```
67	
68	Each panel shows:
69	- File nodes arranged as a graph with data-flow edges (solid lines)
70	- Query node (star marker, fixed position)
71	- Gold/positive file (green fill, connected to query via data-flow)
72	- Selected negatives (red/highlighted, position varies by strategy)
73	- (a) Random: negatives scattered randomly, most far from query
74	- (b) Embedding: negatives clustered near query in embedding space (shown as spatial proximity), some connected via data-flow
75	- (c) Dataflow: negatives near query in embedding space BUT with no data-flow edges to gold files — dashed lines showing "no connection"
76	
77	Key visual element: data-flow edges drawn as solid gray lines between connected nodes; absence of edges for dataflow-aware negatives emphasized with ✕ or dotted-line-with-cross.
78	
79	**Data source**: No empirical data. Use a stylized 8-10 node example.
80	
81	**Design notes**:
82	- Same 3-color scheme as Figure 1 for strategy identity
83	- Negative nodes: filled with strategy color; non-selected nodes: light gray
84	- Add a small "sim(q, f⁻)" annotation showing relative similarity values
85	- Reference style: similar to GraphCodeBERT (Guo et al. 2021) data-flow illustrations
86	- This is the figure that makes the paper "click" for reviewers — invest design effort here
87	
88	**Priority**: **必须** — critical for paper comprehension
89	
90	---
91	
92	## Figure 3: Main Results Comparison
93	
94	**Purpose**: Visual summary of Table 1 main results. Supports Claim 1 (embedding mining suffices) and Claim 2 (dataflow encoder-dependent).
95	
96	**Layout**: Single-column width (~3.25in). Grouped bar chart.
97	
98	```
99	         Qwen2.5-Coder-3B              StarCoder2-3B
100	    ┌───────────────────────┐     ┌───────────────────────┐
101	R@1 │  ██ ██ ██ ██          │     │  ██ ██ ██ ██          │
102	    │  Ra BM Em DF          │     │  Ra BM Em DF          │
103	    └───────────────────────┘     └───────────────────────┘
104	```
105	
106	- X-axis: 4 strategies (Random, BM25-mined, Embedding-distance, Dataflow-aware)
107	- Y-axis: R@1 (truncated axis starting from a reasonable baseline, e.g., 0.40)
108	- Error bars: ±1 std across 3 seeds
109	- Two panels side-by-side for the two encoders
110	- Horizontal dashed line: BM25 retrieval baseline (no training)
111	- Significance annotations: bracket + asterisk for statistically significant differences (bootstrap 95% CI)
112	
113	**Data source**: Table 1 from experiments_v1.md — currently placeholder values. M2 full runs in progress:
114	- Qwen random: s42=0.5527, s43=0.5554, s44 running (eval@500: 0.6009)
115	- StarCoder random: s42=0.4604, s43 running (eval@500: 0.4708)
116	- Embedding/dataflow seeds: not yet started
117	- **Available for figure**: after M2 completes (~3-4 days)
118	
119	**Design notes**:
120	- Truncated y-axis to magnify differences (document the truncation clearly)
121	- Okabe-Ito colors consistent with Fig 1-2
122	- Consider adding a small inset or annotation showing the delta (pp improvement) above embedding bars
123	- Alternative: radar/spider chart showing R@1/R@5/MRR simultaneously — but bar chart is cleaner for the primary claim
124	
125	**Priority**: **必须** — main evidence figure. Cannot be finalized until M2 completes.
126	
127	---
128	
129	## Figure 4: Representation Geometry & Negative Difficulty
130	
131	**Purpose**: Visual evidence for the mechanistic hypothesis (Claim 2). Shows WHY embedding mining works and why dataflow interacts with encoder geometry.
132	
133	**Layout**: Full-width. Composite figure with 2-3 panels. Recommend merging/adapting from the 3 existing charts.
134	
135	### Panel (a): Margin Comparison (adapting existing `neg_difficulty_margin_comparison`)
136	```
137	   Qwen (saturated)           StarCoder (healthy)
138	   pos_sim ≈ 0.986            pos_sim ≈ 0.80
139	┌──────────────────┐        ┌──────────────────┐
140	│  ████ ████ ████  │        │  ████ ████ ████  │
141	│  neg_sim  margin │        │  neg_sim  margin │
142	│  Ra   Em   DF   │        │  Ra   Em   DF   │
143	└──────────────────┘        └──────────────────┘
144	```
145	- Stacked bars: neg_sim (bottom, lighter) + margin (top, darker)
146	- Dashed horizontal line at pos_sim level
147	- Qwen: tiny margins (0.017–0.074), visually compressed
148	- StarCoder: larger margins (0.067–0.194), visually spread
149	- Key message: StarCoder has 2.6–4.1× more room to separate
150	
151	### Panel (b): Similarity Distribution (adapting existing `neg_difficulty_similarity_dist`)
152	- Violin or KDE plot showing full distribution of query-negative cosine similarities
153	- 3 strategies overlaid per encoder
154	- Qwen: distributions tightly packed near 0.95–0.99
155	- StarCoder: distributions spread across 0.4–0.8
156	- Shows not just means but distribution shape — important for understanding tail behavior
157	
158	### Panel (c): Margin Ratio Heatmap (evaluate whether needed)
159	- 2×3 heatmap: encoders × strategies, cell value = SC/Qwen margin ratio
160	- May be redundant with panel (a) — consider dropping if space is tight
161	- Alternative: include as supplementary material
162	
163	**Data source**: `neg_difficulty_stats_v3_2048.json` on server. All data available now.
164	- Qwen 2048t: random margin=0.074, embedding margin=0.017, dataflow margin=0.029
165	- StarCoder 2048t: random margin=0.194, embedding margin=0.067, dataflow margin=0.119
166	- SC/Qwen ratio: random=2.61, embedding=3.94, dataflow=4.07
167	
168	**Existing charts** (on server, need evaluation):
169	- `neg_difficulty_margin_comparison.{pdf,png}` — 1×2 stacked bar, Okabe-Ito, 300 DPI
170	- `neg_difficulty_similarity_dist.{pdf,png}` — distribution plot
171	- `neg_difficulty_ratio_heatmap.{pdf,png}` — ratio heatmap
172	
173	**Design notes**:
174	- Panels (a)+(b) are the strongest combination — (a) shows aggregate, (b) shows distribution
175	- Drop panel (c) from main paper, move to appendix if needed
176	- Add margin value annotations directly on bars in panel (a)
177	- Ensure axis labels are readable at ACL column width
178	- Consider adding a schematic inset in panel (a) showing "saturated" vs "healthy" embedding space as 2D projections
179	
180	**Priority**: **必须** — key mechanistic evidence figure. Data already available, can be produced now.
181	
182	---
183	
184	## Figure 5: Pool Size Sensitivity
185	
186	**Purpose**: Robustness check — show that strategy rankings hold across evaluation pool sizes. Addresses anticipated reviewer concern about pool size = 50 being too small.
187	
188	**Layout**: Single-column width. Line plot with 2 panels (Qwen, StarCoder) or overlaid.
189	
190	```
191	R@1
192	 │     ─●─ Embedding
193	 │     ─○─ Random
194	 │     ─△─ Dataflow
195	 │
196	 └──────────────────→
197	   50  100  200  500
198	        Pool Size
199	```
200	
201	- X-axis: pool size {50, 100, 200, 500}
202	- Y-axis: R@1
203	- 3 lines per encoder (one per strategy)
204	- Error bands: ±1 std (3 seeds)
205	- Key message: embedding > random gap persists (or widens) at larger pool sizes
206	
207	**Data source**: plan_019 — not yet executed. Requires M2 best checkpoints + re-evaluation at different pool sizes.
208	- **Available for figure**: after M2 completes + plan_019 runs (~4-5 days)
209	
210	**Design notes**:
211	- If gap widens at larger pools, this strengthens the paper substantially
212	- If gap closes, need careful framing — "sufficient at practical pool sizes"
213	- Log-scale x-axis may be cleaner
214	
215	**Priority**: **建议** — strong robustness evidence, likely requested by reviewers. Can be table-only (Table 3) if figure space is tight.
216	
217	---
218	
219	## Figure 6: Training Dynamics (Learning Curves)
220	
221	**Purpose**: Show training behavior differences across strategies — does embedding mining converge faster? Is there overfitting divergence?
222	
223	**Layout**: Single-column width. 2×1 panels (Qwen top, StarCoder bottom) or 1×2 side-by-side.
224	
225	```
226	R@1
227	 │    /──── Embedding
228	 │   / ──── Dataflow
229	 │  / ──── Random
230	 │ /
231	 └──────────────────→
232	   0   500  1000 1500 2000
233	          Training Step
234	```
235	
236	- X-axis: training steps
237	- Y-axis: validation R@1 (or val loss)
238	- 3 curves per encoder
239	- Shaded regions: ±1 std across seeds
240	- Mark best checkpoint with ★
241	- Show overfitting region (s42 3-epoch run provides this data)
242	
243	**Data source**: M2 training logs — partially available (random s42 curves for both encoders). Full data after M2 completes.
244	- Qwen random s42: R@1 peaks at step 1000 (0.5527), then oscillates
245	- StarCoder random s42: R@1 peaks at step 2500 (0.4604), slower convergence
246	
247	**Design notes**:
248	- This figure is information-dense but potentially very insightful
249	- Alternative: move to appendix, show only val_loss in main paper
250	- Can combine with dual-checkpoint analysis (val_loss vs R@1 divergence for StarCoder)
251	
252	**Priority**: **可选** — informative but not essential for claims. Consider appendix placement.
253	
254	---
255	
256	## Figure 7: SWE-bench Downstream Results
257	
258	**Purpose**: Validate that retrieval improvements translate to real-world bug fixing. Supports external validity.
259	
260	**Layout**: Single-column width. Simple bar chart or table figure.
261	
262	```
263	Resolve Rate (%)
264	 │  ██ BM25
265	 │  ██ Random-trained
266	 │  ██ Embedding-trained
267	 │
268	 └──────────────────→
269	```
270	
271	- X-axis: retriever variant
272	- Y-axis: resolve rate (%)
273	- 3 bars (BM25 baseline, random-trained, embedding-trained)
274	- Optional: add confidence intervals if multiple runs
275	
276	**Data source**: plan_003 — not yet executed. Requires M2 best checkpoints + SWE-bench Lite evaluation pipeline.
277	- **Available for figure**: after plan_003 completes (~post-M2)
278	
279	**Design notes**:
280	- If improvement is small (<2pp), present as table instead of figure
281	- If improvement is substantial, this becomes a highlight figure
282	- Consider showing per-category breakdown (by repo or difficulty tier) if data allows
283	
284	**Priority**: **建议** — high impact if results are strong. Space decision depends on effect size.
285	
286	---
287	
288	## Figure 8: Stratified Analysis by Structural Data Availability
289	
290	**Purpose**: Disentangle the dataflow strategy's effectiveness from confound variables (repo size, pool size). Addresses the 99.3% rich-dataflow-in-large-repos confound identified in plan_005.
291	
292	**Layout**: Single-column width. Grouped bar chart with 3 strata.
293	
294	```
295	R@1 Delta (Emb vs DF)
296	 │  ██ Rich dataflow (≥5 edges)
297	 │  ██ Sparse (1-4 edges)
298	 │  ██ No structural data
299	 │
300	 └──────────────────→
301	      Qwen    StarCoder
302	```
303	
304	- Show per-stratum R@1 delta between embedding and dataflow strategies
305	- Control for pool size (use within-bin comparison from plan_005 design)
306	- Mark underpowered strata (n<30) with hatching
307	
308	**Data source**: plan_005 — script ready, awaiting M2 checkpoints.
309	- Confound analysis available: rich-dataflow 99.3% in large/xlarge repos
310	- **Available for figure**: after M2 + plan_005 evaluation
311	
312	**Design notes**:
313	- This is the most technically nuanced figure — may be better as a table (Table 5)
314	- If dataflow benefit is stratum-dependent, figure is more effective than table
315	- Include pool-size-controlled numbers to address the confound
316	
317	**Priority**: **可选** — important for Claim 2 depth, but table may suffice. Move to appendix if main paper is tight.
318	
319	---
320	
321	## Summary & Production Timeline
322	
323	| Figure | Type | Purpose | Data Ready? | Priority | Estimated Effort |
324	|--------|------|---------|-------------|----------|-----------------|
325	| Fig 1: Pipeline | Schematic | Method overview | Yes (no data) | 必须 | 4-6h (TikZ/draw.io) |
326	| Fig 2: Mining Strategies | Schematic | Strategy intuition | Yes (no data) | 必须 | 3-4h (TikZ) |
327	| Fig 3: Main Results | Bar chart | Claim 1 evidence | No (M2 running) | 必须 | 1h (matplotlib) |
328	| Fig 4: Rep. Geometry | Composite | Claim 2 mechanism | Yes (v3 data) | 必须 | 2-3h (refine existing) |
329	| Fig 5: Pool Sensitivity | Line plot | Robustness | No (plan_019) | 建议 | 1h (matplotlib) |
330	| Fig 6: Training Curves | Line plot | Training dynamics | Partial | 可选 | 1h (matplotlib) |
331	| Fig 7: SWE-bench | Bar chart | Downstream validity | No (plan_003) | 建议 | 1h (matplotlib) |
332	| Fig 8: Stratified | Bar chart | Confound control | No (plan_005) | 可选 | 1-2h (matplotlib) |
333	
334	**Space budget**: ACL 2-column format typically allows 5-7 figures in 8 pages. Recommend 4 必须 figures in main paper + 1-2 建议 figures. 可选 figures go to appendix.
335	
336	**Production order**:
337	1. Fig 4 (data ready now — refine existing charts)
338	2. Fig 1 + Fig 2 (schematics, no data dependency)
339	3. Fig 3 (after M2 completes)
340	4. Fig 5/7 (after respective plans complete)
341	
342	**Color scheme** (Okabe-Ito, consistent across all figures):
343	- Random: #E69F00 (orange)
344	- Embedding-distance: #0072B2 (blue)
345	- Dataflow-aware: #009E73 (green)
346	- BM25: #CC79A7 (pink/mauve)
347	- Qwen encoder: solid lines/fills
348	- StarCoder encoder: hatched fills or dashed lines
349	
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "parentUuid": "8c0467d3-93bf-442f-81bb-2862d2e0e8a6",
  "isSidechain": false,
  "promptId": "82620338-1cd7-4c43-9283-e5cb821c1607",
  "type": "user",
  "uuid": "458dcb02-c075-407c-9aa3-ab9d1f8e9fa4",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/figure_design_v1.md",
      "content": "# Figure Design — StructFuse Paper\n\nTarget: EMNLP 2026 Main (ARR May 25 deadline)\nStyle: Two-column ACL format, max width ~3.25in (single col) or ~6.75in (full width)\n\n---\n\n## Figure 1: StructFuse Pipeline Overview\n\n**Purpose**: Establish the full method at a glance. Supports Claim 3 (CodeQL pipeline practicality) and orients the reader for §3.\n\n**Layout**: Full-width (2-column span). Left-to-right flow diagram with 4 major blocks:\n\n```\n[Input]              [Extraction]           [Mining]              [Training]\n┌──────────┐      ┌──────────────┐      ┌──────────────┐      ┌──────────────┐\n│ Repo +   │ ──→  │ CodeQL       │ ──→  │ Negative     │ ──→  │ Contrastive  │\n│ Bug      │      │ Data-flow    │      │ Mining       │      │ Fine-tuning  │\n│ Report   │      │ Analysis     │      │ (3 strats)   │      │ (InfoNCE)    │\n└──────────┘      └──────────────┘      └──────────────┘      └──────────────┘\n                        │                      │\n                   Structural            ┌─────┴─────┐\n                   Graph G               │ Random    │\n                                         │ Embedding │\n                                         │ Dataflow  │\n                                         └───────────┘\n```\n\n- Input block: repo file tree icon + issue/bug report text snippet\n- Extraction block: CodeQL logo/icon, arrows showing inter-procedural data-flow paths crossing file boundaries, output = Graph G (nodes=files, edges=data-flow)\n- Mining block: 3 parallel branches for the 3 strategies, each with a mini-icon (dice for random, cosine curve for embedding, graph for dataflow). Show query → candidate selection for each\n- Training block: encoder icon (Qwen/StarCoder), InfoNCE loss formula snippet, output = trained retriever\n- Bottom annotation: \"Static mining — computed once, no re-mining during training\"\n\n**Data source**: No empirical data needed. Schematic only.\n\n**Design notes**:\n- Color: 3 distinct colors for the 3 strategies — use Okabe-Ito palette consistently across all figures (orange=#E69F00 for random, blue=#0072B2 for embedding, green=#009E73 for dataflow)\n- Rounded rectangles, thin arrows, sans-serif labels\n- Reference style: similar to ANCE (Xiong et al. 2021) Fig 1, or DPR (Karpukhin et al. 2020) pipeline diagrams\n- Tools: TikZ or draw.io → PDF export\n\n**Priority**: **必须** — every methods paper needs a pipeline figure\n\n---\n\n## Figure 2: Negative Mining Strategies Illustration\n\n**Purpose**: Make the 3 strategies intuitive. Directly supports §3.4 and helps readers understand what \"structurally disconnected but textually similar\" means concretely.\n\n**Layout**: Full-width. 3 panels side by side, each showing the same mini-repo graph with different negative selections highlighted.\n\nPanel structure (each ~2.2in wide):\n```\n(a) Random               (b) Embedding-distance      (c) Dataflow-aware\n┌─────────────────┐      ┌─────────────────┐         ┌─────────────────┐\n│  ○ ○ ○ ○ ○      │      │  ○ ○ ○ ○ ○      │         │  ○ ○ ○ ○ ○      │\n│   /  \\           │      │   /  \\           │         │   /  \\           │\n│  ○────○          │      │  ○────○          │         │  ○────○          │\n│  query  pos      │      │  query  pos      │         │  query  pos      │\n│                  │      │                  │         │                  │\n│  neg₁ neg₂ neg₃ │      │  neg₁ neg₂ neg₃ │         │  neg₁ neg₂ neg₃ │\n│  (scattered)     │      │  (close to query)│         │  (close but      │\n│                  │      │                  │         │   disconnected)  │\n└─────────────────┘      └─────────────────┘         └─────────────────┘\n```\n\nEach panel shows:\n- File nodes arranged as a graph with data-flow edges (solid lines)\n- Query node (star marker, fixed position)\n- Gold/positive file (green fill, connected to query via data-flow)\n- Selected negatives (red/highlighted, position varies by strategy)\n- (a) Random: negatives scattered randomly, most far from query\n- (b) Embedding: negatives clustered near query in embedding space (shown as spatial proximity), some connected via data-flow\n- (c) Dataflow: negatives near query in embedding space BUT with no data-flow edges to gold files — dashed lines showing \"no connection\"\n\nKey visual element: data-flow edges drawn as solid gray lines between connected nodes; absence of edges for dataflow-aware negatives emphasized with ✕ or dotted-line-with-cross.\n\n**Data source**: No empirical data. Use a stylized 8-10 node example.\n\n**Design notes**:\n- Same 3-color scheme as Figure 1 for strategy identity\n- Negative nodes: filled with strategy color; non-selected nodes: light gray\n- Add a small \"sim(q, f⁻)\" annotation showing relative similarity values\n- Reference style: similar to GraphCodeBERT (Guo et al. 2021) data-flow illustrations\n- This is the figure that makes the paper \"click\" for reviewers — invest design effort here\n\n**Priority**: **必须** — critical for paper comprehension\n\n---\n\n## Figure 3: Main Results Comparison\n\n**Purpose**: Visual summary of Table 1 main results. Supports Claim 1 (embedding mining suffices) and Claim 2 (dataflow encoder-dependent).\n\n**Layout**: Single-column width (~3.25in). Grouped bar chart.\n\n```\n         Qwen2.5-Coder-3B              StarCoder2-3B\n    ┌───────────────────────┐     ┌───────────────────────┐\nR@1 │  ██ ██ ██ ██          │     │  ██ ██ ██ ██          │\n    │  Ra BM Em DF          │     │  Ra BM Em DF          │\n    └───────────────────────┘     └───────────────────────┘\n```\n\n- X-axis: 4 strategies (Random, BM25-mined, Embedding-distance, Dataflow-aware)\n- Y-axis: R@1 (truncated axis starting from a reasonable baseline, e.g., 0.40)\n- Error bars: ±1 std across 3 seeds\n- Two panels side-by-side for the two encoders\n- Horizontal dashed line: BM25 retrieval baseline (no training)\n- Significance annotations: bracket + asterisk for statistically significant differences (bootstrap 95% CI)\n\n**Data source**: Table 1 from experiments_v1.md — currently placeholder values. M2 full runs in progress:\n- Qwen random: s42=0.5527, s43=0.5554, s44 running (eval@500: 0.6009)\n- StarCoder random: s42=0.4604, s43 running (eval@500: 0.4708)\n- Embedding/dataflow seeds: not yet started\n- **Available for figure**: after M2 completes (~3-4 days)\n\n**Design notes**:\n- Truncated y-axis to magnify differences (document the truncation clearly)\n- Okabe-Ito colors consistent with Fig 1-2\n- Consider adding a small inset or annotation showing the delta (pp improvement) above embedding bars\n- Alternative: radar/spider chart showing R@1/R@5/MRR simultaneously — but bar chart is cleaner for the primary claim\n\n**Priority**: **必须** — main evidence figure. Cannot be finalized until M2 completes.\n\n---\n\n## Figure 4: Representation Geometry & Negative Difficulty\n\n**Purpose**: Visual evidence for the mechanistic hypothesis (Claim 2). Shows WHY embedding mining works and why dataflow interacts with encoder geometry.\n\n**Layout**: Full-width. Composite figure with 2-3 panels. Recommend merging/adapting from the 3 existing charts.\n\n### Panel (a): Margin Comparison (adapting existing `neg_difficulty_margin_comparison`)\n```\n   Qwen (saturated)           StarCoder (healthy)\n   pos_sim ≈ 0.986            pos_sim ≈ 0.80\n┌──────────────────┐        ┌──────────────────┐\n│  ████ ████ ████  │        │  ████ ████ ████  │\n│  neg_sim  margin │        │  neg_sim  margin │\n│  Ra   Em   DF   │        │  Ra   Em   DF   │\n└──────────────────┘        └──────────────────┘\n```\n- Stacked bars: neg_sim (bottom, lighter) + margin (top, darker)\n- Dashed horizontal line at pos_sim level\n- Qwen: tiny margins (0.017–0.074), visually compressed\n- StarCoder: larger margins (0.067–0.194), visually spread\n- Key message: StarCoder has 2.6–4.1× more room to separate\n\n### Panel (b): Similarity Distribution (adapting existing `neg_difficulty_similarity_dist`)\n- Violin or KDE plot showing full distribution of query-negative cosine similarities\n- 3 strategies overlaid per encoder\n- Qwen: distributions tightly packed near 0.95–0.99\n- StarCoder: distributions spread across 0.4–0.8\n- Shows not just means but distribution shape — important for understanding tail behavior\n\n### Panel (c): Margin Ratio Heatmap (evaluate whether needed)\n- 2×3 heatmap: encoders × strategies, cell value = SC/Qwen margin ratio\n- May be redundant with panel (a) — consider dropping if space is tight\n- Alternative: include as supplementary material\n\n**Data source**: `neg_difficulty_stats_v3_2048.json` on server. All data available now.\n- Qwen 2048t: random margin=0.074, embedding margin=0.017, dataflow margin=0.029\n- StarCoder 2048t: random margin=0.194, embedding margin=0.067, dataflow margin=0.119\n- SC/Qwen ratio: random=2.61, embedding=3.94, dataflow=4.07\n\n**Existing charts** (on server, need evaluation):\n- `neg_difficulty_margin_comparison.{pdf,png}` — 1×2 stacked bar, Okabe-Ito, 300 DPI\n- `neg_difficulty_similarity_dist.{pdf,png}` — distribution plot\n- `neg_difficulty_ratio_heatmap.{pdf,png}` — ratio heatmap\n\n**Design notes**:\n- Panels (a)+(b) are the strongest combination — (a) shows aggregate, (b) shows distribution\n- Drop panel (c) from main paper, move to appendix if needed\n- Add margin value annotations directly on bars in panel (a)\n- Ensure axis labels are readable at ACL column width\n- Consider adding a schematic inset in panel (a) showing \"saturated\" vs \"healthy\" embedding space as 2D projections\n\n**Priority**: **必须** — key mechanistic evidence figure. Data already available, can be produced now.\n\n---\n\n## Figure 5: Pool Size Sensitivity\n\n**Purpose**: Robustness check — show that strategy rankings hold across evaluation pool sizes. Addresses anticipated reviewer concern about pool size = 50 being too small.\n\n**Layout**: Single-column width. Line plot with 2 panels (Qwen, StarCoder) or overlaid.\n\n```\nR@1\n │     ─●─ Embedding\n │     ─○─ Random\n │     ─△─ Dataflow\n │\n └──────────────────→\n   50  100  200  500\n        Pool Size\n```\n\n- X-axis: pool size {50, 100, 200, 500}\n- Y-axis: R@1\n- 3 lines per encoder (one per strategy)\n- Error bands: ±1 std (3 seeds)\n- Key message: embedding > random gap persists (or widens) at larger pool sizes\n\n**Data source**: plan_019 — not yet executed. Requires M2 best checkpoints + re-evaluation at different pool sizes.\n- **Available for figure**: after M2 completes + plan_019 runs (~4-5 days)\n\n**Design notes**:\n- If gap widens at larger pools, this strengthens the paper substantially\n- If gap closes, need careful framing — \"sufficient at practical pool sizes\"\n- Log-scale x-axis may be cleaner\n\n**Priority**: **建议** — strong robustness evidence, likely requested by reviewers. Can be table-only (Table 3) if figure space is tight.\n\n---\n\n## Figure 6: Training Dynamics (Learning Curves)\n\n**Purpose**: Show training behavior differences across strategies — does embedding mining converge faster? Is there overfitting divergence?\n\n**Layout**: Single-column width. 2×1 panels (Qwen top, StarCoder bottom) or 1×2 side-by-side.\n\n```\nR@1\n │    /──── Embedding\n │   / ──── Dataflow\n │  / ──── Random\n │ /\n └──────────────────→\n   0   500  1000 1500 2000\n          Training Step\n```\n\n- X-axis: training steps\n- Y-axis: validation R@1 (or val loss)\n- 3 curves per encoder\n- Shaded regions: ±1 std across seeds\n- Mark best checkpoint with ★\n- Show overfitting region (s42 3-epoch run provides this data)\n\n**Data source**: M2 training logs — partially available (random s42 curves for both encoders). Full data after M2 completes.\n- Qwen random s42: R@1 peaks at step 1000 (0.5527), then oscillates\n- StarCoder random s42: R@1 peaks at step 2500 (0.4604), slower convergence\n\n**Design notes**:\n- This figure is information-dense but potentially very insightful\n- Alternative: move to appendix, show only val_loss in main paper\n- Can combine with dual-checkpoint analysis (val_loss vs R@1 divergence for StarCoder)\n\n**Priority**: **可选** — informative but not essential for claims. Consider appendix placement.\n\n---\n\n## Figure 7: SWE-bench Downstream Results\n\n**Purpose**: Validate that retrieval improvements translate to real-world bug fixing. Supports external validity.\n\n**Layout**: Single-column width. Simple bar chart or table figure.\n\n```\nResolve Rate (%)\n │  ██ BM25\n │  ██ Random-trained\n │  ██ Embedding-trained\n │\n └──────────────────→\n```\n\n- X-axis: retriever variant\n- Y-axis: resolve rate (%)\n- 3 bars (BM25 baseline, random-trained, embedding-trained)\n- Optional: add confidence intervals if multiple runs\n\n**Data source**: plan_003 — not yet executed. Requires M2 best checkpoints + SWE-bench Lite evaluation pipeline.\n- **Available for figure**: after plan_003 completes (~post-M2)\n\n**Design notes**:\n- If improvement is small (<2pp), present as table instead of figure\n- If improvement is substantial, this becomes a highlight figure\n- Consider showing per-category breakdown (by repo or difficulty tier) if data allows\n\n**Priority**: **建议** — high impact if results are strong. Space decision depends on effect size.\n\n---\n\n## Figure 8: Stratified Analysis by Structural Data Availability\n\n**Purpose**: Disentangle the dataflow strategy's effectiveness from confound variables (repo size, pool size). Addresses the 99.3% rich-dataflow-in-large-repos confound identified in plan_005.\n\n**Layout**: Single-column width. Grouped bar chart with 3 strata.\n\n```\nR@1 Delta (Emb vs DF)\n │  ██ Rich dataflow (≥5 edges)\n │  ██ Sparse (1-4 edges)\n │  ██ No structural data\n │\n └──────────────────→\n      Qwen    StarCoder\n```\n\n- Show per-stratum R@1 delta between embedding and dataflow strategies\n- Control for pool size (use within-bin comparison from plan_005 design)\n- Mark underpowered strata (n<30) with hatching\n\n**Data source**: plan_005 — script ready, awaiting M2 checkpoints.\n- Confound analysis available: rich-dataflow 99.3% in large/xlarge repos\n- **Available for figure**: after M2 + plan_005 evaluation\n\n**Design notes**:\n- This is the most technically nuanced figure — may be better as a table (Table 5)\n- If dataflow benefit is stratum-dependent, figure is more effective than table\n- Include pool-size-controlled numbers to address the confound\n\n**Priority**: **可选** — important for Claim 2 depth, but table may suffice. Move to appendix if main paper is tight.\n\n---\n\n## Summary & Production Timeline\n\n| Figure | Type | Purpose | Data Ready? | Priority | Estimated Effort |\n|--------|------|---------|-------------|----------|-----------------|\n| Fig 1: Pipeline | Schematic | Method overview | Yes (no data) | 必须 | 4-6h (TikZ/draw.io) |\n| Fig 2: Mining Strategies | Schematic | Strategy intuition | Yes (no data) | 必须 | 3-4h (TikZ) |\n| Fig 3: Main Results | Bar chart | Claim 1 evidence | No (M2 running) | 必须 | 1h (matplotlib) |\n| Fig 4: Rep. Geometry | Composite | Claim 2 mechanism | Yes (v3 data) | 必须 | 2-3h (refine existing) |\n| Fig 5: Pool Sensitivity | Line plot | Robustness | No (plan_019) | 建议 | 1h (matplotlib) |\n| Fig 6: Training Curves | Line plot | Training dynamics | Partial | 可选 | 1h (matplotlib) |\n| Fig 7: SWE-bench | Bar chart | Downstream validity | No (plan_003) | 建议 | 1h (matplotlib) |\n| Fig 8: Stratified | Bar chart | Confound control | No (plan_005) | 可选 | 1-2h (matplotlib) |\n\n**Space budget**: ACL 2-column format typically allows 5-7 figures in 8 pages. Recommend 4 必须 figures in main paper + 1-2 建议 figures. 可选 figures go to appendix.\n\n**Production order**:\n1. Fig 4 (data ready now — refine existing charts)\n2. Fig 1 + Fig 2 (schematics, no data dependency)\n3. Fig 3 (after M2 completes)\n4. Fig 5/7 (after respective plans complete)\n\n**Color scheme** (Okabe-Ito, consistent across all figures):\n- Random: #E69F00 (orange)\n- Embedding-distance: #0072B2 (blue)\n- Dataflow-aware: #009E73 (green)\n- BM25: #CC79A7 (pink/mauve)\n- Qwen encoder: solid lines/fills\n- StarCoder encoder: hatched fills or dashed lines\n",
      "numLines": 349,
      "startLine": 1,
      "totalLines": 349
    }
  },
  "sourceToolAssistantUUID": "8c0467d3-93bf-442f-81bb-2862d2e0e8a6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "999f865e-f544-467f-b7e8-732fb33862f3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
````

</details>

---

### Tool call

_source line 36 · 2026-05-15T01:58:40.996Z_

<details open><summary>🔧 Tool call — Read · `toolu_01KxtWDfdZbYmpMhUnS8cdK2`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/experimental_setup_k_checkpoint.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "458dcb02-c075-407c-9aa3-ab9d1f8e9fa4",
  "isSidechain": false,
  "requestId": "req_011Cb3XV3RNgjKXqkRNHfAAo",
  "type": "assistant",
  "uuid": "bbf8bf43-20ac-4342-a56f-39ee809fcaf5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "999f865e-f544-467f-b7e8-732fb33862f3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RmtrSWnaQ6G4HTR38aWSQJ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7521,
      "cache_read_input_tokens": 23676,
      "output_tokens": 640,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 7521,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 640,
          "cache_read_input_tokens": 23676,
          "cache_creation_input_tokens": 7521,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 7521
          },
          "type": "message"
        }
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

_source line 37 · 2026-05-15T01:58:41.067Z_

```json
{
  "parentUuid": "4df6b46e-758d-413d-a00c-90e4d76eb904",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "fb23a75e-76e9-46d5-aafd-bd6a07b30695",
  "timestamp": "2026-05-15T01:58:41.067Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "999f865e-f544-467f-b7e8-732fb33862f3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 38_

```json
{
  "type": "last-prompt",
  "leafUuid": "fb23a75e-76e9-46d5-aafd-bd6a07b30695",
  "sessionId": "999f865e-f544-467f-b7e8-732fb33862f3"
}
```

---

### Runtime record

_source line 39_

```json
{
  "type": "ai-title",
  "aiTitle": "Review Claim 2 wording defensiveness",
  "sessionId": "999f865e-f544-467f-b7e8-732fb33862f3"
}
```

---

### Assistant

_source line 40 · 2026-05-15T01:58:45.058Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the material. Let me also read the decisions file to get D035 context.

Actually, let me check if there's a decisions.yaml file with D035.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fb23a75e-76e9-46d5-aafd-bd6a07b30695",
  "isSidechain": false,
  "requestId": "req_011Cb3XVnBNfwVkMkKa1z5DC",
  "type": "assistant",
  "uuid": "fa0a7df5-24ff-484e-a85c-efb66e11efb9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "999f865e-f544-467f-b7e8-732fb33862f3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016wPf4ZD1Ym8PAXDQGshZSo",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 20767,
      "cache_read_input_tokens": 31197,
      "output_tokens": 174,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 20767,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 174,
          "cache_read_input_tokens": 31197,
          "cache_creation_input_tokens": 20767,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 20767
          },
          "type": "message"
        }
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

_source line 41 · 2026-05-15T01:58:46.034Z_

Let me also check the decisions file for D035 context.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fa0a7df5-24ff-484e-a85c-efb66e11efb9",
  "isSidechain": false,
  "requestId": "req_011Cb3XVnBNfwVkMkKa1z5DC",
  "type": "assistant",
  "uuid": "f7025c36-4cf4-4338-a8f6-1a1f373948b5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "999f865e-f544-467f-b7e8-732fb33862f3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016wPf4ZD1Ym8PAXDQGshZSo",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 20767,
      "cache_read_input_tokens": 31197,
      "output_tokens": 174,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 20767,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 174,
          "cache_read_input_tokens": 31197,
          "cache_creation_input_tokens": 20767,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 20767
          },
          "type": "message"
        }
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

_source line 42 · 2026-05-15T01:58:46.928Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_012VZ57WtykYXwmrrzjaGjkG`</summary>

```json
{
  "project": "structfuse-context",
  "file": "decisions.yaml",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f7025c36-4cf4-4338-a8f6-1a1f373948b5",
  "isSidechain": false,
  "requestId": "req_011Cb3XVnBNfwVkMkKa1z5DC",
  "type": "assistant",
  "uuid": "4bb89274-0b46-465b-b6f6-aaa3090d327b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "999f865e-f544-467f-b7e8-732fb33862f3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016wPf4ZD1Ym8PAXDQGshZSo",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 20767,
      "cache_read_input_tokens": 31197,
      "output_tokens": 174,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 20767,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 174,
          "cache_read_input_tokens": 31197,
          "cache_creation_input_tokens": 20767,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 20767
          },
          "type": "message"
        }
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

_source line 43 · 2026-05-15T01:58:46.941Z_

<details><summary>↩ Tool result · `toolu_012VZ57WtykYXwmrrzjaGjkG`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/decisions.yaml\", \"content\": \"_next_id: 41\\ndecisions:\\n- id: D001\\n  date: 2026-05-12 09:57 UTC\\n  summary: 'MVP 设计: CodeQL 试点(10 repos) + 迷你对比训练(500 instances) 验证核心假设'\\n  rationale: 13 天 DDL，需要最快速验证核心假设链：(1) CodeQL inter-procedural data-flow 在 Python\\n    repos 上可行（timeout < 30%），(2) data-flow hard negatives 比 random negatives 提升检索\\n    recall。两个 phase 串行，总计约 1 天。通过后立即进入全量数据提取和训练。\\n  related_experiments: []\\n  depends_on: []\\n- id: D002\\n  date: 2026-05-12 10:01 UTC\\n  summary: '采纳 Reviewer 反馈: MVP Phase 2 增加线性分类器 proxy 验证 + 3-seed 训练 + 显式 kill criteria'\\n  rationale: 'Reviewer 指出 Phase 2 原方案（500 instances, ~100 held-out, 2pp gate）统计效力不足，2pp\\n    差异在随机噪声范围内。增加: (1) Phase 2a 线性分类器 proxy 验证解耦特征质量与训练策略；(2) 3-seed 训练要求 ≥2/3 seed\\n    提升；(3) 每个 phase 的 fail→kill/fallback 路径。防止 13 天 DDL 下的沉没成本陷阱。'\\n  related_experiments: []\\n  depends_on:\\n  - D001\\n- id: D003\\n  date: 2026-05-12 10:02 UTC\\n  summary: 'H2 验证并入 Phase 1: 提取后立即统计 data-flow 连通文件 vs 不连通文件的 gold patch 覆盖率差异'\\n  rationale: Reviewer 指出 H2（特征区分度）在原 MVP 中无独立验证，Phase 2 失败时无法区分是 H2 还是 H3 问题。零成本 sanity\\n    check（统计连通/不连通文件的 gold patch 覆盖率）可在 Phase 1 提取完后立即执行，不需要训练。这比 Phase 2a 的线性分类器更早给出诊断信号。\\n  related_experiments: []\\n  depends_on:\\n  - D002\\n- id: D004\\n  date: 2026-05-12 11:21 UTC\\n  summary: 'Phase 1 gate PASS: timeout 0%, H2 Fisher p=1.54e-7, 75% instance recall.\\n    进入 Phase 2。'\\n  rationale: 10 repos 中 8 个成功提取（2 个 skip 因 buggy file 路径不存在，非 CodeQL 限制）。timeout rate\\n    0% 远低于 30% 阈值。H2 sanity check：连通文件 gold 覆盖 1.44% vs 不连通 0.00%，Fisher p=1.54e-7。75%\\n    instance recall（6/8 gold file 在连通集）。数据质量问题（路径匹配、skip rate、registry 注册）并行修复，不阻塞\\n    Phase 2。\\n  related_experiments: []\\n  depends_on: []\\n- id: D005\\n  date: 2026-05-12 11:35 UTC\\n  summary: 'CRITICAL: GPU 越界 PID 59170 跑在 GPU 5 而非分配的 cuda:4，立即 kill + 全脚本修复 CUDA_VISIBLE_DEVICES'\\n  rationale: Reviewer 核实 nvidia-smi 发现 run_mvp.py 在 GPU 5 上运行 9.3GB，而项目分配的 cuda:4\\n    完全空闲。违反 L1 红线（GPU 资源边界）。要求 Agent 立即 kill 进程、修复所有脚本强制 CUDA_VISIBLE_DEVICES=4、排查\\n    dry-run 是否也越界。\\n  related_experiments: []\\n  depends_on: []\\n- id: D006\\n  date: 2026-05-12 17:24 UTC\\n  summary: P2b pass criteria 调整：recall@5→recall@1，pool_size 26→50+，阈值 ≥2pp 不变\\n  rationale: Eval v2 (pool_size=26) 显示 random recall@5 已达 98.4-99.2%，原标准\\\"dataflow\\n    recall@5 > random ≥2pp\\\"数学上几乎不可能达标（天花板仅 0.8-1.6pp 空间）。recall@1 有更大区分度（random mean\\n    93.97%），且是更严格的排序指标。同时扩大 pool_size 至 50+ 使 recall@5/10 也获得有效梯度。新标准：dataflow_aware\\n    recall@1 > random recall@1 ≥2pp in ≥2/3 seeds，pool_size=50。\\n  related_experiments:\\n  - exp_id: mvp_p2b_contrastive_training\\n    role: trigger\\n    result: random recall@1 mean=0.940, emb_dist recall@1=0.669 at pool=26; recall@5\\n      ceiling\\n  depends_on:\\n  - D002\\n- id: D007\\n  date: 2026-05-12 19:52 UTC\\n  summary: MVP P2b dataflow 策略不可验证：connected⊆gold 导致数据相同。决定：50-repo 规模验证 + Scheme\\n    B 备份\\n  rationale: 修复 build_p2b_data.py 后重新生成数据，train_dataflow.jsonl 仍与 train_embedding.jsonl\\n    完全相同。根因：8 个 MVP repos 中 dataflow 连接文件全部是 gold 文件的子集（connected-but-not-gold = 0），non_pos\\n    过滤无差异。这不是方法缺陷而是规模问题——小 repo 紧耦合，2-hop 连接集≈gold 集。P1（Fisher p=1.54e-7）和 P2a（AUC=0.78）仍有效，说明\\n    dataflow connectivity 有信号，只是 MVP 规模不足以分离 connected-but-not-gold 子集。决策：(1) 立即跑\\n    50-repo 样本的 overlap 统计（CPU, ~2-4h），确认大规模下 connected⊃gold；(2) 并行准备 Scheme B（distance-weighted\\n    negatives）作为 pivot 备选；(3) overlap>20% 实例有 connected≠gold → 进入全量 M1 提取；overlap≈100%\\n    → pivot to Scheme B。\\n  related_experiments:\\n  - exp_id: mvp_p2b_contrastive_training\\n    role: trigger\\n    result: dataflow≡embedding 因 connected⊆gold\\n  depends_on:\\n  - D006\\n  - D004\\n- id: D008\\n  date: 2026-05-12 20:38 UTC\\n  summary: MVP 条件性通过：P1+P2a PASS，P2b dataflow 在 MVP 规模不可测但 50-repo 规模验证确认方法可行（Z=40.8%）。进入\\n    research 阶段。\\n  rationale: MVP 三阶段结果：P1 PASS（timeout 0%, Fisher p=1.54e-7, 75% instance recall）；P2a\\n    PASS（AUC 0.78, BM25 系数为负）；P2b 部分有效——random>>embedding（-27pp recall@1 at pool=26,\\n    -3.7pp at pool=50）确认 naive hard negatives 有害，但 dataflow vs random 因 connected⊆gold\\n    无法在 8 repos 上区分。50-repo 规模验证 Z=40.8%（中型 repo 55.7%），timeout 4%，确认方法在全量数据上可行。Kill\\n    criteria 均未触发。P2b dataflow 对比将在 M2 全量训练中完成。\\n  related_experiments:\\n  - exp_id: mvp_p1_codeql_feasibility\\n    role: evidence\\n    result: PASS\\n  - exp_id: mvp_p2a_linear_proxy\\n    role: evidence\\n    result: PASS\\n  - exp_id: mvp_p2b_contrastive_training\\n    role: evidence\\n    result: partial - random>>emb confirmed, dataflow untestable at MVP scale\\n  depends_on:\\n  - D007\\n  - D006\\n  - D004\\n- id: D009\\n  date: 2026-05-12 22:04 UTC\\n  summary: Dream 审稿完成：best=Weak Accept, median=Weak Reject, worst=Reject。批准 P0 启动，但\\n    plan 需增补 5 个 dream-derived 实验\\n  rationale: 三档共识问题：(1) 单编码器无法支撑 generality claim，需加 StarCoder/CodeBERT；(2) static\\n    vs dynamic embedding mining 是潜在 confound；(3) τ=0.05 可能 regime-specific；(4) SWE-bench\\n    +2pp 需 bootstrap CI；(5) abstract \\\"complementary\\\" 需降调。关键风险变量是 M1 的 Z%：≥35% best\\n    framing 成立，20-35% pivot 到 Claim 2 headline，<20% 需重大调整。已在 experiment_plan.yaml\\n    增加 plan_013-017（+35h GPU），paper_framing.md 增加 contingency framing。P0 实验（M1 已在跑）可继续，不需\\n    re-dream。\\n  related_experiments:\\n  - exp_id: dream_20260512T204322\\n    role: dream_simulate\\n    result: best=WA, median=WR, worst=R\\n  depends_on:\\n  - D008\\n- id: D010\\n  date: 2026-05-12 22:09 UTC\\n  summary: plan_013 (second encoder) 从 P1 升级至 P0，headline template 降调修复\\n  rationale: Reviewer 指出 single encoder 是 best→accept 的关键区分因素，在 best-R1-W1 和 median-R2-W5\\n    两档都出现。P1 排期可能导致论文缺少 generality 证据而被 WR。升级后 M2 完成即可并行启动 plan_013。同时修复 headline\\n    template \\\"cannot recover\\\" → \\\"complementary signal not captured by\\\"。\\n  related_experiments:\\n  - exp_id: plan_013\\n    role: priority_upgrade\\n    result: P1→P0\\n  depends_on:\\n  - D009\\n- id: D011\\n  date: 2026-05-13 01:38 UTC\\n  summary: Z%=74.0% 确认 Best Framing — Claim 1 为 headline，批准 M2 早期训练\\n  rationale: M1 部分数据（24/222 repos, 5128 instances）Z%=74.0%，远超 ≥35% 阈值。对比 D007 的 40.8%（50\\n    SWE-bench repos），SWE-Smith 数据集跨文件依赖密度更高。Best framing 成立：Claim 1 (\\\"structure-grounded\\n    negatives outperform\\\") 为 headline。批准在当前 5K instances 上做 M2 早期训练 pilot（3 strategies\\n    × 1 seed），利用 cuda:4 空闲期获取早期信号，不等全量 M1（还需 ~46h）。磁盘已清理至 61GB free (64%)，足够训练。\\n  related_experiments:\\n  - exp_id: m1_extraction\\n    role: data_source\\n    result: Z%=74.0% at 24/222 repos\\n  - exp_id: d007_50repo_overlap\\n    role: baseline\\n    result: Z%=40.8% on SWE-bench 50 repos\\n  depends_on:\\n  - D009\\n  - D010\\n- id: D012\\n  date: 2026-05-13 02:11 UTC\\n  summary: Kill m2_early_pilot_v3 (PID 897752) — 第二次 GPU 越界 (cuda:0)\\n  rationale: Reviewer 发现 m2_early_pilot_v3 在 cuda:0 运行（PID 897752, 17100 MiB），项目仅分配\\n    cuda:4。这是第二次 GPU 越界（第一次 D005 在 GPU 5）。立即 kill 并标记 killed。同时 m2_early_pilot_v2\\n    因 wandb API key error 已崩溃标记 FAILED。当前唯一合法训练为 PID 795791 (m2_early_pilot, cuda:4)。要求\\n    Agent 排查越界原因并确保后续脚本强制 CUDA_VISIBLE_DEVICES=4。\\n  related_experiments:\\n  - exp_id: m2_early_pilot_v3\\n    role: violated\\n    result: killed - GPU 越界 cuda:0\\n  - exp_id: m2_early_pilot_v2\\n    role: failed\\n    result: wandb API key error\\n  - exp_id: m2_early_pilot\\n    role: active\\n    result: PID 795791 on cuda:4, running\\n  depends_on:\\n  - D011\\n- id: D013\\n  date: 2026-05-13 02:50 UTC\\n  summary: 服务器迁移：cqa1-21977 cuda:4 → bjb1-42106 cuda:0/1 (RTX PRO 6000 96GB×2)\\n  rationale: Manager 分配独立服务器 bjb1-42106（2x RTX PRO 6000 96GB）。迁移策略：(1) M1 提取继续在 cqa1-21977\\n    CPU 上完成（不中断），(2) 新服务器立即搭建环境+同步代码+下载模型，(3) M2 early pilot 在 cqa1-21977 cuda:4 跑完后所有\\n    GPU 工作转到新服务器，(4) 通知 Manager 释放 cuda:4。RTX PRO 6000 96GB 彻底解决 M3a VRAM 问题（Qwen3.6-27B\\n    不再需要 fallback），2 卡可并行 M2 全量 + plan_013。\\n  related_experiments:\\n  - exp_id: m2_early_pilot\\n    role: in_progress\\n    result: finishing on cqa1-21977 cuda:4\\n  - exp_id: m1_extraction\\n    role: in_progress\\n    result: CPU only, stays on cqa1-21977\\n  depends_on:\\n  - D011\\n- id: D014\\n  date: 2026-05-13 04:44 UTC\\n  summary: Kill m2_early_pilot (PID 795791) — 过拟合+卡死，bjb1 m2_embed_verify 取代\\n  rationale: m2_early_pilot 在 cqa1 cuda:4 上仅完成 random 策略（best val_loss=0.5879 at step\\n    1500，之后持续过拟合到 0.728）。进程在 step 4000 卡死 45+ min。OOM 干扰（另一进程在同 GPU 启动）。embedding_distance\\n    和 dataflow_aware 策略未启动。bjb1 上的 m2_embed_verify 使用 true embedding mining + 更大参数（negatives=7,\\n    seq_len=2048, batch=8）+ eval bug fix，将完全取代此 pilot。通知 Manager 释放 cqa1 cuda:4。\\n  related_experiments:\\n  - exp_id: m2_early_pilot\\n    role: killed\\n    result: random best val_loss=0.5879, overfitting after step 1500\\n  - exp_id: m2_embed_verify\\n    role: replacement\\n    result: preparing on bjb1 cuda:1\\n  depends_on:\\n  - D011\\n  - D013\\n- id: D015\\n  date: 2026-05-13 11:43 UTC\\n  summary: 全量 Z%=78.0%（条件）确认 Best Framing；Coverage 34.3% 需论文讨论\\n  rationale: 全量 M1（123/131 repos, 44,173 instances）统计：15,153 instances 有结构数据（34.3%），其中\\n    11,825 有 connected-but-not-gold 文件（条件 Z%=78.0%，高于 pilot 72.5%）。条件 Z% 远超 35% 阈值，Best\\n    Framing（Claim 1 as headline）完全成立。但 Coverage 仅 34.3%——65.7% instances CodeQL/Beniget\\n    未产出结构连接，论文需讨论此局限性并限定 claim 范围为\\\"有结构数据的 instances\\\"。\\n  related_experiments:\\n  - exp_id: m1_extraction\\n    role: data_source\\n    result: 123/131 repos, 44173 instances, 15897 structural\\n  - exp_id: plan_006_scalability\\n    role: prior_pilot\\n    result: pilot Z%=72.5% on 29 repos\\n  depends_on:\\n  - D011\\n- id: D016\\n  date: 2026-05-13 15:24 UTC\\n  summary: 'Reviewer Critical: m2_embed_verify 和 plan_013_starcoder 实际已完成全部 3 策略，registry\\n    错误标记为 failed'\\n  rationale: Reviewer 直接从服务器日志验证：两个实验的 dataflow 策略均已完成（\\\"All 3 strategies completed\\\"），EXIT_CODE\\n    异常发生在训练完成之后（wrapper 脚本问题）。关键数据：(1) Qwen dataflow peak R@1=0.5584 (+2.27pp vs random)，支撑\\n    Claim 1；(2) StarCoder dataflow R@1=0.4869 < random 0.4922，encoder-agnostic claim\\n    受挑战；(3) 两个编码器的 dataflow 策略均严重过拟合（train loss→0）。已派 Agent 紧急修正 registry + 收集完整 metrics\\n    + 验证 StarCoder random 数据来源。方向决策待 Agent 汇报验证数据后确定。\\n  related_experiments:\\n  - exp_id: m2_embed_verify\\n    role: primary\\n    result: 实际完成（3 strategies all done），Qwen dataflow peak R@1=0.5584\\n  - exp_id: plan_013_starcoder\\n    role: primary\\n    result: 实际完成（3 strategies all done），StarCoder dataflow R@1=0.4869 < random 0.4922\\n  depends_on: []\\n- id: D017\\n  date: 2026-05-13 16:03 UTC\\n  summary: Pilot 结果验证完成：embedding > random 跨编码器一致；dataflow 需按两种 checkpoint 标准报告；Claim\\n    2 需修订\\n  rationale: 'Reviewer 验证 18 个指标全部精确匹配。核心发现：(1) embedding > random 在 Qwen (+2.0pp)\\n    和 StarCoder (+1.6pp) 上一致，是最稳健结论；(2) dataflow 排名取决于 checkpoint 选择——按 val_loss:\\n    embedding > dataflow > random (Qwen)，按 peak R@1: dataflow > embedding > random\\n    (Qwen)；(3) StarCoder dataflow final eval 追平 embedding (0.5078=0.5078)，\\\"embedding\\n    consistently beats dataflow\\\" 不成立；(4) Claim 2 (\\\"embedding harms\\\") 在 true embedding\\n    mining 下不复现，仅在 MVP BM25 proxy 下成立。全量 M2 训练需报告两种 checkpoint 标准下的结果，避免 cherry-picking\\n    质疑。Paper framing 修订延后至全量 M2 结果出来后。'\\n  related_experiments:\\n  - exp_id: m2_embed_verify\\n    role: primary\\n    result: 'Qwen: embedding(0.5557) > dataflow(0.5436) > random(0.5357) by val_loss;\\n      dataflow peak(0.5584) > embedding(0.5557) by R@1'\\n  - exp_id: plan_013_starcoder\\n    role: primary\\n    result: 'StarCoder: embedding(0.5078) > random(0.4922) > dataflow(0.4869) by val_loss;\\n      dataflow final(0.5078) = embedding'\\n  depends_on:\\n  - D016\\n- id: D018\\n  date: 2026-05-13 16:04 UTC\\n  summary: 不做预判性 framing pivot，full M2 (18 runs) 是 go/no-go 唯一判据；双 checkpoint 标准；准备\\n    B/C 两条后备路线\\n  rationale: Pilot 仅 24 repos / 1 seed，<2pp delta 统计功效不足以支持强 claim 或否决原假设。Full M2\\n    (131 repos × 3 strategies × 3 seeds × 2 encoders = 18 runs) 提供 3-seed 统计功效，是唯一可信判据。不选\\n    Agent 提议的 A/B/C 任何一个——过早锁定叙事会限制后续解读空间。数据构建已在进行，不浪费时间在 framing 讨论上。Full M2 结果出来后根据实际数据\\n    pattern 决定：(a) dataflow 跨编码器一致 > random → 原 framing 修正后可用；(b) dataflow 不一致但 embedding\\n    一致 → 方案 B 或 C；(c) 所有差异不显著 → 需要更大规模实验或 pivot。同时要求 dual checkpoint (best-val-loss\\n    + best-R@1) 和 3-seed CI 确保结果可信。\\n  related_experiments:\\n  - exp_id: m2_embed_verify\\n    role: evidence\\n    result: pilot underpowered (1 seed, 24 repos)\\n  - exp_id: plan_013_starcoder\\n    role: evidence\\n    result: pilot underpowered (1 seed, 24 repos)\\n  depends_on:\\n  - D017\\n- id: D019\\n  date: 2026-05-13 18:08 UTC\\n  summary: D018 补充：Full M2 go/no-go 量化阈值 + 统计检验方案\\n  rationale: 'Reviewer 指出 D018 缺量化阈值，go/no-go 判据需在结果出来前明确，避免事后 rationalization。\\n\\n\\n    **统计方法**：每个 encoder 3 seeds 的 R@1 (best-by-val-loss checkpoint) 做 paired difference，bootstrap\\n    95% CI + paired t-test (p<0.05)。同时报告 best-by-R@1 checkpoint 结果作为透明度补充。\\n\\n\\n    **Go/No-Go 阈值**：\\n\\n    (A) Go — 原 framing 可用：dataflow > random 的 95% CI 在两个 encoder 上均 > 0\\n\\n    (B) Conditional Go — 修正 framing：dataflow > random 在至少一个 encoder 上 CI > 0，另一个 CI\\n    含 0（差异不显著）\\n\\n    (C) No-Go for Claim 1：dataflow ≤ random 在两个 encoder 上 CI 均含 0 或为负 → Claim 1 失效，pivot\\n    到 \\\"mining strategy × architecture\\\" 分析论文\\n\\n\\n    **Claim 2 判据**：若 full M2 显示 embedding > random 且 CI > 0 → 原 Claim 2 (\\\"embedding\\n    harms\\\") 被否定。新 Claim 2 候选：\\\"true embedding mining helps, but BM25 proxy harms\\\" 或\\n    \\\"hard negative mining method matters more than hard negative source\\\"\\n\\n\\n    **跨 encoder 一致性规则**：\\n\\n    - 同方向同显著 → 强泛化 claim\\n\\n    - 同方向不同显著 → 条件 claim + architecture discussion\\n\\n    - 反方向 → Claim 1 原形式被拒，需 conditional reframe\\n\\n\\n    阈值在 full M2 结果出来前锁定，不允许事后修改。'\\n  related_experiments:\\n  - exp_id: m2_full_qwen\\n    role: primary\\n    result: RUNNING - random_s42 in progress\\n  - exp_id: m2_full_starcoder\\n    role: primary\\n    result: RUNNING - data build phase\\n  depends_on:\\n  - D018\\n- id: D020\\n  date: 2026-05-13 18:10 UTC\\n  summary: D019 补充：Claim 2 完整判定矩阵 + n=3 功效限制声明\\n  rationale: 'Reviewer 指出 D019 的 Claim 2 阈值不完整 + n=3 统计功效天然受限。补充如下：\\n\\n\\n    **Claim 2 完整判定矩阵**（3 seeds, paired bootstrap 95% CI）：\\n\\n    (i) random > embedding CI>0 → Claim 2 confirmed（embedding harms，与 MVP 一致）\\n\\n    (ii) embedding > random CI>0 → Claim 2 falsified（true embedding mining helps，需\\n    reframe）\\n\\n    (iii) CI 含 0 → inconclusive（效应存在但检测不到或确实无差异，论文报告为 \\\"no significant difference\\\"\\n    + 报告 effect size）\\n\\n\\n    **n=3 功效限制**（显式承认，不修改阈值）：\\n\\n    - df=2 时 t 临界值 4.303，pilot 级别差异（<2pp）极难达到 p<0.05\\n\\n    - Bootstrap n=3 仅 27 种重采样，CI 估计粗糙\\n\\n    - 阈值框架偏向 No-Go（Type II error 高）\\n\\n    - 若结果落入 (C) No-Go，论文 Discussion 必须讨论功效限制，不能简单声明 \\\"dataflow 无效\\\"\\n\\n    - 这是算力约束下的合理选择，不改阈值，但明确风险\\n\\n\\n    **plan_014 排期**：Full M2 完成后优先启动 plan_014（temperature ablation, ~10h）——无论 Claim\\n    2 reframe 成哪个方向，temperature regime-specificity 都需要回答。'\\n  related_experiments:\\n  - exp_id: m2_full_qwen\\n    role: primary\\n    result: RUNNING\\n  - exp_id: m2_full_starcoder\\n    role: primary\\n    result: RUNNING\\n  depends_on:\\n  - D019\\n- id: D021\\n  date: 2026-05-13 19:10 UTC\\n  summary: Negative difficulty 分析揭示 encoder capacity 差异是 dataflow 效果不一致的根因\\n  rationale: '预训练模型 cosine similarity 分析显示：Qwen pretrained embeddings 分辨力弱（random\\n    cosine sim 0.899），StarCoder 分辨力强（random cosine sim 0.553）。Dataflow negatives 在两个模型上都比\\n    random 更难（higher sim），说明方法设计正确。但 StarCoder 已经\\\"懂\\\"结构差异（所有策略 sim 都低），额外训练信号边际收益小。这解释了\\n    pilot 中 StarCoder dataflow < random 的现象：不是方法问题，是 encoder 已有足够 capacity。\\n\\n\\n    论文价值：(1) 从 negative result 中提取 mechanistic explanation；(2) 定义 method applicability\\n    condition：\\\"structure-grounded negatives benefit most when pretrained encoder has\\n    limited structural separability\\\"；(3) 产出论文级图表（Figure: Negative Difficulty Distributions）；(4)\\n    无论 full M2 落入 A/B/C，这个分析都增加论文深度。不修改 go/no-go 阈值，但丰富解读框架。'\\n  related_experiments:\\n  - exp_id: m2_embed_verify\\n    role: context\\n    result: 'Qwen: dataflow > random (+0.8~2.3pp)'\\n  - exp_id: plan_013_starcoder\\n    role: context\\n    result: 'StarCoder: dataflow < random (-0.5pp), explained by high pretrained separability'\\n  depends_on:\\n  - D018\\n  - D019\\n- id: D022\\n  date: 2026-05-13 19:25 UTC\\n  summary: M1 28K instances 可恢复（运行时故障非数据问题）；当前 M2 继续，并行后台重跑 M1 提取\\n  rationale: 'Fuzzy match 抽查 10/10 发现 buggy_file 全部存在——28,276 个 \\\"error\\\" 是 CodeQL 并行提取时的运行时故障（磁盘/存储瞬态），不是\\n    SWE-smith 数据质量问题。训练数据潜在从 15,897 → ~44,173（2.8x）。\\n\\n\\n    决策：不中断当前 M2 训练 + 并行后台重跑 M1 提取。理由：\\n\\n    (1) 当前 M2 已在双卡运行，中断重来延期 3-7 天超出 DDL\\n\\n    (2) M1 重提取是 CPU 工作，可在 bjb1-42106 后台运行不影响 GPU 训练\\n\\n    (3) 如果当前 M2 结果落入 (C) No-Go 或 effect size 太小，扩展数据集是 natural next step\\n\\n    (4) 2.8x 数据量可能显著缓解 dataflow 过拟合问题（D021 中的核心风险）\\n\\n\\n    Claim 3 叙事需修正：\\\"64% failure 是上游数据问题\\\" → \\\"64% 是运行时提取故障，CodeQL 本身在有效输入上 100% 成功，可通过重跑恢复\\\"。这是\\n    engineering limitation with clear fix，不是方法局限。'\\n  related_experiments:\\n  - exp_id: m1_extraction\\n    role: primary\\n    result: 28,276 instances recoverable - runtime failure, not data quality\\n  - exp_id: plan_006_scalability\\n    role: affected\\n    result: 'error classification needs correction: buggy_file_not_found was misattributed'\\n  depends_on:\\n  - D018\\n  - D019\\n- id: D023\\n  date: 2026-05-13 19:43 UTC\\n  summary: Kill M1 重提取：bjb1 CodeQL 查询 100% 失败，D022 前提不成立需诊断后重新评估\\n  rationale: Reviewer CRITICAL 发现 bjb1-42106 上 CodeQL call_graph.ql 查询全部 exit status\\n    2，317/325 行失败，零有效结构数据产出。原 M1 在 cqa1-21977 成功，迁移后 CodeQL 版本/QL pack 可能不兼容。立即 kill\\n    进程释放 CPU/RAM，诊断 CodeQL 配置后决定修复或换服务器。\\n  related_experiments:\\n  - exp_id: m1_reextract\\n    role: subject\\n    result: killed - CodeQL incompatible on bjb1\\n  depends_on:\\n  - D022\\n- id: D024\\n  date: 2026-05-14 00:49 UTC\\n  summary: 'Major paper framing rewrite: drop falsified \\\"embedding harms\\\" claim, pivot\\n    to \\\"systematic analysis + mechanistic insight\\\" narrative'\\n  rationale: 'Reviewer deep assessment confirmed Claim 2 (\\\"embedding actively harms\\\",\\n    -27pp) was built on BM25-proxy mislabeled as embedding-distance in MVP. D017 proved\\n    true embedding mining helps (+1.6-2.0pp). New framing: (1) embedding universally\\n    helps (corrects misconception), (2) dataflow conditionally helps (mediated by\\n    representation saturation), (3) CodeQL scalable. This is a stronger, more honest\\n    paper type for EMNLP — empirical analysis with mechanistic depth rather than false\\n    \\\"our method beats all\\\" claim.'\\n  related_experiments:\\n  - exp_id: m2_embed_verify\\n    role: evidence\\n    result: embedding > random confirmed for both encoders\\n  - exp_id: plan_013_starcoder\\n    role: evidence\\n    result: dataflow helps Qwen only, not StarCoder — conditional benefit\\n  - exp_id: neg_difficulty_analysis\\n    role: evidence\\n    result: pos_sim saturation explains strategy-encoder interaction\\n  depends_on: []\\n- id: D025\\n  date: 2026-05-14 01:01 UTC\\n  summary: Plan_014 temperature ablation 缩减为 2 strategies × 3τ × 2 epochs = 6 runs\\n    (~70h)，deadline 可达\\n  rationale: 原方案 9 runs × 3 epochs = 157h GPU，超出 May 25 ARR 截稿。缩减理由：(1) 回答 Dream reviewer\\n    的 regime-specificity concern 只需证明 embedding vs random 的相对优势跨 τ 一致，不需要 3 策略全跑；(2)\\n    M2 和 pilot 均显示 epoch 3 过拟合无收益，2 epochs 足够；(3) τ=0.07 已由 M2 覆盖，只需 {0.05, 0.1, 0.2}。6\\n    runs × ~11.7h = ~70h → 双卡并行 35h wall time，M2 完成后 ~1.5 天可跑完。Dataflow strategy 的\\n    τ ablation 降为 P2，时间充裕再补。\\n  related_experiments:\\n  - exp_id: m2_full_qwen\\n    role: evidence\\n    result: step 1000 best, epoch 3 overfitting → 2 epochs sufficient\\n  - exp_id: plan_014\\n    role: target\\n    result: budget revised from 10h to 70h, scope from 9 to 6 runs\\n  depends_on:\\n  - D024\\n- id: D026\\n  date: 2026-05-14 02:56 UTC\\n  summary: Qwen eval@2000 确认过拟合，后续 M2 runs 从 3 epochs 减至 2 epochs\\n  rationale: 'eval@2000: val_loss=0.5162, R@1=0.5228（与 @1500 持平，未恢复）。Best 锁定 step\\n    1000 (epoch 1 中段)。train_loss=0.04 vs val_loss=0.52，gap 持续扩大。模式与 pilot 一致（best\\n    at ~25% training）。当前 s42 保留 3 epochs 完整跑完（提供 full overfitting curve 数据），后续 8 runs/encoder\\n    设 max_epochs=2。节省 ~48h/GPU，M2 完成时间从 ~May 20-21 提前到 ~May 18-19。'\\n  related_experiments:\\n  - exp_id: m2_full_qwen\\n    role: evidence\\n    result: eval@2000 R@1=0.5228 flat, overfitting confirmed\\n  - exp_id: m2_full_starcoder\\n    role: pending\\n    result: eval@1000 still improving, apply 2-epoch precaution for subsequent seeds\\n  depends_on:\\n  - D025\\n- id: D027\\n  date: 2026-05-14 08:13 UTC\\n  summary: M2 剩余 runs 加 early stopping (patience=2 evals)，加速关键路径\\n  rationale: Reviewer 计算 M2 全 18 runs 需 ~5.5 天（StarCoder 瓶颈 ~133h）。两个编码器 best checkpoint\\n    均在 step 1000，之后 val_loss 持续上升。加 early stopping（patience=2，即连续 2 次 eval@500 无改善即停）预计在\\n    step 2000 左右停止（vs 2828 full 2-epoch），节省 ~30% 时间（~1.5 天），M2 从 May 19.5 提前到 ~May\\n    18。关键路径 May 25 ARR 余量从 5 天增至 7 天。风险低：仅影响未启动的 runs，不改已跑数据。\\n  related_experiments:\\n  - exp_id: m2_full_qwen\\n    role: target\\n    result: running, best@1000, overfitting confirmed\\n  - exp_id: m2_full_starcoder\\n    role: target\\n    result: running, best@1000, overfitting confirmed\\n  depends_on:\\n  - D026\\n- id: D028\\n  date: 2026-05-14 11:09 UTC\\n  summary: Claim 2 降级待定：M2 full 结果决定 \\\"conditional benefit\\\" 是独立 claim 还是降为 observation\\n  rationale: Reviewer 覆盖率审查指出 Claim 2 最薄弱：n=2 encoders 交互效应无统计功效，neg_difficulty 是描述性非实验性证据。建议降为\\n    \\\"observation + mechanistic hypothesis\\\"。决策延迟到 M2 full 18 runs 完成后：若 Qwen dataflow>random\\n    p<0.05 则保持 conditional claim；否则降级为 observation。\\n  related_experiments:\\n  - exp_id: m2_embed_verify\\n    role: Qwen pilot positive\\n    result: dataflow > random +0.8pp val_loss\\n  - exp_id: plan_013_starcoder\\n    role: StarCoder pilot negative\\n    result: dataflow < random -0.5pp\\n  - exp_id: m2_full_qwen\\n    role: go/no-go for claim strength\\n    result: RUNNING\\n  - exp_id: m2_full_starcoder\\n    role: encoder generality test\\n    result: RUNNING\\n  depends_on:\\n  - D018\\n  - D019\\n- id: D029\\n  date: 2026-05-14 16:23 UTC\\n  summary: Dream full review 完成：7 条三档一致结构性问题确认，BM25 baseline 升为 P0，pool size sensitivity\\n    新增 plan_019\\n  rationale: 'dream_20260514T075732 (full review mode) 三档评分: Best 4/6 WA, Median 3/6\\n    WR, Worst 3/6 WR。跨三档一致的结构性问题 7 条：(1) 缺 BM25 baseline 是 #1 共识——论文核心叙事（纠正 CoCoHaNeRe）无实证支撑，已加\\n    plan_018 P0；(2) N=2 编码器限制——保持 honest framing，无法加更多编码器；(3) StarCoder 误标为 encoder-decoder——已修正为\\n    decoder-only；(4) RepoBench-R 无 CIs——plan_004 已标注多 seed 要求；(5) Pool=50 太小——新增 plan_019\\n    P1；(6) 34% structural coverage 未分层——plan_005 已扩展；(7) Checkpoint selection criterion\\n    未指定——写作时明确。观察项：effect sizes 太小（等 M2 真实数据）、overfitting 分析（提取现有训练 log）。忽略项：broken\\n    bibliography（dream artifact）、0 figures（dream artifact）。评分顺序正常（best≥median=worst）。下一步：派\\n    Agent 准备 BM25 mining（CPU），M2 完成后立即执行 plan_018 training phase。'\\n  related_experiments:\\n  - exp_id: plan_018\\n    role: new P0 experiment added\\n    result: planned\\n  - exp_id: plan_019\\n    role: new P1 experiment added\\n    result: planned\\n  - exp_id: plan_004\\n    role: updated with multi-seed CI requirement\\n    result: planned\\n  - exp_id: plan_005\\n    role: extended with structural coverage stratification\\n    result: planned\\n  depends_on:\\n  - D024\\n  - D028\\n- id: D030\\n  date: 2026-05-14 16:23 UTC\\n  summary: Dream dream_20260514T075732 分析完成：7 项确认行动 + 5 项观察项 + re-dream 后批准新 P0\\n  rationale: 'Dream full review (2 Reviewers roundtable) 三档评分: Best=4/6(WA), Median=3/6(WR),\\n    Worst=3/6(WR)。Median 未达 borderline，需修复结构性问题后 re-dream。\\n\\n\\n    **三档一致的结构性问题（7 项确认行动）：**\\n\\n    1. [EXP] 缺 BM25 negative baseline — 论文核心 narrative (correcting CoCoHaNeRe) 无实证。加\\n    plan_018, P0, Phase1 CPU 立即启动\\n\\n    2. [EXP] RepoBench-R 缺 CIs — plan_004 增加多 seed 评估\\n\\n    3. [EXP] Pool size 50 过小 — 加 plan_019 sensitivity analysis\\n\\n    4. [EXP] 34% structural coverage 未分层 — 扩展 plan_005 加 structural-available vs fallback\\n    stratum + neg_difficulty quartile\\n\\n    5. [FRAMING] N=2 encoders → 降级为 \\\"observation + hypothesis\\\"，非 validated mechanism\\n\\n    6. [FRAMING] StarCoder 架构 → 修正为 \\\"decoder-only\\\"（已改）\\n\\n    7. [FRAMING] Claim 3 (CodeQL pipeline) → 降为 supporting methodology（已改）\\n\\n\\n    **观察项（等真实数据）：**\\n\\n    1. Effect sizes marginal [M][W] — 等 M2 full 统计结果\\n\\n    2. Dataflow claim strength [M][W] — D028 已 plan\\n\\n    3. \\\"Scaling law\\\" [W] → 用 \\\"trend\\\" + CIs\\n\\n    4. Temperature ablation contradiction [W] — plan_014 结果决定\\n\\n    5. Zero method contribution [M][W] — framing 强度决定\\n\\n\\n    **Re-dream 要求：** framing + plan 修改完成后需 re-dream，best ≥ WA 且 median ≥ borderline\\n    后才批准新 P0 实验。已在跑的实验继续。'\\n  related_experiments:\\n  - exp_id: dream_20260514T075732\\n    role: trigger\\n    result: best=4/6 WA, median=3/6 WR, worst=3/6 WR\\n  - exp_id: plan_018\\n    role: new_from_dream\\n    result: planned — BM25 baseline\\n  - exp_id: plan_019\\n    role: new_from_dream\\n    result: planned — pool size sensitivity\\n  depends_on:\\n  - D028\\n  - D024\\n- id: D031\\n  date: 2026-05-14 17:02 UTC\\n  summary: 'BM25 Phase 1 完成: 87% overlap with embedding_distance，预示论文叙事可能从 \\\"纠正误标\\\"\\n    转向 \\\"受控对比证明 hard negatives 普遍有效\\\"'\\n  rationale: 'plan_018 Phase 1 (CPU) 完成。3 seeds BM25 negatives 已生成，与 embedding_distance\\n    negatives 重叠率高达 87.1%。小 repo 候选池 ≤50 导致所有策略完全重合，BM25 differentiation 主要在大 repo\\n    上体现。\\n\\n\\n    Phase 2 训练结果预期 3 种可能：\\n\\n    A) BM25 harm (BM25 << random) → 原叙事成立（\\\"BM25 proxy 导致 CoCoHaNeRe 错误结论\\\"）\\n\\n    B) BM25 ≈ random → contingency per D030（叙事降为 \\\"systematic comparison\\\"）\\n\\n    C) BM25 ≈ embedding_distance (87% overlap 强烈预示) → 叙事升级为\\\"BM25 和 embedding mining\\n    高度重叠，两者在受控环境下都优于 random；CoCoHaNeRe 的负面结论源于实验控制不足而非 BM25-proxy 本身\\\"\\n\\n\\n    Scenario C 实际上比 A 更强——我们提供的不只是标签纠正，而是受控对比 + 叙事升级。\\n\\n\\n    附带决策：plan_015 暂缓至 camera-ready（44h 超预算 + DDL 紧），Limitations 中承认 static vs dynamic\\n    confound。'\\n  related_experiments:\\n  - exp_id: plan_018\\n    role: phase1_complete\\n    result: BM25 data ready, 87% overlap with embedding_distance\\n  - exp_id: plan_015\\n    role: deferred\\n    result: design complete, execution deferred to camera-ready\\n  depends_on:\\n  - D030\\n- id: D032\\n  date: 2026-05-14 17:02 UTC\\n  summary: plan_015 缩减为 1 seed × dynamic_ep (~11h)；BM25 overlap 87% 需分层验证\\n  rationale: 'plan_015 原设计 3 variants × 多 seeds = 44h，DDL May 25 前 GPU 时间不够。缩减为 dynamic_ep\\n    × 1 seed (Qwen s42) ~11h，足以排除 static vs dynamic confound。预期 dynamic ≈ static（<1pp），在\\n    Limitation 段写实验证据。\\n\\n\\n    BM25 Phase 1 完成：BM25 vs embedding overlap 87.1%。但 Agent 指出小 repo (pool ≤50) 导致所有策略\\n    negatives 重合——overlap 被拉高。已派补充分析按 repo 大小分层统计真实差异化程度。Phase 2 训练结果将决定 CoCoHaNeRe\\n    narrative 是否需要 pivot（contingency 已在 paper_framing.md）。'\\n  related_experiments:\\n  - exp_id: plan_015\\n    role: scope_reduction\\n    result: 44h→11h, 1 seed × dynamic_ep only\\n  - exp_id: plan_018\\n    role: phase1_complete\\n    result: BM25 vs embedding overlap 87.1%, 3 seeds done\\n  depends_on:\\n  - D030\\n- id: D033\\n  date: 2026-05-14 17:10 UTC\\n  summary: D031 修正：BM25 top-7 overlap 远低于 k=50 的 87%，大 repo 仅 30%，Phase 2 将有区分度\\n  rationale: '分层 Jaccard 分析（top-7, seed 42, 2920 matched queries）显示 BM25 vs embedding_distance\\n    重叠率：small=67%, medium=38%, large=30%。之前报告的 87% 是 k=50 全候选重叠，训练实际用 top-7 negatives\\n    差异大得多。\\n\\n\\n    关键修正：D031 中预判的 \\\"BM25 ≈ embedding_distance\\\" 不再成立。Phase 2 训练预期结果重新开放为三种可能（BM25 harm\\n    / neutral / help），实验区分度足够。\\n\\n\\n    方法论 flag: BM25 使用 whitespace tokenization (str.split())，不处理 camelCase/snake_case。如果\\n    BM25 表现差，tokenization 可能是 confound。论文中需标注。Reviewer 已指出。\\n\\n\\n    24% match rate 源于 BM25 mining 使用了不同 train/val split，不影响分层趋势结论但如需严格配对可重新生成。'\\n  related_experiments:\\n  - exp_id: plan_018\\n    role: phase1_analysis\\n    result: 'stratified overlap: large_repo BM25-vs-embedding=30%, BM25-vs-random=0.7%'\\n  depends_on:\\n  - D031\\n- id: D034\\n  date: 2026-05-14 17:50 UTC\\n  summary: Re-dream gate 未通过但决定继续：median=WR 由不可修复因素驱动（novelty/effect-size/n=2），override\\n    gate 推进 Phase 2\\n  rationale: 'Re-dream dream_20260514T162530 评分：Best=4/6(WA), Median=3/6(WR), Worst=3/6(WR)。与首次\\n    dream 完全一致，修复 BM25 baseline + pool size + framing 降级未改变评分。\\n\\n\\n    Gate 要求 median ≥ borderline。分析 median WR 原因：\\n\\n    1. Novelty (\\\"ANCE for code\\\") — 不可修复，是 framing 层面问题\\n\\n    2. Effect sizes (pool=200: +0.4~0.7pp) — 数据决定，不可修复\\n\\n    3. N=2 encoders — DDL 前不可加\\n\\n    4. Dataflow null — 数据已确定\\n\\n    5. Bibliography (2 citations) — dream artifact，实际论文可修\\n\\n\\n    因素 1-4 是 dream 模拟的固有限制（无论怎么改 plan，dream 想象的 median/worst 数据都会是 marginal），而非实验设计缺陷。Best\\n    case 达到 WA=4/6 并且 R1 明确给出 \\\"specify K + checkpoint criterion → 5/6\\\" 路径。\\n\\n\\n    决策：Override gate，允许 Phase 2 在 GPU 空闲时执行。理由：\\n\\n    (a) 阻塞因素为写作/scope 层面，非实验层面，更多 dream 不会改变\\n\\n    (b) Best case BM25 baseline 被评为 \\\"paper''s most clean-cut contribution\\\"\\n\\n    (c) ARR May 25 DDL 时间紧，Phase 2 是关键路径\\n\\n    (d) Writing 层面的修复（related work, specification）会在实际论文中自然解决'\\n  related_experiments:\\n  - exp_id: dream_20260514T162530\\n    role: re-dream\\n    result: best=4/6 WA, median=3/6 WR, worst=3/6 WR — unchanged from first dream\\n  - exp_id: plan_018\\n    role: gate_override\\n    result: Phase 2 approved despite gate not passing\\n  depends_on:\\n  - D030\\n  - D031\\n  - D033\\n- id: D035\\n  date: 2026-05-14 18:48 UTC\\n  summary: Claim 2 降级：从 \\\"conditional benefit beyond embedding mining\\\" 降为 \\\"exploratory\\n    observation\\\"\\n  rationale: Reviewer 覆盖率审查发现 pilot 数据不支持 \\\"beyond embedding mining\\\"——两个编码器都是 dataflow\\n    < embedding (Qwen -1.2pp, StarCoder -1.0pp)。0/3 支撑实验完成。降级为观察+机制假说，不再作为核心贡献。paper_framing.md\\n    已更新。\\n  related_experiments:\\n  - exp_id: m2_embed_verify\\n    role: evidence\\n    result: embedding > dataflow on both encoders\\n  - exp_id: plan_013_starcoder\\n    role: evidence\\n    result: 'StarCoder: embedding 0.5174 > dataflow 0.5078'\\n  depends_on:\\n  - D028\\n- id: D036\\n  date: 2026-05-14 19:10 UTC\\n  summary: M2 checkpoint 选择统一用 R@1 而非 val_loss 作为 primary criterion\\n  rationale: Reviewer 核实 s43 发现 val_loss 最优在 step 500、R@1 最优在 step 1500，两个 criterion\\n    给出不同最优点。检索任务的目标指标是 R@1，val_loss 仅反映语言建模质量，不直接对应下游检索性能。统一用 R@1 选 checkpoint 确保论文报告一致性，后续所有\\n    M2 实验沿用此标准。\\n  related_experiments:\\n  - exp_id: m2_full_qwen_continued\\n    role: 触发\\n    result: s43 val_loss best@500 vs R@1 best@1500\\n  - exp_id: m2_full_starcoder_resumed\\n    role: 同步适用\\n    result: 进行中\\n  depends_on: []\\n- id: D037\\n  date: 2026-05-14 19:13 UTC\\n  summary: 'D037: M2 checkpoint 改为只存 LoRA adapter weights，不存 merged 完整模型'\\n  rationale: 磁盘剩余 43GB，后续 18 runs 需 ~249GB checkpoint 空间。根因：LoRA rank=16 的 3B 模型存完整\\n    float16 merged weights (5.8GB/checkpoint)，但 adapter 仅 ~100MB。改为 PeftModel.save_pretrained\\n    只存 adapter，18 runs × 2 checkpoints × 100MB ≈ 3.6GB，彻底解决。同时删旧 pilot 输出 (+66GB)\\n    和 final 目录 (+11.6GB) 作为即时缓解。与 mvp_p2b_contrastive_training 磁盘满崩溃为同一 failure pattern。\\n  related_experiments:\\n  - exp_id: m2_full_qwen_continued\\n    role: 受影响\\n    result: 剩余 7 runs 将受益于 adapter-only saving\\n  - exp_id: m2_full_starcoder_resumed\\n    role: 受影响\\n    result: 剩余 7 runs 同样受益\\n  depends_on: []\\n- id: D038\\n  date: 2026-05-14 20:39 UTC\\n  summary: Plan 005 分层分析需额外控制 pool_size；dataflow richness 维度不单独做 claim\\n  rationale: Confound 分析显示 rich-dataflow 实例的候选池远大于 moderate（46-50 vs 17-37），pool_size\\n    机械性驱动 R@1 差异。控制 repo_size 后模式不消失，确认 pool_size 才是真正 confound。论文中 dataflow richness\\n    维度需 pool_size-matched 对比后才能下结论。\\n  related_experiments:\\n  - exp_id: plan_005_stratified\\n    role: evidence\\n    result: dry-run 确认 confound 存在\\n  depends_on: []\\n- id: D039\\n  date: 2026-05-14 20:40 UTC\\n  summary: 分层分析 R@1 数据无效：dry-run mock predictions，非真实模型结果。confound 分布结构(repo_size×dataflow)有效保留。\\n  rationale: Reviewer critical 审查确认：stratified_dryrun v1/v2 和 confound_analysis 的所有\\n    R@1 值均来自 dry-run mock predictions。策略排序模式和优势幅度需用 M2 真实 checkpoint 重新验证。仅 cross-tabulation\\n    分布结构（rich dataflow 99.3% 集中在 large/xlarge repos, Spearman ρ=0.077）为真实数据，可用于论文写作中声明\\n    confound 关系。plan_005_stratified 必须等 M2 真实 checkpoint 完成后执行。\\n  related_experiments:\\n  - exp_id: worker_analysis_dataflow_reposize_confound\\n    role: invalidated_analysis\\n    result: R@1 from mock data, distribution structure valid\\n  - exp_id: m2_full_qwen_continued\\n    role: dependency\\n    result: running - provides real checkpoints\\n  - exp_id: m2_full_starcoder_resumed\\n    role: dependency\\n    result: running - provides real checkpoints\\n  depends_on: []\\n- id: D040\\n  date: 2026-05-14 21:27 UTC\\n  summary: Claim 1 framing 微调：从\\\"纠正 embedding negatives 不行的误解\\\"改为\\\"挑战必须用昂贵 gradient-based\\n    方法的假设\\\"\\n  rationale: CoCoHaNeRe (ACM TOSEM 2025) 实际论点是 non-differentiable embedding negatives\\n    \\\"slow and ineffective\\\"（相对 gradient-based），并非说 embedding negatives 有害。原 Claim 1\\n    \\\"correcting misconception\\\" 措辞会被审稿人以 CoCoHaNeRe 原文反驳。新措辞\\\"simple static embedding-distance\\n    mining suffices, challenging the assumption that expensive gradient-based hard\\n    negative methods are necessary\\\"更准确、更defensible，且保留 contribution。\\n  related_experiments:\\n  - exp_id: plan_017_literature\\n    role: evidence\\n    result: CoCoHaNeRe framing conflict identified during related work expansion\\n  depends_on: []\\n\", \"total_chars\": 31588, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4bb89274-0b46-465b-b6f6-aaa3090d327b",
  "isSidechain": false,
  "promptId": "82620338-1cd7-4c43-9283-e5cb821c1607",
  "type": "user",
  "uuid": "8997cc8c-ffda-4da9-b65c-0208d69154a5",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"path\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/decisions.yaml\\\", \\\"content\\\": \\\"_next_id: 41\\\\ndecisions:\\\\n- id: D001\\\\n  date: 2026-05-12 09:57 UTC\\\\n  summary: 'MVP 设计: CodeQL 试点(10 repos) + 迷你对比训练(500 instances) 验证核心假设'\\\\n  rationale: 13 天 DDL，需要最快速验证核心假设链：(1) CodeQL inter-procedural data-flow 在 Python\\\\n    repos 上可行（timeout < 30%），(2) data-flow hard negatives 比 random negatives 提升检索\\\\n    recall。两个 phase 串行，总计约 1 天。通过后立即进入全量数据提取和训练。\\\\n  related_experiments: []\\\\n  depends_on: []\\\\n- id: D002\\\\n  date: 2026-05-12 10:01 UTC\\\\n  summary: '采纳 Reviewer 反馈: MVP Phase 2 增加线性分类器 proxy 验证 + 3-seed 训练 + 显式 kill criteria'\\\\n  rationale: 'Reviewer 指出 Phase 2 原方案（500 instances, ~100 held-out, 2pp gate）统计效力不足，2pp\\\\n    差异在随机噪声范围内。增加: (1) Phase 2a 线性分类器 proxy 验证解耦特征质量与训练策略；(2) 3-seed 训练要求 ≥2/3 seed\\\\n    提升；(3) 每个 phase 的 fail→kill/fallback 路径。防止 13 天 DDL 下的沉没成本陷阱。'\\\\n  related_experiments: []\\\\n  depends_on:\\\\n  - D001\\\\n- id: D003\\\\n  date: 2026-05-12 10:02 UTC\\\\n  summary: 'H2 验证并入 Phase 1: 提取后立即统计 data-flow 连通文件 vs 不连通文件的 gold patch 覆盖率差异'\\\\n  rationale: Reviewer 指出 H2（特征区分度）在原 MVP 中无独立验证，Phase 2 失败时无法区分是 H2 还是 H3 问题。零成本 sanity\\\\n    check（统计连通/不连通文件的 gold patch 覆盖率）可在 Phase 1 提取完后立即执行，不需要训练。这比 Phase 2a 的线性分类器更早给出诊断信号。\\\\n  related_experiments: []\\\\n  depends_on:\\\\n  - D002\\\\n- id: D004\\\\n  date: 2026-05-12 11:21 UTC\\\\n  summary: 'Phase 1 gate PASS: timeout 0%, H2 Fisher p=1.54e-7, 75% instance recall.\\\\n    进入 Phase 2。'\\\\n  rationale: 10 repos 中 8 个成功提取（2 个 skip 因 buggy file 路径不存在，非 CodeQL 限制）。timeout rate\\\\n    0% 远低于 30% 阈值。H2 sanity check：连通文件 gold 覆盖 1.44% vs 不连通 0.00%，Fisher p=1.54e-7。75%\\\\n    instance recall（6/8 gold file 在连通集）。数据质量问题（路径匹配、skip rate、registry 注册）并行修复，不阻塞\\\\n    Phase 2。\\\\n  related_experiments: []\\\\n  depends_on: []\\\\n- id: D005\\\\n  date: 2026-05-12 11:35 UTC\\\\n  summary: 'CRITICAL: GPU 越界 PID 59170 跑在 GPU 5 而非分配的 cuda:4，立即 kill + 全脚本修复 CUDA_VISIBLE_DEVICES'\\\\n  rationale: Reviewer 核实 nvidia-smi 发现 run_mvp.py 在 GPU 5 上运行 9.3GB，而项目分配的 cuda:4\\\\n    完全空闲。违反 L1 红线（GPU 资源边界）。要求 Agent 立即 kill 进程、修复所有脚本强制 CUDA_VISIBLE_DEVICES=4、排查\\\\n    dry-run 是否也越界。\\\\n  related_experiments: []\\\\n  depends_on: []\\\\n- id: D006\\\\n  date: 2026-05-12 17:24 UTC\\\\n  summary: P2b pass criteria 调整：recall@5→recall@1，pool_size 26→50+，阈值 ≥2pp 不变\\\\n  rationale: Eval v2 (pool_size=26) 显示 random recall@5 已达 98.4-99.2%，原标准\\\\\\\"dataflow\\\\n    recall@5 > random ≥2pp\\\\\\\"数学上几乎不可能达标（天花板仅 0.8-1.6pp 空间）。recall@1 有更大区分度（random mean\\\\n    93.97%），且是更严格的排序指标。同时扩大 pool_size 至 50+ 使 recall@5/10 也获得有效梯度。新标准：dataflow_aware\\\\n    recall@1 > random recall@1 ≥2pp in ≥2/3 seeds，pool_size=50。\\\\n  related_experiments:\\\\n  - exp_id: mvp_p2b_contrastive_training\\\\n    role: trigger\\\\n    result: random recall@1 mean=0.940, emb_dist recall@1=0.669 at pool=26; recall@5\\\\n      ceiling\\\\n  depends_on:\\\\n  - D002\\\\n- id: D007\\\\n  date: 2026-05-12 19:52 UTC\\\\n  summary: MVP P2b dataflow 策略不可验证：connected⊆gold 导致数据相同。决定：50-repo 规模验证 + Scheme\\\\n    B 备份\\\\n  rationale: 修复 build_p2b_data.py 后重新生成数据，train_dataflow.jsonl 仍与 train_embedding.jsonl\\\\n    完全相同。根因：8 个 MVP repos 中 dataflow 连接文件全部是 gold 文件的子集（connected-but-not-gold = 0），non_pos\\\\n    过滤无差异。这不是方法缺陷而是规模问题——小 repo 紧耦合，2-hop 连接集≈gold 集。P1（Fisher p=1.54e-7）和 P2a（AUC=0.78）仍有效，说明\\\\n    dataflow connectivity 有信号，只是 MVP 规模不足以分离 connected-but-not-gold 子集。决策：(1) 立即跑\\\\n    50-repo 样本的 overlap 统计（CPU, ~2-4h），确认大规模下 connected⊃gold；(2) 并行准备 Scheme B（distance-weighted\\\\n    negatives）作为 pivot 备选；(3) overlap>20% 实例有 connected≠gold → 进入全量 M1 提取；overlap≈100%\\\\n    → pivot to Scheme B。\\\\n  related_experiments:\\\\n  - exp_id: mvp_p2b_contrastive_training\\\\n    role: trigger\\\\n    result: dataflow≡embedding 因 connected⊆gold\\\\n  depends_on:\\\\n  - D006\\\\n  - D004\\\\n- id: D008\\\\n  date: 2026-05-12 20:38 UTC\\\\n  summary: MVP 条件性通过：P1+P2a PASS，P2b dataflow 在 MVP 规模不可测但 50-repo 规模验证确认方法可行（Z=40.8%）。进入\\\\n    research 阶段。\\\\n  rationale: MVP 三阶段结果：P1 PASS（timeout 0%, Fisher p=1.54e-7, 75% instance recall）；P2a\\\\n    PASS（AUC 0.78, BM25 系数为负）；P2b 部分有效——random>>embedding（-27pp recall@1 at pool=26,\\\\n    -3.7pp at pool=50）确认 naive hard negatives 有害，但 dataflow vs random 因 connected⊆gold\\\\n    无法在 8 repos 上区分。50-repo 规模验证 Z=40.8%（中型 repo 55.7%），timeout 4%，确认方法在全量数据上可行。Kill\\\\n    criteria 均未触发。P2b dataflow 对比将在 M2 全量训练中完成。\\\\n  related_experiments:\\\\n  - exp_id: mvp_p1_codeql_feasibility\\\\n    role: evidence\\\\n    result: PASS\\\\n  - exp_id: mvp_p2a_linear_proxy\\\\n    role: evidence\\\\n    result: PASS\\\\n  - exp_id: mvp_p2b_contrastive_training\\\\n    role: evidence\\\\n    result: partial - random>>emb confirmed, dataflow untestable at MVP scale\\\\n  depends_on:\\\\n  - D007\\\\n  - D006\\\\n  - D004\\\\n- id: D009\\\\n  date: 2026-05-12 22:04 UTC\\\\n  summary: Dream 审稿完成：best=Weak Accept, median=Weak Reject, worst=Reject。批准 P0 启动，但\\\\n    plan 需增补 5 个 dream-derived 实验\\\\n  rationale: 三档共识问题：(1) 单编码器无法支撑 generality claim，需加 StarCoder/CodeBERT；(2) static\\\\n    vs dynamic embedding mining 是潜在 confound；(3) τ=0.05 可能 regime-specific；(4) SWE-bench\\\\n    +2pp 需 bootstrap CI；(5) abstract \\\\\\\"complementary\\\\\\\" 需降调。关键风险变量是 M1 的 Z%：≥35% best\\\\n    framing 成立，20-35% pivot 到 Claim 2 headline，<20% 需重大调整。已在 experiment_plan.yaml\\\\n    增加 plan_013-017（+35h GPU），paper_framing.md 增加 contingency framing。P0 实验（M1 已在跑）可继续，不需\\\\n    re-dream。\\\\n  related_experiments:\\\\n  - exp_id: dream_20260512T204322\\\\n    role: dream_simulate\\\\n    result: best=WA, median=WR, worst=R\\\\n  depends_on:\\\\n  - D008\\\\n- id: D010\\\\n  date: 2026-05-12 22:09 UTC\\\\n  summary: plan_013 (second encoder) 从 P1 升级至 P0，headline template 降调修复\\\\n  rationale: Reviewer 指出 single encoder 是 best→accept 的关键区分因素，在 best-R1-W1 和 median-R2-W5\\\\n    两档都出现。P1 排期可能导致论文缺少 generality 证据而被 WR。升级后 M2 完成即可并行启动 plan_013。同时修复 headline\\\\n    template \\\\\\\"cannot recover\\\\\\\" → \\\\\\\"complementary signal not captured by\\\\\\\"。\\\\n  related_experiments:\\\\n  - exp_id: plan_013\\\\n    role: priority_upgrade\\\\n    result: P1→P0\\\\n  depends_on:\\\\n  - D009\\\\n- id: D011\\\\n  date: 2026-05-13 01:38 UTC\\\\n  summary: Z%=74.0% 确认 Best Framing — Claim 1 为 headline，批准 M2 早期训练\\\\n  rationale: M1 部分数据（24/222 repos, 5128 instances）Z%=74.0%，远超 ≥35% 阈值。对比 D007 的 40.8%（50\\\\n    SWE-bench repos），SWE-Smith 数据集跨文件依赖密度更高。Best framing 成立：Claim 1 (\\\\\\\"structure-grounded\\\\n    negatives outperform\\\\\\\") 为 headline。批准在当前 5K instances 上做 M2 早期训练 pilot（3 strategies\\\\n    × 1 seed），利用 cuda:4 空闲期获取早期信号，不等全量 M1（还需 ~46h）。磁盘已清理至 61GB free (64%)，足够训练。\\\\n  related_experiments:\\\\n  - exp_id: m1_extraction\\\\n    role: data_source\\\\n    result: Z%=74.0% at 24/222 repos\\\\n  - exp_id: d007_50repo_overlap\\\\n    role: baseline\\\\n    result: Z%=40.8% on SWE-bench 50 repos\\\\n  depends_on:\\\\n  - D009\\\\n  - D010\\\\n- id: D012\\\\n  date: 2026-05-13 02:11 UTC\\\\n  summary: Kill m2_early_pilot_v3 (PID 897752) — 第二次 GPU 越界 (cuda:0)\\\\n  rationale: Reviewer 发现 m2_early_pilot_v3 在 cuda:0 运行（PID 897752, 17100 MiB），项目仅分配\\\\n    cuda:4。这是第二次 GPU 越界（第一次 D005 在 GPU 5）。立即 kill 并标记 killed。同时 m2_early_pilot_v2\\\\n    因 wandb API key error 已崩溃标记 FAILED。当前唯一合法训练为 PID 795791 (m2_early_pilot, cuda:4)。要求\\\\n    Agent 排查越界原因并确保后续脚本强制 CUDA_VISIBLE_DEVICES=4。\\\\n  related_experiments:\\\\n  - exp_id: m2_early_pilot_v3\\\\n    role: violated\\\\n    result: killed - GPU 越界 cuda:0\\\\n  - exp_id: m2_early_pilot_v2\\\\n    role: failed\\\\n    result: wandb API key error\\\\n  - exp_id: m2_early_pilot\\\\n    role: active\\\\n    result: PID 795791 on cuda:4, running\\\\n  depends_on:\\\\n  - D011\\\\n- id: D013\\\\n  date: 2026-05-13 02:50 UTC\\\\n  summary: 服务器迁移：cqa1-21977 cuda:4 → bjb1-42106 cuda:0/1 (RTX PRO 6000 96GB×2)\\\\n  rationale: Manager 分配独立服务器 bjb1-42106（2x RTX PRO 6000 96GB）。迁移策略：(1) M1 提取继续在 cqa1-21977\\\\n    CPU 上完成（不中断），(2) 新服务器立即搭建环境+同步代码+下载模型，(3) M2 early pilot 在 cqa1-21977 cuda:4 跑完后所有\\\\n    GPU 工作转到新服务器，(4) 通知 Manager 释放 cuda:4。RTX PRO 6000 96GB 彻底解决 M3a VRAM 问题（Qwen3.6-27B\\\\n    不再需要 fallback），2 卡可并行 M2 全量 + plan_013。\\\\n  related_experiments:\\\\n  - exp_id: m2_early_pilot\\\\n    role: in_progress\\\\n    result: finishing on cqa1-21977 cuda:4\\\\n  - exp_id: m1_extraction\\\\n    role: in_progress\\\\n    result: CPU only, stays on cqa1-21977\\\\n  depends_on:\\\\n  - D011\\\\n- id: D014\\\\n  date: 2026-05-13 04:44 UTC\\\\n  summary: Kill m2_early_pilot (PID 795791) — 过拟合+卡死，bjb1 m2_embed_verify 取代\\\\n  rationale: m2_early_pilot 在 cqa1 cuda:4 上仅完成 random 策略（best val_loss=0.5879 at step\\\\n    1500，之后持续过拟合到 0.728）。进程在 step 4000 卡死 45+ min。OOM 干扰（另一进程在同 GPU 启动）。embedding_distance\\\\n    和 dataflow_aware 策略未启动。bjb1 上的 m2_embed_verify 使用 true embedding mining + 更大参数（negatives=7,\\\\n    seq_len=2048, batch=8）+ eval bug fix，将完全取代此 pilot。通知 Manager 释放 cqa1 cuda:4。\\\\n  related_experiments:\\\\n  - exp_id: m2_early_pilot\\\\n    role: killed\\\\n    result: random best val_loss=0.5879, overfitting after step 1500\\\\n  - exp_id: m2_embed_verify\\\\n    role: replacement\\\\n    result: preparing on bjb1 cuda:1\\\\n  depends_on:\\\\n  - D011\\\\n  - D013\\\\n- id: D015\\\\n  date: 2026-05-13 11:43 UTC\\\\n  summary: 全量 Z%=78.0%（条件）确认 Best Framing；Coverage 34.3% 需论文讨论\\\\n  rationale: 全量 M1（123/131 repos, 44,173 instances）统计：15,153 instances 有结构数据（34.3%），其中\\\\n    11,825 有 connected-but-not-gold 文件（条件 Z%=78.0%，高于 pilot 72.5%）。条件 Z% 远超 35% 阈值，Best\\\\n    Framing（Claim 1 as headline）完全成立。但 Coverage 仅 34.3%——65.7% instances CodeQL/Beniget\\\\n    未产出结构连接，论文需讨论此局限性并限定 claim 范围为\\\\\\\"有结构数据的 instances\\\\\\\"。\\\\n  related_experiments:\\\\n  - exp_id: m1_extraction\\\\n    role: data_source\\\\n    result: 123/131 repos, 44173 instances, 15897 structural\\\\n  - exp_id: plan_006_scalability\\\\n    role: prior_pilot\\\\n    result: pilot Z%=72.5% on 29 repos\\\\n  depends_on:\\\\n  - D011\\\\n- id: D016\\\\n  date: 2026-05-13 15:24 UTC\\\\n  summary: 'Reviewer Critical: m2_embed_verify 和 plan_013_starcoder 实际已完成全部 3 策略，registry\\\\n    错误标记为 failed'\\\\n  rationale: Reviewer 直接从服务器日志验证：两个实验的 dataflow 策略均已完成（\\\\\\\"All 3 strategies completed\\\\\\\"），EXIT_CODE\\\\n    异常发生在训练完成之后（wrapper 脚本问题）。关键数据：(1) Qwen dataflow peak R@1=0.5584 (+2.27pp vs random)，支撑\\\\n    Claim 1；(2) StarCoder dataflow R@1=0.4869 < random 0.4922，encoder-agnostic claim\\\\n    受挑战；(3) 两个编码器的 dataflow 策略均严重过拟合（train loss→0）。已派 Agent 紧急修正 registry + 收集完整 metrics\\\\n    + 验证 StarCoder random 数据来源。方向决策待 Agent 汇报验证数据后确定。\\\\n  related_experiments:\\\\n  - exp_id: m2_embed_verify\\\\n    role: primary\\\\n    result: 实际完成（3 strategies all done），Qwen dataflow peak R@1=0.5584\\\\n  - exp_id: plan_013_starcoder\\\\n    role: primary\\\\n    result: 实际完成（3 strategies all done），StarCoder dataflow R@1=0.4869 < random 0.4922\\\\n  depends_on: []\\\\n- id: D017\\\\n  date: 2026-05-13 16:03 UTC\\\\n  summary: Pilot 结果验证完成：embedding > random 跨编码器一致；dataflow 需按两种 checkpoint 标准报告；Claim\\\\n    2 需修订\\\\n  rationale: 'Reviewer 验证 18 个指标全部精确匹配。核心发现：(1) embedding > random 在 Qwen (+2.0pp)\\\\n    和 StarCoder (+1.6pp) 上一致，是最稳健结论；(2) dataflow 排名取决于 checkpoint 选择——按 val_loss:\\\\n    embedding > dataflow > random (Qwen)，按 peak R@1: dataflow > embedding > random\\\\n    (Qwen)；(3) StarCoder dataflow final eval 追平 embedding (0.5078=0.5078)，\\\\\\\"embedding\\\\n    consistently beats dataflow\\\\\\\" 不成立；(4) Claim 2 (\\\\\\\"embedding harms\\\\\\\") 在 true embedding\\\\n    mining 下不复现，仅在 MVP BM25 proxy 下成立。全量 M2 训练需报告两种 checkpoint 标准下的结果，避免 cherry-picking\\\\n    质疑。Paper framing 修订延后至全量 M2 结果出来后。'\\\\n  related_experiments:\\\\n  - exp_id: m2_embed_verify\\\\n    role: primary\\\\n    result: 'Qwen: embedding(0.5557) > dataflow(0.5436) > random(0.5357) by val_loss;\\\\n      dataflow peak(0.5584) > embedding(0.5557) by R@1'\\\\n  - exp_id: plan_013_starcoder\\\\n    role: primary\\\\n    result: 'StarCoder: embedding(0.5078) > random(0.4922) > dataflow(0.4869) by val_loss;\\\\n      dataflow final(0.5078) = embedding'\\\\n  depends_on:\\\\n  - D016\\\\n- id: D018\\\\n  date: 2026-05-13 16:04 UTC\\\\n  summary: 不做预判性 framing pivot，full M2 (18 runs) 是 go/no-go 唯一判据；双 checkpoint 标准；准备\\\\n    B/C 两条后备路线\\\\n  rationale: Pilot 仅 24 repos / 1 seed，<2pp delta 统计功效不足以支持强 claim 或否决原假设。Full M2\\\\n    (131 repos × 3 strategies × 3 seeds × 2 encoders = 18 runs) 提供 3-seed 统计功效，是唯一可信判据。不选\\\\n    Agent 提议的 A/B/C 任何一个——过早锁定叙事会限制后续解读空间。数据构建已在进行，不浪费时间在 framing 讨论上。Full M2 结果出来后根据实际数据\\\\n    pattern 决定：(a) dataflow 跨编码器一致 > random → 原 framing 修正后可用；(b) dataflow 不一致但 embedding\\\\n    一致 → 方案 B 或 C；(c) 所有差异不显著 → 需要更大规模实验或 pivot。同时要求 dual checkpoint (best-val-loss\\\\n    + best-R@1) 和 3-seed CI 确保结果可信。\\\\n  related_experiments:\\\\n  - exp_id: m2_embed_verify\\\\n    role: evidence\\\\n    result: pilot underpowered (1 seed, 24 repos)\\\\n  - exp_id: plan_013_starcoder\\\\n    role: evidence\\\\n    result: pilot underpowered (1 seed, 24 repos)\\\\n  depends_on:\\\\n  - D017\\\\n- id: D019\\\\n  date: 2026-05-13 18:08 UTC\\\\n  summary: D018 补充：Full M2 go/no-go 量化阈值 + 统计检验方案\\\\n  rationale: 'Reviewer 指出 D018 缺量化阈值，go/no-go 判据需在结果出来前明确，避免事后 rationalization。\\\\n\\\\n\\\\n    **统计方法**：每个 encoder 3 seeds 的 R@1 (best-by-val-loss checkpoint) 做 paired difference，bootstrap\\\\n    95% CI + paired t-test (p<0.05)。同时报告 best-by-R@1 checkpoint 结果作为透明度补充。\\\\n\\\\n\\\\n    **Go/No-Go 阈值**：\\\\n\\\\n    (A) Go — 原 framing 可用：dataflow > random 的 95% CI 在两个 encoder 上均 > 0\\\\n\\\\n    (B) Conditional Go — 修正 framing：dataflow > random 在至少一个 encoder 上 CI > 0，另一个 CI\\\\n    含 0（差异不显著）\\\\n\\\\n    (C) No-Go for Claim 1：dataflow ≤ random 在两个 encoder 上 CI 均含 0 或为负 → Claim 1 失效，pivot\\\\n    到 \\\\\\\"mining strategy × architecture\\\\\\\" 分析论文\\\\n\\\\n\\\\n    **Claim 2 判据**：若 full M2 显示 embedding > random 且 CI > 0 → 原 Claim 2 (\\\\\\\"embedding\\\\n    harms\\\\\\\") 被否定。新 Claim 2 候选：\\\\\\\"true embedding mining helps, but BM25 proxy harms\\\\\\\" 或\\\\n    \\\\\\\"hard negative mining method matters more than hard negative source\\\\\\\"\\\\n\\\\n\\\\n    **跨 encoder 一致性规则**：\\\\n\\\\n    - 同方向同显著 → 强泛化 claim\\\\n\\\\n    - 同方向不同显著 → 条件 claim + architecture discussion\\\\n\\\\n    - 反方向 → Claim 1 原形式被拒，需 conditional reframe\\\\n\\\\n\\\\n    阈值在 full M2 结果出来前锁定，不允许事后修改。'\\\\n  related_experiments:\\\\n  - exp_id: m2_full_qwen\\\\n    role: primary\\\\n    result: RUNNING - random_s42 in progress\\\\n  - exp_id: m2_full_starcoder\\\\n    role: primary\\\\n    result: RUNNING - data build phase\\\\n  depends_on:\\\\n  - D018\\\\n- id: D020\\\\n  date: 2026-05-13 18:10 UTC\\\\n  summary: D019 补充：Claim 2 完整判定矩阵 + n=3 功效限制声明\\\\n  rationale: 'Reviewer 指出 D019 的 Claim 2 阈值不完整 + n=3 统计功效天然受限。补充如下：\\\\n\\\\n\\\\n    **Claim 2 完整判定矩阵**（3 seeds, paired bootstrap 95% CI）：\\\\n\\\\n    (i) random > embedding CI>0 → Claim 2 confirmed（embedding harms，与 MVP 一致）\\\\n\\\\n    (ii) embedding > random CI>0 → Claim 2 falsified（true embedding mining helps，需\\\\n    reframe）\\\\n\\\\n    (iii) CI 含 0 → inconclusive（效应存在但检测不到或确实无差异，论文报告为 \\\\\\\"no significant difference\\\\\\\"\\\\n    + 报告 effect size）\\\\n\\\\n\\\\n    **n=3 功效限制**（显式承认，不修改阈值）：\\\\n\\\\n    - df=2 时 t 临界值 4.303，pilot 级别差异（<2pp）极难达到 p<0.05\\\\n\\\\n    - Bootstrap n=3 仅 27 种重采样，CI 估计粗糙\\\\n\\\\n    - 阈值框架偏向 No-Go（Type II error 高）\\\\n\\\\n    - 若结果落入 (C) No-Go，论文 Discussion 必须讨论功效限制，不能简单声明 \\\\\\\"dataflow 无效\\\\\\\"\\\\n\\\\n    - 这是算力约束下的合理选择，不改阈值，但明确风险\\\\n\\\\n\\\\n    **plan_014 排期**：Full M2 完成后优先启动 plan_014（temperature ablation, ~10h）——无论 Claim\\\\n    2 reframe 成哪个方向，temperature regime-specificity 都需要回答。'\\\\n  related_experiments:\\\\n  - exp_id: m2_full_qwen\\\\n    role: primary\\\\n    result: RUNNING\\\\n  - exp_id: m2_full_starcoder\\\\n    role: primary\\\\n    result: RUNNING\\\\n  depends_on:\\\\n  - D019\\\\n- id: D021\\\\n  date: 2026-05-13 19:10 UTC\\\\n  summary: Negative difficulty 分析揭示 encoder capacity 差异是 dataflow 效果不一致的根因\\\\n  rationale: '预训练模型 cosine similarity 分析显示：Qwen pretrained embeddings 分辨力弱（random\\\\n    cosine sim 0.899），StarCoder 分辨力强（random cosine sim 0.553）。Dataflow negatives 在两个模型上都比\\\\n    random 更难（higher sim），说明方法设计正确。但 StarCoder 已经\\\\\\\"懂\\\\\\\"结构差异（所有策略 sim 都低），额外训练信号边际收益小。这解释了\\\\n    pilot 中 StarCoder dataflow < random 的现象：不是方法问题，是 encoder 已有足够 capacity。\\\\n\\\\n\\\\n    论文价值：(1) 从 negative result 中提取 mechanistic explanation；(2) 定义 method applicability\\\\n    condition：\\\\\\\"structure-grounded negatives benefit most when pretrained encoder has\\\\n    limited structural separability\\\\\\\"；(3) 产出论文级图表（Figure: Negative Difficulty Distributions）；(4)\\\\n    无论 full M2 落入 A/B/C，这个分析都增加论文深度。不修改 go/no-go 阈值，但丰富解读框架。'\\\\n  related_experiments:\\\\n  - exp_id: m2_embed_verify\\\\n    role: context\\\\n    result: 'Qwen: dataflow > random (+0.8~2.3pp)'\\\\n  - exp_id: plan_013_starcoder\\\\n    role: context\\\\n    result: 'StarCoder: dataflow < random (-0.5pp), explained by high pretrained separability'\\\\n  depends_on:\\\\n  - D018\\\\n  - D019\\\\n- id: D022\\\\n  date: 2026-05-13 19:25 UTC\\\\n  summary: M1 28K instances 可恢复（运行时故障非数据问题）；当前 M2 继续，并行后台重跑 M1 提取\\\\n  rationale: 'Fuzzy match 抽查 10/10 发现 buggy_file 全部存在——28,276 个 \\\\\\\"error\\\\\\\" 是 CodeQL 并行提取时的运行时故障（磁盘/存储瞬态），不是\\\\n    SWE-smith 数据质量问题。训练数据潜在从 15,897 → ~44,173（2.8x）。\\\\n\\\\n\\\\n    决策：不中断当前 M2 训练 + 并行后台重跑 M1 提取。理由：\\\\n\\\\n    (1) 当前 M2 已在双卡运行，中断重来延期 3-7 天超出 DDL\\\\n\\\\n    (2) M1 重提取是 CPU 工作，可在 bjb1-42106 后台运行不影响 GPU 训练\\\\n\\\\n    (3) 如果当前 M2 结果落入 (C) No-Go 或 effect size 太小，扩展数据集是 natural next step\\\\n\\\\n    (4) 2.8x 数据量可能显著缓解 dataflow 过拟合问题（D021 中的核心风险）\\\\n\\\\n\\\\n    Claim 3 叙事需修正：\\\\\\\"64% failure 是上游数据问题\\\\\\\" → \\\\\\\"64% 是运行时提取故障，CodeQL 本身在有效输入上 100% 成功，可通过重跑恢复\\\\\\\"。这是\\\\n    engineering limitation with clear fix，不是方法局限。'\\\\n  related_experiments:\\\\n  - exp_id: m1_extraction\\\\n    role: primary\\\\n    result: 28,276 instances recoverable - runtime failure, not data quality\\\\n  - exp_id: plan_006_scalability\\\\n    role: affected\\\\n    result: 'error classification needs correction: buggy_file_not_found was misattributed'\\\\n  depends_on:\\\\n  - D018\\\\n  - D019\\\\n- id: D023\\\\n  date: 2026-05-13 19:43 UTC\\\\n  summary: Kill M1 重提取：bjb1 CodeQL 查询 100% 失败，D022 前提不成立需诊断后重新评估\\\\n  rationale: Reviewer CRITICAL 发现 bjb1-42106 上 CodeQL call_graph.ql 查询全部 exit status\\\\n    2，317/325 行失败，零有效结构数据产出。原 M1 在 cqa1-21977 成功，迁移后 CodeQL 版本/QL pack 可能不兼容。立即 kill\\\\n    进程释放 CPU/RAM，诊断 CodeQL 配置后决定修复或换服务器。\\\\n  related_experiments:\\\\n  - exp_id: m1_reextract\\\\n    role: subject\\\\n    result: killed - CodeQL incompatible on bjb1\\\\n  depends_on:\\\\n  - D022\\\\n- id: D024\\\\n  date: 2026-05-14 00:49 UTC\\\\n  summary: 'Major paper framing rewrite: drop falsified \\\\\\\"embedding harms\\\\\\\" claim, pivot\\\\n    to \\\\\\\"systematic analysis + mechanistic insight\\\\\\\" narrative'\\\\n  rationale: 'Reviewer deep assessment confirmed Claim 2 (\\\\\\\"embedding actively harms\\\\\\\",\\\\n    -27pp) was built on BM25-proxy mislabeled as embedding-distance in MVP. D017 proved\\\\n    true embedding mining helps (+1.6-2.0pp). New framing: (1) embedding universally\\\\n    helps (corrects misconception), (2) dataflow conditionally helps (mediated by\\\\n    representation saturation), (3) CodeQL scalable. This is a stronger, more honest\\\\n    paper type for EMNLP — empirical analysis with mechanistic depth rather than false\\\\n    \\\\\\\"our method beats all\\\\\\\" claim.'\\\\n  related_experiments:\\\\n  - exp_id: m2_embed_verify\\\\n    role: evidence\\\\n    result: embedding > random confirmed for both encoders\\\\n  - exp_id: plan_013_starcoder\\\\n    role: evidence\\\\n    result: dataflow helps Qwen only, not StarCoder — conditional benefit\\\\n  - exp_id: neg_difficulty_analysis\\\\n    role: evidence\\\\n    result: pos_sim saturation explains strategy-encoder interaction\\\\n  depends_on: []\\\\n- id: D025\\\\n  date: 2026-05-14 01:01 UTC\\\\n  summary: Plan_014 temperature ablation 缩减为 2 strategies × 3τ × 2 epochs = 6 runs\\\\n    (~70h)，deadline 可达\\\\n  rationale: 原方案 9 runs × 3 epochs = 157h GPU，超出 May 25 ARR 截稿。缩减理由：(1) 回答 Dream reviewer\\\\n    的 regime-specificity concern 只需证明 embedding vs random 的相对优势跨 τ 一致，不需要 3 策略全跑；(2)\\\\n    M2 和 pilot 均显示 epoch 3 过拟合无收益，2 epochs 足够；(3) τ=0.07 已由 M2 覆盖，只需 {0.05, 0.1, 0.2}。6\\\\n    runs × ~11.7h = ~70h → 双卡并行 35h wall time，M2 完成后 ~1.5 天可跑完。Dataflow strategy 的\\\\n    τ ablation 降为 P2，时间充裕再补。\\\\n  related_experiments:\\\\n  - exp_id: m2_full_qwen\\\\n    role: evidence\\\\n    result: step 1000 best, epoch 3 overfitting → 2 epochs sufficient\\\\n  - exp_id: plan_014\\\\n    role: target\\\\n    result: budget revised from 10h to 70h, scope from 9 to 6 runs\\\\n  depends_on:\\\\n  - D024\\\\n- id: D026\\\\n  date: 2026-05-14 02:56 UTC\\\\n  summary: Qwen eval@2000 确认过拟合，后续 M2 runs 从 3 epochs 减至 2 epochs\\\\n  rationale: 'eval@2000: val_loss=0.5162, R@1=0.5228（与 @1500 持平，未恢复）。Best 锁定 step\\\\n    1000 (epoch 1 中段)。train_loss=0.04 vs val_loss=0.52，gap 持续扩大。模式与 pilot 一致（best\\\\n    at ~25% training）。当前 s42 保留 3 epochs 完整跑完（提供 full overfitting curve 数据），后续 8 runs/encoder\\\\n    设 max_epochs=2。节省 ~48h/GPU，M2 完成时间从 ~May 20-21 提前到 ~May 18-19。'\\\\n  related_experiments:\\\\n  - exp_id: m2_full_qwen\\\\n    role: evidence\\\\n    result: eval@2000 R@1=0.5228 flat, overfitting confirmed\\\\n  - exp_id: m2_full_starcoder\\\\n    role: pending\\\\n    result: eval@1000 still improving, apply 2-epoch precaution for subsequent seeds\\\\n  depends_on:\\\\n  - D025\\\\n- id: D027\\\\n  date: 2026-05-14 08:13 UTC\\\\n  summary: M2 剩余 runs 加 early stopping (patience=2 evals)，加速关键路径\\\\n  rationale: Reviewer 计算 M2 全 18 runs 需 ~5.5 天（StarCoder 瓶颈 ~133h）。两个编码器 best checkpoint\\\\n    均在 step 1000，之后 val_loss 持续上升。加 early stopping（patience=2，即连续 2 次 eval@500 无改善即停）预计在\\\\n    step 2000 左右停止（vs 2828 full 2-epoch），节省 ~30% 时间（~1.5 天），M2 从 May 19.5 提前到 ~May\\\\n    18。关键路径 May 25 ARR 余量从 5 天增至 7 天。风险低：仅影响未启动的 runs，不改已跑数据。\\\\n  related_experiments:\\\\n  - exp_id: m2_full_qwen\\\\n    role: target\\\\n    result: running, best@1000, overfitting confirmed\\\\n  - exp_id: m2_full_starcoder\\\\n    role: target\\\\n    result: running, best@1000, overfitting confirmed\\\\n  depends_on:\\\\n  - D026\\\\n- id: D028\\\\n  date: 2026-05-14 11:09 UTC\\\\n  summary: Claim 2 降级待定：M2 full 结果决定 \\\\\\\"conditional benefit\\\\\\\" 是独立 claim 还是降为 observation\\\\n  rationale: Reviewer 覆盖率审查指出 Claim 2 最薄弱：n=2 encoders 交互效应无统计功效，neg_difficulty 是描述性非实验性证据。建议降为\\\\n    \\\\\\\"observation + mechanistic hypothesis\\\\\\\"。决策延迟到 M2 full 18 runs 完成后：若 Qwen dataflow>random\\\\n    p<0.05 则保持 conditional claim；否则降级为 observation。\\\\n  related_experiments:\\\\n  - exp_id: m2_embed_verify\\\\n    role: Qwen pilot positive\\\\n    result: dataflow > random +0.8pp val_loss\\\\n  - exp_id: plan_013_starcoder\\\\n    role: StarCoder pilot negative\\\\n    result: dataflow < random -0.5pp\\\\n  - exp_id: m2_full_qwen\\\\n    role: go/no-go for claim strength\\\\n    result: RUNNING\\\\n  - exp_id: m2_full_starcoder\\\\n    role: encoder generality test\\\\n    result: RUNNING\\\\n  depends_on:\\\\n  - D018\\\\n  - D019\\\\n- id: D029\\\\n  date: 2026-05-14 16:23 UTC\\\\n  summary: Dream full review 完成：7 条三档一致结构性问题确认，BM25 baseline 升为 P0，pool size sensitivity\\\\n    新增 plan_019\\\\n  rationale: 'dream_20260514T075732 (full review mode) 三档评分: Best 4/6 WA, Median 3/6\\\\n    WR, Worst 3/6 WR。跨三档一致的结构性问题 7 条：(1) 缺 BM25 baseline 是 #1 共识——论文核心叙事（纠正 CoCoHaNeRe）无实证支撑，已加\\\\n    plan_018 P0；(2) N=2 编码器限制——保持 honest framing，无法加更多编码器；(3) StarCoder 误标为 encoder-decoder——已修正为\\\\n    decoder-only；(4) RepoBench-R 无 CIs——plan_004 已标注多 seed 要求；(5) Pool=50 太小——新增 plan_019\\\\n    P1；(6) 34% structural coverage 未分层——plan_005 已扩展；(7) Checkpoint selection criterion\\\\n    未指定——写作时明确。观察项：effect sizes 太小（等 M2 真实数据）、overfitting 分析（提取现有训练 log）。忽略项：broken\\\\n    bibliography（dream artifact）、0 figures（dream artifact）。评分顺序正常（best≥median=worst）。下一步：派\\\\n    Agent 准备 BM25 mining（CPU），M2 完成后立即执行 plan_018 training phase。'\\\\n  related_experiments:\\\\n  - exp_id: plan_018\\\\n    role: new P0 experiment added\\\\n    result: planned\\\\n  - exp_id: plan_019\\\\n    role: new P1 experiment added\\\\n    result: planned\\\\n  - exp_id: plan_004\\\\n    role: updated with multi-seed CI requirement\\\\n    result: planned\\\\n  - exp_id: plan_005\\\\n    role: extended with structural coverage stratification\\\\n    result: planned\\\\n  depends_on:\\\\n  - D024\\\\n  - D028\\\\n- id: D030\\\\n  date: 2026-05-14 16:23 UTC\\\\n  summary: Dream dream_20260514T075732 分析完成：7 项确认行动 + 5 项观察项 + re-dream 后批准新 P0\\\\n  rationale: 'Dream full review (2 Reviewers roundtable) 三档评分: Best=4/6(WA), Median=3/6(WR),\\\\n    Worst=3/6(WR)。Median 未达 borderline，需修复结构性问题后 re-dream。\\\\n\\\\n\\\\n    **三档一致的结构性问题（7 项确认行动）：**\\\\n\\\\n    1. [EXP] 缺 BM25 negative baseline — 论文核心 narrative (correcting CoCoHaNeRe) 无实证。加\\\\n    plan_018, P0, Phase1 CPU 立即启动\\\\n\\\\n    2. [EXP] RepoBench-R 缺 CIs — plan_004 增加多 seed 评估\\\\n\\\\n    3. [EXP] Pool size 50 过小 — 加 plan_019 sensitivity analysis\\\\n\\\\n    4. [EXP] 34% structural coverage 未分层 — 扩展 plan_005 加 structural-available vs fallback\\\\n    stratum + neg_difficulty quartile\\\\n\\\\n    5. [FRAMING] N=2 encoders → 降级为 \\\\\\\"observation + hypothesis\\\\\\\"，非 validated mechanism\\\\n\\\\n    6. [FRAMING] StarCoder 架构 → 修正为 \\\\\\\"decoder-only\\\\\\\"（已改）\\\\n\\\\n    7. [FRAMING] Claim 3 (CodeQL pipeline) → 降为 supporting methodology（已改）\\\\n\\\\n\\\\n    **观察项（等真实数据）：**\\\\n\\\\n    1. Effect sizes marginal [M][W] — 等 M2 full 统计结果\\\\n\\\\n    2. Dataflow claim strength [M][W] — D028 已 plan\\\\n\\\\n    3. \\\\\\\"Scaling law\\\\\\\" [W] → 用 \\\\\\\"trend\\\\\\\" + CIs\\\\n\\\\n    4. Temperature ablation contradiction [W] — plan_014 结果决定\\\\n\\\\n    5. Zero method contribution [M][W] — framing 强度决定\\\\n\\\\n\\\\n    **Re-dream 要求：** framing + plan 修改完成后需 re-dream，best ≥ WA 且 median ≥ borderline\\\\n    后才批准新 P0 实验。已在跑的实验继续。'\\\\n  related_experiments:\\\\n  - exp_id: dream_20260514T075732\\\\n    role: trigger\\\\n    result: best=4/6 WA, median=3/6 WR, worst=3/6 WR\\\\n  - exp_id: plan_018\\\\n    role: new_from_dream\\\\n    result: planned — BM25 baseline\\\\n  - exp_id: plan_019\\\\n    role: new_from_dream\\\\n    result: planned — pool size sensitivity\\\\n  depends_on:\\\\n  - D028\\\\n  - D024\\\\n- id: D031\\\\n  date: 2026-05-14 17:02 UTC\\\\n  summary: 'BM25 Phase 1 完成: 87% overlap with embedding_distance，预示论文叙事可能从 \\\\\\\"纠正误标\\\\\\\"\\\\n    转向 \\\\\\\"受控对比证明 hard negatives 普遍有效\\\\\\\"'\\\\n  rationale: 'plan_018 Phase 1 (CPU) 完成。3 seeds BM25 negatives 已生成，与 embedding_distance\\\\n    negatives 重叠率高达 87.1%。小 repo 候选池 ≤50 导致所有策略完全重合，BM25 differentiation 主要在大 repo\\\\n    上体现。\\\\n\\\\n\\\\n    Phase 2 训练结果预期 3 种可能：\\\\n\\\\n    A) BM25 harm (BM25 << random) → 原叙事成立（\\\\\\\"BM25 proxy 导致 CoCoHaNeRe 错误结论\\\\\\\"）\\\\n\\\\n    B) BM25 ≈ random → contingency per D030（叙事降为 \\\\\\\"systematic comparison\\\\\\\"）\\\\n\\\\n    C) BM25 ≈ embedding_distance (87% overlap 强烈预示) → 叙事升级为\\\\\\\"BM25 和 embedding mining\\\\n    高度重叠，两者在受控环境下都优于 random；CoCoHaNeRe 的负面结论源于实验控制不足而非 BM25-proxy 本身\\\\\\\"\\\\n\\\\n\\\\n    Scenario C 实际上比 A 更强——我们提供的不只是标签纠正，而是受控对比 + 叙事升级。\\\\n\\\\n\\\\n    附带决策：plan_015 暂缓至 camera-ready（44h 超预算 + DDL 紧），Limitations 中承认 static vs dynamic\\\\n    confound。'\\\\n  related_experiments:\\\\n  - exp_id: plan_018\\\\n    role: phase1_complete\\\\n    result: BM25 data ready, 87% overlap with embedding_distance\\\\n  - exp_id: plan_015\\\\n    role: deferred\\\\n    result: design complete, execution deferred to camera-ready\\\\n  depends_on:\\\\n  - D030\\\\n- id: D032\\\\n  date: 2026-05-14 17:02 UTC\\\\n  summary: plan_015 缩减为 1 seed × dynamic_ep (~11h)；BM25 overlap 87% 需分层验证\\\\n  rationale: 'plan_015 原设计 3 variants × 多 seeds = 44h，DDL May 25 前 GPU 时间不够。缩减为 dynamic_ep\\\\n    × 1 seed (Qwen s42) ~11h，足以排除 static vs dynamic confound。预期 dynamic ≈ static（<1pp），在\\\\n    Limitation 段写实验证据。\\\\n\\\\n\\\\n    BM25 Phase 1 完成：BM25 vs embedding overlap 87.1%。但 Agent 指出小 repo (pool ≤50) 导致所有策略\\\\n    negatives 重合——overlap 被拉高。已派补充分析按 repo 大小分层统计真实差异化程度。Phase 2 训练结果将决定 CoCoHaNeRe\\\\n    narrative 是否需要 pivot（contingency 已在 paper_framing.md）。'\\\\n  related_experiments:\\\\n  - exp_id: plan_015\\\\n    role: scope_reduction\\\\n    result: 44h→11h, 1 seed × dynamic_ep only\\\\n  - exp_id: plan_018\\\\n    role: phase1_complete\\\\n    result: BM25 vs embedding overlap 87.1%, 3 seeds done\\\\n  depends_on:\\\\n  - D030\\\\n- id: D033\\\\n  date: 2026-05-14 17:10 UTC\\\\n  summary: D031 修正：BM25 top-7 overlap 远低于 k=50 的 87%，大 repo 仅 30%，Phase 2 将有区分度\\\\n  rationale: '分层 Jaccard 分析（top-7, seed 42, 2920 matched queries）显示 BM25 vs embedding_distance\\\\n    重叠率：small=67%, medium=38%, large=30%。之前报告的 87% 是 k=50 全候选重叠，训练实际用 top-7 negatives\\\\n    差异大得多。\\\\n\\\\n\\\\n    关键修正：D031 中预判的 \\\\\\\"BM25 ≈ embedding_distance\\\\\\\" 不再成立。Phase 2 训练预期结果重新开放为三种可能（BM25 harm\\\\n    / neutral / help），实验区分度足够。\\\\n\\\\n\\\\n    方法论 flag: BM25 使用 whitespace tokenization (str.split())，不处理 camelCase/snake_case。如果\\\\n    BM25 表现差，tokenization 可能是 confound。论文中需标注。Reviewer 已指出。\\\\n\\\\n\\\\n    24% match rate 源于 BM25 mining 使用了不同 train/val split，不影响分层趋势结论但如需严格配对可重新生成。'\\\\n  related_experiments:\\\\n  - exp_id: plan_018\\\\n    role: phase1_analysis\\\\n    result: 'stratified overlap: large_repo BM25-vs-embedding=30%, BM25-vs-random=0.7%'\\\\n  depends_on:\\\\n  - D031\\\\n- id: D034\\\\n  date: 2026-05-14 17:50 UTC\\\\n  summary: Re-dream gate 未通过但决定继续：median=WR 由不可修复因素驱动（novelty/effect-size/n=2），override\\\\n    gate 推进 Phase 2\\\\n  rationale: 'Re-dream dream_20260514T162530 评分：Best=4/6(WA), Median=3/6(WR), Worst=3/6(WR)。与首次\\\\n    dream 完全一致，修复 BM25 baseline + pool size + framing 降级未改变评分。\\\\n\\\\n\\\\n    Gate 要求 median ≥ borderline。分析 median WR 原因：\\\\n\\\\n    1. Novelty (\\\\\\\"ANCE for code\\\\\\\") — 不可修复，是 framing 层面问题\\\\n\\\\n    2. Effect sizes (pool=200: +0.4~0.7pp) — 数据决定，不可修复\\\\n\\\\n    3. N=2 encoders — DDL 前不可加\\\\n\\\\n    4. Dataflow null — 数据已确定\\\\n\\\\n    5. Bibliography (2 citations) — dream artifact，实际论文可修\\\\n\\\\n\\\\n    因素 1-4 是 dream 模拟的固有限制（无论怎么改 plan，dream 想象的 median/worst 数据都会是 marginal），而非实验设计缺陷。Best\\\\n    case 达到 WA=4/6 并且 R1 明确给出 \\\\\\\"specify K + checkpoint criterion → 5/6\\\\\\\" 路径。\\\\n\\\\n\\\\n    决策：Override gate，允许 Phase 2 在 GPU 空闲时执行。理由：\\\\n\\\\n    (a) 阻塞因素为写作/scope 层面，非实验层面，更多 dream 不会改变\\\\n\\\\n    (b) Best case BM25 baseline 被评为 \\\\\\\"paper''s most clean-cut contribution\\\\\\\"\\\\n\\\\n    (c) ARR May 25 DDL 时间紧，Phase 2 是关键路径\\\\n\\\\n    (d) Writing 层面的修复（related work, specification）会在实际论文中自然解决'\\\\n  related_experiments:\\\\n  - exp_id: dream_20260514T162530\\\\n    role: re-dream\\\\n    result: best=4/6 WA, median=3/6 WR, worst=3/6 WR — unchanged from first dream\\\\n  - exp_id: plan_018\\\\n    role: gate_override\\\\n    result: Phase 2 approved despite gate not passing\\\\n  depends_on:\\\\n  - D030\\\\n  - D031\\\\n  - D033\\\\n- id: D035\\\\n  date: 2026-05-14 18:48 UTC\\\\n  summary: Claim 2 降级：从 \\\\\\\"conditional benefit beyond embedding mining\\\\\\\" 降为 \\\\\\\"exploratory\\\\n    observation\\\\\\\"\\\\n  rationale: Reviewer 覆盖率审查发现 pilot 数据不支持 \\\\\\\"beyond embedding mining\\\\\\\"——两个编码器都是 dataflow\\\\n    < embedding (Qwen -1.2pp, StarCoder -1.0pp)。0/3 支撑实验完成。降级为观察+机制假说，不再作为核心贡献。paper_framing.md\\\\n    已更新。\\\\n  related_experiments:\\\\n  - exp_id: m2_embed_verify\\\\n    role: evidence\\\\n    result: embedding > dataflow on both encoders\\\\n  - exp_id: plan_013_starcoder\\\\n    role: evidence\\\\n    result: 'StarCoder: embedding 0.5174 > dataflow 0.5078'\\\\n  depends_on:\\\\n  - D028\\\\n- id: D036\\\\n  date: 2026-05-14 19:10 UTC\\\\n  summary: M2 checkpoint 选择统一用 R@1 而非 val_loss 作为 primary criterion\\\\n  rationale: Reviewer 核实 s43 发现 val_loss 最优在 step 500、R@1 最优在 step 1500，两个 criterion\\\\n    给出不同最优点。检索任务的目标指标是 R@1，val_loss 仅反映语言建模质量，不直接对应下游检索性能。统一用 R@1 选 checkpoint 确保论文报告一致性，后续所有\\\\n    M2 实验沿用此标准。\\\\n  related_experiments:\\\\n  - exp_id: m2_full_qwen_continued\\\\n    role: 触发\\\\n    result: s43 val_loss best@500 vs R@1 best@1500\\\\n  - exp_id: m2_full_starcoder_resumed\\\\n    role: 同步适用\\\\n    result: 进行中\\\\n  depends_on: []\\\\n- id: D037\\\\n  date: 2026-05-14 19:13 UTC\\\\n  summary: 'D037: M2 checkpoint 改为只存 LoRA adapter weights，不存 merged 完整模型'\\\\n  rationale: 磁盘剩余 43GB，后续 18 runs 需 ~249GB checkpoint 空间。根因：LoRA rank=16 的 3B 模型存完整\\\\n    float16 merged weights (5.8GB/checkpoint)，但 adapter 仅 ~100MB。改为 PeftModel.save_pretrained\\\\n    只存 adapter，18 runs × 2 checkpoints × 100MB ≈ 3.6GB，彻底解决。同时删旧 pilot 输出 (+66GB)\\\\n    和 final 目录 (+11.6GB) 作为即时缓解。与 mvp_p2b_contrastive_training 磁盘满崩溃为同一 failure pattern。\\\\n  related_experiments:\\\\n  - exp_id: m2_full_qwen_continued\\\\n    role: 受影响\\\\n    result: 剩余 7 runs 将受益于 adapter-only saving\\\\n  - exp_id: m2_full_starcoder_resumed\\\\n    role: 受影响\\\\n    result: 剩余 7 runs 同样受益\\\\n  depends_on: []\\\\n- id: D038\\\\n  date: 2026-05-14 20:39 UTC\\\\n  summary: Plan 005 分层分析需额外控制 pool_size；dataflow richness 维度不单独做 claim\\\\n  rationale: Confound 分析显示 rich-dataflow 实例的候选池远大于 moderate（46-50 vs 17-37），pool_size\\\\n    机械性驱动 R@1 差异。控制 repo_size 后模式不消失，确认 pool_size 才是真正 confound。论文中 dataflow richness\\\\n    维度需 pool_size-matched 对比后才能下结论。\\\\n  related_experiments:\\\\n  - exp_id: plan_005_stratified\\\\n    role: evidence\\\\n    result: dry-run 确认 confound 存在\\\\n  depends_on: []\\\\n- id: D039\\\\n  date: 2026-05-14 20:40 UTC\\\\n  summary: 分层分析 R@1 数据无效：dry-run mock predictions，非真实模型结果。confound 分布结构(repo_size×dataflow)有效保留。\\\\n  rationale: Reviewer critical 审查确认：stratified_dryrun v1/v2 和 confound_analysis 的所有\\\\n    R@1 值均来自 dry-run mock predictions。策略排序模式和优势幅度需用 M2 真实 checkpoint 重新验证。仅 cross-tabulation\\\\n    分布结构（rich dataflow 99.3% 集中在 large/xlarge repos, Spearman ρ=0.077）为真实数据，可用于论文写作中声明\\\\n    confound 关系。plan_005_stratified 必须等 M2 真实 checkpoint 完成后执行。\\\\n  related_experiments:\\\\n  - exp_id: worker_analysis_dataflow_reposize_confound\\\\n    role: invalidated_analysis\\\\n    result: R@1 from mock data, distribution structure valid\\\\n  - exp_id: m2_full_qwen_continued\\\\n    role: dependency\\\\n    result: running - provides real checkpoints\\\\n  - exp_id: m2_full_starcoder_resumed\\\\n    role: dependency\\\\n    result: running - provides real checkpoints\\\\n  depends_on: []\\\\n- id: D040\\\\n  date: 2026-05-14 21:27 UTC\\\\n  summary: Claim 1 framing 微调：从\\\\\\\"纠正 embedding negatives 不行的误解\\\\\\\"改为\\\\\\\"挑战必须用昂贵 gradient-based\\\\n    方法的假设\\\\\\\"\\\\n  rationale: CoCoHaNeRe (ACM TOSEM 2025) 实际论点是 non-differentiable embedding negatives\\\\n    \\\\\\\"slow and ineffective\\\\\\\"（相对 gradient-based），并非说 embedding negatives 有害。原 Claim 1\\\\n    \\\\\\\"correcting misconception\\\\\\\" 措辞会被审稿人以 CoCoHaNeRe 原文反驳。新措辞\\\\\\\"simple static embedding-distance\\\\n    mining suffices, challenging the assumption that expensive gradient-based hard\\\\n    negative methods are necessary\\\\\\\"更准确、更defensible，且保留 contribution。\\\\n  related_experiments:\\\\n  - exp_id: plan_017_literature\\\\n    role: evidence\\\\n    result: CoCoHaNeRe framing conflict identified during related work expansion\\\\n  depends_on: []\\\\n\\\", \\\"total_chars\\\": 31588, \\\"truncated\\\": false}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/decisions.yaml\", \"content\": \"_next_id: 41\\ndecisions:\\n- id: D001\\n  date: 2026-05-12 09:57 UTC\\n  summary: 'MVP 设计: CodeQL 试点(10 repos) + 迷你对比训练(500 instances) 验证核心假设'\\n  rationale: 13 天 DDL，需要最快速验证核心假设链：(1) CodeQL inter-procedural data-flow 在 Python\\n    repos 上可行（timeout < 30%），(2) data-flow hard negatives 比 random negatives 提升检索\\n    recall。两个 phase 串行，总计约 1 天。通过后立即进入全量数据提取和训练。\\n  related_experiments: []\\n  depends_on: []\\n- id: D002\\n  date: 2026-05-12 10:01 UTC\\n  summary: '采纳 Reviewer 反馈: MVP Phase 2 增加线性分类器 proxy 验证 + 3-seed 训练 + 显式 kill criteria'\\n  rationale: 'Reviewer 指出 Phase 2 原方案（500 instances, ~100 held-out, 2pp gate）统计效力不足，2pp\\n    差异在随机噪声范围内。增加: (1) Phase 2a 线性分类器 proxy 验证解耦特征质量与训练策略；(2) 3-seed 训练要求 ≥2/3 seed\\n    提升；(3) 每个 phase 的 fail→kill/fallback 路径。防止 13 天 DDL 下的沉没成本陷阱。'\\n  related_experiments: []\\n  depends_on:\\n  - D001\\n- id: D003\\n  date: 2026-05-12 10:02 UTC\\n  summary: 'H2 验证并入 Phase 1: 提取后立即统计 data-flow 连通文件 vs 不连通文件的 gold patch 覆盖率差异'\\n  rationale: Reviewer 指出 H2（特征区分度）在原 MVP 中无独立验证，Phase 2 失败时无法区分是 H2 还是 H3 问题。零成本 sanity\\n    check（统计连通/不连通文件的 gold patch 覆盖率）可在 Phase 1 提取完后立即执行，不需要训练。这比 Phase 2a 的线性分类器更早给出诊断信号。\\n  related_experiments: []\\n  depends_on:\\n  - D002\\n- id: D004\\n  date: 2026-05-12 11:21 UTC\\n  summary: 'Phase 1 gate PASS: timeout 0%, H2 Fisher p=1.54e-7, 75% instance recall.\\n    进入 Phase 2。'\\n  rationale: 10 repos 中 8 个成功提取（2 个 skip 因 buggy file 路径不存在，非 CodeQL 限制）。timeout rate\\n    0% 远低于 30% 阈值。H2 sanity check：连通文件 gold 覆盖 1.44% vs 不连通 0.00%，Fisher p=1.54e-7。75%\\n    instance recall（6/8 gold file 在连通集）。数据质量问题（路径匹配、skip rate、registry 注册）并行修复，不阻塞\\n    Phase 2。\\n  related_experiments: []\\n  depends_on: []\\n- id: D005\\n  date: 2026-05-12 11:35 UTC\\n  summary: 'CRITICAL: GPU 越界 PID 59170 跑在 GPU 5 而非分配的 cuda:4，立即 kill + 全脚本修复 CUDA_VISIBLE_DEVICES'\\n  rationale: Reviewer 核实 nvidia-smi 发现 run_mvp.py 在 GPU 5 上运行 9.3GB，而项目分配的 cuda:4\\n    完全空闲。违反 L1 红线（GPU 资源边界）。要求 Agent 立即 kill 进程、修复所有脚本强制 CUDA_VISIBLE_DEVICES=4、排查\\n    dry-run 是否也越界。\\n  related_experiments: []\\n  depends_on: []\\n- id: D006\\n  date: 2026-05-12 17:24 UTC\\n  summary: P2b pass criteria 调整：recall@5→recall@1，pool_size 26→50+，阈值 ≥2pp 不变\\n  rationale: Eval v2 (pool_size=26) 显示 random recall@5 已达 98.4-99.2%，原标准\\\"dataflow\\n    recall@5 > random ≥2pp\\\"数学上几乎不可能达标（天花板仅 0.8-1.6pp 空间）。recall@1 有更大区分度（random mean\\n    93.97%），且是更严格的排序指标。同时扩大 pool_size 至 50+ 使 recall@5/10 也获得有效梯度。新标准：dataflow_aware\\n    recall@1 > random recall@1 ≥2pp in ≥2/3 seeds，pool_size=50。\\n  related_experiments:\\n  - exp_id: mvp_p2b_contrastive_training\\n    role: trigger\\n    result: random recall@1 mean=0.940, emb_dist recall@1=0.669 at pool=26; recall@5\\n      ceiling\\n  depends_on:\\n  - D002\\n- id: D007\\n  date: 2026-05-12 19:52 UTC\\n  summary: MVP P2b dataflow 策略不可验证：connected⊆gold 导致数据相同。决定：50-repo 规模验证 + Scheme\\n    B 备份\\n  rationale: 修复 build_p2b_data.py 后重新生成数据，train_dataflow.jsonl 仍与 train_embedding.jsonl\\n    完全相同。根因：8 个 MVP repos 中 dataflow 连接文件全部是 gold 文件的子集（connected-but-not-gold = 0），non_pos\\n    过滤无差异。这不是方法缺陷而是规模问题——小 repo 紧耦合，2-hop 连接集≈gold 集。P1（Fisher p=1.54e-7）和 P2a（AUC=0.78）仍有效，说明\\n    dataflow connectivity 有信号，只是 MVP 规模不足以分离 connected-but-not-gold 子集。决策：(1) 立即跑\\n    50-repo 样本的 overlap 统计（CPU, ~2-4h），确认大规模下 connected⊃gold；(2) 并行准备 Scheme B（distance-weighted\\n    negatives）作为 pivot 备选；(3) overlap>20% 实例有 connected≠gold → 进入全量 M1 提取；overlap≈100%\\n    → pivot to Scheme B。\\n  related_experiments:\\n  - exp_id: mvp_p2b_contrastive_training\\n    role: trigger\\n    result: dataflow≡embedding 因 connected⊆gold\\n  depends_on:\\n  - D006\\n  - D004\\n- id: D008\\n  date: 2026-05-12 20:38 UTC\\n  summary: MVP 条件性通过：P1+P2a PASS，P2b dataflow 在 MVP 规模不可测但 50-repo 规模验证确认方法可行（Z=40.8%）。进入\\n    research 阶段。\\n  rationale: MVP 三阶段结果：P1 PASS（timeout 0%, Fisher p=1.54e-7, 75% instance recall）；P2a\\n    PASS（AUC 0.78, BM25 系数为负）；P2b 部分有效——random>>embedding（-27pp recall@1 at pool=26,\\n    -3.7pp at pool=50）确认 naive hard negatives 有害，但 dataflow vs random 因 connected⊆gold\\n    无法在 8 repos 上区分。50-repo 规模验证 Z=40.8%（中型 repo 55.7%），timeout 4%，确认方法在全量数据上可行。Kill\\n    criteria 均未触发。P2b dataflow 对比将在 M2 全量训练中完成。\\n  related_experiments:\\n  - exp_id: mvp_p1_codeql_feasibility\\n    role: evidence\\n    result: PASS\\n  - exp_id: mvp_p2a_linear_proxy\\n    role: evidence\\n    result: PASS\\n  - exp_id: mvp_p2b_contrastive_training\\n    role: evidence\\n    result: partial - random>>emb confirmed, dataflow untestable at MVP scale\\n  depends_on:\\n  - D007\\n  - D006\\n  - D004\\n- id: D009\\n  date: 2026-05-12 22:04 UTC\\n  summary: Dream 审稿完成：best=Weak Accept, median=Weak Reject, worst=Reject。批准 P0 启动，但\\n    plan 需增补 5 个 dream-derived 实验\\n  rationale: 三档共识问题：(1) 单编码器无法支撑 generality claim，需加 StarCoder/CodeBERT；(2) static\\n    vs dynamic embedding mining 是潜在 confound；(3) τ=0.05 可能 regime-specific；(4) SWE-bench\\n    +2pp 需 bootstrap CI；(5) abstract \\\"complementary\\\" 需降调。关键风险变量是 M1 的 Z%：≥35% best\\n    framing 成立，20-35% pivot 到 Claim 2 headline，<20% 需重大调整。已在 experiment_plan.yaml\\n    增加 plan_013-017（+35h GPU），paper_framing.md 增加 contingency framing。P0 实验（M1 已在跑）可继续，不需\\n    re-dream。\\n  related_experiments:\\n  - exp_id: dream_20260512T204322\\n    role: dream_simulate\\n    result: best=WA, median=WR, worst=R\\n  depends_on:\\n  - D008\\n- id: D010\\n  date: 2026-05-12 22:09 UTC\\n  summary: plan_013 (second encoder) 从 P1 升级至 P0，headline template 降调修复\\n  rationale: Reviewer 指出 single encoder 是 best→accept 的关键区分因素，在 best-R1-W1 和 median-R2-W5\\n    两档都出现。P1 排期可能导致论文缺少 generality 证据而被 WR。升级后 M2 完成即可并行启动 plan_013。同时修复 headline\\n    template \\\"cannot recover\\\" → \\\"complementary signal not captured by\\\"。\\n  related_experiments:\\n  - exp_id: plan_013\\n    role: priority_upgrade\\n    result: P1→P0\\n  depends_on:\\n  - D009\\n- id: D011\\n  date: 2026-05-13 01:38 UTC\\n  summary: Z%=74.0% 确认 Best Framing — Claim 1 为 headline，批准 M2 早期训练\\n  rationale: M1 部分数据（24/222 repos, 5128 instances）Z%=74.0%，远超 ≥35% 阈值。对比 D007 的 40.8%（50\\n    SWE-bench repos），SWE-Smith 数据集跨文件依赖密度更高。Best framing 成立：Claim 1 (\\\"structure-grounded\\n    negatives outperform\\\") 为 headline。批准在当前 5K instances 上做 M2 早期训练 pilot（3 strategies\\n    × 1 seed），利用 cuda:4 空闲期获取早期信号，不等全量 M1（还需 ~46h）。磁盘已清理至 61GB free (64%)，足够训练。\\n  related_experiments:\\n  - exp_id: m1_extraction\\n    role: data_source\\n    result: Z%=74.0% at 24/222 repos\\n  - exp_id: d007_50repo_overlap\\n    role: baseline\\n    result: Z%=40.8% on SWE-bench 50 repos\\n  depends_on:\\n  - D009\\n  - D010\\n- id: D012\\n  date: 2026-05-13 02:11 UTC\\n  summary: Kill m2_early_pilot_v3 (PID 897752) — 第二次 GPU 越界 (cuda:0)\\n  rationale: Reviewer 发现 m2_early_pilot_v3 在 cuda:0 运行（PID 897752, 17100 MiB），项目仅分配\\n    cuda:4。这是第二次 GPU 越界（第一次 D005 在 GPU 5）。立即 kill 并标记 killed。同时 m2_early_pilot_v2\\n    因 wandb API key error 已崩溃标记 FAILED。当前唯一合法训练为 PID 795791 (m2_early_pilot, cuda:4)。要求\\n    Agent 排查越界原因并确保后续脚本强制 CUDA_VISIBLE_DEVICES=4。\\n  related_experiments:\\n  - exp_id: m2_early_pilot_v3\\n    role: violated\\n    result: killed - GPU 越界 cuda:0\\n  - exp_id: m2_early_pilot_v2\\n    role: failed\\n    result: wandb API key error\\n  - exp_id: m2_early_pilot\\n    role: active\\n    result: PID 795791 on cuda:4, running\\n  depends_on:\\n  - D011\\n- id: D013\\n  date: 2026-05-13 02:50 UTC\\n  summary: 服务器迁移：cqa1-21977 cuda:4 → bjb1-42106 cuda:0/1 (RTX PRO 6000 96GB×2)\\n  rationale: Manager 分配独立服务器 bjb1-42106（2x RTX PRO 6000 96GB）。迁移策略：(1) M1 提取继续在 cqa1-21977\\n    CPU 上完成（不中断），(2) 新服务器立即搭建环境+同步代码+下载模型，(3) M2 early pilot 在 cqa1-21977 cuda:4 跑完后所有\\n    GPU 工作转到新服务器，(4) 通知 Manager 释放 cuda:4。RTX PRO 6000 96GB 彻底解决 M3a VRAM 问题（Qwen3.6-27B\\n    不再需要 fallback），2 卡可并行 M2 全量 + plan_013。\\n  related_experiments:\\n  - exp_id: m2_early_pilot\\n    role: in_progress\\n    result: finishing on cqa1-21977 cuda:4\\n  - exp_id: m1_extraction\\n    role: in_progress\\n    result: CPU only, stays on cqa1-21977\\n  depends_on:\\n  - D011\\n- id: D014\\n  date: 2026-05-13 04:44 UTC\\n  summary: Kill m2_early_pilot (PID 795791) — 过拟合+卡死，bjb1 m2_embed_verify 取代\\n  rationale: m2_early_pilot 在 cqa1 cuda:4 上仅完成 random 策略（best val_loss=0.5879 at step\\n    1500，之后持续过拟合到 0.728）。进程在 step 4000 卡死 45+ min。OOM 干扰（另一进程在同 GPU 启动）。embedding_distance\\n    和 dataflow_aware 策略未启动。bjb1 上的 m2_embed_verify 使用 true embedding mining + 更大参数（negatives=7,\\n    seq_len=2048, batch=8）+ eval bug fix，将完全取代此 pilot。通知 Manager 释放 cqa1 cuda:4。\\n  related_experiments:\\n  - exp_id: m2_early_pilot\\n    role: killed\\n    result: random best val_loss=0.5879, overfitting after step 1500\\n  - exp_id: m2_embed_verify\\n    role: replacement\\n    result: preparing on bjb1 cuda:1\\n  depends_on:\\n  - D011\\n  - D013\\n- id: D015\\n  date: 2026-05-13 11:43 UTC\\n  summary: 全量 Z%=78.0%（条件）确认 Best Framing；Coverage 34.3% 需论文讨论\\n  rationale: 全量 M1（123/131 repos, 44,173 instances）统计：15,153 instances 有结构数据（34.3%），其中\\n    11,825 有 connected-but-not-gold 文件（条件 Z%=78.0%，高于 pilot 72.5%）。条件 Z% 远超 35% 阈值，Best\\n    Framing（Claim 1 as headline）完全成立。但 Coverage 仅 34.3%——65.7% instances CodeQL/Beniget\\n    未产出结构连接，论文需讨论此局限性并限定 claim 范围为\\\"有结构数据的 instances\\\"。\\n  related_experiments:\\n  - exp_id: m1_extraction\\n    role: data_source\\n    result: 123/131 repos, 44173 instances, 15897 structural\\n  - exp_id: plan_006_scalability\\n    role: prior_pilot\\n    result: pilot Z%=72.5% on 29 repos\\n  depends_on:\\n  - D011\\n- id: D016\\n  date: 2026-05-13 15:24 UTC\\n  summary: 'Reviewer Critical: m2_embed_verify 和 plan_013_starcoder 实际已完成全部 3 策略，registry\\n    错误标记为 failed'\\n  rationale: Reviewer 直接从服务器日志验证：两个实验的 dataflow 策略均已完成（\\\"All 3 strategies completed\\\"），EXIT_CODE\\n    异常发生在训练完成之后（wrapper 脚本问题）。关键数据：(1) Qwen dataflow peak R@1=0.5584 (+2.27pp vs random)，支撑\\n    Claim 1；(2) StarCoder dataflow R@1=0.4869 < random 0.4922，encoder-agnostic claim\\n    受挑战；(3) 两个编码器的 dataflow 策略均严重过拟合（train loss→0）。已派 Agent 紧急修正 registry + 收集完整 metrics\\n    + 验证 StarCoder random 数据来源。方向决策待 Agent 汇报验证数据后确定。\\n  related_experiments:\\n  - exp_id: m2_embed_verify\\n    role: primary\\n    result: 实际完成（3 strategies all done），Qwen dataflow peak R@1=0.5584\\n  - exp_id: plan_013_starcoder\\n    role: primary\\n    result: 实际完成（3 strategies all done），StarCoder dataflow R@1=0.4869 < random 0.4922\\n  depends_on: []\\n- id: D017\\n  date: 2026-05-13 16:03 UTC\\n  summary: Pilot 结果验证完成：embedding > random 跨编码器一致；dataflow 需按两种 checkpoint 标准报告；Claim\\n    2 需修订\\n  rationale: 'Reviewer 验证 18 个指标全部精确匹配。核心发现：(1) embedding > random 在 Qwen (+2.0pp)\\n    和 StarCoder (+1.6pp) 上一致，是最稳健结论；(2) dataflow 排名取决于 checkpoint 选择——按 val_loss:\\n    embedding > dataflow > random (Qwen)，按 peak R@1: dataflow > embedding > random\\n    (Qwen)；(3) StarCoder dataflow final eval 追平 embedding (0.5078=0.5078)，\\\"embedding\\n    consistently beats dataflow\\\" 不成立；(4) Claim 2 (\\\"embedding harms\\\") 在 true embedding\\n    mining 下不复现，仅在 MVP BM25 proxy 下成立。全量 M2 训练需报告两种 checkpoint 标准下的结果，避免 cherry-picking\\n    质疑。Paper framing 修订延后至全量 M2 结果出来后。'\\n  related_experiments:\\n  - exp_id: m2_embed_verify\\n    role: primary\\n    result: 'Qwen: embedding(0.5557) > dataflow(0.5436) > random(0.5357) by val_loss;\\n      dataflow peak(0.5584) > embedding(0.5557) by R@1'\\n  - exp_id: plan_013_starcoder\\n    role: primary\\n    result: 'StarCoder: embedding(0.5078) > random(0.4922) > dataflow(0.4869) by val_loss;\\n      dataflow final(0.5078) = embedding'\\n  depends_on:\\n  - D016\\n- id: D018\\n  date: 2026-05-13 16:04 UTC\\n  summary: 不做预判性 framing pivot，full M2 (18 runs) 是 go/no-go 唯一判据；双 checkpoint 标准；准备\\n    B/C 两条后备路线\\n  rationale: Pilot 仅 24 repos / 1 seed，<2pp delta 统计功效不足以支持强 claim 或否决原假设。Full M2\\n    (131 repos × 3 strategies × 3 seeds × 2 encoders = 18 runs) 提供 3-seed 统计功效，是唯一可信判据。不选\\n    Agent 提议的 A/B/C 任何一个——过早锁定叙事会限制后续解读空间。数据构建已在进行，不浪费时间在 framing 讨论上。Full M2 结果出来后根据实际数据\\n    pattern 决定：(a) dataflow 跨编码器一致 > random → 原 framing 修正后可用；(b) dataflow 不一致但 embedding\\n    一致 → 方案 B 或 C；(c) 所有差异不显著 → 需要更大规模实验或 pivot。同时要求 dual checkpoint (best-val-loss\\n    + best-R@1) 和 3-seed CI 确保结果可信。\\n  related_experiments:\\n  - exp_id: m2_embed_verify\\n    role: evidence\\n    result: pilot underpowered (1 seed, 24 repos)\\n  - exp_id: plan_013_starcoder\\n    role: evidence\\n    result: pilot underpowered (1 seed, 24 repos)\\n  depends_on:\\n  - D017\\n- id: D019\\n  date: 2026-05-13 18:08 UTC\\n  summary: D018 补充：Full M2 go/no-go 量化阈值 + 统计检验方案\\n  rationale: 'Reviewer 指出 D018 缺量化阈值，go/no-go 判据需在结果出来前明确，避免事后 rationalization。\\n\\n\\n    **统计方法**：每个 encoder 3 seeds 的 R@1 (best-by-val-loss checkpoint) 做 paired difference，bootstrap\\n    95% CI + paired t-test (p<0.05)。同时报告 best-by-R@1 checkpoint 结果作为透明度补充。\\n\\n\\n    **Go/No-Go 阈值**：\\n\\n    (A) Go — 原 framing 可用：dataflow > random 的 95% CI 在两个 encoder 上均 > 0\\n\\n    (B) Conditional Go — 修正 framing：dataflow > random 在至少一个 encoder 上 CI > 0，另一个 CI\\n    含 0（差异不显著）\\n\\n    (C) No-Go for Claim 1：dataflow ≤ random 在两个 encoder 上 CI 均含 0 或为负 → Claim 1 失效，pivot\\n    到 \\\"mining strategy × architecture\\\" 分析论文\\n\\n\\n    **Claim 2 判据**：若 full M2 显示 embedding > random 且 CI > 0 → 原 Claim 2 (\\\"embedding\\n    harms\\\") 被否定。新 Claim 2 候选：\\\"true embedding mining helps, but BM25 proxy harms\\\" 或\\n    \\\"hard negative mining method matters more than hard negative source\\\"\\n\\n\\n    **跨 encoder 一致性规则**：\\n\\n    - 同方向同显著 → 强泛化 claim\\n\\n    - 同方向不同显著 → 条件 claim + architecture discussion\\n\\n    - 反方向 → Claim 1 原形式被拒，需 conditional reframe\\n\\n\\n    阈值在 full M2 结果出来前锁定，不允许事后修改。'\\n  related_experiments:\\n  - exp_id: m2_full_qwen\\n    role: primary\\n    result: RUNNING - random_s42 in progress\\n  - exp_id: m2_full_starcoder\\n    role: primary\\n    result: RUNNING - data build phase\\n  depends_on:\\n  - D018\\n- id: D020\\n  date: 2026-05-13 18:10 UTC\\n  summary: D019 补充：Claim 2 完整判定矩阵 + n=3 功效限制声明\\n  rationale: 'Reviewer 指出 D019 的 Claim 2 阈值不完整 + n=3 统计功效天然受限。补充如下：\\n\\n\\n    **Claim 2 完整判定矩阵**（3 seeds, paired bootstrap 95% CI）：\\n\\n    (i) random > embedding CI>0 → Claim 2 confirmed（embedding harms，与 MVP 一致）\\n\\n    (ii) embedding > random CI>0 → Claim 2 falsified（true embedding mining helps，需\\n    reframe）\\n\\n    (iii) CI 含 0 → inconclusive（效应存在但检测不到或确实无差异，论文报告为 \\\"no significant difference\\\"\\n    + 报告 effect size）\\n\\n\\n    **n=3 功效限制**（显式承认，不修改阈值）：\\n\\n    - df=2 时 t 临界值 4.303，pilot 级别差异（<2pp）极难达到 p<0.05\\n\\n    - Bootstrap n=3 仅 27 种重采样，CI 估计粗糙\\n\\n    - 阈值框架偏向 No-Go（Type II error 高）\\n\\n    - 若结果落入 (C) No-Go，论文 Discussion 必须讨论功效限制，不能简单声明 \\\"dataflow 无效\\\"\\n\\n    - 这是算力约束下的合理选择，不改阈值，但明确风险\\n\\n\\n    **plan_014 排期**：Full M2 完成后优先启动 plan_014（temperature ablation, ~10h）——无论 Claim\\n    2 reframe 成哪个方向，temperature regime-specificity 都需要回答。'\\n  related_experiments:\\n  - exp_id: m2_full_qwen\\n    role: primary\\n    result: RUNNING\\n  - exp_id: m2_full_starcoder\\n    role: primary\\n    result: RUNNING\\n  depends_on:\\n  - D019\\n- id: D021\\n  date: 2026-05-13 19:10 UTC\\n  summary: Negative difficulty 分析揭示 encoder capacity 差异是 dataflow 效果不一致的根因\\n  rationale: '预训练模型 cosine similarity 分析显示：Qwen pretrained embeddings 分辨力弱（random\\n    cosine sim 0.899），StarCoder 分辨力强（random cosine sim 0.553）。Dataflow negatives 在两个模型上都比\\n    random 更难（higher sim），说明方法设计正确。但 StarCoder 已经\\\"懂\\\"结构差异（所有策略 sim 都低），额外训练信号边际收益小。这解释了\\n    pilot 中 StarCoder dataflow < random 的现象：不是方法问题，是 encoder 已有足够 capacity。\\n\\n\\n    论文价值：(1) 从 negative result 中提取 mechanistic explanation；(2) 定义 method applicability\\n    condition：\\\"structure-grounded negatives benefit most when pretrained encoder has\\n    limited structural separability\\\"；(3) 产出论文级图表（Figure: Negative Difficulty Distributions）；(4)\\n    无论 full M2 落入 A/B/C，这个分析都增加论文深度。不修改 go/no-go 阈值，但丰富解读框架。'\\n  related_experiments:\\n  - exp_id: m2_embed_verify\\n    role: context\\n    result: 'Qwen: dataflow > random (+0.8~2.3pp)'\\n  - exp_id: plan_013_starcoder\\n    role: context\\n    result: 'StarCoder: dataflow < random (-0.5pp), explained by high pretrained separability'\\n  depends_on:\\n  - D018\\n  - D019\\n- id: D022\\n  date: 2026-05-13 19:25 UTC\\n  summary: M1 28K instances 可恢复（运行时故障非数据问题）；当前 M2 继续，并行后台重跑 M1 提取\\n  rationale: 'Fuzzy match 抽查 10/10 发现 buggy_file 全部存在——28,276 个 \\\"error\\\" 是 CodeQL 并行提取时的运行时故障（磁盘/存储瞬态），不是\\n    SWE-smith 数据质量问题。训练数据潜在从 15,897 → ~44,173（2.8x）。\\n\\n\\n    决策：不中断当前 M2 训练 + 并行后台重跑 M1 提取。理由：\\n\\n    (1) 当前 M2 已在双卡运行，中断重来延期 3-7 天超出 DDL\\n\\n    (2) M1 重提取是 CPU 工作，可在 bjb1-42106 后台运行不影响 GPU 训练\\n\\n    (3) 如果当前 M2 结果落入 (C) No-Go 或 effect size 太小，扩展数据集是 natural next step\\n\\n    (4) 2.8x 数据量可能显著缓解 dataflow 过拟合问题（D021 中的核心风险）\\n\\n\\n    Claim 3 叙事需修正：\\\"64% failure 是上游数据问题\\\" → \\\"64% 是运行时提取故障，CodeQL 本身在有效输入上 100% 成功，可通过重跑恢复\\\"。这是\\n    engineering limitation with clear fix，不是方法局限。'\\n  related_experiments:\\n  - exp_id: m1_extraction\\n    role: primary\\n    result: 28,276 instances recoverable - runtime failure, not data quality\\n  - exp_id: plan_006_scalability\\n    role: affected\\n    result: 'error classification needs correction: buggy_file_not_found was misattributed'\\n  depends_on:\\n  - D018\\n  - D019\\n- id: D023\\n  date: 2026-05-13 19:43 UTC\\n  summary: Kill M1 重提取：bjb1 CodeQL 查询 100% 失败，D022 前提不成立需诊断后重新评估\\n  rationale: Reviewer CRITICAL 发现 bjb1-42106 上 CodeQL call_graph.ql 查询全部 exit status\\n    2，317/325 行失败，零有效结构数据产出。原 M1 在 cqa1-21977 成功，迁移后 CodeQL 版本/QL pack 可能不兼容。立即 kill\\n    进程释放 CPU/RAM，诊断 CodeQL 配置后决定修复或换服务器。\\n  related_experiments:\\n  - exp_id: m1_reextract\\n    role: subject\\n    result: killed - CodeQL incompatible on bjb1\\n  depends_on:\\n  - D022\\n- id: D024\\n  date: 2026-05-14 00:49 UTC\\n  summary: 'Major paper framing rewrite: drop falsified \\\"embedding harms\\\" claim, pivot\\n    to \\\"systematic analysis + mechanistic insight\\\" narrative'\\n  rationale: 'Reviewer deep assessment confirmed Claim 2 (\\\"embedding actively harms\\\",\\n    -27pp) was built on BM25-proxy mislabeled as embedding-distance in MVP. D017 proved\\n    true embedding mining helps (+1.6-2.0pp). New framing: (1) embedding universally\\n    helps (corrects misconception), (2) dataflow conditionally helps (mediated by\\n    representation saturation), (3) CodeQL scalable. This is a stronger, more honest\\n    paper type for EMNLP — empirical analysis with mechanistic depth rather than false\\n    \\\"our method beats all\\\" claim.'\\n  related_experiments:\\n  - exp_id: m2_embed_verify\\n    role: evidence\\n    result: embedding > random confirmed for both encoders\\n  - exp_id: plan_013_starcoder\\n    role: evidence\\n    result: dataflow helps Qwen only, not StarCoder — conditional benefit\\n  - exp_id: neg_difficulty_analysis\\n    role: evidence\\n    result: pos_sim saturation explains strategy-encoder interaction\\n  depends_on: []\\n- id: D025\\n  date: 2026-05-14 01:01 UTC\\n  summary: Plan_014 temperature ablation 缩减为 2 strategies × 3τ × 2 epochs = 6 runs\\n    (~70h)，deadline 可达\\n  rationale: 原方案 9 runs × 3 epochs = 157h GPU，超出 May 25 ARR 截稿。缩减理由：(1) 回答 Dream reviewer\\n    的 regime-specificity concern 只需证明 embedding vs random 的相对优势跨 τ 一致，不需要 3 策略全跑；(2)\\n    M2 和 pilot 均显示 epoch 3 过拟合无收益，2 epochs 足够；(3) τ=0.07 已由 M2 覆盖，只需 {0.05, 0.1, 0.2}。6\\n    runs × ~11.7h = ~70h → 双卡并行 35h wall time，M2 完成后 ~1.5 天可跑完。Dataflow strategy 的\\n    τ ablation 降为 P2，时间充裕再补。\\n  related_experiments:\\n  - exp_id: m2_full_qwen\\n    role: evidence\\n    result: step 1000 best, epoch 3 overfitting → 2 epochs sufficient\\n  - exp_id: plan_014\\n    role: target\\n    result: budget revised from 10h to 70h, scope from 9 to 6 runs\\n  depends_on:\\n  - D024\\n- id: D026\\n  date: 2026-05-14 02:56 UTC\\n  summary: Qwen eval@2000 确认过拟合，后续 M2 runs 从 3 epochs 减至 2 epochs\\n  rationale: 'eval@2000: val_loss=0.5162, R@1=0.5228（与 @1500 持平，未恢复）。Best 锁定 step\\n    1000 (epoch 1 中段)。train_loss=0.04 vs val_loss=0.52，gap 持续扩大。模式与 pilot 一致（best\\n    at ~25% training）。当前 s42 保留 3 epochs 完整跑完（提供 full overfitting curve 数据），后续 8 runs/encoder\\n    设 max_epochs=2。节省 ~48h/GPU，M2 完成时间从 ~May 20-21 提前到 ~May 18-19。'\\n  related_experiments:\\n  - exp_id: m2_full_qwen\\n    role: evidence\\n    result: eval@2000 R@1=0.5228 flat, overfitting confirmed\\n  - exp_id: m2_full_starcoder\\n    role: pending\\n    result: eval@1000 still improving, apply 2-epoch precaution for subsequent seeds\\n  depends_on:\\n  - D025\\n- id: D027\\n  date: 2026-05-14 08:13 UTC\\n  summary: M2 剩余 runs 加 early stopping (patience=2 evals)，加速关键路径\\n  rationale: Reviewer 计算 M2 全 18 runs 需 ~5.5 天（StarCoder 瓶颈 ~133h）。两个编码器 best checkpoint\\n    均在 step 1000，之后 val_loss 持续上升。加 early stopping（patience=2，即连续 2 次 eval@500 无改善即停）预计在\\n    step 2000 左右停止（vs 2828 full 2-epoch），节省 ~30% 时间（~1.5 天），M2 从 May 19.5 提前到 ~May\\n    18。关键路径 May 25 ARR 余量从 5 天增至 7 天。风险低：仅影响未启动的 runs，不改已跑数据。\\n  related_experiments:\\n  - exp_id: m2_full_qwen\\n    role: target\\n    result: running, best@1000, overfitting confirmed\\n  - exp_id: m2_full_starcoder\\n    role: target\\n    result: running, best@1000, overfitting confirmed\\n  depends_on:\\n  - D026\\n- id: D028\\n  date: 2026-05-14 11:09 UTC\\n  summary: Claim 2 降级待定：M2 full 结果决定 \\\"conditional benefit\\\" 是独立 claim 还是降为 observation\\n  rationale: Reviewer 覆盖率审查指出 Claim 2 最薄弱：n=2 encoders 交互效应无统计功效，neg_difficulty 是描述性非实验性证据。建议降为\\n    \\\"observation + mechanistic hypothesis\\\"。决策延迟到 M2 full 18 runs 完成后：若 Qwen dataflow>random\\n    p<0.05 则保持 conditional claim；否则降级为 observation。\\n  related_experiments:\\n  - exp_id: m2_embed_verify\\n    role: Qwen pilot positive\\n    result: dataflow > random +0.8pp val_loss\\n  - exp_id: plan_013_starcoder\\n    role: StarCoder pilot negative\\n    result: dataflow < random -0.5pp\\n  - exp_id: m2_full_qwen\\n    role: go/no-go for claim strength\\n    result: RUNNING\\n  - exp_id: m2_full_starcoder\\n    role: encoder generality test\\n    result: RUNNING\\n  depends_on:\\n  - D018\\n  - D019\\n- id: D029\\n  date: 2026-05-14 16:23 UTC\\n  summary: Dream full review 完成：7 条三档一致结构性问题确认，BM25 baseline 升为 P0，pool size sensitivity\\n    新增 plan_019\\n  rationale: 'dream_20260514T075732 (full review mode) 三档评分: Best 4/6 WA, Median 3/6\\n    WR, Worst 3/6 WR。跨三档一致的结构性问题 7 条：(1) 缺 BM25 baseline 是 #1 共识——论文核心叙事（纠正 CoCoHaNeRe）无实证支撑，已加\\n    plan_018 P0；(2) N=2 编码器限制——保持 honest framing，无法加更多编码器；(3) StarCoder 误标为 encoder-decoder——已修正为\\n    decoder-only；(4) RepoBench-R 无 CIs——plan_004 已标注多 seed 要求；(5) Pool=50 太小——新增 plan_019\\n    P1；(6) 34% structural coverage 未分层——plan_005 已扩展；(7) Checkpoint selection criterion\\n    未指定——写作时明确。观察项：effect sizes 太小（等 M2 真实数据）、overfitting 分析（提取现有训练 log）。忽略项：broken\\n    bibliography（dream artifact）、0 figures（dream artifact）。评分顺序正常（best≥median=worst）。下一步：派\\n    Agent 准备 BM25 mining（CPU），M2 完成后立即执行 plan_018 training phase。'\\n  related_experiments:\\n  - exp_id: plan_018\\n    role: new P0 experiment added\\n    result: planned\\n  - exp_id: plan_019\\n    role: new P1 experiment added\\n    result: planned\\n  - exp_id: plan_004\\n    role: updated with multi-seed CI requirement\\n    result: planned\\n  - exp_id: plan_005\\n    role: extended with structural coverage stratification\\n    result: planned\\n  depends_on:\\n  - D024\\n  - D028\\n- id: D030\\n  date: 2026-05-14 16:23 UTC\\n  summary: Dream dream_20260514T075732 分析完成：7 项确认行动 + 5 项观察项 + re-dream 后批准新 P0\\n  rationale: 'Dream full review (2 Reviewers roundtable) 三档评分: Best=4/6(WA), Median=3/6(WR),\\n    Worst=3/6(WR)。Median 未达 borderline，需修复结构性问题后 re-dream。\\n\\n\\n    **三档一致的结构性问题（7 项确认行动）：**\\n\\n    1. [EXP] 缺 BM25 negative baseline — 论文核心 narrative (correcting CoCoHaNeRe) 无实证。加\\n    plan_018, P0, Phase1 CPU 立即启动\\n\\n    2. [EXP] RepoBench-R 缺 CIs — plan_004 增加多 seed 评估\\n\\n    3. [EXP] Pool size 50 过小 — 加 plan_019 sensitivity analysis\\n\\n    4. [EXP] 34% structural coverage 未分层 — 扩展 plan_005 加 structural-available vs fallback\\n    stratum + neg_difficulty quartile\\n\\n    5. [FRAMING] N=2 encoders → 降级为 \\\"observation + hypothesis\\\"，非 validated mechanism\\n\\n    6. [FRAMING] StarCoder 架构 → 修正为 \\\"decoder-only\\\"（已改）\\n\\n    7. [FRAMING] Claim 3 (CodeQL pipeline) → 降为 supporting methodology（已改）\\n\\n\\n    **观察项（等真实数据）：**\\n\\n    1. Effect sizes marginal [M][W] — 等 M2 full 统计结果\\n\\n    2. Dataflow claim strength [M][W] — D028 已 plan\\n\\n    3. \\\"Scaling law\\\" [W] → 用 \\\"trend\\\" + CIs\\n\\n    4. Temperature ablation contradiction [W] — plan_014 结果决定\\n\\n    5. Zero method contribution [M][W] — framing 强度决定\\n\\n\\n    **Re-dream 要求：** framing + plan 修改完成后需 re-dream，best ≥ WA 且 median ≥ borderline\\n    后才批准新 P0 实验。已在跑的实验继续。'\\n  related_experiments:\\n  - exp_id: dream_20260514T075732\\n    role: trigger\\n    result: best=4/6 WA, median=3/6 WR, worst=3/6 WR\\n  - exp_id: plan_018\\n    role: new_from_dream\\n    result: planned — BM25 baseline\\n  - exp_id: plan_019\\n    role: new_from_dream\\n    result: planned — pool size sensitivity\\n  depends_on:\\n  - D028\\n  - D024\\n- id: D031\\n  date: 2026-05-14 17:02 UTC\\n  summary: 'BM25 Phase 1 完成: 87% overlap with embedding_distance，预示论文叙事可能从 \\\"纠正误标\\\"\\n    转向 \\\"受控对比证明 hard negatives 普遍有效\\\"'\\n  rationale: 'plan_018 Phase 1 (CPU) 完成。3 seeds BM25 negatives 已生成，与 embedding_distance\\n    negatives 重叠率高达 87.1%。小 repo 候选池 ≤50 导致所有策略完全重合，BM25 differentiation 主要在大 repo\\n    上体现。\\n\\n\\n    Phase 2 训练结果预期 3 种可能：\\n\\n    A) BM25 harm (BM25 << random) → 原叙事成立（\\\"BM25 proxy 导致 CoCoHaNeRe 错误结论\\\"）\\n\\n    B) BM25 ≈ random → contingency per D030（叙事降为 \\\"systematic comparison\\\"）\\n\\n    C) BM25 ≈ embedding_distance (87% overlap 强烈预示) → 叙事升级为\\\"BM25 和 embedding mining\\n    高度重叠，两者在受控环境下都优于 random；CoCoHaNeRe 的负面结论源于实验控制不足而非 BM25-proxy 本身\\\"\\n\\n\\n    Scenario C 实际上比 A 更强——我们提供的不只是标签纠正，而是受控对比 + 叙事升级。\\n\\n\\n    附带决策：plan_015 暂缓至 camera-ready（44h 超预算 + DDL 紧），Limitations 中承认 static vs dynamic\\n    confound。'\\n  related_experiments:\\n  - exp_id: plan_018\\n    role: phase1_complete\\n    result: BM25 data ready, 87% overlap with embedding_distance\\n  - exp_id: plan_015\\n    role: deferred\\n    result: design complete, execution deferred to camera-ready\\n  depends_on:\\n  - D030\\n- id: D032\\n  date: 2026-05-14 17:02 UTC\\n  summary: plan_015 缩减为 1 seed × dynamic_ep (~11h)；BM25 overlap 87% 需分层验证\\n  rationale: 'plan_015 原设计 3 variants × 多 seeds = 44h，DDL May 25 前 GPU 时间不够。缩减为 dynamic_ep\\n    × 1 seed (Qwen s42) ~11h，足以排除 static vs dynamic confound。预期 dynamic ≈ static（<1pp），在\\n    Limitation 段写实验证据。\\n\\n\\n    BM25 Phase 1 完成：BM25 vs embedding overlap 87.1%。但 Agent 指出小 repo (pool ≤50) 导致所有策略\\n    negatives 重合——overlap 被拉高。已派补充分析按 repo 大小分层统计真实差异化程度。Phase 2 训练结果将决定 CoCoHaNeRe\\n    narrative 是否需要 pivot（contingency 已在 paper_framing.md）。'\\n  related_experiments:\\n  - exp_id: plan_015\\n    role: scope_reduction\\n    result: 44h→11h, 1 seed × dynamic_ep only\\n  - exp_id: plan_018\\n    role: phase1_complete\\n    result: BM25 vs embedding overlap 87.1%, 3 seeds done\\n  depends_on:\\n  - D030\\n- id: D033\\n  date: 2026-05-14 17:10 UTC\\n  summary: D031 修正：BM25 top-7 overlap 远低于 k=50 的 87%，大 repo 仅 30%，Phase 2 将有区分度\\n  rationale: '分层 Jaccard 分析（top-7, seed 42, 2920 matched queries）显示 BM25 vs embedding_distance\\n    重叠率：small=67%, medium=38%, large=30%。之前报告的 87% 是 k=50 全候选重叠，训练实际用 top-7 negatives\\n    差异大得多。\\n\\n\\n    关键修正：D031 中预判的 \\\"BM25 ≈ embedding_distance\\\" 不再成立。Phase 2 训练预期结果重新开放为三种可能（BM25 harm\\n    / neutral / help），实验区分度足够。\\n\\n\\n    方法论 flag: BM25 使用 whitespace tokenization (str.split())，不处理 camelCase/snake_case。如果\\n    BM25 表现差，tokenization 可能是 confound。论文中需标注。Reviewer 已指出。\\n\\n\\n    24% match rate 源于 BM25 mining 使用了不同 train/val split，不影响分层趋势结论但如需严格配对可重新生成。'\\n  related_experiments:\\n  - exp_id: plan_018\\n    role: phase1_analysis\\n    result: 'stratified overlap: large_repo BM25-vs-embedding=30%, BM25-vs-random=0.7%'\\n  depends_on:\\n  - D031\\n- id: D034\\n  date: 2026-05-14 17:50 UTC\\n  summary: Re-dream gate 未通过但决定继续：median=WR 由不可修复因素驱动（novelty/effect-size/n=2），override\\n    gate 推进 Phase 2\\n  rationale: 'Re-dream dream_20260514T162530 评分：Best=4/6(WA), Median=3/6(WR), Worst=3/6(WR)。与首次\\n    dream 完全一致，修复 BM25 baseline + pool size + framing 降级未改变评分。\\n\\n\\n    Gate 要求 median ≥ borderline。分析 median WR 原因：\\n\\n    1. Novelty (\\\"ANCE for code\\\") — 不可修复，是 framing 层面问题\\n\\n    2. Effect sizes (pool=200: +0.4~0.7pp) — 数据决定，不可修复\\n\\n    3. N=2 encoders — DDL 前不可加\\n\\n    4. Dataflow null — 数据已确定\\n\\n    5. Bibliography (2 citations) — dream artifact，实际论文可修\\n\\n\\n    因素 1-4 是 dream 模拟的固有限制（无论怎么改 plan，dream 想象的 median/worst 数据都会是 marginal），而非实验设计缺陷。Best\\n    case 达到 WA=4/6 并且 R1 明确给出 \\\"specify K + checkpoint criterion → 5/6\\\" 路径。\\n\\n\\n    决策：Override gate，允许 Phase 2 在 GPU 空闲时执行。理由：\\n\\n    (a) 阻塞因素为写作/scope 层面，非实验层面，更多 dream 不会改变\\n\\n    (b) Best case BM25 baseline 被评为 \\\"paper''s most clean-cut contribution\\\"\\n\\n    (c) ARR May 25 DDL 时间紧，Phase 2 是关键路径\\n\\n    (d) Writing 层面的修复（related work, specification）会在实际论文中自然解决'\\n  related_experiments:\\n  - exp_id: dream_20260514T162530\\n    role: re-dream\\n    result: best=4/6 WA, median=3/6 WR, worst=3/6 WR — unchanged from first dream\\n  - exp_id: plan_018\\n    role: gate_override\\n    result: Phase 2 approved despite gate not passing\\n  depends_on:\\n  - D030\\n  - D031\\n  - D033\\n- id: D035\\n  date: 2026-05-14 18:48 UTC\\n  summary: Claim 2 降级：从 \\\"conditional benefit beyond embedding mining\\\" 降为 \\\"exploratory\\n    observation\\\"\\n  rationale: Reviewer 覆盖率审查发现 pilot 数据不支持 \\\"beyond embedding mining\\\"——两个编码器都是 dataflow\\n    < embedding (Qwen -1.2pp, StarCoder -1.0pp)。0/3 支撑实验完成。降级为观察+机制假说，不再作为核心贡献。paper_framing.md\\n    已更新。\\n  related_experiments:\\n  - exp_id: m2_embed_verify\\n    role: evidence\\n    result: embedding > dataflow on both encoders\\n  - exp_id: plan_013_starcoder\\n    role: evidence\\n    result: 'StarCoder: embedding 0.5174 > dataflow 0.5078'\\n  depends_on:\\n  - D028\\n- id: D036\\n  date: 2026-05-14 19:10 UTC\\n  summary: M2 checkpoint 选择统一用 R@1 而非 val_loss 作为 primary criterion\\n  rationale: Reviewer 核实 s43 发现 val_loss 最优在 step 500、R@1 最优在 step 1500，两个 criterion\\n    给出不同最优点。检索任务的目标指标是 R@1，val_loss 仅反映语言建模质量，不直接对应下游检索性能。统一用 R@1 选 checkpoint 确保论文报告一致性，后续所有\\n    M2 实验沿用此标准。\\n  related_experiments:\\n  - exp_id: m2_full_qwen_continued\\n    role: 触发\\n    result: s43 val_loss best@500 vs R@1 best@1500\\n  - exp_id: m2_full_starcoder_resumed\\n    role: 同步适用\\n    result: 进行中\\n  depends_on: []\\n- id: D037\\n  date: 2026-05-14 19:13 UTC\\n  summary: 'D037: M2 checkpoint 改为只存 LoRA adapter weights，不存 merged 完整模型'\\n  rationale: 磁盘剩余 43GB，后续 18 runs 需 ~249GB checkpoint 空间。根因：LoRA rank=16 的 3B 模型存完整\\n    float16 merged weights (5.8GB/checkpoint)，但 adapter 仅 ~100MB。改为 PeftModel.save_pretrained\\n    只存 adapter，18 runs × 2 checkpoints × 100MB ≈ 3.6GB，彻底解决。同时删旧 pilot 输出 (+66GB)\\n    和 final 目录 (+11.6GB) 作为即时缓解。与 mvp_p2b_contrastive_training 磁盘满崩溃为同一 failure pattern。\\n  related_experiments:\\n  - exp_id: m2_full_qwen_continued\\n    role: 受影响\\n    result: 剩余 7 runs 将受益于 adapter-only saving\\n  - exp_id: m2_full_starcoder_resumed\\n    role: 受影响\\n    result: 剩余 7 runs 同样受益\\n  depends_on: []\\n- id: D038\\n  date: 2026-05-14 20:39 UTC\\n  summary: Plan 005 分层分析需额外控制 pool_size；dataflow richness 维度不单独做 claim\\n  rationale: Confound 分析显示 rich-dataflow 实例的候选池远大于 moderate（46-50 vs 17-37），pool_size\\n    机械性驱动 R@1 差异。控制 repo_size 后模式不消失，确认 pool_size 才是真正 confound。论文中 dataflow richness\\n    维度需 pool_size-matched 对比后才能下结论。\\n  related_experiments:\\n  - exp_id: plan_005_stratified\\n    role: evidence\\n    result: dry-run 确认 confound 存在\\n  depends_on: []\\n- id: D039\\n  date: 2026-05-14 20:40 UTC\\n  summary: 分层分析 R@1 数据无效：dry-run mock predictions，非真实模型结果。confound 分布结构(repo_size×dataflow)有效保留。\\n  rationale: Reviewer critical 审查确认：stratified_dryrun v1/v2 和 confound_analysis 的所有\\n    R@1 值均来自 dry-run mock predictions。策略排序模式和优势幅度需用 M2 真实 checkpoint 重新验证。仅 cross-tabulation\\n    分布结构（rich dataflow 99.3% 集中在 large/xlarge repos, Spearman ρ=0.077）为真实数据，可用于论文写作中声明\\n    confound 关系。plan_005_stratified 必须等 M2 真实 checkpoint 完成后执行。\\n  related_experiments:\\n  - exp_id: worker_analysis_dataflow_reposize_confound\\n    role: invalidated_analysis\\n    result: R@1 from mock data, distribution structure valid\\n  - exp_id: m2_full_qwen_continued\\n    role: dependency\\n    result: running - provides real checkpoints\\n  - exp_id: m2_full_starcoder_resumed\\n    role: dependency\\n    result: running - provides real checkpoints\\n  depends_on: []\\n- id: D040\\n  date: 2026-05-14 21:27 UTC\\n  summary: Claim 1 framing 微调：从\\\"纠正 embedding negatives 不行的误解\\\"改为\\\"挑战必须用昂贵 gradient-based\\n    方法的假设\\\"\\n  rationale: CoCoHaNeRe (ACM TOSEM 2025) 实际论点是 non-differentiable embedding negatives\\n    \\\"slow and ineffective\\\"（相对 gradient-based），并非说 embedding negatives 有害。原 Claim 1\\n    \\\"correcting misconception\\\" 措辞会被审稿人以 CoCoHaNeRe 原文反驳。新措辞\\\"simple static embedding-distance\\n    mining suffices, challenging the assumption that expensive gradient-based hard\\n    negative methods are necessary\\\"更准确、更defensible，且保留 contribution。\\n  related_experiments:\\n  - exp_id: plan_017_literature\\n    role: evidence\\n    result: CoCoHaNeRe framing conflict identified during related work expansion\\n  depends_on: []\\n\", \"total_chars\": 31588, \"truncated\": false}, \"error\": null, \"metadata\": {}}"
    }
  },
  "sourceToolAssistantUUID": "4bb89274-0b46-465b-b6f6-aaa3090d327b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "999f865e-f544-467f-b7e8-732fb33862f3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 44_

```json
{
  "type": "last-prompt",
  "leafUuid": "8997cc8c-ffda-4da9-b65c-0208d69154a5",
  "sessionId": "999f865e-f544-467f-b7e8-732fb33862f3"
}
```

---

### Runtime record

_source line 45_

```json
{
  "type": "ai-title",
  "aiTitle": "Review Claim 2 wording defensiveness",
  "sessionId": "999f865e-f544-467f-b7e8-732fb33862f3"
}
```

---

### Assistant

_source line 46 · 2026-05-15T02:00:06.000Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the material I need. Let me systematically review Claim 2 wording across all documents.

Let me compile my findings:

## paper_framing.md - Claim 2 appearances:

1. **Core Claims section (Claim 2)**:
   > **[Exploratory observation] Structure-grounded (dataflow) negatives interact with encoder representation geometry, but do not consistently outperform embedding mining.** Pilot data shows dataflow < embedding on both encoders (Qwen: -1.2pp, StarCoder: -1.0pp R@1 vs embedding). 

The saturation levels in each encoder tell an interesting story — Qwen's already-saturated representations (pos_sim > 0.98) show a smaller performance gap compared to StarCoder's healthier geometry (pos_sim ~ 0.80) — which suggests that representation maturity is what determines how well each strategy works. The difficulty margins we're seeing (+17% for Qwen, +28% for StarCoder) point to a mechanistic explanation for this interaction. Still need multi-seed validation, the stratified analysis from plan_005, and the dynamic mining controls in plan_015 before drawing firm conclusions. This stays framed as an exploratory observation with a mechanistic hypothesis rather than a confirmed finding.

   ✅ Good - clearly marked as [Exploratory observation], explicitly states "not an established finding", includes caveats about pending confirmation.

2. **Story Spine - Our contribution**

I'm noticing that structure-grounded negatives (dataflow-based) interact with how the encoder represents information, and the difficulty margin analysis gives us a mechanistic window into when and why different strategies succeed or fail — though this is still exploratory given the limited sample size.

3. **Headline result template**:

Structure-grounded negatives reveal encoder-dependent interaction patterns, where representation geometry (measured through negative difficulty) explains when different mining strategies become effective — pending confirmation across multiple seeds.

4. **Core Insight**:

The success of hard negative mining strategies hinges on the encoder's representation geometry. When the pretrained space is already saturated...

This is stated as a general finding, but I should hedge it as an exploratory observation limited by n=2.

5. **Dual-Pillar Motivation - Secondary**:

The neg_difficulty analysis (margin distribution across strategy and encoder) offers explanatory depth beyond raw empirical comparison, potentially helping practitioners reason about which strategy fits their encoder — though this predictive claim needs validation beyond two encoders.

6. **Formal Definition**:

No issues with Claim 2 wording here.

7. **Title Options**:

The primary title doesn't directly reference Claim 2, which is fine. The alternative title about static embedding negatives being sufficient is contingent on confirming the dataflow conditional benefit holds across encoders.

8. **Venue Fit**:

The contribution is fundamentally about understanding encoder-dependent patterns, not just proposing a new method.

9. **Anticipated Reviewer Concerns**:

With only two encoders, generalizability is the obvious question. I'm framing this as an interaction observation with mechanistic explanation rather than a universal principle, which acknowledges the n=2 constraint.

10. **Contingency section**:

If the dataflow benefit disappears even at full scale for Qwen, I pivot to a two-claim paper instead.

Now looking at how Claim 2 appears in the introduction draft — the third paragraph introduces it as an encoder-dependent interaction pattern where dataflow negatives don't consistently outperform embedding mining.

The language here is too assertive. Saying "reveals" and "providing a mechanistic explanation" sounds conclusive when I should be more exploratory given the limited sample. I need to add the n=2 caveat and soften the framing. The contribution statement itself does better — it explicitly marks this as an exploratory observation and includes the specific margin improvements for each encoder, but then notes that dataflow actually underperforms on both, which is the key finding I'm trying to highlight.

Looking at how this appears in the paper, I'm catching places where I've drifted toward overstating the findings. The setup section implies this is a confirmed mechanism rather than a hypothesis I'm testing. The pilot validation section is fine — it correctly notes the encoder-dependent effect. I need to be consistent about the exploratory nature throughout and make sure I'm not claiming mechanistic proof when I only have suggestive evidence from two seeds. Continuing through the discussion section, I'm noticing several places where the language overstates confidence given the limited sample size. The title "Representation Geometry as a Predictor" suggests validated predictive power that n=2 doesn't support. In the body text, phrases like "reveals" and "predicts" are too assertive—I should soften these to "suggests" or "is consistent with." The claim that this "explains" the improvement needs hedging too; "may explain" or "aligns with" would be more appropriate for exploratory findings.

The practical implication about computing pos_sim on held-out samples feels premature to present as actionable guidance from just two observations. However, I do see that later in the section I've already added an explicit caveat about the pos_sim > 0.98 threshold being derived from limited data and needing broader validation, which is good. The limitations section appropriately flags that generalization to other architectures, scales, and domains remains open, and the future work section is starting to outline what needs investigation next. Looking at how the three mining strategies compare and interact with different encoder geometries—this is the core empirical contribution. The figures then provide visual support for both claims, with Figure 4 specifically illustrating the mechanistic reasoning behind why embedding-based approaches work and how dataflow sensitivity varies by encoder.

Now I'm compiling the review findings. The main issues are scattered throughout: assertive language like "reveals" and "explains" appears without proper hedging for the exploratory claim, the "[Exploratory observation]" tag is underused, and the n=2 limitation isn't flagged consistently. Discussion section 5.2 is particularly problematic with repeated unhedged assertions, while the core insight statement has no qualification at all—though the contribution section does maintain a clear distinction between the strong claim and the exploratory one.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8997cc8c-ffda-4da9-b65c-0208d69154a5",
  "isSidechain": false,
  "requestId": "req_011Cb3XWDy9vDuoFC2xuMYPE",
  "type": "assistant",
  "uuid": "80f8d583-84af-424c-bbdc-5579c3a18637",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "999f865e-f544-467f-b7e8-732fb33862f3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019g3RePv3h4er9MzcUv8DUJ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 17017,
      "cache_read_input_tokens": 51964,
      "output_tokens": 7580,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 17017,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 7580,
          "cache_read_input_tokens": 51964,
          "cache_creation_input_tokens": 17017,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 17017
          },
          "type": "message"
        }
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

_source line 47 · 2026-05-15T02:00:06.154Z_

I have all the material. Now writing the review report.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "80f8d583-84af-424c-bbdc-5579c3a18637",
  "isSidechain": false,
  "requestId": "req_011Cb3XWDy9vDuoFC2xuMYPE",
  "type": "assistant",
  "uuid": "4dee100a-227a-473d-8690-4a65ad039e87",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "999f865e-f544-467f-b7e8-732fb33862f3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019g3RePv3h4er9MzcUv8DUJ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 17017,
      "cache_read_input_tokens": 51964,
      "output_tokens": 7580,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 17017,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 7580,
          "cache_read_input_tokens": 51964,
          "cache_creation_input_tokens": 17017,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 17017
          },
          "type": "message"
        }
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

_source line 48 · 2026-05-15T02:01:38.294Z_

<details open><summary>🔧 Tool call — Write · `toolu_01Pve9a5DxTkngf4U5TxPwFe`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/claim2_wording_review.md",
  "content": "# Claim 2 Wording Review: \"Exploratory Observation\" Consistency Audit\n\n**Date**: 2026-05-15\n**Scope**: All paper_framing.md + paper draft .md files\n**Reference decision**: D035 — Claim 2 降级为 \"exploratory observation with testable prediction\"\n\n---\n\n## Summary\n\nClaim 2 的 **[Exploratory observation]** 标签仅在 2 处出现（paper_framing.md Claim 定义 + introduction contribution list），但 body text 中有 **11 处** 使用了与 exploratory 不兼容的断言性措辞（\"reveals\", \"explains\", \"predicts\", \"shows that\"）。Discussion §5.2 是最严重的区域——标题和正文均用预测性语言，暗示 n=2 观察已构成 validated mechanism。\n\nClaim 1（strong, confirmed）与 Claim 2（exploratory）的区分在 contribution list 中清晰，但在正文中逐渐模糊，特别是 introduction 最后一段、related work §2.3、discussion §5.2。\n\n---\n\n## 逐处审查\n\n### paper_framing.md\n\n| 位置 | 当前措辞 | 强度 | 问题 |\n|------|----------|------|------|\n| Core Claims - Claim 2 | \"[Exploratory observation]...This is reported as an observation with mechanistic hypothesis, not an established finding.\" | ✅ 合适 | 明确标记+caveat |\n| Story Spine - contribution (2) | \"observe that structure-grounded (dataflow) negatives interact with encoder representation geometry and provide mechanistic analysis\" | ⚠️ 偏强 | 缺 \"exploratory\" 标签；\"provide mechanistic analysis\" 暗示已完成验证 |\n| Headline result template | \"representation geometry analysis via negative difficulty provides mechanistic explanation for when different mining strategies are effective\" | ⚠️ 偏强 | \"provides mechanistic explanation\" 对 n=2 过于断言 |\n| Core Insight | \"The effectiveness of hard negative mining strategies depends on the encoder's representation geometry.\" | ❌ 过强 | 无任何 hedge，读为 general claim，无 n=2/exploratory 标记 |\n| Dual-Pillar Motivation - Secondary | \"enabling practitioners to predict which strategy suits their encoder without exhaustive experiments\" | ❌ 过强 | 从 n=2 观察直接推出 practitioner guidance，暗示 validated predictive power |\n| Reviewer Concerns - \"Only 2 encoders\" | \"n=2 is minimum for interaction claim; we frame as observation with mechanism, not universal law\" | ✅ 合适 | 明确承认 |\n| Contingency | \"Pivot to 2-claim paper...Drop Claim 2 to analysis observation\" | ✅ 合适 | 有降级准备 |\n\n### introduction_v1.md\n\n| 位置 | 当前措辞 | 强度 | 问题 |\n|------|----------|------|------|\n| Para 3 (intro body) | \"analysis of negative difficulty margins reveals that the encoder's pretrained representation geometry...mediates which strategy is most effective, providing a mechanistic explanation for when and why\" | ⚠️ 偏强 | \"reveals\" + \"providing a mechanistic explanation\" 无 exploratory hedge；与紧接其后的 Contribution 2 的 hedging 形成矛盾 |\n| Contribution 2 | \"[Exploratory observation] We report that...This is reported as an observation with mechanistic hypothesis, pending multi-seed confirmation.\" | ✅ 合适 | 完整 hedge：标签+caveat+pending 声明 |\n\n**矛盾**：Para 3 用 \"reveals...provides mechanistic explanation\"，Contribution 2 紧接着说 \"observation with mechanistic hypothesis\"。读者会注意到措辞强度骤降。\n\n### experiments_v1.md\n\n| 位置 | 当前措辞 | 强度 | 问题 |\n|------|----------|------|------|\n| §4.1 Encoders | \"This divergence enables us to study how representation geometry mediates the effectiveness of different negative mining strategies.\" | ⚠️ 偏强 | \"mediates\" 预设因果，应为 \"may mediate\" 或 \"appears to mediate\" |\n| §4.3 Pilot (ii) | \"the dataflow-aware strategy's effectiveness is encoder-dependent—beneficial for Qwen but neutral-to-negative for StarCoder\" | ✅ 合适 | 限定在 pilot 结果描述 |\n| §4.4 Mechanistic hypothesis title | \"Mechanistic hypothesis\" | ✅ 合适 | 标题正确标记为 hypothesis |\n| §4.4 Mechanistic hypothesis body | \"When the pretrained space is saturated, the encoder has limited room...Embedding-distance negatives provide a direct optimization target...Dataflow-aware negatives...may not align with the encoder's most informative gradient direction\" | ⚠️ 偏强 | 前半段读为已确认的解释（\"the encoder has limited room\"），后半段用 \"may not align\" 有 hedge。整体偏 explanatory 而非 hypothesis |\n| §4.4 Difficulty gradient | \"The steeper relative compression for Qwen suggests that...\" | ✅ 合适 | \"suggests\" 恰当 |\n\n### discussion_v2.md (最严重)\n\n| 位置 | 当前措辞 | 强度 | 问题 |\n|------|----------|------|------|\n| §5.2 标题 | \"Representation Geometry as a Predictor of Strategy Effectiveness\" | ❌ 过强 | \"Predictor\" 暗示 validated predictive power，n=2 不支持 |\n| §5.2 首句 | \"reveals a practical insight: the pretrained encoder's representation geometry predicts whether structure-grounded negatives will provide benefit\" | ❌ 过强 | \"reveals\" + \"predicts\" 双重断言 |\n| §5.2 Qwen 解释 | \"This explains the +0.8pp R@1 improvement\" | ❌ 过强 | \"explains\" 对 n=2 correlational 观察过于因果 |\n| §5.2 practical implication | \"This interaction...has a practical implication: practitioners can compute pos_sim...\" | ⚠️ 偏强 | 从 n=2 直接给出 practitioner recipe |\n| §5.2 threshold | \"though we note this threshold is derived from two encoder observations and should be validated more broadly\" | ✅ 合适 | 明确 n=2 caveat |\n| §5.3 Limitations | \"enabling our interaction analysis—generalizing...requires further investigation\" | ✅ 合适 | 承认泛化限制 |\n| §5.4 Future Work | \"Our observation that pos_sim predicts strategy effectiveness suggests...\" | ⚠️ 偏强 | \"predicts\" 仍过强，但 \"observation...suggests\" 结构有 hedge |\n\n### related_work_v1.md\n\n| 位置 | 当前措辞 | 强度 | 问题 |\n|------|----------|------|------|\n| §2.3 末段 | \"show that the relative effectiveness of mining strategies depends on the encoder's pretrained representation geometry\" | ❌ 过强 | \"show that...depends on\" 是 confirmed finding 的措辞 |\n\n### method_v1.md\n\n| 位置 | 当前措辞 | 强度 | 问题 |\n|------|----------|------|------|\n| §3.1 | \"analyze how their effectiveness interacts with the encoder's pretrained representation geometry\" | ✅ 合适 | 描述研究行为，不做 claim |\n\n---\n\n## 统计\n\n| 强度 | 数量 | 位置 |\n|------|------|------|\n| ✅ 合适 | 11 | paper_framing (3), intro contrib (1), experiments (3), discussion (2), method (1), figure_design (1) |\n| ⚠️ 偏强 | 7 | paper_framing (2), intro para3 (1), experiments (2), discussion (2) |\n| ❌ 过强 | 5 | paper_framing Core Insight (1), paper_framing Dual-Pillar (1), discussion §5.2 (3) |\n\n---\n\n## 建议修改\n\n### 必须修改 (❌ 过强)\n\n**1. paper_framing.md - Core Insight**\n- 现在: \"The effectiveness of hard negative mining strategies depends on the encoder's representation geometry.\"\n- 建议: \"Our pilot data suggests that the effectiveness of hard negative mining strategies may depend on the encoder's representation geometry — a hypothesis derived from two encoders and requiring broader validation.\"\n\n**2. paper_framing.md - Dual-Pillar Secondary**\n- 现在: \"enabling practitioners to predict which strategy suits their encoder without exhaustive experiments\"\n- 建议: \"offering a candidate heuristic (pos_sim threshold) that, if validated on more encoders, could help practitioners select strategies without exhaustive experiments\"\n\n**3. discussion_v2.md - §5.2 标题**\n- 现在: \"Representation Geometry as a Predictor of Strategy Effectiveness\"\n- 建议: \"Representation Geometry and Strategy Effectiveness: An Exploratory Analysis\"\n\n**4. discussion_v2.md - §5.2 首句**\n- 现在: \"reveals a practical insight: the pretrained encoder's representation geometry predicts whether...\"\n- 建议: \"suggests a hypothesis worth further investigation: the pretrained encoder's representation geometry may predict whether...\"\n\n**5. discussion_v2.md - §5.2 \"explains\"**\n- 现在: \"This explains the +0.8pp R@1 improvement\"\n- 建议: \"This is consistent with the +0.8pp R@1 improvement\"\n\n**6. related_work_v1.md - §2.3**\n- 现在: \"show that the relative effectiveness of mining strategies depends on\"\n- 建议: \"observe that the relative effectiveness of mining strategies appears to depend on\"\n\n### 建议修改 (⚠️ 偏强)\n\n**7. paper_framing.md - Story Spine contribution (2)**\n- 添加 \"[exploratory]\" 标签: \"(2) [exploratory] observe that...\"\n\n**8. introduction_v1.md - Para 3**\n- \"reveals\" → \"suggests\"\n- \"providing a mechanistic explanation\" → \"providing a candidate mechanistic explanation (Section 4.4)\"\n\n**9. experiments_v1.md - §4.1 Encoders**\n- \"mediates\" → \"may mediate\"\n\n**10. experiments_v1.md - §4.4 Mechanistic hypothesis body**\n- 首句添加: \"Based on our two-encoder comparison, we hypothesize the following mechanism:\"\n\n**11. discussion_v2.md - §5.4 Future Work**\n- \"predicts\" → \"appears to correlate with\"\n\n---\n\n## Claim 1 vs Claim 2 区分度\n\n| 文档位置 | 区分清晰度 | 说明 |\n|----------|-----------|------|\n| paper_framing Contribution list | ✅ 清晰 | Claim 1 无标签 (strong), Claim 2 有 [Exploratory observation] |\n| introduction Contribution list | ✅ 清晰 | 同上，且 Claim 2 有 pending 声明 |\n| introduction body (Para 3) | ❌ 模糊 | \"central finding\" 引出 Claim 1 后直接 \"we observe\" 引出 Claim 2，无强度差异标记 |\n| experiments body | ⚠️ 部分模糊 | pilot 段落区分合理，但 §4.4 mechanistic hypothesis 读为与 §4.3 main results 同等强度 |\n| discussion | ❌ 模糊 | §5.2 标题和正文与 §5.1 (methodology) 同等断言强度 |\n| related work | ❌ 模糊 | 两个 claim 在 §2.3 末段同一句中出现，用相同强度的 \"show that\" |\n\n**建议**: Introduction Para 3 中 Claim 2 部分添加括号注: \"(an exploratory finding; see Section 4.4)\"。Discussion §5.2 开头添加一句: \"We present the following analysis as an exploratory observation from two encoders, not a validated mechanism.\"\n\n---\n\n## 审稿人攻击角度与预备 Rebuttal\n\n### 攻击 1: \"n=2 不足以支持任何 interaction claim\"\n**预期措辞**: \"The authors claim representation geometry mediates strategy effectiveness, but with only two encoders this is an anecdote, not evidence.\"\n**Rebuttal 要点**:\n- 承认 n=2 是核心限制，这正是我们标记为 exploratory observation 而非 confirmed finding 的原因\n- 但两个编码器有 meaningful variation: 不同预训练语料、不同 representation geometry (pos_sim 0.986 vs 0.799)、不同预训练目标\n- 我们提供 testable prediction: pos_sim > 0.98 时 structure-grounded negatives 更有效。这比纯 empirical 结果更有 scientific value\n- 论文主要贡献是 Claim 1 (embedding mining suffices)，Claim 2 是 bonus insight\n\n### 攻击 2: \"Mechanistic explanation 是 post-hoc rationalization\"\n**预期措辞**: \"The representation geometry analysis is descriptive, not causal. You cannot conclude that saturation causes strategy interaction.\"\n**Rebuttal 要点**:\n- 正确，neg_difficulty analysis 是描述性的 (cosine similarity statistics)，不是实验操控\n- 我们明确标记为 \"mechanistic hypothesis\" 而非 \"causal proof\"\n- 但描述性证据仍有 explanatory value: margin compression (77% Qwen vs 65% StarCoder) 与 pilot 结果方向一致\n- 完整因果验证需要控制实验 (e.g., 人工缩放 pos_sim 后测试策略效果)，留待 future work\n\n### 攻击 3: \"Exploratory observation 不算 contribution\"\n**预期措辞**: \"If Claim 2 is merely an observation, the paper has only one real contribution (Claim 1) plus a methodology contribution (Claim 3).\"\n**Rebuttal 要点**:\n- EMNLP 有 strong tradition of empirical analysis papers where observations + hypotheses are valued (cf. \"Do Language Models...\" papers)\n- Claim 2 包含 testable prediction (pos_sim threshold)，不是 vacuous observation\n- Claim 1 (challenging gradient-based assumption) + Claim 3 (scalable pipeline) + Claim 2 (explanatory observation) 的组合足够\n- 如果审稿人认为不够，可考虑升级 Claim 3 的呈现方式或添加 BM25 baseline 作为第四个贡献点\n\n### 攻击 4: \"Paper 内部不一致——abstract/intro 说 exploratory，但 discussion 说 predicts/explains\"\n**预期措辞**: \"The paper's own framing is inconsistent — Section 5.2 uses assertive language that contradicts the [Exploratory observation] tag.\"\n**Rebuttal 要点**:\n- 这是本 review 发现的核心问题。如果不修改，审稿人会指出 self-contradiction。\n- **在提交前必须修复 discussion §5.2 的措辞**，否则审稿人有理由认为作者试图 overclaim。\n- 一致性是可信度的基础——hedging 要么全做要么不做，不能 contribution list 说 exploratory 但 body text 说 established。\n\n### 攻击 5: \"Dataflow 两个编码器都不如 embedding，interaction 在哪?\"\n**预期措辞**: \"Both encoders show dataflow < embedding. Where is the interaction? The pattern is uniformly negative.\"\n**Rebuttal 要点**:\n- Interaction 不是 \"dataflow sometimes wins\"，而是 gap magnitude is encoder-dependent (Qwen -1.2pp vs StarCoder -1.0pp, 或 full M2 数据)\n- neg_difficulty margin 差异 (+17% vs +28%) 与 gap 方向一致\n- 更根本的 interaction 是 dataflow vs random: Qwen +0.8pp, StarCoder -0.5pp (pilot)——方向相反\n- 但要诚实: 如果 full M2 显示两个编码器 dataflow vs random 都为负，interaction claim 进一步弱化\n\n---\n\n## 缺失的 Hedging 元素清单\n\n当前 Claim 2 的 hedge 应在**每个出现位置**包含以下至少 2/4 项:\n\n| 元素 | paper_framing Claim 2 | intro Contrib 2 | intro Para 3 | exp §4.4 | disc §5.2 | RW §2.3 |\n|------|:---:|:---:|:---:|:---:|:---:|:---:|\n| \"exploratory\" / \"observation\" 标签 | ✅ | ✅ | ❌ | ⚠️(title only) | ❌ | ❌ |\n| n=2 limitation | ❌(pending区) | ❌ | ❌ | ❌ | ✅(末尾) | ❌ |\n| encoder-dependent caveat | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ |\n| testable prediction 前向声明 | ❌ | ❌ | ❌ | ❌ | ⚠️(partial) | ❌ |\n\n**最薄弱**: related_work §2.3（0/4 元素）、intro Para 3（1/4）、discussion §5.2 body（1/4，仅末尾 caveat）。\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4dee100a-227a-473d-8690-4a65ad039e87",
  "isSidechain": false,
  "requestId": "req_011Cb3XWDy9vDuoFC2xuMYPE",
  "type": "assistant",
  "uuid": "bdd1c3a2-53f9-42fd-8baf-15718caf2b8f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "999f865e-f544-467f-b7e8-732fb33862f3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019g3RePv3h4er9MzcUv8DUJ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 17017,
      "cache_read_input_tokens": 51964,
      "output_tokens": 7580,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 17017,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 7580,
          "cache_read_input_tokens": 51964,
          "cache_creation_input_tokens": 17017,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 17017
          },
          "type": "message"
        }
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

_source line 49 · 2026-05-15T02:01:38.362Z_

<details><summary>↩ Tool result · `toolu_01Pve9a5DxTkngf4U5TxPwFe`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/claim2_wording_review.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bdd1c3a2-53f9-42fd-8baf-15718caf2b8f",
  "isSidechain": false,
  "promptId": "82620338-1cd7-4c43-9283-e5cb821c1607",
  "type": "user",
  "uuid": "c6fc1922-d19c-4acb-a575-5c8e42dd8532",
  "toolUseResult": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/claim2_wording_review.md",
    "content": "# Claim 2 Wording Review: \"Exploratory Observation\" Consistency Audit\n\n**Date**: 2026-05-15\n**Scope**: All paper_framing.md + paper draft .md files\n**Reference decision**: D035 — Claim 2 降级为 \"exploratory observation with testable prediction\"\n\n---\n\n## Summary\n\nClaim 2 的 **[Exploratory observation]** 标签仅在 2 处出现（paper_framing.md Claim 定义 + introduction contribution list），但 body text 中有 **11 处** 使用了与 exploratory 不兼容的断言性措辞（\"reveals\", \"explains\", \"predicts\", \"shows that\"）。Discussion §5.2 是最严重的区域——标题和正文均用预测性语言，暗示 n=2 观察已构成 validated mechanism。\n\nClaim 1（strong, confirmed）与 Claim 2（exploratory）的区分在 contribution list 中清晰，但在正文中逐渐模糊，特别是 introduction 最后一段、related work §2.3、discussion §5.2。\n\n---\n\n## 逐处审查\n\n### paper_framing.md\n\n| 位置 | 当前措辞 | 强度 | 问题 |\n|------|----------|------|------|\n| Core Claims - Claim 2 | \"[Exploratory observation]...This is reported as an observation with mechanistic hypothesis, not an established finding.\" | ✅ 合适 | 明确标记+caveat |\n| Story Spine - contribution (2) | \"observe that structure-grounded (dataflow) negatives interact with encoder representation geometry and provide mechanistic analysis\" | ⚠️ 偏强 | 缺 \"exploratory\" 标签；\"provide mechanistic analysis\" 暗示已完成验证 |\n| Headline result template | \"representation geometry analysis via negative difficulty provides mechanistic explanation for when different mining strategies are effective\" | ⚠️ 偏强 | \"provides mechanistic explanation\" 对 n=2 过于断言 |\n| Core Insight | \"The effectiveness of hard negative mining strategies depends on the encoder's representation geometry.\" | ❌ 过强 | 无任何 hedge，读为 general claim，无 n=2/exploratory 标记 |\n| Dual-Pillar Motivation - Secondary | \"enabling practitioners to predict which strategy suits their encoder without exhaustive experiments\" | ❌ 过强 | 从 n=2 观察直接推出 practitioner guidance，暗示 validated predictive power |\n| Reviewer Concerns - \"Only 2 encoders\" | \"n=2 is minimum for interaction claim; we frame as observation with mechanism, not universal law\" | ✅ 合适 | 明确承认 |\n| Contingency | \"Pivot to 2-claim paper...Drop Claim 2 to analysis observation\" | ✅ 合适 | 有降级准备 |\n\n### introduction_v1.md\n\n| 位置 | 当前措辞 | 强度 | 问题 |\n|------|----------|------|------|\n| Para 3 (intro body) | \"analysis of negative difficulty margins reveals that the encoder's pretrained representation geometry...mediates which strategy is most effective, providing a mechanistic explanation for when and why\" | ⚠️ 偏强 | \"reveals\" + \"providing a mechanistic explanation\" 无 exploratory hedge；与紧接其后的 Contribution 2 的 hedging 形成矛盾 |\n| Contribution 2 | \"[Exploratory observation] We report that...This is reported as an observation with mechanistic hypothesis, pending multi-seed confirmation.\" | ✅ 合适 | 完整 hedge：标签+caveat+pending 声明 |\n\n**矛盾**：Para 3 用 \"reveals...provides mechanistic explanation\"，Contribution 2 紧接着说 \"observation with mechanistic hypothesis\"。读者会注意到措辞强度骤降。\n\n### experiments_v1.md\n\n| 位置 | 当前措辞 | 强度 | 问题 |\n|------|----------|------|------|\n| §4.1 Encoders | \"This divergence enables us to study how representation geometry mediates the effectiveness of different negative mining strategies.\" | ⚠️ 偏强 | \"mediates\" 预设因果，应为 \"may mediate\" 或 \"appears to mediate\" |\n| §4.3 Pilot (ii) | \"the dataflow-aware strategy's effectiveness is encoder-dependent—beneficial for Qwen but neutral-to-negative for StarCoder\" | ✅ 合适 | 限定在 pilot 结果描述 |\n| §4.4 Mechanistic hypothesis title | \"Mechanistic hypothesis\" | ✅ 合适 | 标题正确标记为 hypothesis |\n| §4.4 Mechanistic hypothesis body | \"When the pretrained space is saturated, the encoder has limited room...Embedding-distance negatives provide a direct optimization target...Dataflow-aware negatives...may not align with the encoder's most informative gradient direction\" | ⚠️ 偏强 | 前半段读为已确认的解释（\"the encoder has limited room\"），后半段用 \"may not align\" 有 hedge。整体偏 explanatory 而非 hypothesis |\n| §4.4 Difficulty gradient | \"The steeper relative compression for Qwen suggests that...\" | ✅ 合适 | \"suggests\" 恰当 |\n\n### discussion_v2.md (最严重)\n\n| 位置 | 当前措辞 | 强度 | 问题 |\n|------|----------|------|------|\n| §5.2 标题 | \"Representation Geometry as a Predictor of Strategy Effectiveness\" | ❌ 过强 | \"Predictor\" 暗示 validated predictive power，n=2 不支持 |\n| §5.2 首句 | \"reveals a practical insight: the pretrained encoder's representation geometry predicts whether structure-grounded negatives will provide benefit\" | ❌ 过强 | \"reveals\" + \"predicts\" 双重断言 |\n| §5.2 Qwen 解释 | \"This explains the +0.8pp R@1 improvement\" | ❌ 过强 | \"explains\" 对 n=2 correlational 观察过于因果 |\n| §5.2 practical implication | \"This interaction...has a practical implication: practitioners can compute pos_sim...\" | ⚠️ 偏强 | 从 n=2 直接给出 practitioner recipe |\n| §5.2 threshold | \"though we note this threshold is derived from two encoder observations and should be validated more broadly\" | ✅ 合适 | 明确 n=2 caveat |\n| §5.3 Limitations | \"enabling our interaction analysis—generalizing...requires further investigation\" | ✅ 合适 | 承认泛化限制 |\n| §5.4 Future Work | \"Our observation that pos_sim predicts strategy effectiveness suggests...\" | ⚠️ 偏强 | \"predicts\" 仍过强，但 \"observation...suggests\" 结构有 hedge |\n\n### related_work_v1.md\n\n| 位置 | 当前措辞 | 强度 | 问题 |\n|------|----------|------|------|\n| §2.3 末段 | \"show that the relative effectiveness of mining strategies depends on the encoder's pretrained representation geometry\" | ❌ 过强 | \"show that...depends on\" 是 confirmed finding 的措辞 |\n\n### method_v1.md\n\n| 位置 | 当前措辞 | 强度 | 问题 |\n|------|----------|------|------|\n| §3.1 | \"analyze how their effectiveness interacts with the encoder's pretrained representation geometry\" | ✅ 合适 | 描述研究行为，不做 claim |\n\n---\n\n## 统计\n\n| 强度 | 数量 | 位置 |\n|------|------|------|\n| ✅ 合适 | 11 | paper_framing (3), intro contrib (1), experiments (3), discussion (2), method (1), figure_design (1) |\n| ⚠️ 偏强 | 7 | paper_framing (2), intro para3 (1), experiments (2), discussion (2) |\n| ❌ 过强 | 5 | paper_framing Core Insight (1), paper_framing Dual-Pillar (1), discussion §5.2 (3) |\n\n---\n\n## 建议修改\n\n### 必须修改 (❌ 过强)\n\n**1. paper_framing.md - Core Insight**\n- 现在: \"The effectiveness of hard negative mining strategies depends on the encoder's representation geometry.\"\n- 建议: \"Our pilot data suggests that the effectiveness of hard negative mining strategies may depend on the encoder's representation geometry — a hypothesis derived from two encoders and requiring broader validation.\"\n\n**2. paper_framing.md - Dual-Pillar Secondary**\n- 现在: \"enabling practitioners to predict which strategy suits their encoder without exhaustive experiments\"\n- 建议: \"offering a candidate heuristic (pos_sim threshold) that, if validated on more encoders, could help practitioners select strategies without exhaustive experiments\"\n\n**3. discussion_v2.md - §5.2 标题**\n- 现在: \"Representation Geometry as a Predictor of Strategy Effectiveness\"\n- 建议: \"Representation Geometry and Strategy Effectiveness: An Exploratory Analysis\"\n\n**4. discussion_v2.md - §5.2 首句**\n- 现在: \"reveals a practical insight: the pretrained encoder's representation geometry predicts whether...\"\n- 建议: \"suggests a hypothesis worth further investigation: the pretrained encoder's representation geometry may predict whether...\"\n\n**5. discussion_v2.md - §5.2 \"explains\"**\n- 现在: \"This explains the +0.8pp R@1 improvement\"\n- 建议: \"This is consistent with the +0.8pp R@1 improvement\"\n\n**6. related_work_v1.md - §2.3**\n- 现在: \"show that the relative effectiveness of mining strategies depends on\"\n- 建议: \"observe that the relative effectiveness of mining strategies appears to depend on\"\n\n### 建议修改 (⚠️ 偏强)\n\n**7. paper_framing.md - Story Spine contribution (2)**\n- 添加 \"[exploratory]\" 标签: \"(2) [exploratory] observe that...\"\n\n**8. introduction_v1.md - Para 3**\n- \"reveals\" → \"suggests\"\n- \"providing a mechanistic explanation\" → \"providing a candidate mechanistic explanation (Section 4.4)\"\n\n**9. experiments_v1.md - §4.1 Encoders**\n- \"mediates\" → \"may mediate\"\n\n**10. experiments_v1.md - §4.4 Mechanistic hypothesis body**\n- 首句添加: \"Based on our two-encoder comparison, we hypothesize the following mechanism:\"\n\n**11. discussion_v2.md - §5.4 Future Work**\n- \"predicts\" → \"appears to correlate with\"\n\n---\n\n## Claim 1 vs Claim 2 区分度\n\n| 文档位置 | 区分清晰度 | 说明 |\n|----------|-----------|------|\n| paper_framing Contribution list | ✅ 清晰 | Claim 1 无标签 (strong), Claim 2 有 [Exploratory observation] |\n| introduction Contribution list | ✅ 清晰 | 同上，且 Claim 2 有 pending 声明 |\n| introduction body (Para 3) | ❌ 模糊 | \"central finding\" 引出 Claim 1 后直接 \"we observe\" 引出 Claim 2，无强度差异标记 |\n| experiments body | ⚠️ 部分模糊 | pilot 段落区分合理，但 §4.4 mechanistic hypothesis 读为与 §4.3 main results 同等强度 |\n| discussion | ❌ 模糊 | §5.2 标题和正文与 §5.1 (methodology) 同等断言强度 |\n| related work | ❌ 模糊 | 两个 claim 在 §2.3 末段同一句中出现，用相同强度的 \"show that\" |\n\n**建议**: Introduction Para 3 中 Claim 2 部分添加括号注: \"(an exploratory finding; see Section 4.4)\"。Discussion §5.2 开头添加一句: \"We present the following analysis as an exploratory observation from two encoders, not a validated mechanism.\"\n\n---\n\n## 审稿人攻击角度与预备 Rebuttal\n\n### 攻击 1: \"n=2 不足以支持任何 interaction claim\"\n**预期措辞**: \"The authors claim representation geometry mediates strategy effectiveness, but with only two encoders this is an anecdote, not evidence.\"\n**Rebuttal 要点**:\n- 承认 n=2 是核心限制，这正是我们标记为 exploratory observation 而非 confirmed finding 的原因\n- 但两个编码器有 meaningful variation: 不同预训练语料、不同 representation geometry (pos_sim 0.986 vs 0.799)、不同预训练目标\n- 我们提供 testable prediction: pos_sim > 0.98 时 structure-grounded negatives 更有效。这比纯 empirical 结果更有 scientific value\n- 论文主要贡献是 Claim 1 (embedding mining suffices)，Claim 2 是 bonus insight\n\n### 攻击 2: \"Mechanistic explanation 是 post-hoc rationalization\"\n**预期措辞**: \"The representation geometry analysis is descriptive, not causal. You cannot conclude that saturation causes strategy interaction.\"\n**Rebuttal 要点**:\n- 正确，neg_difficulty analysis 是描述性的 (cosine similarity statistics)，不是实验操控\n- 我们明确标记为 \"mechanistic hypothesis\" 而非 \"causal proof\"\n- 但描述性证据仍有 explanatory value: margin compression (77% Qwen vs 65% StarCoder) 与 pilot 结果方向一致\n- 完整因果验证需要控制实验 (e.g., 人工缩放 pos_sim 后测试策略效果)，留待 future work\n\n### 攻击 3: \"Exploratory observation 不算 contribution\"\n**预期措辞**: \"If Claim 2 is merely an observation, the paper has only one real contribution (Claim 1) plus a methodology contribution (Claim 3).\"\n**Rebuttal 要点**:\n- EMNLP 有 strong tradition of empirical analysis papers where observations + hypotheses are valued (cf. \"Do Language Models...\" papers)\n- Claim 2 包含 testable prediction (pos_sim threshold)，不是 vacuous observation\n- Claim 1 (challenging gradient-based assumption) + Claim 3 (scalable pipeline) + Claim 2 (explanatory observation) 的组合足够\n- 如果审稿人认为不够，可考虑升级 Claim 3 的呈现方式或添加 BM25 baseline 作为第四个贡献点\n\n### 攻击 4: \"Paper 内部不一致——abstract/intro 说 exploratory，但 discussion 说 predicts/explains\"\n**预期措辞**: \"The paper's own framing is inconsistent — Section 5.2 uses assertive language that contradicts the [Exploratory observation] tag.\"\n**Rebuttal 要点**:\n- 这是本 review 发现的核心问题。如果不修改，审稿人会指出 self-contradiction。\n- **在提交前必须修复 discussion §5.2 的措辞**，否则审稿人有理由认为作者试图 overclaim。\n- 一致性是可信度的基础——hedging 要么全做要么不做，不能 contribution list 说 exploratory 但 body text 说 established。\n\n### 攻击 5: \"Dataflow 两个编码器都不如 embedding，interaction 在哪?\"\n**预期措辞**: \"Both encoders show dataflow < embedding. Where is the interaction? The pattern is uniformly negative.\"\n**Rebuttal 要点**:\n- Interaction 不是 \"dataflow sometimes wins\"，而是 gap magnitude is encoder-dependent (Qwen -1.2pp vs StarCoder -1.0pp, 或 full M2 数据)\n- neg_difficulty margin 差异 (+17% vs +28%) 与 gap 方向一致\n- 更根本的 interaction 是 dataflow vs random: Qwen +0.8pp, StarCoder -0.5pp (pilot)——方向相反\n- 但要诚实: 如果 full M2 显示两个编码器 dataflow vs random 都为负，interaction claim 进一步弱化\n\n---\n\n## 缺失的 Hedging 元素清单\n\n当前 Claim 2 的 hedge 应在**每个出现位置**包含以下至少 2/4 项:\n\n| 元素 | paper_framing Claim 2 | intro Contrib 2 | intro Para 3 | exp §4.4 | disc §5.2 | RW §2.3 |\n|------|:---:|:---:|:---:|:---:|:---:|:---:|\n| \"exploratory\" / \"observation\" 标签 | ✅ | ✅ | ❌ | ⚠️(title only) | ❌ | ❌ |\n| n=2 limitation | ❌(pending区) | ❌ | ❌ | ❌ | ✅(末尾) | ❌ |\n| encoder-dependent caveat | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ |\n| testable prediction 前向声明 | ❌ | ❌ | ❌ | ❌ | ⚠️(partial) | ❌ |\n\n**最薄弱**: related_work §2.3（0/4 元素）、intro Para 3（1/4）、discussion §5.2 body（1/4，仅末尾 caveat）。\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  },
  "sourceToolAssistantUUID": "bdd1c3a2-53f9-42fd-8baf-15718caf2b8f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "999f865e-f544-467f-b7e8-732fb33862f3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 50_

```json
{
  "type": "last-prompt",
  "leafUuid": "c6fc1922-d19c-4acb-a575-5c8e42dd8532",
  "sessionId": "999f865e-f544-467f-b7e8-732fb33862f3"
}
```

---

### Runtime record

_source line 51_

```json
{
  "type": "ai-title",
  "aiTitle": "Review Claim 2 wording defensiveness",
  "sessionId": "999f865e-f544-467f-b7e8-732fb33862f3"
}
```

---

### Assistant

_source line 52 · 2026-05-15T02:01:49.914Z_

审查报告已写入 `artifacts/paper_drafts/claim2_wording_review.md`。

核心发现：

- **[Exploratory observation] 标签仅出现在 2 处**（paper_framing Claim 定义 + intro contribution list），但 body text 有 **5 处 ❌ 过强** + **7 处 ⚠️ 偏强** 的措辞
- **最严重区域是 Discussion §5.2**：标题用 "Predictor"，正文用 "reveals"/"explains"/"predicts"，与 contribution list 的 "exploratory observation" 直接矛盾——审稿人会抓这个 self-contradiction
- **Related Work §2.3** 末段用 "show that...depends on"，是 confirmed finding 的措辞，0/4 hedging 元素
- **paper_framing.md Core Insight** 无任何 hedge，读为 general claim
- Claim 1 vs Claim 2 的强度区分在 contribution list 清晰，在 intro body、discussion、related work 中模糊

报告包含 11 条具体修改建议（6 条必须、5 条建议）和 5 个审稿人攻击角度的 rebuttal 要点。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c6fc1922-d19c-4acb-a575-5c8e42dd8532",
  "isSidechain": false,
  "requestId": "req_011Cb3XirwjLMK6uxg6fGoai",
  "type": "assistant",
  "uuid": "e83c9773-f195-4b8b-b835-dc2a1076fe05",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "999f865e-f544-467f-b7e8-732fb33862f3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TyCV17ueiJBqWoKmQS5Xbd",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7637,
      "cache_read_input_tokens": 68981,
      "output_tokens": 350,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 7637,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 350,
          "cache_read_input_tokens": 68981,
          "cache_creation_input_tokens": 7637,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 7637
          },
          "type": "message"
        }
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

_source line 53_

```json
{
  "type": "last-prompt",
  "leafUuid": "e83c9773-f195-4b8b-b835-dc2a1076fe05",
  "sessionId": "999f865e-f544-467f-b7e8-732fb33862f3"
}
```

---

### Runtime record

_source line 54_

```json
{
  "type": "ai-title",
  "aiTitle": "Review Claim 2 wording defensiveness",
  "sessionId": "999f865e-f544-467f-b7e8-732fb33862f3"
}
```

---
