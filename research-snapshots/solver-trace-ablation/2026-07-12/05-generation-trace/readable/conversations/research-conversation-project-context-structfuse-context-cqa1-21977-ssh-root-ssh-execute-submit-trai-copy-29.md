# Research conversation: <project_context> # 项目: structfuse-context ## 运行环境 - 服务器名: cqa1-21977 - SSH 账户: root（调用 ssh_execute / submit_training_jo

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 50
- **Recorded user turns:** 1
- **Tool calls:** 11
- **Original source:** `logs/chats/exported-trajectories/account-2/f2480f86-9e1e-4510-980e-6abe201dd7a7.jsonl`
- **Structured JSON:** [`ae77435c2ce2377ed256.json`](../../sessions/ae/ae77435c2ce2377ed256.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-13T02:20:13.185Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-13T02:20:13.185Z",
  "sessionId": "f2480f86-9e1e-4510-980e-6abe201dd7a7",
  "content": "&lt;project_context>\n# 项目: structfuse-context\n\n## 运行环境\n- 服务器名: cqa1-21977\n- SSH 账户: root（调用 ssh_execute / submit_training_job 时传入 account=\"root\"）\n- SSH 连接命令: ssh connect.cqa1.seetacloud.com  # 必须用此命令，~/.ssh/config 自动应用密钥和跳板机，禁止用裸 IP\n- 项目代码根目录: /root/structfuse-context\n\n\n## 环境搭建\n连接服务器后先调 `detect_image` 检测是否为预置镜像。如果匹配，跳过基础环境搭建，只装项目特有依赖。已预装的包不要重复安装。\n\n## 输出风格\n回复简洁直接。只输出执行结果和必要信息，不要解释过程、不要客套、不要给未被要求的建议。\n&lt;/project_context>\n## 任务：合并文献文件 + 修正 Survey Takeaway\n\n项目：structfuse-context\n\n### 任务 A：合并 literature_map.yaml 和 literature_survey_related_work.md\n\n1. 先读取两个文件：\n   - `read_project_file(project=\"structfuse-context\", file=\"literature_map.yaml\", max_chars=0)`\n   - 读取 artifact 文件：`/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/_project/report/literature_survey_related_work.md`\n\n2. 找出 literature_map.yaml 中有但 survey 中缺失的论文：\n   - **Mondorf et al. (2510.06811)** — direct competitor，必须详细讨论\n   - **PIE (2604.16889)**\n   - **EAP-GP (2502.06852)**\n   - **GIM (2505.17630)**\n\n3. 将缺失论文补入 survey，按已有格式组织。特别是 **Mondorf et al.** 作为 direct competitor 必须详细讨论其局限：\n   - 仅限 gradient 族方法（不跨方法族）\n   - 使用 score averaging 而非 binary consensus\n   - CSS 与之对比的差异化要点\n\n4. 确保合并后 survey 成为单一权威源，所有 direct competitor 都有完整条目。\n\n### 任务 B：修正 Survey Takeaway #5\n\n当前 survey 中的 Takeaway #5 表述\"CSS 系统性评估 consensus circuits 的 distribution-shift robustness\"暗示已有这个能力。但 OOD 实验尚未进行（已在 D015 中推到 Phase 2）。\n\n修改为 **planned contribution** 表述，例如：\"CSS 计划系统性评估 consensus circuits 在分布偏移下的鲁棒性（Phase 2 planned）\" 或类似的 future-tense 表述。\n\n### 产出\n\n1. 更新后的 survey 文件（写回原路径）\n2. 列出所有新增/修改的条目\n3. 确认 Takeaway #5 的修改前后对比"
}
```

---

### Runtime record

_source line 2 · 2026-05-13T02:20:13.189Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-13T02:20:13.189Z",
  "sessionId": "f2480f86-9e1e-4510-980e-6abe201dd7a7"
}
```

---

## Round 1

48 recorded events

### User

_source line 3 · 2026-05-13T02:20:13.226Z_

&lt;project_context>
# 项目: structfuse-context

## 运行环境
- 服务器名: cqa1-21977
- SSH 账户: root（调用 ssh_execute / submit_training_job 时传入 account="root"）
- SSH 连接命令: ssh connect.cqa1.seetacloud.com  # 必须用此命令，~/.ssh/config 自动应用密钥和跳板机，禁止用裸 IP
- 项目代码根目录: /root/structfuse-context


## 环境搭建
连接服务器后先调 `detect_image` 检测是否为预置镜像。如果匹配，跳过基础环境搭建，只装项目特有依赖。已预装的包不要重复安装。

## 输出风格
回复简洁直接。只输出执行结果和必要信息，不要解释过程、不要客套、不要给未被要求的建议。
&lt;/project_context>
## 任务：合并文献文件 + 修正 Survey Takeaway

项目：structfuse-context

### 任务 A：合并 literature_map.yaml 和 literature_survey_related_work.md

1. 先读取两个文件：
   - `read_project_file(project="structfuse-context", file="literature_map.yaml", max_chars=0)`
   - 读取 artifact 文件：`/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/_project/report/literature_survey_related_work.md`

2. 找出 literature_map.yaml 中有但 survey 中缺失的论文：
   - **Mondorf et al. (2510.06811)** — direct competitor，必须详细讨论
   - **PIE (2604.16889)**
   - **EAP-GP (2502.06852)**
   - **GIM (2505.17630)**

3. 将缺失论文补入 survey，按已有格式组织。特别是 **Mondorf et al.** 作为 direct competitor 必须详细讨论其局限：
   - 仅限 gradient 族方法（不跨方法族）
   - 使用 score averaging 而非 binary consensus
   - CSS 与之对比的差异化要点

4. 确保合并后 survey 成为单一权威源，所有 direct competitor 都有完整条目。

### 任务 B：修正 Survey Takeaway #5

当前 survey 中的 Takeaway #5 表述"CSS 系统性评估 consensus circuits 的 distribution-shift robustness"暗示已有这个能力。但 OOD 实验尚未进行（已在 D015 中推到 Phase 2）。

修改为 **planned contribution** 表述，例如："CSS 计划系统性评估 consensus circuits 在分布偏移下的鲁棒性（Phase 2 planned）" 或类似的 future-tense 表述。

### 产出

1. 更新后的 survey 文件（写回原路径）
2. 列出所有新增/修改的条目
3. 确认 Takeaway #5 的修改前后对比

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "16c2e1a1-23bf-4ab8-bc32-4fa92e1b898b",
  "type": "user",
  "uuid": "e274ce9f-7d9c-4ac2-964c-d41f62edb06b",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context",
  "sessionId": "f2480f86-9e1e-4510-980e-6abe201dd7a7",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-13T02:20:13.226Z_

