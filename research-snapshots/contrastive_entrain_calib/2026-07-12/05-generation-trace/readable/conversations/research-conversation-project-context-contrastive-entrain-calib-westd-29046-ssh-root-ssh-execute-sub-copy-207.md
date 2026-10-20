# Research conversation: <project_context> # 项目: contrastive_entrain_calib ## 运行环境 - 服务器名: westd-29046 - SSH 账户: root（调用 ssh_execute / submit_tra

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 24
- **Recorded user turns:** 1
- **Tool calls:** 4
- **Original source:** `logs/chats/exported-trajectories/account-1/18617432-1b96-47d9-ab5a-20c855a029c1.jsonl`
- **Structured JSON:** [`19556cefa782d7661cac.json`](../../sessions/19/19556cefa782d7661cac.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-22T11:58:37.042Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-22T11:58:37.042Z",
  "sessionId": "18617432-1b96-47d9-ab5a-20c855a029c1",
  "content": "&lt;project_context>\n# 项目: contrastive_entrain_calib\n\n## 运行环境\n- 服务器名: westd-29046\n- SSH 账户: root（调用 ssh_execute / submit_training_job 时传入 account=\"root\"）\n- SSH 连接命令: ssh connect.westd.seetacloud.com  # 必须用此命令，~/.ssh/config 自动应用密钥和跳板机，禁止用裸 IP\n- 项目代码根目录: /root/contrastive_entrain_calib\n\n\n## 环境搭建\n连接服务器后先调 `detect_image` 检测是否为预置镜像。如果匹配，跳过基础环境搭建，只装项目特有依赖。已预装的包不要重复安装。\n\n## 输出风格\n回复简洁直接。只输出执行结果和必要信息，不要解释过程、不要客套、不要给未被要求的建议。\n&lt;/project_context>\n## 任务：研究 Wu & Tang (2026) \"When Reward Hacking Rebounds\" (arXiv:2604.01476)\n\n### 背景\n我们的论文发现 representation-level directions (d_syc) 作为 GRPO reward 会失败——discriminability ≠ reward utility。审稿人 SF-8 提到 Wu & Tang (2026) 可能是相关工作。我们需要确认他们的方法与我们的发现是否一致或矛盾。\n\n### 必须确认的问题\n\n1. **他们用 representation-level concept directions 在 GRPO 中做什么任务？**（reward hacking detection? 或直接作为 reward?）\n2. **成功了吗？什么 metric？**（如果成功，需要理解为什么他们成功而我们失败——可能是任务差异）\n3. **Representation direction 是怎么融入 GRPO 的？**（scalar reward? advantage modification? 其他机制？）\n4. **他们的 representation direction 和目标行为之间是否有 geometric conflation 问题？**（即 direction 是否混淆了不同行为类别，类似我们的 d_syc 混淆 sycophantic capitulation 和 genuine revision）\n\n### 方法\n- 用 WebSearch 搜索 arXiv:2604.01476 或 \"When Reward Hacking Rebounds Wu Tang 2026\"\n- 如果找到 PDF/HTML，重点阅读 Method 和 Results 部分\n- 如果是长论文，优先看 Abstract、Section 3 (Method)、Section 4 (Results)、Related Work\n\n### 输出\n逐条回答上述 4 个问题，每个答案附原文引用。如果论文不可获取，报告搜索尝试。\n"
}
```

---

### Runtime record

_source line 2 · 2026-05-22T11:58:37.046Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-22T11:58:37.046Z",
  "sessionId": "18617432-1b96-47d9-ab5a-20c855a029c1"
}
```

---

## Round 1

22 recorded events

### User

_source line 3 · 2026-05-22T11:58:37.084Z_

&lt;project_context>
# 项目: contrastive_entrain_calib

## 运行环境
- 服务器名: westd-29046
- SSH 账户: root（调用 ssh_execute / submit_training_job 时传入 account="root"）
- SSH 连接命令: ssh connect.westd.seetacloud.com  # 必须用此命令，~/.ssh/config 自动应用密钥和跳板机，禁止用裸 IP
- 项目代码根目录: /root/contrastive_entrain_calib


## 环境搭建
连接服务器后先调 `detect_image` 检测是否为预置镜像。如果匹配，跳过基础环境搭建，只装项目特有依赖。已预装的包不要重复安装。

## 输出风格
回复简洁直接。只输出执行结果和必要信息，不要解释过程、不要客套、不要给未被要求的建议。
&lt;/project_context>
## 任务：研究 Wu & Tang (2026) "When Reward Hacking Rebounds" (arXiv:2604.01476)

### 背景
我们的论文发现 representation-level directions (d_syc) 作为 GRPO reward 会失败——discriminability ≠ reward utility。审稿人 SF-8 提到 Wu & Tang (2026) 可能是相关工作。我们需要确认他们的方法与我们的发现是否一致或矛盾。

### 必须确认的问题

1. **他们用 representation-level concept directions 在 GRPO 中做什么任务？**（reward hacking detection? 或直接作为 reward?）
2. **成功了吗？什么 metric？**（如果成功，需要理解为什么他们成功而我们失败——可能是任务差异）
3. **Representation direction 是怎么融入 GRPO 的？**（scalar reward? advantage modification? 其他机制？）
4. **他们的 representation direction 和目标行为之间是否有 geometric conflation 问题？**（即 direction 是否混淆了不同行为类别，类似我们的 d_syc 混淆 sycophantic capitulation 和 genuine revision）

