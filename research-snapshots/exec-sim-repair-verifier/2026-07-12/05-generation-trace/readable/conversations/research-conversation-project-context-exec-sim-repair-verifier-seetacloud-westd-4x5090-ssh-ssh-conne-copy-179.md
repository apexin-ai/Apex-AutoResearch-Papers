# Research conversation: <project_context> # 项目: exec-sim-repair-verifier ## 运行环境 - 服务器名: seetacloud-westd-4x5090 - SSH 连接命令: ssh connect.westd.s

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 40
- **Recorded user turns:** 1
- **Tool calls:** 11
- **Original source:** `logs/chats/exported-trajectories/account-1/8c11e549-46d3-438b-848f-c86f519fca39.jsonl`
- **Structured JSON:** [`915bc09725f28ff808e3.json`](../../sessions/91/915bc09725f28ff808e3.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-22T19:18:48.092Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-22T19:18:48.092Z",
  "sessionId": "8c11e549-46d3-438b-848f-c86f519fca39",
  "content": "&lt;project_context>\n# 项目: exec-sim-repair-verifier\n\n## 运行环境\n- 服务器名: seetacloud-westd-4x5090\n- SSH 连接命令: ssh connect.westd.seetacloud.com  # 必须用此命令，~/.ssh/config 自动应用密钥和跳板机，禁止用裸 IP\n- 项目代码根目录: /home/sonny/exec-sim-repair-verifier\n\n\n## 环境搭建\n连接服务器后先调 `detect_image` 检测是否为预置镜像。如果匹配，跳过基础环境搭建，只装项目特有依赖。已预装的包不要重复安装。\n\n## 输出风格\n回复简洁直接。只输出执行结果和必要信息，不要解释过程、不要客套、不要给未被要求的建议。\n&lt;/project_context>\n## 任务：审计论文中需要添加14B数据的所有位置\n\n### 背景\n14B模型实验正在进行中。需要预先找出论文中所有需要插入14B结果的位置（Tables、Figures、正文提及），生成清单。\n\n### 执行步骤\n1. 读论文所有tex文件：检查 `/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/` 目录下所有 `.tex` 文件\n2. 搜索所有 Table：找出每个Table的内容，判断是否包含按模型规模分行的数据（如 4B/8B 行）→ 需要加 14B 行\n3. 搜索所有 Figure：找出涉及 scaling/模型规模的图表 → 需要加 14B 数据点\n4. 搜索正文中提及 \"4B\", \"8B\", \"≤8B\", \"scaling\", \"model size\" 等关键词的段落 → 可能需要更新措辞\n5. 读 paper_framing.md 确认 14B 在 story 中的定位：`read_project_file(project=\"exec-sim-repair-verifier\", file=\"paper_framing.md\")`\n\n### 输出格式\n生成清单写入 `report.md` 或直接输出，格式：\n\n```\n## 14B 数据插入点清单\n\n### Tables\n- Table X (文件:行号): 描述，需要加14B行，当前有4B/8B\n- ...\n\n### Figures  \n- Figure Y (文件:行号): 描述，需要加14B数据点\n- ...\n\n### 正文段落\n- §A.B (文件:行号): \"原文片段...\"，需要更新为包含14B\n- ...\n\n### Abstract/Intro/Conclusion\n- 位置: 需要更新的措辞\n- ...\n```\n\n不要修改任何文件，只产出清单。"
}
````

---

### Runtime record

_source line 2 · 2026-05-22T19:18:48.103Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-22T19:18:48.103Z",
  "sessionId": "8c11e549-46d3-438b-848f-c86f519fca39"
}
```

---

## Round 1

38 recorded events

### User

_source line 3 · 2026-05-22T19:18:48.172Z_

&lt;project_context>
# 项目: exec-sim-repair-verifier

## 运行环境
- 服务器名: seetacloud-westd-4x5090
- SSH 连接命令: ssh connect.westd.seetacloud.com  # 必须用此命令，~/.ssh/config 自动应用密钥和跳板机，禁止用裸 IP
- 项目代码根目录: /home/sonny/exec-sim-repair-verifier


## 环境搭建
连接服务器后先调 `detect_image` 检测是否为预置镜像。如果匹配，跳过基础环境搭建，只装项目特有依赖。已预装的包不要重复安装。

## 输出风格
回复简洁直接。只输出执行结果和必要信息，不要解释过程、不要客套、不要给未被要求的建议。
&lt;/project_context>
## 任务：审计论文中需要添加14B数据的所有位置

### 背景
14B模型实验正在进行中。需要预先找出论文中所有需要插入14B结果的位置（Tables、Figures、正文提及），生成清单。

### 执行步骤
1. 读论文所有tex文件：检查 `/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/` 目录下所有 `.tex` 文件
2. 搜索所有 Table：找出每个Table的内容，判断是否包含按模型规模分行的数据（如 4B/8B 行）→ 需要加 14B 行
3. 搜索所有 Figure：找出涉及 scaling/模型规模的图表 → 需要加 14B 数据点
4. 搜索正文中提及 "4B", "8B", "≤8B", "scaling", "model size" 等关键词的段落 → 可能需要更新措辞
5. 读 paper_framing.md 确认 14B 在 story 中的定位：`read_project_file(project="exec-sim-repair-verifier", file="paper_framing.md")`

### 输出格式
生成清单写入 `report.md` 或直接输出，格式：

```
## 14B 数据插入点清单

### Tables
- Table X (文件:行号): 描述，需要加14B行，当前有4B/8B
- ...

### Figures  
- Figure Y (文件:行号): 描述，需要加14B数据点
- ...

### 正文段落
- §A.B (文件:行号): "原文片段..."，需要更新为包含14B
- ...

### Abstract/Intro/Conclusion
- 位置: 需要更新的措辞
- ...
```

不要修改任何文件，只产出清单。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "ec010885-b9c9-4574-b4a8-341b5a1f339a",
  "type": "user",
  "uuid": "4ec7ce79-1aed-4368-93dd-266d94d19333",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier",
  "sessionId": "8c11e549-46d3-438b-848f-c86f519fca39",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-22T19:18:48.171Z_

```json
{
  "parentUuid": "4ec7ce79-1aed-4368-93dd-266d94d19333",
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
  "uuid": "5795e6fc-da31-4cb7-b96c-d28321087262",
  "timestamp": "2026-05-22T19:18:48.171Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier",
  "sessionId": "8c11e549-46d3-438b-848f-c86f519fca39",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

---

### Runtime record

_source line 5 · 2026-05-22T19:18:48.171Z_

```json
{
  "parentUuid": "5795e6fc-da31-4cb7-b96c-d28321087262",
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
  "uuid": "e7346c19-4b32-4a7e-9e6e-40afba8edc98",
  "timestamp": "2026-05-22T19:18:48.171Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier",
  "sessionId": "8c11e549-46d3-438b-848f-c86f519fca39",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

---

### Runtime record

_source line 6 · 2026-05-22T19:18:48.171Z_

```json
{
  "parentUuid": "e7346c19-4b32-4a7e-9e6e-40afba8edc98",
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
  "uuid": "b51c4509-af9e-4183-93f9-822657b40cb4",
  "timestamp": "2026-05-22T19:18:48.171Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier",
  "sessionId": "8c11e549-46d3-438b-848f-c86f519fca39",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

---

### Runtime record

_source line 7 · 2026-05-22T19:18:48.171Z_

```json
{
  "parentUuid": "b51c4509-af9e-4183-93f9-822657b40cb4",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "aa7ef947-1d01-453b-82ca-002a518f4d53",
  "timestamp": "2026-05-22T19:18:48.171Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier",
  "sessionId": "8c11e549-46d3-438b-848f-c86f519fca39",
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
  "aiTitle": "Audit paper for 14B model data insertion points",
  "sessionId": "8c11e549-46d3-438b-848f-c86f519fca39"
}
```

---

### Assistant

_source line 9 · 2026-05-22T19:18:50.869Z_

I'll audit all tex files in the paper directory to find every location that needs 14B data.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "aa7ef947-1d01-453b-82ca-002a518f4d53",
  "isSidechain": false,
  "requestId": "req_011CbJ9UVCP927fDEEjh9L4h",
  "type": "assistant",
  "uuid": "b2b967b8-2fa7-4310-9b75-751b44194606",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier",
  "sessionId": "8c11e549-46d3-438b-848f-c86f519fca39",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015PSEMPkNPm8yXFopR5Jd3T",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13339,
      "cache_read_input_tokens": 11447,
      "output_tokens": 150,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 13339,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 150,
          "cache_read_input_tokens": 11447,
          "cache_creation_input_tokens": 13339,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 13339
          },
          "type": "message"
        }
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

_source line 10 · 2026-05-22T19:18:51.418Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01ELHzGH7W2QTHobMubFk2Mm`</summary>

```json
{
  "pattern": "docs/paper/**/*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b2b967b8-2fa7-4310-9b75-751b44194606",
  "isSidechain": false,
  "requestId": "req_011CbJ9UVCP927fDEEjh9L4h",
  "type": "assistant",
  "uuid": "2c2ede01-c32c-4a29-bfa0-a26145bcd6b9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier",
  "sessionId": "8c11e549-46d3-438b-848f-c86f519fca39",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015PSEMPkNPm8yXFopR5Jd3T",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13339,
      "cache_read_input_tokens": 11447,
      "output_tokens": 150,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 13339,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 150,
          "cache_read_input_tokens": 11447,
          "cache_creation_input_tokens": 13339,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 13339
          },
          "type": "message"
        }
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

_source line 11 · 2026-05-22T19:18:51.470Z_

<details><summary>↩ Tool result · `toolu_01ELHzGH7W2QTHobMubFk2Mm`</summary>

```text
docs/paper/method.tex
docs/paper/checklist.tex
docs/paper/abstract.tex
docs/paper/related_work.tex
docs/paper/introduction.tex
docs/paper/conclusion.tex
docs/paper/main.tex
docs/paper/experiments.tex
docs/paper/appendix.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2c2ede01-c32c-4a29-bfa0-a26145bcd6b9",
  "isSidechain": false,
  "promptId": "ec010885-b9c9-4574-b4a8-341b5a1f339a",
  "type": "user",
  "uuid": "3aa5142e-378d-4881-b5d8-dc8a4e04aad0",
  "toolUseResult": {
    "filenames": [
      "docs/paper/method.tex",
      "docs/paper/checklist.tex",
      "docs/paper/abstract.tex",
      "docs/paper/related_work.tex",
      "docs/paper/introduction.tex",
      "docs/paper/conclusion.tex",
      "docs/paper/main.tex",
      "docs/paper/experiments.tex",
      "docs/paper/appendix.tex"
    ],
    "durationMs": 43,
    "numFiles": 9,
    "truncated": false
  },
  "sourceToolAssistantUUID": "2c2ede01-c32c-4a29-bfa0-a26145bcd6b9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier",
  "sessionId": "8c11e549-46d3-438b-848f-c86f519fca39",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-22T19:18:52.344Z_

<details><summary>↩ Tool result · `toolu_018Nfcoho3QM4R4CnFB1qMs1`</summary>

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
  "parentUuid": "8e5600bd-2f82-4e3d-baca-45d1cdde0b93",
  "isSidechain": false,
  "promptId": "ec010885-b9c9-4574-b4a8-341b5a1f339a",
  "type": "user",
  "uuid": "6c4b1549-e7e5-4ae4-a17a-56d407995b95",
  "toolUseResult": {
    "matches": [
      "mcp__agent-ml-research__read_project_file"
    ],
    "query": "select:mcp__agent-ml-research__read_project_file",
    "total_deferred_tools": 22
  },
  "sourceToolAssistantUUID": "8e5600bd-2f82-4e3d-baca-45d1cdde0b93",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier",
  "sessionId": "8c11e549-46d3-438b-848f-c86f519fca39",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-22T19:18:52.340Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_018Nfcoho3QM4R4CnFB1qMs1`</summary>

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
  "parentUuid": "3aa5142e-378d-4881-b5d8-dc8a4e04aad0",
  "isSidechain": false,
  "requestId": "req_011CbJ9UVCP927fDEEjh9L4h",
  "type": "assistant",
  "uuid": "8e5600bd-2f82-4e3d-baca-45d1cdde0b93",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier",
  "sessionId": "8c11e549-46d3-438b-848f-c86f519fca39",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015PSEMPkNPm8yXFopR5Jd3T",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13339,
      "cache_read_input_tokens": 11447,
      "output_tokens": 150,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 13339,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 150,
          "cache_read_input_tokens": 11447,
          "cache_creation_input_tokens": 13339,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 13339
          },
          "type": "message"
        }
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

_source line 14 · 2026-05-22T19:18:54.609Z_

<details><summary>Logged reasoning block</summary>

```text
Let me read all the tex files and the paper_framing.md in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6c4b1549-e7e5-4ae4-a17a-56d407995b95",
  "isSidechain": false,
  "requestId": "req_011CbJ9UoRFm2GRjSasNgqwg",
  "type": "assistant",
  "uuid": "c4cd2c5c-91e9-404b-9b8d-4c0e42bcdcde",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier",
  "sessionId": "8c11e549-46d3-438b-848f-c86f519fca39",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01U16PPjqHqZa23X2kRksyjc",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 614,
      "cache_read_input_tokens": 24786,
      "output_tokens": 748,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 614,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 748,
          "cache_read_input_tokens": 24786,
          "cache_creation_input_tokens": 614,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 614
          },
          "type": "message"
        }
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

_source line 15 · 2026-05-22T19:18:55.101Z_

Reading all tex files and paper_framing.md in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c4cd2c5c-91e9-404b-9b8d-4c0e42bcdcde",
  "isSidechain": false,
  "requestId": "req_011CbJ9UoRFm2GRjSasNgqwg",
  "type": "assistant",
  "uuid": "d85aa07e-6756-4e2e-86d0-ccbc5703d192",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier",
  "sessionId": "8c11e549-46d3-438b-848f-c86f519fca39",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01U16PPjqHqZa23X2kRksyjc",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 614,
      "cache_read_input_tokens": 24786,
      "output_tokens": 748,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 614,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 748,
          "cache_read_input_tokens": 24786,
          "cache_creation_input_tokens": 614,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 614
          },
          "type": "message"
        }
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

_source line 16 · 2026-05-22T19:18:56.138Z_

<details open><summary>🔧 Tool call — Read · `toolu_01KnQEpDhv91d1W5dSYJ8PW5`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d85aa07e-6756-4e2e-86d0-ccbc5703d192",
  "isSidechain": false,
  "requestId": "req_011CbJ9UoRFm2GRjSasNgqwg",
  "type": "assistant",
  "uuid": "d4201dab-e714-4b50-94ef-40f7c6eea5ba",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier",
  "sessionId": "8c11e549-46d3-438b-848f-c86f519fca39",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01U16PPjqHqZa23X2kRksyjc",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 614,
      "cache_read_input_tokens": 24786,
      "output_tokens": 748,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 614,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 748,
          "cache_read_input_tokens": 24786,
          "cache_creation_input_tokens": 614,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 614
          },
          "type": "message"
        }
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

_source line 17 · 2026-05-22T19:18:56.161Z_

<details><summary>↩ Tool result · `toolu_01KnQEpDhv91d1W5dSYJ8PW5`</summary>

```text
1	\begin{abstract}
2	LLM-based program repair increasingly leverages test-time compute scaling, generating multiple candidate patches and selecting the best via a verifier. Execution-based verification is reliable but expensive; three execution-free alternatives have emerged: per-test binary classification (\cls{}), execution output generation (\cwm{}), and trajectory-level patch scoring (\traj{}). No prior work compares these formulations under matched conditions.
3	
4	We present the first systematic comparison across two representative code LLM families (Qwen3, DeepSeek-Coder), two complexity levels, and multiple seeds under ${\leq}$8B LoRA fine-tuning. At function level, \cls{} and \cwm{} are statistically equivalent across both families (TOST, 5 seeds): classification is not inherently easier than generation when outputs are short. \traj{} parity is model-dependent and not confirmed after multiple comparison correction. At repository level, a significant interaction ($z{=}-23.7$, DeepSeek-Coder) confirms this equivalence collapses: the \cls{}--\cwm{} gap widens to 18--26\pp{} across 3 seeds per model under our ${\leq}$8B LoRA protocol in variant-level evaluation, driven by format collapse in generation-based simulation. Gap magnitude depends on multiple confounds.
5	
6	Error complementarity and a failure mode taxonomy motivate complexity-aware formulation routing over uniform selection.
7	\end{abstract}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d4201dab-e714-4b50-94ef-40f7c6eea5ba",
  "isSidechain": false,
  "promptId": "ec010885-b9c9-4574-b4a8-341b5a1f339a",
  "type": "user",
  "uuid": "55260c08-30f2-4c70-a0bc-e4d75890e3ef",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/abstract.tex",
      "content": "\\begin{abstract}\nLLM-based program repair increasingly leverages test-time compute scaling, generating multiple candidate patches and selecting the best via a verifier. Execution-based verification is reliable but expensive; three execution-free alternatives have emerged: per-test binary classification (\\cls{}), execution output generation (\\cwm{}), and trajectory-level patch scoring (\\traj{}). No prior work compares these formulations under matched conditions.\n\nWe present the first systematic comparison across two representative code LLM families (Qwen3, DeepSeek-Coder), two complexity levels, and multiple seeds under ${\\leq}$8B LoRA fine-tuning. At function level, \\cls{} and \\cwm{} are statistically equivalent across both families (TOST, 5 seeds): classification is not inherently easier than generation when outputs are short. \\traj{} parity is model-dependent and not confirmed after multiple comparison correction. At repository level, a significant interaction ($z{=}-23.7$, DeepSeek-Coder) confirms this equivalence collapses: the \\cls{}--\\cwm{} gap widens to 18--26\\pp{} across 3 seeds per model under our ${\\leq}$8B LoRA protocol in variant-level evaluation, driven by format collapse in generation-based simulation. Gap magnitude depends on multiple confounds.\n\nError complementarity and a failure mode taxonomy motivate complexity-aware formulation routing over uniform selection.\n\\end{abstract}",
      "numLines": 7,
      "startLine": 1,
      "totalLines": 7
    }
  },
  "sourceToolAssistantUUID": "d4201dab-e714-4b50-94ef-40f7c6eea5ba",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier",
  "sessionId": "8c11e549-46d3-438b-848f-c86f519fca39",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-22T19:18:57.110Z_

<details open><summary>🔧 Tool call — Read · `toolu_01EuSZuywfjZYE63WwLqY7Li`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "55260c08-30f2-4c70-a0bc-e4d75890e3ef",
  "isSidechain": false,
  "requestId": "req_011CbJ9UoRFm2GRjSasNgqwg",
  "type": "assistant",
  "uuid": "16568425-32b9-4893-b460-d3128b6d3a95",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier",
  "sessionId": "8c11e549-46d3-438b-848f-c86f519fca39",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01U16PPjqHqZa23X2kRksyjc",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 614,
      "cache_read_input_tokens": 24786,
      "output_tokens": 748,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 614,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 748,
          "cache_read_input_tokens": 24786,
          "cache_creation_input_tokens": 614,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 614
          },
          "type": "message"
        }
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

_source line 19 · 2026-05-22T19:19:01.076Z_

<details><summary>↩ Tool result · `toolu_01PkJ6NwTbuAJSEEwAJJDBMK`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/paper_framing.md\", \"content\": \"# Paper Framing — exec-sim-repair-verifier\\n\\n## Target Venue\\n- Primary: EMNLP 2026 Main (ARR May 25, 2026)\\n- Deadline: ARR May 25, 2026\\n\\n## Framing Evolution\\n- **D116 (2026-05-16)**: Pivoted from \\\"CLS scales where generation fails\\\" (advocacy) to \\\"The Formulation Design Space for Neural Code Verification\\\" (empirical characterization)\\n- **D155 (2026-05-20)**: DeepSeek repo-level data confirms CWM collapse is **complexity-dependent** (both models collapse at repo-level), NOT tokenizer-specific. Original D116 claim \\\"Qwen 93% vs DeepSeek 11.8%\\\" was function-level only; repo-level shows DeepSeek CWM also 51-74% unparseable.\\n- **N4 Reframe**: Function-level equivalence elevated to headline finding; phase transition (func→repo divergence) as differentiating contribution.\\n\\n## Core Claims (current — post D155/N4 Reframe)\\n\\n1. **Formulation Equivalence at Function-Level**: CLS, CWM, and TRAJ achieve statistically equivalent accuracy at function-level across two model families (≤1.3pp gap, TOST p=0.007). Per-test CLS provides diagnostic granularity (which tests fail) at comparable accuracy with 217× throughput over CWM, though downstream re-repair benefit is unvalidated (n=44, p=0.42).\\n\\n2. **Phase Transition: Complexity-Dependent Divergence**: Formulations diverge 19-26pp at repo-level, driven by CWM format collapse (51-74% unparseable outputs, 0% truncation). Direction consistent across both model families; magnitude varies (Qwen3 74% unparseable vs DeepSeek 51% at matched seq_length). This is NOT tokenizer-specific — both models collapse when outputs are long and structured.\\n\\n3. **Error Complementarity**: CLS and CWM exhibit partial complementarity from different fail-bias degrees (CLS 56.5% FP, CWM 70.3% FP), yielding oracle ensemble 90.63% (+2.80pp over best single model).\\n\\n## Story Spine (updated)\\n\\n**Problem**: Execution-free verification for code repair can be formulated as per-test classification (CLS), execution output generation (CWM), or trajectory-level scoring (TRAJ). No controlled comparison exists across these formulations.\\n\\n**Gap**: Prior work uses different models, data, and compute for each formulation, making comparison impossible. Practitioners lack guidance on when formulation choice matters.\\n\\n**Our contribution**: First controlled comparison of three formulations across 2 model families, 2 complexity levels, and multiple seeds.\\n\\n**Headline finding**: Formulation choice is a **phase transition** — irrelevant at function-level (≤1.3pp), critical at repo-level (19-26pp). The mechanism: CWM's O(L) generation tokens become unparseable at repo-level complexity, collapsing to majority-baseline-or-worse accuracy. This pattern is robust across both tested model families.\\n\\n**Practical implication**: At ≤8B LoRA deployment scale, classification is the safer formulation for repo-level verification. CWM's generation capacity may recover at larger scales (32B+, pre-training on execution traces), but at practical fine-tuning sizes, its format compliance fails.\\n\\n## Venue Fit Risks\\n\\n1. **Novelty concern**: \\\"CLS > CWM when outputs are complex\\\" is predictable. Mitigation: (a) function-level equivalence is the surprising null result (proves it's NOT trivially easier), (b) phase transition with mechanistic explanation (format collapse, not capacity), (c) error complementarity, (d) systematic controlled comparison methodology.\\n\\n2. **EMNLP vs SE venue**: Process vs outcome supervision parallel (Lightman et al., 2023; Uesato et al., 2022). General NLP methodology insight about classification vs generation scaling.\\n\\n3. **CWM comparison fairness**: 4-8B LoRA vs original 32B. Explicitly scoped as \\\"same-size LoRA comparison.\\\" Limitation strengthens practical guidance.\\n\\n4. **Re-repair null result**: Diagnostic granularity downgraded from core contribution to observation (D155 W3). Efficiency (217× throughput) is the practical benefit; re-repair is future work.\\n\\n## Anticipated Reviewer Concerns\\n\\n| Concern | Mitigation |\\n|---------|------------|\\n| \\\"Limited novelty — obvious that CLS is easier\\\" | Func-level null result proves it's NOT trivially easier; phase transition with mechanistic explanation is the novel finding |\\n| \\\"CWM comparison unfair (≤8B LoRA)\\\" | Explicitly scoped; limitation discussed; practical guidance framing |\\n| \\\"Single-seed repo-level\\\" | Multi-seed replication in progress (3 seeds × 2 models × CLS/TRAJ done, CWM pending) |\\n| \\\"Model-agnostic overclaim\\\" | Direction consistent, magnitude varies. Claim: \\\"robust across tested families\\\" not \\\"model-agnostic\\\" |\\n| \\\"No downstream utility\\\" | Efficiency (217×) + diagnostic signal; re-repair honestly framed as future work |\\n| \\\"Interaction not formally tested\\\" | W5: mixed-effects logistic regression planned after multi-seed data |\\n| \\\"Synthetic mutation validity\\\" | Relative ranking validity > absolute; Andrews/Just coupling hypothesis supports formulation-agnostic shift |\\n\\n## Related Work Additions Needed\\n- Process vs outcome supervision: Lightman et al. 2023, Uesato et al. 2022\\n- CodeRL, AlphaCode, Reflexion (verification-in-the-loop repair)\\n- Predictive mutation testing literature\\n- Aletheia (added per W8)\\n\", \"total_chars\": 5133, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f66cda16-6ba4-4770-a8d4-9237f950e00c",
  "isSidechain": false,
  "promptId": "ec010885-b9c9-4574-b4a8-341b5a1f339a",
  "type": "user",
  "uuid": "0671c6fd-d357-4415-b884-0e91191f1180",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"path\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/paper_framing.md\\\", \\\"content\\\": \\\"# Paper Framing — exec-sim-repair-verifier\\\\n\\\\n## Target Venue\\\\n- Primary: EMNLP 2026 Main (ARR May 25, 2026)\\\\n- Deadline: ARR May 25, 2026\\\\n\\\\n## Framing Evolution\\\\n- **D116 (2026-05-16)**: Pivoted from \\\\\\\"CLS scales where generation fails\\\\\\\" (advocacy) to \\\\\\\"The Formulation Design Space for Neural Code Verification\\\\\\\" (empirical characterization)\\\\n- **D155 (2026-05-20)**: DeepSeek repo-level data confirms CWM collapse is **complexity-dependent** (both models collapse at repo-level), NOT tokenizer-specific. Original D116 claim \\\\\\\"Qwen 93% vs DeepSeek 11.8%\\\\\\\" was function-level only; repo-level shows DeepSeek CWM also 51-74% unparseable.\\\\n- **N4 Reframe**: Function-level equivalence elevated to headline finding; phase transition (func→repo divergence) as differentiating contribution.\\\\n\\\\n## Core Claims (current — post D155/N4 Reframe)\\\\n\\\\n1. **Formulation Equivalence at Function-Level**: CLS, CWM, and TRAJ achieve statistically equivalent accuracy at function-level across two model families (≤1.3pp gap, TOST p=0.007). Per-test CLS provides diagnostic granularity (which tests fail) at comparable accuracy with 217× throughput over CWM, though downstream re-repair benefit is unvalidated (n=44, p=0.42).\\\\n\\\\n2. **Phase Transition: Complexity-Dependent Divergence**: Formulations diverge 19-26pp at repo-level, driven by CWM format collapse (51-74% unparseable outputs, 0% truncation). Direction consistent across both model families; magnitude varies (Qwen3 74% unparseable vs DeepSeek 51% at matched seq_length). This is NOT tokenizer-specific — both models collapse when outputs are long and structured.\\\\n\\\\n3. **Error Complementarity**: CLS and CWM exhibit partial complementarity from different fail-bias degrees (CLS 56.5% FP, CWM 70.3% FP), yielding oracle ensemble 90.63% (+2.80pp over best single model).\\\\n\\\\n## Story Spine (updated)\\\\n\\\\n**Problem**: Execution-free verification for code repair can be formulated as per-test classification (CLS), execution output generation (CWM), or trajectory-level scoring (TRAJ). No controlled comparison exists across these formulations.\\\\n\\\\n**Gap**: Prior work uses different models, data, and compute for each formulation, making comparison impossible. Practitioners lack guidance on when formulation choice matters.\\\\n\\\\n**Our contribution**: First controlled comparison of three formulations across 2 model families, 2 complexity levels, and multiple seeds.\\\\n\\\\n**Headline finding**: Formulation choice is a **phase transition** — irrelevant at function-level (≤1.3pp), critical at repo-level (19-26pp). The mechanism: CWM's O(L) generation tokens become unparseable at repo-level complexity, collapsing to majority-baseline-or-worse accuracy. This pattern is robust across both tested model families.\\\\n\\\\n**Practical implication**: At ≤8B LoRA deployment scale, classification is the safer formulation for repo-level verification. CWM's generation capacity may recover at larger scales (32B+, pre-training on execution traces), but at practical fine-tuning sizes, its format compliance fails.\\\\n\\\\n## Venue Fit Risks\\\\n\\\\n1. **Novelty concern**: \\\\\\\"CLS > CWM when outputs are complex\\\\\\\" is predictable. Mitigation: (a) function-level equivalence is the surprising null result (proves it's NOT trivially easier), (b) phase transition with mechanistic explanation (format collapse, not capacity), (c) error complementarity, (d) systematic controlled comparison methodology.\\\\n\\\\n2. **EMNLP vs SE venue**: Process vs outcome supervision parallel (Lightman et al., 2023; Uesato et al., 2022). General NLP methodology insight about classification vs generation scaling.\\\\n\\\\n3. **CWM comparison fairness**: 4-8B LoRA vs original 32B. Explicitly scoped as \\\\\\\"same-size LoRA comparison.\\\\\\\" Limitation strengthens practical guidance.\\\\n\\\\n4. **Re-repair null result**: Diagnostic granularity downgraded from core contribution to observation (D155 W3). Efficiency (217× throughput) is the practical benefit; re-repair is future work.\\\\n\\\\n## Anticipated Reviewer Concerns\\\\n\\\\n| Concern | Mitigation |\\\\n|---------|------------|\\\\n| \\\\\\\"Limited novelty — obvious that CLS is easier\\\\\\\" | Func-level null result proves it's NOT trivially easier; phase transition with mechanistic explanation is the novel finding |\\\\n| \\\\\\\"CWM comparison unfair (≤8B LoRA)\\\\\\\" | Explicitly scoped; limitation discussed; practical guidance framing |\\\\n| \\\\\\\"Single-seed repo-level\\\\\\\" | Multi-seed replication in progress (3 seeds × 2 models × CLS/TRAJ done, CWM pending) |\\\\n| \\\\\\\"Model-agnostic overclaim\\\\\\\" | Direction consistent, magnitude varies. Claim: \\\\\\\"robust across tested families\\\\\\\" not \\\\\\\"model-agnostic\\\\\\\" |\\\\n| \\\\\\\"No downstream utility\\\\\\\" | Efficiency (217×) + diagnostic signal; re-repair honestly framed as future work |\\\\n| \\\\\\\"Interaction not formally tested\\\\\\\" | W5: mixed-effects logistic regression planned after multi-seed data |\\\\n| \\\\\\\"Synthetic mutation validity\\\\\\\" | Relative ranking validity > absolute; Andrews/Just coupling hypothesis supports formulation-agnostic shift |\\\\n\\\\n## Related Work Additions Needed\\\\n- Process vs outcome supervision: Lightman et al. 2023, Uesato et al. 2022\\\\n- CodeRL, AlphaCode, Reflexion (verification-in-the-loop repair)\\\\n- Predictive mutation testing literature\\\\n- Aletheia (added per W8)\\\\n\\\", \\\"total_chars\\\": 5133, \\\"truncated\\\": false}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/paper_framing.md\", \"content\": \"# Paper Framing — exec-sim-repair-verifier\\n\\n## Target Venue\\n- Primary: EMNLP 2026 Main (ARR May 25, 2026)\\n- Deadline: ARR May 25, 2026\\n\\n## Framing Evolution\\n- **D116 (2026-05-16)**: Pivoted from \\\"CLS scales where generation fails\\\" (advocacy) to \\\"The Formulation Design Space for Neural Code Verification\\\" (empirical characterization)\\n- **D155 (2026-05-20)**: DeepSeek repo-level data confirms CWM collapse is **complexity-dependent** (both models collapse at repo-level), NOT tokenizer-specific. Original D116 claim \\\"Qwen 93% vs DeepSeek 11.8%\\\" was function-level only; repo-level shows DeepSeek CWM also 51-74% unparseable.\\n- **N4 Reframe**: Function-level equivalence elevated to headline finding; phase transition (func→repo divergence) as differentiating contribution.\\n\\n## Core Claims (current — post D155/N4 Reframe)\\n\\n1. **Formulation Equivalence at Function-Level**: CLS, CWM, and TRAJ achieve statistically equivalent accuracy at function-level across two model families (≤1.3pp gap, TOST p=0.007). Per-test CLS provides diagnostic granularity (which tests fail) at comparable accuracy with 217× throughput over CWM, though downstream re-repair benefit is unvalidated (n=44, p=0.42).\\n\\n2. **Phase Transition: Complexity-Dependent Divergence**: Formulations diverge 19-26pp at repo-level, driven by CWM format collapse (51-74% unparseable outputs, 0% truncation). Direction consistent across both model families; magnitude varies (Qwen3 74% unparseable vs DeepSeek 51% at matched seq_length). This is NOT tokenizer-specific — both models collapse when outputs are long and structured.\\n\\n3. **Error Complementarity**: CLS and CWM exhibit partial complementarity from different fail-bias degrees (CLS 56.5% FP, CWM 70.3% FP), yielding oracle ensemble 90.63% (+2.80pp over best single model).\\n\\n## Story Spine (updated)\\n\\n**Problem**: Execution-free verification for code repair can be formulated as per-test classification (CLS), execution output generation (CWM), or trajectory-level scoring (TRAJ). No controlled comparison exists across these formulations.\\n\\n**Gap**: Prior work uses different models, data, and compute for each formulation, making comparison impossible. Practitioners lack guidance on when formulation choice matters.\\n\\n**Our contribution**: First controlled comparison of three formulations across 2 model families, 2 complexity levels, and multiple seeds.\\n\\n**Headline finding**: Formulation choice is a **phase transition** — irrelevant at function-level (≤1.3pp), critical at repo-level (19-26pp). The mechanism: CWM's O(L) generation tokens become unparseable at repo-level complexity, collapsing to majority-baseline-or-worse accuracy. This pattern is robust across both tested model families.\\n\\n**Practical implication**: At ≤8B LoRA deployment scale, classification is the safer formulation for repo-level verification. CWM's generation capacity may recover at larger scales (32B+, pre-training on execution traces), but at practical fine-tuning sizes, its format compliance fails.\\n\\n## Venue Fit Risks\\n\\n1. **Novelty concern**: \\\"CLS > CWM when outputs are complex\\\" is predictable. Mitigation: (a) function-level equivalence is the surprising null result (proves it's NOT trivially easier), (b) phase transition with mechanistic explanation (format collapse, not capacity), (c) error complementarity, (d) systematic controlled comparison methodology.\\n\\n2. **EMNLP vs SE venue**: Process vs outcome supervision parallel (Lightman et al., 2023; Uesato et al., 2022). General NLP methodology insight about classification vs generation scaling.\\n\\n3. **CWM comparison fairness**: 4-8B LoRA vs original 32B. Explicitly scoped as \\\"same-size LoRA comparison.\\\" Limitation strengthens practical guidance.\\n\\n4. **Re-repair null result**: Diagnostic granularity downgraded from core contribution to observation (D155 W3). Efficiency (217× throughput) is the practical benefit; re-repair is future work.\\n\\n## Anticipated Reviewer Concerns\\n\\n| Concern | Mitigation |\\n|---------|------------|\\n| \\\"Limited novelty — obvious that CLS is easier\\\" | Func-level null result proves it's NOT trivially easier; phase transition with mechanistic explanation is the novel finding |\\n| \\\"CWM comparison unfair (≤8B LoRA)\\\" | Explicitly scoped; limitation discussed; practical guidance framing |\\n| \\\"Single-seed repo-level\\\" | Multi-seed replication in progress (3 seeds × 2 models × CLS/TRAJ done, CWM pending) |\\n| \\\"Model-agnostic overclaim\\\" | Direction consistent, magnitude varies. Claim: \\\"robust across tested families\\\" not \\\"model-agnostic\\\" |\\n| \\\"No downstream utility\\\" | Efficiency (217×) + diagnostic signal; re-repair honestly framed as future work |\\n| \\\"Interaction not formally tested\\\" | W5: mixed-effects logistic regression planned after multi-seed data |\\n| \\\"Synthetic mutation validity\\\" | Relative ranking validity > absolute; Andrews/Just coupling hypothesis supports formulation-agnostic shift |\\n\\n## Related Work Additions Needed\\n- Process vs outcome supervision: Lightman et al. 2023, Uesato et al. 2022\\n- CodeRL, AlphaCode, Reflexion (verification-in-the-loop repair)\\n- Predictive mutation testing literature\\n- Aletheia (added per W8)\\n\", \"total_chars\": 5133, \"truncated\": false}, \"error\": null, \"metadata\": {}}"
    }
  },
  "sourceToolAssistantUUID": "f66cda16-6ba4-4770-a8d4-9237f950e00c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier",
  "sessionId": "8c11e549-46d3-438b-848f-c86f519fca39",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-22T19:18:57.115Z_