```json
{
  "parentUuid": "e274ce9f-7d9c-4ac2-964c-d41f62edb06b",
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
  "uuid": "8d01d3e4-101e-4162-a79c-f6d6c42c121f",
  "timestamp": "2026-05-13T02:20:13.226Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context",
  "sessionId": "f2480f86-9e1e-4510-980e-6abe201dd7a7",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-13T02:20:13.226Z_

```json
{
  "parentUuid": "8d01d3e4-101e-4162-a79c-f6d6c42c121f",
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
  "uuid": "7b89852f-e999-4b6c-a788-de897ee51cd7",
  "timestamp": "2026-05-13T02:20:13.226Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context",
  "sessionId": "f2480f86-9e1e-4510-980e-6abe201dd7a7",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 6 · 2026-05-13T02:20:13.226Z_

```json
{
  "parentUuid": "7b89852f-e999-4b6c-a788-de897ee51cd7",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "cecc93ec-5389-439c-a6d1-53c2ef5defa2",
  "timestamp": "2026-05-13T02:20:13.226Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context",
  "sessionId": "f2480f86-9e1e-4510-980e-6abe201dd7a7",
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
  "aiTitle": "Merge literature files and fix survey takeaway",
  "sessionId": "f2480f86-9e1e-4510-980e-6abe201dd7a7"
}
```

---

### Assistant

_source line 8 · 2026-05-13T02:20:18.823Z_

<details><summary>Logged reasoning block</summary>

```text
Let me start by reading both files to understand their current content.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cecc93ec-5389-439c-a6d1-53c2ef5defa2",
  "isSidechain": false,
  "requestId": "req_011CaymXCaD7ixjAyZKGbBzb",
  "type": "assistant",
  "uuid": "0a947ea4-2060-48fa-9ef8-c9f228477ff1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context",
  "sessionId": "f2480f86-9e1e-4510-980e-6abe201dd7a7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NPnMAHGXBDNk8p6RvC8Dwy",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11355,
      "cache_read_input_tokens": 11841,
      "output_tokens": 125,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11355,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 125,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11355,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11355
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

_source line 9 · 2026-05-13T02:20:18.836Z_

读取两个源文件。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0a947ea4-2060-48fa-9ef8-c9f228477ff1",
  "isSidechain": false,
  "requestId": "req_011CaymXCaD7ixjAyZKGbBzb",
  "type": "assistant",
  "uuid": "f184de19-b65c-4afb-99d3-6ab0a37ffbcc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context",
  "sessionId": "f2480f86-9e1e-4510-980e-6abe201dd7a7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NPnMAHGXBDNk8p6RvC8Dwy",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11355,
      "cache_read_input_tokens": 11841,
      "output_tokens": 125,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11355,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 125,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11355,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11355
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

_source line 10 · 2026-05-13T02:20:19.784Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01P6VZV26DyrJq7phYdAcV5J`</summary>

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
  "parentUuid": "f184de19-b65c-4afb-99d3-6ab0a37ffbcc",
  "isSidechain": false,
  "requestId": "req_011CaymXCaD7ixjAyZKGbBzb",
  "type": "assistant",
  "uuid": "ad88bfe0-2119-4cca-bbe1-8341f8c60073",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context",
  "sessionId": "f2480f86-9e1e-4510-980e-6abe201dd7a7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NPnMAHGXBDNk8p6RvC8Dwy",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11355,
      "cache_read_input_tokens": 11841,
      "output_tokens": 125,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11355,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 125,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11355,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11355
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

_source line 11 · 2026-05-13T02:20:19.790Z_

<details><summary>↩ Tool result · `toolu_01P6VZV26DyrJq7phYdAcV5J`</summary>

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
  "parentUuid": "ad88bfe0-2119-4cca-bbe1-8341f8c60073",
  "isSidechain": false,
  "promptId": "16c2e1a1-23bf-4ab8-bc32-4fa92e1b898b",
  "type": "user",
  "uuid": "5d6abfc0-93bc-482f-b74f-e11476ee4dae",
  "toolUseResult": {
    "matches": [
      "mcp__agent-ml-research__read_project_file"
    ],
    "query": "select:mcp__agent-ml-research__read_project_file",
    "total_deferred_tools": 22
  },
  "sourceToolAssistantUUID": "ad88bfe0-2119-4cca-bbe1-8341f8c60073",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context",
  "sessionId": "f2480f86-9e1e-4510-980e-6abe201dd7a7",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-13T02:20:22.515Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01FYUyDugM4Pd7cEMyVtD54f`</summary>

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
  "parentUuid": "5d6abfc0-93bc-482f-b74f-e11476ee4dae",
  "isSidechain": false,
  "requestId": "req_011CaymXgn6vSapwc6uXkrQk",
  "type": "assistant",
  "uuid": "222b0777-b232-4d6b-8c1e-f01ca094ac3b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context",
  "sessionId": "f2480f86-9e1e-4510-980e-6abe201dd7a7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ug9z9M5FfB33BqcqqDXmBC",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 472,
      "cache_read_input_tokens": 23196,
      "output_tokens": 187,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 472,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 187,
          "cache_read_input_tokens": 23196,
          "cache_creation_input_tokens": 472,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 472
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

_source line 13 · 2026-05-13T02:20:22.528Z_

<details><summary>↩ Tool result · `toolu_01FYUyDugM4Pd7cEMyVtD54f`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No literature_map.yaml found for 'structfuse-context'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "222b0777-b232-4d6b-8c1e-f01ca094ac3b",
  "isSidechain": false,
  "promptId": "16c2e1a1-23bf-4ab8-bc32-4fa92e1b898b",
  "type": "user",
  "uuid": "b78b5bc8-335e-44f0-8a67-a8c125ce05c9",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {}, \\\"error\\\": \\\"No literature_map.yaml found for 'structfuse-context'.\\\", \\\"metadata\\\": {}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {}, \"error\": \"No literature_map.yaml found for 'structfuse-context'.\", \"metadata\": {}}"
    }
  },
  "sourceToolAssistantUUID": "222b0777-b232-4d6b-8c1e-f01ca094ac3b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context",
  "sessionId": "f2480f86-9e1e-4510-980e-6abe201dd7a7",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-13T02:20:22.921Z_

<details open><summary>🔧 Tool call — Read · `toolu_01KHr4JhPr6GL7XjRfbrq79y`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/_project/report/literature_survey_related_work.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b78b5bc8-335e-44f0-8a67-a8c125ce05c9",
  "isSidechain": false,
  "requestId": "req_011CaymXgn6vSapwc6uXkrQk",
  "type": "assistant",
  "uuid": "2620c7b8-35a6-40c5-a9ac-ae1ad5e75e0e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context",
  "sessionId": "f2480f86-9e1e-4510-980e-6abe201dd7a7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ug9z9M5FfB33BqcqqDXmBC",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 472,
      "cache_read_input_tokens": 23196,
      "output_tokens": 187,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 472,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 187,
          "cache_read_input_tokens": 23196,
          "cache_creation_input_tokens": 472,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 472
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

_source line 15 · 2026-05-13T02:20:22.931Z_

<details><summary>↩ Tool result · `toolu_01KHr4JhPr6GL7XjRfbrq79y`</summary>

```text
1	# Related Work Literature Survey for CSS (Cross-method Structural Consensus)
2	
3	> Generated: 2026-05-13 | Target: EMNLP 2026 Main (ARR deadline 2026-05-25)
4	
5	---
6	
7	## Direction 1: Cross-method Consensus / Ensemble in Mechanistic Interpretability
8	
9	### 1.1 CIRCUS: Circuit Consensus under Uncertainty via Stability Ensembles
10	- **Authors:** Swapnil Parekh
11	- **Year:** 2026 (arXiv: 2603.00523)
12	- **Venue:** arXiv preprint (Feb 2026)
13	- **Core findings:** Reframes circuit discovery as an uncertainty-quantification problem. Constructs an ensemble of attribution graphs by pruning a *single* raw attribution run under multiple threshold configurations, assigns each edge a stability score (fraction of configs retaining it), and extracts a strict-consensus circuit (edges appearing in all views). On Gemma-2-2B and Llama-3.2-1B, strict consensus circuits are ~40× smaller than the union while retaining comparable explanatory power. Consensus-identified nodes beat matched non-consensus controls in causal relevance (p=0.0004).
14	- **Relation to CSS:** **直接竞争 (Primary competitor)**. CIRCUS varies pruning thresholds on a single attribution method to build consensus; CSS uses multiple independent discovery methods (EAP-IG, EP, ACDC/IFR). Key differentiators: (1) CSS captures cross-method agreement (different algorithms with different inductive biases), not just threshold robustness within one method; (2) CSS uses binary agreement rather than fractional stability scores; (3) CSS explicitly tests distribution-shift robustness. Must position CSS as complementary/stronger: method diversity > threshold diversity.
15	
16	### 1.2 Certified Circuits: Stability Guarantees for Mechanistic Circuits
17	- **Authors:** Alaa Anani, Tobias Lorenz, Bernt Schiele, et al.
18	- **Year:** 2026 (arXiv: 2602.22968)
19	- **Venue:** arXiv preprint (Feb 2026)
20	- **Core findings:** Wraps any black-box discovery algorithm with randomized data subsampling to certify that circuit component inclusion decisions are invariant to bounded edit-distance perturbations of the concept dataset. On ImageNet with ResNet-101, certified circuits achieved 96% accuracy vs 86% baseline using half the neurons. Addresses dataset-to-circuit instability.
21	- **Relation to CSS:** **互补 (Complementary)**. Certified Circuits focuses on data perturbation stability for vision models with formal guarantees; CSS focuses on method-agreement stability for language model circuits. Both address instability but from orthogonal angles. Could cite as motivation for why stability matters.
22	
23	### 1.3 Open Problems in Mechanistic Interpretability
24	- **Authors:** Lee Sharkey, Bilal Chughtai, Joshua Batson, et al. (29 authors, 18 organizations)
25	- **Year:** 2025 (arXiv: 2501.16496)
26	- **Venue:** arXiv preprint (Jan 2025), commissioned by Schmidt Sciences
27	- **Core findings:** Landmark collaborative paper establishing the field's consensus open problems. Highlights systematic non-identifiability: multiple circuits, features, and algorithm mappings can yield the same behavioral fidelity. Advocates reporting explanation ensembles and clarifying pragmatic vs. unicity criteria.
28	- **Relation to CSS:** **支持 (Supports CSS)**. Directly motivates multi-method consensus: if circuits are non-unique, reporting ensembles and agreement is essential. CSS operationalizes this recommendation.
29	
30	### 1.4 Circuit Tracing: Revealing Computational Graphs in Language Models
31	- **Authors:** Anthropic (Dario Amodei team)
32	- **Year:** 2025
33	- **Venue:** Anthropic Technical Report (March 2025)
34	- **Core findings:** Uses cross-layer transcoders to build attribution graphs—graphical representations of computational steps where nodes are features and edges are causal interactions. Open-sourced circuit tracing tools supporting Gemma-2-2B, Llama-3.1-1B, Qwen3-4B.
35	- **Relation to CSS:** **互补 (Complementary)**. Provides a different paradigm (feature-level circuits via transcoders vs. component-level circuits). CSS methods operate at edge/component level; circuit tracing works at feature level. Represents a parallel direction worth acknowledging.
36	
37	---
38	
39	## Direction 2: Circuit Faithfulness Evaluation
40	
41	### 2.1 Transformer Circuit Faithfulness Metrics Are Not Robust
42	- **Authors:** Joseph Miller, Bilal Chughtai, William Saunders
43	- **Year:** 2024
44	- **Venue:** COLM 2024
45	- **Core findings:** Faithfulness scores are highly sensitive to seemingly insignificant ablation methodology choices. Edge-level vs node-level ablation, resample vs mean ablation, and other methodological variations yield substantially different faithfulness percentages. Existing circuit faithfulness scores reflect researcher methodology as much as actual circuit quality.
46	- **Relation to CSS:** **强支持 (Strongly supports CSS)**. Core motivation for CSS: if single-method faithfulness metrics are unreliable, cross-method agreement provides a more robust signal. Directly supports the claim that binary consensus is more stable than score-dependent evaluation.
47	
48	### 2.2 Have Faith in Faithfulness: Going Beyond Circuit Overlap When Finding Model Mechanisms
49	- **Authors:** Michael Hanna, Sandro Pezzelle, Yonatan Belinkov
50	- **Year:** 2024
51	- **Venue:** COLM 2024 (also ICML 2024 MI Workshop Spotlight)
52	- **Core findings:** Introduces EAP-IG (EAP with integrated gradients) which finds more faithful circuits than EAP. Key finding: high node overlap ≠ high faithfulness. When comparing circuits, measuring overlap is no substitute for measuring faithfulness.
53	- **Relation to CSS:** **支持+基础方法 (Supports + foundational method)**. EAP-IG is one of CSS's three discovery methods. The finding that overlap ≠ faithfulness motivates CSS's use of faithfulness-based evaluation rather than simple circuit overlap metrics.
54	
55	### 2.3 MIB: A Mechanistic Interpretability Benchmark
56	- **Authors:** Yoav Goldberg, Yonatan Belinkov, et al.
57	- **Year:** 2025–2026 (arXiv: 2504.13151)
58	- **Venue:** ICML 2025 / ICLR 2026
59	- **Core findings:** Establishes two evaluation tracks—circuit localization and causal variable localization—across diverse tasks and models. Attribution and mask optimization methods perform best on circuit localization. Supervised DAS significantly outperforms unsupervised SAE features for causal variable localization.
60	- **Relation to CSS:** **互补 (Complementary)**. Provides standardized evaluation framework. CSS could adopt MIB tasks/metrics for evaluation; MIB results contextualize method performance differences.
61	
62	### 2.4 Functional Faithfulness in the Wild: Circuit Discovery with Differentiable Computation Graph Pruning
63	- **Authors:** Lei Yu, Jingcheng Niu, Zining Zhu, et al.
64	- **Year:** 2024 (arXiv: 2407.03779)
65	- **Venue:** arXiv preprint (July 2024)
66	- **Core findings:** Introduces DiscoGP—differentiable masking that prunes both weights and edges. Extracts sheaves preserving 93–100% model performance using only 1–7% of original weights/connections. Identifies that activation-patching-based circuits tend to be neither functionally faithful nor complete.
67	- **Relation to CSS:** **互补 (Complementary)**. Shows that weight+edge pruning yields more faithful circuits than edge-only approaches, further highlighting that methodology choices dramatically affect circuit quality—supporting CSS's cross-method approach.
68	
69	---
70	
71	## Direction 3: Binary vs Continuous Scoring in Circuit Discovery
72	
73	### 3.1 Finding Transformer Circuits with Edge Pruning
74	- **Authors:** Adithya Bhaskar, Alexander Wettig, Dan Friedman, et al.
75	- **Year:** 2024
76	- **Venue:** NeurIPS 2024
77	- **Core findings:** Frames circuit discovery as gradient-based optimization with binary masks over edges. EP is considerably more faithful on IOI and Greater-Than than both ACDC and EAP, especially at higher sparsities. Scales effectively to 100K examples where it is fastest and most faithful.
78	- **Relation to CSS:** **基础方法+支持 (Foundational method + supports)**. EP is one of CSS's discovery methods. Uses binary masks (0/1) for edge inclusion—directly relevant to CSS's binary consensus. Shows binary edge selection can be highly faithful.
79	
80	### 3.2 Attribution Patching Outperforms Automated Circuit Discovery
81	- **Authors:** Aaquib Syed, Can Rager, Arthur Conmy
82	- **Year:** 2024
83	- **Venue:** BlackboxNLP 2024 (NeurIPS Workshop)
84	- **Core findings:** A simple method based on attribution patching outperforms ACDC while requiring just two forward passes + one backward pass. However, EAP's first-order approximations show lower faithfulness to the full model than EP.
85	- **Relation to CSS:** **支持 (Supports)**. Documents that different methods (ACDC, EAP, EP) yield different circuits with different faithfulness levels—core motivation for cross-method consensus. Methods that are fast (EAP) and methods that are faithful (EP) produce systematically different results.
86	
87	### 3.3 Discovering Transformer Circuits via a Hybrid Attribution and Pruning Framework (HAP)
88	- **Authors:** Adithya Bhaskar, Alexander Wettig, et al.
89	- **Year:** 2025 (arXiv: 2510.03282)
90	- **Venue:** NeurIPS 2025
91	- **Core findings:** Two-stage pipeline: EAP filters unimportant edges (continuous scores → top-k), then EP refines with binary masks. HAP is ≥46% faster than EP while maintaining high faithfulness. Preserves cooperative circuit components (e.g., S-inhibition heads) that EAP alone prunes at high sparsity.
92	- **Relation to CSS:** **互补 (Complementary)**. Shows that combining methods sequentially (EAP→EP) improves over either alone. CSS takes a different combination approach: run methods independently, then take binary consensus. Complementary philosophies of method combination.
93	
94	### 3.4 Sparse Feature Circuits: Discovering and Editing Interpretable Causal Graphs in Language Models
95	- **Authors:** Samuel Marks, Can Rager, Eric Michaud, Yonatan Belinkov, David Bau, Aaron Mueller
96	- **Year:** 2025
97	- **Venue:** ICLR 2025 (Oral)
98	- **Core findings:** Uses SAEs to identify features, then discovers feature-level causal circuits. Small feature circuits (<100 nodes) explain a large proportion of model performance on subject-verb agreement. Introduces SHIFT for improving classifier generalization by ablating task-irrelevant features.
99	- **Relation to CSS:** **互补 (Complementary)**. Operates at feature level (SAE features) vs. CSS's component level (attention heads, MLPs). Shows that sparse/binary feature selection is powerful for circuit analysis. CSS could potentially extend to feature-level consensus in future work.
100	
101	### 3.5 Transcoders Find Interpretable LLM Feature Circuits
102	- **Authors:** Jacob Dunefsky, Philippe Morel, et al.
103	- **Year:** 2024
104	- **Venue:** NeurIPS 2024
105	- **Core findings:** Transcoders approximate dense MLP layers with wider, sparsely-activating layers. On par with SAEs in sparsity, faithfulness, and interpretability. Applied to reverse-engineer circuits in GPT-2-small including novel insights on the greater-than circuit.
106	- **Relation to CSS:** **互补 (Complementary)**. Offers alternative circuit representation (feature-level via transcoders). Relevant as a potential additional discovery method for CSS.
107	
108	---
109	
110	## Direction 4: Instability / Unreliability of Single-method Circuit Discovery
111	
112	### 4.1 Mechanistic Interpretability as Statistical Estimation: A Variance Analysis
113	- **Authors:** Maxime Méloux et al.
114	- **Year:** 2025–2026 (arXiv: 2510.00845, revised Feb 2026)
115	- **Venue:** arXiv preprint
116	- **Core findings:** Frames circuit discovery as a statistical estimation problem. Uncovers fundamental instability: single-input CMA scores exhibit high intrinsic variance—causal effects are volatile random variables, not fixed properties. Small perturbations in input data or hyperparameters yield vastly different circuits. Focuses on EAP and EAP-IG, systematically decomposing variance sources.
117	- **Relation to CSS:** **强支持 (Strongly supports CSS)**. Provides quantitative evidence that single-method circuits are unstable. Directly motivates CSS: if individual methods have high variance, cross-method consensus filters out method-specific noise.
118	
119	### 4.2 Circuit Stability Characterizes Language Model Generalization
120	- **Authors:** Alan Sun
121	- **Year:** 2025
122	- **Venue:** ACL 2025
123	- **Core findings:** Mathematically formalizes circuit stability—a model's ability to apply a consistent reasoning process (circuit) across inputs. Through three case studies, shows circuit stability predicts different aspects of generalization. Models that lack circuit stability fail to generalize.
124	- **Relation to CSS:** **支持 (Supports)**. Establishes that circuit stability is a valuable property. CSS targets a complementary notion of stability: consistency across methods rather than across inputs.
125	
126	### 4.3 Finding Highly Interpretable Prompt-Specific Circuits in Language Models
127	- **Authors:** Gabriel Franco, Lucas M. Tassis, Azalea Rohr, Mark Crovella
128	- **Year:** 2026 (arXiv: 2602.13483)
129	- **Venue:** arXiv preprint (Feb 2026)
130	- **Core findings:** Circuits are prompt-specific even within a fixed task. Applying ACC++ to IOI in GPT-2, Pythia, and Gemma 2: no single circuit for IOI in any model—different prompt templates induce systematically different mechanisms.
131	- **Relation to CSS:** **支持+挑战 (Supports + challenges)**. Supports CSS by showing single circuits are insufficient; challenges CSS to demonstrate that consensus circuits are more stable across prompts. CSS should test prompt-level robustness.
132	
133	### 4.4 Formal Mechanistic Interpretability: Automated Circuit Discovery with Provable Guarantees
134	- **Authors:** Itamar Hadad, Guy Katz, Shahaf Bassan
135	- **Year:** 2026
136	- **Venue:** ICLR 2026
137	- **Core findings:** Leverages neural network verification to yield circuits with provable guarantees: input domain robustness, robust patching, and minimality. Prior methods depend on heuristics without guarantees over continuous input domains. Applied to vision models.
138	- **Relation to CSS:** **互补 (Complementary)**. Takes a formal verification approach to robustness; CSS takes an empirical consensus approach. Both address circuit reliability but through fundamentally different mechanisms. Currently limited to vision models.
139	
140	### 4.5 Efficient Automated Circuit Discovery in Transformers using Contextual Decomposition (CD-T)
141	- **Authors:** Adelaide Hsu et al.
142	- **Year:** 2025
143	- **Venue:** ICLR 2025
144	- **Core findings:** Uses mathematical decomposition (no approximations) for circuit discovery. Reduces runtime from hours to seconds vs ACDC. Achieves 97% ROC AUC on IOI, Greater-Than, and Docstring tasks. Compatible with all transformer types, no training required.
145	- **Relation to CSS:** **互补 (Complementary)**. Provides yet another discovery method with different inductive biases than EAP-IG/EP/ACDC—could be a candidate additional method for CSS's ensemble.
146	
147	### 4.6 Towards Automated Circuit Discovery for Mechanistic Interpretability (ACDC)
148	- **Authors:** Arthur Conmy, Augustine N. Mavor-Parker, Aaquib Lynch, Stefan Heimersheim, Adrià Garriga-Alonso
149	- **Year:** 2023
150	- **Venue:** NeurIPS 2023
151	- **Core findings:** Foundational automated circuit discovery method using iterative activation patching. Effective but slow (runtime scales linearly with edges). Recovers IOI, Greater-Than, Docstring circuits. Establishes benchmark tasks for circuit discovery evaluation.
152	- **Relation to CSS:** **基础方法 (Foundational method)**. ACDC is one of CSS's three discovery methods for GPT-2 Small. Its different algorithmic approach (iterative patching vs. gradient-based) provides genuine method diversity in CSS's ensemble.
153	
154	---
155	
156	## Additional Relevant Work
157	
158	### RelP: Faithful and Efficient Circuit Discovery via Relevance Patching
159	- **Authors:** Farnoush Rezaei Jafari et al.
160	- **Year:** 2025
161	- **Venue:** NeurIPS 2025 MechInterp Workshop (Spotlight)
162	- **Core findings:** Replaces gradients in attribution patching with LRP propagation coefficients. For MLP outputs in GPT-2 Large, attribution patching achieves Pearson correlation 0.006 vs. RelP's 0.956 with activation patching ground truth. Faithfulness comparable to IG at lower cost.
163	- **Relation to CSS:** **互补 (Complementary)**. Another discovery method with different inductive bias. Documents dramatic differences between methods on the same components—supports CSS's premise.
164	
165	---
166	
167	## Key Takeaways for CSS Positioning
168	
169	### 1. CSS fills a specific gap in the literature
170	The field has established that (a) circuit discovery methods disagree (Syed et al. 2024; Méloux et al. 2025), (b) faithfulness metrics are unreliable (Miller et al. 2024), and (c) circuits are sensitive to analyst choices (CIRCUS, Certified Circuits). CSS is the first to exploit **cross-method binary consensus** as a robustness mechanism, using method diversity rather than threshold/data perturbation diversity.
171	
172	### 2. CIRCUS is the primary competitor — positioning is critical
173	CIRCUS (Parekh, 2026) is the closest work. Key differentiation:
174	- **CIRCUS:** varies pruning thresholds within one attribution method → threshold robustness
175	- **CSS:** uses multiple independent discovery methods → method robustness
176	- CSS argument: method diversity captures a broader space of inductive biases than threshold variation. A threshold ensemble still inherits the blind spots of its single underlying attribution method (e.g., EAP's first-order approximation errors). CSS's methods have structurally different failure modes (gradient-based vs. iterative patching vs. similarity-based).
177	
178	### 3. The "instability problem" is well-documented — CSS offers a practical solution
179	Multiple papers (Méloux et al., Franco et al., Miller et al.) document that circuits are unstable across data, prompts, and methodology. The Open Problems paper (Sharkey et al. 2025) explicitly calls for reporting ensembles. CSS directly operationalizes this recommendation with a concrete, lightweight algorithm.
180	
181	### 4. Binary scoring is underexplored relative to continuous scoring
182	Most methods produce continuous importance scores (EAP, EAP-IG, CD-T) and require threshold selection. Edge Pruning uses binary masks but within a single optimization. CSS's binary consensus (edge included/excluded per method → majority vote) is a distinct aggregation strategy that avoids score calibration issues across methods with incomparable scales.
183	
184	### 5. Distribution-shift robustness is a novel evaluation angle
185	No existing work systematically evaluates whether consensus circuits maintain faithfulness under distribution shift. CSS's off-diagonal evaluation (train on distribution A, test on distribution B) is a distinctive contribution.
186	
187	### 6. Recommended related work structure for the paper
188	1. **Circuit discovery methods** (ACDC, EAP-IG, EP, CD-T, HAP) — establish method landscape
189	2. **Faithfulness evaluation** (Miller et al. 2024, Hanna et al. 2024) — motivate robustness concerns
190	3. **Circuit instability** (Méloux et al. 2025, Franco et al. 2026, Sun 2025) — establish the problem CSS solves
191	4. **Consensus/stability approaches** (CIRCUS, Certified Circuits) — position CSS against alternatives
192	5. **Feature-level circuits** (Sparse Feature Circuits, Transcoders, Circuit Tracing) — acknowledge parallel direction, note CSS works at component level
193	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2620c7b8-35a6-40c5-a9ac-ae1ad5e75e0e",
  "isSidechain": false,
  "promptId": "16c2e1a1-23bf-4ab8-bc32-4fa92e1b898b",
  "type": "user",
  "uuid": "83510ccb-4b4e-4750-8350-66e3064b27ea",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/_project/report/literature_survey_related_work.md",
      "content": "# Related Work Literature Survey for CSS (Cross-method Structural Consensus)\n\n> Generated: 2026-05-13 | Target: EMNLP 2026 Main (ARR deadline 2026-05-25)\n\n---\n\n## Direction 1: Cross-method Consensus / Ensemble in Mechanistic Interpretability\n\n### 1.1 CIRCUS: Circuit Consensus under Uncertainty via Stability Ensembles\n- **Authors:** Swapnil Parekh\n- **Year:** 2026 (arXiv: 2603.00523)\n- **Venue:** arXiv preprint (Feb 2026)\n- **Core findings:** Reframes circuit discovery as an uncertainty-quantification problem. Constructs an ensemble of attribution graphs by pruning a *single* raw attribution run under multiple threshold configurations, assigns each edge a stability score (fraction of configs retaining it), and extracts a strict-consensus circuit (edges appearing in all views). On Gemma-2-2B and Llama-3.2-1B, strict consensus circuits are ~40× smaller than the union while retaining comparable explanatory power. Consensus-identified nodes beat matched non-consensus controls in causal relevance (p=0.0004).\n- **Relation to CSS:** **直接竞争 (Primary competitor)**. CIRCUS varies pruning thresholds on a single attribution method to build consensus; CSS uses multiple independent discovery methods (EAP-IG, EP, ACDC/IFR). Key differentiators: (1) CSS captures cross-method agreement (different algorithms with different inductive biases), not just threshold robustness within one method; (2) CSS uses binary agreement rather than fractional stability scores; (3) CSS explicitly tests distribution-shift robustness. Must position CSS as complementary/stronger: method diversity > threshold diversity.\n\n### 1.2 Certified Circuits: Stability Guarantees for Mechanistic Circuits\n- **Authors:** Alaa Anani, Tobias Lorenz, Bernt Schiele, et al.\n- **Year:** 2026 (arXiv: 2602.22968)\n- **Venue:** arXiv preprint (Feb 2026)\n- **Core findings:** Wraps any black-box discovery algorithm with randomized data subsampling to certify that circuit component inclusion decisions are invariant to bounded edit-distance perturbations of the concept dataset. On ImageNet with ResNet-101, certified circuits achieved 96% accuracy vs 86% baseline using half the neurons. Addresses dataset-to-circuit instability.\n- **Relation to CSS:** **互补 (Complementary)**. Certified Circuits focuses on data perturbation stability for vision models with formal guarantees; CSS focuses on method-agreement stability for language model circuits. Both address instability but from orthogonal angles. Could cite as motivation for why stability matters.\n\n### 1.3 Open Problems in Mechanistic Interpretability\n- **Authors:** Lee Sharkey, Bilal Chughtai, Joshua Batson, et al. (29 authors, 18 organizations)\n- **Year:** 2025 (arXiv: 2501.16496)\n- **Venue:** arXiv preprint (Jan 2025), commissioned by Schmidt Sciences\n- **Core findings:** Landmark collaborative paper establishing the field's consensus open problems. Highlights systematic non-identifiability: multiple circuits, features, and algorithm mappings can yield the same behavioral fidelity. Advocates reporting explanation ensembles and clarifying pragmatic vs. unicity criteria.\n- **Relation to CSS:** **支持 (Supports CSS)**. Directly motivates multi-method consensus: if circuits are non-unique, reporting ensembles and agreement is essential. CSS operationalizes this recommendation.\n\n### 1.4 Circuit Tracing: Revealing Computational Graphs in Language Models\n- **Authors:** Anthropic (Dario Amodei team)\n- **Year:** 2025\n- **Venue:** Anthropic Technical Report (March 2025)\n- **Core findings:** Uses cross-layer transcoders to build attribution graphs—graphical representations of computational steps where nodes are features and edges are causal interactions. Open-sourced circuit tracing tools supporting Gemma-2-2B, Llama-3.1-1B, Qwen3-4B.\n- **Relation to CSS:** **互补 (Complementary)**. Provides a different paradigm (feature-level circuits via transcoders vs. component-level circuits). CSS methods operate at edge/component level; circuit tracing works at feature level. Represents a parallel direction worth acknowledging.\n\n---\n\n## Direction 2: Circuit Faithfulness Evaluation\n\n### 2.1 Transformer Circuit Faithfulness Metrics Are Not Robust\n- **Authors:** Joseph Miller, Bilal Chughtai, William Saunders\n- **Year:** 2024\n- **Venue:** COLM 2024\n- **Core findings:** Faithfulness scores are highly sensitive to seemingly insignificant ablation methodology choices. Edge-level vs node-level ablation, resample vs mean ablation, and other methodological variations yield substantially different faithfulness percentages. Existing circuit faithfulness scores reflect researcher methodology as much as actual circuit quality.\n- **Relation to CSS:** **强支持 (Strongly supports CSS)**. Core motivation for CSS: if single-method faithfulness metrics are unreliable, cross-method agreement provides a more robust signal. Directly supports the claim that binary consensus is more stable than score-dependent evaluation.\n\n### 2.2 Have Faith in Faithfulness: Going Beyond Circuit Overlap When Finding Model Mechanisms\n- **Authors:** Michael Hanna, Sandro Pezzelle, Yonatan Belinkov\n- **Year:** 2024\n- **Venue:** COLM 2024 (also ICML 2024 MI Workshop Spotlight)\n- **Core findings:** Introduces EAP-IG (EAP with integrated gradients) which finds more faithful circuits than EAP. Key finding: high node overlap ≠ high faithfulness. When comparing circuits, measuring overlap is no substitute for measuring faithfulness.\n- **Relation to CSS:** **支持+基础方法 (Supports + foundational method)**. EAP-IG is one of CSS's three discovery methods. The finding that overlap ≠ faithfulness motivates CSS's use of faithfulness-based evaluation rather than simple circuit overlap metrics.\n\n### 2.3 MIB: A Mechanistic Interpretability Benchmark\n- **Authors:** Yoav Goldberg, Yonatan Belinkov, et al.\n- **Year:** 2025–2026 (arXiv: 2504.13151)\n- **Venue:** ICML 2025 / ICLR 2026\n- **Core findings:** Establishes two evaluation tracks—circuit localization and causal variable localization—across diverse tasks and models. Attribution and mask optimization methods perform best on circuit localization. Supervised DAS significantly outperforms unsupervised SAE features for causal variable localization.\n- **Relation to CSS:** **互补 (Complementary)**. Provides standardized evaluation framework. CSS could adopt MIB tasks/metrics for evaluation; MIB results contextualize method performance differences.\n\n### 2.4 Functional Faithfulness in the Wild: Circuit Discovery with Differentiable Computation Graph Pruning\n- **Authors:** Lei Yu, Jingcheng Niu, Zining Zhu, et al.\n- **Year:** 2024 (arXiv: 2407.03779)\n- **Venue:** arXiv preprint (July 2024)\n- **Core findings:** Introduces DiscoGP—differentiable masking that prunes both weights and edges. Extracts sheaves preserving 93–100% model performance using only 1–7% of original weights/connections. Identifies that activation-patching-based circuits tend to be neither functionally faithful nor complete.\n- **Relation to CSS:** **互补 (Complementary)**. Shows that weight+edge pruning yields more faithful circuits than edge-only approaches, further highlighting that methodology choices dramatically affect circuit quality—supporting CSS's cross-method approach.\n\n---\n\n## Direction 3: Binary vs Continuous Scoring in Circuit Discovery\n\n### 3.1 Finding Transformer Circuits with Edge Pruning\n- **Authors:** Adithya Bhaskar, Alexander Wettig, Dan Friedman, et al.\n- **Year:** 2024\n- **Venue:** NeurIPS 2024\n- **Core findings:** Frames circuit discovery as gradient-based optimization with binary masks over edges. EP is considerably more faithful on IOI and Greater-Than than both ACDC and EAP, especially at higher sparsities. Scales effectively to 100K examples where it is fastest and most faithful.\n- **Relation to CSS:** **基础方法+支持 (Foundational method + supports)**. EP is one of CSS's discovery methods. Uses binary masks (0/1) for edge inclusion—directly relevant to CSS's binary consensus. Shows binary edge selection can be highly faithful.\n\n### 3.2 Attribution Patching Outperforms Automated Circuit Discovery\n- **Authors:** Aaquib Syed, Can Rager, Arthur Conmy\n- **Year:** 2024\n- **Venue:** BlackboxNLP 2024 (NeurIPS Workshop)\n- **Core findings:** A simple method based on attribution patching outperforms ACDC while requiring just two forward passes + one backward pass. However, EAP's first-order approximations show lower faithfulness to the full model than EP.\n- **Relation to CSS:** **支持 (Supports)**. Documents that different methods (ACDC, EAP, EP) yield different circuits with different faithfulness levels—core motivation for cross-method consensus. Methods that are fast (EAP) and methods that are faithful (EP) produce systematically different results.\n\n### 3.3 Discovering Transformer Circuits via a Hybrid Attribution and Pruning Framework (HAP)\n- **Authors:** Adithya Bhaskar, Alexander Wettig, et al.\n- **Year:** 2025 (arXiv: 2510.03282)\n- **Venue:** NeurIPS 2025\n- **Core findings:** Two-stage pipeline: EAP filters unimportant edges (continuous scores → top-k), then EP refines with binary masks. HAP is ≥46% faster than EP while maintaining high faithfulness. Preserves cooperative circuit components (e.g., S-inhibition heads) that EAP alone prunes at high sparsity.\n- **Relation to CSS:** **互补 (Complementary)**. Shows that combining methods sequentially (EAP→EP) improves over either alone. CSS takes a different combination approach: run methods independently, then take binary consensus. Complementary philosophies of method combination.\n\n### 3.4 Sparse Feature Circuits: Discovering and Editing Interpretable Causal Graphs in Language Models\n- **Authors:** Samuel Marks, Can Rager, Eric Michaud, Yonatan Belinkov, David Bau, Aaron Mueller\n- **Year:** 2025\n- **Venue:** ICLR 2025 (Oral)\n- **Core findings:** Uses SAEs to identify features, then discovers feature-level causal circuits. Small feature circuits (<100 nodes) explain a large proportion of model performance on subject-verb agreement. Introduces SHIFT for improving classifier generalization by ablating task-irrelevant features.\n- **Relation to CSS:** **互补 (Complementary)**. Operates at feature level (SAE features) vs. CSS's component level (attention heads, MLPs). Shows that sparse/binary feature selection is powerful for circuit analysis. CSS could potentially extend to feature-level consensus in future work.\n\n### 3.5 Transcoders Find Interpretable LLM Feature Circuits\n- **Authors:** Jacob Dunefsky, Philippe Morel, et al.\n- **Year:** 2024\n- **Venue:** NeurIPS 2024\n- **Core findings:** Transcoders approximate dense MLP layers with wider, sparsely-activating layers. On par with SAEs in sparsity, faithfulness, and interpretability. Applied to reverse-engineer circuits in GPT-2-small including novel insights on the greater-than circuit.\n- **Relation to CSS:** **互补 (Complementary)**. Offers alternative circuit representation (feature-level via transcoders). Relevant as a potential additional discovery method for CSS.\n\n---\n\n## Direction 4: Instability / Unreliability of Single-method Circuit Discovery\n\n### 4.1 Mechanistic Interpretability as Statistical Estimation: A Variance Analysis\n- **Authors:** Maxime Méloux et al.\n- **Year:** 2025–2026 (arXiv: 2510.00845, revised Feb 2026)\n- **Venue:** arXiv preprint\n- **Core findings:** Frames circuit discovery as a statistical estimation problem. Uncovers fundamental instability: single-input CMA scores exhibit high intrinsic variance—causal effects are volatile random variables, not fixed properties. Small perturbations in input data or hyperparameters yield vastly different circuits. Focuses on EAP and EAP-IG, systematically decomposing variance sources.\n- **Relation to CSS:** **强支持 (Strongly supports CSS)**. Provides quantitative evidence that single-method circuits are unstable. Directly motivates CSS: if individual methods have high variance, cross-method consensus filters out method-specific noise.\n\n### 4.2 Circuit Stability Characterizes Language Model Generalization\n- **Authors:** Alan Sun\n- **Year:** 2025\n- **Venue:** ACL 2025\n- **Core findings:** Mathematically formalizes circuit stability—a model's ability to apply a consistent reasoning process (circuit) across inputs. Through three case studies, shows circuit stability predicts different aspects of generalization. Models that lack circuit stability fail to generalize.\n- **Relation to CSS:** **支持 (Supports)**. Establishes that circuit stability is a valuable property. CSS targets a complementary notion of stability: consistency across methods rather than across inputs.\n\n### 4.3 Finding Highly Interpretable Prompt-Specific Circuits in Language Models\n- **Authors:** Gabriel Franco, Lucas M. Tassis, Azalea Rohr, Mark Crovella\n- **Year:** 2026 (arXiv: 2602.13483)\n- **Venue:** arXiv preprint (Feb 2026)\n- **Core findings:** Circuits are prompt-specific even within a fixed task. Applying ACC++ to IOI in GPT-2, Pythia, and Gemma 2: no single circuit for IOI in any model—different prompt templates induce systematically different mechanisms.\n- **Relation to CSS:** **支持+挑战 (Supports + challenges)**. Supports CSS by showing single circuits are insufficient; challenges CSS to demonstrate that consensus circuits are more stable across prompts. CSS should test prompt-level robustness.\n\n### 4.4 Formal Mechanistic Interpretability: Automated Circuit Discovery with Provable Guarantees\n- **Authors:** Itamar Hadad, Guy Katz, Shahaf Bassan\n- **Year:** 2026\n- **Venue:** ICLR 2026\n- **Core findings:** Leverages neural network verification to yield circuits with provable guarantees: input domain robustness, robust patching, and minimality. Prior methods depend on heuristics without guarantees over continuous input domains. Applied to vision models.\n- **Relation to CSS:** **互补 (Complementary)**. Takes a formal verification approach to robustness; CSS takes an empirical consensus approach. Both address circuit reliability but through fundamentally different mechanisms. Currently limited to vision models.\n\n### 4.5 Efficient Automated Circuit Discovery in Transformers using Contextual Decomposition (CD-T)\n- **Authors:** Adelaide Hsu et al.\n- **Year:** 2025\n- **Venue:** ICLR 2025\n- **Core findings:** Uses mathematical decomposition (no approximations) for circuit discovery. Reduces runtime from hours to seconds vs ACDC. Achieves 97% ROC AUC on IOI, Greater-Than, and Docstring tasks. Compatible with all transformer types, no training required.\n- **Relation to CSS:** **互补 (Complementary)**. Provides yet another discovery method with different inductive biases than EAP-IG/EP/ACDC—could be a candidate additional method for CSS's ensemble.\n\n### 4.6 Towards Automated Circuit Discovery for Mechanistic Interpretability (ACDC)\n- **Authors:** Arthur Conmy, Augustine N. Mavor-Parker, Aaquib Lynch, Stefan Heimersheim, Adrià Garriga-Alonso\n- **Year:** 2023\n- **Venue:** NeurIPS 2023\n- **Core findings:** Foundational automated circuit discovery method using iterative activation patching. Effective but slow (runtime scales linearly with edges). Recovers IOI, Greater-Than, Docstring circuits. Establishes benchmark tasks for circuit discovery evaluation.\n- **Relation to CSS:** **基础方法 (Foundational method)**. ACDC is one of CSS's three discovery methods for GPT-2 Small. Its different algorithmic approach (iterative patching vs. gradient-based) provides genuine method diversity in CSS's ensemble.\n\n---\n\n## Additional Relevant Work\n\n### RelP: Faithful and Efficient Circuit Discovery via Relevance Patching\n- **Authors:** Farnoush Rezaei Jafari et al.\n- **Year:** 2025\n- **Venue:** NeurIPS 2025 MechInterp Workshop (Spotlight)\n- **Core findings:** Replaces gradients in attribution patching with LRP propagation coefficients. For MLP outputs in GPT-2 Large, attribution patching achieves Pearson correlation 0.006 vs. RelP's 0.956 with activation patching ground truth. Faithfulness comparable to IG at lower cost.\n- **Relation to CSS:** **互补 (Complementary)**. Another discovery method with different inductive bias. Documents dramatic differences between methods on the same components—supports CSS's premise.\n\n---\n\n## Key Takeaways for CSS Positioning\n\n### 1. CSS fills a specific gap in the literature\nThe field has established that (a) circuit discovery methods disagree (Syed et al. 2024; Méloux et al. 2025), (b) faithfulness metrics are unreliable (Miller et al. 2024), and (c) circuits are sensitive to analyst choices (CIRCUS, Certified Circuits). CSS is the first to exploit **cross-method binary consensus** as a robustness mechanism, using method diversity rather than threshold/data perturbation diversity.\n\n### 2. CIRCUS is the primary competitor — positioning is critical\nCIRCUS (Parekh, 2026) is the closest work. Key differentiation:\n- **CIRCUS:** varies pruning thresholds within one attribution method → threshold robustness\n- **CSS:** uses multiple independent discovery methods → method robustness\n- CSS argument: method diversity captures a broader space of inductive biases than threshold variation. A threshold ensemble still inherits the blind spots of its single underlying attribution method (e.g., EAP's first-order approximation errors). CSS's methods have structurally different failure modes (gradient-based vs. iterative patching vs. similarity-based).\n\n### 3. The \"instability problem\" is well-documented — CSS offers a practical solution\nMultiple papers (Méloux et al., Franco et al., Miller et al.) document that circuits are unstable across data, prompts, and methodology. The Open Problems paper (Sharkey et al. 2025) explicitly calls for reporting ensembles. CSS directly operationalizes this recommendation with a concrete, lightweight algorithm.\n\n### 4. Binary scoring is underexplored relative to continuous scoring\nMost methods produce continuous importance scores (EAP, EAP-IG, CD-T) and require threshold selection. Edge Pruning uses binary masks but within a single optimization. CSS's binary consensus (edge included/excluded per method → majority vote) is a distinct aggregation strategy that avoids score calibration issues across methods with incomparable scales.\n\n### 5. Distribution-shift robustness is a novel evaluation angle\nNo existing work systematically evaluates whether consensus circuits maintain faithfulness under distribution shift. CSS's off-diagonal evaluation (train on distribution A, test on distribution B) is a distinctive contribution.\n\n### 6. Recommended related work structure for the paper\n1. **Circuit discovery methods** (ACDC, EAP-IG, EP, CD-T, HAP) — establish method landscape\n2. **Faithfulness evaluation** (Miller et al. 2024, Hanna et al. 2024) — motivate robustness concerns\n3. **Circuit instability** (Méloux et al. 2025, Franco et al. 2026, Sun 2025) — establish the problem CSS solves\n4. **Consensus/stability approaches** (CIRCUS, Certified Circuits) — position CSS against alternatives\n5. **Feature-level circuits** (Sparse Feature Circuits, Transcoders, Circuit Tracing) — acknowledge parallel direction, note CSS works at component level\n",
      "numLines": 193,
      "startLine": 1,
      "totalLines": 193
    }
  },
  "sourceToolAssistantUUID": "2620c7b8-35a6-40c5-a9ac-ae1ad5e75e0e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context",
  "sessionId": "f2480f86-9e1e-4510-980e-6abe201dd7a7",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 16_