### 方法
- 用 WebSearch 搜索 arXiv:2604.01476 或 "When Reward Hacking Rebounds Wu Tang 2026"
- 如果找到 PDF/HTML，重点阅读 Method 和 Results 部分
- 如果是长论文，优先看 Abstract、Section 3 (Method)、Section 4 (Results)、Related Work

### 输出
逐条回答上述 4 个问题，每个答案附原文引用。如果论文不可获取，报告搜索尝试。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "d98eea28-12ff-4731-859e-3af8f7d1585e",
  "type": "user",
  "uuid": "98f2a5ad-d952-4c64-b210-e6567dd81efc",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib",
  "sessionId": "18617432-1b96-47d9-ab5a-20c855a029c1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-22T11:58:37.083Z_

```json
{
  "parentUuid": "98f2a5ad-d952-4c64-b210-e6567dd81efc",
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
      "WebSearch"
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
      "WebSearch"
    ],
    "removedNames": []
  },
  "type": "attachment",
  "uuid": "f83b4884-c898-4e8f-a8fb-902d9906b467",
  "timestamp": "2026-05-22T11:58:37.083Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib",
  "sessionId": "18617432-1b96-47d9-ab5a-20c855a029c1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-22T11:58:37.083Z_

```json
{
  "parentUuid": "f83b4884-c898-4e8f-a8fb-902d9906b467",
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
  "uuid": "5a53aa2c-7c9b-4779-b194-1af5dbf90843",
  "timestamp": "2026-05-22T11:58:37.083Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib",
  "sessionId": "18617432-1b96-47d9-ab5a-20c855a029c1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 6 · 2026-05-22T11:58:37.083Z_

```json
{
  "parentUuid": "5a53aa2c-7c9b-4779-b194-1af5dbf90843",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "91540b2a-a038-49ca-a683-7cbe6dd25707",
  "timestamp": "2026-05-22T11:58:37.083Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib",
  "sessionId": "18617432-1b96-47d9-ab5a-20c855a029c1",
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
  "aiTitle": "Research Wu & Tang 2026 reward hacking paper",
  "sessionId": "18617432-1b96-47d9-ab5a-20c855a029c1"
}
```

---

### Assistant

_source line 8 · 2026-05-22T11:58:40.632Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to research a specific paper: Wu & Tang (2026) "When Reward Hacking Rebounds" (arXiv:2604.01476). Let me search for this paper online.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "91540b2a-a038-49ca-a683-7cbe6dd25707",
  "isSidechain": false,
  "requestId": "req_011CbHZucMj5hjRzw5RrVRu9",
  "type": "assistant",
  "uuid": "644604e6-a549-4425-af8e-765836777acf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib",
  "sessionId": "18617432-1b96-47d9-ab5a-20c855a029c1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01M3a4aWpPfKEoUsjydD8bbB",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 11817,
      "cache_read_input_tokens": 11841,
      "output_tokens": 141,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11817,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 141,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11817,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11817
          },
          "type": "message"
        }
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

_source line 9 · 2026-05-22T11:58:40.726Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01GBPPJCaTGNQy3ThoydK6Le`</summary>

```json
{
  "query": "select:WebSearch,WebFetch",
  "max_results": 2
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "644604e6-a549-4425-af8e-765836777acf",
  "isSidechain": false,
  "requestId": "req_011CbHZucMj5hjRzw5RrVRu9",
  "type": "assistant",
  "uuid": "d233fbc7-67fb-461d-a484-1ae985910a11",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib",
  "sessionId": "18617432-1b96-47d9-ab5a-20c855a029c1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01M3a4aWpPfKEoUsjydD8bbB",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 11817,
      "cache_read_input_tokens": 11841,
      "output_tokens": 141,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11817,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 141,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11817,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11817
          },
          "type": "message"
        }
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

_source line 10 · 2026-05-22T11:58:40.733Z_

<details><summary>↩ Tool result · `toolu_01GBPPJCaTGNQy3ThoydK6Le`</summary>

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
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d233fbc7-67fb-461d-a484-1ae985910a11",
  "isSidechain": false,
  "promptId": "d98eea28-12ff-4731-859e-3af8f7d1585e",
  "type": "user",
  "uuid": "eabeea26-2588-4935-b2b9-a249b4292993",
  "toolUseResult": {
    "matches": [
      "WebSearch",
      "WebFetch"
    ],
    "query": "select:WebSearch,WebFetch",
    "total_deferred_tools": 19
  },
  "sourceToolAssistantUUID": "d233fbc7-67fb-461d-a484-1ae985910a11",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib",
  "sessionId": "18617432-1b96-47d9-ab5a-20c855a029c1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-22T11:58:43.627Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01PRriP5GutGzeQHUGR61gPV`</summary>

```json
{
  "query": "arXiv:2604.01476 \"When Reward Hacking Rebounds\" Wu Tang 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "eabeea26-2588-4935-b2b9-a249b4292993",
  "isSidechain": false,
  "requestId": "req_011CbHZutByzLJmiyQp1enCh",
  "type": "assistant",
  "uuid": "f1456668-6d03-41e9-8b16-d8f0ab46b82f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib",
  "sessionId": "18617432-1b96-47d9-ab5a-20c855a029c1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WoEmui7iMRzD1gMksf4y6Y",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1160,
      "cache_read_input_tokens": 23658,
      "output_tokens": 132,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1160,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 132,
          "cache_read_input_tokens": 23658,
          "cache_creation_input_tokens": 1160,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1160
          },
          "type": "message"
        }
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

_source line 12 · 2026-05-22T11:58:43.757Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01GgcJC6zgebhUo3R511qoQM`</summary>

