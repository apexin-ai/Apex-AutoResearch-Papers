# Research conversation: <agent_context> Director 将 paper_outline.md 从 P1 升级到 P0，要求与 paper_framing.md 一起修完。245-ep baseline 已由 plan-003-baseline-2

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 62
- **Recorded user turns:** 1
- **Tool calls:** 16
- **Original source:** `logs/chats/exported-trajectories/account-2/fe1af098-4ed4-4fac-9d28-af54a02d46ce.jsonl`
- **Structured JSON:** [`6f476d2fb1f327e96f3c.json`](../../sessions/6f/6f476d2fb1f327e96f3c.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-14T08:19:36.709Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-14T08:19:36.709Z",
  "sessionId": "fe1af098-4ed4-4fac-9d28-af54a02d46ce",
  "content": "&lt;agent_context>\nDirector 将 paper_outline.md 从 P1 升级到 P0，要求与 paper_framing.md 一起修完。245-ep baseline 已由 plan-003-baseline-245eps 完成。修完后 D028 论文写作暂停限制解除。\n&lt;/agent_context>\n\n&lt;project_context>\n# 项目: simgate-modular-routing\n\n## 运行环境\n- 服务器名: westb-13313\n- SSH 账户: root（调用 ssh_execute / submit_training_job 时传入 account=\"root\"）\n- SSH 连接命令: ssh connect.westb.seetacloud.com  # 必须用此命令，~/.ssh/config 自动应用密钥和跳板机，禁止用裸 IP\n- 项目代码根目录: /root/autodl-tmp/simgate-modular-routing\n\n\n## 环境搭建\n连接服务器后先调 `detect_image` 检测是否为预置镜像。如果匹配，跳过基础环境搭建，只装项目特有依赖。已预装的包不要重复安装。\n\n## 输出风格\n回复简洁直接。只输出执行结果和必要信息，不要解释过程、不要客套、不要给未被要求的建议。\n&lt;/project_context>\n## 更新 paper_outline.md 中的 baseline 数字到 245-ep 版本\n\n### 任务\n用 `read_project_file(file=\"paper_outline.md\")` 读取当前内容（可能在 artifacts/_project/paper/ 路径下，用 max_chars=0 获取全文）。\n\n替换 baseline 数字：\n\n| Strategy | 旧 (194 eps) | 新 (245 eps) |\n|----------|-------------|-------------|\n| always-internal | -37.16 | **-39.07** |\n| always-deterministic | -11.64 | **-9.47** |\n| oracle | -9.03 | **-6.58** |\n| random | -23.75 | **-22.38** |\n\n同时检查文件中是否有其他需要从 194-ep / 30-task 更新到 11-task/245-ep 的数字：\n- Δ_full 应为 29.60（非 38.33）\n- Δ_nd 应为 2.84（非 0.48）\n- DAF 应为 90.41%（非 98.75%）\n- r 应为 0.9698（非 0.9864）\n- p 应为 8.12e-07\n- 11 tasks / 245 episodes（非 30 tasks / 249 eps）\n- find-non-living-thing: n=40, Δ=+9.58\n\n每个数字后标注 `[A: plan-012-full, 245eps/11tasks]`。\n\n用 `save_project_file` 保存修改后的文件。\n"
}
```

---

### Runtime record

_source line 2 · 2026-05-14T08:19:36.716Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-14T08:19:36.716Z",
  "sessionId": "fe1af098-4ed4-4fac-9d28-af54a02d46ce"
}
```

---

## Round 1

60 recorded events

### User

_source line 3 · 2026-05-14T08:19:36.790Z_

&lt;agent_context>
Director 将 paper_outline.md 从 P1 升级到 P0，要求与 paper_framing.md 一起修完。245-ep baseline 已由 plan-003-baseline-245eps 完成。修完后 D028 论文写作暂停限制解除。
&lt;/agent_context>

&lt;project_context>
# 项目: simgate-modular-routing

## 运行环境
- 服务器名: westb-13313
- SSH 账户: root（调用 ssh_execute / submit_training_job 时传入 account="root"）
- SSH 连接命令: ssh connect.westb.seetacloud.com  # 必须用此命令，~/.ssh/config 自动应用密钥和跳板机，禁止用裸 IP
- 项目代码根目录: /root/autodl-tmp/simgate-modular-routing


## 环境搭建
连接服务器后先调 `detect_image` 检测是否为预置镜像。如果匹配，跳过基础环境搭建，只装项目特有依赖。已预装的包不要重复安装。

## 输出风格
回复简洁直接。只输出执行结果和必要信息，不要解释过程、不要客套、不要给未被要求的建议。
&lt;/project_context>
## 更新 paper_outline.md 中的 baseline 数字到 245-ep 版本

### 任务
用 `read_project_file(file="paper_outline.md")` 读取当前内容（可能在 artifacts/_project/paper/ 路径下，用 max_chars=0 获取全文）。

替换 baseline 数字：

| Strategy | 旧 (194 eps) | 新 (245 eps) |
|----------|-------------|-------------|
| always-internal | -37.16 | **-39.07** |
| always-deterministic | -11.64 | **-9.47** |
| oracle | -9.03 | **-6.58** |
| random | -23.75 | **-22.38** |

同时检查文件中是否有其他需要从 194-ep / 30-task 更新到 11-task/245-ep 的数字：
- Δ_full 应为 29.60（非 38.33）
- Δ_nd 应为 2.84（非 0.48）
- DAF 应为 90.41%（非 98.75%）
- r 应为 0.9698（非 0.9864）
- p 应为 8.12e-07
- 11 tasks / 245 episodes（非 30 tasks / 249 eps）
- find-non-living-thing: n=40, Δ=+9.58

每个数字后标注 `[A: plan-012-full, 245eps/11tasks]`。

用 `save_project_file` 保存修改后的文件。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "de32f0f5-b4f7-4fe9-872c-8108c929635d",
  "type": "user",
  "uuid": "ef3bc0c8-1075-4ce6-9f10-e0e8aa2620d6",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing",
  "sessionId": "fe1af098-4ed4-4fac-9d28-af54a02d46ce",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-14T08:19:36.787Z_

```json
{
  "parentUuid": "ef3bc0c8-1075-4ce6-9f10-e0e8aa2620d6",
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
  "uuid": "2035bd80-204e-4f5c-a781-022e12844564",
  "timestamp": "2026-05-14T08:19:36.787Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing",
  "sessionId": "fe1af098-4ed4-4fac-9d28-af54a02d46ce",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-14T08:19:36.787Z_

```json
{
  "parentUuid": "2035bd80-204e-4f5c-a781-022e12844564",
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
  "uuid": "861140a0-c536-4f6c-ad14-860ce99e0353",
  "timestamp": "2026-05-14T08:19:36.787Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing",
  "sessionId": "fe1af098-4ed4-4fac-9d28-af54a02d46ce",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 6 · 2026-05-14T08:19:36.787Z_

```json
{
  "parentUuid": "861140a0-c536-4f6c-ad14-860ce99e0353",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "e8ddf3eb-8214-4c11-92ce-5cb07697bc1c",
  "timestamp": "2026-05-14T08:19:36.787Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing",
  "sessionId": "fe1af098-4ed4-4fac-9d28-af54a02d46ce",
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
  "aiTitle": "Update paper_outline.md baseline numbers to 245-ep",
  "sessionId": "fe1af098-4ed4-4fac-9d28-af54a02d46ce"
}
```

---

### Assistant

_source line 8 · 2026-05-14T08:19:40.049Z_

<details><summary>Logged reasoning block</summary>

```text
Let me start by reading the current paper_outline.md file using the MCP tool.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e8ddf3eb-8214-4c11-92ce-5cb07697bc1c",
  "isSidechain": false,
  "requestId": "req_011Cb28jfJqaDfdEnxLJnSBH",
  "type": "assistant",
  "uuid": "9cd3b478-797d-41ba-b401-782089f0ec48",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing",
  "sessionId": "fe1af098-4ed4-4fac-9d28-af54a02d46ce",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EcCvTbktUJGKkwVCuYCsPF",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 11284,
      "cache_read_input_tokens": 11841,
      "output_tokens": 153,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11284,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 153,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11284,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11284
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

_source line 9 · 2026-05-14T08:19:40.072Z_

先读取当前 paper_outline.md 内容。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9cd3b478-797d-41ba-b401-782089f0ec48",
  "isSidechain": false,
  "requestId": "req_011Cb28jfJqaDfdEnxLJnSBH",
  "type": "assistant",
  "uuid": "168e930f-6ede-46a1-8fd2-61aec3da09b0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing",
  "sessionId": "fe1af098-4ed4-4fac-9d28-af54a02d46ce",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EcCvTbktUJGKkwVCuYCsPF",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 11284,
      "cache_read_input_tokens": 11841,
      "output_tokens": 153,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11284,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 153,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11284,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11284
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

_source line 10 · 2026-05-14T08:19:40.880Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01GJWQ9CF5ZQuYJUPunTPsKh`</summary>

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
  "parentUuid": "168e930f-6ede-46a1-8fd2-61aec3da09b0",
  "isSidechain": false,
  "requestId": "req_011Cb28jfJqaDfdEnxLJnSBH",
  "type": "assistant",
  "uuid": "47076009-3c40-4da4-8292-f6a7a3557392",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing",
  "sessionId": "fe1af098-4ed4-4fac-9d28-af54a02d46ce",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EcCvTbktUJGKkwVCuYCsPF",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 11284,
      "cache_read_input_tokens": 11841,
      "output_tokens": 153,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11284,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 153,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11284,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11284
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

_source line 11 · 2026-05-14T08:19:40.887Z_

<details><summary>↩ Tool result · `toolu_01GJWQ9CF5ZQuYJUPunTPsKh`</summary>

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
  "parentUuid": "47076009-3c40-4da4-8292-f6a7a3557392",
  "isSidechain": false,
  "promptId": "de32f0f5-b4f7-4fe9-872c-8108c929635d",
  "type": "user",
  "uuid": "9f4e1441-e453-47e5-8a1b-41b8a35f8016",
  "toolUseResult": {
    "matches": [
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__save_project_file"
    ],
    "query": "select:mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__save_project_file",
    "total_deferred_tools": 22
  },
  "sourceToolAssistantUUID": "47076009-3c40-4da4-8292-f6a7a3557392",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing",
  "sessionId": "fe1af098-4ed4-4fac-9d28-af54a02d46ce",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-14T08:19:44.434Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_018xpeuXvCK5tYWAqT5KU4W7`</summary>

```json
{
  "project": "simgate-modular-routing",
  "file": "paper_outline.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9f4e1441-e453-47e5-8a1b-41b8a35f8016",
  "isSidechain": false,
  "requestId": "req_011Cb28jxrmXtmGZozsSSUmb",
  "type": "assistant",
  "uuid": "a8b9bf9a-fc49-4d72-bff0-d9702eca8612",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing",
  "sessionId": "fe1af098-4ed4-4fac-9d28-af54a02d46ce",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CRVPoYehzN4XrfBh7y6AYC",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 748,
      "cache_read_input_tokens": 23125,
      "output_tokens": 111,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 748,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 111,
          "cache_read_input_tokens": 23125,
          "cache_creation_input_tokens": 748,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 748
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

_source line 13 · 2026-05-14T08:19:44.482Z_

<details><summary>↩ Tool result · `toolu_018xpeuXvCK5tYWAqT5KU4W7`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"file must be one of ['ARCHITECTURE.md', 'DATA.md', 'EVALUATION.md', 'MODELS.md', 'ROADMAP.md', 'constraints.yaml', 'decisions.yaml', 'ideas.md', 'literature_map.yaml', 'memory.md', 'paper_checklist.yaml', 'paper_framing.md', 'paper_provenance.yaml', 'report.md', 'writing_plan.yaml'], got 'paper_outline.md'\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a8b9bf9a-fc49-4d72-bff0-d9702eca8612",
  "isSidechain": false,
  "promptId": "de32f0f5-b4f7-4fe9-872c-8108c929635d",
  "type": "user",
  "uuid": "f53a9c84-6bfe-4cac-8659-40eacfc80a6a",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {}, \\\"error\\\": \\\"file must be one of ['ARCHITECTURE.md', 'DATA.md', 'EVALUATION.md', 'MODELS.md', 'ROADMAP.md', 'constraints.yaml', 'decisions.yaml', 'ideas.md', 'literature_map.yaml', 'memory.md', 'paper_checklist.yaml', 'paper_framing.md', 'paper_provenance.yaml', 'report.md', 'writing_plan.yaml'], got 'paper_outline.md'\\\", \\\"metadata\\\": {}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {}, \"error\": \"file must be one of ['ARCHITECTURE.md', 'DATA.md', 'EVALUATION.md', 'MODELS.md', 'ROADMAP.md', 'constraints.yaml', 'decisions.yaml', 'ideas.md', 'literature_map.yaml', 'memory.md', 'paper_checklist.yaml', 'paper_framing.md', 'paper_provenance.yaml', 'report.md', 'writing_plan.yaml'], got 'paper_outline.md'\", \"metadata\": {}}"
    }
  },
  "sourceToolAssistantUUID": "a8b9bf9a-fc49-4d72-bff0-d9702eca8612",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing",
  "sessionId": "fe1af098-4ed4-4fac-9d28-af54a02d46ce",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 14 · 2026-05-14T08:19:47.885Z_

paper_outline.md 不在白名单中，直接从文件系统读取。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f53a9c84-6bfe-4cac-8659-40eacfc80a6a",
  "isSidechain": false,
  "requestId": "req_011Cb28kEHU2zC92mnhhXdPJ",
  "type": "assistant",
  "uuid": "16a27da7-117b-4cc7-b9bd-b8ea142536b1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing",
  "sessionId": "fe1af098-4ed4-4fac-9d28-af54a02d46ce",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014Fk5sjpwJKKDjrBLzfDTtx",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 274,
      "cache_read_input_tokens": 23873,
      "output_tokens": 174,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 274,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 174,
          "cache_read_input_tokens": 23873,
          "cache_creation_input_tokens": 274,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 274
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

_source line 15 · 2026-05-14T08:19:49.580Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01UrVBmhY8zCMwBdWH4Nkgvu`</summary>

```json
{
  "description": "Find paper_outline.md location",
  "subagent_type": "Explore",
  "prompt": "Find the file paper_outline.md in the project directory /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/. Search recursively. Report the full path(s) found."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "16a27da7-117b-4cc7-b9bd-b8ea142536b1",
  "isSidechain": false,
  "requestId": "req_011Cb28kEHU2zC92mnhhXdPJ",
  "type": "assistant",
  "uuid": "4626670d-4b91-4738-8bef-f49a391f6562",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing",
  "sessionId": "fe1af098-4ed4-4fac-9d28-af54a02d46ce",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014Fk5sjpwJKKDjrBLzfDTtx",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 274,
      "cache_read_input_tokens": 23873,
      "output_tokens": 174,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 274,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 174,
          "cache_read_input_tokens": 23873,
          "cache_creation_input_tokens": 274,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 274
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

_source line 16 · 2026-05-14T08:19:52.121Z_

<details><summary>↩ Tool result · `toolu_01UrVBmhY8zCMwBdWH4Nkgvu`</summary>

```text
The file has been found at the following path:

**/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/_project/paper/paper_outline.md**
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4626670d-4b91-4738-8bef-f49a391f6562",
  "isSidechain": false,
  "promptId": "de32f0f5-b4f7-4fe9-872c-8108c929635d",
  "type": "user",
  "uuid": "090fafb2-cbf7-4f1b-b6d9-98bd56b7ac4b",
  "toolUseResult": {
    "status": "completed",
    "prompt": "Find the file paper_outline.md in the project directory /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/. Search recursively. Report the full path(s) found.",
    "agentId": "aa63dbe31175fd83a",
    "agentType": "Explore",
    "content": [
      {
        "type": "text",
        "text": "The file has been found at the following path:\n\n**/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/_project/paper/paper_outline.md**"
      }
    ],
    "totalDurationMs": 2535,
    "totalTokens": 16491,
    "totalToolUseCount": 1,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 980,
      "cache_read_input_tokens": 15449,
      "output_tokens": 57,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 980
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 5,
          "output_tokens": 57,
          "cache_read_input_tokens": 15449,
          "cache_creation_input_tokens": 980,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 980,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 0,
      "searchCount": 1,
      "bashCount": 0,
      "editFileCount": 0,
      "linesAdded": 0,
      "linesRemoved": 0,
      "otherToolCount": 0
    }
  },
  "sourceToolAssistantUUID": "4626670d-4b91-4738-8bef-f49a391f6562",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing",
  "sessionId": "fe1af098-4ed4-4fac-9d28-af54a02d46ce",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-14T08:19:54.783Z_

<details open><summary>🔧 Tool call — Read · `toolu_01QDyfapUtDgXcpFYNzJoRbi`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/_project/paper/paper_outline.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "090fafb2-cbf7-4f1b-b6d9-98bd56b7ac4b",
  "isSidechain": false,
  "requestId": "req_011Cb28knd9c1g6TGEhhRfVY",
  "type": "assistant",
  "uuid": "76191722-967c-4eff-9c43-cabebc895fb6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing",
  "sessionId": "fe1af098-4ed4-4fac-9d28-af54a02d46ce",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013AGuFF7E2QVGwVkebp2wZz",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 240,
      "cache_read_input_tokens": 24147,
      "output_tokens": 93,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 240,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 93,
          "cache_read_input_tokens": 24147,
          "cache_creation_input_tokens": 240,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 240
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

_source line 18 · 2026-05-14T08:19:54.791Z_

<details><summary>↩ Tool result · `toolu_01QDyfapUtDgXcpFYNzJoRbi`</summary>

```text
1	# EMNLP 2026 Short Paper Outline
2	
3	## Title Candidates
4	
5	1. **Death Avoidance Dominates Routing Signal: A Counterfactual Analysis of LLM Agent Tool Use in Interactive Environments**
6	2. **When Does Deterministic Computation Help LLM Agents? Episode-Level Counterfactual Analysis Reveals Death Avoidance Dominance**
7	3. **90% Death Avoidance: Decomposing the Routing Signal Between LLM Reasoning and Deterministic Simulation**
8	
9	Recommended: **Title 1** (clear claim + methodology in title; fits short paper convention of stating the finding)
10	
11	---
12	
13	## Abstract Skeleton (~150 words)
14	
15	Key points to cover:
16	
17	- **Problem**: LLM agents hallucinate state transitions in rule-governed environments, causing catastrophic failures (deaths). Routing between internal LLM reasoning and deterministic computation (simulators) can mitigate this, but what exactly does routing learn?
18	- **Methodological gap**: Per-step oracle labeling degenerates in sparse-reward settings (98% tie rate on ScienceWorld). We propose episode-level counterfactual analysis.
19	- **Core finding**: Death avoidance accounts for ~90% of routing signal (Δ_full=+29.60, Δ_no_death=+2.84; Pearson r=0.97, p<1e-6 across 11 task types / 245 episodes). Non-death performance is approximately equal between modalities.
20	- **Supporting finding**: Keyword heuristics structurally fail (match rates degenerate to ≈always-det or ≈always-internal); episode-level counterfactual labels can train a lightweight router (internal_recall=51.5%).
21	- **Implication**: The value of deterministic computation in interactive environments is concentrated in catastrophic failure prevention, not positive task guidance.
22	
23	---
24	
25	## Section Structure
26	
27	### 1. Introduction (0.8 pages)
28	
29	**Key points:**
30	- LLM agents on rule-governed environments (physics, chemistry) suffer catastrophic failures from hallucinated state transitions → motivate the routing question
31	- Existing work: tool-use learning (Toolformer, ART, Chameleon) learns *when* to invoke tools but doesn't analyze *what* routing learns; ITP-R routes to approximate world models but underperforms pure internal reasoning; ReTool/AgentMath use implicit routing entangled with backbone
32	- Per-step oracle labeling degenerates in sparse-reward environments (98% tie rate) → need episode-level analysis
33	- **Contributions** (bulleted):
34	  1. Episode-level counterfactual methodology that overcomes per-step oracle degeneracy
35	  2. Empirical finding: death avoidance accounts for ≥90% of routing signal on ScienceWorld (11 tasks, 245 episodes)
36	  3. Structural failure analysis of keyword heuristics; demonstration that counterfactual labels can train a lightweight diagnostic router
37	
38	### 2. Method (1.0 pages)
39	
40	**Key points:**
41	- **2.1 Problem Setup**: ScienceWorld environment; two computation modalities (internal LLM reasoning vs. deterministic simulation via environment forking); per-step routing decision
42	- **2.2 Episode-Level Counterfactual Labeling**: Why per-step oracle fails (98% tie rate in sparse rewards) → run complete episodes under pure-internal and pure-deterministic strategies → compare episode-level scores → label: det-preferred / internal-preferred / no-preference. Distribution: 86 det-pref / 9 int-pref / 150 no-pref (245 episodes)
43	- **2.3 Death Decomposition Framework**: Decompose Δ_full into death-avoidance component (Δ_death) and non-death component (Δ_nd). Death avoidance fraction = (Δ_full - Δ_nd) / Δ_full. Cross-task correlation: Pearson r between per-task death rate difference and Δ_full
44	
45	### 3. Experiments (1.5 pages)
46	
47	**Key points:**
48	- **3.1 Setup**: Qwen3-1.7B backbone; ScienceWorld 11 task types × 20-40 episodes; evaluation: always-internal, always-deterministic, oracle, random, keyword heuristic, learned router
49	- **3.2 Death Decomposition Results** (core result):
50	  - Δ_full=+29.60, Δ_nd=+2.84, death fraction=90.41%
51	  - 10/11 death-prone tasks: death-dominated gaps
52	  - 1 exception: find-non-living-thing (0 deaths, Δ=+9.58 from non-death mechanisms)
53	  - Pearson r=0.9698 (p=8.12e-07)
54	- **3.3 Baseline Comparison**:
55	  - always-internal: -37.16, always-det: -11.64, oracle: -9.03, random: -23.75
56	  - Keyword heuristic: structural failure (v1 85.8% match → ≈always-det; v2 4.9% → ≈always-internal)
57	  - Learned router (ablation-b): internal_recall=51.5%, first non-degenerate; classification head variants all degenerate
58	- **3.4 Analysis**: Death rate: internal 42.9% vs. deterministic 16.3%; alive-episode scores nearly equal across modalities
59	
60	### 4. Related Work (0.5 pages, integrated or separate)
61	
62	**Key points:**
63	- **Tool-use learning**: Toolformer (self-supervised API insertion), ART (LLM-as-router), Chameleon (LLM-as-planner), ToolkenGPT (token-level triggers). Differentiation: episode-level counterfactual labeling, safety-aware framing, explicit modular router
64	- **Adaptive computation / routing**: CogRouter (RL-based), ARES, Mixture-of-Depths. Our focus: empirical analysis of *what* routing learns, not a new routing architecture
65	- **World model routing**: ITP-R, Dyna-Think. Our deterministic computation is exact (simulator), not approximate (LLM world model)
66	- **Agent frameworks**: ReAct, Reflexion. Orthogonal — we analyze the routing decision within an agent loop
67	
68	### 5. Conclusion (0.3 pages)
69	
70	**Key points:**
71	- Summary: death avoidance ≥90% of routing signal; episode-level counterfactual analysis as diagnostic methodology
72	- **Limitations**: single benchmark (ScienceWorld), episode-level granularity (not step-level), DAgger distribution shift (train on pure strategies, deploy on mixed)
73	- **Future work**: step-level labeling with denser reward signals, extension to MATH/code interpretation domains, DAgger-style iterative relabeling
74	
75	---
76	
77	## Figure/Table Plan
78	
79	### Table 1: Baseline Comparison
80	| Method | Score | 90% CI | Success Rate | Death Rate | Sim Ratio |
81	|--------|-------|--------|-------------|------------|-----------|
82	| Always-Internal | -37.16 | [-43.39, -31.43] | 12.4% | 40.7% | 0.00 |
83	| Always-Deterministic | -11.64 | [-17.39, -6.55] | 23.7% | 18.6% | 1.00 |
84	| Oracle | -9.03 | [-14.14, -4.15] | 24.2% | 16.5% | 0.96 |
85	| Random | -23.75 | [-29.60, -18.11] | 16.5% | 28.4% | 0.50 |
86	| Keyword Heuristic (v1) | ≈ Always-Det | — | — | — | 0.86 |
87	| Keyword Heuristic (v2) | ≈ Always-Int | — | — | — | 0.05 |
88	| Learned Router (implicit) | TBD | — | — | — | TBD |
89	
90	*Source: plan-003-baseline, plan-011-rule-based*
91	
92	### Figure 1: Death Decomposition (core figure)
93	- **Type**: Grouped bar chart or stacked bar
94	- **X-axis**: 11 task types (sorted by death fraction)
95	- **Y-axis**: Score delta (deterministic − internal)
96	- **Bars**: Δ_full decomposed into Δ_death (death-avoidance component, dark) and Δ_nd (non-death component, light)
97	- **Highlight**: find-non-living-thing as sole exception (Δ_nd = Δ_full = 9.58, zero deaths)
98	- **Annotation**: Overall death fraction = 90.41%
99	
100	*Source: plan-012-full*
101	
102	### Figure 2: Cross-task Correlation (if space permits)
103	- **Type**: Scatter plot with regression line
104	- **X-axis**: Per-task death rate difference (internal − deterministic)
105	- **Y-axis**: Δ_full per task
106	- **Regression line**: r=0.9698, p=8.12e-07
107	- **11 points**, labeled by task type
108	- **Purpose**: Visually demonstrates near-perfect linear relationship
109	
110	*Source: plan-012-full, plan-012-decomposition*
111	
112	**Space strategy**: Figure 1 is mandatory. Figure 2 can be merged as an inset in Figure 1, or moved to appendix if space is tight. Table 1 is mandatory. Per-task breakdown table → appendix.
113	
114	---
115	
116	## Key References
117	
118	### Tool-Use Learning
119	- Schick et al. (2024). Toolformer: Language Models Can Teach Themselves to Use Tools. *NeurIPS*
120	- Paranjape et al. (2023). ART: Automatic Multi-step Reasoning and Tool-Use. *arXiv*
121	- Lu et al. (2024). Chameleon: Plug-and-Play Compositional Reasoning with Large Language Models. *NeurIPS*
122	- Hao et al. (2024). ToolkenGPT: Augmenting Frozen Language Models with Massive Tools via Tool Embeddings. *NeurIPS*
123	
124	### Agent Routing / Adaptive Computation
125	- CogRouter — RL-based cognitive routing (ScienceWorld SOTA)
126	- ITP-R — imagination-based routing to LLM world model
127	- ARES — adaptive routing for efficient serving
128	- Raposo et al. (2024). Mixture-of-Depths. *ICML*
129	
130	### Agent Frameworks
131	- Yao et al. (2023). ReAct: Synergizing Reasoning and Acting in Language Models. *ICLR*
132	- Shinn et al. (2023). Reflexion: Language Agents with Verbal Reinforcement Learning. *NeurIPS*
133	
134	### Methodology
135	- Ross et al. (2011). A Reduction of Imitation Learning and Structured Prediction to No-Regret Online Learning. *AISTATS* (DAgger)
136	
137	### Environment
138	- Wang et al. (2022). ScienceWorld: Is your Agent Smarter than a 5th Grader? *EMNLP*
139	
140	### Code Execution Routing
141	- Gou et al. (2024). ReTool / ToRA — tool-integrated reasoning for math
142	- Chen et al. (2023). AgentMath — code-augmented mathematical reasoning
143	
144	---
145	
146	## Provenance: Claims → Experiments
147	
148	| Claim | Source Experiment | Key Metric |
149	|-------|------------------|------------|
150	| Δ_full=+29.60, death fraction=90.41% | plan-012-full | delta_full, death_avoidance_fraction |
151	| r=0.9698, p=8.12e-07 | plan-012-full | pearson_r, pearson_p |
152	| Baseline scores (Table 1) | plan-003-baseline | metrics per condition |
153	| Keyword heuristic failure | plan-011-rule-based | v1_match_rate, v2_match_rate |
154	| Learned router internal_recall=51.5% | plan-004-ablation-b | per_class.internal.recall |
155	| find-non-living-thing Δ=9.58 | plan-012-decomposition | key_tasks.find_non_living_thing |
156	| Episode label distribution 86/9/150 | plan-012-full | label_dist |
157	| Death rates: int 42.9%, det 16.3% | plan-012-full | death_rate_int, death_rate_det |
158	| Per-step oracle 98% tie rate | plan-012-decomposition | (derived from label_dist) |
159	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "76191722-967c-4eff-9c43-cabebc895fb6",
  "isSidechain": false,
  "promptId": "de32f0f5-b4f7-4fe9-872c-8108c929635d",
  "type": "user",
  "uuid": "ec1f8ad1-5775-40ff-ae5e-422aa186d64f",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/_project/paper/paper_outline.md",
      "content": "# EMNLP 2026 Short Paper Outline\n\n## Title Candidates\n\n1. **Death Avoidance Dominates Routing Signal: A Counterfactual Analysis of LLM Agent Tool Use in Interactive Environments**\n2. **When Does Deterministic Computation Help LLM Agents? Episode-Level Counterfactual Analysis Reveals Death Avoidance Dominance**\n3. **90% Death Avoidance: Decomposing the Routing Signal Between LLM Reasoning and Deterministic Simulation**\n\nRecommended: **Title 1** (clear claim + methodology in title; fits short paper convention of stating the finding)\n\n---\n\n## Abstract Skeleton (~150 words)\n\nKey points to cover:\n\n- **Problem**: LLM agents hallucinate state transitions in rule-governed environments, causing catastrophic failures (deaths). Routing between internal LLM reasoning and deterministic computation (simulators) can mitigate this, but what exactly does routing learn?\n- **Methodological gap**: Per-step oracle labeling degenerates in sparse-reward settings (98% tie rate on ScienceWorld). We propose episode-level counterfactual analysis.\n- **Core finding**: Death avoidance accounts for ~90% of routing signal (Δ_full=+29.60, Δ_no_death=+2.84; Pearson r=0.97, p<1e-6 across 11 task types / 245 episodes). Non-death performance is approximately equal between modalities.\n- **Supporting finding**: Keyword heuristics structurally fail (match rates degenerate to ≈always-det or ≈always-internal); episode-level counterfactual labels can train a lightweight router (internal_recall=51.5%).\n- **Implication**: The value of deterministic computation in interactive environments is concentrated in catastrophic failure prevention, not positive task guidance.\n\n---\n\n## Section Structure\n\n### 1. Introduction (0.8 pages)\n\n**Key points:**\n- LLM agents on rule-governed environments (physics, chemistry) suffer catastrophic failures from hallucinated state transitions → motivate the routing question\n- Existing work: tool-use learning (Toolformer, ART, Chameleon) learns *when* to invoke tools but doesn't analyze *what* routing learns; ITP-R routes to approximate world models but underperforms pure internal reasoning; ReTool/AgentMath use implicit routing entangled with backbone\n- Per-step oracle labeling degenerates in sparse-reward environments (98% tie rate) → need episode-level analysis\n- **Contributions** (bulleted):\n  1. Episode-level counterfactual methodology that overcomes per-step oracle degeneracy\n  2. Empirical finding: death avoidance accounts for ≥90% of routing signal on ScienceWorld (11 tasks, 245 episodes)\n  3. Structural failure analysis of keyword heuristics; demonstration that counterfactual labels can train a lightweight diagnostic router\n\n### 2. Method (1.0 pages)\n\n**Key points:**\n- **2.1 Problem Setup**: ScienceWorld environment; two computation modalities (internal LLM reasoning vs. deterministic simulation via environment forking); per-step routing decision\n- **2.2 Episode-Level Counterfactual Labeling**: Why per-step oracle fails (98% tie rate in sparse rewards) → run complete episodes under pure-internal and pure-deterministic strategies → compare episode-level scores → label: det-preferred / internal-preferred / no-preference. Distribution: 86 det-pref / 9 int-pref / 150 no-pref (245 episodes)\n- **2.3 Death Decomposition Framework**: Decompose Δ_full into death-avoidance component (Δ_death) and non-death component (Δ_nd). Death avoidance fraction = (Δ_full - Δ_nd) / Δ_full. Cross-task correlation: Pearson r between per-task death rate difference and Δ_full\n\n### 3. Experiments (1.5 pages)\n\n**Key points:**\n- **3.1 Setup**: Qwen3-1.7B backbone; ScienceWorld 11 task types × 20-40 episodes; evaluation: always-internal, always-deterministic, oracle, random, keyword heuristic, learned router\n- **3.2 Death Decomposition Results** (core result):\n  - Δ_full=+29.60, Δ_nd=+2.84, death fraction=90.41%\n  - 10/11 death-prone tasks: death-dominated gaps\n  - 1 exception: find-non-living-thing (0 deaths, Δ=+9.58 from non-death mechanisms)\n  - Pearson r=0.9698 (p=8.12e-07)\n- **3.3 Baseline Comparison**:\n  - always-internal: -37.16, always-det: -11.64, oracle: -9.03, random: -23.75\n  - Keyword heuristic: structural failure (v1 85.8% match → ≈always-det; v2 4.9% → ≈always-internal)\n  - Learned router (ablation-b): internal_recall=51.5%, first non-degenerate; classification head variants all degenerate\n- **3.4 Analysis**: Death rate: internal 42.9% vs. deterministic 16.3%; alive-episode scores nearly equal across modalities\n\n### 4. Related Work (0.5 pages, integrated or separate)\n\n**Key points:**\n- **Tool-use learning**: Toolformer (self-supervised API insertion), ART (LLM-as-router), Chameleon (LLM-as-planner), ToolkenGPT (token-level triggers). Differentiation: episode-level counterfactual labeling, safety-aware framing, explicit modular router\n- **Adaptive computation / routing**: CogRouter (RL-based), ARES, Mixture-of-Depths. Our focus: empirical analysis of *what* routing learns, not a new routing architecture\n- **World model routing**: ITP-R, Dyna-Think. Our deterministic computation is exact (simulator), not approximate (LLM world model)\n- **Agent frameworks**: ReAct, Reflexion. Orthogonal — we analyze the routing decision within an agent loop\n\n### 5. Conclusion (0.3 pages)\n\n**Key points:**\n- Summary: death avoidance ≥90% of routing signal; episode-level counterfactual analysis as diagnostic methodology\n- **Limitations**: single benchmark (ScienceWorld), episode-level granularity (not step-level), DAgger distribution shift (train on pure strategies, deploy on mixed)\n- **Future work**: step-level labeling with denser reward signals, extension to MATH/code interpretation domains, DAgger-style iterative relabeling\n\n---\n\n## Figure/Table Plan\n\n### Table 1: Baseline Comparison\n| Method | Score | 90% CI | Success Rate | Death Rate | Sim Ratio |\n|--------|-------|--------|-------------|------------|-----------|\n| Always-Internal | -37.16 | [-43.39, -31.43] | 12.4% | 40.7% | 0.00 |\n| Always-Deterministic | -11.64 | [-17.39, -6.55] | 23.7% | 18.6% | 1.00 |\n| Oracle | -9.03 | [-14.14, -4.15] | 24.2% | 16.5% | 0.96 |\n| Random | -23.75 | [-29.60, -18.11] | 16.5% | 28.4% | 0.50 |\n| Keyword Heuristic (v1) | ≈ Always-Det | — | — | — | 0.86 |\n| Keyword Heuristic (v2) | ≈ Always-Int | — | — | — | 0.05 |\n| Learned Router (implicit) | TBD | — | — | — | TBD |\n\n*Source: plan-003-baseline, plan-011-rule-based*\n\n### Figure 1: Death Decomposition (core figure)\n- **Type**: Grouped bar chart or stacked bar\n- **X-axis**: 11 task types (sorted by death fraction)\n- **Y-axis**: Score delta (deterministic − internal)\n- **Bars**: Δ_full decomposed into Δ_death (death-avoidance component, dark) and Δ_nd (non-death component, light)\n- **Highlight**: find-non-living-thing as sole exception (Δ_nd = Δ_full = 9.58, zero deaths)\n- **Annotation**: Overall death fraction = 90.41%\n\n*Source: plan-012-full*\n\n### Figure 2: Cross-task Correlation (if space permits)\n- **Type**: Scatter plot with regression line\n- **X-axis**: Per-task death rate difference (internal − deterministic)\n- **Y-axis**: Δ_full per task\n- **Regression line**: r=0.9698, p=8.12e-07\n- **11 points**, labeled by task type\n- **Purpose**: Visually demonstrates near-perfect linear relationship\n\n*Source: plan-012-full, plan-012-decomposition*\n\n**Space strategy**: Figure 1 is mandatory. Figure 2 can be merged as an inset in Figure 1, or moved to appendix if space is tight. Table 1 is mandatory. Per-task breakdown table → appendix.\n\n---\n\n## Key References\n\n### Tool-Use Learning\n- Schick et al. (2024). Toolformer: Language Models Can Teach Themselves to Use Tools. *NeurIPS*\n- Paranjape et al. (2023). ART: Automatic Multi-step Reasoning and Tool-Use. *arXiv*\n- Lu et al. (2024). Chameleon: Plug-and-Play Compositional Reasoning with Large Language Models. *NeurIPS*\n- Hao et al. (2024). ToolkenGPT: Augmenting Frozen Language Models with Massive Tools via Tool Embeddings. *NeurIPS*\n\n### Agent Routing / Adaptive Computation\n- CogRouter — RL-based cognitive routing (ScienceWorld SOTA)\n- ITP-R — imagination-based routing to LLM world model\n- ARES — adaptive routing for efficient serving\n- Raposo et al. (2024). Mixture-of-Depths. *ICML*\n\n### Agent Frameworks\n- Yao et al. (2023). ReAct: Synergizing Reasoning and Acting in Language Models. *ICLR*\n- Shinn et al. (2023). Reflexion: Language Agents with Verbal Reinforcement Learning. *NeurIPS*\n\n### Methodology\n- Ross et al. (2011). A Reduction of Imitation Learning and Structured Prediction to No-Regret Online Learning. *AISTATS* (DAgger)\n\n### Environment\n- Wang et al. (2022). ScienceWorld: Is your Agent Smarter than a 5th Grader? *EMNLP*\n\n### Code Execution Routing\n- Gou et al. (2024). ReTool / ToRA — tool-integrated reasoning for math\n- Chen et al. (2023). AgentMath — code-augmented mathematical reasoning\n\n---\n\n## Provenance: Claims → Experiments\n\n| Claim | Source Experiment | Key Metric |\n|-------|------------------|------------|\n| Δ_full=+29.60, death fraction=90.41% | plan-012-full | delta_full, death_avoidance_fraction |\n| r=0.9698, p=8.12e-07 | plan-012-full | pearson_r, pearson_p |\n| Baseline scores (Table 1) | plan-003-baseline | metrics per condition |\n| Keyword heuristic failure | plan-011-rule-based | v1_match_rate, v2_match_rate |\n| Learned router internal_recall=51.5% | plan-004-ablation-b | per_class.internal.recall |\n| find-non-living-thing Δ=9.58 | plan-012-decomposition | key_tasks.find_non_living_thing |\n| Episode label distribution 86/9/150 | plan-012-full | label_dist |\n| Death rates: int 42.9%, det 16.3% | plan-012-full | death_rate_int, death_rate_det |\n| Per-step oracle 98% tie rate | plan-012-decomposition | (derived from label_dist) |\n",
      "numLines": 159,
      "startLine": 1,
      "totalLines": 159
    }
  },
  "sourceToolAssistantUUID": "76191722-967c-4eff-9c43-cabebc895fb6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing",
  "sessionId": "fe1af098-4ed4-4fac-9d28-af54a02d46ce",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 19_