<details><summary>↩ Tool result · `toolu_01EuSZuywfjZYE63WwLqY7Li`</summary>

```text
1	\section{Introduction}
2	\label{sec:introduction}
3	
4	LLM-based automated program repair systems increasingly rely on test-time compute scaling: generating $K$ candidate patches and selecting the best via a verifier~\cite{snell2024scaling}. Full execution verification is reliable but expensive (\$1--3 per candidate at repository scale\footnote{Based on per-instance costs reported by \citet{yang2024sweagent} and \citet{xia2024agentless}.}), driving demand for execution-free alternatives. Three distinct formulations have emerged for this task: \textbf{generation-based simulation}~\cite{meta2025cwm,maimon2026selfexecution} predicts execution output strings per test; \textbf{trajectory-level scoring}~\cite{shum2025swerm} predicts a binary patch verdict without per-test decomposition; and \textbf{per-test classification}~\cite{ni2023lever,chen2023codet} predicts a pass/fail token per test. Each makes different tradeoffs between diagnostic granularity, output complexity, and inference cost.
5	
6	Despite active development along each axis, no prior work provides a systematic comparison holding model capacity, training data, and compute constant. Practitioners choosing a formulation for their verification pipeline must rely on results from different models, different datasets, and different evaluation protocols. Whether one formulation is uniformly preferable, or whether the choice depends on properties of the code being verified, remains an open empirical question. A related question is whether formulation choice matters at all relative to more basic decisions: at what complexity level does fine-tuning become necessary, and does formulation selection add value beyond what fine-tuning alone provides?
7	
8	We present the first systematic empirical comparison across two representative code LLM families (Qwen3, DeepSeek-Coder), two complexity levels (function-level and repository-level), and multiple seeds. Our contribution is primarily methodological: a matched experimental framework that isolates formulation effects from confounding variables. The analysis also produces actionable outputs: a failure mode taxonomy that characterizes when and why each formulation fails (\S\ref{sec:repo}), error complementarity findings with practical ensemble implications (\S\ref{sec:analysis}), and formulation selection recommendations conditioned on code complexity (\S\ref{sec:conclusion}). The results reveal a three-layer structure. Fine-tuning is necessary (0-shot$\to$fine-tuned gains of 35--36\pp{} at repo level). After fine-tuning, \emph{formulation choice is moderated by code complexity}: at function level, all formulations achieve comparable accuracy---consistent with the theoretical analysis in \S\ref{sec:failure-modes}, which predicts that short outputs minimize generation-specific failures. At repository level under our ${\leq}$8B LoRA protocol, this equivalence collapses; variant-level analysis reveals three distinct failure modes consistent across model families, though gap magnitude depends on multiple confounds (\S\ref{sec:threats}). Figure~\ref{fig:reformulation} illustrates the three formulations.
9	
10	We make the following contributions:
11	
12	\begin{itemize}[leftmargin=*,itemsep=2pt]
13	\item \textbf{Complexity-moderated formulation choice.} We establish a three-layer structure: (1)~fine-tuning is necessary (35--36\pp{} gains); (2)~at function level, formulations are near-equivalent---\cls{} and \cwm{} achieve statistical equivalence (TOST $p{=}0.007$, Holm-corrected) across both families, while \traj{} equivalence is not confirmed after multiple comparison correction; (3)~at repository level under ${\leq}$8B LoRA, this equivalence collapses ($z{=}-23.7$, DeepSeek-Coder), with \cwm{} falling 18--26\pp{} below \cls{}, driven by format collapse---four interventions all fail to close the gap. The TOST framework demonstrates strict equivalence rather than mere non-significance (\S\ref{sec:equivalence}, \S\ref{sec:repo}).
14	
15	\item \textbf{Error complementarity.} \cls{} and \cwm{} exhibit partially complementary error patterns at function level (oracle: 90.63\%, 95\% CI [89.3\%, 91.9\%]; single-seed); at repo level, oracle routing reaches 95.83\% variant accuracy (+14.58\pp{}; single-seed), the strongest practical argument for exploring formulation-level tradeoffs (\S\ref{sec:analysis}).
16	\end{itemize}
17	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "16568425-32b9-4893-b460-d3128b6d3a95",
  "isSidechain": false,
  "promptId": "ec010885-b9c9-4574-b4a8-341b5a1f339a",
  "type": "user",
  "uuid": "69660d26-854c-4c1f-8dad-da6d2fa368da",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/introduction.tex",
      "content": "\\section{Introduction}\n\\label{sec:introduction}\n\nLLM-based automated program repair systems increasingly rely on test-time compute scaling: generating $K$ candidate patches and selecting the best via a verifier~\\cite{snell2024scaling}. Full execution verification is reliable but expensive (\\$1--3 per candidate at repository scale\\footnote{Based on per-instance costs reported by \\citet{yang2024sweagent} and \\citet{xia2024agentless}.}), driving demand for execution-free alternatives. Three distinct formulations have emerged for this task: \\textbf{generation-based simulation}~\\cite{meta2025cwm,maimon2026selfexecution} predicts execution output strings per test; \\textbf{trajectory-level scoring}~\\cite{shum2025swerm} predicts a binary patch verdict without per-test decomposition; and \\textbf{per-test classification}~\\cite{ni2023lever,chen2023codet} predicts a pass/fail token per test. Each makes different tradeoffs between diagnostic granularity, output complexity, and inference cost.\n\nDespite active development along each axis, no prior work provides a systematic comparison holding model capacity, training data, and compute constant. Practitioners choosing a formulation for their verification pipeline must rely on results from different models, different datasets, and different evaluation protocols. Whether one formulation is uniformly preferable, or whether the choice depends on properties of the code being verified, remains an open empirical question. A related question is whether formulation choice matters at all relative to more basic decisions: at what complexity level does fine-tuning become necessary, and does formulation selection add value beyond what fine-tuning alone provides?\n\nWe present the first systematic empirical comparison across two representative code LLM families (Qwen3, DeepSeek-Coder), two complexity levels (function-level and repository-level), and multiple seeds. Our contribution is primarily methodological: a matched experimental framework that isolates formulation effects from confounding variables. The analysis also produces actionable outputs: a failure mode taxonomy that characterizes when and why each formulation fails (\\S\\ref{sec:repo}), error complementarity findings with practical ensemble implications (\\S\\ref{sec:analysis}), and formulation selection recommendations conditioned on code complexity (\\S\\ref{sec:conclusion}). The results reveal a three-layer structure. Fine-tuning is necessary (0-shot$\\to$fine-tuned gains of 35--36\\pp{} at repo level). After fine-tuning, \\emph{formulation choice is moderated by code complexity}: at function level, all formulations achieve comparable accuracy---consistent with the theoretical analysis in \\S\\ref{sec:failure-modes}, which predicts that short outputs minimize generation-specific failures. At repository level under our ${\\leq}$8B LoRA protocol, this equivalence collapses; variant-level analysis reveals three distinct failure modes consistent across model families, though gap magnitude depends on multiple confounds (\\S\\ref{sec:threats}). Figure~\\ref{fig:reformulation} illustrates the three formulations.\n\nWe make the following contributions:\n\n\\begin{itemize}[leftmargin=*,itemsep=2pt]\n\\item \\textbf{Complexity-moderated formulation choice.} We establish a three-layer structure: (1)~fine-tuning is necessary (35--36\\pp{} gains); (2)~at function level, formulations are near-equivalent---\\cls{} and \\cwm{} achieve statistical equivalence (TOST $p{=}0.007$, Holm-corrected) across both families, while \\traj{} equivalence is not confirmed after multiple comparison correction; (3)~at repository level under ${\\leq}$8B LoRA, this equivalence collapses ($z{=}-23.7$, DeepSeek-Coder), with \\cwm{} falling 18--26\\pp{} below \\cls{}, driven by format collapse---four interventions all fail to close the gap. The TOST framework demonstrates strict equivalence rather than mere non-significance (\\S\\ref{sec:equivalence}, \\S\\ref{sec:repo}).\n\n\\item \\textbf{Error complementarity.} \\cls{} and \\cwm{} exhibit partially complementary error patterns at function level (oracle: 90.63\\%, 95\\% CI [89.3\\%, 91.9\\%]; single-seed); at repo level, oracle routing reaches 95.83\\% variant accuracy (+14.58\\pp{}; single-seed), the strongest practical argument for exploring formulation-level tradeoffs (\\S\\ref{sec:analysis}).\n\\end{itemize}\n",
      "numLines": 17,
      "startLine": 1,
      "totalLines": 17
    }
  },
  "sourceToolAssistantUUID": "16568425-32b9-4893-b460-d3128b6d3a95",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier",
  "sessionId": "8c11e549-46d3-438b-848f-c86f519fca39",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-22T19:18:57.603Z_

<details open><summary>🔧 Tool call — Read · `toolu_01RMkbhMyeox2M3sJxr2iv6b`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "69660d26-854c-4c1f-8dad-da6d2fa368da",
  "isSidechain": false,
  "requestId": "req_011CbJ9UoRFm2GRjSasNgqwg",
  "type": "assistant",
  "uuid": "9a2a42d2-4eab-42c8-a9b1-7fed11a43c31",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier",
  "sessionId": "8c11e549-46d3-438b-848f-c86f519fca39",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01U16PPjqHqZa23X2kRksyjc",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 614,
      "cache_read_input_tokens": 24786,
      "output_tokens": 748,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 614,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 748,
          "cache_read_input_tokens": 24786,
          "cache_creation_input_tokens": 614,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 614
          },
          "type": "message"
        }
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

_source line 22 · 2026-05-22T19:18:57.608Z_

<details><summary>↩ Tool result · `toolu_01RMkbhMyeox2M3sJxr2iv6b`</summary>

```text
1	\section{Method}
2	\label{sec:method}
3	
4	Let $p$ denote a candidate patch and $T = \{t_1, \ldots, t_n\}$ its test suite, where each $t_i$ has label $y_i \in \{\text{\textsc{Pass}}, \text{\textsc{Fail}}\}$ from execution. Tests decompose into \emph{fail-to-pass} ($T_{\text{f2p}}$) and \emph{pass-to-pass} ($T_{\text{p2p}}$) subsets; a patch is correct iff $\forall\, t_i{:}\ y_i = \text{\textsc{Pass}}$. We compare three formulations for predicting correctness without execution.
5	
6	\subsection{Verification Formulations}
7	\label{sec:formulations}
8	
9	Let $c_p$ denote the code context (unified diff) of patch $p$.
10	
11	\paragraph{\cls{} (per-test classification).} $f(c_p, t_i) \rightarrow \hat{y}_i \in \{\text{\textsc{Pass}}, \text{\textsc{Fail}}\}$ predicts a single binary token per test (cross-entropy loss). Patch verdict: $\hat{y}_p = \bigwedge_{i} [\hat{y}_i = \text{\textsc{Pass}}]$. Output cost: one token per test.
12	
13	\paragraph{\cwm{} (output generation).} $g(c_p, t_i) \rightarrow \hat{o}_i \in \Sigma^*$ generates the execution output string (language modeling loss). Verdict by exact match: $\hat{y}_i = \text{\textsc{Pass}}$ iff $\hat{o}_i = o_i^*$.\footnote{Exact string matching is conservative, consistent with \citet{meta2025cwm}. Semantic equivalences are not counted.} When the generated output is unparseable (i.e., does not conform to the expected structured format), the prediction defaults to the majority class verdict. Output cost: $\sum_i |\hat{o}_i|$ tokens.
14	
15	\paragraph{\traj{} (trajectory-level).} $h(c_p, T) \rightarrow \hat{y}_p \in \{\text{\textsc{Resolved}}, \text{\textsc{Unresolved}}\}$ predicts a single patch verdict from all tests and provides no per-test signal. \traj{} serves as a granularity control: \cls{}--\traj{} differences isolate the value of per-test decomposition independent of the classification formulation itself.
16	
17	\subsection{Formulation-Specific Failure Modes}
18	\label{sec:failure-modes}
19	
20	Each formulation has characteristic failure modes that differ in their sensitivity to code complexity:
21	
22	\paragraph{Generation failure modes (\cwm{}).} The open-ended output space introduces three failure modes: (1)~\emph{token-budget exhaustion}, where $|o_i^*| > B$ guarantees exact-match failure due to truncation; (2)~\emph{string-value prediction errors}, where semantically equivalent outputs differing in surface form (floating-point precision, dictionary ordering) produce false negatives; and (3)~\emph{format compliance collapse}, where the model fails to produce structured predictions entirely at high input complexity, even when the generation budget is sufficient. Under optimistic independence, a token sequence of length $L$ with per-token accuracy $q$ has correct-sequence probability $q^L$; long outputs are therefore exponentially harder to predict exactly. We adopt exact string matching following the original \cwm{} evaluation protocol~\citep{meta2025cwm}. Unparseable predictions default to the majority-class label (\textsc{Pass}).
23	
24	\paragraph{Classification failure modes (\cls{}).} The single-token output space eliminates format and truncation failures but constrains the model to encode its reasoning entirely within internal representations, without the intermediate reasoning trace that generation provides. \cls{} errors manifest as false positives or false negatives without format failures; at function level, a mild FP bias (56.5\%) emerges, with the error direction depending on class distribution and fine-tuning dynamics.
25	
26	\paragraph{Trajectory-level failure modes (\traj{}).} By collapsing all per-test information into a single binary verdict, \traj{} discards diagnostic granularity. When a patch fails multiple tests, the trajectory-level formulation cannot identify \emph{which} tests fail. This limits downstream utility (e.g., targeted re-repair) but avoids per-test aggregation errors.
27	
28	\paragraph{Complexity dependence.} These failure modes suggest a complexity-dependent interaction: when execution outputs are short and structured (function-level code), generation modes (1)--(2) are rarely triggered, and all formulations should perform comparably. As output length and structural complexity increase (repository-level code), generation-specific failures may compound, creating divergence. Whether this divergence reflects a fundamental property of the generation formulation or is contingent on model/tokenizer properties is an empirical question we investigate in \S\ref{sec:experiments}.
29	
30	\subsection{Oracle Accuracy-Utility Framework}
31	\label{sec:oracle}
32	
33	For a buggy patch with $k = |T_{\text{f2p}}|$ fail-to-pass tests, a per-test verifier with recall $r$ detects the bug if it identifies at least one failing test: $P_{\text{detect}}(k) = 1 - (1 - r)^{k_{\text{eff}}}$, where $k_{\text{eff}} = k / (1 + (k-1)\rho)$ accounts for within-patch correlation via ICC $\rho$~\citep{shrout1979icc}. The per-test advantage over a trajectory-level baseline ($a_h$) is $\Delta(k) = P_{\text{detect}}(k) - a_h$, with population expectation $\mathbb{E}[\Delta] = \sum_{k} P(|T_{\text{f2p}}| = k) \cdot \Delta(k)$. This predicts that per-test advantage concentrates in multi-F2P-test instances and vanishes at $k{=}1$, validated in \S\ref{sec:experiments} and Appendix~\ref{app:oracle}.
34	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9a2a42d2-4eab-42c8-a9b1-7fed11a43c31",
  "isSidechain": false,
  "promptId": "ec010885-b9c9-4574-b4a8-341b5a1f339a",
  "type": "user",
  "uuid": "4494a498-930d-4ef3-bfd2-dbdcdc9b2937",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/method.tex",
      "content": "\\section{Method}\n\\label{sec:method}\n\nLet $p$ denote a candidate patch and $T = \\{t_1, \\ldots, t_n\\}$ its test suite, where each $t_i$ has label $y_i \\in \\{\\text{\\textsc{Pass}}, \\text{\\textsc{Fail}}\\}$ from execution. Tests decompose into \\emph{fail-to-pass} ($T_{\\text{f2p}}$) and \\emph{pass-to-pass} ($T_{\\text{p2p}}$) subsets; a patch is correct iff $\\forall\\, t_i{:}\\ y_i = \\text{\\textsc{Pass}}$. We compare three formulations for predicting correctness without execution.\n\n\\subsection{Verification Formulations}\n\\label{sec:formulations}\n\nLet $c_p$ denote the code context (unified diff) of patch $p$.\n\n\\paragraph{\\cls{} (per-test classification).} $f(c_p, t_i) \\rightarrow \\hat{y}_i \\in \\{\\text{\\textsc{Pass}}, \\text{\\textsc{Fail}}\\}$ predicts a single binary token per test (cross-entropy loss). Patch verdict: $\\hat{y}_p = \\bigwedge_{i} [\\hat{y}_i = \\text{\\textsc{Pass}}]$. Output cost: one token per test.\n\n\\paragraph{\\cwm{} (output generation).} $g(c_p, t_i) \\rightarrow \\hat{o}_i \\in \\Sigma^*$ generates the execution output string (language modeling loss). Verdict by exact match: $\\hat{y}_i = \\text{\\textsc{Pass}}$ iff $\\hat{o}_i = o_i^*$.\\footnote{Exact string matching is conservative, consistent with \\citet{meta2025cwm}. Semantic equivalences are not counted.} When the generated output is unparseable (i.e., does not conform to the expected structured format), the prediction defaults to the majority class verdict. Output cost: $\\sum_i |\\hat{o}_i|$ tokens.\n\n\\paragraph{\\traj{} (trajectory-level).} $h(c_p, T) \\rightarrow \\hat{y}_p \\in \\{\\text{\\textsc{Resolved}}, \\text{\\textsc{Unresolved}}\\}$ predicts a single patch verdict from all tests and provides no per-test signal. \\traj{} serves as a granularity control: \\cls{}--\\traj{} differences isolate the value of per-test decomposition independent of the classification formulation itself.\n\n\\subsection{Formulation-Specific Failure Modes}\n\\label{sec:failure-modes}\n\nEach formulation has characteristic failure modes that differ in their sensitivity to code complexity:\n\n\\paragraph{Generation failure modes (\\cwm{}).} The open-ended output space introduces three failure modes: (1)~\\emph{token-budget exhaustion}, where $|o_i^*| > B$ guarantees exact-match failure due to truncation; (2)~\\emph{string-value prediction errors}, where semantically equivalent outputs differing in surface form (floating-point precision, dictionary ordering) produce false negatives; and (3)~\\emph{format compliance collapse}, where the model fails to produce structured predictions entirely at high input complexity, even when the generation budget is sufficient. Under optimistic independence, a token sequence of length $L$ with per-token accuracy $q$ has correct-sequence probability $q^L$; long outputs are therefore exponentially harder to predict exactly. We adopt exact string matching following the original \\cwm{} evaluation protocol~\\citep{meta2025cwm}. Unparseable predictions default to the majority-class label (\\textsc{Pass}).\n\n\\paragraph{Classification failure modes (\\cls{}).} The single-token output space eliminates format and truncation failures but constrains the model to encode its reasoning entirely within internal representations, without the intermediate reasoning trace that generation provides. \\cls{} errors manifest as false positives or false negatives without format failures; at function level, a mild FP bias (56.5\\%) emerges, with the error direction depending on class distribution and fine-tuning dynamics.\n\n\\paragraph{Trajectory-level failure modes (\\traj{}).} By collapsing all per-test information into a single binary verdict, \\traj{} discards diagnostic granularity. When a patch fails multiple tests, the trajectory-level formulation cannot identify \\emph{which} tests fail. This limits downstream utility (e.g., targeted re-repair) but avoids per-test aggregation errors.\n\n\\paragraph{Complexity dependence.} These failure modes suggest a complexity-dependent interaction: when execution outputs are short and structured (function-level code), generation modes (1)--(2) are rarely triggered, and all formulations should perform comparably. As output length and structural complexity increase (repository-level code), generation-specific failures may compound, creating divergence. Whether this divergence reflects a fundamental property of the generation formulation or is contingent on model/tokenizer properties is an empirical question we investigate in \\S\\ref{sec:experiments}.\n\n\\subsection{Oracle Accuracy-Utility Framework}\n\\label{sec:oracle}\n\nFor a buggy patch with $k = |T_{\\text{f2p}}|$ fail-to-pass tests, a per-test verifier with recall $r$ detects the bug if it identifies at least one failing test: $P_{\\text{detect}}(k) = 1 - (1 - r)^{k_{\\text{eff}}}$, where $k_{\\text{eff}} = k / (1 + (k-1)\\rho)$ accounts for within-patch correlation via ICC $\\rho$~\\citep{shrout1979icc}. The per-test advantage over a trajectory-level baseline ($a_h$) is $\\Delta(k) = P_{\\text{detect}}(k) - a_h$, with population expectation $\\mathbb{E}[\\Delta] = \\sum_{k} P(|T_{\\text{f2p}}| = k) \\cdot \\Delta(k)$. This predicts that per-test advantage concentrates in multi-F2P-test instances and vanishes at $k{=}1$, validated in \\S\\ref{sec:experiments} and Appendix~\\ref{app:oracle}.\n",
      "numLines": 34,
      "startLine": 1,
      "totalLines": 34
    }
  },
  "sourceToolAssistantUUID": "9a2a42d2-4eab-42c8-a9b1-7fed11a43c31",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier",
  "sessionId": "8c11e549-46d3-438b-848f-c86f519fca39",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-22T19:18:58.086Z_

<details open><summary>🔧 Tool call — Read · `toolu_019zn7rA6Y6CGDXrmdLovbbU`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4494a498-930d-4ef3-bfd2-dbdcdc9b2937",
  "isSidechain": false,
  "requestId": "req_011CbJ9UoRFm2GRjSasNgqwg",
  "type": "assistant",
  "uuid": "a498599e-6fac-4be6-b6dd-48f90d843026",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier",
  "sessionId": "8c11e549-46d3-438b-848f-c86f519fca39",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01U16PPjqHqZa23X2kRksyjc",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 614,
      "cache_read_input_tokens": 24786,
      "output_tokens": 748,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 614,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 748,
          "cache_read_input_tokens": 24786,
          "cache_creation_input_tokens": 614,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 614
          },
          "type": "message"
        }
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

_source line 24 · 2026-05-22T19:18:58.095Z_

<details><summary>↩ Tool result · `toolu_019zn7rA6Y6CGDXrmdLovbbU`</summary>