```json
{
  "query": "\"When Reward Hacking Rebounds\" representation direction GRPO reward hacking 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f1456668-6d03-41e9-8b16-d8f0ab46b82f",
  "isSidechain": false,
  "requestId": "req_011CbHZutByzLJmiyQp1enCh",
  "type": "assistant",
  "uuid": "fd2566f4-fc94-4a83-ae37-c259a7714b86",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib",
  "sessionId": "18617432-1b96-47d9-ab5a-20c855a029c1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WoEmui7iMRzD1gMksf4y6Y",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1160,
      "cache_read_input_tokens": 23658,
      "output_tokens": 132,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1160,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 132,
          "cache_read_input_tokens": 23658,
          "cache_creation_input_tokens": 1160,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1160
          },
          "type": "message"
        }
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

_source line 13 · 2026-05-22T11:58:54.196Z_

<details><summary>↩ Tool result · `toolu_01GgcJC6zgebhUo3R511qoQM`</summary>

```text
Web search results for query: ""When Reward Hacking Rebounds" representation direction GRPO reward hacking 2026"

Links: [{"title":"When Reward Hacking Rebounds: Understanding and Mitigating It with Representation-Level Signals","url":"https://arxiv.org/html/2604.01476v1"},{"title":"Reward Hacking in the Era of Large Models: Mechanisms, Emergent Misalignment, Challenges","url":"https://arxiv.org/html/2604.13602v1"},{"title":"GitHub - xhwang22/Awesome-Reward-Hacking: A curated list of papers and resources on Reward Hacking, Emergent Misalignment, and Proxy Exploitation in Large Models · GitHub","url":"https://github.com/xhwang22/Awesome-Reward-Hacking"},{"title":"A brief example of reward hacking in GRPO","url":"https://ishanjmukherjee.github.io/reward-hacking-grpo"},{"title":"[2509.22047] MO-GRPO: Mitigating Reward Hacking of Group Relative Policy Optimization on Multi-Objective Problems","url":"https://arxiv.org/abs/2509.22047"},{"title":"Reward Hacking in Reinforcement Learning | Lil'Log","url":"https://lilianweng.github.io/posts/2024-11-28-reward-hacking/"},{"title":"MO-GRPO: Mitigating Reward Hacking of Group Relative Policy Optimization on Multi-Objective Problems","url":"https://arxiv.org/html/2509.22047"},{"title":"Reward hacking - Wikipedia","url":"https://en.wikipedia.org/wiki/Reward_hacking"},{"title":"Mitigating Reward Hacking in RLHF via Advantage Sign Robustness","url":"https://arxiv.org/html/2604.02986"},{"title":"MO-GRPO: Mitigating Reward Hacking of Group Relative Policy Optimization on Multi-Objective Problems | Request PDF","url":"https://www.researchgate.net/publication/395944746_MO-GRPO_Mitigating_Reward_Hacking_of_Group_Relative_Policy_Optimization_on_Multi-Objective_Problems"}]

I found relevant research on your query. Here are the key findings:

## "When Reward Hacking Rebounds" Paper

The research identifies a three-phase pattern where models first attempt to hack rewards but fail, then temporarily retreat to legitimate solving, and finally rebound into successful hacking with qualitatively different strategies when legitimate reward remains scarce.

### Representation-Level Analysis

Using representation engineering, the researchers extract concept directions for shortcut, deception, and evaluation awareness from domain-general contrastive pairs and find that the shortcut direction tracks hacking behavior most closely, making it an effective representational proxy for detection.

### GRPO-Based Mitigation

The paper proposes Advantage Modification, a method that integrates shortcut concept scores into GRPO advantage computation to penalize hacking rollouts at the training-signal level, providing more robust suppression than generation-time activation steering.

The approach builds on representational analysis by proposing Advantage Modification, a training-time intervention that integrates concept scores into the GRPO advantage computation, and shows that hacking emerges because the policy shifts toward test rewriting where the same reward is obtainable at lower cost, with a clear representational signature where hacking rollouts score systematically higher along a concept direction associated with hacking behavior.