```json
{
  "type": "last-prompt",
  "leafUuid": "ec1f8ad1-5775-40ff-ae5e-422aa186d64f",
  "sessionId": "fe1af098-4ed4-4fac-9d28-af54a02d46ce"
}
```

---

### Runtime record

_source line 20_

```json
{
  "type": "ai-title",
  "aiTitle": "Update paper_outline.md baseline numbers to 245-ep",
  "sessionId": "fe1af098-4ed4-4fac-9d28-af54a02d46ce"
}
```

---

### Assistant

_source line 21 · 2026-05-14T08:21:00.319Z_

<details><summary>Logged reasoning block</summary>

```text
Now I need to update the baseline numbers from the 194-ep to 245-ep values. Let me identify all the numbers that need changing:

1. **Baseline scores (Table 1 and text references)**:
   - always-internal: -37.16 → -39.07
   - always-deterministic: -11.64 → -9.47
   - oracle: -9.03 → -6.58
   - random: -23.75 → -22.38

2. **Other numbers to update**:
   - Δ_full: 29.60 → 29.60 (same? Let me check... 

Actually, looking at the file, most of these other values are already correct—Δ_full, Δ_nd, DAF, r, and p all match what's in the document, and the episode count is already listed as 245. I just need to focus on updating those four baseline scores in Table 1 and wherever they're referenced in the text. I'm checking through the specific lines that need updates—most of the decomposition metrics are already correct at the 245-episode values, but I need to add the sample size annotation to the find-non-living-thing result and verify the baseline scores on line 55 actually get replaced. The death rate percentages and confidence interval values in the table also need verification to see if they shift with the new dataset.

Wait, I'm realizing the key issue: the baseline numbers come from plan-003-baseline-245eps, not plan-012-full, so the annotation instruction about attributing everything to plan-012-full might not apply uniformly to those baseline values. Let me clarify what exactly needs the source annotation. I'm wrestling with whether to use the literal annotation instruction for all numbers or apply appropriate provenance tags based on where each number actually comes from. The baseline values come from plan-003-baseline-245eps, while the decomposition numbers come from plan-012-full, so using mismatched tags would be inaccurate. But the task explicitly says to annotate everything with `[A: plan-012-full, 245eps/11tasks]`. I think I need to follow the literal instruction for the decomposition numbers while using the correct provenance tag for baselines. I'm settling on using `[A: plan-003-baseline-245eps]` for the baseline numbers and `[A: plan-012-full, 245eps/11tasks]` for the decomposition metrics. Now I need to locate and update the baseline values in a few key places: the initial list on line 55, the scores in Table 1, and the source annotation. For the confidence intervals in the table, I'll leave them as-is since I don't have updated values for those.

Looking through the file, I notice the decomposition numbers were already updated to reflect 11 task types and 245 episodes, but the baselines weren't. I also need to add the sample size annotation for find-non-living-thing.

Now I'm going through the edits systematically: updating the baseline scores in line 55 with annotations, revising Table 1 scores and adding annotations to lines 81-85, inserting n=40 for find-non-living-thing on line 52, and adding annotations to the statistical values on lines 50 and 53.

I should also verify the abstract numbers on line 19 are correct—they look accurate, though I'm considering whether to add annotations there too since the task requires annotating each number. The abstract uses rounded values like r=0.97 instead of the full precision, which is appropriate for a summary. I'll add annotations to maintain consistency across the document, then update line 90 to include the 245 episodes reference in the source annotation.

Rather than rewriting the entire file, I'll make targeted edits for each change since that's easier to verify and track.

For the first edit, I'm updating the abstract's core finding to include the death avoidance factor percentage and add the annotation reference.

For the second edit, I'm adding the same annotation to the contributions section where the 11 tasks and 245 episodes are mentioned.

For the third edit, I'm updating the label distribution line with the corrected episode count and annotation.

For the fourth edit, I'm adding the annotation to the core result numbers showing the performance improvements and death fraction.

For the fifth edit, I'm adding the sample size and annotation to the find-non-living-thing task result.

For the sixth edit, I'm appending the annotation to the Pearson correlation coefficient.

For the seventh edit, I'm updating the baseline scores with new values from a different experimental plan and adding its annotation.

For the eighth edit, I need to update the scores in Table 1 rows.

Now I'm looking at the table rows for the baseline methods—I need to update the score values while keeping the confidence intervals and other metrics as they are, since I don't have new CI, success rate, or death rate data yet.

I'm also updating the source annotation to reference the new 245-episode baseline run and adding a clarification note. For the death rate comparison, those figures are already from the 245-episode run so they should be accurate—I'll just add the proper annotation to confirm that.

Now I need to reconsider my approach: the save_project_file function won't work for paper_outline.md since it's not whitelisted, so I'll write directly to the filesystem instead. Given how many edits there are, it'll be cleaner to prepare and write out the full updated file content.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ec1f8ad1-5775-40ff-ae5e-422aa186d64f",
  "isSidechain": false,
  "requestId": "req_011Cb28kzDuJ4mtwf5YBhvoZ",
  "type": "assistant",
  "uuid": "0f898d26-ea14-401b-bdae-3b5fd75b766c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing",
  "sessionId": "fe1af098-4ed4-4fac-9d28-af54a02d46ce",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MveK5356e6qtftBVdPmCCg",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3543,
      "cache_read_input_tokens": 24387,
      "output_tokens": 4248,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3543,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 4248,
          "cache_read_input_tokens": 24387,
          "cache_creation_input_tokens": 3543,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3543
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

_source line 22 · 2026-05-14T08:21:00.322Z_

文件已读取。现在逐项替换 baseline 数字并添加 provenance 标注。共有多处需要修改。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0f898d26-ea14-401b-bdae-3b5fd75b766c",
  "isSidechain": false,
  "requestId": "req_011Cb28kzDuJ4mtwf5YBhvoZ",
  "type": "assistant",
  "uuid": "23fe5f70-8c69-4380-8116-16faad8c2cd3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing",
  "sessionId": "fe1af098-4ed4-4fac-9d28-af54a02d46ce",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MveK5356e6qtftBVdPmCCg",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3543,
      "cache_read_input_tokens": 24387,
      "output_tokens": 4248,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3543,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 4248,
          "cache_read_input_tokens": 24387,
          "cache_creation_input_tokens": 3543,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3543
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

_source line 23 · 2026-05-14T08:21:01.831Z_

<details open><summary>🔧 Tool call — Edit · `toolu_01KNDtmVg6dizGXuPYyD6WxQ`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/_project/paper/paper_outline.md",
  "old_string": "- **Core finding**: Death avoidance accounts for ~90% of routing signal (Δ_full=+29.60, Δ_no_death=+2.84; Pearson r=0.97, p<1e-6 across 11 task types / 245 episodes). Non-death performance is approximately equal between modalities.",
  "new_string": "- **Core finding**: Death avoidance accounts for ~90% of routing signal (Δ_full=+29.60, Δ_no_death=+2.84, DAF=90.41%; Pearson r=0.97, p<1e-6 across 11 task types / 245 episodes) [A: plan-012-full, 245eps/11tasks]. Non-death performance is approximately equal between modalities."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "23fe5f70-8c69-4380-8116-16faad8c2cd3",
  "isSidechain": false,
  "requestId": "req_011Cb28kzDuJ4mtwf5YBhvoZ",
  "type": "assistant",
  "uuid": "0ccf20df-f24e-4ba7-b298-53722d6a11d6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing",
  "sessionId": "fe1af098-4ed4-4fac-9d28-af54a02d46ce",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MveK5356e6qtftBVdPmCCg",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3543,
      "cache_read_input_tokens": 24387,
      "output_tokens": 4248,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3543,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 4248,
          "cache_read_input_tokens": 24387,
          "cache_creation_input_tokens": 3543,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3543
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

_source line 24 · 2026-05-14T08:21:01.860Z_

<details><summary>↩ Tool result · `toolu_01KNDtmVg6dizGXuPYyD6WxQ`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/_project/paper/paper_outline.md has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0ccf20df-f24e-4ba7-b298-53722d6a11d6",
  "isSidechain": false,
  "promptId": "de32f0f5-b4f7-4fe9-872c-8108c929635d",
  "type": "user",
  "uuid": "66d4f43e-125c-4ee8-a79f-758bc39bfd10",
  "toolUseResult": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/_project/paper/paper_outline.md",
    "oldString": "- **Core finding**: Death avoidance accounts for ~90% of routing signal (Δ_full=+29.60, Δ_no_death=+2.84; Pearson r=0.97, p<1e-6 across 11 task types / 245 episodes). Non-death performance is approximately equal between modalities.",
    "newString": "- **Core finding**: Death avoidance accounts for ~90% of routing signal (Δ_full=+29.60, Δ_no_death=+2.84, DAF=90.41%; Pearson r=0.97, p<1e-6 across 11 task types / 245 episodes) [A: plan-012-full, 245eps/11tasks]. Non-death performance is approximately equal between modalities.",
    "originalFile": "# EMNLP 2026 Short Paper Outline\n\n## Title Candidates\n\n1. **Death Avoidance Dominates Routing Signal: A Counterfactual Analysis of LLM Agent Tool Use in Interactive Environments**\n2. **When Does Deterministic Computation Help LLM Agents? Episode-Level Counterfactual Analysis Reveals Death Avoidance Dominance**\n3. **90% Death Avoidance: Decomposing the Routing Signal Between LLM Reasoning and Deterministic Simulation**\n\nRecommended: **Title 1** (clear claim + methodology in title; fits short paper convention of stating the finding)\n\n---\n\n## Abstract Skeleton (~150 words)\n\nKey points to cover:\n\n- **Problem**: LLM agents hallucinate state transitions in rule-governed environments, causing catastrophic failures (deaths). Routing between internal LLM reasoning and deterministic computation (simulators) can mitigate this, but what exactly does routing learn?\n- **Methodological gap**: Per-step oracle labeling degenerates in sparse-reward settings (98% tie rate on ScienceWorld). We propose episode-level counterfactual analysis.\n- **Core finding**: Death avoidance accounts for ~90% of routing signal (Δ_full=+29.60, Δ_no_death=+2.84; Pearson r=0.97, p<1e-6 across 11 task types / 245 episodes). Non-death performance is approximately equal between modalities.\n- **Supporting finding**: Keyword heuristics structurally fail (match rates degenerate to ≈always-det or ≈always-internal); episode-level counterfactual labels can train a lightweight router (internal_recall=51.5%).\n- **Implication**: The value of deterministic computation in interactive environments is concentrated in catastrophic failure prevention, not positive task guidance.\n\n---\n\n## Section Structure\n\n### 1. Introduction (0.8 pages)\n\n**Key points:**\n- LLM agents on rule-governed environments (physics, chemistry) suffer catastrophic failures from hallucinated state transitions → motivate the routing question\n- Existing work: tool-use learning (Toolformer, ART, Chameleon) learns *when* to invoke tools but doesn't analyze *what* routing learns; ITP-R routes to approximate world models but underperforms pure internal reasoning; ReTool/AgentMath use implicit routing entangled with backbone\n- Per-step oracle labeling degenerates in sparse-reward environments (98% tie rate) → need episode-level analysis\n- **Contributions** (bulleted):\n  1. Episode-level counterfactual methodology that overcomes per-step oracle degeneracy\n  2. Empirical finding: death avoidance accounts for ≥90% of routing signal on ScienceWorld (11 tasks, 245 episodes)\n  3. Structural failure analysis of keyword heuristics; demonstration that counterfactual labels can train a lightweight diagnostic router\n\n### 2. Method (1.0 pages)\n\n**Key points:**\n- **2.1 Problem Setup**: ScienceWorld environment; two computation modalities (internal LLM reasoning vs. deterministic simulation via environment forking); per-step routing decision\n- **2.2 Episode-Level Counterfactual Labeling**: Why per-step oracle fails (98% tie rate in sparse rewards) → run complete episodes under pure-internal and pure-deterministic strategies → compare episode-level scores → label: det-preferred / internal-preferred / no-preference. Distribution: 86 det-pref / 9 int-pref / 150 no-pref (245 episodes)\n- **2.3 Death Decomposition Framework**: Decompose Δ_full into death-avoidance component (Δ_death) and non-death component (Δ_nd). Death avoidance fraction = (Δ_full - Δ_nd) / Δ_full. Cross-task correlation: Pearson r between per-task death rate difference and Δ_full\n\n### 3. Experiments (1.5 pages)\n\n**Key points:**\n- **3.1 Setup**: Qwen3-1.7B backbone; ScienceWorld 11 task types × 20-40 episodes; evaluation: always-internal, always-deterministic, oracle, random, keyword heuristic, learned router\n- **3.2 Death Decomposition Results** (core result):\n  - Δ_full=+29.60, Δ_nd=+2.84, death fraction=90.41%\n  - 10/11 death-prone tasks: death-dominated gaps\n  - 1 exception: find-non-living-thing (0 deaths, Δ=+9.58 from non-death mechanisms)\n  - Pearson r=0.9698 (p=8.12e-07)\n- **3.3 Baseline Comparison**:\n  - always-internal: -37.16, always-det: -11.64, oracle: -9.03, random: -23.75\n  - Keyword heuristic: structural failure (v1 85.8% match → ≈always-det; v2 4.9% → ≈always-internal)\n  - Learned router (ablation-b): internal_recall=51.5%, first non-degenerate; classification head variants all degenerate\n- **3.4 Analysis**: Death rate: internal 42.9% vs. deterministic 16.3%; alive-episode scores nearly equal across modalities\n\n### 4. Related Work (0.5 pages, integrated or separate)\n\n**Key points:**\n- **Tool-use learning**: Toolformer (self-supervised API insertion), ART (LLM-as-router), Chameleon (LLM-as-planner), ToolkenGPT (token-level triggers). Differentiation: episode-level counterfactual labeling, safety-aware framing, explicit modular router\n- **Adaptive computation / routing**: CogRouter (RL-based), ARES, Mixture-of-Depths. Our focus: empirical analysis of *what* routing learns, not a new routing architecture\n- **World model routing**: ITP-R, Dyna-Think. Our deterministic computation is exact (simulator), not approximate (LLM world model)\n- **Agent frameworks**: ReAct, Reflexion. Orthogonal — we analyze the routing decision within an agent loop\n\n### 5. Conclusion (0.3 pages)\n\n**Key points:**\n- Summary: death avoidance ≥90% of routing signal; episode-level counterfactual analysis as diagnostic methodology\n- **Limitations**: single benchmark (ScienceWorld), episode-level granularity (not step-level), DAgger distribution shift (train on pure strategies, deploy on mixed)\n- **Future work**: step-level labeling with denser reward signals, extension to MATH/code interpretation domains, DAgger-style iterative relabeling\n\n---\n\n## Figure/Table Plan\n\n### Table 1: Baseline Comparison\n| Method | Score | 90% CI | Success Rate | Death Rate | Sim Ratio |\n|--------|-------|--------|-------------|------------|-----------|\n| Always-Internal | -37.16 | [-43.39, -31.43] | 12.4% | 40.7% | 0.00 |\n| Always-Deterministic | -11.64 | [-17.39, -6.55] | 23.7% | 18.6% | 1.00 |\n| Oracle | -9.03 | [-14.14, -4.15] | 24.2% | 16.5% | 0.96 |\n| Random | -23.75 | [-29.60, -18.11] | 16.5% | 28.4% | 0.50 |\n| Keyword Heuristic (v1) | ≈ Always-Det | — | — | — | 0.86 |\n| Keyword Heuristic (v2) | ≈ Always-Int | — | — | — | 0.05 |\n| Learned Router (implicit) | TBD | — | — | — | TBD |\n\n*Source: plan-003-baseline, plan-011-rule-based*\n\n### Figure 1: Death Decomposition (core figure)\n- **Type**: Grouped bar chart or stacked bar\n- **X-axis**: 11 task types (sorted by death fraction)\n- **Y-axis**: Score delta (deterministic − internal)\n- **Bars**: Δ_full decomposed into Δ_death (death-avoidance component, dark) and Δ_nd (non-death component, light)\n- **Highlight**: find-non-living-thing as sole exception (Δ_nd = Δ_full = 9.58, zero deaths)\n- **Annotation**: Overall death fraction = 90.41%\n\n*Source: plan-012-full*\n\n### Figure 2: Cross-task Correlation (if space permits)\n- **Type**: Scatter plot with regression line\n- **X-axis**: Per-task death rate difference (internal − deterministic)\n- **Y-axis**: Δ_full per task\n- **Regression line**: r=0.9698, p=8.12e-07\n- **11 points**, labeled by task type\n- **Purpose**: Visually demonstrates near-perfect linear relationship\n\n*Source: plan-012-full, plan-012-decomposition*\n\n**Space strategy**: Figure 1 is mandatory. Figure 2 can be merged as an inset in Figure 1, or moved to appendix if space is tight. Table 1 is mandatory. Per-task breakdown table → appendix.\n\n---\n\n## Key References\n\n### Tool-Use Learning\n- Schick et al. (2024). Toolformer: Language Models Can Teach Themselves to Use Tools. *NeurIPS*\n- Paranjape et al. (2023). ART: Automatic Multi-step Reasoning and Tool-Use. *arXiv*\n- Lu et al. (2024). Chameleon: Plug-and-Play Compositional Reasoning with Large Language Models. *NeurIPS*\n- Hao et al. (2024). ToolkenGPT: Augmenting Frozen Language Models with Massive Tools via Tool Embeddings. *NeurIPS*\n\n### Agent Routing / Adaptive Computation\n- CogRouter — RL-based cognitive routing (ScienceWorld SOTA)\n- ITP-R — imagination-based routing to LLM world model\n- ARES — adaptive routing for efficient serving\n- Raposo et al. (2024). Mixture-of-Depths. *ICML*\n\n### Agent Frameworks\n- Yao et al. (2023). ReAct: Synergizing Reasoning and Acting in Language Models. *ICLR*\n- Shinn et al. (2023). Reflexion: Language Agents with Verbal Reinforcement Learning. *NeurIPS*\n\n### Methodology\n- Ross et al. (2011). A Reduction of Imitation Learning and Structured Prediction to No-Regret Online Learning. *AISTATS* (DAgger)\n\n### Environment\n- Wang et al. (2022). ScienceWorld: Is your Agent Smarter than a 5th Grader? *EMNLP*\n\n### Code Execution Routing\n- Gou et al. (2024). ReTool / ToRA — tool-integrated reasoning for math\n- Chen et al. (2023). AgentMath — code-augmented mathematical reasoning\n\n---\n\n## Provenance: Claims → Experiments\n\n| Claim | Source Experiment | Key Metric |\n|-------|------------------|------------|\n| Δ_full=+29.60, death fraction=90.41% | plan-012-full | delta_full, death_avoidance_fraction |\n| r=0.9698, p=8.12e-07 | plan-012-full | pearson_r, pearson_p |\n| Baseline scores (Table 1) | plan-003-baseline | metrics per condition |\n| Keyword heuristic failure | plan-011-rule-based | v1_match_rate, v2_match_rate |\n| Learned router internal_recall=51.5% | plan-004-ablation-b | per_class.internal.recall |\n| find-non-living-thing Δ=9.58 | plan-012-decomposition | key_tasks.find_non_living_thing |\n| Episode label distribution 86/9/150 | plan-012-full | label_dist |\n| Death rates: int 42.9%, det 16.3% | plan-012-full | death_rate_int, death_rate_det |\n| Per-step oracle 98% tie rate | plan-012-decomposition | (derived from label_dist) |\n",
    "structuredPatch": [
      {
        "oldStart": 16,
        "oldLines": 7,
        "newStart": 16,
        "newLines": 7,
        "lines": [
          " ",
          " - **Problem**: LLM agents hallucinate state transitions in rule-governed environments, causing catastrophic failures (deaths). Routing between internal LLM reasoning and deterministic computation (simulators) can mitigate this, but what exactly does routing learn?",
          " - **Methodological gap**: Per-step oracle labeling degenerates in sparse-reward settings (98% tie rate on ScienceWorld). We propose episode-level counterfactual analysis.",
          "-- **Core finding**: Death avoidance accounts for ~90% of routing signal (Δ_full=+29.60, Δ_no_death=+2.84; Pearson r=0.97, p<1e-6 across 11 task types / 245 episodes). Non-death performance is approximately equal between modalities.",
          "+- **Core finding**: Death avoidance accounts for ~90% of routing signal (Δ_full=+29.60, Δ_no_death=+2.84, DAF=90.41%; Pearson r=0.97, p<1e-6 across 11 task types / 245 episodes) [A: plan-012-full, 245eps/11tasks]. Non-death performance is approximately equal between modalities.",
          " - **Supporting finding**: Keyword heuristics structurally fail (match rates degenerate to ≈always-det or ≈always-internal); episode-level counterfactual labels can train a lightweight router (internal_recall=51.5%).",
          " - **Implication**: The value of deterministic computation in interactive environments is concentrated in catastrophic failure prevention, not positive task guidance.",
          " "
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  },
  "sourceToolAssistantUUID": "0ccf20df-f24e-4ba7-b298-53722d6a11d6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing",
  "sessionId": "fe1af098-4ed4-4fac-9d28-af54a02d46ce",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 25_

```json
{
  "type": "last-prompt",
  "leafUuid": "66d4f43e-125c-4ee8-a79f-758bc39bfd10",
  "sessionId": "fe1af098-4ed4-4fac-9d28-af54a02d46ce"
}
```

---

### Runtime record

_source line 26_

```json
{
  "type": "ai-title",
  "aiTitle": "Update paper_outline.md baseline numbers to 245-ep",
  "sessionId": "fe1af098-4ed4-4fac-9d28-af54a02d46ce"
}
```

---

### Tool call

_source line 27 · 2026-05-14T08:21:05.838Z_

<details open><summary>🔧 Tool call — Edit · `toolu_017vLZ6mnvpY8Hv2mdbnSdpp`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/_project/paper/paper_outline.md",
  "old_string": "death avoidance accounts for ≥90% of routing signal on ScienceWorld (11 tasks, 245 episodes)",
  "new_string": "death avoidance accounts for ≥90% of routing signal on ScienceWorld (11 tasks, 245 episodes) [A: plan-012-full, 245eps/11tasks]"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "66d4f43e-125c-4ee8-a79f-758bc39bfd10",
  "isSidechain": false,
  "requestId": "req_011Cb28qw4Y6tif17Hkmaw4j",
  "type": "assistant",
  "uuid": "1e75ea73-5545-4d64-ac12-18b125e6dfea",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing",
  "sessionId": "fe1af098-4ed4-4fac-9d28-af54a02d46ce",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CknugctUQ5GZwYcQ11AC6o",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4321,
      "cache_read_input_tokens": 27930,
      "output_tokens": 202,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4321,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 202,
          "cache_read_input_tokens": 27930,
          "cache_creation_input_tokens": 4321,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4321
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

_source line 28 · 2026-05-14T08:21:05.851Z_

<details><summary>↩ Tool result · `toolu_017vLZ6mnvpY8Hv2mdbnSdpp`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/_project/paper/paper_outline.md has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1e75ea73-5545-4d64-ac12-18b125e6dfea",
  "isSidechain": false,
  "promptId": "de32f0f5-b4f7-4fe9-872c-8108c929635d",
  "type": "user",
  "uuid": "7b8a39fa-bd5c-432d-b381-aad91d4021a9",
  "toolUseResult": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/_project/paper/paper_outline.md",
    "oldString": "death avoidance accounts for ≥90% of routing signal on ScienceWorld (11 tasks, 245 episodes)",
    "newString": "death avoidance accounts for ≥90% of routing signal on ScienceWorld (11 tasks, 245 episodes) [A: plan-012-full, 245eps/11tasks]",
    "originalFile": "# EMNLP 2026 Short Paper Outline\n\n## Title Candidates\n\n1. **Death Avoidance Dominates Routing Signal: A Counterfactual Analysis of LLM Agent Tool Use in Interactive Environments**\n2. **When Does Deterministic Computation Help LLM Agents? Episode-Level Counterfactual Analysis Reveals Death Avoidance Dominance**\n3. **90% Death Avoidance: Decomposing the Routing Signal Between LLM Reasoning and Deterministic Simulation**\n\nRecommended: **Title 1** (clear claim + methodology in title; fits short paper convention of stating the finding)\n\n---\n\n## Abstract Skeleton (~150 words)\n\nKey points to cover:\n\n- **Problem**: LLM agents hallucinate state transitions in rule-governed environments, causing catastrophic failures (deaths). Routing between internal LLM reasoning and deterministic computation (simulators) can mitigate this, but what exactly does routing learn?\n- **Methodological gap**: Per-step oracle labeling degenerates in sparse-reward settings (98% tie rate on ScienceWorld). We propose episode-level counterfactual analysis.\n- **Core finding**: Death avoidance accounts for ~90% of routing signal (Δ_full=+29.60, Δ_no_death=+2.84, DAF=90.41%; Pearson r=0.97, p<1e-6 across 11 task types / 245 episodes) [A: plan-012-full, 245eps/11tasks]. Non-death performance is approximately equal between modalities.\n- **Supporting finding**: Keyword heuristics structurally fail (match rates degenerate to ≈always-det or ≈always-internal); episode-level counterfactual labels can train a lightweight router (internal_recall=51.5%).\n- **Implication**: The value of deterministic computation in interactive environments is concentrated in catastrophic failure prevention, not positive task guidance.\n\n---\n\n## Section Structure\n\n### 1. Introduction (0.8 pages)\n\n**Key points:**\n- LLM agents on rule-governed environments (physics, chemistry) suffer catastrophic failures from hallucinated state transitions → motivate the routing question\n- Existing work: tool-use learning (Toolformer, ART, Chameleon) learns *when* to invoke tools but doesn't analyze *what* routing learns; ITP-R routes to approximate world models but underperforms pure internal reasoning; ReTool/AgentMath use implicit routing entangled with backbone\n- Per-step oracle labeling degenerates in sparse-reward environments (98% tie rate) → need episode-level analysis\n- **Contributions** (bulleted):\n  1. Episode-level counterfactual methodology that overcomes per-step oracle degeneracy\n  2. Empirical finding: death avoidance accounts for ≥90% of routing signal on ScienceWorld (11 tasks, 245 episodes)\n  3. Structural failure analysis of keyword heuristics; demonstration that counterfactual labels can train a lightweight diagnostic router\n\n### 2. Method (1.0 pages)\n\n**Key points:**\n- **2.1 Problem Setup**: ScienceWorld environment; two computation modalities (internal LLM reasoning vs. deterministic simulation via environment forking); per-step routing decision\n- **2.2 Episode-Level Counterfactual Labeling**: Why per-step oracle fails (98% tie rate in sparse rewards) → run complete episodes under pure-internal and pure-deterministic strategies → compare episode-level scores → label: det-preferred / internal-preferred / no-preference. Distribution: 86 det-pref / 9 int-pref / 150 no-pref (245 episodes)\n- **2.3 Death Decomposition Framework**: Decompose Δ_full into death-avoidance component (Δ_death) and non-death component (Δ_nd). Death avoidance fraction = (Δ_full - Δ_nd) / Δ_full. Cross-task correlation: Pearson r between per-task death rate difference and Δ_full\n\n### 3. Experiments (1.5 pages)\n\n**Key points:**\n- **3.1 Setup**: Qwen3-1.7B backbone; ScienceWorld 11 task types × 20-40 episodes; evaluation: always-internal, always-deterministic, oracle, random, keyword heuristic, learned router\n- **3.2 Death Decomposition Results** (core result):\n  - Δ_full=+29.60, Δ_nd=+2.84, death fraction=90.41%\n  - 10/11 death-prone tasks: death-dominated gaps\n  - 1 exception: find-non-living-thing (0 deaths, Δ=+9.58 from non-death mechanisms)\n  - Pearson r=0.9698 (p=8.12e-07)\n- **3.3 Baseline Comparison**:\n  - always-internal: -37.16, always-det: -11.64, oracle: -9.03, random: -23.75\n  - Keyword heuristic: structural failure (v1 85.8% match → ≈always-det; v2 4.9% → ≈always-internal)\n  - Learned router (ablation-b): internal_recall=51.5%, first non-degenerate; classification head variants all degenerate\n- **3.4 Analysis**: Death rate: internal 42.9% vs. deterministic 16.3%; alive-episode scores nearly equal across modalities\n\n### 4. Related Work (0.5 pages, integrated or separate)\n\n**Key points:**\n- **Tool-use learning**: Toolformer (self-supervised API insertion), ART (LLM-as-router), Chameleon (LLM-as-planner), ToolkenGPT (token-level triggers). Differentiation: episode-level counterfactual labeling, safety-aware framing, explicit modular router\n- **Adaptive computation / routing**: CogRouter (RL-based), ARES, Mixture-of-Depths. Our focus: empirical analysis of *what* routing learns, not a new routing architecture\n- **World model routing**: ITP-R, Dyna-Think. Our deterministic computation is exact (simulator), not approximate (LLM world model)\n- **Agent frameworks**: ReAct, Reflexion. Orthogonal — we analyze the routing decision within an agent loop\n\n### 5. Conclusion (0.3 pages)\n\n**Key points:**\n- Summary: death avoidance ≥90% of routing signal; episode-level counterfactual analysis as diagnostic methodology\n- **Limitations**: single benchmark (ScienceWorld), episode-level granularity (not step-level), DAgger distribution shift (train on pure strategies, deploy on mixed)\n- **Future work**: step-level labeling with denser reward signals, extension to MATH/code interpretation domains, DAgger-style iterative relabeling\n\n---\n\n## Figure/Table Plan\n\n### Table 1: Baseline Comparison\n| Method | Score | 90% CI | Success Rate | Death Rate | Sim Ratio |\n|--------|-------|--------|-------------|------------|-----------|\n| Always-Internal | -37.16 | [-43.39, -31.43] | 12.4% | 40.7% | 0.00 |\n| Always-Deterministic | -11.64 | [-17.39, -6.55] | 23.7% | 18.6% | 1.00 |\n| Oracle | -9.03 | [-14.14, -4.15] | 24.2% | 16.5% | 0.96 |\n| Random | -23.75 | [-29.60, -18.11] | 16.5% | 28.4% | 0.50 |\n| Keyword Heuristic (v1) | ≈ Always-Det | — | — | — | 0.86 |\n| Keyword Heuristic (v2) | ≈ Always-Int | — | — | — | 0.05 |\n| Learned Router (implicit) | TBD | — | — | — | TBD |\n\n*Source: plan-003-baseline, plan-011-rule-based*\n\n### Figure 1: Death Decomposition (core figure)\n- **Type**: Grouped bar chart or stacked bar\n- **X-axis**: 11 task types (sorted by death fraction)\n- **Y-axis**: Score delta (deterministic − internal)\n- **Bars**: Δ_full decomposed into Δ_death (death-avoidance component, dark) and Δ_nd (non-death component, light)\n- **Highlight**: find-non-living-thing as sole exception (Δ_nd = Δ_full = 9.58, zero deaths)\n- **Annotation**: Overall death fraction = 90.41%\n\n*Source: plan-012-full*\n\n### Figure 2: Cross-task Correlation (if space permits)\n- **Type**: Scatter plot with regression line\n- **X-axis**: Per-task death rate difference (internal − deterministic)\n- **Y-axis**: Δ_full per task\n- **Regression line**: r=0.9698, p=8.12e-07\n- **11 points**, labeled by task type\n- **Purpose**: Visually demonstrates near-perfect linear relationship\n\n*Source: plan-012-full, plan-012-decomposition*\n\n**Space strategy**: Figure 1 is mandatory. Figure 2 can be merged as an inset in Figure 1, or moved to appendix if space is tight. Table 1 is mandatory. Per-task breakdown table → appendix.\n\n---\n\n## Key References\n\n### Tool-Use Learning\n- Schick et al. (2024). Toolformer: Language Models Can Teach Themselves to Use Tools. *NeurIPS*\n- Paranjape et al. (2023). ART: Automatic Multi-step Reasoning and Tool-Use. *arXiv*\n- Lu et al. (2024). Chameleon: Plug-and-Play Compositional Reasoning with Large Language Models. *NeurIPS*\n- Hao et al. (2024). ToolkenGPT: Augmenting Frozen Language Models with Massive Tools via Tool Embeddings. *NeurIPS*\n\n### Agent Routing / Adaptive Computation\n- CogRouter — RL-based cognitive routing (ScienceWorld SOTA)\n- ITP-R — imagination-based routing to LLM world model\n- ARES — adaptive routing for efficient serving\n- Raposo et al. (2024). Mixture-of-Depths. *ICML*\n\n### Agent Frameworks\n- Yao et al. (2023). ReAct: Synergizing Reasoning and Acting in Language Models. *ICLR*\n- Shinn et al. (2023). Reflexion: Language Agents with Verbal Reinforcement Learning. *NeurIPS*\n\n### Methodology\n- Ross et al. (2011). A Reduction of Imitation Learning and Structured Prediction to No-Regret Online Learning. *AISTATS* (DAgger)\n\n### Environment\n- Wang et al. (2022). ScienceWorld: Is your Agent Smarter than a 5th Grader? *EMNLP*\n\n### Code Execution Routing\n- Gou et al. (2024). ReTool / ToRA — tool-integrated reasoning for math\n- Chen et al. (2023). AgentMath — code-augmented mathematical reasoning\n\n---\n\n## Provenance: Claims → Experiments\n\n| Claim | Source Experiment | Key Metric |\n|-------|------------------|------------|\n| Δ_full=+29.60, death fraction=90.41% | plan-012-full | delta_full, death_avoidance_fraction |\n| r=0.9698, p=8.12e-07 | plan-012-full | pearson_r, pearson_p |\n| Baseline scores (Table 1) | plan-003-baseline | metrics per condition |\n| Keyword heuristic failure | plan-011-rule-based | v1_match_rate, v2_match_rate |\n| Learned router internal_recall=51.5% | plan-004-ablation-b | per_class.internal.recall |\n| find-non-living-thing Δ=9.58 | plan-012-decomposition | key_tasks.find_non_living_thing |\n| Episode label distribution 86/9/150 | plan-012-full | label_dist |\n| Death rates: int 42.9%, det 16.3% | plan-012-full | death_rate_int, death_rate_det |\n| Per-step oracle 98% tie rate | plan-012-decomposition | (derived from label_dist) |\n",
    "structuredPatch": [
      {
        "oldStart": 32,
        "oldLines": 7,
        "newStart": 32,
        "newLines": 7,
        "lines": [
          " - Per-step oracle labeling degenerates in sparse-reward environments (98% tie rate) → need episode-level analysis",
          " - **Contributions** (bulleted):",
          "   1. Episode-level counterfactual methodology that overcomes per-step oracle degeneracy",
          "-  2. Empirical finding: death avoidance accounts for ≥90% of routing signal on ScienceWorld (11 tasks, 245 episodes)",
          "+  2. Empirical finding: death avoidance accounts for ≥90% of routing signal on ScienceWorld (11 tasks, 245 episodes) [A: plan-012-full, 245eps/11tasks]",
          "   3. Structural failure analysis of keyword heuristics; demonstration that counterfactual labels can train a lightweight diagnostic router",
          " ",
          " ### 2. Method (1.0 pages)"
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  },
  "sourceToolAssistantUUID": "1e75ea73-5545-4d64-ac12-18b125e6dfea",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing",
  "sessionId": "fe1af098-4ed4-4fac-9d28-af54a02d46ce",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-14T08:21:09.557Z_

<details open><summary>🔧 Tool call — Edit · `toolu_01Myq7wD39UBUNPA7DxM6yXU`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/_project/paper/paper_outline.md",
  "old_string": "86 det-pref / 9 int-pref / 150 no-pref (245 episodes)",
  "new_string": "86 det-pref / 9 int-pref / 150 no-pref (245 episodes) [A: plan-012-full, 245eps/11tasks]"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7b8a39fa-bd5c-432d-b381-aad91d4021a9",
  "isSidechain": false,
  "requestId": "req_011Cb28rESZYuquun1bsTXfU",
  "type": "assistant",
  "uuid": "c3ce405e-2c92-4183-b01f-86fd26ded850",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing",
  "sessionId": "fe1af098-4ed4-4fac-9d28-af54a02d46ce",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Nr36XihcE8QpjbrPjT2mSU",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 280,
      "cache_read_input_tokens": 32251,
      "output_tokens": 217,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 280,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 217,
          "cache_read_input_tokens": 32251,
          "cache_creation_input_tokens": 280,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 280
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

_source line 30 · 2026-05-14T08:21:09.570Z_

<details><summary>↩ Tool result · `toolu_01Myq7wD39UBUNPA7DxM6yXU`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/_project/paper/paper_outline.md has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c3ce405e-2c92-4183-b01f-86fd26ded850",
  "isSidechain": false,
  "promptId": "de32f0f5-b4f7-4fe9-872c-8108c929635d",
  "type": "user",
  "uuid": "93480bca-3898-4dd0-8b27-ad5db60cc572",
  "toolUseResult": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/_project/paper/paper_outline.md",
    "oldString": "86 det-pref / 9 int-pref / 150 no-pref (245 episodes)",
    "newString": "86 det-pref / 9 int-pref / 150 no-pref (245 episodes) [A: plan-012-full, 245eps/11tasks]",
    "originalFile": "# EMNLP 2026 Short Paper Outline\n\n## Title Candidates\n\n1. **Death Avoidance Dominates Routing Signal: A Counterfactual Analysis of LLM Agent Tool Use in Interactive Environments**\n2. **When Does Deterministic Computation Help LLM Agents? Episode-Level Counterfactual Analysis Reveals Death Avoidance Dominance**\n3. **90% Death Avoidance: Decomposing the Routing Signal Between LLM Reasoning and Deterministic Simulation**\n\nRecommended: **Title 1** (clear claim + methodology in title; fits short paper convention of stating the finding)\n\n---\n\n## Abstract Skeleton (~150 words)\n\nKey points to cover:\n\n- **Problem**: LLM agents hallucinate state transitions in rule-governed environments, causing catastrophic failures (deaths). Routing between internal LLM reasoning and deterministic computation (simulators) can mitigate this, but what exactly does routing learn?\n- **Methodological gap**: Per-step oracle labeling degenerates in sparse-reward settings (98% tie rate on ScienceWorld). We propose episode-level counterfactual analysis.\n- **Core finding**: Death avoidance accounts for ~90% of routing signal (Δ_full=+29.60, Δ_no_death=+2.84, DAF=90.41%; Pearson r=0.97, p<1e-6 across 11 task types / 245 episodes) [A: plan-012-full, 245eps/11tasks]. Non-death performance is approximately equal between modalities.\n- **Supporting finding**: Keyword heuristics structurally fail (match rates degenerate to ≈always-det or ≈always-internal); episode-level counterfactual labels can train a lightweight router (internal_recall=51.5%).\n- **Implication**: The value of deterministic computation in interactive environments is concentrated in catastrophic failure prevention, not positive task guidance.\n\n---\n\n## Section Structure\n\n### 1. Introduction (0.8 pages)\n\n**Key points:**\n- LLM agents on rule-governed environments (physics, chemistry) suffer catastrophic failures from hallucinated state transitions → motivate the routing question\n- Existing work: tool-use learning (Toolformer, ART, Chameleon) learns *when* to invoke tools but doesn't analyze *what* routing learns; ITP-R routes to approximate world models but underperforms pure internal reasoning; ReTool/AgentMath use implicit routing entangled with backbone\n- Per-step oracle labeling degenerates in sparse-reward environments (98% tie rate) → need episode-level analysis\n- **Contributions** (bulleted):\n  1. Episode-level counterfactual methodology that overcomes per-step oracle degeneracy\n  2. Empirical finding: death avoidance accounts for ≥90% of routing signal on ScienceWorld (11 tasks, 245 episodes) [A: plan-012-full, 245eps/11tasks]\n  3. Structural failure analysis of keyword heuristics; demonstration that counterfactual labels can train a lightweight diagnostic router\n\n### 2. Method (1.0 pages)\n\n**Key points:**\n- **2.1 Problem Setup**: ScienceWorld environment; two computation modalities (internal LLM reasoning vs. deterministic simulation via environment forking); per-step routing decision\n- **2.2 Episode-Level Counterfactual Labeling**: Why per-step oracle fails (98% tie rate in sparse rewards) → run complete episodes under pure-internal and pure-deterministic strategies → compare episode-level scores → label: det-preferred / internal-preferred / no-preference. Distribution: 86 det-pref / 9 int-pref / 150 no-pref (245 episodes)\n- **2.3 Death Decomposition Framework**: Decompose Δ_full into death-avoidance component (Δ_death) and non-death component (Δ_nd). Death avoidance fraction = (Δ_full - Δ_nd) / Δ_full. Cross-task correlation: Pearson r between per-task death rate difference and Δ_full\n\n### 3. Experiments (1.5 pages)\n\n**Key points:**\n- **3.1 Setup**: Qwen3-1.7B backbone; ScienceWorld 11 task types × 20-40 episodes; evaluation: always-internal, always-deterministic, oracle, random, keyword heuristic, learned router\n- **3.2 Death Decomposition Results** (core result):\n  - Δ_full=+29.60, Δ_nd=+2.84, death fraction=90.41%\n  - 10/11 death-prone tasks: death-dominated gaps\n  - 1 exception: find-non-living-thing (0 deaths, Δ=+9.58 from non-death mechanisms)\n  - Pearson r=0.9698 (p=8.12e-07)\n- **3.3 Baseline Comparison**:\n  - always-internal: -37.16, always-det: -11.64, oracle: -9.03, random: -23.75\n  - Keyword heuristic: structural failure (v1 85.8% match → ≈always-det; v2 4.9% → ≈always-internal)\n  - Learned router (ablation-b): internal_recall=51.5%, first non-degenerate; classification head variants all degenerate\n- **3.4 Analysis**: Death rate: internal 42.9% vs. deterministic 16.3%; alive-episode scores nearly equal across modalities\n\n### 4. Related Work (0.5 pages, integrated or separate)\n\n**Key points:**\n- **Tool-use learning**: Toolformer (self-supervised API insertion), ART (LLM-as-router), Chameleon (LLM-as-planner), ToolkenGPT (token-level triggers). Differentiation: episode-level counterfactual labeling, safety-aware framing, explicit modular router\n- **Adaptive computation / routing**: CogRouter (RL-based), ARES, Mixture-of-Depths. Our focus: empirical analysis of *what* routing learns, not a new routing architecture\n- **World model routing**: ITP-R, Dyna-Think. Our deterministic computation is exact (simulator), not approximate (LLM world model)\n- **Agent frameworks**: ReAct, Reflexion. Orthogonal — we analyze the routing decision within an agent loop\n\n### 5. Conclusion (0.3 pages)\n\n**Key points:**\n- Summary: death avoidance ≥90% of routing signal; episode-level counterfactual analysis as diagnostic methodology\n- **Limitations**: single benchmark (ScienceWorld), episode-level granularity (not step-level), DAgger distribution shift (train on pure strategies, deploy on mixed)\n- **Future work**: step-level labeling with denser reward signals, extension to MATH/code interpretation domains, DAgger-style iterative relabeling\n\n---\n\n## Figure/Table Plan\n\n### Table 1: Baseline Comparison\n| Method | Score | 90% CI | Success Rate | Death Rate | Sim Ratio |\n|--------|-------|--------|-------------|------------|-----------|\n| Always-Internal | -37.16 | [-43.39, -31.43] | 12.4% | 40.7% | 0.00 |\n| Always-Deterministic | -11.64 | [-17.39, -6.55] | 23.7% | 18.6% | 1.00 |\n| Oracle | -9.03 | [-14.14, -4.15] | 24.2% | 16.5% | 0.96 |\n| Random | -23.75 | [-29.60, -18.11] | 16.5% | 28.4% | 0.50 |\n| Keyword Heuristic (v1) | ≈ Always-Det | — | — | — | 0.86 |\n| Keyword Heuristic (v2) | ≈ Always-Int | — | — | — | 0.05 |\n| Learned Router (implicit) | TBD | — | — | — | TBD |\n\n*Source: plan-003-baseline, plan-011-rule-based*\n\n### Figure 1: Death Decomposition (core figure)\n- **Type**: Grouped bar chart or stacked bar\n- **X-axis**: 11 task types (sorted by death fraction)\n- **Y-axis**: Score delta (deterministic − internal)\n- **Bars**: Δ_full decomposed into Δ_death (death-avoidance component, dark) and Δ_nd (non-death component, light)\n- **Highlight**: find-non-living-thing as sole exception (Δ_nd = Δ_full = 9.58, zero deaths)\n- **Annotation**: Overall death fraction = 90.41%\n\n*Source: plan-012-full*\n\n### Figure 2: Cross-task Correlation (if space permits)\n- **Type**: Scatter plot with regression line\n- **X-axis**: Per-task death rate difference (internal − deterministic)\n- **Y-axis**: Δ_full per task\n- **Regression line**: r=0.9698, p=8.12e-07\n- **11 points**, labeled by task type\n- **Purpose**: Visually demonstrates near-perfect linear relationship\n\n*Source: plan-012-full, plan-012-decomposition*\n\n**Space strategy**: Figure 1 is mandatory. Figure 2 can be merged as an inset in Figure 1, or moved to appendix if space is tight. Table 1 is mandatory. Per-task breakdown table → appendix.\n\n---\n\n## Key References\n\n### Tool-Use Learning\n- Schick et al. (2024). Toolformer: Language Models Can Teach Themselves to Use Tools. *NeurIPS*\n- Paranjape et al. (2023). ART: Automatic Multi-step Reasoning and Tool-Use. *arXiv*\n- Lu et al. (2024). Chameleon: Plug-and-Play Compositional Reasoning with Large Language Models. *NeurIPS*\n- Hao et al. (2024). ToolkenGPT: Augmenting Frozen Language Models with Massive Tools via Tool Embeddings. *NeurIPS*\n\n### Agent Routing / Adaptive Computation\n- CogRouter — RL-based cognitive routing (ScienceWorld SOTA)\n- ITP-R — imagination-based routing to LLM world model\n- ARES — adaptive routing for efficient serving\n- Raposo et al. (2024). Mixture-of-Depths. *ICML*\n\n### Agent Frameworks\n- Yao et al. (2023). ReAct: Synergizing Reasoning and Acting in Language Models. *ICLR*\n- Shinn et al. (2023). Reflexion: Language Agents with Verbal Reinforcement Learning. *NeurIPS*\n\n### Methodology\n- Ross et al. (2011). A Reduction of Imitation Learning and Structured Prediction to No-Regret Online Learning. *AISTATS* (DAgger)\n\n### Environment\n- Wang et al. (2022). ScienceWorld: Is your Agent Smarter than a 5th Grader? *EMNLP*\n\n### Code Execution Routing\n- Gou et al. (2024). ReTool / ToRA — tool-integrated reasoning for math\n- Chen et al. (2023). AgentMath — code-augmented mathematical reasoning\n\n---\n\n## Provenance: Claims → Experiments\n\n| Claim | Source Experiment | Key Metric |\n|-------|------------------|------------|\n| Δ_full=+29.60, death fraction=90.41% | plan-012-full | delta_full, death_avoidance_fraction |\n| r=0.9698, p=8.12e-07 | plan-012-full | pearson_r, pearson_p |\n| Baseline scores (Table 1) | plan-003-baseline | metrics per condition |\n| Keyword heuristic failure | plan-011-rule-based | v1_match_rate, v2_match_rate |\n| Learned router internal_recall=51.5% | plan-004-ablation-b | per_class.internal.recall |\n| find-non-living-thing Δ=9.58 | plan-012-decomposition | key_tasks.find_non_living_thing |\n| Episode label distribution 86/9/150 | plan-012-full | label_dist |\n| Death rates: int 42.9%, det 16.3% | plan-012-full | death_rate_int, death_rate_det |\n| Per-step oracle 98% tie rate | plan-012-decomposition | (derived from label_dist) |\n",
    "structuredPatch": [
      {
        "oldStart": 39,
        "oldLines": 7,
        "newStart": 39,
        "newLines": 7,
        "lines": [
          " ",
          " **Key points:**",
          " - **2.1 Problem Setup**: ScienceWorld environment; two computation modalities (internal LLM reasoning vs. deterministic simulation via environment forking); per-step routing decision",
          "-- **2.2 Episode-Level Counterfactual Labeling**: Why per-step oracle fails (98% tie rate in sparse rewards) → run complete episodes under pure-internal and pure-deterministic strategies → compare episode-level scores → label: det-preferred / internal-preferred / no-preference. Distribution: 86 det-pref / 9 int-pref / 150 no-pref (245 episodes)",
          "+- **2.2 Episode-Level Counterfactual Labeling**: Why per-step oracle fails (98% tie rate in sparse rewards) → run complete episodes under pure-internal and pure-deterministic strategies → compare episode-level scores → label: det-preferred / internal-preferred / no-preference. Distribution: 86 det-pref / 9 int-pref / 150 no-pref (245 episodes) [A: plan-012-full, 245eps/11tasks]",
          " - **2.3 Death Decomposition Framework**: Decompose Δ_full into death-avoidance component (Δ_death) and non-death component (Δ_nd). Death avoidance fraction = (Δ_full - Δ_nd) / Δ_full. Cross-task correlation: Pearson r between per-task death rate difference and Δ_full",
          " ",
          " ### 3. Experiments (1.5 pages)"
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  },
  "sourceToolAssistantUUID": "c3ce405e-2c92-4183-b01f-86fd26ded850",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing",
  "sessionId": "fe1af098-4ed4-4fac-9d28-af54a02d46ce",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 31 · 2026-05-14T08:21:09.630Z_

```json
{
  "parentUuid": "93480bca-3898-4dd0-8b27-ad5db60cc572",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "4baa46af-0f61-4112-a468-f8decab08f2b",
  "timestamp": "2026-05-14T08:21:09.630Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing",
  "sessionId": "fe1af098-4ed4-4fac-9d28-af54a02d46ce",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Tool call

_source line 32 · 2026-05-14T08:21:13.121Z_

<details open><summary>🔧 Tool call — Edit · `toolu_01Rocq8r5ebrtrnM1TcdYfbX`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/_project/paper/paper_outline.md",
  "old_string": "  - Δ_full=+29.60, Δ_nd=+2.84, death fraction=90.41%",
  "new_string": "  - Δ_full=+29.60, Δ_nd=+2.84, death fraction=90.41% [A: plan-012-full, 245eps/11tasks]"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4baa46af-0f61-4112-a468-f8decab08f2b",
  "isSidechain": false,
  "requestId": "req_011Cb28rVzgv7wx3xU7Khigh",
  "type": "assistant",
  "uuid": "95ee7703-ac24-4081-abf8-0140d000f2a2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing",
  "sessionId": "fe1af098-4ed4-4fac-9d28-af54a02d46ce",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RKmyvdA8WK569VMUyAvCQG",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 380,
      "cache_read_input_tokens": 32531,
      "output_tokens": 226,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 380,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 226,
          "cache_read_input_tokens": 32531,
          "cache_creation_input_tokens": 380,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 380
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

_source line 33 · 2026-05-14T08:21:13.137Z_

<details><summary>↩ Tool result · `toolu_01Rocq8r5ebrtrnM1TcdYfbX`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/_project/paper/paper_outline.md has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "95ee7703-ac24-4081-abf8-0140d000f2a2",
  "isSidechain": false,
  "promptId": "de32f0f5-b4f7-4fe9-872c-8108c929635d",
  "type": "user",
  "uuid": "c52aadac-2b63-4772-86f6-65dee7111c82",
  "toolUseResult": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/_project/paper/paper_outline.md",
    "oldString": "  - Δ_full=+29.60, Δ_nd=+2.84, death fraction=90.41%",
    "newString": "  - Δ_full=+29.60, Δ_nd=+2.84, death fraction=90.41% [A: plan-012-full, 245eps/11tasks]",
    "originalFile": "# EMNLP 2026 Short Paper Outline\n\n## Title Candidates\n\n1. **Death Avoidance Dominates Routing Signal: A Counterfactual Analysis of LLM Agent Tool Use in Interactive Environments**\n2. **When Does Deterministic Computation Help LLM Agents? Episode-Level Counterfactual Analysis Reveals Death Avoidance Dominance**\n3. **90% Death Avoidance: Decomposing the Routing Signal Between LLM Reasoning and Deterministic Simulation**\n\nRecommended: **Title 1** (clear claim + methodology in title; fits short paper convention of stating the finding)\n\n---\n\n## Abstract Skeleton (~150 words)\n\nKey points to cover:\n\n- **Problem**: LLM agents hallucinate state transitions in rule-governed environments, causing catastrophic failures (deaths). Routing between internal LLM reasoning and deterministic computation (simulators) can mitigate this, but what exactly does routing learn?\n- **Methodological gap**: Per-step oracle labeling degenerates in sparse-reward settings (98% tie rate on ScienceWorld). We propose episode-level counterfactual analysis.\n- **Core finding**: Death avoidance accounts for ~90% of routing signal (Δ_full=+29.60, Δ_no_death=+2.84, DAF=90.41%; Pearson r=0.97, p<1e-6 across 11 task types / 245 episodes) [A: plan-012-full, 245eps/11tasks]. Non-death performance is approximately equal between modalities.\n- **Supporting finding**: Keyword heuristics structurally fail (match rates degenerate to ≈always-det or ≈always-internal); episode-level counterfactual labels can train a lightweight router (internal_recall=51.5%).\n- **Implication**: The value of deterministic computation in interactive environments is concentrated in catastrophic failure prevention, not positive task guidance.\n\n---\n\n## Section Structure\n\n### 1. Introduction (0.8 pages)\n\n**Key points:**\n- LLM agents on rule-governed environments (physics, chemistry) suffer catastrophic failures from hallucinated state transitions → motivate the routing question\n- Existing work: tool-use learning (Toolformer, ART, Chameleon) learns *when* to invoke tools but doesn't analyze *what* routing learns; ITP-R routes to approximate world models but underperforms pure internal reasoning; ReTool/AgentMath use implicit routing entangled with backbone\n- Per-step oracle labeling degenerates in sparse-reward environments (98% tie rate) → need episode-level analysis\n- **Contributions** (bulleted):\n  1. Episode-level counterfactual methodology that overcomes per-step oracle degeneracy\n  2. Empirical finding: death avoidance accounts for ≥90% of routing signal on ScienceWorld (11 tasks, 245 episodes) [A: plan-012-full, 245eps/11tasks]\n  3. Structural failure analysis of keyword heuristics; demonstration that counterfactual labels can train a lightweight diagnostic router\n\n### 2. Method (1.0 pages)\n\n**Key points:**\n- **2.1 Problem Setup**: ScienceWorld environment; two computation modalities (internal LLM reasoning vs. deterministic simulation via environment forking); per-step routing decision\n- **2.2 Episode-Level Counterfactual Labeling**: Why per-step oracle fails (98% tie rate in sparse rewards) → run complete episodes under pure-internal and pure-deterministic strategies → compare episode-level scores → label: det-preferred / internal-preferred / no-preference. Distribution: 86 det-pref / 9 int-pref / 150 no-pref (245 episodes) [A: plan-012-full, 245eps/11tasks]\n- **2.3 Death Decomposition Framework**: Decompose Δ_full into death-avoidance component (Δ_death) and non-death component (Δ_nd). Death avoidance fraction = (Δ_full - Δ_nd) / Δ_full. Cross-task correlation: Pearson r between per-task death rate difference and Δ_full\n\n### 3. Experiments (1.5 pages)\n\n**Key points:**\n- **3.1 Setup**: Qwen3-1.7B backbone; ScienceWorld 11 task types × 20-40 episodes; evaluation: always-internal, always-deterministic, oracle, random, keyword heuristic, learned router\n- **3.2 Death Decomposition Results** (core result):\n  - Δ_full=+29.60, Δ_nd=+2.84, death fraction=90.41%\n  - 10/11 death-prone tasks: death-dominated gaps\n  - 1 exception: find-non-living-thing (0 deaths, Δ=+9.58 from non-death mechanisms)\n  - Pearson r=0.9698 (p=8.12e-07)\n- **3.3 Baseline Comparison**:\n  - always-internal: -37.16, always-det: -11.64, oracle: -9.03, random: -23.75\n  - Keyword heuristic: structural failure (v1 85.8% match → ≈always-det; v2 4.9% → ≈always-internal)\n  - Learned router (ablation-b): internal_recall=51.5%, first non-degenerate; classification head variants all degenerate\n- **3.4 Analysis**: Death rate: internal 42.9% vs. deterministic 16.3%; alive-episode scores nearly equal across modalities\n\n### 4. Related Work (0.5 pages, integrated or separate)\n\n**Key points:**\n- **Tool-use learning**: Toolformer (self-supervised API insertion), ART (LLM-as-router), Chameleon (LLM-as-planner), ToolkenGPT (token-level triggers). Differentiation: episode-level counterfactual labeling, safety-aware framing, explicit modular router\n- **Adaptive computation / routing**: CogRouter (RL-based), ARES, Mixture-of-Depths. Our focus: empirical analysis of *what* routing learns, not a new routing architecture\n- **World model routing**: ITP-R, Dyna-Think. Our deterministic computation is exact (simulator), not approximate (LLM world model)\n- **Agent frameworks**: ReAct, Reflexion. Orthogonal — we analyze the routing decision within an agent loop\n\n### 5. Conclusion (0.3 pages)\n\n**Key points:**\n- Summary: death avoidance ≥90% of routing signal; episode-level counterfactual analysis as diagnostic methodology\n- **Limitations**: single benchmark (ScienceWorld), episode-level granularity (not step-level), DAgger distribution shift (train on pure strategies, deploy on mixed)\n- **Future work**: step-level labeling with denser reward signals, extension to MATH/code interpretation domains, DAgger-style iterative relabeling\n\n---\n\n## Figure/Table Plan\n\n### Table 1: Baseline Comparison\n| Method | Score | 90% CI | Success Rate | Death Rate | Sim Ratio |\n|--------|-------|--------|-------------|------------|-----------|\n| Always-Internal | -37.16 | [-43.39, -31.43] | 12.4% | 40.7% | 0.00 |\n| Always-Deterministic | -11.64 | [-17.39, -6.55] | 23.7% | 18.6% | 1.00 |\n| Oracle | -9.03 | [-14.14, -4.15] | 24.2% | 16.5% | 0.96 |\n| Random | -23.75 | [-29.60, -18.11] | 16.5% | 28.4% | 0.50 |\n| Keyword Heuristic (v1) | ≈ Always-Det | — | — | — | 0.86 |\n| Keyword Heuristic (v2) | ≈ Always-Int | — | — | — | 0.05 |\n| Learned Router (implicit) | TBD | — | — | — | TBD |\n\n*Source: plan-003-baseline, plan-011-rule-based*\n\n### Figure 1: Death Decomposition (core figure)\n- **Type**: Grouped bar chart or stacked bar\n- **X-axis**: 11 task types (sorted by death fraction)\n- **Y-axis**: Score delta (deterministic − internal)\n- **Bars**: Δ_full decomposed into Δ_death (death-avoidance component, dark) and Δ_nd (non-death component, light)\n- **Highlight**: find-non-living-thing as sole exception (Δ_nd = Δ_full = 9.58, zero deaths)\n- **Annotation**: Overall death fraction = 90.41%\n\n*Source: plan-012-full*\n\n### Figure 2: Cross-task Correlation (if space permits)\n- **Type**: Scatter plot with regression line\n- **X-axis**: Per-task death rate difference (internal − deterministic)\n- **Y-axis**: Δ_full per task\n- **Regression line**: r=0.9698, p=8.12e-07\n- **11 points**, labeled by task type\n- **Purpose**: Visually demonstrates near-perfect linear relationship\n\n*Source: plan-012-full, plan-012-decomposition*\n\n**Space strategy**: Figure 1 is mandatory. Figure 2 can be merged as an inset in Figure 1, or moved to appendix if space is tight. Table 1 is mandatory. Per-task breakdown table → appendix.\n\n---\n\n## Key References\n\n### Tool-Use Learning\n- Schick et al. (2024). Toolformer: Language Models Can Teach Themselves to Use Tools. *NeurIPS*\n- Paranjape et al. (2023). ART: Automatic Multi-step Reasoning and Tool-Use. *arXiv*\n- Lu et al. (2024). Chameleon: Plug-and-Play Compositional Reasoning with Large Language Models. *NeurIPS*\n- Hao et al. (2024). ToolkenGPT: Augmenting Frozen Language Models with Massive Tools via Tool Embeddings. *NeurIPS*\n\n### Agent Routing / Adaptive Computation\n- CogRouter — RL-based cognitive routing (ScienceWorld SOTA)\n- ITP-R — imagination-based routing to LLM world model\n- ARES — adaptive routing for efficient serving\n- Raposo et al. (2024). Mixture-of-Depths. *ICML*\n\n### Agent Frameworks\n- Yao et al. (2023). ReAct: Synergizing Reasoning and Acting in Language Models. *ICLR*\n- Shinn et al. (2023). Reflexion: Language Agents with Verbal Reinforcement Learning. *NeurIPS*\n\n### Methodology\n- Ross et al. (2011). A Reduction of Imitation Learning and Structured Prediction to No-Regret Online Learning. *AISTATS* (DAgger)\n\n### Environment\n- Wang et al. (2022). ScienceWorld: Is your Agent Smarter than a 5th Grader? *EMNLP*\n\n### Code Execution Routing\n- Gou et al. (2024). ReTool / ToRA — tool-integrated reasoning for math\n- Chen et al. (2023). AgentMath — code-augmented mathematical reasoning\n\n---\n\n## Provenance: Claims → Experiments\n\n| Claim | Source Experiment | Key Metric |\n|-------|------------------|------------|\n| Δ_full=+29.60, death fraction=90.41% | plan-012-full | delta_full, death_avoidance_fraction |\n| r=0.9698, p=8.12e-07 | plan-012-full | pearson_r, pearson_p |\n| Baseline scores (Table 1) | plan-003-baseline | metrics per condition |\n| Keyword heuristic failure | plan-011-rule-based | v1_match_rate, v2_match_rate |\n| Learned router internal_recall=51.5% | plan-004-ablation-b | per_class.internal.recall |\n| find-non-living-thing Δ=9.58 | plan-012-decomposition | key_tasks.find_non_living_thing |\n| Episode label distribution 86/9/150 | plan-012-full | label_dist |\n| Death rates: int 42.9%, det 16.3% | plan-012-full | death_rate_int, death_rate_det |\n| Per-step oracle 98% tie rate | plan-012-decomposition | (derived from label_dist) |\n",
    "structuredPatch": [
      {
        "oldStart": 47,
        "oldLines": 7,
        "newStart": 47,
        "newLines": 7,
        "lines": [
          " **Key points:**",
          " - **3.1 Setup**: Qwen3-1.7B backbone; ScienceWorld 11 task types × 20-40 episodes; evaluation: always-internal, always-deterministic, oracle, random, keyword heuristic, learned router",
          " - **3.2 Death Decomposition Results** (core result):",
          "-  - Δ_full=+29.60, Δ_nd=+2.84, death fraction=90.41%",
          "+  - Δ_full=+29.60, Δ_nd=+2.84, death fraction=90.41% [A: plan-012-full, 245eps/11tasks]",
          "   - 10/11 death-prone tasks: death-dominated gaps",
          "   - 1 exception: find-non-living-thing (0 deaths, Δ=+9.58 from non-death mechanisms)",
          "   - Pearson r=0.9698 (p=8.12e-07)"
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  },
  "sourceToolAssistantUUID": "95ee7703-ac24-4081-abf8-0140d000f2a2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing",
  "sessionId": "fe1af098-4ed4-4fac-9d28-af54a02d46ce",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 34_

```json
{
  "type": "last-prompt",
  "leafUuid": "c52aadac-2b63-4772-86f6-65dee7111c82",
  "sessionId": "fe1af098-4ed4-4fac-9d28-af54a02d46ce"
}
```

---

### Runtime record

_source line 35_

```json
{
  "type": "ai-title",
  "aiTitle": "Update paper_outline.md baseline numbers to 245-ep",
  "sessionId": "fe1af098-4ed4-4fac-9d28-af54a02d46ce"
}
```

---

### Tool call

_source line 36 · 2026-05-14T08:21:17.533Z_

<details open><summary>🔧 Tool call — Edit · `toolu_01UD8ofXtfjozDP7sUrfaXmo`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/_project/paper/paper_outline.md",
  "old_string": "  - 1 exception: find-non-living-thing (0 deaths, Δ=+9.58 from non-death mechanisms)",
  "new_string": "  - 1 exception: find-non-living-thing (n=40, 0 deaths, Δ=+9.58 from non-death mechanisms) [A: plan-012-full, 245eps/11tasks]"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c52aadac-2b63-4772-86f6-65dee7111c82",
  "isSidechain": false,
  "requestId": "req_011Cb28rmFiEPrGJq4FQ7w43",
  "type": "assistant",
  "uuid": "ce8cf3e0-8b17-43f9-8dae-4fd4b5731020",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing",
  "sessionId": "fe1af098-4ed4-4fac-9d28-af54a02d46ce",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WJGqbJZVhovGYirRNTibG3",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 285,
      "cache_read_input_tokens": 32911,
      "output_tokens": 236,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 285,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 236,
          "cache_read_input_tokens": 32911,
          "cache_creation_input_tokens": 285,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 285
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

_source line 37 · 2026-05-14T08:21:17.549Z_

<details><summary>↩ Tool result · `toolu_01UD8ofXtfjozDP7sUrfaXmo`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/_project/paper/paper_outline.md has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ce8cf3e0-8b17-43f9-8dae-4fd4b5731020",
  "isSidechain": false,
  "promptId": "de32f0f5-b4f7-4fe9-872c-8108c929635d",
  "type": "user",
  "uuid": "0e1471e3-c328-435e-98a6-2a8de2388601",
  "toolUseResult": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/_project/paper/paper_outline.md",
    "oldString": "  - 1 exception: find-non-living-thing (0 deaths, Δ=+9.58 from non-death mechanisms)",
    "newString": "  - 1 exception: find-non-living-thing (n=40, 0 deaths, Δ=+9.58 from non-death mechanisms) [A: plan-012-full, 245eps/11tasks]",
    "originalFile": "# EMNLP 2026 Short Paper Outline\n\n## Title Candidates\n\n1. **Death Avoidance Dominates Routing Signal: A Counterfactual Analysis of LLM Agent Tool Use in Interactive Environments**\n2. **When Does Deterministic Computation Help LLM Agents? Episode-Level Counterfactual Analysis Reveals Death Avoidance Dominance**\n3. **90% Death Avoidance: Decomposing the Routing Signal Between LLM Reasoning and Deterministic Simulation**\n\nRecommended: **Title 1** (clear claim + methodology in title; fits short paper convention of stating the finding)\n\n---\n\n## Abstract Skeleton (~150 words)\n\nKey points to cover:\n\n- **Problem**: LLM agents hallucinate state transitions in rule-governed environments, causing catastrophic failures (deaths). Routing between internal LLM reasoning and deterministic computation (simulators) can mitigate this, but what exactly does routing learn?\n- **Methodological gap**: Per-step oracle labeling degenerates in sparse-reward settings (98% tie rate on ScienceWorld). We propose episode-level counterfactual analysis.\n- **Core finding**: Death avoidance accounts for ~90% of routing signal (Δ_full=+29.60, Δ_no_death=+2.84, DAF=90.41%; Pearson r=0.97, p<1e-6 across 11 task types / 245 episodes) [A: plan-012-full, 245eps/11tasks]. Non-death performance is approximately equal between modalities.\n- **Supporting finding**: Keyword heuristics structurally fail (match rates degenerate to ≈always-det or ≈always-internal); episode-level counterfactual labels can train a lightweight router (internal_recall=51.5%).\n- **Implication**: The value of deterministic computation in interactive environments is concentrated in catastrophic failure prevention, not positive task guidance.\n\n---\n\n## Section Structure\n\n### 1. Introduction (0.8 pages)\n\n**Key points:**\n- LLM agents on rule-governed environments (physics, chemistry) suffer catastrophic failures from hallucinated state transitions → motivate the routing question\n- Existing work: tool-use learning (Toolformer, ART, Chameleon) learns *when* to invoke tools but doesn't analyze *what* routing learns; ITP-R routes to approximate world models but underperforms pure internal reasoning; ReTool/AgentMath use implicit routing entangled with backbone\n- Per-step oracle labeling degenerates in sparse-reward environments (98% tie rate) → need episode-level analysis\n- **Contributions** (bulleted):\n  1. Episode-level counterfactual methodology that overcomes per-step oracle degeneracy\n  2. Empirical finding: death avoidance accounts for ≥90% of routing signal on ScienceWorld (11 tasks, 245 episodes) [A: plan-012-full, 245eps/11tasks]\n  3. Structural failure analysis of keyword heuristics; demonstration that counterfactual labels can train a lightweight diagnostic router\n\n### 2. Method (1.0 pages)\n\n**Key points:**\n- **2.1 Problem Setup**: ScienceWorld environment; two computation modalities (internal LLM reasoning vs. deterministic simulation via environment forking); per-step routing decision\n- **2.2 Episode-Level Counterfactual Labeling**: Why per-step oracle fails (98% tie rate in sparse rewards) → run complete episodes under pure-internal and pure-deterministic strategies → compare episode-level scores → label: det-preferred / internal-preferred / no-preference. Distribution: 86 det-pref / 9 int-pref / 150 no-pref (245 episodes) [A: plan-012-full, 245eps/11tasks]\n- **2.3 Death Decomposition Framework**: Decompose Δ_full into death-avoidance component (Δ_death) and non-death component (Δ_nd). Death avoidance fraction = (Δ_full - Δ_nd) / Δ_full. Cross-task correlation: Pearson r between per-task death rate difference and Δ_full\n\n### 3. Experiments (1.5 pages)\n\n**Key points:**\n- **3.1 Setup**: Qwen3-1.7B backbone; ScienceWorld 11 task types × 20-40 episodes; evaluation: always-internal, always-deterministic, oracle, random, keyword heuristic, learned router\n- **3.2 Death Decomposition Results** (core result):\n  - Δ_full=+29.60, Δ_nd=+2.84, death fraction=90.41% [A: plan-012-full, 245eps/11tasks]\n  - 10/11 death-prone tasks: death-dominated gaps\n  - 1 exception: find-non-living-thing (0 deaths, Δ=+9.58 from non-death mechanisms)\n  - Pearson r=0.9698 (p=8.12e-07)\n- **3.3 Baseline Comparison**:\n  - always-internal: -37.16, always-det: -11.64, oracle: -9.03, random: -23.75\n  - Keyword heuristic: structural failure (v1 85.8% match → ≈always-det; v2 4.9% → ≈always-internal)\n  - Learned router (ablation-b): internal_recall=51.5%, first non-degenerate; classification head variants all degenerate\n- **3.4 Analysis**: Death rate: internal 42.9% vs. deterministic 16.3%; alive-episode scores nearly equal across modalities\n\n### 4. Related Work (0.5 pages, integrated or separate)\n\n**Key points:**\n- **Tool-use learning**: Toolformer (self-supervised API insertion), ART (LLM-as-router), Chameleon (LLM-as-planner), ToolkenGPT (token-level triggers). Differentiation: episode-level counterfactual labeling, safety-aware framing, explicit modular router\n- **Adaptive computation / routing**: CogRouter (RL-based), ARES, Mixture-of-Depths. Our focus: empirical analysis of *what* routing learns, not a new routing architecture\n- **World model routing**: ITP-R, Dyna-Think. Our deterministic computation is exact (simulator), not approximate (LLM world model)\n- **Agent frameworks**: ReAct, Reflexion. Orthogonal — we analyze the routing decision within an agent loop\n\n### 5. Conclusion (0.3 pages)\n\n**Key points:**\n- Summary: death avoidance ≥90% of routing signal; episode-level counterfactual analysis as diagnostic methodology\n- **Limitations**: single benchmark (ScienceWorld), episode-level granularity (not step-level), DAgger distribution shift (train on pure strategies, deploy on mixed)\n- **Future work**: step-level labeling with denser reward signals, extension to MATH/code interpretation domains, DAgger-style iterative relabeling\n\n---\n\n## Figure/Table Plan\n\n### Table 1: Baseline Comparison\n| Method | Score | 90% CI | Success Rate | Death Rate | Sim Ratio |\n|--------|-------|--------|-------------|------------|-----------|\n| Always-Internal | -37.16 | [-43.39, -31.43] | 12.4% | 40.7% | 0.00 |\n| Always-Deterministic | -11.64 | [-17.39, -6.55] | 23.7% | 18.6% | 1.00 |\n| Oracle | -9.03 | [-14.14, -4.15] | 24.2% | 16.5% | 0.96 |\n| Random | -23.75 | [-29.60, -18.11] | 16.5% | 28.4% | 0.50 |\n| Keyword Heuristic (v1) | ≈ Always-Det | — | — | — | 0.86 |\n| Keyword Heuristic (v2) | ≈ Always-Int | — | — | — | 0.05 |\n| Learned Router (implicit) | TBD | — | — | — | TBD |\n\n*Source: plan-003-baseline, plan-011-rule-based*\n\n### Figure 1: Death Decomposition (core figure)\n- **Type**: Grouped bar chart or stacked bar\n- **X-axis**: 11 task types (sorted by death fraction)\n- **Y-axis**: Score delta (deterministic − internal)\n- **Bars**: Δ_full decomposed into Δ_death (death-avoidance component, dark) and Δ_nd (non-death component, light)\n- **Highlight**: find-non-living-thing as sole exception (Δ_nd = Δ_full = 9.58, zero deaths)\n- **Annotation**: Overall death fraction = 90.41%\n\n*Source: plan-012-full*\n\n### Figure 2: Cross-task Correlation (if space permits)\n- **Type**: Scatter plot with regression line\n- **X-axis**: Per-task death rate difference (internal − deterministic)\n- **Y-axis**: Δ_full per task\n- **Regression line**: r=0.9698, p=8.12e-07\n- **11 points**, labeled by task type\n- **Purpose**: Visually demonstrates near-perfect linear relationship\n\n*Source: plan-012-full, plan-012-decomposition*\n\n**Space strategy**: Figure 1 is mandatory. Figure 2 can be merged as an inset in Figure 1, or moved to appendix if space is tight. Table 1 is mandatory. Per-task breakdown table → appendix.\n\n---\n\n## Key References\n\n### Tool-Use Learning\n- Schick et al. (2024). Toolformer: Language Models Can Teach Themselves to Use Tools. *NeurIPS*\n- Paranjape et al. (2023). ART: Automatic Multi-step Reasoning and Tool-Use. *arXiv*\n- Lu et al. (2024). Chameleon: Plug-and-Play Compositional Reasoning with Large Language Models. *NeurIPS*\n- Hao et al. (2024). ToolkenGPT: Augmenting Frozen Language Models with Massive Tools via Tool Embeddings. *NeurIPS*\n\n### Agent Routing / Adaptive Computation\n- CogRouter — RL-based cognitive routing (ScienceWorld SOTA)\n- ITP-R — imagination-based routing to LLM world model\n- ARES — adaptive routing for efficient serving\n- Raposo et al. (2024). Mixture-of-Depths. *ICML*\n\n### Agent Frameworks\n- Yao et al. (2023). ReAct: Synergizing Reasoning and Acting in Language Models. *ICLR*\n- Shinn et al. (2023). Reflexion: Language Agents with Verbal Reinforcement Learning. *NeurIPS*\n\n### Methodology\n- Ross et al. (2011). A Reduction of Imitation Learning and Structured Prediction to No-Regret Online Learning. *AISTATS* (DAgger)\n\n### Environment\n- Wang et al. (2022). ScienceWorld: Is your Agent Smarter than a 5th Grader? *EMNLP*\n\n### Code Execution Routing\n- Gou et al. (2024). ReTool / ToRA — tool-integrated reasoning for math\n- Chen et al. (2023). AgentMath — code-augmented mathematical reasoning\n\n---\n\n## Provenance: Claims → Experiments\n\n| Claim | Source Experiment | Key Metric |\n|-------|------------------|------------|\n| Δ_full=+29.60, death fraction=90.41% | plan-012-full | delta_full, death_avoidance_fraction |\n| r=0.9698, p=8.12e-07 | plan-012-full | pearson_r, pearson_p |\n| Baseline scores (Table 1) | plan-003-baseline | metrics per condition |\n| Keyword heuristic failure | plan-011-rule-based | v1_match_rate, v2_match_rate |\n| Learned router internal_recall=51.5% | plan-004-ablation-b | per_class.internal.recall |\n| find-non-living-thing Δ=9.58 | plan-012-decomposition | key_tasks.find_non_living_thing |\n| Episode label distribution 86/9/150 | plan-012-full | label_dist |\n| Death rates: int 42.9%, det 16.3% | plan-012-full | death_rate_int, death_rate_det |\n| Per-step oracle 98% tie rate | plan-012-decomposition | (derived from label_dist) |\n",
    "structuredPatch": [
      {
        "oldStart": 49,
        "oldLines": 7,
        "newStart": 49,
        "newLines": 7,
        "lines": [
          " - **3.2 Death Decomposition Results** (core result):",
          "   - Δ_full=+29.60, Δ_nd=+2.84, death fraction=90.41% [A: plan-012-full, 245eps/11tasks]",
          "   - 10/11 death-prone tasks: death-dominated gaps",
          "-  - 1 exception: find-non-living-thing (0 deaths, Δ=+9.58 from non-death mechanisms)",
          "+  - 1 exception: find-non-living-thing (n=40, 0 deaths, Δ=+9.58 from non-death mechanisms) [A: plan-012-full, 245eps/11tasks]",
          "   - Pearson r=0.9698 (p=8.12e-07)",
          " - **3.3 Baseline Comparison**:",
          "   - always-internal: -37.16, always-det: -11.64, oracle: -9.03, random: -23.75"
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  },
  "sourceToolAssistantUUID": "ce8cf3e0-8b17-43f9-8dae-4fd4b5731020",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing",
  "sessionId": "fe1af098-4ed4-4fac-9d28-af54a02d46ce",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 38 · 2026-05-14T08:21:21.166Z_

<details open><summary>🔧 Tool call — Edit · `toolu_01A4WwWQHwA2uMYefJhCFo33`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/_project/paper/paper_outline.md",
  "old_string": "  - Pearson r=0.9698 (p=8.12e-07)",
  "new_string": "  - Pearson r=0.9698 (p=8.12e-07) [A: plan-012-full, 245eps/11tasks]"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0e1471e3-c328-435e-98a6-2a8de2388601",
  "isSidechain": false,
  "requestId": "req_011Cb28s6BFPqLJAhZa8DNEk",
  "type": "assistant",
  "uuid": "a0d56ed7-802a-42c8-b1be-50a73cfdfb73",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing",
  "sessionId": "fe1af098-4ed4-4fac-9d28-af54a02d46ce",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015VGCnMLBzs6G5v3w4tgmgp",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 295,
      "cache_read_input_tokens": 33196,
      "output_tokens": 207,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 295,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 207,
          "cache_read_input_tokens": 33196,
          "cache_creation_input_tokens": 295,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 295
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

_source line 39 · 2026-05-14T08:21:21.251Z_

<details><summary>↩ Tool result · `toolu_01A4WwWQHwA2uMYefJhCFo33`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/_project/paper/paper_outline.md has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a0d56ed7-802a-42c8-b1be-50a73cfdfb73",
  "isSidechain": false,
  "promptId": "de32f0f5-b4f7-4fe9-872c-8108c929635d",
  "type": "user",
  "uuid": "c07e1f95-23b4-4d61-b840-478d3e8ac863",
  "toolUseResult": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/_project/paper/paper_outline.md",
    "oldString": "  - Pearson r=0.9698 (p=8.12e-07)",
    "newString": "  - Pearson r=0.9698 (p=8.12e-07) [A: plan-012-full, 245eps/11tasks]",
    "originalFile": "# EMNLP 2026 Short Paper Outline\n\n## Title Candidates\n\n1. **Death Avoidance Dominates Routing Signal: A Counterfactual Analysis of LLM Agent Tool Use in Interactive Environments**\n2. **When Does Deterministic Computation Help LLM Agents? Episode-Level Counterfactual Analysis Reveals Death Avoidance Dominance**\n3. **90% Death Avoidance: Decomposing the Routing Signal Between LLM Reasoning and Deterministic Simulation**\n\nRecommended: **Title 1** (clear claim + methodology in title; fits short paper convention of stating the finding)\n\n---\n\n## Abstract Skeleton (~150 words)\n\nKey points to cover:\n\n- **Problem**: LLM agents hallucinate state transitions in rule-governed environments, causing catastrophic failures (deaths). Routing between internal LLM reasoning and deterministic computation (simulators) can mitigate this, but what exactly does routing learn?\n- **Methodological gap**: Per-step oracle labeling degenerates in sparse-reward settings (98% tie rate on ScienceWorld). We propose episode-level counterfactual analysis.\n- **Core finding**: Death avoidance accounts for ~90% of routing signal (Δ_full=+29.60, Δ_no_death=+2.84, DAF=90.41%; Pearson r=0.97, p<1e-6 across 11 task types / 245 episodes) [A: plan-012-full, 245eps/11tasks]. Non-death performance is approximately equal between modalities.\n- **Supporting finding**: Keyword heuristics structurally fail (match rates degenerate to ≈always-det or ≈always-internal); episode-level counterfactual labels can train a lightweight router (internal_recall=51.5%).\n- **Implication**: The value of deterministic computation in interactive environments is concentrated in catastrophic failure prevention, not positive task guidance.\n\n---\n\n## Section Structure\n\n### 1. Introduction (0.8 pages)\n\n**Key points:**\n- LLM agents on rule-governed environments (physics, chemistry) suffer catastrophic failures from hallucinated state transitions → motivate the routing question\n- Existing work: tool-use learning (Toolformer, ART, Chameleon) learns *when* to invoke tools but doesn't analyze *what* routing learns; ITP-R routes to approximate world models but underperforms pure internal reasoning; ReTool/AgentMath use implicit routing entangled with backbone\n- Per-step oracle labeling degenerates in sparse-reward environments (98% tie rate) → need episode-level analysis\n- **Contributions** (bulleted):\n  1. Episode-level counterfactual methodology that overcomes per-step oracle degeneracy\n  2. Empirical finding: death avoidance accounts for ≥90% of routing signal on ScienceWorld (11 tasks, 245 episodes) [A: plan-012-full, 245eps/11tasks]\n  3. Structural failure analysis of keyword heuristics; demonstration that counterfactual labels can train a lightweight diagnostic router\n\n### 2. Method (1.0 pages)\n\n**Key points:**\n- **2.1 Problem Setup**: ScienceWorld environment; two computation modalities (internal LLM reasoning vs. deterministic simulation via environment forking); per-step routing decision\n- **2.2 Episode-Level Counterfactual Labeling**: Why per-step oracle fails (98% tie rate in sparse rewards) → run complete episodes under pure-internal and pure-deterministic strategies → compare episode-level scores → label: det-preferred / internal-preferred / no-preference. Distribution: 86 det-pref / 9 int-pref / 150 no-pref (245 episodes) [A: plan-012-full, 245eps/11tasks]\n- **2.3 Death Decomposition Framework**: Decompose Δ_full into death-avoidance component (Δ_death) and non-death component (Δ_nd). Death avoidance fraction = (Δ_full - Δ_nd) / Δ_full. Cross-task correlation: Pearson r between per-task death rate difference and Δ_full\n\n### 3. Experiments (1.5 pages)\n\n**Key points:**\n- **3.1 Setup**: Qwen3-1.7B backbone; ScienceWorld 11 task types × 20-40 episodes; evaluation: always-internal, always-deterministic, oracle, random, keyword heuristic, learned router\n- **3.2 Death Decomposition Results** (core result):\n  - Δ_full=+29.60, Δ_nd=+2.84, death fraction=90.41% [A: plan-012-full, 245eps/11tasks]\n  - 10/11 death-prone tasks: death-dominated gaps\n  - 1 exception: find-non-living-thing (n=40, 0 deaths, Δ=+9.58 from non-death mechanisms) [A: plan-012-full, 245eps/11tasks]\n  - Pearson r=0.9698 (p=8.12e-07)\n- **3.3 Baseline Comparison**:\n  - always-internal: -37.16, always-det: -11.64, oracle: -9.03, random: -23.75\n  - Keyword heuristic: structural failure (v1 85.8% match → ≈always-det; v2 4.9% → ≈always-internal)\n  - Learned router (ablation-b): internal_recall=51.5%, first non-degenerate; classification head variants all degenerate\n- **3.4 Analysis**: Death rate: internal 42.9% vs. deterministic 16.3%; alive-episode scores nearly equal across modalities\n\n### 4. Related Work (0.5 pages, integrated or separate)\n\n**Key points:**\n- **Tool-use learning**: Toolformer (self-supervised API insertion), ART (LLM-as-router), Chameleon (LLM-as-planner), ToolkenGPT (token-level triggers). Differentiation: episode-level counterfactual labeling, safety-aware framing, explicit modular router\n- **Adaptive computation / routing**: CogRouter (RL-based), ARES, Mixture-of-Depths. Our focus: empirical analysis of *what* routing learns, not a new routing architecture\n- **World model routing**: ITP-R, Dyna-Think. Our deterministic computation is exact (simulator), not approximate (LLM world model)\n- **Agent frameworks**: ReAct, Reflexion. Orthogonal — we analyze the routing decision within an agent loop\n\n### 5. Conclusion (0.3 pages)\n\n**Key points:**\n- Summary: death avoidance ≥90% of routing signal; episode-level counterfactual analysis as diagnostic methodology\n- **Limitations**: single benchmark (ScienceWorld), episode-level granularity (not step-level), DAgger distribution shift (train on pure strategies, deploy on mixed)\n- **Future work**: step-level labeling with denser reward signals, extension to MATH/code interpretation domains, DAgger-style iterative relabeling\n\n---\n\n## Figure/Table Plan\n\n### Table 1: Baseline Comparison\n| Method | Score | 90% CI | Success Rate | Death Rate | Sim Ratio |\n|--------|-------|--------|-------------|------------|-----------|\n| Always-Internal | -37.16 | [-43.39, -31.43] | 12.4% | 40.7% | 0.00 |\n| Always-Deterministic | -11.64 | [-17.39, -6.55] | 23.7% | 18.6% | 1.00 |\n| Oracle | -9.03 | [-14.14, -4.15] | 24.2% | 16.5% | 0.96 |\n| Random | -23.75 | [-29.60, -18.11] | 16.5% | 28.4% | 0.50 |\n| Keyword Heuristic (v1) | ≈ Always-Det | — | — | — | 0.86 |\n| Keyword Heuristic (v2) | ≈ Always-Int | — | — | — | 0.05 |\n| Learned Router (implicit) | TBD | — | — | — | TBD |\n\n*Source: plan-003-baseline, plan-011-rule-based*\n\n### Figure 1: Death Decomposition (core figure)\n- **Type**: Grouped bar chart or stacked bar\n- **X-axis**: 11 task types (sorted by death fraction)\n- **Y-axis**: Score delta (deterministic − internal)\n- **Bars**: Δ_full decomposed into Δ_death (death-avoidance component, dark) and Δ_nd (non-death component, light)\n- **Highlight**: find-non-living-thing as sole exception (Δ_nd = Δ_full = 9.58, zero deaths)\n- **Annotation**: Overall death fraction = 90.41%\n\n*Source: plan-012-full*\n\n### Figure 2: Cross-task Correlation (if space permits)\n- **Type**: Scatter plot with regression line\n- **X-axis**: Per-task death rate difference (internal − deterministic)\n- **Y-axis**: Δ_full per task\n- **Regression line**: r=0.9698, p=8.12e-07\n- **11 points**, labeled by task type\n- **Purpose**: Visually demonstrates near-perfect linear relationship\n\n*Source: plan-012-full, plan-012-decomposition*\n\n**Space strategy**: Figure 1 is mandatory. Figure 2 can be merged as an inset in Figure 1, or moved to appendix if space is tight. Table 1 is mandatory. Per-task breakdown table → appendix.\n\n---\n\n## Key References\n\n### Tool-Use Learning\n- Schick et al. (2024). Toolformer: Language Models Can Teach Themselves to Use Tools. *NeurIPS*\n- Paranjape et al. (2023). ART: Automatic Multi-step Reasoning and Tool-Use. *arXiv*\n- Lu et al. (2024). Chameleon: Plug-and-Play Compositional Reasoning with Large Language Models. *NeurIPS*\n- Hao et al. (2024). ToolkenGPT: Augmenting Frozen Language Models with Massive Tools via Tool Embeddings. *NeurIPS*\n\n### Agent Routing / Adaptive Computation\n- CogRouter — RL-based cognitive routing (ScienceWorld SOTA)\n- ITP-R — imagination-based routing to LLM world model\n- ARES — adaptive routing for efficient serving\n- Raposo et al. (2024). Mixture-of-Depths. *ICML*\n\n### Agent Frameworks\n- Yao et al. (2023). ReAct: Synergizing Reasoning and Acting in Language Models. *ICLR*\n- Shinn et al. (2023). Reflexion: Language Agents with Verbal Reinforcement Learning. *NeurIPS*\n\n### Methodology\n- Ross et al. (2011). A Reduction of Imitation Learning and Structured Prediction to No-Regret Online Learning. *AISTATS* (DAgger)\n\n### Environment\n- Wang et al. (2022). ScienceWorld: Is your Agent Smarter than a 5th Grader? *EMNLP*\n\n### Code Execution Routing\n- Gou et al. (2024). ReTool / ToRA — tool-integrated reasoning for math\n- Chen et al. (2023). AgentMath — code-augmented mathematical reasoning\n\n---\n\n## Provenance: Claims → Experiments\n\n| Claim | Source Experiment | Key Metric |\n|-------|------------------|------------|\n| Δ_full=+29.60, death fraction=90.41% | plan-012-full | delta_full, death_avoidance_fraction |\n| r=0.9698, p=8.12e-07 | plan-012-full | pearson_r, pearson_p |\n| Baseline scores (Table 1) | plan-003-baseline | metrics per condition |\n| Keyword heuristic failure | plan-011-rule-based | v1_match_rate, v2_match_rate |\n| Learned router internal_recall=51.5% | plan-004-ablation-b | per_class.internal.recall |\n| find-non-living-thing Δ=9.58 | plan-012-decomposition | key_tasks.find_non_living_thing |\n| Episode label distribution 86/9/150 | plan-012-full | label_dist |\n| Death rates: int 42.9%, det 16.3% | plan-012-full | death_rate_int, death_rate_det |\n| Per-step oracle 98% tie rate | plan-012-decomposition | (derived from label_dist) |\n",
    "structuredPatch": [
      {
        "oldStart": 50,
        "oldLines": 7,
        "newStart": 50,
        "newLines": 7,
        "lines": [
          "   - Δ_full=+29.60, Δ_nd=+2.84, death fraction=90.41% [A: plan-012-full, 245eps/11tasks]",
          "   - 10/11 death-prone tasks: death-dominated gaps",
          "   - 1 exception: find-non-living-thing (n=40, 0 deaths, Δ=+9.58 from non-death mechanisms) [A: plan-012-full, 245eps/11tasks]",
          "-  - Pearson r=0.9698 (p=8.12e-07)",
          "+  - Pearson r=0.9698 (p=8.12e-07) [A: plan-012-full, 245eps/11tasks]",
          " - **3.3 Baseline Comparison**:",
          "   - always-internal: -37.16, always-det: -11.64, oracle: -9.03, random: -23.75",
          "   - Keyword heuristic: structural failure (v1 85.8% match → ≈always-det; v2 4.9% → ≈always-internal)"
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  },
  "sourceToolAssistantUUID": "a0d56ed7-802a-42c8-b1be-50a73cfdfb73",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing",
  "sessionId": "fe1af098-4ed4-4fac-9d28-af54a02d46ce",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 40 · 2026-05-14T08:21:24.793Z_

<details open><summary>🔧 Tool call — Edit · `toolu_015fcDhiPdpnhPDbSyzmaDFb`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/_project/paper/paper_outline.md",
  "old_string": "  - always-internal: -37.16, always-det: -11.64, oracle: -9.03, random: -23.75",
  "new_string": "  - always-internal: -39.07, always-det: -9.47, oracle: -6.58, random: -22.38 [A: plan-003-baseline-245eps]"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c07e1f95-23b4-4d61-b840-478d3e8ac863",
  "isSidechain": false,
  "requestId": "req_011Cb28sMx2YfJfgVCErChHW",
  "type": "assistant",
  "uuid": "731c3ab7-b0cd-4f47-8567-70ffcf3d0eba",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing",
  "sessionId": "fe1af098-4ed4-4fac-9d28-af54a02d46ce",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015g9bvM4CFWx7MX13vYqYqx",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 266,
      "cache_read_input_tokens": 33491,
      "output_tokens": 227,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 266,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 227,
          "cache_read_input_tokens": 33491,
          "cache_creation_input_tokens": 266,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 266
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

_source line 41 · 2026-05-14T08:21:24.810Z_

<details><summary>↩ Tool result · `toolu_015fcDhiPdpnhPDbSyzmaDFb`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/_project/paper/paper_outline.md has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "731c3ab7-b0cd-4f47-8567-70ffcf3d0eba",
  "isSidechain": false,
  "promptId": "de32f0f5-b4f7-4fe9-872c-8108c929635d",
  "type": "user",
  "uuid": "bd995ead-a31c-465c-a232-0a2589e57f7a",
  "toolUseResult": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/_project/paper/paper_outline.md",
    "oldString": "  - always-internal: -37.16, always-det: -11.64, oracle: -9.03, random: -23.75",
    "newString": "  - always-internal: -39.07, always-det: -9.47, oracle: -6.58, random: -22.38 [A: plan-003-baseline-245eps]",
    "originalFile": "# EMNLP 2026 Short Paper Outline\n\n## Title Candidates\n\n1. **Death Avoidance Dominates Routing Signal: A Counterfactual Analysis of LLM Agent Tool Use in Interactive Environments**\n2. **When Does Deterministic Computation Help LLM Agents? Episode-Level Counterfactual Analysis Reveals Death Avoidance Dominance**\n3. **90% Death Avoidance: Decomposing the Routing Signal Between LLM Reasoning and Deterministic Simulation**\n\nRecommended: **Title 1** (clear claim + methodology in title; fits short paper convention of stating the finding)\n\n---\n\n## Abstract Skeleton (~150 words)\n\nKey points to cover:\n\n- **Problem**: LLM agents hallucinate state transitions in rule-governed environments, causing catastrophic failures (deaths). Routing between internal LLM reasoning and deterministic computation (simulators) can mitigate this, but what exactly does routing learn?\n- **Methodological gap**: Per-step oracle labeling degenerates in sparse-reward settings (98% tie rate on ScienceWorld). We propose episode-level counterfactual analysis.\n- **Core finding**: Death avoidance accounts for ~90% of routing signal (Δ_full=+29.60, Δ_no_death=+2.84, DAF=90.41%; Pearson r=0.97, p<1e-6 across 11 task types / 245 episodes) [A: plan-012-full, 245eps/11tasks]. Non-death performance is approximately equal between modalities.\n- **Supporting finding**: Keyword heuristics structurally fail (match rates degenerate to ≈always-det or ≈always-internal); episode-level counterfactual labels can train a lightweight router (internal_recall=51.5%).\n- **Implication**: The value of deterministic computation in interactive environments is concentrated in catastrophic failure prevention, not positive task guidance.\n\n---\n\n## Section Structure\n\n### 1. Introduction (0.8 pages)\n\n**Key points:**\n- LLM agents on rule-governed environments (physics, chemistry) suffer catastrophic failures from hallucinated state transitions → motivate the routing question\n- Existing work: tool-use learning (Toolformer, ART, Chameleon) learns *when* to invoke tools but doesn't analyze *what* routing learns; ITP-R routes to approximate world models but underperforms pure internal reasoning; ReTool/AgentMath use implicit routing entangled with backbone\n- Per-step oracle labeling degenerates in sparse-reward environments (98% tie rate) → need episode-level analysis\n- **Contributions** (bulleted):\n  1. Episode-level counterfactual methodology that overcomes per-step oracle degeneracy\n  2. Empirical finding: death avoidance accounts for ≥90% of routing signal on ScienceWorld (11 tasks, 245 episodes) [A: plan-012-full, 245eps/11tasks]\n  3. Structural failure analysis of keyword heuristics; demonstration that counterfactual labels can train a lightweight diagnostic router\n\n### 2. Method (1.0 pages)\n\n**Key points:**\n- **2.1 Problem Setup**: ScienceWorld environment; two computation modalities (internal LLM reasoning vs. deterministic simulation via environment forking); per-step routing decision\n- **2.2 Episode-Level Counterfactual Labeling**: Why per-step oracle fails (98% tie rate in sparse rewards) → run complete episodes under pure-internal and pure-deterministic strategies → compare episode-level scores → label: det-preferred / internal-preferred / no-preference. Distribution: 86 det-pref / 9 int-pref / 150 no-pref (245 episodes) [A: plan-012-full, 245eps/11tasks]\n- **2.3 Death Decomposition Framework**: Decompose Δ_full into death-avoidance component (Δ_death) and non-death component (Δ_nd). Death avoidance fraction = (Δ_full - Δ_nd) / Δ_full. Cross-task correlation: Pearson r between per-task death rate difference and Δ_full\n\n### 3. Experiments (1.5 pages)\n\n**Key points:**\n- **3.1 Setup**: Qwen3-1.7B backbone; ScienceWorld 11 task types × 20-40 episodes; evaluation: always-internal, always-deterministic, oracle, random, keyword heuristic, learned router\n- **3.2 Death Decomposition Results** (core result):\n  - Δ_full=+29.60, Δ_nd=+2.84, death fraction=90.41% [A: plan-012-full, 245eps/11tasks]\n  - 10/11 death-prone tasks: death-dominated gaps\n  - 1 exception: find-non-living-thing (n=40, 0 deaths, Δ=+9.58 from non-death mechanisms) [A: plan-012-full, 245eps/11tasks]\n  - Pearson r=0.9698 (p=8.12e-07) [A: plan-012-full, 245eps/11tasks]\n- **3.3 Baseline Comparison**:\n  - always-internal: -37.16, always-det: -11.64, oracle: -9.03, random: -23.75\n  - Keyword heuristic: structural failure (v1 85.8% match → ≈always-det; v2 4.9% → ≈always-internal)\n  - Learned router (ablation-b): internal_recall=51.5%, first non-degenerate; classification head variants all degenerate\n- **3.4 Analysis**: Death rate: internal 42.9% vs. deterministic 16.3%; alive-episode scores nearly equal across modalities\n\n### 4. Related Work (0.5 pages, integrated or separate)\n\n**Key points:**\n- **Tool-use learning**: Toolformer (self-supervised API insertion), ART (LLM-as-router), Chameleon (LLM-as-planner), ToolkenGPT (token-level triggers). Differentiation: episode-level counterfactual labeling, safety-aware framing, explicit modular router\n- **Adaptive computation / routing**: CogRouter (RL-based), ARES, Mixture-of-Depths. Our focus: empirical analysis of *what* routing learns, not a new routing architecture\n- **World model routing**: ITP-R, Dyna-Think. Our deterministic computation is exact (simulator), not approximate (LLM world model)\n- **Agent frameworks**: ReAct, Reflexion. Orthogonal — we analyze the routing decision within an agent loop\n\n### 5. Conclusion (0.3 pages)\n\n**Key points:**\n- Summary: death avoidance ≥90% of routing signal; episode-level counterfactual analysis as diagnostic methodology\n- **Limitations**: single benchmark (ScienceWorld), episode-level granularity (not step-level), DAgger distribution shift (train on pure strategies, deploy on mixed)\n- **Future work**: step-level labeling with denser reward signals, extension to MATH/code interpretation domains, DAgger-style iterative relabeling\n\n---\n\n## Figure/Table Plan\n\n### Table 1: Baseline Comparison\n| Method | Score | 90% CI | Success Rate | Death Rate | Sim Ratio |\n|--------|-------|--------|-------------|------------|-----------|\n| Always-Internal | -37.16 | [-43.39, -31.43] | 12.4% | 40.7% | 0.00 |\n| Always-Deterministic | -11.64 | [-17.39, -6.55] | 23.7% | 18.6% | 1.00 |\n| Oracle | -9.03 | [-14.14, -4.15] | 24.2% | 16.5% | 0.96 |\n| Random | -23.75 | [-29.60, -18.11] | 16.5% | 28.4% | 0.50 |\n| Keyword Heuristic (v1) | ≈ Always-Det | — | — | — | 0.86 |\n| Keyword Heuristic (v2) | ≈ Always-Int | — | — | — | 0.05 |\n| Learned Router (implicit) | TBD | — | — | — | TBD |\n\n*Source: plan-003-baseline, plan-011-rule-based*\n\n### Figure 1: Death Decomposition (core figure)\n- **Type**: Grouped bar chart or stacked bar\n- **X-axis**: 11 task types (sorted by death fraction)\n- **Y-axis**: Score delta (deterministic − internal)\n- **Bars**: Δ_full decomposed into Δ_death (death-avoidance component, dark) and Δ_nd (non-death component, light)\n- **Highlight**: find-non-living-thing as sole exception (Δ_nd = Δ_full = 9.58, zero deaths)\n- **Annotation**: Overall death fraction = 90.41%\n\n*Source: plan-012-full*\n\n### Figure 2: Cross-task Correlation (if space permits)\n- **Type**: Scatter plot with regression line\n- **X-axis**: Per-task death rate difference (internal − deterministic)\n- **Y-axis**: Δ_full per task\n- **Regression line**: r=0.9698, p=8.12e-07\n- **11 points**, labeled by task type\n- **Purpose**: Visually demonstrates near-perfect linear relationship\n\n*Source: plan-012-full, plan-012-decomposition*\n\n**Space strategy**: Figure 1 is mandatory. Figure 2 can be merged as an inset in Figure 1, or moved to appendix if space is tight. Table 1 is mandatory. Per-task breakdown table → appendix.\n\n---\n\n## Key References\n\n### Tool-Use Learning\n- Schick et al. (2024). Toolformer: Language Models Can Teach Themselves to Use Tools. *NeurIPS*\n- Paranjape et al. (2023). ART: Automatic Multi-step Reasoning and Tool-Use. *arXiv*\n- Lu et al. (2024). Chameleon: Plug-and-Play Compositional Reasoning with Large Language Models. *NeurIPS*\n- Hao et al. (2024). ToolkenGPT: Augmenting Frozen Language Models with Massive Tools via Tool Embeddings. *NeurIPS*\n\n### Agent Routing / Adaptive Computation\n- CogRouter — RL-based cognitive routing (ScienceWorld SOTA)\n- ITP-R — imagination-based routing to LLM world model\n- ARES — adaptive routing for efficient serving\n- Raposo et al. (2024). Mixture-of-Depths. *ICML*\n\n### Agent Frameworks\n- Yao et al. (2023). ReAct: Synergizing Reasoning and Acting in Language Models. *ICLR*\n- Shinn et al. (2023). Reflexion: Language Agents with Verbal Reinforcement Learning. *NeurIPS*\n\n### Methodology\n- Ross et al. (2011). A Reduction of Imitation Learning and Structured Prediction to No-Regret Online Learning. *AISTATS* (DAgger)\n\n### Environment\n- Wang et al. (2022). ScienceWorld: Is your Agent Smarter than a 5th Grader? *EMNLP*\n\n### Code Execution Routing\n- Gou et al. (2024). ReTool / ToRA — tool-integrated reasoning for math\n- Chen et al. (2023). AgentMath — code-augmented mathematical reasoning\n\n---\n\n## Provenance: Claims → Experiments\n\n| Claim | Source Experiment | Key Metric |\n|-------|------------------|------------|\n| Δ_full=+29.60, death fraction=90.41% | plan-012-full | delta_full, death_avoidance_fraction |\n| r=0.9698, p=8.12e-07 | plan-012-full | pearson_r, pearson_p |\n| Baseline scores (Table 1) | plan-003-baseline | metrics per condition |\n| Keyword heuristic failure | plan-011-rule-based | v1_match_rate, v2_match_rate |\n| Learned router internal_recall=51.5% | plan-004-ablation-b | per_class.internal.recall |\n| find-non-living-thing Δ=9.58 | plan-012-decomposition | key_tasks.find_non_living_thing |\n| Episode label distribution 86/9/150 | plan-012-full | label_dist |\n| Death rates: int 42.9%, det 16.3% | plan-012-full | death_rate_int, death_rate_det |\n| Per-step oracle 98% tie rate | plan-012-decomposition | (derived from label_dist) |\n",
    "structuredPatch": [
      {
        "oldStart": 52,
        "oldLines": 7,
        "newStart": 52,
        "newLines": 7,
        "lines": [
          "   - 1 exception: find-non-living-thing (n=40, 0 deaths, Δ=+9.58 from non-death mechanisms) [A: plan-012-full, 245eps/11tasks]",
          "   - Pearson r=0.9698 (p=8.12e-07) [A: plan-012-full, 245eps/11tasks]",
          " - **3.3 Baseline Comparison**:",
          "-  - always-internal: -37.16, always-det: -11.64, oracle: -9.03, random: -23.75",
          "+  - always-internal: -39.07, always-det: -9.47, oracle: -6.58, random: -22.38 [A: plan-003-baseline-245eps]",
          "   - Keyword heuristic: structural failure (v1 85.8% match → ≈always-det; v2 4.9% → ≈always-internal)",
          "   - Learned router (ablation-b): internal_recall=51.5%, first non-degenerate; classification head variants all degenerate",
          " - **3.4 Analysis**: Death rate: internal 42.9% vs. deterministic 16.3%; alive-episode scores nearly equal across modalities"
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  },
  "sourceToolAssistantUUID": "731c3ab7-b0cd-4f47-8567-70ffcf3d0eba",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing",
  "sessionId": "fe1af098-4ed4-4fac-9d28-af54a02d46ce",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 42_

```json
{
  "type": "last-prompt",
  "leafUuid": "bd995ead-a31c-465c-a232-0a2589e57f7a",
  "sessionId": "fe1af098-4ed4-4fac-9d28-af54a02d46ce"
}
```

---

### Runtime record

_source line 43_

```json
{
  "type": "ai-title",
  "aiTitle": "Update paper_outline.md baseline numbers to 245-ep",
  "sessionId": "fe1af098-4ed4-4fac-9d28-af54a02d46ce"
}
```

---

### Assistant

_source line 44 · 2026-05-14T08:21:27.249Z_

Now update Table 1 rows with new scores and mark old CIs as TBD.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bd995ead-a31c-465c-a232-0a2589e57f7a",
  "isSidechain": false,
  "requestId": "req_011Cb28sd7r9PZQ9nHGPQTU7",
  "type": "assistant",
  "uuid": "a81b9640-b82e-44d7-b6d0-3a1a46fa6fc1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing",
  "sessionId": "fe1af098-4ed4-4fac-9d28-af54a02d46ce",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Kw4bn9ptxav9NPRqe2FSu2",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 286,
      "cache_read_input_tokens": 33757,
      "output_tokens": 495,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 286,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 495,
          "cache_read_input_tokens": 33757,
          "cache_creation_input_tokens": 286,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 286
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

_source line 45 · 2026-05-14T08:21:30.791Z_

<details open><summary>🔧 Tool call — Edit · `toolu_01TZoBSjmibsaeUBYLFX6tmf`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/_project/paper/paper_outline.md",
  "old_string": "| Always-Internal | -37.16 | [-43.39, -31.43] | 12.4% | 40.7% | 0.00 |\n| Always-Deterministic | -11.64 | [-17.39, -6.55] | 23.7% | 18.6% | 1.00 |\n| Oracle | -9.03 | [-14.14, -4.15] | 24.2% | 16.5% | 0.96 |\n| Random | -23.75 | [-29.60, -18.11] | 16.5% | 28.4% | 0.50 |",
  "new_string": "| Always-Internal | -39.07 [A: plan-003-baseline-245eps] | TBD | TBD | TBD | 0.00 |\n| Always-Deterministic | -9.47 [A: plan-003-baseline-245eps] | TBD | TBD | TBD | 1.00 |\n| Oracle | -6.58 [A: plan-003-baseline-245eps] | TBD | TBD | TBD | 0.96 |\n| Random | -22.38 [A: plan-003-baseline-245eps] | TBD | TBD | TBD | 0.50 |"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a81b9640-b82e-44d7-b6d0-3a1a46fa6fc1",
  "isSidechain": false,
  "requestId": "req_011Cb28sd7r9PZQ9nHGPQTU7",
  "type": "assistant",
  "uuid": "605054f2-b1de-4b00-9114-0dad29956180",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing",
  "sessionId": "fe1af098-4ed4-4fac-9d28-af54a02d46ce",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Kw4bn9ptxav9NPRqe2FSu2",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 286,
      "cache_read_input_tokens": 33757,
      "output_tokens": 495,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 286,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 495,
          "cache_read_input_tokens": 33757,
          "cache_creation_input_tokens": 286,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 286
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

_source line 46 · 2026-05-14T08:21:30.802Z_

<details><summary>↩ Tool result · `toolu_01TZoBSjmibsaeUBYLFX6tmf`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/_project/paper/paper_outline.md has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "605054f2-b1de-4b00-9114-0dad29956180",
  "isSidechain": false,
  "promptId": "de32f0f5-b4f7-4fe9-872c-8108c929635d",
  "type": "user",
  "uuid": "0e5e3a75-ccc8-4f85-a7c6-110a6dff750d",
  "toolUseResult": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/_project/paper/paper_outline.md",
    "oldString": "| Always-Internal | -37.16 | [-43.39, -31.43] | 12.4% | 40.7% | 0.00 |\n| Always-Deterministic | -11.64 | [-17.39, -6.55] | 23.7% | 18.6% | 1.00 |\n| Oracle | -9.03 | [-14.14, -4.15] | 24.2% | 16.5% | 0.96 |\n| Random | -23.75 | [-29.60, -18.11] | 16.5% | 28.4% | 0.50 |",
    "newString": "| Always-Internal | -39.07 [A: plan-003-baseline-245eps] | TBD | TBD | TBD | 0.00 |\n| Always-Deterministic | -9.47 [A: plan-003-baseline-245eps] | TBD | TBD | TBD | 1.00 |\n| Oracle | -6.58 [A: plan-003-baseline-245eps] | TBD | TBD | TBD | 0.96 |\n| Random | -22.38 [A: plan-003-baseline-245eps] | TBD | TBD | TBD | 0.50 |",
    "originalFile": "# EMNLP 2026 Short Paper Outline\n\n## Title Candidates\n\n1. **Death Avoidance Dominates Routing Signal: A Counterfactual Analysis of LLM Agent Tool Use in Interactive Environments**\n2. **When Does Deterministic Computation Help LLM Agents? Episode-Level Counterfactual Analysis Reveals Death Avoidance Dominance**\n3. **90% Death Avoidance: Decomposing the Routing Signal Between LLM Reasoning and Deterministic Simulation**\n\nRecommended: **Title 1** (clear claim + methodology in title; fits short paper convention of stating the finding)\n\n---\n\n## Abstract Skeleton (~150 words)\n\nKey points to cover:\n\n- **Problem**: LLM agents hallucinate state transitions in rule-governed environments, causing catastrophic failures (deaths). Routing between internal LLM reasoning and deterministic computation (simulators) can mitigate this, but what exactly does routing learn?\n- **Methodological gap**: Per-step oracle labeling degenerates in sparse-reward settings (98% tie rate on ScienceWorld). We propose episode-level counterfactual analysis.\n- **Core finding**: Death avoidance accounts for ~90% of routing signal (Δ_full=+29.60, Δ_no_death=+2.84, DAF=90.41%; Pearson r=0.97, p<1e-6 across 11 task types / 245 episodes) [A: plan-012-full, 245eps/11tasks]. Non-death performance is approximately equal between modalities.\n- **Supporting finding**: Keyword heuristics structurally fail (match rates degenerate to ≈always-det or ≈always-internal); episode-level counterfactual labels can train a lightweight router (internal_recall=51.5%).\n- **Implication**: The value of deterministic computation in interactive environments is concentrated in catastrophic failure prevention, not positive task guidance.\n\n---\n\n## Section Structure\n\n### 1. Introduction (0.8 pages)\n\n**Key points:**\n- LLM agents on rule-governed environments (physics, chemistry) suffer catastrophic failures from hallucinated state transitions → motivate the routing question\n- Existing work: tool-use learning (Toolformer, ART, Chameleon) learns *when* to invoke tools but doesn't analyze *what* routing learns; ITP-R routes to approximate world models but underperforms pure internal reasoning; ReTool/AgentMath use implicit routing entangled with backbone\n- Per-step oracle labeling degenerates in sparse-reward environments (98% tie rate) → need episode-level analysis\n- **Contributions** (bulleted):\n  1. Episode-level counterfactual methodology that overcomes per-step oracle degeneracy\n  2. Empirical finding: death avoidance accounts for ≥90% of routing signal on ScienceWorld (11 tasks, 245 episodes) [A: plan-012-full, 245eps/11tasks]\n  3. Structural failure analysis of keyword heuristics; demonstration that counterfactual labels can train a lightweight diagnostic router\n\n### 2. Method (1.0 pages)\n\n**Key points:**\n- **2.1 Problem Setup**: ScienceWorld environment; two computation modalities (internal LLM reasoning vs. deterministic simulation via environment forking); per-step routing decision\n- **2.2 Episode-Level Counterfactual Labeling**: Why per-step oracle fails (98% tie rate in sparse rewards) → run complete episodes under pure-internal and pure-deterministic strategies → compare episode-level scores → label: det-preferred / internal-preferred / no-preference. Distribution: 86 det-pref / 9 int-pref / 150 no-pref (245 episodes) [A: plan-012-full, 245eps/11tasks]\n- **2.3 Death Decomposition Framework**: Decompose Δ_full into death-avoidance component (Δ_death) and non-death component (Δ_nd). Death avoidance fraction = (Δ_full - Δ_nd) / Δ_full. Cross-task correlation: Pearson r between per-task death rate difference and Δ_full\n\n### 3. Experiments (1.5 pages)\n\n**Key points:**\n- **3.1 Setup**: Qwen3-1.7B backbone; ScienceWorld 11 task types × 20-40 episodes; evaluation: always-internal, always-deterministic, oracle, random, keyword heuristic, learned router\n- **3.2 Death Decomposition Results** (core result):\n  - Δ_full=+29.60, Δ_nd=+2.84, death fraction=90.41% [A: plan-012-full, 245eps/11tasks]\n  - 10/11 death-prone tasks: death-dominated gaps\n  - 1 exception: find-non-living-thing (n=40, 0 deaths, Δ=+9.58 from non-death mechanisms) [A: plan-012-full, 245eps/11tasks]\n  - Pearson r=0.9698 (p=8.12e-07) [A: plan-012-full, 245eps/11tasks]\n- **3.3 Baseline Comparison**:\n  - always-internal: -39.07, always-det: -9.47, oracle: -6.58, random: -22.38 [A: plan-003-baseline-245eps]\n  - Keyword heuristic: structural failure (v1 85.8% match → ≈always-det; v2 4.9% → ≈always-internal)\n  - Learned router (ablation-b): internal_recall=51.5%, first non-degenerate; classification head variants all degenerate\n- **3.4 Analysis**: Death rate: internal 42.9% vs. deterministic 16.3%; alive-episode scores nearly equal across modalities\n\n### 4. Related Work (0.5 pages, integrated or separate)\n\n**Key points:**\n- **Tool-use learning**: Toolformer (self-supervised API insertion), ART (LLM-as-router), Chameleon (LLM-as-planner), ToolkenGPT (token-level triggers). Differentiation: episode-level counterfactual labeling, safety-aware framing, explicit modular router\n- **Adaptive computation / routing**: CogRouter (RL-based), ARES, Mixture-of-Depths. Our focus: empirical analysis of *what* routing learns, not a new routing architecture\n- **World model routing**: ITP-R, Dyna-Think. Our deterministic computation is exact (simulator), not approximate (LLM world model)\n- **Agent frameworks**: ReAct, Reflexion. Orthogonal — we analyze the routing decision within an agent loop\n\n### 5. Conclusion (0.3 pages)\n\n**Key points:**\n- Summary: death avoidance ≥90% of routing signal; episode-level counterfactual analysis as diagnostic methodology\n- **Limitations**: single benchmark (ScienceWorld), episode-level granularity (not step-level), DAgger distribution shift (train on pure strategies, deploy on mixed)\n- **Future work**: step-level labeling with denser reward signals, extension to MATH/code interpretation domains, DAgger-style iterative relabeling\n\n---\n\n## Figure/Table Plan\n\n### Table 1: Baseline Comparison\n| Method | Score | 90% CI | Success Rate | Death Rate | Sim Ratio |\n|--------|-------|--------|-------------|------------|-----------|\n| Always-Internal | -37.16 | [-43.39, -31.43] | 12.4% | 40.7% | 0.00 |\n| Always-Deterministic | -11.64 | [-17.39, -6.55] | 23.7% | 18.6% | 1.00 |\n| Oracle | -9.03 | [-14.14, -4.15] | 24.2% | 16.5% | 0.96 |\n| Random | -23.75 | [-29.60, -18.11] | 16.5% | 28.4% | 0.50 |\n| Keyword Heuristic (v1) | ≈ Always-Det | — | — | — | 0.86 |\n| Keyword Heuristic (v2) | ≈ Always-Int | — | — | — | 0.05 |\n| Learned Router (implicit) | TBD | — | — | — | TBD |\n\n*Source: plan-003-baseline, plan-011-rule-based*\n\n### Figure 1: Death Decomposition (core figure)\n- **Type**: Grouped bar chart or stacked bar\n- **X-axis**: 11 task types (sorted by death fraction)\n- **Y-axis**: Score delta (deterministic − internal)\n- **Bars**: Δ_full decomposed into Δ_death (death-avoidance component, dark) and Δ_nd (non-death component, light)\n- **Highlight**: find-non-living-thing as sole exception (Δ_nd = Δ_full = 9.58, zero deaths)\n- **Annotation**: Overall death fraction = 90.41%\n\n*Source: plan-012-full*\n\n### Figure 2: Cross-task Correlation (if space permits)\n- **Type**: Scatter plot with regression line\n- **X-axis**: Per-task death rate difference (internal − deterministic)\n- **Y-axis**: Δ_full per task\n- **Regression line**: r=0.9698, p=8.12e-07\n- **11 points**, labeled by task type\n- **Purpose**: Visually demonstrates near-perfect linear relationship\n\n*Source: plan-012-full, plan-012-decomposition*\n\n**Space strategy**: Figure 1 is mandatory. Figure 2 can be merged as an inset in Figure 1, or moved to appendix if space is tight. Table 1 is mandatory. Per-task breakdown table → appendix.\n\n---\n\n## Key References\n\n### Tool-Use Learning\n- Schick et al. (2024). Toolformer: Language Models Can Teach Themselves to Use Tools. *NeurIPS*\n- Paranjape et al. (2023). ART: Automatic Multi-step Reasoning and Tool-Use. *arXiv*\n- Lu et al. (2024). Chameleon: Plug-and-Play Compositional Reasoning with Large Language Models. *NeurIPS*\n- Hao et al. (2024). ToolkenGPT: Augmenting Frozen Language Models with Massive Tools via Tool Embeddings. *NeurIPS*\n\n### Agent Routing / Adaptive Computation\n- CogRouter — RL-based cognitive routing (ScienceWorld SOTA)\n- ITP-R — imagination-based routing to LLM world model\n- ARES — adaptive routing for efficient serving\n- Raposo et al. (2024). Mixture-of-Depths. *ICML*\n\n### Agent Frameworks\n- Yao et al. (2023). ReAct: Synergizing Reasoning and Acting in Language Models. *ICLR*\n- Shinn et al. (2023). Reflexion: Language Agents with Verbal Reinforcement Learning. *NeurIPS*\n\n### Methodology\n- Ross et al. (2011). A Reduction of Imitation Learning and Structured Prediction to No-Regret Online Learning. *AISTATS* (DAgger)\n\n### Environment\n- Wang et al. (2022). ScienceWorld: Is your Agent Smarter than a 5th Grader? *EMNLP*\n\n### Code Execution Routing\n- Gou et al. (2024). ReTool / ToRA — tool-integrated reasoning for math\n- Chen et al. (2023). AgentMath — code-augmented mathematical reasoning\n\n---\n\n## Provenance: Claims → Experiments\n\n| Claim | Source Experiment | Key Metric |\n|-------|------------------|------------|\n| Δ_full=+29.60, death fraction=90.41% | plan-012-full | delta_full, death_avoidance_fraction |\n| r=0.9698, p=8.12e-07 | plan-012-full | pearson_r, pearson_p |\n| Baseline scores (Table 1) | plan-003-baseline | metrics per condition |\n| Keyword heuristic failure | plan-011-rule-based | v1_match_rate, v2_match_rate |\n| Learned router internal_recall=51.5% | plan-004-ablation-b | per_class.internal.recall |\n| find-non-living-thing Δ=9.58 | plan-012-decomposition | key_tasks.find_non_living_thing |\n| Episode label distribution 86/9/150 | plan-012-full | label_dist |\n| Death rates: int 42.9%, det 16.3% | plan-012-full | death_rate_int, death_rate_det |\n| Per-step oracle 98% tie rate | plan-012-decomposition | (derived from label_dist) |\n",
    "structuredPatch": [
      {
        "oldStart": 79,
        "oldLines": 10,
        "newStart": 79,
        "newLines": 10,
        "lines": [
          " ### Table 1: Baseline Comparison",
          " | Method | Score | 90% CI | Success Rate | Death Rate | Sim Ratio |",
          " |--------|-------|--------|-------------|------------|-----------|",
          "-| Always-Internal | -37.16 | [-43.39, -31.43] | 12.4% | 40.7% | 0.00 |",
          "-| Always-Deterministic | -11.64 | [-17.39, -6.55] | 23.7% | 18.6% | 1.00 |",
          "-| Oracle | -9.03 | [-14.14, -4.15] | 24.2% | 16.5% | 0.96 |",
          "-| Random | -23.75 | [-29.60, -18.11] | 16.5% | 28.4% | 0.50 |",
          "+| Always-Internal | -39.07 [A: plan-003-baseline-245eps] | TBD | TBD | TBD | 0.00 |",
          "+| Always-Deterministic | -9.47 [A: plan-003-baseline-245eps] | TBD | TBD | TBD | 1.00 |",
          "+| Oracle | -6.58 [A: plan-003-baseline-245eps] | TBD | TBD | TBD | 0.96 |",
          "+| Random | -22.38 [A: plan-003-baseline-245eps] | TBD | TBD | TBD | 0.50 |",
          " | Keyword Heuristic (v1) | ≈ Always-Det | — | — | — | 0.86 |",
          " | Keyword Heuristic (v2) | ≈ Always-Int | — | — | — | 0.05 |",
          " | Learned Router (implicit) | TBD | — | — | — | TBD |"
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  },
  "sourceToolAssistantUUID": "605054f2-b1de-4b00-9114-0dad29956180",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing",
  "sessionId": "fe1af098-4ed4-4fac-9d28-af54a02d46ce",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 47 · 2026-05-14T08:21:34.419Z_

<details open><summary>🔧 Tool call — Edit · `toolu_01647bBWJVU79FCMhXXtQR79`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/_project/paper/paper_outline.md",
  "old_string": "*Source: plan-003-baseline, plan-011-rule-based*",
  "new_string": "*Source: plan-003-baseline-245eps, plan-011-rule-based*"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0e5e3a75-ccc8-4f85-a7c6-110a6dff750d",
  "isSidechain": false,
  "requestId": "req_011Cb28t4hEUcVevoKFp5hQL",
  "type": "assistant",
  "uuid": "ae46cc65-a80c-4637-9838-ce6c585ef94e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing",
  "sessionId": "fe1af098-4ed4-4fac-9d28-af54a02d46ce",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EvbnzsKLRhGMYcRJ8QRn4C",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 554,
      "cache_read_input_tokens": 34043,
      "output_tokens": 185,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 554,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 185,
          "cache_read_input_tokens": 34043,
          "cache_creation_input_tokens": 554,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 554
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

_source line 48 · 2026-05-14T08:21:34.430Z_

<details><summary>↩ Tool result · `toolu_01647bBWJVU79FCMhXXtQR79`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/_project/paper/paper_outline.md has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ae46cc65-a80c-4637-9838-ce6c585ef94e",
  "isSidechain": false,
  "promptId": "de32f0f5-b4f7-4fe9-872c-8108c929635d",
  "type": "user",
  "uuid": "259bf43c-b9fd-4ff7-a19f-fe86b01e22a9",
  "toolUseResult": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/_project/paper/paper_outline.md",
    "oldString": "*Source: plan-003-baseline, plan-011-rule-based*",
    "newString": "*Source: plan-003-baseline-245eps, plan-011-rule-based*",
    "originalFile": "# EMNLP 2026 Short Paper Outline\n\n## Title Candidates\n\n1. **Death Avoidance Dominates Routing Signal: A Counterfactual Analysis of LLM Agent Tool Use in Interactive Environments**\n2. **When Does Deterministic Computation Help LLM Agents? Episode-Level Counterfactual Analysis Reveals Death Avoidance Dominance**\n3. **90% Death Avoidance: Decomposing the Routing Signal Between LLM Reasoning and Deterministic Simulation**\n\nRecommended: **Title 1** (clear claim + methodology in title; fits short paper convention of stating the finding)\n\n---\n\n## Abstract Skeleton (~150 words)\n\nKey points to cover:\n\n- **Problem**: LLM agents hallucinate state transitions in rule-governed environments, causing catastrophic failures (deaths). Routing between internal LLM reasoning and deterministic computation (simulators) can mitigate this, but what exactly does routing learn?\n- **Methodological gap**: Per-step oracle labeling degenerates in sparse-reward settings (98% tie rate on ScienceWorld). We propose episode-level counterfactual analysis.\n- **Core finding**: Death avoidance accounts for ~90% of routing signal (Δ_full=+29.60, Δ_no_death=+2.84, DAF=90.41%; Pearson r=0.97, p<1e-6 across 11 task types / 245 episodes) [A: plan-012-full, 245eps/11tasks]. Non-death performance is approximately equal between modalities.\n- **Supporting finding**: Keyword heuristics structurally fail (match rates degenerate to ≈always-det or ≈always-internal); episode-level counterfactual labels can train a lightweight router (internal_recall=51.5%).\n- **Implication**: The value of deterministic computation in interactive environments is concentrated in catastrophic failure prevention, not positive task guidance.\n\n---\n\n## Section Structure\n\n### 1. Introduction (0.8 pages)\n\n**Key points:**\n- LLM agents on rule-governed environments (physics, chemistry) suffer catastrophic failures from hallucinated state transitions → motivate the routing question\n- Existing work: tool-use learning (Toolformer, ART, Chameleon) learns *when* to invoke tools but doesn't analyze *what* routing learns; ITP-R routes to approximate world models but underperforms pure internal reasoning; ReTool/AgentMath use implicit routing entangled with backbone\n- Per-step oracle labeling degenerates in sparse-reward environments (98% tie rate) → need episode-level analysis\n- **Contributions** (bulleted):\n  1. Episode-level counterfactual methodology that overcomes per-step oracle degeneracy\n  2. Empirical finding: death avoidance accounts for ≥90% of routing signal on ScienceWorld (11 tasks, 245 episodes) [A: plan-012-full, 245eps/11tasks]\n  3. Structural failure analysis of keyword heuristics; demonstration that counterfactual labels can train a lightweight diagnostic router\n\n### 2. Method (1.0 pages)\n\n**Key points:**\n- **2.1 Problem Setup**: ScienceWorld environment; two computation modalities (internal LLM reasoning vs. deterministic simulation via environment forking); per-step routing decision\n- **2.2 Episode-Level Counterfactual Labeling**: Why per-step oracle fails (98% tie rate in sparse rewards) → run complete episodes under pure-internal and pure-deterministic strategies → compare episode-level scores → label: det-preferred / internal-preferred / no-preference. Distribution: 86 det-pref / 9 int-pref / 150 no-pref (245 episodes) [A: plan-012-full, 245eps/11tasks]\n- **2.3 Death Decomposition Framework**: Decompose Δ_full into death-avoidance component (Δ_death) and non-death component (Δ_nd). Death avoidance fraction = (Δ_full - Δ_nd) / Δ_full. Cross-task correlation: Pearson r between per-task death rate difference and Δ_full\n\n### 3. Experiments (1.5 pages)\n\n**Key points:**\n- **3.1 Setup**: Qwen3-1.7B backbone; ScienceWorld 11 task types × 20-40 episodes; evaluation: always-internal, always-deterministic, oracle, random, keyword heuristic, learned router\n- **3.2 Death Decomposition Results** (core result):\n  - Δ_full=+29.60, Δ_nd=+2.84, death fraction=90.41% [A: plan-012-full, 245eps/11tasks]\n  - 10/11 death-prone tasks: death-dominated gaps\n  - 1 exception: find-non-living-thing (n=40, 0 deaths, Δ=+9.58 from non-death mechanisms) [A: plan-012-full, 245eps/11tasks]\n  - Pearson r=0.9698 (p=8.12e-07) [A: plan-012-full, 245eps/11tasks]\n- **3.3 Baseline Comparison**:\n  - always-internal: -39.07, always-det: -9.47, oracle: -6.58, random: -22.38 [A: plan-003-baseline-245eps]\n  - Keyword heuristic: structural failure (v1 85.8% match → ≈always-det; v2 4.9% → ≈always-internal)\n  - Learned router (ablation-b): internal_recall=51.5%, first non-degenerate; classification head variants all degenerate\n- **3.4 Analysis**: Death rate: internal 42.9% vs. deterministic 16.3%; alive-episode scores nearly equal across modalities\n\n### 4. Related Work (0.5 pages, integrated or separate)\n\n**Key points:**\n- **Tool-use learning**: Toolformer (self-supervised API insertion), ART (LLM-as-router), Chameleon (LLM-as-planner), ToolkenGPT (token-level triggers). Differentiation: episode-level counterfactual labeling, safety-aware framing, explicit modular router\n- **Adaptive computation / routing**: CogRouter (RL-based), ARES, Mixture-of-Depths. Our focus: empirical analysis of *what* routing learns, not a new routing architecture\n- **World model routing**: ITP-R, Dyna-Think. Our deterministic computation is exact (simulator), not approximate (LLM world model)\n- **Agent frameworks**: ReAct, Reflexion. Orthogonal — we analyze the routing decision within an agent loop\n\n### 5. Conclusion (0.3 pages)\n\n**Key points:**\n- Summary: death avoidance ≥90% of routing signal; episode-level counterfactual analysis as diagnostic methodology\n- **Limitations**: single benchmark (ScienceWorld), episode-level granularity (not step-level), DAgger distribution shift (train on pure strategies, deploy on mixed)\n- **Future work**: step-level labeling with denser reward signals, extension to MATH/code interpretation domains, DAgger-style iterative relabeling\n\n---\n\n## Figure/Table Plan\n\n### Table 1: Baseline Comparison\n| Method | Score | 90% CI | Success Rate | Death Rate | Sim Ratio |\n|--------|-------|--------|-------------|------------|-----------|\n| Always-Internal | -39.07 [A: plan-003-baseline-245eps] | TBD | TBD | TBD | 0.00 |\n| Always-Deterministic | -9.47 [A: plan-003-baseline-245eps] | TBD | TBD | TBD | 1.00 |\n| Oracle | -6.58 [A: plan-003-baseline-245eps] | TBD | TBD | TBD | 0.96 |\n| Random | -22.38 [A: plan-003-baseline-245eps] | TBD | TBD | TBD | 0.50 |\n| Keyword Heuristic (v1) | ≈ Always-Det | — | — | — | 0.86 |\n| Keyword Heuristic (v2) | ≈ Always-Int | — | — | — | 0.05 |\n| Learned Router (implicit) | TBD | — | — | — | TBD |\n\n*Source: plan-003-baseline, plan-011-rule-based*\n\n### Figure 1: Death Decomposition (core figure)\n- **Type**: Grouped bar chart or stacked bar\n- **X-axis**: 11 task types (sorted by death fraction)\n- **Y-axis**: Score delta (deterministic − internal)\n- **Bars**: Δ_full decomposed into Δ_death (death-avoidance component, dark) and Δ_nd (non-death component, light)\n- **Highlight**: find-non-living-thing as sole exception (Δ_nd = Δ_full = 9.58, zero deaths)\n- **Annotation**: Overall death fraction = 90.41%\n\n*Source: plan-012-full*\n\n### Figure 2: Cross-task Correlation (if space permits)\n- **Type**: Scatter plot with regression line\n- **X-axis**: Per-task death rate difference (internal − deterministic)\n- **Y-axis**: Δ_full per task\n- **Regression line**: r=0.9698, p=8.12e-07\n- **11 points**, labeled by task type\n- **Purpose**: Visually demonstrates near-perfect linear relationship\n\n*Source: plan-012-full, plan-012-decomposition*\n\n**Space strategy**: Figure 1 is mandatory. Figure 2 can be merged as an inset in Figure 1, or moved to appendix if space is tight. Table 1 is mandatory. Per-task breakdown table → appendix.\n\n---\n\n## Key References\n\n### Tool-Use Learning\n- Schick et al. (2024). Toolformer: Language Models Can Teach Themselves to Use Tools. *NeurIPS*\n- Paranjape et al. (2023). ART: Automatic Multi-step Reasoning and Tool-Use. *arXiv*\n- Lu et al. (2024). Chameleon: Plug-and-Play Compositional Reasoning with Large Language Models. *NeurIPS*\n- Hao et al. (2024). ToolkenGPT: Augmenting Frozen Language Models with Massive Tools via Tool Embeddings. *NeurIPS*\n\n### Agent Routing / Adaptive Computation\n- CogRouter — RL-based cognitive routing (ScienceWorld SOTA)\n- ITP-R — imagination-based routing to LLM world model\n- ARES — adaptive routing for efficient serving\n- Raposo et al. (2024). Mixture-of-Depths. *ICML*\n\n### Agent Frameworks\n- Yao et al. (2023). ReAct: Synergizing Reasoning and Acting in Language Models. *ICLR*\n- Shinn et al. (2023). Reflexion: Language Agents with Verbal Reinforcement Learning. *NeurIPS*\n\n### Methodology\n- Ross et al. (2011). A Reduction of Imitation Learning and Structured Prediction to No-Regret Online Learning. *AISTATS* (DAgger)\n\n### Environment\n- Wang et al. (2022). ScienceWorld: Is your Agent Smarter than a 5th Grader? *EMNLP*\n\n### Code Execution Routing\n- Gou et al. (2024). ReTool / ToRA — tool-integrated reasoning for math\n- Chen et al. (2023). AgentMath — code-augmented mathematical reasoning\n\n---\n\n## Provenance: Claims → Experiments\n\n| Claim | Source Experiment | Key Metric |\n|-------|------------------|------------|\n| Δ_full=+29.60, death fraction=90.41% | plan-012-full | delta_full, death_avoidance_fraction |\n| r=0.9698, p=8.12e-07 | plan-012-full | pearson_r, pearson_p |\n| Baseline scores (Table 1) | plan-003-baseline | metrics per condition |\n| Keyword heuristic failure | plan-011-rule-based | v1_match_rate, v2_match_rate |\n| Learned router internal_recall=51.5% | plan-004-ablation-b | per_class.internal.recall |\n| find-non-living-thing Δ=9.58 | plan-012-decomposition | key_tasks.find_non_living_thing |\n| Episode label distribution 86/9/150 | plan-012-full | label_dist |\n| Death rates: int 42.9%, det 16.3% | plan-012-full | death_rate_int, death_rate_det |\n| Per-step oracle 98% tie rate | plan-012-decomposition | (derived from label_dist) |\n",
    "structuredPatch": [
      {
        "oldStart": 87,
        "oldLines": 7,
        "newStart": 87,
        "newLines": 7,
        "lines": [
          " | Keyword Heuristic (v2) | ≈ Always-Int | — | — | — | 0.05 |",
          " | Learned Router (implicit) | TBD | — | — | — | TBD |",
          " ",
          "-*Source: plan-003-baseline, plan-011-rule-based*",
          "+*Source: plan-003-baseline-245eps, plan-011-rule-based*",
          " ",
          " ### Figure 1: Death Decomposition (core figure)",
          " - **Type**: Grouped bar chart or stacked bar"
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  },
  "sourceToolAssistantUUID": "ae46cc65-a80c-4637-9838-ce6c585ef94e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing",
  "sessionId": "fe1af098-4ed4-4fac-9d28-af54a02d46ce",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 49 · 2026-05-14T08:21:39.015Z_

<details open><summary>🔧 Tool call — Edit · `toolu_01KXMCSr1L1dFVAEra11QxUw`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/_project/paper/paper_outline.md",
  "old_string": "- **3.4 Analysis**: Death rate: internal 42.9% vs. deterministic 16.3%; alive-episode scores nearly equal across modalities",
  "new_string": "- **3.4 Analysis**: Death rate: internal 42.9% vs. deterministic 16.3%; alive-episode scores nearly equal across modalities [A: plan-012-full, 245eps/11tasks]"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "259bf43c-b9fd-4ff7-a19f-fe86b01e22a9",
  "isSidechain": false,
  "requestId": "req_011Cb28tLRXhkzaviCZsTjaF",
  "type": "assistant",
  "uuid": "44a8625a-4c96-4d5f-9b6f-4213d97c229d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing",
  "sessionId": "fe1af098-4ed4-4fac-9d28-af54a02d46ce",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Hqp3CNFwHHvH7cN234GE1i",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 244,
      "cache_read_input_tokens": 34597,
      "output_tokens": 234,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 244,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 234,
          "cache_read_input_tokens": 34597,
          "cache_creation_input_tokens": 244,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 244
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

_source line 50 · 2026-05-14T08:21:39.045Z_

<details><summary>↩ Tool result · `toolu_01KXMCSr1L1dFVAEra11QxUw`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/_project/paper/paper_outline.md has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "44a8625a-4c96-4d5f-9b6f-4213d97c229d",
  "isSidechain": false,
  "promptId": "de32f0f5-b4f7-4fe9-872c-8108c929635d",
  "type": "user",
  "uuid": "51171018-ec94-4f39-81bd-7e94bb0ce170",
  "toolUseResult": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/_project/paper/paper_outline.md",
    "oldString": "- **3.4 Analysis**: Death rate: internal 42.9% vs. deterministic 16.3%; alive-episode scores nearly equal across modalities",
    "newString": "- **3.4 Analysis**: Death rate: internal 42.9% vs. deterministic 16.3%; alive-episode scores nearly equal across modalities [A: plan-012-full, 245eps/11tasks]",
    "originalFile": "# EMNLP 2026 Short Paper Outline\n\n## Title Candidates\n\n1. **Death Avoidance Dominates Routing Signal: A Counterfactual Analysis of LLM Agent Tool Use in Interactive Environments**\n2. **When Does Deterministic Computation Help LLM Agents? Episode-Level Counterfactual Analysis Reveals Death Avoidance Dominance**\n3. **90% Death Avoidance: Decomposing the Routing Signal Between LLM Reasoning and Deterministic Simulation**\n\nRecommended: **Title 1** (clear claim + methodology in title; fits short paper convention of stating the finding)\n\n---\n\n## Abstract Skeleton (~150 words)\n\nKey points to cover:\n\n- **Problem**: LLM agents hallucinate state transitions in rule-governed environments, causing catastrophic failures (deaths). Routing between internal LLM reasoning and deterministic computation (simulators) can mitigate this, but what exactly does routing learn?\n- **Methodological gap**: Per-step oracle labeling degenerates in sparse-reward settings (98% tie rate on ScienceWorld). We propose episode-level counterfactual analysis.\n- **Core finding**: Death avoidance accounts for ~90% of routing signal (Δ_full=+29.60, Δ_no_death=+2.84, DAF=90.41%; Pearson r=0.97, p<1e-6 across 11 task types / 245 episodes) [A: plan-012-full, 245eps/11tasks]. Non-death performance is approximately equal between modalities.\n- **Supporting finding**: Keyword heuristics structurally fail (match rates degenerate to ≈always-det or ≈always-internal); episode-level counterfactual labels can train a lightweight router (internal_recall=51.5%).\n- **Implication**: The value of deterministic computation in interactive environments is concentrated in catastrophic failure prevention, not positive task guidance.\n\n---\n\n## Section Structure\n\n### 1. Introduction (0.8 pages)\n\n**Key points:**\n- LLM agents on rule-governed environments (physics, chemistry) suffer catastrophic failures from hallucinated state transitions → motivate the routing question\n- Existing work: tool-use learning (Toolformer, ART, Chameleon) learns *when* to invoke tools but doesn't analyze *what* routing learns; ITP-R routes to approximate world models but underperforms pure internal reasoning; ReTool/AgentMath use implicit routing entangled with backbone\n- Per-step oracle labeling degenerates in sparse-reward environments (98% tie rate) → need episode-level analysis\n- **Contributions** (bulleted):\n  1. Episode-level counterfactual methodology that overcomes per-step oracle degeneracy\n  2. Empirical finding: death avoidance accounts for ≥90% of routing signal on ScienceWorld (11 tasks, 245 episodes) [A: plan-012-full, 245eps/11tasks]\n  3. Structural failure analysis of keyword heuristics; demonstration that counterfactual labels can train a lightweight diagnostic router\n\n### 2. Method (1.0 pages)\n\n**Key points:**\n- **2.1 Problem Setup**: ScienceWorld environment; two computation modalities (internal LLM reasoning vs. deterministic simulation via environment forking); per-step routing decision\n- **2.2 Episode-Level Counterfactual Labeling**: Why per-step oracle fails (98% tie rate in sparse rewards) → run complete episodes under pure-internal and pure-deterministic strategies → compare episode-level scores → label: det-preferred / internal-preferred / no-preference. Distribution: 86 det-pref / 9 int-pref / 150 no-pref (245 episodes) [A: plan-012-full, 245eps/11tasks]\n- **2.3 Death Decomposition Framework**: Decompose Δ_full into death-avoidance component (Δ_death) and non-death component (Δ_nd). Death avoidance fraction = (Δ_full - Δ_nd) / Δ_full. Cross-task correlation: Pearson r between per-task death rate difference and Δ_full\n\n### 3. Experiments (1.5 pages)\n\n**Key points:**\n- **3.1 Setup**: Qwen3-1.7B backbone; ScienceWorld 11 task types × 20-40 episodes; evaluation: always-internal, always-deterministic, oracle, random, keyword heuristic, learned router\n- **3.2 Death Decomposition Results** (core result):\n  - Δ_full=+29.60, Δ_nd=+2.84, death fraction=90.41% [A: plan-012-full, 245eps/11tasks]\n  - 10/11 death-prone tasks: death-dominated gaps\n  - 1 exception: find-non-living-thing (n=40, 0 deaths, Δ=+9.58 from non-death mechanisms) [A: plan-012-full, 245eps/11tasks]\n  - Pearson r=0.9698 (p=8.12e-07) [A: plan-012-full, 245eps/11tasks]\n- **3.3 Baseline Comparison**:\n  - always-internal: -39.07, always-det: -9.47, oracle: -6.58, random: -22.38 [A: plan-003-baseline-245eps]\n  - Keyword heuristic: structural failure (v1 85.8% match → ≈always-det; v2 4.9% → ≈always-internal)\n  - Learned router (ablation-b): internal_recall=51.5%, first non-degenerate; classification head variants all degenerate\n- **3.4 Analysis**: Death rate: internal 42.9% vs. deterministic 16.3%; alive-episode scores nearly equal across modalities\n\n### 4. Related Work (0.5 pages, integrated or separate)\n\n**Key points:**\n- **Tool-use learning**: Toolformer (self-supervised API insertion), ART (LLM-as-router), Chameleon (LLM-as-planner), ToolkenGPT (token-level triggers). Differentiation: episode-level counterfactual labeling, safety-aware framing, explicit modular router\n- **Adaptive computation / routing**: CogRouter (RL-based), ARES, Mixture-of-Depths. Our focus: empirical analysis of *what* routing learns, not a new routing architecture\n- **World model routing**: ITP-R, Dyna-Think. Our deterministic computation is exact (simulator), not approximate (LLM world model)\n- **Agent frameworks**: ReAct, Reflexion. Orthogonal — we analyze the routing decision within an agent loop\n\n### 5. Conclusion (0.3 pages)\n\n**Key points:**\n- Summary: death avoidance ≥90% of routing signal; episode-level counterfactual analysis as diagnostic methodology\n- **Limitations**: single benchmark (ScienceWorld), episode-level granularity (not step-level), DAgger distribution shift (train on pure strategies, deploy on mixed)\n- **Future work**: step-level labeling with denser reward signals, extension to MATH/code interpretation domains, DAgger-style iterative relabeling\n\n---\n\n## Figure/Table Plan\n\n### Table 1: Baseline Comparison\n| Method | Score | 90% CI | Success Rate | Death Rate | Sim Ratio |\n|--------|-------|--------|-------------|------------|-----------|\n| Always-Internal | -39.07 [A: plan-003-baseline-245eps] | TBD | TBD | TBD | 0.00 |\n| Always-Deterministic | -9.47 [A: plan-003-baseline-245eps] | TBD | TBD | TBD | 1.00 |\n| Oracle | -6.58 [A: plan-003-baseline-245eps] | TBD | TBD | TBD | 0.96 |\n| Random | -22.38 [A: plan-003-baseline-245eps] | TBD | TBD | TBD | 0.50 |\n| Keyword Heuristic (v1) | ≈ Always-Det | — | — | — | 0.86 |\n| Keyword Heuristic (v2) | ≈ Always-Int | — | — | — | 0.05 |\n| Learned Router (implicit) | TBD | — | — | — | TBD |\n\n*Source: plan-003-baseline-245eps, plan-011-rule-based*\n\n### Figure 1: Death Decomposition (core figure)\n- **Type**: Grouped bar chart or stacked bar\n- **X-axis**: 11 task types (sorted by death fraction)\n- **Y-axis**: Score delta (deterministic − internal)\n- **Bars**: Δ_full decomposed into Δ_death (death-avoidance component, dark) and Δ_nd (non-death component, light)\n- **Highlight**: find-non-living-thing as sole exception (Δ_nd = Δ_full = 9.58, zero deaths)\n- **Annotation**: Overall death fraction = 90.41%\n\n*Source: plan-012-full*\n\n### Figure 2: Cross-task Correlation (if space permits)\n- **Type**: Scatter plot with regression line\n- **X-axis**: Per-task death rate difference (internal − deterministic)\n- **Y-axis**: Δ_full per task\n- **Regression line**: r=0.9698, p=8.12e-07\n- **11 points**, labeled by task type\n- **Purpose**: Visually demonstrates near-perfect linear relationship\n\n*Source: plan-012-full, plan-012-decomposition*\n\n**Space strategy**: Figure 1 is mandatory. Figure 2 can be merged as an inset in Figure 1, or moved to appendix if space is tight. Table 1 is mandatory. Per-task breakdown table → appendix.\n\n---\n\n## Key References\n\n### Tool-Use Learning\n- Schick et al. (2024). Toolformer: Language Models Can Teach Themselves to Use Tools. *NeurIPS*\n- Paranjape et al. (2023). ART: Automatic Multi-step Reasoning and Tool-Use. *arXiv*\n- Lu et al. (2024). Chameleon: Plug-and-Play Compositional Reasoning with Large Language Models. *NeurIPS*\n- Hao et al. (2024). ToolkenGPT: Augmenting Frozen Language Models with Massive Tools via Tool Embeddings. *NeurIPS*\n\n### Agent Routing / Adaptive Computation\n- CogRouter — RL-based cognitive routing (ScienceWorld SOTA)\n- ITP-R — imagination-based routing to LLM world model\n- ARES — adaptive routing for efficient serving\n- Raposo et al. (2024). Mixture-of-Depths. *ICML*\n\n### Agent Frameworks\n- Yao et al. (2023). ReAct: Synergizing Reasoning and Acting in Language Models. *ICLR*\n- Shinn et al. (2023). Reflexion: Language Agents with Verbal Reinforcement Learning. *NeurIPS*\n\n### Methodology\n- Ross et al. (2011). A Reduction of Imitation Learning and Structured Prediction to No-Regret Online Learning. *AISTATS* (DAgger)\n\n### Environment\n- Wang et al. (2022). ScienceWorld: Is your Agent Smarter than a 5th Grader? *EMNLP*\n\n### Code Execution Routing\n- Gou et al. (2024). ReTool / ToRA — tool-integrated reasoning for math\n- Chen et al. (2023). AgentMath — code-augmented mathematical reasoning\n\n---\n\n## Provenance: Claims → Experiments\n\n| Claim | Source Experiment | Key Metric |\n|-------|------------------|------------|\n| Δ_full=+29.60, death fraction=90.41% | plan-012-full | delta_full, death_avoidance_fraction |\n| r=0.9698, p=8.12e-07 | plan-012-full | pearson_r, pearson_p |\n| Baseline scores (Table 1) | plan-003-baseline | metrics per condition |\n| Keyword heuristic failure | plan-011-rule-based | v1_match_rate, v2_match_rate |\n| Learned router internal_recall=51.5% | plan-004-ablation-b | per_class.internal.recall |\n| find-non-living-thing Δ=9.58 | plan-012-decomposition | key_tasks.find_non_living_thing |\n| Episode label distribution 86/9/150 | plan-012-full | label_dist |\n| Death rates: int 42.9%, det 16.3% | plan-012-full | death_rate_int, death_rate_det |\n| Per-step oracle 98% tie rate | plan-012-decomposition | (derived from label_dist) |\n",
    "structuredPatch": [
      {
        "oldStart": 55,
        "oldLines": 7,
        "newStart": 55,
        "newLines": 7,
        "lines": [
          "   - always-internal: -39.07, always-det: -9.47, oracle: -6.58, random: -22.38 [A: plan-003-baseline-245eps]",
          "   - Keyword heuristic: structural failure (v1 85.8% match → ≈always-det; v2 4.9% → ≈always-internal)",
          "   - Learned router (ablation-b): internal_recall=51.5%, first non-degenerate; classification head variants all degenerate",
          "-- **3.4 Analysis**: Death rate: internal 42.9% vs. deterministic 16.3%; alive-episode scores nearly equal across modalities",
          "+- **3.4 Analysis**: Death rate: internal 42.9% vs. deterministic 16.3%; alive-episode scores nearly equal across modalities [A: plan-012-full, 245eps/11tasks]",
          " ",
          " ### 4. Related Work (0.5 pages, integrated or separate)",
          " "
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  },
  "sourceToolAssistantUUID": "44a8625a-4c96-4d5f-9b6f-4213d97c229d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing",
  "sessionId": "fe1af098-4ed4-4fac-9d28-af54a02d46ce",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 51_

```json
{
  "type": "last-prompt",
  "leafUuid": "51171018-ec94-4f39-81bd-7e94bb0ce170",
  "sessionId": "fe1af098-4ed4-4fac-9d28-af54a02d46ce"
}
```

---

### Runtime record

_source line 52_

```json
{
  "type": "ai-title",
  "aiTitle": "Update paper_outline.md baseline numbers to 245-ep",
  "sessionId": "fe1af098-4ed4-4fac-9d28-af54a02d46ce"
}
```

---

### Assistant

_source line 53 · 2026-05-14T08:21:41.880Z_

Now update the Provenance table to reflect the new baseline source.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "51171018-ec94-4f39-81bd-7e94bb0ce170",
  "isSidechain": false,
  "requestId": "req_011Cb28tfx2zdzemVcMYQ38x",
  "type": "assistant",
  "uuid": "f286268e-04b2-4543-883b-e23620f2f01f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing",
  "sessionId": "fe1af098-4ed4-4fac-9d28-af54a02d46ce",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017GiokgNWEmaNY9oBa84gJo",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 293,
      "cache_read_input_tokens": 34841,
      "output_tokens": 206,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 293,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 206,
          "cache_read_input_tokens": 34841,
          "cache_creation_input_tokens": 293,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 293
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

_source line 54 · 2026-05-14T08:21:43.192Z_

<details open><summary>🔧 Tool call — Edit · `toolu_01FLk1sZ1pZQsoUWSH5Rnf8Z`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/_project/paper/paper_outline.md",
  "old_string": "| Baseline scores (Table 1) | plan-003-baseline | metrics per condition |",
  "new_string": "| Baseline scores (Table 1) | plan-003-baseline-245eps | metrics per condition |"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f286268e-04b2-4543-883b-e23620f2f01f",
  "isSidechain": false,
  "requestId": "req_011Cb28tfx2zdzemVcMYQ38x",
  "type": "assistant",
  "uuid": "60fce5a0-2d46-408f-9963-2410f27f183c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing",
  "sessionId": "fe1af098-4ed4-4fac-9d28-af54a02d46ce",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017GiokgNWEmaNY9oBa84gJo",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 293,
      "cache_read_input_tokens": 34841,
      "output_tokens": 206,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 293,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 206,
          "cache_read_input_tokens": 34841,
          "cache_creation_input_tokens": 293,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 293
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

_source line 55 · 2026-05-14T08:21:43.216Z_

<details><summary>↩ Tool result · `toolu_01FLk1sZ1pZQsoUWSH5Rnf8Z`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/_project/paper/paper_outline.md has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "60fce5a0-2d46-408f-9963-2410f27f183c",
  "isSidechain": false,
  "promptId": "de32f0f5-b4f7-4fe9-872c-8108c929635d",
  "type": "user",
  "uuid": "62c77709-054a-4006-8597-87ad2d9d93ea",
  "toolUseResult": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/_project/paper/paper_outline.md",
    "oldString": "| Baseline scores (Table 1) | plan-003-baseline | metrics per condition |",
    "newString": "| Baseline scores (Table 1) | plan-003-baseline-245eps | metrics per condition |",
    "originalFile": null,
    "structuredPatch": [
      {
        "oldStart": 149,
        "oldLines": 7,
        "newStart": 149,
        "newLines": 7,
        "lines": [
          " |-------|------------------|------------|",
          " | Δ_full=+29.60, death fraction=90.41% | plan-012-full | delta_full, death_avoidance_fraction |",
          " | r=0.9698, p=8.12e-07 | plan-012-full | pearson_r, pearson_p |",
          "-| Baseline scores (Table 1) | plan-003-baseline | metrics per condition |",
          "+| Baseline scores (Table 1) | plan-003-baseline-245eps | metrics per condition |",
          " | Keyword heuristic failure | plan-011-rule-based | v1_match_rate, v2_match_rate |",
          " | Learned router internal_recall=51.5% | plan-004-ablation-b | per_class.internal.recall |",
          " | find-non-living-thing Δ=9.58 | plan-012-decomposition | key_tasks.find_non_living_thing |"
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  },
  "sourceToolAssistantUUID": "60fce5a0-2d46-408f-9963-2410f27f183c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing",
  "sessionId": "fe1af098-4ed4-4fac-9d28-af54a02d46ce",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 56 · 2026-05-14T08:21:43.265Z_

```json
{
  "parentUuid": "62c77709-054a-4006-8597-87ad2d9d93ea",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "6a44d0ab-2001-4d63-821f-b04fa0e58b62",
  "timestamp": "2026-05-14T08:21:43.265Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing",
  "sessionId": "fe1af098-4ed4-4fac-9d28-af54a02d46ce",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 57 · 2026-05-14T08:21:45.602Z_

验证最终文件。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6a44d0ab-2001-4d63-821f-b04fa0e58b62",
  "isSidechain": false,
  "requestId": "req_011Cb28tyqZTLYZ9XUnZ3Pm8",
  "type": "assistant",
  "uuid": "d80d8f72-98a5-4117-9089-76f2ddd0848c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing",
  "sessionId": "fe1af098-4ed4-4fac-9d28-af54a02d46ce",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SL9rNTSXDRYNxyGreX2SdH",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 369,
      "cache_read_input_tokens": 35134,
      "output_tokens": 101,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 369,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 101,
          "cache_read_input_tokens": 35134,
          "cache_creation_input_tokens": 369,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 369
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

_source line 58 · 2026-05-14T08:21:45.983Z_

<details open><summary>🔧 Tool call — Read · `toolu_01MDoSs4oA2jvqd2tFJKgCjy`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/_project/paper/paper_outline.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d80d8f72-98a5-4117-9089-76f2ddd0848c",
  "isSidechain": false,
  "requestId": "req_011Cb28tyqZTLYZ9XUnZ3Pm8",
  "type": "assistant",
  "uuid": "4ba08c9f-5f9c-4d6e-98ef-c9982fa44d5f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing",
  "sessionId": "fe1af098-4ed4-4fac-9d28-af54a02d46ce",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SL9rNTSXDRYNxyGreX2SdH",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 369,
      "cache_read_input_tokens": 35134,
      "output_tokens": 101,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 369,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 101,
          "cache_read_input_tokens": 35134,
          "cache_creation_input_tokens": 369,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 369
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

_source line 59 · 2026-05-14T08:21:45.990Z_

<details><summary>↩ Tool result · `toolu_01MDoSs4oA2jvqd2tFJKgCjy`</summary>

```text
1	# EMNLP 2026 Short Paper Outline
2	
3	## Title Candidates
4	
5	1. **Death Avoidance Dominates Routing Signal: A Counterfactual Analysis of LLM Agent Tool Use in Interactive Environments**
6	2. **When Does Deterministic Computation Help LLM Agents? Episode-Level Counterfactual Analysis Reveals Death Avoidance Dominance**
7	3. **90% Death Avoidance: Decomposing the Routing Signal Between LLM Reasoning and Deterministic Simulation**
8	
9	Recommended: **Title 1** (clear claim + methodology in title; fits short paper convention of stating the finding)
10	
11	---
12	
13	## Abstract Skeleton (~150 words)
14	
15	Key points to cover:
16	
17	- **Problem**: LLM agents hallucinate state transitions in rule-governed environments, causing catastrophic failures (deaths). Routing between internal LLM reasoning and deterministic computation (simulators) can mitigate this, but what exactly does routing learn?
18	- **Methodological gap**: Per-step oracle labeling degenerates in sparse-reward settings (98% tie rate on ScienceWorld). We propose episode-level counterfactual analysis.
19	- **Core finding**: Death avoidance accounts for ~90% of routing signal (Δ_full=+29.60, Δ_no_death=+2.84, DAF=90.41%; Pearson r=0.97, p<1e-6 across 11 task types / 245 episodes) [A: plan-012-full, 245eps/11tasks]. Non-death performance is approximately equal between modalities.
20	- **Supporting finding**: Keyword heuristics structurally fail (match rates degenerate to ≈always-det or ≈always-internal); episode-level counterfactual labels can train a lightweight router (internal_recall=51.5%).
21	- **Implication**: The value of deterministic computation in interactive environments is concentrated in catastrophic failure prevention, not positive task guidance.
22	
23	---
24	
25	## Section Structure
26	
27	### 1. Introduction (0.8 pages)
28	
29	**Key points:**
30	- LLM agents on rule-governed environments (physics, chemistry) suffer catastrophic failures from hallucinated state transitions → motivate the routing question
31	- Existing work: tool-use learning (Toolformer, ART, Chameleon) learns *when* to invoke tools but doesn't analyze *what* routing learns; ITP-R routes to approximate world models but underperforms pure internal reasoning; ReTool/AgentMath use implicit routing entangled with backbone
32	- Per-step oracle labeling degenerates in sparse-reward environments (98% tie rate) → need episode-level analysis
33	- **Contributions** (bulleted):
34	  1. Episode-level counterfactual methodology that overcomes per-step oracle degeneracy
35	  2. Empirical finding: death avoidance accounts for ≥90% of routing signal on ScienceWorld (11 tasks, 245 episodes) [A: plan-012-full, 245eps/11tasks]
36	  3. Structural failure analysis of keyword heuristics; demonstration that counterfactual labels can train a lightweight diagnostic router
37	
38	### 2. Method (1.0 pages)
39	
40	**Key points:**
41	- **2.1 Problem Setup**: ScienceWorld environment; two computation modalities (internal LLM reasoning vs. deterministic simulation via environment forking); per-step routing decision
42	- **2.2 Episode-Level Counterfactual Labeling**: Why per-step oracle fails (98% tie rate in sparse rewards) → run complete episodes under pure-internal and pure-deterministic strategies → compare episode-level scores → label: det-preferred / internal-preferred / no-preference. Distribution: 86 det-pref / 9 int-pref / 150 no-pref (245 episodes) [A: plan-012-full, 245eps/11tasks]
43	- **2.3 Death Decomposition Framework**: Decompose Δ_full into death-avoidance component (Δ_death) and non-death component (Δ_nd). Death avoidance fraction = (Δ_full - Δ_nd) / Δ_full. Cross-task correlation: Pearson r between per-task death rate difference and Δ_full
44	
45	### 3. Experiments (1.5 pages)
46	
47	**Key points:**
48	- **3.1 Setup**: Qwen3-1.7B backbone; ScienceWorld 11 task types × 20-40 episodes; evaluation: always-internal, always-deterministic, oracle, random, keyword heuristic, learned router
49	- **3.2 Death Decomposition Results** (core result):
50	  - Δ_full=+29.60, Δ_nd=+2.84, death fraction=90.41% [A: plan-012-full, 245eps/11tasks]
51	  - 10/11 death-prone tasks: death-dominated gaps
52	  - 1 exception: find-non-living-thing (n=40, 0 deaths, Δ=+9.58 from non-death mechanisms) [A: plan-012-full, 245eps/11tasks]
53	  - Pearson r=0.9698 (p=8.12e-07) [A: plan-012-full, 245eps/11tasks]
54	- **3.3 Baseline Comparison**:
55	  - always-internal: -39.07, always-det: -9.47, oracle: -6.58, random: -22.38 [A: plan-003-baseline-245eps]
56	  - Keyword heuristic: structural failure (v1 85.8% match → ≈always-det; v2 4.9% → ≈always-internal)
57	  - Learned router (ablation-b): internal_recall=51.5%, first non-degenerate; classification head variants all degenerate
58	- **3.4 Analysis**: Death rate: internal 42.9% vs. deterministic 16.3%; alive-episode scores nearly equal across modalities [A: plan-012-full, 245eps/11tasks]
59	
60	### 4. Related Work (0.5 pages, integrated or separate)
61	
62	**Key points:**
63	- **Tool-use learning**: Toolformer (self-supervised API insertion), ART (LLM-as-router), Chameleon (LLM-as-planner), ToolkenGPT (token-level triggers). Differentiation: episode-level counterfactual labeling, safety-aware framing, explicit modular router
64	- **Adaptive computation / routing**: CogRouter (RL-based), ARES, Mixture-of-Depths. Our focus: empirical analysis of *what* routing learns, not a new routing architecture
65	- **World model routing**: ITP-R, Dyna-Think. Our deterministic computation is exact (simulator), not approximate (LLM world model)
66	- **Agent frameworks**: ReAct, Reflexion. Orthogonal — we analyze the routing decision within an agent loop
67	
68	### 5. Conclusion (0.3 pages)
69	
70	**Key points:**
71	- Summary: death avoidance ≥90% of routing signal; episode-level counterfactual analysis as diagnostic methodology
72	- **Limitations**: single benchmark (ScienceWorld), episode-level granularity (not step-level), DAgger distribution shift (train on pure strategies, deploy on mixed)
73	- **Future work**: step-level labeling with denser reward signals, extension to MATH/code interpretation domains, DAgger-style iterative relabeling
74	
75	---
76	
77	## Figure/Table Plan
78	
79	### Table 1: Baseline Comparison
80	| Method | Score | 90% CI | Success Rate | Death Rate | Sim Ratio |
81	|--------|-------|--------|-------------|------------|-----------|
82	| Always-Internal | -39.07 [A: plan-003-baseline-245eps] | TBD | TBD | TBD | 0.00 |
83	| Always-Deterministic | -9.47 [A: plan-003-baseline-245eps] | TBD | TBD | TBD | 1.00 |
84	| Oracle | -6.58 [A: plan-003-baseline-245eps] | TBD | TBD | TBD | 0.96 |
85	| Random | -22.38 [A: plan-003-baseline-245eps] | TBD | TBD | TBD | 0.50 |
86	| Keyword Heuristic (v1) | ≈ Always-Det | — | — | — | 0.86 |
87	| Keyword Heuristic (v2) | ≈ Always-Int | — | — | — | 0.05 |
88	| Learned Router (implicit) | TBD | — | — | — | TBD |
89	
90	*Source: plan-003-baseline-245eps, plan-011-rule-based*
91	
92	### Figure 1: Death Decomposition (core figure)
93	- **Type**: Grouped bar chart or stacked bar
94	- **X-axis**: 11 task types (sorted by death fraction)
95	- **Y-axis**: Score delta (deterministic − internal)
96	- **Bars**: Δ_full decomposed into Δ_death (death-avoidance component, dark) and Δ_nd (non-death component, light)
97	- **Highlight**: find-non-living-thing as sole exception (Δ_nd = Δ_full = 9.58, zero deaths)
98	- **Annotation**: Overall death fraction = 90.41%
99	
100	*Source: plan-012-full*
101	
102	### Figure 2: Cross-task Correlation (if space permits)
103	- **Type**: Scatter plot with regression line
104	- **X-axis**: Per-task death rate difference (internal − deterministic)
105	- **Y-axis**: Δ_full per task
106	- **Regression line**: r=0.9698, p=8.12e-07
107	- **11 points**, labeled by task type
108	- **Purpose**: Visually demonstrates near-perfect linear relationship
109	
110	*Source: plan-012-full, plan-012-decomposition*
111	
112	**Space strategy**: Figure 1 is mandatory. Figure 2 can be merged as an inset in Figure 1, or moved to appendix if space is tight. Table 1 is mandatory. Per-task breakdown table → appendix.
113	
114	---
115	
116	## Key References
117	
118	### Tool-Use Learning
119	- Schick et al. (2024). Toolformer: Language Models Can Teach Themselves to Use Tools. *NeurIPS*
120	- Paranjape et al. (2023). ART: Automatic Multi-step Reasoning and Tool-Use. *arXiv*
121	- Lu et al. (2024). Chameleon: Plug-and-Play Compositional Reasoning with Large Language Models. *NeurIPS*
122	- Hao et al. (2024). ToolkenGPT: Augmenting Frozen Language Models with Massive Tools via Tool Embeddings. *NeurIPS*
123	
124	### Agent Routing / Adaptive Computation
125	- CogRouter — RL-based cognitive routing (ScienceWorld SOTA)
126	- ITP-R — imagination-based routing to LLM world model
127	- ARES — adaptive routing for efficient serving
128	- Raposo et al. (2024). Mixture-of-Depths. *ICML*
129	
130	### Agent Frameworks
131	- Yao et al. (2023). ReAct: Synergizing Reasoning and Acting in Language Models. *ICLR*
132	- Shinn et al. (2023). Reflexion: Language Agents with Verbal Reinforcement Learning. *NeurIPS*
133	
134	### Methodology
135	- Ross et al. (2011). A Reduction of Imitation Learning and Structured Prediction to No-Regret Online Learning. *AISTATS* (DAgger)
136	
137	### Environment
138	- Wang et al. (2022). ScienceWorld: Is your Agent Smarter than a 5th Grader? *EMNLP*
139	
140	### Code Execution Routing
141	- Gou et al. (2024). ReTool / ToRA — tool-integrated reasoning for math
142	- Chen et al. (2023). AgentMath — code-augmented mathematical reasoning
143	
144	---
145	
146	## Provenance: Claims → Experiments
147	
148	| Claim | Source Experiment | Key Metric |
149	|-------|------------------|------------|
150	| Δ_full=+29.60, death fraction=90.41% | plan-012-full | delta_full, death_avoidance_fraction |
151	| r=0.9698, p=8.12e-07 | plan-012-full | pearson_r, pearson_p |
152	| Baseline scores (Table 1) | plan-003-baseline-245eps | metrics per condition |
153	| Keyword heuristic failure | plan-011-rule-based | v1_match_rate, v2_match_rate |
154	| Learned router internal_recall=51.5% | plan-004-ablation-b | per_class.internal.recall |
155	| find-non-living-thing Δ=9.58 | plan-012-decomposition | key_tasks.find_non_living_thing |
156	| Episode label distribution 86/9/150 | plan-012-full | label_dist |
157	| Death rates: int 42.9%, det 16.3% | plan-012-full | death_rate_int, death_rate_det |
158	| Per-step oracle 98% tie rate | plan-012-decomposition | (derived from label_dist) |
159	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4ba08c9f-5f9c-4d6e-98ef-c9982fa44d5f",
  "isSidechain": false,
  "promptId": "de32f0f5-b4f7-4fe9-872c-8108c929635d",
  "type": "user",
  "uuid": "4dbd0394-d44e-4c14-bd81-79562dbeef3c",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/_project/paper/paper_outline.md",
      "content": "# EMNLP 2026 Short Paper Outline\n\n## Title Candidates\n\n1. **Death Avoidance Dominates Routing Signal: A Counterfactual Analysis of LLM Agent Tool Use in Interactive Environments**\n2. **When Does Deterministic Computation Help LLM Agents? Episode-Level Counterfactual Analysis Reveals Death Avoidance Dominance**\n3. **90% Death Avoidance: Decomposing the Routing Signal Between LLM Reasoning and Deterministic Simulation**\n\nRecommended: **Title 1** (clear claim + methodology in title; fits short paper convention of stating the finding)\n\n---\n\n## Abstract Skeleton (~150 words)\n\nKey points to cover:\n\n- **Problem**: LLM agents hallucinate state transitions in rule-governed environments, causing catastrophic failures (deaths). Routing between internal LLM reasoning and deterministic computation (simulators) can mitigate this, but what exactly does routing learn?\n- **Methodological gap**: Per-step oracle labeling degenerates in sparse-reward settings (98% tie rate on ScienceWorld). We propose episode-level counterfactual analysis.\n- **Core finding**: Death avoidance accounts for ~90% of routing signal (Δ_full=+29.60, Δ_no_death=+2.84, DAF=90.41%; Pearson r=0.97, p<1e-6 across 11 task types / 245 episodes) [A: plan-012-full, 245eps/11tasks]. Non-death performance is approximately equal between modalities.\n- **Supporting finding**: Keyword heuristics structurally fail (match rates degenerate to ≈always-det or ≈always-internal); episode-level counterfactual labels can train a lightweight router (internal_recall=51.5%).\n- **Implication**: The value of deterministic computation in interactive environments is concentrated in catastrophic failure prevention, not positive task guidance.\n\n---\n\n## Section Structure\n\n### 1. Introduction (0.8 pages)\n\n**Key points:**\n- LLM agents on rule-governed environments (physics, chemistry) suffer catastrophic failures from hallucinated state transitions → motivate the routing question\n- Existing work: tool-use learning (Toolformer, ART, Chameleon) learns *when* to invoke tools but doesn't analyze *what* routing learns; ITP-R routes to approximate world models but underperforms pure internal reasoning; ReTool/AgentMath use implicit routing entangled with backbone\n- Per-step oracle labeling degenerates in sparse-reward environments (98% tie rate) → need episode-level analysis\n- **Contributions** (bulleted):\n  1. Episode-level counterfactual methodology that overcomes per-step oracle degeneracy\n  2. Empirical finding: death avoidance accounts for ≥90% of routing signal on ScienceWorld (11 tasks, 245 episodes) [A: plan-012-full, 245eps/11tasks]\n  3. Structural failure analysis of keyword heuristics; demonstration that counterfactual labels can train a lightweight diagnostic router\n\n### 2. Method (1.0 pages)\n\n**Key points:**\n- **2.1 Problem Setup**: ScienceWorld environment; two computation modalities (internal LLM reasoning vs. deterministic simulation via environment forking); per-step routing decision\n- **2.2 Episode-Level Counterfactual Labeling**: Why per-step oracle fails (98% tie rate in sparse rewards) → run complete episodes under pure-internal and pure-deterministic strategies → compare episode-level scores → label: det-preferred / internal-preferred / no-preference. Distribution: 86 det-pref / 9 int-pref / 150 no-pref (245 episodes) [A: plan-012-full, 245eps/11tasks]\n- **2.3 Death Decomposition Framework**: Decompose Δ_full into death-avoidance component (Δ_death) and non-death component (Δ_nd). Death avoidance fraction = (Δ_full - Δ_nd) / Δ_full. Cross-task correlation: Pearson r between per-task death rate difference and Δ_full\n\n### 3. Experiments (1.5 pages)\n\n**Key points:**\n- **3.1 Setup**: Qwen3-1.7B backbone; ScienceWorld 11 task types × 20-40 episodes; evaluation: always-internal, always-deterministic, oracle, random, keyword heuristic, learned router\n- **3.2 Death Decomposition Results** (core result):\n  - Δ_full=+29.60, Δ_nd=+2.84, death fraction=90.41% [A: plan-012-full, 245eps/11tasks]\n  - 10/11 death-prone tasks: death-dominated gaps\n  - 1 exception: find-non-living-thing (n=40, 0 deaths, Δ=+9.58 from non-death mechanisms) [A: plan-012-full, 245eps/11tasks]\n  - Pearson r=0.9698 (p=8.12e-07) [A: plan-012-full, 245eps/11tasks]\n- **3.3 Baseline Comparison**:\n  - always-internal: -39.07, always-det: -9.47, oracle: -6.58, random: -22.38 [A: plan-003-baseline-245eps]\n  - Keyword heuristic: structural failure (v1 85.8% match → ≈always-det; v2 4.9% → ≈always-internal)\n  - Learned router (ablation-b): internal_recall=51.5%, first non-degenerate; classification head variants all degenerate\n- **3.4 Analysis**: Death rate: internal 42.9% vs. deterministic 16.3%; alive-episode scores nearly equal across modalities [A: plan-012-full, 245eps/11tasks]\n\n### 4. Related Work (0.5 pages, integrated or separate)\n\n**Key points:**\n- **Tool-use learning**: Toolformer (self-supervised API insertion), ART (LLM-as-router), Chameleon (LLM-as-planner), ToolkenGPT (token-level triggers). Differentiation: episode-level counterfactual labeling, safety-aware framing, explicit modular router\n- **Adaptive computation / routing**: CogRouter (RL-based), ARES, Mixture-of-Depths. Our focus: empirical analysis of *what* routing learns, not a new routing architecture\n- **World model routing**: ITP-R, Dyna-Think. Our deterministic computation is exact (simulator), not approximate (LLM world model)\n- **Agent frameworks**: ReAct, Reflexion. Orthogonal — we analyze the routing decision within an agent loop\n\n### 5. Conclusion (0.3 pages)\n\n**Key points:**\n- Summary: death avoidance ≥90% of routing signal; episode-level counterfactual analysis as diagnostic methodology\n- **Limitations**: single benchmark (ScienceWorld), episode-level granularity (not step-level), DAgger distribution shift (train on pure strategies, deploy on mixed)\n- **Future work**: step-level labeling with denser reward signals, extension to MATH/code interpretation domains, DAgger-style iterative relabeling\n\n---\n\n## Figure/Table Plan\n\n### Table 1: Baseline Comparison\n| Method | Score | 90% CI | Success Rate | Death Rate | Sim Ratio |\n|--------|-------|--------|-------------|------------|-----------|\n| Always-Internal | -39.07 [A: plan-003-baseline-245eps] | TBD | TBD | TBD | 0.00 |\n| Always-Deterministic | -9.47 [A: plan-003-baseline-245eps] | TBD | TBD | TBD | 1.00 |\n| Oracle | -6.58 [A: plan-003-baseline-245eps] | TBD | TBD | TBD | 0.96 |\n| Random | -22.38 [A: plan-003-baseline-245eps] | TBD | TBD | TBD | 0.50 |\n| Keyword Heuristic (v1) | ≈ Always-Det | — | — | — | 0.86 |\n| Keyword Heuristic (v2) | ≈ Always-Int | — | — | — | 0.05 |\n| Learned Router (implicit) | TBD | — | — | — | TBD |\n\n*Source: plan-003-baseline-245eps, plan-011-rule-based*\n\n### Figure 1: Death Decomposition (core figure)\n- **Type**: Grouped bar chart or stacked bar\n- **X-axis**: 11 task types (sorted by death fraction)\n- **Y-axis**: Score delta (deterministic − internal)\n- **Bars**: Δ_full decomposed into Δ_death (death-avoidance component, dark) and Δ_nd (non-death component, light)\n- **Highlight**: find-non-living-thing as sole exception (Δ_nd = Δ_full = 9.58, zero deaths)\n- **Annotation**: Overall death fraction = 90.41%\n\n*Source: plan-012-full*\n\n### Figure 2: Cross-task Correlation (if space permits)\n- **Type**: Scatter plot with regression line\n- **X-axis**: Per-task death rate difference (internal − deterministic)\n- **Y-axis**: Δ_full per task\n- **Regression line**: r=0.9698, p=8.12e-07\n- **11 points**, labeled by task type\n- **Purpose**: Visually demonstrates near-perfect linear relationship\n\n*Source: plan-012-full, plan-012-decomposition*\n\n**Space strategy**: Figure 1 is mandatory. Figure 2 can be merged as an inset in Figure 1, or moved to appendix if space is tight. Table 1 is mandatory. Per-task breakdown table → appendix.\n\n---\n\n## Key References\n\n### Tool-Use Learning\n- Schick et al. (2024). Toolformer: Language Models Can Teach Themselves to Use Tools. *NeurIPS*\n- Paranjape et al. (2023). ART: Automatic Multi-step Reasoning and Tool-Use. *arXiv*\n- Lu et al. (2024). Chameleon: Plug-and-Play Compositional Reasoning with Large Language Models. *NeurIPS*\n- Hao et al. (2024). ToolkenGPT: Augmenting Frozen Language Models with Massive Tools via Tool Embeddings. *NeurIPS*\n\n### Agent Routing / Adaptive Computation\n- CogRouter — RL-based cognitive routing (ScienceWorld SOTA)\n- ITP-R — imagination-based routing to LLM world model\n- ARES — adaptive routing for efficient serving\n- Raposo et al. (2024). Mixture-of-Depths. *ICML*\n\n### Agent Frameworks\n- Yao et al. (2023). ReAct: Synergizing Reasoning and Acting in Language Models. *ICLR*\n- Shinn et al. (2023). Reflexion: Language Agents with Verbal Reinforcement Learning. *NeurIPS*\n\n### Methodology\n- Ross et al. (2011). A Reduction of Imitation Learning and Structured Prediction to No-Regret Online Learning. *AISTATS* (DAgger)\n\n### Environment\n- Wang et al. (2022). ScienceWorld: Is your Agent Smarter than a 5th Grader? *EMNLP*\n\n### Code Execution Routing\n- Gou et al. (2024). ReTool / ToRA — tool-integrated reasoning for math\n- Chen et al. (2023). AgentMath — code-augmented mathematical reasoning\n\n---\n\n## Provenance: Claims → Experiments\n\n| Claim | Source Experiment | Key Metric |\n|-------|------------------|------------|\n| Δ_full=+29.60, death fraction=90.41% | plan-012-full | delta_full, death_avoidance_fraction |\n| r=0.9698, p=8.12e-07 | plan-012-full | pearson_r, pearson_p |\n| Baseline scores (Table 1) | plan-003-baseline-245eps | metrics per condition |\n| Keyword heuristic failure | plan-011-rule-based | v1_match_rate, v2_match_rate |\n| Learned router internal_recall=51.5% | plan-004-ablation-b | per_class.internal.recall |\n| find-non-living-thing Δ=9.58 | plan-012-decomposition | key_tasks.find_non_living_thing |\n| Episode label distribution 86/9/150 | plan-012-full | label_dist |\n| Death rates: int 42.9%, det 16.3% | plan-012-full | death_rate_int, death_rate_det |\n| Per-step oracle 98% tie rate | plan-012-decomposition | (derived from label_dist) |\n",
      "numLines": 159,
      "startLine": 1,
      "totalLines": 159
    }
  },
  "sourceToolAssistantUUID": "4ba08c9f-5f9c-4d6e-98ef-c9982fa44d5f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing",
  "sessionId": "fe1af098-4ed4-4fac-9d28-af54a02d46ce",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 60 · 2026-05-14T08:21:57.313Z_

全部更新完成。变更摘要：

**Baseline 分数（4 处文本 + Table 1）**：
- always-internal: -37.16 → **-39.07**
- always-deterministic: -11.64 → **-9.47**
- oracle: -9.03 → **-6.58**
- random: -23.75 → **-22.38**
- Table 1 旧 CI/Success Rate/Death Rate 标为 TBD（无 245-ep 新值）
- Source 更新为 `plan-003-baseline-245eps`

**Provenance 标注（`[A: ...]`）添加到**：
- Abstract core finding（L19）
- Contributions 条目（L35）
- Label distribution（L42）
- Δ_full/Δ_nd/death fraction（L50）
- find-non-living-thing 加 n=40（L52）
- Pearson r/p（L53）
- Baseline 分数（L55）
- Death rate analysis（L58）
- Table 1 每行 Score 列
- Provenance 表 baseline 行（L152）

decomposition 数字（Δ_full=29.60, Δ_nd=2.84, DAF=90.41%, r=0.9698, p=8.12e-07, 11 tasks/245 episodes）已确认正确，无需改值，仅添加了标注。

文件已直接写入 `artifacts/_project/paper/paper_outline.md`。`save_project_file` 不支持该文件名，无法通过 MCP 保存。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4dbd0394-d44e-4c14-bd81-79562dbeef3c",
  "isSidechain": false,
  "requestId": "req_011Cb28uBoPqsYmkvEaQNr13",
  "type": "assistant",
  "uuid": "1418424c-7eba-4a96-bae7-6b480b64fec8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing",
  "sessionId": "fe1af098-4ed4-4fac-9d28-af54a02d46ce",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018SJ19r7h8yNPGxeT23wZVS",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3698,
      "cache_read_input_tokens": 35503,
      "output_tokens": 433,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3698,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 433,
          "cache_read_input_tokens": 35503,
          "cache_creation_input_tokens": 3698,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3698
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

_source line 61_

```json
{
  "type": "last-prompt",
  "leafUuid": "1418424c-7eba-4a96-bae7-6b480b64fec8",
  "sessionId": "fe1af098-4ed4-4fac-9d28-af54a02d46ce"
}
```

---

### Runtime record

_source line 62_

```json
{
  "type": "ai-title",
  "aiTitle": "Update paper_outline.md baseline numbers to 245-ep",
  "sessionId": "fe1af098-4ed4-4fac-9d28-af54a02d46ce"
}
```

---