```json
{
  "type": "last-prompt",
  "leafUuid": "83510ccb-4b4e-4750-8350-66e3064b27ea",
  "sessionId": "f2480f86-9e1e-4510-980e-6abe201dd7a7"
}
```

---

### Runtime record

_source line 17_

```json
{
  "type": "ai-title",
  "aiTitle": "Merge literature files and fix survey takeaway",
  "sessionId": "f2480f86-9e1e-4510-980e-6abe201dd7a7"
}
```

---

### Assistant

_source line 18 · 2026-05-13T02:20:26.680Z_

<details><summary>Logged reasoning block</summary>

```text
The literature_map.yaml doesn't exist as a project file. Let me search for it in the artifacts or other locations.

I need to find literature_map.yaml. Let me search for it.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "83510ccb-4b4e-4750-8350-66e3064b27ea",
  "isSidechain": false,
  "requestId": "req_011CaymXvJSt1BNwN92txAGV",
  "type": "assistant",
  "uuid": "900f5c8c-f468-4bad-b418-122b58313007",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context",
  "sessionId": "f2480f86-9e1e-4510-980e-6abe201dd7a7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UuELbxLtdTd2JVaxJiDqc4",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5749,
      "cache_read_input_tokens": 23668,
      "output_tokens": 184,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5749,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 184,
          "cache_read_input_tokens": 23668,
          "cache_creation_input_tokens": 5749,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5749
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

_source line 19 · 2026-05-13T02:20:27.823Z_

literature_map.yaml 未在项目文件中找到，搜索其他位置。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "900f5c8c-f468-4bad-b418-122b58313007",
  "isSidechain": false,
  "requestId": "req_011CaymXvJSt1BNwN92txAGV",
  "type": "assistant",
  "uuid": "e376ff54-151b-4b56-a99e-9a80490e4372",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context",
  "sessionId": "f2480f86-9e1e-4510-980e-6abe201dd7a7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UuELbxLtdTd2JVaxJiDqc4",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5749,
      "cache_read_input_tokens": 23668,
      "output_tokens": 184,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5749,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 184,
          "cache_read_input_tokens": 23668,
          "cache_creation_input_tokens": 5749,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5749
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

_source line 20 · 2026-05-13T02:20:29.249Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01Tt8snDwU6dZ1S8TC5XjXva`</summary>

```json
{
  "pattern": "**/literature_map.yaml",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e376ff54-151b-4b56-a99e-9a80490e4372",
  "isSidechain": false,
  "requestId": "req_011CaymXvJSt1BNwN92txAGV",
  "type": "assistant",
  "uuid": "5ba8efde-4e26-4ed9-aa8a-538f833592b4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context",
  "sessionId": "f2480f86-9e1e-4510-980e-6abe201dd7a7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UuELbxLtdTd2JVaxJiDqc4",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5749,
      "cache_read_input_tokens": 23668,
      "output_tokens": 184,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5749,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 184,
          "cache_read_input_tokens": 23668,
          "cache_creation_input_tokens": 5749,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5749
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

_source line 21 · 2026-05-13T02:20:29.269Z_

<details><summary>↩ Tool result · `toolu_01Tt8snDwU6dZ1S8TC5XjXva`</summary>

```text
artifacts/literature_map.yaml
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5ba8efde-4e26-4ed9-aa8a-538f833592b4",
  "isSidechain": false,
  "promptId": "16c2e1a1-23bf-4ab8-bc32-4fa92e1b898b",
  "type": "user",
  "uuid": "fbb171e1-ef2f-46d4-997d-1b7f09a1d9bb",
  "toolUseResult": {
    "filenames": [
      "artifacts/literature_map.yaml"
    ],
    "durationMs": 15,
    "numFiles": 1,
    "truncated": false
  },
  "sourceToolAssistantUUID": "5ba8efde-4e26-4ed9-aa8a-538f833592b4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context",
  "sessionId": "f2480f86-9e1e-4510-980e-6abe201dd7a7",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-13T02:20:32.061Z_

<details open><summary>🔧 Tool call — Read · `toolu_0134v9DMV5djaBWgKfKUeSi7`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/literature_map.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fbb171e1-ef2f-46d4-997d-1b7f09a1d9bb",
  "isSidechain": false,
  "requestId": "req_011CaymYPFBbDsjVhKueLRyy",
  "type": "assistant",
  "uuid": "601f1df8-be08-4c47-8f0a-4f4f8e76dba3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context",
  "sessionId": "f2480f86-9e1e-4510-980e-6abe201dd7a7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NQ7smwJDWt4WDv2wiiaQ6o",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 203,
      "cache_read_input_tokens": 29417,
      "output_tokens": 87,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 203,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 87,
          "cache_read_input_tokens": 29417,
          "cache_creation_input_tokens": 203,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 203
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

_source line 23 · 2026-05-13T02:20:32.069Z_

<details><summary>↩ Tool result · `toolu_0134v9DMV5djaBWgKfKUeSi7`</summary>