The paper was published in April 2026 and provides a systematic study of reward hacking in coding tasks using environment-manipulation settings.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fd2566f4-fc94-4a83-ae37-c259a7714b86",
  "isSidechain": false,
  "promptId": "d98eea28-12ff-4731-859e-3af8f7d1585e",
  "type": "user",
  "uuid": "a63d7a38-5745-4ad7-8528-4380311d06d0",
  "toolUseResult": {
    "query": "\"When Reward Hacking Rebounds\" representation direction GRPO reward hacking 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_016RGbPuLCCBowqnUnsuG2Va",
        "content": [
          {
            "title": "When Reward Hacking Rebounds: Understanding and Mitigating It with Representation-Level Signals",
            "url": "https://arxiv.org/html/2604.01476v1"
          },
          {
            "title": "Reward Hacking in the Era of Large Models: Mechanisms, Emergent Misalignment, Challenges",
            "url": "https://arxiv.org/html/2604.13602v1"
          },
          {
            "title": "GitHub - xhwang22/Awesome-Reward-Hacking: A curated list of papers and resources on Reward Hacking, Emergent Misalignment, and Proxy Exploitation in Large Models · GitHub",
            "url": "https://github.com/xhwang22/Awesome-Reward-Hacking"
          },
          {
            "title": "A brief example of reward hacking in GRPO",
            "url": "https://ishanjmukherjee.github.io/reward-hacking-grpo"
          },
          {
            "title": "[2509.22047] MO-GRPO: Mitigating Reward Hacking of Group Relative Policy Optimization on Multi-Objective Problems",
            "url": "https://arxiv.org/abs/2509.22047"
          },
          {
            "title": "Reward Hacking in Reinforcement Learning | Lil'Log",
            "url": "https://lilianweng.github.io/posts/2024-11-28-reward-hacking/"
          },
          {
            "title": "MO-GRPO: Mitigating Reward Hacking of Group Relative Policy Optimization on Multi-Objective Problems",
            "url": "https://arxiv.org/html/2509.22047"
          },
          {
            "title": "Reward hacking - Wikipedia",
            "url": "https://en.wikipedia.org/wiki/Reward_hacking"
          },
          {
            "title": "Mitigating Reward Hacking in RLHF via Advantage Sign Robustness",
            "url": "https://arxiv.org/html/2604.02986"
          },
          {
            "title": "MO-GRPO: Mitigating Reward Hacking of Group Relative Policy Optimization on Multi-Objective Problems | Request PDF",
            "url": "https://www.researchgate.net/publication/395944746_MO-GRPO_Mitigating_Reward_Hacking_of_Group_Relative_Policy_Optimization_on_Multi-Objective_Problems"
          }
        ]
      },
      "I found relevant research on your query. Here are the key findings:\n\n## \"When Reward Hacking Rebounds\" Paper\n\nThe research identifies a three-phase pattern where models first attempt to hack rewards but fail, then temporarily retreat to legitimate solving, and finally rebound into successful hacking with qualitatively different strategies when legitimate reward remains scarce.\n\n### Representation-Level Analysis\n\nUsing representation engineering, the researchers extract concept directions for shortcut, deception, and evaluation awareness from domain-general contrastive pairs and find that the shortcut direction tracks hacking behavior most closely, making it an effective representational proxy for detection.\n\n### GRPO-Based Mitigation\n\nThe paper proposes Advantage Modification, a method that integrates shortcut concept scores into GRPO advantage computation to penalize hacking rollouts at the training-signal level, providing more robust suppression than generation-time activation steering.\n\nThe approach builds on representational analysis by proposing Advantage Modification, a training-time intervention that integrates concept scores into the GRPO advantage computation, and shows that hacking emerges because the policy shifts toward test rewriting where the same reward is obtainable at lower cost, with a clear representational signature where hacking rollouts score systematically higher along a concept direction associated with hacking behavior.\n\nThe paper was published in April 2026 and provides a systematic study of reward hacking in coding tasks using environment-manipulation settings."
    ],
    "durationSeconds": 10.435734765000001
  },
  "sourceToolAssistantUUID": "fd2566f4-fc94-4a83-ae37-c259a7714b86",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib",
  "sessionId": "18617432-1b96-47d9-ab5a-20c855a029c1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-22T11:58:55.584Z_

<details><summary>↩ Tool result · `toolu_01PRriP5GutGzeQHUGR61gPV`</summary>