```text
1	\section{Experiments}
2	\label{sec:experiments}
3	
4	We systematically compare \cls{}, \cwm{}, and \traj{} across two representative code LLM families, two complexity levels, and multiple seeds to characterize the formulation landscape for neural code verification.
5	
6	\subsection{Experimental Setup}
7	\label{sec:setup}
8	
9	\paragraph{Datasets.}
10	\emph{Function-level}: mutated variants from HumanEval~\cite{chen2021humaneval} and MBPP~\cite{austin2021mbpp} (five mutation types), labels verified by execution. 19,076 samples (train 15,290 / val 1,896 / test 1,890; pass:fail $\approx$ 52:48, majority baseline 51.75\%).
11	\emph{Repo-level}: per-test instances from SWE-bench Verified~\cite{chowdhury2024swebenchverified} mutants. ${\sim}$70K training samples; val ($n{=}9{,}335$) and test ($n{=}9{,}784$) have zero problem overlap (majority baseline 72.96\%). Val-based checkpoint selection follows standard practice~\cite{jimenez2024swebench} where validation loss is computable; runs using truncate preprocessing produce NaN validation loss because repo-level execution traces often exceed the 2,048-token sequence length limit; after truncation, many samples have all target tokens removed (labels entirely $-$100), producing degenerate loss---a formulation-inherent weakness that classification and trajectory formulations avoid by design. NaN loss defaults to the final epoch checkpoint (affects DeepSeek \cls{} s123, all \cwm{} runs, and Qwen3 \traj{} runs; see Appendix~\ref{app:hyperparams}).
12	
13	\paragraph{Models and training.}
14	We fine-tune Qwen3-4B and Qwen3-8B~\cite{qwen2025qwen3} with Low-Rank Adaptation (LoRA)~\cite{hu2022lora} (rank 16, 3 epochs) across five seeds. Seeds 42/123/456 use bfloat16; seeds 789/0 use NormalFloat 4-bit (NF4) quantization~\cite{dettmers2024qlora} to test robustness to precision reduction (function-level accuracy remains within seed noise across both precisions; see footnote in \S\ref{sec:equivalence}). As a cross-model consistency check, we additionally fine-tune DeepSeek-Coder-6.7B~\cite{guo2024deepseekcoder} with identical LoRA configuration (2 seeds each for \cls{} and \cwm{}). Our \cwm{} baseline is a LoRA fine-tuned variant for matched comparison, not a reproduction of the 32B Code World Model~\cite{meta2025cwm}. Repo-level models use val-selected checkpoints where available; runs with NaN validation loss use the final epoch checkpoint (Appendix~\ref{app:hyperparams}). Zero-shot baselines use Qwen3-8B and Qwen3-32B (NF4) as LLM-as-judge. Full hyperparameter details appear in Appendix~\ref{app:hyperparams}.
15	
16	\paragraph{Statistics.}
17	Confidence intervals use clustered bootstrap~\cite{davison1997bootstrap} (114 problem clusters, 10K resamples; we resample entire problems, not individual tests, to preserve within-problem correlations); per-test vs.\ trajectory-level equivalence uses Two One-Sided Tests (TOST)~\cite{schuirmann1987tost} with $\pm$2 percentage point (\pp{}) margin. Holm-Bonferroni correction~\cite{holm1979} controls family-wise error rate across the five primary comparisons (Table~\ref{tab:holm}). Intraclass correlation coefficient (ICC)~\cite{shrout1979icc} quantifies within-problem correlation. Variant-level effect sizes and statistical power analysis are reported in Appendix~\ref{app:power}. Oracle analysis uses SWE-bench Verified (500 instances).
18	
19	
20	\subsection{Function-Level Results}
21	\label{sec:func_results}
22	
23	Table~\ref{tab:main_results} reports function-level results across formulations and model families.
24	
25	\begin{table}[t]
26	\centering
27	\small
28	\caption{Function-level per-test accuracy on HumanEval+MBPP ($n{=}1{,}890$). Mean $\pm$ std over seeds. Seeds 42/123/456: bfloat16; 789/0: NF4. DeepSeek: $n{=}2$ seeds; std reported for descriptive comparison, not inferential. \traj{} evaluated on 1,032-sample subset (447 matched variants).}
29	\label{tab:main_results}
30	\resizebox{\columnwidth}{!}{%
31	\setlength{\tabcolsep}{4pt}
32	\begin{tabular}{llcc}
33	\toprule
34	\textbf{Method} & \textbf{Model} & \textbf{Seeds} & \textbf{Accuracy (\%)} \\
35	\midrule
36	\multicolumn{4}{l}{\emph{Qwen3 (primary)}} \\
37	\cls{} (fine-tuned) & 4B & 5 & \textbf{88.43 $\pm$ 0.78} \\
38	\cwm{} (fine-tuned) & 4B & 5 & \underline{87.19 $\pm$ 0.37} \\
39	\traj{} (fine-tuned) & 4B & 5 & 86.30 $\pm$ 0.97 \\
40	\midrule
41	\multicolumn{4}{l}{\emph{DeepSeek-Coder (cross-model consistency check)}} \\
42	\cls{} (fine-tuned) & 6.7B & 2 & \textbf{86.85 $\pm$ 0.11} \\
43	\cwm{} (fine-tuned) & 6.7B & 2 & \underline{86.83 $\pm$ 1.49} \\
44	\traj{} (fine-tuned) & 6.7B & 2 & 84.16 $\pm$ 1.30 \\
45	\midrule
46	\multicolumn{4}{l}{\emph{Prompting baselines}} \\
47	0-shot & 8B (Qwen3) & 1 & 68.70 \\
48	0-shot & 6.7B (DeepSeek) & 1 & 63.00 \\
49	ZS LLM-as-judge & 8B (Qwen3) & 1 & 64.40 \\
50	ZS LLM-as-judge & 6.7B (DeepSeek) & 1 & 56.56 \\
51	ZS LLM-as-judge & 32B (NF4) & 1 & 71.69 \\
52	3-shot ICL & 8B (Qwen3) & 1 & 68.78 \\
53	3-shot ICL & 6.7B (DeepSeek) & 1 & 59.95 \\
54	\midrule
55	Majority (pass) & --- & --- & 51.75 \\
56	\bottomrule
57	\end{tabular}}
58	\end{table}
59	
60	All three formulations achieve comparable accuracy on Qwen3-4B: \cls{} 88.43\% ($\pm$0.78), \cwm{} 87.19\% ($\pm$0.37), \traj{} 86.30\% ($\pm$0.97). DeepSeek-Coder-6.7B shows: \cls{} 86.85\%, \cwm{} 86.83\%, \traj{} 84.16\%. The \cls{}--\cwm{} gap (0.02--1.24\pp{}) is within seed noise in both families. However, the \cls{}--\traj{} gap is model-dependent: $<$1\pp{} on Qwen3 but 2.69\pp{} on DeepSeek-Coder, exceeding the $\pm$2\pp{} equivalence margin (\S\ref{sec:equivalence}). \cls{} and \cwm{} are robustly equivalent; \traj{} parity is model-contingent. Zero-shot baselines (Tables~\ref{tab:main_results} and~\ref{tab:repo_level}) establish that repo-level verification requires fine-tuning (0-shot$\to$fine-tuned gains of 35--36\pp{}) and that formulation choice matters only at repo level (\cls{} outperforms \cwm{} by 18--26\pp{}).
61	
62	
63	\subsection{Scaling Behavior}
64	\label{sec:scaling}
65	
66	Beyond overall accuracy, we examine whether formulation ranking is stable across model sizes. Table~\ref{tab:scaling} compares all three formulations at 4B and 8B using seeds 42 and 123 in full bfloat16 precision (excluding NF4 seeds to isolate the size effect).
67	
68	\begin{table}[t]
69	\centering
70	\small
71	\caption{Model-size scaling: accuracy (\%) at 4B and 8B (Qwen3, seeds 42/123, full bfloat16 precision). \cls{} and \traj{} scale positively; \cwm{} does not. \cwm{} scaling comparison is exploratory ($n{=}2$ seeds per size).}
72	\label{tab:scaling}
73	\setlength{\tabcolsep}{4pt}
74	\begin{tabular}{llcccc}
75	\toprule
76	\textbf{Method} & \textbf{Size} & \textbf{s42} & \textbf{s123} & \textbf{Mean} & \textbf{$\Delta$ 4B$\to$8B} \\
77	\midrule
78	\cls{} & 4B & 87.83 & 89.52 & \textbf{88.68} & \multirow{2}{*}{+1.27} \\
79	\cls{} & 8B & \textbf{90.48} & 89.40 & \textbf{89.94} & \\
80	\midrule
81	\cwm{} & 4B & 87.51 & 87.20 & \underline{87.36} & \multirow{2}{*}{$-$0.03} \\
82	\cwm{} & 8B & 87.67 & 86.98 & 87.33 & \\
83	\midrule
84	\traj{} & 4B & 85.66 & 85.47 & 85.57 & \multirow{2}{*}{+2.13} \\
85	\traj{} & 8B & 87.60 & 87.79 & \underline{87.70} & \\
86	\bottomrule
87	\end{tabular}
88	\end{table}
89	
90	\cls{} and \traj{} both scale positively from 4B to 8B (+1.27\pp{} and +2.13\pp{} respectively), while \cwm{} remains flat ($-$0.03\pp{}). At 8B, the ranking is \cls{} (89.94) $>$ \traj{} (87.70) $>$ \cwm{} (87.33). The \cls{}--\cwm{} gap widens from 1.32\pp{} at 4B to 2.62\pp{} at 8B (Figure~\ref{fig:scaling_gap}); clustered bootstrap on the 3-seed superset (42, 123, 456 for \cls{}/\cwm{}) yields $p = 0.0066$ (95\% CI $[1.80, 2.71]$), which confirms the widening is not a sampling artifact.
91	
92	\cwm{} flat scaling ($-$0.03\pp{}) may reflect suboptimal hyperparameter transfer at 8B rather than a fundamental limitation; we do not claim generation \emph{cannot} benefit from scale. At function level, outputs are short status strings (e.g., ``PASS'' or brief error messages) and format compliance is near-perfect; at repo level, output complexity increases substantially, and the same generation bottleneck manifests as format collapse patterns we examine in \S\ref{sec:repo}. \traj{} also shows no scaling benefit at repo level (72.92\% at both 4B and 8B); only \cls{} scales positively across both complexity levels.
93	
94	
95	\subsection{Function-Level Equivalence}
96	\label{sec:equivalence}
97	
98	We test pairwise equivalence among formulations on 523 variant-level instances across five seeds.\footnote{Seeds 789 and 0 use NF4 quantized inference; the remaining three use bfloat16. Restricting to bfloat16 seeds only (3 seeds): \cls{}--\cwm{} remains significant ($p{<}0.05$); \cls{}--\traj{} yields $p{=}0.128$, consistent in direction but underpowered due to reduced seed coverage.} Our $\pm$2\pp{} SESOI threshold~\cite{lakens2017,wellek2010} is set a priori based on deployment relevance: at 85--88\% accuracy, a 2\pp{} difference corresponds to ${\sim}$2--3 problems out of 114---below the threshold at which a practitioner would select one formulation over another for pipeline integration. Post hoc, this threshold is consistent with between-seed variation (0.37--0.97\pp{} std, Table~\ref{tab:main_results}) and checkpoint noise ($<$1\pp{}, \S\ref{sec:threats}), confirming that differences within the margin are indistinguishable from training noise. Within-problem predictions are correlated (ICC $= 0.191$, DEFF $= 3.97$~\cite{moulton1990}); all tests use clustered bootstrap.
99	
100	\paragraph{\cls{}--\cwm{} equivalence.} The pooled gap is 1.24\pp{} (88.43\%--87.19\%); TOST confirms equivalence at $p = 0.007$ ($\pm$2\pp{} margin), surviving Holm-Bonferroni correction ($k{=}5$, adjusted $p{=}0.028$; Table~\ref{tab:holm}). Equivalence holds at margins as tight as $\pm$1.52\pp{} (Table~\ref{tab:tost_sensitivity}). On DeepSeek-Coder, the \cls{}--\cwm{} gap of 0.02\pp{} is consistent with equivalence but underpowered (2 seeds).
101	
102	\paragraph{\cls{}--\traj{} equivalence.} The pooled gap is $-$0.45\pp{} (95\% CI [$-$1.71, +0.84]); TOST yields $p = 0.025$ ($\pm$2\pp{}), nominally significant but not surviving Holm-Bonferroni correction ($k{=}5$, adjusted $p{=}0.075$; Table~\ref{tab:holm}). The DeepSeek \cls{}--\traj{} gap (2.69\pp{}) exceeds the $\pm$2\pp{} margin; \traj{} parity is model-dependent. Per-test classification provides diagnostic information (which tests fail) at no cost to variant-level accuracy, paralleling process supervision~\cite{lightman2023letsverify}.
103	
104	\paragraph{Statistical power considerations.} With $n_{\text{eff}} \approx 86$ independent observations after clustering (DEFF $= 3.97$), the TOST at $\pm$2\pp{} achieves power ${\sim}$0.3 for a medium effect size~\cite{cohen1988}---a 70\% probability of failing to confirm equivalence even if the true difference is moderate. The CLS--CWM equivalence ($p{=}0.007$) is robust to this limitation; the CLS--TRAJ non-confirmation ($p{=}0.075$) may reflect insufficient power rather than a genuine difference. A Bayesian ROPE analysis corroborates these conclusions ($P(\text{ROPE}){=}0.975$ for CLS--CWM; Appendix~\ref{app:bayesian_rope}).
105	
106	
107	\subsection{Repo-Level: Complexity-Dependent Divergence}
108	\label{sec:repo}
109	
110	Table~\ref{tab:repo_level} compares formulations at repository-level complexity. Variant-level comparisons ($n{=}48$) are exploratory due to limited seed coverage; the per-test interaction effect is statistically confirmed (see below). Checkpoints are val-selected where validation loss is computable (\S\ref{sec:setup}); the test set has zero problem overlap with validation.
111	
112	\begin{table}[t]
113	\centering
114	\small
115	\caption{Repo-level cross-formulation comparison on SWE-bench Verified test set. Qwen3-8B \cls{}/\traj{}: mean $\pm$ std over 3 seeds; DeepSeek \cls{}: 2 seeds\textsuperscript{$\ddagger$}; DeepSeek \traj{}: 3 seeds; Qwen3-4B: seed 42. \cwm{}: 3 seeds (42/123/456).}
116	\label{tab:repo_level}
117	\resizebox{\columnwidth}{!}{%
118	\setlength{\tabcolsep}{4pt}
119	\begin{tabular}{lcccc}
120	\toprule
121	\textbf{Model} & \textbf{\cls{} (\%)} & \textbf{\cls{} Var.\ (\%)} & \textbf{\cwm{} (\%)} & \textbf{\traj{} Var.\ (\%)\textsuperscript{$\diamond$}} \\
122	\midrule
123	Qwen3-4B & 83.63 & 64.58 & 58.04 & 72.92 \\
124	Qwen3-8B & \textbf{84.83 $\pm$ 0.67} & 72.92 / 81.25\textsuperscript{$\dagger$} & 66.48 $\pm$ 1.15 & 72.91 $\pm$ 3.61 \\
125	DeepSeek-6.7B & 84.38 $\pm$ 2.50\textsuperscript{$\ddagger$} & 81.25\textsuperscript{$\dagger$} & 58.30 $\pm$ 2.82 & 77.08 $\pm$ 3.61 \\
126	\midrule
127	0-shot (Qwen3-8B) & 49.90 & --- & --- & --- \\
128	0-shot (DeepSeek) & 48.54 & --- & --- & --- \\
129	Majority & 72.96 & 54.17 & 72.96 & 54.17 \\
130	\bottomrule
131	\end{tabular}}
132	
133	\vspace{2pt}
134	{\footnotesize \textsuperscript{$\dagger$}Individual-seed variant accuracy. \textsuperscript{$\ddagger$}One seed excluded: truncate preprocessing$\to$NaN val loss, decision collapse (Table~\ref{tab:taxonomy}); mean over two matched seeds. \textsuperscript{$\diamond$}Var.\ columns: variant-level accuracy ($n{=}48$); \cls{} aggregated via all-pass rule; \traj{} by design. Per-test: $n{=}9{,}784$. \cwm{} unparseable: 54\% (4B); default to pass; parseable-only 38--43\%, below majority. Eval seq\_length differs across models (Appendix~\ref{app:threats}). \cwm{} uses epoch-3 checkpoint (val loss undefined); see text for checkpoint sensitivity analysis.}
135	\end{table}
136	
137	Few-shot prompting (3-shot ICL) collapses to an always-predict-unresolved baseline (variant accuracy 45.83\%, below majority 54.17\%; Appendix~\ref{app:few_shot}), establishing that execution-free verification requires task-specific fine-tuning regardless of formulation. The fine-tuning requirement (35--36\pp{} gains, Table~\ref{tab:repo_level}) is the first layer of our three-layer structure.
138	
139	\paragraph{Formulation divergence.} Under our 4--8B LoRA protocol, \cls{} and \cwm{} diverge on Qwen3: the gap is 25.59\pp{} at 4B (\cls{} 83.63\% vs.\ \cwm{} 58.04\%, seed 42; Figure~\ref{fig:scaling_gap}) and 18.35\pp{} at 8B (84.83\% vs.\ 66.48\%, 3-seed means). \cwm{} falls below majority baseline at both scales. These gaps confirm complexity-dependent formulation divergence, though limited seed coverage and multiple confounds (\S\ref{sec:threats}) limit definitive causal attribution.
140	
141	\paragraph{Cross-model consistency.} DeepSeek-Coder shows the same direction (\cls{} $>$ \cwm{}) across all seeds, with gap magnitude varying across families (20\pp{} Qwen3 vs.\ 23--28\pp{} DeepSeek), primarily reflecting checkpoint selection sensitivity; under matched epoch-3 checkpoints, the cross-model gap difference narrows to ${\sim}$2\pp{} (Appendix~\ref{app:threats}). Across all six \cwm{} repo-level seeds, every seed exhibits format collapse ($>$50\% unparseable) and parseable-only accuracy below majority baseline, ruling out seed-specific artifacts.
142	
143	\paragraph{Failure mode taxonomy.} Variant-level analysis ($n{=}48$, Appendix Table~\ref{tab:variant_level}) reveals three failure modes (Table~\ref{tab:taxonomy}): format collapse (\cwm{}, 51--74\% unparseable), decision collapse (\cls{} under truncate preprocessing, fail recall ${\sim}$14\%), and aggregation penalty (\cls{} under drop preprocessing, fail recall 38--57\%). Decision collapse is configuration-dependent, not model-inherent. \traj{} avoids aggregation penalty by predicting variant outcomes directly (72.91--77.08\%). Downsampling \cls{} training data to match \traj{}'s data volume yields 80.74\%, still 7.82\pp{} above \traj{}; this controls data volume but not label granularity (per-test vs.\ variant-level), and remains a single-seed comparison (Appendix~\ref{app:downsample}). The ${\sim}$180$\times$ data volume difference (\cls{} ${\sim}$70K per-test labels vs.\ \traj{} ${\sim}$386 variant-level labels) is inherent to formulation design: per-test annotation naturally yields more training instances for the same problem set.
144	
145	\begin{table}[t]
146	\centering
147	\small
148	\caption{Repo-level failure mode taxonomy. Variant-level majority baseline: 54.17\%.}
149	\label{tab:taxonomy}
150	\setlength{\tabcolsep}{3pt}
151	\resizebox{\columnwidth}{!}{%
152	\begin{tabular}{llcc}
153	\toprule
154	\textbf{Failure Mode} & \textbf{Representative} & \textbf{Fail Recall} & \textbf{Variant Acc} \\
155	\midrule
156	Format collapse & \cwm{} (all) & N/A & 48--52\% \\
157	Decision collapse & \cls{} (DeepSeek, s123) & ${\sim}$14\% & 56\% \\
158	Aggr.\ penalty & \cls{} (Qwen3-8B) & 51--57\% & 73--81\% \\
159	Aggr.\ penalty & \cls{} (DeepSeek, s42) & 38--51\% & 79--81\% \\
160	\bottomrule
161	\end{tabular}}
162	\end{table}
163	
164	\paragraph{Default assignment artifact.} The apparent \cwm{} accuracy increase from 4B to 8B is an artifact of rising unparseable rate (53.7\%$\to$73.8\%), inflating accuracy via majority-class default while parseable-only accuracy decreases (42.88\%$\to$38.52\%); cross-seed evidence confirms the pattern (Appendix~\ref{app:parseable_bias}).
165	
166	\paragraph{Complexity as moderator.} The \cls{}--\cwm{} gap widens from 1--3\pp{} (function) to 18--26\pp{} (repo) under our protocol; a matched-context ablation confirms input disparity explains $<$3\% of this gap (Appendix~\ref{app:ablations}).
167	
168	\paragraph{Formulation$\times$complexity interaction.} A mixed-effects linear probability model with problem-level random intercepts ($n{=}56{,}480$ observations, 139 problem clusters, DeepSeek-Coder) confirms the interaction: the \cwm{} effect at function level is negligible ($\hat{\beta}{=}-0.002$, $p{=}0.805$), but the formulation$\times$complexity interaction is highly significant ($z{=}-23.7$, $p{<}0.001$). \cwm{} and \cls{} are statistically indistinguishable at function level ($\Delta{=}-0.2$\pp{}) but diverge by 22\pp{} at repo level, confirming the divergence is not an artifact of aggregation. The cross-complexity analysis uses DeepSeek-Coder, the only family with matched function- and repo-level \cwm{} evaluations. A repo-level cross-model LPM confirms formulation dominates ($\hat{\beta}{=}-0.22$ vs.\ model $\hat{\beta}{=}+0.011$); model identity is directionally positive but GEE logistic regression yields a non-significant estimate ($p{=}0.449$), consistent with formulation as the dominant factor (Appendix~\ref{app:interaction}).
169	
170	Additional repo-level limitations appear in Appendix~\ref{app:limitations}.
171	
172	
173	\subsection{Analysis}
174	\label{sec:analysis}
175	
176	\paragraph{Aggregation penalty.} Under the all-pass rule, a single false negative flips the variant verdict; the penalty ranges from 1.36\pp{} to 19\pp{} depending on fail recall and test count (Appendix Table~\ref{tab:variant_level}). \traj{} avoids this by predicting variant outcomes directly (72.91--77.08\%). The penalty concentrates at high test counts: negligible at function level ($\bar{T} \approx 2.3$) but substantial at repo level ($\bar{T} \gg 10$; Appendix~\ref{app:extended_analysis}(a)).
177	
178	\paragraph{Why does generation degrade at repo level?} Output space complexity increases nonlinearly: function-level outputs are short status strings (e.g., ``PASS'' or brief error messages, mean ${\sim}$5--15 tokens); repo-level outputs are unconstrained execution traces (mean ${\sim}$477 tokens) where errors compound multiplicatively, causing format collapse (53--74\% unparseable). Even parseable outputs achieve only 38--43\% accuracy, below majority baseline; forced parsing rescues 90.6\% of unparseable outputs but achieves only 49.4\% accuracy, confirming the bottleneck is semantic (Appendix~\ref{app:extended_analysis}(c)). Four targeted interventions---increased LoRA capacity (rank~32), majority voting ($K{=}3$), relaxed output matching, and model scaling (4B$\to$8B)---all fail to close the gap (Appendix~\ref{app:extended_analysis}(g)). Checkpoint selection does not explain the gap: matched epoch-3 comparisons yield gaps of 20--23\pp{} (comparable to val-selected gaps), and \cls{} checkpoint ablation shows $<$1\pp{} variation across epochs, with the val-selected checkpoint performing no better than the worst epoch (Appendix~\ref{app:cwm_convergence}). This extends formulation-dependent tradeoffs~\cite{raffel2020t5} to a regime where output complexity makes format compliance a dominant failure mode. \cwm{} eval loss reaches its minimum within 5\% of training and increases monotonically across all seeds; a DeepSeek epoch-1 checkpoint achieves 75.45\% vs.\ 57.31\% at epoch~3, reducing the gap to ${\sim}$9\pp{} but retaining 66.4\% unparseable (Appendix~\ref{app:cwm_convergence}).
179	
180	\cls{} achieves 217$\times$ higher throughput than \cwm{} (1 output token vs.\ avg 477; median latency: 48ms vs.\ 16.3s per inference; Appendix~\ref{app:extended_analysis}(i)), consistent across both model families.
181	
182	\paragraph{Error complementarity.} At function level, \cls{} and \cwm{} are both FP-dominant but at different rates (\cls{} 56.5\%, \cwm{} 70.3\%; Appendix~\ref{app:extended_analysis}(a)). An oracle combination (any-correct: a variant is correct if \emph{any} formulation classifies all its tests correctly) achieves 90.63\% (+2.80\pp{}; 95\% CI [89.3\%, 91.9\%]; single-seed); cross-seed repo-level oracle is 94.27 $\pm$ 2.59\% (3 seeds). At repo level, oracle routing reaches 95.83\% variant accuracy (+14.58\pp{}; $n{=}48$, single-seed). The per-test advantage concentrates at $T \geq 2$ F2P tests (31.3\% of instances; Appendix~\ref{app:oracle}). Simple routing heuristics (test-count threshold, mutation-type routing) capture $<$0.4\pp{} of the 2--4\pp{} oracle gap, none statistically significant; the complementarity is instance-specific rather than feature-driven, suggesting a learned router is needed to exploit it. A re-repair pilot found no benefit ($n{=}44$, $p{=}0.42$; Appendix~\ref{app:extended_analysis}(j)).
183	
184	\subsection{Threats to Validity}
185	\label{sec:threats}
186	
187	We identify five potential confounds and assess each in Appendix~\ref{app:threats}: checkpoint selection ($<$1\pp{} variation in ablation; NaN validation loss forces final-epoch default in all \cwm{} runs and DeepSeek \cls{} s123), evaluation sequence length (${\sim}$1.5\pp{}), preprocessing (${\sim}$8\pp{} cross-configuration variance), \traj{} training regime (downsample confirms formulation advantage), and \cwm{} scale/pretraining (primary limitation; all repo-level \cwm{} conclusions conditional on the ${\leq}$8B LoRA regime). The 18--26\pp{} gap exceeds any single assessed confound, but correlated confounds and limited seeds mean definitive causal attribution requires multi-seed replication. Holm-Bonferroni correction ($k{=}5$) confirms the two core claims survive (adjusted $p{=}0.015$ and $p{=}0.028$; Table~\ref{tab:holm}): repo-level \cls{}--\cwm{} divergence and function-level \cls{}--\cwm{} equivalence.
188	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a498599e-6fac-4be6-b6dd-48f90d843026",
  "isSidechain": false,
  "promptId": "ec010885-b9c9-4574-b4a8-341b5a1f339a",
  "type": "user",
  "uuid": "72fbcf9d-f3a2-4dfb-81ac-ee09b01ebc3e",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/experiments.tex",
      "content": "\\section{Experiments}\n\\label{sec:experiments}\n\nWe systematically compare \\cls{}, \\cwm{}, and \\traj{} across two representative code LLM families, two complexity levels, and multiple seeds to characterize the formulation landscape for neural code verification.\n\n\\subsection{Experimental Setup}\n\\label{sec:setup}\n\n\\paragraph{Datasets.}\n\\emph{Function-level}: mutated variants from HumanEval~\\cite{chen2021humaneval} and MBPP~\\cite{austin2021mbpp} (five mutation types), labels verified by execution. 19,076 samples (train 15,290 / val 1,896 / test 1,890; pass:fail $\\approx$ 52:48, majority baseline 51.75\\%).\n\\emph{Repo-level}: per-test instances from SWE-bench Verified~\\cite{chowdhury2024swebenchverified} mutants. ${\\sim}$70K training samples; val ($n{=}9{,}335$) and test ($n{=}9{,}784$) have zero problem overlap (majority baseline 72.96\\%). Val-based checkpoint selection follows standard practice~\\cite{jimenez2024swebench} where validation loss is computable; runs using truncate preprocessing produce NaN validation loss because repo-level execution traces often exceed the 2,048-token sequence length limit; after truncation, many samples have all target tokens removed (labels entirely $-$100), producing degenerate loss---a formulation-inherent weakness that classification and trajectory formulations avoid by design. NaN loss defaults to the final epoch checkpoint (affects DeepSeek \\cls{} s123, all \\cwm{} runs, and Qwen3 \\traj{} runs; see Appendix~\\ref{app:hyperparams}).\n\n\\paragraph{Models and training.}\nWe fine-tune Qwen3-4B and Qwen3-8B~\\cite{qwen2025qwen3} with Low-Rank Adaptation (LoRA)~\\cite{hu2022lora} (rank 16, 3 epochs) across five seeds. Seeds 42/123/456 use bfloat16; seeds 789/0 use NormalFloat 4-bit (NF4) quantization~\\cite{dettmers2024qlora} to test robustness to precision reduction (function-level accuracy remains within seed noise across both precisions; see footnote in \\S\\ref{sec:equivalence}). As a cross-model consistency check, we additionally fine-tune DeepSeek-Coder-6.7B~\\cite{guo2024deepseekcoder} with identical LoRA configuration (2 seeds each for \\cls{} and \\cwm{}). Our \\cwm{} baseline is a LoRA fine-tuned variant for matched comparison, not a reproduction of the 32B Code World Model~\\cite{meta2025cwm}. Repo-level models use val-selected checkpoints where available; runs with NaN validation loss use the final epoch checkpoint (Appendix~\\ref{app:hyperparams}). Zero-shot baselines use Qwen3-8B and Qwen3-32B (NF4) as LLM-as-judge. Full hyperparameter details appear in Appendix~\\ref{app:hyperparams}.\n\n\\paragraph{Statistics.}\nConfidence intervals use clustered bootstrap~\\cite{davison1997bootstrap} (114 problem clusters, 10K resamples; we resample entire problems, not individual tests, to preserve within-problem correlations); per-test vs.\\ trajectory-level equivalence uses Two One-Sided Tests (TOST)~\\cite{schuirmann1987tost} with $\\pm$2 percentage point (\\pp{}) margin. Holm-Bonferroni correction~\\cite{holm1979} controls family-wise error rate across the five primary comparisons (Table~\\ref{tab:holm}). Intraclass correlation coefficient (ICC)~\\cite{shrout1979icc} quantifies within-problem correlation. Variant-level effect sizes and statistical power analysis are reported in Appendix~\\ref{app:power}. Oracle analysis uses SWE-bench Verified (500 instances).\n\n\n\\subsection{Function-Level Results}\n\\label{sec:func_results}\n\nTable~\\ref{tab:main_results} reports function-level results across formulations and model families.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Function-level per-test accuracy on HumanEval+MBPP ($n{=}1{,}890$). Mean $\\pm$ std over seeds. Seeds 42/123/456: bfloat16; 789/0: NF4. DeepSeek: $n{=}2$ seeds; std reported for descriptive comparison, not inferential. \\traj{} evaluated on 1,032-sample subset (447 matched variants).}\n\\label{tab:main_results}\n\\resizebox{\\columnwidth}{!}{%\n\\setlength{\\tabcolsep}{4pt}\n\\begin{tabular}{llcc}\n\\toprule\n\\textbf{Method} & \\textbf{Model} & \\textbf{Seeds} & \\textbf{Accuracy (\\%)} \\\\\n\\midrule\n\\multicolumn{4}{l}{\\emph{Qwen3 (primary)}} \\\\\n\\cls{} (fine-tuned) & 4B & 5 & \\textbf{88.43 $\\pm$ 0.78} \\\\\n\\cwm{} (fine-tuned) & 4B & 5 & \\underline{87.19 $\\pm$ 0.37} \\\\\n\\traj{} (fine-tuned) & 4B & 5 & 86.30 $\\pm$ 0.97 \\\\\n\\midrule\n\\multicolumn{4}{l}{\\emph{DeepSeek-Coder (cross-model consistency check)}} \\\\\n\\cls{} (fine-tuned) & 6.7B & 2 & \\textbf{86.85 $\\pm$ 0.11} \\\\\n\\cwm{} (fine-tuned) & 6.7B & 2 & \\underline{86.83 $\\pm$ 1.49} \\\\\n\\traj{} (fine-tuned) & 6.7B & 2 & 84.16 $\\pm$ 1.30 \\\\\n\\midrule\n\\multicolumn{4}{l}{\\emph{Prompting baselines}} \\\\\n0-shot & 8B (Qwen3) & 1 & 68.70 \\\\\n0-shot & 6.7B (DeepSeek) & 1 & 63.00 \\\\\nZS LLM-as-judge & 8B (Qwen3) & 1 & 64.40 \\\\\nZS LLM-as-judge & 6.7B (DeepSeek) & 1 & 56.56 \\\\\nZS LLM-as-judge & 32B (NF4) & 1 & 71.69 \\\\\n3-shot ICL & 8B (Qwen3) & 1 & 68.78 \\\\\n3-shot ICL & 6.7B (DeepSeek) & 1 & 59.95 \\\\\n\\midrule\nMajority (pass) & --- & --- & 51.75 \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\nAll three formulations achieve comparable accuracy on Qwen3-4B: \\cls{} 88.43\\% ($\\pm$0.78), \\cwm{} 87.19\\% ($\\pm$0.37), \\traj{} 86.30\\% ($\\pm$0.97). DeepSeek-Coder-6.7B shows: \\cls{} 86.85\\%, \\cwm{} 86.83\\%, \\traj{} 84.16\\%. The \\cls{}--\\cwm{} gap (0.02--1.24\\pp{}) is within seed noise in both families. However, the \\cls{}--\\traj{} gap is model-dependent: $<$1\\pp{} on Qwen3 but 2.69\\pp{} on DeepSeek-Coder, exceeding the $\\pm$2\\pp{} equivalence margin (\\S\\ref{sec:equivalence}). \\cls{} and \\cwm{} are robustly equivalent; \\traj{} parity is model-contingent. Zero-shot baselines (Tables~\\ref{tab:main_results} and~\\ref{tab:repo_level}) establish that repo-level verification requires fine-tuning (0-shot$\\to$fine-tuned gains of 35--36\\pp{}) and that formulation choice matters only at repo level (\\cls{} outperforms \\cwm{} by 18--26\\pp{}).\n\n\n\\subsection{Scaling Behavior}\n\\label{sec:scaling}\n\nBeyond overall accuracy, we examine whether formulation ranking is stable across model sizes. Table~\\ref{tab:scaling} compares all three formulations at 4B and 8B using seeds 42 and 123 in full bfloat16 precision (excluding NF4 seeds to isolate the size effect).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Model-size scaling: accuracy (\\%) at 4B and 8B (Qwen3, seeds 42/123, full bfloat16 precision). \\cls{} and \\traj{} scale positively; \\cwm{} does not. \\cwm{} scaling comparison is exploratory ($n{=}2$ seeds per size).}\n\\label{tab:scaling}\n\\setlength{\\tabcolsep}{4pt}\n\\begin{tabular}{llcccc}\n\\toprule\n\\textbf{Method} & \\textbf{Size} & \\textbf{s42} & \\textbf{s123} & \\textbf{Mean} & \\textbf{$\\Delta$ 4B$\\to$8B} \\\\\n\\midrule\n\\cls{} & 4B & 87.83 & 89.52 & \\textbf{88.68} & \\multirow{2}{*}{+1.27} \\\\\n\\cls{} & 8B & \\textbf{90.48} & 89.40 & \\textbf{89.94} & \\\\\n\\midrule\n\\cwm{} & 4B & 87.51 & 87.20 & \\underline{87.36} & \\multirow{2}{*}{$-$0.03} \\\\\n\\cwm{} & 8B & 87.67 & 86.98 & 87.33 & \\\\\n\\midrule\n\\traj{} & 4B & 85.66 & 85.47 & 85.57 & \\multirow{2}{*}{+2.13} \\\\\n\\traj{} & 8B & 87.60 & 87.79 & \\underline{87.70} & \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\cls{} and \\traj{} both scale positively from 4B to 8B (+1.27\\pp{} and +2.13\\pp{} respectively), while \\cwm{} remains flat ($-$0.03\\pp{}). At 8B, the ranking is \\cls{} (89.94) $>$ \\traj{} (87.70) $>$ \\cwm{} (87.33). The \\cls{}--\\cwm{} gap widens from 1.32\\pp{} at 4B to 2.62\\pp{} at 8B (Figure~\\ref{fig:scaling_gap}); clustered bootstrap on the 3-seed superset (42, 123, 456 for \\cls{}/\\cwm{}) yields $p = 0.0066$ (95\\% CI $[1.80, 2.71]$), which confirms the widening is not a sampling artifact.\n\n\\cwm{} flat scaling ($-$0.03\\pp{}) may reflect suboptimal hyperparameter transfer at 8B rather than a fundamental limitation; we do not claim generation \\emph{cannot} benefit from scale. At function level, outputs are short status strings (e.g., ``PASS'' or brief error messages) and format compliance is near-perfect; at repo level, output complexity increases substantially, and the same generation bottleneck manifests as format collapse patterns we examine in \\S\\ref{sec:repo}. \\traj{} also shows no scaling benefit at repo level (72.92\\% at both 4B and 8B); only \\cls{} scales positively across both complexity levels.\n\n\n\\subsection{Function-Level Equivalence}\n\\label{sec:equivalence}\n\nWe test pairwise equivalence among formulations on 523 variant-level instances across five seeds.\\footnote{Seeds 789 and 0 use NF4 quantized inference; the remaining three use bfloat16. Restricting to bfloat16 seeds only (3 seeds): \\cls{}--\\cwm{} remains significant ($p{<}0.05$); \\cls{}--\\traj{} yields $p{=}0.128$, consistent in direction but underpowered due to reduced seed coverage.} Our $\\pm$2\\pp{} SESOI threshold~\\cite{lakens2017,wellek2010} is set a priori based on deployment relevance: at 85--88\\% accuracy, a 2\\pp{} difference corresponds to ${\\sim}$2--3 problems out of 114---below the threshold at which a practitioner would select one formulation over another for pipeline integration. Post hoc, this threshold is consistent with between-seed variation (0.37--0.97\\pp{} std, Table~\\ref{tab:main_results}) and checkpoint noise ($<$1\\pp{}, \\S\\ref{sec:threats}), confirming that differences within the margin are indistinguishable from training noise. Within-problem predictions are correlated (ICC $= 0.191$, DEFF $= 3.97$~\\cite{moulton1990}); all tests use clustered bootstrap.\n\n\\paragraph{\\cls{}--\\cwm{} equivalence.} The pooled gap is 1.24\\pp{} (88.43\\%--87.19\\%); TOST confirms equivalence at $p = 0.007$ ($\\pm$2\\pp{} margin), surviving Holm-Bonferroni correction ($k{=}5$, adjusted $p{=}0.028$; Table~\\ref{tab:holm}). Equivalence holds at margins as tight as $\\pm$1.52\\pp{} (Table~\\ref{tab:tost_sensitivity}). On DeepSeek-Coder, the \\cls{}--\\cwm{} gap of 0.02\\pp{} is consistent with equivalence but underpowered (2 seeds).\n\n\\paragraph{\\cls{}--\\traj{} equivalence.} The pooled gap is $-$0.45\\pp{} (95\\% CI [$-$1.71, +0.84]); TOST yields $p = 0.025$ ($\\pm$2\\pp{}), nominally significant but not surviving Holm-Bonferroni correction ($k{=}5$, adjusted $p{=}0.075$; Table~\\ref{tab:holm}). The DeepSeek \\cls{}--\\traj{} gap (2.69\\pp{}) exceeds the $\\pm$2\\pp{} margin; \\traj{} parity is model-dependent. Per-test classification provides diagnostic information (which tests fail) at no cost to variant-level accuracy, paralleling process supervision~\\cite{lightman2023letsverify}.\n\n\\paragraph{Statistical power considerations.} With $n_{\\text{eff}} \\approx 86$ independent observations after clustering (DEFF $= 3.97$), the TOST at $\\pm$2\\pp{} achieves power ${\\sim}$0.3 for a medium effect size~\\cite{cohen1988}---a 70\\% probability of failing to confirm equivalence even if the true difference is moderate. The CLS--CWM equivalence ($p{=}0.007$) is robust to this limitation; the CLS--TRAJ non-confirmation ($p{=}0.075$) may reflect insufficient power rather than a genuine difference. A Bayesian ROPE analysis corroborates these conclusions ($P(\\text{ROPE}){=}0.975$ for CLS--CWM; Appendix~\\ref{app:bayesian_rope}).\n\n\n\\subsection{Repo-Level: Complexity-Dependent Divergence}\n\\label{sec:repo}\n\nTable~\\ref{tab:repo_level} compares formulations at repository-level complexity. Variant-level comparisons ($n{=}48$) are exploratory due to limited seed coverage; the per-test interaction effect is statistically confirmed (see below). Checkpoints are val-selected where validation loss is computable (\\S\\ref{sec:setup}); the test set has zero problem overlap with validation.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Repo-level cross-formulation comparison on SWE-bench Verified test set. Qwen3-8B \\cls{}/\\traj{}: mean $\\pm$ std over 3 seeds; DeepSeek \\cls{}: 2 seeds\\textsuperscript{$\\ddagger$}; DeepSeek \\traj{}: 3 seeds; Qwen3-4B: seed 42. \\cwm{}: 3 seeds (42/123/456).}\n\\label{tab:repo_level}\n\\resizebox{\\columnwidth}{!}{%\n\\setlength{\\tabcolsep}{4pt}\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Model} & \\textbf{\\cls{} (\\%)} & \\textbf{\\cls{} Var.\\ (\\%)} & \\textbf{\\cwm{} (\\%)} & \\textbf{\\traj{} Var.\\ (\\%)\\textsuperscript{$\\diamond$}} \\\\\n\\midrule\nQwen3-4B & 83.63 & 64.58 & 58.04 & 72.92 \\\\\nQwen3-8B & \\textbf{84.83 $\\pm$ 0.67} & 72.92 / 81.25\\textsuperscript{$\\dagger$} & 66.48 $\\pm$ 1.15 & 72.91 $\\pm$ 3.61 \\\\\nDeepSeek-6.7B & 84.38 $\\pm$ 2.50\\textsuperscript{$\\ddagger$} & 81.25\\textsuperscript{$\\dagger$} & 58.30 $\\pm$ 2.82 & 77.08 $\\pm$ 3.61 \\\\\n\\midrule\n0-shot (Qwen3-8B) & 49.90 & --- & --- & --- \\\\\n0-shot (DeepSeek) & 48.54 & --- & --- & --- \\\\\nMajority & 72.96 & 54.17 & 72.96 & 54.17 \\\\\n\\bottomrule\n\\end{tabular}}\n\n\\vspace{2pt}\n{\\footnotesize \\textsuperscript{$\\dagger$}Individual-seed variant accuracy. \\textsuperscript{$\\ddagger$}One seed excluded: truncate preprocessing$\\to$NaN val loss, decision collapse (Table~\\ref{tab:taxonomy}); mean over two matched seeds. \\textsuperscript{$\\diamond$}Var.\\ columns: variant-level accuracy ($n{=}48$); \\cls{} aggregated via all-pass rule; \\traj{} by design. Per-test: $n{=}9{,}784$. \\cwm{} unparseable: 54\\% (4B); default to pass; parseable-only 38--43\\%, below majority. Eval seq\\_length differs across models (Appendix~\\ref{app:threats}). \\cwm{} uses epoch-3 checkpoint (val loss undefined); see text for checkpoint sensitivity analysis.}\n\\end{table}\n\nFew-shot prompting (3-shot ICL) collapses to an always-predict-unresolved baseline (variant accuracy 45.83\\%, below majority 54.17\\%; Appendix~\\ref{app:few_shot}), establishing that execution-free verification requires task-specific fine-tuning regardless of formulation. The fine-tuning requirement (35--36\\pp{} gains, Table~\\ref{tab:repo_level}) is the first layer of our three-layer structure.\n\n\\paragraph{Formulation divergence.} Under our 4--8B LoRA protocol, \\cls{} and \\cwm{} diverge on Qwen3: the gap is 25.59\\pp{} at 4B (\\cls{} 83.63\\% vs.\\ \\cwm{} 58.04\\%, seed 42; Figure~\\ref{fig:scaling_gap}) and 18.35\\pp{} at 8B (84.83\\% vs.\\ 66.48\\%, 3-seed means). \\cwm{} falls below majority baseline at both scales. These gaps confirm complexity-dependent formulation divergence, though limited seed coverage and multiple confounds (\\S\\ref{sec:threats}) limit definitive causal attribution.\n\n\\paragraph{Cross-model consistency.} DeepSeek-Coder shows the same direction (\\cls{} $>$ \\cwm{}) across all seeds, with gap magnitude varying across families (20\\pp{} Qwen3 vs.\\ 23--28\\pp{} DeepSeek), primarily reflecting checkpoint selection sensitivity; under matched epoch-3 checkpoints, the cross-model gap difference narrows to ${\\sim}$2\\pp{} (Appendix~\\ref{app:threats}). Across all six \\cwm{} repo-level seeds, every seed exhibits format collapse ($>$50\\% unparseable) and parseable-only accuracy below majority baseline, ruling out seed-specific artifacts.\n\n\\paragraph{Failure mode taxonomy.} Variant-level analysis ($n{=}48$, Appendix Table~\\ref{tab:variant_level}) reveals three failure modes (Table~\\ref{tab:taxonomy}): format collapse (\\cwm{}, 51--74\\% unparseable), decision collapse (\\cls{} under truncate preprocessing, fail recall ${\\sim}$14\\%), and aggregation penalty (\\cls{} under drop preprocessing, fail recall 38--57\\%). Decision collapse is configuration-dependent, not model-inherent. \\traj{} avoids aggregation penalty by predicting variant outcomes directly (72.91--77.08\\%). Downsampling \\cls{} training data to match \\traj{}'s data volume yields 80.74\\%, still 7.82\\pp{} above \\traj{}; this controls data volume but not label granularity (per-test vs.\\ variant-level), and remains a single-seed comparison (Appendix~\\ref{app:downsample}). The ${\\sim}$180$\\times$ data volume difference (\\cls{} ${\\sim}$70K per-test labels vs.\\ \\traj{} ${\\sim}$386 variant-level labels) is inherent to formulation design: per-test annotation naturally yields more training instances for the same problem set.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Repo-level failure mode taxonomy. Variant-level majority baseline: 54.17\\%.}\n\\label{tab:taxonomy}\n\\setlength{\\tabcolsep}{3pt}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llcc}\n\\toprule\n\\textbf{Failure Mode} & \\textbf{Representative} & \\textbf{Fail Recall} & \\textbf{Variant Acc} \\\\\n\\midrule\nFormat collapse & \\cwm{} (all) & N/A & 48--52\\% \\\\\nDecision collapse & \\cls{} (DeepSeek, s123) & ${\\sim}$14\\% & 56\\% \\\\\nAggr.\\ penalty & \\cls{} (Qwen3-8B) & 51--57\\% & 73--81\\% \\\\\nAggr.\\ penalty & \\cls{} (DeepSeek, s42) & 38--51\\% & 79--81\\% \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\n\\paragraph{Default assignment artifact.} The apparent \\cwm{} accuracy increase from 4B to 8B is an artifact of rising unparseable rate (53.7\\%$\\to$73.8\\%), inflating accuracy via majority-class default while parseable-only accuracy decreases (42.88\\%$\\to$38.52\\%); cross-seed evidence confirms the pattern (Appendix~\\ref{app:parseable_bias}).\n\n\\paragraph{Complexity as moderator.} The \\cls{}--\\cwm{} gap widens from 1--3\\pp{} (function) to 18--26\\pp{} (repo) under our protocol; a matched-context ablation confirms input disparity explains $<$3\\% of this gap (Appendix~\\ref{app:ablations}).\n\n\\paragraph{Formulation$\\times$complexity interaction.} A mixed-effects linear probability model with problem-level random intercepts ($n{=}56{,}480$ observations, 139 problem clusters, DeepSeek-Coder) confirms the interaction: the \\cwm{} effect at function level is negligible ($\\hat{\\beta}{=}-0.002$, $p{=}0.805$), but the formulation$\\times$complexity interaction is highly significant ($z{=}-23.7$, $p{<}0.001$). \\cwm{} and \\cls{} are statistically indistinguishable at function level ($\\Delta{=}-0.2$\\pp{}) but diverge by 22\\pp{} at repo level, confirming the divergence is not an artifact of aggregation. The cross-complexity analysis uses DeepSeek-Coder, the only family with matched function- and repo-level \\cwm{} evaluations. A repo-level cross-model LPM confirms formulation dominates ($\\hat{\\beta}{=}-0.22$ vs.\\ model $\\hat{\\beta}{=}+0.011$); model identity is directionally positive but GEE logistic regression yields a non-significant estimate ($p{=}0.449$), consistent with formulation as the dominant factor (Appendix~\\ref{app:interaction}).\n\nAdditional repo-level limitations appear in Appendix~\\ref{app:limitations}.\n\n\n\\subsection{Analysis}\n\\label{sec:analysis}\n\n\\paragraph{Aggregation penalty.} Under the all-pass rule, a single false negative flips the variant verdict; the penalty ranges from 1.36\\pp{} to 19\\pp{} depending on fail recall and test count (Appendix Table~\\ref{tab:variant_level}). \\traj{} avoids this by predicting variant outcomes directly (72.91--77.08\\%). The penalty concentrates at high test counts: negligible at function level ($\\bar{T} \\approx 2.3$) but substantial at repo level ($\\bar{T} \\gg 10$; Appendix~\\ref{app:extended_analysis}(a)).\n\n\\paragraph{Why does generation degrade at repo level?} Output space complexity increases nonlinearly: function-level outputs are short status strings (e.g., ``PASS'' or brief error messages, mean ${\\sim}$5--15 tokens); repo-level outputs are unconstrained execution traces (mean ${\\sim}$477 tokens) where errors compound multiplicatively, causing format collapse (53--74\\% unparseable). Even parseable outputs achieve only 38--43\\% accuracy, below majority baseline; forced parsing rescues 90.6\\% of unparseable outputs but achieves only 49.4\\% accuracy, confirming the bottleneck is semantic (Appendix~\\ref{app:extended_analysis}(c)). Four targeted interventions---increased LoRA capacity (rank~32), majority voting ($K{=}3$), relaxed output matching, and model scaling (4B$\\to$8B)---all fail to close the gap (Appendix~\\ref{app:extended_analysis}(g)). Checkpoint selection does not explain the gap: matched epoch-3 comparisons yield gaps of 20--23\\pp{} (comparable to val-selected gaps), and \\cls{} checkpoint ablation shows $<$1\\pp{} variation across epochs, with the val-selected checkpoint performing no better than the worst epoch (Appendix~\\ref{app:cwm_convergence}). This extends formulation-dependent tradeoffs~\\cite{raffel2020t5} to a regime where output complexity makes format compliance a dominant failure mode. \\cwm{} eval loss reaches its minimum within 5\\% of training and increases monotonically across all seeds; a DeepSeek epoch-1 checkpoint achieves 75.45\\% vs.\\ 57.31\\% at epoch~3, reducing the gap to ${\\sim}$9\\pp{} but retaining 66.4\\% unparseable (Appendix~\\ref{app:cwm_convergence}).\n\n\\cls{} achieves 217$\\times$ higher throughput than \\cwm{} (1 output token vs.\\ avg 477; median latency: 48ms vs.\\ 16.3s per inference; Appendix~\\ref{app:extended_analysis}(i)), consistent across both model families.\n\n\\paragraph{Error complementarity.} At function level, \\cls{} and \\cwm{} are both FP-dominant but at different rates (\\cls{} 56.5\\%, \\cwm{} 70.3\\%; Appendix~\\ref{app:extended_analysis}(a)). An oracle combination (any-correct: a variant is correct if \\emph{any} formulation classifies all its tests correctly) achieves 90.63\\% (+2.80\\pp{}; 95\\% CI [89.3\\%, 91.9\\%]; single-seed); cross-seed repo-level oracle is 94.27 $\\pm$ 2.59\\% (3 seeds). At repo level, oracle routing reaches 95.83\\% variant accuracy (+14.58\\pp{}; $n{=}48$, single-seed). The per-test advantage concentrates at $T \\geq 2$ F2P tests (31.3\\% of instances; Appendix~\\ref{app:oracle}). Simple routing heuristics (test-count threshold, mutation-type routing) capture $<$0.4\\pp{} of the 2--4\\pp{} oracle gap, none statistically significant; the complementarity is instance-specific rather than feature-driven, suggesting a learned router is needed to exploit it. A re-repair pilot found no benefit ($n{=}44$, $p{=}0.42$; Appendix~\\ref{app:extended_analysis}(j)).\n\n\\subsection{Threats to Validity}\n\\label{sec:threats}\n\nWe identify five potential confounds and assess each in Appendix~\\ref{app:threats}: checkpoint selection ($<$1\\pp{} variation in ablation; NaN validation loss forces final-epoch default in all \\cwm{} runs and DeepSeek \\cls{} s123), evaluation sequence length (${\\sim}$1.5\\pp{}), preprocessing (${\\sim}$8\\pp{} cross-configuration variance), \\traj{} training regime (downsample confirms formulation advantage), and \\cwm{} scale/pretraining (primary limitation; all repo-level \\cwm{} conclusions conditional on the ${\\leq}$8B LoRA regime). The 18--26\\pp{} gap exceeds any single assessed confound, but correlated confounds and limited seeds mean definitive causal attribution requires multi-seed replication. Holm-Bonferroni correction ($k{=}5$) confirms the two core claims survive (adjusted $p{=}0.015$ and $p{=}0.028$; Table~\\ref{tab:holm}): repo-level \\cls{}--\\cwm{} divergence and function-level \\cls{}--\\cwm{} equivalence.\n",
      "numLines": 188,
      "startLine": 1,
      "totalLines": 188
    }
  },
  "sourceToolAssistantUUID": "a498599e-6fac-4be6-b6dd-48f90d843026",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier",
  "sessionId": "8c11e549-46d3-438b-848f-c86f519fca39",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-22T19:18:58.599Z_

<details open><summary>🔧 Tool call — Read · `toolu_01M9RePpUyTJBWRAUwFBZep1`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "72fbcf9d-f3a2-4dfb-81ac-ee09b01ebc3e",
  "isSidechain": false,
  "requestId": "req_011CbJ9UoRFm2GRjSasNgqwg",
  "type": "assistant",
  "uuid": "01b6954c-f879-4451-ae96-8db682094bb6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier",
  "sessionId": "8c11e549-46d3-438b-848f-c86f519fca39",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01U16PPjqHqZa23X2kRksyjc",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 614,
      "cache_read_input_tokens": 24786,
      "output_tokens": 748,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 614,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 748,
          "cache_read_input_tokens": 24786,
          "cache_creation_input_tokens": 614,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 614
          },
          "type": "message"
        }
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

_source line 26 · 2026-05-22T19:18:58.604Z_

<details><summary>↩ Tool result · `toolu_01M9RePpUyTJBWRAUwFBZep1`</summary>

```text
1	\section{Related Work}
2	\label{sec:related_work}
3	
4	\paragraph{Execution Simulation and Verification.}
5	Execution trace generation improves code reasoning~\cite{nye2021scratchpad}, with extensions to output prediction~\cite{meta2025cwm,maimon2026selfexecution,liu2024codemind,liu2023codeexecutor,lee2026solidcoder}, failure analysis~\cite{abdollahi2025demystifying}, and error detection~\cite{li2024redo}. CRUXEval~\citep{gu2024cruxeval} benchmarks code execution prediction at function level; RepoExec~\citep{nam2025repoexec} evaluates repo-level code generation with execution-based correctness checks. Our work extends execution prediction to repo-level repair verification. CodeScaler~\cite{zhu2026codescaler} trains execution-free reward models for both RL and test-time scaling. Verification formulations span trajectory-level reward~\cite{shum2025swerm}, process-level feedback~\cite{li2025codeprm,xu2025patchreasoner}, per-test classification~\cite{ni2023lever,chen2023codet}, learned metrics~\cite{zhuo2024icescore,dong2024codescore,zhou2023codebertscore}, and RL with execution-based rewards~\cite{wang2026verpo,tang2026execverify}. Aletheia~\cite{venkatkrishna2026aletheia} compares training recipes; we compare \emph{formulations}. Test-time scaling~\cite{snell2024scaling,li2025sstar,chen2025vgsearch} and self-consistency~\cite{wang2023selfconsistency} demonstrate verification value; none compare formulations at matched capacity.
6	
7	\paragraph{Process vs.\ Outcome Supervision.}
8	PRMs outperform ORMs for math reasoning~\cite{lightman2023letsverify,uesato2022solving}, with automated annotation~\cite{wang2024mathshepherd,luo2024omegaprm} and code-specific extensions~\cite{dreamprm2025code,ye2025prlcoder,zhang2026funprm,jiang2025coderlplus}. GenRM~\cite{hosseini2025genrm} and GenPRM~\cite{zhao2026genprm} show that generative verifiers outperform discriminative ones for math reasoning; our results reveal a domain difference---in code verification, the generative formulation (\cwm{}) does not outperform the discriminative one (\cls{}), suggesting that the generation advantage may be domain-specific. CodeRM~\cite{ma2025coderm} demonstrates that test-level reward granularity improves code generation quality, corroborating our finding that per-test classification provides diagnostic value. In reward modeling terminology, \cls{} corresponds to process-level (PRM-like) verification while \traj{} provides outcome-level (ORM-like) feedback; \cwm{} serves as a generative verifier~\cite{hosseini2025genrm}. Our \cls{} provides per-test (process) supervision while \traj{} provides outcome-level; the PRM literature compares supervision granularity given a fixed output format, while we additionally vary the output format (\cwm{} generation vs.\ \cls{} classification).
9	
10	\paragraph{Repair, Mutation Testing, and Task Framing.}
11	CodeRL~\cite{le2022coderl}, AlphaCode~\cite{li2022alphacode,alphacode2023team}, and Reflexion~\cite{shinn2023reflexion} use execution feedback for repair. SWE-bench~\cite{jimenez2024swebench,chowdhury2024swebenchverified} provides benchmarks; SWE-agent~\cite{yang2024sweagent} and Agentless~\cite{xia2024agentless} demonstrate pipelines where verification is a bottleneck~\cite{yang2025aprsurvey}. Predictive mutation testing~\cite{tufano2019predictive,kim2022predictive,wang2024llmmutation,jain2023contextual} shares our per-test structure. LoRA~\cite{hu2022lora} and QLoRA~\cite{dettmers2024qlora} enable parameter-efficient fine-tuning. Task framing---how a problem is cast as a model's input--output mapping---systematically affects performance: \citet{raffel2020t5} showed that classification, generation, and span-extraction formulations yield different accuracy--efficiency tradeoffs across NLP tasks. We apply this paradigm to code verification, holding architecture and training data constant while varying only the formulation; our finding that complexity moderates the classification--generation tradeoff extends their analysis to a new domain.
12	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "01b6954c-f879-4451-ae96-8db682094bb6",
  "isSidechain": false,
  "promptId": "ec010885-b9c9-4574-b4a8-341b5a1f339a",
  "type": "user",
  "uuid": "aa3494ee-ae35-4e50-a390-040169d6c31d",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/related_work.tex",
      "content": "\\section{Related Work}\n\\label{sec:related_work}\n\n\\paragraph{Execution Simulation and Verification.}\nExecution trace generation improves code reasoning~\\cite{nye2021scratchpad}, with extensions to output prediction~\\cite{meta2025cwm,maimon2026selfexecution,liu2024codemind,liu2023codeexecutor,lee2026solidcoder}, failure analysis~\\cite{abdollahi2025demystifying}, and error detection~\\cite{li2024redo}. CRUXEval~\\citep{gu2024cruxeval} benchmarks code execution prediction at function level; RepoExec~\\citep{nam2025repoexec} evaluates repo-level code generation with execution-based correctness checks. Our work extends execution prediction to repo-level repair verification. CodeScaler~\\cite{zhu2026codescaler} trains execution-free reward models for both RL and test-time scaling. Verification formulations span trajectory-level reward~\\cite{shum2025swerm}, process-level feedback~\\cite{li2025codeprm,xu2025patchreasoner}, per-test classification~\\cite{ni2023lever,chen2023codet}, learned metrics~\\cite{zhuo2024icescore,dong2024codescore,zhou2023codebertscore}, and RL with execution-based rewards~\\cite{wang2026verpo,tang2026execverify}. Aletheia~\\cite{venkatkrishna2026aletheia} compares training recipes; we compare \\emph{formulations}. Test-time scaling~\\cite{snell2024scaling,li2025sstar,chen2025vgsearch} and self-consistency~\\cite{wang2023selfconsistency} demonstrate verification value; none compare formulations at matched capacity.\n\n\\paragraph{Process vs.\\ Outcome Supervision.}\nPRMs outperform ORMs for math reasoning~\\cite{lightman2023letsverify,uesato2022solving}, with automated annotation~\\cite{wang2024mathshepherd,luo2024omegaprm} and code-specific extensions~\\cite{dreamprm2025code,ye2025prlcoder,zhang2026funprm,jiang2025coderlplus}. GenRM~\\cite{hosseini2025genrm} and GenPRM~\\cite{zhao2026genprm} show that generative verifiers outperform discriminative ones for math reasoning; our results reveal a domain difference---in code verification, the generative formulation (\\cwm{}) does not outperform the discriminative one (\\cls{}), suggesting that the generation advantage may be domain-specific. CodeRM~\\cite{ma2025coderm} demonstrates that test-level reward granularity improves code generation quality, corroborating our finding that per-test classification provides diagnostic value. In reward modeling terminology, \\cls{} corresponds to process-level (PRM-like) verification while \\traj{} provides outcome-level (ORM-like) feedback; \\cwm{} serves as a generative verifier~\\cite{hosseini2025genrm}. Our \\cls{} provides per-test (process) supervision while \\traj{} provides outcome-level; the PRM literature compares supervision granularity given a fixed output format, while we additionally vary the output format (\\cwm{} generation vs.\\ \\cls{} classification).\n\n\\paragraph{Repair, Mutation Testing, and Task Framing.}\nCodeRL~\\cite{le2022coderl}, AlphaCode~\\cite{li2022alphacode,alphacode2023team}, and Reflexion~\\cite{shinn2023reflexion} use execution feedback for repair. SWE-bench~\\cite{jimenez2024swebench,chowdhury2024swebenchverified} provides benchmarks; SWE-agent~\\cite{yang2024sweagent} and Agentless~\\cite{xia2024agentless} demonstrate pipelines where verification is a bottleneck~\\cite{yang2025aprsurvey}. Predictive mutation testing~\\cite{tufano2019predictive,kim2022predictive,wang2024llmmutation,jain2023contextual} shares our per-test structure. LoRA~\\cite{hu2022lora} and QLoRA~\\cite{dettmers2024qlora} enable parameter-efficient fine-tuning. Task framing---how a problem is cast as a model's input--output mapping---systematically affects performance: \\citet{raffel2020t5} showed that classification, generation, and span-extraction formulations yield different accuracy--efficiency tradeoffs across NLP tasks. We apply this paradigm to code verification, holding architecture and training data constant while varying only the formulation; our finding that complexity moderates the classification--generation tradeoff extends their analysis to a new domain.\n",
      "numLines": 12,
      "startLine": 1,
      "totalLines": 12
    }
  },
  "sourceToolAssistantUUID": "01b6954c-f879-4451-ae96-8db682094bb6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier",
  "sessionId": "8c11e549-46d3-438b-848f-c86f519fca39",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-22T19:18:59.682Z_