```text
1	# Literature Map — structfuse-context (cross-method circuit consensus)
2	# Last updated: 2026-05-12
3	
4	- arxiv_id: "2603.00523"
5	  title: "CIRCUS: Circuit Consensus under Uncertainty via Stability Ensembles"
6	  authors: "Unknown (arXiv 2603.00523v2)"
7	  year: 2026
8	  category: "direct-competitor"
9	  role: "Primary competitor — intra-method stability scoring"
10	  summary: >
11	    Constructs ensemble of attribution graphs by pruning a single raw attribution
12	    run under multiple threshold configurations. Assigns per-edge stability score
13	    (fraction of configs retaining it). Strict-consensus circuit = edges in all views.
14	    ~40x smaller than union on Gemma-2-2B/Llama-3.2-1B while retaining explanatory power.
15	    Consensus nodes beat non-consensus controls in activation patching (p=0.0004).
16	  relevance_to_css: >
17	    CLOSEST competitor but fundamentally intra-method: varies thresholds within ONE
18	    attribution algorithm. Does NOT combine across algorithm families (gradient vs mask
19	    vs causal). CSS's cross-method consensus remains a distinct and unclaimed novelty.
20	    v2 update (2026-03-20) is same paper, no separate follow-up found.
21	  discovered_date: "2026-05-12"
22	
23	- arxiv_id: "2510.06811"
24	  title: "BlackboxNLP-2025 MIB Shared Task: Exploring Ensemble Strategies for Circuit Localization Methods"
25	  authors: "Mondorf, Wang et al."
26	  year: 2025
27	  category: "direct-competitor"
28	  role: "Limited cross-method ensembling (EAP-IG + Edge Pruning)"
29	  summary: >
30	    Explores parallel ensembling (averaging/min/max of attribution scores across methods)
31	    and sequential ensembling (EAP-IG warm-start then Edge Pruning refinement).
32	    Parallel ensemble over all variants achieves best CMD=0.03, CPR=1.83 on MIB leaderboard.
33	    Workshop short paper at BlackboxNLP 2025.
34	  relevance_to_css: >
35	    Closest to cross-method but limited: only combines EAP-IG and Edge Pruning, both
36	    gradient-based edge attribution methods from the same algorithmic family.
37	    No causal/mask-based methods included. Simple score aggregation (avg/min/max),
38	    no principled consensus framework. CSS goes beyond by spanning algorithm families
39	    and providing binary consensus with confidence scoring.
40	  discovered_date: "2026-05-12"
41	
42	- arxiv_id: "2602.22968"
43	  title: "Certified Circuits: Stability Guarantees for Mechanistic Circuits"
44	  authors: "Alaa Anani, Tobias Lorenz, Bernt Schiele, Mario Fritz, Jonas Fischer"
45	  year: 2026
46	  category: "method-component"
47	  role: "Stability via data subsampling (complementary orthogonal axis)"
48	  summary: >
49	    Wraps any black-box circuit discovery algorithm with randomized data subsampling
50	    (1000 subsamples) + per-neuron vote aggregation. Certifies that circuit component
51	    inclusion is invariant to bounded dataset edit-distance perturbations. Certified
52	    circuits: 91% higher accuracy, 45% fewer neurons vs baselines on ImageNet.
53	  relevance_to_css: >
54	    Complementary: addresses data stability (same method, different data subsets).
55	    CSS addresses method stability (same data, different algorithms). Could combine:
56	    run CSS consensus then certify the consensus circuit's data-robustness.
57	  discovered_date: "2026-05-12"
58	
59	- arxiv_id: "2602.16823"
60	  title: "Formal Mechanistic Interpretability: Automated Circuit Discovery with Provable Guarantees"
61	  authors: "Itamar Hadad, Guy Katz, Shahaf Bassan"
62	  year: 2026
63	  category: "method-component"
64	  role: "Formal verification for circuit discovery (ICLR 2026)"
65	  summary: >
66	    Integrates neural network verification tools into circuit discovery. Provides
67	    provable guarantees over continuous input domains: (i) input-domain robustness,
68	    (ii) patching-domain robustness, (iii) family of minimality guarantees
69	    (quasi-, local-, subset-, cardinal-minimality). Published at ICLR 2026.
70	  relevance_to_css: >
71	    Orthogonal: provides theoretical guarantees for a single discovery method.
72	    CSS is empirical cross-method consensus. Could use formal methods to verify
73	    that CSS consensus circuits satisfy minimality/faithfulness properties.
74	  discovered_date: "2026-05-12"
75	
76	- arxiv_id: "2604.16889"
77	  title: "PIE: A Cross-Layer Transcoder-Native Framework for Efficient Circuit Discovery via Feature Attribution"
78	  authors: "Qinhao Chen, Linyang He, Nima Mesgarani"
79	  year: 2026
80	  category: "method-component"
81	  role: "New circuit discovery method (CLT-native, could be input to CSS)"
82	  summary: >
83	    First CLT-native end-to-end framework. Feature Attribution Patching (FAP) scores
84	    CLT features by gradient-weighted write contributions. FAP-Synergy adds synergy-aware
85	    reranking. Evaluated with KL-divergence behavior retention and FADE-style metrics.
86	  relevance_to_css: >
87	    Potential new method to include in CSS ensemble. As CLT/transcoder methods become
88	    standard, CSS should demonstrate it can incorporate them alongside traditional
89	    edge-level methods. Not a competitor.
90	  discovered_date: "2026-05-12"
91	
92	- arxiv_id: "2602.16740"
93	  title: "Quantifying LLM Attention-Head Stability: Implications for Circuit Universality"
94	  authors: "Karan Bali, Jack Stanley, Praneet Suresh, Danilo Bzdok"
95	  year: 2026
96	  category: "evaluation"
97	  role: "Cross-seed stability analysis (motivates need for robust circuits)"
98	  summary: >
99	    Quantifies attention head similarity across independently initialized training runs.
100	    Middle-layer heads are least stable yet most representationally distinct. Deeper models
101	    show stronger mid-depth divergence. AdamW increases head stability for deeper models.
102	  relevance_to_css: >
103	    Motivational: shows circuits can be seed-dependent, strengthening the argument
104	    that consensus across methods (not just seeds) is needed for robust circuit claims.
105	    Citable as motivation in related work.
106	  discovered_date: "2026-05-12"
107	
108	- arxiv_id: "2510.00845"
109	  title: "Mechanistic Interpretability as Statistical Estimation: A Variance Analysis of EAP-IG"
110	  authors: "Unknown"
111	  year: 2025
112	  category: "evaluation"
113	  role: "Statistical stability framework for circuit discovery"
114	  summary: >
115	    Argues interpretability methods should be viewed as statistical estimators subject to
116	    variance/robustness questions. Systematic stability analysis of EAP-IG. Shows circuits
117	    are often reported without quantification of statistical stability or uncertainty.
118	  relevance_to_css: >
119	    Strong motivation paper for CSS. If a single method has high variance, cross-method
120	    consensus provides a principled way to identify edges that are stable regardless of
121	    estimation noise. Citable as framing/motivation.
122	  discovered_date: "2026-05-12"
123	
124	- arxiv_id: "2510.25786"
125	  title: "BlackboxNLP-2025 MIB Shared Task: Improving Circuit Faithfulness via Better Edge Selection"
126	  authors: "Yaniv Nikankin, Dana Arad, Itay Itzhak, Anja Reusch, Adi Simhi, Gal Kesten-Pomeranz, Yonatan Belinkov"
127	  year: 2025
128	  category: "method-component"
129	  role: "Bootstrapping for edge consistency + ILP selection"
130	  summary: >
131	    Three improvements: (1) bootstrapping to identify edges with consistent attribution scores,
132	    (2) ratio-based selection for strong positive edges, (3) integer linear programming
133	    formulation replacing greedy selection. Yields more faithful circuits on MIB.
134	  relevance_to_css: >
135	    Bootstrapping for intra-method edge consistency is related to CSS stability concept
136	    but limited to single method. ILP selection idea could inspire CSS aggregation.
137	  discovered_date: "2026-05-12"
138	
139	- arxiv_id: "2505.24731"
140	  title: "Circuit Stability Characterizes Language Model Generalization"
141	  authors: "Alan Sun"
142	  year: 2025
143	  category: "evaluation"
144	  role: "Circuit stability predicts generalization (ACL 2025)"
145	  summary: >
146	    Circuit stability = model applying consistent circuit across inputs. Through case studies
147	    on arithmetic and Boolean evaluation, shows stability predicts length/structural/compositional
148	    generalization. Stability can be induced via chain-of-thought prompting.
149	  relevance_to_css: >
150	    Downstream application: if CSS consensus circuits are more stable (by construction),
151	    they may better predict generalization. Potential evaluation angle for CSS paper.
152	  discovered_date: "2026-05-12"
153	
154	- arxiv_id: "2511.18409"
155	  title: "Findings of the BlackboxNLP 2025 Shared Task: Localizing Circuits and Causal Variables in Language Models"
156	  authors: "Shared Task Organizers"
157	  year: 2025
158	  category: "evaluation"
159	  role: "Benchmark and evaluation framework for circuit localization"
160	  summary: >
161	    Two tracks: circuit localization (causally influential components) and causal variable
162	    localization (mapping activations to interpretable features). Three teams, eight methods.
163	    Ensemble and regularization strategies most effective. Evaluation via faithfulness curves.
164	  relevance_to_css: >
165	    MIB benchmark could be used to evaluate CSS. Finding that ensembles help validates
166	    the general direction. But no team did true cross-family consensus.
167	  discovered_date: "2026-05-12"
168	
169	- arxiv_id: "2505.17630"
170	  title: "GIM: Improved Interpretability for Large Language Models"
171	  authors: "Corti team"
172	  year: 2025
173	  category: "method-component"
174	  role: "Top-performing gradient method on MIB benchmark"
175	  summary: >
176	    Gradient Interaction Modifications — gradient-based circuit discovery method.
177	    Tops HuggingFace Mechanistic Interpretability Benchmark. Outperforms other methods
178	    in early layers; Integrated Gradients better in middle/late layers.
179	  relevance_to_css: >
180	    Strong single-method baseline to include in CSS ensemble. Layer-dependent performance
181	    differences across methods further motivates cross-method consensus.
182	  discovered_date: "2026-05-12"
183	
184	- arxiv_id: "2502.06852"
185	  title: "EAP-GP: Mitigating Saturation Effect in Gradient-based Automated Circuit Identification"
186	  authors: "Unknown"
187	  year: 2025
188	  category: "method-component"
189	  role: "Improved gradient-based circuit discovery (fixes EAP saturation)"
190	  summary: >
191	    Addresses gradient saturation in Edge Attribution Patching. Proposes gradient
192	    propagation fix for more accurate edge importance scoring.
193	  relevance_to_css: >
194	    Another gradient-family method variant. Existence of EAP, EAP-IG, EAP-GP shows
195	    intra-family variation — CSS's value is cross-family agreement, not intra-family.
196	  discovered_date: "2026-05-12"
197	
198	# ============================================================
199	# NOVELTY ASSESSMENT (as of 2026-05-12)
200	# ============================================================
201	# No paper found that performs TRUE cross-method consensus spanning
202	# different algorithm families (gradient-based vs mask-learning vs
203	# causal intervention). Specifically:
204	#
205	# - CIRCUS: intra-method (threshold variation within single algorithm)
206	# - Mondorf et al.: EAP-IG + EP (both gradient-family)
207	# - Nikankin et al.: bootstrapping within single method
208	# - Certified Circuits: data perturbation stability (single method)
209	#
210	# CSS's core novelty — binary consensus across algorithm families
211	# (e.g., EAP-IG vs ACDC vs subnetwork probing vs edge pruning)
212	# with principled cross-family agreement scoring — REMAINS UNCLAIMED
213	# as of 2026-05-12.
214	# ============================================================
215	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "601f1df8-be08-4c47-8f0a-4f4f8e76dba3",
  "isSidechain": false,
  "promptId": "16c2e1a1-23bf-4ab8-bc32-4fa92e1b898b",
  "type": "user",
  "uuid": "ff3c214e-97b6-445e-bd82-7e8054a142e1",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/literature_map.yaml",
      "content": "# Literature Map — structfuse-context (cross-method circuit consensus)\n# Last updated: 2026-05-12\n\n- arxiv_id: \"2603.00523\"\n  title: \"CIRCUS: Circuit Consensus under Uncertainty via Stability Ensembles\"\n  authors: \"Unknown (arXiv 2603.00523v2)\"\n  year: 2026\n  category: \"direct-competitor\"\n  role: \"Primary competitor — intra-method stability scoring\"\n  summary: >\n    Constructs ensemble of attribution graphs by pruning a single raw attribution\n    run under multiple threshold configurations. Assigns per-edge stability score\n    (fraction of configs retaining it). Strict-consensus circuit = edges in all views.\n    ~40x smaller than union on Gemma-2-2B/Llama-3.2-1B while retaining explanatory power.\n    Consensus nodes beat non-consensus controls in activation patching (p=0.0004).\n  relevance_to_css: >\n    CLOSEST competitor but fundamentally intra-method: varies thresholds within ONE\n    attribution algorithm. Does NOT combine across algorithm families (gradient vs mask\n    vs causal). CSS's cross-method consensus remains a distinct and unclaimed novelty.\n    v2 update (2026-03-20) is same paper, no separate follow-up found.\n  discovered_date: \"2026-05-12\"\n\n- arxiv_id: \"2510.06811\"\n  title: \"BlackboxNLP-2025 MIB Shared Task: Exploring Ensemble Strategies for Circuit Localization Methods\"\n  authors: \"Mondorf, Wang et al.\"\n  year: 2025\n  category: \"direct-competitor\"\n  role: \"Limited cross-method ensembling (EAP-IG + Edge Pruning)\"\n  summary: >\n    Explores parallel ensembling (averaging/min/max of attribution scores across methods)\n    and sequential ensembling (EAP-IG warm-start then Edge Pruning refinement).\n    Parallel ensemble over all variants achieves best CMD=0.03, CPR=1.83 on MIB leaderboard.\n    Workshop short paper at BlackboxNLP 2025.\n  relevance_to_css: >\n    Closest to cross-method but limited: only combines EAP-IG and Edge Pruning, both\n    gradient-based edge attribution methods from the same algorithmic family.\n    No causal/mask-based methods included. Simple score aggregation (avg/min/max),\n    no principled consensus framework. CSS goes beyond by spanning algorithm families\n    and providing binary consensus with confidence scoring.\n  discovered_date: \"2026-05-12\"\n\n- arxiv_id: \"2602.22968\"\n  title: \"Certified Circuits: Stability Guarantees for Mechanistic Circuits\"\n  authors: \"Alaa Anani, Tobias Lorenz, Bernt Schiele, Mario Fritz, Jonas Fischer\"\n  year: 2026\n  category: \"method-component\"\n  role: \"Stability via data subsampling (complementary orthogonal axis)\"\n  summary: >\n    Wraps any black-box circuit discovery algorithm with randomized data subsampling\n    (1000 subsamples) + per-neuron vote aggregation. Certifies that circuit component\n    inclusion is invariant to bounded dataset edit-distance perturbations. Certified\n    circuits: 91% higher accuracy, 45% fewer neurons vs baselines on ImageNet.\n  relevance_to_css: >\n    Complementary: addresses data stability (same method, different data subsets).\n    CSS addresses method stability (same data, different algorithms). Could combine:\n    run CSS consensus then certify the consensus circuit's data-robustness.\n  discovered_date: \"2026-05-12\"\n\n- arxiv_id: \"2602.16823\"\n  title: \"Formal Mechanistic Interpretability: Automated Circuit Discovery with Provable Guarantees\"\n  authors: \"Itamar Hadad, Guy Katz, Shahaf Bassan\"\n  year: 2026\n  category: \"method-component\"\n  role: \"Formal verification for circuit discovery (ICLR 2026)\"\n  summary: >\n    Integrates neural network verification tools into circuit discovery. Provides\n    provable guarantees over continuous input domains: (i) input-domain robustness,\n    (ii) patching-domain robustness, (iii) family of minimality guarantees\n    (quasi-, local-, subset-, cardinal-minimality). Published at ICLR 2026.\n  relevance_to_css: >\n    Orthogonal: provides theoretical guarantees for a single discovery method.\n    CSS is empirical cross-method consensus. Could use formal methods to verify\n    that CSS consensus circuits satisfy minimality/faithfulness properties.\n  discovered_date: \"2026-05-12\"\n\n- arxiv_id: \"2604.16889\"\n  title: \"PIE: A Cross-Layer Transcoder-Native Framework for Efficient Circuit Discovery via Feature Attribution\"\n  authors: \"Qinhao Chen, Linyang He, Nima Mesgarani\"\n  year: 2026\n  category: \"method-component\"\n  role: \"New circuit discovery method (CLT-native, could be input to CSS)\"\n  summary: >\n    First CLT-native end-to-end framework. Feature Attribution Patching (FAP) scores\n    CLT features by gradient-weighted write contributions. FAP-Synergy adds synergy-aware\n    reranking. Evaluated with KL-divergence behavior retention and FADE-style metrics.\n  relevance_to_css: >\n    Potential new method to include in CSS ensemble. As CLT/transcoder methods become\n    standard, CSS should demonstrate it can incorporate them alongside traditional\n    edge-level methods. Not a competitor.\n  discovered_date: \"2026-05-12\"\n\n- arxiv_id: \"2602.16740\"\n  title: \"Quantifying LLM Attention-Head Stability: Implications for Circuit Universality\"\n  authors: \"Karan Bali, Jack Stanley, Praneet Suresh, Danilo Bzdok\"\n  year: 2026\n  category: \"evaluation\"\n  role: \"Cross-seed stability analysis (motivates need for robust circuits)\"\n  summary: >\n    Quantifies attention head similarity across independently initialized training runs.\n    Middle-layer heads are least stable yet most representationally distinct. Deeper models\n    show stronger mid-depth divergence. AdamW increases head stability for deeper models.\n  relevance_to_css: >\n    Motivational: shows circuits can be seed-dependent, strengthening the argument\n    that consensus across methods (not just seeds) is needed for robust circuit claims.\n    Citable as motivation in related work.\n  discovered_date: \"2026-05-12\"\n\n- arxiv_id: \"2510.00845\"\n  title: \"Mechanistic Interpretability as Statistical Estimation: A Variance Analysis of EAP-IG\"\n  authors: \"Unknown\"\n  year: 2025\n  category: \"evaluation\"\n  role: \"Statistical stability framework for circuit discovery\"\n  summary: >\n    Argues interpretability methods should be viewed as statistical estimators subject to\n    variance/robustness questions. Systematic stability analysis of EAP-IG. Shows circuits\n    are often reported without quantification of statistical stability or uncertainty.\n  relevance_to_css: >\n    Strong motivation paper for CSS. If a single method has high variance, cross-method\n    consensus provides a principled way to identify edges that are stable regardless of\n    estimation noise. Citable as framing/motivation.\n  discovered_date: \"2026-05-12\"\n\n- arxiv_id: \"2510.25786\"\n  title: \"BlackboxNLP-2025 MIB Shared Task: Improving Circuit Faithfulness via Better Edge Selection\"\n  authors: \"Yaniv Nikankin, Dana Arad, Itay Itzhak, Anja Reusch, Adi Simhi, Gal Kesten-Pomeranz, Yonatan Belinkov\"\n  year: 2025\n  category: \"method-component\"\n  role: \"Bootstrapping for edge consistency + ILP selection\"\n  summary: >\n    Three improvements: (1) bootstrapping to identify edges with consistent attribution scores,\n    (2) ratio-based selection for strong positive edges, (3) integer linear programming\n    formulation replacing greedy selection. Yields more faithful circuits on MIB.\n  relevance_to_css: >\n    Bootstrapping for intra-method edge consistency is related to CSS stability concept\n    but limited to single method. ILP selection idea could inspire CSS aggregation.\n  discovered_date: \"2026-05-12\"\n\n- arxiv_id: \"2505.24731\"\n  title: \"Circuit Stability Characterizes Language Model Generalization\"\n  authors: \"Alan Sun\"\n  year: 2025\n  category: \"evaluation\"\n  role: \"Circuit stability predicts generalization (ACL 2025)\"\n  summary: >\n    Circuit stability = model applying consistent circuit across inputs. Through case studies\n    on arithmetic and Boolean evaluation, shows stability predicts length/structural/compositional\n    generalization. Stability can be induced via chain-of-thought prompting.\n  relevance_to_css: >\n    Downstream application: if CSS consensus circuits are more stable (by construction),\n    they may better predict generalization. Potential evaluation angle for CSS paper.\n  discovered_date: \"2026-05-12\"\n\n- arxiv_id: \"2511.18409\"\n  title: \"Findings of the BlackboxNLP 2025 Shared Task: Localizing Circuits and Causal Variables in Language Models\"\n  authors: \"Shared Task Organizers\"\n  year: 2025\n  category: \"evaluation\"\n  role: \"Benchmark and evaluation framework for circuit localization\"\n  summary: >\n    Two tracks: circuit localization (causally influential components) and causal variable\n    localization (mapping activations to interpretable features). Three teams, eight methods.\n    Ensemble and regularization strategies most effective. Evaluation via faithfulness curves.\n  relevance_to_css: >\n    MIB benchmark could be used to evaluate CSS. Finding that ensembles help validates\n    the general direction. But no team did true cross-family consensus.\n  discovered_date: \"2026-05-12\"\n\n- arxiv_id: \"2505.17630\"\n  title: \"GIM: Improved Interpretability for Large Language Models\"\n  authors: \"Corti team\"\n  year: 2025\n  category: \"method-component\"\n  role: \"Top-performing gradient method on MIB benchmark\"\n  summary: >\n    Gradient Interaction Modifications — gradient-based circuit discovery method.\n    Tops HuggingFace Mechanistic Interpretability Benchmark. Outperforms other methods\n    in early layers; Integrated Gradients better in middle/late layers.\n  relevance_to_css: >\n    Strong single-method baseline to include in CSS ensemble. Layer-dependent performance\n    differences across methods further motivates cross-method consensus.\n  discovered_date: \"2026-05-12\"\n\n- arxiv_id: \"2502.06852\"\n  title: \"EAP-GP: Mitigating Saturation Effect in Gradient-based Automated Circuit Identification\"\n  authors: \"Unknown\"\n  year: 2025\n  category: \"method-component\"\n  role: \"Improved gradient-based circuit discovery (fixes EAP saturation)\"\n  summary: >\n    Addresses gradient saturation in Edge Attribution Patching. Proposes gradient\n    propagation fix for more accurate edge importance scoring.\n  relevance_to_css: >\n    Another gradient-family method variant. Existence of EAP, EAP-IG, EAP-GP shows\n    intra-family variation — CSS's value is cross-family agreement, not intra-family.\n  discovered_date: \"2026-05-12\"\n\n# ============================================================\n# NOVELTY ASSESSMENT (as of 2026-05-12)\n# ============================================================\n# No paper found that performs TRUE cross-method consensus spanning\n# different algorithm families (gradient-based vs mask-learning vs\n# causal intervention). Specifically:\n#\n# - CIRCUS: intra-method (threshold variation within single algorithm)\n# - Mondorf et al.: EAP-IG + EP (both gradient-family)\n# - Nikankin et al.: bootstrapping within single method\n# - Certified Circuits: data perturbation stability (single method)\n#\n# CSS's core novelty — binary consensus across algorithm families\n# (e.g., EAP-IG vs ACDC vs subnetwork probing vs edge pruning)\n# with principled cross-family agreement scoring — REMAINS UNCLAIMED\n# as of 2026-05-12.\n# ============================================================\n",
      "numLines": 215,
      "startLine": 1,
      "totalLines": 215
    }
  },
  "sourceToolAssistantUUID": "601f1df8-be08-4c47-8f0a-4f4f8e76dba3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context",
  "sessionId": "f2480f86-9e1e-4510-980e-6abe201dd7a7",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 24 · 2026-05-13T02:20:56.258Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have both files. Let me identify what's missing from the survey:

1. **Mondorf et al. (2510.06811)** — in literature_map.yaml but NOT in the survey
2. **PIE (2604.16889)** — in literature_map.yaml but NOT in the survey
3. **EAP-GP (2502.06852)** — in literature_map.yaml but NOT in the survey
4. **GIM (2505.17630)** — in literature_map.yaml but NOT in the survey

Also missing from survey but in literature_map:


- Bali et al. (2602.16740) - Quantifying LLM Attention-Head Stability
- Nikankin et al. (2510.25786) - BlackboxNLP-2025 MIB Shared Task: Improving Circuit Faithfulness
- BlackboxNLP shared task findings (2511.18409)

But the task only asks about the 4 papers listed above.

Now let me also check Takeaway #5 in the survey. The current version at lines 184-185 starts with "Distribution-shift robustness is a novel evaluation angle" and mentions that no existing work systematically evaluates whether consensus...

Looking at the next thinking, it continues with how circuits maintain faithfulness under distribution shift, and CSS's off-diagonal evaluation is positioned as a distinctive contribution. But since OOD experiments are deferred to Phase 2, I need to reframe this as a planned contribution rather than a current one.

Now I'm working through the placement of the additional papers. Mondorf et al. should go in Direction 1 as a direct competitor since it also looks at cross-method consensus. PIE, EAP-GP, and GIM are method-component papers that fit better in Direction 3 or the Additional Relevant Work section. Let me integrate these appropriately and update Takeaway #5 to reflect that the distribution-shift evaluation is something CSS will address in its next phase. I'm settling on placing Mondorf et al. in Direction 1 as section 1.5 since it's a direct competitor using cross-method ensembling, then moving PIE, EAP-GP, and GIM to Additional Relevant Work as method-component papers rather than core directional work.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ff3c214e-97b6-445e-bd82-7e8054a142e1",
  "isSidechain": false,
  "requestId": "req_011CaymYb55mDnWp2zVf8b4k",
  "type": "assistant",
  "uuid": "16585b7d-b978-439b-927c-4a4987fc9cad",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context",
  "sessionId": "f2480f86-9e1e-4510-980e-6abe201dd7a7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015DtaSe6X9vkcwS7ev8cGNQ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3658,
      "cache_read_input_tokens": 29620,
      "output_tokens": 1929,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3658,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1929,
          "cache_read_input_tokens": 29620,
          "cache_creation_input_tokens": 3658,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3658
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

_source line 25 · 2026-05-13T02:20:56.340Z_

两个文件都已读取。现在执行编辑：添加 4 篇缺失论文 + 修正 Takeaway #5。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "16585b7d-b978-439b-927c-4a4987fc9cad",
  "isSidechain": false,
  "requestId": "req_011CaymYb55mDnWp2zVf8b4k",
  "type": "assistant",
  "uuid": "aeca4c23-ec08-48fd-8c3c-90c906017115",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context",
  "sessionId": "f2480f86-9e1e-4510-980e-6abe201dd7a7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015DtaSe6X9vkcwS7ev8cGNQ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3658,
      "cache_read_input_tokens": 29620,
      "output_tokens": 1929,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3658,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1929,
          "cache_read_input_tokens": 29620,
          "cache_creation_input_tokens": 3658,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3658
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

_source line 26 · 2026-05-13T02:21:16.600Z_

<details open><summary>🔧 Tool call — Edit · `toolu_016tY8TL67RS1r6c3MZryh95`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/_project/report/literature_survey_related_work.md",
  "old_string": "### 1.4 Circuit Tracing: Revealing Computational Graphs in Language Models\n- **Authors:** Anthropic (Dario Amodei team)\n- **Year:** 2025\n- **Venue:** Anthropic Technical Report (March 2025)\n- **Core findings:** Uses cross-layer transcoders to build attribution graphs—graphical representations of computational steps where nodes are features and edges are causal interactions. Open-sourced circuit tracing tools supporting Gemma-2-2B, Llama-3.1-1B, Qwen3-4B.\n- **Relation to CSS:** **互补 (Complementary)**. Provides a different paradigm (feature-level circuits via transcoders vs. component-level circuits). CSS methods operate at edge/component level; circuit tracing works at feature level. Represents a parallel direction worth acknowledging.\n\n---",
  "new_string": "### 1.4 Circuit Tracing: Revealing Computational Graphs in Language Models\n- **Authors:** Anthropic (Dario Amodei team)\n- **Year:** 2025\n- **Venue:** Anthropic Technical Report (March 2025)\n- **Core findings:** Uses cross-layer transcoders to build attribution graphs—graphical representations of computational steps where nodes are features and edges are causal interactions. Open-sourced circuit tracing tools supporting Gemma-2-2B, Llama-3.1-1B, Qwen3-4B.\n- **Relation to CSS:** **互补 (Complementary)**. Provides a different paradigm (feature-level circuits via transcoders vs. component-level circuits). CSS methods operate at edge/component level; circuit tracing works at feature level. Represents a parallel direction worth acknowledging.\n\n### 1.5 Exploring Ensemble Strategies for Circuit Localization Methods (Mondorf et al.)\n- **Authors:** Mondorf, Wang et al.\n- **Year:** 2025 (arXiv: 2510.06811)\n- **Venue:** BlackboxNLP 2025 (Workshop short paper, MIB Shared Task)\n- **Core findings:** Explores parallel ensembling (averaging/min/max of attribution scores across methods) and sequential ensembling (EAP-IG warm-start then Edge Pruning refinement) for circuit localization. Parallel ensemble over all variants achieves best CMD=0.03, CPR=1.83 on the MIB leaderboard.\n- **Relation to CSS:** **直接竞争 (Direct competitor — limited scope)**. The closest existing work to cross-method circuit ensembling, but with critical limitations: (1) **仅限 gradient 族方法**: only combines EAP-IG and Edge Pruning, both gradient-based edge attribution methods from the same algorithmic family — no causal/mask-based methods (e.g., ACDC) included; (2) **Score averaging 而非 binary consensus**: uses simple score aggregation (avg/min/max) rather than principled binary agreement, inheriting score calibration issues across methods with incomparable scales; (3) **无 consensus 理论框架**: no analysis of method agreement patterns, confidence scoring, or consensus circuit properties; (4) **Workshop short paper 规模**: limited evaluation scope compared to CSS's full pipeline. CSS goes beyond by spanning algorithm families (gradient-based vs. iterative patching vs. mask optimization), providing binary consensus with confidence scoring, and analyzing consensus circuit properties (size, faithfulness, robustness).\n\n---"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "aeca4c23-ec08-48fd-8c3c-90c906017115",
  "isSidechain": false,
  "requestId": "req_011CaymYb55mDnWp2zVf8b4k",
  "type": "assistant",
  "uuid": "fd499962-dcc2-418c-af20-2d6eaf2bfb7a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context",
  "sessionId": "f2480f86-9e1e-4510-980e-6abe201dd7a7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015DtaSe6X9vkcwS7ev8cGNQ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3658,
      "cache_read_input_tokens": 29620,
      "output_tokens": 1929,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3658,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1929,
          "cache_read_input_tokens": 29620,
          "cache_creation_input_tokens": 3658,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3658
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

_source line 27 · 2026-05-13T02:21:16.631Z_

<details><summary>↩ Tool result · `toolu_016tY8TL67RS1r6c3MZryh95`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/_project/report/literature_survey_related_work.md has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fd499962-dcc2-418c-af20-2d6eaf2bfb7a",
  "isSidechain": false,
  "promptId": "16c2e1a1-23bf-4ab8-bc32-4fa92e1b898b",
  "type": "user",
  "uuid": "a503efd7-49b8-4571-ae03-cc219d5fbaf5",
  "toolUseResult": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/_project/report/literature_survey_related_work.md",
    "oldString": "### 1.4 Circuit Tracing: Revealing Computational Graphs in Language Models\n- **Authors:** Anthropic (Dario Amodei team)\n- **Year:** 2025\n- **Venue:** Anthropic Technical Report (March 2025)\n- **Core findings:** Uses cross-layer transcoders to build attribution graphs—graphical representations of computational steps where nodes are features and edges are causal interactions. Open-sourced circuit tracing tools supporting Gemma-2-2B, Llama-3.1-1B, Qwen3-4B.\n- **Relation to CSS:** **互补 (Complementary)**. Provides a different paradigm (feature-level circuits via transcoders vs. component-level circuits). CSS methods operate at edge/component level; circuit tracing works at feature level. Represents a parallel direction worth acknowledging.\n\n---",
    "newString": "### 1.4 Circuit Tracing: Revealing Computational Graphs in Language Models\n- **Authors:** Anthropic (Dario Amodei team)\n- **Year:** 2025\n- **Venue:** Anthropic Technical Report (March 2025)\n- **Core findings:** Uses cross-layer transcoders to build attribution graphs—graphical representations of computational steps where nodes are features and edges are causal interactions. Open-sourced circuit tracing tools supporting Gemma-2-2B, Llama-3.1-1B, Qwen3-4B.\n- **Relation to CSS:** **互补 (Complementary)**. Provides a different paradigm (feature-level circuits via transcoders vs. component-level circuits). CSS methods operate at edge/component level; circuit tracing works at feature level. Represents a parallel direction worth acknowledging.\n\n### 1.5 Exploring Ensemble Strategies for Circuit Localization Methods (Mondorf et al.)\n- **Authors:** Mondorf, Wang et al.\n- **Year:** 2025 (arXiv: 2510.06811)\n- **Venue:** BlackboxNLP 2025 (Workshop short paper, MIB Shared Task)\n- **Core findings:** Explores parallel ensembling (averaging/min/max of attribution scores across methods) and sequential ensembling (EAP-IG warm-start then Edge Pruning refinement) for circuit localization. Parallel ensemble over all variants achieves best CMD=0.03, CPR=1.83 on the MIB leaderboard.\n- **Relation to CSS:** **直接竞争 (Direct competitor — limited scope)**. The closest existing work to cross-method circuit ensembling, but with critical limitations: (1) **仅限 gradient 族方法**: only combines EAP-IG and Edge Pruning, both gradient-based edge attribution methods from the same algorithmic family — no causal/mask-based methods (e.g., ACDC) included; (2) **Score averaging 而非 binary consensus**: uses simple score aggregation (avg/min/max) rather than principled binary agreement, inheriting score calibration issues across methods with incomparable scales; (3) **无 consensus 理论框架**: no analysis of method agreement patterns, confidence scoring, or consensus circuit properties; (4) **Workshop short paper 规模**: limited evaluation scope compared to CSS's full pipeline. CSS goes beyond by spanning algorithm families (gradient-based vs. iterative patching vs. mask optimization), providing binary consensus with confidence scoring, and analyzing consensus circuit properties (size, faithfulness, robustness).\n\n---",
    "originalFile": null,
    "structuredPatch": [
      {
        "oldStart": 34,
        "oldLines": 6,
        "newStart": 34,
        "newLines": 13,
        "lines": [
          " - **Core findings:** Uses cross-layer transcoders to build attribution graphs—graphical representations of computational steps where nodes are features and edges are causal interactions. Open-sourced circuit tracing tools supporting Gemma-2-2B, Llama-3.1-1B, Qwen3-4B.",
          " - **Relation to CSS:** **互补 (Complementary)**. Provides a different paradigm (feature-level circuits via transcoders vs. component-level circuits). CSS methods operate at edge/component level; circuit tracing works at feature level. Represents a parallel direction worth acknowledging.",
          " ",
          "+### 1.5 Exploring Ensemble Strategies for Circuit Localization Methods (Mondorf et al.)",
          "+- **Authors:** Mondorf, Wang et al.",
          "+- **Year:** 2025 (arXiv: 2510.06811)",
          "+- **Venue:** BlackboxNLP 2025 (Workshop short paper, MIB Shared Task)",
          "+- **Core findings:** Explores parallel ensembling (averaging/min/max of attribution scores across methods) and sequential ensembling (EAP-IG warm-start then Edge Pruning refinement) for circuit localization. Parallel ensemble over all variants achieves best CMD=0.03, CPR=1.83 on the MIB leaderboard.",
          "+- **Relation to CSS:** **直接竞争 (Direct competitor — limited scope)**. The closest existing work to cross-method circuit ensembling, but with critical limitations: (1) **仅限 gradient 族方法**: only combines EAP-IG and Edge Pruning, both gradient-based edge attribution methods from the same algorithmic family — no causal/mask-based methods (e.g., ACDC) included; (2) **Score averaging 而非 binary consensus**: uses simple score aggregation (avg/min/max) rather than principled binary agreement, inheriting score calibration issues across methods with incomparable scales; (3) **无 consensus 理论框架**: no analysis of method agreement patterns, confidence scoring, or consensus circuit properties; (4) **Workshop short paper 规模**: limited evaluation scope compared to CSS's full pipeline. CSS goes beyond by spanning algorithm families (gradient-based vs. iterative patching vs. mask optimization), providing binary consensus with confidence scoring, and analyzing consensus circuit properties (size, faithfulness, robustness).",
          "+",
          " ---",
          " ",
          " ## Direction 2: Circuit Faithfulness Evaluation"
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  },
  "sourceToolAssistantUUID": "fd499962-dcc2-418c-af20-2d6eaf2bfb7a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context",
  "sessionId": "f2480f86-9e1e-4510-980e-6abe201dd7a7",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 28_

```json
{
  "type": "last-prompt",
  "leafUuid": "a503efd7-49b8-4571-ae03-cc219d5fbaf5",
  "sessionId": "f2480f86-9e1e-4510-980e-6abe201dd7a7"
}
```

---

### Runtime record

_source line 29_

```json
{
  "type": "ai-title",
  "aiTitle": "Merge literature files and fix survey takeaway",
  "sessionId": "f2480f86-9e1e-4510-980e-6abe201dd7a7"
}
```

---

### Tool call

_source line 30 · 2026-05-13T02:21:45.828Z_

<details open><summary>🔧 Tool call — Edit · `toolu_01KWjamqo8Soc93697r8Ew3G`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/_project/report/literature_survey_related_work.md",
  "old_string": "### RelP: Faithful and Efficient Circuit Discovery via Relevance Patching\n- **Authors:** Farnoush Rezaei Jafari et al.\n- **Year:** 2025\n- **Venue:** NeurIPS 2025 MechInterp Workshop (Spotlight)\n- **Core findings:** Replaces gradients in attribution patching with LRP propagation coefficients. For MLP outputs in GPT-2 Large, attribution patching achieves Pearson correlation 0.006 vs. RelP's 0.956 with activation patching ground truth. Faithfulness comparable to IG at lower cost.\n- **Relation to CSS:** **互补 (Complementary)**. Another discovery method with different inductive bias. Documents dramatic differences between methods on the same components—supports CSS's premise.\n\n---",
  "new_string": "### RelP: Faithful and Efficient Circuit Discovery via Relevance Patching\n- **Authors:** Farnoush Rezaei Jafari et al.\n- **Year:** 2025\n- **Venue:** NeurIPS 2025 MechInterp Workshop (Spotlight)\n- **Core findings:** Replaces gradients in attribution patching with LRP propagation coefficients. For MLP outputs in GPT-2 Large, attribution patching achieves Pearson correlation 0.006 vs. RelP's 0.956 with activation patching ground truth. Faithfulness comparable to IG at lower cost.\n- **Relation to CSS:** **互补 (Complementary)**. Another discovery method with different inductive bias. Documents dramatic differences between methods on the same components—supports CSS's premise.\n\n### PIE: A Cross-Layer Transcoder-Native Framework for Efficient Circuit Discovery via Feature Attribution\n- **Authors:** Qinhao Chen, Linyang He, Nima Mesgarani\n- **Year:** 2026 (arXiv: 2604.16889)\n- **Venue:** arXiv preprint (April 2026)\n- **Core findings:** First CLT-native end-to-end circuit discovery framework. Feature Attribution Patching (FAP) scores CLT features by gradient-weighted write contributions; FAP-Synergy adds synergy-aware reranking. Evaluated with KL-divergence behavior retention and FADE-style metrics.\n- **Relation to CSS:** **互补 (Complementary)**. Operates at the feature level via cross-layer transcoders rather than at the component/edge level. As CLT/transcoder methods become standard, PIE represents a potential additional discovery method for CSS's ensemble, bridging component-level and feature-level consensus.\n\n### EAP-GP: Mitigating Saturation Effect in Gradient-based Automated Circuit Identification\n- **Authors:** arXiv: 2502.06852\n- **Year:** 2025\n- **Venue:** arXiv preprint (Feb 2025)\n- **Core findings:** Addresses gradient saturation in Edge Attribution Patching by proposing a gradient propagation fix for more accurate edge importance scoring. Improves upon EAP/EAP-IG in faithfulness for circuits where saturation artifacts degrade standard gradient estimates.\n- **Relation to CSS:** **互补 (Complementary)**. Another intra-family gradient variant alongside EAP, EAP-IG. The proliferation of EAP variants (EAP → EAP-IG → EAP-GP) illustrates intra-family variation driven by specific failure modes—CSS's value lies in cross-family agreement that transcends these intra-family fixes.\n\n### GIM: Improved Interpretability for Large Language Models\n- **Authors:** Corti team\n- **Year:** 2025 (arXiv: 2505.17630)\n- **Venue:** arXiv preprint (May 2025)\n- **Core findings:** Gradient Interaction Modifications — gradient-based circuit discovery method that tops the HuggingFace Mechanistic Interpretability Benchmark. Outperforms other methods in early layers; Integrated Gradients performs better in middle/late layers, suggesting layer-dependent method strengths.\n- **Relation to CSS:** **互补 (Complementary)**. Strong single-method baseline. The finding that different gradient methods excel in different layers directly motivates cross-method consensus: no single method dominates across all model components. A potential candidate for inclusion in CSS's method ensemble.\n\n---"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a503efd7-49b8-4571-ae03-cc219d5fbaf5",
  "isSidechain": false,
  "requestId": "req_011CaymbsaqtyZrTpEhHhwpc",
  "type": "assistant",
  "uuid": "0156a182-8ef1-4126-b35a-00e7d4edada5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context",
  "sessionId": "f2480f86-9e1e-4510-980e-6abe201dd7a7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01P6QKnKxFbNmBxwwW1WiE4U",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2007,
      "cache_read_input_tokens": 33278,
      "output_tokens": 1174,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2007,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1174,
          "cache_read_input_tokens": 33278,
          "cache_creation_input_tokens": 2007,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2007
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

_source line 31 · 2026-05-13T02:21:45.931Z_

<details><summary>↩ Tool result · `toolu_01KWjamqo8Soc93697r8Ew3G`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/_project/report/literature_survey_related_work.md has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0156a182-8ef1-4126-b35a-00e7d4edada5",
  "isSidechain": false,
  "promptId": "16c2e1a1-23bf-4ab8-bc32-4fa92e1b898b",
  "type": "user",
  "uuid": "e5fe4d86-ac90-4f3c-9f08-f92674085134",
  "toolUseResult": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/_project/report/literature_survey_related_work.md",
    "oldString": "### RelP: Faithful and Efficient Circuit Discovery via Relevance Patching\n- **Authors:** Farnoush Rezaei Jafari et al.\n- **Year:** 2025\n- **Venue:** NeurIPS 2025 MechInterp Workshop (Spotlight)\n- **Core findings:** Replaces gradients in attribution patching with LRP propagation coefficients. For MLP outputs in GPT-2 Large, attribution patching achieves Pearson correlation 0.006 vs. RelP's 0.956 with activation patching ground truth. Faithfulness comparable to IG at lower cost.\n- **Relation to CSS:** **互补 (Complementary)**. Another discovery method with different inductive bias. Documents dramatic differences between methods on the same components—supports CSS's premise.\n\n---",
    "newString": "### RelP: Faithful and Efficient Circuit Discovery via Relevance Patching\n- **Authors:** Farnoush Rezaei Jafari et al.\n- **Year:** 2025\n- **Venue:** NeurIPS 2025 MechInterp Workshop (Spotlight)\n- **Core findings:** Replaces gradients in attribution patching with LRP propagation coefficients. For MLP outputs in GPT-2 Large, attribution patching achieves Pearson correlation 0.006 vs. RelP's 0.956 with activation patching ground truth. Faithfulness comparable to IG at lower cost.\n- **Relation to CSS:** **互补 (Complementary)**. Another discovery method with different inductive bias. Documents dramatic differences between methods on the same components—supports CSS's premise.\n\n### PIE: A Cross-Layer Transcoder-Native Framework for Efficient Circuit Discovery via Feature Attribution\n- **Authors:** Qinhao Chen, Linyang He, Nima Mesgarani\n- **Year:** 2026 (arXiv: 2604.16889)\n- **Venue:** arXiv preprint (April 2026)\n- **Core findings:** First CLT-native end-to-end circuit discovery framework. Feature Attribution Patching (FAP) scores CLT features by gradient-weighted write contributions; FAP-Synergy adds synergy-aware reranking. Evaluated with KL-divergence behavior retention and FADE-style metrics.\n- **Relation to CSS:** **互补 (Complementary)**. Operates at the feature level via cross-layer transcoders rather than at the component/edge level. As CLT/transcoder methods become standard, PIE represents a potential additional discovery method for CSS's ensemble, bridging component-level and feature-level consensus.\n\n### EAP-GP: Mitigating Saturation Effect in Gradient-based Automated Circuit Identification\n- **Authors:** arXiv: 2502.06852\n- **Year:** 2025\n- **Venue:** arXiv preprint (Feb 2025)\n- **Core findings:** Addresses gradient saturation in Edge Attribution Patching by proposing a gradient propagation fix for more accurate edge importance scoring. Improves upon EAP/EAP-IG in faithfulness for circuits where saturation artifacts degrade standard gradient estimates.\n- **Relation to CSS:** **互补 (Complementary)**. Another intra-family gradient variant alongside EAP, EAP-IG. The proliferation of EAP variants (EAP → EAP-IG → EAP-GP) illustrates intra-family variation driven by specific failure modes—CSS's value lies in cross-family agreement that transcends these intra-family fixes.\n\n### GIM: Improved Interpretability for Large Language Models\n- **Authors:** Corti team\n- **Year:** 2025 (arXiv: 2505.17630)\n- **Venue:** arXiv preprint (May 2025)\n- **Core findings:** Gradient Interaction Modifications — gradient-based circuit discovery method that tops the HuggingFace Mechanistic Interpretability Benchmark. Outperforms other methods in early layers; Integrated Gradients performs better in middle/late layers, suggesting layer-dependent method strengths.\n- **Relation to CSS:** **互补 (Complementary)**. Strong single-method baseline. The finding that different gradient methods excel in different layers directly motivates cross-method consensus: no single method dominates across all model components. A potential candidate for inclusion in CSS's method ensemble.\n\n---",
    "originalFile": null,
    "structuredPatch": [
      {
        "oldStart": 169,
        "oldLines": 6,
        "newStart": 169,
        "newLines": 27,
        "lines": [
          " - **Core findings:** Replaces gradients in attribution patching with LRP propagation coefficients. For MLP outputs in GPT-2 Large, attribution patching achieves Pearson correlation 0.006 vs. RelP's 0.956 with activation patching ground truth. Faithfulness comparable to IG at lower cost.",
          " - **Relation to CSS:** **互补 (Complementary)**. Another discovery method with different inductive bias. Documents dramatic differences between methods on the same components—supports CSS's premise.",
          " ",
          "+### PIE: A Cross-Layer Transcoder-Native Framework for Efficient Circuit Discovery via Feature Attribution",
          "+- **Authors:** Qinhao Chen, Linyang He, Nima Mesgarani",
          "+- **Year:** 2026 (arXiv: 2604.16889)",
          "+- **Venue:** arXiv preprint (April 2026)",
          "+- **Core findings:** First CLT-native end-to-end circuit discovery framework. Feature Attribution Patching (FAP) scores CLT features by gradient-weighted write contributions; FAP-Synergy adds synergy-aware reranking. Evaluated with KL-divergence behavior retention and FADE-style metrics.",
          "+- **Relation to CSS:** **互补 (Complementary)**. Operates at the feature level via cross-layer transcoders rather than at the component/edge level. As CLT/transcoder methods become standard, PIE represents a potential additional discovery method for CSS's ensemble, bridging component-level and feature-level consensus.",
          "+",
          "+### EAP-GP: Mitigating Saturation Effect in Gradient-based Automated Circuit Identification",
          "+- **Authors:** arXiv: 2502.06852",
          "+- **Year:** 2025",
          "+- **Venue:** arXiv preprint (Feb 2025)",
          "+- **Core findings:** Addresses gradient saturation in Edge Attribution Patching by proposing a gradient propagation fix for more accurate edge importance scoring. Improves upon EAP/EAP-IG in faithfulness for circuits where saturation artifacts degrade standard gradient estimates.",
          "+- **Relation to CSS:** **互补 (Complementary)**. Another intra-family gradient variant alongside EAP, EAP-IG. The proliferation of EAP variants (EAP → EAP-IG → EAP-GP) illustrates intra-family variation driven by specific failure modes—CSS's value lies in cross-family agreement that transcends these intra-family fixes.",
          "+",
          "+### GIM: Improved Interpretability for Large Language Models",
          "+- **Authors:** Corti team",
          "+- **Year:** 2025 (arXiv: 2505.17630)",
          "+- **Venue:** arXiv preprint (May 2025)",
          "+- **Core findings:** Gradient Interaction Modifications — gradient-based circuit discovery method that tops the HuggingFace Mechanistic Interpretability Benchmark. Outperforms other methods in early layers; Integrated Gradients performs better in middle/late layers, suggesting layer-dependent method strengths.",
          "+- **Relation to CSS:** **互补 (Complementary)**. Strong single-method baseline. The finding that different gradient methods excel in different layers directly motivates cross-method consensus: no single method dominates across all model components. A potential candidate for inclusion in CSS's method ensemble.",
          "+",
          " ---",
          " ",
          " ## Key Takeaways for CSS Positioning"
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  },
  "sourceToolAssistantUUID": "0156a182-8ef1-4126-b35a-00e7d4edada5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context",
  "sessionId": "f2480f86-9e1e-4510-980e-6abe201dd7a7",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 32 · 2026-05-13T02:21:45.938Z_

```json
{
  "parentUuid": "e5fe4d86-ac90-4f3c-9f08-f92674085134",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "48284915-39d2-4fa7-883f-4f4505e71b10",
  "timestamp": "2026-05-13T02:21:45.938Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context",
  "sessionId": "f2480f86-9e1e-4510-980e-6abe201dd7a7",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 33 · 2026-05-13T02:21:48.736Z_

现在修正 Takeaway #5。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "48284915-39d2-4fa7-883f-4f4505e71b10",
  "isSidechain": false,
  "requestId": "req_011Cayme2ujSPeLvQvZo4BM6",
  "type": "assistant",
  "uuid": "ece88705-71b6-4733-bd0b-df5c9201deaa",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context",
  "sessionId": "f2480f86-9e1e-4510-980e-6abe201dd7a7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Kx8RmJC9qvUVkuX4KFFecM",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1339,
      "cache_read_input_tokens": 35285,
      "output_tokens": 327,
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
          "output_tokens": 327,
          "cache_read_input_tokens": 35285,
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

### Tool call

_source line 34 · 2026-05-13T02:21:54.046Z_

<details open><summary>🔧 Tool call — Edit · `toolu_019TAMc7ApjEfgdT6B5aHw3b`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/_project/report/literature_survey_related_work.md",
  "old_string": "### 5. Distribution-shift robustness is a novel evaluation angle\nNo existing work systematically evaluates whether consensus circuits maintain faithfulness under distribution shift. CSS's off-diagonal evaluation (train on distribution A, test on distribution B) is a distinctive contribution.",
  "new_string": "### 5. Distribution-shift robustness is a planned novel evaluation angle\nNo existing work systematically evaluates whether consensus circuits maintain faithfulness under distribution shift. CSS 计划在 Phase 2 中系统性评估 consensus circuits 在分布偏移下的鲁棒性（off-diagonal evaluation: train on distribution A, test on distribution B），这将成为一个独特的贡献方向（Phase 2 planned, cf. D015）。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ece88705-71b6-4733-bd0b-df5c9201deaa",
  "isSidechain": false,
  "requestId": "req_011Cayme2ujSPeLvQvZo4BM6",
  "type": "assistant",
  "uuid": "fd8560a0-2637-48d3-8dca-49c0033b47af",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context",
  "sessionId": "f2480f86-9e1e-4510-980e-6abe201dd7a7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Kx8RmJC9qvUVkuX4KFFecM",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1339,
      "cache_read_input_tokens": 35285,
      "output_tokens": 327,
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
          "output_tokens": 327,
          "cache_read_input_tokens": 35285,
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

### Tool result

_source line 35 · 2026-05-13T02:21:54.058Z_

<details><summary>↩ Tool result · `toolu_019TAMc7ApjEfgdT6B5aHw3b`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/_project/report/literature_survey_related_work.md has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fd8560a0-2637-48d3-8dca-49c0033b47af",
  "isSidechain": false,
  "promptId": "16c2e1a1-23bf-4ab8-bc32-4fa92e1b898b",
  "type": "user",
  "uuid": "ea1e694c-9bb0-4064-b555-5f5ea50555a6",
  "toolUseResult": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/_project/report/literature_survey_related_work.md",
    "oldString": "### 5. Distribution-shift robustness is a novel evaluation angle\nNo existing work systematically evaluates whether consensus circuits maintain faithfulness under distribution shift. CSS's off-diagonal evaluation (train on distribution A, test on distribution B) is a distinctive contribution.",
    "newString": "### 5. Distribution-shift robustness is a planned novel evaluation angle\nNo existing work systematically evaluates whether consensus circuits maintain faithfulness under distribution shift. CSS 计划在 Phase 2 中系统性评估 consensus circuits 在分布偏移下的鲁棒性（off-diagonal evaluation: train on distribution A, test on distribution B），这将成为一个独特的贡献方向（Phase 2 planned, cf. D015）。",
    "originalFile": null,
    "structuredPatch": [
      {
        "oldStart": 209,
        "oldLines": 8,
        "newStart": 209,
        "newLines": 8,
        "lines": [
          " ### 4. Binary scoring is underexplored relative to continuous scoring",
          " Most methods produce continuous importance scores (EAP, EAP-IG, CD-T) and require threshold selection. Edge Pruning uses binary masks but within a single optimization. CSS's binary consensus (edge included/excluded per method → majority vote) is a distinct aggregation strategy that avoids score calibration issues across methods with incomparable scales.",
          " ",
          "-### 5. Distribution-shift robustness is a novel evaluation angle",
          "-No existing work systematically evaluates whether consensus circuits maintain faithfulness under distribution shift. CSS's off-diagonal evaluation (train on distribution A, test on distribution B) is a distinctive contribution.",
          "+### 5. Distribution-shift robustness is a planned novel evaluation angle",
          "+No existing work systematically evaluates whether consensus circuits maintain faithfulness under distribution shift. CSS 计划在 Phase 2 中系统性评估 consensus circuits 在分布偏移下的鲁棒性（off-diagonal evaluation: train on distribution A, test on distribution B），这将成为一个独特的贡献方向（Phase 2 planned, cf. D015）。",
          " ",
          " ### 6. Recommended related work structure for the paper",
          " 1. **Circuit discovery methods** (ACDC, EAP-IG, EP, CD-T, HAP) — establish method landscape"
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  },
  "sourceToolAssistantUUID": "fd8560a0-2637-48d3-8dca-49c0033b47af",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context",
  "sessionId": "f2480f86-9e1e-4510-980e-6abe201dd7a7",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 36 · 2026-05-13T02:22:00.543Z_

Now update the Takeaway #2 to include Mondorf et al. as a second competitor, and update the recommended related work structure to reflect the new papers.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ea1e694c-9bb0-4064-b555-5f5ea50555a6",
  "isSidechain": false,
  "requestId": "req_011CaymedphRhPxTb5xsCBcE",
  "type": "assistant",
  "uuid": "b3b71b6e-f989-439a-8c5a-5c693553d3ea",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context",
  "sessionId": "f2480f86-9e1e-4510-980e-6abe201dd7a7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RaupVQVSE88PSZp4Ydbdt2",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 388,
      "cache_read_input_tokens": 36624,
      "output_tokens": 572,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 388,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 572,
          "cache_read_input_tokens": 36624,
          "cache_creation_input_tokens": 388,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 388
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

_source line 37 · 2026-05-13T02:22:10.980Z_

<details open><summary>🔧 Tool call — Edit · `toolu_01S36tP54TRx289j75pT9TnV`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/_project/report/literature_survey_related_work.md",
  "old_string": "### 2. CIRCUS is the primary competitor — positioning is critical\nCIRCUS (Parekh, 2026) is the closest work. Key differentiation:\n- **CIRCUS:** varies pruning thresholds within one attribution method → threshold robustness\n- **CSS:** uses multiple independent discovery methods → method robustness\n- CSS argument: method diversity captures a broader space of inductive biases than threshold variation. A threshold ensemble still inherits the blind spots of its single underlying attribution method (e.g., EAP's first-order approximation errors). CSS's methods have structurally different failure modes (gradient-based vs. iterative patching vs. similarity-based).",
  "new_string": "### 2. CIRCUS and Mondorf et al. are the primary competitors — positioning is critical\nTwo closest works, each with distinct limitations:\n- **CIRCUS (Parekh, 2026):** varies pruning thresholds within one attribution method → threshold robustness within a single algorithm family\n- **Mondorf et al. (2510.06811):** ensembles EAP-IG + Edge Pruning via score averaging → cross-method but limited to gradient-family methods only, no binary consensus\n- **CSS:** uses multiple independent discovery methods spanning different algorithm families (gradient-based, iterative patching, mask optimization) → true cross-family method robustness with binary consensus\n- CSS argument: method diversity across algorithm families captures a broader space of inductive biases than either threshold variation (CIRCUS) or intra-family score averaging (Mondorf). CIRCUS inherits the blind spots of its single underlying method; Mondorf stays within the gradient family. CSS's methods have structurally different failure modes, and binary consensus avoids score calibration issues."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b3b71b6e-f989-439a-8c5a-5c693553d3ea",
  "isSidechain": false,
  "requestId": "req_011CaymedphRhPxTb5xsCBcE",
  "type": "assistant",
  "uuid": "17f0726e-a9b8-4f56-8f1e-2b09c7c5b068",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context",
  "sessionId": "f2480f86-9e1e-4510-980e-6abe201dd7a7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RaupVQVSE88PSZp4Ydbdt2",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 388,
      "cache_read_input_tokens": 36624,
      "output_tokens": 572,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 388,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 572,
          "cache_read_input_tokens": 36624,
          "cache_creation_input_tokens": 388,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 388
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

_source line 38 · 2026-05-13T02:22:11.036Z_

<details><summary>↩ Tool result · `toolu_01S36tP54TRx289j75pT9TnV`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/_project/report/literature_survey_related_work.md has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "17f0726e-a9b8-4f56-8f1e-2b09c7c5b068",
  "isSidechain": false,
  "promptId": "16c2e1a1-23bf-4ab8-bc32-4fa92e1b898b",
  "type": "user",
  "uuid": "bfdacfe4-3af6-4446-8e31-ecc6bd830840",
  "toolUseResult": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/_project/report/literature_survey_related_work.md",
    "oldString": "### 2. CIRCUS is the primary competitor — positioning is critical\nCIRCUS (Parekh, 2026) is the closest work. Key differentiation:\n- **CIRCUS:** varies pruning thresholds within one attribution method → threshold robustness\n- **CSS:** uses multiple independent discovery methods → method robustness\n- CSS argument: method diversity captures a broader space of inductive biases than threshold variation. A threshold ensemble still inherits the blind spots of its single underlying attribution method (e.g., EAP's first-order approximation errors). CSS's methods have structurally different failure modes (gradient-based vs. iterative patching vs. similarity-based).",
    "newString": "### 2. CIRCUS and Mondorf et al. are the primary competitors — positioning is critical\nTwo closest works, each with distinct limitations:\n- **CIRCUS (Parekh, 2026):** varies pruning thresholds within one attribution method → threshold robustness within a single algorithm family\n- **Mondorf et al. (2510.06811):** ensembles EAP-IG + Edge Pruning via score averaging → cross-method but limited to gradient-family methods only, no binary consensus\n- **CSS:** uses multiple independent discovery methods spanning different algorithm families (gradient-based, iterative patching, mask optimization) → true cross-family method robustness with binary consensus\n- CSS argument: method diversity across algorithm families captures a broader space of inductive biases than either threshold variation (CIRCUS) or intra-family score averaging (Mondorf). CIRCUS inherits the blind spots of its single underlying method; Mondorf stays within the gradient family. CSS's methods have structurally different failure modes, and binary consensus avoids score calibration issues.",
    "originalFile": null,
    "structuredPatch": [
      {
        "oldStart": 197,
        "oldLines": 11,
        "newStart": 197,
        "newLines": 12,
        "lines": [
          " ### 1. CSS fills a specific gap in the literature",
          " The field has established that (a) circuit discovery methods disagree (Syed et al. 2024; Méloux et al. 2025), (b) faithfulness metrics are unreliable (Miller et al. 2024), and (c) circuits are sensitive to analyst choices (CIRCUS, Certified Circuits). CSS is the first to exploit **cross-method binary consensus** as a robustness mechanism, using method diversity rather than threshold/data perturbation diversity.",
          " ",
          "-### 2. CIRCUS is the primary competitor — positioning is critical",
          "-CIRCUS (Parekh, 2026) is the closest work. Key differentiation:",
          "-- **CIRCUS:** varies pruning thresholds within one attribution method → threshold robustness",
          "-- **CSS:** uses multiple independent discovery methods → method robustness",
          "-- CSS argument: method diversity captures a broader space of inductive biases than threshold variation. A threshold ensemble still inherits the blind spots of its single underlying attribution method (e.g., EAP's first-order approximation errors). CSS's methods have structurally different failure modes (gradient-based vs. iterative patching vs. similarity-based).",
          "+### 2. CIRCUS and Mondorf et al. are the primary competitors — positioning is critical",
          "+Two closest works, each with distinct limitations:",
          "+- **CIRCUS (Parekh, 2026):** varies pruning thresholds within one attribution method → threshold robustness within a single algorithm family",
          "+- **Mondorf et al. (2510.06811):** ensembles EAP-IG + Edge Pruning via score averaging → cross-method but limited to gradient-family methods only, no binary consensus",
          "+- **CSS:** uses multiple independent discovery methods spanning different algorithm families (gradient-based, iterative patching, mask optimization) → true cross-family method robustness with binary consensus",
          "+- CSS argument: method diversity across algorithm families captures a broader space of inductive biases than either threshold variation (CIRCUS) or intra-family score averaging (Mondorf). CIRCUS inherits the blind spots of its single underlying method; Mondorf stays within the gradient family. CSS's methods have structurally different failure modes, and binary consensus avoids score calibration issues.",
          " ",
          " ### 3. The \"instability problem\" is well-documented — CSS offers a practical solution",
          " Multiple papers (Méloux et al., Franco et al., Miller et al.) document that circuits are unstable across data, prompts, and methodology. The Open Problems paper (Sharkey et al. 2025) explicitly calls for reporting ensembles. CSS directly operationalizes this recommendation with a concrete, lightweight algorithm."
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  },
  "sourceToolAssistantUUID": "17f0726e-a9b8-4f56-8f1e-2b09c7c5b068",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context",
  "sessionId": "f2480f86-9e1e-4510-980e-6abe201dd7a7",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-13T02:22:18.796Z_

<details open><summary>🔧 Tool call — Edit · `toolu_014pWtAyo9KTGppi7gtnorWg`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/_project/report/literature_survey_related_work.md",
  "old_string": "4. **Consensus/stability approaches** (CIRCUS, Certified Circuits) — position CSS against alternatives\n5. **Feature-level circuits** (Sparse Feature Circuits, Transcoders, Circuit Tracing) — acknowledge parallel direction, note CSS works at component level",
  "new_string": "4. **Consensus/stability approaches** (CIRCUS, Mondorf et al., Certified Circuits) — position CSS against alternatives\n5. **Feature-level circuits** (Sparse Feature Circuits, Transcoders, Circuit Tracing, PIE) — acknowledge parallel direction, note CSS works at component level\n6. **Method variants and benchmarks** (EAP-GP, GIM, MIB) — contextualize method landscape diversity that motivates cross-family consensus"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bfdacfe4-3af6-4446-8e31-ecc6bd830840",
  "isSidechain": false,
  "requestId": "req_011CaymftGP8MJRVcoLyLtPz",
  "type": "assistant",
  "uuid": "4298d13e-059f-4c4b-bf41-8e50f6a4ee62",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context",
  "sessionId": "f2480f86-9e1e-4510-980e-6abe201dd7a7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015KmZN6r3dDUPpGufBpdLGJ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 633,
      "cache_read_input_tokens": 37012,
      "output_tokens": 317,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 633,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 317,
          "cache_read_input_tokens": 37012,
          "cache_creation_input_tokens": 633,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 633
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

_source line 40 · 2026-05-13T02:22:18.816Z_

<details><summary>↩ Tool result · `toolu_014pWtAyo9KTGppi7gtnorWg`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/_project/report/literature_survey_related_work.md has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4298d13e-059f-4c4b-bf41-8e50f6a4ee62",
  "isSidechain": false,
  "promptId": "16c2e1a1-23bf-4ab8-bc32-4fa92e1b898b",
  "type": "user",
  "uuid": "fe6ea377-099c-431a-ae4f-e27032a21501",
  "toolUseResult": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/_project/report/literature_survey_related_work.md",
    "oldString": "4. **Consensus/stability approaches** (CIRCUS, Certified Circuits) — position CSS against alternatives\n5. **Feature-level circuits** (Sparse Feature Circuits, Transcoders, Circuit Tracing) — acknowledge parallel direction, note CSS works at component level",
    "newString": "4. **Consensus/stability approaches** (CIRCUS, Mondorf et al., Certified Circuits) — position CSS against alternatives\n5. **Feature-level circuits** (Sparse Feature Circuits, Transcoders, Circuit Tracing, PIE) — acknowledge parallel direction, note CSS works at component level\n6. **Method variants and benchmarks** (EAP-GP, GIM, MIB) — contextualize method landscape diversity that motivates cross-family consensus",
    "originalFile": null,
    "structuredPatch": [
      {
        "oldStart": 217,
        "oldLines": 5,
        "newStart": 217,
        "newLines": 6,
        "lines": [
          " 1. **Circuit discovery methods** (ACDC, EAP-IG, EP, CD-T, HAP) — establish method landscape",
          " 2. **Faithfulness evaluation** (Miller et al. 2024, Hanna et al. 2024) — motivate robustness concerns",
          " 3. **Circuit instability** (Méloux et al. 2025, Franco et al. 2026, Sun 2025) — establish the problem CSS solves",
          "-4. **Consensus/stability approaches** (CIRCUS, Certified Circuits) — position CSS against alternatives",
          "-5. **Feature-level circuits** (Sparse Feature Circuits, Transcoders, Circuit Tracing) — acknowledge parallel direction, note CSS works at component level",
          "+4. **Consensus/stability approaches** (CIRCUS, Mondorf et al., Certified Circuits) — position CSS against alternatives",
          "+5. **Feature-level circuits** (Sparse Feature Circuits, Transcoders, Circuit Tracing, PIE) — acknowledge parallel direction, note CSS works at component level",
          "+6. **Method variants and benchmarks** (EAP-GP, GIM, MIB) — contextualize method landscape diversity that motivates cross-family consensus"
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  },
  "sourceToolAssistantUUID": "4298d13e-059f-4c4b-bf41-8e50f6a4ee62",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context",
  "sessionId": "f2480f86-9e1e-4510-980e-6abe201dd7a7",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 41_

```json
{
  "type": "last-prompt",
  "leafUuid": "fe6ea377-099c-431a-ae4f-e27032a21501",
  "sessionId": "f2480f86-9e1e-4510-980e-6abe201dd7a7"
}
```

---

### Runtime record

_source line 42_

```json
{
  "type": "ai-title",
  "aiTitle": "Merge literature files and fix survey takeaway",
  "sessionId": "f2480f86-9e1e-4510-980e-6abe201dd7a7"
}
```

---

### Assistant

_source line 43 · 2026-05-13T02:22:21.665Z_

验证最终文件完整性。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fe6ea377-099c-431a-ae4f-e27032a21501",
  "isSidechain": false,
  "requestId": "req_011CaymgTry7iVa6RENHYpHK",
  "type": "assistant",
  "uuid": "c9305e08-e270-4526-a9d3-fa094774e604",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context",
  "sessionId": "f2480f86-9e1e-4510-980e-6abe201dd7a7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VTZrkwfFipyYFoq1vt8q6M",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 378,
      "cache_read_input_tokens": 37645,
      "output_tokens": 106,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 378,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 106,
          "cache_read_input_tokens": 37645,
          "cache_creation_input_tokens": 378,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 378
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

_source line 44 · 2026-05-13T02:22:22.285Z_

<details open><summary>🔧 Tool call — Read · `toolu_0129gjC19EzatXR2Qk2bqpmV`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/_project/report/literature_survey_related_work.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c9305e08-e270-4526-a9d3-fa094774e604",
  "isSidechain": false,
  "requestId": "req_011CaymgTry7iVa6RENHYpHK",
  "type": "assistant",
  "uuid": "4ae1b15d-cec4-425f-88a1-f3a46efeab38",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context",
  "sessionId": "f2480f86-9e1e-4510-980e-6abe201dd7a7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VTZrkwfFipyYFoq1vt8q6M",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 378,
      "cache_read_input_tokens": 37645,
      "output_tokens": 106,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 378,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 106,
          "cache_read_input_tokens": 37645,
          "cache_creation_input_tokens": 378,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 378
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

_source line 45 · 2026-05-13T02:22:22.340Z_

<details><summary>↩ Tool result · `toolu_0129gjC19EzatXR2Qk2bqpmV`</summary>

```text
1	# Related Work Literature Survey for CSS (Cross-method Structural Consensus)
2	
3	> Generated: 2026-05-13 | Target: EMNLP 2026 Main (ARR deadline 2026-05-25)
4	
5	---
6	
7	## Direction 1: Cross-method Consensus / Ensemble in Mechanistic Interpretability
8	
9	### 1.1 CIRCUS: Circuit Consensus under Uncertainty via Stability Ensembles
10	- **Authors:** Swapnil Parekh
11	- **Year:** 2026 (arXiv: 2603.00523)
12	- **Venue:** arXiv preprint (Feb 2026)
13	- **Core findings:** Reframes circuit discovery as an uncertainty-quantification problem. Constructs an ensemble of attribution graphs by pruning a *single* raw attribution run under multiple threshold configurations, assigns each edge a stability score (fraction of configs retaining it), and extracts a strict-consensus circuit (edges appearing in all views). On Gemma-2-2B and Llama-3.2-1B, strict consensus circuits are ~40× smaller than the union while retaining comparable explanatory power. Consensus-identified nodes beat matched non-consensus controls in causal relevance (p=0.0004).
14	- **Relation to CSS:** **直接竞争 (Primary competitor)**. CIRCUS varies pruning thresholds on a single attribution method to build consensus; CSS uses multiple independent discovery methods (EAP-IG, EP, ACDC/IFR). Key differentiators: (1) CSS captures cross-method agreement (different algorithms with different inductive biases), not just threshold robustness within one method; (2) CSS uses binary agreement rather than fractional stability scores; (3) CSS explicitly tests distribution-shift robustness. Must position CSS as complementary/stronger: method diversity > threshold diversity.
15	
16	### 1.2 Certified Circuits: Stability Guarantees for Mechanistic Circuits
17	- **Authors:** Alaa Anani, Tobias Lorenz, Bernt Schiele, et al.
18	- **Year:** 2026 (arXiv: 2602.22968)
19	- **Venue:** arXiv preprint (Feb 2026)
20	- **Core findings:** Wraps any black-box discovery algorithm with randomized data subsampling to certify that circuit component inclusion decisions are invariant to bounded edit-distance perturbations of the concept dataset. On ImageNet with ResNet-101, certified circuits achieved 96% accuracy vs 86% baseline using half the neurons. Addresses dataset-to-circuit instability.
21	- **Relation to CSS:** **互补 (Complementary)**. Certified Circuits focuses on data perturbation stability for vision models with formal guarantees; CSS focuses on method-agreement stability for language model circuits. Both address instability but from orthogonal angles. Could cite as motivation for why stability matters.
22	
23	### 1.3 Open Problems in Mechanistic Interpretability
24	- **Authors:** Lee Sharkey, Bilal Chughtai, Joshua Batson, et al. (29 authors, 18 organizations)
25	- **Year:** 2025 (arXiv: 2501.16496)
26	- **Venue:** arXiv preprint (Jan 2025), commissioned by Schmidt Sciences
27	- **Core findings:** Landmark collaborative paper establishing the field's consensus open problems. Highlights systematic non-identifiability: multiple circuits, features, and algorithm mappings can yield the same behavioral fidelity. Advocates reporting explanation ensembles and clarifying pragmatic vs. unicity criteria.
28	- **Relation to CSS:** **支持 (Supports CSS)**. Directly motivates multi-method consensus: if circuits are non-unique, reporting ensembles and agreement is essential. CSS operationalizes this recommendation.
29	
30	### 1.4 Circuit Tracing: Revealing Computational Graphs in Language Models
31	- **Authors:** Anthropic (Dario Amodei team)
32	- **Year:** 2025
33	- **Venue:** Anthropic Technical Report (March 2025)
34	- **Core findings:** Uses cross-layer transcoders to build attribution graphs—graphical representations of computational steps where nodes are features and edges are causal interactions. Open-sourced circuit tracing tools supporting Gemma-2-2B, Llama-3.1-1B, Qwen3-4B.
35	- **Relation to CSS:** **互补 (Complementary)**. Provides a different paradigm (feature-level circuits via transcoders vs. component-level circuits). CSS methods operate at edge/component level; circuit tracing works at feature level. Represents a parallel direction worth acknowledging.
36	
37	### 1.5 Exploring Ensemble Strategies for Circuit Localization Methods (Mondorf et al.)
38	- **Authors:** Mondorf, Wang et al.
39	- **Year:** 2025 (arXiv: 2510.06811)
40	- **Venue:** BlackboxNLP 2025 (Workshop short paper, MIB Shared Task)
41	- **Core findings:** Explores parallel ensembling (averaging/min/max of attribution scores across methods) and sequential ensembling (EAP-IG warm-start then Edge Pruning refinement) for circuit localization. Parallel ensemble over all variants achieves best CMD=0.03, CPR=1.83 on the MIB leaderboard.
42	- **Relation to CSS:** **直接竞争 (Direct competitor — limited scope)**. The closest existing work to cross-method circuit ensembling, but with critical limitations: (1) **仅限 gradient 族方法**: only combines EAP-IG and Edge Pruning, both gradient-based edge attribution methods from the same algorithmic family — no causal/mask-based methods (e.g., ACDC) included; (2) **Score averaging 而非 binary consensus**: uses simple score aggregation (avg/min/max) rather than principled binary agreement, inheriting score calibration issues across methods with incomparable scales; (3) **无 consensus 理论框架**: no analysis of method agreement patterns, confidence scoring, or consensus circuit properties; (4) **Workshop short paper 规模**: limited evaluation scope compared to CSS's full pipeline. CSS goes beyond by spanning algorithm families (gradient-based vs. iterative patching vs. mask optimization), providing binary consensus with confidence scoring, and analyzing consensus circuit properties (size, faithfulness, robustness).
43	
44	---
45	
46	## Direction 2: Circuit Faithfulness Evaluation
47	
48	### 2.1 Transformer Circuit Faithfulness Metrics Are Not Robust
49	- **Authors:** Joseph Miller, Bilal Chughtai, William Saunders
50	- **Year:** 2024
51	- **Venue:** COLM 2024
52	- **Core findings:** Faithfulness scores are highly sensitive to seemingly insignificant ablation methodology choices. Edge-level vs node-level ablation, resample vs mean ablation, and other methodological variations yield substantially different faithfulness percentages. Existing circuit faithfulness scores reflect researcher methodology as much as actual circuit quality.
53	- **Relation to CSS:** **强支持 (Strongly supports CSS)**. Core motivation for CSS: if single-method faithfulness metrics are unreliable, cross-method agreement provides a more robust signal. Directly supports the claim that binary consensus is more stable than score-dependent evaluation.
54	
55	### 2.2 Have Faith in Faithfulness: Going Beyond Circuit Overlap When Finding Model Mechanisms
56	- **Authors:** Michael Hanna, Sandro Pezzelle, Yonatan Belinkov
57	- **Year:** 2024
58	- **Venue:** COLM 2024 (also ICML 2024 MI Workshop Spotlight)
59	- **Core findings:** Introduces EAP-IG (EAP with integrated gradients) which finds more faithful circuits than EAP. Key finding: high node overlap ≠ high faithfulness. When comparing circuits, measuring overlap is no substitute for measuring faithfulness.
60	- **Relation to CSS:** **支持+基础方法 (Supports + foundational method)**. EAP-IG is one of CSS's three discovery methods. The finding that overlap ≠ faithfulness motivates CSS's use of faithfulness-based evaluation rather than simple circuit overlap metrics.
61	
62	### 2.3 MIB: A Mechanistic Interpretability Benchmark
63	- **Authors:** Yoav Goldberg, Yonatan Belinkov, et al.
64	- **Year:** 2025–2026 (arXiv: 2504.13151)
65	- **Venue:** ICML 2025 / ICLR 2026
66	- **Core findings:** Establishes two evaluation tracks—circuit localization and causal variable localization—across diverse tasks and models. Attribution and mask optimization methods perform best on circuit localization. Supervised DAS significantly outperforms unsupervised SAE features for causal variable localization.
67	- **Relation to CSS:** **互补 (Complementary)**. Provides standardized evaluation framework. CSS could adopt MIB tasks/metrics for evaluation; MIB results contextualize method performance differences.
68	
69	### 2.4 Functional Faithfulness in the Wild: Circuit Discovery with Differentiable Computation Graph Pruning
70	- **Authors:** Lei Yu, Jingcheng Niu, Zining Zhu, et al.
71	- **Year:** 2024 (arXiv: 2407.03779)
72	- **Venue:** arXiv preprint (July 2024)
73	- **Core findings:** Introduces DiscoGP—differentiable masking that prunes both weights and edges. Extracts sheaves preserving 93–100% model performance using only 1–7% of original weights/connections. Identifies that activation-patching-based circuits tend to be neither functionally faithful nor complete.
74	- **Relation to CSS:** **互补 (Complementary)**. Shows that weight+edge pruning yields more faithful circuits than edge-only approaches, further highlighting that methodology choices dramatically affect circuit quality—supporting CSS's cross-method approach.
75	
76	---
77	
78	## Direction 3: Binary vs Continuous Scoring in Circuit Discovery
79	
80	### 3.1 Finding Transformer Circuits with Edge Pruning
81	- **Authors:** Adithya Bhaskar, Alexander Wettig, Dan Friedman, et al.
82	- **Year:** 2024
83	- **Venue:** NeurIPS 2024
84	- **Core findings:** Frames circuit discovery as gradient-based optimization with binary masks over edges. EP is considerably more faithful on IOI and Greater-Than than both ACDC and EAP, especially at higher sparsities. Scales effectively to 100K examples where it is fastest and most faithful.
85	- **Relation to CSS:** **基础方法+支持 (Foundational method + supports)**. EP is one of CSS's discovery methods. Uses binary masks (0/1) for edge inclusion—directly relevant to CSS's binary consensus. Shows binary edge selection can be highly faithful.
86	
87	### 3.2 Attribution Patching Outperforms Automated Circuit Discovery
88	- **Authors:** Aaquib Syed, Can Rager, Arthur Conmy
89	- **Year:** 2024
90	- **Venue:** BlackboxNLP 2024 (NeurIPS Workshop)
91	- **Core findings:** A simple method based on attribution patching outperforms ACDC while requiring just two forward passes + one backward pass. However, EAP's first-order approximations show lower faithfulness to the full model than EP.
92	- **Relation to CSS:** **支持 (Supports)**. Documents that different methods (ACDC, EAP, EP) yield different circuits with different faithfulness levels—core motivation for cross-method consensus. Methods that are fast (EAP) and methods that are faithful (EP) produce systematically different results.
93	
94	### 3.3 Discovering Transformer Circuits via a Hybrid Attribution and Pruning Framework (HAP)
95	- **Authors:** Adithya Bhaskar, Alexander Wettig, et al.
96	- **Year:** 2025 (arXiv: 2510.03282)
97	- **Venue:** NeurIPS 2025
98	- **Core findings:** Two-stage pipeline: EAP filters unimportant edges (continuous scores → top-k), then EP refines with binary masks. HAP is ≥46% faster than EP while maintaining high faithfulness. Preserves cooperative circuit components (e.g., S-inhibition heads) that EAP alone prunes at high sparsity.
99	- **Relation to CSS:** **互补 (Complementary)**. Shows that combining methods sequentially (EAP→EP) improves over either alone. CSS takes a different combination approach: run methods independently, then take binary consensus. Complementary philosophies of method combination.
100	
101	### 3.4 Sparse Feature Circuits: Discovering and Editing Interpretable Causal Graphs in Language Models
102	- **Authors:** Samuel Marks, Can Rager, Eric Michaud, Yonatan Belinkov, David Bau, Aaron Mueller
103	- **Year:** 2025
104	- **Venue:** ICLR 2025 (Oral)
105	- **Core findings:** Uses SAEs to identify features, then discovers feature-level causal circuits. Small feature circuits (<100 nodes) explain a large proportion of model performance on subject-verb agreement. Introduces SHIFT for improving classifier generalization by ablating task-irrelevant features.
106	- **Relation to CSS:** **互补 (Complementary)**. Operates at feature level (SAE features) vs. CSS's component level (attention heads, MLPs). Shows that sparse/binary feature selection is powerful for circuit analysis. CSS could potentially extend to feature-level consensus in future work.
107	
108	### 3.5 Transcoders Find Interpretable LLM Feature Circuits
109	- **Authors:** Jacob Dunefsky, Philippe Morel, et al.
110	- **Year:** 2024
111	- **Venue:** NeurIPS 2024
112	- **Core findings:** Transcoders approximate dense MLP layers with wider, sparsely-activating layers. On par with SAEs in sparsity, faithfulness, and interpretability. Applied to reverse-engineer circuits in GPT-2-small including novel insights on the greater-than circuit.
113	- **Relation to CSS:** **互补 (Complementary)**. Offers alternative circuit representation (feature-level via transcoders). Relevant as a potential additional discovery method for CSS.
114	
115	---
116	
117	## Direction 4: Instability / Unreliability of Single-method Circuit Discovery
118	
119	### 4.1 Mechanistic Interpretability as Statistical Estimation: A Variance Analysis
120	- **Authors:** Maxime Méloux et al.
121	- **Year:** 2025–2026 (arXiv: 2510.00845, revised Feb 2026)
122	- **Venue:** arXiv preprint
123	- **Core findings:** Frames circuit discovery as a statistical estimation problem. Uncovers fundamental instability: single-input CMA scores exhibit high intrinsic variance—causal effects are volatile random variables, not fixed properties. Small perturbations in input data or hyperparameters yield vastly different circuits. Focuses on EAP and EAP-IG, systematically decomposing variance sources.
124	- **Relation to CSS:** **强支持 (Strongly supports CSS)**. Provides quantitative evidence that single-method circuits are unstable. Directly motivates CSS: if individual methods have high variance, cross-method consensus filters out method-specific noise.
125	
126	### 4.2 Circuit Stability Characterizes Language Model Generalization
127	- **Authors:** Alan Sun
128	- **Year:** 2025
129	- **Venue:** ACL 2025
130	- **Core findings:** Mathematically formalizes circuit stability—a model's ability to apply a consistent reasoning process (circuit) across inputs. Through three case studies, shows circuit stability predicts different aspects of generalization. Models that lack circuit stability fail to generalize.
131	- **Relation to CSS:** **支持 (Supports)**. Establishes that circuit stability is a valuable property. CSS targets a complementary notion of stability: consistency across methods rather than across inputs.
132	
133	### 4.3 Finding Highly Interpretable Prompt-Specific Circuits in Language Models
134	- **Authors:** Gabriel Franco, Lucas M. Tassis, Azalea Rohr, Mark Crovella
135	- **Year:** 2026 (arXiv: 2602.13483)
136	- **Venue:** arXiv preprint (Feb 2026)
137	- **Core findings:** Circuits are prompt-specific even within a fixed task. Applying ACC++ to IOI in GPT-2, Pythia, and Gemma 2: no single circuit for IOI in any model—different prompt templates induce systematically different mechanisms.
138	- **Relation to CSS:** **支持+挑战 (Supports + challenges)**. Supports CSS by showing single circuits are insufficient; challenges CSS to demonstrate that consensus circuits are more stable across prompts. CSS should test prompt-level robustness.
139	
140	### 4.4 Formal Mechanistic Interpretability: Automated Circuit Discovery with Provable Guarantees
141	- **Authors:** Itamar Hadad, Guy Katz, Shahaf Bassan
142	- **Year:** 2026
143	- **Venue:** ICLR 2026
144	- **Core findings:** Leverages neural network verification to yield circuits with provable guarantees: input domain robustness, robust patching, and minimality. Prior methods depend on heuristics without guarantees over continuous input domains. Applied to vision models.
145	- **Relation to CSS:** **互补 (Complementary)**. Takes a formal verification approach to robustness; CSS takes an empirical consensus approach. Both address circuit reliability but through fundamentally different mechanisms. Currently limited to vision models.
146	
147	### 4.5 Efficient Automated Circuit Discovery in Transformers using Contextual Decomposition (CD-T)
148	- **Authors:** Adelaide Hsu et al.
149	- **Year:** 2025
150	- **Venue:** ICLR 2025
151	- **Core findings:** Uses mathematical decomposition (no approximations) for circuit discovery. Reduces runtime from hours to seconds vs ACDC. Achieves 97% ROC AUC on IOI, Greater-Than, and Docstring tasks. Compatible with all transformer types, no training required.
152	- **Relation to CSS:** **互补 (Complementary)**. Provides yet another discovery method with different inductive biases than EAP-IG/EP/ACDC—could be a candidate additional method for CSS's ensemble.
153	
154	### 4.6 Towards Automated Circuit Discovery for Mechanistic Interpretability (ACDC)
155	- **Authors:** Arthur Conmy, Augustine N. Mavor-Parker, Aaquib Lynch, Stefan Heimersheim, Adrià Garriga-Alonso
156	- **Year:** 2023
157	- **Venue:** NeurIPS 2023
158	- **Core findings:** Foundational automated circuit discovery method using iterative activation patching. Effective but slow (runtime scales linearly with edges). Recovers IOI, Greater-Than, Docstring circuits. Establishes benchmark tasks for circuit discovery evaluation.
159	- **Relation to CSS:** **基础方法 (Foundational method)**. ACDC is one of CSS's three discovery methods for GPT-2 Small. Its different algorithmic approach (iterative patching vs. gradient-based) provides genuine method diversity in CSS's ensemble.
160	
161	---
162	
163	## Additional Relevant Work
164	
165	### RelP: Faithful and Efficient Circuit Discovery via Relevance Patching
166	- **Authors:** Farnoush Rezaei Jafari et al.
167	- **Year:** 2025
168	- **Venue:** NeurIPS 2025 MechInterp Workshop (Spotlight)
169	- **Core findings:** Replaces gradients in attribution patching with LRP propagation coefficients. For MLP outputs in GPT-2 Large, attribution patching achieves Pearson correlation 0.006 vs. RelP's 0.956 with activation patching ground truth. Faithfulness comparable to IG at lower cost.
170	- **Relation to CSS:** **互补 (Complementary)**. Another discovery method with different inductive bias. Documents dramatic differences between methods on the same components—supports CSS's premise.
171	
172	### PIE: A Cross-Layer Transcoder-Native Framework for Efficient Circuit Discovery via Feature Attribution
173	- **Authors:** Qinhao Chen, Linyang He, Nima Mesgarani
174	- **Year:** 2026 (arXiv: 2604.16889)
175	- **Venue:** arXiv preprint (April 2026)
176	- **Core findings:** First CLT-native end-to-end circuit discovery framework. Feature Attribution Patching (FAP) scores CLT features by gradient-weighted write contributions; FAP-Synergy adds synergy-aware reranking. Evaluated with KL-divergence behavior retention and FADE-style metrics.
177	- **Relation to CSS:** **互补 (Complementary)**. Operates at the feature level via cross-layer transcoders rather than at the component/edge level. As CLT/transcoder methods become standard, PIE represents a potential additional discovery method for CSS's ensemble, bridging component-level and feature-level consensus.
178	
179	### EAP-GP: Mitigating Saturation Effect in Gradient-based Automated Circuit Identification
180	- **Authors:** arXiv: 2502.06852
181	- **Year:** 2025
182	- **Venue:** arXiv preprint (Feb 2025)
183	- **Core findings:** Addresses gradient saturation in Edge Attribution Patching by proposing a gradient propagation fix for more accurate edge importance scoring. Improves upon EAP/EAP-IG in faithfulness for circuits where saturation artifacts degrade standard gradient estimates.
184	- **Relation to CSS:** **互补 (Complementary)**. Another intra-family gradient variant alongside EAP, EAP-IG. The proliferation of EAP variants (EAP → EAP-IG → EAP-GP) illustrates intra-family variation driven by specific failure modes—CSS's value lies in cross-family agreement that transcends these intra-family fixes.
185	
186	### GIM: Improved Interpretability for Large Language Models
187	- **Authors:** Corti team
188	- **Year:** 2025 (arXiv: 2505.17630)
189	- **Venue:** arXiv preprint (May 2025)
190	- **Core findings:** Gradient Interaction Modifications — gradient-based circuit discovery method that tops the HuggingFace Mechanistic Interpretability Benchmark. Outperforms other methods in early layers; Integrated Gradients performs better in middle/late layers, suggesting layer-dependent method strengths.
191	- **Relation to CSS:** **互补 (Complementary)**. Strong single-method baseline. The finding that different gradient methods excel in different layers directly motivates cross-method consensus: no single method dominates across all model components. A potential candidate for inclusion in CSS's method ensemble.
192	
193	---
194	
195	## Key Takeaways for CSS Positioning
196	
197	### 1. CSS fills a specific gap in the literature
198	The field has established that (a) circuit discovery methods disagree (Syed et al. 2024; Méloux et al. 2025), (b) faithfulness metrics are unreliable (Miller et al. 2024), and (c) circuits are sensitive to analyst choices (CIRCUS, Certified Circuits). CSS is the first to exploit **cross-method binary consensus** as a robustness mechanism, using method diversity rather than threshold/data perturbation diversity.
199	
200	### 2. CIRCUS and Mondorf et al. are the primary competitors — positioning is critical
201	Two closest works, each with distinct limitations:
202	- **CIRCUS (Parekh, 2026):** varies pruning thresholds within one attribution method → threshold robustness within a single algorithm family
203	- **Mondorf et al. (2510.06811):** ensembles EAP-IG + Edge Pruning via score averaging → cross-method but limited to gradient-family methods only, no binary consensus
204	- **CSS:** uses multiple independent discovery methods spanning different algorithm families (gradient-based, iterative patching, mask optimization) → true cross-family method robustness with binary consensus
205	- CSS argument: method diversity across algorithm families captures a broader space of inductive biases than either threshold variation (CIRCUS) or intra-family score averaging (Mondorf). CIRCUS inherits the blind spots of its single underlying method; Mondorf stays within the gradient family. CSS's methods have structurally different failure modes, and binary consensus avoids score calibration issues.
206	
207	### 3. The "instability problem" is well-documented — CSS offers a practical solution
208	Multiple papers (Méloux et al., Franco et al., Miller et al.) document that circuits are unstable across data, prompts, and methodology. The Open Problems paper (Sharkey et al. 2025) explicitly calls for reporting ensembles. CSS directly operationalizes this recommendation with a concrete, lightweight algorithm.
209	
210	### 4. Binary scoring is underexplored relative to continuous scoring
211	Most methods produce continuous importance scores (EAP, EAP-IG, CD-T) and require threshold selection. Edge Pruning uses binary masks but within a single optimization. CSS's binary consensus (edge included/excluded per method → majority vote) is a distinct aggregation strategy that avoids score calibration issues across methods with incomparable scales.
212	
213	### 5. Distribution-shift robustness is a planned novel evaluation angle
214	No existing work systematically evaluates whether consensus circuits maintain faithfulness under distribution shift. CSS 计划在 Phase 2 中系统性评估 consensus circuits 在分布偏移下的鲁棒性（off-diagonal evaluation: train on distribution A, test on distribution B），这将成为一个独特的贡献方向（Phase 2 planned, cf. D015）。
215	
216	### 6. Recommended related work structure for the paper
217	1. **Circuit discovery methods** (ACDC, EAP-IG, EP, CD-T, HAP) — establish method landscape
218	2. **Faithfulness evaluation** (Miller et al. 2024, Hanna et al. 2024) — motivate robustness concerns
219	3. **Circuit instability** (Méloux et al. 2025, Franco et al. 2026, Sun 2025) — establish the problem CSS solves
220	4. **Consensus/stability approaches** (CIRCUS, Mondorf et al., Certified Circuits) — position CSS against alternatives
221	5. **Feature-level circuits** (Sparse Feature Circuits, Transcoders, Circuit Tracing, PIE) — acknowledge parallel direction, note CSS works at component level
222	6. **Method variants and benchmarks** (EAP-GP, GIM, MIB) — contextualize method landscape diversity that motivates cross-family consensus
223	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4ae1b15d-cec4-425f-88a1-f3a46efeab38",
  "isSidechain": false,
  "promptId": "16c2e1a1-23bf-4ab8-bc32-4fa92e1b898b",
  "type": "user",
  "uuid": "2421dd8b-aa4e-4662-9209-e3ee2cc60da1",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/_project/report/literature_survey_related_work.md",
      "content": "# Related Work Literature Survey for CSS (Cross-method Structural Consensus)\n\n> Generated: 2026-05-13 | Target: EMNLP 2026 Main (ARR deadline 2026-05-25)\n\n---\n\n## Direction 1: Cross-method Consensus / Ensemble in Mechanistic Interpretability\n\n### 1.1 CIRCUS: Circuit Consensus under Uncertainty via Stability Ensembles\n- **Authors:** Swapnil Parekh\n- **Year:** 2026 (arXiv: 2603.00523)\n- **Venue:** arXiv preprint (Feb 2026)\n- **Core findings:** Reframes circuit discovery as an uncertainty-quantification problem. Constructs an ensemble of attribution graphs by pruning a *single* raw attribution run under multiple threshold configurations, assigns each edge a stability score (fraction of configs retaining it), and extracts a strict-consensus circuit (edges appearing in all views). On Gemma-2-2B and Llama-3.2-1B, strict consensus circuits are ~40× smaller than the union while retaining comparable explanatory power. Consensus-identified nodes beat matched non-consensus controls in causal relevance (p=0.0004).\n- **Relation to CSS:** **直接竞争 (Primary competitor)**. CIRCUS varies pruning thresholds on a single attribution method to build consensus; CSS uses multiple independent discovery methods (EAP-IG, EP, ACDC/IFR). Key differentiators: (1) CSS captures cross-method agreement (different algorithms with different inductive biases), not just threshold robustness within one method; (2) CSS uses binary agreement rather than fractional stability scores; (3) CSS explicitly tests distribution-shift robustness. Must position CSS as complementary/stronger: method diversity > threshold diversity.\n\n### 1.2 Certified Circuits: Stability Guarantees for Mechanistic Circuits\n- **Authors:** Alaa Anani, Tobias Lorenz, Bernt Schiele, et al.\n- **Year:** 2026 (arXiv: 2602.22968)\n- **Venue:** arXiv preprint (Feb 2026)\n- **Core findings:** Wraps any black-box discovery algorithm with randomized data subsampling to certify that circuit component inclusion decisions are invariant to bounded edit-distance perturbations of the concept dataset. On ImageNet with ResNet-101, certified circuits achieved 96% accuracy vs 86% baseline using half the neurons. Addresses dataset-to-circuit instability.\n- **Relation to CSS:** **互补 (Complementary)**. Certified Circuits focuses on data perturbation stability for vision models with formal guarantees; CSS focuses on method-agreement stability for language model circuits. Both address instability but from orthogonal angles. Could cite as motivation for why stability matters.\n\n### 1.3 Open Problems in Mechanistic Interpretability\n- **Authors:** Lee Sharkey, Bilal Chughtai, Joshua Batson, et al. (29 authors, 18 organizations)\n- **Year:** 2025 (arXiv: 2501.16496)\n- **Venue:** arXiv preprint (Jan 2025), commissioned by Schmidt Sciences\n- **Core findings:** Landmark collaborative paper establishing the field's consensus open problems. Highlights systematic non-identifiability: multiple circuits, features, and algorithm mappings can yield the same behavioral fidelity. Advocates reporting explanation ensembles and clarifying pragmatic vs. unicity criteria.\n- **Relation to CSS:** **支持 (Supports CSS)**. Directly motivates multi-method consensus: if circuits are non-unique, reporting ensembles and agreement is essential. CSS operationalizes this recommendation.\n\n### 1.4 Circuit Tracing: Revealing Computational Graphs in Language Models\n- **Authors:** Anthropic (Dario Amodei team)\n- **Year:** 2025\n- **Venue:** Anthropic Technical Report (March 2025)\n- **Core findings:** Uses cross-layer transcoders to build attribution graphs—graphical representations of computational steps where nodes are features and edges are causal interactions. Open-sourced circuit tracing tools supporting Gemma-2-2B, Llama-3.1-1B, Qwen3-4B.\n- **Relation to CSS:** **互补 (Complementary)**. Provides a different paradigm (feature-level circuits via transcoders vs. component-level circuits). CSS methods operate at edge/component level; circuit tracing works at feature level. Represents a parallel direction worth acknowledging.\n\n### 1.5 Exploring Ensemble Strategies for Circuit Localization Methods (Mondorf et al.)\n- **Authors:** Mondorf, Wang et al.\n- **Year:** 2025 (arXiv: 2510.06811)\n- **Venue:** BlackboxNLP 2025 (Workshop short paper, MIB Shared Task)\n- **Core findings:** Explores parallel ensembling (averaging/min/max of attribution scores across methods) and sequential ensembling (EAP-IG warm-start then Edge Pruning refinement) for circuit localization. Parallel ensemble over all variants achieves best CMD=0.03, CPR=1.83 on the MIB leaderboard.\n- **Relation to CSS:** **直接竞争 (Direct competitor — limited scope)**. The closest existing work to cross-method circuit ensembling, but with critical limitations: (1) **仅限 gradient 族方法**: only combines EAP-IG and Edge Pruning, both gradient-based edge attribution methods from the same algorithmic family — no causal/mask-based methods (e.g., ACDC) included; (2) **Score averaging 而非 binary consensus**: uses simple score aggregation (avg/min/max) rather than principled binary agreement, inheriting score calibration issues across methods with incomparable scales; (3) **无 consensus 理论框架**: no analysis of method agreement patterns, confidence scoring, or consensus circuit properties; (4) **Workshop short paper 规模**: limited evaluation scope compared to CSS's full pipeline. CSS goes beyond by spanning algorithm families (gradient-based vs. iterative patching vs. mask optimization), providing binary consensus with confidence scoring, and analyzing consensus circuit properties (size, faithfulness, robustness).\n\n---\n\n## Direction 2: Circuit Faithfulness Evaluation\n\n### 2.1 Transformer Circuit Faithfulness Metrics Are Not Robust\n- **Authors:** Joseph Miller, Bilal Chughtai, William Saunders\n- **Year:** 2024\n- **Venue:** COLM 2024\n- **Core findings:** Faithfulness scores are highly sensitive to seemingly insignificant ablation methodology choices. Edge-level vs node-level ablation, resample vs mean ablation, and other methodological variations yield substantially different faithfulness percentages. Existing circuit faithfulness scores reflect researcher methodology as much as actual circuit quality.\n- **Relation to CSS:** **强支持 (Strongly supports CSS)**. Core motivation for CSS: if single-method faithfulness metrics are unreliable, cross-method agreement provides a more robust signal. Directly supports the claim that binary consensus is more stable than score-dependent evaluation.\n\n### 2.2 Have Faith in Faithfulness: Going Beyond Circuit Overlap When Finding Model Mechanisms\n- **Authors:** Michael Hanna, Sandro Pezzelle, Yonatan Belinkov\n- **Year:** 2024\n- **Venue:** COLM 2024 (also ICML 2024 MI Workshop Spotlight)\n- **Core findings:** Introduces EAP-IG (EAP with integrated gradients) which finds more faithful circuits than EAP. Key finding: high node overlap ≠ high faithfulness. When comparing circuits, measuring overlap is no substitute for measuring faithfulness.\n- **Relation to CSS:** **支持+基础方法 (Supports + foundational method)**. EAP-IG is one of CSS's three discovery methods. The finding that overlap ≠ faithfulness motivates CSS's use of faithfulness-based evaluation rather than simple circuit overlap metrics.\n\n### 2.3 MIB: A Mechanistic Interpretability Benchmark\n- **Authors:** Yoav Goldberg, Yonatan Belinkov, et al.\n- **Year:** 2025–2026 (arXiv: 2504.13151)\n- **Venue:** ICML 2025 / ICLR 2026\n- **Core findings:** Establishes two evaluation tracks—circuit localization and causal variable localization—across diverse tasks and models. Attribution and mask optimization methods perform best on circuit localization. Supervised DAS significantly outperforms unsupervised SAE features for causal variable localization.\n- **Relation to CSS:** **互补 (Complementary)**. Provides standardized evaluation framework. CSS could adopt MIB tasks/metrics for evaluation; MIB results contextualize method performance differences.\n\n### 2.4 Functional Faithfulness in the Wild: Circuit Discovery with Differentiable Computation Graph Pruning\n- **Authors:** Lei Yu, Jingcheng Niu, Zining Zhu, et al.\n- **Year:** 2024 (arXiv: 2407.03779)\n- **Venue:** arXiv preprint (July 2024)\n- **Core findings:** Introduces DiscoGP—differentiable masking that prunes both weights and edges. Extracts sheaves preserving 93–100% model performance using only 1–7% of original weights/connections. Identifies that activation-patching-based circuits tend to be neither functionally faithful nor complete.\n- **Relation to CSS:** **互补 (Complementary)**. Shows that weight+edge pruning yields more faithful circuits than edge-only approaches, further highlighting that methodology choices dramatically affect circuit quality—supporting CSS's cross-method approach.\n\n---\n\n## Direction 3: Binary vs Continuous Scoring in Circuit Discovery\n\n### 3.1 Finding Transformer Circuits with Edge Pruning\n- **Authors:** Adithya Bhaskar, Alexander Wettig, Dan Friedman, et al.\n- **Year:** 2024\n- **Venue:** NeurIPS 2024\n- **Core findings:** Frames circuit discovery as gradient-based optimization with binary masks over edges. EP is considerably more faithful on IOI and Greater-Than than both ACDC and EAP, especially at higher sparsities. Scales effectively to 100K examples where it is fastest and most faithful.\n- **Relation to CSS:** **基础方法+支持 (Foundational method + supports)**. EP is one of CSS's discovery methods. Uses binary masks (0/1) for edge inclusion—directly relevant to CSS's binary consensus. Shows binary edge selection can be highly faithful.\n\n### 3.2 Attribution Patching Outperforms Automated Circuit Discovery\n- **Authors:** Aaquib Syed, Can Rager, Arthur Conmy\n- **Year:** 2024\n- **Venue:** BlackboxNLP 2024 (NeurIPS Workshop)\n- **Core findings:** A simple method based on attribution patching outperforms ACDC while requiring just two forward passes + one backward pass. However, EAP's first-order approximations show lower faithfulness to the full model than EP.\n- **Relation to CSS:** **支持 (Supports)**. Documents that different methods (ACDC, EAP, EP) yield different circuits with different faithfulness levels—core motivation for cross-method consensus. Methods that are fast (EAP) and methods that are faithful (EP) produce systematically different results.\n\n### 3.3 Discovering Transformer Circuits via a Hybrid Attribution and Pruning Framework (HAP)\n- **Authors:** Adithya Bhaskar, Alexander Wettig, et al.\n- **Year:** 2025 (arXiv: 2510.03282)\n- **Venue:** NeurIPS 2025\n- **Core findings:** Two-stage pipeline: EAP filters unimportant edges (continuous scores → top-k), then EP refines with binary masks. HAP is ≥46% faster than EP while maintaining high faithfulness. Preserves cooperative circuit components (e.g., S-inhibition heads) that EAP alone prunes at high sparsity.\n- **Relation to CSS:** **互补 (Complementary)**. Shows that combining methods sequentially (EAP→EP) improves over either alone. CSS takes a different combination approach: run methods independently, then take binary consensus. Complementary philosophies of method combination.\n\n### 3.4 Sparse Feature Circuits: Discovering and Editing Interpretable Causal Graphs in Language Models\n- **Authors:** Samuel Marks, Can Rager, Eric Michaud, Yonatan Belinkov, David Bau, Aaron Mueller\n- **Year:** 2025\n- **Venue:** ICLR 2025 (Oral)\n- **Core findings:** Uses SAEs to identify features, then discovers feature-level causal circuits. Small feature circuits (<100 nodes) explain a large proportion of model performance on subject-verb agreement. Introduces SHIFT for improving classifier generalization by ablating task-irrelevant features.\n- **Relation to CSS:** **互补 (Complementary)**. Operates at feature level (SAE features) vs. CSS's component level (attention heads, MLPs). Shows that sparse/binary feature selection is powerful for circuit analysis. CSS could potentially extend to feature-level consensus in future work.\n\n### 3.5 Transcoders Find Interpretable LLM Feature Circuits\n- **Authors:** Jacob Dunefsky, Philippe Morel, et al.\n- **Year:** 2024\n- **Venue:** NeurIPS 2024\n- **Core findings:** Transcoders approximate dense MLP layers with wider, sparsely-activating layers. On par with SAEs in sparsity, faithfulness, and interpretability. Applied to reverse-engineer circuits in GPT-2-small including novel insights on the greater-than circuit.\n- **Relation to CSS:** **互补 (Complementary)**. Offers alternative circuit representation (feature-level via transcoders). Relevant as a potential additional discovery method for CSS.\n\n---\n\n## Direction 4: Instability / Unreliability of Single-method Circuit Discovery\n\n### 4.1 Mechanistic Interpretability as Statistical Estimation: A Variance Analysis\n- **Authors:** Maxime Méloux et al.\n- **Year:** 2025–2026 (arXiv: 2510.00845, revised Feb 2026)\n- **Venue:** arXiv preprint\n- **Core findings:** Frames circuit discovery as a statistical estimation problem. Uncovers fundamental instability: single-input CMA scores exhibit high intrinsic variance—causal effects are volatile random variables, not fixed properties. Small perturbations in input data or hyperparameters yield vastly different circuits. Focuses on EAP and EAP-IG, systematically decomposing variance sources.\n- **Relation to CSS:** **强支持 (Strongly supports CSS)**. Provides quantitative evidence that single-method circuits are unstable. Directly motivates CSS: if individual methods have high variance, cross-method consensus filters out method-specific noise.\n\n### 4.2 Circuit Stability Characterizes Language Model Generalization\n- **Authors:** Alan Sun\n- **Year:** 2025\n- **Venue:** ACL 2025\n- **Core findings:** Mathematically formalizes circuit stability—a model's ability to apply a consistent reasoning process (circuit) across inputs. Through three case studies, shows circuit stability predicts different aspects of generalization. Models that lack circuit stability fail to generalize.\n- **Relation to CSS:** **支持 (Supports)**. Establishes that circuit stability is a valuable property. CSS targets a complementary notion of stability: consistency across methods rather than across inputs.\n\n### 4.3 Finding Highly Interpretable Prompt-Specific Circuits in Language Models\n- **Authors:** Gabriel Franco, Lucas M. Tassis, Azalea Rohr, Mark Crovella\n- **Year:** 2026 (arXiv: 2602.13483)\n- **Venue:** arXiv preprint (Feb 2026)\n- **Core findings:** Circuits are prompt-specific even within a fixed task. Applying ACC++ to IOI in GPT-2, Pythia, and Gemma 2: no single circuit for IOI in any model—different prompt templates induce systematically different mechanisms.\n- **Relation to CSS:** **支持+挑战 (Supports + challenges)**. Supports CSS by showing single circuits are insufficient; challenges CSS to demonstrate that consensus circuits are more stable across prompts. CSS should test prompt-level robustness.\n\n### 4.4 Formal Mechanistic Interpretability: Automated Circuit Discovery with Provable Guarantees\n- **Authors:** Itamar Hadad, Guy Katz, Shahaf Bassan\n- **Year:** 2026\n- **Venue:** ICLR 2026\n- **Core findings:** Leverages neural network verification to yield circuits with provable guarantees: input domain robustness, robust patching, and minimality. Prior methods depend on heuristics without guarantees over continuous input domains. Applied to vision models.\n- **Relation to CSS:** **互补 (Complementary)**. Takes a formal verification approach to robustness; CSS takes an empirical consensus approach. Both address circuit reliability but through fundamentally different mechanisms. Currently limited to vision models.\n\n### 4.5 Efficient Automated Circuit Discovery in Transformers using Contextual Decomposition (CD-T)\n- **Authors:** Adelaide Hsu et al.\n- **Year:** 2025\n- **Venue:** ICLR 2025\n- **Core findings:** Uses mathematical decomposition (no approximations) for circuit discovery. Reduces runtime from hours to seconds vs ACDC. Achieves 97% ROC AUC on IOI, Greater-Than, and Docstring tasks. Compatible with all transformer types, no training required.\n- **Relation to CSS:** **互补 (Complementary)**. Provides yet another discovery method with different inductive biases than EAP-IG/EP/ACDC—could be a candidate additional method for CSS's ensemble.\n\n### 4.6 Towards Automated Circuit Discovery for Mechanistic Interpretability (ACDC)\n- **Authors:** Arthur Conmy, Augustine N. Mavor-Parker, Aaquib Lynch, Stefan Heimersheim, Adrià Garriga-Alonso\n- **Year:** 2023\n- **Venue:** NeurIPS 2023\n- **Core findings:** Foundational automated circuit discovery method using iterative activation patching. Effective but slow (runtime scales linearly with edges). Recovers IOI, Greater-Than, Docstring circuits. Establishes benchmark tasks for circuit discovery evaluation.\n- **Relation to CSS:** **基础方法 (Foundational method)**. ACDC is one of CSS's three discovery methods for GPT-2 Small. Its different algorithmic approach (iterative patching vs. gradient-based) provides genuine method diversity in CSS's ensemble.\n\n---\n\n## Additional Relevant Work\n\n### RelP: Faithful and Efficient Circuit Discovery via Relevance Patching\n- **Authors:** Farnoush Rezaei Jafari et al.\n- **Year:** 2025\n- **Venue:** NeurIPS 2025 MechInterp Workshop (Spotlight)\n- **Core findings:** Replaces gradients in attribution patching with LRP propagation coefficients. For MLP outputs in GPT-2 Large, attribution patching achieves Pearson correlation 0.006 vs. RelP's 0.956 with activation patching ground truth. Faithfulness comparable to IG at lower cost.\n- **Relation to CSS:** **互补 (Complementary)**. Another discovery method with different inductive bias. Documents dramatic differences between methods on the same components—supports CSS's premise.\n\n### PIE: A Cross-Layer Transcoder-Native Framework for Efficient Circuit Discovery via Feature Attribution\n- **Authors:** Qinhao Chen, Linyang He, Nima Mesgarani\n- **Year:** 2026 (arXiv: 2604.16889)\n- **Venue:** arXiv preprint (April 2026)\n- **Core findings:** First CLT-native end-to-end circuit discovery framework. Feature Attribution Patching (FAP) scores CLT features by gradient-weighted write contributions; FAP-Synergy adds synergy-aware reranking. Evaluated with KL-divergence behavior retention and FADE-style metrics.\n- **Relation to CSS:** **互补 (Complementary)**. Operates at the feature level via cross-layer transcoders rather than at the component/edge level. As CLT/transcoder methods become standard, PIE represents a potential additional discovery method for CSS's ensemble, bridging component-level and feature-level consensus.\n\n### EAP-GP: Mitigating Saturation Effect in Gradient-based Automated Circuit Identification\n- **Authors:** arXiv: 2502.06852\n- **Year:** 2025\n- **Venue:** arXiv preprint (Feb 2025)\n- **Core findings:** Addresses gradient saturation in Edge Attribution Patching by proposing a gradient propagation fix for more accurate edge importance scoring. Improves upon EAP/EAP-IG in faithfulness for circuits where saturation artifacts degrade standard gradient estimates.\n- **Relation to CSS:** **互补 (Complementary)**. Another intra-family gradient variant alongside EAP, EAP-IG. The proliferation of EAP variants (EAP → EAP-IG → EAP-GP) illustrates intra-family variation driven by specific failure modes—CSS's value lies in cross-family agreement that transcends these intra-family fixes.\n\n### GIM: Improved Interpretability for Large Language Models\n- **Authors:** Corti team\n- **Year:** 2025 (arXiv: 2505.17630)\n- **Venue:** arXiv preprint (May 2025)\n- **Core findings:** Gradient Interaction Modifications — gradient-based circuit discovery method that tops the HuggingFace Mechanistic Interpretability Benchmark. Outperforms other methods in early layers; Integrated Gradients performs better in middle/late layers, suggesting layer-dependent method strengths.\n- **Relation to CSS:** **互补 (Complementary)**. Strong single-method baseline. The finding that different gradient methods excel in different layers directly motivates cross-method consensus: no single method dominates across all model components. A potential candidate for inclusion in CSS's method ensemble.\n\n---\n\n## Key Takeaways for CSS Positioning\n\n### 1. CSS fills a specific gap in the literature\nThe field has established that (a) circuit discovery methods disagree (Syed et al. 2024; Méloux et al. 2025), (b) faithfulness metrics are unreliable (Miller et al. 2024), and (c) circuits are sensitive to analyst choices (CIRCUS, Certified Circuits). CSS is the first to exploit **cross-method binary consensus** as a robustness mechanism, using method diversity rather than threshold/data perturbation diversity.\n\n### 2. CIRCUS and Mondorf et al. are the primary competitors — positioning is critical\nTwo closest works, each with distinct limitations:\n- **CIRCUS (Parekh, 2026):** varies pruning thresholds within one attribution method → threshold robustness within a single algorithm family\n- **Mondorf et al. (2510.06811):** ensembles EAP-IG + Edge Pruning via score averaging → cross-method but limited to gradient-family methods only, no binary consensus\n- **CSS:** uses multiple independent discovery methods spanning different algorithm families (gradient-based, iterative patching, mask optimization) → true cross-family method robustness with binary consensus\n- CSS argument: method diversity across algorithm families captures a broader space of inductive biases than either threshold variation (CIRCUS) or intra-family score averaging (Mondorf). CIRCUS inherits the blind spots of its single underlying method; Mondorf stays within the gradient family. CSS's methods have structurally different failure modes, and binary consensus avoids score calibration issues.\n\n### 3. The \"instability problem\" is well-documented — CSS offers a practical solution\nMultiple papers (Méloux et al., Franco et al., Miller et al.) document that circuits are unstable across data, prompts, and methodology. The Open Problems paper (Sharkey et al. 2025) explicitly calls for reporting ensembles. CSS directly operationalizes this recommendation with a concrete, lightweight algorithm.\n\n### 4. Binary scoring is underexplored relative to continuous scoring\nMost methods produce continuous importance scores (EAP, EAP-IG, CD-T) and require threshold selection. Edge Pruning uses binary masks but within a single optimization. CSS's binary consensus (edge included/excluded per method → majority vote) is a distinct aggregation strategy that avoids score calibration issues across methods with incomparable scales.\n\n### 5. Distribution-shift robustness is a planned novel evaluation angle\nNo existing work systematically evaluates whether consensus circuits maintain faithfulness under distribution shift. CSS 计划在 Phase 2 中系统性评估 consensus circuits 在分布偏移下的鲁棒性（off-diagonal evaluation: train on distribution A, test on distribution B），这将成为一个独特的贡献方向（Phase 2 planned, cf. D015）。\n\n### 6. Recommended related work structure for the paper\n1. **Circuit discovery methods** (ACDC, EAP-IG, EP, CD-T, HAP) — establish method landscape\n2. **Faithfulness evaluation** (Miller et al. 2024, Hanna et al. 2024) — motivate robustness concerns\n3. **Circuit instability** (Méloux et al. 2025, Franco et al. 2026, Sun 2025) — establish the problem CSS solves\n4. **Consensus/stability approaches** (CIRCUS, Mondorf et al., Certified Circuits) — position CSS against alternatives\n5. **Feature-level circuits** (Sparse Feature Circuits, Transcoders, Circuit Tracing, PIE) — acknowledge parallel direction, note CSS works at component level\n6. **Method variants and benchmarks** (EAP-GP, GIM, MIB) — contextualize method landscape diversity that motivates cross-family consensus\n",
      "numLines": 223,
      "startLine": 1,
      "totalLines": 223
    }
  },
  "sourceToolAssistantUUID": "4ae1b15d-cec4-425f-88a1-f3a46efeab38",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context",
  "sessionId": "f2480f86-9e1e-4510-980e-6abe201dd7a7",
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
  "leafUuid": "2421dd8b-aa4e-4662-9209-e3ee2cc60da1",
  "sessionId": "f2480f86-9e1e-4510-980e-6abe201dd7a7"
}
```

---

### Runtime record

_source line 47_

```json
{
  "type": "ai-title",
  "aiTitle": "Merge literature files and fix survey takeaway",
  "sessionId": "f2480f86-9e1e-4510-980e-6abe201dd7a7"
}
```

---

### Assistant

_source line 48 · 2026-05-13T02:22:33.706Z_

文件完整且格式正确。总结：

---

### 新增条目（4 篇）

| 论文 | 位置 | 类型 |
|------|------|------|
| **Mondorf et al. (2510.06811)** | §1.5 (Direction 1) | 直接竞争，详细讨论 4 点局限 |
| **PIE (2604.16889)** | Additional Relevant Work | 互补，CLT-native 方法 |
| **EAP-GP (2502.06852)** | Additional Relevant Work | 互补，gradient 族变体 |
| **GIM (2505.17630)** | Additional Relevant Work | 互补，MIB 顶分方法 |

### 修改条目

- **Takeaway #2**: 从仅讨论 CIRCUS 扩展为同时讨论 CIRCUS + Mondorf et al. 两个竞争者
- **Takeaway #6**: 新增第 4 项加入 Mondorf et al.，第 5 项加入 PIE，新增第 6 项 "Method variants and benchmarks"

### Takeaway #5 修改前后

**修改前：**
> Distribution-shift robustness is a novel evaluation angle — No existing work systematically evaluates whether consensus circuits maintain faithfulness under distribution shift. CSS's off-diagonal evaluation (train on distribution A, test on distribution B) is a distinctive contribution.

**修改后：**
> Distribution-shift robustness is a **planned** novel evaluation angle — No existing work systematically evaluates whether consensus circuits maintain faithfulness under distribution shift. CSS 计划在 Phase 2 中系统性评估 consensus circuits 在分布偏移下的鲁棒性（off-diagonal evaluation: train on distribution A, test on distribution B），这将成为一个独特的贡献方向（Phase 2 planned, cf. D015）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2421dd8b-aa4e-4662-9209-e3ee2cc60da1",
  "isSidechain": false,
  "requestId": "req_011Caymgiu6nQNZGQP9TnGHx",
  "type": "assistant",
  "uuid": "e0308ae8-bf03-4ff8-bf23-8cf831544d48",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context",
  "sessionId": "f2480f86-9e1e-4510-980e-6abe201dd7a7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011Sz9GzQTWM912SYJ2i8vNr",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6871,
      "cache_read_input_tokens": 38023,
      "output_tokens": 500,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 6871,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 500,
          "cache_read_input_tokens": 38023,
          "cache_creation_input_tokens": 6871,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 6871
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

_source line 49_

```json
{
  "type": "last-prompt",
  "leafUuid": "e0308ae8-bf03-4ff8-bf23-8cf831544d48",
  "sessionId": "f2480f86-9e1e-4510-980e-6abe201dd7a7"
}
```

---

### Runtime record

_source line 50_

```json
{
  "type": "ai-title",
  "aiTitle": "Merge literature files and fix survey takeaway",
  "sessionId": "f2480f86-9e1e-4510-980e-6abe201dd7a7"
}
```

---