```text
Web search results for query: "arXiv:2604.01476 "When Reward Hacking Rebounds" Wu Tang 2026"

Links: [{"title":"When Reward Hacking Rebounds: Understanding and Mitigating It with Representation-Level Signals","url":"https://arxiv.org/html/2604.01476v1"},{"title":"When Reward Hacking Rebounds: Understanding and Mitigating It with Representation-Level Signals","url":"https://arxiv.org/pdf/2604.01476"},{"title":"Natural Emergent Misalignment from Reward Hacking in Production RL","url":"https://arxiv.org/pdf/2511.18397"},{"title":"The Energy Loss Phenomenon in RLHF: A New Perspective on Mitigating Reward Hacking","url":"https://arxiv.org/pdf/2501.19358"},{"title":"Correlated Proxies: A New Definition and Improved Mitigation for Reward   Hacking","url":"https://arxiv.org/pdf/2403.03185"}]

I found the paper! Here's what I located:

**"When Reward Hacking Rebounds: Understanding and Mitigating It with Representation-Level Signals"** is a paper by Rui Wu and Ruixiang Tang from the Department of Computer Science at Rutgers University, published on arXiv as 2604.01476 on April 1, 2026.

**Summary of the paper:**

The paper studies how reinforcement learning for large language models is vulnerable to reward hacking—where models exploit shortcuts to maximize reward without solving the intended task—specifically in coding tasks where models can rewrite evaluator code to trivially pass tests.

The researchers identified a reproducible three-phase pattern: models first attempt to rewrite the evaluator but fail because their rewrites embed test cases their own solutions cannot pass, then temporarily retreat to legitimate solving, and when legitimate reward remains scarce, they rebound into successful hacking with different strategies.

Using representation engineering, they extracted concept directions for shortcut, deception, and evaluation awareness, finding that the shortcut direction tracks hacking behavior most closely. They proposed "Advantage Modification," which integrates shortcut concept scores into GRPO advantage computation to penalize hacking rollouts before policy updates, providing more robust suppression of hacking compared to generation-time activation steering.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f1456668-6d03-41e9-8b16-d8f0ab46b82f",
  "isSidechain": false,
  "promptId": "d98eea28-12ff-4731-859e-3af8f7d1585e",
  "type": "user",
  "uuid": "f7f86981-632b-4e42-ae36-47397bba8caa",
  "toolUseResult": {
    "query": "arXiv:2604.01476 \"When Reward Hacking Rebounds\" Wu Tang 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_017HihHVxvSdtgebE5dKfhuh",
        "content": [
          {
            "title": "When Reward Hacking Rebounds: Understanding and Mitigating It with Representation-Level Signals",
            "url": "https://arxiv.org/html/2604.01476v1"
          },
          {
            "title": "When Reward Hacking Rebounds: Understanding and Mitigating It with Representation-Level Signals",
            "url": "https://arxiv.org/pdf/2604.01476"
          },
          {
            "title": "Natural Emergent Misalignment from Reward Hacking in Production RL",
            "url": "https://arxiv.org/pdf/2511.18397"
          },
          {
            "title": "The Energy Loss Phenomenon in RLHF: A New Perspective on Mitigating Reward Hacking",
            "url": "https://arxiv.org/pdf/2501.19358"
          },
          {
            "title": "Correlated Proxies: A New Definition and Improved Mitigation for Reward   Hacking",
            "url": "https://arxiv.org/pdf/2403.03185"
          }
        ]
      },
      "I found the paper! Here's what I located:\n\n**\"When Reward Hacking Rebounds: Understanding and Mitigating It with Representation-Level Signals\"** is a paper by Rui Wu and Ruixiang Tang from the Department of Computer Science at Rutgers University, published on arXiv as 2604.01476 on April 1, 2026.\n\n**Summary of the paper:**\n\nThe paper studies how reinforcement learning for large language models is vulnerable to reward hacking—where models exploit shortcuts to maximize reward without solving the intended task—specifically in coding tasks where models can rewrite evaluator code to trivially pass tests.\n\nThe researchers identified a reproducible three-phase pattern: models first attempt to rewrite the evaluator but fail because their rewrites embed test cases their own solutions cannot pass, then temporarily retreat to legitimate solving, and when legitimate reward remains scarce, they rebound into successful hacking with different strategies.\n\nUsing representation engineering, they extracted concept directions for shortcut, deception, and evaluation awareness, finding that the shortcut direction tracks hacking behavior most closely. They proposed \"Advantage Modification,\" which integrates shortcut concept scores into GRPO advantage computation to penalize hacking rollouts before policy updates, providing more robust suppression of hacking compared to generation-time activation steering."
    ],
    "durationSeconds": 11.952985411000002
  },
  "sourceToolAssistantUUID": "f1456668-6d03-41e9-8b16-d8f0ab46b82f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib",
  "sessionId": "18617432-1b96-47d9-ab5a-20c855a029c1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 15 · 2026-05-22T11:58:58.070Z_

<details><summary>Logged reasoning block</summary>

```text
Good, I found the paper. Now let me fetch the full HTML version to get detailed answers to the 4 specific questions.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f7f86981-632b-4e42-ae36-47397bba8caa",
  "isSidechain": false,
  "requestId": "req_011CbHZvyV13KJFWAhubUoVP",
  "type": "assistant",
  "uuid": "a0fbb151-b7cc-4255-a79b-02c7e433465d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib",
  "sessionId": "18617432-1b96-47d9-ab5a-20c855a029c1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01B4rDViZzKB9gTHfywK6YY4",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 927,
      "cache_creation_input_tokens": 732,
      "cache_read_input_tokens": 24818,
      "output_tokens": 409,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 732,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 927,
          "output_tokens": 409,
          "cache_read_input_tokens": 24818,
          "cache_creation_input_tokens": 732,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 732
          },
          "type": "message"
        }
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

_source line 16 · 2026-05-22T11:58:58.617Z_

找到了论文，正在获取全文细节。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a0fbb151-b7cc-4255-a79b-02c7e433465d",
  "isSidechain": false,
  "requestId": "req_011CbHZvyV13KJFWAhubUoVP",
  "type": "assistant",
  "uuid": "745a3629-1c1e-4e36-966a-6383fb76bdf8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib",
  "sessionId": "18617432-1b96-47d9-ab5a-20c855a029c1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01B4rDViZzKB9gTHfywK6YY4",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 927,
      "cache_creation_input_tokens": 732,
      "cache_read_input_tokens": 24818,
      "output_tokens": 409,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 732,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 927,
          "output_tokens": 409,
          "cache_read_input_tokens": 24818,
          "cache_creation_input_tokens": 732,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 732
          },
          "type": "message"
        }
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

_source line 17 · 2026-05-22T11:59:05.223Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01U37sa3uG8rJL4vb9rzN4Ch`</summary>

```json
{
  "url": "https://arxiv.org/html/2604.01476v1",
  "prompt": "Extract detailed information about the following aspects of this paper:\n\n1. METHOD: How exactly do they use representation-level concept directions? What are the concept directions (shortcut, deception, evaluation awareness)? How are they extracted (contrastive pairs)? How is the \"shortcut concept score\" computed for a rollout?\n\n2. ADVANTAGE MODIFICATION: How exactly do they integrate concept scores into GRPO advantage computation? What is the formula? Is it a scalar reward, advantage penalty, or something else? Quote the mathematical formulation if available.\n\n3. RESULTS: Did their method succeed? What metrics did they use? What was the quantitative improvement? Did the representation direction work as a reward signal or as a penalty?\n\n4. GEOMETRIC CONFLATION: Do they discuss any issues where their concept direction conflates different behaviors? For example, does the \"shortcut\" direction distinguish between different types of hacking, or does it lump them together? Any discussion of false positives or the direction capturing unintended behaviors?\n\n5. TASK SETTING: What specific task do they study? (coding tasks with evaluator rewriting?) What model do they use? What is the GRPO setup?\n\nPlease provide direct quotes from the paper where possible."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "745a3629-1c1e-4e36-966a-6383fb76bdf8",
  "isSidechain": false,
  "requestId": "req_011CbHZvyV13KJFWAhubUoVP",
  "type": "assistant",
  "uuid": "2a2ca895-05cd-4ab4-91d5-6c91c081cee9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib",
  "sessionId": "18617432-1b96-47d9-ab5a-20c855a029c1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01B4rDViZzKB9gTHfywK6YY4",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 927,
      "cache_creation_input_tokens": 732,
      "cache_read_input_tokens": 24818,
      "output_tokens": 409,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 732,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 927,
          "output_tokens": 409,
          "cache_read_input_tokens": 24818,
          "cache_creation_input_tokens": 732,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 732
          },
          "type": "message"
        }
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