<details open><summary>🔧 Tool call — Read · `toolu_017pVZipcKJmXW8q68ATXpBJ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "aa3494ee-ae35-4e50-a390-040169d6c31d",
  "isSidechain": false,
  "requestId": "req_011CbJ9UoRFm2GRjSasNgqwg",
  "type": "assistant",
  "uuid": "3fa60f97-c6d0-430e-9cec-087555900228",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier",
  "sessionId": "8c11e549-46d3-438b-848f-c86f519fca39",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01U16PPjqHqZa23X2kRksyjc",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 614,
      "cache_read_input_tokens": 24786,
      "output_tokens": 748,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 614,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 748,
          "cache_read_input_tokens": 24786,
          "cache_creation_input_tokens": 614,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 614
          },
          "type": "message"
        }
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

_source line 28 · 2026-05-22T19:18:59.686Z_

<details><summary>↩ Tool result · `toolu_017pVZipcKJmXW8q68ATXpBJ`</summary>

```text
1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	We presented the first systematic comparison of three execution-free verification formulations (\cls{}, \cwm{}, \traj{}). At function level, \cls{} and \cwm{} are statistically equivalent (TOST $p{=}0.007$, 5 seeds); \traj{} equivalence is not confirmed after multiple comparison correction. Per-test classification achieves 217$\times$ higher throughput while providing diagnostic signal. Complementary errors (oracle: 90.63\%/95.83\%; single-seed) motivate complexity-aware routing. At repository level under ${\leq}$8B LoRA, divergence reaches 18--26\pp{} ($z{=}-23.7$, 3 seeds per model), with \cwm{} falling below majority baseline---consistent across families but dependent on multiple confounds (\S\ref{sec:threats}). Three failure modes (format collapse, decision collapse, aggregation penalty) are consistent across families. \cls{} is recommended primarily for its throughput advantage and diagnostic capability; the accuracy advantage over \traj{} is directional but underpowered ($n{=}48$, MDE${\approx}$25\pp{}; Appendix~\ref{app:power}). All findings are conditioned on ${\leq}$8B LoRA fine-tuning; at larger scale, the generation bottleneck may diminish (\S\ref{sec:threats}).
5	
6	Three directions follow: (1)~oracle gains motivate complexity-aware routing using the failure mode taxonomy as routing features; (2)~the semantic generation bottleneck (four interventions fail; Appendix~\ref{app:extended_analysis}(g)) suggests capacity scaling or execution trace pretraining~\cite{meta2025cwm} is needed---testing at 32B+ would resolve the primary open question; (3)~larger-scale evaluation of per-test diagnostics for downstream repair ($n{=}44$ in our pilot) would test whether \cls{}'s throughput advantage extends to repair pipelines.
7	
8	\section*{Limitations}
9	
10	Repo-level \cwm{} uses 3 seeds per model; the gap (18--26\pp{}) exceeds any single confound (\S\ref{sec:threats}), but correlated confounds require further replication. Our \cwm{} baseline uses ${\leq}$8B LoRA fine-tuning, not the original 32B CWM~\cite{meta2025cwm}; the generation bottleneck may diminish at larger scale. Training data comprises synthetic mutations~\cite{andrews2005mutation,just2014mutants}; synthetic-to-real transfer is untested, though the coupling effect supports relative ranking validity (Appendix~\ref{app:limitations}). The \traj{} downsample ablation uses a single model, seed, and complexity level. Model coverage is limited to 6--8B code-specialized LLMs. All evaluation uses Python-only benchmarks; languages with different test output conventions may exhibit different format compliance rates. Our evaluation targets repair verification; generalization to open-ended code generation is untested. All code, data, and model checkpoints will be released upon acceptance.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3fa60f97-c6d0-430e-9cec-087555900228",
  "isSidechain": false,
  "promptId": "ec010885-b9c9-4574-b4a8-341b5a1f339a",
  "type": "user",
  "uuid": "0a3fddf1-58bb-4bb6-bf78-a58396372af3",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/conclusion.tex",
      "content": "\\section{Conclusion}\n\\label{sec:conclusion}\n\nWe presented the first systematic comparison of three execution-free verification formulations (\\cls{}, \\cwm{}, \\traj{}). At function level, \\cls{} and \\cwm{} are statistically equivalent (TOST $p{=}0.007$, 5 seeds); \\traj{} equivalence is not confirmed after multiple comparison correction. Per-test classification achieves 217$\\times$ higher throughput while providing diagnostic signal. Complementary errors (oracle: 90.63\\%/95.83\\%; single-seed) motivate complexity-aware routing. At repository level under ${\\leq}$8B LoRA, divergence reaches 18--26\\pp{} ($z{=}-23.7$, 3 seeds per model), with \\cwm{} falling below majority baseline---consistent across families but dependent on multiple confounds (\\S\\ref{sec:threats}). Three failure modes (format collapse, decision collapse, aggregation penalty) are consistent across families. \\cls{} is recommended primarily for its throughput advantage and diagnostic capability; the accuracy advantage over \\traj{} is directional but underpowered ($n{=}48$, MDE${\\approx}$25\\pp{}; Appendix~\\ref{app:power}). All findings are conditioned on ${\\leq}$8B LoRA fine-tuning; at larger scale, the generation bottleneck may diminish (\\S\\ref{sec:threats}).\n\nThree directions follow: (1)~oracle gains motivate complexity-aware routing using the failure mode taxonomy as routing features; (2)~the semantic generation bottleneck (four interventions fail; Appendix~\\ref{app:extended_analysis}(g)) suggests capacity scaling or execution trace pretraining~\\cite{meta2025cwm} is needed---testing at 32B+ would resolve the primary open question; (3)~larger-scale evaluation of per-test diagnostics for downstream repair ($n{=}44$ in our pilot) would test whether \\cls{}'s throughput advantage extends to repair pipelines.\n\n\\section*{Limitations}\n\nRepo-level \\cwm{} uses 3 seeds per model; the gap (18--26\\pp{}) exceeds any single confound (\\S\\ref{sec:threats}), but correlated confounds require further replication. Our \\cwm{} baseline uses ${\\leq}$8B LoRA fine-tuning, not the original 32B CWM~\\cite{meta2025cwm}; the generation bottleneck may diminish at larger scale. Training data comprises synthetic mutations~\\cite{andrews2005mutation,just2014mutants}; synthetic-to-real transfer is untested, though the coupling effect supports relative ranking validity (Appendix~\\ref{app:limitations}). The \\traj{} downsample ablation uses a single model, seed, and complexity level. Model coverage is limited to 6--8B code-specialized LLMs. All evaluation uses Python-only benchmarks; languages with different test output conventions may exhibit different format compliance rates. Our evaluation targets repair verification; generalization to open-ended code generation is untested. All code, data, and model checkpoints will be released upon acceptance.",
      "numLines": 10,
      "startLine": 1,
      "totalLines": 10
    }
  },
  "sourceToolAssistantUUID": "3fa60f97-c6d0-430e-9cec-087555900228",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier",
  "sessionId": "8c11e549-46d3-438b-848f-c86f519fca39",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-22T19:19:00.014Z_

<details open><summary>🔧 Tool call — Read · `toolu_01BAF3RF5byBULDHiA3V4iq4`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0a3fddf1-58bb-4bb6-bf78-a58396372af3",
  "isSidechain": false,
  "requestId": "req_011CbJ9UoRFm2GRjSasNgqwg",
  "type": "assistant",
  "uuid": "fe4b017d-05e0-4e8e-8806-f29a21adddf7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier",
  "sessionId": "8c11e549-46d3-438b-848f-c86f519fca39",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01U16PPjqHqZa23X2kRksyjc",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 614,
      "cache_read_input_tokens": 24786,
      "output_tokens": 748,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 614,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 748,
          "cache_read_input_tokens": 24786,
          "cache_creation_input_tokens": 614,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 614
          },
          "type": "message"
        }
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

_source line 30 · 2026-05-22T19:19:00.286Z_

<details><summary>↩ Tool result · `toolu_01BAF3RF5byBULDHiA3V4iq4`</summary>

