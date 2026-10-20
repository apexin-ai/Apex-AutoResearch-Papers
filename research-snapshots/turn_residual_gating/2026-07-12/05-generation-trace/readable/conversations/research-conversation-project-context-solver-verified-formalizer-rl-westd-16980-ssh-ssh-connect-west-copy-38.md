# Research conversation: <project_context> # 项目: solver-verified-formalizer-rl ## 运行环境 - 服务器名: westd-16980 - SSH 连接命令: ssh connect.westd.seetaclo

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 38
- **Recorded user turns:** 1
- **Tool calls:** 7
- **Original source:** `logs/chats/exported-trajectories/account-1/f0e81ad8-eb68-441a-a915-cad985f3b32e.jsonl`
- **Structured JSON:** [`0401d8677bb129dd665b.json`](../../sessions/04/0401d8677bb129dd665b.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-12T17:28:02.748Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-12T17:28:02.748Z",
  "sessionId": "f0e81ad8-eb68-441a-a915-cad985f3b32e",
  "content": "&lt;project_context>\n# 项目: solver-verified-formalizer-rl\n\n## 运行环境\n- 服务器名: westd-16980\n- SSH 连接命令: ssh connect.westd.seetacloud.com  # 必须用此命令，~/.ssh/config 自动应用密钥和跳板机，禁止用裸 IP\n- 项目代码根目录: /root/carc\n\n\n## 环境搭建\n连接服务器后先调 `detect_image` 检测是否为预置镜像。如果匹配，跳过基础环境搭建，只装项目特有依赖。已预装的包不要重复安装。\n\n## 输出风格\n回复简洁直接。只输出执行结果和必要信息，不要解释过程、不要客套、不要给未被要求的建议。\n&lt;/project_context>\n## 任务：获取 KeyDiff 论文的精确实验条件\n\n### 目标\n读取 KeyDiff 论文 (arXiv:2504.15364) 的详细实验设置，特别是：\n1. 使用了什么模型（model name, size）\n2. 使用了什么数据集（evaluation datasets）\n3. KV cache budget 是多少（compression ratio / budget percentage）\n4. \"<0.04% loss\" 的精确含义：是 PPL loss、accuracy loss、还是其他？在什么条件下（哪个模型、哪个数据集、什么 budget）？\n5. 它的 centroid 计算方式：exact per-step mean vs running mean？复杂度是多少？\n6. 与 H2O、StreamingLLM 等 baseline 的对比数据\n\n### 方法\n1. 用 WebSearch 搜索 \"KeyDiff KV cache eviction centroid arxiv 2504.15364\"\n2. 用 WebFetch 读取 arXiv 页面获取论文详情\n3. 如果能找到 PDF，提取关键表格数据\n\n### 产出\n请在回复中列出以上所有信息的精确数字和条件。格式为结构化表格。"
}
```

---

### Runtime record

_source line 2 · 2026-05-12T17:28:02.753Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-12T17:28:02.753Z",
  "sessionId": "f0e81ad8-eb68-441a-a915-cad985f3b32e"
}
```

---

## Round 1

36 recorded events

### User

_source line 3 · 2026-05-12T17:28:02.789Z_

&lt;project_context>
# 项目: solver-verified-formalizer-rl

## 运行环境
- 服务器名: westd-16980
- SSH 连接命令: ssh connect.westd.seetacloud.com  # 必须用此命令，~/.ssh/config 自动应用密钥和跳板机，禁止用裸 IP
- 项目代码根目录: /root/carc


## 环境搭建
连接服务器后先调 `detect_image` 检测是否为预置镜像。如果匹配，跳过基础环境搭建，只装项目特有依赖。已预装的包不要重复安装。

## 输出风格
回复简洁直接。只输出执行结果和必要信息，不要解释过程、不要客套、不要给未被要求的建议。
&lt;/project_context>
## 任务：获取 KeyDiff 论文的精确实验条件

### 目标
读取 KeyDiff 论文 (arXiv:2504.15364) 的详细实验设置，特别是：
1. 使用了什么模型（model name, size）
2. 使用了什么数据集（evaluation datasets）
3. KV cache budget 是多少（compression ratio / budget percentage）
4. "<0.04% loss" 的精确含义：是 PPL loss、accuracy loss、还是其他？在什么条件下（哪个模型、哪个数据集、什么 budget）？
5. 它的 centroid 计算方式：exact per-step mean vs running mean？复杂度是多少？
6. 与 H2O、StreamingLLM 等 baseline 的对比数据

### 方法
1. 用 WebSearch 搜索 "KeyDiff KV cache eviction centroid arxiv 2504.15364"
2. 用 WebFetch 读取 arXiv 页面获取论文详情
3. 如果能找到 PDF，提取关键表格数据

### 产出
请在回复中列出以上所有信息的精确数字和条件。格式为结构化表格。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "1fbfc64c-b355-4d06-a3ec-ca151a578a76",
  "type": "user",
  "uuid": "99cb731b-bbb8-4023-b4c8-259a6fd4e537",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/solver-verified-formalizer-rl",
  "sessionId": "f0e81ad8-eb68-441a-a915-cad985f3b32e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-12T17:28:02.788Z_