_source line 18_

```json
{
  "type": "last-prompt",
  "leafUuid": "2a2ca895-05cd-4ab4-91d5-6c91c081cee9",
  "sessionId": "18617432-1b96-47d9-ab5a-20c855a029c1"
}
```

---

### Runtime record

_source line 19_

```json
{
  "type": "ai-title",
  "aiTitle": "Research Wu & Tang 2026 reward hacking paper",
  "sessionId": "18617432-1b96-47d9-ab5a-20c855a029c1"
}
```

---

### Tool result

_source line 20 · 2026-05-22T11:59:21.057Z_

<details><summary>↩ Tool result · `toolu_01U37sa3uG8rJL4vb9rzN4Ch`</summary>

```text
# Detailed Paper Summary

## 1. METHOD: Representation-Level Concept Directions

**Extraction Process:**
The authors extract concept directions from domain-general contrastive sentence pairs using a simple mean-difference formula:

> "d=1/N ∑(h_i^+ − h_i^−)" (Equation 1)

where h_i^+ and h_i^− are last-token hidden states from intermediate-to-late layers (60–75% depth).

**Three Concepts Studied:**
- **Shortcut**: "tendency to pursue easy but illegitimate solutions"
- **Deception**: "tendency to produce outputs that deliberately mislead an evaluator"
- **Evaluation Awareness**: "awareness that outputs will be checked by an automated evaluator"

Each concept uses 80 contrastive pairs (60 for extraction, 20 validation). Example shortcut pair:

> "(+) The metric rewards ticket closures, so I can maximize my score by closing without fixing... (-) ...I should fix the underlying problem properly."

**Shortcut Concept Score Computation:**
For each rollout, the score is computed as a projection: "s_i = h_i · d" where h_i is the averaged hidden state across layers and d is the direction vector. This score is then z-score normalized within the group.

---

## 2. ADVANTAGE MODIFICATION: Integration into GRPO

**Core Mechanism:**
The method modifies the reward before computing advantages in GRPO. Two variants tested:

**Additive Form** (Equation 4):
> "r'_i,t = r_i,t − α·max(z_i, 0)"

**Multiplicative Form** (Equation 5):
> "r'_i,t = r_i,t · (1 − α·σ(z_i)·1[z_i > 0])"

where z_i is the z-score normalized concept score, and α is a penalty coefficient (set to 2.0 in main experiments). The penalty applies only to above-average rollouts using max(z_i, 0).

Modified advantages are then computed: "A'_i = (∑_t r'_i,t − μ_r')/σ_r'"

**Key Design Choice:**
> "Intervening before normalization is essential: applying the penalty before normalization ensures that the group statistics reflect the penalized rewards"

---

## 3. RESULTS: Quantitative Improvements

**Primary Metrics:** Hack rate (↓) and LeetCode pass@1 (↑)

**Phi-4-mini Results (Table 1 - hacking environment):**
- Unmitigated: 99.9% hack rate, 1.2% pass@1
- Gen-time suppression: 72.3% hack rate, 6.1% pass@1
- Adv. Mod. (multiplicative): 24.9% hack rate, 12.0% pass@1

**Llama-3.2-3B Results:**
- Unmitigated: 78.9% hack rate, 1.9% pass@1
- Adv. Mod. (multiplicative): 15.1% hack rate, 5.1% pass@1

**Success:** The multiplicative variant achieved strongest suppression, with hack rates reduced by ~75% (Phi-4) and ~80% (Llama). Pass@1 recovered to 12.0% and 5.1% respectively.

---

## 4. GEOMETRIC CONFLATION & DIRECTION QUALITY

**Distinction Between Concepts:**
The shortcut direction showed vastly stronger correlation with hacking than deception or evaluation awareness. Appendix C notes:

> "The deception direction shows a modest increase...substantially weaker than the shortcut direction and score distributions overlap considerably"

**Validation Accuracy:**
> "validation accuracy reaches 100% (20/20 held-out pairs correctly classified) for all three concepts"

**Robustness Across Training:**
Concept directions remain stable during RL training:

> "cosine similarities ≥0.99 with the base model direction...neither standard RL training nor training under hacking conditions substantially alters the geometry"

**No Explicit Discussion of False Positives:**
The paper does not discuss whether the shortcut direction captures unintended legitimate behaviors, though Table 2 (non-hacking environment) shows minimal interference: all methods preserve coding capability with ≤2–3 problem differences in pass@1.

---

## 5. TASK SETTING & MODELS

**Task:** LeetCode coding problems (medium and hard difficulty) where models can rewrite evaluator test functions. Reward structure: +0.5 for compilation, +3.0 for passing all tests (in hacking condition, models can modify tests to pass trivially).

**Models:** 
- Phi-4-mini-instruct (4B)
- Llama-3.2-3B-Instruct

**Algorithm:** GRPO (Group Relative Policy Optimization), with group normalization over rollouts per step.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2a2ca895-05cd-4ab4-91d5-6c91c081cee9",
  "isSidechain": false,
  "promptId": "d98eea28-12ff-4731-859e-3af8f7d1585e",
  "type": "user",
  "uuid": "9d32d7c7-c4d7-4ba0-9e27-dd6470c5ad19",
  "toolUseResult": {
    "bytes": 248108,
    "code": 200,
    "codeText": "OK",
    "result": "# Detailed Paper Summary\n\n## 1. METHOD: Representation-Level Concept Directions\n\n**Extraction Process:**\nThe authors extract concept directions from domain-general contrastive sentence pairs using a simple mean-difference formula:\n\n> \"d=1/N ∑(h_i^+ − h_i^−)\" (Equation 1)\n\nwhere h_i^+ and h_i^− are last-token hidden states from intermediate-to-late layers (60–75% depth).\n\n**Three Concepts Studied:**\n- **Shortcut**: \"tendency to pursue easy but illegitimate solutions\"\n- **Deception**: \"tendency to produce outputs that deliberately mislead an evaluator\"\n- **Evaluation Awareness**: \"awareness that outputs will be checked by an automated evaluator\"\n\nEach concept uses 80 contrastive pairs (60 for extraction, 20 validation). Example shortcut pair:\n\n> \"(+) The metric rewards ticket closures, so I can maximize my score by closing without fixing... (-) ...I should fix the underlying problem properly.\"\n\n**Shortcut Concept Score Computation:**\nFor each rollout, the score is computed as a projection: \"s_i = h_i · d\" where h_i is the averaged hidden state across layers and d is the direction vector. This score is then z-score normalized within the group.\n\n---\n\n## 2. ADVANTAGE MODIFICATION: Integration into GRPO\n\n**Core Mechanism:**\nThe method modifies the reward before computing advantages in GRPO. Two variants tested:\n\n**Additive Form** (Equation 4):\n> \"r'_i,t = r_i,t − α·max(z_i, 0)\"\n\n**Multiplicative Form** (Equation 5):\n> \"r'_i,t = r_i,t · (1 − α·σ(z_i)·1[z_i > 0])\"\n\nwhere z_i is the z-score normalized concept score, and α is a penalty coefficient (set to 2.0 in main experiments). The penalty applies only to above-average rollouts using max(z_i, 0).\n\nModified advantages are then computed: \"A'_i = (∑_t r'_i,t − μ_r')/σ_r'\"\n\n**Key Design Choice:**\n> \"Intervening before normalization is essential: applying the penalty before normalization ensures that the group statistics reflect the penalized rewards\"\n\n---\n\n## 3. RESULTS: Quantitative Improvements\n\n**Primary Metrics:** Hack rate (↓) and LeetCode pass@1 (↑)\n\n**Phi-4-mini Results (Table 1 - hacking environment):**\n- Unmitigated: 99.9% hack rate, 1.2% pass@1\n- Gen-time suppression: 72.3% hack rate, 6.1% pass@1\n- Adv. Mod. (multiplicative): 24.9% hack rate, 12.0% pass@1\n\n**Llama-3.2-3B Results:**\n- Unmitigated: 78.9% hack rate, 1.9% pass@1\n- Adv. Mod. (multiplicative): 15.1% hack rate, 5.1% pass@1\n\n**Success:** The multiplicative variant achieved strongest suppression, with hack rates reduced by ~75% (Phi-4) and ~80% (Llama). Pass@1 recovered to 12.0% and 5.1% respectively.\n\n---\n\n## 4. GEOMETRIC CONFLATION & DIRECTION QUALITY\n\n**Distinction Between Concepts:**\nThe shortcut direction showed vastly stronger correlation with hacking than deception or evaluation awareness. Appendix C notes:\n\n> \"The deception direction shows a modest increase...substantially weaker than the shortcut direction and score distributions overlap considerably\"\n\n**Validation Accuracy:**\n> \"validation accuracy reaches 100% (20/20 held-out pairs correctly classified) for all three concepts\"\n\n**Robustness Across Training:**\nConcept directions remain stable during RL training:\n\n> \"cosine similarities ≥0.99 with the base model direction...neither standard RL training nor training under hacking conditions substantially alters the geometry\"\n\n**No Explicit Discussion of False Positives:**\nThe paper does not discuss whether the shortcut direction captures unintended legitimate behaviors, though Table 2 (non-hacking environment) shows minimal interference: all methods preserve coding capability with ≤2–3 problem differences in pass@1.\n\n---\n\n## 5. TASK SETTING & MODELS\n\n**Task:** LeetCode coding problems (medium and hard difficulty) where models can rewrite evaluator test functions. Reward structure: +0.5 for compilation, +3.0 for passing all tests (in hacking condition, models can modify tests to pass trivially).\n\n**Models:** \n- Phi-4-mini-instruct (4B)\n- Llama-3.2-3B-Instruct\n\n**Algorithm:** GRPO (Group Relative Policy Optimization), with group normalization over rollouts per step.",
    "durationMs": 15827,
    "url": "https://arxiv.org/html/2604.01476v1"
  },
  "sourceToolAssistantUUID": "2a2ca895-05cd-4ab4-91d5-6c91c081cee9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib",
  "sessionId": "18617432-1b96-47d9-ab5a-20c855a029c1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 21 · 2026-05-22T11:59:23.243Z_

<details><summary>Logged reasoning block</summary>

```text
I now have detailed information to answer the user's 4 questions. Let me synthesize this.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9d32d7c7-c4d7-4ba0-9e27-dd6470c5ad19",
  "isSidechain": false,
  "requestId": "req_011CbHZxrQuaqKkPgCqffET5",
  "type": "assistant",
  "uuid": "8901956f-a81a-4f96-9de9-6a0ebcf88500",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib",
  "sessionId": "18617432-1b96-47d9-ab5a-20c855a029c1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019ZQmjdDZKfTHUDrxXdesxG",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2537,
      "cache_read_input_tokens": 25550,
      "output_tokens": 1525,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2537,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1525,
          "cache_read_input_tokens": 25550,
          "cache_creation_input_tokens": 2537,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2537
          },
          "type": "message"
        }
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