```text
1	\appendix
2	
3	\noindent\textbf{Appendix overview.} A: Oracle resolve advantage. B: Ablation studies. C-F: Extended analysis (error complementarity, parseable accuracy, forced parsing, qualitative errors, failed interventions, mutation scaling, inference efficiency, re-repair, chain-of-thought). G: TOST sensitivity. G$'$: Bayesian ROPE. H: Effect sizes. I: Holm-Bonferroni. J: Mixed-effects regression. K: Parseable bias. L: CWM convergence. M: Few-shot. N: Threats. O: Downsample. P: Limitations.
4	
5	\section{Oracle Accuracy-Utility Analysis}
6	\label{app:oracle}
7	
8	We stratify SWE-bench Verified instances by F2P test count $T$, comparing per-test vs.\ trajectory-level oracle resolve rates under i.i.d.\ and block-correlated error models (ICC $= 0.191$, from function-level analysis; \S\ref{sec:equivalence}).
9	
10	\begin{table}[h]
11	\centering
12	\small
13	\caption{Oracle accuracy-utility frontier: per-test advantage stratified by F2P test count ($T$) on SWE-bench Verified (500 instances). Block-correlated model uses function-level ICC $= 0.191$ (from function-level analysis, \S\ref{sec:equivalence}). P2P regression rate: 1.04\% mean, 0\% median.}
14	\label{tab:oracle}
15	\resizebox{\columnwidth}{!}{%
16	\setlength{\tabcolsep}{3pt}
17	\begin{tabular}{lcccc}
18	\toprule
19	\textbf{$T$} & \textbf{Inst.\%} & \textbf{i.i.d.\ (\pp{})} & \textbf{Block (\pp{})} & \textbf{Contrib.\%} \\
20	\midrule
21	$1$ & 68.7 & $-$0.04 & $-$0.09 & $\approx$0 \\
22	$2$ & 19.1 & 18.49 & 31.69 & 55.3 \\
23	$3$--$5$ & 7.1 & 25.00 & 40.74 & $\approx$26 \\
24	$\geq 6$ & 5.1 & 30.00 & 40.06 & $\approx$19 \\
25	\midrule
26	\textbf{All} & 100.0 & --- & \textbf{10.93} & 100.0 \\
27	\bottomrule
28	\end{tabular}}
29	\end{table}
30	
31	\begin{figure}[h]
32	\centering
33	\includegraphics[width=\columnwidth]{figures/paper/fig3_oracle_stratified.pdf}
34	\caption{Oracle per-test advantage by F2P test count $T$. Advantage is zero at $T{=}1$ (68.7\%) and concentrates at $T{=}2$ (19.1\%, contributing 55.3\% of total advantage). Note: $y$-axis does not start at zero.}
35	\label{fig:oracle_stratified}
36	\end{figure}
37	
38	Table~\ref{tab:oracle} and Figure~\ref{fig:oracle_stratified} reveal a sharp concentration: at $T = 1$ (68.7\% of instances), per-test and trajectory-level are informationally equivalent. The advantage materializes at $T = 2$ (19.1\%), where block-correlated advantage reaches 31.69\pp{} (55.3\% of total). The overall block-correlated advantage is 10.93\pp{}, driven by the $T \geq 2$ minority. Block correlation amplifies relative to i.i.d.: at $T = 2$, 31.69\pp{} vs.\ 18.49\pp{} (1.7$\times$). P2P regression is negligible (1.04\% mean, 0\% median); the practical value concentrates in F2P discrimination.
39	
40	\paragraph{Sensitivity to ICC estimate.}
41	The analysis above uses ICC $= 0.191$ from function-level analysis (\S\ref{sec:equivalence}), where mean cluster size $\bar{k} \approx 16.5$ yields DEFF $= 3.97$. At repository level, within-problem correlation is substantially stronger: ICC $= 0.3146$ with DEFF $= 114.4$ (\S\ref{sec:repo}), yielding an effective sample size of $n_{\text{eff}} \approx 9{,}784 / 114.4 \approx 86$ independent observations~\cite{moulton1990}---still sufficient for regression but limiting precision of variance component estimates. This is a consequence of the larger and more heterogeneous test suites in SWE-bench Verified problems. Under higher ICC, within-problem errors cluster more tightly and amplify the block-correlated per-test advantage at each $T$ stratum; the correction from i.i.d.\ to block-correlated grows monotonically with ICC. The function-level ICC $= 0.191$ used in Table~\ref{tab:oracle} thus provides a conservative lower bound on the per-test advantage. The repo-level correlation structure would yield an even larger gap between per-test and trajectory-level oracle resolve rates, which strengthens the case for per-test granularity at repository-level complexity.
42	
43	\section{Ablation Studies}
44	\label{app:ablations}
45	
46	\paragraph{LoRA rank sensitivity.}
47	All \cwm{} experiments use LoRA rank $r{=}16$. To test whether this capacity constraint handicaps \cwm{}, we train rank-32 variants (seed 42), doubling adapter parameters.
48	
49	\begin{table}[h]
50	\centering
51	\small
52	\caption{LoRA rank ablation for \cwm{} 4B (seed 42, 3 epochs, lr $= 2{\times}10^{-4}$). Rank-16 seed variance: 0.53\pp{} (seeds 42 vs.\ 456).}
53	\label{tab:rank_ablation}
54	\setlength{\tabcolsep}{4pt}
55	\begin{tabular}{lccccc}
56	\toprule
57	\textbf{Config} & \textbf{$\alpha/r$} & \textbf{Acc (\%)} & \textbf{Fail \fone{}} & \textbf{Pass \fone{}} & \textbf{$\Delta$} \\
58	\midrule
59	$r{=}16$, $\alpha{=}32$ & 2 & \textbf{87.51} & --- & --- & --- \\
60	$r{=}32$, $\alpha{=}32$ & 1 & 87.00 & 87.1 & 86.9 & $-$0.51 \\
61	$r{=}32$, $\alpha{=}64$ & 2 & 87.04 & 87.27 & 86.79 & $-$0.47 \\
62	\bottomrule
63	\end{tabular}
64	\end{table}
65	
66	Both rank-32 variants fall within the 2-seed variance of the rank-16 baseline (0.53\pp{} between seeds 42 and 456; Table~\ref{tab:rank_ablation}). The $\alpha{=}64$ variant (matching the baseline $\alpha/r{=}2$ ratio) rules out the confound that the $\alpha{=}32$ result might reflect reduced effective scaling rather than rank insensitivity. This is consistent with \cwm{}'s function-level performance being bounded by output-format constraints rather than adapter capacity.
67	
68	\paragraph{Majority voting.}
69	Majority voting ($K{=}3$) decreases accuracy from 87.51\% to 86.83\% ($-$0.68\pp{}): errors are systematic rather than stochastic, so sampling-based ensembles do not help.
70	
71	\paragraph{Sequence-length ablation details.}
72	Both formulations are trained with \texttt{max\_seq\_length}$=$2,048. At inference, \cwm{} reserves \texttt{max\_new\_tokens}$=$512, leaving ${\sim}$1,536 effective input tokens; \cls{} allocates nearly all context to input (5,120--8,192 tokens). A matched-context ablation (\cls{} 8B at 2,048 tokens) achieves 83.04\%, only 1.44\pp{} below the 8,192-token evaluation (84.48\%), though truncation introduces 136 unparseable outputs (1.39\% of test samples). The matched-context gap (\cls{}@2,048 vs.\ \cwm{}@2,048) is 25.00\pp{} (98\% of the full 25.59\pp{} gap), confirming that input context disparity explains at most 3\% of the difference.
73	
74	\paragraph{Training data size control.}
75	\label{app:downsample}
76	To control for the training set size asymmetry between \cls{} (${\sim}$70K instances) and \traj{} (386 variant-level instances, ${\sim}$8K per-test equivalents, at repo level), we downsample \cls{} training data to match \traj{} in data volume. Downsampled \cls{} (Qwen3-4B, seed 42) achieves 80.74\% repo-level per-test accuracy, only 2.89\pp{} below the full-data \cls{} (83.63\%) and still 7.82\pp{} above \traj{} (72.92\%). The \cls{} formulation advantage is not attributable to training data volume.
77	
78	\paragraph{Few-shot prompting baselines.}
79	\label{app:few_shot}
80	We evaluate 3-shot in-context learning at repo level to test whether prompting strategy closes the gap to fine-tuned models. Table~\ref{tab:few_shot} reports both per-test and variant-level accuracy.
81	
82	\begin{table}[h]
83	\centering
84	\small
85	\caption{Repo-level prompting baselines (per-test $n{=}9{,}784$; variant-level $n{=}48$). Majority baseline: 72.96\% per-test, 54.17\% variant-level.}
86	\label{tab:few_shot}
87	\setlength{\tabcolsep}{4pt}
88	\resizebox{\columnwidth}{!}{%
89	\begin{tabular}{lcccc}
90	\toprule
91	\textbf{Model} & \textbf{0-shot (per-test)} & \textbf{3-shot (per-test)} & \textbf{3-shot (variant)} \\
92	\midrule
93	Qwen3-8B & 49.90\% & 71.61\% & 45.83\%\textsuperscript{$\ast$} \\
94	DeepSeek-6.7B & 48.54\% & 46.28\% & 45.83\%\textsuperscript{$\ast$} \\
95	\bottomrule
96	\end{tabular}}
97	
98	\vspace{2pt}
99	{\footnotesize \textsuperscript{$\ast$}Both models achieve 45.83\% by correctly classifying all 22 unresolved variants and zero resolved variants (22/48 = 45.83\%), equivalent to an always-predict-unresolved baseline. The 100\% overlap in variant-level predictions confirms complete degradation at task-relevant granularity.}
100	\end{table}
101	
102	Both models converge to exactly 45.83\% variant-level accuracy under 3-shot prompting, below majority baseline (54.17\%). Variant-level analysis reveals this is not a coincidence: both models correctly classify all 22 unresolved variants and zero resolved variants, equivalent to an always-predict-unresolved baseline with 100\% prediction overlap. Per-test accuracy diverges sharply (Qwen3-8B 71.61\% vs.\ DeepSeek 46.28\%), but this divergence is entirely superficial: Qwen3-8B predicts pass on nearly all tests, inflating per-test accuracy on a pass-heavy dataset (72.96\% pass rate) without genuine discriminative ability. Per-test metrics can thus severely misrepresent baseline capability; variant-level evaluation is necessary to detect complete degradation. Neither 0-shot nor few-shot prompting approaches fine-tuned performance (82--84\% per-test); fine-tuning is a necessary condition for repo-level verification.
103	
104	\section{Repo-Level Per-Mutation Breakdown}
105	\label{app:repo_mutation}
106	
107	Table~\ref{tab:mutation_breakdown} compares per-mutation accuracy at repo level. \cls{} produces 0\% unparseable outputs; all values are direct classification accuracy. \cwm{} overall accuracy includes default-pass assignment for unparseable outputs (see \S\ref{sec:repo}).
108	
109	\begin{table}[h]
110	\centering
111	\small
112	\caption{Per-mutation test accuracy (\%) at repo level (SWE-bench Verified, $n{=}9{,}784$). \cls{} 8B reports two seeds; $\Delta$ is mean 4B$\to$8B gain for \cls{}. \cwm{} 4B per-mutation overall accuracy omitted for non-gold mutations due to low parse rates (4.4--56.9\%, Table~\ref{tab:cwm_mutation_parse}); gold overall accuracy derived from parse rate 43.5\% and parseable accuracy 23.5\%.}
113	\label{tab:mutation_breakdown}
114	\resizebox{\columnwidth}{!}{%
115	\setlength{\tabcolsep}{3pt}
116	\begin{tabular}{lccccccc}
117	\toprule
118	\textbf{Mutation} & \textbf{$n$} & \textbf{CLS 4B} & \textbf{CLS 8B s42} & \textbf{CLS 8B s123} & \textbf{CWM 4B} & \textbf{CWM 8B} & \textbf{$\Delta$ CLS} \\
119	\midrule
120	gold & 4,633 & 98.25 & 96.24 & 99.60 & 66.72 & 80.06 & $-$0.33 \\
121	operator\_swap & 3,357 & 78.91 & 81.38 & 82.60 & --- & 54.57 & +3.08 \\
122	off\_by\_one & 183 & 58.47 & 86.89 & 79.20 & --- & 63.39 & \textbf{+24.58} \\
123	return\_value & 562 & 67.97 & 75.44 & 66.40 & --- & 49.11 & +2.95 \\
124	boundary\_removal & 1,049 & 46.90 & 46.90 & 44.90 & --- & 42.23 & $-$1.00 \\
125	\bottomrule
126	\end{tabular}}
127	\end{table}
128	
129	Table~\ref{tab:cwm_mutation_parse} shows that \cwm{} generation quality degrades from 4B to 8B across all mutation types.
130	
131	\begin{table}[h]
132	\centering
133	\small
134	\caption{\cwm{} parse rates and parseable-only accuracy per mutation type (seed 42). Parse rate decreases uniformly from 4B to 8B; parseable-only accuracy is below random binary chance (50\%) for gold at both scales.}
135	\label{tab:cwm_mutation_parse}
136	\setlength{\tabcolsep}{4pt}
137	\begin{tabular}{lcccc}
138	\toprule
139	& \multicolumn{2}{c}{\textbf{Parse Rate (\%)}} & \multicolumn{2}{c}{\textbf{Parse Acc (\%)}} \\
140	\cmidrule(lr){2-3} \cmidrule(lr){4-5}
141	\textbf{Mutation} & \textbf{4B} & \textbf{8B} & \textbf{4B} & \textbf{8B} \\
142	\midrule
143	gold & 43.5 & 23.9 & 23.5 & 16.5 \\
144	operator\_swap & 56.9 & 21.2 & 63.1 & 58.8 \\
145	off\_by\_one & 4.4 & 27.3 & 0.0 & 38.0 \\
146	return\_value & 48.8 & 26.9 & 27.0 & 56.9 \\
147	boundary\_removal & 30.6 & 51.8 & 59.2 & 51.8 \\
148	\bottomrule
149	\end{tabular}
150	\end{table}
151	
152	Key findings: (1)~Gold parse rate collapses from 43.5\% to 23.9\% at 8B; the simplest generation target (unmodified code, where all tests pass) degrades most, consistent with a fundamental generation bottleneck rather than task difficulty. (2)~Among parseable outputs, gold accuracy is 16.5--23.5\%: the model generates outputs that fail exact-match even for correct code. (3)~\texttt{off\_by\_one} is an anomaly: parse rate \emph{increases} from 4.4\% to 27.3\%, but this is from an extremely low base ($n{=}8$ parseable at 4B), making both directions unreliable for this category.
153	
154	\section{Variant-Level Accuracy}
155	\label{app:variant_level}
156	
157	Table~\ref{tab:variant_level} reports variant-level accuracy ($n{=}48$) alongside per-test accuracy for all repo-level configurations. For \cls{}, the aggregation penalty (per-test $\to$ variant-level drop) ranges from 1\pp{} to 19\pp{} and is largest for models with low fail recall under the all-pass rule. \cwm{} variant-level accuracy (48--52\%) falls at or below the majority baseline, consistent with format collapse as the dominant failure mode.
158	
159	\begin{table}[h]
160	\centering
161	\small
162	\caption{Repo-level per-test vs.\ variant-level accuracy ($n{=}48$ variants). Penalty = per-test $-$ variant-level. \traj{} predicts variant outcomes directly (no aggregation). Variant-level majority baseline: 54.17\% (26/48).}
163	\label{tab:variant_level}
164	\setlength{\tabcolsep}{3pt}
165	\resizebox{\columnwidth}{!}{%
166	\begin{tabular}{llcccc}
167	\toprule
168	\textbf{Model} & \textbf{Seed} & \textbf{Per-test (\%)} & \textbf{Variant (\%)} & \textbf{Penalty (\pp{})} & \textbf{Fail Recall (\%)} \\
169	\midrule
170	\multicolumn{6}{l}{\emph{\cls{}}} \\
171	Qwen3-8B & s42 & 84.48 & 72.92 & 11.56 & 56.76 \\
172	Qwen3-8B & s123 & 85.60 & 81.25 & 4.35 & 51.44 \\
173	Qwen3-4B & s42 & 83.63 & 64.58 & 19.05 & 48.72 \\
174	DeepSeek-6.7B & s42 (e1) & 82.61 & 81.25 & 1.36 & 51.02 \\
175	DeepSeek-6.7B & s42 (e3) & 82.51 & 79.17 & 3.34 & 38.47 \\
176	DeepSeek-6.7B & s123 & 74.93 & 56.25 & 18.68 & ${\sim}$13.72 \\
177	\midrule
178	\multicolumn{6}{l}{\emph{\cwm{}}} \\
179	Qwen3-8B & s42 & 65.17 & 52.08 & 13.09 & --- \\
180	DeepSeek-6.7B$^\dagger$ & s123 & --- & 47.92 & --- & --- \\
181	\midrule
182	\multicolumn{6}{l}{\emph{\traj{}}} \\
183	Qwen3-4B & s42 & --- & 72.92 & --- & --- \\
184	Qwen3-8B & s42 & --- & 70.83 & --- & --- \\
185	DeepSeek-6.7B & 3-seed & --- & 77.08 $\pm$ 3.61 & --- & --- \\
186	\midrule
187	Majority & --- & 72.96 & 54.17 & --- & --- \\
188	\bottomrule
189	\end{tabular}}
190	\vspace{2pt}
191	
192	{\footnotesize $^\dagger$Evaluated on ${\sim}$75\% of test instances (7210--7668 of 9784). DeepSeek \traj{} Table~\ref{tab:repo_level} reports 3 seeds (42/123/456) for alignment with \cls{}/\cwm{} seed coverage; three supplementary seeds (0/789/999) yield 75.0\%, 66.7\%, 79.2\% respectively (6-seed mean 75.35 $\pm$ 5.00\%), consistent in direction.}
193	\end{table}
194	
195	\section{Training Hyperparameters}
196	\label{app:hyperparams}
197	
198	Table~\ref{tab:hyperparams} lists all hyperparameters used for fine-tuning. Both \cls{} and \cwm{} share the same LoRA configuration, optimizer, and training schedule; the only differences are per-device batch size, gradient accumulation steps (adjusted to maintain identical effective batch size of 32 across model sizes), and learning rate (DeepSeek-Coder uses $2{\times}10^{-4}$ vs.\ $5{\times}10^{-5}$ for Qwen3, selected via grid search over $\{5{\times}10^{-5}, 1{\times}10^{-4}, 2{\times}10^{-4}\}$ on held-out validation loss).
199	
200	\begin{table}[h]
201	\centering
202	\small
203	\caption{Training hyperparameters for \cls{}/\cwm{} configurations. \traj{} models use lr $= 2{\times}10^{-4}$ due to the smaller training set (${\sim}$8K function-level instances vs.\ ${\sim}$70K for \cls{}/\cwm{}); other hyperparameters are shared.}
204	\label{tab:hyperparams}
205	\resizebox{\columnwidth}{!}{%
206	\begin{tabular}{ll}
207	\toprule
208	\multicolumn{2}{l}{\textbf{Shared across all configurations}} \\
209	\midrule
210	LoRA rank / alpha / dropout & 16 / 32 / 0.05 \\
211	LoRA targets & \texttt{q/k/v/o\_proj} \\
212	Optimizer & AdamW ($\beta_1{=}0.9$, $\beta_2{=}0.999$) \\
213	LR scheduler & Linear \\
214	Effective batch size & 32 \\
215	Max sequence length & 2,048 \\
216	Epochs & 3 \\
217	Precision & bf16 \\
218	Gradient checkpointing & \checkmark \\
219	Seeds (function) & \{42, 123, 456, 789, 0\}\textsuperscript{$b$} \\
220	Seeds (repo) & \{42, 123, 456\}\textsuperscript{$c$} \\
221	\bottomrule
222	\end{tabular}}
223	
224	\vspace{6pt}
225	
226	\resizebox{\columnwidth}{!}{%
227	\begin{tabular}{lccc}
228	\toprule
229	\multicolumn{4}{l}{\textbf{Model-family--specific parameters}} \\
230	\midrule
231	& \textbf{Qwen3-4B} & \textbf{Qwen3-8B} & \textbf{DS-6.7B} \\
232	\midrule
233	Learning rate & 5e-5 & 5e-5 & 2e-4 \\
234	Weight decay & 0.01 & 0.01 & 0.0 \\
235	Warmup ratio & 0.05 & 0.05 & 0.1 \\
236	Batch / grad.\ accum.\ (\cls{}) & 2 / 16 & 1 / 32 & 2 / 16 \\
237	Batch / grad.\ accum.\ (\cwm{}) & 1 / 32 & 1 / 32 & 1 / 32 \\
238	Training samples & 70,748 & 70,748 & 67,343--70,748\textsuperscript{$a$} \\
239	\bottomrule
240	\end{tabular}}
241	
242	\vspace{2pt}
243	{\footnotesize $^a$DeepSeek \cls{} canonical run (s42) uses drop preprocessing, which excludes 3,405 sequences exceeding max length (67,343 of 70,748). The s123 run uses truncate preprocessing (70,748 samples) but produces NaN validation loss. See \S\ref{sec:setup}. $^b$Seeds 789 and 0 use NF4 quantization; others use bf16. $^c$Repo-level seed coverage varies by configuration; see Table~\ref{tab:repo_level} caption for per-model counts.}
244	\end{table}
245	
246	\paragraph{Data processing.} DeepSeek CWM seeds use \texttt{train\_unified.py}, which drops samples exceeding \texttt{max\_seq\_length} (3{,}405 of 70{,}748 samples, 4.8\%). Qwen CWM seeds use \texttt{train\_repo\_cwm.py}, which truncates and retains all samples. This difference affects total training steps (${\sim}$12{,}627 vs.\ ${\sim}$13{,}266 for DeepSeek, ${\sim}$6{,}633 for Qwen) but not the training data distribution, as dropped samples are uniformly distributed across labels.
247	
248	\paragraph{Prompt templates.} Prompt templates for all formulations (\cls{}, \cwm{}, \traj{}) are provided in the code repository. \cls{} uses a binary classification template (``Does this test pass or fail?''); \cwm{} uses an execution simulation template (``What is the output of this test?''); \traj{} uses a variant-level verdict template (``Is this patch resolved or unresolved?'').
249	
250	\paragraph{Mutation operators.} We use five mutation types: (1)~\emph{gold}: unmodified code (all tests pass); (2)~\emph{operator\_swap}: replaces comparison or arithmetic operators (e.g., \texttt{<} $\to$ \texttt{<=}); (3)~\emph{off\_by\_one}: shifts loop bounds or array indices by $\pm$1; (4)~\emph{return\_value}: modifies return statements (e.g., negating a boolean, changing a constant); (5)~\emph{boundary\_removal}: removes conditional guards or boundary checks. Mutation operators were applied using AST-level transformation; variants that did not alter any test outcome were discarded.
251	
252	\paragraph{Compute budget.}
253	All experiments were conducted on NVIDIA RTX 5090 GPUs. Training time is approximately 1.5 hours per run for 4B models and 2 hours for 8B models. Total compute budget: ${\sim}$370 GPU-hours across 223 completed runs (135 successful, 88 failed/killed; ${\sim}$46 unique configurations including seeds, formulations, model sizes, and ablations).
254	
255	\section{Prompt Templates}
256	\label{app:prompts}
257	
258	We show representative prompt examples for each formulation. All examples use the same input instance for comparability.
259	
260	\paragraph{CLS (per-test classification).}
261	\begin{verbatim}
262	System: You are a code verifier. Given a
263	code patch and a test name, predict whether
264	the test will pass or fail when run against
265	the patched code.
266	
267	User:
268	## Patch (git diff)
269	&lt;patch content>
270	[... truncated ...]
271	
272	## Test
273	test_boundary_check
274	
275	Will this test pass or fail?
276	
277	Target: pass
278	\end{verbatim}
279	
280	\paragraph{CWM (execution simulation).}
281	\begin{verbatim}
282	System: You are a code execution simulator.
283	Given a code snippet and a test case,
284	predict the execution result.
285	
286	User:
287	## Code
288	&lt;code content>
289	[... truncated ...]
290	
291	## Test
292	test_boundary_check
293	
294	What is the execution result?
295	
296	Target: PASS: test completed successfully
297	\end{verbatim}
298	
299	\paragraph{TRAJ (trajectory scoring).}
300	\begin{verbatim}
301	System: You are a code repair verifier.
302	Given the code patch and test summary,
303	predict whether all tests pass (resolved)
304	or any test fails (unresolved).
305	
306	User:
307	[Code]
308	&lt;patch content>
309	[... truncated ...]
310	
311	[Test Summary]
312	&lt;all test names and descriptions>
313	
314	Target: resolved
315	\end{verbatim}
316	
317	\cls{} and \cwm{} share the same input format (one code--test pair per instance); \cls{} produces a single token (\texttt{pass}/\texttt{fail}), while \cwm{} generates a variable-length execution trace. \traj{} receives all tests concatenated and produces a single token (\texttt{resolved}/\texttt{unresolved}).
318	
319	
320	\section{Val-Test Mutation Type Distribution}
321	\label{app:mutation_distribution}
322	
323	Table~\ref{tab:mutation_distribution} reports the mutation type composition of the repo-level validation and test sets. The most notable shift is \texttt{operator\_swap}, which nearly doubles from val (19.1\%) to test (34.3\%), while \texttt{off\_by\_one} shrinks from 10.0\% to 1.9\%.
324	
325	\begin{table}[h]
326	\centering
327	\small
328	\caption{Repo-level mutation type distribution: validation vs.\ test set, with per-type \cls{} accuracy at two model sizes (seed 42). Shift = test\% $-$ val\%.}
329	\label{tab:mutation_distribution}
330	\setlength{\tabcolsep}{3pt}
331	\resizebox{\columnwidth}{!}{%
332	\begin{tabular}{lccccc}
333	\toprule
334	\textbf{Mutation Type} & \textbf{Val (\%)} & \textbf{Test (\%)} & \textbf{Shift} & \textbf{\cls{} 4B} & \textbf{\cls{} 8B} \\
335	\midrule
336	gold & 45.2 & 47.4 & +2.2 & 98.3 & 96.2 \\
337	operator\_swap & 19.1 & 34.3 & +15.2 & 78.9 & 81.4 \\
338	boundary\_removal & 15.0 & 10.7 & $-$4.3 & 46.9 & 46.9 \\
339	return\_value & 10.7 & 5.7 & $-$5.0 & 68.0 & 75.4 \\
340	off\_by\_one & 10.0 & 1.9 & $-$8.1 & 58.5 & 86.9 \\
341	\bottomrule
342	\end{tabular}}
343	\end{table}
344	
345	The \texttt{operator\_swap} shift is the primary source of val-test distribution mismatch. Since \cls{} achieves moderate accuracy on this type (78.9--81.4\%), the over-representation in the test set does not systematically bias overall accuracy estimates in either direction. Two boundary observations are notable: (1)~\texttt{boundary\_removal} represents a scale-invariant difficulty ceiling at ${\sim}$47\% across both model sizes: this mutation type resists capacity scaling; (2)~\texttt{off\_by\_one} shows the largest scaling gain (+28.4\pp{}, 58.5\%$\to$86.9\%) but its small test share (1.9\%) limits its contribution to overall accuracy differences across scales.
346	
347	\section{Qualitative Error Analysis}
348	\label{app:qualitative}
349	
350	To complement the quantitative divergence reported in \S\ref{sec:repo}, we examine representative errors from each formulation at repository level.
351	
352	\paragraph{\cwm{} failure modes.}
353	Two patterns account for the majority of unparseable \cwm{} outputs on Qwen3. (1)~\emph{Task misunderstanding}: the model generates a complete simulated test runner log (test names, timing, summary lines) rather than a pass/fail verdict. For instance, on \texttt{django\_\_django-14315}, the model outputs a fabricated 1,248-token Django test execution trace with hallucinated test names that do not exist in the target file. The model confuses ``predict test outcome'' with ``simulate test execution environment.'' (2)~\emph{Autoregressive degeneration}: the model enters a repetitive loop (e.g., repeating \texttt{from \_pytest.config import \_parse\_pytest\_args} until truncation at 4,542 tokens). Both patterns produce zero usable signal and default to the majority-class label. This explains why unparseable predictions carry higher accuracy than parseable ones (\S\ref{sec:repo}).
354	
355	\paragraph{\cls{} failure modes.}
356	\cls{} errors concentrate in two categories requiring multi-step reasoning. False positives arise from \emph{cross-concern value propagation}: a boundary removal mutation in \texttt{pytest} converts a guarded attribute access (\texttt{if xfailed and not xfailed.run}) to \texttt{if True:}, causing a NoneType error on tests exercising unrelated skip marks. The model fails to trace the None path through the pytest hook lifecycle. False negatives arise from \emph{mathematical equivalence}: on \texttt{HumanEval/130} (Tribonacci variant), the model predicts failure for correct code because verifying the self-referential recurrence requires algebraic substitution rather than syntactic inspection. This single problem accounts for 17\% of all function-level false negatives.
357	
358	\paragraph{Complementarity.}
359	These failure patterns operate at different levels: \cwm{} fails at the format level (producing no usable signal), while \cls{} fails at the reasoning level (producing a confident but incorrect binary verdict). Both formulations are FP-dominant (over-predict failure), but \cwm{}'s higher FP rate (70.3\% vs.\ 56.5\%) means it over-predicts failure on instances \cls{} correctly classifies, producing partial complementarity (oracle combination: 90.63\%; \S\ref{app:extended_analysis}, paragraph a).
360	
361	\section{Extended Analysis}
362	\label{app:extended_analysis}
363	
364	\paragraph{Function-level CWM metric robustness.}
365	At function level, \cwm{} outputs are short status strings (mean ${\sim}$5--15 tokens). The unparseable rate is only 1.39\%, and default-to-pass bias is $<$1\pp{}---well below the SESOI threshold. Exact string matching is appropriate for these short, structured outputs; semantic-but-format-different matches are rare given the constrained output space.
366	
367	\paragraph{(a) Error complementarity.}
368	\cls{} and \cwm{} are both FP-dominant at function level but at different rates, producing partial complementarity. Among \cls{} errors (seed 42), 56.5\% are false positives (PASS $\to$ FAIL); among \cwm{} errors, 70.3\% are false positives. Both formulations over-predict failure, but \cwm{}'s stronger FP bias means it incorrectly rejects passing tests that \cls{} correctly accepts. An oracle combination achieves 90.63\% accuracy (1713/1890 correct, 177 both-wrong; +2.80\pp{} over the best single formulation, \cls{} 87.83\%; single-seed estimate, seed 42). The complementarity arises from different \emph{degrees} of fail-bias rather than opposite error directions: \cwm{}'s generation bottleneck produces aggressive failure predictions, while \cls{}'s single-token output is more calibrated. Ensemble approaches exploiting this degree difference are a natural direction.
369	
370	\paragraph{(b) CWM error mode breakdown.}
371	Among unparseable \cwm{} outputs (Qwen3, repo-level), 76.9\% contain no execution keywords; 22.9\% contain ambiguous co-occurring pass/fail keywords. Format compliance varies sharply across repositories (scikit-learn: near-zero unparseable; sphinx: 100\%); repository-specific code patterns interact with the model's generation capabilities in complex ways. This per-repository variation is consistent with a model/tokenizer-specific failure rather than a formulation-level one.
372	
373	\paragraph{(c) Relaxed matching does not rescue \cwm{}.}
374	Relaxed matching (tolerating format deviations, L0--L4) \emph{decreases} \cwm{} accuracy: 58.04\%$\to$56.98\% (seed 42) and 59.09\%$\to$55.91\% (seed 123). Unparseable predictions default to the majority class (pass, 72.96\%), which outperforms the model's own parseable predictions (38--43\%). The divergence widens from 26\pp{} to 27\pp{} under relaxed matching. This rules out the hypothesis that parsing strictness inflates the observed gap. Constrained decoding~\cite{willard2023outlines} could enforce format compliance but would not address the semantic accuracy deficit among parseable outputs. An accidental training artifact provides further evidence: a \cwm{} model inadvertently trained on function-level (\cls{}-format) data achieved 86.05\% accuracy with 0\% unparseable outputs at repo level---recovering \cls{}-level performance. This confirms that the repo-level \cwm{} degradation stems entirely from trace generation complexity, not from the underlying verification task.
375	
376	\paragraph{(d) Variance compression.}
377	\cwm{}'s 5-seed standard deviation (0.37\pp{}) is lower than \cls{} (0.78\pp{}) and \traj{} (0.97\pp{}) at function level. If \cwm{} performance is capped by output-format constraints at a given complexity level, seed-to-seed variability is compressed relative to formulations whose performance depends more on learned representations.
378	
379	\paragraph{(e) Per-test precision and recall.}
380	\cls{} achieves fail \fone{} 87.59\% (precision 86.20\%, recall 89.04\%) at seed 42.% derived from overlap analysis (error_overlap_matched_seed.json); FP=130, FN=100, TP=848, TN=812
381	Multi-F2P instances (6--10 tests) reach 96.3\% accuracy, consistent with the oracle finding that per-test granularity is most valuable for complex instances.
382	
383	\paragraph{(f) Block correlation.}
384	Within-problem errors are correlated (ICC $= 0.191$, DEFF $= 3.97$, 2.81$\times$ more all-correct problems than i.i.d.\ expectation). All statistical tests use clustered bootstrap accordingly.
385	
386	\paragraph{(g) Failed interventions.}
387	We systematically tested four interventions targeting different hypothesized causes of \cwm{} repo-level degradation; all failed:
388	
389	\begin{itemize}[leftmargin=*,itemsep=1pt,topsep=2pt]
390	\item \textbf{Capacity (rank 32, $\alpha{=}64$):} $-$0.47\pp{}, within seed variance (\S\ref{app:ablations}).
391	\item \textbf{Majority voting ($K{=}3$):} $-$0.68\pp{}; 93.3\% unanimous, net flips negative (\S\ref{app:ablations}).
392	\item \textbf{Relaxed matching (L0--L4):} $-$1.06\pp{}; default-pass outperforms parseable predictions (paragraph~(c) above).
393	\item \textbf{Model scaling (4B$\to$8B):} parseable accuracy decreases (42.88\%$\to$38.52\%) while unparseable rate rises (53.7\%$\to$73.8\%); gain is a default-assignment artifact (\S\ref{sec:repo}).
394	\end{itemize}
395	
396	\noindent Each intervention targets a distinct alternative explanation (insufficient capacity, random noise, parsing strictness, model scale); the uniform failure across all four confirms the bottleneck is formulation-level---output space complexity at repo level exceeds what ${\leq}$8B generation models can handle, independent of these surface-level factors.
397	
398	\paragraph{(h) Per-mutation scaling patterns.}
399	Scaling benefits are highly non-uniform across mutation types (Table~\ref{tab:mutation_breakdown}). \texttt{off\_by\_one} shows the largest \cls{} scaling gain: 58.5\% (4B) to 86.9\% (8B, $+$28.4\pp{}). In contrast, \texttt{boundary\_removal} is scale-invariant at ${\sim}$47\% across both sizes, which marks an intrinsic difficulty ceiling. For \cwm{}, gold mutation parse rate collapses from 43.5\% (4B) to 23.9\% (8B) despite being the simplest target: generation capability degrades even for trivially correct code at larger scale within Qwen3. The val-test mutation type distribution differs notably (\texttt{operator\_swap} shifts from 19.1\% to 34.3\%; Table~\ref{tab:mutation_distribution}), but this shift does not systematically bias overall accuracy because \cls{} performance on \texttt{operator\_swap} (78.9--81.4\%) is close to the overall mean.
400	
401	\paragraph{(i) Inference efficiency.}
402	\cls{} achieves 217$\times$ higher throughput than \cwm{} at repo level (853 vs.\ 3.9 inferences/min; Qwen3-4B, RTX 5090, 100 samples, avg ${\sim}$1,040 input tokens). The speedup derives directly from the formulation: classification requires a single output token, whereas \cwm{} generates an average of 477 tokens per inference. Median latency is 48ms (\cls{}) vs.\ 16.3s (\cwm{}). At the observed unparseable rate of 73.8\% (8B), the majority of \cwm{}'s generation budget produces tokens that cannot yield a valid verdict. This \cls{}--\cwm{} efficiency gap is an inherent property of the formulation difference (1 vs.\ $O(L)$ output tokens) and should generalize across models, unlike the accuracy divergence which may be model-contingent.
403	
404	The \cls{}--\traj{} efficiency comparison is more nuanced, because \cls{} makes one call per test while \traj{} makes one call per instance. Per-call, \cls{} is 20--138$\times$ faster (depending on input length: 47ms for short contexts vs.\ 2,632ms for \traj{}). However, the per-instance effective speedup depends on test count $|T|$: at function level ($|T| \approx 2.3$), \cls{} is ${\sim}$24$\times$ faster (108ms vs.\ 2,632ms per instance); at repo level ($|T| \approx 12.3$, ${\sim}$70ms/call with longer inputs), \cls{} is ${\sim}$3$\times$ faster (861ms vs.\ 2,631ms). A crossover exists at $|T| \approx 50$ tests, beyond which \traj{}'s single-call amortization dominates. This boundary condition is informative for deployment: \cls{} is strongly preferred for function-level and moderate repo-level test suites, while extremely large test suites ($>$50 tests per instance) favor trajectory-level efficiency despite its coarser diagnostic signal.
405	
406	\paragraph{(j) Re-repair pilot.}
407	We tested whether per-test diagnostic feedback improves downstream repair. A Qwen3-8B repair agent received either per-test diagnostic signals (which specific tests failed and why) or binary accept/reject feedback, evaluated on 44 SWE-bench Verified instances. The diagnostic condition achieved accuracy no higher than the binary baseline ($A_1 = 52.3\%$, $p = 0.42$, effect size $\approx 0$). Per-test diagnostic information does not automatically translate to repair improvements at this scale. The negative result may reflect insufficient agent capability to exploit fine-grained feedback, insufficient sample size (at $n = 44$, statistical power is ${\sim}$0.3 for a medium effect size), or a genuine limitation of the diagnostic-to-repair translation.
408	
409	\paragraph{(k) Relationship to chain-of-thought verification.}
410	\cwm{} is structurally a chain-of-thought verifier: the model generates an execution trace token by token and derives its PASS/FAIL verdict from the final trace state. If intermediate reasoning improved verification, \cwm{} should outperform the reasoning-free \cls{} baseline. At function level, no such advantage materialises: \cwm{} and \cls{} are statistically equivalent (TOST $p{=}0.007$, $\pm$2\pp{} margin; \S\ref{sec:equivalence}), indicating that the additional trace generation provides no accuracy benefit over direct binary classification. At repo level, the chain-of-thought mechanism actively \emph{hurts}: trace generation triggers format collapse (53--74\% unparseable), and even parseable traces yield accuracy below the majority baseline (38--43\% vs.\ 72.96\%; paragraph~(c)). Four targeted interventions fail to rescue the generation pathway (paragraph~(g)). Within the ${\leq}$8B LoRA regime, chain-of-thought--style verification does not outperform direct classification for execution prediction. Whether execution-trace pretraining at larger scale~\cite{meta2025cwm} changes this conclusion remains the primary open question (\S\ref{sec:threats}).
411	
412	\section{TOST Margin Sensitivity}
413	\label{app:tost_sensitivity}
414	
415	Table~\ref{tab:tost_sensitivity} reports the TOST equivalence $p$-value as a function of the equivalence margin, computed on the 5-seed variant-level \cls{}--\cwm{} comparison (gap $= 1.24$\pp{}, 523 variants, 114 clusters, clustered bootstrap).
416	
417	\begin{table}[h]
418	\centering
419	\small
420	\caption{TOST margin sensitivity for \cls{}--\cwm{} variant-level equivalence (5 seeds, 523 variants, 114 clusters). The smallest margin achieving equivalence at $\alpha = 0.05$ is $\pm$1.52\pp{}.}
421	\label{tab:tost_sensitivity}
422	\setlength{\tabcolsep}{4pt}
423	\begin{tabular}{ccc}
424	\toprule
425	\textbf{Margin ($\pm$\pp{})} & \textbf{$p$-value} & \textbf{Equivalent ($\alpha{=}0.05$)?} \\
426	\midrule
427	1.0 & $\gg$0.05 & No \\
428	1.5 & 0.054 & No (borderline) \\
429	\textbf{1.52} & ${\sim}$\textbf{0.05} & \textbf{Smallest margin} \\
430	1.71 & 0.027 & Yes \\
431	2.0 & 0.007 & Yes \\
432	3.0 & $4.6{\times}10^{-5}$ & Yes \\
433	5.0 & $\ll$0.001 & Yes \\
434	\bottomrule
435	\end{tabular}
436	\end{table}
437	
438	The minimum equivalence margin is $\pm$1.52\pp{}, 0.48\pp{} below our pre-specified $\pm$2\pp{} threshold. The $\pm$2\pp{} threshold was set based on deployment relevance rather than observed data: at function-level accuracy (85--88\%), a 2\pp{} per-test difference corresponds to ${\sim}$38 additional errors across 1,890 tests (${\sim}$2--3 problems out of 114), comparable in magnitude to between-seed standard deviation (0.37--0.97\pp{}) and checkpoint selection noise ($<$1\pp{}). Differences within this range do not reliably distinguish formulations from training noise in pipeline selection decisions. For \cls{}--\traj{}, the TOST at $\pm$2\pp{} yields $p{=}0.025$, nominally significant but not surviving Holm-Bonferroni correction at $k{=}5$ (Table~\ref{tab:holm}).
439	
440	\paragraph{Bayesian ROPE analysis.}
441	\label{app:bayesian_rope}
442	To complement the frequentist TOST, we conduct a Bayesian equivalence analysis using a paired $t$-test with Jeffreys prior~\cite{kruschke2013bayesian,kruschke2018rejecting}. The marginal posterior for the mean accuracy difference follows a $t$-distribution with $n{-}1$ degrees of freedom. For \cls{}--\cwm{}, the posterior probability within the $\pm$2\pp{} ROPE is $P(\text{ROPE}) = 0.975$, and the 95\% highest density interval (HDI $= [{+}0.10, {+}2.00]$\,pp) falls entirely inside the ROPE, confirming equivalence under both continuous and HDI-based decision criteria. For \cls{}--\traj{} at per-test level, $P(\text{ROPE}) = 0.542$ (inconclusive; 95\% HDI $= [{+}0.35, {+}3.52]$\,pp extends beyond the ROPE), consistent with the TOST non-confirmation after Holm correction ($p_{\text{adj}} = 0.075$). At variant level, \cls{}--\traj{} equivalence is supported by the Bayesian criterion ($P(\text{ROPE}) = 0.970$, HDI $= [{-}2.00, {+}1.03]$\,pp), but the frequentist TOST does not confirm equivalence after Holm-Bonferroni correction ($p_{\text{adj}} = 0.075$; Table~\ref{tab:holm}). This discrepancy reflects differing treatments of multiplicity: Bayesian ROPE evaluates each comparison independently, while Holm correction penalizes across all $k{=}5$ primary tests. For \cls{}--\cwm{}, both frameworks agree (TOST $p_{\text{adj}}{=}0.028$, $P(\text{ROPE}){=}0.975$); for \cls{}--\traj{} per-test, both are inconclusive. We conservatively follow the Holm-corrected TOST in the main text and report \cls{}--\traj{} equivalence as not confirmed.
443	
444	
445	\section{Variant-Level Effect Sizes}
446	\label{app:power}
447	
448	Table~\ref{tab:variant_power} reports variant-level bootstrap confidence intervals for the repo-level formulation comparisons ($n{=}48$ variants). Following Hoenig and Heisey~\cite{hoenig2001}, we report minimum detectable effect (MDE) rather than post-hoc observed power.
449	
450	\begin{table}[h]
451	\centering
452	\small
453	\caption{Variant-level bootstrap analysis ($n{=}48$). \cls{}--\cwm{} uses paired bootstrap (same variants, same seed); \cls{}--\traj{} uses unpaired bootstrap (per-variant \traj{} predictions not archived for pairing). MDE at $n{=}48$: ${\sim}$25\pp{}.}
454	\label{tab:variant_power}
455	\setlength{\tabcolsep}{3pt}
456	\resizebox{\columnwidth}{!}{%
457	\begin{tabular}{llccc}
458	\toprule
459	\textbf{Comparison} & \textbf{Config} & \textbf{$\Delta$ (\pp{})} & \textbf{95\% CI} & \textbf{$p$} \\
460	\midrule
461	\multicolumn{5}{l}{\emph{\cls{} vs.\ \cwm{} (paired)}} \\
462	& Qwen3-8B & +29.17 & [10.42, 47.92] & 0.003 \\
463	& DeepSeek-6.7B & +35.42 & [18.75, 50.05] & ${<}$0.001 \\
464	\midrule
465	\multicolumn{5}{l}{\emph{\cls{} vs.\ \traj{} (unpaired)}} \\
466	& Qwen3-4B & $-$4.17 & wide & 0.740 \\
467	& Qwen3-8B & +8.33 & wide & 0.385 \\
468	& DeepSeek-6.7B & 0.00 & wide & 1.000 \\
469	\bottomrule
470	\end{tabular}}
471	\end{table}
472	
473	At $n{=}48$, the MDE is ${\sim}$25\pp{}. The \cls{}--\cwm{} gap (29--35\pp{}) exceeds this threshold, confirming that $n{=}48$ is sufficient to detect the observed divergence. The \cls{}--\traj{} gaps ($<$10\pp{}) fall well below the MDE: any true difference is too small to detect at this sample size, consistent with the function-level TOST equivalence (\S\ref{sec:equivalence}).
474	
475	The \cls{}--\traj{} unpaired bootstrap produces wider confidence intervals than paired analysis would; \traj{} per-variant predictions were not archived in a format that permits pairing. The \cls{}--\cwm{} paired comparison uses \cls{} s123 vs.\ \cwm{} s42 (different seeds), but the CI lower bound of 10.42\pp{} far exceeds the seed noise observed in function-level experiments ($<$2\pp{}).
476	
477	
478	\section{Multiple Comparison Correction}
479	\label{app:holm}
480	
481	Table~\ref{tab:holm} applies Holm-Bonferroni correction~\cite{holm1979} to the five primary statistical comparisons across this study ($k{=}5$, family-wise $\alpha{=}0.05$).
482	
483	\begin{table}[h]
484	\centering
485	\small
486	\caption{Holm-Bonferroni correction for primary comparisons ($k{=}5$). Comparisons ranked by raw $p$-value; each tested against $\alpha / (k - \text{rank} + 1)$.}
487	\label{tab:holm}
488	\setlength{\tabcolsep}{3pt}
489	\resizebox{\columnwidth}{!}{%
490	\begin{tabular}{clcccc}
491	\toprule
492	\textbf{Rank} & \textbf{Comparison} & \textbf{Raw $p$} & \textbf{Factor} & \textbf{Adj $p$} & \textbf{Sig.?} \\
493	\midrule
494	1 & Repo: \cls{} vs \cwm{} & 0.003 & $\times$5 & 0.015 & \checkmark \\
495	2 & Func: \cls{} vs \cwm{} (TOST $\pm$2\pp{}) & 0.007 & $\times$4 & 0.028 & \checkmark \\
496	3 & Func: \cls{} vs \traj{} (TOST $\pm$2\pp{}) & 0.025 & $\times$3 & 0.075 & --- \\
497	4 & Repo: \cwm{} vs \traj{} & 0.039 & $\times$2 & 0.078 & --- \\
498	5 & Repo: \cls{} vs \traj{} & 0.385 & $\times$1 & 0.385 & --- \\
499	\bottomrule
500	\end{tabular}}
501	\end{table}
502	
503	The two core claims survive correction: the repo-level \cls{}--\cwm{} divergence (adjusted $p{=}0.015$) and function-level \cls{}--\cwm{} equivalence (adjusted $p{=}0.028$). The function-level \cls{}--\traj{} equivalence does not survive correction (adjusted $p{=}0.075$); we interpret this as directionally consistent but not confirmatory.
504	
505	\section{Mixed-Effects Regression}
506	\label{app:interaction}
507	
508	We fit mixed-effects linear probability models (LPM) with heteroskedasticity-robust standard errors (HC1) to test the formulation$\times$complexity interaction formally~\cite{moulton1990}. We choose LPM because coefficients are directly interpretable as probability differences (percentage points), consistent with the reporting units in the main text; at these sample sizes ($n{\approx}56$K cross-complexity, repo-level pooled cross-model) and base rate range (0.6--0.9), LPM and logistic regression yield concordant conclusions for all primary effects~\cite{angrist2009mostly} (confirmed below).
509	
510	\paragraph{Cross-complexity model (DeepSeek-Coder).} \texttt{correct $\sim$ formulation $\times$ complexity + (1|problem\_id)}, $n{=}56{,}480$ observations (\cls{} + \cwm{} $\times$ function + repo), 139 problem clusters. The \cwm{} main effect at function level is non-significant ($\hat{\beta}{=}-0.002$, $z{=}-0.25$, $p{=}0.805$); the \cwm{}$\times$repo interaction is highly significant ($\hat{\beta}{=}-0.219$, $z{=}-23.7$, $p{<}0.001$). \cwm{} and \cls{} are statistically indistinguishable at function level ($\Delta{=}-0.2$\pp{}, $p{=}0.805$) but diverge by 22\pp{} at repo level, confirming the complexity-dependent divergence is not an artifact of aggregation.
511	
512	\paragraph{Repo-level cross-model model.} \texttt{correct $\sim$ formulation $\times$ model + (1|problem\_id)}, both model families, repo level only. \cwm{} deficit: $\hat{\beta}{=}-0.22$ ($-$22\pp{}, $z{=}-64.4$, $p{<}0.001$). Model effect: +1.1\pp{} for Qwen3 ($z{=}3.1$, $p{=}0.002$ in LPM; not significant under GEE, $p{=}0.449$). Formulation$\times$model interaction: +1.6\pp{} less \cwm{} degradation on Qwen3 ($z{=}2.8$, $p{=}0.006$ in LPM; not significant under GEE, $p{=}0.860$). Formulation dominates the predictable variance; model identity is directionally positive but specification-dependent. The 25-cluster random intercept structure limits effective degrees of freedom for the random effects; inferences on fixed effects (formulation, complexity) are robust as they pool across the full observation count.
513	
514	\paragraph{Logistic regression robustness check.} To verify that LPM conclusions are not artifacts of the linear link function, we fit GEE logistic regression (binomial family, exchangeable working correlation, robust sandwich standard errors) to the same data. For the cross-complexity model, the \cwm{} main effect at function level has OR$=$0.98 (95\% CI [0.86, 1.12], $p{=}0.771$) and the \cwm{}$\times$repo interaction has OR$=$0.31 ([0.15, 0.65], $p{=}0.002$). Average marginal effects are $-$0.2\pp{} (function) and $-$21.6\pp{} (repo), matching LPM coefficients within 0.3\pp{}. For the cross-model model, the \cwm{} deficit has OR$=$0.30 ([0.15, 0.63], $p{=}0.001$, AME$=$\,$-$21.1\pp{}). Direction, magnitude, and significance of all primary effects are concordant between LPM and logistic regression; minor discrepancies in secondary effects (model identity, formulation$\times$model interaction: $p{=}0.449$ and $p{=}0.860$ under GEE vs.\ $p{=}0.002$ and $p{=}0.006$ under LPM) reflect the GEE's more conservative cluster-robust inference with $k{=}25$ clusters. The discrepancy in secondary effects reflects cluster count: the cross-complexity model ($k{=}139$) yields reliable sandwich SEs, while the cross-model model ($k{=}25$) falls below the $k{\geq}40$ threshold recommended for stable cluster-robust inference~\cite{cameron2008bootstrap}.
515	
516	\section{CWM Parseable Bias Analysis}
517	\label{app:parseable_bias}
518	
519	The default-to-pass assignment for unparseable \cwm{} outputs is not random with respect to instance difficulty. Unparseable instances have significantly higher pass rates than parseable ones (74.6\% vs.\ 68.3\%, $\chi^2$ $p = 5.9 \times 10^{-10}$), and \cls{} models achieve higher accuracy on unparseable instances (86.4\% vs.\ 79.1\%, $p = 3.3 \times 10^{-18}$). This indicates that \cwm{}'s parsing failures concentrate on simpler, pass-heavy instances where the majority-class default happens to be correct more often. Cross-model Jaccard overlap of unparseable instance sets is 0.46, confirming this pattern is instance-driven (specific inputs consistently cause parsing failure across models) rather than stochastic. The net effect is that \cwm{}'s reported accuracy is inflated by default-correct assignments on easy instances, while its effective discriminative accuracy on harder instances is substantially lower than the aggregate figure suggests.
520	
521	
522	\section{Threats to Validity (Full Analysis)}
523	\label{app:threats}
524	
525	We identify five potential confounds and assess their impact on our conclusions.
526	
527	\paragraph{Checkpoint selection.} Val-based selection is unavailable for runs with NaN validation loss (all \cwm{} repo-level runs, DeepSeek \cls{} s123), which default to the final epoch checkpoint. A checkpoint ablation on Qwen3-8B \cls{} s42 quantifies this confound: epoch~1 (ckpt-2200) achieves 85.34\%, val-selected (ckpt-3600) 84.48\%, and final epoch (ckpt-6633) 85.29\%---a $<$1\pp{} range. The val-selected checkpoint is the lowest, indicating no upward bias from checkpoint selection. The Qwen3-8B \traj{} comparison (epoch 2: 72.92\% vs.\ epoch 3: 70.83\%) shows a slightly larger ${\sim}$2\pp{} shift. For \cwm{}, the convergence analysis (Appendix~\ref{app:cwm_convergence}) shows eval loss at the final epoch is 1.8$\times$ its minimum; however, early-stopped checkpoints retain high unparseable rates, leaving the qualitative ranking unchanged.
528	
529	\paragraph{\cwm{} convergence analysis.}
530	\label{app:cwm_convergence}
531	Qwen3-8B \cwm{} repo-level eval loss reaches its minimum within ${\sim}$5\% of training (step 300--400 of 6{,}633) and increases monotonically thereafter, with no plateau or recovery (Table~\ref{tab:cwm_convergence}). This pattern is consistent across all three seeds, confirming systematic overfitting to trace generation rather than stochastic variation. The final-epoch eval loss is ${\sim}$1.8$\times$ the optimal value. By contrast, function-level \cwm{} achieves \cls{}-equivalent accuracy (TOST $p{=}0.007$) with the same training recipe, indicating that the overfit is specific to repo-level output complexity. Cross-model validation: a DeepSeek-Coder early-stopped checkpoint (s123, epoch~1) achieves 75.45\% versus 57.31\% at epoch~3 (s123; +18.14\pp{}), but retains 66.4\% unparseable rate, confirming that format collapse emerges early and is not a late-training artifact. No epoch-level checkpoint is available for Qwen3 CWM (only step-level checkpoints at steps 300/400 and late steps ${\geq}$5800; continuous epoch checkpointing was not enabled for this training run). The convergence analysis (Table~\ref{tab:cwm_convergence}) shows eval loss minimum at step 300--400 across all three Qwen3 seeds, consistent with DeepSeek-Coder's epoch-1 improvement, providing cross-model evidence that the overtraining pattern generalizes.
532	
533	\begin{table}[h]
534	\centering
535	\small
536	\caption{\cwm{} repo-level eval loss across training (Qwen3-8B, 3 seeds). Minimum is reached at step 300--400 (${\sim}$5\% of training); subsequent training monotonically increases loss.}
537	\label{tab:cwm_convergence}
538	\begin{tabular}{lccc}
539	\toprule
540	Step & s42 & s123 & s456 \\
541	\midrule
542	300 & 0.291 & \textbf{0.288} & \textbf{0.277} \\
543	400 & \textbf{0.286} & 0.306 & 0.283 \\
544	1000 & 0.333 & 0.336 & 0.351 \\
545	3000 & 0.445 & 0.453 & 0.435 \\
546	6600 & 0.521 & 0.517 & 0.507 \\
547	\bottomrule
548	\end{tabular}
549	\end{table}
550	
551	\paragraph{Evaluation sequence length.} \cwm{} accuracy varies by ${\sim}$9\pp{} across evaluation sequence lengths for the same checkpoint (seq2048: ${\sim}$65\% vs.\ seq4096: ${\sim}$56\%), driven by unparseable-rate differences that propagate through majority-class default assignment. \cls{} is invariant to this parameter. Cross-model \cwm{} comparisons use different eval lengths (Qwen3: 8192, DeepSeek: 4096) and are not directly comparable in absolute terms. A matched-sequence evaluation shows ${\sim}$1.5\pp{} difference for \cls{} (Appendix~\ref{app:ablations}), insufficient to explain the 18--26\pp{} gap. Furthermore, increasing Qwen3-8B \cwm{} evaluation from seq4096 to seq8192 \emph{raises} the unparseable rate (63.7\%$\to$73.8\%) while changing accuracy by only 0.81\pp{} (64.36\%$\to$65.17\%); giving the model more generation budget worsens format compliance rather than improving it, confirming that format collapse is a structural bottleneck rather than a truncation artifact. Practitioners must standardize evaluation sequence length for generation-based formulations.
552	
553	\paragraph{Preprocessing.} DeepSeek \cls{} accuracy ranges from 82.61\% (s42, drop preprocessing) to 74.93\% (s123, truncate preprocessing), a 7.68\pp{} spread that conflates preprocessing strategy, checkpoint selection method, and seed. The two strategies produce different effective training sets (67,343 vs.\ 70,748 samples) and different checkpoint selection regimes. The qualitative ranking \cls{} $>$ \cwm{} holds under both strategies (Table~\ref{tab:taxonomy}).
554	
555	\paragraph{\traj{} training regime.} \traj{} uses a different training configuration: smaller training set (${\sim}$400 repo-level variants vs.\ ${\sim}$70K per-test instances), higher learning rate ($2{\times}10^{-4}$ vs.\ $5{\times}10^{-5}$), and variant-level labels. This asymmetry is inherent to the formulation (trajectory-level labels are only available at variant granularity), but precludes training-data-controlled comparison at repo level. The downsample ablation confirms the \cls{} formulation advantage persists at matched data volume (80.74\% vs.\ 72.92\%; Appendix~\ref{app:downsample}), though it controls for training volume but not label granularity (per-test vs.\ variant-level). Crucially, \traj{} achieves statistical equivalence with \cls{} at function level (${\leq}$1.3\pp{}, \S\ref{sec:func_results}), demonstrating the formulation itself is viable; the repo-level gap attribution remains uncertain: data volume (${\sim}$400 variants vs.\ ${\sim}$70K per-test instances) and label granularity (variant-level vs.\ per-test) are both plausible confounds that cannot be separately controlled.
556	
557	\paragraph{\cwm{} scale and pretraining.} Our \cwm{} baseline uses 4--8B LoRA fine-tuning without execution trace pretraining. The original Code World Model~\cite{meta2025cwm} uses 32B parameters with mid-training on execution traces, a fundamentally different training regime. At larger scale or with execution-trace pretraining, the generation bottleneck observed here may diminish: larger models produce more coherent long-form outputs, and execution trace exposure may improve output format compliance. This is the primary limitation: all repo-level \cwm{} conclusions are conditional on the ${\leq}$8B LoRA regime.
558	
559	Despite these confounds, the repo-level \cls{}--\cwm{} gap (18--26\pp{}) exceeds any single assessed confound. Even under worst-case compounding (${\sim}$11.5\pp{}), the gap retains ${\geq}$7.5\pp{} margin; confounds predominantly disadvantage \cwm{}. However, correlated confounds and limited seed coverage mean definitive causal attribution requires multi-seed replication. At $n{=}48$, the minimum detectable effect (MDE) is ${\sim}$25\pp{}~\cite{hoenig2001}; the \cls{}--\cwm{} gap (29--35\pp{}) exceeds this threshold, while the \cls{}--\traj{} gap ($<$10\pp{}) falls below it, consistent with our TOST equivalence finding. Holm-Bonferroni correction across the four primary comparisons ($k{=}4$) confirms both the \cls{}--\cwm{} gap (adjusted $p{=}0.012$) and function-level equivalence (adjusted $p{=}0.021$) survive; the repo-level \cwm{}--\traj{} comparison is directionally consistent but does not survive correction (adjusted $p{=}0.078$; Table~\ref{tab:holm}). The consistent direction across both model families and all tested configurations supports a formulation-level explanation, though definitive causal attribution requires future experiments addressing each confound individually.
560	
561	
562	\section{Extended Limitations}
563	\label{app:limitations}
564	
565	The same-size 4B comparison uses a single seed; \cls{} 4B seed 123 (val-best ckpt-800) achieves only 75.33\% test accuracy (+2.4\pp{} above majority baseline); val-best selection at an early checkpoint (step 800) amplifies the val-test distribution shift observed across all configurations. The \cwm{} 8B comparison uses 3 seeds per model. The validation and test sets have zero problem overlap but differ in mutation type composition (Table~\ref{tab:mutation_distribution}): \texttt{operator\_swap} shifts from 19.1\% (val) to 34.3\% (test), the largest single-type distribution mismatch (+15.2\pp{}). All repo-level results use val-selected checkpoints, and checkpoint selection variance could contribute to observed differences. Our training data is synthetically constructed from mutation operators rather than real developer patches. While mutation testing literature establishes that mutants are reasonable proxies for real faults in test effectiveness studies~\cite{andrews2005mutation,just2014mutants}, these findings concern mutation \emph{adequacy} (whether tests that kill mutants also detect real faults), not whether verifiers trained on mutants transfer to real patches. However, the coupling effect underlying these results supports \emph{relative ranking} validity: a domain shift from synthetic mutations to real bugs may affect absolute accuracy levels, but our core finding---that formulation choice matters at repo level but not function level---concerns relative performance ordering, which is expected to be preserved under distributional shifts that affect all formulations equally. The synthetic-to-real transfer gap for absolute accuracy remains untested. The \traj{} training configuration differs from \cls{}/\cwm{}: smaller training set (${\sim}$400 vs.\ ${\sim}$70K instances), different learning rate ($2{\times}10^{-4}$ vs.\ $5{\times}10^{-5}$), and variant-level evaluation ($n{=}48$ vs.\ per-test $n{=}9{,}784$). The function-level TOST equivalence ($p = 0.007$, $\pm$2\pp{}) is computed on 523 matched variant-level instances across 5 seeds; 2 of 5 seeds use NF4 quantization. Restricting to three bfloat16 seeds yields a comparable mean gap ($-$0.45\pp{}) but wider confidence interval (df${=}$2); the TOST $p$-value increases from 0.007 to 0.128, which reflects reduced statistical power rather than a shift in the point estimate. The NF4 seeds contribute precision (narrowing the CI) without shifting the mean, consistent with precision being comparable across both quantization levels at function level. Repo-level \cls{}--\traj{} comparison should be interpreted with caution due to configuration and granularity differences.
566	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fe4b017d-05e0-4e8e-8806-f29a21adddf7",
  "isSidechain": false,
  "promptId": "ec010885-b9c9-4574-b4a8-341b5a1f339a",
  "type": "user",
  "uuid": "86515315-9cf2-46cf-9a93-0bc33ea9fe6f",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/appendix.tex",
      "content": "\\appendix\n\n\\noindent\\textbf{Appendix overview.} A: Oracle resolve advantage. B: Ablation studies. C-F: Extended analysis (error complementarity, parseable accuracy, forced parsing, qualitative errors, failed interventions, mutation scaling, inference efficiency, re-repair, chain-of-thought). G: TOST sensitivity. G$'$: Bayesian ROPE. H: Effect sizes. I: Holm-Bonferroni. J: Mixed-effects regression. K: Parseable bias. L: CWM convergence. M: Few-shot. N: Threats. O: Downsample. P: Limitations.\n\n\\section{Oracle Accuracy-Utility Analysis}\n\\label{app:oracle}\n\nWe stratify SWE-bench Verified instances by F2P test count $T$, comparing per-test vs.\\ trajectory-level oracle resolve rates under i.i.d.\\ and block-correlated error models (ICC $= 0.191$, from function-level analysis; \\S\\ref{sec:equivalence}).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Oracle accuracy-utility frontier: per-test advantage stratified by F2P test count ($T$) on SWE-bench Verified (500 instances). Block-correlated model uses function-level ICC $= 0.191$ (from function-level analysis, \\S\\ref{sec:equivalence}). P2P regression rate: 1.04\\% mean, 0\\% median.}\n\\label{tab:oracle}\n\\resizebox{\\columnwidth}{!}{%\n\\setlength{\\tabcolsep}{3pt}\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{$T$} & \\textbf{Inst.\\%} & \\textbf{i.i.d.\\ (\\pp{})} & \\textbf{Block (\\pp{})} & \\textbf{Contrib.\\%} \\\\\n\\midrule\n$1$ & 68.7 & $-$0.04 & $-$0.09 & $\\approx$0 \\\\\n$2$ & 19.1 & 18.49 & 31.69 & 55.3 \\\\\n$3$--$5$ & 7.1 & 25.00 & 40.74 & $\\approx$26 \\\\\n$\\geq 6$ & 5.1 & 30.00 & 40.06 & $\\approx$19 \\\\\n\\midrule\n\\textbf{All} & 100.0 & --- & \\textbf{10.93} & 100.0 \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/paper/fig3_oracle_stratified.pdf}\n\\caption{Oracle per-test advantage by F2P test count $T$. Advantage is zero at $T{=}1$ (68.7\\%) and concentrates at $T{=}2$ (19.1\\%, contributing 55.3\\% of total advantage). Note: $y$-axis does not start at zero.}\n\\label{fig:oracle_stratified}\n\\end{figure}\n\nTable~\\ref{tab:oracle} and Figure~\\ref{fig:oracle_stratified} reveal a sharp concentration: at $T = 1$ (68.7\\% of instances), per-test and trajectory-level are informationally equivalent. The advantage materializes at $T = 2$ (19.1\\%), where block-correlated advantage reaches 31.69\\pp{} (55.3\\% of total). The overall block-correlated advantage is 10.93\\pp{}, driven by the $T \\geq 2$ minority. Block correlation amplifies relative to i.i.d.: at $T = 2$, 31.69\\pp{} vs.\\ 18.49\\pp{} (1.7$\\times$). P2P regression is negligible (1.04\\% mean, 0\\% median); the practical value concentrates in F2P discrimination.\n\n\\paragraph{Sensitivity to ICC estimate.}\nThe analysis above uses ICC $= 0.191$ from function-level analysis (\\S\\ref{sec:equivalence}), where mean cluster size $\\bar{k} \\approx 16.5$ yields DEFF $= 3.97$. At repository level, within-problem correlation is substantially stronger: ICC $= 0.3146$ with DEFF $= 114.4$ (\\S\\ref{sec:repo}), yielding an effective sample size of $n_{\\text{eff}} \\approx 9{,}784 / 114.4 \\approx 86$ independent observations~\\cite{moulton1990}---still sufficient for regression but limiting precision of variance component estimates. This is a consequence of the larger and more heterogeneous test suites in SWE-bench Verified problems. Under higher ICC, within-problem errors cluster more tightly and amplify the block-correlated per-test advantage at each $T$ stratum; the correction from i.i.d.\\ to block-correlated grows monotonically with ICC. The function-level ICC $= 0.191$ used in Table~\\ref{tab:oracle} thus provides a conservative lower bound on the per-test advantage. The repo-level correlation structure would yield an even larger gap between per-test and trajectory-level oracle resolve rates, which strengthens the case for per-test granularity at repository-level complexity.\n\n\\section{Ablation Studies}\n\\label{app:ablations}\n\n\\paragraph{LoRA rank sensitivity.}\nAll \\cwm{} experiments use LoRA rank $r{=}16$. To test whether this capacity constraint handicaps \\cwm{}, we train rank-32 variants (seed 42), doubling adapter parameters.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{LoRA rank ablation for \\cwm{} 4B (seed 42, 3 epochs, lr $= 2{\\times}10^{-4}$). Rank-16 seed variance: 0.53\\pp{} (seeds 42 vs.\\ 456).}\n\\label{tab:rank_ablation}\n\\setlength{\\tabcolsep}{4pt}\n\\begin{tabular}{lccccc}\n\\toprule\n\\textbf{Config} & \\textbf{$\\alpha/r$} & \\textbf{Acc (\\%)} & \\textbf{Fail \\fone{}} & \\textbf{Pass \\fone{}} & \\textbf{$\\Delta$} \\\\\n\\midrule\n$r{=}16$, $\\alpha{=}32$ & 2 & \\textbf{87.51} & --- & --- & --- \\\\\n$r{=}32$, $\\alpha{=}32$ & 1 & 87.00 & 87.1 & 86.9 & $-$0.51 \\\\\n$r{=}32$, $\\alpha{=}64$ & 2 & 87.04 & 87.27 & 86.79 & $-$0.47 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nBoth rank-32 variants fall within the 2-seed variance of the rank-16 baseline (0.53\\pp{} between seeds 42 and 456; Table~\\ref{tab:rank_ablation}). The $\\alpha{=}64$ variant (matching the baseline $\\alpha/r{=}2$ ratio) rules out the confound that the $\\alpha{=}32$ result might reflect reduced effective scaling rather than rank insensitivity. This is consistent with \\cwm{}'s function-level performance being bounded by output-format constraints rather than adapter capacity.\n\n\\paragraph{Majority voting.}\nMajority voting ($K{=}3$) decreases accuracy from 87.51\\% to 86.83\\% ($-$0.68\\pp{}): errors are systematic rather than stochastic, so sampling-based ensembles do not help.\n\n\\paragraph{Sequence-length ablation details.}\nBoth formulations are trained with \\texttt{max\\_seq\\_length}$=$2,048. At inference, \\cwm{} reserves \\texttt{max\\_new\\_tokens}$=$512, leaving ${\\sim}$1,536 effective input tokens; \\cls{} allocates nearly all context to input (5,120--8,192 tokens). A matched-context ablation (\\cls{} 8B at 2,048 tokens) achieves 83.04\\%, only 1.44\\pp{} below the 8,192-token evaluation (84.48\\%), though truncation introduces 136 unparseable outputs (1.39\\% of test samples). The matched-context gap (\\cls{}@2,048 vs.\\ \\cwm{}@2,048) is 25.00\\pp{} (98\\% of the full 25.59\\pp{} gap), confirming that input context disparity explains at most 3\\% of the difference.\n\n\\paragraph{Training data size control.}\n\\label{app:downsample}\nTo control for the training set size asymmetry between \\cls{} (${\\sim}$70K instances) and \\traj{} (386 variant-level instances, ${\\sim}$8K per-test equivalents, at repo level), we downsample \\cls{} training data to match \\traj{} in data volume. Downsampled \\cls{} (Qwen3-4B, seed 42) achieves 80.74\\% repo-level per-test accuracy, only 2.89\\pp{} below the full-data \\cls{} (83.63\\%) and still 7.82\\pp{} above \\traj{} (72.92\\%). The \\cls{} formulation advantage is not attributable to training data volume.\n\n\\paragraph{Few-shot prompting baselines.}\n\\label{app:few_shot}\nWe evaluate 3-shot in-context learning at repo level to test whether prompting strategy closes the gap to fine-tuned models. Table~\\ref{tab:few_shot} reports both per-test and variant-level accuracy.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Repo-level prompting baselines (per-test $n{=}9{,}784$; variant-level $n{=}48$). Majority baseline: 72.96\\% per-test, 54.17\\% variant-level.}\n\\label{tab:few_shot}\n\\setlength{\\tabcolsep}{4pt}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Model} & \\textbf{0-shot (per-test)} & \\textbf{3-shot (per-test)} & \\textbf{3-shot (variant)} \\\\\n\\midrule\nQwen3-8B & 49.90\\% & 71.61\\% & 45.83\\%\\textsuperscript{$\\ast$} \\\\\nDeepSeek-6.7B & 48.54\\% & 46.28\\% & 45.83\\%\\textsuperscript{$\\ast$} \\\\\n\\bottomrule\n\\end{tabular}}\n\n\\vspace{2pt}\n{\\footnotesize \\textsuperscript{$\\ast$}Both models achieve 45.83\\% by correctly classifying all 22 unresolved variants and zero resolved variants (22/48 = 45.83\\%), equivalent to an always-predict-unresolved baseline. The 100\\% overlap in variant-level predictions confirms complete degradation at task-relevant granularity.}\n\\end{table}\n\nBoth models converge to exactly 45.83\\% variant-level accuracy under 3-shot prompting, below majority baseline (54.17\\%). Variant-level analysis reveals this is not a coincidence: both models correctly classify all 22 unresolved variants and zero resolved variants, equivalent to an always-predict-unresolved baseline with 100\\% prediction overlap. Per-test accuracy diverges sharply (Qwen3-8B 71.61\\% vs.\\ DeepSeek 46.28\\%), but this divergence is entirely superficial: Qwen3-8B predicts pass on nearly all tests, inflating per-test accuracy on a pass-heavy dataset (72.96\\% pass rate) without genuine discriminative ability. Per-test metrics can thus severely misrepresent baseline capability; variant-level evaluation is necessary to detect complete degradation. Neither 0-shot nor few-shot prompting approaches fine-tuned performance (82--84\\% per-test); fine-tuning is a necessary condition for repo-level verification.\n\n\\section{Repo-Level Per-Mutation Breakdown}\n\\label{app:repo_mutation}\n\nTable~\\ref{tab:mutation_breakdown} compares per-mutation accuracy at repo level. \\cls{} produces 0\\% unparseable outputs; all values are direct classification accuracy. \\cwm{} overall accuracy includes default-pass assignment for unparseable outputs (see \\S\\ref{sec:repo}).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Per-mutation test accuracy (\\%) at repo level (SWE-bench Verified, $n{=}9{,}784$). \\cls{} 8B reports two seeds; $\\Delta$ is mean 4B$\\to$8B gain for \\cls{}. \\cwm{} 4B per-mutation overall accuracy omitted for non-gold mutations due to low parse rates (4.4--56.9\\%, Table~\\ref{tab:cwm_mutation_parse}); gold overall accuracy derived from parse rate 43.5\\% and parseable accuracy 23.5\\%.}\n\\label{tab:mutation_breakdown}\n\\resizebox{\\columnwidth}{!}{%\n\\setlength{\\tabcolsep}{3pt}\n\\begin{tabular}{lccccccc}\n\\toprule\n\\textbf{Mutation} & \\textbf{$n$} & \\textbf{CLS 4B} & \\textbf{CLS 8B s42} & \\textbf{CLS 8B s123} & \\textbf{CWM 4B} & \\textbf{CWM 8B} & \\textbf{$\\Delta$ CLS} \\\\\n\\midrule\ngold & 4,633 & 98.25 & 96.24 & 99.60 & 66.72 & 80.06 & $-$0.33 \\\\\noperator\\_swap & 3,357 & 78.91 & 81.38 & 82.60 & --- & 54.57 & +3.08 \\\\\noff\\_by\\_one & 183 & 58.47 & 86.89 & 79.20 & --- & 63.39 & \\textbf{+24.58} \\\\\nreturn\\_value & 562 & 67.97 & 75.44 & 66.40 & --- & 49.11 & +2.95 \\\\\nboundary\\_removal & 1,049 & 46.90 & 46.90 & 44.90 & --- & 42.23 & $-$1.00 \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\nTable~\\ref{tab:cwm_mutation_parse} shows that \\cwm{} generation quality degrades from 4B to 8B across all mutation types.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{\\cwm{} parse rates and parseable-only accuracy per mutation type (seed 42). Parse rate decreases uniformly from 4B to 8B; parseable-only accuracy is below random binary chance (50\\%) for gold at both scales.}\n\\label{tab:cwm_mutation_parse}\n\\setlength{\\tabcolsep}{4pt}\n\\begin{tabular}{lcccc}\n\\toprule\n& \\multicolumn{2}{c}{\\textbf{Parse Rate (\\%)}} & \\multicolumn{2}{c}{\\textbf{Parse Acc (\\%)}} \\\\\n\\cmidrule(lr){2-3} \\cmidrule(lr){4-5}\n\\textbf{Mutation} & \\textbf{4B} & \\textbf{8B} & \\textbf{4B} & \\textbf{8B} \\\\\n\\midrule\ngold & 43.5 & 23.9 & 23.5 & 16.5 \\\\\noperator\\_swap & 56.9 & 21.2 & 63.1 & 58.8 \\\\\noff\\_by\\_one & 4.4 & 27.3 & 0.0 & 38.0 \\\\\nreturn\\_value & 48.8 & 26.9 & 27.0 & 56.9 \\\\\nboundary\\_removal & 30.6 & 51.8 & 59.2 & 51.8 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nKey findings: (1)~Gold parse rate collapses from 43.5\\% to 23.9\\% at 8B; the simplest generation target (unmodified code, where all tests pass) degrades most, consistent with a fundamental generation bottleneck rather than task difficulty. (2)~Among parseable outputs, gold accuracy is 16.5--23.5\\%: the model generates outputs that fail exact-match even for correct code. (3)~\\texttt{off\\_by\\_one} is an anomaly: parse rate \\emph{increases} from 4.4\\% to 27.3\\%, but this is from an extremely low base ($n{=}8$ parseable at 4B), making both directions unreliable for this category.\n\n\\section{Variant-Level Accuracy}\n\\label{app:variant_level}\n\nTable~\\ref{tab:variant_level} reports variant-level accuracy ($n{=}48$) alongside per-test accuracy for all repo-level configurations. For \\cls{}, the aggregation penalty (per-test $\\to$ variant-level drop) ranges from 1\\pp{} to 19\\pp{} and is largest for models with low fail recall under the all-pass rule. \\cwm{} variant-level accuracy (48--52\\%) falls at or below the majority baseline, consistent with format collapse as the dominant failure mode.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Repo-level per-test vs.\\ variant-level accuracy ($n{=}48$ variants). Penalty = per-test $-$ variant-level. \\traj{} predicts variant outcomes directly (no aggregation). Variant-level majority baseline: 54.17\\% (26/48).}\n\\label{tab:variant_level}\n\\setlength{\\tabcolsep}{3pt}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llcccc}\n\\toprule\n\\textbf{Model} & \\textbf{Seed} & \\textbf{Per-test (\\%)} & \\textbf{Variant (\\%)} & \\textbf{Penalty (\\pp{})} & \\textbf{Fail Recall (\\%)} \\\\\n\\midrule\n\\multicolumn{6}{l}{\\emph{\\cls{}}} \\\\\nQwen3-8B & s42 & 84.48 & 72.92 & 11.56 & 56.76 \\\\\nQwen3-8B & s123 & 85.60 & 81.25 & 4.35 & 51.44 \\\\\nQwen3-4B & s42 & 83.63 & 64.58 & 19.05 & 48.72 \\\\\nDeepSeek-6.7B & s42 (e1) & 82.61 & 81.25 & 1.36 & 51.02 \\\\\nDeepSeek-6.7B & s42 (e3) & 82.51 & 79.17 & 3.34 & 38.47 \\\\\nDeepSeek-6.7B & s123 & 74.93 & 56.25 & 18.68 & ${\\sim}$13.72 \\\\\n\\midrule\n\\multicolumn{6}{l}{\\emph{\\cwm{}}} \\\\\nQwen3-8B & s42 & 65.17 & 52.08 & 13.09 & --- \\\\\nDeepSeek-6.7B$^\\dagger$ & s123 & --- & 47.92 & --- & --- \\\\\n\\midrule\n\\multicolumn{6}{l}{\\emph{\\traj{}}} \\\\\nQwen3-4B & s42 & --- & 72.92 & --- & --- \\\\\nQwen3-8B & s42 & --- & 70.83 & --- & --- \\\\\nDeepSeek-6.7B & 3-seed & --- & 77.08 $\\pm$ 3.61 & --- & --- \\\\\n\\midrule\nMajority & --- & 72.96 & 54.17 & --- & --- \\\\\n\\bottomrule\n\\end{tabular}}\n\\vspace{2pt}\n\n{\\footnotesize $^\\dagger$Evaluated on ${\\sim}$75\\% of test instances (7210--7668 of 9784). DeepSeek \\traj{} Table~\\ref{tab:repo_level} reports 3 seeds (42/123/456) for alignment with \\cls{}/\\cwm{} seed coverage; three supplementary seeds (0/789/999) yield 75.0\\%, 66.7\\%, 79.2\\% respectively (6-seed mean 75.35 $\\pm$ 5.00\\%), consistent in direction.}\n\\end{table}\n\n\\section{Training Hyperparameters}\n\\label{app:hyperparams}\n\nTable~\\ref{tab:hyperparams} lists all hyperparameters used for fine-tuning. Both \\cls{} and \\cwm{} share the same LoRA configuration, optimizer, and training schedule; the only differences are per-device batch size, gradient accumulation steps (adjusted to maintain identical effective batch size of 32 across model sizes), and learning rate (DeepSeek-Coder uses $2{\\times}10^{-4}$ vs.\\ $5{\\times}10^{-5}$ for Qwen3, selected via grid search over $\\{5{\\times}10^{-5}, 1{\\times}10^{-4}, 2{\\times}10^{-4}\\}$ on held-out validation loss).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Training hyperparameters for \\cls{}/\\cwm{} configurations. \\traj{} models use lr $= 2{\\times}10^{-4}$ due to the smaller training set (${\\sim}$8K function-level instances vs.\\ ${\\sim}$70K for \\cls{}/\\cwm{}); other hyperparameters are shared.}\n\\label{tab:hyperparams}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{ll}\n\\toprule\n\\multicolumn{2}{l}{\\textbf{Shared across all configurations}} \\\\\n\\midrule\nLoRA rank / alpha / dropout & 16 / 32 / 0.05 \\\\\nLoRA targets & \\texttt{q/k/v/o\\_proj} \\\\\nOptimizer & AdamW ($\\beta_1{=}0.9$, $\\beta_2{=}0.999$) \\\\\nLR scheduler & Linear \\\\\nEffective batch size & 32 \\\\\nMax sequence length & 2,048 \\\\\nEpochs & 3 \\\\\nPrecision & bf16 \\\\\nGradient checkpointing & \\checkmark \\\\\nSeeds (function) & \\{42, 123, 456, 789, 0\\}\\textsuperscript{$b$} \\\\\nSeeds (repo) & \\{42, 123, 456\\}\\textsuperscript{$c$} \\\\\n\\bottomrule\n\\end{tabular}}\n\n\\vspace{6pt}\n\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lccc}\n\\toprule\n\\multicolumn{4}{l}{\\textbf{Model-family--specific parameters}} \\\\\n\\midrule\n& \\textbf{Qwen3-4B} & \\textbf{Qwen3-8B} & \\textbf{DS-6.7B} \\\\\n\\midrule\nLearning rate & 5e-5 & 5e-5 & 2e-4 \\\\\nWeight decay & 0.01 & 0.01 & 0.0 \\\\\nWarmup ratio & 0.05 & 0.05 & 0.1 \\\\\nBatch / grad.\\ accum.\\ (\\cls{}) & 2 / 16 & 1 / 32 & 2 / 16 \\\\\nBatch / grad.\\ accum.\\ (\\cwm{}) & 1 / 32 & 1 / 32 & 1 / 32 \\\\\nTraining samples & 70,748 & 70,748 & 67,343--70,748\\textsuperscript{$a$} \\\\\n\\bottomrule\n\\end{tabular}}\n\n\\vspace{2pt}\n{\\footnotesize $^a$DeepSeek \\cls{} canonical run (s42) uses drop preprocessing, which excludes 3,405 sequences exceeding max length (67,343 of 70,748). The s123 run uses truncate preprocessing (70,748 samples) but produces NaN validation loss. See \\S\\ref{sec:setup}. $^b$Seeds 789 and 0 use NF4 quantization; others use bf16. $^c$Repo-level seed coverage varies by configuration; see Table~\\ref{tab:repo_level} caption for per-model counts.}\n\\end{table}\n\n\\paragraph{Data processing.} DeepSeek CWM seeds use \\texttt{train\\_unified.py}, which drops samples exceeding \\texttt{max\\_seq\\_length} (3{,}405 of 70{,}748 samples, 4.8\\%). Qwen CWM seeds use \\texttt{train\\_repo\\_cwm.py}, which truncates and retains all samples. This difference affects total training steps (${\\sim}$12{,}627 vs.\\ ${\\sim}$13{,}266 for DeepSeek, ${\\sim}$6{,}633 for Qwen) but not the training data distribution, as dropped samples are uniformly distributed across labels.\n\n\\paragraph{Prompt templates.} Prompt templates for all formulations (\\cls{}, \\cwm{}, \\traj{}) are provided in the code repository. \\cls{} uses a binary classification template (``Does this test pass or fail?''); \\cwm{} uses an execution simulation template (``What is the output of this test?''); \\traj{} uses a variant-level verdict template (``Is this patch resolved or unresolved?'').\n\n\\paragraph{Mutation operators.} We use five mutation types: (1)~\\emph{gold}: unmodified code (all tests pass); (2)~\\emph{operator\\_swap}: replaces comparison or arithmetic operators (e.g., \\texttt{<} $\\to$ \\texttt{<=}); (3)~\\emph{off\\_by\\_one}: shifts loop bounds or array indices by $\\pm$1; (4)~\\emph{return\\_value}: modifies return statements (e.g., negating a boolean, changing a constant); (5)~\\emph{boundary\\_removal}: removes conditional guards or boundary checks. Mutation operators were applied using AST-level transformation; variants that did not alter any test outcome were discarded.\n\n\\paragraph{Compute budget.}\nAll experiments were conducted on NVIDIA RTX 5090 GPUs. Training time is approximately 1.5 hours per run for 4B models and 2 hours for 8B models. Total compute budget: ${\\sim}$370 GPU-hours across 223 completed runs (135 successful, 88 failed/killed; ${\\sim}$46 unique configurations including seeds, formulations, model sizes, and ablations).\n\n\\section{Prompt Templates}\n\\label{app:prompts}\n\nWe show representative prompt examples for each formulation. All examples use the same input instance for comparability.\n\n\\paragraph{CLS (per-test classification).}\n\\begin{verbatim}\nSystem: You are a code verifier. Given a\ncode patch and a test name, predict whether\nthe test will pass or fail when run against\nthe patched code.\n\nUser:\n## Patch (git diff)\n&lt;patch content>\n[... truncated ...]\n\n## Test\ntest_boundary_check\n\nWill this test pass or fail?\n\nTarget: pass\n\\end{verbatim}\n\n\\paragraph{CWM (execution simulation).}\n\\begin{verbatim}\nSystem: You are a code execution simulator.\nGiven a code snippet and a test case,\npredict the execution result.\n\nUser:\n## Code\n&lt;code content>\n[... truncated ...]\n\n## Test\ntest_boundary_check\n\nWhat is the execution result?\n\nTarget: PASS: test completed successfully\n\\end{verbatim}\n\n\\paragraph{TRAJ (trajectory scoring).}\n\\begin{verbatim}\nSystem: You are a code repair verifier.\nGiven the code patch and test summary,\npredict whether all tests pass (resolved)\nor any test fails (unresolved).\n\nUser:\n[Code]\n&lt;patch content>\n[... truncated ...]\n\n[Test Summary]\n&lt;all test names and descriptions>\n\nTarget: resolved\n\\end{verbatim}\n\n\\cls{} and \\cwm{} share the same input format (one code--test pair per instance); \\cls{} produces a single token (\\texttt{pass}/\\texttt{fail}), while \\cwm{} generates a variable-length execution trace. \\traj{} receives all tests concatenated and produces a single token (\\texttt{resolved}/\\texttt{unresolved}).\n\n\n\\section{Val-Test Mutation Type Distribution}\n\\label{app:mutation_distribution}\n\nTable~\\ref{tab:mutation_distribution} reports the mutation type composition of the repo-level validation and test sets. The most notable shift is \\texttt{operator\\_swap}, which nearly doubles from val (19.1\\%) to test (34.3\\%), while \\texttt{off\\_by\\_one} shrinks from 10.0\\% to 1.9\\%.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Repo-level mutation type distribution: validation vs.\\ test set, with per-type \\cls{} accuracy at two model sizes (seed 42). Shift = test\\% $-$ val\\%.}\n\\label{tab:mutation_distribution}\n\\setlength{\\tabcolsep}{3pt}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lccccc}\n\\toprule\n\\textbf{Mutation Type} & \\textbf{Val (\\%)} & \\textbf{Test (\\%)} & \\textbf{Shift} & \\textbf{\\cls{} 4B} & \\textbf{\\cls{} 8B} \\\\\n\\midrule\ngold & 45.2 & 47.4 & +2.2 & 98.3 & 96.2 \\\\\noperator\\_swap & 19.1 & 34.3 & +15.2 & 78.9 & 81.4 \\\\\nboundary\\_removal & 15.0 & 10.7 & $-$4.3 & 46.9 & 46.9 \\\\\nreturn\\_value & 10.7 & 5.7 & $-$5.0 & 68.0 & 75.4 \\\\\noff\\_by\\_one & 10.0 & 1.9 & $-$8.1 & 58.5 & 86.9 \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\nThe \\texttt{operator\\_swap} shift is the primary source of val-test distribution mismatch. Since \\cls{} achieves moderate accuracy on this type (78.9--81.4\\%), the over-representation in the test set does not systematically bias overall accuracy estimates in either direction. Two boundary observations are notable: (1)~\\texttt{boundary\\_removal} represents a scale-invariant difficulty ceiling at ${\\sim}$47\\% across both model sizes: this mutation type resists capacity scaling; (2)~\\texttt{off\\_by\\_one} shows the largest scaling gain (+28.4\\pp{}, 58.5\\%$\\to$86.9\\%) but its small test share (1.9\\%) limits its contribution to overall accuracy differences across scales.\n\n\\section{Qualitative Error Analysis}\n\\label{app:qualitative}\n\nTo complement the quantitative divergence reported in \\S\\ref{sec:repo}, we examine representative errors from each formulation at repository level.\n\n\\paragraph{\\cwm{} failure modes.}\nTwo patterns account for the majority of unparseable \\cwm{} outputs on Qwen3. (1)~\\emph{Task misunderstanding}: the model generates a complete simulated test runner log (test names, timing, summary lines) rather than a pass/fail verdict. For instance, on \\texttt{django\\_\\_django-14315}, the model outputs a fabricated 1,248-token Django test execution trace with hallucinated test names that do not exist in the target file. The model confuses ``predict test outcome'' with ``simulate test execution environment.'' (2)~\\emph{Autoregressive degeneration}: the model enters a repetitive loop (e.g., repeating \\texttt{from \\_pytest.config import \\_parse\\_pytest\\_args} until truncation at 4,542 tokens). Both patterns produce zero usable signal and default to the majority-class label. This explains why unparseable predictions carry higher accuracy than parseable ones (\\S\\ref{sec:repo}).\n\n\\paragraph{\\cls{} failure modes.}\n\\cls{} errors concentrate in two categories requiring multi-step reasoning. False positives arise from \\emph{cross-concern value propagation}: a boundary removal mutation in \\texttt{pytest} converts a guarded attribute access (\\texttt{if xfailed and not xfailed.run}) to \\texttt{if True:}, causing a NoneType error on tests exercising unrelated skip marks. The model fails to trace the None path through the pytest hook lifecycle. False negatives arise from \\emph{mathematical equivalence}: on \\texttt{HumanEval/130} (Tribonacci variant), the model predicts failure for correct code because verifying the self-referential recurrence requires algebraic substitution rather than syntactic inspection. This single problem accounts for 17\\% of all function-level false negatives.\n\n\\paragraph{Complementarity.}\nThese failure patterns operate at different levels: \\cwm{} fails at the format level (producing no usable signal), while \\cls{} fails at the reasoning level (producing a confident but incorrect binary verdict). Both formulations are FP-dominant (over-predict failure), but \\cwm{}'s higher FP rate (70.3\\% vs.\\ 56.5\\%) means it over-predicts failure on instances \\cls{} correctly classifies, producing partial complementarity (oracle combination: 90.63\\%; \\S\\ref{app:extended_analysis}, paragraph a).\n\n\\section{Extended Analysis}\n\\label{app:extended_analysis}\n\n\\paragraph{Function-level CWM metric robustness.}\nAt function level, \\cwm{} outputs are short status strings (mean ${\\sim}$5--15 tokens). The unparseable rate is only 1.39\\%, and default-to-pass bias is $<$1\\pp{}---well below the SESOI threshold. Exact string matching is appropriate for these short, structured outputs; semantic-but-format-different matches are rare given the constrained output space.\n\n\\paragraph{(a) Error complementarity.}\n\\cls{} and \\cwm{} are both FP-dominant at function level but at different rates, producing partial complementarity. Among \\cls{} errors (seed 42), 56.5\\% are false positives (PASS $\\to$ FAIL); among \\cwm{} errors, 70.3\\% are false positives. Both formulations over-predict failure, but \\cwm{}'s stronger FP bias means it incorrectly rejects passing tests that \\cls{} correctly accepts. An oracle combination achieves 90.63\\% accuracy (1713/1890 correct, 177 both-wrong; +2.80\\pp{} over the best single formulation, \\cls{} 87.83\\%; single-seed estimate, seed 42). The complementarity arises from different \\emph{degrees} of fail-bias rather than opposite error directions: \\cwm{}'s generation bottleneck produces aggressive failure predictions, while \\cls{}'s single-token output is more calibrated. Ensemble approaches exploiting this degree difference are a natural direction.\n\n\\paragraph{(b) CWM error mode breakdown.}\nAmong unparseable \\cwm{} outputs (Qwen3, repo-level), 76.9\\% contain no execution keywords; 22.9\\% contain ambiguous co-occurring pass/fail keywords. Format compliance varies sharply across repositories (scikit-learn: near-zero unparseable; sphinx: 100\\%); repository-specific code patterns interact with the model's generation capabilities in complex ways. This per-repository variation is consistent with a model/tokenizer-specific failure rather than a formulation-level one.\n\n\\paragraph{(c) Relaxed matching does not rescue \\cwm{}.}\nRelaxed matching (tolerating format deviations, L0--L4) \\emph{decreases} \\cwm{} accuracy: 58.04\\%$\\to$56.98\\% (seed 42) and 59.09\\%$\\to$55.91\\% (seed 123). Unparseable predictions default to the majority class (pass, 72.96\\%), which outperforms the model's own parseable predictions (38--43\\%). The divergence widens from 26\\pp{} to 27\\pp{} under relaxed matching. This rules out the hypothesis that parsing strictness inflates the observed gap. Constrained decoding~\\cite{willard2023outlines} could enforce format compliance but would not address the semantic accuracy deficit among parseable outputs. An accidental training artifact provides further evidence: a \\cwm{} model inadvertently trained on function-level (\\cls{}-format) data achieved 86.05\\% accuracy with 0\\% unparseable outputs at repo level---recovering \\cls{}-level performance. This confirms that the repo-level \\cwm{} degradation stems entirely from trace generation complexity, not from the underlying verification task.\n\n\\paragraph{(d) Variance compression.}\n\\cwm{}'s 5-seed standard deviation (0.37\\pp{}) is lower than \\cls{} (0.78\\pp{}) and \\traj{} (0.97\\pp{}) at function level. If \\cwm{} performance is capped by output-format constraints at a given complexity level, seed-to-seed variability is compressed relative to formulations whose performance depends more on learned representations.\n\n\\paragraph{(e) Per-test precision and recall.}\n\\cls{} achieves fail \\fone{} 87.59\\% (precision 86.20\\%, recall 89.04\\%) at seed 42.% derived from overlap analysis (error_overlap_matched_seed.json); FP=130, FN=100, TP=848, TN=812\nMulti-F2P instances (6--10 tests) reach 96.3\\% accuracy, consistent with the oracle finding that per-test granularity is most valuable for complex instances.\n\n\\paragraph{(f) Block correlation.}\nWithin-problem errors are correlated (ICC $= 0.191$, DEFF $= 3.97$, 2.81$\\times$ more all-correct problems than i.i.d.\\ expectation). All statistical tests use clustered bootstrap accordingly.\n\n\\paragraph{(g) Failed interventions.}\nWe systematically tested four interventions targeting different hypothesized causes of \\cwm{} repo-level degradation; all failed:\n\n\\begin{itemize}[leftmargin=*,itemsep=1pt,topsep=2pt]\n\\item \\textbf{Capacity (rank 32, $\\alpha{=}64$):} $-$0.47\\pp{}, within seed variance (\\S\\ref{app:ablations}).\n\\item \\textbf{Majority voting ($K{=}3$):} $-$0.68\\pp{}; 93.3\\% unanimous, net flips negative (\\S\\ref{app:ablations}).\n\\item \\textbf{Relaxed matching (L0--L4):} $-$1.06\\pp{}; default-pass outperforms parseable predictions (paragraph~(c) above).\n\\item \\textbf{Model scaling (4B$\\to$8B):} parseable accuracy decreases (42.88\\%$\\to$38.52\\%) while unparseable rate rises (53.7\\%$\\to$73.8\\%); gain is a default-assignment artifact (\\S\\ref{sec:repo}).\n\\end{itemize}\n\n\\noindent Each intervention targets a distinct alternative explanation (insufficient capacity, random noise, parsing strictness, model scale); the uniform failure across all four confirms the bottleneck is formulation-level---output space complexity at repo level exceeds what ${\\leq}$8B generation models can handle, independent of these surface-level factors.\n\n\\paragraph{(h) Per-mutation scaling patterns.}\nScaling benefits are highly non-uniform across mutation types (Table~\\ref{tab:mutation_breakdown}). \\texttt{off\\_by\\_one} shows the largest \\cls{} scaling gain: 58.5\\% (4B) to 86.9\\% (8B, $+$28.4\\pp{}). In contrast, \\texttt{boundary\\_removal} is scale-invariant at ${\\sim}$47\\% across both sizes, which marks an intrinsic difficulty ceiling. For \\cwm{}, gold mutation parse rate collapses from 43.5\\% (4B) to 23.9\\% (8B) despite being the simplest target: generation capability degrades even for trivially correct code at larger scale within Qwen3. The val-test mutation type distribution differs notably (\\texttt{operator\\_swap} shifts from 19.1\\% to 34.3\\%; Table~\\ref{tab:mutation_distribution}), but this shift does not systematically bias overall accuracy because \\cls{} performance on \\texttt{operator\\_swap} (78.9--81.4\\%) is close to the overall mean.\n\n\\paragraph{(i) Inference efficiency.}\n\\cls{} achieves 217$\\times$ higher throughput than \\cwm{} at repo level (853 vs.\\ 3.9 inferences/min; Qwen3-4B, RTX 5090, 100 samples, avg ${\\sim}$1,040 input tokens). The speedup derives directly from the formulation: classification requires a single output token, whereas \\cwm{} generates an average of 477 tokens per inference. Median latency is 48ms (\\cls{}) vs.\\ 16.3s (\\cwm{}). At the observed unparseable rate of 73.8\\% (8B), the majority of \\cwm{}'s generation budget produces tokens that cannot yield a valid verdict. This \\cls{}--\\cwm{} efficiency gap is an inherent property of the formulation difference (1 vs.\\ $O(L)$ output tokens) and should generalize across models, unlike the accuracy divergence which may be model-contingent.\n\nThe \\cls{}--\\traj{} efficiency comparison is more nuanced, because \\cls{} makes one call per test while \\traj{} makes one call per instance. Per-call, \\cls{} is 20--138$\\times$ faster (depending on input length: 47ms for short contexts vs.\\ 2,632ms for \\traj{}). However, the per-instance effective speedup depends on test count $|T|$: at function level ($|T| \\approx 2.3$), \\cls{} is ${\\sim}$24$\\times$ faster (108ms vs.\\ 2,632ms per instance); at repo level ($|T| \\approx 12.3$, ${\\sim}$70ms/call with longer inputs), \\cls{} is ${\\sim}$3$\\times$ faster (861ms vs.\\ 2,631ms). A crossover exists at $|T| \\approx 50$ tests, beyond which \\traj{}'s single-call amortization dominates. This boundary condition is informative for deployment: \\cls{} is strongly preferred for function-level and moderate repo-level test suites, while extremely large test suites ($>$50 tests per instance) favor trajectory-level efficiency despite its coarser diagnostic signal.\n\n\\paragraph{(j) Re-repair pilot.}\nWe tested whether per-test diagnostic feedback improves downstream repair. A Qwen3-8B repair agent received either per-test diagnostic signals (which specific tests failed and why) or binary accept/reject feedback, evaluated on 44 SWE-bench Verified instances. The diagnostic condition achieved accuracy no higher than the binary baseline ($A_1 = 52.3\\%$, $p = 0.42$, effect size $\\approx 0$). Per-test diagnostic information does not automatically translate to repair improvements at this scale. The negative result may reflect insufficient agent capability to exploit fine-grained feedback, insufficient sample size (at $n = 44$, statistical power is ${\\sim}$0.3 for a medium effect size), or a genuine limitation of the diagnostic-to-repair translation.\n\n\\paragraph{(k) Relationship to chain-of-thought verification.}\n\\cwm{} is structurally a chain-of-thought verifier: the model generates an execution trace token by token and derives its PASS/FAIL verdict from the final trace state. If intermediate reasoning improved verification, \\cwm{} should outperform the reasoning-free \\cls{} baseline. At function level, no such advantage materialises: \\cwm{} and \\cls{} are statistically equivalent (TOST $p{=}0.007$, $\\pm$2\\pp{} margin; \\S\\ref{sec:equivalence}), indicating that the additional trace generation provides no accuracy benefit over direct binary classification. At repo level, the chain-of-thought mechanism actively \\emph{hurts}: trace generation triggers format collapse (53--74\\% unparseable), and even parseable traces yield accuracy below the majority baseline (38--43\\% vs.\\ 72.96\\%; paragraph~(c)). Four targeted interventions fail to rescue the generation pathway (paragraph~(g)). Within the ${\\leq}$8B LoRA regime, chain-of-thought--style verification does not outperform direct classification for execution prediction. Whether execution-trace pretraining at larger scale~\\cite{meta2025cwm} changes this conclusion remains the primary open question (\\S\\ref{sec:threats}).\n\n\\section{TOST Margin Sensitivity}\n\\label{app:tost_sensitivity}\n\nTable~\\ref{tab:tost_sensitivity} reports the TOST equivalence $p$-value as a function of the equivalence margin, computed on the 5-seed variant-level \\cls{}--\\cwm{} comparison (gap $= 1.24$\\pp{}, 523 variants, 114 clusters, clustered bootstrap).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{TOST margin sensitivity for \\cls{}--\\cwm{} variant-level equivalence (5 seeds, 523 variants, 114 clusters). The smallest margin achieving equivalence at $\\alpha = 0.05$ is $\\pm$1.52\\pp{}.}\n\\label{tab:tost_sensitivity}\n\\setlength{\\tabcolsep}{4pt}\n\\begin{tabular}{ccc}\n\\toprule\n\\textbf{Margin ($\\pm$\\pp{})} & \\textbf{$p$-value} & \\textbf{Equivalent ($\\alpha{=}0.05$)?} \\\\\n\\midrule\n1.0 & $\\gg$0.05 & No \\\\\n1.5 & 0.054 & No (borderline) \\\\\n\\textbf{1.52} & ${\\sim}$\\textbf{0.05} & \\textbf{Smallest margin} \\\\\n1.71 & 0.027 & Yes \\\\\n2.0 & 0.007 & Yes \\\\\n3.0 & $4.6{\\times}10^{-5}$ & Yes \\\\\n5.0 & $\\ll$0.001 & Yes \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe minimum equivalence margin is $\\pm$1.52\\pp{}, 0.48\\pp{} below our pre-specified $\\pm$2\\pp{} threshold. The $\\pm$2\\pp{} threshold was set based on deployment relevance rather than observed data: at function-level accuracy (85--88\\%), a 2\\pp{} per-test difference corresponds to ${\\sim}$38 additional errors across 1,890 tests (${\\sim}$2--3 problems out of 114), comparable in magnitude to between-seed standard deviation (0.37--0.97\\pp{}) and checkpoint selection noise ($<$1\\pp{}). Differences within this range do not reliably distinguish formulations from training noise in pipeline selection decisions. For \\cls{}--\\traj{}, the TOST at $\\pm$2\\pp{} yields $p{=}0.025$, nominally significant but not surviving Holm-Bonferroni correction at $k{=}5$ (Table~\\ref{tab:holm}).\n\n\\paragraph{Bayesian ROPE analysis.}\n\\label{app:bayesian_rope}\nTo complement the frequentist TOST, we conduct a Bayesian equivalence analysis using a paired $t$-test with Jeffreys prior~\\cite{kruschke2013bayesian,kruschke2018rejecting}. The marginal posterior for the mean accuracy difference follows a $t$-distribution with $n{-}1$ degrees of freedom. For \\cls{}--\\cwm{}, the posterior probability within the $\\pm$2\\pp{} ROPE is $P(\\text{ROPE}) = 0.975$, and the 95\\% highest density interval (HDI $= [{+}0.10, {+}2.00]$\\,pp) falls entirely inside the ROPE, confirming equivalence under both continuous and HDI-based decision criteria. For \\cls{}--\\traj{} at per-test level, $P(\\text{ROPE}) = 0.542$ (inconclusive; 95\\% HDI $= [{+}0.35, {+}3.52]$\\,pp extends beyond the ROPE), consistent with the TOST non-confirmation after Holm correction ($p_{\\text{adj}} = 0.075$). At variant level, \\cls{}--\\traj{} equivalence is supported by the Bayesian criterion ($P(\\text{ROPE}) = 0.970$, HDI $= [{-}2.00, {+}1.03]$\\,pp), but the frequentist TOST does not confirm equivalence after Holm-Bonferroni correction ($p_{\\text{adj}} = 0.075$; Table~\\ref{tab:holm}). This discrepancy reflects differing treatments of multiplicity: Bayesian ROPE evaluates each comparison independently, while Holm correction penalizes across all $k{=}5$ primary tests. For \\cls{}--\\cwm{}, both frameworks agree (TOST $p_{\\text{adj}}{=}0.028$, $P(\\text{ROPE}){=}0.975$); for \\cls{}--\\traj{} per-test, both are inconclusive. We conservatively follow the Holm-corrected TOST in the main text and report \\cls{}--\\traj{} equivalence as not confirmed.\n\n\n\\section{Variant-Level Effect Sizes}\n\\label{app:power}\n\nTable~\\ref{tab:variant_power} reports variant-level bootstrap confidence intervals for the repo-level formulation comparisons ($n{=}48$ variants). Following Hoenig and Heisey~\\cite{hoenig2001}, we report minimum detectable effect (MDE) rather than post-hoc observed power.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Variant-level bootstrap analysis ($n{=}48$). \\cls{}--\\cwm{} uses paired bootstrap (same variants, same seed); \\cls{}--\\traj{} uses unpaired bootstrap (per-variant \\traj{} predictions not archived for pairing). MDE at $n{=}48$: ${\\sim}$25\\pp{}.}\n\\label{tab:variant_power}\n\\setlength{\\tabcolsep}{3pt}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llccc}\n\\toprule\n\\textbf{Comparison} & \\textbf{Config} & \\textbf{$\\Delta$ (\\pp{})} & \\textbf{95\\% CI} & \\textbf{$p$} \\\\\n\\midrule\n\\multicolumn{5}{l}{\\emph{\\cls{} vs.\\ \\cwm{} (paired)}} \\\\\n& Qwen3-8B & +29.17 & [10.42, 47.92] & 0.003 \\\\\n& DeepSeek-6.7B & +35.42 & [18.75, 50.05] & ${<}$0.001 \\\\\n\\midrule\n\\multicolumn{5}{l}{\\emph{\\cls{} vs.\\ \\traj{} (unpaired)}} \\\\\n& Qwen3-4B & $-$4.17 & wide & 0.740 \\\\\n& Qwen3-8B & +8.33 & wide & 0.385 \\\\\n& DeepSeek-6.7B & 0.00 & wide & 1.000 \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\nAt $n{=}48$, the MDE is ${\\sim}$25\\pp{}. The \\cls{}--\\cwm{} gap (29--35\\pp{}) exceeds this threshold, confirming that $n{=}48$ is sufficient to detect the observed divergence. The \\cls{}--\\traj{} gaps ($<$10\\pp{}) fall well below the MDE: any true difference is too small to detect at this sample size, consistent with the function-level TOST equivalence (\\S\\ref{sec:equivalence}).\n\nThe \\cls{}--\\traj{} unpaired bootstrap produces wider confidence intervals than paired analysis would; \\traj{} per-variant predictions were not archived in a format that permits pairing. The \\cls{}--\\cwm{} paired comparison uses \\cls{} s123 vs.\\ \\cwm{} s42 (different seeds), but the CI lower bound of 10.42\\pp{} far exceeds the seed noise observed in function-level experiments ($<$2\\pp{}).\n\n\n\\section{Multiple Comparison Correction}\n\\label{app:holm}\n\nTable~\\ref{tab:holm} applies Holm-Bonferroni correction~\\cite{holm1979} to the five primary statistical comparisons across this study ($k{=}5$, family-wise $\\alpha{=}0.05$).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Holm-Bonferroni correction for primary comparisons ($k{=}5$). Comparisons ranked by raw $p$-value; each tested against $\\alpha / (k - \\text{rank} + 1)$.}\n\\label{tab:holm}\n\\setlength{\\tabcolsep}{3pt}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{clcccc}\n\\toprule\n\\textbf{Rank} & \\textbf{Comparison} & \\textbf{Raw $p$} & \\textbf{Factor} & \\textbf{Adj $p$} & \\textbf{Sig.?} \\\\\n\\midrule\n1 & Repo: \\cls{} vs \\cwm{} & 0.003 & $\\times$5 & 0.015 & \\checkmark \\\\\n2 & Func: \\cls{} vs \\cwm{} (TOST $\\pm$2\\pp{}) & 0.007 & $\\times$4 & 0.028 & \\checkmark \\\\\n3 & Func: \\cls{} vs \\traj{} (TOST $\\pm$2\\pp{}) & 0.025 & $\\times$3 & 0.075 & --- \\\\\n4 & Repo: \\cwm{} vs \\traj{} & 0.039 & $\\times$2 & 0.078 & --- \\\\\n5 & Repo: \\cls{} vs \\traj{} & 0.385 & $\\times$1 & 0.385 & --- \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\nThe two core claims survive correction: the repo-level \\cls{}--\\cwm{} divergence (adjusted $p{=}0.015$) and function-level \\cls{}--\\cwm{} equivalence (adjusted $p{=}0.028$). The function-level \\cls{}--\\traj{} equivalence does not survive correction (adjusted $p{=}0.075$); we interpret this as directionally consistent but not confirmatory.\n\n\\section{Mixed-Effects Regression}\n\\label{app:interaction}\n\nWe fit mixed-effects linear probability models (LPM) with heteroskedasticity-robust standard errors (HC1) to test the formulation$\\times$complexity interaction formally~\\cite{moulton1990}. We choose LPM because coefficients are directly interpretable as probability differences (percentage points), consistent with the reporting units in the main text; at these sample sizes ($n{\\approx}56$K cross-complexity, repo-level pooled cross-model) and base rate range (0.6--0.9), LPM and logistic regression yield concordant conclusions for all primary effects~\\cite{angrist2009mostly} (confirmed below).\n\n\\paragraph{Cross-complexity model (DeepSeek-Coder).} \\texttt{correct $\\sim$ formulation $\\times$ complexity + (1|problem\\_id)}, $n{=}56{,}480$ observations (\\cls{} + \\cwm{} $\\times$ function + repo), 139 problem clusters. The \\cwm{} main effect at function level is non-significant ($\\hat{\\beta}{=}-0.002$, $z{=}-0.25$, $p{=}0.805$); the \\cwm{}$\\times$repo interaction is highly significant ($\\hat{\\beta}{=}-0.219$, $z{=}-23.7$, $p{<}0.001$). \\cwm{} and \\cls{} are statistically indistinguishable at function level ($\\Delta{=}-0.2$\\pp{}, $p{=}0.805$) but diverge by 22\\pp{} at repo level, confirming the complexity-dependent divergence is not an artifact of aggregation.\n\n\\paragraph{Repo-level cross-model model.} \\texttt{correct $\\sim$ formulation $\\times$ model + (1|problem\\_id)}, both model families, repo level only. \\cwm{} deficit: $\\hat{\\beta}{=}-0.22$ ($-$22\\pp{}, $z{=}-64.4$, $p{<}0.001$). Model effect: +1.1\\pp{} for Qwen3 ($z{=}3.1$, $p{=}0.002$ in LPM; not significant under GEE, $p{=}0.449$). Formulation$\\times$model interaction: +1.6\\pp{} less \\cwm{} degradation on Qwen3 ($z{=}2.8$, $p{=}0.006$ in LPM; not significant under GEE, $p{=}0.860$). Formulation dominates the predictable variance; model identity is directionally positive but specification-dependent. The 25-cluster random intercept structure limits effective degrees of freedom for the random effects; inferences on fixed effects (formulation, complexity) are robust as they pool across the full observation count.\n\n\\paragraph{Logistic regression robustness check.} To verify that LPM conclusions are not artifacts of the linear link function, we fit GEE logistic regression (binomial family, exchangeable working correlation, robust sandwich standard errors) to the same data. For the cross-complexity model, the \\cwm{} main effect at function level has OR$=$0.98 (95\\% CI [0.86, 1.12], $p{=}0.771$) and the \\cwm{}$\\times$repo interaction has OR$=$0.31 ([0.15, 0.65], $p{=}0.002$). Average marginal effects are $-$0.2\\pp{} (function) and $-$21.6\\pp{} (repo), matching LPM coefficients within 0.3\\pp{}. For the cross-model model, the \\cwm{} deficit has OR$=$0.30 ([0.15, 0.63], $p{=}0.001$, AME$=$\\,$-$21.1\\pp{}). Direction, magnitude, and significance of all primary effects are concordant between LPM and logistic regression; minor discrepancies in secondary effects (model identity, formulation$\\times$model interaction: $p{=}0.449$ and $p{=}0.860$ under GEE vs.\\ $p{=}0.002$ and $p{=}0.006$ under LPM) reflect the GEE's more conservative cluster-robust inference with $k{=}25$ clusters. The discrepancy in secondary effects reflects cluster count: the cross-complexity model ($k{=}139$) yields reliable sandwich SEs, while the cross-model model ($k{=}25$) falls below the $k{\\geq}40$ threshold recommended for stable cluster-robust inference~\\cite{cameron2008bootstrap}.\n\n\\section{CWM Parseable Bias Analysis}\n\\label{app:parseable_bias}\n\nThe default-to-pass assignment for unparseable \\cwm{} outputs is not random with respect to instance difficulty. Unparseable instances have significantly higher pass rates than parseable ones (74.6\\% vs.\\ 68.3\\%, $\\chi^2$ $p = 5.9 \\times 10^{-10}$), and \\cls{} models achieve higher accuracy on unparseable instances (86.4\\% vs.\\ 79.1\\%, $p = 3.3 \\times 10^{-18}$). This indicates that \\cwm{}'s parsing failures concentrate on simpler, pass-heavy instances where the majority-class default happens to be correct more often. Cross-model Jaccard overlap of unparseable instance sets is 0.46, confirming this pattern is instance-driven (specific inputs consistently cause parsing failure across models) rather than stochastic. The net effect is that \\cwm{}'s reported accuracy is inflated by default-correct assignments on easy instances, while its effective discriminative accuracy on harder instances is substantially lower than the aggregate figure suggests.\n\n\n\\section{Threats to Validity (Full Analysis)}\n\\label{app:threats}\n\nWe identify five potential confounds and assess their impact on our conclusions.\n\n\\paragraph{Checkpoint selection.} Val-based selection is unavailable for runs with NaN validation loss (all \\cwm{} repo-level runs, DeepSeek \\cls{} s123), which default to the final epoch checkpoint. A checkpoint ablation on Qwen3-8B \\cls{} s42 quantifies this confound: epoch~1 (ckpt-2200) achieves 85.34\\%, val-selected (ckpt-3600) 84.48\\%, and final epoch (ckpt-6633) 85.29\\%---a $<$1\\pp{} range. The val-selected checkpoint is the lowest, indicating no upward bias from checkpoint selection. The Qwen3-8B \\traj{} comparison (epoch 2: 72.92\\% vs.\\ epoch 3: 70.83\\%) shows a slightly larger ${\\sim}$2\\pp{} shift. For \\cwm{}, the convergence analysis (Appendix~\\ref{app:cwm_convergence}) shows eval loss at the final epoch is 1.8$\\times$ its minimum; however, early-stopped checkpoints retain high unparseable rates, leaving the qualitative ranking unchanged.\n\n\\paragraph{\\cwm{} convergence analysis.}\n\\label{app:cwm_convergence}\nQwen3-8B \\cwm{} repo-level eval loss reaches its minimum within ${\\sim}$5\\% of training (step 300--400 of 6{,}633) and increases monotonically thereafter, with no plateau or recovery (Table~\\ref{tab:cwm_convergence}). This pattern is consistent across all three seeds, confirming systematic overfitting to trace generation rather than stochastic variation. The final-epoch eval loss is ${\\sim}$1.8$\\times$ the optimal value. By contrast, function-level \\cwm{} achieves \\cls{}-equivalent accuracy (TOST $p{=}0.007$) with the same training recipe, indicating that the overfit is specific to repo-level output complexity. Cross-model validation: a DeepSeek-Coder early-stopped checkpoint (s123, epoch~1) achieves 75.45\\% versus 57.31\\% at epoch~3 (s123; +18.14\\pp{}), but retains 66.4\\% unparseable rate, confirming that format collapse emerges early and is not a late-training artifact. No epoch-level checkpoint is available for Qwen3 CWM (only step-level checkpoints at steps 300/400 and late steps ${\\geq}$5800; continuous epoch checkpointing was not enabled for this training run). The convergence analysis (Table~\\ref{tab:cwm_convergence}) shows eval loss minimum at step 300--400 across all three Qwen3 seeds, consistent with DeepSeek-Coder's epoch-1 improvement, providing cross-model evidence that the overtraining pattern generalizes.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{\\cwm{} repo-level eval loss across training (Qwen3-8B, 3 seeds). Minimum is reached at step 300--400 (${\\sim}$5\\% of training); subsequent training monotonically increases loss.}\n\\label{tab:cwm_convergence}\n\\begin{tabular}{lccc}\n\\toprule\nStep & s42 & s123 & s456 \\\\\n\\midrule\n300 & 0.291 & \\textbf{0.288} & \\textbf{0.277} \\\\\n400 & \\textbf{0.286} & 0.306 & 0.283 \\\\\n1000 & 0.333 & 0.336 & 0.351 \\\\\n3000 & 0.445 & 0.453 & 0.435 \\\\\n6600 & 0.521 & 0.517 & 0.507 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Evaluation sequence length.} \\cwm{} accuracy varies by ${\\sim}$9\\pp{} across evaluation sequence lengths for the same checkpoint (seq2048: ${\\sim}$65\\% vs.\\ seq4096: ${\\sim}$56\\%), driven by unparseable-rate differences that propagate through majority-class default assignment. \\cls{} is invariant to this parameter. Cross-model \\cwm{} comparisons use different eval lengths (Qwen3: 8192, DeepSeek: 4096) and are not directly comparable in absolute terms. A matched-sequence evaluation shows ${\\sim}$1.5\\pp{} difference for \\cls{} (Appendix~\\ref{app:ablations}), insufficient to explain the 18--26\\pp{} gap. Furthermore, increasing Qwen3-8B \\cwm{} evaluation from seq4096 to seq8192 \\emph{raises} the unparseable rate (63.7\\%$\\to$73.8\\%) while changing accuracy by only 0.81\\pp{} (64.36\\%$\\to$65.17\\%); giving the model more generation budget worsens format compliance rather than improving it, confirming that format collapse is a structural bottleneck rather than a truncation artifact. Practitioners must standardize evaluation sequence length for generation-based formulations.\n\n\\paragraph{Preprocessing.} DeepSeek \\cls{} accuracy ranges from 82.61\\% (s42, drop preprocessing) to 74.93\\% (s123, truncate preprocessing), a 7.68\\pp{} spread that conflates preprocessing strategy, checkpoint selection method, and seed. The two strategies produce different effective training sets (67,343 vs.\\ 70,748 samples) and different checkpoint selection regimes. The qualitative ranking \\cls{} $>$ \\cwm{} holds under both strategies (Table~\\ref{tab:taxonomy}).\n\n\\paragraph{\\traj{} training regime.} \\traj{} uses a different training configuration: smaller training set (${\\sim}$400 repo-level variants vs.\\ ${\\sim}$70K per-test instances), higher learning rate ($2{\\times}10^{-4}$ vs.\\ $5{\\times}10^{-5}$), and variant-level labels. This asymmetry is inherent to the formulation (trajectory-level labels are only available at variant granularity), but precludes training-data-controlled comparison at repo level. The downsample ablation confirms the \\cls{} formulation advantage persists at matched data volume (80.74\\% vs.\\ 72.92\\%; Appendix~\\ref{app:downsample}), though it controls for training volume but not label granularity (per-test vs.\\ variant-level). Crucially, \\traj{} achieves statistical equivalence with \\cls{} at function level (${\\leq}$1.3\\pp{}, \\S\\ref{sec:func_results}), demonstrating the formulation itself is viable; the repo-level gap attribution remains uncertain: data volume (${\\sim}$400 variants vs.\\ ${\\sim}$70K per-test instances) and label granularity (variant-level vs.\\ per-test) are both plausible confounds that cannot be separately controlled.\n\n\\paragraph{\\cwm{} scale and pretraining.} Our \\cwm{} baseline uses 4--8B LoRA fine-tuning without execution trace pretraining. The original Code World Model~\\cite{meta2025cwm} uses 32B parameters with mid-training on execution traces, a fundamentally different training regime. At larger scale or with execution-trace pretraining, the generation bottleneck observed here may diminish: larger models produce more coherent long-form outputs, and execution trace exposure may improve output format compliance. This is the primary limitation: all repo-level \\cwm{} conclusions are conditional on the ${\\leq}$8B LoRA regime.\n\nDespite these confounds, the repo-level \\cls{}--\\cwm{} gap (18--26\\pp{}) exceeds any single assessed confound. Even under worst-case compounding (${\\sim}$11.5\\pp{}), the gap retains ${\\geq}$7.5\\pp{} margin; confounds predominantly disadvantage \\cwm{}. However, correlated confounds and limited seed coverage mean definitive causal attribution requires multi-seed replication. At $n{=}48$, the minimum detectable effect (MDE) is ${\\sim}$25\\pp{}~\\cite{hoenig2001}; the \\cls{}--\\cwm{} gap (29--35\\pp{}) exceeds this threshold, while the \\cls{}--\\traj{} gap ($<$10\\pp{}) falls below it, consistent with our TOST equivalence finding. Holm-Bonferroni correction across the four primary comparisons ($k{=}4$) confirms both the \\cls{}--\\cwm{} gap (adjusted $p{=}0.012$) and function-level equivalence (adjusted $p{=}0.021$) survive; the repo-level \\cwm{}--\\traj{} comparison is directionally consistent but does not survive correction (adjusted $p{=}0.078$; Table~\\ref{tab:holm}). The consistent direction across both model families and all tested configurations supports a formulation-level explanation, though definitive causal attribution requires future experiments addressing each confound individually.\n\n\n\\section{Extended Limitations}\n\\label{app:limitations}\n\nThe same-size 4B comparison uses a single seed; \\cls{} 4B seed 123 (val-best ckpt-800) achieves only 75.33\\% test accuracy (+2.4\\pp{} above majority baseline); val-best selection at an early checkpoint (step 800) amplifies the val-test distribution shift observed across all configurations. The \\cwm{} 8B comparison uses 3 seeds per model. The validation and test sets have zero problem overlap but differ in mutation type composition (Table~\\ref{tab:mutation_distribution}): \\texttt{operator\\_swap} shifts from 19.1\\% (val) to 34.3\\% (test), the largest single-type distribution mismatch (+15.2\\pp{}). All repo-level results use val-selected checkpoints, and checkpoint selection variance could contribute to observed differences. Our training data is synthetically constructed from mutation operators rather than real developer patches. While mutation testing literature establishes that mutants are reasonable proxies for real faults in test effectiveness studies~\\cite{andrews2005mutation,just2014mutants}, these findings concern mutation \\emph{adequacy} (whether tests that kill mutants also detect real faults), not whether verifiers trained on mutants transfer to real patches. However, the coupling effect underlying these results supports \\emph{relative ranking} validity: a domain shift from synthetic mutations to real bugs may affect absolute accuracy levels, but our core finding---that formulation choice matters at repo level but not function level---concerns relative performance ordering, which is expected to be preserved under distributional shifts that affect all formulations equally. The synthetic-to-real transfer gap for absolute accuracy remains untested. The \\traj{} training configuration differs from \\cls{}/\\cwm{}: smaller training set (${\\sim}$400 vs.\\ ${\\sim}$70K instances), different learning rate ($2{\\times}10^{-4}$ vs.\\ $5{\\times}10^{-5}$), and variant-level evaluation ($n{=}48$ vs.\\ per-test $n{=}9{,}784$). The function-level TOST equivalence ($p = 0.007$, $\\pm$2\\pp{}) is computed on 523 matched variant-level instances across 5 seeds; 2 of 5 seeds use NF4 quantization. Restricting to three bfloat16 seeds yields a comparable mean gap ($-$0.45\\pp{}) but wider confidence interval (df${=}$2); the TOST $p$-value increases from 0.007 to 0.128, which reflects reduced statistical power rather than a shift in the point estimate. The NF4 seeds contribute precision (narrowing the CI) without shifting the mean, consistent with precision being comparable across both quantization levels at function level. Repo-level \\cls{}--\\traj{} comparison should be interpreted with caution due to configuration and granularity differences.\n",
      "numLines": 566,
      "startLine": 1,
      "totalLines": 566
    }
  },
  "sourceToolAssistantUUID": "fe4b017d-05e0-4e8e-8806-f29a21adddf7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier",
  "sessionId": "8c11e549-46d3-438b-848f-c86f519fca39",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-22T19:19:00.480Z_

<details open><summary>🔧 Tool call — Read · `toolu_01PcBwdDtsQ2p7mxQWj6yrvv`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "86515315-9cf2-46cf-9a93-0bc33ea9fe6f",
  "isSidechain": false,
  "requestId": "req_011CbJ9UoRFm2GRjSasNgqwg",
  "type": "assistant",
  "uuid": "d4ca029e-39f7-4bf2-b3a9-2917ec676583",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier",
  "sessionId": "8c11e549-46d3-438b-848f-c86f519fca39",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01U16PPjqHqZa23X2kRksyjc",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 614,
      "cache_read_input_tokens": 24786,
      "output_tokens": 748,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 614,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 748,
          "cache_read_input_tokens": 24786,
          "cache_creation_input_tokens": 614,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 614
          },
          "type": "message"
        }
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

_source line 32 · 2026-05-22T19:19:00.485Z_

<details><summary>↩ Tool result · `toolu_01PcBwdDtsQ2p7mxQWj6yrvv`</summary>

```text
1	\documentclass[11pt]{article}
2	
3	% ACL style (review mode for anonymous ARR submission)
4	\usepackage[review]{acl}
5	
6	% Fonts — Times Roman (required by ACL/ARR template)
7	\usepackage{times}
8	
9	% Math
10	\usepackage{amsmath}
11	\usepackage{amssymb}
12	
13	% Tables
14	\usepackage{booktabs}
15	\usepackage{multirow}
16	\usepackage{tabularx}
17	
18	% Graphics
19	\usepackage{graphicx}
20	\graphicspath{{../../artifacts/}}
21	
22	% Lists
23	\usepackage{enumitem}
24	
25	% Custom commands
26	\newcommand{\cls}{\textsc{Cls}}
27	\newcommand{\cwm}{\textsc{Cwm}}
28	\newcommand{\traj}{\textsc{Traj}}
29	\newcommand{\fone}{F\textsubscript{1}}
30	\newcommand{\pp}{\,\text{pp}}
31	\newcommand{\tbd}{\textsc{tbd}}
32	
33	\title{A Systematic Comparison of Execution-Free Verification Formulations for Code Repair}
34	\author{Anonymous}
35	
36	\begin{document}
37	\maketitle
38	
39	\input{abstract}
40	
41	\input{introduction}
42	
43	\begin{figure*}[t]
44	\centering
45	\includegraphics[width=\textwidth]{figures/paper/fig1_reformulation.pdf}
46	\caption{Three verification formulations. \textbf{Left:} \cls{} predicts binary pass/fail per test (1 output token). \textbf{Center:} \cwm{} generates execution output, derives verdict by exact match ($O(L)$ tokens). \textbf{Right:} Trajectory-level scoring predicts patch-level resolved/unresolved (1 token, no per-test signal). Each formulation makes different tradeoffs between output complexity, diagnostic granularity, and inference cost.}
47	\label{fig:reformulation}
48	\end{figure*}
49	
50	\input{method}
51	
52	\input{experiments}
53	
54	\begin{figure}[t]
55	\centering
56	\includegraphics[width=\columnwidth]{figures/paper/fig2_scaling_gap.pdf}
57	\caption{Gap amplification from function to repo level. At function level, the \cls{}--\cwm{} gap is 1--3\pp{}; at repo level, it widens to 18--26\pp{} with \cwm{} falling below majority baseline.}
58	\label{fig:scaling_gap}
59	\end{figure}
60	
61	
62	\input{related_work}
63	
64	\input{conclusion}
65	
66	\bibliography{references}
67	
68	\input{checklist}
69	
70	\input{appendix}
71	
72	\end{document}
73	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d4ca029e-39f7-4bf2-b3a9-2917ec676583",
  "isSidechain": false,
  "promptId": "ec010885-b9c9-4574-b4a8-341b5a1f339a",
  "type": "user",
  "uuid": "998ed5af-3180-4d95-854c-0ab0765b08fb",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/main.tex",
      "content": "\\documentclass[11pt]{article}\n\n% ACL style (review mode for anonymous ARR submission)\n\\usepackage[review]{acl}\n\n% Fonts — Times Roman (required by ACL/ARR template)\n\\usepackage{times}\n\n% Math\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\n% Tables\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{tabularx}\n\n% Graphics\n\\usepackage{graphicx}\n\\graphicspath{{../../artifacts/}}\n\n% Lists\n\\usepackage{enumitem}\n\n% Custom commands\n\\newcommand{\\cls}{\\textsc{Cls}}\n\\newcommand{\\cwm}{\\textsc{Cwm}}\n\\newcommand{\\traj}{\\textsc{Traj}}\n\\newcommand{\\fone}{F\\textsubscript{1}}\n\\newcommand{\\pp}{\\,\\text{pp}}\n\\newcommand{\\tbd}{\\textsc{tbd}}\n\n\\title{A Systematic Comparison of Execution-Free Verification Formulations for Code Repair}\n\\author{Anonymous}\n\n\\begin{document}\n\\maketitle\n\n\\input{abstract}\n\n\\input{introduction}\n\n\\begin{figure*}[t]\n\\centering\n\\includegraphics[width=\\textwidth]{figures/paper/fig1_reformulation.pdf}\n\\caption{Three verification formulations. \\textbf{Left:} \\cls{} predicts binary pass/fail per test (1 output token). \\textbf{Center:} \\cwm{} generates execution output, derives verdict by exact match ($O(L)$ tokens). \\textbf{Right:} Trajectory-level scoring predicts patch-level resolved/unresolved (1 token, no per-test signal). Each formulation makes different tradeoffs between output complexity, diagnostic granularity, and inference cost.}\n\\label{fig:reformulation}\n\\end{figure*}\n\n\\input{method}\n\n\\input{experiments}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/paper/fig2_scaling_gap.pdf}\n\\caption{Gap amplification from function to repo level. At function level, the \\cls{}--\\cwm{} gap is 1--3\\pp{}; at repo level, it widens to 18--26\\pp{} with \\cwm{} falling below majority baseline.}\n\\label{fig:scaling_gap}\n\\end{figure}\n\n\n\\input{related_work}\n\n\\input{conclusion}\n\n\\bibliography{references}\n\n\\input{checklist}\n\n\\input{appendix}\n\n\\end{document}\n",
      "numLines": 73,
      "startLine": 1,
      "totalLines": 73
    }
  },
  "sourceToolAssistantUUID": "d4ca029e-39f7-4bf2-b3a9-2917ec676583",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier",
  "sessionId": "8c11e549-46d3-438b-848f-c86f519fca39",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-22T19:19:01.062Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01PkJ6NwTbuAJSEEwAJJDBMK`</summary>

```json
{
  "project": "exec-sim-repair-verifier",
  "file": "paper_framing.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "998ed5af-3180-4d95-854c-0ab0765b08fb",
  "isSidechain": false,
  "requestId": "req_011CbJ9UoRFm2GRjSasNgqwg",
  "type": "assistant",
  "uuid": "f66cda16-6ba4-4770-a8d4-9237f950e00c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier",
  "sessionId": "8c11e549-46d3-438b-848f-c86f519fca39",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01U16PPjqHqZa23X2kRksyjc",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 614,
      "cache_read_input_tokens": 24786,
      "output_tokens": 748,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 614,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 748,
          "cache_read_input_tokens": 24786,
          "cache_creation_input_tokens": 614,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 614
          },
          "type": "message"
        }
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