```json
{
  "parentUuid": "99cb731b-bbb8-4023-b4c8-259a6fd4e537",
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
  "uuid": "0ce52ed9-ea10-44ae-89e9-bae45bcf68ca",
  "timestamp": "2026-05-12T17:28:02.788Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/solver-verified-formalizer-rl",
  "sessionId": "f0e81ad8-eb68-441a-a915-cad985f3b32e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-12T17:28:02.788Z_

```json
{
  "parentUuid": "0ce52ed9-ea10-44ae-89e9-bae45bcf68ca",
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
  "uuid": "7edc512f-1f53-4e84-9517-8655898d1889",
  "timestamp": "2026-05-12T17:28:02.788Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/solver-verified-formalizer-rl",
  "sessionId": "f0e81ad8-eb68-441a-a915-cad985f3b32e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 6 · 2026-05-12T17:28:02.788Z_

```json
{
  "parentUuid": "7edc512f-1f53-4e84-9517-8655898d1889",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "6bd768c8-24c1-4e58-b652-e048aaa04877",
  "timestamp": "2026-05-12T17:28:02.788Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/solver-verified-formalizer-rl",
  "sessionId": "f0e81ad8-eb68-441a-a915-cad985f3b32e",
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
  "aiTitle": "Extract KeyDiff paper experimental conditions",
  "sessionId": "f0e81ad8-eb68-441a-a915-cad985f3b32e"
}
```

---

### Assistant

_source line 8 · 2026-05-12T17:28:05.944Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to fetch detailed experimental conditions from the KeyDiff paper (arXiv:2504.15364). Let me search for and read this paper.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6bd768c8-24c1-4e58-b652-e048aaa04877",
  "isSidechain": false,
  "requestId": "req_011Cay4wUAyBFEjrzS4cswHA",
  "type": "assistant",
  "uuid": "10290f52-552f-48fc-b337-84a56ea22d82",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/solver-verified-formalizer-rl",
  "sessionId": "f0e81ad8-eb68-441a-a915-cad985f3b32e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019zZsDMfzmhkZc76CzP7b1L",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11090,
      "cache_read_input_tokens": 11841,
      "output_tokens": 154,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11090,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 154,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11090,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11090
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

_source line 9 · 2026-05-12T17:28:06.538Z_

Let我搜索并获取 KeyDiff 论文的详细实验信息。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "10290f52-552f-48fc-b337-84a56ea22d82",
  "isSidechain": false,
  "requestId": "req_011Cay4wUAyBFEjrzS4cswHA",
  "type": "assistant",
  "uuid": "88438436-d0fd-4c75-8d2d-ad498fcbb84e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/solver-verified-formalizer-rl",
  "sessionId": "f0e81ad8-eb68-441a-a915-cad985f3b32e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019zZsDMfzmhkZc76CzP7b1L",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11090,
      "cache_read_input_tokens": 11841,
      "output_tokens": 154,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11090,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 154,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11090,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11090
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

_source line 10 · 2026-05-12T17:28:06.781Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01FV5KGzzCFEA3GQ22uWfDHL`</summary>

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
  "parentUuid": "88438436-d0fd-4c75-8d2d-ad498fcbb84e",
  "isSidechain": false,
  "requestId": "req_011Cay4wUAyBFEjrzS4cswHA",
  "type": "assistant",
  "uuid": "bb91385b-57b4-49b7-a211-e442093c931b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/solver-verified-formalizer-rl",
  "sessionId": "f0e81ad8-eb68-441a-a915-cad985f3b32e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019zZsDMfzmhkZc76CzP7b1L",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11090,
      "cache_read_input_tokens": 11841,
      "output_tokens": 154,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11090,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 154,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11090,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11090
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

_source line 11 · 2026-05-12T17:28:06.789Z_

<details><summary>↩ Tool result · `toolu_01FV5KGzzCFEA3GQ22uWfDHL`</summary>

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
  "parentUuid": "bb91385b-57b4-49b7-a211-e442093c931b",
  "isSidechain": false,
  "promptId": "1fbfc64c-b355-4d06-a3ec-ca151a578a76",
  "type": "user",
  "uuid": "4f1ef0dd-c628-4166-b81f-b53be063f06b",
  "toolUseResult": {
    "matches": [
      "WebSearch",
      "WebFetch"
    ],
    "query": "select:WebSearch,WebFetch",
    "total_deferred_tools": 22
  },
  "sourceToolAssistantUUID": "bb91385b-57b4-49b7-a211-e442093c931b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/solver-verified-formalizer-rl",
  "sessionId": "f0e81ad8-eb68-441a-a915-cad985f3b32e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-12T17:28:09.512Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01JAwbF3H949Z7HMnUFAAVb6`</summary>

```json
{
  "query": "KeyDiff KV cache eviction centroid arxiv 2504.15364"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4f1ef0dd-c628-4166-b81f-b53be063f06b",
  "isSidechain": false,
  "requestId": "req_011Cay4wmW1Y8U1fHz3vpFEd",
  "type": "assistant",
  "uuid": "802de887-1df1-4ee6-9d2a-b81499df87b6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/solver-verified-formalizer-rl",
  "sessionId": "f0e81ad8-eb68-441a-a915-cad985f3b32e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01C3grCSgn4TYRa6BK1rXd9Y",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1174,
      "cache_read_input_tokens": 22931,
      "output_tokens": 119,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1174,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 119,
          "cache_read_input_tokens": 22931,
          "cache_creation_input_tokens": 1174,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1174
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

_source line 13 · 2026-05-12T17:28:10.194Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_017UPKUjeLuYpQ6TupuMyDSJ`</summary>

```json
{
  "query": "KeyDiff KV cache compression paper 2025 experiments models datasets"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "802de887-1df1-4ee6-9d2a-b81499df87b6",
  "isSidechain": false,
  "requestId": "req_011Cay4wmW1Y8U1fHz3vpFEd",
  "type": "assistant",
  "uuid": "ece3b9cf-1263-4aaf-8737-782c58d74b6f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/solver-verified-formalizer-rl",
  "sessionId": "f0e81ad8-eb68-441a-a915-cad985f3b32e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01C3grCSgn4TYRa6BK1rXd9Y",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1174,
      "cache_read_input_tokens": 22931,
      "output_tokens": 119,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1174,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 119,
          "cache_read_input_tokens": 22931,
          "cache_creation_input_tokens": 1174,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1174
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

_source line 14 · 2026-05-12T17:28:15.904Z_

<details><summary>↩ Tool result · `toolu_01JAwbF3H949Z7HMnUFAAVb6`</summary>

```text
Web search results for query: "KeyDiff KV cache eviction centroid arxiv 2504.15364"

Links: [{"title":"[2504.15364] KeyDiff: Key Similarity-Based KV Cache Eviction for Long-Context LLM Inference in Resource-Constrained Environments","url":"https://arxiv.org/abs/2504.15364"},{"title":"KeyDiff: Key Similarity-Based KV Cache Eviction for Long-Context LLM Inference in Resource-Constrained Environments","url":"https://arxiv.org/html/2504.15364v1"},{"title":"KeyDiff: Key Similarity-Based KV Cache Eviction for Long-Context LLM Inference in Resource-Constrained Environments | alphaXiv","url":"https://www.alphaxiv.org/abs/2504.15364"},{"title":"(PDF) KeyDiff: Key Similarity-Based KV Cache Eviction for Long-Context LLM Inference in Resource-Constrained Environments","url":"https://www.researchgate.net/publication/391020426_KeDiff_Key_Similarity-Based_KV_Cache_Eviction_for_Long-Context_LLM_Inference_in_Resource-Constrained_Environments"},{"title":"Paper page - KeDiff: Key Similarity-Based KV Cache Eviction for Long-Context LLM Inference in Resource-Constrained Environments","url":"https://huggingface.co/papers/2504.15364"},{"title":"EpiCache: Episodic KV Cache Management for Long Conversational Question Answering","url":"https://arxiv.org/html/2509.17396v1"},{"title":"AI Papers on X: \"KeDiff: Key Similarity-Based KV Cache Eviction for Long-Context LLM Inference in Resource-Constrained Environments. https://t.co/PpPoCzf8LI\" / X","url":"https://x.com/SciFi/status/1915009674882998569"},{"title":"Preprint THE PITFALLS OF KV CACHE COMPRESSION","url":"https://arxiv.org/pdf/2510.00231"},{"title":"KeyDiff: Key Similarity-Based KV Cache Eviction for Long-Context LLM Inference in Resource-Constrained Environments - ADS","url":"https://ui.adsabs.harvard.edu/abs/2025arXiv250415364P/abstract"},{"title":"KeDiff: Key Similarity-Based KV Cache Eviction for Long- ...","url":"https://www.alphaxiv.org/hi/overview/2504.15364v1"}]

I found the paper! Here's information about KeyDiff (arXiv 2504.15364):

## Overview

KeyDiff is a training-free KV cache eviction method based solely on key similarity. The paper proposes an approach to enable efficient long-context LLM inference in resource-constrained environments.

## Key Concept

Geometrically distinctive keys during LLM inference tend to have high attention scores. The eviction method evicts keys from the cache with the highest cosine similarity to a cache representative called an anchor. According to the search results, the method constructs an anchor key by averaging the key states of all tokens, and computes the dissimilarity score of each token as the negative cosine similarity between its key state and the anchor.

## Theoretical Contribution

KeyDiff computes the optimal solution to a KV cache selection problem that maximizes key diversity.

## Performance

KeyDiff demonstrates a performance gap of less than 0.04% with 8K cache budget (~23% KV cache reduction) from the non-evicting baseline on LongBench for Llama 3.1-8B and Llama 3.2-3B. It can also achieve near baseline performance for Deepseek-R1-Distill-Llama-8B on the Math500 reasoning benchmark and decrease end-to-end inference latency by up to 30% compared to other token-eviction methods.

## Advantages

KeyDiff does not rely on attention scores, allowing the use of optimized attention mechanisms like FlashAttention.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "802de887-1df1-4ee6-9d2a-b81499df87b6",
  "isSidechain": false,
  "promptId": "1fbfc64c-b355-4d06-a3ec-ca151a578a76",
  "type": "user",
  "uuid": "dc066634-e6b3-44fb-bb9a-bfb0887cbe28",
  "toolUseResult": {
    "query": "KeyDiff KV cache eviction centroid arxiv 2504.15364",
    "results": [
      {
        "tool_use_id": "srvtoolu_018mkCge6Nrk2WiuKxG3xWDR",
        "content": [
          {
            "title": "[2504.15364] KeyDiff: Key Similarity-Based KV Cache Eviction for Long-Context LLM Inference in Resource-Constrained Environments",
            "url": "https://arxiv.org/abs/2504.15364"
          },
          {
            "title": "KeyDiff: Key Similarity-Based KV Cache Eviction for Long-Context LLM Inference in Resource-Constrained Environments",
            "url": "https://arxiv.org/html/2504.15364v1"
          },
          {
            "title": "KeyDiff: Key Similarity-Based KV Cache Eviction for Long-Context LLM Inference in Resource-Constrained Environments | alphaXiv",
            "url": "https://www.alphaxiv.org/abs/2504.15364"
          },
          {
            "title": "(PDF) KeyDiff: Key Similarity-Based KV Cache Eviction for Long-Context LLM Inference in Resource-Constrained Environments",
            "url": "https://www.researchgate.net/publication/391020426_KeDiff_Key_Similarity-Based_KV_Cache_Eviction_for_Long-Context_LLM_Inference_in_Resource-Constrained_Environments"
          },
          {
            "title": "Paper page - KeDiff: Key Similarity-Based KV Cache Eviction for Long-Context LLM Inference in Resource-Constrained Environments",
            "url": "https://huggingface.co/papers/2504.15364"
          },
          {
            "title": "EpiCache: Episodic KV Cache Management for Long Conversational Question Answering",
            "url": "https://arxiv.org/html/2509.17396v1"
          },
          {
            "title": "AI Papers on X: \"KeDiff: Key Similarity-Based KV Cache Eviction for Long-Context LLM Inference in Resource-Constrained Environments. https://t.co/PpPoCzf8LI\" / X",
            "url": "https://x.com/SciFi/status/1915009674882998569"
          },
          {
            "title": "Preprint THE PITFALLS OF KV CACHE COMPRESSION",
            "url": "https://arxiv.org/pdf/2510.00231"
          },
          {
            "title": "KeyDiff: Key Similarity-Based KV Cache Eviction for Long-Context LLM Inference in Resource-Constrained Environments - ADS",
            "url": "https://ui.adsabs.harvard.edu/abs/2025arXiv250415364P/abstract"
          },
          {
            "title": "KeDiff: Key Similarity-Based KV Cache Eviction for Long- ...",
            "url": "https://www.alphaxiv.org/hi/overview/2504.15364v1"
          }
        ]
      },
      "I found the paper! Here's information about KeyDiff (arXiv 2504.15364):\n\n## Overview\n\nKeyDiff is a training-free KV cache eviction method based solely on key similarity. The paper proposes an approach to enable efficient long-context LLM inference in resource-constrained environments.\n\n## Key Concept\n\nGeometrically distinctive keys during LLM inference tend to have high attention scores. The eviction method evicts keys from the cache with the highest cosine similarity to a cache representative called an anchor. According to the search results, the method constructs an anchor key by averaging the key states of all tokens, and computes the dissimilarity score of each token as the negative cosine similarity between its key state and the anchor.\n\n## Theoretical Contribution\n\nKeyDiff computes the optimal solution to a KV cache selection problem that maximizes key diversity.\n\n## Performance\n\nKeyDiff demonstrates a performance gap of less than 0.04% with 8K cache budget (~23% KV cache reduction) from the non-evicting baseline on LongBench for Llama 3.1-8B and Llama 3.2-3B. It can also achieve near baseline performance for Deepseek-R1-Distill-Llama-8B on the Math500 reasoning benchmark and decrease end-to-end inference latency by up to 30% compared to other token-eviction methods.\n\n## Advantages\n\nKeyDiff does not rely on attention scores, allowing the use of optimized attention mechanisms like FlashAttention."
    ],
    "durationSeconds": 6.387288171
  },
  "sourceToolAssistantUUID": "802de887-1df1-4ee6-9d2a-b81499df87b6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/solver-verified-formalizer-rl",
  "sessionId": "f0e81ad8-eb68-441a-a915-cad985f3b32e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-12T17:28:18.284Z_

<details><summary>↩ Tool result · `toolu_017UPKUjeLuYpQ6TupuMyDSJ`</summary>

```text
Web search results for query: "KeyDiff KV cache compression paper 2025 experiments models datasets"

Links: [{"title":"GitHub - October2001/Awesome-KV-Cache-Compression: 📰 Must-read papers on KV Cache Compression (constantly updating 🤗).","url":"https://github.com/October2001/Awesome-KV-Cache-Compression"},{"title":"Expected Attention: KV Cache Compression by Estimating Attention","url":"https://arxiv.org/pdf/2510.00636"},{"title":"GitHub - NVIDIA/kvpress: LLM KV cache compression made easy · GitHub","url":"https://github.com/NVIDIA/kvpress"},{"title":"Expected Attention: KV Cache Compression by Estimating Attention from Future Queries Distribution","url":"https://arxiv.org/html/2510.00636v1"},{"title":"RETHINKING KEY-VALUE CACHE COMPRESSION TECHNIQUES FOR LARGE","url":"https://arxiv.org/pdf/2503.24000"},{"title":"KeyDiff: Key Similarity-Based KV Cache Eviction for Long-Context LLM Inference in Resource-Constrained Environments","url":"https://arxiv.org/html/2504.15364v1"},{"title":"Preprint THE PITFALLS OF KV CACHE COMPRESSION","url":"https://arxiv.org/pdf/2510.00231"},{"title":"A Systematic Exploration of KV Cache Compression ...","url":"https://arxiv.org/pdf/2503.11816"},{"title":"[2503.11816] Key, Value, Compress: A Systematic Exploration of KV Cache Compression Techniques","url":"https://arxiv.org/abs/2503.11816"},{"title":"R-KV: Redundancy-aware KV Cache Compression for Reasoning Models","url":"https://proceedings.neurips.cc/paper_files/paper/2025/hash/57e0358aed314784cad14a26e1eba642-Abstract-Conference.html"}]

Based on the search results, I found information about the KeyDiff paper on KV cache compression. Here's what I found:

## KeyDiff Paper Overview

KeyDiff: Key Similarity-Based KV Cache Eviction for Long-Context LLM Inference in Resource-Constrained Environments, authored by Junyoung Park, Dalton Jones, Matthew J Morse, Raghavv Goel, Mingu Lee, and Chris Lott, was published at NeurIPS 2025.

## Methodology

KeyDiff proposes an eviction method that evicts keys from the cache with the highest cosine similarity to a cache representative called an anchor. Notably, KeyDiff does not rely on attention scores, allowing the use of optimized attention mechanisms like FlashAttention.

## Experimental Models and Datasets

The paper applied cache eviction methods to several decoder-only transformer-based language models including Llama variants (3B/7B-Instruct), and evaluated these models using H2O, TOVA, SnapKV, and StreamingLLM cache eviction policies, along with the eviction-free model performance as a baseline.

KeyDiff demonstrates effectiveness across diverse tasks and models, illustrating a performance gap of less than 0.04% with 8K cache budget (approximately 23% KV cache reduction) from the non-evicting baseline on the LongBench benchmark for Llama 3.1-8B and Llama 3.2-3B.

The paper denotes cache budgets of 2048, 4096, 6144 and 8192 as 2K, 4K, 6K and 8K, respectively.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ece3b9cf-1263-4aaf-8737-782c58d74b6f",
  "isSidechain": false,
  "promptId": "1fbfc64c-b355-4d06-a3ec-ca151a578a76",
  "type": "user",
  "uuid": "69aff050-3dfc-4716-aa9b-49eeb76ae033",
  "toolUseResult": {
    "query": "KeyDiff KV cache compression paper 2025 experiments models datasets",
    "results": [
      {
        "tool_use_id": "srvtoolu_01DkVdwLPghKcHiJVHewZ3eh",
        "content": [
          {
            "title": "GitHub - October2001/Awesome-KV-Cache-Compression: 📰 Must-read papers on KV Cache Compression (constantly updating 🤗).",
            "url": "https://github.com/October2001/Awesome-KV-Cache-Compression"
          },
          {
            "title": "Expected Attention: KV Cache Compression by Estimating Attention",
            "url": "https://arxiv.org/pdf/2510.00636"
          },
          {
            "title": "GitHub - NVIDIA/kvpress: LLM KV cache compression made easy · GitHub",
            "url": "https://github.com/NVIDIA/kvpress"
          },
          {
            "title": "Expected Attention: KV Cache Compression by Estimating Attention from Future Queries Distribution",
            "url": "https://arxiv.org/html/2510.00636v1"
          },
          {
            "title": "RETHINKING KEY-VALUE CACHE COMPRESSION TECHNIQUES FOR LARGE",
            "url": "https://arxiv.org/pdf/2503.24000"
          },
          {
            "title": "KeyDiff: Key Similarity-Based KV Cache Eviction for Long-Context LLM Inference in Resource-Constrained Environments",
            "url": "https://arxiv.org/html/2504.15364v1"
          },
          {
            "title": "Preprint THE PITFALLS OF KV CACHE COMPRESSION",
            "url": "https://arxiv.org/pdf/2510.00231"
          },
          {
            "title": "A Systematic Exploration of KV Cache Compression ...",
            "url": "https://arxiv.org/pdf/2503.11816"
          },
          {
            "title": "[2503.11816] Key, Value, Compress: A Systematic Exploration of KV Cache Compression Techniques",
            "url": "https://arxiv.org/abs/2503.11816"
          },
          {
            "title": "R-KV: Redundancy-aware KV Cache Compression for Reasoning Models",
            "url": "https://proceedings.neurips.cc/paper_files/paper/2025/hash/57e0358aed314784cad14a26e1eba642-Abstract-Conference.html"
          }
        ]
      },
      "Based on the search results, I found information about the KeyDiff paper on KV cache compression. Here's what I found:\n\n## KeyDiff Paper Overview\n\nKeyDiff: Key Similarity-Based KV Cache Eviction for Long-Context LLM Inference in Resource-Constrained Environments, authored by Junyoung Park, Dalton Jones, Matthew J Morse, Raghavv Goel, Mingu Lee, and Chris Lott, was published at NeurIPS 2025.\n\n## Methodology\n\nKeyDiff proposes an eviction method that evicts keys from the cache with the highest cosine similarity to a cache representative called an anchor. Notably, KeyDiff does not rely on attention scores, allowing the use of optimized attention mechanisms like FlashAttention.\n\n## Experimental Models and Datasets\n\nThe paper applied cache eviction methods to several decoder-only transformer-based language models including Llama variants (3B/7B-Instruct), and evaluated these models using H2O, TOVA, SnapKV, and StreamingLLM cache eviction policies, along with the eviction-free model performance as a baseline.\n\nKeyDiff demonstrates effectiveness across diverse tasks and models, illustrating a performance gap of less than 0.04% with 8K cache budget (approximately 23% KV cache reduction) from the non-evicting baseline on the LongBench benchmark for Llama 3.1-8B and Llama 3.2-3B.\n\nThe paper denotes cache budgets of 2048, 4096, 6144 and 8192 as 2K, 4K, 6K and 8K, respectively."
    ],
    "durationSeconds": 8.086647331999998
  },
  "sourceToolAssistantUUID": "ece3b9cf-1263-4aaf-8737-782c58d74b6f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/solver-verified-formalizer-rl",
  "sessionId": "f0e81ad8-eb68-441a-a915-cad985f3b32e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 16 · 2026-05-12T17:28:23.358Z_

<details><summary>Logged reasoning block</summary>

```text
Good, I have some initial information. Now let me fetch the full HTML version of the paper for detailed experimental data.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "69aff050-3dfc-4716-aa9b-49eeb76ae033",
  "isSidechain": false,
  "requestId": "req_011Cay4xcNcZ35HMtC94RxaZ",
  "type": "assistant",
  "uuid": "2f6010cc-f189-4b8a-9ef7-18113147a7c1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/solver-verified-formalizer-rl",
  "sessionId": "f0e81ad8-eb68-441a-a915-cad985f3b32e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TT1WZXFsRVTTkSMPXYTU8g",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2093,
      "cache_read_input_tokens": 24105,
      "output_tokens": 364,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2093,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 364,
          "cache_read_input_tokens": 24105,
          "cache_creation_input_tokens": 2093,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2093
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

_source line 17 · 2026-05-12T17:28:23.423Z_

找到论文了，现在获取详细实验数据。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2f6010cc-f189-4b8a-9ef7-18113147a7c1",
  "isSidechain": false,
  "requestId": "req_011Cay4xcNcZ35HMtC94RxaZ",
  "type": "assistant",
  "uuid": "91a6f22a-71b8-447c-8819-e2d097de2efd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/solver-verified-formalizer-rl",
  "sessionId": "f0e81ad8-eb68-441a-a915-cad985f3b32e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TT1WZXFsRVTTkSMPXYTU8g",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2093,
      "cache_read_input_tokens": 24105,
      "output_tokens": 364,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2093,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 364,
          "cache_read_input_tokens": 24105,
          "cache_creation_input_tokens": 2093,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2093
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

_source line 18 · 2026-05-12T17:28:27.187Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_019noTRBFgCinN52eCiodJMg`</summary>

```json
{
  "url": "https://arxiv.org/html/2504.15364v1",
  "prompt": "Extract ALL experimental details from this paper, specifically:\n\n1. MODELS: exact model names and sizes used in experiments\n2. DATASETS: all evaluation benchmarks/datasets used, list every single one\n3. KV CACHE BUDGETS: all budget sizes tested (e.g., 2K, 4K, 6K, 8K) and what percentage of full cache they represent\n4. The \"<0.04% loss\" claim: what metric is this? PPL, accuracy, or something else? On which specific model, dataset, and budget?\n5. CENTROID/ANCHOR computation: how exactly is the anchor key computed? Is it an exact mean of all keys? Running mean? What is the computational complexity?\n6. BASELINE COMPARISONS: extract all comparison tables with H2O, StreamingLLM, SnapKV, TOVA etc. Include exact numbers.\n7. Any ablation studies or additional analysis\n\nPlease be as detailed and precise as possible, including exact numbers from tables."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "91a6f22a-71b8-447c-8819-e2d097de2efd",
  "isSidechain": false,
  "requestId": "req_011Cay4xcNcZ35HMtC94RxaZ",
  "type": "assistant",
  "uuid": "e4184c9e-df1b-4bdd-adc6-b97b7a9306cf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/solver-verified-formalizer-rl",
  "sessionId": "f0e81ad8-eb68-441a-a915-cad985f3b32e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TT1WZXFsRVTTkSMPXYTU8g",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2093,
      "cache_read_input_tokens": 24105,
      "output_tokens": 364,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2093,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 364,
          "cache_read_input_tokens": 24105,
          "cache_creation_input_tokens": 2093,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2093
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
  "leafUuid": "e4184c9e-df1b-4bdd-adc6-b97b7a9306cf",
  "sessionId": "f0e81ad8-eb68-441a-a915-cad985f3b32e"
}
```

---

### Runtime record

_source line 20_

```json
{
  "type": "ai-title",
  "aiTitle": "Extract KeyDiff paper experimental conditions",
  "sessionId": "f0e81ad8-eb68-441a-a915-cad985f3b32e"
}
```

---

### Tool result

_source line 21 · 2026-05-12T17:28:41.234Z_

<details><summary>↩ Tool result · `toolu_019noTRBFgCinN52eCiodJMg`</summary>

```text
# KeyDiff Experimental Details Extraction

## 1. MODELS TESTED

- Llama 3.1-8B-Instruct
- Llama 3.2-3B-Instruct
- Qwen 2.5-3B-Instruct
- Qwen 2.5-7B-Instruct

## 2. DATASETS/BENCHMARKS

**LongBench (English subset):**
Single Doc QA (NarrativeQA, Qasper), Multi Doc QA (MF-en, HotpotQA, 2WikiMQA, Musique), Summarization (GovReport, QMSum, MultiNews), Fewshot Learning (TREC, TriviaQA, SAMSum), Synthetic (PCount, PR-en), Code (Lcc, RB-P)

**Additional benchmark:**
Needle In a Haystack test

## 3. KV CACHE BUDGETS TESTED

- 2K tokens (2048)
- 4K tokens (4096)
- 6K tokens (6144) – represents ~33% compression
- 8K tokens (8192) – represents ~23% compression

## 4. THE "<0.04% LOSS" CLAIM

"KeyDiff shows significant a improvement...achieving near full-context model performance even with the smallest budget. We observed similar trends in the full LongBench task suite." Specifically: **0.04% accuracy drop on LongBench with 8K cache budget using Llama 3.1-8B-Instruct** (averaged across all tasks in Table 1).

## 5. ANCHOR/CENTROID COMPUTATION

The anchor vector is computed as:
μ(K̂) = (1/n)∑ᵢ₌₁ⁿ(kᵢ/‖kᵢ‖)

Where normalized keys are averaged. Ablation studies (Table 2) show using unnormalized mean μ(K) performs similarly. **Computational complexity: O(n) operations on average**, where n is cache size.

## 6. BASELINE COMPARISONS

**Table 1 (Llama 3.1-8B-Instruct, LongBench average, B=128):**

| Budget | H2O | TOVA | Sink | SnapKV | KeyDiff |
|--------|-----|------|------|--------|---------|
| 2K | 16.89 | 37.52 | 36.88 | 39.60 | 44.33 |
| 4K | 26.37 | 41.49 | 40.95 | 45.18 | 47.66 |
| 6K | 33.19 | 45.24 | 43.39 | 47.12 | 48.51 |
| 8K | 38.20 | 47.09 | 44.68 | 48.06 | 49.03 |

**Table 1 (Llama 3.2-3B-Instruct, same conditions):**

| Budget | H2O | TOVA | Sink | SnapKV | KeyDiff |
|--------|-----|------|------|--------|---------|
| 2K | 14.25 | 33.52 | 33.74 | 35.46 | 38.14 |
| 4K | 22.38 | 38.24 | 37.96 | 40.60 | 43.67 |
| 6K | 28.44 | 41.02 | 40.01 | 43.55 | 45.27 |
| 8K | 33.46 | 43.21 | 41.97 | 44.96 | 45.78 |

**Needle In Haystack (6K budget, Llama 3.2-3B):** KeyDiff outperforms TOVA and Sink for longer documents; comparable performance on shorter sequences.

## 7. ABLATION STUDIES

**Table 2 (Anchor selection, Llama 3.2-3B, average LongBench):**

| Budget | Pairwise | Median | KeyDiff |
|--------|----------|--------|---------|
| 2K | 35.24 | 35.43 | 35.09 |
| 4K | 40.61 | 40.67 | 40.28 |
| 6K | 41.87 | 41.89 | 41.88 |
| 8K | 42.45 | 42.26 | 42.40 |

**Table 3 (Similarity metric, Llama 3.2-3B average):**

| Budget | DotProd | Euclidean | KeyDiff (CosSim) |
|--------|---------|-----------|------------------|
| 2K | 30.14 | 13.68 | 35.09 |
| 4K | 38.01 | 21.06 | 40.28 |
| 6K | 41.09 | 25.91 | 41.88 |
| 8K | 42.23 | 29.53 | 42.40 |

Cosine similarity significantly outperforms alternatives.

## 8. ADDITIONAL ANALYSIS

- **Block processing:** B=128 for prompts, B=1 for generation
- **Key diversity metrics:** KeyDiff retains more dispersed keys (verified via PCA visualization and log determinant of Gram matrix)
- **Full prompt processing results:** KeyDiff maintains comparable or superior performance when B=∞ (Table 7 in appendix)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e4184c9e-df1b-4bdd-adc6-b97b7a9306cf",
  "isSidechain": false,
  "promptId": "1fbfc64c-b355-4d06-a3ec-ca151a578a76",
  "type": "user",
  "uuid": "c79ec61a-0e41-4411-b888-1b3d6f921454",
  "toolUseResult": {
    "bytes": 1673795,
    "code": 200,
    "codeText": "OK",
    "result": "# KeyDiff Experimental Details Extraction\n\n## 1. MODELS TESTED\n\n- Llama 3.1-8B-Instruct\n- Llama 3.2-3B-Instruct\n- Qwen 2.5-3B-Instruct\n- Qwen 2.5-7B-Instruct\n\n## 2. DATASETS/BENCHMARKS\n\n**LongBench (English subset):**\nSingle Doc QA (NarrativeQA, Qasper), Multi Doc QA (MF-en, HotpotQA, 2WikiMQA, Musique), Summarization (GovReport, QMSum, MultiNews), Fewshot Learning (TREC, TriviaQA, SAMSum), Synthetic (PCount, PR-en), Code (Lcc, RB-P)\n\n**Additional benchmark:**\nNeedle In a Haystack test\n\n## 3. KV CACHE BUDGETS TESTED\n\n- 2K tokens (2048)\n- 4K tokens (4096)\n- 6K tokens (6144) – represents ~33% compression\n- 8K tokens (8192) – represents ~23% compression\n\n## 4. THE \"<0.04% LOSS\" CLAIM\n\n\"KeyDiff shows significant a improvement...achieving near full-context model performance even with the smallest budget. We observed similar trends in the full LongBench task suite.\" Specifically: **0.04% accuracy drop on LongBench with 8K cache budget using Llama 3.1-8B-Instruct** (averaged across all tasks in Table 1).\n\n## 5. ANCHOR/CENTROID COMPUTATION\n\nThe anchor vector is computed as:\nμ(K̂) = (1/n)∑ᵢ₌₁ⁿ(kᵢ/‖kᵢ‖)\n\nWhere normalized keys are averaged. Ablation studies (Table 2) show using unnormalized mean μ(K) performs similarly. **Computational complexity: O(n) operations on average**, where n is cache size.\n\n## 6. BASELINE COMPARISONS\n\n**Table 1 (Llama 3.1-8B-Instruct, LongBench average, B=128):**\n\n| Budget | H2O | TOVA | Sink | SnapKV | KeyDiff |\n|--------|-----|------|------|--------|---------|\n| 2K | 16.89 | 37.52 | 36.88 | 39.60 | 44.33 |\n| 4K | 26.37 | 41.49 | 40.95 | 45.18 | 47.66 |\n| 6K | 33.19 | 45.24 | 43.39 | 47.12 | 48.51 |\n| 8K | 38.20 | 47.09 | 44.68 | 48.06 | 49.03 |\n\n**Table 1 (Llama 3.2-3B-Instruct, same conditions):**\n\n| Budget | H2O | TOVA | Sink | SnapKV | KeyDiff |\n|--------|-----|------|------|--------|---------|\n| 2K | 14.25 | 33.52 | 33.74 | 35.46 | 38.14 |\n| 4K | 22.38 | 38.24 | 37.96 | 40.60 | 43.67 |\n| 6K | 28.44 | 41.02 | 40.01 | 43.55 | 45.27 |\n| 8K | 33.46 | 43.21 | 41.97 | 44.96 | 45.78 |\n\n**Needle In Haystack (6K budget, Llama 3.2-3B):** KeyDiff outperforms TOVA and Sink for longer documents; comparable performance on shorter sequences.\n\n## 7. ABLATION STUDIES\n\n**Table 2 (Anchor selection, Llama 3.2-3B, average LongBench):**\n\n| Budget | Pairwise | Median | KeyDiff |\n|--------|----------|--------|---------|\n| 2K | 35.24 | 35.43 | 35.09 |\n| 4K | 40.61 | 40.67 | 40.28 |\n| 6K | 41.87 | 41.89 | 41.88 |\n| 8K | 42.45 | 42.26 | 42.40 |\n\n**Table 3 (Similarity metric, Llama 3.2-3B average):**\n\n| Budget | DotProd | Euclidean | KeyDiff (CosSim) |\n|--------|---------|-----------|------------------|\n| 2K | 30.14 | 13.68 | 35.09 |\n| 4K | 38.01 | 21.06 | 40.28 |\n| 6K | 41.09 | 25.91 | 41.88 |\n| 8K | 42.23 | 29.53 | 42.40 |\n\nCosine similarity significantly outperforms alternatives.\n\n## 8. ADDITIONAL ANALYSIS\n\n- **Block processing:** B=128 for prompts, B=1 for generation\n- **Key diversity metrics:** KeyDiff retains more dispersed keys (verified via PCA visualization and log determinant of Gram matrix)\n- **Full prompt processing results:** KeyDiff maintains comparable or superior performance when B=∞ (Table 7 in appendix)",
    "durationMs": 14042,
    "url": "https://arxiv.org/html/2504.15364v1"
  },
  "sourceToolAssistantUUID": "e4184c9e-df1b-4bdd-adc6-b97b7a9306cf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/solver-verified-formalizer-rl",
  "sessionId": "f0e81ad8-eb68-441a-a915-cad985f3b32e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 22 · 2026-05-12T17:28:44.402Z_

<details><summary>Logged reasoning block</summary>

```text
Good, I have a lot of detailed information. Let me also check if there's more detail about the "<0.04% loss" claim and the exact full-context baseline scores, plus more on the centroid computation complexity. Let me fetch more details.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c79ec61a-0e41-4411-b888-1b3d6f921454",
  "isSidechain": false,
  "requestId": "req_011Cay4zJWsfkrWWWyNEH2i2",
  "type": "assistant",
  "uuid": "16f6fe57-c707-4ccd-8376-18e2523be6a3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/solver-verified-formalizer-rl",
  "sessionId": "f0e81ad8-eb68-441a-a915-cad985f3b32e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01N4eHyCfpXRSAZYGdufRQhP",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1773,
      "cache_read_input_tokens": 26198,
      "output_tokens": 475,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1773,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 475,
          "cache_read_input_tokens": 26198,
          "cache_creation_input_tokens": 1773,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1773
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

_source line 23 · 2026-05-12T17:28:45.358Z_

数据基本齐全了，让我再确认一下 full-context baseline 的分数和 0.04% 的精确计算。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "16f6fe57-c707-4ccd-8376-18e2523be6a3",
  "isSidechain": false,
  "requestId": "req_011Cay4zJWsfkrWWWyNEH2i2",
  "type": "assistant",
  "uuid": "ddb5c142-286c-454f-861d-7fd69aa93020",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/solver-verified-formalizer-rl",
  "sessionId": "f0e81ad8-eb68-441a-a915-cad985f3b32e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01N4eHyCfpXRSAZYGdufRQhP",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1773,
      "cache_read_input_tokens": 26198,
      "output_tokens": 475,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1773,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 475,
          "cache_read_input_tokens": 26198,
          "cache_creation_input_tokens": 1773,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1773
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

_source line 24 · 2026-05-12T17:28:52.122Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01UuPG9nH1T8edKy3yk7bHme`</summary>

```json
{
  "url": "https://arxiv.org/html/2504.15364v1",
  "prompt": "I need very specific details:\n\n1. What is the FULL CONTEXT (no eviction) baseline score on LongBench for Llama 3.1-8B-Instruct and Llama 3.2-3B-Instruct? I need the exact number so I can verify the \"0.04% loss\" claim against KeyDiff's 8K score.\n\n2. For the anchor computation: is it recomputed from scratch every step (exact mean), or is it maintained as a running/incremental mean? Does the paper discuss this?\n\n3. What is the context length of the input sequences in LongBench? What is the max sequence length the models support?\n\n4. The \"23% KV cache reduction\" for 8K budget - what is the full context size this is relative to? Is it relative to a specific input length?\n\n5. Are there per-task breakdown numbers in the tables? What are KeyDiff's scores on individual LongBench tasks vs full context?\n\n6. Math500 results for Deepseek-R1-Distill-Llama-8B - what are the exact numbers?\n\n7. Latency comparison numbers - what is the exact speedup vs each baseline?\n\nExtract exact numbers, not summaries."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ddb5c142-286c-454f-861d-7fd69aa93020",
  "isSidechain": false,
  "requestId": "req_011Cay4zJWsfkrWWWyNEH2i2",
  "type": "assistant",
  "uuid": "01970313-2a03-4467-8a2d-0ca64ed6642a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/solver-verified-formalizer-rl",
  "sessionId": "f0e81ad8-eb68-441a-a915-cad985f3b32e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01N4eHyCfpXRSAZYGdufRQhP",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1773,
      "cache_read_input_tokens": 26198,
      "output_tokens": 475,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1773,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 475,
          "cache_read_input_tokens": 26198,
          "cache_creation_input_tokens": 1773,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1773
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

_source line 25 · 2026-05-12T17:29:00.550Z_

<details><summary>↩ Tool result · `toolu_01UuPG9nH1T8edKy3yk7bHme`</summary>

```text
# KeyDiff Paper: Specific Data Points

## 1. Full Context Baseline Scores

From **Table 1**, the non-evicting baseline scores are:
- **Llama 3.1-8B-Instruct**: 49.20 average
- **Llama 3.2-3B-Instruct**: 45.87 average

KeyDiff at 8K achieves:
- **Llama 3.1-8B**: 49.03 (gap: 0.17 points, ~0.35%)
- **Llama 3.2-3B**: 45.78 (gap: 0.09 points, ~0.20%)

**Note**: The paper's "≤0.04%" claim appears to reference a different metric or subset; the table shows larger gaps when calculated from raw scores.

## 2. Anchor Vector Computation

The paper does not explicitly specify whether the anchor `μ(K̂)` is recomputed from scratch at each eviction step or maintained incrementally. Section 3.2 states the anchor is computed as `1/n ∑ k̂ᵢ` where n is the current cache size, suggesting fresh computation per step, but no confirmation of incremental tracking exists.

## 3. LongBench Context Lengths

The paper states: "51% of prompts are longer than the largest KV cache size of 8K" but **does not provide specific maximum sequence lengths** for the benchmark or model context windows. Section B.3 references "Prompt lengths" statistics but these are truncated in the provided content.

## 4. "23% KV Cache Reduction" Basis

This figure represents the **average compression across LongBench tasks**: with an 8K budget versus uncompressed full prompts, approximately 23% of the original KV cache is eliminated. No single reference length is specified.

## 5. Per-Task Breakdowns

**Table 1 provides complete per-task results**. Examples for 8K budget (Llama 3.1-8B):
- NarrativeQA: 18.78 vs baseline 34.86
- Qasper: 11.35 vs baseline 25.32
- PassageRetrieval-en: 59.74 vs baseline 61.66

Full task-level data appears in **Table 11** (referenced as containing complete results but not reproduced in excerpt).

## 6. Math500 / Deepseek Results

**No Math500 or Deepseek-R1-Distill-Llama-8B results appear in the provided content.** The paper evaluates only: Llama 3.1-8B, Llama 3.2-3B, and Qwen 2.5-3B/7B.

## 7. Latency Comparisons

**No latency or throughput numbers are provided.** The paper focuses on accuracy metrics, not inference speed measurements.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "01970313-2a03-4467-8a2d-0ca64ed6642a",
  "isSidechain": false,
  "promptId": "1fbfc64c-b355-4d06-a3ec-ca151a578a76",
  "type": "user",
  "uuid": "f5eeaadf-bcad-478e-b8e0-a544ed4c0c5d",
  "toolUseResult": {
    "bytes": 1673795,
    "code": 200,
    "codeText": "OK",
    "result": "# KeyDiff Paper: Specific Data Points\n\n## 1. Full Context Baseline Scores\n\nFrom **Table 1**, the non-evicting baseline scores are:\n- **Llama 3.1-8B-Instruct**: 49.20 average\n- **Llama 3.2-3B-Instruct**: 45.87 average\n\nKeyDiff at 8K achieves:\n- **Llama 3.1-8B**: 49.03 (gap: 0.17 points, ~0.35%)\n- **Llama 3.2-3B**: 45.78 (gap: 0.09 points, ~0.20%)\n\n**Note**: The paper's \"≤0.04%\" claim appears to reference a different metric or subset; the table shows larger gaps when calculated from raw scores.\n\n## 2. Anchor Vector Computation\n\nThe paper does not explicitly specify whether the anchor `μ(K̂)` is recomputed from scratch at each eviction step or maintained incrementally. Section 3.2 states the anchor is computed as `1/n ∑ k̂ᵢ` where n is the current cache size, suggesting fresh computation per step, but no confirmation of incremental tracking exists.\n\n## 3. LongBench Context Lengths\n\nThe paper states: \"51% of prompts are longer than the largest KV cache size of 8K\" but **does not provide specific maximum sequence lengths** for the benchmark or model context windows. Section B.3 references \"Prompt lengths\" statistics but these are truncated in the provided content.\n\n## 4. \"23% KV Cache Reduction\" Basis\n\nThis figure represents the **average compression across LongBench tasks**: with an 8K budget versus uncompressed full prompts, approximately 23% of the original KV cache is eliminated. No single reference length is specified.\n\n## 5. Per-Task Breakdowns\n\n**Table 1 provides complete per-task results**. Examples for 8K budget (Llama 3.1-8B):\n- NarrativeQA: 18.78 vs baseline 34.86\n- Qasper: 11.35 vs baseline 25.32\n- PassageRetrieval-en: 59.74 vs baseline 61.66\n\nFull task-level data appears in **Table 11** (referenced as containing complete results but not reproduced in excerpt).\n\n## 6. Math500 / Deepseek Results\n\n**No Math500 or Deepseek-R1-Distill-Llama-8B results appear in the provided content.** The paper evaluates only: Llama 3.1-8B, Llama 3.2-3B, and Qwen 2.5-3B/7B.\n\n## 7. Latency Comparisons\n\n**No latency or throughput numbers are provided.** The paper focuses on accuracy metrics, not inference speed measurements.",
    "durationMs": 8418,
    "url": "https://arxiv.org/html/2504.15364v1"
  },
  "sourceToolAssistantUUID": "01970313-2a03-4467-8a2d-0ca64ed6642a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/solver-verified-formalizer-rl",
  "sessionId": "f0e81ad8-eb68-441a-a915-cad985f3b32e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 26 · 2026-05-12T17:29:04.090Z_

<details><summary>Logged reasoning block</summary>

```text
The data is a bit inconsistent between the search results and the actual paper content. Let me try to get more details from the paper, particularly about the Math500/Deepseek results and the 0.04% claim, since the search snippet mentioned it but the HTML content doesn't seem to have it. Let me check the abstract and Qwen results too.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f5eeaadf-bcad-478e-b8e0-a544ed4c0c5d",
  "isSidechain": false,
  "requestId": "req_011Cay51j9jafzA5dr2ViMyp",
  "type": "assistant",
  "uuid": "305d0f08-96ec-4fc1-8867-b9c6e286b07b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/solver-verified-formalizer-rl",
  "sessionId": "f0e81ad8-eb68-441a-a915-cad985f3b32e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ryj2zu1cao1MkQpLfhRuV8",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1177,
      "cache_read_input_tokens": 27971,
      "output_tokens": 496,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1177,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 496,
          "cache_read_input_tokens": 27971,
          "cache_creation_input_tokens": 1177,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1177
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

_source line 27 · 2026-05-12T17:29:04.516Z_

搜索结果提到了 Math500 和延迟数据，但 HTML 版本似乎没有完整显示。让我再查一次。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "305d0f08-96ec-4fc1-8867-b9c6e286b07b",
  "isSidechain": false,
  "requestId": "req_011Cay51j9jafzA5dr2ViMyp",
  "type": "assistant",
  "uuid": "c9148c1a-197e-4053-8ec9-d5cb19204bcd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/solver-verified-formalizer-rl",
  "sessionId": "f0e81ad8-eb68-441a-a915-cad985f3b32e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ryj2zu1cao1MkQpLfhRuV8",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1177,
      "cache_read_input_tokens": 27971,
      "output_tokens": 496,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1177,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 496,
          "cache_read_input_tokens": 27971,
          "cache_creation_input_tokens": 1177,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1177
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

_source line 28 · 2026-05-12T17:29:06.195Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_011YAri6u9TKTswCdyqgiw4h`</summary>

```json
{
  "url": "https://arxiv.org/abs/2504.15364",
  "prompt": "Extract the full abstract of this paper. I need to find the exact wording of the \"0.04% loss\" claim and any mention of Deepseek-R1, Math500, and latency speedup numbers."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c9148c1a-197e-4053-8ec9-d5cb19204bcd",
  "isSidechain": false,
  "requestId": "req_011Cay51j9jafzA5dr2ViMyp",
  "type": "assistant",
  "uuid": "4769eb8c-6eaa-4026-bfdf-18adb825a825",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/solver-verified-formalizer-rl",
  "sessionId": "f0e81ad8-eb68-441a-a915-cad985f3b32e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ryj2zu1cao1MkQpLfhRuV8",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1177,
      "cache_read_input_tokens": 27971,
      "output_tokens": 496,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1177,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 496,
          "cache_read_input_tokens": 27971,
          "cache_creation_input_tokens": 1177,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1177
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

_source line 29 · 2026-05-12T17:29:09.882Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01RCTUupTuadAeDfmwUpQGWy`</summary>

```json
{
  "url": "https://arxiv.org/html/2504.15364v1",
  "prompt": "Find and extract:\n1. The Qwen 2.5-3B and Qwen 2.5-7B results tables with exact numbers for all budgets and all baselines\n2. Any mention of Deepseek-R1-Distill-Llama-8B or Math500 benchmark - search the entire document\n3. Any latency or throughput measurements - search for words like \"latency\", \"speedup\", \"throughput\", \"wall-clock\", \"time\", \"seconds\"\n4. The exact text surrounding the \"0.04%\" claim - I need the exact sentence\n5. Table 7 (appendix) results if available\n6. Algorithm pseudocode or detailed description of per-step eviction procedure"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4769eb8c-6eaa-4026-bfdf-18adb825a825",
  "isSidechain": false,
  "requestId": "req_011Cay51j9jafzA5dr2ViMyp",
  "type": "assistant",
  "uuid": "f9e8869e-f48b-4aab-8316-d1c15d39d633",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/solver-verified-formalizer-rl",
  "sessionId": "f0e81ad8-eb68-441a-a915-cad985f3b32e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ryj2zu1cao1MkQpLfhRuV8",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1177,
      "cache_read_input_tokens": 27971,
      "output_tokens": 496,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1177,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 496,
          "cache_read_input_tokens": 27971,
          "cache_creation_input_tokens": 1177,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1177
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

_source line 30 · 2026-05-12T17:29:12.421Z_

<details><summary>↩ Tool result · `toolu_011YAri6u9TKTswCdyqgiw4h`</summary>

```text
# KeyDiff Paper Abstract - Key Claims

Here is the full abstract with the specific claims you requested:

**Full Abstract:**
"We demonstrate that geometrically distinctive keys during LLM inference tend to have high attention scores. Based on the phenomenon we propose KeyDiff, a training-free KV cache eviction method based solely on key similarity. Unlike other KV cache eviction methods, KeyDiff can process arbitrarily long prompts within strict resource constraints and efficiently generate responses. We provide a theoretical basis for KeyDiff by relating key diversity with attention scores. These results imply KeyDiff can efficiently identify the most important tokens to retain. Notably KeyDiff does not rely on attention scores, allowing the use of optimized attention mechanisms like FlashAttention. Under a strict memory allowance, we demonstrate the effectiveness of KeyDiff for the Llama and Qwen model families by observing a performance gap of less than 0.04% with 8K cache budget (~23% KV cache reduction) from the non-evicting baseline on LongBench for Llama 3.1-8B and Llama 3.2-3B. We also observe near baseline performance for Deepseek-R1-Distill-Llama-8B on the Math500 reasoning benchmark and decrease end-to-end inference latency by up to 30% compared to the other token-eviction methods."

**Key Specific Claims:**
- Performance gap: "less than 0.04%"
- Model tested: "Deepseek-R1-Distill-Llama-8B on the Math500 reasoning benchmark"
- Latency improvement: "up to 30% compared to the other token-eviction methods"
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4769eb8c-6eaa-4026-bfdf-18adb825a825",
  "isSidechain": false,
  "promptId": "1fbfc64c-b355-4d06-a3ec-ca151a578a76",
  "type": "user",
  "uuid": "4129c249-fe8e-4e0a-87bd-31d89e980f6b",
  "toolUseResult": {
    "bytes": 47324,
    "code": 200,
    "codeText": "OK",
    "result": "# KeyDiff Paper Abstract - Key Claims\n\nHere is the full abstract with the specific claims you requested:\n\n**Full Abstract:**\n\"We demonstrate that geometrically distinctive keys during LLM inference tend to have high attention scores. Based on the phenomenon we propose KeyDiff, a training-free KV cache eviction method based solely on key similarity. Unlike other KV cache eviction methods, KeyDiff can process arbitrarily long prompts within strict resource constraints and efficiently generate responses. We provide a theoretical basis for KeyDiff by relating key diversity with attention scores. These results imply KeyDiff can efficiently identify the most important tokens to retain. Notably KeyDiff does not rely on attention scores, allowing the use of optimized attention mechanisms like FlashAttention. Under a strict memory allowance, we demonstrate the effectiveness of KeyDiff for the Llama and Qwen model families by observing a performance gap of less than 0.04% with 8K cache budget (~23% KV cache reduction) from the non-evicting baseline on LongBench for Llama 3.1-8B and Llama 3.2-3B. We also observe near baseline performance for Deepseek-R1-Distill-Llama-8B on the Math500 reasoning benchmark and decrease end-to-end inference latency by up to 30% compared to the other token-eviction methods.\"\n\n**Key Specific Claims:**\n- Performance gap: \"less than 0.04%\"\n- Model tested: \"Deepseek-R1-Distill-Llama-8B on the Math500 reasoning benchmark\"\n- Latency improvement: \"up to 30% compared to the other token-eviction methods\"",
    "durationMs": 6222,
    "url": "https://arxiv.org/abs/2504.15364"
  },
  "sourceToolAssistantUUID": "4769eb8c-6eaa-4026-bfdf-18adb825a825",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/solver-verified-formalizer-rl",
  "sessionId": "f0e81ad8-eb68-441a-a915-cad985f3b32e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 31 · 2026-05-12T17:29:15.629Z_

<details><summary>↩ Tool result · `toolu_01RCTUupTuadAeDfmwUpQGWy`</summary>

```text
Based on my review of the provided document, here are the findings:

## 1. Qwen 2.5 Results Tables

The main paper (Table 1) only shows Llama 3.1-8B and Llama 3.2-3B results. Qwen 2.5-3B/7B results are mentioned as being in Table 9 of the appendix, but **Table 9 is not included in the provided content**. The document references it: "those of Qwen 2.5-3B/7B-Instruct in [Table 9]" but the actual table data is not present.

## 2. Deepseek-R1-Distill or Math500

**No mention found** anywhere in the document of Deepseek-R1-Distill-Llama-8B or a Math500 benchmark.

## 3. Latency or Throughput Measurements

**No latency, speedup, throughput, wall-clock time, or seconds measurements** are provided in this paper. The work focuses exclusively on accuracy metrics.

## 4. The "0.04%" Claim - Exact Text

"KeyDiff outperforms other eviction strategies across most tasks, demonstrating a performance gap of less than 0.04% with 8K cache budget (∼23% KV cache reduction) from the non-evicting baseline on the LongBench benchmark for Llama 3.1-8B and Llama 3.2-3B."

## 5. Table 7 (Appendix Results)

Table 7 is referenced as containing "Results for Full Prompt Processing" but **the actual table data is not included** in the provided document excerpt.

## 6. Algorithm Pseudocode

The document provides equations and mathematical descriptions rather than traditional pseudocode. The eviction procedure is summarized in Equations 7-8, with Figure 3 illustrating the three-step process: compute anchor vector, calculate cosine similarities, retain lowest-similarity tokens.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f9e8869e-f48b-4aab-8316-d1c15d39d633",
  "isSidechain": false,
  "promptId": "1fbfc64c-b355-4d06-a3ec-ca151a578a76",
  "type": "user",
  "uuid": "cd54ba3a-fc13-4c5d-814e-8f6048ec6061",
  "toolUseResult": {
    "bytes": 1673795,
    "code": 200,
    "codeText": "OK",
    "result": "Based on my review of the provided document, here are the findings:\n\n## 1. Qwen 2.5 Results Tables\n\nThe main paper (Table 1) only shows Llama 3.1-8B and Llama 3.2-3B results. Qwen 2.5-3B/7B results are mentioned as being in Table 9 of the appendix, but **Table 9 is not included in the provided content**. The document references it: \"those of Qwen 2.5-3B/7B-Instruct in [Table 9]\" but the actual table data is not present.\n\n## 2. Deepseek-R1-Distill or Math500\n\n**No mention found** anywhere in the document of Deepseek-R1-Distill-Llama-8B or a Math500 benchmark.\n\n## 3. Latency or Throughput Measurements\n\n**No latency, speedup, throughput, wall-clock time, or seconds measurements** are provided in this paper. The work focuses exclusively on accuracy metrics.\n\n## 4. The \"0.04%\" Claim - Exact Text\n\n\"KeyDiff outperforms other eviction strategies across most tasks, demonstrating a performance gap of less than 0.04% with 8K cache budget (∼23% KV cache reduction) from the non-evicting baseline on the LongBench benchmark for Llama 3.1-8B and Llama 3.2-3B.\"\n\n## 5. Table 7 (Appendix Results)\n\nTable 7 is referenced as containing \"Results for Full Prompt Processing\" but **the actual table data is not included** in the provided document excerpt.\n\n## 6. Algorithm Pseudocode\n\nThe document provides equations and mathematical descriptions rather than traditional pseudocode. The eviction procedure is summarized in Equations 7-8, with Figure 3 illustrating the three-step process: compute anchor vector, calculate cosine similarities, retain lowest-similarity tokens.",
    "durationMs": 5741,
    "url": "https://arxiv.org/html/2504.15364v1"
  },
  "sourceToolAssistantUUID": "f9e8869e-f48b-4aab-8316-d1c15d39d633",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/solver-verified-formalizer-rl",
  "sessionId": "f0e81ad8-eb68-441a-a915-cad985f3b32e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 32 · 2026-05-12T17:29:15.636Z_

```json
{
  "parentUuid": "cd54ba3a-fc13-4c5d-814e-8f6048ec6061",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "49b793ed-54aa-4169-977e-c270470326b4",
  "timestamp": "2026-05-12T17:29:15.636Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/solver-verified-formalizer-rl",
  "sessionId": "f0e81ad8-eb68-441a-a915-cad985f3b32e",
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
  "leafUuid": "49b793ed-54aa-4169-977e-c270470326b4",
  "sessionId": "f0e81ad8-eb68-441a-a915-cad985f3b32e"
}
```

---

### Runtime record

_source line 34_

```json
{
  "type": "ai-title",
  "aiTitle": "Extract KeyDiff paper experimental conditions",
  "sessionId": "f0e81ad8-eb68-441a-a915-cad985f3b32e"
}
```

---

### Assistant

_source line 35 · 2026-05-12T17:29:33.378Z_

<details><summary>Logged reasoning block</summary>

```text
The abstract mentions Deepseek-R1 and Math500, but the HTML version of the paper doesn't seem to contain those results in the main body - they might be in the appendix which isn't fully rendered. The "0.04%" claim is about the LongBench average performance gap. But when I computed from the actual table numbers:

- Llama 3.1-8B: baseline 49.20, KeyDiff 8K = 49.03, gap = 0.17 points = 0.35%


- Llama 3.2-3B: baseline 45.87, KeyDiff 8K = 45.78, gap = 0.09 points = 0.20%

Neither of these matches the "less than 0.04%" claim. I'm calculating the relative percentage as (difference / baseline) × 100, which gives 0.35% and 0.20% respectively - both much larger than 0.04%. The discrepancy could mean the abstract is using a different calculation method, or the numbers I extracted from the table might be slightly off. The discrepancy is concerning—either the WebFetch data is slightly off, the 0.04% claim applies to a specific condition I'm missing, or the abstract is overstating the results. I should flag this in my report. Now let me pull together everything I've found about the centroid computation: it's the mean of L2-normalized keys, the paper doesn't clarify if it's recomputed or maintained incrementally, and it runs in O(n) time per eviction, though it could theoretically be tracked as a running sum for efficiency. Time to write up the final answer.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "49b793ed-54aa-4169-977e-c270470326b4",
  "isSidechain": false,
  "requestId": "req_011Cay52qbTZ6qKkhdDrTuEL",
  "type": "assistant",
  "uuid": "d0a502c4-eb20-4532-9024-bb2dd0fba5e6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/solver-verified-formalizer-rl",
  "sessionId": "f0e81ad8-eb68-441a-a915-cad985f3b32e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TpLfQXAtjG2MM4JjTLj7jv",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1514,
      "cache_read_input_tokens": 29148,
      "output_tokens": 3213,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1514,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3213,
          "cache_read_input_tokens": 29148,
          "cache_creation_input_tokens": 1514,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1514
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

_source line 36 · 2026-05-12T17:30:08.123Z_

数据收集完毕。以下是 KeyDiff 论文精确实验条件的汇总。

---

## KeyDiff (arXiv:2504.15364) 实验条件汇总

### 1. 模型

| 模型 | 参数量 | 用途 |
|------|--------|------|
| Llama 3.1-8B-Instruct | 8B | 主实验 (LongBench) |
| Llama 3.2-3B-Instruct | 3B | 主实验 (LongBench) |
| Qwen 2.5-3B-Instruct | 3B | 附录 (Table 9, 未在 HTML 中完整展示) |
| Qwen 2.5-7B-Instruct | 7B | 附录 (Table 9) |
| Deepseek-R1-Distill-Llama-8B | 8B | Math500 (仅在 abstract 提及, 正文/附录未找到详细数据) |

### 2. 评测数据集

**LongBench (English subset, 16 tasks):**
- Single Doc QA: NarrativeQA, Qasper
- Multi Doc QA: MultifieldQA-en, HotpotQA, 2WikiMQA, Musique
- Summarization: GovReport, QMSum, MultiNews
- Few-shot: TREC, TriviaQA, SAMSum
- Synthetic: PassageCount, PassageRetrieval-en
- Code: LCC, RepoBench-P

**其他:** Needle In a Haystack, Math500 (仅 abstract 提及)

### 3. KV Cache Budget

| Budget | Token 数 | 近似压缩比 (基于 LongBench 平均) |
|--------|----------|--------------------------------|
| 2K | 2048 | ~80% reduction |
| 4K | 4096 | ~55% reduction |
| 6K | 6144 | ~33% reduction |
| 8K | 8192 | **~23% reduction** |

Block size: B=128 (prompt processing), B=1 (generation)。51% 的 LongBench prompt 长度超过 8K。

### 4. "<0.04% loss" 精确含义

**论文原文：** "a performance gap of less than 0.04% with 8K cache budget (~23% KV cache reduction) from the non-evicting baseline on LongBench for Llama 3.1-8B and Llama 3.2-3B"

**但实际表格数据存在不一致：**

| 模型 | Full Context | KeyDiff@8K | 绝对差 (pp) | 相对差 |
|------|-------------|------------|-------------|--------|
| Llama 3.1-8B | 49.20 | 49.03 | **0.17 pp** | **0.35%** |
| Llama 3.2-3B | 45.87 | 45.78 | **0.09 pp** | **0.20%** |

- **度量：** LongBench 各任务平均分 (各任务有自己的 metric，综合后取均值)
- **0.04% 与表格数据不匹配** — 可能指特定 subset、附录中的 full-prompt-processing (B=∞) 配置 (Table 7)，或者 abstract 的表述有误。HTML 版未完整展示附录表格，无法最终确认。

### 5. Centroid (Anchor) 计算方式

**公式：**
$$\mu(\hat{K}) = \frac{1}{n}\sum_{i=1}^{n} \frac{k_i}{\|k_i\|}$$

- **先对每个 key 做 L2 归一化，再取算术平均** — 即 exact mean of normalized keys
- 论文**未明确说明**是 per-step 重新计算还是 running mean (incremental)
- 由于是简单均值，理论上可用 running sum 增量维护：`sum += new_key/||new_key||; sum -= evicted_key/||evicted_key||; anchor = sum/n`
- **复杂度：O(n) per eviction step** (n = cache size)，计算所有 token 与 anchor 的 cosine similarity 以选出要驱逐的 token

**Ablation (Llama 3.2-3B, Table 2) — anchor 选择方式对比：**

| Budget | Pairwise | Median | KeyDiff (Mean) |
|--------|----------|--------|----------------|
| 2K | 35.24 | 35.43 | 35.09 |
| 4K | 40.61 | 40.67 | 40.28 |
| 6K | 41.87 | 41.89 | 41.88 |
| 8K | 42.45 | 42.26 | 42.40 |

差异很小，Mean 方案在大 budget 下接近其他方案，但计算最简单。

### 6. Baseline 对比 (主表)

**Llama 3.1-8B-Instruct, LongBench Average, B=128:**

| Budget | H2O | TOVA | StreamingLLM (Sink) | SnapKV | **KeyDiff** | Full Context |
|--------|-----|------|---------------------|--------|-------------|-------------|
| 2K | 16.89 | 37.52 | 36.88 | 39.60 | **44.33** | 49.20 |
| 4K | 26.37 | 41.49 | 40.95 | 45.18 | **47.66** | 49.20 |
| 6K | 33.19 | 45.24 | 43.39 | 47.12 | **48.51** | 49.20 |
| 8K | 38.20 | 47.09 | 44.68 | 48.06 | **49.03** | 49.20 |

**Llama 3.2-3B-Instruct, LongBench Average, B=128:**

| Budget | H2O | TOVA | StreamingLLM (Sink) | SnapKV | **KeyDiff** | Full Context |
|--------|-----|------|---------------------|--------|-------------|-------------|
| 2K | 14.25 | 33.52 | 33.74 | 35.46 | **38.14** | 45.87 |
| 4K | 22.38 | 38.24 | 37.96 | 40.60 | **43.67** | 45.87 |
| 6K | 28.44 | 41.02 | 40.01 | 43.55 | **45.27** | 45.87 |
| 8K | 33.46 | 43.21 | 41.97 | 44.96 | **45.78** | 45.87 |

**Similarity metric ablation (Table 3, Llama 3.2-3B):**

| Budget | Dot Product | Euclidean | **Cosine (KeyDiff)** |
|--------|------------|-----------|---------------------|
| 2K | 30.14 | 13.68 | **35.09** |
| 4K | 38.01 | 21.06 | **40.28** |
| 8K | 42.23 | 29.53 | **42.40** |

### 7. 缺失/不完整数据

| 信息 | 状态 |
|------|------|
| Deepseek-R1 + Math500 精确数字 | **仅 abstract 提及 "near baseline"，正文无详细表格** |
| 延迟 "up to 30% speedup" 具体数据 | **仅 abstract 提及，正文无 latency 表格** |
| Qwen 2.5-3B/7B 完整结果 | **在附录 Table 9，HTML 版未完整渲染** |
| Full prompt processing (B=∞) 结果 | **在附录 Table 7，HTML 版未完整渲染** |
| 0.04% claim 的精确来源 | **与主表数据不一致，可能来自未展示的附录表** |

---

**核心结论：** KeyDiff 在所有 budget 下均优于 H2O、TOVA、StreamingLLM、SnapKV。8K budget 下与 full context 的差距为 0.17pp (Llama-8B) / 0.09pp (Llama-3B)。Anchor 是 normalized keys 的 exact mean，O(n) 复杂度。Abstract 中的 "0.04%"、"30% latency"、"Math500" 三项 claim 在论文正文中均未找到支撑数据表格。

Sources:
- [KeyDiff Paper (arXiv abstract)](https://arxiv.org/abs/2504.15364)
- [KeyDiff Paper (HTML full text)](https://arxiv.org/html/2504.15364v1)
- [AlphaXiv page](https://www.alphaxiv.org/abs/2504.15364)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d0a502c4-eb20-4532-9024-bb2dd0fba5e6",
  "isSidechain": false,
  "requestId": "req_011Cay52qbTZ6qKkhdDrTuEL",
  "type": "assistant",
  "uuid": "aabcea78-afc0-49ea-a904-724d694be75b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/solver-verified-formalizer-rl",
  "sessionId": "f0e81ad8-eb68-441a-a915-cad985f3b32e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TpLfQXAtjG2MM4JjTLj7jv",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1514,
      "cache_read_input_tokens": 29148,
      "output_tokens": 3213,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1514,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3213,
          "cache_read_input_tokens": 29148,
          "cache_creation_input_tokens": 1514,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1514
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

_source line 37_

```json
{
  "type": "last-prompt",
  "leafUuid": "aabcea78-afc0-49ea-a904-724d694be75b",
  "sessionId": "f0e81ad8-eb68-441a-a915-cad985f3b32e"
}
```

---

### Runtime record

_source line 38_

```json
{
  "type": "ai-title",
  "aiTitle": "Extract KeyDiff paper experimental conditions",
  "sessionId": "f0e81ad8-eb68-441a-a915-cad985f3b32e"
}
```

---