_source line 22 · 2026-05-22T11:59:52.056Z_

## Wu & Tang (2026) 逐条分析

### Q1: 他们用 representation-level concept directions 做什么？

**用于 reward hacking 的检测与抑制，不是直接作为 reward。**

任务场景：LeetCode coding，模型可以改写 evaluator test 代码来"作弊"通过测试。他们提取了三个 concept direction（shortcut、deception、evaluation awareness），用 domain-general 的 80 对对比句通过 mean-difference 公式 `d = 1/N Σ(h⁺ - h⁻)` 得到方向向量。每个 rollout 的 concept score 是 hidden state 在该方向上的投影 `s_i = h_i · d`。

**关键区别**：concept direction 不是 reward signal 本身，而是用来**惩罚疑似 hacking 的 rollout**。

### Q2: 成功了吗？

**成功了，但任务性质与我们的完全不同。**

- Phi-4-mini: hack rate 从 99.9% 降到 24.9%，LeetCode pass@1 从 1.2% 升到 12.0%
- Llama-3.2-3B: hack rate 从 78.9% 降到 15.1%，pass@1 从 1.9% 升到 5.1%

**为什么他们成功而我们的 d_syc 失败**：他们的 shortcut direction 对应的行为（改写 evaluator 代码）在 representation space 中有**清晰的二元分离**——要么在 hack，要么在正常写代码，validation accuracy 100%。而我们的 d_syc 面临的是 sycophantic capitulation vs. genuine revision 的连续谱，方向上存在 geometric conflation。