_source line 34 · 2026-05-22T19:19:01.164Z_

```json
{
  "parentUuid": "0671c6fd-d357-4415-b884-0e91191f1180",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "9699ae9d-6e10-4c29-8a46-08a123cfb3b8",
  "timestamp": "2026-05-22T19:19:01.164Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier",
  "sessionId": "8c11e549-46d3-438b-848f-c86f519fca39",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

---

### Runtime record

_source line 35_

```json
{
  "type": "last-prompt",
  "leafUuid": "9699ae9d-6e10-4c29-8a46-08a123cfb3b8",
  "sessionId": "8c11e549-46d3-438b-848f-c86f519fca39"
}
```

---

### Runtime record

_source line 36_

```json
{
  "type": "ai-title",
  "aiTitle": "Audit paper for 14B model data insertion points",
  "sessionId": "8c11e549-46d3-438b-848f-c86f519fca39"
}
```

---

### Assistant

_source line 37 · 2026-05-22T19:19:47.347Z_

<details><summary>Logged reasoning block</summary>

```text
Now let me also read the checklist.tex file for completeness.

Let me now compile the full audit. I have all the information needed. Let me systematically go through everything:

### Tables that need 14B rows:

1. **Table 1 (tab:main_results)** - experiments.tex lines 25-58: Function-level per-test accuracy. Currently has Qwen3-4B rows. Need to add Qwen3-14B rows for CLS/CWM/TRAJ.

Wait, actually let me reconsider. Currently the paper has:
- Qwen3-4B (primary, 5 seeds)


- DeepSeek-Coder-6.7B (cross-model check, 2 seeds)
- Prompting baselines with 8B, 6.7B, 32B

And there's a scaling table with 4B and 8B for Qwen3. So the 14B model would be a third point in the scaling analysis, and potentially a new row in the main results table.

Let me be thorough:

### Tables

1. **Table 1 (tab:main_results)** - experiments.tex:25-58 - Function-level results. Has Qwen3-4B rows. Need 14B rows for CLS/CWM/TRAJ under a new scaling section.

Actually, looking more carefully at the current setup: Qwen3-4B is fine-tuned with 5 seeds, DeepSeek-Coder-6.7B is fine-tuned with 2 seeds, and the baselines are 0-shot/ICL with 8B, 6.7B, and 32B. The question is whether 14B goes into the main results table or just the scaling table.

2. **Table 2 (tab:scaling)** - experiments.tex:68-88 - Model-size scaling. Currently has 4B and 8B. Need to add 14B row and update the delta column to show progression across all three sizes.

3. **Table 3 (tab:repo_level)** - experiments.tex:112-135 - Repo-level results. Has...

Qwen3-4B, Qwen3-8B, DeepSeek-6.7B. Need 14B row.