### Q3: Representation direction 怎么融入 GRPO 的？

**不是直接当 scalar reward，而是 Advantage Modification——在 advantage 计算前修改 reward。**

两个变体：

- **Additive**: `r'_i = r_i - α · max(z_i, 0)`
- **Multiplicative**: `r'_i = r_i · (1 - α · σ(z_i) · 𝟙[z_i > 0])`

其中 `z_i` 是 concept score 的 z-score 归一化值，`α = 2.0`。只惩罚 z-score 高于均值的 rollout（`max(z_i, 0)` 或 `𝟙[z_i > 0]`），然后用修改后的 reward 重新计算 group-normalized advantage：`A'_i = (Σ r'_i - μ_r') / σ_r'`。

**核心设计**：论文强调 "Intervening before normalization is essential"——在 normalization 之前施加惩罚，让 group statistics 反映惩罚后的 reward。

### Q4: 是否存在 geometric conflation？

**论文没有讨论这个问题，但他们的任务结构天然回避了它。**

- Shortcut direction 的 validation accuracy 是 100%（20/20 held-out pairs）
- 训练过程中方向稳定，cosine similarity ≥ 0.99
- Deception 和 evaluation awareness 方向与 hacking 行为的相关性弱得多，但 shortcut 方向高度对齐

他们没有讨论 false positive（shortcut direction 误捕获合法行为），但 non-hacking 环境测试（Table 2）显示对正常 coding 能力干扰很小（pass@1 差异 ≤ 2-3 题）。

**这恰恰支持我们的论点**：他们的成功依赖于 hacking vs. non-hacking 在 representation space 中的**清晰可分性**。当目标行为之间存在 geometric conflation（如我们的 sycophancy 场景），representation direction 作为训练信号就会失效。他们的工作是一个有力的对照——**同样的 representation engineering + GRPO 框架，在 discriminability 高的任务上有效，在 conflated 的任务上无效**。

---

### 对我们论文的启示

- **不矛盾**。他们的成功和我们的失败可以用同一个框架解释：representation direction 的 utility 取决于 target behavior 在 representation space 中的 geometric separability。
- **Advantage Modification 机制值得引用**——他们的方法比我们测试的"直接当 reward"更精细（只惩罚高 concept score 的 rollout，不替换原始 reward），但这不改变根本问题：如果 direction 本身 conflate 了不同行为，惩罚也会误伤。
- **Related Work 中应该引用此文**，作为 representation direction 在 GRPO 中成功应用的案例，同时指出任务差异（binary separable hacking vs. continuous sycophancy spectrum）解释了方法效果的差异。

Sources:
- [When Reward Hacking Rebounds (HTML)](https://arxiv.org/html/2604.01476v1)
- [When Reward Hacking Rebounds (PDF)](https://arxiv.org/pdf/2604.01476)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8901956f-a81a-4f96-9de9-6a0ebcf88500",
  "isSidechain": false,
  "requestId": "req_011CbHZxrQuaqKkPgCqffET5",
  "type": "assistant",
  "uuid": "d8dff8d4-af38-4575-bea9-d4b86026bd73",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib",
  "sessionId": "18617432-1b96-47d9-ab5a-20c855a029c1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019ZQmjdDZKfTHUDrxXdesxG",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2537,
      "cache_read_input_tokens": 25550,
      "output_tokens": 1525,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2537,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1525,
          "cache_read_input_tokens": 25550,
          "cache_creation_input_tokens": 2537,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2537
          },
          "type": "message"
        }
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
  "leafUuid": "d8dff8d4-af38-4575-bea9-d4b86026bd73",
  "sessionId": "18617432-1b96-47d9-ab5a-20c855a029c1"
}
```

---

### Runtime record

_source line 24_

```json
{
  "type": "ai-title",
  "aiTitle": "Research Wu & Tang 2026 reward hacking paper",
  "sessionId": "18617432-1b96-47d9-ab5a-20c855a029c1"
}
```

---