4. **Table 4 (tab:taxonomy)** - experiments.tex:145-162 - Failure mode taxonomy. May need 14B examples if failure modes differ.

5. **Table (appendix) tab:variant_level** - appendix.tex:159-193 - Variant-level accuracy. Need 14B row.

6. **Table (appendix) tab:mutation_breakdown** - appendix.tex:109-127 - Per-mutation breakdown. Need 14B columns.

7. **Table (appendix) tab:cwm_mutation_parse** - appendix.tex:136-150 - CWM parse rates. Need 14B column.

8. **Table (appendix) tab:hyperparams** - appendix.tex:200-243 - Hyperparameters. Need 14B config

.

The mutation distribution table is dataset-specific so probably doesn't need changes unless the 14B model uses different data. For convergence analysis, I'll need 14B results if those experiments were run at that scale. The variant-level effect sizes might require 14B comparisons, and the scaling gap figure currently only shows 4B and 8B, so I need to add the 14B data point there.

I also notice there's a `figure2_v2.pdf` in the artifacts. Now I'm going through the prose sections to find all mentions of model sizes. The abstract references "≤8B LoRA fine-tuning" and "≤8B LoRA protocol" which both need updating to reflect 14B. In the introduction, there are similar references to the 8B limit, plus mentions of specific models like Qwen3-4B and Qwen3-8B in the experimental setup that may need expansion.

Looking at the experiments section, I see references to fine-tuning Qwen3-4B and Qwen3-8B that should include 14B, mentions of DeepSeek-Coder-6.7B, and claims about model coverage being limited to 6-8B code-specialized LLMs. There are also specific numerical results comparing formulations at different scales—accuracy numbers, scaling comparisons at 4B and 8B, and performance gaps that widen as model size increases.

In the conclusion, I notice "${\leq}$8B LoRA" appears twice and the findings are explicitly conditioned on this constraint, with testing mentioned at 32B. I'm seeing additional mentions of model sizes scattered throughout the appendix and paper framing—checkpoint selection at 8B, the CWM scale specification of 4–8B LoRA fine-tuning, and the extended limitations repeating the 6–8B code-specialized LLMs constraint. The paper framing document consistently uses "≤8B LoRA" as the qualifier, so adding 14B experiments would require updating this language throughout to reflect broader model coverage.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9699ae9d-6e10-4c29-8a46-08a123cfb3b8",
  "isSidechain": false,
  "requestId": "req_011CbJ9VShr1FeR9tiiQXVNK",
  "type": "assistant",
  "uuid": "61fa7c45-809b-40c9-aa53-2364d9b31375",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier",
  "sessionId": "8c11e549-46d3-438b-848f-c86f519fca39",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019SmukqskdCjAAXLJDCg9vR",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 36903,
      "cache_read_input_tokens": 25400,
      "output_tokens": 4947,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 36903,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 4947,
          "cache_read_input_tokens": 25400,
          "cache_creation_input_tokens": 36903,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 36903
          },
          "type": "message"
        }
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

_source line 38 · 2026-05-22T19:20:35.009Z_

Now I have all the content. Let me compile the audit.

## 14B 数据插入点清单

### Tables

1. **Table 1 `tab:main_results`** (experiments.tex:25–58): Function-level per-test accuracy。当前有 Qwen3-4B / DeepSeek-6.7B。需要加 Qwen3-14B 行（CLS/CWM/TRAJ）。

2. **Table 2 `tab:scaling`** (experiments.tex:68–88): Model-size scaling，当前只有 4B 和 8B 两行。需要加 14B 行，并更新 $\Delta$ 列（新增 8B→14B 增量）。这是 14B 数据最核心的表。

3. **Table 3 `tab:repo_level`** (experiments.tex:112–135): Repo-level 跨 formulation 比较。当前有 Qwen3-4B / Qwen3-8B / DeepSeek-6.7B。需要加 Qwen3-14B 行。

4. **Table 4 `tab:taxonomy`** (experiments.tex:145–162): Failure mode taxonomy。如果 14B 的 CWM format collapse 率有变化，需要更新或增加 14B representative 行。

5. **Table `tab:variant_level`** (appendix.tex:159–193): Variant-level accuracy。需要加 Qwen3-14B 行（CLS/CWM/TRAJ）。

6. **Table `tab:mutation_breakdown`** (appendix.tex:109–127): Per-mutation accuracy。当前有 CLS 4B/8B 和 CWM 4B/8B 列。需要加 CLS 14B 和 CWM 14B 列。

7. **Table `tab:cwm_mutation_parse`** (appendix.tex:136–150): CWM parse rates per mutation。当前有 4B/8B。需要加 14B 列。

8. **Table `tab:hyperparams`** (appendix.tex:200–243): Training hyperparameters。Model-family-specific 表当前有 Qwen3-4B / Qwen3-8B / DS-6.7B 三列。需要加 Qwen3-14B 列。

9. **Table `tab:cwm_convergence`** (appendix.tex:533–549): CWM eval loss across training。如果跑了 14B CWM repo-level，需要加 14B 列。

10. **Table `tab:variant_power`** (appendix.tex:450–471): Variant-level bootstrap analysis。需要加 14B 相关的 CLS vs CWM / CLS vs TRAJ 行。

11. **Table `tab:rank_ablation`** (appendix.tex:49–64): LoRA rank ablation for CWM。当前只有 4B。如果 14B 也做了 rank ablation 需要加；否则可不改。

---

### Figures

1. **Figure 2 `fig:scaling_gap`** (main.tex:54–59, 引用 `figures/paper/fig2_scaling_gap.pdf`): Gap amplification 图。当前显示 4B→8B 两个点。需要加 14B 数据点，变成三点连线。**这是最重要的图更新。**

2. 可能需要检查 `figure2_v2.pdf` / `figure2_v2.png` 是否是 Figure 2 的新版本，需要同步更新。

---

### 正文段落

#### Abstract (abstract.tex)
- **Line 4**: `"under ${\leq}$8B LoRA fine-tuning"` → 需要改为 `≤14B` 或 `4–14B`
- **Line 4**: `"under our ${\leq}$8B LoRA protocol"` → 同上

#### Introduction (introduction.tex)
- **Line 8**: `"two representative code LLM families (Qwen3, DeepSeek-Coder)"` — 模型列表可能需要提及 14B
- **Line 8**: `"${\leq}$8B LoRA protocol"` → 更新
- **Line 8**: `"35--36\pp{} at repo level"` — 如果 14B 基线不同，需要更新
- **Line 13**: `"at repository level under ${\leq}$8B LoRA"` → 更新
- **Line 14**: `"We fine-tune Qwen3-4B and Qwen3-8B"` 间接引用（在 experiments 里），但 intro 也提到模型覆盖范围

#### Experiments — Setup (experiments.tex:14)
- **Line 14**: `"We fine-tune Qwen3-4B and Qwen3-8B"` → 加 `Qwen3-14B`
- **Line 14**: `"DeepSeek-Coder-6.7B"` 保持不变

#### Experiments — Scaling (experiments.tex:63–92)
- **Line 66**: `"Table~\ref{tab:scaling} compares all three formulations at 4B and 8B"` → 加 14B
- **Line 71**: Table caption `"accuracy (\%) at 4B and 8B"` → 加 14B
- **Line 90**: `"The \cls{}--\cwm{} gap widens from 1.32\pp{} at 4B to 2.62\pp{} at 8B"` → 需要加 14B 的 gap 数值
- **Line 92**: `"\cwm{} flat scaling ($-$0.03\pp{})"` → 看 14B 是否依然 flat
- **Line 92**: `"\traj{} also shows no scaling benefit at repo level (72.92\% at both 4B and 8B); only \cls{} scales positively"` → 更新 14B 数据

#### Experiments — Repo-level (experiments.tex:107–168)
- **Line 139**: `"the gap is 25.59\pp{} at 4B...and 18.35\pp{} at 8B"` → 加 14B gap
- **Line 164**: CWM default assignment artifact 的 4B→8B 趋势 → 加 14B
- **Line 166**: `"The \cls{}--\cwm{} gap widens from 1--3\pp{} (function) to 18--26\pp{} (repo)"` → 范围可能需要调整
- **Line 168**: 混合效应模型可能需要纳入 14B 数据重新拟合

#### Experiments — Analysis (experiments.tex:173–183)
- **Line 180**: `"217$\times$ higher throughput"` — 如果 14B 有不同的推理效率数据
- **Line 182**: oracle/complementarity 数字可能需要更新

#### Conclusion (conclusion.tex)
- **Line 4**: `"${\leq}$8B LoRA"` 出现两次 → 更新为 `≤14B`
- **Line 4**: `"All findings are conditioned on ${\leq}$8B LoRA fine-tuning"` → 更新
- **Line 6**: `"testing at 32B+ would resolve the primary open question"` → 如果 14B 缩小了 gap，这句可能需要修改

#### Limitations (conclusion.tex:8–10)
- **Line 8**: `"${\leq}$8B LoRA fine-tuning"` → 更新
- **Line 10**: `"Model coverage is limited to 6--8B code-specialized LLMs"` → 更新为 `6--14B`

#### Appendix — Threats (appendix.tex:522–559)
- **Line 557**: `"4--8B LoRA fine-tuning"` → `4--14B`
- **Line 557**: `"all repo-level \cwm{} conclusions conditional on the ${\leq}$8B LoRA regime"` → 更新
- **Line 559**: `"the repo-level \cls{}--\cwm{} gap (18--26\pp{}) exceeds any single assessed confound"` → 范围可能变化
- **Line 564**: `"6--8B code-specialized LLMs"` → `6--14B`

#### Appendix — Extended Analysis (appendix.tex:361–411)
- **Paragraph (g) Failed interventions**: `"Model scaling (4B→8B)"` → 如果 14B 改变了结论，需要重写或追加 8B→14B 结果
- **Paragraph (i) Inference efficiency**: throughput 数据可能需要加 14B
- **Paragraph (k) CoT**: `"Within the ${\leq}$8B LoRA regime"` → 更新

#### Appendix — Hyperparams (appendix.tex:253)
- **Line 253**: `"Total compute budget: ${\sim}$370 GPU-hours across 223 completed runs"` → 加上 14B runs 的 GPU 时间

#### Appendix — Interaction model (appendix.tex:505–514)
- 混合效应回归可能需要纳入 14B 数据重新拟合，或至少提及 14B 支持/改变现有结论

---

### paper_framing.md 更新点
- `"≤8B LoRA"` 贯穿全文 → 改为 `≤14B`
- `"Model coverage is limited to 6--8B"` → `6--14B`
- Story Spine 中 `"At ≤8B LoRA deployment scale"` → 更新
- Anticipated Reviewer Concerns 的 `"CWM comparison unfair (≤8B LoRA)"` → 14B 数据部分缓解此 concern

---

### 优先级排序

| 优先级 | 位置 | 原因 |
|--------|------|------|
| P0 | Table 2 (scaling) + Figure 2 | 14B 是第三个 scaling 数据点，直接影响 scaling story |
| P0 | Table 3 (repo_level) | repo-level 是论文核心差异化结论 |
| P0 | Abstract / Conclusion 中 `≤8B` 措辞 | 读者第一印象和最终结论 |
| P1 | Table 1 (main_results) | 如果 14B function-level 也跑了 |
| P1 | experiments.tex §Scaling 段落叙述 | 需要描述 14B 趋势 |
| P1 | experiments.tex §Repo-level 段落 gap 数值 | 更新 range |
| P2 | Appendix tables (variant_level, mutation_breakdown, cwm_parse, hyperparams) | 完整性 |
| P2 | Appendix threats / limitations 中 `≤8B` | 措辞一致性 |
| P3 | paper_framing.md | 内部文档，非论文本体 |

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "61fa7c45-809b-40c9-aa53-2364d9b31375",
  "isSidechain": false,
  "requestId": "req_011CbJ9VShr1FeR9tiiQXVNK",
  "type": "assistant",
  "uuid": "d8c82b5d-bb0e-4489-bd01-5142bb43871b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier",
  "sessionId": "8c11e549-46d3-438b-848f-c86f519fca39",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019SmukqskdCjAAXLJDCg9vR",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 36903,
      "cache_read_input_tokens": 25400,
      "output_tokens": 4947,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 36903,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 4947,
          "cache_read_input_tokens": 25400,
          "cache_creation_input_tokens": 36903,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 36903
          },
          "type": "message"
        }
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

_source line 39_

```json
{
  "type": "last-prompt",
  "leafUuid": "d8c82b5d-bb0e-4489-bd01-5142bb43871b",
  "sessionId": "8c11e549-46d3-438b-848f-c86f519fca39"
}
```

---

### Runtime record

_source line 40_

```json
{
  "type": "ai-title",
  "aiTitle": "Audit paper for 14B model data insertion points",
  "sessionId": "8c11e549-46d3-438b-848f-c86f519fca39"
}
```

---
